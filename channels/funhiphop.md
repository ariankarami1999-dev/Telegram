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
<img src="https://cdn4.telesco.pe/file/Wb-Ss0AqSTsFYj58dPUV2mO2qoM213g3lwYFUifnSBumLlKDHE83DeGHfF8TFnAFKOrm6PPcb5YO7G011Hco2jdosLJ1D9HGzFljKNFJ7Pgwt-5tB66NiQyyLxNZQwEmpsPeqn48j8nIDGYDniNTAsJwMoQFFiYGW0xXTzGSk7fjNEmkPES2h4Mw1D_kaAliBZ2tJ2XUOUBM02AdhatrewoRlligoo09ekpDESD_9J9LXsrRfwQvLhHaUlRPTNKcUN_Gv9IvS65waEpurPWt-89mvOHkJH3aSxeRZatOcczToWPfXq_ybKdVIRLrXAL3FxAqngUELrNZEx9ZwGOW2w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 171K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-27 00:53:57</div>
<hr>

<div class="tg-post" id="msg-78074">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aBPgEWvdz98N1Zv_DTLraUsIzrZKvaSs5EL4NISN4t8g30svwoOvQiR0c73Kx_5Aj7a3-38Uidi-ipDHzkNwk9HwZ-dtZdprBG0BcG7-_cZF9VrUEzGSbCMfeXAld9P9ar9TzN8TEGOUmzFmW8oyVe0BrFrZ9mO7wD5WsOFJsVgyvM2CDHLvHU3yQypiLt2CnF9SH1a3uO8lIXeOlcO_15dB5-gvDFhAJU_PBdggxf1LN1s56uVdTdXNH83ag9mHWcyk22Nf8uRZg0d_LksU4iY6Kde-hc4TwCJnEdBx55tqcqHatEo-5j7iwYurPSRfjlQ7RO9p1yilULihwbIC6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کصکشا از مزرعه‌ای که توش کار میکردین خجالت بکشید، یعنی چی صفر کارت
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 3.69K · <a href="https://t.me/funhiphop/78074" target="_blank">📅 00:32 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78072">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">قبول دارید کسایی که جلو اسمشون پرچم گذاشتن زوال عقل دارن؟</div>
<div class="tg-footer">👁️ 4.29K · <a href="https://t.me/funhiphop/78072" target="_blank">📅 00:29 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78071">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/guSLL-OOwuKLZDhAc9Wsca8IjOkENKy-j-_9TMXoUcgVd0yEG4tgQaYCwPc8vjBNDM-ixyOKWVejcv9xFZZ1aHVT5MPIrEDWy6wm_Da0yQx7j4aGL6GWnkOfXtbfyy5_KQyTU3hqSSHU9SeVjfzArSnlFvyvKuNqW1zvCdIjg0GsKceksEwvOKXJJwd4mLGX8OaqQTTg99ZapYJoV2clgSPznc8gH15HdRISjy1uMqNooVYRS931I7JgEkzG5TMnCPGjoZ0woIWQin8T1LNofCZHoCoK8J5GbOBhTe793HeDHsAYHOxOImjlzBWbycfqfNFmzZauscRD8-EbzbOYiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">احتمال قهرمانی ایتالیا از پرتغال بیشتره  @FunHipHop | Farid</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/funhiphop/78071" target="_blank">📅 00:28 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78070">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">احتمال قهرمانی ایتالیا از پرتغال بیشتره
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/funhiphop/78070" target="_blank">📅 00:23 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78069">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">بنظرم از بین آرژانتین، فرانسه، اسپانیا، آلمان یکیشون قهرمان میشه  @FunHipHop | Farid</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/funhiphop/78069" target="_blank">📅 00:22 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78068">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">بنظرم از بین آرژانتین، فرانسه، اسپانیا، آلمان یکیشون قهرمان میشه
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/funhiphop/78068" target="_blank">📅 00:20 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78067">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">گل دوم هم زد فرانسه
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 5.49K · <a href="https://t.me/funhiphop/78067" target="_blank">📅 00:16 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78066">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">این جام جهانی احتمال زیاد امباپه رکورد کلوزه رو میزنه
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 6.11K · <a href="https://t.me/funhiphop/78066" target="_blank">📅 00:06 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78065">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">چه‌ گلی زد سنگال که رد شد
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 6.11K · <a href="https://t.me/funhiphop/78065" target="_blank">📅 00:02 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78064">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">امباپه زد
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 6.11K · <a href="https://t.me/funhiphop/78064" target="_blank">📅 00:00 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78053">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">کیت فرانسه چه خفنه
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 8.85K · <a href="https://t.me/funhiphop/78053" target="_blank">📅 22:38 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78052">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">پسر اسکوادو نگا   @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/funhiphop/78052" target="_blank">📅 21:18 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78051">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t6okJ6oNRDEy-1WHA0RFLRYQ6t_EW5IYV6sg2aiJrEERYJ4NKUrSDqygVZNo1sKKXVf0jFMhxoc7XCofFjlmeuGlxmtOF3dRq-QUZKubwpmufHcMkVuBQeJySYHptPRGZ22lKsCBc-y0ZA0lIx7O6BDIQWqT7PZQFNZIzPI75_8Kg6bSa6loJL-kxmNhsRW2NdCljt3kZxno-SelBFU7OmudTxW4aDJmTYyxr67DjI8u_gkCwCvMWXX-ia_T8U4hFRs1tUW-Ar9hUoEA7rDsYA35DBhVeuudYpkgPy3n3S7y7PKPzcEbqWvZ_xxf_4xQ5nucXn77GD8PdXhF1sp3vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پسر اسکوادو نگا
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/funhiphop/78051" target="_blank">📅 21:12 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78050">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">نامزد های انتخاباتی در اسرائیل تبلیغات خودشون رو شروع کردن
و جالبه که همشون از طرح هاشون برای دشمنی با جمهوری اسلامی به عنوان اصلی ترین تبلیغ استفاده میکنن
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 9.68K · <a href="https://t.me/funhiphop/78050" target="_blank">📅 20:53 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78049">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">ترک جدید هودادکا به نام Best In The Game ریلیز شد.
🎵
SoundCloud  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 9.13K · <a href="https://t.me/funhiphop/78049" target="_blank">📅 20:51 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78048">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MvCk-grKLUpwGIXKRPKlHBWC2_23wxtuBpxNJL8LP94jObq9yDPeLl4Pf6fCeLx3tZTO1_M70eTbhBccYe8dggT9MuTHmlMKxUt5YRRQaeRoIEUlcmKSzsA9AZRMYo1yhpnPoRQvwLtdMxfmR5yZ9S25V-KqOc08XnMdsF8QHhIBA4DKm2CAttj2UtI0lr5SanlD2g_eb3cZrji1UubvUdufJUfPNaU5Olp8CdWWjmK2b24Fy6Idson-iYCv089zKxAh_udjpndd7XFmh-nPWW9uTTGL7qX78y4Op6jtZZAyqAIi2_Na2MpiZ3KlOzidbgoPuPkPqmc9SkYIzBZtZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید هودادکا به نام Best In The Game ریلیز شد.
🎵
SoundCloud
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 9.09K · <a href="https://t.me/funhiphop/78048" target="_blank">📅 20:46 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78047">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">وال استریت ژورنال:
یادداشت تفاهم آمریکا و ایران به ایران اجازه می‌دهد فوراً فروش نفت را از سر بگیرد و ممکن است تحریم‌های بانکی و بلوکه شدن پول‌ها و محدودیت‌های حمل‌ونقل را برای تسهیل معاملات مرتبط لغو کند.
طبق گزارش، این توافق تسهیلات تحریمی گسترده‌تری نسبت به آنچه قبلاً اعلام شده بود فراهم می‌کند، که احتمالاً صادرات نفت ایران را گسترش داده و امکان بازگرداندن درآمدهای نفتی که در حال حاضر توسط تحریم‌های ثانویه آمریکا محدود شده‌اند را فراهم می‌آورد. (لبیک یا اوباما)
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 8.71K · <a href="https://t.me/funhiphop/78047" target="_blank">📅 20:20 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78046">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">رادیو ارتش اسرائیل:  ارتش اسرائیل قرار بود در ساعات آینده حمله‌ای بزرگ به ایران انجام دهد که شامل ده‌ها جنگنده نیروی هوایی بود که آماده برخاستن و هدف قرار دادن اهدافی در سراسر ایران بودند. این حمله گسترده با فشار ترامپ لغو شد.  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 8.87K · <a href="https://t.me/funhiphop/78046" target="_blank">📅 20:10 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78045">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MSoQAuXWJ_pKIT37qYUx6ZzemGpXhbAMOtb3IzQrFFX4oVJu2cuDtPrkWfkSc_gWRC4RKVLJy4w796erXFGtZRlORiDliRHOFzuJWw_sCGtSF-cwGwvDEEJYcyWnxegSfLMC8frjM9QauoHXlLb7XEMzEqQrXmLQcTnoN0HezdwfoXwDMFwDSNsbrD7NcQHwQx4BXlqc3myfpkSs7zMaetS8ZI_gYzEqhhyRlpnqtKOADDt2c3A4PLqX-NQOaM--C3J6RvRHghYC9XjfHjywKfRGm64hDk3MaGMOwUZf8KnI-aRKsEA2LTD7QZOdho3M-z0uMX6x0aLhCzFcCasL5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خاله شهربانو ازت میخواد همین الان یک لیوان آب بخوری
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 9.33K · <a href="https://t.me/funhiphop/78045" target="_blank">📅 20:00 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78044">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cZVah-eooDnZXFK_qduNu6KqfVcCqEkr-q3KbqBaiTqNCQdWhmPd25iyleg8rPkKbvJxKrwPXs3k0rXs7WYn69Gnv9RBet1kZ-DkWbupnosvWyiYfu_IQJGTvh3xtULxnhFxaUfgVpsIhuiwQ_4Ls2B8dxpd_n4HAcRLPk0DVWaS6qVtxh-KbVgbjMK4Y1KVtlT2Ontc3SO9lIfvfev3uuSc6trt6RQlluw8bqBy3SHavYO5ldXl85lVHU2EzTpLOKZenlIhSIy-u49s6LgP4WWNEZdXkGj6RHDBn-QU_sOFZrFlt8At18BdcecPPglqjQbMRx0S87LTI8ALD1H4Nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوکو خدا به دالگت رحم کنه
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 9.6K · <a href="https://t.me/funhiphop/78044" target="_blank">📅 19:03 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78043">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fAn2hLrzK735W-6ZS-RPzyawNRTkPjw_MLT_iTLyFLcKt6pU_Tq5lvSQECb6kx2Ux5YgFJpuseMoziE9psBnzYujCX9uZQDrCSR_PcuIRha7FpTVM8gEAt1NwfTbufqLfmGElnJ-gFYj-GtW6NjrNQl2JlNQnIJaii_VVN9J8hlgpmRzqGEEfh1h2mEEh5iAbmmb9JCcfQYWOaGrhxp--rNX8LY-L2En79pS1SEo5Pt43xYlxbx3xqsz6ca2KyOT_jmkW4h2K-iqMhC9WXioeUOOuBbP1shYHrCTa7Uj_xuxHLzQdRGT1VEJ9dzAi29e97HMUeK51X_nMEu0y8DAWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 9.85K · <a href="https://t.me/funhiphop/78043" target="_blank">📅 18:02 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78042">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gLx3NXBBe8aD7ntYuNxLU8G2EVqwK5VQxUCqHhoL1c868hVHo9lHFqOzN-EAktYvy4FvONQ34PTsxX2EC1bp8HH-sWdc4gP75-v0BFtRAgbVLTNUeI0ho0vELBnevaeRJ0Ovzea8MeJmeNxl4p5Aoc_BBPtUXTjlldXb4NzyWmo0yYOgV3r2drKRAPZV0jMR8lAZeyksHnPXR9ngqvCUxF9mA7Uvz2LAUiPcqVJJY2wh8MJ5rQ_eMPpKsmVmaXhEccP1J8sRCQ3SErLFw7xN4Dt7VgO-NKWyqsByTO0UgVCoT46zf3O4doDFfGoa3oYgmmi-T9ql_vf97aKGar-mCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همیشه تو قلب ما میمونی
🥲
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 9.72K · <a href="https://t.me/funhiphop/78042" target="_blank">📅 17:56 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78041">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">با ماف بت از جام جهانی پول در بیار چون کلی هدیه هم خود سایت میده
💵</div>
<div class="tg-footer">👁️ 8.67K · <a href="https://t.me/funhiphop/78041" target="_blank">📅 17:56 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78040">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mjMq2oSlpT2Ow_8gTO2o-Z09mVksn83Eac22qfpGGHX1U73YtCWsgEsZXaBVYXWtLqf_WRSDgqhRToHSniqlFmciE-uGQAG_zDu1cr7-PaOQtGaIhGd_DHKuo9sAyVSmfs8QXPvmhvHHjhHcVYfighQG39BLH47gZZb1_kvx48yuHd_8zcJV-F2CyUhnIHqLUjgRtYXtdsZttwg7bde4OYdXshGCC00E2KgIPQeQwKJ2o7cAiJ27Vti6OEBWIDV8c6qN3LyuwKPj1x8N0_uPLwj3obsmPQa0yPanDugM7DIqdqs-J7MBK_T8uZnhIqP72N7NsluRq6pwj-woMM0mfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
چرا سایت بین المللی ماف بت بهترین انتخاب برای پیش بینی جام جهانی
❓
1️⃣
شارژ و برداشت اسان و سریع
2️⃣
پر اپشن ترین سایت فعال در ایران
3️⃣
دارای مجوز رسمی curacao
4️⃣
کارت به کارت همیشه فعال
➖
هدایا بی نظیر ماف بت:
👇
🎁
100% بونوس خوشامدگویی
🎁
برگشت باخت هفتگی
🎁
هر روز 100% فری بت هدیه
🎁
هر روز 20% شارژ اضافی
🎁
گردونه شانس با جوایز بی نظیر
👍
با فعالیت در ماف بت طعم واقعی امکانات در سایت جهانی حس میکنید
👍
🎯
ادرس بدون فیلتر سایت:
✅
https://mafclub.online/fa/?btag=260368
✔️
کانال تلگرام سایت: g26
🅰
🔹
https://t.me/+3Zxs6WU7L_UzY2Fk</div>
<div class="tg-footer">👁️ 9.78K · <a href="https://t.me/funhiphop/78040" target="_blank">📅 17:56 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78039">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">شایعه شده که ویزای مهدی ترابی و مهدی طارمی باطل شده  باید ببینیم تایید میشه یا نه  @FunHipHop | Farid</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/funhiphop/78039" target="_blank">📅 16:46 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78038">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">بازی ۳.۱ به نفع ایران میشه اسکرین بگیرین
👍
😎</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/funhiphop/78038" target="_blank">📅 15:45 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78037">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">زندگیتونو بزنید رو برد مساوی نیوزلند</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/funhiphop/78037" target="_blank">📅 15:43 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78036">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">شایعه شده که ویزای مهدی ترابی و مهدی طارمی باطل شده
باید ببینیم تایید میشه یا نه
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/funhiphop/78036" target="_blank">📅 15:37 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78035">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf7f045c16.mp4?token=SelYTSpwXNffNH6q32vOMuPCb_uIhMj1GzrOstPIp9Gq15wgzZFY1hLd7-ey57k4Al09crl80WfcdfNyB7l_KsTbCBBAsEHrqbjfkcK_VWf_TG3Sx2n6Dr7H5umzxUAxY97g3NNRMWda6KfmhV762gJyyZA0wxP15vNmLsTgN1hkYENJqCzv89m1IeX52BCmPVfJ-fIIPXuoN9lvdR8Yl9dIlsl0cuGqKWtuymb99kgVrbz5ak02JzecwE3164AY-QmV4NuZAEZcGWD83FQfea-FCZf_dQ6JbpOlL1FiUGGr2DOS5j3qnsWoQZbIk7Zowqm5AJdbxlKEaeGTLTubew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf7f045c16.mp4?token=SelYTSpwXNffNH6q32vOMuPCb_uIhMj1GzrOstPIp9Gq15wgzZFY1hLd7-ey57k4Al09crl80WfcdfNyB7l_KsTbCBBAsEHrqbjfkcK_VWf_TG3Sx2n6Dr7H5umzxUAxY97g3NNRMWda6KfmhV762gJyyZA0wxP15vNmLsTgN1hkYENJqCzv89m1IeX52BCmPVfJ-fIIPXuoN9lvdR8Yl9dIlsl0cuGqKWtuymb99kgVrbz5ak02JzecwE3164AY-QmV4NuZAEZcGWD83FQfea-FCZf_dQ6JbpOlL1FiUGGr2DOS5j3qnsWoQZbIk7Zowqm5AJdbxlKEaeGTLTubew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/78035" target="_blank">📅 14:43 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78033">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BXtk02OVHd3r-o89dz3Iu7eryjb9HDLqM4xGjFf5f-JE6I2uLobzwkkSSv81hp3N0T_kzP9akVj6jFO9O_BNTSpswlSkbirttJ-OJnfyjR2zrQpufUMECzp53CxaykxE0D_idueR5hGWz2P6tRy3Gz5lKK5Zs26DvHopkz7PG8GyvdSH1hH4ZPVIuaRO8yM9lzvE4zQxapsj0A-kSQdMnd_8Z-bXBipPYUjYKQ-FvxiOKuJUDxaPTW2GOweMGghaY-ARwL6pEJn9rcQsjj43XtZKFK6h4wm-SjGuLrqGznm2x3FrwCT9F39G7w_vpKyK9ZdwMlwPtfqXtj8_xhaFKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5d3ef255a.mp4?token=bLk5O_TOHGmVXxnoyAmNMnRwU6bJr8_42yYRITnpN0NFoUqaHZwnQO2zOXh4bZuTJLCHDmIIOJsRpzZ-Bq2sivnwitUvglNcDhwE_--B9kWpvUm0ZZ0rdEutprkUdQs8TWSqBfX8URMsEF4r9Hcwgasag_oIYCUjzxObCOJ3w05bOu2mEFbanEZQw6hw1yfWBK6OY6n7bXCb5q-vsVy0VXz3AwkW4294S7NO1mElwUa1oudBohEo803406jXJ-k8Zm3HV9fm1S_EmRKOlaXfGJFFZN7AnvLGVjRBvzhEUQaldG7tHSucBaj4XBnxVn2PQ8ywkcwcuQ-BIjJaMKLqBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5d3ef255a.mp4?token=bLk5O_TOHGmVXxnoyAmNMnRwU6bJr8_42yYRITnpN0NFoUqaHZwnQO2zOXh4bZuTJLCHDmIIOJsRpzZ-Bq2sivnwitUvglNcDhwE_--B9kWpvUm0ZZ0rdEutprkUdQs8TWSqBfX8URMsEF4r9Hcwgasag_oIYCUjzxObCOJ3w05bOu2mEFbanEZQw6hw1yfWBK6OY6n7bXCb5q-vsVy0VXz3AwkW4294S7NO1mElwUa1oudBohEo803406jXJ-k8Zm3HV9fm1S_EmRKOlaXfGJFFZN7AnvLGVjRBvzhEUQaldG7tHSucBaj4XBnxVn2PQ8ywkcwcuQ-BIjJaMKLqBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اون وسط محبی هم داشت به در و دیوار شلیک میکرد.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/funhiphop/78033" target="_blank">📅 14:09 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78032">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kl97SvT6681yT6QuVdrVt4o76xcCbV8L_2wATUeTSvQTxjkvT_bF5k3tCZG2giC_RSC8Rcs6pfPCe9rdKnQphAj1m5Ahq1nzrnhFpT6VfelQecLQOb3YSVxgyOoBrVbVxxun8dfXdVnGtR7pUBT63hXVaQjZBdEDG20_Gc2divFeva6wWRMIbl7QAR9fJf2xIu9QNFqBWDL9JWJCqke7HlLtKFiOBApHkGc1rcG49dagA_r0fmjUNAPBY_DbZa9oSrz4GMv8nYEHrfelYVfP0DmfJoJQrZpeJoUMmXMYtQV6b_eY22a7bsseJou7kcA2MBvlxoZDG6FRzBhireLfAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی که از تحولات ایران خبر نداره دیشب بازیو میدید پشماش میریخت، همزمان پرچم های شیر خورشید، جمهوری اسلامی، لبنان، اسرائیل، فلسطین و آمریکا تو ورزشگاه بودن  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/funhiphop/78032" target="_blank">📅 14:07 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78031">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">یکی که از تحولات ایران خبر نداره دیشب بازیو میدید پشماش میریخت، همزمان پرچم های شیر خورشید، جمهوری اسلامی، لبنان، اسرائیل، فلسطین و آمریکا تو ورزشگاه بودن  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/funhiphop/78031" target="_blank">📅 14:04 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78030">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">یکی که از تحولات ایران خبر نداره دیشب بازیو میدید پشماش میریخت، همزمان پرچم های شیر خورشید، جمهوری اسلامی، لبنان، اسرائیل، فلسطین و آمریکا تو ورزشگاه بودن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/funhiphop/78030" target="_blank">📅 14:00 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78029">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">من به اسرائیل پیشنهاد دادم که سوریه مسئولیت حزب‌الله را بر عهده بگیرد.
@FunHipHop
| دونالد ترامپ</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/78029" target="_blank">📅 13:42 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78028">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">حکم اعدام جواد زمانی و ابوالفضل ساعدی از افراد اعتراضات دی ماه اجرا شد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/78028" target="_blank">📅 13:00 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78027">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">حسینی با یزیدی صلح یکساعت نخواهد کرد؛ قالیباف و ونس توی مراسم امضا حضور دارن.
@FunHipHop
| Sogand</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/78027" target="_blank">📅 12:53 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78025">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qSB0pOpEFHUwBmXdMBJGsf7fz815SubSCqz6q6c6KKB6DHzOzOnWTx3_BsvjM2vKmdUSu8v53P4ZuYXrIALbF1Pu8yLo8pWbZBsuBNPdfdVECYV6B_v8Pgelx3AjzNBaYUP7qfHMUTJdnTambxMSlPUw_RvSGyncllwbomaYLPd_wOt48mTRTYb1heISOhLncwUS6EWFFW6MXmbXaZELJ4SvGfqfCL5qhcoZZu4-I5ul7mxj_55n_iEFwFr9RjcvJzR_eDBUEjbqsO83knhkBAh8m0IugaRrXsH5KqlpN9yzyGhkm8uwkUTcq3Hx1UMx7b-pPDoxsfWZVQcGO4RIFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تنها دلیل باخت تیم نبود این اسطوره بود....
@Funhiphop
| Jenayi</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/78025" target="_blank">📅 12:40 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78024">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">derbybet.apk</div>
  <div class="tg-doc-extra">52 MB</div>
