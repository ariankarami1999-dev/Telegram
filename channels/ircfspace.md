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
<img src="https://cdn1.telesco.pe/file/Ox6xBodijzWgdZCfn2iiC8VfmUFiVhxoKp0s3JMTnOuA45yzAXtcUT-6SaVCrC2kkVwIIJFWBa3D8Yd9gkOObf6YH4iM-v6xbRt1J5VCasg3D3WerQ5jxC_LTyYIIXbHiAU7QgRF3D1zbBV77ukuq6HSYk1enLE61IDOowQRVwJ2UTJQ8U-5huHXr9TQmocvJ9S-0WR-g2bV2KGPvYBWd0BYwIbMUuTXDBh6Pz4wCrpGKMhvlin-k3SpPJ5v-IBuvrUJY-aYW_rdGhnAQUm5AmBcHCJinvx8WD08rETzg260nMnBUU4aezf9zMKQU8tyZptFnA3IPUMXAMVpdKEFpQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 IRCF | اینترنت آزاد برای همه</h1>
<p>@ircfspace • 👥 97.6K عضو</p>
<a href="https://t.me/ircfspace" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 این‌کانال با هدف دسترسی آزاد به اینترنت «به‌عنوان یک حق شهروندی»، به‌دور از هرگونه وابستگی حزبی، سیاسی، تشکیلاتی و ... فعالیت میکنه!https://ircf.space/contactshttps://x.com/ircfspace</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-08 23:22:49</div>
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
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/ircfspace/2399" target="_blank">📅 10:53 · 08 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 20K · <a href="https://t.me/ircfspace/2398" target="_blank">📅 10:51 · 08 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/ircfspace/2397" target="_blank">📅 19:45 · 07 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/ircfspace/2396" target="_blank">📅 19:39 · 07 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/ircfspace/2395" target="_blank">📅 08:50 · 07 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/ircfspace/2394" target="_blank">📅 08:31 · 07 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/ircfspace/2393" target="_blank">📅 08:28 · 07 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/ircfspace/2392" target="_blank">📅 08:25 · 07 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/ircfspace/2390" target="_blank">📅 21:56 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2389">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qQ42dBe9a1kLsDONtQWRNd9SBv1w1-R68o-nXr18zd9J0IFPh7NxwVd6RJ-bAl5xGRNMde8oc1IQvWQHP6B4EMpkI6ULPLqHql8Pww2Crz0OOggL6qA6rXF3pl3pwcVVVWZdRWQpqdu9z32Kk5Xr1RByatnOBn7Q6av__ioWP44LmF8OVVxFVjR8a7qQZVI9z7yCZLQ7VWqHgQRm5HfkgRn8BZZ48MkAOsxH_AlxUMaUvSQXm8Da429V27_C1Mre2rHn62ZmE9eTqV7jsUvNdZuye2_pNLG9dRa8alkww_7raVtIctthDVZzp5V3FYN4jc1hPCevBUbMiufbjx2eEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نت‌بلاکس تایید کرده که میزان دسترسی به اینترنت در ایران افزایش قابل توجهی پیدا کرده و به ۸۶ درصد رسیده؛ هرچند فیلترینگ به قوت خودش باقیه ...
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/ircfspace/2389" target="_blank">📅 21:31 · 05 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/ircfspace/2388" target="_blank">📅 17:30 · 05 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/ircfspace/2387" target="_blank">📅 17:24 · 05 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/ircfspace/2386" target="_blank">📅 17:19 · 05 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/ircfspace/2385" target="_blank">📅 17:12 · 05 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/ircfspace/2384" target="_blank">📅 17:09 · 05 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/ircfspace/2383" target="_blank">📅 14:43 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2382">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PRaCTus9gF22p4RUVURQkwZPsTZKt2f24WSFNZJV-JCkJpfPExrfUR9vup7muwXzZSGGJX5xVmDFk38QZFWCZDPPtFcnxQrZ7glVGo0fQSf_bh7wAvSAg800R2gfFvEzfLr8CVo4Qdsm7uehkJV1IRYT42XI7fMMlv9c3tqj2hDmNikHXjH-Jsmb1PTYUKOu5gpJUXTr5whL4pdCM9Mr7kHtR1Oafg2ddct9Y2n27GMD6KNWkNXgwpyabGnfP5ERRKoD3hXXzHfE_NUW7d8xqAg35xeh79DE4Hw32RoX0cQxw9xuHYTl4hW_VtNDpQnwDTFwsFE9esXremhGcNzuyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه‌ها نوشتن که مسعود پزشکیان مصوبه بازگشایی اینترنت رو امضا کرده و بعد از ۸۷ روز، بزودی فرایند اتصال مردم به شرایط پیش از کشتار دی‌ماه برمیگرده!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/ircfspace/2382" target="_blank">📅 23:19 · 04 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/ircfspace/2381" target="_blank">📅 11:23 · 04 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/ircfspace/2380" target="_blank">📅 17:16 · 03 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/ircfspace/2378" target="_blank">📅 08:57 · 03 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/ircfspace/2377" target="_blank">📅 08:51 · 03 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/ircfspace/2376" target="_blank">📅 08:40 · 03 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/ircfspace/2375" target="_blank">📅 08:36 · 03 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/ircfspace/2374" target="_blank">📅 08:38 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2373">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XRjPCR8UchewHEQ05zq5fZ8x7wMastmYwn2Vx_Pj3FYn55WB1jwVBTPebdZDE137DJlhRNYOQbmti0agzOY8OuGWwFEsUuk21UCiHYnnl1sKM2u6RbwlnCF97PrjeS4IXB-huBT2bLLiesK0MiivcYy2zvJlGjHAaKRUdGHNCzAppMF2LIZljJeWyx9WPQ7cbsrSNYw2O8OU4UZvdsikZbZmxHzqo9shUwPSwmSsYJohLVc5IemS1kb4iW0wIs9zaTFLT8N6WvPiSxxYyX0Lhbx3whMET59Vp2NYIihlil3UwpFlrCcs2L3E61WicaOYEAr1dKKx7ph0UQtcBeGQOg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/ircfspace/2373" target="_blank">📅 08:15 · 02 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/ircfspace/2372" target="_blank">📅 19:51 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2371">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Qx_VIUZqTVgjN9ticLh9wZcwtYvLNW3CY242YUZE1z3BQOuUcohuSs_sNx4rNB1YDiMic9jpQZ4DK773VSsCoo1EVFDFuj_p8L376PL2Q-4TUQLgKkoVOMykgk_d0EXLBHTc8isXUzlmEpSa0e-fa0LDqdP8E015X-BABEF_i7-6NcI_9t3dyct9x8Qd-3ORMXtH_iZdr27zN61rlXe9dsO2kRlK93gdDnHe7K_2YdCxE5Q2I5sFNuMTSB0I9OW3rPRQdzIp7XC9zxoNqkOQQB4pjOvSlUBQgFhpk3b7Zr5yMRO8EvE7_yG8oZX1A0WKbET0RrABzDqZk2LqSEdQgA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/ircfspace/2370" target="_blank">📅 20:18 · 31 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/ircfspace/2369" target="_blank">📅 20:12 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2368">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lWXkqV3cBpPAwWTrZOFDQfZH9mmSJzY9Ji9-RRCP907erYNuU0SXaE5dmfY4o2wsYIEc3Lfbfi4Yww-yx3Lrl6qqIWjXHTqnIPI7363SrwCr_wxJTxx80Nqm0JBQNzyE9zkKtpQQfEBKwMGof3vvtl_O1vwXbqLEHTPCHAYe9uzstQASfQXO9iXVTfoKiADkH-O_jZVJfYXIpceH1njKjEA5-dTZRiXNUFAgajwVBZMqDaKLMDnO8c6CaFSXr1-zTiNPAWV_dZB3p5VDAO6En8Tu4kJ44oyakRYvcB6pBifCwlT3pLWR-WO1s0qeBBBlQJy4AckYoglDvD08bro6vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمدرضا فرزانگان، اقتصاددان حوزه خاورمیانه در دانشگاه فیلیپس ماربورگ آلمان، گفته است حدود ۱۰ میلیون شغل در ایران به‌طور مستقیم یا غیرمستقیم به اقتصاد دیجیتال وابسته هستند.
او به وال‌استریت ژورنال گفته محدودیت گسترده اینترنت باعث کاهش بهره‌وری، تضعیف اعتماد کسب‌وکارها و افزایش نابرابری می‌شود؛ زیرا در چنین شرایطی تنها کاربران ثروتمندتر یا افرادی که به ارتباطات بهتر دسترسی دارند، می‌توانند اتصال پایدار و قابل اتکا داشته باشند. /دیجیاتو
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/ircfspace/2368" target="_blank">📅 20:09 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2367">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/E8_VPPCCHqR4qj0EQhg_UoeRdEKMRNDsNN2sMcGhOdTECx-v5wBQAk8y81rifUYNIUEzva188j8B1lRwqIdoAnCr4ZFoOPic9j_j8HdHFaMaRsL9WOBuSbcPihGyswfdX1tFte2yW4KRPtzCUAtSOR0rronehT1Y-c4S5BomnzQDd3Iaz6NfE_s5P3wLct5B9bpYcHO7bMuBhKEFmvd6G24hr6tjWyeNn8QAhMV0XS8N7lpcB-ptWWHTo9g2qLaxH-uUJ4zmnk5hjS_XkkOImCN_WlVkP_14v1MYITuZTib82-46t1CcPsLAlebxwe3XpFy9Z1seFHP1SZVJ5SCKZQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/ircfspace/2367" target="_blank">📅 20:04 · 31 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/ircfspace/2366" target="_blank">📅 19:52 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2365">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Q4LnJbfJZ_rOofcjgJq6KlveXnqsi_LVghqfDHAz2sH5YvIrgAoHrbtc91NC5ffNeU0A0yiqw0CKzPU7seav8FulaBnpJuVlxyP_rb_t8u-64uOqtBchByl6PTZnsqbftUfH_aoCmcqmPnF1PFg_KNsQxhV4g68Rk7XzS1Or0-458Sx0t5wsjnBGPG7q1Ay4wHVZha742ZAPqh1A9N08MpOREw0U6z4-yreKX5oSzzsPU4JCBlXPMLsN09ezXDzOjx-WRqpaxS7yN8PnCJM6BPfgScqyb4ykdg6uaqZHKTLwp2txHvDk27eGfjNXpAMYZEIA6enEE7CUiB2lgmYu1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قوه عاقله در همراهی با سایر قوا، قطع سراسری اینترنت در ایران رو به روز هشتاد و سوم کشوند.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/ircfspace/2365" target="_blank">📅 08:39 · 31 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/ircfspace/2363" target="_blank">📅 08:27 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2362">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SnhxIrkMEpN_h6tQhvca0V-emCTV2rx5Sc-cMKjV5j29B-Rzw7Xn86NzAAHN3n1uhRoyCtDl6PQhCWDManzBsXT9j01Cv6jpRG3YXBPZNo8D43h4jqCRoMnAG9UvLWBl-9L2aDKxzWC27iJ8a7GbpTQ3DiKF5D_GEy0le67KBKFVQnjXtKt4Bk1CicZLUqLEH9kc_S6nUeIc3EwJLcuuvtMJGNpAtzzWMcphWna634W4t8d1mp7x5pVmTaQbbaNGk7Gjtnd94p1Qp-WuVU_p8wH6Fx-fHUGUreW2r3mzlYXN-AKgUjlLPRV_HMiJrbcdGqgkFGces7eHChO1o60fsw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/ircfspace/2362" target="_blank">📅 08:24 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2361">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RumeTaM0nr4IrOkBpEKy82JLoMtvMWI5vG60xx97JkyinGXg-TQcy_59qA5q8lqn1q5FDY8twLWvqAGpXZpBya41XKOU3fDIhC8SncGQ-IjeH86PyBLDxBDVPgvx9nMqpST2EUqbmi6a4RSxop0qVFWmZj66OqH_tNHO30rVIHDpL2nCLieMJDQpArDNYizHSaPlcdx7hg_uOHIYYBHLAJNCvSpCTAjwbT5NIEXjQVkh3AxZ9btyOK1fTSS93ZM13HCQgk73JSdNP5MUm7rCwKgVF83VLuN3j0FclquSvbJPYdADSLIhR1PA7XqWrjMm1uz8TDYJd86Sb9_Gvk5XnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هشتاد و دومین روز از قطع سراسری اینترنت!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/ircfspace/2361" target="_blank">📅 09:00 · 30 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/ircfspace/2359" target="_blank">📅 08:59 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2358">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/psH5MRRJm_JwyLqigxEAJMvwHos2Oj4zKREltXZ9BOdoyGeRNIizMaQMWRYEHN8h4WoztVeousE49CUzxjuPnOShFeeWFrMl7e26H-FQwu7J-yBZnz6rZOduatUPQJo6uA9qq8WQKctzyzibG5tzMrnvnCWkWFyRYKl020VD2UBLXIP4Hjn1PS1IPRHvMDbwHuwblPKx1OPXPtl94urEKIHLs3MAHFqiGYL80Ak8fIWhnHUDW-OQqQOqHV3Xpe4-PD5nzG0QhK9iBKRXVdyzOiMkYbSH9-ZPo6gzRpDP8K5UKWOe7XkUDtC7y071uHiqJY1wqPH6qdkbVgy5ehsA4A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/ircfspace/2358" target="_blank">📅 08:50 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2357">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Be4Op7boJq9iLOkjMHvbsiyD-btmx634biPxJRBpHQRz6xJ3SGZn8xGUKY8M2MvCGKjHeVsGQiPqP8xrl0Orayw10gzcKjD8assU5txxFFbePBt2Uh-dDBfhgb9Wu2nr0grc-xOjwA0BOjGJh6854JFM1UIXO_PW8vMeWbbeGR9QYwfypm4jXfImWD4Y4nF9iDzKNeMiMnF4ja6n2s8cKTXrZeLaHyafY1spcbIN8XUgee8ul8uw3_RMkss5mPNZXBNI0luuAgFUcrW0NJvAjVds_GhqKC_0bn4mlxEglarOmL7iMlX5wK0RfzrONigbiOkcmxcNvE4MdJ0sxgW-qg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/ircfspace/2357" target="_blank">📅 08:38 · 29 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/ircfspace/2355" target="_blank">📅 20:07 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2354">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/c9rg2cDdTHYA5OfkvejYzo15PJNuDRGjnWUjOETnUjfC_NX659vNtRz-Cgc6jazDxUHwV-8IPk8ZNZZf8r5xByImwXE935u_QrMmZnYaueAOHJycQUxzVuiExUCwYHnkixHvjx3vKSzBPpn-ZeSGjjSKbqrRvyZKMkI5etHY9wD2ENzAqWqWBp5IG25gW8kX6XHrcSc1yZV_DjNzXSsbK_hxuekTZr8c1RfmoudAA1qB_jQSk6YadcMt3GWT1cW8VJsNRlFgIaA0KM91hbrm_69rYEQIYSRzrrvcKXr-zErPEhN77TqVQbjYWGUr-d9WCB0nGO3BvCtz07DqAPSlAA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/ircfspace/2354" target="_blank">📅 20:05 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2353">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BREdiLUOVeNBqE_J6ywV8MYYy9pzi_-AYWcKEQZl5ns-oM2vj4rtdGXzTRJ55kKcU22fJnNOTBwLJpHyZ_XW4y7IGlZ3BWUZzaJKTweoDzYPUSPViskIJBPZWa660TcDWeRAKSinu0-SkVcvdVgHpqCTZfmH_yRAwAoAanRtgSJmdx-ruelbb1z6pHDQ7qwNZmEN356wJPoIFgyuzSYHoxCRAEmxBwaz2Hn0g3qCbOOcDiUKcw6kbvJNGMa_OD20PV_8QHMqqzyKJzsYyG3e_wrZgsgPeuP8TJ_nnrTL1LmmnaZklYMpMf2m97tGHIEJaEK45KQG4ViDhMWTBnCPqA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qau-0uALZ4xSyUBBEtvNUcF-1tkkjyZB9Z65iRi35_wSMGoCcHibV0dSTq-6opZTP7UQwZHgmnFtTVxjYnw1zFT1kEq4LPCTIRy6ltM7uwr1WpX1lXhKvg6Ri2q4XFzfW77_s0-Y160pNhyn_9FmJN6nTJJDOQkQT98mtHqXfQrG5w55zHlR0yW6gID50rNdslpoExxHTsnt8G-wU7shEFdTQZ3d3_nCoWY_1b7pxlkxbtmPZnXSYKo23NEUhPbvCXBm5BAu7lxk-t5-lutUViFT9G38mrvD_dWkbOCtF2ZqctXdOFCxBzSQ6IDj-mvkT1B2ofn_qNmzu9XTbs7tsQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IxBUyNVZJuhBEfXiPBMhRjrbgcx0MXpqKDE15qSj9JXZbCCqYxRWGLX4TIIJnTtHINiAbZphlCHc94Kqm2J0rfEkzwnHxTgRqnyv4KbMdnSlc464B3372wjarbxfKEGeEnC5uGLxkpFPRrQUiVaACfORObmxcoqtWT8tv5-uLp9rnbFDxFpsJQ9BIB-GmZNgmE_D0I6G9EMXIRE0mdDpc5EHfOtCRhopSzFioRGEE9yVR1NLoIbXFCEuoC5aknhcgooXgfLUzMDfwD9Q8BDuav7k6zjHypYm_MCjy5v-bHBG8O6SJhTUUfM06b6qxnJvolqAVOyrWctkxKQGxV-SaA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 77.5K · <a href="https://t.me/ircfspace/2351" target="_blank">📅 10:02 · 28 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/ircfspace/2350" target="_blank">📅 09:21 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2349">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZBwGlWAR87kWLjW_tdmThpWpILDGuuEhFB4F98teqKvKgJg_Ij-10NIOOcw3_IhKnaEKsTyQ7euKUBrU1bGRwGpDrFN5_IoZbZ5LgIuJKNy-oYpYwffq-iVQYuX3tMbS-ObdJsBWnmXFhOAh3VJVYjI8NyPUxmoLw7zyBAgGK4P-eTb5AwPQpJYBF4MCh7EZThE4N7Tg-yTadT-091N3jhTjh9JwMaEDIG-P85DK_rk0L9h0ukt4AjWO9cXkenUk08K2mh_apKTOc5Aa2WSLyrS-7Vjh39yqvNnPcypHiRZ8LUpWLXH6clHbxjA9Gm0z-k58AC5sL0ZZ7INiczUl4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسعود پزشکیان بعد از ۷۹ روز قطع سراسری اینترنت در ایران، روز جهانی ارتباطات رو تبریک گفت!
🤡
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/ircfspace/2349" target="_blank">📅 21:08 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2348">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/V1vFmJapwmOWEiKHZS68Vi9ktaVb0lcrqvY8FT4Xu2-Ccr7uuA_xMIFBHGgYuLK5A4zjmnOG8aF7Zp3WrV20bkfBHP8eKT4f4byDz2E_YFyZsHwwRBiD4twJBbuEB4PS4t-GeAMTqH51n4RavRK8d2ypPw6-sqQKKCth4Jov-v4hmVQAddXvHV59R8eH4cCj91VNWZIvIaKrkVM3ePAOkcWLPRPX5-Wi7VQrALvMRjD0qLvSRgrFcSRRLb-XfavITBUJJrj7QFliTTsvlL8ox6xpDeY-HIwCSPn_Vi9JZF1WvFQSlkUd45LU_ZdzhWpY2J3yby_lxQRIz4vCVJ53HQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Tx2F2jUUhS1ICvdnytV2N4-9D8vbcUXrQ2w7U_W7dZAeGuGbnch_rnUPW3lcL4NBt44WhM9hEbc_gr3IicVUS7NSIL59cdQjy3S97lB6IVI3tRXAXlZX8gvM72zGYQEL_HjGZ-Hzt2GoKdQ7rnIG9o2HtQB7q5qjHkSEljKzyy4mmVHjng40tpG-EDlosneKm-g-yaEDI9Xg7xhfmGTasm1ZOqFfp0GFPTzMlQGWNWCueoS3rfrrBd3kcS6uMbLpMkqeMQXKT9RML1apSoKNPL71vD_Q3kG6UHicEBpveN4C8vzUZ8bEEX8-siBc33t207aS1aZzTeuSMbbXL0E3-g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/ircfspace/2345" target="_blank">📅 23:28 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2344">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EpJqWn9K8-0TxTNdKRo-Arm9iYh0jQLeM31ipSJm61xRIsPOBcFcchXrzwqmfIIEsO1YMbyndwWIDtIxaPJw47rFYklZlauj_50xuSBy-xAU-5GVIsVVgO90ip87k-AW8tAZqgHIg1m9G7FijYVPXfHGXNeHcY5ZNGOBgIn09qazFI0aVnW6sjqmf604SPRv_jt9r9zE8nVGqN9bWXnzHdFw1AAT-KMjQWJLJalAi_BJBflZrMyVhShiwpfyWtLZw5FxD72qQZimcOP2uyahc2a-osY-7n4MAXZU8beRK6kHvBheTzookOH73DwxZs5Gf3HJF78tBF6EYOdgVi2vbA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/b1gpZS9vgl9FBG-BsGfTBMTBEWFCCPd7tFOIWcSa-skLR3rAzZv5OE5PWY8R1_WVEr7OaHGuf2nUtojabsfJkkHY8q6lh-Gp2i_iZ-qZd9I6GwXn58VIFftXAxmRQy4tuAC8mitnRJ_xH2dRWGYmK3rqz5ld8zKCEFhWfvPS7qYwUuQuDgnGy06n8T1gKPENk42b-bphPIqVyw8vnhEEy3k1XfzHKg8Q-DANl4GbVumTLeUtJEY0lrircycaGCbl6LEaT0CMUsXk5nJqez9Q7JvB_wO97_TQLGmlgiUNpWB_cZyKU2IiSUOBUa6fdSgC8UoJ4OMqZfX42EcM-BKaVw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/ircfspace/2343" target="_blank">📅 09:11 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2342">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NzGqY-5rt5jL1TRkSIfL89KhtePCZeoRtZaDtohFlExOsLq3hexTGndojz2CE_MrHeJcd_waAFb3CdQ6nZh1Te-7ObyMizBxruj3mYk_3klne-vGOq2NdaDPa0bOn2NY16aqagzCjNU7ngCF_dcCVFoaXikFIj9xJDyoslVHFX9wbXx9AgXS2lBscGjtVZAyOhrPnfq2AQoek-OQmht_IJf5nWxDP34Mb4vo1nzDr9gs23HW87jeamchBBPfqZAbpZaM6MxuVCc36YQhhRwDSqkHd0NdXliHO5pAxMiuYlmTCEawRIYHTMxcHC_dpohtQv6gG5dJ9XMz9PT9c51vYw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CUlcw7NPUKz-gdepbPgQrhhylLS2d7x1HPPRy1Lm_pHlVOSC1f1V0tQLeQxhyVRWyUgpt75q1RQsmjovGqF16q7eNFuslJpJ_P2J4yK17KC7gIj446BbodVMu_iZZizIf1-bkzDquxPNm76hgBM1dCx0iYM79n-WlGf9bRrWohhqMVcUlHn4Liah6TDdQFrYXDPedUyhDWcMCcy0z6MwbVnuHY8SOZZlHyeMrIkl0hwg39aHSkUzmYNwSdFbA5hwG6x0WuEndzmck1-WQmklkPdm52X4eFiv-MIUopmQVa97e1tEk2lXKPCB7uTX5g8TlnTPoSUOfOpd4oA4IZ4Mnw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/ircfspace/2341" target="_blank">📅 08:44 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2340">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Fr_G7jhYD05PRNWy1IWhwSG2hVcSh5ZoSnhcEmc1yAv7DPHytZn5aM_9B5xh4vggyEjqTtvRKHE8PG-T13vv5Dny-gi0a6TolBUCpNtbMzn6wt_GuwrKcgyetvXu1sYYeeJEiUgU5UzXX217yqZ6cU2QGQUOxtuJJr3UbsJSJy2lLVScwDvD01VpBh7nIHUHovM8GLJb7bzPj9zt-gX_-BzVBd9n7Wrby9A63K0NAIBU3lf6qqSjPqIQ8e4Pf1DhKYpMMx7SceOfXErODuR1ctF799KmFR_JXr-9Ou4qkyE8VfVkapbjtYpvD2uxtMlSt4fNuB8RvOs0zLQcUxDhLw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qfWrH5IMgcmFftnFbmRJcXZPCJRUvGeztfzlg9n_ptBiIE3Ys3DRokiN_CS1ahRRQ7HFnrj2CFE7-VyPLJ8jY3FfoDBHpqwalTKs_RFYGKaeNyVJ83hxbUigqIcNroJh3FAIZtbZq1qDDovLu2RHqUzzL7tesUfQkLylYZRHeHWcuPT7il6lTnjBcViGLPqnd8VORrBxP8kV3M4SepoPe59b2OhfzGhn8I6D0IPaSlhv1iKdYwQyncYwsWLbelGhgeexr8oiv1Ky60I9QmVC6rgUdN-x_p6viEQ0x6eOQIVkBHqClVnyKi6-MxV3ZM8Sr-Bjzpg4zFh89A-6HNBHSg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/ircfspace/2339" target="_blank">📅 08:28 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2338">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NbMYFg3jbMv-b9j-vq9Z7Xe2V9TJXVpmR1aZpwtVBgFXa93hp74xeJWJGVP9eKJJ8NhTtKMAjcIQ8ZAzpAlITBSMxZdyolIgvupqjQ6v6qWoDZRQd9skBL-Ro9Q_c6aboIzF1wjvEzRK6Z7IK3nJ_GlRC3CoM2wMyTMT2tm-Fu-KiaQPAQNLBbwwwk0SZ-Fayu9yDwFOJhJC9ht80BTJRp7Unujot-v3zcdY_FCUQtMMN6ufPXg8-4oPldK2OxzmCfmYrYWnazZam608t7mMyqkaNzM-gcBpB6ljpRHp5_481oPPO4awnbFNMN0F8jmDbZ0_S7O8sSLriJR6Vm5Dzw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/ircfspace/2338" target="_blank">📅 08:27 · 26 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/ircfspace/2336" target="_blank">📅 08:25 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2335">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/E0SzWXsIGkMxH_zuAH5Q8VWMF0Tlz6SBkGSk8_2xk1EUQpVotr9eDbAcNZTlEakIzeaWwukW_BiTyULHtukUbf-vVQ26pnu-fTcyUlZfpglNlGPube_Tu3nAyBK3m8pm7e-8qfNzSbY5tRjZIOCymGEOIwrrzYLEYlwj96SZsHbY1D8g3Ra3tX4xyQPYMT8udvKaNK3Gzg820s2I-PQxrPdkUoLgIqo9I5C4aAkFpjgFCkhXh334rb_xXnPh4ZnWwdvwmkJ5Yruo8Zt_FfiTmnE9fXGJVs28myM1_oBo7riFE2SNCffmWGvkhTW5j5_tHYUJ76iYJgda-bGp3AhmoQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/ircfspace/2335" target="_blank">📅 16:26 · 24 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/ircfspace/2334" target="_blank">📅 16:18 · 24 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/ircfspace/2333" target="_blank">📅 09:19 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2332">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HiuE9HaJk9iDozqM3Ut1lX4SH3lr3wQLT4k4dJkyGBM5MP4-v3Wud8Q0Md9ipDsqX_ZJwwlnqYnBOr8bCX77zzRaDAK_6mvUReS90EshGCuqL_kdKH3zLLFA_PGFBsYypfVm7p7_cX2WmC4VsNzd134nOnUfmFv9EmMMHX791v53A11VZb3FA8JnQ4wJxVPE9FRsyNgpOo1LU70UoB7tQ2en4lLvl4UIuCw7nvuMDBpmwq7ISE2xOvYsG4sztAT1bB5IWve8t_yJ65MUEMUbYL_Pnys2oZNqVwEqQDuN_SLv3f0uS2mhWXI4px-bokHJ5UTDTuDX4PAYIzkrKzvkVw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/t9e1pY6GfdNFJFd3AlWS_5QPvQjA4HGVxRAK3PWBz8Ei2_Gr9wt90TWpSygY1CGF-35beVGh7-RvKdwTaiSMV_TeSOMNpzhCX6NvuRJtqU-YQhPLnjqsZOxnJFGl0Omg_WA60er_-GVMxCQdBjjQ_6BfvGXyAUuBjZ6rAgS_UaVNFUbCf-qx_ZISkGwUPbNt6hichOXBijZAaeTSUKQ6J5kedP4AWwTfYZ57ISEIIz4UbziSne8EXbPY1h5PijtuUFUjgz4-8f-9rd2gt7zT3y4ajeTb_23AMEkaKIpDc7P43S4WnO-B8oLGcXrPQaK1L7JLOnTUfISFCh9K6BXasg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/ircfspace/2331" target="_blank">📅 19:36 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2330">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Vmky1OP_hZz45Ivh1aYseDkFshaDmo9Fp3Fpde3ltwjA1c7QpqYkefyLZwE9rGLjV_JMzaXsvu_NkOEG34HE3a3cse1Y5TGOPpuF7ZJDXK1hAA4xHpSVnebb4rqAbUEo6XzeO6f62GzV312fqi1Yze2xSuXYnoCuAOLyZzemtnWj1aG9R32ud9RLyxQ6f5PfCY9ZbjCQr5elvOhZGTOlAVJzKUMHuYiGdY3-2IORUiDaY2mY6r75RZ68PCcMxt57qV87gU3IVfNmjwp1_p68sTchcckVDhQ75na2XBWNKMaGXifiAW1bsWWgnb8zqpzDlIc5i7JXxEEk5x-wmM4cqQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/d9e9b1e831.mp4?token=iWdL1sidVOY1QOsjwTcFegZ_xdydckKcgD5GO0fqc7M78mCLu6T0OPZmT4WU6_e5P5zogDr-xC7FuNFlYovt_cv6VvNQr5HBmLPGn1NqdM3d7YgyEtRUvjUpKB_UuymvnjHr992POOuz2rAF468YHn1oNkL-20Kk9J5ILg9tTgTs6-XTOdha2_sI_USDlyASmkDs9nOTjOTq7rgk2lo81l60LUycSvjC6WmKrxOx4L72oueN7L9dgOeUCX5Vro8N_vMfn2zb_Btz7ghAWbnn_R_RQ-_B9QZmPEI3b3hN5plXVHaBw_2Ri-czHkFtmhEW0ihWRasRYJL1bj_gzVSWxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d9e9b1e831.mp4?token=iWdL1sidVOY1QOsjwTcFegZ_xdydckKcgD5GO0fqc7M78mCLu6T0OPZmT4WU6_e5P5zogDr-xC7FuNFlYovt_cv6VvNQr5HBmLPGn1NqdM3d7YgyEtRUvjUpKB_UuymvnjHr992POOuz2rAF468YHn1oNkL-20Kk9J5ILg9tTgTs6-XTOdha2_sI_USDlyASmkDs9nOTjOTq7rgk2lo81l60LUycSvjC6WmKrxOx4L72oueN7L9dgOeUCX5Vro8N_vMfn2zb_Btz7ghAWbnn_R_RQ-_B9QZmPEI3b3hN5plXVHaBw_2Ri-czHkFtmhEW0ihWRasRYJL1bj_gzVSWxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/aFQ8bifHS4OfHLKrABPOU77QmdwQbRxqjRsPL0OwEA4AiwKcquBUCr_bRUDDkQx8tJSz8G7C3gHD0Y9_FJ2QVhUDNZlXiTK6fGflg3293LbF1CO0KgwqmLLh2En-pI8qo8unJh1FXKRXV-MI9osSSBcWFmKGc5hxH6kTPUHGhF9LoOxAmdNb9eXjiZ8yQcbveA65tE6VxKKkCHDdRKKWV7Q9kIEJ7QMX9I--4HP4sepl9BxnnFWPMAaBRIBuv-XMvOnjEe8BgLjgyBNUtWBfaAas6fGzagVsnPRLDao2BAqc3DzcXe1zWBHTip43TjdFmrGg6N6ffnck53OYF8OPng.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZCnVCwzWTtsY094eskBdH_bL8mJrY9UM_ql3AlVjJ6GBMDatcAsUJG1_gn4nEjwYQTKQdFGnqWYhwTgveCVPLUm3PneoEkdYGkc5BEGWHWx1n7ixFyE91dyMXGssN-IauczLTM2zxgq0e2lmRJVLYmg3sgvanZEufry5ut9nkAmkab9eq3M017xDgCmfzlA1IN7WpZd5jtuNtn4o9UgqIqNF03vbl00abUoj_iGjMTuSjZvnCnH1Ez0-O52Wuw2fcM3wwR5TlxCbgBltTJvwX2bs_k6MYrIvi3X1hAwprSJ2430QvPlEZMyiC7smXWhxFwBgwIuF3LFV_WyBqSQTdQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qVIeb8qvjoTGyGqPQHP2oCWkN_4cmWnIwbgZBKjdDwgSN203dyj7hT746kwbdUA1Yz-vLg41gllqu8K3UhAh-91yiTVgl-_MBglYTVIFlC-CFKBRS9Su3n1NI1tP_Ses_ZIdtqjqo97r2AaZKpcvaz0mEQPk_jmAN5UAX3g_OR7lF_YHV7uoXzSUke9hOYNutrLBRUbSYchbqcxbbizDv10kj_LARqU7GG0RIJl0Z0T_UvG5kdwCX56u_9HJpdukiqygP_6TOjez3rM6e0totjbjybCYnA4VT-mDHUayreOmARn-Z8keEjwkiy4_t8d66CfIONDbMYY99tZ46iRbmw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 33K · <a href="https://t.me/ircfspace/2322" target="_blank">📅 08:47 · 23 Ordibehesht 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZtzbYIX_CROiZFSDp0hJIperlkGUuMLqr6hhUCchUsVSGXi5hSH6n88CfPX4QpRV3XaQLsQ-R2NZodyzaND159Mk6g55dUMHRAn8XhDBhWnSE1F56lq-egpsLAqLW__PsaZ7XUbRr0rQcLRmrNVzVxqx4n_TaT7CahZJ_lEhhEp136LlmFe1o4004cqNXSpGgYDtz767QASco4iFunvCjUn56FDjo9Mguo_D8e-IaAPXe427qNkDEqs9DKhc3eHwjjE6zGO_XY8kvym7jLEe8-IkDxz8NjhxlsoxCX1n54URBvqiJC2JrsJFyHEA19XB6JZY7NKGEXrbisQ8PRLblw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Nbqq2qlI0WvRq0D9UDM1w6einGg1VivvE3I9_ARADbzmKsZMRm2O3e-tbaLG4XK22CYrcA9RnMqRom4c6CnuECJKYFrMiBXq54QdA8bpIkcjS4AzupvM3t3wIB-k8B-4AY7ZC84uZUT_kMZWMszMNX439XReSAt-2qJ7z1W6sN4C9RTWtSyF_JaLNOqyxCQyVK3Aie7FgfaQUDtu84Tykw4jkBS7HXydsm08vaDHDVYStVCYZOhV4-KGcu9jSEHFWibrLh3zV0DUYmUNk0arm9jUOGCJNyEF6iJ2giIxb9E185RirzAP3q639_W9YlG7A-_WpsMUW3dV7zfqLS2iDw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ahaB6_uxHX9PYs4Es2tRg0NY2Uz1qpCUdrVAihkJG6nca8wJaFDWfbVNRG8PYsFSQOqOPng4OQ_AdI8Xy-1wAZOLVCADoO0V88Ako8KEjBGvW5J2ScSu9rtti8SgzGSItfmDreGLpq3VJQdaDBEnJ5rCDklto9K-zXFsjISTZMenOoT8Fpq2yFNJzSyp_ID450C1F4azNuzDTxS-pkK0-VurXG27QXrYCecSeXUYPxSz12uuQcpfQXM3vembwTqHOYrOKBlENTVb0FjRH6XR8Vwpa01eDe_-zZsgQiCsYzTE2spUk-V8x6BuvTcr753_tfVmjW0NYnIGU3cmtlxjIA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nxmU6CylsTi-i4pV3_VlRvr9vtQknSwGN6XyIdGTIo4WnfeVDC68QW-b7Bhg994SA9FlnznMwj5UOMdVIKZ-Y6dikpYjG_5SBwUILWd65PTE6APQ_-dc00xKkKTZALPGOCSX3W_JLoUiVKG2S2KD9iSv_0FLagYHKX_gfmrT0GTQZFkH6YXKnxELI6g-j1A_c1wsKEFOKS2mZmAQl49sz5IJI39RkYBQCDVXu5Z_kd7dnDXSAkhC0u9a2kqpLWAuazd2SVGIRIL8GsuuEYXEnrBa6yDdfoEMc_96eXZ9VT09bd6GjV-aQ8W_P5qa50Lyz1rP3iHV9FVgy9O7-hp5Pg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/eRbdEB3odvQnsdKMUlFTuQ_o7Ad61VCfEwOq3VPO1lcWarJjAZ2244-Y_V7KcM7lKpvZ6Qx5C6cJACTW7PIzBpTt9rRVnoaHhgTMf8kP8s3q65Zj2O31gvjkS6idQjt6cbhz6hPdgefU0zV_wz_HP6F8ZN9fnNeKaVpQ-DzvVeUUsr18ow96zCSg6tC-1W9UjvR5hHku5xgbjqxOW3vJaYx3BK25j4hy09sKfmrVFMAHEz-UMJy8zI6Cf_tKPP8ObU7X4gG5dhNJ8pBio8Vw_tKDyQ5zEzmAa5SZ_jQdn3YvdzrAlKDe9_RHTHKHzCHZtQzMzfb_KHQLQuW2FaHBUg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kn-6Gd34chANso4flHTOUdamdKJ5kE_OAA4jvitYcNOX63A0EPdF0IFRusd6eBuzt2I_J124FLYm30psdHOkg9kJuiUHFIIaJtAPQHBXnadw7LxqI6-wEwcnZI0_gRAoPr9munj9tvzOfiyhaN7YbY8uDBgWmCaqAxCbthGRNhyrDfbV_GNq1EJWCXHiMHMxUijR29ZGomLmiKueAGlTFUVXpKziw6-QkSKEd06E1YXSUsVWcKg8hHXwiDSdAWlREuxGtuy61MnexafrVet9_vFZkuj3C-Ip5n1UNfO-HrVo1HLRZPJxPYtONm5gyD2oiDvEG9fBs9G1EG2ZHqiUCg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Pw_Khb2UbKtVi584_4nhejOEbrYnTcZ-SplVY1vxt-m1nSPp1yYthrDhFqqAqxZuJ8tA1D8TVx72lgdfmc4EGcd0XEmaS7NtXKGBQt8R0PjtYpw8HfbQug9rMGhBYXsTFEyHw8ngx8wn2Iq3LJ0NeTYIeO82RbS4mRGKfoUobzOQLlORJJktE5ITSbxiEHSLFgzlpEV0keQeAk8nsEDZBsBs7L72Fb1ePeVyapNr6HXkhMVSorH0VVMX7LA6uVn33CCtFHE6JLoxYATxUpqqzSjd89IIiJ48jWWlWIkXNPjTvk_psqj5z32-j-X4GqVP04RdroWol_P7Isg4VDiybQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/ircfspace/2312" target="_blank">📅 08:37 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2311">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/U1dYUzNRp8Xvn5d222BCEOT3t5MdjSTOMlWF2xX16w9HodTGKr6pgpDFgMlmoS5nE9b7uOPWDH6EG4Nv_ooCgjqMq-JDT1ptZ7kaGoRsldlOyASpdG_WkknN4kZROwRoMOmSg5uqvXR5P_4wXr-q-I3HOoiNvKZjJRYm-I3O3KK7jq5FlNWhGXHR-15XrA47LFseh-ejwxMYMofhye7HzKoysyQlGrmWKLeLrNfCDYq_WNThJj7YFdK5ZOeZOGBm6-iV4GbKbH9ESa6lEF6e97KrcRzw3HK50YY7ms7a5uSRar4e5Yx69k1DMVn4tAqFNA8gh3_UwMifHiwylOhfag.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ni1TeK7gDGfQQ5Hd5UFgEOTmTUfGnjuF2rPGN-aNknRDr-VE8QVH5m6z8RNBkPFiyzLxW71L2hG3A2sv8zK8Nlw0WfXfTe9QAu7cAa-PBDnL7yLQhz5RW-64lDs7ffTf5mVLhGdNFTbGux1IymTr-PHZ8fk4zdo0VcHnpFYa1hGO2d1et0dgBcW15JoX46U0KMQSHSG9rquAvEt-H7ChtYMK_I8S9V8v6BK-FoPeXjJwRamYvUdC6oyTi4-FGa29oCusY2-BMm1E-xGn02UABkz7vm3bPdD0u1mAXEvfVS8uy90J7f5gn7YTKU2-Vhqqt_9Dv-HzadQWa9shlhd2hQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JAoyMWSJPFMWZZ3EaZOznYXO_l0B-JZrGAzZurnkXNiks9aMB9140ZFR0pgCjwSD-3i8L8U24ivKEpOv87eLdenPLE1ZqcZKj_SuxD82bqZorWYdV9aaJCgRE3FcTEOfVunPcAUCFEm8AvqypGLXYG8sPUsKqZtcqdqo3MTYJOlcx7MFXzy3RlqnETjptf0QwBvqufTd92ZNZBcZYMJbh1BafSL-m7aLF0s_y_Dd-gzx5Z9z0Mzy335WGTIRIwK-JcA4hTiJ18Sa593jLHoPq1QS8lP6PzPz7OfjPzP_yUyRiPOLVDTXJGhFfppZhkDz-65fnC-XhBwOHQnlhpUHbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون رئیس‌جمهور از وزیر ارتباطات بابت هیچ و پوچ قدردانی میکنه، بعدش همون وزیر از رئیس‌جمهور قدردانی میکنه، بعدترش همین بدردنخورها دسته‌جمعی از مردم قدردانی میکنن؛ اما تهش می‌بینی ۷۳ روزه که اینترنت قطع هست!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/ircfspace/2307" target="_blank">📅 08:13 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2306">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HgxI6Wg-LR1oSWlKjUh8AbfEpu4TK50A_QWQsm_M-G_kcUlz81-gYwBknAowCOJYlh0y_RhhmajpI0kwPIM4QmI0FR83hQYOiHN0mbzBQZ5MpFJ6CyYMbBbB8qa8gCf1pgMyGLXSKsFhdW1fRz6PLmxTWOkD9q6TfElakaD0rB1pbqOjMTIw9F0z9ATivFX8hQhzTFUyPhsdHMnQZ9eQPltj_q4rfFRWJy7Fbk-CKrwN16m2n0gOrAshX5NZCzeXfRJbyZDANwHkxDeUmTIFUJOMssZyRCNDCdMQCvsXtSv9fms0aBi1dX4QW-vD05uhd8pD_Is06tuMeJz1eAlHKg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UqvC5Vy22Wp2UFEZhU0SwdFyWKP0qJC5P9cXC225WHJbv-OBMvH29bBjTavXpRBLL47fOvltobi4kycdurqydAXhSshQEmFGw611kqWNBN9pp2bqp46dVUjyXNNMrVRVNimlP7bUK-WUATv6eIlkdqW792Zj0blXQHvwtNGMWwUMi2okF22uRm5XT6tyBW-NMvBDFuKIM29I0tWepLEEP6Z3Y4qASmWhn13f58YQW5I5tG2Wolv6Tk743X-e2EpqUEuRe1VDvwgOXK3Y7Fx2vK9AzyMJv1dMHSzVnXnszkXO5ueEg6bUN75RqgjPnEZ8tllewiSCmAH01i7ys63jQw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FnNkAjykmDun7gZvrog--0Jrh2idrmdCGaFd9yCTGKPQ8c2YaLGvWsjetDHANCBnie5BsrzXnVEtWy4Zpv9vL8_6-sKU90220n2P5FMY3KbNRjEW_vd7umwi7vzX40_VVakZ1HwKjRVSBhm6u2u4_mPETCYgu8iMuavG0OiUiOH7XGu_riYCKEzsVCHUlf7cteK-_74SLMX8oUXQKDpMOiPDd0T_ePG0Taq-2FcMoTCYB5XYB6MuBnSpBNiftq-MuI_BzjRPaMK8CuMAiwm0FKT55u4WpFWyYBRyBXwgbf_I2cyG9JVBZ1oJAmUTBeFmwLa0XFPaZHrs6f4Uf8r-Cw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/J4Bd210vaPcNcaac6eugwHwctfZA6gT-Chj_KiM6dEzT-RtSRVJl2OpXPI5KESoKjnSAqXayCLHBcaUZzTiLb-u_Ld6PQL2rCQWLuqZEhFyzhq2AkWHImMOwWuRqdWq94iGHsQK69vXjnUPJ2VhitiAnwjW9tHIkzZTX0oGoUqpcYbrssv4xx7kQdd0qt2-BFvav2FW9PUZ6qGwJUoCIrW4dpi4HoCvDglktAjcGGQzfJSbsWVd0v4NV6tOkZlWJ2Y3ljQFky-oyjRL7Da33IegTllE7_tuOmX47AppXk6cEheceGDkhxrWyqmWTwOxVZ5VkfeuuLXhpVGitPu3HXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نت‌بلاکس: قطع سراسری اینترنت در ایران وارد هفتادودومین روز خود شده و هیچ نشانه‌ای از بازگشت گسترده اینترنت دیده نمی‌شود.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/ircfspace/2301" target="_blank">📅 12:07 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2300">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/p7nl76Xea0irZ86yJ4R5S9TSBpuY-EQ6molEdM355Z2cZXtM_IGMiUJLeWUPGPZga3Sb70AAwMN-lhyTWcWIwZaPyDrEZ8IRktm-UcjehF1xeqYmLgZKcKVY1_kJ3wwCLJQ3tKB2UyA03ayAm7jKkoTIx34U6BnGjVm1FqNFDOmVhFgQ4pfd7UI1bP8vEtiOQjIh7kMfWa9WiboGEIKGuee_oi4GNXpwT6UE2rG7RqG2v0pVjkEAOjfA5sI1ExyX1zpVqOlTxqaYrAP2PYZLeQdsSSu000oDs_mMby4_oeyZwIYqgVuGht9rrIZyRrFI5RegQGxEuVtmj5xXFzmtvw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/ircfspace/2300" target="_blank">📅 18:57 · 19 Ordibehesht 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UurDz4HP8RqWVkco9h3ME-EHFOVlV9BiDNDGDDn6CUvOyavMe1jX884y_Ka9p3cbxfrEN25A3Dp9l4nEMO0TG5XPmwXYPSiCrPTI48FwCe4-QAHQG6SGNCPhFgqY4UoQ28a_UMssbM7q-Mt4QQ-YvCPfu2kzigXuzrIsPIJXzGPmMqVEccCICtOkb_iaNj7bIVmNpygC7TB3q4h4UYvBQz9RbLOB19qgJuGd2G9z0JfvyZMedZ5FrJpN-3xs8jU5BWl6XGP1-hgpzM8dX8UuF6IVXTdgjrgY_qUoWesXL2ezb6q0-BtvGiPD5_8YJC0GWPvC6GgHRgJ5mNh0PfgUpw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/ircfspace/2297" target="_blank">📅 17:45 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2296">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Kq6srBCbZNpV6TX-ozZ05D0wa4A0gw1xeKzFOHdlP7G_B0DDoXC0GWCxD1XT6TJXwzDc8RcCN0J0WSLDvtAHIVS-zdYHQD_9FWp7N_kTugCK9KeansIgZirVBw1nT3CVzpHw47ZmfVywE-88zFh0zlXouL1YKZYF3urPf6N8_paYQZB4CfQ5Xt4jkpWne03Ivq2vG0W3O24w2WgQ0fvnlBz2ecBwOAsdaNWxsiyI3oEJf7nHLeQZ_fKHWoBP-0-Mdj883Gh3jUcSy7qnhEdQ-9pDRjIPjZvYsoV_-o53ZKnJaE24MBi6Mlyajw4Im0jkSn1bIOp7mcZwfsayT0s39Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IA6iW6f3J3l00Ujj1P-y4g1gHeKK5gZMUOYU3YEpajEVxk2xfGpgkQlbroYHY3869atzHlqP_zUaBLL8lclj2yg7pMBDCyTSBFAfoDnhTGe_jH8Jo6rtSEui-sge82rlxsnCfjfkcWi0jZSumSxR3ji3-cuiZnxYgIStLWwrowtKimHQd1JfDZ7249BDAheiG0-7X-G5dhyqQ8z0U-7_Z7EHffjgR1BYH3UgI5g31KCnUyROD7AyrwvUnD9I5GhK-1XFR6R31-Ry1lP4LdmYmyINScYpavleG6PoUPlgpGFopsohvUJujQF3qjLy8kmdraZAP8Z_VYnlEZDeBLRRSQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/A4G4BTgG5jImLxZ4tzBK34ApChu_9L_12d0kkLgT2MnIBZ3WikqUpbQZbRxTm79NWGBLOTNRzDdmVZz9zUNOigmlIH6uOtN29yEvMnXsNb0AhFzJAoNnIlbkOjqrbddzU0dsl83_WkKAMtUmAST_l9aLBca7iqLNBy_GddK7fCwY8jwdGSl5ZvTNXfRf8QsJ3TvMDOJ8hJzF3KVz4A0HDvYaVj_xVXUOUh_7ztVD_6kYdW7b6pw3M6HtKwTyL4YuLJy7y5odiaPGg3Q9M7w9RgvvkHyAOD0p0OZMk2eEoDsgx58vxsPgu9KGeFawIcpkD_jHK7ZGYAX4jhn29xWmWA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/luhSx1R6xOJCps3q3bliu9Cdk5dYC8NyIA8fdsj2CitTA3SpuTyL3v8QGl1iJ6p-C4m2gipMEw_12VamTlE0QBT_-4xYURVlsTKgRhnFCQzqRdcuWZCM65f7q6aX4XwWz_JuP-4b-rGCG6I90aJNshx6974cY3WU0wjgvEwLwV9fJEo3CGfda9eRV1H_DKHMPCm803Ere5y9ieV_FETmn2zGAwJiZnfiHjx7o1Kohar7algelhPPkQHppCur553hB5uhWEhjLQT6p3I-FzRyxoL4h5M9ha9zZI7IK82T0gEF212R82ju08Tr95rRyXYCUgcqgFQTkitDgehDfL_6Cg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/ircfspace/2293" target="_blank">📅 17:15 · 18 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
