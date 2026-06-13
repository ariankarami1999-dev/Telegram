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
<img src="https://cdn5.telesco.pe/file/Cma3ZbAAk513kQ8tQvaGzZrD5R_o1snNfZmEamQr3sXUGZ2vLuDMoE8xUp7II6gDfjdlvOp5k5nJkKImFx_vOR8OcEsxKYL1Pe4x123V3KKawuueCwfwLBJ3yicHXLqQLpn7Yv5mZvxL4coOTxBnzX1SBzNVMmKujf7Wcoud4Iqwbbo_Dh0p7CaJUnrMhBMrAuL1_4aAKUVvTExF_YEgjhcbN_n_GAj73bM751lMxTifE6mf0lITj9BjM2gjzpQ8aURY3SS-WY46UNRACeM8OqK9Fgoeqr1HgpI1XPBFji3mZnn1EzcPM0qIhMw6MjXpqDR3SCndDVbsFHSWhOZ2Aw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 468K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-23 03:43:59</div>
<hr>

<div class="tg-post" id="msg-92476">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b291ed502d.mp4?token=aRa91YivnjVMoj52l9cff8BipepbxTDbt-YJEc56cTE11XSJf9KpkBV1cAgh0DzyvpsndAGA1Y33JjYxEKVVff04MhMbd_kgP_Nkd5PSOAE_bPUkPXLZ3yv_XBuO8ewuzQzjTtCWRt5E_gOJ8aDAPgTSFz_d6JrSvLZwTvaFrTmk8JYHw3WcOzl69fHLYKGYC7hQ4UztwQGzzWudaVJAaKo9Ku5KW7fO_KPknbtQn0GKDAxIAQQxU1Or5RR0Qzl67CjlPrhW8tT_dm2G_LdAqVjZvFpbA0mC5kEPj3lGEpw9LdGRKpg20B9jvanWd5MqmkozaRrsMBapwFWA7m0Zxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b291ed502d.mp4?token=aRa91YivnjVMoj52l9cff8BipepbxTDbt-YJEc56cTE11XSJf9KpkBV1cAgh0DzyvpsndAGA1Y33JjYxEKVVff04MhMbd_kgP_Nkd5PSOAE_bPUkPXLZ3yv_XBuO8ewuzQzjTtCWRt5E_gOJ8aDAPgTSFz_d6JrSvLZwTvaFrTmk8JYHw3WcOzl69fHLYKGYC7hQ4UztwQGzzWudaVJAaKo9Ku5KW7fO_KPknbtQn0GKDAxIAQQxU1Or5RR0Qzl67CjlPrhW8tT_dm2G_LdAqVjZvFpbA0mC5kEPj3lGEpw9LdGRKpg20B9jvanWd5MqmkozaRrsMBapwFWA7m0Zxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🏆
اجرای دو نفره بانو لیسا با آنیتا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.22K · <a href="https://t.me/Futball180TV/92476" target="_blank">📅 03:40 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92473">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QeUqCd7QgnNNqyaTCd8zblq9GnIKZ6PhyrUTG1Cq6A0rajTZj7Y_j5BG_488mH2BNlbcEgNiqLh9cEkWgQI1_7pyPR7Anej6wMvRDoDSNCdxrcajtiLXwJxYFU74NxssSLAi3dYTZv7RyPmYQy0bQh-2Bjrdzfjb3aZ2xl__s-F2k_sXT_FkyHvem_tWy8mjZV7zoFbi1zkCLZtpU0rwGQup0B8B2q2Qt9fUpyYRhawDDu6vPfBtJtHTu1KvKyVnMrJQaaTH0I9TIfAEPAWDSds62ErmGk9e0_y5QS7SA7ROkQEhKTMPKOwkcQh_ZJWQR4pHbZRudV9MBGBD3QExhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SG35i8W8xroG71TNLiLEFH0OQ4mqhdAVf_XRE4eT_m3jifdF-4qlY7ycFBB8XrWphl604e1VawrNsUWMTW-WIa8u8N-Tz8s3kfJFQs6tFG6A5PyUSOsZldgAFnV98IwbLnOq1cXVauUXmAGCnboBwlLR99unT_ODU04neyRUH7dFY-FbgCRfFPE3JwgpSXU77qXVABpiTXK1UWpX8oYiLKRm990B6Lz5cq9XLb8goIsG8sHY5gskRrcaJFOyoP0tpARp8LdaTea3b-jQCOFjbtIlxrRIdK3Xg7QiwhfNuEz3gs7dK9f21jyjdoqWRxev9aSUJbkaVpz_zrTFTIYjTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QU0wCaYBC_GeF5_gWadgEkVwFQybvtk6WJdY9gj4eRc-nbVQeJvFwp7Stmbba1v6b7xF17QlUhy9I5H279rMx4-BGriTiOtfLVyhbO9VwEYJVAFNWdmERFXIDadJgj6TRU2y2S4AuEWnbb6OWCl9k-86RwwHT89XKYcFbzr-7r_eWy0GpIOKHnHfGir6R-Yr_yJwsHz6hiF_7Jc9G2E7oyNaR9qZDnk6OC2voNN0PNvMHbCXoyBvW-sKDBz_URtHFPa_ej_bslJU7lIU1qflzGWbwRFn9GUF2ihc_C8yRqh_n8StJKbhHkvrYz9Q5_Ht0r5VEN1EA7ql8USe5ey8gA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🏆
تصاويري ‌زیبا از مراسم افتتاحیه جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.53K · <a href="https://t.me/Futball180TV/92473" target="_blank">📅 03:38 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92472">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">لیگ ملت‌های والیبال/ پایان ست اول به سود ایران  ایران ۱ - ۰ آرژانتین
🇮🇷
۲۵
🇦🇷
۲۳
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.76K · <a href="https://t.me/Futball180TV/92472" target="_blank">📅 03:32 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92471">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚨
🔥
🏆
🇺🇸
اجرای کامل بانو لیسا برای افتتاحیه جام‌ جهانی 2026 آمریکا.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.05K · <a href="https://t.me/Futball180TV/92471" target="_blank">📅 03:30 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92470">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">بخشی از اجرای بانو لیزا تو مراسم افتتاحیه امشب
😍
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.06K · <a href="https://t.me/Futball180TV/92470" target="_blank">📅 03:28 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92469">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0252ecab75.mp4?token=BOk9rw1OhP5N3pdPz_hSfOig8hDmMjYz5GtQww-fU7ILk8ibdOzqc40Sqpu7Pp7fxH3NWnMXw7O9OxbR9mdANJtv1SW15XJybf13AyLEI5B-9QSLTMZZSAW2p1UbmYIGjMQKu_1J3rpIKP6_7V4M0w-dBAhvghdERCzS8aEA0n65JHrZw0u78XdhsIuHp36pXlhOWxgIsoxeXopMIwqRGh1V3Lr0pxK_ihKBCKVpZXXC1u1fqitYADLLJQfqojSzUHEmXhiw6bTtlwfn_C7sC_hYTpcBnjWlWMKkP2TCJoLMBf7RLnjh6ImepaqR_b6_Zqrw8uhBpftFS5zmuG-QoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0252ecab75.mp4?token=BOk9rw1OhP5N3pdPz_hSfOig8hDmMjYz5GtQww-fU7ILk8ibdOzqc40Sqpu7Pp7fxH3NWnMXw7O9OxbR9mdANJtv1SW15XJybf13AyLEI5B-9QSLTMZZSAW2p1UbmYIGjMQKu_1J3rpIKP6_7V4M0w-dBAhvghdERCzS8aEA0n65JHrZw0u78XdhsIuHp36pXlhOWxgIsoxeXopMIwqRGh1V3Lr0pxK_ihKBCKVpZXXC1u1fqitYADLLJQfqojSzUHEmXhiw6bTtlwfn_C7sC_hYTpcBnjWlWMKkP2TCJoLMBf7RLnjh6ImepaqR_b6_Zqrw8uhBpftFS5zmuG-QoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بخشی از اجرای بانو لیزا تو مراسم افتتاحیه امشب
😍
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.67K · <a href="https://t.me/Futball180TV/92469" target="_blank">📅 03:24 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92468">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gNbET_IcJvxi_Y-AzAKoeBuBAqZ9X3_F0XJWK3RuX4nw8JDh8hh9DBjyYzkKjAW1dapPCyv7ec1J0u3LDF-N-sia1FxqFvkc3Hkjqx4E7_E2FTJv2t-Bgb0AS3fTIJlGhTaDA-qC3cvcCbG1btAmu0yVMPqF7VvOxYIRdso5BeiQWegGyUfYsd0oN15i5wHTJY8VTSKpW5l2EBNjG95bWj1CDWXkVQfg0n5WnxJiUZRpI44qJm43T6ebxCLw4Sf-betJIU5PFrAtFJTE6C6VfqWY1D7rg1zfdFCnEPnI36I69LwXV_wHR7eSkAOy94SD-_Fbl0v6CQRVDV3LQHTPgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🏆
سایت پخش بدون سانسور مراسم افتتحایه جام جهانی در آمریکا ( بدون فیلترشکن باز کنید)  لینک سایت: https://live12.arvanlive.ir/hls/sport/sport.m3u8
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.37K · <a href="https://t.me/Futball180TV/92468" target="_blank">📅 03:24 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92467">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚨
🚨
🏆
سایت پخش بدون سانسور مراسم افتتحایه جام جهانی در آمریکا ( بدون فیلترشکن باز کنید)
لینک سایت:
https://live12.arvanlive.ir/hls/sport/sport.m3u8
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.67K · <a href="https://t.me/Futball180TV/92467" target="_blank">📅 03:21 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92466">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WY_NRgkVhnOW95_6jAKN9aAuQH3_TyjiO2OWNUiF_VaYUMg499s4tH4o5dhgqvs-1MAhByo6cQbrSY5jS1riywo_cjDQiFZNtL7OgvzzRrRzFGrcvLX_QErC39j861iJj0WSdHF26DCPXq1x4j43bCwViWwqG6-0Jq9rZcrCv3y3YPbhRM80psrDrRsNNZGP5rupnlrFhcj-JPl1-GEKFJ_5Gu6cz_rwEtXvXRh6AzKRn6jmPE5VPShzUODLb_eNATKjKoohbMxAw9NgRtQUiZ92qaFggfuFF2ss8ykijNbqbj_w7HvukXGGpniSeN69a2Z9s5qz9G1cpEKTR-uTGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
🔥
بانو لیزا درحال اجرا در مراسم امشب
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.67K · <a href="https://t.me/Futball180TV/92466" target="_blank">📅 03:21 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92465">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CLHG4UnDCDyi5onoIdlR_8rzAhs9nRDkvgfOT7EOS7Y7doTFbL75ZvJQAFEdBnGyfEh3qZBjTA-LdaE15H-gw-vPypNpMRvqoiG-xfD24XTfCVVJrKjT2qeiEWA73zE0Tcvggn31CElzFzTVcYXs-6wvejj4VoE8DyLCvgnwrKcBiuztQZ4TN6dRhZ9bbNJ-JPJp8HIi_oLt0ce6i5NBUWcaS6bXpGhVutRnGOQky5l7O6s2sJHzBopwb10t7qnssS4zNfmeJTF_lvVmynXLdIOhPgArd0pzn-HsN8sp0KhxwPP04f_Nn_L1zTp0Cz-glkvIOjETawTPbzhuLFmdZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
🇺🇸
ترکیب آمریکا مقابل پاراگوئه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.98K · <a href="https://t.me/Futball180TV/92465" target="_blank">📅 03:16 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92464">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a643a87a13.mp4?token=Lm85vI7LbGDUwxLnIE_3-a7tWbqlnf1TRihVYGUIO8qmbl5tzhXQ27dEIl0A7p1PIn1IJz9o6TA0VYg6skmskaN8ZRbZEryjGmS49CRovixpwIp6AxvZ4kb_lndaXjsbXoj1Ui9CEJWGN8lvJfNIXkfNN0ZhVoOD5lblazPK27Tv-KeloKAJJKyd0QvhbGoIECA0UKZjAMkkokBRgZHUBVh_ABPTjSWUzo8aHjekX6tvsfufCx-ld0LVMiOep3yA9a99zqITZRO2Cs99Yha4Pdp4iFsaLEXXy6WpuM_oKLPkLICp0Fj0ESfSMPkz8n9f8_HDB8zXT9tjkOjkZ6qUA26Mj9B-_cPeNAEGhAycOegCzA7VOUc5rw7IkkSzbZZi_JDAmdHl7oHA2sPQH-O2-gifzqtdUftdWkjzL98KFAMroXJ_Q8xau34CBPbuPs0IICUywx-FbYqr1AW6B5b8YcZH6XIUocXjm5wTPbjP-liqHxGP-U6Xf2wAuQSbh-RXng3lRQ0rVVL1Hh58cDqSqXr46GwcTTzF7Rbnbb0RIWJBFLPsnkbzS3KosmBiNckPntRzygqPteuvZqf2Bmwo90xJnC298Jw9h7qqtm7Sm-EvlnQlPD5SCQe5CynyKM8gbwqAzYx5coIgP7gznISSo-4d4QaU-9ZTZGjxhGNucJE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a643a87a13.mp4?token=Lm85vI7LbGDUwxLnIE_3-a7tWbqlnf1TRihVYGUIO8qmbl5tzhXQ27dEIl0A7p1PIn1IJz9o6TA0VYg6skmskaN8ZRbZEryjGmS49CRovixpwIp6AxvZ4kb_lndaXjsbXoj1Ui9CEJWGN8lvJfNIXkfNN0ZhVoOD5lblazPK27Tv-KeloKAJJKyd0QvhbGoIECA0UKZjAMkkokBRgZHUBVh_ABPTjSWUzo8aHjekX6tvsfufCx-ld0LVMiOep3yA9a99zqITZRO2Cs99Yha4Pdp4iFsaLEXXy6WpuM_oKLPkLICp0Fj0ESfSMPkz8n9f8_HDB8zXT9tjkOjkZ6qUA26Mj9B-_cPeNAEGhAycOegCzA7VOUc5rw7IkkSzbZZi_JDAmdHl7oHA2sPQH-O2-gifzqtdUftdWkjzL98KFAMroXJ_Q8xau34CBPbuPs0IICUywx-FbYqr1AW6B5b8YcZH6XIUocXjm5wTPbjP-liqHxGP-U6Xf2wAuQSbh-RXng3lRQ0rVVL1Hh58cDqSqXr46GwcTTzF7Rbnbb0RIWJBFLPsnkbzS3KosmBiNckPntRzygqPteuvZqf2Bmwo90xJnC298Jw9h7qqtm7Sm-EvlnQlPD5SCQe5CynyKM8gbwqAzYx5coIgP7gznISSo-4d4QaU-9ZTZGjxhGNucJE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
جو هالیوودی اطراف استادیوم محل‌برگزاری
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.98K · <a href="https://t.me/Futball180TV/92464" target="_blank">📅 03:14 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92463">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IfDQU5MKKVbgfQU7GZml0tIQeJ4u_672q93aXgSqvNzJV8ZDI_eQTMOvtsAOvJ3sZUGQFSyOw-fr14JpQhX_jqOqBLbdbxGCk9rizgTqSxfn5BDhHVPgdWawXrsuDCNCg_SVCmHk9d8diIovd0KcufFs2BADkMkSAGEgs7jXJmh_y0DoJsxjv0HGV52CH81QW-Msxq7wJZZT6bp5ZH51LXvHXnfhPdjgm1npqs3_MgPkJzVfQo2yuqsPqorQPnCdDmCbxs6aDoPAdsv7HZR8uhpXM4-SsFLnTDsPD0i1Oh_RghMnmQQra_TtB9eBP4LOrE5ctvjrKx3lJyVYJwfC5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
🇺🇸
ترکیب آمریکا مقابل پاراگوئه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.97K · <a href="https://t.me/Futball180TV/92463" target="_blank">📅 03:13 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92462">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd835b923e.mp4?token=U70XpIWVhlTFj7ohtuL0zsumfgEOmGiEwl4iT2J7XZHThl0kt-XYo9HWrXyS_PwJv_Lfbqc9m0rnYO66hK5yPCw3uptdgitwtRWcjeuAQXgQMkmVP8af51HoPaP4eAp8tG0_N5iRwOhB81usvl0z4oEryHxq06z-s9wagQeUs2zmB4eM71FAVfuAs4rzEoAiXxcsrqLE9SDY-1dctQHFuG5_Crbz2zMJRXy3yT7kTGfmCN8wodPt59tkbU640MGLl1Ns-wEy9PrIpEgzMZOz_GjZiId-YftOMHlJoyGe4lTezcoM2h1HTqLm_RBBjZl657M6YtlMn98wfYjAj-cQebWFvX3kWyi7SP2hcNc7rAyNg7UOTGd8LPjXgum5_xATwIFWVbPtyabCTeKcGxMdoJHH4P_uV43oJb74UdKS9zj8S2tn1F3ye2hG_s2VXBPNKYdejFLq4OdVQ-BKUCQYJ6Q3lLB-CxchfVnQGbsFnyvbss_ThxlKgc53P6zqE5abmxkvLE5PiAojvUOLKVbULalenwG2osOz8ptUxeysXT5X_oNhwfWr4GFB1qpv3deoK2RU7cGCX8Y8Cao6Dw85AkHBjkwKP81P3XgF9Wrk2J1KXefFHAJXZdQA7KJ2kb4WSjE6QTl41r1VVrIMXciNzl4SG65uKKukXR1B5hLlurM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd835b923e.mp4?token=U70XpIWVhlTFj7ohtuL0zsumfgEOmGiEwl4iT2J7XZHThl0kt-XYo9HWrXyS_PwJv_Lfbqc9m0rnYO66hK5yPCw3uptdgitwtRWcjeuAQXgQMkmVP8af51HoPaP4eAp8tG0_N5iRwOhB81usvl0z4oEryHxq06z-s9wagQeUs2zmB4eM71FAVfuAs4rzEoAiXxcsrqLE9SDY-1dctQHFuG5_Crbz2zMJRXy3yT7kTGfmCN8wodPt59tkbU640MGLl1Ns-wEy9PrIpEgzMZOz_GjZiId-YftOMHlJoyGe4lTezcoM2h1HTqLm_RBBjZl657M6YtlMn98wfYjAj-cQebWFvX3kWyi7SP2hcNc7rAyNg7UOTGd8LPjXgum5_xATwIFWVbPtyabCTeKcGxMdoJHH4P_uV43oJb74UdKS9zj8S2tn1F3ye2hG_s2VXBPNKYdejFLq4OdVQ-BKUCQYJ6Q3lLB-CxchfVnQGbsFnyvbss_ThxlKgc53P6zqE5abmxkvLE5PiAojvUOLKVbULalenwG2osOz8ptUxeysXT5X_oNhwfWr4GFB1qpv3deoK2RU7cGCX8Y8Cao6Dw85AkHBjkwKP81P3XgF9Wrk2J1KXefFHAJXZdQA7KJ2kb4WSjE6QTl41r1VVrIMXciNzl4SG65uKKukXR1B5hLlurM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🏆
هم‌اکنون از اطراف استادیوم دیدار امشب
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.27K · <a href="https://t.me/Futball180TV/92462" target="_blank">📅 03:11 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92461">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lEeDb3CJQqFJt2RtxyRQCRkLhw4gQ2kQMc-qDb4yB5wk6nre76bwuli2L-1bCu5PpbV5aB0bNZnOJzNE6b2iodUHlU_9YJvhsL6ZL8ilElR8oqVbQ2HtoYr509msmpZyEHZma8va8N8R4hm9mtKh7VaOaSlWCqPRBzBzyl8bHRPSad9su-Z8Fp6cjF_pak-wWokFzSEv7ZHoRHVQZgVSbQKE14EHfxjJUDfeFPVAgSBp3ZW8T4seN-_xDjBwZnt9_XQzHeDYgidI-PowJAx3Jn8bnS2ouumChnWINICTFFaWyvLBPAjjX9Mw2_fnJdJg08Isrd4Re5xDTN8M0gedrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
هم‌اکنون استادیوم محل دیدار آمریکا و پاراگوئه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/Futball180TV/92461" target="_blank">📅 03:09 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92459">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">لیگ ملت‌های والیبال/ پایان ست اول به سود ایران
ایران ۱ - ۰ آرژانتین
🇮🇷
۲۵
🇦🇷
۲۳
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/Futball180TV/92459" target="_blank">📅 03:02 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92458">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RmN-ELYKWuxaaooqYwugfk-aFE9pRhdz2hTmkTIZQaBgkWTcD0HQ67C8Uge55n09oia_fVwqhDNK1HKOxWonuLciJjPTMmgQt44Ywck-5FnrTdg3kg_sck2yq1DsNPACE5S9EjT00gK-rAB4amOTXGyOSjk2UUe-aNLyDRUiJk5XMKMjj6ufsD0RYvkFn1_imVYnRSKC7v8PvWDPnakR7mQT22pCSG7VzLLGOAL6lFLdgu7wDRELTOC4towhGg4Dos4aTb68D_IgE2svChv1Of0NtC9zxxfZ95EIex-XbsXsdplbRUmszIJyA9hkWZrx-3UMX1QeyS7vaWiZ1SES_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇧🇷
ترکیب احتمالی برزیل مقابل مراکش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.41K · <a href="https://t.me/Futball180TV/92458" target="_blank">📅 02:58 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92457">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J0PVIz8ONTyiGUfkhbCUkqZmrA7qb1CzRtKzfPgayoOWYmrf-WbWUshvo_D66-kZxIoAxR4XzvQKiSbvxhsGtFJcCbafgJy3KRCE8N4xZDRN0-IxwD_-ovBgMyplufM8cCp5E9LCWrhBKY8Fjwb43ZRzbdwvEi7hlOr6Y3p5G_a5TbabIdbn6XxQ1xnX6u5XNbSlBShn7QPCDtYSZI4OP4Roccsx0IcP8x4M6oXz9WvmfumeTgWUN6BCXZ_RLsI0-fJf0bvS8sfQKUeXk3Jy0RIikhPaGoWt7qzw2ZKmIWdhaGX1xPjeiOJ0O2sBDDCNE69pV_77j6lSXJaID4bKPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤣
🤣
رسانه‌های خارجی از قلعه‌نویی چی ساختن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.34K · <a href="https://t.me/Futball180TV/92457" target="_blank">📅 02:50 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92456">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bea6577b63.mp4?token=f_D4BnhT8mI6eRShz8tZ3FJTAeJBu9xOdRQZUPTfgqlCGljUVS6FoAbZnvy4kHEH8-Q0IsDJ3g0I8nWDiYa4nrKV7SjUv9iDfYVC1yIgK_fS--hUb_4rwrom-9qarwAKvX59NP1e_5vuRzepnTgeoUI6pSXDOT8cc9Ak2ePqZb2KmQllZKQOucRzPKzz_7QVwVxwkz6kFCpAmXyA4kOAth9Ijtu6kVxMSRLnL7Aww_h7qDMawc1gAUl7BOzOG7WJZd70vXPcLFFcxUNtFo27VZ_9J6ku-KtrA3sSPZ_I-udVA4vMTFy1gB-WEJUr4e7BUHJSkC2OJVSHUEou0CI8xDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bea6577b63.mp4?token=f_D4BnhT8mI6eRShz8tZ3FJTAeJBu9xOdRQZUPTfgqlCGljUVS6FoAbZnvy4kHEH8-Q0IsDJ3g0I8nWDiYa4nrKV7SjUv9iDfYVC1yIgK_fS--hUb_4rwrom-9qarwAKvX59NP1e_5vuRzepnTgeoUI6pSXDOT8cc9Ak2ePqZb2KmQllZKQOucRzPKzz_7QVwVxwkz6kFCpAmXyA4kOAth9Ijtu6kVxMSRLnL7Aww_h7qDMawc1gAUl7BOzOG7WJZd70vXPcLFFcxUNtFo27VZ_9J6ku-KtrA3sSPZ_I-udVA4vMTFy1gB-WEJUr4e7BUHJSkC2OJVSHUEou0CI8xDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🏆
#فووووووری
؛ خبرگزاری‌های مکزیک: امروز نزدیک محل کمپ تیم‌ فوتبال جمهوری اسلامی یه جسد پیدا شده و پلیس درحال تحقیق درباره دلایل این قتل هست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/Futball180TV/92456" target="_blank">📅 02:32 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92455">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
🚨
🚨
#فوریییی از رومانو:  نیمار بازی اول برزیل مقابل مراکش رو از دست داد
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/Futball180TV/92455" target="_blank">📅 02:26 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92454">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/khLCDxI_5tIeUiG_WXGmStLiPZUGh-ixzCojKZ8SXGKM7jIiakzyrwBAFskCpq6MSHx39EKTssZFL8FbRdqWRLgcmh5rd01_qDpcqGJlctObv24aOspoD6bi1TCxvUj5XSkyKwGSgAkmuKKKZVVoBNfXLh37FuImOjEGcrhEpqHJiDrcQk-Du8sX1LnDQC3zFhGv1ASRCEHhuZoI-igWHSzW_i5m2btOxmFN80t8ozigWvcPBpEZOffyWlz_gDuZb9A7sELYwcImlIypr0ZgNmgtUEMq1ndZe8lDVuV4EBL4_0LS1_od_eyHGe1rnZyFNtB1Eb_zJA2oKAGbhfXLcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
مادر دختر پاراگوئه‌ای آماده بازی افتتاحیه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/Futball180TV/92454" target="_blank">📅 02:26 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92453">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
از طرف اتحادیه پسرا به دختران مملکت:
دخترخانومای ناز و کیوت
🎀
ما نوکر شما هم هستیم ولی باتوجه به فرا رسیدن جام جهانی و لیگ ملت‌های والیبال، از شما عزیزان تقاضا میشه در راستای حفظ آرامش روانی، حفظ تمرکز این حقیر و جلوگیری از هرگونه دعوا و قطع‌رابطه نهایت همکاری رو به‌ عمل آورید و از انجام موارد زیر خودداری نمایید:
🙏🏻
🙏🏻
❗️
پرسیدن سوالِ «من یا فوتبال؟»
❗️
شروعِ غیبت با پیامِ «اون خرابه رو
یادته؟؟»
❗️
ارسال پیام «بهم زنگ بزن» از دقیقه 60 به بعد بازی
❗️
قهرهای ناگهانی همزمان با ضربات پنالتی
❗️
درخواست بیرون رفتن دقیقا ۲ دقیقه قبل از شروع بازی
❗️
بلاک کردن به‌دلیل« دیر سین زدن» در وسط بازی
❗️
ارسال هرگونه عکس« مدل‌مو،مدل ناخن» و انتظار ذوق در وسط بازی
بدیهی است پس از پایان تورنمنت، تمامی ما مجدداً به چرخه عاطفی عادی کشور و بوجی‌موجی کردن شما بازخواهیم گشت.
#کپی
شما هم میتونید به همسران و دوستانتون این متنو کپی کنید بفرستید یا فوروارد کنید من که کردم تموم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/Futball180TV/92453" target="_blank">📅 02:15 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92452">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SxPYP_4qGYvSfNMX_ovmwPTEzS_Gp5M3fB_20-625fv_kDh5Qaih_TfSqZVx3DVODxUucZPk4Ix8mOwiOH2PwR2R0NFKNmNTW6fW7exuWGz4YTKDnouZFdBCfGSWCu-X8iwYoiz98JAg8oZ_ybbRehXpihFC3lpZBALF0IaBqcyjOMjGiWSmCet-ipeh_tm4i-TsU92zNPe_TlXmQzrZvMKr2TSenBBp5g5MYbntzyaPE8f8qImuYE6z0c0s8njCUEak4cDQbV2w2BrS35gRetmkXiguF-qVPrCj__wao4EcgBRRJgbeEWCr83qFHTClanjyzEPtIweIiGd30jK6vQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😀
پست‌جدید نیمار درحال عشق‌بازی با زنش تو آمریکا با کپشن: خیلی دوست‌دارم بیب
😊
😍
همینکارو میکنه که نصف سال مصدومه
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/92452" target="_blank">📅 02:02 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92451">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uCe3tidXanle4QQT0aNYRoNBpP0oWQiEN_N9wnnLZoq3tKzKFrQLFTdJTM53t5QzXYUzI6TdMsgUsMZxwWNXmqCJmmlR74v9XPiGG2846FgA8F4WAUtXK7MHRvu6f1IpZOgxoRRYdV8go2XJzP3EXbCoemOb1JHU5pYtPNQgkhX2KeJH4Q8uaWhhgQtdflfQdteqmeqOC1w4lASZumkpUEsTvKZpbfYFlMNKrNDfCy857muNGnoYPYrsnYpkaGXvM5m-BczJSfYW4C8PQqcVq_y_-iF2EHxTM45lL-E6ACubAT9LPBs2GgWNtk__-G3LXD8p0w8yg93TCkF-Azw0JQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
#فوریییی
از رومانو:
نیمار بازی اول برزیل مقابل مراکش رو از دست داد
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/92451" target="_blank">📅 01:50 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92450">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FGS4nu1FhZoWKGrMZCKkvQbv416I8iUu750BVCI6E9GXiwaMY_Km9xrZKMKTIv4rmF5dqZJmIcF5BUh28NSE3vjp2ZdScSWqIiJ4GhURZBgNZuO5mw1PH1ekaBxKlDtUWPntbw3PiTWME44mBE11k0ccWtHfyD0ArgZLsC0T_sRQCNaktcTHhmM-epRD2panChsvIB_pxYbvDg8zDfU_DioQg4rM24BiGJD-_FAHsr-VTEjTbEIS-rsYCKUP-OWaGucaTJ6WGtN0bQULuShXrsDG2kBN9H2tRfZl6rzgf4Z4PONBrXsUqW6apdPVemB6G9iar6Wykfdnx1NJQUYGxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
زنده از ورزشگاه بازی آمریکا و پاراگوئه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/92450" target="_blank">📅 01:49 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92449">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uMIvXTm_CHCFUpEmA_PkB5Rzv3gU4o43X4wg9guKGLa9ScR4E5gBwsfIhGyOpElX_HGjEEB9sXAKekFtSV8lblzi9_1Se1jGfWQPwwDB5ib0kUggNLDUzgcadC6b8VY_mNPFQ85ZRAd1R21Xxft1s28ycQ6lcn8QCEDIDLvD1CC5sMcghZhafx_-HAPdYyJDijMczjNYoQ7FWp13LaQ8NlsLlEp6tg3QEDErJCx813wpiOv8nQQaOIzwSfX9WkvdD9aRnQIAcjF9FzWITnVDE3-r3uLuFIzGFdNLpI9KsIpLJ08tQdH6HIkbIyZ1377ZCGhPGXEANXMkGdj4RH260w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
ترکیب تیم‌ملی والیبال مقابل آرژانتین؛ ساعت ۲:۳۰
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/92449" target="_blank">📅 01:46 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92448">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iCLzQ08rv8UzaG_K6fmGIQ-Tz8D9KZCrjUXxGNgABQQmpTkBpYr_8Tb6qIA-wNnGXYa4czbUf9ucDoNtKtxfFGfh9uUfn_UNFelVewGn-qrJvV709IO_ZSTNYHAmXKAhpFTI91ypy5UZU_hkdtfqqUsxHJCDTqgxxxDuc3cr7XoSTRqG2srwqzWwA2fgVOSKCL0hAImeRV-KUJG9lpTs1iGA9dPNCxGd3ZI0S-A0y37wG5x__hXcc13l71_lZnB-w39eSn4Xn36cYyIesW4LkBoOnZTGqiehdTQKh5BPbkRsYYJdqjz5Zv_SMLJwZ4I10WtEd0Gakn883MyGfz3jhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇷🇺
🇷🇺
#فووووووری
؛ رسانه‌های روسیه گزارش دادند که پوتین به مسئولان فوتبالی کشورش دستور داده که تورنمت جدیدی با حضور برخی از تیم‌های حذف شده از جام‌جهانی و تیم‌هایی که شرایط سیاسی خوبی در جهان ندارن طراحی کنه تا به نوعی تحریم فیفا و اروپا علیه روسیه در بخش ورزش به نوعی خنثی بشه!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/92448" target="_blank">📅 01:40 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92447">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ujad1yP1ipKyaBNCnRxBERyY2BBq7Yvj7svrJqp0bLjkpTrwU8nSqlA8Lkv5CttCUwRMUiE38xUxyCYjPcryVwcwmLYZ06TudCyzTLr1_YKcRDCSnGRfQg_RyUVyUUO5WXHfxfQoEt-I7bZB6T54Te97WWiZApItpcmytcpCcHXWjgx03d-X2sM8S9TZlstrSPjJNMbyCJcvV24o-ZmhS0MYYcg_EU1Xu-aPXedx_cIabwX8GX4Y-ZKhSgEQsvOWNAdHglkd02i8wWe3Sk1A8bJ-eHUuWAbSHktHfC0Q92gBy3Rw92A-2XTgzLeAz0RbR21kSXeIc2qcVUjYTtNWsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
هواداران پاراگوئه در آستانه بازی با آمریکا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/92447" target="_blank">📅 01:35 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92446">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KXlIIL_lwygwPxEIuGv7vH7JTdHZoE1axz4teucVOUmN4d8SaGPWRwWIVkGxHe-htQilbdcpjOCviTN6J21lJtt_3toQamWiJSTk0J0O552vrbjHa8ocHBfQ7ZdTAAki_FjCfmKqu3OFXxiferX1nyUnYBPHOShFfDk080Nnc89zQULPbwarlbElrLilbzgBrdXGHKsN5iqmOonMYkEIEbrDyifYNUbpzTGIE5Uj_Iz3JijY29mCYQFp_1VK-MJt1nBrmetO5d0PjCvkzR-S9L8q4J3uAGhe7ISyRIzAhkuz4kPBNniJeLzLQdsh_JcMnd-c4hcOSk0NZ90SKyfagQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇫🇷
#فوووووری
؛ دیمارزیو خبرنگار ایتالیایی: پاری‌سن‌ژرمن قصد داره در صورت درخشش فران‌تورس در جام‌جهانی، برای جذبش اقدام کنه. ظاهرا انریکه از سبک بازی هموطنش شدیدا راضیه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/92446" target="_blank">📅 01:21 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92445">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/kD7teyNhJrvdcegBouUCQtl4gB8KZIDBjuselEJm1bljT1ZbowuawFcnXaAsOYWiJ2dJDCPF75yDJNQbuEkBv2Vcj4VV2Ir5oNZ-QurxGiy6wEAE_Y6kneC1FvcUr4m3I6lR7up6w5jx3ILSWHHvpW6zIExhNpBa4Zq6SNT9mkfLwSIat83WwR1hJ_l6c12HzDpJo4RZjmQtZPnyQYr9FdQUQEJPZjLJ_PJimGerwXy2FYaZdmnZgKWAaLSvvvrnh8XUpnpaVJBZd-jOUHNEkuBYJ0pYEuPZnDnziHeS_-efhr_YVMEhmct8nkO91MRcwv5S3F03ZjFaPLFQz5Angg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کونی خان بهترین بازیکن بازی افتتاحیه کانادا شد
این چه اسمیه تو داری مرد
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/92445" target="_blank">📅 01:19 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92444">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9dd472ef5.mp4?token=rfBX9_9Zbz1tCwaZeVqFGXmQXbMbzYu1kp38xM1lLPf7faikhBb1HFYsgCmIKWPm8v5gx3jRKsdCvJ9E6RfuBaF_z17dThnaSXy2ha9pBNsXtZJ7c0Rsxspq4wFtQ2oFpi3XyCn9vzYz8iCSYwE4hiwQbshswTlLxctX1mpp83OwzCOXPdo44DBPQl24e9voFGc0EXNlSLkb-NBFG1_-gSdpn2yBkpPwrG2F_NEzhB9xvEHs7ok5QAc85fbAZRntcuQlEdzeabgzEKfBeErcToA-XQ8KxPLb9sZCu-aMuTeg3dtZ19yvKDITKCSwvY6HIErOhNJIY2iAdxDL8IZ99Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9dd472ef5.mp4?token=rfBX9_9Zbz1tCwaZeVqFGXmQXbMbzYu1kp38xM1lLPf7faikhBb1HFYsgCmIKWPm8v5gx3jRKsdCvJ9E6RfuBaF_z17dThnaSXy2ha9pBNsXtZJ7c0Rsxspq4wFtQ2oFpi3XyCn9vzYz8iCSYwE4hiwQbshswTlLxctX1mpp83OwzCOXPdo44DBPQl24e9voFGc0EXNlSLkb-NBFG1_-gSdpn2yBkpPwrG2F_NEzhB9xvEHs7ok5QAc85fbAZRntcuQlEdzeabgzEKfBeErcToA-XQ8KxPLb9sZCu-aMuTeg3dtZ19yvKDITKCSwvY6HIErOhNJIY2iAdxDL8IZ99Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چرکی : شب اول تو امریکا یه دهه برام طول کشید تا صبح شه
ساعت 6، 6:20، 6:30، 6:40، 7، 8 و 9 از خواب بیدار شدم
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/Futball180TV/92444" target="_blank">📅 01:15 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92443">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9fa48a9b18.mp4?token=JxIx7RfFTBxPd7WShJyXSmMCugK_SlnM9dwa3_YhKSE0Rfvo3LbA7w8n-p4S-IMn1XuNh6X66NH8J-SCbvL8JPtL1TYTRbmZL8dwdjt2Nsa0mqkU19z_Y4SP0F_oXJosCtAzKWyjp_jGXOgU3uEptwS8Pbm2pIrOL9KAGFoKfzgtifHcOb_ISJUaCIHqOSkBo50IBVKg_SRNldbuFW5s_8WgwhkeXUkKw90DgGH2ISmh3HByDHVMkHlD5wpK_P_4x9bewVzyHCfN_jd3WZl1OnjTU2NyrjzU67SnxMwdpf6Fr45e4IqAmZb1-LELZySObvoGxFreMA7RF3G6QZ00iQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9fa48a9b18.mp4?token=JxIx7RfFTBxPd7WShJyXSmMCugK_SlnM9dwa3_YhKSE0Rfvo3LbA7w8n-p4S-IMn1XuNh6X66NH8J-SCbvL8JPtL1TYTRbmZL8dwdjt2Nsa0mqkU19z_Y4SP0F_oXJosCtAzKWyjp_jGXOgU3uEptwS8Pbm2pIrOL9KAGFoKfzgtifHcOb_ISJUaCIHqOSkBo50IBVKg_SRNldbuFW5s_8WgwhkeXUkKw90DgGH2ISmh3HByDHVMkHlD5wpK_P_4x9bewVzyHCfN_jd3WZl1OnjTU2NyrjzU67SnxMwdpf6Fr45e4IqAmZb1-LELZySObvoGxFreMA7RF3G6QZ00iQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
زندان هم زندانای قدیم؛ یکی از اعضای تیم تتلو یه ویدیو منتشر کرده و گفته که آقا امیر(
😂
) از پشت میله‌های زندان باهام تماس میگرفته تا موزیکشو براش تنظیم کنم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/92443" target="_blank">📅 01:13 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92442">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ed2c6f597.mp4?token=vsdMcZQ8DaFkjNL71uVxJEdMkQ2TYI9_BLGuu-bo3GNfO7oJxpUrQzb5VtecXc2B7pbvYHFlNgfyL73cCQSpvSE4_Qi8_HFpKSbLewLp_4s1iAF3G5OWAAwHyfSAu_yqMDyoq5WCcCfrnEoW58uKcP6mEXsV-qBb3VkJb-uy9ofYQUEMOml9h7hNnEfuShgzTY19fS7qJjgym2fE-GZqKmsDJt7qUnPgFv4SflRl6WRpqmE5StM4PmAWCht16Fyt06g0YryaGfQFLMrCDXSl1XrxinDXNb_wbB_O-a3LePy3h1V1QUzaihrWwqdjU5zsPmVE966XMIhFFjKg2kdH6jzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ed2c6f597.mp4?token=vsdMcZQ8DaFkjNL71uVxJEdMkQ2TYI9_BLGuu-bo3GNfO7oJxpUrQzb5VtecXc2B7pbvYHFlNgfyL73cCQSpvSE4_Qi8_HFpKSbLewLp_4s1iAF3G5OWAAwHyfSAu_yqMDyoq5WCcCfrnEoW58uKcP6mEXsV-qBb3VkJb-uy9ofYQUEMOml9h7hNnEfuShgzTY19fS7qJjgym2fE-GZqKmsDJt7qUnPgFv4SflRl6WRpqmE5StM4PmAWCht16Fyt06g0YryaGfQFLMrCDXSl1XrxinDXNb_wbB_O-a3LePy3h1V1QUzaihrWwqdjU5zsPmVE966XMIhFFjKg2kdH6jzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
دیدار رونالدو با یک اینفلوئنسر که طرفدارشه
دختره زده زیر گریه رونالدو بهش میگه اشکاتو پاک کن تو خیلی خوشگلی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/92442" target="_blank">📅 01:04 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92441">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/Futball180TV/92441" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/92441" target="_blank">📅 01:04 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92440">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j7gQJlNcTO40S785z_huOJr6dfFYfwtSpsje7rL865Fp2A5c59lUIFeuNogKsgEGAHFlmoA0CM9iZKZrVjr_shV8qdDW2PTVRJFRcySipWei5T0yfiRJn4ySegoOEZX7W8xZ3UKKuTgktZEq796QhF9rsLU2Ayfz0952QjerNVXJyjJt1qo1iVmPVnWYWL_XMuXnD_hi3hiMF29TcSG81RpYmcEsHoYWqvo7OPlxMHA2jMO-a89szMSEHLiUk_sBV5Kel6_PApKlyMOlT3WWliFV9GsuffWZWIDVtO8Tm1CCXC2o4OBhGibLyIiPmkPo9KuF8Ya7P2ceijla8grK4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
وان‌ ایکس بت برترین و خفن ترین سایت پیشبینی بین المللی که به کاربران  ایرانی خدمات میدهد
🔥
🎁
با افتتاح حساب در 1XBET از طریق کد هدیه
1x_1566529
تا سقف ۱۳۰ درصد به شما کاربران گرانقدر  بازپرداخت هدیه میدهد
🌐
Link:
bitly.uk/connect1xbet
🌐
Link:
bitly.uk/connect1xbet
🔑
برای ورود به سایت از کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
⬇️
اپلیکیشن وان‌ایکس بت
🔽
🔽</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/92440" target="_blank">📅 01:04 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92439">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a47e4dd2a8.mp4?token=pwR26XpiIYmKEKEBxX0MlEbGxMY3JqYnB_C2vBu6SNkZI0aUKLnfZzc02dMHLIbT4HWHCXiyCrxEHUcP5ensVI1AumlQL1Sv3V8MKGdHOMyIIGB3Lge0ecdSZOFqWzN9w5oyeeuFnLGKDNY2RoVXe5QYENsXFrwjU6yBDJR31c4TaWUzMQXS4vIg7PrF08EGTpDtfeFAR6wbhAatQoexSA5_hJyD2FzIm_65UPyHRbtdRieOQKDtEn4KOmSvgde-XmfnPk3Wr0m9NP1-rUfdR9aszQph8MHyiSYKsRILHe-2Ef0Lb2a1cpBhGwSXdjBeM3CGqNwXAHMGIGv6MduQjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a47e4dd2a8.mp4?token=pwR26XpiIYmKEKEBxX0MlEbGxMY3JqYnB_C2vBu6SNkZI0aUKLnfZzc02dMHLIbT4HWHCXiyCrxEHUcP5ensVI1AumlQL1Sv3V8MKGdHOMyIIGB3Lge0ecdSZOFqWzN9w5oyeeuFnLGKDNY2RoVXe5QYENsXFrwjU6yBDJR31c4TaWUzMQXS4vIg7PrF08EGTpDtfeFAR6wbhAatQoexSA5_hJyD2FzIm_65UPyHRbtdRieOQKDtEn4KOmSvgde-XmfnPk3Wr0m9NP1-rUfdR9aszQph8MHyiSYKsRILHe-2Ef0Lb2a1cpBhGwSXdjBeM3CGqNwXAHMGIGv6MduQjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ترامپ با اعضای تیم ملی آمریکا تلفنی حرف زد و بهشون روحیه داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/92439" target="_blank">📅 00:53 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92438">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hm8rb1HRasM-xRTJ12pzpkrycykZ6FNIPiXANDzOLMb1G_TldJHkkeBfoxrzwqNngGFlja30x5uHVHdbmd120q_oNjmPhI-IHtvApD7-Fq28JIHNEl2mXQ8Ry4CyibBz20PCcV1sAzUYzqo1RMujrqcBUz8xsHZUXUF0ku-Q4sbCFKSP8YFcpnLe-Jid1J_-g-qnyzJzEHd4g8RDDaqdB9-WosHUWHvM_vc61xN-Xjtd8-7Gqe6mCqreVzGfnHHu6jA-P-HUSV65kZlz2SZi-8Vo12oVBe7LlfL_4NNODGVc4pFPS9ea0vA0GJ8CY5Kj5KVg5vdH6bPKC0Y5UkdGUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
🇦🇷
طبق گفته رسانه‌های آرژانتنی، خط‌ هافبک‌ اصلی این کشور در جام‌جهانی متشکل از این چهار دوست عزیز هست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/92438" target="_blank">📅 00:45 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92437">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f2gUqqWQZYdEMATq5bgnFjyoCd4LplCRTp-vXxGyffhg9p9Uck2z3dUR4W1iPoe0_uDakKD4FpD1GVfclm42L9xCZtYMix8E8MjOXHKWeU2hvzUZ1dw_sTsiNfz38HtXi_0umu4PMwZgH3xBjmkwenXja8Iyvj1neL4kgdzE4vzUSirodCIxZaAzeZb6e4Yvx8hKOviWPT2No7hoVsp1RICOdIN5PIRecJuROAD0Ujht5ye71bHWo6LFEdXxYEDy9V8aUkZd74oJDN3OWfZFzawmUb_R3wTxxieVcG3mZNxMaRu3-Ev-MCDJKi5Ua3qV1xHDG5rQttVnRYmraIHfkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
کمتر از ۴ ساعت تا افتتاحیه سوم جام‌جهانی ۲۰۲۶ به میزبانی آمریکا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/92437" target="_blank">📅 00:36 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92436">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BjTcdL2N9gPuj_3H3Y0yWtdcKd3nLlQhHPG8sHfyxIJL6enF_rFLsQyKC-6z7DBBT1HP8CVmiUGOSri1kg927M89Ndz8ZpzawM303dWQMGNpuLL7qsxquJb3t7f1ckYkAfimd8oHaYcPBvcDlXUuZ8lFGhOQXuh8NG4By3171z72CDOYB_th3lqmB0SP_mCiOw-JHsWTTUGHfnXqBtWT4QuaE1mChf7LQ2ADr9w-hZMO2zZjJ17UB9I71ao2Na_fDKGdJWW8bU3Yg_xAJ-fbGWzUAetVuSEX1uhp9CBNm0EzV1ZmoiHMPPlgqIU2nUzwx8MfGrNPSetSk7UMHc9VDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آمار نهایی بازی امشب بوسنی و کانادا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/92436" target="_blank">📅 00:34 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92435">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GZF953ukFrXePehMcTPZA2oK2BM0xQ3VKLLSENg_O_vZhyuNlhEI4Mq_OoKmm4YghPeY2rIAYTQDSgWqPHESlhcsY-r4AIVnhSeEuwol0TcwsMMflPiHUbp_Nwq-0Ku7csJE77L0kIOsNG7g8kmMNO3vAj2GgZm18zD5Hu_--3t7AEJMt4QmPS3N0eO6ep2js5CULKaXdQ4za0aiyTCWv6f2IQF2rzWzU7axkXfBpjatxdKk3t3q8BlQzB2zZnxrhvkeDtYtB1KKk9HRUkEXYHsZyKM4PHbgFomxGkwmbVvoRno3uoQKrYWUjX0k7sKjjUa9l1a8khwMBOEbzPwXxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
هفته‌اول‌مرحله‌گروهی‌جام‌جهانی|کانادا بالاخره در جام‌جهانی نباخت!؛ میزبان مسابقات در بازی افتتاحیه دوم مقابل تماشاگرانش به تساوی رضایت داد!
🇨🇦
کانادا
😃
-
😃
بوسنی‌وهرزگووین
🇧🇦
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/92435" target="_blank">📅 00:33 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92434">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">#فکت
🇨🇦
کانادا اولین مساوی تاریخش رو تو جام جهانی گرفت همرو باخته بود تو بازیای قبلی
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/92434" target="_blank">📅 00:32 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92433">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CdWtnqBBKDOIYus1VllaHoo-u3G2wHMyJ_cCZRAwMp5YAyrHfugCtdy-3smkHSXxvKC9xCTBXy4lXHnHG7xXgiRq7vfg6x3TL3PxI6VZcmoY-hXaYQqpQApAtjXwebvwROtgWOrFWClTKHIAH-y7vEkfVK7FRF3Gee0SjhTvhZjVfuSvkiOkkc85EClee_lps6xesrjUAs4FfdF0IsVPRjJdCL5llwxp3-qI0Ya5yRMibYrjrLA9lPyfa8NoPuxt2a9xAz77RWpxpHgiALMDQ_OBa_ym3pJ8nljoZeq6QfOSOQetmBWE3wcwRo6oB_Sd4Zgqr7C9Wq_aXhTW1LervA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
هفته‌اول‌مرحله‌گروهی‌جام‌جهانی|کانادا بالاخره در جام‌جهانی نباخت!؛ میزبان مسابقات در بازی افتتاحیه دوم مقابل تماشاگرانش به تساوی رضایت داد!
🇨🇦
کانادا
😃
-
😃
بوسنی‌وهرزگووین
🇧🇦
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/92433" target="_blank">📅 00:27 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92432">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FrreH3y8uFTw-TN594KBO5u27CS1TrWdZ99xdYBixQrS-w3eFCjsDdc_fdWcWlJJwfUOBzpG4ZxgZQk1vhDsANtL-pRYNa0wMnrNYDIBEc5OlKsSTT_T0PQL9Vfp1N7Jb0C30Y1QXq9q6OfFV6YBFObBefS-7nqT1rzyRSwRyEl4NxnTJbZhGr5dnlpS-xR7PITDFyJ5LxM5C5eqXb4skCClWpbejTzB7E_cGmy8U2EVGLU-l6Ju29eFOl4wckagIpkGQ4tCUC5Gw2t_4zmG2pevV8qnNc5WjAReyy_8WyYOa2JECY24bzZ8uKCSQeFd-oXQoVPxgBBxDxhBbYI6Uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
برزیل
🇧🇷
-
🇲🇦
مراکش
🏆
جام جهانی ۲۰۲۶ - گروه C
⏰
بامداد یکشنبه ساعت ۰۱:۳۰
🏟
ورزشگاه متلایف
🎲
با بیش از ۸۵۰ نوع آپشن پیش‌بینی
⚡️
ضرایب شگفت‌انگیز
📊
نگاهی به آمار دو تیم:
- برزیل پرافتخارترین تیم جام جهانی با
۵
قهرمانی است و در همه ادوار جام حضور داشته است.
- برزیل در جام جهانی ۲۰۲۲ از گروه خود صعود کرد و در مرحله
یک‌چهارم‌نهایی
در مقابل کرواسی شکست خورد.
- مراکش در شش دوره جام جهانی حضور داشته و بهترین عملکرد این تیم کسب مقام
چهارمی
در ۲۰۲۲ می‌باشد.
- مراکش در جام جهانی ۲۰۲۲ با حذف اسپانیا و پرتغال به
نیمه‌نهایی
رسید و یک شگفتی بزرگ خلق کرد.
🧠
اگر دنبال جبرانید، یعنی از مسیر تحلیل خارج شده‌اید.
🌐
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
💻
@BetForward</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/92432" target="_blank">📅 00:27 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92431">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jd9wns6g-O1wlXyFIsbDKy7trdwanunczbVP-3rEPl-U0Jo5pQl2tz5NoaulFt-2eTo_QsVJqWZGv9q-OfcTRemWNgysQszisWWZxf5SQJD8U1uGo3z7vIkg01RBrsjy5gi3Wjvb3Y-V9kansnIkKwzGS2YHwtJGx1krxvR3_EMvGOGllcVw6U37gDyODdfillD22VEqrDyzylbxnsqQE5hCpAHemEr0JJsj-_DeCBJ5d284p6vwEZzdZI6jEwkGaOZ5N-ZoaX9K3gtmg8CwkBw4qimB2jiUWaAJwpFiWvizoWeBSO33x6kSX3SLh9QDwW8pjqhzithKheiv8OaDsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
‼️
توهین‌ناموسی محمدحسین میثاقی نسبت به منتقدان تیم دوست‌نداشتنی قلعه‌نویی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/92431" target="_blank">📅 00:26 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92430">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QsuqLp23T9mvWV7ldq-q5h8MhxnjcBku4CgLn2zOUqU8XY0AeZQRMQg3nb2uaL-OaBQeb14qIa8_ZJHkqjrA10YRJYxEALEk6ykYXBlPHZBgErpljEu2vK8IS9YDYtZhZKQh_FZebX-Spl56cBUWRy1TfkPQTKIbLULWX2zb5CjfARJE3hqSh0WuJkyXATUuDGcJhuGSYHeuEdd2bJ4e2m7FV2K0FfRufFo5rKmg3D5TDeRJFbe9TAS0OPYyORYjdp3gESiRLCU843oA736xDSq4cHhdydnGM_i08_TtJtBV5n3zWnb9fx4ulDiqGInKXOrrvro-3bjv5CrIF3AfUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇨🇦
گل‌تساوی کانادا به بوسنی دقیقه ۷۸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/92430" target="_blank">📅 00:17 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92429">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🇨🇦
گل‌تساوی کانادا به بوسنی دقیقه ۷۸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/92429" target="_blank">📅 00:11 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92427">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">گللگلگگلگللگل تساوی کانادااا
⬛️
⬛️
⬛️
🇨🇦</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/92427" target="_blank">📅 00:10 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92426">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
‼️
‼️
توهین‌ناموسی محمدحسین میثاقی نسبت به منتقدان تیم دوست‌نداشتنی قلعه‌نویی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/92426" target="_blank">📅 00:06 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92425">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c23cc9050.mp4?token=cFL9bt5hxynCWakGdV4a3fs3lwVs1ambz3MdfOzTm4t3ajKgeCrPLQKbAMNL5gKl2Wz9_1BFGsWe_OGJzcnwgud_c1SrJZxhpXZeR4nF181fHM1StjhWpX_F9cG3p9IEOtmkuDYobNiFwpFbhkbUmrBVbEyfkyNpio33YirI_WbJnovfvL5kZcVGaV8nyrHbiGgYyW5J1CkH8fF36RqiE8mZgAzbJJzY1pNojVpvbyI5V1e0i8O22tpbz_r_jKgWsZkuo5L86nl2lC3weWMTrnJQAqh5e7fiMfVo61Yd8DMVa8Y5hYV6SyqrN6LXeqoCPnw2cw7keBjtMlZF418u_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c23cc9050.mp4?token=cFL9bt5hxynCWakGdV4a3fs3lwVs1ambz3MdfOzTm4t3ajKgeCrPLQKbAMNL5gKl2Wz9_1BFGsWe_OGJzcnwgud_c1SrJZxhpXZeR4nF181fHM1StjhWpX_F9cG3p9IEOtmkuDYobNiFwpFbhkbUmrBVbEyfkyNpio33YirI_WbJnovfvL5kZcVGaV8nyrHbiGgYyW5J1CkH8fF36RqiE8mZgAzbJJzY1pNojVpvbyI5V1e0i8O22tpbz_r_jKgWsZkuo5L86nl2lC3weWMTrnJQAqh5e7fiMfVo61Yd8DMVa8Y5hYV6SyqrN6LXeqoCPnw2cw7keBjtMlZF418u_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
‼️
توهین‌ناموسی محمدحسین میثاقی نسبت به منتقدان تیم دوست‌نداشتنی قلعه‌نویی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/92425" target="_blank">📅 00:05 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92424">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dUwHbbM_jcdsNUP-GPMoIaed-PFFWVLXm3Oms_4Y2YJjWdEx7Uj2rrxKHBnTbQbCZleAVsfTtsdBQy7_tMkgB_fLtYLZNBGZmnmDH_CTi3JlmfgbmaOgyfmrRdPIDv843OcGsV-N8VBfgEYKJF7z5hpL1VjddxR5YbRe-ChidpUhTPTZnAd-K6cxel6u_82RG-jXqyXKnKEcVDngEUCcjTLB1WUoaCIFsmLF1nmVtmoD4ODhTNHHhv3Xv7z0CKco4RwHjFzi22trKMS5pY_f3nUSSymBTPxrIACi-O74GNnbXmgq4PkqIWT2vUG1R5Cw5ZJvjb_mLvbw_qz0QEExcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
لواندوفسکی دقایقی‌پیش با پرواز راهی شیکاگو شد تا قراردادشو با این تیم در فصل‌آینده MLS امضا کنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/92424" target="_blank">📅 00:03 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92423">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wgyb1FE-At39DVX2ym35ePfiRqFpHp_jUwSxRCf-2g_7g2PsYFidSjPluwotza0ML3ty1W3hvEvRYvMlYcpQAt9fcSVc7OKhkFkn9fhrJWCLToeNM36oix4rK7WBywIFFBsS-8FFvx9vaU6nC-eMi_hDZJWdTYN2Db9k1vNN5fHNnXEGdUNRmr4oTUgiLNgDZs5hJNd7iw4b2Va-gcPf5os54DXwR2mAyczsMMqvZv6cBnysZmrcT9nJEmEPTzZJdfBvY3L_q_kuLdFYnK2nu0RxvanVymhD_TyfzTGS5GoXEjfwJSzJKwaDj5_4Bi81MP3LlVwqxZXvgmPUSJfcxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
پیش‌بینی کن، رمزارز جایزه بگیر!
کمپین جام جهانی اتراکس با
۱ میلیارد تومان جایزه
شروع شد
🔥
جام جهانی با
ربات اتراکس
جذاب‌تره؛
۱ میلیارد تومان جایزه
متنوع در انتظار شماست
🔥
🏆
۲۵۰ میلیون تومان قرعه‌کشی نهایی
🎁
۵۰۰ میلیون تومان جایزه با
جعبه‌های هیجان انگیز
👥
۱۵۰ میلیون تومان جایزه برای دعوت از دوستان
📊
۱۵۰ میلیون تومان جایزه لیدربورد
⚡️
۱۰۰ میلیون تومان جایزه هفتگی
همه‌چیز داخل ربات تلگرام انجام می‌شه
!
کافیه ربات اتراکس رو Start کنی، بازی‌ها رو پیش‌بینی کنی، دوستات رو دعوت کنی و برای جایزه رقابت کنی.
👇
همین حالا وارد ربات شو و پیش‌بینی رو شروع کن
👇
https://t.me/EterexBot</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/92423" target="_blank">📅 00:03 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92422">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">نجات دروازه فوق‌العاده مدافع بوسنی
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/92422" target="_blank">📅 23:46 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92421">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">عجب کون سفیدی داره بوسنییی</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/92421" target="_blank">📅 23:45 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92420">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41c6c690d9.mp4?token=WJt-Eyp1dH29hVxnlekesWaznT0_cBn-oX436ZRtPe9yyOiRRMY6ZEQ5SuEiB1naSadvXyuOrpAEojGCtGWjwbNAIrQzsmnARwJzIxKCF--DB8vMuivRngQFOO8xFfvTj_af6ZeM7phX20V-tenQ_UYIy5X3QJHcS5KGJxSpZTF6sJVcGYvY__Pj2rRQgk24wggInGcf5GbGUJ7nEQjxPrJCyitl0gcd40aTGKpI6VyW3xcxiUv-8FLq136XSAv-EP1WvX7j9lC3RcPQ7B20gsBwOSTOhsFPKEthtvowB-eDRajC2SUagDvOC836YI3_1xDSDKfThKL1OQTqX7slFpqFO9acurw07DUjf-NMQzoJuzWx2ZnHr0e8lFOvad5rzef-Vyr16Zn0K04WGSUwsYXs_DAd3_ACiw3IAWnfAQtB5LVdVstR9WhA22uz5HtXGDsa9M30GRshAi3z8fSvcz94t7YG79MGGy5-PrCxk9Br4wh3-6YiCn1Lj1riUgexLlFIr6M3dFUY41cfmgnINLeQ8UDeqM-VfIUcpSjIilKRRNGEKwZhNuIKQAQck00jkCNwRl-ZzxcQsVKnsiTaSYO0YFUhxfywlSQN8N7zzzWYJ0GfgEerQ-kvi9WaG0Ics6s1v5bhyGlOXIU0vRtplUu-2vnRnuULRaPyLsKhVXI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41c6c690d9.mp4?token=WJt-Eyp1dH29hVxnlekesWaznT0_cBn-oX436ZRtPe9yyOiRRMY6ZEQ5SuEiB1naSadvXyuOrpAEojGCtGWjwbNAIrQzsmnARwJzIxKCF--DB8vMuivRngQFOO8xFfvTj_af6ZeM7phX20V-tenQ_UYIy5X3QJHcS5KGJxSpZTF6sJVcGYvY__Pj2rRQgk24wggInGcf5GbGUJ7nEQjxPrJCyitl0gcd40aTGKpI6VyW3xcxiUv-8FLq136XSAv-EP1WvX7j9lC3RcPQ7B20gsBwOSTOhsFPKEthtvowB-eDRajC2SUagDvOC836YI3_1xDSDKfThKL1OQTqX7slFpqFO9acurw07DUjf-NMQzoJuzWx2ZnHr0e8lFOvad5rzef-Vyr16Zn0K04WGSUwsYXs_DAd3_ACiw3IAWnfAQtB5LVdVstR9WhA22uz5HtXGDsa9M30GRshAi3z8fSvcz94t7YG79MGGy5-PrCxk9Br4wh3-6YiCn1Lj1riUgexLlFIr6M3dFUY41cfmgnINLeQ8UDeqM-VfIUcpSjIilKRRNGEKwZhNuIKQAQck00jkCNwRl-ZzxcQsVKnsiTaSYO0YFUhxfywlSQN8N7zzzWYJ0GfgEerQ-kvi9WaG0Ics6s1v5bhyGlOXIU0vRtplUu-2vnRnuULRaPyLsKhVXI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برخورد شدید بازیکنای دو تیم با همدیگه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/92420" target="_blank">📅 23:42 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92419">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">اوه اوه
گلر بوسنی بگا رفت
😐</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/92419" target="_blank">📅 23:41 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92418">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">نیمه دوم شروع شد</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/92418" target="_blank">📅 23:37 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92417">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D4eqVtxNFutYmNgLzst3CB1l5Uak_v4g2LXwzIdmEu5CHsAIkUZBXlFbLSqy0lGjW4P34XrVsWu6oulC4SCF94Xn49s3g7PeVrMcwj8oxH1Yh2aR5BLuQ9MOU9XRmEd2R113jfKQAW_pYmTe8nqkbKg6o5DgypAmNS1tXqgjQLSUFccLLvAnZOLzWYOTBY9TwLrPYM1Hwh9CoR4K1vKLRYut9wyX2nHw1c7eDFTpdWUHu8t9dPxm84Vq0MO1syfbKD90jsSBMZKMlTdgvB1QXmlvxJsGWZ79et9d0w-vwEG8MUG2UyoQX0vtsxvQG_WzDy0v026TUT-5Rtq9GA_lIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
فوورییی سانتی اونا
🇫🇷
:  بعد از سیلوا حالا رئال به سراغ متئوس فرناندز می رود!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/92417" target="_blank">📅 23:36 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92416">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uk5vUQeFPlt4oGlCWDKvhavqZG_T7IQYpZ-_EZ_GccT8b7oQI1yguKUzR_1drNfnaWbWwoiHMjcjNXhtPrmeTI6RbQ4E8AxD6KZ7XyFK0aNLODdiTGGogS8k4wY0XDZbTXieZsoR4_oxUyoZsg6I6MwumF-3BkwcLGZU5_tXAbOCeoOE_8mKOMEnCrpUt3Q9Q2EKJPaALySqVOkKGdX1O7MdwqNKGOSW5gmqYWfr7ydt3jhcX9lXTslNDjOwy6sN7yorf0EcKCOKheUR3q0qizuhtTzwmKv1tZfp47xN6de9ORzySd7JWtwjzlAYWeIXR7c4-50MtVRjAUvXs9tdZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
🇵🇾
آمادگی ورزشگاه لاکچری سوفای برای بازی بین آمریکا و پاراگوئه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/92416" target="_blank">📅 23:34 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92415">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BenrODIbU9fMvvUBuSbSUDMY8jB1qViKZgOYdCu2B5fOpJeiSxvVN_lEEbbAcmJGVIS9JZhWplsqV-z66DnSV0b-RO5xvQ2TIY31dz9R-3EviC2ZTo1QmakjDZUs0P4NdLTXjgGVhF25atL-G_Rz2DciTmhi81q_Q9vB3w5K94kWvGMua8fM2SCqJgNRHU0T5pJe4KnAAGZajdlbXNbjXHjPgqX2Pm7xOD6EMIXS4uLpopx9dm1i_7J4hvw2tIRJ9b8s-qorDYhGA9YOZgeWt07m3im7exdGHvTAjtSwhmulZCtw-Gm_z7pe8IWmXRM2BQkaQSkz508SfECUeRILNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آمار نیمه‌اول بازی امشب بوسنی و کانادا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/92415" target="_blank">📅 23:33 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92414">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WuMyF-H0NLBfnl3NDeD-ODA-RDQJ3qTFtG_R0OptXFpvITliaP8Gond4i3GmZKZ-VIvvHIXIV82LNPhqgbElj6JsXOMaVwajLzkzT3BcEdQEY2E0tThDgDu_ZpUnYZysC__kMwnRRm7qGvz0zgrrZ5WFiRt2rIV2NUEm2IHk9_UISL3qb7_tCTCUbPWKDgXO463fW3qJumx4PlVG7nzqQRiULHxJgTyZMjH73SC_hr6ko1oveZ_JEX7mL5dzvHeSsM8j-96NNTmqlAI4EhnqYC3YSWUFNox3le-k0rMe9MIRYaFHSk50SyIhZ2HFONpS-f5PzAQhqAiLFqNC0mzlTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
طبق گزارش میگل سوریانو، ژوزه مورینیو اعتقاد داره براهیم دیاز در حال حاضر بازیکن چهاردهم یا پانزدهم تیمه.
✅
مورینیو با فروش دیاز مخالفتی نداره و اگر این انتقال به تأمین بودجه خریدهای جدید کمک کنه، چراغ سبز نشون داده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/92414" target="_blank">📅 23:31 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92412">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🏆
پایان نیمه اول
🇨🇦
0️⃣
🏆
1️⃣
🇧🇦
⬛️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/92412" target="_blank">📅 23:22 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92411">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚨
🚨
🎙️
عراقچی:
🔴
ممکن است ۶۰ روز مذاکره تمدید شود و ماه ها ادامه داشته باشد. ممکن است تمدید نشود و دیگر مذاکرات را ادامه ندهیم. باید ببینیم بعد از ۶۰ روز با  چه فضایی مواجه هستیم
🔴
از تنگه هرمز هزینه خدمات رو میگیریم و احتمالا بزودی برنامه مشترکی با عمان درباره مدیریت تنگه هرمز اعلام خواهیم کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/92411" target="_blank">📅 23:21 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92410">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YgJ-_Rfz7RkHo37c4YeowQWiKZnBiHFumAQQ7AhM2VkWCY-8DmDqjS4dlPLIkHh8o0Ss3MgRxkaH-7atYmae_y7hDbqSpUVjdVHYkOziK3M4mQemW69nyOts9K0sgf8X-iGDX8-_hviFAMjPl__9bUwnR01gkeoStkxLfLcSpjrhEndZ5u10INKvivzqhVGEOXwmhWZ2LO_mnh4L7R-f-EZUClHuqUXv07KEYov9lcIUoWbMaA5QKgs_KonFqTMi_DxsiExCJj9oG3bjBnquzZo-J2Xx5ihcy5nRbDA0Y6HReihTT1mgVV76AKjZszULO3dmo9fjhDt3GZW4lIY9cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رایان رینولدز دلها بازیگر محبوب ددپول تو بازی بوسنی و کانادا حضور داره و از نزدیک بازیو میبینه
😍
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/92410" target="_blank">📅 23:18 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92409">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pRbeaRbB51y9SCPj5V5uDHEpIvQSIHcInKVA1RSrG0IZnd3cGmPCNLLJywMZRY67vKpm46wl5-5UTlUp6QV8CoHJ_ywgfr2wIHjXoRLV2ZqZS2vmyU65KC7VMbDakHLU7T1ScJYnX-Mj-rnmkifBDnaT-lV7QCzrQcdy13gGL4z5vuQe3yQWLTTrITounT3gpgQ3CFJSwFW2mMwOTcZJ0Hc0w9CjPbZAjXgCjAtngrIYXwRXHMcGpJU-hxqQvjeJ2c7snc5eXVkfxetbmvvSKPP1iti8JheO24rcW57oJU8y5268vyvNHxLVCXVrRrOmnPX4cpSHVeOQ-ttddC6hLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قسمت بد ماجرا اینه که مکانم از خودشونه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/92409" target="_blank">📅 23:02 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92408">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/cb9e5acac6.mp4?token=mVE0WSXKDjvaNIAFgxGQ2GU2278Wm1uaWutJZXVkMvYr-AONYFjcS0zwhewJj-IZkGskrAfM5piDmpzvYo_-CDsh_tzvB70n2Evd5mDL0zD8iNUYrk7dNbVmOGEm7csIbeVyF_TQQmFlP81ELOR3Wi9gpQGqiUHYIS8697N1rBg2LOtbAZx79XXE3I-GFW5IpSkQAvKhhEvs9TB8tQaDFJHNF9hYdI6g6UCfpY0FQVKcr20E18smAWkhaPT_PMA_xsZF5nj0dZvR38BiXcOWyUjjvTjYqX8PKWKKf-jaFxB36AyJ04FZM6JNUWIscKy_7fVfveoI6ZU8MbZpWa4zh1VA8A3LkPQwkoF0CKYmEtc0v5nuROqsDPaXFCrZAdVMmsHTkzWkEzfuY4jV-_n6Ux6VJ_llqfgK32zOM48etCiN0bz01MthuTrkDkoR4uAvfbXMAiqz_6qwqaVipCqjR6W97vwrRe9xRFbJMB__ObOPWA1bRW4GKSCa6-5gklFCOGIaWZ7-MLiR_4inio7ovp7meiSp5M6Z87_YnT3QjCzghUKwJl4AE9bUPlqJTV5DX9AbhX8GX52B8EmSkDqyfzDbA4V9EdYQmNlBIegveXJDCyqJE1Zpru69U7870d2hTktdnoPukmNOmW7LgWIotOnOLLeOMTGalSBmD878Q5s" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/cb9e5acac6.mp4?token=mVE0WSXKDjvaNIAFgxGQ2GU2278Wm1uaWutJZXVkMvYr-AONYFjcS0zwhewJj-IZkGskrAfM5piDmpzvYo_-CDsh_tzvB70n2Evd5mDL0zD8iNUYrk7dNbVmOGEm7csIbeVyF_TQQmFlP81ELOR3Wi9gpQGqiUHYIS8697N1rBg2LOtbAZx79XXE3I-GFW5IpSkQAvKhhEvs9TB8tQaDFJHNF9hYdI6g6UCfpY0FQVKcr20E18smAWkhaPT_PMA_xsZF5nj0dZvR38BiXcOWyUjjvTjYqX8PKWKKf-jaFxB36AyJ04FZM6JNUWIscKy_7fVfveoI6ZU8MbZpWa4zh1VA8A3LkPQwkoF0CKYmEtc0v5nuROqsDPaXFCrZAdVMmsHTkzWkEzfuY4jV-_n6Ux6VJ_llqfgK32zOM48etCiN0bz01MthuTrkDkoR4uAvfbXMAiqz_6qwqaVipCqjR6W97vwrRe9xRFbJMB__ObOPWA1bRW4GKSCa6-5gklFCOGIaWZ7-MLiR_4inio7ovp7meiSp5M6Z87_YnT3QjCzghUKwJl4AE9bUPlqJTV5DX9AbhX8GX52B8EmSkDqyfzDbA4V9EdYQmNlBIegveXJDCyqJE1Zpru69U7870d2hTktdnoPukmNOmW7LgWIotOnOLLeOMTGalSBmD878Q5s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇦
گل‌اول بوسنی به کانادا در دقیقه ۲۱
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/92408" target="_blank">📅 23:02 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92406">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">سطح بازیای پریمیر لیگ ایران از این بازی بالاتره.</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/Futball180TV/92406" target="_blank">📅 22:53 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92405">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">گلگلگلگلگلگگلل بوسنی زددددد
⬛️
⬛️
⬛️
🇧🇦</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/Futball180TV/92405" target="_blank">📅 22:53 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92404">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oar_J-AC5qUNYMRoFaQxPcjtTBd8MPLOfAc2FoVVX2sLCmLWK6SUoJ8ZY46oIpORjyqfNlIhxpHrvG09uGYXe1pzigPwRgryso9P0Rq5fzvUmYqXZx-c9CQajB8x2ai46F4soj5eC7sAB02sqh6XkfLRutGwYVmiXdYjWitUQPT-Mmq5O0_DpotJlxnbtKrMZu47rnh_gT3St7pmNYjPVxwYbzS58gMEQkzLlVSUElh3Z3yQsnMbNzJP0PsRpYbAI15FjDK-ozJ75p3Na7nC1i-8uiHbdTwCZOOGzKBTa4T6J8soDctYTjvmnNIXj9GfQl1GjJhlBZM4evJuMyHqlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازیکن کانادا این توپو از بین اون همه جا دقیقا زد وسط دست گلر!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/Futball180TV/92404" target="_blank">📅 22:51 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92403">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">سطح بازیای پریمیر لیگ ایران از این بازی بالاتره.</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/92403" target="_blank">📅 22:50 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92402">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">سطح بازیای پریمیر لیگ ایران از این بازی بالاتره.</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/92402" target="_blank">📅 22:48 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92401">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">بازی تا اینجا کصشر خالص بوده.</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/92401" target="_blank">📅 22:46 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92400">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qYWZ0rwFhlg7EdPfZ6F3oV5gjPWFki9wZdLl3Y7-hhfIV8Un8iqNRBrMFAL6l06dbnWbWIYRkznMRkn4uH0we0bPw7ikELc--UHPYtV_P_s3UStLJsvVTj1F5lHTo6cUYqVhCECGZGxq5DxbkFURNzcvpnif0IQyT2RpCbFZVPAJgitSFvhQ4lp8X6-l6lWL0d5rR4BzwIpqWSRSKc6gB4_93QIPFyjnjXR-3WX5JUt0R-nIRD7K3S2qfQejiwjZpQFEGvYLO9HEYvCrG0U-7f8xQUvGQbBTfftpVZGgeenab5l7-jxwWLnM0cgmITf8Daz4V4UzH615hjWHaa4fQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آمار کانادا تو جام جهانی تا قبل بازی امشب
6 بازی
6 باخت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/Futball180TV/92400" target="_blank">📅 22:39 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92399">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X6nVZdmEL1K0Q252btkHb_-TlZ5Q7xkCTa8aY10hMk6tZLm6OZ4RGGQebo801nAwfcqkfZegiDRd2dlZORClmFEDAHlIfHsnYYSZq2vWhZrUJtnUPDeHA3eW1Mri5zKxYjrrZYnC_JtUtul-eBlWs4AwPKB7M4sbu-QZDfTLJuIMn1DUFDZ2hDl64UmXYgOq58GQ5Nl50X4sA7HvlzYzKUk-KJde80H6FbFPwM1s5DfVLK6dPP7ZpTLrg9uHL4RO5Fat5FVzAXD7_tIhuqHMSL7bi2cCUM0U13fTmccjTPKHgYOo5ULjwjric2uUhdigsY8HUcgrZVaAyRldW6pSeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شکیرا : از وقتی مسی اومده آمریکا، همه میدونن GOAT واقعی کیه، دیگه تام بریدی و مایکل جردن نیستن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/92399" target="_blank">📅 22:32 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92398">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🚨
فروش کانفیگ‌های نامحدود
💵
قیمت: 450 تومان
✅
سازگار با تمام اپراتورها
✅
سرعت بالا و پایداری عالی
✅
مناسب برای گیم و استفاده روزمره
✅
تحویل فوری
✅
تست رایگان قبل از خرید
❗️
پشتیبانی 24 ساعته
📣
کانال رضایت مشتری @kavianivpn  جهت خرید اشتراک پیام بدید
⬇️
…</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/92398" target="_blank">📅 22:32 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92397">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fhfiFyco7VFY--1MWc4dLG8eIsaspca8EPKwRXsuvHNabuJFkWvGZuEdB2G2twMxmIyRFNmjkQfqxKvBC285BlMZK5W42zi2fUtmZKQ8Uh817ND5beOGc7eT4450IPtGEVVgGH2e5ggFzggJfl_ziTd7WUoD8HK_cVJ4QTVTmDC_pPFZ77SEvSrYXMoh0Dxc5QhG-wzpiFoalNAF1AWl4ykGy8I6JYn0R_E8A9mFozvhC0O-Tp_nClKgmeCEEQZjo__fOL7u_UOLO5FkhzQDo4nRWpmBwDhnwl8Xxh_8OSUcv-3UewaTSutlhSR4tjUEclq7jMvTQoxMKOgew_O94w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فروش کانفیگ‌های نامحدود
💵
قیمت: 450 تومان
✅
سازگار با تمام اپراتورها
✅
سرعت بالا و پایداری عالی
✅
مناسب برای گیم و استفاده روزمره
✅
تحویل فوری
✅
تست رایگان قبل از خرید
❗️
پشتیبانی 24 ساعته
📣
کانال رضایت مشتری
@kavianivpn
جهت خرید اشتراک پیام بدید
⬇️
@kaviani_vpn
@kaviani_vpn</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/92397" target="_blank">📅 22:32 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92395">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HAFo-gXBgfQk0dQPdC6R_i9FBdx3R1VNzuPGCOPourtOk8iWJi2rSbI_znbDB5M4MI-8_o1MrDv8Zf7-kMdD9UDA_QMzbv3bH-DbECaVgTvh8ybPRXpB9-ZTejduHbVeN-XdRpZHxikOcnc-ch2UdtWK5JpvAld2R16iHkYDII1M_qL3qdqzAb9m16tVFSu60s4PDIesaagVuT55sP2YkSjCANv1ojYgya4yB2fhDxbi6CE4tn1Biv9a_lYdFm7DIpxBVVYZKDNZgqmVdiK7QapsE8gIm2yM9SEJAYDAI25iNCMyfCI2UsDLAWF8x9ea1wBwlYVFAPFWuQz0tq-p9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
فورییی خبرگزاری نزدیک به آرسنال:
🏴󠁧󠁢󠁥󠁮󠁧󠁿
آرسنال به بارکولا علاقه دارد و میخواهد جذبش کند!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/92395" target="_blank">📅 22:18 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92394">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5318d7b2c2.mp4?token=H5E6tywjqT18jaQf00fGsDNM3P-4m3mSjn9URUfWZa8BxwDviqKQ0M1j1kXCss5aaWKtewb0yrv2vAxFs7P71_-K-ow2BKDGRKA6i922MOu_M-FxaJmo0mCkI5TovaGiww82H3CnNzbTRXGHKEYx6gjFkkEryVt4bXMnEQSXw6fNzEP_CC3pwoHg3WesJT1iPl7GPek2Owl-iinc5fLGEx3Ahbxfq9MDRSaJN0_lMJv7Il0NlRjnQ-KjR0nkxBfWfsQb8cDkMz2f12fyAVGY4hbPFgCkITi3MogwrAqVR_UCiDgm90qNtn2PVxCpK90RrOihClTro_EtqAMjmOlT1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5318d7b2c2.mp4?token=H5E6tywjqT18jaQf00fGsDNM3P-4m3mSjn9URUfWZa8BxwDviqKQ0M1j1kXCss5aaWKtewb0yrv2vAxFs7P71_-K-ow2BKDGRKA6i922MOu_M-FxaJmo0mCkI5TovaGiww82H3CnNzbTRXGHKEYx6gjFkkEryVt4bXMnEQSXw6fNzEP_CC3pwoHg3WesJT1iPl7GPek2Owl-iinc5fLGEx3Ahbxfq9MDRSaJN0_lMJv7Il0NlRjnQ-KjR0nkxBfWfsQb8cDkMz2f12fyAVGY4hbPFgCkITi3MogwrAqVR_UCiDgm90qNtn2PVxCpK90RrOihClTro_EtqAMjmOlT1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
افشاگری جنجالی عادل فردوسی‌پور:
فدراسیون بعد از اتفاقاتی که افتاد تصمیم گرفت سردار آزمون رو به جام‌جهانی ببره اما فهمیدند که گاف دادند و اسم او را در لیست ۵۵ نفره نداده‌اند
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/Futball180TV/92394" target="_blank">📅 22:06 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92393">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef6825a80c.mp4?token=bq9DRd8hxrmCozQ2YNbRHt540dvqqlSmrzXKRIe91vNrG5MdYIDgfXo6dVeYtwoQw7awYkX8WDGVHIMtxnXDNlyBoSLr2OOspD0pJ0CEYUg0PZ2Z93KM6eq0gi9zCUCx3CqAXbc4Kd89C-ptu6RRXFL4V2_3kJt8gFOFerU8i9CjUWgsA3qW8r9HaPJsGoSLRa5KXbv6tzD0Lg_CQLHn5meRf7gmvYFww6e_6bd3HmSGdyj9WqwoYQl1So4Bw0ZSmbdSdPordXgixSnqXJgmpyhhzwwqN3RhP1JBREfaw89nPhdQFwAmtk7CK5AnjPFpHHCnIBYVI965Rm6TMfTtpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef6825a80c.mp4?token=bq9DRd8hxrmCozQ2YNbRHt540dvqqlSmrzXKRIe91vNrG5MdYIDgfXo6dVeYtwoQw7awYkX8WDGVHIMtxnXDNlyBoSLr2OOspD0pJ0CEYUg0PZ2Z93KM6eq0gi9zCUCx3CqAXbc4Kd89C-ptu6RRXFL4V2_3kJt8gFOFerU8i9CjUWgsA3qW8r9HaPJsGoSLRa5KXbv6tzD0Lg_CQLHn5meRf7gmvYFww6e_6bd3HmSGdyj9WqwoYQl1So4Bw0ZSmbdSdPordXgixSnqXJgmpyhhzwwqN3RhP1JBREfaw89nPhdQFwAmtk7CK5AnjPFpHHCnIBYVI965Rm6TMfTtpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روش جدید لب گیری در سریال های خانگی
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/Futball180TV/92393" target="_blank">📅 21:55 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92390">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/stXHlOYRrn1FVgYoXBplEioQGFavSljKp0FC26Zvm_5b5-fVr4_MRn7vthxGJKX92k-0WqXuUWmn6Gu-WnbbbbSnbGIsebwYYhDKISol1ZNmMG4mUAMfGTy4GWqvSrAncuc-4vopR1Cl9f7Hm7PlxIcptIa65vWPB84hFEJFAbTMca664aSdQtoL5V0Yd_G_eNVljVUZS-uRMjMs4sHqk0lJ4gU03THPwqSUdbWCvMVba9hBVq1GI38i8ScgEJsWLNzOGe4AWl3feP5sANHDCxJkAmAAIfkpbKPoGHRKrQt6lIxck_GT2co45ZLLtDog0AH1G4Gz_YzN3vvSqlXDbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/A9_wWDmRoDh7p2vNLEZARbFBe4lFEZGCZmi4cDVPp7QcfxaS7TM8Wuc6eUFWDzFiIVwD8L32OCfh-q5Po4p6Z9hce1AMwGrb_UIw2OPLxwlrnTZckDMKqD9qB31UCoOOk6Wc-ZIUZ8D6iLlncICUIJr6tctLe3On2BXmI8o2QdaPxxwjNm3hDM1PwlHHcLWIrjMTV7HojbTfcWWxvVjrIGTtoKv7YGihV5tEOlYZErNnJveVfGxIgL0DFpY0Bjko5-d7wVIP9_Fkik4vwnpiWOki17tagEoY11ctWfgPt2qzOdfkI8M-0gnbkJ_f3u8m1913DUXoYFZHIl0sEI2O8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KrTECSa6uZUAijXe2HANFSOeW77_bibVTsfQU7fDFDQvpU05uo4gYF5qyaGxJu3Zo8KhXn99amqdaAHnUsTndN0HB5mwbgQjwfecUyHHM-MOHIA0AM4BL1LN_M-lPj7xVhJNPhZHOxIU8fOKdj5ayN2IhQqt6lwlh4Caxs4t338g-epiR7tr80mzfqJ9wVSc42ZCdHhZASOThzse9J1G6RenrLHwsNRRQcMKH-YGuQ4vZ38LFH_T2lnkvtC5vjPCF_-fntjWMSoC2mhu84DHHYeL1ku2K6sq1rJffLHGc9W9VonZ58HBc4SP_SOojtuNx3U-Hd0vPYT2FJ5Aetod5A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔺
فتو‌شوت‌های لئو مسی با کیت آرژانتین برای آخرین جام‌جهانی کریرش؛ البته که قطعا به جذابیت ژنرال قلعه‌نویی نمیرسه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/Futball180TV/92390" target="_blank">📅 21:47 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92389">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60b3801082.mp4?token=jz3RITrqN9422Pc-D_qjPGocTTaDPzFEOjrUwcLGKYf5k2grPyHxWoAuSplkbMXj85uMHq47GnfX92msbk2YB3T9i8TnAzr4e5h3CjNEzDheLKIEwY_mmI7b74HI6y9pOWjK8WpO4GgV_ct4OrNxUMpeM2sE7qjkmPSfkyvQgxMLV3c0vgjH_53vFMfyOfMQukggc3VydsLjqOBCpVZKPOS0XrYQ1oMax7daO4qAbQHZLu4pp5x9OW_bY5oAfC2RiUoOyslo1MX-a9MyObbxFGjC8dgB-DQR4CKOeXfExS83u9kcifQvLfVNXQEfQDf32FzIg4tCZTlhc9OuP3_dng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60b3801082.mp4?token=jz3RITrqN9422Pc-D_qjPGocTTaDPzFEOjrUwcLGKYf5k2grPyHxWoAuSplkbMXj85uMHq47GnfX92msbk2YB3T9i8TnAzr4e5h3CjNEzDheLKIEwY_mmI7b74HI6y9pOWjK8WpO4GgV_ct4OrNxUMpeM2sE7qjkmPSfkyvQgxMLV3c0vgjH_53vFMfyOfMQukggc3VydsLjqOBCpVZKPOS0XrYQ1oMax7daO4qAbQHZLu4pp5x9OW_bY5oAfC2RiUoOyslo1MX-a9MyObbxFGjC8dgB-DQR4CKOeXfExS83u9kcifQvLfVNXQEfQDf32FzIg4tCZTlhc9OuP3_dng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
گوشه‌ای از مراسم افتتاحیه جام جهانی تو کانادا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/Futball180TV/92389" target="_blank">📅 21:34 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92387">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cqNGr-DCuxv4CTDcmIktEUI4HNwd16bIBWd2W-niL8WtOyoVIYM9-3ZW9b1ZuZD0aqYetwaNnWfXvvsbuH-blKrfmMFgD8x2eacTMDj506Wq9_yJWB_1n6r7mLltCRBbAAB0x9VqA0mOQ78zsTjvf1ZURyyIhXjxzA45ielaC4-MWfQaYB9y4KUQrBbcyZ8-xX4tlx9225Kvugbq6A1q-_h7xeJY4WnAIOkBUvWlQp9maY80giRY7zKITmQALT9mQZziIyS73REP8QlrTSGeSYxRKF0oZpGNR8waKO1mDx6oRmmFETqpiCzw-kpkl_B4LhVI2-xEIY8Ir_9BVBCErQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qusQOTYDh5gVGp3Oer-dHPIpSU0BVbu1Cob-uqlkv3O5FUEf8j_uNZKl47X7STAhtjaBxDnQlYBDn-CCOg8ZA5s5tWvAK-ScwBB5vflur4GZ7u82EbOvjfcNgWZY_DZVBBb7xrUt2Ou3FPsjxTo5_rgcsi-uufn1uZ7wWjyyfYLpWTgYQ6dU8PCK6qtfIpEycDQnTnH2Q2CwDbaGrwiIEQQWx58SoU47jwYbt3DHeDfG1IM7xgB7MP4OAh0Qt5zaitV34y34XfLs2ZsXO5wLl6cN_H37m7MCAApKqDGYEGVT3I3SvTZ1D7qNEglagXBsHKKYbYNoP6Qs7xdcBiS78g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">هر شاهکاری (رامین رضاییان) یه کپی بی ارزش هم داره
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/Futball180TV/92387" target="_blank">📅 21:33 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92386">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffaacc1d36.mp4?token=vU88kCLcnZ9QJ0vVOjD3WBfnGRUPAGJ4iUqDNUIUAAvEUx4aK4W6yiQ22tI3Cix3-4Ah_iBeiM7rsDqb5N02mlkh0O5HGA1h-Bs6TJ0aa0XlBzFNMwowDy2MaVV-zbc5NhvME17ui0-4nj8w2_rbVsB2C0mHf8q0n1X9QCB-vlUtBtVn3srugIUes8ocYklE5RkqM62QQC_O61Ig4-ORkRiN_0e9auKlQu3q9k-o0TGw7et44Y8eYsme13QK6azSpNl4LcjXbpm9Zv0mVP3bkJnXsqKRiZkpzenjo7G8P2rs55BMwEShq0t0lJzEPEZ5Lyum4iCRQuUCBDcOi_90tQ60OvSaui56SQKClHzFZUwImvRDOaQqHQSh2As44R1fGGuva0iVFwUyd5EcqEUBHfriRWI1BFE7wANHA0yZzNSJf0J3XYJX1wORNEqNLuu8TSgpDOOD6v-DIomXU_yyZYfE2ZYRzf_yrJ1GsyQgx_0aAuHluPIhjEyNv66up4CS--hwLL3HkICYz_r7lKCXcoQgngkq_AZXaYkmCPogyHO3fM1vRt74Lu5_DHGYhPbI_32yAh7sONdtWfcLvSgLxFWcsIJDksC-XLmaT8UyMxqNS3WJcPpl66uRcGH0WNshGaTd5OYZnXTb3H4d_-iE1r72QjX0uhcEM4ru5zWqQGY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffaacc1d36.mp4?token=vU88kCLcnZ9QJ0vVOjD3WBfnGRUPAGJ4iUqDNUIUAAvEUx4aK4W6yiQ22tI3Cix3-4Ah_iBeiM7rsDqb5N02mlkh0O5HGA1h-Bs6TJ0aa0XlBzFNMwowDy2MaVV-zbc5NhvME17ui0-4nj8w2_rbVsB2C0mHf8q0n1X9QCB-vlUtBtVn3srugIUes8ocYklE5RkqM62QQC_O61Ig4-ORkRiN_0e9auKlQu3q9k-o0TGw7et44Y8eYsme13QK6azSpNl4LcjXbpm9Zv0mVP3bkJnXsqKRiZkpzenjo7G8P2rs55BMwEShq0t0lJzEPEZ5Lyum4iCRQuUCBDcOi_90tQ60OvSaui56SQKClHzFZUwImvRDOaQqHQSh2As44R1fGGuva0iVFwUyd5EcqEUBHfriRWI1BFE7wANHA0yZzNSJf0J3XYJX1wORNEqNLuu8TSgpDOOD6v-DIomXU_yyZYfE2ZYRzf_yrJ1GsyQgx_0aAuHluPIhjEyNv66up4CS--hwLL3HkICYz_r7lKCXcoQgngkq_AZXaYkmCPogyHO3fM1vRt74Lu5_DHGYhPbI_32yAh7sONdtWfcLvSgLxFWcsIJDksC-XLmaT8UyMxqNS3WJcPpl66uRcGH0WNshGaTd5OYZnXTb3H4d_-iE1r72QjX0uhcEM4ru5zWqQGY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آتیش بازی کاناداییا در مراسم افتتاحیه
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/Futball180TV/92386" target="_blank">📅 21:27 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92384">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kNlZGgt42W8t_9KYjBbJL4VBR4v626N5jPKQWleb3FtevUYdf1Sa2hx0N6HdKZ-CgDGjo8exjts466874SJkBLvoTfxt1uAmeRAgdYYqgllcRFBMz03W6lQi8oHzoIVwEmm85xlcWp_fEGDE6X_7MhXzSbsd4tmsLmSdXPG96Dd74_VsthWQq7S-ZHR3oRWcwRLJdFhDuBSMtByAwG_E5BW5XOk--VnIagT2KmCGUFhR819fPff4VS0mJQFQoBUeQOQ4ysR5q1saCtJ5y2dd-SzUMfwCCS2y28-tAd_SHT5u47YTI8awTZO7AvL4ZzloFbqB9ynvOHHGBaN0ga_efQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DdE-kzrJWn593yrTxNecBKU4P2PQkt3vTNklX-OV-inUFC0hbGsOHV-5tbmak4jOSwhHS2_fOk3FXuq54pvlN-WtOYXVaUtrGiObc_L-D072iWFWwLBkf9EC5wwSjCYzZ75V7SjSqZi27lKrsRLm8hGFAtnSqctoWfl2AXLzZd7P9n0uBNuuqiKV-doLJ_mZMJCF1c4yejXEAZ-CAEwT2pImQ5pRnfMaxjSNcEDAXLlyi4IMlQSa0vgtK9FO4tQf_ivPQny6NKw3mLd1SKYF87Hiqcg20T1lfgv2lEQW6Oe-pvAlWJ-pUjPcAeOiQoDmrKf8-1OgSgMGLLQ8b9vw6A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🏆
🇨🇦
🇧🇦
هفته‌ اول‌ مرحله‌ گروهی‌ جام‌ جهانی | ترکیب
کانادا و بوسنی؛ ساعت 22:30
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/Futball180TV/92384" target="_blank">📅 21:14 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92383">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🤖
رایگان پیشبینی کن؛ جایزه ببر
🍸
درسته! کاملاً رایگان می‌تونید برنده بشید؛ فقط با پیش‌بینی بازی‌های فوتبال، بصورت کاملاااااا رایگان میتونید برنده جوایز ما باشید
💸
جوایز هفتگی پیشبینی رایگان
🥇
نفر اول ۱۵ میلیون
🥈
نفر دوم ۱۰ میلیون
🥉
نفر سوم ۵ میلیون
🛫
…</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/Futball180TV/92383" target="_blank">📅 21:14 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92382">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cW0TlncgPG9b9al4ZPyYUf7co44-whJ2ktXMmhW-7s1kGk9OQNelVn_lWIargRNzrbPWxIJvU6BXtJyOv7H-eoaD2Ry3N-p8svDBf8RmM3-4-_0vpmquzsvOivybEJ1cwXdmxoJ07ARs3EGFaB6OZi8g2bU-qBHc9mYSIGkOd713ndaGm9BRsu28VJ_K7WZrp8D1gyHBFG-7o7kZCriFAtZbxKe51cTj3CheRrg-lmkZ9gz8ICFKeXe-cl-cHlziyynzwLHX-mW4KtG1i04zC37_8vcPzxUv6bZ8b5vz_UJHNEoletIvsz64XLblu2N2jghli9MI9IyFZ97QMWDDTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤖
رایگان پیشبینی کن؛ جایزه ببر
🍸
درسته! کاملاً رایگان می‌تونید برنده بشید؛ فقط با پیش‌بینی بازی‌های فوتبال، بصورت کاملاااااا رایگان میتونید برنده جوایز ما باشید
💸
جوایز
هفتگی
پیشبینی رایگان
🥇
نفر اول ۱۵ میلیون
🥈
نفر دوم ۱۰ میلیون
🥉
نفر سوم ۵ میلیون
🛫
نفر چهارم تا هشتم ۲ میلیون میلیون
📈
۵ نفر از اعضا به قید قرعه ۲ میلیون
🏆
فقط پیش‌بینی کن و برنده شو
👇
➡️
@PishWin_Bot
➡️
@PishWin_Bot</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/92382" target="_blank">📅 21:14 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92381">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EH-wbSHZKCQCiQScUO41JSq4u9M5zKr_XmDA7urkN1gA4wu8GTu7yzEMdka9C_zXujwR6-deVNT53tg7qa7uTVkdCHo0uFwE2P-N7_F_roPwl6j_aKosKx1tYLgTrtosswjPbdT8RpYPjyrogjuUuMQ9P4Z4JjF0_GF-9ejmzy4x0mwuouWpVWfQyrZlrvpOQY73fXj9phSGF77X1vSi8l-KmdyVsbdZ_42Jz1GQNEaZ5Uh7sdU8jDHh3L5dYTj_uXYRjWqLKwYF13EVCgowuIEgYff9bM4vHIt7I2QY6GVnVHyKafGoQi9wViYXeyVgEcXefuIchMOIHi-aC7E6qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
فابریزیو رومانو:
فلورنتینو پرز می‌خواهد مودریچ پس از بازنشستگی، زمانی که تصمیم به پایان دادن به دوران حرفه‌ای خود می‌گیرد، نقشی در باشگاه داشته باشد.
این تصمیم در داخل باشگاه قبلاً گرفته شده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/92381" target="_blank">📅 21:02 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92380">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RkascUVudVZiG_UO7M1sy-lEpjeaZXpyCKXdhR7Tu1rhnQ9H9M5giOr7lAY_GIKitdjol4ahXoI1MY8V_I-T1pfiHltiDUvQPBQfU4kxM8yiMlbSWdSn_vMw1isxzGk4dJmyncdegtm79WnUupjERguv-gcjYVdYIZmcF3-spBaEw5hoGKJA7qlbrenhVVRkjBYXpNVOzKsnl0RRJJr8tW6t79WMxw3VzQ-Z_yuwm-ZIBJ7kI3Qlg-RTLKYBEWziJ_PQ3MWrubMpGM9JmlwEdIAgq_mIvP2MseCFYlsMnVNQco-Xx92manFMGu0zl84v6s1YRwOpPruu3NUabkrc8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
جیانی اینفانتینو:
هر وقت جام جهانی 64 تیمی شد ایتالیا هم صعود میکنه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/Futball180TV/92380" target="_blank">📅 20:54 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92379">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ln7vjqTcheh5WMG6GETDNkdsS7ZRbKbYy2xTDzRAfrHmKrarhe1eFjNyYc8Itp2shRO-bo6ZSdaZkV_Be3fsOzihXIQYr4ILo0geQJYHS90rmadZ8FlaStgT48Mx3hhmMONoKSQb1m_sx4uEF6F4m3e3HrU76glBzFuKwgvqA5Vrx97iWYqz2IuELOtJYFz7yFT4eDOjQXF8dQC75Ky5DmO_4DmxkRxlOVL_U7oi2gA5pKlBSSA0Fc3s0hGu4U51pq9shiiUNXQqSRX2jWyjoQCKu7BqpFY7HRXkoQ4-lA0WTjq0Dj99aUkEah8I3hjk3a-HNCOxCsp9ScNzr7zXAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
تلگراف:
منچستر یونایتد نگران احتمال اقدام رئال مادرید برای جذب ماتئوس فرناندز است، در حالی که مربی جدید، ژوزه مورینیو، به او علاقه‌مند است. با این حال، منچستر یونایتد در حال حاضر نزدیک‌ترین تیم به نهایی کردن این قرارداد است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/Futball180TV/92379" target="_blank">📅 20:48 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92377">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f444195b78.mp4?token=cRnnJsh5nPBquZimtMck9kzLYFxn5zJIPoA-apR2IXKARlb43ipTwyLmO7hX4viTZu0AgW3jTR7Hv6S3SPB6qHloOfAv-QIkn8VvMu8M1pJBsgdpWkmpuZPqi-6TT1Mgczk6TX5oAZmq5peqmTUBKcNfDNvsHFE5RWjNSbb3DDPAf6uF8Sf5k_ajaGSIpI_QJl1GU6306VmlGKDR-mgR7IztrVoIdtCZK98ywUQi2o5rBifnb1SjZHNi_1kKpNCEzL9NDDajPsC88zDfwELeJ3yqe795kkb7HDuZk9wZ-58JEnxxL09kKBC7arrCxsC8TR8skeXJzSEAubU0cPPvV5MRJvn9EJ6QGTFC-rLjXzfwMU7qukdByMb0kCrdxecaeH_JABuF8pktrxuZEp4q9FhqKTsGtsgJfj2Ug3yGnTe645bfKPCLoKOfrsbIwqbni38UyDe228Z6CMS9UmDa39qvSCNmqaWT0Kw2KNlZPIy0OgT5MPpwBNwvP56xUV0yhQqOfQ4tXoW4iETfZ_jKJvUwSiROxKzlqMguXkU7tZCQaZWgS8N4thXMQ9HKd7rgk6YX02IBUnL9yY3vuXFgcNv3IEpsULAILDuEvPYHppScEmh-pvxa9JteqEWBrES57GY2NIiUJq2RgahUpAVwkW1u7gQ-g6GuYFjNMRaFaXk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f444195b78.mp4?token=cRnnJsh5nPBquZimtMck9kzLYFxn5zJIPoA-apR2IXKARlb43ipTwyLmO7hX4viTZu0AgW3jTR7Hv6S3SPB6qHloOfAv-QIkn8VvMu8M1pJBsgdpWkmpuZPqi-6TT1Mgczk6TX5oAZmq5peqmTUBKcNfDNvsHFE5RWjNSbb3DDPAf6uF8Sf5k_ajaGSIpI_QJl1GU6306VmlGKDR-mgR7IztrVoIdtCZK98ywUQi2o5rBifnb1SjZHNi_1kKpNCEzL9NDDajPsC88zDfwELeJ3yqe795kkb7HDuZk9wZ-58JEnxxL09kKBC7arrCxsC8TR8skeXJzSEAubU0cPPvV5MRJvn9EJ6QGTFC-rLjXzfwMU7qukdByMb0kCrdxecaeH_JABuF8pktrxuZEp4q9FhqKTsGtsgJfj2Ug3yGnTe645bfKPCLoKOfrsbIwqbni38UyDe228Z6CMS9UmDa39qvSCNmqaWT0Kw2KNlZPIy0OgT5MPpwBNwvP56xUV0yhQqOfQ4tXoW4iETfZ_jKJvUwSiROxKzlqMguXkU7tZCQaZWgS8N4thXMQ9HKd7rgk6YX02IBUnL9yY3vuXFgcNv3IEpsULAILDuEvPYHppScEmh-pvxa9JteqEWBrES57GY2NIiUJq2RgahUpAVwkW1u7gQ-g6GuYFjNMRaFaXk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یکی از خواهران منصوریان به کسی که واسه سوپرایز تولدش هم اومده بود رحم نکرد و کتکش زد
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/Futball180TV/92377" target="_blank">📅 20:42 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92376">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pJdPAiBN5eranipxVIyUEUpekEdV5EY4WWwq6j5L7VD6-HX6ee49gl7wtrFbkqJmxt_ZjtkmOeWn050LgxonmdU2XDPU3TYMUVjH8a9be7KstnFgEiBih6OqB7CMxM1uXWM4vFktJLC4J4XoTfgv6v2iZ7fUwc1pQ1iC0wv0SYMDZGFkDM0bl8hd3tv9VW9Zsr7xudQ2js-DPMn86_67RvJEAYq-YVFj5WW4W9D9_YCFWBNCs-51nCNuS4mezRSwFqbjWJgkY8am9vlOQilzzsFcIPu7nlABotc2TiQW8d9dmFUDaemZ3f3BaJvt6tgj67uo-yn9bVT2hOl-IoVgbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇸🇳
از حضور هواداران سنگال جلوگیری شد و به آنها ویزای ورود به آمریکا داده نشد
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/Futball180TV/92376" target="_blank">📅 20:41 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92375">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qe6Xk1quq-oH0dS2qVQcFQmnX7PHPPzUoJzJ48KX9p3AgsqhlVxy1jNaMC4Dhh7eC2vKYYvm8qQNAJbWbS22CwD_dOsM2BdOMaNaKAXuKi3F_JD811j4jjQxgSV8E97I3MVaTkOLNJItXHDneDyyWhXU1xnmrCPP9BoOvCYQsfS3fqINQbzt-tp2Xboi_DgPT2prwjA09wbVPCmioRFL4K647X_KTobQDPdGgBRJm8dgeCSC_tDGjZkcg4r9wgVXEAbuq5kOliABWvYi63weZkvggSTTXPcq0wljek1VtC6mmvKaM5lFzkRsFjmMXPxgKVwy79ue2iz4EVe43MOt6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🔴
بن جیکوبز:
اتلتیکو قراره مذاکراتش برای جذب کوکوریا از چلسی رو در چند روز آینده استارت بزنه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/Futball180TV/92375" target="_blank">📅 20:38 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92372">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EPcCEBNMt7s4k8WZNTsEeZSPpI2U96Jm_znfpsGTkE-YTzp-Vu4ZevBiISnvURgkBahItF6s6I2kAubif6l1q771jexFYuUnVFnWRHLr-3di0rSBkVcrCHoPaGSTEbqZStvHBAYnQ1K6m2vkyLScwEhXmWIw-69CTRvzGpnDdWU0u2lr_tOMVmngk_aF3esthxzBbTlKYpIfZm1iXJROVwDBt__akzjWmnsU8BBQwvFHYE07YwFqosLdPWblLo0sDuK12_RebK18BYFWX4F1j5QGEwgYiBFkp_i0SPkVr-J2sBjNf6fgVd8NY6uL0L7MiH8HDgfj2Hzjv_mLF3Rqvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CMRAetvNTZY60hZ_dw-7CzvzWuDj4zhOMDUAe_A8XHEn1ASo2WQxCU1_hkshjfMN2Z-fs0urF0jtsyIgAY2hxm3Hn5uJD_bpjJGZznRQqmjcmS5YOcf1_Yf-yLpVNqOMjOzV2kNcG49wb5DI4-VpuzO85PKHddO93dkBi8PYHm53CLQS0ZreX4oSgvvb02OKT8eHjuDHK43UK1S0p9XDcBBmym3m1YP6m9VbeNkGjTIHxg0Yu0sjTEdW3GmAwOMnxvpD9S8tApAhlPP-fjcThEytN3A3ffaf275_-OQ_edkWchRhz3ECiBQw-bxnRVb_K46M3MJon0LUL5kYzqDWLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UpWRBmJEzhhLp7n4fjUL8gT3cLb2DRwJJykyfhMhfo4H_fXXLgG3HjrU-7b-AMfHYbRpTx3McFwjnQpTTuJfE4_6kwvYYGb4EE968cmvBjeWUNEKMGCsR7fmcSWY2e7qfTYp7Bt3hB_e2XQ2brL7ftCBbzFiw_prAZ3eXYO3MAUQ5EK8J-lkrxZVG1X7EtCLcOAuaDuzuURzsnBelSDN_5Zb3zOtt1y2EhhQDSGI51AUiPfss6Cdgczds1Eq0Xs-n88rTb1qiSGn2kpAkDWHvFTg2_CQXSieIFbd00dbHIEUivB2wo4MD8pspospcZKj6bp3JzcDV-d9h2BvYT3iJg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">نکنید آقا
😂
😂
😂
(بازیگرای سریال دبویز هستند)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/92372" target="_blank">📅 20:35 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92371">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GHpuHzjcOdDDF7ZvooGdN0VeygAJxLrfs2KSZBG4etPurkSVLTs1udsR5nsHn7YJLrNZs8PhyohsrmFNuHjs9DWnIPlX8i57Wwqa_DcEEFR1qjuQsuctpy1sE09qmMIe5iLNyWryJh2g8QLHDNaZI-cDozdBgGyeU2X9TG34DYiuHhOvwtd1eK1X8OeFzMmscS1_d7UAazjJdbR6_q1j7CmYQPbAb4isggO9oiBhl4K891YG_gvskfnxfAcO4SEQZq8BA12RTfWZ3Kr6JN3C47qWqmQLmqYB5y4dbbnmCvhvg7Z6JvjXDQqQYN3fVBfpKx8yQuSEvL2ofUFLPtGaRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
توماس پارتی به دلیل اتهامات تجاوز جنسی از ورود به کانادا منع شد.
او بازی افتتاحیه تیمش مقابل پاناما در تورنتو را از دست خواهد داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/92371" target="_blank">📅 20:34 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92367">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z3L7zPqMhL7TwbTxUAws2Fo_Aa7L7CT4fJD6cX77w3IPtQWnrrnbreul6Yty-i-0ZeExv6wp_FDLlDHUs2fwj87QZB0cMWrQYL9aIlACGRj__AyDF9H1FDa6Dk9nXKCIAk6NIeKiwO15Wz_qTOW-LbAX1snpjy1InA_h0tRxm8CidsueOn2GUEfwaY_S_bVT0xU73JMgsYQ_yABUllHroK1Y2gXjYOeeUMJBVCBe44bCc1pfFHj35aB7HWxm_vEiGQCkeonfi-pU-dGk4CfEogEyL0dqE0mQesrwyfohNEj0sUDPtjyxaG6kVUTckMSIC1X2FppkgetoSuJVFHMDpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇨🇦
🇧🇦
وضعیت ورزشگاه محل برگزاری دیدار کانادا و بوسنی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/92367" target="_blank">📅 20:17 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92366">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N2lJMedlrN-sE-sVSU4DUQROPSa84gq8OW3wHrV473iV9kUgFs3tpweRh7IXtGjnPosh70wHxIEFiRBudRg6EClFeVT6CS5z6jiqWX4-cqIakKJ73wdu322QzzwtiL0VCx2O--2gxy0Jxq-iK5H4Zu87XpG5gWZH-4-aE4W696Nbajd8G_rt7irt4eNvGN24Ybr5oKbeOqyBfVOdPqmcuoZE9Nn6IIeM0YjPwX5lMh3lXN5xsU3gA-khMJjPPIkVd27vBmhQpWADjLPe5wLQcR9uK90P24F3tlAAontbCTPFEkLZcqodnQWEb6_mON2fTR-bpJ7o2wCRbl-BQBLOOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇲🇽
خولیان کوئینونس:
برای من گل زدن توی لیگ عربستان سخت از گل زدن توی جام جهانیه.
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/Futball180TV/92366" target="_blank">📅 20:14 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92365">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/Futball180TV/92365" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/92365" target="_blank">📅 20:14 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92364">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gmi2kBOo9dvwh5gL0RtZRFE0XtEPTcMQ29G8USgVHBRFZPgpmtWAiKn6dJsv7PQ0JYCffmUdZbxx4dG_gqb7mlbVT9MSdLABKt1Leq8jzaLdVuE-JAJPr3_FUhwPEcZRZfajRqAod7l_E6fswLWIa_bARwEhhTCapss_f5gVDvMLr8L5emXCR3rOOt_36QUyjWuIqfom5ygAwMLEUmJkEK1WsWHhSJep3QGC-zz0JebMlV1BZwAieRY2mM_7YtIxFCV0VKHX06JNImI_X9jKBPn5lKkUwZtX7FKHpF_ONed2E19ayBMMEe5o9tAITOKbJWqudumHI7Tac2ONu3iMjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جام جهانی ۲۰۲۶ فقط یک تورنمنت نیست؛
جاییه که رویاها ساخته می‌شن، ستاره‌ها متولد می‌شن و تاریخ دوباره نوشته می‌شه…
🌍
⚽️
از نبرد غول‌های فوتبال تا شگفتی تیم‌های کوچک،
دنیا دوباره برای بزرگ‌ترین جشن فوتبال آماده می‌شه
🔥
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/92364" target="_blank">📅 20:14 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92363">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RZgN351z9EywvYB3H2PXNVgCdzo4gwGaTJDmx19mZE4ysxvOPG3EeJKmmw8EN7VbpivaYVtcz7s--EX-S5K4vnmp8JHJoqkMmlJQZIpfx-Dfv44FMUny2hc842A9yGuSHmmGA_h0AiudcDkseWCuV05loLzoa3rUzLJHf986PLpwhVau0rIN_EAe_hEPl_yvNMkX4c8YpbsMeX4VSqeiVZBgSKMkRO82_NX_yPppLkjxl091NuvOTSXHue23ht3uncv9IJ5IFzWWXF8K1gHc5DBIE0hjFP08qAu2p2A0myG8IrFDV_NacRSVOw4Kkw8ZJHIC7RT7Rd8vaDMcymPG0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
سیرو لوپز (خبرنگار نزدیک به باشگاه رئال مادرید
:
🔹
یوونتوس ادواردو کاماوینگا را در اولویت‌های نقل و انتقالات تابستانی خود قرار داده است.
🔹
اسپالتی شدیدا به کاماوینگا علاقه‌مند است و برای پروژه‌اش حساب ویژه ای روی کاماوینگا باز کرده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/92363" target="_blank">📅 20:12 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92362">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z3Ajviyc1fjsKoV9o_HJVHmAepxCiaBnNMgauFktz9TjnsD07krqE3wLoNn6Z3NF6HV_vfnSchb5PRkn06Z_16rLJHqA-syHGEBdbem3JF9oYGn2UIVLWiOJd5Pi_Pq6RDKd9Wl4QzEpqzV9rCDcmgX2VhBQjAdKac2CJ1kt8lMw1fn6_W6y38kSQTYl2PJIIhqxVrpj3KK1TxRyxsZlmz2l0ejyzG3gSERAkZj1ImOWYeBaVssWfP4hJ2GHMWYdm6E3daHFldQL2mikJsVK_clzEe7NAgyb0P3k5UoVsjrizNOvnDZR_knbkVppZlMakEb2JsNc_gp3IEOcinnWVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇭🇷
عکس رسمی تیم‌ملی کرواسی برای جام‌جهانی 2026
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/92362" target="_blank">📅 20:08 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92361">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🇨🇦
هوادارای کانادا کمتر از 3 ساعت مونده به بازی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/Futball180TV/92361" target="_blank">📅 20:06 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92360">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/svkfcgiSj6OSFknB3tr6vkSfmIuGU68LDygx7yWXHQsQoy7VPE7HppAI-3xsJFuOpuIGILIn4ENWaaGCPhOGfoE9rr0zI0SpSIRi2nqDR5vMRoNBwPvS5Opd3ToIH76HtZ8eWwUAnkeoHNFDxMc_xXJmJyhqIlADUUCyKBfmVvbNlWKMIhQmhfjBoje2130jpyQxL3dKyPG8TXNFq4r6e9Pmv9SCmTZ2yzESGCMoNECi4GCmWWX7OKV0h6c0ie4508RV3Zj1ftoAVpONa5KNmbYY4ASc_B7EWDGwisS7aHS3l_OFmEVdmoxksuYSGLnOvsW_9IKIlv3VKHaMLW8VTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
🇪🇸
رودری: اگر ازم بخوان توپ‌طلایی که گرفتم رو‌ تقدیم کنم و در ازاش جام‌جهانی قهرمان بشم، قطعا اینکار انجام میدم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/Futball180TV/92360" target="_blank">📅 20:03 · 22 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
