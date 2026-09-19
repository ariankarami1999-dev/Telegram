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
<img src="https://cdn5.telesco.pe/file/AtBtclqpxnk9Jj6d9e8QzZgQw-PQJlCREz1-OwRiiOvCDHa-2LUGGqXei-vdfZex3Vh2cS0-OMDW-zmZUSU50UwFKw7QH4Z3gbmU_Vcd4HlIbRaGgUWUd-LBCBaEb5vws9F0Xb1kaQ5HRM5eTukJI-hXaJLlrsjij6Pting6lTd36gPLQxqjZqVPJgdDSif7LGZFzUKm_-pXZxU9jiVqE4KygDK1Wtz6ObfPk6W5oZOf1HR-eCF-o8Z__gT0aow8t8S1BgSYS40BPh-oc1trTDip2_5-nypjiWjUnPHwlgMEEXytjGkxA6Zh-gOCdzAoKxrZrF0T1Q1vX-kkePxw_Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 408K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-28 19:05:31</div>
<hr>

<div class="tg-post" id="msg-106884">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e4104492c.mp4?token=DgIvbhrLafWsHGnxq2tqK6gKQBlmMPW_i05AjIAIZ781KkKp8hw2pnZXy1llT7rPjMTw7JohdQouQI4NNQ4oHtYUBPFUYrk-lDlEPuTzURSF3dC0NMKpJB7oWhlCN1AwfYDmVK6FNBZuVTSe3HTNzUadv-6FExE4seKsOlu-HB9nseGYHUSVdYp7uA-Q7RW2xljcdIEEOiUFiFGws0Kfd-4uO-_DqfxeL0wkeqhl4uhEyETphITtvL5wHIG7wTpMahcYiUlA6F8ZTusJ-6a6wwc06T4d_dYTTYDoFdLC2dciPvQB_yZ3I8QceQrgvMrqu7wXV3ZoKhYNzN14fyAxWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e4104492c.mp4?token=DgIvbhrLafWsHGnxq2tqK6gKQBlmMPW_i05AjIAIZ781KkKp8hw2pnZXy1llT7rPjMTw7JohdQouQI4NNQ4oHtYUBPFUYrk-lDlEPuTzURSF3dC0NMKpJB7oWhlCN1AwfYDmVK6FNBZuVTSe3HTNzUadv-6FExE4seKsOlu-HB9nseGYHUSVdYp7uA-Q7RW2xljcdIEEOiUFiFGws0Kfd-4uO-_DqfxeL0wkeqhl4uhEyETphITtvL5wHIG7wTpMahcYiUlA6F8ZTusJ-6a6wwc06T4d_dYTTYDoFdLC2dciPvQB_yZ3I8QceQrgvMrqu7wXV3ZoKhYNzN14fyAxWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
صحبت‌های جنجالی یاشار سلطانی خبرنگار، درباره چرایی برهم خوردن توافق پایان جنگ از سوی نیروهای سپاه و جمهوری اسلامی!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 791 · <a href="https://t.me/Futball180TV/106884" target="_blank">📅 19:02 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106883">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ernpZntuzOA3X4jMjo03t-faV5YcnRh5dQ22Udx7F49YkcS9vKFaFm10QBqitRnVgeXBK9JJaI36swU8FQgL4vR0oPz6iexl9ovxUySrHQvYa5_r2V6E-EYn4jiD0Mw6_o5WcF2FI4wGawqx_BIcc3CYAVOfvWw91Z3S6cXcrn8W15YV1bsy3OR0EaLp001C38UnZlsTIjoN1PgYLhIitRjC8uXWEzaGfzy2gF23WPKySWQQW19vkK_XAYRUQXYdCtaWiKy3jsIOeajwqKqgCjtZ-M3yMsXI4SUvQS8nptbUyeXEw9ZZ84HCj-ncK1KolGtaTplWE_XNGMKfaLuHNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">راهکار جدید کاربران برای تأمین نقدینگی به جای فروش طلا
🔹
با روند صعودی قیمت طلا، فروش دارایی برای رفع نیازهای کوتاه‌مدت نقدی توجیه اقتصادی خود را از دست داده است و حفظ طلا و استفاده از آن به عنوان وثیقه راهکار جایگزین بازار است.
🔹
وال‌گلد و بانک کارآفرین امکان دریافت وام تا سقف ۳۰۰ میلیون تومان را با پشتوانه‌ی طلای کاربران فراهم کرده‌اند. این تسهیلات کاملاً آنلاین، بدون ضامن و بدون چک از طریق اپلیکیشن وال‌گلد ارائه می‌شود.
برای دیدن شرایط وام کلیک کنید
برای دیدن شرایط وام کلیک کنید</div>
<div class="tg-footer">👁️ 882 · <a href="https://t.me/Futball180TV/106883" target="_blank">📅 19:02 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106882">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da8b096322.mp4?token=B4Sef2LOb7gBbUXAkMFkb0s-M4cHSbRySlH382DOa3tETdbxEPI3kssCpPU6TSSG_8xlpA3YPEIZK2QucUbDoKpVQfKynd8pX8V8ivVqq71TsEF-NHutOSIFt-vTkjw_o6z3v_BbROPQYWPKohEw5Zh08ny1TZZpO_8rPBP-7-xmY8OsScAwyPT6nBYuzcddiwwybKsTvQNzoZp2QmtQC6hTkPclfAcnSGxLFqPpB2IaDyTDuCJeyKt0XnhMOfVWNbd7mVVcisdnt58juiyTIYALREURyEYwaHjeQ0bRuvgS-VrhbOyIqi5k5XMKw31gPC1zdh07hrcVtRAE_EVsFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da8b096322.mp4?token=B4Sef2LOb7gBbUXAkMFkb0s-M4cHSbRySlH382DOa3tETdbxEPI3kssCpPU6TSSG_8xlpA3YPEIZK2QucUbDoKpVQfKynd8pX8V8ivVqq71TsEF-NHutOSIFt-vTkjw_o6z3v_BbROPQYWPKohEw5Zh08ny1TZZpO_8rPBP-7-xmY8OsScAwyPT6nBYuzcddiwwybKsTvQNzoZp2QmtQC6hTkPclfAcnSGxLFqPpB2IaDyTDuCJeyKt0XnhMOfVWNbd7mVVcisdnt58juiyTIYALREURyEYwaHjeQ0bRuvgS-VrhbOyIqi5k5XMKw31gPC1zdh07hrcVtRAE_EVsFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🔥
🔥
🏴󠁧󠁢󠁥󠁮󠁧󠁿
گل‌سوم برایتون به آرسنال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/Futball180TV/106882" target="_blank">📅 18:50 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106881">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OA29D2CZK7CUnwbHG33gmjvQIvfKixf7jBGgHxGGhN9Emg6uUepO9RnHARwYHzjrQWHYu-hY9OJkH1_Pnh6GzXcyjdk7PAYucRV6O3dUt2sWLuvWuxyRFsY_t05YM0loL0CoR-mukeAO36tcZ2Ra35jcECjFZmg0WO34dNiNn10Bh7JJTXjFMAE8hXE5Lpmt1-scbO5eZifE6utS_hoWc7RLKtphg8H-HOJUntz3A0_H0MGOj91TK9qL3E99FpMaMhM0_DR5yeOo8qNeHmiENd0jf9nPgiEoq_wD0YxKTozJq-DLm8scBFhGIVSYu2r9fTeVBtTHeTY1Bm_U3MxcYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇹
ترکیب اینتر مقابل رم؛ ساعت ۱۹:۳۰
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.8K · <a href="https://t.me/Futball180TV/106881" target="_blank">📅 18:27 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106880">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/9510f8cfbe.mp4?token=Cg3YJKZYcbLXljyWSdRl_kkPKNWy2x8ObG70D1xRvj-lud2e6RpSLb2D3kD7TECBaUfwpcTA58IWa9NZ84WW-wuwp65Wx5IuE1JKbGcUGGKtpAK43gJru9THYYtaM9VT_Tgf8dR5UPfU1O9JFF-ewhpw6erveo5PpJPH5lZv9J2IlH7o7fjdJIpTG9owi5Pv_TCrWCd8TzKCi-X5YHBWf3cnBuh8BsjOPZ_9tc_Ha-2dVMWp_svsLB6xnwzy_wWl8QCJCuk4Era9DG3cC3ENmEAcmO6hf6X2h1DWlTXXASkDvKofwV-JBh-4TUWLds2bx1_0PGql6lbtB33WS1z1cQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/9510f8cfbe.mp4?token=Cg3YJKZYcbLXljyWSdRl_kkPKNWy2x8ObG70D1xRvj-lud2e6RpSLb2D3kD7TECBaUfwpcTA58IWa9NZ84WW-wuwp65Wx5IuE1JKbGcUGGKtpAK43gJru9THYYtaM9VT_Tgf8dR5UPfU1O9JFF-ewhpw6erveo5PpJPH5lZv9J2IlH7o7fjdJIpTG9owi5Pv_TCrWCd8TzKCi-X5YHBWf3cnBuh8BsjOPZ_9tc_Ha-2dVMWp_svsLB6xnwzy_wWl8QCJCuk4Era9DG3cC3ENmEAcmO6hf6X2h1DWlTXXASkDvKofwV-JBh-4TUWLds2bx1_0PGql6lbtB33WS1z1cQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🔥
🔥
🔥
🏴󠁧󠁢󠁥󠁮󠁧󠁿
گل‌دوم برایتون به آرسنال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/Futball180TV/106880" target="_blank">📅 18:20 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106879">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">گلگلگلگگلل آرسنال دومییییی خورد</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/Futball180TV/106879" target="_blank">📅 18:15 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106877">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3613208345.mp4?token=R8LpXSiaRmIlQxbuGlRlI44XGtk2XFkEzH_0XBEc1wuynwWKO6mUxBLTgLHmIbiQoejW1BkKkisi-3-u8LBFiL_2RNlFZ4ybJKHWABCH4EIpvrtinSJIMdIZD77w-xxmzuWbTEuKwyAwOMlwcq9Al58EdrIFwqI_FTNiKND_9z1NY98CRKxbs6ROPsk-v5o-cl-DySFw6fOvkYtskAYS2lbKW8popH5ixlAcqbsWLNphNJMmfiDz7VP4Jl3uwDuVtuYBWwTbeyJ66sFnOruiDiRd5Up_2gBs7zGkEJ9iwdp4lR29YJL14e4P8Cz5AwPE4eARuhdvp_OqbhKoAGtoGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3613208345.mp4?token=R8LpXSiaRmIlQxbuGlRlI44XGtk2XFkEzH_0XBEc1wuynwWKO6mUxBLTgLHmIbiQoejW1BkKkisi-3-u8LBFiL_2RNlFZ4ybJKHWABCH4EIpvrtinSJIMdIZD77w-xxmzuWbTEuKwyAwOMlwcq9Al58EdrIFwqI_FTNiKND_9z1NY98CRKxbs6ROPsk-v5o-cl-DySFw6fOvkYtskAYS2lbKW8popH5ixlAcqbsWLNphNJMmfiDz7VP4Jl3uwDuVtuYBWwTbeyJ66sFnOruiDiRd5Up_2gBs7zGkEJ9iwdp4lR29YJL14e4P8Cz5AwPE4eARuhdvp_OqbhKoAGtoGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚀
🏴󠁧󠁢󠁥󠁮󠁧󠁿
سوپرگل‌اول برایتون مقابل آرسنال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.66K · <a href="https://t.me/Futball180TV/106877" target="_blank">📅 18:04 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106876">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kZ-vInd77-nmJGDM44vL5SasSR3_6W_6JHcF2UarmUNBV-9R6FAiGxjFiDRLmyahJtX_oZuRHZS5uLcnZdCrH4Sad1rGWukK3BJJ1DQwwueZm28QvFrLc23LmD2cRrkVJ18qDL6o8wWEow1xpT77C-Qd1Y2-o60ywM4vZBXpreTJY9K6KwA4nLj78RuZSwR3jB1Ej1CerqVoEff7TAmNYi8Wuvvp7vyklHsg5_ONx7WiEiVZoKy7fd0WXG5huPbfQgQMoL7hx8WecYjeMj6tOY_GONnL6G6qyQL_IWtmzgFP6iQxKHza4ySWHqPefcDKbpk9KclMmlIBIlHSqq_WKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
دکو مدیرورزشی بارسلونا: تمدید قرارداد با رافینیا تا سال 2030 نهایی شده و بزودی اعلام رسمی خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.56K · <a href="https://t.me/Futball180TV/106876" target="_blank">📅 18:04 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106875">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fTNbwHE135VFlN-Dzuc4roA6qw7eM0Jh6yTpRbbwHxpYvzikhZCNCqCehdgIIq3faIP5oSjrr1cpymRPi0QEsW2uwruzQOQ-nPyzOIA9fnrFddC-jrrJp1zPCZIOjSLEGlRfAX44JRV07NAnMYcQI2Cc6_ZSgH2yVd1x4LeRt_rJmeCuMZ_TNmu6dqgmsnSJ0n3ErbxkG7vRl-FCpyDOj7hKRHdZbjMOswqOXmxA6hyRBaQjlwHXhIH2bCfZ1sfxbAGYpiF5cFRwfN3A-jiZpwqZtdKmWfd2obl6EUp1OGGihwUt6JzaP86cJsqxZbUp8AdsyzwJ4pXEcD4m9C2h7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
دکو مدیرورزشی بارسلونا: تمدید قرارداد با رافینیا تا سال 2030 نهایی شده و بزودی اعلام رسمی خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.31K · <a href="https://t.me/Futball180TV/106875" target="_blank">📅 17:48 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106874">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc01f74867.mp4?token=EBLmgFXnFrajBtEAUlUvnPDD-Kd579SkGY6U4icN608tc4dHa8kkgHHHyKkVg6_jKVCQdriKuz_raC4aGvgcgJU7Z_BPt_bx8A3nsLXzMCQPKdAGHZ36FgihX1cBQ8mAeI8byAQnijirtH8LfHitgYTaUCtPAfxhj07LeUqFrdeBiEkU7yi10ewiiAFmSykSDrZi77ReRKfyePRThOmequVByUN50F43YDVhlfK64GljKxC2z9kdlYlHei1W8tk6s5Eggumj87IbSRoo-ghDcOiKzXtzK5M1-yeiubJh8YaTchKJBJiJICHsQYtJ2FexCEgxQw19-6Gch-0piVWImE1NN26OK6xogY4aI1jfrP-sZjniICduuZJf5HM_vYxaJ-vn9JPUDIdxhiptH6_cGkjTyV1oByLzqzYKHaec390TXdTB-xTGYQT3cKRd2gEHBmeoFrLpTxzckAazO1qQ1v_OCfpxfINrFEJOd9oJdQPRS_QOXCA3djLXcj3plpluKyI9kEqxqwJXT-ShpJDuQvqDMOqjVxvZWePiypODOz0DTXqy4x0WzGwaNfVasKHBa0HZGooBTyV40DCGSe2pMFy_ZzCHRznWO9MWbQwUspXEgV-mK4l6lVE-AGHLKz5ECkaNeaEjA87sD8va8GdlkBLc8jmubCqiw4nBqT4KRqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc01f74867.mp4?token=EBLmgFXnFrajBtEAUlUvnPDD-Kd579SkGY6U4icN608tc4dHa8kkgHHHyKkVg6_jKVCQdriKuz_raC4aGvgcgJU7Z_BPt_bx8A3nsLXzMCQPKdAGHZ36FgihX1cBQ8mAeI8byAQnijirtH8LfHitgYTaUCtPAfxhj07LeUqFrdeBiEkU7yi10ewiiAFmSykSDrZi77ReRKfyePRThOmequVByUN50F43YDVhlfK64GljKxC2z9kdlYlHei1W8tk6s5Eggumj87IbSRoo-ghDcOiKzXtzK5M1-yeiubJh8YaTchKJBJiJICHsQYtJ2FexCEgxQw19-6Gch-0piVWImE1NN26OK6xogY4aI1jfrP-sZjniICduuZJf5HM_vYxaJ-vn9JPUDIdxhiptH6_cGkjTyV1oByLzqzYKHaec390TXdTB-xTGYQT3cKRd2gEHBmeoFrLpTxzckAazO1qQ1v_OCfpxfINrFEJOd9oJdQPRS_QOXCA3djLXcj3plpluKyI9kEqxqwJXT-ShpJDuQvqDMOqjVxvZWePiypODOz0DTXqy4x0WzGwaNfVasKHBa0HZGooBTyV40DCGSe2pMFy_ZzCHRznWO9MWbQwUspXEgV-mK4l6lVE-AGHLKz5ECkaNeaEjA87sD8va8GdlkBLc8jmubCqiw4nBqT4KRqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
‼️
🎙
ماجرای دست رد مهدوی کيا به قرارداد ۲‌.۵ میلیون دلاری!
🔻
مهدی مهدوی‌کیا: مدیر باشگاه داریان چین بعد از دوگل من به این تیم پیشنهاد قرارداد ۱.۵ میلیون دلاری را مطرح کرد اما بعد از جام جهانی به دلیل عملکرد، خوبم آقای عابدینی رقم رو به ۲.۵ میلیون دلار افزایش داد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.41K · <a href="https://t.me/Futball180TV/106874" target="_blank">📅 17:45 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106873">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/106873" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/Futball180TV/106873" target="_blank">📅 17:45 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106872">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hUolS0Mv22Sz64Kdi34UwZetWcmneG_ycamxq0V2UH1aq3Gn8gwM1t3SRvzn4S4kFYrhspCbadF7HHxcA82IWhJ8zVVXp4_cUlNJ-bZ2z-RAuMT_5mz5_TgxE1LRljyClhI-h8OQ-MvHSyr2u5Nsyz-15hddfs3LlVdbCaPN1wKuPWJ61ianh8lnmDqkhfD-ZPt7IWP5Q_1jZAnHPWSeMV50PzE4tv0OEpR849wIAmvNVkueotmMRpp_KVzj-2jkkw_M9hXTuZTV_OGf40kz2m2-lLrmjnonhKiOXMvKbCvIt4hbhoU8r7-4JrFzVr0Z5CmAZTp7bCdDvfhJydcWgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
نبرد هیجان‌انگیز  بارسلونا
🆚
سویا
را در
TrexBet
پیش بینی کنید!
📉
نگاهی به آمار ۵ بازی اخیر دو تیم:
بارسلونا: ۵ برد و ۲۵ گل زده
سویا: ۳ برد، ۱ تساوی، ۱ شکست و ۷ کل زده
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
🦖
هیجان بازی، وقتی بیشتره که انتخابت حساب‌شده باشه!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/Futball180TV/106872" target="_blank">📅 17:45 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106871">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N7ETsltDtERTkeJz5Kh0ChpZvOuOHM7qYqWvkCT2bAjN544SuvbaHZGdCEMmOCPn4AFyh8R7mHfneujFpB7RgeSyBGRJv5-KDv8nKCBoEG2hg-mcXQjcf9ZbjuE0wrWvhcIkaQt6MpVEAQpQMUz_vbuv0IY-3walNsqz11zk4jR_lxFQZh882nRP189s_VysHj4kkMcrxOD9Y6BbpGJZPOplfiE31ciFWjLCcSK8IpHx0BbcQaKdZtRPB-mf6o_LMKinKuRpPAUN7GxDD7XuBzmDMx70zW3HMm3hXLGTUz6CBx4m2mPHdbR1hHK6qyqMfpz2IQHr-GebmZmOicQNXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎤
ژوزه مورینیو در پاسخ به اینکه آیا از شرایط بارسلونا نگرانه :
🔻
از نظر تاریخی و فرهنگی، رئال مادرید قابل مقایسه با هیچ تیمی نیست؛ بنابراین من هم خودم را با هیچ تیمی مقایسه نمی‌کنم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.79K · <a href="https://t.me/Futball180TV/106871" target="_blank">📅 17:20 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106870">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jB1NtDKvXYRsos5ZnCZLM1xpj57_DNUEaKgwqQvjiHfYrLEKTdmuj5p2bqI2t722zVuCAkVHzqVkNrlUmUpC1LoMRHB6Psd26FGJA71R8i1YRyilqqiDeVVAWU8GhXrQCWHu20TwmTETHUJDe_nly0ebTZkkKCar8-ywOSTw6tQmzcuOlLGng1KEKK8zbb-VvpimLQX4BDqT6Dzt7nnKyatYQ-N-fGzAWpxlXXvuxC1bTSfELB4FuQxt6BZWQkn-D-HzS88df7of0cceM9KZVdbdKGfsZB77jb8_lXTSH1kKt_bTLBx3-uf69mqgusobu5PxPaRMqoT_blGZiGmOUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
❌
رسمی؛ مجتبی حسینی با توافقی دوجانبه از نساجی جدا شد
📊
2 پیروزی - 2 تساوی و 3 شکست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.44K · <a href="https://t.me/Futball180TV/106870" target="_blank">📅 17:12 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106869">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61cf935413.mp4?token=qzGfjOUAkFfcZBsMOR8AGbPZZe69KdfLbCylrexsbcikrXd85oT4fCNg5CeDmJ7Pp_VfpN1YIMYYEF2Z5XpHhRhskz0YLHsRwAu87PJpsLzhkweTeK0Jb2ktW6r5wXMC99M5fDPYw7ftpg8iSm_rHuPsxIabyiYdtjeYKiVhl1TQXvr6PQBnFzYdUieF_2jYQHQt59pMPCO9cmCB5V0Bka3rNE0CwEGZvs0Oq8OTcgct2fqXVSnRWlCy_0PO1rQ4KCP-AqLtH5cSauSL-8Vgw3foTMtCGYxxQ2CcyuGCCHYjyO7x7nTvjjE-Pjoo6dNiQtJon9gksUpFbSD7h6Rh4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61cf935413.mp4?token=qzGfjOUAkFfcZBsMOR8AGbPZZe69KdfLbCylrexsbcikrXd85oT4fCNg5CeDmJ7Pp_VfpN1YIMYYEF2Z5XpHhRhskz0YLHsRwAu87PJpsLzhkweTeK0Jb2ktW6r5wXMC99M5fDPYw7ftpg8iSm_rHuPsxIabyiYdtjeYKiVhl1TQXvr6PQBnFzYdUieF_2jYQHQt59pMPCO9cmCB5V0Bka3rNE0CwEGZvs0Oq8OTcgct2fqXVSnRWlCy_0PO1rQ4KCP-AqLtH5cSauSL-8Vgw3foTMtCGYxxQ2CcyuGCCHYjyO7x7nTvjjE-Pjoo6dNiQtJon9gksUpFbSD7h6Rh4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
سکانس‌جالب از قسمت جدید مرد سه‌هزارچهره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.16K · <a href="https://t.me/Futball180TV/106869" target="_blank">📅 16:55 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106868">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/98bb41c972.mp4?token=fXL2n9b1vkc4yaqIExJxSPPghdFuu41gSG2ltISVSpEtaLpqF5fB2cO4MudlDqAO9rFHbBmxv6pryhhHx6NF_OsS4zPtsbylepxofLbMANktKDTIRgkCNgW8TDfBnEQSzi_7m1zW5YYT2fM1S8Wao7bfVujRGwmKVjlHW7TVFTnRl1nfxl_fZNW4YDe-T1pAD6GTjBUxYMqbXjIcV2njCmYygJJbSeiLfPyS9hnhACJTiHTaMqeAVZJ3i5WtHTYyQh_IbQv5e7UpGx1hXv4BZ4gvboRMdihHWlZqUqemsPtnE-RuplVvJeDrRKD3sn380OO5LuIRk-wwbmHIeh2Rdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/98bb41c972.mp4?token=fXL2n9b1vkc4yaqIExJxSPPghdFuu41gSG2ltISVSpEtaLpqF5fB2cO4MudlDqAO9rFHbBmxv6pryhhHx6NF_OsS4zPtsbylepxofLbMANktKDTIRgkCNgW8TDfBnEQSzi_7m1zW5YYT2fM1S8Wao7bfVujRGwmKVjlHW7TVFTnRl1nfxl_fZNW4YDe-T1pAD6GTjBUxYMqbXjIcV2njCmYygJJbSeiLfPyS9hnhACJTiHTaMqeAVZJ3i5WtHTYyQh_IbQv5e7UpGx1hXv4BZ4gvboRMdihHWlZqUqemsPtnE-RuplVvJeDrRKD3sn380OO5LuIRk-wwbmHIeh2Rdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
👀
ژرژ ژسوس سرمربی تیم‌ملی پرتغال:
🔻
کریستیانو هم مثل بقیه بازیکناست؛ اگه عملکردش خوب باشه بازی می‌کنه و اگه خوب نباشه، بازی نمی‌کنه. آیا جایگاه ویژه‌ای داره؟ بله، دوران حرفه‌ای متفاوتی داشته و پنج توپ طلا برده، اما آیا این چیزها روی تصمیمات من تأثیر می‌ذاره؟ نه، اصلاً.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.89K · <a href="https://t.me/Futball180TV/106868" target="_blank">📅 16:34 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106867">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a989591ba.mp4?token=GbSitypCeSNy8OQz-tKucB9idfUrXUhes-IaxoS7TLwVGqRXOPhK4_fCMjMJULVymz1uKsMkED1PyprFB-pgqZe51X_PTCMpc7yQ8kUhzx4Ak3wjkd-2muy-uGUJAWdh94PAT_lmlOO6leSsPRuhjiFFR0rt1FhEUvvwNlZBmbY8HV9gPkU2vtiCOOtWr-43F2mIKHAyQCNrk0m7wuApFkttlO2f5tftoPC5Y8P7dsVz2JvDYC11VP70cmSQVuarpxc5Wt4qg7cLjvkgPzrSAxGEmSb_Y7rTcqNCFO5hmrrDdCO1sDJ3z2mW1YsXAIH8pnuMzqkH8HJ6GccaHf3FoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a989591ba.mp4?token=GbSitypCeSNy8OQz-tKucB9idfUrXUhes-IaxoS7TLwVGqRXOPhK4_fCMjMJULVymz1uKsMkED1PyprFB-pgqZe51X_PTCMpc7yQ8kUhzx4Ak3wjkd-2muy-uGUJAWdh94PAT_lmlOO6leSsPRuhjiFFR0rt1FhEUvvwNlZBmbY8HV9gPkU2vtiCOOtWr-43F2mIKHAyQCNrk0m7wuApFkttlO2f5tftoPC5Y8P7dsVz2JvDYC11VP70cmSQVuarpxc5Wt4qg7cLjvkgPzrSAxGEmSb_Y7rTcqNCFO5hmrrDdCO1sDJ3z2mW1YsXAIH8pnuMzqkH8HJ6GccaHf3FoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
جمله قصار فنونی‌زاده خطاب به امید عالیشاه: با آدم بی‌ادب باید بی‌ادب رفتار کرد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.78K · <a href="https://t.me/Futball180TV/106867" target="_blank">📅 16:05 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106866">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RvyPpW2abqWSIBLBSxmLNecQrApHhCrngneQHZSQSyF6QuYauDax4BZ9Uao5he28JJDjd9lluL5WLASlNP00LQb0-XJk5QsMiPNITxybmmKBtddt6O7bMHxv7k1FF6oZKeO7ihhy6zDIWs71TEV4c_4XHQL_0ZJ2RlQyEKl0pJBV8k0Zq5rfrwVO345XG5sLsBXl0eFqeLz60TNh-RDb_WUlKKrpOkubbqZIdtCWNJk6g0jZldioc_QuvqxowxBw1um9jZ7MLw-beEv1BGOxTHYwUrv7-rJ9nXb5tClO-Cug8R_DaAFrJiT9LE6BUlCWV7r21BytJ_uBNODbBtp7Xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
📊
🏴󠁧󠁢󠁥󠁮󠁧󠁿
عملکرد ضعیف املیانو مارتینز از زمان حضور در باشگاه چلسی:
⚽️
⚽️
⚽️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
مقابل برنتفورد دریافت 3گل
⚽️
⚽️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
مقابل هال‌سیتی دریافت 2گل
⚽️
⚽️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
مقابل آرسنال دریافت 2گل
⚽️
⚽️
⚽️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
مقابل برایتون دریافت 2گل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/Futball180TV/106866" target="_blank">📅 15:40 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106865">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MHPHGaeWRNgUSWAyTgWVILn1osuqoC-0keDsvFa3sqnecLluOi28vva9TXw2DP1UZr_DuPgZq-PftdrHy5YUPJKoLZ4bm0BRX6gy1CJK5UL2P2mtFfvfW6-88x0r_WWshMsqmsqEtIzMr8OcmNgd_jsU5JGfsR5o_PdcIi0JFy8SoGlEzlascIiq41MRfOxRvARJSErv9_AvhWJLsMMA_YZWlJOnr5r21hhpSUypcPvLo5XUaOpznTDqISS4ktKoago5NB2i51uWg1FsYDjs-TYgpitAazUnL0vz465mYeAqkT8aUZbD5t-bDWgfRKAk67POqanS64gSh2bCre-0Zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
🇮🇷
لیست‌تیم‌ملی آلبانی برای فیفادی بدون حضور یاسر‌آسانی ستاره تیم‌فوتبال استقلال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/106865" target="_blank">📅 15:11 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106864">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ed8ff21de.mp4?token=JsqZs4QJv01FUklwntDXsQqqP6Pi8djllh7ikCsSnmVR987aum5KBDKiMosX57-UnCYBzua1Ykj3oLwVBzjj0CxUefPVRLhyPdmSrfDWKnh-vqE7-0onscymQP43cCN0-pqLgt40zeFwwh5mGgr4I_bgaog-L99qM4jVSFQftD_t5mz5ulyChZ6yzDXJQLRbjm252B8lBeGF7eL_jn92stgNXsZUt2lK8zTa5QZEzuvGhYr6LDdh4GVNDYv8hMdUXYNXbqipgN8tijhLv66JEbFQfguEbkGMEx-UFYbD_k1ZEl2l0An10DBfuc1bnthHgxxnruLtwyp4fpZgGbPDrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ed8ff21de.mp4?token=JsqZs4QJv01FUklwntDXsQqqP6Pi8djllh7ikCsSnmVR987aum5KBDKiMosX57-UnCYBzua1Ykj3oLwVBzjj0CxUefPVRLhyPdmSrfDWKnh-vqE7-0onscymQP43cCN0-pqLgt40zeFwwh5mGgr4I_bgaog-L99qM4jVSFQftD_t5mz5ulyChZ6yzDXJQLRbjm252B8lBeGF7eL_jn92stgNXsZUt2lK8zTa5QZEzuvGhYr6LDdh4GVNDYv8hMdUXYNXbqipgN8tijhLv66JEbFQfguEbkGMEx-UFYbD_k1ZEl2l0An10DBfuc1bnthHgxxnruLtwyp4fpZgGbPDrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
👀
سوال مهم از هانی رامبد؛ برای رشد پایین تنه حتما باید اسکات بزنیم؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/Futball180TV/106864" target="_blank">📅 14:50 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106863">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e87cfdef19.mp4?token=eVzVOGdLIDcD2EhrIkm1uzLfB-gEPKWnNN2BMmb89QdqkiREMCh0xgdf9vmHlQDaFkHhriGOhIIgIbZsWL-Te9yUnKpY9tGQEvDam9G4ccd93LgrNCPePZle5WraVRsRQQaLACgWd834l3Oxo6PRscYbGy98WqmC6TMWti1rXAr4tH-m-quiDg_ccKcmx8bmh34OG12R7RHcxqCMUfVYdkjCXBZSWZbNutj5iS5vo2Am__lfk4QaWeVJpxFoN5wki_5LQOcyPqA-vGEeWsCwtAao3TaeOsHNOnGgflQmTEQ0-G8OzfLinz2cUA4Cn4iD8OoEgsML2SpRoGREkxteZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e87cfdef19.mp4?token=eVzVOGdLIDcD2EhrIkm1uzLfB-gEPKWnNN2BMmb89QdqkiREMCh0xgdf9vmHlQDaFkHhriGOhIIgIbZsWL-Te9yUnKpY9tGQEvDam9G4ccd93LgrNCPePZle5WraVRsRQQaLACgWd834l3Oxo6PRscYbGy98WqmC6TMWti1rXAr4tH-m-quiDg_ccKcmx8bmh34OG12R7RHcxqCMUfVYdkjCXBZSWZbNutj5iS5vo2Am__lfk4QaWeVJpxFoN5wki_5LQOcyPqA-vGEeWsCwtAao3TaeOsHNOnGgflQmTEQ0-G8OzfLinz2cUA4Cn4iD8OoEgsML2SpRoGREkxteZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚑
صحنه دلخراش مصدومیت یک‌بازیکن در هندوراس که پای بازیکن در آستانه قطع شدن رفت!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/Futball180TV/106863" target="_blank">📅 14:25 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106862">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🔥
👍
🇩🇪
شب فوق‌العاده اولیسه در برابر یونیون برلین با سه گل و یک پاس گل و هدیه‌ای از طرف نیمار؛ بایرن مونیخ ۷ - ۰ یونیون برلین⁣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/Futball180TV/106862" target="_blank">📅 14:04 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106861">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jb98IiMhRhEYO9w8XD0zMfAYSoeaetukRDV5rNotYM2T3pEjh9zuWtn1ppwrq5_rRvBqejdBQ8owTnQJhUi9s_0t6NMPaq5ISEtQ3F5gqo8zLiJC7QkfX6qtrBFoUgcr0QP-BBOss9oFv7oQsEzBV8wr8Hll78Op8N-gX_Yy7IZIQSqDoH9Cejd9QbeMaXHn5EdxwYNMBBbgeKcwtJEcMBvPEVAJ_W6IuPZ5akaKpNQrIRtEkOVxePZrOwhSJxNcUDShArcGwgtiLFTyh7mAr41y2x6i94l76c-TZt-rfMQMZDb1v9dmv0aSRpULl4BRANLJgcoITI6Cwx2Xw67TSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
هفته‌پنجم پریمیرلیگ انگلیس: ترکیب تاتنهام مقابل استون‌ویلا؛ ساعت ۱۵
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/Futball180TV/106861" target="_blank">📅 13:49 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106860">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3121f63a1.mp4?token=HGp_Pp1fibdfGCgPmz1yGYUzBUhA7_1LshtrB2tTvx3s9k3WKHqrkqbc20Cn2DKwtB1pm_vfeIVWe6C6qZVtsW_b9BLQL9EIlTb22bYuJrVOkwobJHPxY40nbh2BUk8oaeaGEy_Tt0rDhS4PcNzvAPrEwrF54orLkpV_ouQkRv4JhOqy0yxI6-oZtgY-td-3lBhkwUlWS9-TaURwqfD3XcALcG-ebOWyfb9OToGBegLVBQkH1pqoZhGJrQ9noBI6zV8k_2E6dmmDlUjxqDd5l4500WIrDDWqFuutrhlGHOlacEuCsg2C0gpolqcVhGvQgqoA9JaDoTSG8JIMqcAWWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3121f63a1.mp4?token=HGp_Pp1fibdfGCgPmz1yGYUzBUhA7_1LshtrB2tTvx3s9k3WKHqrkqbc20Cn2DKwtB1pm_vfeIVWe6C6qZVtsW_b9BLQL9EIlTb22bYuJrVOkwobJHPxY40nbh2BUk8oaeaGEy_Tt0rDhS4PcNzvAPrEwrF54orLkpV_ouQkRv4JhOqy0yxI6-oZtgY-td-3lBhkwUlWS9-TaURwqfD3XcALcG-ebOWyfb9OToGBegLVBQkH1pqoZhGJrQ9noBI6zV8k_2E6dmmDlUjxqDd5l4500WIrDDWqFuutrhlGHOlacEuCsg2C0gpolqcVhGvQgqoA9JaDoTSG8JIMqcAWWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
▶️
ابوطالب حسینی با این ویدیو اعلام کرد که دیگه تو کار ساخت برنامه فان 360 عادل فردوسی‌پور نیست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/106860" target="_blank">📅 13:35 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106859">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bKvwa8ivpPXpVbY88AJvkcbj47Y7QJ5b7brX4gtvqvGGeMFk-XJmC_xzTQQKlCMEJIz-qAN1B7s8LtJJUq3YS9iDDVoq8InkDf8PuXh0eFeq4IoEpD0IuB0hKwPTeIaZiA7Wg_UtnavqZb_QtSQm_6B-WRayjVhSAUs8h0pWJt4ibBkbi2PDpeYE9v0HtQ6oO72-6Abbtson-TtEFQKoCasbSlmxVemKccv6DyaIS8ACLFSYPxRBnsvDzn62W9E08DKc5hiPOYJDNJqqifgO5yz_33f8zNVD6cpeli94dEkKowzxqLJiFYlp_Hizp7rxmlSeB1ZV8U5Ka48Y48Ixqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🎙
🏆
رافینیا: بدون‌شک برنده توپ‌طلا باید یامال باشد. او آمار فوق‌العاده‌ای داشته و قهرمان جهان شده. مردم حاضرند برای تماشای فوتبال او هر رقمی را بپردازند و من یکی از آن مردم هستم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/106859" target="_blank">📅 13:25 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106858">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PgDR8xNkWVzGegZIJGC1xSiOZ8_5OyVgrEL9qO8taintep_9Sw-9HooujlZFx6Tby7npWJn2fIG14eHFxB1vA35HsxOz9uVSbkYoUbRI1sHSpufUUtLNFRT8PD_VLofcivJtD8jO0keqXzj4Kddhr2BmfZzaDJ8Y5a7iwuMoW9_vKZgpR6h2NeEjJl3L3vFQG6ZGv95ND7H0sRbOWvgfXJd-XuQPyN7-jD1qsvcM-4G2_0Jb19qXZF3XPxybl4H797504UCz3X0Ja8KXB8A4CYTwuAamxGwxTv42OV9SCdyMWihgm9yDkPQKFhIiMyseSRv_I3NKvjb43shbhlcEUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🎙
🇪🇸
رافینیا
: در ابتدای فصل یک‌پیشنهاد بزرگ از نظر مالی به دستم رسید که مقصد عربستان بود. این پیشنهاد می‌توانست آینده من و نسل‌های آینده خانواده‌ام را به کلی دگرگون کند اما بخاطر عشق و علاقه خودم به بارسلونا به سرعت با پیشنهاد مخالفت کردم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/106858" target="_blank">📅 13:16 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106857">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da53ddde15.mp4?token=OplahypIfoXDqiyjHnldgPQ2K282c4FDyi79njPE_en8fOC-aMWk7s7xg0wbZno0ulhlc-SEe27Q1jLGkT3oRuHXZmxUoNz-0zSKGMt2XC-D2fFYKlyViX-6YF51EVMsj38dP8mquevLva6LKGmE24EO2w4iJmH5rJHX4FcyxUbhs9Vwcu30aHOZxUcm9mEJ-CnDcYdDQ_-zeMBJ0oYMVvFxUVyDHwQow02pGnubLKAcStdzKPA7KVEqtmdIxf6vmmf0il7gZp2s_ocNQ-tv7SqB4w1XfgSNL09U64IJgbo8_Uwqk6IsuzL4zS92XZ66NN5pWe3EOmVztUvAIOz7kQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da53ddde15.mp4?token=OplahypIfoXDqiyjHnldgPQ2K282c4FDyi79njPE_en8fOC-aMWk7s7xg0wbZno0ulhlc-SEe27Q1jLGkT3oRuHXZmxUoNz-0zSKGMt2XC-D2fFYKlyViX-6YF51EVMsj38dP8mquevLva6LKGmE24EO2w4iJmH5rJHX4FcyxUbhs9Vwcu30aHOZxUcm9mEJ-CnDcYdDQ_-zeMBJ0oYMVvFxUVyDHwQow02pGnubLKAcStdzKPA7KVEqtmdIxf6vmmf0il7gZp2s_ocNQ-tv7SqB4w1XfgSNL09U64IJgbo8_Uwqk6IsuzL4zS92XZ66NN5pWe3EOmVztUvAIOz7kQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
رژه کاروان ایران در مراسم افتتاحیه بازی‌های آسیایی ناگویا 2026
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/Futball180TV/106857" target="_blank">📅 13:01 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106856">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jVKgWbkMakd6CReFpNjDbgjrJoWrvDeavosu1pC-2qRixd0afg1OgSPJPBDRjEoUMR4oHVeC-Cr_dQ96ES_Txl0kxlva69oWl9weaHfeUvkbcHWCgOLfes0F_5dwUmbPKQ23MpEaN8WHDzNv8lOd9d4tyM4mZyT6LuzJTkC6AsySmWzpJjQDIQB2ySznwcvmPXussUrA9Canlr8seNPrvnJ-2DWFFEHYqJu7WSKSRHWcBPf0x4JxNYkE3eztSnFW2ltn2ZnVwr--a6esu1AEBMttCX-YDIfV8Jw7QxsZBi_YyG2ZKI56rTiXcAfuMSWBkYRUivkbinqoZo-4Hv7dOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
💥
🇪🇸
نتایج مانوئل پلگرینی در تیم رئال بتیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/106856" target="_blank">📅 12:45 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106855">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pAs69U695Gns_B3cg2Q_7AtTty5f7ebIDx9turlQkpdwQ_xEFGQ_AWRA7yWWn8o-s5hl1M05qcPBgKZezzLsjr2ASDqe_-E0b-8th0Bp0kQQGZxYfYTrvQv6nCTPm1M0OhEyeAa4vFlNExxj3yIZA-Hq7f0CkhRoW867dpqgzUXbaAmvaKmhX5eDECXwF_0dzDIncFj3iHoUCCM_h5VvQOJpsr22JmYkhQ4Hepgrr9h9f--v0G4UCy-4qHYhwypFeIvNGbprSZf0pyIdBZN3fc4JwyTEjNBNCqs89yTd6BSXcsPb2MUZ7EzOQX4sZKrpNy5KSu56vzSnVdf7mTZYAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
🇮🇷
🏆
با برد استقلال مقابل السد جایگاه 5 ام ایران حفظ شد و سه سهمیه مستقیم باقی موند؛ نتایج مسابقات استقلال و تراکتور مقابل تیم های قطری تاثیر زیادی روی حفظ این جایگاه داره.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/106855" target="_blank">📅 12:32 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106854">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s-sKHmHCUD-mHwY9WeIpcTB6Lovn0Aa-OfI4xSwcgPPrGi5UUwaOY5PoGcN_nZQllioJ6cu-51d8g6G4uVU6qpTbr0jZsTWyyfnaYwZfY0ObXMTFOzI1Ms0SsrLF2vdOsNqjyBVes_82aMKvtxMMwSyPy9uZ_guVZ7hKE8_wEYwS4GxtUW4RWqRnGw3OQ6VaYosR3SQ8j-iZqzo0xa9q46qrkyHkjlvYXOQFbkC2bGSxTsSWpe3s_CtyW85U6xHscf67M8tla012XSgNC3Zy2DvBAnsTZ5PsB0HBWmNIzUtMC4aPkVA-sL6DWPcKjoDbTgcqY8soDR_oWBwNN1pcnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
🇪🇸
لیست‌بارسلونا برای دیدار امشب با سویا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/106854" target="_blank">📅 12:19 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106853">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ltOb71cbpBgfgRZcKklx5LSb2jmXDbMc6DvW2l7RkdFwcYKWwDh0n6B7dO-X3wPSRmzaCtuPcZWE5nX3I4J6ddd_0pAQsd2m7LVZ9TEwzH3P_l0JKetsGzwSUzHh5tbSsY0sNN5XAHJsTa03Rwwls0QQGZi1KjeE861RIFv-_TmAcioMJ0XZhfcRzjxrFtgQWl3MLxsEBUtYAkUpn-PV0kAPUr4sjk27GDpDzPffuQAFNZf27Om_nEFQ9OEkA9yiaW_WlKInj2K8oaAtTG1xUIxOnkBD6EgZAYIn1aqlLTstuKe4Jtj6Jt-7Tq-s643bUwz3qMe4-lyRUCasmeaq5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
▶️
مسابقه دوی نیمه ماراتن بانوان که امروز در بوستان ولایت تهران برگزار شد که حجاب شرکت کنندگان بدون محدودیت خاصی بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/Futball180TV/106853" target="_blank">📅 12:07 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106852">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/106852" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/Futball180TV/106852" target="_blank">📅 12:07 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106851">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fOeoGwwEeFcC9lqDf9tBT5zFXoBj3C6IeYdKZt4uDnp83PrQCo5HzQHYrFRt7FBaHmisV208Frp_8DdR595I3QJWifYn5lJUyJJWmK-2JxzA7Jm0LguDW18pfPlCcMZfboGVobjFqaREHvMzz01vf0ydwHjzQkX1hV5ppoHqSWadl0bDcNL1d6tCTcmznCl3TyT3ScMCC0VRB6KYrjisg9q28CJ5cMCNaIz2bSXzGWpwhFZTI_9to9PAwojs36pSjf9LJuBmxqC28P6NwNqzIpcFu8Ci7nbZkafriZ_a2mB18GON9RYNROHCyfGxqE0fWChwXyxDxkW6ij1XID769Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت بین‌المللی
TrexBet
استون ویلا
🆚
تاتنهام
آرسنال
🆚
برایتون
بارسلونا
🆚
سویا
دورتموند
🆚
اشتوتگارت
اینتر
🆚
رم
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
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/106851" target="_blank">📅 12:07 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106850">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👍
▶️
🇪🇸
🇪🇸
در دیدار خونگی رئال بتیس برابر ختافه، ۱۱ نفر از مسن‌ترین و باسابقه‌ترین هوادارای رسمی باشگاه، بازیکنا رو موقع ورود به زمین همراهی کردن. این مراسم بخشی از برنامه‌های هفته افراد سالمند بنیاد رئال بتیس بود که با هدف قدردانی از هواداران سالخورده و یادآوری نقش اونها در خانواده بتیس برگزار شد.⁣
از اونجایی که بتیس توی بازه اصلی هفته افراد سالمند، یعنی ۷ تا ۱۳ مهر، بازی خونگی نداشت، باشگاه این مراسم رو زودتر و در دیدار برابر ختافه برگزار کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/Futball180TV/106850" target="_blank">📅 11:55 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106849">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sPm3iEzbEdMZWYdf7K8lCma1BzYT2CciPzZjcn4u9YqKtk40IpfJBEdS8gANS9yb89_ROA5PeS-5N7QmM1ZbMA_3iFV0fFpZ1wwHBfvhVd8ioiVVDeQWNXRNupVaEWImlZTNnCJPgWszwa4hvvkP08WSn2IUe9lBTJyBjPTL1Qw1PPJpPlE12_qCfpJiGl2SdOsNHxN3Gu0Dvjy1SSlW8unQZIKO4iRjF2YEngo-1r8svi2pNjBFE4gb7umthA6da6JaKlnNkmLnNGnp5Sgeb3K4aMXUffrrmCT4euqjRal-Ll9WWQkduViPI8ztrrgRIJjI4NdJmc8eVzKbsJiSGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
😆
وضعیت سه‌فصل اخیر اندریک در رئال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/106849" target="_blank">📅 11:33 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106848">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32f6de555a.mp4?token=IFZCKpgcMA-qHVIKV9UFuyW5DNdIMErKs-dvCUzc9JdojrgtaKsgBsqm9NrgOxPYHeqtmqpFIZP5ylzF6GenPIMD4hkzjCmafzJu_bCdxTmfxQPh8nVlbi8NwIGRdB8tRC4g4kQKERhj2qNuLRzceyx0TVam5XXgdocs1tkPiiijgNtieljTctQSqNFQONLzRIf8qmQxUV3o5MQJ_pSKOfTuq0g7rS2oIosVtDFxwyPAJccKsVRFfl9y_ve1SzOn_cdMICWftgGPpUc5gXzxjGflILCi39N6TB7FnIEFU4qZJs5A_cJFZidcK3HuW8Q_dsF03uzkUNMwgBs_TBemZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32f6de555a.mp4?token=IFZCKpgcMA-qHVIKV9UFuyW5DNdIMErKs-dvCUzc9JdojrgtaKsgBsqm9NrgOxPYHeqtmqpFIZP5ylzF6GenPIMD4hkzjCmafzJu_bCdxTmfxQPh8nVlbi8NwIGRdB8tRC4g4kQKERhj2qNuLRzceyx0TVam5XXgdocs1tkPiiijgNtieljTctQSqNFQONLzRIf8qmQxUV3o5MQJ_pSKOfTuq0g7rS2oIosVtDFxwyPAJccKsVRFfl9y_ve1SzOn_cdMICWftgGPpUc5gXzxjGflILCi39N6TB7FnIEFU4qZJs5A_cJFZidcK3HuW8Q_dsF03uzkUNMwgBs_TBemZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇪🇸
وضعیت رئال‌بتیس که خیلی شیک‌ و بی سر و‌صدا خودش رو در جمع تیم‌های برتر لالیگا رسونده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/106848" target="_blank">📅 11:05 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106847">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f7feae8a28.mp4?token=QlA2oM9CZqOdzM_n_-UoOY5_mAlTqeQEMxnpnYKKoY5ZebiLfz44enNKZiJTqywOKNFlhGqoXtZaS8Ng2oRZlclGRpzpIxMs3hKCcQYHNmcKHua0ceIp0jbh7O26lCOrObhihayGsqOrqTEo6MA8w97izdaUGb4JDk6drPC-k36psd2NwK_633Y0l4aNRznZtWCo3yBnd3-e8mLNfPFor4UwXjvK9TfXWnwjdr-EL0hWXUNWSNSZShG3PBdZp7Yflmg1KNlKVFtVl4qhUA5va0iDnZ5sVRn9Jy62vZRA-yb0KHC0VG6J1eXt7ESrrii7kPtyeL_C_W9-yKUxvVxsRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f7feae8a28.mp4?token=QlA2oM9CZqOdzM_n_-UoOY5_mAlTqeQEMxnpnYKKoY5ZebiLfz44enNKZiJTqywOKNFlhGqoXtZaS8Ng2oRZlclGRpzpIxMs3hKCcQYHNmcKHua0ceIp0jbh7O26lCOrObhihayGsqOrqTEo6MA8w97izdaUGb4JDk6drPC-k36psd2NwK_633Y0l4aNRznZtWCo3yBnd3-e8mLNfPFor4UwXjvK9TfXWnwjdr-EL0hWXUNWSNSZShG3PBdZp7Yflmg1KNlKVFtVl4qhUA5va0iDnZ5sVRn9Jy62vZRA-yb0KHC0VG6J1eXt7ESrrii7kPtyeL_C_W9-yKUxvVxsRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇸🇦
استادیوم آرامکو عربستان که 2 سال پیش یه زمین بایر بود حالا تبدیل به ورزشگاه لوکسی شده و در مراحل پایانی واسه افتتاح هست...
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/106847" target="_blank">📅 10:40 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106846">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00ca24d608.mp4?token=fNhSscCi4MyKNfMFDZtTsnc4LBTAtBqe5G-2vh-d5i9zwKIrLwoFOIvWMFsTZPRjLhYkTulMHEdTlAxc7kCcrqAyN3XvyaaXScRAMYJ3K6OLfMOVsRRW5oBwPJgPut9YLMtQummQKkKb-dE-Nd2y3U0j8eqqq6mQTdGk9CaD85bnj6ZISYJsTciMVDjHfWGEGtuEGdHOghIVdYF_9bEVLq0qc_BAQAWyQg_I_DCi93kA2HC51sXm2n04jmQ4qxmPy-dlLz6GFjOtxlbjI4Z3hYf7DLZ6nCZpg3-kuMA1qzLhus5Ty08w-583FAj507OlBUFHYJRBMNjkAa1SjpJ6sTU2Fz6sZfGRG38X_ZFuOjFASOUDhEpRDFo-4sOHlJ0spTN0K91RemDSh9DUFxvAglG7bpnhzbEI7ZsYeCxsLK-h9rQHcIMnAFIZeRtwIKDqXIqJMb_rCEHEjsFDR0K60_sAdr0asUUnajEMiCC_dwnNwbUsRJIz_HlgzAnsXUdB-BRNVL_x1m3ebJ6uSxz7YooNIS-trGse5jwuZcj8pDc5cr4rJOUOoVDNm-Y1AciIHpRkbS1q9ASdxZqTvJjF_xmCchwmvoBm7UeII92Ky0L98rEK1nJW09ypaTiHJjgBFJUxv7YWAn3NfPie4FQcXlZbry1SpIT2A3I4FLsME9I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00ca24d608.mp4?token=fNhSscCi4MyKNfMFDZtTsnc4LBTAtBqe5G-2vh-d5i9zwKIrLwoFOIvWMFsTZPRjLhYkTulMHEdTlAxc7kCcrqAyN3XvyaaXScRAMYJ3K6OLfMOVsRRW5oBwPJgPut9YLMtQummQKkKb-dE-Nd2y3U0j8eqqq6mQTdGk9CaD85bnj6ZISYJsTciMVDjHfWGEGtuEGdHOghIVdYF_9bEVLq0qc_BAQAWyQg_I_DCi93kA2HC51sXm2n04jmQ4qxmPy-dlLz6GFjOtxlbjI4Z3hYf7DLZ6nCZpg3-kuMA1qzLhus5Ty08w-583FAj507OlBUFHYJRBMNjkAa1SjpJ6sTU2Fz6sZfGRG38X_ZFuOjFASOUDhEpRDFo-4sOHlJ0spTN0K91RemDSh9DUFxvAglG7bpnhzbEI7ZsYeCxsLK-h9rQHcIMnAFIZeRtwIKDqXIqJMb_rCEHEjsFDR0K60_sAdr0asUUnajEMiCC_dwnNwbUsRJIz_HlgzAnsXUdB-BRNVL_x1m3ebJ6uSxz7YooNIS-trGse5jwuZcj8pDc5cr4rJOUOoVDNm-Y1AciIHpRkbS1q9ASdxZqTvJjF_xmCchwmvoBm7UeII92Ky0L98rEK1nJW09ypaTiHJjgBFJUxv7YWAn3NfPie4FQcXlZbry1SpIT2A3I4FLsME9I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
‼️
🇮🇷
آنالیز فنی جالب تراکتور در بازی مقابل شباب الاهلی امارات که باعث شکست نکونام شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/106846" target="_blank">📅 10:15 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106845">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec418d62cc.mp4?token=RMZgKx47_ifRSgJ5yAmzk_H3Z-kDgPQQw8SRNiq7_BVkCgL_7Wcw6i7irzSR_8uE6ywckm0kKiGltLMT70LR5ArkYakgdPvpfP_jOjQzqEkWdpli009VNoBtHgs7z7adden7CwwyfPsu9llJDnxhPayoZGJ6lZQ_X6mLnXzmVdnAaQmKSY-H96cUosgcUobaxZ3x-m242UtjJfj62Nhp4zkuQe4qBwImhoHfhW8az21iwxT9YlHNo4X8YhrbCnstPQ6LgQr3SWsrECY5fy0gOFK-J7fiblQYFAwGjm75Pl_BBnH5PGiERSA3rXOWVB91_gn4ZYbG5W9XnmaJhWM9Cg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec418d62cc.mp4?token=RMZgKx47_ifRSgJ5yAmzk_H3Z-kDgPQQw8SRNiq7_BVkCgL_7Wcw6i7irzSR_8uE6ywckm0kKiGltLMT70LR5ArkYakgdPvpfP_jOjQzqEkWdpli009VNoBtHgs7z7adden7CwwyfPsu9llJDnxhPayoZGJ6lZQ_X6mLnXzmVdnAaQmKSY-H96cUosgcUobaxZ3x-m242UtjJfj62Nhp4zkuQe4qBwImhoHfhW8az21iwxT9YlHNo4X8YhrbCnstPQ6LgQr3SWsrECY5fy0gOFK-J7fiblQYFAwGjm75Pl_BBnH5PGiERSA3rXOWVB91_gn4ZYbG5W9XnmaJhWM9Cg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
🇪🇸
امباپه: "اگر میتونستم، کریستیانو، زیدان و رونالدو رو به رئال مادرید میاوردم. من فکر می‌کنم آدم کیفیت و مهارتش رو هیچوقت از دست نمیده."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/106845" target="_blank">📅 09:50 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106844">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cSeg6JXpZiFUvncOx6Twn86k8NO-UuoVk9Xommj8SXqfajr7FjpJ6l2cMsSXhJRbhpireLAgixAOJ9Vq_KDwezAZwqojxX00k3GHqyaB1ZYpU6WdvX0wpNXiKB3RJyrDUkfF1EQHcad8yCO_TrFg5x3AbqmYLLhyktWSnabTRl85cL-OQ3Z-9B_z-qvwSv9y3yWlXhSfYTf-2Zjq3AspXNrBcwU2i-yuWa6-HUthg5pbvTvu49E7ft8RS9BRsFyEHE6U7YtmlXcL0KT2giyYU9SN4vvagaIcceLDvmGcuj24PCrqBwbI2Ynt8U79w3J6frUSFkviA-aykZ1RVSZnYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
👀
از عجایب مملکت؛ یک‌نیسان آبی با ۹۵۲ میلیون تومان خلافی بالاخره توقیف شد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/106844" target="_blank">📅 09:25 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106843">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32c2ecca4f.mp4?token=HsJv1nXhjlIos5fzeA2crMFH7QOYHtOSd8aZYCeo51ZgjE0q17aXKHrF3AhNGeWsQEA3HM_20LIOee9VMbvZCkWblU6EDNUjzMuOKjn7oUM0nw7XPfUwccT81mBgZgKnBM6HmNHqJI697JvDiRZlSy0ZvEWx4I1n6FQKlwKvhMNcUCLlfvRmpHznxQNxm8UKs3KxllAyVhmU1_aJqiOgv5tGgBlAvh9ete-dB6vkMMEUi2_NP5lTEFcQfbRMgx7xiM3wYwioD0XfCyeoVTEvp8UgHp72AVd7iv9gDbHm3RTMvLZW8dvSbhGSVEG95gbLcm1lvZmoPyaJ6CXtsMwlhrOEo0MRGo69pBdGxPvx729_Vjla3sf3C5KCticxrB5J_t3ivaWA82kt1t3sUhVtL3iZhWojvJ1n9-8KWrMmwtXn79eeV-k7ZRuEErsYgUGhkznkHD_TKO3yWeNqtYelpRiF38HaAiiLlX-YV0ZhesAuph8okXth4i2JgNocud-bEsmzh8K5_yz4Ma9P1PgypC1wuDo_rimwPRM6kJB5oyzpBHG5dg8KNdj1cCo0Jxx0RhBXQNL99ILYBm0YGcjXkCQEYSy0reg87DS9NelSozGJHUy4LvcPGPhBjOT8KWzf2AaJKw91wtQi0JqYNAskYEGpKftSl2yBOi-GilGt_xc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32c2ecca4f.mp4?token=HsJv1nXhjlIos5fzeA2crMFH7QOYHtOSd8aZYCeo51ZgjE0q17aXKHrF3AhNGeWsQEA3HM_20LIOee9VMbvZCkWblU6EDNUjzMuOKjn7oUM0nw7XPfUwccT81mBgZgKnBM6HmNHqJI697JvDiRZlSy0ZvEWx4I1n6FQKlwKvhMNcUCLlfvRmpHznxQNxm8UKs3KxllAyVhmU1_aJqiOgv5tGgBlAvh9ete-dB6vkMMEUi2_NP5lTEFcQfbRMgx7xiM3wYwioD0XfCyeoVTEvp8UgHp72AVd7iv9gDbHm3RTMvLZW8dvSbhGSVEG95gbLcm1lvZmoPyaJ6CXtsMwlhrOEo0MRGo69pBdGxPvx729_Vjla3sf3C5KCticxrB5J_t3ivaWA82kt1t3sUhVtL3iZhWojvJ1n9-8KWrMmwtXn79eeV-k7ZRuEErsYgUGhkznkHD_TKO3yWeNqtYelpRiF38HaAiiLlX-YV0ZhesAuph8okXth4i2JgNocud-bEsmzh8K5_yz4Ma9P1PgypC1wuDo_rimwPRM6kJB5oyzpBHG5dg8KNdj1cCo0Jxx0RhBXQNL99ILYBm0YGcjXkCQEYSy0reg87DS9NelSozGJHUy4LvcPGPhBjOT8KWzf2AaJKw91wtQi0JqYNAskYEGpKftSl2yBOi-GilGt_xc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
⚠️
پورن‌استار ایرانی که در ایام‌جنگ اخیر با دختران خوشکل و زیبای اسرائیلی رابطه خشن جنسی برقرار می‌کرد، دست به توبه به درگاه خدا زد
😳
😳
😳
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/106843" target="_blank">📅 09:04 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106842">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/s5fGN2inmCjsg6fKLaRLXZFbxWjhtqDs2PeWBfCZk5dVXF-b1P5nbzL_Yon_1TgxZzPLAzvkjo-x6c2x1zIJyH29p0-1H15FMWFfjDDtje5EY12pqIMLso1I91gI25vPmmmGz3wlwmjEgZ5Jibn5PjJtAfFdoTqwxr35NyrLCchtfS04T9rnJeB2_zqUQB30vGYJ0jM20fTaXvFtWYc441KsSQ5IEBS4YZfBF1aYWgZ04WbbmrTqpHKabxLgvVB5_dFQLvq6oYNAxiauXz2uh_dfgR4szEVrrtsKi56rFHubAXyYKel5PBBsO8dBmdgVmIuGUAzp-jr3UtXm5vFvmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🔥
فیتیله بعد از ۱۱ سال پخشش رو دوباره از شبکه ماهواره‌ای Fx2، شروع کرد.
هر جمعه ساعت ۱۰ صبح.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/106842" target="_blank">📅 08:17 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106841">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/583a7cae1d.mp4?token=G6RzpKdkoB3ui7DPvDTz_RmcqSTQJjGVwtG-VJ1iartmHuqIBsgxF2qTh8oOxDCWk20FkcDfMOqWnnZppUP0tzO1JWV3Stl5q_kJdanvsRsyqKYzxilJyvACeLJ3gqz2r7C0lcNky9WbWhaMEhHjPOHPe5f4KvG8JcozK_X01NyMN4rYIhh4oj5xcHKY0ghl0oavxvuLw3BlK3bIfEZYMrmp2wp4a0l9HVox2iE5d5Y8BAAOYl51O28mP7qFDoSQtfm89pYFLgxDZCosxYRbfv7WNb5u858zH8hgtuXcINzsn4wnJiSpkQitDIuK4UAbsJzyAqmujM8LTBgBEJbqyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/583a7cae1d.mp4?token=G6RzpKdkoB3ui7DPvDTz_RmcqSTQJjGVwtG-VJ1iartmHuqIBsgxF2qTh8oOxDCWk20FkcDfMOqWnnZppUP0tzO1JWV3Stl5q_kJdanvsRsyqKYzxilJyvACeLJ3gqz2r7C0lcNky9WbWhaMEhHjPOHPe5f4KvG8JcozK_X01NyMN4rYIhh4oj5xcHKY0ghl0oavxvuLw3BlK3bIfEZYMrmp2wp4a0l9HVox2iE5d5Y8BAAOYl51O28mP7qFDoSQtfm89pYFLgxDZCosxYRbfv7WNb5u858zH8hgtuXcINzsn4wnJiSpkQitDIuK4UAbsJzyAqmujM8LTBgBEJbqyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
پاس گل جالب دنیس درگاهی با ضربه سر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/106841" target="_blank">📅 08:07 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106840">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/106840" target="_blank">📅 00:21 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106839">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTrexBet IR</strong></div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/Futball180TV/106839" target="_blank">📅 00:21 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106838">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/106838" target="_blank">📅 00:20 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106837">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hRbEAC5kXoCvqpWB1qCoes0J2rN4e_HuRoDuajVwvbkUDG9AZzMdWyXuj9ond0bUnklITa_9Fyne-Ia61voi5mLDJTpo1obLwfvmXTwTfE9zvLPJRm-_Ruk0OL4bh_-eqiDJiDO1qoLH-aeHbWL5juWmlXybxuiFKnbxZ5ccaNInes5KuqyRPYe6JS4fAvS-uUhl8m2bnnGF2lb-Pj-P4lYSdtTgnfGLkc-Eoyi8sWlFS_7EOuRcYchgwUH-hjgYFRi1qUYOiusQA2vWAqu3lGx5HSnZksdJF5pYgfvI0yRFm65JkSO0Bp9_8_jn1CEddEImjgsp11YSj-PiELW7NQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
لامین یامال درباره علاقه‌اش به نیمار:
🔻
همیشه سعی کردم بازیکنی باشم که با خوشحالی بازی می‌کند، و نیمار تجسم واقعی شادی در یک فوتبالیست بود.
🔻
نیمار از آن بازیکن‌هایی بود که فقط با دیدن بازی‌اش لذت می‌بردی. نوع بازی‌اش باعث می‌شد تماشایش سرگرم‌کننده باشد.
🔻
تقریباً تمام دوران کودکی‌ام، صبح که بیدار می‌شدم یک کلیپ از دریبل‌های نیمار می‌دیدم، بعد یک کلیپ از گل‌هایش... او واقعاً بازیکن خاصی بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/106837" target="_blank">📅 00:19 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106836">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ofRZ52L_Vq8RJe2opxgdFiUmIhkTQRArZr641rPx58miCQzv8sEoNc5hENwYdI8ITf1H3Zll3FTKxz-dA1J6uEUAPNsNUej7cwaAxrwB7Ce2ZpDILrhfOHVfck6gB_dUOKrPYNYcwtSt0SvGADDpaN6_JiL-QXINA6xlFGd9fySaFgLkejonjkW7w19EyyTXrh_1vFYhwbW2un_n4x-6zWiwtaXLRO8P1RuGirBeCKALmEDde-nxoBqboJftlIySbyBZJ-xEPNNaclYyBiVnHc6Rl5e_1Wt-sz9zMpQ7G_Ty7CTr1SiO1rvDibxl3-ez_d4ljhdNfOrUba9jsEYzXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
⚽️
يحیی‌گل‌محمدی و تیمش دهوک در هفته هشتم لیگ‌عراق مقابل حریفشان به تساوی رسیدند. این ششمین تساوی یحیی و تیمش در لیگ‌عراق بود!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/106836" target="_blank">📅 00:14 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106835">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gl9jAfSQUaWJ_lOthIyZat1gnTqg0W-5ajlbcmHtD-fopakMPrUWaQAo6i16o2BYjs9dlIVEPCTKdAv8o7BKCNab7D15QRWeo8eGNGc2AkG5ANIpNHwzCxXKojzC_F41sebKiPQhSt4zZz1r_c7EYofQ03UOO34D1LWOsYltWWIdjpFNZ2whbLs38EJypP7X0H9cKrDcULdYqP2wDMbBmvKpdk9OrcODzWXdf2FtnUj9SuJHfKb1iBDa7ewY_vbW6x0MDbR2Jr54MnA7Mllw8K5RVJf8pt5xMiw2PRXJKSqqEhtA9HlKLU6nkq8hem7VPWSZMi19rehOYzjIf08W7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👀
‼️
لامین‌یامال: تا پارسال پاس گل و دریبل زدن را بیشتر دوست داشتم ، اما الان گل زدن از نظرم بهتره ، گل میزنی و تمام، کارت را انجام دادی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/106835" target="_blank">📅 00:13 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106834">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1135acc96f.mp4?token=YTpwXqxc5zwgWAISpwsP3DOlWdqZ1SSNUhS0C071hEO7JDnvy-ja0ISktotw7UMREuu2j1c1rdwPwxVHOkAKTB9wIsv30h3GomEDPzWpx5K-tMVYeZC6lg9fn6SicVRoFGQVJW1qrSRTd1vt3mJv8xRDALXV2vvdZtySJy1i7u1rs0iSeePLpJE00zJY3CxBaimE9M56ky61leGO2cwGSm998c1qYeyROHG7WmCYCRlVv_dpLdXq-oBh2yJgtcm_k1Faj-u44hwwNd5BJQuKmmOyvsTSrtsGkqXKNmANRmP6l0wfWTTgiIG0JzWoAk4ZLnKWbepRXSau5927tnh2SQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1135acc96f.mp4?token=YTpwXqxc5zwgWAISpwsP3DOlWdqZ1SSNUhS0C071hEO7JDnvy-ja0ISktotw7UMREuu2j1c1rdwPwxVHOkAKTB9wIsv30h3GomEDPzWpx5K-tMVYeZC6lg9fn6SicVRoFGQVJW1qrSRTd1vt3mJv8xRDALXV2vvdZtySJy1i7u1rs0iSeePLpJE00zJY3CxBaimE9M56ky61leGO2cwGSm998c1qYeyROHG7WmCYCRlVv_dpLdXq-oBh2yJgtcm_k1Faj-u44hwwNd5BJQuKmmOyvsTSrtsGkqXKNmANRmP6l0wfWTTgiIG0JzWoAk4ZLnKWbepRXSau5927tnh2SQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
🇮🇷
محمد تقوی، در برنامه هت‌تریک درباره پیروزی استقلال در برابر السد در لیگ نخبگان آسیا گفت: «استقلال نمی‌تواند در لیگ برتر مثل لیگ نخبگان بازی کند، چون نوع بازی تیم‌های ایرانی متفاوت است. دفاع منسجم استقلال اجازه نمی‌داد بازیکنان السد، به راحتی بازی کنند.»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/106834" target="_blank">📅 00:09 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106833">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/914fe9902d.mp4?token=k9grUfUNanTxQ60QWbN4xQxkTORrftG57mje8nBjWhGYY1R1oz1G1Lh4ryfuETl-L4sVHuLlKNs3NxH1aiPcXVZsp_bCDPpf0QY0bn8BTDmGDLh2Ug9nca1MYlxH5rfomF0_S7zvP4fac_FhqFE6_Lmv79pc1OBZwGQUiG62D-09RQ9XXkSyHl-IOLKzCMRYghnEnuUPZEO8JT_prEk9QnEqfGZzNHHgarFs5C63wJVwhOI_xZ5tcyHqNDVrzlTOQ81bTsjqKRirxV_Us40grO5fDJ6OLW-Mfhr4o3HnFOa0E5mYpXeaRaQTQE7uWDbQonvVA48EyIiha4uXPqgxog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/914fe9902d.mp4?token=k9grUfUNanTxQ60QWbN4xQxkTORrftG57mje8nBjWhGYY1R1oz1G1Lh4ryfuETl-L4sVHuLlKNs3NxH1aiPcXVZsp_bCDPpf0QY0bn8BTDmGDLh2Ug9nca1MYlxH5rfomF0_S7zvP4fac_FhqFE6_Lmv79pc1OBZwGQUiG62D-09RQ9XXkSyHl-IOLKzCMRYghnEnuUPZEO8JT_prEk9QnEqfGZzNHHgarFs5C63wJVwhOI_xZ5tcyHqNDVrzlTOQ81bTsjqKRirxV_Us40grO5fDJ6OLW-Mfhr4o3HnFOa0E5mYpXeaRaQTQE7uWDbQonvVA48EyIiha4uXPqgxog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
⚽️
گل‌های دیدار بایرن مونیخ - بوینیون برلین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/106833" target="_blank">📅 00:06 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106832">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6e28dd692.mp4?token=jk-c50J4DRyQ7M6sNDk6R7fpknoDP-h4ROGJedOSyqNl75EidTIevDAIhXiXtlfw1kGC7WIGLErkRTueR0YEoFs_9hCXf137U0YZBL_TbGNYc-jNsnGVBnGXvfy6xXqBs7j6hJzTpDezTCW8WHmvv0Ye9v6MhgPCz5gtxGnP2o2dF7H-Yi6qzat3LXekpJaVk25h9Z3JvgPjIggFmDCWEZgerv29qsKsSZweSj1D60OZALlJsmMGcYOKGBW_9MS5WceqxFZ07tsjzltmhFlHzIv-SEPTM5cY4bRGT6eKMg6-LjWDM8ZzAx6V0rgcPpD54XQfQr1un-22FNod_YbECg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6e28dd692.mp4?token=jk-c50J4DRyQ7M6sNDk6R7fpknoDP-h4ROGJedOSyqNl75EidTIevDAIhXiXtlfw1kGC7WIGLErkRTueR0YEoFs_9hCXf137U0YZBL_TbGNYc-jNsnGVBnGXvfy6xXqBs7j6hJzTpDezTCW8WHmvv0Ye9v6MhgPCz5gtxGnP2o2dF7H-Yi6qzat3LXekpJaVk25h9Z3JvgPjIggFmDCWEZgerv29qsKsSZweSj1D60OZALlJsmMGcYOKGBW_9MS5WceqxFZ07tsjzltmhFlHzIv-SEPTM5cY4bRGT6eKMg6-LjWDM8ZzAx6V0rgcPpD54XQfQr1un-22FNod_YbECg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇩🇪
سوپرگل دیدنی اولیسه مقابل یونیون برلین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/106832" target="_blank">📅 22:45 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106831">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sz0U6vJTtl_PxTpZRlGLnDCxwq9kXkOKFDbEaZd_2MDM3rfU4HYHn4tQUGPRZiXmPzune2l_82aK3amz4uKXoYZ-btqWkOO_DGZ7EVQW4KaL19R2KPnghzOZNaFazgcTHed1QGzzZasinpaARgIVpKsh1SMbPJbjAB120rp8CWCDsrg4fC38Ux_ym7h5QDmwCwzEuD-j4lh5MgzTdy_YyPSmJxfWmZgPuNMv8-WYVjc_jToI3RGE8YaJUwNKUW_SqlSI1xY_cGtPMNrafMdcF2hdqgvEKlDbQJlnWfIZXt9n_JiPXk_qbpe0CcgbdCut-u8nxmeDpLoYtVPIEG3L7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✔️
🇪🇸
🇪🇸
پس از دو بازی غیبت بدلیل مصدومیت، آلوارز به دیدار یکشنبه مقابل رئال‌مادرید رسید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/106831" target="_blank">📅 22:40 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106830">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZfXfqBC2VOB4ly3KOyK1tcqboRZUKk_KvUmrf71dpMXVZKNUH3_wVMHGDji_k69_uEtImvKIs77jNCBmR60Pthpb-QSZaK4bk4ZfsDavFJVYCdtdVAmAtUItEfiuYT4MU74gsw4at-eQiynuW732eGPoZnh5SHNZcIxvNKTHddKF8Ih6Pp_34Mk6unUun4HmsfRJz4tVqF1SFdlMQDXLAehQ287VrGm7Ad-gULpYTA3hekBjaWDA6zakkUcCMgThTWrAfMLYIA3NxdTd2BxCN8Gibiegl1zS8nE28M4qnBapZIAKsb-4BuBvTwX5igP_aa36HHPI1ON8FmsUDSq3UQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
داکنز نازون پس از عدم موفقیت در بازگشت به استقلال، راهی النصر لیبی شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/106830" target="_blank">📅 22:27 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106829">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e3aa9abbc6.mp4?token=f5Z499pxEHCzIb-VL9PqEW72MFlbCtauo71Gmoe481J7J_6-4C66JxbmDLa27D7QXREtWTzATJw92IbXqjk9iuJDKNTf0yn1A9n9e-YA0YxIT9rVYXc-d5bgQjKpPQodH4asM5AMpz9WfPdwK7lR5E36ZGYjL5ECtPScLICJSN0VuaAPtWtnQ7vlNAsHTru5Z2zYocGWE809dC_9RQng_-1MExxIXhNwLqvKk66r0mnZ2sYUaNbw06EMBh0LGESjgwxiGgCfz0WXkSEacm7rA3-g0_5pGieMcKmOSgCasyW-ZOzj02HY1P9L-GCEuo4U8_YZbG94N_pWlU8d1T85Zw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e3aa9abbc6.mp4?token=f5Z499pxEHCzIb-VL9PqEW72MFlbCtauo71Gmoe481J7J_6-4C66JxbmDLa27D7QXREtWTzATJw92IbXqjk9iuJDKNTf0yn1A9n9e-YA0YxIT9rVYXc-d5bgQjKpPQodH4asM5AMpz9WfPdwK7lR5E36ZGYjL5ECtPScLICJSN0VuaAPtWtnQ7vlNAsHTru5Z2zYocGWE809dC_9RQng_-1MExxIXhNwLqvKk66r0mnZ2sYUaNbw06EMBh0LGESjgwxiGgCfz0WXkSEacm7rA3-g0_5pGieMcKmOSgCasyW-ZOzj02HY1P9L-GCEuo4U8_YZbG94N_pWlU8d1T85Zw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صف‌فروش آیفون ۱۸ در اولین روز فروش رسمی‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/106829" target="_blank">📅 22:04 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106827">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UdZBu29iEzGAe1jVv0VT7c14cOSSvtlZpFFQQw7JDYoFryNovBTyE50NyxLxVQUW6Bcu8rFg99lC-jcHRDhnemBjgqEHlCcgsn5wWr-ZBmI8CEfplZ6FQse6MLQPNFwPKTI0QwLKQ7UOUMW-DhX67M21AnX4kzLY2YZMqctni23nSQiYEXwwqElu5tZYlwYJ1vpOsKgeaimwY2WosNliIrA71Q4A9QtGjy5uFmf3xcM2jgXEeGVlNlaEN2PdMBNgduXTdOtxjeL5boR503qfDNX2Aej6V23O9t80lJ1LPkf43F2W2Dakn6w5OobUpLAvQP0F2qWB3OKfQClGSl8ufA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/etq-oAnmSrRsazwCpqD6EjWyCGg3tIcWgXyZYkeNnYguAeNE0AJyrj4Zg4cUEEx4QVPkmOwvlSeXFzK3LvuF6I2FMjoz1DJjN4zNVpPlbOxMgNKIzPZQ9dhjO649GDUco4xxyXttISWteHmGMFUCXRaq_3nygtcqcdPNEFXBNyGDfIIkwwzkBCf_1-bba-G3zgD-hFKQuVKgrIbdXLakW-qx0P-khIMlXNTy6ZqgS6_JIh0XpYc_gj-7cl3ZJpVLpjcx8dDhZK0XdkCubMBONa7oXFp0Ahc1e2HsJd2FBZ6qvPjna0ewiq0njPAmDqnx7QsrDjo51c1otsaG2mWasw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
🗓
سه سال پیش در چنین روزی
رونالدو برای اولین و آخرین بار اومد ایران و دوتا بازی بعدی النصر تو ایران رو پیچوند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/106827" target="_blank">📅 21:26 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106826">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cJrWShPDwzlBk8YD-bhkIko4dYsS-XMYPDsrt-tKy6Fdn8_EQfwyInwFmMDcsRzbXlNCayBMsK3ZFpfk39DGKQqpx7WjObC3JUwhhPI88Ow_Pd0eYzAOBqMJXATObQo_lusGjb8nKXNlG1wMA6q1lXaNU9jKu-rqvwlNKaU1tfNonXXvFVxUBKvzLwMGf2gb3_W1YFqUyt2dWmIDX6ldh89M0PPRJOW5LqcR6X0r9xWPHhsv55Di6iIFyXW9SABqV15ZeK3Ki4L4xichePIYE-iA_gImqAwKPso560F6ViCwM9FInwpkATKLKJOAssS3OFuJs1SLa8A9uArPPM4kGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇩🇪
ترکیب بایرن‌ مونیخ مقابل یونیون برلین | هفته 4 بوندسلیگا 2026/27
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/106826" target="_blank">📅 21:10 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106825">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qKD3NxwH3WuN47M9sJeQzqxeu_cvgzBkdrVO6SpWb_WczPI98_vFqWakY15LrY8fvhza8lBreZz-8GbotjP2VK9ptgF7BVb28Or3en_My3UhoX_yEHpGEFmzFxFZXXpBEL5zbAyEY22wKmEU2b2Yto-icJ5h_kJcyVOZZpAy8ljVI-EnMKyXJI16XPodNNqkapuv2QhvWAR7AQ2NQzSH34y6nezn2HdK6caU3-LjMx4BshfWcR7iB19k_GtLBZfrkNoUFpvCBolHRaN-EPdrzp8y0o-mvEBvm8Bw9Hb23UEBarVUnuZdb8TpeFfBJXtPKAUVaRnqdefcuNKkYjxEBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✔️
🇮🇹
لیست تیم‌ملی ایتالیا برای فیفادی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/106825" target="_blank">📅 20:32 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106824">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/daa894a6b5.mp4?token=EkScsNGMKzi-DQgzbCc1VO6rNO8c0E_h7GRjsNaXTQYFkgn-F6Wnz18ZDoFt0nnTz_UL3JKci7TjeWdyt1mxrviMM2aeyKyNZ9EuBg-FaLTsRwgoQj1Ycu-q_Nu8mlcxSDriqOD_84xliWlN7v9vUZLQYd2GA6-XNP5RAZ2BoNsAplh3ExKhQxu4_99ojAj2CbHWvsVsIQuQF7uAYw_LSXLWwbNdmPOFFgVOTfT6xre3mr3gNC4ykQn1CLYi4LKgGR4bx_lJfeXsBbMQePVcmaKGSKv3wpcu4J2WSh-GS8wqP1R-BtE_xkmXroQ087Lb7dv_JCZ91GKuQQI66u_mxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/daa894a6b5.mp4?token=EkScsNGMKzi-DQgzbCc1VO6rNO8c0E_h7GRjsNaXTQYFkgn-F6Wnz18ZDoFt0nnTz_UL3JKci7TjeWdyt1mxrviMM2aeyKyNZ9EuBg-FaLTsRwgoQj1Ycu-q_Nu8mlcxSDriqOD_84xliWlN7v9vUZLQYd2GA6-XNP5RAZ2BoNsAplh3ExKhQxu4_99ojAj2CbHWvsVsIQuQF7uAYw_LSXLWwbNdmPOFFgVOTfT6xre3mr3gNC4ykQn1CLYi4LKgGR4bx_lJfeXsBbMQePVcmaKGSKv3wpcu4J2WSh-GS8wqP1R-BtE_xkmXroQ087Lb7dv_JCZ91GKuQQI66u_mxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
🎬
👍
پدرهای عزیز به این‌دیدگاه عقاید جالب علی فروتن حتما گوش بدید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/106824" target="_blank">📅 20:10 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106823">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ed690df00.mp4?token=mGWZXB06XmE-iK2GIXgqF9cKr1jSZvtAZfmb82ODOZmm_E0O4JmPeSlPTFhd9F4ybGhH83p99stsimEUgCA2VFyT81zegAGSckcq87wp7Fk9xWYiKz_O1GFrmqtTp7EunlJ7hNu04qmHYqnOjV3zD9AmEFakr0FF4QVpYWQDIQiGy5kR98bzEbo2-PAMaCcBd0WAaNIhk3uAhZf30Q6X73PruRuXj_zW7kj2Gj06RUIvt8G_sp0i4PuOw4rmDJf0NKzog-gOWOUrvCF_FRhhz_puS2d7wyqX8OE8EBZ6D2JCrygaDR5togrhjxLTc2nI-9XRQAnBu0124mfxZTPTHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ed690df00.mp4?token=mGWZXB06XmE-iK2GIXgqF9cKr1jSZvtAZfmb82ODOZmm_E0O4JmPeSlPTFhd9F4ybGhH83p99stsimEUgCA2VFyT81zegAGSckcq87wp7Fk9xWYiKz_O1GFrmqtTp7EunlJ7hNu04qmHYqnOjV3zD9AmEFakr0FF4QVpYWQDIQiGy5kR98bzEbo2-PAMaCcBd0WAaNIhk3uAhZf30Q6X73PruRuXj_zW7kj2Gj06RUIvt8G_sp0i4PuOw4rmDJf0NKzog-gOWOUrvCF_FRhhz_puS2d7wyqX8OE8EBZ6D2JCrygaDR5togrhjxLTc2nI-9XRQAnBu0124mfxZTPTHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
▶️
مسابقه دوی نیمه ماراتن بانوان که امروز در بوستان ولایت تهران برگزار شد که حجاب شرکت کنندگان بدون محدودیت خاصی بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/106823" target="_blank">📅 19:55 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106822">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PVejnjTyLU-Hb1VrRG4OyNPcDZJJ5fr32PMxyZDuVVaLAtIHMfRzo6qJPsdoY7_G5gWDxmGMbUEfynzw7OfOnYUYu_TMdPbOKM4tbQ2NeYbBPLEKxe8xqKSwoL_s-IiLNR98aP9G_GQ8ReIB2kKYbW95awkg4w3UId8hQszRDYMeovD3Tn9dkOQ_MJ-Jq-K_FSd1rNOlpW4uoyttZPwrMRRRK23oox2A6lTtdP_0SjN7WCDi5PA45z5Qab26k-Ab-n7_mCCaEpVd4OtqJRIZsUQls_3cBccYzhiA0DCzBO59KHc6PpfM1L2720Eu-q6n-tuSHTyTlbFOE_UhewPejA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
🇫🇷
لیست تیم‌ملی فرانسه برای فیفادی در اولین حضور زیدان روی نیمکت سرمربیگری خروس‌ها
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/106822" target="_blank">📅 19:36 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106821">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b69347998c.mp4?token=hmcpCogZUttoCiTjtkBUnzLsXLmVY95CkgTsM_1AfgBpgkzJeNaXBJCpSfFXc9hcETf9i513gZbLZ1zkYulu-L3K_oMoqDX1QCY2SG74JQF31g4QGeyzKZ2g2Ej8Oa10sKHJcVvIKgovbMnouRzBaPmHag27UbQfcnKay385Erz97AQOlJrqtBk5_zr-tb4lQuyLzvGEh_5t6Ia2KlvVMpUHUkguaZx7KNdJ4u86WQ9nHFut19dYJSVXN1uAJ0tBCIXIaMJb5iRV9At-AJOCIWOYPlJBV8FSizRFovCla0RPq_9D2Fqgs8uitW0E7PAyLL_XGL_YwibucsIAbn5WvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b69347998c.mp4?token=hmcpCogZUttoCiTjtkBUnzLsXLmVY95CkgTsM_1AfgBpgkzJeNaXBJCpSfFXc9hcETf9i513gZbLZ1zkYulu-L3K_oMoqDX1QCY2SG74JQF31g4QGeyzKZ2g2Ej8Oa10sKHJcVvIKgovbMnouRzBaPmHag27UbQfcnKay385Erz97AQOlJrqtBk5_zr-tb4lQuyLzvGEh_5t6Ia2KlvVMpUHUkguaZx7KNdJ4u86WQ9nHFut19dYJSVXN1uAJ0tBCIXIaMJb5iRV9At-AJOCIWOYPlJBV8FSizRFovCla0RPq_9D2Fqgs8uitW0E7PAyLL_XGL_YwibucsIAbn5WvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
اولین واکنش امید عالیشاه به فحاشی ناموسی خداداد عزیزی: دچار شرم نیابتی شدم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/106821" target="_blank">📅 19:32 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106820">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/854ffbdefd.mp4?token=K0h5wqnkEPZ7sz418zkRBTZSkRaoBlAq7H1LUInhRpEIytHufypHsApEuVf4DEzsZYWWFxNYQXhcROJS17lM0KJtzerHYWmRh_EudFBh3kHj7Bi4BFharmNqLnSaH0Dib4H9w5UeG4O9pnRWtj3r4PKGnP88DIeBt2KXgxDz7BNzDQVF7dKHxBK_AG9kDwHFK6DUIcrA-Ng62e3YLTaH2yl21P-E5h9c6anBDrUhdDJ18V1HJsbm7hHocKZ7ziqd6c6dKRN_7CEDB-h-xXy8exNCo4pA4U6M0bntlv_t9vboWmhb9RlBE2YMDxpmK6KX4Zii8JJ6ep7no1Ub4T_JRIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/854ffbdefd.mp4?token=K0h5wqnkEPZ7sz418zkRBTZSkRaoBlAq7H1LUInhRpEIytHufypHsApEuVf4DEzsZYWWFxNYQXhcROJS17lM0KJtzerHYWmRh_EudFBh3kHj7Bi4BFharmNqLnSaH0Dib4H9w5UeG4O9pnRWtj3r4PKGnP88DIeBt2KXgxDz7BNzDQVF7dKHxBK_AG9kDwHFK6DUIcrA-Ng62e3YLTaH2yl21P-E5h9c6anBDrUhdDJ18V1HJsbm7hHocKZ7ziqd6c6dKRN_7CEDB-h-xXy8exNCo4pA4U6M0bntlv_t9vboWmhb9RlBE2YMDxpmK6KX4Zii8JJ6ep7no1Ub4T_JRIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
🐐
دیوید بکام: "من هنوزم باورم نمیشه که اونو اینجا تو میامی داریم و داره واسه تیممون بازی می‌کنه. همه ما دلمون می‌خواد لئو تا ابد بازی کنه. هیچ‌کس تو 39 سالگی همچین کاری رو تو این سطح انجام نمیده. پس حقشه که کاندید توپ طلا باشه. به نظر من که باید ببرتش!"
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/106820" target="_blank">📅 19:10 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106819">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1dccf6f34c.mp4?token=SNQBVZnHj6KQtU6Wtk0gB-EEbE9P1eVtY6-br1UE2jPnRVwRVtUVq4N_yzCOn6d8uq7Nzf7YH9UckTMIuM8zD6uEPF0kBtvaKebJTeu3NuPyuoM-7MwYgHlyKOopngcKItmYB2l7DYDrF5u2Ue8zUzO4i0CQDvr-zOWcM9xQz7yAfLfi2m10cPKW-O0Z3mfKgXxmT2G5izyRfcj1o2Q2MQX6kGgIyWj5ColU5BNggaUGYptf4PaIIBIbULzZrbFK2uoSdVGzEivUdoxA2i5930UidZOYR9Mrrp_v20xFX3z_K_2azdy7EqZUYFtBpJ1K3VWzw2jgfdOqQbwFJVHE0rRTq7QzkIIs5_w8nyBz0gni05jDHIsuiqsAnsBw-PWlnh7HUp51GN5e0TbYihxHFcT5XiiEYmbiQQm5posyy38O6Czvy4SDo0v0_gWyFCeoYmeLSr24L1wJfdVIYgKW95pZURZQfpP0Am_p2NEDGKwy0SkZRevl-x2YBB1EwTIjb81459-QDRQV1T0KvtckIS5dpKks8MOOaXqbKoCGPP44ZErjOjHfbbHFt8L0r2lihHxKGGM9ibGODcYGmqX2W7pa6ZMaSJWg0JMCBpcRBHTLCPttfmB_5VReD_Jr8LLQxOtQRkeLrIHwWll-d1Ytk6CqBLgFhxqoirJGTbTW73E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1dccf6f34c.mp4?token=SNQBVZnHj6KQtU6Wtk0gB-EEbE9P1eVtY6-br1UE2jPnRVwRVtUVq4N_yzCOn6d8uq7Nzf7YH9UckTMIuM8zD6uEPF0kBtvaKebJTeu3NuPyuoM-7MwYgHlyKOopngcKItmYB2l7DYDrF5u2Ue8zUzO4i0CQDvr-zOWcM9xQz7yAfLfi2m10cPKW-O0Z3mfKgXxmT2G5izyRfcj1o2Q2MQX6kGgIyWj5ColU5BNggaUGYptf4PaIIBIbULzZrbFK2uoSdVGzEivUdoxA2i5930UidZOYR9Mrrp_v20xFX3z_K_2azdy7EqZUYFtBpJ1K3VWzw2jgfdOqQbwFJVHE0rRTq7QzkIIs5_w8nyBz0gni05jDHIsuiqsAnsBw-PWlnh7HUp51GN5e0TbYihxHFcT5XiiEYmbiQQm5posyy38O6Czvy4SDo0v0_gWyFCeoYmeLSr24L1wJfdVIYgKW95pZURZQfpP0Am_p2NEDGKwy0SkZRevl-x2YBB1EwTIjb81459-QDRQV1T0KvtckIS5dpKks8MOOaXqbKoCGPP44ZErjOjHfbbHFt8L0r2lihHxKGGM9ibGODcYGmqX2W7pa6ZMaSJWg0JMCBpcRBHTLCPttfmB_5VReD_Jr8LLQxOtQRkeLrIHwWll-d1Ytk6CqBLgFhxqoirJGTbTW73E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
🏴󠁧󠁢󠁥󠁮󠁧󠁿
انزو مارسکا سرمربی سیتیزن‌ها:
🔺
تردید هوادارا پس از رفتن مربیای اسطوره‌ای طبیعیه. این شک و تردیدها برای هوادارای منچستریونایتد و آرسنال هم بعد از رفتن سر الکس و ونگر وجود داشت. برای هوادارای سیتی هم همین مسئله صادقه، چون پپ هم یه مربی معمولی نبود. اونم مثل سر الکس و ونگر، یه اسطوره بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/106819" target="_blank">📅 18:34 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106818">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/106818" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/106818" target="_blank">📅 18:34 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106817">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hJd0XAcQjTuV0KKmG2JXVuI7EWcJfBZeetf_mqvcuMZot-hl5TirHpjV4ljg5G7an3008GxGEtxuEVy_GyMCUt1jWFFRqEbd6mYL4fH_krw5jHbn9D1Pr0MAfMgq7c06XC9_uJ9qMb5Ti-So-97W3wYSsk4N3TQse0ZQkwntwT3SM69QnmOjsvedm-jlCwYnBLev3GpY3LK1odNmeo_YiDSbX9XeXZHlL9K81vuAe9ymmBvTmLvYI13adN-jLSqQexh9FE2G4ZBVlRCXrYQWpKP4eYsdxal5z15dfDRFYVTRf8yHnPus1zNYi0GRufqfyDZdME3THGNTEKQrYTZY8w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/106817" target="_blank">📅 18:34 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106816">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aabf7dd06b.mp4?token=XXJVEjU2WpSYFva8e1zxF_JK-8WWAuIXdIkwWKwckkv9MKvMaqo7bb1LtR0d7BmDhR4NaBD9FCsldEtWkgmssM8Y0QGzx_mE8SYpw2Q5Inac5bK1jP6sRU84yKhQ5uOJwP4NwKkXqEKn37L0g771jrutNOH_UVv5BNIIYDxc_JTA0wJnZPlQ4XiHAJ8-VWczUSP19q_ktY-WeF073wTe34fp-LRWsDvqCwHliRtEajFhCLMI6eSsCBAIaHWysq1Lza4uZA-P6RFh74hnyjN17BNyhc4qhkJJu_qYZ7k0pzTQDC5DfPqkJRgq5XEvvmdynDgnQWm5-g3mwEO689sRzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aabf7dd06b.mp4?token=XXJVEjU2WpSYFva8e1zxF_JK-8WWAuIXdIkwWKwckkv9MKvMaqo7bb1LtR0d7BmDhR4NaBD9FCsldEtWkgmssM8Y0QGzx_mE8SYpw2Q5Inac5bK1jP6sRU84yKhQ5uOJwP4NwKkXqEKn37L0g771jrutNOH_UVv5BNIIYDxc_JTA0wJnZPlQ4XiHAJ8-VWczUSP19q_ktY-WeF073wTe34fp-LRWsDvqCwHliRtEajFhCLMI6eSsCBAIaHWysq1Lza4uZA-P6RFh74hnyjN17BNyhc4qhkJJu_qYZ7k0pzTQDC5DfPqkJRgq5XEvvmdynDgnQWm5-g3mwEO689sRzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
فرشید اسماعیلی: دلم میخواهد دوباره به استقلال برگردم و دلتنگی شدیدی دارم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/106816" target="_blank">📅 18:10 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106815">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tqadMd0CFhmBoYWGSbqwaLldef2SU_xHK7DFc87k3zA-2jqc3MCtyiDH1-EDz5gBsgAvdCFzkNrOm6k48ANkObWfToSE2QSbeh9SaCXIyrXMhcBEK8_CdaxMUWgWQjbM3Cmomt_xaeokif9g_jamhmLx3-1ZcXhPFugBu8kSm_AaFtEORa_5tb4bfwN_vTZt_wLJfiAKeqfhZXIZNO3kRVPxM4Z1RkkGFJSlTaviIbxcst4GwFCljJX45NCwuCiwCWZQfRbPMigUowCCyRX5SNCCpC3wecjbO1egY2LqP_rsWlPZC0sxc_mR3HezJ2UiBnVbkKi6A2DO-6ybCpYUmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🎙
لامین یامال: من در تمام افتخاراتم از امباپه پیشی گرفته‌ام. به عنوان بهترین بازیکن جهان، شاید فقط دو نفر باشیم. من فکر می‌کنم که امسال شایسته توپ طلا هستم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/106815" target="_blank">📅 17:42 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106814">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4fd6e64a79.mp4?token=dNq6E9azPI-9rPDJG3BVIjp4uBfhi3qacAsAlAh-mTPsnrrlMQi20W7ASaVo_6S5Nw5vJnO5kY3dxGjBiRzXCpDqWWWnx_8exlwgrubAmMuEWRwSd4-NXZa9mOyQ4sS_JnKEI5YaxXbJkKgMJ2TK4lIr-_1PkSCYwQfFzLaoAM39gTpP9fo3QWJJmfKPb8Tne0XxzFeykCYdv4F0Ax8dnKD-pf3N-sI6p_bdtnHV_d91cUi-WY8UMMHzOmigPV4CiYvMVu_cQAhN_mMt1y05STIy_C7_amA2-OnaxS7Fnovy4iVxR3I7X5k-Zl-ube5g7_Al2AgPafyGSETuLvehLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4fd6e64a79.mp4?token=dNq6E9azPI-9rPDJG3BVIjp4uBfhi3qacAsAlAh-mTPsnrrlMQi20W7ASaVo_6S5Nw5vJnO5kY3dxGjBiRzXCpDqWWWnx_8exlwgrubAmMuEWRwSd4-NXZa9mOyQ4sS_JnKEI5YaxXbJkKgMJ2TK4lIr-_1PkSCYwQfFzLaoAM39gTpP9fo3QWJJmfKPb8Tne0XxzFeykCYdv4F0Ax8dnKD-pf3N-sI6p_bdtnHV_d91cUi-WY8UMMHzOmigPV4CiYvMVu_cQAhN_mMt1y05STIy_C7_amA2-OnaxS7Fnovy4iVxR3I7X5k-Zl-ube5g7_Al2AgPafyGSETuLvehLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
نظر ژابی‌آلونسو درباره مالکیت جدید چلسی که به یک فرد ایرانی واگذار شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/106814" target="_blank">📅 17:40 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106813">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dc3-x9dd_efnCWLYm5ZPjjz5JnCoVY9IT5vtx9CcgXfVyO5WXSSn-p3lCRYkiCQZtYzax3bMuBTqJ9xxF2E1oi9L9MrfGlWYXThqnpeW9HwejrhjaMccO7ghGyp6qNObSEx9yvgytIcwFqVc-xb74-C3kM6J1bNJ62uqAR0zESo7TukWn1Hn09Kej1iooTZSq3ByVMvzMAueOLTFHK7qtsOyZIhHVolyQUMFbmG2wELXQ_cODhf-aHT4hkEIJZK_pqJ7m80BgURfFpX0FyYNJH5PrlhvqTB_N15G5ebRSnGunVXEC7P-606v64B1lxpNy9j6KWfju8vFpVn7lL8cnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
رافینیا: می‌خواهم قراردادم را تمدید کنم و دوران حرفه‌ای‌ام را در بارسلونا به پایان برسانم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/106813" target="_blank">📅 17:22 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106812">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ac9522ee8.mp4?token=baFmYibV5c3L2oV34ORhR1CjmLMeRzQflP0dmlwtAA40a9lPrAMhhb67wFAPRqm9tWdvRh73EgnXhL65xnAAcdlSN1XUejGxalODyDfc2CCFzZCC_ub44G4y3i-yK1hZEaqXNXwXvnPQ2el2WBYoJKo16kipYzpJ82iP6_gI4liTd5YIEL2yBTSt3B2iW7XKQ8YmIaGFG-jjrrTpX1CKvhutgKZru_o9nGJmzWszuvAHreUqT5-hSv4YIQsmZqRZT9c2-nzTyc2BVKRlXxo-H7PONYUUQGO73N1TVSX32CtCh-1Y1XIubIVQtiXe9_zxhnaEEO2Om2EFZ-9r07otwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ac9522ee8.mp4?token=baFmYibV5c3L2oV34ORhR1CjmLMeRzQflP0dmlwtAA40a9lPrAMhhb67wFAPRqm9tWdvRh73EgnXhL65xnAAcdlSN1XUejGxalODyDfc2CCFzZCC_ub44G4y3i-yK1hZEaqXNXwXvnPQ2el2WBYoJKo16kipYzpJ82iP6_gI4liTd5YIEL2yBTSt3B2iW7XKQ8YmIaGFG-jjrrTpX1CKvhutgKZru_o9nGJmzWszuvAHreUqT5-hSv4YIQsmZqRZT9c2-nzTyc2BVKRlXxo-H7PONYUUQGO73N1TVSX32CtCh-1Y1XIubIVQtiXe9_zxhnaEEO2Om2EFZ-9r07otwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
بابک مرادی بازیکن اسبق آبی‌ها: یک کیلو و ۸۰۰ گرم طلا بخشیدم به استقلال!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/106812" target="_blank">📅 17:20 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106811">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45512a16b8.mp4?token=OdBsNN8PVvj-FpafkuwX516Xv4Pg3s7cJDhsybQRShcvZgsTitEPqxfFT3HErs-4U1YE7RB-8qgfroyIVYFocqIObzgRl7U3Noz4gbhQSnMbDDhG-ceWmE8AhUvvwtwGq7FPTskJGeTsxENUwWewgwTUWpQ0lgWojJrSXE1tzaBPaIDdg2XnkhpyhzPEkJH_BaLOGaS7B2nufvZoBVBFcWmD_Gwy1P4E6H3i3Hk8-xnG814qRbnl2EEKiEMDxwQfeQyOO1Mfdzb3sm2nkgp6NvufKDp9rmOTla9RBPUxkFswXv5R5daj2DJvaIWqBl6B8_51xf09ZXLBPX0Ji-Y9IIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45512a16b8.mp4?token=OdBsNN8PVvj-FpafkuwX516Xv4Pg3s7cJDhsybQRShcvZgsTitEPqxfFT3HErs-4U1YE7RB-8qgfroyIVYFocqIObzgRl7U3Noz4gbhQSnMbDDhG-ceWmE8AhUvvwtwGq7FPTskJGeTsxENUwWewgwTUWpQ0lgWojJrSXE1tzaBPaIDdg2XnkhpyhzPEkJH_BaLOGaS7B2nufvZoBVBFcWmD_Gwy1P4E6H3i3Hk8-xnG814qRbnl2EEKiEMDxwQfeQyOO1Mfdzb3sm2nkgp6NvufKDp9rmOTla9RBPUxkFswXv5R5daj2DJvaIWqBl6B8_51xf09ZXLBPX0Ji-Y9IIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
⚠️
چرا فیتیله‌ای‌ها دیگه پخش نشد؟! افشاگری عجیب علی فروتن از سکانسی که باعث توقیف برنامه فیتیله‌ای‌ها شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/106811" target="_blank">📅 16:33 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106810">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i_4hznsMCHSsmv-Y-Q4ghcg4Y_2e0nXm8eslampOL8-HV8rb5SylwmLAMmtX2iEe6gfYNC5rIagm4BjtAYSJiH_SE_WM6mMCNHaAEY8TQxc9sbzHw_JuoS4-VniBxiJQPresT9yNQxqrO8e9JLfJsci7E2RwbIzrIgaUeFo0TcKYhdIbVcr8mU6JAM4BaFWQrLIuyegebrG40S-EQLhM6vJN-sNH4PXfhsR1N5GQqOXLoJPYeaosmAx2h5zh6AuW3ZIgr6HCRrNc_XdZawv5smwcm6kZXuZ9YlGZcUH6dNWClOnSooHz7ognQAT_bGQ_NyfuquprSBl2RlqGcu7qNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
💥
۵ قهرمانی لیونل‌مسی در ۱۱۵ بازی اینترمیامی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/106810" target="_blank">📅 16:05 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106809">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/171fd833db.mp4?token=MB8c-_bFDBhQO9LWDwKD0oyy4N26f-4RdS3U92okBlWq26Vz0L2C0SyY1ee1D70yeljbYPg2fwh4kVe0yrBFuGX1bahL8d_50uFPo8799zeNH5GwhtHd8lnxXHMSKX5xXxpL4daDF_vl6QNIUHitu1DDrzm1cDZ64MzkC57Pef74zsxFtI0cHDQshP44l9XzajzO7gR5P23Evnxy5v8OPMwXqs4P_KhZToOsfhqqCwFtf2YG8iFBWKywoikng-BxvFQX9FIYFYPN1Au9h_FYVAra6WrW0EJIrzjdd9_r5XYHf6qbf0hIo1ZlRfPFgEbMA1JSeZwwhzGcJcpE_5I0oA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/171fd833db.mp4?token=MB8c-_bFDBhQO9LWDwKD0oyy4N26f-4RdS3U92okBlWq26Vz0L2C0SyY1ee1D70yeljbYPg2fwh4kVe0yrBFuGX1bahL8d_50uFPo8799zeNH5GwhtHd8lnxXHMSKX5xXxpL4daDF_vl6QNIUHitu1DDrzm1cDZ64MzkC57Pef74zsxFtI0cHDQshP44l9XzajzO7gR5P23Evnxy5v8OPMwXqs4P_KhZToOsfhqqCwFtf2YG8iFBWKywoikng-BxvFQX9FIYFYPN1Au9h_FYVAra6WrW0EJIrzjdd9_r5XYHf6qbf0hIo1ZlRfPFgEbMA1JSeZwwhzGcJcpE_5I0oA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مسی نشون داد پَرش و ضربه سر هم خوب بلده.
😮
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/106809" target="_blank">📅 15:40 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106808">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eeb5c6a4f7.mp4?token=rEnomRnaPu9ss38Xlg9iKxRrOcoUhHTcfwlmHoX4z_cptm6ItpUCQUooOKfMLMtHIc2dKbC1cFXHkJTYFGNRngAk7XyCoTwkMNRmKk8zQ3RO6qGCqa4M9RMR50GpvLOXQAvR2PaDQqfzEWLsrsEMIFx9QkLocbhgPMDCVWDHkECedz_PfWv3bGMFuJjjZOnAM4-dbWKRGPqFZbqcqNC7vjNcuCVjNDscy63KLQguvtX35Imr9b30w_NSstZVCdtAAaaRqLyLJet5bXlK_dfqTN0Y6UIQUo8dC00H1gjCKYsMpqdXpqU1b4rksGQmxFWQLjHu33J2iKYZ0Zzv7ETEFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eeb5c6a4f7.mp4?token=rEnomRnaPu9ss38Xlg9iKxRrOcoUhHTcfwlmHoX4z_cptm6ItpUCQUooOKfMLMtHIc2dKbC1cFXHkJTYFGNRngAk7XyCoTwkMNRmKk8zQ3RO6qGCqa4M9RMR50GpvLOXQAvR2PaDQqfzEWLsrsEMIFx9QkLocbhgPMDCVWDHkECedz_PfWv3bGMFuJjjZOnAM4-dbWKRGPqFZbqcqNC7vjNcuCVjNDscy63KLQguvtX35Imr9b30w_NSstZVCdtAAaaRqLyLJet5bXlK_dfqTN0Y6UIQUo8dC00H1gjCKYsMpqdXpqU1b4rksGQmxFWQLjHu33J2iKYZ0Zzv7ETEFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
اعتراض تند رسول خطیبی به حمید مطهری و تیمش بعد از باخت لحظه‌آخری فجرسپاسی به فولاد در اهواز
‌
‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/106808" target="_blank">📅 15:15 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106807">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pf6-NPNU5kyQYdiZwEcQNnB6kMK-Itxb2l_uk_wwp67ILdNbZjUpQyiqiSzN9J1cTEtAUfHOLij_Vf-DnW0Xn_YD3UWvxFpMTl2RAnIAarSlzj9IOZ1-efmFAcJfuWK3ikD6KPoiTxRJdTUlNt-iEm_FvDMJYUXAXMA9jdwS9rhRBIP5EmJa8Gv2QQP-7agYPXVko01-_cAJoVWlIV5cCz6bet2_5iFIo3nOYXyPDdDhLRtl-YFjLDVt2MFcF6lZ42KpxvjZG2z1YGRJaNJOXipVhG9vPjzgqnDUAYfnzcvh_glDmHx9ni6Vp8AWuaomx35tdfOs1IAzOjGVI87ZtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🌐
گزارش هیئت مستقل حقیقت‌یاب سازمان ملل درباره مدرسه میناب: مدرسه یک مکان غیرنظامی بوده و در عین حال این مدرسه در مجاورت یک مجموعه دریایی وابسته به سپاه پاسداران قرار داشت. اطلاعات مربوط به مدرسه در سامانه‌های هدف‌گیری و بانک اهداف آمریکا آپدیت نشده بود. هیئت این حمله را یک حمله کور/تفکیک‌ناپذیر اعلام کرده که موجب مرگ غیرنظامیان شده. بر همین اساس، هیئت آن را جنایت جنگی تحت حقوق بین‌الملل ارزیابی کرده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/106807" target="_blank">📅 15:11 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106806">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a40dc07061.mp4?token=v_75HA6Msz9kjY-6jxc1B1RDOnT6S2ZPvV_5Au8gSI5K0586-RKgONiAZG8hEDe9onPmNK73tdWGEkXIrBfpQmWd8zDaKyHJFHvghgyM2_gimCabI8VIu2SRVRjhoi6y6ZNiPtY9igXVk-geMUqY30BHcUbl5fZZndCDHDRz8V71tF-q0kMfrfWKCVWAPCjSpCeRlKARis-KFNLer_I35jRvTDVP2J_NyRm61wSBIXjREQEENUVKDXuBnCG1v6-y2lF8RauPrfCqwichzbRxL7ON8JwW_1WJcQRPFiS21u3QY0YexkyaHl-coKkH_U96RZYB13PgoWZjwpacBivhNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a40dc07061.mp4?token=v_75HA6Msz9kjY-6jxc1B1RDOnT6S2ZPvV_5Au8gSI5K0586-RKgONiAZG8hEDe9onPmNK73tdWGEkXIrBfpQmWd8zDaKyHJFHvghgyM2_gimCabI8VIu2SRVRjhoi6y6ZNiPtY9igXVk-geMUqY30BHcUbl5fZZndCDHDRz8V71tF-q0kMfrfWKCVWAPCjSpCeRlKARis-KFNLer_I35jRvTDVP2J_NyRm61wSBIXjREQEENUVKDXuBnCG1v6-y2lF8RauPrfCqwichzbRxL7ON8JwW_1WJcQRPFiS21u3QY0YexkyaHl-coKkH_U96RZYB13PgoWZjwpacBivhNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
✔️
▶️
مهمترین اشتباه در محبوب ترین حرکت بالاسینه؛ به توصیه استاد هانی‌رامبد عزیز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/106806" target="_blank">📅 14:50 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106805">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZDaRFRlSX_7kfJ9mw7oPVrQhzCQBxB0pHfYzJFVF5Hf23k1u8-u3LSODVGbrtJ9jamtfVtRzEgIBVIznVQplrarP4IwRTHvSPYLuoKry9rjqEMExB96zm-Y52H3guUXQRLbEtKqn5w3SMiBBfk_-D_RdbzSEHDJipS-_vd0HenfHCt_4vqYjB_s9fql-ofB_RAxlVtUHa45lASpCPHGFsS9HldVIF3k7sP4ggVhGlCRBkzAgAOOO_LUjDvb-3hyS9eCO9zV8igO0jG9RkCBb2P94SlPozlt9NUpAVOi_hEe_eg3x-lL1MSqUIDrHYWm63hwAlR9pRVwh_MVnYK5iaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تیبو کورتوا درباره برنامه‌هاش برای آینده:
کار من بعد از خداحافظی از فوتبال؟ شاید کار توی بخش مربیگری دروازه‌بانان رئال مادرید و ساخت یک آکادمی درجه‌یک تا به جای خریدن یه تیبو کورتوای دیگه، خودمون یکیو پرورش بدیم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/106805" target="_blank">📅 14:25 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106804">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z42GLVwONmjMdqOKG6O6jkevHTAahCPLd5V5pAQlwYmFSLlw6vfumhe88HRvwG3IAyaoHudESLSmf6s4MbdVxzUhtj1C2nktd8aw1D0vtHNSVZqpeIKT0kAnrRnHkhson958IAnJ0fq5IG5GspkyaX3NdcBicxHGeugDEORR5c-WPahZu1JNur4EXaIAXD9hapClYqIcxBOSs6ood01s_9bSJapTYfIwrNnWnX9idFZxfGPLPDrCA-aZX1oQOdxnNi-gIW6_6139RYPZXTxehHpptRjzv_4ta3ZywTm8768bcbBhOYHcfuhevxPzwlDkwMVKx6TEmiq-07ThxYjNug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
هری کین درباره توپ طلایی:
"من دوست ندارم درباره خودم صحبت کنم... 73 گل، خودشون حرف‌های زیادی برای گفتن دارند."
"این بهترین فصل زندگی من بود، و این تفاوت بزرگی ایجاد می‌کند."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/106804" target="_blank">📅 14:23 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106803">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/325a2dc7b7.mp4?token=QIl-62uqNUSLYT5AkLLjjAxv20ze1hpICA1OHN6HWggfyx1X5e1fZ-zd_h-wumXcR5CZ1dRCRYuRg7gUkDJtAz4a-TfLmd9xpi3RJK20c2cf5-lr-SCdtYLi8JQ2d7HUqnnsPKfjZFJTm8m5KMelfuLQrrvWOuNPhw7CMu5qWGs22eU_eJ_KKUzCdy1MYRX5hZybzjIj7D9wyIv4ecFW-5xf8iDtEOzcqva21qMxJf4natfjM8WVssOcnO_FBcXyQv4an4FUVOmyikxzn8tg3y0e35O8QrdJnIxw7NNPeoISSBpD_VP_pfdhvRh5yVx4aVwrjT4kFNrp_6BkNfVG-wMbNVumzxFd5HBwSpSOpA5u5wTNxbcF50ZLbzzdbwqhxnca2KrkpE8IvXBpJU1h5tbLaaQb9-2AGa-12qMy5jw29SIf8J5mk3B_sGCfS1zi-hf9tbvrGYSOAi1OforVSqTzmDFghFdO0fisjEAvMqlCdzyejot3NutN85jE4i4m2QCdCIw3Npmc7_pEk1pvvZH79F3-08l_WRpCrb9gJyU41ybkD12BqMyMDzYEp6fSm_XHbotxG-Y8tiP23mzL7QiPtSaJh58TY4rTVwyzzzf0M2SUj6YjTAu7Da5BbD-wOnjy7dHd4fSMnj1GCltgL6BKbW__dzIASba4uEwqtAU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/325a2dc7b7.mp4?token=QIl-62uqNUSLYT5AkLLjjAxv20ze1hpICA1OHN6HWggfyx1X5e1fZ-zd_h-wumXcR5CZ1dRCRYuRg7gUkDJtAz4a-TfLmd9xpi3RJK20c2cf5-lr-SCdtYLi8JQ2d7HUqnnsPKfjZFJTm8m5KMelfuLQrrvWOuNPhw7CMu5qWGs22eU_eJ_KKUzCdy1MYRX5hZybzjIj7D9wyIv4ecFW-5xf8iDtEOzcqva21qMxJf4natfjM8WVssOcnO_FBcXyQv4an4FUVOmyikxzn8tg3y0e35O8QrdJnIxw7NNPeoISSBpD_VP_pfdhvRh5yVx4aVwrjT4kFNrp_6BkNfVG-wMbNVumzxFd5HBwSpSOpA5u5wTNxbcF50ZLbzzdbwqhxnca2KrkpE8IvXBpJU1h5tbLaaQb9-2AGa-12qMy5jw29SIf8J5mk3B_sGCfS1zi-hf9tbvrGYSOAi1OforVSqTzmDFghFdO0fisjEAvMqlCdzyejot3NutN85jE4i4m2QCdCIw3Npmc7_pEk1pvvZH79F3-08l_WRpCrb9gJyU41ybkD12BqMyMDzYEp6fSm_XHbotxG-Y8tiP23mzL7QiPtSaJh58TY4rTVwyzzzf0M2SUj6YjTAu7Da5BbD-wOnjy7dHd4fSMnj1GCltgL6BKbW__dzIASba4uEwqtAU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
تأثیر غیرمستقیم تحصیلات بر فوتبال، از زبان بهترین بازیکن جام جهانی ۲۰۲۶ و برنده توپ طلای ۲۰۲۴
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/106803" target="_blank">📅 14:00 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106802">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2929cbe0df.mp4?token=nx3Rqu1t-gK-Ya5zvxwxlDrmdzXSZtNOTbr5AQ_vVyOcfqUdUaVFDWe1jzuKLC2ffzofbMyHJmxm9MrxmI9-ka9XEmPA22D-x4gj2v-m09fjXTx8OZNwfqsRw9n4lBJcM3kcWncT6rSJblgFO4nyZ0PqJGjY7UXzRU1cNKVnd9HIc40yp1lpRkclMmSyJopEC5P77fuSmB46PxYZkOQqXW1sUSoHByU2NUE1YR1FIQIoZNZezcqOrZ64JiQz6jjhcQFbvsg9kmcJG3amgjvit3IdGS1rs6rT2r7HUczI09ETgPVPCU-rMHESr9Af8-mPcmX2vj__zDVzvDmRr8nAAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2929cbe0df.mp4?token=nx3Rqu1t-gK-Ya5zvxwxlDrmdzXSZtNOTbr5AQ_vVyOcfqUdUaVFDWe1jzuKLC2ffzofbMyHJmxm9MrxmI9-ka9XEmPA22D-x4gj2v-m09fjXTx8OZNwfqsRw9n4lBJcM3kcWncT6rSJblgFO4nyZ0PqJGjY7UXzRU1cNKVnd9HIc40yp1lpRkclMmSyJopEC5P77fuSmB46PxYZkOQqXW1sUSoHByU2NUE1YR1FIQIoZNZezcqOrZ64JiQz6jjhcQFbvsg9kmcJG3amgjvit3IdGS1rs6rT2r7HUczI09ETgPVPCU-rMHESr9Af8-mPcmX2vj__zDVzvDmRr8nAAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
زیباترین گل‌های کاندید پوشکاش سال ۲۰۲۶
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/106802" target="_blank">📅 13:35 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106801">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37652c08b0.mp4?token=EnTBluolJwZI3ZzAgXt2OHaV3Ywvaeo8CYf35EyneCUmzaO-ntQ7ApRWPfJjmWI-Had7mBsr2-YFOPuYk2wt3gxxwvt0f5RHuri3QLbUJZ3wTN38HFLDS8xBHl_eV5kW9dWrBVi9f8KhaK_7JuZM80ksdtBpmdrdOt5CY65sZ2sSaBakhbAAWUkWhgowM5pTGPLqfoSGH60Caf9y5ykQart-5OtL7usNtiF8Rjv7_bXhAjro4vyOWg3rIXSHyR3uGpXM8A7CX6vpBlIOUL4kwG_zUXBZmckJeXmTmGLuXx7NA3mgMBASl5scOllzqbhrl2UL9e5n5sEUNxP7mSKQtYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37652c08b0.mp4?token=EnTBluolJwZI3ZzAgXt2OHaV3Ywvaeo8CYf35EyneCUmzaO-ntQ7ApRWPfJjmWI-Had7mBsr2-YFOPuYk2wt3gxxwvt0f5RHuri3QLbUJZ3wTN38HFLDS8xBHl_eV5kW9dWrBVi9f8KhaK_7JuZM80ksdtBpmdrdOt5CY65sZ2sSaBakhbAAWUkWhgowM5pTGPLqfoSGH60Caf9y5ykQart-5OtL7usNtiF8Rjv7_bXhAjro4vyOWg3rIXSHyR3uGpXM8A7CX6vpBlIOUL4kwG_zUXBZmckJeXmTmGLuXx7NA3mgMBASl5scOllzqbhrl2UL9e5n5sEUNxP7mSKQtYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
✔️
توضیحات مجتبی‌پوربخش مجری اسبق تلویزیون درباره افتخارآفرینی کیمیا علیزاده در اروپا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/106801" target="_blank">📅 13:10 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106800">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JcjPNkjbcklBNefpZmEeNZ9oT7oPsMft2EMkpaGDdNvSi7vC4sxjQ_qIFqzWh6PNYsxhCAG3qDONr4ycVuEl-3xy5bwLh9ciaLCuTzURRjm9c9aa1KARZOgofxVDheKZs6FFCGUqLbOJMtA3eqeOO3BKjXZFeDjaI_ipRmCSNxAVAfxyPlPpV1k0ZYEkLOZxOiR6zdTE25B7EdPwyWR42cQ6qJwTI-kVzFAZ4sAkMw9jEHTJ_4SfVG4Tl8oJR21L72A-ZIbseYrNxSF3TpqUm6BwZHuAQf_gRqBJTc3J7EtebJTfrvrfWscHIrlKhUHwyOTYz7pjn6kCSXJSR0EJbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✔️
لیست تیم‌ملی انگلیس برای فیفادی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/106800" target="_blank">📅 13:01 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106799">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">‼️
🎙
صحبت‌های عجیب و‌ دردناک مهدوی‌کیا از دخالت خانواده‌ها در مسیر رشد استعدادها!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/106799" target="_blank">📅 12:41 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106798">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/106798" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/106798" target="_blank">📅 12:40 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106797">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t-oyR46xaf8y1I50KzEO3yMbBfC7ZOsGjdX52bcoO5PsyvJJmCpm7nhOHC2JkSMC6NaV1iuXBcjUSmysUCjqUOqBisv0Jcshjy8wd8jBce57IepmmygthzxUFauRlDO0W743LWCuny9KAedqCpEGBHmsAja4kpvq_hZx2ogS8T8vypBIP0ni5fR1_AbRvm7Lx2LRhaE9iq-FtFXeS3s87-cIEqvqkQ66uAh6nQ4xjcJbKxyreGYZGnrakU0X-etPvJW2n3FNSGLFssUTKeNxMJyEj_KsAFOmv030qEw4gRcX89DecWujR7aDsGisPn1IYAxxIPKcCjAaN_9f-c9qww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت بین‌المللی
TrexBet
چلسی
🆚
برنتفورد
انیون برلین
🆚
بایرن مونیخ
لنس
🆚
موناکو
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
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/106797" target="_blank">📅 12:40 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106796">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OiSua1LgimEhLsgyiOYaZ6tNgvfG_WwBwurwbpJSx3TvRQrBZRC1YM3SMmRMiq-Cb2x_GojdZWHSpiWC5RGEjX8h3dOApi50U5p0t7F5NiuwN_Z5taSfEyk7bxtnd_J_uHeywuLQfB-tZjESDFNtb01oxkecOExRzLfTd-4p5CZ-gF4TPXKxclJjNMJ4zpRYe2ddmSyrtqHJQ8wQYnu7fjNUav2ah9t9v2QSlG8VcGq8YNC5D5GlJdrmDysfrFmgGh63rjzGgF7BcHBg4ZqJZHZYfGd7Osd5Mdd5d2a6m34-6z8jCF3ksOUC0cbqro26BdHjm5r7HWkf-vhFUmdd1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🇪🇸
رافینیا، با هت‌تریک خود مقابل راسینگ، در 7 بازی اول فصل 2026/27، به 14 گل و پاس گل رسید و رکورد بهترین شروع فصل لیونل مسی در باشگاه بارسلونا را شکست. مسی در 11 بازی مشابه، 11 گل و پاس گل به ثمر رسانده بود (فصل 2012/13).
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/106796" target="_blank">📅 12:20 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106795">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f364f9a06a.mp4?token=RexepzyKL662rHtA1OCO4ZIN4KLwvj7vfcR7xcTUHKFkb6HfU7tA9mvaove3dAiMv8OYabvwxnjU5EFGurghswRhtxwpdES7wQ0JBjOknwKzROjw8ALuaoglRxCjklsF6T67HLQWAzof9T83XlHeIvavYEPBCUSsl6onY1EpECBh3peVOK5AZFoG1cVTmmL9aG96DfuMwAFMrpp2jaMqSbeNCyWJOdK5wmQGDldkAHOxx0Maq9Qvr-vOq90DvIgBPtWhPV7DrRvbVpTvi9ZwaNRqHtly9mHqKPci1T5Pbb0vIy8RQRHU0s2ZEWQXNPAoLzehj97fSE4TA_1TNx7VzJ7k9UVR6KWW2seQni853lHXv9GJYb_SPdc3tRwGR9vWWDxidasoqeBYOXIau6nDpP82WJ1n8ZSBMTr3UCX-n8GOkmicPdhY1_T7rCwf8HWYerb6HnKFYSJrI43naNKKvCMCRnwgy37E0lR4eUxSfWZJmNczZqLUSZtnPV7Juflp1r691FsVTU-J9Ok0dG3oBuiN77JPwfhiU07JUtrJoXs9h_-xQFTldv3nFWyGUIjlZHJ9bQcF5uD9x8vDGoKWnfFzzdv1aAnOWTw_xgl-9TL-YQLmZdGKm8cyU_HLo-cAXHAc7KAydqKe5y3knHJwGTaPIVKp3lliu2BL9vkgbpU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f364f9a06a.mp4?token=RexepzyKL662rHtA1OCO4ZIN4KLwvj7vfcR7xcTUHKFkb6HfU7tA9mvaove3dAiMv8OYabvwxnjU5EFGurghswRhtxwpdES7wQ0JBjOknwKzROjw8ALuaoglRxCjklsF6T67HLQWAzof9T83XlHeIvavYEPBCUSsl6onY1EpECBh3peVOK5AZFoG1cVTmmL9aG96DfuMwAFMrpp2jaMqSbeNCyWJOdK5wmQGDldkAHOxx0Maq9Qvr-vOq90DvIgBPtWhPV7DrRvbVpTvi9ZwaNRqHtly9mHqKPci1T5Pbb0vIy8RQRHU0s2ZEWQXNPAoLzehj97fSE4TA_1TNx7VzJ7k9UVR6KWW2seQni853lHXv9GJYb_SPdc3tRwGR9vWWDxidasoqeBYOXIau6nDpP82WJ1n8ZSBMTr3UCX-n8GOkmicPdhY1_T7rCwf8HWYerb6HnKFYSJrI43naNKKvCMCRnwgy37E0lR4eUxSfWZJmNczZqLUSZtnPV7Juflp1r691FsVTU-J9Ok0dG3oBuiN77JPwfhiU07JUtrJoXs9h_-xQFTldv3nFWyGUIjlZHJ9bQcF5uD9x8vDGoKWnfFzzdv1aAnOWTw_xgl-9TL-YQLmZdGKm8cyU_HLo-cAXHAc7KAydqKe5y3knHJwGTaPIVKp3lliu2BL9vkgbpU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
🇮🇷
فرزانه جمامی، سرمربی پیشین بسکتبال زنان استقلال: تمام اعضای خانواده‌ام بجز من طرفدار تیم پرسپولیس بودند و هنگام دربی اذیت میشدم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/106795" target="_blank">📅 11:55 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106794">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AfuYsGZn6SEl3O5chI_vejTP5a-pbW1CXclXErwI1OxtoXbpykeHFqqXoQdrQJ-w0cXAl4khqsa6VnXI0WF2A0ST2sCZy61vw3yI00Vm0Wh4qk_uL_dh0CGjQ3TlKZbF--rKRkcnob7hqIKvpTVUtbalChYFcj_dmAPgNYyCPe8EfP0iC2DNsUoR1H5DtlaMbyzCwZNMv4UPCxhzfCjfG15MucMd3Ei4gzH2H-E0uMHNJKgYorgZIKCcgI1cqsQkXB18HQB051q4LKQ1TeqxdT_7FkJc2U4fO80YAJ1POhZFhsAmwse5pbjFA5EUzFa57CnSzCzbw2LX5AmB1bwMGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
📊
🏴󠁧󠁢󠁥󠁮󠁧󠁿
مقایسه شروع آموریم و کریک در پریمیرلیگ با منچستریونایتد؛ اخراج بعدی در راهه؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/106794" target="_blank">📅 11:33 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106793">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd63d44791.mp4?token=u3-dKH4fZr52bp13y6PA6HcCVLE4YFEpP9RT4Sb5x9mTdg3xBpJTIciQvgPIUWoVGAzTdb8zTMdwyRuTEGhmtVNlqRf6cXpHTAnwCFN5irJX9jlJc6Aw21vcMdbW60de5jCiE-8zQC5x_975Z96wFvddeTDi6nesnglvS047xwNUxwR1MnmTQEfQL1hvFYyXy_9vClh_7Ixw2Ty-SsrOUhg2gpZA23AoqladHpTO6ceGOvHb8f-TuXOpYTZQa6Q5pJ5P64j3v5M7-cXl9xuB14ov24_bBtFNfUO6i-_ZMyX0uOyjNPubHGU-_ek1W4E-mRfqROy1l-BBcsKdodtLqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd63d44791.mp4?token=u3-dKH4fZr52bp13y6PA6HcCVLE4YFEpP9RT4Sb5x9mTdg3xBpJTIciQvgPIUWoVGAzTdb8zTMdwyRuTEGhmtVNlqRf6cXpHTAnwCFN5irJX9jlJc6Aw21vcMdbW60de5jCiE-8zQC5x_975Z96wFvddeTDi6nesnglvS047xwNUxwR1MnmTQEfQL1hvFYyXy_9vClh_7Ixw2Ty-SsrOUhg2gpZA23AoqladHpTO6ceGOvHb8f-TuXOpYTZQa6Q5pJ5P64j3v5M7-cXl9xuB14ov24_bBtFNfUO6i-_ZMyX0uOyjNPubHGU-_ek1W4E-mRfqROy1l-BBcsKdodtLqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
پاسخ بامزه علی دایی به یک سوال عجیب
طرف انتظار داشت علی دایی چی جواب بده؟ بگه نظرم در مورد خبرنگارهای مثبت، منفیه؟
😃
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/106793" target="_blank">📅 11:05 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106792">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/71e2af4be6.mp4?token=bRL3q9pIBrCIwOhd07YWkHrJjZiarHpWCyk-tCG7fO5o7zvQm4-RVN_ooao6dhb0GTAMPIkv5W_iGzr-173g767Xy5_9ffH_6PhP15ZPV-ojPvnURKFOGOtgmdu-aw5ai-qrvQUOAm-eEFIV4J9PCRlrNYzmQw6ArjQI_cekxcLnOGjU-tjJWDZinFgU2Y5c8JdzoSldZZD-z1PUEi8ZYlEC0B4iLJe6me87g4TXon-29VBO_U529MRhdH_wPr00szv_OHMVATfnGKdsyx2xPoOI3_MQyGyJEBp3B5ZkK_WUkBErPxNRVTAYYLn-AuR4xBkV_ifGiupFxaghFm22uQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/71e2af4be6.mp4?token=bRL3q9pIBrCIwOhd07YWkHrJjZiarHpWCyk-tCG7fO5o7zvQm4-RVN_ooao6dhb0GTAMPIkv5W_iGzr-173g767Xy5_9ffH_6PhP15ZPV-ojPvnURKFOGOtgmdu-aw5ai-qrvQUOAm-eEFIV4J9PCRlrNYzmQw6ArjQI_cekxcLnOGjU-tjJWDZinFgU2Y5c8JdzoSldZZD-z1PUEi8ZYlEC0B4iLJe6me87g4TXon-29VBO_U529MRhdH_wPr00szv_OHMVATfnGKdsyx2xPoOI3_MQyGyJEBp3B5ZkK_WUkBErPxNRVTAYYLn-AuR4xBkV_ifGiupFxaghFm22uQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
دلایل جدایی اسکوچیچ از تراکتور
زنوزی: اسکوچیچ شخصیت ماجراجویی دارد شاید می خواست با تیم دیگری قهرمان لیگ شود اما...
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/106792" target="_blank">📅 10:59 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106791">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bebaab7dd8.mp4?token=Z_shfvghNvZ-0ZheK7MwG34Lg3vMIs4RbQiK075ekTwOKYrJ3eoAllf5_JXbDahDM46gJKzSAD_Gv2X-qQbvdk0ft3SKZr7gZsxoHUulpN0MxlTLiOAHS3Brho3cVtw4wzQhMaIWfjvmG73tGJz-AENew2Tjo6hsrWVgSATop2t_hEPzIAKnz1zC8xQXDIuBV_fGxcb7KwEij2XjAGVucD1VO1JZBpyWPSNCo9qbEpy24OHIJdteFMKbZsSn_MwPsvV-Dnj1f1T0zddtgqcv5HQl078VG7NaYaD8vHdYp2YovJ3UtpL8YihunAO4yObQ_0JX5GvqtMTDrRfQShtQ_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bebaab7dd8.mp4?token=Z_shfvghNvZ-0ZheK7MwG34Lg3vMIs4RbQiK075ekTwOKYrJ3eoAllf5_JXbDahDM46gJKzSAD_Gv2X-qQbvdk0ft3SKZr7gZsxoHUulpN0MxlTLiOAHS3Brho3cVtw4wzQhMaIWfjvmG73tGJz-AENew2Tjo6hsrWVgSATop2t_hEPzIAKnz1zC8xQXDIuBV_fGxcb7KwEij2XjAGVucD1VO1JZBpyWPSNCo9qbEpy24OHIJdteFMKbZsSn_MwPsvV-Dnj1f1T0zddtgqcv5HQl078VG7NaYaD8vHdYp2YovJ3UtpL8YihunAO4yObQ_0JX5GvqtMTDrRfQShtQ_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
🇮🇷
روزی‌که استقلال تحت هدایت جواد نکونام قهرمانی و اورونوف رو تقدیم پرسپولیس کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/106791" target="_blank">📅 10:40 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106790">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c341c5cc5.mp4?token=ZSxxg0yQa1XyOelCHOV77SaLgrdSMjv8K8YvKvIIDzzq9u3OUZpCOTxHAEA3kJulE47gvNBRQLAh13gQf82papXI5z7oimN6SjbjD-OmZTAkM0h5yIhqZ7GFKpdU1uMA1ihkylQfCzBu_v-bLwQDTUmM-byQGTScMjHmNWb3cutMD_nYvpvfjuPOZ1jlH2fF7g8L90XGLn6Dz1sE-KuegL800UfTQ6-3ZBY4BdZWoz-JBEAFZIzXV6pRN9gUTCGNMP8bFqIBYoEFHfoQwu482Qa2IgpAyIfctdGfRqw03DcsUpmQS3vf_NGoRY2jtmW_v2zLg9GWTLaNU347Tquuv2G6bEv2F7-FVFv7Zv9wM-puBaBRhSsVreP40NlhdyrUQX3YyYDEBwiVqOADR2Uu-tdQSIfSww55UCPp6HZFmQvs1-OMLwrYyXZzehvYjpqe9Vdr9kdEZpSNB94ptl_T0GimULrYliZL8bfF-tIrh-1VFeif8VDUMiTYnjZM_E6YN4LABd37kYGHI54q_IZg9dhiWxzWRyYVZ357n4sxN3GfoB210LxABTVxw1CNPh6xOlgPzSA6h6tTBiiD8O2DxO80Bx4pV7eO_NE9-OssYXneWyCqD7FVcnmPqlspYa2_ZDO6sT5Qr_xVMPA_NAm12pPwHfoQCiJ1I8bMlZMGA0Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c341c5cc5.mp4?token=ZSxxg0yQa1XyOelCHOV77SaLgrdSMjv8K8YvKvIIDzzq9u3OUZpCOTxHAEA3kJulE47gvNBRQLAh13gQf82papXI5z7oimN6SjbjD-OmZTAkM0h5yIhqZ7GFKpdU1uMA1ihkylQfCzBu_v-bLwQDTUmM-byQGTScMjHmNWb3cutMD_nYvpvfjuPOZ1jlH2fF7g8L90XGLn6Dz1sE-KuegL800UfTQ6-3ZBY4BdZWoz-JBEAFZIzXV6pRN9gUTCGNMP8bFqIBYoEFHfoQwu482Qa2IgpAyIfctdGfRqw03DcsUpmQS3vf_NGoRY2jtmW_v2zLg9GWTLaNU347Tquuv2G6bEv2F7-FVFv7Zv9wM-puBaBRhSsVreP40NlhdyrUQX3YyYDEBwiVqOADR2Uu-tdQSIfSww55UCPp6HZFmQvs1-OMLwrYyXZzehvYjpqe9Vdr9kdEZpSNB94ptl_T0GimULrYliZL8bfF-tIrh-1VFeif8VDUMiTYnjZM_E6YN4LABd37kYGHI54q_IZg9dhiWxzWRyYVZ357n4sxN3GfoB210LxABTVxw1CNPh6xOlgPzSA6h6tTBiiD8O2DxO80Bx4pV7eO_NE9-OssYXneWyCqD7FVcnmPqlspYa2_ZDO6sT5Qr_xVMPA_NAm12pPwHfoQCiJ1I8bMlZMGA0Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
خداحافظی خامس رودریگز از تیم ملی کلمبیا.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/106790" target="_blank">📅 10:15 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106789">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0579123b95.mp4?token=J6I32P6Icf4U73lj9y3jMZ3GMGMRpuokFo-509zd6JT7sp08PVeppZxIz2Bkr0YrIizKOc4l-_ljh4AgTOoINgpfCLRV4JQeXcKhZY5AK248F8fW84lYCBEUFxITIX0OElHZ6yFbE94hlltKq9g7G930rwR29_h_bYbhnGo5MmzxqP5hr1VKRrizoTzQ5v98vxXU-gL4gFMCFySJF1_dsz3Ska4LePqQLK9tAQCYtFkaz1Krthb4xal4v5z91TD0y9yv0-Guy2f4SQI3pPGg76WgoAWFoqU1dmNN7FbDU6ydAtvJCWKjUq1n8aL0PCbji_tzn2W-DRprkf2NDzR2zA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0579123b95.mp4?token=J6I32P6Icf4U73lj9y3jMZ3GMGMRpuokFo-509zd6JT7sp08PVeppZxIz2Bkr0YrIizKOc4l-_ljh4AgTOoINgpfCLRV4JQeXcKhZY5AK248F8fW84lYCBEUFxITIX0OElHZ6yFbE94hlltKq9g7G930rwR29_h_bYbhnGo5MmzxqP5hr1VKRrizoTzQ5v98vxXU-gL4gFMCFySJF1_dsz3Ska4LePqQLK9tAQCYtFkaz1Krthb4xal4v5z91TD0y9yv0-Guy2f4SQI3pPGg76WgoAWFoqU1dmNN7FbDU6ydAtvJCWKjUq1n8aL0PCbji_tzn2W-DRprkf2NDzR2zA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
حمله تند فرشید اسماعیلی به شفر: قبل از فینال جام حذفی گفت یا قراردادم زیاد می‌شود یا روی نیمکت نمی‌نشینم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/106789" target="_blank">📅 09:50 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106788">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1063b33e5d.mp4?token=T4NCzdNUhyKGoo6QTpAuLsKotsW_uQGCwhtqIttbOpsTSmpFenk4EM0sHdA3WeROf-nZsL6HwHDaV0vQCxjuwZo8TbYoJRHouhIJQoDefJ27alwdHd43p4BT3MQJHmRKPyhQmXiofG9ANvG6t58Ul9ar-rdg6Bl3feJbDVKDS-t0bA_z9eIbervuRsraMdz7BAySxs9SD1U3G3f_NSMApEBD4KtHTiL9eEPtqscheVxzpd5O3kIxOOllwJkd7M8e-Z698Dulple1VzMrVzhX9XVvo9zXVH_wpAGuFJT3u0PFZceB8Csacn2dtA3-qH7ZFuACJVuLriFXvXQ96RYz7JfQtxMX_6npD193P7ycV9VyaFNSkf9wOjE08jLSSvy8X7PKO9_KTYNZYpmZpdbulPbC2vOkUgKW8_0jsTsPqf1nrXhaY0toFpXbWMtMLQsjwka1d_QtWD5VXaygrwuWnqQK6zInxrK1b_er4Tt0WNW5mrF-Ab8YVPbk2p8TsoJrk4-IZ3t3JzPAdYecJ-W4Ln4SH6un5mIDvzWkNz9dL76UJxrdcH4RLH30-7nCah6TrPJqTe8HWf1Ku73cM9h3k8MOIAihvqrZozwoYNajuVt77Wx9A1M3yxphdHB_TrO1e2Ha4CHPhOZ0R2bweSXbdiz99aHExA_MfpCgj_M_IUE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1063b33e5d.mp4?token=T4NCzdNUhyKGoo6QTpAuLsKotsW_uQGCwhtqIttbOpsTSmpFenk4EM0sHdA3WeROf-nZsL6HwHDaV0vQCxjuwZo8TbYoJRHouhIJQoDefJ27alwdHd43p4BT3MQJHmRKPyhQmXiofG9ANvG6t58Ul9ar-rdg6Bl3feJbDVKDS-t0bA_z9eIbervuRsraMdz7BAySxs9SD1U3G3f_NSMApEBD4KtHTiL9eEPtqscheVxzpd5O3kIxOOllwJkd7M8e-Z698Dulple1VzMrVzhX9XVvo9zXVH_wpAGuFJT3u0PFZceB8Csacn2dtA3-qH7ZFuACJVuLriFXvXQ96RYz7JfQtxMX_6npD193P7ycV9VyaFNSkf9wOjE08jLSSvy8X7PKO9_KTYNZYpmZpdbulPbC2vOkUgKW8_0jsTsPqf1nrXhaY0toFpXbWMtMLQsjwka1d_QtWD5VXaygrwuWnqQK6zInxrK1b_er4Tt0WNW5mrF-Ab8YVPbk2p8TsoJrk4-IZ3t3JzPAdYecJ-W4Ln4SH6un5mIDvzWkNz9dL76UJxrdcH4RLH30-7nCah6TrPJqTe8HWf1Ku73cM9h3k8MOIAihvqrZozwoYNajuVt77Wx9A1M3yxphdHB_TrO1e2Ha4CHPhOZ0R2bweSXbdiz99aHExA_MfpCgj_M_IUE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
👑
🇮🇷
ینی بهتر از این خانم بنظرم کسی نمیتونست تمدن کهن ایران رو بیان کنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/106788" target="_blank">📅 09:25 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106787">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7912d30312.mp4?token=jbwWSI824iXneF4wGmmXHmrDM9OyI_FDQ0UUGE9A3qOMkOXYiq9Bi4hMawcrYsk4gh_Wlzg4BQ_0F9X3PmO8QUZgYvFeRIYO185hOwctrcyVRbqbIbSu2NVbNy0SZSLFDAvVjeomT33Wkgh5EORdpNlf68CrZEvYFWK7ax2Hoht6yc-ajpi3X9AMtc4xt82g3xblltBe61F7pA2tB3_DpHK0vR34q7wWwvz6zvWkQ3OZm3s0R4JJagMqNqE6NiuX3IPEfciH78cMvZSwe5Y63E3KuIOFKYsIrn87zi_D6K4n283GQv2JfpCW19605jatMDPDtIobFL_YC97652Yyb4MJXzSVlDkiRJ-_1ELd_0qszcAtAvlBIo61kfhbZa_qATzTQKABi0Dh1_RZOAaG8AbB8njbPKrxvg1TG8BG3cshgh7EvgmJb0pbD8Kxp6JdicX2I7dK6_W7ao7iowySSPgmfdsjwD8ocmYzSphnTOYhgBCrzaTZSxU-SVsnVZeOCcRixMB38JtY9_dHrqkisb5wY68hdLa9qAqluKCshW4WoMP1Cof-h6Gk9gSAj4g0cXNB-CugkxKstCe48bSebXdU32nTvO--tweBBg2NJL-vrMsBr7OnCXPI_bNqxcejZ_7yYcG8yVHm-S8-dleDyn-sg9jhayb8QrjSWxN8Pqo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7912d30312.mp4?token=jbwWSI824iXneF4wGmmXHmrDM9OyI_FDQ0UUGE9A3qOMkOXYiq9Bi4hMawcrYsk4gh_Wlzg4BQ_0F9X3PmO8QUZgYvFeRIYO185hOwctrcyVRbqbIbSu2NVbNy0SZSLFDAvVjeomT33Wkgh5EORdpNlf68CrZEvYFWK7ax2Hoht6yc-ajpi3X9AMtc4xt82g3xblltBe61F7pA2tB3_DpHK0vR34q7wWwvz6zvWkQ3OZm3s0R4JJagMqNqE6NiuX3IPEfciH78cMvZSwe5Y63E3KuIOFKYsIrn87zi_D6K4n283GQv2JfpCW19605jatMDPDtIobFL_YC97652Yyb4MJXzSVlDkiRJ-_1ELd_0qszcAtAvlBIo61kfhbZa_qATzTQKABi0Dh1_RZOAaG8AbB8njbPKrxvg1TG8BG3cshgh7EvgmJb0pbD8Kxp6JdicX2I7dK6_W7ao7iowySSPgmfdsjwD8ocmYzSphnTOYhgBCrzaTZSxU-SVsnVZeOCcRixMB38JtY9_dHrqkisb5wY68hdLa9qAqluKCshW4WoMP1Cof-h6Gk9gSAj4g0cXNB-CugkxKstCe48bSebXdU32nTvO--tweBBg2NJL-vrMsBr7OnCXPI_bNqxcejZ_7yYcG8yVHm-S8-dleDyn-sg9jhayb8QrjSWxN8Pqo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
👍
صحبت جالب رسول‌مجیدی درباره تواضع رودری ستاره بارسا در دلجویی از والنسیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/106787" target="_blank">📅 09:02 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106784">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KDBLfslpBg3l4NU6XXjUOcGZ9EZTuX7yBVF1XFyrgdB2KVSBvydOEcLSoASQcTmcK9z3P3RnfUbSMtIkCuq9H3tiWk7wXJ-8SGiydV0f_Z7Wffjv7NUwTps1X3eZ_4ZWdsa4-q7zLUYti5LhatulNBkVeEm6kGpOJ49kbe9PD0U8KQjxMUZn74_8x1UaoNmyUii4Ja07I6WqzSoVL9YBNcPEJ-9Abt2EJlkdKAFmlwMGaUqWMjOBIkgIxKfre3A7J-6-HcrTmLotCWq_te8PApKU0GoUsGzcKeD4fCYHSHhsITfKlteiyjqde36PQSCQoFLb09tF7bWtKkYqX971UQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
📊
🇪🇺
نتایج هفته اول لیگ اروپا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/106784" target="_blank">📅 00:34 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106783">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea7884a87d.mp4?token=Pd9QBzRU2MEw8SGXTSYXzowfrhuAk9BzgTVqUlEeMwDdYW55kLEWyxWYC5-NbG01_wPZMIcI40aJDP8eJrUNULKrgY9mWGiqWAgU4HzvVjla_AtXXhDePHTwPvdTlmLiHmg7aq7Smd2bICS1gyJKeqArI2uVEBRmUwdWH9Dz_VSTXTfE8lV8nU8LZufp6u1pPgjAr8-J0XNnw2COUJ__3z_d7FAxIVKo038on9yOcJBURIeaun6j99cZ2qSqSY3eA8y8-olD6NmPnxlDri-Kst0uTXqHjd-QSHWiqgYAOGLOi0ndWwCgFHOMGcFdcJUiLneQXZoXFko_hxeCy0lpRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea7884a87d.mp4?token=Pd9QBzRU2MEw8SGXTSYXzowfrhuAk9BzgTVqUlEeMwDdYW55kLEWyxWYC5-NbG01_wPZMIcI40aJDP8eJrUNULKrgY9mWGiqWAgU4HzvVjla_AtXXhDePHTwPvdTlmLiHmg7aq7Smd2bICS1gyJKeqArI2uVEBRmUwdWH9Dz_VSTXTfE8lV8nU8LZufp6u1pPgjAr8-J0XNnw2COUJ__3z_d7FAxIVKo038on9yOcJBURIeaun6j99cZ2qSqSY3eA8y8-olD6NmPnxlDri-Kst0uTXqHjd-QSHWiqgYAOGLOi0ndWwCgFHOMGcFdcJUiLneQXZoXFko_hxeCy0lpRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
🇺🇸
ادعای هومن افاضلی: ایران در آمریکا از ورزشگاه آزادی هم محبوب تر بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/106783" target="_blank">📅 00:22 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106782">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RmfvgWUZZS7G8nBecL6H1BM6yRdcC-YmCTnXaxxeJWYz-YQmaKYG2ApTpGiJ1hV7yUoMxcP7SlW4igVr-ToI5z43u-mgGYI2xYPlvEwX8XR8IGNfEN7OhGUZGVpiM8b6B5MKMUf9lI-Aq7nPqgXOrKnqjfQ946soqW9t3nnnTwovoQzOs1XA-lPFk4OfZESyiMhstKg2lpthQLX4oCNbx02oMMCWww4mVxJ5FjWLCZ7IgsktCxiSvDn5ujrzIvduTHZm0jCCzglA6udX1RoGTf_nf4BZomv-s9LlIxRTJp-fMRtQSjFCW45TMi8piNXiUd6CuYFMYcSyDLURM6deNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
جام‌اتحادیه انگلیس؛ سیتیزن‌ها در یک بازی درخشان و با گل‌های بازیکنان ذخیره خود مقابل نوریچ پیروز شدند
منچسترسیتی
😄
-
😏
نوریچ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/106782" target="_blank">📅 23:50 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106781">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FK9g0R6lo9f0EFm8ruYA02tfj0kKGkqyBaAQRbw_HeHfdau4wFhjZvesPoCk4zd84JE3r7H7niYN5sNVfNAfd4-TEwiJpK9fD1ymdn_qHi7mYv_JnbfLJliH_hVuOucS848U1b7GbsuambC1m428drHkFOTVVJf4uqzl-7SSHHXqIeGXD5Omir8FRNbgQs-A4NOeHEiauyirvwR0Vg5aXXBwxFmzg3qe9SNOCn2RpUNokWgzK_TbukERschTrH08Lv1AczH6vPn92j9VHMVFyLyNAoLuEEciNw7nuTwWshYkeyeciuKojDDvP_tWfvSVK2NqxGT5eaKjhqBlszWhWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
وقتی لیونل مسی در سال ۲۰۲۳ به اینتر میامی پیوست، این تیم در قعر کنفرانس شرق MLS قرار داشت و تا اون لحظه هیچ جام رسمی‌ای در تاریخش نگرفته بود.
✅
مسی پس از ۱۱۵ بازی، به ۱۰۰ گل با پیراهن اینتر میامی رسید و این تیم را به چهارمین جام تاریخش از زمان حضور خودش رساند.
🐐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/106781" target="_blank">📅 23:27 · 26 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
