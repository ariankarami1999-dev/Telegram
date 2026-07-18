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
<img src="https://cdn4.telesco.pe/file/Sj_AD5fqWsUfV7kg6KEA1B7cVyu8TYJ1u2kzHAU9h8ok4dRLkLTBW05a0r5ogGRzP_aZpEpDGK74TpFvjoHxrUHwUulemIxpci3uQ-b7uIX_1VerRCoaeCw1C-m0FSby-sld5P8ugtBMSRygfovWr8oqNGcx2DGL66u_P0rUSUxN2CrK3Hu9OcYxocAeXVNXQiwpEP0b060Ri6RGLCDXFyKy-FZAufaGhygqcaJA7cbOGEjYFxzx3uJveC40SuqLctIiCsepB7CqKHOdPykp_-4ebG3QV6kaxr4PFQ0bKdj8DsWvpjF3IA5N1DW-2CRd5bKkyKQZ-q6OrIXKkdhEJg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 521K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-28 02:09:42</div>
<hr>

<div class="tg-post" id="msg-26036">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b8dc0f4db.mp4?token=nxkTjt3JSyAt2-9uJ_vGLOZUPfNIeAhs8PflaX9-CFn1wG84NDs8LrDlGF9LI_Vcl8RO5cPPFNuxiQkq4Alsgz6Kv2WlPMSSAafoPJG_6GmVKeQ1gCjbyRCa3hIazflTnqM8-sOAQ2TCUxeCCvThaDp66rQxaea79PTMHdUwTP4PDW1b3sgJMdOLR-ltjgjtDdaF0cENw_a9nx3tqm8_IytLNvsTKm1e358zH8rZxfbixLhwvGDdiK4q2LIqckx9bsshsbMpPah78ubVZZ7Au9k71yR7FmAitSBTwemrt_oHgxGzSvMBulXAnL0ksNSIIzUBszbWTQaz0qOmNURjbr1s8rhls5qFtju2RZq33TDhZTEK-CNxSPE5SS2y1iaV2Jn--xJDVbaxc1S9-9Ab65wXDHwrM5CX4gQehx5Eq1_y7BiiSzd3CcBBS0uKciknd_JY0S_Cy78P5Aqn591XG1_dGkiiZ04ElThGzb4wzveK_4PFoywGNpt7Cmp7OyM-TiQMcq2Rw9uIjwTyEIVL7l51XgaTYXoMVn4Vj3MAqdAanfRuhRZ6dJErpVVBRiLryQGs8GRVJ3njy_G3nAnhI96IudS8M8H5SpDPmTJQlaMhudPsLUqwL3D0LjYBe5neGR7PIzMlwYPEHhZtyxetVEgAmp0gBSRfBhx0EhhPBA0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b8dc0f4db.mp4?token=nxkTjt3JSyAt2-9uJ_vGLOZUPfNIeAhs8PflaX9-CFn1wG84NDs8LrDlGF9LI_Vcl8RO5cPPFNuxiQkq4Alsgz6Kv2WlPMSSAafoPJG_6GmVKeQ1gCjbyRCa3hIazflTnqM8-sOAQ2TCUxeCCvThaDp66rQxaea79PTMHdUwTP4PDW1b3sgJMdOLR-ltjgjtDdaF0cENw_a9nx3tqm8_IytLNvsTKm1e358zH8rZxfbixLhwvGDdiK4q2LIqckx9bsshsbMpPah78ubVZZ7Au9k71yR7FmAitSBTwemrt_oHgxGzSvMBulXAnL0ksNSIIzUBszbWTQaz0qOmNURjbr1s8rhls5qFtju2RZq33TDhZTEK-CNxSPE5SS2y1iaV2Jn--xJDVbaxc1S9-9Ab65wXDHwrM5CX4gQehx5Eq1_y7BiiSzd3CcBBS0uKciknd_JY0S_Cy78P5Aqn591XG1_dGkiiZ04ElThGzb4wzveK_4PFoywGNpt7Cmp7OyM-TiQMcq2Rw9uIjwTyEIVL7l51XgaTYXoMVn4Vj3MAqdAanfRuhRZ6dJErpVVBRiLryQGs8GRVJ3njy_G3nAnhI96IudS8M8H5SpDPmTJQlaMhudPsLUqwL3D0LjYBe5neGR7PIzMlwYPEHhZtyxetVEgAmp0gBSRfBhx0EhhPBA0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
روایت عجیب و غریل میلا مردمی بلاگر ایلامی از افتادنش از روی صخره بخاطر یک تبلیغ کلینیک.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/persiana_Soccer/26036" target="_blank">📅 01:29 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26034">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf49687f0b.mp4?token=r95dhP_T6j6-e0Z2csynEm4Q9wlzge9DUBfWgStJruoFSXy-aLf5ke0dB8nY5QvjL_kGTQsZD4Xh-ulf7G3MopozgC5q4u3ghWSHqQ29YNm9H9qIZR1P4EKsGKtI0-_opA49W8na8T65Mu46u6ESXNcEKymhKWtmfmF6o2U7fFuDQaRNrIOeQsNQiOd-30V7c37ZNdddT-7azOwXUu614S86qjrrFrWTPejTOwIwQE0Q78OfDaYMj6hqH2F_13H9bHMkceC5LpcGWdkQHAtVsi7JWcJsXuTX96xeGgswdSOJq9n6CwqguAD1e8AAiG9WiNj20PT-mW9VeFT7hXl8Lg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf49687f0b.mp4?token=r95dhP_T6j6-e0Z2csynEm4Q9wlzge9DUBfWgStJruoFSXy-aLf5ke0dB8nY5QvjL_kGTQsZD4Xh-ulf7G3MopozgC5q4u3ghWSHqQ29YNm9H9qIZR1P4EKsGKtI0-_opA49W8na8T65Mu46u6ESXNcEKymhKWtmfmF6o2U7fFuDQaRNrIOeQsNQiOd-30V7c37ZNdddT-7azOwXUu614S86qjrrFrWTPejTOwIwQE0Q78OfDaYMj6hqH2F_13H9bHMkceC5LpcGWdkQHAtVsi7JWcJsXuTX96xeGgswdSOJq9n6CwqguAD1e8AAiG9WiNj20PT-mW9VeFT7hXl8Lg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇹
🎙
علاقه‌ شدید‌ جواد کاظمیان به مونیکا بلوچی ایتالیایی در گفتگو با ابوطالب: خیلی دوسش دارم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/persiana_Soccer/26034" target="_blank">📅 01:28 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26033">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b649a7091.mp4?token=sRyxfvaK1Ua-OABJsjTPHIrrMIpN6YbsCXNpbA_9AAx1aSkTAiKqXTSxIIddnTY9ad6ay4D7Yw3xNUsdwSRb5IL44s3gTNYHSmf74EpMJ53l5P_SgVJ2xEWLMZXPu6ic-YBiEFoQEkEU6y-LNLfIbFPEo1APysXUvZ-1qNwOwHqwie3Jio5RFtY3yan5MvxvYTb1l87hjPuUW4aU3oqoA2VIy3rhCXasDYyFJGW5CPx6LAD7YXV26ve2SJNILwLdHfOrjTnPMoChEnB6a0inwPG-sf6bOr9acsZbnYyZan3RU67byw7fR85WX5MKtTMr9CTF6DiXJR-_918BDL_D7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b649a7091.mp4?token=sRyxfvaK1Ua-OABJsjTPHIrrMIpN6YbsCXNpbA_9AAx1aSkTAiKqXTSxIIddnTY9ad6ay4D7Yw3xNUsdwSRb5IL44s3gTNYHSmf74EpMJ53l5P_SgVJ2xEWLMZXPu6ic-YBiEFoQEkEU6y-LNLfIbFPEo1APysXUvZ-1qNwOwHqwie3Jio5RFtY3yan5MvxvYTb1l87hjPuUW4aU3oqoA2VIy3rhCXasDYyFJGW5CPx6LAD7YXV26ve2SJNILwLdHfOrjTnPMoChEnB6a0inwPG-sf6bOr9acsZbnYyZan3RU67byw7fR85WX5MKtTMr9CTF6DiXJR-_918BDL_D7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یادی کنیم از دست دادن فرصت طلایی توسط گاوی؛
سه سال پیش شاهزاده اسپانیا لئونور ۱۷ ساله به بازیکن جوان‌تیم‌بارسلونا «گاوی» علاقه‌مند شد به طوری‌که همه عکس‌های گاوی رو داخل پیج اینستا و توییتر خودش پست‌کرد و ابراز علاقه نشون داد؛ بعد مدت‌ها به گاوی پیشنهادداد اما گاوی در کمال تعجب قبول نکرد و گفت تنها عشق فعلی من بازی فوتباله!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/persiana_Soccer/26033" target="_blank">📅 01:27 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26032">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rFoWesS3FfKvN9PtmV4FBgzLhR5tV6nn_kMrNHwWGe7ZnegEKG1Fj0DxE7_qs-_R8XOQv4hNrWQn-IaD2bx9-n3y7GEzBDUEYAyetC3-fEQ5mKpBdGGwj28CgXzsREiniywKJw53xIcyGyJ2szYe9hKnBRRq0mkleMqOsnZF2kLS8sIjGaiR1f4lIy8r2a1wfZ8y4fUtLAJIgo3XWxPjTp7wTqy-9XvW-V71wqarEFV0HHyfRIC7ZCF2wi_qwSGyln25I4Yo-23zZCrBDRF0D_wxzQffBlZVHm8J35YmWQ9b23Lhr48HVUVWGVKF4KadGKhpmIVu2GsPF4I7oXxrNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک‌کنم‌اگه‌هرشب‌با ۱۰۰ هزار تومن میومدین چنل بت ماشبی‌بالای ۲ میلیون سود کرده بودین مثل دیشب:)
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FuckBet
@FuckBet
@FuckBet
@FuckBet
@FuckBet
@FuckBet</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/persiana_Soccer/26032" target="_blank">📅 01:27 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26031">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h9WDrmxR69nacbZj4X_MX7oY7FMjR8OMYScy3ULJoLavYphkfeW_qPLPe2C7GLsJqgwLuV3VOPh56QY2qH6HaPu3LvIYQkH8b3PADKchLinLOk_DkOTVJK0Jngq12fC1Asrqi8oNNi0dvOzD5jnINGIoS4ybz_e0Tl3ft1MIoRwKI2jux1rr3HIhEvuREB2S7CB7MsYiclWRpPwRRQDnZVOSwR4AGCzV37Nm1wCmQSirIPTtrvFnsybQ7e9Tcei90hwhbAIKYC8EZ9TPBeMYL0mp1r_LzjtVcvfLP-GIoT6MHrwfa9kHCA6-hakmrNJDCi5gYOwPs1Cln-1vjFs5TQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇭🇷
🔴
#تکمیلی؛ رومانو: آلن هلیلوویچ هافبک هجومی 30 ساله کروات در آستانه امضای قرارداد با پرسپولیس قرار دارد و مذاکرات این باشگاه با او در حال نهایی شدنه. هلیلوویچ طی 63 بازی در فورتونا سیتارد آخرین تیم او 6 گل به ثمر رسانده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/persiana_Soccer/26031" target="_blank">📅 00:47 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26029">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/767b719cdd.mp4?token=LuEszKXjVCS-BTjDySMHr0D9Dp8V8NbxDbPm7ZBeVpRGOcbk1Vur84CTS1hX25V4QVW89TyCqGfo1pUDN0O7gi_1v498_XzbvSwJGQeOy4KHjitnBIcB5opZAuyD_zk9rfUrH8XzztiyUtz64XMAN_VUDGqJBAivjFo_J3UZo4KvEfMNZmzPpm8HeRfGx3oeTXdh7OLiEplXeFCMrq3ABUJWvt7YsDHVHC7MiGZaoxr6Qdm0qBBdyXFlFgoA4PRcK4ZJUJdbMG-qyLqUWJQjRhqlnvxNKGHrfDhl_JIiYV4CaxDj5OaJZqfwIeRa6oe-gtrzEznEjgHg6RE7B8K5wg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/767b719cdd.mp4?token=LuEszKXjVCS-BTjDySMHr0D9Dp8V8NbxDbPm7ZBeVpRGOcbk1Vur84CTS1hX25V4QVW89TyCqGfo1pUDN0O7gi_1v498_XzbvSwJGQeOy4KHjitnBIcB5opZAuyD_zk9rfUrH8XzztiyUtz64XMAN_VUDGqJBAivjFo_J3UZo4KvEfMNZmzPpm8HeRfGx3oeTXdh7OLiEplXeFCMrq3ABUJWvt7YsDHVHC7MiGZaoxr6Qdm0qBBdyXFlFgoA4PRcK4ZJUJdbMG-qyLqUWJQjRhqlnvxNKGHrfDhl_JIiYV4CaxDj5OaJZqfwIeRa6oe-gtrzEznEjgHg6RE7B8K5wg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
👤
خاطره علی کریمی هافبک ملی پوش سابق استقلال از اسپانیایی صحبت کردن میلاد محمدی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/persiana_Soccer/26029" target="_blank">📅 00:33 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26028">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kOlq5tuGWCWQABQA-YTDCxSeglP82PztkLFyhxfMOwbN59mmeSZaBBsJZeFU_reBeLH8Ma1vpnzP6ipXKch1vYlNmTV1FrbloFEU777zsQ4_E1apmxRqg-PkwLAQUt10IlHhakHejO4TExlzE3n8aoPQVc0E5udAxiAwf10s9pT4PtHGFBoDX8rHRTZMJDOQUEZ6nbNHM-lYl57YvBukxEK2eJiQNtNIZFdK8RYtnNF8MuOnLNHqb9Aq6abg9tTvCUF92IwzldQSAR_i2al5cqXJVrDDsryF-Ek2dt_d7Qv9yw09ITl3CnunZ_cnYiSbagLJtkzqkuOBxuPEtyOKRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
برنامه‌دیدارهای‌امروز؛
کمتر از 22 ساعت تا نبرد تمام‌ عیار آرژانیتن
🆚
اسپانیا در فینال جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/persiana_Soccer/26028" target="_blank">📅 00:28 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26026">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rm6V6PychbIT_nDrSJR3xAbFfNP_JdjjdbevAvsGjrHb7WsptJnj1dchP7CLGid7WKqTpUx_1BlYjeDDygauidcwBj59b5hb-o2eG5ivhHmsbUOab5t8xgJU5grqGMWAjal4Aq9_8vURmwD1L8iH-dqAimdeBh4v3DGJvLsgZqr_5U2iUkWgbcGyOxovPnpQmnR-bQLGfgu6csFbJRowxA-6tI5sBgP7oz0Movt-bgm0ZKEXChwvdwRN6Ww6QXUR-cg6pL1Pq7-YaZwZBOSG4aBZlXnLhiVW8gn-UmkwKVl1m-SSRIXlL_agEotGqpBE51oSM_FR7hw8TnLiAxK58A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه پرسپولیس امروز صبح با سامان قدوس ستاره تیم ملی و مدیربرنامه‌های این بازیکن جلسه‌ای دو ساعته به شکل ویدیو کال داشته و به این بازیکن اعلام کرده علاوه بر پرداخت مبلغ رضایت نامه حاضره قراردادی سه ساله با رقم بالا با قدوس امضا…</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/persiana_Soccer/26026" target="_blank">📅 00:23 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26025">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fGjHEXzYez31LfZLWxXu5korvtDMCDNDM1fvMmu3ncvjHg_tjyKGAWkSX54zQtGizfN8-PHe3w5n6440zGAiE7bqYsedX32_7Tbl7UTUw1TOwwId4VtOdXP1VUihl6OEFMil1Lxqi7Oi7f_EaUXBNcGVMwOrq_INy-ya_StOmvf7VNt8R5GpeNvwS88pkvtzuFYZ-bUm8PyxQHXaQvGRmEn4rrGFTv1OBRnZ7QgT0-6GNeA8tf4zR0EMW9dnYRyZo-r0fXihQctJZmjayiPc7Zi2MMx4QDPmyDYNOwMRUztqp6TWn6lvUnJX3R-NDmP1dhPij7jYmyVyAimRbL3y_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه استقلال موافقت کامل خود را با افزایش 300 هزار دلاری رقم‌قرارداد یاسر آسانی اعلام کرده و به مدیر برنامه های این بازیکن گفته که یاسر آسانی به ایران برگردد قراردادش رو سه ساله تمدید خواهیم کرد و پیش پرداختی یک میلیون دلار به…</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/persiana_Soccer/26025" target="_blank">📅 00:13 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26024">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ae80f717c.mp4?token=L6cejANz_3SrtkwikIleMLtHmkd-W0N-_pVN6KoK9PlGMfUk80y0qs7jbjN0APVHDLh0EjBai6k2RdQX-YuY_lMpNZO385HzQukN1ihfL26jZ7zlvqGjtZ8RX6WwRa_Z5pa81M1srU_7HcQCH5mgSF0AUji2sxZIoMpxGK1VnvNZElVg_mteihYHPS7rEpkEUQnCkZQAcvfhVzI3pY1Em1ve7La63f3mWkw9IKBvvuQADuVQt4cirHaaIhdacfSbqpiCqptZ5Fv4w9bCp8IV2sIPOfcOTRGngH7mKrIWyHYRBg_jwUotKhppDjGVjW962FutEO7YYAIdjc_7OzwImA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ae80f717c.mp4?token=L6cejANz_3SrtkwikIleMLtHmkd-W0N-_pVN6KoK9PlGMfUk80y0qs7jbjN0APVHDLh0EjBai6k2RdQX-YuY_lMpNZO385HzQukN1ihfL26jZ7zlvqGjtZ8RX6WwRa_Z5pa81M1srU_7HcQCH5mgSF0AUji2sxZIoMpxGK1VnvNZElVg_mteihYHPS7rEpkEUQnCkZQAcvfhVzI3pY1Em1ve7La63f3mWkw9IKBvvuQADuVQt4cirHaaIhdacfSbqpiCqptZ5Fv4w9bCp8IV2sIPOfcOTRGngH7mKrIWyHYRBg_jwUotKhppDjGVjW962FutEO7YYAIdjc_7OzwImA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
ابوطالب‌حسینی امشب دربرنامه‌اش و در گفتگو باجوادکاظمیان ازجدایی‌اش از اکیپ عادل فردوسی پور خبر داد و گفت جدایی ما کاملا دوستانه بوده و ممکنه بزودی به اکیپ ایشون در پلتفرم ۳۶۰ برگردم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/persiana_Soccer/26024" target="_blank">📅 23:59 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26023">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69396b76bf.mp4?token=kmCwpu7bjjUZCTLtO5mmMkW8Su4hFX7u2rx420C-q2aDC8sSQKbfEfNOVEKAwMUf7brqO269DbcnXwel6Ie6AdjQe7aLNzXy7Mq4QbU-jE3z-cSfquwneB4KaIHC9zK2zReU9yjuh8BhzFWYbpT3LnGz-yEth5ScJEQBcy-ORuhi6fmNBCeu6q5n3q8PpZkriB_ylWpDnwB-oaOWwI14chDA2b-PnlvIlaaMD-u4VFsa37B44N2fZbXYouxCTUbyTeD0CjmR0rieecoTTv_c67hbqP8w587-OL7Gez6qG1Ex6oMAdYbK9vzQpJ-eZfANVibtdZ52Qbv5cp_eVQW-tA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69396b76bf.mp4?token=kmCwpu7bjjUZCTLtO5mmMkW8Su4hFX7u2rx420C-q2aDC8sSQKbfEfNOVEKAwMUf7brqO269DbcnXwel6Ie6AdjQe7aLNzXy7Mq4QbU-jE3z-cSfquwneB4KaIHC9zK2zReU9yjuh8BhzFWYbpT3LnGz-yEth5ScJEQBcy-ORuhi6fmNBCeu6q5n3q8PpZkriB_ylWpDnwB-oaOWwI14chDA2b-PnlvIlaaMD-u4VFsa37B44N2fZbXYouxCTUbyTeD0CjmR0rieecoTTv_c67hbqP8w587-OL7Gez6qG1Ex6oMAdYbK9vzQpJ-eZfANVibtdZ52Qbv5cp_eVQW-tA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خب‌شروع‌شد؛ جواد کاظمیان با انتشار این استوری و تگ کردن مونیکا بلوچی تولد او رو تبریک گفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/persiana_Soccer/26023" target="_blank">📅 23:41 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26022">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mBvQZHhpIs4uCpV0NG1aaYXoj34h1Oa2uR7odFjXJr6cbBAxMuXCP42hulwvwseEq1ONhaHYm66fOiJTiBylXmhbjbjmyXf9uOvbEQ50LuB43oIAId7cxumvNZpsazVuD28DP8439Q-2CoSXXSVllPb3weW4iz6ED2VfY5qxkkptpKeKqeKZs79xN4BWudPYrTCr2Ku4WVS1UBqd8bHGDXePwXTDkYaTZJslHblb-Ivg71fClno7lz6KynV9oSNACLnxK_1uqArR1oTp3CPqg3_I-QlnIn7nbajh29fb3_74rx2d-dHWft7TEBBzlMqGqal5kJnAOdYez-lUPK7gsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
🏆
باشگاه اتلتیکومادریداسپانیا برای دومین بار متوالی بیشترین‌تعدادنماینده را در فینال جام جهانی دارد: فینال‌سال2018: 4 بازیکن؛ فینال سال 2022: 4 بازیکن؛ فینال سال 2026: 9 بازیکن
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/persiana_Soccer/26022" target="_blank">📅 23:30 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26020">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/inyKQZuEUhbu8l5OFxJhv4NMMs-iGCsuQwKveaai6G7ro6woVfnlKoN1xqBO0aC86ZUZBePdXrja-BxcfwiK89fm6MypHK3Aqr3DiFMprJ18qvG0zfkVj-vgmhyzkouk5-H8pCDmE2-3mftuPhoEnCmu9pacCRkBel-iMr_hXCma-psC-HN6tRGywRihe0tF6bZXukrHtR2zpJx0Yrsvn-b0Jq5dYc9KIiMMLhySLMFJObNeM_dQqTj7OnzfdpEpwn-q0TvUq3uBn-654LxIBZYQAr1nKg16gzvSDFz5laLSXL79X4XAI1xBynL45NX06px3N5n255yCp9AepRn7ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vPDoVepCH5D6raLO2t6xl-2iRabgrEizUGNAH57BXL_9J3m9HXzmh8C5uhVNkFb_Ve7rhlEvAv2zEIeeavb-MEiE8SrlrQMq8GA6jYaVNMcZak6_C04aUt4NDd5H5KQ1jBAp6d_3W6kXmQY8M0HKa1ZA55Y7YfwGpsEnMXq4kAyLgWbENqxdad1rrXoPHcLRyjta2XkZozUk_Kv2LqCQUlr_UBgE-VxoHnAcow_HtPIZIUmeJVYnzrE_4lxT7U68Eq7ObrkLxVuBXhIPYwhUtl0AVwVT2mVIqg0TpeZYi5kLcVetx7HC4IvCowR8-_bec13HBu6nwyR3-zcDuRWoKg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
مسابقه‌رده‌بندی‌ جام‌جهانی 2026
؛ شماتیک ترکیب دوتیم انگلیس
🆚
فرانسه؛ ساعت 00:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/persiana_Soccer/26020" target="_blank">📅 23:13 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26019">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fOEF_WNIFgF6s1CCzrLPneHV5eI34gKV5h256svvTw51QCf-_xo7ABZ_tbLplMvoNVWq_4lK_wPSKzK8OLB78MYTo68BZqlNojxgJtP3lPC8u88XzEMWDxuAiblQ_5dfWPpDFb2FtSREHO5RS3_npIdWLjX0lGKs9Ps_ieQNOW5lSlCCTl7t1edc905hYoQ_CP3GYy4jC3OlO8Ct2_iOq5BMzYXh_dpwJ7VGqJwrP4wo012kaIyjMJeiBaBi4Vqt7swddGwN4xPEG3so5oN0s629skW_Jhz-z0sJQ0qx3cQFRXwowfxZRAp4liA9yHv8MFqUvQiH04PRNoxU-fJvsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه استقلال موافقت کامل خود را با افزایش 300 هزار دلاری رقم‌قرارداد یاسر آسانی اعلام کرده و به مدیر برنامه های این بازیکن گفته که یاسر آسانی به ایران برگردد قراردادش رو سه ساله تمدید خواهیم کرد و پیش پرداختی یک میلیون دلار به…</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/persiana_Soccer/26019" target="_blank">📅 23:04 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26018">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KHOx6IqdSvwFnqIgRbTzFU9pUYQce6kTrEYU4ICns6IcVMx_42blNdiBhi0rdgyhtnx9Ma2HUMgncvfQ_txfwj27ZUBnp9V37He9HnNZMC8txUZBqNAHWpEFX5schFD_BsRnJkS4XW7UnYdjrHK_EIMtdAE6zT355rr7AH76HiP2oRzY8bvOH50rmz_HWv3ocakOEDPBdhffBaPxGBah_fAUmYZq9vwHk5kJ1gPkRqAqeMucAfaqEyjrcIdjt7-eOpiC5dqR4CB93ouDiSZu6ENqTXG3NUaPpEKjul2EOopYrcg3Tj-sw-nVbgyvihc-DyyvZfYt6RPvnZuT2MTXvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇭🇷
🔴
#تکمیلی؛ رومانو: آلن هلیلوویچ هافبک هجومی 30 ساله کروات در آستانه امضای قرارداد با پرسپولیس قرار دارد و مذاکرات این باشگاه با او در حال نهایی شدنه. هلیلوویچ طی 63 بازی در فورتونا سیتارد آخرین تیم او 6 گل به ثمر رسانده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/persiana_Soccer/26018" target="_blank">📅 23:04 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26017">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qo-Qbn6AlUN-qRDKM8G8Mf4h9MZ-s5sFu6mJdgOprYRLd2PLw4QER6sKjLzop_w21feKIW559xLh7AnLFEkzrn0CoHmiGb7MUoo2mbTf-y7bcdgUSLY9_NTqtfaCUAL5AmLBTFqvN72vO1Kmy68b_-TzyLqwUQd8SGyXueFHkV46KfmUTLpThSPxRcp_ZSxkMNtOeDxRLnzlFzI-VC6eWgfLyH--x-4Hu1EZJ9gHRu0NYJj43ea7ugwry1Trs1HHpDGO4Y9e4BgKqETVDipnen0PCRyfp7a39Y_Uvbob8N4-ccMaCNmBoE2sm3OD06mFe1zmpXKeQaumygMKAfWh8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
۵۰۰ دلار جایزه + ۱ گیگ اینترنت برای هر برنده!
🎁
🇫🇷
فرانسه
🆚
🇬🇧
انگلیس
🔥
دیدار رده‌بندی جام جهانی ۲۰۲۶
🏆
نتیجه را درست پیش‌بینی کن؛
۵۰۰ دلار جایزه
بین تمام برندگان تقسیم می‌شود و
هر برنده ۱ گیگ اینترنت یک‌ماهه
نیز دریافت می‌کند.
⏳
فقط تا قبل از شروع مسابقه فرصت ثبت پیش‌بینی داری!
👇
همین حالا وارد بات شو و پیش‌بینی‌ات را ثبت کن:
https://t.me/betegram_bot?start=p9_r4EF37DCE
جایزه نقدی مطابق قوانین سایت به‌صورت
FreeBet
پرداخت می‌شود.</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/persiana_Soccer/26017" target="_blank">📅 23:04 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26016">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🇪🇸
🔴
هایلایتی‌از عمکرد آلن‌هلیلوویچ ستاره سابق بارسلونا که در آستانه عقد قرار داد با پرسپولیسه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/26016" target="_blank">📅 22:56 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26015">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zej6_G8j_9ma7AypN3wRwd3Q839WHdOvjCoEeO-R3Yxs9bNKHjEjju_2QjA3iuII6jdECfKrIEoXsjc1lLcBzJeBWYB4jpXw-D-mZ21RSmuzlPO6gCWwjdUOMyCtLGVRdB__Ok35kwYgyE-XxSF8Q8WGDThtfhcE1hMUxLmv6LQIJy1c9LqSq7T9S4j1ORIY4bGm6zXEzMufwU_WN4obw3EljV227h7tCQTKIrD_zm5omEJL87sm6QJ_fDXDZpBcm_H7dihYnKZA8cpWy-mMURZMTVcKP5h8VvEw6yYssu5R_XIsQANjzvSlHnRULfdqkZQk6U0jOgG8LzagAVWbGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛طبق‌اخباردریافتی رسانه پرشیانا؛ باشگاه‌پرسپولیس به‌درخواست شخص مهدی تارتار با یک‌مهاجم‌کرواسی که سابقه بازی در تیم‌های ملی پایه این کشور درکارنامه‌خود داره وارد مذاکره شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/persiana_Soccer/26015" target="_blank">📅 22:49 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26014">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/boZ6uFV8INrqZVFjW2xAYSuUed2dSGEnhH19YjBxGd_6QKQ677vmWzapDl82HKeVyrVB1x4cV1HfzYiqBzIMTeXhUpDw7L4YD5Gq8rupdEYYU22q2HLVnzQT9qXvyV3hFVgJHc8bwHUATWXKUEx2CKg7az6eo1zdqzL2oouwMSHoUtuAG8vpogUhBU7i_7wsxR4Hr1jshcBjVNi-5I0IebsZSg7ZEHkD952Nt-yAo6eYgabxjtmb_F_9iskxspw_RMlV69BICpwojL7lTsqavp4F1EiSoK3CEGhHBX8z-dfnBAa7j82c18b9pSlk35j2SfcoowYbexsRVUKSPnmj3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
جان تری اسطوره باشگاه چلسی انگلیس:
این سوال رو از من می‌پرسن که چطور می‌شه مسی رو متوقف‌کرد؟جوابش‌اینه:هیچجوره نمی‌شه! حتی اگه بخوای با بازی فیزیکی جلوش رو بگیری، فقط باعث بهتر شدن اون می‌شی. مسی فوق‌العاده قدرتمنده، از جنگیدن لذت می‌بره و واقعاً هر چی که فکرشو کنید داره. به نظر من که اون بهترین بازیکن تاریخه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/persiana_Soccer/26014" target="_blank">📅 22:31 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26013">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d9c8adea2.mp4?token=G15RIk4ganAoOdOcf2xDY-5co2Nfr61vg2EvO03ODhYJIvl8OCxt2-ryAFBs96dm_4jNcHB-4EjCMq8LfqG5tCuNPQjpbMlcp7YjLQnqOOLRZr4qfnNnowbdn0_NLLbU_OBvoH4mfEfuE6Fc_CKTDQC2LHiWXegSHQMT8G7qjm8Qw7Rp1gd4ozHuRCov7d77aLoM-C27j2z96nFlwhchNwGg8SsGoxhnmg1tpFrXiWYcv5rttiuizr7eAcVhtifBnF85hnJ3c3MjWfjPR2GsV1s60yITZ1Upq7YF1_lVZUbQv270vKgLezoKCk-sahmWSi7MZRG1QF8o-AOavQnJ_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d9c8adea2.mp4?token=G15RIk4ganAoOdOcf2xDY-5co2Nfr61vg2EvO03ODhYJIvl8OCxt2-ryAFBs96dm_4jNcHB-4EjCMq8LfqG5tCuNPQjpbMlcp7YjLQnqOOLRZr4qfnNnowbdn0_NLLbU_OBvoH4mfEfuE6Fc_CKTDQC2LHiWXegSHQMT8G7qjm8Qw7Rp1gd4ozHuRCov7d77aLoM-C27j2z96nFlwhchNwGg8SsGoxhnmg1tpFrXiWYcv5rttiuizr7eAcVhtifBnF85hnJ3c3MjWfjPR2GsV1s60yITZ1Upq7YF1_lVZUbQv270vKgLezoKCk-sahmWSi7MZRG1QF8o-AOavQnJ_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
👤
خاطره علی کریمی هافبک ملی پوش سابق استقلال از اسپانیایی صحبت کردن میلاد محمدی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/persiana_Soccer/26013" target="_blank">📅 22:11 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26012">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NNa-DZyhdu0zjaloaIhJVHNEkXK089UATrl5XA7xTLejZeLdB2lvpN6EH--EMB5_0sk4FVzLS1Qh2pUZfsUzlyEYe9yQrYiwpMWvcxXjyFLM4GxwtMOmkBY3YpE5D0limTeUYWQyQ7g3icPYJ-24CmRq4BhDyx3DIa11fy_C1S1n_1fvHtEOkZ638SnNvVScPjeDDvg88xL6H-zcP1WoRKdX8oOTsxcGz4TuYDFgwNf2M7alF59XRMz0Z2xTDcreMwS1qGviw1r_efgPaQVp7bkXjavT5gUp-6aZNSDhgbPV_xvLc-Bxj-usoEfO7WIT-P49yOA_TSYAQOLCesww3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
بعداز اورنشتاین؛ رومانو هم تایید کرد؛ مورگان راجرز ستاره آستون ویلا رسما به چلسی پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/persiana_Soccer/26012" target="_blank">📅 22:05 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26011">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FUsD5BhORhVAWqemHOgNJOxVnSpnQ8fsQ9Yca_leShzJx5elYMoY6_0W-s7WJdRnuXdDLPpK4NcGEwgd8oDYzZnlQt-4ohgLMj9-kcwbnYeGMKeRHxr3MlDbO3Tl8BNDoMRfGjnm5YWNDdmCvEb1FruhQjaf4BSWZLcFLcxL5i8RWn80TJG6x7YTRnp5En25DEesoRiH4kg1DnKHvdqqyy86rvyy09KfjXpebyDAaY8yUXs4Q0bNCWTKAgY03_cKJK4-K5NmQ-Kjy6dmWi7Wd6FoFbpMinaVAiSqoRAGHxZSJycNsTC14R4XL5ehGG4yH62Ur47I6EDh9zz-0aoC7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
🟢
#اختصاصی_پرشیانا #فوری؛ مدیریت باشگاه‌سپاهان‌باارسال‌نامه‌ای به‌باشگاه اخمت گروژنی خواستارجذب عثمان اندونگ مدافع‌میانی26ساله این تیم شد. اندونگ دو فصل پیش عملکرد خیره کننده‌ای درگلگهر داشت و با 500k€ به روسی‌ها فروخته شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/persiana_Soccer/26011" target="_blank">📅 21:54 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26010">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MrbU4ft2RZkqOcAxqy64WMqvXMp77LOZ6hZRiOvhJLOwZYpdS5olLAZjXP2IAhYKoT6dDx5MNNyNQTKtSlJOReOvzzSGMuiVuctXawNqM82RfrZbfNt-WU5m-26laUgo1IOcNjPbi7gKseMTSCB3VlxrSg-UBmiD2QEzOZfGEPRLTCeoI2Z5uYE1Fblsl943QRf3PPHrgM3u-rwU8VeXYI0ElC1kkrqjjXth0-ccA6TN7OvV63DTC4Sk37NxhazSrXaNMuLy-m0YfdI7OuV6oZJz5W7cbFEv5ukwFg2qx1MbNPQuye1axSdzgNHly5ZHulk3hrEKELtzXTmtwpZxuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
دیوید اورنشتاین: آرسنال هایجک خورد؛ تیم چلسی با ارائه پیشنهادی 137 میلیون یورویی به آستون ویلا درآستانه عقدقرارداد پنج ساله با مورگان راجرز ستاره ملی پوش این باشگاه قرار گرفته است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/persiana_Soccer/26010" target="_blank">📅 21:44 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26009">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qy4Ae5fCdtjH0GR8iW-pi_VD8T_DJ2jCW0xRvcXEWxHvu5th5YJCaemBRccr_rdLLwJ4S-Z05YyPMrsaQAhaftnBIikzx4wLezJ_LwrFpyeKWB-AuIoR50ADyegC6unuomJiGxh08vU9Bpqtk_eNxoYey12sAi__PVRU3HwWM-VkUJxt8aJUKVr1WMeCiZhOdEnJ5pYUh6IFR2PFFbMW9mUAWUCJqZOpsTfkgfuKwF2amNN83BjkiJjyBTBhYKigZQCzClwDqne8ZnHIfOoGFpIFx38arFFkLxURFNzUwZjVM8XuTFWJ5vblTdMsX2u8BKltDmOt0QnwRuvLPJtxNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
بااعلام رومانو؛ کریستوس زولیس وینگر 24 ساله کلوب بروژ با عقدقراردادی چهار ساله به آرسنال پیوست. زولیس یونانی فصل‌گذشته‌در36 مسابقه 17 گل و 23 پاس گل به ثبت رساند. همچنین توپچی‌ ها بدنبال عقد قرارداد فوری با مورگان راجرز ستاره تیم ملی انگلیسه…</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/persiana_Soccer/26009" target="_blank">📅 21:08 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26008">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3acdc0e3a.mp4?token=nuFIf8QsmjePisUFiPJ0f5o8nyF2SRxhVc8jqSi33vTDJsNZ3-vGF5KNjmF8BoWXGEuzpHL38ud8OiLEf5zsMGp9r3Ve3GLEVXa5TrKtoFKMD4xXixX2qmmSftiIkfnFCQlyQH4vaiJDMihPcvhnCyFbF2xXHT9EXrcTGbqbByyprNXm3YKa6nEq5enBQorx6k0OiGxwSGiji3B6ge3kiZ2rg1S7dCSz_-F670SIzWs-j45Cg8ZVFdlcpYtMyZ7GLgWm6DOmW_ApuTUfJNNvvD96YRv2nlWEjEQRnr2wGc1rhvu1dGBeYEtG6_rhhCYyQFYAgydUxkNgNQGNPlHx_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3acdc0e3a.mp4?token=nuFIf8QsmjePisUFiPJ0f5o8nyF2SRxhVc8jqSi33vTDJsNZ3-vGF5KNjmF8BoWXGEuzpHL38ud8OiLEf5zsMGp9r3Ve3GLEVXa5TrKtoFKMD4xXixX2qmmSftiIkfnFCQlyQH4vaiJDMihPcvhnCyFbF2xXHT9EXrcTGbqbByyprNXm3YKa6nEq5enBQorx6k0OiGxwSGiji3B6ge3kiZ2rg1S7dCSz_-F670SIzWs-j45Cg8ZVFdlcpYtMyZ7GLgWm6DOmW_ApuTUfJNNvvD96YRv2nlWEjEQRnr2wGc1rhvu1dGBeYEtG6_rhhCYyQFYAgydUxkNgNQGNPlHx_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
تو زندگی همه باید مثل علیرضا فغانی باشیم که حتی اگه داور فینال جام جهانی هم نشدیم از تلاش کردن تو زندگی ناامید نشیم. امید کلید پیروزیه‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/persiana_Soccer/26008" target="_blank">📅 20:51 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26007">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cV0bykgMIPge3TPs7ONxHCNsEW59pgU_WnGTk7UpVkf8LGoCPA6au6rQmB5prYXsjzXgREeAgLa3_mlTA18GXPkNwIlriN6JH5A572Id4MRzOSVSxqcIRgmj5BVY5HKvsiGRZ06g1bKEind6h6gyT4scIQjOX5Ux3nB8QPG0SQjr32ALXbEFbrmLfF1NkkwTo0J2-ftr8JeIA1W09zzyj6CoHdihdNDVDUBIxk9BJrWumIJrI-kdwHV6IM1SIyLtCJoyMfT4XYAKvd9CamaOAD7DQ04F4gd4cEq6qkp_m2z-iMxiYtBxUUJm7NAWvckL5FiB7MTzO1mZ-tFt4pu5Iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
◽️
🔴
#تکمیلی #اختصاصی_پرشیانا؛ باشگاه نساجی بعد از جلسه امروز با باشگاه پرسپولیس رقم رضایت‌نامه دانیال ایری مدافع تیم خود را از 190 به 150 میلیاردتومان‌کاهش داده و72ساعت به‌ مدیران پرسپولیس فرصت‌داده تااین‌رقم روپرداخت کنند در غیر این صورت توافقات طرفین بهم…</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/persiana_Soccer/26007" target="_blank">📅 20:31 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26006">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OcMnVf1hDV7EOw8hBpUleVHFmZbYGh77HpPxXTOIjLGSuBNxf_EqQINrmiRsWV9HGwzytAkg3hnV1xCIoEJAnqFHRw6sDQ_AnE_QgZtbB30XzifOXCqh-qvpIavSweUrGhvP-c0_mlmL_pyR399BQlOUzoU0oO602fZoTfM9dIGuWr3OUpRGIXkNd711X5DpSW_BtR-6t47_vIjfi97AYL7IIi2FbJ9dHhT1l_rAYzgyu_wLLJx_4sp37mp3DryTQ1V5ih1UPuBwfzucejMJnsdYjCb5LGTFjiuFSNQz5eu0nOIbw_risM5dMFx1YAXXeCQgetr7QTfJxvZq7XnnnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
راجب خبر حسین نژاد هم‌پرسیدیم گفتن تا شب بهتون خبر میدیم که توافق استقلال با روسا صحت داره یا که خیر. وضعیت جلسه باشگاه پرسپولیس با نساجی برای جذب ایری و طاهری هم مشخص بشه قطعا تو کانال میزنیم. خبر رو بی سر و ته نمیزاریم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/persiana_Soccer/26006" target="_blank">📅 20:16 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26005">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ntVQhJnay-t_biNhDj-9PaycKdk6F8D7zLA9_xr529YRYZ6yf5M6hb3v8BRTyEGwYnMt2onqI3V1vGAUBM-egE-uRctI5iOm3r2TzrTWcLZL8fLvnlbWeDbnL05immLhCjHSjhyVfqcetQdBOhRZp8FUNfNNd_S7XQzyVVWn-5h30SzsfVjbHHcWzAXwbGpKkESl0A1aV2EDTQD6T54HQ9htSEn7__cxaLL498i-BpVxD_YozJCgl3FW4bpPhebUjM6lX88oLPNXwcJFmENf-kqFfRH8XHat5wPD-oquruKR9JqpYKBbBxR87mi1ZhDmtT2nlfLCRMH9SrTSJn1gcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
وزارت‌ارتباطات‌شایعه‌قطع‌اینترنت پس از جام جهانی را تکذیب کرد.
علیرضا عبداللهی‌نژاد»، رئیس مرکز روابط‌عمومی و اطلاع‌رسانی وزارت ارتباطات و فناوری اطلاعات، شایعات مطرح شده در شبکه‌های اجتماعی مبنی بر قطع اینترنت پس از مسابقات جام جهانی را کاملاًبی‌اساس‌دانست. واقعا اونایی همچین شایعاتی پخش میکنن مریضن. سه ماه مردم ما نت نداشتن بسه دیگه کم دهن مردم رو سرویس کنید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/persiana_Soccer/26005" target="_blank">📅 19:26 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26003">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uNbS6FrDAXcvTuzmu8Tydtn4j5FiEyU7nLZUx-KYYNwcbxSJa0UboVHiBk8HnlINK-wBkJY5I8RdRMHrK2H2Vx14EAwCJyirJqU__9yzE4EEzWd7QK9QCLbyLFEbxCAFS7myOTbY6B0DonK2vq4mFF5TiV4HLh5Bg80lbmdsd7bgCTzQPYESo03QzbMshCt_FHHO_QMxLMuheVqfzeeSDY8HDl2jSama5-WTJGPOMG1VClPXlQxWmmEromiyrGOy2OZPPlrmOR0_9FAbyMzIVlzyJTTFpxZFNGGzido_yO973z5ck_hd-7EiICGXB7WvcGY08MQu-neTkqREr-gbhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
آدیداس‌ازاستوک‌های مسی برای فینال جام جهانی رونمایی کرد که روش‌عبارت "آخرین رقص" حک شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/persiana_Soccer/26003" target="_blank">📅 19:07 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26002">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e60998a9e.mp4?token=EAMbJqf3oQ8sMyud_PqagSI86atBqirxrWb-vuKuQ_yIxNyg-0X4x6mYsc6q-Rsf2Epy3HaYzEhJJA-wXZwDTO2BDG4tAEpHBqSkEuxf9NAoJhnEjq3TA7UF00wf6OWKylyZsKjaSKkkZ046L7a-tBnqmi2JehZPm4OGNtelnPyYHl5iwjOPAP_qwcS0Yw0VPOLBDzwu0lz0hHT6HayVO-_VsPfmYBV3AkXtJYTvS5MGAXJBgDNXDDiVlwUm2tw9pq7onUERMX5GHlEVhu4Xi5s18_T4t0n6RXKduLa6_eS8k3NhAE77mzhxF_E0wX4Dnd0RG07qQiDjPW5E3P1bqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e60998a9e.mp4?token=EAMbJqf3oQ8sMyud_PqagSI86atBqirxrWb-vuKuQ_yIxNyg-0X4x6mYsc6q-Rsf2Epy3HaYzEhJJA-wXZwDTO2BDG4tAEpHBqSkEuxf9NAoJhnEjq3TA7UF00wf6OWKylyZsKjaSKkkZ046L7a-tBnqmi2JehZPm4OGNtelnPyYHl5iwjOPAP_qwcS0Yw0VPOLBDzwu0lz0hHT6HayVO-_VsPfmYBV3AkXtJYTvS5MGAXJBgDNXDDiVlwUm2tw9pq7onUERMX5GHlEVhu4Xi5s18_T4t0n6RXKduLa6_eS8k3NhAE77mzhxF_E0wX4Dnd0RG07qQiDjPW5E3P1bqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ترامپ درباره مسی: من‌از ورزش‌سر درمیارم، یه چیزایی هم از فوتبال می‌دونم. داشتم بازی مسی رو نگاه می‌کردم، دیدم مدافع‌ها حسابی چسبیده بودن بهش. ولی یهو دیدم غیبش زد و سر از سمت راست زمین درآورد. میفهمید‌ من چی میگم؟ همین خودش توجهم رو جلب کرد. هیچ‌کس هم درباره‌اش حرف نزد، ولی من خودم متوجهش شدم!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/persiana_Soccer/26002" target="_blank">📅 18:47 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26001">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cuAfZjPtzJExFzxg-B2ntzgvj7NJcA82yPuQvYgroIb2VtPOPWirRdyIxlrvcl0z0Ye2rCc0E7t_pGlR3W10L0nbJZ4EbfIoFHZXbeve1e5ft8ragpB-e9hBn0uY7t7rFadV-0_0uJp9p0SX8Xl3rJ03bxpfJmZ-1THWfCs6fkExgxSMSTkynLD9_sRQBCPfWK1XxOZ7FiolPyrB9pUtAVMhAmk6UpS7tBH2W7n7MWzRrkzMwLqm1IpQhHIXvI7j8191WZ2ftM6z1JvZeZxDw3N_3Ufs-co0QKWmGDWmtuHB276qBy4kkzGxkNenXMSeQvvBYTP5JfX07sRMZcn0wQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خوان‌کاپدویلا دفاع‌سابق‌اسپانیا باسابقه قهرمانی جهان دست‌زن و بچه رو گرفته و بره آمریکا فینال رو تماشا کنه بهش ویزا ندادند. حالا چرا؟ چون 10 سال پیش برای بازی خیریه به ایران سفر کرده بود .
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/persiana_Soccer/26001" target="_blank">📅 18:43 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26000">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WqrzsWDt9uj5HDBnY0vh3EscernLFnmaN4rFkoC2E95QffbV91hqnJ6bZ_CtpiAzlmggcX7UWS4-mP-Kh9BrkXCW9tWU_e5iB2RcWZ7rPBLLx1PwXpP18PwaILzSeYIUNvbzj35URkbxm1rmktqfBVVFTS6Ehuo1jU2zybCwhRIQyvhPnOFgaJuTdgObEaqpbB9mFsFR6-DaUfczBX4gCigJ09pPCE-gPuibftwIro5UiLQScJZ1rDH1ihxOJORkpabCe5KVY4Z7oMrXRLZaMC2OzkxsIftjHKXiT4ui89M3V-YZGkkprJBfZgZM2nQXeymLvG6y1BH5F2A7GmDlig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
🏆
باشگاه اتلتیکومادریداسپانیا برای دومین بار متوالی بیشترین‌تعدادنماینده را در فینال جام جهانی دارد: فینال‌سال2018: 4 بازیکن؛ فینال سال 2022: 4 بازیکن؛ فینال سال 2026: 9 بازیکن
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/persiana_Soccer/26000" target="_blank">📅 18:43 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25999">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FKGOy63wrzxyddIIfto0pi3i8cSOWhlqXvtyowgROtNKG5DyUp0WnHVP__8xCYjP2j4HK_s4y68Q4uGvnA8buT7xMm7S9FGwBwRjUxyBwXOf4ih7oyb5HoBC9l5RibfyOCfoq-Bue8Rw-xobR6ww4iddJkXjxEiC9Kg1Mr5c-KSGWXyTO1_ZP75pa12SkR0jaGb1BbT8SmwB3UeuqR-BdeVDvEX4L3uGA3iLJ9HfHUgmdO0zWm9oPmzxc4R0TT56EIWUhhJwB0bESIUFCIXYva2y-9DVBer3Cw_QrZZE6kSRmaA1N8atQwwewucLc-z0oPmlYUJFuKy6j8CfKAVWaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">1_برد مساوی فرانسه
🇫🇷
2_قهرمانی اسپانیا
🇪🇸
🔥
💵
ضریب:
2.18
‼️
سایت های شرط بندی به دنبال صاحب کانال ARON_TIP میگردن
◀️
https://t.me/+6L9plEThEMk5YTJk
آمار روزانه 90 درصد برد
🔥
✅
با آنالیز حرفه‌ای و تخصصی که روی ، فرم ها انجام میدیم میتونید به سود مد نظرتون برسید.
🆔
@ARON_TIP
@ARON_TIP
🆔
@ARON_TIP
@ARON_TIP</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/persiana_Soccer/25999" target="_blank">📅 18:43 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25998">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K76ITIPye2q7Zd2O3zdTKd8-lXKjBaEEy7jKT3kxn162JPHvy13snh-os-4eoDv3vUXyJ71soY2FkqWhJZjmuGFqW5lY1agvxMp4DblpCWYzFPruoefe5Q11ap0puxZ46UUDe93XGR8jgmArDmnJnwh9BtlPOgYKjadMT6C3sPmpN0CDHYTp_pYaHXO4O9yWtskhIs158coVy6WOMgXmhzAMANSnGigPQ8BrGxh1eVT-KaT_yS8gVvpXnqAMiRjyloTzpiByyds3CZvqQLYs_L3pkcYYZyLvOK3RKRm-t6KvYnSLa4Li6IcqjPmzcy4UifW0QbbarAwzOt0qxsOpGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
این خانوم اومده با استفاده از تکنولوژی آفساید درجام‌جهانی2026 باسنشو مورد بررسی قرار داده؛ افساید مهدی طارمی هم تقریبا همچین چیزی بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/persiana_Soccer/25998" target="_blank">📅 18:23 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25997">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NQQwEkJlv71g1BV-WSIfFaGABErZ17w0RJnSYkqM3HzLf8FNmlNLipSRHRRPrlUr3p6gl75Gdpkm6R8ShYpBaHM9_1QJ1a3DhdGZQpuQbLBKgFtZEYJ3_JaECUgOGH1I96sYTdtRxYUM-GXmYKHePfjx2_yh8BFciYWRGIgZSNjZ5VsrbQOfY4qgLI_YL82FE7ye1PfxK71_22kg6x4k3EYn5L8h04b1zIGDwUyARkG3qc9RQfzAgAJ6pYdesoPElh-MQlqcD-WkhCO3Uip7xHdiKHKl1xGUzy1dTIm5K8yDFRxEG_uVI3Lj_NgbSSyB7v60rLnHuZ4IK-bCHy9uAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🇵🇹
🤩
عملکرد استثنایی و محشر لیونل مسی و کریس رونالدو در کل دوران حرفه ایشون در لالیگا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/persiana_Soccer/25997" target="_blank">📅 18:04 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25996">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CyDZUAa_VtdKW_bNSgMy6PxNeoPM4ESVmIWGTAAGGaxzQpq3m3a2IICX2Qwcifa1Y_BpT6zvZ72D3yQV5p3VuOwIKLD0JI_vlcwjN5acyem4mHmVtdIE2r6wPLdvACxvcnU8C_zcn3qh9Dr7oaM2sZtKNUBQxhooGJXStDWW82tvin42d9-Xcci6eesyTwqrq2N0_k5G-5yoCB11hOVxwDldmeNfLVWjEQ96kXeM99FkWm4nfSYUuyTXDhCaBLynJ7gfSQ8nm1xgez-2nM37gIPgZOlof_8WB6lTU9NegOkoPLgPuFexJvv7ou2z5xH7mQ3zra23Sixm_mLJFtCnwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🇵🇹
🤩
عملکرد استثنایی و محشر لیونل مسی و کریس رونالدو در کل دوران حرفه ایشون در لالیگا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/persiana_Soccer/25996" target="_blank">📅 17:49 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25995">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/cf0ae4ecd3.mp4?token=NDK0ZX5okAPWrOWgmczl_vd68cikb5i2f0PB4QYL_ZcOSEm0q-pcSjZbS7TsM73PRR-S0S2X-_QHI13XMqJz-_o3TKD9AVEH7KmilS6CDagf0jpPkCp3pEQqbz4eVV-HJd8x6Y7sBA2XkhXZqr_kb0eF3cqnOUD0h7h0tpBQw6fbTHZaV3WVMaELr4jmUlnSR3bC5HGtlwTy_phyFfraQ8AMaJi94_G9iHDV2mUneheg-xn-liApsBYUmmyaqgeRBHDOGNiMFH--KSJojrEmKEspgjQ3EfW2xV-hgu22BvJbSqL0EDQ62f6m1zwfNCWlsQ46AWLYkoRgD7OW0GEHt3xXJ_Vl725FJVZ1IiKicgwsxF9yA7p0LvZQNPPQSzogXFMmY208G2vf9PreMO7msF8gfoI6vN379cSCx8lY94UhT4rHPKfwXfFquRg6PB2EkNejPM8-_iq-WhtDwD_gtFNWq_xxnM1gKXLHZnQAp93pRWaP9fdaeyzaX_elX1qleEi-BOmhIouUurrRWAWIXtOw93ry7laMmHp-9SAQ9w0ZjZK3CeJVQxAuqK3GV3qJQBN4uI8SR7ZTv4w9rRRPGnMH0rpujiENVYlgqzW9pU7cQ2ckSeDLNL3A2nLmgBNTRb8vtCKFGZU8eX5cCs2UsnvHHn8nwFuwifKWLJOzw5c" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/cf0ae4ecd3.mp4?token=NDK0ZX5okAPWrOWgmczl_vd68cikb5i2f0PB4QYL_ZcOSEm0q-pcSjZbS7TsM73PRR-S0S2X-_QHI13XMqJz-_o3TKD9AVEH7KmilS6CDagf0jpPkCp3pEQqbz4eVV-HJd8x6Y7sBA2XkhXZqr_kb0eF3cqnOUD0h7h0tpBQw6fbTHZaV3WVMaELr4jmUlnSR3bC5HGtlwTy_phyFfraQ8AMaJi94_G9iHDV2mUneheg-xn-liApsBYUmmyaqgeRBHDOGNiMFH--KSJojrEmKEspgjQ3EfW2xV-hgu22BvJbSqL0EDQ62f6m1zwfNCWlsQ46AWLYkoRgD7OW0GEHt3xXJ_Vl725FJVZ1IiKicgwsxF9yA7p0LvZQNPPQSzogXFMmY208G2vf9PreMO7msF8gfoI6vN379cSCx8lY94UhT4rHPKfwXfFquRg6PB2EkNejPM8-_iq-WhtDwD_gtFNWq_xxnM1gKXLHZnQAp93pRWaP9fdaeyzaX_elX1qleEi-BOmhIouUurrRWAWIXtOw93ry7laMmHp-9SAQ9w0ZjZK3CeJVQxAuqK3GV3qJQBN4uI8SR7ZTv4w9rRRPGnMH0rpujiENVYlgqzW9pU7cQ2ckSeDLNL3A2nLmgBNTRb8vtCKFGZU8eX5cCs2UsnvHHn8nwFuwifKWLJOzw5c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
ویدیو ساخته‌شده با هوش‌مصنوعیه که خود کریس هم لایکش کرده، انقدر قشنگ ساخته شده که قطعاًاحساسی‌ترین‌ویدیوییه‌که میتونید امروز ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/persiana_Soccer/25995" target="_blank">📅 17:26 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25994">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d46f404ea6.mp4?token=uGRACek6CZzol1z6-MBSxSr8vgFv2fEgGLsVKvdzEiO2WSZPnHjB4XXTpkNOqwjJkup3zEg-ZWI68a1VUq9Ni5_34py1a2bHsLhT7crB8BEevc_Xi5nKtrhEWB5aKRSGsK1XkD4vjIngII28qKxQXtnaK18LS4XlErJcgzAxcGxpJNQck0pgGjkMIu9CaigAGDVYiTFbfi2p75WHNpePT8jLsUmuG9rmQ3Mb_CPGm0baVHGVsCZMHGMWR_-6X8MuhrTKHzNZbcgZn-dc7o9oDRO-IVpDlDA1aNXgtsFEDn8Qjqw7D1xic7ver1hmQ4qDz_FBwwtoZ6noWhE0bPvL6mLqebpD1ztGv7_fXRrOSGQJrfirUguBfPk3t0xmy2BuONzfkye2WEzs5tT1AMIrkaiLS7k1pWbLahRjT_T4hZVPePXVt4xiVzjIBgKP-w1YAKhFWY226eUSMWoN608-Vwiw6tn52HUrJgYjgCyXtb2tWMTMecPMh2AJbhN8M0HAl3jHO2zt5nP0o4XLDlnKTdW4h-_TdQShIhH_UwGW4Sv5SOV-nJFBf_PO23phwan-JERBb1sn17iM_G1HE27Xi7sxT40p04CvWPH4pb48Ua9AZOYPpDIJ5DmY_EW35pIUROTCuDTJKTNbxzTxo6U4XBR97JThl4r3gyuROltR15U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d46f404ea6.mp4?token=uGRACek6CZzol1z6-MBSxSr8vgFv2fEgGLsVKvdzEiO2WSZPnHjB4XXTpkNOqwjJkup3zEg-ZWI68a1VUq9Ni5_34py1a2bHsLhT7crB8BEevc_Xi5nKtrhEWB5aKRSGsK1XkD4vjIngII28qKxQXtnaK18LS4XlErJcgzAxcGxpJNQck0pgGjkMIu9CaigAGDVYiTFbfi2p75WHNpePT8jLsUmuG9rmQ3Mb_CPGm0baVHGVsCZMHGMWR_-6X8MuhrTKHzNZbcgZn-dc7o9oDRO-IVpDlDA1aNXgtsFEDn8Qjqw7D1xic7ver1hmQ4qDz_FBwwtoZ6noWhE0bPvL6mLqebpD1ztGv7_fXRrOSGQJrfirUguBfPk3t0xmy2BuONzfkye2WEzs5tT1AMIrkaiLS7k1pWbLahRjT_T4hZVPePXVt4xiVzjIBgKP-w1YAKhFWY226eUSMWoN608-Vwiw6tn52HUrJgYjgCyXtb2tWMTMecPMh2AJbhN8M0HAl3jHO2zt5nP0o4XLDlnKTdW4h-_TdQShIhH_UwGW4Sv5SOV-nJFBf_PO23phwan-JERBb1sn17iM_G1HE27Xi7sxT40p04CvWPH4pb48Ua9AZOYPpDIJ5DmY_EW35pIUROTCuDTJKTNbxzTxo6U4XBR97JThl4r3gyuROltR15U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جالبه‌بدونید فدراسیون‌فوتبال‌اسپانیا به سر آشپز ایرانیه یک میلیون‌دلار داده که در آستانه دیدار فینال جام‌جهانی‌بهترین غذاها رو برای بازیکنان درست کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/persiana_Soccer/25994" target="_blank">📅 17:08 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25993">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UfHEcZQIiHq-oYa48qM3xYnESBnUbmYyWpqq_xsbxjdIlHqLcBVkiUSrGlH4qC-ZYDhVCC5bi6-oDo4TPYMu6oqse_s5krLEKW_wuZk0rj5vPGTfmwfTyLeXPy_F1JDrf4KOdI1S6bR2uXjen__bxsAjkDk4BO0xKCUfzEVZv1vYB5xQu39hKJn1hBC-9nn68jOtoXyrcQMdtuGZseeMPwr449jqwhTZcyU6YUhTkjJiilMQy2K1ogzGSxczPaceCvS4JVRNAGCz683pYKjAmBY-RRhTLgl3jsQbtNrHKhfS0aheo3ABCQkSnil0h3gPZ0Q-WkldlpGKHsbabNc02w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ بعداز محمدامین کاظمیان؛ یاسین سلمانی وینگرجوان پرسپولیس در لیست مازاد مهدی تارتار قرار گرفت و از پرسپولیس جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/persiana_Soccer/25993" target="_blank">📅 16:54 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25992">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fpxbr9jJmtSjs2SJEE5zULTliOoEc9PvRUDRvZmAFUr9Un_JUkB6NMRyysxbVYUW6VYT6hFXujwfKsXhUAdY97womn3kFOd3S0HB6HghFrsKdVf1TRcy1jHtko6ZoZHa5dvEA7zhzCU5BFslYOJwoateakkZF8wZHCkC9a4uchplIRyZR1N-myDUr2pmyr1hdM3J1SpGwRnXI1AbRB8ynoQWbSDx9_pb-Ui0h1sVSqdfx1UYR0yBegSU1KjrndqLQlX9A9iXK7o0Nm4aDJRtVrPKO2Ytp-6-1AGuP5mbSjc3mNl7OiETXB9ASpOAqmOv5DmNXOP5ScUAsanaQwYVxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#تکمیلی #اختصاصی_پرشیانا #فوری؛ محمدرضا اخباری گلرسابق‌سپاهان‌بعد از تماس مهدی تارتار دقایقی‌قبل موافقت خود را برای عقد قراردادی دو ساله با باشگاه پرسپولیس اعلام کرده و اگر اتفاق خاصی رخ ندهد اخباری بزودی پرسپولیسی میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/persiana_Soccer/25992" target="_blank">📅 16:44 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25991">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nWjLMQ_B1ubGfPIwrha36UKWIPdIut6OSwVMb9abrtfY3DjPcVZIrbO0bE4gf_t2FDkfRecLd6Nhh1vbPdNiWjIVasr66Od9EdjW9K-FXBmN-E1IWMVJqyEKeP8aWYAvaocGpl_sRG5xjNXWRdvneUa-jxumwH2k4GzbYZgyLC2Xbdo1Vzcw6UKB9YibCc-fF3oGhO45umxskuBufGSF9xCcwsiauJk6OBTaF2ZnOa3gQxk3HWjLfuuU8mwjv4-purr70K-ifhLho-B3d0CTxRwd3OSrLk-KwYXweChLLVgrrtWDUhReyVujJAhQBYHbma5YmY2Yna8ODR8vRVKQ-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ از طریق نزدیکان خودِ محمد جواد حسین نژاد درحال‌پیگیری‌هستیم‌که ببینیم طبق گفته علی‌تاجرنیا باشگاه‌استقلال‌باباشگاه ماخاچ قلعه برای گرفتن‌رضایت‌نامه به توافق کامل رسیده یا که خیر!
🔵
تااینجاش روخبرداریم‌که استقلال با حسین نژاد به توافق شخصی رسیده…</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/persiana_Soccer/25991" target="_blank">📅 16:19 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25990">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IMC7lz8zOjEcu1YjVKXHR2lv4foUP8Zt0CtaT4clyPetU3TNbz7fRkJ5eDmfIfG7gUzcKePRmQ2DsT7NcQuNNTPWmuNd7R03UlKCRQUiOsFM6dLYbezcqQXXVlgKN_b52ydeMF_cZ2SMhbtKmVmvINmBbZlwwPGXR0zE4ssFM-hZOp_XGO1EQ81B_6V3CMPuq3oacC5dkPGZgrpXCGbgTdVQRszIbfrgLlJ87-dJGnb8iALsuW-v25H_5TaqlhJjkBJxHvUmfZ2qCBg8uKCtHZHQBH7Noo-JrHj3KrsB_Ht5rUBUg6L6I5PG5Ubl2aPCcbbiPAIQPQn-K_YTrIcUfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
رفقای گل دیروزهم گفتیم باشگاه پرسپولیس هیچ مذاکره‌ای با علیرضا کوشکی ستاره تیم استقلال انجام نداده و هیچ‌برنامه‌ای هم برای.جذب این بازیکن 26 ساله نداره. بعنوان اولین‌رسانه گفتیم مهدی ترابی 32 ساله بمب اصلی مدیران باشگاه پرسپولیس است و امشب هم جلسه بسیار…</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/persiana_Soccer/25990" target="_blank">📅 15:59 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25989">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bi4gzXHJN_1j3cw4gMCwolOiZaP8N4-9eqQp7wb3eIuWsQAcL_zTK8QlDoyNh2OG9qXqCj3tjv-6j46eWiTWZGWwSKiibJE3d1074ZqIKsiCXfJRyWv0LFhnxJIsPRayLRXvcL0Sp4QKK1q4Ep9bZfOxk29VvH-RXL2NoduTMA5F97_ipwbN1_nKbKioD-ahA7PAGouwLRwkyKtfqgqUXaFc0rc6jSuvkGeNlznrI8M7FchweHLSFe0E9YBWvw2RkmPkO8OVViJ7YphJDsl79oz0KA2T76Rw7wsbhRuidqFpTgdS_bwT7BvrNurd1E-una63FS85I5aj-6f3jyFptA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه استقلال موافقت کامل خود را با افزایش 300 هزار دلاری رقم‌قرارداد یاسر آسانی اعلام کرده و به مدیر برنامه های این بازیکن گفته که یاسر آسانی به ایران برگردد قراردادش رو سه ساله تمدید خواهیم کرد و پیش پرداختی یک میلیون دلار به…</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/persiana_Soccer/25989" target="_blank">📅 15:52 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25988">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OPPlSrofad9kEmVu1ucNgvjcclnAmyvlehcCDl66S76O1kHWXwg4U_DT6w3fac_1MGf3RSwere2cbzSX3JPTWP5iQJUA1kaWho3bZ-9UoQDCKcCTWKfymBA9k3q5ie1dBaat5OHvQsiQbBR6XU3HQfstykE0-jQhQtUipUJQ1KVgBOIqFJLQbD-CEWExeftai4Et-V36ZPEmwAorOG6qKHXeFrmYDnGfYCRN8s5PrUSnIbGknnO7PDjGuIlVZOwiiZXs9SoayRv6uTj2tbg77uQ3mug7Jao-FuwZqbbd1_K2AjCITFPvGnjEQ7Bqciy9V1nkcCTOmaXsaFS5PFfPxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
#تکمیلی؛ طبق شنیده‌های پرشیانا؛ یاسر آسانی برای فصل آینده حضور در استقلال 1.5 میلیون دلار خواسته و ازطریق‌مدیربرنامه‌خود به باشگاه استقلال گفته درصورتیکه بادرخواستش موافقت کنند حاضره قراردادش رو باآبی‌ها به‌مدت‌سه فصل تمدید کند اما در غیر این صورت ظرف 24…</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/persiana_Soccer/25988" target="_blank">📅 15:40 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25987">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/letSSacSNE1zBj5x7PYPzZgL9qAVbMr9fyqNKmZRiNTz_1K4tLThRojlrULGNDr7PukkhsStCsIrI69N51g2FcmMiNcYfot0937WID_NIfi4AqzAStXQNQ6SVH_ZWFJ-As3nxPvtPgTEmnopdtCYMEegmXBaOWBLXrNm4YSE0QmrcHxmyvpOcr6cf53R6AVRv8YS4h-ooPBZpuCjW3xM7nlwaK6PuBzRyQ6LGwF9J0O80nQ_ep15LJlpScEX8XjyZ6rYPtWOGCrBDPOINl7YU-BuyWa3bxjoWdavVD9sw-FEtbGwOaZqH-PqZ3cCK8veEk_LYJ7zilc82wTQR5vqjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق جدید ترین شنیده‌های رسانه پرشیانا؛ باشگاه استقلال ظرف همین‌هفته‌از تمدیدی‌های خود یعنی روزبه چشمی، علیرضا کوشکی و محمد حسین اسلامی رونمایی‌خواهدکرد. همانطور پیش‌ترنیز خبر دادیم تمام توافقات با این 3 نفر انجام شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/persiana_Soccer/25987" target="_blank">📅 15:26 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25986">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SYxb19mj_Ive4DUdSsZfjcOaqOoIhSO98PrqLsM471ECXC8uXehtSzBMamuQtTRRAc3F86isAV3skG6ZvAmEytcsqdqAt8Ru8GwVFZpk5XcQ6kpaBz6d8yfiMOmXesrNDa9iQ0dy23ByGOHOS-0BMfDwI3aEIRKOT-SYQtyF_uinaPppNFalge2tMizF1aWBatYjSlGZhDO47G1d5u2lVscpbBQ6utl_BKDSAZ-3rqUjnFWxcqmMnNaUdCweDTs32T9-qLXaDuIOhYWhg7fG3oFiPK6ivcCcPYAcaBWCtUoDqt-d3QIflfuLJagDa0YDWAuFsB0Sc7w-HsUMl-fTUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
◽️
🔴
#تکمیلی؛ امروز حوالی ساعت پنج عصر جلسه مهم‌سرنوشت‌سازی‌بین‌مدیران دوتیم نساجی و پرسپولیس‌برای‌انتقال دانیال ایری و کسری طاهری به این تیم دارند. طبق شنیده‌های پرشیانا احتمال اینکه این دو انتقال انجام شود بسیار زیاد است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.2K · <a href="https://t.me/persiana_Soccer/25986" target="_blank">📅 14:46 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25985">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mp5DHZdLk7b4hnn7zRpL51RkFFyo0i-gIHOUe4Bo8Q6x5BXtcjf_rC7jye-an5jTVpFT4zMUeL2SaV-sC9wpd3B2fRFZ8WoqGcyi-lOFoDbVKeu76fXNGhlLFqLAciGlbY1FqHPUndGx4mNNtK1jsULa2HUeBgz0UChvaf_7pUudT9LTICcKu076gRIcI7jMDcfpTRCOR212NVqbrGUY3jP-yxyE5SCGdtaPxFAOpy834JT5B-fyXT1hL9sXTLkRek20IxrhKLtcbLO8nFtJ4QWj70R4HS1i9OtupS630qIpV0wY1Qks1ePBO-RlWwr8-AW2_ThTK5Fpd82CWCYLMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ طبق شنیده‌های رسانه پرشیانا؛ باشگاه تراکتور برای عقد قرارداد سه ساله به ارزش 150 میلیارد تومان با محمد مهدی محبی به توافق کامل‌رسیده و بادریافت رضایت‌نامه‌از خرید جدید خود برای فصل‌اینده رقابت‌ها رونمایی خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 72K · <a href="https://t.me/persiana_Soccer/25985" target="_blank">📅 14:21 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25984">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cFab79s20IHbcdme0YcNP1wzFTGcQ3-4SNVFoxCovKDm8jDv04a1Z7Y9UsWUIBJ0Fw8Rih5JTyn53lS4Wja2vipheLNIPtkpE6nx2I4xz00xv-Dl53ieqoKWT5wXpjQwKr-4BVCz-vbLOsKd010gjpsC1OD_CP3LBGYKFlw2k9ifOtP806sAaZn3XsRbcvsoepMdolLD1VTxCRMbHgTr2pHhWsFD31Ie6Uffc3SiXFnsakl7QvhJjfTN7Ur0_EAgfalBYCnyOA0IY0QMPd-gqBb4qjEDS9u977g3KWmuJvK5Tc-83j2wDU4dwR7wIF_BjsYJXdnDMVZYMuorGQq9JQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">◽️
🔴
👤
طبق اخبار دریافتی پرسپولیس؛ کسری طاهری از مدیران‌تیم‌نساجی‌خواسته‌ که کمک کنند در همین پنجره‌باقراردادی‌قرضی همراه بابند خرید دائمی به پرسپولیس بپیوندد. زندی مدیرعامل نساجی قول داده که همکاری کند این انتقال بزودی انجام شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 72.2K · <a href="https://t.me/persiana_Soccer/25984" target="_blank">📅 14:10 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25983">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vl5rvXXabkvRgJvwWLmDlR5RYgqu9jGToSKDh_JJdmgWf1KabqdLdRb3L387T9P3sRZEXBKJrgdDeYu-QLY4kjystEOjpusoF8ePC_auteCFhJlrstGo5QlP-IJQgUylTkg4uA8N1SEStMVV8h78uY4VnReYAMf1zxkPmoRoSuG0Nk8sDe7AxhDcDc5fawknYSEwBhZzPOZdCrrz1iW22sAdt-fQFe8mSPOyFxrBFve-e-kwGogYo7-sL9-9lWPxDcAA8A2eXxf4JvpARkUjz_NIg6EaHDECQ6dTUPjPHvNafHTSSyFMIUogrklOVF8Qyuvm0xsSa_SMwtwGdrGBfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق‌شنیده‌های‌رسانه پرشیانا؛ شهریار مغانلو به پیشنهاد مالی‌باشگاه‌تراکتور پاسخ مثبت داده و اگه اتفاق خاصی رخ ندهد شهریار مغانلو به زودی بعد از بازگشت به ایران قراردادش رو امضا خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 69.2K · <a href="https://t.me/persiana_Soccer/25983" target="_blank">📅 13:59 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25982">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qB5SqCnaWBlgH3PVcuI5iI8Xx1Bq8AKtjA42bXQfGZmrvKwXHl0oRn_1IUosPN5r_kAR5qitf_LakcfZ40JNleQ1758u13JZ0fhrDVPUxgXqQQ517z4byUy5RCPSKcm6DdZAP52YP52iGSYqDWvVTc1l2tYp-y4-WJ9D9kJP7THPxCLh7to-uoSGzzOw8s5ioWt9RJu0U8RsBxtlNVXB22PrA7y06Wim5sksj5ru4Ylzi9Zo9kOaaKkoAdoJwuid500XZvG-oTUkqYD-H3gTBlF6n5kDFybSpnju97FNzLmwcYFwPqPP95D6Mk6WIcgS_NeIJBWRxnN52S7dd7NjBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#فوری؛ تاجرنیا رئیس‌هیات‌مدیره استقلال: مابامحمدجواد حسین نژاد و باشگاه ماخاچ قلعه برای جذب این‌بازیکن به توافق کامل رسیده‌ایم و بزودی با حسین نژاد قراردادی چهار ساله امضا خواهیم کرد.
🔵
علی تاجرنیا نیز اعلام کرد که تکلیف نهایی پنجره نقل‌وانتقالاتی دوشنبه‌رسمامشخص…</div>
<div class="tg-footer">👁️ 71.4K · <a href="https://t.me/persiana_Soccer/25982" target="_blank">📅 13:48 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25981">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/byooo9WLllUMShqtDCUyHpl13gdFhkqvwnGqGMQRBBDwsQfnJIQMnBadcSzuLgmlgelrs2enIB-VBFKBE_nnZ7qeLFdhcu_uov-GpDNgmoDUHOmkbfdGPEoqmkEIMxXdLdEgeFyNuU4wqAqljGQ6JHWQFCLOkV92m3mq343I9hJ6fgFqz9qhHx70z8PWD5KNkS-9aNHcR9Xy33PWo0pguHSZps5Q8CiAJOov1CToU-K9xGDJBytl7LrWMtAtv9_3ovdofsmLmMibpbhBkzDrdnneVLW1Ga6neuMHIq6SBbaOR8l2iY5gmRXVQv3wZNipKvLh0kxp6vN8ik649LmQkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه پرسپولیس امروز صبح با سامان قدوس ستاره تیم ملی و مدیربرنامه‌های این بازیکن جلسه‌ای دو ساعته به شکل ویدیو کال داشته و به این بازیکن اعلام کرده علاوه بر پرداخت مبلغ رضایت نامه حاضره قراردادی سه ساله با رقم بالا با قدوس امضا…</div>
<div class="tg-footer">👁️ 73.3K · <a href="https://t.me/persiana_Soccer/25981" target="_blank">📅 13:40 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25980">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ce_57n8xP8fj6w8xEnnhaD8iWEYuRCp0E-WCZ3XidBPWcYE9A4KO5DzTj2kMp3RmlRGVhdLWOg69kaRJaFC9E2MlY2lntAJUWOnr04Y5OKRFQo5H8_43XzCaDT_ZK1GJLb6UBShOxp_tRxWlg_O0zWSrOEo1p7RV4qmwXepkfaRI6Lka-9g66qdRK0q5aIdlqCS8p1MU9aNAeXa6IlQlvDqMAjOHVFGw6vu7RDnvSnna9SqSqZpWHvpvYgDCQkbyZT5GIYWsxukJvxDZlhabWmQQG9HV-vjeTIlO4RG2KOwpv03xlULwUYhRbNTx1lyKwLTdZMTQWJazerOHBTjhzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
#اختصاصی‌پرشیانا #فوری؛ باشگاه استقلال با ارسال نامه‌ ای رسمی به باشگاه ماخاچ قلعه خواستار جذب‌قطعی محمدجواد حسین‌نژاد ستاره22ساله این باشگاه شد. آبی‌ها با خودِ حسین نژاد به توافق کامل رسیده‌اند و تنها رضایت باشگاه روسی باقی مانده.
🔵
باشگاه استقلال به روس‌ها…</div>
<div class="tg-footer">👁️ 82K · <a href="https://t.me/persiana_Soccer/25980" target="_blank">📅 13:10 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25979">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kIPfZ-4_YgjAumi9rYQ19hCSJ0NnRQSrOCPOrNPCep_t2FggqLUSFDyorZm3dvcB5jP3ZOjkm-gqUgg_o21Ohl9dh8Iw_3NuRmcRe5EHs-_7MzGYBDrwD9Xyc9REerbMdS357OPlVMtEedMRTUyUMfvYo48HIRyGq5szyEvyvgLZoM_Bqfd-Q_qk2Fjc1dohk54c7xqqlnu9QQudcHdV-zMsFLtqbHQuyh19Z8jcMu31FgqQBRVFUXP8K4LOuy_ULpkzUJ5LsDBGuAkZBNXxi5dA1lmmMByLF6Yz39JGEKxiwp1zC12gahQpPbUjNdBQbgtRD1fcrH2j-t9UuAO1OA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق‌شنیده‌های‌رسانه‌پرشیانا؛ باشگاه تراکتور امروز پیشنهاد تمدید قرارداد سه ساله به مهدی هاشم نژاد ستاره جوان این‌تیم داده که رقم بسیار بالایی هم به او پیشنهادشده‌است. حالا دیگه‌باید صبر کرد و دید هاشم نژاد تمایل به ماندن دارد یا رفتن از تبریز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 88.6K · <a href="https://t.me/persiana_Soccer/25979" target="_blank">📅 12:56 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25978">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PVc5TroZW3eTXjs9abQ-L1EszDL47znjY3hazgu2Pj_z30GcXB52lX8OrSydC9LVVXtq2XILvlKp5vsAz-VM-wWG76DF0l2STcbuA5AAx3_6xvQJSoloroHnaamyNDKb-KeTtbZJTErDcDyD8IYi6m8sqwEW8CLz-tdqgZsv8fnJJCsYxEa6xBVCC-qURAvMyqdyXvxk4IZo86KZ1fj_Fc1_O6YQ4cFaIp4aoLyirG44qUP-TSuq2DudbXM72_5n3dpzHKRCTJG-7g3jegWB_kXkc03WAw_3bZtZ-V-9O7lqE9lhEpVMAujUlPwPYu-GHBi2wp59gZ-fpPhI7YtVOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
👤
#اختصاصی‌_پرشیانا #فوری؛ مدیریت اتحاد کلبا ساعتی قبل پاسخ‌ نامه باشگاه پرسپولیس روداد. این باشگاه‌اماراتی طی ایمیلی به سرخپوشان رقم‌ رضایت‌ نامه سامان قدوس هافبک‌ بازی ساز 32 ساله خود را تنها 500 هزار دلار تعیین کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 90.6K · <a href="https://t.me/persiana_Soccer/25978" target="_blank">📅 12:50 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25977">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TnN1IQg1SXn8tC4h0MKvxcb0qkmzXNtqLFeHQ2333Wtz71zUz1m36Ohjjlovv3kWqIPaAcXogjaQAcxM9ghUxIIRy0ah6sL_RU09I3SdcddhLwOSD5YJz-y0W86zOqQq8MqXyS53DwzUUIHNpec9DvMt-M-OUIoSSUtNCYE9WXoSXoMuUosiFiG8XKBL9MMcA3XRg388hQBRHnXNkR7e9YrZHxsY3_EHujxxgmliu4AjtehlY33RRFuElrZPqzSnjElJcnmXbTBNRJIhfcpxv_UvxmIrYAC00IZf9tZOKi9-2pVeceLFuAkvntWYIYXc7-lNyWCWnaQh4BTPPGuRAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق شنیده‌های رسانه پرشیانا؛ مهدی تارتار سرمربی پرسپولیس بامحمدرضا اخباری گلر 33 ساله سابق تیم‌ های گل‌گهر، تراکتور و سپاهان تماس گرفته و بهش گفته با پرسپولیس قرار داد امضا کنه. اخباری گفته میخوام درجایی باشم‌که فیکس بازی کنم. تارتار به اخباری گفته اگه‌شایستگی‌های…</div>
<div class="tg-footer">👁️ 89.7K · <a href="https://t.me/persiana_Soccer/25977" target="_blank">📅 12:40 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25976">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e239GC4BC3IjqDOipMysJQt39GxZ-wY5LVRx195e2iGyp30O7C_eOVEv5D3GmSR69GAkvIcDTeTYmEJaFu-nZ8bXRiO-E33Ka-3X9ZF2EzNYUFRIXi8V7rq-WvufrJltm8mQlilCDPz805TI-R40qNhzh6y7VJ_wP5UBLBdb3_TjMRT9fCwlQQDpoT4aNBODPwhfeY6Chtye9o-V-vi0rxsfQKunRba5kPnNXIXuB9BFVdQtM4D08BkQU3zp2M1DuQRkzaXafHAGovApQGuVZPs-yzRn5kEMJ-6H0h06sc7NPITJ-sXtQR1a9IKorBLnZUmwRKTGkU4esl0PvWChqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
مدیربرنامه‌های یاسر آسانی ستاره فصل قبل استقلال برای جلسه با علی تاجرنیا دقایقی قبل وارد باشگاه استقلال شد. هلدینگ خلیج فارس به مدیران استقلال اعلام‌کرده‌اندکه به هر شکلی که شده آسانی رو برای فصل بعد نگه دارند. ایجنت آسانی نیز اعلام کرده آسانی هنوز نامه…</div>
<div class="tg-footer">👁️ 74.5K · <a href="https://t.me/persiana_Soccer/25976" target="_blank">📅 12:35 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25975">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b3gx_QqqqWiIoBaIP9zlW63Q9KgWxOuOGG1zbo5EtuQabaaH0OfLoZsKx_VcMuloMQs963GLRXOADYMF8cM1wAcxoqeq8StHw61i-fgg8mrZH8SWRYShZJIDLF5gMDscx5FqYzXnjkHguWNdEdqfGAIrHUHtQ6T7S7gNyUoN8oxqkWJU7nIH2PZvpAOt_KCzJN-vpY2j_VP548W8PaG3Hw5u0IYEkjXwTsW4HFQcDs4uSXv2WVYWGh7JwSaR_GHXgCVE0VnX2BuwWDST_9JKoCKduAbf7K9EuqZfiLJzBtt3-K4LpSQalwg_17JdMS3R6cimS_hSGCunrht75ghaPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#فوری؛ شنیده‌میشود محمد عباس زاده مهاجم سابق پرسپولیس، فولاد، نساجی و تراکتور به دلیل مشکل قلبی از دنیای فوتبال خداحافظی کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/persiana_Soccer/25975" target="_blank">📅 12:07 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25974">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZKNdW_F3KqkzTcIo3C1-WM7f62OUNVKjmMFindwGwMRXG_Da2cm2o6Xm7q5-9aXiIUlqRbcFMxTTo1lSDmSjo_EQ_6aqMJ7zWbHqHKOAiZCcT68d7kPiax5ZEAWqtJeDfIoHyuDHppusckEktaT64odi59vDw4oHwpq6JZfqHJWS_zh7O2ffi9JvoKI5tdEXkoM5W06yHdREtu0gW0zwdBt-kpqYL48VigAypLAXsB-SQ9KbfTCDwMJpe-Ntauoh3aC0thbiuJ4gBPwQzhj8MrMR4UIjyMIK7x98aua1-EAXSFar9H-ROS29WKTN0gs7tUyWUE5tdRM65qEVR0PnNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ آفر مالی‌سران‌پرسپولیس به آسانی برای فصل اول1.5میلیون‌دلار بوده و برای فصل دوم 1.8 میلیون دلار بوده. آسانی فعلا هییییچ پاسخ سر راستی به مدیران باشگاه پرسپولیس نداده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/persiana_Soccer/25974" target="_blank">📅 11:58 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25973">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ceab272ed.mp4?token=NQbxTB5aP2hMHtyPeCGBN5YeqipB6x8ReCmzGaWu-gSoOCKAZotf5o-w_mLkcStMo1321THyeQZxu0WnLksZsRz1KSU8n9WllNbLSPELgCxRiIojJpChgqpxnFsd6by_kD4lQuzZPnswuOSymMd4v38MCao6oSU1tVikoQkqVDutD2mA4p8QCBsEgF4wW21oqqmel7sRS99BNEyamlj0TKYmTGFGzrcfp6zIuxPuOaWP4hlxRs-u424eYArNToC3vomETbiXfXEyFyFgqBYBx5Ao2IOflYq4cDImmxbdVaf3PXyPKT2B-mi0FCyRObHi1r86IhnVB6ND4sWj5MbVjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ceab272ed.mp4?token=NQbxTB5aP2hMHtyPeCGBN5YeqipB6x8ReCmzGaWu-gSoOCKAZotf5o-w_mLkcStMo1321THyeQZxu0WnLksZsRz1KSU8n9WllNbLSPELgCxRiIojJpChgqpxnFsd6by_kD4lQuzZPnswuOSymMd4v38MCao6oSU1tVikoQkqVDutD2mA4p8QCBsEgF4wW21oqqmel7sRS99BNEyamlj0TKYmTGFGzrcfp6zIuxPuOaWP4hlxRs-u424eYArNToC3vomETbiXfXEyFyFgqBYBx5Ao2IOflYq4cDImmxbdVaf3PXyPKT2B-mi0FCyRObHi1r86IhnVB6ND4sWj5MbVjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🤩
🤩
انزو فرناندز ستاره تیم ملی آرژانتین:
بعضی‌وقت‌ها واقعا خودمون هم از خونسردی لیونل اسکالونی متعجب میشیم اما او میگه من یقین دارم که‌دوباره قهرمان میشیم. همدل شده‌ایم که قهرمان شیم و لیونل مسی هم نهمین توپ طلایش رو ببره. حقیقتا لیونل مسی رو بیشترازخودم دوست دارم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.1K · <a href="https://t.me/persiana_Soccer/25973" target="_blank">📅 11:47 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25971">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HL3GvLqRhElS6VLn2RhrWt77tWCwu3YwQAXTkXZ6NdN3X7UF6Kgx6UcBqY9GfL1guUxZRktqcN57RF3D6FS7CA8hONfFF1SebIwmoriFkC6GEp5DURRY8N4Thy0oxPSnHAeRb2cFAgdaiaT6K4VN2RKLtBBSybPaWsu9BzDsfQ7bQ41byw5zXcRx9-NlsTRupM_9n6OT8tY6M5Xtp1Dyz9vLRgitz7LVqKRRkjclYgW534BMlksQRl2tybeZh8NZB8JUuNBI2c8ow1I6_xl1rfPdcx6wcEEWHiZGT5xXuG4ay_mBDUctRjnXZzlq5kW258dc8rDlopKBtNsdlPe2Pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pWWQxXYO6sgdbQkA69DEGBptaO3zfSzv54IZmWCWJu99-c-f5MxMzv3Sq2oIo_X7Ya_4MUMdmbB5CTylwKy1inko9Ik54iVf3e8BJC5pkyNyZCSAhAmo7HC5ZYj1B6qqDFo1dmPqbSTTLJ_1QtNOJSnbSKhqNm7Rrylxr8fbYoKzfiEL7GgMg3wB99vkuOoAkKWj5irWf6pri_9UAuMMsgnIWtBk4ldiJidwYZa6RDVtpGTVbe5smbi1BmDLw7feMaDNXfVg1iwtrMSkRPqejlDXWKmny9MurVhayidjhBN9M-xlT2LtSQYQxxTyCc23zJmebOGT5SIvELxcx7ACSQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
پیش‌بینی جدید پارتنر لامین یامال از نتیجه بازی نیمه‌نهایی: اسپانیا بانتیجه 3 بر 2 فرانسه رو شکست خواهدداد و راهی‌فینال‌جام‌جهانی 2026 خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/persiana_Soccer/25971" target="_blank">📅 11:28 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25970">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nk7Wg_2SbOwTuBqzaNRagWIcOHYI8mmCmq0SjdBpjHMmKb96PiUqzT3l8NZOWhbx6VLFpJEQrKVUqmSzwQ3ONeclMXpZlMzCJMAZk3ynS74IpzlZgC0re9om9rgE_ReF04HWyARGb8bIt0pbq_KRkwodNlbH_josMwis3BHNx91T048NonL3PL-aV6879nUSQu3DYmR2KoxFv0MzO54Zx-ZSp0r88HZW0Zq8MVJNy9C0NTiG0gtPfWzxsZtPd-V1B9UnOfKHSNL-qkpZtEY4n_gM5-vPEVUIvu_hzsfbigR45FdgvROmKlpTObiYjYrOoW-c3ew_JSzZSBcp4UDNQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
برترین گلر های فعلی فوتبال جهان که بیشترین فالور رو دراینستاگرام‌دارند؛وزینیا بادرخشش در تنها یک بازی‌مقابل‌اسپانیانزدیک 16 میلیون فالور گرفت.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 69K · <a href="https://t.me/persiana_Soccer/25970" target="_blank">📅 11:09 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25969">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ur3GzlMcRbAFtGsf2XfQC0_ZTfWYDI-fYEi5q4tomgnnlBUMTfpzJcSZobFfmJkoHu-Jg0HLoJVHithwLtbnB-nBEbTOk8-8moPpZWzdQQxcsxT0CWAbCgR5V8G9ySkmGDjO1U4gqPTQutF3VCI1kTMKMYTESWYN6hZ-dYNjL4WXL7rZCP-A9lO4zpCmMOSVTOYUey-VaOdrgr0WWSMIWD2nMVZ3mM88pQsnViHNp6J__o2Nm7j9xA7shhaubAMhLOJmwiCRG3ehIACbYRQduzp7ChVD5Zv2YbV4jH1E0Q-lNHfQkVnKWUU323o01ebp9C-f5q7Zh2TOqqNs0qgf8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇫🇷
🇦🇷
#تکمیلی؛ نشریه لکیپ: فلورنتینو پرز قصد داره به محض اتمام جام جهانی پیشنهاد فوق سنگین خود 200 میلیون یورو برای جذب مایکل اولیسه به بایرن مونیخ ارائه بدهد. بعد از کارهای اولیسه پرز میخواد انزو هم به برنابئو بیاورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/persiana_Soccer/25969" target="_blank">📅 10:59 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25968">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iqEHDCpmILSqwbZKt-zHmvbrcX5jS05Bvl8gKpWtgXnXo_MZK6GwBDFT2Zis-dlYQBcZkdtWcOhFMEZiT8dnOm7uRZtcFBWgPwm9HivMsC9e7jpO28qKayN6ykFNu-QyKeuIUCNaCMA-rUu3Co8iCXGvjof8ug2Y75nsbrIhXEikHUzgQEd0PjZGUpY1EFopOmLkZzU54BuFmK_ZaXpk1-4Ippl-BtixJ5sZwMxIMtB5KZovuWelqbG6qWZKlXk6L_5QDkhdFhLAhGzceqJ-qh_Y6y4jyqB9LefRQG36K9kK6K2pbKRKTl1AgfnA-XCmcFV6thbyB0q0JmV3YsAhSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ مهدی تارتار سرمربی تیم پرسپولیس درجدید ترین اقدام خود تیوی بیفوما و دنیل گرا رو درلیست مازاد سرخوشان قرار داده است و این دو بازیکن نیز بزودی از جمع سرخ‌ها جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/persiana_Soccer/25968" target="_blank">📅 10:57 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25967">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91fe4cb625.mp4?token=KN1K8vp_SY_NQdcCtWOLo7e5mj9iXl5Ug5lRILj7RuIemDUlc5W5dEOCtPjVptvvJYgwAat4Xx6XBBRvzKYcJtclPEKTmZ1BHF3RrO37BuBJt0yURxnLv_OBecCx7Yu_14NAw8rnDJEoTtfGHiRlzeA_5j7Js_6ZAnYdP9-Rjdo5GUAoIbJnxbYZBMW0R6mdUD81juLN0vHQ-ZSNIzXk57cE2p7FbpgFUDNYstwJ2qImzb7XxnDvuw6PVr-Z9Hv7h6ueg5uZYYh_N6cK8AyXkplZ6zv6lknc9JD213othD0igTlJgGbvYlT2JMkgkVfrsN87rE-0etChATzjorxzjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91fe4cb625.mp4?token=KN1K8vp_SY_NQdcCtWOLo7e5mj9iXl5Ug5lRILj7RuIemDUlc5W5dEOCtPjVptvvJYgwAat4Xx6XBBRvzKYcJtclPEKTmZ1BHF3RrO37BuBJt0yURxnLv_OBecCx7Yu_14NAw8rnDJEoTtfGHiRlzeA_5j7Js_6ZAnYdP9-Rjdo5GUAoIbJnxbYZBMW0R6mdUD81juLN0vHQ-ZSNIzXk57cE2p7FbpgFUDNYstwJ2qImzb7XxnDvuw6PVr-Z9Hv7h6ueg5uZYYh_N6cK8AyXkplZ6zv6lknc9JD213othD0igTlJgGbvYlT2JMkgkVfrsN87rE-0etChATzjorxzjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
استوری شدید الحن علیرضا بیرانوند علیه علی دایی اسطوره فوتبال ایران: من را با رانتی بازی به جایی نرسیدم که الان بخوام الکی جانب داری کنم. ترفند هات دیگه نرخ نما شده آقای علی دایی!!!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/persiana_Soccer/25967" target="_blank">📅 10:57 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25966">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p190H2OyRt8qTQIzbWvWjKLn49izLRuiUrtYbId-pEA_616y9QGYU9QgKZ-JH4d9_KgTL2clZI5et8s0IYvv-lI8FbFhKUSNpsBIUL7PiFIPOIVhZX9OTf6rruyO6S4xAaKYzXMJFEiRodm59kJKet_AMpHswiBUHJ8Is5U1MsKVbKtN0_Dcj9mdKO5MHBgFP0YdcPvozZic-5gfIX-7CeKf67tUs_8TbJv1Py37gO0OE1mGNAZCkG6LSFPfD3AteHtTgJKCKTTF3XXeNX35bsiecO6hAfRI_iTRdbrYTij_Cc0MGv-gAVST5wyU9yhNMdtR0tivrYXdRz9rCyPCdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎲
سوپر بونوس
0️⃣
0️⃣
2️⃣
درصدی وینرو
🎲
💰
1️⃣
میلیون تومان واریز كن
3️⃣
میلیون تومان تو وینرو شارژ شو
🔝
✅
مخصوص اولین واریز
✔️
🎲
برای اولین بار در ایران
🎰
متنوع ترین بونوس های را در وینرو تجربه کنید
🔊
با وینرو همیشه راهی برای برد پیدا میکنی
🎁
🚨
اطلاعات تکیملی بونوس
⚡️
✅
✍
️
ثبت نام آسان و سریع کلیک کنید
✅
🤩
🤩
🤩
کش‌بک هفتگی
✅
🤩
🤩
🤩
بونوس واریز کریپتو
✅
تا
🤩
🤩
🤩
🤩
بونوس روی برگه‌های ترکیبی
✅
پخش زنده‌ی تمام مسابقات
کلیک کنید
🎰
✅
درگاه اختصاصی برای کاربران
🔊
اپلیکیشن حرفه ای
📱
🔊
همین الان وارد شو و فرصت را از دست نده
!
🎲
🎲
🎲
🎲
🎲
📱
کانال اخبار و هدایــا
🌟
sr27
📩
@winro_io</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/persiana_Soccer/25966" target="_blank">📅 10:57 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25965">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oEvkHzJPU_xD5fncaS0RHPCmefYieGDqx7jCPhgFmnFHoJ7aU90i5Df_IOh0akNxjqShE-VUffa6Rtpj5Hnz3C-FA_XsRF9-Lvp7cWXum7OAFPtRhqyNmAA8Z9vbg2aLjx6XVRETCwmhV0vk3E6AxzKI6l4teANeVeXxbpMiwEyrUt8aGyQx2al5-gQ6o038DYjT58cXIyG5zBZR1oEf6_FyLS3IcrQ6GRDFy86QeL_EJpB2kwrzAEDrLP1k2GNT18u3eVYabrSoAVrS_CXI01ziAy7oY8tlQCOX1yGPmSdyANujPssBuEeWhLAR23_pgrfpBvSWjDCM4kYiZRGVRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
🇪🇸
درفاصله‌کمتر از 48 ساعت تا فینال جام جهانی؛ لیونل مسی فوق ستاره تیم ملی آرژانتین به این شکل به‌تعریف‌وتمجید از لامین یامال پرداخت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/persiana_Soccer/25965" target="_blank">📅 10:24 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25964">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hSeT2USR-tjMBy9BtKxVJIh_gvGE3qoc0EsUfrcjV97tndyaA7wksXXOGBrDtZaymUunFqrj47hkFN8Z6Core8ybgvNkw0K2VoD9K9aMg0As4FTgVWqFOCy_bOxLi7C7PfGmL9FYaI0GNzMHZPP1q5isbxIwCnqFzurCCNG2H6hME2AwvftTpDUX4awOFfwXslEcEuhsFO_L2EkpJ81cFSOMBN5x5UGp_0X54ZG2ZO3mu54EcJyrSuCtBZ3u1Y5VqYSM1pqq3mdIYzD2xNcJIU2pRqYSrsWrrNI39LmMy9UvGkotioOlN6eg41Xlt1efqlTvxPQguTa9ZpYO9npkPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لحظات کل‌کل پریشب وینیسیوس و اوتامندی و به رخ کشیدن قهرمانی جهان توسط مدافع آرژانتین.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/persiana_Soccer/25964" target="_blank">📅 10:11 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25963">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3687e3b81b.mp4?token=pniUsNM5pLkU9b9pKEjh9_ZnePNceMV8Ox_9znRV7_3lJZLO0td7vKvoFhDeSBTjglnixnVFq78fAcJ671l8F-TDZlAy1nwjgx1OaQRjQQKHIVl1xChJrHMe8nOnHTo3cdF1hEw3T05Ekm-s_FpXvIaGd--226voe7rTc3zJBJjQse9VntMz0VPG8IPxOi_gm1ShBwP6STq-R0xcmgTv4K5o4ZfR_BzSiW_RZiEFVxvkB2L0lKg3svjBCbYjqw5qIUsQZT05ST833gD4aBgeDnxTvBDdmr2meoMMlcB1zrDe4RN_ABNMyLaN-BIxk98IaohwP8YFaqFY8ix27be4lA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3687e3b81b.mp4?token=pniUsNM5pLkU9b9pKEjh9_ZnePNceMV8Ox_9znRV7_3lJZLO0td7vKvoFhDeSBTjglnixnVFq78fAcJ671l8F-TDZlAy1nwjgx1OaQRjQQKHIVl1xChJrHMe8nOnHTo3cdF1hEw3T05Ekm-s_FpXvIaGd--226voe7rTc3zJBJjQse9VntMz0VPG8IPxOi_gm1ShBwP6STq-R0xcmgTv4K5o4ZfR_BzSiW_RZiEFVxvkB2L0lKg3svjBCbYjqw5qIUsQZT05ST833gD4aBgeDnxTvBDdmr2meoMMlcB1zrDe4RN_ABNMyLaN-BIxk98IaohwP8YFaqFY8ix27be4lA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🤩
🇪🇸
درفاصله‌کمتر از 48 ساعت تا فینال جام جهانی؛ لیونل مسی فوق ستاره تیم ملی آرژانتین به این شکل به‌تعریف‌وتمجید از لامین یامال پرداخت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/persiana_Soccer/25963" target="_blank">📅 10:00 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25962">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zmn-vZ3Hh2X_4Gjdb-3IDY36hzYi9Gr5AnVVmhuflrW4bqzR1h4peZqRoWAqBPW9CQCiGYawKJ331t5PAw3J0uv2OsTM6syExZnPLHn6Csg3eK9GbqPAlbPvPjoZu39_DTcjeFoTirAyQjhj1lnkhb5QuxLuBnrS5aKpUE9ajlc1t66uudOR99JDk4hWSbUJQviw1cPKqDaDyRYI-6V3rk7YQZbgpGqozr6tpvsB5jEdCdn2vj8qA-v2nCUkQKF3zpCiw2E5HoBG4orNkHLbaQXeLITOCD9ZwjAO9-6YNaTD5_Ox5D7EsWVgIvSXkaM3oP3eecNHU5A9_Ur078n5nQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ همانطور که در روزهای اخیر خبر داده بودیم؛ محمد جواد کاظمیان وینگر پرسپولیس در لیست مازاد سرخپوشان پایتخت قرار گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/persiana_Soccer/25962" target="_blank">📅 09:44 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25961">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YnaGoTXz5BGXyRW7sa-hiYhMj-Y8LUcGH8HdlKdw2nrcFl_IO8cCxdR64EVVjRV5A9KRXC-_QFkE938_-lYE1PXxgXOLquoDsK2GhbhlVlUXwEMehZacZcjaBhAyZcegUDAqYnXdqxZyFRiSQed6jhR0dyyDOfI2thoZk9ZiBFvZBHpce_K7EFsh2_cGQT3JVbIO5su5L8VWVGsFzZ1DE0yXKh6off9cSvppX-oPUm10mbAeqvNcJFQv2lkOtdcQZX3GRKT0UP7juSS_nFNsUY9RVd5gAuCLlSW66L8RcKJj79XZcy-Q410LQN1q1f4ncgvizh7ew1QwUqM44F15-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">◽️
🔴
با اعلام مدیرعامل باشگاه نساجی؛ باشگاه پرسپولیس درصورتیکه رقم‌مدنظر باشگاه نساجی رو پرداخت کنه این باشگاه دانیال ایری و کسری طاهری رو به سرخپوشان خواهدفروخت. زندی اعلام کرد که طاهری میتونه با قراردادی قرضی همراه با بند خرید دائمی راهی پرسپولیس شود. تنها…</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/persiana_Soccer/25961" target="_blank">📅 09:35 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25959">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DeC5RYswVDnwg8egxJyHqqeIc_RgVnx3twe3PA5SJWq0SWAemYnjtd4UKQY6vZ2RizhYJBSdF75w5uR1N9T0i4EPHEaQ0PmF-tM-KfYpYoMmivvF2CmDuQ2d4b9nOxvIIYVI5eydWH_WJ1pc1F-dFioKVLl6c_vWifxhTZkg746F72u1F8G9Yprkp6zM3Kf4bWjiB-nKxMhLwIgb2m9lYrznMBPfSeHsiccf7bZI9BnRiiDevmRrWUWftnG1n69O9esdUgUYnL_204U5GVNsGj9P5KCnDGToVYsJY3u-ytlZw65F4pJAC4wmY0fAPW6bkQbdvuu81aB-DCuwcLRrrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
تنها مسابقه مهم بامداد فردا؛
رقابت فرانسه و انگلیس برای کسب مقام سومی جام جهانی 2026
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/persiana_Soccer/25959" target="_blank">📅 01:15 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25958">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BxJ7fpzvG8CnEXg0G6iYF7Lf2w6RHA4N6WsNUIeCPxhKPx604PqOMBXvGyBG8khJl0eWNnvslsCnBWFFAZSn-pjVkJSp-mq2jlmXmIqXpOrmZKI06HYr1qXD6vFkaXuTI79MNk5ToDu9_SHX3pQgEFz8lA9v5_zF9R0jkz_-4UjrRfZFrdPRKhrTBqUpxdm7D9VS5OybLiG6nPChoIBohbaqKMOpIFyLFflab-FB2Fzw0M7R5wMkv2jMG-Ajiedu9-8fLk2ZftDPfPupo_fJfItjABpZIWD3j5oh4V8Gse_fTw4RKEIGMQfrsUDcJw3s7BZvO3EN6034-aefA3t1dA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تغذیه بدنسازی‌ویژه قبل و بعدِتمرین؛ چهار گزینه پیشنهادی عضله‌سازی عالی برای قبل و بعد از تمرین
‼️
بهترین‌تایم تغذیه قبلِ‌تمرین‌بین ۳۰ الی ۶۰ دقیقه قبل از شروع تمرین؛ بهترین تایم تغذیه بعد از تمرین بین ۲۰ تا ۱۲۰ دقیقه بعد از اتمام تمرین
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/persiana_Soccer/25958" target="_blank">📅 01:08 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25957">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e06c4bd948.mp4?token=CbAB6CYMHDdAYItIHLcm0hQ3ZdbZ0FpFRvAnj2DzcZltOpB04-a-594y90cIUCu28CIQ8nP9-JjC_HS_uBRzYuBGDczcLQfCwDGhbOnXbtoaq7_q-LNQHcsOoS4DEYiraqR7wPP26CR3niJ8YOYwKoIDxz35WJ8EGdtTXr8pdlTZU_wXo0CkenEx0mrp7VwAwroLOatQN2hgKo3qwHcGT-iD9d09D1eMExKodLgvUkHMIsoYk1kFRfps9AT4LS4wTh7XS3Cie2_07ItkBb1TFmTXerJ3tkuTTDgVoSSgN_q8IRuK6HUIj4vdR-g-cL26D5slqSA_KwJLc4LuIR52DQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e06c4bd948.mp4?token=CbAB6CYMHDdAYItIHLcm0hQ3ZdbZ0FpFRvAnj2DzcZltOpB04-a-594y90cIUCu28CIQ8nP9-JjC_HS_uBRzYuBGDczcLQfCwDGhbOnXbtoaq7_q-LNQHcsOoS4DEYiraqR7wPP26CR3niJ8YOYwKoIDxz35WJ8EGdtTXr8pdlTZU_wXo0CkenEx0mrp7VwAwroLOatQN2hgKo3qwHcGT-iD9d09D1eMExKodLgvUkHMIsoYk1kFRfps9AT4LS4wTh7XS3Cie2_07ItkBb1TFmTXerJ3tkuTTDgVoSSgN_q8IRuK6HUIj4vdR-g-cL26D5slqSA_KwJLc4LuIR52DQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
👤
خاطره‌جالب‌علیرضافغانی از علی آقا دایی: طبق قانون سه بارپنالتی علی آقا دایی رو تکرار دادم چون ابراهیم‌شکوری زودتر میومد تو محوطه جریمه من‌هم‌مجبورمیشدم تکرار بدم. علی اومد گفت بجون داداش تا صبم تکرار میدادی من باز گلش میکردم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/persiana_Soccer/25957" target="_blank">📅 01:03 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25956">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M6Zt1AFbht_sUdSrnZ5uHNxuvSnw1FS3O2XqKx7FfhqTaJ3Rre87PpUdKNX-06sB1PSiuZy0QhhrNP70UbwCdpV_Aqt_WydPHYuzUxFWpAE3EKBpKNdJewX1KdurwHqsl7pIJENryg0pVfpxGOKOWpOi_udNvFIhq3-EAEy79TS9r6QrwEiHEcCDC22ImE1Zhh7ufoub_-XZ8fCcWF1J_sSiVjKhy5ixR7hFg_Sa1zhEaSV3n9gIYk_SJxZ0iS3C1lbBeZ2aTXblK0eZ2jQpOWHIGakDokQGGPhwyJl7Jinb3uvr9x7QN1IKwbuO8fNak316OU7EP4dH7babfTqbkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
#تکمیلی؛ شوک‌شبانه باشگاه نساجی به باشگاه پرسپولیس؛ طاهری ناگهانی بازیکن نساجی شد.
‼️
درحالی که روز گذشته باشگاه پرسپولیس برای پرداخت رقم‌رضایت‌نامه کسری‌طاهری به ارزش 700 هزار دلار به توافق‌کامل رسیده بود شهاب زندی مدیر عامل جوان‌نساجی امروز صبح به مدیریت…</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/persiana_Soccer/25956" target="_blank">📅 00:38 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25955">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sazrFg8aMM9U6ulm-NksuOKD0RPoHSgCelUtiowWwEwU7Zkld7AhrrCpzHjt19lE7S_U7IqMsnG-a7sqMom6VBoK6OHIFAwcCmddcyBMgcFJbtABTJSwLm59nfMTUNIrEY0zpm3ZAY3wMiU2QAU3pcjFFwy_TdGI5tV8IPimHX1aekdfNMH0VJi-MInakxUnMk3Hz94kLtmQEm4GJUhXW0FO2QAXQDb0qbBk1ViHkSgVXhs9ow-O8z_NUPXzd1gHg-gIN7kplfgnOSoWU8UlJTVMUWFiRMjT3Xln3ITg6bqvI6rHBwJ_jeBLUofAEfWjoDh2GxtRhufMZQMH6xRj0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✨
👤
علی آقا دایی اسطوره بی بدلیل و تاریخی نه فوتبال ایران بلکه‌فوتبال‌دنیاست. اعتباری که علی آقا نزد مدیران‌ باشگاه‌های‌ بزرگ‌ اروپایی‌ نظیر بایرن داره بازیکنان پرادعای‌این دوره‌فوتبال‌ایران حتی از نزدیک هم استادیوم بایرن‌مونیخ رو به چشم ندیدند. زیاد به اون…</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/persiana_Soccer/25955" target="_blank">📅 00:18 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25954">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z3aBtZYVgr6eYld5jLcHwjitiGhTA8z1IJT3sEsVkIqI3lKUgKPIl9rx5fkjkqON6A2g3Nx8-LdoiacU0zVlKIex2KADVChmesYVjedZMBvrgNqA8CdYf31O52n6V_-jA1eleT-9X5WQlPFYrVu9t5yYjx7i34H8nEnx0HhHbfY_M4anwuzbcUvV7xI_er-8Lxjs8gDJ9GUZWdQt901rN11kkGrwR8uhawOB6JMIrbk0kbj8WQ_HYpRU-DON9CVXQQe9LDmBsHdklKdWjaaVCaqA7IJ7bG0T2wealrX-JfPkwidSzOoNvdhSa1LmcOnwU43_egyRMXdxKbJlmXcFzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
استوری شدید الحن علیرضا بیرانوند علیه علی دایی اسطوره فوتبال ایران: من را با رانتی بازی به جایی نرسیدم که الان بخوام الکی جانب داری کنم. ترفند هات دیگه نرخ نما شده آقای علی دایی!!!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/persiana_Soccer/25954" target="_blank">📅 00:13 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25953">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KLH-XADCRe0AgMBd3gWihahb9IW2QFyc5CsmgyYWzblRuDwDkiKImuYEHKnvNLjp3AtEeHO38yV0GrRen4x_Iqg-8cmNnnZ8FXttQ0QDQ9VPCt8oi-fBezOBL4Z5xY9i7QiFYHAKrIn7clAMANY_4vkP4iT3nEWb3fj28dS44FMMmDE7X-RK2FldfhwjHbyg_RbAGOym2sGjVPtTR8HPofKQDhBSm0J_yBId4ZgP5hr8GAfVYZBXJYTZVluJK7NaM-6JSStBdI7MVQb9etR5CKlpvunWHmktBu52Jfk3Tcz7ysWhya_24UgrHCXlwNCDf-Y5MIHrW5-Wpfjw8252hA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
کانیه وست پیشنهاد ۲۰ میلیون دلاری سران فیفا برای یک اجرای ۵ دقیقه‌ای‌‌بین‌‌نیمه‌‌فینال‌ جام‌ جهانی رارد کرد. کانیه گفته آنقدر بزرگ است که اصلا نباید استیج را با افرادی چون شکیرا یا مدونا تقسیم کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/persiana_Soccer/25953" target="_blank">📅 00:05 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25952">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d160628032.mp4?token=pcHd5owqRxrXHGe6rqWUNr2HTo63M7DxdCTkKevu9LBJZJuzDZlrA9-qULLawf729-H5Sj3ees0KdJCQfY2XAAgVoSft2TA6baxD5Hxx_H72vA4QK5-5DDJJjwq_lLqsNNnCIttl1DNoAPQawkFxK-vxlpkUjSSv6mFMU_6quKWbr7WPq1oupna6zjL-gmjM0jKRRpRK9ji2JOXiQjNShCB4CT4wdO9BxjRuMMRfDhp28p-lvK6f2l9ov9tCjgUCHUi3V3d969UDngN23WFe0LZVFgcnyY7Ivmtmh9BNykkVWXsjeuz5TEEi9BIB7Cwltmp5bf5lHVnIL9y7uMkxnkWg_xW4COSKErgx42hk6a8I8oYsNIZHgjUiJQ86t7Je27hRLcMfpmj9Y0tlfWSpQ6RYKUitJTl2CtWupjO8rYbjbx2OusPXEPiKPhuoZLMMkrCYS803Of2t1omDemm6ybh5jI_TRJnT-JWoQkim-uyRy2ZbOeph3tAZwKm9XwSGVX3MRgVaqWPIee5gO-Qlygys47Vu-FgB_NkC6QCTGvsMsv_rTVeUXf2eEXGK6dNzXivAdrtPFnL809aWsVlNLIpSY9qEWms3WSh3zCEfjx8ZoW0RL6kaefDENKG-kSX6eJKj4vR4Ng_dvmz8Vp59gWQi8wnTwRXFFLVrrfg6qFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d160628032.mp4?token=pcHd5owqRxrXHGe6rqWUNr2HTo63M7DxdCTkKevu9LBJZJuzDZlrA9-qULLawf729-H5Sj3ees0KdJCQfY2XAAgVoSft2TA6baxD5Hxx_H72vA4QK5-5DDJJjwq_lLqsNNnCIttl1DNoAPQawkFxK-vxlpkUjSSv6mFMU_6quKWbr7WPq1oupna6zjL-gmjM0jKRRpRK9ji2JOXiQjNShCB4CT4wdO9BxjRuMMRfDhp28p-lvK6f2l9ov9tCjgUCHUi3V3d969UDngN23WFe0LZVFgcnyY7Ivmtmh9BNykkVWXsjeuz5TEEi9BIB7Cwltmp5bf5lHVnIL9y7uMkxnkWg_xW4COSKErgx42hk6a8I8oYsNIZHgjUiJQ86t7Je27hRLcMfpmj9Y0tlfWSpQ6RYKUitJTl2CtWupjO8rYbjbx2OusPXEPiKPhuoZLMMkrCYS803Of2t1omDemm6ybh5jI_TRJnT-JWoQkim-uyRy2ZbOeph3tAZwKm9XwSGVX3MRgVaqWPIee5gO-Qlygys47Vu-FgB_NkC6QCTGvsMsv_rTVeUXf2eEXGK6dNzXivAdrtPFnL809aWsVlNLIpSY9qEWms3WSh3zCEfjx8ZoW0RL6kaefDENKG-kSX6eJKj4vR4Ng_dvmz8Vp59gWQi8wnTwRXFFLVrrfg6qFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇷
ویدیویی نوستالژی و خاطره انگیز از تقابل جذاب نیمار نوجوان مقابل رونالدینیو در لیگ سری‌آ برزیل
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/persiana_Soccer/25952" target="_blank">📅 23:53 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25951">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d33f152b80.mp4?token=IZi4E3JPTYStTEbepAXcvEP4lfrZmEZA8zfUcbJ4qadPvdbmmLsZn5ZrM9FeIE2gEBuuld6dXnYhLVSID4I-3ERQ22rsGuzokUdsBO5vqXz1ZqGGSF3hNBA7DUElTdBB5FT_Cy3xwaYgP3nTjeqoC2EfC4QySqsn2hIgKbxtHvpNN3o5nWUzGLCDs4YmNvl0M0XqwC2X8-xWP8HCcx3eugYTQwA8F73fDBxEqcwY7AGuuhe-k-ic1CEZiLq-6Pr83wLoQrFbvGmJQv1b58-hJnvBHIOL16DrO9DWYdfFHJahRk5tQjUnge0gTq5oIL_v71r-mqgh3Hu5F3Jq0EyVL4sZQgYZc9x0eyjXOctev3n-VdzNkHBAYTkgwtrc4jCSi02etOfM0jHllicRPOwD4MoVbtMS8_5yW9MDFHQkmhfuL9Pa2JzjrdcsERJZmFsS8qHmSGuKyn11WyJfFAUdaWK5FwHFiywPFDov0U0TMfR8ecgkioF8X6R47QxbTCNQ5EmYQZiOL0iRW2sUK2EgY8Z4Y7N6rhXVr4ILIaprjTbdi6DFJmtOQ0UVs4WgpsQDGXpAAxA_do4-xF7a_PnmNhXCYB5eixU1tiOMJjd3qBAkPesPXwo6Nf7qCPj0DFPlyQLkC-x_T0EuKM0vM650yl-AHEHlNukMSyqzbwquCuo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d33f152b80.mp4?token=IZi4E3JPTYStTEbepAXcvEP4lfrZmEZA8zfUcbJ4qadPvdbmmLsZn5ZrM9FeIE2gEBuuld6dXnYhLVSID4I-3ERQ22rsGuzokUdsBO5vqXz1ZqGGSF3hNBA7DUElTdBB5FT_Cy3xwaYgP3nTjeqoC2EfC4QySqsn2hIgKbxtHvpNN3o5nWUzGLCDs4YmNvl0M0XqwC2X8-xWP8HCcx3eugYTQwA8F73fDBxEqcwY7AGuuhe-k-ic1CEZiLq-6Pr83wLoQrFbvGmJQv1b58-hJnvBHIOL16DrO9DWYdfFHJahRk5tQjUnge0gTq5oIL_v71r-mqgh3Hu5F3Jq0EyVL4sZQgYZc9x0eyjXOctev3n-VdzNkHBAYTkgwtrc4jCSi02etOfM0jHllicRPOwD4MoVbtMS8_5yW9MDFHQkmhfuL9Pa2JzjrdcsERJZmFsS8qHmSGuKyn11WyJfFAUdaWK5FwHFiywPFDov0U0TMfR8ecgkioF8X6R47QxbTCNQ5EmYQZiOL0iRW2sUK2EgY8Z4Y7N6rhXVr4ILIaprjTbdi6DFJmtOQ0UVs4WgpsQDGXpAAxA_do4-xF7a_PnmNhXCYB5eixU1tiOMJjd3qBAkPesPXwo6Nf7qCPj0DFPlyQLkC-x_T0EuKM0vM650yl-AHEHlNukMSyqzbwquCuo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
ابوطالب حسینی تو برنامه امشب میلاد کریمی بلاگر معروف‌ و معروف ایلامی رو دعوت کرده این بخش ازگفتگوشون جالب و شنیدنیه ببینید. میگه  قبل از بلاگری نمیدونستم ده تومن چند تا صفر داره.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/persiana_Soccer/25951" target="_blank">📅 23:21 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25950">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qTzBINvXeKBt9CXxrfpiwM9FL_vliWMJpLaEJUHHZeNol7kinQymdz7wfDIDtMD6ZKcECYJ_GksDqODkElTiMzdo8YYHHRxBcc_vHCnjhIJORusszcmkbIKu53vrgK46pH25OFDVOK1JE575OqfbRHSdMgVyf8kaDR5Od7Pg_KNt-rlr6xn7QslhLZs9-p4c1lQolwmnJSYnqFeYWPmHyvlHnfVfwU8G-c2uMDxk16RlOuxoC1QY_60jiwy8k6BOzujP3F1f6L5SlR-QB7ivrvF265nd2Yijhw1NBCbw67z5Orr3YVJ0Ih2dXGr8uK3HDLGMcCMG7u5B7cPpJAoj2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق شنیده‌های رسانه پرشیانا؛
مهدی تارتار سرمربی پرسپولیس بامحمدرضا اخباری گلر 33 ساله سابق تیم‌ های گل‌گهر، تراکتور و سپاهان تماس گرفته و بهش گفته با پرسپولیس قرار داد امضا کنه. اخباری گفته میخوام درجایی باشم‌که فیکس بازی کنم. تارتار به اخباری گفته اگه‌شایستگی‌های خود را در تمرینات نشون بدهد گلر اول تیم پرسپولیس خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/persiana_Soccer/25950" target="_blank">📅 23:13 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25949">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e604eb6c6a.mp4?token=OzLnqqtm8r9AxnUVIVMoj5frAIGoGt3DEkmtTkMIzBVOAfVntyZXAldVzsjGuOyo91PV2CtkNiZZfxb9ONCUfjRhCTKz33MeXZed4z4hErcrSNkGxv_xQ30tyqs5b-j4X4aigvZkHrNBWUm7BrSGWhic3hy5HU2k4Lwcn-JJv6KvLjLl6EHheLsMj5Fy3YatIfgnUWdw0ubRyydZGpgJ9_0ZZMliltXDJJjprFxE6w_0ovY37dKfFA82orNTOtC6hyhgbWk9hUltBwWj9bHVp1s5fIWrF0V1Qn2nF1Hh9vrpp-ggxzm_F-pntgQEzcm7ZY5ZpRk9ZXV94cOH5Zgfyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e604eb6c6a.mp4?token=OzLnqqtm8r9AxnUVIVMoj5frAIGoGt3DEkmtTkMIzBVOAfVntyZXAldVzsjGuOyo91PV2CtkNiZZfxb9ONCUfjRhCTKz33MeXZed4z4hErcrSNkGxv_xQ30tyqs5b-j4X4aigvZkHrNBWUm7BrSGWhic3hy5HU2k4Lwcn-JJv6KvLjLl6EHheLsMj5Fy3YatIfgnUWdw0ubRyydZGpgJ9_0ZZMliltXDJJjprFxE6w_0ovY37dKfFA82orNTOtC6hyhgbWk9hUltBwWj9bHVp1s5fIWrF0V1Qn2nF1Hh9vrpp-ggxzm_F-pntgQEzcm7ZY5ZpRk9ZXV94cOH5Zgfyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
علیرضافغانی داور 4 دوره جام‌جهانی: اگه توانی باشه در‌جام‌جهانی2030 نیز حضور پیدا خواهم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/persiana_Soccer/25949" target="_blank">📅 22:51 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25948">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SUHRkgltTTiJVGXLD7IRNG_8ANDiRP3mU7nq00woWYz1HdcApik_5ynodTlv9b631URWBXwBeyKHc6RHCatZc9M_n-tlrON9xWwPwoxOzGf6jzslN5Jb-coSF9BG7yWCjNiDqssV-P3xPlwotMSts9Da79lPTmh8M4Tx_d1azP0ghBLX2MT3KdZj8EZkqr2HUFxYAiD14yH5EToYJkeuyZubG4o74FU2wf5XPrdDDR8FizcIWqw3ss8F_ki6X7ljOjru50JLbgyaEbQtj-GMe4XDsth6O0WiZqNyEcI0mW4uu9ZKVRRIS7cFSvQtkETfjxINodvwNHrswoRg55d_LA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تیکه‌های سنگین کریم باقری: مسئولین سرشون شلوغه. علیرضا بیرانوند خودش یه مجسمه از قلعه نویی درست کنه بزاره خونشون لذت ببره. علی آقا دایی هم میگه نگو بیرانوند؛ بگو دکتر بیرانوند:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66K · <a href="https://t.me/persiana_Soccer/25948" target="_blank">📅 22:28 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25947">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/985ce0bab0.mp4?token=evscT2FU5Tp28zTENV67gwlRAjlJnwEj4EuutUSgIUFohOIdstrZ_o5uNeOqcr0S5F8HK4eLUDW8UncZkXOca4TIbSCHBMN1DPqbBBxc5OzM05beoqaomLApSX005ca0IilkI1SdaE15Sqtw7nrVm0VhMmvchdp_mcD4TiqspIOLL2YTX4w8n4DFGBIs5HjH41pR8ppXlj0WiI9TPN9jIHUziTKrGWoywmHI_ebXrUQ-58IhcBj7UjgjE_rwMXYScBBjZQxMo68G0s_MB1-O6tUFsImMu2wPlShoQ7tsDpXQTLZ72dz4-XF4YKdt1w-ZJtS2eDkG84jNR305Sppu4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/985ce0bab0.mp4?token=evscT2FU5Tp28zTENV67gwlRAjlJnwEj4EuutUSgIUFohOIdstrZ_o5uNeOqcr0S5F8HK4eLUDW8UncZkXOca4TIbSCHBMN1DPqbBBxc5OzM05beoqaomLApSX005ca0IilkI1SdaE15Sqtw7nrVm0VhMmvchdp_mcD4TiqspIOLL2YTX4w8n4DFGBIs5HjH41pR8ppXlj0WiI9TPN9jIHUziTKrGWoywmHI_ebXrUQ-58IhcBj7UjgjE_rwMXYScBBjZQxMo68G0s_MB1-O6tUFsImMu2wPlShoQ7tsDpXQTLZ72dz4-XF4YKdt1w-ZJtS2eDkG84jNR305Sppu4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
👤
#تکمیلی؛ رسانه‌های برزیلی: علیرضا فغانی داور استرالیایی علی رغم داشتن کفایت لازم، به به دلیل داشتن ریشه ایرانی از قضاوت در فینال جام جهانی محروم شد. گفته میشه دونالد ترامپ در این موضوع به دلیل درگیری با ایران نقش داشته است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/persiana_Soccer/25947" target="_blank">📅 22:18 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25946">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZLvmY8F5AU6GfY7wukswbB8CpauBzsoE0ddLG4BllnOSBOyfd3ajVOOB487h50G5NCnmnB8oXucytuKxP1Edph79UEv5Q97hGA-xS8w3_IIcQhrbjyjyYh9XoNRG-cD1f-J7n5FjFp9JfQefyFXMDp6bOi0GUA0A7HburRJgRvJH4W8dOowo7aIbb0e1jLpE7stItTB-IexNF_CPTwcFx09kgjdq7NVrs4SAUfpTbrJk7STDn7oziJQijVXeoOohqFp4i9xOAMsjBJn97lhN2rIBjhGt4auSIgf7DVunf02fbTjGd4qhPhsSjzxYzzLOZDEnE7oxI0Q46e7H1G-eZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی‌پرشیانا #فوری؛بعداز بالا بردن عجیب و غریب رقم رضایت‌نامه دانیال ایری از 100 میلیارد تومان به 190 میلیارد تومان توسط باشگاه نساجی؛ باشگاه پرسپولیس امروز مذاکرات جدی تر روبامدیران باشگاه خیبرخرم‌آباد برای جذب مسعود محبی مدافع میانی 22 ساله این تیم…</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/persiana_Soccer/25946" target="_blank">📅 22:16 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25945">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F5e64BvrQpfrGGVhGfj5uwztY1czUojs6bMvaUgLwLzV7q0d_D-6nTR2yfTXh_7lLkdxp02WTm6s7J-FrXDqzIb_Q6_pexAVLmoJwSl34XPf0RyaEbXQBMVil_3XaqHeTHGQRRIHyZCd8SJFeh5uBUmRJWlvTIT2yK1mNDAKTsDwoUNf8bsPbSMKn23_DlCl1xI2DoJ0uArsZ6pPW59AOVzyLcSMBOBJHOx5RNwd-CFpDuxcz76x6-3pCLD8UT-gr1EM-g6vnIDqxSOBDjzjjveSzovifP599b8x4zHHiE1LcCuw1HbamY2JIO0tusZWS5izi6dWV1oVsHhiqs_rqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
خورخه ژسوس سرمربی‌جدید پرتغال: من هرگز کریس رونالدو رو ازتیم‌ملی کنار نخواهم گذاشت و تا هر زمانی که خودش بخواهد در این تیم خواهد ماند. قطعا تجربه او در یورو 2028 بکارمون خواهد امد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/persiana_Soccer/25945" target="_blank">📅 22:16 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25943">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/96e7669a60.mp4?token=FfBZNRGrMusJ6Kqi6hvT2oOm_Ttf5BCFyIJmLpmYNvYEDWGYyHJJuKoPpTHnsXTRMZ3A1VGCBfShsM-81nbINHMKE1soCOHOmaP7F2wfwIQtzLky1kcEoojKMgZRT2xjkuXxEolcK6_E0xKYtbZ9-cBiuWJNtaWwxWPv5IqLMrcY4jkH7buzjT7ODWNx-K7UKwh3hmtRgwYOj4QmIKn11eFW3K2x1baG-Pel4s9G298N6o4lXvr_A_CT8A0NV1TiO8YbAarjlrbz7bsO8NjfTmbHJiaJctQwozYsziSGCkk9IMJh3vWPtavRievIhPfty7PmmT64I68L6-7DexBeJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/96e7669a60.mp4?token=FfBZNRGrMusJ6Kqi6hvT2oOm_Ttf5BCFyIJmLpmYNvYEDWGYyHJJuKoPpTHnsXTRMZ3A1VGCBfShsM-81nbINHMKE1soCOHOmaP7F2wfwIQtzLky1kcEoojKMgZRT2xjkuXxEolcK6_E0xKYtbZ9-cBiuWJNtaWwxWPv5IqLMrcY4jkH7buzjT7ODWNx-K7UKwh3hmtRgwYOj4QmIKn11eFW3K2x1baG-Pel4s9G298N6o4lXvr_A_CT8A0NV1TiO8YbAarjlrbz7bsO8NjfTmbHJiaJctQwozYsziSGCkk9IMJh3vWPtavRievIhPfty7PmmT64I68L6-7DexBeJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
لئو مسی وقتی قبل شروع بازی آرژانتین - اسپانیا در فینال جام‌جهانی 2026 لامین یامال رو میبینه:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/persiana_Soccer/25943" target="_blank">📅 22:04 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25942">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cfa86464a.mp4?token=bxdVNfoXnDl9pPaTJmsPfv1gWsecQKSdnwZmCVyCJ5Y11vRPvn7UlloRg-2YturIPcSJIC0S1p2Wk7O7JQPTWxP38rNkvvw9AeyLUnmwuyoamrwMl49yYfndf-FtmnPtiaWGe8RDFot6FSfxZiJa84iqC82hq3WGpaO_z3RFVGU-As-6b1qFY1dMMGLuVlO9dDhPtfW1KJabZtAU5LlaLJVETluVpbEi5n4XLLNvYwkKEIe-HvAOy4gq5QMzeMQW24pOkDTv3_ji7pFCnvOsMvh64DNxkBAHLyoiGv5V49dv6ghKmXOfS6NCMGX0DpqMstz_I_zlW7OVLhsRfbFt_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cfa86464a.mp4?token=bxdVNfoXnDl9pPaTJmsPfv1gWsecQKSdnwZmCVyCJ5Y11vRPvn7UlloRg-2YturIPcSJIC0S1p2Wk7O7JQPTWxP38rNkvvw9AeyLUnmwuyoamrwMl49yYfndf-FtmnPtiaWGe8RDFot6FSfxZiJa84iqC82hq3WGpaO_z3RFVGU-As-6b1qFY1dMMGLuVlO9dDhPtfW1KJabZtAU5LlaLJVETluVpbEi5n4XLLNvYwkKEIe-HvAOy4gq5QMzeMQW24pOkDTv3_ji7pFCnvOsMvh64DNxkBAHLyoiGv5V49dv6ghKmXOfS6NCMGX0DpqMstz_I_zlW7OVLhsRfbFt_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
👤
خاطره‌جالب‌وشنیدنی خداداد عزیزی و جواد نکونام از اهمیت‌نماز درامارات درویژه برنامه امشب
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/persiana_Soccer/25942" target="_blank">📅 21:50 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25941">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aCiHY5mNc2v68HSkS_BFXcb1Uz3lmlyXorN0FutIb7LID8yvZcdm3fbGcOwhvn0PLhXFm88nVhKQm1Zj2Acv8Rizva_adQBpLFGA9f1Is2y9nbz07t18VUL6PTdw5oDll13BsTGSBpvalYIR5thjqFGhZy1HiXOPkcj4WcnXwuN5WQSb_t8VMICfNiqwbAqZbZKGT68dmXBOplYK6eqJXiesRL_jVAN0zzXhsOIL4f9vYkI4U-EVpZPE10nZ66s2xzCivxhVbN9Qon1M1qtPbKqIwWFXt86wwiXYF0cxcrDZg8ShD7LfgkyGYklHbx8ztOiZvdACynRobvvnZ9RCCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛باشگاه‌پرسپولیس خطاب به مشتریان قطری اوستون اورونوف: چهار میلیون دلار بدهید رضایت نامه اوستون اورونوف رو صادر میکنیم.
‼️
این اخرین خبر دقیقی بود که ما درباره فروش احتمالی‌اورونوف‌ازباشگاه‌دریافت کردیم. با این پول به‌احتمال فراوان محمد قربانی جذب…</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/persiana_Soccer/25941" target="_blank">📅 21:39 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25940">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03df1d2600.mp4?token=gX_KfQCwiIMZTFDoxeS27fQEUk9Ymt3cr4onqTshiMaLGIK0SGoBksi1_4z1emgpvJPvqDa0ZJSUIBkDNGSG5bwTqZsH5WwVOXRUStNIqywW34E9iI7WD5OMXwx8Z3EHAPQC27AIkhTC2wKaRV0Kj37M-vstXXUGvfT21ZsXkf_xaHNaaMUuwi0Dg7Bo6aJZ4S62vW7kLE2ArscOfLGMuS1UMpTG42_v_DSO7f1Rjlg_KHcVS4yUO5RG8HsAWmZk0W0a4FWC4LXwtgr7nZNixgrLKTkSY__MUwji5UhYN9NhYjDChWXeOr-ToXilrrJEHNeCn_Z4afZvSBAEdZCzcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03df1d2600.mp4?token=gX_KfQCwiIMZTFDoxeS27fQEUk9Ymt3cr4onqTshiMaLGIK0SGoBksi1_4z1emgpvJPvqDa0ZJSUIBkDNGSG5bwTqZsH5WwVOXRUStNIqywW34E9iI7WD5OMXwx8Z3EHAPQC27AIkhTC2wKaRV0Kj37M-vstXXUGvfT21ZsXkf_xaHNaaMUuwi0Dg7Bo6aJZ4S62vW7kLE2ArscOfLGMuS1UMpTG42_v_DSO7f1Rjlg_KHcVS4yUO5RG8HsAWmZk0W0a4FWC4LXwtgr7nZNixgrLKTkSY__MUwji5UhYN9NhYjDChWXeOr-ToXilrrJEHNeCn_Z4afZvSBAEdZCzcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇵🇹
علاقه‌ شدید پوریا پورسرخ به رئال مادرید
: رونالدو هرتیمی‌بره دنبالش‌میکنم و کلکسیون پیراهن رئال مادرید رو دارم. عجیب رونالدو رو دوست دارم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/persiana_Soccer/25940" target="_blank">📅 21:22 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25939">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qjmQCDHzfY4UFiOpNP0qTRZI5OMOkBcSBtc-p3Q3yFmXksPOYoH8cP4PI8PFhu8IQH5jlCrZdfHZOezsgGwYsvnzZPJGBemlztKxpYPh4xCCPpPOFnNVtbC6KZffZR_Msvd4pp4VSJL3Kg0sGrL8HImsGT_kg94VpGFnJZiqv19WdIahEvdYOIPDgEyZCu3rwJaAWmNUY4tPOC8cLj71vMHsOmIhPhLl5v5Rpa-nVne_GaxOJFw3oIrIvwuqc6lPnCoUEKcPAnhsGxhpMRBR2__OlPdzO3qP9rLuhRlXVJ8iTUR47KNlHO8lWr_XeARoG3ndUvJv5zwlH87HM93LzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
ایکر کاسیاس اسطوره‌فوتبال اسپانیا:
ما اجازه نمی‌دیم آرژانتین‌چهارمین‌ ستاره‌ش‌رو روی پیراهنش بذاره ،اسپانیا ستاره دوم رو روی پیراهنش میذاره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/persiana_Soccer/25939" target="_blank">📅 21:03 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25938">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OQOHisHb5dccTKt3fngYU77qvwJNayWFnqyy_IbTOVlf4fOBPp2gbrfEe-8ZU77wpWLDMXouaUrN9Sf1-fTkz-I0NTuxkAB_6FkIEplZ1jZ6C3NE1qzAhzpj3PjTAyRCSP9Q26Yl0M57GLt7gKcF2lWEvk7glQ_bhHSQ1Oxb04JxtzHelqO2-mgqHzFlGyaOhgIRkT-Aid7OaCGmvwoAanpgZnHSbLosnJqGNlBaHsGnLfPi0pvPLOwu3YfKhuOejkVA9Az5YkCxWSVh1RlNf8nfhhGOtbknXMPgaRv0ejl01T1oc8lu7CF2xijtHX1h_eeayNzpGuz3Ecjqr1pojg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇹🇷
🇪🇬
سانتی‌آئونا:
محمد صلاح ستاره‌مصری سابق تیم لیورپول برای‌عقدقراردادی یک‌ساله به ارزش 12 میلیون‌یورو بامدیران تیم بشیکتاش به توافق رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/persiana_Soccer/25938" target="_blank">📅 20:34 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25936">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hfVJ9YwH9Yt1maFuswHlWPEZyUYQSTWSWKBiI7tp-eRkZ-MEtO0JrVxXaN0HR-X2SB5m-ECSVRS72_MXTQsZWSJXHUkzMRXR0dZwgBcd9VO00qUXkYg70O22aMXynZyfFKkRXIJeuJIftDiwKgejtvkXQ6GXxQKwlQebnL9TUUevJoRXFGd4o5EvLkBjIgdfIbuSXMRgEJafJdNzR93jsXfjowZsVSvtLsLutDoDkRhGrkET7DUJBFq3KP2YpVeM4UhsFZfOudsygUS_YwizuTqokGi__3NxrSORCvD7iMlwhNL3nutRVQseDiNCRQHLpdR_3-dDp1U8wxPsjpxDXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
فدراسیون‌فوتبال‌فرانسه؛ طی ساعات آینده زین الدین زیدان رو به عنوان سرمربی جدید خروس‌ها تا پایان رقابتای جام جهانی 2030 معرفی خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/persiana_Soccer/25936" target="_blank">📅 19:57 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25935">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NpjLc6z6tjrjVeqzK2FIwzF0Z5QWAaqD0wpQ1VHAfbRNEhyHl9wwdv-jJhfK1_WuYo86p_x3lzz6BgErr4QPhBKW78xacBkiH3MBPhaVxN0AflPMqDdWk86oOG_BFq-zktrIjaA1kR3NAy6LWCGUxL1avHeAvrHgg_CUN_BsCnVi0lTUWEMofVlBGrVwSCGFu60mpYSkUihZzEyz-zCAadZSePyV6aXPbdzombaXoDLxU5zHhM2QowTvXMyf8B2-FArv_y5OGS_gqrgU_zso5La3KoD1AnX2BPDLPCHpM_ZCfrIYF9iPUX-e_OBVXasXMjTl5_rcHrSnmvdP3fWaKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اسلاوکو وینچیچ همون‌داوریه‌که امسال در بازی رئال - بایرن یه کارت زرد سخت‌ گیرانه به کاماوینگا داد و بعد فهمید کارت زرد دومشه و‌ اخراجش کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/persiana_Soccer/25935" target="_blank">📅 19:46 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25934">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E-B0AqXQ9XDewtVNlEuBl3gUgYWxY570auE1_vtixMcmJPiPWQ8l44lhllUWHpk1qx4rJg05O5e_h16AOR1-Gb1hUlFBWTAqS3OpEMyVWdXfRWLvzAMHNjgq2v4pUhNHmuVZPuOPuJgSjD-oFdaK1PXqmD2u_lH8eSAu4DfCRXUyyErdQVN-HQyw_sGrPsPsfvpgYIDy5IjvUdNN62i4WG3JkD-1m8aap2ZKvoeMUMcuCsTkgAy01iIwgTriQaKuk73lOUwhubQZgbGPq_fEfMMeMGDTqYdBssKyuK0b59YupOhFSDuA-cZRpoJvv_gPrNJTz5o41K8F5AJqxHnU7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
7نفر از11بازیکنی که درفینال‌ جام‌‌جهانی 2022 برای آرژانتین از ابتدا بازی کردند در دیدار نیمه‌نهایی جام جهانی با انگلیس هم در ترکیب حضور داشتند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/persiana_Soccer/25934" target="_blank">📅 19:22 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25933">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J8_Bh-CiLqLVluryY-Tx1tfxGhRKCA1lGLV2mwk5E0RnZpJRtbjK6oOiNwWBmbkMllDQ5wLv2cgi_9koSTHa9mVh25Tk75BUyW5LjN_lAtieAkicO_nsXf9vsneIfRFMepeAhSBj5OrrQrjELGzPQTIwg1K-c0FEV1RepqV804g7NlwbCbES7bUkP96g-MNCHw40LL5JgKkq3Cf5ztoIfkc1iGK6YFt0t4PDtR2ikjDmsmEXQMaGfI1CZ6C62XatEhqFqVk-Dj4hJFGKcMzK2RLhqRaV_MY37WFaubTtQyDQwJe5l3quafVLAYI7j5LuaMeHrGjo_M4rJExFT-9FqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق‌اخرین‌شنیده‌های‌رسانه پرشیانا؛ مهدی تار تار سرمربی جدید تیم پرسپولیس یک فرصت به محمدجواد کاظمیان داده تاشایستگی‌های‌ خود را در تمرینات نشون‌بده در غیر این صورت او نیز همچون شکاری در لیست مازاد سرخ‌ها قرار خواهد گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/persiana_Soccer/25933" target="_blank">📅 19:06 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25932">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">📹
اسحاق نیوتن درسال ۱۶۷۶
: «اگر توانسته‌ام دور ترها را ببینم، به این‌دلیل بوده که بر شانه‌های غول‌ها ایستاده‌ام.» اگر مسی هم دورتر از همه رو دید، یکی ازغول‌هایی که بر شانه‌هایش ایستاد، رونالدینیو بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/persiana_Soccer/25932" target="_blank">📅 15:16 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25931">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4cf1a14d4d.mp4?token=nuhvnHOhw18_GOE25_i-dX6JQDbbkQZ-SgFPvcWMfcTlSpV85w4wISeau-5v2MIpZkPx8OOniXcGiP5p54SGpnZWGpRWZyJyMgQT_3l1j05IhR7o3o2M6FevSs6pftP0AaIdkzhLsnMGWaa-OAM3SNTvXmTjCGYnqRX3D-u1XYWVQnuDfR2cyPZuHtHMF_LiCpDr65iFZguMiYK0GWsHvg_sqUY0ZW8saiPq2cqmJ9POQ9oBYhOB3DFLidXPWQZCjmeLHIX8AanZDKXp2z1MHzWP7hGY59rlXxv2toqbxWIiZ0ypHgdwdQ90gYVd-R6Qw27erqHCVWnCpWJzcOWZSF8uVgme_gdIm5FJ7Vkyv3ru4lV04r90ifgk8HqytHnDjTj-YWtnIyginXj1eYZ7J9JssHSyv2AnxpeYOzeattC1wKhyFI0EYneugz_4E8gypVWbpG5ILmvzX4i8t_H4jYXxL_TB4mRgIwuLlSdNiJ-9MhhoG0Shl59jpfYsu5rjvfDxSEgAqpxbFYqaaS5JQYHtv-m1aEZ6aVfH-ZUHk7caKnBX7J-71KsP6PyIeiUlkc8sZbJfDZu832fKO398I4pKgJi1Ser1yrtzRhx1Vhi5wt91jYIqaaC_Xviww5HJpeOW_1yVpTlSGzAtsVS0_wj32lrSceBL5dtejkjQaJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4cf1a14d4d.mp4?token=nuhvnHOhw18_GOE25_i-dX6JQDbbkQZ-SgFPvcWMfcTlSpV85w4wISeau-5v2MIpZkPx8OOniXcGiP5p54SGpnZWGpRWZyJyMgQT_3l1j05IhR7o3o2M6FevSs6pftP0AaIdkzhLsnMGWaa-OAM3SNTvXmTjCGYnqRX3D-u1XYWVQnuDfR2cyPZuHtHMF_LiCpDr65iFZguMiYK0GWsHvg_sqUY0ZW8saiPq2cqmJ9POQ9oBYhOB3DFLidXPWQZCjmeLHIX8AanZDKXp2z1MHzWP7hGY59rlXxv2toqbxWIiZ0ypHgdwdQ90gYVd-R6Qw27erqHCVWnCpWJzcOWZSF8uVgme_gdIm5FJ7Vkyv3ru4lV04r90ifgk8HqytHnDjTj-YWtnIyginXj1eYZ7J9JssHSyv2AnxpeYOzeattC1wKhyFI0EYneugz_4E8gypVWbpG5ILmvzX4i8t_H4jYXxL_TB4mRgIwuLlSdNiJ-9MhhoG0Shl59jpfYsu5rjvfDxSEgAqpxbFYqaaS5JQYHtv-m1aEZ6aVfH-ZUHk7caKnBX7J-71KsP6PyIeiUlkc8sZbJfDZu832fKO398I4pKgJi1Ser1yrtzRhx1Vhi5wt91jYIqaaC_Xviww5HJpeOW_1yVpTlSGzAtsVS0_wj32lrSceBL5dtejkjQaJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
‼️
خورد تو ذوقمون؛ کج سلیقگی کمیته داوران؛ اسلاوکو وینچیچ به‌ عنوان داور فینال و والنزوئلا هم بعنوان داور بازی‌ رده‌ بندی جام انتخاب شد و بهترین داور تورنمنت خط خورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/persiana_Soccer/25931" target="_blank">📅 15:02 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25930">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kOfWRoKT-RTGGldIOjUXNlCcFHB1gqmCcXwCRBU3ssYSTCYxQWITf-T1pv-2nlV4FcCVA5qudu-lNLJW9ziyY97LClh2xM59DIPo7z1BjnbLPGf1MVf6zQqVw0e5rhFTZe7YuTp_4z49svd2OvU4RpODe09ugvdatS3PVUItk8VtMiilcwnuXuc86KWmfcutCIToK9CezzNg-Uv5jqfMzo5HpFBZcwLjtw5kxep5IiUs-LWyPWlP5jOEbsqqDkEOAfm9gLVDT0GnmYgxFrPTPAImTmreAiJIokeTMiBJ8Z1mYvieAiZhB7svy0l-qlhBn5fzuTG2MgfoJoZep05QxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
‼️
خورد تو ذوقمون؛ کج سلیقگی کمیته داوران؛ اسلاوکو وینچیچ به‌ عنوان داور فینال و والنزوئلا هم بعنوان داور بازی‌ رده‌ بندی جام انتخاب شد و بهترین داور تورنمنت خط خورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.9K · <a href="https://t.me/persiana_Soccer/25930" target="_blank">📅 14:47 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25929">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n4NJUvRFLJNHwymRbJ9FSIsu8s31-M9oxIPrDHJBTaERVPJhyL9kbBeIqPdbZdT4zxbMu_WX51Yx0-oC6b9wqSadYL2ibKsm-LMVds8dZMoGAvaTrAfIjWgkBAYY4j0vZkrCwx5VPW7jv1CF8kqNCaCmHnNwZOKBTVKhJR_mHfvpL9o4UWvFGYei3lhZeGAaZx27MshR9rs0BDA70xtfGo5xFbad3E3pwTjODkXQCxa91mdwh2rTfzmayaVMpjfkGD_D4sZMb7zXYrhYMZCONmPRWLvglkixSaK6KZgbtfXSffGfzl4vx5PuxhfIByGp_39c9IjlJ_uxXvsb_FyQPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇦🇷
نشریه‌اسپورت: بعد از جام جهانی؛ بارسلونا مبلغی بین 120تا150 میلیون‌یورو به سران اتلتیکو مادرید پرداخت میکنه و آلوارز بعد از کش و قوس‌ های فراوان به جمع شاگردان فلیک اضافه میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/persiana_Soccer/25929" target="_blank">📅 14:20 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25928">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cs0XElFb6VtTvljZFvY8h6o6Zn8tpkQfuhAFd1n5y0OXERnbF8ok3v-3NP7fj65hxt2gwOzlVp5kLVgSAnCZakr-FhYq6KarCFawgtmqJSlBww3tbFvDj5G4_zbPsTXWDO2JMMeqzujQCs6Sin51WzRlhL8KdZDo8ttt8pasUZZ9DDqpGBWHamYSbTCYp1oNR9aZRVkFxab5F9kzWUCYeAK2F4fLOcRdSnFxtKCReUQluycPGU2-3yqo0x5wBoYwqI1Z5g9B7ziqUdQ6Lxl6JaR4gFsG92YIW7-rYB_dVRfBfa3EyyBI4jh921Frgfpus4zqG4rTXo7aPSQf-xHagQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇮🇷
طبق‌اخبار دریافتی‌پرشیانا؛ مدیربرنامه های رامین رضاییان شب گذشته به باشگاه استقلال اعلام کرده که این بازیکن مذاکرات مثبتی با باشگاه لگانس اسپانیا داشته‌است‌اما اگر رقم قراردادش رو افزایش بدهید ظرف 48 ساعت آینده رضاییان به ساختمان باشگاه خواهد امد و قراردادش…</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/persiana_Soccer/25928" target="_blank">📅 14:08 · 26 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
