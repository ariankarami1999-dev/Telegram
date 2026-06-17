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
<img src="https://cdn4.telesco.pe/file/Wb-Ss0AqSTsFYj58dPUV2mO2qoM213g3lwYFUifnSBumLlKDHE83DeGHfF8TFnAFKOrm6PPcb5YO7G011Hco2jdosLJ1D9HGzFljKNFJ7Pgwt-5tB66NiQyyLxNZQwEmpsPeqn48j8nIDGYDniNTAsJwMoQFFiYGW0xXTzGSk7fjNEmkPES2h4Mw1D_kaAliBZ2tJ2XUOUBM02AdhatrewoRlligoo09ekpDESD_9J9LXsrRfwQvLhHaUlRPTNKcUN_Gv9IvS65waEpurPWt-89mvOHkJH3aSxeRZatOcczToWPfXq_ybKdVIRLrXAL3FxAqngUELrNZEx9ZwGOW2w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 170K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-27 13:42:08</div>
<hr>

<div class="tg-post" id="msg-78095">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/827713cec2.mp4?token=L4yL20JmJDWTQIARB-Na1I-fL0lDvnrML1HpeMbzf5AU0X0eu-yBCeWEZtJsyFL540eUt68GMjmVKz7toUqlJEXama7GC5V5CMFYn0_o3ZO1M3Dc0vkC1TRgvE-GUmz3AyH-0M7GiA-BRyLSb5vHjV6zlKhcbAiWp8x802VTraD5c3-LFOsVF9fZid7IfltCwxz6GPI51JFmCAn1bdRSSCWeVnSOELrFmZ8A4La1v1bRsw4U6aZXKY5YEajgIcpND5Bc1k92duM0dpGxl_FjJ1KLrAz0ES8TJXwpK4dEb8fR8LsoY4ELw73bPBUPhfZqozWP4sBE-TwplXCljKECvA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/827713cec2.mp4?token=L4yL20JmJDWTQIARB-Na1I-fL0lDvnrML1HpeMbzf5AU0X0eu-yBCeWEZtJsyFL540eUt68GMjmVKz7toUqlJEXama7GC5V5CMFYn0_o3ZO1M3Dc0vkC1TRgvE-GUmz3AyH-0M7GiA-BRyLSb5vHjV6zlKhcbAiWp8x802VTraD5c3-LFOsVF9fZid7IfltCwxz6GPI51JFmCAn1bdRSSCWeVnSOELrFmZ8A4La1v1bRsw4U6aZXKY5YEajgIcpND5Bc1k92duM0dpGxl_FjJ1KLrAz0ES8TJXwpK4dEb8fR8LsoY4ELw73bPBUPhfZqozWP4sBE-TwplXCljKECvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عاااارهههه تو موهات بلنده زیباس
کلی شیک و پیرییییی تو شب کلنگی نیم‌ساز
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/funhiphop/78095" target="_blank">📅 12:24 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78093">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gZDfxx1x0MBHFawQPFtvVuMGuivm9TTc15Pl8DInH4Qkp6Hhh5cH4d3xDuF0IeXdumUmC5gDJsnZSWhvWVNJZ7TrOXftJpAM1EjRpL3J1Fg8mwEnBagCQzYWPcllsx_bp7b6Rj9QIVRKYNZnIh9MD_b179AntoaCnQp50eNV9EnBfcFH_qxtylAl7soqkNTrLLrX1sHc-BiIO9ZsJYjefmIQzF1wnUPP9keSZLPFGlULuC2TF392zhJWbfo1B_ISaI-xc0vqUV9Us53KqQ5Lt-Q87YVdEGdeRSMVItkcW4PAxxDglr9BI6CLHtn3sYPpLthWURqtC6-1gv7u6FebMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gmJ3pG7KNt90IN6WfhMFedi24jEKuu_g6rUusdsadcS-T4h-LG539jhTtR9DJ5hCynJxljWer73eWZPD5xdk4VM2QkHgHti_7rJ10YVtQsGgGhqEgjCRrTKIojs4deoOsJqZ6XA-v8g9jLanUOvFCpWB4Ry1dRvn9WTlwp1kOUFVSqOFHHXFvXRhQogzXbAhRwUpMsnfsuLYecrt76pxbWXH_URfiInZkLHQcWdAQ9wD_cz3RK096Lhdf2SBIVYh6cOct4c-18V17Uwy5suxnDOr6gajhTRL_-FbZPcd2shfOerm5kv3cNexh45rG3jYPzdGkPx8zRcFIC8ht3kzMw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">این داداشمون هم به دخترایی که فالوش میکنن بک میده
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 5.57K · <a href="https://t.me/funhiphop/78093" target="_blank">📅 12:01 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78092">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hA5e39gem9C6fC_YuRNr4urG2hxh0oGJhLOsQDUP8KnUPW88VuFMap2XjJFubW-GKkXoLYG_kLC74N6eKJjPyOwQn04JBiE7WhmRfSGPhMEFzSJqWRC2oKp-0XuzcY4H03ZwFIALnHdMQJ0FCjsFKt_skNiF3kA2hNPFCKzyQkCi0GHi3vnxcM333OB86vdBOkPn0aGtSxX5U1nDoz4o-OFVXG2ihFCcvO5y8gUa33wIEDst6n_Y6W2TeBff9tTzwbW6E6rOJmU5j67Ed_eE4_jXhN1s3jXyEvEm9Bkmb2gOXsHDNDMkD7PdgcFSrRkHtEE6qoIJKnOqfmp9KS_uVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسی چند روزه زنشو نکرده اعصابش تخمیه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 6.51K · <a href="https://t.me/funhiphop/78092" target="_blank">📅 11:48 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78091">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H4Va2fyssAhQPwN6bzTb0qu53cwi0njJlK4t9cg0tR3PbCikENzGH7fONpB73a6WRJzPLo6DsUwO_DxsmFS3M23p4T-FuHFOPvBJyeOZ2jD1TzNaehETby3CT-suuVBk8jyGyd4rSMBxKgbRFIIVdZzCyCIVvztQuVN_xh_z4gUsHg87aSW1Xv2CrA2xjfEgRtvXabaTWvWGwhYxxBeywRP8b8Yh-kXh2_IINym5YsQMNtIetJgJTMOoHcYgKOUaQt_Kp9HXIlrmnHZj4Y8Bqrs3_g-7t92UaVX5VF5sPKB02PMsIq3nvBblMYFnsFvU_m8jezy0rK7P5SuTAMby7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ملت نگران مصدومیت نیمارن
واکنش خود نیمار:
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 6.83K · <a href="https://t.me/funhiphop/78091" target="_blank">📅 11:40 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78090">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">derbybet.apk</div>
  <div class="tg-doc-extra">52 MB</div>
