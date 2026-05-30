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
<img src="https://cdn4.telesco.pe/file/sji9SiE5wsGTNeelQ8Q9JKA8Gc6TOrFE67U7HIX51fofm727SMgGXIV3lcWkDdxdIikfDytfHPeW7cZKWzzPrbcXUfnvSImc5J5Dz9ucey-flJygwz1IMVmznAGp5FomtgXUX7c4lfHqatvzAVwSamE0w8VlSrtPCUMZQbosOg2bb8fRWM1AhbQ9tCoJpCvWVJsuQUGTGU3Wj0O8q-0Ps7K9XtqYOohqqt-ll7VjD5cx48v1Fu-OB2C87njGKjagSdB1E5fVO7f-Tc0qnlspm61-VgxkqV9kUu3qhuLnu1j868j0BAQ6wu-HtwMuYpgTrfdim0KJlQX8ZDBTayd33A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 134K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-10 03:24:19</div>
<hr>

<div class="tg-post" id="msg-90533">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">💡
میخوای یاد بگیری چطوری با همین گوشی تو دستت از پیش بینی فوتبال سود کنی؟ سیگنال ضریب بالا و کم ریسک میخوای؟ فرصتو از دست نده همین الان عضو کانال VIP یونی بت شو
👇
➖
➖
➖
➖
➖
🎁
کسب درامد از پیش بینی فوتبال راحته اگ این کانال داشته باشی چون کارش بلده ae9: https:/…</div>
<div class="tg-footer">👁️ 2.43K · <a href="https://t.me/Futball180TV/90533" target="_blank">📅 01:20 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90532">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UiXklXdLj0e4THvjj_OIz_7YBNAaQ1WeV6dnf7XCI8oQ1Xk5yOaPE0HMFhaPAggzrfU6W6hTnKLGPvnPn1bmKb_wnaQX4txqlr6Mp-dAJLGPsod8x8elKwkzrloIbuBNgr4WJWiKtQmE3-betw4QC6aiPemJsgBmAsg3uCwWk1t_RMPPQvqLUBemsk4e1WfGstbliPc6SVYtXCvxSJx2_Gw1Iudytlo0gFQRRwJl5ZOcD42JmKVS7Vl4GDZ-_cI_aQFewVLWxR0xVtX2x7SyUSJ4kLSPN7RYfRs_Y4Xoyv1CrtGFtf1vh2XxZ2r01rOJ_WCICmc5ryEYZa4LMy4qdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💡
میخوای یاد بگیری چطوری با همین گوشی تو دستت از پیش بینی فوتبال سود کنی؟ سیگنال ضریب بالا و کم ریسک میخوای؟ فرصتو از دست نده همین الان عضو کانال VIP
یونی بت
شو
👇
➖
➖
➖
➖
➖
🎁
کسب درامد از پیش بینی فوتبال راحته اگ این کانال داشته باشی چون کارش بلده ae9:
https://t.me/+YwYFluMQ5-kyNmY8
https://t.me/+YwYFluMQ5-kyNmY8</div>
<div class="tg-footer">👁️ 2.48K · <a href="https://t.me/Futball180TV/90532" target="_blank">📅 01:20 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90531">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QbXtmMHiUwlaTyvGqyfA6oqEYU1ms7C_Dh_mB-eGZOdcIGslSD0dJ4eOOVTPj8fNxT_0DuzoBhZF2qGQ6OuvAhkXiZlrveMOWAkbRfm6bbY0GcBSgXpP2C3g5zW8ctDLWGeuCjW8AoIQCYdXqAtMQVcVlY19wxLkNfeMMivz7hd1M9kpRYndu3QL9lTkX9ls3SGuCHsmuE33pmho64sFgVT2yASvYnTAg3E37oKje2qLhjNdXz_DJbjre6P1nVuXVbMsUhoSPVS3sOjmTlv96HXZWJxLXg2q4OaJd8qHEr55_BMJQZXbrVK0d-Cgo4q1na1GK2RroKxDZYWkUkazcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
شماره 10 برزیل رسما از وینیسیوس گرفته شد و به نیمار دادن. البته قبلش توافق صورت گرفته بود
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/Futball180TV/90531" target="_blank">📅 00:57 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90530">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aac643b260.mp4?token=WFt8-KMO0UiDrleBACjmsbo_9dgygZojUN7wMXLJYHOyiD5BkIUIRSORBfHIYzlbx012lteBZQqjBDbmjmkqNyG-sH2HzQmQpysOCM0e_hfrtSc-1JHhfFj3lEcHEe-icQVVgQHfFAcWcMeQ-4Yd8oGZLlD4IWd7hPVeIiKUaBYiks1kiRt7fWbhPAprKzwdWkNAYla406bGKnnrb03CNQnP6Zu33l97Q7Z9eMaMi0-0cOsAfx30nG6mPmfPJJkNnkQ_gY3bWWJADVIxNQ4xr931x-dYP9UtOTV5MxYKV4K5uGdXm_jxoYa3lT7KMeeOzECImyX15yP3tGXM9nRlJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aac643b260.mp4?token=WFt8-KMO0UiDrleBACjmsbo_9dgygZojUN7wMXLJYHOyiD5BkIUIRSORBfHIYzlbx012lteBZQqjBDbmjmkqNyG-sH2HzQmQpysOCM0e_hfrtSc-1JHhfFj3lEcHEe-icQVVgQHfFAcWcMeQ-4Yd8oGZLlD4IWd7hPVeIiKUaBYiks1kiRt7fWbhPAprKzwdWkNAYla406bGKnnrb03CNQnP6Zu33l97Q7Z9eMaMi0-0cOsAfx30nG6mPmfPJJkNnkQ_gY3bWWJADVIxNQ4xr931x-dYP9UtOTV5MxYKV4K5uGdXm_jxoYa3lT7KMeeOzECImyX15yP3tGXM9nRlJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت جام‌جهانی نصف شب با گزارش سرهنگ:
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/Futball180TV/90530" target="_blank">📅 00:48 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90529">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aEooXv4bGZQk6VC8ADlhm1mMNPsCmG9pKxrV5wBvcZKGD-zpTYElK6WOwcWNv3N5yDNMm0zcnAfG29KjviX8KUfITBrEJBOzbhIpM7Z6R-O_AMmFyz51twMeUb9_RYzty7EW-YNP7wyp4Pru-Tqhwr6-jAvABSZK0Dfio87zHKJW2LLRsjnTayVm10sa4Bw2ZFSX8SJGpSNU4YBcLJRbUoHNObsJrsaVJhasTeZcOxiY3QgYppDsqBz2NugSAtySf51E29JqosakMxwsLYrQ6M9TRzye9a8FEF41mSqmY_u_VoieXcPEww78nSUtGY9ErSWxtA6Zxb9EoMw8CSLY6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امباپه با 15 گل زده آقای گل این فصل چمپیونزلیگ شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/Futball180TV/90529" target="_blank">📅 00:47 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90528">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00937b1a6d.mp4?token=ZQWBkTb6eASFItgI4q9oThS5iFcSh2xWNgfHwmNEx3sQgkRwyb_s4avY8rzlt9b5dQT3wPwZWuQuSSqwlhn35koS9N1NdBYCE9LZ2czYCfAHl-q8ElO4vu4bEKFrE1s0CBNxOKnGXSIcG-ugDOq71Y85_fFwwicP66gQHoPEZTZNFD0Ybn6rVg5OXg1qI7iEPmOG78uWv13hNDJKYLhmGgasI4YnhqBBlbE_CWerbhYgMAiB8AogPyeHw3RJTkr5Y4jQWKLsD4yNRB2UNKCmYg6FcsT5prlViF6cRQYdtnfx1d8pGSHYtIcW2ZK42oQ0Spr6Ym_NlcRSptBc6WdFag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00937b1a6d.mp4?token=ZQWBkTb6eASFItgI4q9oThS5iFcSh2xWNgfHwmNEx3sQgkRwyb_s4avY8rzlt9b5dQT3wPwZWuQuSSqwlhn35koS9N1NdBYCE9LZ2czYCfAHl-q8ElO4vu4bEKFrE1s0CBNxOKnGXSIcG-ugDOq71Y85_fFwwicP66gQHoPEZTZNFD0Ybn6rVg5OXg1qI7iEPmOG78uWv13hNDJKYLhmGgasI4YnhqBBlbE_CWerbhYgMAiB8AogPyeHw3RJTkr5Y4jQWKLsD4yNRB2UNKCmYg6FcsT5prlViF6cRQYdtnfx1d8pGSHYtIcW2ZK42oQ0Spr6Ym_NlcRSptBc6WdFag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عادل گزارش امشبش رو به این شکل شروع کرد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/Futball180TV/90528" target="_blank">📅 00:37 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90527">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UEFF6tiFu00JTRKSY0w5Z7_isn02kpNQTEq6tyof-Hd3tqeKELBnx9QbsOqwQXXh6Vjg5kfGs7CJPaEaLYLQAtffBhKF21UNTVO85d1CLNVNOo3o2vTA-cNomcfw4EmEnQJicYR-LzDxMgEWo4HSLSNwSJ1NI8Q41Enaur-lvXlAIuFfPpVKocjAfExXgXuJee9yRHiU2MZOQs8EszTE__pYszfETHQYM96cnjl1dbJ7W4c1QYfnuukwp4tgDNSZ9_QIE8FjKifCRXOXHBTgU2wxLIlEK75Mcqc6iL4oPRMQHshyzgA3ov50EHxzLfXGg0_SPOl1_9tx_bb8qooXYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست کریستال پالاس برای ترول آرسنال
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.88K · <a href="https://t.me/Futball180TV/90527" target="_blank">📅 00:22 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90525">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qz7Bfe45kBsvH0QRnb5Hu4anpCBu6l1uROrqoulN-asZYRtYr_WOLXoWM9WDwm7KElkg3PxADiZvjj1vuB9B1Qs7Cc6hXvL5XBXkwivRcvFrAe4TgyLoZw71QttQ-qalTYjZDtixvSHPKL9_M3y4Khtg8W-V-37M02KS4Llkmpgs967q70zWsRngl5f3D-U1EphjngnYOo1zGaeHLHIOSHEZ_KssNOKzHLHEldJxTisSeflQ6EoSH7ha9EiGsp1m2ksrGq6sHxXX5-r6uYm7qOySvAMbr-cpC0LFHgnvV8EC0Mo6f_hg_PcakZfUvBDzh85fKcSI1FiTR8XRxkZWCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میکل آرتتا:
می‌خواهم به پاریس سن ژرمن تبریک بگویم، به ویژه لوئیس انریکه. آنها بهترین تیم جهان هستند
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.19K · <a href="https://t.me/Futball180TV/90525" target="_blank">📅 23:52 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90524">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vDUKIyR4akDESRIa4Jn7stYsyejDS55iqPEW3s9slEZgHN5ouR6uQT1NGc-xGcvVGQ6dJAl0PKAhKna3dAjJQ06TfoSSpIaRCoUHyoxFESYeTFCWL2oA8-0keV4CWJ3of-BQFOVItALEYxJLgU5rPlnprbnGvtYo6Ol3WTrQwjmjI_S6LFqbBwjARP18PyrTaM9cM2ZlUyvuKuRYpBAZtl2VvI2L_PaZSHpzQEhM_xupUcnqgd6YQM5xUGYqr3rNR9gMLiNPEWi1HSyJw_OWwIn0u33yf7qSokeDQZz4nB1rza9cuX_GlEFEvReUtN6mk1MOOZIxC4hdEofMczXuRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید چلسی بعد از باخت آرسنال : به لندن بیاید و از این جام بازدید کنید
😂
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.44K · <a href="https://t.me/Futball180TV/90524" target="_blank">📅 23:19 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90518">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LUKwGwyUay_TNZYUh5SwDB7frAlAEP0cfnbmiUxSHwaIb1InBg3P1BREMVH1-gBIwXisMccLb-o_YxxsNLtKbznKoDJnPPlJGtMcc1PzdMaBWQbg017vsQlr5pAiLHZrWL0T3BloFYV_JON7gU7gyMHUlPOCVMb7XKa0y7xhTHQElZoZIQb2JlP8KmubS2LEJFnStVkaYzdI-HzfZK4n7vydcVRuw7CJ1qDT_DoQU-b-_BYy0nc7bu3veagk5KX7QEL5mCzj6lfYO7r6nnP7TDGYo1NmUXKMns9aRD-atJM63kzsx-CVwJi20fkb12deuWTVfljZo0L4JUFewjIE_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cxW1SyfsabYk9C239zdHP5rT7--fdaMP8P4SpmvB9uPk35R08S8onrGl7pmd-qEnvW5RNVXcImwC39nKb77fixKHaXgplq0Ni1k4xkKvGZqM_ueKxvEQdJm3aHyojaUjoCq8Tc3Kpxt09BQ7NIWeMVVr3nbEbN3GcCNe36hCqzDmHZBjMOkfw2bnUi3iBXk1Cnm3TaenV17bgo7qk_9D9Pp-25LoQ5mlemLq0QH6CJkQ0y7joh28SZhQHN9jTfMS2JnptomMr2C1D0IxnS8BlizVzzEwD9avntEXl6Q61shOgnNdgi2Ln2LIj5RYKuiEqPeNfiiTcuAo5RdSbCkLpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QF0gRPgZ3_iGY62BU2NtVtRhzT-EsoJdLrDOWuSfhpDs8A77_IUUbuEXLjh5gwsnu_VTJo38kveqDvb61FvOJog3heJuv2IbhUyRYuzSEBGWZTiQbdvGMHaZWXRBUVJHbWMXN5LsdvaC9DEXWgs1Nqzxdkc3IdJqrF8OspoabljGygDLJN2bX_gr8SebNprW1w41cZVK9490DW8PDYUWj1c1hIuZZW8eSCVwxPb0HBwZRsGHyJqwkxWTs_WYQg2Yw4-034E60oKomY_gz_FabXN4RsFwsyHfHKam5959TEhRSYlWsEjInIotz6Pws_uq6tI-EiJ6MVuWGDIMI8Nhzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VScfe9IOJw_3zPjSedJjb0bwJMv_qs5m9CewOlshfM8GAHY1oWUGIINhUduXJEt93-CzkJSXEJTlOtdplnuRcV8_4LzO-GAIGRzAsMDeLNjSiDKSZht8-rIVAHwCil_dqVxk44EOFbG6JXjXBply6EOeYclkno0gHUgm4UKZ0XeWjSIYA19eMT5EBTb7MjPwxLUVt4GGCKXhL1YavwHh-Ucsakqqx_CP5GpxnqMNQxO62kMtnf9GBSzi0KgI56SrH06Byn_HEDKO11vC14AvNAYNNpKM0YEn0eFYnYY_ojMOO8BmTzbtk3bPqoPv8_aHqfHcheGwsUBZoIJ-CY_vRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vzZVn9UCo6BFVKN1yx5YzUVfK8AdXbh9aKnstKxrrvTWeaBYFJvYLO1kTAeKa3fwPZ2W8sl-AsaaWGQ5GzuiSkSSDji7HuO0V1DhbhNtZ1_lSGPbjm8tt5XYpKwV4LwAuohNxjohxR-TrZOn4s2ojXGYW_XcREGzKihw0WBpfELQbfCL2FjEpZusKqPCMi4tF-weD6kFGONKSsztTrYnu_XMUCWly6EkAgWCLon5qA6ucUW60IsmoOWf6CCFnw5_jtRkd1YRVOP_1cPFowDuMXnFZlmhUNxTeaF2tfsVSj-x4Ttbm3wMafnKTrfOddARd9-LqHuhI1gttR4Mn2uHNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oQuH2_ub59R146xfuGdKC-FlabE90m-H4NFA-_mF3Lsp9YPY3gYCQUmvjTKTKMi27DFfCmg9KaI3K4bLYO8TTiUW251LC-XamfsEcTYjsvdFyCDseD-IIiO1wEw7oMcpKjeDz8MX1n7jq8fsqSk5f2ursbFQSU1jhChVHq84XbgZ7SDn_983pSX11YGBBUVaXVSJMwcCAWLVjmqYFGico67s0mw9S-cYzGwNprfQos9oyIfq7pVv4mIS8WTlQeizjsjmypvo6Xn0Ts9qVzfB23DAUUQZwqw31F5uPrw6BS9Rq__vOUUxz7QIH3FHehw49f8ey3WXTtKVWsxA83tNEw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تصاویری از جشن قهرمانی پاریسی ها پس از دبل قهرمانی در اروپا
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.37K · <a href="https://t.me/Futball180TV/90518" target="_blank">📅 23:08 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90517">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">عجیب ولی باور نکردنی!
امباپه دو سال بعد از ترک پاریس: 0 جام
پاریس بعد از ترک امباپه: ۲ چمپ(بماند باقی جام ها!!)
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.6K · <a href="https://t.me/Futball180TV/90517" target="_blank">📅 22:38 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90516">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/elthntzkPkCnSkCqR1dKc3njDAhPO6h5074f5wnbcUfJKr4fv_KWWmRGb76c49tB8O6j5Yxd_0Tyk8Ys4HinUELOHBtJ89LSzJ5sWWQRFofbRubsDmDsIZ7lUiVIgg4o5-XPVIbo2EyYVyPMaEjq1h9s335w9SiyYi3t7ITGHDipgB8gOQTxU_2rN2nnuH5w-5dHb__qIm8aHS-Rz_WuCbMWgJQ6PGgaimP_xUf2mCLQQCN18jH8xMBhU6A2krvHAlaeGaUYj_ZKiZIdh11AXoVJeNZzxTCZgFgnPxhZ07qynwcvwgZ7f6I22GBFNPgJNRCU-duKztnb1DIrmYCUqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
آلمان
🇩🇪
-
🇫🇮
فنلاند
🏆
رقابت‌های دوستانه بین المللی
🌍
⏰
یکشنبه ساعت ۲۲:۱۵
🏟
ورزشگاه میوا آرنا
🎲
با بیش از ۳۵۰ نوع آپشن پیش‌بینی
⚡️
ضرایب شگفت‌انگیز
📊
نگاهی به آمار دو تیم:
✅
آلمان در
۱۰
دیدار اخیر خود،
هفت
بازی را برده و در
سه
دیدار شکست خورده است.
✅
فنلاند در
۱۰
دیدار اخیر خود،
چهار
برد و
یک
تساوی کسب کرده و در
پنج
بازی شکست خورده است.
📈
میانگین گل در
۱۰
دیدار اخیر آلمان
۳.۶
گل در هر بازی بوده است.
📈
میانگین گل در
۱۰
دیدار اخیر فنلاند
۲.۶
گل در هر بازی بوده است.
🎯
پیشنهاد پیش‌بینی: مجموع گل‌ها: بیشتر از
۲.۵
- ضریب :
۱.۳۰
🧠
قبل از ورود، بدترین سناریو را مرور کنید.
🌐
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
💻
@BetForward</div>
<div class="tg-footer">👁️ 9.35K · <a href="https://t.me/Futball180TV/90516" target="_blank">📅 22:37 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90515">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">پاریس دومین سی ال متوالی رو کسب کرد و باز آرسنال ناکام در کسب قهرمانی سی ال
🔥
🔥
🔥
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.66K · <a href="https://t.me/Futball180TV/90515" target="_blank">📅 22:31 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90514">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">تمامممممممممم</div>
<div class="tg-footer">👁️ 8.7K · <a href="https://t.me/Futball180TV/90514" target="_blank">📅 22:30 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90513">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">گابریلللل زد بیرونننننن</div>
<div class="tg-footer">👁️ 8.79K · <a href="https://t.me/Futball180TV/90513" target="_blank">📅 22:30 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90512">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">زد بیرونننن</div>
<div class="tg-footer">👁️ 8.83K · <a href="https://t.me/Futball180TV/90512" target="_blank">📅 22:30 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90511">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">اگه آرسنال نزنه تمومه</div>
<div class="tg-footer">👁️ 8.84K · <a href="https://t.me/Futball180TV/90511" target="_blank">📅 22:29 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90510">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">گلگلگل برالدو هم زد</div>
<div class="tg-footer">👁️ 8.84K · <a href="https://t.me/Futball180TV/90510" target="_blank">📅 22:29 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90509">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">گلگلگل مارتینلییی</div>
<div class="tg-footer">👁️ 8.87K · <a href="https://t.me/Futball180TV/90509" target="_blank">📅 22:28 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90508">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">عجیبه صداسیما تاخیری نداره</div>
<div class="tg-footer">👁️ 8.75K · <a href="https://t.me/Futball180TV/90508" target="_blank">📅 22:28 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90507">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">گلگلگلگل حکیمی هم زد</div>
<div class="tg-footer">👁️ 8.6K · <a href="https://t.me/Futball180TV/90507" target="_blank">📅 22:27 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90506">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">گلگلگل رایس زددد</div>
<div class="tg-footer">👁️ 8.52K · <a href="https://t.me/Futball180TV/90506" target="_blank">📅 22:26 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90505">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">رایا پنالتی نونو مندز رو گرفتتتت</div>
<div class="tg-footer">👁️ 8.32K · <a href="https://t.me/Futball180TV/90505" target="_blank">📅 22:26 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90504">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">رایا گرفتتتتت</div>
<div class="tg-footer">👁️ 8.11K · <a href="https://t.me/Futball180TV/90504" target="_blank">📅 22:25 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90503">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">ازه زد بیروننننن</div>
<div class="tg-footer">👁️ 7.94K · <a href="https://t.me/Futball180TV/90503" target="_blank">📅 22:24 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90502">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">دوئه گلگل</div>
<div class="tg-footer">👁️ 7.89K · <a href="https://t.me/Futball180TV/90502" target="_blank">📅 22:23 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90501">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">گیوکرش هم گلش کرد</div>
<div class="tg-footer">👁️ 7.72K · <a href="https://t.me/Futball180TV/90501" target="_blank">📅 22:22 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90500">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">راموس اولی رو گل کرد</div>
<div class="tg-footer">👁️ 8.03K · <a href="https://t.me/Futball180TV/90500" target="_blank">📅 22:22 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90499">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">بازی آرسنال پاریس به ضربات پنالتی رفت
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.14K · <a href="https://t.me/Futball180TV/90499" target="_blank">📅 22:15 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90498">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">امروز خبر اومد چشمی جام جهانی رو بدلیل مصدومیت از دست داد ولی چشمی امروز در تمرینات تیم ملی شرکت کرد!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.01K · <a href="https://t.me/Futball180TV/90498" target="_blank">📅 22:10 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90497">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🚨
🚨
⚽️
⚽️
⚽️
اخبار داغ حواشی فوتبالی و تحلیل‌های لحظه‌ای جام جهانی را از این کانال دنبال کنید
👀
اگه می‌خوای جا نمونی، همین الان بیا داخل�،
👇
👇
👇
👇
👇
👇
👇
https://t.me/+5NhkIyyAtBhmMzM1
https://t.me/+5NhkIyyAtBhmMzM1
https://t.me/+5NhkIyyAtBhmMzM1
✨
اخبار داغ  و کانال معتبر
👌
👆
👆</div>
<div class="tg-footer">👁️ 7.88K · <a href="https://t.me/Futball180TV/90497" target="_blank">📅 22:00 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90496">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iDBl6DlbbQbn_Az4IZ9ZeQw5V5RFPb1GKH__xybD1kRRqdwh_wuz4UPPC73lJ_1iJUKPzgX4PmnicEv9rzb3m6oNgpmZZ9aTeowkqu7V5e-CPhGyCaslcjfbjv1rz0vyY7ucpXAG_EOeYZQbNLgbYvxXYDOlOta4fj0K-rYlBWsTANQhkVGV0i0qVLG9J4Lum_69vHkMMPBqYbJ28JiZZdpCd9aiTjZGnj1jGDspHlxxhi87OejEFTSY3iXodSS6NxUCdfsGBMXPgzhfb27KJbNmb7-O2Ety5d4mMP6VuMyTYmkgr3EmfI2tihQgpw3aLOfmZ9stHw81wGrTNzJ6aQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری جدید یاسر آسانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.05K · <a href="https://t.me/Futball180TV/90496" target="_blank">📅 21:58 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90495">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">موقعیت های مشکوک به پنالتی جذاب تر از خود بازی بوده
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.69K · <a href="https://t.me/Futball180TV/90495" target="_blank">📅 21:57 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90494">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">پایان ۹۰ دقیقه
پاریس ۱_۱ آرسنال
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.6K · <a href="https://t.me/Futball180TV/90494" target="_blank">📅 21:32 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90493">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/375a1431bc.mp4?token=Fl3kFqDe9OequnrEJIvsTwm6ywqJc3zDt1FqutY3dwsrD_Neye6xFxl2oMorlN4JXDK5-TuZg-8sb8yPVDW8WIP3o9JYkCOdlMQ1H2f_sVg-1-Q8oyoeBnWJAkbcpWQHN6gJgI-0CDsxF31sDXa-Gz-_D5G11I2tCfh1_C4Fb4kEr4a3mPwM1pDBbm813SHLq7ZqakZ9v_9LMxPqO7UiUH06bllYkN0LHyDWJgg8dXs0yRPH8yqvTcZ_JehT9ya3cdt9sGIziTf39xtAyawVTqZqkg_roezx5qqLVytzC5h7-7a5UHYeR8YfCUYD2jH8X1sjH8jvMfXEjETbheBZHw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/375a1431bc.mp4?token=Fl3kFqDe9OequnrEJIvsTwm6ywqJc3zDt1FqutY3dwsrD_Neye6xFxl2oMorlN4JXDK5-TuZg-8sb8yPVDW8WIP3o9JYkCOdlMQ1H2f_sVg-1-Q8oyoeBnWJAkbcpWQHN6gJgI-0CDsxF31sDXa-Gz-_D5G11I2tCfh1_C4Fb4kEr4a3mPwM1pDBbm813SHLq7ZqakZ9v_9LMxPqO7UiUH06bllYkN0LHyDWJgg8dXs0yRPH8yqvTcZ_JehT9ya3cdt9sGIziTf39xtAyawVTqZqkg_roezx5qqLVytzC5h7-7a5UHYeR8YfCUYD2jH8X1sjH8jvMfXEjETbheBZHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
گل‌اول پاری‌سن‌ژرمن به آرسنال توسط دمبله
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.98K · <a href="https://t.me/Futball180TV/90493" target="_blank">📅 21:03 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90492">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">گلگللگگلگل برای پاریس توسط دمبله از روی نقطه پنالتییی</div>
<div class="tg-footer">👁️ 8.24K · <a href="https://t.me/Futball180TV/90492" target="_blank">📅 20:59 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90491">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">پایان نیمه اول| آرسنال 1_0 پاریس
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.44K · <a href="https://t.me/Futball180TV/90491" target="_blank">📅 20:24 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90490">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">چییی خراب کرد پاریسسسس</div>
<div class="tg-footer">👁️ 8.51K · <a href="https://t.me/Futball180TV/90490" target="_blank">📅 20:14 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90489">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/asa5CulCveMH50O4vJdLzIzmEUengE3JqHAN7d6rVKS5Ze86ykT-Kj6UuYWjQPlVDdKQmpQgeQLWRFIfG0s34LTHosQ3u8U0i0e7t6xwkF5XAaBfdoaGjWxVI8WNZzLq11Dd9aPIWlwtJv7yvB7FbSMWwD8qUnIj3eZQcPjD0S6vZnV4uvh3bjer239iiuId0ds-1JrkOuFHddujOhIBPe_ljZFtykj7b7HqtrcIJe5EAbNjUET4GtlnEkZ_lmNNbiymFC4QPkY1TsdaJXsVlZcOJNVnDPBBxaBJjGq3I4nEstQtfUGCsDq6cEMPXZ20-ljdG15jCERBHJntaoD9Tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آرنه اسلوت گزینه اصلی مربیگری میلان در فصل آینده است!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.7K · <a href="https://t.me/Futball180TV/90489" target="_blank">📅 20:09 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90488">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eNUZWDgXMwoNCYYtZcFsSa6dcwz4Vs2qzNFYbNPVgKEV5R8Lj15kjs0ioVliNdCb8qH0u9QkS6WHKxGqn-c6pzP50WIHZGyhPHApHq15n--LOAZAAiDSfihteRysr6YrjmhbxHVvFb58B6b4YGywZXtKDyrmOCcz1N690Wa2dWN5Rm9whvcixLO_XoBOYe-qPG1qcsQAMCL5-dQatHZaoYe0xK-KIyofKvTxluGFuR6uxo41fbhbUlZB6h6a9FhnVvu5d1Ij682b2OABk-kjW-EbT-2kWGwHY9MCDYyNjp98CWjOoTpGQTxhVaELLh2z6i662AW9fN-kpXYfajL4rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پنالتی پاریس گرفته نشد!!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.26K · <a href="https://t.me/Futball180TV/90488" target="_blank">📅 19:59 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90487">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">derbybet.apk</div>
  <div class="tg-doc-extra">52 MB</div>
