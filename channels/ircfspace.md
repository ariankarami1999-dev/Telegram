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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-09 04:55:53</div>
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
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/ircfspace/2399" target="_blank">📅 10:53 · 08 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/ircfspace/2398" target="_blank">📅 10:51 · 08 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/ircfspace/2397" target="_blank">📅 19:45 · 07 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/ircfspace/2396" target="_blank">📅 19:39 · 07 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/ircfspace/2395" target="_blank">📅 08:50 · 07 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/ircfspace/2394" target="_blank">📅 08:31 · 07 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/ircfspace/2393" target="_blank">📅 08:28 · 07 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/ircfspace/2392" target="_blank">📅 08:25 · 07 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/ircfspace/2390" target="_blank">📅 21:56 · 05 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 38K · <a href="https://t.me/ircfspace/2389" target="_blank">📅 21:31 · 05 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/ircfspace/2388" target="_blank">📅 17:30 · 05 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/ircfspace/2387" target="_blank">📅 17:24 · 05 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/ircfspace/2386" target="_blank">📅 17:19 · 05 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/ircfspace/2385" target="_blank">📅 17:12 · 05 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/ircfspace/2384" target="_blank">📅 17:09 · 05 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/ircfspace/2383" target="_blank">📅 14:43 · 05 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/ircfspace/2382" target="_blank">📅 23:19 · 04 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/ircfspace/2381" target="_blank">📅 11:23 · 04 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/ircfspace/2380" target="_blank">📅 17:16 · 03 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/ircfspace/2378" target="_blank">📅 08:57 · 03 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/ircfspace/2377" target="_blank">📅 08:51 · 03 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/ircfspace/2376" target="_blank">📅 08:40 · 03 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/ircfspace/2375" target="_blank">📅 08:36 · 03 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/ircfspace/2374" target="_blank">📅 08:38 · 02 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/ircfspace/2373" target="_blank">📅 08:15 · 02 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/ircfspace/2371" target="_blank">📅 19:45 · 01 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/ircfspace/2369" target="_blank">📅 20:12 · 31 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/ircfspace/2368" target="_blank">📅 20:09 · 31 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 31K · <a href="https://t.me/ircfspace/2367" target="_blank">📅 20:04 · 31 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/ircfspace/2364" target="_blank">📅 08:31 · 31 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/ircfspace/2359" target="_blank">📅 08:59 · 29 Ordibehesht 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IPwha3AcoWuL-bl7fQPsK1ZelRBjzSlHVS0AitgJP_eTBfCuK3MmAHWC9GKHiNX4Pbg6iNvIQu9RqdmseCbje3HW8Ynj_6LuyvG90g4TcEErVv-zVStw27_icijdsgza1gJFw6k_-5kECFFCmsBfCwULGfpdeVXAp7i1M4i6dOzZ_R99dSUfnxRbFX07zBUTi6z5HrQNzReWwvNv9kzU7vh60QthUZd1dMuq0EAzSWdzOVPRTRpyJM_H8VJnGKNyim4mb5SiuU_C0cv8jxAD7NNTMbGGZsr5ueX5pT5ivGXruNxKPr-9F9EeYBqOP7ZgcwOotNWvcCdmV_qquSk_9Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Vj7yRcbQ9rcnLpbP0OiPTt2dC3E1OedgNUS8GMuZaBF2SLR9kR72Ef_oGU4x9W3fP7kcli2Ks1qN-g119lde1wPuCnE-yFLZ2ix8bWPFVJOAerXA3S38QED3hR_Z26ljGPkJANCGhNk6FVxyh4_ZGjUeiIGMtQ0bqw2BXkqvV6wuHeCvRCrcNMmOGvk2eYzaV0CDR8FFoUl6jFfmYmpbLU1vv0ul5G3J5nDuJQl4sD1kRLUF4po_w4Qcr_tGBr-smPD_jSgaRrud8DFohxijzA12A_tNSbvjcf1aHt_cL6N1rsdtxbNFOW2_MZzM7nyDqJJ0qLP7DhdwIwhDBIzDrw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/s1jefZ9Qiv83h8l-KiQom8Us3k-9YRV7Dll4163YIMxACjPRhR9eYKq6hC-NUv-dBysxcnTbCQsxTnQYJjBnScX0BERQnnBUgsTDqUBDJV7_Wfg_MIyDZH6y93Dx9xyCUzwDBaUUjpXc970Ywohv1xBbn2FHnio40b-45c4B5d-zrGh3QsIUOWZBJ6xLQ6PDMNAZdsNDqrJkm8Egty-Iii0kPfMySqz0yXxqcPL97Vg1awtTAstlWoD71FnsBbP88kHnRoL_w4ZA50p61DLGFRbTPO5u9nUAaIF3sPqmCrZlFTx3qlZxmoDYeOtOXuXJBU0LJuI1-rfCWRa-VwtZ8w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Icke4gt-RS-EMTInqhdi7xvw4cK_KUAWTNj44OJnOQk0CCG32Yod7Ne8Q156gtlrvzoFZR9nEWxE6ukxvbv4UMV88-7vFV58fpDQzEleNQQK_xc2EeQeCAplHVbGk9Mcy_27Xp5EXe7mKXwECl3CGRRfN2d-GB_YGpNqPhh_KFv7bI2ZB_1cpg_n4pgdwcINQrdQvjxSwiMDhB7gbXruoJoSy0eyP5HT1A1t4RocPnUPZbgO7t7pBoIPdNg5hivsqQSPdY0Bn8LGnsTJ8MWH816VcgsXjquHdCTmxrjhm_l2F2or1Bz182E7aPNIShwXVPQV_9MmsmaMyxxFD80RWw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kcs1OzUsrJPgPnxACqSINCDEbYFj5r515lkp5d0iK2FMV7xbxEVWGPgsQV92RawLj9rqSKn5BYx3_q2JxmemW5qO1tMKAwf-6aahAxqQhQLahpy6sMibmNiyqeI81wgjvdC6Ske3mII06S8eAmaqXyJN2P6AMVisHLswDZa6M1ZuxHMjFugzHYNCNb4JKSZuY9kt0kgUhfxLKUhVrTrv3TL5NqdYIbrflEn11dD10TomhW0TB52RWvT8fbhO_57xv3uN4Zsp7Sex43vcU2FRC2JDv4ARnDF8Zmdz9P_iMI1xkEZv0_Ps0W8I6mxyuTNZU2QTkZ0jeizl-6ofKkmUnw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 77.7K · <a href="https://t.me/ircfspace/2351" target="_blank">📅 10:02 · 28 Ordibehesht 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nEfrxnDBwl4xsXVbrymfvULDFRHQLTbxuAm0IP4uujKzH1NbuzRX-ByCV9VAAPcGEg95eUk6GTn3AMS0wxMzxHYhM26LBq0Xc1aVRFyFGSDyBTsQ_CvRQLj8WGF_JbmLhoa0q2wctG2KT2E2UzYUAz7n1sW0ZZo6OxaZu7hBiz32aClGT4jf28t-yg9-xwnlfzRik6y78LJ89SeM4cseT7aHclMu_MmNVxJAOOSuMxD1W8vXP8n7ENxI7XQ576hWJGdZRAuIhNuQKepozI9mC-R3vQhx26bwZDXqP0BAsJWxSlszHjQLMcY0NcYCExS1yiyBDzYQ9-Kze7bxyhodUQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vfAAmeNhQ5AMr8wJbPRgC7STTdgf9taW_zxjcR-awys-d6cilK9iHsLrnrgwJnaJfyFPebzsSy2r_RWKdib3vvJwmF03Wre0wGajszNFPmewqnhBrJSiX5GeXe6zhhf694ENEPIrq5lxReZ-VInmtRHScfHONB9pm828ry0cL7AjgsbJOoW6f7DNkqKnTgRwQfBXOtXGl5QV9RUzNA7atNQwwmuxL_10kck0eTXKJ-CvaUm0p0wUfWlIEWlT0L7B27dQZK9VdsDC2if4j1xSVPDN3Sirq4KuXNdItePg7zVJYqyiW0Ls832pCYEexXYwJKD0MeiLFmWGRCwin6kzNg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/ircfspace/2348" target="_blank">📅 08:49 · 27 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/ircfspace/2347" target="_blank">📅 08:31 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2346">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PDFtoWyVyYW_AIPf-Eumps8FU-NSrB-wxhodvOlKwNrjGI0gIm4jmh1tCL08Nqa-hsdQTj0lAP1zIsdQG5CmAkNK2OzfxBPRSM-DsmfJVP-LRBknr47wORdhZ34ruQt46maMz5Nk_4IN75jOMazMtLu8ICxn5082AOEo4wftR0_6xsbsmhY8FM8IzQOfAnBRxb-jiep9pk4lnRnCdSbxGwV1j9Z9a40aeK9tOT1Xhk3Nr_6k49UDaPq2wkq4piW4hRwQo_m5UgVgycsgafThqisu8yvv_4C4wwcibYMzRF1EJCbJA_UpI7LGKmFryuwELNpFsgtMfWlLF0VHLBJ2Bw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/ircfspace/2346" target="_blank">📅 23:40 · 26 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/ircfspace/2345" target="_blank">📅 23:28 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2344">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Ew2XgGwn00G5sWeLRprW_9Z4juIAVt3LoTAve1LanLWlOlXDV0uE1XZktckSpJXH3e3Dvd4KpcIUVc4SKVSe98MVRTLTry3op1K-FeIoU_Yhz6xitPytOMn2Th1kNTViwXyeveSbJKck4RQvycBVlTrALeyhS_RzxzaeguudborbNxW_FU622kZD4PIlrxZ1yBen_-BEPG6IQBTu6b2fGz77ij-vb5KzQCTrpwxiI1Dmv3lHasxWkQq0L4JSYmW2K8v_z3E0bN4mt5lFsst_GFyP_1R4lk4srqwtabE_9uB1Re26At0vmOS2yz_F94L3AOsHX0klOIMh7U_JwuCgOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رفتن هرچی که تهش Hub داشته فیلتر کردن؛ حتی گیت‌هاب.
قوه عاقله‌س دیگه!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/ircfspace/2344" target="_blank">📅 09:21 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2343">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Ol0Q8KpGFeLIvQbc2n9AbzMj-qumZV3gSaCGhYSj-fJZf257cVQC0spxcG_LbbXTGuTWJUVPwe2eqnKheVFLW9RCtbV5gaXafbeGt-8FUBpczcNfCWhKmcNqayuk_LhFUh_l_51xZ9NHZAY7sI7Sp_ZvlsTiDqL03t9sx0gRxtuAfUgNCkbrPsIAvcbDT4IeNbwC0ABmJGwi8ug8DLkNrW_BO3t55rBF3AnV1mcewjMjikyEf8pVZMWv4TYRArllz9od0cffUGO8-rE7It9eK-h1mfBPXCutxWUrIrXNW1YJhu476ljQxqIL54htaqmd9JghzaHsRGj1qQqtepObcw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GebOJd6Uu1wlwDdXx_6DQDOinIlm84jTGO4R-XCMJHh52EnxPKsKTcEHyalQs21A5SnjtlHxKXSxL2YrLMx5ABM8ci-pQJq9-KdVQTmQA67yL-icpn1Is06cv-Fm0BIOd3wojm77v5r5C1YfnBx27dbWXv6gLWcmxvPRWvIaTmR6ol48kOxNiJOTLW0rLzFN4svGMejir5hc44GlJgw2jPyw6SS9qps6jqXSDKkLc3LWomyxnPOm97u7W7CE0kOtoY4aL-hH-bBCGsqIqBC_bknZaqaCUN_rBAEAR4pfP-eb_QofP_BcleCfaIwGzEyzk-5LZhNcWjnsAbn1w0YLtQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/X6QcQVNg_XsCSzN5Ag6GzuO7UdvZq6tarEYAqmGaZcqNG3Ef4ivlUqJT34bcEjo4wUtUCl9QmEgDxJNGHqLN6d5JRBSizxWs_AHixlkIBaQ3YUF6_zq0oH3sTWvXhPGhaW212xjcntqT6W_npG9iCxLVww-iCSov_SCnPMuJ1liif1Lo6VxiWJ3tBDk7IayIkManRCFdUGHPV31HgV7kEyPiqOv06Uq6NN8e_LtD9dHGdCQAnGxcN9eNdMyFXfjFks1lUNf53Tk1SzxtbX5Y7X2iebSrQXgKy4V-6E_RqLd_99owtF_0IMclqhabWuhZLBeCo9hz5GT_YowRXmliKQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/H1M8KoU1_43vSh_nMAivG2BDSjJF45fi37LYUHOQYpHDhqSvvrwxUFatVZCi8AdpPGEjYBrSI0WOhh3SxHMUKLOoOR9-Wgec6T1YkA7IpNeITaoIqMZXV2xoDr1U44PpPvK2fMpulqDvl3sV_NtxHH0U8n4mIzOlFi5SONNQU4SUHXLsaW_dwbFcuVh9ck8-wuhWQKPfQr18Pftw7Fl0_2c8TIhlC78hoWV3fHtst1NIrcE4lP8cwQ7DYkp6_6zK9Z7ENJFMOsyVDtjGs4-DS44cd1OSRDdv0CXgXL5TIu3xxu_WeA0cRPh9mapMhXzjRuyPWmDrzKGHO15fVWbSeQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IiT-vOdizpFHGROkD2eVXR2xGwqh94mgTK79ozd--kLn-0rVXve_36HnjrqvSXkSWgrdKrq6kFlli4Io5KbTgueyt9LuCkwAfI10raV1rScIpE64aP6XGmyGATtoF2-wEqXUtcU1ueozvv9BfstRrUO-94AJfu6jasJJgYh-BvG0Edr9NliE9ghk9Dlzp4MRZP2ya7a0piClJ9kPmLi8kaRYQyb27CVAJ3JupOBF3U48q5SL0QBgbx1H8oxGTTso89Gyi63Vb5F7uAyjmKU1bmvphzcO9fYoYuJ4l9PvkAHPpLAVv1iNfY4HH0iGoqpCImXtMkqFMlHnybJtfxtFEA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KpYCtMtnvcpZKQMA6qAC9oTFFYU_djTRVcR06q5Nh685FtT2ZqFmyUNGPUifqfewdRCaFOApaGIUTfalkCxBkQnrZ-asqRS4SeVDy2w_9TpLTgqu3ciQaMdWHGPg60hZsf8NBD3weEhNEkmU5yPltAdAOVlqLrVTEVADpVy0P-hupc2vNXXKa7oCnaT5rgnAdjs6zmVsZ-pidgvQRc8QTX_IQ2WAnXqcv7uVb25LRWUfaO49cqQ3UkHcsUBqMTCAWCub156_EUvBe88tYJfB8QTmd_cKOUiZJ9Dc4DE5fMjZ2zmuUBW0rz8dRoRQzkvxgqcWlax8EiG2Qku0MB8NOg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/oRh6moJFZ__Ala9Lh0oz6UCsLW10YA6II8ZDRY_KcBwLdrp469gAoZXM7ENB49MJCyPQ9wWNlftRwJnpluzYUy2CU9tuPu_wIs6FbUk8Dsv_rEXxvSNuVQhWEDUgn4XQNCvfc9tD_xxLu-1ECoLgSpCtNBHuxRX1nR3Nuh43WT01dLXiHV7X2ut_jAJwM8mIKFCMKpEgsZhalSyYMxW4YJ3VNENUMiMHlmK79SQcfONSJeQf3DlZwyeZ6he-ehbz1GPttbV51gmqSCLOnn4mc_TxIZgDJ5Z23MEcaVJGD7T-SgylkByYGMG1VJSxUSrqgzX1GRVaDSbTEbO9IgCZHQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/ircfspace/2335" target="_blank">📅 16:26 · 24 Ordibehesht 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/foKDskJ6rzJSgrtIia-evtuxW_uaJU_Y8hc21lgF-6FBOQnd08x7a0CUg8HrXkbMtA8rlF-_1XHHQnfJBEzAiU6Wc9UIobB42tiB4kUrYv0Sv0cTqYfFy8dvqIZkuEtYXtMlhLKtgdHwgqe_m_eoBiVWUp2B7d21HpoHZvSzyPyQqoXCsPrN-QyoL_6xw5ZzsNDaIB5cptqRSsVKBIgEqtbvjx_QHPB8zGd3WRkLMEfoNvQSRBs_lYH19RfhzdYq7fIX6bacKGpbiL0CvTReSjuComD_WFHZ6hQhlqmAXvF3hp0PGVBWx_NaNbg52sPMcq8lzZBioNVqOoE-5twqjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی کمیسیون فرهنگی مجلس: امروز پیامرسان‌های داخلی گوی رقابت را از پیامرسان‌های خارجی گرفتند.
🤡
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/ircfspace/2332" target="_blank">📅 19:39 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2331">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/T_eb2W7Y8AQcIUnvMHtvZ5YehFoQWSflrBWrg7TCpfzmH-5cHDxm-vMwgE9yQoCIMP8EmElTX8U6GXiSMGFN7ru5wJWX2Fso97uDIoxWixyuXldBGjt6vB6DEzrov5wy5F4C58JZV1U06JXrpN5JjF1L_MWQJqfG6MJdt-u-XQSnXwJyF_PQ9-Yff3MVkpPbAn-tPIhLtZIR80guRUwv3SdZ7mjQCkknz2IVQ3fPtmRakvFOE0np7BoqE7oiT1QkSElAeQVgcmJQqs7CUXJPYW48EUVVTKpsXc2jyu-ROkFxVP_j8Hi2HqJjqGZy_gO4tzwhudt_qA7BIo9XhmeHLQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/R7Aqw4_SPtr2ucX2zRblRCE_CE27Fad97hYixoGBcQn3mvMebOxTgqmSvtIl6lZPw48QYa6YexvOot7XsjsWYvRkqxZVfx08fkYGHHQmN-_whEk4iS3qWNH7xBUK7Cuf2Enzq9hdnv-5mXeL2B7dtsSnj5QakCxh33lHBlUBSl5qIqcmRoSuAB64ZQt0uojTsxQW7_e9STMI5BllKdUxKoJGQrA_3ipqOmf0XtlmGWero9dStWQhUx0M12YZlU2mw0UXqA70HYWuTDcB65SKQc7yWBM5M2DHQSs1tlAzDFqsXIdHZPkKFAe27ls2v64-WbO_rsGeWi6tC6Daw06MYw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/ircfspace/2328" target="_blank">📅 19:27 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2327">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d9e9b1e831.mp4?token=alRvKNZQ1DHstDl1Zf7Fh2p_afvV1lUw5QAZE7qNrf_JwvdMMGdqcQWRRR8xT9kSIBON4kAPOuXeFRrBxNCo493BvuicJ3Be9eW8Bw_yCdcm5G5Oz04RF-_2EVJSgc1SvTHHyBtdRDIeqbutzF_e_tYBWqC0eH4lJJ5ROWlgwdlW2HVhw4pV1HYdgftgRkUEGL75mYQCGmLxgAScyk5kKOWEZ57e9PiJ6yCIGdGWnfJxgAjJPJc8se1poQ-bu_pwlH6_dsW0N6mB4f_-iYdAjlthiVY0ahI_-A9wY-PcaAxJA6rCjFP1y51QkYJeVliVIpoGCWez34zqYx2kLNO0Bw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d9e9b1e831.mp4?token=alRvKNZQ1DHstDl1Zf7Fh2p_afvV1lUw5QAZE7qNrf_JwvdMMGdqcQWRRR8xT9kSIBON4kAPOuXeFRrBxNCo493BvuicJ3Be9eW8Bw_yCdcm5G5Oz04RF-_2EVJSgc1SvTHHyBtdRDIeqbutzF_e_tYBWqC0eH4lJJ5ROWlgwdlW2HVhw4pV1HYdgftgRkUEGL75mYQCGmLxgAScyk5kKOWEZ57e9PiJ6yCIGdGWnfJxgAjJPJc8se1poQ-bu_pwlH6_dsW0N6mB4f_-iYdAjlthiVY0ahI_-A9wY-PcaAxJA6rCjFP1y51QkYJeVliVIpoGCWez34zqYx2kLNO0Bw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/ircfspace/2327" target="_blank">📅 19:25 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2326">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/piQSslUfmP3QjW2gPUCbfC3b73gS6tlALKqErgsPz0Sf4QHb5TLg4aaVWllKXNl_VZBJm7LgLQXbeFRcKJzi-M7OrT8qmzD8k12nfPxWoMezJ1_SB968XLypRzOe3NtjPkw3dYcgLt5lv6bEIibBVsyJYebAXqMbxt2FMSvJoJfl_5BSN5tWQRgLFvxGQFwW-deQySf8h1jRssJy4W7S98xOM36rSYAJU64UcnMyhH6RCsHH_PRSmtEFy1unTy0BVUsQBS9wvRe5s0Jt3LLQd6zrzHy7L8XTNWG7e8MJaupI3gU7YI5d1F8jfJ7CvCBo65q5l4MPUEB7Aq3bwiAvnQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/efrRW94C5YJPB1EobZYqV-8Dqghsy3PYNzCnnO6MGE6c4gdU2MoM3v2O-Y1HnTMXE9Evcs6i0reSSavEifN6bhbYw78dmWx9JAOZ6eKnHvKRjYg-FllhftVBm0880oY649OFSmv7nnJNPaM5bLMgqFGHOoKOWaUYZ3Az3xoLTZFTK3cgelNMJeqjxvG5InkXcPZ0zmpgLLk3lITIEYw96dml2mHIHyoHAXlbh5haE_QFd8CBAVNlcV-RRF07B6vrAlZB1qULx_TQKsFzyvyY57XEFyrFwoO-oInaa5BClLjEa1XNFfjPwSZ8J_4Ep7pXZWMNvqFXIqJMqBZGY02wzQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/ircfspace/2323" target="_blank">📅 08:55 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2322">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SDiZcycjaf6sscjAtN6Yh0BltFUwNI1olxVVKlLcaIgbP1g15fLsQAjFI_ZBkLNKU0LPqOXSn7l5M4F_KgTffvvWHFtqKNZg_6-iG8aj7hotHdwlHPgGPt2mnmQbTxXcE2JzQvgZidWNoXsAJGF8KI2j4ZafC1keFkrg84s0-rFiaoZniAhnJrYWQIL4mX7tkQKzr36VhszD67818xmQq4r8nnIiJ7zzTNwOKdVBa2L7hbQY7CdHycNpS59zSz_-Qfh5IJVct_7VLX3W1n5cjdXZVqDQdzQMnC96KrVfy08TZtzsjocYTRUVPc0Nxs3oWNATn7BYkNpHEz7KzbHKEw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rq_9GPjjIwrbKwwEgQRre4oNOXCIZXIx-cYx-wxe4fCvukpLaYls2ISBk2u7jUStyw_2efi1FoqdlUBQSEqPJNjSMUOdVJkj0uJzQkEXqzQ_W3l81KQ-FtB8hdus5dUm0RmkzFL5WH3HLWTmbTmpnbTbu9G1iEy4w926aJXYXMPNhmjd1DzoMS-Je7F61C9H7q6acDcO3wsf_exU3qNSYVxzp4ldHvOZfXmCtnrS7AfH4SDMeDkzZzYQNgcO-LNI2mTmxHFtJfUrZDssw4Hjob8MTePom2vhQDvDEvQmq1OP1htuuyflNp4HzoPYdG20VO_D79RSq-UNziakUEvIdQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RVYo5sXAI1LS2yONOuLxFl0qRqZAEw8nO3qFVQa9GCEl-Ljn6KfDy0UqPv_v4qPZ9SewVAbiVluSu4HgOfJbG7u9DSBscKy-piDioL9Q8nQMxrjkvObxwnZY91Mj6splh67uJOr8gHi9GjQjrWPdoESXDf61fqKhm7B5Wiimh2uWDI_mzoxd4bgLpMGhmtlg3LNhBYPzcDFrYseJTXV9MhCBeFq8jYseDp5VoemEMUWwE4f_FVZFo9kxY8HM85guTZurRYGmik-lNzGU3q-XebJgqSQZVSu_P3r0XDDHFebdJFmjcgw8Vd44XCTaNiy5DPph-4DCKpH-sUOry7k31g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/M6zxBkv4dP12GS_lr4EaZceC9EOAvqiG7TzU4RegL8yor6_6t7WqzPBwBrCcrcXZtAnDxdySj8eDUC1ZmJZ1ow-azUF-Fpaj-i_q2HtPb0vpegmsOn2vNDoeT4tPigs8scfDgqDjfr8LDTutPVB1xVQvawXe8NYdtty5zGos_4csG0JJ_NtsQ8aJarWcXPutB5-5rD9cx5DRBP2C-PYWBa5sb_69gYcoOmo1aSg2rq2udHtKf0u4yViqtRx5ImEm9IIC7WdWnQoaIgLDdgYVj5rtKYRjV94c4uOWNXyjy4rkejt9nkadk0cmZTKXq61I8aJsQP9SVKPLOPMnekfv2A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/ircfspace/2318" target="_blank">📅 16:35 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2316">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AhNbdX6NLUFkU8nQEVhypXi37FhlxqpQDoom4UTJOiJgpbYaMxC9qEDYlruYBaCGjmWUdM7gPK9uI3kaLMGk6b4EkSzZ10oeDf_SPeJvEQIsTaa4aA8uYM-bWV8hAeQpUpEkph5FFBUWN8-pbhwwzEa7XND_GMQ-eS1csdm8kaZJxPTGA__eWOR4q4VilgBJQxww07oTUiUupCSsAotiuh5FaI0vK-ZtRv2g8ufz7PfoZg1qLqFjYTVM4DqNntFz1PVNcEmZxfrXzUoWzy9K5PsqFvfwv46iQCRRFg-Up3YDOVVY0GGvq9f4pt-l_EBhdk78gvOz2Ybi0sGxYES1iA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/ircfspace/2316" target="_blank">📅 10:26 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2315">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AaGPWkuhCnfmeccL5aIvIYt_GKWBS9tG3iYUajTyMbmHxGEozTc7nsxfv_lEwoDoBxuA5_GOtYAWAMo3mveEu7miYHsP3LerEgcs5B1E3XacrsegvxxPCxJiqpL6fDrCxVvyN93aAJeis3WYWYA9nN-YZkEKQp2o5cylnuzKoPRJe_6d_3B0LkE2EpIQqf7a1dPAE4v5VWvQkhyfO7o01ZQVBhGPw9G4fWrHhDacb3cXR1o_94UJyl5u8rLqSFej1GhvA0yZ6aUisioxwmAlz2vyp87UoEPTa58u-dLEzfHjdlDJrM0VtnDZ6HAUzJnSIRQs7c10ZZZHufMXqesasQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BuBpJCdHG0SN3WUe8E6r1QRUq0mEiaQk_Tv9v6FLi4lPiXTS00KpQrgdJo7a7Ht19nvmHlYZD5TISCel6JHWuIyA-41OIRyrijR0bz8mQ_DaPxcZrUn5ExTLR9nC-U7QyjR7nXPy7OFiJ5AMQgRYnULgz70VIq944XRfGHh8C042T4ThZCQoUTUgG67l9idXsApkrxmuoEBgVXX5G2UUZR-VeoS1pqpBhP2fSpobZMQCNHEOibDGbvzmW1uViBYI4RMR25SBNtgKwWPwNSXwISOy0Das3VoP7XKnRrpv8ZQghKXEUFJb4XgpA9hSNc6XPtMDDA87m3YuDt9c2UEo9A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/u75j-m-2-k7vQ2FD-mlCRzVgRmn-sISMRdIl3vt5dv_K4HBuSqchGUt1s-mFdq--zKYLS6gK489s0C_H3priHMwFMypTfv6E5YYQfmb-UXmOmVW8gFsv41IIgrcxdtbOxfvFY-wnXdFfEE4Lm4OW2JLdlcAsELdVa2Enf0yutqev97M55cx5V3yZrOlI193IqXfEp6No9qj2pToUEQavjKkseeVWvxLGb7a9uVWkLRT7gxzwoo7wi4mp8SO-nb1hEAz3FIX7GPtIQ75oxWBZtVllLwDmLg1mn5--XwnX87y880qr-xu7EK6l1vcPOp5io-EZ8gMyFCQBVKOsrsrCew.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dtDb-U62HoQmrHcQgMyf2z1KtyVAl4Uxg9MjtSP5CKbEFiDYpCwRgGb2BeJS2sLjn5Ey0Rd1s7Og3QiqIjTOBu52QP7FAdKLYQornzyurgVao-NN0YSkuGGmOGjEVfo7OuGjyuITJ1VXJcsGZvm8PGu64ZJDSTHxWLkoedz57wafo59gLZOwTUKBoZ14zCbiwryWKc-7SAV68flkeMCIcKJBteWZCGaYTWot2625bSpGNjsv0TAWz2_FYyNOxY4e4VkVKr0fOm6iTIbveALNf6KnjrxzMWsQFYoW-5eahUPNXcBMCZTlrTP3kU4127ADL-9LD0w3QnGod4trTW0HFg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Wdpxn06LHHHLwqXE48ywwXjBZgZgssqY_CVXIrn80Zv1Bgci0hO3Z8YfuXAwkxeT5hiBftEoT28y1TA19atQtYrJMQcnjODiglzvN9Cny9ChJOPQYLjIy9d2qFmrXGODYdBmVRNnICuzlT-4EBh1ngtPtljtBXvThzpfOIX-ekcmdRH7pOmu5htnAYNf_BaUR3blGWA-OylfuBgQ4E2jzA3RPs_O6NWTiV2XKLfb2DhwuiOHl4F1Q1FXn_b_4mwbAUZ538Ayj9SRarZ7iKNZrEKXlN-bdufKMoxXGD3TwrdmwPCAw6UUTnlRh0r0PLe-KYaZRtvQosvIhJHvxmVm9w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vJPhOZBkEcI6dTwxZ6FyrtXejTNLsHIAu0wmBqG99vctcsqEAgbu4WZx-Qb50s4iF-HMNTXYmZ7QFAh3_OZIKraRzXzwpuZ9uB6_lPS7BSSAqosjKkaxRtgn9WPIyJur3jAt5CCMwC8uwli_fT5p0ovb-yPMYMkPkEFqLkEg2emeI0wkaDKV_CaG9Sa7LVGo4BzAzW4aQeEdAYw3pD_eaNqXhj-_6uEzW8Or9dw4tRom1ORibcExWcrfNNMjcv19HgRb0fiiZFd1m5i6iVHjRlCgLzuI8L7NQ0XQ48B2APAPAcZv7m_EXIut_JZ3pXNSrNLW9gGNNA1H7GR6rRZ7Fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون رئیس‌جمهور از وزیر ارتباطات بابت هیچ و پوچ قدردانی میکنه، بعدش همون وزیر از رئیس‌جمهور قدردانی میکنه، بعدترش همین بدردنخورها دسته‌جمعی از مردم قدردانی میکنن؛ اما تهش می‌بینی ۷۳ روزه که اینترنت قطع هست!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/ircfspace/2307" target="_blank">📅 08:13 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2306">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FYelvJICtyiGb9kLerqMPQVxeq4ptPPkcg6LtRHq9aJmPY0KJ9pI78RC9ZByYO15NFd_PqmkxLpwJJjw45XSFKf6PL4hA9zdtAEfJRab7qi2B0xBlnL0yglk4F4jgUyukkgR1eAm3CuiYRe0z65G77QJ6wdX8Dqoe_UfpvvPFe0YWX-j3YYEhHMNFB_UNW0_Cyj6C1PwzxziETTAuKQewUvR9LMwYeMCskIw_2Y427Tcj5SQpVvauAheRPsUfHZz0Tr56NZlfQ-5CadyzPpMgTciYKNzfAbAxtCJG-r-mK-Ut_fKbtQGZAxQmDlYCxLJOQ6-OTUPW84KSyg1uQGOnQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ej5xscw_SBT2HmmIYlfDa10zSdKrDKmziVxDKr-rw8_I0BIw12XjCenU0rHcL5qSsBd046MSdgyKRZ9l6NFIREAz0PdJ4ggI65l6ecildYBdZkjjVxrpnXxhePCWL574otbt5lZHhnNh2dD4soeHeCBzmmfH_o_NSK6KLDzh-UsCrVx09_cFYJVys0MhDQahAhRtQAWX1NvKWLB0l8Yrmcon3I0Y5wLwk-FhZoy4MeQ0NhglTv50o4LnfiFcP8grF_IdqDVKVzDz0xFI0HXHLOaY5qHt9zN8I4v9hzqbvazlRBVUU6qVqN6eRK10R3588iWKG5qtsuFI1_XN2S1xcQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CMnMOfoDkupXbY3hHUZNPnEgfdhFDFRXXqSg7Axb9EugwUQLZ1-zRGXRSGGhTpmuGiY2t8a6EGH_8DKkK3j0rGtTL36uywXCtIOp0mAvtF9WVbcxadLPMR745myZMCKdrJEH7RyyQZZNWqc0KUqesMMcG8SpTPetL_-vE7DqAfVFBjHEBdm0sjSArCgjTQVP3NA_PfrxKmCtbyJ5owS2walSTzvhMu_HIUN98gSf3cJUzXf9o0-_u4_00jM7aiu1lZnkBLJd_KsmanJyZYMbFk2LW7b3Q_CCLGgthj9dT-kDvPETI7U5UftfFvKMV--Y-NS6Xty_8aBp6DHokQqCrA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uZlmlKdrze2jJhALBvKTUlQ6EiK3FlbydAzprbw466Gn4JuwoYsmzkpY8AwdqWppuCsk6TvAE2DNHZMXlpRe-ZzE0Abb-hltakls7tH4f530VmvaSOGB5vj5FzlGBDiZ5ynCi2rnMSkCRHts0opzrLxJet25sVTcSXQQyt0-APepTmAJrl-rpY_Qau3dIWTpU2YegRv8RaiVZGzAC_sXBCawvo-caEwCx8HS2ErTv0LjFtfign4zzIFAM3w8vycfhiK0FZjMsMpvg0Ep2U-VKg5QfWQyftlgm1zO3sUp4azwuzQd_yUD05DgeTunxW7HsTFtHeaBmSOV0M1TB9ww-w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SfhHE9n8wY0t9pfhUW4HY9ZTUbZxUFgpRCD8clGK04dPkjmOkoS_f7BYV96vO2JckbLkUlNexRqHs6up2vQUstZB20BxynJCQzFZgO2GUyBCklPq58AARXMFU6OhfIsexm97kDcHL5cacNhSsMQdtbg8CY9TAY1G4bqAMBlb-S9J5YnKErnymfP1sJOHraZ6of7-zo9Zr6LKduV-tfRIWU9tR8nibuK7FHDpCW71z6DXbM3e8rnuEw1a6ObcKyt_D4XQWOHN9cdYniu0aNCsb0lgJ0tW4smnL_SbR__mIVVZfxHGpfszGNJaeuKYH--lLoeTauziv5IUGrACuSffaQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/it1HL-UWZBh3W6O-w3G9KSho0UgWAAkAsVFeODJfiZUBhbXB6M7LZrwKveSJx6z49rUVKQzA0MePqMqkk1lHUILwoOsi-PlvseeAGtNm7G0zmGvJzRYaOqYdjmRDCuBa10IdvW8X2jeLxvQYpaaq5BOdxyrIQrapNtnDEn_QZ7lrZGQ-jCu3NuTRvwEYE2Q9e54iIWZFpDyMCmQ58jSDq-syc3GtrJrGf8xRSoTZArNt_jrJ6OGV3hc21FmGgNepGVxgeh1hk-qMkIquvefuQg02ctQ0-E3DCJVby1gHwGIiZI91XJkmykCY-YVOlkleYna2VluMBtQDpPQkVdOP6A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/o35-XVglmsAxDTwrbeIhzXioPx67lDzGV1guU78vnSileKgq9pyC7varmJqXlxGwQqdURr8zumpysdXJyROob7i8N-MWIEhdNGA12_K45E9LnuLZyXNVAqk-i3pJSsVBSfALfJtJc_2dCVxLynb1JFCN_k6HrHRbMslOWEe4f5IXwj7RYtL0-HbAorQEu2ENPaVfyUXG-Z_K5sUZ1aXLN_C10WO9ygE9nR9gPr9ekVWvN4WR_xTTm_gwG9nVwD4JX5761e0MiAoMjqPKQeYc8v9-eAa_ccSB8o4f2HTjcIKYpMhTvd0HRcEhMulPYJFlrck_pa8llqHHKg42cnTvKQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BLG492R8J0i7uFwZAPRvqEj-D7Q3dr0DbYO8MRJ6g15GcGllNhQ9lmF_7M83sXCZIdzJGTeVDaSiaCXjaWauscluppeRJpJhawBp7XJCoTmvhoTMf1PiVLKGmnC74lM1869tX1_WENzj4dYSXRACqiPjGH21MEb5pRHvjWvunfA8aUTWjObaWro2RREN0WNsOasw63lsey1ne56d0jLNlyD1VXRUeqfSXrEp5PNbDbLjHvOCsHRA60VyDAsFBfNiDqOKx8BQAeK5Hexp1F87mqifA6EZ-L_PNtpMpPhJUjxfVDkc9r0oSYFHAjHTEfL0t5ZKce4ctuOC4BzvAdNVjA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/ircfspace/2295" target="_blank">📅 17:36 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2294">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ltwSGpqPRIAMPOS3HHCdXHmpz4CNlqG2p2x9_mVAEgzZtP2gvoZDZ9dpoW93DHswsligs6n5znf5z_I-Lubt5H3O1WYMsrScg_ZYXa7TGZaLc-Cje6vUCzzTSDIZE6Gy43Pp1gF-gBTp5jOmq1OWQpd9d1atwjj44nt0nv2LGgTuw7fkOGXZT6G7DcbLugI3rCHpb-TGbsWq8zRVMVda6XUluDgUFiulljQr5PeK1ALYf6Ri-PaPQXCrR9wdgNZ8MRXPF8ju4SbBHgsr_Zlo9Tgpga18Yn4wwtkdyQCBD23i7PfcAJRfmkHmft663FajsY0LJ11sbRWWX5Ly5zxDkg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HIe5_6EV5nhTEu8GSNxc6pCDcHRlrzAzdFu_BE9kddn2oNDNPOAFRXiEi7sqRuw1VvvMNZaFkxNuKg8B627QxiHtBqX-nXZvjj9AGoSx20q29KKfnX0ThnL0u2Mn_zJE5kXoovz7j4sUGjLYHfr8YZ36v5EN75kwXzcEiTgkiAdYbhdErLXnxsuFAc5JT9Sz3L5lDclwMtx6ZbMQ9vEC4YuwsWOvID4I57BZjFMwUgOnCxjkaNkXdAQcKfhgKUACPJPTh-HActUtRqYRGrVKCVAKv1DeRtTZoSRtOSdzm4ZOgMyjMKQbVObwTW190TsovUOhx_vd4suDUsgQGIHm_g.jpg" alt="photo" loading="lazy"/></div>
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
