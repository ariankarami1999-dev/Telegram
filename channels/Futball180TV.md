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
<img src="https://cdn5.telesco.pe/file/XWdUxjxwYKIg4RFVkyYlUj3sCnNrEcsn58GmpP-kbe8jqG5snBCmsJHIHLsK9c3i8c4EPYE_a_aJpwzOU-MkdAkYoxCy-jWwa98Gj62waDPXNZwUJ_xhhSlLTgSEQoIRYjfIUEvCaokvMVUZ8w83gFqgpXiBBFZ865sY88d7CA0dL9c_jctT9y0n_bHRWn4j9iruK_ib3gnZxMXYha8BNEbZacwDo1IwcS4fG20gBWo5ZFWSpYHgRzPYifEsV41R6xWKBkHmxAQ1yw8ueMQ01dQjk3N_zTiNq266KgjtFSpoAc33vHeAZeJeDG1tzv9_e7ZBIpB2VOge9spQTdXANw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 511K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-08 22:22:45</div>
<hr>

<div class="tg-post" id="msg-102380">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QLfAKICvX3Uz486pXJXeGCeERiCFFDPtDgx7_HqO3I9yAYSd6rQx0UUWpQrmMUEyZBNNHnTDYTsQR5uYgtNfEZPuBIi_1IRxYnkfLC3_Q8zmu7t061cqLImHEm24jIIme_Bynru20vwzG5RRK_TInySyTsqbLPSgveO1V4MtP2WyNPCOaJbhdBI44ANtKIjikQEFy5-TqXeeFckH7wAR5gsUTqWlfHa9ULVm2ywvXk8_v-C-sMappKpkIP7wWEG6FtmudCflb4L-90_iZR71bfkA-w_z2Yr91u-jpybOajghbd44YdT3ONk9M_j9uqO9GdgF6RHu_biacHU1OnGWpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فوری: باشگاه رئال مادرید وارد مذاکره برای جذب کارلوس اسپی شده است تا تلاش کند از باشگاه‌های لیگ برتر انگلیس پیشی بگیرد و بند فسخ قرارداد به مبلغ 25 میلیون یورو را فعال کند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.83K · <a href="https://t.me/Futball180TV/102380" target="_blank">📅 22:18 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102379">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dQVgUtqQN3-UJAAvuh5VwmltILgU-pjcyUI8i7_wU1BXxFDD_opCgYemCZTTBPMgFWfyxxuEvg9AxlXMFmsDXO6ZD469Nx0kgQ-gcKt29bNYFAgwK9uqCgdyKMqQiZvYgBqVvvmdZrTyXh7Oq5oZP2ZRGvJnhii31EvDDOFqnpgNXvA4w1zccbepKpj_GOYKsySWWg4AOCn5kO0LyDFy9_NmHaO0aCVspsphtVb-JJxSp51NSkO5US93vMVo55tHkXMCv35zpfzbigb6LgvqYnuzMLzVgyoLCwPpEVs6m-QLTnodHSLsVUq0JgoANXSHlzbJbPZF3Fkv08fL90V1gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تغییرات وینی تو  فیفا اعمال شد.
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.23K · <a href="https://t.me/Futball180TV/102379" target="_blank">📅 22:06 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102378">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KjpVXpuOYIImt_2NtSjFJQ8jB93UWb3_bXsIuUtdSAGPZu_bEIbYU0_1UJFj7HHi5tN4n666mpuhFWOYv9EEwEqd10WQIoIrjNnGklb58fUVF3g75ZBTwgSNJYKqfnf-WshtuqR8unJCUNsTI6-elYllgb9mHyD39A4879J7U5yVIrNLlXFRGC4pPISjpDyc8Il6TS8ggZyC-9xEipDnGnBhLX2KCHwHmGycucnT0Ij-Db99NmYNr0owFQcOxyLg5dUlZzjColHjf10apPWzQDpBj53_niZLEdid4QJtUUnKQk6t5ogNLrmRx0xE1EuwKSurL58nNMqi--ypeHwukg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
بایرن طبق معمول به این تیمه تجاوز کرد.
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.69K · <a href="https://t.me/Futball180TV/102378" target="_blank">📅 21:25 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102377">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M4MmRsl9_eVxkPaoUF9_H1qPmgI_BY8ZQoS2YcDp5tN6dW2HAS7AhUfi13VqHRAaIBG1VFxm-pfL8RP3AVd5MFX_z1a7sQZ3Njk-w4ki-wniqa4Nu-PZ3bYPN8joQ2i_m_BK7RXAibf1v4956cRUi4qiGQ2SGAcOUpFjcD37uZURU2N8FFpTXGatO25-V8fedtLdYhbjjvZVTw_nPNtkyrI9VvrLfMRMfnR5AZuKzP8d9Bj9AxtYrJSJVRlTiArBHeeW9vm0qZxFqR94mYzQ5SoQLuapTb1fRb_kZkc2iFdkIf_5c_UduegvBILHwnb6Sa3MEKmVXq37UTeVdo2n3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
بیانیه فدراسیون انگلیس:
ما در کنار همکاران اروپایی خود ایستاده‌ایم و بطور کامل از موضع مشترک آن‌ها حمایت میکنیم، ما با برنامه‌های فیفا مخالفیم، جام جهانی متعلق به فوتبال است و همیشه همین‌طور خواهد ماند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.02K · <a href="https://t.me/Futball180TV/102377" target="_blank">📅 21:10 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102376">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">▶️
زودتر حرکت کن؛ راحت‌تر زیارت کن
🔹
همه راه‌ها به عشق حسین(ع) ختم می‌شود؛ اما زمان سفر می‌تواند تجربه زیارت را متفاوت کند.
🔹
اگر سفر خود را به روزهای اوج تردد موکول نکنید، هم مسیرتان آرام‌تر خواهد بود، هم زمان انتظار کمتر و هم خدمات بهتر.
🎥
این ویدئو را ببینید و بدانید چرا
«سفر با برنامه»
، بهترین همراه زائران اربعین است.
#چشم_به_راهیم
#اربعین_حسینی
#سازمان_راهداری_و_حمل_و_نقل_جاده_ای
🌐
rmto.ir
🌐
141.ir
@Cheshm_Be_Rahim</div>
<div class="tg-footer">👁️ 8.22K · <a href="https://t.me/Futball180TV/102376" target="_blank">📅 21:10 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102375">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IhE9JsW1G3TXEq8r9oj8qhZ1RZTY9TWze9NqExerkloiwRO-OWMTxLXyBO5YLoNSWPv4WtPtt8FzL5uQ1xZmUrg4rmD439tn8k__nBwjuoeV0HKcxTGdWBj1KOv4Ns5RUAxg_QozVJVbufOqKPjkquUb2h6sMHLafC_2bWjIdmDJlipzwNzekmEf4FVpDmhF7Xr93gObbock6iJ65OI_YK2VDWwR6ez3r7UFrewUaQa3urbtEj4gPzVFMxgMUjIsUT78J9milmpolgz-Qa0Ic9UrI3hdPH2ctp2FuFRrk5YwK7ZFaTUxYDableKj3JifSEtEQHo2ZPyh_6t3Wk0KsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🗞
اسکای‌اسپورت: منچسترسیتی برای فروش رودری حداقل ۷۵ میلیون یورو میخواد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.31K · <a href="https://t.me/Futball180TV/102375" target="_blank">📅 20:47 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102373">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vlGUMCXF4I7ZeQAvKAdtFUPQ8roV1Z2rZOSooIv5gWYGeThCmdowVJpm884P_07Lxnde1wQtxrC_TFHXhgfqHJzSJCeWbm_Fx3DvFoPt6546ybeeDJyMyIVYl3xQGpslQ0nDtjOP1ICpbMY1Qb_QcQcORa5fICfiXywOoJDea9qCb4M-LjmF6XbeDvtORithY3By_w8r1xe3nkExrGIcizW5_to4oGzkLul4YiTfZJSQcK0P5Rfc8VIJE1l8OKBvFI6jpDUwkRSR_3IOLeghZ3dkT1jAlIGGa1fY5Dm18qGqVbtJoolMH5SwNzrhZw6WO-SK7xzgkil5Ge-cxHKwPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56d9c0f441.mp4?token=vtRVVx8daHKLNbJcL1jzvZvYJ5naLnuYu6DEdXNt8lN-uWqE0r0EYf1jHh8yPg9vJPNtQrgaM8PztmXE763OlgB48QMxDWfRHB8a3KVicod2V93AYyjpvXVXJTRwackBtqKJf8MBvtpFe6Ynlkdeztwc8n2htiJAQ2w0e7eKCE7dCTT8kkvnkQ2cXqlcxuwVYu3zrW3w5Fy8_SIRk6ZaHZdUTKsGgQbuske8NVmqmf_3ZVQI_mlg03bt7woOX5CFuPabFbuk4or29HcsDaSOGUneLkWFNuQaNRcSvf2xZB5O0WmZDat6zF1VA5n36Yrh8DVpy8ivpFc07P0JbZXIlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56d9c0f441.mp4?token=vtRVVx8daHKLNbJcL1jzvZvYJ5naLnuYu6DEdXNt8lN-uWqE0r0EYf1jHh8yPg9vJPNtQrgaM8PztmXE763OlgB48QMxDWfRHB8a3KVicod2V93AYyjpvXVXJTRwackBtqKJf8MBvtpFe6Ynlkdeztwc8n2htiJAQ2w0e7eKCE7dCTT8kkvnkQ2cXqlcxuwVYu3zrW3w5Fy8_SIRk6ZaHZdUTKsGgQbuske8NVmqmf_3ZVQI_mlg03bt7woOX5CFuPabFbuk4or29HcsDaSOGUneLkWFNuQaNRcSvf2xZB5O0WmZDat6zF1VA5n36Yrh8DVpy8ivpFc07P0JbZXIlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
استر اکسپوزیتو درباره آشنایی‌اش با کیلیان امباپه:
ما در مادرید با هم آشنا شدیم. حکیمی به من گفت که کیلیان خجالتیه و خودش نتونسته شماره‌ام رو بخواد، برای همین حکیمی شماره‌ام رو از طرف اون گرفت. چند روز بعد همدیگه رو دیدیم و بقیه‌اش تبدیل به تاریخ شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/102373" target="_blank">📅 20:21 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102369">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OPA7wLvp2bq3XiurIHYyJDW07F_DGFe9eF9REhHfgJQztCqS2MUOFinTcMbUcZAPVtbZfbTwEFhKNkZn9eTZN2AX-BmIfcXuSwDUUbzo-GUsTP4azZQ9CS1gqCrxiaEGVTsD30iCB8T4T4hO_jdho15K4K-oRUYo0i6AIbR25FOE7if88so0jjc-mnY_EoA9Wv2mhQB7NEdd2fI0XHHm7ajV93UU_tEiCYQc8Cr_2uIGbDxIh0XXhqQ1csN53swsikP84omhg054FRbHTK5aeCxlDOT5i81uEtlT1ldrDqC8PCsoZk6CqXxoyheyAD0QqV9qTwsdYnAV6QrKS1lpQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WXVHVYNwpyk7fpz6qPIEVWZPR7dcFHmhuW1oJUsS77yxVhSKM_cEDeEoHZcRn5cmTwfku3qECnNFvjg7aDqYwi4UHAjc8LguZgbOiG7Jvk6i3NNPmBBisTPc9b4ejBsc1-ZeDvlQMbMVlwu4ZbRsJR74uOJQCGlkh7cJkpKJN7XAABjJZ--dQw7WYs2UpNgTmG_rHmCh3Q_m2H0pwzDvw3abLWm-YGSgU-NKfGZevSqP8p6CLBNd70PM66V7enJCm9awVZ3IZtqJ5Vak729ZIhA0UVBxoaq98aiAWroQXMWWl_fPVnIvA0Lw0lCjIhWTXtk5IMGciq2l5bNjR54XQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BuZ_0REUKf83r5lpHWUycWEu6zLIZcNUhg8YiUYjAfPUe9uW45zhwiZdK0-oCjpSLNpaBCQTI1o_UeBuNxbnAg5NM38rEC5xzd_yBsmwvESbnJ8YRcmJKssu_XLrjsowGVlYzTIjwCHHkEnN-iLSFOKdp1KPfjZPCgqHqPCyaNPg1xfL_x98WMuWcPDzctx5kwtuDSqkplx3uWcYF8PH1Cl-262zn5LGKIAKBvkRyI9GA3HNvxd3kE3EqooMD_ZqCKzp_SQjL5VbN6yR5fbPnQgpoyrrV2wbJX5OR5_si4wzdWfCOiCBv3FWmBrur3_TPyx6YG28-KMvJNMySmmMoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nJxGCebcsDEAYxo5K6inySUBchtxzF2rNwHD60VUMfcoTduaNyNLV1KHz8mChAZpC164cowps-jmHaNMpiIJqDLoVZkAoFm30WM9brBjCGyiKd5Y5-t-mU52qmtaCXumteis_kdwkZVnOeJqlQ97xZJ9XjD-90N5S719XIn28BvTZWjVEqr5V_mdNk_z2fsUHOnDjSEOGIph9CRkbAJQYmEg50vVTbhpVQcxJoHI6Bw4DS1__XabM_pS52cM4-cR8ePbFzsudUHeeoZq_wU-MPvtzjTEnS7EniRl5qxFmuwiD1HFxMpH-K7KTW16KgqVHI4nbnwPC_1UoZ2QkNn8sQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🔵
چلسی در همین پنجره نقل‌وانتقالاتی حدود ۳۴۲ میلیون یورو هزینه کرده!
💰
💸
خریدهای آبی‌ها:
🔺
مورگان راجرز
🏴󠁧󠁢󠁥󠁮󠁧󠁿
— ۱۳۸ میلیون یورو
🔺
مکسنس لاکروآ
🇫🇷
— ۶۰ میلیون یورو
🔺
مارکو پالسترا
🇮🇹
— ۵۷ میلیون یورو
🔺
ژئووانی کوئندا
🇵🇹
— ۵۰ میلیون یورو
🔺
امانوئل امه‌گا
🇳🇱
— ۲۵ میلیون یورو
🔺
آلوز دنر
🇧🇷
— ۱۰ میلیون یورو
🔺
دستان ساتپایف
🇰🇿
— ۲.۴ میلیون یورو
⏳
بزودی رسمی میشن:
🔺
والنتین بارکو
🇦🇷
🔺
جردن هندرسون
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🔺
دنی ولبک
🏴󠁧󠁢󠁥󠁮󠁧󠁿
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/Futball180TV/102369" target="_blank">📅 20:01 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102368">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b486c4e528.mp4?token=gvlmaKNTLkRBBqNqZPuDsGyA8qcN19O3_2Y43lbZt4hcOBsnZn7hpexLyCXTZ-yMUnRvvGrwC1kqHMu3QXBD9OXjtv2geIB40zCNDr5OYkJ_u4Of0pCN0Pg8ByyDGJQRm6GAr_QhByeRCVa5suaoEXtZaT2msc9R8ZR-GkXerGPPZwyTg6kHzKkwd6vZLltRW2RGG-z9uT75sELpPj4rtVYUlwCTridEz8Zb2CAD7w_vK43QOd5MKGWdH2zv2_A1TRt77MY1zCl5wKSiRpGi89y7aUjmzOr5A7UyX3yCph9b3HrV1i41uUYPWk0tpZTxcTttbA6-AxoXo6a-er-HgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b486c4e528.mp4?token=gvlmaKNTLkRBBqNqZPuDsGyA8qcN19O3_2Y43lbZt4hcOBsnZn7hpexLyCXTZ-yMUnRvvGrwC1kqHMu3QXBD9OXjtv2geIB40zCNDr5OYkJ_u4Of0pCN0Pg8ByyDGJQRm6GAr_QhByeRCVa5suaoEXtZaT2msc9R8ZR-GkXerGPPZwyTg6kHzKkwd6vZLltRW2RGG-z9uT75sELpPj4rtVYUlwCTridEz8Zb2CAD7w_vK43QOd5MKGWdH2zv2_A1TRt77MY1zCl5wKSiRpGi89y7aUjmzOr5A7UyX3yCph9b3HrV1i41uUYPWk0tpZTxcTttbA6-AxoXo6a-er-HgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🎙
🔴
🔵
تاجرنیا: «ما و تراکتور، بصره را به خاطر نزدیک بودن به مرز، به عنوان ورزشگاه میزبان انتخاب کرده‌ایم.»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/Futball180TV/102368" target="_blank">📅 19:56 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102366">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/twbj8Qcno1G2h7myFH18lTgtNI49cgS0Kh3q4lpFYYYp-RwU2lLS2M_rwj8TjW018v1OQ6OOLNiTzM7zVD3N7GbZP4cnB_g7IL8vvv2MaG-yu_afN7PnclQOHP7EblP4NCDLBNgXIsk5C6wDBUIpDc2ZYnNqGUbBKmlL6LgoJ_3_RnMf387CQW4bI8nY2lbUAb7SfpLRrB17ZVD15WYrI6cAKpzotIs8lX_hiRlv-yfPejOM5ffaU593hktoZAT0H1LJjdN1-6lZd5Urrgq8SiKddsic1JbPPwP2Q6fDzu3hv6rCez9xybJ10BFZDpqb98A1J-j8J6IDmZ4G_S5wTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🤩
✅
تیم‌فوتبال پرسپولیس در دومین بازی تدارکاتی در اردوی ترکیه مقابل آلانیا اسپور این کشور با تک‌گل علی‌علیپور به برتری دست‌یافت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/Futball180TV/102366" target="_blank">📅 19:29 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102364">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u4TNSLgZLMJqFQfW6s5X0CHdq9e-MkeiCuTga013jUPdjz49rb2q42CgbuuLvIYEAX6n4Cm5p8jj8tOtD3l7jaT0rl-WBXXFN62GJKCJGCiyGGeOUkDGu_z0GWcK6N9Vzc8nw3MX2Q6Eo5ZT70Opom_nKj7Lspm_jha_hjO70hS1AU8u4ix5LeRvgtJR3wetlXrFP5bZ-D9TXqemx_SNp2GhNzWbQ_SsyjnNOaRmNAhGA7xsv2FJQGa_Ns_ctKufORQRYKOOpOvX9VloiLhepPCVVansIi6ERkfxas7WHlhfuIgaXECL13K2POf8HBw6t4TortjeMKjz6nm5g_2FBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08c0c36c9e.mp4?token=pALmXJsoFhQJm7nPNJXFinh1cmmLK2Me1yzTba-Bm9Cw7pJvOxcS7JaLVhwBFrWMJNK5STsIU06T9CySUdbuf9Md3hTj4MQvjz9wn3dOWx6lKv1F-YaC_uNjiV8BwGw2xmYhRZTsnX0353bcNgJ74rlgwEk6Ol_PJCEPc3x0r0IOaKCSVr8LCw0CY8GuLq0PYRfnBEJ4OsNezm96QpMFO-jKHOxHM2L30mAtqfqcEuveGtZnt7CEyRsJoElZP35m4Iy4uaN-cjtyY1SEtAqyDxFiW0c6yEz5oGI42GXFtbLTxqeo59dlxZ5H-SP4dKBFQLBoXJIS0SB1je2OIhEFPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08c0c36c9e.mp4?token=pALmXJsoFhQJm7nPNJXFinh1cmmLK2Me1yzTba-Bm9Cw7pJvOxcS7JaLVhwBFrWMJNK5STsIU06T9CySUdbuf9Md3hTj4MQvjz9wn3dOWx6lKv1F-YaC_uNjiV8BwGw2xmYhRZTsnX0353bcNgJ74rlgwEk6Ol_PJCEPc3x0r0IOaKCSVr8LCw0CY8GuLq0PYRfnBEJ4OsNezm96QpMFO-jKHOxHM2L30mAtqfqcEuveGtZnt7CEyRsJoElZP35m4Iy4uaN-cjtyY1SEtAqyDxFiW0c6yEz5oGI42GXFtbLTxqeo59dlxZ5H-SP4dKBFQLBoXJIS0SB1je2OIhEFPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
اولیسه درحال لذت بردن از تعطیلات
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/102364" target="_blank">📅 19:20 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102362">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V_YAfeGmFo-Ud2AAQ3fVICA7t3ZMSNxLyPDBvlWrOvZKUcukQ9KGgSWnAOv9x9tieQpf6eR41uIaAHOCzoHrFQXdK6Yh7g5WqmtmolRyIuolMQzweZX00IG28MxzFeJJLGgqADPCn83Of48-nFDlyDWwxoRlLEtT8gyceAAVcTS075cPWuULycrcYlpCJOdVoEYmw7_n251t1lEXoA8ohM1_eL7Rl9OR_BKcvXix2qUiDLwNmEoxgIDbLb7ezVHsg86fsLoRVtFTcQ5lY0haG2larEb3eB3Rczyc3L3_a94GNO6aWDJ6el8Sl_FzbQlwt_Qz3UL5kmYyFa3_XOC85A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3645ae0183.mp4?token=fIxgOOl64xp-yCY0rRGnKPeCePBiL6udxAkqpk1Knqm699srdqBnRO9EzAlGeFa9rbejmRFkuqrzMfFS11yxjhrIPmgc_A97GGlG8J1Lu-N8kE_yuH7ED65NcQax3766Fz-KrqXcs-_DyazlsAS5rWY5TqDu6IdUgY9SNMHZWrKljEIqjBu80W8qKXgDMdsgXRdaFdYLsGlhBB_Fki8JY43HhPFm2Sa2145SOkTZsAG-XgB4JV_u0odCC9vjICc3Urf3pOmDa7i0BPO-epeGWODOkhePHFnOFn4rLjGi282LqGOKgyD8h-L03iSsI8loIxfFZzPI6D9-k9QWmPB-Vw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3645ae0183.mp4?token=fIxgOOl64xp-yCY0rRGnKPeCePBiL6udxAkqpk1Knqm699srdqBnRO9EzAlGeFa9rbejmRFkuqrzMfFS11yxjhrIPmgc_A97GGlG8J1Lu-N8kE_yuH7ED65NcQax3766Fz-KrqXcs-_DyazlsAS5rWY5TqDu6IdUgY9SNMHZWrKljEIqjBu80W8qKXgDMdsgXRdaFdYLsGlhBB_Fki8JY43HhPFm2Sa2145SOkTZsAG-XgB4JV_u0odCC9vjICc3Urf3pOmDa7i0BPO-epeGWODOkhePHFnOFn4rLjGi282LqGOKgyD8h-L03iSsI8loIxfFZzPI6D9-k9QWmPB-Vw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
نیکی نیکول، رپر آرژانتینی و دوست‌دختر سابق لامین یامال، در مصاحبه‌ای مدعی شد که رابطه‌اش با ستاره بارسلونا فقط برای بیشتر دیده شدن بوده:
راستش باید اینو اعتراف کنم. مهم نیست وایرال بشه یا با واکنش منفی روبه‌رو بشم؛ من سال گذشته فقط با لامین وارد رابطه شدم چون می‌خواستم اسمم بیشتر دیده بشه و به کار موسیقی‌ام کمک کنه. با این حال برای اون خوشحالم و امیدوارم اینس مثل من ازش استفاده نکنه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/102362" target="_blank">📅 19:01 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102360">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Os49vwLRtkfODRLUuPaXnDiMMc4U3FR5mFfMGDbS-YI5Imo8uDO9C3AkTMxRXZ2vBUuClRZaWA6b1aqIRNtqO-jr-GvUbfRDsfct67FFUWg4Z12WvnNaSYdA16ZSo6cDRK2gSc63vyasmH7wkJF4efADRQrPVXoXdMFM5nIIc2dxTW-P9pXDmZxbsE868Lq9YwWK5xxSMAhloHxzPz8AYmgbp4tOGloCxJH73vOw0mAdk6UvIx1rZVEa5bt3XCZKtUFrpf641Jy-dWtPJYmTxRXtauXbtm6GE2MYuSPX4L_-cgaSo5zBiWYJs5iOO1yDBHpOynT34NjenMmjgVcDRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TC7Fmi9l_0VNRcm88mwN99u-NDqWmQ65vjp7t2I2xQr3tuxaMXxQEpqQsuiu1nUyJtospw94Vq6-zD3p_EEOTuDn2AzhaBpkEolDltgrsEc_wP9EMTAM4fSngvSGyxcAnShbQZjR-ZSVnryrK4MNgSGaT1G2eId2wRdhBj8nQGPfs_Rr035S6Fb0mUmxuIgVg_zyQ203wVK3H9JKg01qNVe_qshB8fJSXaZV8sT0cgNbUjaP1vijGB-N-wgeW2tnENKrZdNwEXe5X5X0TUZ_AMsYU2QnHoJRmaiGFyW4tW6oOrq2OZCrZ2UopfRTv9lvCi2Fto_xvrhtfTY0C7ZWTw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🇦🇷
طبق گزارش‌ها، لیساندرو مارتینز و الکسیس مک‌آلیستر بعد از پیروزی آرژانتین مقابل انگلیس در جام جهانی، برای خانه‌هایشان در انگلیس نیروی امنیتی خصوصی گرفتن. گفته میشه بعد از حواشی جشن پیروزی و نمایش یک بنر جنجالی درباره جزایر فالکلند، به خاطر بالا بودن احساسات و احتمال واکنش هواداران انگلیسی، برای چند روز مراقبت امنیتی در نظر گرفتند. البته گزارشی از حمله یا خرابکاری علیه خانه‌های آنها منتشر نشده و این فقط یک اقدام احتیاطی بوده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/102360" target="_blank">📅 18:40 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102358">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qioeAFGCmr43hIjwkAAYpo4e0QRN1qnr8saIZchHOG3hGf0tbanzGW6suGQF81XcfCcNMrIor9skYcy3J-dOvqiyOKf9zllt2iR_s_EIRvaJCzOfOeKT9dUK65rWUOI2mzpwez3Pox_psOyy_OYJvmf5qLOwFBKbaJNxq2TVgdU5LxeCFOh5PfMFFk_CcUCn5PByenH-y7-QkJd-Zp56CGxWhYjZXEsxuXuzHUZGydDB5yRE60lX_k0drVAbD8kU7cIRjIJ9lIArmyffaAlU0swBjIl_R3Lru68RUCzaB7kctTISS32pB63YEbppcQNMc2JLJIRCELYuU877assmqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KVOySIM7dSpifNFGY4NgutTpUsSD5f7wcSgZofOkalcdHTjzzBLOpDskAT-gBzImq6cH57H0SuBWsKG9Wk1kW0ZzCEh0LTLyccwGf_3_73tEx3BwVhO-pAAJXdAqan1oV_VBvT-fSiuT6sWv0SokUvEzlUOd_8VqpR1w70BQwTnifVmexmmJ8RZ-9xksJw5rwKNWs3aQZwgXExCEBtKizIMNn24Mv1YWd_hiWHlaWqgHfE2sxKm68J7qbd22kBX-SRpSqyDZEwCpRbUvnRem0zP62VsSZNDNcxjsyYnhEqJ8DZ7t8EBMHUPcdHvNQxNSWwRHyUb_GYd1TEXxtR8Yxg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
نیکو ویلیامز و دوست‌دخترش آینهی گارسیا جدایی‌شون رو اعلام کردن. طبق ادعاهای منتشرشده، گفته میشه آینهی نیکو رو در ایبیزا و روی یک قایق در حالی دیده که مست بوده و کنار سه دختر دیگه حضور داشته. بعد از این اتفاق هم وسایلش رو جمع کرده و جزیره رو ترک کرده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/102358" target="_blank">📅 18:20 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102357">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14e33cfddb.mp4?token=r846RRxNOJ2n9NnaWpQd7LqS1n61mIs4SvRn4Ur9KLFcP_I3IL0AOsbZQr-dS_wRsBtl4ksJvbAD1-QblxiRvrQcKwMgEqOCSllyfVzUx2ZGh2UQuERsUWKpXghVqLrgKNL8RXP8pFJsrsx-e3SNE0g-E4QtPDRl54EhGDUhbLVf8LEPRqe5dU-aAGF95kLdYp1ePEMlxNCto2pGSZa0X-NnSmrXSXHa4KQWSGDNNMPY-t8T8z_XwOGZxAwjs1PFYVcSXqhoyw-AW2sNsZxJXmzB6MEqsz0FFG32yJZwKs3HjjUYQcpZDXe8cDBGTaQ4K4amSSChn6a3gaDLOGeMwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14e33cfddb.mp4?token=r846RRxNOJ2n9NnaWpQd7LqS1n61mIs4SvRn4Ur9KLFcP_I3IL0AOsbZQr-dS_wRsBtl4ksJvbAD1-QblxiRvrQcKwMgEqOCSllyfVzUx2ZGh2UQuERsUWKpXghVqLrgKNL8RXP8pFJsrsx-e3SNE0g-E4QtPDRl54EhGDUhbLVf8LEPRqe5dU-aAGF95kLdYp1ePEMlxNCto2pGSZa0X-NnSmrXSXHa4KQWSGDNNMPY-t8T8z_XwOGZxAwjs1PFYVcSXqhoyw-AW2sNsZxJXmzB6MEqsz0FFG32yJZwKs3HjjUYQcpZDXe8cDBGTaQ4K4amSSChn6a3gaDLOGeMwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شوخی ترامپ‌نادان با بازیکن غول‌پیگر فوتبال آمریکایی؛ بعدش که مزه میریزه از اتاقش بیرونشون میکنه
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/102357" target="_blank">📅 18:04 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102356">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff5a8032cf.mp4?token=cxc2Y7IZVKD1K96uH_t8cAjyhb7laM_kH24CuBalgVmw4US8CEb7wkjZAg1iMQ22_cU9FfseT92eGqFSiCsoC5SHaQprq_smxqtvbo99C4hccM80O5X8XLzDJoUZOtGTVXkuPvX6Ke8dstJppD7_PXl2iL763xo1q1FaisD-Qsm4dDtBCXh-a6WhOed_7QtA9jfnSlnPUttPOwfEjaRMueWrLfGCfhwfEgvHrLl0o9biw8fdvO8IGiLddDM85ISBSvXGyXd1M-l5YsHZ-3IJBXkPnUb5A3eVlxpDyPqaP4YTnnHC3NBxU25s2QmhKfqzHoOvkC9yMyGTfhcs8JxhVlERt0wexE-D7n0JTpWBATsL5uHVZu4ia6cpdAa7IJnKpGW4VdBxKm13ObM8lqV_mMfPU7ZtGZkD2h7rQ85ZTR8jey4IuSd7QgJDooUqiBAxrdOhywxrPDD76tt3r0TJBcjUmRDENO8ZAu_cH-Fav0QSMeV2u61SO8Y3lwjak2_0WjkLZpSinYxaDKmjzXEHC92NHoW8rcR2mpzz6A2qHWXwU0nHlZeHTRVqxBnsUGOsTFN6WAgiYJ5k4KIOy9YeQ2mlrWc267YsmycV4shYB8ZeDeOU5BmwFVSCwx9Vd7YuQ3ck878jccXT692AfOtXMvxvp2Q3831R4tIsKG0WeYc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff5a8032cf.mp4?token=cxc2Y7IZVKD1K96uH_t8cAjyhb7laM_kH24CuBalgVmw4US8CEb7wkjZAg1iMQ22_cU9FfseT92eGqFSiCsoC5SHaQprq_smxqtvbo99C4hccM80O5X8XLzDJoUZOtGTVXkuPvX6Ke8dstJppD7_PXl2iL763xo1q1FaisD-Qsm4dDtBCXh-a6WhOed_7QtA9jfnSlnPUttPOwfEjaRMueWrLfGCfhwfEgvHrLl0o9biw8fdvO8IGiLddDM85ISBSvXGyXd1M-l5YsHZ-3IJBXkPnUb5A3eVlxpDyPqaP4YTnnHC3NBxU25s2QmhKfqzHoOvkC9yMyGTfhcs8JxhVlERt0wexE-D7n0JTpWBATsL5uHVZu4ia6cpdAa7IJnKpGW4VdBxKm13ObM8lqV_mMfPU7ZtGZkD2h7rQ85ZTR8jey4IuSd7QgJDooUqiBAxrdOhywxrPDD76tt3r0TJBcjUmRDENO8ZAu_cH-Fav0QSMeV2u61SO8Y3lwjak2_0WjkLZpSinYxaDKmjzXEHC92NHoW8rcR2mpzz6A2qHWXwU0nHlZeHTRVqxBnsUGOsTFN6WAgiYJ5k4KIOy9YeQ2mlrWc267YsmycV4shYB8ZeDeOU5BmwFVSCwx9Vd7YuQ3ck878jccXT692AfOtXMvxvp2Q3831R4tIsKG0WeYc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✨
یادی‌کنیم از کینگ‌کمالی از اساطیر بدنسازی ایران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/102356" target="_blank">📅 17:40 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102355">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69a15854e8.mp4?token=LbItQK7bb4HW9rw31vp-Fo_4h_YlPPCYE2UUXUTVNLH2WAIH-5e1s1GlwTRNnIkZF-3lOe6horXImT4I_MGNyk-qHLG6i1n-skJeyLzPaZLcYkEn1_2YbodRBQB-zp5stc6WcLoSUkA3yZt98CM9FqbR4tI1zJlvX7AUZvNjW2e0IDfd5W_g5c3GznPF8FsH2K8XcnoaK0YtFx28fP3HLD5eRueNLcovI5VVrLYUiFz6tm-_PTSBYIXMXcR-E01F_S0HvHTOKM3CDPGe6R89lORZGluAG9TFG_y03ssd2r4gXjfu5xXxKll3JyvmBRqWF9Apcp_8JlF7U5cJqeVW9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69a15854e8.mp4?token=LbItQK7bb4HW9rw31vp-Fo_4h_YlPPCYE2UUXUTVNLH2WAIH-5e1s1GlwTRNnIkZF-3lOe6horXImT4I_MGNyk-qHLG6i1n-skJeyLzPaZLcYkEn1_2YbodRBQB-zp5stc6WcLoSUkA3yZt98CM9FqbR4tI1zJlvX7AUZvNjW2e0IDfd5W_g5c3GznPF8FsH2K8XcnoaK0YtFx28fP3HLD5eRueNLcovI5VVrLYUiFz6tm-_PTSBYIXMXcR-E01F_S0HvHTOKM3CDPGe6R89lORZGluAG9TFG_y03ssd2r4gXjfu5xXxKll3JyvmBRqWF9Apcp_8JlF7U5cJqeVW9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
🇪🇸
وضعیت این‌روزهای هانسی‌فلیک در بارسلونا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/102355" target="_blank">📅 17:27 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102354">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/262bb95a39.mp4?token=dxevt1ZukvxseBOwuYWb4jwnEwKMNDVaLrIWeCXevlvzsNCfmRfojWgYohAd-mOueDriLo8I0J9nM97Vzh30GMtDBpzzOUFloMVZFkuCiIonmstxQ9Le3dd7N57CymdgEv7wyhxW-J0vKkajv48IuCv-XSrtVf1Q9CrxOoiYf70vQc8T-il9nsI9ipsgtO9NzUGISl3jFi9MW5HiaWynWDKROSZnWgqMsJdDIcWOyF_5kJnBfp-XwdwUboOCc-xxmawlZfIgbkGmQdQHCKX_IODpXpSt467bn0-VNqfjILxQ8PpMfiDIB8xFBAzNmMDiz0Hxbt_v4jbWvUXs49wvNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/262bb95a39.mp4?token=dxevt1ZukvxseBOwuYWb4jwnEwKMNDVaLrIWeCXevlvzsNCfmRfojWgYohAd-mOueDriLo8I0J9nM97Vzh30GMtDBpzzOUFloMVZFkuCiIonmstxQ9Le3dd7N57CymdgEv7wyhxW-J0vKkajv48IuCv-XSrtVf1Q9CrxOoiYf70vQc8T-il9nsI9ipsgtO9NzUGISl3jFi9MW5HiaWynWDKROSZnWgqMsJdDIcWOyF_5kJnBfp-XwdwUboOCc-xxmawlZfIgbkGmQdQHCKX_IODpXpSt467bn0-VNqfjILxQ8PpMfiDIB8xFBAzNmMDiz0Hxbt_v4jbWvUXs49wvNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
‌‌ ‌ ‌ یه ویدیوی وحشتناک ۱۰ دقیقه‌ای از
این حرومزاده منتشر شده
🔗
🔞
مشاهده ویدیوی کامل</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/102354" target="_blank">📅 17:23 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102353">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T-o5CHhYbX86xGweWLc5_XPwJLDzWf80wYqf_nDu-2wk9tzdIrdiF2Mb2IUnAfQudD6KaNsH8QQisUkmBhoqKLoLqxPmWD0Rb-Lg0sr9-bNvSQjhFKzLeUL7hmnhUsdunBpp6_l67K9Fd1pY6MOhcuofY5uf9TUkQhXwpwejVHCoKVSqWJ7LKB-DMcmqPfl5JCJQGRxvPZIpU0js7M7xhGO-szB43SEXaqWncOTqadCNr2i1v0blNzHtDY4OCbQNrsHWf19FfKwP4rXfUmM2JmrUrX6NKdaf5uneTOry7OM7NKydOpw6Dm4XTV_XJlSgAj2-1f2UOKG6wBrO4tErKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
🗞
رئال مادرید، پیشنهاد رسمی ۵۱ میلیون پوند برای جذب رودری از منچسترسیتی ارائه کرده است.
❌
🏴󠁧󠁢󠁥󠁮󠁧󠁿
منچسترسیتی قصد فروش او را ندارد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/102353" target="_blank">📅 16:58 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102352">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17f25fd06c.mp4?token=q5p3FiAVMmCOzxCiwwP8Z4aTw5ouBR0IXV14IRMcN8h0gaBUfRcosZMteVBs6X50db4CeHJe8gdAbFTLeW3jTkWdXVWMY6KMG4QPxh_1tf3r-JastFqNvvjL0T15UCGGS5LOYXDsxvkZ31eINA_3iTjiMtI7JZAIW-5ATXptS2ZZU3tXLWVW9yZGKz22M4iElZdGs_L7JQgVPAJN9Aedc6-hNpB0khAKsGePIpDX3j_sfOfrqL_CH8NoNrhnnajtZAb1d2DVguEBMqbmLp8MZkZ6Xwm72Mye1js5RAUxv-Y5vz55uU4yJX7iR0oxDrj5t53DrTh7hcnQtVfwNmlQV07ztEMWgYs9LuCW-Uh_bJn_RR7TrGbuUPPQji4Ci-2QvemPrMXBN3b4m_aZjY_n-NTlGhvd_BI3_UIzLUaVpftCcwjBVW_bW4dsbUX1DEKD733autYBxbIi4PUzE-etg7ZDCuXgy3HmQM9QR3ujvt5qs-5j1gMxHRbzTvAgavbuaVEl-Stp1-jq7txPYxERbbVtyiOEgy4ctiKq5HR5GxO5UJPg-sxmAENOAydc0GtDcwMyX-Gs7m7vcaO8dEtABKFLMLvIKBmPBnQl_mShCCssG3o_nkId-JoCYKBq9d76v3LwRvHU2i97eODbl3ea_l-pepMqZ4LafdHLBbKtScc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17f25fd06c.mp4?token=q5p3FiAVMmCOzxCiwwP8Z4aTw5ouBR0IXV14IRMcN8h0gaBUfRcosZMteVBs6X50db4CeHJe8gdAbFTLeW3jTkWdXVWMY6KMG4QPxh_1tf3r-JastFqNvvjL0T15UCGGS5LOYXDsxvkZ31eINA_3iTjiMtI7JZAIW-5ATXptS2ZZU3tXLWVW9yZGKz22M4iElZdGs_L7JQgVPAJN9Aedc6-hNpB0khAKsGePIpDX3j_sfOfrqL_CH8NoNrhnnajtZAb1d2DVguEBMqbmLp8MZkZ6Xwm72Mye1js5RAUxv-Y5vz55uU4yJX7iR0oxDrj5t53DrTh7hcnQtVfwNmlQV07ztEMWgYs9LuCW-Uh_bJn_RR7TrGbuUPPQji4Ci-2QvemPrMXBN3b4m_aZjY_n-NTlGhvd_BI3_UIzLUaVpftCcwjBVW_bW4dsbUX1DEKD733autYBxbIi4PUzE-etg7ZDCuXgy3HmQM9QR3ujvt5qs-5j1gMxHRbzTvAgavbuaVEl-Stp1-jq7txPYxERbbVtyiOEgy4ctiKq5HR5GxO5UJPg-sxmAENOAydc0GtDcwMyX-Gs7m7vcaO8dEtABKFLMLvIKBmPBnQl_mShCCssG3o_nkId-JoCYKBq9d76v3LwRvHU2i97eODbl3ea_l-pepMqZ4LafdHLBbKtScc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
مملکت به شدت عجیب و غریبی داریم
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/102352" target="_blank">📅 16:39 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102351">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/138f735fee.mp4?token=YVATD0qsXa0hmheDqFYmB1fNlV8VaHW4WkHxXLBiYBO6D7EYnciE8MV56kJdo-Q5QFcf3YbYJBWnh0CxmBJihII8RwFSR1CIYqUdKE5hvbMfboCeSHR4yLXcVCISnk-iLeEcpmx-VxG8SKUnS9vPSCxWIvmqcYvya4IksLx-fjbkymYnyfdA3GiXf9eTPW2V50bqkKT2E29hVhhA3ibpDGx3NYNH86hWV44-ESD3usr0Hgr-rxm8RKEnR6Mv1xxwPNr6R_-Z5OLy1mCGSZh5bjKKSs6CWHR7FlbsR0nyWxwy_ST-RPzJnIZ-MBNVMUFQfVn6dHkLIVUiEi8asA6MoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/138f735fee.mp4?token=YVATD0qsXa0hmheDqFYmB1fNlV8VaHW4WkHxXLBiYBO6D7EYnciE8MV56kJdo-Q5QFcf3YbYJBWnh0CxmBJihII8RwFSR1CIYqUdKE5hvbMfboCeSHR4yLXcVCISnk-iLeEcpmx-VxG8SKUnS9vPSCxWIvmqcYvya4IksLx-fjbkymYnyfdA3GiXf9eTPW2V50bqkKT2E29hVhhA3ibpDGx3NYNH86hWV44-ESD3usr0Hgr-rxm8RKEnR6Mv1xxwPNr6R_-Z5OLy1mCGSZh5bjKKSs6CWHR7FlbsR0nyWxwy_ST-RPzJnIZ-MBNVMUFQfVn6dHkLIVUiEi8asA6MoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🎙
برترین‌های تاریخ از زبان رودری ستاره اسپانیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/102351" target="_blank">📅 16:20 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102350">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🇪🇺
🇪🇸
یادی‌کنیم از آخرین قهرمانی بارسلونا در اروپا با مثلث تاریخی کاتالان‌ها در خط‌حمله
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/102350" target="_blank">📅 16:00 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102349">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RNkBcnpsFMIWA8M8sxuxU-sDFMIxL8K1pqZx-qj5wSNNIeEVG--aLzvtSbVWk3SFOHjmbF2Sm_KJP8gp0Ed0SNEtMcg3HO54Lgew67ZPfuQG_QrQQtSBu0M2kFrjtzTlY47_sxt6f9XpFQywg7Se7UfdRiFDe53S62OxL7qkg-93KCuPgFOdxVTOxDdFmas2dwpIXSAWSaXSMF09lI8xvO57yUJPyGoaAhz-ktv76xjLwozHpeqJsrIUkI80g2lbqGg_XeBj_J4wnqm0O3IXRafDchrhylvMfE59NtB2867yWC2TtiWipcvL8ARZm_6Gse2NneWymnM34WMWGNAj4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
گونزالو گارسیا به فولام پیوست
۴۰ میلیون یورو
۲ میلیون بند پاداشی
۳۰٪ از فروش بعدی به رئال مادرید میرسد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/102349" target="_blank">📅 15:45 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102348">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d88e7b9804.mp4?token=Cdv6_kGuapdAjf9Co-I74z5T5UG_9guMcBmF4Ph9bc7HCMHxtdSr2FotNaKaPuki0IVeWJekTeWKuXI7zD-dTt6toPOXL4qSMD9Z-jbIbZPfvKZUdF9Qa-A6GroW1TIPgxeOzGi0EiK1RTjEjouFTs4-DpMKjNUyA1lc5FBLataS4K2T-tycZ_VFuuggWrnmBOVm-RZHT9nOEZgpZkiLH-8k0HqEkP9NECGHmpK5yKSYJW2SPK_4ogaKDP385SCjWzAphwEwl373qkOYUmamLpxuNYqF7Q_s3LW4yYc1Tpq-XcyG-bEuDPuiq4MG4m1pCHja3s9SvmbXm8FOC-n7AQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d88e7b9804.mp4?token=Cdv6_kGuapdAjf9Co-I74z5T5UG_9guMcBmF4Ph9bc7HCMHxtdSr2FotNaKaPuki0IVeWJekTeWKuXI7zD-dTt6toPOXL4qSMD9Z-jbIbZPfvKZUdF9Qa-A6GroW1TIPgxeOzGi0EiK1RTjEjouFTs4-DpMKjNUyA1lc5FBLataS4K2T-tycZ_VFuuggWrnmBOVm-RZHT9nOEZgpZkiLH-8k0HqEkP9NECGHmpK5yKSYJW2SPK_4ogaKDP385SCjWzAphwEwl373qkOYUmamLpxuNYqF7Q_s3LW4yYc1Tpq-XcyG-bEuDPuiq4MG4m1pCHja3s9SvmbXm8FOC-n7AQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
💥
حالا که بحث تیم‌ملی داغ شده، این تیم‌ملی و بازیکنانش بنظر از همه سر تر بودن :)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/102348" target="_blank">📅 15:40 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102347">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0063915b2d.mp4?token=htdxodQ7Ond_EhzaDNJef6_MXNhT5Ckk-5z7lGtmuL1rSrLnHD2pnIjAw67nXPPpA0bTkQrTPDrhZEaRlmp3PK-T7MBJY59MY3tH1ef9mATYFUGuUxib3byzvFaGB5eWPL8sHAnfaDweC8tvTbz-YHf81ronh8c03iA0u5O3yXzd4M1hAf1DLm5I98d6Ub3ti7g9MoZMn-9QbgI7MFiZcgIloFiXx-gYJDMeMQPGKtMYsU7ya7n5_D5niviKbxUkHqoYNaYBImwM-6IFymXqasfyo00RxWUyUzJIaM_AY5WXL_JTd3eGevYiIL65sXvTy_boucEfobxW1XTXpCYC_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0063915b2d.mp4?token=htdxodQ7Ond_EhzaDNJef6_MXNhT5Ckk-5z7lGtmuL1rSrLnHD2pnIjAw67nXPPpA0bTkQrTPDrhZEaRlmp3PK-T7MBJY59MY3tH1ef9mATYFUGuUxib3byzvFaGB5eWPL8sHAnfaDweC8tvTbz-YHf81ronh8c03iA0u5O3yXzd4M1hAf1DLm5I98d6Ub3ti7g9MoZMn-9QbgI7MFiZcgIloFiXx-gYJDMeMQPGKtMYsU7ya7n5_D5niviKbxUkHqoYNaYBImwM-6IFymXqasfyo00RxWUyUzJIaM_AY5WXL_JTd3eGevYiIL65sXvTy_boucEfobxW1XTXpCYC_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خاطره‌بامزه از زبان فیروز کریمی
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/102347" target="_blank">📅 15:20 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102346">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2314f18179.mp4?token=Y0l1LHU_5B-KrqgK-krqoohGFbjINvSw9c1PW7LXoLfZNv_ahe0gdQIhBOrBbldMXxmXngQ_fje7xb1NATKhLe8HgeM4vO2PeknmFI-NShqj2Kz8-s30ftZa8-2QMwFb80raV2bgXmmp1g6gFlSl_kqN5v9otrs6ZJv4D0cBNwZQYKVavrG9cLnGFuNDLusz_o-Cf4jXwAmbOJeQLmnq5X3f9cyYcapvqC93wkZ-VLjrIF6WWedRc9YbiaQFvmed2O8sydZHmm1G2ue1iTCFb2aROwLGBNUbM8N98KY94_J047_08ByGPUu2AtIOdzZJUA2FC7d-J16LcS7OvfQkdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2314f18179.mp4?token=Y0l1LHU_5B-KrqgK-krqoohGFbjINvSw9c1PW7LXoLfZNv_ahe0gdQIhBOrBbldMXxmXngQ_fje7xb1NATKhLe8HgeM4vO2PeknmFI-NShqj2Kz8-s30ftZa8-2QMwFb80raV2bgXmmp1g6gFlSl_kqN5v9otrs6ZJv4D0cBNwZQYKVavrG9cLnGFuNDLusz_o-Cf4jXwAmbOJeQLmnq5X3f9cyYcapvqC93wkZ-VLjrIF6WWedRc9YbiaQFvmed2O8sydZHmm1G2ue1iTCFb2aROwLGBNUbM8N98KY94_J047_08ByGPUu2AtIOdzZJUA2FC7d-J16LcS7OvfQkdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
⚠️
تمرینات پیش‌فصل بادیگارد لیونل‌مسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/102346" target="_blank">📅 15:04 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102345">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🇪🇸
🔥
۵ گل زیبا در تاریخ باشگاه بارسلونا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/102345" target="_blank">📅 14:40 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102344">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1e80cceff6.mp4?token=VXdTNGR-QbuOIeXwd_XjfpTSNSFtTzBN-ardi1DLLY_TeTa4a4b2kDcEPt15dzm4bb0ARvfMAiye4ygHtFUpnXkARCyunlCcSf0k84uEuXqPY3eZbdbHrC-CI6mGacZ5IJAXLWUCCXlZI73J55P1oyvzSdErry-ProPNou5D9BnKt3E5m0mIw4ycsGR57d70vPnp18hKO4WGeqQXf0cojas1iPmFJWk9jvcHdtGcK-VL2pJyY-tB4dxmnv92VAKeDlmAPvi8ALY0l92ZuU5yYfL02cXq88DddENSQakNvj2vlYZIqPqsCclEjgH_6QDoFiCEHiPjcPk8yartDcFueW8-vG9kPhogkeElvU-wQp0kbmYdiNYthPwYxFp1gq9NhNbQ-OvxRdAOgUMvnvWvDsL2WHOglmi-br-HTixXxvF4NMqEQU5Xbc17fA58mcsv7KKm75oL7DCwt-9CH-SXimip94koWIWlHe95tREPqbYO4IAzMbbEEsYP_GwLNUSAOop_wPv6v_6PFLLuVUPxG5wTIIz6vLwRFKERT32Y-JTTexQiZP5Rm1xmtnXvTT77CHiAI9FdAXGEL38E18uGB4Y5UGOfuYevmUqMBLi0JA_XsFSKfoLsGasHgQU-TGXHPKiZeoYiBHuMnRdrm9X6iAW2yomG7NOSG_KAVI0JNPk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1e80cceff6.mp4?token=VXdTNGR-QbuOIeXwd_XjfpTSNSFtTzBN-ardi1DLLY_TeTa4a4b2kDcEPt15dzm4bb0ARvfMAiye4ygHtFUpnXkARCyunlCcSf0k84uEuXqPY3eZbdbHrC-CI6mGacZ5IJAXLWUCCXlZI73J55P1oyvzSdErry-ProPNou5D9BnKt3E5m0mIw4ycsGR57d70vPnp18hKO4WGeqQXf0cojas1iPmFJWk9jvcHdtGcK-VL2pJyY-tB4dxmnv92VAKeDlmAPvi8ALY0l92ZuU5yYfL02cXq88DddENSQakNvj2vlYZIqPqsCclEjgH_6QDoFiCEHiPjcPk8yartDcFueW8-vG9kPhogkeElvU-wQp0kbmYdiNYthPwYxFp1gq9NhNbQ-OvxRdAOgUMvnvWvDsL2WHOglmi-br-HTixXxvF4NMqEQU5Xbc17fA58mcsv7KKm75oL7DCwt-9CH-SXimip94koWIWlHe95tREPqbYO4IAzMbbEEsYP_GwLNUSAOop_wPv6v_6PFLLuVUPxG5wTIIz6vLwRFKERT32Y-JTTexQiZP5Rm1xmtnXvTT77CHiAI9FdAXGEL38E18uGB4Y5UGOfuYevmUqMBLi0JA_XsFSKfoLsGasHgQU-TGXHPKiZeoYiBHuMnRdrm9X6iAW2yomG7NOSG_KAVI0JNPk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
فرشاد محمدی‌مرام درتست گزارشگری سال ۱۳۹۴
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/102344" target="_blank">📅 14:20 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102343">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ufPyxDRehTWkskIZi-vuvgp_uVzAK04wEKPnR2E_L1GsjmXvLly894zm22CLFJkCcIgCjrTaZ-EIF-vaEFi_Y6QWS_QcRFthw7nVc4dYYpaorBIHYDs-7X3jbv7lLpp-o5VPvN98WDcgIlAwnDJHdtDEK6DmzB0LRZxiEjR7QE3MQ9uyxpTWnfYXRz7H5FvzDrhRJbS1FBV3rIebEpGGcQTZL_tuXaQPM0MDprDYV2WW7EM8YEisb8f5gvtnPICc2lTp7tG6O_5mpCk-jLy6eJLPrtIhz9nwTe2plYGlfN5IFLaL8teoPZnyxMBPhhixTSHZ_iERR2UXDNq8TCXDTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
🔹
رسمی؛ نیو راموس مصدوم شد و حدودا یه ماه و نیم از میادین دوره‌.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/102343" target="_blank">📅 14:16 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102342">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3336c43202.mp4?token=tedZgQiw5LaANkpOd3dMX2fDv2seWXHOZMq_Uf6-K82M1NeIKXdjXlSxsEmBOCY-V89okzBLgNrHJlKyIs_zz4MRNaBiLMKpP7WEf0jVlmtNeyb1dRSh7CoDeAmRHW-ZNVoWAvMXp-79LXHvNLdO_fptQrvjy2e0lMWevolWFKSqQTdRSI31sHK8hpLb33qfC61U-wEC-gRJ5vrtACJQCD0_aMt-WWZiqPOnThMV4HNDSbCNJaHSfN5oO-tE5HzYtFGioMRb2Yby_6vaf62phGe0TChjH0OzE8Wbg9eig9RfgKsKriSibo94B2h_PKduisdoUPQh95E4knheMZV-uA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3336c43202.mp4?token=tedZgQiw5LaANkpOd3dMX2fDv2seWXHOZMq_Uf6-K82M1NeIKXdjXlSxsEmBOCY-V89okzBLgNrHJlKyIs_zz4MRNaBiLMKpP7WEf0jVlmtNeyb1dRSh7CoDeAmRHW-ZNVoWAvMXp-79LXHvNLdO_fptQrvjy2e0lMWevolWFKSqQTdRSI31sHK8hpLb33qfC61U-wEC-gRJ5vrtACJQCD0_aMt-WWZiqPOnThMV4HNDSbCNJaHSfN5oO-tE5HzYtFGioMRb2Yby_6vaf62phGe0TChjH0OzE8Wbg9eig9RfgKsKriSibo94B2h_PKduisdoUPQh95E4knheMZV-uA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
💥
رتبه بندی سوپر گل های فرناندو تورس ستاره سابق باشگاه لیورپول و تیم ملی اسپانیا، توسط خودش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/102342" target="_blank">📅 14:00 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102341">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PyKRIwdr2sShXhBdRDTwUtEig1VQ-vzN73ARztTpI7g7Rv3o_nTiMuSF-RTCmnSKqmi88yev-NQ_VtgSTHL15grsrzvqXCsJNmiGbUGFaVOg2CcnRxlDgM5PMUZ80y7ufSblaYBujeV1dfsyF2kYtKIxUZkACI29TpSZPFHjOjKorWKkrf3l55cKUyfcq5tgJaHSJXVYp5nVe9Zo1Xu3BA9z7iGHFAeA2zsTXDY3x24pIzqz2LnV4U5AyfA-zaMC2maJ36gY05LbCutwtw52Kp9b9-gvilNIV7vbFVCfEEkcGIlUPSeLRzir07RlQmqkdQOec6QnAhO4sD2qzhZVGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوووووری از کوپه: رئال‌مادرید و فولام بر سر انتقال گونزالو گارسیا به مبلغ ۷۰ میلیون یورو به توافق نهایی دست‌یافتند تا این بازیکن شاگرد آربلوآ شود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/102341" target="_blank">📅 13:42 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102336">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r-qqbeyNqxg_HIIYyvcpzlL0_n1QRp4Iom2arBvqgTgwnNkk8gIsapvq-FOAHrDV0I4rxcqfuVaH34kF-6XNijyhJuZ4MCnkG4KklV0_M_HtkmqNxxTWJOf61ym_Dbn99NH3588PrtZHUmJ0wTk8NY_POzYr4dcGnHAYviSEVn_zXXMP0V4b4GVNa48KJRrhkhVZ0YF0kzjva0bpmWgwQY6ekZebHI7NPema7PrPaoh55QzSfm-nDhbCHgs7CxYq6ILtnB3xLPPTbvVNGsjTObJP1AVjgEBbnQPhDirVqo0nTge5H_njcLO7fzzExgx39LDi6Ux4vchVD17NMYXHAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dppjneVktDDpR2cyxdSJAFFkrzOekl0N-xq4izvS6FF9Ig0RNCIeE_D-CoTNjtIpIkn5PmV95qv3u87ziLuJ9g2JsxGfsbxUk9HDgTOkPsrU1C6YfYpgESShapqz3FM2wLu5BcOOkh6CzkzYSs84d_Ykp4huctvtLGXAaoKj6hfoHYT5h1QRbgL33LQ1L9HAAyw2m5rtbeFvnSSZ2LMktSO2PlOI7N4z91qaJ1FS1oJ_5etCkOtwLshIR7vD9jibiE9qeGsrfiz8oznGu_NFSRpHBAKk-tRePaup498Mc3iUBEOPeNhzOag9jF5niOTm0D19UeqEs4IuD102VGtrSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N4XcB-5eGsEJrW23Zvi22eQ_cp66mWxIuxPoxRkv9e-3d8DPWfCZRXSUgIkW86dN44ZhF_shxMzlNaU3voyh8o7x32Z_tsOrP1wk9Qem5C-ZgsR9vNVoKy5ZroBrxGLycZra8OyUJhPUTctbx_q3xUJdSsA40BOSfgwEfDhVIXgUqYQQyRKA7key6BihngzTaEn9XfebcG9SlTkvNEXnEVhsb02ObK3x9cOInlAvEoPpLXKcJhGnuMkTVkMKgN6HmgXpnBVNCFmkRQ3rqfAR71pL-Bii6vK4-gytX9yu57bSw-1Sk95mjsHerQwdaQhBFJXYh26rQv1Xx69Ui4SVkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nrtKuxGYc_m7Z4xEmisPLY-dFWsHjhPkSZ5zOJBgkafv3BbHAbD1_GZfTsVroPmGyMxGFHA1-Ok23mAF59vKHRFXm-OJjMFUQnFfBFsfJPkKrA3I2DYSf-TMeNLyyH6YXcYEoMP6Xg1w9ct5ViNQOALRHFFcyFpdxR-xCXHwoIok-clEWXEGLo4oQeQQRJcp-IR8L7jdUJlEOL6TD-zpEPKPBLikfKNbdJrFuH_cWxYTWOHSRsNgmVrlhmdC_MMG1qCqLvuoAUJAhr1y22Xam1SLphqthWN81ikbVvuA4wBxqg8FpAhfUXM0UOopHPer3T5JRdhIo9HhvTfy-QWOAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CjK3baZWCnURaRnm-1HDGWhkptyamps7k-evjrBPQgHduqjmbgHB1Szgd5Nl8msEh-tzfYxCtS2q8EvvXSAbBpYVnoQFFCq_fNFUfIQmOLx0De6_wqO2TtaZNyb6l6GzVwTR5nfhAVnwWJxxYNz7nc9YoSMAa0V4M6S2zb9mTTFoBnhdkHcjJ_GnI8sNosIuTahlGKzhlgOu8iNebFzmyjpd2wm4eH66uYLu7Yi1reUhLEvyBlAXkUf6F6-VFEbK0gGuwXILEN98JzdYOaWFRf1Bz943NIWis4l7dx78WJDUQEykjsA7mqVxU55iHSDvO47lFEpxae8DSGnKW9YC8Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">+ قدرت تورم :
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/102336" target="_blank">📅 13:40 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102335">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/efgdUFLb99sJDYMT-ESXqw4MRH6PDfJeZeYhQ90rQuURg-U9F43XQc3edOvVpH5Euwp-27kgWVjQIe3S2YjASIFcHO7ObR1d_hsGMd2vcpCfz5GlRrSSPpCwldT1AofRZeOVCW80MWVMUAj1G9fBshGG5Ltq1LzZrgdWZovjqb1qF8BqYVI0BO5MjJuw1NMPDHBeLjb2RDi6z4culoxJXXmA-uS2_D0TEK2yxveMYV2008y5OtxyxU_VEly0Mw_9dTfM5p-3-KIN3rvd2TFAETMnXppStjuHVPF8m7gHq8zWQIWczgw5LpT-gYz1x5J0J8HBPGR9pjCjkqIi0Mbehw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
💙
#رسمیییییی
؛ روزبه چشمی قراردادش را برای یک فصل دیگر با استقلال تمدید کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/102335" target="_blank">📅 13:35 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102334">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pYYg47D9f_gWTOscWY922tkYnOoEiuoqY-ld3mJIUFytfsTx53J3FgAanX8rfKsi5JxcKbZWOZ2bbPkhwC6LpaiKFl-A89davgrdzrY_jFZDT2JTBMJ7YvGvVhEWw9FrbkNIlx8_zOsB0VfrIz7ERv6Qq95dgqWvA6KgVjqaG0cyqGSe68AG-F4tey57EmWcz6AtqRkOJJTGsf1WCClenn3pcUSB7aNuwdlSc0oBIK-HJStdoyuOY5dN2WmI2vL5wVZ4PvbEnqKNs2cqc1VkL46ZN83guhd2Igilsd3TMeIgAstN-w-kGauyaDmrdPPaaN5IDslAAbVozbJffzP9gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇹
⭐
فوری از فابریزیو رومانو:
⚽️
ماکسین لاکرو از کریستال پالاس به چلسی پیوست. 𝙃𝙀𝙍𝙀 𝙒𝙀 𝙂𝙊!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/102334" target="_blank">📅 13:33 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102331">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dW8CLmSKKrU2PzwE1vr7WY7vGT_tscPxVb2xtDGnva_x9sgHPCY7VhARio_EZ7crgvDjTwe4kkX1p2v4R2q3bVpRG0YlcCBg7D9fj1azETpEle-iXscFS9EuA-9lVJX_Emes_l-CBTyiIJfDudS_D1Z8Tjk-tcR26jmEsdirL9BLeFXOJexRmLH-iK9bRqFrMnk3rfz0u9drefLdQngGk2as50oGg6T6mTGDi1C0gdyE-tfFTcrWP9_7JznISp4n11Rpoa2iRA1rUbHrrL4thfug-T_Mbq5kYVyGvQ4MIryN4gLsw7EPtVhcioqSZjldPY3FAUHNrw-XydTFqfUd2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VDccYwmzMB_hdgdtGkUYJmXUY4zvL1p_x6P25bz1wsBgq97zHRMbuRwxJMC3fboVEHyoT4q68UwEK_rgkGRGcxLAlgZM1k2S94Onho5k2HFdB4dLcJaOX8rctxZUj0Kx6zUlBxNZi3-YJ44oOPwKjTEE6_ClmhwathlFwCfD-N-S1TOhdjIZs1UZ6dZLde_iszvo4q2AKwnR2gP5Gpim7qG3h0cJOlRhDdIgvQ_z6fGVffxi64tsRN0v4dLlza1JPB4g8iT60Zv-dYUi5e-ijgHNxoeAlq9FhWF6bg3oPCEy5LzIwQYQ-1aT1IDPWaSUrWO_jjiFhquoJhj26f-0_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uO9wWl8mU180nOAQQDqmJiuwg8shpKpq8dVV2RPW_Z_2E2-DUEzxf0on-FdUKZ4Ba4_pW2Y1W6BHM8jVgPs5pV0fc0lcJaz4It9TQRHCbDP9tdQEYNZCAYjkaWPkoByO-6Dj-kcfxSOsjWhExZ-HI6JwVk4_M_pebP9hFH56RKL4xfzYJRE_gIbN6zD2l3JuzGdomj5O-Uf9VpCBHFRArjNuzaEIw1OtkxdDI2ANKU1CAFagbt4xrP4vZ2WgZ775H6CbQwTGzS2qs0Wc-S0bkJW7i3ashfr6IMysJq-XhBOwWX8JAyE_ScKYq68elv-C7aWbCZbdKqIojYc6HXA2jQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
🚨
🗓
🔹
اعلام برنامه مسابقات سه هفته ابتدایی پریمیر لیگ ایران
⚪️
هفته‌اول لیگ‌برتر
🔵
استقلال - مس‌شهربابک جمعه ۲۳ مرداد
🔴
شمس‌آذر - پرسپولیس شنبه ۲۴ مرداد
⚪️
هفته‌دوم لیگ‌برتر
🔵
استقلال - نساجی سه‌شنبه ۲۷ مرداد
🔴
پرسپولیس - اس‌خوزستان چهارشنبه ۲۸ مرداد
⚪️
هفته‌سوم لیگ‌برتر
🔵
استقلال - سپاهان یکشنبه ۱ شهریور
🔴
پرسپولیس - تراکتور دوشنبه ۲ شهریور
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/102331" target="_blank">📅 13:33 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102330">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SAEn909jin1xduxJ_8gLY_Z5cP6ez5UZTiIpxBMsp7V69bKmVj1cFmoZfhelBFg2Zx41ScWxGgGIF1TMFStq76MB3a_pBwy_zXX1CM0wJT6ap8nR6h10H4ro5cpwEZuVf5tSx9IOVYLPrOXutJgJDGnaUwPdmylKY3ri9USZWleEk3YGa69ogyaBCsPwKFxr0sthuQvtv4h3orGDFDx6jXpW51HlyIGf5efi0IXm87jkdtAVGtXRLWFh1NttT1ZflHOHXt7h-Iev6TuquZMEdkX_67A0QbsgjCjynJzDXpThzFCn-pNkX9sSd-tqQbwKqJIRmJbfJDFgOvawe-Dqzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوووووری
از کوپه: رئال‌مادرید و فولام بر سر انتقال گونزالو گارسیا به مبلغ ۷۰ میلیون یورو به توافق نهایی دست‌یافتند تا این بازیکن شاگرد آربلوآ شود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/102330" target="_blank">📅 13:16 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102329">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AO9rfLsecNDs1bF2pI9YNg3DjGyWdfodgK4EMJrjZOt1X1AHva2fmVZxfoXonNLxRG5JsgoxpvQ_vZw7twtVr_5LHviAWZiINEh4NlxgJYOM91FtJNnJz0r18Lu0Ho0zI3bZ6q8K5rsXdN1GjfuWfG4nv7lNaI1wwnmFWZYpS-o_kLEwxsWr_PEWXtWjrYZteoElQD5ZwMATGEVaHTs41YpeaQZrs4g1DdL6eAYOYWLYz7mtK2ncdB8v7eS7XZwra27MkoZoKuRAabMOTOr02Om2PLXJpTRgiI05aI7nuOSBLjWWxwZMW6rwXd4uZeaS97xxuHTOcFE_3TKGAaUFrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
‼️
✅
توییت مجتبی پوربخش مجری سابق صداوسیما علیه عادل فردوسی‌پور.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/102329" target="_blank">📅 13:14 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102328">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee8b739e27.mp4?token=FcdU_PPMQEug4FGYwnUu61LGtKG-0n86drr9wnmeHKBFeeQQPJ5vGpDqzK_gPz0SCL9lik8J7BDnb4u0Tfpe1HDGbalaAB-V6Lj9F_aEr16hcNzmr8HbOqKJFpKm7IcO7GA6PknOqPNBWmqnKgIy42-hz78uOgLOm4s52-zGQe4cjWaRe4WQ_vgY3L6VH0dbbSaflTqvEg4veUbvBQvaZZKlQAB8olpvXL0ey6e89fpkn7uF8bXHw9wNktmW62xzIkjeJaxvxXmfJbf3wRFN0Qbp2XVag3GZJ3JSXQZ_VD4U2Ox49lGU9lP0C7Rzl3Q3Tk3CryJ21BzGvOG0qPgjVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee8b739e27.mp4?token=FcdU_PPMQEug4FGYwnUu61LGtKG-0n86drr9wnmeHKBFeeQQPJ5vGpDqzK_gPz0SCL9lik8J7BDnb4u0Tfpe1HDGbalaAB-V6Lj9F_aEr16hcNzmr8HbOqKJFpKm7IcO7GA6PknOqPNBWmqnKgIy42-hz78uOgLOm4s52-zGQe4cjWaRe4WQ_vgY3L6VH0dbbSaflTqvEg4veUbvBQvaZZKlQAB8olpvXL0ey6e89fpkn7uF8bXHw9wNktmW62xzIkjeJaxvxXmfJbf3wRFN0Qbp2XVag3GZJ3JSXQZ_VD4U2Ox49lGU9lP0C7Rzl3Q3Tk3CryJ21BzGvOG0qPgjVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
روزی که مسی به برونو فرناندز درس فوتبال داد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/102328" target="_blank">📅 13:01 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102327">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PPcl_wYEp3pYr28fSXwC8o-xdTR9taQJJ3iU3n6FNjouvo3ae_UgrzrzAE8QPShrWvWuZZOGEnWRcyWERowj2WGDi6G3M41GK6w_xW79pztYkq3jAcy92l-aLaSrYD9yJhATxxxRUS0pL2pDRg7B2QcxDRiiywKg7HVXWbEYeSG1yGBLtwd7d5TYioJUsKS2_SGJlHgmOArlcuYaWzJGAVUFRGN1YXRdk8MAMupGrPC7coo159IG3dDb9I1AmowkiIvFebusETLTub5OcCnw_4u17ObgPfqPEXmw9Ylcq4S8JipohB553Ro8bICnUYw_F5hGUUvQnRmhS_b8A2NI8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✅
🟢
صندوق سرمایه‌گذاری عربستان سعودی ضمن تقدیر از یاسیله پس از کسب دو عنوان قهرمانی متوالی در آسیا برای الاهلی، با جدایی این سرمربی به مقصد نیوکاسل موافقت کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/102327" target="_blank">📅 12:48 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102326">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa8a1ce74f.mp4?token=G-73f51DmccXCW77AUTfXo8pQDDNZuz3xJ32oRpcvlb_Kdy3H76241yApZLINwe08GC7r9oUES6wsLOGIXEBtRqwB7A0vPS5HWB2kiMigEvzdJaRWkuT79p8mSdaP51uoCG2M33gzW1ZYZSmnetZ1BAv6Clkd9YuXoPfhh6PrhM0A1-GZfa0APVlokt9uwMIi92OINVr-31YyramgQxdIC2bqox346Wy-sWAbvIRDE5JI20_avYcEz0ceo68j2T_X4oqq7NmzdYnpYttCI5AVgF2k2HmE4qrL96dhxKPHtJNS4eqM3Ffphp2cUnqRCr5G-vc3L5OLG4ezAPykxoVWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa8a1ce74f.mp4?token=G-73f51DmccXCW77AUTfXo8pQDDNZuz3xJ32oRpcvlb_Kdy3H76241yApZLINwe08GC7r9oUES6wsLOGIXEBtRqwB7A0vPS5HWB2kiMigEvzdJaRWkuT79p8mSdaP51uoCG2M33gzW1ZYZSmnetZ1BAv6Clkd9YuXoPfhh6PrhM0A1-GZfa0APVlokt9uwMIi92OINVr-31YyramgQxdIC2bqox346Wy-sWAbvIRDE5JI20_avYcEz0ceo68j2T_X4oqq7NmzdYnpYttCI5AVgF2k2HmE4qrL96dhxKPHtJNS4eqM3Ffphp2cUnqRCr5G-vc3L5OLG4ezAPykxoVWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🙂
یه فلش بک بزنیم به زمانیکه داور زن بازی رو متوقف کرد تا به کاکا کارت زرد بده و باهاش سلفی بگیره.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/102326" target="_blank">📅 12:40 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102325">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/49420aa7fc.mp4?token=D5c7yeXENS-SGTrkdmU5oabRcoCKUtjRvyjixnbBW1KIBy9Edex01q1gSyBNiwvafL68H1Nmov95JjnR1DzhVU3VLdxuebJ-bZ8Gj46JA_3DJOlAr4IhGTjtR_JF-twyQ2GH3Owv3M24AtH-CkzuYrQ3RodHRehwXSyv6BYuiiesfs8msiRZUeXWtLwD6FA5rGSXLbxOyYgOI4F3FQtP9woxLkaxxG-JgZ5hgakZxUJru9s75YHuQngjMs9GkETN9FrhDygOsBvgN2qGUShoQX72d1AkslYHhVGciU9Y0-ShLSdeticG-q3kIc8_LkvECRDhlgWCHHD-7CGZaNvmxIHVziSre9dX6Jqy-rTMVbYndZeCCu45ITtj6lTgAbmM-tAqwJpGquEZfYtYDgIBnQPtCZfvlCyLipEYvFIeEXZARuJAi7FpNdA1rtPzzf6uAWr1RK-ca60INU5n4ATbeI6OcOxQlWg2Ya-HvKKRoZ2fXOKMpGDw-ccwVPoH7VT0jrBtrGrL489-r2o0mQ4IouS8YYbT2ih4srJbKMokvZI2fxQykrs63-1ULiT5IR2PPkb-QXA5m__BZNpRDliyrD5_dkEQ5OL3hLtFqBsKVyJtScayPGLYX7ra5t0QLB2gl8HfXUAX_cePFEEATLEGkJn2mzCSiE5cOwm8XuvRrfk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/49420aa7fc.mp4?token=D5c7yeXENS-SGTrkdmU5oabRcoCKUtjRvyjixnbBW1KIBy9Edex01q1gSyBNiwvafL68H1Nmov95JjnR1DzhVU3VLdxuebJ-bZ8Gj46JA_3DJOlAr4IhGTjtR_JF-twyQ2GH3Owv3M24AtH-CkzuYrQ3RodHRehwXSyv6BYuiiesfs8msiRZUeXWtLwD6FA5rGSXLbxOyYgOI4F3FQtP9woxLkaxxG-JgZ5hgakZxUJru9s75YHuQngjMs9GkETN9FrhDygOsBvgN2qGUShoQX72d1AkslYHhVGciU9Y0-ShLSdeticG-q3kIc8_LkvECRDhlgWCHHD-7CGZaNvmxIHVziSre9dX6Jqy-rTMVbYndZeCCu45ITtj6lTgAbmM-tAqwJpGquEZfYtYDgIBnQPtCZfvlCyLipEYvFIeEXZARuJAi7FpNdA1rtPzzf6uAWr1RK-ca60INU5n4ATbeI6OcOxQlWg2Ya-HvKKRoZ2fXOKMpGDw-ccwVPoH7VT0jrBtrGrL489-r2o0mQ4IouS8YYbT2ih4srJbKMokvZI2fxQykrs63-1ULiT5IR2PPkb-QXA5m__BZNpRDliyrD5_dkEQ5OL3hLtFqBsKVyJtScayPGLYX7ra5t0QLB2gl8HfXUAX_cePFEEATLEGkJn2mzCSiE5cOwm8XuvRrfk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در هرجای دنیا همواره فوتبال آبستن حوادث است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/102325" target="_blank">📅 12:20 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102324">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xp52jHaL-tItnLiudaspfSI0RLn81FyHidO6YRvxewx9GYdzQpnWrlNck3vRg6PDcFibzL3QXoAtf6IArTY1b4D_TiLCSa5e3BpCVamdowlSWuJlLCQBgQEliaXFyXHeRL4jpT6xxawAV7LUWLEBj5TxDckWWgM-pjQhhoW69GfeP4TL6vCiWFmf7kAIV53QonSLA1XTDaZqAH6-FPotOscL-DyzoYrv0_4m4SfXSEbLJm5_tYAnWsnQskShaJegn1WIgjpC4jeVsAQdjRWSKY1qvCvvPxQ_rlYqOjrbqu_-Mbmwxuqtxvz6_fYZzOcbbsSwY4JbyeP37HC37bKfkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🗞
🏴󠁧󠁢󠁥󠁮󠁧󠁿
ماتیاس‌یاسیله سرمربی الاهلی عربستان در آستانه هدایت نیوکاسل قرار دارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/102324" target="_blank">📅 12:08 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102323">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9305c345ee.mp4?token=LEJhivmdzV6DJtOikt2ClMb2vxYJ3qRN8-gsmeWC2dYOfn6c9C6-g98LdUWzA0hNDWSB8GaHH8ZnsrizCoD32esVIs406EpDGbY_GRrHBW6SgunaTIhRdCV7N4FYCOCvu9yUf9S155Q3EPOKvpVpmw2kczs4V7pU5KRThn7ypZZ5I-Gpxs2eNV5kJDSLS9e6emSowDGtklZ6VB2oqr-uTNNA5cQcAN_A1RJQFXcuD6AWLKhQLgMMQ1EkECYvNhdJWWYlqOMxveEMMv-TmpNl4QJyWsVLyZzqQHfqxF61xvbUXMQggSyKGrcaym7chfCAsbafkYfPkj4KydSGlA_LaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9305c345ee.mp4?token=LEJhivmdzV6DJtOikt2ClMb2vxYJ3qRN8-gsmeWC2dYOfn6c9C6-g98LdUWzA0hNDWSB8GaHH8ZnsrizCoD32esVIs406EpDGbY_GRrHBW6SgunaTIhRdCV7N4FYCOCvu9yUf9S155Q3EPOKvpVpmw2kczs4V7pU5KRThn7ypZZ5I-Gpxs2eNV5kJDSLS9e6emSowDGtklZ6VB2oqr-uTNNA5cQcAN_A1RJQFXcuD6AWLKhQLgMMQ1EkECYvNhdJWWYlqOMxveEMMv-TmpNl4QJyWsVLyZzqQHfqxF61xvbUXMQggSyKGrcaym7chfCAsbafkYfPkj4KydSGlA_LaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
🇧🇷
فالکائو برزیلی بهترین فوتسالیست تاریخ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/102323" target="_blank">📅 12:03 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102322">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc1c528fcb.mp4?token=eudO8BNZiT8wHCmGAOOoBNC2-AjVjBZtkHAHlPLgGuovWVjd51nQXRrDUFFPciX-sY1uUiQ3mIbNRzWaSES7RkTfn6ROGYEpyvDwstN4xFXVJGjY45WtHTzjOEhqz_Nl3G0v8SsT7t3bdkjVPNjG0DM-HIrEWhpHFpGHG-7rLXKSEq2plMHLufddzqYEhzmvmU6qWolvCYhH3lrAhgWwPnTaRudLxl5NPhqb87yLlDKEaUUuErmbkOmlgUfPMj9FfJkx8vxQzrDmHjTfApaSbduvfp0EN3usnFAHSTHPIhdqcJecUJ2nmTiLTFIgqzUKMaVhsc-kSqNH068rhb03Kw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc1c528fcb.mp4?token=eudO8BNZiT8wHCmGAOOoBNC2-AjVjBZtkHAHlPLgGuovWVjd51nQXRrDUFFPciX-sY1uUiQ3mIbNRzWaSES7RkTfn6ROGYEpyvDwstN4xFXVJGjY45WtHTzjOEhqz_Nl3G0v8SsT7t3bdkjVPNjG0DM-HIrEWhpHFpGHG-7rLXKSEq2plMHLufddzqYEhzmvmU6qWolvCYhH3lrAhgWwPnTaRudLxl5NPhqb87yLlDKEaUUuErmbkOmlgUfPMj9FfJkx8vxQzrDmHjTfApaSbduvfp0EN3usnFAHSTHPIhdqcJecUJ2nmTiLTFIgqzUKMaVhsc-kSqNH068rhb03Kw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
❌
الکساندر پاتو؛ ستاره‌ای که قدر خودشو ندونست و خیلی زود از فوتبال محو شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/102322" target="_blank">📅 11:40 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102321">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UfUZUV4WD3eypy4er16uF9FukTFMnxT0fODnLF-gcLsxkbegS4ndj0DmzBMHd8jjVGyoGjOqR38gCUDxYtdxUj3Y6PgbwUa811PQIDiOepzuvM-fGRB-4GDv-veDhL-lXU0RsDV1itlRMmXcDOARbRDv0pFFM4g9R3ZPOm0EABs86pEtMesF4MvXxBeHEQFJ_biOW-IIoHTEXB03JwrLNZP64jQXaY2gNjc1N8xt5P07nzIlQ8UEFNY_KVm_AET22ZwxkaojBMX1ag-aLbvYGMYXqOYxF_wCViVWF6npu6oHl0BPSG7IP8um-opdtzX7uc2oQtRJbltx3pRLZ_RVXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
⚽️
رونمایی از کیت اصلی النصر برای فصل بعد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/102321" target="_blank">📅 11:37 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102320">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">✔️
🔹
بازیکنان خارجی ، 4 مدعی لیگ برتر
:
🔵
استقلال:
🔵
آشورماتوف، ماشاریپوف، آسانی
🔴
تراکتور:
🟠
خامروبکوف، هلیلوویچ، ایگور پوستونسکی، اشترکالی
🟡
سپاهان:
🟡
ریکاردو آلوز
🔴
پرسپولیس:
🔴
دنیل گرا، اوستون اورونوف، مارکو باکیچ، ایگور سرگیف، تیوی بیفوما
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/102320" target="_blank">📅 11:26 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102319">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UQcDfqLVoH_HwKLZtXFo_8PbAGmFE2TghnHCnJfUCSQdCKzfftaMSGi1CXQmBdUtWtYaZ9UDwnV0-zb0ehrKf7u2c6Jz1GzGP_kaSk9icpBou25fWpXwrV5xv3UudA0ZhlJBOD2Xp6FnoXs6aVaR6qsvUnstp7e7A4zpFtJeSHlDgmXn8r9EPxox0tTMDiAtGZMpJAWfanQL7uU5bkhpgIHfXB2NdedbvOdxQxRb57UEIuA737mpeSaduCZ1VaiGpngWUPIhK4-CbsuIhu1CWSE96rnMlp8MEoqgyo3xScchyucFePRcO86M_KnVYBhB5ajkxp8ql_KCjud9gzwEjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🗞
🏴󠁧󠁢󠁥󠁮󠁧󠁿
ماتیاس‌یاسیله سرمربی الاهلی عربستان در آستانه هدایت نیوکاسل قرار دارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/102319" target="_blank">📅 11:21 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102318">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b07d2f0b1a.mp4?token=qSXQSJO89G-05cziXmYc1uEtzoM1t-Y-GFjuJk7SWm4u3SJLhjVIng5f2Aw5zBPYE-yDb78GtfwH3kDcokeJGMQk5OxwnTvrlN3dZoYNdzwxgHUShWx2wZLaUxyr32bboWOZXqVuVButyMH0l2R_iTxfmloAh7adlsGM5aLyNnxZnzmfHxvRN-E8AIH3Vg6T054xvoFy8D2ZNMA1EE-B9E4A--NM6yBSJg_CtJzWEWBxVUlTYj35h03CiVUgY5pgt3qEMKzuDul-U4V6S_17KE07aZvkQgX1mJxTSqmaU8buIHtQFTDOvCwLPHuocaSJ_Fn_DsSGtJMO56IfKbpViQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b07d2f0b1a.mp4?token=qSXQSJO89G-05cziXmYc1uEtzoM1t-Y-GFjuJk7SWm4u3SJLhjVIng5f2Aw5zBPYE-yDb78GtfwH3kDcokeJGMQk5OxwnTvrlN3dZoYNdzwxgHUShWx2wZLaUxyr32bboWOZXqVuVButyMH0l2R_iTxfmloAh7adlsGM5aLyNnxZnzmfHxvRN-E8AIH3Vg6T054xvoFy8D2ZNMA1EE-B9E4A--NM6yBSJg_CtJzWEWBxVUlTYj35h03CiVUgY5pgt3qEMKzuDul-U4V6S_17KE07aZvkQgX1mJxTSqmaU8buIHtQFTDOvCwLPHuocaSJ_Fn_DsSGtJMO56IfKbpViQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
با اعلام خبرگزاری رکنا، نوید زیادخان قره‌داغی همون حیوون کثیفی که دخترارو تو خونش کتک می‌زد و لایو می‌ذاشت، بازداشت شده
⚠️
‌‌ ‌ ‌
یه ویدیوی وحشتناک ۱۰ دقیقه‌ای از
این حرومزاده منتشر شده
🔗
🔞
مشاهده ویدیوی کامل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/102318" target="_blank">📅 11:16 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102317">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
‼️
🗞
🇪🇸
رومانو: رئال‌مادرید و لایپزیگ بر سر انتقال دیومانده به توافق نهایی رسیدن اما دلیل اعلام نشدن خبر اینه که لایپزیگ ابتدا باید بازیکن جایگزین جذب کنه و سپس خبر رسمی اعلام میشه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/102317" target="_blank">📅 11:08 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102316">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a432ebcf02.mp4?token=gLFiVhlKzG7FJ0YQi4dqbYp8j0FXmmDpndzcSL5oQDoKa8N4UXSVD-mIVRZAC7_FGHYdl3P5WVw18461NJzqPhz84Sj5ojL6CgpECmFZ4OF7yDEueum7hj8XQ1_OkZ_A_IrFl-6raPUKIdYkmrRasKQWs2ZZHwmxiQOL3al9W4I-xAeEQO5iCCEP2pyLlQDpkU5LC_1cnidbjX1v_oF4ZzewIKRg69WJoK8_xR9KwdS40gIa3j2D1vSOqSDeWFUx8Ko9RpxKRK7A9-4yR7IuOmFLpqRB2K5AwhLBTD733sZcbiCT8u8uXQ4ZFo2LJxNz5T6aonaa8ggamxlsqfbXIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a432ebcf02.mp4?token=gLFiVhlKzG7FJ0YQi4dqbYp8j0FXmmDpndzcSL5oQDoKa8N4UXSVD-mIVRZAC7_FGHYdl3P5WVw18461NJzqPhz84Sj5ojL6CgpECmFZ4OF7yDEueum7hj8XQ1_OkZ_A_IrFl-6raPUKIdYkmrRasKQWs2ZZHwmxiQOL3al9W4I-xAeEQO5iCCEP2pyLlQDpkU5LC_1cnidbjX1v_oF4ZzewIKRg69WJoK8_xR9KwdS40gIa3j2D1vSOqSDeWFUx8Ko9RpxKRK7A9-4yR7IuOmFLpqRB2K5AwhLBTD733sZcbiCT8u8uXQ4ZFo2LJxNz5T6aonaa8ggamxlsqfbXIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
از دعا کردن تا بزرگ کردن لامین؛ چند کلمه درباره یامال از زبون مادربزرگش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/102316" target="_blank">📅 11:04 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102315">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LEJWuDtemdI1MmV-arsWxdozGKeT7mLFcGUzvGA_Cfi04wvRd6NB2H2-r5jwcgrVttMFdSzICR2Crxfv6A2ileQ8NU-1lLZsbIRerUV4kDJB7m_UB0JtNrdqTWVCnaqCIF9MCwTDqPM0tFRwnmsIvmlnxGGHR5DIMyx7X0hzVJrZJY6TbjMtHpOUgeN5HWfthkR_YlpcGRWNKr5miSU919CP2NMmU42BaqXO0MgVLbEqovfcYQ92GqvZ1B8aM0DUV_sHbfI1AJ51JX9Am1k9i7BExl4Z3jBK9q2ifEqfmo3pj5ujCDoJYxeS-8TT_7Fqr_nhY7rB7mzCjalCP6ar_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇸🇦
🔵
با اعلام رسمی AFC، مراحل حذفی سه فصل‌آینده لیگ‌نخبگان آسیا به صورت متمرکز در کشور عربستان‌سعودی برگزار میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/102315" target="_blank">📅 10:42 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102313">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IB8VFnNrszajPacXstSh9A8UjUVhBQMMvodOfpFvsY9cBOhLDWn5ASKGkqIImmd-sixWcYzcaKoZANgKW7EXhMmU8OcsnXRwH8qn_HLZp-f_dk4WtFNGpCZiO6IPqd1ENcvUbKbqGIAmg_GoVeUwmJTxitZY1h_NGHfq4fXLo4P9jVffm6mb1xM_3B1olF6xP18KVs_zH2SAGkDdh7e1n4Xh0H7N7w-3mT3GYLhnuZacoGmgTxRliKeV5srPgHM-3iR7gHAlzNzfaEjTXsQKFUUv5U0lauayWiJgiJFrTbE8j1s70RtW7FrR9yjuXdEFgClSeBTtgHNgsVkvuPd6ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✔️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
ایوب‌بوعدی ستاره جوان و مراکشی باشگاه لیل در آستانه عقد قرارداد با منچسترسیتی قرار داره و بزودی جانشین رودری میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/102313" target="_blank">📅 10:39 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102312">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fac4341594.mp4?token=qBVBxdS3BWZ-5yNFsrCw7AB9GA2hyRnzsknf20OwLusZpmtI2ReEjM2kFmzrA7IVykJSguJmtg4c0ygMbQVMf1rzO3ULNBwdxf-JAqoSczuBdQNH5s-bZZZO9iipZnIuPslANDiDx1HUE3xdWOIF2R01-yVKpoNVuGOLMkAPVuWmKBxNHJd3NXtIFAlG5bt1RL81P6qd9ouMQTYvwgFbKQCN0JgE5oHtDWFthV07MeuoWgOGb1qhyLyH9Y_gkNefYU5sVi9lo42gK9uw3q4URZJVnCD1IlUMooUmCinn4n5o1ZhpNQa0tVWe0oyHo9KIjlugkYNG8IjWbv6cJKSQVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fac4341594.mp4?token=qBVBxdS3BWZ-5yNFsrCw7AB9GA2hyRnzsknf20OwLusZpmtI2ReEjM2kFmzrA7IVykJSguJmtg4c0ygMbQVMf1rzO3ULNBwdxf-JAqoSczuBdQNH5s-bZZZO9iipZnIuPslANDiDx1HUE3xdWOIF2R01-yVKpoNVuGOLMkAPVuWmKBxNHJd3NXtIFAlG5bt1RL81P6qd9ouMQTYvwgFbKQCN0JgE5oHtDWFthV07MeuoWgOGb1qhyLyH9Y_gkNefYU5sVi9lo42gK9uw3q4URZJVnCD1IlUMooUmCinn4n5o1ZhpNQa0tVWe0oyHo9KIjlugkYNG8IjWbv6cJKSQVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">Auraboat kids
💀
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/102312" target="_blank">📅 10:20 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102311">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZX-t7F1mfiTFNx5cIufMXR5g5DQQbw0J0oDVARzJmaKuoSU4vHBDEUCcy8jxyA4c8h2OkkEqZp1W6TKTusPauRJPkiCV5RJwQwO_ee168Efi8I2uk_3bmXy4_c6ycQcnZfkakiwpBfoOw3gj5_vkRz4MTCC82l84eRxaTdlJc6KmG3R6y7x60rCV3HiM3Pbl2c6Rcp5fZXBBOWV66zLs7TmizSCUonTKeY83BnGYqIJQ7dGIpq9r9626OQOtkU64ggNpSn6fyZJblRSLYBAbGpEm7MS8_6GEMmmED5_DVtc921yICGAvU4b0So6QePnw6WXjOa4-mp4LizWLBM2dCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🙂
تمام‌نیازمندی پسران فوتبالی سرزمینم :)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/102311" target="_blank">📅 10:02 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102310">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gY18BWVibkRFkbMHplkbnpKPAbNP4RnKIOPFK66vDlYUXoEpWUM80y2U5oyJ-ssMxjlEucI1E7rDsbwgtuqke5Ovr32uXiYVqufUVRxHX4L5T3I0mVGD035o5lOi6m4lW6PlswKPPP8T_ZgTsd65qsd8KqQEwcgYOr-90VTUFGumJ9aBEozbHpiduMAgQFf07KK4U66cG8QXp03yt4FDnzRmQGmvHUseK_QA-sGuUCV0CkjZStHJLkP8CEeFF2JCAQpH22L3wrniqhv_QFmaDU38hNbG6xbaQ9L9Fnz_IndDQwb4FtbCtrXGHyUrxCCSqcVgDYf7fG8EVv6TcgdOzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇹
🔵
فابریزیو رومانو:
پاریسن ژرمن و موناکو برای انتقال مگنس آکلیوش پیشرفت زیادی داشتن و معامله در قسنت نهایی خودش قرار داره.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/102310" target="_blank">📅 09:35 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102309">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kf5sSrQpzFjq6s7rJJegEMwBk7UEIFxeCSWjFHV1fDh6bzF0YGmSeTORcQtqWsKgZ8ZywzW0kdKJG_nB6jLnr1cckMnQ1ZZBTdHBmdWLxYg0pM21D_sT7w86mUs04yvMeeLFH-IRDheHDf7HwcwPpS6wzWeFbmsbKppoEwMFbCY1-yASdcP9UGOo7lLQFHIaIBqYGVMznIS_F30V78gMmwj4wRtiH3hG6rZDHEgq832PStL6MLpRrPDN6iWXYjQDlD9pGP9dSePGjxC9v9nFpu3xHEYTXeGrJ2LMyOqF_5oJkSNKVBeLGMwOSxiO2zpmAijjkqGh66FVLPdP3QKJng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😳
بلینگهام برا زیدش تو تعطیلات عجب پایی میخوره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/102309" target="_blank">📅 09:20 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102308">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tl1aXHvTWqQoecVsnLSjxuFBn2JHvAVubUcWpRL8sIYy-2fLxw3rQwuNO0mX1ni9TpptFYs3nfq8vtrTOjAacWAuDe6OCoeU3Vp_kelfsfGqHRDaZLrUDHPTJ41ZFiK9J2SJGx_pRRyWi0T4pzpWqOjD-M6zbvToPcY8cA6BuV4S3Oa23dCIrC748N2x2392cHm-A7yExHxyuiNlTJzWSketWLelZgHu8udvUgnxxXkoDfEocXmdzQRgB7NsI4r26uagqmuWot9Cu7wUgmtzhlN1yaxc-XOYHFXHdT7Htv-Ut3qIkmsnt9tpe3mAMytUstNucHnUXbzjm9s71Do8hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❗️
عکس پروفایل فرمین لوپز، در حالی که تمام هم‌تیمی‌هایش در تیم ملی اسپانیا عکس‌هایی با جام جهانی دارند.
😭
🇪🇸
لوپز در بازی آخر بارسلونا قبل از مسابقات جام‌جهانی، دچار آسیب‌دیدگی در پا شد، که عملاً شانس او را برای حضور در جام جهانی از بین برد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/102308" target="_blank">📅 09:00 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102307">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/31f0971b6a.mp4?token=VjZ6NR1Af3b97GzeCK6x2v7_y1sniMynCeDB7kclXiCgURvjwswJC4ZKVQQegyslBTj--hyFVqF8GebuGR5BXczD7ZeSWQYJ_uLDy8gvRYbDEsn_ldZR0xYz5VvFsivWTct1eZZH4LW14DBAEumk7NIBLlVGBuTBaxA-oKczgrIkZrthIPTO7Rw-X77njmGWtTK8g5xipez_-Rr1wgRF9ZRlIfOSu0_TK_8t2LFokyqxSVdVWxKx-qlIwlSx_yJpeP0AAao_OgkchWMTCGe4TwG8PahUmo8ewdKSeH0VeRlm1ZctSWi-9i97H41QH3I5XtgRK2u_QD3931CbqEqw1A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/31f0971b6a.mp4?token=VjZ6NR1Af3b97GzeCK6x2v7_y1sniMynCeDB7kclXiCgURvjwswJC4ZKVQQegyslBTj--hyFVqF8GebuGR5BXczD7ZeSWQYJ_uLDy8gvRYbDEsn_ldZR0xYz5VvFsivWTct1eZZH4LW14DBAEumk7NIBLlVGBuTBaxA-oKczgrIkZrthIPTO7Rw-X77njmGWtTK8g5xipez_-Rr1wgRF9ZRlIfOSu0_TK_8t2LFokyqxSVdVWxKx-qlIwlSx_yJpeP0AAao_OgkchWMTCGe4TwG8PahUmo8ewdKSeH0VeRlm1ZctSWi-9i97H41QH3I5XtgRK2u_QD3931CbqEqw1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ویدیوی سنتکام از حملات بامداد به ایران
.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/102307" target="_blank">📅 08:18 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102306">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">‼️
👀
اسطوره‌علی‌دایی امروز رفته بود مراسم ختم اکبر عبدی که مردم این‌شکلی ولش نمیدادن و دنبال سلفی گرفتن بودن!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/Futball180TV/102306" target="_blank">📅 02:34 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102305">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HiGRLnGkH-vYsSQstItgbbnMIRJoQ7CFVGTKYotSWtUiz9wRma-4drwdSS0FsPShE5HSRm2oa_3zNQP2AJTKAdRMpwpetixjMR-99YuNHYnOzGpLAFIBn8QTBMYQbhoI-qFZBNW3K2O_n50QbFhTzhtzEewK33d7WgaOkvQ1k-F2IGYUGyoSAgkCaCAUudX5Z4zgEiAizrm3eTPBfLH7rnyYN69CNATC-BxojAuNSZhaC3IvrBqWKA8NE8-669koQv4A-sRoTFNTZHbEMWeuBvKog_KoqkWEzwwFGtni8hou3jgaY1Tz3_IOsz9O2lDrVPU2MRf8m4H0Y3W0R5gG4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوووووری
از Cope: اولین پیشنهاد رئال‌مادرید برای جذب رودری به ارزش ۵۰ میلیون یورو تقدیم منچسترسیتی شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/Futball180TV/102305" target="_blank">📅 02:17 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102304">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X7Ci0H5CSDKe19Oym76Al9nSEOoAmSdK6A-8bG3sLTqAIMF_2jEsJ8cHpBnaitUQPEOqcNRUOoc_4i8IPiFbiT_CfNZkx6TLBuQ2TXRJeSiYnqiuP58frmzG39L7YYiNhfO5QBNwxOd-6AGMMU6GIZ2KSqnHD6B_fPkLZW898PDhOgNkyOz-j-z31qJqB3HOkbQaeygNn8XoXeypPbSVTj2YDmEWIhdmws3VMFpgdWQrabX2oy8xK0wxorYcDHf75bcXCnPvLx6_UQorg44PsubdYlJMEoMQd_lCTPhEkuZIHdQOB_aVf7E-KD9NJn_5EH-4bC4BM7rnp8dIF7KisA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇺🇸
🇮🇷
وال استریت ژورنال گزارش می‌دهد که دریاسالار برد کوپر، فرمانده سنتکام، طرح‌هایی را برای یک کمپین هوایی ۱۰ تا ۱۴ روزه با هدف قرار دادن زرادخانه موشکی ایران به ترامپ ارائه کرده است. ترامپ هنوز تصمیم نگرفته است که آیا مجوز عملیات کامل را صادر کند یا حمله محدودتری را انتخاب کند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/Futball180TV/102304" target="_blank">📅 02:14 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102303">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6afbb43876.mp4?token=vr3bwRc7pr8eFyda_3gtk40QUW_zlOMCMpMC7k35xQI1CYKEDGawNJtP6g5HQBxu5CX7E341XH2IL9zXQghXiXTAWUhA8WWOEpLBLs2MvmWsjfQuOvsgsswZztI-IWq-KJesAmBgnoNc8ws8EHgWgi_JIF0vxKXDsQOpk-cOtrxhG62MXmw36qXB-A7zZwfKV74IPlojHt5qWYuaMsLoqA1m3WuwLzTyFJYwJuZiQiJ2MatRb7QUXeqTVyS1R31ieMEkz0NaV_JrpVE9RKDa6iVQ-G7UAnNpTshLriSbr0mP9vNBs7zMclECFhn2Ltnt1G6h1JzwYHMH7Zq-R34owg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6afbb43876.mp4?token=vr3bwRc7pr8eFyda_3gtk40QUW_zlOMCMpMC7k35xQI1CYKEDGawNJtP6g5HQBxu5CX7E341XH2IL9zXQghXiXTAWUhA8WWOEpLBLs2MvmWsjfQuOvsgsswZztI-IWq-KJesAmBgnoNc8ws8EHgWgi_JIF0vxKXDsQOpk-cOtrxhG62MXmw36qXB-A7zZwfKV74IPlojHt5qWYuaMsLoqA1m3WuwLzTyFJYwJuZiQiJ2MatRb7QUXeqTVyS1R31ieMEkz0NaV_JrpVE9RKDa6iVQ-G7UAnNpTshLriSbr0mP9vNBs7zMclECFhn2Ltnt1G6h1JzwYHMH7Zq-R34owg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
⚠️
عصبانیت شدید آزیتا حاجیان خطاب به مردم در حاشیه مراسم ختم اکبر عبدی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/Futball180TV/102303" target="_blank">📅 01:55 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102302">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MLDo44ofznTyJZKbfG9F5IIGqdsWnZeiFVd_VmTxNF5LKAkZ9I-1ifDYnep9IJ4mZZT--IFCGSeP10aF45hc-GcK9gGTC1f5gmT8H6MF2kVsDUFXUZftp7_d7sipf4AaKW-3mumQ30bwEq6c8cwdh6tnHtDvsshNMiv3lW0bQOk_fYkS0KN2now2EOcf5amYL8xvI6hEYm-H7t9xPaCYLuomX70ZbTXjfPgXErcHU15xMPOpwDBvbtjv_P6H4xKo33NQY-tUtxiEyWxHSy17vXleq7LbMf27X3sqc7qrQ64-9ZHPMB92vehnCXhTvekfxiTLyffC3GUAqcMfpbawsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
🟣
بازگشت لیونل‌مسی به تمرینات اینترمیامی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/Futball180TV/102302" target="_blank">📅 01:33 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102301">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4e2122bef.mp4?token=ElpFO0kAQyXRSpeLwYOnq0Bw-xEA15hRF-tKmCK6Io1sIyUSmxR3AkjUIsTu2JgkoU6kZG6nqOPlcHEs6rMt0loN3l3I52TsxAmOCoWQGFocATp2rqc0o-OZR8hvtAjwZi-9NPrIcgiG68byHtWTdkPyh2Dk-SECF5b_6R_Jvn1RtWuIBuQQZi2wwFxYpfZQDOBeJpfHmrVAolhfV1kEFCw1gl2H4-y_hmx14gJd_F8NiGLI4MH_fWvObPDU5gRWYwYle737YP3U-y8ksY8tHYuIs5BJtHTmaU0-syO8fhz0UZrWDmiPTSNnYXTufWu6A8hEUKLSJ43KUIiHSzISvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4e2122bef.mp4?token=ElpFO0kAQyXRSpeLwYOnq0Bw-xEA15hRF-tKmCK6Io1sIyUSmxR3AkjUIsTu2JgkoU6kZG6nqOPlcHEs6rMt0loN3l3I52TsxAmOCoWQGFocATp2rqc0o-OZR8hvtAjwZi-9NPrIcgiG68byHtWTdkPyh2Dk-SECF5b_6R_Jvn1RtWuIBuQQZi2wwFxYpfZQDOBeJpfHmrVAolhfV1kEFCw1gl2H4-y_hmx14gJd_F8NiGLI4MH_fWvObPDU5gRWYwYle737YP3U-y8ksY8tHYuIs5BJtHTmaU0-syO8fhz0UZrWDmiPTSNnYXTufWu6A8hEUKLSJ43KUIiHSzISvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🟡
افشاگری مدیرعامل کارخانه فولاد مبارکه: دشمن با بیش از ۵۰ موشک مارا هدف قرار دارد و بزرگترین دستاوردش در جنگ همین بود!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/Futball180TV/102301" target="_blank">📅 01:23 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102300">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c4QoVvZtR7Ltlu6FiktPO13dsLOVa5AqrojIfoM_Lb7zOMyOG3_xqZx-DnWmlfI8fxjKbF9uYE9aCOuPQX_jpRnZ-oYkRbATWVIyjkYyZ9A1oT1wu5FTDS4ooU0Jvrb0xn_TjsvDiaGVDIZQCgr259IYckQf9Gh6XPV8bFirxajRzQ8H7rtSaMxE6Wfq10JC5nX20Ei87ppw6zfEngggQCbe1nelvEtN0OZrBH4PnTjiIqVnnMKZvFhSq9V8jqMbjKpObWrX5w9dcT26xWExpfR-ZUQmlJ7bK3dvAN3j00E3Ox0WO6GO1crofdIAwRdXTaQZU0u5d0k98v4LQVxLiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📱
📰
به دستور ایلان‌ماسک، صفحه خبرگزاری تسنیم در اپلیکیشن ایکس(توییتر) مسدود شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/Futball180TV/102300" target="_blank">📅 00:58 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102299">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07fe21feda.mp4?token=QXqmgbYB69HB9ydME9RJctDGj2d2y7HdFzwO2EkBa5E3HshnwV67eqrQpqDcnCeEjqZN--zqihHrc3ufkQAoVAvHIojv6Be1uysGEk4PRFUeRLaczPif1DcippfVgKv2OBCP4r8cUOQicYItXleEmBbDgAJ8PN7KYwQ9xzftsq_puLo8rNSzoQCYBxSO2ZK29NFoPSzrxhfD4LOrJxY5YzEzGPSefHz-PK-y76Fam1o3syuL2MIvGjGl5m7pG9wHhKeAPJPcELuNjGt_SM169ogJa6zowwmER5i2EabpIik8_Thctofopr0bwT_lwzOhM-xTficvhadUMK_H_0kHFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07fe21feda.mp4?token=QXqmgbYB69HB9ydME9RJctDGj2d2y7HdFzwO2EkBa5E3HshnwV67eqrQpqDcnCeEjqZN--zqihHrc3ufkQAoVAvHIojv6Be1uysGEk4PRFUeRLaczPif1DcippfVgKv2OBCP4r8cUOQicYItXleEmBbDgAJ8PN7KYwQ9xzftsq_puLo8rNSzoQCYBxSO2ZK29NFoPSzrxhfD4LOrJxY5YzEzGPSefHz-PK-y76Fam1o3syuL2MIvGjGl5m7pG9wHhKeAPJPcELuNjGt_SM169ogJa6zowwmER5i2EabpIik8_Thctofopr0bwT_lwzOhM-xTficvhadUMK_H_0kHFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❤️
پلن آخر بارسا استفاده از ترشتگن تو خط حمله
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/Futball180TV/102299" target="_blank">📅 00:55 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102298">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q0hzyGjESbWLr6uCzSxPMNxvT3FktrSWM-L3cSXpM5Ia6EpQEdy3cp06YdiRWVR2Ns2oSU22ImIdC2GhLiSbCVr4fBAags7NXyxEqo5FvNEjgM7Zi1DKznjur2ki0rhWH8cKQdF6MzIie_61NtRKIplo1Nuc6rtcNKQ240JZpCJhn0U2nAnPsEmL0dhsQY0WYOVMHkdKhRvI7jWFUlCmUsmTdggeDdio4SkyO10VMloAO8Vp3-YSUP91OH4epAE26pCm1yqKR4GlLrd2iF_AJovCWqMrOPgrfnbXL_NNY5BRAeBcUh3rgi6VeLdrNXnqQ6JLJGcya6lNHaKPh31hTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🇪🇸
په‌په‌آلوارز
:
🔻
مورینیو، وینیسیوس را به عنوان یک عنصر ضروری در رئال مادرید نمی‌داند.
🔻
باشگاه، این بازیکن را مجبور به ترک نخواهد کرد، اما در عین حال، درهای خود را به روی یک پیشنهاد "مناسب" بسته نخواهد کرد.
🔻
همچنین، باشگاه قادر به پرداخت پاداش قرارداد به مبلغ 80 میلیون یورو یا اعطای 80 درصد از حقوق تصویر (حقوق بهره‌برداری تجاری از تصویر) به او نیست.
🏴󠁧󠁢󠁥󠁮󠁧󠁿
از طرفی نمایندگان آرسنال پیشنهاد خود را به‌وکیل وینیسیوس ارائه کرده‌اند و حالا همه‌چیز تحت نظر وینیسیوس برای پذیرش یا رد قرارداد با تیم لندنی است!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/Futball180TV/102298" target="_blank">📅 00:46 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102297">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LECAqGfF6AOEwVOb-PH9WFfIWG-405jUWM-vehBK2c7pEJ5XFzZyIC6-nngOtKv_AOsXViLF-NJdWvsvGvP7NDGrdNZhrtXorSyz8EdD4pZ_8qov5PYzeaLb4PVK041YNAq57YFsmxhMOQOE2zM1f9ObYWtplJz1Yd1Hxs6tZD27pZL_aX9owk3z16lghdjyyZeL6kiC7jqkGuyFhFjzcrpXhi1mHfVhHbnbrn8w9AmQX4oP9k5KT7549Cgam2DhXklejYnY2ByS2421kk9xA2YEnJ2ISSvafdm-4xJoa2cVlCDIoaF3aHe1JpowhW2sQDDyV90f-A1ZP0jpoS3kNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
‼️
🇪🇸
🇩🇪
فلوریان پلتنبرگ: امروز هم توافق میان رئال‌مادرید و لایپزیگ بر سر دیومانده حاصل نشد و مذاکرات به فردا موکول شده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/Futball180TV/102297" target="_blank">📅 00:37 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102296">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a93d51cbc.mp4?token=UJE54Zpkrt8kAtHLRhxiVDvibIzr53rrfebNz7tRe1hKRhMtl9cRIirvK1qf6gD9cSuuAK2ewj6-HXIjddrFq8NlrO7SziXQ8JCgCM7fK6EiEIGclCmO0rISZlz_WMVSFxIGdLjk7I_243BN8WDI6B7PoKeAjBkPtD6HTEWGJBpBp9bBD1d24z90CmWuBMqMr_hil33iMqBKZu6ae_N-Zk2gsRnBvWK_vg3A1p-jr4CqpVYtK0W6mxCY1_IzxfpT1203kG926pLfIKcRe2gw2JAQy320q56zxpK4U0msHKHIBNHZu1WKpG5wCq-uIFmgpt_8QeYAnveCt24n-06ycjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a93d51cbc.mp4?token=UJE54Zpkrt8kAtHLRhxiVDvibIzr53rrfebNz7tRe1hKRhMtl9cRIirvK1qf6gD9cSuuAK2ewj6-HXIjddrFq8NlrO7SziXQ8JCgCM7fK6EiEIGclCmO0rISZlz_WMVSFxIGdLjk7I_243BN8WDI6B7PoKeAjBkPtD6HTEWGJBpBp9bBD1d24z90CmWuBMqMr_hil33iMqBKZu6ae_N-Zk2gsRnBvWK_vg3A1p-jr4CqpVYtK0W6mxCY1_IzxfpT1203kG926pLfIKcRe2gw2JAQy320q56zxpK4U0msHKHIBNHZu1WKpG5wCq-uIFmgpt_8QeYAnveCt24n-06ycjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پشمای اورانگوتان از بدن کوارشما ریخته
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/Futball180TV/102296" target="_blank">📅 00:32 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102295">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd4b353d1e.mp4?token=IBVfq8uhG5DABfEk3OWzuutHX5O59FA5zHqlPMSayDiX-Gp4Bl4I7j7cZDg2x7PoJ-D3-kzvy-8Q3foSmBLJYDeW6pLExR0sCWoaPNTLU5uGuW3JImU6J-oDcTuTs0EdRwNjFSqf1bjzDAW8vv1DV23Yz0_S8Rlk_lHz9EifF0DcIjErI7JlUO7VQ4E362g7BruQYwj0WejYd2FtcmMw1Y8DWK79-wWXnJtxLw_aq8O7jKt24taREqRMeUHO-KW9kUiDWNOz2j09GXq8rQ_nMq8eYKJ-cXmAMyBL_XUlEqt0getnX-B11eW4wZE9CnkHoOj_pE02vAjW6QDrZbLWFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd4b353d1e.mp4?token=IBVfq8uhG5DABfEk3OWzuutHX5O59FA5zHqlPMSayDiX-Gp4Bl4I7j7cZDg2x7PoJ-D3-kzvy-8Q3foSmBLJYDeW6pLExR0sCWoaPNTLU5uGuW3JImU6J-oDcTuTs0EdRwNjFSqf1bjzDAW8vv1DV23Yz0_S8Rlk_lHz9EifF0DcIjErI7JlUO7VQ4E362g7BruQYwj0WejYd2FtcmMw1Y8DWK79-wWXnJtxLw_aq8O7jKt24taREqRMeUHO-KW9kUiDWNOz2j09GXq8rQ_nMq8eYKJ-cXmAMyBL_XUlEqt0getnX-B11eW4wZE9CnkHoOj_pE02vAjW6QDrZbLWFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یامال تو تیک تاک : دوست دخترم خوشگل ترین دختر دنیا با من آماده میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/Futball180TV/102295" target="_blank">📅 00:16 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102294">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🔴
چالش ۳۰ روزه: از صفر تا سود مستمر با فوتبال!  ما یک چالش ۳۰ روزه رو شروع کردیم که توش با تحلیل‌های روزانه و مدیریت ریسک، موجودی حسابمون رو چند برابر کنیم. تمام تحلیل‌ها و فرم‌ها کاملاً رایگان در کانال قرار می‌گیره تا خودت روند سوددهی رو ببینی.
➕
پیش‌بینی…</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/102294" target="_blank">📅 00:16 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102293">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/316f36114d.mp4?token=angLLHhCLclNVcB9TPBqM_x2tmu5FbsbGUoO3dhQytHsUpoY8U2Oo7kD261iWT3YnWE_U6fdmyOf_GNiK-9nE-lbR54mNl0XuIZKJwXgM4BzXWmSS90Sfyl8GQgQq6-VkN4qJaGAV7yTpgeDHDmcqRU4NVzhXXsCvsfT3bW1GsbMlQU5473dKyBADtC3rLRekBfUEBQo6_Jcmp-SqNKb3L_P4g8VVKjJAJtQylSvJpdglooKHvpRgzUr8Sf1MD-Tb02wjD6PsvXpKI8izcNIUdF4SWfbxaTfnBukHz5jELDLVfb1vOA2iUW_7CmVBNQ7uDsg7jjy7dr5u_4x3fQlLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/316f36114d.mp4?token=angLLHhCLclNVcB9TPBqM_x2tmu5FbsbGUoO3dhQytHsUpoY8U2Oo7kD261iWT3YnWE_U6fdmyOf_GNiK-9nE-lbR54mNl0XuIZKJwXgM4BzXWmSS90Sfyl8GQgQq6-VkN4qJaGAV7yTpgeDHDmcqRU4NVzhXXsCvsfT3bW1GsbMlQU5473dKyBADtC3rLRekBfUEBQo6_Jcmp-SqNKb3L_P4g8VVKjJAJtQylSvJpdglooKHvpRgzUr8Sf1MD-Tb02wjD6PsvXpKI8izcNIUdF4SWfbxaTfnBukHz5jELDLVfb1vOA2iUW_7CmVBNQ7uDsg7jjy7dr5u_4x3fQlLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
چالش ۳۰ روزه: از صفر تا سود مستمر با فوتبال!
ما یک چالش ۳۰ روزه رو شروع کردیم که توش با تحلیل‌های روزانه و مدیریت ریسک، موجودی حسابمون رو چند برابر کنیم. تمام تحلیل‌ها و فرم‌ها کاملاً رایگان در کانال قرار می‌گیره تا خودت روند سوددهی رو ببینی.
➕
پیش‌بینی تخصصی بازی‌های دوستانه باشگاهی و تورنمنت‌های معتبر
➕
فرم‌های گلزنی (بله/خیر) و گل بالا/پایین با تحلیل آماری
اگر می‌خوای از روز اول چالش همراه ما باشی، همین الان وارد شو:
🔗
https://t.me/+L5I8ulM6jEc2YmE0</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/Futball180TV/102293" target="_blank">📅 00:16 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102292">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NMnUqGnGEusuOSZn1113_-_KGVYx2nZD-4ttFEOf55iiLkXoB27mxt4-D_kklhoPOmqUVu4qqDve-sFGTHJGF9r8CDyKYkb9m0erpEbRsVZ-oH3MPj2l8IO0D07_sVFqePEL-VLmkgWpuiC5I9BEWJ9E63boNRMRB46fpgXNMtmRQtK6PYmKGizXfh-k4JIO6MkChgp4mAWDAYg1ANyCQwGW4cIaE6ySEb306oRzujy1C5o8OfaL2uYznOt1idSvA2UOCv8906pg7i9urpH5EDONhKDKFy3w__Z1iWMeWnmxcpGoHJTUliB3W3jy3dTVaczXDpiXO8VgSO4NMZY1vA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
فوووووری از پپه آلوارز: مارک بلینگهام (پدر جود بلینگهام) در پایان فصل گذشته با باشگاه رئال مادرید در مورد جدایی پسرش صحبت کرد او دلیل این صحبت رو اختلاف نظر در مسائل ورزشی اعلام کرده بود.
باشگاه اعلام کرده است که جدایی او امکان‌پذیر نیست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/Futball180TV/102292" target="_blank">📅 00:13 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102291">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vK6frZPA-bfpKpf3s-3VvGkklvHhLrmpC3ZvokDbaBDqBO8WfuDwf932897tbMFbB5y-I8qKVfCaju2YQ_l8MkRf0YwYW-ggPP9kN8vJRoe-1S5EaL9QhVIhOdFtqKkJHRXOrNrnZ8vnRF2SZGRA9o9xTZVJVH2_ZTZzmUX2hwChhnLXWSNRZ9Eszo3FrulcUffDB1T4It6foOJBgQruzkuT-OsnMLdrEtYIOfeAQ1wqgGNrPK_nli8C1bmcPNHJZDy5kQ9Bg6kpTb-CLw0DqHl0-hkhLrqnkTuIhfyPxmOoS4NuA1e-rxePjPMUSEarlq4sZzyktpvaYCRO9Vpx9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
🇮🇹
فوری از شبکه DAZN ایتالیا:
استراماچونی از ایران برای هدایت تیم ملی این کشور تا پایان جام جهانی ۲۰۳۰ پیشنهاد رسمی دریافت کرد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/Futball180TV/102291" target="_blank">📅 23:40 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102290">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KWnFUZj6wmMFJtHdRI7iWKPGYdsXL-2Hf3XU7MDiQsgBhRUDeKF-FcBSwjmc5fPN5J0d8JX0XYCaLCvO0Wc0Hu_6eguZOcHObtWMmqOmDmQoSuY5THvUgxkrwPZRIvmdD3t0cheg1M_q6IHC7jMSE3I2LiPlY91LUBLge9Jt0suRQBbXBhQ9Q7XOSEzW_d_SmD4msZF7FHIgleWRCMtkiGp4kBsPfQz1VxMTXgVwMRIIIP_oOMOKbpMTkHyR_ApTYyNKl3JO0Y4qe0iJNEP5WSoQSGVXLRXmEqkXv1j-aVGR4Jzzf-ZGrzeoag9BlNPx7HmNNAcdmC3genLkDe7G2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
فرمین:
این بدترین تابستون زندگیم بود! همه چیز داشت خوب پیش میرفت که مصدوم شدم، اوایل جام جهانی نمیتونستم بازی هارو ببینم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/Futball180TV/102290" target="_blank">📅 23:01 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102289">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bqrzW4HaA7pWDIh0UlNZ6paesKRCA_qDl6lIYkTCFj4ytpm8VeRenFzeEW0e2BnZnkZgaY0BISd4XLnzlf04oPWnt1xnC6Y__bOmmqXsAQSQBgJT2MwlpjHjJ9oU4X6rsWfok1iEa-jA1zJ_jDiBTi6UHC7xMz3rEhAM86DM6HqCIVMR12aI_rhBFQFubrBaSb0mfzZeLtiq_B98Aw75Cmtt3YpdbHd_Xjfh9LPhgVvDyk-FaPcQQaQgbx4URnUPrRFH9N45deNUzXeq0qmaxHKh0RyZFtqpNEJrSek3tFNZZStU8H7opPALIt7nGRzvdv6O7wsjkXJixYsELIvpZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
کیت سوم دورتموند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/Futball180TV/102289" target="_blank">📅 22:34 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102288">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bLNEVSG4NEuJM_J2DhHt7bB0ZHCq2iyM3YTfO4JQqifWJbtNGhMuPXySAh7bPDrjCzvFJJdPiGJvJ6NE_DD5-pKFhagMcHAMxwrL83MGQ5NNjjG4agafVII_u2MZtbou3D3pI1dDO4N8u0U6yeCNXud5Vi2WvFW-k48d_eOTtf1HJKQCUob9dW7EXMboKx383wAA7ngOivxZDK16rZMBvcyJOcPFxrdxP1_C74sdeuRW7AQaJEI2SEfOK6e2p4EKJq0S5uh0VuC4lRhBO6ReBpT5qxG-cR0IYnDXN9ymY6v99JE9zDQRb89WjDlNTBFFDIlsJJ-OSgsjR_lcUrt3RQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید رونالدو چه سیسی گرفته
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/Futball180TV/102288" target="_blank">📅 22:19 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102287">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5b210f5e9.mp4?token=cQg3LoqDFH1V4hIzhh5vo98cEKE6vIZrCBRfR94Lb8Yu-sQOcAjt21bpeuzEMeNuQQMVLnmFQKvqeTQ2I9nt3WiUeZiJCa14-Y7hf96LEHXwNhOQEJN5Lnz0dk_3_qtI5UT0mVP8OAk_XM_38uAk2SLOwNvey0rwUXXrjItd6Tth7E3HwsqhmSlXh5RtgE_N0egIhSHGNvgBNYlalegdwolT4TYxUgKXqz-AYyu4v_KLpVYuXCuC5Lb1j9qx350CSy4oDrcqKZRUR45OOcwoIVQ78KFLT-34k0aHA5vzbVQk5CEhpas0zwvRCa8cUeWzdChHgmG1nLaqAFZ82yk06Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5b210f5e9.mp4?token=cQg3LoqDFH1V4hIzhh5vo98cEKE6vIZrCBRfR94Lb8Yu-sQOcAjt21bpeuzEMeNuQQMVLnmFQKvqeTQ2I9nt3WiUeZiJCa14-Y7hf96LEHXwNhOQEJN5Lnz0dk_3_qtI5UT0mVP8OAk_XM_38uAk2SLOwNvey0rwUXXrjItd6Tth7E3HwsqhmSlXh5RtgE_N0egIhSHGNvgBNYlalegdwolT4TYxUgKXqz-AYyu4v_KLpVYuXCuC5Lb1j9qx350CSy4oDrcqKZRUR45OOcwoIVQ78KFLT-34k0aHA5vzbVQk5CEhpas0zwvRCa8cUeWzdChHgmG1nLaqAFZ82yk06Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
ادعای نادر فریادشیران درباره بیرانوند:
اگر بیرانوند همان متنی را که علیه علی دایی نوشته بود، جلوی من نوشت. نامرد باشم، یک ماشین به او ندهم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/Futball180TV/102287" target="_blank">📅 22:15 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102286">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TGu4OSdKGzSkVcSg0BvjvL3BrGRjrHBhg53C80TwMeaCbPySjcYcvN2L8w-EemJ6LzrlMGbD8kh8wmakNS5zTeZTPmT9QJnL1jpRdoEmwWb9Wslp0Z5OKjDDI2jQVl0terxER3Stz_vs3VvqqyeJkpPkmfukNZttSkhfhhn7tes8Yku0ZCmxfdphm5a3GDEVW33nlI0FBGfgKfwkfK3O8Md8tzO1zztnBVOTUrtzztC05ljy-V7-_OKRZrI0ub7eBSedJ56UqMbPMhu-S7RHQaBes53aFzbQaBYExWvJa824vyk1If_sa8ENr5KHF3hL4eAal4sRQywCPbopI0tv2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇦🇷
فیفا بدلیل نمایش بنر فالکلند در جام جهانی 2026، پرونده انضباطی علیه آرژانتین باز کرده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/102286" target="_blank">📅 21:50 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102285">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb35f99ea4.mp4?token=QCBY0ZxNSlZBuP8pfMRf5-MFHgaYyoKyUmd6NAs8dO2A8acqclOQGM4OLeJozN0o0BBtttQmIA_jt0jgTf2_Ci9SmDdk5mwHkEhTqXJXVQGE7MGB-TzxRPxmOiGjrPpYfRdlflRiTDZ9ZHF76BpvbbC97HYXcl81XHKN434k_Ksoe4qsEe9qGBUk7IBurGI8jEeePulOujy7c7_3f5c59WKqFmPYIFWsz4dj1c1hwkhKyOn9-nGKdjeq59eJtBaM_JPv21RmdUQl4Qd71XPrSfBj78B4dBZFHQoPq6zYjo2AgCGA1P32sgRdO4xW2zBb0sO3Vt2sf9QrxFkbEgn4zQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb35f99ea4.mp4?token=QCBY0ZxNSlZBuP8pfMRf5-MFHgaYyoKyUmd6NAs8dO2A8acqclOQGM4OLeJozN0o0BBtttQmIA_jt0jgTf2_Ci9SmDdk5mwHkEhTqXJXVQGE7MGB-TzxRPxmOiGjrPpYfRdlflRiTDZ9ZHF76BpvbbC97HYXcl81XHKN434k_Ksoe4qsEe9qGBUk7IBurGI8jEeePulOujy7c7_3f5c59WKqFmPYIFWsz4dj1c1hwkhKyOn9-nGKdjeq59eJtBaM_JPv21RmdUQl4Qd71XPrSfBj78B4dBZFHQoPq6zYjo2AgCGA1P32sgRdO4xW2zBb0sO3Vt2sf9QrxFkbEgn4zQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یادی کنیم از روزی که نیمار باعث شد کرک و پر امباپه بریزه:) خودش هم اصلا براش مهم نبود ضربه رو زد بیخیال رفت. امباپه اون پشت داشت جون میداد
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/102285" target="_blank">📅 21:42 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102284">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromچِشم به راهیم</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8732bd386a.mp4?token=XsM5quO5gAn94YTEybQLzMqtup7w5CM9fKvQWiLi9ELM9EA6Ygn2GRgz2WXBxnBRNS7s28dHSmxPJEGhtIT1zBNq7NkgrPidFKhZGU6-RnEalVqQadyQZCmAYvFdqQCOJb6LnEvjDVokrbYWO1yOpOMQV8npME5fouoxKvncmvg_iZ84nl7L3R_C3kXVbUSQDBgQtKD-piy9sOeW8Knpw2Viv2YEtUwbYZ9i_H4dQC1RppBpJJxAdqJ-gTzKJyHrfuQZzLhyeabIrqDnFYGPGNCwvuMyWddPyJEFFanCmZQc5KaVYQHOA26e-Xdy3JMwDcJCfIct9JxysVH7j5W3mQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8732bd386a.mp4?token=XsM5quO5gAn94YTEybQLzMqtup7w5CM9fKvQWiLi9ELM9EA6Ygn2GRgz2WXBxnBRNS7s28dHSmxPJEGhtIT1zBNq7NkgrPidFKhZGU6-RnEalVqQadyQZCmAYvFdqQCOJb6LnEvjDVokrbYWO1yOpOMQV8npME5fouoxKvncmvg_iZ84nl7L3R_C3kXVbUSQDBgQtKD-piy9sOeW8Knpw2Viv2YEtUwbYZ9i_H4dQC1RppBpJJxAdqJ-gTzKJyHrfuQZzLhyeabIrqDnFYGPGNCwvuMyWddPyJEFFanCmZQc5KaVYQHOA26e-Xdy3JMwDcJCfIct9JxysVH7j5W3mQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎦
نذر سفر؛ سهمی کوچک، اثری بزرگ
🔹
در سفر اربعین، اگر صندلی خالی در خودروی شما هست، آن را نذر یک همسفر کنید.
🔹
هم‌سفر شدن با خانواده، دوستان یا هم‌مسیرها، علاوه بر کاهش هزینه‌ها، به روان‌تر شدن تردد و کاهش تعداد خودروها در جاده‌ها کمک می‌کند.
🔹
اربعین، سفر همدلی است؛ و همدلی از همین انتخاب‌های ساده آغاز می‌شود.
#چشم_به_راهیم
#اربعین
#نذر_سفر
#هم_سفری
#سفر_ایمن
#فرهنگ_رانندگی
#سازمان_راهداری_و_حمل_ونقل_جاده_ای
#حمل_ونقل_جاده_ای
🌐
rmto.ir
🌐
141.ir
@Cheshm_Be_Rahim</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/102284" target="_blank">📅 21:42 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102283">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nRb1QXsUFHLEWHKgGz9ejjnzwyT8BMhX3ZJVGSk2ooZORxV5JqVtgWXsCD2WsE-Lx38Ted-atUdjM6NX1rxS7O31XuZ2KS656fiepRIsafRxcGGVFHxDExkh3HPsEqxMfdhQTVxq2vwnAKDOaT-KBmyjUg7z5ejroiqPYyPB-s3Kvu2e9wyF2wxa_1Uq6rRiMvkoXgaGov8UHfIWkZAUP-B3nzMll1DxDZxZqGcnoiw3J_myQ8A-IygzLCOspCPS-phlDJQi37p6Bt8VwACJh8PY8JacC_D1PKB0gFwvqx-a8wo5HbTz1pXbYxUC504U27tXtaL7Mzv2OA-rFEpuwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید جورجینا که بسیار هم پرمحتواست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/102283" target="_blank">📅 21:40 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102282">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sZy7EN3gQoIdliaT9B3_XJ5_SkbpFylp_uTuglXRepOPjNTXxrAQxMiTfFRiQ-g7Hz88LknjsksZ0-BxaRGO298KjBlcmj62KOwWnjkaYKXC_JjggEe-waGBGEwqtGfGwsYaOA1mCO9JhAFCl3m7EzV3B-z-bZ1ScopT2FKBx_9-OeJZ6EW4NYpzJl3L3-YWFyjNd2y8KYyk4y6I2785PX_0ekUZuq-ZPXCyD5cMRMVI97FaTSVsHMgAwm61FxZbaYVa5UEW2ni6_dAdiePvQI_gtWfXT8D_ywIsvDLRgYUjpGLMOP98p6qFGAZP54WB8yMaaLWlDzdR2XXjR0RIGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🔹
کریستیانو رونالدو از زمان پیوستن به النصر تا الان حدود ۶۲۵ میلیون یورو دستمزد و پاداش گرفته!
❗️
در کمتر از ۴ سال، قرارداد رونالدو به یکی از بزرگ‌ترین قراردادهای تاریخ فوتبال تبدیل شده:
✅
حقوق پایه (۳.۵ سال): ۵۹۵ میلیون یورو
✅
پاداش ۱۲۹ گل: ۱۱ میلیون یورو
✅
پاداش ۲۳ پاس گل: ۱ میلیون یورو
✅
دو کفش طلا: ۸.۵ میلیون یورو
✅
پاداش قهرمانی لیگ عربستان: ۸.۵ میلیون یورو
💰
مجموع درآمد:
حدود ۶۲۵ میلیون یورو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/102282" target="_blank">📅 21:20 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102281">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1795b5f8ad.mp4?token=NsOLNpnQ203OcPxBkk5D1mqyRU0tdEC-kplyv-Ff0KRA9QeNFseqIDAg_roMW3FMRNeO2CdnzI_DIfpbnzNwyw_Qsf_J_AZdIu7GIHG8dkja0QLL33WxWi91MR4_mZYADce7cd0cZNoG0k_PoOrjKT8RnYXgVF7GiFZS4AfIe-QuEuJ9fE2QG7zKzzTjsX021p9sma0oPtRpjmbxmBvioamzc3qEmlhBfVBeMceIlUlsaLaK2Wfoh6ES3dVv0ew7btlpHD4LtvI39fjb-B9SQ1kOKSCcPuw1TuXkNBcGlLRKSkJ7YrOgDhNTSiMkZjRf_zAmpGcsAes9gWa8zNvYJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1795b5f8ad.mp4?token=NsOLNpnQ203OcPxBkk5D1mqyRU0tdEC-kplyv-Ff0KRA9QeNFseqIDAg_roMW3FMRNeO2CdnzI_DIfpbnzNwyw_Qsf_J_AZdIu7GIHG8dkja0QLL33WxWi91MR4_mZYADce7cd0cZNoG0k_PoOrjKT8RnYXgVF7GiFZS4AfIe-QuEuJ9fE2QG7zKzzTjsX021p9sma0oPtRpjmbxmBvioamzc3qEmlhBfVBeMceIlUlsaLaK2Wfoh6ES3dVv0ew7btlpHD4LtvI39fjb-B9SQ1kOKSCcPuw1TuXkNBcGlLRKSkJ7YrOgDhNTSiMkZjRf_zAmpGcsAes9gWa8zNvYJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ریوالدو، نابغه‌ی تمام‌عیار
🇧🇷
🔺
پای چپش چوب جادو بود
• هت‌تریک تاریخی به والنسیا؛ قیچی از بیرون محوطه
🔺
جام‌جهانی ۲۰۰۲: معمار خاموشِ قهرمانی برزیل
🔺
وقتی رونالدو و رونالدینیو تیتر می‌شدن، اون بازی رو می‌چرخوند
🔺
توپ طلا، قهرمان اروپا و جهان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/102281" target="_blank">📅 21:01 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102280">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GBf5xocU2cetcuG3rAGZq0o6i8EHCr4_D1-tm_qqHrZWKI4rH0M_z-u9D1wSh9abQFMqIfjv5pPC-OH2XG1w87h9icEuWkIoCu9Qd2aGX8_zM3JAC01JVuDCO_-AWIOUPUybB3w2UVHdAf6f7ez5vY5xJLMZmWgQJsjIw7SZ6sQpjItpR1Ksj5LqQI8P_xCvdBazVAtLMuYJU7P6XmovZaI3n_EuAVfLPZXRC393Sp6-MBSONdAeGgO-vnGoN2ARD0MuksqgB6aHi_SEpLmwGl5fBN5uioWi-e898QA1w4doGm7ann9qYHvuIX_SDwsucWFvHTDcqKgF_KqqxOiCww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
🏴󠁧󠁢󠁥󠁮󠁧󠁿
اووووووف کیت‌جدید منچسترسیتی رو ببینید که قراره دو سه روز دیگه رسما رونمایی بشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/102280" target="_blank">📅 21:01 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102279">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lh0qEx87ZF2ymVipL-BvyZ0qNfkjwBNS8God65tm_YYaSP5vxnFenHuXh31h3tnEzHE2T6TyP6DM5H2VIaUZ-aAn_GuI78Vq7VdWt0VJsbJnLbSCjY40oSPmbht0psbGblGBuJyvT_-8WfWnycnL2tI1e90pFa5SfoufxtQS0tQr5SusDZG-Fl3P6qn5s1pdqr917eSbMs3fF64H-tssC4pef1caGI73GN6r3m9jMDoL8pHgKPsHVBGpFZSugs9bqhdOqWFCKuKtME9F3KR3y8qmoYteAC7N4ATzcyHm4gAzLdPAAdgpfiW4d6y94TjUq0T_I1MMeifEXyGKkMNWaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
⚠️
🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#
فوووری
: رسمی: الی جونیور کروپی گزینه خط حمله بارسا پس از شکستگی استخوان متاتارس پنجم پا تحت عمل جراحی قرار گرفت. مهاجم بورنموث طبق برنامه زمان‌بندی ریکاوری، انتظار میره ۳ تا ۴ ماه از میادین دور باشه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/102279" target="_blank">📅 20:42 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102277">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ogMP2zlOU0aEswDlhSOKx5qkbBuQG490ciCCxENFXNmoEpNwCYYoGUZaqUutMBJOO2E1zHffOpnwL5CjEE_vAE_-3ijhixnMR5l4mWYJii4ViVLy5gR75TkqM9AyQ46bhGzKh1WqNDwjMPB03MNytABMOVlE2ulaXnF2emefxiclzbgNl2nTvOZpoXmqIbGBLIzyCXRFBhbJvequ6fHl4BGk2VYg_sPkYsf37W-f2H4jhe2A9s9k6XfyiGhlhUkgSJOaAFkKL_RPTsu5kciBnKlUq6xBbND68odoWTQzI_a6BML0WCPkBUuDvCVSlFng4G29RFfz5Jdijaxl9jT7_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mjjvfq_WhkLP7R2SLxsr_S_Qn7M7Or5rYzot_67Wxjb43OFaGe1JfbiWd6S7U3jwDDrstAm4nD43nIjPdeRgpmJlUkALqvCoG8l9Ow-75d0q_bhG7eo2B42Zm2nDpFwLu69SnjEqfFhe6UF9dtFsMzNjc4_AWbPnuMBbiyO5JHX-PHGYMkTxJTS5_ZJ-oXeW2nJhJSTftJ6BE3rM39bw6vY2uyQ224Rm2V6LxaST_PDgGxDc5JOwblZRspDlFV-bw6HG8h2wu7ZoFXhQGkwK40j-SWb1owfDNxuVHxY5BJD1LwoMKnpkSHBTDexeZNGW090MqeZodk5mNWVcI1_-lw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
طبق گزارش‌ها، ویکتور گیوکرش، مهاجم آرسنال، ظاهرا سر یک ماجرای ۳۰ هزار دلاری گول خورده؛ گفته میشه به یه مدل اینستاگرامی پول داده بود تا برای دیدنش به لندن بیاد، اما اون به‌جای انگلیس با پول رفته یونان و حتی یه عکس فیک فرستاده تا نشون بده تو راهه. گیوکرش میخواسته این قضیه بی‌سروصدا بمونه، ولی ظاهرا اون مدل برای دوستاش تعریف کرده و ماجرا لو رفته. این اولین بار نیست که زندگی شخصی گیوکرش حاشیه‌ساز میشه؛ قبل‌تر هم شایعاتی درباره ارتباطش با اینفلوئنسر سوفی رین مطرح شده بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/102277" target="_blank">📅 20:40 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102275">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JKf6wm32SwWtoGjW2ED2i4DvkcnFUEa80NZohsT8tECKSwAJe63EL4GM1-KDVmOnJE9hVM3EaXTINg79m1A3gXFJLj4ojXFGC7tuUy5HyFz60bQP-JiferuwM-cRyYMjeS_Dreml6WYz6x_cOVWl3fBZKsz9SSVakdywec4uNQEfBXPLsIDYtYVHN3r8hY8nW2W48NIslKTPsMquAa9SwZvWb-2Kk47JZCjodK4oFFbg8fW5RJcxMeps7cXfQ2mRqR3LRiY1WeCSUeKG0cQhZwXX_E6SehtPyzpLVmNSXZA9vNkfUoogojLoMBMYu36mjtM6GjFnre9X8fmpV4e8Og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uogB6uyAXFaqX77IDkaO1eMgCkqZv6Cgs0956WtgeGrilLHS_gpnUPd8ywEDQ9Id_-YOrjUSu3fIhA5tLinHtcENaCpXx0GV3ELv7kqq7anMQ_mkvUSZqZMkOox2uM6jqoyV4OxYtAPcUFgb1DRWbdA6IlCWvdx5tnPI70qcJfSILUBq2nk4p-nlGE-JrPFzyAlFmnLQQel-sleJQ5S13MQoyU5lJT3rgM0nAHglUMxMAt1KqZrSyzpbcrk3a6h7tbOiZnJ1PJQ2HMdhEoAcxYUStzA4rfshBoL3zAYv7tkBvkl2dj2FS5wPKTOvPE52a5eHyQ61iidJrYXtwAL7nw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎙
پپ گواردیولا درباره لیونل مسی:
من جام‌ها، رکوردها و جوایز زیادی بردم، اما شگفت‌انگیزترین چیزی که تا حالا در زمین فوتبال دیدم، لیونل مسی با توپ زیر پاش بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/102275" target="_blank">📅 20:20 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102274">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kHYLMu6lyW0U91WXJdOj8qyyNEc6ZS2PRxpi0txZXZQyhn6gC6D3R7bCBj3JncGbzj1ioTcpjWgxRdol83VPU1cnlqQa3MsHuEIx_F9BnHUb6Rrdz6-kLd9tBnvFFmq4KXYN7ltJXynYYWbbDSGnCoOfuc_57tPWKNtKc8iWQs8Y5jDxeu453u2-g8-uGkozsnnP4lsDM5SX0A7KOgq1QkpNIYc23wz-4v8hBoijIDLpTMTjDieZ5om-joC1u0v26rkANz2Lt0EBZcTTVtd92LNgTEgE9BOmZBIWkVXTyX1phiU6XdLntOvGRPbr3L7sF9720x0Sk9QubAUO_m4s0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇪🇸
🗞
#فوووووری
از رومانو: بارسلونا به طور قطع نظرش راجب فران‌تورس تغییر کرده و هرجور شده میخوان نگهش دارن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/102274" target="_blank">📅 20:11 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102273">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ubS5ifzuBJXadJDChPiaSwr_UpfIEvAIhPRmuKVeNcceQjVb6kd1auyyX-_36ioQmBouJXadJXuIlwUCEx_oY11d3mRbV742yAlzdt-vq54bXyf8DHaVvIxXAlEgu8ctGJ5ek5_Yyjjd2QKtIWG_GQBZDgdABi83InAW9-BvSSF72ZtNJvab5IMKJuCF1AONMLJKMvWmmZAIZig43Lp2Ijpqftkz_Ybv_0Y8G4e9VDgZmNp_JvGrXt9-1HxDF3JRDT2ClGpSNerfmrUKRXRtM03btUXpN88gsiafqJrYzHjPhZAwBfBUSsLVr2EmOIL7RHnFeBjoJswTZBHaxmAyjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیوفیس کوکوریا مدافع رئال‌مادرید
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/102273" target="_blank">📅 20:05 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102272">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/84ff90fced.mp4?token=onDD3wm5gBQHijpTYBvmd3m11F7WsTtiXLuxSp7-XkOF_WdZCiIBxc6Zi3Whzms8jreno1rtr8erWHpVjhoFdPiFX-hHrgbBFkargCqMXWMwUUIH-1hai3O3SG7bnREx__JWtFx2SLfPF2eTSOwp1bHD8F_XK1VjXiPg6zLk5neYPG02QBeNp6fpIveFPAYSxqFQZccoZ-nA3BppagHR0PIUuCqygwDODxze2J1sf0uGcp0lpc1D9VUwvBOwOZjLteXsZpkUo9iOca6ybFJCm51wjRxbKzYXHjBg6T_GAhXu9SNSDdXsgl7VX3QM7rz_hjVE0RjKuF91o6vGbKEyzZFcfEqanNlivu9DH45Awm2kU4NtCJSfUB4bhdlYEDlXRpW94yHQejPwewQ3mLX6pmPFd2r8aRSWbITdFGrCG7zjLhvYOMyy4xXR4U8XztafkNmDcn1MqfocWOAOBV6JEzdNJZ1Xa-BdBQ18UAdH0oHO5P6AXBR5xCvM09jtxwWSP2kMPeC6v-EnLwHUKQSQjscLy6kQwYrUfsmveYks4zHLnQ-s5YIT7qXHy45dxw2AgfqaBPYFoPSCRM-nRARGsz8BARc6HQhktyirW_ARRJEANIEWthrkWfE_X5d4_OtFZTWUde7Q_r_nS7F1rqjvNIWgE4DKuRkaO6J1_6s58ww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/84ff90fced.mp4?token=onDD3wm5gBQHijpTYBvmd3m11F7WsTtiXLuxSp7-XkOF_WdZCiIBxc6Zi3Whzms8jreno1rtr8erWHpVjhoFdPiFX-hHrgbBFkargCqMXWMwUUIH-1hai3O3SG7bnREx__JWtFx2SLfPF2eTSOwp1bHD8F_XK1VjXiPg6zLk5neYPG02QBeNp6fpIveFPAYSxqFQZccoZ-nA3BppagHR0PIUuCqygwDODxze2J1sf0uGcp0lpc1D9VUwvBOwOZjLteXsZpkUo9iOca6ybFJCm51wjRxbKzYXHjBg6T_GAhXu9SNSDdXsgl7VX3QM7rz_hjVE0RjKuF91o6vGbKEyzZFcfEqanNlivu9DH45Awm2kU4NtCJSfUB4bhdlYEDlXRpW94yHQejPwewQ3mLX6pmPFd2r8aRSWbITdFGrCG7zjLhvYOMyy4xXR4U8XztafkNmDcn1MqfocWOAOBV6JEzdNJZ1Xa-BdBQ18UAdH0oHO5P6AXBR5xCvM09jtxwWSP2kMPeC6v-EnLwHUKQSQjscLy6kQwYrUfsmveYks4zHLnQ-s5YIT7qXHy45dxw2AgfqaBPYFoPSCRM-nRARGsz8BARc6HQhktyirW_ARRJEANIEWthrkWfE_X5d4_OtFZTWUde7Q_r_nS7F1rqjvNIWgE4DKuRkaO6J1_6s58ww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
لیونل مسی:
آنتونلا اجازه نمیده داخل خونه با پسرام با توپ بازی کنم. تناقض‌های زندگی همینه دیگه! من از فوتبال پول درمیارم، ولی حتی نمیتونم داخل خونه فوتبال بازی کنم.
👀
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/102272" target="_blank">📅 20:02 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102271">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tDbQObrMymcxiPryyI8PTixqjbLo13_j0Mfey6pJ57tM7g7HdHxDr-N5pXKbgUsbfGFxbIAyXANBSEZwpnE-_OormRX1NH1piYOXamrYwGmAXn71M9GTlDP2bOICJI7I9KSYdgxw5xrZ_uGjTGOVZ0upcAxTGW-PKlp4y0Yo4QgQOk8MBjaAe0U5-OqpprZ2ep0vw1M71gxe3mJWR0y790_o4kKyDlMTk8pm-LGVV1_tJRt37uNhcMD16PUGrJB7IcPmcL9vC7uOd1v4RuLGFQrKjYdMN_6JHevFkhL-42SsEaPu9WrPb4Xipp1bbmBRU2dsfBUNScfo2nd_B_I7ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
✔️
⚽️
نگاهی به اسکوربوردها
.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/102271" target="_blank">📅 19:51 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102270">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f57a7d2d3f.mp4?token=ZUnpvX4BDiYmhGuoTNW_dJi_oUTxdGyxlAkfggQcM063h-xhBclPt3kaRD86xVMEJuuIv7EQWEWtKiSV1HlHKtDo_PEQv1reZfykctXFIhAMzPcNLjcRAbcHkFZmfyT0wHJUdHqM0yaOX5Fp_GDWi6AB-hPH_uQgoNSODrR5IkSL9bg2ila2y8Y21jIhXhfqGA6KezyFUtEX4XCxK-UD346K131OcFMvGBVMF9gIFBus074Tfp8f1M5BAlMxGzHd4JJgvWEjDGNxI5c40t03k34gShVDsIYLZf7gDe7-bprr-W0sA7o-EjDQy2f2qGv6mgQrghYjrDrw-hmpAcKviA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f57a7d2d3f.mp4?token=ZUnpvX4BDiYmhGuoTNW_dJi_oUTxdGyxlAkfggQcM063h-xhBclPt3kaRD86xVMEJuuIv7EQWEWtKiSV1HlHKtDo_PEQv1reZfykctXFIhAMzPcNLjcRAbcHkFZmfyT0wHJUdHqM0yaOX5Fp_GDWi6AB-hPH_uQgoNSODrR5IkSL9bg2ila2y8Y21jIhXhfqGA6KezyFUtEX4XCxK-UD346K131OcFMvGBVMF9gIFBus074Tfp8f1M5BAlMxGzHd4JJgvWEjDGNxI5c40t03k34gShVDsIYLZf7gDe7-bprr-W0sA7o-EjDQy2f2qGv6mgQrghYjrDrw-hmpAcKviA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
⚽️
دریبل‌زنی در حالت عدم تعادل (Off-Balance Dribbling) در FC 27
.
این ویژگی آن‌قدر اعصاب‌خردکن خواهد بود که ممکن است وادارتان کند بازی را وسط مسابقه ترک کنید!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/102270" target="_blank">📅 19:48 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102269">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7495121486.mp4?token=IXKj-TOjM7ouQ3Ckzs5yRF2gJfaRNoJQ8vMiLVM8U_hrFU1nVqOj1Q3qJhGAuMZh_Y74tOSfQeaZv55bl6il7f2QiiodoRG0wpp16vATLZziWeiBQ5Rn_ARWSTB1q3COKphLgG7pQ58kHOWf6SzQj1jqAD6VO-Feiz3eLqcPT0Z9fDPlIrsz4ss1KefjWTV0TFOf7muJzzD4-U4MFQWcXUZvkUpUbSun_NAgH_9zaAkC3Kr1WwNQ80dBc5tmFNio1K_QC1eslpy5QJYNEHbLbPTufTkRxk_y2dq2SplSDwmwbJZMTENiJNS5Ewhfg_hX20Z17vuYWohcOcnrEd59iw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7495121486.mp4?token=IXKj-TOjM7ouQ3Ckzs5yRF2gJfaRNoJQ8vMiLVM8U_hrFU1nVqOj1Q3qJhGAuMZh_Y74tOSfQeaZv55bl6il7f2QiiodoRG0wpp16vATLZziWeiBQ5Rn_ARWSTB1q3COKphLgG7pQ58kHOWf6SzQj1jqAD6VO-Feiz3eLqcPT0Z9fDPlIrsz4ss1KefjWTV0TFOf7muJzzD4-U4MFQWcXUZvkUpUbSun_NAgH_9zaAkC3Kr1WwNQ80dBc5tmFNio1K_QC1eslpy5QJYNEHbLbPTufTkRxk_y2dq2SplSDwmwbJZMTENiJNS5Ewhfg_hX20Z17vuYWohcOcnrEd59iw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
⚽️
کرنر ها در FC 27
!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/102269" target="_blank">📅 19:45 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102268">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/90a87aed54.mp4?token=qJVMsYr-LJekDvqPkDweRxS7TwFvZq_Pd5UE-A1b_WhsDp276Kcc7j9bEJCtiD5yNp_KztcssnJPZszrCWORPVD_095ldPVM-GtIIvL5RfqaddKvmbNkJKzldp23oqmhiJDTuR651_dmrDre6QIYTlMVFlMrqTALapkaG253fWjDn5a9TTFvmf9tiKIKpix13_liaqQ87HtpoIdQYKxf_mBsb21-HgeTDXoV0TM8jIHzFyaceLn-aMz2a2Fdq6w8P5u_0QRepMYKxm68DWNMgx6cAby0rfij_yIdOn3XNuqrN63gl2XaW3YXo0snR9PyUAGV3f-cQkskDR_wqECd1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/90a87aed54.mp4?token=qJVMsYr-LJekDvqPkDweRxS7TwFvZq_Pd5UE-A1b_WhsDp276Kcc7j9bEJCtiD5yNp_KztcssnJPZszrCWORPVD_095ldPVM-GtIIvL5RfqaddKvmbNkJKzldp23oqmhiJDTuR651_dmrDre6QIYTlMVFlMrqTALapkaG253fWjDn5a9TTFvmf9tiKIKpix13_liaqQ87HtpoIdQYKxf_mBsb21-HgeTDXoV0TM8jIHzFyaceLn-aMz2a2Fdq6w8P5u_0QRepMYKxm68DWNMgx6cAby0rfij_yIdOn3XNuqrN63gl2XaW3YXo0snR9PyUAGV3f-cQkskDR_wqECd1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
⚽️
دفاع دستی در FC 27 دوباره به اوج برگشته است!
✅
‌   رهگیری‌های دستی (Manual Interceptions) بهبود یافته‌اند.
✅
‌   دفاع سایه‌ای دستی (Manual Jockey) بهبود یافته است.
✅
‌ در مقابل، قدرت تکل‌های خودکار (Auto Tackles) کاهش یافته است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/102268" target="_blank">📅 19:41 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102267">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5128380014.mp4?token=uf20Tu6Xs2MYxGFkd51PY2eYzB3WAmuTSBu7fOzWFn2pJE2MA5qpZqMjrnyM8CdoUDGtcPjNqMTUk-iNaW4b8RavVAh73h5NXroqMqnKfk1KKwyLZZgywiZ6B3pJoEXvHefWPIKMeRUpYHaGay-R8u4j7BZ3TgIlbLV3N_iYJUWsOAuCTzT9Q3aUp9S_o12fO-LlFbBOEaa_9V3pQHgEwGEymvchMtH6AhXLJzpSxj2ME3lgGZBU3_bX85-U29OVnMapHHhtJVZzLuYlI9lsMRsTcT9j1E__kmfCNCgLq5T_WB30xLP11ewXzjOCuqekjKJ5YtSELM3CKKJSBVSOYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5128380014.mp4?token=uf20Tu6Xs2MYxGFkd51PY2eYzB3WAmuTSBu7fOzWFn2pJE2MA5qpZqMjrnyM8CdoUDGtcPjNqMTUk-iNaW4b8RavVAh73h5NXroqMqnKfk1KKwyLZZgywiZ6B3pJoEXvHefWPIKMeRUpYHaGay-R8u4j7BZ3TgIlbLV3N_iYJUWsOAuCTzT9Q3aUp9S_o12fO-LlFbBOEaa_9V3pQHgEwGEymvchMtH6AhXLJzpSxj2ME3lgGZBU3_bX85-U29OVnMapHHhtJVZzLuYlI9lsMRsTcT9j1E__kmfCNCgLq5T_WB30xLP11ewXzjOCuqekjKJ5YtSELM3CKKJSBVSOYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🔥
⚽️
#
فوووووووووری
و
#رسسسسسمی
: تررریلرررر گیم پلی FC 27 منتششششر شدددددد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/102267" target="_blank">📅 19:40 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102266">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a8d0459b3.mp4?token=GhzYKQufnV0VacTR3W9Lk16AWR3H4K02Ky3hYmi3Ptuy_2X0TVBKEievzdagIxoVQH6BKxzM4RoeF0TT7tI2mnae-JkcRRutjvWPbN0XxFOgJSaAoei6T9GD2GzD7jjMh5TFeoLuYUSiOKYfN8t8xlLBwapd6QUtP7X91zvNICgsJAvi7wcFotp5jYsChmSPChCkhxu1J-HfbHPnwupYNb1K8-H6v3bM5bihFORLI6IkeVcAW_MnJtIv-I4FhuaF2eZeOs47GHYdQ5NI_ypW9vNcC_cxvjCCNOULEgB8bo4j42kS7_nuBDUjfqSPH3e8PTXYcmNy6Y_v93TzyUihnoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a8d0459b3.mp4?token=GhzYKQufnV0VacTR3W9Lk16AWR3H4K02Ky3hYmi3Ptuy_2X0TVBKEievzdagIxoVQH6BKxzM4RoeF0TT7tI2mnae-JkcRRutjvWPbN0XxFOgJSaAoei6T9GD2GzD7jjMh5TFeoLuYUSiOKYfN8t8xlLBwapd6QUtP7X91zvNICgsJAvi7wcFotp5jYsChmSPChCkhxu1J-HfbHPnwupYNb1K8-H6v3bM5bihFORLI6IkeVcAW_MnJtIv-I4FhuaF2eZeOs47GHYdQ5NI_ypW9vNcC_cxvjCCNOULEgB8bo4j42kS7_nuBDUjfqSPH3e8PTXYcmNy6Y_v93TzyUihnoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
روایت جالب مجید «قصه‌های مجید»:
وقتی ۱۵ ساله که بودم، تنها از اصفهان به تهران می‌رفتم تا بازی‌های آسیایی تنها تیم دو ستاره فوتبال ایران (استقلال) را ببینم. در ورزشگاه یک سرود می‌خواندیم که آن زمان غیرمجاز بود و البته خیلی کیف می‌داد؛ آهنگ تنگ غروب سیاوش قمیشی…
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/102266" target="_blank">📅 19:20 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102265">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NTR3sdkUSbSc5TXhRZfZpEN3kOC9aLvbm15NEbam6QioMh_EoJ4FIsqA1lvSNWwiLOzOUl9jW9udCqDa7cnTczQaw2KUcp5iXzKvSG8yz3OeJ9P6_4i49C1T7SApXm41D6KN_haLzlorMMLCeglyeDmp_72HE7f2dC2yVzPH-JntcJDOoGDllbjVlhaUPhmd8XmY48IHPnGkc1B6aTtJQm0uovhkzhwbMkIdNwE99M9j8URDVTstDrEDHTDjkyxEesl5G2kg7EgLVClt-9YxBS-TSJ5q7xgXNyWTHkIPAW7XB7uc386H1eSLBRDoDRGGEFxiNjpNmX3UFb-ay2nQIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
🟢
تلاش‌های علیرضا دبیر برای حضور نکونام در پیکان هم جواب نداد و ساکت‌الهامی سرمربی این تیم شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/102265" target="_blank">📅 19:18 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102264">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6bcb41b861.mp4?token=K6wfHaasOg4BGwx498fn1x3WzzvNms0r1EtNsqL5qYRYD4Ya68Z9-qYM_-RRHaWJHNnGkm6Ej5gl-t0gtHU2oe6pud81jfoguyFkptGsjA8lLMe3N2kSt2Zwc0FebOEilBFT-WaDscBBU0Tv-Vzuknw7xx51ZyzDpXnN70O8NW2cLrsZvf5PVNGRKbrZXvpr9uul5rAW1hRn6rX7JLmIdw_Dngv-eYC27WPjVa-_g-eBRaGws4nqs8b20xVZXmomyiqSu0NYz8vV6jBjM4FQy6Oi6BrtHDpGgdUOFffwZodwDMT2-HvQIWRlP_KLP2TnqSpgpcqE0B-x59HoxnFssg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6bcb41b861.mp4?token=K6wfHaasOg4BGwx498fn1x3WzzvNms0r1EtNsqL5qYRYD4Ya68Z9-qYM_-RRHaWJHNnGkm6Ej5gl-t0gtHU2oe6pud81jfoguyFkptGsjA8lLMe3N2kSt2Zwc0FebOEilBFT-WaDscBBU0Tv-Vzuknw7xx51ZyzDpXnN70O8NW2cLrsZvf5PVNGRKbrZXvpr9uul5rAW1hRn6rX7JLmIdw_Dngv-eYC27WPjVa-_g-eBRaGws4nqs8b20xVZXmomyiqSu0NYz8vV6jBjM4FQy6Oi6BrtHDpGgdUOFffwZodwDMT2-HvQIWRlP_KLP2TnqSpgpcqE0B-x59HoxnFssg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
🔻
داستان پسری که دنیا او را به حال خود رها کرد، تراژدی تلخ زندگی ماریو بالوتلی
🔺
ماریو بالوتلی در ۳ سالگی به دلیل مشکلات مالی از خانواده بیولوژیکی‌اش جدا شد و توسط یک خانواده ایتالیایی بزرگ شد. اما کودکی سختی داشت و به خاطر رنگ پوستش در مدرسه مورد تمسخر قرار می‌گرفت؛ حتی مدتی فکر می‌کرد با شستن دست‌هایش می‌تواند رنگ پوستش را تغییر دهد.
🔺
سال‌ها بعد همان کودک تبدیل به ستاره‌ای بزرگ شد و به اینتر میلان رسید. اما وقتی مشهور شد، خانواده بیولوژیکی‌اش دوباره سراغش آمدند و ادعا کردند می‌خواهند رابطه‌شان را شروع کنند.
🔺
بالوتلی با ناراحتی گفت: «وقتی هیچ‌کس نبودم، کجا بودید؟ حالا که معروف شده‌ام، همه یادشان افتاده من پسرشان هستم.» داستان او، روایت پسری است که با طرد شدن و تبعیض جنگید و دردهایش را به انگیزه‌ای برای موفقیت تبدیل کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/102264" target="_blank">📅 19:03 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102259">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y5EvHmmuHhwts2it3ZPznzxNxdw-LxlUjqPQQV62-LnGL2ijwcqZkf6z7mocIoBaT0B45_06kVPAlvC5Rqso_ezJtoJG_Mxqfk9lRwaHRtMuq8JWExh3I0uuKpeYPPA-bhvklMVGb5icv6qu3dQV6uVg0nKXfsUVHjdwEEO3XSux38IQaa2Kj4-RnvNEasfFpGmpg5EUGjdNHqi5r3wgu6DcZoaxBFnmYIcTUjFYJ5CE_HB7JovwkTDj37y59oCZNTUWUCm8w9QVWWfZf4K3i2pwo8ZUJCSVAfK4f05-qfN6XPNbjDXsA598J2XxpBAaJ1enbNvcUUpAn7IPKmWz0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🔵
می‌دونستید؟
چلسی در سال ۲۰۱۴ با ژوزه مورینیو به جذب لیونل مسی نزدیک شده بود. گفته میشه آبی‌ها آماده پرداخت ۲۵۰ میلیون یورو بودن و حتی با اطرافیان و وکلای مسی مذاکره کردن تا او رو به لیگ برتر بیارن.
اما مسی و خانواده‌اش تصمیم گرفتن در بارسلونا بمونن، چون این باشگاه برای او چیزی فراتر از فوتبال بود. تلاش رومن آبراموویچ هم در نهایت بی‌نتیجه موند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/102259" target="_blank">📅 18:20 · 07 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
