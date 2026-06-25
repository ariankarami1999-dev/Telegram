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
<img src="https://cdn4.telesco.pe/file/vJM0Blj1ZfLHKPSPvru6ho7JvClCvqDsL9rl70_CST0BTh_oGY_MYQDHaRV5zSg6Pi2EGW_soVY9I8NqyMV2PSRHe7IPmaKGoK_QX8wUbw_-5V-QVa-oIniKWX5Ka5_sNn8ABdi8lTgEQcBIYvXDx3BoMLS-6-vo8W5Wj2B4DdJCzHjUGgb09lMgsEyNqrahyZB9KyV5JHrE51G_kmlOlCYMrksorM0oDbcUVzS2mQPzuJcmLTCM5mOmTc385MsjMIvAwokZBi_NFKANFd8ob7rJGx4V_E6ZdTc8LkNG1oLbFpf2Twf3CHDwf6DrDGxxmtd4gPLQNhQsUbdsxiPG5Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 318K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-04 21:39:50</div>
<hr>

<div class="tg-post" id="msg-24312">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lpi2wj3hQy4a1-8bHosTb0WESfuAt7ttdpNTjiSP2hdNxVO1KJrweoZdFESvvjmfIPAuZpHD4CYC6tHd4CusaOZQt2nlxlYAOtLarqF7QVhFfiAX_7jNXGJilHOSmorNNzDxoO_Hi1A7QMxpY7sR7uE1eHG8Irpm8YNlNOMqnCrAX-R_5qqmRr3s6fzELqBhtB33Ee7YD0srkr163igbVobehCqYGauagTdHhKlB8jdeMJlMrieO9bALnKdN0sA6X6-J_ZAzSRhSf3iG7JF44fIwZa2B6NWWYkNTC91GZCJD2sIPsJwL-ZyMlRPu5qVOriBiSLEcJsTC9giWoyh6Kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
موعودبنیادی‌فربعنوان‌داور وسط و وحید کاطمی بعنوان داور اتاقVARدیدار پرسپولیس و چادرملو در تورنمنت سه‌جانبه انتخابی سهمیه آسیا انتخاب شدند. این دیدار فردا جمعه ساعت 18:45 برگزار می‌شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 6.07K · <a href="https://t.me/persiana_Soccer/24312" target="_blank">📅 21:26 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24310">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RmyOoFANsiTVZjgBInoOoMGwUtF-6lxQW8_HORejoxJ2aoHpIuDKHj9Q_ZZxk3GJSX2c8RladVyvmAjBrcUyiLRTY6x3ZmOc3A7zGpqSh5qYorubvQR1xl2kkMpFXHAzKgqC8_qVc_AB6ccMgtRxVb1Zz43xcPMBpLOW5Nj5Q0N_Er2VVhIuM_LJMx81ojV5RKm0AbM8B71QuKW_a0SY8O3fQYg-Uu_ol7oA2ArKq-LbGwTZjr05GqsMJa26o80QRLr0o3aDwvxv6fCxxLgnDPfrpHNQqVdfUCgVjkyKbrHAwV_dUyVKGppOGidMtlEmNrZ0HI_8dsx8_LbEMHO9RQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AET_kiXQx0WNOyqJWAd_5GVVWc8R9atSbGwM4slDFG-TVmk9Hz-KhDO4qMdg2neRYGrIYR-YHGFi29sfaVWNdsSyI10zege8hsMaC4UwlGdfi8f5HxUsatKT_iajIT70IgFTPKVQamrHCC6KqiR_5hc0G_dpCEJSWcwNqcPgkZkEjh1K2SjtwxTovEiRXtM0_yTN3TnXRgPAnwAD-s4xs8rXpPBqUq2sqb-29sWd7BTLyZuyKPcY8iu9wJQi7736fa7RTEAmV1ZpH6Ii89WXOB-GQA5G_MnBaNZ55KajBiWus8Pa-BBkNtH1zNH9Nh-olg9yrLPMablQQpVxutHNEQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇹
🇧🇷
#تکمیلی؛ بازیکنیکه‌فقط برای کشورش خوب باشه ولی‌برای‌باشگاهش نه رو دیده بودیم. بازیکنی‌که فقط برای باشگاهش‌خوب باشه ولی برای کشورش نه رو هم‌دیده‌بودیم. ولی بازیکنی که فقط برای یه مربی خوب بوده باشه و زیر دست بقیه زاییده باشه ندیده بودیم که وینیسیوس جونیور…</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/persiana_Soccer/24310" target="_blank">📅 21:08 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24309">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iSYn7-ioeRIbJ_T_jRilYuqa6W8KDFG1Tpt2IgplubbzNKMahKRqbVEazhx-QYXELiQvvbuTYj1HI8wcBrWlOqUzzAqbxhVcrZH6auP0ZUyydIL04nBl0kWpZfAaF3nUr2OOQfPHt9NiVHXAyj7RjjB2u_UB6vRgEQnWuadZB8tkrusPBP7xxSXHIoEnaMkFjB0nUeWfjgInmcJbr12W_prep1bZ6FUsNWjFS81_vjSV5zi4GlLyT--V-b6gNckgfDqTa-_zKbxxcIQ0Xb-KwyzRS5S0FGlNRVniuf2KxIqnFt6LooorNBAX29wnXA8wKvUWDLl93x08PsIoXCY2TQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کواکو بونسام جادوگرغنایی: حالاهری‌کین کاملا آزاده که گل بزنه، من اصلا دشمن هری کین نیستم، خودم بزودی بچه‌دارمیشم و اسمشو کین میزارم.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/persiana_Soccer/24309" target="_blank">📅 20:42 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24308">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m9IeFauLZau5llPLwpXgjCvaGhvIzIcgkvlV2UI40J_ogERkzb7S7useYuDlE2rgTmxie4-tanOSc_tVd5wfH0Ylh5vamZ6w74GBKcefEUIP454DxIk3_cHc5LTWCfII-HWlX3nCTz-62sybsh9NFx1D5Wwa_8DntYf66O2qXDi2EXhN_myD4iVFlGbjD804FovZJlnePZWGp0A27-0fVGXtQqXBW_ZhontNlNZr-FfVLZirKClnGk7lgl6jokloKA7b4XrZYWSWuhLkeQdbTdjUyrUjduocxUMd0WVDMWXvRyETt2Q3mVZuN2e8vE5H1eP11lFATdYDD74XDJHobw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌دوم لیگ ملت‌های والیبال؛ ترکیب تیم ملی والیبال ایران مقابل آمریکا؛ساعت 18:30 از پرشیانا.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/persiana_Soccer/24308" target="_blank">📅 20:27 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24307">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mfHICObVCv37RTvgM4kAwP9oF3RA7NBqz1NQwAqyewVp8yDJie2oBG6qNkn4obQCJYja7nO_pZtF49w3lDzt8WY2DGjkadIGuhk--oMyjl5g5olbFl04wDDfOwbr8UnLI33qOKjVOkIu8yJWa2d5ajQRbLRXpUdBw-J_o6uqFRNSvyH6jP7bGhu77EOJWikME42vviykQ7mlygtFNdBdxjvyCQsexwDcZTHGXr0b9vq6lVjJxnhZ0XUnmjqxrMFT5IsxTccVH3KhUJycuPhwZWu2k6AolPUVEZjmsQ4OkGZTjwQof1Z7wArZ3AqUV8wMcfzAWlcclgsnwBwLEOHi0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
عملکردخیره‌کننده وینیسیوس‌جونیور در مرحله گروهی‌جام‌جهانی2026: سه بازی سه جایزه بهترین بازیکن‌زمین؛ بازی اول یه گل زد و مانع باخت تیمش شد. بازی دوم یه گل و یه پاس گل داد و سه امتیاز رو برای تیمش گرفت. بازی آخر هم دبل کرد و تیم روصدرنشین گروهش کرد و برد مرحله…</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/persiana_Soccer/24307" target="_blank">📅 20:22 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24306">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/992e363cb7.mp4?token=nKAp3VJ4_SQV7YBGFuen6ocw0VUhUQawJsowb0BHgKuGfi71YKG2ugu7k6rrQvTf5kLyEx3y391V9Zt7L5Y3UqVRILvXz_VT4HYRTSDja9xiY-ejz9X7CbpXPNmvBAGqsFrfl-qnn_LOk4n8qz7m5oK8Y9TJ6IJHub2_a4s_oMFtvckW9OA1KRPMnu5y2DOifQ8Br8mhOsidQnYiuI7rFIKTmBs_81sbFaMrHrCtz4LWFI2VHK3nohPydyAiLSFKemRQWhKIm09BM1wFMJJipi3tAmeEF6lrwzAkn_Os42GaWTxxCQKkyLT-GXRGKT14qGFpXb7k-rAJBX8-MBiu9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/992e363cb7.mp4?token=nKAp3VJ4_SQV7YBGFuen6ocw0VUhUQawJsowb0BHgKuGfi71YKG2ugu7k6rrQvTf5kLyEx3y391V9Zt7L5Y3UqVRILvXz_VT4HYRTSDja9xiY-ejz9X7CbpXPNmvBAGqsFrfl-qnn_LOk4n8qz7m5oK8Y9TJ6IJHub2_a4s_oMFtvckW9OA1KRPMnu5y2DOifQ8Br8mhOsidQnYiuI7rFIKTmBs_81sbFaMrHrCtz4LWFI2VHK3nohPydyAiLSFKemRQWhKIm09BM1wFMJJipi3tAmeEF6lrwzAkn_Os42GaWTxxCQKkyLT-GXRGKT14qGFpXb7k-rAJBX8-MBiu9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
از زیبایی‌های فوتبال و جام‌جهانی 2026
؛ وقتی میگیم‌فوتبال‌فراتر از یه ورزشه دقیقا منظورمون اینه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/persiana_Soccer/24306" target="_blank">📅 20:13 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24305">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qYA5P33ktXDECMQX1iNTLGok_Z0A-gxXU-Q78mahS4CowZrcmh9VejW0kPOPotwmsn0rcr4X0hxxOiOcbYJpm6Be0-NX_CB_rc1Ibu1XD0_ctybh-UoLpNKdgletRYdrYuWCy5Gw6o-tvB7JhA1ClPccZQBp75AUfEzYngE7MpAjd78uB98Bpic6kVrw44bKu8Ks317GthZJHtwo99Zg-8yPsOnRl0ptaaOSC45YCHV7bQ3J7G5v-W0WMGYd50bI4LV7bVR9Ukn-T6wh7Y7ZuAnghi7CsrRdNKhCSBcwkUtodlSJGr3bl2S-8WxbAnofSPl8A1S7fRXH7txH7exlnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کازویوشی میورا 58 ساله میخواد رکوردشکنی خود را تاچهل‌ویکمین‌فصلش با فوکوشیما ادامه بده و بار دیگر بازنشستگی‌اش را به تعویق بیندازه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/persiana_Soccer/24305" target="_blank">📅 19:58 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24304">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BkCZCc_YUJBZ3EXANApcIeJb8nvbvqIDv3ua7JgNdqwV_fxRqKs6kPkFmgq8BjVv7W55IpiQTBD1lwaglqY5qfY6ydbi7r8S7howUpEqlGnoicKA4k6wCshRHfJMXMiAF81AR841msmKWa9amJlQEp-_u0-mTiIoLnMvgXgw7cCHvz3d6exAEZGVw707wPfm5G5V6szE9Z1rbn6OdCWv_UjDIT7Dm1AUthUeRCQ-lt47VwyAharaimzjw8zpj2eMNwWvvHnbakwE3IgkEUyz2ClEFd25qBp-cHH4jiBkPs8fYiXy9Ssc6TrDu24OLdutwCLGX3P9Eg34T_Nx9s3NDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ رونمایی‌دقیق‌از رقم‌قرارداد عجیب محمد دانشگر 33 ساله‌باشگاه‌تراکتور تبریز: فصل اول رقم پایه قرارداد 85 میلیارد تومان توافق شده‌‌. فصل دوم رقم پایه قرارداد 105 میلیارد تومان توافق شده. همین هفته میره دفترمحمدرضازنوزی رسمی میبنده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/persiana_Soccer/24304" target="_blank">📅 19:40 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24303">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sBNw2gbBa6C-EPgtWczg6q8iPoRNiUDEBRouFUMkrufCF6TqDVOkFSu6QtqxBSP_M4Omf7wxYYZa-WyU-zqIdVpiH5_6jEFHDnAZ_JrfKXa01AI6a16RpYkfC-bA3p1elQarX4teLL5P9QACZ-9jUVH-iod14gMqVBlnIqSM7MprPlxPcaUChJWaHVRjXr4kf4jAJ3OIrjqcbERQqvZ_gVAnJurD6RMt042SMQf_0bty5bx5ZPXB52jIzTChll_nnSwure7aIKN-P9mEqhqMyeMTRwMGXFnSQdHwN86iFnCm4cydShwY01VzAu-JJyd4uHfo73C49vHarWbITPpXRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇹🇷
🇨🇲
#نقل‌انتقالات|بااتمام قرارداد قرضی‌اش با باشگاه ترابزون‌اسپور؛ آندره اونانا گلر کامرونی تیم منچستر یونایتد رسما به جمع شیاطین سرخ برگشت تا مایکل کریک نظر نهایی خود را در این باره بدهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/persiana_Soccer/24303" target="_blank">📅 19:28 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24302">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/895e84fb44.mp4?token=Y9TEVFt7jj-gUU1VGn0uu2HigtjNhfmu6FeKU7BaOI9Q3lOm2yuoNwmQHwqyCgRjDTGwMcQOXXHOBJGaU1d80NBB3BMnEGjW3F_EetIQZHqeHj6Q8Z9fz8RGr1XZZh3qyTiU8E25Yh8zTf-llh7_9mYPXBA3x0RI6tcJsTSeUPq_6_3qpkmcEAwXO2_ja83sZg8oVqZhGb4XH1TiM9pscxcAiGt4KJJ6LU2b8iuIojYXAd8lBX4BS6ZkA2jwfsppB6qfRfjfUAZcQBlltV7OOKC53j5EAaIRD1fCJw2eQT9i2Gr3Tze-gBZ1DJ1MqsFZwP3DshgB3-KjBR3g5iEj4YSYnaNsZVtXm2Hf6UZCrHSRVZfTKuqyGKike6HBgGiBYTcfnz2_PYboJodZheApEsDAnIFLcJEhHDb63wJmNYZpxKctxER3AguhEmSwY8eVHURMZPUJ0iRsMSMHfAPrJEAbTHhuDzZdYldUK6QJkACHzhZI8nmOMTuDmihNVp5CEe7KluCCCCbQAZFMFjN7aqR7w8UqMBiBTHa3KXUHZkLcjOvEmD5Ka8Gne_giK59zwEWMDNW-Cy7mJ_iMZLgWEUpSr0R1h5VtPH-c9Vg-6lrIL2Q4aUutie_yzUA4j46wvSKu74UfYwIaAcUqZM6wdVj7ZU89q1Bf4iObIUUCyFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/895e84fb44.mp4?token=Y9TEVFt7jj-gUU1VGn0uu2HigtjNhfmu6FeKU7BaOI9Q3lOm2yuoNwmQHwqyCgRjDTGwMcQOXXHOBJGaU1d80NBB3BMnEGjW3F_EetIQZHqeHj6Q8Z9fz8RGr1XZZh3qyTiU8E25Yh8zTf-llh7_9mYPXBA3x0RI6tcJsTSeUPq_6_3qpkmcEAwXO2_ja83sZg8oVqZhGb4XH1TiM9pscxcAiGt4KJJ6LU2b8iuIojYXAd8lBX4BS6ZkA2jwfsppB6qfRfjfUAZcQBlltV7OOKC53j5EAaIRD1fCJw2eQT9i2Gr3Tze-gBZ1DJ1MqsFZwP3DshgB3-KjBR3g5iEj4YSYnaNsZVtXm2Hf6UZCrHSRVZfTKuqyGKike6HBgGiBYTcfnz2_PYboJodZheApEsDAnIFLcJEhHDb63wJmNYZpxKctxER3AguhEmSwY8eVHURMZPUJ0iRsMSMHfAPrJEAbTHhuDzZdYldUK6QJkACHzhZI8nmOMTuDmihNVp5CEe7KluCCCCbQAZFMFjN7aqR7w8UqMBiBTHa3KXUHZkLcjOvEmD5Ka8Gne_giK59zwEWMDNW-Cy7mJ_iMZLgWEUpSr0R1h5VtPH-c9Vg-6lrIL2Q4aUutie_yzUA4j46wvSKu74UfYwIaAcUqZM6wdVj7ZU89q1Bf4iObIUUCyFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇩🇪
روایتی‌ جالب‌از زندگی سخت و باور نکردنی دنیز اونداف ستاره کُرد تبار 29 ساله تیم ملی المان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/persiana_Soccer/24302" target="_blank">📅 19:23 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24301">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NydwSm1lZnoCbhGDg3yJJVsWGWFfEIOc3BaIUJF6r2MtVyJxj33akODBrt0aNhxT3tVAxsEodEuottazk_4EyCogzcbygF7d8N1HqJR2yGW3mFUqwUR30lumXuCr00oD30OmKkdv2mj368uHZ800z2UqgydzZuoP6Vuhn5i_1ANuLohfa_JWuGtBLgk7VLwhl8ETrfuLJxqnKYBsgeV2BLxXLdD8UZpw1fSVWPMRtDLnPm2jryu7F01LVig31asMYTWEMSD7pvJ4ZddwgvhNVribuT6pqwmApsZD4tUwRUckYbpT3A8qkl5ao8FUNIHEqfx-fRI44aBf-xyOCvERwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
اگه پرتغال درهفته سوم کلمبیا رو ببره در مرحله یک سی‌ودوم بمصاف پاراگوئه میره، بعد بلژیک و اگه ببره دریک‌چهارم‌نهایی با آرژانتین بازی میکنه. اما اگه ببازه یا حتی‌مساوی‌کنه انگلیس، فرانسه و اسپانیا در مرحله حذفی رقابت ها در انتظارش خواهند بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/persiana_Soccer/24301" target="_blank">📅 19:23 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24300">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/E53bu3FewOeLDicpOcTByDelbj7quZCGqnqHjaNuIpdq6lwcaHxilwNfnlhI5fpjm1NEMZEeLmkyzErKe1IR76M9-1ZkFvs0RxRCH2e0Uw5pBNNE_E7gsfVmBzCimKXOV3CkkzGlUqZQQSp8xirV2xs-SqxCUuqaSi5d_4EyUHPIfQQG_E3hW_34ygj7uJeT_odKwTeKxGD8_51EoVD_yzY-ZqxOeFyjMvqwEDwUWFgGa-DbjhhdVIahTif9JUA6iRN_cizshPHeCMe60v72DnWpslSfecVeQQUMQpEfsXLp3t_t48ETX2gMUBaelO2r5Zj3TtaTrqqHjx4E7PPuXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😮
جذابیت‌پیشبینی‌مسابقات‌جام‌جهانی را با بونوس های لنز بت تجربه کن
🔄
☄️
بونوس خوش آمدگویی
🔤
0️⃣
0️⃣
2️⃣
💯
بونوس روزانه ورزشی
🔣
0️⃣
0️⃣
1️⃣
💯
بونوس کازینو
🔤
0️⃣
0️⃣
1️⃣
🔒
کد هدیه چرخش رایگان بعد از اولین واریز
📣
بونوسهای‌باورنکردنی‌لویالتی امتیاز وفاداری برای کاربران فعال سایت
💱
کش بک هفتگی
🔤
0️⃣
3️⃣
💳
کارت به کارت آنلاین و تمامی ارزهای دیجیتال
💬
🪙
واریز و برداشت آنی جوایز
👛
📱
@
lenzbet_official
🌐
https://www.lenzbet.cloud</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/persiana_Soccer/24300" target="_blank">📅 19:23 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24299">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vCnRBN80NdKFoeqUElnJWDig1T5MpvDAucp02BrpOyG-uDu-Lvp6_aSHYyPk4TwaETZekJn8W68EHK9xUsXM81B0WXwBw5K3s90CPvtPIP5PI8gyDAIjdFxtQQKhFEDvqMSSp-kXDtaU4d44x6Bj0Rc6hifc_sg9B5wFlM1LfFw3optASqNRU1WK0tPHiA9LPD7QGiePq_W3IPm_B4gpQ8S89vnIFvQmkbqJ6ZTvSjWkERvNHUR9fT_4Ih8Mg78Ium8vhzkxZ-qUcIf9sj_eFhlSBIBLIRE0aa5xCLWbyl4zmBpX-pZ33vxb09c-ebjvB20Dk8vZPcupnaAoCtWLUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
⚪️
اگه‌تیم‌فوتبال ایران در پایان مرحله گروهی صدرنشین بشه مرحله حذفی به مصاف عربستان یا کیپ ورد میرسه. اگه دوم بشه استرالیا یا پاراگوئه حریفشه. اگه بعنوان تیم سوم بره بالا کارش سخت میشه و باید به مصاف تیم فرانسه یا کانادا بره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/persiana_Soccer/24299" target="_blank">📅 18:54 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24298">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qeofOteOtfv49iTbiKDtICYaQiJBC3hyj5b3fhWkYi4JCArfmK9DrCChGNheYmn0xoHORqPQeQ-F8oEPyGaUbpwWGvizrnu-3pQlc1IxJI2Vl5b9XAaRLcJfsgYOWHPubl45MAM0oJsnmGmF5131ggSW_dhzDPuXAf_DENpdoY4Wed1jlwdnAvvWauYvQ9l8CAtpHKiYxH9EKgVZA1Ouez5GXhjJMxA4c6k9tylie200a4XoMMHJTkT_-D5uIs3hjAsdzZhWBjxApm22coVqeAShNY7alkpk1ceLHbDk_el51sc4VFpy-1RK2j8xDWs8i_zTJqJ8lY4d7EOE_DgTFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دیماریزیو: رئال‌مادریدمیخواد بند فسخ قرارداد 60میلیون‌یورویی‌ نیکوپاز روبرای پیوستن‌به‌ تیم‌های لیگ‌جزیره صادر کنه. مورینیو گفته مشکلی با جدایی قطعی نیکو پاز نداره!!! دقیقا اتفاقی که برای اودگارد رخ داد و چند سال بعد رئال برای جذبش اقدام کرد و آرسنال گفت…</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/persiana_Soccer/24298" target="_blank">📅 18:47 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24297">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qk8i4dZtDd6iJlaer3xQlAV6VrJId0JPG0eajbN7pXsOOsAHARA6oY7EebsY0WeNeNoIp88_OD8De8jxCy5JRd6188BDeSw1pvr9vNlP-gl_sA-BR7BlPk3bsPQcsiKKhw6abAVw_krNfBw2PcZEEaaGeUd8jn337EPUbKD_OU8nhMsS7yOA0MNkSfu_NdPXvo_aTpTGek-WC540_-El58pNAHP7_pHmy1fbyFDGGHVGm9Fp98UCUAUhldy2yP4xF3Gt1P6JWfOCzhOCv8r1AVTiI5iW-0ff808iPc6u5mzOGbTSq0Ui5BQGRXVkz08kLOBX_8ZrgJhA8S-FOkWBdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
کول‌پالمر تو یه‌پروژه‌دریایی تو صربستان 10 میلیون یورو سرمایه‌گذاری کرده ولی بعدش فهمیده صربستان دریا نداره و ازش کلاهبرداری شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/persiana_Soccer/24297" target="_blank">📅 18:26 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24296">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GASIdFZS5MNdEioErClfyuaWKrtUPR6dM0V7sM_SadiQc19NW3d4vdHv-fzzGJRoNaSQ2oTLNP_oU_ubV0rh0sHVgZavOvVzYyFeSUKkYuYUrn9BB3b3LmIVCkRhJl_qWsl7jtSJ6kwv1uQ6NOJpizNCyABNsgCc1glWiLYZ3ISY7193kFEZzO-DeTTZSTdVmQzbsOVw2IieHsI0qtstWJTvdZmBbQLeWtZ7RbJWRY4EMOGbkDsLcISM5_NNilpT-eEYKwbWTWsoHfJlClunziUopeRhv9O79JSOmDeiZcrN3o4XBr1Iz1TbV2N5Ye-POdeZtdOWjjT6llxK1_CQDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌دوم لیگ ملت‌های والیبال؛
ترکیب تیم ملی والیبال ایران مقابل آمریکا؛ساعت 18:30 از پرشیانا.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/persiana_Soccer/24296" target="_blank">📅 18:09 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24295">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/quSX8VY3KdIpyXhwCYRcz5KVqjb5bqR30toV8BI4kDzGMXhPlBWxVlsoxGZo4wLwjC5BgtunzqZKLjP7A2pYJlQdnSyNukQqG9CfS2OuJGh6bGDEi6HpkzWaQemWojL_Pajdvfk72A2yFrfVNLZIjKRiGu7l7Uy2SHuRYqpbeQ4DLG7Tbebg_bXTHBYkrr4osVQmb-pfqYLddZ7hBFynJuavMz5CnVuf_IS6hwoLOT19vl39VYrmHhT4geGHLThfzGT904yjL4tMD4hCwC80x1qJdbKaN4o9hFJUq9tgUXyhDfnVScEzGR2S9Osk8CCDX7fnG1VvnvQ1RdKsgVhj-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
امشب‌بازی‌برزیل و اسکاتلند درجام جهانی برگزار میشه؛ تقابل این‌دوتیم واسه ایرانی‌ها خاطرات تلخی به همراه داره؛ ساعت ۰۰:۳۰ روز ۳۱ خرداد ۱۳۶۹؛ زلزله رودبار-منجیل؛ یکی از مرگبارترین زلزله‌های تاریخ معاصر ایران در شب بازی برزیل و اسکاتلند.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/persiana_Soccer/24295" target="_blank">📅 18:01 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24293">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ecgrc128vMhk2XajUKiOWM6GKiCZAuszgUyxTn7KsWrNjc42ZODFEYiIEON2BBt66q8vACP-brYtthmU8c42sr58GRoWTMfCyTTbl6bWXG1JXGIuRAhwwGE9VcA1t2qeAfl8ZqZE8oAJorV2H0IvPCm9rcRiKBFdvm_kGOpe9pC92dYtJTsHQi79Ee7vM_41AH5Dp0I4I2RIDfqPFq7ZRvTXiwEv1aE5lPGuJ8pU01YdwrryFSRGpBK1xO3bmSUVpPpGpokUaNkZh6amPDNW-9oapP3TtgBga9V7_skFMxobnAyUGc8loaU4vXt9phjoj_ETsdg_Ul2vZBcysvrnxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qMhPVaVm1RHDUra0gQHuGF-iEX0cV6EU86IJZ_AguijdSGxaw-IYADbKo-mV0WWdnGrfHOIzRcklWmaCr9hFpBowsbMGjmUfPN2wrRwB5prCOtaRvKXsdUE7YjT-C3a0yEFKWHFMZPkZaBnsjSERzx9Kx4uxeUYrX4MRjc1OiTLEgeor4I2PUM1WEdTHSTXESZBkeiTyHny4BTte03nqvBYLAaTgWDNIbOZa4dJrp3SF9l8VmCENDSCldxT0w6vztJi_3WXw66zCmqNl9qAglFCBArI0j-BKEQ3excx7bql3MppO-QA_gf611T2Qt6ZW_8Va9NZDYXo6KpjMk42wGQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
"هبا عبوک" اکس اشرف حکیمی که دنبال ثروت اشرف بود و بعدفهمید که همه چیز بنام مادرشه، بایک‌شاهزاده قطری که 2 میلیارد دلار ثروت‌داره رسماواردرابطه شده. هبا و شاهزاده تو جریان جام جهانی 2022 با هم آشنا شدند، زمانی که هبا هنوز همسر اشرف بود هم دنبال ثروت اشرف بود هم بهش خیانت میکرد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/persiana_Soccer/24293" target="_blank">📅 17:37 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24292">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gVO7dhhwWU3nnoYISterXERi9uIKP2mppgOvFaZDpTNUP8qo38t0JbAyvDzyHsdLTTqTMA0bhp0DBPHXAfZM_Vt1M9kqyKtWaeebG0c3wkvmuVwLIiTjgdS_C0Rsh9EkDxvtbHJztlk-jPOBG2mqh2_Lrr2bY_EQ_LsWzYEWWfszemhDA8FSWJvdoVg5gHtrB6kq_o8rQeNPozgUa3EQGGqvB7YeTH9wqxtthYPBa0b3-zZU5TM21vhsw2vSK7fERQxx_PWvMI3k9Xo0bbm5u0Z7urMyc0kgA3JCe9KpPH5de4ndmjfEEKi-XIT879-x40iIIkDqxVAOgcvt3SAhxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ دراگان اسکوچیچ کروات‌دقایقی‌قبل‌رسما پیش‌نویس قرارداد دوساله‌اش با باشگاه پرسپولیس رو امضا کرد و رسما سرمربی سرخپوشان شد. باشگاه بعد از فسخ قرارداد با اوسمار ویرا پوستر اسکو رو منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/persiana_Soccer/24292" target="_blank">📅 17:26 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24291">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fkxJ3r8bfWlpl0Lq9NeSbbX6iMP9ZHDeMecFQXGo0oc5zHhyNGo1bA_6Fgj_x-akdX3CGV_-wGjh7-YIZekNw8rhUoYTgvTvTvD_jX6CINd-PlxoqJgYPl70bKFZsHmTB9lIl5ky-Q6MrF-tHWhnOy4yp2nWcWkRP4p8NeYnxJx3onZl0uIDXiEkMw9xntI5xbWsl268mD1tZ2fsV8MTF0tcPzB38YJyRKCbrcMHM2-QfskWFuyadEAoB4S0xvUBFduvgoRf2Y-pCQhNvy4Fhc9C5bc3N9F0pQWik-qL2161BPd2R0omz7WmYdnCLhTG2Hl4UUxWucSTlJq4cJ3Wrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
استوری اوسمار ویرا سرمربی فعلی پرسپولیس درفاصله 24 ساعت تا دیدار مقابل چادرملو اردکان
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/persiana_Soccer/24291" target="_blank">📅 17:07 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24290">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d5e9c8b86.mp4?token=aP2P-ULs8hX4dk1BdgD7hzEu1xWtSG8giMtJxcqrsQ5bj_u86kKGcToCw_qcJeQ_aBoRl4Ck6KIksvp3yMj0p9HO4RmATOwMbglwLP3c31e6ll_dNtRNSX0oGlIMRyAW7xTiIiwg4ZHB41q4ZG2RTDt27tdols8mAYDLMvZd7POG3j-3x_mzEVm087v_SJImMbYHYwFKqoZU8ACzcqKbAvVXobv60BePQoj1FfvYmqzSnK-mhPuU1XtU-IeisOG6MDo14WNIXwfrE4daFrN89D0FBl6z-OI-5QseNRa2kZ42UbdX4AAATFCTccVzGTcrwDUk6gOVPFD5N3B9D-F4928CdfVLFVYlaa7lUlwiLsV3-ctlnlNPhAXBdHp9fxTW_PaJn_GZ1tiOFDU4uze7G7VoGr6ODxWjfYl64VtEByrw-Dp5nyCiVS7vm_7b3-MWHx7N7RVRQASUp0OvZUhL2-7GUR5272PraEri7zwlo7G9sbcPUYK6g5PCVRJM780XFm4i8bOiJqQsG-UfEtDRseTbZnonrLQbTSC8WMprLWiggwIIV6V0buv32ZsU25Yykl9g7T2ixjwCgJIYHKyp96ZJCY_ubhZ_5kKuqQdx0LtN4gxdIv8Z_yiWUD_zbWcDiEUYoxpUVSdv6dBT5jkP_xH8hHYQLHR4IQC4GNsy0Fw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d5e9c8b86.mp4?token=aP2P-ULs8hX4dk1BdgD7hzEu1xWtSG8giMtJxcqrsQ5bj_u86kKGcToCw_qcJeQ_aBoRl4Ck6KIksvp3yMj0p9HO4RmATOwMbglwLP3c31e6ll_dNtRNSX0oGlIMRyAW7xTiIiwg4ZHB41q4ZG2RTDt27tdols8mAYDLMvZd7POG3j-3x_mzEVm087v_SJImMbYHYwFKqoZU8ACzcqKbAvVXobv60BePQoj1FfvYmqzSnK-mhPuU1XtU-IeisOG6MDo14WNIXwfrE4daFrN89D0FBl6z-OI-5QseNRa2kZ42UbdX4AAATFCTccVzGTcrwDUk6gOVPFD5N3B9D-F4928CdfVLFVYlaa7lUlwiLsV3-ctlnlNPhAXBdHp9fxTW_PaJn_GZ1tiOFDU4uze7G7VoGr6ODxWjfYl64VtEByrw-Dp5nyCiVS7vm_7b3-MWHx7N7RVRQASUp0OvZUhL2-7GUR5272PraEri7zwlo7G9sbcPUYK6g5PCVRJM780XFm4i8bOiJqQsG-UfEtDRseTbZnonrLQbTSC8WMprLWiggwIIV6V0buv32ZsU25Yykl9g7T2ixjwCgJIYHKyp96ZJCY_ubhZ_5kKuqQdx0LtN4gxdIv8Z_yiWUD_zbWcDiEUYoxpUVSdv6dBT5jkP_xH8hHYQLHR4IQC4GNsy0Fw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🤩
اسکالونی بال؛
تاکتیک آقای لیونل اسکالونی سرمربی تیم ملی آرژانتین که به شکل فوق‌ العاده‌ ای هم در حمله و هم دفاع بسیار عالی عمل میکنه.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/persiana_Soccer/24290" target="_blank">📅 16:50 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24288">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HOqvRh9k540kzKOL3G4cicVwQI1w5C2gmf6wfc-_nDPMARYTuI4Ag9eMC3oi23wuzUVH_Kj3UoQMpGU--XP2LUWTG-4TLNLFrjgPuGSuJ-PASsV1zw1Hr3_-E8fNugb1EdGO7BqmRLLa1-T2Rkz7lafeNk_ngBHXTljAyC4l9tfcOcnrWzHT9vGEZyuiMUjUVLulDU2zY3wvN_OriyggZOmOnYuftxNTdtkU7GEvxyCbJWL92YqmC-CRMp9ltmiIKDBCDgtQ74_hBe-njTi5Fuvj1QJ4gedAVEnfzJzqViooR-RSRKEK-f5l-2Olm6G36xUlMoZD_D_-jmVNyUwSqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
خبر مذاکرات‌ نهایی‌ باشگاه‌استقلال و توافق با محمدجواد حسین نژاد که امروز اکثر رسانه‌ها اون رو کار میکنند. 10 روز پیش اعلام کردیم که باشگاه استقلال اوکی قطعی‌رو از حسین نژاد گرفته و فقط بازشدن‌پنجره و پرداخت‌رضایت‌نامه او باقی مونده.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/persiana_Soccer/24288" target="_blank">📅 16:35 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24287">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7fe43357c8.mp4?token=OIVTd0vIOhl7a0rgjn4k6TBugJfCJkSDbivGF6KPlYeJCKtWKamHtp7X2CHkDVbc7GuC--ExqI0OF1jUe_rdNdk8TTNw3ZJ_UiIq2r8ZBhPVeJ2UkbqLJgz5t4MuA97_MJIEHwDoo4ReF2oFcg2V48a-6czE5YzVUyIAASLXXIOmznhI_kCtIekyoghr19LlSOtSsdmSsbwKyjht13H8vDUfEVyV5VKZ3y_RgEVoNUmu5uWFs7avLlwpSWTyoh4MLl9i6G48v2Yg3vSx4Y46k38ZaezMMr0wgjfXLRDcPLz9P2cZV75eqO54Blwq9dS8zxcW7ewKJzHSuDCGABsKcEhwaEtOphD-j2QqzzJNa1zO2Wid6s8A3y1dMLVNxBs7b_xChFdzAK-OOzfdsOTQIJyDY9rguM5jVHqw-PatUEZvjro23kmc5dNAWbTBgpUSiWfqLPSzDQeMeVLRwQwug_PtQBilhnAUKm5150d49S7p0qsxUJiTxa7JfQmoRv-Dp4XaD04Cm4yf5lnEGU-jHw2yQcNAZkKlCvl8Fv-dNYwTxk88tAeI7ym9uV6dG7gE7HGhKJyQIrMSPri3nomey2D3AdXRNWgDxkgMFKFofb3Z7FYkcbroySF99BCALXFpVv4AK_malkJnrXtT-LswBTXCkEPTw0vIfJJ-Tgr8ljc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7fe43357c8.mp4?token=OIVTd0vIOhl7a0rgjn4k6TBugJfCJkSDbivGF6KPlYeJCKtWKamHtp7X2CHkDVbc7GuC--ExqI0OF1jUe_rdNdk8TTNw3ZJ_UiIq2r8ZBhPVeJ2UkbqLJgz5t4MuA97_MJIEHwDoo4ReF2oFcg2V48a-6czE5YzVUyIAASLXXIOmznhI_kCtIekyoghr19LlSOtSsdmSsbwKyjht13H8vDUfEVyV5VKZ3y_RgEVoNUmu5uWFs7avLlwpSWTyoh4MLl9i6G48v2Yg3vSx4Y46k38ZaezMMr0wgjfXLRDcPLz9P2cZV75eqO54Blwq9dS8zxcW7ewKJzHSuDCGABsKcEhwaEtOphD-j2QqzzJNa1zO2Wid6s8A3y1dMLVNxBs7b_xChFdzAK-OOzfdsOTQIJyDY9rguM5jVHqw-PatUEZvjro23kmc5dNAWbTBgpUSiWfqLPSzDQeMeVLRwQwug_PtQBilhnAUKm5150d49S7p0qsxUJiTxa7JfQmoRv-Dp4XaD04Cm4yf5lnEGU-jHw2yQcNAZkKlCvl8Fv-dNYwTxk88tAeI7ym9uV6dG7gE7HGhKJyQIrMSPri3nomey2D3AdXRNWgDxkgMFKFofb3Z7FYkcbroySF99BCALXFpVv4AK_malkJnrXtT-LswBTXCkEPTw0vIfJJ-Tgr8ljc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
🇬🇭
​​
طرفدارکوچولو و بامزه غنایی‌که با جان تری اسطوره چلسی و بلینگهام‌سلفی‌وفیلم‌ میگیره؛ گفته ازکی‌روش میخوام غنا رو قهرمان جام جهانی بکنه.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/persiana_Soccer/24287" target="_blank">📅 16:25 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24286">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kTwohHZEsSEuEaZVmiQ7Lds4pTXilmWnzL_pvGh-RK5qGvrWujJ1jbOzIdmk80sbFkuqqmP_YECj0xFefPiVc9N_2QviUdm8hTsz7jnEb71Oz_-0r6tE7C8CzJlM7_2pPzYzqeshTJbGY_8DTqqsRCwYvuxgYNNEnqVhhiBq-4qJvJAqctgHPWGFaIyogrp9m8VTqZe7BQWGr7uttVpL1Wmu0XxPRxlkCbDn9OYJWNDm4uCFmwGwxNHQjJAnqLb-P1B8xbp1nThrolecJfE_ZDSaLdm8WMaynAqn6AJ9kDgUHJmLiWMzHap2V_7QerpNI0GT292VSKopXRYZxKNV1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🔴
#فوری #اختصاصی_پرشیانا؛جلسه بین مدیران‌پرسپولیس و اوسمارویرا برای‌قطع‌همکاری دو طرفه به‌پایان‌رسید؛ اوسمار ویرا موافقت‌خود را برای جدایی از پرسپولیس با دریافت 900 هزار دلار اعلام کرده‌ قراره بزودی باشگاه‌این‌مبلع رو در دو مرحله به او پرداخت کنه و قراردادش…</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/persiana_Soccer/24286" target="_blank">📅 15:58 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24285">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c9q5sDnw4iAo0mMxfO7Obd81YSZpBdXnppn2-69DrUrI8eg5t9iFRpk8o5p1pWbWfiXW2Cq-TCQe2nxSXDNA0aIyMHmUgaH7lz04gBvp-xrYh1HiinTmkwC7_xPL-9NMb_3FTGt_Uf32OxMB-fZIMkYnlx0BeazAsDkOpGdW4QyddhvJDMS_b7VVZBc7nXEew58NVQcJ0i7JHYL_O7Lf90birPrUTHW6F9B1nEbywBfIAA6UKeNR84e_Vs1OfXbz94b1TnmXrolBekGRHqA6l1aHAPfZcerw5jeYnz1-bR2G-FklH_zB-dSwJaGzATjGsXsEtljsjQL9QMNTDHEtBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ اینکه گفته میشه‌درصورت عقد قرارداد بادراگان اسکوچیچ؛ بازیکنانی همچون سروش رفیعی و امید عالیشاه که‌کارایی‌سابق روندارند در جمع سرخ پوشان ماندگار میشن کذب محض است. سال گذشته قبل از چند دوازده روزه کارتال عالیشاه رو در لیست مازاد گذاشته‌بودکه بافشارشدید…</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/persiana_Soccer/24285" target="_blank">📅 15:48 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24284">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Te6z95D7IXMX1aoLie0vVVZnFUQgCGlQ_VH72njEtAYXxt5bJP2f99a2A0bh3oAgYp7hNykenWrMqf_rk83YvLdEqKAXHHcmjT-rSA6cgE4LpWn5uZWXqo6THqMwjIP4RhatOQEeppsTFolNLZcLDLnDFGQeyxZPMWJSJ3i4mXxx71vCEym_DFTOTR4dpzC8Mkdiu8pZ4IGsSq1bWLkZh6QEOFK4dG3QDRESWxIIcexyxv4MyxRG2TLYgydjsncmRPvY2-hjURr0obcLX-GzJCuOF5mbDSDuql9uSPnNfYWWIGn3lXy0uqgV1p05J-NE0SPmGcyekbu8rdtKQ6pP9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق‌اخباردریافتی‌پرشیانا؛
علی تاجرنیا رئیس هیات‌مدیره‌تیم‌ استقلال صحبت‌هایی با مهدی هاشمی نسب پیشکسوت آبی‌ها انجام داده تا درصورت توافق بین دو طرف؛ هاشمی نسب بعنوان یکی از دستیاران سهراب بختیاری زاده به جمع آبی پوشان برگردد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/persiana_Soccer/24284" target="_blank">📅 15:35 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24283">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/glbc0Es68fCkYP3Ruoq89qVKacBTTJgDa0T4FzCAjrhWmV0VI8azJMgEWZNYFcB4v5pxCFwRJLqbrbR7_Xi0PTaqCnKeDWm8hioYUDqJbGxok86-MvBXCNatf3gm4eOa6Rvij4p3amXvb13x0PDoDWgVKxUtCIwVa-C_RL7LiIwyIg6jnrDrLbmhC5PXMjeLwA3Qkq2C2jR9xKCOHtyn7BK1lvjvdNaN4vq6dnjBylClP4aXKu9gpYWitRBLs694899cSWllCSMTJYHfmJnA1N02gvqzN2WfKfFWpo7Kh6x-8s9NxFRteOJ6C_dNl3Pz9hVtJpN6-UVFbg8AM7d7Yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
یازده بازیکن برتر جام جهانی تا اینجای کار؛ با حضور رامین رضاییان و علیرضا بیرانوند از ایران.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/persiana_Soccer/24283" target="_blank">📅 15:12 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24282">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nNSMKavc8bzbAexTzucFhT27NQXCD07sl-3LoP4_lp_zHikse8RZPHYyFTyDV31EtR6NmFqttlzMwrOcTyLpNXrMf9jc8hTtkM1RQpdo0s8HH270UbsdAFUZwc35bWpG5GXvQ_gDHN7imOWvC_Ph6jnK59B1mOLsxoDl7Y4CGerTn-VDxg56MqzUkuLfhzi-iP4jQSCrUCD7Zfo2BX2zerM5kAXZPi-NdLYlHtIZGAg57BuND7QSiZqEsmYnaNddqhXcjABWgg-fMZZH_Tvbekv3MLWr63YcaJ3Kg4zaNx7eBON1MKnJJ5UvrOh6zv0RZEL4h9FJr7xQDioY0JZOJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
اگه شاگردان قلعه‌نویی به عنوان تیم سوم صعود کنه در مرحله بعد ممکنه به امباپه و رفقا بخوره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/persiana_Soccer/24282" target="_blank">📅 15:03 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24281">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4afba99e55.mp4?token=XUdt_mCckYKEnm6VoUZhD_mBiv32_z7VA3Ty2sm0Ns-XxFVvv92kBLc0mQJyOf3mqZBQL9fTuJouAE9vzeUaLumRRcOjzPGxPseFL81busrHEwUODmtN2R8Vr8rNWgEobKPSh1lWR7vqbMGMFw6cgqKpzS3hYPwwPE0OnvxCIUgOGDRv0Z00cACRWDqKHzjIHBisb4Gb_RsXua4G7COQg51ZtEM8YlP57hJhLZLx0N5D5Qc4J2VPOOGcDCmDIdtdeLuscWtcmGpEC4yE2b_zpqJaJhDtMQsOZ1Ja0gMQsxbHRTY7wizzeWkh_7Fd1MZQI5Bq0US3pBZy-m9j7hMApg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4afba99e55.mp4?token=XUdt_mCckYKEnm6VoUZhD_mBiv32_z7VA3Ty2sm0Ns-XxFVvv92kBLc0mQJyOf3mqZBQL9fTuJouAE9vzeUaLumRRcOjzPGxPseFL81busrHEwUODmtN2R8Vr8rNWgEobKPSh1lWR7vqbMGMFw6cgqKpzS3hYPwwPE0OnvxCIUgOGDRv0Z00cACRWDqKHzjIHBisb4Gb_RsXua4G7COQg51ZtEM8YlP57hJhLZLx0N5D5Qc4J2VPOOGcDCmDIdtdeLuscWtcmGpEC4yE2b_zpqJaJhDtMQsOZ1Ja0gMQsxbHRTY7wizzeWkh_7Fd1MZQI5Bq0US3pBZy-m9j7hMApg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
⚪️
اگه‌تیم‌فوتبال ایران در پایان مرحله گروهی صدرنشین بشه مرحله حذفی به مصاف عربستان یا کیپ ورد میرسه. اگه دوم بشه استرالیا یا پاراگوئه حریفشه. اگه بعنوان تیم سوم بره بالا کارش سخت میشه و باید به مصاف تیم فرانسه یا کانادا بره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/persiana_Soccer/24281" target="_blank">📅 14:50 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24280">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IM_g34HxBCcTuLC7I0hUfV4jh0Q1SjPPiJ76ugeLOjEke3XNZFwwCLVWyMwVYG38fGeuwZqNVWiNEdOAemlZYornXHPrfds874iBPOTzmRU_V5rLUV5lTuO1IcpBkjiC3WYvee09v4tt1joAQooR61kPQpu9dsLVPwuVyal1Yroqwyr4lnv_UjMQP4dCYuizYFDu547s8poKYKYUaR1Nu2vCyuG0shYOtaK7Wn8kxKsl1uy3xsfjRasdRIK1lrEpKj9aIkoJrbhZPD2AN-cdS9tZ-G7podf0XnrfHTjNGS2BfcPRHkqAQVVtxdLXcgKuJH6tvUxTjhLZgzt42x7sqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
امشب‌بازی‌برزیل و اسکاتلند درجام جهانی برگزار میشه؛ تقابل این‌دوتیم واسه ایرانی‌ها خاطرات تلخی به همراه داره؛ ساعت ۰۰:۳۰ روز ۳۱ خرداد ۱۳۶۹؛ زلزله رودبار-منجیل؛ یکی از مرگبارترین زلزله‌های تاریخ معاصر ایران در شب بازی برزیل و اسکاتلند.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/persiana_Soccer/24280" target="_blank">📅 14:21 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24279">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vs0lhlcxyWjM94xu6ds-nR-bvVbZAQUjUvX8-lM-55Wxl-5HjtNOvW-JSOn81-qT4uoHShx0TJUb6JDNNo118u2cgnaoW70Aw4wLhF-X-aI9FLJAgAPi-rOQEWaeeU4l3hWVbUaD4PgVN3gcV-5WqpaJvVTUd28lAbOIGQre9oQAPOtwt7zn8XQOrrWUNBKba9l7noLtZk2NMyusMdx_sPSuTfAggsAZG5MLQX_BAbDKyfqhFYsKjYHCjMIQhG9YwmanPnNg1yQiEtECTmYnq58D9Eka9khSol5Nu728Tj6BlnFVNSv-jVcjv-N3BaXmkMHQglOf8a6f1vgCGGzXtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🏆
جدول‌گروهA رقابت‌های جام‌جهانی در پایان مرحله‌گروهی؛مکزیک‌با 9 امتیاز مقتدرانه صعود کرد. آفریقای جنوبی نیز با شکست دادن کره دوم شد و کره نیز احتمالا بعنوان تیم سوم صعود میکنه اما قرعش سخت خواهد بود.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/persiana_Soccer/24279" target="_blank">📅 13:54 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24277">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LJjJq0uZoe0rCh3qJDuQjobYfzVSM21IKbUrI1rWGEGGQii-Xcec1BeZ_OtPE7877vk59lXSaqAD64XMZEEAIjK0x1sM495IM3D6xL1T8NWsm6To7GlGIr9vNqY0JIPDNk8_E7Fzm4YFhv0U3av18eEFlbLAB9s9SSzFWoGHs24gWr3ycBa77mJCFT7YxE6i7JFwlRtiVdg57Q39zPg8cGusxUKiJzPa2oIX0pCnXi9enBKl-oavjq63vo6vyV_uWUY3hEFUivcZfYaxclA-oocRPv6C4UZinnZqAv4jIEKw8xnJRrBfxSzBMPnaUSj6leUOSjuUWW02oxqwp4TReg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ فیفا امروز صبح به فدراسیون‌ فوتبال اعلام کرده در بازی هفته سوم مقابل تیم ملی مصر؛ شاگردان قلعه نویی باید با بازوبند رنگین کمانی که نشونه حمایت‌از همجنسگراهاست‌واردزمین شوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/persiana_Soccer/24277" target="_blank">📅 13:37 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24276">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c0f79258f.mp4?token=kI72EPGb8O-M2qK8ReEVOBMay8KQWn-ntxYklrFb8kFOFzwYPfkJCXriME_1P1TPVMz52a2SOseXwpRb0tR8CMu2JLyJhAistIBt31s0p7a0osussqTGBY3EhCETJD_gtUOKLg9hXNhd4UvUb1c5asUHJ54x9q6--7dUpxh4DCE-0ufzkD7A1lTaih4S6mNaBazjKrlfbUjSMS6XhYID5GdUW8UbNzbvMyMFsiVsUX_3Qat4jESnHfwHZsO1-jz2857AnutL0SORmxOjGTClCWyvH2Hvmqv-Msc0iuTzoHPxkcOQrOx1IoyWjHir4wOJ27BEJp3pso7l6i5zBJZ2FGck8nFvpBHz7yifJDwa_8CoUHADyiSgVt9sYWuLCikFwjSAScjv_VCgGCPGurhT1OKEINuqCk6gL4d7d8llS8N7AjkXY7Lk9ZCYoS85z_2VigR1rzI5pMVUW6ECoP4bdkUfvGGjlYIGRy-rB8TfgHOTk75NODIXV0yk5dpKxnJ3ir69mgJgtwmJO1LO6FXwTKldjNXwgvF5mW4guWPY52G6RFXwlR7Ak0Hqp5PRl_dT6jyJ_Hk4LnmdZPdZ99wSBY60MOIteAAkD33t5VOHJX2C7IUHr9s2_r4czaFsDINRmlG6_VTR2XgjDH_tAXuJmgKtz1YTNGRswupyka1Pzb8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c0f79258f.mp4?token=kI72EPGb8O-M2qK8ReEVOBMay8KQWn-ntxYklrFb8kFOFzwYPfkJCXriME_1P1TPVMz52a2SOseXwpRb0tR8CMu2JLyJhAistIBt31s0p7a0osussqTGBY3EhCETJD_gtUOKLg9hXNhd4UvUb1c5asUHJ54x9q6--7dUpxh4DCE-0ufzkD7A1lTaih4S6mNaBazjKrlfbUjSMS6XhYID5GdUW8UbNzbvMyMFsiVsUX_3Qat4jESnHfwHZsO1-jz2857AnutL0SORmxOjGTClCWyvH2Hvmqv-Msc0iuTzoHPxkcOQrOx1IoyWjHir4wOJ27BEJp3pso7l6i5zBJZ2FGck8nFvpBHz7yifJDwa_8CoUHADyiSgVt9sYWuLCikFwjSAScjv_VCgGCPGurhT1OKEINuqCk6gL4d7d8llS8N7AjkXY7Lk9ZCYoS85z_2VigR1rzI5pMVUW6ECoP4bdkUfvGGjlYIGRy-rB8TfgHOTk75NODIXV0yk5dpKxnJ3ir69mgJgtwmJO1LO6FXwTKldjNXwgvF5mW4guWPY52G6RFXwlR7Ak0Hqp5PRl_dT6jyJ_Hk4LnmdZPdZ99wSBY60MOIteAAkD33t5VOHJX2C7IUHr9s2_r4czaFsDINRmlG6_VTR2XgjDH_tAXuJmgKtz1YTNGRswupyka1Pzb8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
شکیرا به پسرش میلان میگه قهرمان‌های جام جهانی رو بگو اونم شروع میکنه همه رو میگه بجز قهرمان سال ۲۰۱۰ که باباش با اسپانیا قهرمان شده.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/persiana_Soccer/24276" target="_blank">📅 13:15 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24275">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LDadjQ-8pfc-1FenAykB5Uh0xyhpGn-B2T5jj6HNzQvDRHzAkvWGoim8I9BC_Qwe-GHr_UXarDYTWaDTWcM8vUTdnByRbD_1hd7FVx65K_CkUHxp9xmeCscp-0lstQ7k8oI7DzffyEgtljWKh5qMbWwzy0XJdrQpV4OQfLw_OunfDqSxXRuxU8W3cqDXf9fbi_697AvJbIM8zAVMUxSzi3cKH02Z0Ut6RxnQqctiKFh14JBNklJUe3l_n7YqmQ5wLhQdJYo5F2y772TAG33Q5Qh-zGlkI0Q4o83OZUy6wrobcatEjjN5kiyPccLWzIEWIqW5bf73aRRslEE57ZAjgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
⚽️
🤩
باشگاه اتلتیکو مادرید: ما خولیان آلوارز رو زیر500 میلیون یورو به بارسا نمیدیم. آلوارز زجه هم بزنه زیر این‌قیمت‌فروشی‌نیست. رومانو هم گفته مطمئنم 150 میلیون‌یورو بهشون بدن درجا رضایت نامه خولیان الوارز رو برای بارسا صادر میکنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/persiana_Soccer/24275" target="_blank">📅 12:43 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24274">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06bbac815c.mp4?token=PDjEB4ieHjPs7iR57NU21H3Irq6QENoyW0M7vcd1Rp171ejO8l5BAvoJQaCyXOFTSt7h3-XAuICc1ckY6R2OPm8i6GqxOYeMMpd9XO5lH_EodSFk-6Ni2DiM3xdp7ECesmh_F3_zOde67-DIGMQuXgvkoo_042OlFrEDBcsHdVBjaBFp4VjjqMhfb6RiIitVHGg-eSRYtWg2WAOxl3PZol2JJIIsacZkY0JVInqEKy6X9LMBPKqLq5rcwY2v3qD4aHHKvEgqUfRWkkHzYe53YojbLmZiXphZcjYNV6pd7BcT9OWHRgaYbk59oZuRAWZ-wytAWwBJjkyiaJs7wPgLkCwp71tiesQXkIha7O2EmN7ydavu0QKbSEBenIT3FtXfkZ0qooY3OTp3ndNEDjg42nPcBH3lSBDfX3WmvUcPlWuu4_6jyve1Kl9Iu_4IW0toeamgSFgM41YoE632VM72eNV5xkbhT_lb9J4F3pLXzB6gpuqT-9WXedLLzm9kJPbQ_qbPiSegHZAnAV2iqFRYtLPFHLzIMCza3bIg4ftRiqqpGNplc-jdq2TCNIXrkZ9h361RGxXg1BnSSUwmfbYwEDpo5whHfeTWS4ujkmDyJtlmkNykXPv7GDAgE1HNfwM21EejQ1fr2KZRUDRCtWTKbpfI9P1kp7jKjkjDxC9VeE4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06bbac815c.mp4?token=PDjEB4ieHjPs7iR57NU21H3Irq6QENoyW0M7vcd1Rp171ejO8l5BAvoJQaCyXOFTSt7h3-XAuICc1ckY6R2OPm8i6GqxOYeMMpd9XO5lH_EodSFk-6Ni2DiM3xdp7ECesmh_F3_zOde67-DIGMQuXgvkoo_042OlFrEDBcsHdVBjaBFp4VjjqMhfb6RiIitVHGg-eSRYtWg2WAOxl3PZol2JJIIsacZkY0JVInqEKy6X9LMBPKqLq5rcwY2v3qD4aHHKvEgqUfRWkkHzYe53YojbLmZiXphZcjYNV6pd7BcT9OWHRgaYbk59oZuRAWZ-wytAWwBJjkyiaJs7wPgLkCwp71tiesQXkIha7O2EmN7ydavu0QKbSEBenIT3FtXfkZ0qooY3OTp3ndNEDjg42nPcBH3lSBDfX3WmvUcPlWuu4_6jyve1Kl9Iu_4IW0toeamgSFgM41YoE632VM72eNV5xkbhT_lb9J4F3pLXzB6gpuqT-9WXedLLzm9kJPbQ_qbPiSegHZAnAV2iqFRYtLPFHLzIMCza3bIg4ftRiqqpGNplc-jdq2TCNIXrkZ9h361RGxXg1BnSSUwmfbYwEDpo5whHfeTWS4ujkmDyJtlmkNykXPv7GDAgE1HNfwM21EejQ1fr2KZRUDRCtWTKbpfI9P1kp7jKjkjDxC9VeE4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇷
🇧🇷
نیمار جونیور در بازی امشب مقابل اسکاتلند بعداز 981 یک‌روز برای‌تیم‌ملی‌برزیل به میدان رفت و دقایقی تاثیر گذار در زمین حضور داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/persiana_Soccer/24274" target="_blank">📅 12:30 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24273">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/edc9cbc45e.mp4?token=rPCva1ADdhO8UGjTfO_0D1wl6o9w0szbOYZ_7GebrEw9CjhsH2wjfIxpVO_S3wUNi_k3BBRA3f2Nba_ucmMw-rwiSUAZgDFl3CoJNHYOnmK4_MNLetbhKKQy7_wuAFhDqHG7a4jpk7JPF2k_8KrYA3hmxdgjfKpfoZ1vcsKI-XEWOt6De7IJjRz78Kqt9HFP-Mf0ytgpJlb7MZDzllPP7KjpACpT4NytbqEUc3NSe-WF5mHzizW0nQBa91W-Bl-OCoQ8tuY815OO8ORBXqZ1r1howBGDSwHaN47ZwmrJHQxJbIEHYehCl_-nnRVRVQX2Q7Uf9sUufRacqhjW4dC44g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/edc9cbc45e.mp4?token=rPCva1ADdhO8UGjTfO_0D1wl6o9w0szbOYZ_7GebrEw9CjhsH2wjfIxpVO_S3wUNi_k3BBRA3f2Nba_ucmMw-rwiSUAZgDFl3CoJNHYOnmK4_MNLetbhKKQy7_wuAFhDqHG7a4jpk7JPF2k_8KrYA3hmxdgjfKpfoZ1vcsKI-XEWOt6De7IJjRz78Kqt9HFP-Mf0ytgpJlb7MZDzllPP7KjpACpT4NytbqEUc3NSe-WF5mHzizW0nQBa91W-Bl-OCoQ8tuY815OO8ORBXqZ1r1howBGDSwHaN47ZwmrJHQxJbIEHYehCl_-nnRVRVQX2Q7Uf9sUufRacqhjW4dC44g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
طبق اخبار دریافتی رسانه پرشیانا؛ باشگاه استقلال قصدداره که500هزاردلار به نازون پرداخت کنه و قراردادش رو دو طرفه توافقی فسخ کنه.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/persiana_Soccer/24273" target="_blank">📅 12:25 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24272">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lkpAxPW4GLGKTdCv7PFLyxOieQ4ZHbU7hqe7k6Nurz9BvfstCpGf2lCNAm0BV8lizOz6N2tpMLg9ZSwmVDaY3z2WcfRjtisC18t0WMInBT9Ovkqg-h1zXJa6-tZGm-amcHAMFuHMEp0VnNVNlXzwTxpssmdQND6VKFBlf-Xl9Rl-jXsjWPu_jVhX8bpSFGcVffbnlLbDhao9YFRVaH6jYQ9oDn7suSIU9xdpnmYXRULnVD0BlOUis0XZgY5CRqMBgfrcxvLKmldNEKDiC5NMwm7efBrMeh4ctDZ6H_Uq1k4O7kPC7kxOwjeAu4VuAJHL__VGYtjfSPRe-EPTArfLsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
تعدادفالورهای وزینیا دروازه‌بان تیم‌کیپ ورد در کمتر از یک هفته از 50 هزار به 15.5 میلیون رسید. تعداد فالورهاش از 8 تاازبهترین بازیکنان حال حاضر فوتبال جهان بیشتر شد. عکس رو باز کنید ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/persiana_Soccer/24272" target="_blank">📅 12:06 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24271">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ryPES6kXKN7R0yW6jcXmVEg5-bqcT3GcPnrqGA21BBhEdeqcptBs7DFN2T-SUDbpD1f96BCxWC2goy-o_Mv_yYVa5eSMJI4F8lQZ2hSeO_f79e3crqHUokcr2rklMa2lEauNatKK-ZrxX81o95-hyjTl16nzJ0OGcdNwRMaYcH3hMPZ9aoeRxyv349m4YDo4I8-sdjLksxCWonHHjUhllz7-Zl70pVJXfVQlrshLS9BEel76pEaPvpz2Et94KmpwUFQuhLRtRGjSCB3S8nmEkrs_dTBZCV3Lzl-GkgtxVId5oIAxmgpdSBohhOfvwxRFDSwqUASMqGJa0Vp6cBe3cA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
گل‌ های دیدار امشب دو تیم برزیل
🆚
مراکش و دیدار دوتیم‌مراکش
🆚
هائیتی در هفته سوم جهانی.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/persiana_Soccer/24271" target="_blank">📅 12:06 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24270">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">⚠️
خیلیا نمیدونن که اگه ثبت‌نامشون رو با لینک زیر انجام بدن...
⁉️
💥
بونوس خوش‌آمد گویی تا %220 بیشتر میگیرن!
فقط کافیه به لینک زیر مراجعه کنید و وارد ملبت بشید و به راحتی ثبتنام کنید!
👌
🌐
لینک بدون فیلتر سایت معتبر ملبت
👇
🌐
www.MelBet1.com
🎁
بعد از ثبتنام، وارد حسابت شو و توی بخش "بونوس‌ها" فعالش کن
🎚️
نکته:
فقط این هفته فعاله، پس از دستش نده
🙂
🎁
کد هدیه 100 دلاری فراموش نشه:
Sport100
✅
معرفی سایت و اپلیکیشن مل‌بت
💯
ورود به سایت مل‌بت (فیلترشکن خاموش)</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/persiana_Soccer/24270" target="_blank">📅 12:06 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24269">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EpQ0dp9kFCqLjRG2XTthq9iLKCyNhdWSmzZvD4zxNVcUJWfqRZOZ3eJfwjOhlFHOY3MdhB0DX-Yo0k9qhOB9FIf_7FGGDBSq0fLpXL7ZZypbd6LfCUXYzjw6BQrfhUalE3oHjbq1CEr2wcgfZSdKlKNTuhozEmN_pcbKbg6M-4ZE-SFkTHfVqRTX98hYL4Q2S9oPo4bVnapkKgBHuVGEVSLVg7LrQzBXzet87mCpDzdxSLMUIwHStgVr2HBKmFzXOYL6RcbXK6hgZZfiWc18xFNwJzbACMbkj4gHffzr2Gnr10Pb38tPyjps67IpNw9HrRL_Tz5iFOp_Ki1vh2Cjdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی_پرشیانا #فوری؛ توافق نهایی حسینی با استقلال، رونمایی بعد از آزاد شدن!
🔵
همانطور که درروزهای‌اخیر نیز خبر داده بودیم؛ مدیریت‌ باشگاه‌ استقلال‌ شب‌ گذشته پیشنهاد مالی خودرا برای عقدقراردادی دو ساله به مجید حسینی مدافع 29 ساله تیم کایسری داده و حسینی…</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/persiana_Soccer/24269" target="_blank">📅 11:41 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24267">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oLCZ56GD7xp7Fcd8lZBjskYgZyyGs0ouLRA_-MPgbiny7c3gj8i4mCwH1QrEKT1CnXlYJfIG1bW5lvQFPnpg74ngMidfJwjo0KOSuYgM3RJbyjQDsDW9NL14fS2y6UC6yq-y2cnPIxqEVGs-LXYobJnZh7fVATF4TpbG6POH30_TRfyMu__fXjM0X1gjnfLcajqeS1aUAdmy5Hv6nMW1PkdXuTCpLpWE8L6ueKdTvMZP0fnZulj9ZHGx7beHAsW9rrQ_gOEs8pWXYVOAOsp7IMEwVtJuDjwcEX9egSZvFc9mZKL3TGcp6KZApYGuFVpERgzG-EqnooXaCHbCkn4SAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/M89bVyNN2jPBMLXWpkrYq6aAkH23jRK5xhbNFh695gqt9cKnN4Pc6zIEdSyIwI3-IzpGGJrMY5OF4PDsMhrA7ml_BNNeQKNLVGXPGyFxk9tYVUmfFt90BED1JDffj-ZPHtoHsgw0PR8AiiQPEWRvRr6k_-tHpNCfYH8G9iMHXmYrnJCDWxNh1cNb3UlupL7NEX8CjD4vmbmQAAOigc-tEq0bl6s-QTWm1jWvdl6FGMwwqqFQ4uvfVPiVZUlduvijjd0J-Jr38PMmjk-hsHz3bgy0Zm-ONu3iJfLjdv6pOPxqX2Y_1umM-siZFOIT4J9oEU1n-T3WfFyWVUbRLZ5yJw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
جدول‌گروه C جام‌جهانی 2026 در پایان مرحله گروهی؛ برزیل بادرخشش‌وینی سه بر صفر اسکاتلند روشکست‌داد؛ مراکشم چهار بر دو هائیتی رو برد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/persiana_Soccer/24267" target="_blank">📅 11:33 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24266">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rv9OsLyCJbmmdFqy-Ex5DdTj4YVJ7TQjRV9uPAf_Lsdc1irOFJN2n9IUTQCuzHKp7PWCE3wzCz3F86EHlm6wYnA7yoUxnCA-poRTKysTIoAdHJ8OpI1HBrWG2AYEJn21qQ8A1tUsj73d0qC3lgN-cAQC7SEzjFM7QqFxJGnEuODit-kImOL0iZh_8JRLwvl5nonDku6hWewn2McdcsiK-lKKTXNiAE9cAlxpWGgXOKOiFnRuCo0oDR5vKuxYpOy-aM1kHe6ZzcndhnDasBiX5Pn2bVBXb2NfC0vNAXh-zWs_e3z5PJtc_SdVWznzlym6x93AR9x9OK8nPVm7wYZafA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
🇧🇷
نیمار جونیور در بازی امشب مقابل اسکاتلند بعداز 981 یک‌روز برای‌تیم‌ملی‌برزیل به میدان رفت و دقایقی تاثیر گذار در زمین حضور داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/persiana_Soccer/24266" target="_blank">📅 11:27 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24265">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07d25b9dc0.mp4?token=lJzXFH6c1wmxjkwOusmOXlniImX2W7KU9g3lacGsvyLo3dGJCu3FFI6PeaGKiXKA5Cp8fwxYfoDTl0tRJbmRcOpT8_W8bCWlEu2OgXAokRfbPZYJCEPw4f9PC9_iWCtPtz5bVPdpS8hrC9-7xJ2HpMBbNl7loAo8pmcPaUIEzyprHIr-rgyGbZqoNK9qfQ3lQRWSfwFeIyFiUUbIXhNJE3pqEtsplt4x3ehDBi8i3PYnHQMlnU5JZjDqtm7ZEXmAUQTiYiHGl3MSlQc6zjbnMqcGIGckmBKN_YCEdAdVyJ9mG5i37gBrMNMhA8ONEqVAW1rSzyiOLOfWGPVXt0sOzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07d25b9dc0.mp4?token=lJzXFH6c1wmxjkwOusmOXlniImX2W7KU9g3lacGsvyLo3dGJCu3FFI6PeaGKiXKA5Cp8fwxYfoDTl0tRJbmRcOpT8_W8bCWlEu2OgXAokRfbPZYJCEPw4f9PC9_iWCtPtz5bVPdpS8hrC9-7xJ2HpMBbNl7loAo8pmcPaUIEzyprHIr-rgyGbZqoNK9qfQ3lQRWSfwFeIyFiUUbIXhNJE3pqEtsplt4x3ehDBi8i3PYnHQMlnU5JZjDqtm7ZEXmAUQTiYiHGl3MSlQc6zjbnMqcGIGckmBKN_YCEdAdVyJ9mG5i37gBrMNMhA8ONEqVAW1rSzyiOLOfWGPVXt0sOzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
جدول‌گروه C جام‌جهانی 2026 در پایان مرحله گروهی؛ برزیل بادرخشش‌وینی سه بر صفر اسکاتلند روشکست‌داد؛ مراکشم چهار بر دو هائیتی رو برد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/persiana_Soccer/24265" target="_blank">📅 03:57 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24264">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🏆
جدول‌گروه C جام‌جهانی 2026 در پایان مرحله گروهی؛ برزیل بادرخشش‌وینی سه بر صفر اسکاتلند روشکست‌داد؛ مراکشم چهار بر دو هائیتی رو برد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/persiana_Soccer/24264" target="_blank">📅 03:45 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24263">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S8gy4NOuVIOFZxVjArLJ8CwKZ6vujsQl3Blg7v2cbRejy6_78lCPf3ACvqPO4sC9hl6DClYLMnuEHnziZEdkhcrqh2EnEMikKytbEx-yl7Y7mSL0tfmOFkc_1zFxbuPy7cy6WPt_oj6nUIuAYJVVC-J5013_muNKiQcHk523dyjjjd4Y7289-hCt1RlSKI4SHVl7BD6IeEOBfQwybi_CKRuDcEMhGz1CHndTwZwX3TTl0S9KYqZz_C2mAQ1_H5qaDbNbSe9-392ctdu-gh-89geYX12MFUe4PSe8zjQdd7m4nU8M4umnzjHDgUbxCbSfxsEzBvPhcQY0ihVkSpetyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جدول‌گروهB درپایان‌مرحله‌گروهی جام جهانی؛ سوئیس، کانادا و بوسنی راهی مرحله بعدی شدند.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/persiana_Soccer/24263" target="_blank">📅 03:37 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24261">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HlBwcZkwG1llQNxxYokGZS2Eyh4vOO_VzGBE_wJ7XvLpiXh7AzPDzN33xLmU9u7ccaRQfHCgNYOudfZECDrbhy8vDK4D0gJABVR4dvkFQsyeBlK9rmJFEw6GyfDRWHrbLD2cYHCpb-RAPLgC2I7Ym53-dNToSWnvOcinEMQDq3Xz9KqCFNy2BIeNirt_GKqwd4K0-D5k3nZ7r1xZc4rJhCIZqTYnI2v6N9cX8ZRV08_syg2YaYPKc1Q6UKjp2ymyUP5lZ9atCcDNF3BW_8B4H4E3uG_1-QingNGPKCBzpowHe1fR5BfUDftk8AzW073BFatUgjOQjuUB9znMQK2IDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a6d46fb08.mp4?token=JcjFenJ05_3HwlL_ycwFCRx2PPbwIbOQ9HGL629aL-RJyFi9hD6ileZHRu6A3HjUpD6l-c7TehrOo8JqO0zvoDz1a1lwEZPLJwvxC6XvU-fTIKDy_bLBt3gey74UDmmVmApp0tZTvfmuGGJob3uu0pA-58oe6ZT5pWjVs4nPycp1g3Hp4ns5fC3TDAiUMxBPHnHZK8-7f0TjnnhAikl8ofwb1FkVKGaoefonqCEZG3GqF6vp3Ty4RmjeUfLjdkkxarOOLrXZiyDJd1fVtYZd5uw-2oTP-cukgD7j2I2o0nOjjJMOQ80oPMxsl1f16Rd87Yul-nhYWNm2T15jQi-qEDtqOv_cljB7sCjCrNY6nBo6elpO3eHUn-tdkOMeH45Vj8SAZhKNv_S_o6rrkbwPuupdHVS6eo5lDQzn1qe4o7LDupZ3It3cuhY4XMxnThsUR22P6Mt7wMuVTZ1U25-kEMNdxHTyr83z0sFKE9mgdjHh3ksTEVwWHN_lxT0ymMoz3NjdUZxzB4OMnEwqeK6bqlPzQmyNq9bBhxMnyIGe1l5ufxaQpnyQnL0OOV_eXD5brB159I_W3S9MsNfd3nWPi5KbdpGvr1t4wdUApZq-MjcBGuAhi8ewdohtoQuGYbPQtsnzJueIKUYQZEbiTXfVbIVGPNsSuUGqJYfXzJtTayo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a6d46fb08.mp4?token=JcjFenJ05_3HwlL_ycwFCRx2PPbwIbOQ9HGL629aL-RJyFi9hD6ileZHRu6A3HjUpD6l-c7TehrOo8JqO0zvoDz1a1lwEZPLJwvxC6XvU-fTIKDy_bLBt3gey74UDmmVmApp0tZTvfmuGGJob3uu0pA-58oe6ZT5pWjVs4nPycp1g3Hp4ns5fC3TDAiUMxBPHnHZK8-7f0TjnnhAikl8ofwb1FkVKGaoefonqCEZG3GqF6vp3Ty4RmjeUfLjdkkxarOOLrXZiyDJd1fVtYZd5uw-2oTP-cukgD7j2I2o0nOjjJMOQ80oPMxsl1f16Rd87Yul-nhYWNm2T15jQi-qEDtqOv_cljB7sCjCrNY6nBo6elpO3eHUn-tdkOMeH45Vj8SAZhKNv_S_o6rrkbwPuupdHVS6eo5lDQzn1qe4o7LDupZ3It3cuhY4XMxnThsUR22P6Mt7wMuVTZ1U25-kEMNdxHTyr83z0sFKE9mgdjHh3ksTEVwWHN_lxT0ymMoz3NjdUZxzB4OMnEwqeK6bqlPzQmyNq9bBhxMnyIGe1l5ufxaQpnyQnL0OOV_eXD5brB159I_W3S9MsNfd3nWPi5KbdpGvr1t4wdUApZq-MjcBGuAhi8ewdohtoQuGYbPQtsnzJueIKUYQZEbiTXfVbIVGPNsSuUGqJYfXzJtTayo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇧🇷
یک پیش‌گویی عجیب و آخرالزمانی از یک پیشگوی برزیلی بنام «وو باهیانا» در فضای مجازی جنجال به پاکرده‌است؛ او با گریه و زاری مدعی شده که در جریان بازی برزیل و اسکاتلند در ورزشگاه هارد راک میامی، دو سفینه فضایی به استادیوم حمله خواهند کرد و در دقیقه ۳۸ نیمه دوم، یکی از این یوفوها اختصاصاً
نیمار
را با خود می‌برد، در حالی که سفینه بزرگ‌تر هزاران نفر از بازیکنان و تماشاگران دیگر را می‌رباید!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/persiana_Soccer/24261" target="_blank">📅 01:37 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24260">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed8236df4e.mp4?token=YStUPk5EV2zgtCyOLi7g7lOTMNs6Zw-0jXrS8pJOlZcAzpGalq-MPReXBtRnumXF2jNlNFOKZE8aoyPKDEIETAco6V-wtEl9Dt3g-iFTr35D9dnhCkWwxqy7wPFJxO9pKQPypo2p7qyxz4Xy01ZfvMKby8rx_r0Th3RnrREwDxOGk0EapxU6bUKa1izZCegrjQkPjyLFmqjuJ2y9sSiXnKG_gGBtj4yTbLYcVLrXLxjtpVPnd4zIhm7C27_edHi6PgLoFm7xRI1Qe-ks0N5MhvZHijyv37APu5XNnpCkvqmqZhNecG42fvD68TgrWYajUKIWg6dd0SrA0f9OkfKeVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed8236df4e.mp4?token=YStUPk5EV2zgtCyOLi7g7lOTMNs6Zw-0jXrS8pJOlZcAzpGalq-MPReXBtRnumXF2jNlNFOKZE8aoyPKDEIETAco6V-wtEl9Dt3g-iFTr35D9dnhCkWwxqy7wPFJxO9pKQPypo2p7qyxz4Xy01ZfvMKby8rx_r0Th3RnrREwDxOGk0EapxU6bUKa1izZCegrjQkPjyLFmqjuJ2y9sSiXnKG_gGBtj4yTbLYcVLrXLxjtpVPnd4zIhm7C27_edHi6PgLoFm7xRI1Qe-ks0N5MhvZHijyv37APu5XNnpCkvqmqZhNecG42fvD68TgrWYajUKIWg6dd0SrA0f9OkfKeVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بااعلام رسمی فرهنگستان لغت فارسی:
آب درنگ جایگزین فارسی کلمه hydration break شد!
😂
😂
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/persiana_Soccer/24260" target="_blank">📅 01:23 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24257">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C3frgjkkyfI9r_3xhMh0yuy00sagsRAsla4-w9M0lqEsG27s3rb92Wit2Bo3rWuxP7o5u_oFH9mdyA0CnUumAfddGrJ1GDPjquJCLAimHGWNdzc-6sE0HYMLorCx-tP63dOCkLvO5y4VQmVeCtzVUMuaX4gYlLjWw_KrRvJxeMj4HwiuFJvROXJW5pCqTHyLHDN1KKvUsNtlw3LXte4EtZ57QhbHubFcXoYF3lRgOGsVH8jhkCwqq3mHx445nx5PBWluenJhrtSIsoGzNqLBXOBaq6BJ63HIGJWZtCp0oR8hBdKvDnvoQuQWHXPpUKh85IWU9EJ4F2mdWZHq-4IVEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌دیدارهای‌‌امروز؛
از تقابل حساس سلسائو با یاران اسکات مک‌تامینی تا جدال ژرمن‌ها با اکوادور
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/persiana_Soccer/24257" target="_blank">📅 01:17 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24256">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i1VsMcrIVRai0Vm4N8ao7ND1_by6J-mgrtAD3du9g__NObWbCa22orRfQ8DS10H2nuR566OGXVDzMTIckLNoa0CewZv1yj8m90j7FUz2Z9-yZsSG4fPLUNrDaviCUKFForCgWvFNjkBpZuwOXjD5fJzEMAtAItKAQcd_5yu7u59afzt-UX4Z4Ws85phwMLV4yY_r4CdJ-HQU3OilLrbqrFj2U2gb7rAz1bqHEMWkp74fscYKoDErCUsvPZWy1YeRwAVRCuxhJhxCHlg7OwHPboTSbyFvwUJCyYAroHKOznu74oceUPzgwlKewFIAHWKuingwopYlKbTqYnV0jvMVRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌دیدارهای‌‌‌‌دیروز؛
ازبرتری‌یاران لوکا مودریچ برابر پاناما تا صعودچهار تیم کلمبیا، سوئیس، کانادا و بوسنی به دور حذفی رقابت های جام جهانی 2026.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/persiana_Soccer/24256" target="_blank">📅 01:17 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24254">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KBIjZxzX-XxXMtOHFt11YsglBtQqQ5x2V-3nqd4shcy884Brvc0-wnhNyLu-X97G59SGDoN7wgWIvnqia5BeVB1dTxpfkPxnegULmr3_SrhHrODCTMyP0pQd_kIvJb9RtRy59rw6OslaHfgEf1qSnA2KZxePOwwXMhTo1z0O5LiT2SUy2a19S77jQUpYv4GaMivZBOf1OJ1U0x-7DXslR-SUgPKZATZGxAVL6ZlGhxacLZ_2iVJvSbzxrTPuUZBijNeCPHidYQw-70bMTz5smd3Q0Y8zpWw_UPlQ5IgGNmytXMqehKwzqmywk9ZqxcDS25iaVOPEYDI16Hr8nLP1ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sZFPqVY9g-8bkXYvyJKLQar3kSkjOFzGiZX-uS91giejNNiNz3_LX_smECPCq63kiTl_O2G2zdhED7eCjhNKGzHyUZvsOctP874BRp9nw7Gjh7m7o8D-MKIHWo9fom_DmkUPFbNGaurscLBaEDIItDlehFtHicyAV01MPh_d1iJZ7gGaRfg02ydZWp3LKfPDwd3eo0mJqym4HeAkaq3k5ZreHOvDjccrbUGfBMEspxZG_7pSbAlUZkVScOqWQYcynhd5rR-USgeN7hLiIH4T1otu4PuRkydrdOL6-amzU_y6Ph62ojKzugEIotRNC6jCd9ckFcqw1QIx-a4XWjMcSQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇧🇷
همسر گابریل مارتینی ستاره تیم ملی برزیل که آماده دیدار امشب مقابل اسکاتلنده. جالبههه بدونید که همسر مارتینی پزشکان زنان است.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/persiana_Soccer/24254" target="_blank">📅 01:12 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24253">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ncNUiOnEtE_JyAqZa5836KTpphlD_wWAtESMld5YHEIGhPFCQNdAI2GBa1xGwCF_rYSctUZ72zymCQbjF0DwtOuc70kyLWgVs2SmYsPqAZB94LMPKiHRLP7bt3IaZvC2nMKPO-eFJ1IBKsBYc-kJPGvPQgJL69bVB57E1thNM4EftRLsDvccH9nIuL5g4QgeGAEpLWSwmyF3SOBEkrNXux_9nx7pPJpx4MAiPgtlUlNzDgpi-17cBgb6Bj8s_1ocicY1A3zSt7ftAzzkBsh-VBgOwxS946XtjYCOnxcAyngs59u10d6iY09pZE7RxMhffcyYif3WB2yVNisMgGjvzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی_پرشیانا #فوری؛ توافق نهایی حسینی با استقلال، رونمایی بعد از آزاد شدن!
🔵
همانطور که درروزهای‌اخیر نیز خبر داده بودیم؛ مدیریت‌ باشگاه‌ استقلال‌ شب‌ گذشته پیشنهاد مالی خودرا برای عقدقراردادی دو ساله به مجید حسینی مدافع 29 ساله تیم کایسری داده و حسینی…</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/persiana_Soccer/24253" target="_blank">📅 01:12 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24251">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ehF_C1Jp9qathOegawLmPiS6EW_34Nic9t-8zmr3o-_zT8YLGIJZYUETGzUL79y8QLA-lzzyZxlmHSInRddHOXrnBZ6LI5WyaQBS7ypi1MLioOzT8Ar2GsPI26nc6Z9VWFQjn9w-8WS2KBRXO_iP5RTfiMU0TVrd1AxXlJPz-4zZBg63NGt0FwPf398zzaibVDhKKHHT7rClnMNuvEMy11qbHRZAXNJ3CN4AoPk08KqIvjPxfmbtzsixdzWUt7-cxEvIWuxtWE-4EcBUs6JpQNC_z4hbm9-8cUY6eFSF5YVz0gcMv6IHCjYwwWrNBknHBKNA4k3Hn4Jr2Gk3EpKgig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏐
هفته‌دوم لیگ ملت‌های والیبال؛ ترکیب تیم ملی برای دیدار با فرانسه؛ ساعت 22:00 از پرشیانا سه.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/persiana_Soccer/24251" target="_blank">📅 00:53 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24250">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tLwpvfSFp32b3lhiowhXcEHySbw0lEm8Oj-LU7AOuaiAXzK-EOHMrwV_BK_ZJVLCxBcZO8L4cKs2IAEVJ-kzvUVjg0I9eUstRQcgW_7Ii1Di2C80TDww7O8H81NRXgMfkv2JHEoGwvxjOp33LJPt1L7aYHiFA2m7csxjy-Jnk9QCNBOjkNKf-QPG07vCfaeY6Qix8tMUyqXVJQDPe46qF8F7MjcViTpZM8EdGyGza93r4s8x3admo6hWyWLkQkiLMsvR3LceervIPNZY5SpgNoo3_S2X2FqSCc6erR3p0m_evmzUpZdvxKlvG7SCFk7aOMkjsPd8FYqbcbqCb7F4-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
هفته‌سوم‌جام‌جهانی2026؛ شماتیک‌ترکیب تیم ملی برزیل برای‌دیدارمقابل اسکاتلند؛ ساعت 01:30
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/24250" target="_blank">📅 00:42 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24249">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UwPtfTxftt6cMN-RIEx91nYp25qyXtxsiy3rM3ihdvoKvHJmua1y_Kk9yry3bijmrbyqc4ZoXOY4DuUY_ySiw6b1cEq-g3-orfqmuvV56PauQ9x7G9NhAIaefNKfDxQ897Nu8Pw_uISg6eKyCC0IrSVl31ZCBj8WbysoP6eB4GH9UBXq59fO6fj0eKqVraZzrIdsXxq1ZoLk9Ev05kEIpesalWwa2sZqcMtos7Gx8jDqDvjMShCOFVFWwZRj9jXak7FW1B4xZ69QxswsNUWkG1AXY4j7pla8RRUqlySXMLvA5K4EvtTzP5MDYuoX6kdj0UHl1QT8F4ejEDSw_p86gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌ دیدارهای‌ امروز؛ آغاز تقابل‌های جذاب و حساس هفته‌پایانی‌دورگروهی جام جهانی 2026
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/persiana_Soccer/24249" target="_blank">📅 00:38 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24248">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/81b3f9aaf4.mp4?token=QDAfLM-vP03qk6gEJmoPuNmN5v_ZmdzH4ksoWrcHWvsmh9-2mJACT0V23XY7fqlsAdlUbQUo57MrocXmFSOOLnWrcMy5ZNzY9EILZozGKLkxwBWMVTuU38vVe7egaiWn9UtauzO0qpd9uqdfbWYWQhsZ9AOAFOGDEOmLgQOJPrbKZW2mDnqpMnhxJ8lhKEdaZMYJKdZ7t9NCRUMLthztdy1JqacLCR-B-dC0ONxUCOI6Z9JCRcS8AigrYFjbTqu3YS0qEAhcEkL7Dj2MFOOT7NnDBBmTr4P7v6AuvV-Z__2ao43pzFmK9NIRNUa012kp6nG1omjBCz0eDBP1XsbVOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81b3f9aaf4.mp4?token=QDAfLM-vP03qk6gEJmoPuNmN5v_ZmdzH4ksoWrcHWvsmh9-2mJACT0V23XY7fqlsAdlUbQUo57MrocXmFSOOLnWrcMy5ZNzY9EILZozGKLkxwBWMVTuU38vVe7egaiWn9UtauzO0qpd9uqdfbWYWQhsZ9AOAFOGDEOmLgQOJPrbKZW2mDnqpMnhxJ8lhKEdaZMYJKdZ7t9NCRUMLthztdy1JqacLCR-B-dC0ONxUCOI6Z9JCRcS8AigrYFjbTqu3YS0qEAhcEkL7Dj2MFOOT7NnDBBmTr4P7v6AuvV-Z__2ao43pzFmK9NIRNUa012kp6nG1omjBCz0eDBP1XsbVOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
‏میگویند کیروش باعث‌شد فوتبال‌ما تدافعی شود. مگر قبل از کیروش فوتبال ایران چه آش دهن‌ سوزی بود که نگران دفاعی‌ شدنش هستید ؟ تیمی که حتی دو دوره متوالی نمی‌توانست به جام جهانی برود و در گروهی مقدماتی‌جام‌جهانی ۲۰۱۰ پایین‌تراز کره شمالی و عربستان قرارداشت…</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/persiana_Soccer/24248" target="_blank">📅 00:29 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24247">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gjp0DLiMkh17BBFhkuLq7ZNaJvE_VnTwcssnzP_zrc0DiAR7sqphFapgxcigd_sbSwLgPDqRRc6CWRxI7KiePoR8XDQ4eWFCSIYe22VskqcPjvzTMv-b8mkvKDsmeZIlNKaKPPC-CnZxynHpSP1_-NPMXY39ragznpKoKkXAqdn5tLCXBBK8FItNECQPLiUSNA5eXn0cbiEtkdmEl8WnJvt5ai21C29YLsZILFTMsD6-ecXbriz7SsN_f2v0UFFOpP369JYWz9389wios2i3bH4T1rjcnfX7SUEezbawpJiuQ3RY7GGdglLV1z8AEgJPkBwctBxE5a5Ovm2JWr0vhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ با اعلام کادرپزشکی تیم ملی برزیل؛ نیمار جونیور از هفته سوم جام جهانی میتونه برای سلسائو به میدان بره و مقابل اسکاتلند بازی کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/persiana_Soccer/24247" target="_blank">📅 00:15 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24246">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R4ZDspYYp-CswTKopmuR6GCJNzR-p0CNcHmo5iMGOnXvl1Ly3ykNTL_PUTkhNeta7xGC21Mkh07jLoFqmI0HBuCCnSaZjGc5Y8JWTLD9X74grCHnAPhT2rZTpqge2WWiRa8sEFmrGX228dNwK2LTZ6hCGTf0W0z7dWJRl3GIwqmTOEH4-sl7Xn00UfBz1UCfN8Y4DZW69XQvNrb8xRHFfQJjMpzJcJ5twWT-s1iOLRgPnQQaay1k6mQ4VaK3CNeVjd0hb5LRqAALjefSGXxGXw_GisZDzGZNTLphfFdQBjnB1cztZwD5D3b2U3jy-8JGmG6kdJsi12dYJKv2MhurOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🇬🇭
#تکمیلی؛ عملکرد کارلوس کی‌روش در تیم‌ ملی غنا؛ پیش‌ازجام‌جهانی‌تموم بازی‌های دوستانه رو واگذارکرده‌بود امادرجام‌جهانی و درگروهی‌که دو ابر قدرت فوتبال‌اروپا توش حضور دارند دو کلین شیت کرده و باچهار امتیاز در صدرجدول گروه قرار داره.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/persiana_Soccer/24246" target="_blank">📅 23:59 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24245">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ezoDb7miHXD0VhTBkLmCWAT1wMt4PZN7eZzMaDeM9QoaB4NqHcd77Aws_SVVSEu_CsQUXgWAWAdPKhKsrbxBTvjLTFy4om26PuM3NLUgqdsbjuV2xGE8j4sFsvt3E5sfSqI0X5ahsQ0Y-RSIqMjTx-y6IhMolpppQkLEWJGy0pFMe7ulNCoZwEGHYvu9dCD7x1uXgZ121ytY0l_09a99fxJimMsJfqZBEqdbSoU9EK5_7ZC5W6v1m80DHH8dWaxpoFMl2saur-OlX6T00vPJeFAxPBjU2ESvvCplcjt8VQBiEXQm1HSohaDlDHhjd1x82EYNGeD85VJeOli40ua2hA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق‌شنیده‌های‌پرشیانا؛
محمدرضا آزادی از سه باشگاه گل گهر سیرجان، فولاد خوزستان و نساجی پیشنهاد رسمی دریافت کرده و درصورت موافقت سهراب بختیاری زاده از جمع آبی‌ها جدا میشه.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/persiana_Soccer/24245" target="_blank">📅 23:22 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24244">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EMRa5o1vSxrqXuezsEJt8CSEjjMo7moXNnSQbi3G09mPon9RgmF-vFbi_wLjXosJ-sYPx-9H-imjp41WzBBCKBYN2XmuphkNvSICH7mHdsfWvTEg8ZOk92m-dc044K0gw-Z0MmF-KXMtaO8r_ImEVe0eEc3NWjZKw7T1fvPIhQxdHmvJkRu1JuvLWB7mXS4i5yGKb7hZ6sAKXM2Q3Tc2TLhbzkIYlxqYDqGu7-EenVK1W3jx5ciR6B3HNHotTmrTZftlrZ6Ok4Z13WIa905stctF-3Lpl7HicyyNU9LpDvwVVMgkc3lyTEOgWtIA9aC9YhiYDOhrhn8Kg5O86JQehg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
پوستررسمی‌باشگاه‌کوردستانی دهوک عراق برای یحیی گلمحمدی سرمربی ایرانی و جدید این تیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/persiana_Soccer/24244" target="_blank">📅 22:55 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24243">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pr4ZwE62u6_23KZ3FOzcxs6VOzR0-9NL1KlfiIPv6oYaWJndFjdFXGaICuZI_QXGQLd4rxJr_UP9f70XtYiEKWW34BXReEl6hDG-xQI1AkT2JbL3_eB9JgQUAgP5apKVpEFaEdgGSbd2vMcuepVQogEYJJu2Zi4c20YFLqi7g8yGiBTr4c-VNwe_whgLhNG-3T79DNopFhFS2-LXbENUeEFou4ZvvMNw9C7R2hE3Iaf-JXl__19PUwQNM2cLh-4gCjs3uN_DdbiMbijolTs1wHEIdUUTQVJSE_5IZ_jGzmWeaevi1CM1PAIfK64ek24qr1o_WlIeVM26k3VHIIpapA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
🇵🇹
تمام گل‌های لئو مسی و کریس رونالدو در تاریخ جام‌جهانی مقابل چه تیم‌هایی بوده؟!
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/persiana_Soccer/24243" target="_blank">📅 22:51 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24242">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">📹
این چه سمی بود دیدم؛
رونالدو، یامال و هالند درمدارس هند؛ ارزش دانلود 100000 از 10
😂
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/persiana_Soccer/24242" target="_blank">📅 22:51 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24241">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vdf1hwEqD_fl2gU3D6lBA18UEPrJRzgfw4OPehfbal4bT1s0NggdQK5gO-uE3G1to4LnVzcxYFnKjBDDn1_6TT1Tw5zBJtSSGnC3e0cg62B16M2t8uzuw9ZxZSr0YcPVslIF0eZDdT44ai5oQHSbw-fHU_qg4ysH6txqc-MjDDHkqm5-RCOeU-cnAaLXapn5KGfUQh1hKAXjVnZKcRI-XeQ4KiYT3n8IGAEEGY3P7f1oiKkXG-ox8TnflteIGx-ZGbwp200-zzy0KSF1P3fuVa9HHMJ1lMXV5lJ5sXjskGnAjVhM2UnSG3u8ssVIDf_ClIo6reqTjmbDTxuPWhnTfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
بزرگ‌ترین تورنمنت فوتبال جهان آغاز شده…
📺
پخش آنلاین و بدون سانسور مسابقات منتخب جام جهانی
در کانال تلگرام Betegram
🎁
شرط رایگان ورزشی
🚀
100% بونوس
🪪
داراي لايسنس بين المللي
🌐
فعال در بيش از ٤٩ كشور
⚽
هر گل، هر لحظه و هر شگفتی را از دست ندهید.
امشب میلیون‌ها نفر مسابقه را تماشا می‌کنند…
تو هم به جمع آن‌ها بپیوند.
🌍
http://betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/24241" target="_blank">📅 22:51 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24239">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HPMZ9i2c3bGCnP-AIBkmhKZoDJV8wU13T5qX4FEtLffEoBB_QV15OHadM3_hToK4MWsUNTYjUdbz9kI9DxAjnQErF83C9QmaiXXQdNxIZ8l2U3rGeEn41XeLTK52MGfh0T7HtrNtiu6WkY1acSsfdkWOsmnsvJdvBPnkDx7oBXRPdZo9KPd7W6u-z0lK-mZT0UffLugdyiv_FTxelacCsAO5yBDEJK4ehm3rBjgp7DZgbT5OoLgtVVxH5LjPFd1J8pfpCXbpFh280-1JY2nKf4R1MXRRJ1Vq_YKbdk-TXmZERvf5Vh3De110Hr03p5CbTFKtVpdwokTShBtF3izMnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Zwyi_jpfhroN1bwREX3KpXFrOpodMa9KZxx5HfrByUBckwJGjbBvF863WbnRR5JPF-i5Ehj42LOW2CQUrA0oNaYmAuAfrvYs5SzH6TPuMi6rfehrg4-oNxE6sUheH1S1MXw-SfAMNwWFaGgC0R76KETDi7nXDzPZBl5pC59BU8uuxFuiTvQB4PEUH_zkQtwgHKlLElEFKA8SfQ2FBObsAh1A-JKX0TYzlcb7acASOEAZko94QOYi_Hww0qpZJ7pfBHONpYZYIVjqR8k-pV3bdEJUB_sWzwzs3cjU4S6x2CBnxvZt05ZbwDj8ZjYoMXk-tqO_twf7iyX7V8Ekw3lOtA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🤩
🇵🇹
تمام گل‌های لئو مسی و کریس رونالدو در تاریخ جام‌جهانی مقابل چه تیم‌هایی بوده؟!
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/persiana_Soccer/24239" target="_blank">📅 22:20 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24238">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d46a7b1648.mp4?token=BKGFkJp4Y3uq_WXu0WQ1rwIdG66-7JyYPPF1kttwg156eZAieC5aP5ou5Un9cMrw7jYfVussY2Z-ABZns-vnLISIldwyaV7B9OpePwKSo9DWMGlqQulUqcKJZ7G8LK7yH9946HlH_2RKBO-Y5CNldoM9wRi_WULrJTJLRgH9fwqpWQOIRdfDQtUoSShO5G-Lz-dTDopNajWXkyY_6F0-bjI6RijxjDK2l5I7Kw-MFkIi34U7HFf5LmG5kUWloeJpQZaCpFAdnp6-KLPr8GqooYoxEIpGDbpSEh6QwRvhSou_M1Zlkjn9dIT9m-kJoL-RSqJOSpd11enAcFTN9KHvRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d46a7b1648.mp4?token=BKGFkJp4Y3uq_WXu0WQ1rwIdG66-7JyYPPF1kttwg156eZAieC5aP5ou5Un9cMrw7jYfVussY2Z-ABZns-vnLISIldwyaV7B9OpePwKSo9DWMGlqQulUqcKJZ7G8LK7yH9946HlH_2RKBO-Y5CNldoM9wRi_WULrJTJLRgH9fwqpWQOIRdfDQtUoSShO5G-Lz-dTDopNajWXkyY_6F0-bjI6RijxjDK2l5I7Kw-MFkIi34U7HFf5LmG5kUWloeJpQZaCpFAdnp6-KLPr8GqooYoxEIpGDbpSEh6QwRvhSou_M1Zlkjn9dIT9m-kJoL-RSqJOSpd11enAcFTN9KHvRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
ویدیویی جالب که لامین یامال ستاره اسپانیایی باشگاه‌بارسا امروز داداش کوچیک ترش منتشر کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/24238" target="_blank">📅 22:02 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24237">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RWQX68bC78cFsBTKmjr1FbMDRe_zddXH8kdg9DHRDZZxDcz-LKQYEcL9B2TxrdkOWM32yEAo8dKltskteCj6krHfUaQPL86gYD3ifFzFE0cQhWv2vaAr5nyJjjzPM9L3fKCV1_QvJ2eq-WXWr2bZwDS1uVu_WULHqgytd8ozCdPfCZLH59yV9WUkprwJrwy3JN1MkigBL5Wy4d__KM3PPZMeXVEAHHb86p_grxVNRPQuClv79LUvB5ql3BodXFgxieUsNBGQj5jG8edWMx6Zyixx7_mRwRTXIn2JT1iKR6Ar-xOn5n9YF13aqALwfKtVgkGGtIoc8raqpUs7jFXVqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏐
مسابقه امشب والیبال تیم های ایران و فرانسه به صورت زنده‌ازشبکه‌پرشیانا 3 در یاهست پخش میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/persiana_Soccer/24237" target="_blank">📅 21:45 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24236">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sLvXjTG2w-TIzpvOnD-g6a49wHoEfqdBMtdX5Z4_TFgs-kU9BIo0dz-XK3kOLSgAIE5DgqiLPKENtHRgxdjeXndjWalua0dHV9XCdFl9quQy2jg3xHv-ajCKCOw4P1apiQhAWkCYLALTnhhAA_igGwxmgeGvoOAXkpZwemH1hUs1_aiE062S9zYddXaapSAtDFn2VbIRnYObgFnUumE9xnSVPUe9gG9o9tDaG4dGaFEdEC--lAyppnJzZGYdimqRJLr0BsHTMzXMpU2-CuSqfhJRzRtI5x3XbHb47Qf12m1F9ECktj6mTpW0GxR2yr5L7wBnaNY_Bb8mmcwN9RoMuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مهدی‌طارمی و سعیدالهویی، مربی تیم ایران به محض ورود به فرودگاه سیاتل آمریکا توسط پلیس بازداشت شده و هم‌اکنون در حال بازجویی هستند.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/persiana_Soccer/24236" target="_blank">📅 21:28 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24235">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P2ftSCQ-MyCwJjCYAHS6tVA0WrEFFUrHMdFkM-XfLLoK_rhdSQkE670Y3pZbtNrEk5x6BIgKSTbV3JDV3v_EgE-mCDyxBsmvJfJ0GAMA6BzHgaEHHkODKaTYEtQu3MQCCZqtWjLWtPYGp7ZAwJBIkwhoqd7sIs9p8sYYDsmR3WH0Y79fur_ydV3-A5HjHpbE1yK815KxcS7GEVc9-cnJb_SJcihM5IfGKCeJQYKFcVaiMmDviNi80kznDcYvNR7Bt_166F5AuQ4c18F6-cI832VJOM6bU3Tvi7vhPyioiu7FEvMZBp3-ONADcRmJ5_0gUWHqUqEjQsCSO81uaqQOIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
طبق‌ شنیده‌های‌رسانه‌ پرشیانا؛ مدیریت باشگاه استقلال ساعتی‌قبل به مدیربرنامه سید مجید حسینی اعلام‌کرده‌که درصورتیکه‌خودِ بازیکن رضایت نامه‌اش رو از کایسری‌اسپور بگیره و بازیکن آزاد بشه بااو قراردادی به مدت سه سال امضا خواهند کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/persiana_Soccer/24235" target="_blank">📅 21:11 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24233">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SPfclBCafyKAEDxl_jlupYg3k3gonjAbpB0ZwucPYpecFjf2jeyG60jqm1rx6vQt-VuXVonCbQGPA9Lu4TfUnipvOexWf18Iw2_8ttw2ZMRpdvRhGZZ-PXfnzuy8tcx4cDs8bSxJ5uU9jAmWymIWINLaw-wBlzIP24XhUKUCWCkp4qPfM_jFf46HnfXgnJ6nGI8KtQ2Rj2M6gSg2IKLjRIn-VH_SOq1lGHLYHLBCtz4NGX6RB7nDqaTeFFu0CnxpQkq-daMdIs-gmRGLNG-dnvikeyYhFfMME0qepIUONkB87bT1y6A29jaZ_onJqitGjzxSNAZ97CDtBFc_PChv9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
🇵🇹
ژوزه مورینیو سرمربی جدید رئال مادرید:
رئال‌مادریدبهترین‌باشگاه‌دنیاست و بارسلونا هم بعد از باشگاه‌رئال‌مادرید یکی از بهترین باشگاه‌های دنیاست. درباره کریس رونالدو بارها گفته ام اگه از او متنفرید دوحالت بیشتر نداره یا او تیمتون رو به شدت تحقیر کرده یا از بازیکن مورد علاقه شما خیلی بهتره.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/persiana_Soccer/24233" target="_blank">📅 20:51 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24232">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LVwgAEfl2ZrBajNKjsPssQe9CtjeiQKcfI8_hLj4aNXxn_f15ZSOzP-JrwVN5FAFNGogbjiDo5lpn-1YwybALgi6-w6snpY3-I6Fv26JXbiZi6C0P02r3k3Kl4qWJgKuuZkKepti9z7AhwgeyvSmsHRjL07xEd67SC1RfphTttGLP0ZLiIjgfMGkrfCAQ6Xrkn72RsyK7E154YEjDulcVg2qH1AE9uDdF2T7x6fAr2KYS2jtWldy51lCNCvVMnD34HEFuzzOvMm9aFwA6P_bqH_TxmegEu3YKtz-KgVdcERWj_6rxJfCgbpmxjfxVB2_d8vunxdXDh936lTLfHbGuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
قاب زیبا از دواسطوره تاریخ فوتبال؛ واقعا هر دو بشدت دوست‌داشتنی و محبوبن. حداقل تو کانال خودمون برای این‌دو و تموم هواداران شون به شدت احترام‌قائلیم و تموم امار و ارقام و ویدیوهاشون رو به‌یک اندازه پوشش میدیم که سوتفاهمی پیش نیاد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/persiana_Soccer/24232" target="_blank">📅 20:13 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24231">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dri2I_UnlYqmT95fDMaqypfEPbRdeQpTMVvxi0bL3oSCxdXX4LJ0hmUPV0ZPx7UqxlghqSBFcia_TGRraNBR0VqsM3zguzrHAViNjsMkZTc8iIO4vhadHwVXs5-qcnC0FUBf5efWjsqA-H-8KeXz2aWG7aCEp951EMWcZyam1zLkq1RgEOoJaWVMNIu5JNpYtHpmJhBCdIR50-IfSIBNj-iGrgsVrKYZiAS6MGQ4W176QyMHIjhV8ZaYgKbg7c2DGEQlU2WhBVLak0zSDaKA94Z3weTO-bb9cLS1LGEF-U8wxiek1-uWjQo1o7JQr1dgxC1XUVDqluW_KsM8UVaQFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
برنامه‌کامل‌دیدارهای هفته سوم رقابت های جام جهانی؛ عین برق و باد دو هفته گذشت. یه چشم بهم بزنیم میرسیم به بازی فینال و اتمام رقابت ها.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/persiana_Soccer/24231" target="_blank">📅 19:57 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24230">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f0_MS0f15GSFtoI1QuIeMjkuzwvA2Yw72SHtd40KpGeYYh2ksYTjPP9Z0-l0k3Z54PXDhnp7Qme3Ph0evg5aX_cBmSr5HffaWJNvt3JcOukaSycgkKJUzWzlMWsMgJv1ghRlefQA8hyJ-yu52WGADiJgvL2OBBiYbOnagRl_o-dCS7RVYStztpbKo9TXj9KwECG1vqTADspTNBuyDpe4l2pAetVCpsV84Hl77-Xth3ADHR7DLcUPFuezN_ZBdslrMgtnNMnzsYq7V8ic-uGm23JByg_gU3kKrNipkmAff6al6DUv8tliep22YT_IGLom3dNzb7XgDFZGwFj4Mz2Kfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
#نقل‌وانتقالات؛ آلخاندرو گریمالدو مدافع چپ 30 بایرلورکورن با عقدقراردادی سه ساله به اتلتیکو مادرید پیوست: هزینه این انتقال 10 میلیون یورو.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/persiana_Soccer/24230" target="_blank">📅 19:41 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24229">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VxOMV9j_hTxer0MxnjouBO-FH9euc56J_SggT6aD1_jRgR9jD6EeEo0YHhZyOu0yY29trhHJgAISDpTXGFqzNcBW1xF6m1FC4CuzdEQuhxls_ar9iUEWd3aM1If_azp_xETIYY3qBgIaYKWP2xSTUgIolxA2uvuiLPYemE92CpCZQAucklMwjFY5ZTpSObhWHteDUewmxb8WQRCZki1mHJiQgHW0d_8mpOthUE9aKFg19ib3aCr6JUGDSIed4oCMlS8jzP-RV59bzx6BgajQjjexGG7GWAnqy768Sqp76Ax07qfJ_nLFXBa4Ilc2iShyTZXM_MNnzl4p8ljIuDLyAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇬🇭
مصاحبه جدید جادوگر تیم‌ملی غنا: در بازی باکرواسی‌تمرکزم رو اینه که گلر تیم ملی کرواسی رو طلسم کنم که تمرکزکافی‌ برای این بازی نداشته باشه. صعود تیم‌ملی غنا به مرحله بعدی نهایی شده اما اگه کرواسی رو ببریم میتونیم صدرنشین صعود کنیم.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/persiana_Soccer/24229" target="_blank">📅 19:20 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24228">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Af1n8VkxET_L7bISQT_2CZL1oRzW_KR0Dt8jGokBsU2sdye29lwzI3MbweZUYI8ok_a8Muee-J_MTekTOrtT76toJrHc-GWJEPCu7VNlbedv9ReIc98R7xNRHRzGJNhq6MtmCE0QZWPysJ9VB0UC5PEVRrZ6GB0uOjDTF90rXsVIujFy9SQtXyjqn1FKwppjWKlgrddQXGtzXY7jAqGcf6WjuCKJfWBa971a3V88e30HZsb2kLLdYJbOgxC8dX4HqBo-WRsi2n3Hf3pa1P21qO4TG9Pbjdvf35rLffCsJjDNncrjjQ2NCweoTEEqSZURSD3vyVsR_fzrqj7u2IzK1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇬🇭
مصاحبه جدید جادوگر تیم‌ملی غنا: در بازی باکرواسی‌تمرکزم رو اینه که گلر تیم ملی کرواسی رو طلسم کنم که تمرکزکافی‌ برای این بازی نداشته باشه. صعود تیم‌ملی غنا به مرحله بعدی نهایی شده اما اگه کرواسی رو ببریم میتونیم صدرنشین صعود کنیم.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/persiana_Soccer/24228" target="_blank">📅 19:03 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24227">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PrChCaf88YVkW6vHosQbWzSQN6GccPSyOPHFTkbvQc6p50rpwUTkbz-o-KhuoaBBY1m6r64EK41JB4u9GY6zaPUSDu1ryrXFNGagzg9HHnoK1LZK6Z1FeJoN-V3cGoGTLhY_4Ir3uEBe_gzvIGwAH-5MkGvKhCDdxQGy9oRNRo1ywjc02o4XDm7FD28glTtTWIQ5WQFOBkOQNdzVo2xEqLgfOatLHwhF0NKqBbQ3b4pdvrzWQdz-Uvo3-yGk9Gt74rM18NatxgXGD-2tkgNj1uaqVmd9Mn9G67G-aa5MruY6S2IwlAEEdnQ3LqBCRngpYIqRJlOyAjC82Fr6FQUCeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
علیرضابیرانوند گلرتیم‌ایران در رتبه دوم بهترین دروازه‌‌بانان دوردوم‌مرحله‌گروهی جام‌جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/24227" target="_blank">📅 19:00 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24226">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc38571967.mp4?token=LidOh0dleElLjz1UGWC8ttwS9hJ6DKgBVP0AmXeGju1RdyKHyfD73n_fSURZYymw9_8tpxmVhTrdKyvzB5VHmxWpmGE_CZFON50mW38rtJFxdSWvEvLfwO5Ji_AnIGzYuxPiyKkky4t1-xUCdEiX0FTiGAWszmMK0ck60Qev2j06TeMNNlyMX32e7MFK7iQoC8m2q-FGoinZtABh8nwWPOCM5NYSzljhrD8UKeOHf-ywOJX67fpO_orM446JQ56ctjPqCPwDO-hLPFG51_ZRkzNG0pRZojDCu-WXLgOzt80Fac2AXZtj2TAo7DL4YIPnDpBBY4RzLgsuJXi_49DOXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc38571967.mp4?token=LidOh0dleElLjz1UGWC8ttwS9hJ6DKgBVP0AmXeGju1RdyKHyfD73n_fSURZYymw9_8tpxmVhTrdKyvzB5VHmxWpmGE_CZFON50mW38rtJFxdSWvEvLfwO5Ji_AnIGzYuxPiyKkky4t1-xUCdEiX0FTiGAWszmMK0ck60Qev2j06TeMNNlyMX32e7MFK7iQoC8m2q-FGoinZtABh8nwWPOCM5NYSzljhrD8UKeOHf-ywOJX67fpO_orM446JQ56ctjPqCPwDO-hLPFG51_ZRkzNG0pRZojDCu-WXLgOzt80Fac2AXZtj2TAo7DL4YIPnDpBBY4RzLgsuJXi_49DOXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
۹ فکت‌شگفت‌انگیز ازکشور‌های‌جهانکه‌کمتر کسی میدونه؛
دوست داشتید تو کدوم کشور میبودید؟
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/persiana_Soccer/24226" target="_blank">📅 19:00 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24224">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0eb571605b.mp4?token=IKPr9GSEIWm2ESygyBGk9MmZJNlp55cOiNu3aaIu4z33_qk6j3NiBcZE-O34PZBuemPYZ1UYhkOmPN8Q_S-PBsCVD6eyiPFwdsaGpV1-bvKYcwDzFpDrDRqsBBMJ_ssxcGZ6T0Rk7egm4MraCuq4fJg-hMgJgnqopvQZ4nOWizOo-XdYldwmXo1RGhOyIIc7ZOEsy2zFth9alMTzeaDel1u5TaJ75QEyh7RdH8QX5JazDnt7vwU5JFbH2Lsb7lTQTEZ2tcndGDMSEdADB2_DbuU0_cka4yIZ5Q0xa8eGZuq5Rk9BCtlICdQ2b17tYjkHvrF-hRDRItN2JdlqCzakwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0eb571605b.mp4?token=IKPr9GSEIWm2ESygyBGk9MmZJNlp55cOiNu3aaIu4z33_qk6j3NiBcZE-O34PZBuemPYZ1UYhkOmPN8Q_S-PBsCVD6eyiPFwdsaGpV1-bvKYcwDzFpDrDRqsBBMJ_ssxcGZ6T0Rk7egm4MraCuq4fJg-hMgJgnqopvQZ4nOWizOo-XdYldwmXo1RGhOyIIc7ZOEsy2zFth9alMTzeaDel1u5TaJ75QEyh7RdH8QX5JazDnt7vwU5JFbH2Lsb7lTQTEZ2tcndGDMSEdADB2_DbuU0_cka4yIZ5Q0xa8eGZuq5Rk9BCtlICdQ2b17tYjkHvrF-hRDRItN2JdlqCzakwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
👤
دیگو دالوت درحمایت‌از رونالدو کاپیتان تیم ملی پرتغال: "فکر می‌کنم دیگه همه بدون کریستیانو چقدر توی کنار اومدن با انتقادها مهارت داره‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/persiana_Soccer/24224" target="_blank">📅 18:47 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24222">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nBNNwikjtCcVD9RIDl2tPEEEncv8gbBB2QOOqqSuww7W4gReBj-WaSDCM9ewL_kD4T2eGSNsgKYJ0iaBd-bVTOmasge3wjm8EQtX13DkLeYwFYlH-hY0wtKGIykFt-1A7O933d3Wlep_0sgKIQAe7UE3kRv0Tp07Rc4y8PGZLB6COMEdzlj4vIyItiqqsAZUoOSAA4B4aoq_SLdH5Bw9rxr79YdNjaj6KpRpCopG7_4v0KvjAerXPmL8q8HYwh1OAjhBjlz-8bbs07IqADpCYRUsnKJN8MRKb_fSTZqH0AHPhuyJta3E9VKN5_tjRozp1X-LDI3KAt1gGPfDyGM-GQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rRrveri40hffO_5Eb-i33mxGKi6PaRDyW3qi64e_BO4cWwcYK5S7z0w3gm2T3aulkpsq4rjI_iQXiBmnLfGSk_Be2uU7o1MWV7usFJfgUfPedXwGue1BHW-Us1l0RHX4qV8wvpkAi57eaO9uQrDll7Mf7pKTr_M2a92Dv7LkLtuP-P_2dbbvevlAxPrPS1JYTJSQKrPxIaU4oC6IiksSuZ5fP0F5zPogprmcaS6BsSlZvbrAHLNF61B5EB2xK3_ObDg0UBldKEprRiX99fVDizbSRAl6bTpZA1wE8Z4mI1e7_G5oOb61fhPiOxHXePe5w8H8SnqX5DjmWiM3MeCdjA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇲🇦
این هوادار تیم ملی مراکش گفته که تیم ملی مراکش به فینال جام جهانی راه پیدا میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/persiana_Soccer/24222" target="_blank">📅 18:34 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24221">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QRGAiAGnNxHC5joeZ3LQrCJyDEKJUsvuZ8AEmwhs5elf3z6KF8KkZcKH542G_-8cYaFSKz9-t1ujm5TNaBgpENslVG1Oga8hFA_eONwCWkpY0GxiRze7q0HWlxXAkkH-MDYzI1j3fXXEKRzMb7TxZhRdbCRjMf9XkuGW1k567sBFHRNdCiFxhROvXPc1vnF2L7e3IC6spxTGeIcs9w0Blbxt7CARH-BZsYRyHriY4Vt1fCJ8ZFx4PyZWR2XgREmZS9db87Y3JITGlW3yV02P6f3XGSqpI4VH9ty-wy_1cbMUC9PUnfq2V0hPQF2qjupEvW3x5F5073D5ga5l2K9VVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇦🇷
باشگاه چلسی: انزو فرناندز بارها اعلام کرده که قصد داره بعد از جام جهانی به رئال مارید بره. ما مشکلی برای این انتقال نداریم. با باشگاه رئال مادرید به توافق برسیم بند فسخ انزو رو فعال میکنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/persiana_Soccer/24221" target="_blank">📅 18:04 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24220">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O6ZKx8TI6nlhQkcMuQ2zsfyW_WRDfTB1f-_pY56AXt15frQVywOYVHs7BSuNA0dapqbJmtm_DXkjMjxJ4bCHsBScbGb67LStqRllc35yfccOSY9GLLpO0_vdn2G3mEPMpsLTuIRC2NldZe2O4_mCAYotcGlyVTiT6x7hgxK4RWJ3q_r1BsLFQHjJC4zv7OGjeoGpL96w10B_V3Eq12-1JYxTY57a8Y-8SFxXvrlzcSlEWQ-ZowRd_FIq-_W7QQqJWIWhh2MG5M94VhyB6Pm1MJH1yBAB7aa1O1AsZAyMwKQrh06UyB7_AlGbU51-XSsoiWoE4nCJJCpK0RqeZc6s5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق شنیده‌های رسانه پرشیانا؛ درصورتیکه اتفاق غیرمنتظره‌ای‌رخ‌ندهد و اوضاع‌کشور آروم باشه منیر الحدادی و یاسر آسانی هفته‌اول تیرماه به تهران خواهند آمد و به تمرینات آبی پوشان اضافه میشوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/persiana_Soccer/24220" target="_blank">📅 17:46 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24219">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/btpJM_SNCdBkDszeNWrGvlQ2BYtD7NNrSPl8w3ZRL6MxagfPC5vlsrgE_PXfgTyfQSuErHOqIbT9Hl-cT6lVu5C5XK0NGU7fTbORIhj2c50nwpf5OxOcuvdzTpQVj7XYoOJExpieXcQkuOmja-Qh65dmU3xrK4IwWwNRsX4VEMilhyX3qO57kK62TDjPZCTJYzsrTNQUekFbl7jAtBXFOvogix-hDEgxDU_FjY1P7BxwcVDAHyh9YF-wwT_AVaU050sjR6Vc0f_fONVgiETnWk1dxVjZXX_KL-icubqyfXNvf63qSLUtgYxAPWU_haLIF9oe_wec-loxAY9dRHVKjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
علیرضابیرانوند گلرتیم‌ایران در رتبه دوم بهترین دروازه‌‌بانان دوردوم‌مرحله‌گروهی جام‌جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/persiana_Soccer/24219" target="_blank">📅 17:40 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24218">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dfw5unm_X0lJSfIF2_tlkXPohVb7fOpsbJICqinaCW-dwSTV6dKU-5VZzz1gSzsmH2Lf66ZW0dNzYlaSgS0a-5wyPtbOsXNIIxuHJkYyfLJpN4h8bNQwAGR2OCQ7lobObTDdkfwqOAlwdoeg6M00hz56zu_omM3kWPe-sN_Ddvc-Xrd3hAQoZvYDd-VcPv3vA3t3PxJg9atguKghOT5DmSXj1k7yRoWM1XT2S4lV-r5m5LRB0NuFV4WzMFbA5Sx42_uyoTIRfD7W6HuXDVkDquDe_bufcv92FlglCuEcbQZcOfI5GjAWXe23md0xeftTDvbCxnrX_egPUb0OoJiYsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
👤
علیرضا فغانی اسطوره‌داوری‌فوتبال ایران به عنوان داور بازی جذاب کلمبیا و پرتغال انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/persiana_Soccer/24218" target="_blank">📅 17:30 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24217">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QL4nbtAGDkAIDlXKIcPmAKe91UEQWAowxVUWkYs3dbBBX5CEIIj4tz9Q9CrbU7S1Iyk1qfqzSsaqvyrxx47qi7OtJfzg1t82IKra85zs7rjRipxln2pF-iRX0QnQg5LOQgViKveumsdFd-kU6IX95uTWlI2D6DBoP9uGLQ-EutiS-NF09rVyKE9V8mSWcUnJPakKPcXrufWEFvGbsa1P7cuaOOakISUUDRa4bnmMVs7GExL7gmUmanpHD6kuETlzVO21XLlHFdPw3sXMvYTa_p-vVilaC9rq5u1XIixJ5E-PRZJBhoZKRcQKU3bCgakoRcUmoQG677USHfmyTu1V8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
جادوگر تیم‌ملی‌غنا: گفته بودم که اجازه نمیدم امشب هری‌کین موثرمواقعگشود. همین تیم انگلیس دوره قبلی‌شش تا به‌تیم ایرانِ کی روش زده بود اما امشب حتی نتونستن به بار دروازه مارو باز کنند. به کی روش بابت صعود تیمش تبریک میگم. هدف غنا حضور در جمع هشت تیم برتر…</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/persiana_Soccer/24217" target="_blank">📅 16:25 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24215">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/feLiIx9xXNdInz-THcnYelHuzXVgSojZBotpSZtNan0GYmdYLT2vrXc8ZrYPN-k7rx3EqHiUtbNoc4vA4EQK2ZIydpPl9S8T5VBlTsnab81j4PfX5od5PwoGRz4DgLn3n_vq1u8xgOlpNJS9-0tZSvLSROZqq8A3o3Mt4DhVhKgBfQ_A6HyXjrxZsjBDlSP2G_L9V2_U-6x9g0fPVqJ9dSZAFS27BZJhBvcBLrmq_HDGk7AcES43wLUKgliCeHvcIeDYrOfJneJEm0mUcADiz0dNlw87a0RVdJsdgyIB_CAutgwQ4aYsJiMfJ0vr02-WicjhDGryntFgjz_t8ta20w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NvKG9MJYkYhFg7OaDRMNeHKWYfrQitV667KOSubkM3sDw9aeomTX3a0e38VTn5SxxjkgeZb5KDPSZ8Y0XRmf1bZ41NTWWPhJ4HVaBztgvVKI8hcwtHctI0c_clkdaE3B-WMXA4aUwyXZ4UXxXEp-tPlEzVNpbMv-YKHlpnEP5YXufEr6AUACvj_9dUV5a-UchvkWWgKmGOM8TRy-hKB_diDJCYKPclwVfPdnpBXwd14z0qWz8wofAOF4IMOeBgpuZC8xdlduljlyvnT5M5KCssiTOCzqKHR49-FkEt4kaIK8-Re8DFB_GmpnP46jNUxPYk3kvR425kzwCn8mO53kuQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇲🇦
این هوادار تیم ملی مراکش گفته که تیم ملی مراکش به فینال جام جهانی راه پیدا میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/persiana_Soccer/24215" target="_blank">📅 16:10 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24214">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a79050b237.mp4?token=NvVYAjXa-7TpRbq5W7VjwXGVvtWsYkB77xT4bGVmtcsKu2iqaWeVmMaE2eERrdsjSuIJLrbDeaEWvx-DSdh0nAtCI67eN3pYHEevmJBqpbJA3oz2LPm52x2nlAv_ZY-RzvogjUGcoirscmbpr_JogAwYMtZB8uTlgQyXAh54Bq0bm1f9aFxnxY-jjmeQSDg00NjfG-iS-d90x8M6D05Zi39a_atMK-qyDEgqEk4LfXFNg8sPhoKxIJEz6Enfd9_iizMXwLbQBf331yxw1zBI8NTNiw-pBVPqUecVySDrRbGokQnJmV1eg0nb1xA7PBoHvOyq7xTFE20BUBSPFMqROQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a79050b237.mp4?token=NvVYAjXa-7TpRbq5W7VjwXGVvtWsYkB77xT4bGVmtcsKu2iqaWeVmMaE2eERrdsjSuIJLrbDeaEWvx-DSdh0nAtCI67eN3pYHEevmJBqpbJA3oz2LPm52x2nlAv_ZY-RzvogjUGcoirscmbpr_JogAwYMtZB8uTlgQyXAh54Bq0bm1f9aFxnxY-jjmeQSDg00NjfG-iS-d90x8M6D05Zi39a_atMK-qyDEgqEk4LfXFNg8sPhoKxIJEz6Enfd9_iizMXwLbQBf331yxw1zBI8NTNiw-pBVPqUecVySDrRbGokQnJmV1eg0nb1xA7PBoHvOyq7xTFE20BUBSPFMqROQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🤩
ویدیویی از تمرینات لیونل مسی 39 ساله
؛ نکته جالب ویدیواینه که تو هر بخش آقای رودریگو دی‌پائول فقط چند قدم با لئو فاصله داره.
😂
😂
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/persiana_Soccer/24214" target="_blank">📅 15:55 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24213">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bLU6nzp4nwv7-uEieBwtdUDvu4oQmdbNbQBpjR457rGZtqDLDjQqh6U85epSVemUhywZgGdCZ8W7WdHvM1gQU76WBV5peecOWJpfe1Uhwrq0jCRJCSfj9YQJ6korE0i5OgO9HFMNmAUk3kcr0ri4abH6DXVOHBAyK6uGJ6vkXaRwZpQgHAOLnqQ1pu4WJCBHUnTvP1FPaWblRLdv77xCjHs0PKEmDrRSWFSIC41o2X1mvglOoyDcogaJqJFxmEcweYXpMh1BFnFVqHlYslJyrO9bfCxEj1RExZ6oZofwz4bQFqKtW3Njnm71L9XshUP1-94Atw-5ZRZ9V0aUeqHySw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق شنیده‌ های پرشیانا؛ سیاست باشگاه استقلال در این پنجره نقل و انتقالات جذب بازیکنان جوان ایرانیه تا درصورت وقوع جنگ در وسط فصل اسکواد این تیم خالی نشود. در بین بازیکنان خارجی رستم آشورماتف، جلال ماشاریپوف، مونیر الحدادی، اندونگ و یاسر آسانی در تیم ماندنی…</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/persiana_Soccer/24213" target="_blank">📅 15:41 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24212">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CQaS72MmZZ7QCIk_6_ysa8WCCnREU5M2DDf9xxc6I3OdC9SdBY52xgLxQNa_c0S_v9xOEApFF6NJG8Da5G-Kori_SxaEZXb34QjNsRleBxycqNtmDGRUUuibuN61UH5krHMQTyXHyXfQWlu9bgeDm0PY9KPhQak5UnbroKgU7ouqXUih017Gr9Ltw0pF7GKgvgCsNhOLyC2e-PrCL-SbXDDO0pXtJdpGfIVb8H84LkpUl4Q6blooxEWqAud6mKieWW9370A_Ox-Hp6md3qGQa_iuiPsrKZ8dp6A-FEjuS3Jq0T7W5dcgZZEZYU4RSHbj12tQjHGd-aZCLp14CXDiMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏐
مسابقه امشب والیبال تیم های ایران و فرانسه به صورت زنده‌ازشبکه‌پرشیانا 3 در یاهست پخش میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/persiana_Soccer/24212" target="_blank">📅 15:25 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24211">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q3Boq5jWYB8JVWJrVIBA-Fo8zRa4-5RC9MzbsUkI6K_G4Spv9PX3elmCGxFYdkTNKcTmx6gjS_Z8hd1i1FS_Wz08W2dV5ubGNUuLbzZn-6-DNF5EphZveNqrJfzoGOjqD_KgoUpxPCYwnwZzFTYGC_sQdq90x4oTKHei-nWjp6kylSxRXR4CD3XRi26zOinv8AHhPEQpflamxoUxEl3Je5Y1ae9Jinbn-fU1dzb5sqRjuftmzbWJAdAailYucTdAjW4kDrDEl24Ql1AJT-Gn2qGMmDglnMJcLgtvFOE7Bl9iTGNIMIQid5lKRisNtOvxnPWIbI0NOVWfeeYvSvkL-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
تیم‌هایی‌که‌تاالان بازیکناشون دوبار بهترین بازیکن زمین انتخاب شدند؛ از ایران رضاییان و علی بیرانوند نفری یک بار جایزه بهترین بازیکن زمین رو گرفتند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/persiana_Soccer/24211" target="_blank">📅 15:18 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24210">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eqrHFGxnRxN49uxXM-hOGXLNqJ056p5kZB2f8gRM9ouTEAmn1WLjRJv9tGQCcl5oCs-SFfaDXwUCxB8RLzeInM8TZG6nCT3Yhq0NvhrJLGwjZwTMaulaPymMo0VXRIuxt2Zymf1BeWgQH-5c785TAAAp9F-d1Yz85AN9gQbVCbshABHF__WXVpwALOW07RsrqssF8R6o_0EIix_SKCjt_rvNC2jhVaFKNi2GW3C9BOFtUmtRGJzYGy37_2-0J-Arlmio-MjRAFo7FJq1nw1EJ55ayIMTABdKsH5TOB15KYQZXi66CYxrGtmEDG7EIjtAIRzHOZfrhh6kXpRD1Wevnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ تا دقایقی دیگر جلسه بین مدیران باشگاه پرسپولیس و اوسمار ویرا برگزار خواهد شد. تابرای فسخ قرارداد دوطرفه به توافق کامل برسند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/persiana_Soccer/24210" target="_blank">📅 15:06 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24209">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LivXQPeQDAakW8Ql6Oo9oHUSPaYkjZ77xZn6ngI92N0laP1AUxtUcQw_L5aWT1CnakAgo191b-rWaATJHXCFLHlkoQZ2yDVAu2xBtjyQYIa5t8hAbgc1XMcQFrhMP1hXqKPV4ZOro4gSt0gPBRGNovHgWfc1YSGtTPUQnsr6voYOzWYG8PR0LujkRNucPrePD6wVgSq9Pb_nJn14wJMfBtP_xTU8WUHCMkbI7VgREoaCwH2uq1UslApVp4ZSczyttfeaGUUPEeV6WYJKrGKvDl_liR5ZXt6CZ1IMUfzFpoWK-cim4VrHmp0T1ikbTg-saWrAkHGsS79pCouEb9VIJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
👤
مهدی طارمی کاپیتان‌تیم ایران:
بزرگ‌ ترین شادی صعود به‌ مرحله‌ حذفی جام‌جهانی این‌ست که مردم ایران به هم نزدیک‌تر می‌شوند. اتحاد و همدلی بین مردم داخل و خارج از کشور برای من از هر چیز دیگری مهم‌تر است برای رسیدن به یک هدف.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/persiana_Soccer/24209" target="_blank">📅 14:55 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24208">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u8mP8dfcQFeBK2zzF_5Gt49OI8n-uFjUNlryxO3jXxwrll7FYwHyPPOWJhCs7rHN2nZeNeOtbqjTWu_0EkzxB0DuejQqf_TbN0Fx2m49jDQVPISsp7F08xg7rLd-yD-J3LJjiBba7VZaUuN5C1CliUbzq0AorUXtKoI83XZJYvn6o01PIOdCQeU_8ZP0URgNjulvJXu3qt3f9yM1QGLw_VlD55-rNYS9nXj8ilmC8qDX-G6BuDR9n5dmxug4J-UV8I8WKZqGeokRTYpiu7ctB55xMAsv7GpLx68QHd2H-ROKzoPYyTSSGTpNAFZjeTfvi-NBfmhus045R0Ro2-O0qA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
هلدینگ خلیج فارس و باشگاه استقلال برای پرونده بازشدن پنجره نقل و انتقالاتی آبی‌ها روی هم 850 هزار دلار هزینه کرده اند. وکیل ایتالیایی آبی‌ها هم‌امروز ظهر ایمیل جدید به باشگاه فرستاده و گفته شما تموم کارهای‌نقل‌وانتقالاتی‌خودتون روانجام بدید فیفا پنجره نقل‌وانتقالاتی…</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/persiana_Soccer/24208" target="_blank">📅 14:35 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24206">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a203ff625.mp4?token=RF-WtG5O4wt2PsMVjvf6kCuRXU89EUYbhudJoe9w50cNdbC4_7Cg8oWOw7YgVaGansF4IBYI6fAY2-WBFXPtEDpk8Mwyyy4R0zaFekdHy0cVqiEA25D8Dm7riLMwYb7gxKSmNRxpc6rWDj35f3J2R2BJ-4ijPSktL4RHu6DbY3jxmjePVtYVAiqgVYdRvKBy0jej6lIYKX15f_Ek2nVx9Yk2qw2tWCbcmgVGO4jwRn05tN33XsnOLfhas6jAp6H5tuQPNNW6M2CIdo2w7ztIagtidrGZAh-RUXqobDRuNTQG8MyTfMMD3YXuC8KtDzSrsMCxyY6BVEklBd3bQWSDuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a203ff625.mp4?token=RF-WtG5O4wt2PsMVjvf6kCuRXU89EUYbhudJoe9w50cNdbC4_7Cg8oWOw7YgVaGansF4IBYI6fAY2-WBFXPtEDpk8Mwyyy4R0zaFekdHy0cVqiEA25D8Dm7riLMwYb7gxKSmNRxpc6rWDj35f3J2R2BJ-4ijPSktL4RHu6DbY3jxmjePVtYVAiqgVYdRvKBy0jej6lIYKX15f_Ek2nVx9Yk2qw2tWCbcmgVGO4jwRn05tN33XsnOLfhas6jAp6H5tuQPNNW6M2CIdo2w7ztIagtidrGZAh-RUXqobDRuNTQG8MyTfMMD3YXuC8KtDzSrsMCxyY6BVEklBd3bQWSDuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دخترای‌مکزیکی‌انگار خیلی با پسرای کره‌‌ای حال میکنند؛ هر کدومشون یه پسر کره‌ ای پیدا میکنه یه ماچش میکنه. ببینید چیکار میکنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/persiana_Soccer/24206" target="_blank">📅 14:16 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24205">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8cf62dd03e.mp4?token=Q4x_ONF9-UXnuUG3DZGQf8VexCSq3DnOy1lqUscC4VcQxEDoPLi0UIfXvnOdlhsFsENF-E7uaHmAPRqo4Rd0ZptEjmWZWsxvZSj3ab8aeFOIEHqRJjxwEngTDTT24v8hlgPmTLQFcDXCxSrngtbLb9LbrTqOW0qnDtMs9JJyWNJURAtMAzgKm8e3s2lBt_8ShbNJ3_yc8tBhcKEaJJ0-AkuOrpcB-Wd_QmC_OGoYmCqwA33UuTiiVdHZ1vM1Mkp5Uzc2v-UBuaPGjEUW36bd-xjWh_iOVZ_jyxWdv7QKyYePlYJGTaENCuvWxFwrs20lC7wuWt7wTKJRKo66Qvl2Bw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8cf62dd03e.mp4?token=Q4x_ONF9-UXnuUG3DZGQf8VexCSq3DnOy1lqUscC4VcQxEDoPLi0UIfXvnOdlhsFsENF-E7uaHmAPRqo4Rd0ZptEjmWZWsxvZSj3ab8aeFOIEHqRJjxwEngTDTT24v8hlgPmTLQFcDXCxSrngtbLb9LbrTqOW0qnDtMs9JJyWNJURAtMAzgKm8e3s2lBt_8ShbNJ3_yc8tBhcKEaJJ0-AkuOrpcB-Wd_QmC_OGoYmCqwA33UuTiiVdHZ1vM1Mkp5Uzc2v-UBuaPGjEUW36bd-xjWh_iOVZ_jyxWdv7QKyYePlYJGTaENCuvWxFwrs20lC7wuWt7wTKJRKo66Qvl2Bw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
کلیپ بسیار سمی که صداسینا پخش کرد اینقدر سطح ریدمان بالا بود که از آرشیوم حذفش کردند.
🔴
از سر راه کنار برید ایرانیا رسیدن...
🔴
علی بیرو توی دروازه یا که نیازمند
🔴
کنارش شجاع و کنعانی میشن پدافند
🔴
تنگه ی هرمز ما تو دستای سعیده
🔴
شوتای قدوس و رامین مثل خیبر شکن
🔴
مستقیم به قلب دروازه ی دشمن میرن
🔴
ترابی دریبل زنه، نعمتی هم حامیشه!!!!
🔴
مثل هایپرسونیک از لای دفاع رد میشه
🔴
یه طرف میلاد و از یه طرفم جهانبخش
🔴
پهپاد شاهینو رو دروازه ها میکنن پخش
🔴
حاج صفی، حردانی و یوسفی مثل شیرن
🔴
توپای علیپور از پاتریوت هم درمیرند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/24205" target="_blank">📅 13:48 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24204">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qsPkkWtGXPc5Qlcuwtv9cXSw7LA_ILA7LK3T7EQFkCXS1XEMe3_Kpzqo-edkLRFbRD8e8_G_Q2NF36WHYhJ6eMTJAQFCvXvVCa1hMaIsePmzuIkK0VafeUzTqOjVp1YXdVVXP4D0b78EhK3UQtTLYmWEmbTlsYm5dZRyVrXgaX0V1Ek6lFuFpU53Y5SBHzbd9iBUuQ6hfnBerVWFoioI7NOsr59aDo4zD9YOYRl_9jC6d0ctSp89MAYNqEQ7ttA5Z4GCk3ies_LpGYLivv2Zav0SXEYHaegE-wep7zXHzbiZB-Ae8KXwIPBqatST2cRcNdA8N9ZD6KnptzbKuTGWRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
پس از پیروزی پرگل 5 بر صفر شب گذشته پرتغال مقابل ازبکستان در جام جهانی 2026؛ پست اینستاگرامی رونالدو بعد از گل اول او  به ازبکستان تنها در هشت دقیقه دو میلیون لایک گرفت.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/persiana_Soccer/24204" target="_blank">📅 13:40 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24203">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WLpnOaQamylql3WclCRRkrbm3JmqY_3wy-xAxlvAQwJ_256o80XEyDuCTJFZKY9Yl7yIAtlZU3oCGXeWdbMFqcXvVeIN0NK5jWD0YQedMdmuF_WCqHxQF24ILsxELD-R2rImXkyvnVeUGty8zOGbb3D5mfy3BsNzhhX8NM2W1bnk6e5ui4BFeqUdwnlOn3K6-lRsiPoq4jKwfa1kZPO95xTwNdUweMNYJCYbS5ZW4Un4vU4CJoeMsIw8JDkkIGeGP0_s7lzXa8Cl0GB6tVj0gcSXBQwOsajNhWR48wXCmhFcukQUoGDXDl-C3HjYgMqXlR4qZyuF1HqfzozSREQdRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
👤
موتورگلزنی فوق‌ستاره پرتغالی فوتبال جهان روشن شد؛ گل‌دیدنیCR7 در 40 سالگی به ازبکستان درجام‌جهانی؛ رونالدو به‌اولین بازیکن تاریخ تبدیل شد که در شش جام جهانی پیاپی موفق به گلزنی میشود. این نهمین گل CR7 در تاریخ جام جهانی فوتبال بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/persiana_Soccer/24203" target="_blank">📅 13:06 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24202">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AbgTswVJ_8OhY1drYPBf3c6AtF80XgWRB0ub5coMvL_qLMQAbcqEUsm1UICdQKpU0d-C7ezn5G5v_rpQF2w7Tq4lFvl_vkECXLc--TE4C3P9XY0iB0X0IX4YhwgDaH0hBNSnD1JGNfxpDPES62S9j1lPc_TQ6oR-aYtJdbHtDc-BKmlCxn-7S_wH0Vh2-BCeB3_oYyQs9ZLRiKVFElr6Inwumao13G7eawiR-Jz8ZzxDZ6e_eA5S0rbvtO9WjTl5M7_KuNEHdtZY3mGG1zLVaAxDg1FzR7V-hR9yuOyX5Zsxo1pn1le9AWoo4pHdhsXRFKEK4a6WbhB-oK59-M_nHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
پردرآمدترین سرمربیان حاضر در رقابت‌های جام جهانی 2026؛ سرمربی‌ایتالیایی سابق رئال در صدر.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/persiana_Soccer/24202" target="_blank">📅 12:47 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24200">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QUKeT2jIabKY36erL7yJvJi9STrMwb5x07u5cOUM8u2z8Z32GVvMm24jJwuhtYo_nlqVaHrma6Qn4THCUIeTZMEpPZMbs5O021_-6ev4h5ah4w5uoIPrRsVJb6NLYbAWIVWoTJ0q4yiI285gL8UQN6OwQhwebl0OFyDRViJBnlh2sGDYNLVovKI-sNTxIIftPKdu94c9ChWab0a10Uq_c5JTDALuWsbKkR7Y3hP8Iz_cuF9mEp7UHS_fbWOyANYlIM0cfQos7_Dk3SnMcI5Xqa3GvGZhu0N1qoJ9MBKmKm_PzASbvEjUCSKquFXjRhg8WENrRmlsXhZWHcG9hq4mLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d824e9cab0.mp4?token=C1kQd37WklwbKbTzrxDyZmcHrQvO_pcrfkM6-dKBuKs4zP__mGKir3lr93PufyaEIcki_qD9PsrL2jn7Cf1lymNHdiar776BJ8qYjracwHjbTHhux1pCJI2a796H-WGa-r2dDuoy_LNDN_GqpVM1yLd-Hc_NaO-_tL8i8adNxteGbMYly3Y7eDizMy4gKd3pcQuPbnMzapU7YcKfzyiJUj_BjGpN5fyD5CI7s9E8wZAe7_JgAyrrPRs5EL1KjsSffAo85hY291KsWMxWZd4pZDDybigUU0g1BVt1tXqkMo9Ef2vYPpqJeZfHxFMxIBVf_Zgbek2FjYXKt4WFGgklbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d824e9cab0.mp4?token=C1kQd37WklwbKbTzrxDyZmcHrQvO_pcrfkM6-dKBuKs4zP__mGKir3lr93PufyaEIcki_qD9PsrL2jn7Cf1lymNHdiar776BJ8qYjracwHjbTHhux1pCJI2a796H-WGa-r2dDuoy_LNDN_GqpVM1yLd-Hc_NaO-_tL8i8adNxteGbMYly3Y7eDizMy4gKd3pcQuPbnMzapU7YcKfzyiJUj_BjGpN5fyD5CI7s9E8wZAe7_JgAyrrPRs5EL1KjsSffAo85hY291KsWMxWZd4pZDDybigUU0g1BVt1tXqkMo9Ef2vYPpqJeZfHxFMxIBVf_Zgbek2FjYXKt4WFGgklbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
اگه جدول رقابت‌ها همینجوری بمونه؛ پرتعال
🆚
آرژانتین در یک چهارم نهایی بهم خواهند خورد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/24200" target="_blank">📅 12:24 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24199">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FfPrEvNNshF0FimCE4fH-0DLs4MdAO1BfRrz5YbmZb_Nda74PeSpdnfpyzPDrN-wkYLMjs6Oq7_K7cbZHo50P8q3s4woNhrrMlQMBJQrXm3zjy4pWYUtwdIXwt3NkuoRYHolavYAwb9fZQFFbDzBgURXnIAANQsBqgT0512qC_eDGgq0MUAaT7foMwlFMMcO8XLOD-lKsMuqbIX1-nGxWyXhkfValeEmzNZWfa8-bF0LxIoNu3MjcBjRdGeUKZ-9Bj1Rn3XJdlikVSR_FuFAaU9S80CGrfjAGzf3r3_Wj4zfmJkygJ2nL92yHCIBBMJPvbA0uBd7EgWQ_wXZW4gINQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
پردرآمدترین سرمربیان حاضر در رقابت‌های جام جهانی 2026؛ سرمربی‌ایتالیایی سابق رئال در صدر.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/persiana_Soccer/24199" target="_blank">📅 11:58 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24198">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2111536884.mp4?token=To6BlIMVgiklnSlIpGJsJEwx5KqmVdbKi8RCX48mMGf4At40IuFpCc44_YjUJpcWvBbbKMMYcdu5HO1VER4QbaX8mpXdX9niiAEjVSOEXG9PSsdSXJGs58y4FdToucUCnPZmp3-23N6G8lP186tvWsc4nuw9aDWEqSD8lOV9cxrCecEH2xo2BcbKhcQ7Glcxdml2VBF9abxpHdjpghiis1VbhL1GUvneE4pBLY2VDi9KrTjUxBJhFvPwFxmlKCJvGLgfC5Jv3_njoC0MziEm3N1Zc5ZdhKbgXx0goS5YGlc0O1wPCK4C_Si3CzblyTnr9r-Iw_ywIqzsyl66fbSNgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2111536884.mp4?token=To6BlIMVgiklnSlIpGJsJEwx5KqmVdbKi8RCX48mMGf4At40IuFpCc44_YjUJpcWvBbbKMMYcdu5HO1VER4QbaX8mpXdX9niiAEjVSOEXG9PSsdSXJGs58y4FdToucUCnPZmp3-23N6G8lP186tvWsc4nuw9aDWEqSD8lOV9cxrCecEH2xo2BcbKhcQ7Glcxdml2VBF9abxpHdjpghiis1VbhL1GUvneE4pBLY2VDi9KrTjUxBJhFvPwFxmlKCJvGLgfC5Jv3_njoC0MziEm3N1Zc5ZdhKbgXx0goS5YGlc0O1wPCK4C_Si3CzblyTnr9r-Iw_ywIqzsyl66fbSNgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
ابوطالب‌حسینی‌شاهکاره؛
میگه تا بازی بعدی یه 6 7 سانت کم کنیم تا قهرمانی جام‌جهانی میریم.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/persiana_Soccer/24198" target="_blank">📅 11:51 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24197">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👤
👤
جواد خیابانی محمد جواد رو گیر اورده بنده خدا دهنش رو سرویس کرده؛ عالیه ببینید
😂
😂
😂
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/24197" target="_blank">📅 11:35 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24196">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RlYk357J-n0G05vEJBTbic6P2r0emIzIaRlRx6CuHsoLoDQEiRBl5zfLK00Xb66K6mHdwP0U5qxR_qMthoLNDDjYWLHWQH5xXtRUjFhvu9pNmWwOl6mhaHH8u88rLN0bsou5Hm8HCdDlziWBPd7qjxNZu5of3qy0Dmw5hWF_jDN0XWqlF2b72VI1u24mH0YCJ6XcqqgY-5JUh6wBXal5TW0s4qrRs_i7M2FxcfOapEM3_4n1ROHFm9_j3Gpj0IXRGXchCTL8NbdUqz3EGauGT3r05cwX6EJ9Ee4hyStdpEBlUVXozX233a14JITFALX6_rjht_489CL3_wdzsqpNYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
لیونل مسی اسطوره‌آرژانتینی فوتبال دنیا و باشگاه بارسلونا امشب 39 ساله شد؛ 1158 مسابقه، 916 گل زده، 414 پاس‌گل، هشت توپ طلا فوتبال جهان، قهرمانی ارزشمند در جام جهانی 2022.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/24196" target="_blank">📅 11:22 · 03 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
