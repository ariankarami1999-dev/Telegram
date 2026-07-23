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
<img src="https://cdn5.telesco.pe/file/YDgGIKeUES_mT1P4WbRXqIWyVu2jye9MQxJXLTgqJkjohUcaDUc4z1Bghr96k_6trDA9IWW6tq4nYtIy2_0s7579sc4j0aI1vds7jbHKg0AM1eEtEGZKHdTsgZk6aUSSafK6pJKtiA76qG0wSP3NOF8nFiWSo1gCUDFU5ImKjpiZPVcAC8UQGjnPEy2OEReTvd6wZWXvXJerl7sTpqP-1jwHXjgENYE_8fao6po0pzRneDXkdxwofxVHfCskWG9fDgbd165C7fxLXXoe_RVVzlfsOQCaHrBG8kiXGVYp-EMY1mKcC0w46on4BrcjjCMkXmTtGPNkTHgoobanHdzhLQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 540K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-01 08:59:21</div>
<hr>

<div class="tg-post" id="msg-101617">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CRA1i6EiRCtohnJSDyV3DVwmFW-2R4B7bLnoZoWlvgSG8zeleTVghG0pIuRPO-DVFvNvjmWpIe4vJrcY6RrPR_eclVfuxbxvGh_GxQ5gyHWJ7x-Vh37YkYWZVOsyyxm8Tg9Xdv0ESzcO_dGVXWsRRAfmcUzliYroh-Ut_7e7iXMS5Qx0qtxhfHMgSUOyltScoRDkKWV-DCCD5OVHZneBsGC8pfqeqlfwRoaWYWD07lSXO1vmUWPWcxhhEOrkHpkar65GyGhV8I2wKVi2xBDJRWJ5l5SgYcZ-lxBemj6mLt2WU2ECSaTFWr--nIrs_Qg72mHgQ3RoWWoZwfT20FWwpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
فابریزیو رومانو
🚨
🚨
🚨
🔵
⚪️
منچستر سیتی احتمالا مبلغ زیادی رو برای انتقال رودری به رئال‌مادرید درخواست خواهد کرد. حتی اگر فلورنتینو پِرز موافقت کند، باید دید که آیا این انتقال از نظر مالی برای رئال مادرید امکان‌پذیر است یا خیر.
🔹
🔺
رودری هنوز قراردادش را با منچسترسیتی تمدید نکرده است، زیرا منتظر پیشنهادی از رئال مادرید است.
💣
💣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/Futball180TV/101617" target="_blank">📅 04:54 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101616">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf2512ad65.mp4?token=jYhDaeQLDFmxk34XHVLKtkUuqdyiHqw9Uk_J8j8ZMcN4cgRx3LEwNhR8uggh-RosFZgDdr6OPabLYJ89NWzjkFjSlxdtTZRGAFPk1JLZhnNywqWTenc66JUz1qvY4c0yLB4YBe_QnQlWgBDXaIeb5lTZynPRyCVGoGmpMgrEVJ3iIvEnCLLqSqSZAk5GqLOQ6d93NLVB0xDRFxkmFnKA3IChUTL28LG4hQrBq70jtWdwxWGHbNUo-mlGaHRc5U17t67GSk8gE8oJh1ZCh8A-eztQM0XWadV08L9s-tq_BTB37UlRzHI4XOUOA-baqRwwtUrNgJwla4CU748FRHhpjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf2512ad65.mp4?token=jYhDaeQLDFmxk34XHVLKtkUuqdyiHqw9Uk_J8j8ZMcN4cgRx3LEwNhR8uggh-RosFZgDdr6OPabLYJ89NWzjkFjSlxdtTZRGAFPk1JLZhnNywqWTenc66JUz1qvY4c0yLB4YBe_QnQlWgBDXaIeb5lTZynPRyCVGoGmpMgrEVJ3iIvEnCLLqSqSZAk5GqLOQ6d93NLVB0xDRFxkmFnKA3IChUTL28LG4hQrBq70jtWdwxWGHbNUo-mlGaHRc5U17t67GSk8gE8oJh1ZCh8A-eztQM0XWadV08L9s-tq_BTB37UlRzHI4XOUOA-baqRwwtUrNgJwla4CU748FRHhpjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🎙
⚽️
خاطره مهدی قایدی: بیرانوند خیلی خسیسه. یه روز زنگ زد بستنی آوردن خوردیم و خودش رفت، گفتیم چرا حساب نمیکنی گفت فقط دعوت کردم نگفتم حساب میکنم
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/101616" target="_blank">📅 02:15 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101615">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PsAXcR-s_olgEOWnNWf-OKCBCqSG6U6YNWdRuueK0oLPslTLrQY3aQrY6R0dTv7poMG9zfaSd5R_Wsuzw4XanyPPq9L5E5Uvz5ba0PvUHgwGoGMljfwrHIsJ6HTapN1lbtjBdvbcCXXc8Ix9H26TFf5O9aioAWo6X66oHgWlhqyyTBRKPLIC0BidupI12VxiITKBJRnbFgXfmTdRbFsXs_RLetAmSJrX8RV81DoJoLdApYSjk_pQGHm2y3ntX1WjKiJz9vbGK3I2bT8lrwuJAEpr2kSRewOl-VjU_benDmUe2ls9rHDgsfkmBQtsioJPIAaFEXRk_bxLkeZvEofS1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🗞
منچسترسیتی درخواست اولیه 100 میلیون یورو برای فروش رودری داشته. با توجه به مدت‌کم باقی‌مانده تا پایان قرارداد این بازیکن، رئال‌مادرید می‌تواند با رقمی کمتر ستاره اسپانیا را جذب کند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/101615" target="_blank">📅 01:54 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101614">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qNzb0TmAJITfMIfkVoRGtFp5GYAAgJwjwRBKbsMuHWKJCUZgNAE062O_GIVyGWGHe-653BgrngkIcs7VUt5EvJTcYSZQyKfABjBBN8Fq6EnZ50uIydOrOlNwxbdhp244D0SSqUAnWhK85mNp9xcOS4ZhnM4J5vgUFcI4-v670shQwdzbTA_uOQKuTJ5_kz5qJ7AuKFMQdMA-hNqw_wf693IkdAWqBIyZxFH7nXiJL20wdhACWaIppB3ludi1g1HDIaFCQxqnR5FqPouRr7c_cVPZe094a3DduP0AkSfUAS4_-qan2aBQ3ieKitTA5VIu7yS-DQy0U1XLAmLPjGizIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🗞
منچسترسیتی درخواست اولیه 100 میلیون یورو برای فروش رودری داشته. با توجه به مدت‌کم باقی‌مانده تا پایان قرارداد این بازیکن، رئال‌مادرید می‌تواند با رقمی کمتر ستاره اسپانیا را جذب کند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/101614" target="_blank">📅 01:42 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101613">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TzpDWBjsu4wttz-l8MdcBMOH6PbfronuR_YfcP6jNwe-frab7qEG6SfLpU3lWz44jxH5CyCOFYMB_0rPvNb2wYPgkKjQGwaGkORNoneVuRKpKcXcKniovXCbo946PdYRqQQ-cYAmv-6l_e1OU_BhVT83BNBv9rez5Wl0mgv2COUsBDNuaY39940DMiylt6AGCJA5NTcW-DUT01rUas2tD4ZbXjmXLh_UfZhVkzH2oRdGAvxBbOkIyd7ILYlJTfNmlnbQeGHpWNzXmV-T9SgQJc0MtSXS2cKBCtydx82PCtUwbkiHe3lloHbiOsW4NZPVx0WY42LLoUhkO1PABjAswg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیوید بکهام از تبلیغات تو جام جهانی 22 میلیون دلار درامد داشت و شکیرا 17.5 میلیون دلار
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/101613" target="_blank">📅 01:15 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101612">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/krGP69CagstrhK3_rpQY2fd-zVrvnrAREuO8xp2CKbgn2vfFA0dFMBLk8bEJ-q2OrT5LO-RJ8Xcp83M_eEfJEL9e3hdg41GFhhLLjWj3kEP9hGGeHpWrL6NXSKtrj8hAyICIguRL_mImWy_3dnZEwUdLU4Ubaw9K8AOZPVmw7diZCqqIFK7AhjS4zg-xfMoZHnx__64L-1qtvttlSAzRWU4e422GSAVj6uuwTAeWtv930AH0ics4KyiyB_25j5PTKZyC4P4u-AJ6i1RKZE1uqSxtq_NmT1XpMoFeKMAwrp5lkC0jTt7cA5mZqShl7Kmn9au9TBvFu4zDCnphaM9Eqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فقط 3 بازیکن فعال حال حاضر فوتبال این افتخارات رو دارن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/101612" target="_blank">📅 01:13 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101611">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FK0f2y_l-H4Jedv-TNh95OaJvLNk5ugsKkUnK1d2_Pl4JDsnPQTyDOZg1ki9nDv-uEu-LBfFXBjf2CaZPYyS5JSWuj0-UsSc_Bm51ri-sm36_57gYaBfrq7LKd3PQ3XfJ2fmdOzMk14-MlZO-UtCEf7LdvN7Ci0O0K61VFeK9btHW3KwfRNvq0QiY_pvfP3sgeFgbc9nIky9jUsUDy-441kavsIIpSV1R56lQVRdO64-LPPvdT7756dEJcGk6JCK7tNCembXCYEaPYJUfM2u5MNCYSmJ8IXJKRW8uS6gZp6uESrm-9tsBUtjve0UdgLdUEbhXDu-Gs0Abkx6GfDZ5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آنالیز
دقیق،
برد
تضمینی
!
📊
💵
حرفه‌ای‌ها دیگه حدس نمی‌زنن، آنالیز می‌کنن. توی
Pinbet
، ما آمار و ارقام رو به سود شما تبدیل می‌کنیم
✔️
با ما همیشه یه قدم جلوتر از بازی هستی
⌛
روی لینک زیر کلیک کن و تحلیل بازی‌های امشب رو ببین
👇
🔗
@Pinbet_official
🔗
@Pinbet_official
🔗
@Pinbet_official</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/101611" target="_blank">📅 01:13 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101610">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NfHClRqUXn5ljKMEKvbdTa0G2fT2dgOb9nKfeo0T20qnSLXwHcLC2Apc8wiPXCG6QG5g9QG0HzEVdibI7kIWQ5TPPa0SIuB4tXeM_SUKolAKJBYKTjwHCz7ZKFkDl5SldBbVH9Jp3p_hTPmkDDmMrl34g_k0LqeypoYZv090T5xSmNxuJRsckSL508szl4Z_Br8KkfvcJP4fGCY-X6BoCbQCPAna2b1a8YVub_GyNhPSc0KslfyiyFfBl82sbEeVwpqubPZVm8SobLx7vbLvJXGGc-C4cnAHQQEmb6vKhvZUo2XT1NJdPy40vE_phtAib9XAZRhxLOuqm-taY7PBTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
کیت‌لورفته جدید رئال‌مادرید که قراره فردا رسما رونمایی بشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/101610" target="_blank">📅 01:02 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101609">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🚨
⚪️
فووووری از پپه آلوارز: رودری با قراردادی 4 ساله به رئال مادرید پیوست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/101609" target="_blank">📅 00:45 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101608">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mEJgF-00RqzjhmIKZP4yr21nVZ384l-0_hz7tNe3jFB-tTbgsHTllZJtSP08yuQx2mkDwZowhSHHuxrguNAYeCy4p49PzOfNqyf2RxjzTbDJHmI16bA56FUSJuyj2O2nOWh51HtdNkw9gXX1WE7MfXVRJwczR-yHfkqIp5wctVShIKnfHNNW4GRbNkYoy6ICSQtnSeW8jJeTY0MnxAP9Mbv7rDbfjsn32tOe3Xy7WbXJJQx3wnaR6Wqz_7ulTBligs6lJdqafkN0F1KuYV-aOopI7YuWdr_0gTwkdO8X0NBGArD6nScwWyTVgMUo3Ahves3Gv8BWZQKj8EDnznbozw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
والنتین بارکو با قراردادی به چلسی پیوست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/101608" target="_blank">📅 00:45 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101607">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">‼️
▶️
👤
حمایت‌جمعی از مردم فارسی زبان آفریقایی از عادل فردوسی‌پور
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/101607" target="_blank">📅 00:36 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101606">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#رسمیییییی؛ باشگاه آرسنال رسماً اعلام کرد که با کریستوس تزولیس، وینگر یونانی، از باشگاه کلوب بروژ قرارداد بسته است. مبلغ این انتقال ۴۰ میلیون یورو است و قرارداد او برای پنج فصل اعتبار دارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/101606" target="_blank">📅 00:17 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101605">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GVerz-TBpR7RioqH4lldukGhwu9ku7FocDka7LR91bG0OySzpIB4JLi42yWGahYoQvsnSA0uqeVD03-UQ6yDSeIZ5Kf8hKreiGY_EVv7M2E-AW5Dx9ShxO214fJOwZ5GeQ_f8WZD8nStjUQJNI-pLUYHQsketZHTr5ZxGlLL_8Jsz7TEslS8TaevgW2AvfRfzw-vgHuQ4QqbPz5ZxPdwFFHQrjpNUydOqqLWZN4cwViemPBpzgb4YUvaopySD71obA92WCX8HZ91a2EppThnIyoTkMJgQBDaXPnpELaZzTY5mKublcL-HntMEBudkrzGD9YJbnd_4N5X83iD-T23xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#رسمیییییی
؛ باشگاه آرسنال رسماً اعلام کرد که با کریستوس تزولیس، وینگر یونانی، از باشگاه کلوب بروژ قرارداد بسته است. مبلغ این انتقال ۴۰ میلیون یورو است و قرارداد او برای پنج فصل اعتبار دارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/101605" target="_blank">📅 00:06 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101604">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XcPiwY9YYwsesXe9j95MOtaqc-RJo37WvlL4PpTZA-2YH1qNixE_weyEVU3YgoSTpjFiuxs7A8uukqf5XREVonCALXyWxXYNBwUfw5gzT2mBUUka1crVUEkzF6Y-w2AiVLY2Sez-dgg6MLNZM3X1KmDPNFFH1tLPMyDmU_q_iNGOUyA-k_G6QLeUftAkp4KZ4F_8pIXXvxC16tXuIgqCihmRTW-Gx6V-zy0ZYKaC2VRtlqPLAkiNvoIlULad0gU9qxWUuu_uond5HB9Sk7m7BPHuBLe0vfyDqJNYDFTw2cr5eZkfnGochNgIkBDIN3KgxAcew0Lc8kLhQwaZtQnpWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
🏆
ده‌مسابقه برتر جام‌جهانی ۲۰۲۶
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/101604" target="_blank">📅 00:00 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101603">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jTkUzluyAThA6QEEXr0KH_qCeRVoRYDkViAuxkCmC68wl93d-J7k6KAj5QcunmdsiSyKopCqJjmp4CHHpQLB0qaIGQ1vXNyuFmfCQqG7zcVBULQMpLXpf3cUtEJONq_ygHxuBwjkHoDMoy0lWarRn3Jsvir5aY2aBAbW9Hmhhm04cHl0PCiMv_qgazyWXxYb8uQOu_Q31cJSioLB0mp_MH25N7ZzgQWjWCezRO-vij2sgMVIfX9KvA81OlsMbRCSDkIPu0WAJCejl3A12L9IRhy0-dv7ctpvr_3cEDmMS3l7p85GxhWwEjrrH9dOKlKAWjVBA5U18WKG8Lpeu-n9LQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
بیانیه آرسنال: ویلیام‌سالیبا به دلیل آسیب‌دیدگی در ناحیه کمر برای مدت طولانی قادر به بازی نخواهد بود، اما تحت درمان قرار خواهد گرفت و جراحی برای او ضروری نیست. او فیزیوتراپی خواهد شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/101603" target="_blank">📅 23:36 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101602">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KxAV821xSUTs-UGxsL7dpvieAhExp-Ws_KTkCPacvouFavZPNmKOhfwqZwbEOlfU6hPY0icobBk5FbydLiTbOENBwVp8F8xa5Vcj8Uigoqg22tsvl81egG9nu0uWJ9BeltN6J9Q7c1nZenwwIZ1cL9jZ0z97-DWbKz1wDdumqLG7ve3cLHIDleMx9Q9Y3ZNscIf2WQqaiHhDMFoxi3RUb9SAGwNY9hhpzAV0h-SSCbcM9EE3TVo_vwlR3Pz9L2SCuC5UZWb8AfLuUYJX5Uqil7eKhmER-heZ5aA0OnWuCIJv6K9y5-pWvRp11U3u4KBllP94NAe1FAGEsxlW515VeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
توصیه‌مهم صداوسیما به مردم ایران؛ فقط کاش تجهیزات هم تحویل مردم بدن تا خوب بزنیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/Futball180TV/101602" target="_blank">📅 23:06 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101601">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NGAuIJ3M5B-JgrH_3CAICG8fFI04GDI7Zu_IEOEE7Q_nTkt7fG-42OhKlNcMw6fNFZ5kWcpoIWbu3RtV6QUlp4bx1LoQmg5Gug-DlW752fOWhjiLTOzR6-mO9Boi2PoAwKpIB9aZSW4SkMvLjca_sgiBxJLIhdXyLpE6nBoh7GI6TayRvIDv8mZZFft-GP_FFlriv7TLPYLmGXbpXMSW_oEITUaQ_PAWG-ROUzZtdpd10oKJznWJ21VKefDDlBJKdWMo0VzYAu4cKF0DjVWHuTkUn3ly2o0VI3c17XgfR44OSU_oiaiezJV3_4RhdyQxlZRkXQOtCKL4Xj4O4Rcmkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔸
🔝
ستاره‌های حاضر در لیگ MLS آمریکا.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/Futball180TV/101601" target="_blank">📅 23:03 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101600">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cbgumHywUy70wC_bO2ZVUVTbrJDTkodd8wxnZv4LxGuQttTr1ITOCehcKzN0VKqyHvWD-9NAGK9JiYHBBlmCKtiXtHXT_eJY0zSChRBhrGKeodBLIn-EyJ3qWHgmcrbgYweZUSbENzhSU66LMsbPlmjG_JEAkCQh9XVSjrhyKVeGLbTS1sci25uMFxKze0FbC7xstD-albKY2dF7f6E7u9n5oG0cod6rgsZ_4_KW8lYDOicnwbVjRq5_X18z7xswDVy_9PZavKgC06An-A3mcjt5fWAqKYdNQUYSrfsb0RwnZMRwByr14APcg8NH9OZZsNN-eLRdp1P2cZVmRU9VCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
فووووری از پپه آلوارز:
رودری با قراردادی 4 ساله به رئال مادرید پیوست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/Futball180TV/101600" target="_blank">📅 22:38 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101599">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZYdIvgI2Rs5dWzHrWXB03Gq52jd73TUEpu0gacLNqExdyXlx7P-LuoGWHRGrqXOunCExu6WTaciCT2W30bQgHNnwma3cGFIvU2EtD6gJaRpNZMbQH3JpeHUxPlJJnMgWevw85i1ZB4cPzfoWhJrFaPU0IWfjyYaCMZqMUFl6bGnfl3KhsP_CkaqjTnSbimmrTM254Vxy7g6-T4qrUwgMXAlpXeQC137Korjrw8PdYKPt31rmc4zG4_kzeKBOvqdFGEQgITGEyeNRSiLAi1JfwD2GDYYT6O69shXIKmgM8BVffdMaG7715Irdweeec8eIw11VVWSX5gE4dhnbtMn05A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فووووری از بیلد آلمان: کیلیان امباپه به فلورنتینو پرز اطلاع داده که موفق شده مایکل اولیسه را برای پیوستن به رئال مادرید متقاعد کند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/Futball180TV/101599" target="_blank">📅 22:28 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101598">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jJBgW1j2FkXXsNdO3toeS569FtVQtt756Imht6csytsc2Gi5wWGbRf_D5JYQXO1uIlfKoI8cYe_t6p9LDxFczwrvlY1UhaB9OfSdMcEKVR3pTlNp65AzGCze5DjOShTT278ljeRk2M_Pg8KasF_S862qJQSW-8NmQR-qQ0tMlHQ-onVap-u6pJI_IrAnegcpssBQptczlC2wbjOKP1Rx9YceelS_9j1saddkdrGrQFcpvDl-4QDwrRcY6_wSoKfaOd1rntHagqON0u5_V8-m4EZXBy1laNPUT4tmbLwzvguc-o5D3bTU2zUHodZRu9bm0ZDcw98ohHV3S40DLPb6Ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مشکلی که وینیسیوس این روزا باهاش سروکله میزنه:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/101598" target="_blank">📅 22:25 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101597">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XpuI5fC9tMalj-E456SJIu6G7lCEkqMzbXZqlkbQj63HwMlXlBkvPP4jYTTp6n3XkV-3ZFp8tL4DpqfN0GdUd_12z2Kjo9K1UGLe5fBq08VX9RZDVX1lHJeS-Ujl4g5C3ZSwGX8H5od4fn5fn1tmmu8hNfGM9DX81r1pbubg4LSDaXgd4EKUqY0mVzxfZfsCDfI75Enb7Fohm1CxNI3v-Cb05BVEAnmRWkOJVqGFZAeNG-QbVj59W63dJL6dRE1KPKvaGNUjsKpO_faUdBQejX58J0MUenDNlbauCu_lQK0a59VlPwQse80ga_csKdsuMn1E_JXumVWrrVCmcrjMTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
فابیو کاناوارو:
اگر من بعد از قهرمانی در جام جهانی و کسب عنوان قهرمانی لیگ، توپ طلا را بردم، چرا پائو کوبارسی نتونه این کار رو انجام بده؟ به نظر من، کوبارسی فصل و جام جهانی حتی بهتری نسبت به چیزی که من در سال ۲۰۰۶ داشتم، پشت سر گذاشته. فکر میکنم او بیش از هر کسی شایسته بردن توپ طلاست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/101597" target="_blank">📅 22:01 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101596">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QR4KxT1KPoSzzsMvHkGjby-8UcdIzFKPEYQj9A-rKq0DRlptww24o7hZhVpS1bxPLaaoCKPePewccqc2mCm1tBjNib86xOQnFrfxd_T8cmiKji7-lLumOZuRaNfYbzbMCFIysCWr-Z87hxlbpXbFSbw1koO-UTdIjz9cBwVRYj0gihas_ZY4m11eckyS8tVinGJVnKjLVNx-NczMFbCpqFIJnbJXupuACEmDN_2Go2_2nGDTZku8QHlb5I7qEjIO1fEafAPtcx5XhLCyI235ibM253PvwsZfd3-Hx1qJi8wE5KjZPEChdGEQ0-ekCc9-44JjwrAhKRZzWg5yVIYXqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
🗞
رومانو: سامرویل ستاره وستهم با مبلغ ۵۵ میلیون یورو راهی الهلال شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/101596" target="_blank">📅 21:56 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101595">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PN23a62WMQrZQeGRlt-dticzIUqDy7Cc-jfvo7mZ_B1pIYJc9GdSeP6J-puqiQcOAj8dLd38ixVmrVeCkDE3qo0PptUn-8eGCZNQhijzp9dWhlrLv9aPJdyXON5Dl8N3x1L_K3iBeqquPwAUyEG2XYKIo3CI_PJ7O3meB-vLH1auVIRqpyeM3_Y2LURFKr6lcYfRHTRqKlk1u4z_UrVyPAAPhDqH85Cw6kbHIJT3TzV5S9UY-TiuE68oEJGCMvgyN_QN6zQ9GdrEkq6ii4-czxtKB3GiY96S3iTZnBZ_6IP5lcF72EB1oN59P8u5xu1D0T6Zwj7NFhCGffY84s0Pkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
لامین یامال ناخواسته بعد از فینال جام جهانی یه تبلیغ خفن برای یه برند لباس جور کرد! او چند بار توی بازی پیراهنش رو بالا زد و لوگوی برند آلمانی 6PM رو جلوی چشم حدود یک میلیارد بیننده نشون داد؛ اتفاقی که باعث شد شورت‌های این برند خیلی زود بعد از فینال کاملاً فروش بره.
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/101595" target="_blank">📅 21:30 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101594">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RBwG3h-pPC6BmkPBsiZdl2FSP031rTtc5UsO7dyVyDjdkkkoAYDV7YROIJEoOuVGwAjFles258JGTnUDgbKXkd5bGOGMW6x4tzQNEYNDeoiecfB0WiWilp7Kcq99x4PGl86B6jWQ9Muxf2mffWzV7N6jZmeenTnwTtJSRO1UjTetJ85R9TXnHgSnB5aOCjkRb7RF7CFn6OD5oIrJwqk5kKTNEip0Qv2J6o8lJ-eSbxQUE1aAYIIBmQTXc1hWb6_5FZveldZibJ23W3Nrs2fpwEICfXgAXC0wQn1kEDRYCLLD1fG-Lw_qGEXIpDtqrHx8dzqzy4IpMOCS2dM42v9MOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۶۰ سال بعد، او انجامش داد!
✅
📊
کیلیان امباپه حالا:
⚽️
🥇
آقای گل جام جهانی ۲۰۲۶
⚽️
🥇
آقای گل لیگ قهرمانان اروپا ۲۰۲۵/۲۶
⚽️
🥇
آقای گل لیگ داخلی در فصل ۲۰۲۵/۲۶
تنها اوزه‌بیو
🇵🇹
پیش از این موفق شده بود در یک فصل، آقای گل هر سه رقابت باشد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/101594" target="_blank">📅 21:24 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101593">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🚨
#فوووووری
؛ دیلی‌میل: نیکو ویلیامز ستاره تیم‌ملی اسپانیا پس از تعطیلات احتمال بسیار زیاد از بیلبائو جدا میشه. آرسنال از مشتریان جدی این بازیکنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/101593" target="_blank">📅 21:06 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101592">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76aa3864d3.mp4?token=TZuxHIgSJ334bfiW_VzB_vKZdgHnGpZwunRK-cpaTRrUmuqC1KIEmpNJ35CwkytHEIjZQRPGsvtfq1aMOUr8lR-U0n68BGz1C09Z5OsCXAkY_ImZSiBhsvQN531ShfZ1B0Jj9yNYdVUDcD6-s8hULEkz0KbW7ZplKSEbHu72RW4xwFbGHMlTZvde-67ANcUD3kWEk2pVRIqWBdZvUISH6QtDRJqwXr9y5lDRjMj40GWZjq1MG25WB9t-0fBps5wLyGQnVQu9VuHHcRuh6gh6o39EBHqbXVWLoDJV2AAf3dIFT0tn6ljbeyJI8TYCknff63qywgBhgHr37rGXGYJvVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76aa3864d3.mp4?token=TZuxHIgSJ334bfiW_VzB_vKZdgHnGpZwunRK-cpaTRrUmuqC1KIEmpNJ35CwkytHEIjZQRPGsvtfq1aMOUr8lR-U0n68BGz1C09Z5OsCXAkY_ImZSiBhsvQN531ShfZ1B0Jj9yNYdVUDcD6-s8hULEkz0KbW7ZplKSEbHu72RW4xwFbGHMlTZvde-67ANcUD3kWEk2pVRIqWBdZvUISH6QtDRJqwXr9y5lDRjMj40GWZjq1MG25WB9t-0fBps5wLyGQnVQu9VuHHcRuh6gh6o39EBHqbXVWLoDJV2AAf3dIFT0tn6ljbeyJI8TYCknff63qywgBhgHr37rGXGYJvVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
در اتفاقی عجیب، امروز تو پلی آف صعود به پرمیرلیگ مملکت مس رفسنجان تو زمین حاضر نشد و صنعت نفت آبادان با پیروزی 3_0 صعود کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/Futball180TV/101592" target="_blank">📅 21:02 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101591">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jc4NnRrTdlKE-dFRh3pertCs5RBht0tQdoC_-kuvHbcjT3IeRTLqKVbqFTGvjqSLzgWyiFIHUZz3chi933zW7axkClz-gHK5ZqKBFsVXa1JfMPZOvP4VQG5I1nxibA10OPdV6lZaurOytqeyKOd1fCMqK7-0XZR9WEKmemu-8HFgO3A1PHnObAtVu-oc4GUVKMf3FPHHm19p1ilMDOI8cDVo2XU5glD0akrflStpt7P_TC14IOAgmhuGFOLMthJx0iLPgpAv3DP-TnhMHALrZGPlhB6DXURlgp3vbmwm4pyqDhk4HTKPMgINduQtjQeMDGdaSmgO4R72GykHr6WoOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
ترامپ یه پستی رو گذاشت که توش نوشته : پس از کشته شدن سربازان امریکایی، ترامپ به سنتکام دستور «دروازه جهنم رو باز کنید» و حمله به ایران رو آغاز کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/101591" target="_blank">📅 20:39 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101590">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UsM1MUvrqwNdYulM0FlDXzRZqX9bKxoedcKJMDuQnZSeqX_uE-kefedSwbn2VX-sqGirI32mEjW7oKHqNHdvJF9DHYDbSnYFLmeyC8brUY2blarmqtldUhAMBTJLsAX2drgNTAcIGjvaRaeiIg2Do76K9EKWrfKUm0o2cOxICk_EKWrBeh5cE3XkD-aWjrKxGA8NuuHS-ZutHO0S0aA4fnlVfgWElwNalxM6JPCSn0kqfimn9kpaRsFtcBE5EIbd7IdHCWpPWGqEtCElgqKMYUuI9RfFIZNGCTx9EaD_LalQa7mzfiiqJVo9pAR26rAKlAfX5MBdAwOyYldQfmHSWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✔️
کنفدراسیون فوتبال آفریقا اعلام کرد که این مسابقات از سال ۲۰۲۷ با حضور ۲۸ تیم برگزار خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/101590" target="_blank">📅 20:37 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101588">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/M7kI006o_Gym61vywfFUzrDVLW0U04dapd3aRlwTtJZrlSzwi8QftqCf1KHMx04x_MG_nCGkR6dHWqO6hCf1dY4CfoDjSdmnwshA0rmYeBE5DDEvgWM9pwHvTVxxaKN4qh0EUUiUysLUWtvO3OcGD25VOoMttJorpLhyWPiyZJeMEWFKkAjS34MVIf_8Sg6WYQpy8XPkd1awdrITt-LxDGgnrgyX9coZqedemRkp0hpsC5gEdCPsKRYGiQm_bnG_aEPBVVdXfTpm1e5k3V0a7vORtWeLcxxkt5Tumd1DcrP6uDQbejrRn7gOjihT60eIGAqOEvNDHcoFoYqbGjpmFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/f8v480p-zRu2csLq_Mna6mtHqIX5VL5dH7wzH4wjv3XABvy6ezXNrQANwMI73Rl5crjjYpduEqOiMZolsqxGzkGPrq6bS5rz6klCYk1q1ETspdlHNn25yp4TyMNVo6SH3d0RTpa_4EtyRz_R4aRz3R8wXQaFcxo8WZkW5pjgwtmX78KPv2di3MqZhPzRkiEzFa7kKtHzKTPoVfH2ffG22AX4JbqTXQBn9b1fewr2mh1YKsQLTWTh2teCzLBDpqNOWc2JCA4mNx9TsaN5JrHpN1IoRMC3glqjqtl7msqXLy70ETyplZFFe5OI_iFlAqR48sVaWKtVZdrV2xkiZjiZTw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
کاور رسمی نسخه استاندارد FC27
🔺
تریلر بازی فردا 23 جولای منتشر میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/101588" target="_blank">📅 20:36 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101586">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kxM-VV3CH0A6Cbf1ynzbHx2IG9CPuiTNRJlqHgWFWeNBOVa-VbrbL9zsLcCgux-yyO4gcMwyN2mBt6AU67f9tNpsWa9l72upHL-7vNB1ZTuqH5fmpxXrEGwe2iwn63W8_ZSwxg6FV-NdU9JJhYZ5dEUo8hbjv1EsihbYgXwCNoOHDVeit0Rw87Qpmm9Mdz-YLvGGUxmmKj7u8oM_zzFBPdhUseJHUXZYQUj4m-QXckgaZzk_CX1r_D-yAzibrslE_fEHLz3tHJqVedzgun-exeoSmAvBO_OtDqY2slP4x6jaIx1gek4rAZZ9ooMLAjmZIqBrVIbaa3n7VaAfYJcvng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6db999500.mp4?token=VzbfJshAGBzgjmb5n_WiNS8do9knFCdOBicPmrhc_Utn-Vm-bCmT-rfKcO1Nlpc2gV21d53h6_gMBfZIwj_cqjNsvtV9p_kX6QmBfuORxNwWiQt67gsDCkngFgqd3fidqzGohLHBZkAjx-VS5wwslX6qF1j0jFSI4i51j38Le6M07YwJFr6bj2-QR4aSbGYsOmu3F2MJpKguQSxb3adhKjCr1CjaRtH6qdqQs6LViEfm8KW7pan5S_FR9PTyhfWYdtxac0A30x8YnLl0EqU0ysLYJw7lq_PYnyj0zL_NNh7fnC1iyv8S0_yJ82bFHrGkDIIZkDVcfezydb_rS7vffw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6db999500.mp4?token=VzbfJshAGBzgjmb5n_WiNS8do9knFCdOBicPmrhc_Utn-Vm-bCmT-rfKcO1Nlpc2gV21d53h6_gMBfZIwj_cqjNsvtV9p_kX6QmBfuORxNwWiQt67gsDCkngFgqd3fidqzGohLHBZkAjx-VS5wwslX6qF1j0jFSI4i51j38Le6M07YwJFr6bj2-QR4aSbGYsOmu3F2MJpKguQSxb3adhKjCr1CjaRtH6qdqQs6LViEfm8KW7pan5S_FR9PTyhfWYdtxac0A30x8YnLl0EqU0ysLYJw7lq_PYnyj0zL_NNh7fnC1iyv8S0_yJ82bFHrGkDIIZkDVcfezydb_rS7vffw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📅
🔴
24 سال پیش در چنین‌روزی ریو فردیناند یکی از بهترین مدافعان تاریخ پریمیر لیگ به منچستریونایتد پیوست و با 30 میلیون پوند، گران‌ترین بازیکن تاریخ منچستر یونایتد شد.
🏟️
455 بازی
⛔️
203 بازی بدون گل خورده
✅
🔻
پرمیرلیگ [x6]
🔥
🔻
جام اتحادیه انگلیس [x2]
🚀
🔻
سوپرجام انگلیس [x4]
🔵
🔻
لیگ قهرمانان اروپا [x1]
✔️
🔻
جام باشگاه‌های جهان [x1]
🥇
🔻
عضو تیم منتخب فصل پرمیرلیگ [x6]
🥇
🔻
عضو تیم منتخب فصل فیفا [x1]
🥇
🔻
بازیکن فصل 1997/98 وستهم
🥇
🔻
عضو تالار مشاهیر فوتبال انگلیس
🥇
🔻
عضو تالار مشاهیر پرمیرلیگ
🎙
🔻
مایکل کریک:
به‌طور خلاصه، بهترین مدافع میانی‌ای که تا به حال دیده‌ام.
🎙
🔻
کریستیانو رونالدو:
واسه من افتخار بزرگیه که با یکی از بهترین مدافعان تاریخ همبازی بودم. فوتبال و شخصیت او داخل و خارج از زمین بی نظیر بوده. واقعاً خوش شانس بودم که کنار او بازی کردم نه مقابلش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/Futball180TV/101586" target="_blank">📅 20:03 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101585">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IettCqTYuu4HaEux2BIcO9iEfYYqHtHkh464g5hrjhD2U1qUUTQ8EvRHB8urB06UQp876V1gc-xmpf1GrD3IFKCUhyBCcr92M0lPXila9soRC118M4QRUwK-3v-LQcaV2A1_OpsJczhkjUGVhIPgqossZo98Br_IZAnKtcuEHnGPd89pXENI1fUA794cusEw-tnL2pnJhrDS9lWQc0ec60jIOZw2TE0b0lvzONxAQ6XO71glIgasaske5in6iU4xrhUuNovci3k2LbHytjPfP7pTCN5GZir1o4Lq0nCuuyRULCztC4NLqPR8tKzzP0jVt-CfxLcWHTbnw4qRBrh-1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
کاسمیرو در انتقالی آزاد با قراردادی تا سال 2029 به اینترمیامی پیوست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/101585" target="_blank">📅 19:55 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101584">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ansNckYq26VBoZCWkYD_9JqqmyOyXpBnAZaW4JmaIoZOYFmOGgcWgDTwQdq-als-LjosutiBQMlN_2TFFp_lurTfInnjuKdvJa3H9yESGlGII_Wx6f3xYbnwptjPeLx9y-Tc-KkWH2u1LNcpLMI4biKAEk83uyxpPRYcEvwyP2jlzg3sPCssjbU0X9KajtJsSzduqtcAWD6zKBkAgRXT6i2K2fzEKsDiE9h9pnMmB2KvY4JM1X5TGfVU9bcBqW01S6GNjDw4WYGbpdupLiUfTHJRyVzyEGCSIkovnuCEPjFdXYdKLOURgPclBIRunck6xpJMgUAy0g-_BhIvoTt4QA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوووووری
از رومانو: گارناچو با عقد قراردادی قرضی راهی استون‌ویلا شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/101584" target="_blank">📅 19:45 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101583">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b963f629b0.mp4?token=fJNwhHhp-UZ-ZF4htG7ieqD0QKYLT-yVh6NdFCmhffjwVJGV1Kp8HPLb3QgU3q0rOce9cAyt9JS28dbXoArYyFmBfZSGkCIwvmSIiGiizpYa_HHBBRo2NNU1jMXShhewS5a1yJM_-lubEK5hhUfK-LYEafNm7V-w1U02iRrqP_zT2fbXX407CTyij58Z_wcUp5KHbLlpB8vbp9_Hhr8Oc2gBNtcUK9BcbaexMWu5gUZwAASd64QLL92OhppwkuVErr1TwhuLgNmvRp5TVzwaqjY1hgqbK8iw01wh3HvRP0VZ-xqnM1iG8F96LE4doe6s3LkBcJkHFhPIX-J-wstyRI1gAjJLyUDEV72P0YFhPFRVeAzldia79kRQaZzTeGknrzpBSyD1A-9exmXCtkPoslypz3bUYNLCblGG34NO3vXMs-R_Yh7CiDSmfkhtZI8UOacllux4ZMvNu13sLmaDaxhUInilmbI-GrwHGeFq8NHmWBnRN-9XwH-VqiC7NmOsfIgPU4_6yxipZzPqa2XknsRbBE7DsAZrUAjf74jNHXXue9XWBTdIVK-M9pyL6z-mjk5V-x-qaq91ONyABaWCVDLPjpXmRqfK39_e8P7zSl-Ps_kPfDvqc-6x94otxHGgrd2Kun55DNVvVX0Ua07H9RrZoiI0pwoqcS9S4iVZz5E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b963f629b0.mp4?token=fJNwhHhp-UZ-ZF4htG7ieqD0QKYLT-yVh6NdFCmhffjwVJGV1Kp8HPLb3QgU3q0rOce9cAyt9JS28dbXoArYyFmBfZSGkCIwvmSIiGiizpYa_HHBBRo2NNU1jMXShhewS5a1yJM_-lubEK5hhUfK-LYEafNm7V-w1U02iRrqP_zT2fbXX407CTyij58Z_wcUp5KHbLlpB8vbp9_Hhr8Oc2gBNtcUK9BcbaexMWu5gUZwAASd64QLL92OhppwkuVErr1TwhuLgNmvRp5TVzwaqjY1hgqbK8iw01wh3HvRP0VZ-xqnM1iG8F96LE4doe6s3LkBcJkHFhPIX-J-wstyRI1gAjJLyUDEV72P0YFhPFRVeAzldia79kRQaZzTeGknrzpBSyD1A-9exmXCtkPoslypz3bUYNLCblGG34NO3vXMs-R_Yh7CiDSmfkhtZI8UOacllux4ZMvNu13sLmaDaxhUInilmbI-GrwHGeFq8NHmWBnRN-9XwH-VqiC7NmOsfIgPU4_6yxipZzPqa2XknsRbBE7DsAZrUAjf74jNHXXue9XWBTdIVK-M9pyL6z-mjk5V-x-qaq91ONyABaWCVDLPjpXmRqfK39_e8P7zSl-Ps_kPfDvqc-6x94otxHGgrd2Kun55DNVvVX0Ua07H9RrZoiI0pwoqcS9S4iVZz5E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
⚠️
میلاد کرمی: بخاطر چند میلیون پول بیشتر تصمیم گرفتم یه حرکت وحشتناک بزنم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/101583" target="_blank">📅 19:40 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101582">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b5lREVv1eyZKLsiO4n7a03lqoeHCeLDWuMojF-ILCcXGfpVIYyTEsRgDCKTk1vssw8qvlWSJpQX9OnzEGGvDZXCXc9W0ATGMJnSJjpc0zrNQbNJ9gXbmFC-mr0qph9p1NQT7FOBDINyY5Ufh8sVp9c5T2PylQEb7o6aXnmvDfwaMkEz74FkpAZjtNAEZsm7exzsvu6IwjCR07WDVHEY35ilXnYnMMIBWWF5yBG7ZVGMqzgRLSn_jsTrB2zcIHqU_VMRSHT4T9gNh3g-0cz83HrMr9B4n8TL6vGBMFeWB9jR1237MZzBvpgm2wOT5yWFCJdpPkr0cSd9VkJDq2ak1YA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏امباپه در این فصل آقای گل لالیگا، چمپیونزلیگ و جام جهانی شد و در نهایت هیچ جامی برنده نشد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/101582" target="_blank">📅 19:37 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101581">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/723401c013.mp4?token=cvNEqpQy-FpBc3bH26FRVGkEYx2z0eywtr_w6R6C99s3Ds0pyd82_mc5k6XhwT-tE0BP-KHjCXUxz3YuWCjJLhJjq3xWwVjAHjvZAMFlyDwWeqXeaJHxa0EqmrEl5XDGElWbvGzkRrRlAmHqN9cx5ARdKV7_D4dlgzFAoqR5yvMMg7bCg76Cgt164FLchXY7Y66v1i1y6mdaCKtBe7S9Z89IX-9rJiwRRqv1aBtzgDf7ayV1OxJuui-lhNkvYm6kVvKZZ80w7G-AuNlF82cr1wKpDAbs5KAYs6MsEaF4R-pW6prRFsiouGbrEMiihusiE3nKfAg4yE2xClhzlMgn3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/723401c013.mp4?token=cvNEqpQy-FpBc3bH26FRVGkEYx2z0eywtr_w6R6C99s3Ds0pyd82_mc5k6XhwT-tE0BP-KHjCXUxz3YuWCjJLhJjq3xWwVjAHjvZAMFlyDwWeqXeaJHxa0EqmrEl5XDGElWbvGzkRrRlAmHqN9cx5ARdKV7_D4dlgzFAoqR5yvMMg7bCg76Cgt164FLchXY7Y66v1i1y6mdaCKtBe7S9Z89IX-9rJiwRRqv1aBtzgDf7ayV1OxJuui-lhNkvYm6kVvKZZ80w7G-AuNlF82cr1wKpDAbs5KAYs6MsEaF4R-pW6prRFsiouGbrEMiihusiE3nKfAg4yE2xClhzlMgn3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
علی‌قلی‌زاده: در عمل جراحی رباطی که داشتم، از یک‌عضو جسد برای پیوند استفاده شده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/101581" target="_blank">📅 19:20 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101580">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KaimaR7Fms5FrYnfwuz7zG-_u4pDdR3j2a8Kk3y0yWAfVgKJVYaYUpmqfSN9XcmiZ40tiecCLwiBljQ3MVijyGwEePILM7oOH4ndI7hcrfifl2CZAat2i_LCuaGDKMNKV1-NNNhV0lqQn_gXA3usSXNmUiqDAP5iZxCNQP7tBwGFL-66nmcCaSclYMHPGyGMYjzUpZaHmI64xP6NmJEDYvqljQfltDBnEfGx5xqUiTrRAJVnLodqhVvvk7UfS0pvPKDKwmbcXJQVU_4vqvTTxpX_nPMQhgvSX2DaxeCUHpblvwb8b3w-Q0OEmQJ52ZbH5nkCXh0yL_4yYuq1FxyJnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
پزشکیان:
دستور ویژه دادم که سایت عادل فردوسی‌پور از فیلتر خارج بشه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/101580" target="_blank">📅 19:14 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101579">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JfkX-Aq3lPTjJEE0QJpHhE0K5C5YllIfx20sEne0XxBAZegfgZH05cAoh55fGBmAwR50bQfixpjQBan09TIErZaWBB71geRBew6h1lbmrsx6toFEtBUu9mmbVGkXnLnNmEprLjCawFZoLZgJLDUhBpVz7t80aFPn6PzEQNMQMLikzq7dvhlGAyDQ6hxMLy9q9s67IUyZ4aLuRzQOtAp5iOVxydXGyoQRTnnAwVrIv_Tla7kH9P3CN7wO2WzbhkPYdmfeTV0wL3IuJnNjX77KYwh1omSmlBUTzdoMVJTiVWexcRtNFKez-EkoB7hAXtIpC_cmCIN_ognMVbn3rp0FDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تاد بولی از زمان اومدنش به چلسی 291 میلیون پوند برای بازیکنای آکادمی منچسترسیتی هزینه کرده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/101579" target="_blank">📅 19:09 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101578">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d2ZIrEtOyoOmhs6rhwWQUdTMulmZnb5RjjpAmJveWqXQm6sr5Phl2Z7hWxLmLrFybKXNR_vQjSUNr1ZmwlqoZuwH9pWwPWTsw_dWpax6IxiWraOAtbC2GnH-8811FM7nZq2FY3Q2caoj4UqXskF7wUtNQt-kN-Z0j38dIZ4IkLeffcvxXlxIRQB_meM7ZfoLMIG9jdiLdtCBQD-DQ7WTkFFjN8ht-EDCD1h3LttodNUV5d3ieFNLVQnicg0fEHehSriOWi9dPzuwnyWIka_uQePWLvGVNiqcIBr6h4nNF1MXG10QnVSy4HngwPnaV2AbTq_WxZJUGwTkHaUr8UxYnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آنالیز
دقیق،
برد
تضمینی
!
📊
💵
حرفه‌ای‌ها دیگه حدس نمی‌زنن، آنالیز می‌کنن. توی
Pinbet
، ما آمار و ارقام رو به سود شما تبدیل می‌کنیم
✔️
با ما همیشه یه قدم جلوتر از بازی هستی
⌛
روی لینک زیر کلیک کن و تحلیل بازی‌های امشب رو ببین
👇
🔗
@Pinbet_official
🔗
@Pinbet_official
🔗
@Pinbet_official</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/101578" target="_blank">📅 19:09 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101577">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cab44dc23d.mp4?token=J-DPDvgdT5Izj9KBZKT3TREe_dAkR8ZI1O6l_5pQfhHdW1F37zgh3z2eg5JF7RjSeLHbSvDdzhqVdkgiqgEbKa8vxlgAQu2fDTpITF9SDcPoU6i0SugsM9LgxNVVjv39wyYxuetDbI58YUAPmEBeI1ThdvGGVuNa3QaRS5f89W9QzZTv2EyYi4uUSqccZqKIx1Y7ROsztJA_l2a-pMxrGAZAAzwMANKHRZgjRNgAD3Kzt2lKIDeisb0VZU0k9H4ARAHJATD890XjtKGVVLpd9oijVQRnvWjCHSFpKKXJ5NP1qnwGHKJtL1u0yiEXntYNR9-iU3udf3SK1z6uI88Y3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cab44dc23d.mp4?token=J-DPDvgdT5Izj9KBZKT3TREe_dAkR8ZI1O6l_5pQfhHdW1F37zgh3z2eg5JF7RjSeLHbSvDdzhqVdkgiqgEbKa8vxlgAQu2fDTpITF9SDcPoU6i0SugsM9LgxNVVjv39wyYxuetDbI58YUAPmEBeI1ThdvGGVuNa3QaRS5f89W9QzZTv2EyYi4uUSqccZqKIx1Y7ROsztJA_l2a-pMxrGAZAAzwMANKHRZgjRNgAD3Kzt2lKIDeisb0VZU0k9H4ARAHJATD890XjtKGVVLpd9oijVQRnvWjCHSFpKKXJ5NP1qnwGHKJtL1u0yiEXntYNR9-iU3udf3SK1z6uI88Y3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
دیس سیدجلال‌حسینی به محمدحسین میثاقی و عادل فردوسی‌پور: یادشون رفته از کیروش حمایت می‌کردند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/101577" target="_blank">📅 19:03 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101576">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0c61d3ee9.mp4?token=OEvXiN5cl5euQCq1mRVMCTHal4ydAywkheg6Hg3-yaLABoPMTM3JtAaTSJtBQJ7spEAlhsDSTtD-c5osUPipxFll4knQ1RmRTvuqocLvNtqgDzpscQESIeOsEzOAV-YD4u57LfCDs5Qrba3j-gqGlTccR3LV-ZPplW6dHOPc9XMvg0mJbvP06oUEpxLXrEKL7eHwiQzuIP4Muck9R07vQRXDyDjnVCZKIs085eWBeJxL8Naf-K39YqMGRkQNmfjffZfXTyPfmj4zAHCuURoFBK5_21b9J2CyfeMZj9ERF7yll1pWEoMk2JLgsINzhoKD5meVlZo_6psyD_Co3LH0AA-ZB5AYnLzaH7rt1KrHn-miuUxIJaMSZ0We486JqdK21ZOEtFa2IC9SfrBqCILbIYIAX0RRlNnNFDUmESnu4AtRCpunLQ1NIBejfrkxPvt4jj-epEAacyCOQP3oF1Wj4ZXZaSaacfjtkhOaSr9mp7CLfOsc5OZde_oy5W4jdnrD5GDahUuAJuGkimmyYlkcTtouKtaHbyZ6Fr8t2yxZRU1PgF95zPsKia3ZrxbTlqn8pEUxoo82wITMpuM33t0oO4jHxqeRJ9w2pBRHRUVKY_pYFp5p-7pNo4cpRGY_QVtsQFmPIJnJ-kel7xPm9EJ9lizzdrDrsYw4Y9OImb4ZZzM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0c61d3ee9.mp4?token=OEvXiN5cl5euQCq1mRVMCTHal4ydAywkheg6Hg3-yaLABoPMTM3JtAaTSJtBQJ7spEAlhsDSTtD-c5osUPipxFll4knQ1RmRTvuqocLvNtqgDzpscQESIeOsEzOAV-YD4u57LfCDs5Qrba3j-gqGlTccR3LV-ZPplW6dHOPc9XMvg0mJbvP06oUEpxLXrEKL7eHwiQzuIP4Muck9R07vQRXDyDjnVCZKIs085eWBeJxL8Naf-K39YqMGRkQNmfjffZfXTyPfmj4zAHCuURoFBK5_21b9J2CyfeMZj9ERF7yll1pWEoMk2JLgsINzhoKD5meVlZo_6psyD_Co3LH0AA-ZB5AYnLzaH7rt1KrHn-miuUxIJaMSZ0We486JqdK21ZOEtFa2IC9SfrBqCILbIYIAX0RRlNnNFDUmESnu4AtRCpunLQ1NIBejfrkxPvt4jj-epEAacyCOQP3oF1Wj4ZXZaSaacfjtkhOaSr9mp7CLfOsc5OZde_oy5W4jdnrD5GDahUuAJuGkimmyYlkcTtouKtaHbyZ6Fr8t2yxZRU1PgF95zPsKia3ZrxbTlqn8pEUxoo82wITMpuM33t0oO4jHxqeRJ9w2pBRHRUVKY_pYFp5p-7pNo4cpRGY_QVtsQFmPIJnJ-kel7xPm9EJ9lizzdrDrsYw4Y9OImb4ZZzM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
💥
قدرت شوت‌زنی اسطوره‌رونالدو که اگر‌توپ گل نمیشد قطعا بازیکن مصدوم میشد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/101576" target="_blank">📅 18:40 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101575">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/641d875577.mp4?token=Y1B8W4gDKf28M8qOVZzvEdzoiLBSpMuADiZ4yDb3Y3bn2921gkvcAdKMsa2OV0yKvDMMinBubj7hIKPUM7c761yZJlEBIPewbgUbUFqMat-DzmpAfBfEezievu6nqT_KxI3jHhGgKFhX-R2pqP4ea7_cSOkJeP7bHeYkTk7PE_0FwHI5ht_uASYH4C24awpl1oHLPLDQPtcWIQNKasTFxcKIcFl24IPSV-cpWvdkoOZk6myJiq1haYkB7aPR7ggAbfJ3HW5RfUmh9fxZNuHewnl1zE6ebIdGmEeeUyZQqrNgsPiKpowbEwd6qoFOfoLDS-SjwcuzWh-gNUW7mBlTTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/641d875577.mp4?token=Y1B8W4gDKf28M8qOVZzvEdzoiLBSpMuADiZ4yDb3Y3bn2921gkvcAdKMsa2OV0yKvDMMinBubj7hIKPUM7c761yZJlEBIPewbgUbUFqMat-DzmpAfBfEezievu6nqT_KxI3jHhGgKFhX-R2pqP4ea7_cSOkJeP7bHeYkTk7PE_0FwHI5ht_uASYH4C24awpl1oHLPLDQPtcWIQNKasTFxcKIcFl24IPSV-cpWvdkoOZk6myJiq1haYkB7aPR7ggAbfJ3HW5RfUmh9fxZNuHewnl1zE6ebIdGmEeeUyZQqrNgsPiKpowbEwd6qoFOfoLDS-SjwcuzWh-gNUW7mBlTTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🎙
علی‌ قلی‌زاده‌: کل خانواده‌ام استقلالیه ولی من عاشق پرسپولیسم؛ خیلی دوست دارم در پرسپولیس بازی کنم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/101575" target="_blank">📅 18:31 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101574">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cdff7389ce.mp4?token=fQMUS9iQYTINA2slQ334sJ87KSuGv-ITmHMd2gyxtYRYMGsBIC83Ma7sltg-5m-RNyKk4QpY4HOvTfxtYL5Fr8bluxgQV2_MQTeoKjzzQxwQjwfR8unP7hTJLBnnDnToTuuZpNMoRDGPMDEZom9Wuc81hkFOxEUTUeoHIwIatoHXwIH5NkZmrL3XHnu97SEfQe7xZBCY7aGZ8MUsxbsobk7wJpibpjRhGh2s0uU4FQ9KMEE5sU3B1WseOtSCztUTVVmWhDEmsf-Sz-Iw7BjaUYIlTLhpFM5giHidAdwWEtNGfnjOmcqIFOzt0FC7WJ9quZSuQNcGE8W6Yz5IP5z9Xg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cdff7389ce.mp4?token=fQMUS9iQYTINA2slQ334sJ87KSuGv-ITmHMd2gyxtYRYMGsBIC83Ma7sltg-5m-RNyKk4QpY4HOvTfxtYL5Fr8bluxgQV2_MQTeoKjzzQxwQjwfR8unP7hTJLBnnDnToTuuZpNMoRDGPMDEZom9Wuc81hkFOxEUTUeoHIwIatoHXwIH5NkZmrL3XHnu97SEfQe7xZBCY7aGZ8MUsxbsobk7wJpibpjRhGh2s0uU4FQ9KMEE5sU3B1WseOtSCztUTVVmWhDEmsf-Sz-Iw7BjaUYIlTLhpFM5giHidAdwWEtNGfnjOmcqIFOzt0FC7WJ9quZSuQNcGE8W6Yz5IP5z9Xg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
🎙
جواب عادل فردوسی‌پور به حرف‌های اخیر قلعه‌نویی: بودجه یک‌فصل تولید برنامه من از پاداش سرمربی تیم‌ملی قطعا کمتره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/101574" target="_blank">📅 18:20 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101573">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZDSXiHCNHselNAe_1cGEMrGF8dkPfQF43M-Y4I-K09iJwGvnxNCP-i8qjwIyBypUBaHZdYvRZ0U7pSq42jxRj6UElaSV_p4KBReY202hOOyqiD-fZO1S5A4-2cW-9veyvXX0Dlls_yxd1eJYJ100g1aHzwa00UdYF_uMhOX_7EE9AHFK42oAiTs2hdKA_tFTcC5Fpm9oH8d9UBCPxez9E6bk5Hn_DuefYk6a_ZJRmeh_KlptfmywUJ8TlL0bQqICJPzZTj2nSo3tCDDJlKa0Svbk-1qLoEjxjV0Sxoj6_-5oNgL8f4FfrVSGb9B4AAzA3FPVfNMDW1i497kQmOyADg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔺
👀
فدراسیون بین‌المللی تاریخ و آمار فوتبال (IFFHS) به صورت رسمی لئو مسی را به عنوان بهترین بازیکن جام جهانی ۲۰۲۶ معرفی کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/101573" target="_blank">📅 18:15 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101572">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f420d24855.mp4?token=X-hGiuHc3Vqswcp6eZlN_8PHl82nGryOzNGTcrwvapwzewXU87PubKY8F9oeFS3UGpgAzm5niLZQXk7-8xPsMvzN8Pq0pJnOOArY5yRDxXZCM21rFz0kCosSgr7ll79tMbTaGrtey6_XoewKB8nbANQXDyMZpiuaCb59mKM8nbd4JOKUGJOB0U2Kn2rLi-RotzmgI2PGYIlQWY9ZCWImHTeGa8G7LRo91iVk-GgJOcMmwaxh4t19zs9YtlI1zZ4bZU127sJmLNIQV3YqjTdoY7gLq1W1HXZL_ZdQgquedh6F5EnBLkbn0XBLUDqn9FBG7wxod1vPJHTupJ1fL_dWYykoPluOTkMZ8w4_Ui75Ln3aRYUMkZHabebwuK5vIcYv_s3KWX_4v2m1hvLYExtot8PafBm37exqNcHPpqukK28jdwYe4_2RhJu70wPpUCGNhki1KxvzkqQnpHeySFVX-XMn_5fuVpkX5iC3MtlMZnM01imBx5TPc-xq43sNFaCnIeGYBIazHR5lgkP-W1XnDJ-faWEH0fT9hiKPEacecHNMfhRWFD-_5ChfEIi3tg303nio7JARx373F_pofMzAgU_aHtVd-kYSVQZ6VcQX12j0536bsjrBOedD_BtFIpfkoI-fLFB7eBA5J7pTYsa8EEA2QN0oX0R18pb81Zc6oYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f420d24855.mp4?token=X-hGiuHc3Vqswcp6eZlN_8PHl82nGryOzNGTcrwvapwzewXU87PubKY8F9oeFS3UGpgAzm5niLZQXk7-8xPsMvzN8Pq0pJnOOArY5yRDxXZCM21rFz0kCosSgr7ll79tMbTaGrtey6_XoewKB8nbANQXDyMZpiuaCb59mKM8nbd4JOKUGJOB0U2Kn2rLi-RotzmgI2PGYIlQWY9ZCWImHTeGa8G7LRo91iVk-GgJOcMmwaxh4t19zs9YtlI1zZ4bZU127sJmLNIQV3YqjTdoY7gLq1W1HXZL_ZdQgquedh6F5EnBLkbn0XBLUDqn9FBG7wxod1vPJHTupJ1fL_dWYykoPluOTkMZ8w4_Ui75Ln3aRYUMkZHabebwuK5vIcYv_s3KWX_4v2m1hvLYExtot8PafBm37exqNcHPpqukK28jdwYe4_2RhJu70wPpUCGNhki1KxvzkqQnpHeySFVX-XMn_5fuVpkX5iC3MtlMZnM01imBx5TPc-xq43sNFaCnIeGYBIazHR5lgkP-W1XnDJ-faWEH0fT9hiKPEacecHNMfhRWFD-_5ChfEIi3tg303nio7JARx373F_pofMzAgU_aHtVd-kYSVQZ6VcQX12j0536bsjrBOedD_BtFIpfkoI-fLFB7eBA5J7pTYsa8EEA2QN0oX0R18pb81Zc6oYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
⚠️
وقتی صحبت از کارما میشه منظور چیه:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/101572" target="_blank">📅 18:03 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101571">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CY_sKteO_GIJdb0JsDS759bK9ve-acZH1oy-GGW2YHjDqRE-NlXo0jBGyHJjupSvrX1HD2Z3StgL3o87M2WEB6EA5wB2yhnWLQP26eSWDON1jGJr5PvFlHyoDBpclAwVd8VbrjaSxRYBkB1v0iQT9HJhvwRKcaiSJk6TPQvwOn9YXsgdIb6hZ1ltToODOrlg6cbVIqGo6qdxyloGOqqVdQmlqgnsD5hXIYRUlUjYiSlqYY1ICBsvJW6E-fifXxEz0PS9D25jRNSWa8m71mHmsGwtwrjix5B3GYKQR9rFw2FMBJ9ofgPt9MINqfnDSWUJrP0HrbvK1vwKYeOEer1ynQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
لیورپول و آرسنال درحال رقابت شدید برای جذب بردلی‌بارکولا هستند. حداقل رقم پیشنهادی به پاری‌سن‌ژرمن حدود ۱۰۰ میلیون یورو تخمین زده شده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/101571" target="_blank">📅 17:54 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101570">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb17487185.mp4?token=R7lIVu1DCdJX5iKG7lxCqQOmLkSGscLyFvlfmJl_qhCGDIYblIgcGZ5HylB6Efmilw4gtxe0Nz-8wJP-Km5N6XTdTdokbygHekcjV_g015ikI4EVRt2IMKbE_8Or_0hEDgERJehe_SpqQYmL_CNTHANdX8OC1oo8vGo5RXO_fAcPSwyIflPFPgwAlGr7j-xJn6mDK-WBxfPx7eOmBGdk2wH8zfQ_p0UfmjHyhEc57DhAqm5sq8zcCsZeXbUXVhU8RfAwAtyhHZfimy4RxhYIFhKYheXGJiYcr6jA3MbkTfUlCPn3Q3Xs8EgmhNubUBVUKFMOJiuQfjLrl6VwoiJG0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb17487185.mp4?token=R7lIVu1DCdJX5iKG7lxCqQOmLkSGscLyFvlfmJl_qhCGDIYblIgcGZ5HylB6Efmilw4gtxe0Nz-8wJP-Km5N6XTdTdokbygHekcjV_g015ikI4EVRt2IMKbE_8Or_0hEDgERJehe_SpqQYmL_CNTHANdX8OC1oo8vGo5RXO_fAcPSwyIflPFPgwAlGr7j-xJn6mDK-WBxfPx7eOmBGdk2wH8zfQ_p0UfmjHyhEc57DhAqm5sq8zcCsZeXbUXVhU8RfAwAtyhHZfimy4RxhYIFhKYheXGJiYcr6jA3MbkTfUlCPn3Q3Xs8EgmhNubUBVUKFMOJiuQfjLrl6VwoiJG0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
فرصت‌سوزهای اسطوره فران‌تورس ستاره فعلی اسپانیا در فصل گذشته برای بارسلونا
😂
😳
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/101570" target="_blank">📅 17:40 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101569">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ea79a8c03.mp4?token=Xf1riJsJfvHyrseNjwAa4crzaUTelNts0oTOXQE5qgIBxp4pw7fLe2uzr39-6w3wFRNaJuixUDVywdWIQk9Ixr913UaqXkbnvQVWn_fNyN7qNJtHFjEnq3ebuoQ0C0S6oiNiP4jU9vrBzkT0YsIkTVSxUqyAJoEnGbPdqx3R8RMNJgcW3WAHihThnc0RSaHQrgKsRhRXHy_nK7BP0_LcLC87DHlexp4bKfi4X4JfPmbkXufaBZ0HK87bBvMQSO070nAYttNwnBKipASSF49OoyYf85s2eYagKdEzFRSH5BQCQGfjMhBzHZdXJ1mnC_HO2DqZldaDNhbk8neIArtluQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ea79a8c03.mp4?token=Xf1riJsJfvHyrseNjwAa4crzaUTelNts0oTOXQE5qgIBxp4pw7fLe2uzr39-6w3wFRNaJuixUDVywdWIQk9Ixr913UaqXkbnvQVWn_fNyN7qNJtHFjEnq3ebuoQ0C0S6oiNiP4jU9vrBzkT0YsIkTVSxUqyAJoEnGbPdqx3R8RMNJgcW3WAHihThnc0RSaHQrgKsRhRXHy_nK7BP0_LcLC87DHlexp4bKfi4X4JfPmbkXufaBZ0HK87bBvMQSO070nAYttNwnBKipASSF49OoyYf85s2eYagKdEzFRSH5BQCQGfjMhBzHZdXJ1mnC_HO2DqZldaDNhbk8neIArtluQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
⚠️
دسته‌گل استاد فران‌تورس در حین حمل مینی کاپ اهدایی جام‌جهانی از سوی فیفا!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/101569" target="_blank">📅 17:20 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101568">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o8X3oPuD-JOi123iFE_6WNOZXhZ96ccVtDHUTk44_7j4S6g6OOBLevbhR4pWcydCqTIuhP3G1vjxKWLoMDdFZJe_xAlZPaTkf0nC7p3s6eatDoC9tthBY-8C0fzNgys0B7NSpNNBrSeviwQUqoBw2Tl5rYCyQgoZVWfH9w5XrG83ItZ7-le7EpkBQmnK2diFopB-iB5pikw1KYt_Di6dfl7pOhg-Op9EoCecagOAYCVL8ACWhbKSAPgaa6gN6xKGqEwLeQpD0D-ZANil3y2v2Mh9w4le_BUqax7gRi_AWC5IU7FN-sb1YGX_ePxrpPAdS0FjHN5PKAsRBORmKKrDoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
ترکیب منتخب جام‌جهانی از نگاه فیفا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/101568" target="_blank">📅 17:08 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101567">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e38a17a2eb.mp4?token=ERAvo72M2FE8nbTErnDw28NMc6cu1I0UNF1EeJqSVxTXxoLLufYzWmYmAeoAdfqH1wmBgzlpiIUeL5QoOnLZn2ttbHx-l52QJfjhaGpwe2wm_8J30Zi7O3xTFGLeVw_oCLpZZAOwLpunnYY0tNC374Y7azugcEEdMWhNj5VwYyaxsMTFcOJp5XX-Amn6md1bbeRED036dNHreerzo7om05y21x0EqrLsVw-G9v8yJbyHhIDMwaFDbHdZ7FdBbEwgmz-KuA4S7XhBCBqsP7aIhKo3BBav6TpYRTHHh1OBsidkBF2RwpYYIvUyCbM7jW_HYBTK9h2NmJ5lHmtBy3bqUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e38a17a2eb.mp4?token=ERAvo72M2FE8nbTErnDw28NMc6cu1I0UNF1EeJqSVxTXxoLLufYzWmYmAeoAdfqH1wmBgzlpiIUeL5QoOnLZn2ttbHx-l52QJfjhaGpwe2wm_8J30Zi7O3xTFGLeVw_oCLpZZAOwLpunnYY0tNC374Y7azugcEEdMWhNj5VwYyaxsMTFcOJp5XX-Amn6md1bbeRED036dNHreerzo7om05y21x0EqrLsVw-G9v8yJbyHhIDMwaFDbHdZ7FdBbEwgmz-KuA4S7XhBCBqsP7aIhKo3BBav6TpYRTHHh1OBsidkBF2RwpYYIvUyCbM7jW_HYBTK9h2NmJ5lHmtBy3bqUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
✔️
پیش‌بینی پپ در مورد شرایط رودری در مهر ماه ۱۴۰۴ که در ۲۸ تیر ۱۴۰۵ به حقیقت پیوست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/101567" target="_blank">📅 17:01 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101566">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be9c5de5c5.mp4?token=c_7EnTaFyMi3n8iqdYvBQcHSfxK7s84JTeGODL9szAqyv5DFZrIqK9h6npdOoOXoiDepXXPc-LfNzuoFsDT67N1HNAIOg9THN9apOH9YLbPIaTAKkPlabI0N5_FSLOVjk0wQdFDwJtAgJAGaet3O5O3zZ7wlTcV8Vempi_UohEhubZuur1GwVEkA1_TMpsqSsIt_aWDnSpi2gzTibumZ3ZbCyVQxMVzhEY5x11zAfY3UHTfcAp2cDFc05O4RNoN9e8MrfHKyiVWKDrPK_z5t_xWM0ao_86silveRyUOaFC1iE-dy5WtkGTV8P02NAMC3X1mK-sNbLNMI68PGp_B8C7s_Xxa4in1b4whwUmD0I-TGIdj3LN4lssZ70edPCHGY_PGhhL-0JBXiz8dGPWXkHbLuCSz7Aeq3zI0SBXPKFjGgOevsi8Yi-74w38sW958YvUhdovCZUcqhaZDbsq8uZhbAUklHT9IWoLdyTGncd9E03huL-3EoOuyQGandJ3lXtlWjrhD0sholrWn1F5r__R8bx1gkjjnV0S85zPmeSbYm3yTX2zWQhaBY9qC2jsEq-UK5W2W8CRSr5ZTMBUEElpMDBMOhjQzDYE4GGauAaveotcc96wELPsA2AlcWz4I2MDO5VCu7I8jdXC6p7LK62meCyENuw0dPhhYPGNRJJtM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be9c5de5c5.mp4?token=c_7EnTaFyMi3n8iqdYvBQcHSfxK7s84JTeGODL9szAqyv5DFZrIqK9h6npdOoOXoiDepXXPc-LfNzuoFsDT67N1HNAIOg9THN9apOH9YLbPIaTAKkPlabI0N5_FSLOVjk0wQdFDwJtAgJAGaet3O5O3zZ7wlTcV8Vempi_UohEhubZuur1GwVEkA1_TMpsqSsIt_aWDnSpi2gzTibumZ3ZbCyVQxMVzhEY5x11zAfY3UHTfcAp2cDFc05O4RNoN9e8MrfHKyiVWKDrPK_z5t_xWM0ao_86silveRyUOaFC1iE-dy5WtkGTV8P02NAMC3X1mK-sNbLNMI68PGp_B8C7s_Xxa4in1b4whwUmD0I-TGIdj3LN4lssZ70edPCHGY_PGhhL-0JBXiz8dGPWXkHbLuCSz7Aeq3zI0SBXPKFjGgOevsi8Yi-74w38sW958YvUhdovCZUcqhaZDbsq8uZhbAUklHT9IWoLdyTGncd9E03huL-3EoOuyQGandJ3lXtlWjrhD0sholrWn1F5r__R8bx1gkjjnV0S85zPmeSbYm3yTX2zWQhaBY9qC2jsEq-UK5W2W8CRSr5ZTMBUEElpMDBMOhjQzDYE4GGauAaveotcc96wELPsA2AlcWz4I2MDO5VCu7I8jdXC6p7LK62meCyENuw0dPhhYPGNRJJtM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمود شهریاری چه اجرایی کرد
😂
😂
😍
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/101566" target="_blank">📅 16:40 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101565">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ESoAeKjKSMzxA8p1LJLTrc6megQaia5rKxjojBTYBeFA-nju1Slsn6zagVf1fiqEFpqIf7weZue04nmTiA-ElHem7hYdCshjZAFsRnwqMSWqk2HVUedtHuXbtETb3Ehl1J3H9X63TW9dLED30Jxa7XwUYdG-w4pzU8aGYLLQrNLgghvjd3d3Avdi7wzW2RnBb2X-XCqLeVPo1vgXbDdJQ1TXvGTrlRSW2wjldAQ6IbPASUPpqoBhdWyyvMGxq0D7E3n_fhGCz1_42ZekuaLgJVDk5Tjq9RFZ3ZGMq_YuICt1q-dIsdVqvqGJmYLQ_tFiN90yaUY7MO6cXVejutRIBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
ترامپ: از این به بعد، هر زمان که جمهوری اسلامی ایران در تنگه هرمز به یک کشتی شلیک کند، چه با موشک، چه با پهپاد یا هر وسیله یا سلاح دیگری، ایالات متحده یک پل یا نیروگاه را بمباران و نابود خواهد کرد، از جمله آن‌هایی که در کنار یا در شهر پایتخت تهران قرار دارند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/101565" target="_blank">📅 16:36 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101564">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🎙
🚨
حمایت جالب رضا‌رشیدپور از فردوسی‌پور
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/101564" target="_blank">📅 16:20 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101563">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/318ac55e88.mp4?token=CN699ZVLOYaw6Vgp1wvuvMUgSVkct-uH37kw2_gpkBtVj840Qr_EJn3VNbts59iVGHcU1ohlpAsSFI--S6ijhFX_qzGasEgFxRBS-1Iv9Y1vleAmDh2NCI1PyUwQmf7ZIcohbdPk36INqETRaio-gR7DMM4MLrCcd4_YCi758NBpkVUmPA7YIAo7ongKRz7tD7yLiI0iKh6WwvTsfQfSFaXkupj6fqpXmUEqANpFZzEZEp-I4wxIM99hxlbjbndz6HjxWsnee5SSK3zShmljaul4ckyRhI4ryC8ueW1CaMEPT1Bux2QXT0l3wzATmpHu7Zc28x623sFAP7Gz_S6uGKzymD4Sbo63dcFp4cc0O7xMXVljth6tjBos1Z1cHm1XEwcinTkU5EUTSdLtict-NVfKZ-teI9UUVw8gAXs6rnRddP2xoknh16_UcEHJankNzPwKemLTn-vP1zsZ0uR00dGyCrr7WfUWOk8dLvx6PfFa7L9NqpOsqnCGwBTPxQqokMGEf3iVWVgsmOiJKXdtr3yCbRFmYMOPHgMmYvs9qLLmpJEphvUhFZ--n-Y9UMCqY-N6NRFqkTzuLD_FKS-7BpQqAmF8laL-7uDT7SytSRz9aXfgeigkP08k5fRhvE-6yDTGMbHW7N82_HTlBsyw9FMy6Gpf2vAV4VfC3oDbgNE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/318ac55e88.mp4?token=CN699ZVLOYaw6Vgp1wvuvMUgSVkct-uH37kw2_gpkBtVj840Qr_EJn3VNbts59iVGHcU1ohlpAsSFI--S6ijhFX_qzGasEgFxRBS-1Iv9Y1vleAmDh2NCI1PyUwQmf7ZIcohbdPk36INqETRaio-gR7DMM4MLrCcd4_YCi758NBpkVUmPA7YIAo7ongKRz7tD7yLiI0iKh6WwvTsfQfSFaXkupj6fqpXmUEqANpFZzEZEp-I4wxIM99hxlbjbndz6HjxWsnee5SSK3zShmljaul4ckyRhI4ryC8ueW1CaMEPT1Bux2QXT0l3wzATmpHu7Zc28x623sFAP7Gz_S6uGKzymD4Sbo63dcFp4cc0O7xMXVljth6tjBos1Z1cHm1XEwcinTkU5EUTSdLtict-NVfKZ-teI9UUVw8gAXs6rnRddP2xoknh16_UcEHJankNzPwKemLTn-vP1zsZ0uR00dGyCrr7WfUWOk8dLvx6PfFa7L9NqpOsqnCGwBTPxQqokMGEf3iVWVgsmOiJKXdtr3yCbRFmYMOPHgMmYvs9qLLmpJEphvUhFZ--n-Y9UMCqY-N6NRFqkTzuLD_FKS-7BpQqAmF8laL-7uDT7SytSRz9aXfgeigkP08k5fRhvE-6yDTGMbHW7N82_HTlBsyw9FMy6Gpf2vAV4VfC3oDbgNE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
آنالیز بازی پائو کوبارسی ستاره تیم‌ملی اسپانیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/101563" target="_blank">📅 16:02 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101562">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">‼️
🎙
کنایه علی علیپور به علیرضا بیرانوند به خودم اجازه نمی دهم درباره علی دایی و کریم باقری حرف بزنم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/101562" target="_blank">📅 16:02 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101561">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🏆
🇪🇸
رسانه‌های اسپانیایی با وجود قهرمانی صحنه‌ها مشکوک داوری فینال رو منتشر کردند!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/101561" target="_blank">📅 15:40 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101560">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p4bPC8xxw_EulqoYaNzBvIVyExtZ8nkkurUhCK3SvGbJh4btwrl2oVdWEkyaPmpxXOAPcERKvIGc77iI57Rkc1lHatDPQOtXJl6UijhN9EzJ5tgcKZkjkmr1X3UUAewC1NoGyl03wJ7VPca__HGSUkYRQKKWsmCEcgSm7Rhx-XX3FeBkDql2o_O27De9zVg4SJlPXOOk3dIXChQtlvar1NoLwMVb-_EHgG1-Uv2zFANlvNbKhtuWAIfns8fNwz3xcuXRYwa1vcFOFewmHbki7KlNlVoOowKHiIgVgHDd1uGXcsuu7Z_WDVfFGJXpGnTiLTgYZk3a8kwXeYx5XWQOeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
منچسترسیتی قرارداد فیل فودن را تا سال 2030 تمدید کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/101560" target="_blank">📅 15:33 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101559">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e21d92126a.mp4?token=fPQw-Jszb7tiDR9yBi1W9iJml1jVfeggwuJzfjyLPYv76IdfwOG82rVKpiA9M8iTWR5gx1HmXZNTrs6s0UWa49VfsP_5JVmz4Ku5BEgFmJ4o0rdYL67OUw_eTE7TySFFyLE75zeST-V5E5LeH-x-X4g1wmuAMBTikKiSc3Oa36b3L_-R-g3MgcIOHXJbOPQhc-yHYoVCjRrSP6S1bAvhl1x8USkKS7OZ9_DBJ2XIIu0XK_MMYV3j3WH3LQjrlIo90erpWuTLtc1F9xAzwB3zGJMGIH_2fAnVR7iijIY3nNRbLff1td_kxqfyOeMP1hj9l-n_YT0WqF579z2QiLuMm7M0mqyN-Z0A8gat8V7iWXVVYDZa76d9gkht9XsKabZwump1Cg1m_HbOYylwkNiAjNCwRHlDE0E8x7KOtOpAf_kTCIPKTL0QJd9lnIpnA0baOdwudt52BsPfrRuj98WYq9QtSW2cIXh3XmkrBegm075etE_zb94ZXUSriu49sTjzQK7jAxCcE9MR38QhSrHea5Fvh7ZjC0NfvfMZrIXcf6aVTV603mGldWOsPY2sjT_zwH6ldjb_YSVKsPQsPNlZhNGyuGgwkI3QDNYSzIgK1mFoNwSSjLMAutnzpnptKHAjLOW2qJz7XZSdLA_Es9WCXmDqVGlDLqo74WFVCqcBXjE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e21d92126a.mp4?token=fPQw-Jszb7tiDR9yBi1W9iJml1jVfeggwuJzfjyLPYv76IdfwOG82rVKpiA9M8iTWR5gx1HmXZNTrs6s0UWa49VfsP_5JVmz4Ku5BEgFmJ4o0rdYL67OUw_eTE7TySFFyLE75zeST-V5E5LeH-x-X4g1wmuAMBTikKiSc3Oa36b3L_-R-g3MgcIOHXJbOPQhc-yHYoVCjRrSP6S1bAvhl1x8USkKS7OZ9_DBJ2XIIu0XK_MMYV3j3WH3LQjrlIo90erpWuTLtc1F9xAzwB3zGJMGIH_2fAnVR7iijIY3nNRbLff1td_kxqfyOeMP1hj9l-n_YT0WqF579z2QiLuMm7M0mqyN-Z0A8gat8V7iWXVVYDZa76d9gkht9XsKabZwump1Cg1m_HbOYylwkNiAjNCwRHlDE0E8x7KOtOpAf_kTCIPKTL0QJd9lnIpnA0baOdwudt52BsPfrRuj98WYq9QtSW2cIXh3XmkrBegm075etE_zb94ZXUSriu49sTjzQK7jAxCcE9MR38QhSrHea5Fvh7ZjC0NfvfMZrIXcf6aVTV603mGldWOsPY2sjT_zwH6ldjb_YSVKsPQsPNlZhNGyuGgwkI3QDNYSzIgK1mFoNwSSjLMAutnzpnptKHAjLOW2qJz7XZSdLA_Es9WCXmDqVGlDLqo74WFVCqcBXjE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
🇦🇷
رفتار عجیب بازیکنان آرژانتین در صحنه اخراج انزو فرناندز که وایرال شده !
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/101559" target="_blank">📅 15:20 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101558">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f9401eccd.mp4?token=IbJJh_sVoHTpIdBZ5stoh1AKn5akqmQL4oXVVJks0X347c3_684ZPBjtTPcgA8UAcASIW1iBGCm2whAWaocsuz6X261cnwOdbmjHOSB0tJIkmQX5RwNnV6vVLFBiW3iJ_Q88Xe39Zukhv4ifMsiJhy2-ODOtt1owGV25G0Q1f2FohgWH-9yITRPIcm5xyZigC6Q6C3DQEm1ThAanyEuRvirZBequ2wU6QpHnQNvCWV2aGCFvDghMpmu2e2COQyhsrT4fKQGx5ma55bnGK0M1rxQYWefQiRsdtcTjKai5xCJJAtL7oqd-yWAYaKjFTyFYqykS71dRuhHe75V3X36yvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f9401eccd.mp4?token=IbJJh_sVoHTpIdBZ5stoh1AKn5akqmQL4oXVVJks0X347c3_684ZPBjtTPcgA8UAcASIW1iBGCm2whAWaocsuz6X261cnwOdbmjHOSB0tJIkmQX5RwNnV6vVLFBiW3iJ_Q88Xe39Zukhv4ifMsiJhy2-ODOtt1owGV25G0Q1f2FohgWH-9yITRPIcm5xyZigC6Q6C3DQEm1ThAanyEuRvirZBequ2wU6QpHnQNvCWV2aGCFvDghMpmu2e2COQyhsrT4fKQGx5ma55bnGK0M1rxQYWefQiRsdtcTjKai5xCJJAtL7oqd-yWAYaKjFTyFYqykS71dRuhHe75V3X36yvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
علیرضا نیکبخت جواب بیرانوند رو به زیباترین شکل ممکن داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/101558" target="_blank">📅 15:04 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101557">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iHs_UZZdbzFIOF6hL4mY96v-H21k7eLU-iXfCtfhefeyXDES9U2lwdOjhfmuRajK3syx8LKG6kTwp8xPpI6PRG5HiSxIpE_JkTzN_eyskb-XoL1tRhUYGFljW_Zk0_Bs1x58O4cemHqYgF1mhlzLtOpdj4cg6SQVpx4fSFPUNiI1LDX9WY1jn1CwTL1PHgHaRzGhMQPcmq-UBcZ9-KnM6b0KnSGtXTZkdkT7Glnhe9qSWZr5valcenBEgzBq78NzBGG7alkZxIjo_BOTqZk5gFn-l5KFXO008v88V5U26nkE0nyNXrXyYu_oIMopEm3izBdA_0g5OZTKFE3Cc3Untg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
بازیکنانی که در این فصل، در بین پنج لیگ برتر اروپا، در تمام مسابقات بیشترین گل و پاس گل رو دادن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/101557" target="_blank">📅 14:56 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101556">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a761e81f7f.mp4?token=M7HTVAp4Rj9R-8LVwm5gQs28YcetI4JxhxhfZ19zqnxutc_Zjy8oZflROtmQFTnFDVX9nlWIvSlekYryy820GOKoPpaKJ5OHEUcRPyWy6Dn49F3mgJeHiY00MzqWgBBeHp6wCnUgEk2hqKB8T88v0I-tLmSC33g2Baj4tmhmE3LTAuQWDdt_8a-ZAOSGPPEIUdEJ85Kn00IP3EU44gkbOl5qmff84DV6u5kGKSvAyYpwyRZusF_ZaNDiOTmPE8RgAyCDUVZu2ZYR2fUBj2-xcwMX7DH0L5RwvJmmxlmhH5i_MCMxP0xj9jgK2zC_iBqqGPtZMVR0M88ISRjEM5ihjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a761e81f7f.mp4?token=M7HTVAp4Rj9R-8LVwm5gQs28YcetI4JxhxhfZ19zqnxutc_Zjy8oZflROtmQFTnFDVX9nlWIvSlekYryy820GOKoPpaKJ5OHEUcRPyWy6Dn49F3mgJeHiY00MzqWgBBeHp6wCnUgEk2hqKB8T88v0I-tLmSC33g2Baj4tmhmE3LTAuQWDdt_8a-ZAOSGPPEIUdEJ85Kn00IP3EU44gkbOl5qmff84DV6u5kGKSvAyYpwyRZusF_ZaNDiOTmPE8RgAyCDUVZu2ZYR2fUBj2-xcwMX7DH0L5RwvJmmxlmhH5i_MCMxP0xj9jgK2zC_iBqqGPtZMVR0M88ISRjEM5ihjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سگی که شباهت عجیبی به مارک کوکوریا داره و حسابی وایرال شده
😆
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/101556" target="_blank">📅 14:40 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101554">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eUrjYJJIfFzLKTgJuTOgyKf3fLwozNg2qtUIkk3nEPhb4QkGaabAGkU68QpZd8yPiEytGHHMeevDy8oXmBYicXpPPx5Na1rbFwKSrzC4gO-Y-WvNG63OALRDyswiSrvJMPlAjr7nynpEHu-pvHhXjNPil8S8DMQBQpWPhqxAzzUiKB7Wa1iRY_qKZ56f6tNmY9yrRK5dKcWIVVXgsYVO-kWEioOcnrH2XNxmp9Tprt03f8qvJ2LPhfVP2HTJ7iWyIqS5gxDLZWiNh_k4iCUF55sNn6-6Ik7tdXnnp1zxniqj0t8nCAsdxICtHCPNc62OIEXwUv4AeorNI64QqKsKkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rrvebBrGW5flHk0bAmfSjmQM7oURMVZ3x0PU8fB1sdV9bi5Tzgr6IzO9VFWoEFOQykiaSWfqeBmubuFWZ53CLUzefdGNxFUvYYSAJtL8tJmflckGPfVnEC1nvBZ1GFM-hDRTaoMRoXiNvN0Mc0FzHzcZkkIWN_sLM0Urigiw3kEz2Nr1YZrNt39l2s-0sqUNaLXuZ80Ru_OVGVEKmRIXV1xkfEyW_IQU7grJkn6eXeiZSUQnRgQearuE8jETfgU1OyRr_mZSpFgwATljsOzbeKgoCpd8aOC32eES5vOuVir2xrQjPnAZhWRqLcAhsdWKVQlGxFWN084fTf1Ee4ogVQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎙
خوان مونفورت، عکاس عکس معروف مسی و یامال:
من به خدا اعتقادی ندارم، اما این عکس نگاه من به زندگی رو عوض کرد. انگار همه‌چیز از قبل نوشته شده بود. هیچکس حتی در یک فیلم سینمایی هم چنین داستانی رو باور نمیکنه! هیچ توضیح منطقی یا علمی واسش وجود نداره. یکی به بهترین بازیکن تاریخ فوتبال تبدیل شد و دیگری حالا داره جای پای اونو در بارسلونا دنبال میکنه و در ۱۹ سالگی هم قهرمان جهان شده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/101554" target="_blank">📅 14:37 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101553">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oY7nUqEOcU56lGomh1NXbhPClAP7-HyLeCg1DCnhNcjrsXOicJ4lSwz7OtLbInRCEwrFo0_4PTqgXe-h02ISTn4U1GyLyW2Z3qHlbCpzx6BF2Emjxryfhs0chxVplUkhNGbWcBNo_Cul8P3MreLMXYfszgnPfVCfhvuvdgrZiwPwUsbqbBpiWYfCECtM4UkB5YK1-WmYoN1pMEuh21FSNs6h-IBXaaWd2l7kWWLJEnVXOl9zilLTNwAKkO91Eemnx-XTrhC1cGgTn809AAL7nWr0tAKRIICb1QflIsD7RN7defJL12ouFkSZ0gDpT6i91VhrQG1TMpqPqsNcJzs_lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
نیمار دوباره در برزیل جنجال به پا کرد!
باشگاه سانتوس اعلام کرد نیمار به‌جای سفر با تیم برای دیدار کوپاسودامریکانا، در برزیل ماند تا روی آمادگی بدنی‌اش کار کند. اما ساعاتی بعد، او در یک تورنمنت پوکر با مبلغ بالا در سائوپائولو دیده شد! این اتفاق باعث شد خیلی از هواداران شدیدا از او عصبانی شوند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/101553" target="_blank">📅 14:25 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101552">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rW-GuNshL9_JLUYPoE_nC3K1hmdaVeYFdNMccW3NeIQjxedaAIU9fdqAk7CgL9kxjR8dBxKEOQKpjQ1qm8d5Cr_LbgD4_1hpjlkGhbdBJfB18RsGB8wvDdQ1Xt06b-Q4TWKaRf5radeKhX8kw37NqV9xyUdsIMb_mal9cYtbLgbMIwA4g7BDBhhu1PSetHIJP-FZKsWSBOXlFzJ3tKr377RMZX8njhwzcD8b4PS2kXphXxudnroV_jX93Qa2AGkaSsSblBQp_uMTXN5RmIKTKaOns14oE7jKjqN8_odLJwU6hY4D-Br0iLirnBNlyWKsgecKPdpdDEHuSmevpvcwmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
🔥
الکس فرگوسن: "بعد از اینکه ایتالیا جام جهانی ۲۰۰۶ را برد و یوونتوس به سری B سقوط کرد، من مطمئن بودم که او یوونتوس را ترک خواهد کرد. بازیکنی مانند او در سری B بازی نمی‌کند. در آن زمان، رئال مادرید نیز به او علاقه‌مند بود، و با توجه به مشکلاتی که یوونتوس در آن زمان داشت، تصور می‌کردم که یک رقابت جدی بین منچستریونایتد و رئال مادرید برای جذب او وجود داشته باشد.
🔹
بعد از اینکه پیشنهاد خود را ارائه کردم، پاسخ او بسیار تکان‌دهنده بود. او به من گفت: "آقای فرگوسن، شما قبلاً با من صحبت کرده‌اید و من به شما احترام زیادی می‌گذارم، اما یوونتوس در حال حاضر شرایط سختی را تجربه می‌کند و وظیفه من این است که در اینجا بمانم. یوونتوس در بحران است و من کاپیتان این تیم هستم. آیا انتظار دارید که من آن‌ها را ترک کنم؟"
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/101552" target="_blank">📅 14:20 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101551">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d88e870288.mp4?token=gNy8BFAeVYJ2mzIpI4CNXPI17ACg63SajR7oPeoYSG6nsgToIh-7UnbyXRDY2PcHiG27DTVh9Ws2rapsyAaV6FSw9sJOnt5qQ_ODDsCZMd-_Jeq4jTW5lAMKk_tLGNpUjhhgvRv5wH9cpbdLZMa5WfJHWlkdu5wqMV52ckw3oy3XQ_LQmYD-vzqf9J-FSr4KjhJydUYC-3L0cQ6TBBYFcHxX9s47XX_U0bQEpYCYYFNLk4SnwOXN74YVzxvScMolM3J0AB4eOC_HV8NbcrvBcN8WI-hb76qOU7EXkxpFVjibTZq5IVI9MO3b8A0quOBN3L9iwruIII-PFXAUyy0EdjfM622W47czxtBOx061nqUzuh6Y27lXCwv9A9we5Mji0V0bMCKLOfxjgVFFp_UMtV4qsINQS8owMIP3BjRAeDC3VmLJl0rbMPTnCZTLxCslVAslj-G68xo0wpB86ZX2G1G2G-5u2lplFdZIp-UcV9Cpwmple881HSa0PpKboTP5VPGBMq1PpZ5EJjo5LgP7_vcgkZbD2PvRBcEQICJtfhU2Dj6FdvL-qE92n6usYfS9LmUF7IQEAIt_Y6ShTtX1dBoJYJE2N-YN7H7XvJ7oz5_-zH-0odf0nigeq1IxqmzrA1FwVtTdt_VrFrmVzOjYwDjmIsu4YgGGR2JstCdFXpo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d88e870288.mp4?token=gNy8BFAeVYJ2mzIpI4CNXPI17ACg63SajR7oPeoYSG6nsgToIh-7UnbyXRDY2PcHiG27DTVh9Ws2rapsyAaV6FSw9sJOnt5qQ_ODDsCZMd-_Jeq4jTW5lAMKk_tLGNpUjhhgvRv5wH9cpbdLZMa5WfJHWlkdu5wqMV52ckw3oy3XQ_LQmYD-vzqf9J-FSr4KjhJydUYC-3L0cQ6TBBYFcHxX9s47XX_U0bQEpYCYYFNLk4SnwOXN74YVzxvScMolM3J0AB4eOC_HV8NbcrvBcN8WI-hb76qOU7EXkxpFVjibTZq5IVI9MO3b8A0quOBN3L9iwruIII-PFXAUyy0EdjfM622W47czxtBOx061nqUzuh6Y27lXCwv9A9we5Mji0V0bMCKLOfxjgVFFp_UMtV4qsINQS8owMIP3BjRAeDC3VmLJl0rbMPTnCZTLxCslVAslj-G68xo0wpB86ZX2G1G2G-5u2lplFdZIp-UcV9Cpwmple881HSa0PpKboTP5VPGBMq1PpZ5EJjo5LgP7_vcgkZbD2PvRBcEQICJtfhU2Dj6FdvL-qE92n6usYfS9LmUF7IQEAIt_Y6ShTtX1dBoJYJE2N-YN7H7XvJ7oz5_-zH-0odf0nigeq1IxqmzrA1FwVtTdt_VrFrmVzOjYwDjmIsu4YgGGR2JstCdFXpo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
📊
نمره‌دهی به لیونل‌مسی در بازی فینال جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/101551" target="_blank">📅 14:00 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101550">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c3187f185.mp4?token=Jnj1RFZpXKxBHUjlA7FTRKIykF6dBVcJd5Xp1XU_GO9JR-Yd6dA0urHZrOm5G2TmVnCtus9miiVZPVdWNY6J2VMIFuliMPnFJeeZL2C4jO19Mahlwl1GDmq9TKgyS_dA_coLKahgLLQBWQxRs25AYQmUzgwo1yzMuNU-0UUPSC-_kGudvQq08uct5GQCcR-hDCFjeqn5E_SpsMRlksyRk3U1NYKT6a-prxXBAWOnYFn2rD70tY3aYnoAOLNtuHUnXeZY6QJBdOFukAAL9XZausG6SA2OTlnO8LNcnLxCOwg1w_UBsr9I8kIXpLjiCLKh4REeeuP2J1aN2wq_5fAZE4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c3187f185.mp4?token=Jnj1RFZpXKxBHUjlA7FTRKIykF6dBVcJd5Xp1XU_GO9JR-Yd6dA0urHZrOm5G2TmVnCtus9miiVZPVdWNY6J2VMIFuliMPnFJeeZL2C4jO19Mahlwl1GDmq9TKgyS_dA_coLKahgLLQBWQxRs25AYQmUzgwo1yzMuNU-0UUPSC-_kGudvQq08uct5GQCcR-hDCFjeqn5E_SpsMRlksyRk3U1NYKT6a-prxXBAWOnYFn2rD70tY3aYnoAOLNtuHUnXeZY6QJBdOFukAAL9XZausG6SA2OTlnO8LNcnLxCOwg1w_UBsr9I8kIXpLjiCLKh4REeeuP2J1aN2wq_5fAZE4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
صحبت‌های مجتبی‌پوربخش علیه میثاقی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/101550" target="_blank">📅 13:40 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101549">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c0345d2fb.mp4?token=nLIu4afoMC4ia8Clk1Kir5OeMsCWZMGjkBFCBK7TSUDprGlVnh94PaD_CnJ4NzLPLmNj2rjtIDQrO1ffkaE_PeaXrrTNu2SEl1kugJCi6YktadUGpAAczXTOO3bsJYhBd4CKjBd5M8V9gBKjgM8QhtL_m6VyYN3fwQvNutmkz_Y5jm7w5loizMVxYzaPRaLqGegBKHRi4ZmThxMYSFHSJvpYpZcx8Q1bazYKAT5yRZ90ic9c4Or0yCAsvlWUIc4-A0Ijyh5FAUOp5QOsTo0KJfJfZvzsdMVtSkM2L7xMZPJefLNZ91UQ6trjyWkT5kV0jJufpuefawyqd7r-ExbxEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c0345d2fb.mp4?token=nLIu4afoMC4ia8Clk1Kir5OeMsCWZMGjkBFCBK7TSUDprGlVnh94PaD_CnJ4NzLPLmNj2rjtIDQrO1ffkaE_PeaXrrTNu2SEl1kugJCi6YktadUGpAAczXTOO3bsJYhBd4CKjBd5M8V9gBKjgM8QhtL_m6VyYN3fwQvNutmkz_Y5jm7w5loizMVxYzaPRaLqGegBKHRi4ZmThxMYSFHSJvpYpZcx8Q1bazYKAT5yRZ90ic9c4Or0yCAsvlWUIc4-A0Ijyh5FAUOp5QOsTo0KJfJfZvzsdMVtSkM2L7xMZPJefLNZ91UQ6trjyWkT5kV0jJufpuefawyqd7r-ExbxEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
🎙
خاطره بامزه علی دایی از معلم زبان خود و کریم باقری در دوران حضور در بیلفلد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/101549" target="_blank">📅 13:20 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101548">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fbd74933b1.mp4?token=HIZw1b0qWnD2RTVWKYzxK45UlA0vZLbYqaQhXQGSyIVc_j1jzr94o7gzx50tWy4wIw3uLRNNq_VEFxaoxUwkpXq0Z3TQWMJU1KeUWbeQvFX_dq5tWnA-O9XX6VgE1QxOtEYC3LXvmFa8VauPqKcvUJrhzv0LtOGO-5wZX2PrkKyKmyiOfkG9hXIaUjdYUM10TOfe2AowEV4OS1YWve7MdbUAthAxN-X-lszVWKsbxvbM7cG1EVK50tUlzbQESprZvb5kcS0dEuy-a79usuo5tJtBRGyyuZ8naY7FIHw_Q4y1FDKnXyzG2MrP_ibiqnn6-gIPI8jJKCImuoxIIhUsZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fbd74933b1.mp4?token=HIZw1b0qWnD2RTVWKYzxK45UlA0vZLbYqaQhXQGSyIVc_j1jzr94o7gzx50tWy4wIw3uLRNNq_VEFxaoxUwkpXq0Z3TQWMJU1KeUWbeQvFX_dq5tWnA-O9XX6VgE1QxOtEYC3LXvmFa8VauPqKcvUJrhzv0LtOGO-5wZX2PrkKyKmyiOfkG9hXIaUjdYUM10TOfe2AowEV4OS1YWve7MdbUAthAxN-X-lszVWKsbxvbM7cG1EVK50tUlzbQESprZvb5kcS0dEuy-a79usuo5tJtBRGyyuZ8naY7FIHw_Q4y1FDKnXyzG2MrP_ibiqnn6-gIPI8jJKCImuoxIIhUsZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
وضعیت رئال مادرید در این روزها.
🧐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/101548" target="_blank">📅 13:03 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101547">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qiMGEyjvmFniWqBwDbP9xFVz3gNrt9OGETcI5SPkQ5_LdAYAxxIxHi0eDo-Uj7F3ROARlt-wXdkFvmwq7pLVST7RLA2H1vBLsTKXjKXYhWqigrdIXdQFagAQsiG5etBFgzMyfwOYyXg0ERXdpmOW_82SGRjzJOrp7es7JlgG7CtPQSHIdZj2m2wiT5lEQVnBiHEO4WbrcjP_ZZlDlLRXSX9GuytrwJPYqA3fM983qvXb6WQp2u59j3MRIU8mYSNjUVXR_IAbcFZei7W531sZ-BXKdUf5wMteKU9VquB7XKgTazxNtf8xBxwMRFc48S6plRuk3lxnvRVnmYjR5AttAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🔥
وینیسیوس و زیدش بعد عمل زیبایی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/101547" target="_blank">📅 12:40 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101546">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e1e8799b7.mp4?token=KKfbF5Q0aKLjdrNVWtXhFB-Me5oqn9rJCfnMXS2dZDh3tAzqYe27OV29WEt1ya_XE2IJQXeJrQyzXQzxejy4RtxRdUofviVK0kv-tQZ0XKD2ETmtfVKpMNIpear3Cq3wQjHB3tEjZPzK8BBguTNLG6IydTpZltM3O5Ux6W8VbY_UNv1Lz9IvQvez_No17UkDtM545tcVPfHVRHOlEpoo3yFZOL4KW8yu1ssr3cgSF1ejZ_ck2PO5zCKgEDkuOxsCscWNPgOOGjkpRxswzN49Zwp1XeZaZkdqZFyzop4-I_RX1XIstCtPb3P_mDqD84BO8D0ybLeJyRT4EssiymMxoB2ud7sk_UvU2MHPBld3jdQ5AJvxC-A1g4eEJ5eqoOZWI2Uhp9GM4nDJQ8YIpqGhE0HWvt3dNSh-uyxXsp55BOYt2L_WYNgdUWTwaJyUNKO9_NpfEeejCOsrS8L6IDMOvRWpnVKVugVUSOeJdPm_wYa7MCEQc1X44VuPlc-nfYZKlc1WZ8BzLRXT4NOzXAtd5uIjwqCBDFGpCJ075-k4qOAi7fbf3k2LhhWRnySaQ0JBN7BIbwpNNOTtHsKjRn_KdrxZtawA7iNol_UFSF17UVUo1RPdcGKLx13p5BFOGv6DBTnn1-f0CKVBNbjMpB0BE2QeCbD_DvmJU8l9NAL-9aE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e1e8799b7.mp4?token=KKfbF5Q0aKLjdrNVWtXhFB-Me5oqn9rJCfnMXS2dZDh3tAzqYe27OV29WEt1ya_XE2IJQXeJrQyzXQzxejy4RtxRdUofviVK0kv-tQZ0XKD2ETmtfVKpMNIpear3Cq3wQjHB3tEjZPzK8BBguTNLG6IydTpZltM3O5Ux6W8VbY_UNv1Lz9IvQvez_No17UkDtM545tcVPfHVRHOlEpoo3yFZOL4KW8yu1ssr3cgSF1ejZ_ck2PO5zCKgEDkuOxsCscWNPgOOGjkpRxswzN49Zwp1XeZaZkdqZFyzop4-I_RX1XIstCtPb3P_mDqD84BO8D0ybLeJyRT4EssiymMxoB2ud7sk_UvU2MHPBld3jdQ5AJvxC-A1g4eEJ5eqoOZWI2Uhp9GM4nDJQ8YIpqGhE0HWvt3dNSh-uyxXsp55BOYt2L_WYNgdUWTwaJyUNKO9_NpfEeejCOsrS8L6IDMOvRWpnVKVugVUSOeJdPm_wYa7MCEQc1X44VuPlc-nfYZKlc1WZ8BzLRXT4NOzXAtd5uIjwqCBDFGpCJ075-k4qOAi7fbf3k2LhhWRnySaQ0JBN7BIbwpNNOTtHsKjRn_KdrxZtawA7iNol_UFSF17UVUo1RPdcGKLx13p5BFOGv6DBTnn1-f0CKVBNbjMpB0BE2QeCbD_DvmJU8l9NAL-9aE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
🇯🇴
استقبال از ادهم‌مخادمه داور اردنی(داور چهارم) فینال جام‌جهانی در بدو ورود به کشورش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/101546" target="_blank">📅 12:33 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101545">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sttStQe162y2nzz4FnXYAG6b1AOLASD1Q_xRR5ZEhBXPpQnQgKevTpDTbXvyCRJS03XIJYQlK0xU_m_wk-uS7IrAb93uV4r8yv2vptAf8rRbRv4Aa5pVkgSNxhYbLBDWItgGvhA3SN83UA7AL8CeWI-SItRqnwSA1EMNyDZsoI_C0s-PoMly5yt8YrD5Z5uqBTGUgmB3vh8MGIHIm6khARz2O5u2ZvKFb47_ZP7xE6-CNznhlNFfqkFQiK995Ph-csMwS1wrKrRsrHxFXhb-lof9kfNBR9N5YyuY-1lqtRRd8JP1HK5CqxX5PDaeWUr6DidWhXZrXnOeAd_PsX6uXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
۶ تیم قطعی صعود کرده به جام‌جهانی ۲۰۳۰
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/101545" target="_blank">📅 12:21 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101544">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
✔️
آپشن های متنوع پیشبینی
💥
برداشت سریع با کد پریمیوم ووچر
🔝
با ضرایب بالا، بردهای بزرگ را تجربه‌ کنید
💵
پرداخت آسان و سریع با تمامی روش‌های پرداختی
📣
30% فریبت ورزشی برای واریزهای کریپتوباکس (ارز دیجیتال اتوماتیک)
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
••••••••••••••••••••••••••••••••••
💠
لینک اخبار و هدایای سایت
👇
👇
🔸
https://t.me/+ioIBrQfqMLtmMmEy</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/101544" target="_blank">📅 12:21 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101543">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sUEyDw94DkAkbBs07CtPcaO2ph6IQ-kxpQqrok2-BqYwG4cIC4huGbYI0066bS9WKO0jvqVaM9BHmZhjuvrIMJzny3Az8EqKrk9R-hSRBA0fTkQzTOduolLswKMzdarDvlSzVyWTluEU5tb6-pBHT2xpwwSEp6XI83VBXTK8NRpG6DmDQ9cP5QZHvUZXchTag_jrsjla8togneJxH7IL5fZeVlLSLRd2jWRIppAs7xzftzTP5j4pvx5fc9SLBpOl-P477e8Eyp1W_9701bjPSvIWbVXDGDSa2X0fXMfIA7RPon8bNwIkpPFV7-TWBoo7HqrUOqCIhcVbYL01Dr0X8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💎
سایت پیشبینی
YekBET
💎
🇪🇺
لیگ قهرمانان اروپا
⏰
شروع بازی ساعت 20:30
🎁
100% هدیه ورزشی ویژه اولین واریز
💰
محاسبه نرخ دلار با قیمت 2.200.000 ریال
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
📲
@yekbet</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/101543" target="_blank">📅 12:21 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101541">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bbcad2324d.mp4?token=ZiVODoLK-PKL9zYv3qdSBuwmoifPsLMk4q0xofJFP20YvNmaII-Ars93fxgRlhlknblbYG3w1ReITPnuEyHtCgfFY7n_whQpp4hEUYPYmY7MAIveCLGstOr7ArE4PsvHIvBwzCjmIHSf9yyRiwOtAkcgAN1gZ0iy4nkxEh9SDeX5ip7sRKcygIappH5JgIPN3JPUqfXIIR3t0yDJRLpcwsfrmAj5obX_F5GHo-bHu7U70QuUYn6n2hu3GrC5kCxGYrA4pUCYDXApnbR7gXMfTd8zZr1mWtHFVf8VcjIbqs_7jC_tJFXfU1rznGZeX1nvQ7zKLhONJyaIfMfmTA0yjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bbcad2324d.mp4?token=ZiVODoLK-PKL9zYv3qdSBuwmoifPsLMk4q0xofJFP20YvNmaII-Ars93fxgRlhlknblbYG3w1ReITPnuEyHtCgfFY7n_whQpp4hEUYPYmY7MAIveCLGstOr7ArE4PsvHIvBwzCjmIHSf9yyRiwOtAkcgAN1gZ0iy4nkxEh9SDeX5ip7sRKcygIappH5JgIPN3JPUqfXIIR3t0yDJRLpcwsfrmAj5obX_F5GHo-bHu7U70QuUYn6n2hu3GrC5kCxGYrA4pUCYDXApnbR7gXMfTd8zZr1mWtHFVf8VcjIbqs_7jC_tJFXfU1rznGZeX1nvQ7zKLhONJyaIfMfmTA0yjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
بازی‌های افتتاحیه جام‌جهانی ۲۰۳۰ به میزبانی سه کشور آرژانتین، اروگوئه و پاراگوئه برگزار میشه و سایر بازی‌ها در مراکش، اسپانیا و پرتغال خواهد بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/101541" target="_blank">📅 12:02 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101540">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3cde737c1a.mp4?token=lgZO2BCeXyZJix1sCpMmqsn1zn3vQHjyxhU59MnoF_SMj6GjfHFT9--8hz9xFoZiCBGtEOphwG2ljwOLRWA4O9wmsvDiFvnN8_2_Z0bkZya2eRs4qomPFMh8lYk8bi1e4MdBTc_ucFj_H8Sqf0Ys1LoK1h4MZdsXgm2OoSuWxvz6iSFUZnYLe0HiHRGi0nfqz75R21aQu4HU-76509NxSv9QXLfDrF6QSrHcUC4pU_cqM50G30FWv8USMTXeJ5OmGa2xmL4P125_Qpsvnu7O4BughESWKJDOai0N_pBWnKInbllewzLmczCQ6FGR6aK_-QkC5YlGYeNzt8gn7pchag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3cde737c1a.mp4?token=lgZO2BCeXyZJix1sCpMmqsn1zn3vQHjyxhU59MnoF_SMj6GjfHFT9--8hz9xFoZiCBGtEOphwG2ljwOLRWA4O9wmsvDiFvnN8_2_Z0bkZya2eRs4qomPFMh8lYk8bi1e4MdBTc_ucFj_H8Sqf0Ys1LoK1h4MZdsXgm2OoSuWxvz6iSFUZnYLe0HiHRGi0nfqz75R21aQu4HU-76509NxSv9QXLfDrF6QSrHcUC4pU_cqM50G30FWv8USMTXeJ5OmGa2xmL4P125_Qpsvnu7O4BughESWKJDOai0N_pBWnKInbllewzLmczCQ6FGR6aK_-QkC5YlGYeNzt8gn7pchag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
علیرضا جهانبخش: به فردوسی‌پور قول دادم که لباس محمدصلاح رو براش بگیرم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/101540" target="_blank">📅 11:40 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101539">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h1hIfD25OnWbI0JPzX4tMjUhbc2lMTaLw7-XuKcn1qNPHCvgbGEEOGwpIQK3T_y5m-omg58PNSEWAhAiisivmqEfG40bsk6zcEi-92RVp0-e6pOIVAFJdWB9UUbl1mczbdN7tLk9nU2UYD-zg4QJlkEvPvnNPUGUNp6HvirY89QgDq1oc0Czc2uSSCzGPuYApTaatF-qEu2EgIGDD9_jrELUiygbozMYUpQW9kNkf6xwVwaK-2yDEPkWdsICp9YXmuwqXwM-1cx7E4iaSeMdOEbzzhIxVJLCiNQK-i7gTeJXGwjgdW6x9o66qgUa9PwnYepjyO-6FAQJ3zjfa533Fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
کیت‌دوم منچستریونایتد در فصل‌آینده مسابقات
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/101539" target="_blank">📅 11:33 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101538">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vQobgR1aHUbHo6D1im5P-PK1rpZaIEpU3IMfMwvB-DxxUErEPTtUExilSpAl661CxO3GnTQ0EE8hU7QcIlFx_riDd0DEXGuAYH5E5a0nqnaIXomMXl5O_-IME7hNgjazVo7_fXgPxN4nP4dT9x-CAkcf6BjFbTRSfGItfFCbi1Te0fXjInW-l4RI4lFigZsLbN33xQPWuggV5FA4zJQqZWgK2FwkcdSplAWiV627j-GthdykDLpMcHr7Z6_2abZ9YvQ9XMBw92wBh738NcOOTmcacLB81babY3UynAIieLZ8Ot1r0slsGKOMZB_dK-ldf1rCfhMmdBcI2bewb02Urg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
حمایت یحیی گل‌محمدی از عادل فردوسی‌پور
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/101538" target="_blank">📅 11:21 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101536">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/330d45af26.mp4?token=qU-GA9xbeC0MnoerKNeNGqzT8zupGsbDVV1aYygJgfsf6RYcy-IDEN_dfI9F7EgwHcV_6KO9SLyF8d5z7JIi-cwQHDlWMBZQmj4xJveMsZGw8-MAbHMqELZ112nZkpNRUgwa0iJpBFtiqSj08h68wR48ipxkbj-sxX4aHFYsNYSHSZAhsXl9_FpSqlCBfYkTC0ZPoPonseBIZxxi2TR136j74NeqRQid9DI-FOC8QPNpR8HwtrufakmbBI3o6dCefzlwauuF3YeQrVFEld5mHeMmarGuaUP8losVN3ZW__wKz1_e_mkQK29H5Lx0zrjZjgWaZDxsgWatfXvuwkp1RQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/330d45af26.mp4?token=qU-GA9xbeC0MnoerKNeNGqzT8zupGsbDVV1aYygJgfsf6RYcy-IDEN_dfI9F7EgwHcV_6KO9SLyF8d5z7JIi-cwQHDlWMBZQmj4xJveMsZGw8-MAbHMqELZ112nZkpNRUgwa0iJpBFtiqSj08h68wR48ipxkbj-sxX4aHFYsNYSHSZAhsXl9_FpSqlCBfYkTC0ZPoPonseBIZxxi2TR136j74NeqRQid9DI-FOC8QPNpR8HwtrufakmbBI3o6dCefzlwauuF3YeQrVFEld5mHeMmarGuaUP8losVN3ZW__wKz1_e_mkQK29H5Lx0zrjZjgWaZDxsgWatfXvuwkp1RQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
تمامی قهرمانان جام‌جهانی در یک ویدیو جالب
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/101536" target="_blank">📅 11:02 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101535">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41b3828f7c.mp4?token=e-_63VUpbCRtk3Ld3sCE9Tr6jcr4iinm7XqJ9DYFfr7gAmvnRHxSi8YQcUZqF1H9Voa_S7dtjd45bTvHxG-BB-PxCmleDuI9HOuLtNwD-EajRtyxYoW5L4tUwBWx3hu8IfntvSpWECjTEqd6CXbg6t5IdbedeRb244hZgRyopdtwdaqKUUv3ouQ0gWtjRTbXR1r3bPIagibtC89hcfQmbkdJAMiypFwOQGYNFNpIL94nFeon-OYzAR_uMuzGlH3yPZGVJ3n-shXhXvN3ahsvbQnoNghhCiMh1j2j7dteST8TN_wCWZBHU3QLmKpbGwAd_xO2Eb4HCVtgpDhahTN-GQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41b3828f7c.mp4?token=e-_63VUpbCRtk3Ld3sCE9Tr6jcr4iinm7XqJ9DYFfr7gAmvnRHxSi8YQcUZqF1H9Voa_S7dtjd45bTvHxG-BB-PxCmleDuI9HOuLtNwD-EajRtyxYoW5L4tUwBWx3hu8IfntvSpWECjTEqd6CXbg6t5IdbedeRb244hZgRyopdtwdaqKUUv3ouQ0gWtjRTbXR1r3bPIagibtC89hcfQmbkdJAMiypFwOQGYNFNpIL94nFeon-OYzAR_uMuzGlH3yPZGVJ3n-shXhXvN3ahsvbQnoNghhCiMh1j2j7dteST8TN_wCWZBHU3QLmKpbGwAd_xO2Eb4HCVtgpDhahTN-GQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقتی پول نظرتو عوض می‌کنه
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/101535" target="_blank">📅 10:40 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101533">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/191f51b3e1.mp4?token=l6ctcntkeHdsOhOTEBM0-XsjVa8Hv5jXJ9JZweAiZk05ztgcPN4CRZD7anAy6Z5bT9Xwue3MWmmYob1bHAct6iOza2pWYtwowS218jaWlfqsRL2iaP8No4nIyF2H9i4MaMdFLo9_tQ6H0ByqfxS2CLoYnJXL7AmtK0dLHuZPIlHZHmD3WJwlre5OM28PTRLj0HZjEhK9RyXGYJnEKLYqv93rGqCNpeg2gKWcl9OsvmcZlCB1YdT7pE1VuP0vqUpj6t1_5yinqJc39dzhowljkPkNkYDVaqBPFcJCvmMCKdNYBvB9D-Mrfzqv2CIPmWli0j36BEEYWQXT5COHn_xnCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/191f51b3e1.mp4?token=l6ctcntkeHdsOhOTEBM0-XsjVa8Hv5jXJ9JZweAiZk05ztgcPN4CRZD7anAy6Z5bT9Xwue3MWmmYob1bHAct6iOza2pWYtwowS218jaWlfqsRL2iaP8No4nIyF2H9i4MaMdFLo9_tQ6H0ByqfxS2CLoYnJXL7AmtK0dLHuZPIlHZHmD3WJwlre5OM28PTRLj0HZjEhK9RyXGYJnEKLYqv93rGqCNpeg2gKWcl9OsvmcZlCB1YdT7pE1VuP0vqUpj6t1_5yinqJc39dzhowljkPkNkYDVaqBPFcJCvmMCKdNYBvB9D-Mrfzqv2CIPmWli0j36BEEYWQXT5COHn_xnCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
یه سری ویدیو قدیمی از قبل آشنایی یامال با اینس گارسیا دوست دختر فعلیش داره پخش میشه که توش اینس وقتی یامال با نیکی نیکول بود تو لایو گفته:
‼️
🔻
اگه یامال یه میلیونر یا یک فوتبالیست نبود، نیکی نیکول حتی دو بار به اون نگاه نمیکرد!
﻿
‼️
🔻
همچنین ازش پرسیدن: «لمینه یامال یا امباپه؟»... گفت: «بلینگهام»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/101533" target="_blank">📅 10:26 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101532">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">😂
😂
😂
تفریحات جدید اسپید بعد جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/101532" target="_blank">📅 10:20 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101531">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d084b6a5a.mp4?token=e4v4-hdaBfoBDmgAiCht7mImT2WuFJFEwgtZC_TKl68I_TvPSoYclVyOHWFYqN06RzxHDnga-A6qe01Yeh2ktW9iR92mQZ0G3iPopfmiZCkQLP7HIDaxb_Stiv4PT4Jpuy5oYqBBy3we1HgMFmzzyyvJV1RqCrjnsNrYYrICmSa78DLx6s-RsKZkWtWiS4EvdWen-Oj4wLVmb44H3TNwBOUO_VnAQAKkqP27-x8Zn8Btd0kjrnqb-gdslNUopAp3ywpDahh78RSGNjujX9PjtmRDBI3MES_BhE84cvjm_MLHGXaNVRb0AsVLvC2iBiLFTa7WVX8h1XW5I9VkvzDXXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d084b6a5a.mp4?token=e4v4-hdaBfoBDmgAiCht7mImT2WuFJFEwgtZC_TKl68I_TvPSoYclVyOHWFYqN06RzxHDnga-A6qe01Yeh2ktW9iR92mQZ0G3iPopfmiZCkQLP7HIDaxb_Stiv4PT4Jpuy5oYqBBy3we1HgMFmzzyyvJV1RqCrjnsNrYYrICmSa78DLx6s-RsKZkWtWiS4EvdWen-Oj4wLVmb44H3TNwBOUO_VnAQAKkqP27-x8Zn8Btd0kjrnqb-gdslNUopAp3ywpDahh78RSGNjujX9PjtmRDBI3MES_BhE84cvjm_MLHGXaNVRb0AsVLvC2iBiLFTa7WVX8h1XW5I9VkvzDXXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
یادی‌کنیم از سوال خبرنگار صداوسیما از لیونل‌مسی که بنده‌خدا اصلا ایران رو‌ نمیشناخت :)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/101531" target="_blank">📅 10:03 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101530">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bFDll5_EVHEbEi5MLjvKzJq07wm-SmAqO4VhniJi6VsVJ4uyqsrg3BguTbDk_8lF-akPJde8BlzMQoUKLhqD5U7CUobbXKS_rH5Pv-JdJf_x-6oHKcO7alsJ609Rod5i29gLfPClm-tC3G6T-hPXrdVuJ_YlaL5otxKfuy3QS7O4H4V8rGgh786Cd7mlwBQWuChM-v7blC4uwkjBUM4GKNhumia-4cr6aiFAZSdQWb4IQhX48fmZEobYtYIUsNjs-O1p1syQdqdLsbhuJjUuBgXVHaLKq1qsdEqccwez0z20NfqAEk_klW7FMRN-HAf0QUQcokxhRgJ9iDdLHJSR4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📅
🏆
شش سال پیش، در همچین روزی لیورپول برای اولین بار پس از 30 سال قهرمان لیگ برتر انگلیس شد.
🎙
یورگن کلوپ: "این دستاورد بسیار فراتر از آن چیزی است که من تصور می‌کردم باشد."
🎙
جوردن هندرسون: "من بسیار خوشحالم که این عنوان را برای استیون (جرارد) به دست آوردم."
🎙
اندی رابرتسون: "ما 13 هفته منتظر ماندیم، اما هواداران ما 30 سال صبر کردند. این مدت کوتاهی در مقایسه با زمانی است که آن‌ها تحمل کردند."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/101530" target="_blank">📅 09:50 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101529">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZB2t6pXg_cjgS0bSUVS4UHvM0qzuuSy2YS0_Gu5ij8gw-MqUzL8OkvMqCJhu2ID2dJflIhS7vn2bmXbEIt2S1OWQ0vPsiPgHTZtTfPibT5pFlaF1mvLZJtj9uOczyC0pIJnh8Z6W2c6PE6dfGlbMsWBgvFbMp-rGshu3i6-RzGqsESIR9uKXVb08PEcFVq7-YdgvmuMKCtVRCgibrGCDfuU7f48g4ug_EtcscXLis4RkyY-9tvmHbjkZUICFzdwtWkFYOA2INiVOYLjpt12d08upWk8LDYJHTe9oFlI41l3Kfc2qAI5R44sR8uKljQMohNQzgzKYjUPZv22bAsjSXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
فابریزیو رومانو
🚨
🚨
🚨
🇧🇪
🔻
مارک فان بومل به عنوان سرمربی تیم ملی بلژیک انتخاب شد.
𝙃𝙀𝙍𝙀 𝙒𝙀 𝙂𝙊!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/101529" target="_blank">📅 09:40 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101528">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8781c60fd.mp4?token=nV6FjWRHJXGYqSrP3WPVM6MJfDZXX1VgxyhJOIlAF6uQcJH3QdQd9z6YsA2uAkGYFhvZJu73PZZNbaXqB_WPAsmdeAju5ZMDEAEUWXKX-lmYigooXpPJJiRT2v2LOGYbf7f1WeBLAuaECPz47T7qz9gI0dlKAPFGHm4J0encrNlRTrtBylNxydBYjr_FblHkoTFoNlm6MwwmYRqYpgno957VwViUt96_EZvOCw2Vo8sVe6kicacXT3qtp5L1AgWt7RKcG56yTJSsSBDsWU2qhkycwtpoJ3XwMUyLfJlp6oJcLDV4kjRJUTPerZsoMKC908zBHe1h9PxmHFrYAma-qQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8781c60fd.mp4?token=nV6FjWRHJXGYqSrP3WPVM6MJfDZXX1VgxyhJOIlAF6uQcJH3QdQd9z6YsA2uAkGYFhvZJu73PZZNbaXqB_WPAsmdeAju5ZMDEAEUWXKX-lmYigooXpPJJiRT2v2LOGYbf7f1WeBLAuaECPz47T7qz9gI0dlKAPFGHm4J0encrNlRTrtBylNxydBYjr_FblHkoTFoNlm6MwwmYRqYpgno957VwViUt96_EZvOCw2Vo8sVe6kicacXT3qtp5L1AgWt7RKcG56yTJSsSBDsWU2qhkycwtpoJ3XwMUyLfJlp6oJcLDV4kjRJUTPerZsoMKC908zBHe1h9PxmHFrYAma-qQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
فینال‌باز واقعی آرژانتین در کنار لیونل‌مسی فقط یکی بود اونم دیماریا که واقعا نبودش امسال حس شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/101528" target="_blank">📅 09:40 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101527">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d9304f085.mp4?token=u8_iBlMdmTprUkI47hh-uBVVW1bLWO7dOkG07NHT4IGOLp9J6vo-0gKLt42nDGc61FnCIUqcyD_LlpaQbzGLIiH5kw0fqVnjnvurejBv1BOhibjxn2OJX8TbiAKHOy-ubqLgYuW51X08__LLBczR1H-twO0B3ktYMzIMwqMUpcvabYPA2-Bv0FjHP1PS1-b3HCIGYt_WzmV5KGlOTeHLfQ44uh07jhzShrfqk8SUz_eIR5Wial3RNqGxGLoTvKyYR3L7NmPwPMFJIYp5chQQq2ACc386g6sb7oFfW-nodXOrtzdms-ZgoWPe9C_7jTqeu6oAxd3FCBqtDPpleUMAkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d9304f085.mp4?token=u8_iBlMdmTprUkI47hh-uBVVW1bLWO7dOkG07NHT4IGOLp9J6vo-0gKLt42nDGc61FnCIUqcyD_LlpaQbzGLIiH5kw0fqVnjnvurejBv1BOhibjxn2OJX8TbiAKHOy-ubqLgYuW51X08__LLBczR1H-twO0B3ktYMzIMwqMUpcvabYPA2-Bv0FjHP1PS1-b3HCIGYt_WzmV5KGlOTeHLfQ44uh07jhzShrfqk8SUz_eIR5Wial3RNqGxGLoTvKyYR3L7NmPwPMFJIYp5chQQq2ACc386g6sb7oFfW-nodXOrtzdms-ZgoWPe9C_7jTqeu6oAxd3FCBqtDPpleUMAkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
😔
پیام استاد وحید قلیچ به دونالد ترامپ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/101527" target="_blank">📅 09:20 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101526">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NeJIFyoq6gIZ3_v-U4P0p1Mk6g9CXwcdSLkNFe9k7hPoSOIZunaKYi9Ls5Q-AKlbsvmm2U0yWlheXbvhFSpSR8tOt35WX51VKQSyYVmOqaF3LUaefYwSSyk5PB6Ck6bQIYgmiMRZzzbSdXXeKzojgaP0seqKI__oH9h2tLfoafuz0Mn1lgTmBnFend3WEEKvzuPyP_d1AupmyNsWpUiL3zEZTyoBr7lJEGiJkHZ_LFW_yvFPJpMjOuqY7B1H1KLyxe8Zf57CGEJQb52cj91CxDSIAa0M_GhFhHc40XiG-udV1bipUHFiajpnWbdiX2Rg6yKpYQgXD6i1P97O48BmJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
مارک کلینمن:
🔻
جف بزوس، بنیانگذار آمازون و چهارمین فرد ثروتمند جهان، برای پیوستن به ائتلافی به رهبری آمیت بهاتیا دعوت شده است؛ این ائتلاف در حال مذاکره برای خرید بخشی از باشگاه لیورپول است.
💣
💣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/101526" target="_blank">📅 09:11 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101525">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab5d3c4f61.mp4?token=CEDsYgWuo3CQjtn0XoxnqQxppafg8-MviBA_cYsfkd8oiqs9pPL8uxFmBTdnq9LoYSp0CSJoqrgo9ihI3h80g4MhDMOoSHNgFhL8nVTMxKuR9KTDoqbKp9IE54LAT2JrbptCQLgNrnMIYnPXbKx921SN97PHHYZ6r75mdxBC4JMmBp8-QzLBfPPdy-F1KlNiLXhoFdn1qHbBTecDu71yYeigsriOM9sesc3h-CWqAnQaRFW_YKveP8NR8xZNIjYrxAX3nPrq_YL_5mcYuJH7fNnF9SfGWzxyQrhR-Yw2rexP-sIVDQ7fiZtPLvK1dc7pPJycgw5-QIFiJAS74VFzAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab5d3c4f61.mp4?token=CEDsYgWuo3CQjtn0XoxnqQxppafg8-MviBA_cYsfkd8oiqs9pPL8uxFmBTdnq9LoYSp0CSJoqrgo9ihI3h80g4MhDMOoSHNgFhL8nVTMxKuR9KTDoqbKp9IE54LAT2JrbptCQLgNrnMIYnPXbKx921SN97PHHYZ6r75mdxBC4JMmBp8-QzLBfPPdy-F1KlNiLXhoFdn1qHbBTecDu71yYeigsriOM9sesc3h-CWqAnQaRFW_YKveP8NR8xZNIjYrxAX3nPrq_YL_5mcYuJH7fNnF9SfGWzxyQrhR-Yw2rexP-sIVDQ7fiZtPLvK1dc7pPJycgw5-QIFiJAS74VFzAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
روایت امیر قلعه‌نویی از دیدار با یک آیت‌الله!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/101525" target="_blank">📅 09:01 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101524">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z83MTd3lMg0nPQmpyyDXoXQqd-yBMJxLkyb_htHHEq-kRgtj2UWe9HLgE5AK65hRznzBZBjWY2KJzA0GoPhF_cxQjv4hDMT7jNjht-Yg2_Q_9XXT1ufPPamwnRR7l0Ls-6OXvFAlaJgX4c6WpBhurqtrHtsiZyeQ46rBKZo3IX0xp4oJk0smJbi_siEN5HsDwqHF9XBRvMxKIYGR9dOUDakSBF9dvildmzuAc7jb0e7TVlzC10JSvu4BOJ9NN0FHbgs-f-yhvRInzs4jTrGom6gSgG7TopzWlGirjOzAGUXuTsrwO81fHBdZuQ4POuDYovLLU7OnRsncN3L097px8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر شاهکاری یه کپی بی ارزش هم داره.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/101524" target="_blank">📅 08:51 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101523">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C-TbWtuhdECjf8xoGY373FgrLbBw8c0Wp2yIEkowRK_BSDT1-693VtH9aMwvLIwiQcJmCAZfjKDjKTkjZlE1Mtt8b3yXl5nhWWChNlKObjMml-TVY9lxdNu85SE_ObIeHBaopWz1igy3oDGXNeTcEWIruvpwYiVcEsyOxORk5Gif5HgtAF7iG2sQ0jrjaUC6jYjSQAtBI1LgJs6kwcyAIMgaVnRoLh6VxJj0BrZSzvQFqSFt4oestdVBc2xALt-eJzOv9BXR7Bj2KVuVJbX20CKp1Y-gBJX0U9Ro3bGIoEsLl4aTND9srOG4sxDoC84UoP4SR6bJh4d_zTnZijjWvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇲🇽
👏
دیگه قرار نیست بعد دیدنش بفهمیم که 4 سال از زندگی گذشته و اوچوای دوست داشتنی بالاخره از فوتبال خداحافظی کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/Futball180TV/101523" target="_blank">📅 08:40 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101522">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i4LBxa5GbIjD_NEi7tcIQC12zK_9mXfCSsUxr8bQq1HI8TZuet1iBQJiS1RVa4JhsLAXrrlH0ecq_GzL4gpllCTc8qNkiMmBFLbBXoXU-6SrBJnc7DQIPLB18eC-y0AkuuC0CY30d7gIJYD4KN1eScOOWakamVo7-_jsSUEr9zIh5mDRxxU79OMU_EMKGWuT01D_omzMnoyobIOyygTvvZqLkjE8ezq-41wfnylrzI8VHDH0nqA22Siwj18BzHr0Zx44gbYaBKRA5VxAN89VhrZIGRN3nktEQwvaI5Eq5IzWvTCiauHoyVe7o4mPh8GGSYf9eMaAHlqCUGUmMl6LoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">-EURO 2024
-2025 Champions League
-2026 Champions League
-2026 World Cup
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/Futball180TV/101522" target="_blank">📅 08:21 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101521">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🚨
🚨
⚽️
ماريو كورتگانا:
🤩
🤩
- رئال مادرید در صورت ارائه پیشنهادی مناسب آماده فروش کاماوینگا و رائول آسنسیو است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/Futball180TV/101521" target="_blank">📅 02:06 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101520">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UV_qf6MrJ_JNyhiAwiH1LI8KW-stERCEiBEbx7QXujzhk4iK7ojNuwiiVQ9R2gcJLMNXGsNl_gwVUUd8WDB0OlFQD1jJs-rETx5kDunTMd9MHIR3Pera_aQ4cdANfpoRd2SWGo78QBiHTj116PYRG8u5TJ-giSXyfiBss86l6ozFlx7S3EKA4cWYSnbMufnOtE7LYiusREO2upFs00HS0VHb5FhjBoZ2QLQ1oJiS-fopJ_Mlv7u05yK_smK0187hJ2wz2HA0Q9MF4wJd3bV0PBh7ySljaONQ1rQa81rTuwX4-88iy8DWt-e8rjFl8btZEOsELw1Tn3cysX2XmjDAgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇺🇳
دونالد ترامپ در یک جمع خصوصی به اینفانتینو پیشنهاد داده که در صورت عدم انتخاب مجدد به عنوان رئیس فیفا، نامزد پست دبیرکلی سازمان‌ملل شود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/Futball180TV/101520" target="_blank">📅 01:45 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101519">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XLw1P4Porlqz6hC8A_NtuUUcHCwAD0vle38E-1WNqtBj-w70HjAkKt38J4Af-1dqzL3RUi0cclCVlvlxcCbfFgYc-sSjdbqZj6wMuSEwObNPtNdPCWkUS_RJTSmDmT4h1hkImKttbZjpvsngYo8l4S1mz7pWLpc20ltqkEUNvuydIbLH0cUhNCQudZUTua7qKxZOI9ijvAsqQgMrHu_bxECc2AsmmKfW0ShU7bEoFz-a55mnizX3nULaOkgSYMtfJOfk-l5LVdT1ZNEHIU-QKiGPezGFXShobp6FI4FxEyfgbUBj5JAXw0LFKzf5PG4Tl4-gT_sqQyPNssory3ipGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیشترین جذب فالور از جام جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/Futball180TV/101519" target="_blank">📅 01:34 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101518">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L5Ixe9xgE_pUUVbxYQTC0a83nA_Ae-HDf2ZMgbO-hRh2PUqJBODqohpiZsx1fDd-qiK2Dp56hiRkDqz_oD4bIzY_MewQ64LuSNcT6NaCdTWvmnWPBZ7-haYPmztET9kr_GzBn8cpXExyNupP1zpCmBxNfrLvZM0_2fCFvhsFZDItQbV9J9-nDFDOnJLfHeZPbPpdMtrlIypQOhNHFcDknSXBO_R-gMMSqTImsgT65dfjTg-5KtmCfuw7h-ITM6hKV9U6IbV9khIlG6kCKHwh4W96t419-k7blIKNV5xZ54giamoRlLF9ZevmqhDdLSgr3OYjgOnrTlP6YTTN38nIsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
فورییییییی از متئو مورتو:
– فلورنتینو پِرز اکنون بیشتر از قبل، تمایل به تکمیل انتقال رودری دارد. توافق بر سر شرایط شخصی، به زودی حاصل خواهد شد.
💣
💣
💣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/Futball180TV/101518" target="_blank">📅 01:29 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101517">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
💥
ارائه مهیج‌ ترین اسلات‌ های جهان
💲
شروعی هیجان‌انگیز با 100% هدیه خوش‌ آمدگویی ورزشی و کازینو تا سقف 100 میلیون ریال
🎰
لذت بازی در کازینو و کازینو زنده با 30% کش بک بدون محدودیت سقف
💰
محاسبه نرخ دلار با قیمت 2.200.000 ریال
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
••••••••••••••••••••••••••••••••••
💠
لینک اخبار و هدایای سایت
👇
👇
🔸
https://t.me/+ioIBrQfqMLtmMmEy</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/Futball180TV/101517" target="_blank">📅 01:29 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101516">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FKQK1sJ6ddX3CqjbKtXe1W7gb5_bIi8ODRmSjDuiNYZF6hjFLj7iT0SToYzv8Yhl03zu-G2JnFvO_FqvtApNLnc7u6yWErRwOUxJERwfJKTTB2IhOpBeXAcashYeOkvl9jzsIq5VZPYGp7CfItPH3_ignKF7jwV2XDvcm3UKQ3d_jwfN7aPiyvnR17cTl-47vlVoariZIDCDOOQtMV67u7gDxGAAFPogzg0Bv-37eFRCN01NAfXpdwxCzhdoEeEGt92hPAXLBEtkg7KxsHj3MVzlVpEmP9EwS_N32jbd_r6AjSvXgcUyXO7osLmanHsoOnaDqc2g2B0nlFp_PEAAFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💎
سایت پیشبینی
YekBet
💎
🍾
شب‌های بی‌پایان در یک بت!
🎁
35%
بانس جبران باخت ورزشی و کازینو، شبی پر از هیجان و فرصت‌های جدید
⏰
مختص واریزی‌های ساعت 00 تا 8
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
📲
@yekbet</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/Futball180TV/101516" target="_blank">📅 01:29 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101515">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DSTetecpYqrIGSV7dz8uy10hFkEtCCUTX7S0tYK_03eCj2GupMSeWDzEk7O0t3rRwAmGwjixEWoS23qj6wJOUZZfa_7Qz4__4LDUTwBiK4eOOW-y2zpHbmxwyHn201L8Rq9GVqscAE7Egmi2a6fQ4dOCVKPVLoC_sa7QjNpx311pseWrfAsBxxEmdRoNnJU-wNoA1KcwqGXMz7eqbCga9A2NgKkWDViLJ8Vp9SjCh3PK_Pjg-lTUikKBy3SBxvgz1DEgA3SStltqUe58XOPHLKUDVQ7ObuJEZUkXcQcg80dinqpZLw_2wwkyaq5jmuO9gSPz-gmPKMNSQleDUSb2pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🎙
جدیدترین مصاحبه رودری و باز هم خایمالیش برای رئال مادرید:
🔹
رئال مادرید بزرگ‌ترین باشگاه دنیاست و واقعاً دلم می‌خواد برای این تیم بازی کنم. من و خانواده‌ام دوست داریم به اسپانیا برگردیم. اگر لازم باشه بدون لحظه‌ای تردید قراردادم رو با رئال امضا می‌کنم.
🔹
مدیر برنامه‌هام با رئال مادرید در ارتباطه اما بهش گفتم تا وقتی مسابقات تموم نشده، حواسم رو پرت نکنه. حالا می‌رم تعطیلات رو کنار خانواده‌ام بگذرونم و امیدوارم مدیر برنامه‌هام به‌زودی با یه خبر خوب باهام تماس بگیره.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/Futball180TV/101515" target="_blank">📅 01:20 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101514">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e61b7dff82.mp4?token=km7l1L6_cJJjO3yrTc9Go51BrDUds-mCqi4-GDwGeMkv_Kc9RxgdaMg-y9SusO2-f0eCHrEE4d5aKp0EDjTBnokETEYyF3kcvxKHnwpGVaL4cw41J948a9ApHo-SkL4fgF9mRrJuC6t1NErLRZOFSLp4yIeI0yli4k7_SEtnTKZZs1YNYxr5tKiBI8hlN5bAaVyNovTSYDJzZ2SsSnvkyzHfvLooghZVdvQnfe9Vmmj137AFPLUt-PIuAFYBzrQ3JtzpsCYnyUPYEB1GzBkdXxpphBVowXQs3Q5xToUo3ZKX6kjY97EMTlH3-rfhtkovJXaoAe7aBdIKBeBTjGFgPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e61b7dff82.mp4?token=km7l1L6_cJJjO3yrTc9Go51BrDUds-mCqi4-GDwGeMkv_Kc9RxgdaMg-y9SusO2-f0eCHrEE4d5aKp0EDjTBnokETEYyF3kcvxKHnwpGVaL4cw41J948a9ApHo-SkL4fgF9mRrJuC6t1NErLRZOFSLp4yIeI0yli4k7_SEtnTKZZs1YNYxr5tKiBI8hlN5bAaVyNovTSYDJzZ2SsSnvkyzHfvLooghZVdvQnfe9Vmmj137AFPLUt-PIuAFYBzrQ3JtzpsCYnyUPYEB1GzBkdXxpphBVowXQs3Q5xToUo3ZKX6kjY97EMTlH3-rfhtkovJXaoAe7aBdIKBeBTjGFgPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گاوی و فابیان رویز که اهل شهر لوس پالاسیوس استان سویا هستن بعد از قهرمانی با تیم ملی اسپانیا در جام جهانی، وقتی به شهر محل تولدشون رفتن، بردنشون روی ترازو و اندازه وزن بدنشون بهشون گوجه دادن
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/Futball180TV/101514" target="_blank">📅 01:18 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101513">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dV6tFHLwx_u0ftbey6RzivqqsxQDobhI222IS0l_S-1fyAsJUpyP6GxkcGmufjI11IBi03Mcf0HeVFRjBtBHsoGUwL1B9xTDc38sks8ZW0baA11t7-MiJs0-IsqXGRSEg7eOIqqlpQuvhg6mSBaXpBN5XNFFmDwVRQuLUt9Ov19n6y6OdoS8esH_wc9p_n2P_vBFUkg523-pDTdgc9v75KCUAQbzie_kidPoVXDIl8yKm5gAsdrRUCFEgU_bGsMJ1OPVVtMIMZ3i1tegZACeuu75KBNh5eWgvd7IFeudK41bgByqKliJ3wn7pecAZCM4vLdoRuFxpHKCPVVKmXNz6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
۵۰ بازیکن برتر جام‌جهانی از نگاه the Athletic
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/Futball180TV/101513" target="_blank">📅 01:00 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101512">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RrlTQ2ezeB5y24-lnKpATsizEczdhjCp1m97XjO6TsMJz_n2x1DjpFgnXCcT_TV6Lqrh0gcj38GeflBof8zT3HPP4lhXPIAF-N5bomoVlezfzwwO9CrQZG6dngNXvYXzLGvNnMYM4j-ABNbLQyy3LQPI-lAnW3-nlsqxC9OcpluN_OUiaAg5JDAGes1aNJH_vff202OTpCU0-S5_CNAGOJHRUGqkTh_LlEUcCGzuhhHitxoXUp6lTky8noDjj6pZZa5L7h7p5A_aJ9b3BxIshXLRUkjLYG6FPlvokm4vPKeZAiyupXspCMm3Q8gJZNxgwtrMXNxsl4qY4o7y9POk2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#فوری
از رامون‌آلوارز: دیدگاه رئال‌مادرید نسبت به جذب رودری عوض شده و احتمال عقد قرارداد با ستاره تیم‌ملی اسپانیا افزایش یافته
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/Futball180TV/101512" target="_blank">📅 00:35 · 31 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
