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
<img src="https://cdn5.telesco.pe/file/KdZubS7lfsRTbfAjkIXcZWNpnTocd6t8JsdiL96uR7uYqpQB40aC0vIDKoYCcMT_D9FIt7TuLRe1Wxo0P0E-VyYJJxQA1tGomU8q9Fs-jkyC6Leg3Uz3zQrTZ6Y_MZYwlxKsUfafeN7UChnCQH1CO7Ec59rUoVqX3uLJAKzeMcy9z9uuM2MqlGgzFm_SDWbdkATNrB0fCQJbJlI5rbnV4iSw_vIZM-l2lc6hQ8-o-qHYfhtYQzR6c1wtk-6Iz0Fmds9UkzRFaHgdVW8bJixRFyNE7C0_KwQPqBVo_Pbet7Ilealv2VU-YvSrqL64jQt558ffRFy3KmgGir8VMK1v6A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 406K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-30 09:11:44</div>
<hr>

<div class="tg-post" id="msg-106982">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d9b6fbcb00.mp4?token=jXQ_OrQlYtGGJAkoB9STqYdY7eOQUqAwTrABV3KbJ8aVWJOrP_Hu6OzDhWJccwrNr1YPO3xyNiDY98Mn08BWP-jdzkVglILiUT5gdn3G_C2jxiU_dNSlh1YRlhZq-F_g8Nf6tvB6PiUxSo4gNDGNM9oFWwPGzlgo3f5zfovt0cmjVqb-p1ryBUIC5VjDYPgG64fBJhU4xp_G6veanZ2-g0ZEvZHk5SY7LVj4nn6qhO5cfHYsylPJuluCJmzfA9oqs6ZJoVWZEt_rahc4TykJvOXEhloDb2sY9T_No9N42VPGFvBxWOtl0Pa5aiffFq74MnlqrZcIDHfXZxvXc9_RKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d9b6fbcb00.mp4?token=jXQ_OrQlYtGGJAkoB9STqYdY7eOQUqAwTrABV3KbJ8aVWJOrP_Hu6OzDhWJccwrNr1YPO3xyNiDY98Mn08BWP-jdzkVglILiUT5gdn3G_C2jxiU_dNSlh1YRlhZq-F_g8Nf6tvB6PiUxSo4gNDGNM9oFWwPGzlgo3f5zfovt0cmjVqb-p1ryBUIC5VjDYPgG64fBJhU4xp_G6veanZ2-g0ZEvZHk5SY7LVj4nn6qhO5cfHYsylPJuluCJmzfA9oqs6ZJoVWZEt_rahc4TykJvOXEhloDb2sY9T_No9N42VPGFvBxWOtl0Pa5aiffFq74MnlqrZcIDHfXZxvXc9_RKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
فاصله بارسا و رئال به شش امتیاز رسید.
👀
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.78K · <a href="https://t.me/Futball180TV/106982" target="_blank">📅 08:00 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106981">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-footer">👁️ 8.79K · <a href="https://t.me/Futball180TV/106981" target="_blank">📅 01:17 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106980">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTrexBet IR</strong></div>
<div class="tg-footer">👁️ 3.31K · <a href="https://t.me/Futball180TV/106980" target="_blank">📅 01:16 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106979">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U4uMo4tb-2L-ALE9eU0EylZ2xDkvKWt6vZ5LH7cj22weoOsdtwZW9QfA35Qxah9ivOmHdBsCw0DQtwuUgWsSO6UZs7vSvMW6zdgQmycViF7AJhVi_c393cXQ9BfeSo6yDyZ9PWfnlreZs67agTVcSrXNeufGa-TRK2JbCGAohx6JACpyRQW-GsopfCjCNAp8SshnheDALn1Enmnap2tdiYp5KjSFdZ-AptXdvjLpXzwnEmBG3Z3UEoYWQ_G3bSw7dnFbk2XbdsGXBqCqVmQOuivGl856bySnVZU5WbS-ItgJQ3uMqLajhZ9_uJYqhNB-pL6qC-Q47UeFZpPQ_Kqs5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇪🇸
سیمئونه درباره بارسلونا:
🔻
انگار اونا دارن یه ورزش دیگه‌ای رو بازی می‌کنن، نه همونی که ما بازی می‌کنیم. مهاجم شماره ۹ نداشتن، ولی یهو رافینیا از راه رسید و ۱۲ گل زد. یامال هم اگه اشتباه نکنم ۷ گل زده.
🔻
توی زمین خودت بهت فشار میارن، زمان رو ازت می‌گیرن و از ریسک کردن و گل خوردن هم نمی‌ترسن. حتی انگار گل خوردن باعث میشه بهتر بازی کنن. اونا الان بهترین تیم هستن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/Futball180TV/106979" target="_blank">📅 00:45 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106978">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TIgtIRJXDCx6qbq553ToDfhCwdIQmI3amIvZuicm3yJNekfytM7yiFwyMjxC-pODayaJOU0koL_buv1_SXLxeLLqGVGTfFxTtKH_2LKlGrqjEXtzCvvdWAilmhDNmUKCT8rF14LTcpA0lxeDfAfhTNeVPXVXv83p30LfaVpoMXocimGOQn7QB82n0kPQ8xfMZbR3b_gSkKCEaciPuwcSBWGuDri9WHRzFKxXT5oSnrbsMPEp4puUlSq32_77BI8H74VI-1IvL2BcWoCbH_7TZxjFOk_gLBQe0EKvuCDnJTIIarfakqbUU9Ucin5mgCTY0rKTH_GOKbrHUieepUQkeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
⭕️
شبیری‌زنجانی از مراجع تقلید شیعیان دقایقی پیش در بستر بیماری درگذشت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/Futball180TV/106978" target="_blank">📅 00:36 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106977">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dGaAxhkUyzvaoyb9M42flK71rGtLrZPFuAQlgj5oB6OosnM300-qQDL0Eq8lNwTzveiZfvGNuMPAgCy6AKZb2HHcSnnihWa2hqjDPlBD3PKFsDi_OcQtsYnqOFTVwBUDouDFThRv37bW66X0EBLvrcwvXaJwW1kzVU9kyP-X81LzS0hW9dLH0c2MH4Vlz26wQQAj98ab8K5udmMSQeHWMdgKDObctNlwRq3TzaPJI3cAVvf-bAnPbP8PEMDZlLbxt9LPCmK5qFJJa9vd4KBZlGwzzaYvgfJSXxUHJ6c8yava4Mf9agHoJfp9IEa-qbU7EWSE5ojBf3zRPd7FeJrYQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇪🇸
خوزه مورینیو: به کمیته داوران تبریک می‌گویم. آن‌ها باید از این نتیجه بسیار راضی باشند. همه‌چیز بسیار عجیب بود. بازی باید ۱۱ در برابر ۹ دنبال می‌شد؛ چرا که اتلتیکو از دریافت دو کارت قرمزِ مسلم قسر در رفت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/106977" target="_blank">📅 00:14 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106976">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OugSCzrof76BH6yOMrGLPSrbBwber0U2R01wxs-Eb7AKF9CukIy8zNlKy7giDmpY6DXqCXUCJXvte1-Q0NSqdIjvsbvdUNwLuZQ2I07PTWMg_ciqA7hbxaE_2q8quDiFcAFJSByH2N2R2Dt-8Xd-nlAdhgra5dicmKQut1Bpk0xPey6k9o12cgebQXxELe02X77Kuvr0t2lJBt9AKjTgWgVBuipSR74hsJrclBd-KXLsKuq-R1DP3OL2NJ8YtRTW0gKznTNN4vleyB64wuUVbQy5B6KcGhEQW-52q3LSdyT0Cufy6nJ7kP0froKhekyNDOcg16-XHK8u8T6cxTyVNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بارسلونا در فصل ۲۰۲۶/۲۷ تا اینجا :
⚽️
۸ بازی: ۸ برد، ۰ مساوی، ۰ باخت
⚽️
۳۶ گل زده
🥅
۸ گل خورده
🇧🇷
رافینیا: ۱۷ (
⚽️
۱۴ گل،
🅰️
۳ پاس گل)
🇪🇸
لامین: ۱۴ (
⚽️
۸ گل،
🅰️
۶ پاس گل)
🇪🇸
فرمین: ۶ (
⚽️
۴ گل،
🅰️
۲ پاس گل)
🇩🇪
آدیمی: ۵ (
⚽️
۳ گل،
🅰️
۲ پاس گل)
🏴󠁧󠁢󠁥󠁮󠁧󠁿
گوردون: ۴ (
⚽️
۰ گل،
🅰️
۴ پاس گل)
🇪🇸
پدری: ۳ (
⚽️
۱ گل،
🅰️
۲ پاس گل)
🇪🇸
اسپارت: ۳ (
⚽️
۱ گل،
🅰️
۲ پاس گل)
🇪🇸
اولمو: ۳ (
⚽️
۰ گل،
🅰️
۳ پاس گل)
🇧🇷
ژسوس: ۲ (
⚽️
۲ گل،
🅰️
۰ پاس گل)
🇵🇹
کانسلو: ۲ (
⚽️
۱ گل،
🅰️
۱ پاس گل)
🇪🇸
برنال: ۲ (
⚽️
۰ گل،
🅰️
۲ پاس گل)
🇩🇰
کریستنسن: ۱ (
⚽️
۰ گل،
🅰️
۱ پاس گل)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/106976" target="_blank">📅 00:10 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106975">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/773fad15d7.mp4?token=lb09KJVnFfusSJXKotce0Z4ikhuXgsbn86kAqdFz8s0yzBEUIPZMi75qkbZdXIy6SiFECJZGumc16-tqXy175urLb_Fe3SgSNVJVAXYlNFfO--IOr8c6M31WsD1YlEThqkjKcu1P1c75HPFmBmC-9adl8slIKZApvIUtHIzcimdSO_vqoI2dwkk-Irn4fTjKwK91r0DboK8A1moDb2tgBysvDHZYMu_WpzEP99XnOe9dhGovzx-YS7UR0tUCwhrnD2SpR694cMRF6fJ7ovq0KvyCkwTSi6W1Xr7W70gYUN9zh7DmIsgLKuw6R6dVBqQ-Hd4MTJSxeZnLgH64XyrpQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/773fad15d7.mp4?token=lb09KJVnFfusSJXKotce0Z4ikhuXgsbn86kAqdFz8s0yzBEUIPZMi75qkbZdXIy6SiFECJZGumc16-tqXy175urLb_Fe3SgSNVJVAXYlNFfO--IOr8c6M31WsD1YlEThqkjKcu1P1c75HPFmBmC-9adl8slIKZApvIUtHIzcimdSO_vqoI2dwkk-Irn4fTjKwK91r0DboK8A1moDb2tgBysvDHZYMu_WpzEP99XnOe9dhGovzx-YS7UR0tUCwhrnD2SpR694cMRF6fJ7ovq0KvyCkwTSi6W1Xr7W70gYUN9zh7DmIsgLKuw6R6dVBqQ-Hd4MTJSxeZnLgH64XyrpQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل‌دوم پاری‌سن‌ژرمن به مارسی توسط مارکینیوش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/Futball180TV/106975" target="_blank">📅 23:58 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106974">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f22d5f48d9.mp4?token=iqIu7XO2I7kkmj9iIL0GHSRpvQsVkhGf5WYjAmQyAx8NJ8rpFLPqSojLSNj2gIkoyvGyzqBifF9MzaEeP4sqBV-6aopyiKxPInrWGaTXswtFYAEZGjYNZeUUzWa_UlZGeJ7NDFYm3ymFiAqrNwVouvIwmW3cytI2E0-kOWTEVS7bXlDcPaOOA3GfdqzAqgk-rp_Pid4byrk9daS6e6Lf8qbGZ55shKpQuU_fRhNrQ8VRdMCwvVqWY9vKIcrkkiOXI9-qW6HuLbymR5V_NEq89sF6N27KiAFZqXI4JO70EQDmAU3z2s_1PqkwN1e1vD5Y9kwM6uCkSGpAU2FvsRw2AQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f22d5f48d9.mp4?token=iqIu7XO2I7kkmj9iIL0GHSRpvQsVkhGf5WYjAmQyAx8NJ8rpFLPqSojLSNj2gIkoyvGyzqBifF9MzaEeP4sqBV-6aopyiKxPInrWGaTXswtFYAEZGjYNZeUUzWa_UlZGeJ7NDFYm3ymFiAqrNwVouvIwmW3cytI2E0-kOWTEVS7bXlDcPaOOA3GfdqzAqgk-rp_Pid4byrk9daS6e6Lf8qbGZ55shKpQuU_fRhNrQ8VRdMCwvVqWY9vKIcrkkiOXI9-qW6HuLbymR5V_NEq89sF6N27KiAFZqXI4JO70EQDmAU3z2s_1PqkwN1e1vD5Y9kwM6uCkSGpAU2FvsRw2AQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل‌تساوی مارسی به پاری‌سن‌ژرمن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/Futball180TV/106974" target="_blank">📅 23:53 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106973">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ed04c10225.mp4?token=haJzqXqSR2TmZmZ-lDtA6xud7QTevsUE1ysVP-hEZKff0LfW6p3teub_oMFb1D1sLL8Ouv2becgWOBQrHraqSgI5xLW2-o8Q604P5ZJpcxXG1eQTVChV4Jem1IYq-eGdv2R2SFjCS0JrlTcisG8LWw9a4xtRslFwry9T4GwOYAAqlSHjcllukqvsYgajiUEhhkdXNn9jcjNm5NnbzH4i2CBnwzoVitR_mblySrrp9DyD-R_kB307xdqJ3EKsRFwxtiH0NxpU2DEZcbVBrstD5riqa55EkxH_V-eGjKCGV9NBBQTdiC8ncEswukLxiXggfZxUj1tlweeW6PkgD0Zz17zu8T1T-xlkOj38bLmFUIgbKPaoA6Kk4BtMXuqJiSmw5ua3dVm8-X6BSI39hxdQQMveAA4DoTNJcMUjS0xw1L5O0yNIiq8fA28mxP8G2rYZvzwzYvfXbXRnKTv8W-sN0dOopuTJO0myR1g2p1szUFBGwPJEGIicdCLtB-axAIBebXwFmgj6XF9bKn_ZgZhEbS6qnJJgJSKZWSgJD_f-_07igLFz-FXd14KirmctHL5CXz2PIN1L6wBzWHF274w-KWF8dKzSu9bk4oGOcndLdR0YdJ40r5s2rtGj6PllDi_PUv2N-UqAAi7QafzxXxTUah-oqRA01GSvxSy9Vct2FI8" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ed04c10225.mp4?token=haJzqXqSR2TmZmZ-lDtA6xud7QTevsUE1ysVP-hEZKff0LfW6p3teub_oMFb1D1sLL8Ouv2becgWOBQrHraqSgI5xLW2-o8Q604P5ZJpcxXG1eQTVChV4Jem1IYq-eGdv2R2SFjCS0JrlTcisG8LWw9a4xtRslFwry9T4GwOYAAqlSHjcllukqvsYgajiUEhhkdXNn9jcjNm5NnbzH4i2CBnwzoVitR_mblySrrp9DyD-R_kB307xdqJ3EKsRFwxtiH0NxpU2DEZcbVBrstD5riqa55EkxH_V-eGjKCGV9NBBQTdiC8ncEswukLxiXggfZxUj1tlweeW6PkgD0Zz17zu8T1T-xlkOj38bLmFUIgbKPaoA6Kk4BtMXuqJiSmw5ua3dVm8-X6BSI39hxdQQMveAA4DoTNJcMUjS0xw1L5O0yNIiq8fA28mxP8G2rYZvzwzYvfXbXRnKTv8W-sN0dOopuTJO0myR1g2p1szUFBGwPJEGIicdCLtB-axAIBebXwFmgj6XF9bKn_ZgZhEbS6qnJJgJSKZWSgJD_f-_07igLFz-FXd14KirmctHL5CXz2PIN1L6wBzWHF274w-KWF8dKzSu9bk4oGOcndLdR0YdJ40r5s2rtGj6PllDi_PUv2N-UqAAi7QafzxXxTUah-oqRA01GSvxSy9Vct2FI8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل‌اول پاری‌سن‌ژرمن به مارسی توسط فران تورس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/Futball180TV/106973" target="_blank">📅 23:46 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106972">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2832d49487.mp4?token=DedIFiqIfsupke_ESTfy9C3SzxL1krd_GdEZ970Yh80tJ9Vm5uzWYG5NQ4dJZo2E7TB8tr6Isvq9DZbptc_ieX10ATGqK6FlxiN3uulxjObrIMDUmg4teTgZT_slJNzdweKhZAFUhqpn7ALtapZNTHQPA0Zi20ifGDF8OJT0_5HO3rzjWqMbALdPcZI_s1l6aq6Mt_RhI-fcagTFdfYv4cgM8w6iyQ1hxXlCF6rxnLqVj1WHdScLji8QxNi3cGrfydQLeZdiLtxN3ra6ZiTTK2nPTH3PzA9A0YwZzgkK3vxmwrCupBTJ8oPklKHCyuWpDOuGXTDa5ml5IBX7weI-6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2832d49487.mp4?token=DedIFiqIfsupke_ESTfy9C3SzxL1krd_GdEZ970Yh80tJ9Vm5uzWYG5NQ4dJZo2E7TB8tr6Isvq9DZbptc_ieX10ATGqK6FlxiN3uulxjObrIMDUmg4teTgZT_slJNzdweKhZAFUhqpn7ALtapZNTHQPA0Zi20ifGDF8OJT0_5HO3rzjWqMbALdPcZI_s1l6aq6Mt_RhI-fcagTFdfYv4cgM8w6iyQ1hxXlCF6rxnLqVj1WHdScLji8QxNi3cGrfydQLeZdiLtxN3ra6ZiTTK2nPTH3PzA9A0YwZzgkK3vxmwrCupBTJ8oPklKHCyuWpDOuGXTDa5ml5IBX7weI-6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل سوم لخ پوزنان به رادومیاک توسط اللهیار صیادمنش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/Futball180TV/106972" target="_blank">📅 23:23 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106971">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LwgMFPUZHL7O8j2-TT0lV-o6VohhHOW0P617mEGNtCyS9QrvEcjCO_i0FFucKems7i8ZWJJvCv6BKr2nRk2PZXHRBHPmmK6FnwkPMJcNgQ4ZMwbGCUOSDKt40uM52X4BmPtK-Y8yPaJ7Qsw078hHY5_4FVJdE935jU7oOJYTSVLB6pff_B-f7H3lBOHLH0spVoujEtlQdlyxjRbuASMu95v2DKL-Dvhy4yTu4JP5memOLMLSYyFtOvm_5rK9kw1pUa7J7sK4LzF67f5E2t01g0cpmlxrfx2unqYcSsTFXd1UvJknsggXDgHhfY-Dk01bOVmSIuP_qyA6E8ohbsDP1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
ترکیب پاری‌سن‌ژرمن مقابل مارسی؛ ساعت ۲۲:۳۰
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/106971" target="_blank">📅 21:42 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106970">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/19a38b8192.mp4?token=InCcFscUl-Gnr0uK58jvxPuurowsZ7Wait5Uh_fueqVkH1gtNAWl_psDZ9qaEmiZSy5-v9Lcf6dwbQVaetXrLz9CqhvG8ciLO-3RpU427T8vZ2sIqmLZezyP_8MoRVCJNDJKAqJ-KZP5iyDxDLoDB4Z_jcz3JlBqvCgNQXz9EuzuPyEiuVQ6mV5me6nldn1XzPmXCf08PKHFA9Ih43lP_-5byUwWCJpnsMzFaB5I9tBvai94ItV7qAi-8gGoeQOp78eM-KICNsmeddP8Plzw1ihOnUqih7Sc7I2jz5c3nWrPRmEyL5STqqQV3WMPJkENCtH3pLLTxc3F-7-N9Aeu1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/19a38b8192.mp4?token=InCcFscUl-Gnr0uK58jvxPuurowsZ7Wait5Uh_fueqVkH1gtNAWl_psDZ9qaEmiZSy5-v9Lcf6dwbQVaetXrLz9CqhvG8ciLO-3RpU427T8vZ2sIqmLZezyP_8MoRVCJNDJKAqJ-KZP5iyDxDLoDB4Z_jcz3JlBqvCgNQXz9EuzuPyEiuVQ6mV5me6nldn1XzPmXCf08PKHFA9Ih43lP_-5byUwWCJpnsMzFaB5I9tBvai94ItV7qAi-8gGoeQOp78eM-KICNsmeddP8Plzw1ihOnUqih7Sc7I2jz5c3nWrPRmEyL5STqqQV3WMPJkENCtH3pLLTxc3F-7-N9Aeu1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
توی آلمان یه دختر تریان (انسان‌های که فکر می‌کنن حیوانن) به یه خانم حمله می‌کنه و گازش می‌گیره، به پلیس اطلاع داده شد، هر چقدر از دختر اسم و فامیل پرسیدن فقط پارس کرد، پلیس هم اون رو برد مرکز نگهداری از حیوانات
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/106970" target="_blank">📅 21:20 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106969">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AVN7ZFOY60XYLppjqR8jBSqD45bIiwxoicYSPP7P7nf-G6p8d9YmMZ7dUfT9RxzqyldgBQcGDMpThxVrh_HhnSENO82vl5CpFDQPDivY-5PmpO8iW7DzE4q1L19dfPXk0mLO-zPHF889qLLdUPFnrLevrikvPNdsearaoUqhFUpMubt-nOAzfpTWZ0gajqbZa-7VbGXFeNvxBqpZKx1JAnPtSyNp2EeDU_4K8L9UKLfYSzkS8yAnniXwj1rQLFMCySQR308OG1afuyTkcTieU3uZ14U90dQm9KQXlyA7DvvGv7OPhgeecictrgaqUxlN5YFw08Rif0w-uqs7V35-4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مورینیو در ۱۶ فوریه ۲۰۲۶ که مربی بنفیکا بود:
تو یادداشت داور نوشته شده بود که شوامنی، کارراس و هویسن نباید کارت زرد بگیرن، چون بازی برگشت رو از دست می‌دادن! من خودم سرمربی رئال مادرید بودم، واسه همین خوب می‌دونم اونجا اوضاع چطوری پیش میره.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/106969" target="_blank">📅 21:04 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106968">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qh32ypLj425u0cgrpaMUtV5og-XS4Gd1u0xe2mw_sM984d1xICHCtyLTh85WtLbNB4nRuBYkowvHXa7vDgVRJddy0UNh_nE1wm6PwvYHfGjpqy6z1JBpHV2xQdWqJThPwOgcd5hviEQniT70xWcN5HxUdVDC9pRvLZ8BAemRzLwGvYs8DGNAvGDvFAKPtVTvkYT5FwCQqCVsxFwoAsQ80g_d-wa1vR7W350rZaKRo6le7BBPk71x1YcDajJ11BjBJJK_wnYS2BZudz5AVcB8YkoEKqWcoc3Ll95VpGcxSZ2sD3ldKftl7jrX3xwra3K7UDmCFbr4rn_Lok5oT4lC8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
📊
🏴󠁧󠁢󠁥󠁮󠁧󠁿
نتایج درخشان منچستریونایتد در پریمیرلیگ؛ عجب کسشری شدن بعد فرگوسن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/106968" target="_blank">📅 20:58 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106967">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b23f273f1.mp4?token=OWSgxmKYVCguHvfApVI9QfPXy7K0ZdCwfa9V6UY-IrKou2OdnliF8lELe18GGU5iVhBGKYcOMZPipJsO01S_C43dpvEeT1CSiQOE91m4fA1UtyeN89SkeBsStzZgZe97L6lwX0zsInRsDTiFAnWjIe9viA8SsA8fglOg1h7vnZC1qAIZutlaLjA_eQ7OT2x4H2qInvPPVWAKB9VrQZAZWvE4U4sgi401tL1A_UflLl_GE304UY8RMaNxFfkE_PiSbueljB4_GxMPHrcyBiMIQ2GpSuJZUAiX8D8TFJUjwQ56vrPFvU-9wVR3ryKWjqMdqw7LedYXWW1lD4mruaGtww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b23f273f1.mp4?token=OWSgxmKYVCguHvfApVI9QfPXy7K0ZdCwfa9V6UY-IrKou2OdnliF8lELe18GGU5iVhBGKYcOMZPipJsO01S_C43dpvEeT1CSiQOE91m4fA1UtyeN89SkeBsStzZgZe97L6lwX0zsInRsDTiFAnWjIe9viA8SsA8fglOg1h7vnZC1qAIZutlaLjA_eQ7OT2x4H2qInvPPVWAKB9VrQZAZWvE4U4sgi401tL1A_UflLl_GE304UY8RMaNxFfkE_PiSbueljB4_GxMPHrcyBiMIQ2GpSuJZUAiX8D8TFJUjwQ56vrPFvU-9wVR3ryKWjqMdqw7LedYXWW1lD4mruaGtww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل اول منچستریونایتد به فولام توسط متئوس کونیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/106967" target="_blank">📅 20:49 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106966">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kghxmY5iStH4jZjkWZWl8pZiNmtHEjgcqreSOxbdy3jT4vMKnA3SENDBWmh1YZAgIBzGSkWR2tbH7zS8W5rFXHEpYILd6PGqa4vU7uuURHjXpcTVzrxxGeteK59L0JPf4LqfKzDKjtp9wIcUwuYpVa-OygyKfqFQ1xotDa8kOSTM3qLSQITwhfB7EPsztxKOvpH_HA_su_lzwG6RE4WJeEFZ6GMDTqOeCW54J6yT3WTfgVR-1N9pVctd_f7MOvlnHZ31FKMCpYhTE_MVwiwScLRbEt061E3JPDwk5v2yjnCrf6siALw2hkwBZuEwu8i1qgjjb18ohiDYJovG4Rpmfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
‼️
🇪🇸
رئال مادرید Tv:
🔹
وقتی پای رئال مادرید وسط میاد، برخوردها کاملاً متفاوته.
🔹
لالیگا و فدراسیون فوتبال اسپانیا اجازه نمی‌دن رئال مادرید رقابت کنه... اون‌ها یه نقشه و برنامه از قبل طراحی‌شده دارن.
🔹
دیدن همه این جریان‌ها حالت تهوع به آدم میده... اصلاً براتون مهم نیست که کثافت و مزخرفات تمام لالیگای خاویر تباس رو برداشته.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/106966" target="_blank">📅 20:40 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106965">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/34da8be998.mp4?token=dj3tIGBvB7kbjatfIbYEgbu6euQDgvMKrbfmbO1BMckjN7lzY9HWaA0ICNHCaPjZlzZNI4hefsWRrPqdTfD15ttjCQCZGN1WF5sHknuwY573xnMR4dIzGmWFPzRljB3pH8bJBotyGmP6G_n887c9C54xX1Z-EFqOtr2NJLInfXe63zeTGPPIIgOgZKJvRlPXCQ2CSoDyVZInb8ZVLHkRuT7p8boYVFMfCsbooBeWGElINzFK-ivw0MHUF9MA6T8i6fP0fH662L1bsrWjkkkrco2967X0nSqOtLxUIJwZ4rkx1u35Lzel028QDXUzulhZQy_vgDmL8cHEZP8azICptQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/34da8be998.mp4?token=dj3tIGBvB7kbjatfIbYEgbu6euQDgvMKrbfmbO1BMckjN7lzY9HWaA0ICNHCaPjZlzZNI4hefsWRrPqdTfD15ttjCQCZGN1WF5sHknuwY573xnMR4dIzGmWFPzRljB3pH8bJBotyGmP6G_n887c9C54xX1Z-EFqOtr2NJLInfXe63zeTGPPIIgOgZKJvRlPXCQ2CSoDyVZInb8ZVLHkRuT7p8boYVFMfCsbooBeWGElINzFK-ivw0MHUF9MA6T8i6fP0fH662L1bsrWjkkkrco2967X0nSqOtLxUIJwZ4rkx1u35Lzel028QDXUzulhZQy_vgDmL8cHEZP8azICptQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
حالا که بحث جنگ دوباره داغ شده؛
اگه تو آسمون یه جنگنده دیدید، سعی نکنید بهش شلیک کنید یا سمتش سنگ پرت کنید، فقط این فن استاد رو بزنید تا خود به خود به آشیانه‌ش برگرده :
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/106965" target="_blank">📅 20:35 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106964">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/5cd75fe80e.mp4?token=X3isTsXjAh9FXdZO55seNUv3uyNvJpKwYrfMFfBJpn4BZfFKhlkfVgUAzkP4pwrY4uDocwU3YUX_GQTcQLvRlSSDMSkoVVVaTf0vkqbIKiH8uqVtTud_hOYVcjuxSBHctih70WqyuJ8HWoi-YLEMGS8P9OXthdFhIcQ29b0aCDGdNbUe2ajqJRxJBtRyOe4VTJcjOi604jnwU04QIbDL9YR0P-qqlnMMCyV5SgQU7SO9mhgVEEgQHdTBGHvblWE2-jXwiwtKoVbzN3jkPQMnZhmEolQssjpwcGuwR6y3__ykMZXB9rWcL19ftBznaJPRwfFBosOq2TWY0eQLaeHafWYZacMUMRpEOz5tDVbaHdsGx1D8OLtCFA0H86GkA2i6tO9UM0qNRJkbTY78BfF0a8IdpgMRed1VOssUd1sBCtcJRBikJ2gRo9133MBPcGTSVlyECAc0tjJYuzbHVd8slK4v2J8Ex2TzD1WW8C9jg5MTGZVtIUTAjPRUH4fk_Ag5Kcde3_FPQd77FyqGAWjfch7G1sk9SEU_UsFXNqGlY9jlgapc-eI5rxr92R4uCkO7XQMiSOZMehbHLCENk4tMZveZxWTy2TTHQXr8oJBDZUFcUE0E9o8S8o4Kx5L7TXsPtgAXfCMsKqnIy8pyIfLCXcKkoOgPml02xTQFZrSZrZA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/5cd75fe80e.mp4?token=X3isTsXjAh9FXdZO55seNUv3uyNvJpKwYrfMFfBJpn4BZfFKhlkfVgUAzkP4pwrY4uDocwU3YUX_GQTcQLvRlSSDMSkoVVVaTf0vkqbIKiH8uqVtTud_hOYVcjuxSBHctih70WqyuJ8HWoi-YLEMGS8P9OXthdFhIcQ29b0aCDGdNbUe2ajqJRxJBtRyOe4VTJcjOi604jnwU04QIbDL9YR0P-qqlnMMCyV5SgQU7SO9mhgVEEgQHdTBGHvblWE2-jXwiwtKoVbzN3jkPQMnZhmEolQssjpwcGuwR6y3__ykMZXB9rWcL19ftBznaJPRwfFBosOq2TWY0eQLaeHafWYZacMUMRpEOz5tDVbaHdsGx1D8OLtCFA0H86GkA2i6tO9UM0qNRJkbTY78BfF0a8IdpgMRed1VOssUd1sBCtcJRBikJ2gRo9133MBPcGTSVlyECAc0tjJYuzbHVd8slK4v2J8Ex2TzD1WW8C9jg5MTGZVtIUTAjPRUH4fk_Ag5Kcde3_FPQd77FyqGAWjfch7G1sk9SEU_UsFXNqGlY9jlgapc-eI5rxr92R4uCkO7XQMiSOZMehbHLCENk4tMZveZxWTy2TTHQXr8oJBDZUFcUE0E9o8S8o4Kx5L7TXsPtgAXfCMsKqnIy8pyIfLCXcKkoOgPml02xTQFZrSZrZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
گل‌اول فولام به منچستریونایتد با گل‌بخودی لیساندرو مارتینز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/106964" target="_blank">📅 20:22 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106963">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KyjIsSWkrT8MEemGwQtXUPgiMsDvlJCbpg8LJ5-BAr-6PvAp9hhgLOUoSQDmwS72x-2WjFibeT5TnXWLYzWpyIp1x8_umqc9FW58Ay3owzbIb5CfvV-GOvCGkwLAyMWogNJdnw7qajNArEbHDmnryJ3Ew_-I-hhk5eEuU7U6CT4YAyK9P-Z-qJzmqdq5dQhyWE3MdRoJ31ZmuEsKFtV8twgxh7BeMxtCxqqcKU6nYhZBxNRv8thxNAlpSKyguXIvBAk6y_ZwriUQnUGTvqjG5hKAQbRcZgFhkGZ9zrPgcGSuTLvfjbVsMiGFyQlR6P-obSeUNsWWg8jN8OF811w_1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇪🇸
خوزه مورینیو
: به کمیته داوران تبریک می‌گویم. آن‌ها باید از این نتیجه بسیار راضی باشند. همه‌چیز بسیار عجیب بود. بازی باید ۱۱ در برابر ۹ دنبال می‌شد؛ چرا که اتلتیکو از دریافت دو کارت قرمزِ مسلم قسر در رفت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/106963" target="_blank">📅 20:20 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106962">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IKDFhWimLVqIUDHWeV4bZD6VGJwOWbw_Yf6gXzVoDKYwEydsyWm-mzoVX_B4d_OtLSCUnEwcdJlAgRl7HtAC-jkthzpjeGHopFhmnCp5toEw3sfbWSw37TYTUaLkganb0LmL_FLwIHX2VmYHBI-6lXZIke7WFbEVMd-MdOqIBvTLfqn1fDvkms6kBo38A-XKU1Usd30U_2dtznhUF438TYrLjgnVPkftDXhmvfMyswT-7NLsCNzqq-dG6HkP1kGVnVNTpTNgBE7dDKNYsMJ6q92yQSOw6B2C57LSOrdCaAYPtKPGqzISTAlFt4s_6NHhcl56wvssOGD3-Y8vfZLLyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
‼️
🇪🇸
کانال رسمی رئال مادرید:
اورتیز آریاس داور بازی، رفیقِ لامین یاماله…
😆
😆
😆
😆
😆
😆
😆
😆
😆
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/106962" target="_blank">📅 19:53 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106961">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y9TyQCgZqag6oAxE0aD3izFTCA0EEQKkgMCfX7GVFkLkIgY5dJbnxNa872W4qHQ9if1HcH5AibvpPsfDfoWt8Y3hOjRcI_Ct8dJH6pXYh2PNiQRIXVeJuhEPntoP-f7tOj276oZscL4MpUVXwsns2SB1Gm2bEb1-muvbsbyZFj9XmKnCrGtsKVgVzjKFM5_GVkoo05KQIDWZU4MvodTaA21cYu6lK8QG1jahSDhMNnZb1pTsYcqiog6adi63qL_YacXqe4nW9F4_rGXfdVyH54AOycmZ-IPNCSPdDLKPPTt487FYep_tAdf62XkTEWaGZekxbcZJZl__gMgboOpL7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
هفته‌هفتم لالیگا؛ دربی مادرید به سود بارسلونا شد؛ رئال بازهم شکست خورد و فاصله تیم مورینیو و فلیک به ۶ امتیاز رسید!
🇪🇸
رئال‌مادرید
😃
-
😀
اتلتیکومادرید
🇪🇸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/106961" target="_blank">📅 19:51 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106960">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f3b_VN5d_ii3YEkXqhCOtjtwdk4Yvu2A4H_HX1aPIgW1Rjj0W_-A0knz7gdkLGaTi928fEU42-MmyZXx_oM7dAVdv96qmzz0Psv2dVIqnuQXVRzIRci-MuMqyu0mfLAjMxwiR77OuUZV9xTNhKwSekX6ybZRhrnSvLdj8ePmvdxs_CvjRKng7ibg28vjDOtoPhZTum2N4WcgecwRQ3bb8Oc7EvtWBkOJlwsgGadC-ucIQA2DjFE5hpn-ZQGde81uc2ui8aBF6ZJQAXN6xtpoE8yXPMOXwPX6z0MrryETDi6elqTXT_TSDP2CidI1JXUto6QDFdp23pp4n6x0Fmi_hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
هفته‌هفتم لالیگا؛ دربی مادرید به سود بارسلونا شد؛ رئال بازهم شکست خورد و فاصله تیم مورینیو و فلیک به ۶ امتیاز رسید!
🇪🇸
رئال‌مادرید
😃
-
😀
اتلتیکومادرید
🇪🇸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/106960" target="_blank">📅 19:48 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106959">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aCjxrM6C20cGXVeLgtD2gL_8wVALYnYR1rChDrFSMnpG191zveL9KXUEfQoVwTyGfAfvNIOPUk-ZSst1xCVGpPXTQWYx9nV2JnidqJHYa-0KzEEuQxR7-DygCohT0mTALg2CGSGVXOrgvs7dj4FvaQ1z_Y8krrcNb3KJWFJ2kA0cfJnmXfcUuttbluUcDsSwoRrq8r25_4S_dV6c3Og00wbEfPvEqY83A9abm46UqGunzOx3cs_oIQqBDZBivOBXxRTfF4hnkdNoahuSY7zbY1vgxS9MqYODfMmijpt8vujAF6YqtzYzQ4gWeMAi8b-0Z82kXT-tsNbEGSmTh20Mnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
هفته‌هفتم لالیگا؛ دربی مادرید به سود بارسلونا شد؛ رئال بازهم شکست خورد و فاصله تیم مورینیو و فلیک به ۶ امتیاز رسید!
🇪🇸
رئال‌مادرید
😃
-
😀
اتلتیکومادرید
🇪🇸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/106959" target="_blank">📅 19:45 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106958">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">۶ دقیقه وقت اضافهههههه</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/106958" target="_blank">📅 19:40 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106957">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">دقیقه ۸۹</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/106957" target="_blank">📅 19:39 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106956">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">رودیگررررررر</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/106956" target="_blank">📅 19:39 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106955">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">رئال یکی زددددد</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/106955" target="_blank">📅 19:39 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106954">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">گلگلگلگلگگلگل</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/106954" target="_blank">📅 19:39 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106953">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">یا حضرت عبااااااس چه توپی گرفت کورتوااااا</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/106953" target="_blank">📅 19:15 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106952">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">اتلتیکو دومییییییییی زددددد
🚨
🚨
🚨
🔥
🔥
🔥</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/106952" target="_blank">📅 19:09 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106951">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">گلگلگلگلگگلگلگلگل</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/106951" target="_blank">📅 19:09 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106950">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c7be2074ac.mp4?token=TG72Y5Dfgr90mu7LVtyqu4C-WorrulQI4uqQx4rLSHEu4TAKnGJH330VZzENqNtP5vY50dTr2ynS06CzRW16yVZjEFaTbFzwhQUtv5mgzlH74ie3l14pxc756rH7jE2jvbRJykekOdK7Qc_iaOTl78u204Ug6K22hDkzDU953kXxQzKEFQwKwsfFSuhdNsh3KuqXJ68bfldJxpI5YzXjN62hgpdnstkyElqpvBslotfsDKWBtJhJhzPZb00glGdGOdHr9HTdlgjgerhbLU1SzQ6qeHIsqhMjRO8t-QyPPq3Ij2QIa6cAwGbYVr0U4_3vBVVvEGEocODfqUvJdrbxCw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c7be2074ac.mp4?token=TG72Y5Dfgr90mu7LVtyqu4C-WorrulQI4uqQx4rLSHEu4TAKnGJH330VZzENqNtP5vY50dTr2ynS06CzRW16yVZjEFaTbFzwhQUtv5mgzlH74ie3l14pxc756rH7jE2jvbRJykekOdK7Qc_iaOTl78u204Ug6K22hDkzDU953kXxQzKEFQwKwsfFSuhdNsh3KuqXJ68bfldJxpI5YzXjN62hgpdnstkyElqpvBslotfsDKWBtJhJhzPZb00glGdGOdHr9HTdlgjgerhbLU1SzQ6qeHIsqhMjRO8t-QyPPq3Ij2QIa6cAwGbYVr0U4_3vBVVvEGEocODfqUvJdrbxCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇪🇸
گل‌اول اتلتیکومادرید توسط گریمالدو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/106950" target="_blank">📅 19:04 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106949">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">اتلتیکومادرید زدددددددددد
🔥
🔥
🔥
🔥
🔥</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/106949" target="_blank">📅 19:03 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106948">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">گلگلگگلگلگلگلگگاگلگاگاگاگگاگ</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/106948" target="_blank">📅 19:01 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106947">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">دین هویسن اخراججججججج شدددددد
🚨
🚨
🚨
🚨
🟥
🟥
🟥
🟥
🟥
🟥
🟥</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/106947" target="_blank">📅 19:01 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106946">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">پنالتی برای اتلتیکومادرید
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/106946" target="_blank">📅 18:59 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106945">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
🚨
🚨
‼️
🇪🇸
کانال رئال‌مادرید: وقتی داور طرفدار بارسلونا باشد، چنین اشتباهات خنده داری کاملا عمدی بوده و پرونده نگریرا رو بیش از قبل بزرگنمایی می‌کند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/106945" target="_blank">📅 18:50 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106944">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
🚨
🚨
احتمال اخراج مدافع اتلتیکومادرید</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/106944" target="_blank">📅 18:47 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106943">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mFjCg3MRPFQA-XZYsmyzkNhAXjx_NPyD9i8IbKAAC8vj2SEGxv3A_Qa2iG0I_MgODdcU1PtaIHP4EawDiStXPwAR-ioZQLwZdTXfJ9dCkywK3dPcpBs-v30THcB2Ywu7-ArPnzGe8wDi7FhDIlnIZqgIKGdSKMlAAqqfSyyl52MOEOlX0Zn7oUXdH-gKpNWwqkLschzWWjgrXoIaWtJPaWSUspfHXoiuVf33XsZluYkBe6y5doskT4Rh4tKDnbadxc3lH4HsWygF_66xZaAPuP-2jqoDOzKHDnvy3JeeN3_KvzB2wwTJdWljbgg3kjwUktJ006FPz8LkeTH0j8XzkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
احتمال اخراج مدافع اتلتیکومادرید</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/106943" target="_blank">📅 18:40 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106942">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JV71cQYXwXjXfbms3096YhIfW0lSzWRJrJGhbOGJmHw8y9G1lUOxIxGQSGae8vO5M4VeuXzq8szkmHbcZyRfaFxX6OlkkK2bptcyWlwrDueTaSktTzPABYeeMK9vyTML989HWIfDAMp7prVcwnaEnN4RTRsZF3AGb6Nmrxa8cDdQBv0FXhFmdCISipXzxkwOm1IbF3-dNosVfq_MJTvVh5yCsS7XHDctQdBxgvJ86qDnHb63oUnTA0V-ynrra0d3EMu-EhRE8ncr3luIDCC6f9eIiNUtlBNaws81FdvOCn5wiAwunRIxlOciaklGguoZ6Q9wa3zRlSZQ59CPzN9Rtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
📊
🏴󠁧󠁢󠁥󠁮󠁧󠁿
با گلزنی به ساندرلند؛ ارلینگ هالند اکنون مقابل تمام تیم‌های پریمیرلیگ که تا به حال با آن‌ها رو به رو شده، گلزنی کرده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/106942" target="_blank">📅 18:27 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106941">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
🚨
🚨
احتمال اخراج مدافع اتلتیکومادرید</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/106941" target="_blank">📅 18:25 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106940">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/brDLFZi19NhunRRJFDe1I_o9K5C2UjOloB4OA67F8Hf6ciAEDRPocmkj89nZaadKbziBJJplgENoznDReR484PL2wmJuFMfXKGch8u9H8p75QUZstTajUK4rlJlzzWyy_1qQGQxy2tw_0DzRcrFBk4tvqp_jodkolJqkiwebhnnfPxLmh-MbZvAlDZ4jSGCZgLKpHxTpD4e0mjUNCNK-E5nBf1vPoy2J_yNCeLBwjxjnBdKHsgyW2V33hhaUImAWH8GPBcXMtnv73Uv5TcIOLJdhp5g1sTa5wGw-268czx4Mc928WRp3M0-xxvJj9MeLZE6iGspHqCLCgSApU4HqmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
احتمال اخراج مدافع اتلتیکومادرید</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/106940" target="_blank">📅 18:23 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106939">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">اتلتیکومادرید دقایقی هست رئالو لوله کرده
😐</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/106939" target="_blank">📅 18:08 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106938">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZFIrSFwUQoJaufZWoj0lIfYccfGJ9jNYzCDulVU6JNCvjWfDp42QRWOQx54eBe6LZdK8CUPDqN0qmrJOG7HDnsjGQk-JFzJ2SMnxM2Dtbe1qAlqK3Ppgu41q86Fr6rVekfL_aeplsDyBvNLaOkEs5Hv0hGqkt3PamZRIyfcPrQACbN7xZ-bFeZuNy_wRfpgGOmos-SVDMZXQ8BeFOUBZHe35hBtkzeKkgRr4E_rK96t-TfCIn_8_ATWTGzKFBdDvrLn8GpUESA-UZFMzAHAGxM0hI4hKHHsKJEKN_lw6PwkeKspH16eI_EsFMvI977YCfEtdUfZnyOMrJStD2A_R6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🚑
براساس معاینات اولیه، کریستنسن به مدت حداقل ۴ هفته از میادین دور خواهد بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/106938" target="_blank">📅 17:57 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106937">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/787e254f6d.mp4?token=H-HFsMyJlW3NyXK_AQ_UJkH4jIm-N4VmhGaVqlV1krNsu2lAxlF1Qs7q1zTixqgM2j3DC_zjKOqFvX4Y9uA68WZgS8yQDHqZeA8bDiZb7ullhnfqKN-tMDL4hXa16StA04VeInMVT1glA6OcseiF617tH5QQEtiNJrI1YmD6IG-b0T3w8WDwrKHAy_mKqQ1ihqwmjGfSvS_5fBuNsDmD7hNz6IkVQm2J7YEy2X_WaP3BpyvJQsUyFRUnoK70PW5rvYui75Wwb8aD9Pvc0NjWjDl_xB-4g9PZVmQ8pzKpAUrGTFmSYzOO0a03b4mTPB3YSCg-Eau_mJBhvpo9FIZeMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/787e254f6d.mp4?token=H-HFsMyJlW3NyXK_AQ_UJkH4jIm-N4VmhGaVqlV1krNsu2lAxlF1Qs7q1zTixqgM2j3DC_zjKOqFvX4Y9uA68WZgS8yQDHqZeA8bDiZb7ullhnfqKN-tMDL4hXa16StA04VeInMVT1glA6OcseiF617tH5QQEtiNJrI1YmD6IG-b0T3w8WDwrKHAy_mKqQ1ihqwmjGfSvS_5fBuNsDmD7hNz6IkVQm2J7YEy2X_WaP3BpyvJQsUyFRUnoK70PW5rvYui75Wwb8aD9Pvc0NjWjDl_xB-4g9PZVmQ8pzKpAUrGTFmSYzOO0a03b4mTPB3YSCg-Eau_mJBhvpo9FIZeMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
🏆
پیک‌زدن هری‌کین به سلامتی توپ‌طلا احتمالی‌ش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/106937" target="_blank">📅 17:51 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106936">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/106936" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/106936" target="_blank">📅 17:50 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106935">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QrB_VLCGDnZ0Kp4uzaHL3KR1b0fWKg-haGlyf9edGzGszsy0oqXxr1MfA6tJt7oDHuGKVh_sSJE9qpX1t_skLi5fUf4S9AmciyTLur7cqsPUVWdyPLAt8hkTN6VUVveBIKlF_zOGNbAJdIMrTWitSHnRE6YjP9FkbC5wn7ECd3k3EdKJL-4HHjCUnjoApBe2hOBVQHHalfJhNYxsLICAwZKGN1AIV_MH2LzmLSvxowa_1JXQrsUu2GHl82EaJ3fNQ3NoGnhkAXg1wIHA2JwknGmWZ8cVliF48ihXRulS09I1iybURstWDw1PrHDZGaGPoGId97pSNzSAlpH669eK5A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/106935" target="_blank">📅 17:50 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106934">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">برررررریم سراغ دربی حساس مادریددددد</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/Futball180TV/106934" target="_blank">📅 17:46 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106932">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u46NjaSyhYWTsfzfpaoiWew_2VLPuUhfyV73MnRTXg3TB9BwSPs6B2cAdJmH67C_ET44NzDV1fsv9ZHc3Z7tvVaftbp3WDkFpOhS-BrV9_8SrDoOUzfcerCYcIybs6PZ7RXQQcw85LxNmXan4rkxmOCEpx6g5ttLUad5PB1NWFeT9aROp9YRrik9SAB4tnbituH_EB9xd0t3HSa2w6x3G72BVQbSoRD-Fa8t9EoWHwWEijDkul6vfZVlPUXakgkVtd8cd47Zj0BP42Slgo6pMEnDuE8aOCfIyQDjyQwVkSU9nNC0q9_vkASq29KoUDfcVN0bE55elV5okbKd6SLmsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vhV3KKWvIln2XvnymP5wvK3W6_tjfpfFjRbHT3HUgBaVky_RNB3RTLgZuFwN9h8tNATSObo8dKRLveXaAEroZY7g8CIVJEEfEjB5BhXPG8vXiAN8eN1VVM-1bqJy1murh6WNtmnyqIrnmvAaby_YTkLCYUMKf76AAHeHAAshZAAQ64V6wNDbW5BJj2ntoSQxZkkA2UDqJzZkZdnsLDVO9vEZXo9Z9HHZVgCtvi49lUuUlKEN_yWQuZsObPZAS4AzzWBooTyxvVETAwvCujy_5A96S7lHYG1K1mGt8tOmXwvpzcISiFsgWLSbcNxsJOQo4jLNC639FpCN15KOWmrTqQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
🇪🇸
ترکیب دو تیم رئال مادرید و اتلتیکو مادرید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/106932" target="_blank">📅 16:52 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106931">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0c42dce9e.mp4?token=fZaSs0GoahiUdKUfBBhWGsWDX3hAA8z3n7nlUq4nFLgGcruvlf4xJNDhwmEkiQPr5l82059uzJAQitSb5TLY25A0DsMxvH5aU4J2ejsf2w3CvFF9R3naWdRwG5XC4PzKIwNcyGQAfGMEiqY_oKH8_50BTcmc5zEVyTOL51gtGC9G_3_ZZEMuQLO0iZiiINJJXHCiUCMVOoDbueIgny_MEl7rXMU58LAdhJuCs3qDkpJ6zXw2J1JCq01eI0maR1uq-J8PXLR1kXnuC9dDxPzR3WIFp43wWldtPzGABEYHwC7XdNFzhYVHHFvgUULDTzUp4-_rr84qERc2fdAKiYbP8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0c42dce9e.mp4?token=fZaSs0GoahiUdKUfBBhWGsWDX3hAA8z3n7nlUq4nFLgGcruvlf4xJNDhwmEkiQPr5l82059uzJAQitSb5TLY25A0DsMxvH5aU4J2ejsf2w3CvFF9R3naWdRwG5XC4PzKIwNcyGQAfGMEiqY_oKH8_50BTcmc5zEVyTOL51gtGC9G_3_ZZEMuQLO0iZiiINJJXHCiUCMVOoDbueIgny_MEl7rXMU58LAdhJuCs3qDkpJ6zXw2J1JCq01eI0maR1uq-J8PXLR1kXnuC9dDxPzR3WIFp43wWldtPzGABEYHwC7XdNFzhYVHHFvgUULDTzUp4-_rr84qERc2fdAKiYbP8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇹
دوباره از ایتالیا صدای گرگ میاد.
🔥
🐺
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/106931" target="_blank">📅 16:19 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106930">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27b89b6e77.mp4?token=XGzoTywN1DychMyle2ekx9UI3RYquoNQozepl2R7FMMaxBxSWVXhgKeJyqTBkRtbYUA6slg74Kj0rUQB_s0mlzukH5zSwHc360XW5bf6tl1FDg60SGfFlTm5Nz3okCLJ3fn4ZTIOaO29z9jd-Z43oVZwpTB4UCQEjnyaaNmP6R0ARjIEWgEW71nDTJgF1_WT5HnPZU75eOVERDB2BGXL-qt4B5XtY3loF9eKYHq5Hkj3VIz4GIpwLYDmjoUGnm17CFOGJZKe99oCTuzf47t9XYI3z_ubHSbRxsBkkar0fofg7tIoVxj1XMP-cwlTrMKwaKFhfu8N9OmchFCUJ5yqUIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27b89b6e77.mp4?token=XGzoTywN1DychMyle2ekx9UI3RYquoNQozepl2R7FMMaxBxSWVXhgKeJyqTBkRtbYUA6slg74Kj0rUQB_s0mlzukH5zSwHc360XW5bf6tl1FDg60SGfFlTm5Nz3okCLJ3fn4ZTIOaO29z9jd-Z43oVZwpTB4UCQEjnyaaNmP6R0ARjIEWgEW71nDTJgF1_WT5HnPZU75eOVERDB2BGXL-qt4B5XtY3loF9eKYHq5Hkj3VIz4GIpwLYDmjoUGnm17CFOGJZKe99oCTuzf47t9XYI3z_ubHSbRxsBkkar0fofg7tIoVxj1XMP-cwlTrMKwaKFhfu8N9OmchFCUJ5yqUIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
👍
بغض ایراندوست از طلسمی که شکست
پدر و خواهران مریم ایراندوست در ورزشگاه، برای اولین‌بار؛ خانواده‌ای که بالاخره برای یک بازی زنان دور هم جمع شدند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/106930" target="_blank">📅 15:28 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106929">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e67d6e531.mp4?token=gjtCQ_OLF05c_mBqdtt97ve9jFEKoanH3dANdgOFGb6jkyWjk19XXFgcYeCf2Em7mLhVupii_YepIZuHSy-tA3Lnt19adkRmbEQ2iYbRVqFu5PY6Kf13O41A_uH0M14yGGA6g6_nM-njAzYUe8wIfmOCqkgpvSl4HW8S8aX-qz6J_gMzItt6sQnbZYs5_pjQd97AQzLrXzz39Q1l-WJtO-qGPZf-qIMMU5nQ-yWg3TdvffmkLHBypjTMIcc56tHqePA91JdYZCPF-XxchOYy2RYLHZUbm6NWemdmlnS6DMcfawsFG1Wk2QH6aE1sgHZyjdrEOEx3IklInXpkr_DEZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e67d6e531.mp4?token=gjtCQ_OLF05c_mBqdtt97ve9jFEKoanH3dANdgOFGb6jkyWjk19XXFgcYeCf2Em7mLhVupii_YepIZuHSy-tA3Lnt19adkRmbEQ2iYbRVqFu5PY6Kf13O41A_uH0M14yGGA6g6_nM-njAzYUe8wIfmOCqkgpvSl4HW8S8aX-qz6J_gMzItt6sQnbZYs5_pjQd97AQzLrXzz39Q1l-WJtO-qGPZf-qIMMU5nQ-yWg3TdvffmkLHBypjTMIcc56tHqePA91JdYZCPF-XxchOYy2RYLHZUbm6NWemdmlnS6DMcfawsFG1Wk2QH6aE1sgHZyjdrEOEx3IklInXpkr_DEZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🎙
🇮🇷
فرشید اسماعیلی: یک‌زمانی در زمان رویانیان در آستانه حضور در پرسپولیس بودم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/106929" target="_blank">📅 14:49 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106928">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P15GtKUD0HvUTmdzT7M4lIOTGksS0bRRBCgSCO7L9eEsAWfSanO5fVOIWJHcsrk-ej_vkqaIhftDkpmRMBMApe8T9ayU7biIp52qhXLOqCYSk7f6f_0mzsIsdk9xRMWnKhdDkOyAOwJSViD4ZYgZOWkah1PcADqWOr32DGsheuEIVZa5lg0iFO_i08emMAwcLzDn2hZvObaw_Du2zR7wSJ3XBect9wkTUHrlWNRD9EeAz72PAOKXT7NshBD4n-INXFHl8pvPdOusmP7taJGGH1kKR1C6WQn_DUiQLohfYQKLZM7qie6IyGj39Z1LgnBGpNB7QpjVLVeSrYfzB6s54g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایشون زید دیومانده هستن
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/106928" target="_blank">📅 13:08 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106927">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db2519e30b.mp4?token=da8d3v96i-BqEkJ720BYgMumeaaRhTLXCaFnyge-UO83c1nUtN85DbuFMQgUjCVFxweq5Bke0Paz0rt3vwO0ZW7nhTjoabKgPkuc-bOPjxnQW-aJyls6tKJmVijqczMArbUBeGAkj6-tXXEjdIlER_Vr5GXKcfW9EbWbpngkJCI23bP9IRSIA5aVyuFuOHM5d06wkRnC0BoAOqgBdmzGaN3U9NdhMbwWl0N-_zCDVAf-875v09FQwIxEu2X1tzh2wS8FAS1ytyB1DSCnMMf_FdBRyOR5Df4Y7hInxs6z8JIGcrZ1gNxLmHkAqsxtIab1P-HrxhdlT1Xa7q1iHfbLbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db2519e30b.mp4?token=da8d3v96i-BqEkJ720BYgMumeaaRhTLXCaFnyge-UO83c1nUtN85DbuFMQgUjCVFxweq5Bke0Paz0rt3vwO0ZW7nhTjoabKgPkuc-bOPjxnQW-aJyls6tKJmVijqczMArbUBeGAkj6-tXXEjdIlER_Vr5GXKcfW9EbWbpngkJCI23bP9IRSIA5aVyuFuOHM5d06wkRnC0BoAOqgBdmzGaN3U9NdhMbwWl0N-_zCDVAf-875v09FQwIxEu2X1tzh2wS8FAS1ytyB1DSCnMMf_FdBRyOR5Df4Y7hInxs6z8JIGcrZ1gNxLmHkAqsxtIab1P-HrxhdlT1Xa7q1iHfbLbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
وضعیت رختکن چلسی بعد باخت جلو برنتفورد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/106927" target="_blank">📅 12:25 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106926">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3686f3655.mp4?token=qbss8vGBuWvP-Gqeiksi60Gbn1vRPr4ddQqvBqr_svdcSrbQ6hfKB4ZgECDdnE2PTtpf9sjp_hH7eOkSlSWk-6L2D1AQhRGR61JSPiyqVpNOliARosBkErVAb_KmTOMoaAPwXk0SatBJZwzZ8hnreSu7ook0Gemz67EBv4st3dju-nkCTOw0Nfc8O3hUO-NKjIc4LKTt-fhyrwJhct12R_gJEBnHwESJHaZ7fFSwq7UWe1qELXtCGNXUfiP7-ss6oFjyd3Po8OJUXQ97hJBaOUTAkuB8OGkQ1vfGtQsdATfCDAGG-fQmP-v48OlhbPKcSI0KgRbq8zKvuEd6HI9Fh5kpPgBP98T44vO54yvlQOixLIWDPH20obixz3ksGIvMYEK5dxQVuY97LWUmEK-pNW88lo7Qa5mY0IxSC09U95G53dSO1meRZvb1l2CkDTL0Dxr92lqB3JNXQkcDdaLDt99ppZXq5xGNjnhg7l3TI5ztL7xnzgGUne546AiqtyjAVbMYy2gYrbfA9FAhqKL4a33f9SbFzVlKiF2H-6pMlWUun4XW-dXsHHbfYLwrAu6ZHXgdr2i4J568gt1cVDoOdAkbuDICYcVquqUwaFdOEwpZ3wedxlbnCI2SgT8oX5u62OsOlSGB5Hqy6UdlCn39NsgMkTA1-HqDxf0H_lCn3ac" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3686f3655.mp4?token=qbss8vGBuWvP-Gqeiksi60Gbn1vRPr4ddQqvBqr_svdcSrbQ6hfKB4ZgECDdnE2PTtpf9sjp_hH7eOkSlSWk-6L2D1AQhRGR61JSPiyqVpNOliARosBkErVAb_KmTOMoaAPwXk0SatBJZwzZ8hnreSu7ook0Gemz67EBv4st3dju-nkCTOw0Nfc8O3hUO-NKjIc4LKTt-fhyrwJhct12R_gJEBnHwESJHaZ7fFSwq7UWe1qELXtCGNXUfiP7-ss6oFjyd3Po8OJUXQ97hJBaOUTAkuB8OGkQ1vfGtQsdATfCDAGG-fQmP-v48OlhbPKcSI0KgRbq8zKvuEd6HI9Fh5kpPgBP98T44vO54yvlQOixLIWDPH20obixz3ksGIvMYEK5dxQVuY97LWUmEK-pNW88lo7Qa5mY0IxSC09U95G53dSO1meRZvb1l2CkDTL0Dxr92lqB3JNXQkcDdaLDt99ppZXq5xGNjnhg7l3TI5ztL7xnzgGUne546AiqtyjAVbMYy2gYrbfA9FAhqKL4a33f9SbFzVlKiF2H-6pMlWUun4XW-dXsHHbfYLwrAu6ZHXgdr2i4J568gt1cVDoOdAkbuDICYcVquqUwaFdOEwpZ3wedxlbnCI2SgT8oX5u62OsOlSGB5Hqy6UdlCn39NsgMkTA1-HqDxf0H_lCn3ac" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
اقدام عجیب و جنجالی سیگار کشیدن مجید واشقانی با اردشیر رستمی در برنامه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/106926" target="_blank">📅 11:08 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106925">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J1S4Iw_slfXumC44s0F5NrewQFjcTfHDpRtFwEOHoVg7bYxOzAfroQ55pT2yJqcCiMFWyMnhb3HUG2btbfNXO3pOeZq-Miq8pGqsJTJ2xVzjCYKMxK6waqy5QqEsTI5Pax8gdO8nURWyaJpEAvsGHLuTwnpV8iBe6U1Tqv8MWxb_9EpOAcTd5lTn8CTNcTERZOo4CrBbTDn6uxfkCE5lRuoARt7aPTrEYOBcKyxpVxD0A9-W7UBkQ-ToqtB9szjPy1qXUCeZeNfZphBofM5J_JeRIXUO9DRUBS6ltynF00aB1T459Hcfr-aE1xTYUwkFZ2E4L_DtCzK7g9Kes6huGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
تیم‌ملی امید فوتبال ایران در دومین بازی از مرحله گروهی بازی‌های آسیایی برابر چین با تساوی بدون گل متوقف شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/106925" target="_blank">📅 10:24 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106924">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">📊
🏴󠁧󠁢󠁥󠁮󠁧󠁿
آنالیز متفاوت و جذاب از تاتنهام که برخلاف نتایجش، فوتبال نسبتا خوبی ارائه می‌کند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/106924" target="_blank">📅 09:42 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106923">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8fdf2bd4a2.mp4?token=Zp-rZZqH95z2nQYkdmfOm8Dla9FMCDSQXxguu5qZQVM-MCfy8Z94ZzLX4WlLKV_6c69y0aBZQMW9hEU7oREy5wYRFdXtzSarC_pq_gwM6sFzkSuNSKBnUBaoiIfEwGmcy1lg0JDyCYfiayVemh22C8D917pvUJKafICWcT4OXFgUVXWEamGnm24OrD8Us64dcrwBItGE4ihoyOouNexFomtwG4pqMPt1eUacmT7OfkawTUNP0DJ3a6JNy8YaM4kYStc5pu-9AQCQIxZVNX-eLaXYUyfZDVSzIakfMaYFseAk7xIT8dXWso25V3XmXWHeNJcNTgYhkCayljLJBvPOsDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8fdf2bd4a2.mp4?token=Zp-rZZqH95z2nQYkdmfOm8Dla9FMCDSQXxguu5qZQVM-MCfy8Z94ZzLX4WlLKV_6c69y0aBZQMW9hEU7oREy5wYRFdXtzSarC_pq_gwM6sFzkSuNSKBnUBaoiIfEwGmcy1lg0JDyCYfiayVemh22C8D917pvUJKafICWcT4OXFgUVXWEamGnm24OrD8Us64dcrwBItGE4ihoyOouNexFomtwG4pqMPt1eUacmT7OfkawTUNP0DJ3a6JNy8YaM4kYStc5pu-9AQCQIxZVNX-eLaXYUyfZDVSzIakfMaYFseAk7xIT8dXWso25V3XmXWHeNJcNTgYhkCayljLJBvPOsDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
😢
جوآنا ویتژیک ورزشکار ایتالیایی در مسابقات چین یهو وسط کار اسهال میشه و بی‌اختیار ازش خارج میشه اما با این وجود مسابقه رو ادامه میده و قهرمان میشه. در نهایت از مردم عذرخواهی کرده و گفته امتیازاتی که گرفته رو ازش صرف نظر میکنه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/106923" target="_blank">📅 09:34 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106920">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/571388041d.mp4?token=TL102K9Ne_jY632V16Tt8N1n5X0i_-14CuOtwrs8HPA6I-N-LbeCYozTeH5zEFcfMZdP4Ds19xLiEVPLm9zcuFQ03X3Ybs2W_BgthxOXSu5sXbFzc13HDU-z5aTb5AfaCAK3WmIFI0l4qOIw92xoAVp8JgVih1J2ByUbfn7z7RyXZ1ROSLX9ZGvo45_HVTZN4FssPCur5fyNwaliNMk1EU6vXCHa6-dwU584XAXyMOx5n28JcYj3v91ClIpTCkYRakbp94btoI2kqK5ALIWUGbFz89hB7uNgK9wUpbIm3Odg1HmB4Au875SOypRd9e3DeDruQ4Iip4mRQfO24gq_Ow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/571388041d.mp4?token=TL102K9Ne_jY632V16Tt8N1n5X0i_-14CuOtwrs8HPA6I-N-LbeCYozTeH5zEFcfMZdP4Ds19xLiEVPLm9zcuFQ03X3Ybs2W_BgthxOXSu5sXbFzc13HDU-z5aTb5AfaCAK3WmIFI0l4qOIw92xoAVp8JgVih1J2ByUbfn7z7RyXZ1ROSLX9ZGvo45_HVTZN4FssPCur5fyNwaliNMk1EU6vXCHa6-dwU584XAXyMOx5n28JcYj3v91ClIpTCkYRakbp94btoI2kqK5ALIWUGbFz89hB7uNgK9wUpbIm3Odg1HmB4Au875SOypRd9e3DeDruQ4Iip4mRQfO24gq_Ow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
🇪🇸
کار جدید حمید سحری از برد امشب بارسا: واقعا کی میخواد جلوی این بارسا رو بگیره؟
🥶
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/106920" target="_blank">📅 01:13 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106919">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rQ67J9NPNTJs0FXIXN4bcPyYokVpHlunRUWkGu-8JewZAx1ohXZ5GTS0NsZqnuGjWcPcJrWYEtZPTo_DwZgHXD_rWt5wTW0JLV5oeZ7wSRE4c3S2WI1tk8wcZG6jp5E_noP7vPT8kR0ML2U1T6K4JslDGZJmJzGiHJ51PKt-okZaJXOsC9h8UFzd9esd8xVq9b3_mNJry83qBs-DNoUnhCsqVXM1q_lD2Zsjmn9XMRIlZEYIe_2PgA3mv__Z4fBMheMIYByFiD790C07P8dFdTZhzPPl2f64-AQr-6QwEIo3dJIP_rtd1hyYqAdXX0qHKaVXzbNiqvLV2hrpBfHphg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🚑
براساس معاینات اولیه، کریستنسن به مدت حداقل ۴ هفته از میادین دور خواهد بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/106919" target="_blank">📅 01:10 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106918">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rIHdhtkIgpTUCCiO8r3h-xj0PNWFOV6I_qq0CvpUnpVS_3OmR0RLbKE5kx2xJQDDgWUc0H953iWoXAjb_n0q2_xS5__Kqg5rggYMSe6ew0KUZi2lPCZWGo_jpcuUVMtnH65clw43JJ14-lRycvKb2v1zev5so1refb9673KAc1Qs32K5lKQXQCngcVuRNIUOacecznPFQY9I6v9VlvgrbfJS_9WXYN-MLGwQH0YM_CNdjOIFgvIT--wkh8IcdANfMcnvTGKSALE83DnBDdLIWq47pB32wbAyAg-beSmqMQcFDV5341c1u_XvNAgrx1ncyWJScwMPS8yaKv0QZNXwzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🎙
🇪🇸
هانسی‌فلیک: شگفت‌زدگی بابت عملکرد رافینیا؟ بله من شگفت‌زده شدم اما نه امروز بلکه دو سال پیش و هنگام اولین تمرین با این بازیکن. او و لامین دو عنصر فوق‌العاده تیم ما هستند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/106918" target="_blank">📅 00:51 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106917">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RYTKYMJFli5KH4pJGgQNFkQjtBWKjSuCMkyTDNb0ylQI4o33zeZE2JAHELQwlx4-5gqkDDx6BdbqwWE9aw6SRd9x9Zu2nWIJctPf1erVUQ5hBrsR-wp0NsUbJB6hD5SrxQaIsWxOltRexl7liBGVLJwSfaYk79kjDeUtf3fa47XL9hEZ-l7VDLeanw5cxFCwoKluUBbSaoolnY2HOhV9ld_7BSR0JoASmxrEerKGmskdCCxERkWTr-bPWJeKB-vJQvv1-f0NXN0rVtQCY-11x51ToqEVZV55mZNF3wcX09wKZVz2B_U9a8Rl6kG4h8O3W6SD8HJ3nuNKW5K4K83fcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🇪🇸
عملکرد بارسلونا از شروع‌فصل تا امروز؛ بازی بعدی تیم وحشی فلیک ۲۰ روز دیگه مقابل ختافه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/106917" target="_blank">📅 00:49 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106916">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dlXw1hf8_Gsv1g9Oq1eCQ3V4uzYYYDGQ0a4HFsDoJEehMApqo9fXArRELezDd-lspPyB31dIQqWqL8auFT_rI1OVjY9oULdb-LEj-ytADYLyy_GwQe_F59QVRGqwHble1Te5RPFrlbuoAVwTFQ2tG8P-e4WNebekGCQM2gvbhLBBuW6GbtuY0E_RSFp90FAVlwXIraTQxCj_v75qE9YAFXt62QK0QHiOOWjST-QWG_x35IrRaviK1M358QAk-qv-rrx6u_14bizYBcbPKaYP1vXvyZHi67jRQWeAFuWM7Yji9oV2iNGAt9dROo-1owmmRCRDSdgiCrFFNb5JLoZW5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
✅
هفته‌هفتم لالیگا اسپانیا|یکه‌تازی غایب بزرگ بالندور در این‌فصل اروپا؛ بارسلونا با هتریک کاپیتان رافینیا در جهنم خانگی سویا برنده شد
🇪🇸
بارسلونا
😆
-
😃
سویا
🇪🇸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/106916" target="_blank">📅 00:40 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106915">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZBuxSbv4bYWH-YdOcCTttdEhrmnSvtOt3y68mg0XybkDVVpL8PCIyE_CHYuQz8mpYEYBHj3NEtX8SMHEJ2gwQkn7a2XEepn5U4kmrBJpCpIsCsIFfzSsfdicf5QWJnMbnomgogINakmRTPd7ZFRbzWJHzTKDtztBceZvsQ7ZB5FtuQse6FwA2wzMbE8dD1SKZagP1KHDu718cesKzcljPggIIkv_-0_4oPFxEtbY70zk3LWxEbdpE0vgBHNwTk3i83mGHSkhzrqVt_i5xz0bW_fcRpBNw8b5nSuqprRoLKfiezCzCKpgjMvYCPkeaT0YOpjDoxf4HJQ-x3BKUdwpDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😳
😳
😳
😳
🔥
🔥
🔥
🔥
🥶
🥶
🥶
🥶
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/106915" target="_blank">📅 00:27 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106914">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fkRPffW0ghEsZFgcr7v_Q5R8WFA3K_ZC1p55lxcdBu1j9BxOCDdJPHiH-qF0oZ59ofUaXlO_Ak-YPPVbYK1yO4Ksm7W12spU_PYoeiNZl8jRJ6nHgtB67rKGpSqnl5Svi1_eIVlaASu3r1Wl3aw3lE6js-Jp7qv6-zswGyrYztmASQsZDCJzTjlIACUDOpxJzHCVzcJv5lDQfFM8sMKFjEfS7aerndx4wFuqR7r0s7Lv-MKO2xer9Z5qAb3autqcCxrwDV6tLw9a-jG53dGgOl6p2YWMHKBhPh1jLWXtPcpoSva0kF6MrWtBDUf8YMTIvWOy-cOdbx9XHjJv37R94Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔥
📊
🇪🇸
رافینیا اولین بازیکن تاریخ بارسلونا شد که در ۸ بازی ابتدایی فصل موفق به ثبت ۱۴ گل شده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/106914" target="_blank">📅 00:11 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106913">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EYqFo29Bh2kyb21N_7cyseA_BZIhhRVTx4jD62VFJyA1ZcMYh3O9tp3yJoghgv4glBu8kY8F7drriGSoB7aJu-dcRnYBtunern6McCt9fF6kmapxXvFOAqguRWr_KMcWk03ylMhLmEVGjpo9dSYNqIRXDwBRW8lrB1qZXAbDD6fHyP0avLaWxc4EgEDxxwZVFTpu4S4H_1atFRnaNzlfLEmugH5VmW6SW2MCCxl_vuKaiQTyta5Cw7vLw58xpcI4rAHElDCxJB2X1poHRQnx33Q5lk61IH6Y7EsHa-27z3P8je3qBsXFamHg0Pc4s5CySNu3m9ZtAw66MHRG78Sseg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔥
📊
🇪🇸
رافینیا اولین بازیکن تاریخ بارسلونا شد که در ۸ بازی ابتدایی فصل موفق به ثبت ۱۴ گل شده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/106913" target="_blank">📅 00:07 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106912">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">چه پاس گلی یامال داد
😐
😐
😐
😐
😳
😳</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/106912" target="_blank">📅 00:03 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106911">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">چه چیپ سکسی زدددددددد
😐
😐
😐
😐
🔥</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/106911" target="_blank">📅 00:02 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106910">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">هتریک رافینیااااااااا
😐
😐
😐
😐
🔥</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/106910" target="_blank">📅 00:02 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106909">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">گلگلگلگگلگلگگلگلگلگلگ</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/106909" target="_blank">📅 00:02 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106908">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/2c2fc4a5c5.mp4?token=a_o24T3AGqxYP_DJ8K6Be8F86bcfRlrgWMZyLiWgh4ZktnTGozG-o-d4-6LekmuwI9cMvFjl_v5pt7czMjHzuc1Sei76HHmTkz6iBF0kJFhqcNFbbIOJ-ACVGYFSKe_1Yw-ucViPpl_HQQum2ftadCxZeuOj7nrOkeFjPBrQqp4XYUJ73uWU5wKRG_LSbh3AQNKfLShkFNTce-ZruGQIkNlMSJac2dJv7Klz_XW9wKyYsgPWGVVBEF-Z7DC6goeb-dTUVoRQPiSbA2Q9tkaX9TX3l7giFTBbLyXCsihVcKEOAp_3sqPzsDDfGmrVfVopEJXDvl7PRHH4KuFcMmbMNy8TTNEz_AdgThvBIZ4lhyt4F693RtwEALVUIMe7OiHVMafU8b-tR6sWSEHSj7H9mIV90IfY4uPXYfJeMoeXrTlIkm6blifVX1bmqCmiLg_yPNn3StRhpoC-OBUhMTZBeBa5ba5myllP7P7uL8DUHD6GEIrS1qNYudnGvunPXHxCYLx0-US4znK_EHV0xGjpPM4k6fwxnQjB3eJ84r951CAdqta33NQZ5um8j94tUci9b2CEFt7mPKVfhzM55Sg1OVTXyB1yc0LVRH_cLvv6a5xyQp6wfhFP7ED9ZMXPNRvtmmHc2EUrw6O46LocYGXSVjBHMtfTfJMp3-ISMiiJoYY" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/2c2fc4a5c5.mp4?token=a_o24T3AGqxYP_DJ8K6Be8F86bcfRlrgWMZyLiWgh4ZktnTGozG-o-d4-6LekmuwI9cMvFjl_v5pt7czMjHzuc1Sei76HHmTkz6iBF0kJFhqcNFbbIOJ-ACVGYFSKe_1Yw-ucViPpl_HQQum2ftadCxZeuOj7nrOkeFjPBrQqp4XYUJ73uWU5wKRG_LSbh3AQNKfLShkFNTce-ZruGQIkNlMSJac2dJv7Klz_XW9wKyYsgPWGVVBEF-Z7DC6goeb-dTUVoRQPiSbA2Q9tkaX9TX3l7giFTBbLyXCsihVcKEOAp_3sqPzsDDfGmrVfVopEJXDvl7PRHH4KuFcMmbMNy8TTNEz_AdgThvBIZ4lhyt4F693RtwEALVUIMe7OiHVMafU8b-tR6sWSEHSj7H9mIV90IfY4uPXYfJeMoeXrTlIkm6blifVX1bmqCmiLg_yPNn3StRhpoC-OBUhMTZBeBa5ba5myllP7P7uL8DUHD6GEIrS1qNYudnGvunPXHxCYLx0-US4znK_EHV0xGjpPM4k6fwxnQjB3eJ84r951CAdqta33NQZ5um8j94tUci9b2CEFt7mPKVfhzM55Sg1OVTXyB1yc0LVRH_cLvv6a5xyQp6wfhFP7ED9ZMXPNRvtmmHc2EUrw6O46LocYGXSVjBHMtfTfJMp3-ISMiiJoYY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
گل‌دوم بارسلونا توسط رافینیا با پاس یامال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/106908" target="_blank">📅 23:50 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106907">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">رافینیاااااا دبل کرددددددددددد
🔥
🔥
🔥
🔥</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/106907" target="_blank">📅 23:45 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106906">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">گلگلگگلگلگگلگلگلگلگلگگل</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/106906" target="_blank">📅 23:44 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106905">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p0If792y3yISsXMt63fV_mOQTJ3wv6g0c7i0glg375TOEas799YcduH15onEURVv7s0rRsX7zpdAlwP37i5wcz484b633OmZPxzV2h2BR-aqElJL74-d8h9aFeSypuXPYBiIU81s_5zosw1vt7fLlb9MyWnUfPt19jpepv2DMk87eOmii2gn3g_hvgVbkRubIWJ0zPMqj4-cfSFOVShONzQDf0UP9G7ioFg-I9ZJTmIwiZ7Uq89FXNsOCN-MGG-J7ekjNAQGYfkLtcolJwEvX4AAr0fOWVaWT-SKz_MIGfrOFb_YDRduG8cTmC4B7LH1KEg5dtw1NqPhbhzt_3sVBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
سعید زلفی و نیما تاجیک ۲ گزارشگر مطرح و باسابقه تلویزیون به پلتفرم اینترنتی نماوا اسپورت پیوستند و از تلویزیون کناره گیری کردند. پیش تر محمدرضا احمدی هم از تلوزیون کناره گیری کرده بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/106905" target="_blank">📅 23:09 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106904">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/9e51312166.mp4?token=fBcW7H0ly4FmtixcM-shsDHAxOWek3f_AS2Gs8GT3He5QlQh_6EL1YbksTH66KNHxpv1pOF8asgrXeD1CYPL3wpg3VnCwwF_mvCTqEewVlwf5a73MDh6J-ZHUVyzXnXwXnWV7FBX9zODDoU0Iun4xPQT5qMPezKxrLtMguFqLFVlIsStE9RadWYrVo-45kudVZR7l-t4uxqSUig8Z1NulMT3alOt_GhlhvPgv0hTx92CGJ_kMVy-3ElsX4t9ppltqnFDuq_LJsuvv9WqtQDxHa3y2L2SjNP5o2FhcTEjRU1NqdeRO5C1YvWs4wCiW2W0-hODlFng4hDUXIJTaz36K6Pl4tK2CmLGMgaRA3u-QBkAc3d7vEPO45H13sSCER8FPNYe0ZDzNhYBNBr_fwHKHfjBhgD8fHel5vTgksOvKWwoMSySiglTJ8sAm61BaYAGUkjj8QDfi1msYe36Ekg0KkafICSpbD6nZt8UiPxnWymQ0ZpxFeeZigzJBXkRuW2A8P8Y1lCJ6yj_jKVSLSV31Ph5ieB0dzpSvjKJdcGHDxNlX929rCjrf7uTCs183pvSxqlDkZ8PgnhrAQ-TlfEvdnigleSFiZBdKTMVSplPAhUIkjV0tnMqYL4o-ewC0E8y3f9xXpZ_71DTUS0MuSzZdl1mRaL43GpFMokRv2K3Yp0" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/9e51312166.mp4?token=fBcW7H0ly4FmtixcM-shsDHAxOWek3f_AS2Gs8GT3He5QlQh_6EL1YbksTH66KNHxpv1pOF8asgrXeD1CYPL3wpg3VnCwwF_mvCTqEewVlwf5a73MDh6J-ZHUVyzXnXwXnWV7FBX9zODDoU0Iun4xPQT5qMPezKxrLtMguFqLFVlIsStE9RadWYrVo-45kudVZR7l-t4uxqSUig8Z1NulMT3alOt_GhlhvPgv0hTx92CGJ_kMVy-3ElsX4t9ppltqnFDuq_LJsuvv9WqtQDxHa3y2L2SjNP5o2FhcTEjRU1NqdeRO5C1YvWs4wCiW2W0-hODlFng4hDUXIJTaz36K6Pl4tK2CmLGMgaRA3u-QBkAc3d7vEPO45H13sSCER8FPNYe0ZDzNhYBNBr_fwHKHfjBhgD8fHel5vTgksOvKWwoMSySiglTJ8sAm61BaYAGUkjj8QDfi1msYe36Ekg0KkafICSpbD6nZt8UiPxnWymQ0ZpxFeeZigzJBXkRuW2A8P8Y1lCJ6yj_jKVSLSV31Ph5ieB0dzpSvjKJdcGHDxNlX929rCjrf7uTCs183pvSxqlDkZ8PgnhrAQ-TlfEvdnigleSFiZBdKTMVSplPAhUIkjV0tnMqYL4o-ewC0E8y3f9xXpZ_71DTUS0MuSzZdl1mRaL43GpFMokRv2K3Yp0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔥
🇪🇸
گل‌اول بارسلونا توسط رافینیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/106904" target="_blank">📅 22:59 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106903">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">چه گلیییییی زدددددد</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/106903" target="_blank">📅 22:54 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106902">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">رافینیاااااااااااا</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/106902" target="_blank">📅 22:54 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106901">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">گلگگلگلگاگگاگاگاگا</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/106901" target="_blank">📅 22:54 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106900">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">گلگگلگلگگلگلگلگلگ اول سویااااااا</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/106900" target="_blank">📅 22:50 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106899">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/9f072da801.mp4?token=Mm8tkozMkq5BJ9KA9o6pOflZTeFJLJVpsr7b04-MLCuGHGM-JEdkRVib1KJiy9cZHfyadLl7XQGtQPcSwIanAxj--DJ19kLYPfjYdpgqR2I-xjgMee189KkDP42c9z-5J0bLX12etb-OZXaCF9r3OmdxQqhxhbQoeAX8Gqsl6NTUXde5hoFlVG1FcnK8dEcuYqAlJ5YDo6gMJIs8tV4VXSEhzXHqgO_vfOKvWn-GXN_IIaL383HI9rNIAJ1SKvZvPtUcrcvalo0XZBx-M2Q-rn-OtvlxlK071WYAgbUp8Z0nycnwqeBz0BtCfY5H8LUNfa3NAdCiXImEc3MTEITKoU2J2-EAb_v0kuz73gQWsyKlz_RJkxV5UYwc7nZG_l2JheUIVcn7ltpr_PoolZ4zCQ7Rfeb5P9hF8muB3h54DPxa50GsJssi7utSm_nDS-YfY6V0thYWxon5zkxMWFa1iGco9jocmZB5UoMBLVA-uLQKXubObaF_3nwzwnfX6bTnQXeDx2TcqR1Y1E3zzs63BsGv4iQV8Fh7KsSd3AE1xWjfKh6dk7rObX5juqGBKcxWdZqXsnGPKv7Xxbp2vsKMCg7hxKU1DrgBJ2p7D7l_zRy3r6SaBnHnLW318LjcE6XuW_dqFlC2uoSlV__99w8gyriY0ip4qzjjlBX8V2Kjn3s" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/9f072da801.mp4?token=Mm8tkozMkq5BJ9KA9o6pOflZTeFJLJVpsr7b04-MLCuGHGM-JEdkRVib1KJiy9cZHfyadLl7XQGtQPcSwIanAxj--DJ19kLYPfjYdpgqR2I-xjgMee189KkDP42c9z-5J0bLX12etb-OZXaCF9r3OmdxQqhxhbQoeAX8Gqsl6NTUXde5hoFlVG1FcnK8dEcuYqAlJ5YDo6gMJIs8tV4VXSEhzXHqgO_vfOKvWn-GXN_IIaL383HI9rNIAJ1SKvZvPtUcrcvalo0XZBx-M2Q-rn-OtvlxlK071WYAgbUp8Z0nycnwqeBz0BtCfY5H8LUNfa3NAdCiXImEc3MTEITKoU2J2-EAb_v0kuz73gQWsyKlz_RJkxV5UYwc7nZG_l2JheUIVcn7ltpr_PoolZ4zCQ7Rfeb5P9hF8muB3h54DPxa50GsJssi7utSm_nDS-YfY6V0thYWxon5zkxMWFa1iGco9jocmZB5UoMBLVA-uLQKXubObaF_3nwzwnfX6bTnQXeDx2TcqR1Y1E3zzs63BsGv4iQV8Fh7KsSd3AE1xWjfKh6dk7rObX5juqGBKcxWdZqXsnGPKv7Xxbp2vsKMCg7hxKU1DrgBJ2p7D7l_zRy3r6SaBnHnLW318LjcE6XuW_dqFlC2uoSlV__99w8gyriY0ip4qzjjlBX8V2Kjn3s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اوووووف صلاح ببینید چیکار داره میکنه
😐
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/106899" target="_blank">📅 22:16 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106898">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🔥
🇹🇷
🇹🇷
دبل محمد صلاح در بازی با گالاتاسرای
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/106898" target="_blank">📅 22:14 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106897">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rzReim7FwQYPObm_9V3rsWJyxdYzHfWixTMNNCvaGQY9gYa5ZaAG1UoaJm1-u3oxBlAurw1xXYfBNvTwk33JeT6d1oLKASgxw_FCFsHUo7_gC_VsZXOXVt_eP54h1t52JUiYXPchLKi8ejyZ3wx_pb4eCoGXuV6HxGmg-jexpxTpuznredyGusehMQOE_TecCZ6nFnes_xy53Pbd62Y8U0RJwpcB9nyYnmcs8LKSJhzpleWzy5avvf9Puc58q0YohIxrCUkZTZ9WQawl5hsx6wWMvuLBIFJFBHnCXbtxPrDk7PeujrVO7RJpn6xI-q2Sqz81a5U0pwBIaHtSSl-ZFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
حمله شدید دی‌زربی به بازیکنان تاتنهام:
🔻
ضعیف‌ترین تیم‌تاریخی دوران مربیگریم رو دارم. اصلا نمیدونم این بازیکنان چیزی از فوتبال میفهمن یا نه. اصلا امکان نداره یک تیم اینقدر بازیکنانش ضعیف باشن! واقعا براشون متاسفم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/106897" target="_blank">📅 22:04 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106896">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f38027f14b.mp4?token=niiVxiorq_PZ6dN7xAbGPm3m3D1zzMzvTiqZjdKDabQA6Ls4vAXBsnnn6u00xJ2EhJ9bF53vk3Mzp4WcR5bjN9EoJlhCJErTVxPoPMnP-naIwmydp_mPDgsG6ZLXeeZOuPdd0Xe17Hvgv8mxSzX0yJNJJHCp1ACmRB17zYjI9uHLzS26inSHCNPSzdND4c9dKf-7_UYUqUBn_v38LCLxQY_YdGmFd88yLe-Nsrj0mre0Y-hvsfD1t7Oe73oLMhG6ljJbtbd-RQ_1E5RBNxVgJONX9YPOazKKbx1zidpe5U1uA1v1xbhJes0OYAWcA6_4f9BSU4Ow_40OILSZPg1jepS5c3OWYZ_WG9klN_iQD27vsVsemC2C6hZ3R-BJEJMPaZt57X6VddUqRGwVBhrgZXAXprWlTJ4-ZsxaxHqhKWgTHwE7BPlx1W35FsRPS2AEsYJBhkGw_TDCnowEOAEpLr4kvKs3RUetgwL6BeLDuCUKTQJZTBdmUyH2PEEfhiZ5BDP6ck_9oFiXNGi_ILAeKqYG_jBjRtUuAhGa9cMwsgZJuW7Ak52Wn-iIKFDdXXvhapxnMPjBmSdya0ltKtU2dBU3FdvSnDyaP-B2uCE5Ti6Mcc0HpD8B6HdgLqAK6qpeX4XkF2UxnVR0ixwYcWM-nYwuI641BaEmpFQH1_T3tEI" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f38027f14b.mp4?token=niiVxiorq_PZ6dN7xAbGPm3m3D1zzMzvTiqZjdKDabQA6Ls4vAXBsnnn6u00xJ2EhJ9bF53vk3Mzp4WcR5bjN9EoJlhCJErTVxPoPMnP-naIwmydp_mPDgsG6ZLXeeZOuPdd0Xe17Hvgv8mxSzX0yJNJJHCp1ACmRB17zYjI9uHLzS26inSHCNPSzdND4c9dKf-7_UYUqUBn_v38LCLxQY_YdGmFd88yLe-Nsrj0mre0Y-hvsfD1t7Oe73oLMhG6ljJbtbd-RQ_1E5RBNxVgJONX9YPOazKKbx1zidpe5U1uA1v1xbhJes0OYAWcA6_4f9BSU4Ow_40OILSZPg1jepS5c3OWYZ_WG9klN_iQD27vsVsemC2C6hZ3R-BJEJMPaZt57X6VddUqRGwVBhrgZXAXprWlTJ4-ZsxaxHqhKWgTHwE7BPlx1W35FsRPS2AEsYJBhkGw_TDCnowEOAEpLr4kvKs3RUetgwL6BeLDuCUKTQJZTBdmUyH2PEEfhiZ5BDP6ck_9oFiXNGi_ILAeKqYG_jBjRtUuAhGa9cMwsgZJuW7Ak52Wn-iIKFDdXXvhapxnMPjBmSdya0ltKtU2dBU3FdvSnDyaP-B2uCE5Ti6Mcc0HpD8B6HdgLqAK6qpeX4XkF2UxnVR0ixwYcWM-nYwuI641BaEmpFQH1_T3tEI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇩🇪
🇩🇪
در هفته چهارم بوندسلیگا، دورتمند با یک گل مقابل اشتوتگارت برنده شد و به صدر بازگشت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/106896" target="_blank">📅 21:53 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106895">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qLdNoKaTLw2zN4NLHPr49l5nqR3fZQNiGXpL-3BniLJHoKjhiuWRPaPho45zh3lOOsoiYkwZfkskKWH1exHL6RVqvclVc6MXE55cNAhuj0Me2uBxmUhZnsGfyOGPFK1fkJFNI0YuXaH1czoBDSrQM2YweTQ0q0kl_TvAj-8Ig3LAdBjfUz6f_2Kr3gJ96Xyu6lYCM45DJVw8fVIqit0rSMUXaiX8eKwKFffEo4g3o6ly6tJgie9mG2U3WRWEpJfxpy4A3XCsOMlcFtbknezZGj__tC4Y6v_aWJmSJEBL9VMWq0dA4Ple8Af0aE1o1I_lhByMqIoBwtm8PQIqUDUIhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🇪🇸
لیست اتلتیکومادرید مقابل رئال‌مادرید با حضور خولیان آلوارز و غیبت سورلوث
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/106895" target="_blank">📅 21:42 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106894">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e9f110d93f.mp4?token=b6U98Xjc8KYmSF8MQbY1nnPryfOOh7ZoHu1P8b-0V_4WITyFPRVDrhEqV_uedo1-BL5Xg7cQBt7ESaNks9-rpaDHnhB1hriYpFHrD7VI_8frhZZCdJDkcFGnw7o-u1LpYNs8gXUlIS2E-DuCMR4dLfw9VAOYibyO_LX5TJIT56dc3lrS4XUtBPdpabPXdGkFmzvZXwTizX2m9wZjhnUpKc1i73Z23SOWdtc3e0FLBBmpZMfocthnmi15lgkKDyx_WktNHOELSOfD-JpxaWPW0lv3DfGAumzCNjov5-iBZ2Q9Wp7Z8LJ7_-Bm_4LgVp-Opy1aQgdv1uf8Gm4q8XUjiTozvQZ1nZ843e134-yy_OjfxUNGzxdgdHSN25JYZqiO1zaugTJcv2nXRofpy0UwZzKhQ3bra8jm9nfaYPnyZ0-utzTPOaLR5gohq43M-lptmRNUdsotTfUd3DoJKKEiPqGA28D6T4brlvzv1dE9PnaPjFkIN5T5rdb4OStFtcqs4FD6DBNrriKVnvbf9E0ETbV_m_tY-uIN_8pC1qqHAN6BXA_Gy7zuTsa7ieVnEXuvEbuLgZlkJ5LbEDb6jXVQjEsC1AzWayi3HssgTvOg0OFYI4gpF53Tu8Y2ayQZk_7YJlxDUAqnmDomS70VENXP1X8-0ozbpR4EhC3x_6kNHX4" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e9f110d93f.mp4?token=b6U98Xjc8KYmSF8MQbY1nnPryfOOh7ZoHu1P8b-0V_4WITyFPRVDrhEqV_uedo1-BL5Xg7cQBt7ESaNks9-rpaDHnhB1hriYpFHrD7VI_8frhZZCdJDkcFGnw7o-u1LpYNs8gXUlIS2E-DuCMR4dLfw9VAOYibyO_LX5TJIT56dc3lrS4XUtBPdpabPXdGkFmzvZXwTizX2m9wZjhnUpKc1i73Z23SOWdtc3e0FLBBmpZMfocthnmi15lgkKDyx_WktNHOELSOfD-JpxaWPW0lv3DfGAumzCNjov5-iBZ2Q9Wp7Z8LJ7_-Bm_4LgVp-Opy1aQgdv1uf8Gm4q8XUjiTozvQZ1nZ843e134-yy_OjfxUNGzxdgdHSN25JYZqiO1zaugTJcv2nXRofpy0UwZzKhQ3bra8jm9nfaYPnyZ0-utzTPOaLR5gohq43M-lptmRNUdsotTfUd3DoJKKEiPqGA28D6T4brlvzv1dE9PnaPjFkIN5T5rdb4OStFtcqs4FD6DBNrriKVnvbf9E0ETbV_m_tY-uIN_8pC1qqHAN6BXA_Gy7zuTsa7ieVnEXuvEbuLgZlkJ5LbEDb6jXVQjEsC1AzWayi3HssgTvOg0OFYI4gpF53Tu8Y2ayQZk_7YJlxDUAqnmDomS70VENXP1X8-0ozbpR4EhC3x_6kNHX4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
نبرد اینتر و رم با تساوی دو بر دو خاتمه یافت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/106894" target="_blank">📅 21:27 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106893">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c80348f50.mp4?token=AiObBIBGQo79u1ur3FVq097XFT0F0DFJ7SeuOOEP2RvYAdXk5UxyQEpvCgS0VOlAYRZWazcI8i_1UQYM9ADSLReTbpNKJSaFXuDIOOM4swI-4QralfFw1CdNSoAvz6vVx65xvv8S9yUOrdyleWi_dl4O3VynJxKNNwWnS03JfTsp9sdu0nF65BEVLBO8JhoC-L4-VV0sRlWosFPZ_7DLhfIe5rqyAhLc-aFvjpkB5Lt3kA3Bg1kLsMTFwT22dHtyFQx6aLHqRqVJRE8MjJctkf6Mkf55cgs3LHqcHUyus7hcQoEQlwWQGGwsR5u4HF4xdGx5hnDXcG-2WernVAIWUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c80348f50.mp4?token=AiObBIBGQo79u1ur3FVq097XFT0F0DFJ7SeuOOEP2RvYAdXk5UxyQEpvCgS0VOlAYRZWazcI8i_1UQYM9ADSLReTbpNKJSaFXuDIOOM4swI-4QralfFw1CdNSoAvz6vVx65xvv8S9yUOrdyleWi_dl4O3VynJxKNNwWnS03JfTsp9sdu0nF65BEVLBO8JhoC-L4-VV0sRlWosFPZ_7DLhfIe5rqyAhLc-aFvjpkB5Lt3kA3Bg1kLsMTFwT22dHtyFQx6aLHqRqVJRE8MjJctkf6Mkf55cgs3LHqcHUyus7hcQoEQlwWQGGwsR5u4HF4xdGx5hnDXcG-2WernVAIWUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇹🇷
🇹🇷
دبل محمد صلاح در بازی با گالاتاسرای
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/106893" target="_blank">📅 21:19 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106892">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G8-6-dgOOimEAHpJdUe4Dn2tpPL0fAFu0rH1kqMwJdOZUthSqZ9_ZOM1bhX0bLCmcsLLVM0AjUpD0760aI15bkBY91EEYdcMkrb1dgwmP-p8JmGFBYdEjKMRqUkDlXS22kWMHUCpAYXbwLuY7Y_zlYHW_jgGTq0Odo3k36nuJwbiCrrytcyLSgH6I6CPuzBGjylwUK_K7MYrlVxzWOb8CjlfF9_ePgWVHW3KH6ueYQbfg4EYjmxVt_3dKT_NyijogS1RPbNMVnHL5GFagfqOGSULWG8Tru9W9iVE2RnVED770fZtIuMUfstxkR4aFQ859K3XCrT9VxN4mWbow4VRvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🇪🇸
شماتیک ترکیب بارسلونا مقابل سویا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/106892" target="_blank">📅 21:18 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106891">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d419048b91.mp4?token=q7_GxjiOnotfdIWNV-ZqyRKwRFAIeIhbxtS7eP1IPQ9vJAgGFUmi4jm2cHkZwP-zZjHcbth1CK17qmmiQnd_4sgb5YBZ0ImGSPWb6QKxD6umcK3UqRUBjrxOHFxfp0wOB7jCvJ1-t73xOL37zBA0NAhcEVL0Qk5wO0Gy8wTDGTlYpTKEKj-4hpFArwpy6zSZeKMWccLo2YxO0a2ILX2lN68JZgWZMCkcpcsxoFPbNZ-aqAWnK0hhxCAh03aKEc0YTe8tdudceh0utsjk2ajoKVQPaARjgUz5DeApVZrAqpjT2b5ORDzUMQOscKgM7G7FsmSLib9ptdnEHgAal9Mxww" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d419048b91.mp4?token=q7_GxjiOnotfdIWNV-ZqyRKwRFAIeIhbxtS7eP1IPQ9vJAgGFUmi4jm2cHkZwP-zZjHcbth1CK17qmmiQnd_4sgb5YBZ0ImGSPWb6QKxD6umcK3UqRUBjrxOHFxfp0wOB7jCvJ1-t73xOL37zBA0NAhcEVL0Qk5wO0Gy8wTDGTlYpTKEKj-4hpFArwpy6zSZeKMWccLo2YxO0a2ILX2lN68JZgWZMCkcpcsxoFPbNZ-aqAWnK0hhxCAh03aKEc0YTe8tdudceh0utsjk2ajoKVQPaARjgUz5DeApVZrAqpjT2b5ORDzUMQOscKgM7G7FsmSLib9ptdnEHgAal9Mxww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇹🇷
🇹🇷
گلزنی محمد صلاح مقابل گالاتاسرای
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/106891" target="_blank">📅 20:46 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106890">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c0314b4edd.mp4?token=V55fd5OR1OrOE2OPAh6OWXLYKjzpSDUJ_2KKDY0t1OU_EvBbs4j5zR4TfXUGgVCY2cte-tYsopMjMg23zgKtLfqM7e042IRRaecau1S7d64MvTfnVoT3TgvCyAKvQITojwR7NRkUX3s3l2nKgMbElJgXLrq1AhoZNMJ1isvcHx8Fp2dV_YNonnd7phVBFLZ5qSd9wXR_ieArs5UTfJqGpgBDF6cjtG_6TW0ktymabWO5r6G7ZrkFA5xGKLY13JAUyzqQxNsd9Zh-EsrjLP4fzqilgZRH2rr419FpDCU2v8gkrWEnkf4ZgC9fY83pwlQFf-wHKatTab9xbn6aU_EasQHVOY-uUAMaUo3uAZRoeHID-C9qONbYF5wEN_oS6BrRbKlUZJetUMGF0cAyMYlVJ6q_SHF59vq7c1ME8lxZTiD7GS9CqfPoB5LeyV4igUiyK2s3x1H5QLACPYWbjUXEgMPgJZIKZw1PApou8U4jnktJy0Dsl0NhTxxSBf1dGe8DYi_D08ScyUY_5emYMMHSIVEaoiv57W3iz5UmE_PRM1dqqgO_RIDvTbuyVpKWh-0IcuscYA0ppYQdUS0a5cFIXmIEbSEH_tL2zDFijLGWI-DAWD-ND9xa1rsPaz5XEbPUc-kwMTkq48rMB0Yk31aOTn-ZJrcUZuYJHL8-304sI50" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c0314b4edd.mp4?token=V55fd5OR1OrOE2OPAh6OWXLYKjzpSDUJ_2KKDY0t1OU_EvBbs4j5zR4TfXUGgVCY2cte-tYsopMjMg23zgKtLfqM7e042IRRaecau1S7d64MvTfnVoT3TgvCyAKvQITojwR7NRkUX3s3l2nKgMbElJgXLrq1AhoZNMJ1isvcHx8Fp2dV_YNonnd7phVBFLZ5qSd9wXR_ieArs5UTfJqGpgBDF6cjtG_6TW0ktymabWO5r6G7ZrkFA5xGKLY13JAUyzqQxNsd9Zh-EsrjLP4fzqilgZRH2rr419FpDCU2v8gkrWEnkf4ZgC9fY83pwlQFf-wHKatTab9xbn6aU_EasQHVOY-uUAMaUo3uAZRoeHID-C9qONbYF5wEN_oS6BrRbKlUZJetUMGF0cAyMYlVJ6q_SHF59vq7c1ME8lxZTiD7GS9CqfPoB5LeyV4igUiyK2s3x1H5QLACPYWbjUXEgMPgJZIKZw1PApou8U4jnktJy0Dsl0NhTxxSBf1dGe8DYi_D08ScyUY_5emYMMHSIVEaoiv57W3iz5UmE_PRM1dqqgO_RIDvTbuyVpKWh-0IcuscYA0ppYQdUS0a5cFIXmIEbSEH_tL2zDFijLGWI-DAWD-ND9xa1rsPaz5XEbPUc-kwMTkq48rMB0Yk31aOTn-ZJrcUZuYJHL8-304sI50" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
🇮🇹
گل‌اول اینتر به رم توسط لائوتارو مارتینز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/106890" target="_blank">📅 20:46 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106889">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/102cd70646.mp4?token=NwRvLdpd0w-NemWIJfSfXeyAgr16OvREi7Zsr7mD4dbTwkrVOciD8dgZ4IjeFk6rA8oMsQ4G_jvjCXc7QF9Nhtm8tujUibm1siViG3d41iwDxi3h6oeJgAWq2RzA4yZsv_md2XmaYgzRzXOda6VXftmn2oME37x3ghhksQyu1vfp_f3nTP2ZadpEoo3yn3hhl_2665eYNXZxaIJkwDjwY572_f-gIZD2Sz5YmPh8wri9Bg6-UygJ4SfD6QTIz1p_STkIMkZGG63JoT_T4lIrkrvY5Xd-Yduss89PnP4XO_VFH9YSW-63owLWkH95HAVIq0_4UjV8kx-csDB4V5eHpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/102cd70646.mp4?token=NwRvLdpd0w-NemWIJfSfXeyAgr16OvREi7Zsr7mD4dbTwkrVOciD8dgZ4IjeFk6rA8oMsQ4G_jvjCXc7QF9Nhtm8tujUibm1siViG3d41iwDxi3h6oeJgAWq2RzA4yZsv_md2XmaYgzRzXOda6VXftmn2oME37x3ghhksQyu1vfp_f3nTP2ZadpEoo3yn3hhl_2665eYNXZxaIJkwDjwY572_f-gIZD2Sz5YmPh8wri9Bg6-UygJ4SfD6QTIz1p_STkIMkZGG63JoT_T4lIrkrvY5Xd-Yduss89PnP4XO_VFH9YSW-63owLWkH95HAVIq0_4UjV8kx-csDB4V5eHpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل‌دوم رم به اینتر توسط مانو کونه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/106889" target="_blank">📅 20:46 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106888">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30ac971c9b.mp4?token=HAk0J-ypCD5ZjhGS2EHXSLywBMK5Fuk2xNl7dCQqjU2FZcWdlbewBuvRa53tXDn7s0V_JbXh5-4k5XZm9uCtKj5IN50CGVR0T-kvy5V48N_nyDxzYCoS5_CQfcUBZdPosCZeL_q17Py1J9oy6lZDGrLE8pqlzkhmSu5w4lQr0CVoc47Ks8I0naf8kNGIavRhfci4GxAU628o7sGS8Z-n5xYkPfz7eWmvfh4yLladdgBTTHqFNSrdg-G3QHdneSo5BQOjC0uE-1HNRyl-dUmcI0E84GbSk_Iob6rxzEi5IOT0DKivKgKZWoKPhyteTOIQ3EN6khdq6jPzgCjG69wCnIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30ac971c9b.mp4?token=HAk0J-ypCD5ZjhGS2EHXSLywBMK5Fuk2xNl7dCQqjU2FZcWdlbewBuvRa53tXDn7s0V_JbXh5-4k5XZm9uCtKj5IN50CGVR0T-kvy5V48N_nyDxzYCoS5_CQfcUBZdPosCZeL_q17Py1J9oy6lZDGrLE8pqlzkhmSu5w4lQr0CVoc47Ks8I0naf8kNGIavRhfci4GxAU628o7sGS8Z-n5xYkPfz7eWmvfh4yLladdgBTTHqFNSrdg-G3QHdneSo5BQOjC0uE-1HNRyl-dUmcI0E84GbSk_Iob6rxzEi5IOT0DKivKgKZWoKPhyteTOIQ3EN6khdq6jPzgCjG69wCnIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🚨
⭕️
آخرین وضعیت سربازی بیرانوند از زبان مدیرعامل فجرسپاسی: معافیت بیرانوند تا پایان آذرماه است و این بازیکن در تراکتور می‌ماند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/106888" target="_blank">📅 20:09 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106887">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76f9243a61.mp4?token=RrdfQKO9cTlGkpkzLq4jERP12XbE3Cz9UUFXDlI1WTLaAcMe2LQWBMLWxXl1jkL3SUPXE7hbrbJtyrp52j71OUvdp6y_S2hchYL17NOQdCNGR_svu95DPOB3TdIrIb6PXhUvJuUMs2O_Q03OjKLJKIwS2Ys1DCBLGpkriM3GkTCHDP3DktPUy1zPap2Aio6LpLy21qIN_g9ygXNhreX8zaC2L8yO0GQlUvC7cDZuzsltlqHMgbYP1gXYrA64mDvN44z5p477j0srlHtUlbpHaVa5LcgwHqDdV8xTNC_8B1NrdQ7yMhfPyRWVP9ZhfJEArnKkzAoqL3ZkRSjGypGK3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76f9243a61.mp4?token=RrdfQKO9cTlGkpkzLq4jERP12XbE3Cz9UUFXDlI1WTLaAcMe2LQWBMLWxXl1jkL3SUPXE7hbrbJtyrp52j71OUvdp6y_S2hchYL17NOQdCNGR_svu95DPOB3TdIrIb6PXhUvJuUMs2O_Q03OjKLJKIwS2Ys1DCBLGpkriM3GkTCHDP3DktPUy1zPap2Aio6LpLy21qIN_g9ygXNhreX8zaC2L8yO0GQlUvC7cDZuzsltlqHMgbYP1gXYrA64mDvN44z5p477j0srlHtUlbpHaVa5LcgwHqDdV8xTNC_8B1NrdQ7yMhfPyRWVP9ZhfJEArnKkzAoqL3ZkRSjGypGK3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
🇮🇷
انتقاد کاویانپور پیشکسوت پرسپولیس از کامنت‌ پرسپولیسی‌ها در پیج السد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/106887" target="_blank">📅 20:01 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106886">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/a6d65328b4.mp4?token=ntnOPOySJ6nbLvc-zt_Xx4LkHvb22OwWiJT4DTd-s8HZ8q4TidKBS-ga9GyYN54P1UqmhnBXGGridhn8xKWghdUwpOSUSgDtyO9JM6ohsYb2oz6E8yLEXN0CxhlpqCnn4D7slZytE5yhI6xtRaBPq0MqvzrZjoUBWR59AnmpIxEEpZ0_er6WwkFQPwYRPqb82aDG-YYkApw5b_Gf73S3u8MlClefwQMWcq54AcZjmMIbH8bdh0rrehze666iOPeaTYjeaIE8FRTUpyBaQC__1_USe9fGWXPhy5LqWci4P1Fahbgf_w-cx5MKLdtOKb81Wh3NAb-sSt26zh_l8k6RzC51z5B1PSu74pytQ7FNxoImEi0YhIIDGlnDu0JVgwBBeDzAtf1G6lEHH3hMAXKvg87eDPWIywixeMfWJdvv6_SvZGXuNnSywfKBm0dVZsy8JU3-7OL_2geOIKTYW8cz5Nmf8hY0zUeTfYQVjw2MI2rwPN5-nFDd9iww_SSJTzO7N0Wc8uDdQyqc7bIUzdPZDTT8GbVxTfoZqgqATvSBMplJIYpuZsuJh2m_Og9OhxYEViEzACGDEv8uHVEyqEZEfeG7NDn6h5t_g6RGRJHf5wNk_r0ubiWCg_78St4IOkqTVEzLGlxHyBlPjXd0ltT-FaUUnLc83lnuMIkuktIXOM4" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/a6d65328b4.mp4?token=ntnOPOySJ6nbLvc-zt_Xx4LkHvb22OwWiJT4DTd-s8HZ8q4TidKBS-ga9GyYN54P1UqmhnBXGGridhn8xKWghdUwpOSUSgDtyO9JM6ohsYb2oz6E8yLEXN0CxhlpqCnn4D7slZytE5yhI6xtRaBPq0MqvzrZjoUBWR59AnmpIxEEpZ0_er6WwkFQPwYRPqb82aDG-YYkApw5b_Gf73S3u8MlClefwQMWcq54AcZjmMIbH8bdh0rrehze666iOPeaTYjeaIE8FRTUpyBaQC__1_USe9fGWXPhy5LqWci4P1Fahbgf_w-cx5MKLdtOKb81Wh3NAb-sSt26zh_l8k6RzC51z5B1PSu74pytQ7FNxoImEi0YhIIDGlnDu0JVgwBBeDzAtf1G6lEHH3hMAXKvg87eDPWIywixeMfWJdvv6_SvZGXuNnSywfKBm0dVZsy8JU3-7OL_2geOIKTYW8cz5Nmf8hY0zUeTfYQVjw2MI2rwPN5-nFDd9iww_SSJTzO7N0Wc8uDdQyqc7bIUzdPZDTT8GbVxTfoZqgqATvSBMplJIYpuZsuJh2m_Og9OhxYEViEzACGDEv8uHVEyqEZEfeG7NDn6h5t_g6RGRJHf5wNk_r0ubiWCg_78St4IOkqTVEzLGlxHyBlPjXd0ltT-FaUUnLc83lnuMIkuktIXOM4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇹
گل‌اول آاس‌رم به اینتر توسط مانو کونه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/106886" target="_blank">📅 19:46 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106885">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/947613cda4.mp4?token=bUyFsKH-wY7Nn8tK-6BEMM48n91CeFFvSM88vUApPc553GXo2YRjNE-DXUWuLHafqGbvqNxp1L98zyJChRzNJMKnoc4cwKYZYtgUPVNas7v_oERJvOjTUBhscipRmdk6UrAp8i2b0pCP0gfNWyczbDk7g2I4MW6IlqMfZ4Tk5Hz3ftTfJ8YXIqS9Fvo7wJF7EV5zdwH61UHURpIAGbMEtUW1d7tcXhhSlY6rQH1tGkmQ7oyOOqWUKAGQNIH0PVcX-nCRTawPjiKVpnLoENxHad72NpM4Qt2rIuKRlSc_3941sWCCre8McxUSirLhCWMiM2r3reB7rIJOr3ZsfHV2oIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/947613cda4.mp4?token=bUyFsKH-wY7Nn8tK-6BEMM48n91CeFFvSM88vUApPc553GXo2YRjNE-DXUWuLHafqGbvqNxp1L98zyJChRzNJMKnoc4cwKYZYtgUPVNas7v_oERJvOjTUBhscipRmdk6UrAp8i2b0pCP0gfNWyczbDk7g2I4MW6IlqMfZ4Tk5Hz3ftTfJ8YXIqS9Fvo7wJF7EV5zdwH61UHURpIAGbMEtUW1d7tcXhhSlY6rQH1tGkmQ7oyOOqWUKAGQNIH0PVcX-nCRTawPjiKVpnLoENxHad72NpM4Qt2rIuKRlSc_3941sWCCre8McxUSirLhCWMiM2r3reB7rIJOr3ZsfHV2oIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
🇮🇷
خواجوی گلر پرسپولیس: الگویم نویر است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/106885" target="_blank">📅 19:30 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106884">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e4104492c.mp4?token=FfAyVeykyESN7T64QOuvafnLHJWf6eOVlr-9k4yc4_pAMrh5Fb7A3NgszkaBvnZMzubCLJfghcFVFOtgjNe_tDEsC8u4S6QLW21ZRfQPiyujQZh8R1KMClb_IWtz0j4kVyc5n7A9y1z7DCnA56-MGPR6j4TAh6bJHKR33emWn21MUUl0XEgyqIGwMJchUJwL2ZfmtmHes97D_pDovGT0uZC_X01cLFKENOtx9csntmvDqUQuX_mEtjWk1oj51h8zwCG-6MMeugOSO7W-rtbZYR8EBPIjNITYJY8nVPhN2K_1HY_kxjKUnIIfhMFkAfZnjC_bkNvwaERy8spfvP2tHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e4104492c.mp4?token=FfAyVeykyESN7T64QOuvafnLHJWf6eOVlr-9k4yc4_pAMrh5Fb7A3NgszkaBvnZMzubCLJfghcFVFOtgjNe_tDEsC8u4S6QLW21ZRfQPiyujQZh8R1KMClb_IWtz0j4kVyc5n7A9y1z7DCnA56-MGPR6j4TAh6bJHKR33emWn21MUUl0XEgyqIGwMJchUJwL2ZfmtmHes97D_pDovGT0uZC_X01cLFKENOtx9csntmvDqUQuX_mEtjWk1oj51h8zwCG-6MMeugOSO7W-rtbZYR8EBPIjNITYJY8nVPhN2K_1HY_kxjKUnIIfhMFkAfZnjC_bkNvwaERy8spfvP2tHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
صحبت‌های جنجالی یاشار سلطانی خبرنگار، درباره چرایی برهم خوردن توافق پایان جنگ از سوی نیروهای سپاه و جمهوری اسلامی!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/106884" target="_blank">📅 19:02 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106882">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da8b096322.mp4?token=ljRbVRvFNPHKdlzK40IUKDRCFdPoq3pB4tTtlwttKwwu51KC-feg9giGaUGiR10cmSA3rsrZpMvBuq1VNkurHYek6jF-WG_XbqZZ4nlaOwltalEneGjOm_4MRG6GN_oekcnW0Dc9667FuWjsFiUoZfPGLXizEckC_bB0yDYnMMlcmCn0bdpEShkM1H9IBoJCOlqDaHxDvONvAkzbhpEg8Fp7nBEdxNTRdyZTRDmE5smkNcbS5jxCVK_S6kGs_9n0vIILlJGU-XLuUl02YQ7wFxB1zUTsjgUB6AWn0ZohLKSMZ_rP6zdP9TSROdiMXXgozG6uxzxm44Mb7_fLLxxQ7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da8b096322.mp4?token=ljRbVRvFNPHKdlzK40IUKDRCFdPoq3pB4tTtlwttKwwu51KC-feg9giGaUGiR10cmSA3rsrZpMvBuq1VNkurHYek6jF-WG_XbqZZ4nlaOwltalEneGjOm_4MRG6GN_oekcnW0Dc9667FuWjsFiUoZfPGLXizEckC_bB0yDYnMMlcmCn0bdpEShkM1H9IBoJCOlqDaHxDvONvAkzbhpEg8Fp7nBEdxNTRdyZTRDmE5smkNcbS5jxCVK_S6kGs_9n0vIILlJGU-XLuUl02YQ7wFxB1zUTsjgUB6AWn0ZohLKSMZ_rP6zdP9TSROdiMXXgozG6uxzxm44Mb7_fLLxxQ7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🔥
🔥
🏴󠁧󠁢󠁥󠁮󠁧󠁿
گل‌سوم برایتون به آرسنال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/106882" target="_blank">📅 18:50 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106881">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eEbvQjtgBEsFAhCeS1isj2SUfzrIFiBuFefCuGA7nKrcKb90X3lCiHFY4tgn0QjhRZMiazRQkuUxWfxfAs3x-126rfXpX8p8ljkRhWoFPfn-JkGinrVrtUFDjMVojgwn7xIbWbQ1SqVqsOw9INTs0gl-eVem_AH-j6KOZPS8rNxLc5cOq9z_aECLy5AEzoAgTRN2x5tCS3XWOXMNRFXvH6zQfIpeBocEoYpZfBurzhOtX2vE3yvHtnynZIxarhpoHyB3NbkGdgcl3ZszNxq1fPyCDTB6TQBGgrio_EaeBR1JePJWx7uem6s7QJgWETn9fSoyn2jUF2nPvO9R_gy5-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇹
ترکیب اینتر مقابل رم؛ ساعت ۱۹:۳۰
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/106881" target="_blank">📅 18:27 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106880">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/9510f8cfbe.mp4?token=l9nO1wu7RdqXMU15LruI-P2RNKw3FKA3ihimcpBLgfEhZ7U9Y4H4nS3UDOrLDtmHhXqlDiixV3994dh-eLUBN1Gr1yvfx9oaHK4uhicdNn69jZcnz0HH9Jw5UAvat2nZTnCRjMpVOPLd8XecLSezYTrxT0OMGh6GaIQx8vwNRF1yVeeH1MBfHKaDzJJLBRuPLPwxSZ6srNRgyHbHqpSBf5DXfm48WFPOJhdrUWur55GLZkAqUT_bcT6RW5NVquJnQlVWrO3-7U5hyvyvZnSGxB0TPdJpc0_qHyKOCTzFKhAsqKe6T4OTojlWYn3xF4rUPm9nbq4-Ifv-jGKCukd2XQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/9510f8cfbe.mp4?token=l9nO1wu7RdqXMU15LruI-P2RNKw3FKA3ihimcpBLgfEhZ7U9Y4H4nS3UDOrLDtmHhXqlDiixV3994dh-eLUBN1Gr1yvfx9oaHK4uhicdNn69jZcnz0HH9Jw5UAvat2nZTnCRjMpVOPLd8XecLSezYTrxT0OMGh6GaIQx8vwNRF1yVeeH1MBfHKaDzJJLBRuPLPwxSZ6srNRgyHbHqpSBf5DXfm48WFPOJhdrUWur55GLZkAqUT_bcT6RW5NVquJnQlVWrO3-7U5hyvyvZnSGxB0TPdJpc0_qHyKOCTzFKhAsqKe6T4OTojlWYn3xF4rUPm9nbq4-Ifv-jGKCukd2XQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🔥
🔥
🔥
🏴󠁧󠁢󠁥󠁮󠁧󠁿
گل‌دوم برایتون به آرسنال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/106880" target="_blank">📅 18:20 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106879">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">گلگلگلگگلل آرسنال دومییییی خورد</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/106879" target="_blank">📅 18:15 · 28 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
