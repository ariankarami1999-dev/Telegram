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
<img src="https://cdn4.telesco.pe/file/EC21f-Q8JPnZIjq0ZRmTEIgkCCxPVZVI0BHmadmf0LxUKKbEhWe_bxK6dr1-vLdtZrOtEyZvXi2baUu934g6VAR-4p1UQ0ylVcx2QxxX2U7YvuyGDfHGYpb8HZpwogNqsWUf_sjDQsAAdsuO_fr5Uxny_lWLCKSctVNr0vMvcJy4VmZzrOYZWtaravpPz9mCs3Jcy3C0fhUnlRg-8VRKqDgtFdOaqRrXGCGzZ9Kq3jORbrhI1UFg43Z3ktdVPOXNyiVwXtNizvrfj5vAdS97TgX-w0vDbsroQ7pQ8NaZhhp2gvlbnocoAQupX39KZKsbu-xnwam6BC7_qJk5BAKL7Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.88M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/farsnews.agencyتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-14 10:14:23</div>
<hr>

<div class="tg-post" id="msg-466565">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Se4kgt1LsCENGKEQ5MXZHUfxSSlABuyLIfnef1Tl4xS4eew-a2Z6eg3YzVu83aRoLe-XmVDpVdH4LJQb52B7AeRUe2MZJ1ZLHMlBv6hU-GOmcxbOlG3vUiEa0t4RYGdVXOAUNmQAsafA__Eldj9kJVe-4sa8RoLLVvY3Buf7HIg4MsJ8K5yOTwuRYwTs-ImSGgbF_HQTtDp9wkyNZKZvWhJbIE0fKNJ6eAaXHL64lIZOF98qM2Oj-mjSqsr7MlZKYCmE3KJKVxMsDvByQzqXBn9cfKVWHY-iQb45-BHTIq19Ft3HlE037JFe5_3Gfg002nHA8McXQ_NHAuc29r9Egw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حاضران در رژۀ منسوب به منافقین در کرج به دادگاه رفتند
🔹
در پنجاه‌وششمین جلسۀ دادگاه رسیدگی به اتهامات ۱۰۴ نفر از اعضا و سرکردگان منافقین برخی از افرادی که در نمایش دورغین منافقین در کرج حضور داشتند، برای طرح شکایت از این گروهک در دادگاه حاضر شدند.
🔸
ماجرای این نمایش به شهریورماه امسال برمی‌گردد؛ زمانی‌که انتشار تصاویری از یک رژۀ موتوری و خودرویی در کرج خبرساز شد و ۱۵ نفر در ارتباط با این پرونده بازداشت شدند.
🔹
این افراد گفته بودند برای تهیۀ فیلم جشن تولد و در ازای دریافت دستمزد در این برنامه شرکت کرده و از ارتباط سفارش‌دهنده با منافقین اطلاعی نداشته‌اند.
🔹
همچنین اعلام شده بود که فیلم اصلی پس از ضبط، با ادیت و الحاق تصاویر و پرچم‌های مرتبط با منافقین تغییر کرده و نسخه‌ای متفاوت از مراسم منتشر شده؛ موضوعی که اکنون در جریان رسیدگی به پروندۀ منافقین در دادگاه قرار گرفته.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 1.03K · <a href="https://t.me/farsna/466565" target="_blank">📅 10:11 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466564">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f416b2a7bc.mp4?token=ZsIhMqkk-D69g6Lakx5mdl-4X0p5ujwSLsoWy7Sow21X6bZ5ttoDgmuwAjKREX0ziJeBnNBLlAZQ6vIifnBUXeT-DiWizVCHxqorVh32V7kXTkfK7hthNRnEoCxjvZXhkzlf1F_ZxSN4--5jpa4jktLvwPwBoy_cfy7WDxd6duXtDFHSng75hl5RP57SFX8suCnvhji5Esp493Zc7Yg3qFpsgqGd8C6nwDZ5Pe-mf5rz_SAGEDhpYy0MpxB1GSJjcDUIV1jx5TvGaWgCy3J79X1u7mjBILW7yrpBkieFeJ4Tt4AlagQ1WxXu1AKpy7J3tcHZD7iQ6mqYfZ7_oVeTLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f416b2a7bc.mp4?token=ZsIhMqkk-D69g6Lakx5mdl-4X0p5ujwSLsoWy7Sow21X6bZ5ttoDgmuwAjKREX0ziJeBnNBLlAZQ6vIifnBUXeT-DiWizVCHxqorVh32V7kXTkfK7hthNRnEoCxjvZXhkzlf1F_ZxSN4--5jpa4jktLvwPwBoy_cfy7WDxd6duXtDFHSng75hl5RP57SFX8suCnvhji5Esp493Zc7Yg3qFpsgqGd8C6nwDZ5Pe-mf5rz_SAGEDhpYy0MpxB1GSJjcDUIV1jx5TvGaWgCy3J79X1u7mjBILW7yrpBkieFeJ4Tt4AlagQ1WxXu1AKpy7J3tcHZD7iQ6mqYfZ7_oVeTLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آتش‌سوزی در تأسیسات آرامکو در جده در پی حملۀ نیروهای مسلح یمن
@Farsna</div>
<div class="tg-footer">👁️ 1.44K · <a href="https://t.me/farsna/466564" target="_blank">📅 10:07 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466563">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">‌ سرلشکر حاتمی: صنعت دفاعی کشور به معنای واقعی کلمه حامی و پشتیبان عرصۀ نبرد است
🔹
فرمانده‌کل ارتش در دیدار با وزیر پیشنهادی دفاع: در جریان جنگ تحمیلی ۱۲ روزه و جنگ رمضان باوجود تلاش دشمنان برای متوقف ساختن زنجیرۀ تولید تجهیزات و تسلیحات نظامی، مدیران و کارکنان…</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/farsna/466563" target="_blank">📅 10:03 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466562">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">فرمانده‌کل ارتش: مهندس مهرداد اخلاقی چهره‌ای شناخته‌شده، مجاهد، مجرب و انقلابی در عرصۀ صنعت دفاعی است
🔹
سرلشکر حاتمی در دیدار با وزیر پیشنهادی دفاع: ارتش جمهوری اسلامی ایران، تلاش دارد هرچه بیشتر از ظرفیت‌های بالنده، پویا و مستعد صنعت دفاعی کشور برای قدرت‌افزایی…</div>
<div class="tg-footer">👁️ 2.4K · <a href="https://t.me/farsna/466562" target="_blank">📅 09:59 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466561">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/INnsItJsCPDcBt5qB26wsHuwd0bBdSrjzdMhHbUDHydNqgIdgjNaC950Z03WxQ_tDOCR-TyjFqDvsH1kx-F4CS7E3A49ZSwbiEsyvry87ICMTinkPDbta0cLjuu-Wy4fs05ZDEwgDakWKMnhqsgZ2o4t4T4Yry7d39lsF9bp7C720S6mWcpGSKPPuvzdj3sSueYYO3gISUjeSXitYppwCnfI1qCjeqVp5L12-Fv7HiV3NfaUsyIohZiOgdJjaBgU3txcgUi1ZuA06a7PA6lfOBVFieLzMFcVb0rhQ4o5kT49wySZJiFUZtTOrvxnyO_-DCfstNDLrEJ9aKtx8gXMIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نامۀ معرفی وزیر پیشنهادی دفاع اعلام وصول شد
🔹
نیکزاد: مجلس شورای اسلامی، نامۀ رئیس‌جمهور به رئیس‌مجلس برای معرفی مهرداد اخلاقی به‌سِمت وزیر پیشنهادی دفاع و پشتیبانی نیروهای مسلح را اعلام وصول کرد.
🔹
در نامۀ پزشکیان به قالیباف آمده: در اجرای اصل ۱۳۳ قانون اساسی…</div>
<div class="tg-footer">👁️ 2.47K · <a href="https://t.me/farsna/466561" target="_blank">📅 09:58 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466560">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rzfu-DI56v43dvfQ-NOcWYHxLZ2COD0HUvAZBbI5NLd2dgQDXMrnhcJPXz70FdNlrf-k68UJKR0vEL8g06SFNipDEcTZMIFWw_tz3Mk2u1GWiG9XreG4gDPiZpxHAZwFfEDktODPhB6G4iJgQKcgbYdKGVk7oAoUWcJ3x2cyeLuDH3Q6eFCOu5qXOz9jLpIURh5a2ek5yvsgrL-8M1v4Ae0h8Laf8f18P6TTLWljeBLZzJejJohZu6auQCiFdoKbzDBqozCNcz-b8JrOEbzoYds3UbwUrWy62tW9m6S3DkgoTOdp9iRDt_ecRRrrULjcqXhclsqRg54YwIQSaxBJUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌
🔴
یک منبع در مجلس: مهرداد اخلاقی برای تصدی وزارت دفاع به مجلس معرفی شد. @Farsna - Link</div>
<div class="tg-footer">👁️ 4.36K · <a href="https://t.me/farsna/466560" target="_blank">📅 09:32 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466559">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B97DqTYHpEqxEyQWs4zd0lZWLeC89JEIa4pwWGY179V8Pyhb32sSuhGso3selIWUXaPNJNBQALqYcrrIFIStQptg4Aag4I4rGYTGLBSPeSK0Ti9a42NN9q0JwtLBSjGoVhTignwXX7S0zOZowJtEcgYjFRKl5jjTXgfsbwVMdZh41yuHSAekApDFiUR6l3HC6x62_Yp9rUFFe87459WE-Up_DkWBrQDlmjk9I3wtZVJIbjHpFS1Uy6qOIr-RrIvwqWxHIBSyBkMo1mTzPHMpEk0INUPX5L0IJUMvAALKsjdPcbuO_5L32i-pTA_gxWh08s8KALrQWO7Ucpc0afuAzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تجارت مافیای لاغری باچربی شکم ایرانی‌ها
🔹
تب آمپول‌های لاغری، بازار بزرگی برای کاهش وزن ساخته است؛ بازاری که منتقدان از شکل‌گیری منافع تجاری و مافیای لاغری در سایه تبلیغات گسترده و سکوت درباره عوارض آن سخن می‌گویند.
🔹
چاقی فقط به اضافه‌وزن و تغییر ظاهر محدود نمی‌شود؛ می‌تواند خواب، فعالیت اجتماعی، باروری و حتی سلامت قلب و متابولیسم را تحت تأثیر قرار دهد.
🔹
به‌همین دلیل، درمان آن هم صرفاً به رژیم و ورزش محدود نیست و روش‌هایی مثل داروها و آمپول‌های لاغری و جراحی چاقی مورد توجه قرار گرفته‌اند.
🔹
حامد قلی‌زاده، متخصص جراحی چاقی و بیماری‌های متابولیک، معتقد است انتخاب روش درمان باید متناسب با شرایط هر فرد و بر اساس نظر پزشک انجام شود.
🔹
به گفتهٔ او، مصرف خودسرانهٔ داروهای لاغری می‌تواند خطرناک باشد و این داروها نیز مانند جراحی، بدون عارضه نیستند.
🔹
از سوی دیگر، جراحی چاقی هم تضمین نمی‌کند که وزن فرد هیچ‌گاه بازنگردد و موفقیت درمان به انتخاب درست بیمار و رعایت اصول پس از درمان وابسته است.
🖼
اما کدام روش برای کاهش وزن مؤثرتر و ایمن‌تر است؟
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 6.85K · <a href="https://t.me/farsna/466559" target="_blank">📅 08:30 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466558">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc1315d689.mp4?token=rTNQrwACmB43vpx35fF0bdsxgg9ekIvzl98nfv9ZRw7Ete9aYfSLkSSNB5GJ3_WsPzukAEBPt5pvMrZdk5p6rSx0oYqltQO6kJP_S9tXSAUrZY-UDe_mhzkgFJ6-04TP5DacVUpPg8J_kjV7DduRuvuE872O9HnCqLs3GAYFZe_Wln-2Ztf0CiQp3ifNyYk9MVFTe5l5DxqfdHhXzlNL9AwF7WIViH4ZXKS-v6rzYJ42xLebuFydSmtzQVpbbJ-kzS0k4kZEHXqtVmoVJ_814VEmpw3Z_UUOOHHzV2AM2JLv0zL6995uA0rimy-5ZJ5QYm2EUT0jEyZ9S8ueQubdhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc1315d689.mp4?token=rTNQrwACmB43vpx35fF0bdsxgg9ekIvzl98nfv9ZRw7Ete9aYfSLkSSNB5GJ3_WsPzukAEBPt5pvMrZdk5p6rSx0oYqltQO6kJP_S9tXSAUrZY-UDe_mhzkgFJ6-04TP5DacVUpPg8J_kjV7DduRuvuE872O9HnCqLs3GAYFZe_Wln-2Ztf0CiQp3ifNyYk9MVFTe5l5DxqfdHhXzlNL9AwF7WIViH4ZXKS-v6rzYJ42xLebuFydSmtzQVpbbJ-kzS0k4kZEHXqtVmoVJ_814VEmpw3Z_UUOOHHzV2AM2JLv0zL6995uA0rimy-5ZJ5QYm2EUT0jEyZ9S8ueQubdhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هواشناسی: سامانۀ بارش‌زایی صبح امروز از غرب وارد کشور شد
.
@Farsna</div>
<div class="tg-footer">👁️ 5.77K · <a href="https://t.me/farsna/466558" target="_blank">📅 08:28 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466557">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاخبار لرستان</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/253b2d9da1.mp4?token=LN8vsiWGqyhwkl9S-hIhxa9g2mlsyMHoiZ9JX-QkiELr3l_aNBfTSgd4wFxytYl9tra1OlsLutjWlUUVyLSaXbx1oBx979Sz6YvlsIyZhtpLddtSFBE9RLQ0c9uBHqlBf8SIy5u0A4WgSsESxL3bj7nbs6jKamENyjERH4FBeD13vxTZ7nH23rPejLnMDgwO0j9G8ZjeS3A5fbW6J8rhoHu0zvkf7XaozhjXFyZW_KRteLy1WImrEvE7tGbTBr_2kug1aFqQhROsXZgBQAlFq8efdJ52rgIIm1ZN_H3cRik35_e4pkq2gjv7LXHoBIRoGEzobF5QkVVyYUiMcmXAkFPsPS7aiWCnvpCkQhOA1KIRAX9dyVP800PnhxdTBf73grbM6mFlx0K6fEEgEF1riHGkqcwhbMeFOI8g6KIVvxbVnHzshXW6btIhFxu4GRnIYHw9t953D5vwTWhKniwi33RdonRQybFAN3-o-3GunvobzDo80YJ9KonqXP2Pp8dzHGCbKtHj9LyGX-zsUDEVOyCf15ZVzn461iQW3wKnzhxpYKei_yhcA4U0rIkuPHTxU8L41B3EdwVXT6QQF73MfvddOyHqzPQ3Y5kdeG8Oe16XsQxuzrSMl6DCXQUohvDv-oBm4D0k16okcSyBnWnU9NE4WFQFQJkQ0ZJOpq67SE0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/253b2d9da1.mp4?token=LN8vsiWGqyhwkl9S-hIhxa9g2mlsyMHoiZ9JX-QkiELr3l_aNBfTSgd4wFxytYl9tra1OlsLutjWlUUVyLSaXbx1oBx979Sz6YvlsIyZhtpLddtSFBE9RLQ0c9uBHqlBf8SIy5u0A4WgSsESxL3bj7nbs6jKamENyjERH4FBeD13vxTZ7nH23rPejLnMDgwO0j9G8ZjeS3A5fbW6J8rhoHu0zvkf7XaozhjXFyZW_KRteLy1WImrEvE7tGbTBr_2kug1aFqQhROsXZgBQAlFq8efdJ52rgIIm1ZN_H3cRik35_e4pkq2gjv7LXHoBIRoGEzobF5QkVVyYUiMcmXAkFPsPS7aiWCnvpCkQhOA1KIRAX9dyVP800PnhxdTBf73grbM6mFlx0K6fEEgEF1riHGkqcwhbMeFOI8g6KIVvxbVnHzshXW6btIhFxu4GRnIYHw9t953D5vwTWhKniwi33RdonRQybFAN3-o-3GunvobzDo80YJ9KonqXP2Pp8dzHGCbKtHj9LyGX-zsUDEVOyCf15ZVzn461iQW3wKnzhxpYKei_yhcA4U0rIkuPHTxU8L41B3EdwVXT6QQF73MfvddOyHqzPQ3Y5kdeG8Oe16XsQxuzrSMl6DCXQUohvDv-oBm4D0k16okcSyBnWnU9NE4WFQFQJkQ0ZJOpq67SE0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قابی از پاییز طلایی دریاچه جهانی «گهر»
@LorestanFars
-
Link</div>
<div class="tg-footer">👁️ 5.67K · <a href="https://t.me/farsna/466557" target="_blank">📅 08:26 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466556">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iLtCcAPh9z0TR1p8auHcQildd5IfhN9j8GgiM1p2a7ikdTBGjseCJ6fzicNhnIsHXb9c8CHDkp_mdvjkt-R-03HBoTjLBjLQ3mf6B-Hcs-jW8SLFPFaWmVEu-c9gerRlJh4gaYGC45yer0LNyG0lonBsrZUGsVHz6ydvnzCt2F9QlyzTbGl5-g8gJ23QbjZFHzeGtlFpsDVYW-SnWSsKX-NXYtk2MnplmPjSVR090nxtxcgnIYojQI7LBEpjspZ4AatWCAWYjZbQw0sSQmJmvMv_dW4HnHf15gIr8HeSWz0tllCHTco3bWUx0aVYm1T15umYVOeNP6ylj6iwH1rUGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی ارتش: ذخیرهٔ بزرگی از تجهیزات جدید در اختیار ارتش است
🔹
امیر سرتیپ اکرمی‌نیا: تجهیزات جدید پدافندی و آفندی از جمله موشک و پهپاد، در طول جنگ تحمیلی رمضان به‌صورت روزانه تولید می‌شد و امروز نیز تولید آن‌ها ادامه دارد.
🔹
اکنون ذخیرهٔ بزرگی از این تجهیزات…</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/farsna/466556" target="_blank">📅 08:23 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466555">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4783e8a603.mp4?token=myiGDiuL3J56ZIKoCuUg3PqLHxL3_mlOZsjIqX0BJJZXOJ_S0eyX_jmosBzmhAETIr2ROFJblDrvweO1EDvGqIyHSw6E2sW66Up3TX7dV25aOZZAaKP0jyMMXTmEuh2CRk8s_QnFsSuq_f-C96OGP5dKS5cis1tpJorD3yy4tjqhQ3IKzbBJs9wdMCXDermpJUDOqbKqcfXF628Fbmnaphc6LObF3RBBZ4lTt-ydWZG1PReVSx0jWgsKKevYJyvqncIEXt6rwfNHVQVggAafMXDU7gx6fMzSYbWHPNKV9ub4nISDvJtM-FOCOJ7y3yPMEjCCJ6ai-SHwFnb7i_R6Tw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4783e8a603.mp4?token=myiGDiuL3J56ZIKoCuUg3PqLHxL3_mlOZsjIqX0BJJZXOJ_S0eyX_jmosBzmhAETIr2ROFJblDrvweO1EDvGqIyHSw6E2sW66Up3TX7dV25aOZZAaKP0jyMMXTmEuh2CRk8s_QnFsSuq_f-C96OGP5dKS5cis1tpJorD3yy4tjqhQ3IKzbBJs9wdMCXDermpJUDOqbKqcfXF628Fbmnaphc6LObF3RBBZ4lTt-ydWZG1PReVSx0jWgsKKevYJyvqncIEXt6rwfNHVQVggAafMXDU7gx6fMzSYbWHPNKV9ub4nISDvJtM-FOCOJ7y3yPMEjCCJ6ai-SHwFnb7i_R6Tw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سخنگوی ارتش: ذخیرهٔ بزرگی از تجهیزات جدید در اختیار ارتش است
🔹
امیر سرتیپ اکرمی‌نیا: تجهیزات جدید پدافندی و آفندی از جمله موشک و پهپاد، در طول جنگ تحمیلی رمضان به‌صورت روزانه تولید می‌شد و امروز نیز تولید آن‌ها ادامه دارد.
🔹
اکنون ذخیرهٔ بزرگی از این تجهیزات در اختیار نیروهای ارتش جمهوری اسلامی ایران قرار دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.36K · <a href="https://t.me/farsna/466555" target="_blank">📅 08:01 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466554">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">هوای «قابل‌قبول» تهران
🔹
شاخص امروز کیفیت هوای پایتخت روی عدد ۷۶، و در وضعیت قابل‌قبول قرار دارد.
@Farsna</div>
<div class="tg-footer">👁️ 6.6K · <a href="https://t.me/farsna/466554" target="_blank">📅 07:46 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466553">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffb98f0b2d.mp4?token=rO3LT9zjblnZgfJ3Kp6Jdu3iHcvjxfUpl0NyIR3HQHCN604t23N1uxOC3h64i7iJTw2l3BDSuO-iho3_70AMajCNq7IVqSdfWpTHS9mZwmVa2XZTc2sd7zTGjAqgZnYHQn_QLDqX5hSCIobBceUiiyreQaZrHdNpqe6izCiCBtvgTWrV1u7Z9KUh-gpJKEFtQggNcYQ6ecwtnBhr8tKI8N65DN0EmgXsv31JBD5zXXS1psIh40lhugvvi3tkTUWcHnVvPX9cl47XwMjAO4d17yKeh3hi5qGZ0KBmd-PcsYwsiHDKt4Q2J4sf54L03UphfxUJwadK15HOMlsy-fRoZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffb98f0b2d.mp4?token=rO3LT9zjblnZgfJ3Kp6Jdu3iHcvjxfUpl0NyIR3HQHCN604t23N1uxOC3h64i7iJTw2l3BDSuO-iho3_70AMajCNq7IVqSdfWpTHS9mZwmVa2XZTc2sd7zTGjAqgZnYHQn_QLDqX5hSCIobBceUiiyreQaZrHdNpqe6izCiCBtvgTWrV1u7Z9KUh-gpJKEFtQggNcYQ6ecwtnBhr8tKI8N65DN0EmgXsv31JBD5zXXS1psIh40lhugvvi3tkTUWcHnVvPX9cl47XwMjAO4d17yKeh3hi5qGZ0KBmd-PcsYwsiHDKt4Q2J4sf54L03UphfxUJwadK15HOMlsy-fRoZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حملهٔ پهپادی اوکراین به قلب تأمین سوخت مسکو
🔹
پهپادهای تهاجمی اوکراین مرکز بزرگ ذخیره‌سازی و توزیع سوخت جت، دیزل و بنزین که پایتخت روسیه را تغذیه می‌کند هدف قرار دادند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.47K · <a href="https://t.me/farsna/466553" target="_blank">📅 07:31 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466544">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZSK3KzezsFXtu7Aon6ii3GpulAU82dL3Nab0uJbT5GKEvo_2WtN770xJDG4k1PqC4uLyPyjz6Dv0r3B9QW9b9ncUUbOOfq6lLBMjig5ex7SctKbZsb645r2nOPZv2w7rh1A_qwxqCUamULLTd8doWWQstW1gWIdmg2H0W8kivia7LjIes2u_OnZt7QXF2f-L9pQWGO1JWyigeIkplquSRv5A1JwU5GtvVGWnJqfuN3AXdHz7rMYHY4jF-T_WvCkC7lMFKuK5q4gfcpOKTTUh0jNlyqSCMIzWkOEOQq74MLXcqk3bYVQiWmFHIOFpucS9F-4xiI-_tsR7R8J92PdzYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SUd9FHLqkKrP9A270fyhW9TmKV55zRl0eR3N4uwRXYRkEHXgXHRkTLJovxIENsBUBsaixBfwLL9-qEAmCu9cepm_MGHy8OBQqndTdUkqHCgXaZAuovOFdUD3dxaxoiWZGj7fLknGDbkORrdiKkcu2iItKH9w9ESLPgyJnZs8O_pT7o7qgwtj1VxjXlQLPQopcc1L2663LE4rTlQiM7tU2UnIM8K7pexLzlYnDM-6YNbxaw7JEF1lL0zXhc7Wra5GNULlQOq0c6hvnrkxRFfG8raSOG4zDOjsko8XnDivtj30qMI30oMDCWIGGSXKUm0_vkItYdw0syd6Tg7RNV2mvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BFacnF5OELGy31W1YXp1RuTwgkzvUEHBZAZ01jvg6bxWWpCLPs_2YK_eob_flJb4UM0T1Q0aQpZpcNHTO7fcQJ4zuq_DSWSc1t_2Jeoq-P7jY4GUF0Vn0awNR15R7H0RtepgD7syjaMWVwe-dXthJEhWTb8VvTNzdqMJZvJi28BAlWmo1iRBeIg1Jx6dDlHUWM--8xEJXp4vGgDHrBNPDcppXTxtszGJxWDfoHf4FztQ3KZoLbU6TyzNLAVC7vb-T0bycMrT5WHMZ2_0S-Ac9rUhFv4av-Y-TiehFhuzLm63noHHTRKawiAF-oN8YlUqWCCQPCzbHRL-GtASYW28qA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QR7glJJfK-BIAWH9LURlkAeYQriTbblNIXZLxiJZSSkj9s2VzD1nGJ2vzchnyNSF72AjwTuEpQHFoHV8gTkz-cqRnUUiLVEnFqNDOlVt833WPzGzIv1A2dZWJsilafCBFG0HuN7rUu2ruIaJ4-7T21s6_LmH-nzuCp2dbVFFNzOUTuYwRSZEk9XOrUO9Es28Hcx2HTSw-vSb3fAGPFXXnwqRUBv7lxBnm8c8BYn_fzXy3FWL5sprSa1Crcp7fqhfrm-7iwhy7N_V3KkLA3ebmNQWCz-mr-aZM9G6cefd8DnDZIp2ciVw9UCYuLVPErh_AWGxuPXN6cQ0S1UHYSwEUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FatiwzdaM2xybPq8je5RdqV-k9zrmFIYOaF8Le_FtxUfHkgo3qR_yXKisGl-JEd3AZlTHAHufDNwI0Lv84YF6QM8ptpURMCoqPSBQDJ8el-y60l2iuKKnAbV5hT9zmO-tL8bfCZLrRMKJxg8BnrnnM6wgRdN09Kz0VZjAM2jTKXrbsZjZMHtGMUhwMJ_eaMH8p1Xc-P-FKaVKcKuWbrgxw9AfeMUrFfb5txjoCpBFnGBeV6m5SzdOyszhKdb4lI69AlK-ffxhHm6ly4F7JnVEWXiJnosLE0ADP39aLEcJfFmeVIuoJyrxy8XQAIx6TW0spUaE0Oz7DOJ8MmIQzkg2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JplfalJ0m6bGxhOGvgkvce1pwCpEs16OeUmjhv8gVhjsBSm9qWkaPhLpaRqKxBhu8qXxOR3200ZB9RMRrDWhF1bTGQfUqyIS1jRr158nUfPpxg5W7bodnA_FsQuSgFhDaf0weL4CI9WOtqvC69dVsuLW7AtWmgHpvAO3zD9AL3YrfNVX8hh8-9D-VGhDsW8StjQxf6El0LfSoBk6Ea4jx2SQrM4by5xgIO7kiX0C53zuCmA0wrgESWq94pNOo8EtpcRNGRbP6f_MCkhEpehTVLnP39B1gKjk6MJtu-N6mxeIaS8YICMMxMxnlPsnFTiMSmXMjVheoHCRA-5uEnDEQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BqGnxVje8BKrRbNo9k2Uz_54IFDe7MkH1jjGYBpgjLWPUQMBsNHGppNBfpSbep-EsWIbRzMUPQ0qTFBpYIBa3kqp35wFvZmjSaVCLrKKgmiXKE1A_CuvDRBxVBVGxxxg5zKiF5wVVrUAni7yqvohEzlT9dO3L4KH8UTbARYsiw-kgaimSIQ2q0c_91iL93cC-WtXZKBW97yTmMt0L8I6wZlE7up6vqYa9duDl_Z6KM9Zs8FDSl85Xi0Hvg3zFeX2iiLjkekZ3myQlOo7pOimZlIHclUF4mhLBq7r190XeQ7ssNxx-YZaVkQq249yZiRmWdZ2ZpTGGtxf0w1uQsaJ0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QdHd2kFPIr0u8G8yz4xp2gpvYocTqmLxjTd2YhCqzXybRmMmxaiQdXgdeoRoN-FGLM4fNaRiYBwyzGXzSvUeUMImiBPBDRck-NdCqoPPwkeBVVz7Df-z6OKpwoYGIksOYXTM_FiCeipajpZWRpp1VJKWUcPPkykgyiORMwsa2ybGonvhGf0aLBt3rnTw057pC6V4g2txqAHPRMIOa9nTTNs0x80DYM8U3ODQNTshBxxUDBK5cZ5XtVmttrcd05xm4xxcKp6TnqDL0L67LeUSE9hcEZBmhAqXivhaRYxrmes8he1HYfTuJjhDHx466_drEEROKDHU4yXbL8TZJXzrlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ou3x_GrUkSs0vpLzrUgOEFFecgQq8Yld7Ne85nl4V0XBrcgMuqUXL1quDkFnNFFOUl3R89_tLifEc0apHO2f3fOv5VF-wL2MS7MoqfSC6HlWVin_vgmqRmbpzH3IAavKwT96ysmAaO9PffVnJLsfloFrQNxM3f-Sv5UAC90rKrifOl4YxEhcFxOvvZN-tW4SjYtziMynGAleA1wgzm1Ziy-MT4swHZfldrYAtPbdDUhJwDghbfe0ZTJkz1jVRdaArXec7dNlEI7q9fZpmFN3smtdfYD0yanB8aDheQL73g_iVyv2C4YUC0LDVzNPOuCbEP0NX8ouUxEbxzPy1DMmeQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
باغ‌های خراسا‌ن‌شمالی پُر از بوی سیب شد
عکس:
رضا خبازان
@Farsna</div>
<div class="tg-footer">👁️ 7.39K · <a href="https://t.me/farsna/466544" target="_blank">📅 07:22 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466543">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">حملات هوایی عربستان سعودی به شمال یمن
🔹
منابع خبری گزارش دادند که شمال شهر «صعده» چند مرتبه هدف حملات هوایی تجاوزکارانهٔ سعودی‌ها قرار گرفته است.
🔹
همچنین توپخانهٔ رژیم سعودی روستای أم الضهی در شهرستان حرض را نیز گلوله‌باران کرده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.3K · <a href="https://t.me/farsna/466543" target="_blank">📅 07:10 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466542">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">‌چرا چک تضمین‌شده جایگزین چک رمزدار می‌شود؟
🔸
قابلیت استعلام، قبل از دریافت چک
🔹
اتصال بۀ سامانۀ صیاد و امنیت بالاتر دربرابر سواستفاده‌های مجرمانه
🔸
امکان نقدشوندگی در سراسر کشور، و بدون نیاز به مراجعه به شعبۀ همان استان
⚠️
از امروز صدور چک رمزدار ممنوع است،…</div>
<div class="tg-footer">👁️ 7.63K · <a href="https://t.me/farsna/466542" target="_blank">📅 07:00 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466541">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🔴
مدارس و دانشگاه‌های مناطقی از کرمان تعطیل شد؛ آغاز فعالیت ادارات با یک‌ساعت تأخیر
🔹
به‌دلیل افزایش آلایندگی هوا، فعالیت مدارس، مراکز آموزشی و دانشگاه‌ها در بخش مرکزی شهر کرمان و بخش‌های چترود، ماهان، شهداد و راین امروز تعطیل است.
🔹
فعالیت ادارات، مؤسسات…</div>
<div class="tg-footer">👁️ 7.97K · <a href="https://t.me/farsna/466541" target="_blank">📅 06:45 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466540">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4626e38b60.mp4?token=YueSwhOFGLlK2nduwIFNnkas7zD_XH3NrVj3sWcKBcoA_32xTXUotIT-3tZTdqbqHJ13xGUm-CzUdPux8myrdHXbwri1BMXcnGdk6jUxsfC5Q0wnRpzld7xLaj4SyYRBXP-NwFUqtTf4_ygMQ7iNf7ul7lTq_UoXW5Fq1E4-Gm2FXepgNDlLwOgO95NeGGsLvp3gAnEqGKTWLGjGz_JMvwRAocvUxiVPmga87gCA-blavLVT1568R1-Bu0s0a0BH4h9hpEGt6Vr-_mZvvcJAgOIu40cU53SQum8V5SPFp_TDX9w8cIZ9SFdN5dPKd7TcDpX5d2_deWjHTOdAUdBGhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4626e38b60.mp4?token=YueSwhOFGLlK2nduwIFNnkas7zD_XH3NrVj3sWcKBcoA_32xTXUotIT-3tZTdqbqHJ13xGUm-CzUdPux8myrdHXbwri1BMXcnGdk6jUxsfC5Q0wnRpzld7xLaj4SyYRBXP-NwFUqtTf4_ygMQ7iNf7ul7lTq_UoXW5Fq1E4-Gm2FXepgNDlLwOgO95NeGGsLvp3gAnEqGKTWLGjGz_JMvwRAocvUxiVPmga87gCA-blavLVT1568R1-Bu0s0a0BH4h9hpEGt6Vr-_mZvvcJAgOIu40cU53SQum8V5SPFp_TDX9w8cIZ9SFdN5dPKd7TcDpX5d2_deWjHTOdAUdBGhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصاویری از آتش‌سوزی در فرودگاه بین‌المللی «ریاض» بعد از هدف قرار گرفتن توسط موشک بالستیک یمن
@FarsNewsInt</div>
<div class="tg-footer">👁️ 8.15K · <a href="https://t.me/farsna/466540" target="_blank">📅 06:32 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466539">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EgI40gAq40WPNOH6sz5znL2MQNiH5uU564QygyXDPl-1NLM4NAcYM7fza0hw576ixr7WVwINsY0bGG-7daawcsNxz7fQUfKSMqK_vc8ZfOt5i3P9R_cICRmCurMwik0HG71xlRPrO-Rs6eqgn4AsVZ5WhEy4iIIg1oZlASxzRjzBVp2uXMr6C9wMKAPkLwxITcMDCY7lvMaGpQHd0U7hUz25SlvSMT-uai46C_364bHpzeIzlSjGgIUlVTje75ddveGTHWX6vOJTlpKdposyb17-rEXY_7CKfQ9E_bKruA-TcycCQWRZL8wsDXBrCBQeOjW1NnVKNm34BjKU_3KqcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌قیمت کالاهای اساسی «تورم صفر» اعلام شد  برنج:
🔸
برنج پاکستانی سوپر باسماتی: هر کیلو ۳۳۵ هزارتومان
🔹
برنج پاکستانی۳۸۶: هر کیلو ۲۲۰ هزارتومان
🔸
برنج هندی ۱۷۱۸: هر کیلو ۲۸۰ هزارتومان  گوشت:
🔹
گوشت منجمد گوساله یا گوسفند: هر کیلو ۱ میلیون و ۵۴۵ هزارتومان    روغن:…</div>
<div class="tg-footer">👁️ 9.36K · <a href="https://t.me/farsna/466539" target="_blank">📅 06:00 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466538">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-footer">👁️ 8.84K · <a href="https://t.me/farsna/466538" target="_blank">📅 05:33 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466537">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IJBsiRPq0ES-q-7OixPmvKnWl7CmKEWcusAnW1FZDBsxYx62co2sClpd3ANW3J8vvBbrnwIX6f5kyxzCrubUI3Guk375YgKyUfffYMMmyc80_lIqzxLxrIzbP-nCc7Hrabh0blGICcBP66FRt4NO-6RN6LFUfUNSRBpBCnvltsmE4OGysjZCducPxfydWVtDgWp9JMx-f5r63OS2pyHRj_f_Sn42y-9jrJg5eBomH7PuDUZk8Nb9t77JIIu6k2B9mLpd2igqR_RA7MODx_YxU0HuRcF7klyA8v4hhRuffnVKWu0WkQPIQlvaqVX6sjVTgYBI1FtoouQyBYjowcimQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کمک نظامی ترکیه به اوکراین
🔹
وبگاه میدل‌ایست‌آی به نقل از منابع مطلع گزارش داد که شرکت ترکیه‌ای «آسلسان» چندین فروند سامانهٔ پدافند هوایی کوتاه‌برد «کورکوت» به اوکراین ارسال کرده است.
🔹
این سامانه شامل سه خودروی جنگی و یک خودروی مرکزی فرماندهی است و شرکت سازنده آن ادعا می‌کند این سیستم در برابر پهپادهای انتحاری مؤثر است.
🔹
این منابع که نامشان فاش نشد می‌گویند ترکیه در سال جاری چند فروند از این سامانه‌ها را به اوکراین تحویل داده اما تعداد دقیق آن‌ها را مشخص نکرده‌اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.91K · <a href="https://t.me/farsna/466537" target="_blank">📅 05:13 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466536">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H_rWCTu5gVXvoWgymUceKEavzM7I-L98wKAKUuzX2CNaHDWck6E2WuSSI_w9XCkBAKzE53PUcHbNt08QQSBTsBgu87EzOAr-wbay0vTbpQDny8ej1zqd-6jCg7nEsiUw18wLjYJOqdZSBPQ5CDbSGALpSSlY9xlL0C_Cse92GrNV09XS_uRP8JGJ9OQQJhs7PTW0NoZJLQiaZ5CpMzVFjCGy2m6e_cLT44lGeGT5ncoMRh6UHgOrgl3O4iNnY1txpCoA8PcuLOOLAdO7A_XLbgmeEqRIJ5OvvMPf7cqWgTT8cbBQQIVSKuIZ6c9EXWUGITV3SkMehb8G_VT1EFAvsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یمن: عملیات زمینی برای سعودی‌ها خودکشی است
🔹
سرتیپ «عابد الثور» مشاور وزارت دفاع یمن هشدار داد هرگونه عملیات زمینی برای عربستان سعودی، خودکشی خواهد بود.
🔹
وی با بیان اینکه کنترل تعز به معنای سقوط آخرین برگ برندهٔ مزدوران است، گفت: حالا عملیات خارج از خاک یمن به سمت عربستان سعودی به واقعیت تبدیل شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.96K · <a href="https://t.me/farsna/466536" target="_blank">📅 04:42 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466535">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس معارف</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a7a8bf03a.mp4?token=iP4BH4rPIT5n6awv3YUp1_dAem8X3GFBOsW2EVUUsOiRRM5Lo-fjdkzu49-eqWDQqXCy8LXDknBgCMHpV_SgMiod7v27HlqKNhfZyq_Xdxdo5DtRgzTuDenRoplj-KPbq5mJnBsn8ZZWrNxasTkNxRBntwMWE828JElkg6pIvgSj3zYb_n68xsTLZHK9Z0yolGHZMXPMPHbU5OlVf5NUzNlsZhTopURMzCvi0TVA0mCQqNCWnia3IDamAjaDKZSw8IBtq0WM5_JiCFpCPloVssQ0114e7RD3DS0kgXw3lQb5wAGPJb43blZ1jvw7jXMLBpZoQ3XYrLUXQPLWZrsBw3bdRCwavgEXgveIv7n3ixtwg5czfARLIaxNwu-8CfFAGaEXm1zV7WmvK_TTdzku0rVuNocUKuMtCBGwVgfCYnwM2Iw9d2R9l-ZrHsf7OvcE3TOo4qvu1rNyUzQEb_X1pALNsImpWEU-TwwlQpNvUmh54gIpZwwGtVNLU4IcnYfDCKg_80Bz1puj5twA9Ggatw22rZZJker1Pm_MJoV11mB_MajXZ8KSGpGE1mJATOOjMebdREoKeHfl9qVLGbtxhvlTSnWbfBZ9yFQyJaYzglOV0_9iBuDJIF-J3A0VVBELwRhe_AcutmpbQJkhS1iR6CCGHGtCIDs8ltwg9t24L3Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a7a8bf03a.mp4?token=iP4BH4rPIT5n6awv3YUp1_dAem8X3GFBOsW2EVUUsOiRRM5Lo-fjdkzu49-eqWDQqXCy8LXDknBgCMHpV_SgMiod7v27HlqKNhfZyq_Xdxdo5DtRgzTuDenRoplj-KPbq5mJnBsn8ZZWrNxasTkNxRBntwMWE828JElkg6pIvgSj3zYb_n68xsTLZHK9Z0yolGHZMXPMPHbU5OlVf5NUzNlsZhTopURMzCvi0TVA0mCQqNCWnia3IDamAjaDKZSw8IBtq0WM5_JiCFpCPloVssQ0114e7RD3DS0kgXw3lQb5wAGPJb43blZ1jvw7jXMLBpZoQ3XYrLUXQPLWZrsBw3bdRCwavgEXgveIv7n3ixtwg5czfARLIaxNwu-8CfFAGaEXm1zV7WmvK_TTdzku0rVuNocUKuMtCBGwVgfCYnwM2Iw9d2R9l-ZrHsf7OvcE3TOo4qvu1rNyUzQEb_X1pALNsImpWEU-TwwlQpNvUmh54gIpZwwGtVNLU4IcnYfDCKg_80Bz1puj5twA9Ggatw22rZZJker1Pm_MJoV11mB_MajXZ8KSGpGE1mJATOOjMebdREoKeHfl9qVLGbtxhvlTSnWbfBZ9yFQyJaYzglOV0_9iBuDJIF-J3A0VVBELwRhe_AcutmpbQJkhS1iR6CCGHGtCIDs8ltwg9t24L3Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خودت را با دشمنت بسنج
🎙
حجت‌الاسلام نوروزی
@FarsMaaref
💠</div>
<div class="tg-footer">👁️ 9.15K · <a href="https://t.me/farsna/466535" target="_blank">📅 03:11 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466534">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OIl-JaM6ab76hemy8kHrAF_gBGxY7xpap22nSYGPETztLDG_M-h4eZ2N2hEwfUOBVhB6MEoKghTkB_khsaEHxgNO70CnOsPRuzy_-W51oUWMtXjAuIzr8eT-bu5kKwQB2Eaj3j3SpM7_DuWtfoWCVyzL820uMUu3Dt18fkh35_aoIY7qUURhNH7cOVx2Rm0w1f2btyP8ZGcyWJsDEF-XFbVas-sdWg1YCPzLGSCjzql5FR6rw2wUMTriiGHqKMS2d4oLFhc5iqK5zkk5C0wkeXm8QMH59RgPczeI_dZu7rw1GLqKn0vhbertItRYl2UeVqt-uTOtPHOB10eVZ0lKwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پس از ضربات یمن، پاکستان و ترکیه به دلداری ریاض شتافتند
🔹
در پی ضربات تلافی‌جویانهٔ نیروهای مسلح یمن در واکنش به تجاوزات عربستان طی حدود یک‌ماه گذشته و ناکامی سعودی‌ها در جلوگیری از پیشروی‌های یمن، پاکستان و ترکیه که تاکنون با وجود امضای «پیمان مکه» نظاره‌گر تحولات و ناتوانی عربستان در برابر این حملات بوده‌اند، اکنون از آمادگی برای ارسال نیرو و تجهیزات به‌ منظور دفاع از ریاض خبر می‌دهند.
🔹
کشورهای پاکستان، ترکیه و عربستان سعودی در بیانیهٔ مشترک تحت عنوان پیمان مکه مدعی شدند که امنیت هر کدام از این کشور بخشی جدایی‌ناپذیر از امنیت جمعی سه کشور است.
🔹
در این بیانیهٔ مشترک آمده که اجرای تعهدات دفاع مشترک و تأمین نیروها و توانمندی‌های نظامی و استقرار سریع آن‌ها در عربستان سعودی باید فورا آغاز شود.
🔗
شرح کامل خبر را
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/466534" target="_blank">📅 02:29 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466533">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-text">🎥
حالا نوبت دعوای خطیر و کریمی شد؛
جروبحث دو عضو هیئت‌رئیسهٔ فدراسیون بر سر تمدید قرارداد قلعه‌نویی
@Sportfars</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/466533" target="_blank">📅 02:02 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466532">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d0eQ64vVqCApJLTuQ58mwZ_IJPzVDXO8OurJEDeGflyAkOhVN39L5FvBRvPZCreuX6eOZjHDVU9iUePnWEvS0yUu3NoBaqedoI396ADBA4G0a9wwRWM_A8qbPyA9zv6pckKmx_PnPeStYbkGA7zKaH1mjD5JRvb_wq8FOejaFeF2pCZ8nuVKBIgsYqDdSb2t_YiYHR4lahTUKCodxgvoUNpwZ6Z3xPT9sPA3hb-w47i2m2Omiz6LRwRwyWAdfkM6vjhsBYtYM7eyGl3Zv0WsKN1vuC7FZ36Y_uD96FzZ0L7U2LG-smAW3UvWyRRzb-2fTGcacC3JaELx2eUk5TmMuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گزارش‌ها از سقوط بالگرد آمریکایی در دریای سرخ
🔹
یک فروند بالگرد «سی‌هاوک MH-60R» متعلق به نیروی دریایی آمریکا در نزدیکی آسمان بندر «ینبع» پیام اضطراری (۷۷۰۰) ارسال کرد.
🔹
اطلاعات راداری، ارتفاع نمایش داده شده برای این بالگرد آمریکایی را صفر متر از سطح دریا نشان می‌دهد که احتمال سقوط آن را بیش از پیش می‌کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/466532" target="_blank">📅 01:34 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466531">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0cf32291e6.mp4?token=HiDl9cBw-zzp-Egli6nbd3c5LWdV68RHze2tPdy6jIsPOzIH0KmMMng4kREawA8Y30I7ddeemCFr7NqqEZMLQSTvnRxG6DFz7RXv_48tzub3zRRav6ZDGgkmjK7XfxwFM_TIZUhInuQqTatDscs3YcebpuyAAf30RRcuUNddzMyGo36dax5wvdszKFwY1xw8hmYk0-fA2v9ewfCi-2ANW6M0vwiBNhhSVC1DR1hk2h5b1GMVUO4tlEKOsxC1YQmvx76eQPYyBWVAEKd-dTt9shMQdFAUATGNZ5SbjLpPMUPD_GHjOo8_29NRYJTmJ4vI9xbwgagm-jq4pCRBi7IYUkc44vCXx4SK1aDICG7Z2gr8nj9zw2E4QMH3MbHbYrhfNoVu4cYx9eXGeo_VCwf_4VvlOsNqf-HGobZLQhhNtCCB0ubcKWbvdbrHJVmWC2iTtv9ifer2SZmlp400Emo93c3zphF2GDFTgnT1GxTj9R6VGy8X-l3l3bvstXsTBvPrwvjgt8sYxFJqCVv3CaAxdAqFsWA_WvVCB811qDe01jV8LG_qyH6ADMVPXbpuPMGkjN8KDGu_QdH-zGjC0BJqzJGaS1uVLl6-9S1rD4I6HE6bv-1iML-3P9p21Qs6gxBDAB57zOhE288MuvkEHiccgozbaaIhVnK38D4GRMEIuAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0cf32291e6.mp4?token=HiDl9cBw-zzp-Egli6nbd3c5LWdV68RHze2tPdy6jIsPOzIH0KmMMng4kREawA8Y30I7ddeemCFr7NqqEZMLQSTvnRxG6DFz7RXv_48tzub3zRRav6ZDGgkmjK7XfxwFM_TIZUhInuQqTatDscs3YcebpuyAAf30RRcuUNddzMyGo36dax5wvdszKFwY1xw8hmYk0-fA2v9ewfCi-2ANW6M0vwiBNhhSVC1DR1hk2h5b1GMVUO4tlEKOsxC1YQmvx76eQPYyBWVAEKd-dTt9shMQdFAUATGNZ5SbjLpPMUPD_GHjOo8_29NRYJTmJ4vI9xbwgagm-jq4pCRBi7IYUkc44vCXx4SK1aDICG7Z2gr8nj9zw2E4QMH3MbHbYrhfNoVu4cYx9eXGeo_VCwf_4VvlOsNqf-HGobZLQhhNtCCB0ubcKWbvdbrHJVmWC2iTtv9ifer2SZmlp400Emo93c3zphF2GDFTgnT1GxTj9R6VGy8X-l3l3bvstXsTBvPrwvjgt8sYxFJqCVv3CaAxdAqFsWA_WvVCB811qDe01jV8LG_qyH6ADMVPXbpuPMGkjN8KDGu_QdH-zGjC0BJqzJGaS1uVLl6-9S1rD4I6HE6bv-1iML-3P9p21Qs6gxBDAB57zOhE288MuvkEHiccgozbaaIhVnK38D4GRMEIuAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بگومگوی خطیر و واعظ‌آشتیانی روی آنتن زنده
🔸
شما رو به‌عنوان ایجنت می‌شناسن!
🔹
ایجنت خودتی
@Sportfars</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/466531" target="_blank">📅 01:27 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466530">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">۷ نفتکش در ۵ روز در هرمز به آتش کشیده شدند
🔸
درحالی‌که تقریبا هر روز ترامپ می‌گوید که تنگه هرمز باز است و آن را کنترل می‌کنیم، گزارش‌ها نشان می‌دهد که نیروی دریایی سپاه هر روز تقریبا بیش از یک نفتکش را هدف گرفته است.
🔹
اکانت رهیابی‌های دریایی منچ‌اوسینت بر…</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/466530" target="_blank">📅 01:21 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466520">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fsleZcUR0V9ddqv4Z_6jFUnZ-9B_Xqf6fvwz8OYh8aLBl9HBtUZ-E0sGE0iKrcuOK3d0B5d05dI7UG-gn3dOBbGj2G_xLlRqd5-SKuKo88W07TQBYbLRHvpBHM5d-9DVL_wyY_FewJAZJTdwxpr8eeUPlRzLtcZ5rUc05eOPBkEzdZCWIgpbcnUry51MxtOn1h08NgbbYzwAv7MNGj73F9uT1XB9atuSHscIIPR4ia9P4R4Pny_or8hauNpFIotOUoSFbWS5rxt12bUx6nMnCWndkwqZsI7ntTrl_Rk4fMMkS7zcQLjvYkWEpI2Sm-vMQO4f2t1WlO8eHPaWyhl7yQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZGzh5UXLA_HvJlnG0XkzYaaf4dmxNGpdqCCXpoX1Y0T7gxM6Zw5MTUrRVmnyttEQKPvqaG4XRCBHE4-CWnNfZzrZHO2B0jMOowROlS-Sjwayp_u4P8WMH8-UQYdFl4YyUZ9K4wrSfwbLrEPAzXev63O9FVxjBEH38s_sR4uU_ysBrB9rsQC9OKliKue0_NrXzodnoatG6ZoKZdzSnBeWMDgyCvm3slH9ZFqKtxhHO3scFSC2yw8AOby-O0WQQ6r2HT1w1Alc3A5UgYpc15i4Zk4ODlWr2QozPSUMTRLGyosU02k0e9L1Ql92xQd9bonp4VHk7rOaBaZr0zczEAi2Jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/m7pJfLyMpBOW2kYtPOFjDWnlQsiN1FMUmlAPNgNxKNIPTvrMr3vWzZOX6N_z_VjZXjP9N-DI9Bpy-v-2uyjYsY1b778BVXd2qp62Uzza1xJIzZRP-qzQxtuflpJ8-1MrvugQDpDV-w-D4NJCPv_fTp0QXbl9qaCALZ4uqha0kXUw9NZB5_-YymP00Ebfj72knOwhIGvTgFbVmcDcsTlm1pBOZ8VqbQwoOPdRJ1iYVRO08dNC9N0-wPjRuaOGR5oTSDnFPqJMQF6_nIpeVlsJwkEIhjRmBlK0x4hmTLQiJRS_xvdgV9zRNb5uZ5eqNxDhhRDeopVbu1_3Y2tM2l-neQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UefHPHd8ITxuFMGnnA7H5cUircYt1Yqos0nqJQNZvJshxci1eGv_HI3i7D7IjesBvgGcfJi0KbAHwZAwDqYN2xnibYQNZwIMXU9w0PU-c9fjaCTRti3doz_JaNBp90HsFjHn_sWu9TOytupGW17p7i5BmZweWN2zmYZ9VS43bEJXM_pYnKuMOnOXV3IIgYP72Wcot-fVCgBeBd1U4mVxXP53yj34JtYt4ADiq9KkjYuJyY3M7fDSvyOQKfEdxb7Bbv3f-G7OLutDoCJTR_rmB3Zxw_PDtWwYBbH9dMUdH38sTEVzgTeXTkS6FyVM4RMC6qlFeaZKs1Dc0JMSZr2kNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QQiE4Per4y-ySbu3bBScyAJ-LLDi0gsMsI4YUi5ay2HRYvuB9fhZgnF2m7yRRxyQ7_hgDY7Ht98ls31Cf3OOhEwLCrmwQlnefHE5PAerQ8v2BuFWf9BaYJqiX2CAepsiK7qWu8dsD8pxZ03I3UvIGSxqCy732RChAkG7nBeQL_OUi_wiCZRbg493BKbTtRGI6150COdcQsg2xpUC3_5btWL5gS7vohTYObt6M41cgRA-_8mA2wAo4kFLjx22PKG4Q9NxpDxQRG_hXAT1fS-tJOO_3253bpAZGrAyDnXT7XdYgN9uAMK8KqSELRaxNWlxXkvaiChPUmGHGtPDFUrnyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/puNXfUD85AzzJg-5VRZMmEIxVy-3qR0I7w4xxU-rq3e_uqwM5gkCBE3RCDs5G2vEk43EumRMwRpwdIlNjHIyXjjXK7XmNYY38ECvy3CpC5x24XNBq_bQL0mjc4a5hXPMlJyUveMrXakqT_i-zRonBNz7uBax43LVS5YiYdG3b-YFhWFFweLOq6nYH4NNPtzYLOuDzfbFVjfNJ6_-7PsfPYLDfvHETJLGdv1m7DOHa8de5hfFJkEHyYz81HxZoYGQBdoqNm_QklAdyTks5SjFJQlIBqpZ8tFM03q9wPUR9vDeLx-skAFCnJPXzdNyKTmXz4ap45UkKN72Gbh6xcYc2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nyXYha4mbBp0UZyWcq9w8E239xTF7RJAliNjs9nHEu80dkXlI5saStmtgwP9NvkVPhGLlawz1pU7pJkOWp2shjJMXfMwcvIF7OXA9gDTpifCyQamjFD9YvUdf_L7HLvwqyegLkFDwMLti2r5-rXNbXYttgnvlNyHoADYoYFAjAjj43bDVYgJWxbjA3kbPjjhYTiaeMqxYIzFrRGtKnX-YmF6w9m5S4Q8kuS6wfA_V-XJCYyUwtG1gK4UVG9PVG-Wc7Jg212NH5g9IcFODP0kbYPQT4NWCRpNuaQKqJd3fYRDj0YkySoWzuiKbMNhmx-zxkWYOfjXpKgpVbtsepHjMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CGeGoHWlFI5FL-ZLJrXO50t8-bcKrN9NkGp-tdwtnrcv7JQizUp0m_feaNfDKjPpF-N4mDFyoBNN2CgAHcvrIEIRmCscSDxuhDbrOs0ld9Z7xeuZRMAA3LfU_Jth3297pwCbjCIEbmXYHcdXlsIL2fv_gUJE_h6QcCilNEZQDalJkrEjh46g-fsrkcImXBNtI5zPv3q9wiqYH2gCLXTiPK2kHy3k6SvX5spfQWKykcWnGsO4eb21aV1SiAG-8xWQCZwt5CkEwCwX-1O0tO6gRdnneB_zYDFVnTEKDKarFSKoxOnivwcat5z7f8VaU4DEXLm1DGiZz6t8ih-jjb2b7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/v8lOr_jereEm_6qWzXIyQI8yw4m10E3gu49qi24FArNNAS7B4VLwMxx6BAkE-v2yZkp3U3zgQ8d1hR_YTuQmt0_wbnAl1mS931xHeZJOe86fmiY9O4vyBILzl4KijBW0LBgT0yn8fxvP8CDV1DHMupmfNuDvSSkPOpXaodS0LSlElP8JRM36WQxjjVrhDyF3HVhXIa6sFtAj7Ln2oDrr_u-o1OfptGb6Dl8d1U1jlWHU7ElNid7ym-_hl8dwwI4f23ePvtfjNv941MWoL1I1k8CgzFNVFkof2_5mcaPGb0dvys_ZBL_JsRAbzAnC6r7SmId-Kxlr834xZnT0aQQQcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BPuCge0o3LP2BLEejIWXEiG0udg24wzFIT6geAWuCMBBy9ARpGpggMuCMtLfbkvbu9NUiHc_vy4w9uW6p6TXZi__aQSURm0PdYqHZKwMlHVoco5qBxj4DyhnLYLDg2T8-LFqHZiKe9rAQ8wqXo_PtYQ4934OfiAhlm5AmBqnJRSAOkVA_yT1UG7AwLery7Y5BKlSucsnjf4wwyEEkURFq9ixlyh0ea7pYx7PdfOGTESKwH10CkHsbJdNg19tBzSRliZW6bgfr32mpD8gd08XTIXKLoiKiZa4EkD2UVJM8loL5XEPns14sCG2Oc6etPBMSUrgSmFd1Q-4rHXLQ7MuZQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
بدرقهٔ قهرمانان؛ به مقصد ناگویا در میدان انقلاب
🔹
مراسم بدرقهٔ کاروان ایران اعزامی به پنجمین دورهٔ بازی‌های پاراآسیایی ۲۰۲۶ آیچی–ناگویا در میدان انقلاب تهران برگزار شد.
🔸
کاروان ایران با نام
«جان‌فدای ایران قوی»
متشکل از ۱۶۶ ورزشکار، شامل ۶۲ ورزشکار زن و ۱۰۴ ورزشکار مرد، در ۱۵ رشتهٔ ورزشی راهی ژاپن می‌شود تا از ۲۶ مهر تا ۲ آبان در پنجمین دورهٔ بازی‌های پاراآسیایی به رقابت بپردازد.
عکس:
صادق نیک‌گستر
@Farsna</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/466520" target="_blank">📅 01:04 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466519">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pSVk62kmWYDvHVSrOv_-g-4ywQZUUG3IBTyVufFczzuF_o2li61DbY9c5abMrueDYEdWrq6bEYHMk7AEqRTRubzjW0D7U1IWx-gC6QgE1ZEEBxtuOWgNtVhJveDNgJKiv1GzLo5Sd-h0VNvrQN9BSSV2A0uZ2z5CSh1zXqNHgPgNh7r6BCyaQ-0x95hr1A6pIDr0XqMJ0FZ5AGJfn1u54NRa-BJU0dtAgE68MEhILamJGypaf2nG45yO43EQ6rZW1ird9OSK6QXb54narq_Mp_mDKq_Xcpt6XpgYyCzNcV0tewb5xexrjXoPGwDLb8443BA-oo4YI3_--WfMoVcD8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دبیر کمیسیون امنیت ملی مجلس: تنگهٔ هرمز باید بسته بماند
🔹
بهنام سعیدی: بازار جهانی اکنون هزینهٔ اختلال در یکی از مهم‌ترین مسیرهای انتقال انرژی را پرداخت می‌کند. کشورهایی که تصور می‌کردند می‌توانند بدون توجه به نقش ایران برای امنیت منطقه و انرژی تصمیم‌گیری کنند، امروز با واقعیت متفاوتی مواجه شده‌اند.
🔹
جمهوری اسلامی ایران امروز از یک ظرفیت راهبردی برخوردار است که نمی‌توان آن را در معادلات امنیت انرژی نادیده گرفت.
🔹
پیام روشن است؛ نمی‌توان امنیت منطقه را نادیده گرفت و همزمان انتظار داشت مسیرهای انرژی بدون هزینه و بدون توجه به منافع ایران در اختیار دیگران باشد.
🔹
تنگهٔ هرمز امروز به یکی از مهم‌ترین متغیرهای بازار جهانی نفت تبدیل شده و ادامهٔ این شرایط می‌تواند آثار آن را از بازار انرژی به تورم، تولید و رشد اقتصادی کشورها منتقل کند.
🔹
ایران به‌دنبال ایجاد ناامنی برای بازار انرژی نیست، اما اجازه نخواهد داد، امنیت و منافع ایران نادیده گرفته شود. مسیر کاهش فشار بر بازار جهانی از پذیرش واقعیت‌های منطقه و احترام به مواضع ایران می‌گذرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/466519" target="_blank">📅 00:45 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466518">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">تمساح</div>
  <div class="tg-doc-extra">قسمت ۱</div>