</div>
<a href="https://t.me/funhiphop/78024" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">📲
اپلیکشن رسمی سایت دربی بت
🌐
DerbyBet.com
💰
امکان شارژ ریالی ، ووچر ، کریپتو در کمترین زمان ممکن
🔥
🆔
@DerbyBet</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/funhiphop/78024" target="_blank">📅 12:40 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78023">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nWGR8lsyMX0pyrtWfVgykZyTC6rCaZpU6lE7nBSWkrrIBCc4o26R_Ci5KLnk32OXZPV4sBvw6XS-lEuuqGOYJwOxi-Tt7XtMQGlDNdrDGwZCfFFxTmDfKT0Xf-Ye45tfoQBr8ZBEMG75MzoiizjfmpdSDkRntITi8v7zAwMy4_jWR008bsy-iTZIV-DupTcAmbLTub_j01Nzo_NfWbnRvyfJ0fTg_e8c31pf0wD69bzqboa5uK8ky0xJv5syEk-_pQdXECnpQ2R-g7Qt0qtneqoBbh-sTF0epizKR9UwUeS-1Nc1c4gvopAZBa1ezC1b9jEcMM4fX2Cgaa7rkdRdQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
دربی‌بت؛ جایی که پیش‌بینی فقط حدس نیست، شروعِ بردهای واقعیه!
✅
با لایسنس بین‌المللی معتبر، وارد زمینی شو که حرفه‌ای‌ها بازی می‌کنن!
✅
آفرهای خفن ثبت‌نام در دربی‌بت؛ فرصت‌هایی که تکرار نمی‌شن:
⬅️
۱۰۰٪ بونوس اولین واریز؛ شروع انفجاری
⬅️
پشتیبانی کامل از همه ارزهای دیجیتال
⬅️
درگاه ریالی و تومنی امن، سریع
⬅️
برداشت‌های آنی و بدون معطلی
⬅️
پشتیبانی حرفه‌ای ۲۴ ساعته
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
✅
دربی‌بت؛ بازی کن، ببر، لذت ببر!r26
🅰
✅
https://DerbyBet.com
📩
@Derbybet</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/funhiphop/78023" target="_blank">📅 12:40 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78022">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">بیرانوند: اون دو گلی که از خط دروازه رد شد متعلق به چین و پاکستان بود و عوارض داده بودن.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/funhiphop/78022" target="_blank">📅 12:28 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78021">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">بمب افکن بی پنجاه و دو آمریکا تو رزمایش سقوط کرد
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/funhiphop/78021" target="_blank">📅 12:17 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78020">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">۲۰۱۸ بود ساعت ۵ صبح داشتم از گل خوردنا تیم ملی حرص میخوردم، ولی الان تازه از خواب بیدار شدم نتیجه رو دیدم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/funhiphop/78020" target="_blank">📅 12:06 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78019">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromDiscography ship(blue)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KDVU9F-9HFe948-gLYMUmH9HJfQUSRJ-Q-XzuyyNAvhzJ69mFqHZEY0DjIiLkurwRvH64D2nscSv1rP_IR67k6Xiu5IzOSBwb8U_RBxqaJNKoBJpgqojzYm9f6ikIb_ggs7gQNgafvBZDve0zakCj9wzWTS583vdqfxhy71kAzfvPK5NSSdfY7BLf5ZpFqlvlFRBmVruBgxDhOIP-G8X9etUx7R4QvMvX_-yt9i5wocCBcRW7m-0tzTOogXBdgqxjvTwyxdOi8v4l241SLUZf8iWwCFY5OVN55Np0x6K9eGj5q4z54Bq6chzOegZrzjVZtO3YxJOLcSM2fynYnFuEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Complete Albums Of
Playboi Carti
📌
I Am Music (Deluxe
)
📌
I Am Music
📌
Whole Lotta Red
📌
Die Lit
📌
Playboi Carti
📌
In Abundance
@GangStship
🇺🇸</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/78019" target="_blank">📅 10:27 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78015">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NiHZaUZ5OGJXep7ArDxYYoYb2Nzi5vTzt8yEeB2CzaiBwdylcsILt4FIv_TViI3324zvcB7unmjR0msQWKZ6ehftbs5KDK_JgUo-ezTn9WwfY9bb59Lbx76kiesgBpvoHrr36kFLcdJrvOgvv2GfZdi8rXnRTJoZ2jQPNfkCmYJem64PS-bjjz-Cx0BpfKRoRr8h6lHH3el4SpFABqgQPcXCMygDcsJ9j62HcQSvksUPpky1aHy8ofbEacCJajlxIvSUwJhDBcutqreaGCGmqevhJPtNYppMgpOucBsaCQqC2220AlmA6EmFLXmCb2jdBG01wzC0Ea0IcLGI8S7JCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/a9qeRno59ya7iAbgu9_WHPV53l1o-931frt7d4-7159Gb1Vo62nsH4KFg9jaeRrsU6qUCjNjwDK1fGUtdP2v4-bOyC1aEP9dqQHvEt_IoStjpqVgYJcfKN4jdoerJW1-WziwdstSc6DrYbIjhT2QQDd3FM6lSUZNfSm5em4qWp4xjk2U5psY97BmF_zLfK0zgj-zeM58CcEcoBAA5ga6PovC3TuBL3kz2-h1qgv6v0AkKDS9yrNiXYBcaDPWQdkY_08l9tYFk-APCT6ACQD8Phpb2pGXcH_3Kw_Pj0Zy7W43pX1AvryDlYfoM7MQynp0Si1TgTId9jdEicSkHHGrxA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/78015" target="_blank">📅 08:10 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78013">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">اینو یادت باشه که همیشه تیم‌های مدعی قهرمانی جام جهانی، تو بازی اولشون ضعیف بازی می‌کنن که تاکتیکشون همون اول لو نره. صبر...  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/78013" target="_blank">📅 06:40 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78012">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">بنازم ژنرال تیم قدرتمند نیوزلند رو متوقف کرد  @FunHipHop | Farid</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/78012" target="_blank">📅 06:38 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78011">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">بنازم ژنرال تیم قدرتمند نیوزلند رو متوقف کرد
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/78011" target="_blank">📅 06:33 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78009">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">شوت سعید عزت الهی از ورزشگاه رفت بیرون
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/78009" target="_blank">📅 06:23 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78008">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">حسین زاده جا طارمی اومد
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/78008" target="_blank">📅 06:18 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78007">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">نعمتی چقد دلقکه
😂
😂
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/78007" target="_blank">📅 06:12 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78006">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">نیوزلند تحت فشاره
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/78006" target="_blank">📅 06:11 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78005">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">منو بگو که فکر می‌کردم ایرانیای آمریکا از ایرانیای ایران آیکیوشون بالاتره
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/78005" target="_blank">📅 06:04 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78004">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">محبی گل مساوی رو زد
۲ ۲ مساوی
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/78004" target="_blank">📅 06:01 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78003">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">از توپ لو دادن محبی شروع شد
با ریدمان شجاع ادامه پیدا کرد
و با جاخالی بیرانوند تکمیل شد
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/78003" target="_blank">📅 05:53 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78001">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">واایییی گل دوم نیوزلندددد
🤣
🤣
🤣
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/78001" target="_blank">📅 05:52 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78000">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">علی علیپور اومد کارو دربیاره
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/78000" target="_blank">📅 05:51 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77999">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">چرا سکو ها خالی شد؟</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/77999" target="_blank">📅 05:45 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77998">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">آقا مهدی باشرف (
😂
) جای آریا یوسفی به بازی اومد
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/77998" target="_blank">📅 05:43 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77997">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">فوری از سخنگوی قرارگاه خانم الانبیا:
به زودی به تجاوز نیوزلند پاسخ میدهیم!!
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/77997" target="_blank">📅 05:34 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77995">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BXuIjnNB4mBhUUVe2IEC6jTg8qJXp_kdZ_g8eywoPZxKnwkLnc_xMuo-XvjOgL7KRjcXbhyQ5gtIs8ZVnYbrsrQsY7sO0gpV0v0iHHydzm-h6ZFIeUHCmYdejffOvSUYVblu-EwzxAaLCrWNhJtsHMN9PzUwGCco4WIekDPy9LFWmR29DfXYAOkKeVdwmLg7JzOtKc9ryismSU3rAvV4FSUoc5rjw768xvAorXTCrczEGfsboXYG--maGwoLF07W3_Q-1v1c0H0AXYKytCPH5cAL_K503_GLpzrRDyclmuSG7WM2-UHGTNWjzAFC70I9uOeDuZtE7JY7QFEyS3bntw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
امشب اولییین بازی ایران که  داخل ورزشگاه بردن پرچم شیر و خورشید هم آزاد اعلام شده ، اگر میخوای بدون سانسور بازی ایران دنبال کنی حتما این کانالو داشته باش که تمام بازیای جام جهانی کاملا بدون سانسور پوشش میده :
• @
TrollSporte
• @
TrollSporte</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/77995" target="_blank">📅 05:29 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77993">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">نیمه اول یک یک به نفع ژنرال تموم شد.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/77993" target="_blank">📅 05:26 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77991">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">ریدم علی نعمتی زد ولی افساید شد
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/77991" target="_blank">📅 05:24 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77990">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">گل برای جمهوری اسلامی
رامین رضائیان
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/77990" target="_blank">📅 05:06 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77989">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">ولی شوتای قدوس>>>
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/77989" target="_blank">📅 05:04 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77988">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">این چه کصخل بازی بود گلر نیوزلند دراورد
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/77988" target="_blank">📅 05:03 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77985">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">استایل بیرانوند دقیق مثل‌ بهتاش پایتخت شده وقتی ک سندروم میمون گرفته بود
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/77985" target="_blank">📅 04:54 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77984">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oNwl0fQG40U9VzCOQnX2PTabA0Afd6UISG8P0j3tPhvJ9djaMNm_3CHAZXXsdLlBYBfx7JaI5myvxk8yU_EhTWNMuIv7sVYakoVtWti5SKo06xhHzU-ZNPGr5udOzcBJsNLbOeiTNgc6AdCu-9JpTv0MGQCE0jSsuTrRttb7BYa7vGu4Z_xDDY9n2SjrDjYHhwxCKy8kmdCG6zpLm2EOluEvjZQ7VxMvyePbXDC4RsJv8sP0kMQS1HVWbR-GpRmhJ-YERBeJjJBrKwivcL5RRjHpZ88LLu6Bk_4r5gG7KtpwlFd7uzXINep8sJemojz-0qforgkVyJJI4DZ6XeWVfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گل خوردی ک جاکش
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/77984" target="_blank">📅 04:50 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77983">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">عجب سوپر گلی زد نیوزیلند.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/77983" target="_blank">📅 04:41 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77977">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">بازی یک یک تموم شد
بهترین نتیجه برای نیوزلند
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/77977" target="_blank">📅 00:29 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77976">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">محاصره دریایی رفع شد.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/77976" target="_blank">📅 00:20 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77972">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">عباس و باقر فقط از زنده موندن آقا مجتبی خبر نداشتن و سورپرایز شدن وگرنه همون روز اول جنگ رمضان توافق شده بود بینشون و توافقشونم ساعت ۹ونیم بعد از ۳۰ موشک به بیت رسمی شد.  - تغییر رژیم هم از نظر ترامپ همینه نه چیزی که تو ذهنتون ساختید  @FunHipHop | Constantine</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/77972" target="_blank">📅 23:49 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77971">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EXX35tB64ZMjqWP_QSXAXrq5iNorDigFx3xLyuEyr7twOFUkvKqdZxm7xNf3fKv6mHoKKm1Zljb8ODEHuOrvI01q583EzpxdLqlfl9S1Izjuo2M6ryjf_Ju_61XJRXTLmzyB4OmhF9dy2eWkcQ52GDLqHKOSQsTHmLJQ8BDdqMGAzP6h3zGZ0zgxnp2RV7Gfb2QkcKEzwLeS8dxOxcVzs1TL9xYH3dcbZHxXRyHi7hcgMlMPDnTIySUmL-cw7TtMPAJHc_kocpWYQ3uaFTbG-44z18Tdw0dmoPDXXxKVTplj6M8l7YU_LYWA42vvUOdhbLAdMAbB0vMwRSjlSZ_H0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عباس و باقر فقط از زنده موندن آقا مجتبی خبر نداشتن و سورپرایز شدن
وگرنه همون روز اول جنگ رمضان توافق شده بود بینشون و توافقشونم ساعت ۹ونیم بعد از ۳۰ موشک به بیت رسمی شد.
- تغییر رژیم هم از نظر ترامپ همینه نه چیزی که تو ذهنتون ساختید
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/77971" target="_blank">📅 23:47 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77969">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LV2_EF9bdRSvFAb5sbDI8nk-_p8o7fKnWFdtCcB5UlZINgl5OdME-_CGerQ3irN1AXlvyF0suxeEeWv_W5afme6ZkVKAHWHuSqlBOnFm2NB0QsJCMjEGd-5wXVve27KA7irZeauztYuodmBHB5Z_VpU3KypmG7RIDoAB2Dn40D9g6TvCTAnsOvjiK9YNgEV9fzUnC8XKZMLnRnlBH5y1UPNaHf9qVNW-6LbKycF2yLD0DUn43n1TwgL6OMUnUYbl9i9HxfUHBNK_tMSxu8c8d4W5vZy4qJQefmmUebnfT_STPnSKzzUMjaK1Ymp49xutdWMhRXuYF4mO1bte8HUSqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شایان یو واقعا کونیه پسر
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/77969" target="_blank">📅 23:05 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77968">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v10_ayIqdVAnnf101oxICIQnx9IiGJ7TnhUwx4bll9kprPXMQfOGTo8QA9Mp_ScauH0T-Wm48Vhx3Vt25Qzltn3CF0qR1wTdr30B5bdq6QMj1YEnXtNsL5s_ZNS3n-1ZIpuveBWjgnIlgUCw3AsX0-RHHG9pMZGcpfJ0RscKQ-VJ-32oJ1M5cNvd6ngbFap37-UL4F4Z_mvcJeRLGSuE6n1grM21ZKzhEKUhsOcBsOr5S9Y6jxmonfh_NCQjbheLvvkaDi3x9u9XNvu_UKeB43VkL2rj9hMmDH8UBAdVdOxGycccSwdAytQd4KDoNqXFRomkA3QkQWEwHPA4P-dvEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موزیکای قشنگتو بفرست باهم گوش کنیم.
🎵
🤍
گپ پلی لیستمون
🌓
https://t.me/ORGplaylisT
https://t.me/ORGplaylisT
https://t.me/ORGplaylisT</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/77968" target="_blank">📅 22:56 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77967">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">امام عاشورا برا مصر گل زد
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/77967" target="_blank">📅 22:52 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77966">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">زندگیتونو بزنید رو برد مساوی نیوزلند</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/77966" target="_blank">📅 22:00 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77965">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAmir</strong></div>
<div class="tg-text">اسپانیا بدون یامال در حد پرتغال با رونالدوعه</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/77965" target="_blank">📅 21:57 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77964">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">کیپ ورد جلوی اسپانیا متوقف شد
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/77964" target="_blank">📅 21:40 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77963">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">ریدن تو این بازی باعث میشه اسپانیا خیلی وحشی شه و بقیه رو بگاد و قهرمان شه
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/77963" target="_blank">📅 21:26 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77961">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fNqLT4NuUFWRIdTMNG_dWNua6V36F9qzSDZNEr_ZrPq4shkTnJuz49mHFL5Qd8nL1fUtPbs0HK_gtNS9BDd0-44onSImTbgpVTt7ADzUCqElIBpjihNIhvc-K7b-vYe1IoHmMOd6sqJW2xiXxEmewWdNbOHOaK-OLkCFyZx7XfynBVlqNQbGIQ4pJx8gvbnWKb_Y5AQ8tywt-quyq44BGfhNgJnMJ25Ed4-6W3zxN3CQQeyJ47M0rjxX9TDL6C35pEer7XS5LbU1mhkV1X9VIja0Lpy2BYIImyNUoDF0-g2n8TBEq2Qkq0pAV8S2bEiYUWO_MvJHrbTH9xOW-MKYwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیانیه جدید باقر شاه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/77961" target="_blank">📅 20:59 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77960">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">آپارات اسپرت با ای پی خارج ایران هم بالا میاد جدیدا، اگه خارج ایرانید استفاده کنید.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/77960" target="_blank">📅 20:08 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77959">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">قهرمان جام جهانی ۲۰۲۶ خیلی ریدمان شروع کرده
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/77959" target="_blank">📅 20:03 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77958">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">آپارات اسپرت با ای پی خارج ایران هم بالا میاد جدیدا، اگه خارج ایرانید استفاده کنید.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/77958" target="_blank">📅 19:57 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77956">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">فردوسی پور هویسن رو آورده برنامش
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/77956" target="_blank">📅 18:25 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77954">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WkHsmF-nb2zS8-NhLwjr9BOoCZZUmaRZxz2lJ6Dtx_lzX6lvKtMdrYn0LQrmgK6AVDwpRj9V14l_FVfeavozStDozVqHwlfhtpM5fvPtVlpsPAf8AzuVLw_A8BRSAn2gpcDGMuh2GW0gPs2MYj7skkvDDnehfqLBFviMFqQdCjoRqxNvC3mNDNc81Ijav0arHGZCx9zymX5oxq8vN3BK9FamVg9_4GyFCEa2zmUIHcWGwo-76gQnrzEBksoRC3kLy_q-s8Xt5oAflM3xM6ic8dx4sNSekwwrQ9xXZG3PJm8pGG28bNIu6-hKnX61M2Y8WbdeP3gqz3jLp0iEFQT_NA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kKvHBFE0uXui-_UdumQmb6gMkxf1bqRYJ39xzIS0pv58AC8Ph-H4lmXqk758g0wxkIoM1FVyEDoGqpsQ9UQzHkMHG5T2ZGh_0YKvlVu7qK7DG6WkE_3lhS85lbu-7Dv1EhniPsESxWpLzSsEHLiGoYgl6HYE4Lo3y2WZg0pDMyHHq8plVwhaQ5XmmDdJrr3Ox-RCwbQH5kTCgMzSFO1TQ8KJ6iyZZcfG-igP5txq5JbsFG5fC6w2FHqM1Xz1hy1rVd1ryNg89f7HKIKa6xo0rZlDJDfBAgADfTp27dkNhe8myGqPfvZcSSLtGHsbZmeUIt_ZrveyCH8oj4FGDTox9A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">استوری شوهرش همزمان با استوری خودش رو میبینید، خداشاهده شوهرشو نبرده عروسی
@FuunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/77954" target="_blank">📅 18:10 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77953">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ijIZQsHSAAG04JVzrH54YRPKkUlnlgw10DvqERx6SgbdGZ7MAeHGeigLeRd0vu8TsPttAENP7pDf5A-BL1yEeSSpmCj40Gh5ypwyrFgue67qUQEp_dt0Zhh7AZ6zLT4pT7-cZMN4LatS7GgX3fZTDe1AP5iD_jDkD4xqpsrQneCLxWFmPBVJqYiHJ9l9SY2OWlxmlVqSAADNr58P4jRz_AAM4KmqdCknfswVqJ0wWX2xnw5T39mCyeR8dxwUfBIUzwoiHH7ZlLrqUEjy-PRZccNw5TUwlk53VYynVDlqH4MI_ZWHuqK84wYX0Zakb_n3RuX4_7xfiwZXKtXyW6iWzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری یانگ کید
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/77953" target="_blank">📅 18:03 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77950">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mwYXdNYSUaaFbuqKSGIZrO116QVX4jcaYCryfeBfc7tDtS3FERgAR5w9uoG37AgyWD_87DqSfbIQ5tQk7iEL87bLhCRkUHZJd-U7FHoTETnQ9KmaYc1w64i1SXqpSOG6uFI5FVlvkIamQ4VnkiEhahzxDWkw_Mp0Xfu5TyTjpdaVbsu0RImcljhx9BKBlu89M74q_GEb4BiEzUxyVTGVMwAcJ4rNPRjU_jAkFTcbjOplZhCPYox6fXvjmi94whLIPZtxajgxOGy8yMjmtk2R75r6bbpx9_-OWcFxKWqGzvNva3JaoT1Mm5Zt_kCDfv2PX_oK1NUy4AR1fpclzSQ6Vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مونیکا بلوچی ۶۱ ساله
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/77950" target="_blank">📅 16:08 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77949">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qruV1QGM_G1IDFul2Ho3HfB3kGon0s58iijBYsmUHVoUvyyLVvx3UwJ6O2aDGJwcgDmqlSEtyhK9_Is3grtAt9TnjdZc31GIFxYICdZfqFxXRLZaK7sFBK75QqqI3s5PLG4VCbSPMTkixzWQbV1jLn0nEqoaIJbnIM5eO43yWa88Lz_ljXEcS2-nQC4uzukzIjY44CxksmMYb-tQQq8NSG67jlFiAQq0jpJEthHADtf0LP9Ja5fALR_4RO0sLE_c6iDWRi5wb6vBgNv5zEju_4IeBrv1kFE1ooI2I9s_5o_1_qTq-rGrRJ0IWh6s0Dr68CJhYRwwd2vdDrIksOtJOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😂
😂
😂
😂
😂
ببخشید دیشب کم خندیده بودم
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/77949" target="_blank">📅 15:51 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77948">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qwDYrayBmKHu4tYoU6q_0bJEtIybYRtmTyzYstX_5NHU4n8CP4NcSxU7peCHyol6GU5oocyOfsXK-YnDOcv4N_p-5OxyPxGYjB9MBYc90uuwzceKZeXvAHX1HEJhb2F05TgaDIzWnyi8SoBFXaPcicxQu8DxKUGQVZ6vuJwsSNuTzWBg1tgTJpOgruTsIl5vhVo63Xr2mByiURor4JRfKZ00g_Vv7bC_7cMbQeItIEP1p-AeLjakvPFY_Wkf9rhPMNIwy2PbdTFs0Jm66jauH6psroGqttgq-Uo655O2TyU_C5fkZYNIF0tYlI7FzSTBM-sRwF7-NNDo53tFM6YMJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عمو وصلی؟ نه انگار کانکت نمیشه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/77948" target="_blank">📅 13:54 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77947">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">در چه حالید دوستان؟
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/77947" target="_blank">📅 13:41 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77946">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">یعنی جدی ۳ روزه چارتا بانکو نتونستید درست کنید؟ بعد ادعاتون کون خرو پاره میکنه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/77946" target="_blank">📅 12:48 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77945">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LjXGEQDgGhS7Q_h75_SqjG4kU8UdVE8VtaBSwBVL91dIRXOHqAg_Y-siLy3rnwQsQo9Vkz362qBsTnuWrCLSPsP5xMhJ5I4A8FjZ4f3opjXL5Jq4n1RDzJYUy_uE3zFshYZqAqg7h8hMe0k4jQtXVSevRHZVpn_Tn5oP1PLDqdP-h2k3ymRdKS4aIH83l8XcS8b_39sNqRHalcTZBImKm0bcS2WevdA_BhcvaekvD14boASOOb7j175KV1LVnb1knRf2fL3XKHOQ155aSeemPW3gA26nk30n6iOY4PPgM6Ma1FjIDguwDkzcVMKUPN9RrXVRrlYyS_IawfhtP54DgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میدونستید آپارات چنل یوتوب داره؟
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/77945" target="_blank">📅 12:22 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77944">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">میترسم حرف بزنم رئال منم بخره</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/77944" target="_blank">📅 12:05 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77943">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">میترسم حرف بزنم رئال منم بخره</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/77943" target="_blank">📅 12:03 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77942">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78832f0cf9.mp4?token=G8zW-18agunvpLAMAWauti17gv3rti5f36tuODjkL5yOiqaq2m6yFjzOW1Bat80DsTawdlGrT61gqzMvj4sC60DlYkG1p0xh0v7OpT_7aVE36Yoyoeeskr1_A3LotgUra3-drni9w33x1OosyrvaQrPXaDODEU42BYDiRamyCn4X4CrccBXawmBtVHiCGAnKJBW1YaB0qTSKZlAPVkPIaEObP9amxIRZla6kyaUpOJaa6ZQbsQsLESzyjk5XZ7F0SmGAiy8gBU25xrihRI8oxUBIhcQJ68LazyCci2Jg0YUtq9WieD11BF0emPHICEWkjsr9BVSlb9EpVGPKnUllfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78832f0cf9.mp4?token=G8zW-18agunvpLAMAWauti17gv3rti5f36tuODjkL5yOiqaq2m6yFjzOW1Bat80DsTawdlGrT61gqzMvj4sC60DlYkG1p0xh0v7OpT_7aVE36Yoyoeeskr1_A3LotgUra3-drni9w33x1OosyrvaQrPXaDODEU42BYDiRamyCn4X4CrccBXawmBtVHiCGAnKJBW1YaB0qTSKZlAPVkPIaEObP9amxIRZla6kyaUpOJaa6ZQbsQsLESzyjk5XZ7F0SmGAiy8gBU25xrihRI8oxUBIhcQJ68LazyCci2Jg0YUtq9WieD11BF0emPHICEWkjsr9BVSlb9EpVGPKnUllfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اول یک قیام خونین رخ میده نتانیاهو و ترامپ وارد جنگ میشن رژیم جمهوری اسلامی رو میارن پای میز مذاکره اورانیوم و موشک و رهبران رو می‌گیرند دو دستگیر و تفرقه بین نظامیان و عرازشه و بعد سقوط با فروریختن رژیم از هویتش اتفاق میفته  - ۸ سال پیش پیش‌بینی های مانوک…</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/77942" target="_blank">📅 11:11 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77941">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">بلایی که جاستین سر ایلیا آورد :  @FuunHipHop | Jenayi</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/77941" target="_blank">📅 10:51 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77940">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">دیگه زن مانوکو گاییدین هراتفاقی میوفته یه ربطی بهش میدن</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/77940" target="_blank">📅 10:44 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77939">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">اول یک قیام خونین رخ میده
نتانیاهو و ترامپ وارد جنگ میشن
رژیم جمهوری اسلامی رو میارن پای میز مذاکره
اورانیوم و موشک و رهبران رو می‌گیرند
دو دستگیر و تفرقه بین نظامیان و عرازشه
و بعد سقوط با فروریختن رژیم از هویتش اتفاق میفته
- ۸ سال پیش
پیش‌بینی های مانوک خدابخشیان.
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/77939" target="_blank">📅 10:42 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77938">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">مانوک ۸ سال پیش در رابطه با قهرمانی یک فرد ۴۰ ساله با لباس نارنجی صحبت کرده بود.
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/77938" target="_blank">📅 10:38 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77937">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IpWye29dHvxh-A97t4ayoevg2SgBgqRjlaoYgnxvcChQ_sT4kqIxs2AEdntHsWNcvKLuKKZu-pVcElDVdXlllxdVur6gDcC5E2I3a2oKN5xnw8aQBt0LUBizAvIhyiUKt4UPDJ4Vd7gpYWsHgvQbJB7EMpgXfsHhb1LsDh1XhTwvIGXzAHENuQj0FF0A-Gy2mjfszugdqAA6yC8z8ARf5iU4GHltdntDvVHzpSw3LBBd49-3j-54TBBS54IeL4aSo6F9LyhsylKtIuNsj_und3biijdLbgoU0DVOr-l-KVfLmNhRLGPEfSYjY-9HpnAuldylEjD2Ey2j7F-15wLmMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بلایی که جاستین سر ایلیا آورد :
@FuunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/77937" target="_blank">📅 10:30 · 25 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
