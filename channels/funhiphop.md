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
<img src="https://cdn4.telesco.pe/file/uIm0T3pqXlX0hc23FIrGPxlJLeKuXvfe0ignZCdQokZy-GW2J21jvP_-YP7Vmlj4KX_iHGG1AtCyx3a0qc78GVEraDJ-DVxCYSWquFSn-LBfXfiTdjrSulepeghzHEB5SYSXOHxQukzQLpZzMoBlursnDpxAzpbHiVicUnc2yvuJ0JHJcQ6FSQfrwrJvz8hT77LdyAt4Qx0Lq8aVdwXp2dXPIFDo5XY3Bn6N94meXlYDHlOHzIgFS2IleA5F8YkD7aa17E82rt-WUk__1gpyS7ANVMMt_jG_W2y_6jqGS2l5DjmITIDuMOfm2pTvPiHwog3eoUGWk6CVLc9ZAYFK9A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 175K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-16 16:19:20</div>
<hr>

<div class="tg-post" id="msg-76984">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iR96A7GLvDDg3KgvHwDbdGELlRb35AvGc-09ptlpMkxZg9VEdXfa4M8GP5tclz40Z1zNJeNBqcguCPl9TkYmsyByq3_wS1zU4ZR0mQwGjIu02XvznH3BsJNcmDWuLuNZ42ZADDO5fSaA8kaSZzjz9_zij8Q1kfq3TGfwDzgUJdPJK74TSwlGrcaQsFpFPGLzZaDbAvZNHu--F3mpCEd5aUKheRqhGtkosmiePsBE3Sl-YOAcFGZnXfTRVdJzbuSVX2uGZ3dCxCIIwQDpcFu_f4GZZPpwWyvEp-P4AFLA2mc-Cgs47RoAP6ips005AHay_Si0fjxOy6c9sJi3YVShsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه زوج اندونزیایی اسم بچه تازه متولد شده‌شون رو "علی خامنه‌ای" گذاشتن.
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 1.27K · <a href="https://t.me/funhiphop/76984" target="_blank">📅 16:12 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76983">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🗣
تجربه‌ای متفاوت از اینترنت پرسرعت از جایی سرویس تهیه کنید که تو نت ملی شدید هم باشن
🛡
🔺
سرعت بالا و پایدار
🔺
پینگ پایین و ثابت بدون پکت لاس
🔺
مناسب برای استفاده روزمره و حرفه‌ای
🔺
پشتیبانی سریع و همیشگی
🔺
ساب‌لینک برای مدیریت مصرف
⏱
اعتبار یک‌ماهه
🧑‍💻
کاربر…</div>
<div class="tg-footer">👁️ 2.18K · <a href="https://t.me/funhiphop/76983" target="_blank">📅 16:01 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76982">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mX3sQ-nnCA-v9c65q2FJ66HPC8gsWDnIqKR3EB75KJCcFcApYsxB-ORbkVu2_3BN-hrjQRuVF-HQ9HpguAB14939NJlrJudvlCxDyumEr3iZJvapUsLns8py7yXsWOUL6YTwNSXHo7FIiRyWEpzp012zmA5a2ceUdX2KN0t_JnwFpRb4OlHJAXFudmciYjfYKKcfI2Jy3gQSYoCxOgArgwHzDD2XPCiz7IWab1YyCgVFFzKH_Beh-F8GBNAYmYkaDk66GSd2co9BzUTQ2ITCRkhuG9za9nV7qakNwQv4tW16J1YcXz4lhfH3oQs8gW5UCffY9zHwbjXNg4X_sHhPWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗣
تجربه‌ای متفاوت از اینترنت پرسرعت
از جایی سرویس تهیه کنید که تو نت ملی شدید
هم باشن
🛡
🔺
سرعت بالا و پایدار
🔺
پینگ پایین و ثابت بدون پکت لاس
🔺
مناسب برای استفاده روزمره و حرفه‌ای
🔺
پشتیبانی سریع و همیشگی
🔺
ساب‌لینک برای مدیریت مصرف
⏱
اعتبار یک‌ماهه
🧑‍💻
کاربر نامحدود
🚀
با زرین بدون محدودیت وصل باش
🤖
بات هوشمند
💎
رضایت مشتری
👤
پشتیبانی
📣
کانال
🔸
زرین وی پی ان
🎤
Zarin VPN</div>
<div class="tg-footer">👁️ 2.31K · <a href="https://t.me/funhiphop/76982" target="_blank">📅 16:00 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76980">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">جام جهانی رقابت بین هافبکا اسپانیا با هافبکا پرتغاله</div>
<div class="tg-footer">👁️ 3.7K · <a href="https://t.me/funhiphop/76980" target="_blank">📅 15:41 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76979">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">به مناسبت نزدیک بودن جام جهانی خاطره انگیز ترین بازی که تو جام جهانی دیدید و یادتون مونده رو این زیر بگید.
- خودم هفت یک آلمان برزیل.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/funhiphop/76979" target="_blank">📅 15:31 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76978">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">دوستان این وسط بازی نبودا، خیلی واضح اونوری بود</div>
<div class="tg-footer">👁️ 6.04K · <a href="https://t.me/funhiphop/76978" target="_blank">📅 14:56 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76977">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">استوری جدید امیرحسین قیاسی  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 7.08K · <a href="https://t.me/funhiphop/76977" target="_blank">📅 14:39 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76976">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kqIuNraQ73HRa0MMt3SPXG-7YQG_Orfmd3MOROtadgpKq8j5zKx15_A4yHGVyDDre0WImmMVb7v7-Nb8TrrYL9G7A5uz6_rxqDEOIlE6otjVOnS8okmUtbHrfVoPcgBQrAUMVDlNxk8-TA8q0eVt74jUzEKoXd-HWxZWstxNq3kpzFQQGNBlnfu6ODwHKUArY9he_fHm3wDD62Tg7SYCW3N1KbFeaNCRqrzL2wmRmluAAONRpwTo_vkLHNFYGCexKJ9AaTCyU-R2R9rim5JKAtf2QVT8lm72M0AryRVsgAo5FyUhznri_5dqty3s0RgPBjuD3yj2XYdOoe_X198WRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری جدید امیرحسین قیاسی
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 7.7K · <a href="https://t.me/funhiphop/76976" target="_blank">📅 14:34 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76975">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">نت بلاکس: اینترنت پاکستان داره قطع میشه  @FunHipHop | Menot</div>
<div class="tg-footer">👁️ 8K · <a href="https://t.me/funhiphop/76975" target="_blank">📅 14:06 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76974">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">بهترین خبر امروز هم اینه که وزیر خارجه پاکستان یه بار دیگه داره میاد تهران قلب بذار بنویس خدایا شکرت
😍
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 7.96K · <a href="https://t.me/funhiphop/76974" target="_blank">📅 14:01 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76971">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">ادامه در پست بعد.  @FunHipHop | Constantine</div>
<div class="tg-footer">👁️ 8.96K · <a href="https://t.me/funhiphop/76971" target="_blank">📅 13:32 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76967">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CAbxlFmyi3kMk_LqGw7DapCxQ_5w37J4KI6C1wes307BubjZNiqxT732-OK5umVWP1x3pUs8X8sxAwba1hwLoloxMRNDe8wTFBoRDfx453BHaltIlp8egvCIyj7ZbK_WOySFPtrnAqbjEHBE-ssZV8XOKdCxq2cKtvNXbaWhKp1PFB2p3xufvZXWHZynmQmckrHe_oYWKmX9miBktjr0diMg4K3AHeiVk3NSbrRJsTwF_lzm1aYVw5iNrT9o44EzltJKr9x4BsvsZvFmHxvwj0gRs1-O0Js_mUYKksXocFhNmF1UyGYmKRZlnoQ0gLQhZM5JW3m8pIXuQZbxtjs4hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GwcSb3EfnZWVTT12e2PtZZ3sPesecjC7XJwCCQlKsOY2T5ttGNXfWlX4L-8yupUfhDo_Oz_zt8eDbz1nu8zPaRC-L758HBKuVfYe1Z6Xj5_ot_-aDHrM0iFEZhMAutnEw_3pTEucWNoqVcx2EMy1A85X7BpbDvtBsufaIoMPHnZWHeia4iXrHmNnkmut2c0k9CXzno47io81w7J031neTmGVA1Dx5GGACb6qty7qKgcSnq5kOhXESOFmvjlJlZuvIS-UCocmwHJKMDSQ9W7M59yG6AoV-jt2VlJ26O0F78H8fNXVebC2XVguq3C6igcMJOk5GX07MIdhbTE-pX7FTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ncg57xqyRinV5QNwYA0cedu92e0ZD2ZBPEdExLOyHB5pRSLBHfFOFdPtvTWS2MW87PKDm2SvW7TLlPnwN5lGQFyLJMhY1huaxx-Y4vHw7Qdm2yswR2NKtgylzwwrbux-vR2OTFBFTYiEj7sq--eLRAdSCk4e5zO0pYk6pGLw9--bRhpWK_WLqUVdm_wudj5XcPeqZZKldcU0y05Qy27o0yB0CF-M9U6IWKZNN9widQzOErz5Zs9D3XXbYSqPHM0i0om1bbKPFAHWA_QSglcKqleYve5p2eLLB4fRFedV2Kvp6f6jkQwS9H9eLRLoJXToBVJrz731ZR5ISeUMjusFzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iON55MiHP0KTlMLJMtuYGlVyX0tXhsLxDvXbJ5enG3ZC6nsQQuodyXCfWwoAvQykcWFu_is4aZ2pLJ4ew3PXhq2hVwZZRU0DcBcz11H2H-aGApDl3jR7pt2fFwvv_YrL-tWbm51ZRsPoo-S2dqjMFE5nP1rkJZhqBNrIcDYWTgiPtuXIhKrsHuQmGPrjf8aNffxDrdJ5VncSvczjkTGs_nDzzwpPJEStvD78--SGqzKPdWsT68ITSwFwP__VE0_qI2XLHzFEjW7O2Hm_ddyO-CjJnZZgPF6mSmxQX57SUILhVnYhNfigb_SeXxTWUTkREEc_hX1Qy0F6RNbsC6BPzQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ادامه در پست بعد.  @FunHipHop | Constantine</div>
<div class="tg-footer">👁️ 9.11K · <a href="https://t.me/funhiphop/76967" target="_blank">📅 13:22 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76966">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pwhnzduc8t4e2zmU-Wq2DdpdtqilwiOwMnpnVJLAV7YKIowSAwbUTFA1dp2kUyZkSpBJAXUizH1Ge1EM_ZyGhjEjUXHuVrCGBW1bLfzqVKA-CeWKOh-2-3MrbG4zh9Uehwm7GjixsqB6hl04U2PXdnVrAvuadnFEN6A_K1-rm1W4cnoqbj5yRU_Tw96fXZkM81rIPp5wVe9IDd-klLjIaUrdfM6gDXqHZ3TNPPnZGahjMUwa4HpWkiVBM8BEXRxZxl2cQRt6Bacb2jvQGXlo4hQokee6t5IuwCAwFZHy5HMz3Qrdhkrsmvw-prEdhU2cyK4GffLFcQF7LhfmF1wQAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ادامه در پست بعد.
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 8.45K · <a href="https://t.me/funhiphop/76966" target="_blank">📅 13:21 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76965">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tpK8isyomUSf9HDtqeLF-YESUsSjOJ5Sf5u6PqMoO2X-NAw4FKmjdrQhM7sf-UHneZOBFsG-oJAk1UQslMrrpcctnZa-AtqaGJsXJB1eTipH94XeoybQvVjH8RzMCOeMb9rttt4e3lz8uuuad-nChmHodCjE31N9CBn6G9qWQQjTxe4Myr_I07RZk7HKIfVcpN5XtPmBqK6YvINETeI75UJNtWWEkMY2fVJZt1q29n_2bvSXzt1OwLO90HK6Gz8lgacDT8Fnqf8eKhdlBCXf50W16jKHmwbkjf-sziPRRi666mzpYhjItgaALEsiSmy60SBCkaR1cloPt1OYTxVRjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الان چجوری بیاد تهدید کنه مثل جیسون استاتهام
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 8.43K · <a href="https://t.me/funhiphop/76965" target="_blank">📅 13:11 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76964">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">میگم وسط این اعتراضات مسالمت آمیزتون چرا کِل عروسی میکشید  @FunHipHop | ALI</div>
<div class="tg-footer">👁️ 9.29K · <a href="https://t.me/funhiphop/76964" target="_blank">📅 12:26 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76959">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">یادش بخیر امتحان شیمی نهایی ما افتاد به قضیه خرس و شهید رئیسی، ۲۰ روز به تعویق افتاد
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 9.43K · <a href="https://t.me/funhiphop/76959" target="_blank">📅 12:19 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76958">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l6RTogO0CIabb9nOzRrlrubxcJ7B72oy3TyPEmNCLhMaJjZsjmGyEORz7-aqMaoGns40z70tSGuRZKStR0j86aI870cCF4rmvjejY1ulcCwYtSdECEFIHTpnP88LnhZID5k9Znoz2Noz6q6wWc6E3Kc7pdBIl1YPwVGHvsN7Uj3_h_MNxc3p5n5pl7CvQu-ivhQI6GJ9sxEAL5bZdjFJsKzfOnGttYimaCMAuvU1GCjYikrACbVkXT2J6xjmxtyrTJcL5LwjubkHuCV_qjAb0b-K3RsQFDHbvNj_ro6s8zfsrytyprusxDHs68eEsUzWSLE2Ez9g4pgnp3-UNYGflQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میگم وسط این اعتراضات مسالمت آمیزتون چرا کِل عروسی میکشید  @FunHipHop | ALI</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/funhiphop/76958" target="_blank">📅 12:16 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76957">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69ce83d7ab.mp4?token=c33KDe6gqqgeYkITULKtRbB8LMUpXMmM7nP635z2CglEqMlmibRCXPKTJ6sB0oJBJ8zdEKR9OfjJ2cqW5ZcCIWajIqrC8-LX8Uw6tHeCs63ue9KEuifDaeMnfZL5RRa-C38eMbGEQHNfQCXi3WT1t2egqyVCeTKC9l8Sg3f6fYZz3Anb3zoCdnxmCnqq7_X-S7lkmG4KCsk612vWZz1-ESj-dJTotiTQlO0JjvCeyPoKDPk76qTcrew6f7Hjnid5NAbqDtg6Ki_fFJWKMo5SI57rC5PQ1cLmeqT-bkBNvVoqeCwxtPibQ-_BQYIJ-dgJETDi1gn7cTS9MS3d_EwlRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69ce83d7ab.mp4?token=c33KDe6gqqgeYkITULKtRbB8LMUpXMmM7nP635z2CglEqMlmibRCXPKTJ6sB0oJBJ8zdEKR9OfjJ2cqW5ZcCIWajIqrC8-LX8Uw6tHeCs63ue9KEuifDaeMnfZL5RRa-C38eMbGEQHNfQCXi3WT1t2egqyVCeTKC9l8Sg3f6fYZz3Anb3zoCdnxmCnqq7_X-S7lkmG4KCsk612vWZz1-ESj-dJTotiTQlO0JjvCeyPoKDPk76qTcrew6f7Hjnid5NAbqDtg6Ki_fFJWKMo5SI57rC5PQ1cLmeqT-bkBNvVoqeCwxtPibQ-_BQYIJ-dgJETDi1gn7cTS9MS3d_EwlRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">من که میدونم نصف پسرا برا دختر بازی رفتن  @FuunHipHop | ALI</div>
<div class="tg-footer">👁️ 9.75K · <a href="https://t.me/funhiphop/76957" target="_blank">📅 12:13 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76954">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">فنای اسپرز بیایید بالا میخوام بخندم بهتون</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/funhiphop/76954" target="_blank">📅 11:43 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76953">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">نت بلاکس: اینترنت پاکستان داره قطع میشه
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/funhiphop/76953" target="_blank">📅 11:12 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76952">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r0fllZ3RCduHURYfk_OOcQvD49kXG4DQwhM1pTOewbdrmn4GbMDMw7gWcLQIbXgrDpZ9xLtHXIM8sRzE_Fxq6u-M3dc807x82bRTXsgy22i2OVuY8HPKQzavLBAoD4WvxFaHZ3SGMP_qt6pRRgauA7fY0O6Yqs1brr7VB2zAF3zEY1UPJOcAYsnyDPvDQVh9bUGO2g-_nf7R9foNNClN6DXBfhkr500EqTi9WibJ03y2pfrAOj8PfNb3Q_nVQjkGIbWInmIoi0qriRHKdR4YGvXeq-2_UraNtEHn4qVqdgv0SY93pD6beC7f0E91GLCQkF4ENj3k3UcRAEaBBvVJmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیشنهاد میکنم سریال جدید اسپایدر نوآر با بازی نیکولاس کیج رو حتما ببینید
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/funhiphop/76952" target="_blank">📅 10:32 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76951">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">شایعه شده که خولیان آلوارز رباط داده
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/funhiphop/76951" target="_blank">📅 10:08 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76950">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jr9mqgIpdPXEit9T7VP4wY183Vw0w18U0DN1tc_7uDQqvLQ_66kigH0oXrD9IExr9IpEGmYCtWJU1rqKLFeUnFq_W7xKt4kdsrHqJNjATh8olat13atCx2lmeRRB4YL1-y-tTv4kY6jbwVEhDWXompwFMkRz3OSXRphsvjGCBFxkJ1G0NkpBMSfV4RM0wt4cdrAd2QxLvp94FnqiQISRrgHG0vO8LooFcN-mIAkIvzT-n-xLDf2AEdvVK4wswuQH2fiCEFCzurEUOfhNHrwawyWIOMlNPeBHX6DV0QJv_4pZIR8BVL8_kdeSX8Evgfw7kQg4hn3P07hnFeHJIEaZWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رومانو : رک و پوست کنده بهتون بگم، ناصر کیرشم دست پرز نمیده چه برسه به ویتینیا و نوس، پرز رفته دنبال جذب اولیسه.
@FunHipHop
| AmooFirooz</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/funhiphop/76950" target="_blank">📅 09:15 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76948">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YbS4mauxdHn8mp0hQoANhDPRo6gXt9C21CZ59lLaM2w75zLRb2bRthvPhebAydLKYADbQ28NttUQqeLm9ZnE8t1m1Dy2moU2TE5u2y7mipgloe26MfuPIjzaollPUW2HnLFvAt1SJAGsG_0eRag1gRjnsJvBDHM5kjnkIuuTY9fqWyQns4zY4YB_Ph2zSA3Rfl8hrqMmp-TJOi9wzJ9eOpEOrSZM4f7QmvNwcb_WFjATmxuU8ZLexBGj9_cPKuXcu60TmasYDPCSp7vlqsvGYEosemSnQnZgkD0YJagA43ZF2n7LxAwh6JCWRH-P3S_ZsFCNkbMbj_AOatA9AONZNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SI82lzNuME284R2oLHsSUEeo76BoSxUhazGvlhZdFVEOLzzIGeiq1-X02lmG22yniZ7fkZOphgiFkh7YYUs_eUlClEgo07HoJqcgKkytBLRY7EOxo5IPQy2skQG9MMH6y_fV1gkNA50m4m-e7W_tQ5mdJJtYn_da3S9cFvnA0PaP2HhN8UIWSz5UyQM3qD0gY0l_FpTb55_tvvigCW26aHKAl0fqiXkIyPKZE4osVhJewqdfLhAxv2jEASDh2Xa9MR_fqBfRNM4rfKPJT0SfKIgT-uHBfubE-rQD7v4ApzpFM9lQj25nxtkGWiLrs-8rBgQ1RdngwZvk8Nq9AH1Lpg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
@FunHipHop
| AmooFirooz</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/funhiphop/76948" target="_blank">📅 09:00 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76947">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q0lWOyyV2Td7NubYek-cj7OoIXcn86nk9ngwO5_OhCQVtENm9VpKl1TJPcok0GEBY5dBLlOt6b2FJ5QqkOtIWvMfas3mKCMDpr_CE2ChMGUogcmZRGulj6jTVHCFQGuQAl4CjXWEbe6JZ4G6_t66L8Y4uzJoVAmAPVr__nXxq7yxy873HSlkd7SBGE969JtiE8hYiSM-OsAvUH-I-MAFGef8gBD-8eAKIKJzRRKkrkvdzNFOBnJsTu3o08tcW9J0mkxz0-7vXXRFOni3itrgH_Ra2021fMnjVMnfM022QiVD0qNNxC0SXmFEPp9fwyaszGnqFbkgUYKi9ZmvYUaX8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
برزیل
🇧🇷
-
🇪🇬
مصر
🏆
رقابت‌های دوستانه بین‌المللی
🌍
🕔
بامداد یکشنبه ساعت ۰۱:۳۰
🏟
ورزشگاه کلیولند براونز
🎲
با بیش از ۴۰۰ نوع آپشن پیش‌بینی
⚡
ضرایب شگفت‌انگیز
📊
نگاهی به آمار دو تیم:
✅
برزیل در
۱۰
دیدار اخیر خود،
شش
برد و
یک
تساوی کسب کرده و در
سه
بازی شکست خورده است.
✅
مصر در
۱۰
دیدار اخیر خود،
پنج
برد و
چهار
تساوی کسب کرده و در
یک
بازی شکست خورده است.
📈
میانگین گل در
۱۰
دیدار اخیر برزیل
۳.۴
گل در هر بازی بوده است.
📈
میانگین گل در
۱۰
دیدار اخیر مصر
۱
.
۹
گل در هر بازی بوده
🎯
پیشنهاد پیش‌بینی: مجموع گل‌ها: بیشتر از
۱.۵
- ضریب :
۱.۱۹
🧠
اگر مجبور به پنهان‌کاری شدید، مسیر اشتباه است.
R16
🅰
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
💻
@BetForward</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/funhiphop/76947" target="_blank">📅 09:00 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76946">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">روابط عمومی کل سپاه :
بسم الله القاصم الجبارین
فمن اعتدا علیکم فاعتدوا علیه بمثل معتدی علیکم
ساعت ۰۱.۳۰ بامداد امروز چهار فروند نفتکش متخلف با تحریک و هدایت ارتش متجاوز آمریکا بدون هماهنگی و بدون توجه به اخطارهای مقرر نیروی دریایی سپاه، قصد خروج غیر قانونی از تنگه هرمز را داشتند که پس از اخطار، یکی از نفتکش ها مورد هدف واقع شده و متوقف شد و دیگر شناورها متخلف به عقب برگشتند.
به دنبال این واقعه ساعت دو، پهپادهای آمریکایی یک دکل مخابراتی در قشم و یک دکل را در سیریک مورد اصابت دو پرتابه قرار دادند. در پاسخ به تجاوز ارتش کودک کش آمریکا بلافاصله دو پایگاه هوایی آمریکا در کویت به نامهای علی‌السالم و تاسیسات مهم باقی مانده در ناوگان پنجم نیروی دریایی آمریکا در بحرین هدف آتش موشک‌های بالستیک نیروی هوافضای سپاه واقع شدند.
به دشمن متجاوز و کودک‌کش اخطار می‌کنیم در صورت تکرار این شرارت‌ها به پاسخ محدود اکتفا نخواهد شد. مسئول عواقب بسته شدن کامل تنگه هرمز به روی خروج نفت و گاز شما خواهید بود.
و ما النصر الا من عند الله العزیز الحکیم
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/76946" target="_blank">📅 07:07 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76945">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">باز شب شد آمریکا جزایر رو تصرف کرد سپاه هم آبراهام لینکلن رو غرق کرد.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/76945" target="_blank">📅 03:59 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76944">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">شب جمعه خود را چگونه گذراندید؟  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/76944" target="_blank">📅 01:52 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76943">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">باز شب شد آمریکا جزایر رو تصرف کرد سپاه هم آبراهام لینکلن رو غرق کرد.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/76943" target="_blank">📅 01:05 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76941">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">الجزیره:
15 نفر از اعضای تیم رژیم جمهوری اسلامی واسه جام جهانی ویزا نگرفتند
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/76941" target="_blank">📅 00:38 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76939">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tmY_03rIr4cf8ksqy3bScozeigAcVxH0F_utx8-QzTu2wgf3EN-yuDenG5LUercEsbPtvqfNtvadeFgJCBuYOUFPNrwNbsZYdALopkyJKg2MiHX2P8miDxoqfGZcd7NHEeGOnjF3pDxelDL9jWjp6CwdFri3kh1D84gKQ_5yy2ED4pHbcq2h5DydWYX5PvY8YtrXb6WXfVkgBPTQOwegnnwKaSr-db1ib0SD1x5H01GtEJVEftgBN6Ln0vbLifu7BeoemFjDQAH6sJD-8DXAM8csNKniMZWRykr2-8hMyBF6kpeK2xM5wINC1UG_BXlOXVfJEweu8cynQjrMQ1Zjuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MbjRaHXMnong5r-Y9A9Fi-D19ZBRbpKWSAyACHe4yQ6iCoZ-hZvdk_52BO8i944Abk3O2PBdvkdaubATsDz7QOH_G5AblxqGgC49GcDNGIfmcsB773dnkj0etwxSwWCA1PGyVwaVi44jRNGiHaDggQWKBC2X0HYdZD3PvzjduiQ-GKxwqpmbzEqK2STMFCOK1nLakR3NZb41GsMacKzz0uuP8ndg6qfXyEvSPokESNThuhiobs-2FLJ64xlJVnQbNLiRJqVqgEHPPZVwckANK85L_pBgrEthfAGv-WxRzukIgvmLrWfs5cPEpouDj_6oI53fnM1zAPUK1ch4oq_HXQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ناو هواپیمابر نیروی دریایی آمریکا(لینکلن یا بوش) دیروز در خلیج عمان و در فاصله حدود 280 کیلومتری از سواحل ایران دیده شده.
در مقایسه با موقعیت مکانی این ناو در چندروز گذشته
این ناو 50 کیلومتر به سواحل ایران نزدیک تر شده
!
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/76939" target="_blank">📅 00:18 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76937">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4adf695bc9.mp4?token=HXj5IatdA05ixK_sPMaHIVSa0s87rpQlJZhiRJtQ2xE8YGo55VC2A0UShk0FltVtihiWajhFlpcpxw_PgeddNjZqoG89us6JGS2M-9qLjkn_-cCGJq9mR1rxbEAvPlGDBjRtZzOcywjj0UR7cxiOOVFZbSWRGIo48a6RaG87jdEFcVDWc6gebTqIdayIz06UE7bxvxl4BD9qVbGaQp-_ilXaEIVLHHjWGoUwxdpvMGXF4gLGsr4_KYOnmoYPYk81iR1BDBuKAk0KQ3Q-iAaHrF645Cwc-lwc10gQXwtEl4sUA-fwnQoGvITKkamUeyoXGdYDPl_qHzpSEfTpvvlHNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4adf695bc9.mp4?token=HXj5IatdA05ixK_sPMaHIVSa0s87rpQlJZhiRJtQ2xE8YGo55VC2A0UShk0FltVtihiWajhFlpcpxw_PgeddNjZqoG89us6JGS2M-9qLjkn_-cCGJq9mR1rxbEAvPlGDBjRtZzOcywjj0UR7cxiOOVFZbSWRGIo48a6RaG87jdEFcVDWc6gebTqIdayIz06UE7bxvxl4BD9qVbGaQp-_ilXaEIVLHHjWGoUwxdpvMGXF4gLGsr4_KYOnmoYPYk81iR1BDBuKAk0KQ3Q-iAaHrF645Cwc-lwc10gQXwtEl4sUA-fwnQoGvITKkamUeyoXGdYDPl_qHzpSEfTpvvlHNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بنظرم جی دی ونس  گزینه بهتریه
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/76937" target="_blank">📅 00:09 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76935">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">ی سریا میگن یوتیوب رو نت مخابرات بدون وی پی ان بالا میاد، تست کنید ببینید واقعیه یا نه.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/76935" target="_blank">📅 23:56 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76934">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3980333f44.mp4?token=Ejf4Vkh7GNW0z-zMPOGu8FViWXNf1ksB1jDnvW-Z2Souya5l-nI9ohmfUc4IVI3w3f7XL8aOH5wWR9YH0rd4XHTKfH5rxgpTVylVjJNObDiMiLl8ITkjn9DHrKkWTtNaZF026d6fNJ8utGMDOyHrmZR2xFRiVq3b4T3fElnEMWINaKziXUauDNiHeBUp9gh6P0gckQCirx0zDasWsGDuT9IiveqeI3yhz3aHx0AAEcdXE4iROFE_HO-u1DiXEH3io7zhwAXz6DMFFOWyPpRo2vqIi1Ei3vTjLvAfDgEwzHt9XlO5EK_qVVrGqs6zyFPC2tHAaxkBAMn_bO6YdHzF-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3980333f44.mp4?token=Ejf4Vkh7GNW0z-zMPOGu8FViWXNf1ksB1jDnvW-Z2Souya5l-nI9ohmfUc4IVI3w3f7XL8aOH5wWR9YH0rd4XHTKfH5rxgpTVylVjJNObDiMiLl8ITkjn9DHrKkWTtNaZF026d6fNJ8utGMDOyHrmZR2xFRiVq3b4T3fElnEMWINaKziXUauDNiHeBUp9gh6P0gckQCirx0zDasWsGDuT9IiveqeI3yhz3aHx0AAEcdXE4iROFE_HO-u1DiXEH3io7zhwAXz6DMFFOWyPpRo2vqIi1Ei3vTjLvAfDgEwzHt9XlO5EK_qVVrGqs6zyFPC2tHAaxkBAMn_bO6YdHzF-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">موزیک ویدیوی شکیرای مناطق محروم (زن مورایس) برای جام جهانی هم منتشر شده
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/76934" target="_blank">📅 23:08 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76933">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">مهدی ترابی بگا رفته و احتمالا جام جهانی رو از دست بده
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/76933" target="_blank">📅 23:01 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76932">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">آکسیوس:
به حضرت عباس قسم مذاکرات یه جوری خفن داره پیش می‌ره که پشمام پسر.
نشونه‌های عجیب و غریب مثبتی از ایران دریافت کردیم و مذاکرات به شدت سازنده شده.
ویتکاف امروز رفته بود با کارشناسای هسته‌ای آمریکا صحبت کرده بود تا ببینه شرایط نگه‌داری اورانیوم ایران تو آمریکا قراره چه شکلی باشه و آمریکا یه تیم خفن ۱۰۰ نفره از کارشناسا هم تشکیل داده که این کار رو بکنن.
ما به شدت به توافق نزدیکیم جوری که اختلافای الان رو می‌شه تو نصف روز حل کرد مثلا آمریکا می‌گه بعد از توافق باید تو ۶۰ روز مذاکرات بعدی رو جمع کنیم ولی ایران می‌گه نه ما ۹۰ روز وقت می‌خوایم.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/76932" target="_blank">📅 22:37 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76931">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">خبرنگار:
فینال NBA که قراره بری تماشا کنی، ارزون‌ترین بلیت اون حدود ۸ هزار دلاره. خیلی از مردم عادی آمریکا توان خرید چنین بلیت‌هایی رو ندارن.
ترامپ:
خب، می‌تونن از تلویزیون نگاه کنن. دیدنش از تلویزیون مجانیه
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/76931" target="_blank">📅 22:25 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76928">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">واقعا فاز اینایی که میگن جنگ بخاطر جام جهانی متوقف شده رو نمیفهمم انتظار ندارید ترامپ بخاطر تیم ملی ایران که ویزای ساعتی بهشون داده بیاد جنگ رو توی خاورمیانه که تموم بازیکناش کصخلن , متوقف کنه  عملیات اگه انجام بدن تو خاورمیانه قراره رخ بده نه وسط زمین فوتبال…</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/76928" target="_blank">📅 21:54 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76927">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">لطفا اسراییل رو با هسته ای بزنید دهن این قمار باز رو ببندید
ترامپ:
ما در برابر ایران موفقیت‌های بزرگی کسب کرده‌ایم. آنها در موقعیتی نیستند که سلاح هسته‌ای داشته باشند.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/76927" target="_blank">📅 21:52 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76926">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">واقعا فاز اینایی که میگن جنگ بخاطر جام جهانی متوقف شده رو نمیفهمم انتظار ندارید ترامپ بخاطر تیم ملی ایران که ویزای ساعتی بهشون داده بیاد جنگ رو توی خاورمیانه که تموم بازیکناش کصخلن , متوقف کنه
عملیات اگه انجام بدن تو خاورمیانه قراره رخ بده نه وسط زمین فوتبال جام جهانی تو آمریکا
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/76926" target="_blank">📅 21:48 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76925">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/76925" target="_blank">📅 20:39 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76923">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">برنامه سیاست با علی و تحلیل اتفاقات منطقه در طی 24 ساعت اخیر
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/76923" target="_blank">📅 20:30 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76922">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">طی 24 ساعت آینده جنگ میشه اگه نشد هفته بعد این پیام رو دوباره بخونید
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/76922" target="_blank">📅 20:25 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76918">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">این از دکترمون
اون از دلو که فتیش زیر بغل دختر داره
اون از داریوش فتیش عرق پا و بدن دخترو داره
اون از حصین که فتیش بی غیرتی داره
من کیرم تو حوزه ی فعالیتمون
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/76918" target="_blank">📅 20:15 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76917">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAmirhaz</strong></div>
<div class="tg-text">بیاین بهم پس بدین وطنمو
چهار ماهه آزگاره نخوردم پای همسرمو</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/76917" target="_blank">📅 20:04 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76916">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">مامان شام درست نکن نمیایم خونه
ما عادت داریم شصت همو بخوریم
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/76916" target="_blank">📅 20:01 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76914">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">یکی از روی عشق و حال پا میخوره، یکی مثل توماج توی زندان نیروهای جمهوری اسلامی مجبورش میکنن که بخوره. پیدا کنید پرتقال فروش را  @FunHipHop | Constantine</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/76914" target="_blank">📅 19:52 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76913">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HcqwksXuY0oynVIn-FKlK2XpI7ylMpRyL8idnaduXOvOGZZjZuXuE8qp9NWUgQx9jbtIOki10vWPzHRyE8f2ixT5AUM-0KKhl96JKrWCf-sgpAny73rbMJiGowuNHxMoJOF_FdWdwMVhiE3epCmNQH3F9A1TyfPuSBqmlF71emjHr-k0UqexfNDLszhqkZ7D1CaHvvV6MQ5Sus8KIEHw1he6V60akDz1dFxaZFGe_M4-FRwUH_mjrlwAXjoyA4Qnv2xnIgkYp8bf_-tILmK2FvVDPyLketC3YajIRsfm70tds86BhWEhXdUbEIh3jP_-I6ok9Kn--1OAJJN3XRdMTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از روی عشق و حال پا میخوره، یکی مثل توماج توی زندان نیروهای جمهوری اسلامی مجبورش میکنن که بخوره.
پیدا کنید پرتقال فروش را
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/76913" target="_blank">📅 19:50 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76912">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">دکی: برید پیج گوچی مین محتوای خوبی برا پا دوستا میزاره
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/76912" target="_blank">📅 19:41 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76911">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9bb569f0ca.mp4?token=XPz_UIDc2U6Acod-MnJ0kwClp4Tn1rIanPN90qJrd9OOcj-FqrVEMfzruj4sQuwR0AU9qKzQEeIq-QHjSBsgruebGRqoq1chLVcBzH_tJSjmiC4UdfOBjC5BOo0kHglRN5mQk_vqFui-zkjPig0yRe_bK5zKJBw2E1mOSZANSh4HV-gwO0rWGFN-zThFGtIa4TTq9CmIZI_hPCGkko3MDsf6U0UiDPeqBSv6M4O_8mjLL1dNozDVZMg5UKZgA4uBdPdLf34b_4L-kGNTOyCiyvAMwbV9u-n0Cw34VSFOet2waMD2LBn1PEnPtaglr9AQgYca-Q_cJIX1zlV0AnE8Bg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9bb569f0ca.mp4?token=XPz_UIDc2U6Acod-MnJ0kwClp4Tn1rIanPN90qJrd9OOcj-FqrVEMfzruj4sQuwR0AU9qKzQEeIq-QHjSBsgruebGRqoq1chLVcBzH_tJSjmiC4UdfOBjC5BOo0kHglRN5mQk_vqFui-zkjPig0yRe_bK5zKJBw2E1mOSZANSh4HV-gwO0rWGFN-zThFGtIa4TTq9CmIZI_hPCGkko3MDsf6U0UiDPeqBSv6M4O_8mjLL1dNozDVZMg5UKZgA4uBdPdLf34b_4L-kGNTOyCiyvAMwbV9u-n0Cw34VSFOet2waMD2LBn1PEnPtaglr9AQgYca-Q_cJIX1zlV0AnE8Bg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ریدممممم ویناک عکس پا خوری دکی رو پخش کرد
😂
😂
@Funhiphop | AmooFirooz</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/76911" target="_blank">📅 19:40 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76910">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mTmGGSVEMvsoHohNOpqmb4GyE-Y5Qp7Epq_8-qnV_ofN2v6UPo2JU8U0XU86XGkneyrG_UH_iBerYkRymu4dAKQ8pkYT9rL1uX3AM8UmFvyaYSKpqtVsIWwgYgiCwjyFu4uP6g82FnST4nX-E-eW_6fiJhLmQGKV-SgLXCpQ5cQ-jbFSDJrwR-HUtINr3j44memG3TPbQ4e91icuUt0ciftUkFE3XsZ8jefMwlKFM6Pt8cJYPgF3mMT5Oz9cOhO04oyhKW2knH0nQ2mpl2U0TPe43ye5T85WW6Run1n2rI28WCHquBk5DMRDuqMmdLgjsx5Oo4KUEvKqfOU2ZhwOiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بمیرم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/76910" target="_blank">📅 19:25 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76909">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/skx9b4nzDLdWhliEiAyoBzKmA9P70K12BgrgUThmuW-UNYM_p0giZ9auxEsvsQo-qUz02gdUO1H6sK7RLJwHLMxTsttV-771oqEHGYvPgVQt6B4dOVBYx_FxkwfEGGySqHHZz_Pv8ANsvUQgB9gipn8hxJys_W7dCBGCmQ5BGA01WtZm5t9NA1rNlwnXoii_PbEjxolpmfq7uNPvlwn5u81F08LKcOboOTnGjc1Oq0caMlhq8XOTucdI6_Pi4rmAedGw4RL498hudD9XQci2dDX_PWHcH9qzqW7xcCdE57YIBYJHOYjfMm9be4SWlOiIV8TmrkrfT2gsnBH2DtY47A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بی واسطه بخر
۱۰ گیگ ۱۸۰
🚨
۲۰ گیگ ۲۸۰
🚨
۳۰ گیگ ۳۸۰
🚨
۴۰ گیگ ۴۸۰
🚨
۵۰ گیگ ۵۸۰
🚨
با ارائه کد تخفیف hiphop  تخفیف ۱۰٪ بگیرید
سرعت بالا و لینک ساب اختصاصی
📩
همین الان پیام بده
🔤
@wevpn_admin
🦄</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/76909" target="_blank">📅 19:11 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76908">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">بیت کوین بگا رفت و به 61 هزار دلار رسید
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/76908" target="_blank">📅 18:56 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76906">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1e8ce80ae.mp4?token=FDalUVr7cCo8r_tlAS0Yn256LE_5tjUEUhSgf6AF7jsADzz5bFd5yxeSggIeAgekJ-sJYlY4oMhXozPQSix2IOctSzHxLstwj-RamQ_bzampktdW_ENk7cnCjHxbjPSVtLmE2n85SPoOd6Fp5QgvtnlitBYnM_5kP0mobQtUdY-GTLLlvLkzCMpmj8ffUqBLCvCu3k-r2OQpgIsUSxrjzyWeicJShkE_aHb9-b64ZkrsdpyMT6DJzyNSJMd_bbKIp0He35Z3bDPoGLRvNe2GPxQmJxCGaFkgHriWmHRlkH7_iaTmdEWaO6vnLNm0iQe9yr4nFYNDQFPMJ3F9T6Snjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1e8ce80ae.mp4?token=FDalUVr7cCo8r_tlAS0Yn256LE_5tjUEUhSgf6AF7jsADzz5bFd5yxeSggIeAgekJ-sJYlY4oMhXozPQSix2IOctSzHxLstwj-RamQ_bzampktdW_ENk7cnCjHxbjPSVtLmE2n85SPoOd6Fp5QgvtnlitBYnM_5kP0mobQtUdY-GTLLlvLkzCMpmj8ffUqBLCvCu3k-r2OQpgIsUSxrjzyWeicJShkE_aHb9-b64ZkrsdpyMT6DJzyNSJMd_bbKIp0He35Z3bDPoGLRvNe2GPxQmJxCGaFkgHriWmHRlkH7_iaTmdEWaO6vnLNm0iQe9yr4nFYNDQFPMJ3F9T6Snjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فیت دکی و خلصه بزودی
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/76906" target="_blank">📅 18:24 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76903">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AhtKlyonaPZujM8bCFmKFoV-3IENZZyC7Cio0zS6unsC38_QVzHnJ-rXIGvtFswy9dvhJB3MqgHLihOpOBpJRvhwQSfNDZN9iBUIiLcUT95ZJJosIXE5QX0g2tk3grQKISTpNZGZ83Ods-ml0sgQCrDtDX1pear1Mr1LKdstI1Kv1G-iuTb0yv3nvooycXTuhAJofbBmkQnObdz93OMoSodQap7cW9_wj4pNkIDSaO9V0PoP5JCCW5LYYVGTga2y1RjG168CTm3ovFaRwo55gPqZ3yW7zWbvGh7nbrOZt2zuWV7cNAKrV5JATMoePh8fheXAAXMi0SpdBMHVJjWUvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برنامه هفته اول بازی های تیم ملی توی لیگ ملت های والیبال
@FunHipHop
| AmooFirooz</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/76903" target="_blank">📅 17:52 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76902">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vCH9HxO5CW4UxD4hFBirGSEvMJ0u5VIScUpOzyfw2Nk029vOyovnMMvZj6ARDXzv8zlVhmV8y1YYzWtw8W_6goYD870L_QK94gLLYZ6xEnz5xRbdaU0WDsQdzrdFDxexErinfWAf8tdKNOp6IugI1WkfsuLkrW35BSk-IuYNSBEYsc24XPBUAGNV4CJcO69mU-ZlOfZbVXwE2jGLXSDmRTXwcIA4W0lt7jft1091W42ZIc3EtBanoS0DTAZEi6g4h2nOjwObmBqKuUx-PT10ynQesqOOOxKkyMlYYKVCGDUQpEzfFAgozy9ZcZfYYBtdxUzy4xiFnSmZOvZh0IJ_ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلام رونالدو فن یادته سر این بازی چقد مسی رو مسخره کردی؟
@FunHipHop
| AmooFirooz</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/76902" target="_blank">📅 17:45 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76901">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">app.apk</div>
  <div class="tg-doc-extra">51.3 MB</div>