</div>
<a href="https://t.me/farsna/466518" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🎙
#روایت_شب
|
تماشای معمولی با پایان غیرمعمولی
🔸
یک کارمند، همراه همسرش برای تماشای یک تمساح به بازارچه رفت اما در جریان بازدید، تمساح او را یک‌جا بلعید!
@Farsna</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/farsna/466518" target="_blank">📅 00:35 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466517">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UxkETbM9YqNHtBpKcJ31r4zkxof-VNVW3k_eizMM2LY71-Cdw_s6dvJzf_vqRVmZjuScKv8wg1_qTjHiGls5Uaahd4gxcl06o_g3Rf_qKGMAK6uj7S1nvd6ck21yCK7DJx4WsFh41h402xS_aIUpNVP2uHSRaB_gMf3IyxdhSV6fJz1FX-mirrxhZwFdbvO5YxYS_Ati-LwnWE49dKjoFOe1Iohkhmn_MAmaLCR8ClbI4ITaWmo0MYEG0WtY6CV6qkgZhccUCTHzS9V9bkaxoBrWZl-LCLo04oTi_pSrY3v5R_zeVrp3QTQEYPQWckmIZGLsWLm-VZ-zozkIsyIswA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌
🔴
برخی منابع می‌گویند فرودگاه ریاض هدف حملات موشکی نیروهای مسلح یمن قرار گرفته است. @Farsna</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/466517" target="_blank">📅 00:32 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466515">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PSJsAguLqK0i4-kmWMsljDFUb0fydnCIfEIjOC15NtlXEb_HpnsDpw1vQGPJD5vJZkJY_YhHbSMM9kkImmtsckgh-eL20mDqazNE0vR_E5Kc9AWnaoXX4FpZEVz_vAUFYKcReweOgh-2s36f1yzZ3-wHxifarLcIzbn-DwM2WwHQvN705dr8sAeTlKGjvTrDmRRJNmfJqax5groIO2tqW2O8WWvc0Rt-K4_R5Fy5PjsTunlgWuIBKSRrDituX_PO9SqYbodyNhve16G3n965OKMvxSxc0YoyH6YS91tYN6EhVf9PdfcfmWF9Tkqef48jf7ly8EgGla6ospw-v7eQ-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دهانی که بی‌موقع باز شد
🔹
در برکه‌ای باصفا، دو مرغابی با یک لاک‌پشت همسایه بودند و میانشان رفاقت و الفتی عمیق شکل گرفته بود. روزگار گذشت و بر اثر خشک‌سالی، آب برکه رو به خشکی رفت.
🔹
مرغابی‌ها که دیدند دیگر امکان ماندن نیست، نزد لاک‌پشت آمدند تا خداحافظی کنند و به آبگیری دیگر کوچ کنند.
🔹
لاک‌پشت با اندوه و اشک نالید و گفت: «بی‌آبی برای من که حیوانی کم‌تحرکم بسیار خطرناک‌تر از شماست و زیستنم بی‌هیچ آبی ناممکن است. رسم جوانمردی نیست که مرا در این بی‌آبی رها کنید؛ فکری به حالم کنید و مرا نیز همراه خود ببرید.»
🔹
مرغابی‌ها گفتند: «دوری از تو برای ما نیز سخت است، اما تو عیبی داری که پند دوستان را سبک می‌شماری و دهانت را به موقع نمی‌بندی!
🔹
اگر می‌‌خواهی تو را هم ببریم، یک شرط دارد: چوبی می‌آوریم، ما دو سر چوب را به منقار می‌گیریم و تو وسط چوب را با دهان محکم بگیر تا به پرواز درآییم. در آسمان، مردم هر چه گفتند و هر فریادی که زدند، مبادا دهان باز کنی!»
🔹
لاک‌پشت قول داد و گفت: «فرمان‌بردارم و تا مقصد لب از لب باز نخواهم کرد.»
🔹
مرغابی‌ها چوب را آوردند، لاک‌پشت میانه‌اش را محکم به دندان گرفت و به هوا پریدند. هنگامی که از بالای روستایی می‌گذشتند، مردم چشمشان به این صحنهٔ شگفت‌انگیز افتاد. غوغایی در میان مردم برخاست و فریاد زدند: «نگاه کنید! مرغابی‌ها چطور لاک‌پشت را با چوب به هوا برده‌اند!»
🔹
لاک‌پشت با شنیدن همهمه نتوانست طاقت بیاورد و خشمگین شد. به خیال اینکه چیزی به آنان بگوید، دهان باز کرد و گفت: «تا چشم شما کور شود!»
🔹
اما همین که لب گشود، چوب از دهانش رها شد، از اوج آسمان بر زمین افتاد.
#حکایت
@Farsna</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/466515" target="_blank">📅 00:12 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466514">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UhtmBi8NegCiqI-TDlRj7MEePacHeuYZCVVgtG0QGz1V8zssAkzBQRfFxDSWs9ANkQr4PKpQ90U0jbGnYB3CUTcje6wxv4KP13gpAmsB1IfW7lXT0t5RIYfa7DBBBVCkbTqcrec5fmMsiwMOQXJFdhlbBvG2ULzDqHNs8GLIkD-dw6AzTbZeM6S9Jk9aT9O0WxGNiJ10CnjDMkCCW8rbNveJNpEZlW9ry2R6MIuC-ExOKPciNgT9xb36tV_wLgvHrek_Rfr7TLDofq5lSm0--lRwuZDFooPZCNa0vH7AVtxe90og8JFurIFtOaZwIbU7flgS937DO3JX_AI4y9eQVw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/466514" target="_blank">📅 00:04 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466513">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cFFifYhRZF471__bk9XQl3RZK2Hztmz7gNAbnNmwW00qTwrPR99waljqw4aHJKT6QTFbB8GnyUVGFbO5aYQfBo5KDSe7gezn_Ql5rhmMxnMKpvcUPTzAxvKm9RRSue8-WcVYIvnhnSof6shenRiXsfALZLsGrQBk2wuKkuyGZG0wBi35SVr_5m4gUIDFOl-0LWSo51BADQH2QbYs_5R4uQlf8vuAww02VsAsUqNz-dq7dtJhuVT6u7su_GtNLJjK6jePOEjBooR_s75U9MrABpsSAmpJR-kQD7s-iBqQgd71cAEeCKlp24L01lfWAl30rgxeYzJci1ITETYP5sPTiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیروهای مسلح یمن: در ۳ عملیات ۵ هدف در عربستان را مورد اصابت قرار دادیم
🔹
فرودگاه ملک‌خالد ریاض
🔹
شرکت آرامکو در رابغ
🔹
پایگاه‌ خمیس‌مشیط
🔹
اردوگاه نظامی در عسیر
🔹
مواضعی در نجران و جیزان
@Farsna</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/466513" target="_blank">📅 23:51 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466512">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">جزئیات واردات خودرو برای نخبگان خارج از کشور
🔹
قائم‌مقام بنیاد ملی نخبگان: نخبگان خارج از کشور در صورت بازگشت به ایران، مجاز به واردات یک دستگاه خودرو با سود بازرگانی صفر هستند.
🔹
همچنین این نخبگان از حمایت صندوق نوآوری برای تشکیل شرکت‌های دانش‌بنیان و مزایای قانون جهش تولید مسکن برای خرید یا ساخت مسکن برخوردار می‌شوند و در این زمینه در اولویت قرار می‌گیرند.
🔹
نخبگان می‌توانند تجهیزات علمی، تحقیقاتی، آزمایشگاهی و حرفه‌ای مورد نیاز خود را یک‌بار و به‌صورت غیرتجاری وارد کنند و از حقوق ورودی معاف شوند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/466512" target="_blank">📅 23:49 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466510">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/llCut0WV4Sh5dQ3NUs8se3oYZtZbZXIl8alartwA2Z7KoDrVhJDZuxtlBjwuilJhrRzHetKwfiy22Z-DfKvJm5GImiOu1BmbRBTIPB9JIVbPpg19b_ftVJ6tNR4s0ahdZXRakTXwygGJoTfjHsp2NcmXVi1huXf0ZHZXnckAt-t4CPtMeD9LRjmtMJczwnOpedJhqomKODnbu1Q5XHkGFzMRDFKXp79ZyxhhqBnQw_l7DV0_WB2kyAFXjD4ESJRQwhbmDgBulxp8m5XSBjZ-wgSSqcXxJ6IHhVkfLaZ6TY55REVMlZJYbt5WGTCLYeP7AvvW4dBdp2rDgtCmhrO1Ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XFOafkyoPAVcQ2Yr8RowszzsVARsma0C8miKj9Jof_K3H4EXHTI9w6IMlgtTDxnGGeGasU88aNJpnsrev_D_5yjl-CD-KEctCUcStvph1r_jtArHGWOFlumu-Fv8GmiUh8oSya5j-FjlITZRZE7meDchg_UoPZYx3nJH6bJOv9oBFPsn2Hs9MmWy932WngBqV7BTELAdNg-PkHm4D7kKQwoodyzu1VY0savbWCLlIhoxSHYX9bxslv7p5OJLK0DftRy9sItzdr4hHwhcq5sjmrbfHVOD9WGFTnWTcikqk3YWILvjqwoX6Hs3Y-wbXR5ABXXWULEIwe3OGsPieIn9pQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
تصاویری از رهبر شهید و رهبر انقلاب در رویداد «جمعه نصر»
🗓
۱۳ مهرماه ۱۴۰۳ @Farsna</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/466510" target="_blank">📅 23:45 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466509">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ff1838966.mp4?token=Wvbkr6iIIj_-RlYM2mm1ER9EuxCdq0ExAfTvO8XcF_HjmCnsxcoYJJRsfS5rRyfFVJMGV5AtvJR8iIrNgSFfF3HYzGR-0o6eJXodrlVr5-r3ERqcfunGZ7u0440Pa6gQsyj9XD1_zT-USJ7g3YO5TDzOTgOLI1du_xKLVDKdq86g0P9mEWxXJx-FpGk5D-7KQtnjg82xE0Ogr0w1kYR1JG7OnGlbQkzRWyFU5muKjTX4fe4iBnDwWIm459p5QpuOAA-nlCZIGSRZ1t-9EQyZSt9cDZ2C-EiStj9dOrj4U9lBTnjQlkqt7CT2PBp3DyRWhCgzoeJktpala_03MUtUXwwmq8Ub1dhGylUqJig3H_L4OqIcUoh2dUDpYL4GRJx1S0y8Kxr15cLzbQcEJ10f6egHhMzIZMJZUY0b4cX8RDb_q_vFvKVUwuzXXW53lJspPz4Pv-wGvTSH63DQYsmVRDesdEIU4LMoXkG00KWi9yoduK6YCyXnJFv972-0TQNXhObFESD8zfHTAUfrOr67x5PDQGnbuETvFjcsoBsNYoUh-pjQ0B-FiD7rvqyUv4HTlpLfdYfraLcBW-RWrB4SI-xGHUVpBlkRSJ3cGdQb003ElQYZ0HArpVD1NZkMpjIM12XHhoEXKEb1L0K5IErwPnG6FNQ0JLQwLUWXNWVexPs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ff1838966.mp4?token=Wvbkr6iIIj_-RlYM2mm1ER9EuxCdq0ExAfTvO8XcF_HjmCnsxcoYJJRsfS5rRyfFVJMGV5AtvJR8iIrNgSFfF3HYzGR-0o6eJXodrlVr5-r3ERqcfunGZ7u0440Pa6gQsyj9XD1_zT-USJ7g3YO5TDzOTgOLI1du_xKLVDKdq86g0P9mEWxXJx-FpGk5D-7KQtnjg82xE0Ogr0w1kYR1JG7OnGlbQkzRWyFU5muKjTX4fe4iBnDwWIm459p5QpuOAA-nlCZIGSRZ1t-9EQyZSt9cDZ2C-EiStj9dOrj4U9lBTnjQlkqt7CT2PBp3DyRWhCgzoeJktpala_03MUtUXwwmq8Ub1dhGylUqJig3H_L4OqIcUoh2dUDpYL4GRJx1S0y8Kxr15cLzbQcEJ10f6egHhMzIZMJZUY0b4cX8RDb_q_vFvKVUwuzXXW53lJspPz4Pv-wGvTSH63DQYsmVRDesdEIU4LMoXkG00KWi9yoduK6YCyXnJFv972-0TQNXhObFESD8zfHTAUfrOr67x5PDQGnbuETvFjcsoBsNYoUh-pjQ0B-FiD7rvqyUv4HTlpLfdYfraLcBW-RWrB4SI-xGHUVpBlkRSJ3cGdQb003ElQYZ0HArpVD1NZkMpjIM12XHhoEXKEb1L0K5IErwPnG6FNQ0JLQwLUWXNWVexPs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
باران حریفِ میدان‌داری سنندجی‌ها نشد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/466509" target="_blank">📅 23:32 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466508">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l4N9yYxw9O597VD498-rf1YZeSUtzmOYvk4LUDtM7tEFLYrCGGHdvtKdDbj8uLPU3zwsi6ZtuED9DaZ9X7LWvpd2hpu8VfMEMClGMufr0InUuiDgqVg-mnnWrd3xNy0jnaw0jSQxtWoB57O97ZLb1UT7mp0KrewT3rkCayUhqwo7eHgMji1kYs7c9s8kiBMP1yuckDNQaoCl3UYv0TUwfcx6DlvU3FzpcuiYmDZKgoLT-YkuavEoFvU_1OXaO9xY-dJruSzEdohbIbnx1iu3zl4dscV87O19FY77m3eX_XhTTCRlCtTu7b13-06X1WvvybVQyqWCpTaxgzBg-FhawA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ رئیس آموزش‌وپرورش رباط‌کریم بازداشت شد
🔹
رئیس‌ ادارهٔ آموزش‌وپرورش رباط‌کریم تهران به‌اتهام فساد مالی در آموزش‌وپرورش این شهرستان روانهٔ زندان شد.
🔸
پیش‌از این ۸ نفر از متهمان مرتبط با پرونده‌های تخلفات مالی در آموزش‌وپرورش و برخی مدارس رباط‌کریم دستگیر…</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/466508" target="_blank">📅 23:26 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466507">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S3-oMGIpc0s51U81x2tzYL-3hjg8T0C8T6A-E8S0E07I74xrhLrdYggbxyBb_7zzi5gDKNSQbpyC1JktYV7PJzfZ4sdSd413Z9duh4GzXXyD4IQ_F4m1fIJTltc_MwZvMf_gQXbZxI4Vg3y5Sk3sNPXl1wNMlaShAD9cyYwg-jOsaDnUQyNueolhJ7oaYzzzxx2H0wC42bEZmeS4nu-i0mWpLLnePTtjauJfXkz6GWNYPPAxbBPfIuv4rgDMUknuFVMAiH0iZf1DfxWgB3DPzUQUkrbF1c48WAqENw4dnFbUCZFc69N4h_934eSaLaiS0WwD5yuzmYpzgpwKH_0QVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
آمریکا ۱۲ بمب‌افکن B-1 را از انگلیس خارج کرد
🔹
پس‌از وقوع حادثه‌ای در پایگاه هوایی فرفورد انگلیس، آمریکا تمام بمب‌افکن‌های راهبردیB-1 مستقر در این پایگاه را به آمریکا بازگرداند.
🔹
این پایگاه محل فرود بمب‌افکن‌های آمریکایی برای انجام حملات علیه ایران بود.…</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/466507" target="_blank">📅 23:15 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466505">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bRvrX3Cj2BM92FzVFRDQfWFwh3jnV2yivEWbTipt3RIeiPy4Vn_9PW7I1oEvRVjCXfcdx0QKkCy9kUaCGI0NAseFlc7AU2nQOw1-q68CpRvYygrQj5XiPzgHN6hs8hgtJdOBONkzn1qBF0KCP5l2MDvOjoVdedFs7FrBJd21orLLFt7cmZblqLs1_Dm4FXH11xsp88P6S9kK75LldsLfepQGrE3LYNVciQiu2ErQtT96-EAc5etxltRMgzzCJ53BzjM1AMYmH4zT1zRIrcWBaHy14CSpHQ38kc71VR1ndigx6JGWofIzlCvi7MVaqQ8wBbGH0KPM4QSlLd1_rBtujg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UDq0IjJoJBqb0R8BTNdIsBtPx1tfRFa2BgwsyzByezcicnc0pPttL9kMn8C5lmZzQWoXPJUyJ6Zp9Z74oe6SYlLeMp15vLG5WC_Ffk_dPgzxQ4Kw0yPYt90Kf1ggl-l5wP-F0CAATGaDgu5yOvwzi6oWNhFlCM8dKORCEhPuAFREYJU8DN__8OCjy_lk9k4exRgCr_Dngb8IEYKp3Zm80VQ-kQTlUcvKpr2pFhybnHuhHS6U9fs1uDfUluzKXydYZiUhHKMJAOB5WzUdYbgMPy-XpvCFR2lxhMmkYTb5MQhsuBMmzt39mDtY7pZCPBHRpJz3rriDbv9RWTmBPbbKAw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎥
خدایا اسلام و مسلمانان را یاری فرما و کافران و منافقان را خوار گردان  دعای قنوت رهبر معظم انقلاب در نماز جمعۀ نصر @Farsna</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/466505" target="_blank">📅 22:58 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466504">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/673b28107d.mp4?token=gLt4e-5Iu47-5v_5nfGdnZuME_vC5hxceXBj-F_1g5xPh-prCvf3RI70zb6H-JL0xq3DfaMDfVjQnZkrkAgqsorQZaMCR4Oa1Im96ewkabWJKOVc_5CZjy7OLlzuLo_loH2-6GB1a45ySOc_-7_FqDEanpJ4XXs1G8NHYE2qg0Kx-Z3IAkoQWW5D6Y6NUqsG9-QoXHcij28Ugeg2ivA9q2PQZoloo9sK6wYSNEPJBkspNTP1ZcXWnIMyPKSLhfZphIsDZ5L9ktdl7qnb-EDpbWEf8bV6iHlubZ3hFsR4AQE3LMYWtdWF4qU8VPphhqw-sUcZCXoTU9XQKL_6IoGSHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/673b28107d.mp4?token=gLt4e-5Iu47-5v_5nfGdnZuME_vC5hxceXBj-F_1g5xPh-prCvf3RI70zb6H-JL0xq3DfaMDfVjQnZkrkAgqsorQZaMCR4Oa1Im96ewkabWJKOVc_5CZjy7OLlzuLo_loH2-6GB1a45ySOc_-7_FqDEanpJ4XXs1G8NHYE2qg0Kx-Z3IAkoQWW5D6Y6NUqsG9-QoXHcij28Ugeg2ivA9q2PQZoloo9sK6wYSNEPJBkspNTP1ZcXWnIMyPKSLhfZphIsDZ5L9ktdl7qnb-EDpbWEf8bV6iHlubZ3hFsR4AQE3LMYWtdWF4qU8VPphhqw-sUcZCXoTU9XQKL_6IoGSHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر گردشگری: هتل‌ها می‌توانند با عوارض صفر خودرو وارد کنند
🔹
دولت با این موضوع موافقت کرده؛ این خودروها پلاک گردشگری خواهند داشت و باعث تضمین امنیت برای گردشگران خواهند شد.
@Farsna</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/466504" target="_blank">📅 22:55 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466503">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CymCfw8DiT7OxJfq2lLydSsooNU19pnjv0xVkhd6_0q0JESoClDq8tAw7BbhO6oELm_MW_y3kk_hpp4u7usdoStT46lQVcTJjHfJYBVQenCed_Mx8F5UMZKVmZMBLPKEmeH5ZkIVa0VQVerzD3wXud5mySJz7a1I5I-Y26yWSZQx6DsTOwcgxpz3ewmfcjGLYLWNfyTV2Kr-OWjgkC6_K6Muiw9Q3hlozgb9tlfVSCn-08npwoquZY2hD25gEGQDi1X4bsyep4y0r-Cc3tSLiR3_NFQ1XfjKzdds3pF3OJCjRaXwottNl25DQvdKbxatHJERLw0SSUSkmrWv6KfQwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رد پای دلالان در گرانی گوشت
🔹
قیمت دام زنده کیلویی ۶۹۰ هزار تومان در میادین فروخته می شود که بنا بر عرف، گوشت مغازه‌ها باید ۲ برابر این رقم یعنی یک میلیون و ۳۸۰ هزار تومان باشد.
🔹
گزارش میدانی از فروشگاه زنجیره‌ای منطقهٔ ۶ تهران نشان می‌دهد قیمت گوشت گوسفندی از کیلویی یک‌میلیون و ۷۰۰ هزار تومان تا ۲ میلیون و ۱۰۰ هزار تومان بسته به درصد استخوان متغیر است و نسبت به ۲ هفتهٔ اخیر کاهش نداشته است.
🔹
یک تحقیق دانشگاهی که برای ۳ ماه فصل تابستان انجام شده بود نشان‌داد که قیمت گوشت متاثر از عوامل دلالی بعضاً  تا ۵۰ درصد افزایش پیدا می‌کند.
🔹
یک کارشناس ارشد علوم دامی می‌گوید غلبه درآمد دلال نسبت به تولید کننده،تولید کنندگان را در موضع ضعف قرار می‌دهد و تولید برای فصول بعدی کمتر می‌شود و چرخهٔ افزایش قیمت ادامه می‌یابد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farsna/466503" target="_blank">📅 22:41 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466502">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🎥
خانواده‌های لبنانی که خانه‌هایشان را از دست داده‌اند و هرکدام در یک کلاس درس زندگی می‌کنند  @Farsna</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/466502" target="_blank">📅 22:35 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466501">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd281cff39.mp4?token=Uo4LkTnD13EpDH_OAuHMB5t6bNDP3Uywy80sU2mZjnpCbiJMYrHOiNfhUuycRLELixdiJe3P8-YrHElz7K6yjQOqyppCmVkTgWzoJEqbmv384ngkuRWPnuqfVlRBQ2s43w5FhCEogciX57g6DuQyA9noafcc6qjyxF8K6raL4kQln-EOYiSsEEWQ5xPF5JQiGxtKH1dWKj4yShV_XgMuYaIQFwl1Dio_87CrFERFaUMpbNWqNm4eAaYpK1alDQsxCZvPYgHGkL_HGgyCNuT0VJ_nx6F3PIa8hNnhELTNmYYPSRuwPGKp81DUhC1Lv7Xm7_-Z96HhnjxicqqjW9R8ug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd281cff39.mp4?token=Uo4LkTnD13EpDH_OAuHMB5t6bNDP3Uywy80sU2mZjnpCbiJMYrHOiNfhUuycRLELixdiJe3P8-YrHElz7K6yjQOqyppCmVkTgWzoJEqbmv384ngkuRWPnuqfVlRBQ2s43w5FhCEogciX57g6DuQyA9noafcc6qjyxF8K6raL4kQln-EOYiSsEEWQ5xPF5JQiGxtKH1dWKj4yShV_XgMuYaIQFwl1Dio_87CrFERFaUMpbNWqNm4eAaYpK1alDQsxCZvPYgHGkL_HGgyCNuT0VJ_nx6F3PIa8hNnhELTNmYYPSRuwPGKp81DUhC1Lv7Xm7_-Z96HhnjxicqqjW9R8ug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عاقبت یک نفتکش در تنگۀ هرمز پس‌از تخلف از فرمان ایران
🔹
تصاویر جدیدی از برخورد با یک نفتکش متخلف در تنگه هرمز منتشر شده؛ این نفتکش به‌دلیل نقض مقررات و هشدارهای دریایی، متوقف شد.
🔹
ایران در ۷ روز گذشته ۱۳ نفتکش متخلف را هدف قرار داده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farsna/466501" target="_blank">📅 22:20 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466500">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">تیراندازی به سمت شهروندان در جکیگور راسکِ سیستان‌وبلوچستان
🔹
ساعتی پیش افراد مسلح در منطقه جکیگور راسک در استان سیستان‌وبلوچستان به سمت خودروی شهروندان تیراندازی کردند.
🔹
گزارش‌های اولیه از زخمی شدن چند شهروند در این حادثه حکایت دارد.
🔹
برخی منابع محلی این اقدام را یک حادثه تروریستی عنوان می‌کنند اما هنوز خبر رسمی از سوی منابع امنیتی دربارهٔ این حادثه مخابره نشده است.
📝
اخبار تکمیلی متعاقبا اعلام می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/466500" target="_blank">📅 22:15 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466499">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a1896f7e6.mp4?token=RFvdnVzMSdpOk45RXgna5hLwmnBbvwVuks8tpQ46eGnEgiHkTPFFt1jtKSzF0jAodV8V51xmvXn4NY_7-PmhQ0BFQFwdC1iA3wSIk0EwatO4uQau2g7EjuOpGOo21O20Odqg8LQfTIrczlA1X5kD4xPmoUIX5jC-qUEeJD7GVAGgcRlhMyF00X6iUN69kD79FYwG9KOBIj1K3EYkYOZR80qryyhPYbw2ZtRERsup8RXSeuYTUTl2fFwRpTlTqL_1xtDMjSg0lml4BYMM4D30SjSGGoqX8OWNF3dHjq3c4fy1zQBawRRFAxwClRVzTR9l3yhK5XdxcXK0lSAkAXzbhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a1896f7e6.mp4?token=RFvdnVzMSdpOk45RXgna5hLwmnBbvwVuks8tpQ46eGnEgiHkTPFFt1jtKSzF0jAodV8V51xmvXn4NY_7-PmhQ0BFQFwdC1iA3wSIk0EwatO4uQau2g7EjuOpGOo21O20Odqg8LQfTIrczlA1X5kD4xPmoUIX5jC-qUEeJD7GVAGgcRlhMyF00X6iUN69kD79FYwG9KOBIj1K3EYkYOZR80qryyhPYbw2ZtRERsup8RXSeuYTUTl2fFwRpTlTqL_1xtDMjSg0lml4BYMM4D30SjSGGoqX8OWNF3dHjq3c4fy1zQBawRRFAxwClRVzTR9l3yhK5XdxcXK0lSAkAXzbhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
۲۱۹ شب عشق به وطن در کرمان
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/466499" target="_blank">📅 22:11 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466498">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca4bc98f35.mp4?token=gxmaITBu10PyXYhewflNP_N18JsroCuEa05f7jhV3zvPfQLbqn-Da2L5nUMj7WpuICmlw_fX3WZOd6KrHiTf341U0Qat6v-Pq56vOXs24dtSTVL1jM-3U1ma6WUo147_b53EvpP6m3FtQNqrbYBvPKzQsjx5t3-ZM6QPprwyiwbjBMuI7BUd9OWGkL8WClOCjucfqS-VkB1CQfpat7BjcDcm2c2DdwmDgM4waN45Gi73QvefmOXHOKZHgyPqp_cGTsAfDXsGPsAJPN0ifDJUxoVFB2o7ljfnBZ3yQ6tKBptx5mOwYMOUVQYBC_9zw9IsY2Bnoux2KJ0ix2sNFl-cng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca4bc98f35.mp4?token=gxmaITBu10PyXYhewflNP_N18JsroCuEa05f7jhV3zvPfQLbqn-Da2L5nUMj7WpuICmlw_fX3WZOd6KrHiTf341U0Qat6v-Pq56vOXs24dtSTVL1jM-3U1ma6WUo147_b53EvpP6m3FtQNqrbYBvPKzQsjx5t3-ZM6QPprwyiwbjBMuI7BUd9OWGkL8WClOCjucfqS-VkB1CQfpat7BjcDcm2c2DdwmDgM4waN45Gi73QvefmOXHOKZHgyPqp_cGTsAfDXsGPsAJPN0ifDJUxoVFB2o7ljfnBZ3yQ6tKBptx5mOwYMOUVQYBC_9zw9IsY2Bnoux2KJ0ix2sNFl-cng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایتی از شیوهٔ زندگی مبارزان لبنانی تا اهدای چفیه متبرک رهبر انقلاب به فرزندان شهید حزب‌الله  @Farsna</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/466498" target="_blank">📅 22:05 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466497">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c64b0a1f0c.mp4?token=s11sy94gMPHRB6g5TxgoL1JmafqZfR3Xu0acyzPfxBbgheT56ZX4EXMprtu14w_KOSFuYP5B8tC101cWD-LASWJAr72sBpiZJPFMPJ5JGCJC9C9zpZx3r1_pROKDaA3T9uPkYY-zdskle_9lDBOuXk2nQ0zjgkMtHcaAdfQOrztx_5rUmF63AsPTUqR2KswJ8Emssr8_wnk7SIYnIlA5q2xPo4HIqimmnR_E_C7GAxFaeFyhe9EjplwRS-w81nH9AsbaHy0lhnSws5Km0YmChdjQqva0nKZfnZ5c5fJqGFOYUF_DY-yuFa8RF64MAHHJV5a4lDkbuCUsU3_UrX4pjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c64b0a1f0c.mp4?token=s11sy94gMPHRB6g5TxgoL1JmafqZfR3Xu0acyzPfxBbgheT56ZX4EXMprtu14w_KOSFuYP5B8tC101cWD-LASWJAr72sBpiZJPFMPJ5JGCJC9C9zpZx3r1_pROKDaA3T9uPkYY-zdskle_9lDBOuXk2nQ0zjgkMtHcaAdfQOrztx_5rUmF63AsPTUqR2KswJ8Emssr8_wnk7SIYnIlA5q2xPo4HIqimmnR_E_C7GAxFaeFyhe9EjplwRS-w81nH9AsbaHy0lhnSws5Km0YmChdjQqva0nKZfnZ5c5fJqGFOYUF_DY-yuFa8RF64MAHHJV5a4lDkbuCUsU3_UrX4pjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تقدیر مردم شهرکرد از حافظان امنیت در شب ۲۱۹
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/466497" target="_blank">📅 21:51 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466496">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hhoO67ZKEYY-wesTBTh6NqoOUsisLh_LksjbFzA1WiYHNOxMby-YKxjAAm19hXNWR3rbSGoQN4LqVBWIDMZgQn6bcSDqJ_Z53GgfWk9PwA7iXGDE10O-RdFr3bF_cFRKqndoxKlwz8pjkp9WBhDntomqqswubpi_pjNm0doMyoS9uD4KcfcAcuycnAy-mZeYhoZUy-JKXVNvvC7w0lC9kcNBRYyFWlcx1NdLNDesvcwAHq6fW6tuTAQ2h1rptAxjeC967mIdPBExn5vEY3x0UW0nJS8NENaLX8KDjjChDnONsDzf0D-kTpicxZp2gskOpbi6tLIz8kiR_9ZHYczCmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">افشای طرح محرمانه عربستان برای حمله به کعبه با پهپاد آمریکایی
🔹
منابع منطقه‌ای از طرحی توسط تیم امنیتی سلطنتی عربستان سعودی برای پرتاب دسته‌ای از پهپادهای لوکاس ساخت آمریکا به سمت مکه و هدف قرار دادن کعبه مقدس و تعدادی از مناطق مسکونی اطراف آن پرده برداشتند.
🔸
بر اساس اطلاعات موجود، این طرح ممکن است به اقدام پوچ آتش زدن دیوارهای کعبه مقدس و ریختن خون در مسجد الحرام در مکه و همچنین هدف قرار دادن چندین هتل در نزدیکی مسجد الحرام، از جمله هتل انجم مکه و هتل پولمن زمزم مکه، گسترش یابد.
🔹
علاوه بر این، عملیات تروریستی و قتل عام ممکن است در مناطق المسفله، الغزه، الشبیکه و جبل الکعبه رخ دهد.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/466496" target="_blank">📅 21:50 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466495">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oOTrYGXcSi1rT6u71Cq1Q4XWGvCaI9sRrws9DTjH1qJ0GYRXIpBtzoDLgwc0P2M9ZpHFHcqHvGsp2lyZe7AdypFAZRBgQViK7LD7DII_aN-QyK7nBW6uS6ze7b7BYpyK_GFIycRtjz6QhNsDJkhLBMkyNpwlzbnihkXN6SN_npfiJfsl3PXNqOw2nIII7r3RjVZXxlO6zAFQkRmKQenpbL0lHyPHmRsj_ci5HuF8yAzHiBcwft4gwmGk4Mt368KbTlUKJNcp7JyyX6i-VD__AhHoQWT0yicwfl7dx95rSmKOYgSI5cFjjINk4HF91CnDd4ZyOa1H5umMSzrURW9E8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۳ سوال کوچک‌زاده از همتی دربارۀ دلار کارت ملی
🔹
مهدی کوچک‌زاده نماینده مجلس در گفت‌وگو با فارس: آقای همتی باید درخصوص فروش ۱۰ هزار دلار با کارت ملی به سوالات کارشناسی نمایندگان مجلس و کارشناسان مخالف این سیاست پاسخ دهد.
🔹
اولین سوال از رئیس ‌بانک‌مرکزی این…</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/466495" target="_blank">📅 21:32 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466494">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">بسته خط ۱۴۳.pdf</div>
  <div class="tg-doc-extra">3.9 MB</div>