</div>
<a href="https://t.me/funhiphop/78090" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">📲
اپلیکشن رسمی سایت دربی بت
🌐
DerbyBet.com
💰
امکان شارژ ریالی ، ووچر ، کریپتو در کمترین زمان ممکن
🔥
🆔
@DerbyBet</div>
<div class="tg-footer">👁️ 6.27K · <a href="https://t.me/funhiphop/78090" target="_blank">📅 11:40 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78089">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bC35lJKy-vuwGBUsa866sf_5YzrazZZW4NpKshLG5CMwzm3IJbFp4UxYXmOW7qsi3t-UwRyE94zTqBKHAYJCDFKEqFqrijoNhA3kfTl0rUKoXRcQ9myo0eLKxg-lZuawxAImDTHWpaBNv3RB471G-mYR60g9fWREE_W0dRGIUyOkKNF9n1zowBvEkoffi_bHkNpQmB5V3FzvtupOMl6bQ8Qkt1HqsSB71B87UXsiPBAPLAUwbma90y7-TRPuP86VJjJU1b9kTozetVRR3Y8CDcrPawe7fGI2CAAAVXIuOKcMbYF6Vbch5ZONlyN339z2i2gYqJXQBEkBYN2CnnZS2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
دربی‌بت؛ جایی که پیش‌بینی فقط حدس نیست، شروعِ بردهای واقعیه!
✅
با لایسنس بین‌المللی معتبر، وارد زمینی شو که حرفه‌ای‌ها بازی می‌کنن!
✅
آفرهای خفن ثبت‌نام در دربی‌بت؛ فرصت‌هایی که تکرار نمی‌شن:
⬅️
۱۰۰٪ بونوس اولین واریز؛ شروع انفجاری
⬅️
پشتیبانی کامل از همه ارزهای دیجیتال
⬅️
درگاه ریالی و تومنی امن، سریع
⬅️
برداشت‌های آنی و بدون معطلی
⬅️
پشتیبانی حرفه‌ای ۲۴ ساعته
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
✅
دربی‌بت؛ بازی کن، ببر، لذت ببر!r27
🅰
✅
https://DerbyBet.com
📩
@Derbybet</div>
<div class="tg-footer">👁️ 6.21K · <a href="https://t.me/funhiphop/78089" target="_blank">📅 11:40 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78088">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KdF8VDkTJWpN--KXolwMVuGS9EwPFnqingotffNF2j5lulKwpBFZa53QrDSSNwgHRoMQQf_wK860F4Vmjp6OaWH_sTpbI23RgToy8721JU_tDmFljKgtA4YKu_DaoOgmVRgcD0BsZwOQsXA8iG3fLpTYRCGpxbT-04hJz4jmVtBy7QrcfdXVrG81TPtWVO7FrQcEAMcAkN1tGeggHK6D9vSzTIfsaRF0tR4HsD_NjOrs0ELS6VRNXKeklSoRXnbimyEzRie30OZPW_I6o_83qbsfUuyLJF3coUdh0wT1-Da6CXWC8YozZHRN9x-z1oJV2ReZwsqk9MGETv2Bra0kyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمایت پدر از پسر
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 7.81K · <a href="https://t.me/funhiphop/78088" target="_blank">📅 10:14 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78087">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MYx81fIi1ds0Aq46P3vslxSua8OUP9eDDF-Ou2fMsGeG4XwUgi1FDIKAMhmssBOoXTzaRSCfcDky1X9Xn-8lCtp6Kc6AUdu7HtnJAIkq2silaLPHDrTVGg5zIuuf3-rY3QxYn2fhR1HIowgtZuYx8zQvXO0dur_VFFqsiymDHY2VTVGdMgzaYmuEZCDVQhc71x6XelrASw9Go6poxvy16WvEWTNHZjS1seAjtG_WSMh_l4Tg-dgEPP6KNx8KwinLEdZZ0navWnDEElQnXzxixeKPjsuJOqgwYyFFP1k7w9kPzFfpZLLDMuDXjZUJj1KAMGVPZKCi7X9W4Y3ZuOG3OQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قابو دریاب پسر، یاخدا</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/funhiphop/78087" target="_blank">📅 06:24 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78086">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">حالا رونالدو مصاحبه میکنه میگه نه ببین گروه ما از آرژانتین سخت تره
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/funhiphop/78086" target="_blank">📅 06:16 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78085">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">پادشاه فوتبال تعویض شد تا استراحت کنه و برای گاییدن بقیه تیم ها آماده شه
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/funhiphop/78085" target="_blank">📅 06:13 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78084">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">نویسنده کتاب فوتبال هتریک میکنه
🔥
🔥
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/funhiphop/78084" target="_blank">📅 06:10 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78083">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">گللللل
لیونل مسی
کارگردان فوتبال جهاااان
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/funhiphop/78083" target="_blank">📅 05:54 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78082">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">بهتره برم اول وضو بگیرم بعد در مورد خدا و اسطوره بی بدیل فوتبال حرف بزنم
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/funhiphop/78082" target="_blank">📅 05:49 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78080">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">بهترین بازیکن تاریخ چییییی زد</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/funhiphop/78080" target="_blank">📅 04:51 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78079">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">سنا با محدودکردن اختیارات جنگی ترامپ در قبال ایران مخالفت کرد.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/78079" target="_blank">📅 02:05 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78078">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">خوار عراق رو من گاییدم
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/78078" target="_blank">📅 01:59 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78077">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">هومان بدبخت یسال موزیک نداد مجوز بگیره، تهشم بهش مجوز ندادن دوباره شروع کرد به موزیک زیر زمینی دادن.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/78077" target="_blank">📅 01:27 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78074">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aBPgEWvdz98N1Zv_DTLraUsIzrZKvaSs5EL4NISN4t8g30svwoOvQiR0c73Kx_5Aj7a3-38Uidi-ipDHzkNwk9HwZ-dtZdprBG0BcG7-_cZF9VrUEzGSbCMfeXAld9P9ar9TzN8TEGOUmzFmW8oyVe0BrFrZ9mO7wD5WsOFJsVgyvM2CDHLvHU3yQypiLt2CnF9SH1a3uO8lIXeOlcO_15dB5-gvDFhAJU_PBdggxf1LN1s56uVdTdXNH83ag9mHWcyk22Nf8uRZg0d_LksU4iY6Kde-hc4TwCJnEdBx55tqcqHatEo-5j7iwYurPSRfjlQ7RO9p1yilULihwbIC6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کصکشا از مزرعه‌ای که توش کار میکردین خجالت بکشید، یعنی چی صفر کارت
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/78074" target="_blank">📅 00:32 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78072">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">قبول دارید کسایی که جلو اسمشون پرچم گذاشتن زوال عقل دارن؟</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/78072" target="_blank">📅 00:29 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78071">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/guSLL-OOwuKLZDhAc9Wsca8IjOkENKy-j-_9TMXoUcgVd0yEG4tgQaYCwPc8vjBNDM-ixyOKWVejcv9xFZZ1aHVT5MPIrEDWy6wm_Da0yQx7j4aGL6GWnkOfXtbfyy5_KQyTU3hqSSHU9SeVjfzArSnlFvyvKuNqW1zvCdIjg0GsKceksEwvOKXJJwd4mLGX8OaqQTTg99ZapYJoV2clgSPznc8gH15HdRISjy1uMqNooVYRS931I7JgEkzG5TMnCPGjoZ0woIWQin8T1LNofCZHoCoK8J5GbOBhTe793HeDHsAYHOxOImjlzBWbycfqfNFmzZauscRD8-EbzbOYiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">احتمال قهرمانی ایتالیا از پرتغال بیشتره  @FunHipHop | Farid</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/78071" target="_blank">📅 00:28 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78070">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">احتمال قهرمانی ایتالیا از پرتغال بیشتره
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/78070" target="_blank">📅 00:23 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78069">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">بنظرم از بین آرژانتین، فرانسه، اسپانیا، آلمان یکیشون قهرمان میشه  @FunHipHop | Farid</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/funhiphop/78069" target="_blank">📅 00:22 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78068">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">بنظرم از بین آرژانتین، فرانسه، اسپانیا، آلمان یکیشون قهرمان میشه
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/78068" target="_blank">📅 00:20 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78067">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">گل دوم هم زد فرانسه
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/78067" target="_blank">📅 00:16 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78066">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">این جام جهانی احتمال زیاد امباپه رکورد کلوزه رو میزنه
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/78066" target="_blank">📅 00:06 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78065">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">چه‌ گلی زد سنگال که رد شد
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/78065" target="_blank">📅 00:02 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78064">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">امباپه زد
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/78064" target="_blank">📅 00:00 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78053">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">کیت فرانسه چه خفنه
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/78053" target="_blank">📅 22:38 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78052">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">پسر اسکوادو نگا   @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/78052" target="_blank">📅 21:18 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78051">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aJa1n3a96dCWs7qtLUCCcyqrKJUd6dBRr9mbHUXWg4zRLcm1Ore9iZ2EMIta1_XWTAMxendFdlGfgha0Mxa91VimzXjWf4uBpnkXvwbMShkv-4WGjtjLyVkU45e02DI5Fn-qbKv5rSK1xVkcqRSoThWtu_ZKi3laaDtuUrzOr3cl_qGX0FuYC0ZpcwRwpD5QyA4BQSltWIiX2zUPIAeVMBpTY9UtHjtfqdNNZxSJ1nW7S8ipxM4iwdBZmluGFGWUwBUgglQ46qr-F-WCGJRftHyaBxDCfv9MjbheFQweNPkGk7Ns6j_JHEmidKvKayMDsfaUP5AJa-8KdglbFkXhXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پسر اسکوادو نگا
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/78051" target="_blank">📅 21:12 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78050">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">نامزد های انتخاباتی در اسرائیل تبلیغات خودشون رو شروع کردن
و جالبه که همشون از طرح هاشون برای دشمنی با جمهوری اسلامی به عنوان اصلی ترین تبلیغ استفاده میکنن
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/78050" target="_blank">📅 20:53 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78049">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">ترک جدید هودادکا به نام Best In The Game ریلیز شد.
🎵
SoundCloud  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/funhiphop/78049" target="_blank">📅 20:51 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78048">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/im-Ji7Wzvg4VVPv4uJjFBGgTBn70p8BiVd9Ix8GGJQGr2BI3SnOyh5R2KMDsg23N4LuODIwJyYWIyIuClsQBWYjVxO7gQ3xbICJPXZVPXw82SviOwQSwDMii0Shm_mCvRtu1ZbxPMHAIMC0VxDLR9YpSUXWCuFxlrX1qc1lO1CG-W6cbG7vuVRa8usIjpDoCIGKOnWVL47xoYgmsPPsXuulhqPnyowJ0ZwsNdEIujvMkb2UH8El0g1qu47PUz9AD-fWwJyP_iWkcerxh6qNjdwEJF7efsqYdNbe_8EvMSayvvWgJ1BtgO9bxpo-C-grvgPZdbJl7fX2JTJLMU3JhxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید هودادکا به نام Best In The Game ریلیز شد.
🎵
SoundCloud
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/funhiphop/78048" target="_blank">📅 20:46 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78047">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">وال استریت ژورنال:
یادداشت تفاهم آمریکا و ایران به ایران اجازه می‌دهد فوراً فروش نفت را از سر بگیرد و ممکن است تحریم‌های بانکی و بلوکه شدن پول‌ها و محدودیت‌های حمل‌ونقل را برای تسهیل معاملات مرتبط لغو کند.
طبق گزارش، این توافق تسهیلات تحریمی گسترده‌تری نسبت به آنچه قبلاً اعلام شده بود فراهم می‌کند، که احتمالاً صادرات نفت ایران را گسترش داده و امکان بازگرداندن درآمدهای نفتی که در حال حاضر توسط تحریم‌های ثانویه آمریکا محدود شده‌اند را فراهم می‌آورد. (لبیک یا اوباما)
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/funhiphop/78047" target="_blank">📅 20:20 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78046">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">رادیو ارتش اسرائیل:  ارتش اسرائیل قرار بود در ساعات آینده حمله‌ای بزرگ به ایران انجام دهد که شامل ده‌ها جنگنده نیروی هوایی بود که آماده برخاستن و هدف قرار دادن اهدافی در سراسر ایران بودند. این حمله گسترده با فشار ترامپ لغو شد.  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/funhiphop/78046" target="_blank">📅 20:10 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78045">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lPWbSb9hD5g2tkSjFjHTwNwAJ6dEKNF4-StlZ8XNtaFrXNxRQjUj74FjGWyOKCJT_12GqrOYsYSVpy0H9SlsKlX-YVhoYsEYZ99y2ooAhRLQNnDulOS72dcPd8u0CyMPPL3pocm7usKD6mcZfJ5WmCwmFMYQfxqaQrMAoi7fuPjV3zhFgeLxKv98PQ9w2bv0BkkxKOs_0cBcMBdfdkX3CXtN8Go_q92aMnSlXjgOqtIrO6O7Ba8l1xBWX6cbIzR6GngmkQs6GNeNEM2difx3v_FRcExpbNNxdjjPgZOvLw2JRHx9U_5AmxFKpjKZBoURxlG2JHj6hOe6Hcx_8oiTzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خاله شهربانو ازت میخواد همین الان یک لیوان آب بخوری
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/funhiphop/78045" target="_blank">📅 20:00 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78044">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rAqyBXVxa8BKAcQAkc1QmkIsuMeZjol4VjsaSupo3hbV6SgoNRrdUa6xREe2oNeXrFU5XMGYwq7s6pn2xL7RwmA0vvO6aQeyLOaNeBFC-LLffth1RbDnJejMga4SCTiwO2GSY4RqUeY0T_ZqG6tfCjcqNuYW_zEGAFcXv9wnOQJu11TwTatpvjZjOpt5Z990WjPVT1-JA2J8zr2WeI22RHU76vfh8hmE67EOunu1JybKcteZEq49OalduiB6-dYgdDa3t2c76Uq7VWG1iTsxFImmZusMjxHVa2wgFLcT48upP6ZZNsHJ0QL4RQxT7-8kp_gCkox1JQmAj6jSMNdfeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوکو خدا به دالگت رحم کنه
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/funhiphop/78044" target="_blank">📅 19:03 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78043">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/feGzY7kIuJ7HZUyw6kiGvVSKlbVSvHFmZa3LcposNO87hb463YAYUiAIxhVbBjTR-Ze1h77LzUjLMlsFl7sBRsFEtpgfIC6oECGfrHnqh0mAicDfI6AvUKS0Nf7WCLKlgwCZJiwuBgk1eMeEGTWG5B_HLQYXQZ6mrg7I0gOmeMvqa5-4vhyavexaRoiOCQJRWK5o8Khg-sf-I7I5XCsf8gs6g4Wz0ahxMdOXUyGDpg88KSnNzCQLRpqZqcRE50LUfuhKmCqSdxi6yN1QTrieZwfZwQyuGcVJr50d_4fglqFmEXNmGkzzioGgckwKNvt3shwHKw-SuLvyz_UczCsMSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/78043" target="_blank">📅 18:02 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78042">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gVRpz1zNctG5iPciUD8x3rfIljWR6MJjkBtDCifWCAFU4XXj0x1ZwOWkTXbnscIkh57Lc2N5jd_KlIFOSJKfth35xk8quHuO3PF_qXMp6i5HLb3Pb5qDPU9qnwMjqHvlc4lIoEqvsWnzkvOH1nNyOg8GpACmU3vOPqroZ3HGnxIINjfn4_y2jqOCGaM75RbG5KZmKGd65v9FapJGE_ianHhEdJON2zWnXk7LwJzDjzRRaaxakzF6RqjEpFRgTVqrMDxRbnYtu9QhRGIJwJ8D_ZcLP_qoybCqbCJssIR8bXg01T15Ez73bIYv88SVx_wpyw6SC6Hgn6yivCQ9x1cNCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همیشه تو قلب ما میمونی
🥲
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/funhiphop/78042" target="_blank">📅 17:56 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78041">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">با ماف بت از جام جهانی پول در بیار چون کلی هدیه هم خود سایت میده
💵</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/funhiphop/78041" target="_blank">📅 17:56 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78040">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mjMq2oSlpT2Ow_8gTO2o-Z09mVksn83Eac22qfpGGHX1U73YtCWsgEsZXaBVYXWtLqf_WRSDgqhRToHSniqlFmciE-uGQAG_zDu1cr7-PaOQtGaIhGd_DHKuo9sAyVSmfs8QXPvmhvHHjhHcVYfighQG39BLH47gZZb1_kvx48yuHd_8zcJV-F2CyUhnIHqLUjgRtYXtdsZttwg7bde4OYdXshGCC00E2KgIPQeQwKJ2o7cAiJ27Vti6OEBWIDV8c6qN3LyuwKPj1x8N0_uPLwj3obsmPQa0yPanDugM7DIqdqs-J7MBK_T8uZnhIqP72N7NsluRq6pwj-woMM0mfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
چرا سایت بین المللی ماف بت بهترین انتخاب برای پیش بینی جام جهانی
❓
1️⃣
شارژ و برداشت اسان و سریع
2️⃣
پر اپشن ترین سایت فعال در ایران
3️⃣
دارای مجوز رسمی curacao
4️⃣
کارت به کارت همیشه فعال
➖
هدایا بی نظیر ماف بت:
👇
🎁
100% بونوس خوشامدگویی
🎁
برگشت باخت هفتگی
🎁
هر روز 100% فری بت هدیه
🎁
هر روز 20% شارژ اضافی
🎁
گردونه شانس با جوایز بی نظیر
👍
با فعالیت در ماف بت طعم واقعی امکانات در سایت جهانی حس میکنید
👍
🎯
ادرس بدون فیلتر سایت:
✅
https://mafclub.online/fa/?btag=260368
✔️
کانال تلگرام سایت: g26
🅰
🔹
https://t.me/+3Zxs6WU7L_UzY2Fk</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/78040" target="_blank">📅 17:56 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78039">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">شایعه شده که ویزای مهدی ترابی و مهدی طارمی باطل شده  باید ببینیم تایید میشه یا نه  @FunHipHop | Farid</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/78039" target="_blank">📅 16:46 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78038">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">بازی ۳.۱ به نفع ایران میشه اسکرین بگیرین
👍
😎</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/78038" target="_blank">📅 15:45 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78037">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">زندگیتونو بزنید رو برد مساوی نیوزلند</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/78037" target="_blank">📅 15:43 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78036">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">شایعه شده که ویزای مهدی ترابی و مهدی طارمی باطل شده
باید ببینیم تایید میشه یا نه
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/78036" target="_blank">📅 15:37 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78035">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf7f045c16.mp4?token=Hzo7HNhkIwH_W4Eq-CAVBZP7biI1MU4lyRYO_Rr1FTIP_I9IsLOAgkTID7dconz5bWKSm-bVM9dco-XxyPASPnOIHDKXJS_VHz92nrvVacyA1G2At5dYz8DdUhmhNgVq9ID5FJgYSYgSKuaxPk1Qz5MCyk2QhJMGQffnz7IfUbC6_dUDSBv7UexWOoRvEBR97rCk6mjdCKD1b_zZuig56kf7jQwEFgR_KKMOTQoRQan8yRL_tF5Kx2XWvEGC2Tx1fOSOS6zgHcNqDqPM18JokXOmBbH7Zc5R6oldyEdovupyp-pjniXGo0t6jBQVwY2iiGlqmh727AcIWrlWOB4MnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf7f045c16.mp4?token=Hzo7HNhkIwH_W4Eq-CAVBZP7biI1MU4lyRYO_Rr1FTIP_I9IsLOAgkTID7dconz5bWKSm-bVM9dco-XxyPASPnOIHDKXJS_VHz92nrvVacyA1G2At5dYz8DdUhmhNgVq9ID5FJgYSYgSKuaxPk1Qz5MCyk2QhJMGQffnz7IfUbC6_dUDSBv7UexWOoRvEBR97rCk6mjdCKD1b_zZuig56kf7jQwEFgR_KKMOTQoRQan8yRL_tF5Kx2XWvEGC2Tx1fOSOS6zgHcNqDqPM18JokXOmBbH7Zc5R6oldyEdovupyp-pjniXGo0t6jBQVwY2iiGlqmh727AcIWrlWOB4MnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/78035" target="_blank">📅 14:43 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78033">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eldadfJ0iT8zLBB-wiQd9PMJnJ9p_k2RwqabqKOewwQfIgWtpl9Ewe4BOu1G1BCtNtfzyrzEPvY3td6N0HlU5DFVL3pm47F1tStGP4QWCv7T_yY1sALYw6ayhsH7306g-eURtHEUN1cESW5EVDrlJzY1n7twf6bsLGMlCd0bawRdhfyby1LUXVvU2kgHhlJ65sUXrqWH4xTYJle0BowMCpuJZ_6n8wGR4Nq_B9pv_Epp4rkGuMnMQLThwgbX2aeog3hkS1L4t3Mg3wdrUnObGFRxVyXVLfOA-CbxNzqQXerTR3yuTvozBlc3DxusGX_VHoed8nMfn4xja0s13lcX1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5d3ef255a.mp4?token=IWpp3gypRqf9ltxWtAVXkx6zNjaM90ujZ_RPC6VB6Y248Ka-YQv-bEcLcz2EObAMwtrea5aKdEpc6aArbon_Co1c71BL2gTQlw1k8Yq2qrI7cu6TsbmyE2p6azUiVPgAG6NvMrPgQP8CaC6ltzBGn53nd4DP70iiz7I_eFo2o9m1gl1hX_qez2lRN1DcduNpyZeFqSqFHfgOzQotHirAbDFulV1QaftcCQckJCEzG9NNKkeYvvB-6x7adDVjYVkr5vau2k0tK9dE411uNzVJpyGvbHAMLScPEmNhSqfUBAzOWuQbrekCvavz0Cfs5Z4UPd1qaYU_e7vY4mEo_OJI4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5d3ef255a.mp4?token=IWpp3gypRqf9ltxWtAVXkx6zNjaM90ujZ_RPC6VB6Y248Ka-YQv-bEcLcz2EObAMwtrea5aKdEpc6aArbon_Co1c71BL2gTQlw1k8Yq2qrI7cu6TsbmyE2p6azUiVPgAG6NvMrPgQP8CaC6ltzBGn53nd4DP70iiz7I_eFo2o9m1gl1hX_qez2lRN1DcduNpyZeFqSqFHfgOzQotHirAbDFulV1QaftcCQckJCEzG9NNKkeYvvB-6x7adDVjYVkr5vau2k0tK9dE411uNzVJpyGvbHAMLScPEmNhSqfUBAzOWuQbrekCvavz0Cfs5Z4UPd1qaYU_e7vY4mEo_OJI4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اون وسط محبی هم داشت به در و دیوار شلیک میکرد.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/78033" target="_blank">📅 14:09 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78032">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h-I7rbihEkUZgvF5TrM5V5t_f2vQgCNJHi9Du34F76jW0HH1-uW7tWjBl9ADurr7LkBNAsxBOK0PzvIKBYHuQfv-k7WgxAs4B0FS5OldqmNC1MMf8xvxiZuhO5VrUSZBN4BRgc3NYINDqxbbrl6YRl1fesvLA1a1L7M9ACaxdTMakdrNEHRA46VbHsOdKlM2yGq_Qz1vUEiS6sEExddUBSNCKntIxjXrwZfOHozAx1ZSlVj_zwIzdhCN9YQN-D-ccaPcZ-OmsSk74CSpaKTPKE8Vp48thMkrQzU4Q6vZ8HdgqOjGAXEtWSWwE4zRaFr5djBKqNUMZUMoWINndgXc4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی که از تحولات ایران خبر نداره دیشب بازیو میدید پشماش میریخت، همزمان پرچم های شیر خورشید، جمهوری اسلامی، لبنان، اسرائیل، فلسطین و آمریکا تو ورزشگاه بودن  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/78032" target="_blank">📅 14:07 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78031">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">یکی که از تحولات ایران خبر نداره دیشب بازیو میدید پشماش میریخت، همزمان پرچم های شیر خورشید، جمهوری اسلامی، لبنان، اسرائیل، فلسطین و آمریکا تو ورزشگاه بودن  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/78031" target="_blank">📅 14:04 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78030">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">یکی که از تحولات ایران خبر نداره دیشب بازیو میدید پشماش میریخت، همزمان پرچم های شیر خورشید، جمهوری اسلامی، لبنان، اسرائیل، فلسطین و آمریکا تو ورزشگاه بودن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/78030" target="_blank">📅 14:00 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78029">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">من به اسرائیل پیشنهاد دادم که سوریه مسئولیت حزب‌الله را بر عهده بگیرد.
@FunHipHop
| دونالد ترامپ</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/78029" target="_blank">📅 13:42 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78028">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">حکم اعدام جواد زمانی و ابوالفضل ساعدی از افراد اعتراضات دی ماه اجرا شد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/78028" target="_blank">📅 13:00 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78027">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">حسینی با یزیدی صلح یکساعت نخواهد کرد؛ قالیباف و ونس توی مراسم امضا حضور دارن.
@FunHipHop
| Sogand</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/78027" target="_blank">📅 12:53 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78025">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WTbbw9Y-Gm8Iu-15rUBEQ13A1-YS9OdpxCD7-AqWiMFNCexEnBrAHELdqu2S2Tt0UUHx8uGiT4xM54JlsBLBs9dHSxM-3r74gOODcfgrNMcCngUqI0TrOYuL9UxuU0Jji7QJlZ5IFMLsmfn6XSIim19upojTr6Jj1bFmepNDnJ7RjMLanbQu_9l--j1C7IQYeLM79J9K3WatAruoDM651mt-L3_wbcpmShfDuhKTgtpgUPgqB5p66ytlmsfWXJOzhxaRn7AnSRBPGV_gpVr2tYChOsUNV-Iagc0EcYOQZd0l7K4DJa6n6IGp8FSDFq2Bs5giVxPDzEmgPVXrXUXWsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تنها دلیل باخت تیم نبود این اسطوره بود....
@Funhiphop
| Jenayi</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/78025" target="_blank">📅 12:40 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78024">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">derbybet.apk</div>
  <div class="tg-doc-extra">52 MB</div>
