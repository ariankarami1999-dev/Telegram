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
<img src="https://cdn4.telesco.pe/file/Lsv8vrJmWs7dCo4aRLyxfGyVD5RW8iMEp4i_borQ2Ow2SZBPiVGjf1v7ohb_dH81uHeMt0nH5ED9BoHADVlz68eo6Zdn5-sTrmRgUZ5qwQSn8iN5Qo0rxCaVYWC2Ass1mlWo1wAV_on2AE9gpmdl0KhtnjZQZBQUeKOSSTfAk_cTenZLT-Lu7BwfLxYO_heU9D0s6xt_EGcVSTuZIdWJyxhpSuLZrMFB1_bSpQBf5sMeODEfQCoKW7OphKUkzuy4kyCL58NJAonai93wkfIp1RAayTmb-3re09CV3uprefRQHlI2ZP-yJONn1KZdkmJXSXM0NK6EXKWhuXBFJajCqw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 174K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-16 03:13:42</div>
<hr>

<div class="tg-post" id="msg-22861">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f73764a80a.mp4?token=lqHmpen5w4EqNJF_nnBRjvB48a8h2KGVSPVEiqY1dMgrpUymKMB7vGfhoxo2wIlXw_8V7EKzl2FH4LkG6wjmWl1WhPKPC8Ljy6yObEM3Xx8X7CezsQpjG365rN8hIE5AoAY-cLOCJ3jcB14IQqf-aMBkEtVToFtkc_ozwIwMprW8oaQDOjQ2yTZRU8kkph1MrKX-fw_zteWozLRPxtdhMxbGPojQIytFXnTYOWpmsSavhCzNQVUiezLYgmNZLgdnCaSQHTjapdJ8q0yAHJvUw2eSCu1YIJIeuYHOGXynt3N-KE9gxKyutRsXrnAsKqS16f8AVRTk0Q3vjcmjhThMhaKT4_Zrmku0umCwKNdcfuGLPa0Sm1OCV3gOiw76oieTjra4GqdIncSftxeijc3ae6oe3PvfF5T8SARH98v9ejMg6G1K9-o5_TLP6kgseC72glevnoGeruwB5ummjlMOqrf1PkTWbKqnR2eCdGBo5r96mGt_xgYu_GzBRmi90ReZ9HaGWKFPQXEVzjbRAfF1tVz75pkZCbD5ZTjlWPu5eqiKKqq41UxcsBSggD4EgF-N0OX3XNwQFLmq3IiMT_EW82xEiB31ZbifPGsbBO9HblADeNNu2RCmsPEqswWCh-T9QUvnjkclEJNq24oXyip4XTXXLfDMkzcQzQ1lPKfMNRE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f73764a80a.mp4?token=lqHmpen5w4EqNJF_nnBRjvB48a8h2KGVSPVEiqY1dMgrpUymKMB7vGfhoxo2wIlXw_8V7EKzl2FH4LkG6wjmWl1WhPKPC8Ljy6yObEM3Xx8X7CezsQpjG365rN8hIE5AoAY-cLOCJ3jcB14IQqf-aMBkEtVToFtkc_ozwIwMprW8oaQDOjQ2yTZRU8kkph1MrKX-fw_zteWozLRPxtdhMxbGPojQIytFXnTYOWpmsSavhCzNQVUiezLYgmNZLgdnCaSQHTjapdJ8q0yAHJvUw2eSCu1YIJIeuYHOGXynt3N-KE9gxKyutRsXrnAsKqS16f8AVRTk0Q3vjcmjhThMhaKT4_Zrmku0umCwKNdcfuGLPa0Sm1OCV3gOiw76oieTjra4GqdIncSftxeijc3ae6oe3PvfF5T8SARH98v9ejMg6G1K9-o5_TLP6kgseC72glevnoGeruwB5ummjlMOqrf1PkTWbKqnR2eCdGBo5r96mGt_xgYu_GzBRmi90ReZ9HaGWKFPQXEVzjbRAfF1tVz75pkZCbD5ZTjlWPu5eqiKKqq41UxcsBSggD4EgF-N0OX3XNwQFLmq3IiMT_EW82xEiB31ZbifPGsbBO9HblADeNNu2RCmsPEqswWCh-T9QUvnjkclEJNq24oXyip4XTXXLfDMkzcQzQ1lPKfMNRE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
#تقویم؛ یازده سال پیش در چنین شبی؛ بارسلونا لوئیز انریکه با مثلث خوفناک MSN در فینال لیگ قهرمانان اروپا یوونتوس رو با نتیجه قاطعانه و پرگل سه بر یک شکست‌داد و قهرمان این رقابت‌ها شد. این آخرین قهرمانی آبی اناری ها تا به امروز در چمپیونزلیگ بوده است.
⚪️
…</div>
<div class="tg-footer">👁️ 7.07K · <a href="https://t.me/persiana_Soccer/22861" target="_blank">📅 01:48 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22859">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KvWXUl9u7LKfSNid6Bfjp5C7w3AWyWhgy2KEp6jHLwrjgEhPg3uQnFNlL_MkkPFPJ73cs00hiUoW5iNhTw8Mee4fuylwgmC8KsVSH-uptuH0-qxZiqBXuh0yfHIMbKEEI2HyKa7yheQU_k01CD46a1kxCCeAnszkIKIcpmdg1MQP6U6kgEcpBEfPVgx9X7H-brlqi6SDX9TAkwl5p6er5mBFy5xiPE_IOcjlMMlbrqJbdSdfKcy95SgN68dsgBQ2qvvsdIXh-UgWaYI_kG0frwum1D3CXsdzniNFgbwQ7VVasHrtPYMG-fnAjrVrLhBL5OPJTp7nkk3Qo2VkKkCcig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YVj1Ro3fze3ZaRcQN9DHdnCXjjOhk_kUq0xupB1Fw-ESCAITZ_AincdHV7kZtBWLiWKSoaokNcOm7T_y7bMMLErhw84tCYNOOuslww7941btqN19yePUHDR37QNrYmKUMWVZ0C76iUXdaTFgGRhS8r45pS-WwiFnHtBfcvCqv8sSRoCGkyI_nkRpVzNrylxCS6TCN8rQbcKg7iimGhBbN_tyWfmdYcFaFcWYL26Kap_mexCt0prskaKcXZADn0WDO0YZdd2DDC7mSUvKP_P96beVsZn_BUXN176qmBtsAEHmrwfSLAGJNgODWqq8qt5sec7UIa03lTlkQNsD1ckm5A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
#تقویم
؛ یازده سال پیش در چنین شبی؛
بارسلونا لوئیز انریکه با مثلث خوفناک MSN در فینال لیگ قهرمانان اروپا یوونتوس رو با نتیجه قاطعانه و پرگل سه بر یک شکست‌داد و قهرمان این رقابت‌ها شد. این آخرین قهرمانی آبی اناری ها تا به امروز در چمپیونزلیگ بوده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.31K · <a href="https://t.me/persiana_Soccer/22859" target="_blank">📅 01:39 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22858">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sxbe76dDtgfdWKJq-5pDYWZoZro1OowoMZOO-0U7idsmRDolVYgDU5TXI3XjJjJp2svl0GopClCulqWuguC9NYmvuBEje7lLEcUzrCFbXtK5jH_fBtzRifnQxRXvwguvCWFXjiEWzu9epTQWadPA4QHhYjqSBt4dUVWVMZYcX4vcLw0Vq-OGttT71ecn_UMjTD8Q5tE9M8DCz989fXcnNb1tFlpvChu-ZWGjGSVQkR5dfPOAcMzOP0j9-GK-uIXaP6R1wN06sJ23wbUI_mKFrlc978KSFG9NRR4C8jHf9fw4H2m9PWGwJXAD7LVRCZr4TxlAaSDwh2e3xFQD-iP9UA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌کامل‌دیدارهای‌‌‌امروز؛
ازجدال‌یاران رونالدو برابر شیلی تا تقابل آلمانی‌ ها با شاگردان پوچتینو!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/persiana_Soccer/22858" target="_blank">📅 01:11 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22857">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h0I7b2C8DzHbpBmo92lZJZJAJU9tFWBurYZwFtnz4AVdOfo6Tj_JKay3YxIURHoz5tIQF_SRpNdPI0LGGpHnbBbI2ho5AJTfx7r9rz7JjQ_iM8kF4yeqt8T9s30nfp9bX9Cs9cLWwK2JQLTUo_Pg7N6K8gKHq_Iqizaoxs6cE_lnnd18zC46gTnZGEEn-g96EK3YNDBdks0wA9oOM9ke3cHORcCV3pgtC3DUPuhPQuvlSRg55iNsgLVXRc4AO7P5qPLVVuhy-31r4FHI9y-IJ7wQuPJXW52ZEvmYSDTN5y6HpqxrsONfThKR79ZnQoYLiS52yNx8bnpVef4Xyedauw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌ دیدارهای‌ روز گذشته؛
استقبال مکزیکی‌ها از جام‌جهانی 2026 با جشنواره گل برابر صربستان
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/persiana_Soccer/22857" target="_blank">📅 01:11 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22856">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/grxtckkKbczK_Vyiu-Cq3hkLPJ_7gfu-E_RAaMAiglfX0I5lLxM3M9wu1-EyB-52mTS83xnlKt0QDFFbHlSipYa9IXyu365oosy8Xf_-XH9vvJJtl2K9gV3aFgOwji0xQTrnmQqNs6qvDf4ct-5Czoq39UyDYAWQ3822rfsOOWkJGQoT1w7il2K0_ZWNUpZDkRc40HehrthEX4eIeRCVKmDRXzm6xxEDwGFAQV27uPCVzEWTFdPOn3RwJ_DkPALuVOKOZGZpHEe1lbI0ZWN74XvKCfb0t6Yp7LMPGnm_Gc1u5C0eqp3qJ5LROiHgglT5g40Xqfx4bHS6dEE-4xTJbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
شوک‌دراردوی‌ژرمن‌ها
؛ لنات‌کارل‌ستاره 18 ساله تیم‌ملی آلمان درتمرین امروز این تیم بشدت مصدوم شد و رقابت‌های‌ جام‌جهانی رو از دست داد. ناگلزمن سرمربی‌ژرمن‌ها بلافاصله آسان اودرائوگو ستاره 20 ساله لایپزیگ رو به اردوی تیم ملی آلمان دعوت کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/persiana_Soccer/22856" target="_blank">📅 01:06 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22855">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uqwoczyQp0iqmK5wNCWxPod5zT8u4BnxJbvpF9YaZAVIsSqsx-7bMSFc9fGA0g_jViB2D667fjtHbFDFO_kX0y369IsLtx1Wulxmfz2llxpwVfmXuu2zc-tWM_BxGT2DFXHq6jC37lAfqAvFPrPURIJ_jxMgjv8DfRteDpQFF_qlSVh6p_GxySuj-bvT9d-emBYBCsDIzSOl4HGobouQU7h_PAG_QqFrHa0_KjWcDphvLBHR0J7znBpthhj03yJ1MT5UN0lRZ9Ptq530Weia6GopJprn7K-Y3Q3OZHk4wlaKuao5SqpLkATvRb6n1Iim7EZdGlR3InKpjBAJpMuFOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی_پرشیانا #فوری؛طبق شنیده‌های رسانه پرشیانا؛ محمد جواد حسین نژاد ستاره ایرانی ماخاچ قلعه بزودی از این تیم جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/persiana_Soccer/22855" target="_blank">📅 00:48 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22854">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/moXOZdWmGZua0El7pokyHMObL71dk96GLOZBKDGW-84RRnWuFSVsf2xD7J4Pagmi6T41Ra80caIH5-pxxsNzhnigDMRnDr8RtqLBKW1X0FIl1GlGKwHY3ntxPqmH8qR1AYd_zXKzNNAc_WEuMZ0TK49La61Hyuo7xmR09C4h-OOQTfvIO8haZMQOXxQ9wGVzgIzhqvODVWQfPJ6xoP48PaJueKy3z5f3fzf3COPcLPGnhETne6qeswZRitSs8dAAScKxhy3TMkAkqoPF6Uss5h4yXMvSliGBdpTh9a7oK7CBbSzHMLdpbRi5Z3BVWFQP2v4tevEiScmHQItC0pzwCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
چت‌جی‌پی‌تی،دیپ‌سیک و گراک بدون فیلترشکن در دسترس قرار گرفت. همه برنامه ها دارن رفع فیلتر میشن جز تلگرام،اینستاگرام و توییتر؛ سه‌برنامه‌ای که بیشترین استفاده کاربردی رو دارند باید فیلتر بمونه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/persiana_Soccer/22854" target="_blank">📅 00:35 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22853">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e00cf6e9a5.mp4?token=BKdIxgA5xJM4Z6hiiOhPEYn6hTdfNyDKSWXoLWRlshdzm5HhmtRmBUx5IZI2lcHJywveT_anURyRWHQAUCuEb_YItCgfzEhkwW1WgUmE7cQF-9j90YPHU1EP5cCJaZsgew2wFyL90lddyAp0h-dnx9tgGkooa9XVQiN6r5yxuoohauC8leIIVEpJyc0cCUHgfriDUrzvQyJneFkH_xDvo7CympEQe5_sd1CDy_M9wFc420srAaaQR9SNX3vsD9X0dzX3uPj7FY34mu7sbgmMwiwlmQFl4e1KugBNaVRfUX68QMS7fiZx7CWtl-pHIKJfGw2dLkjiev8otKCCQh1GYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e00cf6e9a5.mp4?token=BKdIxgA5xJM4Z6hiiOhPEYn6hTdfNyDKSWXoLWRlshdzm5HhmtRmBUx5IZI2lcHJywveT_anURyRWHQAUCuEb_YItCgfzEhkwW1WgUmE7cQF-9j90YPHU1EP5cCJaZsgew2wFyL90lddyAp0h-dnx9tgGkooa9XVQiN6r5yxuoohauC8leIIVEpJyc0cCUHgfriDUrzvQyJneFkH_xDvo7CympEQe5_sd1CDy_M9wFc420srAaaQR9SNX3vsD9X0dzX3uPj7FY34mu7sbgmMwiwlmQFl4e1KugBNaVRfUX68QMS7fiZx7CWtl-pHIKJfGw2dLkjiev8otKCCQh1GYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ابراهیم کوناته مدافع جدید باشگاه رئال مادرید هستن دربازی روزگذشته با ساحل عاج؛ واقعا مدافع قحطی بود که فلورنتینو پرز رفت این رو گرفت؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/persiana_Soccer/22853" target="_blank">📅 00:35 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22852">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e488d912f.mp4?token=XyfnDN0ki4gc7-S0etGYfqQVTf5uYknBoKs2jKXLUuHtAjr2VQ4MU8fISUis8UxNMULbfT6D2ko6Gt6eJEAC-xmHa0wpI41VRWo0mfZHcfzAmJM_EVoJLQjAN9v4JGkaH4IkHkvVD-frh54GwZxHAKa3pnlLsncNQ0_r2KEVGo43gPCk3rR2B9XpqE8X1nRMecViON8TT6iEJ8UIn1Ijzs75ctm8sA86948ONFRKZWl-NABx2ImRfMci-7GhKhDsXEqJxzBYIqFBe12lF73SS8BFdMoSFP2uFqwqMHrMD0fThuZ6mN3fuSEGrXS_iKhOozwH0w0Haq-TOrfu6iATJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e488d912f.mp4?token=XyfnDN0ki4gc7-S0etGYfqQVTf5uYknBoKs2jKXLUuHtAjr2VQ4MU8fISUis8UxNMULbfT6D2ko6Gt6eJEAC-xmHa0wpI41VRWo0mfZHcfzAmJM_EVoJLQjAN9v4JGkaH4IkHkvVD-frh54GwZxHAKa3pnlLsncNQ0_r2KEVGo43gPCk3rR2B9XpqE8X1nRMecViON8TT6iEJ8UIn1Ijzs75ctm8sA86948ONFRKZWl-NABx2ImRfMci-7GhKhDsXEqJxzBYIqFBe12lF73SS8BFdMoSFP2uFqwqMHrMD0fThuZ6mN3fuSEGrXS_iKhOozwH0w0Haq-TOrfu6iATJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بچه ها اسم این بازی عبور مرغ از خیابون  هست ویدئو نگاه کنید خیلی راحت 8 میلیون ازش سود گرفتیم
😍
😤
اگ‌توم‌دوس‌داری‌خیلی راحت از بازی های انلاین پول در بیاری حتما عضو کازینو شبانه شو
✅
توی کازینو شبانه بهت اموزش میدیم از بازی های انلاین پول دربیاری
👌
کانال کازینوشبانه‌راهی‌برای‌چند برابر کردن سرمایت
کسب درامد انلاین با یه ادم حرفه ای یاد بگیر و‌ پول دربیار
💵
🎯
همین حالا عضو شو و شروع کن
👇
e15
https://t.me/+6ckCmywafrxiYzk0
https://t.me/+6ckCmywafrxiYzk0</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/persiana_Soccer/22852" target="_blank">📅 00:35 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22851">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FYSxX4nUlH4JvAKib2UZ0r3PXf2ajZmmCPG_GUZk_2BOOdnIpvb4835WnJcM5q-y1OzjQVlQ5CSWpkWJtULUwn9Xscmn-2RGOWz_BYRERfVH8F1zNFt6ofhHPZCW669Fwdwuk2TaO5JW1e_Z4ohqu_8sc7ZpWrfGqP5CRvnBcK5eVnpG6E0HQNh3DPaKIb5hr9I5XiDo3y-sYvcOb1dai_hk2dubO0n-XEFMFJQuukvkO6HiXc08JAuEkn-Pvopz-fWRNDfpS5wiXeQgw21LfEwS8t7OkQpf5nTapC3gMqo2RLE_DEb_W9GgWfnGdL6ASfhJ_88F5nT07XtZVCXevQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
علی‌‌تاجرنیا رئیس‌ هیات مدیره باشگاه استقلال: یک‌‌نفر از اعضای‌هیات‌مدیره تیم استقلال در طی روز های گذشته با مدیران باشگاه آلومینیوم اراک صحبت کرده‌ تا انتقال محمد خلیفه رو نهایی کنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/persiana_Soccer/22851" target="_blank">📅 00:08 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22850">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IZ5DYk-uCAp-xJJsR0ovcPvA3hXBBazUe-kVdIDMjHZNe5R2bxZHBvvZeowQo2qyAntr8w4Be1ztOQj2ifxoJ9EWcQmok714VkAaSrsmcW1VcXDWhzKZ-9KhX2JUCfUEt9RktcCSj20fa6k7MtLhOnEvpNlOwNmBZwBI3_iB0YQ7AE42_wA03pyn_LfE3OEOFoWPbobmv2czQ058MuEvsabPInsIZZtfvQfsMPegOgkNwKpOGZAwST7IOPTwyzEd69sJv8ZFwvCmGidJZMQhfnX-3l4k039mU2kyGYkWPyjx_ZqVn7mI0NVdyA7ckUhJOxzxFmF1xn0HM8uUHvIsqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ انریکه ریکلمه: درقرارداد ارلینگ هالند با منچستر سیتی بند فسخی وجود داره که بلافاصله بعداز انتخاب‌شدنم‌بعنوان رئیس باشگاه اون رو فعال میکنم. به تموم‌رئالی‌ها قول میدم رئیس بشم هالند و رودری دوستاره سیتی روبلافاصله رئالی خواهم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/persiana_Soccer/22850" target="_blank">📅 23:51 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22849">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aedcb21ace.mp4?token=nrctwEdoF1iNq670drOZ9L1YMie2qih-ZH6lhHr5TwVZguTwhIV9ajhMAwM8RxFBNUxBcK4Du2hMbjdn_31iHRLCH0oX5UyubZauUW2dS5pVTtpYBgNaiTJkZoWERhhxFdAHoiMtG4Wr1PNLLUJnK8j7kz7jjcAvvb1kNy6MGrBo1t4VDx9bhbJugdEtXGnOlnQdgKDcfCBrmkCS6wCg5gjb7jvRktaAwCs3dGNNVUR-w4sKB14u_d2HvUPRmJxWuWZCA0PZBzyk7__RfjRfoBX-gmSjpkJ5uOofKql8cQnuSojQOuX-oUtAixMpauT2TmQxxLA_ZzDJ9AAYqXCNAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aedcb21ace.mp4?token=nrctwEdoF1iNq670drOZ9L1YMie2qih-ZH6lhHr5TwVZguTwhIV9ajhMAwM8RxFBNUxBcK4Du2hMbjdn_31iHRLCH0oX5UyubZauUW2dS5pVTtpYBgNaiTJkZoWERhhxFdAHoiMtG4Wr1PNLLUJnK8j7kz7jjcAvvb1kNy6MGrBo1t4VDx9bhbJugdEtXGnOlnQdgKDcfCBrmkCS6wCg5gjb7jvRktaAwCs3dGNNVUR-w4sKB14u_d2HvUPRmJxWuWZCA0PZBzyk7__RfjRfoBX-gmSjpkJ5uOofKql8cQnuSojQOuX-oUtAixMpauT2TmQxxLA_ZzDJ9AAYqXCNAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
طبق‌شنیده‌های‌رسانه پرشیانا؛ باشگاه آلومینیوم اراک اعلام کرده‌است‌که هر باشگاهی محمد خلیفه رو میخواهد باید 100 میلیارد تومان ناقابل تنها بعنوان رضایت نامه این بازیکن به ایرالکو پرداخت کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/persiana_Soccer/22849" target="_blank">📅 23:43 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22848">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e230120d7d.mp4?token=iZUYuSwWDO4PIBInTdjRW1zjtNdxgsmKqzl6y7yUgomMnG3fpnQLbdWiLjya5wdXkZe4pFHGpfEi_V12TObapxs2Km-iJ1UOQ9Rlhiaoc-I1EYWvOkN4h9uai756WkpynBqz7mtadXHgaNDBXUeIfGCImxlkoMg7_pzIasD56VRHmKTXiJj_0c_Bz1SXGGZg3l0VPezeBsFtrP8aVtmRjxFFwrNYfcMgwgNX96_p4QrLTSyN2EsICDVIP63x4vkjkTa3fQfc6ntcHFFcVF-9SbnN_kNDpPRNjDvefR3I9eWI0dXNVPemMS3b6F5XK5t4OrFH-8AvD7fONjHvu4HHgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e230120d7d.mp4?token=iZUYuSwWDO4PIBInTdjRW1zjtNdxgsmKqzl6y7yUgomMnG3fpnQLbdWiLjya5wdXkZe4pFHGpfEi_V12TObapxs2Km-iJ1UOQ9Rlhiaoc-I1EYWvOkN4h9uai756WkpynBqz7mtadXHgaNDBXUeIfGCImxlkoMg7_pzIasD56VRHmKTXiJj_0c_Bz1SXGGZg3l0VPezeBsFtrP8aVtmRjxFFwrNYfcMgwgNX96_p4QrLTSyN2EsICDVIP63x4vkjkTa3fQfc6ntcHFFcVF-9SbnN_kNDpPRNjDvefR3I9eWI0dXNVPemMS3b6F5XK5t4OrFH-8AvD7fONjHvu4HHgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
#تکمیلی؛ اینکه خبرمیزنن پنجره نقل و انتقالاتی باشگاه استقلال بازشد زمانی صحت داره که درسایت استعلام فیفازمانیکه‌نام باشگاه استقلال رو سرچ کنی بالا نیاره. شماهمین‌الان هم نام باشگاه استقلال دو در سایت استعلام پنجره فیفا سرچ کنید بالا میاره چون هنوز بسته است…</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/persiana_Soccer/22848" target="_blank">📅 23:34 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22847">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UtRGVTCm9ikfXxsX-nEz24lpe77p3xU8pXKPLMKaR_JJTSq51anmVc5en0wnFxh3dVEm4HGG2fACh2m_iGKFTd_DB2oU92TRzhl_7ZwU0r6GU71JTcgO3cO825yiIb8BMugMsnaW4gFHKI1cxPkNv24nL56Ac1nC8zbL2BdezZI62C5Q01wZrlKsXMw5aG8ExcIOvBZaUCUbmx7FkjnbN5gnE7OKF5dLmYMLjDAACTxjMbxe24ALgBcEzt2bck2wl_ySnwWx1JzuXQWm_YSvxRGV7ZCzaimn3nzsFsidhbmxha1nyYRcQuSaqS6j_5jNuefAeh6xfNvEK0dqW_5ceg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
کیلیان امباپه ستاره رئال مادرید: به پیوستن مایکل‌اولیسه به رئال‌مادرید بعداز چام جهانی بسیار خوش‌بین هستم و امیدوارم هرچه زودتر این انتقال دوسر برد برای ما رقم‌بخوره و اولیسه رو بزودی در تمرینات رئال ببینیم. او یک بازیکن فوق‌العادست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/persiana_Soccer/22847" target="_blank">📅 23:07 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22846">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">▶️
انتشار موزیک ویدیو جدید شیدا مقصودلو همسر ایرانی خوزه‌مورایس‌پرتغالی برای جام جهانی
🔥
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/persiana_Soccer/22846" target="_blank">📅 23:00 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22845">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa70e9e949.mp4?token=ufkxQoD4N6DweIQby-Ajo0Zv4SjLytIN9yP5isw1_v2ZwCIOm6dJ2Pu-qZFQJqSE5ml2G9WHTFutgZGpOrZJNOmcDk7L9YFn2MJSm-JpSiA8QSUaF-r5LGbr40xQmBZYob_6lLKZ46HoibUFFGY8gH8wbVhtfPmmabLvHc1hRmfeN8cshm9EBtxdf_8pBQsZdiJDBX77nddIeC6auZPmwcBvpz4WfOmKXxoyttN-jLOjxdcIoJcPI2eFOo_gKOBpQOMe1yPQMD252OzzNv9m5phMO3Ko1ZdcUrgVnwcdpEtUe6wSdzxcCdXdDbvdRUSQjUJR9m6NiLRk7pYxmHnpfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa70e9e949.mp4?token=ufkxQoD4N6DweIQby-Ajo0Zv4SjLytIN9yP5isw1_v2ZwCIOm6dJ2Pu-qZFQJqSE5ml2G9WHTFutgZGpOrZJNOmcDk7L9YFn2MJSm-JpSiA8QSUaF-r5LGbr40xQmBZYob_6lLKZ46HoibUFFGY8gH8wbVhtfPmmabLvHc1hRmfeN8cshm9EBtxdf_8pBQsZdiJDBX77nddIeC6auZPmwcBvpz4WfOmKXxoyttN-jLOjxdcIoJcPI2eFOo_gKOBpQOMe1yPQMD252OzzNv9m5phMO3Ko1ZdcUrgVnwcdpEtUe6wSdzxcCdXdDbvdRUSQjUJR9m6NiLRk7pYxmHnpfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔴
👤
#فوری؛ نماینده اوسمارویرا در گفتگویی کوتاه با رسانه پرشیانا اعلام‌کردکه اوسمار علاقمند به ادامه‌حضور درباشگاه پرسپولیس است و حتی لیست بازیکنان مدنظر خود رانیز به‌مدیریت داده و اگر اتفاق خاصی از طرف‌مالکان باشگاه رخ ندهد او فصل اینده روی نیمکت سرخپوشان پایتخت…</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/persiana_Soccer/22845" target="_blank">📅 22:43 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22844">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/080305bcc8.mp4?token=YiPx2i_EsV2LYhIGb2SMc5c9GM9l-nEm2rfVCujbJewgwlNwhBbgcaMM0dlIBxEdjv4JHs-76u3j9FU9xJx6HNwgbMS9tx77Yg4OWDUy1nAxU0Tpt1rhH0GuwyOV5DXdxioZ49gXpc5eFszWOAd6XKitDGYt2IUGxvS3WC_w5ysNkNuIJJoVqv9lLWcM8N-lz0-RZ8w-9iN_xzrKmS4lnZS9bSRooKcQ5_9dRhwCKNJmNC2LxSWPLUPQEuFTfhJzxcmvtSD4BxaWP52C-8SdnhSJCzUiWhOonsrym2POEcunFyotgtR-2ooR7hJCxR8KOCEymNEeJ7H9PzFQfW-OwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/080305bcc8.mp4?token=YiPx2i_EsV2LYhIGb2SMc5c9GM9l-nEm2rfVCujbJewgwlNwhBbgcaMM0dlIBxEdjv4JHs-76u3j9FU9xJx6HNwgbMS9tx77Yg4OWDUy1nAxU0Tpt1rhH0GuwyOV5DXdxioZ49gXpc5eFszWOAd6XKitDGYt2IUGxvS3WC_w5ysNkNuIJJoVqv9lLWcM8N-lz0-RZ8w-9iN_xzrKmS4lnZS9bSRooKcQ5_9dRhwCKNJmNC2LxSWPLUPQEuFTfhJzxcmvtSD4BxaWP52C-8SdnhSJCzUiWhOonsrym2POEcunFyotgtR-2ooR7hJCxR8KOCEymNEeJ7H9PzFQfW-OwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇹🇷
ویدیویی‌از قهرمانی تیم زهراگونش در سوپرلیگ ترکیه؛ زهرا گونش بهترین بازیکن فصل لقب گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/persiana_Soccer/22844" target="_blank">📅 22:27 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22843">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63cbb26f8b.mp4?token=vsEZ5JJxbjesoFIKxjzJm-j4oX9WGSUCLuwYuld89og4dpq3uX_G_Wjy3Th6ZzMgcOv0gwyJSmEsQanlSkCJVVKd64uhPoEbzJ7H3ECMWnWksnlUwhfiTtXmPbdcn3qpPn68JZQLwmfUJMLrEddL7LkpsQVGxUgGhFsPgMH1vF9ovIrv6d780UXfjk6L2JV9_Cyry6AELyVoN3uf8oABZ_5ou0-IWRVBtoUHrin6e78VnUGKoVNsjS_eyaynNNF1_3LvSeLWPA2FU5uhwffsf4J9JQ-6fYBxu2tZhWE02xFNCmHoGGthS85SzWuS3Y80S0FbEGTCdHarG5Dg-ABH516onWNlqaRPDlWwbLktUxfvZgkvYEXHDHPom6AYMvhd4DMIUfIGsvBx3MG1Rswv30xMOj8rtdPF0kWpcWpxFwq2-0FrkxVZDZoO_XM7t5Ik8ms4JK9APfwhpGSp3tkgd8nBM3m4oqDsPqRq7C9VFfn81lVPyloUwKbpm3b9SHARWVMpQ_LDH_Pu5rJIfhTXvKDnSliAFlJCbdlhW2OL2oF-5NZtkFe54ynfoo1-_2XLzPYLPKcyCwYdthSdDNSDMwelw259U94CQM4nnvzVehtiN9j0x8DTLZ94jIufkm1VPaU3MSInj1EfCVQFdYjMU1atMy4xxLA0qf-1ebsy04I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63cbb26f8b.mp4?token=vsEZ5JJxbjesoFIKxjzJm-j4oX9WGSUCLuwYuld89og4dpq3uX_G_Wjy3Th6ZzMgcOv0gwyJSmEsQanlSkCJVVKd64uhPoEbzJ7H3ECMWnWksnlUwhfiTtXmPbdcn3qpPn68JZQLwmfUJMLrEddL7LkpsQVGxUgGhFsPgMH1vF9ovIrv6d780UXfjk6L2JV9_Cyry6AELyVoN3uf8oABZ_5ou0-IWRVBtoUHrin6e78VnUGKoVNsjS_eyaynNNF1_3LvSeLWPA2FU5uhwffsf4J9JQ-6fYBxu2tZhWE02xFNCmHoGGthS85SzWuS3Y80S0FbEGTCdHarG5Dg-ABH516onWNlqaRPDlWwbLktUxfvZgkvYEXHDHPom6AYMvhd4DMIUfIGsvBx3MG1Rswv30xMOj8rtdPF0kWpcWpxFwq2-0FrkxVZDZoO_XM7t5Ik8ms4JK9APfwhpGSp3tkgd8nBM3m4oqDsPqRq7C9VFfn81lVPyloUwKbpm3b9SHARWVMpQ_LDH_Pu5rJIfhTXvKDnSliAFlJCbdlhW2OL2oF-5NZtkFe54ynfoo1-_2XLzPYLPKcyCwYdthSdDNSDMwelw259U94CQM4nnvzVehtiN9j0x8DTLZ94jIufkm1VPaU3MSInj1EfCVQFdYjMU1atMy4xxLA0qf-1ebsy04I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
👤
کاشته‌های‌دیدنی رونالدو در تمرین امروز تیم ملی پرتغال در استانه شروع رقابت‌های جام جهانی‌
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/persiana_Soccer/22843" target="_blank">📅 22:13 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22842">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qgNy45Dj87-erwcvj6Y-T5cWk31eheNP_b2YqseHYm9ujbT2vCDw33I5d1PvGT4uCiVNbdOQ9j3O6jKgdTSyj9Hmyrw36muEbhiFOdSDZzJSXBMsT_CRJlKIFNEpQ6ufAoSMQS91Amle5X3viZTXuPD3GgGFgaF9akk8Clr0-nVb9UkkacvkuqjfOjZ3o7UIKLi6xs_m-KmK-jHXVr9pouSGq4KTZeakWY77I0EbbotTiLdRgDQgQNw1g-giFfdZ5YOE6ugV3oE40sd2A8d73l8qbcg67CSKYh1fanSbnvRb8DwP3X-IHKYad1qIJHBOy5S_amA8EN3X5NsdU2rt8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#تکمیلی؛رسانه‌های‌فرانسوی: کیلیان امباپه، مایکل اولیسه رومتقاعدکرده تابافشار به سران بایرن مونیخ موافقت‌خود را باانتقال‌این ستاره 23 به رئال مادرید در پنجره نقل و انتقالات تابستاتی اعلام کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/persiana_Soccer/22842" target="_blank">📅 21:25 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22841">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W67U8lsoLHPmnGnEqAIWpBGKaOHs-NhndjnPDyrnw3e8yhhYMdcyAWrrpW62aGFVnP8MGEFrHIA4JK_EtRP0VTV788eH_NCciCjf2XHSlQfJaj0FgB83DHgQAi9j9SbHnr3_60fgUPv1bAYlrbigaSYiV_OtMdM_1912iwm4_kR1A-NxZqW0uCWu_l71QjjrqEg4qilwVOpDBMg8by8B-_h0MOYeR4VyYWtB8sz43H_Eu9jBITaQdJNG9RzCmO-WqtB-MkwNPeJBhJLLE4ZHTiI0ZtadYB-YnVD8nAwlr9MrW--fCGOEYK2gEV3zDc7gi3sTzFC35_X7YRtT010gQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#تکمیلی؛ طبق اطلاعات موثق به دست اومده پرشیانا؛ باشگاه استقلال افر سه‌ساله سالانه به ارزش 1.2 میلیون‌دلار به دراگان اسکوچیچ سرمربی کروات سابق‌تراکتور داده است. همانطور که در روزهای اخیر خبر دادیم تنها شرط اسکوچیچ امنیت منطقه است. گفته جنگ کامل تموم بشه دوباره…</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/persiana_Soccer/22841" target="_blank">📅 20:57 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22840">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c01b9049b.mp4?token=HqsSD4RTQO2D2XkzRtmc2FIDXqot6JVq9qW2bb_u9l6cF4mhQRqspI991hRinKV77Gxji2UrF4XABa9spcfh8zXQnUVpsq7p95027GwHuKnvay6ziSabPE8eKBegKDI5tLabMwPwG2njpxsyW82zywH0MpCMwRup32T9TsuG_BUgPoDpfkj8lAwpQvY-q_BoBHP79BKBSGk86TIWbu9SVX2SPTaxxL9PebMVy_NoCcIWC2zrv_MCLk2pjt693WB_NdSCpkEULgfG-9WAQ8VoOaUiyYUvbp0Bql31xgW3jNN7AP646dTmj4LHWLGERXBFqMA0rOIH4Ti2Y8M3oCZqBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c01b9049b.mp4?token=HqsSD4RTQO2D2XkzRtmc2FIDXqot6JVq9qW2bb_u9l6cF4mhQRqspI991hRinKV77Gxji2UrF4XABa9spcfh8zXQnUVpsq7p95027GwHuKnvay6ziSabPE8eKBegKDI5tLabMwPwG2njpxsyW82zywH0MpCMwRup32T9TsuG_BUgPoDpfkj8lAwpQvY-q_BoBHP79BKBSGk86TIWbu9SVX2SPTaxxL9PebMVy_NoCcIWC2zrv_MCLk2pjt693WB_NdSCpkEULgfG-9WAQ8VoOaUiyYUvbp0Bql31xgW3jNN7AP646dTmj4LHWLGERXBFqMA0rOIH4Ti2Y8M3oCZqBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚪️
@Persiana_Soccer
| Out Of Context</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/persiana_Soccer/22840" target="_blank">📅 20:53 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22839">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A9U_06HzaKfbF-jPj1fOEKxIuXGivRBEYRVVMg4ugNSmp-0ba9hVOw0Ze9l0yYmL_io5h9xSYmsD8hjQWZ61LKkX_yjNA28WSCZuab9y3nxT6AKFbqOiTpxRLh_DZhCIemIExqGmh5q1o8s0Wokiak9ETxH8eamuugEw-LXCwpBndY-bQuc57KgcWwoC2o8WQXjg1Zui_06cmN9R9yva7xYrTQTsJl1fPAtHXECoLQrpqNnxeaBi-XWyofUzBXo8Ocj37pO6Nf86jTH4UoEo5vw3TVIInpqT1rfd0btdEL0ZLxksO7HkHQvJdOuZIriNPducqvYDFA-yGWKX6-1zhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇹
#نقل‌وانتقالات|ادعای اسپورت: آرن اسلات بعداز بر کناری از تیم لیورپول به گزینه اصلی هدایت باشگاه آث میلان تبدیل شده و مذاکرات بین این سر مربی و سران روسونری بزودی شروع خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/persiana_Soccer/22839" target="_blank">📅 19:38 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22838">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BatfYXnhMi-JPzR743Hxk4PHT92oglrP_CCHJHIU0R0LNfE2XxuEwAVGdel6I3BhMreZKH9V-4StnbXkZdI2NwwZ4hatadMmbHHCt_qBTRbRq6yLU08PKxqzcMpQx7QxRcFO1drNugMGPRd1x6bPh-Ntm9tzsKVQKIKhWVT9xC7NNFwol-ZFj5GUiRx3vv3OpxcRHghQT2b0ajWJ9cPWPmg_ndTWrJt3lo74Ew-Zmo33vM79udINJXOXW4SKsXyb5S_nPsaph92T0WGuZIYmDcR7dpQ80KCca4Z9Zb6mpl75o4w_gLEN__AYvVLdlZb8xRcqRkQdyhNIsjhvUiOgJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
مهدی تاتار سرمربی گل‌گهرسیرجان از طریق دوستان نزدیک‌خود درباشگاه پرسپولیس اعلام کرده درصورتی‌که اوسمار ویرا از این تیم جدا شود حاضر است از گل‌گهرجداشود و راهی تیم محبوبش شود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/persiana_Soccer/22838" target="_blank">📅 19:05 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22836">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l1CxXafY90W-N-U6R5jwd5-Q0irGmLPceZHsQ9QAVMlPyO9xFRaLc6hizP9qzyn4h47StXYqi2k88EcVQvLlr2jowYuu0XeWcXwjGrwu0MzXZD6Ynvz1DG_HsDEG0prjvxD71OPwht5HQ8vTipTfIPrLdLkQd4-a1co6aguJ4W6a5Cpq_TEm-SyYYPZqSXBMr1WZdYhMlBK4eRDllMunCTfsV4mzXDEmrX0846dgkF_7U3Z793yuNnIFhLFuYltRqY3DTZ1B3POoVXuZnm2jgIBA-SLHwn9tAef_mitosLejyoPA7Nkpd5jZqafpJtAigxJRgjqWRkbPCC9eYCLiGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a220e76f7.mp4?token=VeDfgVLQwMNzSbSSa2lUPwsEW_eHGhpERZDCfr7Kh1HD5C2IplZ6Acd941eMlu1v52ZA2LY6NpHUW_q1IJ1We3hv8b4f5xzPJAAYmHCjzlvtY7wAfWt3bCy_e6ISeCmb3w1A0I-EmHetimONr_98u6jZECm1xoyL1IirvpHuXXQZdsjo5UQ2hWFoDj52NECTyFDEV7MaES7IGZgpuzjWPj3_jFs9vYcWH7JESwjPkVDtV5Qv-8ohogJWusELGGKuEXRwOQaLDZkz2E3q6deEd3Lz9_IcmXzoITr3X2iJAJK_fsdEZZcx_SEBeHcz8tUFQP3QOq4f-UhVpvGAFwUP1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a220e76f7.mp4?token=VeDfgVLQwMNzSbSSa2lUPwsEW_eHGhpERZDCfr7Kh1HD5C2IplZ6Acd941eMlu1v52ZA2LY6NpHUW_q1IJ1We3hv8b4f5xzPJAAYmHCjzlvtY7wAfWt3bCy_e6ISeCmb3w1A0I-EmHetimONr_98u6jZECm1xoyL1IirvpHuXXQZdsjo5UQ2hWFoDj52NECTyFDEV7MaES7IGZgpuzjWPj3_jFs9vYcWH7JESwjPkVDtV5Qv-8ohogJWusELGGKuEXRwOQaLDZkz2E3q6deEd3Lz9_IcmXzoITr3X2iJAJK_fsdEZZcx_SEBeHcz8tUFQP3QOq4f-UhVpvGAFwUP1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ارلینگ هالند جدیدا تکثیر شده؛ نسخه هالند جونیور، نسخه هالند پیر، نسخه هالند دختر:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/persiana_Soccer/22836" target="_blank">📅 19:00 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22835">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y_3AKvuSEttRpiW6ILxrhbz_tRQTdoAxFgqq9YUQh2_a3g_Uw8jHR2eKzbdpLgMFqp4cMJ4gg7kaNDWip3KEu31CN3Szgx_FOdBDauF4R4Man1FHlSWZbd5Jf4CqivvimKc-Cs71xqg1G1PxwCEEgMXn47BltbV-KOj1gmSVfikSdgIJGJQOX7zTTNqzIbek29XZ4RDT_LcT2DY4yAMuduxukM-0zU9T4vFfa9G5ezK2J5KBfEEGzDIc3ByXlG0FKcfjJTRSnno6FSj0DRQzl0vR_YDSjdeV8CqNkpGooEZiH1jSmylv21H1D5OWAXncyjjb5CU_JNHrz0rbiFY0pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رومانو هم‌تاییدکرد؛ پرز میخواد به هرشکلی که شده مایکل اولیسه رو تو این پنجره به رئال مادرید بیاره. اولیسه شماره 11 جدید رئال خواهد بود؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/persiana_Soccer/22835" target="_blank">📅 19:00 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22834">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KYQR5m36ZCyUzi1CZ-jr3PnJvIxuj2IBbkZkFeL7tEGekPECUxNmXAJLvV1QlX0ZVPgSNKjibqx3Lx2PjUN7xWxsxDZEAfCRsDpK3IsBKR2Uk4xjy1ymckdlU8rEbPcrcubRsQ6oldmYsf4i2Hv6XKPf17V0nIQESDXn4830WWpqVssyWnHqBN_2LMcYxJXtTVgNmoR02HZpmLs5cru6aTJu6hDHSNbgXQo_RcogoIluVmyROhG3Op0t58BuQ2p2tacArh8Fp0KiD4q7cGe4cZqpq54l7YEl84hSl2YciIhAQl08qmvBdRYhLuqW1DKe9R6oOptT0qYzDUxvYdP7gQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💳
در
#رومابت
میتوانید با کارت بانکی ایران انواع ووچر و همچین انواع ارزهای رایج حسابتون را شارژ و برداشت کنید
✅
🎁
10% بونوس برای شارژ با رمز ارز
💰
10% کش بک روی تیم محبوبت
💰
100% بونوس خوشامدگویی
🎁
20% کش بک بازی های کازینویی و انفجار
🔥
پلن وفاداری همراه با کش بک بی نظیر
#RomaBet
📣
‌
#بدون_احراز_هویت
1️⃣
2️⃣
3️⃣
4️⃣
1️⃣
2️⃣
3️⃣
4️⃣
⛔
در صورت فیلتر بودن از طریق VPN غیر از سرور انگلیس ( سرور
🇺🇸
🇩🇪
🇨🇦
🇫🇮
🇹🇷
👇
👇
)
🇪🇺
https://trentivo6402.bar
✅
کانال تلگرامی
#رومابت
15
👇
🔵
@Romabet_official</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/persiana_Soccer/22834" target="_blank">📅 19:00 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22833">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ijoAa2n8dEFS2RLO7ClDU_n-ozNwtNhM6f4L1BYpey50RqkbztEmdiPGbt00sk4FELiJsD9WL5IJ8Mn2ijxXVTFZ6-ysdjIU8ckDY5f59dsy-l3ZmQ5NdMC6ppV96delNrZIiqCmkIW4l9xBcQm8X2JHyCzzhS6jMcytuLrWS3f7OacpcAxhuvCrmhViynqjZOzw2Oxg_SdpUsmSQ69N4ZEqQCRmcHdENzw-fO_JWYuPqwq1IvPxOy2_REvVz9lsstoJMr15z7ff2f_GxdaKjUEhswE_APDPMCpbd-WIZXjcfcDrqK-V-1DiyyO_F4jINXdAVodXTPzNj1XXAmDjIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
علیرضا محمد دستیار تارتار در گل‌گهر: باشگاه پرسپولیس باتارتارمذاکره‌کرده واگر اوسمار برنگردد تارتار سرمربی می‌شود! او می‌تواند تیم پرسپولیس راقهرمان کند! باید چه کند تا سرمربی شود؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/persiana_Soccer/22833" target="_blank">📅 18:12 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22832">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nE3hFsPmyGp-nfrFVHJ8n1rHIqo6g5bq6nC_fGqJPWcdhpFIlN_ZBrO9aDB9ufAAAIlzS2U52y8DgIcftcxYn4UWB-qFg_231dj1wKNo7D-L4Rtd03nysVukYq9Thg2oVVJmiqzvyY_l0RPXI6uqP-YrkwkzZ1gTuqiBPoGjlm547Nju3Cc7gBzvH5xJBetNWN7qS5ufSM_kcl9cL6-yr8eDwbGpFiSKCZo19BFx-L3SNFIpJyrd4g5NuyZIhcyUsPlpy-HwQTqemTPiKc2ZPhclnztLyCNuZXQFGsygy5XlbZ0GtcsUsrgSG7i8RqSCV8OnKCx6YgePPpWfjm0xGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رومانو هم‌تاییدکرد؛ پرز میخواد به هرشکلی که شده مایکل اولیسه رو تو این پنجره به رئال مادرید بیاره. اولیسه شماره 11 جدید رئال خواهد بود؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/persiana_Soccer/22832" target="_blank">📅 17:52 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22831">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YG9Wd7ulGCBm7wIvWZkHPQabOhkIizA7TfoSZatjXW2IV8C9x-941WKFTUldX-lDBwrP9XTXrTus3XdGIPnkEgx3YYtUXpnq3BIbHdwa-BKUOUTOtEzuBcr6pZGmLJAsJ7u1vz1xbbCzlnpOKvw5ZfT5zYVR_3Wl1XXlFennYza-dfbXQdmutKT_Jai5XRhA7LzZYM0tOzbl-kX3UH_xjJJuiB1ijZiIZrRMCWoIpexvWGEcnClAhw2eGUqsPZ96nvQ3UXxgeTdzQKsdTGlV1FGJK-YjvIkP2n2wkoT4LsMcYoWIPSLKgwEPXdLLyM_1dTRgy3ZFVNOcbizFSRfliQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#تکمیلی؛‌خوزه‌فلیکس‌دیاز:طبق اطلاعاتی که بدست آورد مطمئن‌شدم‌که‌منظور فلورنتینو پرز همون مایکل اولیسه وینگر فرانسوی‌بایرن‌مونیخه و روز سه شنبه پیش رو آفر 150 میلیون یورویی خود را تقدیم سران باشگاه بایرن مونیخ خواهد کرد. خودِ اولیسه هم در جریانه که پرز میخواد…</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/persiana_Soccer/22831" target="_blank">📅 17:34 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22830">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cNxtcBYlq-ELsdT731GzdXyPSIZe8Sc1CToVICoc9RDusXKIR-LDgV6OAm_ZBTnJQuGgKynmh9zg7gd8vie9ZdzzMN--wuIpMvNwA9LHTWoQCFsD0Rxw_pRa3WJV8cvuQvRqGE1Vl46IhQunyAh8Va-YExS80aVUwY_Fkk67LiKQwHOJE_0QVlrGwan7aWji572uIUMthCg4mvD6_RhPvyNY50nmv1jbF-tQYnxarLXyI9Xq9OGyEQaObeljgkZ4qDtC7Zzn8IertpuxCwsEp8F6lWkbg8zHHP4-HRIQ1AGcwM3DdnT4ZLJJBqPfGXxELo-1IMqXI6TQl88wXyNfcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ خوزه فلیکس دیاز: علی رغم تکذیبیه شب‌گذشته فلورنتینو پرز؛ باشگاه رئال مادرید بشدت علاقمند به پیوستن مایکل اولیسه به این تیم است و قطعا در این تابستان برای جذبش تلاش خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/persiana_Soccer/22830" target="_blank">📅 17:05 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22829">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/976cd07773.mp4?token=UnB11S1O74pUpV2B_0zqC3MS2DqBt24wWSy9KgbVBMJxz11eNIpMrjGldFGUn3QQ3q8HtWe3ozaOnC-6f_9peQ2ptSdE5HWW6HXi06dTrvBRwr1yBMoHbWFTWrql4_GXhcm-d94jHBs8jCl6XSjqMpxuYvi9UKDSpGAu22G7xxlvlKjuf1AvuIW3xQM9ly0gzyi7TbMAGNHl87WjQC1x89L82ywzZbsnt4ef8s957Ml_tBFYfCgOy-ifxZ-7GW1Onwr9JE6M8rpRODLTW1vJOSSl6eGVPHzN4wNmto5vuRQY9ccipiDuTlThZP8TwmyJeSVAyZVcuGAVuhrJQ_drNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/976cd07773.mp4?token=UnB11S1O74pUpV2B_0zqC3MS2DqBt24wWSy9KgbVBMJxz11eNIpMrjGldFGUn3QQ3q8HtWe3ozaOnC-6f_9peQ2ptSdE5HWW6HXi06dTrvBRwr1yBMoHbWFTWrql4_GXhcm-d94jHBs8jCl6XSjqMpxuYvi9UKDSpGAu22G7xxlvlKjuf1AvuIW3xQM9ly0gzyi7TbMAGNHl87WjQC1x89L82ywzZbsnt4ef8s957Ml_tBFYfCgOy-ifxZ-7GW1Onwr9JE6M8rpRODLTW1vJOSSl6eGVPHzN4wNmto5vuRQY9ccipiDuTlThZP8TwmyJeSVAyZVcuGAVuhrJQ_drNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
تیکه‌های‌سنگین‌ابوطالب‌به‌تیم قلعه نویی:
شک نکنید این تیم قلعه نویی تا فینال جام جهانی میره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/persiana_Soccer/22829" target="_blank">📅 16:46 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22828">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j6qkZaSKlI38vCC_C0TKps5yb5OqgxMFAuoSKzRXm2BUVE5r9GBuxMV9zv28wyHIqFQqLc85dgwjQa-7jtlJLHExiAg9KuDeCbY8J0GXWoooNIpcR3yNYT6fqB0I7DiSa-0g1e4-cznephyYGYwwOSbPqpdn9o2EDHYw_sRN-eqDi0DfKMDIpADcO9rUa75DTveIMnz1JEEbBppsRPyOPqLYdEiWPAUdfCA_SwB_vLpxo01f2hG2Y__sSYDivhkrBb3lvHEqVfSb3NR40wSoJ7cshi5aVUc_kp_qoNUdU9jkPjQY320yQPSkY2qo6EQMBF-kOveOmgyF4Q1B9JPd4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
بین‌گلگهر و پرسپولیس؛ احتمال زیاد پرسپولیس راهی لیگ دو آسیا خواهد شد. اگه اتفاق خاصی رخ ندهد! گل گهر رضایت نسبی خود را اعلام کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/persiana_Soccer/22828" target="_blank">📅 16:40 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22827">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tBQoog96Hjsl6IhJqKM6bQ2Mw_zS_R9KeNpr4bMokawatBgHNaCBQ4Wnnloo5-9tgmBGQ_w32Ihw6RawqCCrqGPOy3l9D9mxyG5DWugo804FsiyaHcqa01Wa-dDjV-y1rEoUmM5bZHpz0avaPZWeYLmQdgC4hX0IrWj-vddptnUNg8DO3EJD3Ij8aX-MkKhxa4WpA--03I4080irtaSEdae_VlC7udZflu0vspqvx3Se6lIPzqRya2I0IfiLxVNGVINKlGBdRhdc55d7BSylyswEyA9qm7Mzbq79JD5q87T3BdQKTwDm3nEUve3wtIi2IhnEo2rLR-ru_FfvAcugzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
آقا منظور پرز من بودم. شماها چقدر آی‌کیوتون پایینه. سه‌شنبه 150 میلیون‌یورو به حساب سپاهان واریز میشه و رسما میرم اسپانیا برای رونمایی.
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/persiana_Soccer/22827" target="_blank">📅 16:30 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22826">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7414e31a83.mp4?token=htUPydZgqIWRGPjZ6nxdobKDqvrb-lQjjGuzPn326kwkxLgRAPsYLYOF-RCV949L9KMGgVmDq49h89cxgID2lP7ladb2ePqpSL514bdGJk1l2wzH5joGZS4xCoGPmbrT6IL7Bfmict1QO7xwVJRsHs0um8dvJ8wh8xmbYYPmUcAcND-JWuCDpXHE8SC07qm9z6hkhze9CWY-ggBUujWH4xGGs2iqzRrNnd1JMBuKtfJx7P7mvvZAcJ8rxGEXwaPjBl9owsaCtBIzTKdPol3_CmH4XIhWtxVR9fV0xjKti13-msp0QhUUcolD4lxi8LuivcVK-dz17Z_FuD71ot9zQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7414e31a83.mp4?token=htUPydZgqIWRGPjZ6nxdobKDqvrb-lQjjGuzPn326kwkxLgRAPsYLYOF-RCV949L9KMGgVmDq49h89cxgID2lP7ladb2ePqpSL514bdGJk1l2wzH5joGZS4xCoGPmbrT6IL7Bfmict1QO7xwVJRsHs0um8dvJ8wh8xmbYYPmUcAcND-JWuCDpXHE8SC07qm9z6hkhze9CWY-ggBUujWH4xGGs2iqzRrNnd1JMBuKtfJx7P7mvvZAcJ8rxGEXwaPjBl9owsaCtBIzTKdPol3_CmH4XIhWtxVR9fV0xjKti13-msp0QhUUcolD4lxi8LuivcVK-dz17Z_FuD71ot9zQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇪🇸
رومانو: ابراهیم کوناته و دنزل دامفریس با عقد قرار دادی 4 ساله رسما به رئال مادرید پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/persiana_Soccer/22826" target="_blank">📅 16:01 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22825">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cLkW_Ku4GGJRCN8ObjzFcJagdBOycFc8s-RPilrEotu-sInHI4CBH98gIQ42lEDO3mFJ1fvqx8s3dUE11yxzfWXfEIQjJj3vpQZKl2-aKLujT7mBf6k074-gVpsPPbUVg84XY__8X0I3UlJhTx8vV1TzjtCdCQCv8cXUBubB-Hz6Coa8NbOtjXOwDg3recsVkiFNoUT9-zZfki72Ssnl2wMuAHEQ-VbYvzH6euc6zNwTwiCLluTMCNhlfuMgW2ox-oQN4NmMzWZGfRaW1aWKGG4YUvzhO2sxw1PGkpP_FXzZK4J46GceGWAXbNyvaXpQc6dZauNJkf3MjJDZw9wlNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
برنامه کامل هفته سوم رقابت‌های جام جهانی؛ از روز 3 تیرماه هفته سوم شروع میشه تا 7 تیرماه‌‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/persiana_Soccer/22825" target="_blank">📅 15:41 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22824">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CJRtOujKaTdblfk5MxHvDq6LDCf6ef3JRn1cpbqbcFqvqMldpF_4h7qOrmLEM3vQsILTPkHWFMfgrJewYdUtOI2qWCodD9V13ic_jRfRyVNdcQKUcWM1YwnBOQYnF9hUxk3JDqKGSv_9mUUHmghPUSdv_5LSpyy3YlxzGMc8gYUKDThY6nA0xWo4GKRDZnxDyMKy3DV-tEuzpwpuIKMxZWBR-jjz3CKxE1RvvQG8O_IL1BcQz-BO8T1XzhrXpZo6jxDVKiqnjqsoKauILoMfftv1Rhht27Xoyj1rMAYhpQdf7qdtag8iW5pa2lkCwB6LORWuOa3RDnQtpyh9Vd4lWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#تکمیلی؛ نشریه‌ کوپه: رابطه فلورنتینو پرز و خورخه مندس ایجنت فوق‌ ستاره‌ها خوب شده و مندس به پرز گفته هر بازیکنی بخوای رو باشگاهش متقاعد میکنم. ایجنت ویتینا و نوس همین مندسه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/persiana_Soccer/22824" target="_blank">📅 15:23 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22823">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nLLoiDPFhmBndP-w5RcEz9OYCi8MGmTCSDQfOhDqs0dbvcsDN3HBTCCNbmwiXoPmnKDERp7Ql2kejJYKEzJxPTqaQ6aA3ORJHbzT3t4Z_f3-LZjNHzTI0u2lvmGn7TB8KnzJIeRCthG3mo44gp5t-FH-cbVXplFLbtTMMiaDHTeNZT77kJnsUmLqBvNSuWXXJIenpT2FQjYiaKITT0MP5tktqYj_he9TJXq348anOpKwimRAJ35SwAMEa9hfNFJI_2NdxhvNpuKILYXRk2y97LiQf0RizE3N6xYmv3qQZsYsn7kbpliPnG1nIQUTmQaBbvukGO_ro-q9a1D6O2QYug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#فوری؛فابریزیو رومانو درلایو اینستاگرامی خود: مایکل اولیسه ستاره فرانسوی بایرن دیگر هدف اصلی پرز برای تقویت خط حمله رئال مادرید است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/persiana_Soccer/22823" target="_blank">📅 14:49 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22822">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JhfnuCRRQ77RPy6tfSIUYfJpl-2YTR6GobRHB_PCBM-c1SuKmQNsYcFahpGl7QiLdKqwBqPpMOPtXFC0IAvLnj38asTMt0DL2QydfnhPPJx4x2Tjb6okVJSPVNPIxKfe8Qnh3WdR6InKqNgrURRuk4NErIHv4iTO9NXLFiQR8euOwWT5LaIBzyOFR5ovA6dd_rfsJYoIXSgyTrE4iOJR6CUjfLn6UTMwI6qu-VbZxfrHkqb5dpB0saEPUvH1ULN1dsKg_D12WNBLuHM3esIaHnpsU0wD9K49jEfPMFUZeP3Esj_ygc2SsjE96Ud0mKh-UY7eBdbgr5cAYw7YDW5Lmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رسانه‌عراقی‌اکسترا از انتخاب یحیی گل‌محمدی به عنوان سرمربی جدید دهوک خبر داد. دهوک تیمی درکردستان‌عراق است که در فصل قبل لیگ عراق که شب گذشته به پایان رسید در رده دهم ایستاد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/persiana_Soccer/22822" target="_blank">📅 14:25 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22821">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/92b9b84db0.mp4?token=F-F3CSn82dIf-7ZPFp27-gJIOsqzRXhRsgCFlEIXzXRcP-V6D9-PgWwY5vlsz3BxQ4dSh_e8MCHFiBEj-ofQq3CVWUVebLrMtVQv9JhgG2fxE7IBj7fHK4Wabu-3UEfCPtjnv-iM5XLmzMzRiHfy8lb4tDxq8wiHW9l_BYPSxpz_aoXQm7J_0rhE-U57Zif5TFC7rXV2sjouIzc-mtO6E0LA0UmV8uq7HBbGppzEjGtuWj-FT1M5vf9zyyoXrjC6FB424aDG3fyKeMfX-60BwFoehIcQtOj0CRlG2BjXQQfav60haSOyM5mtD4sUKAdZsMXw2WauX7S0P1gLgKHZVEbC9jkkgS_hYodVHAcuAGivZ9OyZCdVUKT2cHxtMhFmCg5JBWqWDA8FAS5qehZ3PILawddQoxqJBd8yBgx24jYCySU7XUtod-2UgUKe30aLnE3xbMrtnIs1LUj02vCdGY-vMHqduKGsmgN32njvHHzzZ9f-bPQ-wpqN8g6TnrvYvHhayDCH73GdcnPHPrjdO3E5Pa1_sT8XfbbEWGklaFnTkM5oYDjFuHjOl1jo47rhPr5bRa5h8yz580zMFl_69Oajzpl4utYYmE3VLOjLv23BErfZgQQQ18nBT85JqUdOiSmo4CX1uU3RJA6vmfKHln2jlJK-83TaN-uHfZ4TNfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/92b9b84db0.mp4?token=F-F3CSn82dIf-7ZPFp27-gJIOsqzRXhRsgCFlEIXzXRcP-V6D9-PgWwY5vlsz3BxQ4dSh_e8MCHFiBEj-ofQq3CVWUVebLrMtVQv9JhgG2fxE7IBj7fHK4Wabu-3UEfCPtjnv-iM5XLmzMzRiHfy8lb4tDxq8wiHW9l_BYPSxpz_aoXQm7J_0rhE-U57Zif5TFC7rXV2sjouIzc-mtO6E0LA0UmV8uq7HBbGppzEjGtuWj-FT1M5vf9zyyoXrjC6FB424aDG3fyKeMfX-60BwFoehIcQtOj0CRlG2BjXQQfav60haSOyM5mtD4sUKAdZsMXw2WauX7S0P1gLgKHZVEbC9jkkgS_hYodVHAcuAGivZ9OyZCdVUKT2cHxtMhFmCg5JBWqWDA8FAS5qehZ3PILawddQoxqJBd8yBgx24jYCySU7XUtod-2UgUKe30aLnE3xbMrtnIs1LUj02vCdGY-vMHqduKGsmgN32njvHHzzZ9f-bPQ-wpqN8g6TnrvYvHhayDCH73GdcnPHPrjdO3E5Pa1_sT8XfbbEWGklaFnTkM5oYDjFuHjOl1jo47rhPr5bRa5h8yz580zMFl_69Oajzpl4utYYmE3VLOjLv23BErfZgQQQ18nBT85JqUdOiSmo4CX1uU3RJA6vmfKHln2jlJK-83TaN-uHfZ4TNfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
لحظاتی‌از عملکرد خیره‌کننده لامین یامال ستاره 18 ساله بارسلونا در رقابت‌های فصل گذشته لالیگا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/persiana_Soccer/22821" target="_blank">📅 14:07 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22820">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63d7daef98.mp4?token=Iqao0qYk_lB8jhxWgssawzvqw3OD24F1XAQw7Z0GGr5ZGnwmx071T5TNfEBJOgJmYhfTRjHFWTkWGqhueMT1e9tpEn2mKR3a07aszY2NzGbfYXcx5SolVFwiVpbzC-JG6N2yiUKbQVncyEv5Hvbgv3AU2HRal3Yo0VTNNaSRj9moFOAAu3C8d8E6mRKkOG4dIoPl_d54e3Qp78IKBnuH5vFvqujPGL2SRABeEEAuxVxdcq1-EqtfpKJKko7dAqp2uBQquOEmOVnHI2lbFvUWiyIDKHlNqQ_5o8ZAZYtbK7loRQNiLmZMpwf0BSnYjRR78qEdXJd36i5_VkfXL8MfhDAGDKVEjrix4hfHRRsCvr8aJ95xmFxg3VBTg7LQokGZwIdYYjWn7UmDjo12FkOPQ_pvd6jeWd1FI5eOidQJQd-vtQzW9dXDQ0i6Biba0qy3g7RQpBcjkG6-DnF1ETyHqmUrM7-8OZ92AceBEC-RelrvS9ucHC4vgSlRys2_nYaIVzoKRODQJjZ97AnW9Ra-UrbK6AtddtkDi9Ik04dPs6SdioPbzBvqQAaucppnCMOQ0MqfmKfNDn4XxZAB0zvTC7XQkMeAaAc93-kHhIIWctoapEm88ufYcs3rBmPIov6kGVdVXM2i9VtFRcpzTy1KjR1Ihrj9wvlscTXJj7tw7AQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63d7daef98.mp4?token=Iqao0qYk_lB8jhxWgssawzvqw3OD24F1XAQw7Z0GGr5ZGnwmx071T5TNfEBJOgJmYhfTRjHFWTkWGqhueMT1e9tpEn2mKR3a07aszY2NzGbfYXcx5SolVFwiVpbzC-JG6N2yiUKbQVncyEv5Hvbgv3AU2HRal3Yo0VTNNaSRj9moFOAAu3C8d8E6mRKkOG4dIoPl_d54e3Qp78IKBnuH5vFvqujPGL2SRABeEEAuxVxdcq1-EqtfpKJKko7dAqp2uBQquOEmOVnHI2lbFvUWiyIDKHlNqQ_5o8ZAZYtbK7loRQNiLmZMpwf0BSnYjRR78qEdXJd36i5_VkfXL8MfhDAGDKVEjrix4hfHRRsCvr8aJ95xmFxg3VBTg7LQokGZwIdYYjWn7UmDjo12FkOPQ_pvd6jeWd1FI5eOidQJQd-vtQzW9dXDQ0i6Biba0qy3g7RQpBcjkG6-DnF1ETyHqmUrM7-8OZ92AceBEC-RelrvS9ucHC4vgSlRys2_nYaIVzoKRODQJjZ97AnW9Ra-UrbK6AtddtkDi9Ik04dPs6SdioPbzBvqQAaucppnCMOQ0MqfmKfNDn4XxZAB0zvTC7XQkMeAaAc93-kHhIIWctoapEm88ufYcs3rBmPIov6kGVdVXM2i9VtFRcpzTy1KjR1Ihrj9wvlscTXJj7tw7AQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
🇫🇷
من خرافاتی نیستم ولی شما این بازی ۲ سال پیش پاری سن ژرمن با حضور امباپه مقابل دورتموند رو ببینید؛ واقعا انگار طلسم شده بنده خدا
😂
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/persiana_Soccer/22820" target="_blank">📅 13:57 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22819">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RsBFztrnWTqx-K2RMkRRagXavrxO24bJ6tQ4ThzMqK5233KoLM1_i6BJ1R7aKXPhgSsSVlCWXghSK3DzkCm-Ii5V51Kyrzxaw6dSNwzgiqyif1SjniD_grUI0lD0I1NMw98ExbPFqSBZjivjdt0Y1k_Jzp9twedlC4eto-ntzYc8-ZoRlZlpAHRET2L4SLs2NWxkhKzEXplo2xVFry0E5fSvH05tiHGa8wn79j5XPYL0udoaR_oe2J0MMPFOIl680Aiy8NLAWqFbZXWIBTHAafVPP7merOH66Zs1aznBxzG1R6RRG2MMviw9aI2VOcC82jTnSBvEsSO-Mhovt8eAsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
👤
#تکمیلی؛ باشگاه پیکان قصد داره درصورت توافق‌ مالی باباشگاه‌روبین‌کازان، رضایت نامه کسری طاهری مهاجم19ساله و گلزن این‌باشگاه رو بگیره و درتابستان سال آینده با رقم بیشتری به سایر تیم‌های لیگ‌برتری‌بفروشه. رقم‌فعلی‌رضایت‌نامه کسری 800 هزار یورو از سوی باشگاه…</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/persiana_Soccer/22819" target="_blank">📅 13:27 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22818">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7913f58d6f.mp4?token=f_r-ZgaFZ_pYVDXOrndfkAa0X7MkXYQDerWnh_0lLSk06pCutAWua6fhWt1KbWCS55w8QEGqCLXFEQVzaJwKHBDBEYsCJpS8OKP7F0PEJjYCeFlDnl6hm14QGdmQXFKk2N9zoBLSJyzq0FCjTkxrxWuxoNiIyESctF1-GbjkGONOpyVgiBu5Xm4esa78wb89-CcVsh1Xh_lz5qAI4sPPc9RSM6NWO6RTI8ypxiQ7aN5rBv4eVxtB9RTpg7-vl2Nlti9fn1IchF4YPMyEZRGcoLPob-SZ7QDa3o-C4hcLDCJkYHq2X-IbRJwwXBOZFH7Sw-6f5MWIbJ8TnYpgAuQdqb5wfaecfYE3D1CtcKzl3wDtJIN0xGgQ_Qq5_1Wm1xYtnGEIGbprgvFA6IUMiGaETQyDn_M7IJQb9OcS-gP9qjzp8vWmRjClIbU38KHdbCU7NNCwZUtZxwbvhYFq8VmZd2u0PnbQHSjA6GQQNQER0nUSIS_4Z-p8MWk09eQ9SLkVW1ktRxHG2Bnm6yjmTbi3r51oef4Q0iZCYmQvEIjBJZtWqS1XgbOgPZSSZO8UQBmYvXNF1uUkHPgMwY7UYvbZmFSZrv8a2KrMUGL74HVFjVfgli8_lcIiE1xBDZfuZ47-yUmgjOnet20dmdh3liu6lsTZLvU7lkMmEZ02isFGLAc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7913f58d6f.mp4?token=f_r-ZgaFZ_pYVDXOrndfkAa0X7MkXYQDerWnh_0lLSk06pCutAWua6fhWt1KbWCS55w8QEGqCLXFEQVzaJwKHBDBEYsCJpS8OKP7F0PEJjYCeFlDnl6hm14QGdmQXFKk2N9zoBLSJyzq0FCjTkxrxWuxoNiIyESctF1-GbjkGONOpyVgiBu5Xm4esa78wb89-CcVsh1Xh_lz5qAI4sPPc9RSM6NWO6RTI8ypxiQ7aN5rBv4eVxtB9RTpg7-vl2Nlti9fn1IchF4YPMyEZRGcoLPob-SZ7QDa3o-C4hcLDCJkYHq2X-IbRJwwXBOZFH7Sw-6f5MWIbJ8TnYpgAuQdqb5wfaecfYE3D1CtcKzl3wDtJIN0xGgQ_Qq5_1Wm1xYtnGEIGbprgvFA6IUMiGaETQyDn_M7IJQb9OcS-gP9qjzp8vWmRjClIbU38KHdbCU7NNCwZUtZxwbvhYFq8VmZd2u0PnbQHSjA6GQQNQER0nUSIS_4Z-p8MWk09eQ9SLkVW1ktRxHG2Bnm6yjmTbi3r51oef4Q0iZCYmQvEIjBJZtWqS1XgbOgPZSSZO8UQBmYvXNF1uUkHPgMwY7UYvbZmFSZrv8a2KrMUGL74HVFjVfgli8_lcIiE1xBDZfuZ47-yUmgjOnet20dmdh3liu6lsTZLvU7lkMmEZ02isFGLAc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
ویدیویی‌ازلحظات خاص و بامزه پپ گواردیولا سرمربی سابق بارسا، بایرن‌مونیخ و منچسترسیتی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/persiana_Soccer/22818" target="_blank">📅 13:08 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22817">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NCGe_QCSSxu-CwQs1gCXTp55jkJmdwxaGWBgpTuJ0_1KdrdYUu1lhsU4pKmVWtk1_4F7_Eeb5SqtvnDo4zrl6qdjf_X9SagJo3Y0odiC9FTuKvqQHj-z14EJAVL2jnrvD5-ZWplAViHuUiq2lDEysP2ic0ZWoeDmftsoRm3_WDkNIqamEuIty6Grb8aNlmZiDCZUpAnf2jWY68iGPXgrcmqrDcwNW7Fy3ax-f7QJpfMuIWpT_uFVk-9QoRYV97Dfy68HMxSStUaNMQIQAtjenasVRUAELujf_nEVEcVzyMkn67UOZ3FYDSrMj0mfkZ94VFxJuVVRNpaNfXwPuZieTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#فوری #اختصاصی_پرشیانا؛پیرو اخبار روزهای اخیر پرشیانا؛ فیفا روزهای‌آینده پنجره نقل و انتقالات تابستانی‌باشگاه‌استقلال بزودی باز خواهدکرد و آبی‌ها قادر خواهندبود تا بازیکنان مدنظر خود را جذب کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/persiana_Soccer/22817" target="_blank">📅 12:40 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22815">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/070c28a96a.mp4?token=gEZgOzLC4cq6rl-N6ZSIoXPs0DfvhviDyayKNkn-tv9pRj-57Cwln5ytkxRziGpOPQe_KcRcZlmubKF-aTDcV95I6Me4paJorXmYGWK3dguHyszHIDZrmkKRLmWzyycpRMFQHGQGW9A4pBpf0B_m0ptf0JjWr3N_uh4EClHsDeHzD9MK0kVr8ZMh_wycFakHBJgmbdtGvRGasOsnVadgwOYgfM1Kf7WvUuBGTCYK8AJZ1Y_U1S4ofaG_yRReLdn-J6DNUfMMS3_9rR-ihsinwXUG8aWvXcO7Am4tUwjQWo7nwZG5olfB_FAsGx9IwFTX6uWgtmZRDeoG-re5Etx-JyUieXUN2oJmwoRCenQKME3v3ef69hmwK01w0l8wxZC6oSXNfGYzO19lsedgDuzE8rpI7oSIIFUhwW_ve_NHMdgqqXeD-seLLotXEHLU6epweQ8wokJt3NSs4wNZdyws_NSMHokMmI_mqqgTE_LI3WEhgJmFccDwJN4zRMeVBzPMrYFcOS0MZKU7buWGOImYO1ijFiXFxkyref577VkOi48AMEtGBm0o56r6NDihQhNn64EoMugM2JI1DJtzFjaH9KpmGUvSmZXlYiVCnqNokNwzrcJLX9UMH08Q9FcIDQBwz1eP_ZdxMPsO0EiUzwtVtoAxjBBydFDwKjtxqM_hryg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/070c28a96a.mp4?token=gEZgOzLC4cq6rl-N6ZSIoXPs0DfvhviDyayKNkn-tv9pRj-57Cwln5ytkxRziGpOPQe_KcRcZlmubKF-aTDcV95I6Me4paJorXmYGWK3dguHyszHIDZrmkKRLmWzyycpRMFQHGQGW9A4pBpf0B_m0ptf0JjWr3N_uh4EClHsDeHzD9MK0kVr8ZMh_wycFakHBJgmbdtGvRGasOsnVadgwOYgfM1Kf7WvUuBGTCYK8AJZ1Y_U1S4ofaG_yRReLdn-J6DNUfMMS3_9rR-ihsinwXUG8aWvXcO7Am4tUwjQWo7nwZG5olfB_FAsGx9IwFTX6uWgtmZRDeoG-re5Etx-JyUieXUN2oJmwoRCenQKME3v3ef69hmwK01w0l8wxZC6oSXNfGYzO19lsedgDuzE8rpI7oSIIFUhwW_ve_NHMdgqqXeD-seLLotXEHLU6epweQ8wokJt3NSs4wNZdyws_NSMHokMmI_mqqgTE_LI3WEhgJmFccDwJN4zRMeVBzPMrYFcOS0MZKU7buWGOImYO1ijFiXFxkyref577VkOi48AMEtGBm0o56r6NDihQhNn64EoMugM2JI1DJtzFjaH9KpmGUvSmZXlYiVCnqNokNwzrcJLX9UMH08Q9FcIDQBwz1eP_ZdxMPsO0EiUzwtVtoAxjBBydFDwKjtxqM_hryg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
محبوبیت بسیار ارزشمند علی آقا دایی اسطوره مردم ایران و فوتبال آسیا در بین مردمان کشورش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/persiana_Soccer/22815" target="_blank">📅 12:06 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22814">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hXo6i3bu1UbKHd-1ymz4jGf5CfXcRv00A7nAKJWwAiwtj3x2cB8TJSvxlyNGLDv0_Pi7yHZAXqRXUrr1-mvIpY48TKyLEbNSJsxBfY6z5QXNC_gvHRmXdNv7tgMQAxperfviWoDQhGMdHEyevykp0qk2RT7edapDqVJq4eRF8v_fED_18TS4VDhcGKyG39ZA9-i8S29jj9upLaqHDRi2OzFfPrg_IZ8o-xJcR0gdnfdJ3pC4tH_M3Uo0dZVvuw6vdNkIwkouDo91RRFT671uJsUnFupX7mhfyhFiEHY09nEp2xPjpT9Ie3Pj9JfORRejJ-as7DWtyJLSVeCsD26j8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
با بازگشت نیمار جونیور به تیم ملی برزیل برای جام جهانی؛ وینیسیوس جونیور شماره 10 این تیم رو به نیمار برگردوند و خودش شماره 7 پوشید.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/persiana_Soccer/22814" target="_blank">📅 11:47 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22813">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z_Em_VTQ1i76FTDwwRPPRzspVwnec_i7eX7hKN4VFFk4HTlGEdAxwRY3bacRu2SqdliYDJGaGpjwPFWOzPckrXQARmMnBXNZGmz_Zde2KazPNaff0uuJqcoo6QPeDZxUfoyDUB1mD00qWeFXutZlCF7_IUleGn3G5Vo7EUSBiWLiGomzAafdgpivo9Pv7GKiVZtZsUqoHPNgmEDsLTpf8DGVmKqImTR4b4-6E46DnL0jpmYe-riU2aiFRZFZCyrS1yRkOwKUXBrpoXalFmZvXHnL4hMS-tlgaXtgai-r4OOBp92BYOSEszpdzevGl7HsUYnLCi75XSvaaGj56q611Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">درصورت باز شدن پنجره نقل‌وانتقالاتی آبی‌ها؛ باشگاه استقلال برای فصل آتی رقابت‌ها برنامه‌ای برای تمدید قرارداد آنتونیوآدان گلر39 ساله‌خودندارند و سنگربان سابق رئال‌مادرید از جمع آبی پوشان جدا خواهد شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/persiana_Soccer/22813" target="_blank">📅 11:24 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22812">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cKTkb695nWPIGfFZyFOp_mxhnCo2I2Cg-tUQ6q5VB13SrJ3gaChUzKgtr-lgKfMkizun2GTydNXFvlGrS3dU7Ek0kiJKVBdPbDkD_fIwm4erVChtMIyERBm_nES9je0eRVC-zZcDGy4qHi3cZeJhLtGvWROvmkl0VfvlGXx4DjICNyV8BvD8redxyWfgXi_N0y29zTUyzbj4c3HaYEPt5eztLEa-frYTv8Tys6ojT0WMB7d5hMmfIGmVZKBbuDtBnxeBEiqtbw2XSjzS-lmaQ8_2fp4xM5rMV1YEq8K8TAjFTvgcnoxDmOLd-YzNnPo7ncnBper3Ist_LVny5BW7kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
🟢
👤
طبق شنیده‌های رسانه پرشیانا؛ سروش رفیعی هافبک 35 ساله‌تیم پرسپولیس که بازیکن آزاد بشمار می‌آید از دوباشگاه‌فولاد خوزستان و ذوب آهن اصفهان افر دریافت کرده. درصورت ماندن اوسمار در پرسپولیس قرارداد سروش با سرخ‌ها تمدید نمیشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/persiana_Soccer/22812" target="_blank">📅 11:24 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22810">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K5D7zJFBdBnd1FV2SPURYHinnJlr8Vpi22VIZqKE5vtHemvA5n1wTb6jFpUEntEOmUjnVpgzr26qMw7n2IpVyPp29Bf5nVnd_VfizojzkvW4bRN_QTTyusovGJVOSss855Ce9reOS5xWXmzAcdK85tLerDvFcOMh0XGCroa2WNGb5DuMEXdMgnPadI3tAHQCuaza_V17ibacaImdDvgfPr3nWsnrXqUdSQorP5cVvrDJG45a79GsIzSXhMV5icRJRXJWH4LRCHFJdaYa0Izm66RYOY5LNlA-2pZJTPBsXzFv9iUg34q96O92YiUFR0R-mScGgfaxR0xEdDZXZUeVog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
آقا منظور پرز من بودم. شماها چقدر آی‌کیوتون پایینه. سه‌شنبه 150 میلیون‌یورو به حساب سپاهان واریز میشه و رسما میرم اسپانیا برای رونمایی.
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/persiana_Soccer/22810" target="_blank">📅 10:42 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22809">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UiSd-mheKOgsxrDLBNwIrz3lXgp0CHL7Em09ZB4qjWuOfXfpkkV64RJdN7Qra75XcuChrL593PXhlMfNd2BTgWCOGt_zWdjPGWY0l-VBHeLhVELIBFIGvWXVrWvd3Biio0kX5hgoQrvnYQyMiF58wquCXis45fYII9ISn7BbYPPnzzP1lpq7MSSA0c61SM8Ja2rBN1LP9uR7CdNcYSDRfKSl3u9hyFzv1XrcZ2xw1lcz_PkIxF30FYusPZWWBlk4XaiNF86NbE-IfT6PxevPDLn8dQOBvSd_RAAFAh3KqlJPKTi8iCkZ4BCfMJfzj33CAQlsEakOraML_gLgDd3BaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
شماتیک ترکیب تیم منتخب فوق ستاره‌هایی که مفت جام جهانی 2026 آمریکا رو از دست دادند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/persiana_Soccer/22809" target="_blank">📅 10:21 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22808">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PgFwInCDyrsbaxy8Rh-RIP12VDmlFZhBlYyKsqSU0HM-kPKuFj9f7M-h9ZK_hJiH4vu5FHF35CcBv3-L14ZL9xxiqKz2K1kn_1qGDcfVWzWp54JxtF2HhcWRK28XWXpl_2VwrUqNBbBcyPn_uPE9sx_7uqSeEBY9mLh-N9p37Nbpy_Tfl_2xCj45C0Wu4UVS_1WmBCjQbLcXIeJmbtg3jzkVDlGRIQ7oltYXM8KYVBtbPZDqIu5vJtT8alwBi1FAM3uKWGX3_owvZzfXupfx4jFq27hQrHZ-UGP7FssdljwjfIvT9aKklHSV981IRcAVjnOMBlqhqexA1qN8taA1nQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
آموزش کامل بازگشایی شیکه‌های کارتی ماهواره که مسابقات جذاب جام جهانی رو پخش میکنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/persiana_Soccer/22808" target="_blank">📅 09:50 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22807">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/atjQkO9ehJAPYwhyN5kfbwZyX5lWMcBPYkEW_mYXuNSZUY63DMxXBS3lbKL6fOKcfIT_3aOCVLHGG-aOIkgGaBYDU8onfxVt38aMimWh2bLtnsdYVChEMtsGhpe6bVLJRXO1IkGcNvz3hyujyrn6EE6hjLvQzG7AVqcuGdQx6TqtTOjYOe8Nig_iWgFyjkIEPHs6Pe34VNjWHjjjsIkVczVeLQc7HpHjqBhkJY9XlM1EuvZl7DQksE_NCmXykOAZFzzXwypLLDf3WQiTD3aDKq-Cesf2OZkhme96V8JZ12ZmGHaBM8iMK49srbkrsCmhQquylDBHtmBqGL-1M0NfzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#تکمیلی؛ قطعا یکی از این سه گزینه مدنظر فلورنتینو پرز خواهد بود. پرز گفته پستش هافبک یا مهاجمه. گفته‌بازیکن‌بسیار ارزنده‌ایه که مثل رونالدو، کاکا، فیگو ماندگار خواهد شد... یه درصد تصور کنید که‌ خولیان آلوارز رو هایجک‌کنه و 150 میلیون یورو به اتلتیکو مادرید…</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/persiana_Soccer/22807" target="_blank">📅 01:39 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22805">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l3fy0_9lwqXoAfgUK9BAYjjo_2paZtqTEhn1g-4KO5yyucB0k2s-9dr9KK112MQl4Xz_YiACPrs5ForvD3CrhHhTd1iBaAe3Tv3mnxQcIClLQYkW3afvmlIJQzrBAiaZ2UVsGOTAIch0PGLvWZ-mmAIJ6aLbEZ2ZpST0QeaXwPCMnEUTV3KUrQeNM8JUIfmk-Mgp2RJKlPWVvrNl-4dlmYu_TC1U_Zq1rivX8o2BiaC9h34Nt_hNbIoKhywL4I_oIOoaJHLbYiS9FmOaCFUHnjeYGYGwaNwlo_kBfEuUqPDbWPkE-Oh7q2hqCYCoOQo4BunYBhLjOPSygfQ-8JTB6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#تکمیلی؛ قطعا یکی از این سه گزینه مدنظر فلورنتینو پرز خواهد بود. پرز گفته پستش هافبک یا مهاجمه. گفته‌بازیکن‌بسیار ارزنده‌ایه که مثل رونالدو، کاکا، فیگو ماندگار خواهد شد... یه درصد تصور کنید که‌ خولیان آلوارز رو هایجک‌کنه و 150 میلیون یورو به اتلتیکو مادرید…</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/persiana_Soccer/22805" target="_blank">📅 01:23 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22804">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FbHb1S92MOIuXukW20vZkGU8OXFh6rlLj1ryPVpGMv5uV0DXm9Aqbndxwm4sFf7p7lTOPp6Ml_6jP_kNczjf0-GDbH-6Q4k9vEauu0QzJrdZjpQj6LVUkpraZGqtfQ23zdcJoFDIz_ZjDGNxDSlHUrVJm9lQUGvHLP0ZoWicbbQdCOtQAiLRUHG_QGcRypCKyL7fWxPVEbEUzXGyo4DSXzkObLUFTbO2yY5bvp1li9Yl99s-Rp45l2QsdvgUVqY-JWnOb-TyqlEnChfQdOj5LjxW2OTdPd61XPldFf2j2A_tbgvj4iuJL3Ztd52mMTgP-6VW_sdua7CC__IEie4y2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌ دیدارهای‌‌ امروز؛
مصاف تدارکاتی تیم ملی مکزیک میزبان جام جهانی برابر یاران میتروویچ!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/persiana_Soccer/22804" target="_blank">📅 01:13 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22803">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wi_8jwHg2c4DycbYXuIear3ffTxAoNJqex7aJHtujmZdJg5sGIEouw1oU_HMTUwZYN-IzInDbX2Qj9I_qwuc5Ir6vWc5SOZwrmOblFsmJ_QvsP0yyz24S4Jm1XHcwfT-w2VaxKut4Ti20f40ALLc0TvtB61BYD4l_Wtkw7hXzeEEQwHLYK21v8VigQm3UKs7FAqIp6kN9k2aLO0_EhcIC8oKAUs5dmYVcueGVu2jHOobG2nuWt77EWsT__JGBkkYSFpLv4LyqrzMBIIe4efgtcxOjS0EM3VObj_0uiyIM6_-rhnTQwRjhy42IUomhaasN91N3AcoEoMqz1phCREOPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌دیدارهای‌دیروز؛
توقف شاگردان دلافوئنته مقابل عراق و شکست‌عجیب فرانسوی‌ها برابر ساحل عاج در فاصله کمتر از یک هفته تا آغاز جام جهانی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/persiana_Soccer/22803" target="_blank">📅 01:13 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22802">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XDACSDa25jmr_HknotT6jm7u8GrUmxCJjtJ9UmbgSQ5MNH60jsJmv1YsrpDSLKIblETwVlJS9wK1G4ILS3ZtSTFuKOi5zO--PBrbErbrM_Dr6EaP2Eqwc-X8iu2MaXZlbOPu8iUGbcgDIPh8KVzmpUhAXfLqvNxguhzGg9iAOP59kBMMDOhxFDAwt08jWP79pUoShPlAxiZ_KY5xQhXAqXKsneEH_PZPb18HS-d0qvz6fQM6nXTago2m4NG35y25r5OiCGSJbEYENrlDZbXinFuDVmb5dyJ6ASqcAuXAaJwmrxYb101q1PaEPMOP3nxDECQyNXGLYoi01vbtD_ma5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ اکثر خبرنگاران و رسانه‌ها میگن منظور فلورنتینو پرز؛ ژائو نوس ستاره 21 ساله  PSG عه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/persiana_Soccer/22802" target="_blank">📅 01:11 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22801">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AXcqWYESh5C62txQ9vXLKNfIC1kYOY1IrML5KcmnJYoun5IjE-C11O9TDWwUbv1W-OtZjbbjt4pb_IvnYtrClf_nvBnjVZFzSDrnsHYv_ZzU4zRqjHb2HD5KN6nZJ4pZep9dqxHy-8OTQf9L029sStznfT_haqkGwVvdw0Nk0NaMQmSoiYLIkXh6YZn2t_9aozDDLtYgy-jaYQEfYGopBc2Yamq9aw5bY_UGNeqx_Xf-0zndTJqlchOZ48gfox5ljOWlEudAi8_puFKvlvDMtQaQ2X69Pzhc4ed0iaZxeeAdIwEE7FvNfZM0-XdzKm2qfuBprId6Gq9WvUxNcizxaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
فلورنتینوپرز رئیس‌باشگاه‌رئال مادرید: روز سه شنبه برای‌خریدیک‌هافبک از یکی از تیم های لیگ قهرمانان‌اروپا پیشنهادی 150 میلیون‌یورویی خواهم دادم. کیفیت‌این بازیکن بشدت بالاست و بارها علاقه خود را برای پیوستن به رئال مادرید نشون داده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/persiana_Soccer/22801" target="_blank">📅 01:01 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22800">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ebb6f9bc26.mp4?token=SN8BF8zUx_52_6RzQWfVyEpD0SgfDNaNYqydncXymHCYT4vVib9wmObQG_t9xDE7QG07RBX3SjMTqYOJbbC6RcHVpaQt5Fy2gUx3W_upedwTWjKJ-b3v7Mg_x2gwd7uI36LXNiK3kcdr-1U0l0-1HKAAjjpH7zbQQKe1U04Qie_OEzqcUojt3aAdSesI_vKziDR2-0Fx8-lTYjk3ONRhP3f7nPYWOotDVzgSljykmVm5FQ3fVeFpvXUTctFq9x8xxZ2so5xf5W35jut5Tl_MhbBgw7qs6g8VOYjsCsVfdzeiNKQR7rnzhOPJMb6-2ybbpGsDLVo32onMLK0qGp2FUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ebb6f9bc26.mp4?token=SN8BF8zUx_52_6RzQWfVyEpD0SgfDNaNYqydncXymHCYT4vVib9wmObQG_t9xDE7QG07RBX3SjMTqYOJbbC6RcHVpaQt5Fy2gUx3W_upedwTWjKJ-b3v7Mg_x2gwd7uI36LXNiK3kcdr-1U0l0-1HKAAjjpH7zbQQKe1U04Qie_OEzqcUojt3aAdSesI_vKziDR2-0Fx8-lTYjk3ONRhP3f7nPYWOotDVzgSljykmVm5FQ3fVeFpvXUTctFq9x8xxZ2so5xf5W35jut5Tl_MhbBgw7qs6g8VOYjsCsVfdzeiNKQR7rnzhOPJMb6-2ybbpGsDLVo32onMLK0qGp2FUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
🇪🇸
تیم ملی اسپانیا امشب با این ترکیب پر ستاره در بازی دوستانه بمصاف عراق خواهند رفت؛ فدراسیون لاروخا ابتدا قصدداشت باایران بازی کنه اما بعد از قتل عام مردم در دی ماه پیشمون شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/persiana_Soccer/22800" target="_blank">📅 00:57 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22799">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LGFIuP_nknMtQ-GETSpWR58Pb9ymbvS9ubjj1hJq5vSIjcqwWnW2aBF5eVfdcqO0bjluheLTJJ33B581rIk4q7yP1Bh-xkMtJzs4ZSj6Zd3iru2rh77M0Vdq0lxfg6UAxeRtrkR-qhwHiMwd3fEwv0Jb1kUx7d5uzueYh_oN5NfUbW_scEGJPkpX-JEjN7SwMcwCEXK4rsmSHjuoWBskmAMFeDUyvZa_jOPfqqsVwLCmPhx0pr4f0cn3Bbq0oJ_QZimOPKrDnWa-mto65-2phHyx82zzLfX2Gv2PMnmPqtP_Q-FDE6ayktqhSutSWx89CrCUtJ-QZoUjCXiunvLxXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
برخی از خبرنگاران اسپانیایی مدعی هستن که نام‌بزرگی‌که‌فلورنتینو پرز قصد داره بعنوان خرید جدید کهکشانی ها از آن نام ببره انزو فرناندزه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/persiana_Soccer/22799" target="_blank">📅 00:52 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22798">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e2029a699.mp4?token=gvAzquGRnwsZfeblRPn1Ub74fhiVjFlaP1Mape7IVsWh33ApcEOKnybSheoc_5y8RJF1Q_4suvjEt3iGSqr82JyYNdiSks_v5pAnE1UabRx_3ST3Xuw1U4xCi6-1T1rfxTHl09EXvgmMxYVGO5jf4kTbo9x9wLyZ2fKX3VJrY6-wAd-Y_LmjPTucT8pv5G-tpO8qPJDntxIOS2ZYWiOW8TXp1HQ1_i1jLv0d1bwZK8qiaJ8KheRX6evuWuzrfKkj6O0u9PQzr5OmIEFxsHur9xYya8wCQyKaIJjOosjrHCkzJeDA4h1vjJ6LsZ1ehU3wSyFvZYT9tBuXWvdlm7YliA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e2029a699.mp4?token=gvAzquGRnwsZfeblRPn1Ub74fhiVjFlaP1Mape7IVsWh33ApcEOKnybSheoc_5y8RJF1Q_4suvjEt3iGSqr82JyYNdiSks_v5pAnE1UabRx_3ST3Xuw1U4xCi6-1T1rfxTHl09EXvgmMxYVGO5jf4kTbo9x9wLyZ2fKX3VJrY6-wAd-Y_LmjPTucT8pv5G-tpO8qPJDntxIOS2ZYWiOW8TXp1HQ1_i1jLv0d1bwZK8qiaJ8KheRX6evuWuzrfKkj6O0u9PQzr5OmIEFxsHur9xYya8wCQyKaIJjOosjrHCkzJeDA4h1vjJ6LsZ1ehU3wSyFvZYT9tBuXWvdlm7YliA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تلویزیون‌کره‌شمالی‌بخشی‌ازدیدار کیم جونگ اون رهبر این کشور باتیم‌‌فوتبال زنان کره منتشر کرده‌اند. دراین ویدیو بازیکنان دوتیم‌فوتبال زنان نا‌گو‌هیانگ و تیم‌ملی زیر ۱۷ سال دیده میشوند که هنگام قدردانی رهبر کره شمالی شادی می‌کنند و اشک می‌ریزند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/persiana_Soccer/22798" target="_blank">📅 00:52 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22795">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SDH5OInDypqD3MKKMiHHHwlnlJgSQgxpkiWcob1EFbMnS8BbqS5xHZdCOKAh7splnaUmJPJ4jR5TxZoBZpAiklEmm1y0rz6sxPVn6Xei0cB7s62SVlknDQ6gsx4rTTmrw3py8Dy5X9vU0E6kJOKhUdsaahv8H_TURH0eOPy-fYv2iyHnUMw7G2xuzh6hEseVhDjT6HVriIdPEEiUJV-EpCHvyAz3YlLvI4cGasgGIFVN53Gd1S1sDovOxQ7_ZxUq8OuKwz5u3ZRbLkoWOj5TH4IoSJRUKve6udgYQh7Bu0e6OycvdRv7x_6E0Y1hwVBvI3B58tD6CE98dnmSv_KRiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
#تکمیلی؛ نشریه کوپه: امشب فلورنتینو پرز میخواد یک خبر بسیار بزرگ رو اعلام کنه و ممکنه بسیاری از هواداران رئال مادرید سورپرایز بشن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/persiana_Soccer/22795" target="_blank">📅 00:32 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22794">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">⚽️
تیزر فوق‌خفن نایکی به مناسبت نزدیک شدن جام جهانی با حضور ستاره‌های فوتبال و سلبریتی ها
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/persiana_Soccer/22794" target="_blank">📅 00:19 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22793">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SmLNaDmoyY_rSC_2S37I8nyVjknRJ6fF1AHO7ezhXVe_cWCDs_OzPkCgOesl2W1Jas1BD-USwb1zvSEPvDi9QjajkjalCne7Kra-LyncsOO1yXCHs4UHwwPoNdDf9R1Jcy6AM19UGaomFKiZ27IXnzBckBwA7ZEd-GA5quyzd2VQHLxk4PxJ-RRbZgPeveLHJzoKVscUsGs5p_fq2euGGg4tG06Nx_C4eA_5jDRy0KdTKmeDvWv_TnlWYnr1hqbqyqMtlqrs54q9p0_d-2NBJ-No7-kf66wxZb-fAUBQvT3cU3yfl6m15h27ZPoBIffxcIOt2-npF3PEUaXq73yJoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
با اعلام ایجنت مونیر الحدادی؛ ستاره مراکشی استقلال فصل‌آینده نیز دراین تیم موندنیه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/persiana_Soccer/22793" target="_blank">📅 00:14 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22792">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VAZAuNNEfQhWFGzW-caI1f_Ad4pzQ60oYBtk8Y7NDR3Bik8u8r3qdhIoGDRAg-RiVmPb0UVNXRJ8IYH8ES8wMXgMq_JNkfZ7GkwPUpqzEOXiOcUzu4Yy79oGv0yOClNL3EX18bmRprODHAjEKI1cIj79kLmLNBHg7Gu3WLkRmsc8_-eNiaixD9Bh2eRe3iQX3qd99Cf1B5hG5RUGpn0zw7YSYPX5sTjkdo1OzVvWKy_Qo5gtFCs19cuoxC9-CUUJmgSYCBsAsRdh_Pr2W0oNm5xq-bNh4UzcwlRnrsug25ZIu-MfHx43X2d-wxziF9dcRbkecqQy1Iyefm68GATsJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
آموزش کامل بازگشایی شیکه‌های کارتی ماهواره که مسابقات جذاب جام جهانی رو پخش میکنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/persiana_Soccer/22792" target="_blank">📅 22:55 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22791">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/elDfCUOlWlhNkU9n71bqLq8XXhza6c9nFMn4pAo8N9BZn4s5G7TCa_0e2dLBMRu7SPhDDmaZ-u4TUEaAXL5_2xzsgoH-sHBT5NS7IhGjZKRRIMjh61OW30OL6uV46IgPAPL0BPV_GgSj45r_TMSejeDTRjIMKWtwELXyJlHO_GybALXYtqSXFWgyFLlMmSgsKl4WZO7-1fTo-1vhTOn2Y99wB630vH9lLk343aCHnNRT4wiMFMM46tVLvL8nRVr_BPm8LsIdaRhfQzp3mkjN0mnU7zLUM3UlR31X1s0YsNm8mb2kPB46VQB4qHr7TYWKEBWql6SH-frBAWf5oaYWjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
برترین تیم‌ های تاریخ رقابت‌های جام جهانی؛
برزیل با اختلاف در صدر جدول تاریخ این رقابت‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/persiana_Soccer/22791" target="_blank">📅 22:40 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22789">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Pdgz5Pr77jE9449JpuInGi4V1hYyY6B_oyRbraEGXpAWTuXCqEkS47KfVN4L3gX8hTqGDpLqkLz8AKRhSwHheqkYhlBMC3VaNJXBgsABEMmlqeU9M460gL9qfRm2pn4tuEkSBgotoYJZvigCK-Nw6ZsFGUsE8hy0cOIik8u8g9PfdkfK3Le_9GYN4ypIBgjowXAIFvqxfdzXVSaXY_cU6TF_IuhKpH2nu7dr040yX9RcX7i2NYqgx5tByTW-TPqUHDKnZ9ACs55Ubgy9Qc--3idcEmzmZbw1drA-p2mdSTZd1Vj-H8H6f7cJKpMN6D6nfrQFX3X_NsQTAoJTo-2p3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/H_FekeNbjYTW48XoVO2rbLCqlEy0Hopgo_k36NZaKmxcIN62WS3PKTQOm8fwM73_sRHkem7S6xZXbaGkuqEpaxvoQvrAGogfZmAzZHoT1vNd1X9DQ-_Aa7cYNrqzbGwlkXgXu8F-k1XVKvbfmgxRv8WSFfPyM86MfHsTukXl-CqEr3NZ9Mg8M0Efo9D_1Akoy4pQbH15lybXpTLblcozPScr49LD6Bh1xAVB221bkE9q-EwFb5wNbKbwWhNZB2j0T5nXfs6u2I1Mc-jMmzXiOQjUZrShGiNcGP2CGLShDLvkLMYNmSpbCW5D3e6uqgQf9nFGSilq9f793Kz4zKm7qw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
بااعلام رومانو: آندونی ایرائولا سرمربی 43 ساله اسپانیایی با عقد قراردادی 3 ساله رسما بعنوان سرمربی جدید باشگاه لیورپول انگلیس انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/persiana_Soccer/22789" target="_blank">📅 22:25 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22786">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31e7361d2f.mp4?token=OqeUJBLvQ8MwOOVW_GoKKIXHJnBpKPJa3ORkFVv4DDKmeZfKreRv-xGog8uxGWZmMu6wASSorCiVc_CCI-c_zaRq8PfLUY9F-priBY9wpdeI1c9X1bh8cSAWBmBMBPsyjqBmyrm2pAvRHxthyLBooimovAs8quf2111uP5d9y8WzFvb0AAyASpDj6mSYJS_pOBU9pfkANtRRzgGRBPrK6EjMAcnn8zEV02EzeQBhjMNdLz4d_8zJ26sQHE1RwM9x16_U-9Gm5SILfSmGvM4m7DDkLUvXV0W891A5Vac0JVXpuRp0WbIgBt_zZb_Y9PnEW2c1geDolikaFyw96G3_IS9dRwYEYBA0OVrvBCyUWFrttyt47bBGjA7Wal0t5grd07QxIClZRSCfLqae5FZzwAL6tm7zm7e7C74no7lSNmTm1jlcZxkEo_udC0DH5gUZNdCaQJXIr36_H05aUuL1UUGizCugvzX2H3Jy5GbxFmhuIIgG0Pwvrd8sOkYKHRN7cl4tfipSNJoP6hyBOoXPExr-2_0JKlqwN1jw3eQoyvHTJoTdPzfknrvKXoLIxe2AaHgFAEhxcqp-PxiQw0h_gmX_qD3CsZQP8X8FNFPsXhrTXOmcydsBSJIYCQyMl3LznMumLsAPgzLYxBUP_kWLu7BgSyEXXn_DgaEbWCtHDyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31e7361d2f.mp4?token=OqeUJBLvQ8MwOOVW_GoKKIXHJnBpKPJa3ORkFVv4DDKmeZfKreRv-xGog8uxGWZmMu6wASSorCiVc_CCI-c_zaRq8PfLUY9F-priBY9wpdeI1c9X1bh8cSAWBmBMBPsyjqBmyrm2pAvRHxthyLBooimovAs8quf2111uP5d9y8WzFvb0AAyASpDj6mSYJS_pOBU9pfkANtRRzgGRBPrK6EjMAcnn8zEV02EzeQBhjMNdLz4d_8zJ26sQHE1RwM9x16_U-9Gm5SILfSmGvM4m7DDkLUvXV0W891A5Vac0JVXpuRp0WbIgBt_zZb_Y9PnEW2c1geDolikaFyw96G3_IS9dRwYEYBA0OVrvBCyUWFrttyt47bBGjA7Wal0t5grd07QxIClZRSCfLqae5FZzwAL6tm7zm7e7C74no7lSNmTm1jlcZxkEo_udC0DH5gUZNdCaQJXIr36_H05aUuL1UUGizCugvzX2H3Jy5GbxFmhuIIgG0Pwvrd8sOkYKHRN7cl4tfipSNJoP6hyBOoXPExr-2_0JKlqwN1jw3eQoyvHTJoTdPzfknrvKXoLIxe2AaHgFAEhxcqp-PxiQw0h_gmX_qD3CsZQP8X8FNFPsXhrTXOmcydsBSJIYCQyMl3LznMumLsAPgzLYxBUP_kWLu7BgSyEXXn_DgaEbWCtHDyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
بمناسبت شروع رقابت های جام جهانی؛
بخشی از صحبت‌های شکیرا خواننده مطرح این مسابقات.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/persiana_Soccer/22786" target="_blank">📅 21:55 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22785">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d39ef7da3.mp4?token=SuUdfnWriRbymFghtbl5oFA9K4e_T7uwksFdZB1FJ6Bxrpxvv_AoDY3D5UbTXwC554gNBQOKm6JRNYtd079spRnX051NGZ4-dqXw-GBC_or3Iz7TtsuxmkP0N0m8DSAlSxfq43hpVqFDgKuse9XyO2IDBGY5SpxGljAPmCFyFxkS-PiWaIt6Ia7kUFEXx5oZwYL_e2t33sz_lh6E4ak4ehCFwIo014es580ytMr9DFpPqUSnfVhiUlFELiaYy8gufOEX8k5N9tXQsM2YIJhJx7-gs--wmgXffM9G5sYDwTwoSUaCEJ8U-Sfh0gy7wmQ7o6fdLY7AJ9DuD38HZtSVTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d39ef7da3.mp4?token=SuUdfnWriRbymFghtbl5oFA9K4e_T7uwksFdZB1FJ6Bxrpxvv_AoDY3D5UbTXwC554gNBQOKm6JRNYtd079spRnX051NGZ4-dqXw-GBC_or3Iz7TtsuxmkP0N0m8DSAlSxfq43hpVqFDgKuse9XyO2IDBGY5SpxGljAPmCFyFxkS-PiWaIt6Ia7kUFEXx5oZwYL_e2t33sz_lh6E4ak4ehCFwIo014es580ytMr9DFpPqUSnfVhiUlFELiaYy8gufOEX8k5N9tXQsM2YIJhJx7-gs--wmgXffM9G5sYDwTwoSUaCEJ8U-Sfh0gy7wmQ7o6fdLY7AJ9DuD38HZtSVTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
👤
جمله‌ای که تمام راه‌های فرار رو بست؛
فکر کنم‌مهدی‌طارمی هم‌این‌ویدیو رو دیده بود که جوگیر شد و به میلاد محمدی گفت بره مقابل تیم ازبکستان پنالتی بزنه، که البته اون پنالتی‌اش رو خراب کرد:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/persiana_Soccer/22785" target="_blank">📅 21:45 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22784">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tz_Qt138qYkB5k9RdwzYDH5E3Uhy-KAnmd2y7hXKax0D5QpO-4-YM8ncjIpxchmJiI-7OfNahUfMNZAbGtEZIFSJ0ZMdzMlA4gVogrTnAfVgPlioJCEFhEB7-jcXRU-JpE-17hrqVfkEdVEG2Kc--7TtlP-rYGZLrxlRVc3OjujLozK0mFn0Q5CjZcwzFM-wYTnJXx1GtQovG5d6CyPKhTU-3oY1gV9KXqw1TfilaD9Q33_DaNXwOf6zJmgy2y-Nu7ngAz5_OvDdFIo5jndN245hY0sy66rYfKG_ms1jKKLXQ8zbF8ymtc3AqnOs5kzZ-tGetMPxeiILts0mIY4vQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
برنامه کامل مسابقات هفته اول و دوم رقابت های جام جهانی 2026؛ بازی‌ها از 21 خرداد ماه در آمریکا رسما استارت خواهد خورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/persiana_Soccer/22784" target="_blank">📅 21:26 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22782">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cihDgYA_9FbZ9k3D97yLEti__ej4Hdl9bFa-h_27VFIXmwRxJ5ZrhM7pHrFoO4dYh8STYiYWwinH7XnLbFZFwfdEvceNtCvXU7kmUj7EoDdtmdRtn_NFUAOxVKjVdJpUZYHVCANiRaD9snaLc35iQJdnb0PQYVpFNLEgfo0CX6qi2NAO6KHs0eliTMbpiAIlqgevxXayS2Uqk2WQ3j5awTm_c1pVjDQak7wtgKrxLMdBIKnTlISQqLhDRJUhSs1FktjpzKqbb5Z-vylM8xZjSIRCP7StofYiQVzLM1yRrMbnPWzpivWg1gOBP123I2HCzegTpBGyHHwjeBWBiJs5ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dZKezVGihegPVm6Fp8cdft_e2jI7W-mfNRM8RQXX45cizzReAchUApdxX21HPbB1tAGge5X7YiK3pvHGOqBnLYFCkq52eM8JleOVJlGhpWNWG5IA148TDDSoeO3k2S-aldzd0ttaUF7bAaeZx5jPwf5aokNaloZJ12Y2X8NnD3r9LRk8G-3Wor4lhSWNaWfJoL9k7fTSHFBH3LyY7A5hhaf-EZNKIfOqeOLMfHPqlK3J2oFTY5iHp5PN8fgDoLxKKli2JTxYzcGimcO8lViq9EX-DN9EJ9DLKTt31Vo74hdwx9eLHN0UmwUCzxnhi1dH6FsCUAr7yYPjQK1LOP1Jdw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚽️
برنامه کامل مسابقات هفته اول و دوم رقابت های جام جهانی 2026؛ بازی‌ها از 21 خرداد ماه در آمریکا رسما استارت خواهد خورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/persiana_Soccer/22782" target="_blank">📅 21:23 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22781">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JbK5AONMeX4qdYz6123aWckswZHjVDOFQTWXB55IM9SobUHvzBFfOM2wcPslF4rP49jvFRWc_gBWwjGXSwZjP6OBCSvYqRIAfQ4cz56i6sdZDoS3wssSpPK7y0Zn8fQW73umNAgAi9N5u0RUSdSi9DCzrsbKgt2QhVSRBVI_fO8YJvmi1e0qnVAky0rQzuwNvfbaqWB1NFv6FtjSS95btvX20Q89prDUx8VpoCQVKPj6PvvOwdzpVNSBHdFvUFcmd5x42a14ZQ8_KsWMFCkN4jjY34-GhuGSO0Fv0TTML1M9pLDvBd4HDllRpMLvvFeAt6J4GVODkydfnfH7KGn4vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
🇪🇸
تیم ملی اسپانیا امشب با این ترکیب پر ستاره در بازی دوستانه بمصاف عراق خواهند رفت؛ فدراسیون لاروخا ابتدا قصدداشت باایران بازی کنه اما بعد از قتل عام مردم در دی ماه پیشمون شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/persiana_Soccer/22781" target="_blank">📅 21:08 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22780">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kziD6tal9CEaIY6RJyh0TXh7F5J1XYYmHtKXOkMDaWxtWMcIgUh4Jihpav_84Hhpm4-TgpGrdRHehZjmAaHcUfjUxnbleLo3yzNl5BWNDt7zw0OnrTQx2aph-8DQE2VKKWScGxcH27zr0oPtUssHVxqQQqg6ImfGtUA48M1QH4BdUdnUeAFvpQaWSqFqXowYGUGnlLcI16AjnUumsZam0iXxJ--FIfTSqNVpEZ3feBIJfCZrF5J7ZgexkS-1g8OLthKR4V_El8UVccctmkndmxgFpXULYfqVPhRFwgLjYcjhAyx9Zb6vlESfqPyWodSsy3pRusuUbYYyXB5pZ-IhEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
💣
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#تکمیلی؛ ادرسون سیلوا هافبک برزیلی 26 ساله آتالانتا با عقد قراردادی چهار ساله رسما به منچستر یونایتد پیوست و جانشین کاسمیرو شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/persiana_Soccer/22780" target="_blank">📅 20:57 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22779">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">⚽️
اسپید با انتشار آهنگ جدیدش برای جام جهانی، هیجان بزرگ‌ترین رویداد فوتبالی را با انرژی همیشگی خودش ترکیب کرده. اسپید که سال‌هاست عشق خود به فوتبال را به نمایش گذاشته، حالا با این ترک تلاش کرده بخشی از فضای جام جهانی را برای میلیون‌ ها طرفدارش زنده‌کند. پیج‌رسمی جام جهانی هم اعلام کرده که این اهنگ در آلبوم جام‌جهانی خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/persiana_Soccer/22779" target="_blank">📅 20:24 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22778">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZLzdW_G4XOf4GeZJFyjw00OjzglEck0xYMecLLY0hCWo2F9HHc4oVg7EDt0x17wuzetm-QMMFTuVLVkVuOIr8QlC4k5GD4JrvORVnuxdrdbP_HvBhkiu60JB_PWe-wMTHVyntLiFSGslPnk94GUJkd7zb5O1x_ZsPEiLEpWJUdJELZDNm591N-SvQj0Rhd6JS65UQ7shsSL46kmk_K9T-lRanGPvFmfyYeVWWXnAoW_wKcVTHJEXqrI-QI7lmDCe1PTduWUeMdsUZeu2Z02D_JiWZYqEEwA3388yj-2qqbrL52cXM911x088sCOxGCQ87zsEegIAPVRVVKWbfQpKVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شوخی‌جالب‌روبرتو پیاتزا ایتالیایی با عرشیا به‌ نژاد: من 58 ساله‌هستم‌اما چربی‌خیلی‌کمتری از تو دارم!  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/persiana_Soccer/22778" target="_blank">📅 20:04 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22777">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dmz4IsNjxa6Mj7nuJztlClBw-jYNf-npw4QKaQ5fEGDh9HbvVaQkqTzDYr0WRHeE5F1Eb9FNJ_3aergw9h1Syj4EpsXQ6to2VwxVBsd8a6ApzkqvOpRq-fFSYaejSZ15GSEef4y6PXRhJu_C_L1gJ37lzjjtNig28dCvKAX4gYmcTnUlldsSD9OK7v8lsRHyiwrW82fJ9q208sz3IphZ1f2CnsYcefaYYHNcgqpJmlQFoU4S9_LHHKPVynpHKnkVwvoBXdfmmqFXQ9w9059-FAqFW_0OnPSNuu3azuDJLQnxwipH5NE2JOKLSdh-YfTwzJA_LnU18ihPnVxeMZ6wlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#تکمیلی؛ 2+1 رونمایی رسمی باشگاه رئال مادرید درصورت‌پیروزی پرز درانتخابات روز یکشنبه هفته آینده. بجز این سه نفر پرز به آقای خاص قول داده بزودی چهار ستاره دیگر جذب خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/persiana_Soccer/22777" target="_blank">📅 19:09 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22776">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qZXrXPdgTj8QKZ2jOw3-nS1TJjQCf0nN-pEsZ_8_1Hqz4lQnpKGs3a2ujrvtPyubx-wq8Cmu66Cv8GFjxrj57VGcBlJoTsdR0JzfwArzR2IXCNXfJz5pF34y7T5kY33q03so415yKShVZOONRQSTTlZ4_iJ8g5SfdxV-XcIZjflV6f03EBZXCUniQwAbaFjgu3QauhSzdJ-_-2oSDY4OZ-UfxFYOlX6anke5n-F3bJSA5Wcm6WHt4B-PTVIulMlYdMwDTy8oCjhLfdyxHoLsRlNgYHttQcPTWu5SfhATW68tSVuhUWY0pbCcFTBwZ1dxaW6pgjuDP9bCWawv-UtLOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛طبق‌آخرین‌اخبار دریافتی پرشیانا؛ فیفا تا 15 روز آینده در مورد باز یا بسته بودن پنجره نقل‌وانتقالات‌تابستانی‌باشگاه استقلال جواب استعلام آبی ها رو خواهد داد. وکیل‌جدید و ایتالیایی که علی تاجرنیا استخدام‌کرده به او قول داده به هر شکلی که شده رضایت‌شاکیان‌وفیفا…</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/persiana_Soccer/22776" target="_blank">📅 18:57 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22775">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sYhgSWP67-ooPb-5EX-ryYxheTgvLLbUfmtWFQ8S2t0uMABwvH3H3brWwvJOum9QiXjzGcgTTz-VZsfkj139Jm5n0DpZLmrjuH_foiOCPOk8eD6cM16L9A7u3TSUl1qzlzoP-1ph-oZGPaZIPO-XEsxtk90YeXv3D-YMA8ZfS96DgpIK-OP9hoqDyn3pD0jqSV20fryqTcKSAQzynYzlb9MA8m5PQBR0_YM5ScdzDbRv4o3PNL-d1tcONc3E0JWd2ajwrqN8pO2vTe8Rk_z3Vz0YaZVbh2b1zAh3gpoUDhiPJ2wtgBmGmxuwWNoyF8TDuis0gC5cixqj69BRaZS6bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#تکمیلی؛ اسکای اسپورت: ریکاردو کالافیوری درلیست خرید مورینیو و فلورنتینو پرز قرار داره و حتی مستقیما با او حرف زده و به زودی پروژه عقد قرارداد باستاره‌ایتالیایی آرسنال کلید خواهد خورد. کالافیوری خودش برای پیوستن به رئال اوکی داده.
‼️
پس تا حالا لیست بازیکنان…</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/persiana_Soccer/22775" target="_blank">📅 18:45 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22774">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EP6oYD0mNpkCzSQPLwhcEPUjsyNk8DtZEJSR_Zpbez5zEQkaE-q778JVUPsE76G4r5grNJ5pGE1uut1S8AbRw4Sbc5M8BWbuz9LAO1cwKwiktRqTjpXfVVJe_SE06Qc1uraL-hIucbEOq1xRH4ftcDgbhGNg9hgFGQdH5j6LaIm_Hwv2cxVP8edzKGujqa1PXtQxJDOjN5Rnv9TXQz6LsApz5XLsQAOdBof0YxPX9cLLurQBzLCPh6UVFC_PrYg63TRpdBJ9qtxim2oRRLw55ADQWSlmcBwMWr0SvjtRZrf_Q2sB5TMKrhXz_1q1Hk2AXT4g6PpRtzFCNF8rD12npQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ انریکه ریکلمه: درقرارداد ارلینگ هالند با منچستر سیتی بند فسخی وجود داره که بلافاصله بعداز انتخاب‌شدنم‌بعنوان رئیس باشگاه اون رو فعال میکنم. به تموم‌رئالی‌ها قول میدم رئیس بشم هالند و رودری دوستاره سیتی روبلافاصله رئالی خواهم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/persiana_Soccer/22774" target="_blank">📅 18:45 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22772">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c00997812.mp4?token=agHzbMXB12kvAUPbzKiCva448harSzDWelxfb8-bK8y03GAmHw_VCUzy9selAJZTuqBwQeh_O3zsvh_38LU0fzehJUoejYfxSLn_aUaUOZglIpcU6x4mCF7BTlQWgGtgWNVWfzQgD1sF-VKIvogw_WUiIFhESaM1ZiCQ8gkUQQbcfNM4vq_CH-JvQgmZLaTs59cmGw_NebFw9HOcy8EAyjbSsINHd-FAsbGmTjqz8o78h6prab2wJ2YFMLWiNxbzpAI7JPCTQdciHh-xEicBhJjdaCsZZ7VeA6O_0Qq53DseZ_oiHwymrWa2Pxd-tWA_UO-IGAcCzEMvyUaFHb1tWWEjzHkkUdQC6nJiExY8lSIg_XakAiTh3KeCbNbbh7NJGvQGX3Vu04LeDEAG_yXEgD93tDUXxsmvuA5FDoN8uP6RmVdipWeaKMQHG_3mDezBGYNLH8Krf17FLAZAtJJielKqrZnIvkSeYFWrFaoDVxYpW-QrNekh_qxVe3ur9tcn7CkpmVNMNTA-iBsjot8QD0YM57iWwrcu7yOZzVMehsk1KkV0diP_rJ2YkwYqP0hK1BUT3oz7m-nj_uc7V13aEAitGs00VLbFPH9iDdwMpgExOcIY9ShYC6ergdoMFnMAE08TxwThka5Xl2WBj-Ebk7og_Pmp5XBymyHHZXCcpWE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c00997812.mp4?token=agHzbMXB12kvAUPbzKiCva448harSzDWelxfb8-bK8y03GAmHw_VCUzy9selAJZTuqBwQeh_O3zsvh_38LU0fzehJUoejYfxSLn_aUaUOZglIpcU6x4mCF7BTlQWgGtgWNVWfzQgD1sF-VKIvogw_WUiIFhESaM1ZiCQ8gkUQQbcfNM4vq_CH-JvQgmZLaTs59cmGw_NebFw9HOcy8EAyjbSsINHd-FAsbGmTjqz8o78h6prab2wJ2YFMLWiNxbzpAI7JPCTQdciHh-xEicBhJjdaCsZZ7VeA6O_0Qq53DseZ_oiHwymrWa2Pxd-tWA_UO-IGAcCzEMvyUaFHb1tWWEjzHkkUdQC6nJiExY8lSIg_XakAiTh3KeCbNbbh7NJGvQGX3Vu04LeDEAG_yXEgD93tDUXxsmvuA5FDoN8uP6RmVdipWeaKMQHG_3mDezBGYNLH8Krf17FLAZAtJJielKqrZnIvkSeYFWrFaoDVxYpW-QrNekh_qxVe3ur9tcn7CkpmVNMNTA-iBsjot8QD0YM57iWwrcu7yOZzVMehsk1KkV0diP_rJ2YkwYqP0hK1BUT3oz7m-nj_uc7V13aEAitGs00VLbFPH9iDdwMpgExOcIY9ShYC6ergdoMFnMAE08TxwThka5Xl2WBj-Ebk7og_Pmp5XBymyHHZXCcpWE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇹🇷
ترکیه پس از ۲۴ سال بار دیگر به جام جهانی باز می‌گردد؛ تیمی‌که با تکیه بر نسل جدیدی از بازیکنان مستعد، از جمله نان ییلدیز یووه و آردا گولر، هافبک رئال مادرید و با خاطره شیرین صعود به نیمه‌نهایی جام جهانی ۲۰۰۲، وارد این رقابت‌ها می‌شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/persiana_Soccer/22772" target="_blank">📅 17:36 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22771">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sg-1l6CEytyHyNN71VLxNJOhVk_Q15c2nKy7gRtrwqvwKWgfFankyyc0-jkhfKGKROXsbonzj-_O_VpR6Kx_vPQd-XHgSDzjSgR9sVsK7yJivXA8VxrEZrn8Xqjf9k0q3Co5arWDqhmXIOYTd-op0pFVv2MuRIx_J6ec6Kd0P9RarNg0GEHPFhckh9rBGN95ifz9pPCFuQW8-4z4SJi4q6WFbaBNHIs0nhqBLFjZsBXXdlqgzM2RUhSUvTwtkcW9KlT7fXArOjpP3aOf6bdg68biOWR9LMZBfPvgkPps2z5Kdj7ol5Jd1jn77J3HwE5BU6G3stTchB2yHhNpdm8Juw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#نقل‌وانتقالات|با اعلام رومانو؛ دوشان ولاهوویچ از باشگاه یوونتوس جدا شد و قراردادش تمدید نشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/persiana_Soccer/22771" target="_blank">📅 17:18 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22770">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10d92766a1.mp4?token=GZYqHGgfyjT5KUuW-RrDN0DlNvxZXFRoxwMA73gHdDRJ_fgCi8LdV86QM3ymUVrqT3tfV-kj4nEE1Jw0IWEdKACKBnVJ8XwCooW8Wo-S14pe6M73J4Zz0nQrRpyi4HG8sGkh_8kSVm8JTwb9u3lkctwPV5a12KbqVjLRnktiSANwW8rRTMlQ9cQkgBFE5tGOsB0U7vNhnwVBq1M47lvbh7V6gW95D-XlYVTrdBye1AJFymrxh5d60W4n3pXJunGLXPBK5NDj_DjA8LHJBdQpErZ-5mPNEuIMOltYi2zjge5qEkunW8w_N8iVgnB00G_2wbTDFkkMGF3V1fMR-b_cyaUh4OFYUG6M0LeIHgfCMXhk4yVmmCcwc3baUbfSj_JyyV8zjHg9WEEjaimSiifVSZg3f6yF1LJzZp7l2oKfcBDWnVRBBIhbZWySTdarSjyQg1Wy3j9CZ10EDt9bC64nZRiB19WRXvoO1sniFzNrKBd42_36pdxlYXdf_dvnc-UgbfGI0n3_8q7zSi6egb29Xo6GFp44us2MrqTILI5DZ7tiUWRb39WDWxVJEZHJNpcCw0_BO0rz54II7bmM0eu9dBksKyFNyRbzuJE2cBENjhVE28na4pDeTgGTqnd5dX59VO7acEJ4WL7YWDG8MVB3ZzPahxn1hZyqjCGgwjMbgxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10d92766a1.mp4?token=GZYqHGgfyjT5KUuW-RrDN0DlNvxZXFRoxwMA73gHdDRJ_fgCi8LdV86QM3ymUVrqT3tfV-kj4nEE1Jw0IWEdKACKBnVJ8XwCooW8Wo-S14pe6M73J4Zz0nQrRpyi4HG8sGkh_8kSVm8JTwb9u3lkctwPV5a12KbqVjLRnktiSANwW8rRTMlQ9cQkgBFE5tGOsB0U7vNhnwVBq1M47lvbh7V6gW95D-XlYVTrdBye1AJFymrxh5d60W4n3pXJunGLXPBK5NDj_DjA8LHJBdQpErZ-5mPNEuIMOltYi2zjge5qEkunW8w_N8iVgnB00G_2wbTDFkkMGF3V1fMR-b_cyaUh4OFYUG6M0LeIHgfCMXhk4yVmmCcwc3baUbfSj_JyyV8zjHg9WEEjaimSiifVSZg3f6yF1LJzZp7l2oKfcBDWnVRBBIhbZWySTdarSjyQg1Wy3j9CZ10EDt9bC64nZRiB19WRXvoO1sniFzNrKBd42_36pdxlYXdf_dvnc-UgbfGI0n3_8q7zSi6egb29Xo6GFp44us2MrqTILI5DZ7tiUWRb39WDWxVJEZHJNpcCw0_BO0rz54II7bmM0eu9dBksKyFNyRbzuJE2cBENjhVE28na4pDeTgGTqnd5dX59VO7acEJ4WL7YWDG8MVB3ZzPahxn1hZyqjCGgwjMbgxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
مهدی تاتار سرمربی گل‌گهرسیرجان از طریق دوستان نزدیک‌خود درباشگاه پرسپولیس اعلام کرده درصورتی‌که اوسمار ویرا از این تیم جدا شود حاضر است از گل‌گهرجداشود و راهی تیم محبوبش شود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/persiana_Soccer/22770" target="_blank">📅 17:03 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22769">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IUvYi4GLosG1CqM4DVJV2UdTs_TYNtO4BUb0y9XbjFV4M_uhnw2xg7kONa1i6T_GZFhStLUBsikK4jRgW2nfvODjDos_C6rcSWm5Q6WAo97GAcd4cJdUFaEwfuPWPriHqrrxzq_AdlS4Odnltjkp9xpetMTwD4sMhwKhLiEzv19J00-3TVCOltemTsOV2Q-2fiPgEtlB_Sx02EXhxAG891p6YS6Z0MyxIs63yVS-512y7xnQpmRoNibu6-qVIWAbS3r9I010keogobSwg1wxQYvDoHlRCntbM4DniGWhi1Z_2n36esrxJ9iEvtiR0euLmpz-_IHV9NLo1yVp36KvNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خلاصه‌اخبارتکنولوژی‌منطقه؛افغانستان: اینترنت 5G تست و راه‌اندازی‌شد. عراق: تلگرام رفع فیلتر شد. سوریه: سوییفت،ویزا و مستر به سوریه آمدند. ایران: رکوردشکنی جدید قطعی اینترنت به یازدهمین هفته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/persiana_Soccer/22769" target="_blank">📅 16:58 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22768">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a3R-qMx4TP8YNN_4G-2wG9tvWjp5BkxjNwQJknHAtpHjLDH4DTg0M9DNs8IDQm8PgFa2mV8_laSutfe9c0A5h9pwhdjRFsjY3VgJXiA7YxWpAXm6gNe5FA_4mgnOm7VtdpeObc9S6L8kTkNf9UlJp7At1fxZF9WpeqpUL76M53NX5cfbQ96hMw0Ply28chw-0mruQLIMsr45ezn6PgiLutvJHnkzXoy3wnZcAkWoyVzW-7MqCMmiBQKetm-Z5oIHXhBbqVL7a9PhnsmmdQMxN8xaeLlh1NV2oN8bPZe5Jon1qKE5xvYeRW5JYvpPGPUXFPnPGEsKUoSnJ5xVmq65LA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
یاسر آسانی ستاره‌آلبانیایی 30 ساله استقلال شب گذشته بدلیل‌عدم‌پرداخت‌حدود 3 ماه مطالباتش به‌باشگاه خود نویس ارسال کرد. هلدینگ قول داده تا 72 ساعت آینده 250  هزار دلار به او پرداخت کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/persiana_Soccer/22768" target="_blank">📅 16:37 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22767">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RYK7eQHI_fOmnVrJZp_hoHjDYKuzsYATm4WSvsq2QnZYm4-g4uN5nors6kf1EYIptiDQfmw76cYm_YvLiSOi_rXO68qXBcQPtr11EZ6f_9DgqB59LlJp_zZuvP50EUyywoXzN9JOdakjxu-bFzmh0ieNKpcY67Lh4t5KeMYT935i0A26Ts-9lpeg5HfYWGDkebBTPY8NjEIE4PXoEsk01PcI6yIbSCOOhsT--Iu12eU_o_10m1DD79GqyAfEz-KCcAt6OPP_7UcO2F9Akn8p9GJsyCssaUbImc48oLHjp9dOyBIJxSRPL1qbHkjJMMQRY2BiHPAgxS4OKXdPoX6YSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#فوری؛ نماینده اوسمارویرا در گفتگویی کوتاه با رسانه پرشیانا اعلام‌کردکه اوسمار علاقمند به ادامه‌حضور درباشگاه پرسپولیس است و حتی لیست بازیکنان مدنظر خود رانیز به‌مدیریت داده و اگر اتفاق خاصی از طرف‌مالکان باشگاه رخ ندهد او فصل اینده روی نیمکت سرخپوشان پایتخت…</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/persiana_Soccer/22767" target="_blank">📅 15:53 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22766">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LiiR8as0AqgKmd_x9Ka2QXGdJIFnwd2puIfIkbhelSRDJ0khGlqLJYxVsgJaLYxihFu_q0NiVjTg0mFFaGCv2-J2cBeo4d5ezaEt3PTMfB1PffPBoiHF-jMCPXpGtTXl6Z7tfNwkkqyX6KmYFdO_zEGa7mpq9xXG48eggWq-feXQcJBRw2VCJ44g_mx0ktaB0Y6-16dNmhFM_A44wOaVIsKV_KnxoMI3f08LJD9Bf4op0xlRKOld_9qX7l1M38ogk7uMugCjey1HPwZGEzhgKDxkbJGK9eFOqwQN6jBWBUhGHvO4-tkwPXpwFudKu92t1jdMbSBbFAhzuQ6bgBzmYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
علاوه‌برجذب‌قطعی‌کوناته و دامفریس؛ ژائو نوس ستاره پاریسن ژرمن و یوشکو گواردیول ستاره خط دفاعی منچستر سیتی دو بازیکن دیگری هستند که هفته آینده فلورنتینو پرز بعدانتخاب‌شدن بعنوان ریاست باشگاه به تیم رئال مادرید خواهد آورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/persiana_Soccer/22766" target="_blank">📅 15:33 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22765">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🔵
مسابقه جالب بین کیلیان امباپه و نیمار جونیور زمانی که هردو در پاری سن ژرمن حضور داشتند‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/persiana_Soccer/22765" target="_blank">📅 15:18 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22764">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r38BLb7cBopViLCo2PvD1G4FHRkiYuIS11t4q1sSEbaD3a_scVseRrmcN2E6c6ywRGm8CDiauMGjexbz3XeplQFLjRWcOlcJo7nCM9PJgRJrs4zE6uHSHYDDoAAnDMKvsV3fNQSEhE1GQiJPyLopkqrraSp6JPXzMIciEtL65tu_6nvwJgjiKQzzDhP5UGZKcJ-10zp8aYzxx8S_za-wpng7tDeyPAyEBDgeKGLK7LjAi1gRjVfAqvMGHWLr-ADuPgxaRjuPZWkRj0vdttDRWWAPktUT1xYLq5JlihZ-1sfnxTt6XgWGV2OfwlMcIh3Vwi7KF754n4oxJBZMeQkCSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#فوری؛فابریزیو رومانو درلایو اینستاگرامی خود: مایکل اولیسه ستاره فرانسوی بایرن دیگر هدف اصلی پرز برای تقویت خط حمله رئال مادرید است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/persiana_Soccer/22764" target="_blank">📅 15:07 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22763">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W4Me3FIHWLCDWwH2cpJTJy9SikO5grESiFEEJjk2y9AcRzcCkzXtL7N1vIsgnoUMLnz-AN0jKBsvbKRNxri2-UYVc6xw9pW36anOqJZh_Hmw8Nx0_YLmbCaUSWbddnx3RjUGyMogMhei13Fh9z4toNUfC7OV9-4N68uGj1pPWTMCnU1gEKFnurJ5q47XaD2NQhMhYKk7oHDITuE1czO78K6D55PcWY--FVklQucFgc4j1T6P_P_QaMs7AdOs4T4jepwaQS0QbkrZ6jqv86RttgOCrBn9P8agpZQaqjYeUZP3x1d9cMdZroN6aEILwp1TnlT7slTwoFO_FT_RluytiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
این چهره که زندگیِ سرشار از خوشبختی‌اش رو درکنار زن و بچه‌ش مشاهده می‌کنید، همین چند روز پیش برای دومین فصل متوالی تیمش قهرمان اروپا شد و خودشم یکی از بهترین فوتبالیست‌های جهانه. عامل موفقیتش هم نه مربیش بوده و نه همسرش، بلکه فتحعلی‌شاه بود با تصویب عهدنامه گلستان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/persiana_Soccer/22763" target="_blank">📅 14:55 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22762">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f4RBFxrxdioC91pZYOdv5WvZwlZAIIRxrX3j4SxeDYMtZOc_z3WFKCxvpcYx6wQ-gL9z2xf2b3xrpQzXwi040pF1KUwceSgPwmWaMze3rCneyU1pkX4VlC0zPsurUEqXjIib1gHQEMXI49_t8hAu0Mj2SirXus1sZCgHSw04vSOn-HWh6S8QUf_0Sor4wld1doVuSRlyGwyRGOAxr4ApjkMX8mxRNPLp9XvtnFmD7lXXg2O6B2ohENVFoChQhqAqh0sH4NnvjGSlCqBInjzpAzwm56250Ltgm1z1lAWzUeONfYMtT5rVl81_rgdy37spnyL1VSKseptiU-wOfpGYVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
رسانه‌ معتبر اسپورت 4TV کرواسی: دراگان اسکوچیچ سرمربی سابق تراکتور از باشگاه استقلال تهران آفر رسمی دریافت کرده و احتمال بازگشت دوباره او به فوتبال ایران وجود دارد.
‼️
پ.ن: اکثر رسانه‌های‌کرواسی خبراز مذاکرات ابی ها با اسکوچیچ‌ میدهند امارسانه‌های حکومتی…</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/persiana_Soccer/22762" target="_blank">📅 14:47 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22761">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t1xqI_f2HPOR8h7qJiRHmXL51BlXf64zUHW3ykNxkDHJgAHlvxVIa2Fq30cmFrWt8Xr7feJmpG_6KH_qy9kf1-eYSfeS2pncHboC1CcXI-krHT95J86rCa7lX0s8J2EdlQiKjhNWjhwgjTTB0zYdatv1pG2zDiICsNLkgYOS-Ci5hJ6k5swFr5MKNPKyTSj7i3w03UImxyh2Id4dcYekmmK0It2lnHtTKCvOFTgCQ_1U96agkdR6SNRrWKoyz1DHTj6-kTwFrBw27ZWro_tp2v44Vv4QzSZGtAfZTClluBwUETLKTQl4ri-yf7zaAVkBVIW5LpJOd6W9wK6CKPSBCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#اختصاصی_پرشیانا #فوری؛ دراگان اسکوچیچ سرمربی‌کروات، موفق‌وسابق‌تراکتور از طریق ایجنت ایرانی نزدیک‌به‌خودگفته درصورتیکه تکلیف مذاکرات جمهوری اسلامی با آمریکامشخص‌شود و دیگر جنگی رخ ندهد به قطعا لیگ برتر باز خواهد گشت و به آفر مدیران باشگاه استقلال پاسخ مثبت…</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/persiana_Soccer/22761" target="_blank">📅 13:36 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22760">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VkJLEfYzt5yee9JJEPHdV85sjqy2isq80k-YfudPR5zPdTtDDzRh5gvdHaXsdlADLzoo3vZoINlA0yfcYReQ0eFIJrCexihnOlj2JP0sAZpFpo6Wlih7QGZ9HN9Ui--OyJwjzBjBfL_DW68JyOZ2UawlRLKj6C3Xs4BsDCFyOID1Dq3pvkSKw0wYR1Gxakpg39Svh7ySCfoka4_7QLfZMVW42mb4ILNmHFqjqnXgmRRBpZDrC8T-yWWEO21bVzz6KTojmLokWxkvZjFElgVmXYGXfMTuIsHsq6apWSLIs6AJyA_VatJ0Z0Ik4KjsoybI14GCKM6f2qqWpZYjoImPGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#تکمیلی؛ اسکای اسپورت: ریکاردو کالافیوری درلیست خرید مورینیو و فلورنتینو پرز قرار داره و حتی مستقیما با او حرف زده و به زودی پروژه عقد قرارداد باستاره‌ایتالیایی آرسنال کلید خواهد خورد. کالافیوری خودش برای پیوستن به رئال اوکی داده.
‼️
پس تا حالا لیست بازیکنان…</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/persiana_Soccer/22760" target="_blank">📅 12:53 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22759">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KyX1997V1vvqcPSIthbjG0_JbawS7TPct_ZzfzM1b4uGKLAKADQiUSzXXqFw4_O4vc0QDVmxaHqtD7yx5zcagTcrEVOjvE90KjNwv346xusOIX2PU8zotHcoNsJPzGZeSPX_V5igxqDbxKXpNLUraA_1hsyV7eIx9e10r09eRYJHuGlGAXXbB51Ipoj-barP5GroIufQ4iEKP3iNcPHfbyeda1b5Sw_wC4aCJyl5dcFyItUQc9983csF6nV9PAdsWbsoEbPVJALJTvVRw3yyyDUw-Zdn5HlFhcEYztq9CYLqEkkQT4gVugfOVcZjvu_N_3PLyx668Ntt6Nm3za0h0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
باشگاه‌های رکورددار بیشترین بازیکن در رقابت های جام جهانی؛ منچسترسیتی در صدر جدول.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/persiana_Soccer/22759" target="_blank">📅 12:18 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22758">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee451d1e8a.mp4?token=mmLUyQyEuw960FfR7Fc_BPXVUdjyjmCcf-O6mll-2nYEV5DWy1bA0xMkvKJbaYulBwBA1Kk77tgXBkCvK356g7f5PIY_jmkw0KiL0WeaAUkKzP7D-e6KmK7Le-5zeQDulfziXvpjvMVdYEutc1JUeWALsTDiNGLIEObHYnQDo-Pwop3-7EmPAHOJe4uwlb7_o4jKJAoanYYW1MzEf32PoLX4bRCcQ_umj93JeM9KobTR2O5Q_oWDwWWphK-GH0JmJQ4s0MB5Dwy6T6NaoTiaYkNOc92AJsSJgMzruBFiTRMd8Rap2zaJi6scXupRZWqCeKfGULGPhHX-vLuXVPUnuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee451d1e8a.mp4?token=mmLUyQyEuw960FfR7Fc_BPXVUdjyjmCcf-O6mll-2nYEV5DWy1bA0xMkvKJbaYulBwBA1Kk77tgXBkCvK356g7f5PIY_jmkw0KiL0WeaAUkKzP7D-e6KmK7Le-5zeQDulfziXvpjvMVdYEutc1JUeWALsTDiNGLIEObHYnQDo-Pwop3-7EmPAHOJe4uwlb7_o4jKJAoanYYW1MzEf32PoLX4bRCcQ_umj93JeM9KobTR2O5Q_oWDwWWphK-GH0JmJQ4s0MB5Dwy6T6NaoTiaYkNOc92AJsSJgMzruBFiTRMd8Rap2zaJi6scXupRZWqCeKfGULGPhHX-vLuXVPUnuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇪🇸
تعدادی‌ازسوپرگل‌های این فصل آردا گولر در رئال مادرید؛ شلیک۶۸متری آردا گولر مقابل الچه، به عنوان بهترین‌گل‌فصل رقابت‌های لالیگا انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/persiana_Soccer/22758" target="_blank">📅 11:40 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22757">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Id7-6yBK7aQNhZed6_H4PuwCQwmY3eQLc0PGPNuPRvapJTf9vdiGDjJsokFI9hHSDj8j87b6wN-gjir2xT2WoX0RI2CyT9L9N0egS4m2yoIn5H5ITjKIjqyzYC6iAdxv00gpECTpV54qng5IyV9R-2ZL7DR-ECHuW6cQN7OuukqR-x8DpTMlhGwIFsftP4kCmD9Xr4g3X9ZAMbXRIgh-06Omrerern1dzP4SLlVaNXFVzTCxY9WJcctYJ4uW_PCC8_CKCdR2P0xICGoucFehiO9kz__rrYdTETXnyCu-_tpFDOILPUuCq3OYA4K1XOWjPMv0u8npe5BlEfU_BU2KuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بازیکنان رکورددار بیشترین تعداد قهرمانی درپنج لیگ معتبر اروپا؛ رابرت لواندوفسکی در صدر جدول.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/persiana_Soccer/22757" target="_blank">📅 11:25 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22756">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MzHmlw-otrI3AotV99Q5Kr2V47islYfNKoXBsVxN8U46_y925LvU7QUKSQGCCxY6ucBY95Dfd-mdRTVrCsEoJKNkuYnprfcxtg6-QE1x8CzZRFerOpSyhMdvm0FDvLI2b_u8CusNwrAIUmJMTPD1K3g7q8kxUNNSKXeHvn53pg6qN2Nd3HIzB6KCIFvgmrQTWmAeNoCZxgjWZDhrSUtj8UbB3aEx-jDcU7qngx7uI6-fjzjfzamJ_didXYiN6VYZyR4j-6GycmgmymGIpVICIY1Ig_Wc4_UrcUJ_rAu-MLXWD8czhqxJXHdAZ0lbwFwxKIqRPqv_GS275uChdxwf-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
یادآوری
؛شبکه‌های رایگان پخش جذاب مسابقات جام جهانی 2026 که از 21 خرداد استارت میخوره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/persiana_Soccer/22756" target="_blank">📅 10:37 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22755">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PMJwpH_GAJvxEp3fdegEvycQ3XZalskrJFo9muzUNCDpo9yJpuvVhTswWlbKSOPUpSIOxgiEhBnTrMmWL7AaU236aD3TqXG65jWQKC4sQTS9FHyvLZ8tSBHrTwTOFnazP8uvm5Pv2YbfLkwyMiO9h61-bfeqNdVHZEAZduafVJs8N7vs8vcLEE4YMXDfN53T-FXU8cy_VB0Y1tdz5wX-NG5CNQTr8BC6pQm5mbwS0HE7ogojTavzw2EUyR8BR3oowUKs0-JdQCMWkjae8uRv7yyaB9sI9UOaYD2mnFvW9zOAzQCkqiSHEQH2_Byk_Op8dVeyJHZ3ah5PE--pwMDVoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
دانیال ایری مدافع‌میانی‌ذوب‌آهن‌که دو فصل گذشته بعنوان سرباز در ملوان بازی میکرد قراردادش با گاندو ها به پایان‌رسیده و بعداز جام جهانی بعنوان بازیکن آزاد میتواند راهی باشگاه جدیدش شود. ایری هم از استقلال و پرسپولیس پیشنهاد داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/persiana_Soccer/22755" target="_blank">📅 10:32 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22754">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ede7c22d43.mp4?token=HvTliOiTZH-3EJ6HR28ow81Nb15mT8yQSvX0qsS0tlEe3RqoM4GQrmJwDdPHaY-M3EwurQ4u3Nj0IdXPwcy0KzA53YkEzAvxqh5qJniXRawuYJ215AW36RTCkS8NUB_AY_8gn_4HT2rtksSjdYKxCDyOJPsiQZZqlRRJ8fY7FB9gH5SNYC5pi6szqRczqs5IeEvJDXH_i8YqA8rc2P57Gju7ghZmd32y8ijQw41O4-cb8hwPcATiAkeS01xzlRHnChLQoRADNFGBnMUkYOkRlTg2zVncG9ZcA6FGHjXd9ekZiBFWDsxeD-PRpNQceVCg1NYQAnY5GJcdkvrkcT9xLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ede7c22d43.mp4?token=HvTliOiTZH-3EJ6HR28ow81Nb15mT8yQSvX0qsS0tlEe3RqoM4GQrmJwDdPHaY-M3EwurQ4u3Nj0IdXPwcy0KzA53YkEzAvxqh5qJniXRawuYJ215AW36RTCkS8NUB_AY_8gn_4HT2rtksSjdYKxCDyOJPsiQZZqlRRJ8fY7FB9gH5SNYC5pi6szqRczqs5IeEvJDXH_i8YqA8rc2P57Gju7ghZmd32y8ijQw41O4-cb8hwPcATiAkeS01xzlRHnChLQoRADNFGBnMUkYOkRlTg2zVncG9ZcA6FGHjXd9ekZiBFWDsxeD-PRpNQceVCg1NYQAnY5GJcdkvrkcT9xLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
تکل‌فوق‌العاده‌مارکینیوش در فینال چمپونزلیگ ونجات PSG؛
ولی‌واقعا برام باورش سخته که فقط 32 سالشه، فکر میکردم نزدیک 15 20 ساله داریم بازیشو میبینیم حداقل‌تو ذهنم 38 39 سالش بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/persiana_Soccer/22754" target="_blank">📅 10:32 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22752">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M69EvWQ-n30Iw2AkPNfUwkt7h6O4S4GWR3atDSqZJJHCOgLtNg5-nQGy-8sk998ZV3Oz9s8AErOPZbJ1LZnATHjb7PjTx7ymVWMO4Lyf8ES6_zY7SPg2pGuWUktl5finhYv__i6Gk6xlPHtyu4h4NVJqtEnavLg988AHG1n_IQ2jlOB7zy2lVfHFATHiedOxhxPeZ5TMkn9QQ37J0TnhIumrcOGYZEh30nZB2IqXi7hFY8FA9-qJTFEQBh9-vvfv8Nm54t1px_1a8ucjb-rUIZmQHkPb-JrdIJrEOSM-yO_lPuzRetDdPIh9llHPb9EG-7keRbn66LFygYnjW-pqPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
درسته برزیل از سال ۲۰۰۲ جام جهانی رو نبرده، اما همچنان پادشاهان بی‌چون‌وچرای این مسابقاته و با بیش از ۲۰ امتیاز در صدر جدول کلی قرار داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/persiana_Soccer/22752" target="_blank">📅 09:42 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22751">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kk6ZYyn16siGeSu-FgmjHMo3v5ypPRJUeLn2V9K1eREqUufqK_dZ75C-YsfHWyIroSSZXk4EtSkhAvQDsnAynG1U_BUOnxBzgns42x-uMX3e7FPXIt1OUh9hZsMjuQJn_3TvhLdjzqg4mnKPlAPBH_UB7KFh77Oi003UHUka-F7i17hsrcgMJs4V1KZAFf6hoYkVtqJ1N7P00j8TaweHzrG7Ule-i7dC9qPblMQigZAJ8BaFqpA0bzgGcfaeVnF9RRY9dB5sDPYJKknF7MPgdNP5aixOxrRPRnW4ePKW4MwEANWwuisBu_LEUTo2y3dJHWOLDpBzdYCUXGDQTzAJYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
جوان‌ترین سرمربیان جام جهانی 2026
؛ یولین ناگلزمن آلمانی‌ها با 38 سال سن جوان‌ترین سرمربی حاضر در رقابت‌های جام جهانی 2026 خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/persiana_Soccer/22751" target="_blank">📅 09:25 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22750">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/txEo1OLVeyxowrcE2v11kGyKPFpJ63jX-kZkDuA0wugZperVJrXuuF5aACs-FVEVCPcGYL6SwpX8i2tO2JJhGfkkPP1VG6prljgWWW1IILMxWppcBidfAAQUEQO5i26-AE4a8Fw4C4LSJnOlS7G2LuYf01wb6EQ5Pyo8om_u7O3RV2H6fh4fBpP_hIVjep48wuk5Kk5lxIUVms6MMUgc2HhcfDs1zAKazKLevIRf__NQOS9u_vmgPTba0PeHmF6AJuLCjz52Tl3Va-VrblDNm8UK8SOlkSMi1SUkyYu7vvZD5nD76Ti0u1ZonpetE4rwkFVOQH1bGabQ_AQ57QU0Cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
درخصوص نحو سرچ فرکانس شبکه‌های رایگان ماهواره یاهست‌سوال‌زیاد پرسیدین. روپست ریپلای شده کامل ویدیونحو سرچ فرکانس شبکه مدنظر رو توضیح‌دادیم. الان‌این ماهواره‌خودمه شبکه‌ها سرچ‌ کردم مرتب پشت سر هم قرار دادم که هرکدوم رو خواستم سریع پیدا بشه. تموم این شبکه‌ها…</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/persiana_Soccer/22750" target="_blank">📅 09:10 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22749">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u4KPIsJ0HZwHolXHs-DuS1yuC7oXt6uLvmq9DO5u8TVz6etDjqj0KsYG_Jcb786ruaj1p0HcEKBt8XysubY8_26KVeHiCCKmCRgLyqmM2GtK3dXIorfqUFPlG9kVPhi0vXXSJUCUx8VheWJOW2WMzzq7vRSgKaTGHbXaRn8x7LJtI3UShGlqMbF4kGBE0eEaNzClbc_POwRtLrOhz9d3OB2YiYIMV5lipe739WZneqOesKT69-odwQIvY6mf7_gVUeyHoQnYoSL_LwmA8r8fQceZfSMXk20iG1E9m63Ft6OhI4eTygr6o5V6VPtwzw0C4_v2E2KvSLh9VbHvJ5ar5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
فابریزیو رومانو: رئال‌مادرید مستقیما به ریکارو کالافیوری مدافع‌چپ خوش‌اتیه آرسنال تماس گرفته و میخواد این‌بازیکن‌ رو بدرخواست ژوزه مورینیو به خدمت بگیره. احتمال این انتقال‌جذاب‌بسیار بالاست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/persiana_Soccer/22749" target="_blank">📅 02:04 · 14 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
