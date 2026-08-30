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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-08 17:38:01</div>
<hr>

<div class="tg-post" id="msg-105094">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qIqLSWpY2178OUkO92MrBZpk3Kz2HKALo8qf4smAHJXFJ6TumZFgheXuXAktsh0em6vQ85R_4b1_RTiOjcjEY-PfmeefV7mZzWdrRd1Bg8WcJmywKgUfek47kBaTErFpLRIe2LirotA_0W1nmkZB1BWWXewN-8nU1O9NGkrgkWkobcoMmEXpp59B47dd-J8qDSqPGARpMv6jf-a5kUY8WFC0D3P7XfKp0r_TFqTQCNaCLdSATgDLCfKCKac8YfUIFZljwe9-6J9FbdNUT9D5kYPOdfe7xsnVmsK8vGKXakyVJUeFwUCyJEI4BfBEwzMf89H4hq8YESnXUQDw0YLN_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🇪🇸
هفته‌سوم لالیگا؛ شماتیک ترکیب رئال‌مادرید مقابل مالاگا؛ ساعت ۱۸:۳۰ شبکه‌سه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.08K · <a href="https://t.me/Futball180TV/105094" target="_blank">📅 17:13 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105093">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VOe4hoHMZV-f7cdfblXAI5TDwNlDwY2CvNntbZ1-bPdYa7F4j1Lw2W5Za0-x9pt4a1rrzYcVQ-VgJNc3iFtbBR8iRqHfcac8cXlpKiOXO352gMRtCAdOrVJSSeDs83DPVrXjpX3pfJUPN6w8cg4sW6j3qZzAPFPmSMPowAFpV5BFbpGQsnkpMMIKtAkD0u1VFI9Fl58T2bLC-ESQxZ460lLvzUdWE-5S9hnYXpsTebFUa0vL1ut7byBbEhnmsqvRQpDHUyyNc3A6Nr35I_BR_cR47aofGi_lBqlsfQB7KqdXakKo08qkqmSXkpDeSZxdmFwTR4tc3HSJW380Zh3K9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🔵
#فوووووری
؛ گابریل مارتینلی از آرسنال به الهلال عربستان؛ HERE WE GO
💸
مبلغ 65 میلیون یورو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/Futball180TV/105093" target="_blank">📅 17:01 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105092">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C8czCL4qQxROqAdLlQXPAfew22vB9VhoVhYH2JpSGBmiqeblWlIH8Jv-KT9_Qfl-v9FALlVw_srMLv1mKgsJqqIElgt5IqI6eImQFQQFtcAkyYpeeM_rTlFikAo1_xzuupFh_LcgPJ0h5G5rT7wxSw-ckyDckvuoQ53IMVNFM1403tWmHrzycy158U4APpaOmJdAe_zkq9xC3uReMcuPgFuY64ZBNk1QzKbfG2AsLBtiUTXH0Vqp2l9K0pMd14ID_I3fXIu5I8UfX8H1GFCYFhnrF-b-Fpi-J56-CBUcmM_XUbs43rqJsQKPPdaIT_bsTi9B0GZott5VjjxTdNnxQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✅
🇪🇸
جرارد رومرو: گابریل‌ژسوس با نظر مستقیم هانسی‌فلیک در ساعات پایانی نقل‌وانتقالات جذب شده و نظر کاملا مثبتی روی این بازیکن در رختکن بارسلونا وجود داره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/Futball180TV/105092" target="_blank">📅 16:59 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105091">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m7uuBB6Qz89WwEVTMVO_YdEts_ZxOIJBBfBBoYlNJbYIhwGQz77iXW4J0Va_By4z-x1bh-xstW-XOvSahIX0eWDHrlCMRJxJS6k-Q4bZoVBNE-bWrHN77p8Ph613pal9Aq8CyZhrHZno8VpYmegbWmUe_oXl7sDw8ctR3DQOEA-JONqOE3FJACOldxLbMnaGo1WFPA0z6Gv0bhao4-nrOHYxzzc2b3BoJpH9nU9cbC2H0G9bNoa30IWehzT9Hfs55ivYgKdPXATwjPqUASQ7itfWbZQcn0sO-drCcd2vU6ZXGKZR30VEV6x_5y3EvY-d_ICdDkYqT-s_4uIJbC3ILw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇪🇸
بازی‌های فوق‌العاده سخت بارساییا بعد فیفا‌دی اکتبر؛ جهنم واقعی قراره تجربه کنن
📅
۱۹ مهر - ختافه
🏟
📅
۲۲ مهر - گالاتاسرای
✈️
📅
۲۵ مهر - بتیس
✈️
📅
۲۸ مهر - پاری‌سن‌ژرمن
✈️
📅
۳ آبان - ال‌کلاسیکو
🏟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/Futball180TV/105091" target="_blank">📅 16:55 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105090">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f55f5f095b.mp4?token=CDOh7SzKXN2u32ZpsT7XYI_XW9m_KoJiw_WM3_sJj5VsAWjBH9jacZ_Q7qePFpYPz9fNdGU4hpxiR5SlKbGD-A_5p_kuLK1gtsH2Mexnqw3C4Vgx85gd7Rex1VHh1hTiOC7a02hzyOnhKC9VxKk2bUdtPlJrWNCqhOT-BIhCHX5L5NoOtizS6KrDf2UC9qL4HJBaJzI95k7JuZIeJ_H_kf8sqPIBHl8QZ4Cvy9GcxywA4-wAMKs9LLcUQep5gpMDGjN69a8L8-qnfdLYk8VzzL3HPmgg6ZrzkZq3-e-9yb5fr1SyE8CleXygn4Hg25jKy-_VE95ib9L_O_eHf2xLEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f55f5f095b.mp4?token=CDOh7SzKXN2u32ZpsT7XYI_XW9m_KoJiw_WM3_sJj5VsAWjBH9jacZ_Q7qePFpYPz9fNdGU4hpxiR5SlKbGD-A_5p_kuLK1gtsH2Mexnqw3C4Vgx85gd7Rex1VHh1hTiOC7a02hzyOnhKC9VxKk2bUdtPlJrWNCqhOT-BIhCHX5L5NoOtizS6KrDf2UC9qL4HJBaJzI95k7JuZIeJ_H_kf8sqPIBHl8QZ4Cvy9GcxywA4-wAMKs9LLcUQep5gpMDGjN69a8L8-qnfdLYk8VzzL3HPmgg6ZrzkZq3-e-9yb5fr1SyE8CleXygn4Hg25jKy-_VE95ib9L_O_eHf2xLEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
یه‌سوپرگل فوق‌العاده از مسابقات هندبال بانوان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.49K · <a href="https://t.me/Futball180TV/105090" target="_blank">📅 16:33 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105089">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hCfPJIErbsAOmoFcrZFU0bX3T1LRDMjOIFdFHbbfq1lh6RxiYZ3W9uXGZX2ck0n79mXcvxP9d4-Y9FDJge-5MjpsaZHpIDjEqigKQDp4s5BJ1zinrbGvlW5wb0V07S894vqESsuyclgO0AM1aB9bkQoxOvuVS-x-GBePZJBdfk847aTna-_JPVAnh_NXc2UITHz7AL4IWCpDiR1Uxx0BUo80o56hppNjZ280ThTsV9Wj5FnH_HfEFuFi9nK471S4YeEpThnHsvQ6FwndjXpxGPc89djuOTGwRTvhCXALpn7PS-xvoPjwGDkjbjmhWtsQiYSTAtk3R8ztTHknCDEm1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
👀
🥶
مقایسه عملکرد وینیسیوس و رافینیا از آغاز فصل 2024/25 تاکنون!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.58K · <a href="https://t.me/Futball180TV/105089" target="_blank">📅 16:05 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105088">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d09cf549f8.mp4?token=Z-wp71T22Aa1UWYJjfIUl0aqrK_88lXzgUKGBbOeLYqdwmNNlgk5BqAKuFqgVmsmoa7YlUVWCW6xAl7qpsuhmnD2S4_DswRuyGWgYgU5-_2O5SRQZ_sXFDLtMQNrKXjkiuCeeaZVjBZkuJ0kKM0z5DshdCT1BgWlLXo4tuArK9drq0hsS71zfvAZgG7cOoEleyB11NYSx9Sw2gucIhXxXodSdx0Ylx35Ik6xCdm792czq7u8yup-p_lBurgUZTSj1pdg-5Oexr6AdY8XvmNT3_x2aZJ7zJ7BSByr70IWs-yS2U4TDFhlm5CSw1tlWCE0mLFnpwVT8PPogqIhthxOQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d09cf549f8.mp4?token=Z-wp71T22Aa1UWYJjfIUl0aqrK_88lXzgUKGBbOeLYqdwmNNlgk5BqAKuFqgVmsmoa7YlUVWCW6xAl7qpsuhmnD2S4_DswRuyGWgYgU5-_2O5SRQZ_sXFDLtMQNrKXjkiuCeeaZVjBZkuJ0kKM0z5DshdCT1BgWlLXo4tuArK9drq0hsS71zfvAZgG7cOoEleyB11NYSx9Sw2gucIhXxXodSdx0Ylx35Ik6xCdm792czq7u8yup-p_lBurgUZTSj1pdg-5Oexr6AdY8XvmNT3_x2aZJ7zJ7BSByr70IWs-yS2U4TDFhlm5CSw1tlWCE0mLFnpwVT8PPogqIhthxOQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
▶️
تیکه‌های فوق‌سمی مهران مدیری در سریال مرد سه‌هزار چهره به عباس‌عراقچی
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.41K · <a href="https://t.me/Futball180TV/105088" target="_blank">📅 15:40 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105087">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4dfc3046d.mp4?token=KcVjt9EaSLACYtfhyFE60LN20_qnfs8OUjNIrOQtJWaOP27FkG4wTDnBVj03DFj8r9U1JfjmLMo9IPhft-fwavhvr0grZpVMU2-KdnU4Nnk4y3Ww69CmlWAK_16WAd1SYcIbno-AqtCmp9YgwFUStngFOJ4p9diR0Kr1N2thQaH89jeu-9f3HmVCFEeVSVQLjRsa_SVCwi32C0AcFk61CjSb0ehgkWRInkvMWovjQNwHXRPMOO3Dn7JlBl8y8PE8AksvRB4kW-zmByhSqCnJjTi1jIq5zpJgpFMc4KGFk1x54vkzg6Q3sq_HmD0HvH_gI7W9kpKYm4ZVxRWd784W1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4dfc3046d.mp4?token=KcVjt9EaSLACYtfhyFE60LN20_qnfs8OUjNIrOQtJWaOP27FkG4wTDnBVj03DFj8r9U1JfjmLMo9IPhft-fwavhvr0grZpVMU2-KdnU4Nnk4y3Ww69CmlWAK_16WAd1SYcIbno-AqtCmp9YgwFUStngFOJ4p9diR0Kr1N2thQaH89jeu-9f3HmVCFEeVSVQLjRsa_SVCwi32C0AcFk61CjSb0ehgkWRInkvMWovjQNwHXRPMOO3Dn7JlBl8y8PE8AksvRB4kW-zmByhSqCnJjTi1jIq5zpJgpFMc4KGFk1x54vkzg6Q3sq_HmD0HvH_gI7W9kpKYm4ZVxRWd784W1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تنها ۲۲ گل تا رسیدن کریستیانو رونالدوی افسانه‌ای به هزارمین گل دوران حرفه‌ایش باقی مونده.
☠️
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/105087" target="_blank">📅 15:15 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105086">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cY_6cfVGG-sHCv7d2CP8v6NQc3b7nTqG4qew_tkaTbe9FuOwu1CLQGHI1ELQDgWFx_uUvhnIt4KaZ3DjvDsmf2rVM8Uzki1xxcAfuiYx-zcvjcrIRUjACkeM6WZl4LrWNqNeYLh2KEQy9Sp0cfnvb_eFFDfnQCC8FQI1Qs3L53tozs5jEh-Lv1VIIcuCK-X7lUC8Ot6E1-eHufoM7gY4zD9fnlYnFyFVcvrP5UMkjokP-gGn3NHkKkbHsAxBBrbYOpg_ks6UPVOCoE3c_hxIbWP3MnQKH5fEUfAZBArMR4zFcEAXf9zgmXr_OL6J8XLaFMTHHy6VX9KkxI4gNmyjFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
😳
🏴󠁧󠁢󠁥󠁮󠁧󠁿
بلایی که دیروز آلیسون بکر سر تابلو تعویض داور چهارم بازی لیورپول آورد بخاطر اینکه داور کسمشنگ تعویض تیمشو دیر انجام داده بود و در نهایت همین اتفاق باعث گل‌‌خوردن لیورپول شد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/105086" target="_blank">📅 14:50 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105085">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14f04c2611.mp4?token=djcRywZBoV2zTv3DKlev3Ex9ULE_fRnKIlORVG5cIbCOY2GO9741ruyIUyv9X4CBg-C3xeFew-sTdAINWly5Y_vTjNT-7gRv7hprXCXvKC68aMUbWwIN3vLzh36YgEhUxfr9dhvz8pZkd1IchNJK4TOp6Hix93J-ofjlEj6m7QgCEvdcxF60S6ffIolXKOGNLV1ZV-V1pkOz40vxkGKT5IkGeydt_g4Y7sll_kU3cec0oBslECKe-kkS7UZRf0E4oCvrj9AVxkGWBEzj8oIp3Mxo29EAFhVWUCI5QY3TGDoWvd-lLdzvoy6sxC4lFEfZew9YT3yeCQ3PK2vftq-Wxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14f04c2611.mp4?token=djcRywZBoV2zTv3DKlev3Ex9ULE_fRnKIlORVG5cIbCOY2GO9741ruyIUyv9X4CBg-C3xeFew-sTdAINWly5Y_vTjNT-7gRv7hprXCXvKC68aMUbWwIN3vLzh36YgEhUxfr9dhvz8pZkd1IchNJK4TOp6Hix93J-ofjlEj6m7QgCEvdcxF60S6ffIolXKOGNLV1ZV-V1pkOz40vxkGKT5IkGeydt_g4Y7sll_kU3cec0oBslECKe-kkS7UZRf0E4oCvrj9AVxkGWBEzj8oIp3Mxo29EAFhVWUCI5QY3TGDoWvd-lLdzvoy6sxC4lFEfZew9YT3yeCQ3PK2vftq-Wxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
داستان دعوای عجیب‌و غریب خداداد عزیزی با رسول مجیدی روی آنتن زنده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/Futball180TV/105085" target="_blank">📅 14:25 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105084">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3436f33e7.mp4?token=E-GyjMxuRmvAHlZOLUnHBIXFpSMc_-NbQuqxUzaW8DQKyO-Ae8mVVXmGfUnT0KwBU59N3Bx91s4DSPLTRA_EGo_24TwJY8xIoZw-6xCap7yX-iK2enfdQ7FmV04tNssIpajUnoekIlwSrlWH7R8kC_ZE7K0FvX-9NrSllHnEnCoX3zsya97HUxuKumB_uNbkVmAl5b2kM3HeZ4B3X0GC9wayKoJEFtfu-1m2TfTR-M4LWoeQogbMzIJ8gHMkIbyKi2tFkj449S5YIajvFTej8xywqIIKfknwOp9ANz1TSARtEX_ZNptKnSZfwxo1HJLW2kP1yXwZT8wOiufl4O2oug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3436f33e7.mp4?token=E-GyjMxuRmvAHlZOLUnHBIXFpSMc_-NbQuqxUzaW8DQKyO-Ae8mVVXmGfUnT0KwBU59N3Bx91s4DSPLTRA_EGo_24TwJY8xIoZw-6xCap7yX-iK2enfdQ7FmV04tNssIpajUnoekIlwSrlWH7R8kC_ZE7K0FvX-9NrSllHnEnCoX3zsya97HUxuKumB_uNbkVmAl5b2kM3HeZ4B3X0GC9wayKoJEFtfu-1m2TfTR-M4LWoeQogbMzIJ8gHMkIbyKi2tFkj449S5YIajvFTej8xywqIIKfknwOp9ANz1TSARtEX_ZNptKnSZfwxo1HJLW2kP1yXwZT8wOiufl4O2oug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤣
🇪🇸
🇪🇺
وضعیت روانی رئالیا بعد از قرعه‌کشی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/105084" target="_blank">📅 14:01 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105083">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dLMb8BtxMoeC2apumZO6fA-b-8jRXlkY4mMF6B-lW8EJ0DofvVAucTikrNeVuycJmreCBwWOY7xNOX-fhz97GOeePs_GbBoiUcGFzTyicq-UUeRrWuQUkAAHajc1RbhG7_mqgBw9XvgyktTij9dGKzNRTtLbhAqHJ_vuhwxPVJsRsuOMQ8HIAEsQJlF_410mQUAiqS859ozJYldgn0xS9_E_BMjTs77Q54GL3iEyDEy7jqtqZSedFkUkSZCXlP1x7aLawBiRT9VNIIWWbpmuE2OMFaGsTucPuzYqiIpDVrFN44vCDzMd1LBDlh0XGv1cN6aeUua_wSg1jmRM4_nDzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💥
✅
🇮🇷
هوادار بانوی فولاد در بازی با استقلال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/105083" target="_blank">📅 13:35 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105082">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FzPKYWfozbqWJHe0Xe-eZGy2EBJc1QTuEmrl8aCpHCUNI0QqYwSoJQCLXh4lN0x3sqTtl0IipcfNhCGRmZ2Af0WjPeNlTlPF9dPZAp6F08P5me6L3IeWXBGr84FhbsVVnqYxhmfO0adAYpnf9Sy7uZawfQo5_09w-mJGfwYaQtsuoyb-Hl1--4wiZ75WNrbulh6j0GpWbKiN5JicjTh8jNO82_m3Yy4liWCfVQBXu6ic2d7NtIm07dGelq2NRRDA2eMqzoyZbkcENh_pzT8HpcYiB9ewYDyrn3oxGmscjLUlrx_mZJkyKW3hU1wETFPHcZQICKkvDFZzvkEen5ZgNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😳
🇪🇸
مبارک اتلتیکویی‌ها؛ آلوارز به تمرینات گروهی تیمش برگشت و بارسا و این حرفا سرش گِرده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/105082" target="_blank">📅 13:20 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105079">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RYtq4njhJiXMnwtINMLlWUYeVpoRYNG9jeTqTJLAyy6tCGlB3NSopCrVZdm4SRBtRdQG19fwX1JxWp13IoFyCYUDFubNImKVnNrSXlVYGWr4p1McSageB77RpnZgxZ3W8voQHWBIJ3FWgCmzni81F51fuftNTCuaXZ7X_FYTz28vTfYbr74R2jPOBwmLty0ZdeoNcqMBvNaObL0gaJhMt6e_OwsgpNfTGSkoGW74vwDz2gLGOokUw9_mxFhTm9WXfoXMAzjjNM1Eo9hcnOUq-jBr0gnwHj3tmhr3JEDtH1lYxHN6w10Jzs0x_MNyNLuqrPxqD8oJ-gPN4Sdn2_IFlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bgp535ubgnz_CDkCKr53KRdioFRvhBIkfsDOjG_-FozNSI7kYCgMvXtxdAi2BoN3Ltdqn8W0vZL1E5mxR2RzYgPwNkt3ECdtBhFWOg1aCNPo1drQRvi6tBkbG0dlqFPKilTB7NdfoA4wIND-DXvKl_2jQHG-95l0aEAOzbAMW7RZJ-utY0waXIiA1yzIleqEOG9PZyzeu4bJ2DfbKeMXUzWuXP452SoRhARKT5mkTgFTGsfQgXiKFjUUpDy1_zLun_VGa35Z5ThCSGARe9Do1uSCiMhXcZq0m1x9LT9E0MS3j3_Os-Mcea5iF7oV4lkfUTyQlAbyeayrsCM72bNH6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OFWXfSJx26fVF2PyscmYkb85SrsSF_iyspkda7RjE3TOtbRy_-C8AITWR8qK71qy5nE2Gq4dwNBbYA97aZIejwCd2d2-XSGXQc_P1YrI1hv60WQ-E6yl8gc1InLnC8R23v9YQAll0c5JutwYCN8bhrh-puDQ5vIUbXdenlo-MC6bmdrlXh6COuUYKd-ywhyT7v6rA8HyyB3qZTy9zCkS1ZtLSxLNOK9jc9y74S3vco27Y8lxestwCNLQ5SU8vnleoVAdKDz4loOJgq_yRG_1l_C5k0K6egJoWVOdq_ygtNxnN0TfFtaD5qhz4W_rFe05WX9sAnRu7fvzOWOFkerA2g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
💥
بساط ممد مورایس برای تولد ۲۹ سالگی شیدا مقصودلو همسر ایرانی‌ش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/Futball180TV/105079" target="_blank">📅 13:10 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105078">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20e0dee25f.mp4?token=vPSQDODAmLXWY8nJvkvreVksInJPok74gdN8tWqGKuNdJ3rjINCk8kqO6Tjv67vqJILKfyii8o0u8p_J0-lbAIy6lCtPsxP4csvFsUyneM6pnE2LGksHzcxCwIQdSREqOX-gWs5TqVDlY65V9L6JyN_uzlcl3mex-7PSbdDw2J8A0hKf7OrbdC_aTzJGRmccgxAYUklu20BDoA4MkF4GM-GiVFsTs-REViQroOKUR3GWxAAdK5HlPBMMdRJ39ZMBW8OQQCGRbKQydJ5JGwffOJmhxCZ0xcCZBLajuVklqGlsiYBFIJr0olEC7A6piq1Znh5U-AOvIorX36sv60yhXjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20e0dee25f.mp4?token=vPSQDODAmLXWY8nJvkvreVksInJPok74gdN8tWqGKuNdJ3rjINCk8kqO6Tjv67vqJILKfyii8o0u8p_J0-lbAIy6lCtPsxP4csvFsUyneM6pnE2LGksHzcxCwIQdSREqOX-gWs5TqVDlY65V9L6JyN_uzlcl3mex-7PSbdDw2J8A0hKf7OrbdC_aTzJGRmccgxAYUklu20BDoA4MkF4GM-GiVFsTs-REViQroOKUR3GWxAAdK5HlPBMMdRJ39ZMBW8OQQCGRbKQydJ5JGwffOJmhxCZ0xcCZBLajuVklqGlsiYBFIJr0olEC7A6piq1Znh5U-AOvIorX36sv60yhXjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
🇮🇷
🇮🇷
امین کریمیان معاون فرهنگی و ارتباطات باشگاه سپاهان: اگر در دربی به امکانات نقش‌جهان آسیب برسد، از استقلال و پرسپولیس غرامت میگیریم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/105078" target="_blank">📅 12:45 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105077">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🚨
🇮🇷
🇮🇷
#اختصاصی_فوتبال‌180؛ کوپال‌ناظمی از سوی کمیته داوران شانس اصلی قضاوت در دربی روز چهارشنبه معرفی شده و قرار است تا روز دوشنبه تصمیم‌گیری نهایی صورت بگیرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/105077" target="_blank">📅 12:21 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105076">
<div class="tg-post-header">📌 پیام #84</div>
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
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/105076" target="_blank">📅 12:13 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105075">
<div class="tg-post-header">📌 پیام #83</div>
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
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/105075" target="_blank">📅 11:50 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105074">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DrWlOcT4xm52_eZfFsWIwz99h3eh3Kmkcatb1r1Z15qKP8qQsiR1FbOBLOkmAgoFdN-jT7bY-SH_IPv4-ZfHQyY2z-KbWr5yoLsdKrXzXf6a_-TV5KlPl4226XsWEkDRyfgxnTyMXaCATfwPr2E81LjjbtCur4S4Iyse6L3cfMC_OPPKsw27KP3jsA8TwAlBPTwXsGwRZKjquqkVUGWkAXV2wxIj2QNpzyaUavIdXN-krFEW4S-19R2Ghd4oG3U5uLo_31u-WzNUvjcX3rv1YI0vKafbg0z69k0ZfR6Sgm3Tn4_mbkN9Ic9dnY77GXMqzpNsaDqh8uYPp-gtldXYlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇮🇷
🇮🇷
سنگ‌بازی دیشب هوادارای استقلال و فولاد حین خروج از ورزشگاه
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/105074" target="_blank">📅 11:48 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105073">
<div class="tg-post-header">📌 پیام #81</div>
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
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/105073" target="_blank">📅 11:48 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105072">
<div class="tg-post-header">📌 پیام #80</div>
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
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/105072" target="_blank">📅 11:48 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105071">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mv_cVkbaF4igK3JFlTUqw26Dw_p5ruJJ6IKel8Qe37eFflFelPrnPTj1W72SOqISLSbvqc3FAWeyepItxZGnGEDgQqkT86juyMya2NN3coijnTjNj7hCkYp93hs8Cv4s0ANsEiqSQckRBeyRLu93JT3zL8dXrSe9FmCJJbGsdQOWN6RjzBpGShZrmlNspKby1AQrXF-jLIxHMkvBWNaRHNB8VngtNSIur5fP0IJdmoVAEDH8oDX4_fYLP1iX7_PuRgf4e5O5OvgfafFqA9Vjtyy4v2MXfwH9s9uQIf30bik_7jlB5nIsjaT4T4VUJty7G7qgzYLYlii2kBf4lKJtPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
✅
#رسمییییی
؛ املیانو مارتینز سنگربان تیم‌ملی آرژانتین با قراردادی دوساله به چلسی پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/105071" target="_blank">📅 11:38 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105070">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hHl0twv_CnpwQJFhNBMLvulvoZYIcatcqZHDQvGeYx3n8hnxwppbCrc4ZV85ypOwvaze6utAODVGt1QF9gUQesm43KK-E86rPJLeIMPAYv6V9ONBpU9WbuDrOhWqrmFvofdU_G3YQddmquqovyHRm4kayPtika8c-hjuu0ZLVTNVg4KtRWriZFPSyhKajMM_QdTZl5LjxqGl6Yq7BwAVCem9DlED4iyqaP8J9SWUwSAEdNJUFvd1YwGr_RezZbQSoFQZUtwMFWAhGGNAWR43qv6vP06LBvu81V9OapVA87RjyyBfqkkFs9VsJPKJHK3JOEW7JTXPwaBKjTH63EvAMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🥶
👀
🇪🇸
🇦🇿
بارسلونا در آخرین بازی لیگ‌قهرمانان خودش باید مسافت بیش از ۴ هزار کیلومتری برای سفر به آذربایجان طی کنه. چیزی حدود ۵ ساعت پرواز!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/105070" target="_blank">📅 11:35 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105069">
<div class="tg-post-header">📌 پیام #77</div>
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
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/105069" target="_blank">📅 11:07 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105068">
<div class="tg-post-header">📌 پیام #76</div>
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
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/105068" target="_blank">📅 11:05 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105067">
<div class="tg-post-header">📌 پیام #75</div>
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
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/105067" target="_blank">📅 10:40 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105066">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kr3ofq9U3lQdq01hq0g7i_qk9Sr78uwZV2xIS80YqVbzf4-_mcDJs2aFhekfWY5EYMD1WnEVzIRl2MBaddfCsh6K41npU_jpAFzKQa7Yf7tbmztmZAXxlmeqXdnswLEy6DCgKXnmzKIL0RVwTihRVtPBcEpwrqK_qvkqK_ZFTsS0uGhX81A37jhK5lroBS8zblxiWonxVWmXRUKNBy-9X1XAqvWngFPKY0AtcvbzEXte6SgG5mKXFKT4g05-M9UuuGKuDH0tve1V9yFpBRZDJ3Pfxw2jh24w3irfW5KNKXGI7s35sppe1OlCfN0-VK5HY0EQ6jTodrFJ_D01Guqp_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
💥
🇮🇷
هوادار فجرسپاسی در بازی دیشب
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/105066" target="_blank">📅 10:19 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105065">
<div class="tg-post-header">📌 پیام #73</div>
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
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/105065" target="_blank">📅 10:07 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105064">
<div class="tg-post-header">📌 پیام #72</div>
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
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/105064" target="_blank">📅 09:50 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105063">
<div class="tg-post-header">📌 پیام #71</div>
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
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/105063" target="_blank">📅 09:25 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105059">
<div class="tg-post-header">📌 پیام #70</div>
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
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/105059" target="_blank">📅 09:00 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105058">
<div class="tg-post-header">📌 پیام #69</div>
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
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/105058" target="_blank">📅 08:43 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105057">
<div class="tg-post-header">📌 پیام #68</div>
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
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/105057" target="_blank">📅 01:34 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105056">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/105056" target="_blank">📅 01:33 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105055">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uObChr4iQvlDfUzQavOEKK_KWD4EYmitwn05AdmRsUhlykNER_IzI1u1BZcMv923j2tHjTbbzlPk1yWIyUHW_7WZtFC3VIHFJrd9V8BpfdvPKJD9Wwc1RUm0rx2s_Nd-_YImLeslyc19Q_sGHmOGdq4p1ge6jhNqgQAjQ4mVB05UJUJIikJ_GwwTw3eNB1SY7_liueTu5TMzsyMRtqmAjCz7HPNFKfhSr8WXan35k2ChngdULJ7kMUa_4yjuR5VwVHSco0Ducm33imwNskTOYBkmi_KLhpJ9tSxtz3Qeek4vQd7YO2u9Wm-LUrX6Q7JjjSORNdLwAasAYWWZ8jMcEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇮🇹
🇪🇸
متئو مورتو: اینتر تا این لحظه با جدایی دی‌مارکو به مقصد بارسلونا موافقت نکرده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/105055" target="_blank">📅 01:24 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105054">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r_sKV2G7GEuF40C4a6eUvQ0PIDq4LUxJZPDBg4-9xA6TDIXyGehrNUyJ4BNEJL7IpXG8Eu1uIY9MMcciqWZO1ljuGUUUwc5LZXYQTgPpJOocdrOuo8bA7DWDkBO8MF97TxwxZSns-bOoq-cTgTSBGY0vlsknI3UGLAFWa_EEuXIfCuNypGWrIv7tFjbueJqOvhKERhZGX6Xgy9qQq_Np28fOpaHnymaLLlfAaHq11CtM6dv5zzjPICpaHxN51axW_-NNMX7Yta5pWMrMBFer7AuaoRlZuIO7XbZQQgd071jU96QnVhY_J62kN9vRt2YGqgRsAufQExp1igpN2KFkPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📱
سردار آزمون با انتشار یک استوری به صورت غیرمستقیم از دعوت شدن به تیم‌ملی برای فیفادی خبر داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/105054" target="_blank">📅 01:14 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105053">
<div class="tg-post-header">📌 پیام #64</div>
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
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/105053" target="_blank">📅 00:56 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105052">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fiRq3Bki8V4hnzAII2KO4z1sGavzKCalKNNeBTOwPlCYPU15zdL_Bm1p4yO6sb-zfibHDPY9s9VDWP_IFBoZeTS44dKMuUX8C1kzRIIAAQ16ShbT8EwQ09NY_bTmJ1u3PQa-h1HDwa11r7z0bNvkOV4yZxLtfLJSiaMS8x2jxZzJ3f8VIfj6GC_FpNFKJp7_8P4yCg3b3Ts530j7QnR2QZxG2HC9gSdRBRtxv_bk8C1OXjZU-dYILMOEWoEjnnZsk69tWqgZc7zJoUwDyH3TsFv6k_KFbmcxd96UNEYNUy8sfMOKFM5tKL9cOebhDhY-JpfdBa57NhFfo6djZIAklw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
🇮🇷
#اختصاصی_فوتبال‌180؛
❌
باشگاه استقلال با ارسال نامه‌ای به فدراسیون فوتبال اعلام کرد که تا پیش از بازی السد هیچ‌یک از سه بازیکن خود یعنی سحرخیزان، قلی‌زاده و رزاقی‌نیا را به تیم‌ملی امید نخواهد داد!
‼️
این درحالیست که بازیکنان دعوت‌شده باید تا فرداشب…</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/105052" target="_blank">📅 00:18 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105051">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MH2fCJmtRxl_a_TIn6DNc2oONSc-mqixsSNU_XPngCw9B4yofh2oAhsjRjt6Nw4nFYXwoSygotMLckV18K9p52-1j0mTIoIoG3dHwxwXu8mGNQJ0PzHvCcUX2CImEBwX7vTVrtipUWz06BiwQzQ66ZBTc_gI_g4gI6rm7E98DBKCDDbs3cSooRUCYnrgTwZzcMKlAjh-S5keTklTtb9QtzTmqQv1bFnUvlXasuiCPu6qKRgE_nxoJpLLx11yBLsspt5xVHXDx4gE-bKz5DuQ26-akWHtEG-qeaMf8euwPUQL5eJDlKgjEnNIXuEPKCkngYfqJWM1GwbcKc72hE2GYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوووووری
از نشریه تایمز: منچسترسیتی تقریبا با لیورپول برای جذب کودی گاکپو به توافق نهایی رسیده و احتمالا امشب یا فردا خبر رسمی منتشر میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/105051" target="_blank">📅 00:04 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105050">
<div class="tg-post-header">📌 پیام #61</div>
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
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/105050" target="_blank">📅 23:49 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105049">
<div class="tg-post-header">📌 پیام #60</div>
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
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/105049" target="_blank">📅 23:06 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105048">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/128d699010.mp4?token=fh4CdayyQWetd6X3WOaxLtuk2HulW-oJANuNk8CcM3gK7I6gnru7XMj0D81kLczxdALVBoc7fx0BnCFT6kDHE-U1s3QkgsXXC17NplHnBwID1V_wotj0-neOhQJVIw4EatAXHr9uj_PwD1aMWOP7tM0MZUFWNP3lIPj6Jipx6HdJf_JIm9EbOEsK7Iqiq-5olVMSANNg7R1Ekpi1LknWetPlXq2zxycZJYi-u3uWqJrGQfagdeRVzZHzJwIthY1IiroVJ5pqdtrcX4ndCgfOJImfOJhAapKKl9h5VOrzlzuW10FqiXxw4kmldITn4xuwAugpxwFRe1GY7BGn9uW0Tg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/128d699010.mp4?token=fh4CdayyQWetd6X3WOaxLtuk2HulW-oJANuNk8CcM3gK7I6gnru7XMj0D81kLczxdALVBoc7fx0BnCFT6kDHE-U1s3QkgsXXC17NplHnBwID1V_wotj0-neOhQJVIw4EatAXHr9uj_PwD1aMWOP7tM0MZUFWNP3lIPj6Jipx6HdJf_JIm9EbOEsK7Iqiq-5olVMSANNg7R1Ekpi1LknWetPlXq2zxycZJYi-u3uWqJrGQfagdeRVzZHzJwIthY1IiroVJ5pqdtrcX4ndCgfOJImfOJhAapKKl9h5VOrzlzuW10FqiXxw4kmldITn4xuwAugpxwFRe1GY7BGn9uW0Tg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🚨
❤️
کریم باقری خطاب به هواداران پرسپولیس: موضوع ارونوف را به کادرفنی واگذار کنید. پرسپولیس بزرگتر از هر بازیکنی است؛ فقط تیم را تشویق کنید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/105048" target="_blank">📅 22:44 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105047">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bdc84af493.mp4?token=j6Dci78I3a7kEIfnoyvULIX2HYVuFcripiit6aMrPmH2dThWXFHIFt-QJNoqybHUR1FK5H4vi69EgLjDXQIvwKH7dRJmVYIF_zQCSs7tOIcVM1oyS1O2sj-i8qOyZbJXp5dM6AeB1Nftn-jOzR0Ezk9zGCFEpb36mRhetwwrzq1rXnH2ear1G5gNfhNSNamJuv74B7lmdErtqy4KTZHLa0agqO7b6Dv6dUmjFM4nt9CpnOMYG-NRNGk6vFAjtwldOFYa1o9CLTqk-HsgS3jXFoQR26FB1bYgsmbD9utLpWy6U38bUM4eRNCBErTwCqiamDC1mQIK4L0mBMF_1I-ijw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bdc84af493.mp4?token=j6Dci78I3a7kEIfnoyvULIX2HYVuFcripiit6aMrPmH2dThWXFHIFt-QJNoqybHUR1FK5H4vi69EgLjDXQIvwKH7dRJmVYIF_zQCSs7tOIcVM1oyS1O2sj-i8qOyZbJXp5dM6AeB1Nftn-jOzR0Ezk9zGCFEpb36mRhetwwrzq1rXnH2ear1G5gNfhNSNamJuv74B7lmdErtqy4KTZHLa0agqO7b6Dv6dUmjFM4nt9CpnOMYG-NRNGk6vFAjtwldOFYa1o9CLTqk-HsgS3jXFoQR26FB1bYgsmbD9utLpWy6U38bUM4eRNCBErTwCqiamDC1mQIK4L0mBMF_1I-ijw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
❤️
کریم باقری: دعوای بین باشگاه‌ها و تیم امید؟ زور هرکی بیشتر باشد همان می‌شود. اگر قرار است قانون اجرا شود باید لیگ را تعطیل کنند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/105047" target="_blank">📅 22:36 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105046">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VrvlWLDSHWujZ_UAUWjI-xAcmnYvnUm0x5sIxXOltggvMvyasXDL5ky6lb4NwY7j8OaOYO7nGW3amGhti5IlTaHcl1nw7n53q2j65p0wjpO9W6wXaLo764U1PoNgXUkiveWsRx7-r0e47iwok-Erx9jQmEtMkwDc2hfdffTBph14Kq-Rq3C9O8bGH5WIU6POzBlQ8xcbacqaWEqMfwH_a2uiY139d68WsTz0x1nd58-7UgyUJc4RGwh61T4Pa90Wmq6YQ8M5P2Zwd-oJMI6bGUCXkK-6FoIM74eFpuIZOvP0CP3F4uPOy_JIwT662cpWWMHmE_eYUfqKkNZo_sf_FQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
🇮🇷
مهدی‌تارتار سرمربی پرسپولیس بدلیل شادی زیاد و افت فشار نتوانست در کنفرانس خبری بعد از بازی با ملوان شرکت کند و کریم‌باقری حضور یافت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/Futball180TV/105046" target="_blank">📅 22:22 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105045">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e97755c4d.mp4?token=YndnWHSWc1UQnHaRwhTiDNXiwTan8uovcbx-6J-OXX2Qwhd9-kU3QBGQwOeMgLpybgBT-wSTO27ufyIQdam0Vf2RO0D4ZXc5KTugApykQ6Xwf8aQsorWLRjBYOPriV3qDoTMz6trmzocxNIjsrV0EsKkwnuHk_fv_1wroP_wRc4mXfop-By9FUlAmbLv1NMQO60HkFHb8fB8TqsADHytQrR8omdZr6GGkPGVLr3-jXiUYj84F3E5gJ3IJyzu2Sw-KYtGgeNJ-2ogSYb-dM2QgVEU_jgtp6urT25Z20dgMrMkjnS8TCSDSVl7bjme-oGhCSiDL1cjGvha3K4xdq_2vKBN57erRDgreFhHVu9hCN2i2TScxeGhuBr20M_HniB4LN_0absrIgh2RZZU_WclyxYYPuf5weLOsckOgJCOlsRtPyWpZqknadv-ZMNtgoj9MMdek2XMFgTDs9DMzg21vbgUcrt6WA1cANc5lw7eFyKT1ySsMSPTY8if_uB2aYaYNNn55mBMiibFID065_7f3CMYNp6NG0pC0Vnl1-5OzNy7jB7VuVrQ233JmMW2Mqk_Fpx_JfeB9mxLFfM0djnAu0pOtLbep_49dWolhI5Wn89Fy3RIlqeyWusyaGF79-gdonvDqXS04iWqlgDsC9-2RwWtHHE9c0QrXM4u9TdUJB0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e97755c4d.mp4?token=YndnWHSWc1UQnHaRwhTiDNXiwTan8uovcbx-6J-OXX2Qwhd9-kU3QBGQwOeMgLpybgBT-wSTO27ufyIQdam0Vf2RO0D4ZXc5KTugApykQ6Xwf8aQsorWLRjBYOPriV3qDoTMz6trmzocxNIjsrV0EsKkwnuHk_fv_1wroP_wRc4mXfop-By9FUlAmbLv1NMQO60HkFHb8fB8TqsADHytQrR8omdZr6GGkPGVLr3-jXiUYj84F3E5gJ3IJyzu2Sw-KYtGgeNJ-2ogSYb-dM2QgVEU_jgtp6urT25Z20dgMrMkjnS8TCSDSVl7bjme-oGhCSiDL1cjGvha3K4xdq_2vKBN57erRDgreFhHVu9hCN2i2TScxeGhuBr20M_HniB4LN_0absrIgh2RZZU_WclyxYYPuf5weLOsckOgJCOlsRtPyWpZqknadv-ZMNtgoj9MMdek2XMFgTDs9DMzg21vbgUcrt6WA1cANc5lw7eFyKT1ySsMSPTY8if_uB2aYaYNNn55mBMiibFID065_7f3CMYNp6NG0pC0Vnl1-5OzNy7jB7VuVrQ233JmMW2Mqk_Fpx_JfeB9mxLFfM0djnAu0pOtLbep_49dWolhI5Wn89Fy3RIlqeyWusyaGF79-gdonvDqXS04iWqlgDsC9-2RwWtHHE9c0QrXM4u9TdUJB0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🎙
🇮🇷
تیکدری: دربی 3 امتیاز دارد. فقط به برد در آن بازی فکر می کنیم. تیم ما آنقدر بازیکن دارد که با بازی های کم فاصله فشار زیادی وارد نمی شود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/105045" target="_blank">📅 22:17 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105044">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3d295e52c.mp4?token=dx4G2Fr7mo8XXQKfd_t1jtnktkIbh6iEBUe-ewNZy1ny3E1-H6TiZcYRrCHrxvkDgzwY3JOn0qryY5G3p2CyXxni31ZM_5HsNDGHcZIXq-ZFAevbv6V9x16-MqlzAPIqQnKZSDykZ7UMNXO-lzSDNCPEZl6XBm7bzTbwsy7Kcp88kvZTrT_xogh11AlID79GFScy7_VlfeaILQo0Tfopzl_Mq9PM-SN6Lv9b2psn2rO9ZIfRgjakfuOj6gn0MaGHntn63qENvrML6alOKPdP6B2zFvXWnZ1eqMOAxo-haxGm2bKfPz9H7WD9drSZ34kskHT1YkAfbl_fiv-iEDWLDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3d295e52c.mp4?token=dx4G2Fr7mo8XXQKfd_t1jtnktkIbh6iEBUe-ewNZy1ny3E1-H6TiZcYRrCHrxvkDgzwY3JOn0qryY5G3p2CyXxni31ZM_5HsNDGHcZIXq-ZFAevbv6V9x16-MqlzAPIqQnKZSDykZ7UMNXO-lzSDNCPEZl6XBm7bzTbwsy7Kcp88kvZTrT_xogh11AlID79GFScy7_VlfeaILQo0Tfopzl_Mq9PM-SN6Lv9b2psn2rO9ZIfRgjakfuOj6gn0MaGHntn63qENvrML6alOKPdP6B2zFvXWnZ1eqMOAxo-haxGm2bKfPz9H7WD9drSZ34kskHT1YkAfbl_fiv-iEDWLDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
🇮🇷
کنایه فوق‌العاده شدید مازیار زارع به خبرنگار برنامه فوتبال برتر: دوست ندارم تصویر من را در برنامه تان پخش کنید. شما اینجا باشید من مصاحبه نمی کنم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/105044" target="_blank">📅 21:58 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105043">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ok3l75OclcCKDJLS9-64zHm0pOptqmBOm8jopOPM2sfGQ040ZXDKi1RYZPcZsuwHxd9-RXnvueBQ-4bFxrSKWZMQX6SXAT99K1pBay_UWaVx3DBQLCC5T16aLWO7SDvyvrWSigTCe5RAKf6yEfQa0JPzSKdSKVSUcpXstwkhOxdbhZkUT3Yzp4i1uk-RggREhVkIdaydDouowkpblAW5601Vi9JmQldF36Hzvd8KrYMpXdXdRt-uZZRgtFzbaf10_iI6az5VFNy2eG2YoAu6M2VOp1WWO8nP1H39fi5eJEIcPaR4lbn84WxYwRjn1JMz4NuvU-OO5U8j6dknoeb25w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
🇮🇷
#اختصاصی_فوتبال‌180
؛ کوپال‌ناظمی از سوی کمیته داوران شانس اصلی قضاوت در دربی روز چهارشنبه معرفی شده و قرار است تا روز دوشنبه تصمیم‌گیری نهایی صورت بگیرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/105043" target="_blank">📅 21:54 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105042">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d2706c562.mp4?token=GHYtQ2bEQDKWKJjMLGuo9ooD3qovmPj6xYqCh1n_aoONlerrcFalP1abfj_7P6NaooXSaBiscuWT_7-GJp6fg4gaVAdKtcOqoxCgzUlM4XzVjDgCewWi8ZaCrKwDrrnEBn2l6b71z53JTunUW54DTOEjXNYPuFJBOqHfVREmxw2DBZEPOQsssSIpFNm5ksPzGvKtF67D6lRM6dv2NQWSOWZDGxUMw80YZTauZeJ36M5Sw8WQwhUHNhB9plvtX9ln9Uni4B9CDFRYMSEDCOm1xmjidPyTkyNBD21aq5iIYohlqlUYp8S5Acm0sOnSR4VvaHvd9Q_JXdf5WhzfuLz1CBgUv-wQ_1WPXZjt82VYa6y8gwS7UE-Zzx9V7RvLYU4pO7V5emmo6x9VdIrrHCdnN5fVnSLIIZSWd9HmLgWZaKbL3IBC5QW6uwHWYQGi2dar4G1pZ4L1yprSA_6TAmh076KXixeDsuDzzfJW310fgWKnb13XgJG-4t1-sVnthXAuvcwJ7wUp7N0ZRvVAqPUxo_PLH823DVYZcfR4gZoYD6M-iHU185tpiUKGgecpAlzrZnUhOLda7j1FO3Nw72SIBhEopXWx5qKLmFd0NTEbsrIVpAFb7mkgMaalVf6uCUbkInOsolZw2fSdWRJRrXH3nt0xE7fD18gmDWegbA20bZY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d2706c562.mp4?token=GHYtQ2bEQDKWKJjMLGuo9ooD3qovmPj6xYqCh1n_aoONlerrcFalP1abfj_7P6NaooXSaBiscuWT_7-GJp6fg4gaVAdKtcOqoxCgzUlM4XzVjDgCewWi8ZaCrKwDrrnEBn2l6b71z53JTunUW54DTOEjXNYPuFJBOqHfVREmxw2DBZEPOQsssSIpFNm5ksPzGvKtF67D6lRM6dv2NQWSOWZDGxUMw80YZTauZeJ36M5Sw8WQwhUHNhB9plvtX9ln9Uni4B9CDFRYMSEDCOm1xmjidPyTkyNBD21aq5iIYohlqlUYp8S5Acm0sOnSR4VvaHvd9Q_JXdf5WhzfuLz1CBgUv-wQ_1WPXZjt82VYa6y8gwS7UE-Zzx9V7RvLYU4pO7V5emmo6x9VdIrrHCdnN5fVnSLIIZSWd9HmLgWZaKbL3IBC5QW6uwHWYQGi2dar4G1pZ4L1yprSA_6TAmh076KXixeDsuDzzfJW310fgWKnb13XgJG-4t1-sVnthXAuvcwJ7wUp7N0ZRvVAqPUxo_PLH823DVYZcfR4gZoYD6M-iHU185tpiUKGgecpAlzrZnUhOLda7j1FO3Nw72SIBhEopXWx5qKLmFd0NTEbsrIVpAFb7mkgMaalVf6uCUbkInOsolZw2fSdWRJRrXH3nt0xE7fD18gmDWegbA20bZY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
نبود توالت در استادیوم مس‌شهربابک که معضل هواداران این‌تیم شده
😐
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/105042" target="_blank">📅 21:51 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105041">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e73d84229.mp4?token=o8TVQp8PEI52koHw4lU24TldhsuP3-TEHl-bCbUniOwBYMmYu44euNh8CnRi_mYhqMLj2E0p2mwm6hraZMMZRZpAuDP2K3p6bksXYRv0jEWcUYub95h3FZ5gEIO_KeSwr68iV0MvqTyFTqJ6ZOS1RNDemUmVnUqAWqk25CUK1Qicy8QQYGJ2fKwc-e-mtst8EZ-94XTNJ5QkTUAhs6kCJwx119cPBWwYJhlvxcDrQZ45Fn0DpUYODfknaDIA1-2rhF9hGusAnacNJe671Q0yj8bNAf8hsS1dy1kzqI5zNCIhKSrn4uMKNxKcyZI3XPdO3ZDQPCt5sOS_JgalqrZuEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e73d84229.mp4?token=o8TVQp8PEI52koHw4lU24TldhsuP3-TEHl-bCbUniOwBYMmYu44euNh8CnRi_mYhqMLj2E0p2mwm6hraZMMZRZpAuDP2K3p6bksXYRv0jEWcUYub95h3FZ5gEIO_KeSwr68iV0MvqTyFTqJ6ZOS1RNDemUmVnUqAWqk25CUK1Qicy8QQYGJ2fKwc-e-mtst8EZ-94XTNJ5QkTUAhs6kCJwx119cPBWwYJhlvxcDrQZ45Fn0DpUYODfknaDIA1-2rhF9hGusAnacNJe671Q0yj8bNAf8hsS1dy1kzqI5zNCIhKSrn4uMKNxKcyZI3XPdO3ZDQPCt5sOS_JgalqrZuEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
‼️
🇮🇷
ابوالفضل جلالی:‌ حضورم در دربی؟ هنوز هیچ چیز مشخص نیست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/105041" target="_blank">📅 21:44 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105040">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0fd696124f.mp4?token=eLRlJIQOaYq3sKt8P3b9mqdpDajywdONR91_lH1x3I8Lis58ieMtD5gNPElPnIBG75-Gg0a6Og8fRU7eMPb_B-k4BntAnu-Dzd2-wFT_qscyNRUiqupU3QLJ54iNhnbSbBymS5pQHa-w1GeHEWfmOmHW3brRSnqF7jiNc2xzHDiI5V0Ms3loolGLh9P89zpf6RFoQN9DlxGtuzXhiMgk3OJph0tjyTHNaRuetQ3UEKSNApyZdXHKkc2EeFhcW9fKo9UVn7fKxp5t-3STyPhr_OxC4itjxicrfemLxSbVGysALQZLjP3iuJGAw4MU0yXbw_rpSfcnncq6ecEWwIGiyGmXE9bTlbQrCCFYYAHSJoyK9M0M_aRsOj2zavg0zCDj8JrbU5yb8GMGtN0XSmqSGm60BZtO4c70DGC6Iup6v4IA8r1-P3QFFWgkIXbw-xdjrCSE4BZKEjhSRLOAv3OaNxwMjckLt0vdSzxmd5RyspCvFgPGrAoyPQT9as7oiK3kywOB2SniOQw2yODKIqbj6GHUFflwwB3WKx8gtIyvXp692SgMnKeD3u0_Syl8v_u9Z8g4BL3Oa7Lp4gAxY3BDNTDAf6dZQbunYeftkiRLAhfp7dI2D65cwB74rX_4vAxYHxa4Kgk5Tq2f0zpBMwNIA0JKjGsHSx6zOIH9cDgcYA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0fd696124f.mp4?token=eLRlJIQOaYq3sKt8P3b9mqdpDajywdONR91_lH1x3I8Lis58ieMtD5gNPElPnIBG75-Gg0a6Og8fRU7eMPb_B-k4BntAnu-Dzd2-wFT_qscyNRUiqupU3QLJ54iNhnbSbBymS5pQHa-w1GeHEWfmOmHW3brRSnqF7jiNc2xzHDiI5V0Ms3loolGLh9P89zpf6RFoQN9DlxGtuzXhiMgk3OJph0tjyTHNaRuetQ3UEKSNApyZdXHKkc2EeFhcW9fKo9UVn7fKxp5t-3STyPhr_OxC4itjxicrfemLxSbVGysALQZLjP3iuJGAw4MU0yXbw_rpSfcnncq6ecEWwIGiyGmXE9bTlbQrCCFYYAHSJoyK9M0M_aRsOj2zavg0zCDj8JrbU5yb8GMGtN0XSmqSGm60BZtO4c70DGC6Iup6v4IA8r1-P3QFFWgkIXbw-xdjrCSE4BZKEjhSRLOAv3OaNxwMjckLt0vdSzxmd5RyspCvFgPGrAoyPQT9as7oiK3kywOB2SniOQw2yODKIqbj6GHUFflwwB3WKx8gtIyvXp692SgMnKeD3u0_Syl8v_u9Z8g4BL3Oa7Lp4gAxY3BDNTDAf6dZQbunYeftkiRLAhfp7dI2D65cwB74rX_4vAxYHxa4Kgk5Tq2f0zpBMwNIA0JKjGsHSx6zOIH9cDgcYA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
مصاحبه سمی با هوادار پرسپولیس قبل از بازی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/105040" target="_blank">📅 21:39 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105039">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Eq2NBbXLV8y5-DEDwMQ7d7fd92alBQNhsh8nbdzaFGwyMMvoMP7logYS1_sYPXByElQFQh_QIwyAdEcsmXXgSa7b1b77C5pQeEtyevvWNIXKQ0d7H1SfjkDqoeKMojnKC5P_ygYC1B7oyEE1KoToosUJrFW1IAQZLau31STceng-IXr-KezJ1n5kU_9rtApXlh3Xfa-98o1Fg-ntkZFRkcDMC2Fbj34Y_WmlNBNj38KQlgbdw5iUU9le82PHPtn0xcTULaHbyK0FgHIdV88jrXiWruQ3DrzM9kju4krJANmMIkPaTrKJycxIw8xhnctaa0SX0TFys_1fECes2obimw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/105039" target="_blank">📅 21:24 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105038">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W_MotFMhK4iRz2FDrTipGPlPDgtP7MNWS1qbN_epfJXPu6oD8NjxjL7sqJv8RDGNP2eql7jaM1lKru5hUC3cOp-JmzwBbWAtWzZj8t03mcvTfaFE-SxhBPol5J2fwg0LzLHuFKehbTZec6CqnbU7IPmJ0yAvqFfrZ9is9W7nTHR8s0BdpqY0_6IQaaDdpVQ1Ghrkguph9hW0ZlJsdi_EtXFPBVGtw8FePL4JprnznrzxxW1H6SJHT8qCxyCFE8jmj7Ooh2uBL0gqOyWhwEEE-fG3qIlZ7YZ3g-KBCAYUKawY7zr6WC5ni4sEmpNzHmT0Jxmxqbvw9XdDMEKamTcypA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/105038" target="_blank">📅 21:18 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105037">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">❌
پایان‌بازی؛ فجرسپاسی صفر - ذوب‌آهن صفر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/105037" target="_blank">📅 21:13 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105036">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HsYmx4Nex-iqi63UetO9O8mztnmRsxeZPOl7kgzycWQW9IkUeK09LpdzKxb4U-m7MwniWpuP7HdHi0Z2at3Ugeorm1RKh7t010o-bJjrtnF7HRbzJ1w5xPmB4WLoCzplANZNkCTSGJr9t4NxXWiq0PcmbYJtfZYGFopJsW4-2LW8RGP6OhnOz3EuU7j9J6OZu8BpNZNcAebznfpRcAgTU5LlTZ41zs0hSJzyccg8eAiIwiQi_Y3HmTh3HHtvjhu1nVqR5kfQOJWNUscgPzoaAUFnVrK87wQvWOizlo-BJktWoBKjlUJZWjElOYAHr0pg0ysub9lyrmYDs6f3A41BsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
پایان
‌بازی؛ فجرسپاسی صفر - ذوب‌آهن صفر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/105036" target="_blank">📅 21:03 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105035">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
🚨
🟥
بازیکن ملوان از زمین اخراج شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/105035" target="_blank">📅 20:48 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105034">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4bd7def575.mp4?token=gsdFekoLAhlEBBAMlh0ewjzKHRIvEqLafH7YAwFBC3Dz7HE6PAX7bmgKPhKtUJ3QbecIvYw5MmBJxNT0CZkkKV6JYlG14Jbe-oWKfkOSF3PnNxl3pfVC8h1MMqp6N2dP911zXgmQH1UO27W0Vpfqtb_buBVcdKh8eD8Zc5bFkoq6XOLnszhFkMGVSaTZ13e3BUm-r0669QXwaraXqyQiDIG11V_JOzPtCqqhfdnydak9TMa7NgQ5dgJ-fY6OSYUgxnSeFi_nUISG4TVblJOiHNZvCTf8jZhvMZEf-hY59_EZmZLQKDxu7XJdYII9Goor3jkx2MCy101z82MZoSnv5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4bd7def575.mp4?token=gsdFekoLAhlEBBAMlh0ewjzKHRIvEqLafH7YAwFBC3Dz7HE6PAX7bmgKPhKtUJ3QbecIvYw5MmBJxNT0CZkkKV6JYlG14Jbe-oWKfkOSF3PnNxl3pfVC8h1MMqp6N2dP911zXgmQH1UO27W0Vpfqtb_buBVcdKh8eD8Zc5bFkoq6XOLnszhFkMGVSaTZ13e3BUm-r0669QXwaraXqyQiDIG11V_JOzPtCqqhfdnydak9TMa7NgQ5dgJ-fY6OSYUgxnSeFi_nUISG4TVblJOiHNZvCTf8jZhvMZEf-hY59_EZmZLQKDxu7XJdYII9Goor3jkx2MCy101z82MZoSnv5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😢
مازیار زارع کارد بهش بزنی خونش در نمیاد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/105034" target="_blank">📅 20:44 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105033">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a373e346f5.mp4?token=bpfEIKHsJu2-gKtrHaVYhGGkc0feRcehf7_HKDaPWHjlK8VUMW409B5yjadKAlV7rO3zK0_1hoWgaq6HmY-WvbtqRPq5AQPgXbXDer4wHoDSxqfSh_zfuy8agHxxKiZgvTUr_9gK5BvaATUf3Ly9ySbTdO2zOTcuHOnp8YdBQo9UVZe6LKLNipKFUxCMOkfhuJDg46BPMWMtaY6-MtzwszXTd7PIqNbvEMv_HxFW-zW2OMOiG1y9f2Qm1NNpbbEQHAIY6nL9TEcapGe-82DYP-ugaeA-kncA0-oRofczkkZNIl8bA3tHBELwdt4ozMXzAObjZgaZkb4jykHaIJFeq1V2URw9EbKhjdBtFP1dZZyF1pn7x_7OPwLsAQQ6uyYouMos2jfNgBqteuJX0a13a-euESv_dWEipxD--5nIH2yni6m8HRE4AV6GizWFab62Q58KIA9EDZnZbUVcJIpvd739HlIYGo8ndcyL65NRQBCb3k-c1i85LOAamRbVHu7hRERWWhRMO8kf-Scx0etlfJ32qfcXChnvwNbSapkC6OPmYpFWLOkbhJcSKeWrkNX_QFuF4PHehiWdMTYzzpR9t8TDa8rsZYPZokK4QPDnv3RhiHvN5ENXuJv5veFdsM2Ry_WJ8G0WcU0WL3wEBWGQtcItaUWyzo6vZgowD24MriQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a373e346f5.mp4?token=bpfEIKHsJu2-gKtrHaVYhGGkc0feRcehf7_HKDaPWHjlK8VUMW409B5yjadKAlV7rO3zK0_1hoWgaq6HmY-WvbtqRPq5AQPgXbXDer4wHoDSxqfSh_zfuy8agHxxKiZgvTUr_9gK5BvaATUf3Ly9ySbTdO2zOTcuHOnp8YdBQo9UVZe6LKLNipKFUxCMOkfhuJDg46BPMWMtaY6-MtzwszXTd7PIqNbvEMv_HxFW-zW2OMOiG1y9f2Qm1NNpbbEQHAIY6nL9TEcapGe-82DYP-ugaeA-kncA0-oRofczkkZNIl8bA3tHBELwdt4ozMXzAObjZgaZkb4jykHaIJFeq1V2URw9EbKhjdBtFP1dZZyF1pn7x_7OPwLsAQQ6uyYouMos2jfNgBqteuJX0a13a-euESv_dWEipxD--5nIH2yni6m8HRE4AV6GizWFab62Q58KIA9EDZnZbUVcJIpvd739HlIYGo8ndcyL65NRQBCb3k-c1i85LOAamRbVHu7hRERWWhRMO8kf-Scx0etlfJ32qfcXChnvwNbSapkC6OPmYpFWLOkbhJcSKeWrkNX_QFuF4PHehiWdMTYzzpR9t8TDa8rsZYPZokK4QPDnv3RhiHvN5ENXuJv5veFdsM2Ry_WJ8G0WcU0WL3wEBWGQtcItaUWyzo6vZgowD24MriQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
گل سوم پرسپولیس به ملوان توسط علیپور(56)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/105033" target="_blank">📅 20:35 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105032">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c8553440b1.mp4?token=KLMqgKlwtFDQGygXzHmeqVr1QO4sl0ClsM1IfLWQfhCLol5k00DkCIk4FgXkCh9u1bMzzhRXYSbQlsfXWLG4D9Yqo-sSFo6trC7IrXQe9wVtRgCdPJ8va7Qvb9NIecYw2jsAfxJOQ-Se1bYjyKOgM06GuJg2ItYw5eHrHMwOVZe8ubryCRTz4RoeKGYbdoyAVuGeoPh7jZu7zet8vMrD9KOZr_H6l6HMGIPhZtJ-bLbEnwVuQq47s25FT7qY7_yGl1n5k4RwkWT_RCyuNHCsW8Qhm3pnxeL7Q9Al9STtAM_9HQeKv4oOixMOdqa-9jtfKHa4nDRvgb_LtijMWuUrqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c8553440b1.mp4?token=KLMqgKlwtFDQGygXzHmeqVr1QO4sl0ClsM1IfLWQfhCLol5k00DkCIk4FgXkCh9u1bMzzhRXYSbQlsfXWLG4D9Yqo-sSFo6trC7IrXQe9wVtRgCdPJ8va7Qvb9NIecYw2jsAfxJOQ-Se1bYjyKOgM06GuJg2ItYw5eHrHMwOVZe8ubryCRTz4RoeKGYbdoyAVuGeoPh7jZu7zet8vMrD9KOZr_H6l6HMGIPhZtJ-bLbEnwVuQq47s25FT7qY7_yGl1n5k4RwkWT_RCyuNHCsW8Qhm3pnxeL7Q9Al9STtAM_9HQeKv4oOixMOdqa-9jtfKHa4nDRvgb_LtijMWuUrqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
سوپرایزی که دانیال اسماعیلی‌فر ستاره تراکتور برای تولد همسرش تدارک دیده:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/105032" target="_blank">📅 20:31 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105031">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q9PBtgd5awRdAEJcljeYLcgtb5gWnnSQJ4NTJXg3HG3yPk9_-TPOX1p93RATg0D8ZNv7oeI1LhIGeWsQ25ua_zFg0w4RI0X17aV8FL5IDGshUd7ETPvS0cbc16RD9GU-O5Qz-aTKd_ErXBEK5y9BeTyo-lcXeW4RAf1CiNAxCiAfs_E8ZkWbRMBX7H-DInmg6j2vbO3p1mmlbAR6WqKkdWtK7pwmb_w9xQbQoXc_PaiH3jzEo7FoydhRNsYvPD0Qp50vR_TpsSg9GMagqxcjhhZknBKCs_nLlkP-DoM0tVVOzWoP9pXmJoXABSrggXcZ9MyVeBY_O6YEgkrXeCAQ3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇪🇸
🇪🇸
تونی فرشا کاندید سابق ریاست بارسا:
جولیان آلوارز می‌تواند آزاد شود، به شرطی که به‌عنوان غرامت، مبلغی معادل سرمایه‌گذاری باشگاهش روی او و دستمزد باقی‌مانده‌اش را به لالیگا پرداخت کند؛ یعنی چیزی حدود ۱۲۰ میلیون یورو.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/105031" target="_blank">📅 20:04 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105030">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ce507e717.mp4?token=fFdiFFG4uzsBZpxi-DeG3SRxqOeXqf8k6F4bHjsk7oEwmIVQ-UyAWjbOf1ZUIR6WMl_7h8Eh-Tgnavv4tgwIqtoDhH6GdhBv-Y5IDvOUODNfhsw5YZZS3-FIpVYASIBaca4F6fy1aiYbwMbjVV-xbYk2e4eXZKhHvthNSMwPMlzCIX7_K8EQp934mrwcbpvL0cp6L_C7FOK7hDUYdOQskBCVyL1Q5VGWFQJDNcqpgCjCDE6Zyv2FOHXVkH-NUhSzVv0t0xAoVdSs7AZoyvPdpmVLYF2hxui1wjjfjk9UxbO2SHkt7NSkzJU1-xBQGIEdhHMiCW0-DZYeskzXjA5YtA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ce507e717.mp4?token=fFdiFFG4uzsBZpxi-DeG3SRxqOeXqf8k6F4bHjsk7oEwmIVQ-UyAWjbOf1ZUIR6WMl_7h8Eh-Tgnavv4tgwIqtoDhH6GdhBv-Y5IDvOUODNfhsw5YZZS3-FIpVYASIBaca4F6fy1aiYbwMbjVV-xbYk2e4eXZKhHvthNSMwPMlzCIX7_K8EQp934mrwcbpvL0cp6L_C7FOK7hDUYdOQskBCVyL1Q5VGWFQJDNcqpgCjCDE6Zyv2FOHXVkH-NUhSzVv0t0xAoVdSs7AZoyvPdpmVLYF2hxui1wjjfjk9UxbO2SHkt7NSkzJU1-xBQGIEdhHMiCW0-DZYeskzXjA5YtA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
ریدمان باورنکردنی علیپور در موقعیت سه به تک
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/105030" target="_blank">📅 20:03 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105029">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚨
🇮🇷
گل دوم پرسپولیس به ملوان توسط بیفوما
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/105029" target="_blank">📅 19:50 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105028">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c9bdeaa27.mp4?token=e6VqxtBckvuIlXJKgZH_qcYfQnyvnAjMlKxdlv9M9qVtrPNPgWKIHfn14auD_3SA9pvNOnosSFgw8-HYm3AxgPaukMDGNXuFAAlI-WkWF8x83Vw6qO1dwSwKVrTxCFsSW3sSA8u4QG-fMgwP2qLdyHmh0wdhTeP5P_EfjpnPsTkHlHCr9INKYlVvOvaOjBOoMfVteo3SQacuQd8JK_rKjUyGTM8iSEU5TqkVvjNRie8lIC4TsCNOHYOkDpKw_SpbS5soBrR1iD76AbIQKKan3UX3YoHEdNxIPxwyvJTYrMCCC_KPIysdgXpT_FfOInPAofjpRbWXC7XLq9AGUPXTRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c9bdeaa27.mp4?token=e6VqxtBckvuIlXJKgZH_qcYfQnyvnAjMlKxdlv9M9qVtrPNPgWKIHfn14auD_3SA9pvNOnosSFgw8-HYm3AxgPaukMDGNXuFAAlI-WkWF8x83Vw6qO1dwSwKVrTxCFsSW3sSA8u4QG-fMgwP2qLdyHmh0wdhTeP5P_EfjpnPsTkHlHCr9INKYlVvOvaOjBOoMfVteo3SQacuQd8JK_rKjUyGTM8iSEU5TqkVvjNRie8lIC4TsCNOHYOkDpKw_SpbS5soBrR1iD76AbIQKKan3UX3YoHEdNxIPxwyvJTYrMCCC_KPIysdgXpT_FfOInPAofjpRbWXC7XLq9AGUPXTRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
عصبانیت مازیار زارع از گل‌بخودی عجیب تیمش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/105028" target="_blank">📅 19:41 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105027">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93421b5bc7.mp4?token=Vd3mgeLi64QnoukiFCavoH-k29eDgSbGTvFl6dsR18JAAfMBa3ln7h74SDTtPhuSF88MBafNnTaEkn8K3i67JU7TnOp2ZUCebZJMDwcrEWuN40PUDlUE_XF31f7YYlDtII3DecbjytILDCQZYonT3qXPinb1MwHjMQEgj5N-Tl3AQwnn6jkuF6Hy-fes8Q4ttEM9mKi_cvLe36g-HhPM_HQ5Y0Qn96bBB2zOzEXEO6t8568AHJg3ZTMpsawUVMLcF3cpmdcTt-zOVs9ZY9A0aPEAffRkkoxd2qJ_wXQ8omNLZOnSbTpp2MReH-23XB1qPq8w4Q-BYL-BYGqmYNsY8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93421b5bc7.mp4?token=Vd3mgeLi64QnoukiFCavoH-k29eDgSbGTvFl6dsR18JAAfMBa3ln7h74SDTtPhuSF88MBafNnTaEkn8K3i67JU7TnOp2ZUCebZJMDwcrEWuN40PUDlUE_XF31f7YYlDtII3DecbjytILDCQZYonT3qXPinb1MwHjMQEgj5N-Tl3AQwnn6jkuF6Hy-fes8Q4ttEM9mKi_cvLe36g-HhPM_HQ5Y0Qn96bBB2zOzEXEO6t8568AHJg3ZTMpsawUVMLcF3cpmdcTt-zOVs9ZY9A0aPEAffRkkoxd2qJ_wXQ8omNLZOnSbTpp2MReH-23XB1qPq8w4Q-BYL-BYGqmYNsY8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
گل‌بخودی سمی ملوان مقابل پرسپولیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/105027" target="_blank">📅 19:36 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105025">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46f5729443.mp4?token=kwh_6hd_6bW5Fj_X4O3LYTWmpuCuszYSjQCi1GTy0UrpzdiCtVxxFgfxWCf98Op90pOX_blnBJ_dv5etBW0Yj4XpvDDsLiYzBNWa_fiZg7k5o5rT4hMNRh36-_RVu85Cpbxmc1GIxiOYHfKiXlz62ca4O2BmUjPiHHlRY3Xj_K4Vist3MtlvCzz6kk4FPCwKdvRpSuAl7bQk95VGRguSKBA9ioOgU1oWmjmsscNTX9RhlGoMNaa1FNwfPdr4GecdCJBV4xe5XvLHg5f_kMs_AkSnt85IGo5Rp9C238BbWyPkoORcFnIw-IJxHgiMWcDB-rKnObubijI-kptGysHfAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46f5729443.mp4?token=kwh_6hd_6bW5Fj_X4O3LYTWmpuCuszYSjQCi1GTy0UrpzdiCtVxxFgfxWCf98Op90pOX_blnBJ_dv5etBW0Yj4XpvDDsLiYzBNWa_fiZg7k5o5rT4hMNRh36-_RVu85Cpbxmc1GIxiOYHfKiXlz62ca4O2BmUjPiHHlRY3Xj_K4Vist3MtlvCzz6kk4FPCwKdvRpSuAl7bQk95VGRguSKBA9ioOgU1oWmjmsscNTX9RhlGoMNaa1FNwfPdr4GecdCJBV4xe5XvLHg5f_kMs_AkSnt85IGo5Rp9C238BbWyPkoORcFnIw-IJxHgiMWcDB-rKnObubijI-kptGysHfAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❤️
🤍
تشویق تارتار و مازیار زارع از سوی هواداران پرسپولیس پیش از شروع بازی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/105025" target="_blank">📅 19:22 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105024">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pPWVj8JmLoT3OvaNspailFV98BWq4kD3bwIiT7Typhq9p45Mv0hsL98gck8huLWbLFTO-TR_2fc6RoxtAQfwH2x37iE9fDED2YRYTiq1m7-V_6q33xhFeXwgRRetsZX_5jZ1IlHyM1VFUa4dmODH3stWtHD1uMC5WtjL5ECnPX0PYRMyoEm9gnUR3nidEc2s5nwp_LFSc-uXE6BaqJvf-dLjgnZvIosjMe_bH0B2tdODYZnlz9VY2vdkuM5xd4iFcbdM7w-UHDwjYlNyVWAKwjH9e7eS_meqidhHmIpMipi8SPbCGiaXxNgbI6qeGvptVvSnB7qM446M7vYnzF-7ZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🗞
رومانو: فرانک‌کسیه از الاهلی عربستان به آتلانتا ایتالیا؛ HERE WE GO
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/105024" target="_blank">📅 19:09 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105022">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aPW6Lz8Q6LCm8baK08yySjcX2oA7BOpitN5quUI2qjZATSNYCiyirPRAdURP03HQcpvi09ElvH0SzFCLhSZpVxrkNjpT8eeCkFBW_sBOlsW_pzkO6HKUZd33eIQrsroyNf6XB2E8USP2Rdy1fCvm0f-6veZ2MeS9eMO68IJubHQDDyWTiA-s_XcaoOnJyAvdohhqCSSl9Onw0CpjvLGMtUjRkj60l1r4g_CTl6a9I4ed25TF_d1apt6Izr9kTSZbazY7EqGqxvpk0l9HA6_5H_3hk9mk0g6FUSN7UJnYZ5i-qxrpj4SEIi6BaNnTjkReRbJfN7gKjgezSiE7PfmNOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BPvbYagI2kuP8KV_rXrMC7o06deF4s8bdARWHm7w5c73eBwDBxwmmI7QUB6r8TM_Qa8TnLizUB7D9_51Ff-gJROdlwZPnGdrvMhwozJVfoQkrilRmv1kGb7vWy-XFb6yN6gFCZ9NApUTY4ozqxToJk1i0gzYIiQG4O-5tk6RDZXdkvIFa62W60R8fyZ71k1QooXUhHZDUsR79UIcIEv_ud67wFGaRWrjS-0n8w-Fu4-s_HJUflnf_oJVN-oOYpi8Zfpo97CBNZ20qz9U5Wi756z_hif1SbcjZPYymXfvmE6cqBjsGW2Kr1lTjtIWV0PKZbkVlgCWGGHa4FXfZcRJkg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🏟️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
ترکیب تاتنهام و نیوکاسل
ساعت 20
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/105022" target="_blank">📅 19:05 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105021">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c974ddb250.mp4?token=qupGD4Kdf9KO9Y9a_uzIfN3bUFyOxttShn10y3LvN6hnTd73nSmPK60PJMiVEXO4mGwCyJML9tZdHvv5XtpmzR7eRTom08Q9ftkhJxoD5O8ZrUfjSvKlRRighgeF9NgIggALH7HrOtSnLq22DQiuvxQGSe3XXUqj1_stPpI7la-td6-X98t6H0S_r63up024UmF2VgQH3AkY_FKHMpAEkVhUoTpQ-voCtUriTBDh2bj9vTl4A7SwRLzHzpZw4uraGl4Qs_cAaQUat9b8FmkJ_Iqamq8qRTO0kYMUT261EHHMUd-HneuSFU4CIQk2uBRsgwg_gbyo3vDlpBipnrpJozzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c974ddb250.mp4?token=qupGD4Kdf9KO9Y9a_uzIfN3bUFyOxttShn10y3LvN6hnTd73nSmPK60PJMiVEXO4mGwCyJML9tZdHvv5XtpmzR7eRTom08Q9ftkhJxoD5O8ZrUfjSvKlRRighgeF9NgIggALH7HrOtSnLq22DQiuvxQGSe3XXUqj1_stPpI7la-td6-X98t6H0S_r63up024UmF2VgQH3AkY_FKHMpAEkVhUoTpQ-voCtUriTBDh2bj9vTl4A7SwRLzHzpZw4uraGl4Qs_cAaQUat9b8FmkJ_Iqamq8qRTO0kYMUT261EHHMUd-HneuSFU4CIQk2uBRsgwg_gbyo3vDlpBipnrpJozzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هیجان فوتبال رو با لیگ ایرانسل چند برابر کن و با پیش‌بینی نتایج، امتیازت رو ببر بالا!
✨
🎁
هرچی پیش‌بینیت دقیق‌تر باشه، شانست برای بردن جوایز جذاب مثل موتور، اسکوتر، پلی‌استیشن ۵ و... بیشتر میشه.
همین الان به سوپراپلیکیشن ایرانسل‌من سر بزن و اولین پیش‌بینیت رو ثبت کن:
ثبت پیش‌بینی</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/105021" target="_blank">📅 19:05 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105020">
<div class="tg-post-header">📌 پیام #33</div>
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
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/105020" target="_blank">📅 19:05 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105019">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W-XnkdIGKod71p2HzLZCgXyKJthjqERD8CF3V2YNM8k-OUSq7kQsvcWPCTAzntflm6Sb75SNRICatUR0-D5RvzTpiGgyGzNO8Be3wco_LZJaYbsuox6j6OVqM_BYugwPkHqv2PQi2Jf4BmkVusrsnnSdKMMp0AWMcPukAjXg-8mEBE12ICT-IdWNKpFaGNbsifc_Qy4Lax7LhOxWlZ6PCTjrIpeaXaKUq2IZiAO0YWg8kr7P6nMLx5c_A8CStdtiZwQXRSKybLdnlwksnnAqqBq_csFCE6HKBusPI9KjFlIypPOsKWZ2eHW07tTVy51dPn5yMCoeQt6pXdPfTfC6zw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/105019" target="_blank">📅 19:05 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105018">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cmhXlkn7Q99c3g_YGqMWDMbZRbgFrcshSlcUmWEqx3f-exUlUCNUHpGpJBJHXxmNy9gqGMsjzUNyp-dpRhAIpMNk4FYUKfzfxDrCkDUZU9n2UcUc36AHPdG2gXQcR7jz6fUqRbu-c-D-At9U-_HrQpJeezPIybI8wyrq-DOeBzGP4TuQ9Mzqafg6xwAU0hspPMql5P3BKp4iaaUruOfuwIj4sTVqE-qiKFcT-YdROFbHnQzEXU-Rh9bA7ummK3AXsgwFSNsMI2jVOfY7TZtalEi8I5Lewhb3eF1URRPEV_oqdH6K5LuzyNdzJSDPHWl3CmXxXXFcB5fH0rDQy9DURw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇮🇷
ترکیب پرسپولیس مقابل ملوان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/105018" target="_blank">📅 18:19 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105017">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DOXVpNS70dETe0cjLlBwgiIjhVAnwjpR7obSLTQTJxbEDB304iSzhrKblN4gmliRtFiOpJBiC7P6hmCyMP1TNArOr2yqJ1H_uOTezz-PJr5HIv_D0omtIpQh9uPzV--oDoTzpO60RvCWEAR_4pF7X6yfkGwpxqh6aEKgW07fUztaLZWuwluyvO422yBnVqm6tW604N57GWo29e6127Aw8hNcjHXpAxqR0bJ_fCPq389c0k1mgN-C6atZmba9EzD2WBiHO8mg7lm60a8dAhIK3eDzLxiR9behW4xbm4VEmWZue-yUtYQ1ffKcTmDYqDbphcyYv3dUo1DA3BSd3vwm2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇮🇷
ترکیب پرسپولیس مقابل ملوان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/105017" target="_blank">📅 18:17 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105016">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
🚨
🚨
‼️
🇮🇷
هوادار پرسپولیس: یک مربی مثل گل محمدی می خواهیم، نه تارتار ترسو!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/105016" target="_blank">📅 18:06 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105015">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6f2734cd0.mp4?token=KMvh1B547-zqnHC8IH0NsL8zhUZiBDbSnOq7BhqJIJ0yUhhg5A9lfMiBeTxuAv7ZIEbEZ4x3ze4Gu1rorD4W9C1B9UEjQxdy-q9mVaV-4XdtKzxB6lvHXGgXZ50lZjAhgB6ThL059NFfl4IEEDR5mmTnnltplBx6zxI3mQXZVdHziDrzSmMonUpOkk0jCmmKMwjjgc544F4lBSPpq260qrhQ0qkmg0WFWPOUdFqZ4oAvkZfLbAzp0i2Gpyj02FFqpYNJ1AL5wrCPfRtKkfsXif0VUP8jeCtJzWw3njbfQOzKZrhYmothSC2q78f_I4Atc9yr2QFD29KF6rn-PKSIcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6f2734cd0.mp4?token=KMvh1B547-zqnHC8IH0NsL8zhUZiBDbSnOq7BhqJIJ0yUhhg5A9lfMiBeTxuAv7ZIEbEZ4x3ze4Gu1rorD4W9C1B9UEjQxdy-q9mVaV-4XdtKzxB6lvHXGgXZ50lZjAhgB6ThL059NFfl4IEEDR5mmTnnltplBx6zxI3mQXZVdHziDrzSmMonUpOkk0jCmmKMwjjgc544F4lBSPpq260qrhQ0qkmg0WFWPOUdFqZ4oAvkZfLbAzp0i2Gpyj02FFqpYNJ1AL5wrCPfRtKkfsXif0VUP8jeCtJzWw3njbfQOzKZrhYmothSC2q78f_I4Atc9yr2QFD29KF6rn-PKSIcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
‼️
🇮🇷
تهدید مهدی‌تارتار توسط گروهی از هواداران پرسپولیس: دربی آخرین فرصت شماست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/105015" target="_blank">📅 17:53 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105014">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f68436a0cf.mp4?token=K9VHsAvfara2lWorTMEna9wVK37dvRjBAYcYItil45I3Ngh1YM3Eo9FQWiF-MAmAM36xJ7B0BpV4TnFz4lwypoOo98um3VE760w243VVMcbd_0WCzwH_-RWcsO5vRRet5h9_DImDW0GdXR4jcDaCnidxGKbZU7VsKHxmldJy3bfApqGeRdQHeGh5CVMA1kSqFKx0zHwSiXrlP3WVVXYGx4f58-8baOTy_kVDj1JvkdjxLY0Tj7-JMSoI1rpRoNzJdPxeqjoN9fwvnCd0EG26wJUgLPFCHOXG1T3ZS5gkJOTluAG04Jbl-Rt1cRahjruqTQP0y0_s5H0Jvc5U0jyLgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f68436a0cf.mp4?token=K9VHsAvfara2lWorTMEna9wVK37dvRjBAYcYItil45I3Ngh1YM3Eo9FQWiF-MAmAM36xJ7B0BpV4TnFz4lwypoOo98um3VE760w243VVMcbd_0WCzwH_-RWcsO5vRRet5h9_DImDW0GdXR4jcDaCnidxGKbZU7VsKHxmldJy3bfApqGeRdQHeGh5CVMA1kSqFKx0zHwSiXrlP3WVVXYGx4f58-8baOTy_kVDj1JvkdjxLY0Tj7-JMSoI1rpRoNzJdPxeqjoN9fwvnCd0EG26wJUgLPFCHOXG1T3ZS5gkJOTluAG04Jbl-Rt1cRahjruqTQP0y0_s5H0Jvc5U0jyLgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/105014" target="_blank">📅 17:50 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105013">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/beb84b277b.mp4?token=ACmWmb_X8ed0ZJGJrnq5jM83L83iSja1YGdniM1nM4n-f7TBPEaq4eN80SRDXYQQKH-fvNqXR6kui3CnO1RihB7mVE9T9ZId1Sv0MxjvD-hVTUrOlUKgiwCKrVBlfZ7nbteoQM2WEaw14ro-J1evHhjyJ1Ehf12GVtqJog9B3MyXomKwDai-b2L4HkNOcXAfghwstAG9BPTI1zZ1v6PLb_KTK-kwoIfQzo9negxPTqM8vGLUTH4P4ks_wKD97Ni5h2Pm8pMSwc4EDD9PjROYt-Cl6Hv1BbvSvlt6lmeSZsf6SLQbiYR_IPqTxUNh3tATT5kGS15X7jzrnjvhCN5KAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/beb84b277b.mp4?token=ACmWmb_X8ed0ZJGJrnq5jM83L83iSja1YGdniM1nM4n-f7TBPEaq4eN80SRDXYQQKH-fvNqXR6kui3CnO1RihB7mVE9T9ZId1Sv0MxjvD-hVTUrOlUKgiwCKrVBlfZ7nbteoQM2WEaw14ro-J1evHhjyJ1Ehf12GVtqJog9B3MyXomKwDai-b2L4HkNOcXAfghwstAG9BPTI1zZ1v6PLb_KTK-kwoIfQzo9negxPTqM8vGLUTH4P4ks_wKD97Ni5h2Pm8pMSwc4EDD9PjROYt-Cl6Hv1BbvSvlt6lmeSZsf6SLQbiYR_IPqTxUNh3tATT5kGS15X7jzrnjvhCN5KAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/105013" target="_blank">📅 17:41 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105012">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0d80d5d54.mp4?token=OaFHDG3zIEe0gd_WiPH-HIcal53MzAD1hEssRy0OYzrwktcgYVG-Jw69F5N_Y0Z5awc4_6IjsGuhe7u1q7SECVJGwvebe2j7LHPVeP8NcNVq7jd9uXK2IcFQjP1VJSucSRR0zfiC92KhczWYCcRGIy5XunvuG6EN7Au1Ohvba16Ta7IXiL34vAbvz5TDcesQBjserRAhfnWjMCxPTP2s0bo-H6eXAK5VAWPjJ-L46Rbed5RKd0JOpzVQEKAn69aOiO6dhZYc_TvO8_vpOdya4P8k7OgYWDzT-NKb0G-edaqygJyukSLr_MHg6ytXwG51zsl4uQWFLu_-nppxdbHVcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0d80d5d54.mp4?token=OaFHDG3zIEe0gd_WiPH-HIcal53MzAD1hEssRy0OYzrwktcgYVG-Jw69F5N_Y0Z5awc4_6IjsGuhe7u1q7SECVJGwvebe2j7LHPVeP8NcNVq7jd9uXK2IcFQjP1VJSucSRR0zfiC92KhczWYCcRGIy5XunvuG6EN7Au1Ohvba16Ta7IXiL34vAbvz5TDcesQBjserRAhfnWjMCxPTP2s0bo-H6eXAK5VAWPjJ-L46Rbed5RKd0JOpzVQEKAn69aOiO6dhZYc_TvO8_vpOdya4P8k7OgYWDzT-NKb0G-edaqygJyukSLr_MHg6ytXwG51zsl4uQWFLu_-nppxdbHVcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😐
🔥
👀
پشماتون از ایونت تنیس تهران بریزه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/105012" target="_blank">📅 17:20 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105011">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kBJn68zVsLMgDA0_Vb0i4ARAAxrZDJKqbaFOdNNjKeGxXddH-Y_y-QLEYylRNPkuos-SEhwp4KH4eBagl8kJTdnsKhqsKnIkgn_uGpUns3j6ztnUF8kSbLevG_t0xCesQSd2hPNXd7Apks-UMbEgCinx9tCh8RXa8UArc0im3NNZiseZAqV1sIK848Mx2TSTCstFXgWmNFdZfdSe2tHoIHIEZBkj2vgtBRaBfGXEyUl6RQzPiGCbHABBqZ5knULD8CRI4jHaJ4YY_rqTQNcsK4s3Nt_iaLTcI4oz2w1_ckg3-pVpY-hJLoDcP4rOV1WQTQ7rWWhju4lR_D8lpmNPGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🗞
🇪🇸
رومانو: سرخیو مارتینز هافبک ۱۹ ساله از رسینگ سانتاندر به رئال‌مادرید؛ HERE WE GO
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/105011" target="_blank">📅 17:09 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105010">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U6mLl4lvn7aH_CRuQ1VSM4FtOFhzQw6WN5GIYwafMWyVWMJjIBN2GGrkXMfbMocHLAH5hA5HB1l_XGtdE2_0nx8RzED6qDpUchcvyXCT4dZADSczZi3ccXUXacJGL17_xOk9QEM_C6sXXMagPZ0AUJ08SYfpJfAKR_XlPYIbO5zfRC4NoX9aG9miFz72SPzKbvsiYyUsk9OvWQ8P_d5dSMMQSwje53JNcxGIChpyUxIQh3DEdKTedGNRTwM23K01ctiypZ8cUN0O3S4wZzaIUE1fkucdXpQ91byHKQKJHyDKpiKZtdb54znSeIkBvcctc15etTy4vj-PIjgYYiLukg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/105010" target="_blank">📅 17:07 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105009">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C9U890IydJz5Lf1xgF6ASnSXIFOzrJ4fQvWOjBsrlI-ptlJGqUT41JLebjP4JaDnXPWwuB-qUNJJV2vtWNeHY4jYqh7F7JPrKD_BZiwnU2RqsnEXDq2yHCJXCVSJR7U-dPWk7axTy5MYfGn5dhPy5GYuARGtfGJ7okk6FuQlLw1EBriuxxxt9NX0Dr_8IHEe94-CQnRY6L0lHz1JvnhHLbiQwiErw7UnJTOY6S3lnGHGy26-RX57IYAr0D8xrhQxDji10fTXb7tyxADq1is469ViVepv1VV69MSXaNtHIAGn64NfyOBrcS95q9ExhfCEjYIEV96aJgqpHlZiKDbOWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
هفته‌دوم پریمیرلیگ؛ ترکیب لیورپول مقابل ناتینگهام؛ ساعت ۱۵ شبکه‌ورزش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/105009" target="_blank">📅 16:58 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105007">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P9-Vt4sMt2CNxhtjZUECY3rp9wdjpZLGKSPzDjXAe72qIykiKO6tbSr0qoq6wl4v_OuBr1O7P-OK5iTpd13JXFJijTDu5pe73ZoAVhdvq54_n7ockBzWpNF1ZnS091NkP4cZUjB7uT2NkEFOnV33m0qeWAUkMeSUgb9mYUwRULM7yB9QI_P9pBH1eej4JF8oMcn0Gk-6GrK-cuwiSZ1R0OM9Tj8S0xPl0LAHd-ZdM9rArNPRv0-4kvrNBiWhibeLy3hPGOr293HpXHOfOgnU5TqQpQVSKBHvTguLh3IHMhRrOdxft1JUHYpq17EJIj5T-JjcdJQyNaeyS54RfhsIFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/W8lxznMDByrTJGX3TbKn-pbab7TcqHTgdKrHR-FDtjIbOtXK9avAbAVkHX6w1E9Q-6a2xLEfbvFBmRzbAsELvjvxwt-s8eSUtPgBFh3tZSuosmYB8Czg9sZ1hshYm8MBFYB-vq8NagfI44R3buVijojo8rouxwzo-s8pk2Z9q8IgWhb8zsPCQhFGN9Thqvmyj2IMygbXvNJUO15luMfu_7nipE9GPNP5Z6iBQc0jghwhSVBKMHgn4GGkTNkYqjO5Xu0ai4kGvVCZNzTD7B5DOsBIealDB3ELvoqsWqxBmlkhNVBhLn8U6qnPv7qam_-laIV17jEzguNbeBYiFTojYg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🇪🇺
برنامه گروهی بازی‌های لیگ قهرمانان اروپا 2026/27 مشخص شد.
18:45 اروپا = 20:15 ایران
21:00 اروپا = 22:30 ایران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/105007" target="_blank">📅 16:56 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105006">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1e0ed52814.mp4?token=ZlWe3aYD2x3de1PKOGw6PEVvtmvF8ZfuUMxEwvm7FRLC0YcpP7Y5kgJfz1MHUTi4KNtbnluUDeYbqxjhyQyqDS04Myx_3VichXwo-UqR1nW76tEJzH9Xhwxc8UdNn4IlaXs2giNqQ06CPQs0JJ5zhowuAeq8deznws0ak6W-XhalMGR8fg0DtS_E-Uc1diDgCpFIHmp_3J-jb43oHHYUekYqwTQP05puPBLRpvCdsAz-7HoTmn-EB9tTDWIlhtIFEVu4BeW7fDsB6bfEwMas1O4OKjXKkS0LOT1UO_xDb6GDVRxBrVDaQJHnHBf-klxkC9mMuizV0dMZYWoehvWvsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1e0ed52814.mp4?token=ZlWe3aYD2x3de1PKOGw6PEVvtmvF8ZfuUMxEwvm7FRLC0YcpP7Y5kgJfz1MHUTi4KNtbnluUDeYbqxjhyQyqDS04Myx_3VichXwo-UqR1nW76tEJzH9Xhwxc8UdNn4IlaXs2giNqQ06CPQs0JJ5zhowuAeq8deznws0ak6W-XhalMGR8fg0DtS_E-Uc1diDgCpFIHmp_3J-jb43oHHYUekYqwTQP05puPBLRpvCdsAz-7HoTmn-EB9tTDWIlhtIFEVu4BeW7fDsB6bfEwMas1O4OKjXKkS0LOT1UO_xDb6GDVRxBrVDaQJHnHBf-klxkC9mMuizV0dMZYWoehvWvsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هانسی فلیک: ژاوی اسپارت شگفت‌زده‌ام کرده و برام سخته که بگم کی قراره توی دفاع چپ بازی کنه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/105006" target="_blank">📅 16:55 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105005">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ELGZWpkCixKt_-Ut9kCaEFPyWRAXnDuVNXK0XQKznpO6WjxAamMG8qVB6BhyOdrUckwGs0-onP4duS6jLontTlOsYmCm_55y9OTcgguv-X5mXVo-ZryosmKidOr5ABWjzGwwI0xvSEdDgq6x6_oZgbXdykic9bqKX2Up7eFAkdi0dqhGZ1hgC1o-Jt-0DU6k-2-Au6ZyOGOEshYgBzUl3_xWpH4ILYy1x3HPHYJBGuTNpGJ3uI5VVnkKwtpe66kWujZoqx1AYi-Cw3ABJBe5BvNHwCLvocR22z5bLHoDhegTTrGu93poznIBWipJCQUaY0ZY8zJq-e1mP9zoKXvDSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
مقایسه بازی‌های بارسلونا و‌ رئال در اروپا؛ با ریکشن نشون بدید کدوم سخت‌تره!
🔥
بارسلونا             رئال‌مادرید
👍
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/105005" target="_blank">📅 16:33 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105004">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/609a9de2f6.mp4?token=ursnUfdO0l82og_23nlKkpFmNUXWD-MulsQ7AetkfC4o7HMYLq2yXwVR2DECeKaFyQBM0fSvlzqQdNp4u8EzQU3RjsK_Q7tR57zFhBVd7mIxuoPJMUoCG03TPTVSPOSQ_IbyxB2xiSsp1QI8HZ2BqTUqaLSXYcDEb4Ap4fUTE6EYiPtYo5xaRV74DjkNK2YQBsKH32GMPf74oWV3EaMESu157oMBaZnaWsZyf4IEYk0iCUWDdLn51xPUYs2uSAjMuVTVuGVDYqYsRE4M_okmk9L9PLkifG6LhrH84427D0M6FGJ9aZ_D1LJOM-ngbwgnezpCyPangLgL9ulNHCcGvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/609a9de2f6.mp4?token=ursnUfdO0l82og_23nlKkpFmNUXWD-MulsQ7AetkfC4o7HMYLq2yXwVR2DECeKaFyQBM0fSvlzqQdNp4u8EzQU3RjsK_Q7tR57zFhBVd7mIxuoPJMUoCG03TPTVSPOSQ_IbyxB2xiSsp1QI8HZ2BqTUqaLSXYcDEb4Ap4fUTE6EYiPtYo5xaRV74DjkNK2YQBsKH32GMPf74oWV3EaMESu157oMBaZnaWsZyf4IEYk0iCUWDdLn51xPUYs2uSAjMuVTVuGVDYqYsRE4M_okmk9L9PLkifG6LhrH84427D0M6FGJ9aZ_D1LJOM-ngbwgnezpCyPangLgL9ulNHCcGvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🥶
برخی از نجات دروازه‌های فوق‌العاده بازیکنان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/105004" target="_blank">📅 16:05 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105003">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5be1dc5a15.mp4?token=raXQMv_He9u4dcEfok0ZxUbWZvxrrkYFzjGPRZFXA4qapkOiYgIhm8W-yLdHRkVm9HNHneGpRXaRH6IH2-znLujDrPEXdnD5zMEU3u4xDSp3JziioP8baFPzNTXsJSUDoKPr47Q2ZgEGShRwJIfXElkr14HqrdgpbCUTCT4OEIU2FYjXJjcHV82AAjAMA8juijKid7QulUcd26rnpVod89_flD7ehHH_kNnmP_ab072CQQCUWkGpLWtzZ6eJ0NmtSZxyDQEwCpX97MQz0Rj8ZgjXIt9b548pLw_BmOqMutEGunm-D9Cv7gIi_NfBDF4M4LZtYgxveOO7XotHFDSoAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5be1dc5a15.mp4?token=raXQMv_He9u4dcEfok0ZxUbWZvxrrkYFzjGPRZFXA4qapkOiYgIhm8W-yLdHRkVm9HNHneGpRXaRH6IH2-znLujDrPEXdnD5zMEU3u4xDSp3JziioP8baFPzNTXsJSUDoKPr47Q2ZgEGShRwJIfXElkr14HqrdgpbCUTCT4OEIU2FYjXJjcHV82AAjAMA8juijKid7QulUcd26rnpVod89_flD7ehHH_kNnmP_ab072CQQCUWkGpLWtzZ6eJ0NmtSZxyDQEwCpX97MQz0Rj8ZgjXIt9b548pLw_BmOqMutEGunm-D9Cv7gIi_NfBDF4M4LZtYgxveOO7XotHFDSoAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🎙
پشت پرده خداحافظی خیابانی با صداوسیما
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/105003" target="_blank">📅 15:40 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105002">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/96846109dc.mp4?token=hm_5TVrMcdLw89mdbiKEm-I4cFDOMK2pkH8YwXZjibr6vgBfazQ3h2DkMTgEh6nzLPyTMtDu2Fze-rh4IDqebj5qi208r4bSOHuGOvbJiLkRRaPrrsnQXJc-sP9OkAmZWXxJ4wPSYZsSw3lZxej8Vk8GBrDeFUbVCqQhz4xaYNupFm3p1hFB-7PJe2Ax2KYe_umKHcvJx-5D9QJUT6meRMmdQjYOWwz9KMPAIKpN264Q6pIYVFqs_rqfNh1eQgKPk8nrNpD3mJkxMAXf2FUAw3EzfwTNJZQPK9kwT_uTJ4JQu4pqsTEj8O1EVaWD06xA8UaZp3W7WClFrYhJCuFqdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/96846109dc.mp4?token=hm_5TVrMcdLw89mdbiKEm-I4cFDOMK2pkH8YwXZjibr6vgBfazQ3h2DkMTgEh6nzLPyTMtDu2Fze-rh4IDqebj5qi208r4bSOHuGOvbJiLkRRaPrrsnQXJc-sP9OkAmZWXxJ4wPSYZsSw3lZxej8Vk8GBrDeFUbVCqQhz4xaYNupFm3p1hFB-7PJe2Ax2KYe_umKHcvJx-5D9QJUT6meRMmdQjYOWwz9KMPAIKpN264Q6pIYVFqs_rqfNh1eQgKPk8nrNpD3mJkxMAXf2FUAw3EzfwTNJZQPK9kwT_uTJ4JQu4pqsTEj8O1EVaWD06xA8UaZp3W7WClFrYhJCuFqdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
✅
مرد سه‌هزار چهره با حضور مهران مدیری از روز جمعه ۱۳ شهریور هر هفته پخش میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/105002" target="_blank">📅 15:15 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105001">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/568c088f46.mp4?token=fdx-3MjSL0HoBcjruQ6bscQVlG-3rBoNLp11-yY8xWqsYnnE6KVTJy-TGdVLRHiJYnbIvPS7b2DbJrgRRF3gmY3W436n5i8k-gfYdc3phGj2JMWLf-eNaPPWig4aMywKHxZ7o7NIVc7OLU2Vf8yLrJizSQw6kc84KKuAc8tvjqlowpAZ7mq9DXphjqh-MAOXcQU6zzL-xLoxTwkRQlFrsXX4EDj1K0TQa3Hlp4Ppvdm2Juu7OHdmq-bzBbHBnudtsd-G1TEyJQkhq91YaPDm7TXd1UGYybumKGQ6yxtv2P-cRnhoYpbNX1L_E3mO-Wk2_lsxAQeXwgQGge_9z_QgxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/568c088f46.mp4?token=fdx-3MjSL0HoBcjruQ6bscQVlG-3rBoNLp11-yY8xWqsYnnE6KVTJy-TGdVLRHiJYnbIvPS7b2DbJrgRRF3gmY3W436n5i8k-gfYdc3phGj2JMWLf-eNaPPWig4aMywKHxZ7o7NIVc7OLU2Vf8yLrJizSQw6kc84KKuAc8tvjqlowpAZ7mq9DXphjqh-MAOXcQU6zzL-xLoxTwkRQlFrsXX4EDj1K0TQa3Hlp4Ppvdm2Juu7OHdmq-bzBbHBnudtsd-G1TEyJQkhq91YaPDm7TXd1UGYybumKGQ6yxtv2P-cRnhoYpbNX1L_E3mO-Wk2_lsxAQeXwgQGge_9z_QgxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😢
وضعیت شیاطین‌سرخ بعد قرعه‌کشی لیگ‌قهرمانان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/105001" target="_blank">📅 14:50 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105000">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5e4faa301.mp4?token=lL9WVjiN9223vlkdUAj978AQfDyvc98cBFfoMfwl3jseawOkyStOceMJRgU-CTQ3-HKtmd8v7XN74fYibBNgqNdWz5qPK4aUmhIz4eAh1mSn41LSyq9ABVGYN7rCO2lV9cdEaBc_QFmOFRh4gKVmzUHG3Fr7qlLLJME1tye2BzB5pHDIiSPAlkQDMhCuAk0Beqblp6IDhP0k2tKNLGd5QTIyw3oRQ-N2kf39mZR2jFZKf0KNQdx5u8gWSKWCO_t2dE8p_7UaLTw8DLFLVe4zBkNyyh3xlsJUQ95t3UB08iDferNvkw7y6V4EkQUDFCXGOFJaEreK7tFpn1ZMm8GrWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5e4faa301.mp4?token=lL9WVjiN9223vlkdUAj978AQfDyvc98cBFfoMfwl3jseawOkyStOceMJRgU-CTQ3-HKtmd8v7XN74fYibBNgqNdWz5qPK4aUmhIz4eAh1mSn41LSyq9ABVGYN7rCO2lV9cdEaBc_QFmOFRh4gKVmzUHG3Fr7qlLLJME1tye2BzB5pHDIiSPAlkQDMhCuAk0Beqblp6IDhP0k2tKNLGd5QTIyw3oRQ-N2kf39mZR2jFZKf0KNQdx5u8gWSKWCO_t2dE8p_7UaLTw8DLFLVe4zBkNyyh3xlsJUQ95t3UB08iDferNvkw7y6V4EkQUDFCXGOFJaEreK7tFpn1ZMm8GrWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤯
🤯
🤯
یه‌سوپرگل در محلات برزیل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/105000" target="_blank">📅 14:25 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104999">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eeH6oL0lQ5QKZdS5fOjiQtIO11rR_15RIwHROyykbwJn5vV7MjLIQPmZ_wNSkCdmsESvwhAS--FCsjNpo_95EmfxLgxSS_9vs8RbdE6ROJM8ofqBODek1MTrBy1_1mL6rusGjlffN4Ob951lj6gSDDPffXnn5YY04TcbeKsqygnQFfN4LwI6JPbVKRqWELXROvs3P3qhzUNrf28l50G_fZ7sTGUg4VUj88go6moqwI9spp7IzCgzCCnrMa0-ydxzXOR2J-l4WeK9WTuKV_OXXyoUzlRnieG1M-reFLk2gVdYY5GSUI3h3lHWNqk4S3H2OZgfWlWB5O_LnhYWQxkx2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🇪🇸
پردرآمدترین بازیکنان لالیگا در فصل 2026/27
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/104999" target="_blank">📅 14:00 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104998">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mVVRrK2E76bUj69daRCKMERC5oBCbBZbOuTmN_8mcWNr8dejZ6313Z1LjoCz2bBlONVqCCo1Lpz__BH3MhP7BjxgrlxbHpo32VzAD8dAVriRcDgNeXn2mbB8rRG-4pUmNxdbrsUoWwtpQgXThrnZhPLYgUETblGLMbdWkzG21nCgsk7el3IBAvjFT9g21HxNNfjozhSiHR5PGh9GIWv-lpZcuiMhaxjPp_Vn85MWPJUD2pagGKK4pgbpQxn2Fj_yyeBOCzceQfgEip0blQudJB_cBrCCF0wJqjV-5rSWTAo4S_ySNawtUuuFas-uNhvKuqJG18zAEHZ6ZuNwKWZsPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
هفته‌دوم پریمیرلیگ؛ ترکیب لیورپول مقابل ناتینگهام؛ ساعت ۱۵ شبکه‌ورزش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/104998" target="_blank">📅 13:50 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104997">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o-PmqfaXbJFmgKGSYDmlnLWyfyAjZ5hoxgDw7bEVMkltrMyIab118X72ayXlOcVW2d5iZUg8UwQoTQsEQGZypKiYEK0SF1tBcGgtiaaxAn-xSNuDRa2fSkSir1_8XQ-_HqDGRY_xvkp_ZwOUVSlyT0fCoi_V-7TxFA62SAVoiHYm5jFXX1xr_wzKpR-En3d_M561W9_gpq43_GgXzACKk8pLUd8Er3OfcayiroDCLTwcE7SsN_6ODJ2LYi0RHUHfRyLM5zYYXxqF4RxM5N98ss4PF3Ak1tRjx2Du6Cv8u0xPZRO2c1J5lCVGKkfbIxdcMO8OHZHpt8HX3h2a61qPxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
رشد قدی لامین‌یامال طی ۳ سال در بارسلونا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/104997" target="_blank">📅 13:35 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104996">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iPgJMI8rSzn6r8s7KoGs1k1CqvnzcDaeX6zZC1TDSDTbkdhd0fPKP5KAhHg85llG8Eg9xg5dAg7oYkNdbLbqnIzn_AC-jalquovaF63Ovls_VDk-YsbqbQ3fX1ZM9EEbz3ptEsJEViX7BKgvxAhPAiFKCJg1CaF76dl7JD_AW8RmAyMBseYU4IBn2nl1wU_au5n1AfMPhul9PgTBdTKvjiaJ1CZT0CZU8CrjZjfjpN3yC_RO26r3pOdHp5OWYveXb36DfME1LRK2O8hqQcHVnhQqm3oGZ8jxGUJd2Gzve_QbYoM1cORkNhgm1Co8C4qA-kYL52KKfw-sCYMsf2xBkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇮🇷
🇮🇷
ابوالفضل رزاق‌پور مدافع چپ‌فولاد:
🔻
پرسپولیس میخواست برای جذب من رقم ۱۲۰ میلیارد به فولاد پرداخت کنه اما در نهایت این اتفاق رخ نداد و خوشحالم که در اهواز موندگار شدم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/104996" target="_blank">📅 13:10 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104995">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1d94427ed.mp4?token=M5cz2mB8iah89baP0r2V2QnQN6u6MLAZSLCEsMlrqULLNh7EQ_43jH1VTrLQ6YNO-5S5rfQpe6rRioyQG2434777897XQJm6k70YWig0ph4uMXCg_zrWYExctXQsxhHBOGbV3_U19EXuoevcimH7HaGoo75ae719aT8vca1TAmvDCLWOwATOcGMSzh-Eg0eBP3VES-g1PcPbOoy3i2jPK57S-q-Djvz6vjrKsomVIe9uS2oWLYQxyUdzh8ORCkSwCT_SogexRsgY154VVH5jCgwNRDd7KDcRDYMM1I2lUzzqsWSSRo_-7eRUptzA6HR7B3_0L_5RSTrZ_VB8LQl9kA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1d94427ed.mp4?token=M5cz2mB8iah89baP0r2V2QnQN6u6MLAZSLCEsMlrqULLNh7EQ_43jH1VTrLQ6YNO-5S5rfQpe6rRioyQG2434777897XQJm6k70YWig0ph4uMXCg_zrWYExctXQsxhHBOGbV3_U19EXuoevcimH7HaGoo75ae719aT8vca1TAmvDCLWOwATOcGMSzh-Eg0eBP3VES-g1PcPbOoy3i2jPK57S-q-Djvz6vjrKsomVIe9uS2oWLYQxyUdzh8ORCkSwCT_SogexRsgY154VVH5jCgwNRDd7KDcRDYMM1I2lUzzqsWSSRo_-7eRUptzA6HR7B3_0L_5RSTrZ_VB8LQl9kA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شاهکار آلوارو موراتا در مراسم معارفه به عنوان بازیکن جدید تیم‌فوتبال لگانس
😂
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/104995" target="_blank">📅 12:51 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104994">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tUwEOP8TvNYGdE-CPHpW8eTXK3zfGLHSVHG0bdUlH-6lgiWyRw8chVxrXwCOJMTOo5HOtZZb4cKbXISnlwRucB8UlMkLDY2Q2K7bt_JOFBKzHpb4tTD8cmkFwWguTgnhDELAOe2aCg_eYATQpFF4w7cwzQyre7C787_m7bb0hEpu-JprlK5Gbs5qHEWbavYHozGxNyXsLlvW3YxBnDRYJcwSgizFNYQ9l_ZWEeuDKOBVnEcpvTH9hcNdFkEWHmvjOAcT7siCEkK2tmgI8B4VXfvyJFxQQrVykPVj1TQxeRIemzoPw3l8IEBCuj5dTm-hKNCFmqLXBt1jU2WQlT8H7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
🇪🇸
🇪🇸
خولیان آلوارز از لیست اتلتیکومادرید برای بازی امشب مقابل سویا خط خورد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/104994" target="_blank">📅 12:45 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104993">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/694fb72f97.mp4?token=kDc7T_yilfrfc1X1hXAhtoAmb4OFc6O88oSHsvGLiPXuMN5kdapTfCdgrMCXTPca_wwrL-jYPYBFOxMqNwCLJiuGeCTcQpywkuaAX5U55PHfRZdYVncsv9a0CsgWuk4Sf1UurA3YuQ6VJZwXXwPJrYmk1WVxlTYlJtZloXwKNB_ofWL0RdAibo9QimvbjepXOhn9xuQe4sP5sjYI5V_PmRUlV7ydil1gTZot0lbwE33a-LcMB9GG8NSSjtAVhO_MniY9O-iXQr6Luyl-mQ4xGOHLes8YbAQaAhIvlKBYx5oAihK00-4hXuZh2oLprWlZpVtSpsqOTRRDdGN-wAF8KwVyYtAiFfGnHVnz4CrM9HSAmF53UAALRQGEZCWmr6PL50neizxyIIJRC8CxcUl8Wa8e5L1Yx7FjsnojO41VFR2usrF0LKup16e-9X1Kfx8u7huZEKNs8kM9kHLT-DCqDuFJg6kSzMLNvLHqeGq8FQKewikk9fLEeyY-C-iqCxzRMAdE4Ci81wQpDy2Map24AyUb4gUF5CGoRNOM3TqAM-x6rftHfCvkIUF1CksubfNAHh_1w6dzNPngAtBqIwV03YpR-89bdsXRh4aJFy02iBlizzYinZrk4r_svM2j1XfWh7gc7foPYmQ5CNld7cMsUMK9hrxWOSZzIo7HGReZacc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/694fb72f97.mp4?token=kDc7T_yilfrfc1X1hXAhtoAmb4OFc6O88oSHsvGLiPXuMN5kdapTfCdgrMCXTPca_wwrL-jYPYBFOxMqNwCLJiuGeCTcQpywkuaAX5U55PHfRZdYVncsv9a0CsgWuk4Sf1UurA3YuQ6VJZwXXwPJrYmk1WVxlTYlJtZloXwKNB_ofWL0RdAibo9QimvbjepXOhn9xuQe4sP5sjYI5V_PmRUlV7ydil1gTZot0lbwE33a-LcMB9GG8NSSjtAVhO_MniY9O-iXQr6Luyl-mQ4xGOHLes8YbAQaAhIvlKBYx5oAihK00-4hXuZh2oLprWlZpVtSpsqOTRRDdGN-wAF8KwVyYtAiFfGnHVnz4CrM9HSAmF53UAALRQGEZCWmr6PL50neizxyIIJRC8CxcUl8Wa8e5L1Yx7FjsnojO41VFR2usrF0LKup16e-9X1Kfx8u7huZEKNs8kM9kHLT-DCqDuFJg6kSzMLNvLHqeGq8FQKewikk9fLEeyY-C-iqCxzRMAdE4Ci81wQpDy2Map24AyUb4gUF5CGoRNOM3TqAM-x6rftHfCvkIUF1CksubfNAHh_1w6dzNPngAtBqIwV03YpR-89bdsXRh4aJFy02iBlizzYinZrk4r_svM2j1XfWh7gc7foPYmQ5CNld7cMsUMK9hrxWOSZzIo7HGReZacc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
رامین‌رضاییان دیشب قصدی برای خوش‌وبش با نیمکت‌استقلال نداشت اما با توصیه ساسان‌انصاری به سمت نیمکت‌آبی‌ها رفت!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/104993" target="_blank">📅 12:20 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104990">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g-v3a_1uXk0xbU9y4GpV9juR-tBndE74jgPWcrL85O2tJRdCDN3l-3eLblWThmYkwJO0WTKd779fpXbY3A6zydYD8YbCkcgO87-RdxzlNXWDshVrHVNxmETmdyMvbMBdgQ1JTGcNEFKELNOkPAfTjlOfo5rz92GaZuQxIs-wLWgrE76JtyyY-m5_buQMnz-O2sG8-yWt0udIySUlWu3_iJuqSDS1-kRdIszUVUPZrTLCrwd-EpdH-VtyBCIImKuynxbsWtwrsmPQeoatdMYyRBOac7Cat-YD5loGh3aHNB-kfZn3TbcjW6FZGzJD1q3RpCadpX3zDqxr9__jIpa8xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TWuw6mitwIaG3HLJIeXLcGW-6JsyaGTBJaAnXz-yU1aSSDGFuJfBNPdfKZzM1Q8yLUxxxaQ90_yzoLIAaP2-TJOAi_AQ5-rjGRn-0S2SfC7ZXiXVvRFRLKnHmGR--VyRFAf-w7S7N37FqHZ0vSTVSTvJ4mneEARQjd8g0RhBRjTYb3x2FZdVv4E_X2r3iNCn0dB4plb6uUDJ__LFrFeWvgOFpgEWe49SXzjYJ75AaJ3XsVNJIiuioqk3BwEE2--DfMMoJjofCfoANoJ0ttmEsubIczNRwiKImvWFD4IoGfC2Z10mH-8nQkhZW9kmmhRb02BVsHPif_Ox0FB336RTxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BuTJRpURXj4YKwGd7IPyjb9S75Rcr83XyeGWQgTXKj7KCigoxnkN8xn_4hV5EfrIN7cce8NfR071ftr37MN57WKr_1DxEwHyFe2RlVs5MepFDpE8IhJLzs2Oef8vshQTb7sex4HoFyNCEYD_ah3PzS02YbeYQks7PZpI7P9nqe2mjIMphsJJ4CbpywNPT1K5-nngOKxxKinu05FiP8dhngWB1uTSfBQ9FkzDaps9llUH40EgdW8uReNWCIyw6KxCVsuO-oDSJc5mLxUadbLi_fZr0gdogGasTXHra3X3hsjN4rZ6j7eVZFrefl-ceyw2GK66tEq0W_h22WPOvuU0Dw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
گابریل آرتتا، پسر بزرگ میکل آرتتا، دارای یک ویژگی نادر به نام "هتروکرومیا" است، به این معنی که چشمان او دو رنگ متفاوت دارند.
❤️
💎
🤯
فقط حدود 0.1 تا 0.2 درصد از جمعیت جهان این عارضه نادر را دارند. یک گوهره‌ی واقعاً کمیاب!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/104990" target="_blank">📅 12:05 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104989">
<div class="tg-post-header">📌 پیام #5</div>
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
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/104989" target="_blank">📅 12:05 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104988">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lUxatrS0QwVbVy0VgCoFEuDy7UZaczKVimXqNGaitk2ahRUC466CVexNvOdteML590_51SCGY-Vf8TMXDKs-h0JWluXpX8XoRdP2iw4VnowsyZMDnfqfptVizBPCurXBXVvB8ayBNFZygs4SucfBvV6z0dWmXyP7wn-0iLUhrY3IxdQ5bsTJVsFGqUf-0VWFQ89TDEQT05Dx7VGYvG4pPEMwRuNlJSRkbNUzKrbFSm_ND5UKysFS60YPfRvjahjVIviAerzfgax_p45hEiL9gJFLJICac9r1DwEw6fNx9QYgfGEGKiKyi2F2UcrtoHYpSq8eNXm52cyh4SKek3AW0g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/104988" target="_blank">📅 12:05 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104984">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb4df35536.mp4?token=hiJBV5vkiVWC0_eXHvKEHGtmBmpL8BWV9hAOXaYAjxfPWfmE5FPC7ZZpFleQ4btChqV1auYyv9XbsKP7sT8BVtqrTK7FaN4upewYOJewgjrbK9lNcrzKUTAx9fpU5PCeny1qV0dmZNz9bxhltDRZNQBolD8cdYryr2O0h9ByK_1Dg0aiPxATnkOqcjsBu9_ZyLl7E1wqy3vat1lzS6UMxK2YhGPsSWke1Nx4VjTXVZh-V4g9nHSf5tssI9dSOmhVrNV3pe4cqpQ8g0agqakl_0S8BuS7PtmOzQECR8_rk84EjYc6CMogCyOYpkY9g5o8XG11Y4JsfPeHwPq2_Lj7ZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb4df35536.mp4?token=hiJBV5vkiVWC0_eXHvKEHGtmBmpL8BWV9hAOXaYAjxfPWfmE5FPC7ZZpFleQ4btChqV1auYyv9XbsKP7sT8BVtqrTK7FaN4upewYOJewgjrbK9lNcrzKUTAx9fpU5PCeny1qV0dmZNz9bxhltDRZNQBolD8cdYryr2O0h9ByK_1Dg0aiPxATnkOqcjsBu9_ZyLl7E1wqy3vat1lzS6UMxK2YhGPsSWke1Nx4VjTXVZh-V4g9nHSf5tssI9dSOmhVrNV3pe4cqpQ8g0agqakl_0S8BuS7PtmOzQECR8_rk84EjYc6CMogCyOYpkY9g5o8XG11Y4JsfPeHwPq2_Lj7ZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
🇮🇷
تعریف و تمجید حمید مطهری سرمربی فولاد: بازی هجومی استقلال باعث شد تیمم مجبور به دفاع کردن بشه چون تیمشون در حمله خیلی فعاله
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/104984" target="_blank">📅 11:53 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104983">
<div class="tg-post-header">📌 پیام #2</div>
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
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/104983" target="_blank">📅 11:45 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104982">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XuGA4r9rNS3QaobWWdNN87FcAx3cxFVPX9_q8eLOliZTmdwcPp4EmtKBD5DkegT62qrBN0M03bvYLGy7IRIVN9NkKs7N7cimLkDJO09AfAw9otPy_M9i3Oz6veXN8Jhqhzj2bLDht3yTu-r3yq_1DrdscIBPLrIEKFk4sl4xR7XgAufrISm-ZR1HtvSjvj8RkgXNdCzOUJAUqxb8Xks9wKzcdKRTMMSbGz_xGeafCaPDPDYxIyK3DFFhJg7LTl21wzu-d0LQeJ3DmEVuk9je5uiUOBB0FXLEtULazRmYJKAHv1TO8u5NLdLl9Wg8Dk9wfKcNvYEaPzGUXSVEBmmfzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
✅
صالح‌حردانی و رستم آشورماتوف مشکلی برای همراهی استقلال برای دربی ندارند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/104982" target="_blank">📅 11:10 · 07 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
