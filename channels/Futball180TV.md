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
<img src="https://cdn5.telesco.pe/file/tRDeUf4nd-Hd2dQli_4ieI5g3K2y7QIDthao4l0wpJEiRhAPgQmfqD0tQpclN2B8KMteoXTmcIFCWwQ3rYFWJX7kBPaSpOyUIuWt1xLsSkYi6DTpx1W6gLgcJbY5Y314h_tjhRgvrwLW8mdkmYD2gChVXAN0XDwEWnH7NgMQ9HeNCnwwsAw3xWG6f1jBCyCtu37CDRltWicqak5h0aLXisJdgJ-C8jLcOAaOUyd0kYAONl5x354HcM6ejViEfo-jH3w9Wz4Xi8IGvmySLS-aZobiSoomXW_wlsTVkTK8pIvarPN2p7so0LG1kkgZrnAJamWvjI8gTaRJUvlreJ7mXQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 528K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-04 11:00:43</div>
<hr>

<div class="tg-post" id="msg-101973">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KjTmAyITjBqGQ50_WlM1hmLZMDU0oluGOGn4Nva7nJetVUCkZmCQe-ZNUF3lKLSNsWs3J0B6X5GIVU-Qj9kD0s4uoUBPHOYP2ZXg5pm_t4oKMi3Sf1Umuzk4wwrL_9XiFXrJoPOAS1dLZZkDXcPojRJVJzhS1p2uEzrQozQYufgsEGPAjm0g9XYZYrxOyyoAuLZwZ0PlR6uomVMY0NyNd6hLdrr3Bj1onJsHKgTzhY-xXugz7zqxAiaMJYnnaIsOaOxGdkyH6ZbGhxRIj2puXmfbS_pUVSbi04_I8xHyMp5yVmkM3RsCiNGr4SuMWtO2MUXAbpTEHcNOHCsxCF9x6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
‼️
مانوئل نویر:
🔺
هرگز آن لحظه را فراموش نمی‌کنم. مسی بواتنگ رو رد کرد و درست جلوی من گل زد.
🔺
بعد از مسابقه، بواتنگ شوکه شده بود و گواردیولا به او گفت: «احساس گناه نکن، این کاری است که مسی با همه می‌کند.» سپس به ما گفت: «حتی اگر صد سال هم مربیگری کنم، دیگر هرگز مربی بازیکنی مثل او نخواهم شد.»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/Futball180TV/101973" target="_blank">📅 11:02 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101972">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c941f7e49.mp4?token=Las1kMFL2aWkWml6xKSP2Z70HFhJtYmJN9OpMCBjCPrvnS_h1qQHLX78gZvaWCUeB7zoN-5ddTFYH6MXRfOt6geJWZVc7wk0PzlXscQVPRKApgTHZjos5r7waD_4Ba38sial1pIy5LgZoCsJ7mcDHICFRuzGfX0FNqojQ9WHy6nAAD8WctCOPVX0IDlkvEYeqfq-A8V3t0iKoPUUsxJ3AYT0lp6lhEULonKjbW7ORFDlU-G1N9ERRchFJgqXIqP18QkfQqzpeTatrpy1dko_Ux7Z20P4FwrOJsMNDb1VQ0z1hygs1TQbNGBVSBTI4QOiKe6RlzcYtaysotn4BZPgIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c941f7e49.mp4?token=Las1kMFL2aWkWml6xKSP2Z70HFhJtYmJN9OpMCBjCPrvnS_h1qQHLX78gZvaWCUeB7zoN-5ddTFYH6MXRfOt6geJWZVc7wk0PzlXscQVPRKApgTHZjos5r7waD_4Ba38sial1pIy5LgZoCsJ7mcDHICFRuzGfX0FNqojQ9WHy6nAAD8WctCOPVX0IDlkvEYeqfq-A8V3t0iKoPUUsxJ3AYT0lp6lhEULonKjbW7ORFDlU-G1N9ERRchFJgqXIqP18QkfQqzpeTatrpy1dko_Ux7Z20P4FwrOJsMNDb1VQ0z1hygs1TQbNGBVSBTI4QOiKe6RlzcYtaysotn4BZPgIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نیوزلندیا اینطوری از بازیکنای تاتنهام استقبال کردن
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.52K · <a href="https://t.me/Futball180TV/101972" target="_blank">📅 10:54 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101970">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Dk3ZjxUHvNjavd6GhPggt80-vtwP5gX6by-zs-LkGteoKDcm7LDhVtTgE2SGj-Zg7etqKeRVjXMSV7FDgeNabXK0gucnFUzU6cEn9mGSgb25ziiDK_gTiidh-YuZJC9Bbmxwf2yx6u3gK0mBOSXFMJYTuM0Bgtc1qVawEJZz9N-T3M-3BqHZUycWHypLCWUYKEyW04UjeZpOMISTU1edGoriFlsh5qs22F6L5CUmKgIRpbKTfYjPI7Ek9DNaGT7WkthdsNUj3fNDn9cPsgjaZwLCn8e4dIwyagKDq1uIRqgM44ywdfobOu5HJi7bHE-DoZtEv6Um7P8fFv5V_uTkwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/viXOTRu5jdHJnqiGEJQPt9gBFcH1u4d7t1AEIF-C1VIJvfln3x9gUn2_oIaI1frnc8XovIX7GzOQvTr4Pn6e1W6LiutNwt2_7DZrqMnVx1WX0LSRu_omEA7mKDhjGkw1wz8hdnmVZb2T5uMZiRfD5iFDm6qn7re5pcn2w1kIsst8pXcXcyVTqQcaE5kDpUHzVM-2PZ0KCdnIwu536guCApgtZY8-3mnqjwIspPLD1CVR5V_tB_o2u5VwNWYlzO9fkSSSdx8V8XC5mW8JFTqTObtEHCOJRThrh11yS9HjZn3btP90vuOP4Eg_fV2uxCtxQ3qnvloFf1a0uJD6jrxXoA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پدری داره تعطیلاتش رو اینجوری تو اسنپ چت میگذرونه
🤣
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.65K · <a href="https://t.me/Futball180TV/101970" target="_blank">📅 10:40 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101968">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ifSpFeQDi6vyX_7SDenGFukBXcZCUbD7lI5PyXhFPUI9_I1b13ZQxEKAlLgzmTDatqXnn9fTCX3iTQHWCdWzSttreO_gQJhsvqMgRGp_PbxGHEAJU5WMEsXG5LoTyWcTFRFxOCdYTKsqAfINqFsDqZrB4i5MYwZOPbtF0fVwH_UloIrlwIXgIAcz6BCk6YRyNMnYgY9F2qq8-wmgw_g5PYXqkzVDd5Enfuwgme6XEj3MOhb5HJDVRYUCOIWCdm8Wr4N-IP8nyQmB7yECYqKnPed3pONWnHgMRfJcXGgDzp1_kBDFJDJ9KcE44CzL5Gok30RuNigDCqs4V3SoCW_1bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KTPi-38ol_8TAoVc8BKQQf6Mk7VL-C3Rj33Mbzg3YcIv9lbrbHaIBtUuwInSSIndpPBPmDrd6TjZUM6EFmTxphqSll7gDqnZ6z367wW83adDtXx739JwDRa-4PXZ1v_1esOs919SezwyiNFhqDwzREGgylV24Liopstdg1Kr2J2flBSBgA2cmPvM7-tS9GgYH4sXJpGv2Zhn0n88yfOJc1cxHyd-hHhKccip-v9l7kzKKnF7Zgmexc6mQfDsS_MjcbM6ln89rSbsiwAULlinepYoiV3nAs8qxJHE1XETJCxxHrhAxLJ6-3tsf-eTS40wf64BN0eqsjpJUKLvqgpy7Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
😞
میگن نیکولاس پپه بعد کات کردن با اکسش تیانا ترامپ ( پ.ورن استار ) الانم داره با لانا رودز وارد رابطه میشه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.09K · <a href="https://t.me/Futball180TV/101968" target="_blank">📅 10:20 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101967">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cMiCH2TCtkoApRf6gQSDvwbjBO9sIuUa__wLqOZtjPbtW2RnhDFTcpY6bHBk61bo7pShdNMldmKWyjkk_9fp_KDDBqOGC9kYKt4twI1ypZUX2SWTsN3ZgPG_QLLerVHmtgL65USiWnaEGhvYU6srCK8qaCpTYl6SETuYwzXauCCSvuXgedSrEtRdrMFuaJ-LbMfXuf294Nav20pI_ZopvK0peTfYJoM5uOwZivCZrs0hnPj19DWGwebTk9DF7B3n_GRtV6bRkHjr1FvrSd8Y4MuqEYcRI_f9WwmXq4u4z39t3j5Rbk4ekYjHv0mgoZByNcIFSqUm5QCfsoBBmOo9fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
موندودپورتیوو:
اگر بارسلونا نتواند خولیان آلوارز را جذب کند، دیگر هیچ مهاجم نوکی هم نخواهد خرید. بعد از جذب آنتونی گوردون و کریم آدیمی، مدیران باشگاه احساس نمیکنند نیازی فوری به خرید مهاجم داشته باشند و معتقدند فصل آینده فران تورس، دنی اولمو و رافینیا هم می‌توانند در نوک خط حمله بازی کنند.
❌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.92K · <a href="https://t.me/Futball180TV/101967" target="_blank">📅 10:02 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101966">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MaauBu-VB59IrA-yODnrgRgj6hWtTvJF8TEGwSNBwcblLHlI1h65pjD147liXmVumIf6ViLyEE2xYj9GArwFZRcaQ1ATUC8SxtjEq802zOJiWX5LkE9JDDqcT1FO5opsLO4t42-cSH2-tMWkVOKTwOdo4uuM7o_kmg_ICavHpDbhMx3tVTpL3o7t7bq4GXrcdR31Y4eq3ueBN6WdYgxawXphwrB82p6eYFEH2wokcYKhkBIm1WWmarnc4zqQrTzW0aLyfnZpDEx-6KtQoRJk-g83wkeCoau9BKqQMiXrisRvZ36hoA-WbIFRP3KFSXfqYaEeIHTJNVyHrDFia0K62g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇮🇹
–
فابریزو رومانو:
⚪️
در ساعات آینده، باشگاه رئال مادرید یک پیشنهاد جدید به باشگاه لایپزیگ برای جذب دیومانده ارسال خواهد کرد.
🔻
این پیشنهاد از 100 میلیون یورو بیشتر خواهد بود!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.93K · <a href="https://t.me/Futball180TV/101966" target="_blank">📅 09:58 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101964">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RBapGYXbH3I-dsqEOi_9zGQZk_AIgjOeJB_Q9nTqE27BEwbUinwigQixw6dJPdEpmS46jFTrVPa5RSzovmX3pxZxUiO5R6MeBNC-WGmmFxBMAZjccF9n6fnLP66GanDJgdnF7H5Sqw8x0TG69_TUr_2cv03v6NjOrM_CzUWWpb6ly1lWQXrdwIpExv-QuvNc6uMK6KutyZIHXDNcA2WYpebJhwb8WCKUpqQA92R1oAmUSFnBwfHAOfQoijiUML-dUdCB5T2kuLtBWKK5bydB_EmP_zlqJAbNrFCYC3TL-0oMyzkLiA0Hj8_kslb-D8oqUVGtIrTv5VS0bVNHWFWeIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DZq5ss6RAvY8I878NDcSzXh4prlVzZRQw_Yf4nWqomCobrSoGqY_CxsrpE9QOs0hjci50XMp5zyVJ9-iWHrPQXKrUywrL8V70YKDEmCo-vaaNAxP1DuJQk9_OZBand6HxiMT474TD7Y8J1A1QN7CijJAR-civhKtugene-VxUC1Tj7RjK4xoYZtzZN-1aNa4fO8zivDGs5ERhJ85NeGmh3p6vak45ewUcscfauR6MqbhrRivIO0VkM8uwRr10yN4eEjYPvRUSBYhP_s0mNn11PxhLoOMzVHBe1kXTG4aEcLNAgaJzcAvI9tgaa3iRGFpty0LYQ0SQ5BLl0qc9pPclA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎙
سوفیا رین شایعه‌ای مبنی بر اینکه حاضره شبی رو با کیلیان امباپه، آقای گل جام جهانی، بگذرونه رد کرد: من هیچ‌وقت با امباپه شب رو نمی‌گذرونم. هنوز باکره‌ام و خودم رو برای همسر آینده‌ام نگه داشته‌ام!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.97K · <a href="https://t.me/Futball180TV/101964" target="_blank">📅 09:40 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101963">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G7DDqU2xJxNjGS0c2jA80ItM7_CuJ84JDM98rwwhMRkZA_MKjzqtxLI9WLyoQYb78lEtUP7VhvLxHSNV12mwVNU2m1ggs-hjoR9rmFNZNMp56gK_AIt7vbG-r8WrRvmnIwXSQr1PJ2GNOIV5d_8ji-0pJVciqzcdGqKb7jEqKU99bJuEC7WZUP6MXGTzSRrt9Pmzgg8LbSbvk5svlbwMO_jTJFp5bXCQfrVAMLbbHBERPTJa8QyyZNnuxTv1reXJ6vd7tUxBVlOye_jy-6a6i3udDKDbEXIdKQiOnyFLrNrQEDhlUQsf5lvoyQJmrOjOWtiuXDo0kB-6ZXJ0JZjKSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
رونالدوی برزیلی درباره کریستیانو رونالدو:
فکر میکنم بازیکن‌های خیلی کمی مثل او از بدنشان مراقبت می‌کنند و این‌قدر اشتیاق پیشرفت دارند. من تمرین میکردم چون مجبور بودم، اما او تمرین میکند چون عاشقش است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.23K · <a href="https://t.me/Futball180TV/101963" target="_blank">📅 09:26 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101962">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f0d0985c7.mp4?token=oH2kDm212imOZF9d5dz6ZyssFTHAkHdSmmcK306XCnudY8DIy7zupr-yXn9RJZvAX8-JsHx2fAOVwj_dqoTYxUyIAlLgzAX49aJUpF_ZcWnw9azTi-JPG_BNrL-Z-z6QgF1_zNs2mal99KjnXN3DMXJZ_Msl6LfmcRXHqMcxaG7y2-hpTra_mJjzCIM7N0RW2tdd94m_DToKOvR_fHTG3DRsMIdog00qXBZsikW1vG6XzlX7aWBlSI-MOx8FTX9OFEz_bbkgn-kVk5GS4ikPpqRM27eG3OIm6xCXUddlrlVUykL2zrYy9dykeAO_eWBaElKGgBofOp9hraPXVkSDPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f0d0985c7.mp4?token=oH2kDm212imOZF9d5dz6ZyssFTHAkHdSmmcK306XCnudY8DIy7zupr-yXn9RJZvAX8-JsHx2fAOVwj_dqoTYxUyIAlLgzAX49aJUpF_ZcWnw9azTi-JPG_BNrL-Z-z6QgF1_zNs2mal99KjnXN3DMXJZ_Msl6LfmcRXHqMcxaG7y2-hpTra_mJjzCIM7N0RW2tdd94m_DToKOvR_fHTG3DRsMIdog00qXBZsikW1vG6XzlX7aWBlSI-MOx8FTX9OFEz_bbkgn-kVk5GS4ikPpqRM27eG3OIm6xCXUddlrlVUykL2zrYy9dykeAO_eWBaElKGgBofOp9hraPXVkSDPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
⚡️
بخشی از گفتگوی جذاب بکهام، زیدان و زلاتان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.71K · <a href="https://t.me/Futball180TV/101962" target="_blank">📅 09:01 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101960">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tyU3KIie7xPDL-jrw5kb5oDplwi2TpRgnJNJ9WUIckTsgsTz0Il07L6vMB6VpzRsVYbpZh069iCtc9v_u6Zu-c5vvH9Ij3vqfLnLMDEBdgqr67-MwsaW9c1gpyDbgc1GnrTcQ4b2XE3zJ9NiectDZdQHk2AV-I8TYQE6vejgB8B9_vQjNLiR_E9ebZWwECAIY9FoNJE83o08XPZC0tDo3q9kaJcBRvjkwVWbsubWcus362wm9C4Qas5WOD_0h-0lsVrGOQXSKeJNCXEH-VlSmKPW58IKRkBl75FT7QLyvLv-R_PP5jFihlRaz3Ra32hbOvPaU2EDE7PTmlzR6ub83w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WzCp1Ch7sRMiuvGlPj32fUL75U5uD8t9UW_1ZPRNI40SFYJGBONhiKvsyFABe0RslF_zGW4WDHrrhdBHwzrDtXaYEL9r3KNpHFZEMtI6iTI0yktjFylmMMGxaVatf0NonY61zwkK6XfZk0iZpg8XUd_lq_yo17WUwhclKWGTDBHq-4XkIcxPe2ZkRnea51FAj5mdk-jB63eELXKEUGn0kT3Ax3-ruGK87ZwWMBdZTc7WlBYhl-5eSE0EvzM9xDM-wgZFXxmJc-M81cK16VJJG2n_5XJNPzHIMgFClcyRDumCuC754DDEo_cThi_KwEer1U4n_2EzVB-qLrkJgG_rjg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">کریستیانو و جورجینا قراره ۱ آگوست با هم ازدواج کنن بالاخره. تبریک به این دو نوگل دیرشکفته.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/101960" target="_blank">📅 07:32 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101959">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YETGVfDKMHUbLeD6v14pkrLVol1ZwRM6s53daTHLdyv8hZkkxdx3ZFQ3UaLU9ERDTlkOuO4Qzd6keQ9iuOJ_9M-EYADdyOmAOde7H2glE3ITsYGUYPGAyAoEoWNSgzLyVI12vINl54L1qfaXuEgrD2tsOpsSzajl0eZgFLl4y-Ts-bF0-bOfsmOjQyXLLSGZSNcPdTWv07Pg38xmgq6zbGOhhuoLLHjGw8trKZ0TggTSfUXdaBCzqBw8yyNlLZla2ZR1B7pMnPShNnapljJggopPRZ8tlX3xxT8QFRx__xsXn9sPLaejW4wb_ZyPUHAHxxSzEO-EojxT8O52dCMWCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👑
موندو:
تعجب نکنید ولی احتمالش زیاده که لاپورتا پرونده نقل و انتقالات بارسلونا رو بدون جذب مهاجم ببنده
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/101959" target="_blank">📅 06:56 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101958">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85d2fa751b.mp4?token=hvHeS5-YhcZXmGeUtSoTOq_54kv4S0hW7DfKURIrSIIRgH0OJTwvRisewzjeQ7nyYs_E8ZOgjWskYSZ_P9ZMdXPzh-W_1-BeZYde4pUPLkdaH-9hI3Z_kJ_Oo7P8-6j4UkemzHVsychLVogV2mvBklwrPjhOx7ezOlXVEKfroj28xjBNJR9ObFozsHx-SCUaTGEZ7tffKy3oLKOF9hJhH3-IeRZZ_gySa0ZYcRgjyNdVWSc80dwgqU-7pTrd-1E--32j_sEPuYUKvdDkLfBvIASOlZx9vt-Tm55MHLFq7-X0m58n6Fwh6lum8iG7C9mq7ltC7oy-trHiq8eCMS9BuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85d2fa751b.mp4?token=hvHeS5-YhcZXmGeUtSoTOq_54kv4S0hW7DfKURIrSIIRgH0OJTwvRisewzjeQ7nyYs_E8ZOgjWskYSZ_P9ZMdXPzh-W_1-BeZYde4pUPLkdaH-9hI3Z_kJ_Oo7P8-6j4UkemzHVsychLVogV2mvBklwrPjhOx7ezOlXVEKfroj28xjBNJR9ObFozsHx-SCUaTGEZ7tffKy3oLKOF9hJhH3-IeRZZ_gySa0ZYcRgjyNdVWSc80dwgqU-7pTrd-1E--32j_sEPuYUKvdDkLfBvIASOlZx9vt-Tm55MHLFq7-X0m58n6Fwh6lum8iG7C9mq7ltC7oy-trHiq8eCMS9BuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
🔥
نیمار تو اولین بازیش بعد از جام‌جهانی با دبلش کون سانتوس رو مجددا نجات داد و با نمره 9.4 بهترین بازیکن زمین شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/101958" target="_blank">📅 06:36 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101955">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sXWVcXEb78TGA7H7S_jc5_A6l1yM0gLFGLQC3qz89WbaQE0AqjZ7pxR_F8iU6mCOB-0QE4h-_Tw4D0_GXVp04LohVHTCG3BwTXmA0AFXmZ5ujUSAeXZtfDME87sANrAYl0MwMjGZaaVLLVj9MCctdEBo82pVgWO-xF-B4eyaYbPGEz58keZg3uhW2otqzh1yDQJfhsyn_3eBD2_hfbIF8U68KLcg7cy3q1mPV9eokvejZN9OHk6EWALfE8Ian2NYQSqTuYe0UGZr3EukwNofU1kAjdGyFcNSbpLB36k0rxp-FtfV0yNXt8uZ1RxlDGJZUJJBapcusS2EC3zdmmGXkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gx_oDIsBQt9_u8qwqTSITnGqCctAlQ8-nI-YnlRPaahp6cHRLOddhOZKmerM7MFcf7uFZ_QixPK0xEpQ9ZdfRnYjnk-Yan_huy0Aod1HN4y1AJOb7Qrv7_YZ3OHJmxhBydMyugm5nwiLNMoEyPVqXyF7pbAwEbDwqX9SugmLoAdNP3nORvo_quD783vwLMZeN4HDJ0FKfIdRBOK1JQlW0qnU4LaupkcvbB4bVPY94e4N9QF3HFyyTMyq8NTnunk49Y7yPodyNnd0stnrzdOlU17HIJU97uqOceVxsI_YBWCZ44wUZtFQm9kfBNaQ8wyHCFH-tHnEhFXTSauFpZcMXA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/953a60dfac.mp4?token=Q-leYCd1fSawmTRGJRKoWlwtIgxy8A3KdxMf557yFRVly_He8y4rrQkTSatxUXMr9lBxrtmciPI_uloAhbl3h-euo7N_oiHJKaBpGs-v4TtfMs4G1P__q1quJX5gzm-LiEHFnrdHRna_KRaoY9ZSJLRNj2j1AwXis31np5xSIVFpDehwjOHPXt3_qa_r8dgO2HZoIxA1R1ptLe7QlatcApwlvKl_0xsrDi_1KuWiJ9n_brFZInKkOAL3xC7FQ8zDt1LkGFo9vg9i4S-dR6tdKhKbACZhcsPhQ31i_5HRckRphCBeUy0Se4rQbOkNdRv7v1ejwiLtgtGvvdH9yABuqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/953a60dfac.mp4?token=Q-leYCd1fSawmTRGJRKoWlwtIgxy8A3KdxMf557yFRVly_He8y4rrQkTSatxUXMr9lBxrtmciPI_uloAhbl3h-euo7N_oiHJKaBpGs-v4TtfMs4G1P__q1quJX5gzm-LiEHFnrdHRna_KRaoY9ZSJLRNj2j1AwXis31np5xSIVFpDehwjOHPXt3_qa_r8dgO2HZoIxA1R1ptLe7QlatcApwlvKl_0xsrDi_1KuWiJ9n_brFZInKkOAL3xC7FQ8zDt1LkGFo9vg9i4S-dR6tdKhKbACZhcsPhQ31i_5HRckRphCBeUy0Se4rQbOkNdRv7v1ejwiLtgtGvvdH9yABuqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
🔥
نیمار تو اولین بازیش بعد از جام‌جهانی با دبلش کون سانتوس رو مجددا نجات داد و با نمره 9.4 بهترین بازیکن زمین شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/101955" target="_blank">📅 06:23 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101954">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HMhu3IvJZ6TL2vLgS6xdQGJVR-o5qYkrtYPsCz9K-Qwqkk7CNQloQpuY_7c68xYMZLuGVgFAFmhyppp_D8lNvYWrU_xY0B2DZA3jgVWHAIAw8yVoQXgdnd7bvfJKSZ-fsyeQdyzdNYuG0VCzNxYUvQ8KX-Tf223amYE9gf0t3dmm1IzCjuM_2-TZEbkSmQbQwPrXnXFi2v3qlbPEDYlDPdYCXfSNu_A5skOTPgec-gfTwrlhnjuXVB9WfJjZTx7xuB8QRDkUE34RJ1E5bmuQMHvoAbg2TiHJjFCvlFs_T1wqj6yquZtv5rQk-OAh2ffj8g6jzMAMT1FwAsf-AAAwyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
مسی امروز اینجوری تو روزاریو شکار شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/101954" target="_blank">📅 01:41 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101953">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44643cb150.mp4?token=SpQoi2w9TpKb-pSuqkyb9CEJ-3LpC2dZg6-sH11m6vwW6IvXKp2YmC3jo_2RmioeMyndh9dLxJleaGj2Sn90KRF8UTDbjmicXRuinFDl6xtyRh9ydpo9r8uc2TpH04H5unqBzGbfkI5TWO_LdJaCoyw_M-wGYP39cun4sfq_KHnQjmF3lnqrwdV86B-diC9BsBAe_Iwjf6M7Wj54Lwm-e1hmoKBDI2gYaADtJaI1qy1xWws6OIeTF4wmt7o18bRzz0BsPU_QlES9rNbSSvK8Nw9QG67RBxLVc1HdwwdLsOmW_GVwySv9UV_AbGS8tCeibe_eyXT7VUARGse78zyu31rwu6K38vJ3loaDD8eyK2QWerOnDdmWPVSvc6w7tCihVOtzOGmh-8dskW1Qevw3lCXGbAITTO28hS1VncLYwDabyIlDcBp5lvrrvUMw0w-_D7MFboSQfjvqKT9uxzH0BGDbzQ5G-rNaFtV85ds68tiKOQdGVazm5yhD_8shp6HyrJLeWpPn-7UYP7mbARKKlniQIipjJsYCAjpDnk37_9K_srbMxJlKsD__RU7ahNI1bfsdlgRcYf-aPZReq3j61IujOvwO90vhvRFFX62_z1b_VauIBUbOtjjopH_jZOW7L9qt46rj-YPbNK_5lYgKZqM-l_IAk_f62zM2B8JcmF0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44643cb150.mp4?token=SpQoi2w9TpKb-pSuqkyb9CEJ-3LpC2dZg6-sH11m6vwW6IvXKp2YmC3jo_2RmioeMyndh9dLxJleaGj2Sn90KRF8UTDbjmicXRuinFDl6xtyRh9ydpo9r8uc2TpH04H5unqBzGbfkI5TWO_LdJaCoyw_M-wGYP39cun4sfq_KHnQjmF3lnqrwdV86B-diC9BsBAe_Iwjf6M7Wj54Lwm-e1hmoKBDI2gYaADtJaI1qy1xWws6OIeTF4wmt7o18bRzz0BsPU_QlES9rNbSSvK8Nw9QG67RBxLVc1HdwwdLsOmW_GVwySv9UV_AbGS8tCeibe_eyXT7VUARGse78zyu31rwu6K38vJ3loaDD8eyK2QWerOnDdmWPVSvc6w7tCihVOtzOGmh-8dskW1Qevw3lCXGbAITTO28hS1VncLYwDabyIlDcBp5lvrrvUMw0w-_D7MFboSQfjvqKT9uxzH0BGDbzQ5G-rNaFtV85ds68tiKOQdGVazm5yhD_8shp6HyrJLeWpPn-7UYP7mbARKKlniQIipjJsYCAjpDnk37_9K_srbMxJlKsD__RU7ahNI1bfsdlgRcYf-aPZReq3j61IujOvwO90vhvRFFX62_z1b_VauIBUbOtjjopH_jZOW7L9qt46rj-YPbNK_5lYgKZqM-l_IAk_f62zM2B8JcmF0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
لوکاس هرناندز: «کیلیان، اگه قرار بود یه تتو بزنی، چی انتخاب می‌کردی؟
🔺
کیلیان امباپه:
فکر نمیکنم هیچ‌وقت تتو بزنم. دوست دارم مردم من رو به خاطر کاری که توی زمین انجام دادم به یاد بیارن، نه به خاطر تتوهایی که روی بدنم دارم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/101953" target="_blank">📅 01:19 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101952">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eRXZmpqtEDS3ZloMdGXANJh29Yvtuvu2Nb6Tybr_sDS-MFRqLfcs_Lqhb4EcGxaZLcnxZrkI8kVeaCFsLCaMTdep8FX4UckN3bmDMznDOlYw2WD-U1paK_JT5qVLkYHSj9YOq7PUkbrGtRB5oELO62hVm3YwNLjkCn-AtBrE_M_e1Tyx6kXng26USr9AaZlIymKOWam2Br0IOsUOAyjZmomerKfX3mEIYGp67oXsNFZi2bd_ks8Se--6Avt5spbHqyjglWoFJ7gYTFE6xa4FVQ-A0ly5FlTl2wsksBcZ--yg5bRRpnw75lfdi8ctthPP5L2zcIejY3rHKkGVMnpwPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
امباپه و پارتنرش بانو اکسپوزیتو‌.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/101952" target="_blank">📅 00:58 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101951">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KmyADtsAfEsQvxnbT0eEj5LxhHoLzslbggAPq-3fecjNEeQaXKdzQLSgZiGLBSO744z8f7edyu9KcKa6wGtyAvCpPjX8JP8XlK8_YpRqFK56ac5oKQLRPxS33r8EBvRDY53hYeSYMTI45z0pBe7toLs8etXCoYmoTcz5Otruw0pelNIrWvGKpEqdyE57NzdcPp7EBq7SVx9YETX1LqBiigMINLGhdvweJW_MYHagOye7c3c897pdNZtgODPSnX-qFP2Tt2HiFc1ADI-dw9h103BL6dg5g78P56Qc7vxSsgUmTV-MAnMoznuvQJewNutWNfAW9ti4vN1xIFOdGtqQKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وینی خوشتیپ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/101951" target="_blank">📅 00:51 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101950">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63dd42dc4d.mp4?token=Z4p0SpqqzCIxtsyXxypOVel9BjDLJ5u3PlIWD7JhNGEtUo-3q-6FIUAmqheGyS3GLBrYo6ehYovPntsTwW6oIYqKjnZVVaMK5KdMQ-YphE669SdgAFNEpw2zo6LuNbWc2fjXVjdO_NLndM_s_Lj8WAoGNjKk_vEYeesIzcPvHkI1vgZKUjD8u6F7vWCo7W8yEZM0XUWcjstGwGqwnFdypgoHhCl6HnBJIjN1NpDyCbGDyRI8l-8G8ANTVQ1D4SnTEsfngB2sW_8kkrYjNXQufL0y5IgR9_yyo_v9GU5WTvsjhx40HkB3DVwr17Hxyg9hZ_NLFnZx8VwkQoBjFACGiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63dd42dc4d.mp4?token=Z4p0SpqqzCIxtsyXxypOVel9BjDLJ5u3PlIWD7JhNGEtUo-3q-6FIUAmqheGyS3GLBrYo6ehYovPntsTwW6oIYqKjnZVVaMK5KdMQ-YphE669SdgAFNEpw2zo6LuNbWc2fjXVjdO_NLndM_s_Lj8WAoGNjKk_vEYeesIzcPvHkI1vgZKUjD8u6F7vWCo7W8yEZM0XUWcjstGwGqwnFdypgoHhCl6HnBJIjN1NpDyCbGDyRI8l-8G8ANTVQ1D4SnTEsfngB2sW_8kkrYjNXQufL0y5IgR9_yyo_v9GU5WTvsjhx40HkB3DVwr17Hxyg9hZ_NLFnZx8VwkQoBjFACGiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ری‌اکشن هالند به میم هایی که ازش ساختن.
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/101950" target="_blank">📅 00:06 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101949">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k8PqW72NY3VBer5XpgINkS0OGIqKSIoVrUYgAECOsGaofGMaSctMjYjadGlgLHaZJ-azmk7zigGzX9seVN0eUodJwhBd_SjyXUr2Ldr890VEK4JtquI8KFedTlj0onWTph8IkGHmSNor_iF_FPSoQ-HyminnVbGrHB_LhGXJaQBxUci7A5UZuO6ts2MBstCLGuZLavJJngHDkNbQyGSh8nPfU99pfACBonz3Ej33K8uzOjMgHo4qXDgzE5HsGtCoEVnSXtixVNwSAYuRNI8aoZpF8tQehl4AUz4-51DopWVIS8MUghsq12KtBpiY_FEtjzhVAq6kE-J8zqL3SR_n9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
فابریزیو رومانو: رئال مادرید و دیومانده بر سر قرارداد 5 ساله تا سال 2031 به توافق رسیدن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/101949" target="_blank">📅 23:59 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101948">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Iase3SUsnKF9pZK9CAR4mKw_WjXGXUqZfqs4NgEtpIga0eNdR-E7hRC2icmNbIhijB0sOZ6owOb1J9tkdSse_fQeIpIMIhAxCnS-nAAvVUSVAJCPoUmUtFmC-hVP78U9TanAMoFFzRHL5STJH5KzQX-QiWJeNww-M8yTyaJUP84DcFbR7bbwu9-KPfCx1OmQhu2KJK1oMtdjahrBRmLf5iuVfIiSVBRjTxlnjMngd73Ly89VTkQWdRhhy52Q8o1m1sHANTUK-Muf4Av9ONVtRNaVmwz7LkHsmPi-exwU5QeQGACMyuLUBrmKd9lXp7HrrOqRD_PZUI4_7Au03taVWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔹
ساشا تاوليری: باشگاه الهلال میخواد مبلغی در حدود 120 الی 150 میلیون دلار برای جذب لوئیز دیاز هزینه کنه! اونا بودجه 350 میلیون دلاری برای نقل و انتقالات کنار گذاشتن و این تازه آغاز کار اوناست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/101948" target="_blank">📅 23:37 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101946">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fj2jLjQTB8BAbMknf3BnvQ1HwnN4wFmcVTz7FQHvfszlArE0fE0O4MyETzoRCRbFoyV7lS4ScDv2XezmAXNYkByTmjo_OxCmpN6R8WxWV1VnCwG8IW9m_A8B0Zp3wvVld_btEpE8ovtbznRErSvLXZUzCoor0BQJvec1ytAs1_pH71ZMGakOnydz7YPNtpsjuyqkpp_9PDclBYiTRp_yiG_LEcgAiXfGXuMCm0M_MyHmVEQacrKheFD3VW3LKp9TQfEJmNMaRifISpZxcdA2HtbL13W2U-Cq72pVERMVqd2-jemfx3Q_xtj1j-WWxSaRrVusNBTE5GKEAuLvvjnBjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GIKUiVkg-nBAtrOrl-xkkim1iYVli_jEg1CDqO4P2cFe8ion9jZJPGK0xCUYE_q94EgWMvlsBY6TBVv1mefWDVetYhK2OI8EnflmyrM2bAlSPZBzeCWI6uirS5xSD64vefwA68u-SIApCg_FBcc6oxA2skDAwJuWCnCZ8N6hfEP53Ewp0WHz61MioOE6gRA3puQ9hTWt-gD3rlMOHoe7z9sPJiL18uPjIYoMFEriaxPLsmW9lZc4TuUen9RnnMfQEx4RPWdoSOr9-98uGBLiuu_M2m6PPfDfiLByLz9o73AbToGAC4djfrlWsi77K4FEcStz0UYL2UF2GgE5jfXsHg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎙
سرخیو راموس درباره اینکه بین کریستیانو رونالدو و لیونل مسی کدام را انتخاب میکند:
برای من جواب این بحث خیلی ساده است؛ اگر فردا فینال داشته باشم و فقط بتوانم یکی را انتخاب کنم، کریستیانو رونالدو را برمی‌دارم. مسی لحظات جادویی خلق میکند که کمتر کسی قادر به انجامش است، اما کریستیانو این حس را به تو می‌دهد که فرقی نمیکند بازی چطور پیش برود، بالاخره راهی برای بردن پیدا میکند. چیزی که بیشتر از همه تحسینش می‌کنم همین است. استعداد یک چیز است، اما در اوج فشار درخشیدن چیز دیگری. وقتی کریستیانو در تیم تو باشد، همه تا سوت آخر به برد ایمان دارند، چون او بارها این را ثابت کرده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/101946" target="_blank">📅 23:31 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101945">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OdSRXUeHFLHfSm42UAeEfXi_pixIRQz_HiVBja2x4g5QIpCTZsGNKPTQteS92dn3M8-ijQVKOS5GUj3Ov--X6lmzxCaInOmQzyVqMvcgoG1KjN75iXjyP556qlIVZl-p8IHKionGTX4mr-V2wu-IvOPtZSyCWwu0-NXnhW4Wf1Cjaejb4aTfeO-IXoaAy8iWUKJNg-mmn93hspcb-8RSGl_gBFMc0s-u8Nj5xLwvXYoHJA9uRgdcrVRav2R9VZBIaRlC5_IaHUE1eEMrmytSnU9sqPyMg9PMZjk4UrZAJb7WpzMKrqyhGlN49maj0vY9gin2fQqjy77oQMmK0C3I7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
به نقل از فابریس هاوکینز:
مایکل اولیسه تمایل دارد به رئال مادرید بپیوندد، اما بایرن مونیخ درخواست او را رد کرده است. رئال مادرید تمایلی به درگیری با بایرن ندارد، زیرا رابطه بسیار خوبی بین این دو باشگاه وجود دارد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/101945" target="_blank">📅 23:20 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101944">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kMEzxtJKITcaoaUwMjtBOl91qyEV_w_RPAnZacKMQcpQa0pyq2-021JnB9iu3c0p8HWLp_nZ0hzwleGY2GsfEF8gU91BufcG2MOT6PiwEElVLFrQ0Ta5OrFWD6Iol2w7fa5l0sMRS0OFqlIOsOh2qHCHtsxSB2FV8A8_6X_wwX8wbhyYlbnztcH5rbKghDJfIn_R5B4BvjN_hyo3MH29MncWYSae8cBLExORG2tgs6axQIaYxpQih12x8FAUBSMQUgMLwyxUiG7xFHviQF92g16Z3GLwdFBlSB5tU3gohpyL4k9GZXLYTJ9I0bMo7R9-EVKmeOdXfXxV6NQIL0b8QA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
فابریزیو رومانو: رئال مادرید و دیومانده بر سر قرارداد 5 ساله تا سال 2031 به توافق رسیدن
.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/101944" target="_blank">📅 22:53 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101943">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rFLvfnMp_ZzSb-ksco28JdTzobhN1Qm_Uw2qBUCO1u9LqwvTYMRjRGClGHZW1hw4LrxJFZcoE_pv0TV7D9y3vuI6ZAQIGt9yjmt3qBWVWrEy1TeOPF_IoGk2-vQk2bqmVnYdya1PWTVo10EaBTjVKgKN1ObpZvEfzFHBPmVAtnFqCD5PM8_GswFfkColsx56ZWtqs8QvurnHF7XoqydNcPk4MiRGtltFFLFGNXOoW8_zyJwpLBDMKyDS2j_ti1pB2V9giVlV713Le7KmYKM60lVhnEyIdJILSAJ1qOTjXLtusMF5hPiTE4O3p1qPFY_pGwB3UtSvpleJVswW18dcbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
فابریزیو رومانو:
رئال مادرید و یان دیومانده به‌ صورت رسمی بر سر شرایط شخصی قرارداد به توافق رسیدند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/101943" target="_blank">📅 22:42 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101942">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qxl-Nd2vb8Ya9fphejAUbJIRRWnlcyemCHtQ1mvAsvvo55Mj_gIMvouIortVMLuDh5V8Ui4aOVjeD7YAOJEJYvBRU7TJe1UdKQW6LPxmOBZ0MsMjw3oCJhcf-DujOaxWO7MZ1NT6VbJyuW-GWpzSMuyUqpDVFgC7-iy2TUqN2aeQhwZzCJuAG57wnvy-E46oB2cDN270z-OPQ2it3AoY7Tuorbp17nAvJZ4OdOdZSbFvLv9CqNFAHtTuqfLtHR_SnFC6fgBtWjCTJmoGyKTi11G2P5Gfh6KXWjpW46173K6hegdyeCCWnFNaTyDnjL4coNwM6XObjT2Zq74Q5-_clw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
👀
ترکیب احتمالی رئال مادرید برای فصل بعد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/101942" target="_blank">📅 22:32 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101941">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vBn0SEq9Ptw84nduwkMrmcuqjfw8nOtcsxM_O3k6qMRzBkzt2q1ffntA1ahxVuUTFRCoANdEz0yw2FURDdRQppDzi-LiRlMg6k3NCYFau5FPIUvd7Zn-C71fT9sgCrExnv7rO-XFzoeL2XHc1JxytWh3mga9OLXSz2-x0reuJuSMW55ar_r0PyVH7fCtc3nOlasHIKfF7MZGQaNGrTgQdGzFxt5V7CifiVf6k5HVvWitSiNupIobtNN4JjjNQOOly8YXGEh6Fj4B85e4TBX-GyJhzNFIPSVREi0YKaoUqpYy6QTEdNFTWMYy7wv7rX_ooZCgG02HXf4NEXOk7IAlmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از قشنگترین تصاویر جام جهانی؛ مارک کوکوریا قهرمانی رو در کنار پسرش متئو که مبتلا به اوتیسمه جشن میگیره.
❤️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/101941" target="_blank">📅 22:10 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101938">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Cn2J9k4jI3P2DiRZ_pBfTxHEbarS7XX6jaMiyTok9RWI3LNyccvCwUIxRuPGo7Gy1DOme9SdcOJTccpxMI4Q7HGfRIOmksEWlfLkk5DLUi3Jd958GfFOxeCnhTiE9dimSk0iG1iiYLpPbmAFkSLXhbMi7xICKttgJTJ28QJ5UwuYgIJMhLjIz9ugYS4HdwMZZAlc8CnBjTD8wHNlRjUbmfYfA0wcvoxunauQimCh-GGmBRqs8eRp4jvKe4wPSRca-fYwLkZYg9JUXY2ImtxZy_dUhInXckXil2UX1BR9aQFqoUEDedi1Ueih_mF_qrdHTfig9Xx6cZlw8M6BkHNxHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eoFhAUEAdkGEwJHpsk2Yq1ZxcsR_-BuGe7TA3mSz6oMsaG6AcSVjPjRbCGhAWGxfWXylj9J_U6x-ZkJztCU5KSrDcYq_No4bijBRQY-dnD-_CvkRateLMG21-eEbXbnsaIxJ4kRIZf-xTV6bvE5BmxwG7noX3XeoQIFrr2c5cT2yO8LQeAerwTsZqsggrPQoYeKIecS1fU1aqzgIHpPuyR51rb1xJwDSexytFOGUPn5UdQWRJuih3q-WNN8Q3OzIisVaxRYQ77rB89PxNBtttfM6W_D0t7QrHVnVAMmleJHY0tgCGkefaOF7mhXZhXqntrSluNIyhURYxubY_WcgvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TML8hGT-zVAnuZlZuC-KgH3hHOMrrSZM8VMG-18lm9v9hS-XaFz73F18umG92bRvrMox7tP8i4HJGdP3ARrX2HsHpH_zL6YfcDzXIu1NR1zkJO39DgYuIvSURpTzsTfwJLQjbtzJcGGM01NRLALoLqgsfsiAlAmeIFmZtPfs3ti38QTKeVKljCRbty2LHXY8BVjnS_sK-9U49R_u3brLAXgghIkz6vcSJJaIkb7NddobME3eSYeNYoqaiudgXG4xvOoto9VGV17FUoBnN7mzd3R9bbfIiPMafPRELLpOMM9F671yHQycxGN8vFxvCsvjNr7RCtOj8YEPeN27Rgzcqw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇳
😆
امروز تو یه حرکت پشم‌ریزون دانشجوهای هندی تو اعتراضاتشون ضد نخست‌وزیر هند، عکس امباپه رو هم آوردن و محتوای بنراشون هم اینا بوده:
«دیکتاتور امباپه شکستِ سیستماتیک را تحمل نمی‌کند. همین حالا استعفا بده!»
«۱۲ سال در قدرت، و تمام چیزی که از مودی(نخست‌وزیر هند) نصیبمان شد، نسخهٔ پرمیوم امباپه بود.»
«دیکتاتور را پیدا کن.»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/101938" target="_blank">📅 21:59 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101937">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O4HstE1qMe-ptgh1q4IL-n2xHl5Yb4VSJ7oAzzGeFw5NDfk4EnKnLBMJn2CP5IDVKG6bEJzOjclEuxojiXw7JMiaamDHgjItp4XMU-9HvkJrtQvM4N7VNAa65N8ctQ8uENJt1AgMrvyJI0IT53Z-kdd01n--OD5SQXT2FkeMvPHb9b5LyNFu_rxZsyv_lSAU24dCPZjLhrD5MKGNe_GRhooegtyehtR-RA1bcdV0V_-L8jZtdDkAFMgvqbPkNelzY5Bn6Fv_eKD5zpR8YeYN_NSqC56sHqwyK8fJMmKKW76EqwSvsnAcO4-eyQjwrryRCtikDisRFzrIfmN0O81kkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زلاتان ابراهیموویچ: "بین این دو باشگاه، این سوال پیش میاد که کدوم یکی احمق‌تره؟ لایپزیگ که پیشنهاد 100 میلیون پوندی رو رد کرد، یا رئال مادرید که 100 میلیون پوند برای این بازیکن معمولی پیشنهاد داد؟"
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/101937" target="_blank">📅 21:48 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101936">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NFi9fi27CU7rxX3BN2Q2ycek2OQNVAiPSO32yU27aoCacVklg8Sy7NcEwFr7CAxwOFmpUwBV1AEIYWHm9yTbRHPpBO4mgDQofCAzM6999y4RzJvIke2_o80vGs9uXYMBPAboiXKQy2lb3j90kar4ommE2cX-VTfjBvoCGxV7rjvM5c5F-L-FDcb5CoEq84ao-xDrIsFGABG9-CJVGWkcgII-woWzUc0AAdAfg-OnQNZVj2VhFVKbQ_N9OVitT1cMWfPKPLDFestn3R5es5UwawxWS79q79X2xsi9dLZYgOQ4zGFnB4VQXz1PbofDvsWFH6f9Lx-o90rpez4GBcbJXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
محمد خلیفه، گلر جوان و ملی‌پوش آلومینیوم به استقلال
پیوست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/101936" target="_blank">📅 21:31 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101935">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LUIG_lnhWsbFQbjy0CT7R8ps6irJ_61Cl5a8gGsM5Dgjsbowa3DSPqHLaXwvSnZ67zRwDZgDftX3nS_RnxNawuoJl5amiJV0x3N-SZMjQKl4uqr6-oc5inYR6l5Rg6ci88xa4hxrPvKHzFk3TUtPfS7k1MWG_ZgBQOv_zc1NUfcQivlvI6gi14zvm1Qmxdv0NnlIj7tj6qNtGA34YXWGIJkgewzmJye9l7eRex9_KvqXDsOz7sJek-628NFxCMWLY01R2mQ7t5W6DuhyC-ksRga8kwcUcYgkC75oDpw72uOuG3nI7L9unoNEcXgfmAuvzyM5EmmD0sOfmAtZzFs1yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
ماریو بالوتلی:
یه بار زلاتان ابراهیموویچ منو با رافائل لیائو مقایسه کرد، ولی جوری حرف زد که انگار می‌خواست بگه بالوتلی بازیکن خوبی نیست.! منم فقط یه عکس از جام قهرمانی لیگ قهرمانان اروپا استوری کردم و زلاتان رو تگ کردم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/101935" target="_blank">📅 21:21 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101934">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nvwBT41ihk7qChGWBU7-py6l0CluTN0AwpqbhQHjRYqu396odHvO_yB2meowFAWhSSAGnKrvKIC0oEYtWKQXzcTDNJdIi94IJVGr0PdrHL3rmZapFx9AFRPmZunzs49NA1FAHHru-HFDr4i13TwUEv8yPrWyAqjlzKcs_44WGDRpz9R7idjUF2u9oXgdF-kg_WpND8wOic9YZjgMZkn2yQQ665_1zXSRCT6vhHyDiercLsHL1I567HK0UuePLuqiizf4MvKnHyYtguyi_abljnqxbaW0jpLvIBMjBDuCVJpC992dnlt66xxvvt988EXD_o8RFBiLNalFsUswTLF6lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
کریستوف فرویند مدیر ورزشی بایرن مونیخ:
اولیسه به رئال مادرید؟ این موضوع اصلا برای ما مطرح نیست. او این فصل هم نقش مهمی در بایرن مونیخ ایفا خواهد کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/101934" target="_blank">📅 21:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101932">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YQn5CY9z63GkhJZyvs9NwuWnKgD83Abmqxb9S9WEKfpLDodLQN66SrcnsvenheOf50PGl7IwVtnkFloNLuaurK9fAfqTF9eu_OGr5jqicQWvbUPhgqjql0f4EE7epq0XhUBHg-4evvYF9bQHFsh_wgL1g4hBxanl1yCEYYAZ4mQKV8c2ciMylTQw2fOhMSO8T3Wn66xn_lAAyEUnh2DBVeQEtKBTZyV08YiLmBNdGUdHbkebJ8IyvC-D-U46ZEkxhloLa4ZdyPm-X2L35y7eMFQtE2BH9eWRYccyHS55Dhj9fTW35Z-RiAg-ODYIGy6iZMQiSSdDLwyjG-_nPmuPhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OkSQHHOyIPxM3ZdWPE4dcOhPAFNQY1eDHxNBu3oUXVsTe9z5t1_7itga7bEdcT-om28cQdvpwLvt3JOPdvJwhr5e-a1SFiZuQ_qVy94bplKmWAKZcRo8bPYOl37c0MxxI6zWumODSfKZvOiTIOYo9_USUnGlp3yhP2dXJmzRQ2XuNnuXmKy1PjO7ro-7YTORQ05pjkZbYUxC_a3YpV7AzNUZIReeF_15HhWq9FMsY9sYnRsHGYIzrL72yETewa18RcOMxelmxAtmrjy_QQhduqX9n5Gw0KidZ4A_X4rN7TrHFB6svYE12124uox79FSRbM0Yc-FkoVsxne9zqFhXRg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
براهیم دیاز هم از پارتنرش لوز مندز خواستگاری کرد و رفت قاطی مرغا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/101932" target="_blank">📅 21:07 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101930">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gcpiRRyF-9D607XaBEjMxecDH8HJMR0yvxh5--6YrEcrfPasOth880aZ_j4PEOSNjlpfHn5K9wKI60HdmpVYwrLUM_9zOABZos0SgS83FYGGY4gTUjG30b-GDhsYv6xm_Z1Y14Exgs7XDA2cmNZkJWHJxzyI7fxzlaac84mKfI5f_B_OgWeg4izQqBSWqfNwOtyQjcVDq1TzElnhMLt6UR1kl6lcOVngWNMgIkN_sUOS5UrvT7g0UXX95tMzRcrdqeivurgWSjZVf9sBe3rNFKWJ6L87Hva5z482qh0UsG0htYwPPh0ngcMoKmUTimTjND-6yYwIaBUPsbAu9C4Oig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f2c2dac8e5.mp4?token=kjHJXSCz1GxNehkBFUkNlGxuznrmcB5gHemV6ttyuEv002CrD6EehbzMuZuiwq5AzAEFYFCBIsitP1RWSHk4AUJSt8v3lle5mnqHKakSHYoChTpuRQhW9hoK6PTLZUEBatPV97HUQitHWgUAWK2tvOWYiFoe2yzCxFz7Jjx2IYfDrfSk6_iA6nW82cfRlB52pBV4RuE4Y1XbwDqPnEMqKVjlHDLKGEa46EaryKG375TwIqP8ejiHgaDP7MeOvZ5DX1RBIQlK0F9YU6Vm5RRVjye4tbXEoi_9IXeiYe6dQu9X8hm8wP-aRqw0XkmWuW3ZAaGsohcKHcMuSIN4IgOZLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f2c2dac8e5.mp4?token=kjHJXSCz1GxNehkBFUkNlGxuznrmcB5gHemV6ttyuEv002CrD6EehbzMuZuiwq5AzAEFYFCBIsitP1RWSHk4AUJSt8v3lle5mnqHKakSHYoChTpuRQhW9hoK6PTLZUEBatPV97HUQitHWgUAWK2tvOWYiFoe2yzCxFz7Jjx2IYfDrfSk6_iA6nW82cfRlB52pBV4RuE4Y1XbwDqPnEMqKVjlHDLKGEa46EaryKG375TwIqP8ejiHgaDP7MeOvZ5DX1RBIQlK0F9YU6Vm5RRVjye4tbXEoi_9IXeiYe6dQu9X8hm8wP-aRqw0XkmWuW3ZAaGsohcKHcMuSIN4IgOZLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
برگام عجب سلیطه‌ایه این! اینس گارسیا دوست‌دختر یامال، بعد از موج انتقادهایی که به خاطر جدایی از دوست‌پسر سابقش گرفت، یه ویدیو منتشر کرد و گفت:
من به خاطر پول یا شهرت لامین باهاش وارد رابطه نشدم. خودم درآمد دارم. از وقتی با لامین وارد رابطه شدم، بیشتر از چیزی که اون برای من خریده، براش هدیه گرفتم. کلی وسیله گرون‌قیمت براش خریدم، ولی اون فقط یه جفت دمپایی برام گرفته که حتی ۷۵ دلار هم ارزش نداره! بعد هم برای اثبات حرفش، کتونی‌های گرونی که برای لامین خریده بود رو نشون داد و در کنارش دمپایی‌ای که لامین براش خریده بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/101930" target="_blank">📅 20:53 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101929">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s7ijrOIIB0qSUL-tnoZ4OZQKlEvtp1Ai8izcgCkaTlMwZJePRx2xDcVvHTl9U-wRPUp5vNext_ck7D-q1Pt9ctPUsiS6Ug2AkizylstoLXK3w0xbypL8hxsSGCXjnpugLOE_KOKYsvjxW-xdNCSl3P098dM92c-pNbeNjItMpkZRbC-uTkIU_m9SoZNKQaARc8R3QcEO3m2Horo4tJmzN4CgE0OwZPhpwWffmBTmUJ11ci4lKNcBZ91m6pN-fBkyKPekvzUEGjDaa3_CBmvRfpW9N3jMaXiwAlzA1tITtZQ0E5mFA89_jStGgBI0nifENOCtXkIO15Dp4KL1skhxnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
پوریا لطیفی‌فر هافبک گل‌گهر با قراردادی ۴ ساله به پرسپولیس پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/101929" target="_blank">📅 20:39 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101928">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/62941770b7.mp4?token=SrrVR2fiWe0A5B6-5CczB29RafVNeTkFOrjokdoqqPG2xR3rEguxzZJnhdMQVz6PDuLwmAozLGLt6HVlFEMt3wt4aesniQcqrQ3N3ZDitLyWNWfgEwDC0_pKpXGEBsmJjXXJYVvQvcGZBmSxzinWBGLEWUUumv7DR_PP-PmMe8xsmqYebFWfFshhKg09nqd2LuXT5q3ToB7TdblLnvGixPdWoAjgRnHkpFwsaGvLNas32Ga1dRfHtw_Y4otdDbynFa8WTQa6Nh2IPfPgKzrgDQi7BOI8oE7wUC3JpsIO6VVA2Raacsl89O5LTBkQfgc1XM9EZslhzrM_vv4u9Pvg6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/62941770b7.mp4?token=SrrVR2fiWe0A5B6-5CczB29RafVNeTkFOrjokdoqqPG2xR3rEguxzZJnhdMQVz6PDuLwmAozLGLt6HVlFEMt3wt4aesniQcqrQ3N3ZDitLyWNWfgEwDC0_pKpXGEBsmJjXXJYVvQvcGZBmSxzinWBGLEWUUumv7DR_PP-PmMe8xsmqYebFWfFshhKg09nqd2LuXT5q3ToB7TdblLnvGixPdWoAjgRnHkpFwsaGvLNas32Ga1dRfHtw_Y4otdDbynFa8WTQa6Nh2IPfPgKzrgDQi7BOI8oE7wUC3JpsIO6VVA2Raacsl89O5LTBkQfgc1XM9EZslhzrM_vv4u9Pvg6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💎
استمرار، استمرار، استمرار تا رسیدن به هدف
این ذهنیت منحصربفرد ترین بازیکنیه که دنیای فوتبال به خودش دیده.
👀
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/101928" target="_blank">📅 20:20 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101923">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V9DXPPsX9-nhFiq_tuTISngjEMm1xB0qwdtJnQpojX9gU_5pJGc4aW9ZVzaMxss55ryz-leyiebfN2_xPrWWSxL5d5ctFnniBK_9Kq2cbTTMsEluldfOTGp6myIAhUzq7adYNOGCDx92EBWlVmcEiU-tQS2GF7kC7vt-Ziepi9kuTsa5PcvaktkBbXS7h7If1ww7noogf0MBBn9TeSmQhp6FGH9-zAbAbEmXALqLYEPk7TKbYmIMPvIo96XQAotSqESE1Ig71HF6iyNf3cpkNecTLaPys9n1u1QzurWn1yUT3qSNmgU32LBcgfWPNE9-etyX31CW_OisISmXaA9ncw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q57m_-JKndkh2Yt0iivERluGF-t9KC661REe9iSbOqhrTfBy1TWxTdBNLb1Xhc7gzueCLppwa_jN7fv4JuBQSiMb9ybaS9oOHZSbsErnTdAtSDNIGbiqwpJBewyKRGT5aInhE31Yx5_OiByz0wNzZiIHOPANeLA4jsjns1psErsCdx8FxyINGibei7tmXPiQNxL3EfLxAthwSUhfBYVtQpiU05dgByV40suPSqXhgh-GoWOPg0NvHHj9HYSqUtophu6P29NBDrGfmy0_v3D3l4Xw1KBmBLCQ8-uxJq4bQciyKPfuIfN9ZC5PQiZWiXTII30OkfJkUbH-Tv0tlQ31Yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I8N-3yq6njXoPloKlKkxbAI7kH20VN5gRqn3VH5UpegweTQyh7eWURXp51Ff-hHE5FTYGzdyMJRHOjAFQq_cOmV8Ub2t8q7qUl9H0JJ3v8slrvzyz7rFwiSMRBVpRFzDPCdDCEXGxkwnyva4L1JntIY40W3b8t4d3PHmehuOej51BNfEEu0_L2xnnvZ39kP9p3k5X8pSP0pL2L3HgD3RI9BXmerb4d6kXMxjBzi0oY0xQNxiZxgQpJR4L8PmjYSNqcOZJ9_FIEWUPd9tanX3VgQQw3aKY40sv2pKa0pAv3sN_DwPgpqoEA7Bte0Wr4qGNkk5tlFmDlqY9eTcM7dJVQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91c7199c9e.mp4?token=vC7kjgsefKn3UwQd4kOaPYpRbwwwEolj-hdBMrgo7ZcT_PrSFiiBxRw0DNxGO4lWqEfljp1iBrLM1HTjwgXoem4QmEGB2TDIlKqMCdvAJXdLYDir9I-5vO-koN5gdnUJtyrJTk8cftPI9klC6JRPM0yC6X9uIo6MBPze-4iLqrAkPBgCktoEAIGoaG7gXm-ejr-1TVzvgcBAUt7pNTA2GV5BkdS-iNDm2AnUQFSYheOFXIvnfasdbNxhjxvpW2XXXY8UK49X2BC5U4GqN8-J6PfRKOYYisepD-gXQNLbwxDcDn9WtULaw1LaKU9p9ViOrof6IeVS-m79DYQAzlIReQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91c7199c9e.mp4?token=vC7kjgsefKn3UwQd4kOaPYpRbwwwEolj-hdBMrgo7ZcT_PrSFiiBxRw0DNxGO4lWqEfljp1iBrLM1HTjwgXoem4QmEGB2TDIlKqMCdvAJXdLYDir9I-5vO-koN5gdnUJtyrJTk8cftPI9klC6JRPM0yC6X9uIo6MBPze-4iLqrAkPBgCktoEAIGoaG7gXm-ejr-1TVzvgcBAUt7pNTA2GV5BkdS-iNDm2AnUQFSYheOFXIvnfasdbNxhjxvpW2XXXY8UK49X2BC5U4GqN8-J6PfRKOYYisepD-gXQNLbwxDcDn9WtULaw1LaKU9p9ViOrof6IeVS-m79DYQAzlIReQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پدری تو تعطیلات در چین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/101923" target="_blank">📅 20:17 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101922">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AwIKZZfQw6ZlxcqvU-vWh7J1vdlYbweOy9ne0t06mja-yuObonJQ9VFlQfSxDl5ZmJwPuR91foCr0uEgLlZMBjys83p4b2xV9BaISoCUfvaRk7QtkAX0fMcvUxXZG5wmmm2xPxezeaoWhm5BHSNvGNQ-IsLwB_hSentmj-DcWDVJ-1Q4bdOIgwvJN-bcwcOctuJlgHkS8L8Z7WCn_oLhzuhfK_3tPrIPokUGm7Q82_o8kaOCTa64sxa6g-2qlNfjrePv8u_1Oyh7vFcV_0RxF2AY78EpfGc05nmgyr6Fx3ALbhH7duXugRRCs-CzyYhqg2yoQrCDnNiavvTmPoyW7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
🔥
همه مدل کیت فوتبالی فقط 570 تومن!
🔥
⚽️
از کلاسیک‌ترین کیت‌های نوستالژی تا جدیدترین کیت‌های باشگاهی و ملی دنیا با قیمتی که هیچ جا پیدا نمی‌کنی!
😮‍💨
❤️‍🔥
👕
کیفیت بالا
💰
قیمت مستقیم از تولیدکننده
🔥
تنوع فوق‌العاده از تیم‌های محبوب دنیا
✅
دارای نماد الکترونیک
✅
امکان خرید حضوری
🚚
ارسال سریع به سراسر کشور با کمترین هزینه
اگر عاشق فوتبال و استایل فوتبالی هستی، این فرصت رو از دست نده
👊
⚽️
💚
کانال تلگرام برای دیدن مدل‌ها و سفارش:
تخفیف  ویژه  برای سفارش از طرف ما
👇
👇
👇
عضورت در کانال
https://t.me/esportsofficiall</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/101922" target="_blank">📅 20:17 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101921">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5fac07199b.mp4?token=pKJZqjoovQnoHazJfoSlKmKAjHf6vlrerfXLwaM93Twv07VBKwvgmzYRlMvr8iWzvVSSlI_IwqqvVo7nmCWLLYO3AxB3Wj_AseyituTulp7qQfQEJdMVJUBJeteu2v9gg81JLVMta83TtvlXfVWAdcVXKk8Qre2kzbLpBX2W1QWGA9Un2GfGmckvvKMVOQ-avP8IpSX24kTJEAYM2bd8QtT25TDTpXCWSepUf7Kt781mV1ep4XXOK3omqgBdtxubNiIgtHeko772SBonBIte5vtse3qmafJrFzPq7DQfXNioz2TZsD1PqekYme89tl4_5CyKkKL1tJ-4wWHvpTq7yw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5fac07199b.mp4?token=pKJZqjoovQnoHazJfoSlKmKAjHf6vlrerfXLwaM93Twv07VBKwvgmzYRlMvr8iWzvVSSlI_IwqqvVo7nmCWLLYO3AxB3Wj_AseyituTulp7qQfQEJdMVJUBJeteu2v9gg81JLVMta83TtvlXfVWAdcVXKk8Qre2kzbLpBX2W1QWGA9Un2GfGmckvvKMVOQ-avP8IpSX24kTJEAYM2bd8QtT25TDTpXCWSepUf7Kt781mV1ep4XXOK3omqgBdtxubNiIgtHeko772SBonBIte5vtse3qmafJrFzPq7DQfXNioz2TZsD1PqekYme89tl4_5CyKkKL1tJ-4wWHvpTq7yw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
😐
تو شیراز یه ایونت ورزشی برگزار کرده بودن که چهارتا کم عقل سر دختر دعواشون میشه و طوری همو میزننن که کم مونده بود بمیرن‌.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/101921" target="_blank">📅 20:07 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101919">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KFAWKlwoJxSnnSXqYpR9MVEh23_Va7uGWioCY36lmy68BhXLCYfltIs5nbKYTinfKbL9PL0LI-sW2iOUYsU5MXYYr5Xvqos6B3IQhl0wyFed5F8MWjUPQPdZuJBbUR3us-YTcDNJJuj1OZEPGx4_C2yDIYJ1a0s-1i93EkBr6RV6eUiQvLgnkXPPw81gkUn98r4k_uEQ1HFz0mspeGWj-Ni_IIvPmvUY5qxvm9pL5B6EVd2t65gLw5f1wyI_zQo11fMNmu9Nwfv3R14PbyP-mtNNR_DuCx1FqcrffQur3um9JxoThFoyEqbcFCeksL-wSLB2ZaEmJ3Aa54p9Zz8VwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h2HWZSqxZbB2Ib7hbblAs-fkVE61DPvkAAGz3zSney1VJ6Ejw8MCAF-ysJc44Vf7sdSGzLeROTiZqTIZgw1DGCcFkrneF0H6vL94jlRgH3cd8r8ZnMlPReZ7yu6OXsYZCgKNtW4MTcNGcC3fX1t8MRkIGNvoDDPZPInM2DUCnzVWhNihMrJV-ImERfRqRlYopf29Z3oGwqmuriMrsH0-OSmkFdzGKh3sX-qS_eu9LjfrxpH8qGyiBOlLMLciumlwwZ1JpppJXpX734-BpHkMfpZjTEF4ie-wKOd71c2v4ZEeNwVdX-nbcbQn-emsOSpegTO6X8o8limq6PiJmr-d1Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
🇪🇸
فرناندو تورس یکی از آندرریتدترین فوتبالیست‌های تاریخه.
افتخاراتش شامل:
🏆
جام جهانی ۲۰۱۰
🇪🇺
یورو ۲۰۰۸
🇪🇺
یورو ۲۰۱۲
🇪🇺
لیگ قهرمانان اروپا ۲۰۱۲
🇪🇺
لیگ اروپا ۲۰۱۳
🇪🇺
لیگ اروپا ۲۰۱۸
🇬🇧
جام حذفی انگلیس ۲۰۱۲
خیلی‌ها دوران سخت اواخر دوران حرفه‌ای تورس رو به یاد میارن و تمام چیزهایی که به دست آورده بود رو فراموش می‌کنن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/101919" target="_blank">📅 20:02 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101918">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VeK5uHH6bN_pAFg5TH5iTj0huK1LQEGUOgiz_fMORhpnPhkWwcvuZ93pfz_O-hlSZqx5onYnFQ_v7M03xS5FjJhZfbZkfRQkRjTpQwlpKJ9mHIASt3ZNCnr0oG6c6nOthhftuUnUZpbs4YnexrhqEw6agxmtc5pbygeNZSHoSFp3DaRHIMB9lTxRLDtLNv4BdJVSQtLuksiqN27qgYXkWYoV666522R1zfTT9i7sUvP7zo3LjaVAmE5pxv9od7o-l6ySKgqNB4oGyEUwBZq-CGTBrw8WNY6uXArm2x0j3pWo_lDv9JclR-Cv0TVWVlRXgV7PffboARuXKF1Vh6ZnPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
اسکای اسپورت:
هری کین بلافاصله پس از پایان تعطیلات تابستانی خود مذاکرات را برای تمدید قرارداد با بایرن مونیخ آغاز خواهد کرد.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/101918" target="_blank">📅 19:48 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101917">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/779a683584.mp4?token=ovi-nWRYCBil-Rm3eFO2d8P4GkICLkV4V0-sx3g_cXMXWo659JzkevhiL1O0JAD7rORsofhQ8zvhhou0VZX9yVXnsUlw8GZBif70z5j9Cy159RzSqK-mIwn7ENAjL60HJ5uggcaTCDZjl_o-xL0iTxzbHljJhXuBUejoT_dlKf2dDtVVQC5ih_GZ0-Q715imTU-limu4T9b0If8NtSexJsIoHju1zZhbO51nnIOI-MuRSqpZDds7l1bBwKVTaPeJGqPjE0EL1bodiTMM5gVskPsPCkMk4fQwwFEjsEfO0eYWn4UaD54dkRmF7dpyAltbhI5tZ1TKhCpzipWZWeEghA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/779a683584.mp4?token=ovi-nWRYCBil-Rm3eFO2d8P4GkICLkV4V0-sx3g_cXMXWo659JzkevhiL1O0JAD7rORsofhQ8zvhhou0VZX9yVXnsUlw8GZBif70z5j9Cy159RzSqK-mIwn7ENAjL60HJ5uggcaTCDZjl_o-xL0iTxzbHljJhXuBUejoT_dlKf2dDtVVQC5ih_GZ0-Q715imTU-limu4T9b0If8NtSexJsIoHju1zZhbO51nnIOI-MuRSqpZDds7l1bBwKVTaPeJGqPjE0EL1bodiTMM5gVskPsPCkMk4fQwwFEjsEfO0eYWn4UaD54dkRmF7dpyAltbhI5tZ1TKhCpzipWZWeEghA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
رونالدوی برزیلی سرعت یک وینگر، قدرت یک شماره ۹ و تکنیک یک بازی‌ساز رو همزمان داشت.
🇧🇷
🐐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/101917" target="_blank">📅 19:40 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101916">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa3ffe3c02.mp4?token=q31bdelCkmipcWHnqeziPbrUZHcjaN7g_2rgGTuNzyZx_abOWkpXH7Etg328L14neOgCw6I2aTHdJo0PCaZsg-upjZYsM7i9Sa5l-xJu4_Uxol5O1DgaDL7PfVakQey2atwBqBdebmy6S-SikkVekvPOQqau495L2lVfAkZyfP_uzTHAIGsqIhWwFIt93r_ht5n0MKmekhLU10yWSy2yd9veKckw30JO68S5TsM3vwPG6aTBP7lzbXSLUe5aISLuqI5JM1jcj4-AbSIaqxHJRj4xV4TxKGui_wirBh3GgJ6HDB4ErmH_BPys-C8LSurRds2aXcjuvBsO2nE7Qrs51S6UwaLXSFXAW-qlC3cGOx-0tSTTMaxWpO1EjOaKAUljQWR6P6Y6oeYlSNsO-TuxQzoACRsY4oesxtMmohBhnjX3ZIzjcMrds0Cxf3BzN7pui9tTmZ_lf99P9CwO13pLv4gTYC-PttNR_4u2q4Dv0TyCiQTxOgDTVw4D_mgbg7QDIfLnvnNlvK-XWVmqCQ5RD8IjTwfXqsuX1Njje64XZ0Wap9s2Cb3bRezq4EM9ef8IfNNxs6s3SFLM0JJQey2HcN-irOEcj3qy_JGc5bjem4CyAusxTGidAprFpWd1eTv_usbQ4FpRSJ9-FzOW2VnPxMfzUb-MmovcSKpkcz4WGeM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa3ffe3c02.mp4?token=q31bdelCkmipcWHnqeziPbrUZHcjaN7g_2rgGTuNzyZx_abOWkpXH7Etg328L14neOgCw6I2aTHdJo0PCaZsg-upjZYsM7i9Sa5l-xJu4_Uxol5O1DgaDL7PfVakQey2atwBqBdebmy6S-SikkVekvPOQqau495L2lVfAkZyfP_uzTHAIGsqIhWwFIt93r_ht5n0MKmekhLU10yWSy2yd9veKckw30JO68S5TsM3vwPG6aTBP7lzbXSLUe5aISLuqI5JM1jcj4-AbSIaqxHJRj4xV4TxKGui_wirBh3GgJ6HDB4ErmH_BPys-C8LSurRds2aXcjuvBsO2nE7Qrs51S6UwaLXSFXAW-qlC3cGOx-0tSTTMaxWpO1EjOaKAUljQWR6P6Y6oeYlSNsO-TuxQzoACRsY4oesxtMmohBhnjX3ZIzjcMrds0Cxf3BzN7pui9tTmZ_lf99P9CwO13pLv4gTYC-PttNR_4u2q4Dv0TyCiQTxOgDTVw4D_mgbg7QDIfLnvnNlvK-XWVmqCQ5RD8IjTwfXqsuX1Njje64XZ0Wap9s2Cb3bRezq4EM9ef8IfNNxs6s3SFLM0JJQey2HcN-irOEcj3qy_JGc5bjem4CyAusxTGidAprFpWd1eTv_usbQ4FpRSJ9-FzOW2VnPxMfzUb-MmovcSKpkcz4WGeM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
یکی از مصاحبه‌های چندوقت پیش کریستیانو رونالدو که اون گفت او قصد نداره یک‌ روزی مربی بشه و بیشتر به مالکیت یک باشگاه فکر میکنه. او همچنین درباره اهمیت مراقبت از ستاره‌های جوانی مثل جود بلینگام و لامین یامال صحبت کرد و گفت باشگاه‌ها باید به رشد و آینده این بازیکنان توجه ویژه‌ای داشته باشن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/101916" target="_blank">📅 19:20 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101914">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ew8LRBdjDJRBih0YLMrSM0PPVxYhN97h3GHPufx-CEZxITPN4KP2uCS9vY-dxeNiE2I05i18bN0ayZ0HHK4-rLBac3T7L8jcAulcv1FCRQI_BzHipVNtdZuKp4fDkHYJP6okMM1r_x1Lycy-PTjjonwO6z-gWFVsWG9FbUYe8Cxy0TV4ofRLORb4R5k_-M3gJMK0r5FJd_gRADZq8Gi3CtM_9MEwDKiH0pBsJu90vfcDX9XgSZWWQuZ9BgVUKnq_zmLnzfnaqL5Nj05LL0meEm3pVEvMNRBfhjCV6m7VU_Za_OnWg9eSgsdOY1LTk7uhALW6hNUwFE7cjrPQvr5Mzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9c742e9e0.mp4?token=IfQPdoMMSTIMq_228jG9pJ9OEwJ-7-Upixz8wIjW98KYmjE8Bjvf7EHSUEfNEHH-hSYS9UpB4OpnF3214p7OWZiV1avpPfrpnlMo9UseGckE-32qKCD4Hv8SyuqTRPGqIrGbo93yMXjo9Ddi-S2yZp0qfjdztTSoRWXQ5--QJZ_gZdqUnJqPZvQAIj75Tgzdl0xBpoqbzdjQmFcDep_q_2yM3G07xqe5m3muJ-pKXjYSNlmLvxkD4nlINXrQbidVYS5RE-lJdFFUTbEgUJ89LaEwZfDjbKv7ljdsTKBV4HwSL9VuSRwX1A-Xo46Gz6pHM8tBJFYkr3Rdk6I1VybP0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9c742e9e0.mp4?token=IfQPdoMMSTIMq_228jG9pJ9OEwJ-7-Upixz8wIjW98KYmjE8Bjvf7EHSUEfNEHH-hSYS9UpB4OpnF3214p7OWZiV1avpPfrpnlMo9UseGckE-32qKCD4Hv8SyuqTRPGqIrGbo93yMXjo9Ddi-S2yZp0qfjdztTSoRWXQ5--QJZ_gZdqUnJqPZvQAIj75Tgzdl0xBpoqbzdjQmFcDep_q_2yM3G07xqe5m3muJ-pKXjYSNlmLvxkD4nlINXrQbidVYS5RE-lJdFFUTbEgUJ89LaEwZfDjbKv7ljdsTKBV4HwSL9VuSRwX1A-Xo46Gz6pHM8tBJFYkr3Rdk6I1VybP0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🎙
طبق گزارش‌ها، لائورا ایگلسیاس، دوست‌دختر رودریگو دی‌پائول، گفته او حتی ۱۰ درصد توجهی که به لیونل مسی دارد را به او نمیدهد. او مدعی شده بعد از شکست در فینال جام جهانی، دی‌پائول دیگر حتی کنار او نخوابیده و رابطه‌شان به جایی رسیده که به فکر پایان دادن به آن است. گفته می‌شود او معتقد است دیگر بازگشتی در کار نخواهد بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/101914" target="_blank">📅 19:03 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101913">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KnmaMsfau34NSLn5E_Lp_j8ytqXOHGDe2AWV7X4SeLfJ4VQ3FM1aeOgfhi8PW9t6jSzVb8iiC1CxWPS3xcRTfoc0S6DC7FDgBq7_2tYT5fOOuGnFEMRXzyDMMKNyGDHonib0tcreHqUzDNn8WLLcqsw9GrswMbx3ZngerxC3DjKLYn1aU54JY9VUiqMjC15QsIrC80jdBcpY5iKcp9hPiZ4YS4cvn93xpsUH1HcaMuicx7tsU2RLID1iMde1BzXn8mULrr5073nJF8aj9MvdHncYz0Wj7IpkrCwzGeXc3ro2wKFv_w1up4Bk09aFXopnS4SSV-NY_WxP7AAxf3kL3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
تلگراف: ژوزه مورینیو با انتقال وینیسیوس جونیور به آرسنال در این تابستون مخالفه.
❌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/101913" target="_blank">📅 18:44 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101911">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CFdA8b3Hefx738vdL1zKfztwqC2xCOPNM-0sJm3Rnpi44ehXhD-l-UJVMc1ZAdTQP6roznOZb24E7Q3lh8gm6_yAF45kiWfxhaR8u7VsmNZM4_YpdWvGLz3eWOc1Zr_5EEeYlgl4viLVMAKauLcWZ7izGRANYYqOD6ZBC5pLpMFuLjGfNGJ_KKAea24c01526PHzZ7-T0_bat8_BjyTSh7vFQu6wXc73A5nvKMAXr-iw4ZrB8h3aLWQY2PY28q3ZLSUWtyCAGrrLqhnOwcqtEG_8MWtwttiMd6OY6YPP83U1Izmugyvug78tr3FgreY7MJ7l1wSFD4a5TGAo3bSosQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O4XM3UbR8c3rOT9CvPn7QtfiMzdMuxCe_i_ABB3tas-SEyimWjw8zXY5eCaPTXMzGkafNLudV1bowTZOjiVxtJjjoPQr9rF7z-uO6vVJbfT6ps6ALO8VNL2jE3Ybfm0YojCZK7eALuUZSf-3scETAX-R4y7mKy2N07UvXeJbbEhaz0X-lIYuf8C5kzUcr9IVVOSInAH4D2KfoUdT7nvyvz-MUo8YSCmo9DLbmld0-cvCogTRqxEkeyiIV4zPhE8pR_Zecw8x_PfjF_0NIfybIH7VHD1f5OI611sfxdg03avqxTJUCki-FWnMGMtgJc94_AAQjRLNx1ExC0TaPs61LA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
⚽️
رامون آلوارز:
اگر انتقال رودری و دیومانده نهایی شود، رئال مادرید ۲۶ بازیکن در فهرست خود خواهد داشت. در این صورت، باشگاه مجبور خواهد شد حداقل یک بازیکن را از فهرست خود حذف کند تا با محدودیت تعداد بازیکنان مطابقت داشته باشد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/101911" target="_blank">📅 18:43 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101910">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DA8VGmVo04FkIskYstZSSnCWD0--kN6ZmJ8aVDz7z-Zi27f5m3XUgpmqzNjVoQyiyPGLSvbKB2_Jd41dsV7MbjTbFgDETBCzqD4_zwkq1grtckJ01txno0iYKpic59S7SdW1bTo3GiTcrUA2wL6ZDPtc_yjPe6sKskxwIzoL5nXYiJTiK0vqiaRC8PCOB92JVsONOGsXn9BaKiln5_mvtvsYG9C-OQl47S8Q_hxW4cKergzoeNjnAXy_4HCWsA1STxt8it9v3M9ON99jPOZz3ZWba3xiC-SRRe_PnSpwMvMORPF7sMmBpzD_eKw5X60mdDP6QFw41vDcyhBdzyK4Jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با ربات هوشمند تهران پی تو ۳۰ ثانیه خرید کن
😍
فروش یووچر، استارز و تلگرام پریمیوم بدون احراز هویت و ثبت نام.
تحویل فوری زیر ۳۰ ثانیه.
درگاه رسمی بانکی و مجوز فعالیت
✅
@Tehranpay_bot
@Tehranpay_bot
همین الان استارت بزن و راحت خرید کن
تلگرام استارز با ۴۰ درصد تخفیف
😍
یا داخل سایت رسمی بخر
🔽
https://tehranpay.net/utopia/</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/101910" target="_blank">📅 18:43 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101907">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/A2UMPqzQcX9G0WxnsKTvxWSpAD3YeBG3hFBrD-wCDRPbd1ovBYiOgP2Uwnzjpi5rkM5qQzIzwUsjogdVITem4zSkK0nk0fQqLzs3QyaufXpxiQ52qMzXmHwh2neTWYzPFeGPzFRN-cqH1pHEvY1iwUBv9tqkz4j3LII_GMhLfdm0NQDa5-phfJ9UAgD2yC3nVmAY8LQtVhKtyEqISZ7kF9sKelaRm1liWpB8ntoUPy9DqjLtsiztoJDan55r5RPbfB_kRmje4UITyEE5LTC7KkolCR1blag6j1_KjLci53kR9JPcw9mayRIEPieOrjLc4pzjAIZA4ZLAU0vwMuMgSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e5ZuhN5DYHWv1HZfrC6621cLuMe6tKZDlc5fR8gyTZuEXuDJWm22FJuXJhwS__zykYjT7Ta2TpPKg-YgiDiL6uGgctNN5OjIUfIMoHfhCdRJLVQf5tzihHPbffZVdZMp-fFhQIkJPZziN26MyQJ8krOUi-xD4fDF57-lHXlzYMJP6Ma8lxIk28oMC9lMVHGRvlMd-zY9D3Uj8U_uXN6KoJ7-W6vR_i9Nerkzmu0DkPaXA5YOMZ6ZK5rqn3XMfd8ARUjj41qTVUA3sjvqTAUSxGP6PKFaOQmPOQbgkZXDPgPOYrtu1jUedsK4OerCrk66o8f8CAsh1uoLm2QCG75qDA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d05827d11.mp4?token=YeMLdfS92PUgueiTem9RwtY3tzOWje4r0QxVZppBmBLERzEIPPf3ef0rReXMZedwDl5G8W4rpuJTfjAvNvzjUBlJ1HaO0TbY-TtZ6QYWHFrgse_1buKYv6yXJ1oUAcQ5BLCvybo-TrFzXNTvRs0zwB_1ypKWFbs3WIC35lTaim4BrRNZAiVPFxnJLjFd0T2hF80k2bkqMWH1flcwC8peyGUE4k01iKDNb6i3iax84Xai0TOxcAKBZPvNXYZjsMd-uCqgV5DUy7QKxOc146T2Ov010tik4j3bT60em96mBSTzwa38mY_pspjY-pWnCGjAsx1rN3E4HttMFvqXmUbJOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d05827d11.mp4?token=YeMLdfS92PUgueiTem9RwtY3tzOWje4r0QxVZppBmBLERzEIPPf3ef0rReXMZedwDl5G8W4rpuJTfjAvNvzjUBlJ1HaO0TbY-TtZ6QYWHFrgse_1buKYv6yXJ1oUAcQ5BLCvybo-TrFzXNTvRs0zwB_1ypKWFbs3WIC35lTaim4BrRNZAiVPFxnJLjFd0T2hF80k2bkqMWH1flcwC8peyGUE4k01iKDNb6i3iax84Xai0TOxcAKBZPvNXYZjsMd-uCqgV5DUy7QKxOc146T2Ov010tik4j3bT60em96mBSTzwa38mY_pspjY-pWnCGjAsx1rN3E4HttMFvqXmUbJOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🎙
رودری درباره جنجال‌های جوایز فردی‌اش:
فهمیدم مهم نیست چه چیزی به دست بیارم، همیشه یه عده هستن که میگن بازیکن دیگه‌ای شایسته‌تر بوده. وقتی توپ طلا رو بردم گفتن وینیسیوس باید می‌برد، حالا که توپ طلای جام جهانی رو گرفتم میگن باید به مسی می‌رسید. این بخشی از فوتباله. به نظرات مردم احترام میذارم؛ مسی و وینیسیوس بازیکنان بزرگی هستن و مقایسه شدن با اون‌ها خودش افتخاره. اما بابت جوایزی که با سال‌ها تلاش، فداکاری و ثبات به دست آوردم عذرخواهی نمیکنم. هیچ‌کس نمیتونه ارزش زحماتی که کشیدم رو زیر سوال ببره.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/101907" target="_blank">📅 18:40 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101906">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4cbd3d9241.mp4?token=B4Q679osbvQJ5K3_8arnz1hcrjXa24QYGwDJXZZoKTqjYmCeWfbFuRg6LYavrwBslNYNhd5ZZ-k7YS8Oi9_i37YlaHTJh6GOz9koXY1_H8GahnGwb1b2oHKPu2qyu3foWLl7urSzfw8ziYEtFv-XYouBihskfy7dxtQ0rP46lokI28AtuyhZGD03yNhk-lqeGJyvN3uZRbHRU8oRF8fNfUJoaNN0nUApfHqYWBqMSwT1L3P5j_cUqkXjQsa53TOQBbAtMxoeJNm-YYGYj0LYctIboqd90ydXwr2gGdrh1CmpTaS-tH6UfPsNEetapamZcMCDGBtMK88uSue545wZPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4cbd3d9241.mp4?token=B4Q679osbvQJ5K3_8arnz1hcrjXa24QYGwDJXZZoKTqjYmCeWfbFuRg6LYavrwBslNYNhd5ZZ-k7YS8Oi9_i37YlaHTJh6GOz9koXY1_H8GahnGwb1b2oHKPu2qyu3foWLl7urSzfw8ziYEtFv-XYouBihskfy7dxtQ0rP46lokI28AtuyhZGD03yNhk-lqeGJyvN3uZRbHRU8oRF8fNfUJoaNN0nUApfHqYWBqMSwT1L3P5j_cUqkXjQsa53TOQBbAtMxoeJNm-YYGYj0LYctIboqd90ydXwr2gGdrh1CmpTaS-tH6UfPsNEetapamZcMCDGBtMK88uSue545wZPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
حالا که اینقدر امروز دربارش صحبت شده یه کم یان دیومانده ببینیم.
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/101906" target="_blank">📅 18:31 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101905">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff6a2da2fb.mp4?token=kamxLwxuvY5tEpIZqFlJlGP4uJqoqYsBjwtxZclS6BEGOkdmvDxpEF1dUE6mJ3nnYNZ1yv99phdfKrpYbHAKPhrFQL8cTGkJi0n5d-xw5Wkiq_fUoerE4s-cK9Y9p6dsBNSfkEZ590dseQWw734Kot2ZA8HOhj1LnOgpgSWpRGyFCQs0CLzau1kETYHsGfBaigCiLSIZQaHnYMnVGGoJERTyIFVjEPblX1WVOLLPE2u4-c5k3NhACOuIv-xvJYlV9QSQWgyKR7ro3mbQbzNmAcMiZuEwh3IQ_LoN72lTaU-VlzZBKZ6cXN57u9j2rmbGD5IoKNqm2h89r-95R8JdkXhB6wAkSd7xXG7gsxDPau96O01QAQ-nQqoI9XqZLvOhwOx9xM2FfZ4v1GrkWF3QeGyzIIYn2m7TiwjZIyPPXvsXkKMjkovLLQWeTEoxEbym2q5yh7XLrdWDGOGq__UVAgtyIDHDeWNj1oRWiFSkwGMltmG-YsaaETl-E02vfSv64W24J3ju2-QGEXDvzk9m5ThKxdG3Pd_EVU4koBnbDCTMF4TtI2pvnhr-y66O_7WXZn6MUpMrSnSnteNVXxuAg5Z75u_9uDW8HbueIQ9hFlx42pzts0IfBxynSWjd-iGaeMm9IgXapPYY7ApBzY_2wvau32tymPnVDP-dtgtvjBo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff6a2da2fb.mp4?token=kamxLwxuvY5tEpIZqFlJlGP4uJqoqYsBjwtxZclS6BEGOkdmvDxpEF1dUE6mJ3nnYNZ1yv99phdfKrpYbHAKPhrFQL8cTGkJi0n5d-xw5Wkiq_fUoerE4s-cK9Y9p6dsBNSfkEZ590dseQWw734Kot2ZA8HOhj1LnOgpgSWpRGyFCQs0CLzau1kETYHsGfBaigCiLSIZQaHnYMnVGGoJERTyIFVjEPblX1WVOLLPE2u4-c5k3NhACOuIv-xvJYlV9QSQWgyKR7ro3mbQbzNmAcMiZuEwh3IQ_LoN72lTaU-VlzZBKZ6cXN57u9j2rmbGD5IoKNqm2h89r-95R8JdkXhB6wAkSd7xXG7gsxDPau96O01QAQ-nQqoI9XqZLvOhwOx9xM2FfZ4v1GrkWF3QeGyzIIYn2m7TiwjZIyPPXvsXkKMjkovLLQWeTEoxEbym2q5yh7XLrdWDGOGq__UVAgtyIDHDeWNj1oRWiFSkwGMltmG-YsaaETl-E02vfSv64W24J3ju2-QGEXDvzk9m5ThKxdG3Pd_EVU4koBnbDCTMF4TtI2pvnhr-y66O_7WXZn6MUpMrSnSnteNVXxuAg5Z75u_9uDW8HbueIQ9hFlx42pzts0IfBxynSWjd-iGaeMm9IgXapPYY7ApBzY_2wvau32tymPnVDP-dtgtvjBo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚪️
تیم رئال مادرید در دوران پرایم خودش یه شاهکار واقعی بود؛ به طوری که تقریبا هر بازیکنی، کاپیتان تیم ملی خود بود.
💀
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/101905" target="_blank">📅 18:20 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101903">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/virCfL5coZz3MGNB6eZSpszrjsvuU2pxswnyATfscf3sRlvBEEDNbKJaWWIecc7jMXye6iigsowu0rdVWgS93_v6ql4k6Z9IPu2kCstxSlE8bE9DSW4Hj2p_2JtxL-T6EPPL8pfNWNQwe8Kg7hvFMu_f2b-sFLdknM9_Daf3U21dmVbnAYmlhRgfGVOjn94Emi_J-L-SlMqBrbI1zkL3qzTgBEAIVNXyI5odLvGBOEmx2l9H0kA18oFR_Rzeyu8GWDYMKVq2XLeuRiqVXbXcItnXB7tOMiyNchQaSXP4BZKlE4oNjKYiFwdIFY-WKuTITpIvXX8FpuYRdTpQByYRig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
⚪️
کاکا درباره دوران سختش در رئال مادرید:
من از میلان آمدم تا بهترین بازیکن جهان شوم، اما مصدومیت‌ها و رقابت با بازیکنانی مثل کریستیانو، بنزما، اوزیل و دی‌ماریا باعث شد کمتر بازی کنم. حتی امروز بعضی‌ها من را یکی از بدترین خریدهای رئال می‌دانند. اما آن دوران باعث شد خود واقعی‌ام را بشناسم. کاکا می‌گوید نه بهترین بازیکن جهان است و نه بدترین خرید؛ بلکه همان سختی‌ها او را به انسانی که امروز هست تبدیل کرد. فلورنتینو پرز هم هنگام جدایی از حرفه‌ای‌گری و شخصیت او تمجید کرد.
❤️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/101903" target="_blank">📅 18:00 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101901">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EQPkreYivvVvURckkyLxWTnPh-jjCPBiaTKimZVkNCdhhNudFBYICDWBBAWPyd93fv_8wUCsZZmIpVMY6eeOctKniRvtNni6Fe_7t_XpbnvbH1nYv2EmPW0H73GzBdxLUgO3Zm2AENm7v3kdrvKu6y2XBcCdNjKiofJVRnDpySPEpFuzgkCFTPFEW05XtMM8QYO4xgo-uVvQZwBUe6FfNfZc9-MaQr-SkrWsRi3PmsVOsJLg0cP6xxwzIkUxkJ_2jxLhyTF-0EzE4WZida_Ira40RrfkV74bEUnlMTTCxJXkk0u8CzpMs8DAJr3xdUQ8S_yapbdkQ65Njs7Uib_KKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/au8g5U9jxUVSpCtLsBBBiki1oOMR3SiyMNy-EGwQYaXvdXGFiHHi4bTKRWP_FeZR-MfD0TY0X6Ca_eHyyUHfrQwrmA5klIveZfPruP-a9Igpx-pO7E-0BNIiOOBh-8RgMRHAHSp6dnJ304oSb4SdMgpcneF5dVvcIlW6Gf2G2k5h-6HJJ0qiSk2B2YnWG40tuTMXkh2qAEhiaNACiQ8M8Mb_otOHvKxbNfMK5I_qUhI-mYFZ0ruyrmMKv_HWRuuYHvywKfm1C4_zS0RhLdNm821kPDKrB84eGI7eeADXfy2QmskykML6iygGIgl9swEL62SXnggPXF7PeIwNJPvT_Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎙
یان دیومانده درباره گرفتن یک پیراهن تقلبی کریستیانو رونالدو در منچستریونایتد به عنوان اولین هدیه تولدش:
اولین هدیه تولدم یک پیراهن منچستریونایتد بود. توان خرید پیراهنی با اسم بازیکن را نداشتیم، برای همین کاملا ساده بود. خودم با ماژیک مشکی پشتش نوشتم "کریستیانو رونالدو" و شماره ۷ را هم اضافه کردم، چون می‌خواستم به خودم انگیزه بدهم. هر بار آن پیراهن را می‌پوشیدم، تصور می‌کردم خود رونالدو هستم. فقط می‌خواستم از همه بازیکنان دریبل بزنم و تا جای ممکن گل بزنم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/101901" target="_blank">📅 17:43 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101900">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b492c31a81.mp4?token=LxnnaTRxa_YC9WhPh-fbZ4dhKQIUQDUn-jd3ta3EbcCIVRPF31OxiA8ldRGnjPQBDvnWc0mmRApXhKsxAUagQQfsnZBH5y9mBEWmD-NybVV_s4qCZ-xYjkU-Fi_6sVNJ4bPGaWaRZClRkYWR6Daj0x9Iha6jmrCg6duS8XqEKLx_MjwpLUvDojiCNfnXGNryoaU-r44VzOCGUipOMs5y1DKZZOuQ_kk_ZEi--JaLvLwpwSiemVF9GgPCpvA9UsK7h-u7UkaB-GkE1lItxGoaAVj-yK6LVtF18RI_i1cX2L-pSj6kYdOPfYhBelzOF5E9sFHHRhQQXwAPdnfsBh8knA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b492c31a81.mp4?token=LxnnaTRxa_YC9WhPh-fbZ4dhKQIUQDUn-jd3ta3EbcCIVRPF31OxiA8ldRGnjPQBDvnWc0mmRApXhKsxAUagQQfsnZBH5y9mBEWmD-NybVV_s4qCZ-xYjkU-Fi_6sVNJ4bPGaWaRZClRkYWR6Daj0x9Iha6jmrCg6duS8XqEKLx_MjwpLUvDojiCNfnXGNryoaU-r44VzOCGUipOMs5y1DKZZOuQ_kk_ZEi--JaLvLwpwSiemVF9GgPCpvA9UsK7h-u7UkaB-GkE1lItxGoaAVj-yK6LVtF18RI_i1cX2L-pSj6kYdOPfYhBelzOF5E9sFHHRhQQXwAPdnfsBh8knA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فران تورس تو تعطیلات در کنار بکهام و مایکل جردن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/101900" target="_blank">📅 17:32 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101899">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/51f2886d75.mp4?token=PY9CW8FUoFFHNmsJQtfrBO8eBB0w3MCAZhachXzsAJzP06bfxg7BhTBZP3JMsMT2eZuw9YiuGO1cugkCFj_rASdnyT6l1ukrbIaxp5XqWw0RuyJJ75KloK2TZabHavKes0HNtbkffgmIF4ybvi9wrlTettZfIV9aYaAlj8DEAkrFXE7CYNelrSw10wmf9kOP_KxKIrimHG5EeMR7gr20DdfanF2U4hUPeJ9KRtnvq9TNRrJAwHPk2yb8pLQvd_Q2pOFfWvtpRkQM_tv4JpzDxFLPUzbr8YGOWFBtsuuj6KQ2uCqRbb39N-odX8X6eEAY0l3IBgif64O1gpUNrCipKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/51f2886d75.mp4?token=PY9CW8FUoFFHNmsJQtfrBO8eBB0w3MCAZhachXzsAJzP06bfxg7BhTBZP3JMsMT2eZuw9YiuGO1cugkCFj_rASdnyT6l1ukrbIaxp5XqWw0RuyJJ75KloK2TZabHavKes0HNtbkffgmIF4ybvi9wrlTettZfIV9aYaAlj8DEAkrFXE7CYNelrSw10wmf9kOP_KxKIrimHG5EeMR7gr20DdfanF2U4hUPeJ9KRtnvq9TNRrJAwHPk2yb8pLQvd_Q2pOFfWvtpRkQM_tv4JpzDxFLPUzbr8YGOWFBtsuuj6KQ2uCqRbb39N-odX8X6eEAY0l3IBgif64O1gpUNrCipKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هر شاهکاری یه کپی بی ارزش داره
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/101899" target="_blank">📅 17:30 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101898">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5fe82274ba.mp4?token=qmpct6rI3jTPmW3R995pmGMfuU9FsA8OijRtMA34oLGdHJTpJogReF7BK02ZC6T8BtxakCCJ2HQhfz0H1z5mWcmpipXq6Zl4iOIEjA-5Z-Ta9d6-ZI3SOxaIXsRxkWz2sME9eo1nhzX1MBFOrA3xNsPoXeLCWKUig548Km7Sna8sG8GtkxrOGDQ-jgFFqmrmkgg--mjNsgc6EMqYusbEVoJvW7oNBSqJl4RSfDcfxgzPZecub6wdqJX1g2YJovLcRgDme0qMC-eLUqWuvYITowLocPZ7Pa6eIkJ8c-iVHFc2epCB-rXIYuPB5bRuKki6X6pk3VB38N5MmT88Lgnj0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5fe82274ba.mp4?token=qmpct6rI3jTPmW3R995pmGMfuU9FsA8OijRtMA34oLGdHJTpJogReF7BK02ZC6T8BtxakCCJ2HQhfz0H1z5mWcmpipXq6Zl4iOIEjA-5Z-Ta9d6-ZI3SOxaIXsRxkWz2sME9eo1nhzX1MBFOrA3xNsPoXeLCWKUig548Km7Sna8sG8GtkxrOGDQ-jgFFqmrmkgg--mjNsgc6EMqYusbEVoJvW7oNBSqJl4RSfDcfxgzPZecub6wdqJX1g2YJovLcRgDme0qMC-eLUqWuvYITowLocPZ7Pa6eIkJ8c-iVHFc2epCB-rXIYuPB5bRuKki6X6pk3VB38N5MmT88Lgnj0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زیر ۲۹۹ هزار تومان با ارسال رایگان!
🥳
با سرویس سفارش
یک نفره اسنپ‌فود
غذای مورد علاقه‌ات رو با
همون کیفیت
ولی ارزون و به
صرفه‌تر
نوش جان کن.
😋
🔥
از اینجا سفارش بده
👇
👇
https://i.snpf.ir/wopv1
https://i.snpf.ir/wopv1
https://i.snpf.ir/wopv1</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/101898" target="_blank">📅 17:30 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101897">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e5e82a980.mp4?token=mCa5uDg0OBMos1utMPpwrEJfkzX91Pw0apqlDV_GU1tCRXhTbKIBDe0xpXjeQF-9VdlbjaRb8rH0k1KqSYCrM-Vw-AjDSFA875cRGD0rIKf4iJxwory653O_xYxsp3JFu9h2ZktFIoz5yw22EciQHy1vkK985GhBK4VbHBGMqDfe87aTp-YDWBJNYK0Qd3j6MXRT-zmgO0iovzAi43St212U4uQRE8-KOkXVYq3_xAFzHa4zoaSBc8WMQj0koX0I8sjlRWAI_MIvUgTxMyOox8h7zKXDB_bSmAzotFyB2QWKU40ztlVZiM39vCZ4DQD1c6X502M48RqJOgCVNNck7oWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e5e82a980.mp4?token=mCa5uDg0OBMos1utMPpwrEJfkzX91Pw0apqlDV_GU1tCRXhTbKIBDe0xpXjeQF-9VdlbjaRb8rH0k1KqSYCrM-Vw-AjDSFA875cRGD0rIKf4iJxwory653O_xYxsp3JFu9h2ZktFIoz5yw22EciQHy1vkK985GhBK4VbHBGMqDfe87aTp-YDWBJNYK0Qd3j6MXRT-zmgO0iovzAi43St212U4uQRE8-KOkXVYq3_xAFzHa4zoaSBc8WMQj0koX0I8sjlRWAI_MIvUgTxMyOox8h7zKXDB_bSmAzotFyB2QWKU40ztlVZiM39vCZ4DQD1c6X502M48RqJOgCVNNck7oWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارلینگ هالند از مزرعه یه پیرزن استیک، عسل و شیر تازه خرید و بعد رفت خونه تا خودش دست‌به‌کار بشه و غذاشو درست کنه. فک کنم هالند بعضی وقتا یادش میره که یه فوتبالیسته با میلیون‌ها دلار ثروت.
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/101897" target="_blank">📅 17:23 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101896">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZsTKCBwkYsqoLNYp0-EDvOaBbIfWH81rM0KWvQnzH35goTqmTtn3rEJKMyEGUTbhL8B0vtM325JN4lpwVDqXgLJaSa5s-tgt8574u_LmRm0Okkw_eAdMHZmrWqTGw1THpR-iYBj06bbBUmLCHVKTdQ3xJiXrHkO6sxQowJveDFsmycaLA5whKXVuWEtybTwdIZkQsOxoeWLWDVRdEUrrdYogDjMgpwf_dTdlcbYy4DjdcQuSjzcrLJymFFrfKZKfrFRzyWVPP_d0MGJZW-IBRUVbwxGnuHJ3wKcn5wdDgWvpqcS186HCMTzm5D_wdzQeC-TuRus8yZnUAc5fvU31AA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
دیوید اورنشتاین: آرسنال در حال بررسی احتمال جذب وینیسیوس جونیور است!‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/101896" target="_blank">📅 17:17 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101895">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZLW-95yeKHLrkEdOdV4GkK0FjAJS2FA9rXM-1HVhCcNziIKTy0Ql6u5ab08qkpQabI2ugOhqdXWRQ8p-vupfD9NPZuNoQju37P85r_ZIB_hBLj2ecXGynOUae-VeIMbqo3F91DDebU_nBMI2hLr6i_YkFcTgf1aoGBZk0H0p2p6aSwvNL1cpEh-dH6LTxLgBGLBsS_SFzWLb-leG-H_r30Zxk597xr_wRBD7H3j2woAJL2cs6fGtCX6p9ozUSMlg8AvTn3YHnUA7D69nfZHlBuqqh8uCy065XQb9uJ4guNq12LN3HOKcX6URt3sX31LGGQUdZK9x5zySMHFmWjjG9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
بن جیکوبز:
نمایندگان وینیسیوس جونیور، این بازیکن را به لیورپول پیشنهاد دادند، اما باشگاه به این پیشنهاد توجهی نکرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/101895" target="_blank">📅 17:08 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101894">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/36c582a64e.mp4?token=gClpTm9CQO7ewkTQw4h7eyEg0s3eAxGjz4TRfpaqY1G0oOWMFTR64OmAeSIi8DH57IBSPr4zbGLTA49WP6bV279I3ltNpgRaSYGE12-sBzHCLkv-aeIhzXAi8W_xWpcwmHiX6XV5AXXnAXZAdBI9kI5pd37v1flyegTVEo7ayjghUj_6vqDoGfMWLWEsZchRcdJiokSRpzRtLqB59-N9n_qmc8vWdnzOew_iZ4pu2GuiSKUiWoWUw34SDDCoM-G9EzktWnZ4oJ1i1zX-z_qeO9hr8g9QRFJXnZwdPqqHZj_cWu8Gjo-SqpyKRY_WMXPLZwqm8w8xMCK2va3jUnNKZV7loxS7EZOOaS3GfS9e5478BzuN_eBbG_rm7b4etJaT0vZVgj0W310pm0ORWt155jR-UyI6Qc4th0gvKkms037Nj73S8Q6bmRvXI978JKBb2DlVKHEomlMxQW8zY7NoIg2TqPi49suqlXje2fcjnMrqCSnQJGtn_SOSl9S5l6jYYpCO81mMjD6EDzn1VHVE_Ylx7vtTpuc7DdY5MUkfyP-mlSfmQ9ZxM2VjTQYZA5GQ0pcsG629UJzapTPZfjF8AJLEty9Vmqmo1Gm79jkXDGjZP1rqhLD3l7B-JZVdK6WYrYvgTbP2izDv1an1mePEF-XpjERdwXhS2HNCtBSwvjc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/36c582a64e.mp4?token=gClpTm9CQO7ewkTQw4h7eyEg0s3eAxGjz4TRfpaqY1G0oOWMFTR64OmAeSIi8DH57IBSPr4zbGLTA49WP6bV279I3ltNpgRaSYGE12-sBzHCLkv-aeIhzXAi8W_xWpcwmHiX6XV5AXXnAXZAdBI9kI5pd37v1flyegTVEo7ayjghUj_6vqDoGfMWLWEsZchRcdJiokSRpzRtLqB59-N9n_qmc8vWdnzOew_iZ4pu2GuiSKUiWoWUw34SDDCoM-G9EzktWnZ4oJ1i1zX-z_qeO9hr8g9QRFJXnZwdPqqHZj_cWu8Gjo-SqpyKRY_WMXPLZwqm8w8xMCK2va3jUnNKZV7loxS7EZOOaS3GfS9e5478BzuN_eBbG_rm7b4etJaT0vZVgj0W310pm0ORWt155jR-UyI6Qc4th0gvKkms037Nj73S8Q6bmRvXI978JKBb2DlVKHEomlMxQW8zY7NoIg2TqPi49suqlXje2fcjnMrqCSnQJGtn_SOSl9S5l6jYYpCO81mMjD6EDzn1VHVE_Ylx7vtTpuc7DdY5MUkfyP-mlSfmQ9ZxM2VjTQYZA5GQ0pcsG629UJzapTPZfjF8AJLEty9Vmqmo1Gm79jkXDGjZP1rqhLD3l7B-JZVdK6WYrYvgTbP2izDv1an1mePEF-XpjERdwXhS2HNCtBSwvjc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔙
🔵
۱۲ سال پیش در چنین روزی، دیدیه دروگبا برای دومین بار به چلسی بازگشت؛ اسطوره‌ای که نامش برای همیشه با آبی‌های لندن گره خورد.
👑
📊
آمار دروگبا با چلسی:
🏟️
۳۸۱ بازی
⚽
۱۶۴ گل
🎯
حدود ۸۶ پاس گل
🔥
۱۰۴ گل در لیگ برتر انگلیس
🏆
افتخارات با چلسی:
🇬🇧
۴ قهرمانی لیگ برتر انگلیس
🇪🇺
۱ قهرمانی لیگ قهرمانان اروپا (۲۰۱۲)
🇬🇧
۴ جام حذفی انگلیس (FA Cup)
🇬🇧
۳ جام اتحادیه انگلیس
🇬🇧
۲ سوپرجام انگلیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/101894" target="_blank">📅 16:57 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101893">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lz9BsfAMgPFKTouYyp8b855L3DetqKfV1sFLuQ5pL2cH7AfRmzD_yBqAGAgR7iBqCiJdYxPr8E2m4lzW9dMHaQom4qAPzCH6e07P5D79rgay9paLzwt8p461WkwVfI0fYH0BqYXBsWUOu4BzmQKGybFYjOfI_W85uEViWIdOSd76TyuBGoZRqTB-rQKnZQq9alKGY7bsQTMzzONxjVmtEc655qEcMFao4Gl_csXpUbmfitWTMop7dlo5P2y7lPWb43UkkC55wGNHw0owY1KI5029EfBV0SNi5gATgX_cnDLBB_wFf69SzrDsrfh0s5fSmyim8fP6HIN09YVFtsusMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارزش مالی جام های مختلف
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/101893" target="_blank">📅 16:45 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101892">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚨
🚨
دیوید اورنشتاین:
آرسنال در حال بررسی احتمال جذب وینیسیوس جونیور است!‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/101892" target="_blank">📅 16:19 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101891">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a105d81352.mp4?token=Go_TuzcxCtCNv1VbtxKq1M0JAKrp7wGHk-3gwUUz4-yLWYMaUK87iUSx9dJATiqhOXDMm3IcUGSErvtPFm0LZCliNrM1LQ3KkEL9GZX5IKSzxns3r6BBYCLX83JkFojuJU-i0ruf-mQjBlicwJfLZqb3wXHlyKmEGorwA_qaBqFLGwjW8SEUGfIhopyXuNMOtG731qA4dmkRNSpjCVH_EDs1t3gzSxTCNqqYQxC7IesUULGplut2UJxpKZVt1AXDR1Fo_K4LWqOBtWiFDaIDIbWZLkhu9yM3V-GpeageBQ_8DPdeUvVxqBVMmpvFalM6ySisqCCBVfyxKIKaUfG4xQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a105d81352.mp4?token=Go_TuzcxCtCNv1VbtxKq1M0JAKrp7wGHk-3gwUUz4-yLWYMaUK87iUSx9dJATiqhOXDMm3IcUGSErvtPFm0LZCliNrM1LQ3KkEL9GZX5IKSzxns3r6BBYCLX83JkFojuJU-i0ruf-mQjBlicwJfLZqb3wXHlyKmEGorwA_qaBqFLGwjW8SEUGfIhopyXuNMOtG731qA4dmkRNSpjCVH_EDs1t3gzSxTCNqqYQxC7IesUULGplut2UJxpKZVt1AXDR1Fo_K4LWqOBtWiFDaIDIbWZLkhu9yM3V-GpeageBQ_8DPdeUvVxqBVMmpvFalM6ySisqCCBVfyxKIKaUfG4xQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بهترین مدافع جوان، دوست‌دخترش خوشگل
پسری خوش‌چهره و بی‌حاشیه، قهرمان جهان
یه مرد دیگه چی از این دنیا میخواد؟
😍
🏆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/101891" target="_blank">📅 15:49 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101889">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oYZVoReC17MiwQIQ-wNA_Fc24Lu8NeANB3GCQfnEaLeahTCR3CgTWZbgwihXZJpVbXjemqcx5Map9ipdgotQBnwzX7anLDw6r2SH3xTMQ5P15_Eh5sWazTAX2X_fyvUP8m1oJl2chwkO-0dmoHtqaSFDdvMXvbQocqain7GpPgYhOJ3I4HHxABggaxMlir3qNyFuIma45qT_avVkJdG4NKMe9Ai04nElUkI_JyzsdPa1u0bEMvg0eISNmBm59l8ZXfsVSh5OXWoNkA6roItg-vHDTQ9PTmyzS0nYc2RjBCOwCtha6hJLj5UNmtBvpyx0xHT8GJndumrkXf-8bPt0wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I8VQ3JIcBKvnUXOfjgSP4NBi4DGURSK-MIp-ny9cNTAKaaBgrV8bM3FptUpDGOihon3Xo8UtKOLd-UT0b267xTUR28gbSvPtnRs0VwaiYsdbsedKfRXyABu15BtlgCLuoh4dT3VpaUj9aprvy3xWsW_bU4_FoPIeWnErc3Pwa2sN1WZP9BQRGNycYLCS0-BekEzJtiqHRnTNkZmIMpRW9-4kV9MI9Q89RnBLjFQ2L5hbyDcM8QZ7PL3Oz1fV4ze58sYS2h-otadkWTi8bstba2no6JJwA4XjS9b3jxGTaY8J4zzMhXP-NtqXY3uDbF2YJFv0hdVUZp5TYdf3Pjkojw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
⚪️
رئال مادرید و ژوزه مورینیو این بازیکنان را به عنوان بازیکنان "غیرقابل فروش" در نظر می‌گیرند:
🔺
کیلیان امباپه
🔺
جود بلینگام
🔺
فدریکو والورده
🔺
آردا گولر
🔺
برناردو سیلوا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/101889" target="_blank">📅 15:34 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101888">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lQO7PBVJeEh8ovhkSFphNo-nZkK5bdcTKouJSvWzZ1bRKiHqG6jBCco4Fq3P5BaSz6dwUAd1FpjUwYKp3QnBqvQFuegKIkj8RUz3dOZAx7SFQ4oSmaDy9xfVUE12Dwj--lvNu4yvhjmcC7q8xgiL6vSkDEIAr7ceqjc6P-QtB0H0aAwSXvt28rp8uMTP0wa8wgdjE_nBwlpOL8qn_ElY0hwCuwDL_CrTHbeHlknOxc4Y8mpxN4O5EHDXF1-KLZaYCqEN0gU190-pZWGrc9BH9wdsASKFVePhbZsDjHSKMKE0iGQr6wg_CDQ2swHRtRtu7gXmpjMpM558dHm-H2ZTgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
فوری از فلوریان بلاتنبرگ: منچسترسیتی به صورت شفاهی اعلام آمادگی کرده که پیشنهادی به ارزش 100 میلیون یورو برای جذب یان دیومانده ارائه دهد. اما تا کنون هیچ پیشنهادی به صورت رسمی ارائه نشده است. و مذاکرات با لایپزیگ همچنان ادامه دارد. منچسترسیتی به دقت وضعیت را زیر نظر دارد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/101888" target="_blank">📅 15:29 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101887">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cpWjd72S_XZ93GjX5eMbX_iRpfhZr4Z3l-S3nps6IdntSDWxP05229R93eiMcqI8oyPU8tUCzdn3NAtLNFj8WL-ylUbg_Rc4o7Z18dAcFtFP423BSOI7Sj3bPjn-KU0YuLh_nCJ89WEifz_jM7qR51rT7eS3A460RMnWBU36GAdS5VUEpNlmQ7CdMXx5PJv_JBGHQZftLlPU2wxQVGP9oPMKFfgeI2Br3JD2Fdsi1buMGi52_-_KeXxqM3Im-Hn8sRYBmIVAMj9y47jxUa6k6h8OCqmb03DBQjCByGukrzAjJ-1-mTdYRtoJ8aGMbGQPjuAwgR6eptCLirrZeQYcIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
هزینه تیم‌های پرمیرلیگ تا اینجای نقل‌وانتقالات
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/101887" target="_blank">📅 15:18 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101886">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rOMO-BSwRWTVVpyUtFM1qVAyDKHi8wJ1039ciQUNwU92kcjhl3tJJqL1_yxQ7wNBNvsAXvze6steWd-EgC7pGfoRnNWMPqFg-2Hfs7-b_aeAaM8a71FOrhQMvnEKu76F-WVpO6YETQbksF9l1WC6fJfs6Q7tzJUbBX6muSa3ndK6ufJaREWfrAbUhBDOEaU4F46vfo0FqC6kJNg4a4BUMRJ-HLpj4HC62iPM-n1cr-JRRiulfpxIUsC8ffzFnXxKjNK0xYjFJx3Z-WYvniehF4B9kKts8RhxkL4phMaiwZeq54iur6GskcI8udw06f_Q249PuysSFGst5J77huBwGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
رودرا: اصلا بعید نیست که اندریک این تابستون رئال رو ترک کنه، این احتمال حالا جدیه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/101886" target="_blank">📅 15:02 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101885">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cLmeOGR2ZsQDcVvEQaeaHdGIuLkmJ-v4xu4aMO6gFf5nX2i11qaw0j1cwKZdaMAwIdLHoP_jCj_4tgbDTlLqcF012RBaUgLLreU_lsaPDjcV3q59j3Eudw84_buwWT52CWkwb8CL04lHrSJoz-LLN1RSGY8E_tr987RD2Vfx1i3iuTVRI5z3ScPIPYSUVd7h8qS2BeE3oHfwCXm_GZbIu9nWnB7Lq1UAxWkWUJVkL4_zA_Po6m6eZaOh_0GMgZEpumIGQkt2B2S7IhLrdqwmweeVqwI19E29ZDoSPYPphDH7JaiSUIR9fZsYmEt4nPGqVH8CCdyCfFKCkveVQ6c64Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
سانتی اونا: رئال مادرید از شایعات مربوط به انتقال مایکل اولیسه در رسانه‌ها استفاده کرد، در حالی که به طور مخفیانه در حال مذاکره برای جذب یان دیومانده بود. حتی آن‌ها به طور پنهانی به مقر باشگاه لایپزیگ سفر کردند تا این انتقال را نهایی کنند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/101885" target="_blank">📅 15:00 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101884">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f29886b9b.mp4?token=iyZpwMS8EIFSYKCGP13nD0aou2XhAY9F_6OOahrwD-g25d7sR8o6FQbesKqUzh-M2X_bdCnDra_yZ42qhw5SSgcAuzSFo3Bc4obosrkYLqBJ551-sYNZ76eSkynpm_GQqeq_rCl4GAFOBqzQZ7L3zqzOY5JrXp6RtK1hJMLU4bM_47XrzUKdHH2d0ANBa7b0_QJ_LtzQD7907DuE3ODctKX0FImD240dcgERixJVg_EbipPYhLbaCzhTe0ZVJ-v7Odv9ixhcn6-qvi-6Ugs7eKRkPDZqupgtQ0IXUesvjYfEo1fBwQ0y_-IAgcOLKZSWXEcm4YzkkKCCrU8XfpTjAA2cgF09NBUwoscArbb5QlGx6mwdvPAOj5mMTXVwDoW_0hmTj_zrs_dwuYmcNkisSOBNx9-VrQMZ-BDE_sMOzcgeVWcaCajpZgoYyaQyErj3431iQ_hZatbfW--wuleDIHzhD_KeqC_FwE4uP-qyhy8KQKHjzQCJRQ0ionV7ljRG40br1YiVWyEwverpTHih-RZQ9jjZsC3Uif_-CMxi1ePIER7ENnjeEFS7CZNBGJH7zxWulZSrk7bQ0IWzkIksGJTZ3WuoMD57JVOwOnzooqYWAY7gOJxImpva_FCDj8RZpeI4kp06mNkqxiIVXEB9rKFccnAfKOHPjybHd6ldFbo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f29886b9b.mp4?token=iyZpwMS8EIFSYKCGP13nD0aou2XhAY9F_6OOahrwD-g25d7sR8o6FQbesKqUzh-M2X_bdCnDra_yZ42qhw5SSgcAuzSFo3Bc4obosrkYLqBJ551-sYNZ76eSkynpm_GQqeq_rCl4GAFOBqzQZ7L3zqzOY5JrXp6RtK1hJMLU4bM_47XrzUKdHH2d0ANBa7b0_QJ_LtzQD7907DuE3ODctKX0FImD240dcgERixJVg_EbipPYhLbaCzhTe0ZVJ-v7Odv9ixhcn6-qvi-6Ugs7eKRkPDZqupgtQ0IXUesvjYfEo1fBwQ0y_-IAgcOLKZSWXEcm4YzkkKCCrU8XfpTjAA2cgF09NBUwoscArbb5QlGx6mwdvPAOj5mMTXVwDoW_0hmTj_zrs_dwuYmcNkisSOBNx9-VrQMZ-BDE_sMOzcgeVWcaCajpZgoYyaQyErj3431iQ_hZatbfW--wuleDIHzhD_KeqC_FwE4uP-qyhy8KQKHjzQCJRQ0ionV7ljRG40br1YiVWyEwverpTHih-RZQ9jjZsC3Uif_-CMxi1ePIER7ENnjeEFS7CZNBGJH7zxWulZSrk7bQ0IWzkIksGJTZ3WuoMD57JVOwOnzooqYWAY7gOJxImpva_FCDj8RZpeI4kp06mNkqxiIVXEB9rKFccnAfKOHPjybHd6ldFbo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇷
امروز تولد هالکه و به همین مناسبت یادی کنیم از یکی از ضربات سنگین و پشم ریزونش.
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/101884" target="_blank">📅 14:52 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101882">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jLCuQB16fV6XI6qiU3MLO6lZttQECUx5_wJh5AwTfJ7TcxYC4bISGuAlHXOQhTkP0LIl7MERUJdHxOq8M0_no5o-DhMxGnGCB3wlTIMKN6isx74JqVGGJ1TvxV52NMw6j6oh148sYOWzEZCcBbPkM1o_ePZ0HhgLcsBt-DKJ6GkOtJYE810S2a5ujsvmXvd4DqmGdAnAv4RlYCyrAQ_7ze4ICUoJrmi1je4qGYPHh5g1SmhWrYc2bVDJ1hVbrwPxzGAEdlEYxw7huqh00bsShAJ4cGIgwFQUmaQIhpiISwwDAwaMXo-Gm-gXLcT2rxC1h42qPdfUAZVzWCR2Z1yBug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f6342fd750.mp4?token=Yz4qFvpjXLqKpvXDSvWM4PMn__rmUzXTT0Tx2qWEEn-C60x6o41-xHjdYgu0VRiHH1gKGZPm7DdUaDEsISU2qohxodJNhMO_zyY29nHEU6_wLJTophZoSaa8C-MIvnjN4oPw-8RhgdT4Oh3MjyHwXY0l4PR5N-85u7pRZS355amA7iHDukX2sZR_Lk80HNpWG3CI_f06VUDIB0QEb5FPU2HGJa8auXgEI-Eb0FcIQTth5GCtUhgfZ_X3TtTyPLHhVeNgnwKDhXVWqCewSj7a1bmMnJgNw1OV1Gwa_FX7kM5n1TvDcyyBIj0mtWAHDJGIm_xqi6M50b8-DCO-5T6vHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f6342fd750.mp4?token=Yz4qFvpjXLqKpvXDSvWM4PMn__rmUzXTT0Tx2qWEEn-C60x6o41-xHjdYgu0VRiHH1gKGZPm7DdUaDEsISU2qohxodJNhMO_zyY29nHEU6_wLJTophZoSaa8C-MIvnjN4oPw-8RhgdT4Oh3MjyHwXY0l4PR5N-85u7pRZS355amA7iHDukX2sZR_Lk80HNpWG3CI_f06VUDIB0QEb5FPU2HGJa8auXgEI-Eb0FcIQTth5GCtUhgfZ_X3TtTyPLHhVeNgnwKDhXVWqCewSj7a1bmMnJgNw1OV1Gwa_FX7kM5n1TvDcyyBIj0mtWAHDJGIm_xqi6M50b8-DCO-5T6vHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
هِیبا ابوک همسر سابق شرف حکیمی:
وقتی سال ۲۰۲۰ با اشرف ازدواج کردم، عاشقش بودم اما او انگار به من شک داشت و فکر میکرد دارم به او خیانت میکنم. وقتی دیدم نمیشه رابطه رو نجات داد درخواست طلاق دادم اما اشرف اصلا ناراحت به نظر نمی‌رسید! بعدا فهمیدم چرا؛ او تمام دارایی‌هاش رو به نام مادرش کرده بود و چیزی به نام خودش نداشت. این یه حرکت حساب شده بود و واقعا شوکه شدم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/101882" target="_blank">📅 14:37 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101881">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/356f27159c.mp4?token=iq1ZofRWxkgxODg4tWOHbh4HvTN0cGO_WRQV6fCBci6dcnq79ALYCnpqQgotaVFj8_NOVnYqHOKKoZh6dU3DSuMlZbImlbUT8T7_mE99uJpUrJstdP0Hj-B8b5U1asxqSzwD2ppAx1RUvCCCZ7EgeCVpcbVGrndRhVcI_ACK7h6XWqVAwOVOltyLkg2syf0fYL3HUH6l-bUyPYZwAotz2wiTKem9yBfO86dcDxozdM9jWjAN-Z6Z_mVt-Hn-h5DakFG8EuLR2rMrTQk4Dq7owCtEI28GdnullVgRBU69Vf4nlEVRu46ls9DEMZ5NAppvilTzcQrg09Stnj4kUqPj1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/356f27159c.mp4?token=iq1ZofRWxkgxODg4tWOHbh4HvTN0cGO_WRQV6fCBci6dcnq79ALYCnpqQgotaVFj8_NOVnYqHOKKoZh6dU3DSuMlZbImlbUT8T7_mE99uJpUrJstdP0Hj-B8b5U1asxqSzwD2ppAx1RUvCCCZ7EgeCVpcbVGrndRhVcI_ACK7h6XWqVAwOVOltyLkg2syf0fYL3HUH6l-bUyPYZwAotz2wiTKem9yBfO86dcDxozdM9jWjAN-Z6Z_mVt-Hn-h5DakFG8EuLR2rMrTQk4Dq7owCtEI28GdnullVgRBU69Vf4nlEVRu46ls9DEMZ5NAppvilTzcQrg09Stnj4kUqPj1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هالند لاشی تو مراسم عروسی دوناروما هم نتونست جلوی خودشو بگیره و مهمان‌ها رو وادار کرد «حرکت پاروی وایکینگی» رو انجام بدن.
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/101881" target="_blank">📅 14:21 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101880">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DG4Tz6Q7e6IXkU76XILEwpuW8sPnH7Ro-tHVJuXAiB5Y3VTB0-GUWtaXOiaTGKiQhm5vvjAMCM4I6PijOR0QwWzSBSsj-CPIEZmWxgPUPxjirWI8eaJ3a8CLlt50Tq6cKtRwlF0CuE8kVippslssPqsDukrJksX1lhnDczQtyk2pb6n9keYYY6ZbgRV6mEkWNDYRD32OHK1wRo5GH4V44tOA9G16sGcU44d5e1kxLBZ9Enk3G-3N6Was7ts0dc54I0yMLaR1fcpCvQNuPh7I88VTVKlTzbxhc7XqI9O9jjq64mzHUaVgzNNT6gipIBXppFNxlR__qVf8TaYNdhZEsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
خط‌حمله نیست که ماشالا فلیک رفته تیم دوومیدانی برا خط‌حمله ش جمع کرده
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/101880" target="_blank">📅 14:00 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101879">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ff0c27865.mp4?token=dVbH2E1Ej4xcP7cvULm1vjC_LswvJWYkS-a6DwLcsZbhvr_HCwZtqivKVqPiVvqoabw-Txz1ZzPX4nNI6GvccjnQLvkIQA8ALftUTJalK-62UMCNw_uyz_dZTlQPFOEgkU6OvVWYvTi77BEGGIp2vyD6MaRrrBVI1Fhxc-PeQvRt1c1sjGqWrGJzU91-IdM7SWeTJ8D18T_oHTy0uv0NE_L4AGddkxA6UW2DJNDm-CuOH5vNa6jliQ17KDNq_VHBFJWnJnmwUlHsKvCy0T0XaOI4nox4XaWRMNtsSdsLf8qCzVyelTd3IlV4dWcGa44phjBc0e2_ggUwvZEKpLvg1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ff0c27865.mp4?token=dVbH2E1Ej4xcP7cvULm1vjC_LswvJWYkS-a6DwLcsZbhvr_HCwZtqivKVqPiVvqoabw-Txz1ZzPX4nNI6GvccjnQLvkIQA8ALftUTJalK-62UMCNw_uyz_dZTlQPFOEgkU6OvVWYvTi77BEGGIp2vyD6MaRrrBVI1Fhxc-PeQvRt1c1sjGqWrGJzU91-IdM7SWeTJ8D18T_oHTy0uv0NE_L4AGddkxA6UW2DJNDm-CuOH5vNa6jliQ17KDNq_VHBFJWnJnmwUlHsKvCy0T0XaOI4nox4XaWRMNtsSdsLf8qCzVyelTd3IlV4dWcGa44phjBc0e2_ggUwvZEKpLvg1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
صدایی که این چند روز تو ذهنمون پلی میشه:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/101879" target="_blank">📅 13:40 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101878">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qJdsF4KIEdFA0V4YPQtg3lbdXsNAZd3A1bNNh_-Gcl4X8QQ5Zfg0-ACMhmHKayCOh9ckqMLZCG902lsEbMiQ1orfOXTV1duBvppIt4Hcz6Q96uBrlCdNJhDDu0S_p1rPv2uBkMQxPHq2uYqbRNJJ6SmHZV_uAIBJd0DCTtWUl3t-Nn0rnvvAstUCaHW5beLx13mcUuwel1oU_IC5lIYc0y73R9J78wSvFJrCcl86_37pEfrGSZf5IHp3WGFr_nC9BsWmsLl7z6Jlit5hHGYVpLCPTLiFQQsgz8EMQTniQ6RXFtHIf3f2kBFKj-9LMWvdJjOpLSRFwp4A3E8hrwLuqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🤯
🇪🇸
ترکیب‌احتمالی فصل‌آینده بارسلونا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/101878" target="_blank">📅 13:20 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101877">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc2d82d4a6.mp4?token=NzdAVep4JiBglX66UlUaCrLZgp8L-L2q-ifljXvYL0K4CUzw6eiNkO-D5QaB868eiK_oWwYjXZ34xYxzBNQde_wSQbon0K_Ur3mzGchxnxa6UR0zDhJLDE3Z38PNn-La1LuAe0cTxsnzd6nAMxPuhIjr2oxWRKW2ZDTMexim0ystrDfIFjE35bHnyH9NuBBHMRtSyn54zkoShSJYmh7zHjDNpxpGeIYB_fvPXe41PFFZzA4ex6Ra2rgLvyU8FWlwybURJTkaVjRhy88yd3547qhj_5pP0VpqXxa-lGjtBXGUjSDN7_qIPmrexsb5eINkNlBEXPePT7g4RWYTExsDEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc2d82d4a6.mp4?token=NzdAVep4JiBglX66UlUaCrLZgp8L-L2q-ifljXvYL0K4CUzw6eiNkO-D5QaB868eiK_oWwYjXZ34xYxzBNQde_wSQbon0K_Ur3mzGchxnxa6UR0zDhJLDE3Z38PNn-La1LuAe0cTxsnzd6nAMxPuhIjr2oxWRKW2ZDTMexim0ystrDfIFjE35bHnyH9NuBBHMRtSyn54zkoShSJYmh7zHjDNpxpGeIYB_fvPXe41PFFZzA4ex6Ra2rgLvyU8FWlwybURJTkaVjRhy88yd3547qhj_5pP0VpqXxa-lGjtBXGUjSDN7_qIPmrexsb5eINkNlBEXPePT7g4RWYTExsDEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇪🇸
مرور دودهه تاریخی برای فوتبال اسپانیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/101877" target="_blank">📅 13:01 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101876">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/705177dcef.mp4?token=qSZJ9P00LMVAsO_1WctuA7uGdO77v0BMABN5qP2SuU-sQLXhUcPmYUZm_aUXuGT6AqAHqfBaqGu6Hn79spmOyFidLHb2FuVd7ciMcGCugoWHpKPJDpzU3hs5z1HQjuZz3lPbJpqnMC_jQcyBi11SQBtlDxyvh57PyzNfL4_77sg8B0iR3IzTRD_anmc6BdneOreSjtyETfVa0jCf-_c8gdgDZ9JWGOFuDrm7N5B9tqbguXDqEr16uQd9GYsui1FnQfY9Xb4s4FDksnulzX-x276pW-dWQ_WsLGzAWua4DmTyyykrEKRdr0tCtibrmA8t5F-HzTXssP_4fp6z4boNBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/705177dcef.mp4?token=qSZJ9P00LMVAsO_1WctuA7uGdO77v0BMABN5qP2SuU-sQLXhUcPmYUZm_aUXuGT6AqAHqfBaqGu6Hn79spmOyFidLHb2FuVd7ciMcGCugoWHpKPJDpzU3hs5z1HQjuZz3lPbJpqnMC_jQcyBi11SQBtlDxyvh57PyzNfL4_77sg8B0iR3IzTRD_anmc6BdneOreSjtyETfVa0jCf-_c8gdgDZ9JWGOFuDrm7N5B9tqbguXDqEr16uQd9GYsui1FnQfY9Xb4s4FDksnulzX-x276pW-dWQ_WsLGzAWua4DmTyyykrEKRdr0tCtibrmA8t5F-HzTXssP_4fp6z4boNBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
عشوه‌های مجری صداوسیما روی آنتن زنده که در فضای مجازی حسابی وایرال شده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/101876" target="_blank">📅 12:40 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101875">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mdXtKrrHbP4dZr2nfnkaZyzq3rucJKf1hEFzXnkKIawNCvLYVZhIAypn93QOZvu7MfyrXJUxqjk7n41kiT98Jkg-8sNL2b3kyV9pcrYhHuMpjpwG96O3nUxULUQfzn1Qx-DCKAVbTAurjNsq0rBqIDbYc_FlwjWxwaDvWMkL6KaZehzzEDYTScX2OTUKq39RxjEgoQJe0_0wBALZNcjeqrYqFFMAt2GFfmaRtsEfMCiIJi-69NL0cADHdB6LTY_Ph__uvyeaUJRzCF30sawSqNH90r02B67995gTL4Gx2ekJ84XdVuzJrciOQp8POczqlUPguISFbLmJasipJYDinw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
متئو مورتو:
رئال مادرید و رودری به توافق رسیدن
حالا رودری فقط منتظر توافق رئال مادرید با سیتیه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/101875" target="_blank">📅 12:22 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101874">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09d9c9fae5.mp4?token=fx0PkAutW9wuVUWELRcntTcDXWdkSwhycucCxfly6bVb2ze5zXe_D5J5zPQ5Blpe9ZTRWv8gVmj4LgbhAoLI1IbspWx82ML8ZhMNm3WkWu2hGdtHRHJZWMvkU57-al9tnDmOk_HRBu_WUeo5uPRkbLX3Nt_dKbL5n6SBWu3POUQ19PoZwlaXW6GW6lx1_95PCUcRNLMi3DAduqQawfBNchd-R84p4iv4J-G01l5Ql5RA1WH9qEhygbHWSxGpn3ZiP6e9YQumriYXHmCjsdAntpT0FtOCVNMIbHPySKb6jFGoKC1bUQ2bAFhiZX5ULt4IcYaA4REAjRuhReyS7_kEcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09d9c9fae5.mp4?token=fx0PkAutW9wuVUWELRcntTcDXWdkSwhycucCxfly6bVb2ze5zXe_D5J5zPQ5Blpe9ZTRWv8gVmj4LgbhAoLI1IbspWx82ML8ZhMNm3WkWu2hGdtHRHJZWMvkU57-al9tnDmOk_HRBu_WUeo5uPRkbLX3Nt_dKbL5n6SBWu3POUQ19PoZwlaXW6GW6lx1_95PCUcRNLMi3DAduqQawfBNchd-R84p4iv4J-G01l5Ql5RA1WH9qEhygbHWSxGpn3ZiP6e9YQumriYXHmCjsdAntpT0FtOCVNMIbHPySKb6jFGoKC1bUQ2bAFhiZX5ULt4IcYaA4REAjRuhReyS7_kEcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😁
🇪🇸
وضعیت رختکن فصل‌آینده رئال‌مادرید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/101874" target="_blank">📅 12:20 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101873">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9cd5ea884d.mp4?token=Iqi11d1y0sY4zTMeR1ah9mvzPTwuJtLdfJ0hloKw8Rhby2hFLBEcdq7S9CiRXHRBUeHnHejxnvLt40Oozr3ogZgDIEVryYpm9kt79rTBw-aoiisp75HX6Z-C_H1LhHs_Zm7GWYgdhxqlMsgoS4gnTVLZBPeUHPXgGlO-yi28uq-Dg4DH9yMlQh4L6EUbjLG78f33WyLK7HN_-L7lsQLLfGqyVW-Kh9zPMRghclONt5enI48LOACzCZRJuwtKXKuw2z0qv_vqyF2wr6EcmP6PVKx1Sn-wMeGyIQCK2SejqsgpYIKaYkzBLPu-o5YumR17MP5hTcn9Crpkrt3rSsZkrmai2YRyzbzoo0bO5RMIHG1Xwe3ssgTP4KcUqSCZoxxVnldims-UB1KOuY6jzV-0QtkQH9TpS6NkfQ9_unkCtoaX7_B6S-sk_hXJ89oLrv5Y6_mSj9r9Nt8A1xPifongtzKJ4TIr4Chu1aRtLsDqeKDLEPRUzyynuTMOJOZKV4uawxJdDCZZ8Zt_QqkjeTk9_GHByfZVOX5cWpNNHm4xLIacdr-mMxWnl1ClQbgW7OWtMbKLjQEgNPWmeVSooreVhiZYx07Z0F7HBX2j_tp6oTMve7VWyaXrDphvQ6tuyDRrFV484Flnw7y4mSWkYMXlCHOhp-uA0w99TiRKY6NNvIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9cd5ea884d.mp4?token=Iqi11d1y0sY4zTMeR1ah9mvzPTwuJtLdfJ0hloKw8Rhby2hFLBEcdq7S9CiRXHRBUeHnHejxnvLt40Oozr3ogZgDIEVryYpm9kt79rTBw-aoiisp75HX6Z-C_H1LhHs_Zm7GWYgdhxqlMsgoS4gnTVLZBPeUHPXgGlO-yi28uq-Dg4DH9yMlQh4L6EUbjLG78f33WyLK7HN_-L7lsQLLfGqyVW-Kh9zPMRghclONt5enI48LOACzCZRJuwtKXKuw2z0qv_vqyF2wr6EcmP6PVKx1Sn-wMeGyIQCK2SejqsgpYIKaYkzBLPu-o5YumR17MP5hTcn9Crpkrt3rSsZkrmai2YRyzbzoo0bO5RMIHG1Xwe3ssgTP4KcUqSCZoxxVnldims-UB1KOuY6jzV-0QtkQH9TpS6NkfQ9_unkCtoaX7_B6S-sk_hXJ89oLrv5Y6_mSj9r9Nt8A1xPifongtzKJ4TIr4Chu1aRtLsDqeKDLEPRUzyynuTMOJOZKV4uawxJdDCZZ8Zt_QqkjeTk9_GHByfZVOX5cWpNNHm4xLIacdr-mMxWnl1ClQbgW7OWtMbKLjQEgNPWmeVSooreVhiZYx07Z0F7HBX2j_tp6oTMve7VWyaXrDphvQ6tuyDRrFV484Flnw7y4mSWkYMXlCHOhp-uA0w99TiRKY6NNvIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇩🇪
اتمام حجت یورگن کلوپ با هواداران و مردم آلمان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/101873" target="_blank">📅 12:03 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101872">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/05d40892a3.mp4?token=ZE4CS7Jt9r2o4l38DsDGzpgyomEOaqLB_fjO1Bo1iYKBNyTDJEIUFhsfUjQRcaCnUkfr51lMIgf91Zqbq0CDUkCtQyv7y-osNOzOhDQ35g9PxROHRhLTdrS6JuaFPsNIzMJVjGPp8lLWUEOJdFGE45BPCHJik8_hnUQY7pswJf44LVFHGEsypY-2M4yfnGjp33yIHtv9fGPSywcgqYWQUe4AQr6_wGT9yxRQTVPoi1vwhWmAJwKl9xvSw8ocEJjce57W-G_XenvNDMF2nWi771hXTR5A-VhFQLSFguyZDcOD37gD1TE9vOJ-o3bIylZiRpYsynXzcGTMIk9uDOBF3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/05d40892a3.mp4?token=ZE4CS7Jt9r2o4l38DsDGzpgyomEOaqLB_fjO1Bo1iYKBNyTDJEIUFhsfUjQRcaCnUkfr51lMIgf91Zqbq0CDUkCtQyv7y-osNOzOhDQ35g9PxROHRhLTdrS6JuaFPsNIzMJVjGPp8lLWUEOJdFGE45BPCHJik8_hnUQY7pswJf44LVFHGEsypY-2M4yfnGjp33yIHtv9fGPSywcgqYWQUe4AQr6_wGT9yxRQTVPoi1vwhWmAJwKl9xvSw8ocEJjce57W-G_XenvNDMF2nWi771hXTR5A-VhFQLSFguyZDcOD37gD1TE9vOJ-o3bIylZiRpYsynXzcGTMIk9uDOBF3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
🇩🇪
خاطره جالب مولر از بازی مقابل آرژانتین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/101872" target="_blank">📅 11:40 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101871">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qmIwpgYLFvucn-8GayoGxc3QsyQqtfP5sGAzLoK2ELo24baGnO-N0DDTyL-0Jw0kj8jI-j7X-5m9tPIfnpBsWWaqheY2QhwNLZRPOhdKU9iTQNKgS8dC5xIXK59LBx5fbAGmwsrL03ujSqTpliMIGCkOm_D8cX2sExAZo9VdTR8rVYnJwFECey9pnrlXm0OCoKykw9xEPzrItVblSZ9nGTJTb_z88QuZTN_Ym_qQCrAO2huh5dH3WIHZ0IgVWknXkX87VFW5E4u2qeAnNNaoLEjmsEz2xpA0O6lx4A2tFjycZhcdXzi7JnmI-ChnpckF1E2kDs3Nfu-AZRnCXg6bYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
لی کانگ این رسما با قراردادی به ارزش 40 میلیون یورو از پاری سن ژرمن به اتلتیکو مادرید پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/101871" target="_blank">📅 11:32 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101870">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XZ9z-FB5PR4q5-F_FRFd6kTvpa_b4kN76MaRThF1In7etNOFKJH-7i4dRSWl--lLebb_y3jj4aYVoTxHRyMvN68BaCQRnY2b_Yz-GGCq-ZoW02Eswkm3lthFmqFblHwhx6m87ubEskCric_OoKN5UxM75D8k7YuYwu8NkAo0aOA0Eudni25TzuvjxblszQwaVrVD9FXzQa3raios8u2ejplLeHUoFCSXhdX1Rtg4n7hqkIa3mz4_OZZgoX7crWPEleg6tAn2mq8r_bPFr5MWTLO1yL4sH2VQ_AHMKjGWKdSgDUqNyzld0v2q8ozF44zKdaWRALfEBln0jwEduu2pBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇧🇷
تحقیقات سه‌ساله فیورنتسو سانتینی، تاریخ‌دان ایتالیایی، نشان می‌دهد که لیونل مسی ریشه‌های برزیلی دارد!
بر اساس این گزارش، جدِ پدربزرگِ مادری مسی در سال ۱۸۹۹ از ایتالیا به برزیل مهاجرت کرده و پس از مدتی خانواده به روساریوِ آرژانتین نقل‌مکان کرده‌اند. همچنین در دوران اقامت در برزیل، نام خانوادگی و برخی از نام‌های کوچک اعضای خانواده تغییر کرده است. این گزارش تأکید می‌کند که پس از مهاجرت خانواده به آرژانتین، دیگر هیچ سندی از حضور آن‌ها در برزیل وجود ندارد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/101870" target="_blank">📅 11:32 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101869">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/917b2cd572.mp4?token=QhsWo5gcyeVdn_VvWxVWCi3Ds_JVF2scz38I1n-hNo64xqZbrbf15yVrPmAx3OxnkbwhkMU9SZgxFWOWpawT7zPoFcvtbz0Bk6G1sT1lmuW8P-1cwrkYi_1FOe8QODsJfZkIE75-BHigpDRBkbApu-KCiGB-xqR4xuVIE0-tCwmiToDcrZ0NPpi8ka1_URAU8YCN2qof71ybBbJ9IYl9F3Y9iHrGBGDxtq93CFDn6xqfEQBf-myf6dGo4W0C67Z1E3p1FEDjDjjJkO5-QwmPYX9OU2-ElhuNeM27E9z-BbTJPVQb5PBPvMoHzW84oR8whvv2DCyB4QtoraL_pobERqA61GoeByCgK7e9V7bUeAvWyyiH9WSxSScYXFkScGMTdhbWraQ3FVetsdTUWxGc_GrOkpl9sNC1HIvqjatzfqDxS3d7OOWItYwuu90D1MpQzOp2yoTCG2zsJc1usJrW7mWUnZTdcY5yExym7grDXDZ_1QmyczkgTmv4Z786UdpvFz3iAHoy77Upk6W5kbplClBVd5GDjJfLZh9rJGW4EXBwAu3b-4grmVjRp8BOge0lQushPKeDec2SXlh2I6pmwR11VMW6FrrHmXlsDzszDt-HUtTny0U1JpeciPeNnofWCAU5Xn1CzydiC7rAxmwnY-iXfnE9nwqA3hmdlEz5O6s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/917b2cd572.mp4?token=QhsWo5gcyeVdn_VvWxVWCi3Ds_JVF2scz38I1n-hNo64xqZbrbf15yVrPmAx3OxnkbwhkMU9SZgxFWOWpawT7zPoFcvtbz0Bk6G1sT1lmuW8P-1cwrkYi_1FOe8QODsJfZkIE75-BHigpDRBkbApu-KCiGB-xqR4xuVIE0-tCwmiToDcrZ0NPpi8ka1_URAU8YCN2qof71ybBbJ9IYl9F3Y9iHrGBGDxtq93CFDn6xqfEQBf-myf6dGo4W0C67Z1E3p1FEDjDjjJkO5-QwmPYX9OU2-ElhuNeM27E9z-BbTJPVQb5PBPvMoHzW84oR8whvv2DCyB4QtoraL_pobERqA61GoeByCgK7e9V7bUeAvWyyiH9WSxSScYXFkScGMTdhbWraQ3FVetsdTUWxGc_GrOkpl9sNC1HIvqjatzfqDxS3d7OOWItYwuu90D1MpQzOp2yoTCG2zsJc1usJrW7mWUnZTdcY5yExym7grDXDZ_1QmyczkgTmv4Z786UdpvFz3iAHoy77Upk6W5kbplClBVd5GDjJfLZh9rJGW4EXBwAu3b-4grmVjRp8BOge0lQushPKeDec2SXlh2I6pmwR11VMW6FrrHmXlsDzszDt-HUtTny0U1JpeciPeNnofWCAU5Xn1CzydiC7rAxmwnY-iXfnE9nwqA3hmdlEz5O6s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
درگیری خونین و فوق‌العاده شدید در لیگ امیدهای فوتبال کرج؛ مملکت بی‌صاحب همینه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/101869" target="_blank">📅 11:20 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101868">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IC0JvuwlWDK_SBu73L6-L7yasGxlfITtKlgzxva1vz6y7t4cIrQC_pfLWs87yZ-6nTAJrPra7KZt9RY_g3jGLBYbCnABqD5F8yWRdUS2VJ9l4xuBa_KAYrV_dL2oyrxN63oj9a3Re8DmQTlYdqyOPutOX2YXHBcR-qeE1FPdBy2MFdGkcb1zW1Ewvc4mwz2KJ_jsSAKrMBhQzGRpO0JR9wis_PvOgY_2UiQZ3JbtATHTyrJLseUw400NyG74Cks0JHBqieiA53OW4BuaP37B7SrGP38og3uYv_QTTouQI6u3BoIIogqOJRER2qiGhfX1kjx4rwicGdPQuikiJHPU3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔝
👀
شاهکار سرمربیان اسپانیایی در فصل‌گذشته
🇪🇸
🏆
دلافوئنته قهرمان جام‌جهانی
🇫🇷
🏆
لوئیز انریکه قهرمان لیگ‌قهرمانان
🏆
🏴󠁧󠁢󠁥󠁮󠁧󠁿
میکل آرتتا قهرمان پریمیرلیگ انگلیس
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏆
اونای امری قهرمان مسابقات لیگ‌اروپا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/101868" target="_blank">📅 11:03 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101867">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f4c9480c3.mp4?token=jke-BppOIswCz_xGEGNi2_Q4wSQ-LSmhFC-_IdYEuIrAmplEjs4Z2lyehADFQrfW01MC2Vpriif7rC9VdHXUvNTPWrnxMXP8dSt6WEdU80_YDzz0kciNgBzQHxjjjNFPUwwbhpt2qzSwRf0586cQDIm0DwoItDxS8eonzk7cYZuOKVI1yJRYc7X18F6tzGDIAPlmMGCmcRsrTzryC2DkFhfcESgpW6zVzG4DsRFbeUbxkY8bfFZTz7qzclPTmYk1tVl7C4lvbuXCp1UKr38TIlHrt2PgkegfqgRfav01ktHGLw_ppOupefYeWtVTe2ASYciOf9sd3d_nyCBSdVp4iA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f4c9480c3.mp4?token=jke-BppOIswCz_xGEGNi2_Q4wSQ-LSmhFC-_IdYEuIrAmplEjs4Z2lyehADFQrfW01MC2Vpriif7rC9VdHXUvNTPWrnxMXP8dSt6WEdU80_YDzz0kciNgBzQHxjjjNFPUwwbhpt2qzSwRf0586cQDIm0DwoItDxS8eonzk7cYZuOKVI1yJRYc7X18F6tzGDIAPlmMGCmcRsrTzryC2DkFhfcESgpW6zVzG4DsRFbeUbxkY8bfFZTz7qzclPTmYk1tVl7C4lvbuXCp1UKr38TIlHrt2PgkegfqgRfav01ktHGLw_ppOupefYeWtVTe2ASYciOf9sd3d_nyCBSdVp4iA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🔥
🏆
رقابت‌نفس‌گیر توپ‌طلا ۲۰۲۶ در یک‌نگاه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/101867" target="_blank">📅 10:40 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101862">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IZeToouDgBlgYbHagUxVqb6s7HMGg4D7v6nSUkGio1-i1_xRcDuZ7B8kQZxjS0Brz0Wq7tVZtXdVLE13w3IMdw7gPjfB-P28uvh_okd9PSEeijGsKL1WY1dOZkB87ym3I4Poi8thcI6lETw0lx1leZLWofIXxgz3JQcCzEaOF_3Kh-oPVnm3Rv9XjVo8FWcTXShN0v43H_mLQeJB8uuXnv6WahmxpZvekZmgxvzYCC9vaHnn88Y0LEkm3prkaQ4VOjDk459vSUrCoC5fBZFOHtGcoM8RA2zq6e57lp5UmUznYWVnO7ubyX6Eb1xfHH1l3KO-y6pvbN_79SjcTmmIsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aFrcdNUTmBl8QvfvVx3TjE_Z1f5sBSlSeXyNVd2CHdaqv6XuDNewnqufhx3QZaPztfwn6MBNjZrPOQ5iDjAJVaw2IPImnm3-hA9otflykKqhwQQaNNjhaPQB1gM7Yw_G3Z7ys7J8LbXKb4l83T-O4T8FbFI-KrvF82ad8oYw1owTHDkYGSUPSW8toxheKEls4VvR2bM5FKTyClm8zF36KQstZLDnn212FgS2oTGpVnR1oYylnsQGt8NQsI9ne56zmjM1wgLXcu9XZ2JSjA62zh9_GMV2jt2puan7uAxcrtKSZbiGCKohH65VGxDMsB8jm8xjazzEjav6rUGh84rEwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CZSpnlg0tO2Z1UxIhWa9s_Ca2wK8m_lU3-8QNKbP9KNH-F4unkjF_rOyRHJZKPpRJ5NhBuLd3rOiHAIWFZxE20XzKl86fYfOxSPqjPI4FpcPuGULzJ5JcpjOJhzYu0_d6cSTnk8v5OJKpBAO0i5fqJ1CVCeRsQzDNd14eDB2TC0QTDKyiEWzosWoWswE_8FPnn3J1iSrEOL03MDAicNvqpIJxtnayvU-5ZAyP0HgKpNuqFACz8lBgnvtFZH4mTEZKMlv31MAhLsm_CkgChs8ULs_WTVvGur-kSLulGOi7qsRrdv0g53oWwAC2CcnuDbsnV7q1wnv2_sdS28FjfPgBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S6rQ2LD5Sq6KTqdCdWexkDUh1NaApMtD80Hq2cL0gjTCVV7SV57mAntqxc5fljW1ksDe2rAO1sfwG-UcKHY9f9LporED5mN_j0XWDEFoU08QYHtAIahzR6jW692r4_NyRJVMs2c6mdWSBOWOD3AmTeDYdi6MusOyg6_PTzRE3lF2R9sNJdDEEzgaGgiq13v0AaX38EcGwFB5io4DiOg7dwLPZw_X_4bQF_HSM9ECkWOACzsqhQEgBgmJRrHr8MFsdacNTOjCtbh9Avas2-QHIMEyxD5Tw5nQLa8PHeeWOCYujaV7RBkUPIalZgYhA_zF5PEdXxOf9zJTnSX52Xyzqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QoachwZDp9afTjB2zBsisbsz-9yUYu-gwIsVskw8aPbJoHk2dJ_d1qDKOFMeSF3207kXngelSCgMN0OSr94ZO4L_3xwVIVKwDRtYSBGBBwgITrm6AhrC1V-tSE42NfFb2EOUz0OtoS8us6HxJK3Qhl6d4ICGG_mInlVGupTH_2RmctxSzjrR77H_dZk2CHaTLoDDN6TOCrDJl3pWCwq_ed6o_dXsIxdHLrnU1asVrWp07TN6NCHSPlUrJJB5Vnb0qo2xmVUKlsUsp2b3zHut6IV-rAL77hZYBEi0ettOSwY8_bjWyrsD-YQBVh3Draz_Pr-XY3MkYRok3N9XnFYPgQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">+ قدرت تورم :
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/101862" target="_blank">📅 10:34 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101861">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5d7ccd208.mp4?token=I-vmmXv5Z5dzWwbVtuxBSUWoc3HbsBv4uCErcJCgUQ4L7CTdpYwMwqW9GU-tgdV0L_0hvHDvhJgCR4bBUSYLNa4-JFzovkYEDy6iQCGlMXcetnLk1cyib439KRjtJ4QyNlV7UFDgoM0OnPO9ns_tZLFWc4HM-3iOpPsMHkAgRkDfvgS8kUr94ESOLuBqrhwFU9OuLaDryvD4wt8mBzt2tSQhzlRUHZk8-2qKg4tUN6n7jUiTV-6MAJOLE9aWvH2j9kRb4AeA4dNdph5H5KmuVPJrb18zh9w-rIYj22vrGtg3RDnsmGfnxXlaiFJsaNuXeVTACZT5JJU3GYJi2aOCwBsNLO9QdQW90Jr0AiCcw1_C4dtU9DVLyGgnVT6n48Keql8nQwxCUdwfzjsQoW_8Rz0oXX4XV8HqGfzsvbhr8AWuKJzW_g9vHiVBbMLY-y2x0nUaGLtmdA22TsHnYShz6_ydaE18uIW0-o86FZmRRk6U4qZ0r1uG_TbzgJ4_X2K85Y4czfxuNwo8Y_TX1g9h9au1rtsf-lEVTJyU2_hngs0my_UwDYjkOYb70h1POvmce6oqp9Q7gQNMhQtbn-FMrl5l9874x26jBzP53C0jtYwR7MIOvKq1K376zcuNVLuZYlK_pi_pKwuwZvtRKpzfFkwrnKUdEsBVsGCZaXKzcRM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5d7ccd208.mp4?token=I-vmmXv5Z5dzWwbVtuxBSUWoc3HbsBv4uCErcJCgUQ4L7CTdpYwMwqW9GU-tgdV0L_0hvHDvhJgCR4bBUSYLNa4-JFzovkYEDy6iQCGlMXcetnLk1cyib439KRjtJ4QyNlV7UFDgoM0OnPO9ns_tZLFWc4HM-3iOpPsMHkAgRkDfvgS8kUr94ESOLuBqrhwFU9OuLaDryvD4wt8mBzt2tSQhzlRUHZk8-2qKg4tUN6n7jUiTV-6MAJOLE9aWvH2j9kRb4AeA4dNdph5H5KmuVPJrb18zh9w-rIYj22vrGtg3RDnsmGfnxXlaiFJsaNuXeVTACZT5JJU3GYJi2aOCwBsNLO9QdQW90Jr0AiCcw1_C4dtU9DVLyGgnVT6n48Keql8nQwxCUdwfzjsQoW_8Rz0oXX4XV8HqGfzsvbhr8AWuKJzW_g9vHiVBbMLY-y2x0nUaGLtmdA22TsHnYShz6_ydaE18uIW0-o86FZmRRk6U4qZ0r1uG_TbzgJ4_X2K85Y4czfxuNwo8Y_TX1g9h9au1rtsf-lEVTJyU2_hngs0my_UwDYjkOYb70h1POvmce6oqp9Q7gQNMhQtbn-FMrl5l9874x26jBzP53C0jtYwR7MIOvKq1K376zcuNVLuZYlK_pi_pKwuwZvtRKpzfFkwrnKUdEsBVsGCZaXKzcRM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🔥
روتین تمرینی لوئیس دلافوئنته‌ی ۶۵ ساله
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/101861" target="_blank">📅 10:20 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101860">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/025979a7c1.mp4?token=WAsHiDIVOzcuHAeIXvWgFBWViUZ09z0dPGMl8MV_DjB1c-Xb1NWXjqC9fJmyN5IFa1XpVk0TBRguiiVXLPt5rrSa-vrLhLVbll7N0QPGCe76X6vC-TkO0B6zzW7GKD1sb5VYXpOZtSWI0nXF1C-hPDuUqqssdohU5738N4JRDoPpH-bN-Vv1YDjsY7gorg1le13qnTakC65b7UtuQIwrMHQpUtc2HkcVIyjatlcPbcD2PHZqjOuGoxa5A4Uj3HzgYAhJGUFDnH2ghVDdHmB8tOYEgDAKmnCgoZf2rTfRFs7QFlMcBJ6HV7natfYozw6VqOWJ7Nfmc9k1L80-Q1emFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/025979a7c1.mp4?token=WAsHiDIVOzcuHAeIXvWgFBWViUZ09z0dPGMl8MV_DjB1c-Xb1NWXjqC9fJmyN5IFa1XpVk0TBRguiiVXLPt5rrSa-vrLhLVbll7N0QPGCe76X6vC-TkO0B6zzW7GKD1sb5VYXpOZtSWI0nXF1C-hPDuUqqssdohU5738N4JRDoPpH-bN-Vv1YDjsY7gorg1le13qnTakC65b7UtuQIwrMHQpUtc2HkcVIyjatlcPbcD2PHZqjOuGoxa5A4Uj3HzgYAhJGUFDnH2ghVDdHmB8tOYEgDAKmnCgoZf2rTfRFs7QFlMcBJ6HV7natfYozw6VqOWJ7Nfmc9k1L80-Q1emFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😐
دلبری‌های لامین‌یامال و‌ زیدش بعد جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/101860" target="_blank">📅 10:04 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101859">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/552820f16b.mp4?token=dIpiwoT7Bfc69vvuY2qo-W14WbGYSd7tZqEUBphreXp7h8NxiVaro3yTmpVmvIQ_ViNP8sjDUzwFDiTGQhBpXcZwX8xmcRk3y87l3wvpCs3whC4wA8p-obTL2OeBdWAHnczMZpI__j4UOClj8TdBjMBhGouWknfibHMHHCEVOfFiKjv1e0s97rwpbW7MUbR7JCPZNZVhOPYIgXsjUjgzR6cjucjCOEqU0YlGj7l7RwGMZFKpEDCIvjQmYf7WzM9RcvjQaXdzevocGW9htQldHOVM1kvXMCGjx4sLbrSYILEueCloX-p9QfDrsbJVtgzoAxpwFgXfEekuTy4l2EBlmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/552820f16b.mp4?token=dIpiwoT7Bfc69vvuY2qo-W14WbGYSd7tZqEUBphreXp7h8NxiVaro3yTmpVmvIQ_ViNP8sjDUzwFDiTGQhBpXcZwX8xmcRk3y87l3wvpCs3whC4wA8p-obTL2OeBdWAHnczMZpI__j4UOClj8TdBjMBhGouWknfibHMHHCEVOfFiKjv1e0s97rwpbW7MUbR7JCPZNZVhOPYIgXsjUjgzR6cjucjCOEqU0YlGj7l7RwGMZFKpEDCIvjQmYf7WzM9RcvjQaXdzevocGW9htQldHOVM1kvXMCGjx4sLbrSYILEueCloX-p9QfDrsbJVtgzoAxpwFgXfEekuTy4l2EBlmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
👀
⚠️
بی‌توجهی یامال به دختر پادشاه اسپانیا که در فضای مجازی حسابی وایرال شده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/101859" target="_blank">📅 09:40 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101858">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5533cc045.mp4?token=Qh0SsXQS_TQxGoYlMvsTLbkue3EyAIvvYRSic3oMEmbMHO12Vv8pGvjur2nwe30eAZiyWwwSXN3IQPWxedDQ6Er4A_Tp-4GEfp7Jm5UoCGb_yvOfEq77ZXTh51fnh466BdVvipk9Zdr_r7vfhOxmDYkh2iJ4ViEpMsMY3fK0bdwTK2DVIxbIl-jghc9FSt_BMi2jRM_Zp4Nq35Pw4I3w5wJ4b7LeS3C6O2rGn6fjdnA_hya-KL9v08BXPut5FTmHqEaIz8t3Z2byJ3eZTsLILCsinJsRjw3GJSH5BHgQ6zqe8B5g7-DTX3oO5-yzpxqNxLyz5GGbDtEBLDs0yMh_Cw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5533cc045.mp4?token=Qh0SsXQS_TQxGoYlMvsTLbkue3EyAIvvYRSic3oMEmbMHO12Vv8pGvjur2nwe30eAZiyWwwSXN3IQPWxedDQ6Er4A_Tp-4GEfp7Jm5UoCGb_yvOfEq77ZXTh51fnh466BdVvipk9Zdr_r7vfhOxmDYkh2iJ4ViEpMsMY3fK0bdwTK2DVIxbIl-jghc9FSt_BMi2jRM_Zp4Nq35Pw4I3w5wJ4b7LeS3C6O2rGn6fjdnA_hya-KL9v08BXPut5FTmHqEaIz8t3Z2byJ3eZTsLILCsinJsRjw3GJSH5BHgQ6zqe8B5g7-DTX3oO5-yzpxqNxLyz5GGbDtEBLDs0yMh_Cw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😔
امباپه‌هم دیروز اکسپوزیتو رو برده یه جواهر فروشی معروف کف پاریس و براش هدیه گرفته
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/101858" target="_blank">📅 09:23 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101857">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XZhDcBInA1Blowinyxo4wgRB5fp25U6EQMgP3A-uuygsfzx47geITME9FJGIFQtEGSRiwwJf772Aiw8NOup0rG1ei-NEVArVBYPcyM3Cgzftr9IcDy9Ue4n13s9cN6Ibnw-RJod2G9dwivunhTDDINVFYBPSviAhqPhV2KJm7twYL4qS62z8gObeddmoFoFds1y6PulRA248d3RsFOXmmWxt2I9UZ8U0dkKQ7aFR522AnQOzwcC8eyrqIhZsT-mVaAq1Ro3baHNDhpJFL-YlxGvLEO0iZRO4JBcZfxZod4s_Jo3ycJCDtrM4tGn8vxVtRNds8OeVJwE7oPOqWBBFlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
✔️
تمامی کاورهای بازی FC در یک‌نگاه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/101857" target="_blank">📅 09:23 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101856">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromحامیان_جبهه_پایداری</strong></div>
<div class="tg-text">این یکی واقعا معرکس و حسابی زده توخال!
#من_نمیتونم
@hamiyanpaydari</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/101856" target="_blank">📅 09:23 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101855">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">❗️
▶️
کلیپ‌فوق‌العاده دیدنی از پایان برخی از اساطیر معروف تاریخ فوتبال در جام‌جهانی ۲۰۲۶
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/Futball180TV/101855" target="_blank">📅 09:20 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101854">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2e5fe7985.mp4?token=C-nvi5N4RQmuOQkNbm_JvzZKVqmnhCB5MvtJyQUcsXYhSlfTAKzcJ188cv_1BXqPazVUenY1d21Co91rbzA51qmNBu_YF1oaWwH7VGOcHKq5rlUudZIjuZ8TNFxOxQS89vyApPIJuuwvOunVXjXHcAFm1d8Ewvts4yFYKUYPWDNhKkAlCjG01c5p8VLNxQ8COOFphYtQviZHOxMMiAVqAeHD4zGFwk9-UZl1v6QIKeyXHPEK6u2FuTPj9fdPw7Ik0DonPY8zhHpnlh0_XkX06sbLWWDRG5K1liERuUvfD2ZXctHc6byVGpIp0PVdf86y0clE-0Brh9fib4Sv38g4NQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2e5fe7985.mp4?token=C-nvi5N4RQmuOQkNbm_JvzZKVqmnhCB5MvtJyQUcsXYhSlfTAKzcJ188cv_1BXqPazVUenY1d21Co91rbzA51qmNBu_YF1oaWwH7VGOcHKq5rlUudZIjuZ8TNFxOxQS89vyApPIJuuwvOunVXjXHcAFm1d8Ewvts4yFYKUYPWDNhKkAlCjG01c5p8VLNxQ8COOFphYtQviZHOxMMiAVqAeHD4zGFwk9-UZl1v6QIKeyXHPEK6u2FuTPj9fdPw7Ik0DonPY8zhHpnlh0_XkX06sbLWWDRG5K1liERuUvfD2ZXctHc6byVGpIp0PVdf86y0clE-0Brh9fib4Sv38g4NQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🎙
✅
علیرضا فغانی: هميشه خود را كنار مردم ايران مي دانم و از حقوقشان دفاع مي كنم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/Futball180TV/101854" target="_blank">📅 09:02 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101853">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aBw2fO4ogObh7iM2c1Z3QZTuMq9ICPDr8uXY9Es61WWG_tiLFtlBdRAWjUvSPWSFKLE8fZHRvrwjQiFN6isfecEH8UywUACW0bL3AMi0oWpRz9zG0gsqNvIOPkfZhDznVxFWWNyB4egZeuhoEZ1_d3eVtR09xgkN1saxXDhj2TT_wGMFIBeIodCaWSxVx4HcHT9vrkzNp1wH-pZXRNLQyHCpvDOjPJoobZDhf_nddUxUzvi3rzXmyWm9kk8Zhdco2ZyW_tMSt9m2LLWCP8qBFJ9HFVa0qJXsGzsyFabusITJWVMoxh0B3J1NrFxjrcxznXG7FISFm9V7i7AymtBZ_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
رسانه ESPN: رئال‌مادرید تصمیم گرفته که به سبک بارسلونا، شاکله اصلی تیمش رو حول محور بازیکنان اسپانیایی بنا کنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/Futball180TV/101853" target="_blank">📅 02:59 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101852">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be7211acfa.mp4?token=EOje4SL_WlpKDpPZXTicuM_VqsYi7wonkk3FsNgxJMfTm-rQCsnifl4xlEt9X5kTbMXx42IO1TYEVhjjadx-OgnBrG8vXIv5L2ZM0iXTPA6N63XV4kHidoD0e3vsaUAHP5R7OMm5H18qH-mnUGVSYHkXwQFVa5CzCWgSFUjxqU95FIIET2I2gFm_u0kVceE5IRumZq16gp6FHToLQSXRq7ECvQjWJbbVBnZW2wGnFle-eZ_g-soH1KxJAdXNJ6NlKxinelh5Q6lfgYt5dgNV61S4AvnIBfiaFsacmQgHx_mNor7-I7fEjfdTp1UiHUrILbnyEr3nQTh3WX92LttDbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be7211acfa.mp4?token=EOje4SL_WlpKDpPZXTicuM_VqsYi7wonkk3FsNgxJMfTm-rQCsnifl4xlEt9X5kTbMXx42IO1TYEVhjjadx-OgnBrG8vXIv5L2ZM0iXTPA6N63XV4kHidoD0e3vsaUAHP5R7OMm5H18qH-mnUGVSYHkXwQFVa5CzCWgSFUjxqU95FIIET2I2gFm_u0kVceE5IRumZq16gp6FHToLQSXRq7ECvQjWJbbVBnZW2wGnFle-eZ_g-soH1KxJAdXNJ6NlKxinelh5Q6lfgYt5dgNV61S4AvnIBfiaFsacmQgHx_mNor7-I7fEjfdTp1UiHUrILbnyEr3nQTh3WX92LttDbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤣
‼️
🇪🇸
شروع‌قدرتمند آردا گولر در ترکیب رئال‌مادرید برای فصل‌جدید با خراب کردن‌پنالتی امروزش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/Futball180TV/101852" target="_blank">📅 02:21 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101851">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cnrz0JWNqbNMrzAWv0fJROczVuY3e9u0uu2qiB0OHCXuABT7S20ha8n6QDNYDQ9VJfFrF4qHRzn5s_gDj_YX0z3cuMYLCH6nQxxJ3QG1ELt27tPyCCBYxkc9Zyjy8DH7oeS0offlHfLEeh1oH5W8QOHZ16IgAb_cZlA7CktVI8rGVbgxcdG-9DD7PYVfUxI2tfbxMRZynT2mVBcv-tEREL9N9ND4KH8AAAWFcVtY6pMrXomngldYIeXRvMs2aeLJC9dupra3amOoBTrLXGGq9HfjGFEJuSFeRja8AWPLIZ8pEratfz6fp7ju_YN1LCagRTso01EgjsF9T9hdDiS8Yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇨🇻
بر اساس شایعات منتشر شده از منابع خبری آمریکای جنوبی، ووزینیا گلر شگفتی‌ساز کیپ‌ورد فصل‌آینده به لیگ‌شیلی خواهد رفت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/Futball180TV/101851" target="_blank">📅 02:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101850">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AFERX5suBkEJUT6wzXoS0SEKWSIXpfx_rwP9tMJf8H48sNnZVOvOARrku57NypmvBURuqdA5mB-UJnaXggXxC5WPQyvo06rLCILHBNrVCVHiQl_KKduLfGut-3ylxDqM_SSLJWkF5nL0dCzDmNZjRuk2ZukeqhaB_YJ9OgXRhTWNpY4XU8ZmkMa-q7QJgO1Y7IR5ROVfsF6FnnO0keasjnVDTJ3TznBP8_SEPWZbm6lpQC1p_Ye_glEnV9ikwjRqjWWo3zJEMTTD6X2OCFpqhGqrvgpga-Mz8smRIo75EqmlRCFqE78cX5p5TavufkP_50fp5gzz2q4i3EHtiYob8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👑
🥶
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/Futball180TV/101850" target="_blank">📅 01:28 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101849">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vNp8a4qNRnL5O3D6jQ6frNUhJSATY7wJRpYn11HpoXa_B3XAOtJgfVGTF1_G2qG3KLCpy_jFSVYQP1e1rjIXpyKWlDOFy-yS2ldp-rLEcQgXK0FNjloj1StvfHtlRPwnKV2nXsLUBJzOgcUl2FEkDPCFROXZrgWDJP-emNmS5zJGUnWDKplKmlqSpr9sdk72Ff4nyDbWJxdt28IGMgkKlkCO2IL0x8ir4ROyfjBOzerxkPg75kN3rycafSchRepfippfFrt_qVKZHzkR9zWA1q1IdNerPGbjoXUiL1UALdR31qsdu-cjgKj1F6k24-KtI05bkWBzzMhRFMJMDe4FFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
⚽️
🔥
🔥
🔥
مارکا: دیومانده تایید نهایی برای حضور در مادرید رو داده. این بازیکن به پیشنهاد نجومی پاری‌سن‌ژرمن دست رد زده و گفته که فقط به مادرید میره. مذاکرات فشرده برای توافق نهایی با لایپزیگ درحال انجامه و بزودی خبر رسمی میاد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/Futball180TV/101849" target="_blank">📅 01:22 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101848">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aSmQiqKtue3JrnSkbLwbR4Jz0isxmUs53gEGt4PXzSUKlzOdRMjpQTO5LU7eERHRG2uOfm1ZhQx_fZhj8ZdrUVje03gEnwIMVi67NdJQbnoXl6dPMTVmKKL7FDMiHIKu6dIaS9xVg0eDITkfbMpau2OC_-cUiyZpL4CEQib5ZGAMpGCu6BbxvoSskfZGuPqr7G9gheLbfjAQ8HxqiJxUNW-zUgdYda867HSLYgm0pYbDLYq5Uf54oml_kXPMnv8jo6Z_6xPg1rhZb91_fxoV4bdKB3mmrXN24rQYyOQaJs9aAj5GZsaZLadHArxfYGJBC7_MtzCnSCCsUfyajWd3ZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
په‌په‌آلوارز: رئال‌مادرید و ژوزه‌مورینیو دیوانه‌وار عاشق دیوماند شده‌اند. این تلاش پس از ناامیدی از جذب اولیسه صورت گرفته!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/Futball180TV/101848" target="_blank">📅 01:18 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101845">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DQFwgrxS-MO4YWKcvAb2-mbfOY_s0JUnp3tEzCF9rNrU6hIAbM-lyqA0w_H9A2cpc2Psw_w6TpWHCjvyeS1bGxE_ne_l-mMcgwmJq6UJSktcEYNMeXKKQxfzgn_Wfde9rDMnRW_NSWvYm5i2HHoVk9-TlmFutUZ3i2Q3eTMEXWoBzfU3RUNKM27fqobrP75saao1cFnFj2jf5TipgZhVP4ETxUV_oJiOtjeenlO6GN2_dJbD3WFVT8jRCL_6Bb_vCZGaMvWJhqj5Oi2UsPNXMvLa47iwq1aZ_zwrJtU6n9_HUpVzFiBK3oecRWjMVqGxyO3eyfaKVAF9gQolResoxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EdSsBHittD8DZyvAc94_eLdWPPluQHGGTxKidDyXGMdUTW01jWL3epjcXxy8aoAd2NbhWnq4t1GeLr6eFC-vYiKbgexVyWroaU8QU3mTmFS37AvX0wE93v6uW-nD-585q0CiTOFI8z54QqnkGsa6bbktiFFttoqtpy2lZSnvScTz130v99dMH-9UvckXrGbv1Df6cBhe_V7RRFvwcjeYfuZ9kxfRe25Gy0MB8Inb2bYwTm77TuvpsMA5jPovLKHI1-LKe2bUz9WuVYyLwRgFarkBTG4--zR5bqMWM1nf4I56aHLAljKZJIQy-A3FqsmPpZfP-xac5yLJJX23h796jw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
په‌په‌آلوارز: رئال‌مادرید و ژوزه‌مورینیو دیوانه‌وار عاشق دیوماند شده‌اند. این تلاش پس از ناامیدی از جذب اولیسه صورت گرفته!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/101845" target="_blank">📅 01:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101844">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LNsxvdmInMzxkL0RYKmQ38DvRCrc5aT9Y5k1ev3nbgLOg6vqYCbFve7xczMOlCwV7HD5dA1HNPS7ED-TVEjafqaHqQgIBrt2NjQPl1_0Pt89AB0v1dsSqhCGTVhQGVS-7RhbEsOGtlM02DraWG_vu4f927o-6TAU-k7hS5ZWIl4nvpT2wo9izwyMSjGAAt1IVYEWaLUhSVU-zrNJp5MJWavVtkyFXDzUzowH3RUhidIZrtD6fNK7sM3eUGqoMeg9fWo_yCEO1uyDfnj3TJRK4QVze2FV39W-NCdZG_cm0MSg7sJsJsaYk3OUYlllRS9nuAiE5gljuLchmLEoRU85dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
‼️
🇪🇸
په‌په‌آلوارز خبرنگار مطرح مادریدی: در رئال‌مادرید برای یک‌فروش دردناک و غیرمنتظره آماده میشن. بزودی نام این بازیکن فاش میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/101844" target="_blank">📅 01:13 · 03 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
