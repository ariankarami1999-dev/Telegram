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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-08 14:09:23</div>
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
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/ircfspace/2399" target="_blank">📅 10:53 · 08 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/ircfspace/2398" target="_blank">📅 10:51 · 08 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/ircfspace/2397" target="_blank">📅 19:45 · 07 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/ircfspace/2396" target="_blank">📅 19:39 · 07 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/ircfspace/2395" target="_blank">📅 08:50 · 07 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/ircfspace/2394" target="_blank">📅 08:31 · 07 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/ircfspace/2393" target="_blank">📅 08:28 · 07 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/ircfspace/2392" target="_blank">📅 08:25 · 07 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/ircfspace/2390" target="_blank">📅 21:56 · 05 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 37K · <a href="https://t.me/ircfspace/2389" target="_blank">📅 21:31 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2388">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/un97CVqgAe65jrECNbaz-S2qUo_uoU5yphMZ4AKFMnpVHXvaYEbTJ5i-0EhRVX8wm_wnxrGP1VltAQvHFqbpLmtOYFPu8XidXKD7HGoCFnzkXmm_ip7cxu6g28qDltx_xeZ6MXJCHcEpWYEfHAPxlYQMFozhn1fSqtlQWLiBerxEhDD4YsXVjue_-VUq79TgsARpvmqoOELHn0IHoTkzvsy3Vydkrq-9ARfOCMxl2InS9yHaNhCSdXszDIcUQjxkQVLI84AFxgvBCGlFTqZBaYlcLm1WuRpwBet7aOypWVBv0SIh7HEPHIU5_KONBeCR7EIcN66wU8YVSvae2MPk9w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/ircfspace/2388" target="_blank">📅 17:30 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2387">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Hu6z-DJIactCCFf3lNuTRH_gGDneMFot4oZo4uyq4PTJvcTkT9TMvW6b3mWw3PUuGs6VaVaXdViWorP6-x6nZ_fDMLVZK6POs0ajtDAeLQD89GGw73gdwdp5LERLx5hPPw-fIGK5wNdJJVjk3xRQ5VkSvuZkvMrPFxz96aIIGHXJnUFh_IIDSALiB1-oOzKA7KwkM0rW3Azl5YcUJJC818MLw9ixlUPC3_Tm0rtRSRdPowaQIaAJZOPTvrBZmXVQNYJ1vFfHAHrvzBzNRBVIIIPccxYFFh3Vrs8O6-3oX3PUH3oK3v-yDWXEy3rM0Zgqyg5vYq5n7S1wN3xXWLcgSg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/ircfspace/2387" target="_blank">📅 17:24 · 05 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/ircfspace/2386" target="_blank">📅 17:19 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2385">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ME57UYjAWx7XJnMX4DAsQVg9PLR1XMpnNepfNspTF2J6USxHC7NbhjQwrlEIVm7e2HrKOx1a5fCBLHvpL_9rXhfqiB3BwMGf5F6bMPoY2kRoVx1l-8j6DTQZhScH8tvCoAYM5SSxJW6xWRKREfvDkreB6tbTQmT1XcKiFJniux1J6d7mQ_p3UAHs-dVMzpv38H0J9u6H50km_7h6yPiwd02-SFCO07m0Tb4PiXGARjanUAmxvss4wX3_m8pCLn8O8KzuqEu3j_Ikx_I5DWhUIf-LSO9lKIjy6VW5O7t4VhzKmaSwKAhA1OxpunYHaYqeH6uQTiYvcCW_0pGwx_zTXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۴ فردی که در دیوان عدالت اداری نسبت به اتصال اینترنت بین‌الملل دست به شکایت زده‌اند، کامیار ثقفی، رضا تقی‌پور، رسول جلیلی و محمدحسن انتظاری بوده‌اند. /انتخاب
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/ircfspace/2385" target="_blank">📅 17:12 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2384">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mNT8-fPOjkdPsKO0mjf1a0Rbn7mdC4U7oFhWD-VXP0uK70bYV5e4bAARx4owgWJv8k_1ZMwdVKwD9lpKq5dfXJwjPZ3xPiiZVberH_JaGRmG0T0umhuwjLsnZ_-Q2m_TgV1LuMCqh532jeiCKZ65ZuMjj7FYunOF4a9MFI51zVsX4jDBxIQBifIjiYp-nKC0xRPoskXfzcURAp-QlRXmj8Dq1Ih-e2k8udFsg37uoLWOIDBLdjwIoJ_aBSDJ4ehgpZmHTd3sbwxhHXD7EY5bYVRZEhcRnA0QMbcG2CXQtqeZXj8Qq2kTATNROgs-msYLfJif63fbsz744ICltEd4ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نت‌بلاکس: داده‌های زنده نشان می‌دهند که در روز هشتاد و هشتم از قطع سراسری اینترنت در ایران، اتصال تا حدی درحال بازگشت است. البته هنوز مشخص نیست که این بازگشت اتصال پایدار خواهد ماند، یا خیر.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/ircfspace/2384" target="_blank">📅 17:09 · 05 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/ircfspace/2383" target="_blank">📅 14:43 · 05 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/ircfspace/2382" target="_blank">📅 23:19 · 04 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/ircfspace/2381" target="_blank">📅 11:23 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2380">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PHCyG2iBSWYegYO5D2IAZUAHotTuIcM-_AHXNmAsD4BLMsyk9Plg-TNcFRhdQsnvdZ0EDEyLCQzd_qOnVaiy5Y5SPWSai5hH-Jwd-XFmkyTHkUGrHRUlBQ_SnFn03GI2Hf5ImnMxrKobCH1gwPh2TXyHPua3zwKdUUqoouq3lZ3tDSl1OxrlAjly3PFnO_s2ATOP-_uSCEfGS35q8O8fSQY5mMd-SsUlX_rwLhY876maFsi6pjehzsvc57oYRRVTkQBLEzmDDRD81HCIuc7oPLVdOeymIcde4SRBI29wWG3MX1tMEh5NfSyDwJzn3LVk3PKl03m9EeemYC-G_EDXYg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/ircfspace/2380" target="_blank">📅 17:16 · 03 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 40K · <a href="https://t.me/ircfspace/2378" target="_blank">📅 08:57 · 03 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/ircfspace/2377" target="_blank">📅 08:51 · 03 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/ircfspace/2376" target="_blank">📅 08:40 · 03 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/ircfspace/2373" target="_blank">📅 08:15 · 02 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/ircfspace/2372" target="_blank">📅 19:51 · 01 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/ircfspace/2371" target="_blank">📅 19:45 · 01 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/ircfspace/2369" target="_blank">📅 20:12 · 31 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/ircfspace/2368" target="_blank">📅 20:09 · 31 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/ircfspace/2367" target="_blank">📅 20:04 · 31 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 32K · <a href="https://t.me/ircfspace/2360" target="_blank">📅 08:56 · 30 Ordibehesht 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fNV5WUGIIN6kMzoxcRdSIE8JTKVI-3MZtNRYomPJZeszCiEnSEllFUzCtb9YHrU7DLEQMdAZEzT0RgD9CLo5uigwoPvHT06l69lSeHcKQ1AvBkTrVx45whKSDehnNgxawpZzNAs-bf2NLo7qCornUE86IeGXbTfFz0ncYtjKanzO-ZPf0lS4T3Z1aIZ-bfDNHajCMTnN01lNceGbzWGZdmiGu7YLRgHjNK_kX-vkRISqAwIl3Eduej0imLmGHCaDmMySDHjG_ozD0GjCBKIo2PN6qtDnRm0JWGZQFBGT7n2VAgl5ZYRpP4N0jU9lADvt2bP6piZkaswEE0z2cHpiVA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/h4bDLLEE0hb83RJhpkE6tJCaE3KvAFZYWarFS8AMcl0FD_vPLBVe5hT29f-b82_0V6NFK9lRuTusnu0T9sMmqTQVk7Ft6e6r2tOkg-kexKX37pRAO06bAuCTi-jRsCKb0yZYCpC3UVq_pxCvTjeD4AjKEwqsNQYpAlWyUoW4iKcH2VSdLimXbc6zY_3W0ITRMB92E6MkAEXh8aogplhgq01aTWt3tuN6vdGKWc0nnToXZxRLLXt9OKmh0Bxlai45td8S5LS7eRjIoXm8396N6Tdr8-mjpMQZWJR2DurCbIz22sO8r1IUMeuCSvzUpvhVRv9aYx-GWs8izuROW1LE8Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/ircfspace/2353" target="_blank">📅 16:24 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2352">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/b9JMUpRQD5lroe3fvJBpL3nIuycaiymqfkn_1kKbj1basaB5HsQHV0d64_eG2PFG5fmhdjFqt5l6iP9YVK0qc8wEl_Ooy7UWEjjiCrgX8E6GnAq2_SLRilM84zqkAxjQwERrvPEuqUAdv4UEths5C4IUC2DBCSTJTUxJ754z6L_lGOVXedh62BC9Dzokhtc9jEUHeuCklCml3jTxh9IYTWF8e_o3zEVB1UE-xe3hcKggu0bqj7KaHW5Z1pnvz9ieZbfSlx-zkwGt8aYPmZUFqjI5ZnANzWZvnmsSrefUn6-siP1FSp8xYVUyvyxulro_5zXyjJ56I1NP8ZjjLG_fFQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YqONX6Tmndo5imkUu83JvT9O90dm9rZcyRDYnGRzhKZqwIsvzA3ElG41Qf4Gpwj-_AJ8alN3CrjTRWb5i2Vo49_5KoWOd3MJMgtJhtMNDYqBj-aDiNnErFjRn6W-wjfRqBD8I6H09ZDmGJLmFeC7FeaMWQ89eWS6Me7zmbSWiE4lSYU63SEeTQ5gMADpOARQEAr3u4cSeg8OeIJa-aOALopcjHCZskXtWCLIAonieA1CnMmQ1toG8vPZK0bQkXoAV0XVYQIAw1TUnKfheq3xfvypREvT7tchKtrCrk_uNSPzn0Tvi3srGjVjwlrIqkkZNXQSmz-8h3ARyZVxmWQvpA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 77.2K · <a href="https://t.me/ircfspace/2351" target="_blank">📅 10:02 · 28 Ordibehesht 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WcppFMkdbiVClZoQxNYLO41bVC51BMa3-46K69uMa3FF8LR7FP1OErVIy88qoBNkGQaBpT222vUHoD28ihwHaJ4LGHXkBQ_bRFZKBS9ncTg7Tu5MLKWDNvpmTA0ySqWaO95ll0tCgHuFECOIVu3sD55Za4KqS697Cw2qPw41GY8B6pdjCFrZpyH9x98KOnYevVqNVHs5QguyK_kE34BSa0Y2wjS11l8c1HQf5z-ZppCZ4HTyEdaAbXS-Qbnf_-D-UpA69zj65FTkOTUNEffTYTe1CedPXnNQmFNR761C94_DrxOuxyptLrHXfXcmsR1xQqzEIovmy4CxypvHK8yCEg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Mk3MWas7uNVGLSLdE559sOx3Xt2yTSsEU_Y-C1-xgfn6nnzrdhnxkNgTS6g_aPql63m7-xy8vsFKzWZU6fI91h6dmYbJq4JdsFANCacKs7sy5rXeQ281nSyahFmvzHSZ18oYNXwzNXnCFenZkHCUYPGN6HHd8Uy-o6Nad1TAhRnrQzXVoaHrke2KC6am3jN9LPMBlXQuLC-wGIjNgTO8CpXOBajbfekL7p7wlXxAe7TxCC4vtxlcjGTU8rtx-o6Lb5PMfR-iK2Kjv6vcjyk_1IFxinRSxh1yMh0Qnd66ioJ-9TKypM42w1DKA9MTqi2U_cGCxUg5Jsvl2WDlaFmy9A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/ircfspace/2348" target="_blank">📅 08:49 · 27 Ordibehesht 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Kaf1ab_r3VInFPNAgTHdv00AzjlB5Ct3iaMXwk_ZoprelUfHoVoL5-_vYW0_ZsRDSKM1IRK5qLwQH-bj5Ne3VBTGlpmi_zWkbO3GadUVkxUMYdZdji1zdQ9vpITPNdjsgBZYEZqB4vT8z7jXQqkR_VEVIH0p3rm5DDCdNl7tbuPfnw3ZwSXIRRFF1kzwAqEo3LDRJjuaqCD7Wx_LUj9ZFNlbpXdBzrA56dH8ztWQJZi7_cDacgAdgN7LC4TBS7TOR3_Q6KrwPqDQ7SSS5Mf4NrxFv_UjnQ3w9rz2TJtv3y5KiHMY1sY9qEzHNPhX7o_akdeUYe4OuJ7zOW3qpLO4VQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/ircfspace/2346" target="_blank">📅 23:40 · 26 Ordibehesht 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/H5GiqUYUm4pio1ZRnI1_aajrvlMjbShcdHxoNBciPeqH0Sv42pNtS9D1WCwd4QT8knPSnLsyDoMHwADlIbdxRaR0oPFuSN1H6U5rGwaexCwJk1dnGX3Db1t0gD9fhow929SWV3HNBcEkZd91AVA8ydwrVGTkMox-tZllEDUOJk8qHIqSrIFuNf9G6o7-Fmq5vP5yskndEWwd6S5-jdM79-eVLaUxgeMNhNZKlMCnkB7_r5KrWaS9mHoMKu2laINzZJX--rS5xwvOIVToAtP0qc0TNON10FGt7k0t6ZSRFYumTe1qAzmrZYn7C9o6r0-WfkvxiGOFCmBQCmS3V7bLcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رفتن هرچی که تهش Hub داشته فیلتر کردن؛ حتی گیت‌هاب.
قوه عاقله‌س دیگه!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/ircfspace/2344" target="_blank">📅 09:21 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2343">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PxyK-FfV868ne6CMtuuYzxubcNRny8l83BLsXiI_7LXGNJHdiXORA7_AXINciMJ-CMdsHdjBba-CLali5RjA-XC7-r7oI_n9o7lasBlzJQr1qhmSCXPDmJKtWxdJBTcpXbisyews7O3rZl2CkhifxvGakN3UWivr7lzHkdwnpPICPobAvAMqCVdGJnztms43NK9GZqrUoXKN3wdUoIsUfb4jy0IZ557t9DDv7-IOyxB42kqj5Z8oo8XYp8XHeff1mzD8W8euU8tBuiNUZUZbCzLCWv_xczBaJaEF2TdDidVcE3tKhLhAcWzSM4EZdITxX8Nbgqo-PlgsMziFZpWJHA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ffxXiw42WgCmenArrybaofbRTgBaiJNd81HuiUTN3mTn2qBhYJqTqaDdB4D9wA6YD3OtDisA973MypTmYI-T7QCOLulFyT77OLP-CN7qqpQOJxi5rezrLod9JV7VYPs3vR-FfOs0EVGH92glhiS-3m9N_oP0Tg1_CD2bfqz1QVpmhIwubDRmd_wpv9vYlUDfyMmcQtP69vFBVXM2bat48fnAvtYRZqWc1n4TyA6zVd7_rYZc4bBwbwzITq0krCR3-8uW9_XYvBsuG-9yPlTjQFbls5kZW8j_x9ZmXsjjjSmczuusAch0QAPTqvc7Wd-ZoMq538Qed0zoH8zpIG8xdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه آسیب‌پذیری جدید به اسم YellowKey در سیستم‌عامل ویندوز پیدا شده که توی بعضی شرایط میشه BitLocker ویندوز ۱۱ رو با یه فلش USB دور زد؛ البته فقط وقتی مهاجم به خود دستگاه دسترسی فیزیکی داشته باشه. برای کمتر شدن ریسک بهتره ویندوز و BIOS آپدیت باشن، سیستم کامل Shutdown بشه نه Sleep، و برای BitLocker رمز یا PIN قبل از بوت فعال بشه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/ircfspace/2342" target="_blank">📅 09:03 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2341">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JPLq-RayQiztUEjMFTkYb5-t9k7tNNfG_BdVUokn_ndXZs-dcEhND0bQ9B7-Ro4okza8z58Ay0xuY5IbLaEB0lhW0YB_FPR6m6VwyZGgM7PmHjEYEndLk2OcchoHUJvRy4-Qc1vJP-zGlHtJDXsHp6kdGf2ed-3nD80PJwbTyC6xAWgQ01xlhBPASlnaRwI73oRR235AN8LZ5XS7I8hh1yjwM18J3nqkkgH3GRxq85XRonxnDC7C2stv8CEjvEsX8m73oT2RXPjxWkNN97dMQcMKikunWkMGDdCcMMBhGJHiJwOmIogLJlbSj-SpiuZnFpmeP6btt-u8-0RZIE-uEw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YYsK3rUUG5JMCP2GZhaSwdpdWJzuA-BIOTdVYBWwLNLZeZShs6NKMDCE0ccO5I6G5368C4D7r1DLqR8kbIGdLEH5C9StaKtTOfWRzFR0os8An3wgzvFES9ccnEfJIWDDkbrtTN9uegTJUlG0EVZMOaVocqaO8AKpYIwwbXIa_J0FjPVk1uqj_4Uh95IuEAqXHeCdJao8LYayhwChdXIpDm3J7bxkZS2qpn3EM2KxAgRO3Ok8lVnVd-SO3j-WbPErke_SFgK3y4oZvyFohVnDHMyHIm952RHy3jfF65JayGs13k4m7KAiUJP4gEfyrytSsFPytNMZb2Ii5xwO8IPmWQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/ircfspace/2337" target="_blank">📅 08:25 · 26 Ordibehesht 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cmZRHVqDXb5lscfOGxPSpJNo-BoP26Ya4EjwpZtWKzBNjOMPtS-2ABNvwvsFfUWLPjXQ6E8u-K_xHDSPPG1fxCHGC30zLo4UkxPo7wcUVmVKuvpwwJZIsoTLmA6yOpjGmV8i9niPoRd8nltbZqS8wVBWmc2PMAj2L3KplAAq54O_kMbteBHLXrymTNeaHhbVDsCQvTngWUZ0CVOlzISWuC8WftOKsGKi-v3JF_-Py76Zw1LZnyg8rcG0zgR9BKvPkxCMbPEUb74wC4CEgXG8PPH2dFQ3GBMGJou3BO8R4J6JGpcggvHYI8jq91KSBqSJW4dJDM1JLYOR_VJvsTv5WQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/ircfspace/2335" target="_blank">📅 16:26 · 24 Ordibehesht 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/l2LAuoCQyIJ7J9VD9Sj3Zg3BoWf3sTLIimz9xKaQ9lP5EtYSkc81CjyZ9SBiG6y1bSSIjtT1NrVPfRcUVjKZGzlZUjKDKo5gSEvogCwALnfNHHWbjrK8Ww0vzO2H_DtSBopVw17loteUcQOz3urxqchRRyJzIvvry5c-NFXCWECIvOCjMeKwbVkQR6yH1RzRetPmLQXcDIM-cgPFZd62qoQEdIldpXgOEWTFZW7ckUBM2urZgVQcQVcnYrr5N9ZjkjB1sCdutOx7n956o2EjcJeyCUnY1UtjvK4ZJAo7a6xu15AIya8QHQEsmX6KwUlWQMyZo2nz7GG8iN92Zp4EBg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bSyxPH3PNV7PcUUzBBZ4FwyjlyXbg7W9ixL5Mn8LvlSHS5lw73DuulvjJISgkra3cz75YOB82YxTrQZ6_o-CpuHdFnWhmbiicnmyMafZvuD-Sd7DedEoStIbdxKt-iaAZ_dWVUj2Zm15WR8IuK86yDcvCcldPcmM9u0k5e5xAV-b07wKHJV-7WvmmczPeF5TvN7x_3mTS1RSTj8hjIyxCJhleH7-5RGYGwQJNsqPSrZe_h6XMMam1hPnFjSJ_S-aqalZJ4TNY-Tq5tV_CyoIxvf2quOiTeTnpK08rTcauyLgtm8nEr0e6I0bNudOOvHKyhL1qADWsDBH4cB9MoUcrg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/P1DqCDrx24dK_2HSN_gOa6tk4uJMlTAmkkK5wMR_-4Rxn0iQakuUDBpF-GE9LKDhas2WSeNW10u0WKkKMXUKVhXDiz7vsoIPdWXaQgetCj-mJ5PGG8jo3ZTPqmDvtlNnYlbezsUBUMivyW4zxiYSjzbNDtIGCAkDrvyoeLi7l3rNLcy8j6hLaq4XY7iBeFBPCJQZHxY1nCbYyOZ7DsVt01dAZRUg4jravdrzNcQITn19QCjstLQI6IPO70pdgSf-0jjGKwLWYqEoO9lFvK8NF_6XobAa5RPC6L_N6nYSlNa48U8kltWYikQN7bb-cmUc51Ir0ZsWHYtBHr-DL7bJWg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/ircfspace/2330" target="_blank">📅 19:32 · 23 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/ircfspace/2329" target="_blank">📅 19:30 · 23 Ordibehesht 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/d9e9b1e831.mp4?token=ZsGCMbo8yDqZuIuy9fgS8XkvsiGEOG9xUr4VZ6XyU8zOrFXXSALt4SA_wlaiPzICLd4UAxRFH2N8RX8qYbXxuI2Fz_-e8EVTOfU6bGn2yFlodTB2Yfx543ZUhbsPHRU30bStskwC1fzIRiBFwZgpM5bOcd9RWU4IHl41d8VBnaA48Gl5iPMbVr_s3fgnp6wvR9AXivf8eS2_mNR5CCdNetrpgq9z7oHmhkrdYwFJON7NrBqetcIyKRIYhVE8Z3xGoYGkxFRFonHTZVBnf8uNVEypT1PlJB3U09xkUMrI86PK3qjSLi5r_ydDHm3e1pa0FNnsNSJbRjhVoFkEUm3g2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d9e9b1e831.mp4?token=ZsGCMbo8yDqZuIuy9fgS8XkvsiGEOG9xUr4VZ6XyU8zOrFXXSALt4SA_wlaiPzICLd4UAxRFH2N8RX8qYbXxuI2Fz_-e8EVTOfU6bGn2yFlodTB2Yfx543ZUhbsPHRU30bStskwC1fzIRiBFwZgpM5bOcd9RWU4IHl41d8VBnaA48Gl5iPMbVr_s3fgnp6wvR9AXivf8eS2_mNR5CCdNetrpgq9z7oHmhkrdYwFJON7NrBqetcIyKRIYhVE8Z3xGoYGkxFRFonHTZVBnf8uNVEypT1PlJB3U09xkUMrI86PK3qjSLi5r_ydDHm3e1pa0FNnsNSJbRjhVoFkEUm3g2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/wAx15PNmcRtZjQaT4vhohRNNtNwpTNek3aggf0DR0OSJE3FuvFlMH6bV1ZT3nIwuNufuQGVbwgVPm_l05F8-HJiVFAywpRfpl21_0alIehgQcM91trVjVHUubD2YTrLfYhUkL-VWb5GGEaga0iuf12Y4O7E80lh1uNr0SPWRKPWBOdapGR-zcB1J1QQQyDjIcFk8c7iUmHeG3jBMIQ4YL-H5glVhicTXAOJYfkTLgK1SvTdxn-xVl1mQ-s4daXG9P6MroZVQBbhd9m37ci45RSFj4TmmDHNs7UUdZuFdUVoEZ-fye4Qcq3v3czfKKX09Dg7Mf9_sy80qMTwLm6To1g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/ircfspace/2326" target="_blank">📅 19:21 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2324">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/isn65gRFGknobPFUbX2BvnRmfi0i9XhAwCm7k9cO9btiIZz2KJ5OVcNnC0vaKiNJBlkOUDAxFGi6hEfxHtYlSWHi8xZU46pm7EI9ZSaKm-e390XzWx20OHLFpsmbg1Oa3dYWdk1ooScLMTztYMbwsrTlToCcSza1CYLpIKJphKfc1U5oZYz6YBY6Ar3xmmbiPwQ6-QBV_MLxnjsK0dZTFhLGcG_tG_yvfBBnkdJfLCN32sgYuff099fxNcKxRcvyI5V-0WUZer0h6o7ARDYEO_2YwWq5K9ZH76Jp_nmyElOrjNh43X6cJv7hZ5J4qHTcWUxiBNncjYgydgrkM5mvRg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RQvK1zt-XRp5aN7eZH2PFi9FgirfpXBdzwCkwJFpFVvAPavuvaGQ63s3HbokxlxKP88TGCnHJZ2GpjhuFDUaB4PYv_G8Alpo7PswVdLI5qT0ZTnfBxrvuBsUCQKH6_Ib67SM1PCAwrAKSgtxDFlhjPP2YhEM8uDQgPsjJ74_RM7vd9MhsV-k0mRSqUPDuUiyIgErzyeDhNCGVJVL7a5QZPH_1NKd80vORNHs0GGc86aP5zF97PH2XBLVtnhTnIlNmovDQjQDE0SDtkDgKdkWlz3jkuI1VieMJvJB6PwfcK8ztRCls8Xe0Avmva4-zBgi2klEi_x2Lbs1-_1a0p7RNQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HtPf0JmXv2BRSQ7mf1Uo_84WwssRI1ghqi5jrXHaO18njptu8bi15GQWxCwTi3pqlorrKV7krjh91oV1-7HINf001FCigUVCfyWWVBImlnt2lVIJ_iJLQ3IYofM_vHZvVcoEtHlJ0b519NIEqIocYs3_22ll-C3DtLc_UMtv8T9_EsfoMUegnOd1YjpoUhE3liF89g6jrsYJo4sbLl3p6rRLATVy8gRyCPiRTgeBzTjYBDd5oWxKQxKS4sz9k0MbRE9qoeFIdIquPZwLszaW1ghkVbIxlV2wO6Td6MGEUmYxH0sBbZkgEymQwd_KkWXzUXi7VmKlQ6BrceGGa6Iplw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WJhyYQPfyhS3x9o9DGWALc5Qbl0yWD3lGWOyholzSC4WbgazQnDQD7PZvjHbNe0btrMU0c8oRqmAUoWZNiNXIInPzuEOfLLg3dEoRzUrN194tRcfgtZFQcgergrqw9Adtzicl1yRktP4iCrcz8YdSGLceOVBv9L9yVIbvCZ5Nz6WV1CMUxS6hYIG7eCEQC4DSGB96fLtDd76vLpsz71qpJpfKrUGGrOhmY1cG1gQyTptJMCke17xZ300y7C8aLqpmn3e6rI0pk1XN5-CUlfMPFtZlVg-YVlwW9pib0xbC51qsq5ADGuP4rzCr6A9LFpIwYY_MAj6_RhPaTCenxJyrg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NWjPWF7jOcXpdDJpDVc9j3k-nRYkDsqLn27fOF-YOpc1NfTQd1-xRepNC8BfMupz_J9VQqo0CqVcMdHuer4p6lEYC7DGBL-gCIFO2MPJsSsyhSKn30KY5eXoHupSiV3MQe7SbWANj9GMEgvBavumrsNkRbBVqIn_J3EaIpBJP-FEDmOfPYGZ_hzRn6uYGCtnBLm_UkFfApOGnLmeA-ZGa-q9E-32CfPgID9_28XvEqUx8cXXj8oq-fBDqlTNJ7XC4Dw6jIsrN0zaXy6d9foovhL1sBVzLEqkuJxQ540uaSYAGkUxoKWoZK7IQrw8-UZsfLEIUqNnoXiBfqL3dQDysg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 41K · <a href="https://t.me/ircfspace/2316" target="_blank">📅 10:26 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2315">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pt3aV42d-1RXXkEcsEqymVW3OkihQYpOznGcNeQIBeRq6BBKqpdIbUTqNdWr4tMIkWOBZoYKzM4kosi6GV6nYrz3hu4cwbBfFjLLbrOc7uPt_sx9GkIso9yAL_538A_X7_WxC-ipN6-X8UVNOEslCDHUCHae4WQA9GFvDrU88QUGK78pXErQm5Z6MlgfQAE4lIQeAdbFOrz6-FnbUhFT9H_xcRJZKFGbfQIL6pQKhF01EP59TZcJLD4VS8XWAYzBpBK6K5889aU4NozexSW7Ci0DROoOtvKids36GFkwp4SvoCFk30bZcwVv7Xd4xR6jr-m5hk5EMbYg74XeF-PzIA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IrGg2IFrT76qSEvmHqeajYLJOA_Hd7n-MXI3I0v3WtWYaSoSFRW6OvJzhLxkf5rAFPhvWeYlSkvrdSeImRyj4jGQ-lEt7_qu__hDTgP3OAyvG-e20Qs4tVt40pBL3ncVr5MrnHTK3p8F_eINkkCuXmeVY6l-D_4dH6G4ThrqMwM1Cp1bRp3gVi6AwCVslGxNFLcEayzwZJ1y2LEYLEWGdn-Oo7O5FmCfah3OXvjmTdEz6c8NcF0cx0VwfGFxTvqGLybJMANDGsm_PLOnOyhfLjTxONC8B88HFpU2QpTYUudxExH4tUJifqe8OC35iQImU8GrqZISjmVzZczTM6Xm9A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hGpol4wLAGf_Kjti_842zvSlpSmoP2fOEDQpsP_l7S5yhmlwow3yodf9bKlfi2zFujVQ7etV4j7anvA_AN991B-wOd7vTGT2XHWqv49fMnuEzkQGqOGQTXMbe5PRGayMI3NBChw7GVzQMzA4ns45gKc-LsTr40y4rwkIwpJnSL7E3GA7DcTGOnaSzZUTw7YVR9uqEqkWpvf71-dfJBH3ZbpeEPwUAoidbHt5-INqMCJRm8Zc6Gx_BnQrznqd_VxSqQTCZFwHz6mExkbLsuViTyPKOrBn2LgxR8Y_XJcgMjLEXTkh_F7EHriWAhzXjYT7F2oH9fS5OG_CGcGRCTHpBQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QfnSaH9DhrNrFbgfhDop55KkQLkED-X3FPppJGTXxOwVd72qZl48ozHUin2GWlWeJegm5MONyk0EDVbcNjPmTr3TRogYBlHhqnohykgdYJCSPPqYR1hZQSjyUTn0CZxVQt1U7_8RCDf33Ul_wdtfcsD5aVceWOOtQyiwSlCkdDK5Kp1dBYOUD9wYuBDa7r4BKYBO4IdFmQQGUjCmc5M4ZXB-5jKlQEXQL2aEPMburIHKVP6MxmTPunw2fimXrLYpZG65FWdfLX1aiEf96kPGzYCyEWE5y_yma4ESVjBP9LPB3BQQMNnoTCMiRd33yK7WqaSQDIBfv4R1Qo96Zm5LHg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HhXYwrRDPf1nnJFFtRijM4rQprJJeWTGHV_sMXQ7bh6ssfIH7-M0ZH3rk_TvG2WEm4ShLrhX2rCstaEUMEd4sh0q5aOuNoeHbe_VrRnTecpV0iF_oqmbmHTUvnqcHD3BXoPMwIFv6rHo0SeSXM9i9CtUzGGr8mysruQk1l3vO5V-kxKV26bKZtxhkltam910zF89fMTIXjcDbCyfOUWnPjYuJQiug6Wvog5Zq65u5wJkiW5J8C4h_htQXvj9HvePGTq8A1Eg6br4JZkJ0y3ZbuCx9SUoOdAQMUoXz3RmHG8ydQib5oyTQvBTbDQqU6PYBkKmizmetI02R-qMemAUFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون رئیس‌جمهور از وزیر ارتباطات بابت هیچ و پوچ قدردانی میکنه، بعدش همون وزیر از رئیس‌جمهور قدردانی میکنه، بعدترش همین بدردنخورها دسته‌جمعی از مردم قدردانی میکنن؛ اما تهش می‌بینی ۷۳ روزه که اینترنت قطع هست!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/ircfspace/2307" target="_blank">📅 08:13 · 21 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 33K · <a href="https://t.me/ircfspace/2306" target="_blank">📅 16:30 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2304">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jrOmQ9t9c42IoROgnEvDoVuCo16STP7LZ4W_fMww3dwzQhItGmCQsQAN4PorJRWxWlKdWAq94F3mf4PDEuVPY23O_pfWwcirOceTU4FfKbeM2uZrc6bq7YBJBTJfHBGuIFSPVDT4SVxtr7bjTGvJN_14Wo-JsNmT4dtbK_GVNEuLCEV7EP9ZJ-u1k60zZU_Ha3SdUnPReuY_BBkxNwDo4Lu5owtohOhtCh1bLy2OtaUso_MwaoOw_QI_9dcHWLFdauTWvxMns1dTuqyu4NqKw8ry9ekc8-Bxnl-QqEwglOOm80pRs48PtpWzEh_ded1mk6kD8mXomSi9-eZnNUyd0Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 29K · <a href="https://t.me/ircfspace/2303" target="_blank">📅 12:21 · 20 Ordibehesht 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nauFMrFjdYIZRk7EKWlyIHBIdoxI2Dww10TPLcgQ8zoTaLaKfSjkKJ2q6JVYnUkpSlW3fOKSfbGxwYXX31GmEk0HgHI650Lbxpu_GV_dWPFBsTnoJn4kDeEQBYeOmZocczWQ_i_btdON1eTLs5ZUhy-XOPqFMBoVqsBXlNtpmf9JWN41yFeAS9wSE1PQmi4uUkSRgIT1xdCSxbxBiG7V2fVpTe7N24Jda6jYCiZ2p2MJzwVFf7YLI5IwgtAdUn0MuSm6hZN-iMjDNlH_w56UYEFRT-9IV-gg7ToJgAonGz0GIRQbIrqvjeRjf9Pc9cUUJF3e_HW_aSJibp9Gs0BqUQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/d_pGxvou3EL89ABrvJ3yeai5vi3aSVaKkSnVPB4BEeOaMMAPU-oQ7vAHflYufbcjWMCKhYvcADap0QZvU-9QitgxzKuLV6u7MPYmV18MRUAishjNZTU85TxHN8w0Y_v2rRZEdRjY7tdeVlg_uTwiEo92sJYvpRbovezE_Lg_SWTncqFdWmpBWEuyV1fC0rTx-fm6_WqJwVASavBzcw-gFj2K0qtvEAUVb8Y5O3t2RlW41fi-qg2pR13DJZX6sNp7tPVjGRuawyxicu6f-KvtIS1WRJSqKu_kNd2fo9_YNvi1F23rq8vd1nhlvvsRX19OqczYcZdqhiHQ-gQaNTkTuw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 33K · <a href="https://t.me/ircfspace/2299" target="_blank">📅 17:52 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2298">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Md-nTtSursr3clw-rsrbJd30EqpTDUL3gnG8PqPboLYUYYiAHDXTerWdqBii_YDT4DBWAelultEwwRtugx_pTAjh8TbkT_BUYQh0QA1HL7BIZ9Df5Bw_uLbPDrBkx1k2GS6txRCA3FZxbQbXoSTrPVmg2akzPvBdWIBBu0wqGuQbO_U_mxqUENmoGq8CPSw75Z3rXVlllkWkUq-BBX2OXciuBYewLLdCFviMqJK5L_tMHrG00xP1-lC3No2hT7qWr0tEBPMhLlYJyrYCRx9y_Y0SyrDYvq03hXKsrHIDriLUsIB3YolBHTC0e-SAfioFjdkvYjsa30zpQEYe0Rz5gg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/ircfspace/2298" target="_blank">📅 17:48 · 19 Ordibehesht 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/oCNA-8V7XLI4zBZxh0N5aE9LTOl1Xjvawh_93nUaaPkKD7KUEPoJDiW5K-LVPOZNomVeMmdKo67kOj9PwZN9rIKELXxTz9XIylzkkozY40zj0JAX87f0l_uIUt7eh7z4quA8tfs_Cgg_fnOr8MVE3mMH3rhH5IuAwDsTbfM9fu073LrzjT4N3FB21ljtTv1DA9fkHMWhCo1SfW1VwUleg_S0jjI2irNu1OcBJiMr7na8XwyUTI7jcB8077JTksQSHLYaOiZn71T_OaO9JfRUY3eevZLSapizm9H7p5hwxuAGx3O3qWrkS8jBEYopbVaSwhirHyCnyOlCzXgK-TVbZg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/ircfspace/2296" target="_blank">📅 17:45 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2295">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/awSOhgUvd2n5wsDTGshOJXPXrrZlqiZqYcFe4p6j3fBMM4OWIbZlxK3whAit9T_Afe9YkuXAzbJqn2Mfxc8UYJ33JYWRbvLTahdx6spazTB7_NTNnBzKTzppRmva6sPhNs7doS304fCh_aTtzYjacASi4vhZMteU9JX-ZDo7Yomq4KctAqJ2f_JDiJrMRUI1QMw0M7wK7GZmnEkyFNp8UPD08IUOYoIXde9nh4ODJZUI8R07hm_ivFIo6EMAiF4pmlx-gSs6fgu5ftf1vlgtbOYR2fEX2fjVOmb3uVRiGIfmskDc4mHpPRBWYpr3TKYvnT5XowSx5og6haGJJqYQ2w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BdgH4EWdhsiXNTIL1h1R6L1RRu_ITcjiMyRu3WZj80RLyEFKsMZnpXTjBwSu2rzXSHJS37Qq7xVc32q3w7e2kYDhg2yuN_Ozk4Wh3rZcGCWNq0BsCk9eClbVY1Jr9Pfl3899j38hRkHMz-8bRIgB-U8VXFh0kdF7pB79t01CWDR9T7eE1NTJIidZUeyit16VLqFqEdvIUnJnz_T3uxz-dNxGjascgzIxpmCq3oG6NmL9imU1qnU0WtORskDCo9rypc5nB_K3HYlBDdIWO0P5uUiL7EW6y-ivCnGEjBYQxnT7oced73v21hw7a4w0BQpsT8cpe7vK-1cFCfEDHonLHA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gaj_pk-koDFEbR_xK1LxVjMY0X_KZAH6U901OhAZYvnn0MLAuKi_7tiGvySvAi_0kpZXtNkfE-IrkmX0KkTIe9xvf2vij5E8Re_J-jxCKPytDBu7KAXCMqcnT58_XF4COyRbLpDRUKqcViCFVr_OpskYdtYGml5HoAs2wQQ1HaQkovFVQEXSqjgz9wvyI5ddoPu2gV7NDfF0OTQI1uA-0Y2pXt5vkC6NbOPQx0tswwEb7S1XnSt6W99z6UHUNvj056mtrpf7LCpGw634Rdk41Aa2IzdOQMkTY704iy1FA7rtgiiy5KTuFk6WvOfVf473jzEnHcTU8GP11plbkoZZJQ.jpg" alt="photo" loading="lazy"/></div>
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