</div>
<a href="https://t.me/Futball180TV/90487" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">📲
#اپلیکیشن
اندروید سایت جهانی دربی بت
👍
اسپانسر لیگ انگلیس
👍
🔥
امکان شارژ امن از طریق کارت بانکی
➖
➖
➖
➖
➖
➖
➖
➖
➖
🪙
همین حالا عضو شوید
👇
https://t.me/+aCbq7yy8QY80NzQ0</div>
<div class="tg-footer">👁️ 7.21K · <a href="https://t.me/Futball180TV/90487" target="_blank">📅 19:58 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90486">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LUSQzErxtqwFl29vKeqpu-CHr_8TGvWP3JiUhQVRPqctgKQJdOQ9xC6P58ffe-Xfs8kBF__6foON0z5meo_IXxgCh8cQ8X9EBykmFLgghHWK9r8p0DRilb1dcvpfpF3ogZFD-MNjnSYh1NEwg3CgbyLBiexykCxZBN1uGcrVpjYQOv4lGZ-t1s2gowZ3nTU-DFi6M_0hd3YSx8YFU-wx5dZWzAt9TtiRQUU-eClDJ81ZzjCmEnp1C2EJ4Q9YukeWCCW5njDo8lrUsCG8QApPt0g9ZJ4zSpVPePQCgstF_lRRONBdRXvtCcI3IA8WduKiBHdmiaDCrBae8lZFFfRJ3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😤
دنبال یه سایت شرط بندی بین المللی بودی که به ایرانیا خدمات بده؟!
⛔
👍
دربی بت همون انتخاب  100%
💎
ویژگی های سایت جهانی Derby Bet:
⬅️
امکان شارژ امن با
کارت بانکی
⬅️
واریز اول دوبل شارژ می شوید(بونوس۱۰۰٪)
⬅️
پر اپشن ترین سایت فعال در ایران
⬅️
تسویه حساب کمتر از 5 دقیقه
⬅️
برگشت بخشی از باخت به صورت هفتگی
🚨
کد هدیه ثبت نام:
GG007
⚠
️
برای دانلود اپلکیشن کلیک کنید
👉
🔔
کانال دربی بت G9:
🪙
https://t.me/+aCbq7yy8QY80NzQ0</div>
<div class="tg-footer">👁️ 7.4K · <a href="https://t.me/Futball180TV/90486" target="_blank">📅 19:58 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90485">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SFWhTnOTjCMTvFNOhCH_m_emTfXI02jZpa0AmteH5qTwiM4mA-T4ppdf5nZviMX9s1OMt4u1zvuUyGe0r8vym9iHkgTbZrQaSSAP-emrx9w82x1ZtxE03WvMMaQO-ECLJNGsjjjBZ-zHSKt_sj_rrsITGJ4p45TZm4jpV4hrrsZVssNsrC5Blw7ydjooI-j0dBd6V-xDZhe9VGMia3AehLOH8ajqetrmfOHZE5uT3XFc5zqoGSwJx5JbHzNYp0aNwmOTh-dn4rOwkbHx1SngfxdBtd5RxEG5TdqZN3ocpWpBdYsASMErHo8DP_t3extCECjtbipEYQrosma8v8mWeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پنالتی پاریس گرفته نشد!!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.7K · <a href="https://t.me/Futball180TV/90485" target="_blank">📅 19:55 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90484">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/71e697023e.mp4?token=RRvSBSAcur-SOGrEP5WaG4apj0SNhjPldFEY1oeIFkDvjbOI0BLUYvdaaoo1jaegGRWqbsd83i-TSx2frd_JH6wkq84yFGIbOmeBHVQqeMsIpJnP_1uL1sCVScVpHtfton5iR_V8U8uw0CepJ1xJu4TlK6R063Mgy2FKkPTTuMB-HNqvOlcxtIlPlN9Tp93LbOXMrzZY__UR60Z8pl8HwuuZo6YHUncQUeqA2ldAI7WDJrIdJ7KSs7TvNHqeb8fuW4eo4RF_B63MIUVYrVsupi5EbDvoZSFCl1dmJzXnepU8oqrqJdljOrlVX1ulP8nNT4FHWHoZn35xOdsooG1Dfg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/71e697023e.mp4?token=RRvSBSAcur-SOGrEP5WaG4apj0SNhjPldFEY1oeIFkDvjbOI0BLUYvdaaoo1jaegGRWqbsd83i-TSx2frd_JH6wkq84yFGIbOmeBHVQqeMsIpJnP_1uL1sCVScVpHtfton5iR_V8U8uw0CepJ1xJu4TlK6R063Mgy2FKkPTTuMB-HNqvOlcxtIlPlN9Tp93LbOXMrzZY__UR60Z8pl8HwuuZo6YHUncQUeqA2ldAI7WDJrIdJ7KSs7TvNHqeb8fuW4eo4RF_B63MIUVYrVsupi5EbDvoZSFCl1dmJzXnepU8oqrqJdljOrlVX1ulP8nNT4FHWHoZn35xOdsooG1Dfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
گل‌اول آرسنال به پاری‌سن‌ژرمن توسط هاورتز
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.26K · <a href="https://t.me/Futball180TV/90484" target="_blank">📅 19:40 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90483">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">سوپرررررررگلللللل کای هاورتززززززززز
🔥
🔥
🔥
🔥</div>
<div class="tg-footer">👁️ 8.2K · <a href="https://t.me/Futball180TV/90483" target="_blank">📅 19:37 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90482">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">آرسنااااااللللللل
🔥
🔥
🔥
🔥
🔥
🔥</div>
<div class="tg-footer">👁️ 8.22K · <a href="https://t.me/Futball180TV/90482" target="_blank">📅 19:37 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90481">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">گلگلگللگگلگلگلگلگلگل اوپوپوپوووللللل</div>
<div class="tg-footer">👁️ 8.3K · <a href="https://t.me/Futball180TV/90481" target="_blank">📅 19:37 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90480">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LvgDtCyBjsjLhIohtJ__Zn073IZxxCvtStX3wxj-l97iyq6uSkm95WGfS1qIiMfh4VQBfUre2PYdmrLnWzk5wXHRmvLhdkILlqC_boovCcuXECE_RBp8Gr9B9S3HSM5a6932SsUYbD8m4gvptrUPonaVRIWiY04tHlznQR1DtGTlIYn1qs1bN6tT5-YzIa1SbkvjJRnV0y3YzNV78zEKgbtQpcLSTFVt21Cpvkk95mzQZpaz_vI0phhuVKEeWqwuNLEf9Xj2umej4AcZfyj_4oZiZOGoePBdvquYtAV0iFQqL7WsyDWqx1WwUx1Yw8wNVF3KG6YZCOmswSl3cCZUKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تتوی یک هوادار آرسنالی از پیشبینیش از بازی امشب سی ال!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.84K · <a href="https://t.me/Futball180TV/90480" target="_blank">📅 19:21 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90478">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pb-9OAGue9OcoYG4tY1SIUU7GRbjzMqixWLgc2X602pb6feSeZUEPbCgFkOQUa_H3rh5ms0RF26YJSg3P9qqDExp5zKmQKcs5c-Z4z9LVLvplOozgztoeDH88ieZOPxZPlktOY0MihSF2pOvolkv06Ioj8m9RVN-OmXp0uDovZOGs0fDnhKVLsjVEa-UojnBLcKrZr1iZB-3-7hZ_Mt39--23R_20FNzU7hjvafdHtHUlhdAFhhf8nNE_5u_eOkkwbz4PNSrlVIE1KsUaxXiTx38GOedJrYLFD1LLKncCt819zdtUvXguS9gTYE3Ziiv-G64dudKfrK5wwy77mz7TA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tuuoF5xZSqH3xRaemvyV_9UoszaJZqaPXZH0F5W-pg5QOKGF9NravdYOCEjrpw7A46JMkBzX1BrrNV1XfiP6DiLP4HIN0ctbcQhEC6ys2Dk0oc7e5acbs4S0GZKERr4FFkdutwDBpijJHE-yy7CyQdxrvPe5SxetmvUqDL8UxXQsZ9kI6AIl1AmnUz7tfl4dugJptaizMKBIU2d_AYaZMX0EWWd-ONwWJ5LRPmv6kxlmDTLBfqXrO0vxZNFOsg9zCWDd_pk2sxUlSnAimFY9dhDfR-TKUS6qM-VhVJD79kXQVIMWUHgn4etpkhI5VUdlSakPb28CEQMe7YeH95Rb4Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اسکواد دو فینالیست ج.ج قبلی و مدعی های ج.ج امسال
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.96K · <a href="https://t.me/Futball180TV/90478" target="_blank">📅 18:20 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90476">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VhgMv-B73FDLNWiXM3hZ2jCArF54UU9zeHkmXA3r4C9PEfKUpn1EQlTNMUkqmsNxdAN1Q-uMaVOu2R4OAezhzyo-gfg-sFdv7mc8C3etw6EIHU7B8CGdXIy3dCRhXKFpSfrFpJ7FONuVhq0uzNOQvT6ojortoqKjxfzr6C1kMEGldq-s0Jbp6E_LXTjCb0jSudrLG2ZWdQEBxpQobcE7dqDyB-AhMKeQn35ghMfz0X-uCL-TVLxrc9tSIkdAqMCPELvvdHdPwmBD48sxmLTNI2C87S3nTqtxyC93Tgl8C6Op0KQGQ9R1kOvnFA_y1ODn3BD7UrgdgAuIkg39t8nd4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j1MhvFcXu5Lggbm9jH0npklyNTPiFC1HXOOQvf3ruvaUtx0zmzP-ckznUoU7_EusCWKjhpd7fGZJTgdq2HCcXSNXifeGWfXeqX30LLZQxbCqUjqxuPrpVlwKwFq30E6OFHXRb8_FiqGPgcCGgv36cce6zvuwuPUL5_aovu5oho3jgY-4yGZEfQFSO0sZQ3M-ylYS7UB7AwKggyP5UapVTniFq-2neYQKh8e8UhYsu6NjiDcniHpZ8AvSw0wsAMDncCVD1WuGbo9T2xcHSJUPjhGGkMKpyTHvOj2KHv4r9AtOO_WM3zKmgQqHz6NlorWIumxFYQQytDkg9IG3fVEIQw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
ترکیب دوتیم پاریس و آرسنال برای فیناللل
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.01K · <a href="https://t.me/Futball180TV/90476" target="_blank">📅 18:14 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90475">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
❌
🇪🇺
با اعلام دبیرکل فدراسیون فوتبال، لیگ‌برتر رسما به پایان رسید و نمایندگان ایران در آسیا مطابق جدول فعلی معرفی خواهند شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.2K · <a href="https://t.me/Futball180TV/90475" target="_blank">📅 17:47 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90474">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AoL2CRZ3rUshR8tz3_S7LtP2Y0-e_P3MGeqUBoKZXk49br7EsLCGEBCUOIHWsbiwUUIq1frterAXqz8IUBTeTgXh0hG69L0DZlBO6yr7uurFZthyKz2kjNLa6BBq-I0FxtwYPMbmqwtS7ympFo6Mok99D71HO7cfvEmKtv9JPeK9Le73TGXiQVhCkyOoS-qycUJm9glMXjkV3IxwUVDc07GMciMWZWPzy1Nc-kux96LgOUUcuKyrjTA32irdOlTf8i5FxBPV5_GHIpJnBEJeIvPLZBv66_BcPMQ5kplb980H4F9lUJ807VFfu1O-THIg78Cks6P04HEcJrTFhVHNrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هشتک
#FreeJulian
ترند شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.18K · <a href="https://t.me/Futball180TV/90474" target="_blank">📅 17:47 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90473">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a387H6Ej5MfN8wZ68wFXWoF31kDIVo-hK_C_fZeTVgXUvAH-ZSvW4ug9pqdUMKCjOCsVU4JbnxLWK88-TYaofkrYY5iIxgjQzi01DT9xdpDVYHprSZ7kxybicdx5CVQn6MWF6vjAz9iyr4JEx5oBzwvsohCoym-Y2zJL4WKd-UmPYOQui7r5mPKwAxwok5sNZ8fKizKERpJm_K2DtflqcRlFMlzkkSTWRZNUoLM3dHYmqLE0xNVuh_RvRdEq2TeHeBxjTmef1DEyBdpgtgl0eAk1_nkKwRB2zMo4VCAUYDPAkoIIdh-5KbOmLC5BZvySVrXX6kEnDuilYv9GSUAEqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
کوپه :
بارسلونا درحال مذاکره برای خرید گواردیول است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.5K · <a href="https://t.me/Futball180TV/90473" target="_blank">📅 17:19 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90472">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46a77e89da.mp4?token=plELs9vaWvZFyadNz0IU4RyWOSON_jRk1_tLanagD5O3eav86IFieI0IimDSebKjpdHGG-YyddLXggwzE8vUDzbGWMIn1bdQHbl6cQDnKRQ6yDf8QjyKmpZ_oGVEVjgddAYHtvFBb2aFvgJG-kvo9PifhArLRWdPJp0W6QhZMatdpFfsI6cwRBslC5DDTtCOTttfrmtH86ByoT6Mn2SCwMAaaH39AWmcTUba_uv5UyB7fvSNmbtjQm-oQWH9uNo2tBryXquk4X2Pg1-luXMlOFKG2GF6cmtpVEiECzu8U5ltvAmNC3v-7inrdDjYBTWZ1xPiyXirmUXsXGxjI_KqhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46a77e89da.mp4?token=plELs9vaWvZFyadNz0IU4RyWOSON_jRk1_tLanagD5O3eav86IFieI0IimDSebKjpdHGG-YyddLXggwzE8vUDzbGWMIn1bdQHbl6cQDnKRQ6yDf8QjyKmpZ_oGVEVjgddAYHtvFBb2aFvgJG-kvo9PifhArLRWdPJp0W6QhZMatdpFfsI6cwRBslC5DDTtCOTttfrmtH86ByoT6Mn2SCwMAaaH39AWmcTUba_uv5UyB7fvSNmbtjQm-oQWH9uNo2tBryXquk4X2Pg1-luXMlOFKG2GF6cmtpVEiECzu8U5ltvAmNC3v-7inrdDjYBTWZ1xPiyXirmUXsXGxjI_KqhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برای اینکه بدونید دعوای بارسلونا و اتلتیکو سر آلوارز دقیقا بخاطر چیه فقط این ویدیو رو ببینید
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.77K · <a href="https://t.me/Futball180TV/90472" target="_blank">📅 16:51 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90471">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N6ScJ2Jehb0756X9uAMXJntoVfvkNKj9NUEtzQVardKxgmij2OStl-qU4-PSPWFzlVtEvW-qgLGfIMhs4P6b_tMCCElzkqA40RJF53zT6dYv6AcidLDjmz_CNun3MkxwKjeZLZsTLAiRRAOMWhuG59Ma49UsYQdZyDp-oW00gLe7b9wrEN8TbuXPd1P4z449G2HZbxOrgB-zJjQdqlJcjqfoWNxqAJ2nAzU2B7qTikkeHAjx9_f0XW060tNtI9Q52z3wjE7pASFd2XQUDdGrfEY6llaXBqcoZ6AqYvEDMPUDGbAIjXE7Er3iJIE4jyi_aDjTLzpQYSUVtAbRQbg8hQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
تمامی افتخارات ملی لیونل‌مسی در آرژانتین
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.55K · <a href="https://t.me/Futball180TV/90471" target="_blank">📅 16:25 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90470">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d9c775485a.mp4?token=F697EZOUg9gtZ0bGoMBZPfXCjvNSFxDpM8rtE_QzyYYq-vEQ1dTDnpEU5kBneaVwGsNWgSwyzFoWah8EvNqq9MwRQv6AM2MEEF_ASuMaOTTG2qQgUXYsbX7JX4vNBlEl35zcIh77HrkuyQWBCIiyIFcHClxs5NgoQknJL6N7RyUVVw7nUQFKvVlm7PJk7NqPZvfrQ2Vo3-KaDN9KAOVmoB4SRB6frX82XR4VsFFpPFgW_TyFdb04-eAsoDEGGtD2q59f8kVltKNKwovFsoPdG02_IsEGMd_bK3Os2RhhVzYRFDLYduFi1tYx00xsWAV7Dh2ZDdoOzePvfRpCxP0V_ISrjptM3KcgvC86-yp-EzSE5HYJng9QR_MCUOTuQAlVrXP69tRdEXcESPXwijok_Q7t9skz2DrvPljDzvqp8MGbCWYvW5cAFnn0-e7ePwbXB-MZiQCqVKeNN_kvhlPuQuvK6x9fVTIl0ebZhRZ_dhPfDCGB7ggtAbyLeVChPwH7phWcT9oYywL4tIAvrtANgBY6CfayR91auyd3W63QNxuOUvp5lv6fgw3dxV7VLWDki5BEhambtxvlCVm_kSB-gnyHvs4iAlUK03pzHtUJqJs3lC1mWrmcL3EuiN-wWuj6X546TfqJ5t2WUyh7FGJw5eb2TMWRkQvZesHV6voJ3wY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d9c775485a.mp4?token=F697EZOUg9gtZ0bGoMBZPfXCjvNSFxDpM8rtE_QzyYYq-vEQ1dTDnpEU5kBneaVwGsNWgSwyzFoWah8EvNqq9MwRQv6AM2MEEF_ASuMaOTTG2qQgUXYsbX7JX4vNBlEl35zcIh77HrkuyQWBCIiyIFcHClxs5NgoQknJL6N7RyUVVw7nUQFKvVlm7PJk7NqPZvfrQ2Vo3-KaDN9KAOVmoB4SRB6frX82XR4VsFFpPFgW_TyFdb04-eAsoDEGGtD2q59f8kVltKNKwovFsoPdG02_IsEGMd_bK3Os2RhhVzYRFDLYduFi1tYx00xsWAV7Dh2ZDdoOzePvfRpCxP0V_ISrjptM3KcgvC86-yp-EzSE5HYJng9QR_MCUOTuQAlVrXP69tRdEXcESPXwijok_Q7t9skz2DrvPljDzvqp8MGbCWYvW5cAFnn0-e7ePwbXB-MZiQCqVKeNN_kvhlPuQuvK6x9fVTIl0ebZhRZ_dhPfDCGB7ggtAbyLeVChPwH7phWcT9oYywL4tIAvrtANgBY6CfayR91auyd3W63QNxuOUvp5lv6fgw3dxV7VLWDki5BEhambtxvlCVm_kSB-gnyHvs4iAlUK03pzHtUJqJs3lC1mWrmcL3EuiN-wWuj6X546TfqJ5t2WUyh7FGJw5eb2TMWRkQvZesHV6voJ3wY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
همسر پورحیدری: روز عروسی من و منصور، داریوش زندان بود، ستار برای ما خواند!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.68K · <a href="https://t.me/Futball180TV/90470" target="_blank">📅 16:00 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90469">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09651a8d65.mp4?token=RSzJkw1K9qqcoGDrgOZEyV7ONLYbSB0EpekX2p6FcVgApBAZS93v9hAWT5nkeUvsk-n-BJYqv_K-9cf_shktidAA8P8f3MLsgiw_cQTZHfwnUTdWSUK8rigTd_9HTeA6u4uWJD6c-uyX6MNfVWqz_7UuYWMZ1mIYa37Cv5uYn7yj4Vc1TyDgGUzeXGn2qPBkf20UMUatACNNmzB1V6KNlLc-deNKOL996yYKuYKJve8mtM7P1TVQobXaE8i5elVlz2RC040ILSVP-SR1Mp9tBxS7ULvtB4xj-NCi0HpYWwMvp9VvdIis5GpKK2SQpekLa0hvvihF_mMQ9DDA1eaD4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09651a8d65.mp4?token=RSzJkw1K9qqcoGDrgOZEyV7ONLYbSB0EpekX2p6FcVgApBAZS93v9hAWT5nkeUvsk-n-BJYqv_K-9cf_shktidAA8P8f3MLsgiw_cQTZHfwnUTdWSUK8rigTd_9HTeA6u4uWJD6c-uyX6MNfVWqz_7UuYWMZ1mIYa37Cv5uYn7yj4Vc1TyDgGUzeXGn2qPBkf20UMUatACNNmzB1V6KNlLc-deNKOL996yYKuYKJve8mtM7P1TVQobXaE8i5elVlz2RC040ILSVP-SR1Mp9tBxS7ULvtB4xj-NCi0HpYWwMvp9VvdIis5GpKK2SQpekLa0hvvihF_mMQ9DDA1eaD4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
و تا ساعاتی دیگر، فینال جذاب و نفس‌گیر لیگ‌قهرمانان اروپا به میزبانی مجارستان
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.67K · <a href="https://t.me/Futball180TV/90469" target="_blank">📅 15:35 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90468">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
بهترین‌گل‌های فصل‌گذشته پریمیرلیگ انگلیس
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.81K · <a href="https://t.me/Futball180TV/90468" target="_blank">📅 15:10 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90467">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوری؛ با اعلام‌رومانو، آرنه‌اسلوت از هدایت تیم‌فوتبال لیورپول اخراج شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.47K · <a href="https://t.me/Futball180TV/90467" target="_blank">📅 14:58 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90466">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v_r8mbzqqVhlmCkd0wBqcRqk-2t5LTGzU_nGSWBgBovCepHaf70KOS0_NkKvaU9whE6z95ewKDtwbjGv7pi6J_sa05_vldlwN7yvUiJMiLu2h2DI8kM79shLfr5nGcw6rFewiXam_jivceuYt2lrsVDy2YGO4ufnLVoUkiV8_aeZeSsJ-uLn3xkom7SLMnyEFNTYu-lQGuj9a8dREWDdD2e9dtxtbVv2o-g4NPRnN03dO4qlgliT9BAc4GbOYI8tqSOECzU2KEOVurLZctg-uhhDq3tueok32HuXwtOP5AOK7j8Sk2nC6GUKGLCkkuIuyfiRCijPUfUfrH5YeAj2dA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوری؛ با اعلام‌رومانو، آرنه‌اسلوت از هدایت تیم‌فوتبال لیورپول اخراج شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/90466" target="_blank">📅 14:47 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90465">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uyyf1Gbr80TAJ6mYjB18-AzqRNalXaYh-IYoFRMY53PjQFSi0yXcv07xlX5gVYP2QA5_6uTI5CXmDTYkkKRiGy2Lz9fDtCJ2klh0xLBNB0O0q5kEgWSyGR5U6pkWMqxJKGHNdNSG1R42lf8bleAk3Ecvxjs4kMq7iOcsqcU_oncxUOYGijS-qrbGs_PXyNOyxAxNSgszruD_VdhHvBBky8tbqnVXGxdPOsLkOJSiSixzrujo7_rJu_iQAzXryxkvF-1gAu4Xwy8sqlkxxoE9gjWW6AEHpgD7O95ORiAvV5-LSgymnR6wfsA89DSmiVOvVyZLYuH64IFQUTos-5ZsxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوری
؛ با اعلام‌رومانو، آرنه‌اسلوت از هدایت تیم‌فوتبال لیورپول اخراج شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.46K · <a href="https://t.me/Futball180TV/90465" target="_blank">📅 14:44 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90463">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/H7iZPrUO8S-vEgKGmdh6PHdLfxY_IGqpWM0Yygcdh4iP0q6qsKa0bwWxACesXiwO_hza-HsUDPd0eW41wOJuIJH893RKCdmRwNDjOwrYU5g5dL4FhYDXFoUs3t80-zt6Zpp4op6xfHVrMxulDO7Gf0hDB5M9mT1aCHW859PDsVb4AS5_gbrExmx7pm70t9ntlRECXGMOXy3-mrOUqsKpHydEUBouIAyAyuy8b2sWuGKUySaJJbteuLMU2zh9aQE-NrABedmrP8-Jc1HqP9_TcYMf6apKv-cfZKuRvPNd4tjYq5lmpwPkaX4tCTazLfqICP2upfLq3YbOTBKPzC83sQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/n9JGgrrK2IBjwLSEfUmHezp6uDZQAoDsKVJcrA7qUcR-7W2hyNZtwEr1ByFcKiF26RyPLToF7t2lVGeAPP3xMUoZbZcon1qTWeZhxMSCeQSqlsz7MdbBQ6EWZUS4_8usRywIsRfZ22DpULdxS4y9HsVcvm1iD9HEX01Ch1ah0QSkTWB_cPWwylWMSnXq_zzHIaqBNbOUkUUkMLYnJazfGCelsAS0zN_fPTU2vUwXYCRgYChBNlcWkgl62NvNaPtV5d5J5bo97b5N_JJhukyUpd3WhVVgpgqpwm1kMPIFJpc3ZpwjFCgJWb6LyikoB7Voik_93NNiVTeNaorv0o025g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇫🇷
ترکیب احتمالی پاری‌سن‌ژرمن و آرسنال
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.77K · <a href="https://t.me/Futball180TV/90463" target="_blank">📅 14:34 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90462">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0ec9fa176.mp4?token=UCVFUm_21fDQCxUWLC35HEVc7TKftAjgqVwn7M4VvKTyheKDles3oubw565LIMogd7xsw0AYq_DGepz15pqJtXBVkHDhZAkQwq03Lwv91o-Yr96G0EwvxA8qIlSYar8aqzY67l-Tc7-W4fIiSOa2g3WDAsmV6-DWjnAju09MRtv4uOu6mreRLWpxImHNt0EtTL8uP8xjp5ucralRjtW6ylWWQDG_cICupJAc2_8QKCXZmURtNYhr6D73K3WmLEDn9EvQEbHV-VKoIBblhWZx634orucCKOQ8ransDBqFrlsDulavjpkmEKx921PTJldPfImuxLC-P5_fTZm74MKgchKFzchhf3xrq4iYKjMm3ONFhrhrqiG1dQPWBVI_75haIHvUOTVb_BrDf5JUG4qbm7h4RBUL-trADlKbIfr1w5T38H5Rnc1mFH8mNANK2_9FdFJ_bMolM97FRYNmLmwFN91ZIqFA71nGArv6HaaIJMFWUt7L_xm-sz0DFcBtysjR9J9JqJFeuZU-O968zi4S9ar_AiD_H8RfSKM0ubyYx2QvIo9OG5atd1HzXDoceQdvs1QvhJGBT5PpGsWWqlEwlV5ZqgTErhjnB6_Ss2NHQvvUR0nk2WJHkoqvHG4MATD5y2LbmlpKKS-Ue7DKaX7zbMM2l5GxkNSJJsRYz3lt2c4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0ec9fa176.mp4?token=UCVFUm_21fDQCxUWLC35HEVc7TKftAjgqVwn7M4VvKTyheKDles3oubw565LIMogd7xsw0AYq_DGepz15pqJtXBVkHDhZAkQwq03Lwv91o-Yr96G0EwvxA8qIlSYar8aqzY67l-Tc7-W4fIiSOa2g3WDAsmV6-DWjnAju09MRtv4uOu6mreRLWpxImHNt0EtTL8uP8xjp5ucralRjtW6ylWWQDG_cICupJAc2_8QKCXZmURtNYhr6D73K3WmLEDn9EvQEbHV-VKoIBblhWZx634orucCKOQ8ransDBqFrlsDulavjpkmEKx921PTJldPfImuxLC-P5_fTZm74MKgchKFzchhf3xrq4iYKjMm3ONFhrhrqiG1dQPWBVI_75haIHvUOTVb_BrDf5JUG4qbm7h4RBUL-trADlKbIfr1w5T38H5Rnc1mFH8mNANK2_9FdFJ_bMolM97FRYNmLmwFN91ZIqFA71nGArv6HaaIJMFWUt7L_xm-sz0DFcBtysjR9J9JqJFeuZU-O968zi4S9ar_AiD_H8RfSKM0ubyYx2QvIo9OG5atd1HzXDoceQdvs1QvhJGBT5PpGsWWqlEwlV5ZqgTErhjnB6_Ss2NHQvvUR0nk2WJHkoqvHG4MATD5y2LbmlpKKS-Ue7DKaX7zbMM2l5GxkNSJJsRYz3lt2c4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
به چالش كشيدن اردلان آشتيانى از حميد استيلى تا مچ پايى كه در دوران فوتبالش شكست
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.52K · <a href="https://t.me/Futball180TV/90462" target="_blank">📅 14:33 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90461">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xduqks8hYdGuONE7vanm1gB0wZCD2iJ1TVq-gTxuu0h9FNf-qCvl3T2Miu09OSFdaO4aqAmh4AAbUDaS9JGej8nMI9epHkdCT5UuHwW6XKAA-N8U2T_FGhythyrotByW3EN2tkfsDS-DmdDfbo-JXdW7WOo5dOQ5e_XWlFWZo0k0iMY5XI6v0OeAzeunCIiBjZDx95nr2JvXeUPvMwf7CprhB67FMXOBSLq14x-9ChqzRWLTBGPuTBdT2XE7cQpKf-5fZBom6G-oBEc7Ubsm4UzG93BjFYwVtFQuIUQBIbX6mm9oydRLAWNjurenhjb7hOjBHvY8ow4RfONzTQIuVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
توییت جدید باشگاه کادیز اسپانیا
😂
😂
😂
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.86K · <a href="https://t.me/Futball180TV/90461" target="_blank">📅 14:24 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90460">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EAPnXsdpK96idtRpuluDBkuvNoG2n94CenmhSEO4jlaCWh4AMzbe53yWkLUHLdIlnQGk8SJ30rke50M0dCQfBahefoG0vW8-TYL_oQ7In_7-UXmiZmBt2jQTvwToBbeV1zQBSVvebq5i20wCWOqyCXMzLEuuDOn_zA4CNs5I92PhGDlWEo45Dq5WpQvBhzqePkeAL4vtlE_GFa2f59NI17hROChdpVCvdHo1jk6NfgT_zZnjHme10XVrWdc6YkV4SGDhJ0KiGftAQIZ-QGCKbZUcZFfACpCouS7DGYOMtk-dkJA5QYjZKQtIIQX14Oo1FXUSfeWBfVOtoTbyhQzGPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🏆
🏴󠁧󠁢󠁥󠁮󠁧󠁿
عملکرد فوق‌العاده داوید رایا ستاره آرسنال در این‌فصل لیگ‌قهرمانان اروپا؛ رایا در صورت کلین‌شیت در بازی امشب، رکورددار در تاریخ اروپا خواهد شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.96K · <a href="https://t.me/Futball180TV/90460" target="_blank">📅 14:00 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90459">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/emVepJW_-MOMj9nLIMT0M4lCkhcp4YgYEdbDlbdVQrb-XinC0UZDy3-4On4nUCEDdKVilX9qDgoZnvwWACw6xX9GuFJAOQ_mBUxb0OaFSWlZcDjDyCXobWqWTTUSG0glCRoT1DMRpjdTIj9Ujb8ukRUNUkYz_dFFmygc3RiEJ0789wq-HQt0O50MmGs7CZM4A5f7P5k2di7oEj2YWr3T4oJBpGC3egAbPJpN0H2FT2-QFlj_sWg34zo1PPOw4JeD6eI9NEsZbyBw3Z4H4nZkiJRysLVRUcyXZNmQ8yJNA2ofHy8Ca3sS5hTA8RCa6FV_F1VJcjAs5EINPWyOfKaw-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⁉️
🇪🇸
آخرین شایعات نقل‌وانتقالات بارسلونا
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/Futball180TV/90459" target="_blank">📅 13:44 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90458">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
🔵
با حکم دادگاه تجدیدنظر، شکایت شرکت امین‌سیمای کیش از باشگاه استقلال برای دریافت غرامت ۳۸۰ میلیارد تومانی مردود و آبی‌ها تبرئه شدند
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/Futball180TV/90458" target="_blank">📅 13:42 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90457">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚨
⚽️
❌
🔵
#اختصاصی_فوتبال‌180
؛ فرهاد مجیدی سرمربی سابق استقلال بدلیل موضع‌گیری در اعتراضات دی‌ماه، شرایط حضور در لیگ‌برتر و بازگشت به نیمکت تیم‌سابقش را ندارد و شایعات مطرح‌شده پیرامون حضور وی در فصل‌آینده کذب‌محض است
❌
درخصوص نیمکت‌استقلال طی روزهای آتی اخبار دقیق و کاملی ارائه خواهیم داد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/Futball180TV/90457" target="_blank">📅 13:33 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90456">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PXUJ350gLc9KtttlunSphgIKhqPM9uGz9fa3RTL2qm5prncOUfh2pfU7Wjm2WlStNq57plL3l_FNlBREXsHemA-8zl9AUalwLUKBkpFvPNfNCtEEyVXmBXnehCF8c_k8gzAA-65ZH2reKpaVV-1bCsAJ_T5fGi1DuZiPrSrMQIV9PmyvHk9uMyB75P4KvJ0KhBHYUzx8--XRx1kTWJh7yLZtH2QlQPNJu6XT4hKxi7sEPF4X7gGdzhD4rlVmP8Is52GHzNnZl7jOfRRlLG5H9L4UzAhSdwx-5G5__tirraMDhwbKGc1hJAc0J-BBTtjMNuNHBDlob7C2IMnRR61_pA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#نقل‌وانتقالات
|ژابی‌آلونسو سرمربی جدید چلسی خواستار جذب آردا گولر شده است هرچند رئال‌مادرید این بازیکن را غیرقابل فروش اعلام کرده مگر اینکه رقمی بسیار نجومی پرداخت شود
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/Futball180TV/90456" target="_blank">📅 13:29 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90455">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nh2tiXxgvLjPmWKYQmRCFC5oH63Lv4BQryCMl_SeG4jpP6cJuatFNn3cZd11HUXEkXPFiXnRbBNXuaNgRwa29x86Y6V8fiFoLj9rZV1R0AxenDJC9dGvFmj-pd_ZqRC_7YabKJ0AJRnBE6UM5RugfU4ZlDUNQNxpIpKhsaL_WChCN_Knhr3FpkRzk8KXhYXjV29Tg4BChyMG43q4L9hNWcZlLxrDIHs2H7s1IcDcvncYBqGtwzs4JJP4572XkDeyvv050HH5X6mHW7M9EI9Z4wkOlTYXXbaZfR7Or0FFVhCeFYcDszr44mn0BwAUE3l3AonmuwX8u2U4e_SEZ8y2xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#نقل‌وانتقالات
|به گزارش منابع اسپانیا، باشگاه بارسلونا در صورت جدایی ژولزکونده به سراغ جذب کوکوریا مدافع تیم‌فوتبال چلسی خواهد رفت
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/Futball180TV/90455" target="_blank">📅 13:25 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90454">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PFx28MFBJrypr0UpaxCJBjvYySjwCFxdkWG8HR5-38iob2IjbKynK1WvM70MQOww1m84sLxJJRmm8zi5ipPS8taWrzQ5W2Ykp_pSo2an9CioeyEbigKdHea3zdDIq5eTsMl-OIu_5GumlZFu_rEXjNFemjUk1qhEoaa-AMVlA5aW8zy7eKJiA04mAWitNAnLxIDouUb7UaaVvy26-kPVy2673PYJTl8G7pfKplgDSIts_bBhqEpJHDpGq3cf040nKDg_4mUxlUanMf64h9SDnxLyE8C7wBKmMBvV1sQ2PFDh3VRVBC0yfU8x5eNCrfzXGIUtUYi92w0f_DWfSfZEuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
عملکرد آردا گولر و لامین‌یامال در بازی‌های‌ملی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/Futball180TV/90454" target="_blank">📅 13:05 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90453">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HH5LYGenwZZ32P98JdTzIp03MBr-AbIQwhMDra5Zo2aa85TjnPo9qoJhgae25ZCVhbCSzhtBNnCsHZ6rmUzWltt1fcC7ZGfAQpCM2hkmsCidzfcdvTE5UtXGeL0Rh4Tk5esORiiH3TLP2r41-AQTPP_yUh5EHliypamVSasuI-t7qXdfFW0dVPW-4aY6diWr49hpwESR4bGQVD-02Jf3-b1Fj-WJIxnD9QK7-5WZz8HjRW7TcnJm3-BasZA7UIBjF5kLmwa60TmjIxyu9XcfcvFVrj51XjUIqaoY3JAaMjzz8ybx6SKIIQkEtkF63T86eMpTh2vKG0ll0qqL7_h_tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#نقل‌وانتقالات
؛ ژوزه مورینیو به سران رئال‌مادرید درخواست کرده که یک‌بازیکن بزرگ در خط دفاعی را جذب کنند. از کوناته فرانسوی تا گابریل ستاره برزیلی آرسنال، گزینه‌های اصلی هستند
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/Futball180TV/90453" target="_blank">📅 12:41 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90452">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iIvOHFCwFq6GjtFeQDLb9_YR0_0XVXQRlbkHvJxAvDaIs2PbOfHObgFDZ2OI8he_bWVmzs0zF2NZnuYE48_MFZTlgsoEPdESSGUfXmsTFQ3FlsX-UGGSqcYZtY-_uQFjBfRJyGHiXqolYctCrdwq3qg2GwrgpJAzCKF9fRGXdSffmJxhobJ7DlQiao2eC8Q0LrUKFwLVnbv8x4ZWqyoVzDzbTfWX1A2y445jn8eB7F941CztZ7huadKzaFqWyhGpc__fi1FHK_kAl1SB181F-sA_oJ8evL8Y2ejkuNkcCMkP0C_HbM5qfXrlsspC7SN6HHl7h_k16id371tYOE5pEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه عملکرد گوردون و رشفورد در فصل‌گذشته
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.89K · <a href="https://t.me/Futball180TV/90452" target="_blank">📅 12:34 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90451">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMelBet | مل بت</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">melbet.apk</div>
  <div class="tg-doc-extra">52.1 MB</div>