</div>
<a href="https://t.me/farsna/466494" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">بسته خط ۱۴۲.pdf</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/466494" target="_blank">📅 21:32 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466493">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Scllskb9XVo_llxfJbOPeapS4ejrIX0nBu4BWZrGzke51_Tx8tTgOC0BH0KFZNrANv0swecT9Iej5Q7kwpYS84K0LRX45iKR0peGy53Pdl8_AUe2alTIt2h_rYbFM84vkbxH-rFqkj5E7WskFbflrJ5TJ3XWdP_I4SluWg6VNTFTe3UyTUk4xzkROWDLZ9jztufSaP23EM7tRScVFlzXiPRihTVCcBPs5HFSanXdCsGY8019-6f7e8jRDgdRDft4PcfBVjjQI308VGLF_wmMNsIo5OwacFVRR7Lei-PAFZcOOc9tg-HvgPAiJBjEdMwAPhPdjIzmgYuxc-HArbPskg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
معاون ترامپ: ایرانی‌ها عامل گرانی سوخت در آمریکا هستند
🔹
ونس: «چون ایرانی‌ها درحال ایجاد ارعاب و تهدید در کشتیرانی هستند، قیمت انرژی بالا رفته است. ما هر کاری که از دستمان برمی‌آید انجام می‌دهیم تا روند این قیمت‌ها را نزولی کنیم و کمی از فشار روی مردم آمریکا…</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/466493" target="_blank">📅 21:15 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466492">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/36fc19948f.mp4?token=KNEAFjZavv7J1aQnwnlWqSDITpM23_3MM9RSS3JMncQ8l25aO-zA6KRBD9GdK5PRgSGrfp65K_gHa3-3RZLJt-kZt5dW5vBq1BPQCzSZq4Ix0bsObweBRBrnou-u2Urw7uZq5j9z2ChkHZopPxFcnz1ZGOZYL81Gel4O1AzRimC0nJYqiOWoD0ylLVHxskQ8BghR3EWpVBylP9rOMzm-6bwubaYT_zSuSGGVDHwbDStt285aWr8vm_cIHcGlrim0LO0KZy7WPn3UGV6VSc4Q5Ddj4UjJnYRgzmmhgeq0A5Vi2_ob2NbXzA72otifT9wfsvXv6Jgyo68_8-OOVweo8DzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/36fc19948f.mp4?token=KNEAFjZavv7J1aQnwnlWqSDITpM23_3MM9RSS3JMncQ8l25aO-zA6KRBD9GdK5PRgSGrfp65K_gHa3-3RZLJt-kZt5dW5vBq1BPQCzSZq4Ix0bsObweBRBrnou-u2Urw7uZq5j9z2ChkHZopPxFcnz1ZGOZYL81Gel4O1AzRimC0nJYqiOWoD0ylLVHxskQ8BghR3EWpVBylP9rOMzm-6bwubaYT_zSuSGGVDHwbDStt285aWr8vm_cIHcGlrim0LO0KZy7WPn3UGV6VSc4Q5Ddj4UjJnYRgzmmhgeq0A5Vi2_ob2NbXzA72otifT9wfsvXv6Jgyo68_8-OOVweo8DzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وقتی ترامپ به روایت ربات‌های فضای مجازی دل می‌بندد
@Farsna</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/466492" target="_blank">📅 21:03 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466491">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lgv9DC1ft_G1NHbmPC5kyPskHIT58mdA44iJuYBX1DKbEnkmtYZko3ozOgp1LbEvRf7vuCO4sIDEH23VGvPpTGRcn257FxbrXJvuqzfkjGf1tuxXQ9CH7v7RmnT-SvvDPbjdtY0PWf8qvFgMqMrqcVGdETtRj42WfWPDYRsYJeVaNa-xPnIZmvjWWE1vDqdZB_veg0iaXG2SKo82TuYJVse_5grjFy3NtbjFHldLx8h6sIX2XIMRhbkiRWt6cxfDdtqM2TWRMadbCVFLU4xi-7bbuHfYi6XD8jzCkokxd5_S7KAyfmEn4YJ-kY1FR_4iUcFD_eHaW_sv9H70YU0v5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
عضو دفتر سیاسی انصارالله: در حومۀ باب‌المندب فقط نیروهای مسلح یمن حضور دارند
🔹
نیروهای وابسته به سعودی صبح امروز تلاش کردند در استان لحج پیشروی کنند اما با «طوفانِ قدرتِ سهمگینِ یمن» درهم‌پیچیده شدند.
@Farsna</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/466491" target="_blank">📅 20:56 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466490">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/edec37e973.mp4?token=F2B50kGKP_YpTvLKBkwRNYpA02yjIg8CtH2HF3SDwuNkVvP8HXtQWCEsJ9eZC2BkRVimt2Mg9NCg-K78kEivm7E83TWHZ2DN8HTVMPwqb-thgx-6sMuvIDGS9yc1s_pFNGqXahBe3W7m2cjUICpSWqlLXR2mlegOv_2rXe_SbvIAVOARb_rtleuPtrI2A-TF3A9mm9Pt2lxluzFfSWwnU_YtxjYtWMdVF1YUYDrthOoQsX8LGuQyhaP8m-MtSHbciCqNO3P_mjkDkzH9WF5Fff9Jkk3BwKEzBR-Ul4cDA08it3hAzFQbx2igX7Ku4XMcBRFa7e-UNjJfjGg153IjaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/edec37e973.mp4?token=F2B50kGKP_YpTvLKBkwRNYpA02yjIg8CtH2HF3SDwuNkVvP8HXtQWCEsJ9eZC2BkRVimt2Mg9NCg-K78kEivm7E83TWHZ2DN8HTVMPwqb-thgx-6sMuvIDGS9yc1s_pFNGqXahBe3W7m2cjUICpSWqlLXR2mlegOv_2rXe_SbvIAVOARb_rtleuPtrI2A-TF3A9mm9Pt2lxluzFfSWwnU_YtxjYtWMdVF1YUYDrthOoQsX8LGuQyhaP8m-MtSHbciCqNO3P_mjkDkzH9WF5Fff9Jkk3BwKEzBR-Ul4cDA08it3hAzFQbx2igX7Ku4XMcBRFa7e-UNjJfjGg153IjaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
طرح جدید کارت سوخت، مردم را پشت جایگاه‌ها سردرگم کرد
@Farsna</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/466490" target="_blank">📅 20:54 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466489">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61b1a1df1b.mp4?token=Or0t9rHPIAjXdUzNOQ6hMu0BOJJ7Yhf8bn_7diNEmK7PhEDNObS4GS7AyQbV-xvSeppfGI3A-nURh-lAL0UJcAjborrRmm71ZijC_as5tvlXLhCxpnZXSXZJmfwH5_NHZzONZzq1Ymwv5riElTNUZui4wRTpjCwJ_BOhYHhsAN6q4znLdGgKgAlAo_7yzpVXqjmYv3_OF3jO45KgO2agnEW-xmeVOWYdzcXZZl1x6EOZBng8POwEoyeVHcROH2nq6cbZEU_Jfvd6C7AlyN4MWEpol6IQmkzSpnKF_xbMG1Hvj0Av-faOIpMUYgWpUYK3jAGvxGCMaY9KaNl-o8534A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61b1a1df1b.mp4?token=Or0t9rHPIAjXdUzNOQ6hMu0BOJJ7Yhf8bn_7diNEmK7PhEDNObS4GS7AyQbV-xvSeppfGI3A-nURh-lAL0UJcAjborrRmm71ZijC_as5tvlXLhCxpnZXSXZJmfwH5_NHZzONZzq1Ymwv5riElTNUZui4wRTpjCwJ_BOhYHhsAN6q4znLdGgKgAlAo_7yzpVXqjmYv3_OF3jO45KgO2agnEW-xmeVOWYdzcXZZl1x6EOZBng8POwEoyeVHcROH2nq6cbZEU_Jfvd6C7AlyN4MWEpol6IQmkzSpnKF_xbMG1Hvj0Av-faOIpMUYgWpUYK3jAGvxGCMaY9KaNl-o8534A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۲ نفر از عوامل اصلی جنایت منجر به شهادت مظلومانه ۴ مأمور پلیس در اصفهان اعدام شدند
🔹
علیرضا سپاهی و علیرضا رئیسی ۲ تن از عناصر جنایت اصفهان که اقدامات فجیع و وحشیانه آن‌ها منجر به شهادت مظلومانه ۴ نیروی فراجا شد، پس از رسیدگی به پرونده و تأیید حکم در دیوان…</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/466489" target="_blank">📅 20:51 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466488">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">‌
🔴
منابع رسانه‌ای از شنیده‌شدن صدای انفجارهایی در پایتخت عربستان و توقف پروازها در فرودگاه ریاض خبر می‌دهند. @Farsna</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/466488" target="_blank">📅 20:49 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466486">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">‌
🔴
پزشکیان: هربار بازرسان آژانس به ایران آمده‌اند، مراکز هسته‌ای و دانشمندان ما شناسایی و پس از آن این مراکز بمباران و دانشمندان ما ترور شده‌اند. @Farsna</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/466486" target="_blank">📅 20:42 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466485">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">‌ ‌
🔴
پزشکیان: حملۀ آمریکا به ایران با هدف سرنگونی نظام، موجب انسجام بیشتر ملت ما شد و به امید خدا از این برهه نیز با سربلندی عبور خواهیم کرد. @Farsna</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/466485" target="_blank">📅 20:39 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466484">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">‌
🔴
پزشکیان: فشارها را خنثی می‌کنیم
🔹
مردم ما استوار ایستاده‌اند. همسایگان بسیار خوبی داریم، ارتباطات خود را تقویت خواهیم کرد و فشارها را نیز خنثی می‌کنیم. @Farsna</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/466484" target="_blank">📅 20:37 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466483">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">‌
🔴
پزشکیان:  آمریکایی‌ها تاکنون ۳ بار پس از گفت‌وگو به ما حمله کرده‌اند و این نشان می‌دهد که آن‌ها دنبال گفت‌وگو نیستند، بلکه هدفشان ساقط‌کردن نظام جمهوری اسلامی ایران است. @Farsna</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/466483" target="_blank">📅 20:36 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466482">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">‌
🔴
پزشکیان: با دشمنی که هر روز ترور، تحریم، فشار و تهدید می‌کند و پیمان‌شکن است، مذاکره معنا ندارد و ملت ما نیز چنین رویکردی را نمی‌پذیرد. @Farsna</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/466482" target="_blank">📅 20:35 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466481">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">‌
🔴
پزشکیان: مشکل ما با آمریکا این است که هر بار به میز مذاکره می‌آییم، بلافاصله جنگ به ما تحمیل می‌شود.   @Farsna</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/466481" target="_blank">📅 20:35 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466480">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">📷
وزیر خارجۀ ارمنستان با پزشکیان هم دیدار کرد  @Farsna</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/466480" target="_blank">📅 20:34 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466479">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W99xReirGv2twbiNlADocES19enBZ7sdBIIb_1lz3bHE_6Lnl1xu0MT5jvDyGQedSIOW-BkwzU220QUo2-i6ARtd2SfMAZH9OJtvkmFf_54GWRlTfJZWgM9D_-wenvpIq6NBVhIQezfL7MybE2xkGnKnVHnPKL3UDUvvFq0p0R8PNI0qsMcE6Dp4nJHC4fMGDmZ74L3mmDShCu7zuuTXVwP_DEDmzNFv2wuLtjGIG6SI-Csdl7q5WwT16qeSbX-6CaOwRSU0jVYjHmaqiOqA-bfo8UuFPBhBVPhsqcVLmWtKPvdfGmizkgfYw7YOtXOYLi_nGgeRLEBY5Gh74lPPuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
وزیر خارجۀ ارمنستان با قالیباف دیدار کرد  @Farsna</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/466479" target="_blank">📅 20:34 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466478">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZWIGfb7xea2LRp2NMXY9bi4eIRHJvA1PUZpy-gVbj6EGiSxwusLYMh3G6TG9Kaf-0l7OxqJs3_15Uq5kLkHOYxl7ZPk_0yCu_saF0Unr6mnFOnoRrWYE93iRRMG0PXhpgWvoL0OICJM-ZE6GGawESpBBSURqcnNvFMOLONq9SjGdv29BT3YUpHVSMP4IjzocY0ahoJtvBXVLF7Y-Y6VzeJGPHenCh9YYu-y0bj0STjSDh6N9-47eZKKfDQ-MciXk6R-mmoyf1cOMImIQKgL57n6rJqDRhm8hMYMw3CieBBq9Wt-eqNc4wvdzVmPGFPdm5E5j2Yyb9O8mpmSqpxo1Iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طارمی ۸ زندانی نیازمند را آزاد کرد
🔹
مهدی طارمی، کاپیتان تیم ملی با مشارکت در طرحی خیرخواهانه، زمینه آزادی ۸ زندانی نیازمند استان تهران را فراهم کرد.
@Farsna</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/466478" target="_blank">📅 20:26 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466477">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">‌
🔴
یمن آسمان عربستان را منطقهٔ پرواز ممنوع اعلام کرد
🔹
مرکز هماهنگی عملیات بشردوستانه یمن در صنعاء به شرکت‌های هواپیمایی هشدار داد که حریم هوایی عربستان به‌جز مکه و مدینه «ناامن» است و صحنه عملیات نیروهای مسلح یمن خواهد بود.
🔸
صنعا اعلام کرده پس از این هشدار…</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/466477" target="_blank">📅 20:24 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466476">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/033bb92fbc.mp4?token=PCk_xgI7d1xaJE0449efWnqarMYy9oDahfdD3N8vwMdFGDQMSUv9aRHwLzJFhQR8m2flT-QSkP7n8LbIFwC26D2gzgAHwmNrqhdUU3PJjdshgA1JzGAaPPK1Iw3uMFsxYRKdwm4zeoA2t8GRRsenC4t-QUrVb5fwNlGOp9xmIMq9pMUjIwjkK8bCYcR7LyO63MOvCRzy74DOUPlnFqVB37jRkrHNiSnmy-z8hHtx3XOZ5vwjHa5lg5olAiLSFZMXT7BXRafpBNYkhqWUtTtJQvnM_N4b4ELDh315AkYWJk4llwN9r0Y1at3f1n-DYpypXUZghMPSY1Vmo0U4kxq-qw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/033bb92fbc.mp4?token=PCk_xgI7d1xaJE0449efWnqarMYy9oDahfdD3N8vwMdFGDQMSUv9aRHwLzJFhQR8m2flT-QSkP7n8LbIFwC26D2gzgAHwmNrqhdUU3PJjdshgA1JzGAaPPK1Iw3uMFsxYRKdwm4zeoA2t8GRRsenC4t-QUrVb5fwNlGOp9xmIMq9pMUjIwjkK8bCYcR7LyO63MOvCRzy74DOUPlnFqVB37jRkrHNiSnmy-z8hHtx3XOZ5vwjHa5lg5olAiLSFZMXT7BXRafpBNYkhqWUtTtJQvnM_N4b4ELDh315AkYWJk4llwN9r0Y1at3f1n-DYpypXUZghMPSY1Vmo0U4kxq-qw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ناراحتی اینترنشنال از شادی ایرانی‌ها
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/466476" target="_blank">📅 20:07 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466475">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">هشدار لندن به اسرائیل
🔹
یدیعوت آحارونوت: سفیر انگلیس به مقامات اسرائیلی اطلاع داد که لندن در صورت عقب‌نشینی نکردن اسرائیل از بستن کنسولگری انگلیس در قدس، ۲۷ دیپلمات اسرائیلی را اخراج خواهد کرد.
@Farsna</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/466475" target="_blank">📅 20:00 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466474">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q0u3oPP9tY9igjfofWGA7N9w2f0EUXL3NYQppy-c5ceZwXsBEQFYBi8qBv1Kg9CrB1WLMz9Urc7uW76q2VZDyQJVAZxmHHTl80P-x7LyW1l6sm03YK6LcEPcDUFjfcsGONUH2RPo0Em6MB7uyRUWXXIoV4I2c24YNxEOEHQ1MBdmnLBwGLQZv2fQXvsrtq-yE5_pgE0Io5yAMlUku21ffUhU_C66expnWl1RupT4bSnhE8I-5L2hVNRxtEl6ns3_d-hljvhUs9XVed-Sp1nX7YbMLweeUvueUM338DfvqZaoOhyzmkxD8HYcg3CA75mYUhNGq6B0F_WWe_WP551jgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر کشور وارد دوحه شد
🔹
این سفر به دعوت رسمی خلیفه بن حمد بن خلیفه آل ثانی وزیر کشور قطر انجام شده است، وزیر کشور در این سفر با همتای خود و برخی از مقامات قطری دربارهٔ مناسبات دوجانبه دیدار و گفتگو می‌کند.
@Farsna</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/466474" target="_blank">📅 19:53 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466473">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0094da11e.mp4?token=mx8Tw0YBVhIuc_gI4o5NJbZizUxHXJCRtxlSqTEomb11Nn4sIfCrH0ieJmnANHBpcboQ_vaGZ6uAS-r7rrAxrJd8rtNaJoxH9OSnl8GgkC4E_v6wImjY-PWyj9HdvEhkxQOJbqpGGou3POEckdUAlUaIFOekuQloNLgshB92QFxijDyHnVv7GFlU8GTjnbjkCYIDgF3P7vcLOndetQVqrTrf23dWAok_2q6etVAhm7Walxq0Y8a8b77PzpRYVhfAUa29fFcmuGceG8anKlCf_CEdrU2E5zPLjVNpgbsBi3ninYyga9-WE9YxMgFOKTy_YgG6D2gx_lddoaAIjnyo-IWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0094da11e.mp4?token=mx8Tw0YBVhIuc_gI4o5NJbZizUxHXJCRtxlSqTEomb11Nn4sIfCrH0ieJmnANHBpcboQ_vaGZ6uAS-r7rrAxrJd8rtNaJoxH9OSnl8GgkC4E_v6wImjY-PWyj9HdvEhkxQOJbqpGGou3POEckdUAlUaIFOekuQloNLgshB92QFxijDyHnVv7GFlU8GTjnbjkCYIDgF3P7vcLOndetQVqrTrf23dWAok_2q6etVAhm7Walxq0Y8a8b77PzpRYVhfAUa29fFcmuGceG8anKlCf_CEdrU2E5zPLjVNpgbsBi3ninYyga9-WE9YxMgFOKTy_YgG6D2gx_lddoaAIjnyo-IWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مدیرعامل اسبق بورس: عرضهٔ ۱۰ هزار دلار به مردم کار بسیار اشتباهی است
🔹
رحمانی مدیرعامل اسبق بورس: نباید خزانه ارزی را خالی کنیم، الان کلی دارایی ارزی در بانک مرکزی است که می‌تواند تبدیل به حساب‌های سپرده ارزی شود و از طریق صندوق های ارزی یا از طریق صندوق های ریالی عرضه شود و هر واحد صندوق برابر یک یورو یا دلار باشد و قدرت بانک مرکزی هم بالا است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/466473" target="_blank">📅 19:51 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466471">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاخبار چهارمحال و بختیاری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RiEfnR7_cDB2_dVVUdbWb6uqzRmoqWX59qd4SUU_gc3KS0x1EXTSFion2Lmx8FIBZcu1DB6WCMl7dw8MuSYc3hxMwtUkM7C0wQ-iWXCt28GWBtD9Z4MBhri_EIYcka6iNgYyF-rDxjK7SiAIlbFAye16sdNkJ-jvIhoDdG9EX4E5vwNgjXfJbHte8SJpMj2KKC-ztaJYL_k8gaHoJ5qvToZrHbTLw_dZbK9Bado3I5Uob8fFKa-KDq0Fgt0Ab2HUqzn6BY5g0XS8dEL9JtDHKKl8ec07nutBLWyDzj2x8oB8tY0uUEuIggSCGa6Qf-_Xw8W7T9spgZIUy9M4I08ZGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رتبه ۱۲ کنکور: شهادت رهبر مرا از درس دور کرد، خون‌خواهیش برگرداندم
🔹
گاهی یک داغ فقط دل آدم را نمی‌شکند؛ مسیر زندگی‌اش را هم برای مدتی از ریل خارج می‌کند. رضا سعیدی ابواسحاق، دانش‌آموز روستایی چهارمحال‌ و بختیاری، بعد از شهادت رهبر شهید آن‌قدر از نظر روحی درگیر شد که از درس فاصله گرفت؛ اما یادآوری توصیه‌های آقای شهید درباره درس خواندن جوانان و ساختن آینده کشور، دوباره رضا را پای کتاب نشاند؛ همان پسری که حالا نامش با رتبه ۱۲ کنکور گره خورده است.
🔹
حالا رضا سعیدی ابواسحاق، دانش‌آموز بسیجی روستای ابواسحاق، در جمع برترین‌های کنکور ایستاده است؛ جوانی که می‌گوید امکانات آموزشی روستا با بسیاری از دانش‌آموزان دیگر قابل مقایسه نبود، اما تصمیم گرفته بود خودش را «محروم» نبیند و کمبودها را با تلاش، کمک معلم‌ها، حمایت خانواده و استمرار جبران کند.
🔹
او می‌خواهد مسیر علمی و پژوهشی خود را ادامه دهد و در آینده بتواند سهمی هرچند کوچک در پیشرفت کشور داشته باشد.
گزارش کامل را
اینجا
بخوانید
@Fars_Chb</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/466471" target="_blank">📅 19:18 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466470">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y6Pqkzg0pgh1hs5jZRdBYUgOs4fyYRWKVfaDj_drQMwVKohmuF_we2XIvxrRRtN9NsVK6NgKvi0pVLrpEo5BInKdCPlAVgTe2FzGiNRt0t-qa804lmEnICKt7FpJdHS8ari5C29UPWsjqba4ZwEcp_twi6rEya4824dkMlu6n5rwaF9oL-_Yb84Ak8ieL4L6tkB6RdhKB5qDHZ70rnCGdicDo-0Ac1CSRhCQ1jplGpTmjPQxHq5ajl_PBxWWT4ANTfmI_gZLixxB--2QxQnMomi4LK0LNBmgqW_9ml_HMl3lK0I6GTLjzzX-H8I3P6FN0emBoPrKcKPbuA-1qH-4Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قالیباف: قفقاز نباید به محل رقابت ژئوپلتیکی قدرت‌های خارجی تبدیل شود
🔹
رئیس مجلس در دیدار با وزیر خارجۀ ارمنستان: امیدوارم به زودی معاهده همکاری راهبردی میان جمهوری اسلامی ایران و ارمنستان نهایی شود.
🔹
قفقاز نیازمند آرامش است و این امر باید با تحکیم مرزهای…</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/466470" target="_blank">📅 19:15 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466469">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LCy_hJqPDsVbefBSqhC2Ca06Eqk8cGdM9d0C1_7MfjcCyf8AwCm4-xpRZ9AqrpXgtGD7QNsxl1kYum2SCRcGOdCZPdNFk3Zc2Ljpjh4ziJD-CLHaRRZjubBQl83SQQkDvrbGEe-2WYzkRPJHF0dkUNUxIKVttaa86CcX28zK1k-lHCBJbCAnGt4KoY38A1MqM-OP4HjvNiB3MQuK-RvHC8HG-WFtaBM-CjzGi2vnO0Gw-4b9TbUbd3VkNPTGgWYn0fC3tADzUl7SntIMrfICoiiMIsX0wzReoryjWQJ6jZRwO4MsxJqV6zBnK57hjzQ9bsVwHnJvPFtvI36kesWpQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
وزیر خارجۀ ارمنستان با قالیباف دیدار کرد  @Farsna</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/466469" target="_blank">📅 19:13 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466466">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vL7a7cQ3ci3KcposzaYievMkjFUjO3wkV1E7fxIKkDEgxR6aaXJDex8he2ojZ7MccO-YeOXbwUAHMD29z42X_RLwCylkx2Q2QnNVvHSI3HsXTpaUV6UbbK9yY3KHfK0BDcw5eITyAu7BeH-q3oodMMF56JfXWzdZYmwAlbwbTqH8pzDA30BTbE0aHChBTgcVXEhyijffPjdZ3ODUnrV9-mTM34IWXh03WTNK9TllhOBS8KHqr99K9FndN9rpubv6GXlE2zrwF0K13gpGZlHJC2bii5h3BZ3bgxtxQQFs84kL9NWNDsde_Y-YLzjD5j9lalabG49muAZ3Skby3xscdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vxGHtTqp_pjV7wolQYos_E3ZpiUmCw3pLBfqj3mBiljMgUbKxO6ahVT0uCMaEcD_mNXUuuEvMieXW21lGYCUcIaupWnityRO0vRMsC5nsZ3qnWvvLChdFXhpEv6sE5-4iJpYpkQgTOP32hrJ78LTrz_ojeumUBbNiD10zHevWL1RwouNR6U6aVrer3FvKF43ciN7tgINfw4bXX3aPEZCcocDyDNPSdNm_UvT7q0gMq2Cg4L9jUM9rIzqTX6V6I9U6BwCboqO9IVPa6pspYROaljMvx_G6FkNqQtdWShFpK1p_i_YVFkSKw7-L5-vrruH60YPx0mKGsWSUvtCkoqTTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sBbxHZOhT08ldJi_6iaairdt9WIFGMrwjd2jz91M2bkwIkU_lL9_4YB9UtbHYYNvXu4tb2dbSZ2jTttcDxbBOtSekW1BlWdmFyM7AGoOXRxrhLTXcB0Hjtg6vEarpNachv6HPsik9orVx7REO-r27fkSqFS9glM9yx4IEHCUroyh103ckvxLx01tOCp1OPWU56_v0i963m_6nB57E2nA28jb4UozgjzPhWITZfoExPcdiUdK4M0XwzTZGKfyqGAziuaGnu1vO81cYaWrYwHZS9XzmAF6HCx8yxwzIevs9GT1WKT6AwA5ZAtXybWXH6HikA8t2n_46zJmpQRCyq3LKA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
وزیر خارجۀ ارمنستان با قالیباف دیدار کرد
@Farsna</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/466466" target="_blank">📅 19:06 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466465">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5885c04db.mp4?token=upBcWRRnGJ2gh2YKXtqrjX13MuTGZ6lUGyWi6eFb3O8WNCE-FQFWw5ADg5T6lc50YCnrI7D0w2rv3wWzZF-6LuTipLeexLdcciUN1PMDfpfNlhXwmgIlFufxbaApAW4ovqH9fWCsuOiXatgEyLD1qXVW_xzJoyNw_vtpAdQuvyKWUK81TDJztvT21CjVv6rVxAVeU05td5UdL8gP-3TiprCY8t0QzSphWx7TdGPHbwnTnabGE4Rc1dXZT0BZy3WtVSZwO8xupNei2BNl87cG7_OBS_lkmPFKL5xDI19z8WZHbkmiU0cIReUQ0ED4093Ga8-qkHPkxyDNkljvFuKTU3051Ha2jRHr0_awm0nQrxz-zSmG8XyIbBO3IjTnK01iz_AqdVG6RGZiarym6IBoe8XEl2voBQGPbSjJK7qDh9NnTzjqgJ8AEN66gKIiB1i_atis8tH7bML5Eh4nIAnJ3nYi5Y3RhebUUMuIbz7k3I558pNjHSh72ZvoneIb6OEfybAh9ZkXMRVISpEr1lpoZBE3qiWd3jxBoiblyEyVd4EksrqxsGImo_I_Z_IfZZsEB-vU4vl7yMupODWMSG9MUl47GvFyg0yAH13HeVFT9dEe_qXFcPdjboXyaj0C2PpIFlLFySZrvNaAap5RI04uiGxlJDY1fL6tL0jbKAp9mW0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5885c04db.mp4?token=upBcWRRnGJ2gh2YKXtqrjX13MuTGZ6lUGyWi6eFb3O8WNCE-FQFWw5ADg5T6lc50YCnrI7D0w2rv3wWzZF-6LuTipLeexLdcciUN1PMDfpfNlhXwmgIlFufxbaApAW4ovqH9fWCsuOiXatgEyLD1qXVW_xzJoyNw_vtpAdQuvyKWUK81TDJztvT21CjVv6rVxAVeU05td5UdL8gP-3TiprCY8t0QzSphWx7TdGPHbwnTnabGE4Rc1dXZT0BZy3WtVSZwO8xupNei2BNl87cG7_OBS_lkmPFKL5xDI19z8WZHbkmiU0cIReUQ0ED4093Ga8-qkHPkxyDNkljvFuKTU3051Ha2jRHr0_awm0nQrxz-zSmG8XyIbBO3IjTnK01iz_AqdVG6RGZiarym6IBoe8XEl2voBQGPbSjJK7qDh9NnTzjqgJ8AEN66gKIiB1i_atis8tH7bML5Eh4nIAnJ3nYi5Y3RhebUUMuIbz7k3I558pNjHSh72ZvoneIb6OEfybAh9ZkXMRVISpEr1lpoZBE3qiWd3jxBoiblyEyVd4EksrqxsGImo_I_Z_IfZZsEB-vU4vl7yMupODWMSG9MUl47GvFyg0yAH13HeVFT9dEe_qXFcPdjboXyaj0C2PpIFlLFySZrvNaAap5RI04uiGxlJDY1fL6tL0jbKAp9mW0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایتی از شیوهٔ زندگی مبارزان لبنانی تا اهدای چفیه متبرک رهبر انقلاب به فرزندان شهید حزب‌الله
@Farsna</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/466465" target="_blank">📅 18:57 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466464">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">‌  علیرضا سپاهی در روز حادثه بنزین روی مأمور ریخت و او را درحالی که زنده بود سوزاند
🔹
با توجه به اظهارات متهمان دستگیرشده، تصاویر مشرف به محل و اظهارات مطلعین، جنایتکاران در طول مدت این سه ساعت مشغول هتک حرمت و رقص و پایکوبی بر بالای پیکر مطهر شهدا بوده‌اند.…</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/466464" target="_blank">📅 18:54 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466463">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VEQHBo7h1nAIWXzlVpyLwaMftmfQqLNsav61E7DObU4J_VxmDiaGrP8kA6e2mQdpLZm_k7p3DJwgsP6AgGYGdElH4j78_tyGfZK4Zq3Nnh8htR6pBa1dz3RkoQTv5osdOMGRTCeQP3jmFgAnm2ioRQEEHuIfMT38JGA55xqC-NWQXQ-JEJ5PcRXhmsdS3rgns8uLG4paXKlSmRHlYHCbtFW1LlA9CfeYIimTMlVrNMIpxQRGABTw7D7qxASYISg9gO59m8n2SWzoOpDBoNbP4iEUB0dPFd-bhZ4UmvmFrPNvJD-ffLavohbH4IeiV2PN6qWzo7kysI4UUxuKqQxIbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دانشگاه علوم پزشکی بقیةالله(عج) از میان داوطلبان خانم و آقا دانشجو می‌پذیرد
🔹
پذیرش همراه با بورسیه و استخدام رسمی است.
🔗
شرایط و جزئیات:
وب‌سایت دانشگاه
@Farsna</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/466463" target="_blank">📅 18:50 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466462">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r-_XJ79I2jretP3peR3-J6sZCCLwkLaXqGunOHXgNX5iqDrkeWNiW4JrdDZ_7YshG7tIyawb9TCo9Woj6O3nx5QIBamB5zOvDstC5hqrdBkDESABAH2OW9pJIw2ycWrrvQeQRFnpQQXDu17XiOd51PgCz5E6RLpSNFVYItjaLVf5LXD-qN9VEzZEUj749W9RuEyTvZ4CdUcyC5CSgvjdxCLJ6Pn9jBLWrQYnMu8a0eH77QEOeSCtM_64TialeL2gmLcHS4qFBWtIJ2esXY9qReuKoP0inQJFCK3zdYeVhYGY4exfpLlqfiLjWnSYZwoOlcw0B4PJfViarEJNFFbuPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بدرقهٔ کاروان ایران برای بازی‌های پاراآسیایی ۲۰۲۶؛ محمد معتمدی در میدان انقلاب می‌خواند
🔹
مراسم بدرقه کاروان ورزشی ایران برای حضور در بازی‌های پاراآسیایی آیچی-ناگویا ۲۰۲۶، امشب، ساعت ۲۰ در میدان انقلاب برگزار می‌شود. این مراسم با اجرای محمد معتمدی همراه خواهد بود.
@Farsna</div>
<div class="tg-footer">👁️ 9.88K · <a href="https://t.me/farsna/466462" target="_blank">📅 18:48 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466461">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lth64xnLtDkR1Xubc4M2TPI8Qs6FrMjngSk9WbWQ-Cx0nxS2vWxCdh_QkGQuQbxAnnK8oVYL5ifSj4sJIGTXuylEJQeSWpn7j-4u8xwTwTs2vlr8_6M9IMUJjOsatwQaSBQ36qt6Rxq8VPOLqQ5JToxpHGXp3bxbCwIhzwMrpqnpT4cmjn4OfEA5g-SrmEGmCMN-qhSkWQTE3InMBwV7Iu_kPuERMQFUBSDTXpqDsr6qcODpcP6-YEbITKPHvkVWfLCkWTbp5H5viPjp45g-c8b0mb7XkyIZJv4eMfxkqF-wQKfh9kqm_Zg_vSmhjziNMbD-LgUQjVtogp9WZtQAyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سامانۀ حساب‌های مازاد همچنان پشت پرده رونمایی
🔹
طبق پیگیری خبرنگار فارس از بانک مرکزی قرار بود سامانه «حسام» هفته گذشته به‌صورت رسمی رونمایی شود اما با گذشت این موعد هنوز این اتفاق نیفتاده است.
🔹
نیمه شهریورماه بانک مرکزی اعلام کرد شهروندان بالای ۱۸ سال می‌توانند…</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/466461" target="_blank">📅 18:40 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466460">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🎥
یمن با پهپاد جدید به سراغ مزدوران سعودی رفت
🔹
در این عملیات پهپادهای انتحاری «شواظ» که تولید داخلی یمن است برای اولین‌بار استفاده شده است.
@Farsna</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/466460" target="_blank">📅 18:34 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466459">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rfLEsADLs4-5cBDp6rS_nIjuvAKg1KCUiiG2ZZa0zKpF3Ir_Qbbcvku0mBESuaTTf0G29sqpPV01lKtxH8ntdTIbVjSQYGceNbn8m-R0p-doHo2hcigOZ3_CtQmkbhxBiB6bCXTMtTXoaWKanBudJDncuQ6tkKlu7eaGa40AMn74zImAeKDq8ITCZDrN1p_RKOFuv-hVEKduVLdpvahbXAmSm71-R2eEXOBvFzwwGUhTJQUqgxgW2GzM_YR417YwlQeOPiZWI-AA78r45WLySHDc2Ya35NlWFATt3Bcnd2_DYbwxh-9xEX93fzAOxa5y_nXb3jjdznxhHaMh_yochQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
دبیر شورای‌عالی امنیت ملی: خطای بعدی دشمن، «جبهه‌های تازه» و «غافلگیری‌های بزرگ‌تر» را درپی خواهد داشت.
@Farsna</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/466459" target="_blank">📅 18:31 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466458">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">‌
🔴
خط لولهٔ نفت عربستان بار دیگر از کار افتاد
🔹
خبرگزاری فرانسه به‌نقل از یک منبع انرژی عربستان گزارش داد خط لولهٔ راهبردی «شرق-غرب» پس از حمله به یک ایستگاه پمپاژ در شرق ریاض بار دیگر متوقف شده است.
🔹
به‌گفتهٔ این منبع، خسارت واردشده به این ایستگاه «شدید»…</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/466458" target="_blank">📅 18:21 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466457">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس من</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hir-A1rIA50EXyuTl51b8yHJ-DFZbDfRwsdrFdRjioF_Lgw0kOF3ze4PBF6Jxk9-Ivo6aNqRoYQwv_dKdSqAZ3UTV10OeXADot5ZKY6odQyYMDFgafqATZxylxR17VAYVvGmXeAnKcJKmUB_dqle0MqFN6qQFbBE2HxC2loA7D_bdgIY0XCZs3sB14kL7GTF0aZLJ24XCmz1lJ5xBbNgA_WUw3j6j18ep5-gqg6UKQzxwrJTildn8R0vHPq8hSD2O_LRoIup643dAXYeF4Z7YGKPV_AIyqWqDQd1ANbvlYqkCTW99KBNQQ6pn9HNSrekzH4OoVc9G7kfDeAdNOCOWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طرح «تورم صفر» در ارومیه هم اجرا شود
🔹
جمعی از مردم ارومیه خواستار اجرای طرح تثبیت قیمت ۱۲ قلم کالای اساسی در این شهر شده‌اند؛ طرحی که به گفته مطالبه‌گران می‌تواند بخشی از فشار هزینه‌های زندگی را از دوش خانوارها کم کند.
🔹
در این پویش از شهرداری و شورای اسلامی شهر ارومیه خواسته شده است با بررسی سازوکار اجرای این طرح در تهران، امکان تأمین کالا، منابع مالی و نحوه نظارت بر اجرای آن را بررسی و در صورت فراهم بودن شرایط، این طرح را در ارومیه نیز اجرا کنند.
🔗
برای حمایت از این پویش، روی
«
حمایت از طرح تورم صفر در ارومیه
»
کلیک کنید.
@Farsnews_My</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/466457" target="_blank">📅 17:49 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466456">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/atc_oaXorT_okWElvT6vwil8b2W4esBctB6V9IoBt9MbqBE7JnI78d3QLk_Z0AMC7hGfWQX7tIuaJXSFS9KSl3Mk3qciueURPDyGTD9d-qU_Q7irT9hn-2topT3Yk4N7q4mjr6h0SCV1RrWuqs_wUnC3R6l8987YUhYTvS7pxgfx4b4SZrWN9j_CUolW9uwqE8t8kh2AFgi-S9AT_2ZaNR1_cIffERvO7JsFNIzukCpNL5XyJdbliib2mG9z-PBhHsLiQiwUoroOuTJxYQP2xJGRL8FltmWCLlzcw1H4oCIb-sBvVuNCw3WaWcaeO-_1GYAY9jRHd7FGdutREoSmng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عبور از مسیر غیرمجاز تنگۀ هرمز، به روایت ملوان هندی
🔹
یک ملوان هندی با نام مستعار «سینگ» با فارس گفت‌وگو کرده و روایت خود از عبور کشتی GFS Galaxy از تنگه هرمز و هدف‌قرار‌گرفتن آن را بازگو کرده است.
🔹
او علت اعلام نام مستعار در گفت‌وگو را ترس از پیگیری حقوقی شرکت مالک کشتی معرفی کرد.
🔸
سینگ می‌گوید: کشتی باید چراغ‌خاموش از هرمز می‌گذشت. رادار خاموش. بی‌سیم خاموش. کاپیتان گفته بود هیچ وسیله ارتباطی روشن نکنید. حتی ملوان‌های ارشد هم بی‌سیم استفاده نکنند.
🔸
مسیر، باریکه‌ای است نزدیک ساحل عمان. عمق دریا حدود ۱۰۰ متر. عرض مسیر به قدری کم که کشتی‌های بزرگ تقریباً شانسی برای عبور ندارند.
🔸
مسیر عمانی جایی برای دریانوردی نیست زیرا عرض آن بسیار کم است، عمق در مکان‌هایی کم می‌شود و صخره‌ها بسیارند و خطا یعنی مرگ. عبور مفت و بی‌خطر از اینجا ناممکن است اما کسی این را به خدمه نمی‌گوید.
🔸
پیش از عبور، کاپیتان به خدمه گفته بود: «آمریکایی‌ها مسیر را داده‌اند و مرتب در تماس هستیم؛ جای نگرانی نیست.» ما هم چاره‌ای نداشتیم. باور کردیم.
🔸
در مسیر بودیم که ناگهان کشتی هدف قرار گرفت. عرشه به هم ریخت. صدای انفجار آمد. کشتی لرزید. همه‌چیز در چند ثانیه.
🔸
پس از اصابت موشک، کاپیتان تلاش کرد با نیروی دریایی آمریکا تماس بگیرد؛ اما پاسخ‌ها دیر رسید.
🔸
خدمه به کاپیتان اعتراض کردند که «تو گفتی امن است» و «ما را به کشتن دادی».
🔸
به ما گفتند که آمریکا همه‌چیز را هماهنگ می‌کند. اما وقتی موشک خوردیم فهمیدیم که آمریکا کاری از دستش برنمی‌آید.
🔸
کاپیتان گفت آمریکا هست؛ اما وقتی موشک به کشتی خورد، ناوهای هواپیمابر بزرگ فقط تماشا کردند.
🔸
اکنون در شهر کارگری می‌کنم. حتی با ۱۰ برابر پول بیشتر هم حاضر نیستم دوباره به این آب‌ها بروم. جانم از پول مهم‌تر است.»
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/466456" target="_blank">📅 17:10 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466455">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">‌
🔴
یک منبع در مجلس: مهرداد اخلاقی برای تصدی وزارت دفاع به مجلس معرفی شد. @Farsna - Link</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/466455" target="_blank">📅 17:00 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466454">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">مهلت تعیین‌تکلیف وزرای ۲ وزارتخانه به پایان رسید
🔹
سخنگوی هیئت‌رئیسۀ مجلس: براساس اصل ۱۳۵ قانون اساسی، رئیس‌جمهور می‌تواند برای وزارتخانه‌های فاقد وزیر، حداکثر به مدت ۳ ماه سرپرست تعیین کند.
🔹
دولت از ۱۹ مردادماه با اذن رهبر انقلاب، ۴۵ روز فرصت داشت تا تکلیف…</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farsna/466454" target="_blank">📅 16:52 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466453">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/efbdaac517.mp4?token=LTZEtjMLPaZYz0xn3_8WbpLJdqqvGw2hQ_rn4BWboano-Dr8c-EArlfkVDpfrQiXdBh5ZoRXGS5N5Z8DAft8CIEa0rfugM5HOJvivRaW_1SnjBOV5ZlCVs8LTUCAEboxlImp8hnvpsdOzpfoCB_EcUd9wXRb6lQYe220iRYdaXrQoh_94MtJFVVtKrTMLmykksQXFs7YZ2k_LWozC7ZOVJeITzbYOiFSnv-_weVsdrkq8W__Q-fC4FPiC1gMouwBI4myMlrL8fDm7iPrmvA8iudzV1QCVh7WHl-OniXxN_SITcqn0BDWuBd78v4QsdKd0coO5A30b8XphtyyaDcywg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/efbdaac517.mp4?token=LTZEtjMLPaZYz0xn3_8WbpLJdqqvGw2hQ_rn4BWboano-Dr8c-EArlfkVDpfrQiXdBh5ZoRXGS5N5Z8DAft8CIEa0rfugM5HOJvivRaW_1SnjBOV5ZlCVs8LTUCAEboxlImp8hnvpsdOzpfoCB_EcUd9wXRb6lQYe220iRYdaXrQoh_94MtJFVVtKrTMLmykksQXFs7YZ2k_LWozC7ZOVJeITzbYOiFSnv-_weVsdrkq8W__Q-fC4FPiC1gMouwBI4myMlrL8fDm7iPrmvA8iudzV1QCVh7WHl-OniXxN_SITcqn0BDWuBd78v4QsdKd0coO5A30b8XphtyyaDcywg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📷
حضور وزیر ارتباطات در خبرگزاری فارس  عکس: هادی ه‍یربدوش @Farsna</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farsna/466453" target="_blank">📅 16:15 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466452">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d3e3b132e.mp4?token=Wso5dBYu8qmeE9HgyqJRfLEcOqdd1jfdnYkizt0NnKfhMgYfXE_UE9tK4HwTBLKFFyqUDdFi4lIp0l_Kjiq_sFGTgeONsxndAww9jPVO06fRu67FQMVX2j3ySqbHFevNIX7JalAUGw09D0hHkFsndIrE9lRan2aYA_tg-sReRoOOBJISRg0mI2SIf6XpqSmqmGK3c1Q1JazgOF5JLUG_y3FmmWeJ0k1BI8AWdZYO7v2dUUVgcPsx5c1yo_yC4IcSpddGjBPe-R1Ou8U18NCo_tdu4_CVB1s2jlALKxt4uTwo40HWJuZg2N5IR61aCm84UFt-cZx6JHUtnrpVcOLpag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d3e3b132e.mp4?token=Wso5dBYu8qmeE9HgyqJRfLEcOqdd1jfdnYkizt0NnKfhMgYfXE_UE9tK4HwTBLKFFyqUDdFi4lIp0l_Kjiq_sFGTgeONsxndAww9jPVO06fRu67FQMVX2j3ySqbHFevNIX7JalAUGw09D0hHkFsndIrE9lRan2aYA_tg-sReRoOOBJISRg0mI2SIf6XpqSmqmGK3c1Q1JazgOF5JLUG_y3FmmWeJ0k1BI8AWdZYO7v2dUUVgcPsx5c1yo_yC4IcSpddGjBPe-R1Ou8U18NCo_tdu4_CVB1s2jlALKxt4uTwo40HWJuZg2N5IR61aCm84UFt-cZx6JHUtnrpVcOLpag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رسیدگی چهره‌به‌چهره به مشکلات زندانیان
🔹
با حضور رئیس دادگستری تهران در ندامتگاه تهران، زمینۀ آزادی ۳۰۰ زندانی فراهم شد.
@Farsna</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/466452" target="_blank">📅 15:59 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466451">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bffcc2cb6f.mp4?token=Dt5KDZIa3NBHX8xkyB3TnRilAqR1ZMju4gMi9Ylv6DEA533fKlxZYjxNOkhus7wZmwKo3IFPOrmhMvOwfWZJM70xau0JGVfl46mlUZ8Gxs_qmZw6KhI1F0_JzExaA-e5OX_7rQWwBPviOR8rKUz5KkYy7byZySQs3argBdZV6YcyZXn9UqmYCNphdSsRkT4hqs-UNPepp7EHAYlt3DltS5VpP8PL5TKvj64RqfeoeLOnokXkS3rc0V-1-nAv-C8v2agO3o6qWdjPxG9ApBPor0R6450i0rfqavwdAR2tGb7bwLBOToRy3HCJb2nZWHKx9l-r_Ei56SA6s26owxn4WA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bffcc2cb6f.mp4?token=Dt5KDZIa3NBHX8xkyB3TnRilAqR1ZMju4gMi9Ylv6DEA533fKlxZYjxNOkhus7wZmwKo3IFPOrmhMvOwfWZJM70xau0JGVfl46mlUZ8Gxs_qmZw6KhI1F0_JzExaA-e5OX_7rQWwBPviOR8rKUz5KkYy7byZySQs3argBdZV6YcyZXn9UqmYCNphdSsRkT4hqs-UNPepp7EHAYlt3DltS5VpP8PL5TKvj64RqfeoeLOnokXkS3rc0V-1-nAv-C8v2agO3o6qWdjPxG9ApBPor0R6450i0rfqavwdAR2tGb7bwLBOToRy3HCJb2nZWHKx9l-r_Ei56SA6s26owxn4WA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آغاز انتخاب رشتهٔ کنکور ۱۴۰۵ از امروز
🔹
فرصت انتخاب رشتهٔ داوطلبان آزمون سراسری و دانشجو-معلم از امروز آغاز می‌شود و متقاضیان تا پنجشنبه ۱۶ مهرماه فرصت دارند حداکثر ۱۵۰ کد رشتهٔ محل را در سامانهٔ جامع آزمون سراسری ثبت کنند.
🔸
هر داوطلب تنها یک‌بار می‌تواند…</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/466451" target="_blank">📅 15:53 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466450">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8cc6cdb21.mp4?token=DZmi_L-549DQDvN1ClCmOgQK3gvX4ut0d98HOOxhE15tmyZhD0w92AH1oehm93suBylBGsM5Rnu79Zb7Krp4XLvReu6h327DAuoaVYDqq5C5d0rTLYWYLt3RQm5PNgspbaRwz0ytZnAqMZ4oXsLsVi60QcyAZQo4IiTPQY5nzvW-bKs71ns-mcFfLbHWrSyelJBp2h17ixSinYL2ErHxUVjYd6-8E2ydfPj_gzXYIa5OHjKWe0tWdJAmxUJdhz3xhgSr8-7Axg-xb18NOAtcX-McrO8dPZ-7fM5Lc3rPzW_Ej_HMDmd6r4f7umjxl940ZsaHtYtwNeRFSdOuRIO0WoTXRf8ayI9_K8YGMBoWimkv0pZtS5PyYkLVnMK9gmd-a9wKjm1_MrEO9wo0TC9-R3MaT6cc-PjloVlzhf7_6L_CmkiOL4LknpDk9YlKZRTtGrRWOqgv7wcUu1iCqBvLB9SO36aTbqmq-CJZSHN9AZblCuyl79Xi0ZHoAP1daEdQha0EGD-HZO3AATbLHZY5hY4lLoer0C4vNlx9RIXyHyMHmrY1tG2Lbo9d_L5MaWB1IxeYIRX7GYzC_x-eUAmmp_RsJSwiaC1R9xO9z6yYEJ6c1J2zoAw992qPR4piIPaf2n9xbK5xgHuup06joQ_mFIzO7aOy2ODvMLMUn9hSHDk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8cc6cdb21.mp4?token=DZmi_L-549DQDvN1ClCmOgQK3gvX4ut0d98HOOxhE15tmyZhD0w92AH1oehm93suBylBGsM5Rnu79Zb7Krp4XLvReu6h327DAuoaVYDqq5C5d0rTLYWYLt3RQm5PNgspbaRwz0ytZnAqMZ4oXsLsVi60QcyAZQo4IiTPQY5nzvW-bKs71ns-mcFfLbHWrSyelJBp2h17ixSinYL2ErHxUVjYd6-8E2ydfPj_gzXYIa5OHjKWe0tWdJAmxUJdhz3xhgSr8-7Axg-xb18NOAtcX-McrO8dPZ-7fM5Lc3rPzW_Ej_HMDmd6r4f7umjxl940ZsaHtYtwNeRFSdOuRIO0WoTXRf8ayI9_K8YGMBoWimkv0pZtS5PyYkLVnMK9gmd-a9wKjm1_MrEO9wo0TC9-R3MaT6cc-PjloVlzhf7_6L_CmkiOL4LknpDk9YlKZRTtGrRWOqgv7wcUu1iCqBvLB9SO36aTbqmq-CJZSHN9AZblCuyl79Xi0ZHoAP1daEdQha0EGD-HZO3AATbLHZY5hY4lLoer0C4vNlx9RIXyHyMHmrY1tG2Lbo9d_L5MaWB1IxeYIRX7GYzC_x-eUAmmp_RsJSwiaC1R9xO9z6yYEJ6c1J2zoAw992qPR4piIPaf2n9xbK5xgHuup06joQ_mFIzO7aOy2ODvMLMUn9hSHDk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایت یک حضور
🔹
با آغاز تهاجم سراسری عراق به ایران در سال ۵۹، رهبر شهید که آن روزها نمایندۀ امام در شورای‌عالی دفاع بودند، راهی جبهه‌ها شدند.
🔹
حضوری که از جبهه‌های جنوب آغاز شد و به غرب کشور رسید و تا دوران ریاست‌جمهوری و اوایل دوران رهبری ایشان، در پیوند با مسائل دفاعی کشور تداوم یافت.
@Farsna</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/466450" target="_blank">📅 15:42 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466449">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/84aebc9db1.mp4?token=PHiwmbhd-bzAPO-ma0GTudMyEisdjcS-qvrmZ-K2dR16rA9Uvf9OJi32XS_vWiF3-HGxQ0-pVWi6Fpp-uarxKdHrWOIKwbXE0_CjUUlGUJh5YzJS7-ZPtzavgxWXTqmR7kBAdYdXBDbhmsnZQk2OJNv9jalNcMVlcwWkvop8qChgIe_8h5ycnbNNa7bXCp4muuIjSzCBxKnd4LNkxvFcMzXZfSQoUriyxip2bScqBUt2tZ-qZOT-CZyDztTFtBSxxQ3pobSVtu7gRVo5mDpodpz_M-cTYufYvOv9xwxr7DwO8wmc5Q2YMvapwvDiPHTEd0IVvd6ni7OTk6m7uAxbTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/84aebc9db1.mp4?token=PHiwmbhd-bzAPO-ma0GTudMyEisdjcS-qvrmZ-K2dR16rA9Uvf9OJi32XS_vWiF3-HGxQ0-pVWi6Fpp-uarxKdHrWOIKwbXE0_CjUUlGUJh5YzJS7-ZPtzavgxWXTqmR7kBAdYdXBDbhmsnZQk2OJNv9jalNcMVlcwWkvop8qChgIe_8h5ycnbNNa7bXCp4muuIjSzCBxKnd4LNkxvFcMzXZfSQoUriyxip2bScqBUt2tZ-qZOT-CZyDztTFtBSxxQ3pobSVtu7gRVo5mDpodpz_M-cTYufYvOv9xwxr7DwO8wmc5Q2YMvapwvDiPHTEd0IVvd6ni7OTk6m7uAxbTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
جمع‌آوری ۱۵ میلیون فوت مکعب گاز همراه نفت
🔹
متخصصان ایرانی موفق شدند با راه‌اندازی ایستگاه تقویت فشار گاز بینک و نصب تجهیزات فشرده‌سازی، امکان جمع‌آوری گازهای همراه نفت و کاهش گازسوزی را فراهم کنند.
@Farsna</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/466449" target="_blank">📅 15:38 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466448">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس علم و فناوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/648bfa8f07.mp4?token=U2-MRn_8NRQKlUIUpMfYWD4EteM3jG759MovW6pfgnNlGwlhJuU-yL4_Px0abbev-A6y-scsr7eenfpSBYZbMQbTgLEWBiZPXUJ95fLXFjseug2r-IMc7Hz-HJ87LYKSp0wDbHRRzCHFBvtoL7yJze5fLtQFEquAOZkcHAMNeCITlvkmc5AwSnlpIGvnQU0YWGCQU7VGoAx39fUlbauclJu4ydqWa6P2PU-g-Dq2EecoC1BApfN6ZrLBVpS1eFiaargZVdKgD9Ofc0sgI1ucilog8TJMKhPX472Ta9WefBx6LWSIhWJviTthUhZUbvNdAetS8FMW1rBEfo54ROq7ig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/648bfa8f07.mp4?token=U2-MRn_8NRQKlUIUpMfYWD4EteM3jG759MovW6pfgnNlGwlhJuU-yL4_Px0abbev-A6y-scsr7eenfpSBYZbMQbTgLEWBiZPXUJ95fLXFjseug2r-IMc7Hz-HJ87LYKSp0wDbHRRzCHFBvtoL7yJze5fLtQFEquAOZkcHAMNeCITlvkmc5AwSnlpIGvnQU0YWGCQU7VGoAx39fUlbauclJu4ydqWa6P2PU-g-Dq2EecoC1BApfN6ZrLBVpS1eFiaargZVdKgD9Ofc0sgI1ucilog8TJMKhPX472Ta9WefBx6LWSIhWJviTthUhZUbvNdAetS8FMW1rBEfo54ROq7ig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
با این کار، حمله دشمن به زیرساخت هوش مصنوعی کم‌اثر می‌شد
@FarsnaTech
-
Link</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/466448" target="_blank">📅 15:34 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466447">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pbpVlYoQybMHHypCSqwI0zN2df0FbN9iREV-p14ipd-PEqVDSyOFCaJel6uHoghg4MrJItnJIoTebhO-2GuN6GR_48y_mFl_cc0TeAIYhgNK5UYHASlVpf-An5wARzkspQRxP0EXCnSWOL3_ZQRk7vDQH_3wzMu5xQgiRwf-pi0YxDyqXrEotvvJOZMc5BUw-bCg9rtoNP2Oq3ux7KqCJykm1xIXGWRjf9b5EdO-VYBUCHU6ikbxivx02V_ul0ahD8QCaTTPMlqzwIWDaQ-rxIg23xM5FX_ibu2Gdv7VQuCYJEG9-XJAXMQOJIYKKDHJgCCxhX_VxNuvORqu3eJZGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان: دولت پشتیبانی از نیروهای نظامی و انتظامی را افتخار می‌داند
🔹
امنیت از بنیادی‌ترین نیازهای جامعه و زیرساخت زندگی آرام، عدالت، رفاه و پیشرفت کشور است و بخش مهمی از آن حاصل تلاش نیروهای انتظامی است.
🔹
در جنگ‌های ۱۲ روزه و  ۴۰ روزه، نیروهای انتظامی با مسئولیت‌پذیری و فداکاری برای حفظ نظم و امنیت مردم تلاش کردند.
🔹
شهادت بیش از ۵۰۰ نفر از کارکنان نیروی انتظامی در این دو جنگ، گواه عمق فداکاری آنان و نماد ایستادگی و دفاع از امنیت کشور است.
🔹
تقویت تجهیزات و فناوری‌های نوین، ارتقای توان حرفه‌ای و معیشتی کارکنان، حمایت از خانواده‌های آنان و فراهم‌کردن الزامات لازم برای انجام ایمن و مؤثر مأموریت‌ها، از ضرورت‌های این مسیر است.
@Farsna</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/466447" target="_blank">📅 15:32 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466446">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f8e7475a0.mp4?token=UtM-iRBjT3iqDWBPhJeq6zJrUpMhb_hwgT08u2zWA1zxl12McNd0VMm5tRhfvohNi9mi94Zpn02H4GnzYm-u_s-9FHmLmyZJzmeSChI0zfNvuA4uzwByzUfYgS4AAZBQ_nbZtj0L74gOSQ0KFhOrZCQ5QbR6_a2FeTEfiq8tmDtDaennErxD0cOPQ66TSrI8V03sQ3QHs-Q7is2zsxrf6z7FzKAgX3YyGHnm96g7fen_6sOIap5ZHn-dw1O3OYWt9FpHTr3depi3T4ep84EM6XI3kiXKvRQ8A8cbTtLrl2i_rwGRm4lYs6MJPfjIHbS96xR_D-uEytLNKMIDT82QNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f8e7475a0.mp4?token=UtM-iRBjT3iqDWBPhJeq6zJrUpMhb_hwgT08u2zWA1zxl12McNd0VMm5tRhfvohNi9mi94Zpn02H4GnzYm-u_s-9FHmLmyZJzmeSChI0zfNvuA4uzwByzUfYgS4AAZBQ_nbZtj0L74gOSQ0KFhOrZCQ5QbR6_a2FeTEfiq8tmDtDaennErxD0cOPQ66TSrI8V03sQ3QHs-Q7is2zsxrf6z7FzKAgX3YyGHnm96g7fen_6sOIap5ZHn-dw1O3OYWt9FpHTr3depi3T4ep84EM6XI3kiXKvRQ8A8cbTtLrl2i_rwGRm4lYs6MJPfjIHbS96xR_D-uEytLNKMIDT82QNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مدارس فرانسه به دلایل امنیتی تعطیل شد  به دنبال اعتراضات دانش‌آموزان دبیرستانی در فرانسه شمار زیادی از مدارس این کشور که در کانون بحران قرار دارند تعطیل شدند.  @FarsNewsInt-Link</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/466446" target="_blank">📅 15:09 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466445">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">انتخاب اعضای هیئت‌رئیسۀ جبهۀ اصلاحات برای سال دوم دورۀ سوم
🔹
در جلسۀ امروز مجمع عمومی جبهۀ اصلاحات ایران، ۵ عضو هیئت‌رئیسه برای دومین سال از دورۀ سوم فعالیت آن انتخاب شدند.
🔹
آذر منصوری، محسن آرمین، سیدحسن رسولی، بدرالسادات مفیدی و جواد امام به‌ترتیب به‌عنوان…</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/466445" target="_blank">📅 15:06 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466437">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/16d174ccaa.mp4?token=BYZv_EsLw3CqmpzsdaQ3HjPxtGGHd62aoaY4cKbDXCRuB7x7pV07GhVMeFcQ1QhKz46uRoEe4MoDnpk7Bl1X1HrBQ2sCkSRcAAY7iCL74QctiyaY4wNSHrQYuQgY3Ebhr8e-ZYs2nMudt_bH-tHpRoGoymdQjII1MhDZ4T2WLQJE3kDFz7wy-Nd0DLNKOYPhUr2PKtwz2JDTBR2AKCubos_7QHCGRmGCLULgVPTrLnXxyXLDV-BMYGfuuxzZWDR8qUq_s01xLZNa0wZm-QfQ5it0lSAw43CqtXNl96M8aGA8C3-Mo8LixTgq5Cpzf52f19F0pkMN8FYX9cE5O1UBPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/16d174ccaa.mp4?token=BYZv_EsLw3CqmpzsdaQ3HjPxtGGHd62aoaY4cKbDXCRuB7x7pV07GhVMeFcQ1QhKz46uRoEe4MoDnpk7Bl1X1HrBQ2sCkSRcAAY7iCL74QctiyaY4wNSHrQYuQgY3Ebhr8e-ZYs2nMudt_bH-tHpRoGoymdQjII1MhDZ4T2WLQJE3kDFz7wy-Nd0DLNKOYPhUr2PKtwz2JDTBR2AKCubos_7QHCGRmGCLULgVPTrLnXxyXLDV-BMYGfuuxzZWDR8qUq_s01xLZNa0wZm-QfQ5it0lSAw43CqtXNl96M8aGA8C3-Mo8LixTgq5Cpzf52f19F0pkMN8FYX9cE5O1UBPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تقدیر از برگزیدگان نیروهای برتر فراجا
🔹
افرادی که خدمت به مردم را در هر شرایطی وظیفه خود می‌دانند و در دو جنگ تحمیلی گذشته، این موضوع را به اثبات رسانده‌اند.
@Farsna</div>
<div class="tg-footer">👁️ 8.94K · <a href="https://t.me/farsna/466437" target="_blank">📅 15:02 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466436">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاخبار لرستان</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aovfDYChlzkjnDSvhRV3kJHVgNkkAz8jyGOEbxgudnZTxRskFTyCi98edtbEV7Y5HgVp6EYFDxz_5l8MYJlF-Rf3P92uDFxeyKturCyqPa22q_FVnXt_LxFg8zOWPaFCceOJyE9NV3psW6I_gWGlIguq9Lfr01KOtPPORkGY0TumeMbjStQdVmw8PhdnDJEhGbHi-4llhTmabt_2zp5E8wqInDGOScg_tBVH7ndvcDGmI4uHhd0jB5wWX7fEUlBYF358muTBusQU-eWcdnysr-tojOXSk6muHIBZZYXydXhHhreds6Hv7j9tpLVWliq_-rW7zoElQL20ZkcUHC3TIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vkQs_nmA_Zi58NuTfgeDTIIQc8UOSv7LmhXLqeXQ6LaIaDwIxRpGkxTdAY5xriQlXVHTRbI_D9EmlvGWxfPqjLfVgxxraVhHY82ffrOMimPL8vmOvflpkO0ghOXcpH2XsrREo1FcezayafLyZDZpgC4yBfhuwJBLionkGb-nYxllGqRqogrU0Dc_6SfB9eaeNWx0s9_We0zsZK0IJl9oppuiqrSucr0Nm9xzKW4BESdUrUbPg60VUa1qFJrZmASFkFLZWSAB9hss84HBldmkgF8ZOFYNkJCvbPe239ZUGiKkxV7EugU55U5btvgyQmS5tcMR-1SazyvipjeNuTqEbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gTdJiVVQtVU_7FxfMNytXont7XyWmBdPxtV3HjdsXLi6mQY1zh3fPd1KNL9nGI_J_MNC2Mg3wrvD2TvXS5qiYt87tGaoezMsL74LXGJfAkkNSahTnRAtEjnbElDdEdI9Q9fER9n6_mKtzySU1L8rAsTKng-AS4NuwJMYKsTQlPKjmZ9nZLtq6T_cMBeI1WUeFh4FgGtubY38-_QqiZoGDByhszgLIKm9DLTKmGxl5qfOCjgHpYjL2OD_sQyt_0YKucCWcwtMeejChi2LX1T5175p_XkU1GiZoHLJmDP--TokjKDu2J552vLMhHxe9L57NNg6OhbPW_scD7QQOQly6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Rvn2fwfK7cSmwg4Sc8QC906YKm1KPer6ou82Dk9uTXLvWIcsWVMo2o34TV2iR8Tkm9uP7jTubqRi_GrdDmkRQpo0Ub6FpeNyKfqbBRPiNAPjqoRvlaF1EUvVeL2Mmqt9GWjiSROlPtGyPUsCNxJkhpMJmjug4ZdWSVpVnTPkDhkckar8XeIfUqO9jJ3pdWmXemDcqep6jbcMKm-NvdhbXiwJDHUjKxUD90yuOmiXrOlN0fmaoVQWXV1B246toKEleoNpXumiRpO3r6kFHiuAA9AAuq9jc_7DBMKQTv1AD0NawdDVjsER4DTPjlUGuSNdufTnanWTXmA7vRqE3dMFZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Wz-ReBU2GWKRM2ySJ9sa2nMcbkcyBZqPQ59XYfBrmPe4nxZYqRLPNvpu3bSYZsVhDyhL85TlpxPbbvXP2ZZrXdDYQbEyhNOEw0oJXn4Dao8LKoe_STPR7U-c1bTY47ZZUQ_PCjNP8mxYOEe2gE06Bc36ENkmMb4t6ubCbvwlDwBsald27ZjtuKBRQJ6KhEmOxl8Frv50mSgz3oLBgqcta3VpK_3KOyZNSTnVcqmfKCx_9bXDNix_v-s4vpxN7TaXhye4DfWzhQHPsX_YuOBludkayM__S1jppDzTnxGmXMLPegHzTGu8_CxV3BEgaJgOccsaMXtaeQ9t2mpGIRawjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BX6K7IL0SXEC7WcQJqfWrrVa6RB9Xq6tnl-wmgcrRAjS3S1n5nOUHRwDnoe79mFQ4jYJ89GqjJ-Y5G3WoFNSoldmDoXuUg54pVKAgn5RXnXQnL27PfJUnlTCfRVQYT0RdBwfVjFViLc9YWrpNChojW8OozwnzGyKE_Kt9OHrgG1GLvrH-2xbRckR9NvBME-PobeynSUrfDqNBBEPEvpfvs1nJVbN0tTenErtRNZch2jknCETDZkVLIJ-YN2sPC0Wm0ZL1uBvO02ty_WARaQesuV37plO6yftzqBLJlBbXkkftsvA_w6jg0FRZV0oxAwTPq581Yl2nxQ0kvCZ7TsUaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Gq1TjEPUFf6KGazOLlyyWu59MfifjiSbpOyOCyAbjmMTdOlBW5rQFMI8sc_LCujT84Y4C-d9ZpKJ5Mo5-Tnh8PyDzxz2e7_tiEtAkRZ_CjteYj5AjlDyTubqdv47Eot4a0bK2RLAGF6APTqa0zekcZHuXeTbDCzXWQdaTq6cJ5V2ae1crI5oXOpsfFx-sanFlZ65-FBuXP8lMl2TcbyobGJ9ncNVpd4n-bpJMjhaPndcfMX1cT_YfnNGrOp2JLz3qTnOcpwliNW3_zjcOt8qD95J6cwF9sX3VQhlH2SiQ9BiBlUeMfFn5xCaCm9-scNOQN8gVv_K_lTsoE2QBEay6Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
برداشت برنج از شالیزارهای لرستان
🔹
فصل برداشت برنج در لرستان بسته به نوع بذر، شرایط آب‌وهوایی و منطقه جغرافیایی، معمولاً از اوایل شهریور آغاز شده و تا اوایل مهر ادامه دارد.
عکس:
نگار ده‌دهی
@LorestanFars</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/466436" target="_blank">📅 15:02 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466435">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/acd905fdb4.mp4?token=bMGEYLNCGTsytDG7_Rklo3JCyhD8sCv1yaEM7sr029WPay2sgAUq8DKOZCq6QyBfZvYghABhD9t70T8f0U03t40DjqXY_qt1z1S0Yr9Rmelg4VL_aWwlU-5IM8hw-1488Qkg6fu5pvltWu7JwABcmmZrKWiYXo2puxXW57Hh3bzrqGWa7ksCOwKTFo_TMchco-2C35JO1M-HRecXg7YQehRH_oyuI9HRT_2PqkbD8ecQ5j492nVeO-c_xRotaxpr0kYrFjtBTr4BRLSYYzB1Z5PYv16UezCdMVYDRgnMDFFFLmxgneFitAM44zQI0FTT-D3idhaehDEO-ax2rEy7YA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acd905fdb4.mp4?token=bMGEYLNCGTsytDG7_Rklo3JCyhD8sCv1yaEM7sr029WPay2sgAUq8DKOZCq6QyBfZvYghABhD9t70T8f0U03t40DjqXY_qt1z1S0Yr9Rmelg4VL_aWwlU-5IM8hw-1488Qkg6fu5pvltWu7JwABcmmZrKWiYXo2puxXW57Hh3bzrqGWa7ksCOwKTFo_TMchco-2C35JO1M-HRecXg7YQehRH_oyuI9HRT_2PqkbD8ecQ5j492nVeO-c_xRotaxpr0kYrFjtBTr4BRLSYYzB1Z5PYv16UezCdMVYDRgnMDFFFLmxgneFitAM44zQI0FTT-D3idhaehDEO-ax2rEy7YA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
صدور گواهینامه در کمتر از یک روز
🔹
رئیس پلیس راهور: با اجرای هوشمندسازی، از این پس تایید و استعلام درخواست گواهینامه به‌صورت برخط انجام و در کمتر از یک روز، عملیاتِ صدور انجام خواهد شد.
@Farsna</div>
<div class="tg-footer">👁️ 9.37K · <a href="https://t.me/farsna/466435" target="_blank">📅 14:51 · 13 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