</div>
<a href="https://t.me/funhiphop/78024" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">📲
اپلیکشن رسمی سایت دربی بت
🌐
DerbyBet.com
💰
امکان شارژ ریالی ، ووچر ، کریپتو در کمترین زمان ممکن
🔥
🆔
@DerbyBet</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/78024" target="_blank">📅 12:40 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78023">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UUtQ22D8wTfKtpa249LMpikYizAIEIOpI31tlAb6ZHsOCvXPou7r4V1fzB9V0rSX1I5YMsy5CxuQLif7wq75BYTku9EzSrIyvipWyeDdXQJ72rMhvLMdMn9k06OIENFqRSkzEOu8BAa2zzUp3fDyH3-rpPv12sYGj-_-Js9n9fqxoMIn2ATN8Z56TpPsbpsEQhkmt1Gbu0x2rHFA6-oFBWe2noZgmB_NyQKyypbEgt7yg21DUHyZ7KvjPbEbiqs7mWNmEVUCJcZZGy1da0shofqzqF-i_nh4R7UElweAgFE9sYtIBIIvRgscUBRAETVSI86dLC8gFuaTa5xyuygfFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
دربی‌بت؛ جایی که پیش‌بینی فقط حدس نیست، شروعِ بردهای واقعیه!
✅
با لایسنس بین‌المللی معتبر، وارد زمینی شو که حرفه‌ای‌ها بازی می‌کنن!
✅
آفرهای خفن ثبت‌نام در دربی‌بت؛ فرصت‌هایی که تکرار نمی‌شن:
⬅️
۱۰۰٪ بونوس اولین واریز؛ شروع انفجاری
⬅️
پشتیبانی کامل از همه ارزهای دیجیتال
⬅️
درگاه ریالی و تومنی امن، سریع
⬅️
برداشت‌های آنی و بدون معطلی
⬅️
پشتیبانی حرفه‌ای ۲۴ ساعته
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
✅
دربی‌بت؛ بازی کن، ببر، لذت ببر!r26
🅰
✅
https://DerbyBet.com
📩
@Derbybet</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/78023" target="_blank">📅 12:40 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78022">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">بیرانوند: اون دو گلی که از خط دروازه رد شد متعلق به چین و پاکستان بود و عوارض داده بودن.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/78022" target="_blank">📅 12:28 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78021">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">بمب افکن بی پنجاه و دو آمریکا تو رزمایش سقوط کرد
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/78021" target="_blank">📅 12:17 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78020">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">۲۰۱۸ بود ساعت ۵ صبح داشتم از گل خوردنا تیم ملی حرص میخوردم، ولی الان تازه از خواب بیدار شدم نتیجه رو دیدم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/78020" target="_blank">📅 12:06 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78019">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromDiscography ship(blue)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZH_x9QN6cf28x-htPmfrEky8BtHzIeLrPFHx6rK6GDbYEdIDh8juhQupK5dgvXOAitauvgXpQeQ5HlipqzES1ldNbG8IfrXRsga46nGoOHWtOxp5MeRrylDly3mg-RWevidWLMvxnvyw7PBvMUvl6KI3SjayRBOMEXqaQ5-ZEVcxotHoovPrznAdg4xLnzO7Xc9sax6XtlqnFnvF0DRayZk_rGnggn0BS_f4FZFIa7Tf7ep1QrVppwj5gU8ErZsn-d0FBwdxP0MpK2C2eBF3-FdGSFsCKmmsrwyI9RRqb5vQi5vafMncmgQwp9-JFhdxsrLL8GAIQwRb9n1XFVBB1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Complete Albums Of
Playboi Carti
📌
I Am Music (Deluxe
)
📌
I Am Music
📌
Whole Lotta Red
📌
Die Lit
📌
Playboi Carti
📌
In Abundance
@GangStship
🇺🇸</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/78019" target="_blank">📅 10:27 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78015">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YYByksXqttXtuFb5cfSrUcOE0H0ZRd3V7XEMjC-CGpht2u1utDtDoILUPXILgBZ5aYJ936RwegY7fqXoYnOXBWsSLqW6lc-BpFw9msVKsFGLsRw8kHPnMiza1iZg9Zt_AHkN6BmVKZJ0e8xK8rx8ar7t1939IJZUyF5Ao_3DScV99x2X2xLyxBdrwKzeOg3vTcoYgsRWzlWilRegFNxXElkMjJ8MGaPNVGEwQ6092QEnaiHt4rc2SF70AZ0XTJSo4kAt3R21-JPavnxaKstlztSqnXaL0FFIGSZUxA7uMxX_5-iusin7I6pEGkWALxe7fXdC2Voikzx_MY5GUoDBuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lb5WH9EUZ7ZY_QILzsACJRwsi_1KuRSVZAXHdJOwd4zvTf72QyVygrCuqFZE7HMLU2cO-1rWp8tSJ-bOeu9HdnXUsOdnjlEr9mAWDTplT5_lec_sIR2edkdGEFGp_9D8D4k66RAg70W9EnHI43IO6TiuAhqi0LADdHNDlqr3Pu0hX9QT44T1QfEaszW20Wm1gIdFlWoEu7J_7QgIsGN_Mi4cp0vE4hp31Y6tiLsAgd8E3gUruhts4ysJgWz-eOs7hThpOdgnOIdVyRP_kbrdEHwWvbITnwnhmD7e2GNBVNztjJtY1buUGNl_RUtm191V4FyNlYFDedRTTlyaRVRgiQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/78015" target="_blank">📅 08:10 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78013">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">اینو یادت باشه که همیشه تیم‌های مدعی قهرمانی جام جهانی، تو بازی اولشون ضعیف بازی می‌کنن که تاکتیکشون همون اول لو نره. صبر...  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/78013" target="_blank">📅 06:40 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78012">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">بنازم ژنرال تیم قدرتمند نیوزلند رو متوقف کرد  @FunHipHop | Farid</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/78012" target="_blank">📅 06:38 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78011">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">بنازم ژنرال تیم قدرتمند نیوزلند رو متوقف کرد
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/78011" target="_blank">📅 06:33 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78009">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">شوت سعید عزت الهی از ورزشگاه رفت بیرون
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/78009" target="_blank">📅 06:23 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78008">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">حسین زاده جا طارمی اومد
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/78008" target="_blank">📅 06:18 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78007">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">نعمتی چقد دلقکه
😂
😂
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/78007" target="_blank">📅 06:12 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78006">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">نیوزلند تحت فشاره
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/78006" target="_blank">📅 06:11 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78005">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">منو بگو که فکر می‌کردم ایرانیای آمریکا از ایرانیای ایران آیکیوشون بالاتره
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/78005" target="_blank">📅 06:04 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78004">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">محبی گل مساوی رو زد
۲ ۲ مساوی
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/78004" target="_blank">📅 06:01 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78003">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">از توپ لو دادن محبی شروع شد
با ریدمان شجاع ادامه پیدا کرد
و با جاخالی بیرانوند تکمیل شد
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/78003" target="_blank">📅 05:53 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78001">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">واایییی گل دوم نیوزلندددد
🤣
🤣
🤣
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/78001" target="_blank">📅 05:52 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78000">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">علی علیپور اومد کارو دربیاره
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/78000" target="_blank">📅 05:51 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77999">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">چرا سکو ها خالی شد؟</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/77999" target="_blank">📅 05:45 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77998">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">آقا مهدی باشرف (
😂
) جای آریا یوسفی به بازی اومد
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/77998" target="_blank">📅 05:43 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77997">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">فوری از سخنگوی قرارگاه خانم الانبیا:
به زودی به تجاوز نیوزلند پاسخ میدهیم!!
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/77997" target="_blank">📅 05:34 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77995">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FQHmZdHruXLMPC_sX4IqquDImqEI8ZBWz4tsdViDPCdsJrVYa4iyAe8k8jn3kEsd1RImrIj1WyGdT9jCb85yhyTmMG6dA0x35odkyI2t3yhuurkP2N4mcN34LXSFtHBcK8Uubjjw9IEfZnXHEO_joQ4CsmolMAVjD--Q-jlh097c55sYln9_SSycgDbQIOvZgYI1c7UDcgr1gVIUQbmYEXvIwsaVUJu_7TnamRt9aG0MdB1f2TIN1JRXzn38kgRd-9lsoJg19nsSvMWCxxnL8RNOcEliKkttkkp8_s2mr7my_pb3Az-Yt2xvlofVROOH_fJfIpu2nwNgjs0Fg8bwcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
امشب اولییین بازی ایران که  داخل ورزشگاه بردن پرچم شیر و خورشید هم آزاد اعلام شده ، اگر میخوای بدون سانسور بازی ایران دنبال کنی حتما این کانالو داشته باش که تمام بازیای جام جهانی کاملا بدون سانسور پوشش میده :
• @
TrollSporte
• @
TrollSporte</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/77995" target="_blank">📅 05:29 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77993">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">نیمه اول یک یک به نفع ژنرال تموم شد.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/77993" target="_blank">📅 05:26 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77991">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">ریدم علی نعمتی زد ولی افساید شد
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/77991" target="_blank">📅 05:24 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77990">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">گل برای جمهوری اسلامی
رامین رضائیان
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/77990" target="_blank">📅 05:06 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77989">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">ولی شوتای قدوس>>>
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/77989" target="_blank">📅 05:04 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77988">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">این چه کصخل بازی بود گلر نیوزلند دراورد
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/77988" target="_blank">📅 05:03 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77985">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">استایل بیرانوند دقیق مثل‌ بهتاش پایتخت شده وقتی ک سندروم میمون گرفته بود
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/77985" target="_blank">📅 04:54 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77984">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dL5Op0f0Vf-DYbpsndzwSkfde7F47isOLtlvfS1wwCRjHzr2i7vAzTbuiLGAChXdRwxTFRoSyxNMQfhttzuBgQAa_k1wJztoHnVzL6HDkBjJenD-3w-yB0LsglaQvWbB170RSI1l4I3-8DUf7xg4XovyiZttuXRgeEDrh8aSr8b5u2Cpy6J-rGvwd-bycT26RSOLP7EgtxdMmVRYUvtaplElHIKeKWC4zZHtSR6YMBlogG-o1o1zro5_SR_pa8PfaKTDyicu1Mg3NZIUr7btdkzAKG3Pe3IzRvHAs1mODWZ-Ry56Zd_MSHsqNgdX7mljXkQRy2OLmsh5eCEpp6l4-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گل خوردی ک جاکش
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/77984" target="_blank">📅 04:50 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77983">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">عجب سوپر گلی زد نیوزیلند.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/77983" target="_blank">📅 04:41 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77977">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">بازی یک یک تموم شد
بهترین نتیجه برای نیوزلند
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/77977" target="_blank">📅 00:29 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77976">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">محاصره دریایی رفع شد.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/77976" target="_blank">📅 00:20 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77972">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">عباس و باقر فقط از زنده موندن آقا مجتبی خبر نداشتن و سورپرایز شدن وگرنه همون روز اول جنگ رمضان توافق شده بود بینشون و توافقشونم ساعت ۹ونیم بعد از ۳۰ موشک به بیت رسمی شد.  - تغییر رژیم هم از نظر ترامپ همینه نه چیزی که تو ذهنتون ساختید  @FunHipHop | Constantine</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/77972" target="_blank">📅 23:49 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77971">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rrZ18RMKg_73FWYnYDjdA64amrjzC1tKD2md7bNj0wooIOmJ8UnDJa5KK4Hj9SNq8PU7RzoTmE3ZgQCP6t4kUzva4VpJ9QmTsosDNBFH4b2uFIOG3xz8Yz8JFoW2ANcuPaL-gjVwgkMdEFDHY4UXf0c0Y82RRm7QrTa2pFbR7GthOQ3wpmDT_Puwct21OXCj8HfQ7FZl6Cn4jg_OT1QOMOk2Z3dyr6xLb-60pGGdz7M_NZs68-R2pKFAmig41ljh6oJLY1GiJA16ArILeZ54OInmYNI69iyQGi9pjVXu1t0huFyj-l9TB_aBarfULzjmLlIGkZ0uxcp31tB5oCa1UA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عباس و باقر فقط از زنده موندن آقا مجتبی خبر نداشتن و سورپرایز شدن
وگرنه همون روز اول جنگ رمضان توافق شده بود بینشون و توافقشونم ساعت ۹ونیم بعد از ۳۰ موشک به بیت رسمی شد.
- تغییر رژیم هم از نظر ترامپ همینه نه چیزی که تو ذهنتون ساختید
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/77971" target="_blank">📅 23:47 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77969">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iCnpRyMv1Hc1fjYE2cV1fugTthIWk4PItl-6EVXn8SQYYuWT2rbVojY3GbsNo1TajdX6iD1M1uiQt2O3njLW9094yUSHz5egEE7puekUwJl6sokAGdFgjtmrk5Ps8Pa95eagoIyfY0YX2r2rqQEJmIISC6coJ34L2tOJHWKsf3XrbC3NcksXJ9sLcSwrSd3fubmKNwHtm7uwqJ73JiV4c_FCcJPnmY_uqJYWwutqCFwq344rZrXowXikjyNubwu83CBgdSYI_ATxBQaQqmvr1bNK20PrOVqDLrwMfAnDo9HGxeoiaDJkVjgpORYxcq8T7dQs1nn4N9Ez1Y6LFJZb3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شایان یو واقعا کونیه پسر
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/77969" target="_blank">📅 23:05 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77968">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aEpxCH8z0G_Y7dtk6LUMKM58O5KP1ZTNEvqNxPrVaaWz4jRftK0DXkgpTBXTQ8-SyV8KVklsirOdVBNHYltodLD93-etbq2t0E0NHtjpc3Gt-er-QzazyP52WDG_BeIIdbLca4V5Z91Y2ffoPsdbXFZnR6kQfn6PVzk6eNsdMybp873M_HMKS3K2HrVTZrZc-CprNSfc5-ndnHSScf9G9E5TuA_jn-rmyGm4tGD5plErPMjN4ZEvbBFAWKxWpnaivAaRJw84YqbDzNcfWS-WCRhKG8dy1HELogFHcCCOKbQ9wVNXBOwJwVP3XT9b_QpNxhOrGRC9ntnsl2RNCncoQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موزیکای قشنگتو بفرست باهم گوش کنیم.
🎵
🤍
گپ پلی لیستمون
🌓
https://t.me/ORGplaylisT
https://t.me/ORGplaylisT
https://t.me/ORGplaylisT</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/77968" target="_blank">📅 22:56 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77967">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">امام عاشورا برا مصر گل زد
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/77967" target="_blank">📅 22:52 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77966">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">زندگیتونو بزنید رو برد مساوی نیوزلند</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/77966" target="_blank">📅 22:00 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77965">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAmir</strong></div>
<div class="tg-text">اسپانیا بدون یامال در حد پرتغال با رونالدوعه</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/77965" target="_blank">📅 21:57 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77964">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">کیپ ورد جلوی اسپانیا متوقف شد
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/77964" target="_blank">📅 21:40 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77963">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">ریدن تو این بازی باعث میشه اسپانیا خیلی وحشی شه و بقیه رو بگاد و قهرمان شه
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/77963" target="_blank">📅 21:26 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77961">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U3mUZF4EedvtaaCNPjCqwVVKIdZ1K80aSbz26w34FlCcdPtvODi17IH2Olrk2tSdHc_GZ2XJMtS2abZvOLqo9LJOzyKDulsjJ8RoLN3PrtV1WNVNwnLeXTl7AjSHZYzwZdrYtoTTdi2Uad8Pjr11y1yYfW4eFmY-JKTCkgYemgomuQge1oRBoTmD1D0_4XB0-rRZJq8PxwrKTTgug07HCRTH9QkLlZPYJkufZO9lBI1wbtQMVplYr0EZAU1au5HU8hJgsr4RLUQdyeEvmR76Z-F48oUMwPsGIXzmNBGIwbjAdZfvmW4O4mqtQQl7Wj3Ry48dO_HBFNuJTkS_fEQtyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیانیه جدید باقر شاه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/77961" target="_blank">📅 20:59 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77960">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">آپارات اسپرت با ای پی خارج ایران هم بالا میاد جدیدا، اگه خارج ایرانید استفاده کنید.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/77960" target="_blank">📅 20:08 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77959">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">قهرمان جام جهانی ۲۰۲۶ خیلی ریدمان شروع کرده
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/77959" target="_blank">📅 20:03 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77958">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">آپارات اسپرت با ای پی خارج ایران هم بالا میاد جدیدا، اگه خارج ایرانید استفاده کنید.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/77958" target="_blank">📅 19:57 · 25 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
