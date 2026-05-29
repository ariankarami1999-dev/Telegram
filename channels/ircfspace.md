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
<img src="https://cdn1.telesco.pe/file/uhwZcofF1_ViVohlIQWSLp9M_DFdjJXei0vt8rXiCcmRn6iQo-KXkYntGh2F1yUxFWM0sYHblpSrSeLXRFNe-bT0vRHi-c2JI5fwEp6w0cQQ49uxbVKpU-qXTI4Gxt1QqE3UUaBSv1hH1VSdNPqMjNZZKCd67vg1QUdMU28OJG6wLbxXT1LgUnGK-v22aPl6sbmcJOQhkDBdxTfS-hSX4eW-457rIXCmlvo09CFmDxGsDxrGL6YMs21qRDcNrgZZbmyns9s2xvWTsSqsMy0-ui_o6NCoPPGOSJKaozpwfy6ZNRsaQVVsEzdCkZMThpCiA66Pnw4cKfGen2nZEDe7kA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 IRCF | اینترنت آزاد برای همه</h1>
<p>@ircfspace • 👥 97.5K عضو</p>
<a href="https://t.me/ircfspace" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 این‌کانال با هدف دسترسی آزاد به اینترنت «به‌عنوان یک حق شهروندی»، به‌دور از هرگونه وابستگی حزبی، سیاسی، تشکیلاتی و ... فعالیت میکنه!https://ircf.space/contactshttps://x.com/ircfspace</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-08 17:23:55</div>
<hr>

