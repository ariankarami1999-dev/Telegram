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
<img src="https://cdn4.telesco.pe/file/Zyer4a-2Cuf_h8g8IjaffaC5ParuhVPWy37Mb2vsDloB0129KTHzWkp6W229B_QZ-xABRzNiGM_tqbLrtPGDKDxmmvP-oEOpHcwnvL3eA-GSNDrSlHINME1clv1baV0adEXSeCganbWG4zgIaO6W1yLb9_2snQTgFjLnFZR7trgEBb36lwf3Vo-OOl8F26tujml5x0gVr6uBweXIhyLSpu5o8tqEUI63i91V092qK6MZ6CuMY_vqDM4Gc7qnXfdHZr9D1PwNcjrr3MD9yILU7Lf8x4lPnU65qPeZMWuIaM3NH9Z40KQ4C1Ncv_gOU0Bsg1ZKL_HZruLbtzjm1pMhWg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 61.2K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-06 02:32:37</div>
<hr>

<div class="tg-post" id="msg-5156">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pw8hCPlWTLHpgVMfZiKHgPIugUEQ7gyIQZP9xgqu3GSnT_ZgmoxCsR1lMDwVlNC0lAKNvZKCw5AxurK9GkjWsuDJaFrrO_CwSBBBp98NLX2uLOmLGBjCNdkaqLQzpTOzoYIWRtrdCNHSKR1miGBK1tE8GHRxj3aT_jxxeWPwpBD8chi4L3lXmeifV2QyLiKnv7PB-PZbKg91dZEZ0kro0irSzQ0YSYVIEV75S2iSOICee3XcU4FDR7weDIusxFJiYOCdFbFu3bSpKjoPI1Bk1CiNSauc_iWSXnGfaVYipdKWbJ4GscM8fBGD-MxBjmXEf4N_hNT9CVHYTCv3k0Fqjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صدا و سیما دیشب بعد از انتشار خبر شنیده شدن صدای انفجار گزارشی تهیه کرد و گفت : منبع صداها مشخص نیست!
بعد صابرین‌نیوز و خبرگزاری دانشجو و… حتی اسامی کشته‌ها رو منتشر کردن
بعد سخنگوی سنتکام رسما گفت حمله کردیم و زدیم و…!
دیگه صدا و سیما در همون مرحله « منبع صداها مشخص‌ نیست» موند که موند و داستان رو ادامه نداد .
«مصلحت» نبود!</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/farahmand_alipour/5156" target="_blank">📅 23:18 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5155">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8fbae4d271.mp4?token=vqQkQbRKBzyKIrOptxlg8x5bfZIPaO2dePmNO33l2KtkgJ_0wEl0aFCxTZmS8nkWBiqkVjKhLCM0hrsUzX07w1z80IbO8HJOFeKUtqomywRHbK4d0qYACNl6RRCFsfL1fJhIW_qz81YEz5SYLjYG4Kh8v6zUpCktmTJwnhyB7l3E-29gvvEajTwyACc-AtbZOMyO3iXTcfEziEPxxaB_rnfw1ThwdGKbWSH8ZiNOcrDzFQMOx05KhakHb4j64_lS4lfkWVxA-PSvjF4wrICWZBTbDpuuckA4YcIUnnwwyCyZVKWC8LcxkwW2cwr_-6lI0KVRtY0qTGvSMiqaftmi1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8fbae4d271.mp4?token=vqQkQbRKBzyKIrOptxlg8x5bfZIPaO2dePmNO33l2KtkgJ_0wEl0aFCxTZmS8nkWBiqkVjKhLCM0hrsUzX07w1z80IbO8HJOFeKUtqomywRHbK4d0qYACNl6RRCFsfL1fJhIW_qz81YEz5SYLjYG4Kh8v6zUpCktmTJwnhyB7l3E-29gvvEajTwyACc-AtbZOMyO3iXTcfEziEPxxaB_rnfw1ThwdGKbWSH8ZiNOcrDzFQMOx05KhakHb4j64_lS4lfkWVxA-PSvjF4wrICWZBTbDpuuckA4YcIUnnwwyCyZVKWC8LcxkwW2cwr_-6lI0KVRtY0qTGvSMiqaftmi1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">علیرضا دبیر: کارمندان بهایی من‌وتو می‌تونن
در صورت بیکاری، تو پارک دانشجو مشغول کار بشن
مدیرِ تراز جمهوری اسلامی</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/farahmand_alipour/5155" target="_blank">📅 22:26 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5154">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B4sHPwwOvyMv33b3BylQkZ-NSbFsrWcpag9qOp2Ya3a4t9h_56mQjNZbE9WPTDLA0xixYR440pSRLwE_W8ShNn4eBMWI-8xaYa1SpgGVLMmhtZ9zW-nuoVcp_o8JvuMe6elpBiFIjE4QlrzyO5oN736iC8p_s1PvOE4DzObYrmjjx8JXAHoT24_aQ5U-pC50BcjFprKsKFRUytTu5RqPadEnaX_yrYXzXEsKGUhMFsDfN1y4Npvg40_JSfRF3PIcsgq6TxVZlPS9fTjf0JwrApGzgUfaY_YKQSk_PXvtvpL_hfMR42N5X92p4D06xxmJmE1NInpKOsxpJAsnJ6E8Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاریکاتور شارلی ابدو
از قصد جمهوری اسلامی برای گرفتن پول برای عبور کشتی‌ها از تنگه هرمز.
آخوندی که میگه : به نظرت
چقدر کاغذ توالت بهمون میرسه؟
اشاره به پول ایران و بی‌ارزش بودن
ریال ایران که ارزشش در حد کاغذ توالته.</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/5154" target="_blank">📅 20:07 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5153">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">‏پیام منتسب به مجتبی خامنه‌ای به مناسبت حج: رژیم منحوس صهیونی ۱۵ سال آینده را نخواهد دید.
باعشه!
بابات هم همین‌ها رو میگفت که باعث شد امروز ۹۰ روزه که معلوم‌ نیست هستی یا نیستی، اگه هم هستی طوری قایم شدی که گویی هرگز نبوده‌‌ای :)</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5153" target="_blank">📅 14:43 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5152">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N_CHL9RBiYyq9HxC_sWmthysfmbb5B-5OrCDN9OICEHUtJtH4UhkWEMPQp4DLV1F7X02ywjdNJGBqmVF4FmJgXGBRKr4_pnMxAlXPs8zswKgRc1anLHmKj8o-iLWWwNHIa_Yblv0w_kQMUZk3dJ4muwk8e9FgsaxlVUSYVlNFSgSPA2DsW53UsAh8-MdcY3_asLX_EHU-9N_bcV_KQu9pPC156VfyP-CyGiCDsTXR0h5W2hvO2BgPzvAP2JP1mt220VmABlMvter9ERG4m3rCyVcwOkqXzv-GSB3tVGVPauscq9_Pp855fvOm0ha4fBKIq-DYqePOEwssVF_IetiXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ذوالقدر دبیر شورای عالی امنیت ملی، میدان جدید رو معرفی کرده که هیچ کس نباید حرفی بزنه که وحدت شکن باشه!
دستور خفه شدن همگانی تا رسیدن به پیروزی!
اسمی هم از مجتبی خامنه‌ای نیست.</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/5152" target="_blank">📅 05:23 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5151">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N7ZbrHhWNkF6asaI_zZ0DZSVagMP0Sj1brzG9CMPzGcZvW3XpWVecnn9714yNRz7_Gj812RfCOZRs2A6u36z5kVK681YWdx1mpQXmDg7KxntxxYCwpdg2TEHLRm_iYWeaR4IgoY8igu48lrD7qmS3uORuT2an-J6XmmJxpeevTTaHKOIlbaE6G_Wwd5MAT5PRdX1T8dWSBXg4VcD38MTZmemcPd9yDI3r0hV0iKx37RRrxiGgikGQ7EcDAH9B0uH7tApvHaCncXJjbUY_rOs78UhjdP6PQXuBz1szf8zOA7691l2VYNkxrXc9XIFPi-NgDCm6On4gedIyXr-71KiOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
ارتش آمریکا حملاتی در جنوب ایران انجام داد / کشته شدن چند نیروی سپاه.   سخنگوی سنتکام رسما اعلام کرد که جنگنده‌های آمریکایی به چند سایت موشکی و دو قایق که مشغول مین‌ریزی بودند، در اطراف بندرعباس، حمله کرده است. خبرگزاری دانشجو، وابسته به بسیج، تعداد کشته‌ها…</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5151" target="_blank">📅 04:57 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5150">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qf7UsMUanr0Aa1Cp5FM1MLqh4WZJe8WqmC5JjLJctb8TzWdg72V7ELk-TNlaAvCYEilxd0GF33n9lyKC8mYLTM_65YUMxi5pWuGLSgo979GvU9_oCtSx9mWutlgxkiYIM-xA0PRXmBtemCgdx7Wur_Y8RBdKYbvGRJeZ7m_eg3Adl3fAV6gN8yrACDMw7llkqXbE0I7opj6DCL3I7eFA8E342pDltsEfZGC5Tg9JGHFfwkLY_ZvxcvaahE3oNdblKqxil5uj9LjJztBrV-bUlEjVSNNriU1z76VdrTL-d1mlcNWmpgBk_f-l-OKRdWTOl_Wl8xS4C0GZyPYUs4YagA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
ارتش آمریکا حملاتی در جنوب ایران انجام داد / کشته شدن چند نیروی سپاه
.
سخنگوی سنتکام رسما اعلام کرد که جنگنده‌های آمریکایی به چند سایت موشکی و دو قایق که مشغول مین‌ریزی بودند، در اطراف بندرعباس، حمله کرده است.
خبرگزاری دانشجو، وابسته به بسیج، تعداد کشته‌ها را نامشخص اعلام کرده اما اسامی سه تن  را نوشته.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5150" target="_blank">📅 04:50 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5149">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">ترامپ : یا یک توافق عالی برای همه خواهد بود یا هیچ توافقی نخواهد بود.
اگر توافقی نباشد آمریکا به جنگ بازمیگردد.
کشورهای منطقه باید عضو پیمان ابراهیم شوند.</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5149" target="_blank">📅 17:30 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5148">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">قیمت نفت : ۹۷ دلار</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/5148" target="_blank">📅 14:48 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5147">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GXPqqXk2dKQDnL13zNIt75kjiWPcxCnQkbopGx8QMWWVn1MYPamt2AYBBfE3XRBxl_UkAFavsSv084txQX--vD5bRa5y53e_S5nm6KIggN2-R2Mylxf1TSoOzlH2Y_yNzCBw-ohhVHXsy58xwKdRas-2PGUwPhiKvJxcIkIAb6i3PwC_043IVknCdcrB4IJZ9K-1JChqKKuF98ZwXYllo3IBnliki3aYGO4-yTl9v77TPwDWforuu2M0UyQliqMym2xtQpSDX4i0YfRqJS7kDD5uKQuaXryZ2pUP2IAS5JTTcVHUV2Wi8fLrxsuH7o4tWSuNJLloO4mPxBpDrjgmrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در حالی که صدا و سیما شیپور پیروزی میزنه و از موافقت آمریکا با هر ده پیش شرط جمهوری اسلامی میگه،
سخنگوی وزارت خارجه امروز گفته : کسی نمی‌تواند ادعا بکند به توافق نزدیک شده‌ایم!</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/5147" target="_blank">📅 14:29 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5146">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🔺
بقایی، سخنگوی وزارت خارجه:
آمریکا به عباس عراقچی، ویزا برای حضور در سازمان ملل نداد.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5146" target="_blank">📅 14:16 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5145">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/77b6861470.mp4?token=hA0DP6WpmX9zWpfMU5FkzQosX87obxsJK5LmrXHShXscXVaZAEgJUSES8f-E6JNVYiKGPYNfqmCUKD8XID-Umkg6DbxWJrxIUMH7O8ynSPdDJ9rtIRgKSJPOEAi7wOuMYquzln75FwIlVtHM0QW4e2szcpJkuUgTsFgU2lOxjwp-Y5twwpBSCCygU3To8lsqOneHWWkh6NjsPgO8dbHWHTsF9Z9wlD4UeLIZyJP2uUrsE8W2rGSaOtM7EvhR7ucPGtvFsD9jt9xa9OJ7_YJMeR53xfvlKrPCXSM6YbN5clkNA7SE-fNHetutH9dXSVatqWYfrodRYEYvofZzluqFZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/77b6861470.mp4?token=hA0DP6WpmX9zWpfMU5FkzQosX87obxsJK5LmrXHShXscXVaZAEgJUSES8f-E6JNVYiKGPYNfqmCUKD8XID-Umkg6DbxWJrxIUMH7O8ynSPdDJ9rtIRgKSJPOEAi7wOuMYquzln75FwIlVtHM0QW4e2szcpJkuUgTsFgU2lOxjwp-Y5twwpBSCCygU3To8lsqOneHWWkh6NjsPgO8dbHWHTsF9Z9wlD4UeLIZyJP2uUrsE8W2rGSaOtM7EvhR7ucPGtvFsD9jt9xa9OJ7_YJMeR53xfvlKrPCXSM6YbN5clkNA7SE-fNHetutH9dXSVatqWYfrodRYEYvofZzluqFZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نمایی از شهر رفح در نوار غزه و پیروزی‌های محور مقاومت
قبل و بعد از  حمله تروریستی ۷ اکتبر</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5145" target="_blank">📅 13:46 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5144">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">رئیس ستاد کل ارتش اسرائیل - توی این مایه‌ها -  گفته: «در پاسخ به هر حمله پهپادی انفجاری حزب‌الله، باید یکی از برج‌های بیروت رو هدف قرار بدیم.»
حملات حزب‌الله به اسرائیل رو یا دولت لبنان باید متوقف کنه، یا اسرائیل.</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5144" target="_blank">📅 13:41 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5143">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EgjpUJ_0cwWCdVN3XkpTsBIEueAVGN7ogXtoZo9OzB08jFW7eU9Qx-0-C7Fri8G3JEaX4ptI3aVewv9IpItLgmgbdMXzLYuAJ2TAErLDL0sP1aMh7TN18QvcYqA1ESah-NSbCt1Sd-ErcuikNZKgzr54ej0v0S1jo8L7P2KiNF3x3L15h23hjOD9oxq_WD530siEoj4Siiz2SHqUp8VDRCynlZvwL5YIomUO7vwW7Ekh4O91RdacU9pEJZekYCVylN2Hs4ZBqaoADbEZlb11LOkkr0mbraA-qr3I6a1anf5VOXP4ii3wFRjWCjTxl7AHmXjueTtNT4hiJERsHuLtIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صبح در ایران با اذان و با اعدام جوانانش شروع می‌شود.</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5143" target="_blank">📅 11:58 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5142">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69381f4f87.mp4?token=Szxi_uYPxSaSRsOG8-cTkVqp8QBZK9UWregbHgRmx_49ctAHQoDehOVrjwAgAzNDXGQ8071JaKqelXJofHfoo2lNbG48p-WgSqiWYslD3LDAXqNOjqwzpQVCaruNhmi3E0N1gKI5hBR4_OGyJobO-aVtAhAOxZhY2g0qkcEf70iRG_hclo6arQ3OenHfrXY03sv8xmVQnWDctbI3GqCui597Iv550bcFLYKFWEzqTnFt2MeegOglJ779Ff3VWSToKK0dWxanyi-pmpOrZIUa6w1Ij0Et-SI2tKyJT8-231I89fFCEwpXlUNx66Q4aHeOij3PI_FahnrBZUK742yqKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69381f4f87.mp4?token=Szxi_uYPxSaSRsOG8-cTkVqp8QBZK9UWregbHgRmx_49ctAHQoDehOVrjwAgAzNDXGQ8071JaKqelXJofHfoo2lNbG48p-WgSqiWYslD3LDAXqNOjqwzpQVCaruNhmi3E0N1gKI5hBR4_OGyJobO-aVtAhAOxZhY2g0qkcEf70iRG_hclo6arQ3OenHfrXY03sv8xmVQnWDctbI3GqCui597Iv550bcFLYKFWEzqTnFt2MeegOglJ779Ff3VWSToKK0dWxanyi-pmpOrZIUa6w1Ij0Et-SI2tKyJT8-231I89fFCEwpXlUNx66Q4aHeOij3PI_FahnrBZUK742yqKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برخلاف
گزارش صدا و سیما
۱- بسیار بعیده آمریکا و اسرائیل
به جمهوری اسلامی حق غنی سازی رو بدن،
۲- غیر قابل تصوره که آمریکا
کنترل تنگه هرمز رو در دست سپاه بگذاره و چندین کشور ثروتمند عربی
رو بگذارن گروگان اینها باشن.
مسئله بزرگ‌تر از جمهوری اسلامی است
مسئله سرنوشت منطقه است.
۳- غیر قابل تصوره آمریکا تحریم‌های اولیه
و ثانویه و….. رو برداره و دارایی‌های
مسدود شده رو بهشون بده!
🔺
اما اگه این حرف‌ها ۱٪ درست باشه :
۴- فاصله میان جنگ ۱۲ روزه
تا جنگ ۴۰ روزه حدود ۲۵۰ روز بود.
ترامپ بعد از جنگ ۱۲ روزه گفت بود :
« جنگ تمام شد، ما پیروز شدیم و تهدید
را خنثی کردیم! »
۵- ۱۶۲ روز دیگه در آمریکا انتخابات میان‌دوره‌ای است.
ولی شاید حتی پیش از ۱۶۲ روز دیگر،
جنگ سومی در راه باشد! و شاید پس از انتخابات.(با فرض اینکه حرفهای صدا و سیما درست باشه!)</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5142" target="_blank">📅 11:04 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5141">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">صدا و سیما:  آمریکا با ۱۰ شرط جمهوری اسلامی موافقت کرده   ‏۱. آمریکا متعهد به عدم تجاوز به ایران شده  ‏۲. استمرار کنترل ایران بر تنگه هرمز ‏۳.پذیرش غنی سازی ‏۴.رفع همه تحریم های اولیه  ‏۵.رفع همه تحریم های ثانویه ‏۶.خاتمه تمامی قطعنامه های شورای امنیت  ‏۷.خاتمه…</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5141" target="_blank">📅 09:00 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5140">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6cc885feb3.mp4?token=K7TxQlAiYAeHQ3cm9TEKUm6c7HLzIfQ2MXJHt7ZCSpntMLwEItYhUUwACaKqa-tPpsvMRzWKblJXijm83JxC1eIJ2WUc8hH6rDxMz6ieyKri4A8Sz3v5E4X55J3YrM3D4nUL60Us_Z0OfhUBJmF2cfc0-fM9jqoFZicdr0l1MI9XKCcHAklnGTV9Tv2y0e50iUgAC0WIuf_XN1GrvsXsjdb9aHab7IpC1rw3GN6k5yQFbOmN6ixw9Oh-T9h3-CHlSZtvBRx9EGkUNzKBiP41MI71M_HWHl0hfEJznKGYKWYgxUcpXYlq_FahSL0oDbIZNJ19sUKga0poHo9Mhdak4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6cc885feb3.mp4?token=K7TxQlAiYAeHQ3cm9TEKUm6c7HLzIfQ2MXJHt7ZCSpntMLwEItYhUUwACaKqa-tPpsvMRzWKblJXijm83JxC1eIJ2WUc8hH6rDxMz6ieyKri4A8Sz3v5E4X55J3YrM3D4nUL60Us_Z0OfhUBJmF2cfc0-fM9jqoFZicdr0l1MI9XKCcHAklnGTV9Tv2y0e50iUgAC0WIuf_XN1GrvsXsjdb9aHab7IpC1rw3GN6k5yQFbOmN6ixw9Oh-T9h3-CHlSZtvBRx9EGkUNzKBiP41MI71M_HWHl0hfEJznKGYKWYgxUcpXYlq_FahSL0oDbIZNJ19sUKga0poHo9Mhdak4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صدا و سیما:
آمریکا با ۱۰ شرط جمهوری اسلامی موافقت کرده
‏۱. آمریکا متعهد به عدم تجاوز به ایران شده
‏۲. استمرار کنترل ایران بر تنگه هرمز
‏۳.پذیرش غنی سازی
‏۴.رفع همه تحریم های اولیه
‏۵.رفع همه تحریم های ثانویه
‏۶.خاتمه تمامی قطعنامه های شورای امنیت
‏۷.خاتمه تمامی قطعنامه های شورای حکام
‏۸.پرداخت خسارت به ایران
‏۹.خروج تمام نیروی آمریکایی از منطقه
‏ ۱۰. توقف جنگ در همه جبهه ها از جمله لبنان</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5140" target="_blank">📅 08:15 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5139">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">برخلاف خبرهایی که یکسره از احتمال توافق می‌گویند، فاصله خواست‌های دو‌ طرف هنوز آنچنان زیاد است که بشود گفت :
توافق بعید است!</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5139" target="_blank">📅 01:47 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5138">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
اکسیوس : ترامپ روز شنبه در یک تماس کنفرانسی به رهبران کشورهای عرب و مسلمان گفت که اگر توافقی برای پایان دادن به جنگ با ایران حاصل شود، او می‌خواهد کشورهای آنها به «توافق‌های ابراهیم» بپیوندند و با اسرائیل توافق صلح امضا کنند.</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5138" target="_blank">📅 00:35 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5137">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
اکسیوس : ترامپ روز شنبه در یک تماس کنفرانسی به رهبران کشورهای عرب و مسلمان گفت که اگر توافقی برای پایان دادن به جنگ با ایران حاصل شود، او می‌خواهد کشورهای آنها به «توافق‌های ابراهیم» بپیوندند و با اسرائیل توافق صلح امضا کنند.</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/5137" target="_blank">📅 22:25 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5136">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromدماوند</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LO_tbO7eldI7KNAGwO9Fw4uLgVJGoRD54hsyqEu7mt7I7vjj-brDA9p87g0MAVX0hPcousI8VWb1ovjyd7ZiJ0PSY2JtJSvQXyhjCinxUEHi_NnpRHH7nuN-SEfH67YbjSjX4PDCLLlVtZlAOqyixkI93sPOUpXWCSNyTJ5ZDp9zeKXf9909oznQnqdDl3gWrgtj39pxAubVlAIJpS14ZdHz8YaTFBiVDwuVQTniYWx3c1_upu9iGbDDIpwVCabjK8zzUavCdHZ0nF3eGARrfmy1vZc3ke_iEoRRUqlw0Nr7svb5kws7VE74u_oDp4f-sFHMtvKSN_x06QfjQVmcvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❗
یک اعدام دیگر
مجتبی کیان، بامداد امروز و همزمان با اذان صبح، به دست جمهوری جنایتکار اسلامی اعدام شد!
جرم او را ارائه مختصات صنایع تولیدی به شبکه‌های ماهواره‌ای اعلام کرده‌اند؛ انگار که اسرائیل که اتاق خواب رهبران رژیم را می‌داند به اطلاعات دیگران نیاز ندارد...
خبرگزاری سپاه نوشته است: «وی در پیام‌هایی به شبکه وابسته به دشمن، اطلاعات محل شرکت مرتبط با صنایع دفاعی را ارسال و با قید نام نخست‌وزیر رژیم صهیونیستی در پیام ارسالی به عوامل این شبکه تأکید می‌کند که موضوع را «به بی‌بی آمار بده»!
T.me/irdamavand</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/5136" target="_blank">📅 15:52 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5135">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">️
🚨
🚨
آکسیوس: یک مقام آمریکایی گفت که پیش‌نویس یادداشت تفاهم شامل تعهدات ایران برای هرگز نرفتن به‌سوی ساخت سلاح هسته‌ای، و همچنین مذاکره درباره تعلیق برنامه غنی‌سازی اورانیوم و خارج کردن ذخایر اورانیوم با غنای بالا از کشور است.
☢️
به گفته دو منبع آگاه، ایران از طریق میانجی‌ها به‌صورت شفاهی به آمریکا درباره میزان امتیازاتی که حاضر است در زمینه تعلیق غنی‌سازی و واگذاری مواد هسته‌ای بدهد، تعهداتی ارائه کرده است.
- ببینیم چی میشه. بعید می‌دونم جمهوری اسلامی اورانیوم غنی سازی شدهاش رو تحویل بده،
خبر هم میگه ج‌ا به یک میانجی (پاکستان / قطر) شفاهی گفته!</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/5135" target="_blank">📅 07:35 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5134">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">‏
🚨
🚨
ترامپ :«من اکنون در کاخ سفید هستم؛ جایی که همین لحظات تماس بسیار خوبی با محمد بن سلمان آل سعود، ولیعهد عربستان سعودی؛
محمد بن زاید آل نهیان، رئیس امارات متحده عربی؛
امیر تمیم بن حمد بن خلیفه آل ثانی، امیر قطر؛
نخست‌وزیر محمد بن عبدالرحمن بن جاسم بن جابر آل ثانی و وزیر علی الثوادی از قطر؛
فیلدمارشال سید عاصم منیر احمد شاه از پاکستان؛
رجب طیب اردوغان، رئیس‌جمهور ترکیه؛ عبدالفتاح السیسی، رئیس‌جمهور مصر؛ ملک عبدالله دوم، پادشاه اردن؛
و همچنین ملک حمد بن عیسی آل خلیفه، پادشاه بحرین داشتیم.
موضوع این گفت‌وگوها جمهوری اسلامی ایران و تمامی مسائل مرتبط با یک “یادداشت تفاهم” در ارتباط با صلح بود.
یک توافق تا حد زیادی مورد مذاکره قرار گرفته و تنها نهایی‌سازی آن میان ایالات متحده آمریکا، جمهوری اسلامی ایران و کشورهای مختلفی که نام برده شد باقی مانده است.
به‌طور جداگانه، من همچنین با نخست‌وزیر اسرائیل،بی‌بی نتانیاهو، تماس داشتم که آن هم به همان اندازه بسیار خوب پیش رفت.
در حال حاضر، جنبه‌ها و جزئیات نهایی این توافق در حال بررسی و گفت‌وگو است و به‌زودی اعلام خواهد شد.
علاوه بر بسیاری از بندهای دیگر توافق، تنگه هرمز نیز باز خواهد شد.»</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/5134" target="_blank">📅 00:31 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5133">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NPvMRMsFf4MtbUIBud1OEFn0HKPX_v1TEWilFqi-HavOfYvfE67Z25-UCtWHpCQhcCxK5DsC7mIRlnU3lA461po1NmB9eKF5c2WxaeHEuoZKZ5GKfKMXCYFEgS0u-Tim9IG-igsYwAxY4zQ4in373nv1t41vAU8nuQFWlgIe_iIGVtOF7RRGLIF8rSZ-5xjP_XN8LXlPG7DgIwocfR7kaVZLXpfxQThDKHgG7Vab5KuXuxY8DUxvovwo7v7iBtQX2JO0Zl3TIygrEESKUEuIgsSbinsNZmJAvXkHSyWvPGVATGm8hlBn1UHpKmUUSulbpn05prRi9Ve6TeGDvIhN3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با هوش مصنوعی طراحی کردم.
گاو : نماد فراوانی و ثروت سرزمین ایران و منطقه.
تن زنانه و نیمه عریان: نماد پاکی، نماد لطافت و ظرافت ، در نقطه تقابل با خشونت و توحش و درندگی
بقیه هم‌ که معرف حضورتونه، آشنای دیرینه.</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5133" target="_blank">📅 22:09 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5132">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">ترامپ به اکسیوس  گفت که درباره توافق با ایران یا بمباران، «کاملاً پنجاه‌پنجاه» است. ترامپ گفت امروز با مشاوران ارشدش دیدار خواهد کرد تا آخرین پیش‌نویس توافق را بررسی کنند و ممکن است تا فردا تصمیم نهایی را بگیرد.</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5132" target="_blank">📅 20:57 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5131">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🚨
آکسیوس : ترامپ ساعت هشت شب امشب ،  در یک تماس کنفرانسی  با رهبران عرب شرکت خواهد کرد تا درباره پیش‌نویس توافق با ایران گفت‌وگو کند و نظر آن‌ها را بشنود.
🔺
نظر شخصی :  توافقی در کار نیست!</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5131" target="_blank">📅 20:55 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5130">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
آکسیوس :
ترامپ ساعت هشت شب امشب ،
در یک تماس کنفرانسی
با رهبران عرب شرکت خواهد کرد تا درباره پیش‌نویس توافق با ایران گفت‌وگو کند و نظر آن‌ها را بشنود.
🔺
نظر شخصی :  توافقی در کار نیست!</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5130" target="_blank">📅 20:13 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5127">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b5c3d0822.mp4?token=vnKHteONam33dE8W5kEe7CkUHaehO4foOAXzCn-PjHPk0397DxDUwGfib6z1VnKl1misWwEV-z9MOsKEpdrfpo1brU5N7v0HyZWP4mudB8-eFWSEUEm1ksnhU0DcBYX_xWcggHOlc_3W0pEm7uteEUtdm5JntGbXLFdaCltjZUiwLvKxI9AGruB_4fbKqzPAFWDWriiImQ54WzqhdbOsFK7wt9HaJDbCKiCthixKQqGy-FwjeybbGCbHbEtBRZg56sVnZQ_L_ErJ4_CO-6BHgeGpv-AhRUvLAhQ217-3MP8ieII8gZptZeZ87YTqrSUsXQ73W7Z8qpHLcgrpXResNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b5c3d0822.mp4?token=vnKHteONam33dE8W5kEe7CkUHaehO4foOAXzCn-PjHPk0397DxDUwGfib6z1VnKl1misWwEV-z9MOsKEpdrfpo1brU5N7v0HyZWP4mudB8-eFWSEUEm1ksnhU0DcBYX_xWcggHOlc_3W0pEm7uteEUtdm5JntGbXLFdaCltjZUiwLvKxI9AGruB_4fbKqzPAFWDWriiImQ54WzqhdbOsFK7wt9HaJDbCKiCthixKQqGy-FwjeybbGCbHbEtBRZg56sVnZQ_L_ErJ4_CO-6BHgeGpv-AhRUvLAhQ217-3MP8ieII8gZptZeZ87YTqrSUsXQ73W7Z8qpHLcgrpXResNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقتی بعد از صدها سال
مردم شمال مدیترانه و جنوب مدیترانه بهم رسیدند
الجزایر سال ۱۹۵۲  (۷۴ سال پیش
مناطق اروپایی نشین
و مناطق مسلمان نشین</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5127" target="_blank">📅 19:52 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5126">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SoVy1160dyFhciEWAN763FS4nZPHSgP5x40ofW7vpiJOWufEevvGO9_FQ4OLwa6-ZyNGYiZsZZezhly85MAhJBquW-N-q7EC_snxaJOCgn0XvVI89l_302kwphAZZzU9usqUwsTV6pz_iNzo4xClskD7NzypD5RLU3hpSwdKSQWP3nxwpGOeRq6f0_M1HOde0eLi4Cs1cW4xB2_Vz33ViMmkvCzx3G79G9cVM9DoKIcxrumthm8gj6q09l-T3SHHGJzYMwMOMIsFFHtXPpAVwnZ9mSvM0hH-HcGT3Y84ZEUxpD2fqac7G7Jp5TH20qUo0JUabtE5_9aIwaWY_xXK7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شمال دریای مدیترانه، اروپا، نماد پیشرفت
آرامش، ثروت، هنر و معماری و….. است.
جنوب مدیترانه، نماد فقر و بی‌ثباتی
و جنگ و سیل مهاجرانی که
از این سرزمین‌ها می‌گریزند و …..
مصر، در جنوب مدیترانه، برای ۹۷۰ سال بخشی از جهان یونانی - رومی بود.
لبنان و فلسطین هزار سال، لیبی ۱۲۰۰ سال،
تونس و الجزایر و مراکش حدود ۹۰۰ سال.
تا اینکه اسلام از راه رسید
و تفاوت میان شمال مدیترانه
و جنوب مدیترانه شکل گرفت.
و دو سرنوشت متفاوت، دو چهره متفاوت گرفت.</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5126" target="_blank">📅 18:48 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5125">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bgBlubWdy7lFFetMjPiMBE-04DfOdiQ31U7Q1rE8vM8q9N1kXu6gD3YHeIzjNeCLR_8QWaEz7U6cM4kHU9P5o7Z5fOsQZNzDWgcVJGUgjyW3cBeBh-55pMZySwnFkoYEtFU3w6MthcaLlMsxVr7Ez556AVbqM_5wGX0imdEAWSPy5lyJjp1ie8TK-NCzBkr-YG_UzLQTPOBSOuMefEHBLGpwNO0WaWbszMEUHk164ulREz5VIzP2CbS_rxgkJjNLCt_erzXdtnQo1QFFBCbgNvXdT2XuxLc_nNS_cbS3DwyzZA5a5GQYEvuI-zWmUCkzVpwOv8M6X6F59hjJcEZSOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید ترامپ که پرچم آمریکا را روی نقشه ایران به تصویر کشیده و تیتر زده «ایالات متحده خاورمیانه؟»</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/5125" target="_blank">📅 18:16 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5124">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">مارکو روبیو در خصوص مذاکرات با جمهوری اسلامی:  شاید تا عصر امروز خبرهایی باشه، شاید هم نه. مطمئن نیستم ولی امیدوارم. پیشرفت‌هایی صورت گرفته. شاید عصر امروز، شاید فردا، شاید این یکی دو روزه، چیزی برای گفتن داشته باشیم.  جمهوری اسلامی باید دست از غنی‌سازی بردارند.…</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5124" target="_blank">📅 17:29 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5123">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">مارکو روبیو در خصوص مذاکرات با جمهوری اسلامی:
شاید تا عصر امروز خبرهایی باشه، شاید هم نه. مطمئن نیستم ولی امیدوارم. پیشرفت‌هایی صورت گرفته.
شاید عصر امروز، شاید فردا، شاید این یکی دو روزه، چیزی برای گفتن داشته باشیم.
جمهوری اسلامی باید دست از غنی‌سازی بردارند. اورانیوم غنی‌سازی شده را تسلیم کنند، تنگه هرمز باید باز شود.  ترجیح رئیس جمهور ترامپ دیپلماسی و رسیدن به یک‌ توافق است.</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5123" target="_blank">📅 17:25 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5122">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uZm0faXYE0ahT7ZjzF_H53G-OPCyxSk-VBOC0HE3OZbzBXJ26vI7DjM8__C5HHJriCIZ1Tb-wmruL70f952ffS7HYopCCV3MA8BoTSM9DVm9mewhuSSO73i7jQELb2m1Cyyagnnzrc1hbALNFCQ-BhXd2nEn5pDcgvtyHnk_CBplW6Nj-SCxChP3CrKfImLeOTr-TtVZsyaMmCkCfpIMPTm7wzlwpJ1ZovMMivl0qXFlfDyTAmVV1MIIeAFYEYFu8-IX9lqD2sPWkGPNpgPnHBx5m-SI-SSIXwxWxrpWiPW1lY4owi2PYE2kkNe6UKktSeYZFofjV_wXkIES9mMCHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چقدر ایران باید هزینه بده برای این گر‌وه‌ها
و برای این جنگ‌های بی‌پایان جمهوری اسلامی با آمریکا و اسرائیل.</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5122" target="_blank">📅 17:18 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5121">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">به خاطر ارسال ویدئو ۲۷ سال زندان!    مجازات پدر «رومینا اشرفی» ۱۴ ساله، که با داس سر دخترش رو برید: ۹ سال زندان   حکومت اسلامی! عدالت علوی!</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5121" target="_blank">📅 13:23 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5120">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T4oAyZN1bsNyiyKGAHQ7hk9riphZJ4ksg5CZBqwbWVv36G0R3w-i2sA-Jfs0ZzZ8w92CEsysUS-F0E6koDbeLvEywV0Mjl8m75GEdTRxZ8_DLsxAfB2L8b5NHjq6UQoCrqDI3CIaGs2Cb_BWShm5tY266uhmSk3aDGORFRbqBSupb6EjrQnfpsi7XaqOS8j0sGRN7ggxe8O7MPZKD8ii4PliLpUlMQ9_fnRagm3OEtIptZEDJo05a2vtyvloD2C6L39rB5Wdd2xVXM8jngNJXuX5HDi4s8hiBYeOeiW_sJhOYtelGv9Ml5j22tmSaJJpRlq37O2UvLi5CviBUHJqBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به خاطر ارسال ویدئو ۲۷ سال زندان!
مجازات پدر «رومینا اشرفی» ۱۴ ساله، که با داس سر دخترش رو برید:
۹ سال زندان
حکومت اسلامی! عدالت علوی!</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5120" target="_blank">📅 13:20 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5119">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🚨
🚨
🚨
نیویورک پست در گزارش اختصاصی خبر داده که طرح ترور ایوانکا ترامپ خنثی شده
.
فردی که برای ترور دختر ترامپ تلاش کرده «محمد
باقر
سعد
داوود
الساعدی ۳۲ ساله و شهروند عراق است که گفته شده توسط سپاه پاسداران آموزش دیده.
انگیزه او انتقام از ترور سلیمانی عنوان شده.
نیویورک پست نوشته که الساعدی از اعضای ارشد گروه شبه‌نظامی کتائب
حزب‌الله
عراق (از گروه‌های نیابتی مورد حمایت جمهوری اسلامی در عراق) است و گفته می‌شود
آموزش‌های نظامی و اطلاعاتی خود را مستقیماً زیر نظر سپاه پاسداران در تهران گذرانده است
. او با قاسم سلیمانی و جانشین وی، اسماعیل قاآنی، ارتباطات نزدیکی داشته است</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5119" target="_blank">📅 08:14 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5118">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">حریم هوایی ایران در مناطق غربی بسته شد.
پروازها فقط در طول روز</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5118" target="_blank">📅 01:01 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5117">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
🚨
براساس گزارش آکسیوس، ترامپ به‌طور جدی در حال بررسی آغاز حملات جدید علیه جمهوری اسلامی است؛ مگر اینکه در آخرین لحظات، گشایشی در مذاکرات حاصل شود.</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5117" target="_blank">📅 00:13 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5116">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">وال‌استریت ژورنال:
واسطه‌ها در تلاش هستند تا یک توافق موقت بین ایران و ایالات متحده به دست آورند.
پاکستان، قطر و دیگر بازیگران منطقه‌ای در تلاش برای کاهش اختلافات بر سر برنامه هسته‌ای ایران، رفع تحریم‌ها و امنیت منطقه‌ای هستند.
هدف، یک توافق کامل نیست، بلکه یک چارچوب موقت است که آتش‌بس را تمدید کرده و امکان ادامه مذاکرات گسترده‌تر را فراهم کند.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5116" target="_blank">📅 23:39 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5115">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gsn6iDiNM8v5uRPUv_Ynudg8StT50FT476KR4KDUBoGfGybFaIh7qa0eluRGjZTE0YA16ZCPVn4DTCHZ9xFRWGUFyVE9L1FjyA16s9gRGsf-JWTkjAIInAGhb1QgOsrnt_nRGoyAlN6F-W8_BnmHTITxCaWlmnF3NpOHfcqtySG-6XjDP7KOKwalBFfnEbkchF6iQYCWIV0lwX9rGsQNfLDufZogGl0ar6CcdtsoUHHMmfBSZTqoaPlWsFi3ogxGuRbIYabDvFsOI5K0n-iigCTgxp-jsrZOyVzxaScFOEmz470KsZWj_cF7SEm0gHBRhvnwbFCg08pOuVNanDC-Hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری وابسته به سپاه این مدلی تیتر میزنه
ولی در واقع «گابارد» از مخالفان معروف جنگ علیه جمهوری اسلامی بود که الان کنار گذاشته شد.</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5115" target="_blank">📅 22:55 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5114">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pAUzFVxa0hAhr6ntZfdAL8atkfVqmZTdfMZojSpfZn6C9E2labbHg_UDaZdGhFZQfqMVMwcadQgWqoF-gEAMKkH_1Zlujevamk5MLQqfval2KP0uEft_gi6vLxESQTgu0_GV-IJyb795xuC7HEXWoGwe3xqfVkaogVvox9hs0Xf5j6_UwhWtY2gLgeLn5JqGlbpI96j50jdbdYS4tN787m3T5GNGQ2Z4fD8WoCvdxarME6NtsDsPJWDJ0TPF8yt5RjYmBf6n1dX7D2nF7_klSw8GHFh-pupnlnzEGVD5reyPrJGpTvZHaIA1q3y58et7F7d-KcRkaIRacmp0tHag0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به بیانی دیگه : توقف جنگ در لبنان، پیش شرط اساسی جمهوری اسلامی برای مذاکره با آمریکاست!
خب چرا جنگ در لبنان شروع شد؟
چون گروه تروریستی حزب‌الله حمله کرد به اسرائیل.
مهم‌ترین دغدغه‌های جمهوری اسلامی نظام خودشه و حفظ نیابتی‌هاش. نه ایران و منافع ایران.</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5114" target="_blank">📅 22:18 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5113">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">سخنگوی وزارت خارجه ج‌ا : «اختلاف‌نظرها بین ایران و آمریکا آن‌قدر عمیق و زیاد است که نمی‌شود گفت با چندبار رفت‌وآمد یا مذاکرات ظرف چند هفته ما باید حتماً به نتیجه برسیم.»
🔺
یادآوری : جمهوری اسلامی از سال ۱۳۸۲  (۲۰۰۳) مذاکرات جدی! در خصوص فعالیت‌های هسته‌ای‌اش رو شروع کرد!</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/5113" target="_blank">📅 21:04 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5112">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromRadioFarda</strong></div>
<div class="tg-text">مصاحبه اختصاصی با قرقاش: ایران در موقعیت ضعیفی است، دور دوم جنگ فاجعه‌بار خواهد بود
🔸
انور قرقاش، مشاور رئیس امارات متحده عربی در امور خارجی، می‌گوید دور دیگر درگیری میان ایران، آمریکا و اسرائیل «فاجعه‌بار» خواهد بود.
🔸
آقای قرقاش که در نشست امنیتی گلوبسک در پراگ حضور دارد، در گفتگویی اختصاصی با گلناز اسفندیاری از رادیو فردا، گفت که کشورش از یک راه‌حل سیاسی حمایت می‌کند، اما در صورت بروز یک دور دیگر از درگیری‌ها از خود دفاع خواهد کرد. او همچنین گفت جنگ کنونی نفوذ آمریکا در خلیج فارس را پررنگ‌تر خواهد کرد.
🔸
رادیو فردا
: آیا امارات از مذاکرات با ایران برای پایان دادن به جنگ حمایت می‌کند یا ترجیح می‌دهد آمریکا و اسرائیل فشار نظامی بیشتری بر ایران وارد کنند و همان‌طور که برخی می‌گویند «کار را تمام کنند»؟
🔸
انور قرقاش
: نه، ما به‌وضوح تلاش زیادی کردیم تا از وقوع جنگ جلوگیری کنیم، زیرا روابط ما با ایران در حدود ۴۰ سال گذشته همواره رابطه‌ای پیچیده بوده است. ما همسایه هستیم؛ تجارت، سرمایه‌گذاری و پیوندهای زیادی با یکدیگر داریم. موضع ما این است که حل این مسئله باید از طریق سیاسی باشد.
راه‌حل‌های نظامی، همان‌طور که امروز دیده‌ایم، پیچیدگی‌های بسیاری به همراه دارند. ما همچنان از یک راه‌حل سیاسی حمایت می‌کنیم، اما این نباید بهانه‌ای برای درگیری‌های آینده باشد. مسئله تنگه هرمز روابط را پیچیده‌تر می‌کند، به‌ویژه در مورد دسترسی آزاد برای تجارت و انرژی جهانی.
🔸
رادیو فردا
: پس در واقع، همه‌چیز به جزئیات بستگی دارد.
🔸
انور قرقاش
: بله، جزئیات بسیار مهم هستند، اما ما همچنان نمی‌خواهیم شاهد تشدید نظامی باشیم، چراکه می‌دانیم تشدید درگیری‌ها در منطقه همیشه به بن‌بست منجر می‌شود و آن بن‌بست مشکلات بیشتری ایجاد می‌کند. همچنین باید در نظر داشته باشیم که منطقه نیازمند ترمیم فراوان است. به‌طور مشخص، امارات هدف ۳۳۰۰ موشک قرار گرفته است.
🔸
رادیو فردا
: که حتی بیشتر از حملات ایران به اسرائیل بود.
🔸
انور قرقاش
: بله بیشتر از اسرائیل و ما همچنان در حال پیدا کردن پهپادهای زیادی هستیم، بنابراین شمار نهایی از ۳۰۰۰ فراتر خواهد رفت. کار زیادی برای ترمیم روابط باقی مانده و پل‌هایی که سوزانده شده‌اند باید دوباره بازسازی شوند.
🔸
کامل این گفت‌وگو را در وب‌سایت
رادیوفردا
بخوانید.
@RadioFarda</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/5112" target="_blank">📅 18:57 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5111">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DgHXHx5q1b6L3Gho0Jx2jBmitkPditLJwho9hIb1rNWDVzdZPZRZOMlJTVJILKygYR1P_tZ5jyRo9-ygOOPasWZDvnju7GirLQdZwLmtZtnmXVNiyLjWiSjmiBBDpicKaB4W9Yptkm9Fpifu28rnV4hsaqb-d2cfsGToQ7R1iyRBsFKj169XohmBBzktUuRENB_0KCHHJox93VJaVMg08Mv-pa8MOlnwA3nSt6F4JUBmFOORJy4h3X6WB_y6lArbQi7F-gicgedHzDfKVlzj9Q36rIOowyKc_wbdFp6CvjQc52OHWmwnWEfz7y417W3ENc0XijvFGpdUTPXs7ZgH7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این خانم! از چهره‌های معروف چپ  در دانشگاه تهران! در تظاهرات حکومتی شرکت میکنه!   بدون توجه به اینکه جمهوری اسلامی طرف  دو‌شب دست به یک قتل عام هولناک زد!  پس چرا کنار جمهوری اسلامی است؟  چون جمهوری اسلامی ضد آمریکاست!  از اسرائیل هم فقط به این دلیل بدشون…</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farahmand_alipour/5111" target="_blank">📅 18:52 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5110">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iuvbb5pgMq3jUJ6jc6ZLO9f0OFvjUVXv4e5EYwn_9vxqREFP880axbqBfV7Jv8-Hdg6nVXYfMCXAXlRmcHhYze_3yCSZHAN_u7q-n7YDRD4aoNrz1N4ZaAca90Jl0ndVyAcpq0k42lWsXIzKfjWYhxbR0x8dMOzrhGb1L0UIERea28unrvPG6bciR8QmAqKwvy4PvXCJPfevbsxfhLWj8MWIw2t3ZQvwYAg_9Vx0CI_MEp1gzlmegJBPBCyg0koEaMp4iPHSzZjmwCJ2RmmZKr8mWiWSj6Yv5auQNatEnkW8vteaauwgWNRq0Gmb45px0Q88yYWETObvy2qCQ0Vw6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این افراد، از همون روز نخست حتی قبل از وقوع انقلاب ۵۷ در آرزوی  تبدیل ایران به یک «ویتنام دیگر» بودند، یک سرزمین دیگر برای مبارزه با آمریکا!  بسیاری از سران و اعضای بلند پایه چپ و…..  توسط جمهوری اسلامی کشته شد،  اما این به چشم خیلی از چپگرایان مهم نیست! چون…</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/farahmand_alipour/5110" target="_blank">📅 18:45 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5109">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cOS7TunRE6cEuOJdMvkI56yvJU3UAK_F4oS3lHk9uX8HvkybV2KxB__XGCdauOJLc9chBKLqIywDwFEmkxWfRqfP4pS1Jz95kY85MEgp8k5MVktnkg0AS9axdppgSjNKGf3H9MiC4jrCbP5_EouwzCvFfISThmv_rficQuIX5heihYOJI5hc73als36BnqcHYgFlylKQF8yX9z_F-pEJXr3ZQFBRMmGxHgyeZoXW2C7w6mzsBL_6Jbea0l-UlgONEBZVzs5UuU3_ZvIvXziJFA8Fc3s9sOR8EkBhxRAiPuFD9NKPPoaDSpLsRCB_nMy6OvlDtT0Eo8rVsrx_F36psw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جلال آل احمد، در سال ۱۳۴۱ کتابی منتشر کرد به نام «غرب زدگی» که تاثیرات بسیار زیادی روی نسلی از ایرانیان گذاشت!  جلال آل احمد با اینکه خود مقید دین و مذهب نبود،  اما فقط به علت دشمنی با غرب  در این کتاب می‌نویسه :« مسجد و محراب و حوزه، از آخرین سنگرهای استقلال…</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/farahmand_alipour/5109" target="_blank">📅 18:39 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5108">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/egB1FYvt2hNWYTJXgyWSm7BnaOaV7gf2BJtANAfMCcVTXkFQnOaXAUjlM8Br2Pf7x8RntHGkIyynbHFcmsrXhiYzPRO9GA_os3yE9725Fqior0uYy43UPLJMMsR626rG9YpNWIdIa_CHtfyFHKQi0YgwuhHuFv0Tr7dVW7Z_zhRQ7g4yrmAwHt5cjLYREP5Rlf-vI-sFL2Q9ZvtNZmepoH5Q_PR_v3Cqz1qdK9zZCA0QkBG5kiIYHy9QRQrFqBozsXrG7I5GN8z8m53TEmy76Vft596ecyyjbzTM3dLGbVxTkrmQajv2faC7zdA7XE0MRJU6BqJ8o0padLpjpBamkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سوال زیاد پیش میاد که چرا مثلا چپ‌ها،  یا به اصطلاح روشنفکران و…..  تا این اندازه در آغوش آخوند هستند و مدافع آخوند!  «ضدیت با غرب»! غرب‌ستیزی! اسرائیل‌ ستیزی، باعث میشه که اینها به آخوند وصل بشن.  اینها ایران رو سنگری میخوان برای مبارزه با غرب و با اسرائیل…</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farahmand_alipour/5108" target="_blank">📅 18:26 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5107">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nhLx8eo0eS2g078qZlpxMNfRZAtLL95fUgBYDGQKvm0f5-ILWX3pBvbyBptKyl2_81SdZxtR5AAz93ZEjIoENtml_5-7hGTZKhigf19GIetQWULgUfhJjEOf6R_3aCIcLm-kwJD-w7OMaUEWDgTdk0ejEkzlyPC2ISJGU7gpv8nIqLaSvVb81mlf-xI9_L9ekbnz6w1gUs9KvwmTjyom_yXtKPaD3HsRkeFBm6WXAv0_Prc0Wg5Jag8vNQh66xKF_TS835VALB5luGj8yv8dvXy7WXuANreMCFV2IHq4s12VA0qbSjgny1K8jOBO8cg9kEVuaPsaAQ8mXNsn8Lanfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سوال زیاد پیش میاد که چرا مثلا چپ‌ها،
یا به اصطلاح روشنفکران و…..
تا این اندازه در آغوش آخوند هستند
و مدافع آخوند!
«ضدیت با غرب»! غرب‌ستیزی! اسرائیل‌ ستیزی، باعث میشه که اینها به آخوند وصل بشن.
اینها ایران رو سنگری میخوان
برای مبارزه با غرب و با اسرائیل و با آمریکا.</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/farahmand_alipour/5107" target="_blank">📅 18:20 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5106">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b7e3e4f1a.mp4?token=QoiMh9A-dz8EHgnn54W4UzuWLlhQvclriUpQXB-kjIt6q1rBJspdteppkSA0XIyRvYtBvAFPFedRJjTrCsfXPk9a09ji4Ap8COIrndeASZ9jRfQYHjsolgwg3a9CY8rGbXk-FsTFaGFqptzB7eK7qLmcv4Q3TEQKkDZG1oy4u-eE4l0Y_vYdYatFF5S0Dx6bglQB57pYmqAEOyDMy5HA1a7SkeeU03UjJrDAiBir8gxhwiinXkRnGNx0lPJ11bqzEaDgwknRzJF0mzOtPWtJKS3DmxzsZvNbOq0Tf1S986k0b_CyPqPX2sAFo0YejAmH_ZM37yI_O79ZIl1twQI9ig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b7e3e4f1a.mp4?token=QoiMh9A-dz8EHgnn54W4UzuWLlhQvclriUpQXB-kjIt6q1rBJspdteppkSA0XIyRvYtBvAFPFedRJjTrCsfXPk9a09ji4Ap8COIrndeASZ9jRfQYHjsolgwg3a9CY8rGbXk-FsTFaGFqptzB7eK7qLmcv4Q3TEQKkDZG1oy4u-eE4l0Y_vYdYatFF5S0Dx6bglQB57pYmqAEOyDMy5HA1a7SkeeU03UjJrDAiBir8gxhwiinXkRnGNx0lPJ11bqzEaDgwknRzJF0mzOtPWtJKS3DmxzsZvNbOq0Tf1S986k0b_CyPqPX2sAFo0YejAmH_ZM37yI_O79ZIl1twQI9ig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت
جمهوری
اسلامی رو :))
با یک نامه ! بدون هیچ مصوبه‌ای
مجلس رو ۸۰ روزه تعطیل کردن.
«اگه رهبری تایید کنه …..»
اصلا رهبری وجود داره؟
رسایی می‌دونه وجود نداره و خبری نیست!</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/farahmand_alipour/5106" target="_blank">📅 18:11 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5105">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d143286b29.mp4?token=rQHpdymsS75OVUE7E_fGL530AN2hzpnsYhZ1qT59Tj9HKgBkQuHABjW7cxR3ZswNASwZUlM62GwWWo2j5ikty3AQwwMTPrVvHCyhIxD1Fo4vsId-02QVB2pHJRz6dS64ToH4NK4Fs4ts0fFoZceUd5EKmIhOByDldlhupGXpCB7DA1hIGhoCCmS_38Mh1YlKFmMKqETr8W-myxs8cf-_0zJ0JFhBVfYM8ehN11FWJ_eOHCaORWRHcCIU3NZ-cSVZ0XAoJrWgfZSNweu9dattfry_l4hSocUXSoR421kOWcCSuJfBlHmFgDxMvyQVl957FGO-dahVu-LiQ-A-AnvFVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d143286b29.mp4?token=rQHpdymsS75OVUE7E_fGL530AN2hzpnsYhZ1qT59Tj9HKgBkQuHABjW7cxR3ZswNASwZUlM62GwWWo2j5ikty3AQwwMTPrVvHCyhIxD1Fo4vsId-02QVB2pHJRz6dS64ToH4NK4Fs4ts0fFoZceUd5EKmIhOByDldlhupGXpCB7DA1hIGhoCCmS_38Mh1YlKFmMKqETr8W-myxs8cf-_0zJ0JFhBVfYM8ehN11FWJ_eOHCaORWRHcCIU3NZ-cSVZ0XAoJrWgfZSNweu9dattfry_l4hSocUXSoR421kOWcCSuJfBlHmFgDxMvyQVl957FGO-dahVu-LiQ-A-AnvFVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیسی، همون فردی است که منتظری در دهه ۶۰ به خاطر اعدام پنهانی هزاران زندانی به او گفت : «نام‌تان در تاریخ به عنوان جنایت‌کار ثبت خواهد شد.»  در دیماه  ۱۴۰۴ نه منتظری بود و نه رئیسی، اما خامنه‌ای و لاریجانی بودند و دست به بزرگ‌ترین قتل‌عام ایرانیان زدند!  …</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farahmand_alipour/5105" target="_blank">📅 17:21 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5104">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">«دست خدا عیان شد» و این صوبتا</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farahmand_alipour/5104" target="_blank">📅 17:15 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5103">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uv9-6hYhRGTxWMeD4Atv2N6K5Mp3TwoFI5VAzYebApEgwqe3FQ90Iq5pojCsA4r0MCwEXxx66JWJ17KYq3fQprrr_bGgL7CNeKQz7hrmFr7nSupmGsVPkNmx4GkcrEwWr8qZTtOZdMoppnukQ7Bh6kNY6Y8E_oVup9ckiXjfjK978gQ7xZa2N_h4odbkBno851Qx6VlpVjzuonxxYJI-kP3Xz0g21AThdbmcQxrue7Js0U4q9xHHFuJ9kOyFNXm9HfO5cImJ6xwQfeTCxQ_kmP9auG1N2YNZMg68VyiW37FF-VjVfP_d97qvjdix-a0pdVg-8VqFu6l_Uet2P33Yjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«دست خدا عیان شد» و این صوبتا</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/5103" target="_blank">📅 17:05 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5102">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">مارکو روبیو: پیشرفت جزئی‌ای در مذاکرات با ایران حاصل شده، کمی حرکت رو به جلو وجود داشته.</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farahmand_alipour/5102" target="_blank">📅 13:53 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5101">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">توییت سخنگوی کمیسیون امنیت ملی مجلس! (مجلسی که ۸۰ روزه تعطیلش کردن!)  فریبه آقا! فریب!  موشک بفرستید!</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/5101" target="_blank">📅 13:10 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5100">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G-x1weGZ06BPIP96wgUBaiBkkJqQaNeXS0e9wr_LsIifK503K_VcpcvvVzGOfRJlojWYNZ9dnpQ9NljcB2L8ZsHlfA4W6czgspdfyJatZaMrevWE1rZuxVv0vFtLA_3jo5u8BhjN-zlVvMK9_7zwpGynA1NKZUwBT6XlOxeXgoIYgIJEWCy0JqfEU2FVDXls6LfpHHNBa6Jje0J8XEqkUH3vBW9AzVYdYwJ6pBaxXOZ4-Fq5Bmv0eIOs0zqGbTnxsIyPxg3ZyI8lVvfgUO_Ad-LULbk_MNv3cDZAevLIKlpQRzNwB0QHz-EVzPbFcvcBwANR_rlH9FQQlWTfsIm52Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/5100" target="_blank">📅 12:57 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5099">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M58R0ROHMdQd8FjbU7E4vqkAi9Isj9NJttnthuVTk_e4CMBUj0KLbXBd6CnF6ZfsFPsJP9lXhxPenk0E-yr7_p6HhdK8VRvUzCi_6LssWAFxv4gRxmK7fKeGR5SvWWANNctJgixG-nGR8CqR3ZMvjXjy607N88lar4_js9_NAJ6D4qhZAkzptO1wsJVLoBK-cpsB3Scad8eGX8aoc3w6e0xRfodIIVn1ZXiVVO4b_ib3rcNZaM9oZCkhNq9xm6v0wEyWrEtZ3pUkk1ErwFUAkjMh7jaX3plkAwSzoCId_F_kcXeFVdwVO8fzWAR4yirZeygmBAUS3okXO7oqI0oEnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت سخنگوی کمیسیون امنیت ملی مجلس! (مجلسی که ۸۰ روزه تعطیلش کردن!)
فریبه آقا! فریب!  موشک بفرستید!</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/5099" target="_blank">📅 12:47 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5098">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">رویترز به نقل از یک منبع پاکستانی:
نگرانی وجود دارد که صبر ترامپ رو به اتمام است، اما ما در حال تسریع سرعت انتقال پیام‌ها بین دو طرف هستیم.</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/5098" target="_blank">📅 10:59 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5097">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca3794683c.mp4?token=aT1mL3Fr5Ya0ZTm-_L_c2H9roAg6_7b6xRFkqjdAEphW382wZrDxt1bgT4N8eRUVWMhi4JrHIQdWJLAEn1SSqLFk1f8xHgSfbkaAJ6AprEcx6Bu27906EEqz8CzQEG6XK54q4M1bobv4MUQpV0RM6omuk3CifVIhk45x3sDId7fHzJ0uPBSJoLM724_waboK12liEyyXgU8LvxyMH-deiZQVG8soBc6PfrG04doObZxdYj45Vz3nvks1IjwPwd4ta66gAOlEEIRPTcdE8UY6zbzTTcwSpMfQXNM2UechWPQMx8mWkGkLYqK6nTHvbW2RhIxHEYpNbOr367YZG087OA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca3794683c.mp4?token=aT1mL3Fr5Ya0ZTm-_L_c2H9roAg6_7b6xRFkqjdAEphW382wZrDxt1bgT4N8eRUVWMhi4JrHIQdWJLAEn1SSqLFk1f8xHgSfbkaAJ6AprEcx6Bu27906EEqz8CzQEG6XK54q4M1bobv4MUQpV0RM6omuk3CifVIhk45x3sDId7fHzJ0uPBSJoLM724_waboK12liEyyXgU8LvxyMH-deiZQVG8soBc6PfrG04doObZxdYj45Vz3nvks1IjwPwd4ta66gAOlEEIRPTcdE8UY6zbzTTcwSpMfQXNM2UechWPQMx8mWkGkLYqK6nTHvbW2RhIxHEYpNbOr367YZG087OA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انترهای جمهوری اسلامی
یادتونه برای حمله گروه تروریستی حماس،
شیرینی میدادن؟ یک‌ شب شیرینی دادن و ۲ سال
به سازمان ملل و به دنیا فحش میدادن که چرا مداخله نمی‌کنید و متوقف نمیکنید؟
(شما چرا نرفتید متوقف کنید؟ و البته میگن
پیروز شدن و نمیگن اگه پیروز شدن
چرا خواستار توقف مسیر پیروزی‌ها بودن)
حالا هر شب میگن «بزن و ‌دوباره بزن»!
فردا که «زدن‌ها» شروع شد، بخش «خوردن» که رسید، مقصر میشه دنیا و این «لاشخورها» میشن «کبوتران صلح»</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5097" target="_blank">📅 10:27 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5096">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">قرار بود امشب و در ادامه تلاش‌های پاکستان برای میانجی‌گری میان جمهوری اسلامی و آمریکا، عاصم منیر، فرمانده ارتش پاکستان به تهران برود که ظاهرا این سفر لغو شده.
رسانه‌های پاکستانی هنوز چیزی نگفتن. اما العربیه، خبر لغو سفر رو منتشر کرد.
عاصم روابط بسیار نزدیک و ویژه‌ای با ترامپ داره و غیر از این، کشور پاکستان نیاز بسیار شدیدی به پایان تخاصم در منطقه دارد، به خاطر اقتصاد آسیب دیده‌اش و…
اما به نظر می‌رسد که عاصم منیر به این دلیل سفر خود را لغو کرده که چشم اندازی از موفقیت و دستاورد، برای سفر خود نمی‌بیند.</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5096" target="_blank">📅 00:33 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5095">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/afm2MqBqsxqDQbBE_0ow3r5coXqqp6pKzLUS4x0D-q1uyx3tumDU0VilxyLueFXMfrOA2fkuajdzRI8N1iP1Z0wlaz13pzDyXN2w0wBnSBz9akkYGWI0S-Fdh04tGMT1mVo0C-2Nz9vhbKOQABIvSHt2RcEiT8wfouN7K41IJ2s7RcskABOVjRElUerzEUlsXLmhrjN2CtUbI21Z_-hdBTBiTPcoTaGM19Vjm4xESKNolXZA-YjsaVEs2tyrz4datGP5fcmhT7JpjJs7RgnkNSV2773FV9oImtGIZZVbOvkPYrZ1rI-AEYC7btvKS-iIW8XPZBJ3o-EYNSOO4Jv-9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5095" target="_blank">📅 00:23 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5094">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XRMBL9xQsiWrOS54mkfmjv_H2usfSAK1PcS_k3gB016cm_WnXFpfHqjMpivXttcxUaMgV_JRfx3M9VxFJYUarmr9G8Jk8dPzpmVhU3iGIaXmFebTdkyhtmD8jvAdlWCodChM3Nq_1v9WvgKdFf43duu2gh0RnNVuqbMMI1dyBanveW34nKEbZV9sFk_vD4PxqdPwkoNJD7GJ0LfUagJo5rCwQlnwxJ2L_nNJK-SyiBODaX2kAi-yqY89R9IZpzqVRVOLJGbQ9d2r8up6AT7ay2qtgG62Ga9F8QO4V8h6Fbv77RcJdm_b7mrfViRcnMhTXyLhdAn0dq5Q0JBDHdo_qQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از پیام‌های دریافتی</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5094" target="_blank">📅 00:23 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5092">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ICY2jQTw3ClvrfVF76Q9p8OuDPPhcqzy8sMWA9tOGXeo5gg2mAWlaROIK_TQULJq10LoeYcIgfap-GV9xd4lHDTkSwDjOIqTg3XclWkTNVz2bHs8YbutrnZEOU1FSumcdHCDWGPC36P3Hxfb_GJbtqhp2NMeLLYiOu84MMab3TM13sh8Oc2_sWuiaiUYkdqyCD39yssON4u4gLwaWGrFcbrWB3cru1IULuXYc3XhakV7Ffrn6DktJLNgE41jwVxpXj1PKKtVaE_y_xbEYfb5G8VZ0xJqwj70uFXyGAOLVyn0_aCjU4XY76v56-bBFFLM7dEn0HWSg9NUgTanWCTPbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از پیام‌های دریافتی</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5092" target="_blank">📅 21:15 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5091">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lLCr13eXHXn6jyFmsxlEWNnnl1Ah4W0jqrKAKeZbLf1XWdTw1u9_YuXzPxErnrgMZJVXXeEXN8L93nr-1st0OuixEyL4kH_7H_x3ftV0zQTbq5z3TpjOZmEroIkLan6zfjkZp7oXbqjMAf0MX3E1ApwDMu9hpimdMrSi4QLaJe3nxWpQum2IUWUFZty7Lv4vKoG2Hy6iBeFg4qsooWaGM81E21KbCsVpJpTa_EM-8qNVxBMb6UiIf6erliSUsmMyuGhrsvu3LjpZD5DJs641t5yWIKantFgQFjG2ZoO65F2oB8w2aolKPcZII_yii7SKgqCTwHHtIeETtqHYF9ViHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر بار مطلبی منتشر میشه که نشون میده
گزارش نیویورک تایمز چقدر بیراه بوده و بی‌پایه</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5091" target="_blank">📅 19:37 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5090">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mMjX-eK03qDC3NwzA8fsc-VG4Xj0PD6Xnc_dQy5FZ3Sp2JcaKANl2eYkwcDzx2SUA_mpc7VUj4gZhozdqYBCi2icHtFn_4UjwuTVnb4OqCQ5tLw47kfn181yMQHCorxEcXeROJ59Ddyg0DFjMvZliPVN9FF8LEtUfzuC1IMmL0sLwcLyzB4hnIvOUQVjYQmXCpVwu8M3sVqV6uZMucb_mhXJwsCV557xXptsb7Bvr8b7yenGfd8vK0eyXyaK6kJ8H3t7x-HrMg9p1v0ldDkhm7_y5o_YQ5Cuf1whNmCC7O5J-kC3xuR7TCK_bE1S8We6fpSnxdOicCsJf3IzyQENzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی رسما بخشی از سواحل عمان و امارات رو هم تحت حاکمیت نظامی خودش ترسیم کرده.
از اهداف اصلی این طرح و نقشه شهر
«فجیره» اماراته که برای امارات راه تنفس و عبور از تنگه است.
تنگه هرمز، تنگه احد شما خواهد شد.</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5090" target="_blank">📅 13:02 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5085">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OxSTSbZTvPEs_kb8YEv_JiRCAGKe3isc6PYEZLs67LpvWWELTUJMSyAtNqNf0zRkhlpq26k1SakEhMkr7GwIj_CC_933OMn3cyUizt63LJKtVlqKQQgt_on2PEsi9WQ1pEZEFPeWr_qvT9I8sgaHd9snb3J9LoNsgO90bDHr-q0cxf7N6loroe0E8LaCokMnPXGPn-3-nzdpPzE-9cqQeS0xMo1xZS38_Yb-Wl3LfEvqlPInRuqHOtfcL_YTx7W4sA8YT-jGIQYzl5E1APt4EFavrAHZV-KVz39SFA-H4op1cVrkZ3cm7jqa-7TZ8WakdGcUO6_p5SMo-as9CFKr9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hJZViS2DFE2ncuxaVuiJZ3zJLNCLTBy1kMlc2JJu357xu6TvelEzA55uLrGOh40oGkot116qg1jxug1wlf2tCYc9kVL0wD1xzBkx8vsreV3TogmkPSAY69NA4cIAkJ4FYA2Rf0-8n7amTjZ_EY8My6Y53Bj63OpmKb11YV3hnLG2dLvvxptyv0bf9mVVh1dptOopxQKMCscO8Ujt1RpdLnWW9Jbfp7-1sPpMOfw8f9iFK17AW8_dcyoluenwXD29bjzCYxGqecmn-L2aP-RgwQckGnrdZdXzZFXI0p5zquz07f1czVCCIxa2805_pgynH8v7Uhh9YfDe7PBzjeNooA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mRwakzCaMLrZ--nOf2UFONODl3gx4ofUv6tEjC1oUqa6-PB6XEQ77tvKW7S2Fht0Jf68S_QSZUMaE300qGNiz-1fnlXZCQksGaBdOISb1vtrWrfAzwAgAAoVkqm7TLZ-MgqPrcEtQkWO04Oya0XyV69H8qGyixf-hICB7Z0ER0-a_Yxc2gO-MjZiQSz_1upwCj9T3xS2QNZk5TXy8brcRQo3zP-4tO5ABERvV6ZxE62TKLvO4zJ2de1mZLXJfiXBcHdr5GLBlUIEjLA74yOFFjxKb9PypwT3_iePsZgUukCRXa_Q8BSJl68eJ5Vigdt-JaakW-BDIraHfuMRgguGVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IKiu7AH_OJiIeoi0Ibc0NHOkuqbuJgPnBeXtvpQX02LlHkfRfHDsEEDJ5Z82xFxYov3l4ozlgSZGYFWm6kOcvENkQq8eP0N5e9h3EzkeoBoK8raKKHLYP-MIwwtBOjAaWLp_h0KOrBUsFwPNP_ZlnO_OCNCAcNp2dB6_MEobH0dHjUcmOP7rogWhkTRpz2zQ1TFcplFyusg1nGXB_as-pFSil2I2gEyNSDX8CNYbsIJgy0zs1VmmgKXgbFVwCsrNr_0KnnfbgyASwgOO4mdZvFsb1r-f27n_siZ1VvjG3BYU1xqDS9MJCF7kBwsUvM9dbKNcPpmT2TYe5VQ_mjM0Rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qA4NKm9DE1qiHr9l7XY1ME9WwbAZJiuL5sfWvqVogAN5527QmBULatuy72KGP6Vn8f-W0RYZlO7_du37x45ZePI3jCAgWjwQ3pKgeQ1DLpbgdMsV_QfYqhrsTCNjthZVjnrpuyxKjTQH3sx0CxqCQrOZakIESJnn4Qnpz6WhGlptGmGc7Wm06ncUerIhuhqKRWLug4b8zK5s6Ku8Wvq3ASdkUTIpMfzED-0PeejpTHyfDQAWJNvBJQ3tGQIjnCB9eF0J6_gsZo9z_6xC3eQ3scK-0ptgkdhV_lhaDdy3lLMP2CwSLZajSAvaxdiWwzKl80PapVxBGEyVRMVVA10ngA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">'من وطن‌فروش نیستم... زنده باد جمهوری اسلامی... تا آخر کنار ولایت می‌مانیم... این پرچم با طوفان نمی‌افتد... سقوط این کشور را به گور خواهند برد... عزت این ملت معامله‌شدنی نیست راه مقاومت ادامه دارد...'  تبلیغ «وطن»دوستی در «کشور جمهوری اسلامی» با شهروندان وارداتی…</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5085" target="_blank">📅 12:29 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5083">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g7CeZXlpajZzc2zJIMNJ1pVmsRMhfYtNeiJ221XMBZHa0EOE4g3e0XhWjRSyctbzAcEWiDX_tfzatGB5Oga-coRV61wskq8vRQ3YNmTcH4jvhLQ2rYfgVHSSU5gdcoVPTzDyNWj_QJOw94ng0HvrpdynpNhsnvrHvhKa-IN-sLOjLpgUWXY_l0Pci7ZcTzWekYTK9ybAmuq8k7tYP23ory9HQchCVdGUxvf2vXPoI_22Kot1MHI4rHvtwoGLIHI2M3TNcitkZqAv4A_4xW54Hv35IE1UjCQXkHGNKk76tcNBHmVMadMZg89koL9lRV6Vo7yVxtLBkc7rgBBGIPeDKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54c0c9f59b.mp4?token=CwkcToZ1DX4NBz-8TcTcpZhyAoltcDSUZjGElGKvkiFIEQgF4FSRLP9i20qUR4EZBhkJVoEAn1mUNtvsy0DRllZkFa5OpfkxA4AwsbJA1lLYJ1OJuGVpDkO5u4xTglkylEqCrWHhlkaV94s3DMLAt1EjJKvX0m-vOCHFu6fIFdyXfjQTSfe26meC7W7Cs_j6IX_LXq9vyTYlzzx9phU1w5EcJUYtbaTl8t87jDbbPFOfQ-RfwDHTHykjXZCz3-pUwAQUpURJr8pAcVFRKUPISgJ9wzuPZ-dkYmfEr-XZaNr1x08355cp7rdl41-9067UeXdwwNerF3mYfpcvzSYKlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54c0c9f59b.mp4?token=CwkcToZ1DX4NBz-8TcTcpZhyAoltcDSUZjGElGKvkiFIEQgF4FSRLP9i20qUR4EZBhkJVoEAn1mUNtvsy0DRllZkFa5OpfkxA4AwsbJA1lLYJ1OJuGVpDkO5u4xTglkylEqCrWHhlkaV94s3DMLAt1EjJKvX0m-vOCHFu6fIFdyXfjQTSfe26meC7W7Cs_j6IX_LXq9vyTYlzzx9phU1w5EcJUYtbaTl8t87jDbbPFOfQ-RfwDHTHykjXZCz3-pUwAQUpURJr8pAcVFRKUPISgJ9wzuPZ-dkYmfEr-XZaNr1x08355cp7rdl41-9067UeXdwwNerF3mYfpcvzSYKlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حاصل ۱۴۰۰ سال علوم اسلامی!
علی خامنه‌ای هم به صراحت در یک سخنرانی «اجنه» را متهم کرد که با سرویس‌های اطلاعاتی غربی علیه جمهوری اسلامی همکاری می‌کنند.
در زمان محاصره اصفهان
توسط ارتش محمود افغان،
روحانیون بلند پایه شیعه، به شاه صفوی وعده دادند که به زودی ارتشی از اجنه
به یاری ارتش امام زمان (ارتش صفویه)
خواهد آمد و شورش افغان‌ها را دفع خواهند کرد.</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5083" target="_blank">📅 10:42 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5082">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/add91fa506.mp4?token=loLR1u4w3E37NMKSNY6sMnFpkd8LQLEJDaj3Yz-6SV-kf39NlmTPHJ-hovL8q98HubGpNyqd9u9SjBBMl4xw7SPTOetDiGHDWSw3-3YTIpnZdcj-8Xc3a9BaV2cIXCWeY9QC51RKYG5n2-mO5suYlY6msapLV4s9LTVkM7EMKrEUYqqrnSQzTul176FagX2810LReMlT6ksGOleLgN0l6ZGnvHSbn7C6Akj2JRLVDpvuSAm_y3Ibr6enKyJTfws-lrVOA6CvrGP4zysIXNVkP3MbofFzAEKE1QuZCmha59L4K_woSjJgD7qMftUS0_FMlmgu6D40_uUecLb1DgkyKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/add91fa506.mp4?token=loLR1u4w3E37NMKSNY6sMnFpkd8LQLEJDaj3Yz-6SV-kf39NlmTPHJ-hovL8q98HubGpNyqd9u9SjBBMl4xw7SPTOetDiGHDWSw3-3YTIpnZdcj-8Xc3a9BaV2cIXCWeY9QC51RKYG5n2-mO5suYlY6msapLV4s9LTVkM7EMKrEUYqqrnSQzTul176FagX2810LReMlT6ksGOleLgN0l6ZGnvHSbn7C6Akj2JRLVDpvuSAm_y3Ibr6enKyJTfws-lrVOA6CvrGP4zysIXNVkP3MbofFzAEKE1QuZCmha59L4K_woSjJgD7qMftUS0_FMlmgu6D40_uUecLb1DgkyKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یادآوری :
در پی انتشار رسمی خبر کشته شدن خامنه‌ای، در شهرهای ایران جشن گرفته شد
و ویدئوهای بسیار زیادی از این جشن
و تجمع‌ها منتشر شد.
و به قول این مداح
«صداش عالم رو پر کرد»!
حکومت از همون موقع اینترنت رو بست.
تا الان جمهوری اسلامی بیش از ۴ میلیارد دلار به خاطر قطع اینترنت زیان کرده!</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/5082" target="_blank">📅 10:32 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5081">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">محققان ژاپنی اولین آزمایش‌های بالینی انسانی جهان را برای داروی
رشد مجدد دندان
به نام TRG-035 آغاز کرده‌اند که در صورت موفقیت‌آمیز بودن، می‌تواند تا سال ۲۰۳۰ جایگزین طبیعی برای ایمپلنت‌ها و دندان‌های مصنوعی باشد.
از چند هفته بعد داستان جدید شروع میشه : اسلام ۱۴۰۰ سال پیش به این علم رسیده بود و پیش بینی کرده بود! ولی چون ما مسلمان‌ها به دستورات اسلام به اندازه کافی عمل نکردیم نتونستیم این رو کشف کنیم!
یه حدیث «معتبر» هم براش پیدا میکنن، مثلا حدیثی که اشاره داره به رشد دوباره گیاهان در فصل بهار! که به تفسیر آیت‌الله فلانی، اشاره به علم رشد دوباره دندان در بزرگسالان داره.</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/5081" target="_blank">📅 10:25 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5080">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">'من وطن‌فروش نیستم... زنده باد جمهوری اسلامی... تا آخر کنار ولایت می‌مانیم... این پرچم با طوفان نمی‌افتد... سقوط این کشور را به گور خواهند برد... عزت این ملت معامله‌شدنی نیست راه مقاومت ادامه دارد...'  تبلیغ «وطن»دوستی در «کشور جمهوری اسلامی» با شهروندان وارداتی…</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/5080" target="_blank">📅 09:31 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5079">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/48d635b5ce.mp4?token=Kx1gu5fsqgeC2xrEhmiTg3IoTBLrMrjknkBlvVotq4gulpCpYyXdDtA3JHQYdJRvxC5u55wVfCB787sfPiUuWea9F4isoMcHdSItSEj9FH_ZQSdJL4vFWzI7J38mWxviYg0PjfS1iVagjN94AZPTY664Vs13vPllnkAeHSh4v4pEev1r3n7v-uPMm-bCWc4eavcDiVc3ia3XYU-KDuMjGyQJ9PsoJr91tQy90mldb2X0MepFQRlyAVGhmxNRkyOUrWlMuAgFfxzDgCZ28a9eOpBZZt0bIbJYAK_nkZtRCjOAWXIf-gGpFTzz_LCJc4K5rwIsDTwWd9RqygAOPyRiCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/48d635b5ce.mp4?token=Kx1gu5fsqgeC2xrEhmiTg3IoTBLrMrjknkBlvVotq4gulpCpYyXdDtA3JHQYdJRvxC5u55wVfCB787sfPiUuWea9F4isoMcHdSItSEj9FH_ZQSdJL4vFWzI7J38mWxviYg0PjfS1iVagjN94AZPTY664Vs13vPllnkAeHSh4v4pEev1r3n7v-uPMm-bCWc4eavcDiVc3ia3XYU-KDuMjGyQJ9PsoJr91tQy90mldb2X0MepFQRlyAVGhmxNRkyOUrWlMuAgFfxzDgCZ28a9eOpBZZt0bIbJYAK_nkZtRCjOAWXIf-gGpFTzz_LCJc4K5rwIsDTwWd9RqygAOPyRiCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">'من وطن‌فروش نیستم... زنده باد جمهوری اسلامی... تا آخر کنار ولایت می‌مانیم... این پرچم با طوفان نمی‌افتد... سقوط این کشور را به گور خواهند برد... عزت این ملت معامله‌شدنی نیست راه مقاومت ادامه دارد...'
تبلیغ «وطن»دوستی در «کشور جمهوری اسلامی» با شهروندان وارداتی از 'عمان، سنگال، غنا، کنیا، بورکینافاسو، ساحل عاج، نیجریه، تانزانیا، مالی'
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5079" target="_blank">📅 09:04 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5078">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hZLdOPARgjViJwV2m9gV8AwAK8YL_GruD08LsSQ1Qm5pQCcJVk50NuGT7lHgW-v2ZgmFFU2g8-7UubSkpJmB9l0RXPW3D5H-ya_ylDeM3aWaRcko8O7pTqQhXexlmePNALL52uPeg6hv5yyzFdHcoJZHB6NF-tFFKJ4yZGQNIllHTf-UWAI6hWTNB6ImdrDp3bJMdYLgvM7O81B4yP5vYVcFu_UuRmcoKMD6CEco0nF7_cihu_Z6305vQldnNV_M82_zSs-OAH1V3hgZDqjZQJ8GN8R0h8aEsQDugK2H-QJ93ilEQFPz5bnSK4sjgQvcIx6hjCHm6Z9iTjIB_iHERw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5078" target="_blank">📅 23:13 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5077">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">قاآنی، رئیس سپاه قدس: «دستاوردهای ناوگان صمود ادامه دارد؛ این ناوگان چهره واقعی تمدن غرب و رژیم صهیونیستی را آشکار کرد و فلسطین را دوباره به کانون توجه جهان بازگرداند. »
🔺
یادآوری اینکه جمهوری اسلامی چگونه از موضوع فلسطین ارتزاق میکنه و درست به خاطر همین ارتزاق از موضوع فلسطینه، که مانع هر گونه صلح و سازشی میشه.
جمهوری اسلامی با راه‌اندازی گروه‌های تروریستی و جنگجویی چون حماس و جنبش جهاد اسلامی و… هر چند سال یکبار جنگی راه می‌اندازه، که منجر به تمرکز جهان به موضوع فلسطین بشه و اینگونه برای مبارزه خود با آمریکا و اسرائیل اصطلاحا مشروعیت بخره.
وقتی نگاه جهان به این نقطه متمرکز میشه، پیشنهاد صلح و گفتگو مطرح میشه، که خب دست نشاندگان ج‌ا صلح و سازش را «خیانت» معرفی می‌کنند و تنها راه را آزادی همه فلسطین معرفی می‌کنند.
و اینگونه جمهوری اسلامی از عوامل اصلی تشدید این بحران و عدم پایان این درگیری است، چون از آن ارتزاق می‌کند!
اگر جنگ و دشمنی نباشید، «مقاومتی» هم نخواهد بود! محور مقاومتی هم نخواهد بود! جمهوری اسلامی دیگر حرف و روایتی برای ارائه به دنیا نخواهد داشت!  تبدیل به یک رژیم عادی میشه! و این عادی شدن چیزی نیست که نظام ایدئولوژیک جمهوری اسلامی بخواد.
اینگونه فلسطین درگیر و قربانی جنگ‌های بی‌پایان جمهوری اسلامی شده.</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5077" target="_blank">📅 23:07 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5076">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">به گزارش تسنیم آمریکا پیشنهاد تازه‌ای برای جمهوری اسلامی فرستاده</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5076" target="_blank">📅 22:16 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5075">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e76a3523c2.mp4?token=N3cF5pOR97MF70zwYjfw-C32AgUc7uTUfTSuT5BfSikUskM5sJz89FZy8WViCZO3_FcEJyWAoNfpiW6yXNUjt7OfZVnsQXNSONimPN2Y5mojXyphePF6M9wAUj2KBhAM3ZxbLJju09bKIrojrPwxTxUiwGF2foBmWtTqy17_ZpPkRFf5sSkOhdYms85bu3Beu4XPBWlS4CjQsy40UdT5FCOyZXEQ1-TOvcvfQL5fvEdiG0vHQOjXV_N9hXncQup754uZwZf_6OXdbmXO44-7dQMWQXzyxv7ok-AspFiZCgpDgkxanGDL30qB5Cbud4PfwNP2m-ypNdK6RaARjbA7mA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e76a3523c2.mp4?token=N3cF5pOR97MF70zwYjfw-C32AgUc7uTUfTSuT5BfSikUskM5sJz89FZy8WViCZO3_FcEJyWAoNfpiW6yXNUjt7OfZVnsQXNSONimPN2Y5mojXyphePF6M9wAUj2KBhAM3ZxbLJju09bKIrojrPwxTxUiwGF2foBmWtTqy17_ZpPkRFf5sSkOhdYms85bu3Beu4XPBWlS4CjQsy40UdT5FCOyZXEQ1-TOvcvfQL5fvEdiG0vHQOjXV_N9hXncQup754uZwZf_6OXdbmXO44-7dQMWQXzyxv7ok-AspFiZCgpDgkxanGDL30qB5Cbud4PfwNP2m-ypNdK6RaARjbA7mA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ در خصوص ایران : همه چیز از بین رفته است. نیروی دریایی و نیروی هوایی شون. تنها سوال این است که آیا ما می‌رویم و کار را تمام می‌کنیم، یا آنها قرار است سند را امضا کنند؟ ببینیم چه پیش می‌آید.</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5075" target="_blank">📅 20:21 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5074">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromVahid Online وحید آنلاین</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4c1cd69554.mp4?token=S5P1Lb3b4bxcvrp7z0fE8UfTf_GWK8vwAxGlmqYnKLt8Q8Mri_5jdS4WjoxS1mfkitqpM3ztnxOpZIYbv0dT7I_VxHvYpFTwa_DGNEY3kwfXOgxFEqRkIYeZbe-xchWjmSEAnRQEMODsTJfVzAwQCwRGDlqQSfuG-QZ7iF6l5L-nQUonPQgd-whvrQq-yjJcTYVKExdiA2FNJG5r7E52d4DW0kLuxEuNaDBczRkCALb5Ayn6SzmCwRd2tBtmj2GlLHdDsBdEORkmXi2hMmFJaUj0A-OwlQWUU8EFB85PzH_so9svMQLUYeKKdxd5Sj3KEogvuY4TQ6Azy6he6JeNJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4c1cd69554.mp4?token=S5P1Lb3b4bxcvrp7z0fE8UfTf_GWK8vwAxGlmqYnKLt8Q8Mri_5jdS4WjoxS1mfkitqpM3ztnxOpZIYbv0dT7I_VxHvYpFTwa_DGNEY3kwfXOgxFEqRkIYeZbe-xchWjmSEAnRQEMODsTJfVzAwQCwRGDlqQSfuG-QZ7iF6l5L-nQUonPQgd-whvrQq-yjJcTYVKExdiA2FNJG5r7E52d4DW0kLuxEuNaDBczRkCALb5Ayn6SzmCwRd2tBtmj2GlLHdDsBdEORkmXi2hMmFJaUj0A-OwlQWUU8EFB85PzH_so9svMQLUYeKKdxd5Sj3KEogvuY4TQ6Azy6he6JeNJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمدباقر قالیباف، رئیس مجلس ایران گفت که «تحرکات آشکار و پنهان دشمن نشان می‌دهد که به موازات فشارهای اقتصادی و سیاسی از اهداف نظامی خود دست نکشیده و به دنبال دور جدیدی از جنگ و ماجراجویی جدید است.»
او این اظهارات را در سومین پیام صوتی خود مطرح کرد و با اشاره به گذشت یک ماه از آتش‌بس، فضای سیاسی پیرامون دونالد ترامپ، رئیس‌جمهور ایالات متحده را از عوامل تأثیرگذار بر تصمیم‌گیری‌های او در قبال ایران دانست.
قالیباف در این پیام، با تاکید بر تداوم فشارهای اقتصادی و سیاسی، گفت که هدف این فشارها واداشتن ایران به عقب‌نشینی است، اما به ادعای او ساختار نظامی کشور برای بازسازی توان عملیاتی خود از فرصت این دوره یک‌ماهه آتش‌بس استفاده کرده است.
در بخش دیگری از این پیام صوتی ۱۲ دقیقه‌ای، رئیس مجلس ایران با انتقاد از برخی جریان‌های سیاسی، آنان را به «نادیده گرفتن شرایط امنیتی» و تمرکز بیش از حد بر نقد دولت متهم کرد و گفت که طرح این انتقادات می‌تواند به انسجام ملی آسیب بزند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farahmand_alipour/5074" target="_blank">📅 19:15 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5073">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🚨
ترامپ : در مراحل پایانی هستیم.
یا با ایران به توافق میرسیم یا اقدامات سختی انجام خواهیم داد.</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/5073" target="_blank">📅 19:11 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5072">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hygQ5mGGJJhLrhBBERU9NSPbFB8CyyAp5UZxH6l8fR9OuCtjYAz2CcJtiVDb3NQ9HeKqYS3Nvxg1WjGusSEn_ex3Uzw9KubKiiZjEtcEtGTFZMCZJPvPqsxe5eQ5kMKdpl-ad336TaZ2pJFK_7r8DB5uuVaQhyMVHeH0NwrNaayaF8N0q_IY2aCiyhzpjqLkt5CCyRtB4f6CgbE4361G7Urb7XIbW3g6PwbE4U0VmcbrlLEcrBfgL5VIUX8pFylYDqBPmnX830VDs-3a9uGfV_6OzgC0SyoiQ7hjsjG-Unsx_4CR-JPa8eBlKeU4j-yDL-vLKQkF5RGd0SAOjLdM8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قراره جنگ بشه و هزینه‌اش رو هم ملت مستضعف و فقرای آمریکا پرداخت کنن!
قالیباف توی پیام‌‌هاش همش به فکر
یا مردم مظلوم غزه است! یا مردم مظلوم آمریکا!
مردم ایران هم که مشخصه
تنها نیازشون توسعه موشکی است
و تداوم غنی‌سازی!
الیاس هم توی استرالیا توی کار ملک و املاکه
زنش در شمال تهران
خانواده اش در طرقبه!
گاهی هم به دنبال سیسمونی و خرید و فروش آپارتمان در استانبول!
زندگی زیباست!</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5072" target="_blank">📅 17:32 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5071">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">‏عراقچی: ‏«نیروهای مسلح قدرتمند ما نخستین نیرویی در جهان بودند که جنگنده پیشرفته و پرآوازه اف‌۳۵ را سرنگون کردند.»
چند بار هم ناوهای هواپیمابر آمریکا
رو غرق کردند! که عراقچی نگفته تا آبروی آمریکایی‌ها حفظ بشه!
راستی این جنگنده اف ۳۵ که زدید، لاشه نداشت؟ پودر شد؟ سرنوشت اون زن خلبان اسرائیلی که در جنگ ۱۲ روزه دستگیر کردید چی شد بالاخره؟
آمریکا در جنگ ۴۰ روزه، ۱۳ هزار سورتی پرواز بر فراز آسمان ایران داشت، روزانه به طور میانگین ۳۲۵ پرواز در آسمان ایران
!  شما سنگ هم می‌انداختید، شانسی یکی از سنگ‌ها باید کنار یکی از هواپیماها رد می‌شد.</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/5071" target="_blank">📅 16:39 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5070">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uM2E5gn47OuWO58BPmmR3aw-Fg7e0b9pxj_L_QeMf135-Tkd6anpNt4Pt1RyOdphXdo_jpgPbXDVMkx9ylt_8OD2gPlBTUu5K17_6MrgwYyN9nOivsCX0cgHSlSnGI35gL6iRM1dMoEdRDEUyJytoNNnB1dFULGLLY8pKEOJ1-qPpkPaglSE7fjgFWUtNG0CHQtT8SZj66d6efq19k0tEVDZVQitfmGh0-tAIcSGpgzdA2MQI0UBdI05r41VFIcg0xwo0KKB3MYiEA-sb4X2c1scMNfNHFUf1MSUqnERf0xuIoGwEBbwp7OEoND8DTbmj2sjFJJwlZ_LRHD_cdVVnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">افزایش ۲۰٪ قیمت لبنیات از ابتدای خرداد</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5070" target="_blank">📅 12:18 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5069">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Iza42qUHUZZbXXAZC5E5hEic9RUgaHIun-J8qS9fDq11-6dLGafLaBT-xrhK9O15RN1ESyex_y8jxIgh5zxsdDkuv0G4A9X9g7QJap3ZbjgSp1vVvs8XeJ9ccjgLAC21TdgzA0cRJup94lps5KgyMj2PEZ3oBQsIaQljvEcCnMXEQOyoWTY-EmXM49tATNs8lVON2Box8FjLYqk-AIf5eU79QW_lQsgCyr2Q69x5P0y9utAaqIoB0AVxhwwVfg4OXZBaIfricgeJRjLGcHoCScxP9FiGzQHbpHs9QwjvUrLUXvvY9x_dn8VG9nq5YEAv3-jhtgMLxxrSBDM9OvBGOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شماها تحمل کنید چون ما میخوایم
۴۰۰ کیلوگرم اورانیوم غنی سازی شده داشته باشیم و «استقلال» داشته باشیم ،
استقلال یعنی چی؟ یعنی هر جا خواستیم ده‌ها هزار نفر رو بکشیم و اینترنت قطع کنیم و…. انتخابات مهندسی شده زیر نظر مهندس جنتی با ۹۹ سال تجربه برگزار کنیم و
و بقیه کشورها هم در این امور دخالت نکنن!
بگیم مسائل داخلی خودمونه!
خودمون حلش میکنیم!
این یعنی عزت و استقلال!</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5069" target="_blank">📅 10:42 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5068">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M_NJ0g3in9h3-Mu43zx-MPG7OF1I_t-d8fJkqxcsGPZtd_yhv2GnbX4GIaK-Oi49Y5Rh2FgHbZI8g7AeqWjwqzBL22WH1WMYwiRFaqLMPChITYhMetH_rBvQ0_6q8Owp9QXE97_vDOw5XmcgWbe9u_jm8dbc76GByv640CTbixmyseOdLyWvI9GpxAkbhM84YOlQJK9_sTMKhl1nu-S9GGDIOiM3j2Y7n1z41qjqV7c9xeWelrq62UvVXny2QnVHW4ZI0MH9Ko8BOjYc3677PRS3fxUuNQVFNIipsZNbUMkdula4p4-w0RlrdiFLDmkpUfY_odY9EOCbu8EtJonGow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این خانم تا قبل از اینکه اینترنت قطع بشه،  به خدا و پیامبر فحش میداد اگه حامی این حکومت باشن!  یعنی حتی خدا و پیغمبر!!
حکومتی که می‌نوشت : «خونخواره! »
خلاصه! ما که علیه آخوند می‌نوشتیم، ایشون هم ریپلای میزد و از ظلم آخوند میگفت که ۱۵۰۰ نفر رو میکشن و «فقط باید لال باشی»!!
یه سه ماهی رفت توی «بله» و «روبیکا» و برگشت! ما که «لال» نشده بودیم و ادامه میدادیم یهو تبدیل شدیم به گیرنده پول!! و دروغگو
:))</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/5068" target="_blank">📅 10:33 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5065">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GgPfykuS_FXqu_0meRwFQrfYZG-502FVOqITjaAr2BRLQc7mw7GuDu_Prkjh4zohc1kEwrzUu8GOYy-JH8mxPJMZszUWpc8ch1cWW7NigZ72T2DSnwtQNlQccKnVrh0y4roLmEOU7Xci-SazNahjrzcxouOv5VErFe0Ob5_dgvZeQg4-xdGCv06-G98AD-ilsvK8dBvJC9R3UBxoYpoI_CeTQxThO4Wry4YRCnbA4WX4TtVlkVEIWOSjPZB30Cnlf8Fc0e7jEhdDwzDyqwhFSJg2TbcS2hg7P7CvzKXxXq1m4ZKUA0-hG3o0mc5WNO8ZYyoCZJgk67hcH9lYKJTgtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/E3WR8Fg9mbaW6gkfcFn8ZcI3JOIMkyg0ss833J6WASPvkF8_6h5k3pD4h3rFjqvLze3EKrzBW76EjnvXkI1TwJ4hkeUvsNABYYFDYD87K813pPo1_ByYSW8kbcMVi2k95v-_z1mdEY22IhmT4VTC2Ff-HSBYx3imfMq6_0WAL7yOE_qfOnYed16cOdEICxWRZSEYqtXUd58HsEI-AT1_cJkaZFwY-qNxs_QrkRio35JO73Avuv2a76ZYX-Wl4d2RbExAjKODyPzqBUeR4KKs0mg9d7m3Ur2gln-H_BpY_iTLUTdNkTZY8x0lfiuKo2OWmgNVnYZ01PPq-VO2Nw4pRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/l67vbidIrF8nrH1l_wYv-z-phNSFjz7DdssAfVOyPNn181o4nRY4CDNQZN4oHoJf6N8PlgaonWo2M4C37DWvkFEwl-MGQ3gotpggM0p6k3yhKwYrpC9ooMsEoqBMOh5kPE2eOy2AE9Fd8j6feXNU-k72zLVt_jU_FgtoUQMdGEp1NYMVB1K_ZZUDvFGY1ERvBN2F1pEiLo0FzWgstEAvTZhfgpkTIYmfiPW98UkcQMqndgAKZGtKu6-sQgdYpGiB5JkLMSDK3MuV9gjgqYPWtNgEo2ECWpK8gJ8dl8Zw6vtzwmaLbNlDtVt_wUs-WzILGd_2MTtwdwinVSKJvmfQrA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">صداوسیما روز ۲۹ اردیبهشت‌ماه، در برنامه «سلام صبح بخیر»، از تندیس «مشت گره‌کرده» علی خامنه‌ای، رهبر کشته‌شده جمهوری اسلامی، به‌عنوان نماد جدید میدان انقلاب تهران رونمایی کرد. @iranintltv</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/5065" target="_blank">📅 09:28 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5064">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIran International ایران اینترنشنال</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ac9d9acc3.mp4?token=Uxovnx6I9XjzIcojAMHj8GEnHEyBcqyT_UoLmR56sw14Dkrrpq8IDcAetxnv6DXariS6Ory45_Tb-DQZ34A4l4vVPFpCiaFhKrWUV5l-qEIizkO8DRPxeDAW0EbiK50w-v_X1iSFXk3YXCLRy4jiWWRqBOpiNYma0mgagSZwwjI4WwXaavtX8Wlf8da-KarykL1WxK7UAEChxHTjBokUSjwe8W3VGZRY0shvIcKfG4-dhEjLvyGYXXJSPLAU1LDLUewiTlx-AKIRr1CgVAQqQmOy6nirTeMXo81rk1vnlx77tzMF0gqgziLEGau5HpHyExipkDuMpj02mavqP-3OVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ac9d9acc3.mp4?token=Uxovnx6I9XjzIcojAMHj8GEnHEyBcqyT_UoLmR56sw14Dkrrpq8IDcAetxnv6DXariS6Ory45_Tb-DQZ34A4l4vVPFpCiaFhKrWUV5l-qEIizkO8DRPxeDAW0EbiK50w-v_X1iSFXk3YXCLRy4jiWWRqBOpiNYma0mgagSZwwjI4WwXaavtX8Wlf8da-KarykL1WxK7UAEChxHTjBokUSjwe8W3VGZRY0shvIcKfG4-dhEjLvyGYXXJSPLAU1LDLUewiTlx-AKIRr1CgVAQqQmOy6nirTeMXo81rk1vnlx77tzMF0gqgziLEGau5HpHyExipkDuMpj02mavqP-3OVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صداوسیما روز ۲۹ اردیبهشت‌ماه، در برنامه «سلام صبح بخیر»، از تندیس «مشت گره‌کرده» علی خامنه‌ای، رهبر کشته‌شده جمهوری اسلامی، به‌عنوان نماد جدید میدان انقلاب تهران رونمایی کرد.
@iranintltv</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/5064" target="_blank">📅 09:26 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5063">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gq-j0XXSN6bZDsEesP-O0fexdAjoj7x1bYTBMbaf4VAn42mfkqs393n1TNNA4wiJYqHAO2G6gTlE3ZvtBavxfTOfED2Q1y_EMbVZSgu2vSgqq7O3uiHV_x_bVfv5AwByoeOc064nsvPxXmaV7dMGwQGinLH_iwMAg61dYP8onc7LPLvHNmHtVCviOMBr3LHTenYBO4G42AvnlwjSWi1tVKKkXLY4CTIgoJ6QKFG8Qpq9mPxNXKWFCy8dqAmmGKjVPK2nk3jeAMNUiZmQP5-_Nwqyr2y9skI35Ude1dz8gaoexMPLdWuI6gRjQepvtdMQDxzJvLVZVMeoIGf-8732gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«بهمن فرزانه» قاتل «الهه حسین‌نژاد» اعدام شد.
الهه حسین‌نژاد در خرداد ۱۴۰۴ برای بازگشت به منزل سوار یک خودرو شده بود، اما راننده او را ربود، به قتل رساند و پیکر او را در بیابان‌های اطراف تهران رها کرد.
«بهمن فرزانه» ابتدا انگیزه قتل را سرقت بیان کرد، اما در ویدیوی کوتاهی که از اعترافات او منتشر شد، دلیل این جنایت را خشم ناشی از نوع حجاب و وضعیت ظاهری الهه حسین‌نژاد عنوان کرد و حتی از واژه «بی‌حیایی» برای توصیف وضعیت الهه استفاده کرد.</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/5063" target="_blank">📅 09:12 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5062">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">روزنامه آمریکایی نیویورک‌تایمز به نقل از مقام‌های آمریکایی نوشت که در روز نخست جنگ، نیروی هوایی اسرائیل به خانه محمود احمدی‌نژاد حمله کرده است.    هدف از حمله این بود که احمدی‌نژاد از «حصر خانگی» خارج شود و پس از حذف خامنه‌ای، در موقعیتی قرار گیرد که بتواند…</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/5062" target="_blank">📅 08:56 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5061">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WQU0gMzJYmH9w_GvWcRepm6feTxbc1su_dkQiPXaKZEkt_U_EGmwPC1YNA7UunNryFk5KecWW2UahBd1xAE57YoazZeFoGOeveuIITrj2Pe5USRXbr_hmC9mv-xD3T645TFZFdLEl4G_RFprVFRLq5RzpEamoLbrfYnX6btw8XolArtfpM15Xsvyk0nQhmZszVCxzEo_rkw67tYPbUgUecYKxC6AOszLiTNL0pDh9WVTm9eOnUgx5irkj7XMoMaTvHcd0Zbs8DNKYQq_hY_SBj9M1b3187CDiMePH64vSuwvmEcudI9oUByQiEqUoQG31lIlf5Z9ozqq82Sk914FJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزنامه آمریکایی نیویورک‌تایمز به نقل از مقام‌های آمریکایی نوشت که در روز نخست جنگ، نیروی هوایی اسرائیل به خانه محمود احمدی‌نژاد حمله کرده است.
هدف از حمله این بود که احمدی‌نژاد از «حصر خانگی» خارج شود و پس از حذف خامنه‌ای، در موقعیتی قرار گیرد که بتواند کنترل کشور را به دست بگیرد.
این منابع همچنین ادعا کرده‌اند که اسرائیل، با اطلاع آمریکا، طرحی برای بازگرداندن احمدی‌نژاد به قدرت پس از تضعیف جمهوری اسلامی آماده کرده بود و این موضوع پیش‌تر به خود او نیز منتقل شده بود.
اما عملیات طبق برنامه پیش نرفت. احمدی‌نژاد در جریان حمله به‌طور اتفاقی زخمی شد. هدف اصلی حمله، یک پست امنیتی در ابتدای خیابان محل سکونت او بود؛ جایی که چند عضو سپاه، که گفته می‌شود عملاً او را تحت کنترل و محدودیت شدید قرار داده بودند، کشته شدند.
از زمان این حمله، احمدی‌نژاد دیگر در انظار عمومی دیده نشده و در حال حاضر، اطلاعی از محل حضور یا وضعیت دقیق او در دست نیست.
….
آدم قحطی بود؟ هیچ کس نبود اونهم احمدی‌نژاد.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5061" target="_blank">📅 08:40 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5060">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HWd8VsSXmRNB9uxmSoBYU6lgcDa55opydkh5NjCNbwb_NDiU2Ng35nUHwIdknuHv3GltrOlmeMrjpMt_b13N5sjMc3WCMpKQ53OFsY0sshx7Huv_LB3ez8Im-Zvw_MET6IBQNwOyJa2yPD75bSliq2X9iC2i3ZPzZUdu1QYhIYLGhYSkgNNv1v2nsUCO-cFrGb8v4z4IaSFR_6Y5gX34H10FUhcmsUEf2E85QLEf9bu_XuunPuCuofNpGXVHz3jLridSt1ODIClyPPmzg0IhVlZPEMu5uXtTa41FOuhNZl8Lup0m2HZvT4L7YrYHKM2GWrrRuMozc3T-A3l3JVb86g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه نقشه‌‌ای کشیده که یهو از  لغو حمله نظامی، به گفتن این جملات رسیده.</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5060" target="_blank">📅 03:43 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5059">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">من وارد توییتر  (ایکس) شدم
😊
https://x.com/farahmandalipur/status/2056814391148834909?s=46
.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5059" target="_blank">📅 22:40 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5058">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
نتانیاهپ خواستار لغو جلسه دادگاه خود در چهارشنبه شد و دادستانی با این درخواست موافقت کرد.</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5058" target="_blank">📅 20:59 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5057">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">وزیر خارجه مصر به سی‌ان‌ان : در هر گفتگویی بین جمهوری اسلامی و آمریکا، موضوع باز شدن تنگه هرمز و آزادی تردد کشتیرانی باید در صدر موضوعات باشه.
مصر اخیرا یک اسکادران جنگنده و خلبان در امارات مستقر کرد و به جمهوری اسلامی نسبت به تهدید امارات هشدار داد و گفت امنیت امارات، امنیت مصر است.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5057" target="_blank">📅 19:58 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5056">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🚨
ترامپ: «ممکن است مجبور باشیم حمله بزرگی دوباره به ایران بکنیم. هنوز مطمئن نیستم. به زودی خواهیم فهمید.»</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5056" target="_blank">📅 18:15 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5055">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pWuOBYxoXoU-kW72we9u5Ma7j02Yly8PBnpbc6CRh1V2LXrB6PcE56aeKXZFA-CnnuMVxALeRMYfdjtFXWpyxbeZB2-nxCQ9Qd9NLpCvFdtBRaqxkOBytibAGsSGn42E9ZQ7SigU7bu_nOJnvHeo3qtqVUMX-BJfz0N8inwSdx6BOrPzDoooKIMDAc5JXOT0lW8pUVS8jFlmGVsxhhC4JZepw1eD8znwK1bp3BObedlWbd7HBmZRId3Uxpy07NpbEuSS8XW6tgGS1d02hjsNIP1ORA1-gcdtf9Op6dYVGL8y6aGTmxd4wnRwDyp641J8odEB-A-I0KIu0qD-hUyKew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در طی جنگ ۴۰ روزه ، اولین حملات به زیرساخت‌ها، توسط جمهوری اسلامی شروع شد! با حمله به فرودگاه بغداد، فرودگاه نخجوان، فرودگاه کردستان عراق، فرودگاه دوبی و ….. بعد حمله کرد به تاسیسات گازی قطری به مجتمع فولاد امارات و…..
الان هم که مثلا آتش‌بسه،
به تاسیسات هسته‌ای امارات حمله کرد!
و حالا هم به روشنی تهدید میکنه!
این بازی خطرناک حمله به زیرساخت‌ها رو جمهوری اسلامی شروع کرد!
رژیمی که به روشنی بین زیرساخت‌های ایران و فعالیت هسته‌ای‌اش، دومی رو انتخاب کرده!</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5055" target="_blank">📅 18:13 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5054">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03ae416835.mp4?token=LUa9fblvdApfCUybwsrlGrikbDToqltB4wLLS-T-NjrJ3NRN2oEj1aJKqnlJDBXimGyFw6naC9nIcKmXUzrCiozbcwCb8dO5ZBmYNXnJNh1DsnpgFetVP-FM8wHoVzU9fILhc93Jp92LOWnDd2qV4t31bSs3Ab9FK3N312uBdU6MOCmmVGGuCdIPQ1d4BDk0cmVe5nfZssYZy_uAUpyCeo5gdwrDR5bLcAIoQAqdzJZh8PzioZDB1bNK-_RWaljzSrR8j5zxnXe7SbGp76panEIIGCnaYcmKga6SeIFTJ-jvtJlvi2MoBEdWeLYscykQXFY9c1QeSN4SM1xS5KB4rQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03ae416835.mp4?token=LUa9fblvdApfCUybwsrlGrikbDToqltB4wLLS-T-NjrJ3NRN2oEj1aJKqnlJDBXimGyFw6naC9nIcKmXUzrCiozbcwCb8dO5ZBmYNXnJNh1DsnpgFetVP-FM8wHoVzU9fILhc93Jp92LOWnDd2qV4t31bSs3Ab9FK3N312uBdU6MOCmmVGGuCdIPQ1d4BDk0cmVe5nfZssYZy_uAUpyCeo5gdwrDR5bLcAIoQAqdzJZh8PzioZDB1bNK-_RWaljzSrR8j5zxnXe7SbGp76panEIIGCnaYcmKga6SeIFTJ-jvtJlvi2MoBEdWeLYscykQXFY9c1QeSN4SM1xS5KB4rQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جواد ظریف و البته خود علی خامنه‌ای
گفته بودن : شهرک‌نشینان اسرائیل «شهروند عادی» و «غیر نظامی» نیستن!
حالا حکایت خودشونه!
که زیر دوشکا و خودروهای نظامی ویژه سرکوب مردم ایران، جشن و عروسی میگیرن!
اینها سلاح های مبارزه با آمریکا و اسرائیل
نبود و نیست! اینها سلاح و خودروی سرکوب
شهروندان معترض بود!</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5054" target="_blank">📅 15:47 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5053">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tRjqjzL2VtkOKkjNv1jw6EPaxD_IBHIdzR5r-8SGi_vCAsglKRPj369aNIzyI29ggWCvViiI4dxv3v20c0KofoItqkKabe5IUHT8gxmv-II_C30yK_KMdAWzVLr3CGGYQYOqjDlNuYAhq_Z4CWdyXJ1tKuRkAVFHdUgidJCSW71TMWnLVI__yyROJJaHqu9_ktyBhIXA6bFsylMCxvyfNSPGiJ2hMLSTfEEsBTTfE4hV9fcs7f9bWOb7-R4cufgaHbQsNJkNOe4EbVTsuRIv-USOlNlA-xwslh4WivHRRMgRf9Siar_1p_xeSYZQZ545MMR_VFAI7on6mpRQCmoO2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اعدام و غارت و سرکوب!</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5053" target="_blank">📅 15:17 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5052">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WAKKWoPGcDOh0sxFi0lob-uJnVCdv99aA8ZKty-H5dZ_WS_NJ_xEoiYN64nuFKc1rAjuKhtkc7Lvoj2uTBxJyeNI8BVnaehS5D3AozRnsHJ_CxzFzYWk0uGB13oatMTuDsXvAjs81XhJbDIae0vCuaPev4_9V4-ABkG1CHqF62fPE1SvXsOQDZlc8iDjXtFK7C-ju-3HA9PUYLgluMYS_XvEKo84Dzm5IYnFZhiZJS573a4yIZMk7a7oj-PtaS2mXxECC1Efuhq4sPers1IpFgLJ5P-DMI_U8_HFprhLVOFE2a2CwbutRU1-n3gCTHmnRAHGdjA7GX1OR_kfBPAFFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سیاست‌های ترامپ اینها رو گیج کرده ،
آشنا که «معاون ویژه وزارت اطلاعات» بود و بعدها رئیس مرکز بررسی‌های استراتژیک در دولت روحانی شد نوشته که شاید «از عقب» وارد بشن!  :)</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5052" target="_blank">📅 12:55 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5051">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UZwO8Qk2wUqMn6aRXxHXcIS-yR5U5fdW2LGXz4YyM0xfWYuUiMWzvJIq8jOPT1wZ758_1QCA1_biTbcEBhRzESDoTVGAsWB1HwucFRdZ1OQKV0yU3HOQWSHbHIt5ffkw1xILwO0SxNdA1GtTwSozr5s3Fgrd-t7QBt1ONpcFKg81iddh4haCu4pBZYy7OntATRdzBfXkaOnqJW6CCWUxScGVKy6luVgcj3gnnddLWJiZuTtkF6zUEAi3wuP8sLMFr06SVtSPmOms5ZN-2FfDOwdVuK-UJWdf3F1GrjrV7-HYJbQbhjUHLzNvVPhh4rsQfN_9uwUNbW1TvsrCprrDcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پاکستان که ۸ هزار نیرو و سامانه دفاعی موشکی و یک اسکادران جنگنده در عربستان برای دفاع از ارتش عربستان
در برابر «تهدیدها»! مستقر کرده گفته آماده است در صورت نیاز این تعداد را به ۸۰ هزار نیرو برساند!
تمام حقوق این نظامیان بر عهده عربستان خواهد بود. مقامات عربستانی در سال‌های اخیر هم بارها گفته بودند که «سلاح هسته‌ای پاکستان» در خدمت دفاع
از «حرمین شریفین» است!</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5051" target="_blank">📅 12:39 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5050">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rxm8Nk5tt3zObSiUvNoSJAdXBoayBRY0bssl3iYevnCog_YkIhM4KrRI191O1LjFUvtGCJgGhJgXJuRQ4hEBzwokLystkELkR0D3uu5S8_NSchqqJt_OOmJZOWdU7eLJdkyoRNHMh2kFDQjwzohrStpfM9Nxbtkk4WUHyFPz7KGKJip0mSVyKZmFGO4arToDwmsc_ZHntfrDmBkG9ZWixFW8fR0CVekUzY-u38eoeeaBxJEZd9zWFBJuHU5dBryC7Yngx-EFSRY7hnbN8989y-DmUe6LzlUCjvP1Uj_oLPhI5ERY8QGLpqaDyrSNVSrjv4tK2NNZ6qVueeP7pTn5lQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عالی بود این جمله :
رئیسی شاخص و مدل عینی
حاکمیت اسلامی است!
نهایت الگوی اینها فردی شبیه رئیسی است! که دیگه همه به چشم دیدیم
کی بود و چی بود و چه کرد!</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5050" target="_blank">📅 11:31 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5049">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YMNkIzAHGEu4DymtlyM2UNqemtHp-NJLFd7uIuYp4vaK6KjWr3NpHHbu-qvsyUU8GvNMODWKS_V1pj8FwC7BhMhJQJFdY6R_nEE241AgLsvW2cmuY9ptWIMnL2FxMK4smPkdjgDQo7D_8ObkHoCiBVCyiaiT0K2t8zTW0m-2VXDf29sZWsS6ExZ6kR_kKWCvhILaPp4xLrVuDLYfDKxAfb2OPBuwZFYVhJmjd3d0V32pc0H-XMw552MD59Fjp5ccKkrrauqUoN2lorFkrb6sbvoiaF3PoSqtZB3VVhfnnFY5OQPEKkbqsj-_u3eVFdJU23mqfKxKG4IyPH6JKSq8hA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تاثیر توییت ترامپ که میخواستم حمله کنم به خاطر کشورهای عربی حمله نکردم و…. بر بهای نفت در بازارهای جهانی.
کاهش حدود ۷ دلاری بهای نفت</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5049" target="_blank">📅 06:26 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5048">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b8eb45098.mp4?token=W3Hv-KDV5BmW44DKOciRuBa5Pgbbbj6Mep_unh8mt52OHGYQrCL_oxSN1SPGXZ1Sbje5XTjiey9Be9_9-PrMFlM8so1iD1Y9zuPZ5NYco6C8s-R2pumXRmqTVt7k7QwQjuzs0KV6ryK5W1j4vb-C2h3629M9ZB5rPCy-gg6npx2VNldgEcCkO6st0xcWolGHtqRHZIS0Z1AoV6ly3PTIwVUvxczU78dDY6Flpj8MttC_sR_7u0hqqSx9ECUkJqu748JtX9Z8m1kIok7jbhZP-T48etfzgQZlalJNwKXgUQBnBOTvmZ0mkIlgNhBsmYhmUeFO5zTlL7cSLcN4Xredpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b8eb45098.mp4?token=W3Hv-KDV5BmW44DKOciRuBa5Pgbbbj6Mep_unh8mt52OHGYQrCL_oxSN1SPGXZ1Sbje5XTjiey9Be9_9-PrMFlM8so1iD1Y9zuPZ5NYco6C8s-R2pumXRmqTVt7k7QwQjuzs0KV6ryK5W1j4vb-C2h3629M9ZB5rPCy-gg6npx2VNldgEcCkO6st0xcWolGHtqRHZIS0Z1AoV6ly3PTIwVUvxczU78dDY6Flpj8MttC_sR_7u0hqqSx9ECUkJqu748JtX9Z8m1kIok7jbhZP-T48etfzgQZlalJNwKXgUQBnBOTvmZ0mkIlgNhBsmYhmUeFO5zTlL7cSLcN4Xredpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فعال شدن پدافند در اصفهان</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5048" target="_blank">📅 00:06 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5047">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
رسانه‌های داخلی : فعال شدن پدافند در جزیره قشم و درگیری با «پهپادهای متخاصم.»</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5047" target="_blank">📅 00:03 · 29 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
