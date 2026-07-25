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
<img src="https://cdn4.telesco.pe/file/tVvIYb0uPmhtpZQZhA0TuxHkrFuvq7hnLdweN6Y09tPv3bhlMKFxozD_mUTr1CzBCGPE6zf_kEM8v80eaD8VC2ZDwYa1mzQlIlMyfm_tCc6HKplrFIcvNe80l-5X1K3PyWnXXbs_aehWhuwtuYxNJG1xfj6yt1k_dttLpV8lCZMnJDrFULdW1CYo1AjXvRkyLXBUv-59NNR5xj4-6n5cwfEF54b6Qs9ySdvMokDO3G-dzZdi9SsafEDh_GiaC3Jo2A509Yi0o_RcpI89VvwIp4kl_Br9RiALw09OslR3I9ZnxvFc6aeypthor2lf5FdWL7sAKjWzVFJL2zKw7FaJIw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 208K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-04 01:53:38</div>
<hr>

<div class="tg-post" id="msg-81266">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lxc91Pe6f3xBAp1ORJOgq9i-eqdrwPvWyOVJ0Gs_IIjdeLdJcB6m78fB6kC6rQz9Bgxmm83z3-idOx6p4pvu2lb6CM6r8i93NAzuIUmax43DBGdYDEuUAwt4rLccqXgijBf-dCE65Ujqr9Mh6FwsavfuoBZGnfkf2BSKluC2dTzEJtKHRdg_B0y48AMvaUW6wUs7xClgthyy8t2PaWuWM37x8J_7a5mfOrUb0dzvYVNYPcKW396feCL-1LJYeo2OvhKXFS0HTsDpgrQTB8Y7WCaAxAWOVy8guOSm9mEJItqyHQP0ovKIPYawWxWh47IFqtOCP_skPeTkzUtsAgs4iQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چی رپفارسی؟
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 884 · <a href="https://t.me/funhiphop/81266" target="_blank">📅 01:52 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81265">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">ترک جدید حسین تی‌ام و شایان یو به نام "تقصیر منه" منتشر شد.  SoundCloud  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 4.32K · <a href="https://t.me/funhiphop/81265" target="_blank">📅 00:29 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81264">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K0hd3unCBNLJd4mVKYAj8gLVNJNI5YvuaMM-LifFWPiXDTvPYX98nPYzskYIH1-csCxn0bTLDzEmc95Aw5GNKzLzUZ1Bgew1KaFkH4503ksLGQrnWLAYVXRLgkNTngAnozY25L_tDV6lGpvgatPwBIaL_UmDe5ARHbCimJX74LjxEhA5bxXG-4pxEU43A-85mLuqPI-Yx2qVB0nbo3Y4itjVmGWDppA_gAAweDJaXygPwC75elMw-OMPWtxbY6T43hjLA7z3FfNTqE9KtbAEueVoG_9QacNZ2QcYrA4tx9VDQFjRjeJPW2ZXQNgbzHj9iCKGEatHkhAYlr01jVc-xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید حسین تی‌ام و شایان یو به نام "تقصیر منه" منتشر شد.
SoundCloud
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/funhiphop/81264" target="_blank">📅 00:29 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81263">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">طبق جنگ ۴۰ روزه امشب شدید میزنن
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 8.17K · <a href="https://t.me/funhiphop/81263" target="_blank">📅 23:36 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81262">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">تموم شد، دیگه هیچوقت، هیچوقت نمیزنن.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 9.26K · <a href="https://t.me/funhiphop/81262" target="_blank">📅 23:24 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81261">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">ترامپ در گفتگو با شبکه LCI فرانسه، درباره ایران:
به مامان توماج صالحی قسم این دفعه
این‌دفعه به شرافتم قسم بار آخره که به دیپلماسی فرصت می‌دم و اگه برا بار ۸۲۸۲۸۳۹۸ام، ۱۰۰ درصد از ۱۲ درصدِ نصف خواسته‌هام برآورده نشه یه جوری حمله می‌کنم که اصلا خیلی شدید و دروازه های جهنم و این داستانا قول می‌دم قول
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/funhiphop/81261" target="_blank">📅 23:09 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81260">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">هوف
کانال ۱۴ اسرائیل: ترامپ دستور توقف تمام حملات به ایران را تا اطلاع ثانوی صادر کرد.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/funhiphop/81260" target="_blank">📅 22:56 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81259">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b585792e34.mp4?token=gANAr6NqFxBiUzTzC9wJUU3Gd-g8eCx6c1hZPe5zhsPnxNjvKqjZQ1kTG_rDblVonzcqvN7aGFfe7J_zQmuhBEXR_mvI-UIzTr06JmVzuMGzw5ZNr-gaYktXMLaadCSs771dD4kq3CNQoq9pi6o--8fIiDRWrxS4mgpt8cXHPEpxWhp7aHo8CBC_8xW1hd2gWzexsk6myhG5LRLJ8Si_PGR-yWUuV2dhpWcvD0pnL4RhPppnpJDKDn_pUTJ3M9k8tZbD0edT-024fb32KZ-uP-_1wFbG1kt6DfYlzcWBBwRdnhqH6F0OmaWj90oQf8BYTzY1UxUTGuyH7y8WtINy_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b585792e34.mp4?token=gANAr6NqFxBiUzTzC9wJUU3Gd-g8eCx6c1hZPe5zhsPnxNjvKqjZQ1kTG_rDblVonzcqvN7aGFfe7J_zQmuhBEXR_mvI-UIzTr06JmVzuMGzw5ZNr-gaYktXMLaadCSs771dD4kq3CNQoq9pi6o--8fIiDRWrxS4mgpt8cXHPEpxWhp7aHo8CBC_8xW1hd2gWzexsk6myhG5LRLJ8Si_PGR-yWUuV2dhpWcvD0pnL4RhPppnpJDKDn_pUTJ3M9k8tZbD0edT-024fb32KZ-uP-_1wFbG1kt6DfYlzcWBBwRdnhqH6F0OmaWj90oQf8BYTzY1UxUTGuyH7y8WtINy_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینم از مادر رپفارسی
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/funhiphop/81259" target="_blank">📅 22:27 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81258">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ff8068cd9.mp4?token=oD8loc8wmxGPa47smxr-MPFZOvL5FYP5rhOtSftMsEsIL_Ee5r9B0DwUOKl21DEt8uYFQpFsdHjWaGTqTY5A00sxmVB0Z6VMT4sXJEKVq-bIkMUif-QiMXZjNUrSch1Na2YO7DEBNX16z-IQw9GbquSRLBogKcZi1QLlIvA1J98BYfBmcivE_-R986cayaX_yOrqXGBco4gIk0Km3lGIuTbiA2K_03FNgMvgHK8SXALuzUySIJvnGlNKYZ-ALtQFdPjx2ZyfLWen3rAa9ydk6rzgvYg7npeDY9WwHJR0bvCZKH5w3viCBcBZyYyV8mewuHm_Rhxh_Jr9J6hKI1mNSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ff8068cd9.mp4?token=oD8loc8wmxGPa47smxr-MPFZOvL5FYP5rhOtSftMsEsIL_Ee5r9B0DwUOKl21DEt8uYFQpFsdHjWaGTqTY5A00sxmVB0Z6VMT4sXJEKVq-bIkMUif-QiMXZjNUrSch1Na2YO7DEBNX16z-IQw9GbquSRLBogKcZi1QLlIvA1J98BYfBmcivE_-R986cayaX_yOrqXGBco4gIk0Km3lGIuTbiA2K_03FNgMvgHK8SXALuzUySIJvnGlNKYZ-ALtQFdPjx2ZyfLWen3rAa9ydk6rzgvYg7npeDY9WwHJR0bvCZKH5w3viCBcBZyYyV8mewuHm_Rhxh_Jr9J6hKI1mNSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عباس داوینچی درحال لذت بردن از مذاکره
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/funhiphop/81258" target="_blank">📅 22:17 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81257">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X-bzLitSOqaXam0F_G0gGX-VGYPrr9JlWh_J0g1fZKAX7UNHU1JBWMkVayz34Y-1F_UJZBLpxeEOZLnJfycOlFlMJbAFLqPt7kbuOaL9lrUPoSe0ZlGuTwhjjodGW7RN6dW1A_Go7vKUm7AemIdKmEkYOAlQQ04_AQV33kxEM4OiSD5viNXR0VgjzXabGahECVdNAa3rP4v6_76y1O_IelUYIypGlRe3wAZNP9XpavYedDkawEfp1auSdnpyoDsJDnd0UOGjqs1QSZUdQKEpVLZsgQqxLZZcDW182Hu25KOPD8EFfOR028E7xFLTVMbbJV5EFAKFLd58ERqBIJIgKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/funhiphop/81257" target="_blank">📅 21:39 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81256">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HwUjSN71K8Au3n5kGAIxIAbidQHuiLyDpdxKEfUBfVCseR3XskXuIGPeT9rX-aezHTMp-JrvGhKhMS5iUAJ8Qn1mzp2jvC3o3-I4QrdVr2n9J0S_X2z1InRHMaUtHad7IZ-YsIWJ-0YKHEkFKUShGt-AGfUWg957QF1uGBpiDkQUNc9QnJ0z0Suuf_BaexrWO35sg3k0sKe31hp6iCkX554rFEsXwXPx7nuDNcBXlsDliW2-SUVGTxWPg_POwCcHVV9kCFbDfRuyle4wD3ru5mOGWJSVLKslBAEK06DSMKTIpja47RIROU6E3N2JAPWEKqR9pUmxR9BtBguQQcBnGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یهو یادم افتاد چند وقتیه براتون طهلیل و پیشبینی میلیون دلاری نکردم پس قطعا مشتاق و منتظرید: این هفته رو کامل قراره از ترامپ و باراک راوید و نظافت‌چی رویترز و میانجگر پاکستانی-بنگلادشی و راننده شخصی جی‌دی ونس اخبار پیشرفت مذاکرات و آتش‌بس بشنوید، این یه هفته…</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/81256" target="_blank">📅 20:43 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81255">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">یهو یادم افتاد چند وقتیه براتون طهلیل و پیشبینی میلیون دلاری نکردم پس قطعا مشتاق و منتظرید:
این هفته رو کامل قراره از ترامپ و باراک راوید و نظافت‌چی رویترز و میانجگر پاکستانی-بنگلادشی و راننده شخصی جی‌دی ونس اخبار پیشرفت مذاکرات و آتش‌بس بشنوید، این یه هفته که بگذره خواهیم دید چه خواهد شد.
#تاحدودی_بماند_به_یادگار
#تحلیل
#اکسپلور
#مراد_الله_ویسی
#خدابخشیان
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/funhiphop/81255" target="_blank">📅 20:05 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81254">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Aip7FQMuwEBZpLQXTaL2JRzGUob_jvIEIfr_LTAu75hW_7LVbQQocp2vO9W14Y28P-qXnSk4SCmSiuDImNcz4rhuEyqWljTY40Nbl2HIRD7cPso7Bk7k_0AeQXhuuD8fvHlfkPPAUYQ0y8Pw0fK04yXiEHqe_Cl_sLS1LlYblLxrhxe3Gc57yKtDS5yTaj5o3_g5YCBm_F_vAAD3EFYe1eNeJQBHA2fOizyZHB-BKlllHyTNU2YmYt9nr0QkCz-RZvslJzn15yUiHXQTzzwuJ07E7pWbfjsNZIAgWIhhoZiW1jj-NAAHMgCmp00YE-d687CU9Bbhap7zgBRo9Nt-Rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید باشگاه فرهنگی ورزشی لیورپول :
@Funhiphop
| Jenayi</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/81254" target="_blank">📅 19:50 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81253">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">قوه قضاییه اعلام کرد که ساعدی‌نیا حق باز کردن کافه نداره.
@Funhiphop
| Jenayi</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/81253" target="_blank">📅 18:51 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81252">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sdhEpKR8g4ucPiSdPWbyvTZ0bURoPSPiiXlXHwSEWhbPR_-OOImuPH9G8DHmGhDHfmBn9iTM55-2S7A6aTxLKNUGvNUgPXrYT_TMyVLjGW0_k8YxKlCnxpRZqc1Fn_pFvu_mr686v-zDpGjwuQmwZ9JpwKFE6Apq0TjBlNs3p_O04nD4PbM0Pshx3-G64OOV10d2SCtNqmX1_CswB5ril13D1iPmhRese0r086qrxd3jgDNQwWuoZo1Ijz2V0ljMHpIURNcd8a7Q6cWfhdYMewbodLzM0v96O0wx599uPpEE6trAVOlVFyip2Vhs050ht-IF4cbShFOYLEBXKb1nZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میدونستم اینو قبلا یه جایی دیدم.
@Funhiphop
| Jenayi</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/81252" target="_blank">📅 18:46 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81251">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fHlfTOD8oE8tRVrKHaD5ikgaSmhUzzRRO7wHEru33hnpnt8iBelijP1S-Oehf7HD7yI5WHP_hHysX6hDU0JzQrvzbAS-B5vF_Kr4CYqfHHVoF9wM6UYgomPmnMdyaHdH66BIVwLjJmQCBa0kUcSOAKKKGV-k0nO5MMTGiqXlYoE8ezW6Zv8Mwitt7dUaZ9s_sCYl4lnPmiAb_GdHEn5SJ9xl9vRAiyMgJAcKw4MdA_ZIIvT3Psm_QDet-f0gbh52sqBdSm2E4FvnbSfhnx1MPb2qDRsiBNc6AZ1SMTotB2tuIEJer6vjmkMdo42Dd05QwCqzcbocRCSNY7b1jjq7Vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
پورتو
🇵🇹
-
🏴
استون ویلا
🏆
رقابت‌های دوستانه باشگاهی‌
🌍
🕔
شنبه ساعت ۲۲:۳۰
🎲
با بیش از ۲۵۰ نوع آپشن پیش‌بینی
👆
ضرایب شگفت‌انگیز
📊
نگاهی به آمار دو تیم:
✅
پورتو در ۵ بازی اخیر خود مساوی نکرده است.
✅
استون ویلا ۴ بازی اخیر خود را برده است.
📈
میانگین گل در ۱۰ دیدار اخیر استون ویلا ۳.۷ گل در هر بازی بوده است.
🧠
پیش‌بینی آگاهانه، تمرینی برای نظم ذهن است.
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
r3
💻
@BetForward</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/funhiphop/81251" target="_blank">📅 18:46 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81250">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">خبرگزاری وای‌نت اسرائیل درمورد اینکه چرا دیشب نزدن و چه خواهد شد:
ترامپج می‌خواست خیلی عظیم و گسترده بزنه ها، ولی گفت یه فرصت دیگه به ایران میدم شاید دکتر عراقچی یه کاری کرد، پاکستان و قطر هم دارن تمام تلاششون رو می‌کنن.
ولی برای اسرائیل، این یک فرصت موقت برای ایران است که تغییری در ارزیابی کلی ایجاد نمی‌کند: توافق‌نامه آمریکا و ایران از بین رفته است و
احتمال دستیابی به یک توافق نهایی که در آن ایران تسلیم شود، صفر است
.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/81250" target="_blank">📅 16:59 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81246">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g1pxHqmJD6MwwhJ8j7Xj2G8QKtmL5QzF5KcC0FWFvkHt1jLcH2s8o4tfFpBhtmE-HCHRKVMsQjsOdfSQUcmGf0-ZBwXXnftN6pqCHnvJ9QSA3Y5XvGqoS7Jj5yNZLRfVxE-75MaCM3-AWj5CvFeH3y7jA1eAZcky2H_H_2f7ssTigSZU7qqz54AAyqJUx2Q-4G1ikeoIAD7Sa3RaqO5DXGwXPQ9Sog3ko9ot9DiPXpYv7atEyYqyT0YWCmQlQlMLr_96zIRe6BVV1KQ4Yttx52plLnv20zOIloJexX_QK4opNuvbni4_ICs2tI4sLDYssW5Xgzc9aj0v_TIpzriV3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بدبخت مهدی
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/81246" target="_blank">📅 16:00 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81244">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">نیویورک پست:
آمریکا در حال بررسی طرحی برای خارج کردن اورانیوم غنی‌شده از تأسیسات هسته‌ای ایرانه؛ «پیچیده‌ترین عملیات نظامی تاریخ»
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/81244" target="_blank">📅 15:43 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81243">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">عباسدرمن: اگه وزیر نبودم میرفتم پشت لانچر.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/81243" target="_blank">📅 15:08 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81241">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gx2b06JK4b94jNvCnWQKAmJIG5wymvQZoSaJgfT59cYwqxzojnFsy3kATsY0r7ewEbqJopGiO5Y8vflJajFNs53bmATTTUk47-uwgNIfnM9CAccXMjvIeVSy7OOc32yPfcF-QH_ZTstJBd7WEbqAk_yip1EV1AvT-tgXDYddbysGjBxVEFyojwe93vD3-GFL-8_zslSOFZjQL_tP394WR74opc6mbGOZHuYu76l6N168WRgDZyX5zcD9J_b2g1zUUs0DpI2xSDxYJ521aySDH5D73QhX2ed568urUT9K70MZ4gSZHh902_cqx8RblNI0Px-4syfbIY8Twa0eibhM-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تا ما بزرگ شدیم علاقه به کودک ترند شد
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/81241" target="_blank">📅 14:39 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81240">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/llGCb2siPXW3fah_ghbYT4Ty7rdaAFFNsqcYu_60FPFr7GNWJi6R4kuWFxrmxPcofGUpXX1qzxoDyqf05qylgI0G7Rfakdc8hvmaVuuGzWcpO944HYb0tB9QzVcHxMJxmHh2JZYzyl1qCaqky2BJIddEfAqBnmTQZbYYcMhOEiAQG3XaHhO1fDZNewfafNa86HbIEdknccv6Wi92vQJBZ8swguNrJjlqOA1sP2hFZxRgiUwyK8Kfmgb7SyNQCLUd1KXpPZa5Uc8MMCH2J8KsOMwZLBPpTXnJ9WgqeHm9XmX5uyDTuF7Fq4XO9LvvXX3dqENCFdhF9q1NR9-ZyslH4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هیچکس نمیدونه چرا این پست انقدر ری اکشن "
🤣
" میگیره.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/81240" target="_blank">📅 14:10 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81239">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">اوکراین چنتا کشتی روسی که محموله های نظامی ایران رو حمل میکردن تو دریای خزر زده
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/81239" target="_blank">📅 13:53 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81238">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">شهریاری، گوینده جمله مگه تنگه ارث مامانته:
متوهم ها باید قبول کنن‌ که آمریکا ابرقدرته و حریفش نمیشیم.
پ.ن: نه مشتی صبر کن رستاخیز بزنیم آمریکا این سری دیگه از خاورمیانه میره
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/81238" target="_blank">📅 13:40 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81236">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q_d144NU4lDUeJLF-7VZ7t6ybrVuZ-rTb-qdC8UTUpD7g6GP0c7EIf_ETySgBtqCi8-vFt2RSxnBnu80lh-ZDuMOnTEnh26q9N0_fst72IB1CVg0rf3TuVhqjb-hgOwPR4TfGFqdSIfGRE2hdMks2mSK5NrCvdoBTiuiBzJoeccUSKpUzppl9fvaA0UrHAypilEdE0CZc9ZKV21OITTKMn0sjSx2GRxXLErxfiyyJkLiI_C0-GGCv4vem_fDIpF-sqebnqZGuL0-8qI6e6I0uHHSxwGhUwtVqaOg5hWT5WT_j7E9uHRTfbqnnE1sa4cPLqsz8V2hmf-wepi3_EHXvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BdAse9oaBoLgpyh3F4HJchAyuodCTFaUHuOEAfMt3OCyqjtNkHg5JICFZROtKsGfyn5K_fciWWJzo6KwX-NHIWP2eyIxsMlHiipk_sI2UuO2arruhRhii9YKSVwvRcHKBcGeQb5f9gH8ef88AZZUDD9Hn2vZ34u5SW9Hn2LdKpp-womjO5f9MtKFrQ69xPFTWGDbb9mXzN0cp3GOA--ob7UqszdIJTTVXzpW3V11WHRalvgaW80NcLSdLU6q5FYsxk2IEZJ4FSyjQ_C7XWsS-gdfgax4zB7WUbCZslMXSukD9NM-U5zpmV_QnnJP2EOn8Ri3VvTi1Gl8BJV92IJlIQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">این اسب که فقط ۵۶ سانت قدشه رکورد کوچیک ترین اسب دنیارو زده
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/81236" target="_blank">📅 13:00 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81235">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">هوا گرمه کصشر نگید</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/81235" target="_blank">📅 12:01 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81234">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🔴
ترامپ: رسانه ها به دستاوردهای فوق العاده من توجه نمیکنن. من رهبر ایران که یه آدم قدرتمند بود و همه ازش میترسیدن رو کشتم و الان یه دیکتاتور همـجنسگرا شده رهبرشون. اینکه یه قوی رو کشتم و جاش یه همجـنسگرا گذاشتم دستاورد نیست؟!  @FuunHipHop | Jenayi</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/81234" target="_blank">📅 11:38 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81231">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c1e370de3.mp4?token=tG2umWAxAw9Su8lG25-8P7S9VR9kDpdU6qtRf1ztSx7XCWlmOK9DsVQIR0pnDQxFcZuciqHwqb-4TZ-mvyi33D31qdG0yOWbFFJhtp4EG8zAPQdMkX4HHeIX5PqBtg9MKbfVx0WFqWYdU5C-Jb6zeWJYCmqewLcvTe2L87hee2yXasNAuJB7zrB4FG6srEEJG9bsyWHsFvq4YUA7HV7cybKy5LErcG_0k8sP9GdvGsTI_A4KC1Bokk8oWsbYuf5jbky8rzIz39tSKpgFI9HA83rOLNm-TEB-g5H80iGrWiZmwk3qVuqFKlYZWnM_avrlY2LDk7oLJ6G2H-_bdqVX4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c1e370de3.mp4?token=tG2umWAxAw9Su8lG25-8P7S9VR9kDpdU6qtRf1ztSx7XCWlmOK9DsVQIR0pnDQxFcZuciqHwqb-4TZ-mvyi33D31qdG0yOWbFFJhtp4EG8zAPQdMkX4HHeIX5PqBtg9MKbfVx0WFqWYdU5C-Jb6zeWJYCmqewLcvTe2L87hee2yXasNAuJB7zrB4FG6srEEJG9bsyWHsFvq4YUA7HV7cybKy5LErcG_0k8sP9GdvGsTI_A4KC1Bokk8oWsbYuf5jbky8rzIz39tSKpgFI9HA83rOLNm-TEB-g5H80iGrWiZmwk3qVuqFKlYZWnM_avrlY2LDk7oLJ6G2H-_bdqVX4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
ترامپ:
رسانه ها به دستاوردهای فوق العاده من توجه نمیکنن. من رهبر ایران که یه آدم قدرتمند بود و همه ازش میترسیدن رو کشتم و الان یه دیکتاتور همـجنسگرا شده رهبرشون. اینکه یه قوی رو کشتم و جاش یه همجـنسگرا گذاشتم دستاورد نیست؟!
@FuunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/81231" target="_blank">📅 11:33 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81230">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n_cdde_jU7ONfCr1PrRAWKITpSk1eN84ZF-aqonFsqSkzbul767MmoSeAWUkRt9ucREBUv21el5dkl3M37Yw0_BDWQmrYBV_K2C3wHqFVG6KYhTdRaAO8e_xsC9CWEprSeibhREr00rmaAkr6qJJQcy07fOHKVpSG_HB4mDjX2C3tjOa7fdvEFW8y8PC6RYyxHdHk9erY8kFpAKQhaPUuP2sJHIPYulFkUiZa9338KLWxfsdyO6gObSmZ84AoH1MLxTD1K4r6Y5owTKyl9ndMzBHwKYsWEob-AbmoT1XHC-1hnTzX-BkY0PaGVVY_5_fJI_qLB-y3WGXtgt_5_RxHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
پورتو
🇵🇹
-
🏴
استون ویلا
🏆
رقابت‌های دوستانه باشگاهی‌
🌍
🕔
شنبه ساعت ۲۲:۳۰
🎲
با بیش از ۲۵۰ نوع آپشن پیش‌بینی
👆
ضرایب شگفت‌انگیز
📊
نگاهی به آمار دو تیم:
✅
پورتو در ۵ بازی اخیر خود مساوی نکرده است.
✅
استون ویلا ۴ بازی اخیر خود را برده است.
📈
میانگین گل در ۱۰ دیدار اخیر استون ویلا ۳.۷ گل در هر بازی بوده است.
🧠
پیش‌بینی آگاهانه، تمرینی برای نظم ذهن است.
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
r3
💻
@BetForward</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/81230" target="_blank">📅 11:33 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81229">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from[ Fun HipHop ](Mehdi)</strong></div>
<div class="tg-text">کانیه وست
😂
@FuunHipHop | Menot</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/81229" target="_blank">📅 11:30 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81228">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from[ Fun HipHop ](Mehdi)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nw0ORU2o-gvHwTA_bQfu-LnIy7ScuyoDfdOcoEZcz2-DHQmqTGayqJ-pnjsl4ho-21hJUuaaUeGeSjEt_VaonCJC6fIFOmt6rOsuorltGXWTd0OoEKzDb9Zjt0UYZtX5QCkQBtab0I8nHl8iqhKS-UzabgHhcdIs6OsbXSrbJqEHTk755KXINxuAGppnZ8mG9rMWpkw5J17T9G7oBp1GW5Gtj-BKBN6AG3JatPPho5gXNPtj0cc8kt_Btf42z7mb24E4WfefRnD2c0fweyL7jTUY0ONWf1n8M5L6gFW89gDJGxDvZ0DDP8XrC56adD78gi3BVmJm5KY1pxZh6TQMlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کانیه وست
😂
@FuunHipHop
| Menot</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/81228" target="_blank">📅 11:30 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81227">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">قدرت اول منطقه برق ما دو ساعتش تموم شده ۲۰ دقیقه تاخیر دادین چرا نمیاد</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/81227" target="_blank">📅 11:24 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81226">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">چین حجم تسلیحاتی که آمریکا تو خاورمیانه مستقر کرده رو دید و رید، حالا خودش دست به کار شده و قراره کنار پاکستان میانجی‌گری کنه تا قبل از اینکه آمریکا حملاتش به ایران رو دوباره شروع کنه توافق رو نهایی کنن
علت چصه دامپ تتر و نفت در روز گذشته هم همین خبره
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/81226" target="_blank">📅 11:13 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81225">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">یمن همینجوری حملاتش به عربستانو ادامه بده واقعا برمیگردن دوران ملخ خوری</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/81225" target="_blank">📅 10:07 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81224">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">یمن همینجوری حملاتش به عربستانو ادامه بده واقعا برمیگردن دوران ملخ خوری</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/81224" target="_blank">📅 10:05 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81223">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Od743QZDiaD05UqK6JJd_Ac-ka1c6yqomrKdZYT4BhnS4kr6VDlGQNpmIn38yZ74u6LdkaBXkJaJyBTFztMxecHJFyN7dNQWZZtYrO9XMGhLAyYbkkB_WyzR8trn6_Zjxz5wbgZ1Nn8U6tsaxN2PylDSExm7ZEyNjryMa_C1CgtYmBT5wfnhgWneFWveKCJ9XnB7R3eTIb56er_7t9-D-L71y3WTCCeH2kOjNe9WBUNm1GoisHsbVVeHo-E5T_Tp1OBVZG06-t7Ks63aks6G5hnMMM6kzjH3NkYqdREbzIeP4Uys7hpz-xAYW6LRkXy1qIZ2Rqp95nCPs8K5KFtKzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#بالاخره_یه_پست_رپی
پست جدید ایلاکه که احتمال منظورش اینه که "پوری خارت گاییدس فقط صبر کن" ولی روش نمیشه مستقیم بنویسه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/81223" target="_blank">📅 09:45 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81222">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SHm88q0-PKmlxWMgR79cHG6xcSnRO47WJ8YQXSgpXoJ8zCyMSXsy3u7bPsf_HAJp_JfCeey8-VOIpZ7btrjAZrzDfkxnkkDJ-pxBWIgYB-Jru-bV3GiCH4bpPRQX3MNxqXpSr_hSv2oYDfHlMnj8-DOZJEartUOqe1fE4WHpN0LLVTOjxK4qAsEwwpxOK4LXSwpuGUM7WDhmzGbHsfqoJB6tlJGNrJq812ZQEskAoNZKY_imnadlKRcw3A_7ovb1A-Kk0jCLV1aoNhLsRMkwZY5Tw65e9Kp16q9sc49eGqfI8akTbEqMz2pZGwA_A9xO2gHy8F5xW4fqW56Bc7n9Vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باور کنید اینا با آمریکا تبانی کردن خار عربارو بگان
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/81222" target="_blank">📅 09:31 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81221">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">این وینگری که رئال داره میخره از قیافش معلومه فقط برا کار تو مزرعه ساخته شده.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/81221" target="_blank">📅 09:19 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81218">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">لبران جیمز بعد از ۸سال از ال‌ای لیکرز جدا شده و رفته فیلادلفیا سیکسرز
تینیجرای ایرانیِ همیشه در صحنه، آماده شید جرزی این تیمو بخرید و مدعی بشید که از ۵ سالگی طرفدار این تیم بودید و بخاطر لبران نیست
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/81218" target="_blank">📅 08:44 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81217">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">علل حساب اگه جلسه سرانی چیزی صبح هست لغو کنید که اوضاع مشکوکه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/funhiphop/81217" target="_blank">📅 04:36 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81215">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">رفتم قسمت آخر برنامه ابوطالبو دیدم، بلافاصله رفتم هایلایت لوکاکو جلو سیتی تو فینال سی ال رو نگا کردم</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/funhiphop/81215" target="_blank">📅 03:30 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81214">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">شرکت هواپیمایی اتریش، تمام پروازهای خود به تل‌آویو را تا اطلاع ثانوی لغو کرد.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/funhiphop/81214" target="_blank">📅 02:47 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81213">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">امشب آمریکا نزد، من زدم  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/funhiphop/81213" target="_blank">📅 01:06 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81212">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">امشب آمریکا نزد، من زدم
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/funhiphop/81212" target="_blank">📅 00:51 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81211">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">عربستان و یمن همچنان دارن کون هم میزارن
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/funhiphop/81211" target="_blank">📅 00:41 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81210">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q6qdQQi7N47H8URtDEck8W77gMR-yW0lq9dPncOWxOjXjqWRjvGKmermG3ICwmOOiA9X1Cg3MnnQbSyuQd2fvoWVkgimftnrGCQwq8RpRXE78iC8BlbVqHJ2EV8BSS7nywCFKsGQ5eLw0j_B9iPujMPAKdj2oXfSJlzJMfXG_m_mqw6p-hydL8SzfksJDM79wt7vduhv_RBN9oPL73mKFc1OzasRp5KSK8WwIwc91ufFLC5HOB0LFNWgencuXZw700I3-3CJJsA7uP_l5zp2ZjIXyEsuCnvF7HLuE0p_BQfGDnmxAqf4e0w12a0R73OHGUS3EqxRmVr9q4epTiEEFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/funhiphop/81210" target="_blank">📅 00:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81208">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">کوسه و زیدی درحال لذت بردن بعد از قهرمانی  @FunHipHop | Taymaz</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/funhiphop/81208" target="_blank">📅 23:55 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81207">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P771ItwhQVzmnB6518FK7O0vnKbQ0tmClK2aKMQWr-Dr1XuWgjz0ZLj_ghcdb9nCZy1OuKHKV6ZY4fzHc86XJyKTFCEsEGy17EANam1e1bOfv71PrPcETkY366uS1l-219KDpB7j5mYYG7GqEvILOBxBBNQjNhGuZpC1OPNgkLp9qEqqbVmnxKQi52ZUBzrGQGsaGYn87mc3CVaTM-NqRQxYb6jD0Khq_azRwiy6NDLCGXXPzQtGJ3FjDIBsY_943vRlte8O68wgGdiAZukpepStgygNNFtwsDmyKww0b7gpKEvdYl0YoWCc_a59LhTg-g2TrONDQ5IQqLJ-C-pn5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کوسه و زیدی درحال لذت بردن بعد از قهرمانی
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/funhiphop/81207" target="_blank">📅 23:26 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81206">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">ترامپ:  مهمات برای یک حمله بزرگ علیه ایران آماده است. ایرانی‌ها باید این موضوع را جدی‌تر بگیرند.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/81206" target="_blank">📅 23:14 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81205">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">عباسدرمن: تو عراق بهم میگن عباس بَطَل، یعنی قهرمان.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/81205" target="_blank">📅 23:04 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81204">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/842d3e3bd5.mp4?token=Flj3SWIfFkU3GZ3ACnWZJ4P_qPcbhTxqZiv3kZvkTy5VlR45oJfqT4H8L1XTUCYdKjR4eZjAwvUT-2NWaC_6_tJhBT8ohCtlVRyX1-uwG19kOYls8KDtksLcCi56YqnWdmC6rpenXCp5BIqVXX4tsrFWG58p2qO_upD0jbqXGh9rhCG93nuFF_petHEsMOTTVRW2zX4Uht4539r8b5EMYdZFlDhIEQ8iHs3hpqbaJkcMJkMqYy73Az4CgFj9wXDx2rJdYkrIJRPgpWIhLUui0Jx8l77NJF9qBgHD1hv-xe1M1XchHzqvhW5oo6lw3k5OBXWKtLst3pKyIgqcSgBhYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/842d3e3bd5.mp4?token=Flj3SWIfFkU3GZ3ACnWZJ4P_qPcbhTxqZiv3kZvkTy5VlR45oJfqT4H8L1XTUCYdKjR4eZjAwvUT-2NWaC_6_tJhBT8ohCtlVRyX1-uwG19kOYls8KDtksLcCi56YqnWdmC6rpenXCp5BIqVXX4tsrFWG58p2qO_upD0jbqXGh9rhCG93nuFF_petHEsMOTTVRW2zX4Uht4539r8b5EMYdZFlDhIEQ8iHs3hpqbaJkcMJkMqYy73Az4CgFj9wXDx2rJdYkrIJRPgpWIhLUui0Jx8l77NJF9qBgHD1hv-xe1M1XchHzqvhW5oo6lw3k5OBXWKtLst3pKyIgqcSgBhYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آخرین صحبت های مرحوم در مورد وضعیت مملکت هم ببینید
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/funhiphop/81204" target="_blank">📅 21:41 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81203">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb669ee556.mp4?token=h7ZrCKbPN5oGaEOKoEafE_0aaxqWWo-0NuebCYgPoZ4mkD-xYZ8TebOSvjvXcybHkLgYG3B98quC8bHUJgNA0eBejwuw0d4U8_txsZ6Lm5jL0qhQ0xMUkk2U7oIulhuuOSTKGyhIaHcL7ABO13Wf22kfhorHUSCres8ILxzpUSNDsYIQV9CsSBKQxFtoaneCnw_RjJp4wU2DhLjDmBsBi4Hgsfpw3vzg27PIoT8PLv1PZUUtlUYANGSN6Lh58tuN_dEWw3f-iwx5i88Ik-yKEmduAZg4mktgZ-4Z53aeS66LliaQWMhDtm-hw_Vp_wU-B0EH7LSZRGxQR32uGBov30_aI-4M-pZtaLyKm_ObYWrwX2T8nVBTIcmjkSNd_UDDlovxVQ9gJlZxf9Os2g-EJrRGjN1_F2NT-PhXqv14lxtysql7qbUdNkpO43HiVNoemqdcQV1IIRIpOPboQLy84KBayY83vPG-csPU7V_EpwIs1SqchvxeQ7OFr09JTyrO4tf8TRhho7Gpr4uQr9LU6srGmWH36f4Mur0hsrsFogoVjzsnrR7ZeIm7jQm7jYWJbhunICj06MOduCjI0eVpQMqk76Q2saQFHTxYh_X5obrLx4WAEmF_xzHJW5dYbvvyn0IIccFt5Ixvhe3_lS4DFc_LUIUgXdcl5mtdkoUE5Cs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb669ee556.mp4?token=h7ZrCKbPN5oGaEOKoEafE_0aaxqWWo-0NuebCYgPoZ4mkD-xYZ8TebOSvjvXcybHkLgYG3B98quC8bHUJgNA0eBejwuw0d4U8_txsZ6Lm5jL0qhQ0xMUkk2U7oIulhuuOSTKGyhIaHcL7ABO13Wf22kfhorHUSCres8ILxzpUSNDsYIQV9CsSBKQxFtoaneCnw_RjJp4wU2DhLjDmBsBi4Hgsfpw3vzg27PIoT8PLv1PZUUtlUYANGSN6Lh58tuN_dEWw3f-iwx5i88Ik-yKEmduAZg4mktgZ-4Z53aeS66LliaQWMhDtm-hw_Vp_wU-B0EH7LSZRGxQR32uGBov30_aI-4M-pZtaLyKm_ObYWrwX2T8nVBTIcmjkSNd_UDDlovxVQ9gJlZxf9Os2g-EJrRGjN1_F2NT-PhXqv14lxtysql7qbUdNkpO43HiVNoemqdcQV1IIRIpOPboQLy84KBayY83vPG-csPU7V_EpwIs1SqchvxeQ7OFr09JTyrO4tf8TRhho7Gpr4uQr9LU6srGmWH36f4Mur0hsrsFogoVjzsnrR7ZeIm7jQm7jYWJbhunICj06MOduCjI0eVpQMqk76Q2saQFHTxYh_X5obrLx4WAEmF_xzHJW5dYbvvyn0IIccFt5Ixvhe3_lS4DFc_LUIUgXdcl5mtdkoUE5Cs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بنده خدا حتی وقتی اعصابش خورد بود هم ملت رو میخندوند
روحش شاد
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/81203" target="_blank">📅 21:34 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81202">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">اکبر عبدی درگذشت
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/81202" target="_blank">📅 20:57 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81201">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pQRZz7TYv7v8hkzmmT9APcoea65vc4CpNaKzDO1iDrGi_AZ73_8df68Tu0Gw774UEXcIE6Dn-DC1jXH-0NPUGXLW9av2r52H7iwWlT-4uFAOwEdSIVDzOwcIDYHgs9u3qwSdCKhKUvlui4uWbBaFX32TjgCVAmts4rSylR2U-rioEi6Njc60yYkAvO7H3MDbDTDW-omFdORKHuLCPQG-W0WhAICQPjNSIJNlrMeTsaWeu56ivUPNxpFQyPW0k-ZjsL7UYXeFQ7BKhO3K6XExTGdvw53Hf9OsjrBDBgBZlH8eQiqeZemqHa_qwUO42sNIxHCpF9kTnptTpg9ay9wzpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ریدم این چه سمیه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/81201" target="_blank">📅 20:52 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81200">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">تنگه رو مفت بدیم بررررره؟
مال ننته بدیم بررررره؟
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/81200" target="_blank">📅 20:16 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81199">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k_J-7AMN69DFTKO5akxr7sH6FdKPNh-Ltbe4tWmYa3Zglub70y2C53tXoM1IgaTuw3bfIFWUy0FwxX7P8m38hhqaFjJzA-O3viUIDDmBwY-NXnZjWZA7kW99wy8P7b6o6SbJgPxk2hjzSmu4aWC27gPPzmLYQyR0N1RLr_p5POZoLWPfwGxYKiNP7DFZjGNnwi9uX3wJ1YDRd20VlxWzeAFAmVCg08a0f8s6IhF7HOob7iiVxDKI_nW5llSEcGHb3ExRI5Hr7a41seJPhwOSIqMysHWN3R4F-SZFlMMQFBHe0eL1AvIVuzf7_N7r59c6eRawgLdcCsfibkrfnDqgUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از این مقایسه ها که خیلی دوست دارید.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/81199" target="_blank">📅 19:07 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81197">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pfIAqerd7f-jKfAH8GXggmBA7R4bp5bJlYxUJi-PXZdeTYD8SCH8Rg1ulpbmKPWtmEH5imSqAF4W9EBefb--2OMRSk4_8--eWDJcRUdix2BXU9X-si1V4hQSxgzOJ1RnwChaKqvBpJtwwTI4-KveoM_KJZju8eOUwT7o8oEhEuXtHErWGIT68Z3WgwasxCclLaEijDbvniAy-cxrDadvzhK3BGSweAQ08CjdfpdhKH3eDOTsjJ01-xoaIxJgpb7mH_aMkTztAAwBGeY0d2TvGN_y-mDUmnf8Tpu1w9rY9rEWGAT6uxA0YrWOyPCY-DRbTho7ujM896NuvpRe5fNRww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینم از مقایسه رونالدو و مسی توی جام‌جهانی که خیلی درخواست کرده بودید.
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/81197" target="_blank">📅 18:28 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81195">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/USFbPKfjsQKlATZtdeFjJCNwRsZAEPD700iR_agxNUeo_CpkHKkOBZLn4MS6YEyE_cPXqcFoWD46Vduv4BVuTtD2hB8JoZWU05-cCVc_eZsOa7vg5c6bM3F5hrmlIU4k2P06a7T7FxRVVzeiW4JI3-7NuOo40IFqpQLc6SPEEgpefqkPXCPRec7D9oEowAY0R4kYFTnXLz80mOmIY7wc5oLFWM9hrAH4HdoxtOv7InzXrjk8FEi998J5bgI_qpxOSdbEOCa25NotOap42k8k4NiEBcXMQl8wKyfHP7W_G9MghXF4MJBwY-R3jOeWRMJKgmzSRJ5PBbSOHJvZl6I9bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lGkC-_M4i8ClB1ISfHePyp0jW6Smi_hrZckQEQuUUqXz-KoIwYnMapEUgdzGIKP93ngU5SYHDebEjJJpduqN0u8t9f-aDLdLhCXL2qWIiGL2akRR_4PqEbrXdUJOBAm2Wz-5q45jhIHsbNNPN_mahr1NOnd34vFFPxnfmJE_itqJVuKYHyrdffxVBZ-DQIt3Xulg1nf-Y9NJ6MFkA_GiqUIKB_j2gkhTNdQMVTMnNLJukseq4csuyhsHy8O2OnjaWkVOfuRHHE4wG8hP_ItK8JPajgC0vh0Psog-erlWlkYn3N1RKcw8AYr1xkxwxMJnoi91PTkKR0Z8lTciEK1d3Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">زن مورد علاقه رامین رضاییان
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/81195" target="_blank">📅 18:07 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81193">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">۰۲۱کید داداش بخدا ما بخوایم یو‌کی گوش بدیم انتخاب های خیلی فراوونی داریم، چه اصراری داری انگلیسی دریل میخونی
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/81193" target="_blank">📅 17:45 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81192">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dp4wV0EdmmPuCqcdTaA-7U22SC3B-eEcz4LhzJVwTT77bSba0jP6dp4t7MBVisvWXRAzUajwgxCBiwO1xeXXbeUhTLf61F4NW2HYUZe9EhXawpzriKATGkeyDVbpuUpY2LnVo2KnPYFUsWRegWD38mxG53ccK5aiOGPy8ptdoaTKEAnvYjAqQwBuorWpkC4HuEhgTN5an6aFBS0Oq6GoGBr_muHBssMRMCCMxMTxpDRChqjr2H2nBmNxv2dVzG0BvNe7BwQb8Q8LRr8EhJxQtLSaGe5QoE77tqhDpa6s5iENikmUCfCY8W8Fy_rvmsgsl2TeVZS_75WOuf8dZ87avw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/81192" target="_blank">📅 17:27 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81191">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uJA6zMxcRwBqNQ0WzAFhsi93XQ-2Wu08Z2p6an57X7JBAnX244wQ-udLIKraJa92AmScKj0NpCgz66koIvwc5OoTLDs6AiGT5FEBQAJwf1Ss_S2pPlL7o_4PftElaN5FOABalqXupozsRsVM1ALYSB_QVdJfv5ypGc-2Gufr-ch7uMYd4DrVE8BugkR0K57dYVFt4bVnxFobYRTpGdvXm1lWpXF-3VhuxJA0x7MSUJLUH_FMWLYCVIDrmJ6VfwKlJ0de12oypQIxfPbNHGx64q97ualNpiytDeOweNSYKWRgm9bZk_KYgwfVpqU-xey6GUhn4EILjCDbal9X_wodCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بهترین عکس جام جهانی 2026 از نگاه هواداران فان هیپ هاپ.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/81191" target="_blank">📅 17:07 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81190">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/meX49jVBd50010i1pikZU-3yDFTUNRS1yxDAepjTHwGGd7icVtCHpCgVF1UmyBCZpnA51DSRqDzzV_HdCr85L4THyrbmixydoFE5iPCvydG__k_0OP5Rtxp0U4Ic3W_2ymEYyoHAlzw2EhFmKh5-xJfwNsTkQB3wBG0EiCiB9ueGbaxTVXsf1HFiI04pZITEVx26cwVoc27EO5pYBlhba72A1IQx4KZvwQBIAHfT18MgqxkY-Xil4QTpF1CjAS2eYcdhnx36uWbSY9uMWWBOSl1JNYTxDHqbqlBcaiFSYcx6KY-n3F3psMiR47y_x_QKTrTHU2u0GqNOsRpmXJeTOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این عکس مسی بهترین عکس جام جهانی ۲۰۲۶ از دیدگاه هواداران شد  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/81190" target="_blank">📅 17:00 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81189">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tp8kXi6tXUr4AnkhBbZp5LO2IHF1zjjFUTUkbbUcl2Pgni-fWKkw-sysawNhlTS8VY1S9HKSvVq-R4UaChQcCRr4QMQlQuZh-VeVy1YBXvxTwB619gNl-vEfWDJ0Y7bz87SSOrzsPIa3jQbW0ZWZU0WCXI3uTBNuQtUDaGU20n9Sc1ODNauuUV_Hjqi-VUO3p1vhhtRbKEs5YgTNzUFPJQiQ8b1T8Nmr21LnrEdDb6kHQT6vgDl0xunWzIG8pmrMmRFLRYug-pSz9q4tlRROSEVgCs2IMTaad1U9phDzdSj7o3mI2qaNxiEpH_MUDOgFVwWGxTzr9b7F6SdyuJg9lA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این عکس مسی بهترین عکس جام جهانی ۲۰۲۶ از دیدگاه هواداران شد
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/81189" target="_blank">📅 16:53 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81188">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MsE8zOcK_yiZknJ645odXXB1p7V47YYl96mivRleuScQ34ZUBsBkkKu3WjlpJryRUpM4YYn1WFYLJxFN7o54KliyYPA1ckNv2W33tULigeEH1H_U-iMosmqtWbkU8b1VIsWzI4U0_wq0FD9RinlodBumtuRtfA43OAG6felmEUv6P05pz2yBdZODbUOy1c9XV-e2XeZUcCIsnyE2kJyKBz9OaXJXQxgPhQct-x_LAtoWKfDpVmsRFcWnA0nSq8nb9KKPBugGXqY4eaOzvK4a7eQpoXb-LKt1i3GnjJoSa1hitqBmNaNEHLQ8mPk52LmZ-nMP1Tt2S2WFMJPmCUuU9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وضعیت بورس آمریکا تقریبا مثل قبل از شروع جنگ ۴۰ روزه اس
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/81188" target="_blank">📅 16:33 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81187">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pQ-8c3s_jREDtd0PGrnrCAU19kgwdkjBd_NQXCeDrZA7m0f7KzHK5xECqhq_60z9LF7YCGtbNTTvW6V1q9DKlh_s0UF3JynH5b1JPdLEXNcYZqoKyDoRsk3IuGYjxmEdC0Lb0lmvTdsDfAIuO8UYRckwzKcQfXRxUxq6qqB8VS_z445GArWstFzG8h6dj86Q3Wpl_dGkCimOZeY5rwKlYD6DJVrC9ueEe-r6C1pUBX8szNiC27gd_f3cJS0uomkDsU2eueaDg5owP5r0p1QCrox38EtlUqEyCdKtTY8neF23CPIm3svHHKfnfiOIBK3QGyWzLrX71orww4-bfhcPeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان کوکوریا زمانی که بارسا بودم موهاش همین شکلی بود، پسرشم نهایت ۴.۵ سالش باشه این که میگن بخاطر بیماری پسرش موهاشو بلند کرده از بیخ و بن کصشره.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/81187" target="_blank">📅 15:58 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81186">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">اختلال تنگه هرمز قیمت نوشابه رژیمی تو کشور هند و بالا برده.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/81186" target="_blank">📅 15:43 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81185">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">دقایقی پیش ادامین فان هیپ هاپ از من خواستند فورا فان هیپ هاپ را ترک کنم.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/81185" target="_blank">📅 15:34 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81183">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">وزارت خارجه آلمان از شهروندان خود خواست فوراً ایران را ترک کنند.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/81183" target="_blank">📅 14:45 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81182">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">وزارت خارجه آلمان از شهروندان خود خواست فوراً ایران را ترک کنند.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/funhiphop/81182" target="_blank">📅 14:34 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81181">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RUs_Zy4XmUxexW_BSd0eZWvXx0C8F8aa6LEAih4oC87nk7bKcoUyLOiYfPQc-no5XJoB9PaAl5QI4ArQXFDSlYckzNGRT2rlUqrjsjn-8TvO0hj68kj8VSBeL3nfbu4by8Hc2gV_drGQ67p6avCB8k8YBZFy_3iPy_XgWfWAARs4e2sA2zIciPpMsR1_KdTTRAa77oYnoe9vZmbdRSlLTUwuNj1dOj7TDZOJ1zmYX5aKRY9rTAWdke7MnG-fXKOM-OI73nY4nExV4AkUvk_c9h6RRoyC02KSm5q9BTlRhYTjId1QWHs6-0zr_Zcq0vYcaWE4Zh1ilGwFiG9aTQApVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خداوند زمین و آسمان را شکر که زبان فارسی را به من آموخت و اجازه داد آنقدر عمر کنم تا بتوانم این محتوا را با چشمان خودم لمس کنم.
🙏
🙏
🙏
(
معرفی بازی رومیزی نجات کودکان از جزیره‌ی اپستین و رساندنشان به بیمارستان خاتم الانبیا سپاه با طرح جلد کیف صورتی معروف دانش‌آموزان…</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/funhiphop/81181" target="_blank">📅 14:09 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81180">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/6bcddf257b.mp4?token=WBAuMv-wXTO4_mZqe0uwL1CRgL8P0DTf-jg5f-6vqZ4hIKyuf2tuSv8wDVOkpx_6VBtqK0cgksgRvl0FcQodQjAG5s1jYdv1YjaFuRooRfiQ539GO7mEQ0Ln2AqpkqkUo6h7ZZVERe0X7PWhB6tmYYKEK5SLcU9yXsNTpcCaas8ujjgYaSQhpa-lnuvpZdDHTonArHY18ODZMuO0D8a4dBkDcRTvzMGG7nKVAaZ1kPY5naXE5MQ6ROR1rfmi3nQHuHE_QOt3_aRqmFRu5z_OAC4IgUjn5YbxSqKVWMu_caJpjG0vamJcE03fYFNh9RPtUZ4rb4UsewyhsGrv0U0i2A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/6bcddf257b.mp4?token=WBAuMv-wXTO4_mZqe0uwL1CRgL8P0DTf-jg5f-6vqZ4hIKyuf2tuSv8wDVOkpx_6VBtqK0cgksgRvl0FcQodQjAG5s1jYdv1YjaFuRooRfiQ539GO7mEQ0Ln2AqpkqkUo6h7ZZVERe0X7PWhB6tmYYKEK5SLcU9yXsNTpcCaas8ujjgYaSQhpa-lnuvpZdDHTonArHY18ODZMuO0D8a4dBkDcRTvzMGG7nKVAaZ1kPY5naXE5MQ6ROR1rfmi3nQHuHE_QOt3_aRqmFRu5z_OAC4IgUjn5YbxSqKVWMu_caJpjG0vamJcE03fYFNh9RPtUZ4rb4UsewyhsGrv0U0i2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خداوند زمین و آسمان را شکر که زبان فارسی را به من آموخت و اجازه داد آنقدر عمر کنم تا بتوانم این محتوا را با چشمان خودم لمس کنم.
🙏
🙏
🙏
(
معرفی بازی رومیزی نجات کودکان از جزیره‌ی اپستین و رساندنشان به بیمارستان خاتم الانبیا سپاه با طرح جلد کیف صورتی معروف دانش‌آموزان میناب در صدا و سیما.
)
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/funhiphop/81180" target="_blank">📅 13:43 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81179">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">یک مقام ارشد در کاخ سفید گفت که ایالات متحده یک برنامه دقیق برای سرنگونی رژیم ایران دارد.
«اطلاعاتی به دست من رسیده که بسیاری از افراد از آن بی‌خبرند، و من می‌توانم با اطمینان بگویم که ایالات متحده برنامه‌ای برای شکست دادن رژیم در ایران دارد. کارشناسان بسیار متعجب خواهند شد و سپس خواهند گفت که همیشه این را می‌دانستند. به سادگی، به آنچه اتفاق می‌افتد، توجه کنید.»
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/81179" target="_blank">📅 12:34 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81178">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/meAiLRxJeQkLjiXm5RQIsYjrH2_I1jOuq1In6JiEtSOa_Uk8HEzyozoAt61HSqYReKIei1pmqM1O1W0xbU1wBHZ7sr-ghBvsTEwX0zsdHTA-krUKrZN8n9YqicPuZJ42YE1Uj572Ys5X5sxdiHDeseKvOhmokpKLBnd2-kbuv1jf52A900PWiWDWBcimZU31zkGndi9LyUhWlrK6BAbt8X6bwjqVaOu28NCknosUs972NIXN4qOMZUPCT5JnbmYZ4rYbbxbIJlwfJq1ZXQ_ACvlwX1LazuNxzAE8XvH04sPFswY4D6rYMtn2j3ciH1Heb9i61n_qnpXhT9LaUdgrXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه اهل وسط زاگرس نمیشیم یه نفس بکشیم با اجازه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/81178" target="_blank">📅 12:03 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81176">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FM5ULDckID7MT4eORbP4Mnrz2WDr1dnnGnp7dgKPHtW7Cj5QzPtAKd0jxlQcn5ktQg5gEPNbGhxAShnr66hhN4Qi9D_V3soZq2omoH-aLuTmNMKG7G-ykkKUWmf1nnYV7fossH0h4Fo54R-8vqnIEgCLl0wmGiP5VAxTdOQliPLMBOhxK2ungvh9iUWBOuVVhCfqfJRvYvGEe8wByd450XTI_f5-GxCyjrL7NMaun4iEWGM0NTNB8M7SYSYnH8XjlRsIZQTUAKQdd36RbmsVygQfzUUjvdhAT2UAR0DKn7sUhl6mpoOUbsoOozOFOwoAWvtSh9D-92QPER-dddXZ6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان کوکوریا زمانی که بارسا بودم موهاش همین شکلی بود، پسرشم نهایت ۴.۵ سالش باشه
این که میگن بخاطر بیماری پسرش موهاشو بلند کرده از بیخ و بن کصشره.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/funhiphop/81176" target="_blank">📅 10:36 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81175">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">حملات امشب آمریکا هم تموم شد.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/funhiphop/81175" target="_blank">📅 05:20 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81173">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">فیروز آباد فارس صدای انفجار شنیده شده.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/funhiphop/81173" target="_blank">📅 04:30 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81170">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">وای
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/funhiphop/81170" target="_blank">📅 02:46 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81169">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">بندرعباسم زدن</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/funhiphop/81169" target="_blank">📅 02:43 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81168">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">اهواز جر خورد</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/funhiphop/81168" target="_blank">📅 02:42 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81167">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">باورم نمیشه ایرانیا دارن از فلایت رادار مسیر حرکت B1 آنالیز میکنن  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/funhiphop/81167" target="_blank">📅 02:31 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81166">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">اهوازو زدن</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/funhiphop/81166" target="_blank">📅 02:30 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81165">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">اهوازو زدن</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/funhiphop/81165" target="_blank">📅 02:29 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81164">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47a5b222b2.mp4?token=O5bqsIJ0WZnE01-wLHlqO93tB_QnaH71Asfq5sIpbYuOjn9UHDBAm-ga1UxLlSjYNt6POCdcsJnqXP-IRTP824sLgjbQBFFBvHCxwebETCsbGZRDbJVKRBBem2FmoUjDnglg46_Iu0haLLiylr_2lt1_a0vYKZ6LjsmYLMzcktAM1eMUnku6njvO-YvryYUbaykWtwKK1NI98xJ5VShfM3LTISiCxupwcGVQdogNoAFimHqbLeibu_J21WN9MXeZfxo0Rlg9hEE6ysukUUk0TALPQsnt5JwDGoA-851EpfrCEJLTULoJyD6h4zIx_hB_E1J4C1ceHiRrZQoQOKR8dQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47a5b222b2.mp4?token=O5bqsIJ0WZnE01-wLHlqO93tB_QnaH71Asfq5sIpbYuOjn9UHDBAm-ga1UxLlSjYNt6POCdcsJnqXP-IRTP824sLgjbQBFFBvHCxwebETCsbGZRDbJVKRBBem2FmoUjDnglg46_Iu0haLLiylr_2lt1_a0vYKZ6LjsmYLMzcktAM1eMUnku6njvO-YvryYUbaykWtwKK1NI98xJ5VShfM3LTISiCxupwcGVQdogNoAFimHqbLeibu_J21WN9MXeZfxo0Rlg9hEE6ysukUUk0TALPQsnt5JwDGoA-851EpfrCEJLTULoJyD6h4zIx_hB_E1J4C1ceHiRrZQoQOKR8dQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فارس: یک پرندۀ ناشناس پس از اصابت در آسمان جزیرۀ قشم، در حال سقوط است.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/funhiphop/81164" target="_blank">📅 02:21 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81163">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">بمولا این یکی یعنی تعویق.
ترامپ به آکسیوس: جنگ جدید با ایران می‌تواند از عملیات خشم حماسی که 40 روز طول کشید نیز بزرگ تر باشد.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/81163" target="_blank">📅 02:11 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81162">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">ترامپ گفته ایران از این به بعد هر کشتی که تو تنگه هرمز بترکونه، خسارتشو از پولای بلوکه شده اش ورمیداریم.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/funhiphop/81162" target="_blank">📅 02:06 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81161">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">باورم نمیشه ایرانیا دارن از فلایت رادار مسیر حرکت B1 آنالیز میکنن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/funhiphop/81161" target="_blank">📅 01:51 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81159">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">انگار قسمت نی اونموقع بمیریم، قبل اون میخوان بکشنمون.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/funhiphop/81159" target="_blank">📅 01:18 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81158">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j12BqHxHyMF7bAR177iQ-CfDBcyM-jpLJv-HuUpDm_k4p2ntnHD0wcXrfy-31LvM2no65cR7JPDBazXHp7FrxzK8QQoEJYF4edFsR-O_O1CskkVfSgPdiYGcTdXBMHYJoNZpSMZAMwDBZUSa8svwFgRdLS8Im59avwCxrFYVFQsD73XKDlTi_iZJNbV9H793DWcFCQpHdUqzf1JVoY1nPdmnCKRoTlPImw_-UtI2VHwiNrwtF1_v4v_ooXp0rRGCb_qLPYI6kobzp9KisHNgK3Pf0lISFkcRHySVwXXNbnckCWKuhCUGxczm_v9eksEPcXzogLqffBvXQEJ2qGP2ZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">5/5/5 نزدیکه، تا دیر نشده پلن بچینید برای خودکشی که دیگه از این فرصتا پا نمیده.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/funhiphop/81158" target="_blank">📅 01:08 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81157">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">5/5/5 نزدیکه، تا دیر نشده پلن بچینید برای خودکشی که دیگه از این فرصتا پا نمیده.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/funhiphop/81157" target="_blank">📅 00:48 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81156">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EWi1eREYgGLClzh8JZRUo6q-hJo7Rcc1Z0XDxqjnXPLe2zBGsqEhEQsj-iw4XCWgPc2sPygbADdMnID-DSC1iyttM4ZkAnMtH3udrKa1J2Q7H9wCvTzJEoOjAr9cKgIlBBgVF69ciykRX9Fou9jTUvuBySan2Uj9J2k30mPaT7DLMWuy7-RhjlBeyRPGIXk5zq2oT6BSpjPqHhp1E_shA-pm4UpgqVYEGRS7Nef6Do5SlmCpZZRI1kH5jnR1OU2Jw7jUyE66-8S474aFoAyzEkObIm_CQNv9hoSepMZ5YP1-QzDRbsfo4KZmaL-FUokVy-asPLeDRMATDSCoA-GM0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منوچهر متکی نماینده مجلس: احضاریه پرونده قصاص ترامپ به کاخ سفید ارسال شده است.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/funhiphop/81156" target="_blank">📅 23:52 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81155">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">دخترا جنگ نزدیکه، لطفا مراقب خودتون باشید قربونتون برم.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/funhiphop/81155" target="_blank">📅 23:46 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81154">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">سپاه چند دقیقه پیش حمله کرد به کویت و مدعیه تونسته یکی از رادار های تاد رو بزنه.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/funhiphop/81154" target="_blank">📅 23:33 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81153">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">امروز تولد 33 سالگی نوید افکاری بود، تولدش تو آسمونا مبارک، روحش شاد و یادش جاویدان.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/funhiphop/81153" target="_blank">📅 23:00 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81152">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">کان: از لحظاتی پیش تمام بیمارستان ها در اسرائیل دستورالعمل‌هایی را دریافت کرده‌اند تا برای فعالیت در مناطق زیرزمینی و محافظت‌شده آماده شوند.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/funhiphop/81152" target="_blank">📅 22:46 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81151">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">ترامپ: ایران میخواهد از طریق مسیر دیپلماتیک به کار ادامه دهد اما به نظرم هنوز آماده نیستند و باید بیشتر تحت فشار قرار بگیرند.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/funhiphop/81151" target="_blank">📅 22:25 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81150">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">یارو اومد گفت هر کشتی بزنید یه زیرساخت جنوب میزنم گوش نکردید نتیجه اش رو دارید میبینید، الانم گفته هر کشتی یه زیرساخت تهران بازم دارید کار خودتونو میکنید، وطن پرستای زیرساختی نظری ندارن؟
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/81150" target="_blank">📅 21:45 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81149">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">ببخشید ولی برا خنده‌م گزینه‌ی تحویل هوایی با B2 رو انتخاب کردم هروقت دراپ شد قول می‌دم بخندم.
🙏
🌹
@FunHipHop | Nima</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/81149" target="_blank">📅 21:23 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81148">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">سپاه پاسداران انقلاب اسلامی به کشتی های توی هرمز موشک شلیک کرد
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/81148" target="_blank">📅 21:08 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81147">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">سپاه چن ساعت پیش یه نیروگاه برق تو کویت زده
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/81147" target="_blank">📅 20:59 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81146">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k3EIklguPRn14dowQXedukec0OM-rW7ZQYrfKoXPDEMxU1VpEPOxhbNb97K1aoLxqcHh-6BFWzw5-RZwOlv2TMJl3qJovM_D89rGf1yF9Fm7gI1qtg6DVPwEn4DGJSbBOfR6MZS609lcaz0sL9DV_ZldgOwh7GgjjuG0FHgdTKydZrLI0wezxytIls0U-oE3HZaeYWSIb-YAyuawNkU1VluayiKmfdwA5LNPMukcAOIDX_D10XPYKU_PQCIUAj-tTidhWXpWJBTzVIcJXErs6dOdtrQqb19ub6xYx4yM_VOPvdLWJxMvuQp7skBqO4PpkQB86EyoXJRifoM3xr6H_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یامال جقی قبل از معروف شدن :
@Funhiphop
| TemSah</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/81146" target="_blank">📅 20:40 · 01 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