<div class="tg-post" id="msg-2399">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/apdwhwhap86XFO9l5eaulHsiGQWxY65afHoMe5rA_MOi5t1DQCYWqLW_3CW-ipsap5JlMpzd67XOqLbVGIuuIGJqjorSG4fEGCb-bk3c9wxQgZ1nXJzXu2gEg6-Lk9Vd6HrmYSgHFZu6Nq1qSySa0ACWh06DkZVgLfVzCqWeqxE3kOGZGXt0ZzQ8WKXKabHqAr3X8WRLxOlOiGQZX6kqu-95wELZNhMiPWCxKDwPeVm108Ef4Mj9eKy1mUI3Sc62zBuqdE2sQF_RZ1ruAwcoA75VZBVTbcNuyX6MAt9H5_jjrqT7W3L6qi_i8kaUqc975C2DxPB6tUfgS6E5taPoHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در جدیدترین بروزرسانی از فیلترشکن رایگان و متن‌باز
#دیفیکس
فرایند دریافت کانفیگ از API بهبود داده شده، متد CDN Fronting رو به‌همراه اسکنر داخلی به بخش روش‌های اتصال اضطراری در قسمت ترجیحات اضافه کردن و همچنین روی بهبود عملکرد، افزایش پایداری و رفع چندین مشکل گزارش‌شده در نسخه‌های اندروید، آیفون و ویندوز تمرکز داشتن.
👉
defyxvpn.com/download
💡
t.me/PersianGithubMirror/5676
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/ircfspace/2399" target="_blank">📅 10:53 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2398">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mVuAhucNqrybvSXCmAboVjQOJfea2alwMaYUsJ_I8ZJL7NaUZ0GYeS2pBsQaJm8SRS-u4_B7cmtjMTNx-IaxcO8vM3Wqxu3n-PsAtXEJXGm-WVeSi3pFHUbcEqP952umBpQZVdin1xK96O485xaderC6WJAGFqx1CJi195ghPr3d8iB3onNd8ViSYkyLf2_og1HIJIwuYLSi_HFqR3hpDf_-2KbD0SMMqa-YBEerMHmczzVRx1nyQfah1gdvlTVNsbz9zUXQQXGQiKK_MFAZvTdWzQHOYYilcmi-pgeHseqK3loNXNB2Kl5DZxVGa_txzDefDPbqBTqn_-6liarF0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در بروزرسانی جدید از کلاینت NexaTunnel امکان پشتیبانی از کانفیگ‌‌های Xray در کنار Stormdns, SSH over VPN, WhiteDNS برای iOS فراهم شده.
👉
apps.apple.com/us/app/nexatunnel/id6766783641
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/ircfspace/2398" target="_blank">📅 10:51 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2397">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">رئیس کمیسیون تحول، نوآوری و بهره‌وری اتاق بازرگانی تهران گفت: خسارتی که کسب و کار‌ها و به‌ویژه فعالان حوزه اقتصاد دیجیتال در این مدت متحمل شدند، اصلا قابل جبران نیست. /ایلنا
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/ircfspace/2397" target="_blank">📅 19:45 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2396">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">این اینترنتی که وصل شده داره نمی‌اینترنته ...
©
okhtapoos80
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/ircfspace/2396" target="_blank">📅 19:39 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2395">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SlVxbxM6FEPodiyLGk11ytUpRP4OLFeUX8gBwyJQiIhEUvxvIbyOYjSX3aKm3M6tZUt3zDqJBGolo5veyxuOztJ9oOPObCaxzzbBkkHIa6Z1AmzTs086ij0FooeJUsEq0oYowjgYH0T8qhLSUPKl-biIHKJxNtu4NfA_JCg6fznr5rn0AwwsV4urp7iL2NxYlcOENTOmraXcedJ190gpm4TGrgn74zin4Tp0mKYZLKYZvah8yOjr-koHqvc2XG-JteHlRuyZRorIUauCmVx3ZUjezzgqGf0_5CLBhIYS346E2Cd9lv-FJxCtYzd0UC4ijHbCPgHfS6pwdsP6iNd6WA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زمانی که اینترنت در ایران قطع بود و تیم رسول جلیلی موفق به مسدودسازی Signature وارپ شد، اپ رسمی کلودفلر بروزرسانی جدیدی داد که حتی رابط کاربریشم تغییر کرد. آپدیت جدید این برنامه الان روی بعضی از سرویس‌دهنده‌ها داره کار میکنه، هرچند امیدی نیست که در محدودیت‌های شدید بعدی دووم بیاره.
برنامه‌هایی مثل Oblivion که بر پایه وارپ کار میکنن هم تا زمانی‌که هسته‌های وارپ‌پلاس یا وی‌وارپ بروزرسانی نشن، کار خاصی ازشون برنمیاد.
👉
one.one.one.one
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/ircfspace/2395" target="_blank">📅 08:50 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2394">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">بعد از وصل فیلترنت یا همون اختلال‌نت، اکثر VPNهای متن‌باز و رایگان دارن به روند آپدیت‌های منظم خودشون برمیگردن. تجربه قطع کامل اینترنت در ایران احتمالا به ابتکار عمل بعضیاشون کمک کنه، تا بتونن در شرایط سخت بعدی کمک بیشتری انجام بدن. به مرور سعی می‌کنم بروزرسانی‌های جدیدشون رو اطلاع‌رسانی کنم.
👉
t.me/PersianGithubMirror
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/ircfspace/2394" target="_blank">📅 08:31 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2393">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">دسترسی به اپ‌استور و گوگل‌پلی روی خیلی از سرویس‌دهنده‌های اینترنت باز شده. احتمالا خیلی‌هاتون دیگه حتی حوصله وب‌گردی رو نداشته باشین، ولی توصیه می‌کنم وقت بذارین و حتما برنامه‌ها و دیوایس‌هاتون رو بروزرسانی کنین. حتی سایت‌هایی که دارین (از جمله مواردی که با وردپرس بالا اومدن) نیاز به آپدیت‌های فوری دارن!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/ircfspace/2393" target="_blank">📅 08:28 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2392">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">بعد از ۸۸ روز قطعی کامل اینترنت، جمهوری اسلامی اینترنت رو وصل کرد. فقط یه مشکل ریز داره: فیلترینگ انقدر لایه‌لایه و سنگین شده که عملا فیلترنت ۲x پلاس رو باز کردن، نه اینترنت رو، و همین فیلترنت پراختلال رو به اسم بازگشت اینترنت دارن به عنوان دستاورد دولت تبلیغ می‌کنن.
بماند که جمهوری اسلامی میگه اینترنت به وضعیت قبل از دی ماه برگشته، ولی ترافیک شبکه حدود ۴۰-۵۰ درصد کمتر از  قبل از کشتار دی هست.
©
AManafii
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/ircfspace/2392" target="_blank">📅 08:25 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2390">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">عدد ۸۸ برای چینی‌ها نماد خوش‌شانسیه، برای موزیسین‌ها نماد پیانو، برای فیلم‌بازها نماد سفر در زمان…
ولی برای ایرانی‌ها، یادآور اعتراضات سراسری سال ۸۸ بود و حالا ۸۸ روز قطع سراسری اینترنت و خاموشی‌ دیجیتال!
جمهوری اسلامی اصلاح‌پذیر نیست و بین اونها و ما دریایی از خون فاصله هست.
از فرصت استفاده کنین و دیوایس‌ها و برنامه‌هایی که دارین رو بروزرسانی کنین.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/ircfspace/2390" target="_blank">📅 21:56 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2389">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bd57xoKf7seIezEhJiiP6pClYqlG1mGbBJKx5iabsMGbwmweo8Cox15I-vWuuuCefrc5RmQd5-Mtn-SL87c8ajYLqm-7cNx9BW4d1AUmGDFmAQ1sLGNaaBc4-ylhp4CioIMFXVq_QpCTaWKoNbC3D_b8oJhFt3Co8nSprm6z7L_vZbC2lFPhMK0RHhux7oyIEDX46REga9-T2KlCyyci5mthizrcSdipdozvX8Xl2e0-ACN6VCwv3bUUDcvw8CNaxYIbLcPbqAg-tKmfxrwtsLdGn63DTq_NYSeHf1oIuA9gFoSXxW5WdQoPnBdhSGGmlvCeRGZpazeAmfTmu-quCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نت‌بلاکس تایید کرده که میزان دسترسی به اینترنت در ایران افزایش قابل توجهی پیدا کرده و به ۸۶ درصد رسیده؛ هرچند فیلترینگ به قوت خودش باقیه ...
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/ircfspace/2389" target="_blank">📅 21:31 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2388">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YfkK1MLovpyQwqrc0F25gXfmdfr-kGh3GMZVFDb9ldirqE9_0H9x4ymvcNnSaxX1dCA1UebsM_Gxz1hAEUqVL9GIicnswzTLKFGVVvI2vtyZo-XCJKFeMqTEmQUx35xaQxbrs6Nw_1eQ6cMb7JLSDos16mZA8KeKGfVLqsIsYc-_vjSqdc2y2Toknoo_GPCjNY5wio7mh1iiwfTqzYHLNLQRo_JxecewmY0FOjdb-ZRHGqsklnAA34Q9HR4TgG3i82VAZkyQTZ7LjV7LWZ6WTgH-dPZa-pNYr1UP71ZivQxypaK2JOJN5TeU-UjwwE5Av1eZ28i_FRr8aBo1rlYJJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای اینکه از وضعیت این روزهای اتصال نسبی اینترنت در ایران آگاه شوید، لطفاً نگاهی به این نمودار زمانی جامع بیندازید. ایران هنوز راه درازی در پیش دارد تا به همان سطحی از ترافیک بازگردد که قبل از ۸ ژانویه داشت.
©
nimaclick, DougMadory
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/ircfspace/2388" target="_blank">📅 17:30 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2387">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/D2X9A1UjyhNdE-fnfuEyeug8DcfxAMe6P5ulScJmJYwfkluks1vxFdXHc26NfA86jq_j-nRPhTyb2qOgBrBQuZFwRDY4pOnBYwr8t_z_STaD55Lt5rPKMzhjqMPhtG6jEhdEwhZvy0Tj-8DyYywJiow6HrXbkLhwJFZabaZ0DafF-KS_iXZRYBgaHNFq8G7Jh5jDoHJMdVEaLQiQo_4yd8lBu-9Ps0dOsk7BpJ9X9noweObysxgIiA4vCfik6n9XYHCqeS2hlJg_iYCNe6cH6SPaKpBeprJlk9Ot-Zi91vnMAaPecVgwy3iVIG2IkoQWaLyVBb0IM1oPtrjb3zMHzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه‌ای از تلگرام اندروید که از طریق سایت APKPure منتشر شده، ظاهراً یک نسخه دستکاری‌شده و آلوده بوده و محقق‌ها متوجه شدن APK مربوط به نسخه ۱۲.۶.۵ امضای دیجیتال متفاوتی نسبت به نسخه رسمی تلگرام داره، که داخل اون کدی با نام DataCollector قرار داده شده و میتونه پیام‌ها، مخاطبین، فایل‌های رسانه‌ای، موقعیت مکانی و اطلاعات دیگر کاربر رو جمع‌آوری کنه. گفتن این نسخه به سرور مشکوکی در هنگ‌کنگ متصل می‌شده و داده‌ها رو به یکسری API ارسال می‌کرده!
©
vpnreviews
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/ircfspace/2387" target="_blank">📅 17:24 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2386">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">بازگشت اینترنت به وضعیت قبل از دی ۱۴۰۴ را با ذوق و شوق تیتر زده‌اند، انگار فتح‌الفتوح کرده‌اند.
کدام اینترنت؟ همان اینترنت ناقصی که UDP و QUIC و IPv6 رویش عملاً بسته بود؟ همان اینترنتی که نصف سرویس‌های مدرن دنیا باهاش درست کار نمی‌کرد؟ همان اینترنتی که برای هر کار ساده باید ده جور VPN و تونل و کلک می‌زدی؟
اسم این چیزی که شما تحویل مردم دادید «اینترنت» نیست؛ این یک شبکه دستکاری‌شده، محدود و مهندسی‌شده ا‌ست که هر روز بخشی از استانداردهای جهانی‌اش را قطع کرده‌اید. بعد تازه اگر همین شورای جدید واقعاً قدرت تصمیم‌گیری داشته باشد و فردا یک نهاد دیگر همه چیز را دوباره برنگرداند!
این‌همه خسارت به زندگی و کار مردم زدید، حالا برگشت به وضعیت نیمه‌خراب قبلی را هم دارید مثل دستاورد ملی قالب می‌کنید.
©
iSegar0
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/ircfspace/2386" target="_blank">📅 17:19 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2385">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OxzRo-UKYAY3HS7vYkYcb_18e-Kg5spGwcZ9E77Q6DKJ3aNhEEAib-28JD3adVZ5e51pTBnKvvR3dRbzCy8V3AMd_-sQ-_bvmVOxf5MeRa-q4JET448T2GQ1F6Rg5AfjZ9j_tBTOy5niDoPwd2uZ7mEk8HZ0lJHetDkZ52fx_7XlEhhT38ksDX01wC-ATVapaNwdqs2MKGIOwLtKF-tRUvFL7p2NxkC_V4w-qtJY7mjXxOI6P1Jnj2sR4sTTz3CVWFVbwrepSbjW0dtUaqrLGBoO5cfVEyqVFX5Q2rJSRM4GTaFtGqI24sWy3gQGZl6HI2MBxiJSzgES9pz02h34qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۴ فردی که در دیوان عدالت اداری نسبت به اتصال اینترنت بین‌الملل دست به شکایت زده‌اند، کامیار ثقفی، رضا تقی‌پور، رسول جلیلی و محمدحسن انتظاری بوده‌اند. /انتخاب
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/ircfspace/2385" target="_blank">📅 17:12 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2384">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IypyjCDCtDZRVlCW5Lg27w1MQuMlpFZKhLLmDrZfItxbrFHDkmwOzOtAVjr73CUEy_yPmC-ETg-ggqWqsYMhVZKG4vNXSADn-ujG3bKz0aPfvsCbSkcoaRk39Z9v72aSx6KoX5agpPHbdwbFUYNDcqbNO1elpYwWV8r8IYWGHpQ0Cf6gGbAw7I2r6AHmWv0XHH7NT4N5ZDlcvrjoQKrR4oOjVMtoh044YzjC9QGGIRVaGJ6PbfYc_rcL0dQSxIogWLLp3sfcC9bA--ubEkXqReIzzG5MP138cAAFWNqnUe5XL3g0i74PeIqk7p7a0aCNNRBahkqwLNXRt7GYfJab2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نت‌بلاکس: داده‌های زنده نشان می‌دهند که در روز هشتاد و هشتم از قطع سراسری اینترنت در ایران، اتصال تا حدی درحال بازگشت است. البته هنوز مشخص نیست که این بازگشت اتصال پایدار خواهد ماند، یا خیر.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/ircfspace/2384" target="_blank">📅 17:09 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2383">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">دیوان عدالت اداری به مصوبه تشکیل ستاد ویژه ساماندهی و راهبری فضای مجازی کشور ایراد گرفته و گفته مصوبات و تصمیماتشون تا زمان رسیدگی به شکایات، قابل ترتیب‌اثر نیست.
فعلا اون نمایشی که پزشکیان و هاشمی واسه وصل فیلترنت اجرا کردن به دیوار خورد و شرایط روی ملانت باقی می‌مونه!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/ircfspace/2383" target="_blank">📅 14:43 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2382">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Pn3waCp9O5qp0CAq1qnKXH4bz4Ht_ksE54kTyLguYgsjuhgSf8BMrZhvHMjAJ5UNtqMT87U3d80EIfVZgouK7jnUIDgvDyDO6DsF9FuNQc-SsRO1qdscq3XMZEIY6ZZhuNKGD5rT29dR1-vucsqlWVeqCBDTNWYnnJ9VoHiplZ6yLmN0yoEOryGSDV_PLJSDQHT3mHXw7r8euueBndhwQ8Uu05a14AB8RieCjyOwsN7UWrbojV7n9t2nnclQw5tjiDaDeS7fzd16sK6uRsCR8BJB0ceFXlvPF4vbddTpmKEJN6GjcrLD7Ag_2N0RSDcjT1YkkkrOHVQnX5qRBIvZfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه‌ها نوشتن که مسعود پزشکیان مصوبه بازگشایی اینترنت رو امضا کرده و بعد از ۸۷ روز، بزودی فرایند اتصال مردم به شرایط پیش از کشتار دی‌ماه برمیگرده!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/ircfspace/2382" target="_blank">📅 23:19 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2381">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pX12hWm-GLMhBz8tO-llgA-zDTyUHxgKzo062s2eP7mUrODDoKrnoH0FK3uW2fz8NnL8KRzdIflRKauZMAIwPR5uS4JBp1LdZl57frWZswXPx0jM_YauoFBG_Kc2lMCpjju2BghImfiIpcPG6eQb7JX_C_sVuilcuYKogSMtarZZbS2b_Z3JE4VhZ-FR1wBNsx1uLSIM2sWH5KHQAdMUiYsZQ0mNKgbASkTM8PV_nqydfIAOok7peGJ7Yybi_OvDPovwndTwzXjR025KzJK12iOdSsAip8_LLHj4WoaZ8wx_GZg2WWvOBW6QndDtOcAM-8zSrA_60jI3Axl0-DuqaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نت‌بلاکس: اکنون هشتاد و هفتمین روز متوالی قطع سراسری اینترنت در ایران است؛ محدودیتی که بیش از ۲۰۶۴ ساعت ادامه داشته. این اقدام هرگونه شفافیت درباره اعدام‌ها را از بین برده و به شرایط غیرانسانی و بلاتکلیفی روزمره‌ای که منتقدان زندانی، مخالفان و حتی گردشگران بازداشت‌شده با آن روبه‌رو هستند، دامن زده است.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/ircfspace/2381" target="_blank">📅 11:23 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2380">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ciNt_OV1ep_kc0sax8NDHdsysfHnH-1cEGhWnsjwoSYcIqMmx17J7p4-xLwCgF9u8OraAXqX2A5snL5jJh3tqiHx3kaK5oIjxKG5xalbg34nv06MIYEWPT3iWk1dbaLSWUgJuY-VSDB3bVEPd4vStr_YmpoLP6To-yT5AvptOcrsjH1qIiyucBbItNphTTr-QC8buXZ76HxEj_H6fkv3Hdz9riFgHHR1DbM4OUQynu4w_LgB4lU5Fzh5QDWwnDX09M0ozbbcCHWJtStFl8zwGDfS_ep5taUuas3ZWm7BCQpV756SOFHYhUQzjPCZRN93dHuDbcAHsSxOauZw6V7sHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توی آپدیت جدید از اپ متن‌باز و رایگان
#شیروخورشید
کار خاصی نیاز نیست بکنید! حالت اتصال رو روی CDN FRONTING بذارید، اگر قبلا آی‌پی و SNI ست کرده بودین، پاک کنین؛ بعد روی اتصال بزنین و برای مدتی صبر کنید تا نرم‌افزار خودش آی‌پی تمیز پیدا کنه و وصلتون کنه!
👉
github.com/shirokhorshid/shirokhorshid-android/releases/latest
💡
t.me/PersianGithubMirror/5515
©
yebekhe
آیا این برنامه امنه؟ قبلا
اینجا
توضیح دادم.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/ircfspace/2380" target="_blank">📅 17:16 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2378">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">مامانم دچار آلزایمره، از وقتی اینترنت قطع شده و نتونستیم ویدیوکال کنیم، فراموش کرده من ایران نیستم، فکر می‌کنه باهاش قهرم و نمیرم دیدنش.
©
MaryamA89323145
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/ircfspace/2378" target="_blank">📅 08:57 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2377">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cAkVaWDfX9fMO0ISZGaz1MX5EAJ63zG75HpJcZ-JA2bLjPQVSWN2rJjD8iE_w9p0cZkpp-Y7JzJXiwELO4PybBpO6ki_rR-ruEEdz1zm77sQ2pfS1bITyVQx7LtPJ7oMprwPecDNrIcKt5HJk0wSruKTiXjgfpa--1H91gfsPQW6Bx1skaZt-3ukrvLNwW7atjAWpVtS6Opb_XaDfWBzFGhOoVHIyAalMnc8a3CPCvTuBRbIdomupe0PTDMrJIpf31N7LOQImeCwMcxKr-4umcpt-jyXQSxC4_3O1bEqldMGGR4_RJMqEp_446aFpbYFOt-_oZ9YVZSrmzCpWCCSKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قطع سراسری اینترنت در ایران به روز ۸۶م رسیده و همزمان توجه رسانه‌های جریان اصلی به این موضوع داره کمتر میشه. انگار دنیا معمولاً به رنج و فاجعه‌های طولانی عادت می‌کنه؛ مخصوصاً وقتی قربانی‌ها صدایی برای دیده شدن نداشته باشن.
Iran’s nationwide internet shutdown has now reached its 86th day, while mainstream media attention to the issue continues to fade. It seems the world gradually gets used to prolonged suffering and ongoing disasters — especially when the victims have no voice powerful enough to keep themselves visible.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/ircfspace/2377" target="_blank">📅 08:51 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2376">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/a874f4f669.mp4?token=d_vr-lcbI0N3L7Bj4ENb7OkjNPEhbzS7AR1nRVN1vnA3l1lorXjv13B7NpZm3lXHF537WVW3KeTboiOu6usyC0orYOh77GmZwqi7DKJQ-tp5BfQBtMKce91tHxIieQQdOoXGwFI2bZissLk8bT8HFaNBrmUtt5HPUh0u35cVj17CWGwYje7-GEvFn3Yx_BzWmiBqgMEQRpcH-fy-pTO3hO-tYPJlzglBDQEU-K6QbpcKjkuq_s_s29nxkd0Lo4MhJcdeAiaOIMkTYtCOySOW9HPEyPJYEVzklqO92j4p8vm5L3Skasli6fGGsJX5IVFxx-P8L5Ze8P8exUxjdM-PoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/a874f4f669.mp4?token=d_vr-lcbI0N3L7Bj4ENb7OkjNPEhbzS7AR1nRVN1vnA3l1lorXjv13B7NpZm3lXHF537WVW3KeTboiOu6usyC0orYOh77GmZwqi7DKJQ-tp5BfQBtMKce91tHxIieQQdOoXGwFI2bZissLk8bT8HFaNBrmUtt5HPUh0u35cVj17CWGwYje7-GEvFn3Yx_BzWmiBqgMEQRpcH-fy-pTO3hO-tYPJlzglBDQEU-K6QbpcKjkuq_s_s29nxkd0Lo4MhJcdeAiaOIMkTYtCOySOW9HPEyPJYEVzklqO92j4p8vm5L3Skasli6fGGsJX5IVFxx-P8L5Ze8P8exUxjdM-PoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بازم خداروشكر كه الحمدالله، وگرنه والا به خدا
🤡
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/ircfspace/2376" target="_blank">📅 08:40 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2375">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">رئیس کمیسیون تولید سازمان نظام صنفی رایانه‌ای استان تهران با انتقاد از تداوم محدودیت اینترنت گفت: پیام‌رسان‌ها و پلتفرم‌های داخلی هنوز نتوانسته‌اند نیاز کسب‌وکارها را تامین کنند و مشکلات فنی و محدودیت‌های ارتباطی همچنان پابرجاست.
حسین ریاضی اضافه کرد: راه‌اندازی اینترنت پرو و اینترنت ویژه برای برخی گروه‌ها، نشان می‌دهد که خود سیاست‌گذاران هم پذیرفته‌اند محدودیت‌های فعلی، فعالیت شرکت‌ها و کسب‌وکارها را مختل کرده است.
او با اشاره به آثار طولانی‌مدت اختلال اینترنت بر فضای کسب‌وکار افزود: ماه‌هاست درباره آسیب‌های ناشی از محدودیت اینترنت صحبت می‌شود اما هنوز مشکل به شکل اساسی حل نشده است. در عین حال، ایجاد این محدودیت برای اینترنت باعث حساسیت و نارضایتی گسترده در جامعه شده و بسیاری این وضعیت را تبعیض‌آمیز می‌دانند. /دیجیاتو
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/ircfspace/2375" target="_blank">📅 08:36 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2374">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/usa2L3Guq-ena1H1PEIsq6ih8vc6C_3QpvD4LFvSezr99C7Ly1ACOmnwHVdZQh-kZ8BO_XeNjArD3a-b1ZSk-ctzM2qxn_KmZ8qYA4sB94p6ulUqrXO_nREG78uSZTGo5dGl28wMnNgshemHNs5Kzbp1R2lff75gelwYTX70fKwFRkktKPvAN372cf5gW4zhsHp23dDmQ43MzRGMCZK2eK-CNW0VwxtY3It0lodyoUAvO9ODKlLR0hkhMYliJwqHLXHqimr1kKhYymhYYyo2xAP936FBzvj6DV8zV4R1TsdUPKmehyKmFgUb7G5wCNHboKQdg0RQvYxx4psZ6Hz9jA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۸۵ روز از قطع سراسری اینترنت در ایران گذشت!
قطع اینترنت در ایران، یک پروژه چندوجهی است. قطع شده تا بین "هواداران پهلوی" و "پهلوی" فاصله ایجاد شود و همزمان عده‌ای بتوانند روایت جعلی بسازند.
صدبار دیگر ایران بمباران شود، نظام با بمباران تغییر نمی‌کند؛ چیزی که جمهوری اسلامی را ساقط می‌کند، آن مردمی هستند که شعار دادند "این آخرین نبرده، پهلوی برمی‌گرده" ...
با تمام دشمنی‌ها، سرنوشت محتوم ایران محقق خواهد شد.
©
AmirHadiAnvari
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/ircfspace/2374" target="_blank">📅 08:38 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2373">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hKI1dRYfwEBydGILSbwxZkz_lUrObJJMvWcu3GAQ80AyilskC6_TuT06RY9BQQtnTIgp4DHo6Meg5CG4HFfWR5B6bvUYBUHz2oqsquvBX2uM5LwYMDvpX14V9ybrSQVasY-7stbXZ6x3IOn8OxE0la7jP2MzIStZ4q4QwOaykWIQ91oVhYaym-t1GMME-8njFxVLAwIJ6AoTB_3Ootl4uZKIdNwyUcWo0V50962JdoLO3j8maSkZZDYoyHbUc_7FRc4bjhscBXlrR7y94omA4vSBBjUAE38IHnWke3juGShoilmvhhvjKHziW-PUc8QNfIPV_2vrJW_i2nPY-qz0fQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طی یک عملیات بین‌المللی، سرویس VPN موسوم به First VPN که توسط مجرمان سایبری، گروه‌های باج‌افزاری و هکرها استفاده میشد، از کار افتاده. در این عملیات بیش از ۳۳ سرور توقیف شده، دامنه‌ها و سرویس‌های Onion بسته شدن و یک مظنون در اوکراین هم بازجویی شده.
مقامات میگن این VPN در تقریباً تمام پرونده‌های بزرگ سایبری یوروپل دیده شده بود و برخلاف ادعای بدون لاگ بودن، نیروهای امنیتی به دیتابیس و اطلاعات کاربرانش دسترسی پیدا کردن و هزاران کاربر شناسایی شدن.
©
eurojust
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/ircfspace/2373" target="_blank">📅 08:15 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2372">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">جمعی از سازمان‌های مردم‌نهاد و فعالان حوزه حقوق کودک، با انتشار بیانیه‌ای نسبت به تداوم محدودسازی و طبقاتی‌سازی اینترنت در ایران هشدار دادند و آن را عاملی در تشدید نابرابری آموزشی و اجتماعی، به‌ویژه برای کودکان و نوجوانان دانستند.
در این بیانیه که به امضای ۱۹ نهاد رسیده، تاکید شده دسترسی آزاد و برابر به اینترنت، بخشی از حقوق بنیادین شهروندان، به‌ویژه در حوزه آموزش، دسترسی به اطلاعات و رشد فردی است. این بیانیه، با اشاره به تعهدات بین‌المللی ایران از جمله پیمان‌نامه حقوق کودک، محدودسازی اینترنت را در تضاد با این تعهدات دانسته و همچنین با اشاره به نقش اینترنت در آموزش و معیشت خانوارها، تاکید می‌کند که اختلال در دسترسی بر شرایط اقتصادی و امنیت روانی خانواده‌ها نیز اثرگذار است.
©
hra_news
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/ircfspace/2372" target="_blank">📅 19:51 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2371">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Not-HzoRWW4jSOFPyF3BgpUgveMMUg8rp6s9nPZj-dRzUAMatV7xHnF5_xw0EhbRLDO-dDRal0rNhz1KYiO2KNMDDN49bT-CAhOwL7-JiZ-kJZS0Je8Tr3sLLZmI50rACuvcpwtCHN8wcYMd_NrBELJiBCEpIGQlF7pZcU22zlB6v7CnKoxqlYDv4gD1TV1wppKgHo3Jt6lqK2gD7NxsThdHfqD8k74iGvW5dOQWpxo0kgdpJOerllm7H1D-qGNgQAUHmOuzuB_wHiP2H-gVs60qDokd6zWuS1qFMR0iZWzhLqHDJd_PFRBZjJoSz3Uzq9sEBszi2u5MQMEy37wxeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نت‌بلاکس: قطع سراسری اینترنت در ایران با ورود به روز هشتاد و چهارم، از ۲ هزار ساعت عبور کرد. هر ساعتی که می‌گذرد، شکاف‌های اجتماعی و اقتصادی عمیق‌تر می‌شوند؛ به‌طوری‌که هرگونه ارتباط با دنیای خارج به جایگاه، تبعیت و امتیاز وابسته شده است.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/ircfspace/2371" target="_blank">📅 19:45 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2370">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">خیلی راحت آمارسازی میکنن و میگن ۹۰ درصد مردم با قطع اینترنت مشکلی ندارن؛ به همون راحتی که احتمالا قراره تعداد ثبت‌نامی‌های سامانه
#جانفدا
از کل جمعیت ایران بیشتر بشه!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/ircfspace/2370" target="_blank">📅 20:18 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2369">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">کسانی که قبلاً کانفیگ می‌خریدن، الان ترجیح میدن دیگه نخرن، دلیلش هم تکراری شدن خبرهاست. دنبال کردن مجازی دیگه اون‌قدر براشون ارزش نداره که بخوان بابت هر گیگش خدا تومن پول بدن.
از اون طرف، کسایی هم که سیم‌کارت پرو گرفتن، خیلی‌هاشون توی کسب‌وکار خودشون موندن. چون درسته اونها اینترنت دارن، ولی دیگه کسی نیست که بخواد تبلیغشون رو بخونه. تقریبا اون چرخه‌ای که باید بین محتوا، دیده شدن و فروش می‌چرخید، به بن بست خورده و کل سیستم رو از کار انداخته.
©
NR2OH
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/ircfspace/2369" target="_blank">📅 20:12 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2368">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ksnY6ePWiRukI5vHMHYrq0X8qsZAu-fTX9iYnqbEsLzgReK3mNPMsNCKYenpmB6vnbtkIZAufmcDNT2OPysAQlmInM_dwyG2q7szmpb3OSpNQjnuHVk6b-Nf1JYpcYfa_wjkUnQ6W4MLKuWsAWvkW8mBFeKoQ1umQLvCAnf7jW-ROqBHNDKwJbyRAlMmuPTRO_AZuMK9twxC8EIJviYQ4adj_1ETLKLeroXtVqNSU5CuEjfn6Gy0m0ZZVD4Gg0WRyzNBFTWYrGIsq_egHSRYfJKArAsrKZhR0JX9s4bbhxz6dWPT3OHuewclHEkMauLor4r8HM2b-w2zHKdX1TZK6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمدرضا فرزانگان، اقتصاددان حوزه خاورمیانه در دانشگاه فیلیپس ماربورگ آلمان، گفته است حدود ۱۰ میلیون شغل در ایران به‌طور مستقیم یا غیرمستقیم به اقتصاد دیجیتال وابسته هستند.
او به وال‌استریت ژورنال گفته محدودیت گسترده اینترنت باعث کاهش بهره‌وری، تضعیف اعتماد کسب‌وکارها و افزایش نابرابری می‌شود؛ زیرا در چنین شرایطی تنها کاربران ثروتمندتر یا افرادی که به ارتباطات بهتر دسترسی دارند، می‌توانند اتصال پایدار و قابل اتکا داشته باشند. /دیجیاتو
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/ircfspace/2368" target="_blank">📅 20:09 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2367">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/V7OodAJAo6Lr0QNtjbhbEGz9u6myH5oKN1ieiXzCfEm7F9mHHXIGTyzBbDrCkX5w-2EIBnjw6zd1enBLbSa7WzPADjUEyVAf1flPxedTeGa4TZyzp-0XV9rTMGItfybNyA5MWEcXcufVyjG01T6PptD0GWsFOLAwES7XsYylfz7bPa2AVmQIcR3VsHGQMrJV37rOWrXhM0KH7eRJYqIe_TAIRSu1Wnu8N8ifHvBbzbvLfYDIlVoZ4NxtvEwoGeA5d6ms7THtNzpnirZRVKJ3IL3d7OtN5HB-Jt2aG4LHyuFZrU-U-_mLSry-Bz6u4okHkPZ6vvwjUvHK9siBX2zQxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زارع‌پور، وزیر قطع‌ارتباطات دولت قبل گفته "جمع‌بندی رئیسی این بود که اینترنت به خاطر هیچ‌چیز نباید قطع بشه"، ولی یادش رفته که رئیسی با ۶ کلاس سواد حتی جمع و تفریقشم افتضاح بود.
جهت یادآوری واسه
#قوه_عاقله
، اینستاگرام و واتس‌اپ توی دولت سیزدهم فیلتر شدن!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/ircfspace/2367" target="_blank">📅 20:04 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2366">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">یزدی‌خواه، نماینده طویله مجلس گفته "در شرایط فعلی تصمیمی برای بازگشایی اینترنت جهانی وجود ندارد" و "با قطع اینترنت، کسب‌وکارهای مردم از جهت ارتباطات بانکی، خرید و فروش و بسیاری از سایت‌ها همچنان در حال خدمت‌رسانی هستند و مردم مشکل عمده‌ای ندارند".
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/ircfspace/2366" target="_blank">📅 19:52 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2365">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SA7ZYphLbDLAodeUWwW5YPMqqnTIv2Q0klXYbb-CkwXUmpNMtbZPhgAQJLUrPUp-OsXVpSljzK0_NuXyV2C5w3_PTiuwpibtJ8ymhKcIe3Kx_PWhV_NiBaYARhEdaXI4ht94Cfht60eL67K69CVhPor36bPg2YY4nPGqav9T-w_KHEgT8nT7j_-Hm9zrFrZ3rOhq7YT9OUXm-_xxrCOXGPGt42ZL66aZ6ouu_KPy8Uc-kTNXuIoeXQcnMcdAfolzmpJVISHFRy5wd8ZzaTEJpLxTkldS5WBi-euhaK0SjrEXP7WpMP1d-XAa0U_3mLsce3Fm9pMjzaD1qGV4q2IN0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قوه عاقله در همراهی با سایر قوا، قطع سراسری اینترنت در ایران رو به روز هشتاد و سوم کشوند.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/ircfspace/2365" target="_blank">📅 08:39 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2364">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">گیت‌هاب گفته دستگاه یکی از کارمنداش از طریق یک افزونه آلوده VS Code هک شده و مهاجم تونسته به تعدادی از ریپازیتوری‌های داخلی خود GitHub دسترسی پیدا کنه و اطلاعاتشون رو خارج کنه.
فعلاً میگن شواهدی از دسترسی به ریپوهای کاربران یا داده‌های مشتری‌ها پیدا نکردن و موضوع فقط مربوط به ریپوهای داخلی خود گیت‌هابه. البته دارن لاگ‌ها و میزان دسترسی مهاجم رو بررسی می‌کنن و گفتن بعد از کامل شدن تحقیقات، گزارش کامل منتشر میشه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/ircfspace/2364" target="_blank">📅 08:31 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2363">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">عضو هیأت رئیسه مجلس: تصمیمات مربوط به اتصال اینترنت فقط با امضای رئیس‌جمهور انجام می‌شود؛ تشکیل ستادها نمایشی است.
این هم خبری دیگر درباره اینکه مسعود پزشکیان نه‌تنها مخالف قطع اینترنت نیست، بلکه در ساختار سرکوب و محدودسازی اینترنت کاملاً همراه و همسو با حاکمیت عمل می‌کند؛ تمام نمایش‌های رسانه‌ای درباره «بی‌اختیاری دولت» فقط برای فریب افکار عمومی بود.
©
alirezaer
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/ircfspace/2363" target="_blank">📅 08:27 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2362">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/i9erDV74zIWxCzHBYc4qqiO0IzJPZnj95YklRbwG-94crCXt6NCXZYkr9foc3whyal1Mea9ShcVTes_iTidtCLX6nMAWE8e4SMrsmHTmnAlyafMyh0wCBCEcDOjso_5nr8pAZlWogo8Wv5LFuvAHyH-Bpg3HQm0D0rCjAG4FxEaLmSTCpg3_nZw2CVW8cxS1FRPnBZlznYEwN_BFS40YRbn78q7BMKFL8afFe2lPsMXX2GLVzeRWvnW1lnTHs_FUD6-OmmbLuqfp4BkMtoiHZzcUIkOnTGvGGK5w7C3pxEZ7VZ08WjtY72zcMjh11HYC--MxQLJAdJZwnWSTv_Q-pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمار نشون میده در ۳ ماه گذشته یک پاکسازی طبقاتی دیجیتال در ایران رخ داده. در این مدت سهم اندروید از ترافیک اینترنت ۲۵٪ افت و آیفون ۱۸۰٪ رشد داشته. این به معنی خروج میلیون‌ها کاربر طبقه متوسط و پایین از فضای آنلاینه. اونی که آیفون داره (احتمالا) از پس هزینه کانفیگ یا اینترنت پرو برمیاد، اونی که نداره، اونقدر دغدغه مالی مختلف داره که عطای اینترنت رو به لقاش می‌بخشه.
©
arashzd
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/ircfspace/2362" target="_blank">📅 08:24 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2361">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BMr5tVBgcnI-xGT0tcZqroxi5TIvnuiP4LH6xaqXOEWy8TJfBvqbgFhhe_X3fLjCdDHAUyV6qlcjh4JdGmFnOp43JCYTmphklbRH93KZGzqBO1fghfMLgca_usVWuEu3MbAM25YrL9xaEPWltx7wkYnHTXTpnhMvesFFTIrVbQf8Bp2_gO2u76a1M_bCDz82-onKtCz9WWxpmbPJIJL7IAJI1JQYfK2R5J0RuD4mt3o6knUHN5yhSYYvz1ia1Owfjb890a4cR1FsPb_x8kgEof2u8PCDN88Za1s3vofsdjfIT19_bWF33O4DdW5vvjOLWYImUlHIHJ8gZx8vOVnrbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هشتاد و دومین روز از قطع سراسری اینترنت!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/ircfspace/2361" target="_blank">📅 09:00 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2360">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">قطع اینترنت به خاطر تأمین امنیت، یک دروغ بزرگ است
گفته شده قطع اینترنت به خاطر تأمین امنیت زیرساختی، نرم‌افزاری و سخت‌افزاری است تا کمتر مورد حمله‌های سایبری قرار بگیریم، در حالی که این یک دروغ بزرگ است. حمله‌های سایبری و ناامنی زیرساخت هیچ ارتباطی به قطع اینترنت ندارد. متخصصان به این‌گونه دلیل‌تراشی‌ها پوزخند می‌زنند. البته نه به این معنا که زیرساخت مخابراتی ما یا زیرساخت شبکه ملی اطلاعات ما در حال حاضر امن است؛ نه، ناامنی وجود دارد، اما قطع اینترنت کمکی به تأمین امنیت زیرساخت نمی‌کند، بلکه لطمه بسیار جدی‌تری هم به امنیت زیرساخت می‌زند.
در همین مدت دو ماه و نیم گذشته ده‌ها آپدیت امنیتی برای باگ‌های «زیرو دی» یا اصطلاحاً باگ‌های روز صفر داده شده است. این‌ها باگ‌هایی هستند که می‌توانند دسترسی بسیار بالایی برای هکرها ایجاد کنند؛ روی گوشی‌های مردم، روی مودم‌ها، روی شبکه‌های صنعتی داخلی. این‌ها هیچ‌کدام آپدیت‌ها را نگرفته‌اند. آپدیت‌های ضروری‌ای که حتی یک روز به تعویق انداختنشان گاهی باعث ایجاد ناامنی می‌شود، الان بیشتر از دو ماه و نیم است که دریافت نشده‌اند و ما با یک بمب ساعتی در ناامنی زیرساخت شبکه کشور مواجهیم.
من فکر می‌کنم وقتی بحث امنیت مطرح می‌شود، بیشتر از اینکه منظور امنیت شبکه و زیرساخت باشد، منظورشان کنترل افکار عمومی و جریان آزاد اطلاعات است. اگر با این چارچوب امنیت را فهم کنیم، بنظر می‌رسد حق با این آقایان است؛ قطع اینترنت قطعاً باعث جلوگیری از جریان آزاد اطلاعات می‌شود. دلیل اینترنت پرو هم اتفاقاً همین است. اینترنت پرو نهایتاً شاید به یک یا دو میلیون نفر ارائه شود. یک یا دو میلیون نفر با ۵۰ یا ۶۰ میلیون کاربر فعال ایرانی خیلی متفاوت است و باعث می‌شود جلوی جریان آزاد اطلاعات گرفته شود و در واقع کنترل افکار عمومی و کنترل جامعه راحت‌تر شود.
چطور اینستاگرام یک پلتفرم آمریکایی است و ممکن است لوکیشن و اطلاعات مردم را در اختیار مثلاً نهادهای امنیتی آمریکا بگذارد، اما سیستم‌عامل اندروید که متعلق به گوگل است، نمی‌تواند چنین کاری کند؟ اساساً منطقی که مطرح شده، پر از اشکال است. وقتی شما اینترنت را قطع می‌کنید، عملاً یعنی تمام زیرساخت‌های رشد و توسعه یک جامعه را متوقف می‌کنید. به یک معنا، ما با این مسیر داریم گام‌به‌گام به عصر حجری نزدیک می‌شویم که در آن از فناوری اثری نبوده.
©
hamedbd
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/ircfspace/2360" target="_blank">📅 08:56 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2359">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">امروز هشتاد و یکمین روزیه که اینترنت ایران بصورت سراسری قطع شده، ولی پروپاگاندای حکومت بدون لگ داره کار می‌کنه.
امروز هشتاد و یکمین روزیه که جمهوری اسلامی داره
#روز_ارتباطات
رو با قطع اینترنت جشن می‌گیره!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/ircfspace/2359" target="_blank">📅 08:59 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2358">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/N2Gad7mSJr7NlHBHXSUYbQ4P5XJbkG-L9f9uaAGAkgZaT483gV4Z8B8wM4DGM-NpG0sGmk-prvYt3P79zypOD0bjjoEsxCfxSMW-nFle7ZhB7O3Ben6UBBEGI-gseXv0T7ftWW8Uc3QOOWSsA076XqDi_cfEUXMa-DIcyrvVgsiuU3MBj0pKmJVEVfgzVXHweRfpZXIPvajFu_q7_g-uXnL2FEbE0qEgEBc7_YHiCkL1c4NYyFUHbNWPlvVlZwG_OP4rT36T-jnkIb3oWXlteI7y1hZC8IC5TSoGy_sk6MCJoygPjKRWv9Py24xXNEuLnKDR_8yCJSKP_l91sJaciw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در بروزرسانی جدید از اپ Network Checker برای اندروید، ویندوز و لینوکس، قابلیت اسکنر آیپی Akamai (جهت استفاده در اپ
#شیروخورشید
) اضافه شده.
👉
github.com/mirarr-app/network-checker/releases/latest
💡
t.me/PersianGithubMirror/5227
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/ircfspace/2358" target="_blank">📅 08:50 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2357">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tK-w3yYCgQOP9aE2yoemiUYwIin3e7afqNEyGcYgiv5xYMuac_7rQpUNg71GIMKIRbt5X9042w8w9-Hpt9hGaP435GGdBnN-E1zvOUQGpPgSNtpHYpzlkU4etaSocMdqiwB8ZTi4j78fb_qBszk3l0cMjSEipvHWm_g7U_KXJuWJvJMTFVkNhfTLftpq7Pr6XbR_tRvaGT3uNUEJ2PzPicnIT1PA8Kh5mgTFhvbplrvMKZNeFc-cDXBQ_zmmzB8HmAc_LFQtUBeRpgPjLsJjlZma-F5UZ84D9gLkRLuOhDdUKmjEYgSt14gtlMy5cPFk85WcnzBjauAXAmbMZypJXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ NexaTunnel یک کلاینت رایگان برای مدیریت تانل‌های StormDNS در iOS هست، که به شما اجازه میده کانفیگ‌های مختلف رو وارد و مدیریت کنین، وضعیت اتصال و ترافیک رو بصورت زنده ببینین، DNS Resolverها رو تست کنین و خیلی راحت بین پروفایل‌های مختلف سوییچ کنین.
این برنامه با رابط کاربری ساده طراحی شده تا بتونین وضعیت تانل، سرعت دانلود و آپلود، پینگ، IP عمومی و سلامت اتصال رو بطور لحظه‌ای بررسی کنین و مدیریت بهتری روی اتصال‌هاتون داشته باشین.
👉
apps.apple.com/us/app/nexatunnel/id6766783641
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/ircfspace/2357" target="_blank">📅 08:38 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2355">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">توصیه اکید من اینه که برای وصل شدن به اینترنت سعی نکنید از سرویسهای ایرانی (خصوصا سرویسهای متصل به نهادهای امنیتی) که شمارو قبلا احراز هویت هم کردن، سو استفاده کنید.
به هیچ وجه حتی برای امتحان کردن هم ارزش ریسک کردن نداره. و به هیچ وجه هم روشهای مربوطه رو معرفی یا پروموت نکنید! اگر کردید بهتره همین الان پاکش کنید. از سر دلسوزی میگم، بچه‌هایی که از چندسال پیش در ایکس فعال بودن میدونن دارم در مورد چی حرف میزنم.
©
aleskxyz
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/ircfspace/2355" target="_blank">📅 20:07 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2354">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/m8IDTfUfC1O-9qV-Zgz8YAm4wWy7cJ66I4_Cfjs4pLeaUiOPK0Up9l1HtgWji7xbl2Q_a77LQFguQADR1tmXNTnG5QuhO7pHsfQtVq2l75TBHAJ1xsewD7-YmZHaBlLajd0lZUU08iA1bLm3gGKcsV_Ty32ZWTns6d_ghZV67RLpqRzMdvuzrNGARg8EJErmxyzy242l2PKNrzmUWCJHuZdT9DsXIYECJuChz24fJEYcjhthvAQrsKJ_FxKYO7Cf6Cy91ZP09uzigQoX5fml5lqDTjx9hlZQsrNNDwbChBdz28n3xZXf0ZA7pvYeFWMaMvXpywpgXl5HrsgD7sJm-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ما در انجمن تجارت الکترونیک تهران تجربه واقعی کسب‌وکارها در زمان اختلالات ارتباطی را مستند کردیم. از میان ۹۴۴ کسب‌وکاری که به نظرسنجی پاسخ دادند، بیش از ۸۰٪ اعلام کردند در زمان قطعی اینترنت، فروششان بیش از ۵۰٪ افت کرده است.
اما یک نکته مهم‌تر در داده‌ها وجود دارد: حدود ۳۳٪ کسب‌وکارها گفته‌اند در زمان بحران، «پیامک» مهم‌ترین ابزار ارتباط با مشتری برای ادامه فعالیت آنهاست. پیامک در زمان اختلال اینترنت، یکی از آخرین مسیرهای باقیمانده برای حفظ ارتباط، اطلاع‌رسانی، پشتیبانی و فروش است.
حالا تصور کنید پیامک هم قطع شود. بیش از نیمی از کسب‌وکارها گفته‌اند با قطعی پیامک، افت فروش جدی (بیش از ۳۰ درصد) خواهند داشت. پیامک بخشی از زیرساخت تداوم اقتصاد دیجیتال است؛ نه یک سرویس فرعی.
©
NimaQazi
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/ircfspace/2354" target="_blank">📅 20:05 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2353">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BO1S16WqYDmU4STk8p4-pMqt4833OK-Iuz4fW4YAXVpg0Jmm3h6YlV3dZCvzjgqdZ_DiuHPVENPckAXNYt4rgNvlJUJ7FiLJ0OAbcGLUUhukw57XnMXoLJpp6NLjHztLHGaK7TA5Ef2X7v1FbHW-30nNsw4EVZVi3r59Rg0gkPbjBXTW022NR7rads3kdtKmHA-aUmmwbbbxXXdjAwyef8LfYmKmn_Io5XKdMfMGpNwC2K-xEX1ddAVFav-E7s_WilsGU2rUWg0C5nVFgGLuHkUjUfP7VAmUCAeo1EJcZYyU4NW12ocR76BreZOWRnqqn0csVAJV43OTf-gksbHKCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باید به افتخار وزارت قطع‌ارتباطات ایستاده
شاشید
!
آیندگان در کتب درسی از تمامی دست‌اندرکاران فیلترینگ و وزارتخونه‌ای که اسمش ارتباطات بود اما ۸۰ روز متولی قطع‌ارتباطات شدن، بعنوان
#قصاب_اینترنت
یاد خواهند کرد.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/ircfspace/2353" target="_blank">📅 16:24 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2352">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/H7NJaCfG-AYnVHIK8E_9fNoPzoF6Qu8yJDckVACOwqB1fk8YKGy3Soka9Pc89Cw7EDZkWEcMfzsjMHBoHvGKrrJ_B_Y8UtzuhaFkNEIFsyJpG_uM69wIlhBjPIV4tff2eEtvlLJ93N5BV02uLzVZCOK4nLjCHgX99wQrtIivPiB1pjr4m3y50YAcVJnBkKWeWG_d2cpunUH0ep4hnz6ooLcRMZqfOnlObZ3lFjBc4TI1F40VzU0QeQuUpZcKJJKnlcj9nLp7VhZDMr_tWWbpg1t8iPpJbaFkJ4TwsueBfi3Xk-6Q_e4Z7LvkikWi2LmRU3HJGT6mPY2rxGUxEWnLyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ستار هاشمی از پایداری شبکه ملی اطلاعات در دوران جنگ تمجید کرد و گفت: شبکه ملی اطلاعات کارکردهای متفاوتی دارد. در شرایط جنگ شاهد پایداری شبکه داخلی کشور بودیم تا ارتباط بین مردم قطع نشود و خدمات مورد نیاز مردم ارائه شود.
وزیر ارتباطات افزود: در دولت چهاردهم نشان دادیم شبکه ملی اطلاعات ورای یک شعار در میدان عمل کار می‌کند. این اتفاق بی‌نظیر و شاید در دنیا کم‌نظیر است. /دیجیاتو
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/ircfspace/2352" target="_blank">📅 16:21 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2351">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VJFWRKSbNPJyqNNDTyy1f1VXKNDfLUeOUlIyorOd113QHyFQFPPDSQy1LZIwihNAWMP3xzALPmT66Dn8l1cFlPO-aA5joXxgJZAi0-77gwyR-1AEg9XoAj11N-eY-idEwmBbfHT91Q5M10ZM5my7RsNnhRqhR2pfIla5I_F-_ZvdXU6tKJRpqkYnSW-31rjm6nM9csWL1ZopeLHI1wgepnqzAiV_Fx5lL3nQtROPAFPLDHrekwOopKGj4IrOCprAyfC_6R7Pq5Sy8r7bC3_Wjc_bn8XewjoaDvsCYFMi3Dgu6tNZ2u6m074GUupR2GpgrLrHClOr0EP8rq0lXfXEkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ اندروید
#چشم_عقاب
نه فقط یه خبرخوان، بلکه یه راه آفلاین برای دسترسی آزاد به اطلاعاته، که بدون اینترنت، بدون VPN و حتی بدون داشتن مجوز اینترنت روی گوشی، خبرها و اطلاعات رو مستقیما از ماهواره روی دستگاه شما میاره.
کافیه کانالش رو روی فرکانس 10762/27500V ماهواره ترکمن‌عالم باز کنین و دوربین گوشی رو سمت کدهای QR که روی صفحه نمایش داده میشن بگیرید، تا اپ در چند ثانیه اطلاعات رو بخونه و روی گوشی ذخیره کنه.
اپ فقط به دوربین دسترسی داره تا QR Codeها رو اسکن کنه و هیچ عکس یا ویدئویی ذخیره یا ارسال نمی‌کنه. تمام محتواهایی که دریافت می‌کنین، قبل از پخش با امضای رمزنگاری‌شده Ed25519 تأیید میشن تا اپ فقط اطلاعات واقعی و معتبر رو قبول کنه.
👉
play.google.com/store/apps/details?id=com.filtershekanha.cheshmoghab
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 77.3K · <a href="https://t.me/ircfspace/2351" target="_blank">📅 10:02 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2350">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">باورم نمیشه قطع اینترنت به ۸۰ روز رسیده!
وقتی حکومتی برای حفظ خودش حاضر میشه یک کشور رو وارد خاموشی دیجیتال کنه، یعنی مردم هیچ اولویتی براش ندارن؛ وگرنه امروز وضعیت اینترنت، اقتصاد، مهاجرت، ناامیدی و زندگی روزمره‌ی مردم این نبود.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/ircfspace/2350" target="_blank">📅 09:21 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2349">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QBBJpDi4myemjpVnHmH20EE2fK2KO6GCIa-7qutY03PPrJ1Vt4CtGfAwq5Bo6G-2_bwTROhdeQ_ApLVARfQr1IEFVi9mvDJeDV2Z4HMRLcLlNzt1wKleBgJxMHv3xUSTxWd5VZKhJB6uq0X6QuxQTPNA_g8g-yG6uJwgLZjxVf1FRTwh9BJvPFvKqs3zMm3oKsLLNFgeK_oeyokR-C_2DOjbEY1FUIKw7UAnCOk9qDBeO5sCeyuBgUtNFIQPUTYO39a2FeBJzaBcra8m13w83x9AnWHGmOkV62CjDEyxujzZsa5StS8ey8RWF3EgyFC7JvXOurSx0-T6o0dB879CSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسعود پزشکیان بعد از ۷۹ روز قطع سراسری اینترنت در ایران، روز جهانی ارتباطات رو تبریک گفت!
🤡
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/ircfspace/2349" target="_blank">📅 21:08 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2348">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ljPJad39EVemNWuzC3qqFR65sbcmcCFhngJDkKEj8GzBa1NnUAZ2Y8Vo7ZaS6crr-Dx6Q6zWcTq16iitpUHpC3y6ajkLDMkD6VRwdEUmM9dFabLV_hGrXpBNVkQ3UkWfLkWq6HNy-z_PeUSad9TqT9yzf2yqKbADrRBzyazIJuC5PU8blkdvfMJIFAqseaOrvjWxawU2oHZ506loeE8G7Ud-Q9-4omwhO9HN4s0AmAFG6-_uKIE03oyBInzLOozJfWTAalrUvGcWTs9Hyt87RZeIVM8OPkm00SlA-oDsdrNZfHMdKMfBej7ocfSXfILLh6PY2DPUb8fbDAdMav-2BQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سیمکارت‌های بدون فیلتر، حفره‌ی جاسوسی برای مسئولان!
در رابطه با قطع سراسری اینترنت به بهانه امنیت و اعطای
#سیمکارت_سفید
، سیتنا در مطلبی نوشته: طبق منطق فنی، وقتی با سیمکارت سفید و بدون فیلترشکن به اینستاگرام، واتس‌اپ یا سایر پلتفرم‌های خارجی وصل می‌شوید، هیچ لایه واسطه‌ای برای مخفی‌سازی وجود ندارد. یعنی دقیقاً در همان لحظه‌ای که یک مقام مسئول درحال چک کردن دایرکت‌های خود است، اپلیکیشن‌ها لوکیشن دقیق او را با کمترین خطا رصد می‌کنند. اگر نفوذ و ردیابی، خط قرمز امنیت ملی است، پس چطور با دسترسی‌های ویژه، عملاً موقعیت مکانی لحظه‌به‌لحظه خود را تقدیم سرورهای خارجی می‌کنند؟
تناقض وقتی اوج می‌گیرد که می‌بینیم مردم عادی برای اتصال به همان شبکه‌ها، مجبورند از کانفیگ و پروکسی استفاده کنند. این ابزارها با وجود تمام دردسرهایشان، حداقل یک لایه پوششی ایجاد می‌کنند که لوکیشن واقعی کاربر را تغییر می‌دهد. اینجاست که بوی یک تجارت کثیف بلند می‌شود!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/ircfspace/2348" target="_blank">📅 08:49 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2347">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">اینترنت برای عده‌ای خاص، محدودیت و خفقان برای بقیه مردم
امروز هفتاد و نهمین روزیه که جمهوری اسلامی اینترنت رو به روی مردم خودش بسته، تا زیر سایه‌ی خاموشی دیجیتال، سرکوب، اعدام و پروپاگاندای خودش رو پیش ببره.
چندماه هست که هزاران کسب‌وکار اینترنتی لطمه دیدن یا نابود شدن، اقتصاد ضربه‌ی سنگینی خورده، تعدیل نیرو و تعطیلی‌ها بیشتر شده و مردم حتی برای ساده‌ترین ارتباطات روزمره هم با مشکل مواجهن. با اینحال هنوز هم بهانه‌ی امنیت رو تکرار می‌کنن!
این قطعی تکان‌دهنده معلوم نیست قراره چندروز یا چندماه دیگه ادامه پیدا کنه؛ اما همزمان جمهوری اسلامی با پروژه‌ی اینترنت‌پرو هم جیب خودش رو پر می‌کنه و هم به رفتارهای متناقضش ادامه میده؛ یعنی اینترنت آزاد برای عده‌ای خاص، محدودیت و خفقان برای بقیه مردم.
در این بین، عده‌ای در شبکه‌های اجتماعی تلاش می‌کنن با فضاسازی‌های ساختگی یا حتی ری‌اکشن‌های فیک، تصویری غیرواقعی و عادی از وضعیت کشور به دنیا نشون بدن؛ رفتاری که علاوه بر نبود بلوغ فکری و ناتوانی در درک عمق بحران و رنج واقعی مردم، برای خیلی‌ها نشانه‌ی هم‌پیالگی با ساختار سرکوب یا فعالیت‌های سازمان‌یافته‌ی سایبریه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/ircfspace/2347" target="_blank">📅 08:31 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2346">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Wi7AAsMZ0g6rcayk_1RzVBAMJSJsO27idQHNljV26CAZuN_rWmfZGompxvMYkrEfT2GFIzFT6v5R-_rVs7oNGkyEbT7Q_1Recf81qHpwPrEmA5RFr2Iwra70qFylvbvj01whvUHiPS4dHtXCrRMC3CMXaNeGuX-ledOW5Lvi897pCdHOg6ENqp76IrlNWjhtvI_g46ta8S5-fPWDkRbANazAz9kM1lZt1683gi50oIUI6etjGAjGCfd6d-9PPWVYNCDu8kL72CuGoA_v8Tgl_Q1AIb-2K8do_sfWDvmzjKJ_fszk-6T8mAKiaOy-q2N3McHfw3HPp-mP8Qk9XbhRxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه ۱۶ از فیلترشکن
#MahsaNG
برای گوشی‌های اندروید در دسترس قرار گرفت.
در این آپدیت هسته‌های MasterDNS، GooseRelay و FlowDriver اضافه شدن، قابلیت CDN-Fronting سایفون تعبیه شده که میتونه شانس اتصال رو در برخی محدودیت‌های شدید شبکه افزایش بده، امکان وارد کردن دستی HTTP Type لحاظ شده، یه سری از مشکلات رفع شدن و اسکنر DNS حالا IPهارو بصورت تصادفی بررسی می‌کنه تا نتایج بهتری ارائه بده.
👉
github.com/GFW-knocker/MahsaNG/releases/latest
💡
t.me/PersianGithubMirror/5051
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/ircfspace/2346" target="_blank">📅 23:40 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2345">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">اپ
#شیروخورشید
بعنوان یک فورک از اپ رسمی سایفون بصورت متن‌باز ارائه شده و توسط گیت‌هاب اکشنز بیلد میشه.
آپدیت جدید این برنامه تونسته دسترسی هزاران نفر به اینترنت رو در محدودیت‌های شدید فعلی فراهم کنه و همونطور که انتظار می‌رفت، افرادی سعی کردن برنامه رو به حاشیه ببرن و برای کاربران نگرانی ایجاد کنن.
علاوه بر متن‌باز بودن پروژه و امکان بررسی کامل سورس و روند بیلد، متخصصین حوزه امنیت و افراد فنی آشنا با ساختار این نوع ابزارها امکان تحلیل دقیق رفتار، ترافیک و عملکرد برنامه رو دارن؛ نه اینکه صرفاً بر اساس برداشت‌های سطحی، حدس و گمان یا خروجی‌های بدون اعتبار AI، درباره چنین پروژه‌هایی قضاوت بشه.
در رابطه با تفاوت این روش با MITM هم توضیحاتی از طرف توسعه‌دهنده برنامه منتشر شده که پیشنهاد میشه مطالعه کنین.
روش کار کلاینت شیر و خورشید کلا متفاوت هست و اصلا MitM انجام نمیده، که نیازی به سرتیفیکیت داشته باشه! دلیل اون روش این بوده که بیرون هسته سایفون میخواستن ترافیک رو در v2ray تغییر بدن، پس باید از سرتیفیکیت خودشون استفاده میکردن (که در صورت بی احتیاطی نا امن هم میتونست باشه). در شیر و خورشید تغییر تنظیمات SNI و ... که روی ترافیک ایجاد میشه در خود هسته سایفون اضافه شده. در واقع اگه کد رو بررسی کنین میبینید این قابلیت Domain Fronting چیزی هست که خود سایفون در نظر گرفته بود، ولی تنظیمات و قابلیت تغییر درستی رو برای فیلترنت امروز ایران در نظر نگرفته بودن، که الان در شیروخورشید اضافه شده.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/ircfspace/2345" target="_blank">📅 23:28 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2344">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vs4Uwvaf_nNswlS3PbmeiDmjpadiCu6NyfQrHy89Rxy4CA15dBxDqjLOQWfcsLYYbuvcRhTfHxpVu7_u8wxPw3TGnHf7jH5pGJXIbbNqEA8KB0nV28A5qiq1lziFTnNPKUZsgAKmtESvEa8YTS1Dw6Ix_scjUq04wGwlqkYro-zDVR9pEmRLe_dT9R7Xbgq39ABjRfeu9eDQilhlB_gnqf_sFRMWojwpq7WdtxpeJ7xSxvTuO3ByaLDadowdHlwQr44C6DDIcRRa_JdDOM5vOVNt80rCVK_iem6zTGtCK_JyYEF4dbMTQtAlDlT6otP27HGWQddu3LNepSPmt0d09w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رفتن هرچی که تهش Hub داشته فیلتر کردن؛ حتی گیت‌هاب.
قوه عاقله‌س دیگه!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/ircfspace/2344" target="_blank">📅 09:21 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2343">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jg0H_pedCttdnpMlmy0peWroXIgjfkyP8uxSNILEvVOKiBEQZY3fzK-PXSGfNl74RvPF756N0DOGx0mVF2MmNxoIAP3id5BF5KzsIZzOGc_6ESJ6IVZ7KO64wpjZ7R0TiPHw5R5HyH8tOfMdWRui_7uyjKPq2dJFW-fCdjU6jUcWMk8gu1GPN0RZbDB1qwjFK3zM-iEhUwCf4VvvvHsoO_5edcGeSLJSUbdpUTUYViiuNSMUG5musVgoPB1SWB3Pg6yHETcDysmZDaJT1wNUZRHwSjQSSd1xunlCrqdiiJh0ptp9k5RaDm21zBD6lteAwGXv3_u0PXO1FP0_Fg_n4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ متن‌باز و رایگان TunnelForge یک کلاینت L2TP برای اندروید هست، که از امکاناتی مثل حالت VPN برای کل دستگاه، حالت پروکسی با پشتیبانی از پروتکل‌های HTTP و SOCKS5، مسیریابی، پشتیبانی از چندین پروفایل همراه با ذخیره‌سازی اطلاعات لاگین، بررسی وضعیت اتصال، امکان استفاده از DNS سفارشی و تنظیم مقدار MTU برخورداره.
👉
github.com/evokelektrique/tunnel-forge/releases/latest
💡
t.me/PersianGithubMirror/5008
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/ircfspace/2343" target="_blank">📅 09:11 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2342">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZBJ607NfIUd89thEgWxoYKKfOfNtozWykPuX_xCeocCfJyTt0tqy4oooAKEweJ0eUNpvbTZUJWUdQZcLF_x4C9XMgyvo4i2GdUVZb_W15lmXd_uackNei4j999TDQmoRouOqpZrSVz-VfibNv7sqx_pTwUBw5iX-BWM5bR7-o4N9jW2mfGMiEMD34Q5BoCdveFBs6Z3jLy2fAXIkS6w3IZrqHwIPtk5nZtPW9hR8v4SMdhwVwLfiBRPnbGvsQabAq28sck3i3ai7jrTbu0YfchGiiIUmb7Myuge9SxGjL5mm77r_vsf2y3dOkmTVeI1431p7BAlav_Mxk2KUx01K1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه آسیب‌پذیری جدید به اسم YellowKey در سیستم‌عامل ویندوز پیدا شده که توی بعضی شرایط میشه BitLocker ویندوز ۱۱ رو با یه فلش USB دور زد؛ البته فقط وقتی مهاجم به خود دستگاه دسترسی فیزیکی داشته باشه. برای کمتر شدن ریسک بهتره ویندوز و BIOS آپدیت باشن، سیستم کامل Shutdown بشه نه Sleep، و برای BitLocker رمز یا PIN قبل از بوت فعال بشه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/ircfspace/2342" target="_blank">📅 09:03 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2341">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RXkk64DKLmTLRaRhU0BRZ9rmcoD8aE7CAPcHknT-g7uhmWlNz85ZSQmGZEpnmQmUmSmZKVPaGyWY4oqL6ByhsIVReq5isPKpL--d1hfQEPYb3tRA5HvU6-fdoyILRDPyU95eAhnvcEWKjYEy4pRIE6oN3v3WuDu1L6zOh55qXb_0FDerkNxeid0OULV_I2n67OaY5JK49WwkNhXAeELcH7_iooqXEfkqueyyl_ZYHMh8yoMYs4kFRLQw5-KUUF8vZoWYkHB0C_q9PQJC-YtF5UxAVezVz3ZMFU4ix1I5rWP93kXZgcuZT-hAHxwgSovyKayC1ZzSijhgtcaGak_t7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت استارلینک مینی به ۲۰۰ دلار رسیده که فعلا اشتراکش هم رایگانه. کنترل اینترنت با اینترنت پرو و قیمت‌های کذایی یه توهم زودگذر هست!
©
imanraisii
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/ircfspace/2341" target="_blank">📅 08:44 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2340">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/a6uoef6D_gnlflXUTyjL8cyimXQcyXhDN2MgYswzPNWstUZujynM0ekzjotjq4kNC14-WWTtr8eFkX4_8Oq0qRs7d3B-Fc_I0RIfQ5hRt2VA8skQhfLEsTB_Cs8bwmOXohQLxXEjryr9844y_WCVOA9CJ03DeyZwLkM55bU3OYVup8nb-iDTdchwapHiYXsu9AU2UCZyrQSz5MRX-oIGIVtmYJdoV31sVi-3dMtxLFBSFUYegtoZ7hIEA7dpgnI1coAyUvDGlixOH-SlZw87UzcielGUTofgn9VrXLdSo-B2FuwW462JdN5V9nQET4o8yEPhNJOsY0cbOcADCY2vDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در هفتاد و هشتمین روز از قطع سراسری اینترنت، از جدیدترین روش ترکیبی عبور از فیلترینگ با ذکر "لعنت بر جمهوری اسلامی" رونمایی شد.
😁
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/ircfspace/2340" target="_blank">📅 08:38 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2339">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Bn0ivw778cciel6mFysvhNELx7AB3hbO_7GY6YlMiN7U7FITphL2DGiLiXgJ9POa-jpRSTtjcJrmLvYSFR8CEZ_1206W34XXVDF85nHiWt5V6wOBczyQKy0zfFIqYJ1yp9deJVLHEiexLpD-mfCv2bOEAHs5EyelTgu-OJQ25mQef3zfX9jjkSHfi_rzjpwMvKEK6_v1n6bX8d16TEzrffjLXaBNLBPT3nWt3TsP1hkZtcEJegHgtQxHN-bpDDo__M5r_Q1OSzhFogw94wFx4kvNynd9jrMa1Qyf_2w4qY0_hscpKrsE4y8fRxZA6JlFwJnh62p4eLVl4v25ojve5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هشتگ از تبعیض بگو!
اینترنت غزه که قطع میشه، اتحادیه بین‌المللی مخابرات میاد محکومش می‌کنه، ولی وقتی که اینترنت ایران برای نزدیک ۳ ماه قطع میشه، سکوت مطلق! ۱۰ ساله در مورد ایران توییت نزده!
©
markpash
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/ircfspace/2339" target="_blank">📅 08:28 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2338">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Udh-LN9vbA979UTPre9KNJDlnmzrZ9fVuW9Z0Z-cxZnVCuA8exqLe1a6cZJqJO4Uu48ki5hI5fAn7QW7V5FDhI93WPC8SznsU4EaODysW8MZkBmyFtgNljjrHE4almH1wVwLCVbYAv5pe1zrf4eE372VlMtHhmOK91vYu89DViIbM6mMRHeB0eYyCDcVr0sjgNIrW1hUYsywbgRI8WEsyoUF5zC9V8N0L9n_YFSPTRp6IoM-hXC-SjPMpovfgW0WPgkyp0XiIOYWexJ16p--t6nUIYPHZob1GYzRMbgyMbXo1r8wx5rAHQtD28PuXr3cheHy8psYdGST3tOvnk_hWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد حساب این الاغ [توی ایکس] بسته میشه، داد میزنه که آزادی بیان نیست...
©
AminSabeti
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/ircfspace/2338" target="_blank">📅 08:27 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2337">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">تقابل اینترنت و امنیت یه دروغ بزرگه. مردم نه‌تنها  دسترسی به اینترنت رو به امنیت کذایی شما ترجیح میدن، بلکه هر چیز دیگری که خلاف ترجیحات شما باشه رو هم به انتخاب و تصمیم شما ترجیح میدن. شما هیچوقت جسارت برگزاری همه‌پرسی در هیچ موضوعی رو ندارید.
©
vahidfarid
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/ircfspace/2337" target="_blank">📅 08:25 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2336">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">ستاد فضای مجازی با مدیریت دکتر عارف در اولین روز کاری برای افزایش رفاه مردم و تحقق وعده‌های دولت وفاق ملی، گیت‌هابو فیلتر کرد.
©
pey_74
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/ircfspace/2336" target="_blank">📅 08:25 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2335">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/g5F0oMSerV6X8XaH-CP6tFhld5NfKnzYk-Ej90-uJifpZ4pOKF2DvcKSX1H_iC7gwzwEekR60biji6hILP19PP1hypydamCPIGbs4qZpTfvB2ouKjzWazohRq3-RXsIwtZmuIBKU7MmK8SYlAEG7p54QamlXA1nzim18G3cpqw76CX4wMUyIGAQbSsG2x0-WnuiDw8dIyqT_GK_kR6TPFGPSoU1sSwh2XSaSJIPyYPus2lTafatsLA6fZgOCbiRAjOypcx_mJOBe_LrJBASmt_ZLoc0MWbu8HIH5r8_LUuPT76GYMbxYa2fsOk6VsrItrLwebYG0l7ZiSIACLEEvlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روش
MITM
در آپدیت جدید از اپ اندروید
#شیروخورشید
گنجونده شده و می‌تونین بدون دردسر ازش استفاده کنین.
برای استفاده بعد از نصب یا بروزرسانی، باید وارد Options، سپس More Options و بخش Connection Protocol شده و CDN Fronting رو انتخاب کنین.
همینطور در قسمت CDN edge IPs اگر IPهای وایت‌لیست شده
Akamai
رو بذارید، سرعت اتصال بهتر میشه.
👉
github.com/shirokhorshid/shirokhorshid-android/releases/latest
💡
t.me/PersianGithubMirror/4954
©
PawnToPromotion, mahdavi
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/ircfspace/2335" target="_blank">📅 16:26 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2334">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">نحوه اتصال رایگان و نامحدود به اینترنت آزاد با متد ترکیبی MITM + Psiphon
👉
github.com/patterniha/MITM-DomainFronting
©
patterniha, MatinSenPaii
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/ircfspace/2334" target="_blank">📅 16:18 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2333">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">روز هفتاد و ششم از قطع اینترنت.
معاون دفتر پزشکیان گفته "درصورت برگزاری همه‌پرسی، مردم امنیت را به اینترنت ترجیح می‌دهند".
وقتی گفته میشه هدف از قطع سراسری اینترنت و خاموشی دیجیتال مسئله امنیت نیست، دقیقا مطرح شدن همین اراجیفه که به جای نظر مردم به افکار عمومی تحمیل میکنن.
زمان زیادی از کشتار دی‌ماه نگذشته. به جای این چیز خوریا، بهتره یه همه‌پرسی بذارن تا وضعیت مشروعیت جمهوری اسلامی دستشون بیاد!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/ircfspace/2333" target="_blank">📅 09:19 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2332">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/K8yf46vt74gW12GTXUdFbmI8yNSrEH1Eok54cCmescv72bfcKN1-cKrCoeEXdhSb_t1xVDPbROQdU-HBqip9I6ZWiwtCyG9cxQMoszFtdzJPGwLv0qeUATbKA1IypYs3k9fVJ1589uImJN1etgw_MOtktLRQWh6otJCMm4S8txGNPjmeQbsI0oYRiX3uWHsJlMieWMbZAeHIR9D13YzwRP22Di_e7ZFNB53amOj2iD0xhwYC1rcY_xZMtXOgMiog8sZhai33v8GgOanvzUtUw8cMm0GRVlkN3PW787JmO2Lq0GhRKnh7EYqIy-B_2r2SZAMEM2ahGodbPZvGLd-wrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی کمیسیون فرهنگی مجلس: امروز پیامرسان‌های داخلی گوی رقابت را از پیامرسان‌های خارجی گرفتند.
🤡
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/ircfspace/2332" target="_blank">📅 19:39 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2331">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EdxSZ8GvDw_TP088G0VHL2cbs56oGazVniUWMnhGGeOLLy2xBw68Br0DPHRhS91N7L_9RY1Y7bofW4G0PjpnKiAeM8xnPSgOG8U5WypyRPGrUA5c3b8TcSpazMGT56qzyZJn3-Fa1JPRhBpTgCCWx4xz9YTVejCzZEAuwWa2KC-rP9wYEyyxDUfpjRzFy_0snFl05P5MH5IYHc_SqBBxZo8D1vPjgM1N-ygXGIKlQDjNl_CYMC5ktAWY47Pon6nnvuI8a_GVPz68P0yvpcqGSnY8eJDOEEbbFb8nGHcL9bnSmxnPkwWdx9IToZ3uzVnbKuJ7U5ouO9bSDpXczZdtgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۷۵ روز از قطع اینترنت گذشت؛ همزمان درآمد یک کانال فروش فیلترشکن از ۱ میلیون دلار گذشت!
©
mosi115
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/ircfspace/2331" target="_blank">📅 19:36 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2330">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/P5DgU6uKBVIgb990q3wSNkxS5242Ulzr9-FeELZpwwv3MfPVCvi-Kb25TENnea9GiMH4Yyjgk-CzaymChNcPzBtAb9g0FpRjzGhiBDne3rS9lv8-YORN_yf0NMrTBu0ZH-tcy4diWUc5SJcQRKFAciD8ob6h81M-p16Iqujok_FIUa8KgvwcE7A948oVAQ8y-6WLKWqT5PzI0bj5TXNyPxS-ewPD2VqPRmXPLU-94n5Kbr4pADgJmFW2MHwm7Sa8oG6sMxzyeePQPVFY3dGxQ1pIXxsUb9JujVFSbsLBj8MneRVG3i790-LR3wNHLi_yf6CgQ1zs2aFNYQ4adgXvVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به نظر میاد مرحله‌ی جدیدی از
#اینترنت_طبقاتی
شروع شده؛ دیگه خجالت هم نمیکشن. قدم به قدم دسترسی برخی افراد و کسب و کارها وصل میشه، تا عموم مردم به عصر بدون اینترنت و بدون هوش مصنوعی برگردن.
©
vahidfarid
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/ircfspace/2330" target="_blank">📅 19:32 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2329">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">سی‌ان‌ان در گزارشی نوشته
#اینترنت_طبقاتی
در ایران خشم و نارضایتی عمومی رو شعله‌ور کرده و به نمادی از نابرابری ساختاری در جمهوری اسلامی تبدیل شده ...
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/ircfspace/2329" target="_blank">📅 19:30 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2328">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">قوه قضائیه در یک کشور مردم سالار آنجایی که حقوق مردم با تصمیمات دولت یا نهادهای امنیتی نقض می‌شود واکنش نشان میدهد. در ایران رئیس این قوه نه تنها حق مردم در دسترسی به اینترنت و کسب و کار مردم برایش مهم نبوده، بلکه چندبار شاکی شده چرا اینترنت پرو را سختگیرانه نداده‌اید!
©
alirezashirazi
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/ircfspace/2328" target="_blank">📅 19:27 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2327">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d9e9b1e831.mp4?token=XpRAvPQPn-hRwdULzzOMZ1_Atjl7xF4Gzc92VRSW6ymGfkpuAwEFd7teG-pb2Xf7YQYeXISb8iHdMZ6g3Tu0vtcqkEfrElMpvBn70cL-tTljm1jj-khtVTQgv0DzGqAryIpUEtPcengraK0H0VNV8Ssvmwjsih5Q-WvldzyX6PxjhHF6APfugeF8PHyhl6w8mQnyh-8fKiYfu7khgpPZAbriQ07wZfsbEOoiy2QJZ9mJidimgbFDIuHV6uR2RX1zXQTCmUGkQgnqp9Aw7Ey4SX3JYX_9bPntN2Zj49mhhunKUtANA7OAPwsMugFgxicJL2tXlA9r0TIAgk65uKpfFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d9e9b1e831.mp4?token=XpRAvPQPn-hRwdULzzOMZ1_Atjl7xF4Gzc92VRSW6ymGfkpuAwEFd7teG-pb2Xf7YQYeXISb8iHdMZ6g3Tu0vtcqkEfrElMpvBn70cL-tTljm1jj-khtVTQgv0DzGqAryIpUEtPcengraK0H0VNV8Ssvmwjsih5Q-WvldzyX6PxjhHF6APfugeF8PHyhl6w8mQnyh-8fKiYfu7khgpPZAbriQ07wZfsbEOoiy2QJZ9mJidimgbFDIuHV6uR2RX1zXQTCmUGkQgnqp9Aw7Ey4SX3JYX_9bPntN2Zj49mhhunKUtANA7OAPwsMugFgxicJL2tXlA9r0TIAgk65uKpfFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اگر هکر بودین و میخواستین بانکهای جمهوری اسلامی رو هک کنین، سرورتون رو کجا میذاشتین؟
علی کیافی‌فر، متخصص امنیت اطلاعات: در جنگ دوازده‌روزه، نوبیتکس، بانک پاسارگاد، بانک سپه و بانک مرکزی از داخل خود ایران هک شدند. مثلاً نوبیتکس توسط یک سرور زامبی واقع در یک مدرسه‌ی علمیه خواهران قم هک شد.
قطع اینترنت امنیت رو کمتر میکنه و نه بیشتر. سیستم‌ها نمی‌تونن آپدیت امنیتی بگیرن، سرتیفیکیت‌ها expire میشن، ابزارهای دفاعی (فایروال، آنتی‌ویروس) از کار می‌افتن و هکرها (داخلی یا خارجی) راحت‌تر کار می‌کنن، چون نظارت و لاگ‌گیری مختل میشه.
©
farhad_mottaghi
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/ircfspace/2327" target="_blank">📅 19:25 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2326">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WQYj_-nHFmR1RkWX-qTDKN8MOgUrpHrV5wW7inxgpVDFq-IOCWWFJKRZTL5TaNsieZUGlN1izZ27yQxOFPL_eSzu2zhw8K1-FT4jMrEokRtR7Iudedm-xTLUTTpNM3wM28lW1o4E7qZbT2lYTaOZoU-uZhpeZkbvegjNjLvat3jjXXzSsRc3-92UNGvD3vsMSKDKQp7tNQOiec674lJI6VwNUD8RCe2xcIHKYNEBfdAQ-PzF4hMpHZ9E2buDDM_n_wvw4Fwkb22fz8MXVNu3qUstRsV1j6Ev0HfnASTrHTgiTSnmXVZ6gGpPLc-i1waB-dsDgy17jJ2k4Yk168K05A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آگهی یک دفتر پیشخوان دولت برای فروش
#اینترنت_پرو
©
mamlekate
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/ircfspace/2326" target="_blank">📅 19:21 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2324">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/K5-jnvwiRLUpX0LM7e5nDezyydZ_YKcgKdrlTqZUvsvaBot9ZveeEUVKPA6JCHSqUX2vdeIMDAOSHI7xE2VkenViEufyLOPcTc2KIKqN3mqCTQDRaS7BMouxsw2BV1_wtA-NSMjJg46XDVHocTQ215hsqzttTIJOSBbs3sgW5e7di-AM_WjX1mJF-d0dBMy8ksWWimBi_FdLb4pwGcit8qoSxATEB_dgJXSEswW6exZozauI6QgV4DQmdI9eZJIHuMCtE5UI9JTnhUTm7n2ElhDO_YTI5PSSDAODZvoFUsYJapsRonMpnRacJ_bD6KYUTjOLVFst3G6Anv0PSDTZFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فعلا دسترسی آزاد به اینترنت در متن سخنرانی‌های رییس‌جمهور و هیات دولت برقرار شده!
🤡
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/ircfspace/2324" target="_blank">📅 10:54 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2323">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">تعداد کاربران اینترنت پرو کمتر از نیم‌میلیون نفر است!
تا امروز یک اپراتور با ارسال بیش از ۴ میلیون پیامک، برای بیش از ۴۵۰ هزار سیمکارت،
#اینترنت_پرو
فعال کرده و اپراتور دیگر با ارسال بیش از ۵۰۰ هزار پیامک، حدود ۴۰ هزار کاربر پرو فعال دارد.
©
aghplt
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/ircfspace/2323" target="_blank">📅 08:55 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2322">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GsGwzcJl5B26pO17XhdieaBdxEzQ-S35bBw8uBexolwBS7Qm8N3r56MNpmKeWyXaspc16siODNyoqf8JVGP6d-DQetnbCSI9mxhSiDvLGAkokvwtQet0V38vHZ-0ptyxa0fmm8QINkdZrvbWHFT1ack9zp2E54C93O4GT8kawGhHpru3W8ejZIqBxCXlKchEdu-4CJYDoj9-w6yyeUST4ZzxtI5LRdivGXlBDEhXkVitqAgT5-mZyVnV_bEUFlEIGn7brWDUpjbrRign3Kzu4F8zT5zVa6KqdpG04vjAaUOnpb0Szy8eo3RRUJCNNeTSsQx8YpAk36bbzRLZ3o3sDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انجمن مهندسان نفت برای دریافت
#اینترنت_پرو
واجد شرایط شد.
۷۵ روزه اینترنت رو به بهانه امنیت به روی میلیون‌ها ایرانی بستن و هرکی که کار و زندگیش به اینترنت وابسته بود به خاک سیاه نشوندن، تا
#اینترنت_طبقاتی
رو اجرا کنن. مدیونین اگر فکر کنین کیسه دوختن!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/ircfspace/2322" target="_blank">📅 08:47 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2321">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">بدتر از قطعی اینترنت فکر اینه که سالها درس خوندی، دکتر و مهندس و محقق و پژوهشگر شدی، بعد واسه کار علمی دسترسی به اینترنت بین‌الملل نداری؛ اونوقت حمید رسایی با حول و حوش دو کلاس سواد برات تصمیم میگیره تو اینترنت نداشته باشی، تازه خودشم تو ایکس وله!!!
©
NiHa_Mehr
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/ircfspace/2321" target="_blank">📅 08:38 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2320">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SNN0f0eAGGTNw7-yQ6bC0-lELYoUlp1hFBLqOf5_dL_siRJDyHqhMIBEkR-7PmLby7MzLKiGIIEGC_0kQYoO1jrQPxKCNRTwS3J1BvVfuZahWwyYw_rrnhgJXikOXMdGR_vQoxvPfkh3Cc8NUyULceuyUAcFgE-0xe9N1h1rMROHW3IV6_RixzOre42oFkhiaTLnvETvwC4lpLHXBHZvbdWgoQirioSwfhMqtKJyBCAYgXs60pWgFn6yE32qlBbFFibSvPQAC8c7Rw7-SJVd4BiI_b0Lk7Dow6hjS5ogUD97UZl43KXh08nXF08la4nqvNSC4jvm-ZTN-zt3lx37Xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پس قوای سه‌گانه کشور در واقع ۴تان، که یکیشون به نام
#قوه_عاقله
نه توان قانون‌گذاری داره، نه زور اجرای قوانین رو، و نه در جایگاه قضاوته. مهم اینه که قوه عاقله قصه ما با
#اینترنت_طبقاتی
مخالفه و قراره نقش اپوزیسیون داخلی رو در این مضحکه بازی کنه!
©
nimaclick
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/ircfspace/2320" target="_blank">📅 18:06 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2319">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WRuv4z5yD670NiRwHRLfkZvjjQj4QLj7qfuBMt_rj0AGHXvuztASFWU9tshxtMSOvvFXHxAsM276e-C063VNxi-7bWRvpszq4kzhf-7EAErDN74MUq9uXs7F5OSnj6bYKcUG6Xyv0vuLHP3bWwOiQ1aVGnEuA0OHilpG4oFdLeeFkx0WuFTjppwmDDcxtBVg8nZrpZ2K8ls-owi-i496dEhjXj0qDjkBzzZJJRY9-qI60ZoyUAs7q7FmF2rhowFpoDniyO8EY3EnBbmuqz_8qmWPPNRMSsgRSDhrD8wTQiBHvJc_xqSemusLXecZX_rWxsQxO9MyoXBxMyFCkdUIkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پای
#اینترنت_پرو
به اتحادیه صنف اغذیه‌فروشان و مواد غذایی باز شد و حالا با ارائه پروانه کسب و کارت ملی میتونن از
#اینترنت_طبقاتی
استفاده کنن!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/ircfspace/2319" target="_blank">📅 17:04 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2318">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pdrcfLbRhxZH-98QMP2_HGT9ctvPE-W7tQijhYrRoONGzatwbyH_jlAe9tx6-Kfg8t37zgoKpyGF1017Sy7wt3-tSnyju06TmxXD0d7WR2SBYgpVdhKSrC-yNaRwPxD_Be7RAt0A2383wTig7KlWmM-laYjyWAZcnW5wFq1DpJslMfSFnjo0snxPS4LtCQbluEHH2-NSSHuhqiR05GktvFWjMRueTu1Hv6Ote0etE2qgWWc1jJxZ_AWS87JzvvJvqIGKA4tEelZcm0kmOLgyzotrjNRFwyTxcMf_RkbDrSX2cA4repRrFIuVKg0Y3-4sMKWEFVEb-0msT8VrKdiIbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ متن‌باز و رایگان TunnelX برای زمانی ساخته شده که کاربر نمیخواد تمام ترافیک در سیستم‌عامل ویندوز از VPN عبور کنه. با این برنامه میشه فقط برنامه‌هایی مثل مرورگر، تلگرام، ابزارهای توسعه یا برنامه‌های مشخص دیگه رو وارد تانل کرد و بقیه ترافیک سیستم رو روی اینترنت عادی نگه داشت.
👉
github.com/MaxiFan/TunnelX/releases/latest
💡
t.me/PersianGithubMirror/4816
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/ircfspace/2318" target="_blank">📅 16:35 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2316">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/oUMBCP0EmeyU0Trjd52vMbBwrwTQnWgpUEs5Q_H4Nn8bc_eQmf2ZmALgK4PUlnnMeGLslIeqf2nlESJ6K0sQhShfPHW1PBo7onxn79dt_v_vINI2OqbJrCcBkkyjV-MZ_PdfXA5Nf7TrM4Abtqyo_bofwCRmDCj125taHpVU4JslTHQ5RX7SuiaBj6xIcrxkI-rpRvbdBQ8SzAQMuhtMi0XtLrR2xLP1nVjbVCJlq6YkfDV4Gg_SqNua-KzxCqeVgOG2AfRRnKrAqJO9J2MTIWV8AUZ10tYYL7EjTdvqKGFVvGu9dbau1pGSDYuDpvSganw3tnNHCajQrrQPwXo17Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر اینترنت غزه، اوکراین یا هرجایی که حمایت از آن برای حامی‌نماهای حقوق بشر "ویترین اخلاقی" داشته باشد فقط ۷ روز قطع میشد، دنیا را روی سرشان خراب می‌کردند؛ اما اینترنت ایران ۷۴ روز است عملاً قطع شده و آب از آب تکان نخورده است.
فکر می‌کنید اتفاق خاصی افتاده؟ خیر.
ضریب دسترسی واقعی به اینترنت آزاد در ایران به گواه نت‌بلاکس به حدود ۲ درصد رسیده؛ میلیون‌ها انسان نه ۷ روز، بلکه ۷۴ روز عملاً در یک زندان دیجیتال گروگان گرفته شده‌اند و همزمان که جمهوری اسلامی در پشت پرده به سرکوب، بازداشت و اعدام مشغول است، آشغالی به نام "اینترنت پرو" را به‌عنوان راه‌حل به مردم می‌فروشد، که عقیم‌سازی عمدی دسترسی آزاد به اطلاعات و نقض آشکار حقوق انسانی و حریم خصوصی شهروندان است.
ظاهراً برای جهان مدعی آزادی، فقط آن دسته از رنج‌هایی دیده می‌شوند که موضع‌گیری برایش هزینه‌ای نداشته باشد، یا چشم‌های مردمانش رنگی باشد.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/ircfspace/2316" target="_blank">📅 10:26 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2315">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TZzxFiU0R7YAFAwT8WXL6gKUnFF3sy3udHdcXYSLP8ItzW3Ku4o8r2jtCWv2mIWm3fGK7Wc2_4b6CMfyj1bQcnX0LIhQi_Bybdtegg0nk-VHi9OZgFWUTGrK-v5yBwxei1m0xeX73nBGQ-J_Qagqo--kk2tXO9hiVa31ltHbuT7Vky-ap5Aug8HDXLnJQVL173LUVUkTr9bcIM0S_uuGdhRlbmasFhPNuoDirnxYrRjcrMQA5nMzx6DuGmXbCCUuKX62G2U-z9E3AqWaG6GyA07G4tSmWWqXYVboGTSAGZukjprtQt3Zs_FyXJwn_IPysPWPf6ftWkeGoyPhwhMxTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در روز ۷۴م از قطع سراسری اینترنت هستیم.
وزیر قطع‌ارتباطات گفته "در تلاش برای برقراری اینترنت بین‌الملل در اسرع وقت هستیم".
نتیجه عملکرد و تلاش ۷۴ روز اخیر این فرد از خروجی عملکرد یه مترسک داخل مزرعه هم کمتر بوده و جالبه با اینکه از بی‌خاصیتی خودش آگاهه، حتی بصورت نمادین دست به استعفا نزده!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/ircfspace/2315" target="_blank">📅 08:55 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2314">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Uu3Q1OJMEPtXjehSkNY9jUx3SyXDLUlumPypQBZvq9HYDYTwuYdLwdtDdqUYzNXGuD3ul_EYYZmgtP3_9UunoJv9xvrYil2OtWaiJHEJf5ho95a_nOGUX2WUgqEV1eBDQS3iuqF0MXX0tNJd-KWTrHKRLFsiBVen9qDvPKNdHgj9681NhNREfrV5Itu_wbcpRXn6etc4TmMN1xg0RO5fYcetS7pBY12cAYwdi8Hamu4EWDc3sWYZXZqfxQiWzoh6x7Nz6JB5QNA7jzcW9lEdJzqyYjWpm6m3ObEnCc6FQceX75wiN7xJbnUBwOHpk6tCchVdBwnSc6BLZVpYFAfIEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در ادامه روندی که نشان می‌دهد تصمیم‌گیری درباره اینترنت و سطح دسترسی کاربران عملاً از دولت خارج شده، وزیر بهداشت برای رفع محدودیت دسترسی به پایگاه علمی «پاب‌مد» مستقیماً به رئیس مرکز ملی فضای مجازی نامه نوشت؛ اقدامی که بار دیگر نقش کمرنگ وزارت ارتباطات در سیاست‌گذاری اینترنت را پررنگ کرده است. /شرق
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/ircfspace/2314" target="_blank">📅 08:46 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2312">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WpukYRms1kHmRr8tDTkFvTnEuqd7aX91R-a6YBIopePBiJLquwNvRex1aD_oUjqYTfBwE1gT0QhWelovQ15qKe1jWl52xOLJAG63oN5oJEol8Wp54MaJjjyE5jpz0X1bSx44zzQp4dJ30PGCHphGTaBulFL145k3LTk3NkBwEcbjWbt4NCMMwI7KEq8xPkTuAdxO1No6bzKEPxXWUSqZHn8NJWuEH-RLgzE6N_RBl9wv3BhUs6LfPXgCsJFSKKb7RsoDK9cklKscDbO2Rn6uwAxjBbU_eEdtYdWiReM6z2-iu6Ki_w-3JKYR_36Xm_YXB0ZWjw6eSVvVt1t4s9NpIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکریپت AIO Downloader یه ابزار متن‌باز و کاربردی برای دانلود فایل و محتوا از سرویس‌هایی مثل یوتیوب، گیت‌هاب، اینستاگرام، ایکس، تلگرام، گوگل‌پلی، تیک‌تاک، پینترست، ساندکلود و ... هست، که فرایند دانلود رو از طریق GitHub Actions انجام میده.
این ابزار طوری طراحی شده که در شرایط محدودیت شدید اینترنت و وایت‌لیست فعلی بتونه بسیاری از فایل‌ها و لینک‌ها رو دریافت کنه، بدون اینکه نیاز باشه سیستم یا سرور شخصی برای دانلود داشته باشین.
با توجه به اینکه این پروژه به GitHub Actions متکیه، بهتره برای استفاده ازش از اکانت اصلی گیت‌هاب استفاده نکنین و ترجیحاً یک اکانت جداگانه بسازین.
👉
github.com/ProAlit/aio-downloader
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/ircfspace/2312" target="_blank">📅 08:37 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2311">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AJMhlv3dTmsRw01bEmSYILPxTE8YIpCpI7e08MpzkKHMHRQp1ATGy75rMAqoLR97eyazrwcU7EgtYwcJ8Yk2Dr_JDAOKlqMBHYipW3NoORkn9ncxZu4jbn5wfrydjm3arV459jyx-pkIyDCV_RBZzH8v2ZlY8fj829DNC2sg33c0ohxfVoKziSYzQocygXdq54hKqz-0LPpbVPWytMxQBBKXZGh5ybP_7AyYwOIoe8_zwZcWc0ivxq3ycR92uRvTDP5aUovl5gJRkaZVIqo9cp9h14rnWMDNB3qTduGUHt6M8k1_bwlJDtx1vrL0zrb49WdcvmpQqrjzyf8F7g_PhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#پیامرسان_بومی
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/ircfspace/2311" target="_blank">📅 21:33 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2310">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vDpZS8Qrfc8uhE-9x0v5skXPrDlffJwtuywle013dsSai2UXBf3f0N_VqnVhxdnDZFNZYt2nP5vtZt30cn8RECPV7jYJ1wk3fVxAY6ej1UCQ-uvqFByhXKnwbVsWleq0MXbg69r-GXiJBjZCn2KiegHFLzPIiTgM9iTFMmA9KRt1d1F3BPFIWWfB18o0jHv0nW7J3kV7Gxqg68i_w2RP3MfktchFg2Pu1kxxopul8HzNPU_DsenrH6SuacvXN14CQ24E2LmBAaljRFYxHbExY8zAmtK50DJqWNTwxsUGG42sY4UJFT8KYLHdwQ0BWcRj_1KeAAy8QqFHKa_Y6QUmQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیگه رودربایستی رو کنار گذاشتن و بدون ثبت‌نام و بدون احرازهویت، بابت پیوستن به پویش جان‌فدا ازت تقدیر میکنن
😁
کی به کیه؛ اگر آمارش به ۳۰۰ میلیون برسه هم تعجب نمی‌کنم.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/ircfspace/2310" target="_blank">📅 21:28 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2309">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">تا الان توی هیچ پستی نگفتم که به پروژه‌هام دونیت کنین، چون حس خوبی به مطرح کردنش نداشتم؛ ولی شرایط همینطور پیش بره احتمالا سر چهارراه نشسته باشم
😂
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/ircfspace/2309" target="_blank">📅 21:25 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2308">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">قبل از شروع جنگ و قطعی اینترنت درخواست فیبر نوری دادم و حالا اومدن نصب و فعالش کردن.
با تشکر از شاتل بابت سرویس خوبشون؛ در واقع قبل از نصب اینترنت نداشتم، ولی الان با سرعت خیلی بیشتری اینترنت ندارم.
©
itsmralii
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/ircfspace/2308" target="_blank">📅 11:45 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2307">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/a5ShH2apQ651gbIKRt5bnIy00SORBMB-v5lmXETqFmoaTCIvLqphADMmL_zcDaHqQ4ySyAdSIJcXi4bJTOcilkXANTIA0fjXp1Q6sqWcRLXcp2IVb9iHQW3TjJBMgA-0LT7CtuIRePI7Av2HKs7qPmf8qgkqn2uyolGT1H_DYGdzF-Az-iLn_NPcTxiDiReVOOwUJoJDCZYBHha1bOa0rO1u47ieqlTKUALeK0igQlPSwqSI5ffXrlOPI8n18UKKNTqwYzI2VObO8dHdjqEuEcnFtzxnniDdG-1pqm9Aa7jAiInb-qAtAQ7ZMsydhY17_kp-KRFX2g4_039ba8KJLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون رئیس‌جمهور از وزیر ارتباطات بابت هیچ و پوچ قدردانی میکنه، بعدش همون وزیر از رئیس‌جمهور قدردانی میکنه، بعدترش همین بدردنخورها دسته‌جمعی از مردم قدردانی میکنن؛ اما تهش می‌بینی ۷۳ روزه که اینترنت قطع هست!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/ircfspace/2307" target="_blank">📅 08:13 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2306">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YJRxDerdI2m3o3waP7G2QT6o5tNHv5QR4aiJsWwUG3qXpJ04NutGGaVRXEQrEGCjMMeHkBLA7b90a499xCRWfAFZtB9Cp6louj6jhWwfvzqXtdAI9exVN149QpPvcSfAA0iG1bzXHEQufbUbnfitx3Bk2IiLqZZaq1JPZlXRWJ9MEhJVZ6qubQdp3ALeGBmUtfRc75Yp21sKtDseOFlvnnHZK5R5doSKMkxEKnY7NpA_oLJRwdygAflNsPrPgBZQtu6WKD8_JdAf_50k_08MqZhp8B2hNdDGYQzFaZJeQjWgNQB36il36Re6NjfMpPrJx4CzSRsRHYrv3TbgNPG_DQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ WhiteDNS یک کلاینت متن‌باز و رایگان برای اندرویده، که امکان اتصال از طریق DNS Tunnel رو با دو حالت Proxy و VPN فراهم می‌کنه. این برنامه با تکیه بر MasterDNS و StormDNS طراحی شده و میتونه بدون نیاز به تنظیمات پیچیده، ارتباط رو از طریق تانل DNS برقرار کنه.
👉
github.com/iampedii/WhiteDNS/releases/latest
💡
t.me/PersianGithubMirror/4637
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/ircfspace/2306" target="_blank">📅 16:30 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2304">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UnvzWXbYRaCg58dEdNzXksnzdfzrTASyRH2oUVk46n511cGuwgdG2TbSF4489dKzfpJH-3TzXh8NMRsmdiReyKWnpZ2DKX8HotosRQZZ5_KOdnlgOjPWj-YxSJJeTJaI3EH8LWRd135W_pMN0gK3V-QmE9ArI5HbzgGF18--zWV11Ze56-N5N6B8bt6jQ1yRRE7Swo8yi-mzn_qcy9eqvII59nVWiMDLZrA0fbcKPKa_XjFOqMQzrfP7LQl3vA7vdRO5kiIyB91JN6CtHjOBLOVbl-Z4zXNJ6gBxbf3bP01BQk6PuZJuKDm1cj6cs9zBOwxdS-QSn5X57ImW1jD3-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز که نت‌بلاکس عدد روزهای قطع سراسری اینترنت در ایران رو اعلام می‌کنه، یه عده میگن "خب شمردن که کاری نداره، خودمونم بلدیم".
ولی مسئله فقط شمردن نیست؛ مسئله اینه که نباید این قضیه عادی‌سازی و فراموش بشه. اگر فکر می‌کنیم راه مؤثرتری برای اثرگذاری وجود داره، خوبه؛ ولی سوال اینجاست که چرا تماشا می‌کنیم؟
۷۲ روز گذشته و هیچ اقدام جدی‌ای برای کمک جهت اتصال آزاد به اینترنت انجام نشده، کسب‌وکارها نابود شدن، آدم‌ها شغلشون رو از دست دادن و سفره خیلی از خانواده‌ها کوچیک‌تر شده. مردم برای یک اتصال معمولی باید میلیون‌ها تومان از جیب خودشون هزینه کنن و در عین حال بخش بزرگی از نهادها و جوامع حقوق بشری نسبت به تداوم قطع اینترنت، سرکوب، دستگیری‌ها و اعدام‌ها سکوت رو ترجیح میدن.
در فضایی که همه‌چیز خیلی سریع به حاشیه میره، استمرار در اطلاع‌رسانی خودش یک کار مهمه و همین گزارش‌های روزانه امثال نت‌بلاکس حداقل باعث میشه موضوع قطع اینترنت در ایران کامل از توجه‌ها خارج نشه!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/ircfspace/2304" target="_blank">📅 12:30 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2303">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">این هفت کابل اینترنت جهانی در خلیج فارس رو اگه قطع کنید خیلی خوبه، اونا هم مثل ما اینترنت نداشته باشن، بلکه دکان‌های حقوق حشری صداشون برای اونا دربیاد و یه نگاهی هم اینور بندازن و دل ما هم خنک بشه!
قطع کنید.
©
ehsan_369
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/ircfspace/2303" target="_blank">📅 12:21 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2302">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cNOKRNL34xmkAUmZHgeZCWvL-xCoz0ZctNySj6bFQSEglLZI7ZcBY2J6vq6eKRxJwa78AXnxZK4JMJ0UrMXsSCidsQwgTu8NFL0MY1_yzfNUfHuZ4-5DdkzHC6oZtP_fvP_AAI3biiIPlvbH7iD7iUp-ssI0M2XcfAOlhlBtsaKBG8OAg5Q_3DZAuVyqdIu_HaS199k-TJPwiCk5wIfCCFDJeNtyE-AHPJ2y2u8ziJZMSt-_NH9LGo8bt90-GytvQZFGZH--lC7r0WRG5X1_C-tFfVU7A7vSpPP639NV70rViN066NfhPhXWaOMA6J5xpuehk7b53xv52uUxfC5XIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تسنیم نوشته تنگه هرمز فقط مسیر نفت و کشتی نیست؛ بخش بزرگی از اینترنت و تبادلات مالی دنیا هم از کابل‌های زیردریا رد میشه، که از اونجا عبور می‌کنن. پیشنهاد داده ایران از این مسیر پول و کنترل بیشتری بگیره؛ یعنی برای عبور کابل‌ها مجوز و هزینه تعیین بشه، شرکت‌های بزرگی مثل متا و مایکروسافت مجبور بشن تحت قوانین ایران کار کنن و تعمیر کابل‌ها هم فقط دست شرکت‌های داخلی باشه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/ircfspace/2302" target="_blank">📅 12:17 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2301">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/s9J2CKgTUkPZiOQEKp11aZIoDPaFZ5-M2E6ewTgfaH_ZkrBxrNLsc7tvIlmrw1CveSIszdv2UzTwm7nQSN5CIAsVHJ2uit4K4roX-hHwjl2BG80OtqI-2Yh4m5Gr-GH3oxhhAuLq651-64osYWUkmoM_CgKBMdOGAag04aNq3aZGK6MhC5tlv_l3J1HX2d5uHWU9__enR7gnglkBliaJfYsLybLiS-KKlCIm8gdijUKPvfqmy-CfWt4K55-K8d68LLUw1apLV7vfay4RrwXTsRGRkvOn21xX4liZ0JfFHso3ghadEwGENQLbC7-EQwJdhHLicXb2FzbeUPIuzuvwFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نت‌بلاکس: قطع سراسری اینترنت در ایران وارد هفتادودومین روز خود شده و هیچ نشانه‌ای از بازگشت گسترده اینترنت دیده نمی‌شود.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/ircfspace/2301" target="_blank">📅 12:07 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2300">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/guzU5U-K7cgSWr9NdV4bLZH8NzZl1W84dSXjFdIBrVtB3fXh2rZJByc-80xtL1Z9oBMiBfK_boBewboK6LHBqT1bbQJYY7a_4KQ7MmWziNd8eMipslsGg2ZJkrRKcN_DvsVR8VeUXg7yU5jRkWKHWFPDSI8piLrUh3e84P9ODd61kCbSNn9w15SlzOBs65ade9hZhThSgtCw9BZcHSXmLYu0dqNv8IdIqgZzI9odCflNx6nP1QMUHA9Eks0GC7X_W9F4Df2JR6YbNj7GZJQtB9tJDjk-xwOns82yLVvHqRYwS3YmfSGo9V9ABDcio6bAByln-N_85yws3aji1UhJ6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه ۳ از اپ متن‌باز و رایگان TeleMirror برای "دریافت آخرین مطالب کانال‌های تلگرام در شرایط محدودیت شدید اینترنت" برای ویندوز، لینوکس و مک منتشر شد.
در این نسخه نمایش پست‌ها بهینه‌تر شده و مشکلات مربوط به کش تا حد زیادی برطرف شده، بخش تنظیمات به برنامه اضافه شده و امکان بازگشت به تنظیمات پیشفرض فراهم اومده. لیست کانال‌های پیشفرض افزایش پیدا کرده و علاوه بر نسخه Lite، یک حالت Normal اضافه شده که تلاش می‌کنه در صورت امکان تصاویر فیلترشده رو هم نمایش بده.
این برنامه فیلترشکن نیست و بر پایه دسترسی‌های فعلی وایت‌لیست اینترنت عمل می‌کنه، بنابراین ممکنه روی برخی از اینترنت‌ها قابل استفاده نباشه.
👉
github.com/ircfspace/teleMirror/releases/latest
💡
t.me/PersianGithubMirror/4599
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/ircfspace/2300" target="_blank">📅 18:57 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2299">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">افغانستان تست خدمات اینترنت 5G رو در کابل استارت زده، عراق تلگرام رو رفع فیلتر کرده؛ اما جمهوری اسلامی تا دقیقه ۹۰ درحال آزار و اذیت میلیون‌ها ایرانیه!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/ircfspace/2299" target="_blank">📅 17:52 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2298">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mpkEySTWfN3cMO0iJN8lqKGh_P-zyigTi12-H0-JEzoT73bFLCtcdMF-mQI3995nTJrWdE9SmOHwUnqhqY6TvzhqCiKj3VYZR7jEXNL_1XJzxlYiO__doaKspCzFNAnMGoC9RfnsJjH_mva1F7_fBEA3FzIp-B6hfE-kMwhW2qHZVnI9sHyui-rounzOj8k7Txc-2dXowEh3Xb7IW9ZClTPDRXJHmJumYI7FN6bmtOcCDvFuoZYYPolGB14kH0eqi17T5QEWBwFBSjTTdluQSckWEIyi_sIvAmwaqik0E0C4QAYsbRjfTb2lNR7L4iSNXWILvUZNE7ni-S9Gq8p_yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یعنی خاک بر سرتون (پیامرسان‌های بومی) که با اینهمه حمایت و در میدانی بدون رقیبِ جدی هم عرضه ندارین کیفیت خدمات دهی، پشتیبانی و توان زیرساختیتون رو ارتقا بدین و بعداز اینهمه سال سابقه، آدم نمیتونه ۸ مگ فیلم ارسال کنه.
بعد از خودروسازی، باید شماها رو هم دومین فرزند لوس و بی‌خاصیت کسب و کارهای داخلی دونست!
©
kamran_falahati
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/ircfspace/2298" target="_blank">📅 17:48 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2297">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">جمهوری اسلامی ۷۱ روز هست که اینترنت رو به روی مردم خودش بسته!
روح‌الله مومن‌نسب (تئوریسین بارداری با ۲ گیگ اینترنت) گفته شرایط اینترنت به هیچ وجه نباید به روال گذشته برگرده.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/ircfspace/2297" target="_blank">📅 17:45 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2296">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TYw5qqe-uRyJqXeOZymBkjRbS1p6YLNOxeBKagOekx6enH_93MZR0lugVSl_rZWe1zsivwfWnPrksy0LsgjV9cBevk60JcrT36HYdg86uJdbGblG5hrQD4OtBe6T04VM-65NyqB0uBF1RqtvSL2KPXzQpYKM7PbGMWg9swU5BMJUd4FHqA3BT7I1bO7WxIvbKx-IRApmMNmdL5lrXeIcXSegqZhaHM9Xx3cm7GjC_FvR2SEFJogmzYBRV_Kr4FEfQJyefTt6ISjdk8RhWkZVa0FLTwiyV27TPti0tHTrgAJjG82eP8l8g49JNjcBX8WOHamvnwmO9SjRHyxrJGGnHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ متن‌باز و رایگان Pigeon یه فورک از پروژه تله‌میرور برای macOS هست، که از طریق اون میشه بدون نیاز به فیلترشکن یا لاگین در حساب، به محتوای کانال‌های عمومی تلگرام دسترسی پیدا کرد.
👉
github.com/MaroMushii/Pigeon/releases/latest
💡
t.me/PersianGithubMirror/4500
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/ircfspace/2296" target="_blank">📅 17:45 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2295">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VjsG7Gncc4BRUtcl7xkCZOXuanFaMmqmBYcANgUlsFsUrBkFd9kMGsj3TThYSVo5n7gcvG86jNWNml8UPYzlXlpvUoobztHurYQnRyZ2bHNF-5W0czlQhZvB6bZMPjOyYivWbUglNlxevRgP6al80FV9Qwi4_ptGgsQhsHIxZ32NGNqgmjQBWUe8oxIi8ShblDhJBe9wBXC7t4GP8JgXtRfNfgLrm9CapMMrW_A2trAw6dk619KMuZOS4QVQiQ_BeIqaJfA5dwEEVRcVSIBRHC8Y-E9uJKAyU-kFXcZ1xMM71ywOuNY4Xsdq6joqvHfuvJhHRI8IIC04cyAw6Q6OeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پروژه Youtube Sandbox با استفاده از GitHub Actions بهمون اجازه میده که فقط با ارسال لینک یوتیوب توی کامیت‌مسیج، فایل ویدیوی موردنظرمون رو توی فولدر Downloads (داخل مخزن) ذخیره کنیم.
👉
github.com/iphoenixon/youtube-sandbox
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/ircfspace/2295" target="_blank">📅 17:36 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2294">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IrHRUdVKRch4NmM_FE2MV8LH_E4NnlSCT_MeuVYJWPQI7b13EOjcX1Bl8d0I-WMDLSLvEGJt-06n4OVMtcQZyIYzhARRV1cmjCfvBUsH7C0ABlx4S2MSSPuphV4iyoJ_Yiru4QPFRPV9FOXmg59ozAF6u96w3rcexAjrGsU_D2U8Z1XzpRpPNZpk2C5-TQKOzE3v1rz0VBjr-MhEz-2KIKyTdbDx1gB198B_ziwoPoW4ddZg4vGGBownXn_Sc4EJp-If6HAHD23oVfqxUjbIKL27kk_RjMLkDhdio13E-x0uKxmeclf3g2qIM2ow1Sxn9gE6cFMcpEmMtKcMECBR5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه گوگل براتون باز میشه و در وایت‌لیست اینترنتتون قرار داره، می‌تونین خیلی راحت با نصب این کلاینت اپن‌سورس به گوگل درایو در اندروید دسترسی داشته باشین.
👉
github.com/aleskxyz/Round-Sync/releases/latest
💡
t.me/PersianGithubMirror/4489
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/ircfspace/2294" target="_blank">📅 17:26 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2293">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gTJJg_rXnvHIZSB_0DK8QaCQTl-Ku2KpelKGhg1ZgNaR_vXoAPXytysRmZcvn5bGwLZtm1UrdxexyF62BjvHoj425BKTIsr7284SMmW3pmdR7rs3INdpxjN9WAqyy6rq8R38K0MGpNJRI7lPMM6xK2gaQGvYzAeQkwnCrKbCWfv6tUsJS0bI7j2McjQPbweqY-CNXsuzegALbc7pTGcDQY1Sc3PWUiVU0f4K1CpLtVPRn0wcwWz6ccApkC-Xh73-FNCiIlovO8J8vpPhaajy1CYQzr-AaErbmIQImXNfClylwqlQcqzN69QO1Wq2QBh1uXC1VfNkegi-Oyf5qVOMmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آپدیت جدید کلاینت ZedSecure از طریق گوگل‌پلی در دسترس قرار گرفت.
در بروزرسانی جدید این‌برنامه پشتیبانی از پروتکل DNSTT اضافه شده، هسته ایکس‌ری رو بروزرسانی کردن، بخش تنظیمات تکمیل‌تر شده و یک‌سری از مشکلات برطرف شدن.
👉
play.google.com/store/apps/details?id=com.zedsecure.vpn
💡
t.me/PersianGithubMirror/4496
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/ircfspace/2293" target="_blank">📅 17:15 · 18 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
