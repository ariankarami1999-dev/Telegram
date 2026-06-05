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
<img src="https://cdn4.telesco.pe/file/pAOfAhPescjWXlVXVusE6LBGN2pif_OUhruW9FKiLYXjNTaVKpID9h37MRICjH2KPklEiNUpKMgFc38Zf9A9X8i48RNToYqCxQECocyMNtsDUWI0s_nhu_4_YTwZWnULe0AXi3AR_aJDc8Q6ts-5LZrpFjRVLBPa7eDZd1uqMzcbBTNaBFKsgIx7A2JeajF8Nxzl5qTKp_Hw2CzoTYW4d9_OPyC1oa62umhGx5ksOtTBVW2U4BbY9IK8y9OCL1eMpnYTwOQeAvQSJdZ8z-syYn5lcw1BKWEeOUxpSXMwK0yQ_ayxYp1zIghsNv0BkuRsQtw1TUJ3hsu7SWLYz7aAcw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.21M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforii</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-15 20:29:14</div>
<hr>

<div class="tg-post" id="msg-656413">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">♦️
پوتین: مسکو معتقد نیست ایران به‌دنبال سلاح هسته‌ای است
🔹
رئیس‌جمهور روسیه با حمایت از توقف اقدامات نظامی علیه ایران گفت مسکو نشانه‌ای از تحریک از سوی تهران نمی‌بیند و معتقد نیست ایران به‌دنبال سلاح هسته‌ای است.
🔹
پوتین همچنین از آمادگی روسیه برای دریافت اورانیوم غنی‌شده ایران و ادامه رایزنی با آمریکا، ایران و اسرائیل برای کاهش تنش‌ها خبر داد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/akhbarefori/656413" target="_blank">📅 20:23 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656412">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0e3968f346.mp4?token=C3Oen8UJXCO48Gh9rtXw174isNKfgI9FD61s-QyHZ3XNmGs1lJ1ljZU167hwtlp5YntXOyPvL2oMrLaAKrK8dfL0TEIq0Uw--cJp09DFrqIWHwZ47eif1jzZUNxWJalhjjnN3C3PttfHIJ1gRPZJ18isrQMA0WNTD1phqLRAC7s-DsiSIqt9_97SEOECIKWozSmQC173bg-J5jDuUzitu570je37S6Ll3GeekbjOSz_aZaHPkXgN5ustiCF06mRUNeDf1DTRJEVYq750uWmR8CdyVenyfPkkhAsL6ptCCy1WbVpmqFdM0SL_I4JuJdQfNlcQCapyWoxYv7ZPMiofuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0e3968f346.mp4?token=C3Oen8UJXCO48Gh9rtXw174isNKfgI9FD61s-QyHZ3XNmGs1lJ1ljZU167hwtlp5YntXOyPvL2oMrLaAKrK8dfL0TEIq0Uw--cJp09DFrqIWHwZ47eif1jzZUNxWJalhjjnN3C3PttfHIJ1gRPZJ18isrQMA0WNTD1phqLRAC7s-DsiSIqt9_97SEOECIKWozSmQC173bg-J5jDuUzitu570je37S6Ll3GeekbjOSz_aZaHPkXgN5ustiCF06mRUNeDf1DTRJEVYq750uWmR8CdyVenyfPkkhAsL6ptCCy1WbVpmqFdM0SL_I4JuJdQfNlcQCapyWoxYv7ZPMiofuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
محسن رضایی به سی‌ان‌ان: آیت الله خامنه‌ای با ترامپ دیدار نخواهد کرد؛ آقای ترامپ مذاکرات را به بن‌بست کشانده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 7.44K · <a href="https://t.me/akhbarefori/656412" target="_blank">📅 20:10 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656411">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">♦️
رویترز مدعی تهیه پیش‌نویس قطعنامه‌ علیه ایران در آژانس از سوی آمریکا شد
رویترز:
🔹
ایالات متحده در آستانه نشست هفته آینده شورای حکام آژانس بین‌المللی انرژی اتمی، در حال آماده‌سازی پیش‌نویس قطعنامه‌ای برای محکوم کردن ایران است.
🔹
این در حالی است که تهران و واشنگتن در حال گفت‌وگو درباره تمدید آتش‌بس هستند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/akhbarefori/656411" target="_blank">📅 19:59 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656409">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nfp91cffGQI07pyKCBr0r0xyhQWpwQr86DvuQ34S6-XiFO4_uhl7hHuA1rVXH1WEc4Y8S5rXK2oV87nsKp2oMTVWjHUUkfJ2ZUs8PRjNaBCd0DsGpLCCl9-3PVZkdORNJI2XcQ7Omh_aJRn8yDewCEFLuZEO4fZdCxmlzRQiaGVek8udy3aESQWyv485dx2mzIp9zNSekJaS6O-H--GY38d_lBNmlOfwh0oDmCBhps14612gAnnYIM4kCg_GIorhL0tCAb0YiGy7skJWXCRsrD5GEEJHLkLM0lstlycI4phI0S5bPOW0Bl93spDigeLggRiUE37Kss_Je6o2-de9iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EPNWy1Y5igEGd6W0j3r3xkqQOR4ytgTaR1LyLJDG-So1ywE_s1Etq3AKfcsEQMbjE0MLU6xwnlJ1_IHIyTupESSqGmPHtP_YaKrnzBbgC8NbuM5raShGe7G9bLtzxxZyYo9iwEtWFxGxF7sP8BTF31dUGhhivnP3nA0TEM2S8r-UNnEy-plDO6zPKjoUZNINNBfqXOTm6m4HQAyAp3ceF0BLic9FQVp9_AxcKBNOEqAtBzAIGImDs8k8CqQcRrhYHTmuxvRWj3xqEcUJ-na4fxHVX-gnrXK0I-cQgvGS6FMGFpEEKnpkbfAcIN6u0dVB0_3595talkH6ZqsgXzXIBw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
فقط به عشق علی...
🔹
به مناسبت عید سعید غدیر خم، مخاطبان خبرفوری تصاویر اقدامات خیرخواهانه و نیکوکارانه خود را درپی پویش به عشق علی برای ما ارسال کردند؛ روایت‌هایی از مهربانی که به نام امیرالمؤمنین علی (ع) رقم خورد.
#فقط_به_عشق_علی
#LiveLikeAli
الوفوری را دنبال کنید
👇
@Alo_fori</div>
<div class="tg-footer">👁️ 9.84K · <a href="https://t.me/akhbarefori/656409" target="_blank">📅 19:59 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656408">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
تحریم‌های جدید آمریکا علیه ایران
🔹
وزارت خزانه‌داری آمریکا از اعمال تحریم‌های جدید علیه ایران خبر داد.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/akhbarefori/656408" target="_blank">📅 19:42 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656407">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SdPhc3MZyiDtCbI81NevtE6q8_GJLoi1HpC6EUw9bYXjMHKD3GZOcien_3cm0IMdaTdA0SvDq9HcufDDH7d5j-4mc5jFo955ZiW6AelHl4oW1khCyjsqmp4QRIUmZg8qWlyillacw0svUsV-tnUI5pYz2KFzgurXvHmf_XlZVvY-cJXzpu6I4kmLsvzHKsAz4x3Rxn8eVLd1bfPjaQzOrl9swe1UpZnvPEiaAOGvqbQeBOLmBaq0fQ-7dxF51vaHx0G4vOy4No0m016LCgHsO_qFqdLdtwObW95Ce9pwMJgCKGx6kBx4tGR23qGn4fYDIYpBaKB8KwFOB0DDAs7Ctg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پزشکیان در شبکه اجتماعی ایکس: سرو می‌ماند ولی طوفان به پایان می‌رسد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/akhbarefori/656407" target="_blank">📅 19:34 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656406">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">♦️
زمین‌لرزهٔ ۴.۸ ریشتری در عمق ۸ کیلومتری زمین، حوالی منطقهٔ بالاده در مرز استان‌های فارس و بوشهر را لرزاند
#اخبار_فارس
در فضای مجازی
👇
@akhbarfars</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/akhbarefori/656406" target="_blank">📅 19:29 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656404">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CF9St5mkCLR3SJ-yxe8qBbic_4WRfHpQiwX1umdhtTdCIW0ozb_c8EvTvbyVr9IBzTC7bob8Fu3Cf37T-KiTwREWjiywRm5Hul7kZ76iyMc3uwCCtFl8KKfK0njjG9NaHE5V_PZlNGKLfiK5P90vz3Durc35O8uMXi0CxThU5q3z6iaxPNedrPERdB-jwbnDMsocb7_QxvEaSGDr37nQt_LGsTW1nKHS92I5OCGzto5eBVwpsFhaEvSJQeaWi7Dume1DasLeuvmzTbwBu1Q2Bi1lIRn_xfgOKWKiAkDsOxhNbom9bSsst6YARRXpZ9NeU3iZaNqQUhmva183XRNrUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویری از سنگ مزار شهید علی لاریجانی در حرم مطهر حضرت معصومه (ع)
#اخبار_قم
در فضای مجازی
👇
@akhbareghom</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/akhbarefori/656404" target="_blank">📅 19:15 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656403">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VApl3DRaChtSoMInRSipQEz20r4hwn1isKyZciZKN5Yr17jYGyss5WlSbbboTHm3xE1Z9KMIbM7DKbP2EzRd4ufo5ShqKUfn4cZh7m7lMHdcAf5wpStuaypOaPwAzj9w8milUWIDZd3OFSAsW643fNDCtgxzOQA1G2ULC8ZKIScb4fCE9P2yQT8wdfOFtA67YwvG3Zm4vue2avBELxZe7IpISB5_0ZjH4ZmiiN3vrqIdha3wgwa2VpCS1I973IeoCfn6VQAAV-q3F7Z7sNrHGHtST3Tn7Jmk23ALttQoLt3gsPCTXUwwF4hRvGn3s0dRYIMuq8Rn1D9efJDuUD0oGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بگو مگوی توییتری رئیس کمیسیون امنیت ملی و مشاور ترامپ
🔹
روز گذشته مشاور ترامپ در پاسخ به ابراهیم عزیزی تصاویر موشک خیبرشکن را هوش مصنوعی خواند.
🔹
ابراهیم عزیزی در پاسخ به مشاور ترامپ  در توییتر به او یادآور شد: فرار ۹۰۰۰ آمریکایی و تخریب پایگاه‌های آمریکا در منطقه هوش مصنوعی است؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/akhbarefori/656403" target="_blank">📅 19:11 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656399">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MKAzhUQ7mSN5DrbNwao-X1nFcKqbAXAI0yugkJaH7xnJtI-7gZtGo3eCpEPvJRiFUane5HpKGK-lt5fQrYQm16XYIwXm5OwExwItNSjm9HvcffGXopR0LUP-GZxSo_P90nN-0MyOVqycsQy-8NK8H1tf11Iyr2ct23m0q0zUBMs_Giy3h_Y5T6ahQbL3iH5oBjOIk37pF7DwzlPMss4WtZ9ePt-A60PtHrm72YL-D1utnBmHC17fE6fPiTYUH2djfjziPx-mJ-GbTYoXwGPcJFzNjdAKzgrYfMPMLJ4_L5Irc4gCHT8y-ohrkHQaihZqNRtsrKO7gM99fJ4Eqyp0lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BuDNNd_knoeKElO5NHbfO3KWSTFrisGTmVKf7ZVauXa0rtHN9gULWQXmV_7oTDaEI4C7m2Jhi_fRqLD7kh4UCQg2UZbD4RtoWvDbVhWoMT4CYD52c1lquARgQ3wPVUUgDKidj2IpTi2dOoWitDSCiTiDDuogFxeIAiF-9dCFYoEoImtJElsQnOgydM_aM8FO4zi01hPAuBE-8o2ahd3_E6JwxaCrc296W2SHw-XCc2wqICX70L4Xt66AVZsDAKRRURV_-MGLYg92VsFqU10tb6hMb6Vtie8nY6JVT1yQM0NAiqnRK4e-ynlS_2I3kZ5A1F7hxo6nk_0TeqOLVevEaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kUqgHcWAXbSZnp5rV8Q4RoKRx-5L79zeGa_l_MbN01keLY4-DZOvXOSnBFkQxa56WZ_BWbmzfxUNVKiiqVo8Va3gITvPlfzY7TozfQ0DNqQT5Dy3fJK_jbzYZiAqNhjOLk_YdhF1fTZqNTvD4WTLcV3kXoY6c_Aw-TKHGnlgjdsf4B9vk-EjFLfvtgKk1CX-T_Q7-vyw_kKmB6sx6f3K8aJamg6r2ugivyCU7ZVFjRw9ti7QaG2GW0K6TmH0B-W2vESMtCZC6kdcJmEbqSP1mG04phdQC7gdA0VZ2mMHQNv6q2w--2b6jzLF2_OPkOLDNUvvvPlNjVzDCstMF0DQOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KU7B8_wt-taYYCNGI52TIgYMvhVtyMu2YQVoBJ4JXPPXICfMIeaIZRnp_GUPfJJfwhxSN4v7jwMDxpYui1Q87IseY10yCDmn4ZM2iUxxo5ihGBOICDF-OefSL2a7ZgEoICVIdLvSS_NU0ZBt7clUDFogDKcfq6Red12xG5MT-NNoCVD-XwVBiJacwNTI6kCYuBEetAXiHi8sNwEUWri7nt75tGTj1KLDsYaNboH6tC5jwYivaFUfqOpE42245ssTfjgvzhpZf2fIQ5IrOPO2JkZAqUrKOIS80Yg0HL_7PAphiWnjy9K6pbnkczdYCeGBWkmcFSSATzVTu0Zauw_9uw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
تمرکز اپل روی عینک هوشمند؛ جانشین ویژن پرو در کار نیست
🔹
گزارش‌ها می‌گویند اپل توسعه جانشین هدست Vision Pro را متوقف کرده و تمرکز خود را روی دو مدل عینک هوشمند گذاشته است.
🔹
همزمان تصاویری از نسخه مشکی این هدست نیز منتشر شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/akhbarefori/656399" target="_blank">📅 19:08 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656398">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EO-tLKuVkhnq_QXdxDDo_2n3eQyspAAw-BkJmNzGBd6elTRNwML-ipXEMJjP3PFEoQvsWDDelx9c567ItJdWxf_UYSnvakpBGFVrnJureOAJaAraPY2bWklUqTe9SllQJXDTjPrKyrjTq0fltMVoKw3o7rGwupo8sCsS3_gZ4N4n-sa6Or0RipJCMHVa5mv1r5jTDzqviOfkcFd4IJZWWJlXk1JwY6B0ZnD9JuS0auEzya0k3ysxFD3quSAGi3ZWUPNt7L7UjavmQo-OeNi00Fg_vxtZHdIT0aT2x1vaswUIHS8AzeHlw8fXHAHcQpwkpwvF_tn0ldu1Ed15vhTo1Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/akhbarefori/656398" target="_blank">📅 19:04 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656397">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">♦️
پوتین: دلیلی برای دیدار با زلنسکی نمی‌بینم
رئیس‌جمهور روسیه:
🔹
نمی‌دانم که چرا اوکراین نمی‌خواهد ببیند که دولت ترامپ ضامن مذاکرات صلح باشد.
🔹
زلنسکی خواستار دیدار شده، ‌ولی من دلیلی برای آن نمی‌بینم، در حالی که ما به توافق صلح دائمی نیاز داریم.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/akhbarefori/656397" target="_blank">📅 19:03 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656395">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V2UfU4R7tn7R4GOfZg6Y6JyM6tsZ3hHR4of4qmZ276BWMAr6DSTw3f7LZ4MMYb50YTWBmOM9PBO6_Kck2AEJoQx8VNJiNobvNqcaoq2uNCjiqde5F3n2ZrFFBMbZAyYwi_y_mIcJautcqxTYrghknSP-ViJnS4JQiPdLTlTGznWZnnEA_Biudodf5ev_KO8soeW-BlRzOcL1xmj6cPCnDWiMgWRHUnXfVxaTG4IFUC9lnVKWJWDrstcmQpDekKmBfegc_cumpgaptOfEoOO9z83gS8ExcOaD9j-2m49PSMupTxY_XCBL477ofyCY3N-4z1h2inkDLJ8LOfWFaC1lsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ریزش رمز ارزها ادامه دارد
🔹
برای اولین بار در ماه‌های گذشته ارزش بیت‌کوین  به ۶۰ هزار دلار رسید.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/akhbarefori/656395" target="_blank">📅 18:56 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656394">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mkd9nh7leO7iuM3tfj-IMOrKgNfdMigDKWDrkQ08CoBypUmzCVKSPtWe3MWPDPBB-cR_QEElE-rQVe-6Kw-Q1k_vL5Rhb18vGIUkO9jbV3yViUCLEJYX1sLxRpkotMDBb5mIemqqdYdYnr-b0HfDBcbd0ur0oMgUocEurMfRNyH97gP_ZnSfJYVpqs6HyRKq47UsZOzvp6Qkf6bXlXq7dGFgGSmgvEWCBHgUEIcmKLrTYYiIvjtzPJHK3f_nXFyPLtsqKkKDDqiXvzX3UezGQNOO5vgpbs96ba4ApjE4jrcUIlh1KH4K3HuhAFeGYvx9PIw9U8LxJah6Ct67oFYoBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خبرفوری رو در سایر پیام‌رسان‌ها هم دنبال کنید
🔹
خبرفوری در ویراستی
👇
https://virasty.com/akhbarefori
🔹
خبرفوری در روبیکا
👇
rubika.ir/AkhbareFori
🔹
خبرفوری در ایتا
👇
eitaa.com/AkhbareFori
🔹
خبرفوری در بله
👇
ble.ir/akhbarefori
🔹
خبرفوری در سروش
👇
Splus.ir/AkhbareFori
🔹
خبرفوری در روبینو
👇
https://rubika.ir/akhbarefori
🔹
خبرفوری در گپ
👇
gap.im/AkhbareFori
🔹
خبرفوری در ای‌گپ
👇
iGap.net/AkhbareFori
🔹
خبرفوری در واتساپ
👇
https://whatsapp.com/channel/0029Vb1RfOdJkK71F9wpxh3F
🔹
خبرفوری در اینستاگرام
👇
http://instagram.com/_u/akhbare.fori
🔹
سایت خبرفوری
👇
http://khabarfoori.com/</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/akhbarefori/656394" target="_blank">📅 18:50 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656393">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">♦️
انفجار بندر شهید رجایی؛ حادثه‌ای ملی با گزارش بیمه‌ای ناقص!
🔹
پرویز خوشکلام خسروشاهی پس از برکناری از ریاست کلی بیمه مرکزی، هر گونه بررسی عملکرد و انتقاد نسبت به سازمان تحت مدیریت خود را جهت‌دار و باج‌خواهانه توصیف کرده است. اتهامی بدون سند و مدرک که به‌نظر می‌رسد نوعی انتقام‌جویی به دلیل برکناری وی در چارچوب تحولات اقتصادی و مدیریتی وزارت اقتصاد باشد.
این در حالی است که در فقره انفجار بندر شهید رجایی کارنامه شفافی از عملکرد بیمه مرکزی در دسترس قرار نگرفت.
🔹
چنین حادثه‌ای باید بلافاصله به پرسش‌های بنیادین منجر می‌شد؛ چه مقدار از کالاهای آسیب‌دیده تحت پوشش بیمه باربری بوده است؟ چه میزان خسارت ناشی از توقف فعالیت بندر برآورد شد؟ سهم بیمه آتش‌سوزی، مسئولیت، مهندسی، باربری و اتکایی از این حادثه چه بود؟ کدام شرکت‌ها درگیر بودند؟ میانگین زمان ارزیابی خسارت چقدر شد؟ چه مقدار از خسارت‌ها از ابتدا خارج از پوشش بیمه‌ای بود؟
اما در دوره خسروشاهی، افکار عمومی با چنین نقشه شفافی از خسارت مواجه نشد!
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/akhbarefori/656393" target="_blank">📅 18:49 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656392">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">♦️
تخریب کلیسا ثبت‌ ملی انجیلی شهر مشهد
🔹
تاریخ ساخت این کلیسا به دوره پهلوی اول می‌رسد و ثبت ملی بود.
🔹
هنوز خبر رسمی از علت تخریب منتشر نشده است.  #اخبار_مشهد در فضای مجازی
👇
@Akhbarmashhad</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/akhbarefori/656392" target="_blank">📅 18:47 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656391">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">♦️
تحریم‌های جدید آمریکا علیه ایران
🔹
وزارت خزانه‌داری آمریکا از اعمال تحریم‌های جدید علیه ایران خبر داد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/akhbarefori/656391" target="_blank">📅 18:44 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656389">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/so0u0iyO5_rKycSPCXHCNeNXz0-lyQQ-AYYS10391lYz1c6WWER7a7B5n6I14nXhx4BUKd4bJ37JCvpRmxqmvuU-h5SvAagkXvqY6Bfpy9htYyC41-fqm1IrOrQCA5DhgnfDttHJqnR4YzogyT5_cZfjLTY8kxlXbl39koT9Khmu65M-G9Jx-UBHWu7kzZ0pUTlaIES6v6jgtHKZMAQtE_MgToiGEa3UtXiR1TfRJed7FI9smFuMGwIptA3LDrvJ2OOrUeIyPhMEzoW9ixZuq9zJQduIzZTHENj7q-gTBQ3hnTNouUDQITApRIdCGupo9640IxSkjLRgSnGDdGJ8pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/c4kOJ8VzIL1fMoDAbJtdK6MXfHXfRufUJUKoaSRfHPTRxnvJAAIIEuHDTUk_mLNiCNU4aT9zJbaoGKzo7RBVB9wqti06NHMWhUyfFphujSRoRdIGNoELAETrfBk3mzE0Suvix5uC1kn1hsfZZ4lWaj50o0jHv2pKECfDP1yl5UrBNM6RfMqtsrss82PXN0he_D2FvPWFozdyuBxTA12HGj1fl6k74QVE2c_JTxzmz4rGfrwoI1lq1fss4sLRCkjHHBELiofdfbHOW5ziMucdoRsaKSSvtzgVVN4Imc2VTJZ56u2JbK2gquGGZ3Au7XJfrzR2K8VGisHNWcJHz0YyFw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
آماده‌سازی شهر ونکوور برای رقابت‌های جام جهانی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/akhbarefori/656389" target="_blank">📅 18:38 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656388">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LnCY-sHtmiO69ndhQR1rvsRBs1Y6FgAoXbnDBh6sbWuJ8F-jNVYVm_cnH-iMOHfK57C0Bx97mZQP9lr_avC-vsVG0jrq1H8Hb5r8zfJW-60tmHKbh4vKTgw497O_UzPel9RGEOEP-D_w9mS9PrFsc81D7G6FI7xpe_qhZ2G1J2yihHNtbuT7RUUVAr-GJALPG6m5_tZsGbLOuKQiKBf7hbSvh0Rcp6NMsKC53QkDngxmFyMcPVhIvmaHtU54ATCGorqXWcLGXMgwSnUuLILyJxXhxCVPxYu5xzwHYxdiRpTuQW7L01tH2TjRyIU9A-9Wr_cJ6NJ2SQ7zsfn3Ta5Z2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
«زینب دشتی»مجری تلویزیون کویت، به دلیل حمایت از ایران به ۳ سال حبس محکوم شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/akhbarefori/656388" target="_blank">📅 18:26 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656387">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UUHgodLuzYvH-gqNFdiTCZ2zDII-8BsEaKKUuN3F2ErAbRntaddgzm3bRUJhB4alcyrpVwywafxyxnGbZgHCV0DmspulP-MoxZGHZjKwHqazIJT59jH5k5ayjJqfAY7WI1tALNb900SHtWdDMz8eLI1hA3z9O4pj1TGKVN94clwxldDsF7x4Iexjhlq3b4ADIsn6Y4YxJgFCY-fuG6o_mHECH9RJjRWhDbYZDkReR-Hg4PI-WkZQPRIwlXZ3_1zWhWHyVZJl0kibM5VXmgCrVtnTjV077grNvmv0gwDW68kNnkyln0VpLQXJHORbP3luw4wDRKgvNMLUwFvbcebbbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خبر و بیانیه‌ای که از دیدار عراقچی و ویتکاف به نقل از کاخ سفید درحال پخش شدن است قدیمی بوده و برای سال گذشته و برای تاریخ ۱۳ آوریل ۲۰۲۵ است
/جماران
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/akhbarefori/656387" target="_blank">📅 18:24 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656386">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
ادعای سنتکام: تغییر مسیر ۱۲۹ کشتی تجاری همزمان با محاصره دریایی ایران
فرماندهی مرکزی آمریکا:
🔹
از زمان آغاز محاصره دریایی ایران، مسیر ۱۲۹ کشتی تجاری تغییر کرده و ۶ کشتی از کار افتاده‌اند.
🔹
کشتی تهاجمی آبی-خاکی «تریپولی» برای حمایت از این عملیات در حال عبور از دریای عرب است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/akhbarefori/656386" target="_blank">📅 18:21 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656385">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2107dd4795.mp4?token=XqFfUScjYNIPUC10BJTmqF6kmQnUtQ_hXSMss0zRPK_00MAJK0xoqS89I5Y0h_mU90qUM_uwmqToy8C6P3uejVK2NWgpu27UaLrnrjw96to3-mjNqdW-j1NK62pxaD5-QhhqGIsN-WaMXSP6GQhAlIbGC_cdJMQodJmuOstShA1eKAw-SaUVE8YBIHfJjb0KnCPL3ZfJZd6ws5JWw33yITjKLl0XgM__SJX7qSjEuvbxfInReJqCgI9anKS2CfgzqxGZBJQ_8ExNjWQ06kxpxOlTSU3n1-8ZyIqw3iU5RpH0nHG1E9BO5ehTojdPEz4LgBrqV2WPcTMeFa0o6wTV3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2107dd4795.mp4?token=XqFfUScjYNIPUC10BJTmqF6kmQnUtQ_hXSMss0zRPK_00MAJK0xoqS89I5Y0h_mU90qUM_uwmqToy8C6P3uejVK2NWgpu27UaLrnrjw96to3-mjNqdW-j1NK62pxaD5-QhhqGIsN-WaMXSP6GQhAlIbGC_cdJMQodJmuOstShA1eKAw-SaUVE8YBIHfJjb0KnCPL3ZfJZd6ws5JWw33yITjKLl0XgM__SJX7qSjEuvbxfInReJqCgI9anKS2CfgzqxGZBJQ_8ExNjWQ06kxpxOlTSU3n1-8ZyIqw3iU5RpH0nHG1E9BO5ehTojdPEz4LgBrqV2WPcTMeFa0o6wTV3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
به نظرتون با چه سلاحی میشه تو جنگ پیروز شد؟!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/akhbarefori/656385" target="_blank">📅 18:07 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656383">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">شلیک اخطار موشکی - پهپادی نداجا به سمت ناوشکن‌های متجاوز و مزاحم آمریکایی   روابط عمومی ارتش:
🔹
پس از شلیک اخطار موشک‌های «قدیر» و پهپادهای تهاجمی نیروی دریایی ارتش به سمت ناوشکن‌های آمریکایی DDG-103 و DDG-87، این شناورها دریای عمان را ترک کرده و به سمت اقیانوس…</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/akhbarefori/656383" target="_blank">📅 17:56 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656382">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OtqjsIwDPV4Da95HItyHmDn34IfyNRKOJ4__3Lsf5NdNC36M6vGra8Xjwm2HvB8gxNFAlH_bLHhkdVRJh7K7JU4NWV-jXJFGdwZKAhhn9wD7boEVvb6ANnHwxB5nGdVw8RRmuvgY-zbVKT-CkB0yBVAnJyCwyIhejp9q2dcty-cAycT5EgLoghqNBccpS0bQQnoEeptpQMb51xvnoiUBHKDR1c0qQ8e_gaIQvbMpynYe1VC3VqKOrYz7wXEOJgjBpvR6IrKQ4Awo9GYLrzDNjSsDqSrAgFUBZfKCeM-nELZZUcRXySNtJEq8kRlViF7Mx5V9ItQDJfOxdCMgpB1QUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بازگشت ایران به جمع ۲۰ تیم برتر جهان؛ آرژانتین صدرنشین جدید رنکینگ فیفا!
🔹
تیم ملی ایران پس از پیروزی مقابل مالی، با یک پله صعود در رنکینگ فیفا به رتبه بیستم جهان رسید.
#ورزشی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/akhbarefori/656382" target="_blank">📅 17:52 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656379">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac4c63bd03.mp4?token=Pxkzhc0itjezMiWzEsVsycv_xbHpigwnOQXoBhQ7bJZi49GUY4_oO8wDZZM-7JgtglktwpocEMZ664hPd0rPJbOkgsU5MyFe0B7638aEXWEE3HnC7LEPD3xuu0699v1fvekb8oem9zNOIS4ZNZ5cwgTgXm6xmn3Dv3QeadOaHYbyRb8_fjywaZvhF8k9oUtaKPowK_x-borC1u_LcT0JFrmQOltET4uS_Tetc6K5ORwEpkWBQ00Sthr1g4Iv9BiIvTtaLtwa9Fz82_5m-iaE-Tqwru4EVvQ9BAjiUR7yKtZrZ6YCBOfyKVx4tb4gpss5CoxEUTujKhqxMNGi-yzg-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac4c63bd03.mp4?token=Pxkzhc0itjezMiWzEsVsycv_xbHpigwnOQXoBhQ7bJZi49GUY4_oO8wDZZM-7JgtglktwpocEMZ664hPd0rPJbOkgsU5MyFe0B7638aEXWEE3HnC7LEPD3xuu0699v1fvekb8oem9zNOIS4ZNZ5cwgTgXm6xmn3Dv3QeadOaHYbyRb8_fjywaZvhF8k9oUtaKPowK_x-borC1u_LcT0JFrmQOltET4uS_Tetc6K5ORwEpkWBQ00Sthr1g4Iv9BiIvTtaLtwa9Fz82_5m-iaE-Tqwru4EVvQ9BAjiUR7yKtZrZ6YCBOfyKVx4tb4gpss5CoxEUTujKhqxMNGi-yzg-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شارژر چینی که بعد از کامل شدن شارژ، خودش از پریز خارج می‌شود
🔹
یک شرکت چینی به نام
Kuwajia
شارژری طراحی کرده که پس از رسیدن شارژ دستگاه به درصد تعیین‌شده (مثلاً ۱۰۰٪)، به‌طور خودکار دوشاخه خود را از پریز بیرون می‌کشد و شارژ را قطع می‌کند؛ محصولی که به‌تازگی در فضای مجازی وایرال شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/akhbarefori/656379" target="_blank">📅 17:50 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656378">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b1fa8b999.mp4?token=RbI4o2wS0HnDhc5dUKwmJFmc7tqZixvItxtHcco1gH-QQv2DO1OKXPi6PAsKjy9mKmzJNUGak_i0phsVUckNze91qfYm54nVhk19BHSoCpWU9wKQIipARUs2f4uFQxod7NwujD2uB74_g9K4UxCS3G0WFlDoS8fl2S6NPbEKTFYHL7gHLkATZn7rz_BJDykxBCBSTDkhY-we4A11yoVuqTCosurE3IAUqyjMgCpPMQXMZeqWXSTIgkN27L1NsSLkzLWpxPYRQEVzJlPGSDsUF78wFpDmyUZjCt_7Q7G5rl3-drZUNGj0Gs-8_Z1i6GS-ldjFR48WgzCPQLQlrxIDHYO0sofW-eqgBm6sxHcTTCQV6eqlJNbSZ8eL-ba_GO4p3aaXeAPDAHWpz6baCTs2l9QAw8HDYmCqFKuaXLAjbXa9-pIKJ0Fs7F1XZO-N0HTmF09nKcwGSIlm9YTIun3nPHAp6g_CqE79moVYW6gl2A1wUisMlHg_j_wMAk0xhOWq3b8bl7mv1rxQnryZUkXSaRh6ee9QN-9VldajDn9irejH1Woo8bNL-3E5F4jP4JwvfhhHi1GAZMMBBY7rtc_Z2NpS11lCweabBZ_ChxijYsnrNwHZUUXHK8d_7b9d3JJF4prZfrDO56tq5ossMX45lDRmzsmLGStLdNHjKjVPDDk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b1fa8b999.mp4?token=RbI4o2wS0HnDhc5dUKwmJFmc7tqZixvItxtHcco1gH-QQv2DO1OKXPi6PAsKjy9mKmzJNUGak_i0phsVUckNze91qfYm54nVhk19BHSoCpWU9wKQIipARUs2f4uFQxod7NwujD2uB74_g9K4UxCS3G0WFlDoS8fl2S6NPbEKTFYHL7gHLkATZn7rz_BJDykxBCBSTDkhY-we4A11yoVuqTCosurE3IAUqyjMgCpPMQXMZeqWXSTIgkN27L1NsSLkzLWpxPYRQEVzJlPGSDsUF78wFpDmyUZjCt_7Q7G5rl3-drZUNGj0Gs-8_Z1i6GS-ldjFR48WgzCPQLQlrxIDHYO0sofW-eqgBm6sxHcTTCQV6eqlJNbSZ8eL-ba_GO4p3aaXeAPDAHWpz6baCTs2l9QAw8HDYmCqFKuaXLAjbXa9-pIKJ0Fs7F1XZO-N0HTmF09nKcwGSIlm9YTIun3nPHAp6g_CqE79moVYW6gl2A1wUisMlHg_j_wMAk0xhOWq3b8bl7mv1rxQnryZUkXSaRh6ee9QN-9VldajDn9irejH1Woo8bNL-3E5F4jP4JwvfhhHi1GAZMMBBY7rtc_Z2NpS11lCweabBZ_ChxijYsnrNwHZUUXHK8d_7b9d3JJF4prZfrDO56tq5ossMX45lDRmzsmLGStLdNHjKjVPDDk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بیعت مادران شهدای کودک میناب با آقا سید مجتبی خامنه ای
📍
میدان انقلاب اسلامی
مهمونی کیلومتری غدیر
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/akhbarefori/656378" target="_blank">📅 17:50 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656377">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">همدردی مادر شهید کودک میناب با مردم و رزمندگان لبنان
📍
میدان انقلاب اسلامی
مهمونی کیلومتری غدیر
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/akhbarefori/656377" target="_blank">📅 17:49 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656376">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">«چالش بیعت» در مراسم مهمونی کیلومتری غدیر
در روز ولایت امیرالمومنین علیه السلام مردم تهران با خلف صالح رهبر شهید انقلاب بیعت کردند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/akhbarefori/656376" target="_blank">📅 17:49 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656375">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3103085dcb.mp4?token=BdVhQ6nFT9huCBf1aiN7o6Nh_SjNuIDWd9lHrDsn1zHEXxVzu0RU7ujpO6jkOvN_t0CetmyaCsPkNxUfkjnihhOU7LDNR2Fzw6MALlT-MFPIxa1Qaop5WXcSZzvWEOaRVmZteRE3oi0UtLKNHqcFixCzBchn9bAVXUKV5TtvxF2KYiqLxp3M0fHh0l5UQ25lh9paTzCiy9tV8ECAbf6A4T7YBMND5z9fnDPtYPVkm0CS6_sEq19HQp-BL4pwwVaHErOwvq48IDeea6RdN38Hq2UHcofiB9-Z_MX-Z_V_o0Hvz7LK33P7sfxMly0SEG2sXEWEMCOntECkRd4DoPnPjHaL7aFIIO6BeGVVBhrr4UVMJiR4GhFxNxCeWSEOs8xoK3RDoONdIcK9ZaoOpXg_UzhnTC5WwqTLUin4b3ViIv9rVNZqvHkuc-02QjT7rUhXu6Oj5fWhQRONRo3QnO8Ek6GDs8V_xQFBE9tX4YbocHs1L87LGMOXOnQ72rR979fRYA65uBUgzENyOu6mbSYQ0_nuzJM6ONI3ERDlZL-V_M2NoRLuucoj3mbRKMvW2n3RMEX_OGAnqLrCSO3GmvXYgLgBR0m41z_dmo9Lxun3QrT1_K5IZ_Sw2C1rmg-QQiOoJx_QWs4cUMGHgQZxP_K0GUU6M-lmm99CXJCIgti5i4c" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3103085dcb.mp4?token=BdVhQ6nFT9huCBf1aiN7o6Nh_SjNuIDWd9lHrDsn1zHEXxVzu0RU7ujpO6jkOvN_t0CetmyaCsPkNxUfkjnihhOU7LDNR2Fzw6MALlT-MFPIxa1Qaop5WXcSZzvWEOaRVmZteRE3oi0UtLKNHqcFixCzBchn9bAVXUKV5TtvxF2KYiqLxp3M0fHh0l5UQ25lh9paTzCiy9tV8ECAbf6A4T7YBMND5z9fnDPtYPVkm0CS6_sEq19HQp-BL4pwwVaHErOwvq48IDeea6RdN38Hq2UHcofiB9-Z_MX-Z_V_o0Hvz7LK33P7sfxMly0SEG2sXEWEMCOntECkRd4DoPnPjHaL7aFIIO6BeGVVBhrr4UVMJiR4GhFxNxCeWSEOs8xoK3RDoONdIcK9ZaoOpXg_UzhnTC5WwqTLUin4b3ViIv9rVNZqvHkuc-02QjT7rUhXu6Oj5fWhQRONRo3QnO8Ek6GDs8V_xQFBE9tX4YbocHs1L87LGMOXOnQ72rR979fRYA65uBUgzENyOu6mbSYQ0_nuzJM6ONI3ERDlZL-V_M2NoRLuucoj3mbRKMvW2n3RMEX_OGAnqLrCSO3GmvXYgLgBR0m41z_dmo9Lxun3QrT1_K5IZ_Sw2C1rmg-QQiOoJx_QWs4cUMGHgQZxP_K0GUU6M-lmm99CXJCIgti5i4c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روایت دستور رهبر شهید انقلاب به امیرموسوی در روز اول جنگ ۱۲ روزه برای در نظر گرفتن تجمع مردمی عید غدیر
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/akhbarefori/656375" target="_blank">📅 17:49 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656374">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">در مهمونی کیلومتری غدیر تهران چه گذشت؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/akhbarefori/656374" target="_blank">📅 17:48 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656373">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc5d3e0763.mp4?token=pHb5uN5R77zqnuvhInfhfuqe9MffFQTT9leR1dVmCFSEhuzB4XRBvZIHIf-FXSTvWCideZTMh5thNYQyb4YB10bdcK8_XtkZKI0VLOza-spThgXFBkFGodv9yYq-YilopyhQrtv6dGZ0lFNMdj3TWGY9zz-ufG4NnetI_Nt7fb5KW6h4RWM5dJOJgpOtaXWeL7OLhO-ipeouounMNE1QFjVBXsyHsB-D7jpILjQk-QhrlaBtkeEFScZHps3Fu5eawBv2Y34rf9VvVAWyJxl634th7VXfnjwMIHhNe2HqxX5SpiM2lbxB9vYojEEEnLuDVdcpJT_J6DSi8_1vpt6wSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc5d3e0763.mp4?token=pHb5uN5R77zqnuvhInfhfuqe9MffFQTT9leR1dVmCFSEhuzB4XRBvZIHIf-FXSTvWCideZTMh5thNYQyb4YB10bdcK8_XtkZKI0VLOza-spThgXFBkFGodv9yYq-YilopyhQrtv6dGZ0lFNMdj3TWGY9zz-ufG4NnetI_Nt7fb5KW6h4RWM5dJOJgpOtaXWeL7OLhO-ipeouounMNE1QFjVBXsyHsB-D7jpILjQk-QhrlaBtkeEFScZHps3Fu5eawBv2Y34rf9VvVAWyJxl634th7VXfnjwMIHhNe2HqxX5SpiM2lbxB9vYojEEEnLuDVdcpJT_J6DSi8_1vpt6wSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مرد گمشده نپالی پس از مراسم تشییع جنازه‌اش، زنده پیدا شد
🔹
یک راهنمای کوهستانی نپالی که گمان می‌رفت در کوه اورست جان باخته باشد، یک هفته پس از مفقود شدن و پس از آغاز مراسم تشییع جنازه‌اش، در حالی که سینه خیز به سمت کمپ اصلی می‌رفت، زنده پیدا شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/akhbarefori/656373" target="_blank">📅 17:46 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656372">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aMQGZfF5ddKm8nDgVr8x_k-pO3HobCw9TgzcYnaK4bqGuKb8kTp_1dztP8_3eTMEMOB9-eKIOVzaQBpDJwi3AS4GLzngLZjNP08u3M2ntGhZ2Rv-yDc6FimLxBwcEWA9jb1-U4TXVRHCxkLvrGowvWGwuIaNdH0p-X25uOxtZcqHusaAGj0XnHDMAVvpAeKc9lcnj2vjCeZUl0OXTeyTxs9YPTUyX9YXnPcxpI-a1gCwEeKUTSPzWJyb7qKVmJ-kwkbcWgVR0X2EfUwnzDTgkzZUtCbVXYOYRqX40UT1JqCxRCTwiSKkWFADNLjRWPeh26dVuateW5dQqO0GYemN5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بازداشت مدیر یک شرکت ایرانی حوزه فناوری در آمریکا
🔹
وزارت دادگستری آمریکا خبر داد که مدیرعامل شرکت ایران تک به اتهام تأمین تجهیزات آمریکایی برای تأسیسات هسته‌ای و نظامی ایران دستگیر شد.
🔹
جمشید قمی، ۶۳ ساله، اهل ساحل نیوپرت، به توطئه برای نقض قانون اختیارات…</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/akhbarefori/656372" target="_blank">📅 17:41 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656371">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">♦️
تکذیب وخامت حال میرحسین موسوی
یکی از نزدیکان خانواده میرحسین موسوی:
🔹
او به‌دلیل سرماخوردگی و با توجه به سابقه آنژیوپلاستی قلب، برای مراقبت بیشتر در بیمارستان بستری شده است.
🔹
به گفته وی، حال موسوی خوب است و خبر وخامت وضعیت او صحت ندارد./ جماران
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/akhbarefori/656371" target="_blank">📅 17:35 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656370">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
ادعای گروسی: ازسرگیری بازرسی‌ها پیش‌شرط هر توافق است  مدیرکل آژانس بین‌المللی انرژی اتمی به الجزیره:
🔹
بیش از هشت ماه است راستی‌آزمایی موجودی اورانیوم ایران انجام نشده و بازگشت به بازرسی از سایت‌ها شرطی غیرقابل چشم‌پوشی برای هر توافقی است.
🇮🇷
✊
@AkhbareFori…</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/akhbarefori/656370" target="_blank">📅 17:30 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656369">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">دعای خاص امام زمان علیه‌السلام در عصر جمعه
✨
گفته شده هرکس صلوات ابوالحسن ضراب اصفهانی را بفرستد، حضرت حجت ارواحنافداه برای او دعا می‌کند.
✨
بیایید در این جمعه‌ نورانی، با فرستادن این صلوات، دل‌های‌مان را به عطر یاد امام زمان ارواحنافداه معطر کنیم و مشمول دعای حضرت شویم.
#گنج_پنهان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/akhbarefori/656369" target="_blank">📅 17:22 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656367">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65ef51f223.mp4?token=HbfF2rKs8uPgYcIDUBWbdefzqGozXgtKzPImyjp2YFkgZdS44I6GOgDuneEDH1tBXSWHejol0tQaL8Ub5GJM_ijEr6pECCRqBZxfiaj5VSaJNXle8_D6SOgOvVfa6_UYjlAukmaCtDeFiZ8qJqibOBeYKLh6hNLsQeHZp4YcQg6Q9Dor0EBhoUjoQnP0pgsu4KqvYH7QXTjx2YwYMaeGoVAF9Mq_XclRN9t6p2AO5anjinW2DTmFnpfLFyAZvRX7EzP6zXhqDjZRhv-7Uzh-ytH-UHao-Ni3fQrTBgQkiqpq8ugOLjL8UJiZsZ4YjWi_UxeLQW7WALU0WtphGuv-cw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65ef51f223.mp4?token=HbfF2rKs8uPgYcIDUBWbdefzqGozXgtKzPImyjp2YFkgZdS44I6GOgDuneEDH1tBXSWHejol0tQaL8Ub5GJM_ijEr6pECCRqBZxfiaj5VSaJNXle8_D6SOgOvVfa6_UYjlAukmaCtDeFiZ8qJqibOBeYKLh6hNLsQeHZp4YcQg6Q9Dor0EBhoUjoQnP0pgsu4KqvYH7QXTjx2YwYMaeGoVAF9Mq_XclRN9t6p2AO5anjinW2DTmFnpfLFyAZvRX7EzP6zXhqDjZRhv-7Uzh-ytH-UHao-Ni3fQrTBgQkiqpq8ugOLjL8UJiZsZ4YjWi_UxeLQW7WALU0WtphGuv-cw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
من به عشق حضرت علی(ع)...
🔹
در روز عید غدیر خم، از مردم خواستیم جمله «من به عشق علی(ع)...» را کامل کنند. آنچه شنیدیم، جلوه‌هایی از مهرورزی، خدمت به مردم، یاری نیازمندان و عمل به سیره نورانی امیرالمؤمنین(ع) بود.
#فقط_به_عشق_علی
#LiveLikeAli
الوفوری را دنبال کنید
👇
@Alo_fori</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/akhbarefori/656367" target="_blank">📅 17:20 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656366">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/84be7c8b93.mp4?token=gh3CoqptQEf5pxi6LyLM838CrYveXf1EBaYBoF_P-gR3SFngDqHdMxgYp4RQ8GQYSvvVt9Lp6tZvL2QRKC-fvjFUdZD0Ls7SB4H4Da-97KlGNneKf4-6-LhmasOLgU4K_6EBKjpYgT3z7GbKMYg1jGzsEi7NVa5BPMufRJjohzMVzzOrouTTbMlNRcG3AgsZwM9s5SKBDfPEq_AixQpUXR_G8JwOTnN8qo7gBEsiCzNtypAkRoAfrnzWIFt-1hzZ8uA5gVoEigqLwrgjIyTXSZhML4bRRuU1IfxfV2KyG6ZHSI-v2324E4b_5Zofo4R6AX8Y5KIxdRVk-sFFfpyO3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/84be7c8b93.mp4?token=gh3CoqptQEf5pxi6LyLM838CrYveXf1EBaYBoF_P-gR3SFngDqHdMxgYp4RQ8GQYSvvVt9Lp6tZvL2QRKC-fvjFUdZD0Ls7SB4H4Da-97KlGNneKf4-6-LhmasOLgU4K_6EBKjpYgT3z7GbKMYg1jGzsEi7NVa5BPMufRJjohzMVzzOrouTTbMlNRcG3AgsZwM9s5SKBDfPEq_AixQpUXR_G8JwOTnN8qo7gBEsiCzNtypAkRoAfrnzWIFt-1hzZ8uA5gVoEigqLwrgjIyTXSZhML4bRRuU1IfxfV2KyG6ZHSI-v2324E4b_5Zofo4R6AX8Y5KIxdRVk-sFFfpyO3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آلبانی علیه داماد ترامپ؛ معترضین البانیایی: پروژه لوکس کوشنر را متوقف کنید
🔹
در ادامه اعتراضات مردمی در آلبانی علیه «جارد کوشنر» داماد ترامپ که در حال ساخت استراحتگاه مجلل در خاک این کشور اروپایی است، مردم دست به تظاهرات زدند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/akhbarefori/656366" target="_blank">📅 17:17 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656365">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">♦️
ادعای گروسی: ازسرگیری بازرسی‌ها پیش‌شرط هر توافق است
مدیرکل آژانس بین‌المللی انرژی اتمی به الجزیره:
🔹
بیش از هشت ماه است راستی‌آزمایی موجودی اورانیوم ایران انجام نشده و بازگشت به بازرسی از سایت‌ها شرطی غیرقابل چشم‌پوشی برای هر توافقی است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/akhbarefori/656365" target="_blank">📅 17:10 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656364">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d40dbeba5.mp4?token=VG7z6Hs7OvZtjBdVZyxhUbYjttpwQRMQaXrTcgupwZRsYaoafDsXo2yJnVS_V7Bsyc8qnbOoeroJyWfU5jv1uGWkWPqNi9CZSqB-oApEDU9nSHosWCHlNagoergRR35Iw3iZ7CicSiHZD7XGyt-S-K_WtNDSC2J-Y7T30yNum0J0KxpsIZFWARmxgW9-Ar02ZCR3qjHfPcFiNQXHe5qB8qpGvhpsXEHx72fHwAWzT2aXv60Sm6HbsacsUXNTh3ImS5jR5Pdl6rxdD-fN_4ddf7UQDU79wRYqeue47ABUPznr-yOmB_rHiHhv8ZOQr46qOCuz9J69xtQoEfS0vSHdmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d40dbeba5.mp4?token=VG7z6Hs7OvZtjBdVZyxhUbYjttpwQRMQaXrTcgupwZRsYaoafDsXo2yJnVS_V7Bsyc8qnbOoeroJyWfU5jv1uGWkWPqNi9CZSqB-oApEDU9nSHosWCHlNagoergRR35Iw3iZ7CicSiHZD7XGyt-S-K_WtNDSC2J-Y7T30yNum0J0KxpsIZFWARmxgW9-Ar02ZCR3qjHfPcFiNQXHe5qB8qpGvhpsXEHx72fHwAWzT2aXv60Sm6HbsacsUXNTh3ImS5jR5Pdl6rxdD-fN_4ddf7UQDU79wRYqeue47ABUPznr-yOmB_rHiHhv8ZOQr46qOCuz9J69xtQoEfS0vSHdmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نصب کتیبه‌های ولادت امام موسی‌ الکاظم(ع) در حرم رضوی
#اخبار_مشهد
در فضای مجازی
👇
@Akhbarmashhad</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/akhbarefori/656364" target="_blank">📅 16:51 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656363">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/42cc35c7d4.mp4?token=lb4WhuV4vVEllZXuqYFZD3UsrIdmoo6WKU7DW-kvEfky_2p-tMXdAsQ9uWQFRcjIA147zsTPPEzsPHUF9UX6SwJx2HPh-PHDUUXbe2sOPRdlIiAq3lC2L1UkF_3O2q3Z3s1PPmLNWVDIPR23F4NQ86fkVPsuE5kn4EcP_LZ217Zz4Pau4VegkHdbXPqwJMPo5jx01oJVPCynfT1PvuwzY0eaoPts9QlCBrqZPBsc_7nuV75fC0QsYzWY_wptKwd23BoVbGz1QvuLZDZDS1dNKdhM0DZt1nAsxOQMza6kJ8DbC2KxkDtVhJ2KMj96YxLTtrBhjlw73WR7oHKb_JRpiykk0-ZVxmN657oqnScfnxqoQ99WAh9nDR4wsB_oBYz6KzbSVYdTO_YeDDPM86lsMq4hnMVXsY-_0NVnVaDDpadhQM9CaDpwPX_JZHft1H4Dcnl6nlrhTyQ0ji33BRIW5GQuXc5SFXtMQ7yM8ysEiNRTcPRVZj_f-B6scrBcq15a_YTbjkfdtO1x4-e0N3i45QF9u4yjcT9QWBX2QByMx7W1CSl5KSiNm6WAH9AIvXhsCAY1lVe20gW0rt-G8m3TwXbHwM4odMeOhryd9Kon2Cne9D25YPftEHxPYqHSyt-3-5J5zExwHjtg3XWCfxJS26PdwFqsbSBLSV1Rc00ctoc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/42cc35c7d4.mp4?token=lb4WhuV4vVEllZXuqYFZD3UsrIdmoo6WKU7DW-kvEfky_2p-tMXdAsQ9uWQFRcjIA147zsTPPEzsPHUF9UX6SwJx2HPh-PHDUUXbe2sOPRdlIiAq3lC2L1UkF_3O2q3Z3s1PPmLNWVDIPR23F4NQ86fkVPsuE5kn4EcP_LZ217Zz4Pau4VegkHdbXPqwJMPo5jx01oJVPCynfT1PvuwzY0eaoPts9QlCBrqZPBsc_7nuV75fC0QsYzWY_wptKwd23BoVbGz1QvuLZDZDS1dNKdhM0DZt1nAsxOQMza6kJ8DbC2KxkDtVhJ2KMj96YxLTtrBhjlw73WR7oHKb_JRpiykk0-ZVxmN657oqnScfnxqoQ99WAh9nDR4wsB_oBYz6KzbSVYdTO_YeDDPM86lsMq4hnMVXsY-_0NVnVaDDpadhQM9CaDpwPX_JZHft1H4Dcnl6nlrhTyQ0ji33BRIW5GQuXc5SFXtMQ7yM8ysEiNRTcPRVZj_f-B6scrBcq15a_YTbjkfdtO1x4-e0N3i45QF9u4yjcT9QWBX2QByMx7W1CSl5KSiNm6WAH9AIvXhsCAY1lVe20gW0rt-G8m3TwXbHwM4odMeOhryd9Kon2Cne9D25YPftEHxPYqHSyt-3-5J5zExwHjtg3XWCfxJS26PdwFqsbSBLSV1Rc00ctoc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آمریکا مدعی توقیف ابرنفتکش مرتبط با ایران در اقیانوس هند شد
سنتکام:
🔹
نیروهای آمریکایی در یک عملیات شبانه، کشتی بدون پرچم و تحریم‌شده «داوینا» را در اقیانوس هند توقیف کرده‌اند.
🔹
به‌گفته مقام‌های آمریکایی، این کشتی در اکتبر ۲۰۲۴ به دلیل ارتباطات نفتی با ایران تحریم شده بود؛ «داوینا» یک ابرنفتکش با ظرفیت حمل حدود دو میلیون بشکه نفت‌خام است.
🔹
گزارش‌ها حاکی است این کشتی آخرین بار روز جمعه در سواحل جنوبی سریلانکا مشاهده شده بود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/656363" target="_blank">📅 16:47 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656362">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8363494d27.mp4?token=vR2L17_tcr-0nSvoS8v54_zafRPB37wtECQihbY1N3nOZSpHYtdSgk-AOBUJGICL-QiyfSjGWVJZXmL4jZD1yQ3lV6hO-Hzl_U3ur0tsDQZnvZ831cLlSn_agv0GgwR2qatrMBudIjGMJKg1VCVqrdXLldzhXaqGXaPq89PpJVRx3OPrMoE4dED-OeoGRuL9lqIsUUeU7u6TOxTjt74LWDYfTnqSGlE3txGHRUyevd5zsmv042ic6pRzenNS_Awhv9aE6qqvovujMyozWI-NaDqxn5z7tz2c1T1BzW7wnoTIaFIiQ_QPfIvURqWY2SG_z4qL_wvqpUaVTaB1SP3PIDs460y7PSlzOiAyIomgTGiu5eFlh7F3ghKfndlG_K3jK6bGWDF8n6APwLIH1us-jrYjQk8djTUNI6SPZ8bII30dnbbLxGRftwu96ZSfCgONgQDpHLBvH48DxlS-a7_iz02pZHlAu4qaAh2HCnFG_4oNfrJRlSj2TfTC4HfsBRYjK6jtpaWOeXaKaZzA3VcV8gktz9RPs0je-i04OH6mWwUuHpZfrDgYz5K6ncdX-L52c2JuaQC19ZzcVACO7dXmnhUNMXbOGTZKxpjoQ-bSP-v238XnKrJu41sbOIMk7re7LuwzvK7X3M45G_39KrFST1K--jeoAQAFRgaX2BGfNlM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8363494d27.mp4?token=vR2L17_tcr-0nSvoS8v54_zafRPB37wtECQihbY1N3nOZSpHYtdSgk-AOBUJGICL-QiyfSjGWVJZXmL4jZD1yQ3lV6hO-Hzl_U3ur0tsDQZnvZ831cLlSn_agv0GgwR2qatrMBudIjGMJKg1VCVqrdXLldzhXaqGXaPq89PpJVRx3OPrMoE4dED-OeoGRuL9lqIsUUeU7u6TOxTjt74LWDYfTnqSGlE3txGHRUyevd5zsmv042ic6pRzenNS_Awhv9aE6qqvovujMyozWI-NaDqxn5z7tz2c1T1BzW7wnoTIaFIiQ_QPfIvURqWY2SG_z4qL_wvqpUaVTaB1SP3PIDs460y7PSlzOiAyIomgTGiu5eFlh7F3ghKfndlG_K3jK6bGWDF8n6APwLIH1us-jrYjQk8djTUNI6SPZ8bII30dnbbLxGRftwu96ZSfCgONgQDpHLBvH48DxlS-a7_iz02pZHlAu4qaAh2HCnFG_4oNfrJRlSj2TfTC4HfsBRYjK6jtpaWOeXaKaZzA3VcV8gktz9RPs0je-i04OH6mWwUuHpZfrDgYz5K6ncdX-L52c2JuaQC19ZzcVACO7dXmnhUNMXbOGTZKxpjoQ-bSP-v238XnKrJu41sbOIMk7re7LuwzvK7X3M45G_39KrFST1K--jeoAQAFRgaX2BGfNlM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لحظاتی کمتر دیده شده از حضور سال ۱۳۹۶ رهبر شهید انقلاب در منطقه زلزله‌زده سرپل ذهاب
🔹
همراهی حضرت آیت‌الله سیدمجتبی خامنه‌ای با رهبر شهید انقلاب در بازدید از وضعیت مردم زلزله‌زده کرمانشاه
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/akhbarefori/656362" target="_blank">📅 16:43 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656356">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TI8u5FBmIMbHyADbiYyRQ4h5RvPG8FJ2XtlvdTPf6CSllfv-BPd55tKj36BoK-f_hGlIoRt1tXceM5-8sKIpoAvkoO3EF7Xr874ULrG-LtT1QVV8hAYRhsNWryxzDz8txplkqu-K_vEwlWT8WRdq_MRIgzpu3ZSWGXeZB4iaPcDQMjgoGP7eTipgwtOgQvOORv_sjRrehNQpB1ohGvnSVf5bAsTh4LSInAM2OTnFSAtlBjGjRIfF6zJhTCAuHXocE0NAonZXiLRnAQPgU0ROGI6sP28-ro_0JZZSU1COZDonRXQvun6ptTBY8LtRzd4Q7egESAc_nGokNAzB5x7EQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شانس ۱۱ درصدی ایران برای صعود از گروه G جام‌جهانی
🔹
براساس پیش‌بینی‌های پلی‌مارکت شانس ایران برای صعود از گروه، ۱۱ درصد عنوان شده است. بلژیک در گروه ایران با ۶۷ درصد بیشترین بخت را برای صعود از گروه دارد.
🔹
مصر ۸ درصد بیشتر از ایران شانس دارد و نیوزلند با ۳ درصد کمترین شانس صعود را دارد./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/akhbarefori/656356" target="_blank">📅 16:33 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656355">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LfRIVlefqVlQ7BffHfJSNIBTb4rPY92HBZ9VLcJPtrXduUXB6djLmfSHzlC4mkDmQN02t8xwNqACz7oTPGo3Ivm6UjjBIIUlmWrBeKI295Kid-JQ-TiMlSVqd_V1qXn9W5H3vqGmNhwhlHh4HwP8Oru51S0y4sPq0ePCn3rdFcAFFdOlA7hsjW1KxVwrexKvEDvLiJwg5-hs_5mq3zTsv5bSV8Z3X5XBX_1vIwPxqlTqSf7cN6_4tPkWrkBDJFHtY_F4IA7yxyXudfYC3KiM2v8Bgzmlfjhe6GlhltxDcQOXfwwHjwICzgL2tgphfYLOQxnDEBsIzrrG8vgnKmFuuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
«تنها مذاکره‌کننده»
🔹
جلدِ ویژهٔ «الأخبار»، روزنامهٔ نزدیک به جریان مقاومت لبنان، در واکنش به تحولات این روزها و عطشِ دولتِ این کشور برای مذاکره مستقیم با سران رژیم اسرائیل
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/akhbarefori/656355" target="_blank">📅 16:19 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656354">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p2Qnsd5I4NE0IyGIC2LxA88ErgOCUJE8eaIGYv0mAu-pRSfq8LUuPI_t4ib7J_5WtfJjBgADuQzs72-iI0ci7hDe0Fxfke0_mkfcvcoqviMcJVNkhMiom0B4CkYBlbo5pmAjFiphaUl2lGG9gUuN1PCH85ThEiOxNFjy0SQonCVnAbfmXobiIPZdy2OKwUlmR63YS64pMFfdxxW8PUUIph_Gf6dbmDXNkvvNm_yD8HCjwgJtYKf5NeDxodD1yJGqCGVwP0krzDI1Ljfmr-SdXSSy_0UsApbCi4jSpnt-KkkZJKUUMnf0XRvSzRJS3h0U8d73t7zdNsnYJA9zwDZL_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پاپ لئو برای نخستین‌بار یک زن غیرروحانی را به مقام ارشد واتیکان منصوب کرد
🔹
ماریا مونتسرات آلوارادو، که هم‌اکنون ریاست رسانه کاتولیک مستقر در ایالات متحده با نام «اخبار ای‌دبلیوتی‌ان» را بر عهده دارد، هدایت بخش قدرتمند ارتباطات واتیکان را بر عهده خواهد گرفت.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/akhbarefori/656354" target="_blank">📅 16:14 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656351">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fec0af58a4.mp4?token=pmuJsN7HBQM0i7ZxqH9ubd83OG7l4yyRjcH_K-L5_GeOa_5jVhV3hTr-1646u7PmPNlGHukzwkGjNOZsiaWpm7RySvPPT_7zvqCeaSahoCjgaR1VYyyEcyvUOWCfvRJzg8i1czkOEOVb88QpM1PawH60CWYxGCrKKWqBhWwQM-eaKVTxfTd30xo8jacOoMVsrCK56GeJUzn4NKSf1PzAKiXq5Mv7wnCrEEyrKpvWHSvum52RlWEVSfnsLfiKvEc29ybDhY9n_tLUJkZWCwQQd7jWO6Fa18RmrFcpAG0ct3C6I6ZjmWxFWNO89pyWLFehANDyetp9E8Lw6lHB5ZvcmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fec0af58a4.mp4?token=pmuJsN7HBQM0i7ZxqH9ubd83OG7l4yyRjcH_K-L5_GeOa_5jVhV3hTr-1646u7PmPNlGHukzwkGjNOZsiaWpm7RySvPPT_7zvqCeaSahoCjgaR1VYyyEcyvUOWCfvRJzg8i1czkOEOVb88QpM1PawH60CWYxGCrKKWqBhWwQM-eaKVTxfTd30xo8jacOoMVsrCK56GeJUzn4NKSf1PzAKiXq5Mv7wnCrEEyrKpvWHSvum52RlWEVSfnsLfiKvEc29ybDhY9n_tLUJkZWCwQQd7jWO6Fa18RmrFcpAG0ct3C6I6ZjmWxFWNO89pyWLFehANDyetp9E8Lw6lHB5ZvcmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بمباران مناطق جنوبی لبنان توسط جنگنده‌های اسرائیلی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/akhbarefori/656351" target="_blank">📅 16:10 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656349">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">♦️
تیزر قسمت هفتم از فصل چهارم
🔹
در این قسمت روایت تجربه نزدیک به مرگ آقای حمید علیزاده را که در تصادف شدید روح از بدن جدا شده و از فرشتگان طلب ملاقات با خداوند را می‌کند و با واقعی‌ترین غم روبه‌رو می شود را با هم نظاره می‌کنیم
🔹
قسمت کامل این برنامه ساعت ۲۰:۳۰ منتشر می‌شود.
#تجربه‌گر
: حمید علیزاده
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/akhbarefori/656349" target="_blank">📅 16:00 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656348">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">♦️
کلاس‌های دانشگاه شریف از روز شنبه ۲۳ خرداد حضوری شد
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/akhbarefori/656348" target="_blank">📅 15:56 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656347">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/97ce25261d.mp4?token=K2kEeAtbT6pVnaqJEOBPSDm56rKP8SZ6jNg-CXGXjxQjpZajYtI-Lt-hJ-12B6YOl2ezGuHECU7Ex8598Qw2Isvz1-3IWVOD6NB2xyw7Yvwc-Uxm3zZcEcDqZ3HywYhWjVRtbqCuRb_ky5aNdzvXlmzflx80W-pz-aGwxN4GnN9gpwShL6ixRxkxNG31OpBl6N0PpcaMshzzJwx7_33S4dAI-Lvl9n2kCOHBwIr_KMhex3J7DaonhspyZZdcuB-M9yp8XJX15pXudmd5LonsYQrF0uKPv9fXh3zYiA-jt7uDpnh6WKwy7lnvev8WC91gNQmy9_cwlbLj9HQYltKRUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/97ce25261d.mp4?token=K2kEeAtbT6pVnaqJEOBPSDm56rKP8SZ6jNg-CXGXjxQjpZajYtI-Lt-hJ-12B6YOl2ezGuHECU7Ex8598Qw2Isvz1-3IWVOD6NB2xyw7Yvwc-Uxm3zZcEcDqZ3HywYhWjVRtbqCuRb_ky5aNdzvXlmzflx80W-pz-aGwxN4GnN9gpwShL6ixRxkxNG31OpBl6N0PpcaMshzzJwx7_33S4dAI-Lvl9n2kCOHBwIr_KMhex3J7DaonhspyZZdcuB-M9yp8XJX15pXudmd5LonsYQrF0uKPv9fXh3zYiA-jt7uDpnh6WKwy7lnvev8WC91gNQmy9_cwlbLj9HQYltKRUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اصفهان نصف جهان
😍
#اخبار_اصفهان
در فضای مجازی
👇
@akhbareisfahan</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/akhbarefori/656347" target="_blank">📅 15:52 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656346">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/craFPWjX2g3ojJ5Hp8zaysB6YC7p6prHsgozQYIUMDsUULDoUZ_8YSSmI-cxX2WNrRjOAvyAepvj0eii1J1L4wuTdvbFP8K37Z0GOrogAtEOYykT4cC0MZqASzBFrIRLxSIRD3nZb7m9vOHF6XqmrxpbYc751GQcgGTmGmhK3z6xz__JxRojUWohtRT1Or_QXpk6qESkt-JtltipRNma3A6O1DnmOTLy2u80c7YDicbD0iO8bJjeQfwPVzBUqhWtLR8bz-1h-5hsYOpy_SgfSp6AtRORKE2cIuF92mlRHA5KdlejnGL3BZaI6Nz3HlZvt-H7pOm_qPDZBobXCo1zAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
از هر ۱۰ آمریکایی ۷ نفر می‌خواهند جنگ با ایران سریع تمام شود
هیل:
🔹
در نظرسنجی اکونومیست/یوگاو، ۶۸ درصد از پاسخ‌دهندگان گفتند که معتقدند که آمریکا «باید برای پایان دادن به جنگ با ایران هر چه سریع‌تر به توافق برسد»، در حالی که ۱۱ درصد با این نظر مخالف بودند. ۲۱ درصد هم در مورد رسیدن به توافق مطمئن نبودند./  خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/akhbarefori/656346" target="_blank">📅 15:43 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656343">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NNWMu--i7EdkfMZmh15pDzCwWqnI__yTlkaRW4NSoum3uVTJE8YBxPa0ep1m90uTveHmVX9cjRyhfdw5P3Hh8ezwDuW3Gguoy4fMHI37W0fF1_pZxGjOnckxuCucs8L1LqPHGYDpep8vLLB0DqEjhIPleZwEiTrZ8J8RmFdDAf2oQYXBH6kuM9C32bW7yDXKhMKTSZobbn1DMi4Frr_aL3ZJu2r-ISGu0U4lkety2RyFwGtwaEq9C6b7TT6OYO6CRtim_s2IYHXi9cLpNvQzp2fCEnzHHrBYekIWMJw7RJV203K5Oet1cFwBxKLc7SR5BxWhopTRa5OQBXb3JneHAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قابلیت جدید گوگل برای چهره‌های معروف و رسانه‌ها: ساخت پروفایل اختصاصی در موتور جستجو
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/akhbarefori/656343" target="_blank">📅 15:24 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656342">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39a54395ca.mp4?token=JkiSZBBZa57Q2Kq_Pjw3nMg22jRta-Yy5hx1ppNWZzUtxDgJfRIuwhyuZMyE9FTkwybvPZ9vtUei742x9EUNGuJKKB6HpgWcKFTFOvzKlNLhTaqhMzIzD5W8UNWZuxJ6NLW1wqy5Au1HYVQbNUNXmYzsyrFuwYsmwhpgkxdxtQsb8_-K_bwwLK0tqG3-igGi3S-0isQP382hKHO4phz8mc2w181QUvhgaO0opB_MjdI3OLCxAgC1pCIVHv_twt9u8mKWt8Zr0s2jsWO0tU2pqwf4BpFH_r57wewU6uCqaJU8mrmmnl-Lu_6xhtKPGo4p710wA04Tyn9vAhq_4ZAVwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39a54395ca.mp4?token=JkiSZBBZa57Q2Kq_Pjw3nMg22jRta-Yy5hx1ppNWZzUtxDgJfRIuwhyuZMyE9FTkwybvPZ9vtUei742x9EUNGuJKKB6HpgWcKFTFOvzKlNLhTaqhMzIzD5W8UNWZuxJ6NLW1wqy5Au1HYVQbNUNXmYzsyrFuwYsmwhpgkxdxtQsb8_-K_bwwLK0tqG3-igGi3S-0isQP382hKHO4phz8mc2w181QUvhgaO0opB_MjdI3OLCxAgC1pCIVHv_twt9u8mKWt8Zr0s2jsWO0tU2pqwf4BpFH_r57wewU6uCqaJU8mrmmnl-Lu_6xhtKPGo4p710wA04Tyn9vAhq_4ZAVwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روایت ثابتی از اختیارات قالیباف و مذاکرات اسلام‌آباد
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/akhbarefori/656342" target="_blank">📅 15:15 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656341">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d14e75aa6.mp4?token=atrUVplvp0_Hbl8_5i3gC-QpKqq-8ZcRoqN3mm4FKlDMs_00YCid19QLlqIOTtqTqh0CSDkg10F_FW94tFnG-QQyIIdFklJ57uXau_uyRwihl-CEk9aR0tDTyWXePksKsVVLGJMdzhJ1jI1wro9DXKN65O_Va1fN19Y3YYEtiBnpWciNkOHmjBtyN1op7xCo2MAc2OrLD-h7Omngh_0vfJby2UYoomInCKuE7H2P-wmCMglFHnjyHrlv0ZzGPsdeJ3E8vo_As7pPHx6lk_Oo1sLM8yCKP7Q9qE21XmWaHoRrbT7Ajx7-JHOLRZYDLchK41P7jVEQ6CBQZ6gCa9nm_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d14e75aa6.mp4?token=atrUVplvp0_Hbl8_5i3gC-QpKqq-8ZcRoqN3mm4FKlDMs_00YCid19QLlqIOTtqTqh0CSDkg10F_FW94tFnG-QQyIIdFklJ57uXau_uyRwihl-CEk9aR0tDTyWXePksKsVVLGJMdzhJ1jI1wro9DXKN65O_Va1fN19Y3YYEtiBnpWciNkOHmjBtyN1op7xCo2MAc2OrLD-h7Omngh_0vfJby2UYoomInCKuE7H2P-wmCMglFHnjyHrlv0ZzGPsdeJ3E8vo_As7pPHx6lk_Oo1sLM8yCKP7Q9qE21XmWaHoRrbT7Ajx7-JHOLRZYDLchK41P7jVEQ6CBQZ6gCa9nm_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شلیک اخطار موشکی - پهپادی نداجا به سمت ناوشکن‌های متجاوز و مزاحم آمریکایی
روابط عمومی ارتش:
🔹
پس از شلیک اخطار موشک‌های «قدیر» و پهپادهای تهاجمی نیروی دریایی ارتش به سمت ناوشکن‌های آمریکایی DDG-103 و DDG-87، این شناورها دریای عمان را ترک کرده و به سمت اقیانوس هند رفتند.
🔹
همچنین ناوبالگرد تهاجمی آب‌خاکی «تریپولی» نیز از منطقه خارج شد.
🔹
در صورت نیاز از موشک‌های با برد بیشتر استفاده خواهد کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/akhbarefori/656341" target="_blank">📅 15:09 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656340">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ff94c6303.mp4?token=cYM535HRya5x6w_dJvBJzwx0LapvtNdk5mCkODYFLXNJv9YivHc-0CuIm2CN_OftW4iFGjgMGvtqKorGmRcE5vbk1ZoDnn_u2NDdmcYxgnzZneuYVz6Wtas2l5WLnAXMvAsPdeER5R9aLgbsUxbg57n_0eG5gKn4AJ3jPHMD36vSUZ_iwg96y80BInr8kpZ-GejqGwZ7x0Uhm0g_JeVuXX-dXBQJtYETOMyzDh3B5t8UUmoQ27PcnerldKuEU-HpqEdog4-20zWMhkTIa7s1lRxadst4vzZfmRSbk84G7vAs42jmqnV8nqnbX4puIrmljriVCJVk-V7ZIqdBj5VUYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ff94c6303.mp4?token=cYM535HRya5x6w_dJvBJzwx0LapvtNdk5mCkODYFLXNJv9YivHc-0CuIm2CN_OftW4iFGjgMGvtqKorGmRcE5vbk1ZoDnn_u2NDdmcYxgnzZneuYVz6Wtas2l5WLnAXMvAsPdeER5R9aLgbsUxbg57n_0eG5gKn4AJ3jPHMD36vSUZ_iwg96y80BInr8kpZ-GejqGwZ7x0Uhm0g_JeVuXX-dXBQJtYETOMyzDh3B5t8UUmoQ27PcnerldKuEU-HpqEdog4-20zWMhkTIa7s1lRxadst4vzZfmRSbk84G7vAs42jmqnV8nqnbX4puIrmljriVCJVk-V7ZIqdBj5VUYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پست اینستاگرامی عراقچی در داغ دانش‌آموزان میناب/داغ ناتمام میناب
‌
وزیر امور خارجه:
🔹
داغ کودکان، داغی نیست که واژه‌ها تابِ بیانش را داشته باشند؛ به‌ویژه آن‌گاه که پای دخترکان و پسرکان معصومی در میان باشد که با رویاهای کوچک و قلب‌های بزرگ، پا به مدرسه گذاشته بودند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/656340" target="_blank">📅 15:01 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656339">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">♦️
منبع ایرانی: ادعای العربیه دربارهٔ موافقت تهران با انتقال ذخایر اورانیوم به کشور ثالث صحت ندارد
🔹
یک منبع آگاه نزدیک به تیم مذاکره‌کنندهٔ ایران روز جمعه گزارش رسانهٔ‌ سعودی مبنی‌بر موافقت تهران با انتقال بخشی از ذخایر اورانیوم غنی‌شده خود به یک کشور ثالث را رد کرد و آن را نادرست خواند.
🔹
شبکهٔ العربیه پیش‌تر گزارش داده بود که ایران به‌طور رسمی با انتقال بخشی از ذخایر اورانیوم خود به کشوری ثالث که مورد توافق طرفین باشد، موافقت کرده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/akhbarefori/656339" target="_blank">📅 14:57 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656338">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/92e2301c57.mp4?token=bw4EAWAu7ezICSvqV4WYM5xwGx18p5d1w3qrIiSquboDi3Nbw3gWECPeDDcCArvu2Kor10ClhgbVUqM9SwdK49PjOF58OQz7mKkU8_-6PqJj4etxV2OtPsRAQJz3WVQUvFfli85QummNYi1sqSyyVWKHcWGOCzoVTePWHHTthk32ofsNOJ__Vd50kVG5SWncSnkT2riB-AY-rnzdKDe43wwZlruf26iatzitEU9-zDzihxCrSX3lp-euIAMu806eqXNHCZI8SQEhKTSACB-zdsMOZefCMUA8-fdf8azhS1__VQNhcd2EyPpBcxhaqEeERpypjqNHlsMeK2rqQf7EjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/92e2301c57.mp4?token=bw4EAWAu7ezICSvqV4WYM5xwGx18p5d1w3qrIiSquboDi3Nbw3gWECPeDDcCArvu2Kor10ClhgbVUqM9SwdK49PjOF58OQz7mKkU8_-6PqJj4etxV2OtPsRAQJz3WVQUvFfli85QummNYi1sqSyyVWKHcWGOCzoVTePWHHTthk32ofsNOJ__Vd50kVG5SWncSnkT2riB-AY-rnzdKDe43wwZlruf26iatzitEU9-zDzihxCrSX3lp-euIAMu806eqXNHCZI8SQEhKTSACB-zdsMOZefCMUA8-fdf8azhS1__VQNhcd2EyPpBcxhaqEeERpypjqNHlsMeK2rqQf7EjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدئوی پربازدید زن ایرانی در رمی جمرات
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/akhbarefori/656338" target="_blank">📅 14:50 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656336">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Va9hgn3eg6yuivcXAnYQ53Gn-PhWCENVpsr_8FqCwGdCLNrzLglx5f8TX5DJxbqLedzyW-F9BldaYhTDuQX3w2Ffw0spVVY-pr0c55SMs6OqYwH1oniW_y6ywlOSD_wlqI6Zb7fTgpcjCWVofwW68NpLS-nkzx0acg6aZnpCA_Cx5FFyA3tDsh1LMKhs5UydrN_JmoVbmbjK-JMPVa79p-F1AXuJuN81ygsKpcIX5ZFc7z7AHNiwFE6V1vCRHYOlmLT-tpiTH4MannayKigOgmVfZsPEF1gGAxTWqnUyYhR9_x02CjQhdvpAI6X3v_mpEjwAhC0fshMVfmKdn6TIFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
راهنمای ویتامین‌های ضروری: مزایا و منابع کلیدی غذایی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/akhbarefori/656336" target="_blank">📅 14:28 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656335">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sXTKi5puDBEF_Vsv0-d1QWbPnvGh-JnTTnA5qACXdjGeu8g9mod30Y2afukdTlkg2UQ2bZG1GFNhqGarZNCvXVMjvTEVGTM8OUlTol7i_0u63SG3juZiqViTKXyHRHlkjYkB86o8PutPACHASr_X03qC1hL3fHHfVNYOVYCIb4OwG16kiXyetb_XutBFpAk-eZcd036pETLWnMmThV04yQ3P2RtA-9TyulUB9vzUKYHpQaXlQVOlV49kgx6dK9pcaAH2vdNsdUBui3_OClvIfW7MgSganQMrt0yZPu3_5Rz1Et0Np1opCiAkhUM2uSFsZYRWt6fwv1_FCYSQBr6dag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فراخوان خبرفوری به مناسبت روز جهانی محیط زیست؛ «ایران سبز»
🔹
همراهان عزیز خبرفوری، برای شرکت در این فراخوان کافی است تنها یک اقدام ساده برای محیط زیست را انتخاب و همین امروز انجام دهید؛ از کاشت یک نهال یا جمع‌آوری زباله در فضاهای عمومی گرفته تا کاهش مصرف پلاستیک، صرفه‌جویی در آب و برق و استفاده بیشتر از دوچرخه یا حمل‌ونقل عمومی.
🔹
عکس ها و ویدئو های خودتون رو برای ما ارسال کنید
👇
#ایران_سبز
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/akhbarefori/656335" target="_blank">📅 14:18 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656334">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">♦️
ابراز دلتنگی مردم به رهبر شهید در مهمانی کیلومتری غدیر
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/akhbarefori/656334" target="_blank">📅 14:17 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656333">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ec1c1c628.mp4?token=JB3UvMXnQP62z8vDUAIA2TcN7jrLnpEEfjUx26iyQDR0iO8612f7rPtSQiYI8LGBxQWHZ6P0i3P0i4EONCRxdsC0tjNNkqbkyYyO6VEzeUoexKVt5f2S085AEzQvZ0Y1nzwrYXiBIkkaQL0yzOf9ivJ6m0nvTeHH7EnqmpOH4IEX2DzSbHEuevyOsePV4t8x37omuLP-iJbpu5GwFEL2D-ycnZR5Fb0Rvarea_epiJff3IpVTVEwDOQwfqK0alSI26f_v6jMp-OgU1Br5JKMALWJBE2kg0a5dqpsw5610oYhBoN_lnsa5bOo7loFrsxtUJ0-aPhG_NxE8clNkVrK6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ec1c1c628.mp4?token=JB3UvMXnQP62z8vDUAIA2TcN7jrLnpEEfjUx26iyQDR0iO8612f7rPtSQiYI8LGBxQWHZ6P0i3P0i4EONCRxdsC0tjNNkqbkyYyO6VEzeUoexKVt5f2S085AEzQvZ0Y1nzwrYXiBIkkaQL0yzOf9ivJ6m0nvTeHH7EnqmpOH4IEX2DzSbHEuevyOsePV4t8x37omuLP-iJbpu5GwFEL2D-ycnZR5Fb0Rvarea_epiJff3IpVTVEwDOQwfqK0alSI26f_v6jMp-OgU1Br5JKMALWJBE2kg0a5dqpsw5610oYhBoN_lnsa5bOo7loFrsxtUJ0-aPhG_NxE8clNkVrK6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای امیرحسین ثابتی: آمریکا بعد از جام جهانی سنگین‌تر به ایران حمله خواهد کرد/ ایران را تبدیل به غزه دوم خواهند کرد
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/akhbarefori/656333" target="_blank">📅 14:15 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656331">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QDqSN4mbfFDRYnrmQAn9ull6mMFTcvDxuCX7X6rueIGbc0_sAJNXo7rgwEFpA7d2V7ThU5q5t1QmnFPFT5uDBmsqOPMa9sVxh387TtYJJvhm8kahnAn6CUxiA05qLckHJ_o4IYlyHKxPl_klTDqQO7qyQFRmzVd1gVfiV5klmznyFkVyktXziGYSwvkCpLsLfhVoB1nWkVH5wI5sgxb1VYG6k7OmP-eqoeHL4JUGS78mAZcheleET1FSFDTYiRmbULtg5Dd443gj85I5PN8Q3df3I4gxTaXLeHQlI1eZr89ZVl2lXHRK0a8FGgMHE1QliMV35lkKMXEfGhQpBqMI4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فیفا تأیید کرد که نقصی در وب‌سایتش باعث شد ده‌ها هوادار بلیت‌های رایگان جام جهانی دریافت کنند!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/akhbarefori/656331" target="_blank">📅 14:06 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656330">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">♦️
نماینده مجلس: میزان کشت خشخاش در استان‌های ایران بسیار بالا رفته
جمالیان:
🔹
در استانی که قبلا برنج می‌کاشتند، امروز به کاشت خشخاش روی آوردند.
🔹
با توجه به اینکه این محصولات خالص‌تر هستند، قطعاً شدت اعتیاد را افزایش می‌دهند
🔹
خشخاش‌هایی که [غیر قانونی] کاشته می‌شوند، جزو کشفیات‌است و به کارخانه‌های داروسازی تحویل داده می‌شود./انتخاب
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/akhbarefori/656330" target="_blank">📅 13:58 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656328">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1a3232953.mp4?token=UBmx3cHI6nFsp1P6MCePo_BMOcH3QrojGvufz4TE4ZzvTQGZ0ZsFrh9gv5xSmsoyXhmCZhqmkIUf2VhydxE74Ce1-AnQ5134GX_2rPnMJ82FED1kxeBkudDtE9MwlS8lb_mXsbxcbwkLQ2S3YRL1Yn12XVmPqBkHusQfA8RTlN-9JcHbx-2ImpaDYzTy3BxwRsiFxBO_NfnkqDaWpQDuy7rDHb9I9ebiTLP5EH1ohJMyJ-mxAFMLp1IfVuepbiiBs7P88oaQP8p-MC3UdeRNFQ83clVqSCp9ohL3UEfUGBy6piBCACxqNw1gIYBs7o-TYL9RePgiH4ytNseAvJWM03BGMjoUmxWh6EAp_USTeSrgfOilf3T6kVFjlZv5Lbe6dhu1AqJwuLzWD0lcbmqQUC-YapGC3PNOHo5CLJv-cydFpo7ubE8_8z2WGNu-IwOCYTEdu-aHtSAmIIXsOPcU-uzgQ5kgUqWdPUHcdg0qpDO-OPz_xEfN2p4FLsT5iVZQ0G7nJcRePMpxpgJ3Wg7-YgiImilj_4pWNx8zZVrm9EFW1wtBN5FJQptmRW3d9j-dF1INby1H7suOzFhiu3EPUzsAaqOn0kshCSY__rpbUhHwLeeVgKvq39tAWYdwtFDyTT5yAxz16RDKOrGizfbQnWNg53vsB9D7PCtblsCdIMU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1a3232953.mp4?token=UBmx3cHI6nFsp1P6MCePo_BMOcH3QrojGvufz4TE4ZzvTQGZ0ZsFrh9gv5xSmsoyXhmCZhqmkIUf2VhydxE74Ce1-AnQ5134GX_2rPnMJ82FED1kxeBkudDtE9MwlS8lb_mXsbxcbwkLQ2S3YRL1Yn12XVmPqBkHusQfA8RTlN-9JcHbx-2ImpaDYzTy3BxwRsiFxBO_NfnkqDaWpQDuy7rDHb9I9ebiTLP5EH1ohJMyJ-mxAFMLp1IfVuepbiiBs7P88oaQP8p-MC3UdeRNFQ83clVqSCp9ohL3UEfUGBy6piBCACxqNw1gIYBs7o-TYL9RePgiH4ytNseAvJWM03BGMjoUmxWh6EAp_USTeSrgfOilf3T6kVFjlZv5Lbe6dhu1AqJwuLzWD0lcbmqQUC-YapGC3PNOHo5CLJv-cydFpo7ubE8_8z2WGNu-IwOCYTEdu-aHtSAmIIXsOPcU-uzgQ5kgUqWdPUHcdg0qpDO-OPz_xEfN2p4FLsT5iVZQ0G7nJcRePMpxpgJ3Wg7-YgiImilj_4pWNx8zZVrm9EFW1wtBN5FJQptmRW3d9j-dF1INby1H7suOzFhiu3EPUzsAaqOn0kshCSY__rpbUhHwLeeVgKvq39tAWYdwtFDyTT5yAxz16RDKOrGizfbQnWNg53vsB9D7PCtblsCdIMU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
از عجیب‌ترین چشمه‌های جهان
🔹
در یکی از چشمه‌های ارتفاعات دهلران به جای آب خالص، قیر و نفت خام بیرون میاد
#اخبار_ایلام
در فضای مجازی
👇
@akhbarilam</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/656328" target="_blank">📅 13:48 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656327">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HoF2HiYGkkGXDsrShsOMvqp5k55TYCspsCjLS17TYKFubVGR4BQumwQM8PBUlxLayK3GhCZp6K3c0bPpvOqfKZ5q9seJ3sUDNMRvFBVG8kNTrazGvHM4y5g0KfP1Olo3zCIxdCs-8QBgZoNo965glkSswAub6_wVgewE9YpfmkTQXCNlSEMSbc_IqKu-Ycaqcb6mzSbp0r5D5Vx67KzQhbrBt_7zrPnrg8oIMENQhgAWpyderTDfSUD52l6ufYknd8twx5y9rgyNmFK1N_Jeio8wy37SlJGg0ZH2cI8IH9aChlIBun9MpnqMTzd8IUexVJgbHxksMZscpO8aQjs-Og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تیم منتخب مسن‌ترین بازیکنان جام جهانی ٢٠٢۶
#جام_جهانی_۲٠۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/akhbarefori/656327" target="_blank">📅 13:38 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656326">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">♦️
سرنوشت دارایی‌های مسدودشدهٔ ایران همچنان در هاله‌ای از ابهام
🔹
در حالیکه یکی از اصلی‌ترین خواسته‌های ایران در مذاکرات، آزادسازی دارایی‌های این کشور است، شبکهٔ العربیه مدعی شده است که ایالات متحده همچنان با درخواست ایران برای آزادسازی دارایی‌های بلوکه‌ شده مخالفت می‌کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/akhbarefori/656326" target="_blank">📅 13:32 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656325">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">♦️
از یک اتاق بچگی ساده تا یک سوئیت لوکس شخصی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/akhbarefori/656325" target="_blank">📅 13:28 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656324">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c14e51c158.mp4?token=ZORfgDAStcrzzrKe3iiOEqFbAl2do1yPOpF4XXPjEDGP9SY52G06tpRNyPgPWIEwE2F3A0ZSiS-b9xdi5QlMSl5G1_N-HWq0jAGUvshOiZrRpRfnd1jnLu3vuZEBaoQx-DOumCf_b8sayamt_TdFLFL4iK-FnfdadwUVLwdUtYKaU5iYD4fhB-GeZrKXegWJ3b6gF7XtJtniFR93DPHWPEVBYS655ZJCKhozUOgSZclPwqx06TGqJ6lJfY4ysdTXqDATT0rMAXJgIFOreJplkB-vKvAuEVoDPuRnqgTUqa-vzMv0SD-oSfYqWK9LAevSLvlY_SYgQ9h--aOX2YbK5rTpO3vu3Q9YQlN9lFhXDaMXRiFSwUp3GK2H49446bUCn1ouzqkKVzJVgiByBnfVzGrKqxAZUyVtbsk7_9tKlEpgFuf2pdlTD97xFqTnjFtefcym9cEKD-KjqI-irKKncBxi6_3Iz5CJrRhzSjKKZ0Y_va2P5jP5jgAqNxtUslPj-NX7QNjq13h-FvP0fGoof48U0vuQh-XEnlmSOEatczKj8w_pbPuBPR0RH9W3wqW2X_u45tm8efqKYbeY5rIkzXPUGjmZ2XC6MQxK8tSvqtfCMv6hd2O0dJO1kc-dxGvCYL0DCy5wIXJRfJ3oKXEqBevlaYXXB6XlYQFhAVc4A2M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c14e51c158.mp4?token=ZORfgDAStcrzzrKe3iiOEqFbAl2do1yPOpF4XXPjEDGP9SY52G06tpRNyPgPWIEwE2F3A0ZSiS-b9xdi5QlMSl5G1_N-HWq0jAGUvshOiZrRpRfnd1jnLu3vuZEBaoQx-DOumCf_b8sayamt_TdFLFL4iK-FnfdadwUVLwdUtYKaU5iYD4fhB-GeZrKXegWJ3b6gF7XtJtniFR93DPHWPEVBYS655ZJCKhozUOgSZclPwqx06TGqJ6lJfY4ysdTXqDATT0rMAXJgIFOreJplkB-vKvAuEVoDPuRnqgTUqa-vzMv0SD-oSfYqWK9LAevSLvlY_SYgQ9h--aOX2YbK5rTpO3vu3Q9YQlN9lFhXDaMXRiFSwUp3GK2H49446bUCn1ouzqkKVzJVgiByBnfVzGrKqxAZUyVtbsk7_9tKlEpgFuf2pdlTD97xFqTnjFtefcym9cEKD-KjqI-irKKncBxi6_3Iz5CJrRhzSjKKZ0Y_va2P5jP5jgAqNxtUslPj-NX7QNjq13h-FvP0fGoof48U0vuQh-XEnlmSOEatczKj8w_pbPuBPR0RH9W3wqW2X_u45tm8efqKYbeY5rIkzXPUGjmZ2XC6MQxK8tSvqtfCMv6hd2O0dJO1kc-dxGvCYL0DCy5wIXJRfJ3oKXEqBevlaYXXB6XlYQFhAVc4A2M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای امیرحسین ثابتی: آمریکا بعد از جام جهانی سنگین‌تر به ایران حمله خواهد کرد/ ایران را تبدیل به غزه دوم خواهند کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/akhbarefori/656324" target="_blank">📅 13:16 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656321">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WaIdFO2feRYwd6IHr0yfheUPsIouuya4pP0cZTDr28GMXPEg8g4HqQ7jxwZeZKlsmH2XJ-tcViuCN-_k-KmxByMTWLDANJjkJTEZmBrOpQkVODb6TeuB3MYrfTyQWPEklCkHATeglB2PwyARucd-RhEOzP2-g2p2X0dOtyRPvT_01ZbUrQuYhr7rzBRX86OOZyHl7xwky0EiKr_bVMWU9lW-G8m6Q55zrKMI6rM1evlzdzPvOzkD1nvXHwWCMs1ZgkTITQgIbpDYYO_r0KjJOckP3AGQ4ltPqJoJJTkbngWncKYvGgnYk9q61XVsG2smlPQsh26BGSKGiG7D_PicAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bkG2yXc4yDDGDhjIGlGP47XCeC2AyhGdvJP80iHytIzEliY-pnsWEKCqKm-BuIOPmRwrbYoAFsQi2Q9U68a2j9VDmeAq2kvJGkHzSbU9IIc8B9y5XyFQNf4VVWwHsMKtYrNVkDAnZO-79yczIxxv_SZpCge3IAhtUKn7yhY06GCO3vxSbX18muM_wLBhITfAns2Mux5-RbFDxJd-D3mJmZ7URMz54yL1VuGFL5OU480zVzb1kd0kzgarHg65UgeFcNkpKuo8sLBABxfRpwBBA0wN8z_gkFwoy-3WiHgkfq5m5kvwgIAblXB2o3yhLN73tXDI6wu5eZd3SHgghrbfRw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
تخریب کلیسا ثبت‌ ملی انجیلی شهر مشهد
🔹
تاریخ ساخت این کلیسا به دوره پهلوی اول می‌رسد و ثبت ملی بود.
🔹
هنوز خبر رسمی از علت تخریب منتشر نشده است.
#اخبار_مشهد
در فضای مجازی
👇
@Akhbarmashhad</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/akhbarefori/656321" target="_blank">📅 13:04 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656320">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">♦️
برگزاری مراسم سی‌وهفتمین سالگرد ارتحال امام خمینی(س) در حرم مطهر
🔹
مراسم سی‌وهفتمین سالگرد ارتحال حضرت امام خمینی(س) با حضور پرشور زائران و ارادتمندان بنیانگذار جمهوری اسلامی ایران در حرم مطهر ایشان برگزار شد.
🔹
این مراسم با تلاوت آیاتی از کلام‌الله مجید آغاز شد و در ادامه، مداحان اهل بیت(ع) با مرثیه‌سرایی و ذکر مصائب، یاد و خاطره امام راحل را گرامی داشتند.
🔹
همچنین در این مراسم، پیام رهبر معظم انقلاب اسلامی به مناسبت سی‌وهفتمین سالگرد ارتحال حضرت امام خمینی(س) قرائت شد و حاضران با آرمان‌های والای بنیانگذار جمهوری اسلامی ایران تجدید میثاق کردند.
🔹
اقامه نماز جماعت ظهر و عصر به امامت حجت الاسلام والمسلمین سید یاسر خمینی از دیگر برنامه‌های این مراسم معنوی بود که با حضور گسترده شرکت‌کنندگان در شبستان‌ها و صحن‌های حرم مطهر برگزار شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/akhbarefori/656320" target="_blank">📅 13:01 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656319">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">♦️
موافقت رهبر معظم انقلاب با عفو یا تخفیف و تبدیل مجازات بیش از دو هزار نفر از محکومان قضایی
🔹
حضرت آیت‌الله سیدمجتبی حسینی خامنه‌ای رهبر انقلاب اسلامی با درخواست رییس قوه‌ قضاییه برای عفو یا تخفیف و تبدیل مجازات دو هزار نفر از محکومان محاکم به مناسبت عید سعید غدیر خم موافقت کردند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/akhbarefori/656319" target="_blank">📅 12:59 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656318">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oSs1n1Swt-Cmpjpfw71L1k4Le-fOGy_20LIDt6Q2fMNdd8Bf5yVwfvIZox8iqw7SKmTJ9RuMoXaKHk6DoABjvBQt1R9q98j20VfP3oeByOZiDQgM1y-kdsB6Vre7lDAkdh2iN70rZ2BSisKUmT8JQQf7mYUbbdbAbdUw737zrfFUi4ai8TlQQRQ02nkyqpobb77t7KVv-FDur6Za44vXGXQaDk4NemERA9PanISIuwXEDUEhvtmNdbyHB8Td2OYqcWNX7YuS9wWhiue4iTiifkPmb8n2DL9DGYvk6_de4dAIFVW9xgprfaQNXvXzhEFLIN8i3rWvlZVq1aVm78Qg4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بچه‌گربه‌های جنگلی، مازندران
🔹
حامد تیزرویان
#اخبار_مازندران
در فضای مجازی
👇
@akhbarmazandaran</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/akhbarefori/656318" target="_blank">📅 12:55 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656317">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47f690f90a.mp4?token=kc2eZxIPM3QZzojRTqrJmY_J-fK4xyHvC_Laex8TMXN46-342MfM-MnaxBB7_5JcktdioEYS7WK1FjLLUpwuFSmU8hs0rlg5Vlfd6oXuv-AlygdSaHpuczfCfMVUZhoCJsVEBGPTUYjuhmAQBtVJFZ4n8udGOfMDdWcmr7y5QoW0osY1pk4U82SCQ-oDMqG6h_gpY83YBn_GkZUr-inxE0sAsvKWOtQVmB0nuL43Ri2vW8-q-5aHKlQqUyHFrI1fwC-i6pG7RXRJdf72w0-ixmo9ZU-Q63pcMUlzfqcs0UHRNNnG_hFssohhgTieZZcOLIUxjUtjDyJyAEhoK2O-w4mZlWy86xggfTRmf3ZfLm5ib3SHsDqesuDhXbIN75Q8CgJeiALaa_jzUcRmkLMm0cl-VUuvePslU7u7ugnC5zjheS4IVQ0wKJVAZn1xmsshP48jPoHaTYBMo667DJ2i-7iy3ovrH8iZ5krRWxNUQVri91HAoLA_37AuPQsRpn4xZdGco8y9XCKH1TQala9ooYd0tklPImGZcR8gEjRk26pwBFGu3fmQbG0MwxVqznEEBEDrRwzuJMul9cFZWjcd3nz3j1i_JXzNIIrQHymDMr55-G7cOnGLbLk8lxr_ZsmFW86VfDItVmVuc5CCSw-JF0tzerKSa15pZTuiTFvIwSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47f690f90a.mp4?token=kc2eZxIPM3QZzojRTqrJmY_J-fK4xyHvC_Laex8TMXN46-342MfM-MnaxBB7_5JcktdioEYS7WK1FjLLUpwuFSmU8hs0rlg5Vlfd6oXuv-AlygdSaHpuczfCfMVUZhoCJsVEBGPTUYjuhmAQBtVJFZ4n8udGOfMDdWcmr7y5QoW0osY1pk4U82SCQ-oDMqG6h_gpY83YBn_GkZUr-inxE0sAsvKWOtQVmB0nuL43Ri2vW8-q-5aHKlQqUyHFrI1fwC-i6pG7RXRJdf72w0-ixmo9ZU-Q63pcMUlzfqcs0UHRNNnG_hFssohhgTieZZcOLIUxjUtjDyJyAEhoK2O-w4mZlWy86xggfTRmf3ZfLm5ib3SHsDqesuDhXbIN75Q8CgJeiALaa_jzUcRmkLMm0cl-VUuvePslU7u7ugnC5zjheS4IVQ0wKJVAZn1xmsshP48jPoHaTYBMo667DJ2i-7iy3ovrH8iZ5krRWxNUQVri91HAoLA_37AuPQsRpn4xZdGco8y9XCKH1TQala9ooYd0tklPImGZcR8gEjRk26pwBFGu3fmQbG0MwxVqznEEBEDrRwzuJMul9cFZWjcd3nz3j1i_JXzNIIrQHymDMr55-G7cOnGLbLk8lxr_ZsmFW86VfDItVmVuc5CCSw-JF0tzerKSa15pZTuiTFvIwSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لاوروف: ادعاها درباره برنامه هسته‌ای نظامی ایران «بی‌پایه» است
وزیر خارجه روسیه:
🔹
هیچ مدرکی درباره تلاش ایران برای ساخت سلاح هسته‌ای وجود ندارد و این اتهامات «بی‌اساس» است. تاکنون هیچ مدرک معتبری ارائه نشده که نشان دهد برنامه هسته‌ای ایران به سمت تسلیحاتی شدن حرکت کرده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/akhbarefori/656317" target="_blank">📅 12:46 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656314">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kfwnwXKGqOlAbx0Br8O1zSogaITo4_zHrTXAMmUJJ1u5Dmr2q_hMq_qua126Y_PwVyvicoS2SPkDKwifPM8biLzX-W9TtRsWjYsrG4qmExwCGyurGnYX7kpnOJjlawax558ZbDGVyB-HTKkvZoKL6HwUDDKoIU2C_dkNXFBiNKttpcoZIqxGwpvtbDbAvDDNQXvOMZZN2e5MYojj3_YEy2pK_ER-RXRtNMEwdAavZCMG7IEHGdj0x-9H6nHR0a6tmyYSUz211H4pT1TcEUyHCN2njpuemL14HLgKVUA-ABssZdHtsHWNk0PEEEn6EjlngMBW9q_jTTqCXE1PedMB_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JaYmntl1vTT9wG6TK63O4ZASl1Gd9cejXka4Zl-nXJbb2cRSZ81f2MasA7K_-PCJWx_ZGZrvIEBxDX7cvPrv_1zxANF4lmfGVkZSelLR7DMoo-eAszqLLJK3aC0-921iHfxcNnicLGUegz10gTdUTmZJ1tVVuFLpfLlMBZY_Rft-GTP0Jd5IRFA6e4D9BsDNkBZke_-blqHJqqk1OLZTexnoN8pncI9izWTrI5gaUMMgsum2xtMY_ukqJR5bAOO1S8h-_9kOCZ8e4YnJ0RHvKszJY61ozDO3Hf8GpjgJ9FJsmIBdoTmAUGuxSuMeXTM5oASbwz9qiUOb-ZRC4ZPa5A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
نخستین اطلاعیه‌های ستاد تشییع و تدفین پیکر امام خمینی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/akhbarefori/656314" target="_blank">📅 12:30 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656312">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/010c76d2c7.mp4?token=E9mjGTTxDOjccMh3K1Kb_Cj5V1LiCHNfpvjPb4LkEc2nYVYJL5816B-cwZAdxQ_ef6lZZ8VLLeveT6dFChYezPQ49cISAsZNkM-A_zQhXbEFF_ByYqr70Kp7y_gZ3RtqGorCKims3quqQNtov6JIT2ddvLtM9d2g9Y5dmQGPA6rkaHEytiO1IdFfs2LzOrt6AYZyr18EF5HcsYfAby4GLKgU4pvpLhbsWm7Rp26ES09YfGDksTRYEz8aJkpBzX4wjpJZNQAhXQEuHOuY1DmDpkiOVEwlMiG74n67JY5JW-ZXg6ibL3MCpr_jxPcXtD8-9nl9Lh34J0V45fDju1UOwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/010c76d2c7.mp4?token=E9mjGTTxDOjccMh3K1Kb_Cj5V1LiCHNfpvjPb4LkEc2nYVYJL5816B-cwZAdxQ_ef6lZZ8VLLeveT6dFChYezPQ49cISAsZNkM-A_zQhXbEFF_ByYqr70Kp7y_gZ3RtqGorCKims3quqQNtov6JIT2ddvLtM9d2g9Y5dmQGPA6rkaHEytiO1IdFfs2LzOrt6AYZyr18EF5HcsYfAby4GLKgU4pvpLhbsWm7Rp26ES09YfGDksTRYEz8aJkpBzX4wjpJZNQAhXQEuHOuY1DmDpkiOVEwlMiG74n67JY5JW-ZXg6ibL3MCpr_jxPcXtD8-9nl9Lh34J0V45fDju1UOwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
صحنه جالب در نشست خبری رئیس‌جمهور مکزیک با توپ جام جهانی ۲
۰۲۶
🔹
در پایان یک نشست خبری، رئیس‌جمهور مکزیک، چند توپ فوتبال نمادین جام جهانی را به میان حاضران پرتاب کرد.
🔹
در این میان، یکی از خبرنگاران که مصمم بود یکی از توپ‌ها را به دست آورد، برای گرفتن آن به سمت جمعیت حرکت کرد. او در نهایت موفق شد توپ را تصاحب کند، اما درست پیش از آن مقابل دیدگان حاضران تعادل خود را از دست داد و روی زمین افتاد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/akhbarefori/656312" target="_blank">📅 12:18 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656311">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">♦️
تاج: انتظار داریم ویزای اعضای تیم ملی به زودی صادر شود و بازیکنان با در دست داشتن ویزای آمریکا اول به مکزیک و بعد به آمریکا سفر کنند
#جام_جهانی_۲٠۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/akhbarefori/656311" target="_blank">📅 12:13 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656310">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LGjDHueXSGybar-EOEh5fYbDV4kUUM5SfNvEVBvv7-bLYRqXpEmTpKcZNdWzOMDKKmPfb6cvS6DEBtH1B5P7CLg18hW3-NDdCsGNzxg3bTXG382hQai_QktCNXwducGZF5bvv0-vLHZRE2T7ziSpkZfQLjI8F2o06O2OHRl4a72CblnPNU5GzQQJC26bXS-M3Mk5v35RFDeI243L77wT3FglgV_AGxchnZCaH4_dUlQfZ2MZmWGC_kVZtpxcNL4l9JXkcRKyPVhBKWX8x2t0EUrBUPctCndaczUmkWtgGDR_iCdrmq55fuaEjZdTPvXaw110uEPpcTEpCpSkiVDl1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
جنگنده‌های اسرائیلی شهرک قلیله در جنوب لبنان را بمباران کردند
🔹
شبکه خبری المیادین از حمله پهپادی رژیم صهیونیستی به شهرک‌های «تول»، «حبوش» و «تبنین» در جنوب لبنان خبر داد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/akhbarefori/656310" target="_blank">📅 12:12 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656309">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5de025c702.mp4?token=M_irtnwxH_4Be3Hde_r3uvUfR_uwifDTGkAVmc3F51Jtz02-6VNksM6ayYjBeRuRLprUMIYqvxVPt9G37IKQdCAbCEqv4UAu1YilOHtmR3lCYMaWIsxw7s8j9-hNonY0Rrz9Eogalc6mFWg5dSe7i8om1wfPU9jkAK4bugZTvGVDFYa_BXgkFBW6QPNRw3lAbSWlkmtIL7eEI3X_ciyFe0PZnA4iMsTfB2iwQhbNzycrHGQ06WZNXposWGeHBZX2QlrCidlFEbUm3IRS64M34mrxHJje1Q_FS_fPE3PD9_zel2cxZy5rEnUMKWH5IYQR8angrDVgvg7cdWbwDNcpFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5de025c702.mp4?token=M_irtnwxH_4Be3Hde_r3uvUfR_uwifDTGkAVmc3F51Jtz02-6VNksM6ayYjBeRuRLprUMIYqvxVPt9G37IKQdCAbCEqv4UAu1YilOHtmR3lCYMaWIsxw7s8j9-hNonY0Rrz9Eogalc6mFWg5dSe7i8om1wfPU9jkAK4bugZTvGVDFYa_BXgkFBW6QPNRw3lAbSWlkmtIL7eEI3X_ciyFe0PZnA4iMsTfB2iwQhbNzycrHGQ06WZNXposWGeHBZX2QlrCidlFEbUm3IRS64M34mrxHJje1Q_FS_fPE3PD9_zel2cxZy5rEnUMKWH5IYQR8angrDVgvg7cdWbwDNcpFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حال و احوال جسمانی‌ ناراحت‌کننده خسرو احمدی، بازیگر سابق سینما
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/akhbarefori/656309" target="_blank">📅 12:10 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656308">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">♦️
ادعای سی‌ان‌ان: اسرائیل در دوره جنگ علیه ایران به آذربایجان نیرو فرستاد
🔹
شبکه سی‌ان‌ان مدعی شده اسرائیل در جریان جنگ با ایران به‌طور محرمانه نیروهای ویژه نظامی و اطلاعاتی خود را به جمهوری آذربایجان اعزام کرده بود.
🔹
به گفته دو نفر از این منابع، این نیروها…</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/akhbarefori/656308" target="_blank">📅 12:06 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656307">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">♦️
ادعای سی‌ان‌ان: اسرائیل در دوره جنگ علیه ایران به آذربایجان نیرو فرستاد
🔹
شبکه سی‌ان‌ان مدعی شده اسرائیل در جریان جنگ با ایران به‌طور محرمانه نیروهای ویژه نظامی و اطلاعاتی خود را به جمهوری آذربایجان اعزام کرده بود.
🔹
به گفته دو نفر از این منابع، این نیروها از چندین مکان در جنوب آذربایجان، در مجاورت مرز شمالی ایران و نزدیک‌ترین نقطه آن تنها حدود ۶۰ مایلی (حدود ۹۷ کیلومتری) شهر تبریز که اسرائیل در جریان جنگ به آن حمله کرد، فعالیت می‌کردند.
🔹
دو منبع دیگر گفتند که یگان‌های ویژه کماندویی نیز در این مکان مستقر شده و مأموریت‌های اطلاعاتی و عملیات پهپادی را انجام می‌دادند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/akhbarefori/656307" target="_blank">📅 12:01 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656306">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RWjoS3B37WhrZgippOb8UM0VkkV7_K8-6dJ6TlAtVb7xpAFJ8hsxFkL96nCDFWcN5ErRhr9Pkh3KIiVE3YnglYSUQFQmhtn7hMcliyUREYuWt7H5UhdDDs6bHaW7Y58VRHI_c0VFaFhBnn3fRlFVPjgrkcdm9JtvcVRt1W3uQ_7SAp-MssrgPGYUDkXe64PMe6M3-5e6_et9_5DRpgeMsfjkGKAu2kVyBhbwN6-RAPalXOeEWIR6tCUTqHHl-R3zc6jXjIldJiKNevOujI9yU2qnIKhY6PNoLxsXZ0bddP86NwWLfgJ6Q0x2jDT8OjAZsTS1m9Q3tU0mx18mPI7ong.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سوتی اطلاعاتی نیروی هوایی آمریکا
🔹
نیروی هوایی آمریکا عکسی از عملیات سوخت‌گیری جنگنده‌های خود در اواسط ماه می منتشر کرده و مکان آن را «افشا نشده» اعلام کرده است.
🔹
این درحالیست که در پس زمینه آن جزیره مصنوعی پالم جمیرا مربوط به دُبی کاملا مشخص کرده که این عملیات در آسمان امارات در حال انجام است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/akhbarefori/656306" target="_blank">📅 11:58 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656303">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/COcJbpb6qHa0SSQjkixMTkfajpKn4WqCmARB0XFoCLSa_BvDjDuxcx28gTelWozV5ernBeHTOX86YDzOX_xTtoVoqbnF8GWzL9iPDWIEDxtJ9qGkm2eA-GXI87KgcG2ou4c96FsYlUvbYaA3bnU7R_KIwEW0l92lrW8jviDP-xmFIjBiYLpUv7zhtcQG3IPySmOVvCviV3dCeTEVXFOtH1ATIGtTHi2ddVK5TuT7sfAd0jVWMD0wpr083n114NuOWCyp7FiV76kvD5nzsQgEw5KcNiVEKOj0Rf-zIdhLSk0KGKnmIXgjJr43nqW2u3zhG8ISxIJTK9vfkNeSmlLO5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Zr4jHf9MVTqpoFwcGvfh8k4Vcux8okk8KMr4ZhK5NTaL4p_-TW3oGvMvK_K7eFXbueFs3R8JXbPIcrL5QVlyKCjPH-qqmWZHb-Ks2OTVeLRHMaEC7ydDpgwO8TKIpgaEwoJGIFcuRQwcGBcDiWl4AYdklnvfB2uPCAD3Z0vMa4UwLLD5HyXfItVzvlWphXWBDxeNjcNAjxyXfj3GkOeNJgMYoigLvjkFHUjtvOtJFnOco5Mv27UzYA48t3mJiH7HrzK9KCXVNCKEhQTWpriLtf4s9yNukmi8ZzowJmmHDzBZj9iByNOJhvRGDOwW0qeINsc8WKwNToCUHcytzP8nIQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
خلاصه اخبار سیاسی، اقتصادی و اجتماعی هفته در یک نگاه
#مرور_هفته
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/656303" target="_blank">📅 11:45 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656302">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JldT1X_SeyM0_k0RVsggXhuG81YObPwsTytYCVLlajtR6rHdW3RL2ELPv0J6ILySvG28cddPq-zTrPQt4JYxX4uruREVzsh0zWwT6Nq-cyfNiMwFUZHd51koKQf7kjKx9jexJpn86O3z5g4XFHdj6hGNIi7h_1S_hUtMRnppWTYFBKr-oB47R0-4srsqHTB51mokr_nBnQR5n7wUmuliANQ0anyAKcOIGObpyTNhcFY1qZryJr325KlgLI2yrwi3RgDd0ny_mQzyR_KHQXOPHYqdZseYyBhOsG-8MGNl1YEsEjpjYfexUHL-bdgoyXwj_eiPqMbRLCdUCn-EwCl-Ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تعرض رئیس جدید موساد به مسجدالاقصی
🔹
رومان گوفمان، رئیس جدید موساد، برای نخستین بار پس از تصدی این منصب، به دیوار براق در مجاورت مسجد الاقصی تعرض کرد و آیین‌های تلمودی را به‌ جا آورد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/akhbarefori/656302" target="_blank">📅 11:38 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656301">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ndrxDNCi6Ypy2rRaevMuc66R3aSX0RKHC4U-LvDsgujDbaHW-qIt6kx4VoETnOMrOXw3NY0OmP33orbRzuTDN9jzkkNR2KN1nNqez2-JQ25cCmQAjAB3nXJ3AjauXRev_5Mw4QBnyiqLUJ6RRyiVUr10G1CmqLmIhbcCqJ-UXxW9pPxci62Oq1dr3TKTiUFwjfuS6QvivWlh-JThhl26J8dL70PS3dcHidUzuhDkGlLPvQigArXZPuRCfEKwswJbPh1FMUijq9hpHLb4_vCaDRsW-rM5PVG1EZ8mkz0FiOYkcsr8imUV7qjhbySIw3SgjppIQhYNzFT5N6EwiQUr6w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/akhbarefori/656301" target="_blank">📅 11:36 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656300">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/42b1f3b02d.mp4?token=mNakMuWE0qDkljF1LdIcG6_abF6wQByBGe9nn8yrsnUgxs4DHiDlaQpJQbG1Hlw-aTKlym_EPvUkPM6EijF7gVLD-wlAF98F6ni3lzhSp9EsOTddfos5yh-VaIHgHnHmGPzMFGb3hMmYjURqAEQionUKMy5cjaRo8OVPXDIkzfHtCjSpu0cn8KQ19PiZKCNEjRdO5iL9veQLO3RAq4dC3vOMHLdvEvb5HYsLxFEK8TiMl6vjhUAsQboPLTx0brOVVRk3gNJ_R3w_w4RC-MpxsGYfi5oPHlvGwncEQAwyyG59R0vnLoG4C_fZnPjTKfoz5DpVI38lv7LtqjueeU19xw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/42b1f3b02d.mp4?token=mNakMuWE0qDkljF1LdIcG6_abF6wQByBGe9nn8yrsnUgxs4DHiDlaQpJQbG1Hlw-aTKlym_EPvUkPM6EijF7gVLD-wlAF98F6ni3lzhSp9EsOTddfos5yh-VaIHgHnHmGPzMFGb3hMmYjURqAEQionUKMy5cjaRo8OVPXDIkzfHtCjSpu0cn8KQ19PiZKCNEjRdO5iL9veQLO3RAq4dC3vOMHLdvEvb5HYsLxFEK8TiMl6vjhUAsQboPLTx0brOVVRk3gNJ_R3w_w4RC-MpxsGYfi5oPHlvGwncEQAwyyG59R0vnLoG4C_fZnPjTKfoz5DpVI38lv7LtqjueeU19xw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یک ربات انسان‌نما در جریان نمایش کونگ‌فو در باغ گیاه‌شناسی ارومچی در منطقه سین‌کیانگ، هنگام اجرای حرکت «لگد پرشی» به شکم یک پسربچه تماشاگر لگد زد و او را نقش زمین کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/akhbarefori/656300" target="_blank">📅 11:33 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656296">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EKwfXJO54a5EoX9g1GTU6CacFvEJRyQqB0qdNAUhMrBbvJVGr-fkFNq7EPxMAp2TP4MndI5t8HwIgrSAzJU0kOl8VCTONwQARyotwwWPIntQ-RK-2xnGOsMhTNvOEE6HuEKsZq5ql3NsZ-f2i327i4d-zofsTgKRjP4Dbbh-0ZaIYWwWxuYkS8SSLqxlk1AfVLLjhtac5SP_R71IGcAcd4VFmWLupsSemcFRTB8hZQhLXWD3Lj4t8PpQf9Wu-PCLI5buCONa1_3H4p8Mx2_59iNIo7o-VCabPE4G86jxGxMTsu3GrMFMnGQXk1D2fMBIoELth9p2qKLAtJUp9luX9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ntUgxLUXFTXt3_TNSmZVeGvSufO2M4d9WT7uqqIblQOYXAq9k0piObkkkdVb922Iz3CfKC4o3r237XYuvv-wqOrqeB3ILkmRec2OWGqg-7Mlm5DLXDeIMmjWYO6OeYZE-qC3J3_OgTTRXeDUmDfoqjAPNon2zZuzonLRerOe-hQ41asPs6z2xoEIRvGu-D3lCNwYQgOw39qaionPzL9nGOk5nrbQ7wbImglOW8Dp39dT3a11mA7Ip_jNBhDzJePkUXiL3GHiNnm_2BqU7uLKVQoHOf7OEgeM2H9QRXP_r9L3m5yDNKYitVETdJwkyGzN3u8Gb5uUvvhjRNgUakobMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hYNzx3xBJsIbteLe0caM3CS7wXdAXS4ekP8Spq5miFyT7JvzPzg-_7GeJyLvtnfxEzk7-_54JCTxL80OZxOWPwwHoJE8iP1jiEo6GP4TxUhVZx0rJa3YrpkrfAWyntSzOls2JgpTGK-xnXA6qUbqkJeJ7wld6JEhpTpinXtfhlNrAx2V6UNxYyk7QcREWs_GJgb57ZB4ufxw3aoTSmIz7vk6NYskX7tv1uy_k0D9ShAgRVS2lieCr5ejgTzWAxV3dIOKepiDkcE4qJ-PWvcofra3FwmyihxiDCMaSX2_P2APHQ-QFKBFMyf8fbQJ6BBSXUDgxkOXRf7laSsXx0PxSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZLf7cWcfOTMbA8ZLX0i1b5RhqzhoPnO3WBQH-8K_Q9UunkyJqN1o_q_qlLTEuFyFVUDWtCk3vd_HYXWgaQjMXtEiNppd53VCEjONwC46ZF5o9OQQdGK1HFfVkwWDULHL0qHCpWieaTbEf2kmPu7VfGu5OjpWxixbcyx9sNI6DOTWwF5AX-ZBEXlDSfAa9Kb2BsGoxQKbcGbZFwp8JYdVUG_Rzz-koSOFOADxgV5-smbqRW5LcdvQycA8Kntt7QdLl31HkN_qKQZ_0Dkb52xQiQjtqFJzPGydHtWPCvwp5SzZOetlFdppfyqYwfdH3JTxz9A0N5Y2hj5vpWrE_F_ung.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
نمایی تماشایی از وقوع طوفان در داکوتای جنوبی آمریکا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/akhbarefori/656296" target="_blank">📅 11:30 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656292">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aef77db9be.mp4?token=cCb07-n44sdvi3wvWsqGJ5zyQK1QS-_tnxLLH6-uk3EMwl5YmUEQfRICTlModIo6WKQYesV-kLns9BUT6JdtYVgcyBWSXlX4OgXcC9iChkmlQ77_bxTN67a9Ayx5ADiFZdN1cNfCz8AHqxTohM77W-I5sX_JVwYEzkjfRemfR88nhpKDwswKbTCvvfjI5nULnk9G7IpKvaNM_J3AZfcEJR4HBkWYJFvU0Jt8Qaq-qDAxF8DIxjN33VeaPP9EEtYeFNoKfSGnZYMMP61YjfDIbu-bFugGugL3c1_ai9b50oWf9mPW_JPnxT3rMr0grKkPVlh32JSfrY-a1dyk5_2LZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aef77db9be.mp4?token=cCb07-n44sdvi3wvWsqGJ5zyQK1QS-_tnxLLH6-uk3EMwl5YmUEQfRICTlModIo6WKQYesV-kLns9BUT6JdtYVgcyBWSXlX4OgXcC9iChkmlQ77_bxTN67a9Ayx5ADiFZdN1cNfCz8AHqxTohM77W-I5sX_JVwYEzkjfRemfR88nhpKDwswKbTCvvfjI5nULnk9G7IpKvaNM_J3AZfcEJR4HBkWYJFvU0Jt8Qaq-qDAxF8DIxjN33VeaPP9EEtYeFNoKfSGnZYMMP61YjfDIbu-bFugGugL3c1_ai9b50oWf9mPW_JPnxT3rMr0grKkPVlh32JSfrY-a1dyk5_2LZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
انتقال هندوانه با پهپاد در منطقه کوهستانی چین
🍉
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/akhbarefori/656292" target="_blank">📅 11:16 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656289">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f4873087b.mp4?token=o3RoKjVi4Qs24I6eUKyASNYBTuXVLhbBSCcew9mcnA1bIQYsUTRD1tOtrC4gQ3tCj8OJWHKOTq6CsfmwXyGHXKDFXVECbkT48GRlYzXc5ssdyrZbbvayYpBrAF5IartzGsJuwidHxKor7XAfemr3g-ckkCjVAi0zV-YsyHRq99Mj4XC_hiIYtXhyO8D65I7azpqplbtCgw2oyo4DPSgulA-GY_F1-27-_m2N00vsHkK87J1DmLhShts353GQmhw_D258ozpCQvBNb_6zgbwCmDsOqhHIPN3QSbb0O7BVKgj9wuqqVGU353QI1XNFwzrsKNF9GJZseTwpuDhRjbEHag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f4873087b.mp4?token=o3RoKjVi4Qs24I6eUKyASNYBTuXVLhbBSCcew9mcnA1bIQYsUTRD1tOtrC4gQ3tCj8OJWHKOTq6CsfmwXyGHXKDFXVECbkT48GRlYzXc5ssdyrZbbvayYpBrAF5IartzGsJuwidHxKor7XAfemr3g-ckkCjVAi0zV-YsyHRq99Mj4XC_hiIYtXhyO8D65I7azpqplbtCgw2oyo4DPSgulA-GY_F1-27-_m2N00vsHkK87J1DmLhShts353GQmhw_D258ozpCQvBNb_6zgbwCmDsOqhHIPN3QSbb0O7BVKgj9wuqqVGU353QI1XNFwzrsKNF9GJZseTwpuDhRjbEHag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
واکنش جالب امام خمینی(ره) به تمجید آیت‌الله مشکینی از ایشان
🔹
ما آن قدری که گرفتار به نفس خودمان هستیم کافی است، دیگر مسائلی نفرمایید که انباشته بشود در نفوس ما و ما را به عقب برگرداند. شما دعا کنید که آدم بشویم. دعا کنید به ظواهر اسلام حداقل عمل کنیم.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/akhbarefori/656289" target="_blank">📅 11:04 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656288">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bead13e540.mp4?token=bcAoCnrTzRZiRCs1FbmW2NMW2sHZMkIKM8oypuEMIKdN-fGxVNnB3uRDSyKBipBVN_Oq164-DMcpl_VjazyrekjoV7hmgG3JAbUOVThi88n89OHkK5UvFrfj5rs__R-6ikK-Odt3EN0JW2CEjwdcl9XdYMDtiDzQt2sZO4BPsACEB_GwTDAT1uwkhZaV66t-OmeCTTBdwU0pL2NIVdqoxRIwZ9qajlZ84LJUKXDOCPP5ChrjRYW_xWJcafP8OGlpgnusUPaI23sea4N5jXlqEdxXXmcmwqQvSxr7QUVS9VxkSsvRXH2QXnBwJOSNYPH1_le5f3AH4yM14q72IFS10w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bead13e540.mp4?token=bcAoCnrTzRZiRCs1FbmW2NMW2sHZMkIKM8oypuEMIKdN-fGxVNnB3uRDSyKBipBVN_Oq164-DMcpl_VjazyrekjoV7hmgG3JAbUOVThi88n89OHkK5UvFrfj5rs__R-6ikK-Odt3EN0JW2CEjwdcl9XdYMDtiDzQt2sZO4BPsACEB_GwTDAT1uwkhZaV66t-OmeCTTBdwU0pL2NIVdqoxRIwZ9qajlZ84LJUKXDOCPP5ChrjRYW_xWJcafP8OGlpgnusUPaI23sea4N5jXlqEdxXXmcmwqQvSxr7QUVS9VxkSsvRXH2QXnBwJOSNYPH1_le5f3AH4yM14q72IFS10w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
از این دسر سالم و خوشمزه که ترکیب سیب و شکلاته درست کنین و لذت ببرین
😍
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/akhbarefori/656288" target="_blank">📅 10:56 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656286">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WqIdcdVAQVTr-UaJLAz-3dyMGw-A9d20OgsKDjurVjOKDSoDhs7e2yJZjzMXKsPVM6G954IqWuJTWjtJ6dCGcaCo77LIZRUXVi_lMd_eyCm1Dt6PH_RaqC4m5iEMNm34QAL4hQayXnr0xpbzpmg92JRlVaUICBNFf33hjy0eJQc0KT5Ict5Dtd6E_AElBiD_qNQyhNQvyYca8MO95qbjT_I_H7n0sE3SmJbk3S2zzwShp8NZAB-KhgIQGuATr2UpFXrwIJPwl6SJDZkwu7X9ryonJbMqldu0KR3x9tZ2LB4toxZ2bVVBj7eYJNDcR7zdAqrdkCXkWEYkkDQ6OYZJZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رئیس پلیس راهور تهران بزرگ: تردد اسکوتر‌های ایستاده و نشسته بدون پلاک در خیابان‌ها و معابر به جز بوستان‌ها و مسیر‌های ویژه ممنوع است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/akhbarefori/656286" target="_blank">📅 10:41 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656284">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dea408e562.mp4?token=nfjEIecc10UQaczbIhwzD-miqAGnPPvq7bsju0iIJSKIEyWWYLjEB86fHve-cfvEHEs5yJThR9wsygC-i2kAfSPWgReEl9qLQsBz968kFZKDHLySWAA0j3j-PsRvwINuNfPP7zhQGkxwK13sGl8aP5mGvxcwyln9wa7fm5JDQWriI1NnbUZCcAn0u4cl-vkg8atHWaY5KJUUN6VEp8gKBqvFHioNA2RWj8r82E8_1kui16N8RqF4OPtzz9mfqkwPxRJ-0TzIcTXKJtSGv3HczaOUcApXqlDXMblbwfb_7YyKlC11fk64pEOXYs1nUC-HfsAlAwGMfXj13HKDiaPxuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dea408e562.mp4?token=nfjEIecc10UQaczbIhwzD-miqAGnPPvq7bsju0iIJSKIEyWWYLjEB86fHve-cfvEHEs5yJThR9wsygC-i2kAfSPWgReEl9qLQsBz968kFZKDHLySWAA0j3j-PsRvwINuNfPP7zhQGkxwK13sGl8aP5mGvxcwyln9wa7fm5JDQWriI1NnbUZCcAn0u4cl-vkg8atHWaY5KJUUN6VEp8gKBqvFHioNA2RWj8r82E8_1kui16N8RqF4OPtzz9mfqkwPxRJ-0TzIcTXKJtSGv3HczaOUcApXqlDXMblbwfb_7YyKlC11fk64pEOXYs1nUC-HfsAlAwGMfXj13HKDiaPxuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نمایی از اشترانکوه زیبا و باشکوه
#اخبار_لرستان
در فضای مجازی
👇
@Akhbarlorestan</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/akhbarefori/656284" target="_blank">📅 10:38 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656281">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q4UgZSc45aCGZQyI6nWK6VXtIcGCvsfrv987GqhY-ebU_q4f9LtKtJcipmKzpTlro7ABc3gXIPO5WQE3HgzomXYFUnL3f6lKKOEsdimxVqonUmWmf3wckOnwTKG8AFA8nb36qs9bvGBZnVkLmsUGKeTrUMi-VUqRFGjAiajlaVe7T6G96Cv06GuvYMzWM4ZOvLlVZnNaQ9wIz8xFfVHhLdmudPM8E3yWw-O0QKDo5ZHxT3NfWbpSy6zdS2YhUpvuDtF-X3rDzheal_ILUuCWtsBcmV7noUFHvkXZ--ESf2Sm25ash2TOYo-mCbJGqDKBgRPjAwHXGVeKKuXN_pgQdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5f540d5f5.mp4?token=SFiC1owhvqHhyxOGlt7nhCpz-fUDyCXUtXkqz_rB9CdsWvl2ljjduOlFUjPLYEA-ljH8v5Avnjx6S0Ty8fDlnL8Kzi3hmCbx4NqVhmNBZyjAIm7tgxkdTR7Urfq9UhcIUM2IlLLUmqqo4grlEmSkRt97PUSd4wi0uke4z7_LdNQs1haxZGkV8so8rBRK2V7kuNGFx-F0wLZgpqJoqJp8T3iwdcYXwMAfivrUZvuO-wUZR3SbzPSxTgH5uatEEZw5UYa1EyfrP8BaO_hcZr5LAPuWx273YrwI-DyZHdqjVORenPf17kzWuvkqriB17MmxzDTI8WYUE_-MW-xoj5zvAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5f540d5f5.mp4?token=SFiC1owhvqHhyxOGlt7nhCpz-fUDyCXUtXkqz_rB9CdsWvl2ljjduOlFUjPLYEA-ljH8v5Avnjx6S0Ty8fDlnL8Kzi3hmCbx4NqVhmNBZyjAIm7tgxkdTR7Urfq9UhcIUM2IlLLUmqqo4grlEmSkRt97PUSd4wi0uke4z7_LdNQs1haxZGkV8so8rBRK2V7kuNGFx-F0wLZgpqJoqJp8T3iwdcYXwMAfivrUZvuO-wUZR3SbzPSxTgH5uatEEZw5UYa1EyfrP8BaO_hcZr5LAPuWx273YrwI-DyZHdqjVORenPf17kzWuvkqriB17MmxzDTI8WYUE_-MW-xoj5zvAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جنجال بزرگ پروژه لوکس کوشنر و ایوانکا در سواحل آلبانی
🔹
پروژه تفریحی لوکس با حمایت جرد کوشنر و ایوانکا ترامپ در نزدیکی تالاب حفاظت‌شده نارتا در آلبانی، با موجی از اعتراضات مردمی و فعالان محیط‌زیست روبه‌رو شده است.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/akhbarefori/656281" target="_blank">📅 10:28 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656280">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vlSbN6JuGHq9M9Hwu-GnsBz0R9zcHS4J1kiXBFbTw5_6tauYwK-KorJEMUakDlyabiwxwGEtZ71nKMm6EYojyl1x7BBiW_HrhlJ6racx9oZDcdF4hdA53_k-WGlZRv6qCQF9zO9ZO91tyB9Z-5ld1QgvOdsV-LJ09rJMjdlsvp0a4qUv8OFfkGsOfJqg0TrS-LV_Qxg54ih4zBxvNGbXoqae6LsSTdicyE8l_GLdpjTQBXUD6cxA5UK9VZ080RR0nL9wwQF04Wc3KahB34VHAlAbo4FtkuAeJP46yKIZliBm2xD2X947du-HcRlaxtc_IG0L7GRp8OpWNytx39P3Kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تغییرات عجیب و بزرگ فیفا برای جام جهانی ۲۰۲۶؛ از آرایش جدید بازیکنان تا پرچم‌های غول‌آسا!
‌
آرایش جدید:
🔹
هر ۲۶ بازیکن + داوران هنگام سرود در زمین حاضرند و دو تیم رودررو می‌ایستند (نه پشت هم).
🔹
پرچم‌های غول‌پیکر: قبل از سوت شروع، پرچم‌های بزرگ تمام زمین را می‌پوشانند.
🔹
هدف اینفانتینو: نماد غرور و اتحاد با نگاه روبروی بازیکنان و داوران در مرکز زمین.
#جام_جهانی_۲۰۲۶
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/akhbarefori/656280" target="_blank">📅 10:24 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656279">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b234d7bd0.mp4?token=W5oiMubNxaeq-ggyiMIVGAkAZQmTEKRks57iiGPpic3sp-_AZeM1QKdBNIWhgn13SM95Z90428bjwnI5qouk46GtmA-xKDWgQoWrFNr9l4gLzMmLXRlFk3F-FFBRu5xNvlttsz7n1Kgqvt812F17266NlbMDx_PcLWMCDGFv_X4OCvuaah3pLb8MpG-7ioGDeZ-4ygzXLog80zswDCG8PuWmK5mMxBdJVcxmjVRbggKKsLXif0awPoHl3Np2RPpXGaUqoOlnTbPA2vTvXeNitsvbP0xhmedLIUYfIhfZzhkh1-DJZoP-BViXR5nMvuhI7YEEy6LZo4a2cvwgr8oQYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b234d7bd0.mp4?token=W5oiMubNxaeq-ggyiMIVGAkAZQmTEKRks57iiGPpic3sp-_AZeM1QKdBNIWhgn13SM95Z90428bjwnI5qouk46GtmA-xKDWgQoWrFNr9l4gLzMmLXRlFk3F-FFBRu5xNvlttsz7n1Kgqvt812F17266NlbMDx_PcLWMCDGFv_X4OCvuaah3pLb8MpG-7ioGDeZ-4ygzXLog80zswDCG8PuWmK5mMxBdJVcxmjVRbggKKsLXif0awPoHl3Np2RPpXGaUqoOlnTbPA2vTvXeNitsvbP0xhmedLIUYfIhfZzhkh1-DJZoP-BViXR5nMvuhI7YEEy6LZo4a2cvwgr8oQYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گربه‌ ایرانی، فرش ایرانی و موشک ایرانی
🔹
یه خانم در بحرین این ریلز رو از حمله موشکی چند روز پیش ایران گذاشته، اما بهترین کامنتش این بود: گربه‌ ایرانی، فرش ایرانی و موشک ایرانی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/akhbarefori/656279" target="_blank">📅 10:14 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656277">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/48ff8fa43c.mp4?token=aODbV-E5zZ0-CWTu5KtHVRcHuQLFpiTD87fgMDOwWsnPlwkzs5sVhIcdBrsHM6Xnd7p0zbXZStlts8Fl-fZBb-xPAHacZ-lNr6x32lIdPo0yPrgzvgOcRXRy0jEIsIuxbKLp6s-uO8YbAN4iEyIThDQyH4Ffu3hrSFYt6qDrvimKEpKFNIFTzrQT06pFai05rkKQxA6sdy08pGNvFoL6blrv57zVJp2wqVpB2SKzNKYpo4jkgPyhwWEQzqXwWjA7PpfLxWs2O7Sga1cnoPQVHRLE5WoPO1_BzN-nURzDZFvhTpD_Vl0yPxlUHxILjFKrg-br2kZOGean2oUcasm3kQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/48ff8fa43c.mp4?token=aODbV-E5zZ0-CWTu5KtHVRcHuQLFpiTD87fgMDOwWsnPlwkzs5sVhIcdBrsHM6Xnd7p0zbXZStlts8Fl-fZBb-xPAHacZ-lNr6x32lIdPo0yPrgzvgOcRXRy0jEIsIuxbKLp6s-uO8YbAN4iEyIThDQyH4Ffu3hrSFYt6qDrvimKEpKFNIFTzrQT06pFai05rkKQxA6sdy08pGNvFoL6blrv57zVJp2wqVpB2SKzNKYpo4jkgPyhwWEQzqXwWjA7PpfLxWs2O7Sga1cnoPQVHRLE5WoPO1_BzN-nURzDZFvhTpD_Vl0yPxlUHxILjFKrg-br2kZOGean2oUcasm3kQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پرتاب کفش و زباله روی سر کاپیتان اسرائیل
🔹
تیم فوتبال رژیم صهیونیستی در یک بازی دوستانه مهمان آلبانی بود که تماشاگران این کشور در جریان بازی با پرتاب کفش و زباله روی سر کاپیتان اسرائیل از صهیونیست‌ها پذیرایی کردند.
#ورزشی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/akhbarefori/656277" target="_blank">📅 10:06 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656275">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IHAgzhPneHXl0Kfdfb9a7vtLF9-Slvwg9WH_brIEKG74LjDH07bP4oH-yimCN6qtvSMiZcRj3ULeGUqCGMSFI_CSSIh347FqMFpNW7mEqssGs7jbcZjS7zTxniJDXYAvHNo2CdhmDNimkZ5xQ21ql7H4VQyOWQavW-AYBIdStQj8NbHE93OC922x5geqSv8o8dB4xdg43rCqTRGkDuU9w7JTpbBa25bIdeQ3EJSKZIv7GI4hYxizzUW7b5uv9WTR2WMcdGqaglMw1DqScyCY3rftj7SJ3l0htSrf7ibOUUs5ZamAR268cCCmP49vKoX5GyU7m37__bGHLsdMnAHwfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رئیس‌جمهور چین بعد از ۷ سال به کره‌شمالی می‌رود
‌
دولت کره‌شمالی:
🔹
رئیس‌جمهور چین به دعوت کیم جونگ اون، رهبر این کشور در روزهای ۸ تا ۹ ژوئن (۱۸ و ۱۹ خرداد) به پیونگ یانگ سفر خواهد کرد.
🔹
این سفر در شصت‌وپنجمین سالگرد معاهدۀ همکاری‌های چین و کره‌شمالی انجام خواهد شد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/akhbarefori/656275" target="_blank">📅 09:58 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656274">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">♦️
مرحله یازدهم کالابرگ الکترونیکی از امروز آغاز شد و حساب سرپرستان خانوارهایی که رقم پایانی کد ملی ۰، ۱ و ۲ و همچنین خانوارهای تحت پوشش نهادهای حمایتی و نیروهای مسلح شارژ شده است
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/akhbarefori/656274" target="_blank">📅 09:55 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656273">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/osc9pSHtpj1ifnJHXL7eS-r4zZ2Di9Et8pOaTmZfQs63l6YD9QvdtSZ6u5yaPCRpWUtzCct8wKNXV5lUE5LMcD2QaLHHwipfx-U18Z8u4nN1wnjz02KgMjku416XKR8e0wZjPPaB5hHOafQAXOabsdPe2ckWhYHQd3a6vdJ-nupMStUgYEcP9sVqJiLeAjP4CoMbPVBG_z-ZPVGtOFQbY9uouEjYyKgKRrxZmDVRL-AjT-URUb3Vyc8btI8BV1AisuYr177YdlPXnCheitwILvrV4udNz3q_j6vd8Rg2JuOkdmq1DJDFPUJbro8NvNSJ3n67vWwsGzQpzBanUZA1Iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دماوند با شکوه
🔹
امیرحسین گوهردهی
#اخبار_مازندران
در فضای مجازی
👇
@akhbarmazandaran</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/akhbarefori/656273" target="_blank">📅 09:47 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656271">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NNAYWa40l9nmadme9Zpd2P28-TtEKErGwwSIY4-HgqldI8gLrwRlM9wGytnLMrQqnb3GngM5XVK-FuxpzWedN9hCKap2dAcQqKz1vAvveGd3beZS2WBkt0Qcm6VJiQR3BcMMHxRt7vCINxs2BCB-UFSWq7uGVFuA9nZcklqX4OJy6DM1m_iDtMxv2JzEHQmlfbGJmJEvAdciAQHJJ1uhIjSGM2b31OXLb3LlJj_y0vLSS-dbE6oJtO0hHCYqABlMywXWVWnCtzdrc_95XgcjqwILQhmTG2IqfQeNI7XLHC6my1_mjltpU_Wy57HDBWOptgQpHqYtRQpiMreVCs68vQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای خرید این ویلا و مشاهده قیمت و عکسهای بیشتر به سایت زیر مراجعه کنید
👇🏼
:
https://melksell.ir/
نوشهر
📍
دریابیشه
۶۰۰ متر زمین
۷۰۰ متر بنا
تعداد خواب ۴
استخردار با تاسیسات
شهرک با نگهبانی ۲۴ ساعته
سند تکبرگ و مجوز ساخت
دسترسی عالی تا دریا و جنگل
🔻
برای خرید این ویلا و مشاهده قیمت و عکسهای بیشتر به سایت زیر مراجعه کنید
👇🏼
:
https://melksell.ir/</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/akhbarefori/656271" target="_blank">📅 09:42 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656269">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tFTq9tWHnV7hEgfU5fgc_zD_gG8KqtDjclGfKvEV7dSSfeUFicniKjEXzu7VEzvD9gpNxUblmMeXY8kNPNZBx4EpKEew9gIsrsGlfavRnAtIWh8eM4PqKp145SCbePqGueLY_w-gUYUexA4URtlpJ-JATGsi-5J4jTdBr0VSq5O0l74wF8AmCZokkj3kL6ZvXV2BFzd55xzQgCKDUxxbkLjhrG0x6OY7jfCyDgF8UyZErVs_pZiTGguQU_gaufdED-44T3PdRsxdNMW1pQ9dYJFSMnb7ixP4dq0pd7qCNjcIRx6QjVtNavzmlatcGRwPuBYOgeUSdgpTyikKFDbIog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
عکس تیمی جالب نروژی ها قبل از سفر به آمریکا به سبک وایکینگ‌ها
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/akhbarefori/656269" target="_blank">📅 09:34 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656268">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jpMDlj-Bvr39MQkbpr0ReD-Sw7stbbJm87T_WQeFgpuNQQ3_ejP2jwdyuI5Vk0uu9ziOQ6_u64Z-yaIJIq0F_AMahOvYJbhtNaC_jgBIsLfMF_2XNHOWieIWxxjCiV30Mv72Qu8BSaxcDAlEwa-WW8Te6TQGjJuwVxo_zwRUq0gtfnRQdEceQzrsewis_pSGPfzbpnWlJDq8bTNtfyIV-ZzvyG0_TOZdKXTg1e585Ge6rQw1F-UHBfwBwIVn2u7RQHZdGKtJwsUtgojWELY64PWbyBMBTU4dA01GKBO3ezzzZjXuLkwDfXzY1-joPIIEX0W8jAI5ibJP5fBKBSt53w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
واکنش بقائی به ناکامی آلمان در عضویت در شورای امنیت
‌
سخنگوی وزارت امور خارجه:
🔹
ناکامی آلمان در کسب کرسی غیردائم شورای امنیت سازمان ملل برای اولین بار پس از دهه‌ها، نشانه اعتراض جامعه جهانی به رویکرد ریاکارانه و غیرمسئولانه این کشور در قبال نسل‌کشی فلسطینیان و تجاوز نظامی رژیم صهیونیستی به ایران است. وی افزود: آلمان سلاح به رژیم صهیونیستی می‌فروشد، نسل‌کشی را توجیه می‌کند و تجاوز به ایران را «کار کثیفی که اسرائیل برای همه ما انجام می‌دهد» توصیف کرد.
🔹
بقائی همچنین به سکوت آلمان در قبال کشتار ۱۷۰ دانش‌آموز در شهر میناب توسط موشک‌های آمریکایی اشاره کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/akhbarefori/656268" target="_blank">📅 09:32 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656266">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/95f26bbeb2.mp4?token=M5kBo6WJxADVUiUta3hWexVWLuAME5tAZgVsfYSmevBo0Tx6qBst0zkKHkiOqhHTkWJPtThzh1PI3aP51qYTj-omCiIDtzM022shNfs0p3EP3qKhRf46oHpbX7zISXaZEQBZ1nl0LHf7UQzahCeMmKAi1v5iYXMokKVi8pmX0mkUnYjM6rnORpD1LiJtwyd3kfab25VjAekC-w9dgFAS6e7axPo-mMEQt3RU46Z2xbMBp7S5X-m-EVA4bvB-0cLmIawCweIxTOEnLHVHRenJKVLqmXHFtuRUnGc3q8svuuN0yIYDdLgvmMARUmSd65mnVE6Vak3Y3jVDE0d_cgBM6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/95f26bbeb2.mp4?token=M5kBo6WJxADVUiUta3hWexVWLuAME5tAZgVsfYSmevBo0Tx6qBst0zkKHkiOqhHTkWJPtThzh1PI3aP51qYTj-omCiIDtzM022shNfs0p3EP3qKhRf46oHpbX7zISXaZEQBZ1nl0LHf7UQzahCeMmKAi1v5iYXMokKVi8pmX0mkUnYjM6rnORpD1LiJtwyd3kfab25VjAekC-w9dgFAS6e7axPo-mMEQt3RU46Z2xbMBp7S5X-m-EVA4bvB-0cLmIawCweIxTOEnLHVHRenJKVLqmXHFtuRUnGc3q8svuuN0yIYDdLgvmMARUmSd65mnVE6Vak3Y3jVDE0d_cgBM6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بزرگترین نقشه سه بُعدی تهیه شده از جهان هستی، شامل بیش از ۴۷ میلیون کهکشانِ کامل
🔹
هر نقطه نورانی در تصویر یک کهکشان است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/656266" target="_blank">📅 09:10 · 15 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
