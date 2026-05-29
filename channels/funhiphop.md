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
<img src="https://cdn4.telesco.pe/file/fQYvqGzRE0SKhC4z7cWwHNAsdDrQUWsUBW5DYnr23rG_zXk9n90U_6mCyhcKCvUpnqLWDyOxoCVp1qfl6R_dmIg-Btfxrc7Dxxgbv0i446N75ByPAA-mntxPNOAVOzYXIwGMhvwR-FsB-i0DTk-NQBwbu_Nb7tQSHt6YFQaorr1sBu7EiWdIAZVVvl_s9KBtpRWIzVl2hUA7_4mPozPIlK5hvXs4KwgdDkDkySUSmhJRFx8c7pIoUxafJVvhsHra1gWWLnqeg-L75NDjAYVFVQzMkkz3o7B3yNNagcWFZJwvirXbFH3e_NcOErdaGkEYxlKc3qAzd2gPgwHw1a93Hg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 180K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-08 14:09:23</div>
<hr>

<div class="tg-post" id="msg-76236">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">مدیران اتلتیکو:
خولیان نخواهد رفت
مذاکره نخواهیم کرد
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 1.69K · <a href="https://t.me/funhiphop/76236" target="_blank">📅 14:00 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76235">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">ناتو: روسیه شب گذشته یه ساختمون تو رومانی رو هدف حمله قرار داده.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 4.26K · <a href="https://t.me/funhiphop/76235" target="_blank">📅 13:19 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76234">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">آه رسایی اینترنت و گرفته
هر لحظه داره ضعیف تر میشه
@funhiphop
| reza</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/funhiphop/76234" target="_blank">📅 13:09 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76233">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">رسایی آقا مجتبی رو به پسر نوح تشبیه کرد  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 7.81K · <a href="https://t.me/funhiphop/76233" target="_blank">📅 12:33 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76228">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vkZ_zW-hK3wdtNqjySHS5iqEUiIqwxUur_3l0NGUXxnMTjb5y4eK2b19pNKjNZRrwB-HwZ1OLS7ntQKGyVADOV1uIyHhxoK8Zb_NwiPSlCwzB0wQzc5vk7K-580Ypi7tO50-2UU3NI-9u_auuLoSuO6efzQ0fT2DZW5T6JxqPh5qwpieHt0PdR93gc1ytfyu9XaO6XUDrrxn_2p7MijHhcYSKx8m6MN5sw-kzjaW2TJEnCKZka6ZD71V7cqkBrBIv3Chs-3MPEhOixi4Q66mtytxi4XTCmlF7v1rsWEzRH0vLxxLBsDyGGY523_m5YefzLVfcZGgDG65z1WUmXSWDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسایی آقا مجتبی رو به پسر نوح تشبیه کرد
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/funhiphop/76228" target="_blank">📅 11:47 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76227">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8334aba596.mp4?token=U7N-bLTeax2DOSxxllKIj0M1ztC3pUp5_OhRIzapBHRHsXzReXVUqfmhSmdbQQ8bgfZ_bDvCUhdnM0XdDdagJToF1W4g3l9WJ8VOjFyVe2F4vSi8LSVlw3j7wp_gKFhgY9QLU1nyuuCq7hz_i4FHwznRB0jscdx2cUocGyZjUtJI7-w_L4nlqHf2j67mbD14q-3C0I0vDKjVGhm3Rouod_T1-74D4si7Mnemjvr9f2RnZfcaYfvc3PbAu4nR_6RIi9XLiNhJlJ1o_2GXWu5L7-t8oIVoPLht2PCbmIGd3-BCXGV8BpYLAGDLtP6l5qZI4niuvUguPuTM67ev69oYXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8334aba596.mp4?token=U7N-bLTeax2DOSxxllKIj0M1ztC3pUp5_OhRIzapBHRHsXzReXVUqfmhSmdbQQ8bgfZ_bDvCUhdnM0XdDdagJToF1W4g3l9WJ8VOjFyVe2F4vSi8LSVlw3j7wp_gKFhgY9QLU1nyuuCq7hz_i4FHwznRB0jscdx2cUocGyZjUtJI7-w_L4nlqHf2j67mbD14q-3C0I0vDKjVGhm3Rouod_T1-74D4si7Mnemjvr9f2RnZfcaYfvc3PbAu4nR_6RIi9XLiNhJlJ1o_2GXWu5L7-t8oIVoPLht2PCbmIGd3-BCXGV8BpYLAGDLtP6l5qZI4niuvUguPuTM67ev69oYXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنوب ایران ۱۲ شب به بعد
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/funhiphop/76227" target="_blank">📅 11:31 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76226">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">چرا وقتی اینترنت وصل شد انگار قطع شدیم؟
@funhiphop
| reza</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/funhiphop/76226" target="_blank">📅 11:15 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76225">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lq_3o4yFSixBiybGPvC7Ke0jVCAzlB7X7TNbFlkfyu7Lqf6OkJTwzeJO_RdI6bMtZMvC2iyyjhCQKLBDrgiWW5ouIl7g0NPYviqxq_LgXrzVd6JD2Uchwf7AE24w9EbvQNsQbDCYx3uqUGraBrH0WbP41eSCXs7e4V82GMr3Aj-XDhyueF_VgbhBG17eKtipHJtwMiPljAuom2tMGsFh_yXw9zuhky0zyYWiV_sgeLpTa-Jki-J8j5bPAkYzSungl9MtgKjgBq2-kLzttYGClyPg6PNjdWQzrOQ1ADogZVwjP1w4g4RfECa9Ubn7-3cP7ChRXmB1xl1h27RlHDevZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت کتاب پاور آف نگوشییشن، امروز به دلیل تخفیف، ۵ درصد افت قیمت و تجربه کرد.
@funhiphop
| reza</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/funhiphop/76225" target="_blank">📅 10:53 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76224">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">زهران ممدانی، شهردار نیویورک جنگ آمریکا و رژیم اسرائیل علیه ایران را تجاوزکارانه خواند و اون رو بشدت محکوم کرد، او تاکید کرد آمریکا هرچه سریعتر باید از این جنگ خارج بشه  @funhiphop | AmooFirooz</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/funhiphop/76224" target="_blank">📅 10:15 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76223">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JUocsczEU2YwFzumEHE35JE3HXtNHt0xn_CAXnHtKcUFhqxn2hLdhFucJYU4IbYWG-m2FZkK681oYb7zQ4BxvzVyZMSq8uB2P5Wc8TwjLx6vFuoRTCgV5eaQvKfFjTj9u-wmd6E7ivfilfeKMdS5ZadL88NhvL1wCe1tEeAb3Vxl5C40_k3Y4I-xgNAWJSBhUIrpBEhBPm2vLoLOFO0-htLG2ZT81kL7e5fYigjKflv-TwpnXHonZyPoXf0e3PjrYF0eHLvZ-_Y5X_RReKCsrG5u2wqhJE3n9L9I9lF6dnRC6yqZ9Jln0bJVtnHe7SZ_Cw23PENvwzGCqa-a0BTsNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زهران ممدانی، شهردار نیویورک جنگ آمریکا و رژیم اسرائیل علیه ایران را تجاوزکارانه خواند و اون رو بشدت محکوم کرد، او تاکید کرد آمریکا هرچه سریعتر باید از این جنگ خارج بشه
@funhiphop
| AmooFirooz</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/funhiphop/76223" target="_blank">📅 10:12 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76222">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LhixyyaI1tw8D6lW4QdmJoJTOp94skGhYjIWo-AH4_D1r9hgNHL1t85I2UW9JDGnwb37LuBG4iZsyw09QH1kX63aBvt0jyBZbGR7ET0DO3t-2mztyS-RRrxKwIar0AbtwB9jHV29IcSchCZHcPAPQ2_oOPpsKVPXhYtCKiQlhpS8YgaYZEkHI9Hc-k4Ir_VAYdtO3n4x7NtTiftmGceqf2NELFqyElv77zs6-e1L6Tmw7J83ti2T2Jkfs5CU2_p213m_0wQpSwdSF34-1N_MFKZqGUtK7wWxeHyw0NgDW3sPeoJNV1bYMuZlH-ouzrf5z-5o3Qv_SCBa7iKVirBtUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لاپورتا افتاده دنبال گواردیول میخواد باهاش قراداد ببنده.
@funhiphop
| AmooFirooz</div>
<div class="tg-footer">👁️ 9.95K · <a href="https://t.me/funhiphop/76222" target="_blank">📅 09:52 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76221">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">derbybet.apk</div>
  <div class="tg-doc-extra">52 MB</div>