</div>
<a href="https://t.me/Futball180TV/90451" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🆕
اپلیکیشن MelBet
✅
🎁
کد هدیه 100 دلاری:
Sport100
🌀
کاملترین برنامه موبایل
🤝
اسپانسر رسمی لالیگا
🥇
صرافی معتبر
🌐
ربات راهنما
🇮🇷
برای تغییر زبان برنامه، زبان موبایل خود را تغییر دهید.
✅
ورود به اپلیکیشن بدون فیلترشکن</div>
<div class="tg-footer">👁️ 8.53K · <a href="https://t.me/Futball180TV/90451" target="_blank">📅 12:34 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90450">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMelBet | مل بت</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/W9BKryufdm0Qk-2EIOpmBq3pV9ntcLAVrXqIyjGsmvsvcdaiZ5Gm96JyMYDwc-PeXlQzAC_Nd24zk7vhEgdn8ERSxNgFYwjB9Ax6hylvMHkJ2TdtZty7pOsSlvwQpCWWPiXysF-1Q3a9p_AZbNS-VIVcjp4Cgs2r7zlYOtK_TTzPNnF78zp16dyuIBvJadFSb39uMgdcS5SC01XljkBWR81gVg5Cl8Bynlf7EoCsz7YjvVZDgIUpTxxrnuL5QeWY3qCU4wydONxW778JS8psmpurfd0GiorDk2yQW8WB6M-dhp1k7aGaWzuRN6iubXv83Hco2FN5UApYbJribmMFKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
فینال لیگ قهرمانان اروپا
رو با آپشن های تخصصی در
MelBe
t پیشبینی کنید!
⚽️
🔥
😍
💵
امکان شارژ
کارت بکارت
و
هات ووچر
🎁
قرعه کشی و آفر های جذاب با جوایز ویژه
📱
کاملترین برنامه موبایل
🤝
اسپانسر رسمی لالیگا
🇮🇷
پشتیبانی از زبان فارسی
✍️
حرفه ای، مطمئن و در کلاس جهانی پیشبینی کنید!
برای ورود به سایت فیلترشکن خود را خاموش کنید!
‌
🌐
Link
🔜
MelBet1.net
🌐
‌
Link
🔜
MelBet1.net</div>
<div class="tg-footer">👁️ 8.22K · <a href="https://t.me/Futball180TV/90450" target="_blank">📅 12:34 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90449">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/584cdcb707.mp4?token=iOBy4yW-bUtoeXlmI-Bt_913Q6p5ATZij-X-0puqORXwb9Dg0FA0XjjajYHBJiiBg4UTeVGdEzzChyQkzZ8s4fIYUPupz8biJ1-M3oGHSTL7aF4_M4y1IjOfYLBQcsSrDxOnMpnlptXQKKhyDMWZogEURR3y5G4Yp6N7CuwHHcSKtvyMCkABP2eN5B1cVlSuDCpnN-VXZRc_D35B52vgDNWECiNa3r7cxdbFJD64p408TT6G43XKCxsU8YR7YwCCfPQnISwC97M_M5ZX54OguWLHN_hm6F8OQoaYpbJzQ-agmvAoXSvIFV8PK18ytVuiFkWsWh1wisO_5t5rNidrEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/584cdcb707.mp4?token=iOBy4yW-bUtoeXlmI-Bt_913Q6p5ATZij-X-0puqORXwb9Dg0FA0XjjajYHBJiiBg4UTeVGdEzzChyQkzZ8s4fIYUPupz8biJ1-M3oGHSTL7aF4_M4y1IjOfYLBQcsSrDxOnMpnlptXQKKhyDMWZogEURR3y5G4Yp6N7CuwHHcSKtvyMCkABP2eN5B1cVlSuDCpnN-VXZRc_D35B52vgDNWECiNa3r7cxdbFJD64p408TT6G43XKCxsU8YR7YwCCfPQnISwC97M_M5ZX54OguWLHN_hm6F8OQoaYpbJzQ-agmvAoXSvIFV8PK18ytVuiFkWsWh1wisO_5t5rNidrEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
👀
🇪🇸
وقتی سال ۲۰۱۱ از خولیان آلوارز درباره رویاهاش پرسیدن:
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/Futball180TV/90449" target="_blank">📅 12:15 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90448">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/628ff40327.mp4?token=p87SMkknMQ03DSWBRiBEo38360Lm0Wy6-f_dDMknQUk--dJMehwjjKCB825DAtpQtm3VPeb1PdPYGJdoEPBGPUUqvJ4wVT9qdYaM4fpyCJQzKjYrwi0N31NzxLxydjYuWkOl2L3uWASvGfItV14XELtbFTQQBduLO99m3BBKulikR0bAEAxhSY7akr4swpDc2mZgWL-nVGW8mU_AvOHGjJLL-mhzFbP5SnLakbw4NYvRGCgtxDvPMeDHkQg4valYoFnbCo9q-jdZni62tjR95iNGvfL1p7hcBDtXrLkMrNPbmZw0tFXiiWBiIuSaHzcqgpdyDSmlFDAB8SA3WDudqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/628ff40327.mp4?token=p87SMkknMQ03DSWBRiBEo38360Lm0Wy6-f_dDMknQUk--dJMehwjjKCB825DAtpQtm3VPeb1PdPYGJdoEPBGPUUqvJ4wVT9qdYaM4fpyCJQzKjYrwi0N31NzxLxydjYuWkOl2L3uWASvGfItV14XELtbFTQQBduLO99m3BBKulikR0bAEAxhSY7akr4swpDc2mZgWL-nVGW8mU_AvOHGjJLL-mhzFbP5SnLakbw4NYvRGCgtxDvPMeDHkQg4valYoFnbCo9q-jdZni62tjR95iNGvfL1p7hcBDtXrLkMrNPbmZw0tFXiiWBiIuSaHzcqgpdyDSmlFDAB8SA3WDudqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
مجسمه‌ لیونل مسی، با ارتفاع ۲۱ متر که در کلکته هند برپا شده، قرار است پایین آورده شود. این تصمیم پس از آن گرفته شد که مهندسان اعلام کردند این مجسمه در برابر وزش باد تکان می‌خورد و «به‌طور خطرناکی ناپایدار است.»
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/Futball180TV/90448" target="_blank">📅 11:50 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90447">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56a196e55e.mp4?token=n9lBBYWmQEkvK7JTiVMkAKnMN4sy9AYSPwy5BZj1PJPFJwU9S3gsNcbL6Ib-lr4AfaGqL0OdTnY2lI6963MGTzXZzTPiIEYOWRZYeYQlcnRl8Z5VFde7f5kCxr00fFKwjVnWrvCwYuRQGeUzxaeMfr7GpWkxZrcNdGVzf45ICKQg8-QC4Qs3LpDt_gFZo-FBjI88h2Sn2EOizpVSHvveGgOTnG-PW1UaWbrUSAAfxrRmyAlXwpQudTS9cBJCNGsSMh8KrkBsswHQsa74vpUM2t5k8OOyS6-StAJ-RDyqmZiis0TopFq9QOf8cE6uYzEDlXuPV6xhe16lV1fDdPW9Ow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56a196e55e.mp4?token=n9lBBYWmQEkvK7JTiVMkAKnMN4sy9AYSPwy5BZj1PJPFJwU9S3gsNcbL6Ib-lr4AfaGqL0OdTnY2lI6963MGTzXZzTPiIEYOWRZYeYQlcnRl8Z5VFde7f5kCxr00fFKwjVnWrvCwYuRQGeUzxaeMfr7GpWkxZrcNdGVzf45ICKQg8-QC4Qs3LpDt_gFZo-FBjI88h2Sn2EOizpVSHvveGgOTnG-PW1UaWbrUSAAfxrRmyAlXwpQudTS9cBJCNGsSMh8KrkBsswHQsa74vpUM2t5k8OOyS6-StAJ-RDyqmZiis0TopFq9QOf8cE6uYzEDlXuPV6xhe16lV1fDdPW9Ow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
👀
آخرش کی برنده میشه؟
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/Futball180TV/90447" target="_blank">📅 11:25 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90446">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46c8501f73.mp4?token=sVyCB0AgD__uQjncilmASWlrQZwQANE6um94kwffg6Z_mAAl17WavjZ_AXlAwPHTPstHdSYTGZOzQHbUF7sALt3baC9F-tH8kiAMi6ZF0URfV6u3JOr3b9ilBNGS59a0c2bpnQyOMQCJEPHG_bdVs7400pLYRKJ3QE_O5GGEHUCpqEL_OMWUVwMetpIGzzjB294cJf44KmyEBeFGV74qTsqW68WrVfoLrrzF7XO6LYgqhXREx2gpjvzhiQJ-Imc8WOrVEwB3cQdjpqcVqx7MmWP4FPjSIE0AdR-3m-ssAxtFAubWsbp0uHDC9-3H-dmnKYhhIbKsBHavbd3OJD0jxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46c8501f73.mp4?token=sVyCB0AgD__uQjncilmASWlrQZwQANE6um94kwffg6Z_mAAl17WavjZ_AXlAwPHTPstHdSYTGZOzQHbUF7sALt3baC9F-tH8kiAMi6ZF0URfV6u3JOr3b9ilBNGS59a0c2bpnQyOMQCJEPHG_bdVs7400pLYRKJ3QE_O5GGEHUCpqEL_OMWUVwMetpIGzzjB294cJf44KmyEBeFGV74qTsqW68WrVfoLrrzF7XO6LYgqhXREx2gpjvzhiQJ-Imc8WOrVEwB3cQdjpqcVqx7MmWP4FPjSIE0AdR-3m-ssAxtFAubWsbp0uHDC9-3H-dmnKYhhIbKsBHavbd3OJD0jxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇳🇿
مدافع نیوزلند رقیب ایران، در ۴۸ ساعت ۱.۵ میلیون فالوور گرفت!
یک اینفلوئنسر آرژانتینی پس از بررسی تمام تیم‌های جام جهانی ۲۰۲۶، "تیم پِین" مدافع نیوزیلند را بعنوان کم فالوورترین بازیکن جام معرفی کرد. اما حالا پس از چند روز، تعداد فالوورها این بازیکن نیوزیلندی از  ۴ هزار به ۱.۵ میلیون نفر رسیده است.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/Futball180TV/90446" target="_blank">📅 11:11 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90445">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aKb6Nkwv6lAFs7N2f3J26ouPEVn0SkEzqQxNdmNbOY-c4_q-2A7BjSg86YzuxobodPgT0dANwj0-8PdDAuFniSzgSj4zfnRgbwAkXKUPpFAmlPr7U6k9I48yHctkLqk07DUo8k4Uv8GbKvhnEYNt-STHKMxxDZtot5k_kawSNPlRssPjBn1Qhz9Y84Kl33mp4gf1LhTd5kau0x5Pr05pD8aU4E4UQOq0JCPwhtD3xRliAQXReg5iEmQQigYufFSBcErBx3NOqABlREPgx_hLoo_KMQUTWezDsdFkYR8__nwkAPXwEHGOr7r7We5EoubmUck4TiVpsg9a24WkDWF7-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
کونده با پلی‌استیشن‌وان در اردوی تیم‌ملی فرانسه!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/Futball180TV/90445" target="_blank">📅 11:09 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90444">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
⭕️
کنکور سراسری ۱۴۰۵ در روزهای ۲۹ و ۳۰ مرداد برگزار خواهد شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.95K · <a href="https://t.me/Futball180TV/90444" target="_blank">📅 11:02 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90443">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aPQ1ulunq108Zum4ktxhU8OFYdZPdIuLx-FoLpqBnaVJOKtK__myxXaxXpbGN5mFmN2TpIxc9cEzuoZFjFsxQbHkc_zPeM39WHs1LJBSnlJcU3-J6socU1ctHwF5LlzbQmkk6vLvF6ejK-LsCEeKatld-RSjpMylI2z-fqEUkWgqQFDXdCV0ruZvOLlyqN6Zu1YvSJttq8rEP4lkNYTKpFjTuG9B8J4_Ot66_Z12jnvssFHR_6pOrwiWQh_tHGID1LP_vI7KW3FKJ0nvpNIklESgpuWjlRv3EjNrYdJMNHzmCjT15ZiOwg8gx3pcz91EGMYEkXfADZwR_NAcYJ_8kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
🏆
باشگاه‌های
قهرمان UCL بدون شکست
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/Futball180TV/90443" target="_blank">📅 10:57 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90442">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4bcf8f7c1.mp4?token=R6LqmYslyu74hWZgFhsrgrsxsWux0_cs7Auv6M2WqYPoGLOPKhY1_ru-RjAMDweNsvyGEtuGo1udgolX_v1E7MYv99IQ_G6sKoQLJLK_YD3M0mYmeU9CPd_VEqwWC_fXj6HQR-_6pCJ4wCfBva5k5OkaK7QH7ngNVGA2YSLkftt5lXjE_vX9vmwMqSJW6Cs8iYwa6cqU48QcqHSBhDUDFN11-MoCUX4y_o70vZ_6mTIZLn-McV2enxr3_Vcl_N2TRd80Krx5II6qIn4t8wTil7LmZNcXPQ7tBQWAEexgmOWeZBDKeGQvj45m-pB_GeU0kuXGN986YD_V3_6kQ1NvDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4bcf8f7c1.mp4?token=R6LqmYslyu74hWZgFhsrgrsxsWux0_cs7Auv6M2WqYPoGLOPKhY1_ru-RjAMDweNsvyGEtuGo1udgolX_v1E7MYv99IQ_G6sKoQLJLK_YD3M0mYmeU9CPd_VEqwWC_fXj6HQR-_6pCJ4wCfBva5k5OkaK7QH7ngNVGA2YSLkftt5lXjE_vX9vmwMqSJW6Cs8iYwa6cqU48QcqHSBhDUDFN11-MoCUX4y_o70vZ_6mTIZLn-McV2enxr3_Vcl_N2TRd80Krx5II6qIn4t8wTil7LmZNcXPQ7tBQWAEexgmOWeZBDKeGQvj45m-pB_GeU0kuXGN986YD_V3_6kQ1NvDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🇮🇷
اردلان‌آشتیانی کارشناس فوتبال: سن و سال تيم ملى خيلى بالاست و ريكاورى سخته
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/Futball180TV/90442" target="_blank">📅 10:35 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90441">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cLrqzCZABlAsEgHurk38trN8c36IyOTxpDAYbcr8VsShFTg-jT_FY9BN-Mmec0dtRcqX3roS7O24GolesTd1vMMD556UK35o12SUqLmj_qxTOtDwwyCw_xma72sNud53XKp3dOtFebSzF-ObrmZLr9iPwmM5eTiAWIzTMzNkaJZtdRfyVxTKARfWzJ7A0s8AWSBNTxyAZN7YQjMXZ1WXRtQhwPCCZrGeL4_mneYA6JraVrDP1Zi1oQmUyEpkRKW4K7KFDIudkiFjxmfY1_m-wTRf8en6KshLFNq2aPVTgPfxm5VHs2D5miJHFi7u4msVmK_S42aMFKYDG2cTklxegQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🏆
پرافتخارترین سرمربیان تاریخ لیگ‌قهرمانان
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/Futball180TV/90441" target="_blank">📅 10:07 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90440">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b6df1df4a.mp4?token=n5FFSZBU7ZJFmItyDHidDQRgwYbIktnweULwErgq1Gi9bgIyhWTlQT6g-pzdfNRlpcviVBL5OzGZ39fkbS_s7C7f-JPhzXVLSOVbHV8tr3-e1V29xtmLi16OKtfSrMDT4nivosD1yzal2iX1GeFvHGmhLCJjxZvaluPNxDvxjpdrS_gF9Ruhfqg0fBbf6XSs86FjbSi5NeCCO8GJ8U_4I7dR9ch5Bc0xc2Gwip2g2mblHeXknoihV9po5KanplkFSqRhtT23tUTCqCKxCZIB6fXMQ6RBwBHVEPDRcb1tVQolur1h8TXU3i86_Goo4p9XETwDEgI0yFTDvJHRiYvpww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b6df1df4a.mp4?token=n5FFSZBU7ZJFmItyDHidDQRgwYbIktnweULwErgq1Gi9bgIyhWTlQT6g-pzdfNRlpcviVBL5OzGZ39fkbS_s7C7f-JPhzXVLSOVbHV8tr3-e1V29xtmLi16OKtfSrMDT4nivosD1yzal2iX1GeFvHGmhLCJjxZvaluPNxDvxjpdrS_gF9Ruhfqg0fBbf6XSs86FjbSi5NeCCO8GJ8U_4I7dR9ch5Bc0xc2Gwip2g2mblHeXknoihV9po5KanplkFSqRhtT23tUTCqCKxCZIB6fXMQ6RBwBHVEPDRcb1tVQolur1h8TXU3i86_Goo4p9XETwDEgI0yFTDvJHRiYvpww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😂
تمرینات فوق‌تاکتیکی آرسنال برای فینال امشب:
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/Futball180TV/90440" target="_blank">📅 09:45 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90439">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iwcip0_qm6shz58rRCa4I0da6_bTWBn7Odn4BNZBClf5GD864GuJXjw6WfQeiC9QzrPK4QaxqWkflvHcMorLyKqEM5D9ZHWX-t69XcEo0PdYdcy4ONn2u0KIwT4a4emb7Ohz9Ax4HLzSb_VLnB3N3ivR2lgiqRBfvmS1dHBQLmHcNPEbCIMsqWqKuevu6n2w4MpsS8wMd_oaMtmpDsKCrhxHsplZNyT8xqZ4PcRQhREqEgM_uU3rLllpWVKficnadn4i1BlfN32u0nPn1stXThdMx8ADo1BEGSrVaKv6tbVoTSq0U3bcTULcffsmDEa-zrJysJw1s5AK0onnUIxrAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه آمار یامال و دمبله در فصل‌گذشته
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/Futball180TV/90439" target="_blank">📅 09:20 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90438">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pbFiZygLTu2DabXRfqhg3tivcaD6rWkWYASK3gZAvROEYu9SDRzWeW3AcA7Xv1Try04I01JRTiCMRWC2iYBQwoxGSw40UwamDfEwJLcDZz3YAGMD74DFlACRFoICFQ1HDc6_ZjwJ1HYHYzQNLf5yB6Re6pwI5WwJ16pIFJ-j-KLuLEOif1mqXK6OrMJh9q0gYx3xJEI8cDLveJ1S1bm0E7LcTxoWDCjfgbIatLLoOFhanqtcAiMG23Uy3v2bxmp8ZZERGaXzESSiGA2V5TSdr0tjvrx2FmU14fj1spf2eaM8GkQ1mtCQ63gQFK7zjtdrf6o2mDHMgcLid6rOit33TQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
👀
آمار تقابل‌های دوران مربیگری فلیک‌و مورینیو
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/90438" target="_blank">📅 08:55 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90437">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l619GyQaKuwOrHcL1ABctcwMA_dUOKH1fKnnLATqYsuX0bkMy-WAOJ9THe0qT7JE3dnCzNEFzkBiKZFMwxdPzov4UnxKj5zMDDUPYnTPTrDqWyk8JCl1JblyM4jb6pYUh00WEIAzjATueU5CIfy8gi3kr0uEoW22fzA1j74MurR34TC8l8TQ7ecA4uyz6kQc4uR-MbUKES-lBu8SECXSn295gBHR57uyWyZztdjG1AmDLdwnjHaZhwtH-4heHAGEMIIP8sQ3yaF1AY9Ypbkfn8A_3WIxpmTni2Mv0lg0qAXR-AAuKMcZmwLd3_sUnYp8n4r6xmRs3XcTYo8ayk2lwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آمار و عملکرد رافینیا در دوران فوتبالش
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/90437" target="_blank">📅 08:30 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90436">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">⭕️
تا حالا بدون واریزی روی فوتبال ها شرط بستی؟!
🎉
500 هزارتومن بونوس رایگان فقط با ثبت نام بدون هیچگونه واریزی!
😮
تنها سایتی که با عضویت بدون  واریز 500,000 تومان شارژ بی قیدو شرط میده #وینرو هست
💰
👑
#معتبرترین سایت ایرانی
⬇️
🌐
Winro.io
🌐
Winro.io
📱
کانال…</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/90436" target="_blank">📅 00:09 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90435">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MXKEeU_34gaDn75fWjCoIdPGbUyJgGIuCFuVdC7JgH89Sw4CZjNxzHuEb5-yk5T1blQ4-EaVwvpmfXxGN_QWoqXvZ00mxH2x1GPxbT8Na6zqF7i47Mr5GNQ67aI2PTXnsXoqjDrJoloPNFKYI7upFhpTwuXGMTM2W2ysFUHlQaS4o36IrR0nDAVGf9usS9vaC6LFHnvmZ1c3L2IG5rJvUEGnfKtPZPwOChrB97glsVo6-A3Xo49sQow5yDzA4wRjzUiZs5Pi8jYCEFhB2GrOpEH5Hs6h8sPGPmp17r-16smnE2qirWdr2YfcmpvPIdy4ik60eh8sLVzRHqOACtyRXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
تا حالا بدون واریزی روی فوتبال ها شرط بستی؟!
🎉
500 هزارتومن بونوس رایگان فقط با ثبت نام بدون هیچگونه واریزی!
😮
تنها سایتی که با عضویت بدو
ن
واریز
500,000 تومان شارژ
بی قیدو شرط
میده
#وینرو
هست
💰
👑
#معتبرترین
سایت ایرانی
⬇️
🌐
Winro.io
🌐
Winro.io
📱
کانال اخبار و هدایا
a8
🎁
📱
@winro_io</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/Futball180TV/90435" target="_blank">📅 00:09 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90434">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bCct3YUwHgVoQyjHajI1EKlj6mW5X_leG9oHPSUgZ6ebOmRsbR6iC7VC-R4Uqb1RnRGJ6bCvSDMroIm1P4qBr84TpaY_0muiV-q4MKEqeIEjtXXrzNhDhLMr3wagnT1TokO4NkcFhkc7otR7k4H8Imn8AKEMBLEocru8xlnEx9UnGWWfqFXQabgb5jFpSRX8_57KMSCPLiN6O2Rmxv3C_Vcqnw5mMgECjYzG_wMeXRv88nFj6bVV5AHX7X3FTnKCCLKuni9HVCXPyWq0SCLk3BuPl-7gMxEZNi0GQNcdSY2pmw02bntMUvqjSTMXTq8s_VC00p16wcccgGUn7DTdFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ساپینتو با پافوس قبرس قهرمان جام حذفی شد.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/Futball180TV/90434" target="_blank">📅 00:04 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90433">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">مجوز حرفه ای سپاهان صادر شد و فردا اعلام میشود.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/Futball180TV/90433" target="_blank">📅 23:26 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90432">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v_xhHqXpFIovzN8gWPWk4SPEbkenTnljETNE-FV5nXDHsc6DgKK7CRh6EsvDZ11cgdZyRaYvX4HZJSWPj1msTzm-U8mf6Hsy8eKEDb5AJGKsHo6NAHBcZAZrUNZ-yPjzYomAPiVFNGCa4ERQ_uQaJe7cHg13DVYbWeQuoSDVg-3n6pfq7FUtcMkpmY4oM3zbDgKJ8zYTwL2K6LhCBWWpSeQlGg9yc2Udy3O8dHdvePkvRN9z6vcq2phgZjWrcONySBmDl8c5F2BWViggDH7opLs_UavTVkaQx6BGxc2RUZ-qDqSa6rEwWaQrUo4BLpxb2jCajsLISQanp5SsjDiB0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
فوری و رسمی
گوردون با قرادادی تا سال ۲۰۳۱ به بارسلونا پیوست
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/Futball180TV/90432" target="_blank">📅 22:50 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90431">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WzfutsDja_ahcN3jTHhKTng7zEf8mm-nfeotqQPK4_1cGyt6JosmlKoMqykSr7yWGkUCawy3uL1TsudkpZSN66ANDu6mDTMcGu5kvTrjtRHZ86ill3Qim6y-SjL_uvW7JGej99I33ZSuXIeTQ-BG97kdyCLHGm6s-w5wtXb6vwwRnvbJ4hlPHhP58Ty6HqQqV9nwO0Y3xSPqg6lkrUveqLb0cqvj11WTL4rr2cu1JgRDsHwAsmhzeAU98D9NILEKsSPB0TaI2cyX1b0u-8EGwgQbcDqJGXDwM9A-MZM8qA_OEubf7Mb45Wi-dU-11mc0JzVDhbE_gEKkAFRGzkqcYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست دورتمند
😂
😂
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/90431" target="_blank">📅 22:44 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90430">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rEbsChyBAClscZ2zV8Z9moyy7Pwz6ZXxvxXOkoPjWzVejhPaNPVa9a5sr2B0z7WLqyVtYUiLK-E8BSIybSDpmWjsejoWbwR81aYzU7uQ-KvHqPAqrxPOu4Jmip5ViYZqaoBB-EZ0nzEitzMk2dwpfgLFliFmNQLisknhrYAmoT8hrpHBADlthETEgg9fjfTJijqqMKGgtI2eRSrPgC5h-UZf0BzAtDE6fSJ7CelOpmUG6cdJDA_ZPQJvrzBAGwY1nWBqVjLtCUaxqaVV0icBvS2TWpSvha770AibavlS2t_g711Va3QgepU5GV72NFL8jkffEjxKfKohEVZ0DRC6DA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
اتلتیکو مادرید بیانیه ای طولانی را برای روزنامه های اسپانیایی ارسال کرد:
خلاصه این بیانیه این است که اتلتیکو مادرید به دلیل نحوه رسیدگی به پرونده جولیان آلوارز از بارسلونا بسیار عصبانی است و معتقد است که بارسلونا به جای مذاکره رسمی با باشگاه، از رسانه ها، افشاگری ها و فشار از طریق خبرنگاران و عوامل استفاده کرده است. اتلتیکو تأیید می کند که این بازیکن برای فروش نیست مگر اینکه بند آزادسازی کامل را بپردازد: 500 میلیون یورو نقد، و او تا سال 2030 قرارداد دارد و بخشی از برنامه های تیم در فصل آینده خواهد بود
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/90430" target="_blank">📅 22:17 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90429">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🎙
لوئیس انریکه:
به آرتتا می‌گویم تو هنوز جوانی، پس بذار این پیرمرد دوباره قهرمان سی‌ال بشه، چون آینده بزرگی در پیش روی توست
😂
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/Futball180TV/90429" target="_blank">📅 21:46 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90428">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lsukUYov7H_v4I2VlLaKQtixoVDBNb1sz-t4JJamyXIISWNA_UIo94qVPy9buoJxWLrCJCppNWVHl1MJyxMW9PlGV9WMV6pDNdqKVuaDz_5Lg3NRIsxbL-Q0LvydwlZUvNj7Hg1mkOjiJLcFeLFsetwRg0e9t5d3FfhPVyMZ1UDYsnKcWT3aAk_WAVyicLno_bcpuTQNzBzoRqExUviR-ElMbn7phIIFBvtIO6_esQuXNtA5fcFxL3qPym4uOd8uRt72j9cATAPPQh775Jpm-Q-Q-MC4vdPyvB4sTHRJAn7CRH8DFw25-4vFtx1G5EzuXTTb4t_QE0mNY_Ds_yGBHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
پاری سن ژرمن
🇫🇷
-
🏴󠁧󠁢󠁥󠁮󠁧󠁿
آرسنال
🏆
فینال لیگ قهرمانان اروپا‌
🇪🇺
⏰
شنبه ساعت ۱۹:۳۰
🏟
ورزشگاه پوشکاش آرنا، بوداپست
🎲
با بیش از ۶۵۰ نوع آپشن پیش‌بینی
⚡️
با بالاترین ضرایب پیش‌بینی و بیمه صد درصدی
💯
📊
نگاهی به آمار دو تیم:
✅
پاری سن ژرمن در ۹ بازی اخیر خود در لیگ قهرمانان شکست نخورده است.
✅
آرسنال در ۱۴ بازی اخیر خود در لیگ قهرمانان شکست نخورده است.
📈
میانگین گل در ۱۰ دیدار اخیر پاری سن ژرمن در لیگ قهرمانان ۲.۹ گل در هر بازی بوده است.
📈
میانگین گل در ۱۰ دیدار اخیر آرسنال در لیگ قهرمانان ۲.۴ گل در هر بازی بوده است.
🧠
وقتی بازی با فکر انجام شود، باختی وجود ندارد.
⏩
اطلاعات بیش‌تر و قوانین بونوس:
🔗
bwrd.link/CH100
🌐
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
💻
@BetForward</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/90428" target="_blank">📅 21:46 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90427">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d5ed95013.mp4?token=miDpONsHAonNTFnJt2XJUZ_lHqY_t4C1EKFsL8Eg2T-ddbQdwt7w7b0_-BeK6J2_SdHRIPBwQPm1xESbP6TvNYqCRhXDoRGJ0JpRJhXdJrwfGG2hA_M9WiR_4Pt5K3IPNuR1Ju9AMoGKNnuSWehcUjLE0JX7K9K4CX3DQ40jSmkI88IbVCTgSC6LZmWNgLxN6vri9SqJJu7HxAeEvJmagkfPd3p0cBD-HNRXeF475_BCAlCB5ki9ELct9KVkZodlKMMStSVgMjcVshXm55tk1hR_1uFTuDrVVZYalI9VZ-aLdJg0vFvji7Pz1tXgjLQ0RK_0S6-WVkSijyanNG-Cdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d5ed95013.mp4?token=miDpONsHAonNTFnJt2XJUZ_lHqY_t4C1EKFsL8Eg2T-ddbQdwt7w7b0_-BeK6J2_SdHRIPBwQPm1xESbP6TvNYqCRhXDoRGJ0JpRJhXdJrwfGG2hA_M9WiR_4Pt5K3IPNuR1Ju9AMoGKNnuSWehcUjLE0JX7K9K4CX3DQ40jSmkI88IbVCTgSC6LZmWNgLxN6vri9SqJJu7HxAeEvJmagkfPd3p0cBD-HNRXeF475_BCAlCB5ki9ELct9KVkZodlKMMStSVgMjcVshXm55tk1hR_1uFTuDrVVZYalI9VZ-aLdJg0vFvji7Pz1tXgjLQ0RK_0S6-WVkSijyanNG-Cdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
ویدیو جدید اتلتیکومادرید علیه بارسلونا
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/Futball180TV/90427" target="_blank">📅 21:38 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90426">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A3n7kxjpf3v225dkNeu-Ik8jhEDNuzpAkF28CwkT_nWbFpTfNtyuA5zQNAQvDNoG9HBWanXmcPVJCv21A1jDXEoxrzfGEq_UG6lJqo7DQXRZWZHXbOJ3t6wYlrL0ih5zxIJyFVA3Dmr531RBUR4P-8YYuPr60bp8IFULl2ikj_ygPEI6rjqze178huP-xzfaos-jYU_l77Es-GGA8AdGIle9nS9Deco8xtqdar3IG2mkBr9PrAFmxuEjYlePsL1A_OWKPvvE7tZ4y6H1KmdoCNYZpItbfXqBFmZY2CI3rlSqwRVU8JRy6nSbY8baZllQw1g8taEloWtrwGLvMxVzPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیانه جدید اتلتیکو:  برای این پیشنهاد مشکلی داشتیم، چون متوجه شدیم بلیت های کنسرت فردا تمام شده. پس پیشنهاد جدیدمان را با ۶ بلیت برای کنسرت یکشنبه بهبود بخشیدیم
😐
😐
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/Futball180TV/90426" target="_blank">📅 21:27 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90425">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">تیم ملی ایران موفق شد در یک بازی دوستان ۳_۱ گامبیا رو شکست بده
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/Futball180TV/90425" target="_blank">📅 20:57 · 08 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
