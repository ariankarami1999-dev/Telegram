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
<img src="https://cdn5.telesco.pe/file/XKVbbA7f8rSpsPgQjGcwdPb8W-qgAreGmeTv04qAKJyl1W3N1WLiI5R45GlbfdS5HoP7G9qODS_w12ShjYIzmWAq2IwU10A4sGLS1qOrI2ipjD6osmGifaVtNcM8KBuLEnV7GOOpWG_df8uKiOjeDEMP-rkQMW87KcziMDFUstJGo5dUyhCB-qW-8C9HRcQNlu37pWgK3wVlEDvmorfWJLe9VC1BgZ7hVQaYvenpdfItTNMZwmCTdhyKsiwsJZDqhX-QbB1g0j4yH6RF6PTnheO-TSCWis3NslRJn3eSW9x3YSNq7qVbiNxcUp65Um9MMntnJEs37G9BfGipic909g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 436K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-08 12:13:41</div>
<hr>

<div class="tg-post" id="msg-105076">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b3d5a56b7.mp4?token=WZ0eL2R3glKl8a2mkF6iGUOz38-9whI5sclqQLHoPJevDEhKpDWTVqgiC0YNO8_Pnw0zeD0BqgHWHAbIFF_ebpdDxNr6TudH6pDW22rJD8u0TwuUbSyl36ImfHN6Gq7azcxLE7KWSAwc_0q47cREopumA0x4b1wCYI-yjLtO9XJsVxy4azp1kJb9hXOR-i1TeBZxu4EAmbKtokdLAJ-inSCb5o0Efu8sjar8wmjtqE7a_Wdu8xIxUXzBfpOIk1alUhxPH14k-L_qpQ5jF0VdKJ8goxsyT2CznkzJLKElrtSOjwd2jnvzNDAlYR99iyYXqH1TtYgtCTQp4LNJlSlVow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b3d5a56b7.mp4?token=WZ0eL2R3glKl8a2mkF6iGUOz38-9whI5sclqQLHoPJevDEhKpDWTVqgiC0YNO8_Pnw0zeD0BqgHWHAbIFF_ebpdDxNr6TudH6pDW22rJD8u0TwuUbSyl36ImfHN6Gq7azcxLE7KWSAwc_0q47cREopumA0x4b1wCYI-yjLtO9XJsVxy4azp1kJb9hXOR-i1TeBZxu4EAmbKtokdLAJ-inSCb5o0Efu8sjar8wmjtqE7a_Wdu8xIxUXzBfpOIk1alUhxPH14k-L_qpQ5jF0VdKJ8goxsyT2CznkzJLKElrtSOjwd2jnvzNDAlYR99iyYXqH1TtYgtCTQp4LNJlSlVow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
پروژه تبلیغاتی فوق‌کسشر و خطرناک روز گذشته در آفریقای جنوبی که نزدیک بود دوتا هواپیما به سقف ورزشگاهی برخورد کنن!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 616 · <a href="https://t.me/Futball180TV/105076" target="_blank">📅 12:13 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105075">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2d58cb930.mp4?token=qx5PKs4paR3Q9oGAnI1C_Bw0RiWwqWPvAdeym7vP00NWAgclOdzLjEerg8GB5_Cm2vFRJxbkUoMatHzbsFClTzvWayjxgfXDt7wuewfNkUW2Ko0UDFhC05mFdMo3ZKfB6C1dooSvj6i-CoXrYSifBRNVG-IDUKbtLdMbTujN60887CwUV0w7pPzQfYqPLa8HKJuHeOF-P8GRNjYTzNKSxuzR6YSN0Y--UXsN4Fx_-XyQEKXucHanpv3HCRvWo-L1OgVg8fobIV5ilCWM2AGYuCED-YnO_Sl3iGw1bqKIAhxu97WRVa_5Z9qBXGul5zNRskpiY3RWIw-sxWDM-dCSjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2d58cb930.mp4?token=qx5PKs4paR3Q9oGAnI1C_Bw0RiWwqWPvAdeym7vP00NWAgclOdzLjEerg8GB5_Cm2vFRJxbkUoMatHzbsFClTzvWayjxgfXDt7wuewfNkUW2Ko0UDFhC05mFdMo3ZKfB6C1dooSvj6i-CoXrYSifBRNVG-IDUKbtLdMbTujN60887CwUV0w7pPzQfYqPLa8HKJuHeOF-P8GRNjYTzNKSxuzR6YSN0Y--UXsN4Fx_-XyQEKXucHanpv3HCRvWo-L1OgVg8fobIV5ilCWM2AGYuCED-YnO_Sl3iGw1bqKIAhxu97WRVa_5Z9qBXGul5zNRskpiY3RWIw-sxWDM-dCSjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🔴
یه خانم مُسِن پرسپولیسی : من پرسپولیسی ام الان 55 سالمه و از شش سالگی فوتبال نگاه کردم یعنی کم کمش 49 ساله که پرسپولیسی‌ام
‼️
🇮🇷
دختر کناریش که استقلالیه: خاله تا حالا قهرمانی آسیا هم دیدی؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.73K · <a href="https://t.me/Futball180TV/105075" target="_blank">📅 11:50 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105074">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DrWlOcT4xm52_eZfFsWIwz99h3eh3Kmkcatb1r1Z15qKP8qQsiR1FbOBLOkmAgoFdN-jT7bY-SH_IPv4-ZfHQyY2z-KbWr5yoLsdKrXzXf6a_-TV5KlPl4226XsWEkDRyfgxnTyMXaCATfwPr2E81LjjbtCur4S4Iyse6L3cfMC_OPPKsw27KP3jsA8TwAlBPTwXsGwRZKjquqkVUGWkAXV2wxIj2QNpzyaUavIdXN-krFEW4S-19R2Ghd4oG3U5uLo_31u-WzNUvjcX3rv1YI0vKafbg0z69k0ZfR6Sgm3Tn4_mbkN9Ic9dnY77GXMqzpNsaDqh8uYPp-gtldXYlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇮🇷
🇮🇷
سنگ‌بازی دیشب هوادارای استقلال و فولاد حین خروج از ورزشگاه
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.01K · <a href="https://t.me/Futball180TV/105074" target="_blank">📅 11:48 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105073">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/105073" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 3.65K · <a href="https://t.me/Futball180TV/105073" target="_blank">📅 11:48 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105072">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qir6XKQ0gAYGibzwhvBKyqA4-a4sX36Sd-mAbOMzCRWvXG9tHzZIXjK7O46033Ja1t01-InTAkYvY2GbKzKpJOlDljCJb1qHga6qNoy5zCbyn3wEAnIAZgZwDcov4mNj5Ag5GO17i6tZO3Da8io8hgQaDevmh1Z-Xcp9fYMVpQ3NFHAg_xMguTvG-pvV-v0OZbmBYIH3w6Q0MCQPNADNjB5-gbjC8i2UwinSWHJURcvWNF_VAzazs7v2-FozZZUMoRRLyuNvlBKLf-nm60dFoimTPEhbtpqTC2Zcxpzj7BuTk7bpFhtGFtBweivgOBeKKsHHFGaUdNHeueRK2YgYcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تیرکس‌ بت می‌بردت وسط هیجان US Open!
🎾
🔥
🦖
رقابت‌های نفس‌گیر، امتیازهای سرنوشت‌ساز و هیجانی که تا آخرین ضربه ادامه داره!
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
TREXBET — PLAY. PREDICT. WIN
.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 3.71K · <a href="https://t.me/Futball180TV/105072" target="_blank">📅 11:48 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105071">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mv_cVkbaF4igK3JFlTUqw26Dw_p5ruJJ6IKel8Qe37eFflFelPrnPTj1W72SOqISLSbvqc3FAWeyepItxZGnGEDgQqkT86juyMya2NN3coijnTjNj7hCkYp93hs8Cv4s0ANsEiqSQckRBeyRLu93JT3zL8dXrSe9FmCJJbGsdQOWN6RjzBpGShZrmlNspKby1AQrXF-jLIxHMkvBWNaRHNB8VngtNSIur5fP0IJdmoVAEDH8oDX4_fYLP1iX7_PuRgf4e5O5OvgfafFqA9Vjtyy4v2MXfwH9s9uQIf30bik_7jlB5nIsjaT4T4VUJty7G7qgzYLYlii2kBf4lKJtPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
✅
#رسمییییی
؛ املیانو مارتینز سنگربان تیم‌ملی آرژانتین با قراردادی دوساله به چلسی پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/Futball180TV/105071" target="_blank">📅 11:38 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105070">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hHl0twv_CnpwQJFhNBMLvulvoZYIcatcqZHDQvGeYx3n8hnxwppbCrc4ZV85ypOwvaze6utAODVGt1QF9gUQesm43KK-E86rPJLeIMPAYv6V9ONBpU9WbuDrOhWqrmFvofdU_G3YQddmquqovyHRm4kayPtika8c-hjuu0ZLVTNVg4KtRWriZFPSyhKajMM_QdTZl5LjxqGl6Yq7BwAVCem9DlED4iyqaP8J9SWUwSAEdNJUFvd1YwGr_RezZbQSoFQZUtwMFWAhGGNAWR43qv6vP06LBvu81V9OapVA87RjyyBfqkkFs9VsJPKJHK3JOEW7JTXPwaBKjTH63EvAMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🥶
👀
🇪🇸
🇦🇿
بارسلونا در آخرین بازی لیگ‌قهرمانان خودش باید مسافت بیش از ۴ هزار کیلومتری برای سفر به آذربایجان طی کنه. چیزی حدود ۵ ساعت پرواز!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/Futball180TV/105070" target="_blank">📅 11:35 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105069">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad71709b9e.mp4?token=lzLHv9XhHOm8p6QIENDB2BEoEpcuH9ALateEo6KLb9_WxVEeEHMR5BHzRci795WL_MklHEQQkfnMzHZlbcs873NSViQpiziRRMeBhAj34Lsy_qUNWwqjfWL0cwqhou2KNRYYgMMdzVvFpkUgIuGM_YycoB1Evbkzx2_FKM6c53aR2HMTlqBmEi97DreTy_31MvBY4PUmm1LHVWqG6iRYGpg2lIT8MI_qnyIz22M9As0hfs4IFLk5Ie21jjpyr2pUNx0N_Q9tg29e8kg-NxpLCFxhwBl4uBKi-3zkJQwgwKDGqoxlM3XEozwQJ3QgJM0NFJlFEkTE9GWkRvmf41rIbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad71709b9e.mp4?token=lzLHv9XhHOm8p6QIENDB2BEoEpcuH9ALateEo6KLb9_WxVEeEHMR5BHzRci795WL_MklHEQQkfnMzHZlbcs873NSViQpiziRRMeBhAj34Lsy_qUNWwqjfWL0cwqhou2KNRYYgMMdzVvFpkUgIuGM_YycoB1Evbkzx2_FKM6c53aR2HMTlqBmEi97DreTy_31MvBY4PUmm1LHVWqG6iRYGpg2lIT8MI_qnyIz22M9As0hfs4IFLk5Ie21jjpyr2pUNx0N_Q9tg29e8kg-NxpLCFxhwBl4uBKi-3zkJQwgwKDGqoxlM3XEozwQJ3QgJM0NFJlFEkTE9GWkRvmf41rIbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😳
🇮🇷
دیشب خدا دوستان‌فانتزی‌باز لیگ‌برتر رو خیلی دوست داشت که کیری بازی این جیمی‌جامپ عزیز باعث گل‌خوردن پیام‌نیازمند نشد
😐
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.83K · <a href="https://t.me/Futball180TV/105069" target="_blank">📅 11:07 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105068">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aeeb0876ab.mp4?token=ickY0OVzNp3UbMA41k4H60pk9nht3ZLvUYPUIxPlA7Y9TJO-HYuCmxYtBuVpzVTHJE0kVsUDBVzXbmD0L7BRo-BXfAuGT2z5KJKRSkw6H_t27yeQSrMHtSHV5vO2mSgTtQCPesPEt74hTc2zMnNu8lfVpWK-97Y3KzDFi3DoXrBj5FP-idCvFOBBAXoM4WCTJCFji8KcDGWiu_6ZZOxpN2ZwYWSvMo4c-5RmnySCql20Jx608bc27YVam2JYZZAKtBCBATcYavJSFkbvf0yDFnsl31gVPMIIBbdJflF6FUylBgzuKZUCUYd0Y-bSrhCayR3YQfec8jkW1C-SfUGX1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aeeb0876ab.mp4?token=ickY0OVzNp3UbMA41k4H60pk9nht3ZLvUYPUIxPlA7Y9TJO-HYuCmxYtBuVpzVTHJE0kVsUDBVzXbmD0L7BRo-BXfAuGT2z5KJKRSkw6H_t27yeQSrMHtSHV5vO2mSgTtQCPesPEt74hTc2zMnNu8lfVpWK-97Y3KzDFi3DoXrBj5FP-idCvFOBBAXoM4WCTJCFji8KcDGWiu_6ZZOxpN2ZwYWSvMo4c-5RmnySCql20Jx608bc27YVam2JYZZAKtBCBATcYavJSFkbvf0yDFnsl31gVPMIIBbdJflF6FUylBgzuKZUCUYd0Y-bSrhCayR3YQfec8jkW1C-SfUGX1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
👀
این یوتیوبر استرالیایی میره سراغ مردم عادی و بهشون پیشنهاد میده در ازای ۲۰۰ دلار براش غذا بپزن. دیروز اتفاقی میره سراغ یک خانم ایرانی که قبول می‌کنه و ادامه ماجرا ...
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.01K · <a href="https://t.me/Futball180TV/105068" target="_blank">📅 11:05 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105067">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a3fe4297a.mp4?token=H_REJe5bFb1o3c53WcGlF_zhPM8qZiw3b9pT8d2l4VMQ7ZQJparxlaOEsNIyHXnaS44fJioaTqZELn0qiPY3oGv3M3WHzZDA0z8EmfZ3RNCHs09frPrVt5VeV2pL2Mmoezl5FdknWijWyY_AjMm3IrxmkbZ7TsWJ-LTNZALqTQzuVpIMbtOHvps_d1weTxfe6s8OKnK25eIjuOLRvidw-rY_J34xwMlDFrPFptEb8lWX_BiVdOiQsFpSuV2S9OTxzPrHTgaz4kjasZgRepmmCQXo66EUKIm65ImY43peotrSQJ2gNmOBCcaDjmbMFRnrVflLO1UcFERIRZ7YOru5Mg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a3fe4297a.mp4?token=H_REJe5bFb1o3c53WcGlF_zhPM8qZiw3b9pT8d2l4VMQ7ZQJparxlaOEsNIyHXnaS44fJioaTqZELn0qiPY3oGv3M3WHzZDA0z8EmfZ3RNCHs09frPrVt5VeV2pL2Mmoezl5FdknWijWyY_AjMm3IrxmkbZ7TsWJ-LTNZALqTQzuVpIMbtOHvps_d1weTxfe6s8OKnK25eIjuOLRvidw-rY_J34xwMlDFrPFptEb8lWX_BiVdOiQsFpSuV2S9OTxzPrHTgaz4kjasZgRepmmCQXo66EUKIm65ImY43peotrSQJ2gNmOBCcaDjmbMFRnrVflLO1UcFERIRZ7YOru5Mg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇪🇸
پست سمی تیم‌ذلیل آلاوس که بعد سه هفته و با یه بازی بیشتر صدرنشین لالیگا شده
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.27K · <a href="https://t.me/Futball180TV/105067" target="_blank">📅 10:40 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105066">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kr3ofq9U3lQdq01hq0g7i_qk9Sr78uwZV2xIS80YqVbzf4-_mcDJs2aFhekfWY5EYMD1WnEVzIRl2MBaddfCsh6K41npU_jpAFzKQa7Yf7tbmztmZAXxlmeqXdnswLEy6DCgKXnmzKIL0RVwTihRVtPBcEpwrqK_qvkqK_ZFTsS0uGhX81A37jhK5lroBS8zblxiWonxVWmXRUKNBy-9X1XAqvWngFPKY0AtcvbzEXte6SgG5mKXFKT4g05-M9UuuGKuDH0tve1V9yFpBRZDJ3Pfxw2jh24w3irfW5KNKXGI7s35sppe1OlCfN0-VK5HY0EQ6jTodrFJ_D01Guqp_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
💥
🇮🇷
هوادار فجرسپاسی در بازی دیشب
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.77K · <a href="https://t.me/Futball180TV/105066" target="_blank">📅 10:19 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105065">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c6851cddf.mp4?token=tIOlwX5ZQ19XoGPTkcNpZ2U7tXzjSKrYq_CW8d7Rbo8tGgzSZ_hvMafQqoQyN41fi11-ySKnEb2IeaDGCfY2Igq0Yx2rJvDzRncdoeNOv6UzXVulth8BagGAUe4uvvmNUCaOrhMeR9Wiab-Shcq7giqfk7nkePAaImvedoC4wI-D7VWIXB1w5Kw-NFo-AMTYQ61uTroz0kKHIhwNb4nXyesSwP73Se-EkE5i1l4SRm8ElSPJjeYCsTMAsRuqiBQktvLcThmNMTLuNQpKqSHl0LsSQ6ZKgwnMY8-BszrO9Q3yltB9z3VvbZNX7xkjcFxGmTw2ocXqkDXLyP3GJAfxPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c6851cddf.mp4?token=tIOlwX5ZQ19XoGPTkcNpZ2U7tXzjSKrYq_CW8d7Rbo8tGgzSZ_hvMafQqoQyN41fi11-ySKnEb2IeaDGCfY2Igq0Yx2rJvDzRncdoeNOv6UzXVulth8BagGAUe4uvvmNUCaOrhMeR9Wiab-Shcq7giqfk7nkePAaImvedoC4wI-D7VWIXB1w5Kw-NFo-AMTYQ61uTroz0kKHIhwNb4nXyesSwP73Se-EkE5i1l4SRm8ElSPJjeYCsTMAsRuqiBQktvLcThmNMTLuNQpKqSHl0LsSQ6ZKgwnMY8-BszrO9Q3yltB9z3VvbZNX7xkjcFxGmTw2ocXqkDXLyP3GJAfxPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚑
❌
🇮🇷
یک‌سایت خبری روزگذشته مدعی شده که مهدی‌ترابی در بازی با چادرملو دچار پارگی رباط صلیبی شده و فصل رو از دست داده! باید منتظر تایید یا تکذیب این خبر باشیم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.49K · <a href="https://t.me/Futball180TV/105065" target="_blank">📅 10:07 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105064">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac5342ab00.mp4?token=MrmELqFc0RxVKgA5h3ZaqM-z7u_5c8YnEzbp6RL3RA1om_H76Mx5KQmvYVmKnhcTGhhZUyw5nCAQAMPbPwQSKbX_LZf8u7NXaz5RY-Te4oJR0EWruLXHpwcgRo13ZldGjxPlWadiXNo2Fu5rkKhuBk49CGbKqYvU3i6AN0gfyGm0B0SA14ATdS4psiXAHSm7CaN_LmMxxl1Yifmcn8u54khB5inLYY2i6aRoaWl633Ld6OL2BowVfBTSB-np6THrmyB8NM6lHJh89qwTXzRImMoKh_mUhg7Zdq05ZxfCUkSXz_G7k3TXDhgWeyPAvw9blMJslfqHnbxcKHpHgYip_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac5342ab00.mp4?token=MrmELqFc0RxVKgA5h3ZaqM-z7u_5c8YnEzbp6RL3RA1om_H76Mx5KQmvYVmKnhcTGhhZUyw5nCAQAMPbPwQSKbX_LZf8u7NXaz5RY-Te4oJR0EWruLXHpwcgRo13ZldGjxPlWadiXNo2Fu5rkKhuBk49CGbKqYvU3i6AN0gfyGm0B0SA14ATdS4psiXAHSm7CaN_LmMxxl1Yifmcn8u54khB5inLYY2i6aRoaWl633Ld6OL2BowVfBTSB-np6THrmyB8NM6lHJh89qwTXzRImMoKh_mUhg7Zdq05ZxfCUkSXz_G7k3TXDhgWeyPAvw9blMJslfqHnbxcKHpHgYip_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
⚠️
فرونشست فوق‌کیری دیروز در اصفهان!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/Futball180TV/105064" target="_blank">📅 09:50 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105063">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/891ec9c375.mp4?token=R9bH1a0YnrifdI0gV71v2FfycpKhpsgw5uGz5Fqn6Q348AT_IYABTP4S5UfP0Q8c4_H4XBKz7qb43S5X3aaoY47uwUB3NHVbtIS6CmvOQ8jmNMpBCi3i31C1IZBVKyIOYH5tGcGMDDntg7ThrFcrPxMZudSFL8ZcLYZEDg3OofhW_jELnKKL65Thic7Nv31z0RC4y_J5u9ZaOw8FVZVCqhV3CwCv3NY5BLDYDX0c3mK1Tmw1fYOUrq0km5taBk_EbyFYVmgT1-JxlNIb3H8qtVD2wg-IECYPfc_-fjNK38qpOP2_6fWMfvAMwhab0DbjIbcnW7rMOliDFIByIgG3Soi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/891ec9c375.mp4?token=R9bH1a0YnrifdI0gV71v2FfycpKhpsgw5uGz5Fqn6Q348AT_IYABTP4S5UfP0Q8c4_H4XBKz7qb43S5X3aaoY47uwUB3NHVbtIS6CmvOQ8jmNMpBCi3i31C1IZBVKyIOYH5tGcGMDDntg7ThrFcrPxMZudSFL8ZcLYZEDg3OofhW_jELnKKL65Thic7Nv31z0RC4y_J5u9ZaOw8FVZVCqhV3CwCv3NY5BLDYDX0c3mK1Tmw1fYOUrq0km5taBk_EbyFYVmgT1-JxlNIb3H8qtVD2wg-IECYPfc_-fjNK38qpOP2_6fWMfvAMwhab0DbjIbcnW7rMOliDFIByIgG3Soi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇹🇷
ویدیو جدید از استقبال پشم‌ریزون رافائل لیائو در قلب ترکیه و توسط گالاتاسرای
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/Futball180TV/105063" target="_blank">📅 09:25 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105059">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/srYqGxqGz9O-9Y2pAYG6h69xEJPWCwLTg3vUxgoi27T0f6c_GIzQ4eOjmSLBbu5tDVANKJxeejNxBJgNLY6QWID-vebhVqdXB8WFUDvEI5vwLGI6RbGMjKl7TdRqJnoYCSEPJQbuOck9p68gl70W30muc_i81dG-KM7L98PxXDKI4s9m2NcYMZoA1a9RW7lf6-GRVo_fxWyjovPlDd3EZwpMphMrbBRRagEMel6kGhBpSnM9vbqVMMS-LzSP0oR6sYCFE2BWy4zscutDaepFoZQtfL3WaIuNVHBthJj3B8ADjJ209N3zUa3m1cs0Enss-U5uUYhwc3QiOyBnG2iTAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oRUgbl3t6Nn7GzBGAPR_-l8QZtTVER2F2azO2D-x60G2hwmtNrvF_-_-d4yClVytbIWSgNP8iBAu5TA7_qxpe0ATpvMfq03xuPaoHbU0zjTS8ZpHUzCc02P6VIeitZiGhdL1HXsR5xeIE1xPSAFGLJT48GmdhbalIOfAom2VENyyY39Cyj0cB1it0138MR4f6PaxaG-3H_3F_01kRlCd0hsupxOwG_WislZ-ER3gtDIL8sa6ogvjOW9PTnj9aR3iGctZ6IOyfS23UZrFsBzjQbjdLrF928U4QOJlSZqtTWxPqKSsqBGY_s3wLRFVUEk_mdDDm0FfRdr-eW2B_TRstA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ARmkU_ImXXU5syv_zSIZ6Q_yWBKz1a5LcCNpgLMkm9ziZM4xTtSYtPhAj-wVAPpLfPr2WI9JTirq9SkpLodxZaEhne3nbnHgEjNC9rekdR0K0SJ0LRei1TlvNfufvTEjlZov3diOCvfNEsJmo3KHNcTbUiJnLJjkdio4rEHSNecMWk4QQHPv9Z3ApmeO658RBMQU6TD-eIJ2vm6fKnwWpFK9KtBIkh8NQRFSLSkuEheczu8hrvvWSnyFxRtK0CRNZKKStnSty7LOZSs4D0sdBwvB9rj17FBAJQS7l8M7-JvhBfY49EtQV3axQlxM1f7A8832T1xD71h65A9VixWNfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PCDfNEYKVFykm0UunNU1Hi2ka0-hd77YNUfck0c38Cj1M-mkOXjy5J6lVRQce5PYd95CskzupQYcbGZOYzRufQKfu_tVfYEKfoYvvuo8iGmKhFh0yF7ZcMn4ZbOHpw34Xfg_117LwgIbzKg9jxfeng-o36MoE9vxf86skGC3ViNR4HtBivdkP0S7sj1MqE-BzDWU-e1MgZ7O68YGCJnjdX0qAIefTA3FpiA3KSk2JwONXivi0qqihRrmVKp5Ub1ek0jIQIPWHbDc1G-h7ByXEvSs-ZQOBb_c6ZhOJO3xhIXWeGEXEWT7dv7XXZ4URUQrGRglAmJY1IiG9RbIimM-ZA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
🇮🇷
بانوان جذاب پرسپولیس در بازی دیشب
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/Futball180TV/105059" target="_blank">📅 09:00 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105058">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1503ea5fd.mp4?token=OeEp2ZjQP-ySVOn88kEbmElMFboHRGgsV6wjvnSy08Z1nTWzra10TGKIGMxwWo5JcxYhRBD15fZUCav7tEPH-SXZInFS_mYO-mQ_oaAstrwvUrGS1FogNU-RzQQTPRIqyyW_GfyjB3Zb5cD1C4onN0zUvIIat_Kq3CJFFaZ1rrnjLslE1x6kKrjDiTstWla0CU8IxTUWoNhVVmZpbRCzu40DAVCgS8Z8Cc2-q3EIaD-yvBZTFWSAhpr98wq0QuhT2YCXsQZVV2bld_VeDBLLk1yyVdmiXdXwRy0ZZv6cI80agIleO2P1L0Mz6A68MnzUJLcXDcchVJYA91tIheNjiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1503ea5fd.mp4?token=OeEp2ZjQP-ySVOn88kEbmElMFboHRGgsV6wjvnSy08Z1nTWzra10TGKIGMxwWo5JcxYhRBD15fZUCav7tEPH-SXZInFS_mYO-mQ_oaAstrwvUrGS1FogNU-RzQQTPRIqyyW_GfyjB3Zb5cD1C4onN0zUvIIat_Kq3CJFFaZ1rrnjLslE1x6kKrjDiTstWla0CU8IxTUWoNhVVmZpbRCzu40DAVCgS8Z8Cc2-q3EIaD-yvBZTFWSAhpr98wq0QuhT2YCXsQZVV2bld_VeDBLLk1yyVdmiXdXwRy0ZZv6cI80agIleO2P1L0Mz6A68MnzUJLcXDcchVJYA91tIheNjiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🟣
در جریان پیروزی 1_7 اینتر میامی مقابل مونترال، لیونل مسی موفق شد چهار بار گلزنی کند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/105058" target="_blank">📅 08:43 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105057">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O-9JlfUAb8ZcJwBJebMVQvhOf5qu_i5Nd_Rk4U6f5Zo2beSutXfsdtoZ9i61Y6ncLp9N8JDTrg9PjJz19NpGjrdvkNTQs3-PxzGZrdB6kA-Q6EDwQkmDE0c2kVSLNi8J6O5M2-1Hw8VDPNCuRzwf7CNuJPaPJ5Lcgl4hwPmOpcvklTN2LqIqwnAzClHf24PTGAAZ-EBYegc1fzOwfIHn01b_qG5go5WhRfFZRvkIxYXH4yzO-L9i_DkcEERq8CBB5vMoOGT95ABh4-cCFTcCRzuLMw_mzDGr_nlvhoIqYh5f0s54c_NK8Cd_rgxTwqEeZN2A0zTMDD6xkBjFPwCw7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😶
🚨
🚨
این کانال باعث ورشکستگی خیلی از سایتای بت شده و پلیس FBI برای دستگیری ادمینای این چنل جایزه تعیین کرده
🔥
@Vision_Bet
@Vision_Bet
@Vision_Bet
@Vision_Bet</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/105057" target="_blank">📅 01:34 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105056">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/105056" target="_blank">📅 01:33 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105055">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uObChr4iQvlDfUzQavOEKK_KWD4EYmitwn05AdmRsUhlykNER_IzI1u1BZcMv923j2tHjTbbzlPk1yWIyUHW_7WZtFC3VIHFJrd9V8BpfdvPKJD9Wwc1RUm0rx2s_Nd-_YImLeslyc19Q_sGHmOGdq4p1ge6jhNqgQAjQ4mVB05UJUJIikJ_GwwTw3eNB1SY7_liueTu5TMzsyMRtqmAjCz7HPNFKfhSr8WXan35k2ChngdULJ7kMUa_4yjuR5VwVHSco0Ducm33imwNskTOYBkmi_KLhpJ9tSxtz3Qeek4vQd7YO2u9Wm-LUrX6Q7JjjSORNdLwAasAYWWZ8jMcEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇮🇹
🇪🇸
متئو مورتو: اینتر تا این لحظه با جدایی دی‌مارکو به مقصد بارسلونا موافقت نکرده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/105055" target="_blank">📅 01:24 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105054">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r_sKV2G7GEuF40C4a6eUvQ0PIDq4LUxJZPDBg4-9xA6TDIXyGehrNUyJ4BNEJL7IpXG8Eu1uIY9MMcciqWZO1ljuGUUUwc5LZXYQTgPpJOocdrOuo8bA7DWDkBO8MF97TxwxZSns-bOoq-cTgTSBGY0vlsknI3UGLAFWa_EEuXIfCuNypGWrIv7tFjbueJqOvhKERhZGX6Xgy9qQq_Np28fOpaHnymaLLlfAaHq11CtM6dv5zzjPICpaHxN51axW_-NNMX7Yta5pWMrMBFer7AuaoRlZuIO7XbZQQgd071jU96QnVhY_J62kN9vRt2YGqgRsAufQExp1igpN2KFkPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📱
سردار آزمون با انتشار یک استوری به صورت غیرمستقیم از دعوت شدن به تیم‌ملی برای فیفادی خبر داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/105054" target="_blank">📅 01:14 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105053">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W2azAUBQPbdKpEgt1X7Uq_GDsu_6l6s1muixFRCMX8sixxh8DyhJas-IhF2XSWmrJBkt-VDKgmld0nfq-bI-qTNoz2yu3e9T22byJf41VvyrQxhy70BDP-7wIblO1Me_b79UgUILvjn3Tekk7n4bULyMGm8yaF13UJML2rL1I-wCfhGqdqnPfrTtIc5In0SOs7_Jk4MSw_QJPQM8huGIVstrHU0GzQLb4ehw4Mj_94DXZ3Lul-O9_AD0Zeye1A4tqEADGZGXlG1kYMpP1stzyXdVVo9kV4cDOh8NoIbAv1M6lYpa27kVpre2P82P--o4HptImM-RLd3iOTNJOjjREA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
سرجی کاپدویا :
🔻
🇪🇸
🇮🇹
بارسلونا و اینتر چند روزه که روی یک معاوضه احتمالی بین «بالده و دی‌مارکو» کار می‌کنن.
‼️
این انتقال بسیار پیچیده‌س و اینتر فعلا چراغ سبزی برای انجام آن نشان نداده. بالده هنوز حتی یک دقیقه هم در لالیگا بازی نکرده و بارسلونا به دنبال…</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/105053" target="_blank">📅 00:56 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105052">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fiRq3Bki8V4hnzAII2KO4z1sGavzKCalKNNeBTOwPlCYPU15zdL_Bm1p4yO6sb-zfibHDPY9s9VDWP_IFBoZeTS44dKMuUX8C1kzRIIAAQ16ShbT8EwQ09NY_bTmJ1u3PQa-h1HDwa11r7z0bNvkOV4yZxLtfLJSiaMS8x2jxZzJ3f8VIfj6GC_FpNFKJp7_8P4yCg3b3Ts530j7QnR2QZxG2HC9gSdRBRtxv_bk8C1OXjZU-dYILMOEWoEjnnZsk69tWqgZc7zJoUwDyH3TsFv6k_KFbmcxd96UNEYNUy8sfMOKFM5tKL9cOebhDhY-JpfdBa57NhFfo6djZIAklw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
🇮🇷
#اختصاصی_فوتبال‌180؛
❌
باشگاه استقلال با ارسال نامه‌ای به فدراسیون فوتبال اعلام کرد که تا پیش از بازی السد هیچ‌یک از سه بازیکن خود یعنی سحرخیزان، قلی‌زاده و رزاقی‌نیا را به تیم‌ملی امید نخواهد داد!
‼️
این درحالیست که بازیکنان دعوت‌شده باید تا فرداشب…</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/105052" target="_blank">📅 00:18 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105051">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MH2fCJmtRxl_a_TIn6DNc2oONSc-mqixsSNU_XPngCw9B4yofh2oAhsjRjt6Nw4nFYXwoSygotMLckV18K9p52-1j0mTIoIoG3dHwxwXu8mGNQJ0PzHvCcUX2CImEBwX7vTVrtipUWz06BiwQzQ66ZBTc_gI_g4gI6rm7E98DBKCDDbs3cSooRUCYnrgTwZzcMKlAjh-S5keTklTtb9QtzTmqQv1bFnUvlXasuiCPu6qKRgE_nxoJpLLx11yBLsspt5xVHXDx4gE-bKz5DuQ26-akWHtEG-qeaMf8euwPUQL5eJDlKgjEnNIXuEPKCkngYfqJWM1GwbcKc72hE2GYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوووووری
از نشریه تایمز: منچسترسیتی تقریبا با لیورپول برای جذب کودی گاکپو به توافق نهایی رسیده و احتمالا امشب یا فردا خبر رسمی منتشر میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/105051" target="_blank">📅 00:04 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105050">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XsLJIVBeP9eGFHQGxDISwwt4frz_jAiKR57_KU-7oOpg8kzJyF8rlOp9CSYWp37EnlYZoKZdygdF6r6ev8dlqPHBLZ39inHGdjCPUqqYreQucOhKzTBYU5SqYJCbtZ4ya3neQ315ME9BSPVUl6ieN4YvOOfyJifUYwnQpL-JxP3RoeK-R2jQaedNN7V_7jQPix8xtKB0J61IXakIPOs_eSJyraFRk_RatOA6lR5u_ikfHwnYX9Kim5Czp1YvM5tTqOQXa9Y9g3xqOM940NFlhlSitFoQV-0l87LVHYLhl-EODiM_6JMVz5ReH6N0BLf4Q9_Dihegy14hkphbv5F-tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
سرجی کاپدویا :
🔻
🇪🇸
🇮🇹
بارسلونا و اینتر چند روزه که روی یک معاوضه احتمالی بین «بالده و دی‌مارکو» کار می‌کنن.
‼️
این انتقال بسیار پیچیده‌س و اینتر فعلا چراغ سبزی برای انجام آن نشان نداده. بالده هنوز حتی یک دقیقه هم در لالیگا بازی نکرده و بارسلونا به دنبال راهی برای جدایی اوست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/105050" target="_blank">📅 23:49 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105049">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22168159c1.mp4?token=hGTjtW_aIjNGEKjiZUi4AIcwrUkCGX3tNNATmV2WDdBhvrt0wnRCZjZSKVABgIGaM99tHydrbw7U3POS5FCNXdr96zyzZZSumnnhDqAaPtMH2jU8j1cXf5mWJs8Av9bVW9aOabDi63sWdrIHen6_5TYe11RCU8zzDPYzSNpi7n3idao2eFc1C3bgERdSZQHUPUswRvoAmnBw0SsfB7c8sfs74vFxLID4848XdWuSN9jKOFIfFV76O9fonbrGpS52LgnZz8Xjsqd3xa-2m5V2_aceg5wKD1YtPzGZWz1Wr0QAkbXHrsgtFeIrCZo53AZuHj5Ena08mnPuNO5_WW9Htw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22168159c1.mp4?token=hGTjtW_aIjNGEKjiZUi4AIcwrUkCGX3tNNATmV2WDdBhvrt0wnRCZjZSKVABgIGaM99tHydrbw7U3POS5FCNXdr96zyzZZSumnnhDqAaPtMH2jU8j1cXf5mWJs8Av9bVW9aOabDi63sWdrIHen6_5TYe11RCU8zzDPYzSNpi7n3idao2eFc1C3bgERdSZQHUPUswRvoAmnBw0SsfB7c8sfs74vFxLID4848XdWuSN9jKOFIfFV76O9fonbrGpS52LgnZz8Xjsqd3xa-2m5V2_aceg5wKD1YtPzGZWz1Wr0QAkbXHrsgtFeIrCZo53AZuHj5Ena08mnPuNO5_WW9Htw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔥
🇹🇷
استقبال پشم‌ریزون از رافائل لیائو خرید جدید تیم گالاتاسرای در استانبول!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/105049" target="_blank">📅 23:06 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105048">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/128d699010.mp4?token=n4sIyiHSB9HGk3cJooSUx0VkwtcEwX5VyRk15bviHAwJiHFaFEKwqmTJcmFl3VrSXZ0Qjyh0K3ZFh_dLi_nORDk2bN11EDzF1A6c9SZtTv2Ng_WEY1_KwShjFwVUOAnJideR_Mp8CuVqKe5QXUG9enNxI_W81GtAN0j8TJz9ap3W1v50zlU1nRH-DTQty6qlguPf_DEl774jq5pOURTVRAIym2odWaf6um4R01G0pGVVQwwdeUjC_qORwNZwIbhDipvjhXHQL_18sJkaEijqAmrYywoe211oRyZHYLJypeJVizuyZZkugrpxqSoG3iz7OdOuk9AFJRdMf0H97sDgCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/128d699010.mp4?token=n4sIyiHSB9HGk3cJooSUx0VkwtcEwX5VyRk15bviHAwJiHFaFEKwqmTJcmFl3VrSXZ0Qjyh0K3ZFh_dLi_nORDk2bN11EDzF1A6c9SZtTv2Ng_WEY1_KwShjFwVUOAnJideR_Mp8CuVqKe5QXUG9enNxI_W81GtAN0j8TJz9ap3W1v50zlU1nRH-DTQty6qlguPf_DEl774jq5pOURTVRAIym2odWaf6um4R01G0pGVVQwwdeUjC_qORwNZwIbhDipvjhXHQL_18sJkaEijqAmrYywoe211oRyZHYLJypeJVizuyZZkugrpxqSoG3iz7OdOuk9AFJRdMf0H97sDgCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🚨
❤️
کریم باقری خطاب به هواداران پرسپولیس: موضوع ارونوف را به کادرفنی واگذار کنید. پرسپولیس بزرگتر از هر بازیکنی است؛ فقط تیم را تشویق کنید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/105048" target="_blank">📅 22:44 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105047">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bdc84af493.mp4?token=PAQWBO_zY282hq6RfYgrCRM5Zb-oMSV4P2BX3kvDOJp1YMLm4ZYECHj20v5kV5wue0WOreT8_NTAWH6JpVE7aAVeNSMoM3gbNmh9Anx6Q5Urra7dhcbd2-tXDco8xBvAwqhWnECFywh9f8Yf9_PxNS5uIVmPWMxY6QuBCGBBoxcurmBSH1S7jO8_IFe96OrYX7csLLMPHLFF9InUY6xr5UvwZTtmWRW6FpJQWgCQs-Fy-F77EuivP9gF36TFg1i72UjJa746LJSInXY4wSHk7FJtIFJI1cDwd2bE-XSm9Qw-2DwmButj4MLQSki7hu5NsbC5qQIN1RuxlDBChaJqIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bdc84af493.mp4?token=PAQWBO_zY282hq6RfYgrCRM5Zb-oMSV4P2BX3kvDOJp1YMLm4ZYECHj20v5kV5wue0WOreT8_NTAWH6JpVE7aAVeNSMoM3gbNmh9Anx6Q5Urra7dhcbd2-tXDco8xBvAwqhWnECFywh9f8Yf9_PxNS5uIVmPWMxY6QuBCGBBoxcurmBSH1S7jO8_IFe96OrYX7csLLMPHLFF9InUY6xr5UvwZTtmWRW6FpJQWgCQs-Fy-F77EuivP9gF36TFg1i72UjJa746LJSInXY4wSHk7FJtIFJI1cDwd2bE-XSm9Qw-2DwmButj4MLQSki7hu5NsbC5qQIN1RuxlDBChaJqIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
❤️
کریم باقری: دعوای بین باشگاه‌ها و تیم امید؟ زور هرکی بیشتر باشد همان می‌شود. اگر قرار است قانون اجرا شود باید لیگ را تعطیل کنند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/105047" target="_blank">📅 22:36 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105046">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M7MliDpDGv3b0TW4aAcjDA7U92xp2wtyXjaYlyQw5Omw9npMChrZ9SmhcCveHBXxtrFeA_2W1h8IjKG5hB9dtBN-ghC2iQuB5hH3DJYd7kfdpJQ26RyCIWJN5mc0LxHQvm1DY4hwvv7Q0fyY8F2OyO7B3QzjC0Ri2nd9JXGWzfVtKnMHxZjjTEUwaeyMGM1_b_8PB-xptM_q_daxT2FLrZITcDBNc115iYXPZ-A-uwsg-RvOJowLcfun7ik6Vxf5GaYGJwIDUuaOFyXE9vkHSdajvqWG-sE19saa5O0IKRxNRhVHNwrpWedZ7c0s7FFl_NmxHFrXgMpyW5g6_1LOKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
🇮🇷
مهدی‌تارتار سرمربی پرسپولیس بدلیل شادی زیاد و افت فشار نتوانست در کنفرانس خبری بعد از بازی با ملوان شرکت کند و کریم‌باقری حضور یافت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/105046" target="_blank">📅 22:22 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105045">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e97755c4d.mp4?token=KHt7vaapZtMsax7Vbrv_Z-YlVgAnDk1Cum_PPSMbQdg3B2qr2oWBAVafSD_zana5f7d0IwziPN_glmNoirvUApU9FMfIRB3O7kA6accn8R1MDVQZwjNkCJaW_mcS3w26nX4S2TJWjyD5jWfPrwBCH9OeYXUgqZmb8-93s4vScUAkdaL2mi4t7ocWIRHAEauQX3_oRMoDVop4-oM72YavOr2LBm3Uy9a1E2WeBe8Bv12vrLsEHGZyrXQ7hgYAul8WTLcY9JHEgWFy_mAMtKRVGAnR7qW1fUbhWwDc9tIDnsYUqrGYO354sXgHXX3oTvSUHVdrqcG_52YO1877JJNG4DXjgvNg8WmHCIrvqOV__UjV7dsHA_q2xagtVapDhqX8IsY3rUJ7gyA8HLIWbkT5-XUrMhMF-JGdpXrXgk1vDktD2s-bNqp12WsLWlGg9zTb3yO2mbB4RT67E0B_art05wQBD-EBqJgu9bBo2xGrWQll3fgKbgLvHVcGe0LaX7xGHILCCT2871IMFxwTZGEBcIyLC2zH9AJOe1iX_8SARzpD10TUrr77U7bJg5ZHY2uhOeekVK8xbhBRTt_JcTVaGG4NtQY3860urXZlx_rn8XgQ5_2v9j3xqq_PPaxcC2QO66i9G6UUfC6d6N3zuF8xne1jzY4L9cDG2sRqdmHjsOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e97755c4d.mp4?token=KHt7vaapZtMsax7Vbrv_Z-YlVgAnDk1Cum_PPSMbQdg3B2qr2oWBAVafSD_zana5f7d0IwziPN_glmNoirvUApU9FMfIRB3O7kA6accn8R1MDVQZwjNkCJaW_mcS3w26nX4S2TJWjyD5jWfPrwBCH9OeYXUgqZmb8-93s4vScUAkdaL2mi4t7ocWIRHAEauQX3_oRMoDVop4-oM72YavOr2LBm3Uy9a1E2WeBe8Bv12vrLsEHGZyrXQ7hgYAul8WTLcY9JHEgWFy_mAMtKRVGAnR7qW1fUbhWwDc9tIDnsYUqrGYO354sXgHXX3oTvSUHVdrqcG_52YO1877JJNG4DXjgvNg8WmHCIrvqOV__UjV7dsHA_q2xagtVapDhqX8IsY3rUJ7gyA8HLIWbkT5-XUrMhMF-JGdpXrXgk1vDktD2s-bNqp12WsLWlGg9zTb3yO2mbB4RT67E0B_art05wQBD-EBqJgu9bBo2xGrWQll3fgKbgLvHVcGe0LaX7xGHILCCT2871IMFxwTZGEBcIyLC2zH9AJOe1iX_8SARzpD10TUrr77U7bJg5ZHY2uhOeekVK8xbhBRTt_JcTVaGG4NtQY3860urXZlx_rn8XgQ5_2v9j3xqq_PPaxcC2QO66i9G6UUfC6d6N3zuF8xne1jzY4L9cDG2sRqdmHjsOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🎙
🇮🇷
تیکدری: دربی 3 امتیاز دارد. فقط به برد در آن بازی فکر می کنیم. تیم ما آنقدر بازیکن دارد که با بازی های کم فاصله فشار زیادی وارد نمی شود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/105045" target="_blank">📅 22:17 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105044">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3d295e52c.mp4?token=Xny2uFWf57pDC9AqNjp13beaicFiC5IpVjhJ9irMMWABhZ0dJCtSUDYUNj4hiUnH__3c7nIaoEzM1so13ngvtUQfzUEcZvJ0-gmeApogVL91PLZMdxZ9e1HvGLoSp-hUkDQExbGt6ElE87pgx0gTYdzCqQw4LFLyMrPIgTJEt2uGRsZ21LegzrXE6tLaeIZf3j1R9DuHnPZIUNfsl1Ec3wau7bcCAJW3EGeAR8Y9rXsIsPUb0pV7ajRzy0ojdWcl5MCB6qausKewLeQJH4L8fCvlXM2rHPguthPT4hkxKPhZns6NznLZay3uaj_5bXj8aOv1f9c1WrHfAZxJyJrW8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3d295e52c.mp4?token=Xny2uFWf57pDC9AqNjp13beaicFiC5IpVjhJ9irMMWABhZ0dJCtSUDYUNj4hiUnH__3c7nIaoEzM1so13ngvtUQfzUEcZvJ0-gmeApogVL91PLZMdxZ9e1HvGLoSp-hUkDQExbGt6ElE87pgx0gTYdzCqQw4LFLyMrPIgTJEt2uGRsZ21LegzrXE6tLaeIZf3j1R9DuHnPZIUNfsl1Ec3wau7bcCAJW3EGeAR8Y9rXsIsPUb0pV7ajRzy0ojdWcl5MCB6qausKewLeQJH4L8fCvlXM2rHPguthPT4hkxKPhZns6NznLZay3uaj_5bXj8aOv1f9c1WrHfAZxJyJrW8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
🇮🇷
کنایه فوق‌العاده شدید مازیار زارع به خبرنگار برنامه فوتبال برتر: دوست ندارم تصویر من را در برنامه تان پخش کنید. شما اینجا باشید من مصاحبه نمی کنم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/105044" target="_blank">📅 21:58 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105043">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jK8vH8HPewJ7E3m9u1x0zl_Kmlqo5KFP_8p1RS-CBG-gWgecY_lKDS1lkOlmG8TPkR92m_b9_1gv7zPdeiPdCj5OsTOXAsvm7aVXKStIn4jc9JlEQsrIq1LQoLAIrX2saaJFKDBpnhnAuEhRleuv8KP57DupPcn2wzCocGUKhHlsp_IqS7E_JqIxD9Rf2txum5NO8FphQxODRupeQl8d7cGLHtOitLOlFXCY_hTzWXO8gUOKzwiBGc5PA7xmimKzigi3Qip942-UyVEl8oJsGQtxDL9yOdv1nu7QdHvUMfBXKMmXg7GlmOcMfSpiLMo3qv4izM-7KLAFNsNkalSX2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
🇮🇷
#اختصاصی_فوتبال‌180
؛ کوپال‌ناظمی از سوی کمیته داوران شانس اصلی قضاوت در دربی روز چهارشنبه معرفی شده و قرار است تا روز دوشنبه تصمیم‌گیری نهایی صورت بگیرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/105043" target="_blank">📅 21:54 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105042">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d2706c562.mp4?token=QOlJWEVpCyNwbKsd1ubBAVEebeq9IECPPgUz30OMYnedO2JoY2xs9u5EgG94X5nETgOd6UZ1Ci2DupU4EGcPJk1hkpsIPwh9MeE5JCQ7ptyaX2-de-OThXwSc2daUzeW9U3NaD4cJC-o_QVf7fMUy5RqWdxUsZH4zbEzHqY3ZW7KM_9FhYZLM5ZDkX4J0HDQDS0tjxtRyWNQnC3UqakbdonmK_y2Muiw94Ikqp7UzQ6YcPAorFa6MEy5QNLUFuM1ZQmCG1KuiZCQmczX7CFCIoXhfQSqe48Aw9xEAKHyutNtN2Chpzz0u4suFihmWWSxkWt8L8Z2hEGZHmnRponbJUoiuKcvmbmUQa6Ysqk_zTGBWLS5wVjL1CXPSyO3eIxuy7Aj1NfIN9tHf2xDxSc8DfPW9GC65vexFzsKAEUXMcxq1mI7zwEHZVmJeQcg5mksGKVd0UcIX4_GC5TxiIthv-WB1Z1-LppxgnqCYaSGbs6zWRiGwuBdOzyFFmi9kiUtpGlKW55jpxQmZQJDF49bkIx8gT1PC8S23GpYI2F3UQanohr7yv9wiGyOJuEmpAO8RHk_AXmAo8ksbe8nOYW7bzEQmM2H_sqpxdwG7Xa1uHUDXO-mlW_6j1RsFM4G59su66EMNy7fgFkFceMRiFTXUuuJ4zHPKmTU-bPHup5DENI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d2706c562.mp4?token=QOlJWEVpCyNwbKsd1ubBAVEebeq9IECPPgUz30OMYnedO2JoY2xs9u5EgG94X5nETgOd6UZ1Ci2DupU4EGcPJk1hkpsIPwh9MeE5JCQ7ptyaX2-de-OThXwSc2daUzeW9U3NaD4cJC-o_QVf7fMUy5RqWdxUsZH4zbEzHqY3ZW7KM_9FhYZLM5ZDkX4J0HDQDS0tjxtRyWNQnC3UqakbdonmK_y2Muiw94Ikqp7UzQ6YcPAorFa6MEy5QNLUFuM1ZQmCG1KuiZCQmczX7CFCIoXhfQSqe48Aw9xEAKHyutNtN2Chpzz0u4suFihmWWSxkWt8L8Z2hEGZHmnRponbJUoiuKcvmbmUQa6Ysqk_zTGBWLS5wVjL1CXPSyO3eIxuy7Aj1NfIN9tHf2xDxSc8DfPW9GC65vexFzsKAEUXMcxq1mI7zwEHZVmJeQcg5mksGKVd0UcIX4_GC5TxiIthv-WB1Z1-LppxgnqCYaSGbs6zWRiGwuBdOzyFFmi9kiUtpGlKW55jpxQmZQJDF49bkIx8gT1PC8S23GpYI2F3UQanohr7yv9wiGyOJuEmpAO8RHk_AXmAo8ksbe8nOYW7bzEQmM2H_sqpxdwG7Xa1uHUDXO-mlW_6j1RsFM4G59su66EMNy7fgFkFceMRiFTXUuuJ4zHPKmTU-bPHup5DENI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
نبود توالت در استادیوم مس‌شهربابک که معضل هواداران این‌تیم شده
😐
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/105042" target="_blank">📅 21:51 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105041">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e73d84229.mp4?token=m7dgU_R2PLfL_Jyn3gbHIZ3DDYa7kqCfvriO3B6QFRFcORfl_lukqRg9yWwXHRXyCLpZsNEp0NgiPHLcTJzFXsdZAObd5njMHeWyxK0VW1fA3ZTkRBu46I3fKN-xEXXFpEcKnDxhs1IlUayJ49w2pbwjdxNaHthhzxrQzedMkTn0-37-xDvv2Zk4kAvi_YuEV2X2vN-IcOqMp5tWCsLW9cl4Y2of2XK_crlLQpLWvo0TftKMmpjXtlqy6hrkQRjOmUW8VOkdvMgOxGfwrbQAuDLwYg9mmFos_Ol2A8xua8QCYtvkg5Jp5A4MCTClAhJdfeHMo7avw2N9gEphVyps9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e73d84229.mp4?token=m7dgU_R2PLfL_Jyn3gbHIZ3DDYa7kqCfvriO3B6QFRFcORfl_lukqRg9yWwXHRXyCLpZsNEp0NgiPHLcTJzFXsdZAObd5njMHeWyxK0VW1fA3ZTkRBu46I3fKN-xEXXFpEcKnDxhs1IlUayJ49w2pbwjdxNaHthhzxrQzedMkTn0-37-xDvv2Zk4kAvi_YuEV2X2vN-IcOqMp5tWCsLW9cl4Y2of2XK_crlLQpLWvo0TftKMmpjXtlqy6hrkQRjOmUW8VOkdvMgOxGfwrbQAuDLwYg9mmFos_Ol2A8xua8QCYtvkg5Jp5A4MCTClAhJdfeHMo7avw2N9gEphVyps9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
‼️
🇮🇷
ابوالفضل جلالی:‌ حضورم در دربی؟ هنوز هیچ چیز مشخص نیست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/105041" target="_blank">📅 21:44 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105040">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0fd696124f.mp4?token=rN7iORzvp8ms9B7Z41TctjGgI9TCXr4a8FRC_cXqdHrgsYCYTX-GTGsVA5weW1qfvtsDVlKJGTAry4x8veCTz2QLWkQhAZIpBS9XQ10W03tpHzP6GLwZejYXbpMSGYK-tMl0nOTQsfVU9pZy0cY3qpIvKp-VuY_0jgyj7z9bHDubwOyxuTefnqx8Id3ZOVUjqYVOicz1RCO4YB71T81eUaFtANs77VeDqdDoxPzDUh3pyUyEeZCv_4-SlK4040muRdf2gf_BFHXWj5bLljWr31dpMDiDQusAvL_X511-6gdqRjmPk84GoACVK9ZWyiV_Clv49ZNvUOerd4cu-GPz7ZYHNgAcNhD-SQJk_CsEBUDpttcDxw1T25UXPMVpmD-e9G8sG8yCeTzw_1_vOfS08ExNmnuXZ07kLYMHgjv86kh8adhWgnDgbR8ZwjOhnb2I19GJxxm_9s-nqo723KGZRpAZPVSRIAm31J-cQl0YDmgzgVP-G7ZDJQXtMagS6HTyebAgnZ2iKUrz0Lm7Qfx_nSWEO8Jjb5O7VYM-T22qFSbJ7twwdaPJDXBQWnPbCAixsPwp8P7LXa4ZYLZFjXu1pdzpdDq_67fc8UYHK53wzYvUejsC854_TPB6KehsBsa2zLLZxznmfEQ-UgEW8Lb0Lx2GFpQoYAOryj5retFKc74" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0fd696124f.mp4?token=rN7iORzvp8ms9B7Z41TctjGgI9TCXr4a8FRC_cXqdHrgsYCYTX-GTGsVA5weW1qfvtsDVlKJGTAry4x8veCTz2QLWkQhAZIpBS9XQ10W03tpHzP6GLwZejYXbpMSGYK-tMl0nOTQsfVU9pZy0cY3qpIvKp-VuY_0jgyj7z9bHDubwOyxuTefnqx8Id3ZOVUjqYVOicz1RCO4YB71T81eUaFtANs77VeDqdDoxPzDUh3pyUyEeZCv_4-SlK4040muRdf2gf_BFHXWj5bLljWr31dpMDiDQusAvL_X511-6gdqRjmPk84GoACVK9ZWyiV_Clv49ZNvUOerd4cu-GPz7ZYHNgAcNhD-SQJk_CsEBUDpttcDxw1T25UXPMVpmD-e9G8sG8yCeTzw_1_vOfS08ExNmnuXZ07kLYMHgjv86kh8adhWgnDgbR8ZwjOhnb2I19GJxxm_9s-nqo723KGZRpAZPVSRIAm31J-cQl0YDmgzgVP-G7ZDJQXtMagS6HTyebAgnZ2iKUrz0Lm7Qfx_nSWEO8Jjb5O7VYM-T22qFSbJ7twwdaPJDXBQWnPbCAixsPwp8P7LXa4ZYLZFjXu1pdzpdDq_67fc8UYHK53wzYvUejsC854_TPB6KehsBsa2zLLZxznmfEQ-UgEW8Lb0Lx2GFpQoYAOryj5retFKc74" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
مصاحبه سمی با هوادار پرسپولیس قبل از بازی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/105040" target="_blank">📅 21:39 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105039">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/swS1SEzSU4Scb55K8p26Vc_iiskvjq8ur0fhA7xEUJavgQKSwwUn6oBg52JRHAnlUqAJ7XQC4ckHuu5QkqkXkOeRay-qDpKKVOmTiLSw2jlT0AX150IBK0jHb4E3fJOGyfOrpqrdYWasbkwGPuOZ2jP4e5srTheJnrLPza98IPNrIsBYb6ivLvM5LNcX_3rDoFKB-pNNPp3bKwC440Lx_kQa-eEEudqyh02rhKGObMXKloDdZZGEV2pVSrqszu5WMgFb_-DYHWi8H87-QuA4I_HbHs5JuCAXhEi8RAhpFd4kPK67Rq2ty5eptevBbSJex-MYXidGeq7d0OIopeZ3xQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
✅
هفته‌چهارم لیگ‌برتر فوتبال؛ یک نمایش روان و دیدنی در شهرقدس؛ بیفوما همچنان درخشان است؛ تارتار با پاسخ به منتقدان به استقبال دربی رفت
🇮🇷
پرسپولیس
😆
-
😏
ملوان
🇮🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/105039" target="_blank">📅 21:24 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105038">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G-wz9iVWsZpp67GorPZuWL6M7sPxAoslS1U8Sk1vDt7nREaF3gqD61qc_yhUgUWKZvTIfHmsmxXTd4w7A62nfby0fBlwuiH0LxVJF32-GQmbrma-XbZCcLYJoVo9V2k8y4qyPsVjX4aUxCpaLwC2GC1maRRCmAJiho6qpCB9LzyAahdt4txwDwX1BkaK-pOZa7hHd6SsEBXAbMOFkmnuxAizDMqDx9C1Ru1Rcjc4CDmO23mhmEoihVUgTe6zFJL2t1y6Oyy-FRLrrqUNhDmaP2_cFnUUMrRmY-qf4JNRq_zaGTU43hr3MnebrK1e-IgddjwitAcQAqdd3b-BoOANnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
✅
هفته‌چهارم لیگ‌برتر فوتبال؛ یک نمایش روان و دیدنی در شهرقدس؛ بیفوما همچنان درخشان است؛ تارتار با پاسخ به منتقدان به استقبال دربی رفت
🇮🇷
پرسپولیس
😆
-
😏
ملوان
🇮🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/105038" target="_blank">📅 21:18 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105037">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">❌
پایان‌بازی؛ فجرسپاسی صفر - ذوب‌آهن صفر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/105037" target="_blank">📅 21:13 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105036">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sND-cuYjIAIDeGpqzt1UI24zq8TWMcoxX8K88hPML6NDuBz2z0llds5iSt2vJ4N6mthvpUwFVsBNPDC1noJSfddHIWR2RkK98sl9vQQ5H_D2sVtL-47IWZWmSpzmbiByLnebevndMjwUKW-HjLWlNfpZpvQijNZ1Dduv8p-OFGFdR4rjSLzKjhSWTI2tecFCBA7MhbwSgzJu7QMbZeQ26DIPaM1RLmivNz_utZMFuJPlXpCQdx-sSudWTnSbO4eIH0Yy3B7JHjIRJKwSpPsWe44iSjwfOCWxmIYqxe0kVQh5vY9cAxyHQEFJiEb3jKU8rGogJs-yllMEorFKrAw_0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
پایان
‌بازی؛ فجرسپاسی صفر - ذوب‌آهن صفر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/105036" target="_blank">📅 21:03 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105035">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
🚨
🟥
بازیکن ملوان از زمین اخراج شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/105035" target="_blank">📅 20:48 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105034">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4bd7def575.mp4?token=ti4a4-GaSpotZfMGi7djX4-2kxx7NlFu7-YgCNG1f2t2a1a942uIlsPcVbfWOc-3cX71XabVtILcIt-kHt2dnh75xXrkXo8cqOqRchi-orS_a_2xYFm6p_Vdbzj-hj8O_duaDojbSym18TbeQEpdOk0figC_Rl6zoLfgMtFaLJBEzI6UdM5CEoMR4VCociNh2X0mnDDwGvszcyUqq_4z-a7B96uVKyloaILkwkTsNuXRPBCu9onOTNWy9Gf5KxRMzOesjrp5NBIkkIWhGorCpYWU6emRk6b27xj4reh0WcuzJipSUHrketkx3_d0UPSBLiABstkJiZ9we_KOALbt5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4bd7def575.mp4?token=ti4a4-GaSpotZfMGi7djX4-2kxx7NlFu7-YgCNG1f2t2a1a942uIlsPcVbfWOc-3cX71XabVtILcIt-kHt2dnh75xXrkXo8cqOqRchi-orS_a_2xYFm6p_Vdbzj-hj8O_duaDojbSym18TbeQEpdOk0figC_Rl6zoLfgMtFaLJBEzI6UdM5CEoMR4VCociNh2X0mnDDwGvszcyUqq_4z-a7B96uVKyloaILkwkTsNuXRPBCu9onOTNWy9Gf5KxRMzOesjrp5NBIkkIWhGorCpYWU6emRk6b27xj4reh0WcuzJipSUHrketkx3_d0UPSBLiABstkJiZ9we_KOALbt5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😢
مازیار زارع کارد بهش بزنی خونش در نمیاد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/105034" target="_blank">📅 20:44 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105033">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a373e346f5.mp4?token=bpfEIKHsJu2-gKtrHaVYhGGkc0feRcehf7_HKDaPWHjlK8VUMW409B5yjadKAlV7rO3zK0_1hoWgaq6HmY-WvbtqRPq5AQPgXbXDer4wHoDSxqfSh_zfuy8agHxxKiZgvTUr_9gK5BvaATUf3Ly9ySbTdO2zOTcuHOnp8YdBQo9UVZe6LKLNipKFUxCMOkfhuJDg46BPMWMtaY6-MtzwszXTd7PIqNbvEMv_HxFW-zW2OMOiG1y9f2Qm1NNpbbEQHAIY6nL9TEcapGe-82DYP-ugaeA-kncA0-oRofczkkZNIl8bA3tHBELwdt4ozMXzAObjZgaZkb4jykHaIJFeq7sZuD0paSzv7E77NrE6kAvmQD22jQy3onFROFGRmR9_bqTeVXf7ahCHHB37e9amyB6-bZXdd5c6Ggk-9mo2xsuIYlE-J3xpanz4RpZu918V2kE87G_muabfvy8cqtagD_EwrdNrc_nQJVQJnVM-pfpvM-iyd7vRFsG-wtwAtbm7gnZfQa2wMVo8CtJI_vWkcNz08a39VstugIQOk3_DO1KrvZ3yhGow_0qzBPrxeTEzENSO5eHzkUYY9ZQnjIm_qfIDcOJq-sze3n4RjIYOjCMXPwKXnpwjmvZUQyl8MngZkPp6XQHUNqYVQ9isH7ZSOVzfxU9Mf_aaIxnNTfMnWsk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a373e346f5.mp4?token=bpfEIKHsJu2-gKtrHaVYhGGkc0feRcehf7_HKDaPWHjlK8VUMW409B5yjadKAlV7rO3zK0_1hoWgaq6HmY-WvbtqRPq5AQPgXbXDer4wHoDSxqfSh_zfuy8agHxxKiZgvTUr_9gK5BvaATUf3Ly9ySbTdO2zOTcuHOnp8YdBQo9UVZe6LKLNipKFUxCMOkfhuJDg46BPMWMtaY6-MtzwszXTd7PIqNbvEMv_HxFW-zW2OMOiG1y9f2Qm1NNpbbEQHAIY6nL9TEcapGe-82DYP-ugaeA-kncA0-oRofczkkZNIl8bA3tHBELwdt4ozMXzAObjZgaZkb4jykHaIJFeq7sZuD0paSzv7E77NrE6kAvmQD22jQy3onFROFGRmR9_bqTeVXf7ahCHHB37e9amyB6-bZXdd5c6Ggk-9mo2xsuIYlE-J3xpanz4RpZu918V2kE87G_muabfvy8cqtagD_EwrdNrc_nQJVQJnVM-pfpvM-iyd7vRFsG-wtwAtbm7gnZfQa2wMVo8CtJI_vWkcNz08a39VstugIQOk3_DO1KrvZ3yhGow_0qzBPrxeTEzENSO5eHzkUYY9ZQnjIm_qfIDcOJq-sze3n4RjIYOjCMXPwKXnpwjmvZUQyl8MngZkPp6XQHUNqYVQ9isH7ZSOVzfxU9Mf_aaIxnNTfMnWsk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
گل سوم پرسپولیس به ملوان توسط علیپور(56)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/105033" target="_blank">📅 20:35 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105032">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c8553440b1.mp4?token=ocFmSXJoscrssngUOOiCsk2tbumfEsMix_D-3bucgT2x0P2irETTJRYt21FVlVkMbYTW4CS586ZvOlunyMKSLAFhD_3O5F1jFdn1BGfzv-6UdivM70onl46NC8VdOB1Z2w3FY7Timd24EjrdsVJtotKFyiZVfYDi16GRNRBb1bt2UOhmJtAg-Tf846jOMhosnpgJ1FT0V4q3yeIa9rYB6Apydg-Ypown_Z8n_f2OlZpVqA-Byy5iLSaEJQMZ9NuNqXJDQHOhZYDNCU5ivOwxn9lsn24kj8djEwqC1ZFUezrLNnaoK1A19A8XWDq57CdLEDQvnPGFm7EtZTM5FBRpnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c8553440b1.mp4?token=ocFmSXJoscrssngUOOiCsk2tbumfEsMix_D-3bucgT2x0P2irETTJRYt21FVlVkMbYTW4CS586ZvOlunyMKSLAFhD_3O5F1jFdn1BGfzv-6UdivM70onl46NC8VdOB1Z2w3FY7Timd24EjrdsVJtotKFyiZVfYDi16GRNRBb1bt2UOhmJtAg-Tf846jOMhosnpgJ1FT0V4q3yeIa9rYB6Apydg-Ypown_Z8n_f2OlZpVqA-Byy5iLSaEJQMZ9NuNqXJDQHOhZYDNCU5ivOwxn9lsn24kj8djEwqC1ZFUezrLNnaoK1A19A8XWDq57CdLEDQvnPGFm7EtZTM5FBRpnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
سوپرایزی که دانیال اسماعیلی‌فر ستاره تراکتور برای تولد همسرش تدارک دیده:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/105032" target="_blank">📅 20:31 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105031">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P9Qx0fTUAxrOcXS2OqRbHqHE_cIx0AHkv5l07RwSczXpKEPp13DsDOwJ1OxO0wZ8b5kbizgX8sxATk7yAwytZ6V1gbqxwTB993tGqlZWp3THTGmx6a7CiwDeAi1do1D2SmZopsWyRUm4H64e9s3XukVgBOW9dQGSlWVu9kHdS3J90umES5ThDHhTE18M5Hk8fbjWjkNf5CFLhx3Z816vWLZKMeRvb_Wy8AfGwtcJh90L0J40YDGjWkMW7LM3SQ7SPBLNCHexqwxrM1-MQC6KZ4g89eKxOCNFLkrOiSeAgtJQDeVy1E1GGweOuXR4vJs5DXBBZd9bY7k7cHCEOOIDMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇪🇸
🇪🇸
تونی فرشا کاندید سابق ریاست بارسا:
جولیان آلوارز می‌تواند آزاد شود، به شرطی که به‌عنوان غرامت، مبلغی معادل سرمایه‌گذاری باشگاهش روی او و دستمزد باقی‌مانده‌اش را به لالیگا پرداخت کند؛ یعنی چیزی حدود ۱۲۰ میلیون یورو.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/105031" target="_blank">📅 20:04 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105030">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ce507e717.mp4?token=YGrOKrZ5n2dwIldZFhCokYyc0QhOO58gQuWWkX2w3AD6HgomFtdN89uAI45p_j2zSQP8FYXhfN-o_UVnChtjDNYJ_O2tnbRXUrfgQOobrB5VlAGx_epswp8YDj9DMF6GLu-aVixOrhxCr6XwIz260GsqU7C_OK_E4m13ToayGzPkYyAhDkWkGz2bpGrbDqipqxq2I6PAD2jlANmFqQc0px-X8k2kbmNLTC0BxW3RxOnzkKf8HP3PnJgHY5oKW93qZMo0iSe3iQkcRjhNOz3Cn4uE8sy7LB8CFZ096vGS_q_1sIKOLbm8BJLcdNybJwAmc9uTKZ2Txai4T2L0nVUSQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ce507e717.mp4?token=YGrOKrZ5n2dwIldZFhCokYyc0QhOO58gQuWWkX2w3AD6HgomFtdN89uAI45p_j2zSQP8FYXhfN-o_UVnChtjDNYJ_O2tnbRXUrfgQOobrB5VlAGx_epswp8YDj9DMF6GLu-aVixOrhxCr6XwIz260GsqU7C_OK_E4m13ToayGzPkYyAhDkWkGz2bpGrbDqipqxq2I6PAD2jlANmFqQc0px-X8k2kbmNLTC0BxW3RxOnzkKf8HP3PnJgHY5oKW93qZMo0iSe3iQkcRjhNOz3Cn4uE8sy7LB8CFZ096vGS_q_1sIKOLbm8BJLcdNybJwAmc9uTKZ2Txai4T2L0nVUSQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
ریدمان باورنکردنی علیپور در موقعیت سه به تک
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/105030" target="_blank">📅 20:03 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105029">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
🇮🇷
گل دوم پرسپولیس به ملوان توسط بیفوما
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/105029" target="_blank">📅 19:50 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105028">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c9bdeaa27.mp4?token=MeF4b2E4WEuBOuhwtNN3a3IzBE8IF4JGsXwMKXh0px8bJjzP_RRn82qa-e5gyt7bL8GLKzW4tRF3jUGROE2Z3GlCaUwiEB1fInJlbidQCKM0ytyvaLfjGxb5FaEspUQZulexUzUjbNs-MoqzRQJaxswKUQaGeqeH9Uzn_9FQBVrDAA2uxepNyphxgRmkka28zL19Wh-N28_twPBac8MxFgULqNygw9Rm2PJfKpvykO8wBMHEc-0Q_QTpMdneG8LYKA4tjZLiUK1Tbca7wOZrTqLOiOjfAebx4-qxV4lH-C49Z2CJ3kSxQNVsE6ui-dqCNvHXwp_n0RKDgMrC4USjFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c9bdeaa27.mp4?token=MeF4b2E4WEuBOuhwtNN3a3IzBE8IF4JGsXwMKXh0px8bJjzP_RRn82qa-e5gyt7bL8GLKzW4tRF3jUGROE2Z3GlCaUwiEB1fInJlbidQCKM0ytyvaLfjGxb5FaEspUQZulexUzUjbNs-MoqzRQJaxswKUQaGeqeH9Uzn_9FQBVrDAA2uxepNyphxgRmkka28zL19Wh-N28_twPBac8MxFgULqNygw9Rm2PJfKpvykO8wBMHEc-0Q_QTpMdneG8LYKA4tjZLiUK1Tbca7wOZrTqLOiOjfAebx4-qxV4lH-C49Z2CJ3kSxQNVsE6ui-dqCNvHXwp_n0RKDgMrC4USjFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
عصبانیت مازیار زارع از گل‌بخودی عجیب تیمش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/105028" target="_blank">📅 19:41 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105027">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93421b5bc7.mp4?token=Opgsb0J3aG2EpIRt8O79_VjPcbdtKzKFO23m-jex5nk1J1DrGg4ydH_QAtsG4S7edhHiG0Hmhc9egI8S2seCRRhGrfffj-RadgHayEzJNSHYqmh3TuF_ibaDK0Hjoj8jWwOg6KoMEDVyO8mNdm11xPcmPwk4U2vq0v2e_vRj-vRWmY0IlEGNiK_49K5Z-bTiMkMeTcYotEd7u4I1iKxRFYNdZcgZR906g15jwtUzeexbOZp2YPnYxCvOc7B-S7kGML9Pq4udaPuqC4cAhtd7JfzcDxpKb3VwKGt7pmQerxhOijyBYugG92Igf6ZlG6Yoc62gnWyqnujG9S969KqzLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93421b5bc7.mp4?token=Opgsb0J3aG2EpIRt8O79_VjPcbdtKzKFO23m-jex5nk1J1DrGg4ydH_QAtsG4S7edhHiG0Hmhc9egI8S2seCRRhGrfffj-RadgHayEzJNSHYqmh3TuF_ibaDK0Hjoj8jWwOg6KoMEDVyO8mNdm11xPcmPwk4U2vq0v2e_vRj-vRWmY0IlEGNiK_49K5Z-bTiMkMeTcYotEd7u4I1iKxRFYNdZcgZR906g15jwtUzeexbOZp2YPnYxCvOc7B-S7kGML9Pq4udaPuqC4cAhtd7JfzcDxpKb3VwKGt7pmQerxhOijyBYugG92Igf6ZlG6Yoc62gnWyqnujG9S969KqzLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
گل‌بخودی سمی ملوان مقابل پرسپولیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/105027" target="_blank">📅 19:36 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105025">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46f5729443.mp4?token=WnGZlBBcS07AJb1wmrIXwV9i2rn-UG3kct1rPv_dBf9On3FtopaSGm9x5KjoPDlXDGihbCuA1BdzgAbvOKU1pb4v1Ijm3Kp0qN0meGL2CW_22VgAeCD1w4Yk3TQ-RfxFmw_RfcCMXBXe7QZf516IgQOvMFLUyjfVmLqu9GRoFCZb8PZpS1VNnd9cLH2AK17P_37AN26UxHmak0NFk6NUjPrbh-MEe0kVBuHwF2SYoJpJz_m--x6PK2qc2BkmhvBSpUDm25Et9qzkyoNGFzHoxy3c6gIKZwvXtfW0JmzerBV2yvatM6VZlK3jka2JsSX4H3fZKBhaQd6uXAVOm1FZAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46f5729443.mp4?token=WnGZlBBcS07AJb1wmrIXwV9i2rn-UG3kct1rPv_dBf9On3FtopaSGm9x5KjoPDlXDGihbCuA1BdzgAbvOKU1pb4v1Ijm3Kp0qN0meGL2CW_22VgAeCD1w4Yk3TQ-RfxFmw_RfcCMXBXe7QZf516IgQOvMFLUyjfVmLqu9GRoFCZb8PZpS1VNnd9cLH2AK17P_37AN26UxHmak0NFk6NUjPrbh-MEe0kVBuHwF2SYoJpJz_m--x6PK2qc2BkmhvBSpUDm25Et9qzkyoNGFzHoxy3c6gIKZwvXtfW0JmzerBV2yvatM6VZlK3jka2JsSX4H3fZKBhaQd6uXAVOm1FZAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❤️
🤍
تشویق تارتار و مازیار زارع از سوی هواداران پرسپولیس پیش از شروع بازی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/105025" target="_blank">📅 19:22 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105024">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RLt9wMOPagSMLkDuRvuZY0s_3deTyCAeIhCyIusxBL-1gp62jJPUa7rmuZXTyWCvcWJoAsD-JPaIp2znQ0ELpOkxxJ4Uf-4q8FGhPhkqxvZB6tBSeZ-ns9sg9IrDAVZkqo084PlhFnkVM0QwOWXkr6vMdmRzJwrc9bE8TcL2A-u_ozlsQz4q6HB5ow1ki6GVmYujGUI8HWwGUeOLsnagh7LyZxZ6VO4t6FPo0WFuMDCx8X2YYBfcJVI5Neod6T9OxC3g6Of0FCCpqtxULUWCmotbJ2LahTXVG9fltRg0Aoh4AmCiU6hiAIl5cBvfi73HP26Z06eC-TSgRLNcZXZd2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🗞
رومانو: فرانک‌کسیه از الاهلی عربستان به آتلانتا ایتالیا؛ HERE WE GO
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/105024" target="_blank">📅 19:09 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105022">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mwGyr70B2pGygHnWKGaelrbkbSpwHSjqumoCrdueARBPEMrgLT1V4rJUfdVuBSsCcT2sfKIgcannzCkU7xTcqitkBtRYmvxVdf2VwJFeZaF-D3Xi3jm-U3EhZEFHaf9jikw-V7gKogrJ6GdZqVztSFkC7JZotubappyrisjAWaehsc45BmvcrcMfiTlaGdJ7Ehoo3kwM9cXaVwjx1_J1IaVRgASU5IzRSZ96nbT8aK5eF40ZIRo6cOtuWM09-AqAxl19zPLNWT4BCRqMliwPjEj4C9PY4_p1qiiPXvCK6J12wAsJFlIUWHgvoDvaVcPux9nVh11oNeXq2GzlwnmeiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ApTd5PtmPWM-oPlDP9QFoEQa1ejPReCMpkuFRWIjbbe-28UCcGzFaugYemxHVJ7UjkZAeV5n4ml0L8SSRrm7gUh2N73QBBWB-BoVRjrzjd8loN9F1o1IkK7NV6kmE5DTuEbryPwJn5CZRdMKg5dsWrnu04wN2oytq4BrRbMquaOxE5o7nJfqFyU8w-MYQNFghznxDSNwl2KoxlFiVoac8wRa2ZvjNubsjUdNQhuyKfhRCU4fv6T38jUUafsMtlwf4KhAHjBk2TlE7chVr2hEet_JNcheCMBial6ijBFuJp4shqyNj00y95qdxEdJdfHHoPvVSvlp4wBU7fzOdUAfxA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🏟️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
ترکیب تاتنهام و نیوکاسل
ساعت 20
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/105022" target="_blank">📅 19:05 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105021">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c974ddb250.mp4?token=TFhy9285heot1sNj8BKxWOSOW4KZDKBxmWrHNqcH57I9wCKQY4-eXXZB2BQQtXtwsJfLuib1Kt3v-UxN3dyVnTwp2dyaeEFKcM9ANaOB-D8D427xrh6e_l2NV3Ktq33-zbbdTa9Th7IdrOv_ZGCQ5Zt7nMaUywL9EHQMGTQlG-4z6rMgDsGqQwyGvMzjDhf1HRID0k0We0uxIejgpjQmyGHsodiId-n0YZ_eGJa2Hfvt6RwiVViDdy24NpBH-f4C0M4XgnlEsvnpLsrOlIyqlwlCnHCNkhGzbrQoWCHOqJ4819RJxmMBXN8QkfRwBJkEYhdpG5IV52Jig0-n10-0wTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c974ddb250.mp4?token=TFhy9285heot1sNj8BKxWOSOW4KZDKBxmWrHNqcH57I9wCKQY4-eXXZB2BQQtXtwsJfLuib1Kt3v-UxN3dyVnTwp2dyaeEFKcM9ANaOB-D8D427xrh6e_l2NV3Ktq33-zbbdTa9Th7IdrOv_ZGCQ5Zt7nMaUywL9EHQMGTQlG-4z6rMgDsGqQwyGvMzjDhf1HRID0k0We0uxIejgpjQmyGHsodiId-n0YZ_eGJa2Hfvt6RwiVViDdy24NpBH-f4C0M4XgnlEsvnpLsrOlIyqlwlCnHCNkhGzbrQoWCHOqJ4819RJxmMBXN8QkfRwBJkEYhdpG5IV52Jig0-n10-0wTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هیجان فوتبال رو با لیگ ایرانسل چند برابر کن و با پیش‌بینی نتایج، امتیازت رو ببر بالا!
✨
🎁
هرچی پیش‌بینیت دقیق‌تر باشه، شانست برای بردن جوایز جذاب مثل موتور، اسکوتر، پلی‌استیشن ۵ و... بیشتر میشه.
همین الان به سوپراپلیکیشن ایرانسل‌من سر بزن و اولین پیش‌بینیت رو ثبت کن:
ثبت پیش‌بینی</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/105021" target="_blank">📅 19:05 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105020">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/105020" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/105020" target="_blank">📅 19:05 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105019">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VkGSo10JRsbraAPNxh8x6wF0IWG_WzuwpdOvxW0IVIeyxy17-VaSAcLgVyz07nOFlIbyTktn8KH9TpI7dqqclGlwXPtRc7GOJsPPFHumVFk1QNBdS5tEUQ2Fcn7R1Ez4hlc_D0ynSU8vM5UM0g89daWY3mQfMsJXgg3EsgC8u9wBL28yw_z8SIwoztfTKBz8qQ7-Z28flXMIW5A9m8D0SNAzUohvYoXvRVKaMgMWfIuommx_IhinCdMl7867Vj5DbVg6r5c1hSGqevqPR_hhvCWtbxk6oyGtSgzzqWUF2YnMK_ZPgJkJOKpYvIkyq_FqgB-UOHhU9DSehitDHG-JVA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/105019" target="_blank">📅 19:05 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105018">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Foizx_uz21xjiEbpFvqJCm5mO8J1IVpvFkJ9NE4JkUAqxWAuONzUnztkrQ9SOCK87KRCXQchlHVxAw4mqLz4DDD1CHP5dcTJokv7y03b5bWlIpvi6BsavCMeQkR5CAfUfyfRfIISMvhoPzLwobzW77lyRxrh3pmVXTB9foI5ZJmw-c23lpv3MTBr1Itezzx4i85nSl-PmLG_OWidgPfv4QcyFXeaEPIsCskgpzXEmjLyUjyiLqM7oXclYyYmgIgT6fauHZ6NL563GP0jCeNdX4asaSw9HvES0krJnoodePco3gCIOMbxfgE7aHAUcJbfpMWRuEuahOiMEQURS3CVsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇮🇷
ترکیب پرسپولیس مقابل ملوان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/105018" target="_blank">📅 18:19 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105017">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DoiKPn3e9CJhMzdsewLwQOtPtFGYU2P25nStfrN4cvKGb8-QPMiFmEkEfzxe_nfuw5uVpd2DRmt3gAALTU80mDqtmLBbItP6TBfIF1zchzBfhPvidBqH0lrntITnkmgShuCs_z8AocrPMbmeykUymhUlsb7fy81b9MO_YK440ABuOdZKfS3pKcLk2rZzuJvMumEPvyBJF_x5dUGzxEsorV7dFvk3RNwTOYM-Dk_13MZNxaOn7MrO75XGhJP3gtnik6uc3v2CRqNigLdYcglCvI7Lrzhrhbfzdyp5ADIjoa9C9J-z6_INhL6qCH-2QIynB2FSoxLhXu-qc1d2EdtutA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇮🇷
ترکیب پرسپولیس مقابل ملوان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/105017" target="_blank">📅 18:17 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105016">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
🚨
🚨
‼️
🇮🇷
هوادار پرسپولیس: یک مربی مثل گل محمدی می خواهیم، نه تارتار ترسو!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/105016" target="_blank">📅 18:06 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105015">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6f2734cd0.mp4?token=iIzRzzXuCgRKXM5gDm15n8i6LJlUut-YngDs5dTs09vUKjIk-WxtHGcOhFtZdc7RI6JzgA8bNlP8W4ShenoSCfh327-_S01IJXNTzsujjtA4OY_seq9HwWmLxYRuc5czOJDIqRRRgufeZhPNFXWHhaltAXlQ0paSB_wXcIXk2tCinROJvblMLsMWcP0S0jUr1wwjKQRF6I8Xotx7E3j6WxrIHEg3pY_wDBuTDnW0SMGVsaiqfNwwxXDTYGiVeihaXc07UKXkXRwiDwVRqblNg-Du-76QCmy1DyZ97aL-7UgCPpkKplZsMexjFDCcR7SaQ3viui-3MU-_5gGPjBJROA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6f2734cd0.mp4?token=iIzRzzXuCgRKXM5gDm15n8i6LJlUut-YngDs5dTs09vUKjIk-WxtHGcOhFtZdc7RI6JzgA8bNlP8W4ShenoSCfh327-_S01IJXNTzsujjtA4OY_seq9HwWmLxYRuc5czOJDIqRRRgufeZhPNFXWHhaltAXlQ0paSB_wXcIXk2tCinROJvblMLsMWcP0S0jUr1wwjKQRF6I8Xotx7E3j6WxrIHEg3pY_wDBuTDnW0SMGVsaiqfNwwxXDTYGiVeihaXc07UKXkXRwiDwVRqblNg-Du-76QCmy1DyZ97aL-7UgCPpkKplZsMexjFDCcR7SaQ3viui-3MU-_5gGPjBJROA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
‼️
🇮🇷
تهدید مهدی‌تارتار توسط گروهی از هواداران پرسپولیس: دربی آخرین فرصت شماست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/105015" target="_blank">📅 17:53 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105014">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f68436a0cf.mp4?token=W8nczKUPta0AeauYQc-MLsNmLbR2w-3NNEE0cMe_HYvfCsv1QWIM7ZZngbHtEeqtC2IGd--Vz1zLfydOesu1-ShokFPSxJIGZPTDPGbuSWPw495gZutVoebU9v5d49LTUDV0HPKk9E4yyk-Ut-xV1wsqiu9ga0yTPGAO2VZP3T5C_WwTPgaW0_f02sJJwNflokhBykeNG2svYB-KCtumOi3HycreP6XObqODxlo56KfB9l7EKNhhCVTItuxAAaCvI7TiboPhMeEyFWw8wPSx5JvhmM-F87ab6y6CKi7PqDs_lc6y1XvMpjjZWchcihvDGONmxfjaY1DICGMb6jtgwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f68436a0cf.mp4?token=W8nczKUPta0AeauYQc-MLsNmLbR2w-3NNEE0cMe_HYvfCsv1QWIM7ZZngbHtEeqtC2IGd--Vz1zLfydOesu1-ShokFPSxJIGZPTDPGbuSWPw495gZutVoebU9v5d49LTUDV0HPKk9E4yyk-Ut-xV1wsqiu9ga0yTPGAO2VZP3T5C_WwTPgaW0_f02sJJwNflokhBykeNG2svYB-KCtumOi3HycreP6XObqODxlo56KfB9l7EKNhhCVTItuxAAaCvI7TiboPhMeEyFWw8wPSx5JvhmM-F87ab6y6CKi7PqDs_lc6y1XvMpjjZWchcihvDGONmxfjaY1DICGMb6jtgwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
‼️
ریدممممم حاجی اینجارو
😆
😆
😆
🇮🇷
نحوه ورود هوادار پرسپولیس به ورزشگاه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/105014" target="_blank">📅 17:50 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105013">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/beb84b277b.mp4?token=C9dWpxYuThz2weth7FyX5CJXYdYrCgorv7lmwO6R8dqwzc_8xGjkyMmXHX2VwSOlgb9WJ40OmsZp8hLsJov6L73thRtD43ZQoi6iBo8xAPmJv8UXbDJ4aBvruPzIXynhEivs54aali-Ch_wHwxNg-GGHu3yAlThYAhqSSt85m7IHqPEHlPrV81vW_F--OEirI31-DJJvLaSdYPXEa5ByO2ZXhTv13PEp4XSvAuSqeXBwuECOvs7lNIExJ-IQiQR-dK9r7o_ow9mwcPxzR9MqAzddIt8Ndm41Worv_5OBe6ENr-t0947km78vIqcOpG3egVNwDxdWc0O6g5w1psFjsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/beb84b277b.mp4?token=C9dWpxYuThz2weth7FyX5CJXYdYrCgorv7lmwO6R8dqwzc_8xGjkyMmXHX2VwSOlgb9WJ40OmsZp8hLsJov6L73thRtD43ZQoi6iBo8xAPmJv8UXbDJ4aBvruPzIXynhEivs54aali-Ch_wHwxNg-GGHu3yAlThYAhqSSt85m7IHqPEHlPrV81vW_F--OEirI31-DJJvLaSdYPXEa5ByO2ZXhTv13PEp4XSvAuSqeXBwuECOvs7lNIExJ-IQiQR-dK9r7o_ow9mwcPxzR9MqAzddIt8Ndm41Worv_5OBe6ENr-t0947km78vIqcOpG3egVNwDxdWc0O6g5w1psFjsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
‼️
ریدممممم حاجی اینجارو
😆
😆
😆
🇮🇷
نحوه ورود هوادار پرسپولیس به ورزشگاه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/105013" target="_blank">📅 17:41 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105012">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0d80d5d54.mp4?token=Fm9sbtaPRjWX0SkxJTyccq-PAxDFg2zFk1PlbePxo6s6e1drgt7YaZamZ0pAOSMyrqG9uBefcA1uiQr9jLLj3miXUhcPgt9IiOkn6tzqM9JvHwCaoKcqPYAw3OdMttosvOvGyraZNLiMsrMBrErnJgJwtPxaieexhwsDqBQ4ICYe-aLlFRYAIX7Lyxh2OaZxvXyMRiph3Nslm4yrkLibexWh47YnLkZsYwoZrZx7rNTMK_joJOtqVOY50t14F7znEJGRp3AujOaUR2u_LKGewUL98lM8gUsPvm00L43DafbVZbO4J3EyxVQerOD-82WU7FpySIf7XQrZ4bmftjXsQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0d80d5d54.mp4?token=Fm9sbtaPRjWX0SkxJTyccq-PAxDFg2zFk1PlbePxo6s6e1drgt7YaZamZ0pAOSMyrqG9uBefcA1uiQr9jLLj3miXUhcPgt9IiOkn6tzqM9JvHwCaoKcqPYAw3OdMttosvOvGyraZNLiMsrMBrErnJgJwtPxaieexhwsDqBQ4ICYe-aLlFRYAIX7Lyxh2OaZxvXyMRiph3Nslm4yrkLibexWh47YnLkZsYwoZrZx7rNTMK_joJOtqVOY50t14F7znEJGRp3AujOaUR2u_LKGewUL98lM8gUsPvm00L43DafbVZbO4J3EyxVQerOD-82WU7FpySIf7XQrZ4bmftjXsQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😐
🔥
👀
پشماتون از ایونت تنیس تهران بریزه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/105012" target="_blank">📅 17:20 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105011">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZY6KiJli8roiA_izAZPOhr7Xgjl7SC7GTfX2S0HZRHzIwo7bHfLbQcdtrWJmvHaKB9pxOP4Qf3dpLoQyV79REIPaF7VW16Q0H34TTZolEObE6cuZ69z9Pdqwq_Pn7SfqkPbC0keA7p-eIv2TH3luE1bcdkSybegWimxyDNm80kojiQtK4O0j8UNVebs4msb7x7E-8KqVroz-BA_OIiPLvRhKoZGZi-4KdeRVw3-7SvDuYWuBnlO4s4xOO59QRBNF71Yw7phfioFzGWItXf7qsB-Bp60W8wpWxhfnyrXU3popN_KvwS5f_tNQKSozY5ye4zU5mj9fPucIMy1e1rbw5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🗞
🇪🇸
رومانو: سرخیو مارتینز هافبک ۱۹ ساله از رسینگ سانتاندر به رئال‌مادرید؛ HERE WE GO
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/105011" target="_blank">📅 17:09 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105010">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n03e6oHP-vXGyidJV-Ikk70AfsOzE7apB7c0iR9We2JEcjpk8FhIabi65aIvJqM6x-wWKLskVcgG3YBd1nAWbhGO--uxUAOoA7d0iPLK9beyGN8yE9a0QQXwfxbMFj-3nj7MsYo-l2QEAfjLkxFHK7clzJDVE3HRFlTA5CBSjcpjWCSbnKNvAh2m9n-P6xt0U1N61LC-eeWxhwkti00eRm-kmWNnC-zuHoOwafNNgZPt4ImplHg6smm_N2EoFWB17gOl73iZwqrqYvOOkQ325MITBu-9IoB7AEDAcbQWmzpssJr6xfuxWgvW3ZR9GwatdC1usN_8bQBPnS_ntDKbqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
هفته‌دوم لیگ‌برتر انگلیس؛ لک‌لک‌ها در قواره یک مدعی نشان نمی‌دهند! شاگردان ایرائولا به دومین تساوی خود دست یافتند!
🏴󠁧󠁢󠁥󠁮󠁧󠁿
لیورپول
😀
-
😀
ناتینگهام فارست
🏴󠁧󠁢󠁥󠁮󠁧󠁿
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/105010" target="_blank">📅 17:07 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105009">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZqdsfDXmmfJQcWVHRaQBgbFc4YzZ6MYqBM1wae8ZzKcFmI24PPooKhfmMIcpvxfp4sar_nSpa0KuMzoMxIFhZ6DsRFJJmZdKKnMtr0lDuvPX6rGbhLW55xkwGhcqLK9nZNgn8D12Q7CORv30DdM2A8PL7NHzy2NFVFPe387GGdjjunD_NEzzXuLZQYBkSfyjAB7ZXpA-nqC8JmGVColN7inc6xfVUnHLejJ0PWAgg7zUhOon5q5boZHRz_k21BlJDn3oyl3KUFz6J3kytoASluMKr4i4vGvKSkfgRdYjWpscIqPF_8mp_bN-zoq3KoPUvxECmLFSFzoULn3lVE6tZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
هفته‌دوم پریمیرلیگ؛ ترکیب لیورپول مقابل ناتینگهام؛ ساعت ۱۵ شبکه‌ورزش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/105009" target="_blank">📅 16:58 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105007">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C6l4vEbXLx0o-ThELuOoz8SPakjXCIc8pLgyd5UBX5YkILKoNrpFBP4Rvj-6Uk88A_eq8xMdBOw8-2G1Cq0l3U19MEFe0O3WVIBbMjnf7jrA9AbYNua64vO5l_1o_IfIMmExfGrtZhhCyebeN4kGyyFxqyAPGLrRk3C1EpRWMjJsXa4CJFh59Xhv-w2_j7YAA1oswS_JE-gFD3vq-kN6mx5TUWeNWI4FOSZTridyIb_ao-RMPydywu67P_xqG2VAzx1llg8Hb0f15hWXNya6uLgYYxrLjfoL_M1mzP1VyUqaBEPTp0ssVFqbAt7ku8D-WvjuT_i3DSuEoWDIXzvJ5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/A-0CZZVh7VAeJ4uFJzDEo6o2o9_c6JvgXG5RbX1md3SeMHf0ZTV5eCQ1FQjbWmR2J83FUsBT9uuzYsykdaHNlRSm0fq4o732Yp4LmDUGd1Lz8YIHl9MkfzsOPZPeVNuA5ENNRCo87tiVtBhnJZ-mdeXs7oPaAOELW7m9bmKnDo5FYk7FPk1RGaq7Wa44Xx1MBdVduOGL6huXPG4Bn9oYhcTIhKxvXJQAlUnZ9TSjc6CYmT9X72EBY7EC1xP8RacNDzFIJz-dqtF6cpiK3FjSNWQLzp39g_Q4fyrs_bnJdo76qzgkoTo_5zlfW0ASpi5NbUzRRpRr6UO2Mz7dx9e4eA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🇪🇺
برنامه گروهی بازی‌های لیگ قهرمانان اروپا 2026/27 مشخص شد.
18:45 اروپا = 20:15 ایران
21:00 اروپا = 22:30 ایران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/105007" target="_blank">📅 16:56 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105006">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1e0ed52814.mp4?token=VDW3fzUdeX_hyn9OTNaQs9cEqAYRnVyIsAI1POTeWySzkwKJan-yCLvCZG7pr5vx0XHFSWc2UkwDGYbp2uKGggoySaf4_7AjWx7UbIpjBBF3rQrpznkU732Nkry808N708ywJy_zI4U4P2gyLcVdJYqMYLhsIRmJsjsAVOsK2DVC01AbNfrfY-5u8557jmfz36JCJAVUPr4PrqXDoyxPaWmUjUD84_eTh4_SRSKJcf6vWYlkzilUM0lk2-fB18S5LIHlt3IQlwF3U-z4v5swHoSgFMn2fwl9yEL8ZT6usNmrz2oBgZhMZgeazKAQcZXQWYx0DiGBwdRjbt3upQxbYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1e0ed52814.mp4?token=VDW3fzUdeX_hyn9OTNaQs9cEqAYRnVyIsAI1POTeWySzkwKJan-yCLvCZG7pr5vx0XHFSWc2UkwDGYbp2uKGggoySaf4_7AjWx7UbIpjBBF3rQrpznkU732Nkry808N708ywJy_zI4U4P2gyLcVdJYqMYLhsIRmJsjsAVOsK2DVC01AbNfrfY-5u8557jmfz36JCJAVUPr4PrqXDoyxPaWmUjUD84_eTh4_SRSKJcf6vWYlkzilUM0lk2-fB18S5LIHlt3IQlwF3U-z4v5swHoSgFMn2fwl9yEL8ZT6usNmrz2oBgZhMZgeazKAQcZXQWYx0DiGBwdRjbt3upQxbYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هانسی فلیک: ژاوی اسپارت شگفت‌زده‌ام کرده و برام سخته که بگم کی قراره توی دفاع چپ بازی کنه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/105006" target="_blank">📅 16:55 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105005">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QL0MEPlHfWsvkJ0QZOIMrNORQynzLtTNpVzwuWakSHkCAiy9yFfBpoozYoIvHwWJwx6u0FapkHkJoJNetbgzADDeeSj7i9cIr46yYpGSKXiE3ZKRVihFgAcwfR1KGnWm97Qd-Wc5CGziNNEwK3g9w9fqQE9_H9jw4O-7a5IArYynRPdyvtP5qozNQDSkz7nC7ZT5wvXtK0FejwRmwdq8mZhkHFtb6puDn0RoO2cK1_A2OejyIgN6IBmlXfesYTyGmNeAUr9mNMMky7ucadaJ1IkvpNIX9MQPSaKgJWTOtY3ID4t5PRstkjQefzSv1MHztc0c50uRBq9-o4AjCq3qTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
مقایسه بازی‌های بارسلونا و‌ رئال در اروپا؛ با ریکشن نشون بدید کدوم سخت‌تره!
🔥
بارسلونا             رئال‌مادرید
👍
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/105005" target="_blank">📅 16:33 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105004">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/609a9de2f6.mp4?token=GswB24B5-1aG4GjuEQE3DORalWJD0oB5GkEBd_Al2g9aO2Qx_e-1_K6pJJ-pJRlqr-q-0UMvZELDMCY_nNJnoHjcDhujRaS4HJBysRuDcbDh9H46fyXYbub78bxRmJz9zEHv9GAgtzs3syveglvSPFJ-wWzsbtKzBiOo854bm6rCuVRXrGZN_6nN2FnhQFPrgTWaaUwS9hTYqj14q2MGcBNGJpNjmL_1uWzOsm2gPdSb5CsBz3Hc8veaFlfNgM3bmdrsMnGZfnIvZHDESGWFu5qmLFY5chxoNRcjDzdENN9NTFyLtR-8Q2zMoRIcqAtU5JUJYb26eBiLzFNx5JZCBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/609a9de2f6.mp4?token=GswB24B5-1aG4GjuEQE3DORalWJD0oB5GkEBd_Al2g9aO2Qx_e-1_K6pJJ-pJRlqr-q-0UMvZELDMCY_nNJnoHjcDhujRaS4HJBysRuDcbDh9H46fyXYbub78bxRmJz9zEHv9GAgtzs3syveglvSPFJ-wWzsbtKzBiOo854bm6rCuVRXrGZN_6nN2FnhQFPrgTWaaUwS9hTYqj14q2MGcBNGJpNjmL_1uWzOsm2gPdSb5CsBz3Hc8veaFlfNgM3bmdrsMnGZfnIvZHDESGWFu5qmLFY5chxoNRcjDzdENN9NTFyLtR-8Q2zMoRIcqAtU5JUJYb26eBiLzFNx5JZCBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🥶
برخی از نجات دروازه‌های فوق‌العاده بازیکنان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/105004" target="_blank">📅 16:05 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105003">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5be1dc5a15.mp4?token=kr_CESkS2poO6tqgDsrpc7E3ZbYOL5_vK_vMDhCmNwjjHu742i9WPndcoman_dWsloWpo8pU2hq_dsFQ-gM9CdoRcJvfwtpS5tnTJR1fk96k0Ij6GPmup95lsXcjEQINYycsCPAztpn03DcWMUNrHiq3wygHvKnPztiJYMDTb2GE1ZjEG21zGntAFgXCZQwFqXcagMCpr5BjJtn6g9ZB-ea3oel-OpNnbInGu4SIkgIomiK9eaUjxppp4Ni2Ycp5ndpEmjUqhn71022PzBIZlKlqHMUoqCUDGwdrNHyvuhHHozw53qAQKhziK9CN0sp8-CTGdPTgIzpnP1jcwngeGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5be1dc5a15.mp4?token=kr_CESkS2poO6tqgDsrpc7E3ZbYOL5_vK_vMDhCmNwjjHu742i9WPndcoman_dWsloWpo8pU2hq_dsFQ-gM9CdoRcJvfwtpS5tnTJR1fk96k0Ij6GPmup95lsXcjEQINYycsCPAztpn03DcWMUNrHiq3wygHvKnPztiJYMDTb2GE1ZjEG21zGntAFgXCZQwFqXcagMCpr5BjJtn6g9ZB-ea3oel-OpNnbInGu4SIkgIomiK9eaUjxppp4Ni2Ycp5ndpEmjUqhn71022PzBIZlKlqHMUoqCUDGwdrNHyvuhHHozw53qAQKhziK9CN0sp8-CTGdPTgIzpnP1jcwngeGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🎙
پشت پرده خداحافظی خیابانی با صداوسیما
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/105003" target="_blank">📅 15:40 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105002">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/96846109dc.mp4?token=ML8QiXingsvNZU6Hxxo3arRVZ_X930_7h_FJ6tuKVcs9FYgtHrYbDEzUKJ8RSzO3zBlIn_n4evNccp8IOmwDhYtsdqm47jCakqIESr9fRO0j9w2NuDOz1hnyfofnakMi8qMLrz9SThjMhyymj2GW9cLWIzG6Qv3bPABpQrru1KTsHmS557G92dPHDr3CSjoDSE1LyY3i8e-h5PNgtMFb-kFFnigANaiQOIifdFN_JOFfl74-r8hCrrrMkEjUqTGZf-MdwL0YwareHg1cPX6hcN79w694KHwUvOVVn_2xjF7jtJ2upOvqhHbFb7mYgEpPQkY5idoK0oOmoAWduh89Pg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/96846109dc.mp4?token=ML8QiXingsvNZU6Hxxo3arRVZ_X930_7h_FJ6tuKVcs9FYgtHrYbDEzUKJ8RSzO3zBlIn_n4evNccp8IOmwDhYtsdqm47jCakqIESr9fRO0j9w2NuDOz1hnyfofnakMi8qMLrz9SThjMhyymj2GW9cLWIzG6Qv3bPABpQrru1KTsHmS557G92dPHDr3CSjoDSE1LyY3i8e-h5PNgtMFb-kFFnigANaiQOIifdFN_JOFfl74-r8hCrrrMkEjUqTGZf-MdwL0YwareHg1cPX6hcN79w694KHwUvOVVn_2xjF7jtJ2upOvqhHbFb7mYgEpPQkY5idoK0oOmoAWduh89Pg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
✅
مرد سه‌هزار چهره با حضور مهران مدیری از روز جمعه ۱۳ شهریور هر هفته پخش میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/105002" target="_blank">📅 15:15 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105001">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/568c088f46.mp4?token=C2fgmR8PvLfT9WCLECDxG4yLWkGMVr5whvHwgvRACjX3VWhvGxX2hKwVt7RnDKojKxcroyZIOBNpGakxd9oR1xgYgD0wGIRLgjRqGReWgtdacNbU2JrBJtNF3ds0eCj3RnUf1K0dEzGAxuUSzqwq8TUeRIIOdxWGCFbV6hna7Cz51NP5Y6410EICthorEW1IEUyo2wluDnPrEInjGK2hkGBdXO6Q7wAuCuns_dyOmcdeJC1LwPVIvw3ofoh7rr-34WTuCWLsCzgxYzHBqj_lYVFM-cpO9dvDfon2iOznZWunPdOyTVSfg-JJUkF6SITd3potChOkLWJ6rup_SE3hNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/568c088f46.mp4?token=C2fgmR8PvLfT9WCLECDxG4yLWkGMVr5whvHwgvRACjX3VWhvGxX2hKwVt7RnDKojKxcroyZIOBNpGakxd9oR1xgYgD0wGIRLgjRqGReWgtdacNbU2JrBJtNF3ds0eCj3RnUf1K0dEzGAxuUSzqwq8TUeRIIOdxWGCFbV6hna7Cz51NP5Y6410EICthorEW1IEUyo2wluDnPrEInjGK2hkGBdXO6Q7wAuCuns_dyOmcdeJC1LwPVIvw3ofoh7rr-34WTuCWLsCzgxYzHBqj_lYVFM-cpO9dvDfon2iOznZWunPdOyTVSfg-JJUkF6SITd3potChOkLWJ6rup_SE3hNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😢
وضعیت شیاطین‌سرخ بعد قرعه‌کشی لیگ‌قهرمانان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/105001" target="_blank">📅 14:50 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105000">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5e4faa301.mp4?token=AnP0r_Ty4UwxrLmWt71Hido_btCaLzNxIPsTEjcuYugx-KB3vOkeFKhrlnhKMGjWiGc6My4Hy2xXtL7Af2axlF9eLfbICurvjgsINQVIINVqV65viKjA8JD6wwGjguPAYw_4ufAKNFERI9V9QMGADpFLRQE8oEyM0NqaO1InqeMQF4Q2FAIl2-i29D876Gn3VninseFkoqVKd8thx5ZoX4D3M-7eFsvpoQKY_Yd_vYyWJiWbUaqCcSxM_bvj5F2JGoIS5dvfoT6stRL64Cmr01KIoJ3Ay_994pdk-xq5OiqYdKhJjtz0rGt6TGLMhScIqc12aQxzowhwHJunmg1WTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5e4faa301.mp4?token=AnP0r_Ty4UwxrLmWt71Hido_btCaLzNxIPsTEjcuYugx-KB3vOkeFKhrlnhKMGjWiGc6My4Hy2xXtL7Af2axlF9eLfbICurvjgsINQVIINVqV65viKjA8JD6wwGjguPAYw_4ufAKNFERI9V9QMGADpFLRQE8oEyM0NqaO1InqeMQF4Q2FAIl2-i29D876Gn3VninseFkoqVKd8thx5ZoX4D3M-7eFsvpoQKY_Yd_vYyWJiWbUaqCcSxM_bvj5F2JGoIS5dvfoT6stRL64Cmr01KIoJ3Ay_994pdk-xq5OiqYdKhJjtz0rGt6TGLMhScIqc12aQxzowhwHJunmg1WTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤯
🤯
🤯
یه‌سوپرگل در محلات برزیل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/105000" target="_blank">📅 14:25 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104999">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JcHc7-d5qkFcukGflfSPaF52eYSd4HgiAM8jjB0ZU15yETxew_U67TmU18tJecDjR6dnAg3BaySW4FbkO7pHXvPZs9k2ITv_e_zcf38UxE13MSP9dn9FbUpsZZ8zsfnrSkCVxT9DQPhOVyxhrfPLajKXN8KPfQ8knhgyXacm4W9N6Bo-Vh2QAMGly9gt5dJrrV8xw7yVCQSO9H9SWRHOkw6SsgkXUSvmal7IPjmMGbPLaY-usTY6s5Sg-geRoJmeCnnYCfGh9dDNY-E2xX5gV1JOE6dP6eUu42tlIEWJqpoP2JjM3Y5XKlfhuXrHT3thF7KM9gkPie0TZ1-BgziZNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🇪🇸
پردرآمدترین بازیکنان لالیگا در فصل 2026/27
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/104999" target="_blank">📅 14:00 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104998">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n3cUxEWbLrM6lgUejQU6UH3wA3UNOi_TVUWKXE4ldfwk5iWWK1OsALw1uAfcMYE3TYRbvMd5oB0X9XvJMX7DUzTXT7VEn0v0OSzBe312OajiD3ZAhEC3TPUZLEc-6m93RLsfFwkU10G_79r0_SXRW8zv7m0Ls-DI9AbMFB0r8R2BLYn8DFnQZldHzzDNB6_DjGHHteSoMzRNBhqcmj8yEJ3aA0_NnNJEr9E5HB_OqtcpNEvLDIz2ii4AtTGTaL5qxEeroJ_ne887Xcq6T6rcRkOx5WhJa2SZGZuYd3FhwR0upvZPZYMP04hEmipCLURadxEUwrsUqdY1zscgomZGbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
هفته‌دوم پریمیرلیگ؛ ترکیب لیورپول مقابل ناتینگهام؛ ساعت ۱۵ شبکه‌ورزش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/104998" target="_blank">📅 13:50 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104997">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rgFg8V4TQZ-3SNfinZKCNtG12CwrTtG5En5s4_xmeqEsxCvAtNFkuwF7PEmy2kJjnMu9LRy_WKJbrbsRKjOJPHbxOoY_TQa8qLzIMfSb6rE5vCbZiULwZu9hFhUQxpVR_qufJls6OGr8f0kE9UfxlcEtO1-ZoKCdUxWJyIyefNLxsZbXZx8KzmQA58SxK3Fh_An4iMf7cRCjjmbTTrbnboZg8-0xQc6Q5p06Nji6EEFzgNHzh60_DvPtGLhkxOyNgsh5mq4vuNDq1c3A1Gep8oeehG8Sf8rPNvutow8gXNlp72jXtwkw8m3jD67W3JWzYOTKvudg5_H20H5iVb4YUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
رشد قدی لامین‌یامال طی ۳ سال در بارسلونا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/104997" target="_blank">📅 13:35 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104996">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g83L3ohmpRGIR0xItIr9KJKtLwdUIeqhsQGTQphzH0_Z2GVbR9JpPZE5JRFbxGnkibT7Iv7vv7B40Hfnu9U3hyFCZ-izHnanN0haCEQK4Y4pG2edePArZ1yvHyTyLkWlDn_r1C93-6YNaL3FSla7WSAqJPRVmKWcboN1OGUV_HLZpBOnjixrLdkvAJDuIM_RtoNsiuiA0A7vuA-YI_Z6HNM4O6KT3bEtb6pf8xvygEbl72up7ZH9BcN9y-qGuUQRSdZ8aJMRPqdlK_r_rgZO900Vk_Asag1fQTtY6q0ocxpjYmH1_sqFa2pb8FzXE-68WJlj8B7tB4lKWNHio6YUdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇮🇷
🇮🇷
ابوالفضل رزاق‌پور مدافع چپ‌فولاد:
🔻
پرسپولیس میخواست برای جذب من رقم ۱۲۰ میلیارد به فولاد پرداخت کنه اما در نهایت این اتفاق رخ نداد و خوشحالم که در اهواز موندگار شدم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/104996" target="_blank">📅 13:10 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104995">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1d94427ed.mp4?token=TBmBhQ1WwKGtBLXQLcRbKUIC9uz-KHfxRZb08691Jpq9ELnnw5KnxVgm2TUOeuzrfnUVQkbYXif77YtJIcn6sQq-dnM1dAjTZq77Pz_yaH1F1d9ulRTJOa0QTueX07LeOTLRSh0Or6zAEmU9qwyNrdek9OoYJyp2hO6OB3QibQsSQAfHw3ck14lGaTZCSVT3MxVnGrzdl-qD0dduiukk-3iMKtLSZkVCQBufJNxkjzSOYl3IRCNnUXgmwSXxzAKRT5Fki7JijZu4Ix8yB4gGkBBOcHbnXAr24bSBQ_BRKr3hcvSy9-xQPk3R0EkIlinFnTDNUJUtP-J4KrHE67ZnMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1d94427ed.mp4?token=TBmBhQ1WwKGtBLXQLcRbKUIC9uz-KHfxRZb08691Jpq9ELnnw5KnxVgm2TUOeuzrfnUVQkbYXif77YtJIcn6sQq-dnM1dAjTZq77Pz_yaH1F1d9ulRTJOa0QTueX07LeOTLRSh0Or6zAEmU9qwyNrdek9OoYJyp2hO6OB3QibQsSQAfHw3ck14lGaTZCSVT3MxVnGrzdl-qD0dduiukk-3iMKtLSZkVCQBufJNxkjzSOYl3IRCNnUXgmwSXxzAKRT5Fki7JijZu4Ix8yB4gGkBBOcHbnXAr24bSBQ_BRKr3hcvSy9-xQPk3R0EkIlinFnTDNUJUtP-J4KrHE67ZnMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شاهکار آلوارو موراتا در مراسم معارفه به عنوان بازیکن جدید تیم‌فوتبال لگانس
😂
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/104995" target="_blank">📅 12:51 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104994">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ic2egGFFlto7awfbBkD2hhHZRL69FgiSXgTXNg7rFsz6zPBGgjuaTnV2yHYdYBPtWMwnndcUdanFlf4oH7fuD_chVJV7JWu9EUcQAErhUpMbwftXN3e6y6d_8iXdRDwpgqYHbktkHJv0CCM9p-NdGoOwxSzcD1cwVziPOjxoRfIHLjSA_4mub6PIblDIh4mr81dpKxnwzUXmneePasPFwc_TW1y2Xokz12kzK0RGmTE7tJQF51IzhJCOuiDtkEgcEIbOsawszRVbAJt2gPlDZKls7PwtXozBH4zv7MuP1Lf21mCxTyfvtgSGefQU-bSGxJOsVk8GQ7fmet7nzBUeGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
🇪🇸
🇪🇸
خولیان آلوارز از لیست اتلتیکومادرید برای بازی امشب مقابل سویا خط خورد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/104994" target="_blank">📅 12:45 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104993">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/694fb72f97.mp4?token=GRlOqRxTVuAVN8h2xUG1Yc4o8BMQ5s3SpxQZvWKGFPxKYT0E-lvY95gG7JOuICIeIMVKAbCr92OHJPPAPPTsZwB2Ebev8K4TVL_HoDMZufzSbdmqqSi1PuOfgaLX_b3Zq3i2TUhw-AeQ4Kz7f0N83n5JjsD6Aom026omS2KgFFGgtTdMTiBcYd09JgM-Igk_0EFdzXFPcJni73KW1P-5PPPGspLKPfWRYElM5daLi7VlH7DWj8oAAIXQSgA1iQawtOc9aksqUAsFo3uq8a5f4H-YOmEpwuL_PgEsdNJ35hvx88IWaPPKovlTp5d4sZJ7EVKLFrOn36_y7ubmJfbsPYi4F4CSSMVxqWrh0E7lbgtfdi6KXC_7sLMj1WOpTW9tBzvCQP_ZT5WjNdbp253AbvSk4CR_Ig8YbBYYQ0WZu3B1R0Rnr1_lUA5c0mDc8MBV3OA_JhLL6utRRyvHgtROilq0nNk9PjHJ0SZQV-Ty-xNS3fL6sPdxc1mO987piL2vj9U6zEEga4AYDda74erA5fey9pDAU6TOGBJGe3b4W9J6ukl90HlXixT1oA_QQ7zco8bTnIVl7BosRWcKcNpk2_9KpiM2cvVesdjT0uqO6zKC2U1kXF_3S0EJxGfrtgWRbI-XVbHPxzsqmgWW6q5OU3mVbczIoegsI5w9NSHezZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/694fb72f97.mp4?token=GRlOqRxTVuAVN8h2xUG1Yc4o8BMQ5s3SpxQZvWKGFPxKYT0E-lvY95gG7JOuICIeIMVKAbCr92OHJPPAPPTsZwB2Ebev8K4TVL_HoDMZufzSbdmqqSi1PuOfgaLX_b3Zq3i2TUhw-AeQ4Kz7f0N83n5JjsD6Aom026omS2KgFFGgtTdMTiBcYd09JgM-Igk_0EFdzXFPcJni73KW1P-5PPPGspLKPfWRYElM5daLi7VlH7DWj8oAAIXQSgA1iQawtOc9aksqUAsFo3uq8a5f4H-YOmEpwuL_PgEsdNJ35hvx88IWaPPKovlTp5d4sZJ7EVKLFrOn36_y7ubmJfbsPYi4F4CSSMVxqWrh0E7lbgtfdi6KXC_7sLMj1WOpTW9tBzvCQP_ZT5WjNdbp253AbvSk4CR_Ig8YbBYYQ0WZu3B1R0Rnr1_lUA5c0mDc8MBV3OA_JhLL6utRRyvHgtROilq0nNk9PjHJ0SZQV-Ty-xNS3fL6sPdxc1mO987piL2vj9U6zEEga4AYDda74erA5fey9pDAU6TOGBJGe3b4W9J6ukl90HlXixT1oA_QQ7zco8bTnIVl7BosRWcKcNpk2_9KpiM2cvVesdjT0uqO6zKC2U1kXF_3S0EJxGfrtgWRbI-XVbHPxzsqmgWW6q5OU3mVbczIoegsI5w9NSHezZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
رامین‌رضاییان دیشب قصدی برای خوش‌وبش با نیمکت‌استقلال نداشت اما با توصیه ساسان‌انصاری به سمت نیمکت‌آبی‌ها رفت!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/104993" target="_blank">📅 12:20 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104990">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X-BvGa1LGjlHwlsPu0OPDwkr6RydwVMGAKJQL4keNT077Px8zCZUi3qOX1RcaRlHQakSRiL9pza5-tmevjbmAo3sYGSeBj376tQvqbh-qWgaMidBWVjwpjU1DsGIuWsIjcFX8OAHwAHqCd61YhXMPcaYmK5JxdYkpowJlkBo-nv6cBXRwirPJW5X9iRRxj9tBMvL6rIFNL9TW5QuMi9wYIn9X93QWObxzTMWw_EpdY4M4bAgavuHh73HHbGsb6EqBoG4VTDvqtT7lxEOnCXKkFJxIVmfygDPefoIWAI_wHyqDsDJ2zrqIdJnlmY8jFsD6A_o5-c5dzanqfmawrFIGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rl1b2JVPOhXOs9t46rPPkFfJ5Uz9AfJNf2K45cJSOR7ReBFcNtF4JGNPFZRQHzBQshEzglsjhwNA0OfNznxSD7Ex3tQMEM_CUSgud40X2xsm7-9rbvlFrHNkiQn-qY6sW-b3FjCTRPJzsClMT-LJG54YNlYhYCtHhjtY3jXTbAwHcRY0YcNUuzqoLDHH4_u9kVjXl9hagFJiYGDzsNoX3s54bcK6MZwsJC75B_nPE83k9pIXsL3Thk-Ol3kvc-Hnogr-tK0z1kRJdfH32XuVwPDmP30HYt6gOjtLcUu6KUVncptW2w0mn3Q3WuZpbm8bjkpkD6m_XpqvQoI-JqoAkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/s2Im6eyN3g0LhRv_UzyShrIs5NJp6zZAdEmkN6Q_wMFGQzPMrQ-1GdVKn7NGd2h44BouJG1amSewytdN8Ke7JMFAAy1CsEMMOFmN2BVcl_02PrXQbMYLGVAvbFmcfRsUceXxN1NS5Kr47SNsVUk9Do_eFW-Cen20fukOcHik1prr25FZhE4JVMmNXKSH9jYIg4QwpL-uyyhOPxySKYUPlplP9A-jHr_GmEumKZvJO-Ix5VsHYRVRyuZpuj4U3G3GYRcHRTUGbsxnSbzFMYZqgPl4ke8EkwlDXcZnNb-59bu8D69Jb49ZLACxRAPYJCQnHGE1fP3Ruf_miOdD4JuXtQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
گابریل آرتتا، پسر بزرگ میکل آرتتا، دارای یک ویژگی نادر به نام "هتروکرومیا" است، به این معنی که چشمان او دو رنگ متفاوت دارند.
❤️
💎
🤯
فقط حدود 0.1 تا 0.2 درصد از جمعیت جهان این عارضه نادر را دارند. یک گوهره‌ی واقعاً کمیاب!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/104990" target="_blank">📅 12:05 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104989">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/104989" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/104989" target="_blank">📅 12:05 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104988">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NoEVrKqJxKQmDC_FEEays5-FkEFAI0dB0cX6WdwrFblkLBLcxLg6UPxrRbaBwiT3n8FHdeE8-yMI_QuHRf2M_Pl65R2sK-jSsfyCPESel3c71aNwKwDQRAcrROl__Crqppkv3ciDBrTSjr6D_TGKfYBe2AZk54zFybuLpd-ckoAcLHrFZcq4by-DRDE0c2fzXCAgzMLswghQTe5aulpNlPod9ktiHl3yXwBjO3cnjfzX6sqSUQjguwlpvTYaewfMSwckbGjZhM-LRHQOxWVvR1mtXmPvJ2_MqL6aoFcqCR9baPmH0vaI280hMugMLdMkDYzMx1NXu-tyGCawVXEIxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
بازی جذاب
پرسپولیس
🆚
ملوان
را در سایت بین المللی
TrexBet
پیش‌بینی کنید.
🦖
دوشنبه ساعت ۱۹:۱۵
🦖
استادیوم شهر قدس
📊
نگاهی به آمار دو تیم در ۵ بازی اخیر:
ملوان: ۱ برد، ۲ تساوی، ۲ شکست در ۵ بازی
پرسپولیس: ۲ برد، ۳ شکست در ۵ بازی
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
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/104988" target="_blank">📅 12:05 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104984">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb4df35536.mp4?token=XCxqyyQWf34dDSdSUjBKkmrqGxfTDDALeH-BIkaDiGhyrMuksvT8GiPY-q3R_8CuFntbWMnwRrJ22J9UtDTdmnopNYKON1o5rkZwA2bLOO0i2pDZvq63z8piQ-4bEocL8xJ_NAzHTYnw7O0b_Pu_n0BTXYtAOre0qMw-Wzycd6JALZxeYPT2TsojoLgIMnaT3x-OvkJnwYGEOgNR9h_2rFsbgQYVSoye7U8qYZPXi9X8ESXLwbyZy2qr94GnzWR6X2cUCVrauQTb-klPdIwS3IZ0-IkxikxhRovVdDAgu3U_kqnLyEKgCqJFvT7E_q1FxS6C7MvnZno_U2uz_DgR9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb4df35536.mp4?token=XCxqyyQWf34dDSdSUjBKkmrqGxfTDDALeH-BIkaDiGhyrMuksvT8GiPY-q3R_8CuFntbWMnwRrJ22J9UtDTdmnopNYKON1o5rkZwA2bLOO0i2pDZvq63z8piQ-4bEocL8xJ_NAzHTYnw7O0b_Pu_n0BTXYtAOre0qMw-Wzycd6JALZxeYPT2TsojoLgIMnaT3x-OvkJnwYGEOgNR9h_2rFsbgQYVSoye7U8qYZPXi9X8ESXLwbyZy2qr94GnzWR6X2cUCVrauQTb-klPdIwS3IZ0-IkxikxhRovVdDAgu3U_kqnLyEKgCqJFvT7E_q1FxS6C7MvnZno_U2uz_DgR9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
🇮🇷
تعریف و تمجید حمید مطهری سرمربی فولاد: بازی هجومی استقلال باعث شد تیمم مجبور به دفاع کردن بشه چون تیمشون در حمله خیلی فعاله
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/104984" target="_blank">📅 11:53 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104983">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">📹
✔️
⏸
تحلیل داوری سه بازی مهم هفته چهارم لیگ‌برتر فوتبال با مارک کلاتنبرگ
🔸
چادرملو - تراکتور
🔸
(امیرحسین حسین‌زاده باید با کارت قرمز اخراج میشد. همچنین یک بازیکن دیگر گل‌گهر هم در ابتدای بازی باید کارت قرمز میگرفت)
🔸
سپاهان - گل‌گهر
🔸
🔸
فولاد - استقلال
🔸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/104983" target="_blank">📅 11:45 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104982">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UpAmV_qVW9o7HC3SJxyP24Mb1WKpD257VQbCg1-99HRLINEBdOrQkkxQBYnscHbBKEfO9E0-gaZsmdJHIS6Ahr_a-GiXIbMw5-KfOKsn-VSeanxNWU3bfL36ev8vIih5S7HdlwVW4DgbdC8p-rBnej4lE7PVL-L7K3y0Zn4AoDK0VcJX0XuXd_eTiXEvvySmnxpkEHGcfOc6vLFzfWHs8BNzFu7AzY14LlUa68ZPMdgpoN9nFHJ41FdXAPHpqJ1EmBXLd4pjJdHavMR3bWV63Mw3M0R43uZlBJU0CmKlYvJ4taCQE33YyYjh6Q0XJGi2xewlUvpHrQ9VhMBOr4buUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
✅
صالح‌حردانی و رستم آشورماتوف مشکلی برای همراهی استقلال برای دربی ندارند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/104982" target="_blank">📅 11:10 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104981">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f929791585.mp4?token=WviERGODUurK4LyTUElCpZ7Dec_hXOmO7NqYeryhbr0e5jB9TiiZo-qyWtwHs2zvNZEKDnz7zF21HGP2OVCYYWcBCAfWPA-ve_4rimGpwWa01JYWsSAPdjCL3FhwEF4b7dqZUfEVEqh_xiHFDzRdDo4SRRPzpqVkIfq6VvlWk0nWtDd0YVNL8xOIZ-SceJqHGVnWxZHq85jlVx4OSU5tv7WS39H5UMQw3NMa12Xf_suewWmr3ZQEAnSSEirlMV6F2kZ4TCJ_I1Nqr8rFN9H7r8z0cwiMY9uzKpxf2iJc1_hjYHiJaT1hC1YRWnxDmcgOrjb1cLp_QDJjXo2xSrkDYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f929791585.mp4?token=WviERGODUurK4LyTUElCpZ7Dec_hXOmO7NqYeryhbr0e5jB9TiiZo-qyWtwHs2zvNZEKDnz7zF21HGP2OVCYYWcBCAfWPA-ve_4rimGpwWa01JYWsSAPdjCL3FhwEF4b7dqZUfEVEqh_xiHFDzRdDo4SRRPzpqVkIfq6VvlWk0nWtDd0YVNL8xOIZ-SceJqHGVnWxZHq85jlVx4OSU5tv7WS39H5UMQw3NMa12Xf_suewWmr3ZQEAnSSEirlMV6F2kZ4TCJ_I1Nqr8rFN9H7r8z0cwiMY9uzKpxf2iJc1_hjYHiJaT1hC1YRWnxDmcgOrjb1cLp_QDJjXo2xSrkDYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این شاید تمیزترین و بی‌نقص‌ترین اجرای کل مسابقات جهانی ربات‌های انسان‌نمای چین در بخش هنرهای رزمی باشه، آنها آمده اند که بمانند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/104981" target="_blank">📅 11:05 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104980">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f8294617ce.mp4?token=kw7DSMTgt7CmFTHEc4RnHhrfbP_NwfibnWtlYtVyxUqjX_HzxjNY-6ehhX5qKYWm4ERIcLZc5UpAIXMUNTtnXpSVDrKkdBRcGvRlPyf5ZX0CrTDowTeNBnz7BMMWLDm0eb5UDrqZdp26Hw23yh2K-BFmT0ys3oICKHEmCYefO1Yli16Lx-eReb84c3vGbQvcjp3TMgKz3b0EEiH1UFqhVUbrooyIU6mAGVhhiWVVcn2iD2G7yvP4QF1cLXZ_UpMUo9jjweca2cU-Otvw-0DAYDqBrMnSrmJYNLRdbXUq5DH6i4f76kjoz_b9Q_Mrg-G5Ob9Z8PTIUZ1tB2x3xSYD3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f8294617ce.mp4?token=kw7DSMTgt7CmFTHEc4RnHhrfbP_NwfibnWtlYtVyxUqjX_HzxjNY-6ehhX5qKYWm4ERIcLZc5UpAIXMUNTtnXpSVDrKkdBRcGvRlPyf5ZX0CrTDowTeNBnz7BMMWLDm0eb5UDrqZdp26Hw23yh2K-BFmT0ys3oICKHEmCYefO1Yli16Lx-eReb84c3vGbQvcjp3TMgKz3b0EEiH1UFqhVUbrooyIU6mAGVhhiWVVcn2iD2G7yvP4QF1cLXZ_UpMUo9jjweca2cU-Otvw-0DAYDqBrMnSrmJYNLRdbXUq5DH6i4f76kjoz_b9Q_Mrg-G5Ob9Z8PTIUZ1tB2x3xSYD3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
👀
چرا در آلمان از کلمه قیصر برای پادشاهان‌شان استفاده می‌کنند و به فرانتس بکن‌بائر می‌گویند قیصر فوتبال آلمان.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/104980" target="_blank">📅 10:40 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104979">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31c7fdcd83.mp4?token=cN4poylUq2mMpjTW6dqHvKzxRqn73Vf-QfYaWcfM3lHk7FGeESVQ-3F-vixdeX9BAEjk1UDM7yD0zVAQmrqBFJDuOmv5OvVDaHdmPZ7rLEC2gw4XxeF4vi5Ko2Ea3OVsc9q1crj2RPLq-laVmgg4LJOm8LDD5wLhI0ToGeNh19r5JoUJoMmUVtVZzBbTH1p1NauKIZxxECPkBPtk6XX2Ry7FLURDGNjZadgjdj7iWDx9TrO8xs90dqWhHw5BNf9VfnPpg1pET3Kk9dFjSte10f8ejwPFxwzN7C3zjLTPUGh0y1VoPY569nEKhNH5PcKghib8ARep1nhzNNuUPs6xnCUmBLFpbz3DnZP8OfPfu_sHQMpi43a0MljpSepkOYOKbDk6dk6oYPorIDCz8H-tbLInImjL-KbYNzNO2G0h10lZg5G3_NhBzfVNh-wKux9Z0kg24YjdnqFYOwnng9ELzGxYT4AQP02AsqGTIPdxCoogK0zXC22p4-4rdZ8HzkkLOq9ZVGErDzykh4aJMckiDgNXGMG7AdA8Gt4JD13p_jL36TaWIViPvboDYctcA5xpnUgCJZz0imkYAFpfrkxUeOg-Qr7l8jsbT1iPHMvevo77nxg7jV6Fcv6rWfeljyHE0KwpNOxJ2bgfKriRc4Mj_lOpELkMNutUrjF2xRDYgrU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31c7fdcd83.mp4?token=cN4poylUq2mMpjTW6dqHvKzxRqn73Vf-QfYaWcfM3lHk7FGeESVQ-3F-vixdeX9BAEjk1UDM7yD0zVAQmrqBFJDuOmv5OvVDaHdmPZ7rLEC2gw4XxeF4vi5Ko2Ea3OVsc9q1crj2RPLq-laVmgg4LJOm8LDD5wLhI0ToGeNh19r5JoUJoMmUVtVZzBbTH1p1NauKIZxxECPkBPtk6XX2Ry7FLURDGNjZadgjdj7iWDx9TrO8xs90dqWhHw5BNf9VfnPpg1pET3Kk9dFjSte10f8ejwPFxwzN7C3zjLTPUGh0y1VoPY569nEKhNH5PcKghib8ARep1nhzNNuUPs6xnCUmBLFpbz3DnZP8OfPfu_sHQMpi43a0MljpSepkOYOKbDk6dk6oYPorIDCz8H-tbLInImjL-KbYNzNO2G0h10lZg5G3_NhBzfVNh-wKux9Z0kg24YjdnqFYOwnng9ELzGxYT4AQP02AsqGTIPdxCoogK0zXC22p4-4rdZ8HzkkLOq9ZVGErDzykh4aJMckiDgNXGMG7AdA8Gt4JD13p_jL36TaWIViPvboDYctcA5xpnUgCJZz0imkYAFpfrkxUeOg-Qr7l8jsbT1iPHMvevo77nxg7jV6Fcv6rWfeljyHE0KwpNOxJ2bgfKriRc4Mj_lOpELkMNutUrjF2xRDYgrU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چرا پرز بعد از هر قهرمانی رئال در اروپا به مورینیو زنگ می‌زد؟
چرا رئال دوباره مورینیو رو برگردوند؟
و چرا پرز فکر میکنه مربی شر ضروریه؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/104979" target="_blank">📅 10:15 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104978">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/181464f819.mp4?token=UrX04zrFB2D_tRXo2x0Md8enfLpMGYcHGxQKehq1uE3-QNE5IGuxk2kWm-IA8PlbwRcZGwxzaf2NcI9t6J6u4DHj8_KR6rwch22rmTFflgh0ckXl5EuY3XMkloLCyTpkQC5hpmL1w3bBliKKY-L8pF5S8xQ4tbLRIWDQ2vpXVV8thsSShGq-hzFCUm3-TjIhc9bbhCHLHukxfBoWjBxIdaHct6f1wpmTQBL0iymgaPIDocpPi19-WArI0xIKWzhLisD7_O-B2CAAbgdyMurdhZJmHfwRHpeBt5KsDJW4QSOPAA0IhqA3ZbSDewCia4qa7-60bhtUCr1DiOBvQ8rn4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/181464f819.mp4?token=UrX04zrFB2D_tRXo2x0Md8enfLpMGYcHGxQKehq1uE3-QNE5IGuxk2kWm-IA8PlbwRcZGwxzaf2NcI9t6J6u4DHj8_KR6rwch22rmTFflgh0ckXl5EuY3XMkloLCyTpkQC5hpmL1w3bBliKKY-L8pF5S8xQ4tbLRIWDQ2vpXVV8thsSShGq-hzFCUm3-TjIhc9bbhCHLHukxfBoWjBxIdaHct6f1wpmTQBL0iymgaPIDocpPi19-WArI0xIKWzhLisD7_O-B2CAAbgdyMurdhZJmHfwRHpeBt5KsDJW4QSOPAA0IhqA3ZbSDewCia4qa7-60bhtUCr1DiOBvQ8rn4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
⚠️
درخواست ۳۰میلیارد تومانی مربی لیگ برتر برای حضور در تلویزیون
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/104978" target="_blank">📅 09:50 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104977">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f84e6b721d.mp4?token=lp4RHznepB_PJ1bPZ6EoFzFxzk1CoZrE5kXOOfltfPRLZKmk9RvVAyLp19t6TztAPBywp9aJ-IqjJJCjqZIiOeDcFx-guCG7CTl4gAof_L4VJ3252kEEFKShmD0ZedzShPoVhKzpHSXwmLoj6DNFItVn19DD4tjTRQwO3nyc0GKMCjFQyhMPjcH3-3vVrRXQ7VhErA7ZlSmmSLv5ojJkELgF2_Wz19PAA2ojsMQdBnek88PNUufPeKrusRUTr6sPqRwLmNwXkVEGyQuLrk0R9fu-oF8KC74jPK_529rojyeSZT-Pp2lTD873O4zijALZyWEdYg5y6L-ZJ2l8YxF3OQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f84e6b721d.mp4?token=lp4RHznepB_PJ1bPZ6EoFzFxzk1CoZrE5kXOOfltfPRLZKmk9RvVAyLp19t6TztAPBywp9aJ-IqjJJCjqZIiOeDcFx-guCG7CTl4gAof_L4VJ3252kEEFKShmD0ZedzShPoVhKzpHSXwmLoj6DNFItVn19DD4tjTRQwO3nyc0GKMCjFQyhMPjcH3-3vVrRXQ7VhErA7ZlSmmSLv5ojJkELgF2_Wz19PAA2ojsMQdBnek88PNUufPeKrusRUTr6sPqRwLmNwXkVEGyQuLrk0R9fu-oF8KC74jPK_529rojyeSZT-Pp2lTD873O4zijALZyWEdYg5y6L-ZJ2l8YxF3OQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
🇮🇷
سنگ‌بازی دیشب هوادارای استقلال و فولاد حین خروج از ورزشگاه
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/104977" target="_blank">📅 09:20 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104976">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75514852e3.mp4?token=qMsgdPZQpqWBUrLZC4iuNLxiuMbs0yB8RG2795D4Wow8AONRLikp5PsI5uqo3XEIUePuDEjjWCyLr5oD-F46EyOlVK-9cPvZE5JWYtnh6JTgRlymOQmTVoAr-BXcvoQRw690nvrOKPUFLapfAQ08l2YkNRe8gK7PJ3JmZc61pjAq6XPWCFsGNPwLkFo5S6ZSbK6Xxu8CYMpSv67PsKyhouWQz8TPwnn_qQwql-pVmyeuECxX1alenXs4TuNMgfOmq1ySQYDv2qyXOM0JywvSuSJMCJn5StMBEzlaV35b5HXlTnMqF-Vy9seqV6_UUtFOZz1qI3jSbPbJLo5gpJPXlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75514852e3.mp4?token=qMsgdPZQpqWBUrLZC4iuNLxiuMbs0yB8RG2795D4Wow8AONRLikp5PsI5uqo3XEIUePuDEjjWCyLr5oD-F46EyOlVK-9cPvZE5JWYtnh6JTgRlymOQmTVoAr-BXcvoQRw690nvrOKPUFLapfAQ08l2YkNRe8gK7PJ3JmZc61pjAq6XPWCFsGNPwLkFo5S6ZSbK6Xxu8CYMpSv67PsKyhouWQz8TPwnn_qQwql-pVmyeuECxX1alenXs4TuNMgfOmq1ySQYDv2qyXOM0JywvSuSJMCJn5StMBEzlaV35b5HXlTnMqF-Vy9seqV6_UUtFOZz1qI3jSbPbJLo5gpJPXlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
🇮🇷
🇮🇷
تشویق دیشب اسطوره علی‌دایی در یزد توسط تماشاگران چادرملو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/104976" target="_blank">📅 09:00 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104975">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">‼️
سوتی فوق‌سمی یاسین‌بونو و کولیبالی در بازی امشب الهلال که منجر به پنالتی برای حریف شد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/104975" target="_blank">📅 02:02 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104974">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4aac6582ca.mp4?token=QUaTAxRr2aDll1z80p9gCkHim8ehCU_lur5n5ShO1rdjczD9LaEutDvwUBlnvTFfC9ukKgwzIV_h8EQ4MXTKfsRks9pe4NDDBL6VOmd6kQQ3nKxPqIwY2PbbJ8hblTgLhiRUZtlYzM40dswelJNkuLVqY6lrW59IsHdZgL3LLg8KYQpm5-7VYJtzpCzZPXlEtd_Y6uvDWkv8Y5ehhoMCMkcc9IZFK5u67plrRXqW1ccjO3RCO7tGyqlBtC20_49Bz3-cRpCJjlcouSXGO1sjJgmAxIvxUgTFVHRW_vL-FeT03Y7O7eWyqikLDVsr5eVAvB7eXeXpgRbrT4ZU-fmw7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4aac6582ca.mp4?token=QUaTAxRr2aDll1z80p9gCkHim8ehCU_lur5n5ShO1rdjczD9LaEutDvwUBlnvTFfC9ukKgwzIV_h8EQ4MXTKfsRks9pe4NDDBL6VOmd6kQQ3nKxPqIwY2PbbJ8hblTgLhiRUZtlYzM40dswelJNkuLVqY6lrW59IsHdZgL3LLg8KYQpm5-7VYJtzpCzZPXlEtd_Y6uvDWkv8Y5ehhoMCMkcc9IZFK5u67plrRXqW1ccjO3RCO7tGyqlBtC20_49Bz3-cRpCJjlcouSXGO1sjJgmAxIvxUgTFVHRW_vL-FeT03Y7O7eWyqikLDVsr5eVAvB7eXeXpgRbrT4ZU-fmw7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
🙂
🇮🇷
مصاحبه با خواهر صالح‌حردانی ستاره استقلال بعد بازی
: کل خاندانمون استقلالی هستیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/Futball180TV/104974" target="_blank">📅 01:10 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104973">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/241731bcb2.mp4?token=qmPsaYKMYhZ8jDHIkHfP-AWQYqM4vBBCZnnveEWOwmjfa0XSvSqK1OGy8p4ntxZOPJ9BFG9-ZzMi3zs4bGdUwvuMv2tj7tBaaombnivPJYZ01aaJYeAoBv8zkLwq4N-2VX2FdH3bjSOvgsl6alTe6mYRtmxtDuc3PZgWhOSZaba_Bo8DGutRhqydSRydGdYyrMvpwRktC25Z16cKJxPWwKIC-ZHmvhBKrEvrWVX4OJ3wXRLO3c4qckAt-zjpPmJHLLm3E4oZwjuEse16EEplwfk3gluq-XbbO4sNzbaRKfZnb0Rl7HvsTV23xWmNFjv7pPIfeuXNM7b-YW7LAAHnQIDtgnOlHdUnJPk-9n5cS_J12RU-2WTZmRwdMB_98qrbNZx72IRx_TGMOkStMuiE3fTZZ8XCCnKN7k7xS2NrYZb9hCMK8Q7Hjp6cwX7BBoL4NAvVJzYGC7xJV6iDEyaj5C-EAqK0GS_4slvh_GOy0teVTZLs2KxHdx_cDCW8sOgml97hbupMCiDRjKj0-t7440YRAVRktPld5XsZ_aNNmstCo8aP0vort2eERy6B2qGkLoWwvql9q_EMi4X3ntuqyt6emfHJRWRJzT-7FvkgmwJnN9xcFv6i87jPyZIAdPQmOiBXsJVzPM1Jd2QAwz6T-KFbTUy6B4qliF5ZoJmdv68" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/241731bcb2.mp4?token=qmPsaYKMYhZ8jDHIkHfP-AWQYqM4vBBCZnnveEWOwmjfa0XSvSqK1OGy8p4ntxZOPJ9BFG9-ZzMi3zs4bGdUwvuMv2tj7tBaaombnivPJYZ01aaJYeAoBv8zkLwq4N-2VX2FdH3bjSOvgsl6alTe6mYRtmxtDuc3PZgWhOSZaba_Bo8DGutRhqydSRydGdYyrMvpwRktC25Z16cKJxPWwKIC-ZHmvhBKrEvrWVX4OJ3wXRLO3c4qckAt-zjpPmJHLLm3E4oZwjuEse16EEplwfk3gluq-XbbO4sNzbaRKfZnb0Rl7HvsTV23xWmNFjv7pPIfeuXNM7b-YW7LAAHnQIDtgnOlHdUnJPk-9n5cS_J12RU-2WTZmRwdMB_98qrbNZx72IRx_TGMOkStMuiE3fTZZ8XCCnKN7k7xS2NrYZb9hCMK8Q7Hjp6cwX7BBoL4NAvVJzYGC7xJV6iDEyaj5C-EAqK0GS_4slvh_GOy0teVTZLs2KxHdx_cDCW8sOgml97hbupMCiDRjKj0-t7440YRAVRktPld5XsZ_aNNmstCo8aP0vort2eERy6B2qGkLoWwvql9q_EMi4X3ntuqyt6emfHJRWRJzT-7FvkgmwJnN9xcFv6i87jPyZIAdPQmOiBXsJVzPM1Jd2QAwz6T-KFbTUy6B4qliF5ZoJmdv68" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
فراز فاطمی سرپرست چادرملو:
🔺
آقای پیام حیدری فکر کرده ما خریم. قشنگ بگید میخواید یه تیم ببازه دیگه اینجور قضاوت کردن بخاطر چیه. امیرحسین حسین‌زاده با تکلی که زد دوبار باید اخراج میشد ولی حتی صحنه به وار نرفت!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/104973" target="_blank">📅 01:02 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104972">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7aa1d6121e.mp4?token=SLtJXb_gFlmo3rcFU3Guawz4_2hZbNTgJI3FKbU53jOhxyE3jypJrDxVMy4BBGt13I4kBcWVcIvEkZDHvnrF6zfx6JWidPtgBVjssFqKOMtEnMstr6Nlz5sQFaSvX40VYTs11RUn4rDosVH0TMjPEV89gmZt08vnnOdNiuDpDOTG_qC4lRQQ8WvlREsCQzOVNt3gNWsUitOxkXndmpOx-B9pxzxzMih4nBFpQAQAOPbeeKIvicu9NsAppNbjCej_k49tB_JeZcrJOiHLmoKPjwE93tKIU_8sufgVjuP4aDod4oSbJ74jhMbgmAfJdUpZvGdjC3yQAepqkrQR06dxCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7aa1d6121e.mp4?token=SLtJXb_gFlmo3rcFU3Guawz4_2hZbNTgJI3FKbU53jOhxyE3jypJrDxVMy4BBGt13I4kBcWVcIvEkZDHvnrF6zfx6JWidPtgBVjssFqKOMtEnMstr6Nlz5sQFaSvX40VYTs11RUn4rDosVH0TMjPEV89gmZt08vnnOdNiuDpDOTG_qC4lRQQ8WvlREsCQzOVNt3gNWsUitOxkXndmpOx-B9pxzxzMih4nBFpQAQAOPbeeKIvicu9NsAppNbjCej_k49tB_JeZcrJOiHLmoKPjwE93tKIU_8sufgVjuP4aDod4oSbJ74jhMbgmAfJdUpZvGdjC3yQAepqkrQR06dxCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
🚨
معاون اجرایی پزشکیان: شخصا اگر میدونستم آمریکا قراره رهبر نظام رو ترور کنه، دست از ایدئولوژی‌های خطرناک برمی‌داشتم و غنی‌سازی رو حذف میکردم چون عقلانیت حکم می‌کرد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/Futball180TV/104972" target="_blank">📅 00:37 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104971">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o-5N_CpPy8dJnqDposQfwqSrPC522yx66YU45owLkhPtQ4_FuhsrRfsOquxeO56ckTXDsODVcDGjMPT2marq9H1TorILHaTS3K34YBcQKHWixtDftp3Fwb3NI9o4fVbbDpUa4D9WUgE7hoCex3cz2hiAEti-mpYgh8ZslQ_QmA2PUS9CplgZcYYjNRgn8o9bTNOgF6AzvDscMXoJHpHZnjiC9Nbu3-UL949QHokd18B1qvrHWQFkzTVS9XFPwL6XZzc7rugfCB6vUqBPszo1KKdFh-cst4q1V2VY_NRM0m9tgNGGVL3-QGSSq0nJWrLHYq48j4AUrG3_29rbAOeh3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇫🇷
هفته‌دوم لوشامپیونه؛ انریکه همچنان در حسرت برد؛ لیل موفق به کسب امتیاز از قهرمان اروپا شد!
🇫🇷
پاری‌سن‌ژرمن
😀
-
😀
لیل
🇫🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/104971" target="_blank">📅 00:27 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104970">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FQdz0lFWWdFX2rx6WfEg6Bw0dMCwFffxMy6gyYJJRbytfARTJJ8Yg8P5p2PopnJSG6PUipLogwam7r22qGZvLf2MMcacTUtxWUTYI1s5jHsK90VhELj9vW3z1Q8EERRkG71NmC5i2ejdeB8hKPrR5cM2fAv8y6sr5H9zg7m8ePhojTwYgzo9XSU7VbLTMF7az-0ieOoZTCTUqaEoDocSn_ElAmsdvhFD9tRhyagkQggS09Vz3LE5g3wP32lndEP92EicRZDOkgQFOzD8Ekyg_HhOim_c91IPYtE1zeAEClKcqiuTy_si4DL_FqIG-3D7Dmd0LWez42CCnXGdXdXulQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
هفته‌دوم پریمیرلیگ؛ پیروزی پرگل در خارج از خانه؛ موتور گلزنی هالند به موقع روشن شد
🏴󠁧󠁢󠁥󠁮󠁧󠁿
منچسترسیتی
😀
-
😃
کریستال‌پالاس
🏴󠁧󠁢󠁥󠁮󠁧󠁿
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/104970" target="_blank">📅 00:25 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104969">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bzdh1J80Pr65xIgd4Vo2HtqN1wV8VORJElP5D8frlIO04_NQ42LtalNYMF3lKwL-lPrrFwWzYBpfT2JDKhZL_feyRwNIp9LR6eeDaIwCdIGIm_vyE5XAppSkxHDxrZyyUDLpxC4vLE2pySrS6516Oyr63qyYCM6W9r1yrltQmtO3e9cfpBYmAV9Ono6uWTMewR1TMjTJb1oKpLMaz1zu8toKWLY0wm_xSD1mAHArsOFnlfXvpnuCul1Rx1K7CZSRxHLsR-iNauOBPZuyzDpQU1Ftg8e7P9Xn9zAdJSd_n29A8JgNLA3kyLtK8Otyo6FE6omX_m4OpPOlaDfq1mn4NA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇹
هفته‌دوم سری‌آ؛ پیروزی راحت در خانه؛ روسونری با مهاجم جدیدش دلبری می‌کند
🇮🇹
میلان
😀
-
😏
ونتزیا
🇮🇹
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/104969" target="_blank">📅 00:19 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104968">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32fe7cb793.mp4?token=vKUadNkbnquf5779Yb2OKRX-5R9t2QLnUfAcivgJtxxPeYPy1JmFNDwlBNNVuKfesUhdgPutzGw0qxXwDyp4UheG5Of1NshiWocT5TpBerjAGJkamV3_renE6Vhijoy5PgF0Nq3ntUrkQs_Gmfp-Ja74jhWOTdRabRbWbC24cipIg0bQIJ9A-coGkOr-AUh_GwLITMiywCUWEa8SfTloeW5r297G7DmE35xy50CXNHsDCkRE62FAD1jQSDLgQKe6_Ys9taQ9Opr2KGnQ9b97JCd6VSl3E-XP87Eq6tcB-fxoUWZAVV9UQE2vUe9yA4QzTgoR0zfOI5aLMwDY7GRcaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32fe7cb793.mp4?token=vKUadNkbnquf5779Yb2OKRX-5R9t2QLnUfAcivgJtxxPeYPy1JmFNDwlBNNVuKfesUhdgPutzGw0qxXwDyp4UheG5Of1NshiWocT5TpBerjAGJkamV3_renE6Vhijoy5PgF0Nq3ntUrkQs_Gmfp-Ja74jhWOTdRabRbWbC24cipIg0bQIJ9A-coGkOr-AUh_GwLITMiywCUWEa8SfTloeW5r297G7DmE35xy50CXNHsDCkRE62FAD1jQSDLgQKe6_Ys9taQ9Opr2KGnQ9b97JCd6VSl3E-XP87Eq6tcB-fxoUWZAVV9UQE2vUe9yA4QzTgoR0zfOI5aLMwDY7GRcaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
‼️
🇮🇷
کشاله‌درد دوباره شجاع خلیل‌زاده در بازی امشب مقابل هواداران یزدی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/104968" target="_blank">📅 00:09 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104967">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K8_IHhV9M499brRuFTjbu0kph-WVZ3gRT4FdUrhLCVWkcHsqSXr8FkCx2NbLWn7K6HP46caTtONNNf7agpaMJ_Ao5gYSfoDmefdQUlU5nerDpEFgLI77Fr1N6wHU6NTT-gj0ZDm3LsNTu_CiDqDMThygmK6mcdiJN4q4-kDRBZEipAfSIQc0VLbw9DAJyfckh46xtFvOIIkJzANgRLVpfYaPrOkgM3gHiA0H0ZDRbKQgS0i3Jv1XzgDX80gaRDOdtZXk9mMKwKJEGIABqdWc_dpwQtyP01wxSYEBqgT3zVFBnuVSkJ2akdsHo7Iv_rGGkwKWYn0MMITK7Qvcbpazwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🇩🇪
هفته‌اول بوندسلیگا؛ موتور گلزنی خشن تیم‌کمپانی با قدرت لیگ‌را آغاز کرد!
🇩🇪
بایرن‌مونیخ
😄
-
😃
اشتوتگارت
🇩🇪
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/104967" target="_blank">📅 23:57 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104966">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e92dec0fb.mp4?token=ZFhJOkUQGWwaXExuLSOE8DB9OT2gUg6eSKhZjJcgURWaWtM4Tjey8MUQKOkpjXOI_kdaDxHLK6CUfjPn8Kk9jHoBSBqkpFoQElvCigzHrz3hNLVdawJwVUUtMC-B0vBPX9o97frVKPGK4NlAWQMxUwbeytiX4wKL4a-_fzaid-NYWgKTM4u-LzmCZHd7kwUZYUq_VDPACqv__7-lqCijLBY7Me_Q7SNYGZB1YvRv5kZuaYC7WP1hODYxtAKhw3SuUR_QZeC1GKGW_XCAK5OvbnwR3zHxsqohaQIzZveyVI39NY-sh8_TmL2xR6ao4cQBsnqnFPntMj2KDrqtWqEpXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e92dec0fb.mp4?token=ZFhJOkUQGWwaXExuLSOE8DB9OT2gUg6eSKhZjJcgURWaWtM4Tjey8MUQKOkpjXOI_kdaDxHLK6CUfjPn8Kk9jHoBSBqkpFoQElvCigzHrz3hNLVdawJwVUUtMC-B0vBPX9o97frVKPGK4NlAWQMxUwbeytiX4wKL4a-_fzaid-NYWgKTM4u-LzmCZHd7kwUZYUq_VDPACqv__7-lqCijLBY7Me_Q7SNYGZB1YvRv5kZuaYC7WP1hODYxtAKhw3SuUR_QZeC1GKGW_XCAK5OvbnwR3zHxsqohaQIzZveyVI39NY-sh8_TmL2xR6ao4cQBsnqnFPntMj2KDrqtWqEpXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
‼️
🇮🇷
🇮🇷
محمد تقوی، ایران‌اینترنشنال در برنامه هت‌تریک درباره تساوی استقلال برابر فولاد گفت:
«غیبت آشورماتوف در ترکیب استقلال باعث شد تا عارف آقاسی کمی با مشکل روبرو شود و نزدیک بود با اخراجش شرایط استقلال را در بازی عوض کند. همچنین بازیکنان دو تیم در ضربات آخر بی‌دقت بودند.»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/104966" target="_blank">📅 23:55 · 06 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