</div>
<a href="https://t.me/funhiphop/76221" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">✅
اپلیکیشن حرفه ای اندروید سایت بین المللی دربی بت
✅
اسپانسر لیگ انگلستان
💰
اولین سایت جهانی با امکان شارژ و برداشت با کارت بانکی
🔹
برای ورود فیلترشکن خاموش کنید
😀
Telegram Channel
👇
https://t.me/+kpFvLD9kaeJhYTI0</div>
<div class="tg-footer">👁️ 9.01K · <a href="https://t.me/funhiphop/76221" target="_blank">📅 09:52 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76220">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LSSrhXXjbEL7WI8NrrmH-hgrV5X9CTgsowzzXA24mo1JUqoRUQwc0H4P88uADb-m7kVtf0Dh871wfh_yELS7cWno58-hQAbUsA1SKtBSUMXVPumgLR7ECjcoaY_7nDDenC7_K8dLXnEIhAgHZOgh7ucfikLhDYzGXERwN30gYxmU9A69pxQOnNTFsiB1ZJDgJmc5HM3rnhysWPExCq9jxfDq_xlA9MVvC7Isc6TuTD34NxZ5arhNAOaFbVRPM_5t7_iTKijPgOiXAfeFALw8YhpJ5-B6l7-CDTKWfeYdNTEEAFQolZURit-1hJN3FZl06LSbbvUXe-vV7bATIV7fYA.jpg" alt="photo" loading="lazy"/></div>
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
⭐
دارای لایسنس و مجوز anjuan
🚨
کد هدیه ثبت نام:
GG007
⚠️
برای دانلود اپلکیشن کلیک کنید
👉
🔔
کانال دربی بت :
👇
r8
🅰
✅
https://t.me/+kpFvLD9kaeJhYTI0</div>
<div class="tg-footer">👁️ 9.8K · <a href="https://t.me/funhiphop/76220" target="_blank">📅 09:52 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76219">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">سی‌ان‌ان:
حداقل 50 تونل دسترسی به شهرهای موشکی در ایران پس از حملات اسرائیل که آنها را مسدود کرده بود، پاکسازی و تعمیر شدن
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 9.42K · <a href="https://t.me/funhiphop/76219" target="_blank">📅 09:46 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76218">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">خبرگزاری مهر: هنوز مطمئن نیستیما ولی فکر می‌کنیم یه پهپاد MQ9 دیگه از آمریکا رو امشب نابود کردیم.  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/76218" target="_blank">📅 02:36 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76216">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">دکی واقن دکتره؟</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/76216" target="_blank">📅 01:49 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76215">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">اینم گذاشت چنلش گفت بگم اینایی که باهاشون عکس گرفتی شغلشون چیه؟  @FunHipHop | Menot</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/76215" target="_blank">📅 01:41 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76214">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">۹۰ روز از تـرور سید علی خامنه ای توسط اسرائیل و آمریکا گذشت
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/76214" target="_blank">📅 00:57 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76212">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">امشب وحید جان خبر از چند انفجار مهیب و لانچ موشک تو جنوب کشور مخصوصا بندرعباس داد و تسنیم هم الان گفته به سمت ناوهای آمریکا و کشتی‌های تجاری‌ای می‌خواستن از تنگه رد شن چندتا موشک و پهپاد شلیک کردیم که خب چیز خاصی نیست خاورمیانه‌ست دیگه.  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/76212" target="_blank">📅 23:53 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76211">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a936874c3.mp4?token=L52u1P65q_Tanr0tD32-HvUwpJngUlNrmLI_OWrJ7CbSlMv_rq_TsBMvgCb6SXFrK8cj7A1XE5YBM5dFDwf2T_mRRYuu-RmrvRQjWGwF3zdIqOfiWRBG3DGedxgwpqFp5EDwR_rPYQCeN_g4-uWRyRzX21gBc4JfV0Liwy7edu_D_ZsFYZ-1syltAZyJwM7vtu6cgBHH73TD6-KkoOIhhKUYXkvGgGFo04cfWSdu0YOYRHsJUEyE2ZnqLZzlvgrGccCRpRZa7xvcMI3wDNkPj3quUFVkMpMHmtI9JFEMA2ro_oucY2lB_wD4390rIdIeChoj2GhbYmXPLwBYBtoFyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a936874c3.mp4?token=L52u1P65q_Tanr0tD32-HvUwpJngUlNrmLI_OWrJ7CbSlMv_rq_TsBMvgCb6SXFrK8cj7A1XE5YBM5dFDwf2T_mRRYuu-RmrvRQjWGwF3zdIqOfiWRBG3DGedxgwpqFp5EDwR_rPYQCeN_g4-uWRyRzX21gBc4JfV0Liwy7edu_D_ZsFYZ-1syltAZyJwM7vtu6cgBHH73TD6-KkoOIhhKUYXkvGgGFo04cfWSdu0YOYRHsJUEyE2ZnqLZzlvgrGccCRpRZa7xvcMI3wDNkPj3quUFVkMpMHmtI9JFEMA2ro_oucY2lB_wD4390rIdIeChoj2GhbYmXPLwBYBtoFyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرگزاری مهر:
هنوز مطمئن نیستیما ولی فکر می‌کنیم یه پهپاد MQ9 دیگه از آمریکا رو امشب نابود کردیم.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/76211" target="_blank">📅 23:53 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76210">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">میدونم برای وصل شدن داری سرویس میشی، منم همینطور  ولی دیگ بسه بیاید یه چنل آوردم براتون سوپره کانفیگاش، کانفیگای رایگان میزاره که وصله همه کانفیگاشونم از قبل تست میکنن رو همه اپراتور ها، خیالتون راحت. کانفیگای اختصاصی خودشونو هم میزارن  خودم تست کردم عالیه
👌🏾
🤌🏽
…</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/76210" target="_blank">📅 23:46 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76209">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">میدونم برای وصل شدن داری سرویس میشی،
منم همینطور
ولی دیگ بسه
بیاید یه چنل آوردم براتون سوپره کانفیگاش، کانفیگای رایگان میزاره که وصله
همه کانفیگاشونم از قبل تست میکنن رو همه اپراتور ها، خیالتون راحت.
کانفیگای اختصاصی خودشونو هم میزارن
خودم تست کردم عالیه
👌🏾
🤌🏽
اینم آدرسش
👉🏽
📡
@VPNir404
👉🏽
📡
@VPNir404
👉🏽
📡
@VPNir404</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/76209" target="_blank">📅 23:43 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76207">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">امشب وحید جان خبر از چند انفجار مهیب و لانچ موشک تو جنوب کشور مخصوصا بندرعباس داد و تسنیم هم الان گفته به سمت ناوهای آمریکا و کشتی‌های تجاری‌ای می‌خواستن از تنگه رد شن چندتا موشک و پهپاد شلیک کردیم که خب چیز خاصی نیست خاورمیانه‌ست دیگه.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/76207" target="_blank">📅 23:37 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76206">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BDc6WGP1KbDQEWjUqCbUcUJCN-Q3wIOLdDG4qc6BC3w3zqCaiAVg1b-B-18nJa8OwzqBD7R6W2Bzw4mrFQHPKo5EgKnATXKZKbk-NrQA4ccE_ZwJIWvSOLgyiTN41BbzOm9qwWQ5PRDGLSMWhT6R0xQdjuNm7nHmJClo5rwbFxhV0q8g3FDGnHWPcck4cYeHnz1Sa__f00hxuexAIEUTNWRjnlRymd9zV4ng1_B8pof5-0pXHUKOjehmJT-V9QX-gjYDfSYFRfNxq4R1NN2g3AEjeEN1eXCOgJWQcTe_DtmOQuO0A6r4RX3nhvAWhnM229i57twOljXqt7_Aup37gQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نه داداش بخدا من خوشحالم از این که اینترنت برگشته و مردم میتونن وصل شن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/76206" target="_blank">📅 23:25 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76205">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">این گروهو زدیم که فقط میشه موزیک فرستاد
بیاید موزیکاتونو ول بدید و ی پلی لیست خفن درست کنیم
(فقط میشه موزیک فرستاد نمیشه پیام داد)
@Hiphopiplaylist</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/76205" target="_blank">📅 23:02 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76204">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">نیمار:
حتی اگه جام جهانی رو از دست بدم خیالم راحته چون برزیل وینیسیوس رو داره
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/76204" target="_blank">📅 22:40 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76203">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wwnd9bnLTywZA3drww3C41zfynIt-bDja_KaHQXNprefFLsnVT9SBQ5wPM6KaNVwfMjM4gvqjyfRUqTvoGgKuuJllCwxUyRJZQBCqTs2xvcVotTgnRMLYo6BfxkWTiVKb3ZU-nQ6o8tlZneWDVBZTc_0vAyd2lnGKAWnmN2I_W3TMqA10ZAZAFOxmcRNYc_hy5BTKCXYECu-TB6v--ARJu8Pz0KdK_sQfuGb3GFIseMhWF0tY1Gk6KOQLvAj7jKSNmXMjLbETNR8NYC9o0pDsFFJEnkLyV6Bmq-hhefJ4_FCeWO_AB9ekj6E72UCWnPZhoXibpCenoLcxRDvUZcg6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یعنی انقد کصخلید یه توییتی رو باور میکنید حتی بدون این که به تاریخش نگاه کنید یا ادا در میارید
یا واقعا با این شوخی کصشر خندتون میگیره
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/76203" target="_blank">📅 22:30 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76202">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">نیمار تو تمرینات برزیل مصدوم شده و معلوم نیست به جام جهانی میرسه یا نه
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/76202" target="_blank">📅 22:24 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76201">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">مجتبی جان ،بخدا نیاز نیست برای هر مناسبتی یه پی دی اف ده صفحه ای بدی بیرون، ما خودمون میدونیم در صحت وسلامت کاملی
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/76201" target="_blank">📅 21:46 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76200">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">پرزیدنت پزشکیان:
ما مذاکرات را برای تحقیر و تسلیم انجام نمی‌دهیم، برای این انجام می‌دهیم که از اول هم گفته‌ایم که به دنبال داشتن سلاح هسته‌ای نیستیم.
ناآرامی‌ها در منطقه تقصیر اسرائیل است.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/76200" target="_blank">📅 20:41 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76198">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">فرید رومانو:
برناردو سیلوا به بارسلونا
هیر وی گووووو
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/76198" target="_blank">📅 20:11 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76197">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">من کاری به این که ویناک قبلا چیکار کرده ندارم، ولی تمام این فشارا بهش سر موزیکاییه که داره میده و اینه که سر پرونده هاش بهشون باج نداده و زده بیرون از ایران
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/76197" target="_blank">📅 20:07 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76195">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ihKGHUgsqvW9uUjBk81d_fLwaEQIuU6f7a5x4aelPPshja5QfOOqnVfw_i7bgyXWwIb48Z-ZBYrHguUkP5D82if2q7cDFNJjjtqo_oj4UQXbwb7bjTLBcJUDLA1zHI8GEn_IqkRO08Gv0yvnZSfk1hC2BAYBxFHy3932CYWunOe3NVBGTdjzcI_JBnuasoSjYVTce_jo54iZL2B06ik7z5jaxV64z8r_YG69Xhy71zYh-INPOAdhPOpDSTQiL57_t5sjA0RyKcNEjD283hht4TnV4P9FJs3Uf4tJRZWeLwgr1fr6XC5emnOAKS0cuTKTO-C0rYr5P9pzBfQWiPWQVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/76195" target="_blank">📅 20:05 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76194">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">امین منیجر سر کیری که ویناک بهشون زده و از ایران فرار کرده فشاری شده و داره میگه تو ایران بودی خایمالی مارو میکردی الان رفتی بیرون بهمون دیس میدی.
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/76194" target="_blank">📅 20:02 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76193">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">دوستان من تازه آنلاین شدم، ترک هایی که سورنا و بهرام بخاطر اعتراضات و حمایت از شاهزاده دادن رو بفرستید گوش کنم.
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/76193" target="_blank">📅 20:00 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76192">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">یک دیپلمات ارشد اسرائیلی به شبکه ۱۴ اسرائیل: تا جایی که می‌دانیم، این توافق توسط رئیس‌جمهور ترامپ یا مجتبی خامنه‌ای تأیید نشده است. اگر توافقی وجود داشته باشد، در حال حاضر هنوز در سطوح پایین‌تر قرار دارد.  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/76192" target="_blank">📅 19:39 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76191">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">یک دیپلمات ارشد اسرائیلی به شبکه ۱۴ اسرائیل:
تا جایی که می‌دانیم، این توافق توسط رئیس‌جمهور ترامپ یا مجتبی خامنه‌ای تأیید نشده است.
اگر توافقی وجود داشته باشد، در حال حاضر هنوز در سطوح پایین‌تر قرار دارد.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/76191" target="_blank">📅 19:33 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76190">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u_5jNX2iMltaOFCcdD3t5Rv-1H6DzkFzBFBcFh9dSL_UYd0RmaV_UglTFiepJBvVwx1m5LXOITjcuzhdYoZ0rbOky0ZXr_P2TiO7FetLE2VYyE0jys5-qe5MLZzxYjgffVuxVP8Gwl19OXjAso1GgwgzF1JRGwoGj8p6b9rDWTtzyuRAf41z9849hY-aGiHL2a0COCx6E8_rydZMuLmrl-mmB2BOTklyi-HP_PDNzgz3LaS69QmA9mICcEbL8JYST2jJ4BwhoLkii01-0JSN67yoy-VewWM1fKrsrLfWGdMG3rplw3J5pr3JxaadC7vM36BguYn-dh6DlIjVseL1Ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فوری از آکسیوس: ایران و آمریکا در حال حاضر به توافق رسیدن و فقط تأیید نهایی ترامپ باقی مونده.  @FunHipHop | Taymaz</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/76190" target="_blank">📅 18:56 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76189">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">خبرگزاری i24NEWS اسرائیل: مجتبی خامنه‌ای، رهبر معظم ایران، یادداشت تفاهم با آمریکا را نپذیرفته است.  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/76189" target="_blank">📅 18:33 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76187">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">خبرگزاری i24NEWS اسرائیل: مجتبی خامنه‌ای، رهبر معظم ایران، یادداشت تفاهم با آمریکا را نپذیرفته است.  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/76187" target="_blank">📅 18:29 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76186">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">خبرگزاری i24NEWS اسرائیل:
مجتبی خامنه‌ای، رهبر معظم ایران، یادداشت تفاهم با آمریکا را نپذیرفته است.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/76186" target="_blank">📅 18:26 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76185">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">وزیر خزانه‌داری آمریکا: ایالات متحده قصد دارد دسترسی خطوط هوایی ایران به حقوق فرود هواپیما، خدمات سوخت‌گیری و فروش بلیت را مسدود کند. سازمان مدیریت تنگه هرمز که توسط سپاه پاسداران تاسیس شده، مضحک و خنده‌دار است. دولت ایالات متحده هیچ تلاشی برای تحمیل سیستم…</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/76185" target="_blank">📅 18:17 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76184">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">وزیر خزانه‌داری آمریکا:
ایالات متحده قصد دارد دسترسی خطوط هوایی ایران به حقوق فرود هواپیما، خدمات سوخت‌گیری و فروش بلیت را مسدود کند.
سازمان مدیریت تنگه هرمز که توسط سپاه پاسداران تاسیس شده، مضحک و خنده‌دار است.
دولت ایالات متحده هیچ تلاشی برای تحمیل سیستم عوارض در تنگه هرمز را تحمل نخواهد کرد.
روزهای ترساندن منطقه و جهان توسط تهران به پایان رسیده است.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/funhiphop/76184" target="_blank">📅 18:17 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76183">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">آکسیوس: توافق در واقع همون سه‌شنبه به دست اومد؛ حالا فقط تأیید ترامپ باقی مونده تا همه‌چیز نهایی شه.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/funhiphop/76183" target="_blank">📅 18:10 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76182">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">واسم سواله سود این تفاهم نامه واسه ایران چیه دقیقا؟
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/76182" target="_blank">📅 18:09 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76181">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">جدی جدی حزب‌الله و مثل آب خوردن فروختن</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/76181" target="_blank">📅 18:05 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76180">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">فوری از آکسیوس: ایران و آمریکا در حال حاضر به توافق رسیدن و فقط تأیید نهایی ترامپ باقی مونده.  @FunHipHop | Taymaz</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/76180" target="_blank">📅 18:03 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76179">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">فوری از آکسیوس: ایران و آمریکا در حال حاضر به توافق رسیدن و فقط تأیید نهایی ترامپ باقی مونده.  @FunHipHop | Taymaz</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/76179" target="_blank">📅 18:00 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76178">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">فوری از آکسیوس: ایران و آمریکا در حال حاضر به توافق رسیدن و فقط تأیید نهایی ترامپ باقی مونده.  @FunHipHop | Taymaz</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/funhiphop/76178" target="_blank">📅 17:54 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76177">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">فوری از آکسیوس: ایران و آمریکا در حال حاضر به توافق رسیدن و فقط تأیید نهایی ترامپ باقی مونده.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/76177" target="_blank">📅 17:47 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76176">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">بنیامین نتانیاهو، نخست وزیر اسرائیل:
ما باید ماموریتمان را در ایران را کامل کنیم و من هر روز در این خصوص با دونالد ترامپ صحبت می‌کنم.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/funhiphop/76176" target="_blank">📅 17:40 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76175">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">روسیه:
ترامپ با انتقال اورانیوم غنی‌شده ایران به مسکو موافقت نکرد
@FunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/funhiphop/76175" target="_blank">📅 17:26 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76174">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c6XUNz_lFV2fxY1qDv2CNfw0aYmbNXWHgEe2SZGxWxZQC86TzH632e6rKEee52oeOz1TCLnqYQrNGrN1ybjadvhW1TAFra5aJ8a5qEbYKAB3U21iUaZGC_1lNIWQI_xcm2-7UvwHlVqEsjTK6MvnaDMGlTPc429jrK3rmzJHQtt0gO6BPQRt7NWFEWSHKMudo3Tdz9rmn-gm4LUklixIC4eCz7tYUwYkaAni1im3lAPju-AMgoE1xb_Vqja6jNRTM6iXmYmFCXvRKwGpo2BfsnGxDS2jEQ9rbTpC7lCZ4sQQi95AnURNuo3sEmsv1rPfY74Iz1IPf8e1ZKw6AV8G6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">و اما مسعود که بود و چیکار کرد.
@Funhiphop
| TemSah</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/funhiphop/76174" target="_blank">📅 17:17 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76173">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HNArOmoxcq-K1vQVZzEtzg-oZotnBnN6u28kRzUrehD-PcU1Tf3DnXj6dcy8g2ELQFFoybncnJR1ZP6-FjIB1PFkdV0kc7ROhK8tBGHTO-aJ4H2OACgc55PF1agFjLqkoeokJtHCkuCIpRzKyS_EGQsmwl3la-KeWxh_MigoZV43e5MZHQGI8OyG2mKyQoXOt1fiwFSRf3GJ2psFXs8ucYB2j3as8auPpMOEvEHuIqyLoHP6ABDyMtTHxsg07xn7WF250ketFCxwWHCoambz2KvlybwqhAkAM94Oq_xG68itRbeopSkygFkO0nZkdVu8XAucwkycWi7pbMVcQZ9-5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✖️
سایت بین المللی
bet120x
✖️
👍
دارای مجوز رسمی Gambling Judge سوئد
👍
💳
شارژ حساب از طریق ارز و
یووچر
و پرمیوم ووچر
💳
تسویه حساب دلاری سریع
💊
بیمه شرط میکس
⚠️
فروش شرط
🔔
ویرایش شرط
3️⃣
2️⃣
🎁
20%هدیه واریز از طریق ارز و ووچر
┅━━━━━━━━━━━
🎁
10%برگشت باخت به صورت روزانه
🎁
10%برگشت باخت به صورت هفتگی
🎁
10%برگشت باخت به صورت ماهانه
💻
ادرس ورود به سایت:
https://bet120x.com/fa/?btag=971470
➖
➖
➖
➖
➖
👈
آموزش واریز و برداشت دلاری
👉
🔪
کانال اطلاع رسانی:
👇
g7
🅰
✈️
https://t.me/+RvVnWMHCqUc4YzFk</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/76173" target="_blank">📅 17:17 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76172">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">گزارش های تایید نشده: فرمانده توپخانه حزب الله توسط ارتش دفاعی اسرائیل ترور شده.
@funhiphop
| reza</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/funhiphop/76172" target="_blank">📅 17:04 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76171">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TNfIreMQO3aQBmpBkumxyqyK6DCqFAvjLEzateHpojZkXHZs84xWH8D2YlFLdlJaTC69EQRr6H4wPzPFI1QBC0tmDJmjMCf0rKouv3hf5c82kjMxyDt9TWfla0rULPi0odJQ6EvjdjAky9IMOzgN4o8Lsu5XyiLpbM7UohXuRWwfXZlZSwEidwOWD1bQWdqK3-d_6R8LmzI-lKn0Tb5Ea09_KCf3CiBkvGK6B_yb1_tBQr7CKo1EhtiZ5fXoawKpd7uJTwKzxo_2aaqxeAV_b_DxuHQNKzyFdxpDthgQGtJqA9FMGWUcv86CYXtV8F_VXjIfgGvcOZGE8IPmY1fCrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همون همیشگی  @funhiphop | reza</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/76171" target="_blank">📅 17:02 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76168">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">الان وضعیت جوری شده نه دیتا سنترا کامل باز شده کانفیگ فروشا بتونن تانل بزنن ارزون بفروشن نه دیگه مردم کانفیگ گرون میخرن، همه به یه استوپی خوردن که معلوم نیست چخبره
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/76168" target="_blank">📅 15:24 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76167">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">من الان دقت کردم موزیک یه رپر نو نیم به نام مارسلو تو چنل ارشیو بیشتر از ترک جی جی فوروارد خورده، بعد این پلشت میگه دیگه کسی ابی داریوش گوش نمیده مارو گوش میدن</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/76167" target="_blank">📅 15:15 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76166">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RqEGvdgJ4rw8gwN7P4K29OQE9bxp-5Rdmu2o0yzBc5IfihFM0Zo61gxT1-d18QSyD1XSKbmljGrVSMn2L9TDVIBo0HoP1ip6Q7BW-w8t9qNKR0hUfs66b-V-Py_4ZwJcAV_uDtYLDKG5qz46mD777m-kKjb-t3AXuVyNcSpjm8HK6KinlL8GkO7D8VufIRmuIUuzsRQE_Q4aVWX-eAZhzSr3OTSmgGcNQJ24e2iw88hZz4Gzup1u-2A3FATxY7JsyFrWJl8ZGDYblvOInM5eUVZQzpIKBmEgCS0XZlaWXsDYswq-nszPaYJCH7B5x8Bze7bh6R3OmzRrZ8ZiKK_sZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید ویناک به اسم پس میگیریم منتشر شد
Youtube
Download
@FunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/76166" target="_blank">📅 15:08 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76165">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">ویناک ترک داد
@FunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/76165" target="_blank">📅 15:05 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76164">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">سنتکام: حمله صبح امروز سپاه با یک موشک بالستیک به کویت، نقض فاحش آتش‌بس بود.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/76164" target="_blank">📅 14:56 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76163">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">با شرفی ازمون تمدید شد
سردار آزمون از لیست بلند مدت تیم‌ ملی ایران هم خط خورد و دیگه به جام‌جهانی دعوت نمیشه.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/76163" target="_blank">📅 14:48 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76162">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">کانال ۱۲ عبری:
منابع آگاه از مذاکرات خبر دادن که طی ساعات اخیر پیشرفت نسبتاً چشمگیری از لحاظ رفع اختلافات میان ایران و آمریکا صورت گرفته هرچند که چندین اختلاف همچنان بین دو طرف وجود داره.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/76162" target="_blank">📅 14:06 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76161">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">بارسا که دیشب گوردونو خرید امروز هم برا آلوارز پیشنهاد رسمی فرستاد
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/76161" target="_blank">📅 12:56 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76160">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">بنازم پرزیدنت پزشکیان
جوری اینترنت رو باز کرده که آدمایی که موقع نت ملی وصل بودن الان قطع شدن
@FunHopHop
| ALI</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/76160" target="_blank">📅 12:37 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76159">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">یه لحظه یادم افتاد قبل جنگ یسری جوک ترند شده بود که میگفتن "کشورو بدین دست وی پی ان فروشا چهار ساله دارن یه قیمت می‌فروشن و گرون نکردن"
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/76159" target="_blank">📅 11:56 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76157">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">صداوسیما رو باز میکنی حالت بهم میخوره، هر اوب زاده ای رو آوردن تو هرشبکه ای داره تحلیل جنگ رو میکنه
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/76157" target="_blank">📅 11:32 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76156">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h5bDPwfxtAMNpQKM7uNeFzModE2oHC3RnSS2dDlorJ-AbBwNzw8jgK9APe-1gjJIxU7E6lxQd_iKWIj81hEorDdou8k_BJoeAL-Z7Bb9h4UVlruCtocO7DWnVHpd1XCfU9Sw9-3SjprECDG22Xr8uvphoQFLQ9LUt7LHmuFO4JZbe-Q2z-kP434qOcUqgu1uhsQ9rYemnMuCKakKjo6QbpCWQ8QK3_VTxJ5TTiJfsbJCx_c0Hdceo9JECeHRK3SD1QJVRBIB86VuskEWLb3a4aEFq8hjlIQQ8012Dk1J-d4yukFM5tpcx1eOeo7TRICtSHok9sq8zmo89GI6iDZRog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حکایت وصل شدن اینترنت
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/76156" target="_blank">📅 11:09 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76155">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/urRmSxjnf-g_ybnVB71uPnODpNCk0WZHxK1w6LP363jEatRmI7_SKaMO8dS1ZCmU2PmIfuEa1mROj6hnM4FxIY6IWQG_MDvJ7x5CVmV8JHTin-SRMG0vKCL9M4AI5oV7CeWptgg-0dQGFEaBoywHkQUJ3qTcWeXVRwNz67mG1zp4ob0W1zA4kebG2KrcbK3-jHT_Pk6l1gLqozGJtFRnGE9dDDhYO8blQGUdXXNcd_0MMD673OvDY8t92RrCZ2O1n3D66MLih66gTX0kD24dK4QB5TnGPVfibO4zbgaGX9k6EguZa6ZphfPt9eVr_GTmC1U6OuyfkhxpiYqdcnquvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امسال عجب کیتای شاهکاری داریم.
@FunHipHop
| AmooFirooz</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/76155" target="_blank">📅 10:55 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76154">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">بامداد امروز بعد از شلیک موشک از امیدیه خوزستان به سمت کویت ، صدای انفجار شنیده شده و ستون دود دیده شده که ظاهراً لانچری که موشک ازش شلیک شده بلافاصله توسط ارتش آمریکا مورد هدف قرار گرفته
@FunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/76154" target="_blank">📅 10:47 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76152">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D3gT5MUZ7V_vAmrUp_M60tXRiTZiLMcUo2dEbH23OyoEuNJQSre9h-AE0ARCy7ProY4_uQ89SE3UGHiEfHjSCwCyaFOADJZ7nG2PfkrFIZnn8FoKcUEb1WLEYzyexI3g-SVG89BGNr4hv0hrf4IIb_R5ZmwfT54qkO6RFXpgKci5a9X7LkgwoTjspXvTDbsXMXgUtOeoq_EgSR0kr_mCfSAfVvkud0w36KpFop96dSoIsNWn_8u6e0sRv4H2ESiJ-FypDnlYDlwyLPWT4dYJaVP6rz36kLNwBNF68tfHLJs_n7LsDuc0ca0rD-w6mkyDgapqkgYXWaifUNvQsw9OjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cIyGZy2WfPU1J_RXKW5JphLn6nPiWKIopSbk1ZCivvyoleb_2_rGDQT7lpK8FOoQDInVKy78D6DHmIRbFqAJRp3FVHjDZVZAWopyoa25eQCMTIJOBk5jU30B7QdCVPNvTxANkm1skEti-L9s4_to8W5Vq3RvW-sBb7PJL4xM0rg-8XQI6iRGg2Vz8AzS_1461L_H599jjpcqatbHIOK-yhi0b5eY-h8I7LJnFhhj_NmrOf_gfM8jB1gS9Jbgi8z-GF-nP2KKlYvD1_kCQqNYVSZbS4xr_8h2hbEO-nnLM4aUMje6z8ZU2BGiLOhf_tTkEnaiECTQLuZK_XvZ2ynDxA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">از سایز پات معلومه اوب داری پسرجان.
@FunHipHop
| AmooFirooz</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/76152" target="_blank">📅 10:38 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76151">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/goCwXg-vrMEMcnifZ1IBXFbHgexHkBPrVp9Yz1rQQUshBw12zhStewsqOa_WTEmiV5tzH1l4qrys4bhfPivsTI1c5vKxWtjl7K2zRrF4Xl7eqVaXNbKKH8FlI7N-ThAgZqBON7nLwzByjT0x-FYP67-wXv2UH_W5mlcj7c8mhmXqP2_k7XX2QUNK78F_OqXnbHGyYhTB5eMGtYdQkm0aBzzylwPoQCLrads1x0hFIT21ZBIM0wZmxZ92MW5a_1dTkxyjJXuEncQzsjhAH3Fh5dWgmFupiqK5D2HSh_YWX2ry2b3MDGO73aK7UjzxjSVNmeOanJrOYMrgmgnKO43asw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این توییت هیچوقت قدیمی نمیشه.
@FunHipHop
| AmooFirooz</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/76151" target="_blank">📅 10:29 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76150">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ORgkZSGBKK2xKdIKRXd53OGP3up9sRP90FeAL6_Nalm4upMUISPkJRNnyqOZYJn6AkmiYXvePht9_3f2--dKbfIwRX1p7aXRLqYIDfsA-rWPqgMc0AkfVoVjZSd137iydRonLIbPfyN4CFXMcwSW1zWmPxo5Kc77zrg84D1ngmFupQyRniBuk0KMGku5tyWlcRcp2unp6oVwrWbHs-tu9xo18pDs9h7Krhg2isNuOH0CrsUasmgA2SpSOCfgJU9OiXODLKkI85oZ0pyIAQoVr72wlIba3bQ3SEnqtwO4w7oKS2yDxsK0cw7_Zp-owMV1FwnM_kpw1p0cPwMgFmOn2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تیمی نام ببرید که توان مقابله با این طوفان را داشته باشد.
@FunHipHop
| AmooFirooz</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/76150" target="_blank">📅 10:24 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76149">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">derbybet.apk</div>
  <div class="tg-doc-extra">52 MB</div>