</div>
<a href="https://t.me/funhiphop/76901" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🆕
اپلیکیشن حرفه ای لنزبت
🤩
۱۰۰٪ بونوس اولین واریز
👏
اپلیکیشن را روی موبایل اندروید خود نصب کنید و بدون نیاز به vpn وارد سایت شوید</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/76901" target="_blank">📅 17:45 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76900">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c1aqyPRy4IZ5UPgqUyZhWM_7ftTT2crNHaeiAMWBjuvJYjEcE2QH8QaRdLGSNAtoU4obAihskUlkwHoCC2oESuAitaH38a4yeaL_G2TCMLFNYyEzfCERDZa37bTZGrta98e6HrjY4BnmVN8wLf1JtsHbo9kuVaLizLARBheQRZUpcSnRTKUDDm7JEjeFqWsro9LGHNpfU1sEE7FQHkO4BVdFTv4s_GA2pzoyvhXaMWLaEvKTEuh8by8DUsItbQITYMlIRZW0OhehIWWnn9lrFf5jrBH0HrY12bqXyNKgtz6rMgqktzIqdmP2fVFRWPUeEUuYWs_MW4Y4Q7XH3UIFtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
لنزبت بهترین و حرفه ای‌ترین سایت پیشبینی
🔥
🏆
↗️
بالاترین ضرایب و متنوع ترین آپشنهای پیشبینی درلنز بت
↗️
🔣
0️⃣
0️⃣
1️⃣
بونوس برای هر واریز
💳
شارژ کارت به کارت آنلاین و درگاه
🔠
🔠
🔠
🔣
0️⃣
3️⃣
کش بک هفتگی
🧑‍💻
با انواع دیلرهای فارسی زبان
🪙
واریز و برداشت انواع رمز ارزها
💵
💻
همین الان وارد لنزبت شو و از جوایز ویژه ما لذت ببر
g15
🅰
🔠
🔠
🔠
🔠
🔠
🔠
🔠
📱
http://Lenzbet.cloud
📱
https://t.me/lenzbet_official
📱
https://instagram.com/lenzbet_official</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/76900" target="_blank">📅 17:45 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76899">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">راستی یاسینی هنوز تو زیرزمینه یا بالاخره فرار کرد؟
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/76899" target="_blank">📅 16:00 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76898">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qqYl1sy8MpCpRCyZ1J5E_HxFbk7KTB4AU96HDsklQ_6l4CGoGn9G28jD5-D2LUJ-eSKlz2VUC9F8Lp8pl3MIWKyxiOnwQI9b-RDZdvsYQAvBKcaIvobwvU8RuNWUceRsxbL1MkOdZPNOyHP0m0aHPclOQJ32rtk0KdRVSNohVVmeT9txOco5N148Wik0u-701nZ6D2TvepHEiqkZKiTfJFGt7HyCorRAB09CtO1TZWvKoKzhHWvm1QK7HhlZbwTr7ccASmuWLsYExZfRHuyhBsSzdIg51WLr8yxhfm21X74iTG9i4X1T4CMghEl0F6OYQg5_04cVNfG-3bQT_432FA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میدونستید ملکه جدید فرانسه بزودی قراره گلشیفته فراهانی بازیگر ایرانی بشه؟
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/76898" target="_blank">📅 15:09 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76897">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">نروژ برا جام جهانی عجب حرکت خفنی زده  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/76897" target="_blank">📅 14:46 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76896">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uf2A9RlzmI7ISlGwpd9IQZUVrFb9kC8U-wKPfOyh-wlftbLRLwHAhYnxRgGoazN9Ws-vU5WvrqE2Txv1nRyunQ0uon4DsrznfrLIqS0H6HIVg3uEKT9TbDM--G7gdsESOksvT3qhgxEgA9totQBpwKTtmFknHRKP20ko6sMsX6QzgRWH8uhj_oXXfZZ99lE6qXfkkRFf6CvVgo-tNwi0AkqF2PatgoA6T_0Z1V3bKvQYAwgyCqUwZC4O5sOc5AvamnqjEDejbyk6mplptHf7_JVvyD1wD4yDwsNyDrCnNJf_3myHs4kAi6vWS3IfJFhWn_4Ji_p7y6BegaVecQaQug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نروژ برا جام جهانی عجب حرکت خفنی زده
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/76896" target="_blank">📅 14:29 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76895">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">نزدن رعد و برقه نترسید.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/76895" target="_blank">📅 14:28 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76894">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">اسرائیل جنایتکار حملات خودش رو به جنوب لبنان دوباره آغاز کرده، خواسته این مردم حمله به صهیونیست های کثیف و حمایت از برادران لبنانی ماست، لطفا بزنید، لطفا.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/76894" target="_blank">📅 14:20 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76893">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">وای اگر قالیشاه حکم جهادم دهد.
@FunHipHop
| Sogand</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/76893" target="_blank">📅 13:55 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76892">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E9YiWFCFdr982_XE0yJmYxEe6gsQB0d6rZaviD94HIDIx6Ut6V3LfnVz-u8T6Rsrln56Y3xcUJezvotHwIySwe7cobMn-sf7xztyNh-EixyhyXCyfvtjBWUjafPS-abwNMBRBtmx0s-ZG69NNP4x7cCSpimfL7_3BfBcvkOIHoJuiFN4TjYA1_iA1ac3Iso-xw9Ce1FqWEv-xSo6QYKPRNEn9RJlVU_tUcor1_WdQKUa4aV1KGcsd8jHk1PiaTtl5P96xcOC-L7-tNjV3b3x0fJLtxWBseUuaSH8vHzIM4kEVnoP3jbdvR2ipxyc4DWnUJm6LQSoFtlxfNsBNTi05A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/76892" target="_blank">📅 13:40 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76891">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">مرکز ملی فضای مجازی:
طبق بررسی های فنی و ارزیابی‌ های عملیاتی که انجام دادیم، قطع اینترنت الکی بوده همچین تاثیر معناداری روی خنثی‌ سازی حملات سایبری پیشرفته نداشته
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/76891" target="_blank">📅 13:32 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76890">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a4cedd5da.mp4?token=A4vpj2-WDrDaTM7k5hTpBT2BHOoNYPqq_kGu6-CXGXEod5Lf3hvHRlmZHy38bP-zGmXB4-Oxu4YK5zWAp88Qq4or9JnJjHzNhZJisGH4bk3kcqymLdiKlxg_GFQT5q9AHPpbzDjLlQtnTAEc5mSQsrKjtUDe0bDqXT-aSKnGb3EbsR4Lr2U6e7LDoR5vNt5ilIzkMUYivrCv7nB2rMIyoXOQTttar3XAVNLq8O34P8exy0NiptWEsZONTmUhj4yTXnNibpdApmFPmWy2rM1XJINl5YejZmWIdvrgy5w6J8f7cuWLbKue2XKITswmVT3_9o4jkNzT2Jq_3dSKMt-IsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a4cedd5da.mp4?token=A4vpj2-WDrDaTM7k5hTpBT2BHOoNYPqq_kGu6-CXGXEod5Lf3hvHRlmZHy38bP-zGmXB4-Oxu4YK5zWAp88Qq4or9JnJjHzNhZJisGH4bk3kcqymLdiKlxg_GFQT5q9AHPpbzDjLlQtnTAEc5mSQsrKjtUDe0bDqXT-aSKnGb3EbsR4Lr2U6e7LDoR5vNt5ilIzkMUYivrCv7nB2rMIyoXOQTttar3XAVNLq8O34P8exy0NiptWEsZONTmUhj4yTXnNibpdApmFPmWy2rM1XJINl5YejZmWIdvrgy5w6J8f7cuWLbKue2XKITswmVT3_9o4jkNzT2Jq_3dSKMt-IsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اوه اوه جنگ داخلی
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/76890" target="_blank">📅 13:17 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76889">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">تون 1.5 دلار شد
Make Pavel Mom Great Again
#MPMGA
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/76889" target="_blank">📅 12:30 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76888">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">تو هند 4 تا دختر یه پسرو دزدیدن بردن بهش تجاوز کردن.
پسره الان رفته برا باکرگیش شکایت کرده.
دخترا هم دستگیر شدن.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/76888" target="_blank">📅 11:48 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76887">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">ممه های دوسدختر صادن کو</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/76887" target="_blank">📅 11:29 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76886">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cEUF43qTVp--ZXMytRd5sxqQ3pjMu69YtY2s_DDAG8FRb90U0W137-1kALrUpOHwjzb5VXGSDKjyWeAiDiLrRyLi5L6CaZUjIvBn5_Gw0vgjE5UaWkMwBRbE7CoEdQjfNBdL6F19ZBMKtDurJ2A9ADI31BRT9AMyY2m5BJGHiKms1GjuJbRIat4NIjknb4px4N4Mvw15SRHc-6EJdW9x_xO46YVJmLdSxJ-zpHZ6FXI3RTL9lhnGKRaxQ8t1Ko43r0SLrwdogqLiWqObECKY7eBJu2LmV_3UPE3m2F8GgTCgSPNybWXWAVZrg64Z3XDB-QUN5soonD6kpm5GptVopg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چالش حدس پا.
@FunHipHop
| AmooFirooz</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/76886" target="_blank">📅 11:16 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76884">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tn5anJi_ae3QqwFbFo5Vk6YOE1F2noxQGWG7nc6RIVBB_OjLLybN21qZsEx7H7xity2T-m8eIRKhEdu6HDYmNNNdDx1vJoG6y92cylK2y-F_UMBxStjwDjsPPSs4tF_nyq0RRAJNVTSkR2kk2FPYqgWNssVcL-3NxoyxGVQIQBM7aHycz77DTmasUxU5eTpOtfugXah04d6VK8HmnNrT3n2XMi4qthM3Gg0y_F8FIlCShNewAsLJb93vMEUvgIh9Xp-VqlKG0PBN_C9-kIiC4B0iOZolGC5juBmUbOebQIhGC5oxyFHUlfN63DtVuakq64MeTvd5MX4Y_91wbKtyoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شاید براتون سوال شده باشه که کنعانی زادگان چرا انقد مادرج چیز یعنی موفق و بازیکن خوبیه، باید خدمتتون عرض کنم مربی خوب داشتن تمام ماجراس.
@FunHipHop
| AmooFirooz</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/76884" target="_blank">📅 10:07 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76883">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K0hhpvDyHgiYG8DGVN5lMYrLaQ6tefbFq7K61vGk3Xo6e1jLulLnW95w88qpe4W6seMkuBJi6710pZTz40XfNbP3wx5zmMQ7A_pxwm4G3WZSMJp7kqGI7gxgIQ6m97f94uRddGhs8f1R47N24qBMAmBZpjbtfn2ueKwoAxxGoJGNEBW3sbADrZnp2mdS_KvK4L22Yt2_-fIUebCS8pMJALIDYuA7LPOrieY5oo_KBWe9poyPE92fxT_Prp2mFUI4oOUUKw8t6BSYaEqSKOt9hrY7YryBKqOR0HxBrTVOyfR1Er4aMA60H9ePIPhvqev_l-5LFQsAniRO5MVqh9GEoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رفیق حسین رحمتی بودن مزایای خودشو هم داره
@FunHipHop
| AmooFirooz</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/76883" target="_blank">📅 09:55 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76882">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F5pjKvX_PG_JxzzOKS6Mz50Qqs6BOKFbqFtkbyrERtXXeS9KvdSab5W45ghPOEHfMXQNLMDhUvTfqRX6VUI9wZePWNYrBqP4thd-BOql3CnCoSQ1osVRZYSbgRdtXosQknGPcNLP668psTgJwppycXz-Lbp7fjOZ9zDmJihll6n4dbVkG7KcCS51wpaFwT7vTO9HWsc1l7-SLf-Y8ol2da70bPNqwUTnWlergiWj3D_AGEBypuwXPeJANVQvKpV0xlwa9xPxvFZIYolWoHuZ08lZtpBVZpwxEwgY2KoZfH9KPi8A8r8jABiAm6s4v3ohI3221XwXN4OiY_LwtTnI2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
پرتغال
🇵🇹
-
🇨🇱
شیلی
🏆
رقابت‌های دوستانه بین‌المللی
🌍
🕔
شنبه ساعت ۲۱:۱۵
🏟
ورزشگاه ملی لیسبون
🎲
با بیش از ۴۰۰ نوع آپشن پیش‌بینی
⚡
ضرایب شگفت‌انگیز
📊
نگاهی به آمار دو تیم:
✅
پرتغال در
۱۰
دیدار اخیر خود،
شش
برد و
سه
تساوی کسب کرده و در
یک
بازی شکست خورده است.
✅
شیلی در
۱۰
دیدار اخیر خود،
چهار
برد و
دو
تساوی کسب کرده و در
چهار
بازی شکست خورده است.
📈
میانگین گل در
۱۰
دیدار اخیر پرتغال
۳.۶
گل در هر بازی بوده است.
📈
میانگین گل در
۱۰
دیدار اخیر شیلی
۲
.
۵
گل در هر بازی بوده است.
🎯
پیشنهاد پیش‌بینی: نتیجه مسابقه: پرتغال - ضریب:
۱.۲۰
🧠
پیش‌بینی آگاهانه، تمرین شناخت خود است.
👍
ورود به سایت با فیلترشکن
R15
🅰
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
💻
@BetForward</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/76882" target="_blank">📅 09:54 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76881">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">ولی همیشه داغه نفس اژدها  @FunHipHop | Reza</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/76881" target="_blank">📅 09:14 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76880">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JMx0A0Z-YOAEsQ-ccegVujXG9V35X2hDKrURXQXMtgtSHbcl7ZSGtzEFQh__yX6e1JVodCTtGuqNxQOiBbRImyBid68OX9UoFFmVxMtsD1piDTMnRAduXQkSn7LlMydiqUuTCXrpjv7FAK-ZsDhK0wSJpoyg6Rupstxcu_wtKXypZ-kaRRUjDkmFE4l8Hhe7Zh3RgABt-h27LHmyB0uiHo0azO5TeCn17l-62R4Lggrey2ayjWHe8HPiDt3VUrP_OrleoRe4HIl49e2cDLLwFwI4dkYljkZ_Ur8qSmo6VewC08MnKGcmL7L3di30k91WtCRHiqUcUZ-F9kPBSjw4Cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولی همیشه داغه نفس اژدها
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/76880" target="_blank">📅 08:45 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76879">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HKuwrDvSrNkh-7ZsALPZxY43e5BRB6ASobppttMixp_znYpg7kSGTmBKR5Sw6NvmOeNOMX7kFqGD5gm6E5KCpm_M1eIk6zxkAjk0N8SeRe2uayfPr74PO9bEbBRZAPYXYlbDVVwRySEH6GcQdfZ7KfdgZbtImoAgSGQ07voQFJ5b_l66a558WXfbXOufyDENdXx-4g1kykGoKQshTSlFycoaCC10BiIxfAjHL0Aj6Ds1RJEK693oobCfUJjulXHddbf7HmTvonzsHOWlZjjlBHJ5OLxj-JC0j-kZnsOzfw_ekswMmaeHX8FmEYBBjxrj14juOAv19gp9AO9HmWiN1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صبی که با آلبوم جدید Blok3 شروع شه تا شب باید بخوابی سرجات افسردگی بکشی
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/76879" target="_blank">📅 08:29 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76876">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">لری جانسون افسر سابق سیا و تحلیلگر امنیتی مدعی شده از یک منبع آگاه اطلاعاتی دریافت کرده که نشان می‌دهد ایران به کلاهک هسته‌ای دست یافته است!
به گفته او و پپه اسکوبار، پس از حملات اخیر آمریکا به قشم و بندرعباس، شورای عالی امنیت ملی ایران تصمیم به فعال‌سازی «بازدارندگی نهایی» گرفته است.
ایران از طریق نخست‌وزیر پاکستان یک اولتیماتوم سه‌مرحله‌ای به آمریکا ارسال کرده که مرحله سوم آن، انفجار یک کلاهک هسته‌ای در خاک ایران برای اثبات توان هسته‌ای کشور است.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/76876" target="_blank">📅 02:29 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76875">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j8FZZ2PmHwfbMtTMauURyxtdQYlPcs8umhiKUyR1NZ3Ml3hJXkT9CMUD4bMBwCy9MkrF4Hyz4dFCXD5_UBlzgeuAwIK3gy32fHEgug0Dbs1UOjo-VxqRfQ-kuqBKM6lbK_NnOQ77KZCXkCAr2UyecWq1YUojbS0w9AvA2p3qMc1qQaynqlC83vRSVf8OTPngMMs-kuIiRfbEhreMSq79f0reEC0I2jqWFfLTBnkrmLWwVDQVylC_A-t_H3IVoL7XWGfDj4PuRMCL7I0jFv1zhmBbGldTcD2NY6O8-eIRosqQUf3LsXZCHnh4mbRsZLF_FKk-WN7eSfv4EovY5Y6lbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دفعه‌ی قبلی که این اتاق جنگ اسرائیل از این دلقک بازیا درآورد فرداش ترامپ
پست گذاشت
که همه‌چی آماده بود می‌خواستم فردا حمله کنما ولی ببخشید لب‌های عاصم منیر مهم تره.
الان باز اتاق جنگ اسرائیل دلقک بازیش گل کرده و خواهیم دید این دفعه چه خواهد شد.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/76875" target="_blank">📅 02:10 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76874">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">برای بیانیه نیاز به اشتراک Plus دارید.
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/76874" target="_blank">📅 01:59 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76873">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">۲۵ بهمن ۱۴۰۴  @FunHipHop | ALI</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/76873" target="_blank">📅 01:49 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76872">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">#NewAlbum Released
🆕
🗣
Artists: Future, Shakira, Tyla, IShowspeed, 21 Savage, French Montana, The rolling stones, Lisa & …
📋
Title: FIFA WORLD CUP 2026  @GangStship
🇺🇸</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/76872" target="_blank">📅 01:28 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76871">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromGangstShip(blue)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g2JGMBafLRPK56ZJFGFGFd6fcGvBUkRwNLN-Pre04LlJVr7O3aLuq-dTKRIBZljyepncLJ84UqpgwrdoMJmapDwOukpxMCsLjkKyNc6fkP1SSi_mE5E2EkQLQZpbrMHM7RjCABullrjVtpYDE6M-wjG3q9TFHHfoCRWojHIsI8h-54xeO80wgObb1NJWjQUKc22MXbCSlog8AasqYQC75gkDIFFnwb5ldxnnkZ3q2w0uNnRiBTyAo19fZO14TaRcchGJAqWSxJ5q7MdvNOa_xTdwN9EP-J8XjvVCIrEcnhol5p509yto5vbRD0jv6qqUjDSJLGfrJMBej421xsq9uQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#NewAlbum
Released
🆕
🗣
Artists:
Future, Shakira, Tyla, IShowspeed, 21 Savage, French Montana, The rolling stones, Lisa & …
📋
Title:
FIFA WORLD CUP 2026
@GangStship
🇺🇸</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/76871" target="_blank">📅 01:27 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76870">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AzrA-SKTi7uGVrmVLL1XBimN5uIZ7AbM-Bzlk6uKyh82-OzE3rCHIA6OgRw3fCbg10DXZ3JU9__TlwFTsjTNJukKx9R1JOoGFryUN6IG8cn6klQCVhFB88oeNAfV__26POP1uXY80ZUgozhCVFbxQE22prnpHTWfNEtMwqCJkgMii0V45PlL8XpPPClcZD0TzD8-1YyF98_cEdyOUsLkUGI0jpoOKG2NYPs6SZ5Kqja0X4u8WKyuV7s9hTb95w8x60ypUaeuyny6hhoXvOq-V3hidNMtukN0b3f_jp4m3QdTF8CgDfCTy3ZyW40IQ2-251ABGj46s01q5-Gfty4v_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: من نمی‌خواهم با آیت‌الله ملاقات کنم، اما اگر با او ملاقات می‌کردم، برایم افتخار بود که با او دیدار کنم و در این دیدار من محترمانه رفتار می‌کردم. خبرنگار: شما پدر، همسر و فرزند مجتبی خامنه‌ای را کشتید، چگونه می‌خواهید با او کنار بیایید؟ ترامپ:  خب من…</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/76870" target="_blank">📅 01:05 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76869">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">شب جمعه خود را چگونه گذراندید؟  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/76869" target="_blank">📅 00:22 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76868">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">ترامپ:
من نمی‌خواهم با آیت‌الله ملاقات کنم، اما اگر با او ملاقات می‌کردم، برایم افتخار بود که با او دیدار کنم و در این دیدار من محترمانه رفتار می‌کردم.
خبرنگار:
شما پدر، همسر و فرزند مجتبی خامنه‌ای را کشتید، چگونه می‌خواهید با او کنار بیایید؟
ترامپ:
خب من قطعا فرد مورد علاقه او نیستم، اما احتمالاً او یک فرد حرفه‌ای است و آداب حرفه‌ای رفتار کردن را می‌داند.
او در برخی محافل شهرت بسیار خوبی دارد، در واقع.
برخی افراد درباره‌اش بد می‌گویند، اما خیلی‌ها درباره من هم بد می‌گویند که نادرست است.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/76868" target="_blank">📅 00:08 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76867">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">ترامپ: جنگ را یا از طریق مذاکره با ایران یا از راه دیگر پیروز خواهیم شد، اما قطعا پیروز خواهیم شد
ما سایت‌های هسته‌ای ایران را از فضا رصد می‌کنیم و هرکس به آن‌ها نزدیک شود، همانطور که باید با آنها برخورد می‌کنیم
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/76867" target="_blank">📅 00:00 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76864">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">یه طهلیل ریز بریم
آمریکا تنها یک شب بعد از هشدار دادن به شهروندانش حمله رو شروع نمیکنه
در نتیجه حداقل تا جمعه هفته آینده خبری نخواهد بود
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/76864" target="_blank">📅 23:20 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76863">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">میگم جنگ تحمیلی دوم چه روزی شروع شد؟ صبح جمعه؟ فردا چن شنبس  @FunHipHop | ALI</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/76863" target="_blank">📅 23:17 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76862">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">میگم جنگ تحمیلی دوم چه روزی شروع شد؟ صبح جمعه؟
فردا چن شنبس
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/76862" target="_blank">📅 23:14 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76861">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">وزارت خارجه آمریکا هشدار سفر به اسرائیل صادر کرد  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/76861" target="_blank">📅 23:11 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76860">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">بزودی حملات ما علیه اسراییل و متحدان اسراییل اغاز خواهد شد .اسراییل 15 سال آینده را نخواهد دید</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/76860" target="_blank">📅 22:49 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76859">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">وزارت خارجه آمریکا هشدار سفر به اسرائیل صادر کرد  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/76859" target="_blank">📅 22:34 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76858">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yy9ZdIi8BhMvy4rbLGHab1LJGAbsbdE1HGQluLP1FS9tOORL9eCuzb394MPOWTu8tjrpNQ8A1SP3Ia2wTkMQKOydGwAO3ncs0sFdZXIgEoYrYPIAomklXjzj9at8NukgvqzPDBl7fdxA8Z13YEPjQzd73X157KeFxp9EyLhlVwWHttWxO_VFZIkR5FkX1zz52tcuOmdWM0TmLEWypje5IOXjI6KyaHP-zwyX8sJAXZjDiDQShLGE_g1fs05SxzyRY8giqNEZ8dkZ5bVGeHubd3NextHEUEpERTVputaKdEwpa_vrFqOwFYBjXc0G-kcjOCGx9epFXrG7yf_hIcLcwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت خارجه آمریکا هشدار سفر به اسرائیل صادر کرد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/76858" target="_blank">📅 22:33 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76856">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">بخاطر وجود بزرگترین تهدید علیه جمهوری اسلامی یعنی پوریا پوتک  @FunHipHop | ALI</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/76856" target="_blank">📅 22:18 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76855">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">تلگرام چون با ایران همکاری نکرد و مشخصات کاربرهاش رو نداد فیلتر شد اینستاگرام و فیسبوک به دلیل نشر محتوای ضدحکومت فیلتر شد پورنهاب بخاطر داشتن سوپر فیلتر شد  این وسط نمیدونم یوتوب برای چی فیلتر شد    @FunHipHop | ALI</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/76855" target="_blank">📅 22:16 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76854">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">تلگرام چون با ایران همکاری نکرد و مشخصات کاربرهاش رو نداد فیلتر شد
اینستاگرام و فیسبوک به دلیل نشر محتوای ضدحکومت فیلتر شد
پورنهاب بخاطر داشتن سوپر فیلتر شد
این وسط نمیدونم یوتوب برای چی فیلتر شد
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/76854" target="_blank">📅 22:14 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76853">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tkQrApO0NtvN-zTlEnII6CVzVDah1rXBaI9TDqcxKtHePCDEq8iYDDCkiuBXlsZQqfgWZUMdr9yRaTIIXLufDgSbwE5qvrCI0vFgR5pZtjUwwCxM6UcR5bVc9Ucdwx3qODZKbeDQ-M9x8UYizA3eYCdv61Pi0deSjVodkxQxidBYq4XIdlR52UcELhs9rSjOLDbiYyT5SjZqh_IfTS3wh23Rc79c3xjj_Dcl7vbxLpFVvDIPqOYooTqYubrTp-9pK2hvEs2dHZd0KpjEwYkLSxv7pZ8vEvaLMzyvsnTIseOVdgfZTEqtUU2odwctHsay3NlMOX9lGLF8ZOkkw3tU2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت صادق
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/76853" target="_blank">📅 22:02 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76852">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aYKOesB1Ie94UJBj2eI5EbnrtWD_SUeca5t3Ia96k0tAj9tp5jW_jUVIuVgTufY1_TS1YoYsXUfPkeHnSN8GiQTS-7l8-TfJsdoP1I5UgshtP7bhBKrfLiHh8wWTOYMtfvzAqKzLrBI69fpx3LtC1_Cz74CPE5ourANO6WNkx7PYw1hiCc51XVy6RVt5ZfXZ4IG9ite3bAXjYPdSCKbpm9VD-ZAfqR_3XUMDJSu2yGp8retrYYe0T387djIuSchWxL-duar5ByTZihPTAvPQ0f5E4OHlJS39RszRDJ_wOfKpfmW2GbWkTQHXNuGPLYVMJQzC9aov4bDZk7EWySb6rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کسکش تحت تعقیبیما
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/76852" target="_blank">📅 21:46 · 14 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
