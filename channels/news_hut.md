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
<img src="https://cdn4.telesco.pe/file/qv0zHbFY8WTyRl5HgTZnlUKwbG-AfVRELkqLCWAB3zXRVAUCgw81BUV1NhqjpcKdxfK7g3RFj3IGQm9CLEe4io5rvN9KI3kRF0IEonhUtDiN1V63P6PxnBCVvDoyvnWe_3Q8hKkdP06mTszOxfa84PBN5FgIk7B9cRq3JgCj3cLNI-cK0MKqQPoe-Qrd5capcZBMHutNnIgFK3Bop36PLZdls-Mte7CUhzuEbA0dU7qE5Y2hRXe5LhgR1kz6S3LFASkrpJAndUobZzZ6rKraxKKLrWjMeyxwpcGx2KG_XYyz_b9cQBfowkT50Umxp6kI-j5_ayVTAe4FqnokEWrEfQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 112K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-15 16:29:26</div>
<hr>

<div class="tg-post" id="msg-71186">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22246726de.mp4?token=pl96_1ClUtH0GVZDLdPNKbUfEhYFqhy1d5toMKMxlEhqMXZtibzMloN12qAgwp61tZyWjmbyTpH5ibzUOiTJkXSPqkHf25BZCU38izfmTGKFqHqNOMoI6gcF_K7FzQDD27f3QTdqrqcjT21rxnom0YXRhCI3REvG74HZbxwC4uf1G-Yj2LEvm366FwzGwRBjX0pImQlb34JNLHZdwAQvwrc1_IAQTl3-OU2xqgfdYKsVT3nld4PyIt9SVOEhk8dlnD3ppJQgBSmnyp0wUAHvUfMVmgUNNdADJMvLhy9lkoRyeWCNo-w-WAocyAVRxkj6-FkgHUq538RnQt8U2R1rBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22246726de.mp4?token=pl96_1ClUtH0GVZDLdPNKbUfEhYFqhy1d5toMKMxlEhqMXZtibzMloN12qAgwp61tZyWjmbyTpH5ibzUOiTJkXSPqkHf25BZCU38izfmTGKFqHqNOMoI6gcF_K7FzQDD27f3QTdqrqcjT21rxnom0YXRhCI3REvG74HZbxwC4uf1G-Yj2LEvm366FwzGwRBjX0pImQlb34JNLHZdwAQvwrc1_IAQTl3-OU2xqgfdYKsVT3nld4PyIt9SVOEhk8dlnD3ppJQgBSmnyp0wUAHvUfMVmgUNNdADJMvLhy9lkoRyeWCNo-w-WAocyAVRxkj6-FkgHUq538RnQt8U2R1rBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
فیلم وایرال شده از ی دختر ایرانی که با یه پسر مکزیکی با هم وارد رابطه میشن و بعد از ۴ سال بالاخره به هم میرسن و باهم ازدواج میکنن.
@News_Hut</div>
<div class="tg-footer">👁️ 3.92K · <a href="https://t.me/news_hut/71186" target="_blank">📅 16:01 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71185">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KWt1__7W_WkU62DTYn28DTMFhp6qCrU4_HG_aS4YpI87FriX7_VQq3UAF4OtjsngdbuRcIYusvsSViPuQ-wPSjC43KBCbel2pqyyzUFpp61lruQ2MX1vlfikpONkvvF2K4rVI10ApXnXwcdZgrrUlthNCZCxD9sAW6WP790uDXcErUi-Djco6hDlywkMeuRk2WltyBqSawdc-sVGlDrerl2FHrVRyXqQ6JqBv21Q5p_PgnWBYGJsmxrZHj0Cbdj0mBauusxJxVULVIRTUoqD_Azh_I202Wrd4GkLhy-15dsVRbrJa1vo-NKHgmKW0WnvfnhiXQ7IfvNxuyxzRqisSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
دیده شده در تجمعات شبانه:
قالیباف
:
علی الاصول یادت رفت
علی الطاهر هوا رفت
@News_Hut</div>
<div class="tg-footer">👁️ 6.63K · <a href="https://t.me/news_hut/71185" target="_blank">📅 15:30 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71184">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/64baa312ad.mp4?token=tPG1rWT3OEY1Zq_kN7pIjt7FNY4w98i0Ih0UQPCDUhw7q1OrxUq3NyUjxyJPFAvCbvFKtMIal8TSfaFb_2vKGXHqM4tyzsAkOe8O4FEeUBIKaPGKfvOsMcdzuINyhcVOW_EvxpuiI71v7846ETuoc65vOQp27XOqz67iJ2x17qbHgDbAGxA7PJZ0HT3wHr4xlLFzFAlJC4nVgkcQaybiWjD80PqECxzm5OnJmpLejHC63R_lRVO-sE9NxFfjYrJ6HSni9YfUtXyc8EuFYOYmafaoLTlswf2l0i3k5cUgB4HJuRIjaiiNMYG0dnqGPdwWfdIUqqaXnh8qWjDV8Ex4bA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/64baa312ad.mp4?token=tPG1rWT3OEY1Zq_kN7pIjt7FNY4w98i0Ih0UQPCDUhw7q1OrxUq3NyUjxyJPFAvCbvFKtMIal8TSfaFb_2vKGXHqM4tyzsAkOe8O4FEeUBIKaPGKfvOsMcdzuINyhcVOW_EvxpuiI71v7846ETuoc65vOQp27XOqz67iJ2x17qbHgDbAGxA7PJZ0HT3wHr4xlLFzFAlJC4nVgkcQaybiWjD80PqECxzm5OnJmpLejHC63R_lRVO-sE9NxFfjYrJ6HSni9YfUtXyc8EuFYOYmafaoLTlswf2l0i3k5cUgB4HJuRIjaiiNMYG0dnqGPdwWfdIUqqaXnh8qWjDV8Ex4bA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این ویدیو درباره یکی از جنبه‌های سختی مرد بودن در حال وایرال شدنه:
@News_Hut</div>
<div class="tg-footer">👁️ 8.39K · <a href="https://t.me/news_hut/71184" target="_blank">📅 15:05 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71183">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c325a7591.mp4?token=rBa6RFTmZ7g-6k3yAY-pgURNReHR3_VxDVg8QCpR_2fGPxlKq5UX81Ko4oDDinxupZUC8VK30ul_NbI5ecDhKkrnHGbCHwp1Lur-_KWjrTzlYfaB-85p0sndhUn-MeSBDdW_ZhwADf57LyGal2ppXpy-h2a7dYNM2b5D0j2WeVn_wJpx4jCd1m8Xn4UoE2HNG1YknmXBKLiwdRCz480kRB6EzrLFHBj12-MQ3ZC5RExXq2ZE1TUAG9WM5P7DU1yTTVHKwzV53a2T-IbyoHdIQ72DZxFvMlRqo-jocjNwurUkPaa-9dqKMBczBtDwdszDNgSvV8xlgx3uCHc0g5oznoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c325a7591.mp4?token=rBa6RFTmZ7g-6k3yAY-pgURNReHR3_VxDVg8QCpR_2fGPxlKq5UX81Ko4oDDinxupZUC8VK30ul_NbI5ecDhKkrnHGbCHwp1Lur-_KWjrTzlYfaB-85p0sndhUn-MeSBDdW_ZhwADf57LyGal2ppXpy-h2a7dYNM2b5D0j2WeVn_wJpx4jCd1m8Xn4UoE2HNG1YknmXBKLiwdRCz480kRB6EzrLFHBj12-MQ3ZC5RExXq2ZE1TUAG9WM5P7DU1yTTVHKwzV53a2T-IbyoHdIQ72DZxFvMlRqo-jocjNwurUkPaa-9dqKMBczBtDwdszDNgSvV8xlgx3uCHc0g5oznoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
مراد ویسی درباره مسعود پزشکیان:
حساب اینو نکنید این متخصص قلبه. از نظر سواد اجتماعی یه آدم به شدت پرتیه پزشکیان.
گفته کارمند‌های دولتو داریم صحبت می‌کنیم در سراسر شهرها، نیان تو شهرها. مثلاً اگر کارمند بانک‌اند اولین بانکی که اونجا هستن برن تو بانک بشینن کار کنن. اگر کارمند تامین اجتماعی‌اند اولین شعبه تامین اجتماعی که هست برن اونجا کار کنن
😟
گفته دو میلیون خودرو میاد کارمند ما اگر یه میلیون از این کارمندها رو بگیم روزانه نیان سر کار تعطیل کنیم اداره رو یا بگیم اولین اداره‌ای که می‌بینن برن اونجا بشینن کار کنن.
گفته یه میلیون خودرو هرکدوم روزی بیست لیتر مصرف می‌کنن یه میلیون ضربدر بیست لیتر می‌شه بیست میلیون لیتر مسئله بنزین حل می‌شه
🧠
@News_Hut</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/news_hut/71183" target="_blank">📅 14:32 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71181">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c318eb355.mp4?token=syVL68JNC_ZP5TAsB1MUGepEiYmgLKMm6NTC9gZ5yb2QOmjI_Yt9I4JmzEygSRKO3uiDcfcRK_QhaAfMKcCszMo4L_36i-wa7c3dMHEzJTyFK4vMTQjS1kzYAysJWWB45hTFPp2T184-n0izOChpjVRY3fH7aKhrQSbv6SCyI0-tjZjGO2C7K8S8mLfmIRshMkS31Jr-YqEOMJ05eBggwxRw5TH0KwZpwoAMb9cFWcvKUdGjgWqfN9N9_jV9b9nvFBaTTGo0r-QvCUKEx6AB-zYG-YUJrC44rx642MPPBjKZzJOXP1oHjOL6dJys_Sx1EEvjm0p3XvDYiWdNTHjqng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c318eb355.mp4?token=syVL68JNC_ZP5TAsB1MUGepEiYmgLKMm6NTC9gZ5yb2QOmjI_Yt9I4JmzEygSRKO3uiDcfcRK_QhaAfMKcCszMo4L_36i-wa7c3dMHEzJTyFK4vMTQjS1kzYAysJWWB45hTFPp2T184-n0izOChpjVRY3fH7aKhrQSbv6SCyI0-tjZjGO2C7K8S8mLfmIRshMkS31Jr-YqEOMJ05eBggwxRw5TH0KwZpwoAMb9cFWcvKUdGjgWqfN9N9_jV9b9nvFBaTTGo0r-QvCUKEx6AB-zYG-YUJrC44rx642MPPBjKZzJOXP1oHjOL6dJys_Sx1EEvjm0p3XvDYiWdNTHjqng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇹🇭
〰️
ناو هواپیمابر «یو‌اس‌اس آبراهام لینکلن» (CVN-72) اسکله C-0 در بندر «لائم چابانگ» واقع در استان چونبوری تایلند را ترک کرد و مسیر خود را در عرض اقیانوس آرام به سوی پایگاه اصلی‌اش در سن‌دیگو در پیش گرفت.
خروج این ناو در صبح روز ۶ سپتامبر، به توقفِ حدوداً چهارروزه‌ای که از ۲ سپتامبر آغاز شده بود پایان داد و مرحله بعدیِ مسیر بازگشت آن به ایالات متحده را رقم زد.
@News_Hut</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/news_hut/71181" target="_blank">📅 13:54 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71180">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/003437fd92.mp4?token=UDHpKZ6wUlhBD7tD_maHAlXPASJg9r4qrKJCB5DNvD6tf0HXXG5AHLxXZ4dcxHKFH8RuYTwSOuxmVF90tbO_gU9Jh0q1sWebDfZ_EQ2w4F9X-Z_wOWNMr6pZcH-wFGm_qfIfInn7C5kRCfDnf8gNFy34kvLyhVk5FtW7l-Ls7rbyckvtGkLf39nmqJJaoAUCwmhMGwlDcTYTMz22ukTyp7S0HkJ9VJdjLXWbxmSAs8Osu0cBkuhQhOJjW5yjdGojtb1xna3trJJ2jb5oIzUnl9gQ7bSBztfyHs3fYdaao9xZFGEc-MAd_L6kFKBKH7xF11Xp_NDZZan7VQjnDM3rFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/003437fd92.mp4?token=UDHpKZ6wUlhBD7tD_maHAlXPASJg9r4qrKJCB5DNvD6tf0HXXG5AHLxXZ4dcxHKFH8RuYTwSOuxmVF90tbO_gU9Jh0q1sWebDfZ_EQ2w4F9X-Z_wOWNMr6pZcH-wFGm_qfIfInn7C5kRCfDnf8gNFy34kvLyhVk5FtW7l-Ls7rbyckvtGkLf39nmqJJaoAUCwmhMGwlDcTYTMz22ukTyp7S0HkJ9VJdjLXWbxmSAs8Osu0cBkuhQhOJjW5yjdGojtb1xna3trJJ2jb5oIzUnl9gQ7bSBztfyHs3fYdaao9xZFGEc-MAd_L6kFKBKH7xF11Xp_NDZZan7VQjnDM3rFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
توی ایتا و روبیکا، ناو جرالد فورد رو بمبارون و غرق کردن
@News_Hut</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/news_hut/71180" target="_blank">📅 13:53 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71179">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71179" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/news_hut/71179" target="_blank">📅 13:52 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71178">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jLa0BzHCsWqzoE6Gn_zylpf7gzWlm-DekfxB34mEqIgP5AkEQiUZOiIhSb14XC8KzMmhqPAYgP1NCqLJvK4m-WnUdW_b_l-Jw8gGQ4Sl_glY0viZb6ljgk2nA8K5WrNu9f3UsME5FybQsMgNMDg40DicctNrI-w336fj5rD_2P-msAJe-rJN8fNPIO0IdYt3GRo9QLvVJ1Y9Hbm0Rd5guY7x7xEvDJm-A7L08BeHc5KJH1qxoXQRofFzYXVB-rPEO97-VqgJFrYu-ELhhHpqgDbI69pIMMyztbZ1we_N6kliVynm2QlINZdnviaEVb7cF2LVEu3DICi8syQ9tmNjSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت بین‌المللی
TrexBet
پیش‌بینی کنید
.
اورتون
🆚
منچستریونایتد
آرسنال
🆚
چلسی
آلومینیوم
🆚
استقلال
والنسیا
🆚
بارسلونا
یوونتوس
🆚
میلان
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز و برداشت آسان و امن
انتخابت رو انجام بده و آماده‌ی هیجان باش!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/news_hut/71178" target="_blank">📅 13:52 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71177">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3c6743716.mp4?token=shWpq0Fh8vbfMc6EF2zUmmSV2Dd5iDHwPsDg89bu6SfSkFddaMgmx4FgUaM8wTnH5Ruyk7RxOAuPLjW3fknFuHiFH6_Tg320jds5gy1lU4_0X3iM4WRFQMz_7sUTyoUj45RzdyA8lekm4o-4ya4h23GZlb0iVpIKVIsw7A9ee5JOo_hKZHGngc5gSRnlwNzp2fDbj_J2Yf6gS_E1-P0MuDmQbadCcW4GD8hbQW5gsY44x5kwwLg1xy4uennQut9OSrl5nWeK6Ijk1DmVUG0C1uR760lTPNmE6tDnX6Tv2ZN2Se5JOEYSzQKSrRkqdXQZQXwTP491OSFInvqnoBtdjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3c6743716.mp4?token=shWpq0Fh8vbfMc6EF2zUmmSV2Dd5iDHwPsDg89bu6SfSkFddaMgmx4FgUaM8wTnH5Ruyk7RxOAuPLjW3fknFuHiFH6_Tg320jds5gy1lU4_0X3iM4WRFQMz_7sUTyoUj45RzdyA8lekm4o-4ya4h23GZlb0iVpIKVIsw7A9ee5JOo_hKZHGngc5gSRnlwNzp2fDbj_J2Yf6gS_E1-P0MuDmQbadCcW4GD8hbQW5gsY44x5kwwLg1xy4uennQut9OSrl5nWeK6Ijk1DmVUG0C1uR760lTPNmE6tDnX6Tv2ZN2Se5JOEYSzQKSrRkqdXQZQXwTP491OSFInvqnoBtdjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">〰️
سنتکام ویدئو غرق شدن نفتکش ایرانی در دریای عمان را منتشر کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/news_hut/71177" target="_blank">📅 13:12 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71176">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">⏺
🇮🇷
قالیباف:
آمریکایی‌ها باید دریافته باشند که دوران «پاسخ‌های متناسب» به سر آمده است.
حملات ما به پایگاه‌های متجاوزان تنها یک آغاز بود.
قواعد بازی تغییر کرده است.
از این پس، هرگونه تجاوز به منافع ایران، پاسخی سریع‌تر، سنگین‌تر و دردناک‌تر در پی خواهد داشت.
@News_Hut</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/news_hut/71176" target="_blank">📅 12:44 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71175">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20d5a31326.mp4?token=WCIXwXYIV44dZKFF2JrKc9M2-RlRHijOUKcYtSUo_WnpHuSGopy4ippSXLhaoCUn4NiPQxSflbWU_GygXJFXjpxCUjsGcy4SMu3RC1ghyX8q6sX6OI0NG8chXcq0VtKR942bmly4Rn6nZ7Atb4bmREHy3DrAw-utVMdvnbo9tKchjyHrjykkCVgFiB5zdDG390Te_vUlUjvPAHYsiH8G5DjWHTEtVQENy_XZopuDOTNK9R5yWQNbkXmtVmCgcdD6ehYK5_JIWtEHj_197cHufcdogWGQfO7mUAKcTOyk6kJeDpCOL45sKomCvUNf0ly3JtSLUuxjo6hGkiSMFMDRvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20d5a31326.mp4?token=WCIXwXYIV44dZKFF2JrKc9M2-RlRHijOUKcYtSUo_WnpHuSGopy4ippSXLhaoCUn4NiPQxSflbWU_GygXJFXjpxCUjsGcy4SMu3RC1ghyX8q6sX6OI0NG8chXcq0VtKR942bmly4Rn6nZ7Atb4bmREHy3DrAw-utVMdvnbo9tKchjyHrjykkCVgFiB5zdDG390Te_vUlUjvPAHYsiH8G5DjWHTEtVQENy_XZopuDOTNK9R5yWQNbkXmtVmCgcdD6ehYK5_JIWtEHj_197cHufcdogWGQfO7mUAKcTOyk6kJeDpCOL45sKomCvUNf0ly3JtSLUuxjo6hGkiSMFMDRvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
قالیباف:بستن تنگه هرمز به ضرر ایران شد.
@News_Hut</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/news_hut/71175" target="_blank">📅 12:01 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71174">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8313313bb.mp4?token=ZUzxWwEX2OLx-zL_HXxLo_ha3OPUDSeaLhkLrxTv2x3CRHkZojQmwtqTQZH_saVVcpt5BnCTEylAlPgkzIEFfF-Litp_aNo3lHv6PLejoQUQg1yrjRgsWnu3GGZdEhRR19Pz0wEriFRVug5XG3z-L0dlpWJq9HiBFUjJ0gNdsf0Y4TvY4sAmNEOVkXxgWLPvCG0xHuBlLWj1ieEvisUuJCp3RqryCWZX3dhST4j--oxUKhNMc0FxIo2xw8hge6ML_knC-CBUDqu_tn4-L4UVu3EEizgS_o9bZgMs5a-4qvOvmbItPjOPinyXI1RAZVGJdMAgG4cYXTKhxMXejeqWPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8313313bb.mp4?token=ZUzxWwEX2OLx-zL_HXxLo_ha3OPUDSeaLhkLrxTv2x3CRHkZojQmwtqTQZH_saVVcpt5BnCTEylAlPgkzIEFfF-Litp_aNo3lHv6PLejoQUQg1yrjRgsWnu3GGZdEhRR19Pz0wEriFRVug5XG3z-L0dlpWJq9HiBFUjJ0gNdsf0Y4TvY4sAmNEOVkXxgWLPvCG0xHuBlLWj1ieEvisUuJCp3RqryCWZX3dhST4j--oxUKhNMc0FxIo2xw8hge6ML_knC-CBUDqu_tn4-L4UVu3EEizgS_o9bZgMs5a-4qvOvmbItPjOPinyXI1RAZVGJdMAgG4cYXTKhxMXejeqWPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">〰️
ویدیویی که در توییتر فارسی به شدت در حال وایرال شدنه
😃
@News_Hut</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/news_hut/71174" target="_blank">📅 11:31 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71173">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f8295abc0.mp4?token=gQ9Ch83aKMeFIeq0KSbrrYARWxMRdcfkiGc-eShUCxqcEx3wRHky-EzlA-nO4Ff-8QwClcsoBrNETN4sxjgkjtH6eJX8L_HwOquvIQN9AYjnTtc0KMhB-l3vkUbVjiQ-UkK9_4f1HvdYKXWQiWrica3ShbJUfwOoqFE_prwbq2J5WDU0jzKuw8b4y0d894QXYb-UdHFIJXE4_q3hjjBpo8sKoiDUY79SpfOuSpWpbBFLIAmuUhYqb3PuYX1VdTcAPsjqlBWCXECjE0n_-zFD_J2fiU23rASQ24Zil6aNrcnXLlcj3nDwZNKxaHGohGXYDpMFsBzvC3PPT7aO52m7bg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f8295abc0.mp4?token=gQ9Ch83aKMeFIeq0KSbrrYARWxMRdcfkiGc-eShUCxqcEx3wRHky-EzlA-nO4Ff-8QwClcsoBrNETN4sxjgkjtH6eJX8L_HwOquvIQN9AYjnTtc0KMhB-l3vkUbVjiQ-UkK9_4f1HvdYKXWQiWrica3ShbJUfwOoqFE_prwbq2J5WDU0jzKuw8b4y0d894QXYb-UdHFIJXE4_q3hjjBpo8sKoiDUY79SpfOuSpWpbBFLIAmuUhYqb3PuYX1VdTcAPsjqlBWCXECjE0n_-zFD_J2fiU23rASQ24Zil6aNrcnXLlcj3nDwZNKxaHGohGXYDpMFsBzvC3PPT7aO52m7bg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
به گفته آقای دکتر اگه می‌خوای سرطان پروستات نگیری، باید ماهی ۲۱ بار سکس کنی...!
@News_Hut</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/news_hut/71173" target="_blank">📅 11:02 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71172">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b321711db4.mp4?token=t7IN4Ae5hSlzneuLiJPVjiyNhoSN0UYCvRy459E9f3vn5lmn4ibmkODbiGuvtgKEv7yzVZPYgrrzLRJuF63oMDBnLuh_tX2KLw7AMzhWQqcV8PBifhhclOPO2O57cZ1AYgeuNGIn6jpObWD3ucBDnvq6lHBHaJqxkmWRtmBPjO7BFrXHyRJ8NdHNLnWQc-FzRXJ_2andnd8R4SddLkudCA-2Q6g_HTgdo6sSKocI4lLLpwBP5dWCLXu_5jq41M44Gm3T5KNVE_DLYYqP81eeNTqXJ2eAJLHtKtofQtEUIUHfsReq2fSpuE7-kAIbZEvaNO4pxEMplyzBOEdjb8ERWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b321711db4.mp4?token=t7IN4Ae5hSlzneuLiJPVjiyNhoSN0UYCvRy459E9f3vn5lmn4ibmkODbiGuvtgKEv7yzVZPYgrrzLRJuF63oMDBnLuh_tX2KLw7AMzhWQqcV8PBifhhclOPO2O57cZ1AYgeuNGIn6jpObWD3ucBDnvq6lHBHaJqxkmWRtmBPjO7BFrXHyRJ8NdHNLnWQc-FzRXJ_2andnd8R4SddLkudCA-2Q6g_HTgdo6sSKocI4lLLpwBP5dWCLXu_5jq41M44Gm3T5KNVE_DLYYqP81eeNTqXJ2eAJLHtKtofQtEUIUHfsReq2fSpuE7-kAIbZEvaNO4pxEMplyzBOEdjb8ERWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
🇹🇷
این پسر بچه ارومیه ای که چند وقت پیش با ویدیوش که در حال آهنگ خوندن بود توی اینستاگرام به شدت وایرال شد حالا یه کمپانی بزرگ از ترکیه اومده و باهاش قرارداد همکاری بسته؛
فعلا این قرارداد واسه اجرای کنسرت های مختلف تو ترکیه‌ست
رئیس کمپانی میگه که این تازه اول راهه و قراره بزودی تو سراسر جهان کنسرت برگزار کنیم...
@News_Hut</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/71172" target="_blank">📅 10:31 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71171">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99e529d142.mp4?token=FUSmnnKaODjdZG6SGjp8GiHyCYHxPq9nuGNFC9j8PtnFKa-OEamnJPimog4yQo0kxxdP8RI0sbr71YX--rKXwPTCtq7USq6sPlivqpdp-hqPtNwmMNaVBDTlXpv7EczHCkEjMIrum0k7NcTI-Ajwsx1gzhYNxuoAEA9WedEtIVfHmxxCKswBMTQQFuedoUO3Ds800IYSTqYa4jtQ1m4i9V3hYdzO-zrhzk_vMZYotQmmJKMG85jCVb5InHe0DVcMITWb0BhilkvMiP7bu_hxvosu01ZKlwaj4LdajDmSI9W-1fty3eZUeFz0zRgZsal9Dr6eP71-SV1lBTJ7sjR4sA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99e529d142.mp4?token=FUSmnnKaODjdZG6SGjp8GiHyCYHxPq9nuGNFC9j8PtnFKa-OEamnJPimog4yQo0kxxdP8RI0sbr71YX--rKXwPTCtq7USq6sPlivqpdp-hqPtNwmMNaVBDTlXpv7EczHCkEjMIrum0k7NcTI-Ajwsx1gzhYNxuoAEA9WedEtIVfHmxxCKswBMTQQFuedoUO3Ds800IYSTqYa4jtQ1m4i9V3hYdzO-zrhzk_vMZYotQmmJKMG85jCVb5InHe0DVcMITWb0BhilkvMiP7bu_hxvosu01ZKlwaj4LdajDmSI9W-1fty3eZUeFz0zRgZsal9Dr6eP71-SV1lBTJ7sjR4sA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇱🇧
🇱🇧
خبرنگار جمهوری اسلامی در لبنان:
اعضای سپاه پاسداران در تپه‌های علی‌الطاهر، به دلیل محاصره اسرائیل، در شرایط عاشورایی قرار دارن.
@News_Hut</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/71171" target="_blank">📅 10:04 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71170">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a662811c73.mp4?token=DknzSltuync5bBFkTl5BxKGUpDnZ1cO9e3yiH-hWc_00NrQJRqY7YQo3B8Wv3OwiFs9Z4HmfDoecbS5kQRDHhQpG5zslbj7Zgr3-bBdte0bIZVUiqwV-Pwtn2hAiD8hGgxTB46i0ldpUWV9zVION219411ucyTHbbSfApghn4MNCoxEzJRtEbLof5alZAKNN2GY9QeQHPjWImvohYvkK1Ck83QCDT1kKvV2XA3ny-iNqJDvq3rEsHeC-IjMpiky2gC8zvQPcDjtNxAvi0u5tQWy2N52F-kU9J3mnpIgV2ISxlDIiBbvgeHJi2qUof_s45-knmdFNmpIlLElI86Ah1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a662811c73.mp4?token=DknzSltuync5bBFkTl5BxKGUpDnZ1cO9e3yiH-hWc_00NrQJRqY7YQo3B8Wv3OwiFs9Z4HmfDoecbS5kQRDHhQpG5zslbj7Zgr3-bBdte0bIZVUiqwV-Pwtn2hAiD8hGgxTB46i0ldpUWV9zVION219411ucyTHbbSfApghn4MNCoxEzJRtEbLof5alZAKNN2GY9QeQHPjWImvohYvkK1Ck83QCDT1kKvV2XA3ny-iNqJDvq3rEsHeC-IjMpiky2gC8zvQPcDjtNxAvi0u5tQWy2N52F-kU9J3mnpIgV2ISxlDIiBbvgeHJi2qUof_s45-knmdFNmpIlLElI86Ah1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
شاهین نجفی:
هرکسی رضا پهلوی رو مورد انتقادهای عجیب غریب قرار میده و میزنتش یه سرش وصل میشه به جمهوری اسلامی
اینا جوگیر شدن چهارتا شعار دادن و حرف زدن بعد دیدن اینجا خبری از سهم دهی به کسی نیست مسیرشون رو عوض کردن
@News_Hut</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/71170" target="_blank">📅 09:33 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71169">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2d150aea8.mp4?token=GN-74MSeoqDpq0cAtAkdEtuOWsMiS1M_Umxju9KkZaywSPpdCv30QciYT1zXbxd-K5sVPad6CjbQyJgU6q08NeT62admDTovs1rViVQ1hopw1sWLL1E6X3T-XMuFmZSTFdM-ZrJqRDgkjHl30bvtulOaT6gSVC3Gk7SZB0hyt2WZe3ZvrY5LLWKVIa4OS-U01j1lIH7oLR3bWtNTY6qMOKk58wCxQipiwEU3jFJUu5O4uLV8ugHovlK7KuiX_f6w7HOSzW80NsQH8RD_yW7pOJ8FqC4lwuYhrTqzocXJS1foEQSQWjVuF2h9dDmDiEKI59SVgY1xR9f8khupZTLzGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2d150aea8.mp4?token=GN-74MSeoqDpq0cAtAkdEtuOWsMiS1M_Umxju9KkZaywSPpdCv30QciYT1zXbxd-K5sVPad6CjbQyJgU6q08NeT62admDTovs1rViVQ1hopw1sWLL1E6X3T-XMuFmZSTFdM-ZrJqRDgkjHl30bvtulOaT6gSVC3Gk7SZB0hyt2WZe3ZvrY5LLWKVIa4OS-U01j1lIH7oLR3bWtNTY6qMOKk58wCxQipiwEU3jFJUu5O4uLV8ugHovlK7KuiX_f6w7HOSzW80NsQH8RD_yW7pOJ8FqC4lwuYhrTqzocXJS1foEQSQWjVuF2h9dDmDiEKI59SVgY1xR9f8khupZTLzGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
صداوسیما آمار رسمی کشته شدگان اسرائیل تو سه روز اول جنگ رو منتشر کرد:
۶عدد ژنرال ارشد اسرائیلی
۳۲ نفر مامور موساد و ۷۸ نفر مامور شین بت
یازده دانشمند هسته‌ای
۱۹۸ نفر افسر نیروی هوایی
۴۶۲ سرباز و ۴۲۳ نیروی ذخیره ارتش اسرائیل کشته شدند
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/71169" target="_blank">📅 09:01 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71168">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
🇺🇸
🇮🇷
سپاه پاسداران انقلاب اسلامی ساعاتی قبل در بیانیه ای مدعی حمله به یک ناو هواپیمابر و یک ناوشکن آمریکایی شد و اعلام کرد که پس از این حمله اونا خسارت دیدن، ترسیدن و از منطقه فرار کردن.
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/71168" target="_blank">📅 08:02 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71167">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71167" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/71167" target="_blank">📅 01:34 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71166">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MjIEiUMi_KBmioT68QbN53CbczX2ygQJcZK0IYg6jwA-OE3IwmjFqC7D9ozQMqxjR5YVrY9hqAHYJhDluZUEx8N4W-oJ45JWsIaxW1HtTzp6QVTXWI70UIiaKGx2PuVSnxhNzONBfm8i0bT6j4j38YHCOsBvn5qCVS9mM6q4Dfd-JWkiELsWe2U2DnVR-89bCnQ1SbZHY_faSLQcLu5Be_RYunfiw0t-5l1e0GuungRjaKPULQfSz-LrVjCQFFtbZdIVxJcIKAQF58Ms3rTRAP67CgDYh3klVWyKUOZ8InscC6UWMeXUp6lzAfM8wdDS4Z1tfkfC8UMwovnFTqg-yQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
تنیس US Open داغ‌تر از همیشه دنبال میشه!
🦖
مسابقات جذاب
US Open
رو در
TrexBet
پیش‌بینی کنید، هیجان رقابت‌ها رو بیشتر کنید و برای جوایز جذاب وارد رقابت بشید!
🦖
فرصت هیجان
US Open
رو از دست ندید!
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/71166" target="_blank">📅 01:34 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71165">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">ویس فحاشی خداداد</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/news_hut/71165" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🚨
🚫
فوتبال مملکت هم اوضاع جالبی داره.  خداداد عزیزی امشب کلش فوق‌العاده کیری شده و اینجوری خواهر و مادر امید عالیشاه رو به فوش کشیده
😳
😳
😳
😳
😳
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/71165" target="_blank">📅 01:04 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71163">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c0f365bbb.mp4?token=HFSs3dGd6bngEWuIT2bNXKegGQaheh-VsdXVedqBNconeR_KtKOasDRyQAlory9z4j3Knh4JpHhKR1p5LX0M7xAFMJnqvdtfimTLsdSNhpWwyQ2NHG_vv5vieR5lK_I4uVaBP_HivEyCJc9knEZJyWXFJbOOn_3CSX36qYCEE7rbISu8ummj0tyDeh7LB1httAuxECQ6zNVkbLNs27ZPc7deYH87ysYdsFBUgrOQfMvmAZEdCFDniAfmeTJdNvtsi0JrWQCkFdxAoLVHdVqVtlXm1XnHCEJfWl29ydv8xw3mIRNCW4HLtvIopErVA9iFSDMCpSjV2raQ4IKij9LArw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c0f365bbb.mp4?token=HFSs3dGd6bngEWuIT2bNXKegGQaheh-VsdXVedqBNconeR_KtKOasDRyQAlory9z4j3Knh4JpHhKR1p5LX0M7xAFMJnqvdtfimTLsdSNhpWwyQ2NHG_vv5vieR5lK_I4uVaBP_HivEyCJc9knEZJyWXFJbOOn_3CSX36qYCEE7rbISu8ummj0tyDeh7LB1httAuxECQ6zNVkbLNs27ZPc7deYH87ysYdsFBUgrOQfMvmAZEdCFDniAfmeTJdNvtsi0JrWQCkFdxAoLVHdVqVtlXm1XnHCEJfWl29ydv8xw3mIRNCW4HLtvIopErVA9iFSDMCpSjV2raQ4IKij9LArw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
سپاه پاسداران تصاویری از «رصد و رهگیری شناورهای متخلف» در تنگه هرمز منتشر کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/71163" target="_blank">📅 00:38 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71162">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e9440ae83.mp4?token=Zt0ZlwM-HnP-jrZE2H_kLkUw3351WDrqVoIOVD1tbeUDclGejT7FucNGzqQvmmyQlrS6xZUi1lQgrgFQ7u1PVZSANTKllxPpDP34UCot20rapqxooxyBQW8hLg52pGPyEeggHfbV0-AnXtPLqseQgvXxjVUGpg-tFjXur5R1Wj0cSLJ3KEBQozUzBI99K4rQp7cXSC_gKN8R1n4feBvZCquqLfs708gZqXGmNVxWLca3h2jEl1yIVzaWvP42M_riUz-HTsSuER1avcbG0IBmYkNTbcgNtbbDMp06q2kQwoDG0KsGlgdoh8zm7J35pLxodl75Q8tFXColvAD5WUimzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e9440ae83.mp4?token=Zt0ZlwM-HnP-jrZE2H_kLkUw3351WDrqVoIOVD1tbeUDclGejT7FucNGzqQvmmyQlrS6xZUi1lQgrgFQ7u1PVZSANTKllxPpDP34UCot20rapqxooxyBQW8hLg52pGPyEeggHfbV0-AnXtPLqseQgvXxjVUGpg-tFjXur5R1Wj0cSLJ3KEBQozUzBI99K4rQp7cXSC_gKN8R1n4feBvZCquqLfs708gZqXGmNVxWLca3h2jEl1yIVzaWvP42M_riUz-HTsSuER1avcbG0IBmYkNTbcgNtbbDMp06q2kQwoDG0KsGlgdoh8zm7J35pLxodl75Q8tFXColvAD5WUimzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇬🇷
یک فروند جنگنده F-4 فانتوم نیروی هوایی یونان در جریان رویداد «هفته پرواز آتن» در پایگاه هوایی تاناگرا سقوط کرد و دو خلبان این جنگنده کشته شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/71162" target="_blank">📅 00:14 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71161">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a02f1d06a.mp4?token=Iq7Fq64UmkQ0kMHXXmByWltp5XaNcbfx7ZG9uSliOkmTwR_ijztkXQkE24oVOREZQkAGkeCfVmcC0fStT0C3f6I6N8CvZwScJ5FbyF3mjQB-ANpffvcbzIoWbfmNzv083tUq8MxF0oriy3fd7e4qQxtaNEps4YvkhCsMEojmIj8xYv6Q_4Jy-uXZfCF--9I6PGpO7VnPB1Dou0FsG70iEtIGUTbyxozdejfzSbD6Nt0YbPkh-DmFwA9QJw0948MhWgS5w3-LHv0i8A-O_qKma4Ov9YhVQ91SWPC4sBwm-igkoBtlABVKDiqLBsE0OZUzyDYAXjOK13fRSMTY2wGghg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a02f1d06a.mp4?token=Iq7Fq64UmkQ0kMHXXmByWltp5XaNcbfx7ZG9uSliOkmTwR_ijztkXQkE24oVOREZQkAGkeCfVmcC0fStT0C3f6I6N8CvZwScJ5FbyF3mjQB-ANpffvcbzIoWbfmNzv083tUq8MxF0oriy3fd7e4qQxtaNEps4YvkhCsMEojmIj8xYv6Q_4Jy-uXZfCF--9I6PGpO7VnPB1Dou0FsG70iEtIGUTbyxozdejfzSbD6Nt0YbPkh-DmFwA9QJw0948MhWgS5w3-LHv0i8A-O_qKma4Ov9YhVQ91SWPC4sBwm-igkoBtlABVKDiqLBsE0OZUzyDYAXjOK13fRSMTY2wGghg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
یه خانم درباره اقتصاد:
چرا مردم هر چی گرون میشه از زاویه ی آدمای متوسط بهش نگاه می‌کنن؟
خونه از ۵ میلیارد شده ۵۰ میلیارد.
گوشت از ۵۰۰ تومن شده ۴ میلیون.
سود شما چند برابر شده.
مردم از گرونیا دارن سود میکنن، مردم باید دیدگاهشون از آدمای متوسط جامعه تغییر بدن و بگن هر چی گرون میشه خب ما هم سودمونو داریم میبریم
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/71161" target="_blank">📅 23:32 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71160">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2d7d2ec60.mp4?token=TPYLHapmj58bopj7U7dqfn3r_jLTq2QLGL1RGd2EASGp1vnxtQGVo8EWW2VLyuXExUTAx8wgU2IRL7EG_N4-xXljKPg4dl0Ly_2_fXOSFNyZCQiSy-08aZYQrofNVIxRzG4IdGeZD8P8ENjP7AjSAk_5Gqy73fF7_9aom3-k9uxD1fPkL-MCkcR7v-OZyxLNGSgQHnnM78h8znk5hn4CjEnkTCu8YSqxryMX0o-IbIAk8LTYPh34LA-NtYEFnvnZYWyI3x7P_5HtaGZxvCB9Lh-rKZ_votWRUUZ4zhPHQ83g5D5-qKIBWRFNVAIomH1_6dQHBtPpvH9KkVbtM21rlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2d7d2ec60.mp4?token=TPYLHapmj58bopj7U7dqfn3r_jLTq2QLGL1RGd2EASGp1vnxtQGVo8EWW2VLyuXExUTAx8wgU2IRL7EG_N4-xXljKPg4dl0Ly_2_fXOSFNyZCQiSy-08aZYQrofNVIxRzG4IdGeZD8P8ENjP7AjSAk_5Gqy73fF7_9aom3-k9uxD1fPkL-MCkcR7v-OZyxLNGSgQHnnM78h8znk5hn4CjEnkTCu8YSqxryMX0o-IbIAk8LTYPh34LA-NtYEFnvnZYWyI3x7P_5HtaGZxvCB9Lh-rKZ_votWRUUZ4zhPHQ83g5D5-qKIBWRFNVAIomH1_6dQHBtPpvH9KkVbtM21rlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه جانفدای رندوم و حرکات جالبش
😃
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/71160" target="_blank">📅 22:54 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71159">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/66b1ca1096.mp4?token=J9XGSR6DZAuy_txhEj47TlS8D5JCUCjHFUL1C1yWkuGODRxrNrxoBULIOtQcnAqLrXW2RKbZFvvB8M8YpOiZuuM19NrXRzrk7l9zybscI__nIZYFuYL5PCo9-Emt2zNtxCnk-ZVz0DiEFDGy7ZkGLoc7im31C086Okc49iBJeFoEIDCoj73l_3f9MuqA8T6ADRPQitqH3eDCWYYYhhpdxlE3Np5644qlWwS30lyQeYpBO39TGa3TWecAhZCO7kiz15pUWbM3e_PQ-aMWeY1XiypEzN0h6KI2JVnf_ndfioE0gu60018JOipu38y3J99P216oFZmAsqKhWaIJXnFYYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/66b1ca1096.mp4?token=J9XGSR6DZAuy_txhEj47TlS8D5JCUCjHFUL1C1yWkuGODRxrNrxoBULIOtQcnAqLrXW2RKbZFvvB8M8YpOiZuuM19NrXRzrk7l9zybscI__nIZYFuYL5PCo9-Emt2zNtxCnk-ZVz0DiEFDGy7ZkGLoc7im31C086Okc49iBJeFoEIDCoj73l_3f9MuqA8T6ADRPQitqH3eDCWYYYhhpdxlE3Np5644qlWwS30lyQeYpBO39TGa3TWecAhZCO7kiz15pUWbM3e_PQ-aMWeY1XiypEzN0h6KI2JVnf_ndfioE0gu60018JOipu38y3J99P216oFZmAsqKhWaIJXnFYYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ساعاتی پیش تو مسیر پلیس‌راه همدان ـ سنندج، یه ماشین سنگین گویا ترمز می‌بره و مستقیم با یه دستگاه تانکر حامل سوخت برخورد می‌کنه و یه انفجار وحشتناک رخ میده!
متاسفانه تا الان 7  جونشون رو از دست دادن...
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/71159" target="_blank">📅 22:12 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71158">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3aea156fe3.mp4?token=lk5E_IDwb9GAwUbVVtUaSzd45E8t7xReF-39ErZiezV9jS1rK8lu-cPApxS4aedU2UlXYzMGiP_9e0yiYCHW5_fyd4Kpg3oc6N_-SSr8TGe9HGUA_c40P3Mcvu5H75BcebMtWzHPJoaHxFDPHp6jQ3lAWMk3UZD0qBEtDgce2EGcRJmQP4bzta0DgsZ0sVPdpuHfwgc0LJ4KUgLOb9t5PnUmMp8PxPs4zgfQh_nXnY6FtW_P3mkYbG7M28f8TjCEPCFPwD9B3BV7oFQo5FQmcGAWlPSniDFpypuWOkQCjmwWknIl7e9Up4X6745fRdNV3sCSnBGIrqhtVzCSOLYrJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3aea156fe3.mp4?token=lk5E_IDwb9GAwUbVVtUaSzd45E8t7xReF-39ErZiezV9jS1rK8lu-cPApxS4aedU2UlXYzMGiP_9e0yiYCHW5_fyd4Kpg3oc6N_-SSr8TGe9HGUA_c40P3Mcvu5H75BcebMtWzHPJoaHxFDPHp6jQ3lAWMk3UZD0qBEtDgce2EGcRJmQP4bzta0DgsZ0sVPdpuHfwgc0LJ4KUgLOb9t5PnUmMp8PxPs4zgfQh_nXnY6FtW_P3mkYbG7M28f8TjCEPCFPwD9B3BV7oFQo5FQmcGAWlPSniDFpypuWOkQCjmwWknIl7e9Up4X6745fRdNV3sCSnBGIrqhtVzCSOLYrJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
وزیر نیرو:
دیگر قطعی برق برنامه‌ریزی‌شده نداریم
اگر مردم جایی دیدند به سامانهٔ ۱۲۱ اطلاع دهند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/71158" target="_blank">📅 21:42 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71157">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31160c5df1.mp4?token=tWPfe6rbBjGHosUP_fK94Sf0cMj6mOhmzVGjRqNKIenGiHx8Jcfo_R1Pm21p9HGdFnnvvEL7SwNSOerexpKPlt7-YaF8y7MgWgroeNNWVNwzh6w1u1ccFHYCp_V-Nqs8O1Lz0pa6qmwW39BSv1qfiYxSzUI0RCx5h_WWGOltHXZYRlXsqHniXdRfREfDFd7kLpySxczF0tkIHHGatr3POAY_NqS6xKhm8sqxCZrz-4ufrh9BAdL3IR5YJ0foWaKOVgXEEaQifIR0tR0HNGUGDeJnKV6j9gaBn8_6siSdpLqQqvHVY2I9Ywc1pzS8FLa_m74tWxcY6lnUhOj4-oluh4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31160c5df1.mp4?token=tWPfe6rbBjGHosUP_fK94Sf0cMj6mOhmzVGjRqNKIenGiHx8Jcfo_R1Pm21p9HGdFnnvvEL7SwNSOerexpKPlt7-YaF8y7MgWgroeNNWVNwzh6w1u1ccFHYCp_V-Nqs8O1Lz0pa6qmwW39BSv1qfiYxSzUI0RCx5h_WWGOltHXZYRlXsqHniXdRfREfDFd7kLpySxczF0tkIHHGatr3POAY_NqS6xKhm8sqxCZrz-4ufrh9BAdL3IR5YJ0foWaKOVgXEEaQifIR0tR0HNGUGDeJnKV6j9gaBn8_6siSdpLqQqvHVY2I9Ywc1pzS8FLa_m74tWxcY6lnUhOj4-oluh4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇺🇸
جان بولتون دیپلمات آمریکایی درباره ایران:
من معتقدم — و دهه‌هاست که چنین نظری دارم — که تنها راه دستیابی به صلح و امنیت واقعی و پایدار در خاورمیانه، خلاص شدن از شر رژیم تهران است.
به گمانم حملات آمریکا و اسرائیل آسیب قابل‌توجهی به این رژیم وارد کرد.
بی‌شک ما اشتباهات زیادی مرتکب شدیم.
اما اگر اراده کنیم که درباره چگونگی انجام آن به‌درستی بیندیشیم، این هدف همچنان قابل‌تحقق است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/71157" target="_blank">📅 21:19 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71156">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
صداوسیما:
صدای انفجار هایی که در جزیره قشم شنیده شده مربوط به شلیک موشک ها به سمت شناور های متخلف در تنگه هرمز است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/71156" target="_blank">📅 21:04 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71155">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bed43299c5.mp4?token=aDrHwtiX9sMRJ6Gslqb9DMll_WIJjUgpeF8C42uTI7PRqqIz85dG3BmHQDd6bwVzZjorynqPdqWO0AGV61Hfg_WXiTTsqGmGpDEs5B9VSPqt5qxzffE3TAl3eIL95DH3TXarOhG3mbPyu2GWAyT952i1L39D6auaeWXFDD7QYBmoRj9J42XzV2NQ6u_MXI___HMrQWFndJiDCAlqnFt6fD8IVtNP87LUMRc1JASJ4mqBwzA1bgWMhm-3W87FdETrmdamKX3TS6ClUq1Ih8bJHsENIExLjPN_mimLSfRGOie5-1T1F-J5iL2AZlXKkRsKXnNj0jnWN_GW0Zel91r7Lg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bed43299c5.mp4?token=aDrHwtiX9sMRJ6Gslqb9DMll_WIJjUgpeF8C42uTI7PRqqIz85dG3BmHQDd6bwVzZjorynqPdqWO0AGV61Hfg_WXiTTsqGmGpDEs5B9VSPqt5qxzffE3TAl3eIL95DH3TXarOhG3mbPyu2GWAyT952i1L39D6auaeWXFDD7QYBmoRj9J42XzV2NQ6u_MXI___HMrQWFndJiDCAlqnFt6fD8IVtNP87LUMRc1JASJ4mqBwzA1bgWMhm-3W87FdETrmdamKX3TS6ClUq1Ih8bJHsENIExLjPN_mimLSfRGOie5-1T1F-J5iL2AZlXKkRsKXnNj0jnWN_GW0Zel91r7Lg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
تصاویر منتشرشده نشان می‌دهد یک کشتی کانتینربر در اسکله بوشهر تقریبا به‌طور کامل نابود شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/71155" target="_blank">📅 20:33 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71154">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🚨
سازمان تجارت دریایی بریتانیا UKMTO:
گزارش‌ هایی مبنی بر وقوع حوادث برای چندین کشتی تجاری در شمال خلیج فارس و دریای عمان دریافت کردیم.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/71154" target="_blank">📅 19:48 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71153">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5717843ac.mp4?token=JdW_NiouVEv1HbWPXn4Yjw3yTJBUiqX_nbfUKWb-aNuNQD2wkfcbXN_fnS-n6Ao9j7fK6h3bs6y6c3gtBhimSpktaroPchrH2wfarYi32JcZOR7Fw8W6fljm0ughkm3n-PBwiffnigU4LdOHgECX7tgeRl3wvVStnPfI5eZxGW8M4Xw5WXotErbhLLUe9UppDzVRtTzZrj8neEaVeOGvl3dgr8r8zm1zoejc-c-PLs1vSxWCt6kBOUh9r_-qFAe9gpNexq8GvWRNx5iNt754zNbZFDucpW8hSQhwQBPGMov_87Va1uyb9GLJSB7Aa9QV0boI5ZzihT2i16fAJ90k5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5717843ac.mp4?token=JdW_NiouVEv1HbWPXn4Yjw3yTJBUiqX_nbfUKWb-aNuNQD2wkfcbXN_fnS-n6Ao9j7fK6h3bs6y6c3gtBhimSpktaroPchrH2wfarYi32JcZOR7Fw8W6fljm0ughkm3n-PBwiffnigU4LdOHgECX7tgeRl3wvVStnPfI5eZxGW8M4Xw5WXotErbhLLUe9UppDzVRtTzZrj8neEaVeOGvl3dgr8r8zm1zoejc-c-PLs1vSxWCt6kBOUh9r_-qFAe9gpNexq8GvWRNx5iNt754zNbZFDucpW8hSQhwQBPGMov_87Va1uyb9GLJSB7Aa9QV0boI5ZzihT2i16fAJ90k5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇺🇸
✈️
ویدیویی تایید نشده از پرواز تانکر سوخت‌رسان آمریکایی به همراه دو جنگنده در آسمان جزیره کیش استان هرمزگان
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/71153" target="_blank">📅 19:39 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71152">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71152" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/71152" target="_blank">📅 19:39 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71151">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HvB66GpBm_0KGBOP_TTTh810aGyYCK7MwcqvdzdxSUFc0yolqg78pP5QLmSFNMkvb757ZZglTmoPr6CVdaHnCNgkXAw7jQd7HcGobANFJ2oqg6idKnXNJ0lqKQkxZJqsXxICla4TROUftMIwLOONIZB9VgqyQEtofNQSW9o_pQusVsSNM1vAvP1baG8oJIe-IheqPC-m97_ctV1-4ayfCFg0AYo4t33x8fImDx_m65m_GBV0hUslokSDDDHC6epKE80jFpUcsgFYfWiUqvnRG_BjgV842qoCGKVLAKjFjxsdCYqJZ3BELoBYqwQmDBj9pswzobuwuEUOqUgH1p8N0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
بازی جذاب اینتر
🆚
ناپولی را در سایت بین‌المللی
TrexBet
پیش‌بینی کنید.
📊
نگاهی به آمار دو تیم:
اینتر: ۲ بازی ۲ برد و کسب و ۵ گل زده
ناپولی: ۲ بازی ۱ برد و ۱ شکست و ۳ گل زده
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/71151" target="_blank">📅 19:39 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71150">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf5e996b2c.mp4?token=XHWz1HKb5EMG_fuM8ITquJb7UvtezAZ4hOodH6C7Wh2W9FIC3DWfp1soXXL1SBb5eElOsegi_91rWpRVGQb2_4M06dNRTn8alqsD2Mj6RV68f7r9hkqJVb9HFFwPeWTrcJfzE-BvKHWMsy2Sg7jBEI8h428utxZ-VY0QOGX-5rPlhhl09uyPh7sr_J1ZdJ3d-KjQm43phjO2LKFMrWy__ocp20r8HIDsPb9AcERJ4EW-n-dIlaM9basA4BShKbVHlbTvAkZKHiYeHh9YkBiZieAFVtd4vt8w3Wyj1_ItXBEDMoOhNvVuZ2vQOw3XA9qpv1rfNRG_Wy82hsFjsD5DIabtEMzXjJ7g9CkljDDu7XZTfRiWttQfevWnl7OWAcV3irAcIA93fcJYeuVZtD27IPpIahvmGwFoxz0wFdu3HO3VMYtOiEAqzmRvWvq-Lo-9rE03JuhEJP9erWwiLGpb36obQVQ4O5LBu_pAe3-m9660gAFL1nsj-t4wIbIbn3z3fpDKiEruJ4boNVcLm0ZJ4BTtaLx2PoXHO9QBBlEBDGTePZLSOc_vc5wqmComddgGyHQvKWRVfJfgted5DQ5wq1t9g5AQl2M10txyLRmdfC2hqcbF7W5moZhcjlXsQvc6uJW-Rmq4qEJ9LDrIoSCJFFQiUP7dhjb6buY1lUVJ3-s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf5e996b2c.mp4?token=XHWz1HKb5EMG_fuM8ITquJb7UvtezAZ4hOodH6C7Wh2W9FIC3DWfp1soXXL1SBb5eElOsegi_91rWpRVGQb2_4M06dNRTn8alqsD2Mj6RV68f7r9hkqJVb9HFFwPeWTrcJfzE-BvKHWMsy2Sg7jBEI8h428utxZ-VY0QOGX-5rPlhhl09uyPh7sr_J1ZdJ3d-KjQm43phjO2LKFMrWy__ocp20r8HIDsPb9AcERJ4EW-n-dIlaM9basA4BShKbVHlbTvAkZKHiYeHh9YkBiZieAFVtd4vt8w3Wyj1_ItXBEDMoOhNvVuZ2vQOw3XA9qpv1rfNRG_Wy82hsFjsD5DIabtEMzXjJ7g9CkljDDu7XZTfRiWttQfevWnl7OWAcV3irAcIA93fcJYeuVZtD27IPpIahvmGwFoxz0wFdu3HO3VMYtOiEAqzmRvWvq-Lo-9rE03JuhEJP9erWwiLGpb36obQVQ4O5LBu_pAe3-m9660gAFL1nsj-t4wIbIbn3z3fpDKiEruJ4boNVcLm0ZJ4BTtaLx2PoXHO9QBBlEBDGTePZLSOc_vc5wqmComddgGyHQvKWRVfJfgted5DQ5wq1t9g5AQl2M10txyLRmdfC2hqcbF7W5moZhcjlXsQvc6uJW-Rmq4qEJ9LDrIoSCJFFQiUP7dhjb6buY1lUVJ3-s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
🇮🇷
لحظه تهدید تخلیه خدمه نفتکش های جمهوری اسلامی توسط خلبان جنگنده ارتش آمریکا
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/71150" target="_blank">📅 18:59 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71149">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🚨
〰️
⭕️
سنتکام مسئولیت حمله به نفتکش های ایرانی را گردن گرفت؛  پس از شلیک موشک‌های بالستیک سپاه به سمت دو ناو جنگی آمریکا، نیروهای آمریکایی ۳ نفتکش حامل نفت خام ایران را هدف قرار داده و از کار انداختند. دو نفتکش نزدیک خارک و جاسک هدف قرار گرفتند و یک نفتکش دیگر…</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/71149" target="_blank">📅 18:39 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71148">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xbr2CZ5Ddlf02ZDHva5FKd9thSeJi7bIFDtVM_Lvec4FSE6q7ybNSKfAXXda9nemcxNkltUnyMWbfW-szw97U9iQ9XC5Ew0gwkeyNw_jimKqYVe0icuXino_4SrWVj0NlpygSGAR8mgEAWwIqfN0IS4MHXJa7mwFY2tLFP_Y1VFU6gJabMP2sA6C-LOo0vIo4KgZQHiEYvuLi6oVhekAv1lNl7asVCcEpNwVe0w42j0twabcES1uiK9MKhNeVof8PkxHNApHvCZS4lc3KOPZ7KXKmVNiBHDHC8N8A7WHgXpVo4JBQ_vs7jTvTM6FknGDsVfMGPDUhL48N7NQnLV10A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇺🇸
🇧🇭
سفارت ایالات متحده در بحرین:
با توجه به تنش‌ها در خاورمیانه، وضعیت امنیتی همچنان پیچیده است و احتمال تشدید غیرمنتظره اوضاع وجود دارد.
سفارت ایالات متحده به شهروندان آمریکایی یادآوری می‌کند که ایران پیش‌تر زیرساخت‌های غیرنظامی در بحرین، از جمله هتل‌های منامه، را هدف قرار داده است.
آمریکایی‌هایی که در حال حاضر در خاورمیانه حضور دارند، باید هوشیاری خود را افزایش دهند و نسبت به احتمال لغو پروازها، بسته شدن حریم هوایی و اختلال در سفرها آگاه باشند.
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/71148" target="_blank">📅 18:17 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71147">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/1d8dfb05eb.mp4?token=eb1CqUcYxditAcuj-p3wEinA9myZoMYd6x86sqwcZSHWnGqpJXDqSlRU_89XduvIXoxRphhhaYcV8GtLxqjlD8jxVuJGm_AFgCgv95FzH1Bj5lX7_TGfLSrFVPQlhss_c6NHILDdRJd3WdURuJuzXbjksKAWrTH4UHVd5-6pma62gGiaWQpin5xjwiIhrtvouMaxqTyM6mCNFZAIpKtEW1GDjOwBWTFbS4YBeE06dpxAeWIpQum7dnCuyl80XH7-ZgyF9iC38UoQAYsAg4eeRE-_G_KMflTTjfBG0HPBPGDZkrOM5HfKGJzXo2_k7QZvY3NZKGGEsafBVBCvH7o33g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/1d8dfb05eb.mp4?token=eb1CqUcYxditAcuj-p3wEinA9myZoMYd6x86sqwcZSHWnGqpJXDqSlRU_89XduvIXoxRphhhaYcV8GtLxqjlD8jxVuJGm_AFgCgv95FzH1Bj5lX7_TGfLSrFVPQlhss_c6NHILDdRJd3WdURuJuzXbjksKAWrTH4UHVd5-6pma62gGiaWQpin5xjwiIhrtvouMaxqTyM6mCNFZAIpKtEW1GDjOwBWTFbS4YBeE06dpxAeWIpQum7dnCuyl80XH7-ZgyF9iC38UoQAYsAg4eeRE-_G_KMflTTjfBG0HPBPGDZkrOM5HfKGJzXo2_k7QZvY3NZKGGEsafBVBCvH7o33g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
〰️
⭕️
سنتکام مسئولیت حمله به نفتکش های ایرانی را گردن گرفت؛
پس از شلیک موشک‌های بالستیک سپاه به سمت دو ناو جنگی آمریکا، نیروهای آمریکایی ۳ نفتکش حامل نفت خام ایران را هدف قرار داده و از کار انداختند.
دو نفتکش نزدیک خارک و جاسک هدف قرار گرفتند و یک نفتکش دیگر در دریای عمان منهدم شد.
سنتکام اعلام کرد این نفتکش‌ها بخشی از شبکه تأمین مالی سپاه و نیروهای نیابتی آن بوده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/71147" target="_blank">📅 17:55 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71146">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c865776e9.mp4?token=QpXFm4UPfh-a1VgO4pG6BnZG-8O0wovr9JM9OzG_FK7p_xz6t_gcOsOTGTV6Q2lzxBSWSv1PsZNtiDQkkXjYlkuHgYhc_twImHH9-ZhHPS3PygMvhc4-ZPgmDmiLe3Cyypsc_Sx_7054i1WdavF_Pm4EnG49--YeagPy2yJIqQ2HvhVCxD1jnUYDoftlPaX8Cehx1SOt7Ktw7ghXsDmBtDbZpInI8P2-Hw8S2NJo8f-Ki5kQqdfq6VjBU6MlHOIJPCqGUooakmSeDFsN05ks-W5Im2bvq43En7_bccE7reb-bnnSlip8Po0KzHiLK22XFt4YMmf_fZw62Rj2tAZCgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c865776e9.mp4?token=QpXFm4UPfh-a1VgO4pG6BnZG-8O0wovr9JM9OzG_FK7p_xz6t_gcOsOTGTV6Q2lzxBSWSv1PsZNtiDQkkXjYlkuHgYhc_twImHH9-ZhHPS3PygMvhc4-ZPgmDmiLe3Cyypsc_Sx_7054i1WdavF_Pm4EnG49--YeagPy2yJIqQ2HvhVCxD1jnUYDoftlPaX8Cehx1SOt7Ktw7ghXsDmBtDbZpInI8P2-Hw8S2NJo8f-Ki5kQqdfq6VjBU6MlHOIJPCqGUooakmSeDFsN05ks-W5Im2bvq43En7_bccE7reb-bnnSlip8Po0KzHiLK22XFt4YMmf_fZw62Rj2tAZCgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
حسن روحانی:
به مردم بگیم قرار ما اینه که با قدرت‌های بزرگ تا بیست سال دیگه بجنگیم.
اگه مردم قبول کردن عالیه بریم ادامه بدیم.
ولی اگه مردم نپذیرفتن و راه دیگه‌ای نشون دادن حق نداریم نادیده‌شون بگیریم.
حتی پیغمبر هم با مردم خودش مشورت می‌کرد.
تو این کشور هیچکی از جانب خدا حاکم نیست‌؛ همه به لطف رای مردم اومدن.
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/71146" target="_blank">📅 17:30 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71145">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/100451e13a.mp4?token=D-gVyVuEIAa5F6hxO109KZUXmali5OiwemjuyJ458y0vUa9wU9us8h9F00pLiX-u5yKuDjkqIZUMhYDrUlN_LTlStsaufXf0wkxlXyn-emzD6WbYaAHBPlBh1UrMPlI6jBCKnXsj63L_iGUd1D9y_F_Ed-ZdLoDq2a0q78s5N3KH-ER8xYP5Q-9DyE-OTYK8c4jnJ5exEaPGygS2S-CFldnWwWD-dM3c8HjIZei06S2Mihw-CjmIWwPJCqXg_lSKQzD-6AMkSjjeVLEZG5rVUIVthcHHO3U0zJd3lKljWsisHQ7dH482CnXm7cbPC1-GOUwpFsOYO8iZXHLeOOaRgTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/100451e13a.mp4?token=D-gVyVuEIAa5F6hxO109KZUXmali5OiwemjuyJ458y0vUa9wU9us8h9F00pLiX-u5yKuDjkqIZUMhYDrUlN_LTlStsaufXf0wkxlXyn-emzD6WbYaAHBPlBh1UrMPlI6jBCKnXsj63L_iGUd1D9y_F_Ed-ZdLoDq2a0q78s5N3KH-ER8xYP5Q-9DyE-OTYK8c4jnJ5exEaPGygS2S-CFldnWwWD-dM3c8HjIZei06S2Mihw-CjmIWwPJCqXg_lSKQzD-6AMkSjjeVLEZG5rVUIVthcHHO3U0zJd3lKljWsisHQ7dH482CnXm7cbPC1-GOUwpFsOYO8iZXHLeOOaRgTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
بابک زنجانی: سایپا را ۱ میلیارد دلار می‌فروختند، ۲ میلیارد پیشنهاد دادم، نفروختند
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/71145" target="_blank">📅 17:00 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71144">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b09e3df411.mp4?token=F03JEyFUsKaLA7V9iXj7rHJr4TVsXxh5sXkH_Pq1v0ZzTUfZ9mrh8UVsJkp8fLZ6JXcq_9r8nPb-fvg4itPkZLq0RzHoN5GxBbf7f3ZDXmxzITHdwMs5xZPHFcKX8FKjhGl8PjJnM-M6iMOHCfk320gpv4l0H-HyF5Fbjek_u4dZAPI34YmpdnypDjGPwYP6uPZaUrf6FsDP3CpMbne6C-Xbh0j_sWJGkXhvKXOsMDFBjoCyKQUN07IKJ-MD_ftliZeagHbsvvVLRaIEj4BZNq48jJkc9wKxkFjqDuTWv2HYYCT9tqT_Dj0xfSl3AsIeh2P-MteK3AuCu3MXxwcVKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b09e3df411.mp4?token=F03JEyFUsKaLA7V9iXj7rHJr4TVsXxh5sXkH_Pq1v0ZzTUfZ9mrh8UVsJkp8fLZ6JXcq_9r8nPb-fvg4itPkZLq0RzHoN5GxBbf7f3ZDXmxzITHdwMs5xZPHFcKX8FKjhGl8PjJnM-M6iMOHCfk320gpv4l0H-HyF5Fbjek_u4dZAPI34YmpdnypDjGPwYP6uPZaUrf6FsDP3CpMbne6C-Xbh0j_sWJGkXhvKXOsMDFBjoCyKQUN07IKJ-MD_ftliZeagHbsvvVLRaIEj4BZNq48jJkc9wKxkFjqDuTWv2HYYCT9tqT_Dj0xfSl3AsIeh2P-MteK3AuCu3MXxwcVKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه سری ایرانیا هم انگار توی یه ایران دیگن و رفتن توی جنگلای شمال پستونک پارتی گرفتن
🙁
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/71144" target="_blank">📅 16:31 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71143">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc463ce6f9.mp4?token=Z9wNClRgjI8jL-nBbaCLvyrRgmOziYwKf8T3UPz0kI568GfRy0T0k-76_lUjhLumqAounZbhIYKe22HwKSS0ZqVlfiAQN_Dj2vLqExhBPN73ozyXZedjtzrzctTPTvqBYkODmJRajFNQb5er24DXMnmwxfn02urMrEph5_ceBEcdnhNOwFATyGEKwgV7tbr7CkZhcFakP8JUI6ntJCZRkLTeZuiOW2tmK4bzIuSrBgRzp5nNG3nH_uumYxDgsZ3rgWWb-TcToX6YoNZLLmcVCN3fGrBKpZiHqUKA3_qzlGVA-oBi0J8Z0wQSJ1JdL0ll5TVp_hz8VTiCv5LT8ljqag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc463ce6f9.mp4?token=Z9wNClRgjI8jL-nBbaCLvyrRgmOziYwKf8T3UPz0kI568GfRy0T0k-76_lUjhLumqAounZbhIYKe22HwKSS0ZqVlfiAQN_Dj2vLqExhBPN73ozyXZedjtzrzctTPTvqBYkODmJRajFNQb5er24DXMnmwxfn02urMrEph5_ceBEcdnhNOwFATyGEKwgV7tbr7CkZhcFakP8JUI6ntJCZRkLTeZuiOW2tmK4bzIuSrBgRzp5nNG3nH_uumYxDgsZ3rgWWb-TcToX6YoNZLLmcVCN3fGrBKpZiHqUKA3_qzlGVA-oBi0J8Z0wQSJ1JdL0ll5TVp_hz8VTiCv5LT8ljqag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇨🇳
تو چین یه نفر بعد ورود به مغازه‌ش که به علت نشتی پر از گاز بوده، کلید برق رو میزنه و کل مغازه میترکه ولی خوشبختانه زنده میمونه و بعد از اینکه به بیرون پرت میشه کون لختی فرار میکنه.
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/71143" target="_blank">📅 16:03 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71142">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c9c6b59588.mp4?token=fnmYKAwPMlaIHMr8rWrKVDWRg89su-W7o1iPXxP-RT6diPmQW3FSyQSRO0K4VJsfUwcOfDe3asx7b1UnY4_8Zjuf7uf8u89qVJFyaxsEMMWpR-3yP72Ufj7YGentcfdy6jriiKWTIXcDam7T4im1pmQKPo8rXkECtU4zoYPP63N5ltGxAKYMwGeWaxRJT9PefAl5hrz_SSyKog2fXyPa_IonFe9H-Ufv0VcW1nuD2ZmrQI3eGatkf_OOrHvG3ZHB-y7m_GBcYS_r_aqdGQx7gywY7nMpy5wWtL4rKEmGwHk6h0L050kSmjnogVvOZCWnXd74sJ2_eqnIEJW7JCc9rDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c9c6b59588.mp4?token=fnmYKAwPMlaIHMr8rWrKVDWRg89su-W7o1iPXxP-RT6diPmQW3FSyQSRO0K4VJsfUwcOfDe3asx7b1UnY4_8Zjuf7uf8u89qVJFyaxsEMMWpR-3yP72Ufj7YGentcfdy6jriiKWTIXcDam7T4im1pmQKPo8rXkECtU4zoYPP63N5ltGxAKYMwGeWaxRJT9PefAl5hrz_SSyKog2fXyPa_IonFe9H-Ufv0VcW1nuD2ZmrQI3eGatkf_OOrHvG3ZHB-y7m_GBcYS_r_aqdGQx7gywY7nMpy5wWtL4rKEmGwHk6h0L050kSmjnogVvOZCWnXd74sJ2_eqnIEJW7JCc9rDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇷
🇺🇦
🇷🇺
یک مزدور برزیلی که در درگیری‌های روسیه و اوکراین می‌جنگید، لحظه حیرت‌انگیز عبور یک تانک از روی خود را — در حالی که میان علف‌ها پنهان شده بود — ضبط و در حساب اینستاگرامش منتشر کرد
😟
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/71142" target="_blank">📅 15:32 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71141">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f07a24e005.mp4?token=frmCpO14c4l6wodlqH-v8QOh3WyM01d1_-mIxtaMJ2L1jUmkOwJfu-kXSLsm13T0ACAT31Cz6kNu-UNo7cIqKWIYTZ7uCOfcsVx8IivoCOmvcIReQynDTE3Sv0n6zaN0Gass0b8iYUgP5JQpt_UDpdk5l4lcOt3Bg2SlZXYs6OhPoYMvKDPN_6h9RRB297wX0MZRWIZCip7GRlEXq4p1JItV9t_iRZT169gSCoEiRfZ_KTxdXUp-fpQ8D2gUkPuk7uG1D47qiKzEOe734rLcDZlUhZVbwVQv-BR7CmR0cEv07LrheYdimu9kt-W_9T5SfUC8YTvLsVbcy47pYNNUAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f07a24e005.mp4?token=frmCpO14c4l6wodlqH-v8QOh3WyM01d1_-mIxtaMJ2L1jUmkOwJfu-kXSLsm13T0ACAT31Cz6kNu-UNo7cIqKWIYTZ7uCOfcsVx8IivoCOmvcIReQynDTE3Sv0n6zaN0Gass0b8iYUgP5JQpt_UDpdk5l4lcOt3Bg2SlZXYs6OhPoYMvKDPN_6h9RRB297wX0MZRWIZCip7GRlEXq4p1JItV9t_iRZT169gSCoEiRfZ_KTxdXUp-fpQ8D2gUkPuk7uG1D47qiKzEOe734rLcDZlUhZVbwVQv-BR7CmR0cEv07LrheYdimu9kt-W_9T5SfUC8YTvLsVbcy47pYNNUAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
یه آخوند درباره شعار«تا آخوند کفن نشود این وطن وطن نشود»
؛
همونطور که رهبرمون رو شهید کردن یه آخوند دیگه جاشو گرفت
به ترامپ و نتانیاهو و منافقین داخلی میگم این حرفمو
تا آخوند شماهارو کفن نکنه ول نخواهیم کرد
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/71141" target="_blank">📅 15:01 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71140">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">⛔️
این قبیله ای که میبینید اسمشون موکو موکو هست
؛
این قبلیه در افریقا که مثل سرخپوست ها هستن برای اینکه زنان قبیله خودشون دعوت کنن به سبک رقص های به خصوص خودشون انجام میدن
هر زنی در قبیله شون مجذوب رقص مردی بشه میره بهش میده و اصلا اینطوری نیست که کسی حتما باید زن شخص خاصی بشه.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/71140" target="_blank">📅 14:33 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71137">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca83f4e683.mp4?token=kI5HNjbGtUeF_vRazf5AAoWJzMbNiZ2GYvKmD5MjBl3nMnNx-izIZ8AP-dEUUsUim-fvdC1THyH-eFzQNFzvQaVK5QMi38ZVxqQ500QBgbigTIicWHZxscX2Zf0-fS2y86oEmLZftljE6wwQ9GpRsbuPoLGI03Djn7VmwetT1Zh6158FdBvwhx9CO3H2gd2wE2AOuvWGHPKGQBOZXCIcMZW2kPOaoBI7c86NjSP1LcwUNRlHVu2cZ4AEprhtq1me6UiMu7SusfjAdlXkNkDbCyvIMM_WpLOGaaREQSq8qI7-Ml9huy0fUA7ilZp-o33ijHzWYHGkUEvMGI9bOI40ew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca83f4e683.mp4?token=kI5HNjbGtUeF_vRazf5AAoWJzMbNiZ2GYvKmD5MjBl3nMnNx-izIZ8AP-dEUUsUim-fvdC1THyH-eFzQNFzvQaVK5QMi38ZVxqQ500QBgbigTIicWHZxscX2Zf0-fS2y86oEmLZftljE6wwQ9GpRsbuPoLGI03Djn7VmwetT1Zh6158FdBvwhx9CO3H2gd2wE2AOuvWGHPKGQBOZXCIcMZW2kPOaoBI7c86NjSP1LcwUNRlHVu2cZ4AEprhtq1me6UiMu7SusfjAdlXkNkDbCyvIMM_WpLOGaaREQSq8qI7-Ml9huy0fUA7ilZp-o33ijHzWYHGkUEvMGI9bOI40ew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇨🇦
تصاویری از تورنتو کانادا بعد از بارش باران و طوفان
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/71137" target="_blank">📅 13:51 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71136">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8fec01afbd.mp4?token=WXUYh4vDIo0n4yLLdKYEgD7isfUxgyoQAyiCnT3a7b0bmFhrYfbKKl5XCLKvuGbG1mkmUeQEkSrBns66cFmu5cZcH3XlXkK7NuDBk7TOebyMNMyJYxhlbinPyFk_muEXisfNyJmXSd8ZnLwFdga16ko73Kj1XOaT_Fpm1OUoIQi1HkzfwUmfs5bM2ctsO-2O2EdJmBLp3jctPrr1slvj70-aPOFhP92crUU2lLvxUjt02XqHmrYYj-LM4Y9GqQBVIKf0lilBirBTOjeQ4XMONvLVgTQGEOq1fVP2ukiyhmtLGfLHSA6K1UQ5hgxYRba3lfPhJuFY7Fc6hRu_ylVi-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8fec01afbd.mp4?token=WXUYh4vDIo0n4yLLdKYEgD7isfUxgyoQAyiCnT3a7b0bmFhrYfbKKl5XCLKvuGbG1mkmUeQEkSrBns66cFmu5cZcH3XlXkK7NuDBk7TOebyMNMyJYxhlbinPyFk_muEXisfNyJmXSd8ZnLwFdga16ko73Kj1XOaT_Fpm1OUoIQi1HkzfwUmfs5bM2ctsO-2O2EdJmBLp3jctPrr1slvj70-aPOFhP92crUU2lLvxUjt02XqHmrYYj-LM4Y9GqQBVIKf0lilBirBTOjeQ4XMONvLVgTQGEOq1fVP2ukiyhmtLGfLHSA6K1UQ5hgxYRba3lfPhJuFY7Fc6hRu_ylVi-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
پیرزن طرفدار حکومت که میگه:
نه پول میخایم نه چیزی دیگه گرونی هم تحمل میکنیم مسئله حجاب رو حل بکنید خیلی مسئله مهم تر و واجبی هستش
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/71136" target="_blank">📅 13:09 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71135">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5af49e9554.mp4?token=uFRcKeEUDbzXdLJ-_rrWY42jWz9qg-Q0xXy7SZnm9wOrldK38PP9i3JbImutCVhnCrWetTEA5Hv6TOM74HdxuJpf7vHZsKtma-CGtYj5-y9LZAqJp3IloEQraZQbyFhy0yS3t9izELLEqaUgtSSAjjzW6_RX6EzDPuJCm1-2_ME_T_g3h1ymaqkSlS6JbB_Y9F8kHQCVgON7hEbQ5iDMS7IQCdreilKfYH90i_GkOsPcAYTo3XIwaM1mPtaxSoedwzi7IIVBVgqhYxh8cNG0igfl8a_ISAYcApEp3pE338DX9pgLP587f0N24FegZ8_n3G_QT62YBKSPLt_tToPTwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5af49e9554.mp4?token=uFRcKeEUDbzXdLJ-_rrWY42jWz9qg-Q0xXy7SZnm9wOrldK38PP9i3JbImutCVhnCrWetTEA5Hv6TOM74HdxuJpf7vHZsKtma-CGtYj5-y9LZAqJp3IloEQraZQbyFhy0yS3t9izELLEqaUgtSSAjjzW6_RX6EzDPuJCm1-2_ME_T_g3h1ymaqkSlS6JbB_Y9F8kHQCVgON7hEbQ5iDMS7IQCdreilKfYH90i_GkOsPcAYTo3XIwaM1mPtaxSoedwzi7IIVBVgqhYxh8cNG0igfl8a_ISAYcApEp3pE338DX9pgLP587f0N24FegZ8_n3G_QT62YBKSPLt_tToPTwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
🇮🇷
تصاویری از نفتکش ایرانی که چند ساعت قبل هدف حمله آمریکا قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/71135" target="_blank">📅 12:41 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71131">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4bb2e861ad.mp4?token=alsxo-y1xxn6K-qnmUUFU7ziQpm2Q7I1boDGU_InwdT7Ja-2zYf_junJrYTH4EdaGwNGg-ksdhRKlGDB7_bGiMXxZy08UhScwkrs23EyY27AAPlY42y_ozEJ2HoW3nOaXsLKMZO6w2KMizOVhUVF2OMyr7KGi8n3g8-XfKcpytpmND4wJudi2keZzhU2-QnepCfNxCSm1qHNyAj5FBaPL5JA7F28uaXlY-XhJynTX1p3YsOU01xuyj7k33TkKIAs8OIK-AolhSoEagQCaOGu2co62ldvi2WRx8q0DKAhoq7nhmhmpgmjIEOtzV8T6_PuuxV4cjEWwbIArGqWR7kx-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4bb2e861ad.mp4?token=alsxo-y1xxn6K-qnmUUFU7ziQpm2Q7I1boDGU_InwdT7Ja-2zYf_junJrYTH4EdaGwNGg-ksdhRKlGDB7_bGiMXxZy08UhScwkrs23EyY27AAPlY42y_ozEJ2HoW3nOaXsLKMZO6w2KMizOVhUVF2OMyr7KGi8n3g8-XfKcpytpmND4wJudi2keZzhU2-QnepCfNxCSm1qHNyAj5FBaPL5JA7F28uaXlY-XhJynTX1p3YsOU01xuyj7k33TkKIAs8OIK-AolhSoEagQCaOGu2co62ldvi2WRx8q0DKAhoq7nhmhmpgmjIEOtzV8T6_PuuxV4cjEWwbIArGqWR7kx-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇱🇧
خبرنگار اعزامی صداوسیما به لبنان سقوط تپه علی الطاهر در جنوب لبنان رو تایید کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/71131" target="_blank">📅 12:08 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71130">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🚨
خبرگزاری فارس:ساعتی پیش، صدای چند انفجار از خلیج فارس در محدوده جزیره خارگ شنیده شد  خبرنگار فارس در جزیره خارگ می‌گوید صدای انفجار از محدودهٔ خلیج فارس به گوش رسیده است اما نشانه‌ای از دود و آتش در خلیج فارس مشاهده نمی‌شود. تاکنون اطلاعات رسمی و دقیقی درباره…</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/71130" target="_blank">📅 11:54 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71128">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ocDXJKzvmaG50aD-M5vXSNXrqsHxAd6plg3EG3swj6_JtCYdo6HUZ5fw0QqfDlDkHneVjNrqb7pYoN5IMG1yTYlbielhphoxCiH7Nwr1wY9KWo_m8kkzhQGoVn-usVWWwqzPTTMh4sPUUNww4pjGTXp3e0tM_D3hMGKaUDUXp9tJcpwl8X2NS086tgOsQwSOE53xOzgQ5wkcYhJ6eMoAXPgb64Im76B30LSqgcroUr8yLxJtNm0PerK2mPJKzL-7MuLw8YmNuy5FLPSuThEjUnPHkyXhLsrPesj70IrQhhqE616Qucq1KmZOrlbyRKQWBJcqi6DkJ7bmd2nQnV0B3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/924e97ac3c.mp4?token=HT8QLhvnauF-Cs7st6MgqOwxiPdzTxykrSZQU0GDwBgC9oDzH7g10G06Rur3tOf17pMoyA5sgAZBBcAKo7r2WFcWxeiNq6Ze73ubDtk607YC4AAZU6kvGrMAhJhqGfa_nBjfUcsbO5m5QWVkJ4uw6w9fieKliDlqVE0FEOKZj6f9dvRidaT8Me2XH1-YHS5jfc5SMARV4WMluT9IQRcgKhLYJlo8UETcQOYvYxp5_20_rfiN6-whJVpX5DhQ9EPdr4_Yp1PyKFPD13_PuO_JfN9QyHD3GOC3VrZcAXif-ZzBiV6DgcuAOOGAe0lYLG38vsHfaxD8l7sn_M1WqzKVSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/924e97ac3c.mp4?token=HT8QLhvnauF-Cs7st6MgqOwxiPdzTxykrSZQU0GDwBgC9oDzH7g10G06Rur3tOf17pMoyA5sgAZBBcAKo7r2WFcWxeiNq6Ze73ubDtk607YC4AAZU6kvGrMAhJhqGfa_nBjfUcsbO5m5QWVkJ4uw6w9fieKliDlqVE0FEOKZj6f9dvRidaT8Me2XH1-YHS5jfc5SMARV4WMluT9IQRcgKhLYJlo8UETcQOYvYxp5_20_rfiN6-whJVpX5DhQ9EPdr4_Yp1PyKFPD13_PuO_JfN9QyHD3GOC3VrZcAXif-ZzBiV6DgcuAOOGAe0lYLG38vsHfaxD8l7sn_M1WqzKVSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
یه پسر بدبخت پست گذاشته که اگه این پست ۵ هزار تا لایک بخوره، صاحبکارم منو میکنه! تورو خدا لایکش نکنین.
و حالا واکنش مردم دلسوز ایران:
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/71128" target="_blank">📅 11:39 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71127">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
خبرگزاری فارس:ساعتی پیش، صدای چند انفجار از خلیج فارس در محدوده جزیره خارگ شنیده شد
خبرنگار فارس در جزیره خارگ می‌گوید صدای انفجار از محدودهٔ خلیج فارس به گوش رسیده است اما نشانه‌ای از دود و آتش در خلیج فارس مشاهده نمی‌شود.
تاکنون اطلاعات رسمی و دقیقی درباره علت و منشأ این صداها منتشر نشده و جزئیات تکمیلی متعاقباً اعلام خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/71127" target="_blank">📅 11:39 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71126">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71126" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/71126" target="_blank">📅 11:39 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71125">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kAEqFKFk2XeV59nQdsLUw6hlHpc8ZJN1x2HjnVLrtMpPYqOFaYME1c5LIX9Ea7o4eSnc8TkI5jTAXm2aJ8pS3rutTxJbEBeVGtDG9nElNzGgg_OyJEM4yxnhAWgSo5sOl-KgLomMkeA8ioX_zZAmkdB9Gke93OaI6gAUSTrRT8tKgI1Hxeo3x4kqqVxk8KEYJ5aPIxYM0aWhceFLQ2e2eEe3qeY6fGjDPhaRAFKTkUD5t2eMDbjbSou2fkEBiA8Of7cgcYAPKV5aeoLgnYFFV9T1u7Q13B3wnIsg3BSc0FVjTbUyywKgGGfE8zYYqst8Vxd5TEsVz7mL0cgUEyUXLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت بین‌المللی
TrexBet
پیش‌بینی کنید.
بورنموث
🆚
نیوکاسل
کاونتری
🆚
منچستر سیتی
تاتنهام
🆚
ناتینگهام فارست
اتلتیکو مادرید
🆚
اتلتیکو بیلبائو
ناپولی
🆚
اینتر
آتالانتا
🆚
رم
دورتموند
🆚
هوفنهایم
بایرن مونیخ
🆚
شالکه
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
انتخابت رو انجام بده و آماده‌ی هیجان باش!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/71125" target="_blank">📅 11:39 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71124">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0380bdceab.mp4?token=CNzqQaDLC3_eSCHZHAb9HFp9d2XXsyEsbGAVwHg9X9erE3XxtJJw-euvCq6CAB9m8hL-3ruWzUf73txf8Tm3UOP0Dr6qwofhriOPTMIZkxGr7khW8Vt2vNTMgZ_3KNF0WF1lnD3UlumnXdvZcy8icI4buQp1_pxZdhYcqS1gNWlif59IppPDLrvfaCwfIYYN5mVaiHXSF3tfjHGRt61uwnn_3fxOjpCctZAWzP7XsrKwSjT8dWfMeJYAr43EWQdwTxzB0NQw4Tsb4z4btrIoL4iOrqEC72ObKYc57ferKpeVN8IeJULi4QzYYMLerLlb9_KbDZ-oyTtTKLvxOHOWdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0380bdceab.mp4?token=CNzqQaDLC3_eSCHZHAb9HFp9d2XXsyEsbGAVwHg9X9erE3XxtJJw-euvCq6CAB9m8hL-3ruWzUf73txf8Tm3UOP0Dr6qwofhriOPTMIZkxGr7khW8Vt2vNTMgZ_3KNF0WF1lnD3UlumnXdvZcy8icI4buQp1_pxZdhYcqS1gNWlif59IppPDLrvfaCwfIYYN5mVaiHXSF3tfjHGRt61uwnn_3fxOjpCctZAWzP7XsrKwSjT8dWfMeJYAr43EWQdwTxzB0NQw4Tsb4z4btrIoL4iOrqEC72ObKYc57ferKpeVN8IeJULi4QzYYMLerLlb9_KbDZ-oyTtTKLvxOHOWdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📚
معرفی لاکچری‌ترین مدارس ایران !
برای اینکه به علم برسی هم باید اول ثروت داشته باشی!
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/71124" target="_blank">📅 11:03 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71123">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a478b3c9a9.mp4?token=kBK9IV8hYy12qXWxuMCnN2gZcmePl2svR2EmizEj4HIh2wFyVJxDXTvDxMvnfk-UDBYjDVsMKOXRGHhaUuhQRAleuNYa7egXftwYPgogT__TMPCE4D6tAZ7374lrhXJGG4mYihMq7KCCherI-Q25ULPwYUmlqP3V9qdfteKecaztL6RfQFWmqCRa-UNSDujkpVNPlkaDmEd7cNh3POL1y0Sqp3JqujySydRSgFs-Y4Uc1KK3UD31FWcD-G7r4-LY9UoqGrdoOBVBELU-ZXhIwxiZh_XSY_DwPK5hhFCkYVfewBCUCyxqNaMMOuLYOcO88sbmitMwemoj9BvHoxpEFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a478b3c9a9.mp4?token=kBK9IV8hYy12qXWxuMCnN2gZcmePl2svR2EmizEj4HIh2wFyVJxDXTvDxMvnfk-UDBYjDVsMKOXRGHhaUuhQRAleuNYa7egXftwYPgogT__TMPCE4D6tAZ7374lrhXJGG4mYihMq7KCCherI-Q25ULPwYUmlqP3V9qdfteKecaztL6RfQFWmqCRa-UNSDujkpVNPlkaDmEd7cNh3POL1y0Sqp3JqujySydRSgFs-Y4Uc1KK3UD31FWcD-G7r4-LY9UoqGrdoOBVBELU-ZXhIwxiZh_XSY_DwPK5hhFCkYVfewBCUCyxqNaMMOuLYOcO88sbmitMwemoj9BvHoxpEFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تسلا، سفر با تاکسی‌های خودران Cybercab رو تو تگزاس آغاز کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/71123" target="_blank">📅 10:34 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71122">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a09a3f19ee.mp4?token=oxoU7GrkXowIi5QEshKy0CZWZqSyJtvqAXXtN7L2yGKa2PgDC-IzbSGddTF0nVkvEbaqCiWiXD2aGJyiyJ6hS40ry7h6G-wquRiEz1FWsUw-VDE4smYOpEgH7o4Qbma9HGbpmKK2UU1NQRUrINABMj7WSHwLK9gl-F0rKANzvCf9Y2_9LUTSrq7fbjQ6rVG-rbNNluWAsZUHYXOYf7siozAhWgu7QDgrHMa9imc0VsISsHmUUGPRAi6xaRGrWF1BAiu2E30qfVKc5juIRYt3YHvxBHezw8vZLLXI-hJ3JGnjteZ3tZyOfDkgVJKOf_CLnaJTy8_AyTgHblFZgKge-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a09a3f19ee.mp4?token=oxoU7GrkXowIi5QEshKy0CZWZqSyJtvqAXXtN7L2yGKa2PgDC-IzbSGddTF0nVkvEbaqCiWiXD2aGJyiyJ6hS40ry7h6G-wquRiEz1FWsUw-VDE4smYOpEgH7o4Qbma9HGbpmKK2UU1NQRUrINABMj7WSHwLK9gl-F0rKANzvCf9Y2_9LUTSrq7fbjQ6rVG-rbNNluWAsZUHYXOYf7siozAhWgu7QDgrHMa9imc0VsISsHmUUGPRAi6xaRGrWF1BAiu2E30qfVKc5juIRYt3YHvxBHezw8vZLLXI-hJ3JGnjteZ3tZyOfDkgVJKOf_CLnaJTy8_AyTgHblFZgKge-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
〰️
🇹🇭
کامیون‌های سوخت‌رسان مشغول انتقال سوخت هواپیما به ناو هواپیمابری «یو‌اس‌اس آبراهام لینکلن» (CVN-72) در بندر «لائم چابانگ» تایلند هستند؛ به‌طوری که از زمان پهلو گرفتن این ناو، روزانه ورود و خروج ۲۰ تا ۳۰ دستگاه کامیون مشاهده شده است.
این سوخت برای تأمین نیازهای «بال هوایی نهم ناو» (CVW-9) در داخل ناو ذخیره می‌شود؛
یگانی شامل جنگنده‌های رادارگریز F-35C Lightning II، جنگنده‌های تهاجمی F/A-18E/F Super Hornet، جت‌های جنگ الکترونیک EA-18G Growler، هواپیماهای هشدار زودهنگام E-2D Advanced Hawkeye و بالگردهای MH-60 Seahawk.
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/71122" target="_blank">📅 10:04 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71121">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/deba41468f.mp4?token=XS8a4viKXVBMLnovunVvadgwZc3eJRu4fNWvFT8udKXYpz0yetOy_vqjnQ5WinCne_Gft-rnlenihFZ-Je-V6B6gAOuPPFqE8E-3s2yDrs_8WxvJJ18uWrxTOKj6_X0MWExg3_veacURFzpUZ6dZueHnqk8QPDj1x0jSoeUXyM6JsUC_883hMhWypNbOVud7gbADjXVgQej0hBSl_prGwDjj9nYk7TVWdnR3byV3-L88xLbNqthIXfJv_MC4HaR2NXiZgrHGoH_4Mkshuku9O74iTiUy3iosyi9Efc-t4u-PWWL18gbg20JX7YjnDC3I5uk36FUBnrJWKwmhy3N58jVjcjADhF0xN6yyB-klF60SpG6CcN20s_FM12O_6oI04cznE71L777H2HIQTTPO5GaX6L1nFITlpTb_tu1noHS1nogah8V4Rek0aY-rCLSQgGsi2EYbP5R3AIJwynwlzM38_5fZP6qutP5C5pe71n1eGM5RaGy6Llke_P7pjzklkOvrEGEiA00WlosZJBcu4m_N1qlLVnjnYCUq49LWV0nuFczoGMhzE5Y0EIy1ysYzgdPLcjelrqxUs1dpf05OObVI3qnDMkzCObacEnwt_nrd28c1hBY2LaqiGXS1SasszrqWdKdVgvaQvRqT4HGbgeSwJr2H6N-aYXtgvHNo6E4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/deba41468f.mp4?token=XS8a4viKXVBMLnovunVvadgwZc3eJRu4fNWvFT8udKXYpz0yetOy_vqjnQ5WinCne_Gft-rnlenihFZ-Je-V6B6gAOuPPFqE8E-3s2yDrs_8WxvJJ18uWrxTOKj6_X0MWExg3_veacURFzpUZ6dZueHnqk8QPDj1x0jSoeUXyM6JsUC_883hMhWypNbOVud7gbADjXVgQej0hBSl_prGwDjj9nYk7TVWdnR3byV3-L88xLbNqthIXfJv_MC4HaR2NXiZgrHGoH_4Mkshuku9O74iTiUy3iosyi9Efc-t4u-PWWL18gbg20JX7YjnDC3I5uk36FUBnrJWKwmhy3N58jVjcjADhF0xN6yyB-klF60SpG6CcN20s_FM12O_6oI04cznE71L777H2HIQTTPO5GaX6L1nFITlpTb_tu1noHS1nogah8V4Rek0aY-rCLSQgGsi2EYbP5R3AIJwynwlzM38_5fZP6qutP5C5pe71n1eGM5RaGy6Llke_P7pjzklkOvrEGEiA00WlosZJBcu4m_N1qlLVnjnYCUq49LWV0nuFczoGMhzE5Y0EIy1ysYzgdPLcjelrqxUs1dpf05OObVI3qnDMkzCObacEnwt_nrd28c1hBY2LaqiGXS1SasszrqWdKdVgvaQvRqT4HGbgeSwJr2H6N-aYXtgvHNo6E4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
بابک زنجانی:
الان کافه‌های مردم را می‌بندید بعد شب آدم می‌فرستید که بیاید تعامل کند.
می‌خواهم فیلم و مستند درباره این موضوع تهیه کنم... آن شخص هم فکر می‌کند که با ۱۰، ۲۰ سکه زندگی‌اش را گذرانده
بیکار کردن ۸۰ نفر در منِ بابک زنجانی چه اثری دارد؟! اصلاً فردا بیایید آتشَش بزنید.
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/71121" target="_blank">📅 09:30 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71120">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DgicCry2Qp8s22Jnc72XZUY6QfJjbp1-Gb-FgQMf6ZzRkZD6ck_v3rbxtagLIVwx-iG3oY_2hdOnD8pWccQf0libSIMv-7TBp-xvxfwC6h7gx2bP9eXEMsq0m6Mwf2_KF2RPAObxJgv2hj7XJGKXqhS67rchMC9stigSfjLmM0ckvJaagNm5qUQRLu0IXuvd5kRSl3Tom8i7v89EyWaiAuaje6q4EyEhMsf4k5Sqt7sNMkeaA3N_A9PEjgNsX9GAHBResetkCj-01Xbxp9pgDz53YbVmieJvfqai5aysZxy06YvVyvUjl7bg8KD5THWdgDx5fWFDv6UGBNYCxqQoJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇮🇷
🇴🇲
نیویورک پست:عمان بی‌سروصدا پیشنهاد ایران برای دریافت مشترک عوارض از کشتی‌های عبوری از تنگه هرمز — حتی به‌صورت داوطلبانه — را رد کرده است.
این اقدام، ادعای هفته گذشته سپاه پاسداران مبنی بر توافق دو کشور بر سر تقسیم درآمدهای این آبراه را تضعیف می‌کند.
عمان معتقد است که دریافت عوارض از کشتی‌های عبوری ناقض قوانین بین‌المللی است و تحت فشار آمریکا و کشورهای حوزه خلیج فارس، از این طرح عقب‌نشینی کرده است.
ترامپ دو بار تهدید کرده است که در صورت موافقت عمان با دریافت عوارض، این کشور را بمباران خواهد کرد.
ایران در دوران جنگ، نهادی برای مدیریت تنگه ایجاد کرده بود و از هر نفتکش مبلغی بین ۱ تا ۲ میلیون دلار عوارض می‌گرفت؛ اما بدون همکاری عمان، هرگونه سازوکار دریافت عوارض در دوران پس از جنگ، فاقد وجاهت قانونی خواهد بود.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/71120" target="_blank">📅 09:02 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71119">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71119" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/71119" target="_blank">📅 01:13 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71118">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oGicQy7qUgeHB3hstIA8-m7tZypk05e09caqmNJ0wqF5MJ52rkUSadxE1vD72SjR1I-tOdZgay3AKtJXdJNQjBmGq4Nk18YT0MVTOa3dWDXUVRNIMoZyA-C7fUg6A56EihLtVvQScNTnYZDCooN5eYbjg5IJO5Igcd9aEfSibexoRNl7F8sM-wKWazXicg2VWscvv4yXWWQSj0hl3VD28ifMJEtInNckb2gSVfUiPN8iAYfukS8TGMtIvqWC4Ykx6ciia6DdKTGRMQ7-HhrnZ8tzK4T2GHHQIg_8ixdfIVBwy67byKnS17EDyVSAySIfzoBcZ6NE96HkDtfcKv--ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
فقط یک بازی از میکس‌ت لوز شده؟
پولت برمی‌گرده!
میکس می‌بندی، هیجان بالا میره، اما یکی از انتخاب‌هات خراب می‌شه؟
با پیشنهاد ویژه
TrexBet
، در صورت رعایت شرایط، می‌تونی
۱۰۰٪ مبلغ شرطت رو پس بگیری
.
همین الان وارد سایت شو و شرایط آسان‌ش رو مطالعه کن!
💰
🦖
🦖
🦖
🦖
🦖
بونوس صدرصدی اولین واریز
🦖
واریز آسان، برداشت سریع
🦖
سرعت بالا، طراحی حرفه ای و تجربه ای متفاوت
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/71118" target="_blank">📅 01:13 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71117">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59487b6d80.mp4?token=aFYKKQ50rEbsA4aMfvTpwQ8NMxoJ9WDpf_GWB1_F9EMxejTmweUtmiewEEYidTOYsxEh0iM3DQ1xrbePtquhFgSACjjchhz5P9MVgPBkGyz9XG7sJDGGjMkxsp50gBMLcAoK7H5mVhOSRIpUnk_U3KKPsWcfLe5zNiEIV1NRl3ro0TMFmxk8oIF97XM_8EcfIv3SlxIQo3neMKezqsOOP8vJWZZxguJDUyhcVQsHXeSUsEYQf8MKBh0L3P9T-PhIajNZzY7JRo87aTMQB-EZPn1bYKEeQsjCAsDZ1y2IJaCuY0lhv2RuYoKWCWB1JcrQhVKQp7y7VPWkpBdnGCu1Sg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59487b6d80.mp4?token=aFYKKQ50rEbsA4aMfvTpwQ8NMxoJ9WDpf_GWB1_F9EMxejTmweUtmiewEEYidTOYsxEh0iM3DQ1xrbePtquhFgSACjjchhz5P9MVgPBkGyz9XG7sJDGGjMkxsp50gBMLcAoK7H5mVhOSRIpUnk_U3KKPsWcfLe5zNiEIV1NRl3ro0TMFmxk8oIF97XM_8EcfIv3SlxIQo3neMKezqsOOP8vJWZZxguJDUyhcVQsHXeSUsEYQf8MKBh0L3P9T-PhIajNZzY7JRo87aTMQB-EZPn1bYKEeQsjCAsDZ1y2IJaCuY0lhv2RuYoKWCWB1JcrQhVKQp7y7VPWkpBdnGCu1Sg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار:
مردم آمریکا چه زمانی باید انتظار تعیین تکلیف (resolution) در مورد ایران را داشته باشند؟
🇺🇸
ترامپ:
انقلاب(Revolution)؟
🎙
خبرنگار:
تعیین تکلیف(Resolution).
🇺🇸
ترامپ:
تفاوت بزرگی است. فکر کردم انقلاب(Revolution) جالب‌تر بود.
⭕️
🗒️
به دلیل تلفظ نزدیک دو کلمه راه حل/تعیین‌وتکلیف(Resolution) و انقلاب(Revolution) ممکنه ترامپ اینجا به عمد کلمه انقلاب رو انتخاب کرده باشه!
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/71117" target="_blank">📅 01:01 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71116">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76ef0c44cf.mp4?token=jBxmHflclscmj7UCx78gU-ALCASopVXYD7s7okIwz-2iK2V5QuerEOCLcFHX3iIxlgBw79ISXqGWcbrq6i5RHD60h9toeoY3bbj8XVjVllpPR51bR-hD0qzGH2SCNRDq3N13ys44DiiBdbOfCqcvIPhkhhRS20bd5v6utYYYI0NoRDJzpB1MetUhust22CH2g5Quzq9_8GTmuxFaHGrbZBmjdniv1sXsLJlAOuUvDp_EHD_5OPzfuJ-m3w4CMsk-Jrey_R7RABwecQIWz0JokaRf5I-d__u0D6JLcXCjOwTq8omwZE-5fDoDg1Rb_sMr8eQbRZxZsT9t3h_2979E3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76ef0c44cf.mp4?token=jBxmHflclscmj7UCx78gU-ALCASopVXYD7s7okIwz-2iK2V5QuerEOCLcFHX3iIxlgBw79ISXqGWcbrq6i5RHD60h9toeoY3bbj8XVjVllpPR51bR-hD0qzGH2SCNRDq3N13ys44DiiBdbOfCqcvIPhkhhRS20bd5v6utYYYI0NoRDJzpB1MetUhust22CH2g5Quzq9_8GTmuxFaHGrbZBmjdniv1sXsLJlAOuUvDp_EHD_5OPzfuJ-m3w4CMsk-Jrey_R7RABwecQIWz0JokaRf5I-d__u0D6JLcXCjOwTq8omwZE-5fDoDg1Rb_sMr8eQbRZxZsT9t3h_2979E3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تو ایتا و روبیکا از یچیزی رونمایی کردن که حتی خودشون هم نمیدونن چیه
😳
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/71116" target="_blank">📅 23:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71115">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c1e4d7b78.mp4?token=v4mcWhw-P1BiXhwgd-U_2R8XNG8r5wECaqDKPHloXueplCqjx8AB2T0qc2anaAfYp8Lpe6GwJ1T0Fvy7GoiOZfwsi_HQbLJVI_fmiV43LjApUeWwgKuUuDrB6CYsFEwozhS0OamIucdKqbh05TmVQiRMqrKkX0YUuMcLQHrPAasCwGiShLNTYJaRcogDboBlGooOMr59x24bShVVSedKUbEYHMlYdP9UBiRQoO_pavr8-_8BdQYDpqbAKgF8JYYuresXLbZGC1raZIssJ9wsjOC2cu1IAGF873E4OVvYvc_gTxEv0Lxb5fwtj-0ROFyN79k6WgU_McM3lbYAlbIlYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c1e4d7b78.mp4?token=v4mcWhw-P1BiXhwgd-U_2R8XNG8r5wECaqDKPHloXueplCqjx8AB2T0qc2anaAfYp8Lpe6GwJ1T0Fvy7GoiOZfwsi_HQbLJVI_fmiV43LjApUeWwgKuUuDrB6CYsFEwozhS0OamIucdKqbh05TmVQiRMqrKkX0YUuMcLQHrPAasCwGiShLNTYJaRcogDboBlGooOMr59x24bShVVSedKUbEYHMlYdP9UBiRQoO_pavr8-_8BdQYDpqbAKgF8JYYuresXLbZGC1raZIssJ9wsjOC2cu1IAGF873E4OVvYvc_gTxEv0Lxb5fwtj-0ROFyN79k6WgU_McM3lbYAlbIlYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
طرف اندازه یه گاری پول جمع کرده و الان آورده تبدیل به دلارش کنه، کل این همه پول نقد شد فقط ۳۰۰ دلار
!
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/71115" target="_blank">📅 22:52 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71114">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/05f93dafa7.mp4?token=Gcw6P6AfqH3pqLpbRr0Y6FDXb2DUvgW6gBd0_Hr00R2JnEjgBNBisPR-dUWAgcgzc8AygYyBnRjeZImFyM-L3eMBtVdRMHH6Ctu42HiWYn3iazN2nKH_rnML1KGefN59Y9lU9lqg-dQuQBUdkcK9D1Sct6p92bNdIpuaBgmtU9LOjjQRR0HQXAF5IVTe2rJiQimAW1c5eLKiXQ-Rt1FLi66Ccu4KSJswVQl77rHmYQnQljwNfWSGlES02DoeDw4R3N-80Wm7IIAemY6sTg0-TIdkImnopzgHkGoFO7iVMwxwGoTD517XhIf3m_zrBnOd_uji7p5Xg6nCSfCV1dHhT1DvrWRAGUmMzzk2pRyWs3g0pNlogI5nYrkvaGP2LRdHBXyNxTHG5r0C11m909cpYBeIFZrFq1_ejDJ2G1dFFiINNTrmhvfJ1BCHL_NjvO_EzzTPvxft6zQgcjDwDYnGzYUzHNzczFd72L5NpX73u-34zptx0gluBk2KudzOS32taQ0JzfSbZcJLyRGs1FZKoH2XuvaRUOwesSiI_5udwN7fzPveEA5s8xVhtGdC7rNGhfPlJg3F-Atch-ETTcmvsbaBEmX5Bmlbkob5nGv5E71Syy0qpFXMFF9Y3GsPscuTGBJEC8CgZkPEX7cCVAdjmhSgWI_Wy3Pt_BhlrqZUjNk" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/05f93dafa7.mp4?token=Gcw6P6AfqH3pqLpbRr0Y6FDXb2DUvgW6gBd0_Hr00R2JnEjgBNBisPR-dUWAgcgzc8AygYyBnRjeZImFyM-L3eMBtVdRMHH6Ctu42HiWYn3iazN2nKH_rnML1KGefN59Y9lU9lqg-dQuQBUdkcK9D1Sct6p92bNdIpuaBgmtU9LOjjQRR0HQXAF5IVTe2rJiQimAW1c5eLKiXQ-Rt1FLi66Ccu4KSJswVQl77rHmYQnQljwNfWSGlES02DoeDw4R3N-80Wm7IIAemY6sTg0-TIdkImnopzgHkGoFO7iVMwxwGoTD517XhIf3m_zrBnOd_uji7p5Xg6nCSfCV1dHhT1DvrWRAGUmMzzk2pRyWs3g0pNlogI5nYrkvaGP2LRdHBXyNxTHG5r0C11m909cpYBeIFZrFq1_ejDJ2G1dFFiINNTrmhvfJ1BCHL_NjvO_EzzTPvxft6zQgcjDwDYnGzYUzHNzczFd72L5NpX73u-34zptx0gluBk2KudzOS32taQ0JzfSbZcJLyRGs1FZKoH2XuvaRUOwesSiI_5udwN7fzPveEA5s8xVhtGdC7rNGhfPlJg3F-Atch-ETTcmvsbaBEmX5Bmlbkob5nGv5E71Syy0qpFXMFF9Y3GsPscuTGBJEC8CgZkPEX7cCVAdjmhSgWI_Wy3Pt_BhlrqZUjNk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇨🇳
یه بلاگر ایرانی رفته چین و ربات انسان نمای چینی رو به مبارزه طلبیده؛
حرکات ربات به قدری تمیزه که انسان واقعا از آینده جهان خایه میکنه!
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/71114" target="_blank">📅 22:16 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71113">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a66a864cef.mp4?token=sEjKZO9GQyALW9bWOqfDvmRXHOxAXoPB6_u01jnFroOt87FLjIp4nnhsol7XcA2QTK70LIsDsE6J_maUiWZVtHOutnFDQGonHc6rAavBM_2WEonkJqzRbwgvGcdYk7-ci7qt-WGwkQP7kFcNuPPAafjrQI2XpdC6VTfZueMNmAcYgapnmT6biuYNeQ7Uo0UlNeeSwn-jMwaQnzyIxXc8FD02XOdQPxx-cq6E3cSZh7dL_0Po9kp1Sd0POySkcZFXHkVFAda9WK6tGIHSsZnR8-oI0Yy6Q7g-9BODV4sKJ6sMib1e32P2vSVAQv7IP9cNH3lcyWFZHhBWzqubpY4tiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a66a864cef.mp4?token=sEjKZO9GQyALW9bWOqfDvmRXHOxAXoPB6_u01jnFroOt87FLjIp4nnhsol7XcA2QTK70LIsDsE6J_maUiWZVtHOutnFDQGonHc6rAavBM_2WEonkJqzRbwgvGcdYk7-ci7qt-WGwkQP7kFcNuPPAafjrQI2XpdC6VTfZueMNmAcYgapnmT6biuYNeQ7Uo0UlNeeSwn-jMwaQnzyIxXc8FD02XOdQPxx-cq6E3cSZh7dL_0Po9kp1Sd0POySkcZFXHkVFAda9WK6tGIHSsZnR8-oI0Yy6Q7g-9BODV4sKJ6sMib1e32P2vSVAQv7IP9cNH3lcyWFZHhBWzqubpY4tiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اخیرا بعضی دخترا طی یه حرکت فوق‌العاده و زیبا، دارن هرچی ژل و بوتاکس تو صورتشون بوده رو خارج میکنن تا نچرال به نظر بیان
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/71113" target="_blank">📅 21:29 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71112">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from[ 𝐇𝐨𝐭𝐍𝐞𝐰𝐬➕]</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XixgZy09QVGHQHC8Un6g7MDHFKhr871xkah7ss13Zs2Jyi9af-6VDPwNNqNfgdQcvKCU_h8ZC-isHB1yf2TeL3wMMRlFyDj1TmmpElZapspgpheHgkkF6Cu_SIX319BW0Pnv3gFY6-XZsg4AnoXKtk3MGUUgzP4Bq-jE9yXbnovtYIa87rSnsFvGy5ZNDLh-cqWa6p1nzgjW9ophDRJJ0Z4fSj-D8HWasNUaWvW5Gaoplj8cBAZy_vZBjmzRkAp9_HoGTy7mJ7SmdK-DNWDS2UHOW3VtryuOGitNExzroqnhmhAeSCrjoAPaafxmgXjtV90_2Nu_1GaJORB4EokGQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👎
قرارگاه خاتم الانبیا: حملات پیش دستانه علیه پایگاه آمریکا در اردن که در حال آماده سازی برای حملاتی علیه کشور بودند را انجام دادیم!
❌
خبر بالا که بطور گسترده در حال انتشار در رسانه هاست فیک و نادرسته، همونطور که می‌بینید سپاه پاسداران و قرارگاه خاتم‌الانبیا هیچ اطلاعیه‌ای مبنی بر حملات پیش‌دستانه منتشر نکرده
@HutNewsPlus</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/71112" target="_blank">📅 21:28 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71111">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dNB5jYWsRzTXb5CRBX96Su1vvlt1oCUGh9U3shEvextoDKPPdUbVV47RLeyApNPNk4cc-JHQVCnLTbl3kYbJtF248eEAYB17ZT-27PKQRR5PcmKZ6KJ7UuLvIU4Jep9dCd_6cHLlGUN792wFM0CO4LFtY5wfy5Qi0n58PoGrceW2S0S2VTnz1Ede9rOClIjXVnf9XbA_WjLNF3RB7PdSyZdb85hM3UTDRrttwyWJiZtPyAMsjju8VR0cZ4vjYAFa69Wdd4-99Hgmyw3R6gG2ZCQnGBnnu9khH5ySvnwPh0EFXLaOE6eYbKnj1t_uQzqAnPwfaThlQHtS9JtScRFoDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقام ارشد آمریکایی به کانال 12: در حال حاضر هیچ اطلاعی از وقوع آتش‌سوزی در پایگاه‌های آمریکا در اردن وجود ندارد.
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/71111" target="_blank">📅 21:04 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71110">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c74f1d2d4f.mp4?token=H_lLoWMaC3ZTN0ZCPNIUvgrpV-VPIpAcHmfUBJScfciBTg7UBDqi6pBWFCzbGzdQj8OLo6XCU1s6uZW8gP4uBLzvIL-KKp2yddmdXoPPlFG-1YdLDlIgVQ9VDFhx3mOUqV3npnECWyF3fVDsRZ3nexfU4CxDxoN5UXuwoCzR4RjSGclmIx9Ec4A2LBcZ4J9us-3VgxDQJbp7owwnKl_RZga4zvheVx7WYsIzI7Nfxwl8_VQqhab739-7BDVh3rmFkRFVeGMSxv-kpZTAfwQtVQ-1rm-Ja6REBEJmTbXbmnpDwgFUGY7pSdgoXwX3nmyrd0IMM0L83Ci5FQ1fmuaq3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c74f1d2d4f.mp4?token=H_lLoWMaC3ZTN0ZCPNIUvgrpV-VPIpAcHmfUBJScfciBTg7UBDqi6pBWFCzbGzdQj8OLo6XCU1s6uZW8gP4uBLzvIL-KKp2yddmdXoPPlFG-1YdLDlIgVQ9VDFhx3mOUqV3npnECWyF3fVDsRZ3nexfU4CxDxoN5UXuwoCzR4RjSGclmIx9Ec4A2LBcZ4J9us-3VgxDQJbp7owwnKl_RZga4zvheVx7WYsIzI7Nfxwl8_VQqhab739-7BDVh3rmFkRFVeGMSxv-kpZTAfwQtVQ-1rm-Ja6REBEJmTbXbmnpDwgFUGY7pSdgoXwX3nmyrd0IMM0L83Ci5FQ1fmuaq3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
شلیک موشک ها از ایران به سمت اردن
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/71110" target="_blank">📅 20:29 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71109">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
منابع عربی:چندین انفجار در اردن رخ داد
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/71109" target="_blank">📅 20:13 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71108">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cbf8f1e1a9.mp4?token=bBRZiwKN6-4Y5RdLcamuPI7VB37EvNOs6HoAK48ptnuF3U4A7ColS5DylXMmqLcXebV9SNswsnNYAc7RnTnm4aFeRvOt4PHn0_PO1pUCMKXhdNmuUh2RikkbSIkv49IFL4BZOSqw8ryQqqudJSjUQYJJyx1oxJURjJZMbaQx8tF0MiGbe7K1JHdK_mvmFqNKyPxXpwlvK3iwjEsnlrVgSczp0KkSNHl_1q9f97_E3yzcx9Xtr1unc4HiCotaJi2jnr1gFs1or28v2NkUO-kRNEwsOeyP9dZtnO5hJ8EjQsyzQXoSWo1seFCamve31cUJfkAwPaUCD_uFWh8gQ1pEZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cbf8f1e1a9.mp4?token=bBRZiwKN6-4Y5RdLcamuPI7VB37EvNOs6HoAK48ptnuF3U4A7ColS5DylXMmqLcXebV9SNswsnNYAc7RnTnm4aFeRvOt4PHn0_PO1pUCMKXhdNmuUh2RikkbSIkv49IFL4BZOSqw8ryQqqudJSjUQYJJyx1oxJURjJZMbaQx8tF0MiGbe7K1JHdK_mvmFqNKyPxXpwlvK3iwjEsnlrVgSczp0KkSNHl_1q9f97_E3yzcx9Xtr1unc4HiCotaJi2jnr1gFs1or28v2NkUO-kRNEwsOeyP9dZtnO5hJ8EjQsyzQXoSWo1seFCamve31cUJfkAwPaUCD_uFWh8gQ1pEZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⭕️
🇮🇷
🇨🇳
بِسِنت درباره ایران:
آن‌ها محموله‌های نفت را به سمت چین روانه کردند. منتظر اقدامات مربوط به این موضوع در روز سه‌شنبه باشید.
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/71108" target="_blank">📅 20:11 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71105">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64aa07a7bb.mp4?token=PlHnEkvps3l0omtKSbg81ZkI-bx-keSCNyTgCmIxQZMtMB4AxFzHhi-vfoQZoxeEyS7fHuBoAgZSOj84gzP4fOL3pte_ORIXAUsFZNQuPdv4sCVBNSnagnpPtCaktesqJrsjMQw1oa1Sb8e8xZIQCYDb_FzMijVu06CJlt9dwa3rSS_6DFskc17FaV9zgmIJAoGgjfUineapIuVqBIqIcWE48lzBL-xfw61YjgwlFqYwn64Ywq3f2DX7hLYVCq2Be6dHOO_ubQy7l5IlVAF_CNIFS2H5TuvlxdI_nHMUVXA98MJtL9h4RWgJKecVhhKSl1JzbdS0eOZdEZvGNN1HTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64aa07a7bb.mp4?token=PlHnEkvps3l0omtKSbg81ZkI-bx-keSCNyTgCmIxQZMtMB4AxFzHhi-vfoQZoxeEyS7fHuBoAgZSOj84gzP4fOL3pte_ORIXAUsFZNQuPdv4sCVBNSnagnpPtCaktesqJrsjMQw1oa1Sb8e8xZIQCYDb_FzMijVu06CJlt9dwa3rSS_6DFskc17FaV9zgmIJAoGgjfUineapIuVqBIqIcWE48lzBL-xfw61YjgwlFqYwn64Ywq3f2DX7hLYVCq2Be6dHOO_ubQy7l5IlVAF_CNIFS2H5TuvlxdI_nHMUVXA98MJtL9h4RWgJKecVhhKSl1JzbdS0eOZdEZvGNN1HTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
بابک زنجانی: دلار رو بدید دست من تا یک سال رو همین قیمت نگهش میدارم وگرنه با همین فرمون کشور تا یک سال دیگه نابود میشه.
من رو ۷ سال بدون بدهی انداختن زندان و همشم تو انفرادی بودم. همه اموالمم ازم گرفتن. وقتی آزاد شدم حتی ۱ دلار نداشتم.
با چند تا تلفن ۱ میلیارد دلار پول جور کردم و چندتا شرکت تاسیس کردم.
من میخواستم سایپا رو به قیمت ۲ میلیارد دلار بخرم که نشد ولی خودم میخوام کارخونه تولید خودرو تاسیس کنم
من توی خارج کشور بانک داشتم پولای وزارت نفت تو اون حساب بود. اونا تحریم شدن پولاشون اونجا گیر کرد گفتن تقصیر توعه و حکم اعـدام بهم دادن
تمام بانکای ایران بیان جلوی من بشینن ببینیم من بیشتر میتونم سرمایه جذب کنم یا اونا. فقط با چندتا تلفن. تا معلوم بشه کی اعتبار داره
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/71105" target="_blank">📅 19:28 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71104">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf31ca2a30.mp4?token=vLO-QjozVKf5Yd4wKD3BSl8ujqAAoXMtQb5Bs0siUvn5d1EkI0usrVXItXaL26QftvUVpycoko_BchRmvTjGaL5yb385GOZqPLygKYFPOPIp-eWH-arAr2_5jOjMa_T5qK57HlvZjO1fwmM6cEeKsdDa5Yiklt1OgPiF7Z6SgG1kTNaXLuXc-3JxIzkJ0RJfvXXc0PASIkSvIE87F_RlF5Qn_B3lYEBKuk1ce8DaY4khhSwn1TXDpYmr9ejUsZvXeG14zTKtyvmnzNCE2i7Yz896g2Saq09GCzWHhwzEGfrNxeMKT4iO3TkvJ1lSz3SY5csl1tEusY2V0HoWqVRJUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf31ca2a30.mp4?token=vLO-QjozVKf5Yd4wKD3BSl8ujqAAoXMtQb5Bs0siUvn5d1EkI0usrVXItXaL26QftvUVpycoko_BchRmvTjGaL5yb385GOZqPLygKYFPOPIp-eWH-arAr2_5jOjMa_T5qK57HlvZjO1fwmM6cEeKsdDa5Yiklt1OgPiF7Z6SgG1kTNaXLuXc-3JxIzkJ0RJfvXXc0PASIkSvIE87F_RlF5Qn_B3lYEBKuk1ce8DaY4khhSwn1TXDpYmr9ejUsZvXeG14zTKtyvmnzNCE2i7Yz896g2Saq09GCzWHhwzEGfrNxeMKT4iO3TkvJ1lSz3SY5csl1tEusY2V0HoWqVRJUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇺🇸
بسنت درباره ایران:
متحدان ما در امارات متحده عربی در خصوص این بانک مستقر در دبی همکاری بسیار مؤثری داشتند. اکنون ما برای متوقف کردن تمامی این جریان‌های مالی غیرقانونی، با آن‌ها وارد همکاری شده‌ایم.
ما برای رفع این مشکل با آن‌ها همکاری خواهیم کرد، چرا که بانک‌های متعددی در سیستم مالی آن‌ها فعالیت می‌کنند.
ما نمی‌خواهیم این بانک‌ها را نابود کنیم — هرچند اگر لازم باشد چنین خواهیم کرد — اما اکنون همه کشورها در این مسیر با ما همراه شده‌اند.
این پایان کار برای این رژیم است؛ آن‌ها یا باید [رفتار خود را] عادی‌سازی کنند و یا با عواقب آن روبرو شوند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/71104" target="_blank">📅 18:41 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71103">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38e7eb93ff.mp4?token=kRYAXEYlZYEFbfMJKjOPj0DvuWOccmBUcUnOsDhvjRXBPjUg2vxYQAym1JMeR0ggqg5GWgbrEF_MHiq_VhuezS1eFdEyokfnjJ94Qvlf97tL1WZZmTgjumtel4QMId8asBpnrKCZkfHcqKBPt0aL53fmepH_x1NLkfw7efnEfnPoOa9ajew11pjCpi83SPDVzEp2eRco-Pa_h-RZPGFXX-1XK-HrcGIkvoueVAToyrrjL4M1XFhRF14gmaA-XEdEpx_yb5sIPu_HDauJWStmOUB5Yw6U_040BqiiKqAodmEU6mItRWKTyg3JvoWqMwyherF5peEN4dNz_zAwkEDrNFZ3xJpQoQ772wU_Ns_6kKoqk5IGeKn_SnxwtT1lC9PyXhLL8clSiMXa2wEAXWKC4YQeZ_YS3LJsRaN_nym3eEAY93re980xV-wq56IdYFLthEXWOXPc8rHMCrWengQzkn-rnNWQfArKXB1O8M-5I-tfZoD4lOs3bfovzmYK9fH65Jy9xnkGBAwrca-4c8O8wWFwTwBV0A74ZlKSTlyYlQAG-VyJFefcBZwe1WQD38OvBCw655ODW4q5Ye7qxmqmcGJHgPvw53vbEmLB8uLpbigKttuL5ZUWnl2ZTDRCFfi8BdUP6sJKvsI9Qv-YHGFvmfc6Bv6KoyprOKeRDuW3yTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38e7eb93ff.mp4?token=kRYAXEYlZYEFbfMJKjOPj0DvuWOccmBUcUnOsDhvjRXBPjUg2vxYQAym1JMeR0ggqg5GWgbrEF_MHiq_VhuezS1eFdEyokfnjJ94Qvlf97tL1WZZmTgjumtel4QMId8asBpnrKCZkfHcqKBPt0aL53fmepH_x1NLkfw7efnEfnPoOa9ajew11pjCpi83SPDVzEp2eRco-Pa_h-RZPGFXX-1XK-HrcGIkvoueVAToyrrjL4M1XFhRF14gmaA-XEdEpx_yb5sIPu_HDauJWStmOUB5Yw6U_040BqiiKqAodmEU6mItRWKTyg3JvoWqMwyherF5peEN4dNz_zAwkEDrNFZ3xJpQoQ772wU_Ns_6kKoqk5IGeKn_SnxwtT1lC9PyXhLL8clSiMXa2wEAXWKC4YQeZ_YS3LJsRaN_nym3eEAY93re980xV-wq56IdYFLthEXWOXPc8rHMCrWengQzkn-rnNWQfArKXB1O8M-5I-tfZoD4lOs3bfovzmYK9fH65Jy9xnkGBAwrca-4c8O8wWFwTwBV0A74ZlKSTlyYlQAG-VyJFefcBZwe1WQD38OvBCw655ODW4q5Ye7qxmqmcGJHgPvw53vbEmLB8uLpbigKttuL5ZUWnl2ZTDRCFfi8BdUP6sJKvsI9Qv-YHGFvmfc6Bv6KoyprOKeRDuW3yTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⭕️
🇺🇸
بسنت، وزیر خزانه‌داری آمریکا، درباره ایران:
همه خواهان پایان یافتن این وضعیت هستند. ۴۷ سال از عمر این رژیم شرور می‌گذرد و دنیا دیگر از دست آن‌ها به ستوه آمده است.
مردم ایران مردمی عالی هستند؛ اما رژیمی سرکوبگر بر آن‌ها حاکم است.
یا رژیم از درون تغییر خواهد کرد، یا مردم قیام خواهند کرد، و یا باید دید چه پیش می‌آید.
ما آن‌ها را از نظر اقتصادی خفه خواهیم کرد. آن‌ها در وضعیتی قرار دارند که من آن را «آرواره‌های مرگ اقتصادی» می‌نامم.
ارزش پول ملی‌شان در حال فروپاشی است و صادرات نفت آن‌ها به صفر رسیده است.
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/71103" target="_blank">📅 18:30 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71102">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/13cf8fb01d.mp4?token=GP7jAF55K6XdJvmdw0xsRyCnrjqRJ2jy0z62glq-TcnOjKvl-u1Tvbrt6amSyFLKQ-3w5auLNsYKYRn3QE2G2oy-2qc8GWV8cdVLeYAWXnFrZ1tXhOKLXGS6wY1B1W2DN4jLTJMAdXvbT379FQxwsezRNjERT0e5xIRancsuRxidmBHnCMvtqpnUQ2w6qFj9qBnUTctzQjhMhUFyXyvNdniN-sU0GiDFukMxswvZA6Cx0_a3_Uj_j0RBp_wxYnd1dZ6Xjy_8EjDdYmRNqGtkP_weESgNNdcA5qmoHHSwl1R5pWmfGRCTN-NDTwRMciU6g1FJvy4YLp9xoZXkYfjFaYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/13cf8fb01d.mp4?token=GP7jAF55K6XdJvmdw0xsRyCnrjqRJ2jy0z62glq-TcnOjKvl-u1Tvbrt6amSyFLKQ-3w5auLNsYKYRn3QE2G2oy-2qc8GWV8cdVLeYAWXnFrZ1tXhOKLXGS6wY1B1W2DN4jLTJMAdXvbT379FQxwsezRNjERT0e5xIRancsuRxidmBHnCMvtqpnUQ2w6qFj9qBnUTctzQjhMhUFyXyvNdniN-sU0GiDFukMxswvZA6Cx0_a3_Uj_j0RBp_wxYnd1dZ6Xjy_8EjDdYmRNqGtkP_weESgNNdcA5qmoHHSwl1R5pWmfGRCTN-NDTwRMciU6g1FJvy4YLp9xoZXkYfjFaYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇺🇸
بسنت، وزیر خزانه‌داری آمریکا، درباره ایران:
ما بانک دیگری را که با ایران مرتبط است، تحریم کردیم. هفته گذشته، یک بانک مصری را که پنج شعبه در دبی داشت و ۱.۸ میلیارد دلار در اختیار این رژیم قرار داده بود، تحریم کردیم.
امروز بانک دیگری را تحریم خواهیم کرد و احتمالاً هفته آینده نیز بانک دیگری را تحریم می‌کنیم.
ما به سیستم مالی می‌گوییم:
ای عوامل مخرب، ما می‌دانیم شما چه کسانی هستید. خودتان هم می‌دانید چه کسانی هستید. کارتان تمام است.
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/71102" target="_blank">📅 18:27 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71101">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🚨
⭕️
🇹🇷
🇮🇷
وزارت خزانه‌داری آمریکا سه نهاد مستقر در ترکیه را به‌دلیل ارتباطات مالی و فعالیت‌های مرتبط با ایران تحریم کرده است:  Golden Global Portföy Yönetimi Golden Global Varlık Kiralama Golden Global Yatırım Bankası
⏺
هم‌زمان یک مجوز عمومی برای دوره جمع‌کردن…</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/71101" target="_blank">📅 18:23 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71100">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🚨
⭕️
🇹🇷
🇮🇷
وزارت خزانه‌داری آمریکا سه نهاد مستقر در ترکیه را به‌دلیل ارتباطات مالی و فعالیت‌های مرتبط با ایران تحریم کرده است:
Golden Global Portföy Yönetimi
Golden Global Varlık Kiralama
Golden Global Yatırım Bankası
⏺
هم‌زمان یک مجوز عمومی برای دوره جمع‌کردن معاملات (wind-down) با این نهادها صادر شده است
@News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/71100" target="_blank">📅 18:14 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71099">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/372294672d.mp4?token=q8iHCu-d_vu-gvVakUAfSBqIwpZPdIauKN0EXozp9gCFr5IcSNiDS8hgoFOvV9K6OHNVZpD1Sa356P282dEUw4uekkQjih_ocPVNggsyQcH831jlh4ISc38zlUkm10Q3u_-gZ94dog-5e-9MjPeZAABeKLUtaehR_L5mfOSpdCKB-X1FDaVHeecT2cEjQTM-n7kF_cT5UAo-NPI_gO5lo_yTKZIEauA6Kj5DOrJ6wmJuIzToidq8e_vEOmLQK9z_B5qX3XPOW2nKHZmVj5MpaGMdiul6lBQLNx58nQRmoDlroP1ki0glhWiEJnuxb6nYZCdpicMsQMQIIqp7OaXSuDzR-odQD6zykQMqtrHO5xSh8JAQ6GTG68zS3ThJxOCqnE-QODDmNBNHUrxG5d4nnVBh507jOfDr_OgyPhKVnWnGb5q_ZDggo-8xd812lUebaF5Tl6SetQPu61fm9MtmsiH9DmW5B0dTu3UL-G4suvwiCWViKTO6wf0sJ1vyN7hcxCA4YB5LAnqAtscW9Tb8wC36dUd_tJXcWsKPsCPXb_4GgXs1a3xMARFgHtpPVB5laTHSmn17YQ4qX_c2xzNT4YdJqSmXcNkwAASBNwC99X41Po22IMD6jBwiigBEripwNcxGe3t2OTG8K8TfbkyKNO-RYXOxWiNAfT1OWB3_lUk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/372294672d.mp4?token=q8iHCu-d_vu-gvVakUAfSBqIwpZPdIauKN0EXozp9gCFr5IcSNiDS8hgoFOvV9K6OHNVZpD1Sa356P282dEUw4uekkQjih_ocPVNggsyQcH831jlh4ISc38zlUkm10Q3u_-gZ94dog-5e-9MjPeZAABeKLUtaehR_L5mfOSpdCKB-X1FDaVHeecT2cEjQTM-n7kF_cT5UAo-NPI_gO5lo_yTKZIEauA6Kj5DOrJ6wmJuIzToidq8e_vEOmLQK9z_B5qX3XPOW2nKHZmVj5MpaGMdiul6lBQLNx58nQRmoDlroP1ki0glhWiEJnuxb6nYZCdpicMsQMQIIqp7OaXSuDzR-odQD6zykQMqtrHO5xSh8JAQ6GTG68zS3ThJxOCqnE-QODDmNBNHUrxG5d4nnVBh507jOfDr_OgyPhKVnWnGb5q_ZDggo-8xd812lUebaF5Tl6SetQPu61fm9MtmsiH9DmW5B0dTu3UL-G4suvwiCWViKTO6wf0sJ1vyN7hcxCA4YB5LAnqAtscW9Tb8wC36dUd_tJXcWsKPsCPXb_4GgXs1a3xMARFgHtpPVB5laTHSmn17YQ4qX_c2xzNT4YdJqSmXcNkwAASBNwC99X41Po22IMD6jBwiigBEripwNcxGe3t2OTG8K8TfbkyKNO-RYXOxWiNAfT1OWB3_lUk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
تیزر دوم فصل اول سریال هری پاتر که از کریسمس 2027 قراره پخش بشه
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/71099" target="_blank">📅 18:13 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71098">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71098" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/71098" target="_blank">📅 18:13 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71097">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bnp9TY0pUoLwQUe7ATuY_ZluL2HAb_4P1Tp3fhEyzI5yQbWw7wZUksASiAvnL80qsFEQcPNwZz95gcHT_cZ4AJt0RMs_9usFyFGUIpJb5ptIrfMIjQR6JbeKfaDHKROmJxP3Jf32af6J41fr7v2TKsVA_qlJmSZJCVUCMjRDFhaL3m5bx82mxRYPIszOmlC1gMN2apPF4fRvkTylLTmiBSAcHF4mLSh5BZ9Zq2LcEbFtrobtZO-6aJMp3qQZ4YgFJ0Dounk-9nJFMl_z3cYzFatI9ga5HFuSevrxgPu7WwHr0tl7EuZWyehzIfamjl6V6BdXrKmuPrMPsXiHcGeK1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
بازی جذاب
⚽️
پاری‌سن‌ژرمن
🆚
موناکو
⚽️
را در سایت بین‌المللی
TrexBet
پیش بینی کنید.
📊
مونامو ۲ برد | ۱ تساوی | ۲ شکست | ۹ گل زده
پاریس ۲ برد | ۱ تساوی | ۲ شکست | ۱۰ گل زده
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/71097" target="_blank">📅 18:13 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71096">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">〰️
سنت‌کام:
بیش از ۲۶۰۰ تفنگدار دریایی و سرباز نیروی دریایی آمریکا، بر روی ناو جنگی USS Boxer (LHD 4) مستقر هستند و این ناو جنگی در حال حاضر در خاورمیانه در حال انجام ماموریت است.
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/71096" target="_blank">📅 17:32 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71095">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9fcc841fe5.mp4?token=Q5zy1b8tE6kr5UTcc6oe_xTqJjNNrTRuvdynbkmzqNq0CRru8SFO8A8nNsBAI2jw88x01ADbjlW_BZfQxp5NN16cPLuEnu0FxBZZd7FlxZ-k3LY0N5G_zy7mZyRug7qjOXBiaZ94Nu5rJnFGldW_XVWQ-oNBgR5Fq7qLemUU8137E5cNy20VVbxGmMlkn_hjJu2wUXXWBRU1VEwcrsuXnNdtkJxGqnr1FPn_mocTUfv6C7kYVrSgVA3ISo28AuWQ3aHw61enJjYBaPWGskpdVdF5a5LqrTKTWOF3iq04GuC_JjYHvdXjbK5_DYL7CyrpP3-MbV1EsNJ_8oLnuK7bdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9fcc841fe5.mp4?token=Q5zy1b8tE6kr5UTcc6oe_xTqJjNNrTRuvdynbkmzqNq0CRru8SFO8A8nNsBAI2jw88x01ADbjlW_BZfQxp5NN16cPLuEnu0FxBZZd7FlxZ-k3LY0N5G_zy7mZyRug7qjOXBiaZ94Nu5rJnFGldW_XVWQ-oNBgR5Fq7qLemUU8137E5cNy20VVbxGmMlkn_hjJu2wUXXWBRU1VEwcrsuXnNdtkJxGqnr1FPn_mocTUfv6C7kYVrSgVA3ISo28AuWQ3aHw61enJjYBaPWGskpdVdF5a5LqrTKTWOF3iq04GuC_JjYHvdXjbK5_DYL7CyrpP3-MbV1EsNJ_8oLnuK7bdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ببینید از خانمی که داره از تجربیات رفتن خودش به تور کویر میگه...
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/71095" target="_blank">📅 17:02 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71094">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf229661bf.mp4?token=aJ4kZuIjolgVxYUGCxTZ9SX3ZWYOi2S4AFGjV0BKi5xUtDs3VmJnKm9FxWSX0piLKQvEaNSUM4tZdX4eYwtbSE4r51IBhItQG5CwJYJREW4zZAG2C4d5mBWAj7aEHHA5XuZ5wybyYhZmDlwQeEAzvlMnmuEn-Th7CkaEJGHrSwX1ThDfZN_-U6uPBB8WbO-Yenwi5AHunhxbWZtG_44BbXsPb_Cw5G_rJtKOMglW5CDcWlgX-jG5xdmjHztIQMdFefBbBrAk6eUrDTz7HzkKLDqT_HplziFIIJPGd6CGkRrmlF5ksXWdSLBqA8hQTY3711rjA64T83XhO1YvQW77FQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf229661bf.mp4?token=aJ4kZuIjolgVxYUGCxTZ9SX3ZWYOi2S4AFGjV0BKi5xUtDs3VmJnKm9FxWSX0piLKQvEaNSUM4tZdX4eYwtbSE4r51IBhItQG5CwJYJREW4zZAG2C4d5mBWAj7aEHHA5XuZ5wybyYhZmDlwQeEAzvlMnmuEn-Th7CkaEJGHrSwX1ThDfZN_-U6uPBB8WbO-Yenwi5AHunhxbWZtG_44BbXsPb_Cw5G_rJtKOMglW5CDcWlgX-jG5xdmjHztIQMdFefBbBrAk6eUrDTz7HzkKLDqT_HplziFIIJPGd6CGkRrmlF5ksXWdSLBqA8hQTY3711rjA64T83XhO1YvQW77FQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
سامسونگ A17 که یکی از ضعیف‌ترین و تخمی‌ترین‌ گوشی‌های بازار به حساب میاد، قیمتش به 100 میلیون تومن رسیده.
البته این قیمت واسه دیروزه و امروز احتمالا گرونتر شده.
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/71094" target="_blank">📅 16:30 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71093">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc7b61838f.mp4?token=rGzos_7xVNXQHoaX2Obpyq1qvOSm059ojHPy18xlu-qs0XitAqOas_68G_ZkGP5JzV9LgCJezYV5tMV5WF7ljtnYud93TrLcI_mK221FScOqm6-yjNLpTOxEf95rtSdptsGNMSE_RcPFyYIH65CjhxPu4ulKO85oFFqjSYnqGNCirZ5mm6HRQGwb1EsAZ_XQUP0_9m8rEhqTqrTW4UDHrFpMS4QaMNg0k_jN4bUl_kqIx1bxQjhly0B25-yE5q8hwaW89eFSEZOr61IbmTLOQu_w5YLGlaKLhFJjBHZKt0iqVwPh_UZntOvxw3V7DJYwxhAHSZnsy6xdbAFCUYrsLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc7b61838f.mp4?token=rGzos_7xVNXQHoaX2Obpyq1qvOSm059ojHPy18xlu-qs0XitAqOas_68G_ZkGP5JzV9LgCJezYV5tMV5WF7ljtnYud93TrLcI_mK221FScOqm6-yjNLpTOxEf95rtSdptsGNMSE_RcPFyYIH65CjhxPu4ulKO85oFFqjSYnqGNCirZ5mm6HRQGwb1EsAZ_XQUP0_9m8rEhqTqrTW4UDHrFpMS4QaMNg0k_jN4bUl_kqIx1bxQjhly0B25-yE5q8hwaW89eFSEZOr61IbmTLOQu_w5YLGlaKLhFJjBHZKt0iqVwPh_UZntOvxw3V7DJYwxhAHSZnsy6xdbAFCUYrsLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
یک راننده کامیون:
الان کنار مرز پاکستان هستیم میخوایم رد بشیم اجازه نمیدن.
رفتیم پیش رئیس گمرک میگه طرف پاکستانی اجازه ورود نمیده.
پاکستان گفته به ازای هر ماشین باید دو میلیارد تعرفه بدین.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/71093" target="_blank">📅 16:02 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71092">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45bdb5a184.mp4?token=emTUTX-mZD-lKzRRcPu94y52W_-HvBN9SBFqaRgnfQhufz6wUGfmbgjhRmxiB0oZvSkJvznjSIrrN4ysDJO67A_RrtTocxSFq53maU-AGb3YO_z4TpSHeML-5c0cAH1_enpeQaEV7DMeg266DrszsQGstVUuIaqWWnScp8CNzkHEcWm0dUcGEXe_cYsdnRBtxbJ0jf0vmvDVKflFe_M6sY2Mkf0DfHJYAW6DnPtJHWCy3HE1utCDqame9gBCs0pxKqjMRGQUIRm5UIMxeiB6NAyXBh87efLtnOHwy2bisNKhahc72HM1Vlu4bqShNfAVrrtbk-n4PkfxNs271WBHWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45bdb5a184.mp4?token=emTUTX-mZD-lKzRRcPu94y52W_-HvBN9SBFqaRgnfQhufz6wUGfmbgjhRmxiB0oZvSkJvznjSIrrN4ysDJO67A_RrtTocxSFq53maU-AGb3YO_z4TpSHeML-5c0cAH1_enpeQaEV7DMeg266DrszsQGstVUuIaqWWnScp8CNzkHEcWm0dUcGEXe_cYsdnRBtxbJ0jf0vmvDVKflFe_M6sY2Mkf0DfHJYAW6DnPtJHWCy3HE1utCDqame9gBCs0pxKqjMRGQUIRm5UIMxeiB6NAyXBh87efLtnOHwy2bisNKhahc72HM1Vlu4bqShNfAVrrtbk-n4PkfxNs271WBHWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
یه دختر حامی حکومت:
فک کردین اومدم از قیمت دلار آه و ناله کنم؟ نه اومدم پاره‌اش کنم!
رزق و روزی دست خداست نه آمریکا، دلار قیمتش عوض شده، خدای ما که عوض نشده.
قیمت دلار هر چقدرم بشه، باز روزی مارو خدا می‌رسونه، منم اعتراض دارم ولی ناامیدی تزریق نمی کنم.
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/71092" target="_blank">📅 15:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71091">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2be4c50b6.mp4?token=OeX6HZcY033XSD04aIcOmiY3T-nLNGgarptNDAEOPtQOlm1IKxQBloC7QY23RNGFHrYfMjATZGJ-q_PgfL1TmCLoY_8-syVg318IOZ-7SJ88wUYGvReAfcX9IhL3t5NfX6YCPqNtmj8mwI8Ka6YvZJalDzOArSATo2_yWtdMRs9Q379MUuAb4j_SJlNhw9yx5-z--CfcZaFdhItu71qmx-hb2ohL0i8U7ojGtuevZA31DZSOs4SiK_QrQZd3Nqjwzt9cmPv_dNOZQF1WRgZd14bDlBOIRcrin8P221KI6pYcy_e4UciuwgBJsC_XntNyNI3vzN_goYxyNcUpuOit0jzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2be4c50b6.mp4?token=OeX6HZcY033XSD04aIcOmiY3T-nLNGgarptNDAEOPtQOlm1IKxQBloC7QY23RNGFHrYfMjATZGJ-q_PgfL1TmCLoY_8-syVg318IOZ-7SJ88wUYGvReAfcX9IhL3t5NfX6YCPqNtmj8mwI8Ka6YvZJalDzOArSATo2_yWtdMRs9Q379MUuAb4j_SJlNhw9yx5-z--CfcZaFdhItu71qmx-hb2ohL0i8U7ojGtuevZA31DZSOs4SiK_QrQZd3Nqjwzt9cmPv_dNOZQF1WRgZd14bDlBOIRcrin8P221KI6pYcy_e4UciuwgBJsC_XntNyNI3vzN_goYxyNcUpuOit0jzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🚀
🇰🇼
روز گذشته، یک پهپاد انتحاری که توسط ارتش جمهوری اسلامی پرتاب شده بود، یکی از واحدهای برج مسکونی الدیره در شهر کویت را هدف قرار داد. این اصابت باعث آتش‌ سوزی و تخریب کامل آن واحد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/71091" target="_blank">📅 14:57 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71090">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a0b6b730d.mp4?token=LAUVMmtPhfF8rG78u0w7X5rQwBKizjFawU-mIBc3lsWDlw5IL-XwAZtLonHpKzT1CYEk-wJ2ZD-5Pdn7sHBgAutItXkEw3HUs_IuUjX6SrJR0ENEkOUiIJvUHeo5T6QEpr544LhyiwangaBqvPdik0LqRzaGCzU4BuIGmTfU5BEFuksbR9I0SNtKQP3uCd7hT1klTuSxlzu5V-AtMxwRJwSfEnvgEypmj6T1HIwsfIwgiT6cJ0B4ZBjcb9QZ8ki8Zfp3uXvC9MTXpd2iKsVp75kFyf6vR95M-bHYIFBcOQxpQ7eT4FhF6yPTXx7UaVcBiJ6BwW-G2LSpA5pYBjNp_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a0b6b730d.mp4?token=LAUVMmtPhfF8rG78u0w7X5rQwBKizjFawU-mIBc3lsWDlw5IL-XwAZtLonHpKzT1CYEk-wJ2ZD-5Pdn7sHBgAutItXkEw3HUs_IuUjX6SrJR0ENEkOUiIJvUHeo5T6QEpr544LhyiwangaBqvPdik0LqRzaGCzU4BuIGmTfU5BEFuksbR9I0SNtKQP3uCd7hT1klTuSxlzu5V-AtMxwRJwSfEnvgEypmj6T1HIwsfIwgiT6cJ0B4ZBjcb9QZ8ki8Zfp3uXvC9MTXpd2iKsVp75kFyf6vR95M-bHYIFBcOQxpQ7eT4FhF6yPTXx7UaVcBiJ6BwW-G2LSpA5pYBjNp_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
❌
🇦🇪
با افزایش تحریم‌های آمریکا تجار و بازرگانان می‌گویند امارات از بارگیری لنج‌های ایرانی خودداری می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/71090" target="_blank">📅 14:31 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71089">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/28ac9cc9fe.mp4?token=SMU-T-CK68QGSVxlMfFRLwq8c_NG6CtJLGP1u7tYm3dXNyrmMZqJFEchHt3B7bvpoQPZiui0A2oc2dPO0dgLaf1Qp2HEoEU_6nNP8iebVEmdQAy7KnX5Jb9i6XSqjOK2lYF8YBEWn0sT1dGL9eBYd0wcCO0AEvJmfxnOkUoJCqWF9IELp9IaD-wQIoBJ6FiPeh0qnsbVSweM3GrL5OWTtdAkCsZ8zZlzPvA8XBX_io5NSI51H_rBSfFqrzt2Ccf7ok_jjoe2-F6kmKeiL3LCVBvzn-1s1hCf8NUtwS6jj0NaWG45acfUKNFtG1T1C-nrj75ZDOVNbo2WQzbUv84Eqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/28ac9cc9fe.mp4?token=SMU-T-CK68QGSVxlMfFRLwq8c_NG6CtJLGP1u7tYm3dXNyrmMZqJFEchHt3B7bvpoQPZiui0A2oc2dPO0dgLaf1Qp2HEoEU_6nNP8iebVEmdQAy7KnX5Jb9i6XSqjOK2lYF8YBEWn0sT1dGL9eBYd0wcCO0AEvJmfxnOkUoJCqWF9IELp9IaD-wQIoBJ6FiPeh0qnsbVSweM3GrL5OWTtdAkCsZ8zZlzPvA8XBX_io5NSI51H_rBSfFqrzt2Ccf7ok_jjoe2-F6kmKeiL3LCVBvzn-1s1hCf8NUtwS6jj0NaWG45acfUKNFtG1T1C-nrj75ZDOVNbo2WQzbUv84Eqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇵🇱
🚂
برخورد قطار با یک کامیون در گذرگاه راه‌آهن در گدانسک لهستان.
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/71089" target="_blank">📅 13:51 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71088">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b60a6b68b8.mp4?token=l6_2cS8vfGLsrgZW5_1DZptxVthvPhOU0yYimgdgoLn-KoDnF27x-QwdRqx1vh1dAOmn4jytwzoZGyWtobzRIumbWz3tDGKJK0jnh--zTSbxeucRWlQOF0m5YL_Gokjs35tZqHfj0STUSn9Qi2e79rdDQaJm1QZiyz934wd8kZ6HZNp_3frfk5Dk2KKTCiL27VSR1SrvWl52E_tX0876dbv9jKammW6uuR7UH6TUfyCtaXZQ3ia_GTv-sZHNrVXe3Wgpsj29J_FUW1JSw00dSAgB1HT4pAno2ON8u7ejKxmZlRgk7wfo-rUlm4pRLsnUbDc-n4hjaQnuAsVI985hSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b60a6b68b8.mp4?token=l6_2cS8vfGLsrgZW5_1DZptxVthvPhOU0yYimgdgoLn-KoDnF27x-QwdRqx1vh1dAOmn4jytwzoZGyWtobzRIumbWz3tDGKJK0jnh--zTSbxeucRWlQOF0m5YL_Gokjs35tZqHfj0STUSn9Qi2e79rdDQaJm1QZiyz934wd8kZ6HZNp_3frfk5Dk2KKTCiL27VSR1SrvWl52E_tX0876dbv9jKammW6uuR7UH6TUfyCtaXZQ3ia_GTv-sZHNrVXe3Wgpsj29J_FUW1JSw00dSAgB1HT4pAno2ON8u7ejKxmZlRgk7wfo-rUlm4pRLsnUbDc-n4hjaQnuAsVI985hSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طرف با رفیقش رفته دور دور الهیه و به یه دختره شماره دادن،
و حالا اولین پیامی که دختره براشون فرستاده
😟
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/71088" target="_blank">📅 13:49 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71087">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71087" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/71087" target="_blank">📅 13:49 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71086">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WW381J321KnJBtoaXH0XNVk9jBVkyN8E9Y88zu7GujXZj-G5DpxDrAAw3AakDqgXGGV6HW2QqEBjJUMmChXJDCEpqSLrYVcyRdV46oS3SMgPrf68UPt9xI7-S5nOf4pe-g_oF90AturcB94VhIBZGzqCvv_StSYEUsAH6hrTsuHB4CVZruDdcVCL8P6STSO8QOPr92w_gbxRni8SsPR9OUhgVdVfuS4bbB5JtY1c20pfF77z60mvhAwn14piXr0IoLmaomP6IScOa2ETW-cfxmg0NE7x9uVcoMYc26Z07r6xO-BtV4_OK4uOiVclKNBlgmwX6dp1wpVM0o6-mMDSEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
بازی جذاب رئال بتیس
🆚
رئال مادرید را در سایت بین المللی
TrexBet
پیش بینی کنید
📊
نگاهی به آمار دو تیم در ۵ بازی اخیر
رئال بتیس: ۲ برد، ۱ تساوی، ۲ شکست در ۵ بازی
رئال مادرید: ۵ برد در ۵ بازی اخیر
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/71086" target="_blank">📅 13:49 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71085">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4843999275.mp4?token=d3OXAQF3r1Me2TdgnB8pnavd7-2iFHMGI5qshNxnYwhVzlU-iaspSG9NQz2x59x_OxKAFKgcMcTm7rhBsd92_S99dKLs6HAa9FNDPeuKe6N46nS3wQul6c3_BXzp7mIPgXZfkr2EOBofOZ3YBCOwcnzZxWU9HM8zM73biD6xAkchmSRByDxxxmbFf7a-1VwWEr2zw96jyFCF55-RKhT97f7m4SOR5oIeQTalc-Up5ongswh-Bd0oeiLExQ9t1nnBw8hEb3l_hUNvXGpMHDUqvaopbZQFzMNn_C6t54agPHprBehn7S1sBHP3qbI6uEEUSunVrMy_xw1ktASJA9G_XQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4843999275.mp4?token=d3OXAQF3r1Me2TdgnB8pnavd7-2iFHMGI5qshNxnYwhVzlU-iaspSG9NQz2x59x_OxKAFKgcMcTm7rhBsd92_S99dKLs6HAa9FNDPeuKe6N46nS3wQul6c3_BXzp7mIPgXZfkr2EOBofOZ3YBCOwcnzZxWU9HM8zM73biD6xAkchmSRByDxxxmbFf7a-1VwWEr2zw96jyFCF55-RKhT97f7m4SOR5oIeQTalc-Up5ongswh-Bd0oeiLExQ9t1nnBw8hEb3l_hUNvXGpMHDUqvaopbZQFzMNn_C6t54agPHprBehn7S1sBHP3qbI6uEEUSunVrMy_xw1ktASJA9G_XQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار:
پرزیدنت ترامپ در رسانه‌های اجتماعی پرسید: «مردم ایران کی قیام می‌کنند و می‌جنگند؟» آیا دولت در حال بررسی مسلح کردن یا ارائه، سایر حمایت‌های مستقیم از مخالفان ایرانی است؟
🇺🇸
ونس:
ها ها ها... مگر پیتر دوسی امروز صبح این سوال را در فاکس نیوز نپرسید؟
سوال خیلی خوبی است.
و چیزی که رئیس جمهور گفت(درجواب به این سوال) دقیقاً همان چیزی است که من می‌خواهم بگویم.
قرار نیست درمورد این سوال صحبت کنم!
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/71085" target="_blank">📅 13:10 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71084">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gKv9zqEsyNzIfNORbEIEoMspkj4o4My1Au7RVfnBg9RF1N7_O8JIPHOarG92lfefDzb_Rx20_T0H_tj5X-VtbUHXeGi5BKIjwwLZw2MMUl50ZzX4OMbhS8VRusgw1UTdUCEr89KJYh_9RCLKwb4KGAyHZ7re0CPuo3i-6e7ntRbN4n5lbk1dmDjvLpc81iWEXJM6PmTaty0fJovosMKXV7cFOZy72pFt_Fz2ADrKjWMceJqzwaA1NDzyQh28U6G2DA-icSzHO90oSZym1vnrXw6lab3JLfHSoukJxFutElGbVrAi2M0CzKHlZXMPHIrNLJM2A7QeJmmME6VhzAb_fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عرزشی با این پست به شدت میسوزه
😃
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/71084" target="_blank">📅 12:12 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71083">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0edd50344.mp4?token=sSywWnFI1YhjEhZh9tdl0Ht-CMuyRQcvyHZFAC7VZvU5pwDDxSg5m6b_caS233oQa-l48CoNWJJSuO23CuXe6g7H7Yh_OM1sBnbZDHd8ZlopXyl0RjuHJ1HZ3FTriDuatTWaqWdsrBvie1oIi2sadhlnPJ1yh9DmawcWSqe1G9vPVIIY2UdOS3mmzEETtQo1mnbIPzs0ZTFiVrrXVC-Wbw4iVFbrHYPnNNXp5C9hUtIfyrdUuGTuJyoXC0h0hL0sWM7ZB703Vuj-R5v3SXtDKL2gGEggbAh9rVtVikBtWuLjEdKJiUQezvr5WywaSO-3CGgmKNE9bz0MzgFCM7PkAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0edd50344.mp4?token=sSywWnFI1YhjEhZh9tdl0Ht-CMuyRQcvyHZFAC7VZvU5pwDDxSg5m6b_caS233oQa-l48CoNWJJSuO23CuXe6g7H7Yh_OM1sBnbZDHd8ZlopXyl0RjuHJ1HZ3FTriDuatTWaqWdsrBvie1oIi2sadhlnPJ1yh9DmawcWSqe1G9vPVIIY2UdOS3mmzEETtQo1mnbIPzs0ZTFiVrrXVC-Wbw4iVFbrHYPnNNXp5C9hUtIfyrdUuGTuJyoXC0h0hL0sWM7ZB703Vuj-R5v3SXtDKL2gGEggbAh9rVtVikBtWuLjEdKJiUQezvr5WywaSO-3CGgmKNE9bz0MzgFCM7PkAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
ویدیو وایرال شده از طرفدار حکومت
🎙
خبرنگار:
از قیمت دلار خبر داری ؟
🇮🇷
طرفدار حکومت:
بله شده 200 و خورده ای
🎙
خبرنگار:
با این قیمت پس چرا اومدی اجتماعات ؟
🇮🇷
طرفدار حکومت:
دیگه باید قدرت تفکیک داشته باشید تو ذهنتون و قیمت دلار یه چیزه و بیرون اومدن یه چیز
اصلا اگه امنیت ما نباشه شما میتونید راجب قیمت دلار فکر بکنید؟ نه نمیتونید!
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/71083" target="_blank">📅 12:01 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71082">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">⏺
ویدیو وایرال شده از اعتراض یه زن کارتون خواب:
به عنوان یک کارتون خواب که 20 ساله دارم این زندگی تجربه میکنم!
شما مسئولین که مردان خدا هستید شما دیگه چرا؟
تو دانشگاه رشته حقوق خوندم
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/71082" target="_blank">📅 11:34 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71081">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d18ffbfe89.mp4?token=ELtcVK7shPa5wLSnzuS7efpJLDz6TQmWLWRUy0O3t-jfsjNreb2q0indKLhbqPkQXCYn9jOSRftaGMfNd6ii7ZPvuWy7NZRa20f6dcyFdfFth0pyfDvyR7md_q1KUZfzn5NH6HINdIirjp1SbqtQqJ1YMH6TfO-xESDfRRSclMRo_JBwJB3uIfW-i6Gc34wOb5WWGxy0zbnyVfouERsJXL6_Tcg7odJnMPAhgfc91XCXDLg5XrAHufyyRXLMbKpjUTU95p02QBOW7pG80MUAZXTfqPRTrXQaugVKwUafS-6tgIKvJaOP-aQWWQm0U8y1RcApdCxQjhtQ1t8A3oSd4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d18ffbfe89.mp4?token=ELtcVK7shPa5wLSnzuS7efpJLDz6TQmWLWRUy0O3t-jfsjNreb2q0indKLhbqPkQXCYn9jOSRftaGMfNd6ii7ZPvuWy7NZRa20f6dcyFdfFth0pyfDvyR7md_q1KUZfzn5NH6HINdIirjp1SbqtQqJ1YMH6TfO-xESDfRRSclMRo_JBwJB3uIfW-i6Gc34wOb5WWGxy0zbnyVfouERsJXL6_Tcg7odJnMPAhgfc91XCXDLg5XrAHufyyRXLMbKpjUTU95p02QBOW7pG80MUAZXTfqPRTrXQaugVKwUafS-6tgIKvJaOP-aQWWQm0U8y1RcApdCxQjhtQ1t8A3oSd4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه پسره دوست دخترشو برده تو کوچه پس کوچه ها بهش رانندگی یاد بده
آخرش هردو غافلگیر شدن
😂
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/71081" target="_blank">📅 11:01 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71078">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8bc34fe3de.mp4?token=tJC-dfVQgv2r13I9126mJMecaSCyma1TaJiVItDDhcqb-gCTWB2tknhah3WDYeCvlFOWLQLZ6CVQ0_7KLKaeK8rK2xIWLjwA2-tFMFJnElYmk0LEkboBPthX7cWXELsv0wll1mX-dJi1O_VN9ZAhWIYq26uF-0R4dbiPw0lR21TkVc7OfvV7kWKiUZ_DKFuNOQU1hMyIH8BvQb0rc9QNezaZFsUBTNBjq5xFc0Thq6LBpq7BvLK7iPMUlcTd4trOG3-dR22aS7pCgskESYorziBkxJffsPJGiHNRumY7bJ8ipPPy4tc5GD3DZwrujEIjeh8MzSQJBZvM8KbIGx9v1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8bc34fe3de.mp4?token=tJC-dfVQgv2r13I9126mJMecaSCyma1TaJiVItDDhcqb-gCTWB2tknhah3WDYeCvlFOWLQLZ6CVQ0_7KLKaeK8rK2xIWLjwA2-tFMFJnElYmk0LEkboBPthX7cWXELsv0wll1mX-dJi1O_VN9ZAhWIYq26uF-0R4dbiPw0lR21TkVc7OfvV7kWKiUZ_DKFuNOQU1hMyIH8BvQb0rc9QNezaZFsUBTNBjq5xFc0Thq6LBpq7BvLK7iPMUlcTd4trOG3-dR22aS7pCgskESYorziBkxJffsPJGiHNRumY7bJ8ipPPy4tc5GD3DZwrujEIjeh8MzSQJBZvM8KbIGx9v1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
توی دزفول چند تا دزد میرن توی یه خونه مجهز به وسایل ضد سرقت و 3 کیلو طلایی که توی اون خونه بوده و قاحب‌خونه قصد داشته باهاش طلا فروشی بزنه رو میدزدن!
صاحب خونه شب قبلش توی اینستاگرام گفته بوده که میخواد طلا فروشی راه بندازه که این حرفا رسیده به گوش دزدا ؛
فردای همون روزی که این حرف رو زده وقتی صاحب خونه خانومش که باردار بوده رو وقتی میبره بیرون یه هوایی بخوره دزدا میریزن تو خونه و طلا ها رو میبرن.
حالا صاحب خونه گفته که هرکسی هر سرنخی از این دزدا داشته باشه و بهم بده ، 10 میلیارد تومن بهش پاداش میدم.
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/71078" target="_blank">📅 10:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71077">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0def551e36.mp4?token=kqmloNDiw7IK-Jbx4cOfaQh6bfjH5z1Sad9AJOCpg9qstmHuvuKj9YRE6uJaV3K8pPbj0WIY3zVFO-EWipztDfYI49zY6gK90T3G0fmu2DaEIoJdi0yIdfWzah8vP6pWnyuo7zfJG4rJXwy4jNk-7jXVAQO39KaxUqts4O0vKYDeBMBxZkm2Lz7PS2FZvjpRIwvJBsiNs_FhIcMobK3eZL8LfgwtThO4QFcuAO5pxfexKdiNfxNBGzpeMrxFgjawmW4RzDPOL3Co78cVrWAovRadwjWfsf2AOLv3exRbIw0o_N9xpS1cyxp09V5AOFZF9vgAzcKdv-bIXCQow6DbDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0def551e36.mp4?token=kqmloNDiw7IK-Jbx4cOfaQh6bfjH5z1Sad9AJOCpg9qstmHuvuKj9YRE6uJaV3K8pPbj0WIY3zVFO-EWipztDfYI49zY6gK90T3G0fmu2DaEIoJdi0yIdfWzah8vP6pWnyuo7zfJG4rJXwy4jNk-7jXVAQO39KaxUqts4O0vKYDeBMBxZkm2Lz7PS2FZvjpRIwvJBsiNs_FhIcMobK3eZL8LfgwtThO4QFcuAO5pxfexKdiNfxNBGzpeMrxFgjawmW4RzDPOL3Co78cVrWAovRadwjWfsf2AOLv3exRbIw0o_N9xpS1cyxp09V5AOFZF9vgAzcKdv-bIXCQow6DbDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
امروز یه دختره داشت تو قزوين واسه خودش قدم میزد؛
که یهو یه پیرمرده خواست مزاحمش بشه ولی بعد که فهمید طرف پسر نیست، عذرخواهی کرد و رفت
😳
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/71077" target="_blank">📅 10:02 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71076">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4ba13b0e17.mp4?token=UekEd9BxvjeorY8jx0d-DRsSK-_3jSbsyWaKPcOjPflMfREgS9CgnD0rc9iuosLGuUwJZ_-B_dqiqGMfbMD0PgEgr3EUPngJ2byRvyRq0Fb7A7UPF7DGpNN7_YgtzvVtx0Su_xI3cglYMu79b3pTqQgY407LVJLG7gPwEK5WdPUjlLdzKehPiE1SrgHNddtRRhFz7bYN7-YudvRUmJa9rghD1l8CBiLiTbChrhe8_072AQZMIGUt-Ix6QuX-Lu5eVACHBCvh8Rkdie4seXWlov8P2kACJw_4EDdxaxJKbI9hvAnqskCSGLc_guYizKEYAGMyzX2WJSf87P1eS5i56Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4ba13b0e17.mp4?token=UekEd9BxvjeorY8jx0d-DRsSK-_3jSbsyWaKPcOjPflMfREgS9CgnD0rc9iuosLGuUwJZ_-B_dqiqGMfbMD0PgEgr3EUPngJ2byRvyRq0Fb7A7UPF7DGpNN7_YgtzvVtx0Su_xI3cglYMu79b3pTqQgY407LVJLG7gPwEK5WdPUjlLdzKehPiE1SrgHNddtRRhFz7bYN7-YudvRUmJa9rghD1l8CBiLiTbChrhe8_072AQZMIGUt-Ix6QuX-Lu5eVACHBCvh8Rkdie4seXWlov8P2kACJw_4EDdxaxJKbI9hvAnqskCSGLc_guYizKEYAGMyzX2WJSf87P1eS5i56Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
لحظه دستگیری یه قاتل فراری در ایرانه
:
قاتل با چاقو مامورا رو میزنه و داشت فرار میکرد که یکی از مامورا عین راموس تکل زد و طرف افتاد.
بعدش یکی دیگه از مامورا ویلچر برداشت و میکوبید تو سر و بدن قاتل تا بیفته زمین، هر لحظه این فیلم عجیب‌تر میشه.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/71076" target="_blank">📅 09:32 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71075">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r253K_z1Rh4Ru6pnoBVKvV6-bXdg2DNpeI036EiJ0342aXsl11K7_t5dHup2yBx3rHrZ4XQvpFV0PV0S_q6EwIhi-O6fKtNrcBRWXXJ7Q3ZDH46gI_yaR8g8PqIIJD58md-Djp72IT5Pk3JHRq8HVNuxIUuxmk91zvGitoqQ1SgFx8DrhH7HhotrxUqHI_RgyGG0NwiJ3khjEgI4VArVKHK9xSM7dHSYEcPsCXuSrHtbQxtIGbEfpo7o-XILIv2pYh_O23r3GwY3jwRTyTjrgwwGTvqVvDmSWawPqtmA_Lm7DkjKO_TUPwYgb84_VkYrQ28PZNFsrBFPkG4cBenwBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
🇺🇸
⭕️
#فوری
؛اسکات بسنت وزیر خزانه‌داری آمریکا:
اتحادیه اروپا رسماً به «عملیات طرد اقتصادی» (Operation Economic Outcast) پیوسته است و ما از موضع قاطع و زودهنگام آن‌ها قدردانی می‌کنیم.
ایالات متحده در کنار متحدان خود قاطعانه ایستاده است تا اطمینان حاصل کند که رژیم جنایتکار ایران نمی‌تواند از سیستم مالی جهانی برای تأمین مالی جاه‌طلبی‌های هسته‌ای، برنامه‌های تسلیحاتی و نیروهای نیابتی تروریستی خود بهره‌برداری کند.
جهان پیام روشنی به رژیم ایران می‌فرستد: ما تا زمانی که آخرین شریان حیاتی مالی باقی‌مانده قطع نشود، از تلاش دست نخواهیم کشید.
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/71075" target="_blank">📅 09:03 · 13 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
