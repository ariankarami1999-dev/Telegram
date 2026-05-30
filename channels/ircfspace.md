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
<p>@ircfspace • 👥 97.7K عضو</p>
<a href="https://t.me/ircfspace" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 این‌کانال با هدف دسترسی آزاد به اینترنت «به‌عنوان یک حق شهروندی»، به‌دور از هرگونه وابستگی حزبی، سیاسی، تشکیلاتی و ... فعالیت میکنه!https://ircf.space/contactshttps://x.com/ircfspace</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-09 16:36:06</div>
<hr>

<div class="tg-post" id="msg-2400">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">توی یک لحظه دسترسی مردم رو قطع میکنن، بعد میخوان به همون فیلترنت سابق برگردونن میگن این روند تدریجیه!
مشت‌مشت خاک بر سرتون.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 7.31K · <a href="https://t.me/ircfspace/2400" target="_blank">📅 15:58 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2399">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jfGpqmxD9m0-JGS8iKzbAOM8AMMSpOyMhySc-AvrGT6oZBZTV1skQ3wA3h56ZwjwKGzauPWOFpIWlC6Li9bughz5S6YTmonA78cj-nd-Sll1oiOCG0rWr9kGJC03ZjJuMGn6PX1H_rrqZWDCG4ua9hqgVW20xA7_B0xvslm4tKZP0c0EZ2TneNhTRyfvZwwxU6E3YYZ6a5vAd6Y_g0-85zStsWSP61AmmJm_rx2h2bzN9QG3JuUJgP-BGVyWXOlxmoC5MUkHcBIwmpICElsqMHJKzLcuvjoqVeiSBET2TMhk3VgwWfIU_pRDuTV6WojlGpK-ihj1OS2dCm97aleVTw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/ircfspace/2399" target="_blank">📅 10:53 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2398">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vI2hjNjBDKvWNcKcxL0x7Wg7bcFSqGeeEZZAA8FRXt2Hpj26Rj2_XIEQTa7bipC8qY5s0Ss4xqYLZ4V2L4jOmhu_7aeswJ6DnRZmT_Q2yfQqiw1YRSaPFq73estmE_jtYr0wURQY0ju1UT8D6lhpjFzi4dHWvP3yeaEtCueheXBxbDxlDSB-turSdecVkVxId_zvyPp0nrWqc9MxJQ1KUIPJ1IBif0pJw3-gxNJebanYpiv-xvOpI4dkndvGcvl__t-8lbaLVN4xBJPW3jI-6S44ROyIPsTu8Agb8j2fXGdpghtr7JGy8KWMKG19Qe3vUuPGXlqW11rwJ8Dz9IUb5w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/ircfspace/2398" target="_blank">📅 10:51 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2397">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">رئیس کمیسیون تحول، نوآوری و بهره‌وری اتاق بازرگانی تهران گفت: خسارتی که کسب و کار‌ها و به‌ویژه فعالان حوزه اقتصاد دیجیتال در این مدت متحمل شدند، اصلا قابل جبران نیست. /ایلنا
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/ircfspace/2397" target="_blank">📅 19:45 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2396">
<div class="tg-post-header">📌 پیام #96</div>
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
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/ircfspace/2396" target="_blank">📅 19:39 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2395">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Sjad1Kq8JCSOv9llL4Q-OHGwj1YX7axsTEIiqGosUMVAzpE-AyhCz7n3J5k39v5uICeYx1nHiNib69K_YB_15mdPye_bLyg5HiKuw_khI8E3XzCIomboSimPjbDkA6_XLpb6hMIwc88_qJteMCDfktt70VTib8YwfHx0V5AKfj5GK1hA6Y1IenfNRwwoFCuF42s4mz-eECI-Tb9B4TZpMjMCB_qHZ_l6ay90XacN3yQI3iA2BsWttaCjS5x_vtH6sqnvsFKxFTsNAQmyb8DXk2jC7aD3urYXgRfU1Yn9QvCjz6RzslnP7h5FIWj8mCZ9cdmva4YWF5elMusbLWsbHA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/ircfspace/2395" target="_blank">📅 08:50 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2394">
<div class="tg-post-header">📌 پیام #94</div>
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
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/ircfspace/2394" target="_blank">📅 08:31 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2393">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">دسترسی به اپ‌استور و گوگل‌پلی روی خیلی از سرویس‌دهنده‌های اینترنت باز شده. احتمالا خیلی‌هاتون دیگه حتی حوصله وب‌گردی رو نداشته باشین، ولی توصیه می‌کنم وقت بذارین و حتما برنامه‌ها و دیوایس‌هاتون رو بروزرسانی کنین. حتی سایت‌هایی که دارین (از جمله مواردی که با وردپرس بالا اومدن) نیاز به آپدیت‌های فوری دارن!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/ircfspace/2393" target="_blank">📅 08:28 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2392">
<div class="tg-post-header">📌 پیام #92</div>
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
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/ircfspace/2392" target="_blank">📅 08:25 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2390">
<div class="tg-post-header">📌 پیام #91</div>
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
<div class="tg-footer">👁️ 40K · <a href="https://t.me/ircfspace/2390" target="_blank">📅 21:56 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2389">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qQ42dBe9a1kLsDONtQWRNd9SBv1w1-R68o-nXr18zd9J0IFPh7NxwVd6RJ-bAl5xGRNMde8oc1IQvWQHP6B4EMpkI6ULPLqHql8Pww2Crz0OOggL6qA6rXF3pl3pwcVVVWZdRWQpqdu9z32Kk5Xr1RByatnOBn7Q6av__ioWP44LmF8OVVxFVjR8a7qQZVI9z7yCZLQ7VWqHgQRm5HfkgRn8BZZ48MkAOsxH_AlxUMaUvSQXm8Da429V27_C1Mre2rHn62ZmE9eTqV7jsUvNdZuye2_pNLG9dRa8alkww_7raVtIctthDVZzp5V3FYN4jc1hPCevBUbMiufbjx2eEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نت‌بلاکس تایید کرده که میزان دسترسی به اینترنت در ایران افزایش قابل توجهی پیدا کرده و به ۸۶ درصد رسیده؛ هرچند فیلترینگ به قوت خودش باقیه ...
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/ircfspace/2389" target="_blank">📅 21:31 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2388">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RYFz6mw5lR3Wy3hnuE0sxRBKxSO8Rp8V9Upknu4OS_HeXSdl-fYwWHOtal4pdplL1NWvfZxHrhUkk0HxyN-4FgLdGxgRzRb3W8fSHwPSh08gJL37qFxDQqCFeO-lDFuo5GpNE0bmcguBVUKqu-IJ759Nis1uMBKY92XU5tlvRW9V8nUNk2VvvEtgMPVZxAv6aqV1g1Gg3U28Ujf4KiLfr-gYhSYVtjwInBK37oS3KMCLakSe5cFSnWdsQ4aF3y5VBMc8RvBfqDnJofCXzYHrDAJX6sQG-nNo5Vdi10W65ND_ovDoocqU33-t_k1UFmiZ2InANrd5WmMr5CpiirK-Ug.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 66.9K · <a href="https://t.me/ircfspace/2388" target="_blank">📅 17:30 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2387">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uOfs8el3VQVt3Z_OR19beov-PFzNDCn0cUSvGorZWxxg5D4_8n_yCMoQ4MiDhMGBINOXTiyTl1Q-U64aycI9y-NvlW4jQw0B5kjsavKNywjuLpfkltrIJquwF1d7r6-wt6TPrYqVZTaPJE47yd-sBaKRTbrOjnNMXy9T1lWY_CO9gsS2xpQ7hdutAluTJ1iHUQgHOe7znRe8dRWux-Ly9uWRoeHRtCmksNhqYrmk19R9zfaIDsrdesFhnQ1UJSC1C8FV0bzXoYFBiNKX6c4Z6reU6x9idgfWUoGJWzkBHgN_FxyPLWpgJuORObgnifFCJ_oFGvilIVdBm0ke7jic-g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/ircfspace/2387" target="_blank">📅 17:24 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2386">
<div class="tg-post-header">📌 پیام #87</div>
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
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/ircfspace/2386" target="_blank">📅 17:19 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2385">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/m2QaEY_lgj4Vo3KQD77R41ZozVH7abYo1X_p0PvW2Ux9MH4_IAA2An6P0g6jN9JqychqE8ctLUZHuOT1O-uhz30SQ3sMwJLVuwKwA30LN7dX0pEsZ1O067k4iHaND4kwxd4AwjPwPdQYUL-aUYqOV-2WEPLStQpcMzc-nOJIoP4_BuweZZonew0eoEdma0kp3XiRAV03qC2vkC9uU4GjrMJ5nUZoFEvWQ4ko2ywCx3OVMOI7dL_XGdExJNvFbN43x9wxNF9Q0vRxzZN-htu3tTlIwvqa-EudOs2sza8Wb7vGy_Zb-XeLo0n-jBlWO-H3oBeny3jiqOooVH7Yhw3zvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۴ فردی که در دیوان عدالت اداری نسبت به اتصال اینترنت بین‌الملل دست به شکایت زده‌اند، کامیار ثقفی، رضا تقی‌پور، رسول جلیلی و محمدحسن انتظاری بوده‌اند. /انتخاب
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/ircfspace/2385" target="_blank">📅 17:12 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2384">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HTXuY3QYyrI-4WehMsS7dujRo2xxhkTA0IvtMECgrv4jo8UKO_UYYjB3EFpLFOlYBl4JGGd2qaBvEK91qfeYCcBtQyHAjeBmkeg45GiCjq4qL4pm2jMX14lyk9fctq36vPJEc3-3VRlo8xWzc90tqUJSMGJJ77tubsxwdUw3NvydB8Vq2n4LE85IKIOjU0Cxd2JfvDNsxO26X1_qSNvuU92Y5sB3xR8jRPIL_lFH-eEdvlpJUxfw-xpifbQSzhGvxNXlWkH1wm7Yz9alVH4L43vG42YhryH1fOouj4-KVMdJrlJpYPQTDI9sP_Yf34b7f7IMOsJmouzCi2iVglbjXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نت‌بلاکس: داده‌های زنده نشان می‌دهند که در روز هشتاد و هشتم از قطع سراسری اینترنت در ایران، اتصال تا حدی درحال بازگشت است. البته هنوز مشخص نیست که این بازگشت اتصال پایدار خواهد ماند، یا خیر.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/ircfspace/2384" target="_blank">📅 17:09 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2383">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">دیوان عدالت اداری به مصوبه تشکیل ستاد ویژه ساماندهی و راهبری فضای مجازی کشور ایراد گرفته و گفته مصوبات و تصمیماتشون تا زمان رسیدگی به شکایات، قابل ترتیب‌اثر نیست.
فعلا اون نمایشی که پزشکیان و هاشمی واسه وصل فیلترنت اجرا کردن به دیوار خورد و شرایط روی ملانت باقی می‌مونه!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/ircfspace/2383" target="_blank">📅 14:43 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2382">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PRaCTus9gF22p4RUVURQkwZPsTZKt2f24WSFNZJV-JCkJpfPExrfUR9vup7muwXzZSGGJX5xVmDFk38QZFWCZDPPtFcnxQrZ7glVGo0fQSf_bh7wAvSAg800R2gfFvEzfLr8CVo4Qdsm7uehkJV1IRYT42XI7fMMlv9c3tqj2hDmNikHXjH-Jsmb1PTYUKOu5gpJUXTr5whL4pdCM9Mr7kHtR1Oafg2ddct9Y2n27GMD6KNWkNXgwpyabGnfP5ERRKoD3hXXzHfE_NUW7d8xqAg35xeh79DE4Hw32RoX0cQxw9xuHYTl4hW_VtNDpQnwDTFwsFE9esXremhGcNzuyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه‌ها نوشتن که مسعود پزشکیان مصوبه بازگشایی اینترنت رو امضا کرده و بعد از ۸۷ روز، بزودی فرایند اتصال مردم به شرایط پیش از کشتار دی‌ماه برمیگرده!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/ircfspace/2382" target="_blank">📅 23:19 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2381">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/llSGIGuJxz9sH1lUIjqVgQbfKyUrZ-foCzRj8yfkIGgTRNDlftjwRAWM_N3xfydOkF4LvUP1oJ2rJ7ceh7YrZRn5RPfcrCzaD7grqqu5XUObRSBfWg0u8KIN7iwOJxztF3dTjUeoRP2pD-r1ZPCbiOjkh3qBloOmbGSbnCHTzO605wHzCLUgRCvIFNLNJ6mvBpPAODx6WLOR3WQ0sLfaxsub_JC_MdxYlrYRUyMJ2Y0v2i7VOh-y36lrQ9iN8SqvTOxW2X2-wAbMMzikpSLHL-mNf4sfm50E8HZy3D2XD53MDOTYZV9mPN7jhVmjGxySE89bYoSquLsDK7o7itHZRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نت‌بلاکس: اکنون هشتاد و هفتمین روز متوالی قطع سراسری اینترنت در ایران است؛ محدودیتی که بیش از ۲۰۶۴ ساعت ادامه داشته. این اقدام هرگونه شفافیت درباره اعدام‌ها را از بین برده و به شرایط غیرانسانی و بلاتکلیفی روزمره‌ای که منتقدان زندانی، مخالفان و حتی گردشگران بازداشت‌شده با آن روبه‌رو هستند، دامن زده است.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/ircfspace/2381" target="_blank">📅 11:23 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2380">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/eONv_nPDg5hXjWijHOp3QP6mKJmZuKyxjZB-BjG0C39DuQr1sgZ9XAsgZxsUXsSA3m2kb-jafVHdiQOmhBMwapqiWZQL21B8mJdy00vDILxcntoqYaD1BKAOry64yr4eFsmNGqCOI8VdnluUvDcGpbb3nA_dFjftBkJIFzdXH_dxTpB2hmt5y29OjJX7XUXEqAor99lUjlawh3QRO_crWNagmgkT5iFq6yTmmX-n1_kR6HjAeFxerSMfysRANu8llAwYZK-gWrHU8VN9SvItPd9s1TpU1Hdt8P5z5szKMmvPJTSbiLaspgxt826DtsbCThxYaVIolYgEdXnCyhiY9A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/ircfspace/2380" target="_blank">📅 17:16 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2378">
<div class="tg-post-header">📌 پیام #80</div>
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
<div class="tg-footer">👁️ 41K · <a href="https://t.me/ircfspace/2378" target="_blank">📅 08:57 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2377">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/aw4A-DHqoT1CvLN7a9ffQEqIVt91jp0pPzDF8rCtXCXjHjibalWwRP20vyT_fBRQlcmbqsGPl24s8r3JE6vRryl-JAepNj5WIgPysGkTsuiWs79nJwxBotCqtfF5H-gZjixOt2VWCdIKY9xZfp22M8jD8PcnxsbeakYuju2b4PY4cqyYHhiz9SsZQtorG_4LeCF31dEvYL9rP5hvWUinym8S9e4jVO7V25kgPQyBEoT0QH5M9GscSrVTKv6Oy2phgVrEN1bQFyjdq2jDIudFaInLwLhHZqHycE2z2lT_K-Dgw0mf6iOYb99M194J6bEVUTMM_JK4e1-MxgywsUC21A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قطع سراسری اینترنت در ایران به روز ۸۶م رسیده و همزمان توجه رسانه‌های جریان اصلی به این موضوع داره کمتر میشه. انگار دنیا معمولاً به رنج و فاجعه‌های طولانی عادت می‌کنه؛ مخصوصاً وقتی قربانی‌ها صدایی برای دیده شدن نداشته باشن.
Iran’s nationwide internet shutdown has now reached its 86th day, while mainstream media attention to the issue continues to fade. It seems the world gradually gets used to prolonged suffering and ongoing disasters — especially when the victims have no voice powerful enough to keep themselves visible.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/ircfspace/2377" target="_blank">📅 08:51 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2376">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/a874f4f669.mp4?token=HSi9UKrtMLcYI-aIbzWjTC5x4Lz2P-PaeKczssR9wqhSs0het67Q8qj3BlXp7LSeqZk_w7Tp511sKLq-zDp3HjWdroKgAmJBzT3RE_34cOo0Dkds39Pt9wfUWOJpgyK5uXETrdltDCmmxuBqfXCCnmbD9MxdFFIvkWyXqkvwvwd3BR8Lpp4LKtvz5vtqslA2hDJE5IIeFL4Ds0PuaSuPEoeE0BLzzLL2diVAeJETNjVnZMQWLmeVAEWkbinRRrgafthoMUZEI1NvMLVMhVXYXm9URcqR8Uil_ezHD8iYINejLwKa8J-GgPEbRmnc-1JnLiBiIELYvtwa8fmv4YzvAg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/a874f4f669.mp4?token=HSi9UKrtMLcYI-aIbzWjTC5x4Lz2P-PaeKczssR9wqhSs0het67Q8qj3BlXp7LSeqZk_w7Tp511sKLq-zDp3HjWdroKgAmJBzT3RE_34cOo0Dkds39Pt9wfUWOJpgyK5uXETrdltDCmmxuBqfXCCnmbD9MxdFFIvkWyXqkvwvwd3BR8Lpp4LKtvz5vtqslA2hDJE5IIeFL4Ds0PuaSuPEoeE0BLzzLL2diVAeJETNjVnZMQWLmeVAEWkbinRRrgafthoMUZEI1NvMLVMhVXYXm9URcqR8Uil_ezHD8iYINejLwKa8J-GgPEbRmnc-1JnLiBiIELYvtwa8fmv4YzvAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 32K · <a href="https://t.me/ircfspace/2376" target="_blank">📅 08:40 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2375">
<div class="tg-post-header">📌 پیام #77</div>
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
<div class="tg-footer">👁️ 28K · <a href="https://t.me/ircfspace/2375" target="_blank">📅 08:36 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2374">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SRYi9oZvdRYsBfRXrQWuqpDxPUe07iTWJzq10AmNiamtJNyS37f8_385rhJfr40imqrzNcHIaosAO5RnaPrX14bgb_tdVkyvEDdwLKYWDQQub2m62Do8DRwciT6_C-g0JMujN29jWflmq0sHC4Rg9fLkjDIN8Km747iywsNdzsYJJNE3a4I7ZIOOpg4eYvQd0aO35muH73OXBUklHlePywOwBKabDPvBIsiTogFs3d8HY7FfGO9lMAPUkXYjV88ZIu3J-NS7GnZzVCSfns5TfQs4UeQYDEpUJbNxlUMYedkERdAxsbR-AgCljWRo4S4NXLZjVi6lXVp_A1FQ4M29Xw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/ircfspace/2374" target="_blank">📅 08:38 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2373">
<div class="tg-post-header">📌 پیام #75</div>
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
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/ircfspace/2373" target="_blank">📅 08:15 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2372">
<div class="tg-post-header">📌 پیام #74</div>
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
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/ircfspace/2372" target="_blank">📅 19:51 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2371">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Qx_VIUZqTVgjN9ticLh9wZcwtYvLNW3CY242YUZE1z3BQOuUcohuSs_sNx4rNB1YDiMic9jpQZ4DK773VSsCoo1EVFDFuj_p8L376PL2Q-4TUQLgKkoVOMykgk_d0EXLBHTc8isXUzlmEpSa0e-fa0LDqdP8E015X-BABEF_i7-6NcI_9t3dyct9x8Qd-3ORMXtH_iZdr27zN61rlXe9dsO2kRlK93gdDnHe7K_2YdCxE5Q2I5sFNuMTSB0I9OW3rPRQdzIp7XC9zxoNqkOQQB4pjOvSlUBQgFhpk3b7Zr5yMRO8EvE7_yG8oZX1A0WKbET0RrABzDqZk2LqSEdQgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نت‌بلاکس: قطع سراسری اینترنت در ایران با ورود به روز هشتاد و چهارم، از ۲ هزار ساعت عبور کرد. هر ساعتی که می‌گذرد، شکاف‌های اجتماعی و اقتصادی عمیق‌تر می‌شوند؛ به‌طوری‌که هرگونه ارتباط با دنیای خارج به جایگاه، تبعیت و امتیاز وابسته شده است.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/ircfspace/2371" target="_blank">📅 19:45 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2370">
<div class="tg-post-header">📌 پیام #72</div>
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
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/ircfspace/2370" target="_blank">📅 20:18 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2369">
<div class="tg-post-header">📌 پیام #71</div>
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
<div class="tg-footer">👁️ 42K · <a href="https://t.me/ircfspace/2369" target="_blank">📅 20:12 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2368">
<div class="tg-post-header">📌 پیام #70</div>
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
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/ircfspace/2368" target="_blank">📅 20:09 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2367">
<div class="tg-post-header">📌 پیام #69</div>
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
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/ircfspace/2367" target="_blank">📅 20:04 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2366">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">یزدی‌خواه، نماینده طویله مجلس گفته "در شرایط فعلی تصمیمی برای بازگشایی اینترنت جهانی وجود ندارد" و "با قطع اینترنت، کسب‌وکارهای مردم از جهت ارتباطات بانکی، خرید و فروش و بسیاری از سایت‌ها همچنان در حال خدمت‌رسانی هستند و مردم مشکل عمده‌ای ندارند".
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/ircfspace/2366" target="_blank">📅 19:52 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2365">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Q4LnJbfJZ_rOofcjgJq6KlveXnqsi_LVghqfDHAz2sH5YvIrgAoHrbtc91NC5ffNeU0A0yiqw0CKzPU7seav8FulaBnpJuVlxyP_rb_t8u-64uOqtBchByl6PTZnsqbftUfH_aoCmcqmPnF1PFg_KNsQxhV4g68Rk7XzS1Or0-458Sx0t5wsjnBGPG7q1Ay4wHVZha742ZAPqh1A9N08MpOREw0U6z4-yreKX5oSzzsPU4JCBlXPMLsN09ezXDzOjx-WRqpaxS7yN8PnCJM6BPfgScqyb4ykdg6uaqZHKTLwp2txHvDk27eGfjNXpAMYZEIA6enEE7CUiB2lgmYu1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قوه عاقله در همراهی با سایر قوا، قطع سراسری اینترنت در ایران رو به روز هشتاد و سوم کشوند.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/ircfspace/2365" target="_blank">📅 08:39 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2364">
<div class="tg-post-header">📌 پیام #66</div>
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
<div class="tg-post-header">📌 پیام #65</div>
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
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/ircfspace/2363" target="_blank">📅 08:27 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2362">
<div class="tg-post-header">📌 پیام #64</div>
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
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/ircfspace/2362" target="_blank">📅 08:24 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2361">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RumeTaM0nr4IrOkBpEKy82JLoMtvMWI5vG60xx97JkyinGXg-TQcy_59qA5q8lqn1q5FDY8twLWvqAGpXZpBya41XKOU3fDIhC8SncGQ-IjeH86PyBLDxBDVPgvx9nMqpST2EUqbmi6a4RSxop0qVFWmZj66OqH_tNHO30rVIHDpL2nCLieMJDQpArDNYizHSaPlcdx7hg_uOHIYYBHLAJNCvSpCTAjwbT5NIEXjQVkh3AxZ9btyOK1fTSS93ZM13HCQgk73JSdNP5MUm7rCwKgVF83VLuN3j0FclquSvbJPYdADSLIhR1PA7XqWrjMm1uz8TDYJd86Sb9_Gvk5XnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هشتاد و دومین روز از قطع سراسری اینترنت!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/ircfspace/2361" target="_blank">📅 09:00 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2360">
<div class="tg-post-header">📌 پیام #62</div>
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
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/ircfspace/2360" target="_blank">📅 08:56 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2359">
<div class="tg-post-header">📌 پیام #61</div>
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
<div class="tg-footer">👁️ 49K · <a href="https://t.me/ircfspace/2359" target="_blank">📅 08:59 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2358">
<div class="tg-post-header">📌 پیام #60</div>
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
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/ircfspace/2358" target="_blank">📅 08:50 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2357">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TLxAaYbzIDwDck_qeouAPd4HvDMgTEnk4g7i2VgPXNeP3Jo78_Wb80RBbrmwVN4RdYo97TJM_82yF3rHl6av_EKQLEeJsz0qWBjlcZO-6gItLSNvwOaDt0Q6u5FXPEjKEExO_3YUfwrm7o7fNpqI46E6d0d10pnXFXX3MwNnM0-o_jPok4qxnUQDY2cOvXtzPVUlgbtkzLFGd1LQNaFx7bCO9qcj-Pjpsa9kQoz63uROU31xXnoW99S3Ac8JbtRQGrLbSsLbLumePaCkaCI6rjvvIAHM4BcsjdXScprISaFpmn2VQg_X7A3StMWqcZYep_3L2Otz4_nQzvWA3X1kGw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/ircfspace/2357" target="_blank">📅 08:38 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2355">
<div class="tg-post-header">📌 پیام #58</div>
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
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/ircfspace/2355" target="_blank">📅 20:07 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2354">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/v5BTiT8a6mbwWXx_SgQk_SGPXU50skalexA01iKqRjgq1ZtFy8XaNdHGrcDk2jA62ztyjFZCSRDh7CaswQY-YkDmAJ7701LA81BtuR3znoym2IYJJwaglgcHO-uNvj1_sxW0kYz3LA5LGzI8qqudQeuj7m4kwptlbLUabDIkhUFVHrO2JRVxd3Vzu5SbEdKV31eX0rcUCYL_31P2_AYy4JRuK-9zqBL3B8WQxNsi14RN3MGO5hWpf2wSC14DPdeA0__SthpNir_Sue_m1pbJKrQjSPsBT4Ki0nlxXr6fTdnbFaOHQgY-5wcE3ykuhqpQuqzyenDMa_p3nYrIaiywzg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/ircfspace/2354" target="_blank">📅 20:05 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2353">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/saJtmUiXPXgttnL-3H5-X2ieKTLAbTpcAJ-xB6OliPHmVp_hIts4SK3JW5rZGNjehu_okFkL40OgfMP27eN0z8VUFUMGtlMFhCjpv_UxMU3FjUledo3uCnW2ljr7q_Eg6u4HSlJm5tLT9cEr6DZb5wqpN9fixebbBvRGgYKjNNDr9GbjzsIr4dW_SfDN5fd1uL3rRuL1MH8GAFgH1_uTqvTeyq1jDleYdNkXSgGqjFcgj927Ow36xaVTH66mCXST-ASL1SQwOUrYM21THnp5DgA73pd6DXoYk_cDTLqdqmVCUHnXXXwQ0HkHTPT48iq4DoRDwYalZIAg4tyKZ8-wiQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/ircfspace/2353" target="_blank">📅 16:24 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2352">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/opYqKkCaKs9PlEICmGPnx9NitM6UQmcCbWgArfVWfP9QFaEeIh4tpoFsED0u5W9eCDBvdPTWrPSpxODn6dtXOrqzoOhb7-FcAh0Wtn_spjINz0oAVaLMofsEfmykoU4QKb5bSfFW5Kg5_P2PIP3cCjjN2vGEwQ9Q8bZcsPi2ax8-eVhRNrmaD3_WJc91ergMUYAfOef-v-dJk3-0hb3vUq_lwP4EwpTpNJYNynlqvuJtbqAwRoySmHNWYQMI-WMWLJRpcwAUB3aNhAeZ-7jsXB45MbPozCuFtrg6sWbb9csHvY1bO7pR-z_QVETW8cHOnWQH7BeQPl7Bexe0L1MAEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ستار هاشمی از پایداری شبکه ملی اطلاعات در دوران جنگ تمجید کرد و گفت: شبکه ملی اطلاعات کارکردهای متفاوتی دارد. در شرایط جنگ شاهد پایداری شبکه داخلی کشور بودیم تا ارتباط بین مردم قطع نشود و خدمات مورد نیاز مردم ارائه شود.
وزیر ارتباطات افزود: در دولت چهاردهم نشان دادیم شبکه ملی اطلاعات ورای یک شعار در میدان عمل کار می‌کند. این اتفاق بی‌نظیر و شاید در دنیا کم‌نظیر است. /دیجیاتو
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/ircfspace/2352" target="_blank">📅 16:21 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2351">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/t-inhjUVMF-bgR7Q3Dh95OTOeI-uD_8mcvCm22Gqs9svAKPr2nPAxXG1TOmx-alemAWUJg5UhFefa8EkPr6trAgu93BBJlZ2UXxet_nr_j5sZMYwfcb7ta_I41JzXTNRNUM9fhVxqBZJtKW_9zU2KfQMTQBHmsre1ETt7lbicskTptTeb-iRF9BMMAisXmzGsEMGQY53WIufuUEH0egD_CrX40lZcU7f6JMYWlQ7xPOqLZir-AhNIJTf8foHXu2UdCyrHEbL461YWuyvs6k-detNa6sotxdH5F54k_Lfd0dKpmEscGWth8lLoBFdgBplLcSRRrkFUE7alfQVUyDqUg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 78K · <a href="https://t.me/ircfspace/2351" target="_blank">📅 10:02 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2350">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">باورم نمیشه قطع اینترنت به ۸۰ روز رسیده!
وقتی حکومتی برای حفظ خودش حاضر میشه یک کشور رو وارد خاموشی دیجیتال کنه، یعنی مردم هیچ اولویتی براش ندارن؛ وگرنه امروز وضعیت اینترنت، اقتصاد، مهاجرت، ناامیدی و زندگی روزمره‌ی مردم این نبود.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/ircfspace/2350" target="_blank">📅 09:21 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2349">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rYkbJlqjBys-SBwRI84wMIIuWBT5dBopwvvn98zorxpnI-gBB8Jje60bXY8_UtUQf2e1uOOflcCK6_SMJEGNeUmetpDKRwiutZS20w1kg0cNu4BJntLqJDJGfjhco8YAR-jp95RK1t6hWjl_CFeKjAPHbroA_xzhDaS-Wzz3oPuSAW9xZ7-23_VpEeb07PnzJwrRyvOpycw6nO1lGnZOm8dGHwxPO0QUM_EtsYml0yT60Klx2VN4NNZZHbU-YltJpQROYABpVFMQ0eDwqwNZCCWTKCVTtXPkqzi4bEpYUocoeI_KPnyGI9xUlbdyubRGKmZCpC9zAmY5_3CAF2snrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسعود پزشکیان بعد از ۷۹ روز قطع سراسری اینترنت در ایران، روز جهانی ارتباطات رو تبریک گفت!
🤡
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/ircfspace/2349" target="_blank">📅 21:08 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2348">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KlreIKoiiugpO46t1Idw7oloNTFtR7GXXAPRjXdyw56y8q0D1fjOC9XgK7oe_9LOQjmlTtGlQAXX2UmsM_aTrdH1nTvwyAZSwY1jfHH9NaP_M2-HCwAQcEGqtnGH1t7CKY0SBTU6dY7_6o_xEDL55Q1SLD4qO70rEK1z7D9o_5Y8K7Yr0-VLnDbY88BSgFFVuKAFR-yGUg9n-r15-DrWs56vp59KcfRM2Mi4J1EQAcKMvNRQb4yE83mi0RWr2wt9hAOKry_rS_dmG_kHNZhnHrHmV7tsa48sqSXXB_dwOb45zg9-x1UQ-LL7i1cTuVMBGx3CMte4lLLb0OWRBry_Eg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #50</div>
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
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FbQUAKmhU3wvqE9bcJ5Ge-hMTnnfusv6QpQbOEhcbsItjlRSXGWVf9R57QTfYAoT_1nogRw27SxajeJVEokshUUd4eQ2teTNRSIwVepHhHP-qVJpMAEogo8K1oiJS7DvUnL18918f2aRxtE8BN4y7dwwfCunmW0UCou60LBy9RWDTyeo-RFKY-VrGhD5hY-vRnbHplQ2AhcYkDYyFIjeXyf5t4NNzyHZ7c2X8BBmD-yWeYXFCcGP9wwpMgTO0_Uv17OvxPu4RG7P-MEMoWrCouojQ1ZdErAMkMhWfAFGsJWGpgmYqYEzLo6qHnEDgFmTk0CutBH3QT4Hhhlluw7mCA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/ircfspace/2346" target="_blank">📅 23:40 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2345">
<div class="tg-post-header">📌 پیام #48</div>
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
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/ircfspace/2345" target="_blank">📅 23:28 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2344">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ovtaKMHW0qahjEp02CPH0wWS1CWKKRaCXH9hnkGOAjFUWtHEIkLYXhjLvMnQIJPhaVQCT7jbAKoVaeXQq4xzaVCQjABt_PtiHmo5UNwvB3PIPq458wvl4x3J80K-ABczVJ2EgNXDXXTt8PmDxCwMKOgXGHzo5v6K8UGC01dCsb6DIaokpF8GOc4h69GHxzB0UrhXBPg2pWeY_z1xMBtJHh-MXHTskIHaCNploB8qd5kX5Clm_mDwX_z05ijOq321HWiOIFt8vjjca90tfHzKN7wb4YOQmVJSV0rRJ9Jpt9ciEGuo43DXdELlBaNps-dzrKx_6RHCHGeRi38AhHe_-w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NLzf-Z1pf2bNF0_WSQvsoJZRrp-QcqQl8s8tM4hMrx8gdqMFThSIRtxpJJNzcXnrUOSq_HVpBCqX-nh2evG9MsT5G_lkVyLSPPkw3-cRCp-2rVGIV6CXhApfNnOk9lHzazsE5W118yVPd0Wi79Li3XLJ3xijIhL6mxjEzCz9TS4v0ufaeFL60CMI7PjXM6WvA09m9NeaJgYVJAZ1wQGAhhA_Gbfkx4VGhQksVOf0Vwr0g23Hp3OqjSPVcyydpLvrG8lACp2chVMfhvrM4v2pPTZsssYZYloDF9YTe9NdSMccSI4eR3_C0m4PxRvgbCDrRkw-rxXq3O4LlEKXP3Ubsw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/ircfspace/2343" target="_blank">📅 09:11 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2342">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iX6AmDb5ueztIFgCZy5XXKFIGIFQlxM_kPyXleCAjcu_D141Z68586CofPdfY9kxtShvbvS5PJqmfDRDTwAacr1Z96Pd5vYTPbX58esIqNGluVa7CiQWtWuvUPDsieR0kvjjUHYsUHiFyBjhThOzM3bZQSh1kASRMb-SpvFmNljk6dXgsYJdIJhkKJKAuWcJtc9qwPoRVyNopMn34hg_3R3mlQpZ_MjHKRVwFh1r229NusvDCTiHbj2go2ZcdBJxjIZRq6n1-LOAHe5c7gsLSDKc4S74L2pu9nuHeGOxobdbHbTqIWt_i6xuxSa2ORqIdUGplwouDXea_5fiPwT1Dg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RMxMVhyANELKzT6_i7YBR1YZWiKBQm0ARm7v8L-zymV6AzV26arli5eWTl_LdQAhjMIZgLnFGSMK_opyfqDvqPz5mBK7nGB7LA9zSYhLLJ1mYJexSqEEy_YqbFGoGZYfAjWAjf1fxkwwIcj1mwS84Sf4Q1-yNuYZOJCZb21zS-DM7IZRFPjjmHgJkqw-PsVGg0C8x8gs2wt56RVhFBvJYagv8WapQTQbmGgK5kz_x1eL_4hiMsYr-KDuNT9H1dtcK8_77SogNotKPu8CGvmlDpdlKmA6r0O-y3NASSgciaUbX1pq2I6EZwekHedytS_dxx2S4S8okN_tBqxeKnYfsA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rL5SNmQw53Sgb6T24cAB4HTSwbLZzEkVJlYpKhut2QVyh6M6SdFZA8Uh-mRkGuU62B-FsWMQ6aVCkzo0hrU7kigZD2UnMRhbvoJc9CKAc0-ZAL_xwRyqVsV3j71IugkXL8aOvBdEsw21z6LHRv79eeVnRkGs-R4c66UNIU9X4X6pp6k6qgf1WE2pxBvxlyf2H_1SKKz77kYr0t5Rrg45OLn_6D0CvtdnEpdgd4qjeDYdaDyucpCHjLjBUfug_9WabZf1w8tGilXBM9jbB2QfHg-7Rv-GqirZ_3g8SlM1dwoHZvV3FnQ3ELOjVY6Pn1Aac7OGz50RKsr3WthIzcSeEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در هفتاد و هشتمین روز از قطع سراسری اینترنت، از جدیدترین روش ترکیبی عبور از فیلترینگ با ذکر "لعنت بر جمهوری اسلامی" رونمایی شد.
😁
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/ircfspace/2340" target="_blank">📅 08:38 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2339">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/aCqglQ0ZfXH923HaUU75me0ScJZ_t14By2nTeUTjaP13nsJaOIMVwfla4dqO8ZFORpVdHcB9SSoNaZkg87nbPYUrp9ig90SdyITVVuFY5mKyX66sljboJMg_tTtIXrdxprnGVcMVCqCK4RDNShj10N961yDwjQv_Ysdd6XkxtpW0iZW1paVaTnl7hIRKA7Uju4RNQgtAUJJCa_DJYnTsgVni0t9WnJ8dL4Xoe88VRi58Hy74DBQGs1AVisJ6Q2HqID_IKWFW2tlHgApGX29U5sSB38B7wPTRlWCNKLPqJY7CiN0kN6e0f0JZUqHZ2aZIQO8dLTKHPnhVSA0NlfWSOA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/ircfspace/2339" target="_blank">📅 08:28 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2338">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gVxkNlX1jzpk00Tywp1gTdoCuA-1ELW6I7Rmb8AM6VY9KOxjjqmOP46JxMiQ2iCvgzdy2cwItvtmbiy5N8BTFEZh1BE45Z9IXB1ITOTUapTyxV-c4xGUd51dXqS1WWIfI0tuKpPoyNsk2TRlajR935E2DE6S4UL9R-lGv1RYuJkokheFjzh8c9oKYhuj-NT-TLL9gC9XLS1XTrAb3B9wfr7erZuhuQnKa0ePoRVkeZ3uiwft1lcZW6oMnMV_ndOcszmNl9ILj94LsY6uVCjZ_dhG0JazxSrPo2OyMpqgfkXGEe_xJBxnjkpXhegRp9SPFoxXvfJ-6QcFKRR794SxTg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #40</div>
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
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/ircfspace/2337" target="_blank">📅 08:25 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2336">
<div class="tg-post-header">📌 پیام #39</div>
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
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/aC1ZmQarsJ614DV1gdxUfD26BKE_YvU6t1jZMSzp-junkrxkYk5pToz-PS7H-kpM3JdLGL92F7Hs6DnuOmURGk9U6kMzvMIaq7LcwLSlbM0ZiQWFEx_iCPGnF482bysDfDTtl45gmri5tLd1diCY83RX3fx-eNGvtFE8uIbJZlrDUJ-3m3_fnYLODJj-ZM3nj7QcQNFGuClK86u876q2v-PT3kDIJLk_htqukwPbDzeNJkL1xi_KydrNbVISH8ql4-8l8XJgSBcKEemIFUz_qlC0yYEMMH9J-3Wg-uMbNr9wVKEjkiDied9e8lpDHJ80K-LLPqe799oo0nzJtllpMw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/ircfspace/2335" target="_blank">📅 16:26 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2334">
<div class="tg-post-header">📌 پیام #37</div>
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
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/ircfspace/2334" target="_blank">📅 16:18 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2333">
<div class="tg-post-header">📌 پیام #36</div>
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
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/ircfspace/2333" target="_blank">📅 09:19 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2332">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/k5cdnaXdCTs8_C2Lgct5Njg3nzzINcPu2tTY2ee3pbyygkRxQNZzEanGo9UqbTtreaZhqXU7qVVC9RVQoOOmC8wMFQ_mvUzNMmAxecTuSRq6HQ8zj87ouA1-MsSnVNdIrfG9qATEm78jDlA1puACc8TahJjnXX_-NAsJpx651-n1OmlsOTYS0D6fbwMHkV5BSsYmK7D_uA7YWZEJeeGVZ_qarYW8VIsrePT4Ngi8AJJJMQP0JmY1mfpLZgt4CEo4bQv-yP7Qhf6Rt0gYBL3uH28ejchlef1ni3j2PE9ln74w32AorjzxpC2VCqiHl3F-ToYDIlRkqKLSzhvcQVuElA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ggkAZR3T-m4Uw_CRsOrJeEwMOMFA4FIOG70sJWO_aoqFLfs0p5sG7sevp5QwPHwwGvdL2GvDNok8327yMh-SepSumlN-2AZLP8vSg5dCmWvOjEd60tD4_Y0GQwFmvSTsq9K5mkEN__TDNxxau9ATB-d9hCMQms61WFqkUTc-9Ik9u8GIcdv8qOCWTBEJ12GsKK9S14RbwP7-H-WbFjbO9PgGegU2RYf9g8-Iltu5_hfFapOYi5RcuiTXU7vwM8uwgfuDZ55Mp3bt1iHpicnWEPPlyMUuy6aTsr4Fu4Y8r7o2YRMPTx5m1tKPr9ogWT9-LTAa5vMySvhxgsqIPWI5sA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/g2Q-abd7N0tX29r-NWnOqLL2sJoEILZG5gJIac0tIEHL27cKfxJ8C2oSBLcArkYe0irehd7mAx_8mrNfK8cggSFIKXCMliLd0Us6feBag-0h-nYqnbf9ImKcM7APs7Qcep_3TjI8YDFGX0f5F3G4RWOfqnXqNIMFa9Sr9BaOAFAg3mYv3SvxPpuoNJuDiubP0JdDEIpC-f6s-5LWv4-9ifGCx9JUJKQKnESALHI3nml7Ft_iBWi_YYnl33PqhFN12nR9fS86stQ7ZIbjAcReLv43j7U0SJuVUQmsXjmL2sxTvEx92JAHfdOxcg3kJ5T2aXaXE7RRmSr7qXbcy2Uu7A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/ircfspace/2330" target="_blank">📅 19:32 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2329">
<div class="tg-post-header">📌 پیام #32</div>
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
<div class="tg-post-header">📌 پیام #31</div>
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
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d9e9b1e831.mp4?token=oizocOjGZJ_F_eNN4oe5Yi9njK8cBXQPlJ2vgrSL4z0rXhqcd-PjUMisabrVXgV1smfoBDireToEeuZdNyZsQiKeO6ovzuviC83R8SjBMMg9yCkY2VsZKXEE5rKyKcM07t_TQ1IhiNf2b26Y0SZ36w-ZKH8rV4iFddrZZrLEhW2KyJQc7Fl-u-uiSxMzxQeJyEnbDT2Uja9C9_Q6NUSl1XLB0AQFNrqomCSJiaG4BKudYJWdxteWkg5l5M3SfOhGo7j_GLLRlTeWg-s_9ci-lnXEOF4ebMc53UsL8X_uH38LfnvS5dp_kaCQfqtahXcw147HxngpVjzvekfOy34pNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d9e9b1e831.mp4?token=oizocOjGZJ_F_eNN4oe5Yi9njK8cBXQPlJ2vgrSL4z0rXhqcd-PjUMisabrVXgV1smfoBDireToEeuZdNyZsQiKeO6ovzuviC83R8SjBMMg9yCkY2VsZKXEE5rKyKcM07t_TQ1IhiNf2b26Y0SZ36w-ZKH8rV4iFddrZZrLEhW2KyJQc7Fl-u-uiSxMzxQeJyEnbDT2Uja9C9_Q6NUSl1XLB0AQFNrqomCSJiaG4BKudYJWdxteWkg5l5M3SfOhGo7j_GLLRlTeWg-s_9ci-lnXEOF4ebMc53UsL8X_uH38LfnvS5dp_kaCQfqtahXcw147HxngpVjzvekfOy34pNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RudpsBt146dkPF7UklG9e0u435DOwSHFu4wgV3383OyH2wcW2RogDTs1m7uCynaZTQlbwgsG7Q86hm9Zy_fDwcYPa8wMNmIz2J2ckN81UkXxt6AMUsJNJEzLRP5qktuSzuIY8cTaVT9eyia7aD85Bvcqfxe3LzWPI8LfbM-YpxrHchOi7r7Lpa138X_-qzEAj00qI6k3Mj-ub7kHCqBVQb93lN_8W39amITf46KhlVCLaZvYTXaNBL5zbEmUJy4IlmjN7qFDq5kpzDh7ys9vB4q2zu28G2Y_R7-yNL0tURRdEYv9yGDW6Q84y8QQKCm18WFdRq4-A3nGQTjOaVD2Rg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FtYZLN8G7uMi84uHMifS3Nde8LlTb44bTH4lGovylZqx8OKKITqeL7T4Ho2NOCLotpvdHfeknXA0z_UAypkrwwMbatKUBKR7efWtLkM5X6SrXgo3IrhgLPN0FUBTFspBN7-nlqUoKMIoMjCmx_8qmUAUcHr_1Bk0sBSCr46bIrdy6DYnNLIMhMCAmqdDtFXU7kGGhE8MG-wjmV0bsOGa05toG0ItsH8-BkG9ntLzG5c_d31Bubgx6Tzjq-xnv23sML3zPRbccRdwQpx-kwhctPkCTyPzB1Afz2sb4AciJThmAN-zWDDFplZ287cCoGNtY01m0uwkxl2fLfqG6dTNgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فعلا دسترسی آزاد به اینترنت در متن سخنرانی‌های رییس‌جمهور و هیات دولت برقرار شده!
🤡
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/ircfspace/2324" target="_blank">📅 10:54 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2323">
<div class="tg-post-header">📌 پیام #27</div>
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
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vy7slaH0v2M8EXLeawaZApy5yv-xYQmFgZ0fdTy2PvMIr-qyM8TVQjtds6xZJJ-seIL8wGj0xKqBmUsp_wCTLVFC_k6sJ8K0bFiu5D1ycUltgDKI_KS9ReSTH3lmeS3JQQd5fPMrMNpDKqOJk2X_Hw6IGVY7i7H1rSFtKWZtmJ1WS2si97dCN-bV9-9KEcr_f8AuV0wfIDE5vE1sl1D2FAZ6f2MjmPQGjUOvCnzVqsxJaotWZA1_NevWVMwuMVN_Me8PaJVtVqUbHnEEk4FZ5F3WbKf-G_UVW1WlwIg-O3OHTBCTovLGdkNe9tKmglALoiFBQlNSvhDXp86Dltm7Gw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #25</div>
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
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/ircfspace/2321" target="_blank">📅 08:38 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2320">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/b7AgLYisLKasPbR2O18RPy4tJR38Z9AEYtvaNcbI3Kx-o5G9DsJBRhUx4Y9p2ulFjywGSW_1BTPN6Juu5whIyeSlaZpSnw2-Xk065HBjDcQuuJbmJLg-hgVHUjnMhebqg20MVe9eEcyAFjFd8ZYAg0U3SjBCMNrnR05jqKxnk_GjZR7Rj93ziv5v7hno6AINBWD7tqEj3m0CUJMZkHM26iSXXQTE1p-OKAaPXmxyp-r-amgi8jx4jiuMuCpk38G1od3uT1YaWbVLUfIiK-MvTuHzoEV3IeE_jNKDRlTmTPyOban-Cfo9XP9Ad4ceU39V5Xs8dnfbEZs1w-Obml41Lg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/ircfspace/2320" target="_blank">📅 18:06 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2319">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gg7JKU_Zx1ORxhHYFQKulKt7VZ4QiTUrEqrUGHAs6qlMl5OPseMeyGOc8GxgdrE1QKA-LW0pftZHlJHI7cnoPE_vh-hR3G4FRcvH0eRl3ME8O5t3UEQO90PHXVmJUsGX0rHJVNKTlycDAESGNd5hzMjnFQVNhOAddBfuHGG-BD1-wsUD3n03dj8Zv27I5Ui2hN2-aWp9O8nmVYJOSnSwSSyQFI5EUR038Ld3YwUbw6ofnLqdrUEVoEuMAx81VYRh2ubEU9rtGP-tZliF3sAKmu-gjwMCyl2dXkKMSNlP5vGnq4-3_sL3RFQEYL80Vpin1oO0ckd7GIEy3T8L44IoRg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/ircfspace/2319" target="_blank">📅 17:04 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2318">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/U9pmtEsj6h1REaaEm-1S8avM5u0oCcvi0HVe8ovjgYuLA3D6OT88qhF2XHi62twau_GHN7SdXHamhjb6r_XiwSShG2Z6MaHEgeFMiILHbHochKbITJtshZVJFPxXlS4BHaQxCieI5V2YnUiZfMUl7F1DX5TfUktsAEml53ufxkACCWem5VQ-8c7LwoJSg30IbErcIti_EMm5lkSIYb2QKQ7dk3Pp_o3fAipQZ5t1scUSBheEElBM4E-CLMvak3akvou-iqIYBxEFP_0cj99u5eWzmwBctNMxC9BEINZV2dIuXBOED8HThge43kkW_MrGmWr2z9bTZAVowwKXJkLoLw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/ircfspace/2318" target="_blank">📅 16:35 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2316">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YXZIt9ywpRjOR2L1Nl4Go6IJa-vEaFX7J2DiRtV-hvDbakWlm1JANCuemhKImkxsfUsh95DsOJ6oOhIFIpbLGdM4w5kR7ru3-1ZmgVukQW9IQdKlgTRKzyB1AtqfF1n4YSkEovckkH2FRTBz7HNkHog5WpWn3k8rn9UD4nWyLWTwpCrzIR0Om0dB5Rv3TPa8RojSOsb7XVIIGIbl2g8sAZsHYB9tAeQ05BHWgwz2csfKWUrc0oCVh6W7rQBW4xiA7Dzm8Ov5hLKaeidQjKI_h6qeDk4UFmtCR2al5EKJ95g7kTprUxwewTS0QNgSbD0dR3pnIuecLoBrR7K4Kb7UYQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QcxAGeK_y1fwkWclXeavmarUaYlH8hpCh4B2pYPsgN09HeUdnEl1NAdHaxAwbOOEorjRc_wjQW-CLJwTRq7NcDMHe3FWgapZ9LVYGfu0qVCaX-803EQqup1I865jiRoTi4CT782rCcJnrfJyPSzc0tthn5afIxTqbUyNWpPFzoqZ1ShBOkTz7u3Zb-SCmLK-AYZYf-KbBl0RfDNuD8gytDob47cZOi7UzdmwDntosxNjKjiYEwY4TWRuavF3DFljWR2dpGF3Xe4OIQ2pSTbx9PDh0u6inoLCd26w67smUvZCRBONDCYprIGf9EUCbmtnuvxfPkSWhy_fE0mvMdQ0Kw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/ircfspace/2315" target="_blank">📅 08:55 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2314">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/A0PhEMMDGmGrqpeTUbo0I-HuMQCo_NNzXNzNT83qvSE29G5FpwLsr-OKvdLd3e0zxdLgG5z2C6HG4Zm6N5pPZN9QnXlp4WuEJPXmGxXOLvUCjcfkX8d-BD4Ya9k4Ti1wAcWbnND6q5d3SGoyt3mNshEEPL87Qdq3kHyQPcklInW18BaKzoyqZviBpHUji49ZzcMj-djYTQDTF_OBuHir57dkhcXBPzje4qP1s0prF_yHs5GziG38o7N4XfKzn-VcSQ3tZVXDDlUXpbcn9lT0a1_L4hCAfydw_QJVR-r_MLszzL0nmVclEuFjEzxkm3T2VhhqVfYScKuaC_Z7spB8dg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VKmAOizzBEV_j_aXWHs5BiJ8lKbT2GPUQbJ0lswrgZzVnjm7o5Wp-wBcaU2pCU-ETinX6bfjOURhJgN_zq6vuik3rJoLRPxZKdUbliO2RDZBQhRztaJERtTI_zkk-7Q-ePCn-873fLCEQCOh5gGBN26kgZeXVInIUAVaeinBbzobK5pir_XdoeN25FxDf1MufU_7mqlp-sC2_x79JPgpqijYweoRIiSSRuVT66Y3VaBCHU6iU27q8bOIokUYo4N-ha4K8p4ytROSDSus4wIfM4tnVMYjoDpmmlL2f70IL79OryE4JN0ePBTPdtbh7qKagHFq9mgkRxQDPQp3t5blcA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kIZjyxNXmeJCUqiZwiYyaKVP370Wa0uVpbD-UDjlJAUdxFx0zsTeuPf6TChcdopTu339svO8nMsqUTO2v9gcXWntlpYGMMRp-XTECldzJR2orzjKtJL_wvjiiFi_eTxHb9fsXOsfz6Iq1LCnrUXJT4XHVT-pHCapdhtvmt4fb-XX4CdwQcPVs8Pq8kZuYiti4upTIdt9FaClgjJIW6PwHDq7rLjhJYsd6Uf3YFTs1BDa7C80AHkfqprxU9vDdf0InO1HHgWBeLdNvRFTJ4FqJWHmVocTyIOQmOEIzlRnUYJudNhIw5MbtNe-qf-EKpgQtaZ3Ex-6JALbV8So-omd6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#پیامرسان_بومی
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/ircfspace/2311" target="_blank">📅 21:33 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2310">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ldR16tqwy9dccb5g52fYZSmG0hzgRH40cjhc3RoEfjeHB0y5Wi84opuJuX51JGyEGGOd_SQbxZgdRow9Ya9txt18awO5oVH804jX55HeRP5Imb11ftAuWLGt_9qDD6_chG2FR7Zb5ERM-suJK8FOCi41gEk-S1TzW0I8rXRBFLlYR5ZjYauwwmtLwWz1-904AcgCMjvXpeFIF1DqZY18dhH8FNFPdgHAGPS21QToT5fYL2vE27_CLuU1mAs8uuk-TjR3a03Is0Ks2NKWpBQgLLUxlUus0oRYUi2IKagdS3FzmZinw0bNEKm4hBvO0g5Ao5OoVxRUOt_z2ikvZz-8fA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/ircfspace/2310" target="_blank">📅 21:28 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2309">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">تا الان توی هیچ پستی نگفتم که به پروژه‌هام دونیت کنین، چون حس خوبی به مطرح کردنش نداشتم؛ ولی شرایط همینطور پیش بره احتمالا سر چهارراه نشسته باشم
😂
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/ircfspace/2309" target="_blank">📅 21:25 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2308">
<div class="tg-post-header">📌 پیام #14</div>
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
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/ircfspace/2308" target="_blank">📅 11:45 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2307">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TQXnR7Hf9qM78IKnNo9MB2w83U9G3xkuGFLzJdd7BxbbWAHt1iTT3cWVxxgxMdHXhzG-TNhuD08ZNQmaep1qGWQqI-7BfKBIAZd4x_c2oxBNIaS8SBW9UbF-O-sX5JtecCI5Vzlm2spEc9SaylOTXOREyh0zwujZUnjEM2DQN_gJoXFb2Gf7oj3lSAjWZQYOLH42b9AnjNljzzctXF5ySyXn1PsM45WbVPY1YUQ2kapEPTqYQ3CsZpNTP8772ZVg3qrHcP2YJFh_MNTQx0bqGdy2Cvh3IXsbPHdepB3RjbuD2Hr6oZoy_j_WFdALcLeehKo8saXxr9itdhVtnac0-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون رئیس‌جمهور از وزیر ارتباطات بابت هیچ و پوچ قدردانی میکنه، بعدش همون وزیر از رئیس‌جمهور قدردانی میکنه، بعدترش همین بدردنخورها دسته‌جمعی از مردم قدردانی میکنن؛ اما تهش می‌بینی ۷۳ روزه که اینترنت قطع هست!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/ircfspace/2307" target="_blank">📅 08:13 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2306">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AKvMA6JdkkTESo5OxHBueT45qL93bU9WMFTJlohv_2sIPgF60JduyXXIOxbjxTS54L3oP_ney1e4npjMQyevlyXoT9Y9DdDSAEEy4HXqYZMh22SndZl8YpTCGqYIIWRsFOk-hcYeJzViLf7usSZZEMI-0MsivQzB2WLkcYpQgVtxrj3857wpeLWD-QZp2yOTUuA3h6BcIx5WD8w81_hOCQL5mu6gGH18CPzSUhghX3ZDjA3udcq9JXXT1sf6kkmMHUTZqsACfx9TBjXpqclaZL6_EBgKkePCG4f6IrYy226b4esXaLOukhDB4TNmbTqBadLwZ67EpgFr3UaWNobBAQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/ircfspace/2306" target="_blank">📅 16:30 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2304">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/s_HFQ7ojzfZsAlgJU6Ygf_U5AnyyLizpoesvGP862jnKF2D239qslJilE6rBLB8rlLUqHYV64x30rVPneEX_PluuJc_Zjx4Viqgs21JX4ZnQi0aU7-MxGIPpXdcJm9Tn-5bNdWEIn4KlTZfjNQ6kU3BSpVMuo_h43vhM8xP9rYpw_9dcm3_weBOkwqkGkgVvrWbzRHiAyIsC-__b_sALgE0baKR8oSZCy0trwHUI1gF82mlMYSjocQ4Krjkmoi-xMU8fRtlrhVUX4Nn7VirHNZtb8RCbg0aaQig5zO_RqDIv5lEJrzyEECzoGggW_7i-2pUskHWlnBMwrrtu8ZZgyw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/ircfspace/2304" target="_blank">📅 12:30 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2303">
<div class="tg-post-header">📌 پیام #10</div>
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
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RUYCP-tKlJzSTEaIyVo_bfGCCTupNm-d8qLKWBYL4kOAsoCJU9X4QPnpqStdp3CNEZ8ss-kldwDa3ZVCeKbjoNWKmPy1DhQSVttLy_tg9cVbFiDhNxWNHAlelriM6pMcKfGNXMUW_DFxOgeBAYX-BpoLLQviyS5emnSopNCQWvcwjfeUbcf98IyQHIq2LKNVIlayyCnUZtPQb56kQBKEpC5nfDhFcqsXnIVpKWSU_yYM1qfnHCoHUQL4UhOISGmT1ZVxua28njY3iiboM202VQXmgOdiIBz_LFljMKEU1CxMzTf8OZ1gZMBo1ezQzqzzn8X3TDvfNx8KFmJqsyId7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تسنیم نوشته تنگه هرمز فقط مسیر نفت و کشتی نیست؛ بخش بزرگی از اینترنت و تبادلات مالی دنیا هم از کابل‌های زیردریا رد میشه، که از اونجا عبور می‌کنن. پیشنهاد داده ایران از این مسیر پول و کنترل بیشتری بگیره؛ یعنی برای عبور کابل‌ها مجوز و هزینه تعیین بشه، شرکت‌های بزرگی مثل متا و مایکروسافت مجبور بشن تحت قوانین ایران کار کنن و تعمیر کابل‌ها هم فقط دست شرکت‌های داخلی باشه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/ircfspace/2302" target="_blank">📅 12:17 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2301">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/on_zucaBVoQqxzomgA2c9nGAKwrgUjktCYVL7irDKuGvpAR4Ch8dltCjHW8L5iApnACgdY6LNsNlO3ard_2s-bivb_3WzW04l_eYjC02mSddt7WVeaIljOyi30B_kS8hzkqFcp6zucXWOciOgQfymwbYFViptaRfMtfeCpRWabr8X_Dc0ticO7_9pLOWu8p4PO09oQv-7uEIHRYgpGOGkYgwH0ynm10Fan5xe4GNqwbBOxeJITBY4GE4v8jKgOsYDScgr3CDUF3Of2WRBS3FqncV-u_C9hG5H-AF1YY3g9dhRgjdmQVE3q-45XWH1XfrZHd-lGNbRIv_cKFTLAFv4A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BX_DF6wTEXb48vVfoiw95sOah8gAw-c6f8cz2Bvs-9ZxCQxY0qSekkIcZCFifUO4cS5SQz6EG76S-kmTnf1nJbNNsziqYo9mK6SIFpzrjlSvIZDEX2CjY76XefBcLX1aGzSdVsvwCYVJVzdkl-eXma2WMBrfVKdPkt_XIcej6xhbYE8ky3wXjT5hxxPLil1DNHC3wdZvyasRyh2E8fQLpBaMCnULhDzXK4Z0T_OgMJ041FKMHbX2p9Pftn92faRvbPsGTkCbVJG3XLpEq-DBHJpOvs8EHeKRl5xGAbBucv332EPxvsAHwUU2kjX6YCMmGQXsW7gjFIX_XqbHyVQPDw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #6</div>
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
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qXsgOBjBJ6UkclO2yx30JJD4ksKhKGKOQwdl5shTvXg91UdD09HiqbbTdRKlulUu5QOgIo8PzZ1U1Bn6YelCBtTrjOyO943pglTCbv1ZZRWSXqA80F8-6qaRHHMGugcfhOJIKyrzhz5brGTKuo29ns62GyjCzNgSbnXwao14_n3glzEYSSuaYd_6b78w0QPrkSntIrnuTIblnmHvu_U81cf4LCW2x37DxeWq49teox9mlXUctRT1w-4DTv1va5YH8O4UagH2u9Y6k4rNqf98ZkgAwkmfQmv3yTQiZNOY-CrRHn5MdN4FEk2kAYb-Xr1-pNIlb9tDCO78ZYDeXvertQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #4</div>
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
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/coO5fgeMoqXxYTJy26GUmDHt7QmPjr0F7u6bnec48wJdaxCujqPprXtNpCGDVSfjsV8crpLwgWCnMsCADjAJJDM9BTXGNZah6EooRBAckPxVXWXB15GLi-uCCNIv70RRRsCMSo69jg1hxt5EuUw4iniCBXkZ9Vy_RVBRz0lQQF9LMydnCVIEmPEEZlSSBILapCQAxmQZUKkbTPhqpGapHx9mFEhZOnkMCDtOS9pb50RrY8gMdxFXIjtAhuwLujvaeAPNPfjYKCXmTYkKKy8vz7R5Ah0sCGACKDQtj4QbNzwGy5Y3Tp95HR9EhN5y3eaPgsxlxSWmrW7i3hFR1yTrTQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Wmb9Y-2HIrgofGHej6JDAJSjYVxhJk6ANLsSlxNQCrykKvh0rXpug-XGVVkNVkaysLuboJeLN0HIK_aQCoxazSOlR-kDQa0LcsDDb9EZtHgTLD_vP3tMmcUVerwk_wSqWH3NYg7JSQ8BlGT_NU9xnDY70P0ZLzzMGhtGM2a2PCqYVpi1LLLuEtnue7Sl4QdRN_DsvT97nM4cP0fgVYUl_3polmAooSmNJXz6w_HPvkPu9Jjx8ANOzNMgqeK7MNxW3i6Ck5SX4lKMOeIhyBEDXFXBs0wmu6SP9M8FZzTL3P5GeYnkOfPMMIOTUSCSOfNNkqoIBWl_m_iJ-spvHIIafw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RREO8Mi8aWfhu6xBti1Fka8R3mTzUNEg6B_wpYC1bUi3ve_EC3Wpe5KH9zkFv7qIVgUkXMxPKC9lX_J-AfG49i82pH2UzyRBOGzbNZyTMqVzOU3z5_4ZJ8zVPPyBdqlN-xx7WN0AFLuFEis4PKrOl4gsxZ2TvP23xADvkWSZZkEcMu4Q1ZD-pv48BrE0_5CQEgUT9hQ2DBD7AvaqxIHMk7C4PD9Uyha9wjb26-EQJmGZjI_dY62E_w4vHRe3P-56M2rZNGLphe3n-glpFwN91lYVR2TMVttLOas9Do5gN8Hjr_p6-WwjOfLAR9466COhYOGrxmW0zOHZoedtxaWqcA.jpg" alt="photo" loading="lazy"/></div>
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

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