</div>
<a href="https://t.me/funhiphop/76149" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">✅
اپلیکیشن حرفه ای اندروید سایت بین المللی دربی بت
✅
اسپانسر لیگ انگلستان
💰
اولین سایت جهانی با امکان شارژ و برداشت با کارت بانکی
🔹
برای ورود فیلترشکن خاموش کنید
😀
Telegram Channel
👇
https://t.me/+kpFvLD9kaeJhYTI0</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/76149" target="_blank">📅 10:24 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76148">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pW6mmGWngQbQfOVj6ra1TvD5P-7iWZbl7HN7WWUshHzebMMHlSDjnqhjTSBdSplMfMoqEIyt48nBpR6zmqnKG92zRsj-YUzeh74h-AFJCWJPCMkGvLgGLiZZ4yQ6i8k7OW00hp-svZPOltf_LPLRSWlr801IBiBueIDCeDfdc-Zm-ay5KaobzXfk23L0l1Qg01NpSGkH9_ml3NvTIyscW2dfJmUpq0TqRxibampxq13XL34E0zarMLE__m-L-lu3WQAyJr1vgqEPK6OdYIh9p655R4cNkvYQ8MhAaAVm19EI7xztfmKtMocGFU_rvLo5hhANADNYo4s4QewqmXyBUQ.jpg" alt="photo" loading="lazy"/></div>
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
⭐
دارای لایسنس و مجوز anjuan
🚨
کد هدیه ثبت نام:
GG007
⚠️
برای دانلود اپلکیشن کلیک کنید
👉
🔔
کانال دربی بت :
👇
r7
🅰
✅
https://t.me/+kpFvLD9kaeJhYTI0</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/funhiphop/76148" target="_blank">📅 10:24 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76147">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WGhF78byq4dW7nwQsQGem4_ROQi0pVeFOCM0MwdfZ259C8bpPmz9TwEsFgD3O_qzhmBzTvZluVanfquXklTtCyC5QLKLmW-Ey_6AheNXHcF0V5MlKssFKNmNQTHds4LwA3SBalnbPIko-1csr7vT9UbGjGkP56WCKQwTrcCZW9HcomLCPia56TshlvKrykn266g_9cZtXkiwVTSrWjDnTJjqcPSLSNLsNfgVZvHGnGm6xW_13LRNng85A_dC63mIpqONZI7O2OJkrGjTe32I_GlFnzbMHbPtEu47-6QAmTmY27oyPXcyHScKysxO3HmH4T0Mg1-lKqCDD9tvWBwM4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با شرف
🇮🇷
🙏🏼
@FunHipHop
| AmooFirooz</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/76147" target="_blank">📅 10:09 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76146">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a936874c3.mp4?token=juwImIUgx8tKmBWJ-JGZKOocE8couSRouSXEGQZMhMhgOdy1Cl2UUiXhGE6VkgPYYIYsM7rk-r13s55n1-fjI08HlNudov3uiusmKJx0kqtDzbAAmQ2VNK4HnGhYr3tkzwFET7TouyADoaz-nZUKoNsmaEsfLvuASaPGuWrIFrV-X9wqZ7xwqfvqrs1FSFjMijBO-1oEd29NNUWy7H1kCSsiyTmHBn5ggNDliL9dMIeZbK0NLkKoYds_xQto8g9z9eNJJt_003pzKz-HluTnO3Vd9j0BTLh6bry3Y5-peKeWkK-g1VegW9HFyyHr4e272vySHbbuLIcB8NBSAEAMbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a936874c3.mp4?token=juwImIUgx8tKmBWJ-JGZKOocE8couSRouSXEGQZMhMhgOdy1Cl2UUiXhGE6VkgPYYIYsM7rk-r13s55n1-fjI08HlNudov3uiusmKJx0kqtDzbAAmQ2VNK4HnGhYr3tkzwFET7TouyADoaz-nZUKoNsmaEsfLvuASaPGuWrIFrV-X9wqZ7xwqfvqrs1FSFjMijBO-1oEd29NNUWy7H1kCSsiyTmHBn5ggNDliL9dMIeZbK0NLkKoYds_xQto8g9z9eNJJt_003pzKz-HluTnO3Vd9j0BTLh6bry3Y5-peKeWkK-g1VegW9HFyyHr4e272vySHbbuLIcB8NBSAEAMbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بیانیه‌ی سپاه که توش حرفی از نقض شدن آتش‌بس نزد:
بسم الله القاسم الجبارین
فمن اعتدی علیکم فاعتدوا علیه بمثل ما اعتدی علیکم
به دنبال تعرض سحرگاه امروز ارتش متجاوز آمریکا به نقطه ای در حاشیه فرودگاه بندر عباس با پرتابه های هوایی (گفته می‌شه تلاش برای ترور یک مقام بلند پایه تو ماشینش بوده)، پایگاه هوایی آمریکایی مبدا تجاوز، در ساعت ۴/۵۰ دقیقه هدف قرار گرفت.
این پاسخ یک اخطار جدی است تا دشمن بداند، تجاوز بدون پاسخ نخواهد ماند و در صورت تکرار، پاسخ ما قاطع تر خواهد بود.
مسئولیت عواقب آن با متجاوز است.
و ما النصر الا من عندالله العزیز الحکیم
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/76146" target="_blank">📅 06:49 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76145">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">فان‌هیپ‌هاپ نیوز:
بازکردن اینترنت نشون دهنده پایان جنگ نیست/ تقی به توقی بخوره باز قراره ببندن و همین الانشم درست حسابی باز نشده. وآماده قطع کردنش هستن
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/76145" target="_blank">📅 06:10 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76144">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">نمی‌دونم چرا و چطوری ولی همین الان آژیرهای خطر حمله‌ی هوایی تو کویت روشن شدن.  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/76144" target="_blank">📅 06:03 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76143">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uc3SwgrC7dhrHdVp0_3nMIi3I4dKlx30CY4s1fXfvdxOWzvs2BLn-DP-mDAWKb-6W8EHatnk6IkJADEmrm2YhzF_w2gUEpkB7jZA7811lM7KRsr-3SAE3fnZl_gyMF8t9QTY8CEJqdIOV9aMB5UEcQK6SDpCnJk2uKTx9w_fJoFpH_P0RjkAiVEJtjB_XHAQripOvHdbSSNDNW-DodZw6sifBYDorafF6r9k2p4O0K2HNY7DlAlIKkM9VoEG00CyAWnheVtTIH3AH2iST7LUrIr5uD6aP_3JV48iYv_m49aA_ZEwoFS09PUVCdAS4FIRVCcTW_eM69NEC7SG93KYrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نمی‌دونم چرا و چطوری ولی همین الان آژیرهای خطر حمله‌ی هوایی تو کویت روشن شدن.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/76143" target="_blank">📅 05:55 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76142">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">اشتباه برداشت نکنید، قطر داره پولارو با جنگنده جابجا میکنه</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/76142" target="_blank">📅 03:27 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76141">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">به گزارش رویترز، ارتش ایالات متحده حملات جدیدی را به یک پایگاه نظامی ایرانی که تهدیدی برای نیروهای آمریکایی و کشتی‌های تجاری در تنگه هرمز بود، انجام داد.
ارتش آمریکا همچنین در جریان این حملات چندین پهپاد ایرانی را رهگیری و سرنگون کرد.
@FunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/76141" target="_blank">📅 02:57 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76140">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">فارس: سه انفجار در بندرعباس  @funhiphop | reza</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/76140" target="_blank">📅 02:28 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76139">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromYashar</strong></div>
<div class="tg-text">کانفیگ فروشان با پول کانفیگاb2 خریدن میخوان نتو قطع کنن</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/funhiphop/76139" target="_blank">📅 02:18 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76138">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">فارس: سه انفجار در بندرعباس
@funhiphop
| reza</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/76138" target="_blank">📅 02:16 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76135">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">سلام فرید جان بندرعباس صدای انفجار میاد
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/76135" target="_blank">📅 01:44 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76134">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Stcu18oHsEnnehSq_lVKNeM8H5gSzQsQO6HeyUsmyJB6dYD1JqtiRSmBMVNfAdb5529rO3gYC3RgDaa8Vpi0s4FOX2hkbj1u9nWIbF2r-zPIR0zWppjbxbIahQKfpQpTp0MYkxwU7j_qu3hwWA4aDnpy6Kf7GswY1519msMlW_xyw9WCtCySs6O3i7jscAI1AFiilUR-_q8P9rkW1_DnWfrU87ZPsg1BPp3h8Qqu7qvUjgVfXcj2TR-jcDSk0zf_dN5WFKpZKmMDaj4lLfyomO1YklHOSJHU1fuaj2-9SW0qM16E5TwbcDFYB6ibVpzsT-fs3mLkKduI9pNwQYuqgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پروفسور ابراهیم عزیزی، رئیس کمیسیون امنیت ملی مجلس:
ایران با سخنان تهدیدآمیز ترامپ از خطوط قرمز خود عقب‌نشینی نخواهد کرد:
حق غنی‌سازی اورانیوم، مالکیت اورانیوم غنی‌شده، اختیار بر تنگه هرمز و رفع تحریم‌ها.
واضح است که ترامپ، در جستجوی راهی برای خروج از این بن‌بست استراتژیک، بین صدور تهدید و درخواست توافق در نوسان است.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/76134" target="_blank">📅 00:42 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76133">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">گوگل پلی مثکه رفع فیلتر شده
@FunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/76133" target="_blank">📅 00:01 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76131">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">این مشکل سامسونگ که بعد چند ساعت استفاده از تلگرام تلگرام هنگ می‌کنه رو شمام دارید؟</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/76131" target="_blank">📅 23:57 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76130">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J2-Q5Za4LXf_d8Cp-jXADW6WeqJQBzPBXZXLv_LQHv20aYITeh7NzHG83Grp-YwE00iasAfq6vCC8f7vyXN912QZk6Qo7-OHOC6hn4Ak40Qjph0wFUzv8HW84fRBtsfdmFDjgryT0JjtUSaMKmV3ywrBXTb3INM_sUktwKppdkVnxfPs6xkHOBlZJpqowa9VyQExc-y6zTmFXiTFGFIGLr9gcjoXSnxvLYcNE17f5nhexwrqVM1D8mglxUcvTEd3WcrotaLh2wLlxR2CeAzm4sRpFpT3JUJJr-nSGGnDNBMDZR-oM3ugVc7R6KhvUAgf9nbhdgNKnn1IZtzkU6IV-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💎
1.00 ton = $1.904
💶
327,221 toman
💰
درصد تغییرات: 5.98%
🔴
مقدار ضرر: 0.113859 $ / 19,568 toman  1405/03/06 | 23:41:05   @FunHipHop | ALI</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/76130" target="_blank">📅 23:55 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76129">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CWQZpwvXLWvLhfIEZT3PG6Td68dBHyhxo0iUbE_z0VuegG3HedXvDeN1pXS6odvBjMMYenIVlRR24NHUe8DMq3egd2GdiLBl3TMXaxRSgpplNnKytwHAsWPP0OXuEsoJ1GKG0U34XnbT5yLvfN_y5H3C1AkUXJu73dFb_kHAEXHPWonHvz-x4L8ySMLGyRF5LLSrWWqxCkP5Ymk7jZC_P6yrzkhqn-zcYFeGcc4LpAtbqDqpdsCBqL1djvFiL7HLW6CQNVERlJ9mnBOqttburqkMLpKcM1cQDPn7Pre_OkaShFc-hZgl4ZDkatsZM3FzqX5mqRBF9ctwHYwiiDBUew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💎
1.00 ton
= $1.904
💶
327,221
toman
💰
درصد تغییرات
: 5.98%
🔴
مقدار ضرر
: 0.113859
$
/ 19,568
toman
1405/03/06 | 23:41:05
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/76129" target="_blank">📅 23:41 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76128">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">سخنگوی ارتش اسرائیل:
ارتش اسرائیل دقایقی پیش دو تروریست ارشد سازمان حماس را در شمال نوار غزه هدف قرار داد، جزئیات بیشتر بعداً اعلام خواهد شد.
@FunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/76128" target="_blank">📅 23:24 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76127">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">اسرائیل هیوم:
ترامپ پیش‌نویس یادداشت تفاهم با ایران را به نتانیاهو و رهبران منطقه تحویل داد تا نظرات خود را اعلام کنند.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/76127" target="_blank">📅 22:17 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76126">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eqGnSehbOQcanQC6XiphilCA6IrlbJ0tHfp8yWn_Z9srR7pMy4oH2xhypR6wjIdhxn78KO8sCure3KLLvUC4n4_yQCVrXJh9Gmlf3-jH2ahusxx3I4xqQ0PSsEMHbTcAxyTNQ8ZQZ1iwqbDy4-vrc8l6xObe3nxdnASO0J0JuQi8dFeF4X-U_YxhmyBEOTpFgMS0G7xs8fYr0xVD77K1wPZeXPq8CVMSdRbXTDH0b2zjkKe4ybYxxh2yeBq7-uyZsIOPg3T7H3IeRAPh8EfFOlcViseXW2ZC2z58946fURvHi6N_WvlUhpkak5rWITogS-N5eYyCy1bjb4PFfwoMNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نکنه رئیس باند فروش کانفیگ ایران لاپورتا بوده</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/76126" target="_blank">📅 22:06 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76125">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">اسرائیل همچنان داره لبنانو میکوبه
@FunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/76125" target="_blank">📅 21:57 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76124">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">نکنه رئیس باند فروش کانفیگ ایران لاپورتا بوده</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/76124" target="_blank">📅 21:54 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76123">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">ترامپ:
عربستان و سایر کشورهای عربی به ما بدهکارند، اگر آنها به پیمان ابراهیم (عادی سازی روابط با اسرائیل) نپیوندند، من فکر نمی‌کنم اصلا مذاکره و توافق صلحی با ایران انجام بدهم.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/76123" target="_blank">📅 21:02 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76122">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">با تایید رومانو آنتونی گوردون به بارسلونا پیوست تا درصد اوب بازیکناش از میانگین ۹۰ درصد به ۹۵ درصد برسه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/76122" target="_blank">📅 20:54 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76121">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">ترامفض:
این کاملا رژیم چنج است. ما یک رژیم را از بین بردیم، سپس رژیم دیگری را هم از بین بردیم، و ما الان درحال مذاکره با رژیم سوم هستیم و خواهیم دید.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/76121" target="_blank">📅 20:52 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76120">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">ترامپ:
به خدا من می‌خواستم بزنم ولی فقط به خاطر روی گل عاصم منیر که خیلی دوستش دارم و درخواستی که کرد به ایران یه فرصت دیگه دادم.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/76120" target="_blank">📅 20:45 · 06 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
