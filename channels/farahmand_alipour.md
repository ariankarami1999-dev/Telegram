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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-05 23:28:31</div>
<hr>

<div class="tg-post" id="msg-5156">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pw8hCPlWTLHpgVMfZiKHgPIugUEQ7gyIQZP9xgqu3GSnT_ZgmoxCsR1lMDwVlNC0lAKNvZKCw5AxurK9GkjWsuDJaFrrO_CwSBBBp98NLX2uLOmLGBjCNdkaqLQzpTOzoYIWRtrdCNHSKR1miGBK1tE8GHRxj3aT_jxxeWPwpBD8chi4L3lXmeifV2QyLiKnv7PB-PZbKg91dZEZ0kro0irSzQ0YSYVIEV75S2iSOICee3XcU4FDR7weDIusxFJiYOCdFbFu3bSpKjoPI1Bk1CiNSauc_iWSXnGfaVYipdKWbJ4GscM8fBGD-MxBjmXEf4N_hNT9CVHYTCv3k0Fqjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صدا و سیما دیشب بعد از انتشار خبر شنیده شدن صدای انفجار گزارشی تهیه کرد و گفت : منبع صداها مشخص نیست!
بعد صابرین‌نیوز و خبرگزاری دانشجو و… حتی اسامی کشته‌ها رو منتشر کردن
بعد سخنگوی سنتکام رسما گفت حمله کردیم و زدیم و…!
دیگه صدا و سیما در همون مرحله « منبع صداها مشخص‌ نیست» موند که موند و داستان رو ادامه نداد .
«مصلحت» نبود!</div>
<div class="tg-footer">👁️ 3.92K · <a href="https://t.me/farahmand_alipour/5156" target="_blank">📅 23:18 · 05 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 9.51K · <a href="https://t.me/farahmand_alipour/5155" target="_blank">📅 22:26 · 05 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 15K · <a href="https://t.me/farahmand_alipour/5154" target="_blank">📅 20:07 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5153">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">‏پیام منتسب به مجتبی خامنه‌ای به مناسبت حج: رژیم منحوس صهیونی ۱۵ سال آینده را نخواهد دید.
باعشه!
بابات هم همین‌ها رو میگفت که باعث شد امروز ۹۰ روزه که معلوم‌ نیست هستی یا نیستی، اگه هم هستی طوری قایم شدی که گویی هرگز نبوده‌‌ای :)</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/5153" target="_blank">📅 14:43 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5152">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N_CHL9RBiYyq9HxC_sWmthysfmbb5B-5OrCDN9OICEHUtJtH4UhkWEMPQp4DLV1F7X02ywjdNJGBqmVF4FmJgXGBRKr4_pnMxAlXPs8zswKgRc1anLHmKj8o-iLWWwNHIa_Yblv0w_kQMUZk3dJ4muwk8e9FgsaxlVUSYVlNFSgSPA2DsW53UsAh8-MdcY3_asLX_EHU-9N_bcV_KQu9pPC156VfyP-CyGiCDsTXR0h5W2hvO2BgPzvAP2JP1mt220VmABlMvter9ERG4m3rCyVcwOkqXzv-GSB3tVGVPauscq9_Pp855fvOm0ha4fBKIq-DYqePOEwssVF_IetiXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ذوالقدر دبیر شورای عالی امنیت ملی، میدان جدید رو معرفی کرده که هیچ کس نباید حرفی بزنه که وحدت شکن باشه!
دستور خفه شدن همگانی تا رسیدن به پیروزی!
اسمی هم از مجتبی خامنه‌ای نیست.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5152" target="_blank">📅 05:23 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5151">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N7ZbrHhWNkF6asaI_zZ0DZSVagMP0Sj1brzG9CMPzGcZvW3XpWVecnn9714yNRz7_Gj812RfCOZRs2A6u36z5kVK681YWdx1mpQXmDg7KxntxxYCwpdg2TEHLRm_iYWeaR4IgoY8igu48lrD7qmS3uORuT2an-J6XmmJxpeevTTaHKOIlbaE6G_Wwd5MAT5PRdX1T8dWSBXg4VcD38MTZmemcPd9yDI3r0hV0iKx37RRrxiGgikGQ7EcDAH9B0uH7tApvHaCncXJjbUY_rOs78UhjdP6PQXuBz1szf8zOA7691l2VYNkxrXc9XIFPi-NgDCm6On4gedIyXr-71KiOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
ارتش آمریکا حملاتی در جنوب ایران انجام داد / کشته شدن چند نیروی سپاه.   سخنگوی سنتکام رسما اعلام کرد که جنگنده‌های آمریکایی به چند سایت موشکی و دو قایق که مشغول مین‌ریزی بودند، در اطراف بندرعباس، حمله کرده است. خبرگزاری دانشجو، وابسته به بسیج، تعداد کشته‌ها…</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5151" target="_blank">📅 04:57 · 05 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5150" target="_blank">📅 04:50 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5149">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">ترامپ : یا یک توافق عالی برای همه خواهد بود یا هیچ توافقی نخواهد بود.
اگر توافقی نباشد آمریکا به جنگ بازمیگردد.
کشورهای منطقه باید عضو پیمان ابراهیم شوند.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5149" target="_blank">📅 17:30 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5148">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">قیمت نفت : ۹۷ دلار</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5148" target="_blank">📅 14:48 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5147">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GXPqqXk2dKQDnL13zNIt75kjiWPcxCnQkbopGx8QMWWVn1MYPamt2AYBBfE3XRBxl_UkAFavsSv084txQX--vD5bRa5y53e_S5nm6KIggN2-R2Mylxf1TSoOzlH2Y_yNzCBw-ohhVHXsy58xwKdRas-2PGUwPhiKvJxcIkIAb6i3PwC_043IVknCdcrB4IJZ9K-1JChqKKuF98ZwXYllo3IBnliki3aYGO4-yTl9v77TPwDWforuu2M0UyQliqMym2xtQpSDX4i0YfRqJS7kDD5uKQuaXryZ2pUP2IAS5JTTcVHUV2Wi8fLrxsuH7o4tWSuNJLloO4mPxBpDrjgmrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در حالی که صدا و سیما شیپور پیروزی میزنه و از موافقت آمریکا با هر ده پیش شرط جمهوری اسلامی میگه،
سخنگوی وزارت خارجه امروز گفته : کسی نمی‌تواند ادعا بکند به توافق نزدیک شده‌ایم!</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5147" target="_blank">📅 14:29 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5146">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🔺
بقایی، سخنگوی وزارت خارجه:
آمریکا به عباس عراقچی، ویزا برای حضور در سازمان ملل نداد.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5146" target="_blank">📅 14:16 · 04 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5145" target="_blank">📅 13:46 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5144">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">رئیس ستاد کل ارتش اسرائیل - توی این مایه‌ها -  گفته: «در پاسخ به هر حمله پهپادی انفجاری حزب‌الله، باید یکی از برج‌های بیروت رو هدف قرار بدیم.»
حملات حزب‌الله به اسرائیل رو یا دولت لبنان باید متوقف کنه، یا اسرائیل.</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5144" target="_blank">📅 13:41 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5143">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EgjpUJ_0cwWCdVN3XkpTsBIEueAVGN7ogXtoZo9OzB08jFW7eU9Qx-0-C7Fri8G3JEaX4ptI3aVewv9IpItLgmgbdMXzLYuAJ2TAErLDL0sP1aMh7TN18QvcYqA1ESah-NSbCt1Sd-ErcuikNZKgzr54ej0v0S1jo8L7P2KiNF3x3L15h23hjOD9oxq_WD530siEoj4Siiz2SHqUp8VDRCynlZvwL5YIomUO7vwW7Ekh4O91RdacU9pEJZekYCVylN2Hs4ZBqaoADbEZlb11LOkkr0mbraA-qr3I6a1anf5VOXP4ii3wFRjWCjTxl7AHmXjueTtNT4hiJERsHuLtIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صبح در ایران با اذان و با اعدام جوانانش شروع می‌شود.</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5143" target="_blank">📅 11:58 · 04 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5142" target="_blank">📅 11:04 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5141">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">صدا و سیما:  آمریکا با ۱۰ شرط جمهوری اسلامی موافقت کرده   ‏۱. آمریکا متعهد به عدم تجاوز به ایران شده  ‏۲. استمرار کنترل ایران بر تنگه هرمز ‏۳.پذیرش غنی سازی ‏۴.رفع همه تحریم های اولیه  ‏۵.رفع همه تحریم های ثانویه ‏۶.خاتمه تمامی قطعنامه های شورای امنیت  ‏۷.خاتمه…</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5141" target="_blank">📅 09:00 · 04 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5140" target="_blank">📅 08:15 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5139">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">برخلاف خبرهایی که یکسره از احتمال توافق می‌گویند، فاصله خواست‌های دو‌ طرف هنوز آنچنان زیاد است که بشود گفت :
توافق بعید است!</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5139" target="_blank">📅 01:47 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5138">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
اکسیوس : ترامپ روز شنبه در یک تماس کنفرانسی به رهبران کشورهای عرب و مسلمان گفت که اگر توافقی برای پایان دادن به جنگ با ایران حاصل شود، او می‌خواهد کشورهای آنها به «توافق‌های ابراهیم» بپیوندند و با اسرائیل توافق صلح امضا کنند.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5138" target="_blank">📅 00:35 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5137">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
اکسیوس : ترامپ روز شنبه در یک تماس کنفرانسی به رهبران کشورهای عرب و مسلمان گفت که اگر توافقی برای پایان دادن به جنگ با ایران حاصل شود، او می‌خواهد کشورهای آنها به «توافق‌های ابراهیم» بپیوندند و با اسرائیل توافق صلح امضا کنند.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5137" target="_blank">📅 22:25 · 03 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/5136" target="_blank">📅 15:52 · 03 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/5135" target="_blank">📅 07:35 · 03 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/5134" target="_blank">📅 00:31 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5133">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NPvMRMsFf4MtbUIBud1OEFn0HKPX_v1TEWilFqi-HavOfYvfE67Z25-UCtWHpCQhcCxK5DsC7mIRlnU3lA461po1NmB9eKF5c2WxaeHEuoZKZ5GKfKMXCYFEgS0u-Tim9IG-igsYwAxY4zQ4in373nv1t41vAU8nuQFWlgIe_iIGVtOF7RRGLIF8rSZ-5xjP_XN8LXlPG7DgIwocfR7kaVZLXpfxQThDKHgG7Vab5KuXuxY8DUxvovwo7v7iBtQX2JO0Zl3TIygrEESKUEuIgsSbinsNZmJAvXkHSyWvPGVATGm8hlBn1UHpKmUUSulbpn05prRi9Ve6TeGDvIhN3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با هوش مصنوعی طراحی کردم.
گاو : نماد فراوانی و ثروت سرزمین ایران و منطقه.
تن زنانه و نیمه عریان: نماد پاکی، نماد لطافت و ظرافت ، در نقطه تقابل با خشونت و توحش و درندگی
بقیه هم‌ که معرف حضورتونه، آشنای دیرینه.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5133" target="_blank">📅 22:09 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5132">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">ترامپ به اکسیوس  گفت که درباره توافق با ایران یا بمباران، «کاملاً پنجاه‌پنجاه» است. ترامپ گفت امروز با مشاوران ارشدش دیدار خواهد کرد تا آخرین پیش‌نویس توافق را بررسی کنند و ممکن است تا فردا تصمیم نهایی را بگیرد.</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5132" target="_blank">📅 20:57 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5131">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🚨
آکسیوس : ترامپ ساعت هشت شب امشب ،  در یک تماس کنفرانسی  با رهبران عرب شرکت خواهد کرد تا درباره پیش‌نویس توافق با ایران گفت‌وگو کند و نظر آن‌ها را بشنود.
🔺
نظر شخصی :  توافقی در کار نیست!</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5131" target="_blank">📅 20:55 · 02 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5130" target="_blank">📅 20:13 · 02 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5127" target="_blank">📅 19:52 · 02 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5126" target="_blank">📅 18:48 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5125">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bgBlubWdy7lFFetMjPiMBE-04DfOdiQ31U7Q1rE8vM8q9N1kXu6gD3YHeIzjNeCLR_8QWaEz7U6cM4kHU9P5o7Z5fOsQZNzDWgcVJGUgjyW3cBeBh-55pMZySwnFkoYEtFU3w6MthcaLlMsxVr7Ez556AVbqM_5wGX0imdEAWSPy5lyJjp1ie8TK-NCzBkr-YG_UzLQTPOBSOuMefEHBLGpwNO0WaWbszMEUHk164ulREz5VIzP2CbS_rxgkJjNLCt_erzXdtnQo1QFFBCbgNvXdT2XuxLc_nNS_cbS3DwyzZA5a5GQYEvuI-zWmUCkzVpwOv8M6X6F59hjJcEZSOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید ترامپ که پرچم آمریکا را روی نقشه ایران به تصویر کشیده و تیتر زده «ایالات متحده خاورمیانه؟»</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/5125" target="_blank">📅 18:16 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5124">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">مارکو روبیو در خصوص مذاکرات با جمهوری اسلامی:  شاید تا عصر امروز خبرهایی باشه، شاید هم نه. مطمئن نیستم ولی امیدوارم. پیشرفت‌هایی صورت گرفته. شاید عصر امروز، شاید فردا، شاید این یکی دو روزه، چیزی برای گفتن داشته باشیم.  جمهوری اسلامی باید دست از غنی‌سازی بردارند.…</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/5124" target="_blank">📅 17:29 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5123">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">مارکو روبیو در خصوص مذاکرات با جمهوری اسلامی:
شاید تا عصر امروز خبرهایی باشه، شاید هم نه. مطمئن نیستم ولی امیدوارم. پیشرفت‌هایی صورت گرفته.
شاید عصر امروز، شاید فردا، شاید این یکی دو روزه، چیزی برای گفتن داشته باشیم.
جمهوری اسلامی باید دست از غنی‌سازی بردارند. اورانیوم غنی‌سازی شده را تسلیم کنند، تنگه هرمز باید باز شود.  ترجیح رئیس جمهور ترامپ دیپلماسی و رسیدن به یک‌ توافق است.</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5123" target="_blank">📅 17:25 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5122">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uZm0faXYE0ahT7ZjzF_H53G-OPCyxSk-VBOC0HE3OZbzBXJ26vI7DjM8__C5HHJriCIZ1Tb-wmruL70f952ffS7HYopCCV3MA8BoTSM9DVm9mewhuSSO73i7jQELb2m1Cyyagnnzrc1hbALNFCQ-BhXd2nEn5pDcgvtyHnk_CBplW6Nj-SCxChP3CrKfImLeOTr-TtVZsyaMmCkCfpIMPTm7wzlwpJ1ZovMMivl0qXFlfDyTAmVV1MIIeAFYEYFu8-IX9lqD2sPWkGPNpgPnHBx5m-SI-SSIXwxWxrpWiPW1lY4owi2PYE2kkNe6UKktSeYZFofjV_wXkIES9mMCHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چقدر ایران باید هزینه بده برای این گر‌وه‌ها
و برای این جنگ‌های بی‌پایان جمهوری اسلامی با آمریکا و اسرائیل.</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5122" target="_blank">📅 17:18 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5121">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">به خاطر ارسال ویدئو ۲۷ سال زندان!    مجازات پدر «رومینا اشرفی» ۱۴ ساله، که با داس سر دخترش رو برید: ۹ سال زندان   حکومت اسلامی! عدالت علوی!</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5121" target="_blank">📅 13:23 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5120">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T4oAyZN1bsNyiyKGAHQ7hk9riphZJ4ksg5CZBqwbWVv36G0R3w-i2sA-Jfs0ZzZ8w92CEsysUS-F0E6koDbeLvEywV0Mjl8m75GEdTRxZ8_DLsxAfB2L8b5NHjq6UQoCrqDI3CIaGs2Cb_BWShm5tY266uhmSk3aDGORFRbqBSupb6EjrQnfpsi7XaqOS8j0sGRN7ggxe8O7MPZKD8ii4PliLpUlMQ9_fnRagm3OEtIptZEDJo05a2vtyvloD2C6L39rB5Wdd2xVXM8jngNJXuX5HDi4s8hiBYeOeiW_sJhOYtelGv9Ml5j22tmSaJJpRlq37O2UvLi5CviBUHJqBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به خاطر ارسال ویدئو ۲۷ سال زندان!
مجازات پدر «رومینا اشرفی» ۱۴ ساله، که با داس سر دخترش رو برید:
۹ سال زندان
حکومت اسلامی! عدالت علوی!</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5120" target="_blank">📅 13:20 · 02 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5119" target="_blank">📅 08:14 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5118">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">حریم هوایی ایران در مناطق غربی بسته شد.
پروازها فقط در طول روز</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5118" target="_blank">📅 01:01 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5117">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
🚨
براساس گزارش آکسیوس، ترامپ به‌طور جدی در حال بررسی آغاز حملات جدید علیه جمهوری اسلامی است؛ مگر اینکه در آخرین لحظات، گشایشی در مذاکرات حاصل شود.</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5117" target="_blank">📅 00:13 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5116">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">وال‌استریت ژورنال:
واسطه‌ها در تلاش هستند تا یک توافق موقت بین ایران و ایالات متحده به دست آورند.
پاکستان، قطر و دیگر بازیگران منطقه‌ای در تلاش برای کاهش اختلافات بر سر برنامه هسته‌ای ایران، رفع تحریم‌ها و امنیت منطقه‌ای هستند.
هدف، یک توافق کامل نیست، بلکه یک چارچوب موقت است که آتش‌بس را تمدید کرده و امکان ادامه مذاکرات گسترده‌تر را فراهم کند.</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5116" target="_blank">📅 23:39 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5115">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PXTMzUl7F3_2zCYdWll1lf4GG2Z46bEijhk7OAdPSQiFZDhr6KYA1Hwv4hSGsQ-fdXdOucbFKcJY24XRBEQ-m1zqQfogrDgaXnt7joU84xGIH0danEssbIpjqxtUxCAOBRJ9njj0oUrANJyY5BFbjZt5r7zD1krRDOLVFa6dDrpFNFHacn7d3ctBcVcX2OtLHF-QL_bRVpnRwGg_8ljrCGWDT_Xlg6zP5spKiKtVMDaxpC23wpLIwS_djBCJz4A-1WOy9nGCmHLWMVkhMaPcJdAQG9tvLTJwvwnAzlePLerFcv9KIdfkkgUYxtzgcqP41Zu4cpuHuvRQ_16KceKxnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری وابسته به سپاه این مدلی تیتر میزنه
ولی در واقع «گابارد» از مخالفان معروف جنگ علیه جمهوری اسلامی بود که الان کنار گذاشته شد.</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5115" target="_blank">📅 22:55 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5114">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WQTtk7caSampyod0s7eEaN-xt-FgryH6mM6YwclvcEqTP858s9axfF8CxBnXKxecbUtwiuWhM4MOq_jZWabkXwRdVL7NQxO5ke2MFZI3T3bTLkvEbJ-ilFFyDt4soY_5NXdguo07a0sLss8SBS_ubAP1sdyXia0LPGfb9N18XGIF9kxF8H1Oe3GSE-1n1mQMsXQdHFOZWqqc65hV5EVv2uvw962Z4XsNJDC35350TzHK1OMXxmqXoBl2lzatVCUXPPbosfyZROwbWtyTxUfA7edvq4iBqolyjxX01cQlmeN4pZDNTsi_e3ItIhXzP7I6IHipZk-tJcY8H3H76zpalg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به بیانی دیگه : توقف جنگ در لبنان، پیش شرط اساسی جمهوری اسلامی برای مذاکره با آمریکاست!
خب چرا جنگ در لبنان شروع شد؟
چون گروه تروریستی حزب‌الله حمله کرد به اسرائیل.
مهم‌ترین دغدغه‌های جمهوری اسلامی نظام خودشه و حفظ نیابتی‌هاش. نه ایران و منافع ایران.</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5114" target="_blank">📅 22:18 · 01 Khordad 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EvWf7hZY2HUcdAjMdH--4XJrrt--mcrlpPg7tRxbutk4LDPY72R9x2KaHziqG-ljG7jsoVB5HTdwNBG4SFFPnnjW6ZUJ0kabmHFKjLvAa7Rb2SCKrgTFJW5KFNtouqa_l9ZiDg-Gt69VWvm2ZTPCV86dAJCZCwtWt19K57zmyU4thFE5J91j3LIkLpH3G4Jbo2dcShxw2pR2utV2zmHZ7v_buXuedDKZqxQx29JKYlVXrRQj5hOrh1wzLcfaHqlrlrZTJNHFlEEMrAPoBDXFHUsK9FLOqCle5M5PsLTq98SvjOWT3va2k4LOSWwdX6JMlCzmq7BSROaaKnqp8IKyrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این افراد، از همون روز نخست حتی قبل از وقوع انقلاب ۵۷ در آرزوی  تبدیل ایران به یک «ویتنام دیگر» بودند، یک سرزمین دیگر برای مبارزه با آمریکا!  بسیاری از سران و اعضای بلند پایه چپ و…..  توسط جمهوری اسلامی کشته شد،  اما این به چشم خیلی از چپگرایان مهم نیست! چون…</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/farahmand_alipour/5110" target="_blank">📅 18:45 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5109">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cOS7TunRE6cEuOJdMvkI56yvJU3UAK_F4oS3lHk9uX8HvkybV2KxB__XGCdauOJLc9chBKLqIywDwFEmkxWfRqfP4pS1Jz95kY85MEgp8k5MVktnkg0AS9axdppgSjNKGf3H9MiC4jrCbP5_EouwzCvFfISThmv_rficQuIX5heihYOJI5hc73als36BnqcHYgFlylKQF8yX9z_F-pEJXr3ZQFBRMmGxHgyeZoXW2C7w6mzsBL_6Jbea0l-UlgONEBZVzs5UuU3_ZvIvXziJFA8Fc3s9sOR8EkBhxRAiPuFD9NKPPoaDSpLsRCB_nMy6OvlDtT0Eo8rVsrx_F36psw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جلال آل احمد، در سال ۱۳۴۱ کتابی منتشر کرد به نام «غرب زدگی» که تاثیرات بسیار زیادی روی نسلی از ایرانیان گذاشت!  جلال آل احمد با اینکه خود مقید دین و مذهب نبود،  اما فقط به علت دشمنی با غرب  در این کتاب می‌نویسه :« مسجد و محراب و حوزه، از آخرین سنگرهای استقلال…</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/farahmand_alipour/5109" target="_blank">📅 18:39 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5108">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eL8OcGSU6PMX8-6miklcNyedidKM1MkolZqt9k43146Td82oIPqui1ZRIpVKxv7EhBVnhLQMZbUY0HHNLbOtrpxtwoqq-eRDVzHY5WhkBST6o_nWS23FFLlJNGA4hPS_g9LhTG-6y9in6M3YBxd-qV7Ueak2Rs2D4xU7jyqONWkLfCsiAfoC7NEdeeS2-2lVSk4y6oAL4uoRfH-zPryx4oSHOqT_tt8OQC7kxK7UdMTqNY5JaECOMY2RWeoaF6mIjGi7DOB55jaJcm2qYjPGyEZyLdvFNBkPze7t-M_yxSRJBK2zcKzj5rD4P_yt8cu5dFcYMwZi7whPze-e3KaFzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سوال زیاد پیش میاد که چرا مثلا چپ‌ها،  یا به اصطلاح روشنفکران و…..  تا این اندازه در آغوش آخوند هستند و مدافع آخوند!  «ضدیت با غرب»! غرب‌ستیزی! اسرائیل‌ ستیزی، باعث میشه که اینها به آخوند وصل بشن.  اینها ایران رو سنگری میخوان برای مبارزه با غرب و با اسرائیل…</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farahmand_alipour/5108" target="_blank">📅 18:26 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5107">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jGPDfRq8c10tRoVyR-jzKO3r9ZunHl3n7fW2cphIEAEAu4j3U5jgsQQXHjiEUQckIDJbDVjrKazw8Qo_MwtqMzgVq2wrcXmcd3Gs8EcT9EZy42CFRIiiKGCcYiXwD0-7OnJAL4hMNARvOrDM3Krk4SE77SaMlNR_cZgldKm1zajbMoIOSJYG24zpwHtR_ZOcgl98B6tehksoSkQBLSKjP6nmRBoPtE3qL46pH711lf1cpPZcM7zK4Uz4rR2TDWG5W5FCU8ywNKEZYx2vM76G0tN1zm1v5RkO5pQC3PkHNxrve6QWptMatX53qA9ayuiARP05Fv087yAMiSPrvUTWZw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/9b7e3e4f1a.mp4?token=CHM5JPoIEbOkCLvrQe3Z8g6y3sWqt4fylkU0W4-JWvDCzGEXVEoP08xC-gmyFIWHkyboAwdQcNK6bFsVqtIAXSlX-yzFacyIRBbGzBp7WBFoPh-EYqajrGie9ZsLqrYgHYdNKkLH0kV-S49TOM3BeY3Rrz_fLHBEMiMDW3fyJuEQ5T2cv3bf7zBw_t8hvttBBqwyZjrm0pRG-B2rNMPXy0sgXHVsL9e1TTVQrzXCX9J5kuJmlCILOiBz3_Jt5rYswFJc61cLUqI5BpyPS3d-Qcn7jvK2zf-WK41vKisXcS0Ff67WAl2ofsTtfw3QSw2hQfAJrlVwHz8CYuEpdCxl9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b7e3e4f1a.mp4?token=CHM5JPoIEbOkCLvrQe3Z8g6y3sWqt4fylkU0W4-JWvDCzGEXVEoP08xC-gmyFIWHkyboAwdQcNK6bFsVqtIAXSlX-yzFacyIRBbGzBp7WBFoPh-EYqajrGie9ZsLqrYgHYdNKkLH0kV-S49TOM3BeY3Rrz_fLHBEMiMDW3fyJuEQ5T2cv3bf7zBw_t8hvttBBqwyZjrm0pRG-B2rNMPXy0sgXHVsL9e1TTVQrzXCX9J5kuJmlCILOiBz3_Jt5rYswFJc61cLUqI5BpyPS3d-Qcn7jvK2zf-WK41vKisXcS0Ff67WAl2ofsTtfw3QSw2hQfAJrlVwHz8CYuEpdCxl9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/d143286b29.mp4?token=StBC1wEJ9RaCuVur3aem4JJsTIBmC4e3UPjCV1OVAA_O29czYnm39urr61MMepFg_0LwfP44JSIJhtoogxiXW8aCGEXvbmyLJnsGdkPfTifiZi7a3sUu65lVWMTyd6qi3TzTGbXXXUnhiqnItrgNUA5eFKY9rpMU-Nt1rGssB5cQ3qc3T92U2p1xX0HVQRIsjXov3hzYI2FxH2_kb9MP265gVBpl1uvgcbJavWikp2fBwgviWXWNsgMhRaxpBizPZ6boKmmpgfgjZewm_tOaRQ5mCec0HQXyiJjiOUn3U79aFiwmv5ewkQea1KbfutMGuvsLe-56ovKx26gOKYcmAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d143286b29.mp4?token=StBC1wEJ9RaCuVur3aem4JJsTIBmC4e3UPjCV1OVAA_O29czYnm39urr61MMepFg_0LwfP44JSIJhtoogxiXW8aCGEXvbmyLJnsGdkPfTifiZi7a3sUu65lVWMTyd6qi3TzTGbXXXUnhiqnItrgNUA5eFKY9rpMU-Nt1rGssB5cQ3qc3T92U2p1xX0HVQRIsjXov3hzYI2FxH2_kb9MP265gVBpl1uvgcbJavWikp2fBwgviWXWNsgMhRaxpBizPZ6boKmmpgfgjZewm_tOaRQ5mCec0HQXyiJjiOUn3U79aFiwmv5ewkQea1KbfutMGuvsLe-56ovKx26gOKYcmAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cgS_JDbh7lvcR-J5Tq77HE567FT4KLwIpEpowUyKUe7_Gi5qXEncCjP_BdokV3lQu5N_ZU749AS3d4IQQUVl9oKth829q9DMoG9TVf5T3taoC5CkWsTmG8fe75qCfA_Cn3Fmejw85q-0B0mrPrbaf3QuaZ5P-5oS89sxdMFFIT1bHDZ56TkrhllMvBOEBBSmdGIUXwvW5WrOH6l8wP0RwbNbssdlivKqfslTPsFS1He3_xV3-ROJRksXdPAQpKbfFONM7P0dx1ArTB23r34EZPhHpV6Dqz4HQdrWmKHlTnNgA1UU_R-bl7Q42bMdSSib3c555Ih5vPp39j_6B9gflg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«دست خدا عیان شد» و این صوبتا</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/5103" target="_blank">📅 17:05 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5102">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">مارکو روبیو: پیشرفت جزئی‌ای در مذاکرات با ایران حاصل شده، کمی حرکت رو به جلو وجود داشته.</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farahmand_alipour/5102" target="_blank">📅 13:53 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5101">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">توییت سخنگوی کمیسیون امنیت ملی مجلس! (مجلسی که ۸۰ روزه تعطیلش کردن!)  فریبه آقا! فریب!  موشک بفرستید!</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/5101" target="_blank">📅 13:10 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5100">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BekkUMXyqSGPA0GLBMzoAs6xD6Vkm-gTHkzuiaeQGwfwy096RAE1AfwoUCKlvjUWUFzb9Y-lHP_u3BTc-VQfobAGEeFd5IeEB3FuwTHrD-yBcpY4krXXrkvErjhDgStFQRSl-TdmdyS0VZ_Hq96ptWzgX6kxLanYJid7eC2lTq5yiEBn0QsMdHA4vW3m0aOYRD_ogdT-2V8cQicwh2RAAYyk9DOSayCXDbarawKT8y6XodI7DbKroT4XjWOEd9kimykgStLrTr6u88ytcHocqK7bnOfqTPLPWTf2h_r7mStiF4h2u9KFuINDnTd-qZjPn81g873-eUgkreAIntHrPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/5100" target="_blank">📅 12:57 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5099">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fd1NHlpKoIb12wGigxdoSYgzl7U8hYoIr_MNN1a-qY8l05XMx0bdJ-v3mt5SQew13jHSq_ZoxfO3-ZUOwyaCLiei6eqUf74qH1tKuwTVJ8QfE4ms-ddJqpD03uOgBK6_Ek7kQWqrH55Jg-Bq0q_Y1gnjUlsVSL3j7peaXy8Gx8SAVVFJT5IQAp0KvYu4EYA3dFCbYb-jN8pRUb1UfQAiyc1tTruzLIftNGWO1qf3scrpwjEQJlzdzMUgVeaCAsa9SefY354rZI7vj0AwVD6IIMA4h0uS9NZx2fjT1BnDmxIM7FiZhrANGeEwGzUHnGiqvpwo1pUSNMHoUffrmiibAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت سخنگوی کمیسیون امنیت ملی مجلس! (مجلسی که ۸۰ روزه تعطیلش کردن!)
فریبه آقا! فریب!  موشک بفرستید!</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/5099" target="_blank">📅 12:47 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5098">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">رویترز به نقل از یک منبع پاکستانی:
نگرانی وجود دارد که صبر ترامپ رو به اتمام است، اما ما در حال تسریع سرعت انتقال پیام‌ها بین دو طرف هستیم.</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/5098" target="_blank">📅 10:59 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5097">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca3794683c.mp4?token=BV17NFr-cgeaUSOpLkiOcbU8b_i_hiNWe8cxzDppzUMg6VC2lpFLF_KLgkGaJ7x2HrfKrWyGWTp4FPTtuZuryusc6EvKcxUNClTEBj6317eBJmESDY_Lm0wfGeGZ0DBvNUjKb4iHZyt1WcI34-YPQYiFFX1m6yRxnSUR7iL1uPqPXmzDhTHejuyDk6xjB57V0AY-sEec_oYMsIb6vA14sGbQwObzGdYWxOB51-lZOHPTMxAAtcybvYy-71wDVWfBuG4wtddm_qTxGteHG61y_wCZehmCYXWggcy0PdU9R-kbljLRi87W6aDMbwbnjNQGu7pLjlROb6_YHznA3zlu1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca3794683c.mp4?token=BV17NFr-cgeaUSOpLkiOcbU8b_i_hiNWe8cxzDppzUMg6VC2lpFLF_KLgkGaJ7x2HrfKrWyGWTp4FPTtuZuryusc6EvKcxUNClTEBj6317eBJmESDY_Lm0wfGeGZ0DBvNUjKb4iHZyt1WcI34-YPQYiFFX1m6yRxnSUR7iL1uPqPXmzDhTHejuyDk6xjB57V0AY-sEec_oYMsIb6vA14sGbQwObzGdYWxOB51-lZOHPTMxAAtcybvYy-71wDVWfBuG4wtddm_qTxGteHG61y_wCZehmCYXWggcy0PdU9R-kbljLRi87W6aDMbwbnjNQGu7pLjlROb6_YHznA3zlu1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5097" target="_blank">📅 10:27 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5096">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">قرار بود امشب و در ادامه تلاش‌های پاکستان برای میانجی‌گری میان جمهوری اسلامی و آمریکا، عاصم منیر، فرمانده ارتش پاکستان به تهران برود که ظاهرا این سفر لغو شده.
رسانه‌های پاکستانی هنوز چیزی نگفتن. اما العربیه، خبر لغو سفر رو منتشر کرد.
عاصم روابط بسیار نزدیک و ویژه‌ای با ترامپ داره و غیر از این، کشور پاکستان نیاز بسیار شدیدی به پایان تخاصم در منطقه دارد، به خاطر اقتصاد آسیب دیده‌اش و…
اما به نظر می‌رسد که عاصم منیر به این دلیل سفر خود را لغو کرده که چشم اندازی از موفقیت و دستاورد، برای سفر خود نمی‌بیند.</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/5096" target="_blank">📅 00:33 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5095">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d3-mEH5xB6zj1ch1B5UCmBBzaDtzD1f0GnXcYI9aWTcqr9J1vj41WqWA3gVGQhARZGWEn2tyhK_ZMmVthEzXy8uuTdkBKpgY4935mv0Ta2y7iVAbDyI9aonmww9DW5-p-a4g6THnMvMYTI22esHtXgkA2aG6_dON403bt-8EVF3VDod407MV6fLt_6MohpIxSTKtw9o7Rhy5LeHjSX0tJph5Ey4Ze8XMhMUBSNqaY6-UeHGW3DR5oJ0KvFD7aYh0FgB8MKQIw4E1xZoU-CjwEiTY6of7tS_zcM-9mslQA3kInAy8362aBRue4-p4mV7oZWgtHHfDynqi_HAoIiDCJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5095" target="_blank">📅 00:23 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5094">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uvZHmCF8PwJ31ZTGMMuBT9xcfpZj63-di2Q3SHFUQ92NUrCBkOiI4r30CYGe_IhU_KdBrcSLkw4Vx9c9Ejs_-LBYhKCH0ANbWU0d4xNH6gapsOSddaozqpjma5vl-wSRrxZaesZ7V3wOd1LWaVz98H_6cwUalyo2geUPQjO52CYOLKH7gCghtgyYy537dMaMZK72XCPfO5pU_Il95iuZH7Byb8c9y1PDnqi1uorZCUtYeavoNEm8KxxaFNfX-9__3BkgvFIgpjVOHlqNaAIOssyKosh_R88anHZG2r1nNLtiZ3YVc1Jy2caeAzg4AvIP9_6VwK_bhck-i_-Ct_LM2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از پیام‌های دریافتی</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5094" target="_blank">📅 00:23 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5092">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/euYPHFGfHF0ZIFehVBNUdn534YDIRPfFGOA1nij2Ho9qu61D2rN-3DcTO-N2fw0H6DkN5mWlD6FdB-Q91OlMon7ia55h3R3o-ZM6LB49-k5zjC3GthDWuBW0KOQxgxRBtRq3pZqlWSWbw_1WAdlqn4Y0pOBqkZbFVMkNeiLi7vIYZoEv2lSyPSYvlJ6O885kOamIfnvoypw8ouaDPC6j4WFLRBlUq9TTnLX2SnZFm8CNHxnZnqk93E2BtRjg635qdM4-F6nI3nmrau8cyakL_WLFibspwFourBx1cvflfDZlQsG60hURXX0auTXxZewzWLlA48L_K92c1fGxkVIZmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از پیام‌های دریافتی</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5092" target="_blank">📅 21:15 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5091">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tnUYgAy-fqJsX_Lve3CRCrnCjRbTSxTaZdC2ddY8OnzJY-LfhQrDZuvFSZ93xp6xepDr1z3TnOoxuyjSVKMvp5rNnauazp2GLShFa2g4WkkeZWQpOdj8occcYhNXPM3OE4RUpPYyzJhLrg4vOZ9doNF-shKoDw1kpd4KEYRdsxl2t_hChBr2dPi-yExJOPqMbuVoRjWQqNmuVpN-HvT-OMX6rMnrbYs4vjjGnnqs6YhWQjOLhZJVvn32Xqk8mP4ZSD1QC9JKAQf9us5-iflyv1u_4MqG2zSN92-XPC7ndRpiQR0ZJWgZoiHtpwRT4EnOWD_D_iXzILcbICgFlpBmFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر بار مطلبی منتشر میشه که نشون میده
گزارش نیویورک تایمز چقدر بیراه بوده و بی‌پایه</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5091" target="_blank">📅 19:37 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5090">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VdHgfErsSobyUztMAy1a8avYBeQLUcKULaP4TBmhco00LgwQgPnhWSCF4sYN1MC349suBOKWVXjutfOieXG7HXod_ETyq0DcxKqydDWFxff82wIbUBoil8jJ_1J1jNF6utPlV5eM3UyKB2rzOggfnFgjyDDsvp6E2mHnvFZfvimTwY5ypeolEWfuYj28H8Gl2lDJVToB3tTQpxoBgOauQ_8gDsPl9MWOsZDKuX084YgVN6aDaIh7IDAEaiXfWYGV-rsa8E80igTidvEhy4NGfsCyO5sDgt-Z4FU_YPIapYBgA14IliUnVAuqrjdHmiY9C2QQ7y2FDCDP3sio_Y_Lyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی رسما بخشی از سواحل عمان و امارات رو هم تحت حاکمیت نظامی خودش ترسیم کرده.
از اهداف اصلی این طرح و نقشه شهر
«فجیره» اماراته که برای امارات راه تنفس و عبور از تنگه است.
تنگه هرمز، تنگه احد شما خواهد شد.</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5090" target="_blank">📅 13:02 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5085">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kfmEobHlRdvoGQLT3pCCeseIzZHUH4OGlMuNdwTQFYJix04lJa77L77i3yOcWwQ5ki0Czt7jhg_BIp6fi8JEaesQOMHbeEQv18uiIXYL-aj8pzyg5wU1SRIO7bpT4utX3e2BrquJ2FTlb7k2VVedHT2o6_OZ44jkybO079vPVHkZ7kh_NOT1E51vL_GEowSDD8O3osAnlJpfeVzKbNuGQpl1j5uvHhJjKVYXoyDAn5M0OXV6c8NNDe2FURT51TnOEJMs4XiTldsLerJa6FfSVXnKo1yGjtdr6a4tYSsRN5TCn3K6jNjFUw_0-r0h0sZsKGybbZE1Vd_uVEf1hrqT3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Nba5VhY45ERNj9B2tlpcAFNJhc7rCl5WKOY7MxPK-4Z4F8CvjQFHzcwpK_vn2buDTzKb43jT4qj0rRSPWS9B9iJZDuhO1nvwDrVF37No7hUKfL3fXS8chD_Ey8fP3-vc5CgMmVzgmE7GwFKnXMdWMbDkD5vgexkYle61Dhmyx8VlBR2niwTjGQ3P30vuwKo1GedBsynfKw94RCCxwNEkX2re8rTZIvLcBC882hzeX3JFCcN7EM1w_I-Hb7XGmbvqP6G1uCXCTR6kMijlOlaAHg5DeMvokjUMY0C5GWzr27Vk_ng5BtP896WkCd5N8dwNHJK4_j7n0DEo7_xs39Sfvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VmkkXeIlpEcNWtGD6S3P6piIE-qLeAbkvvfmXT1fZHIr84yeilFPpfE6d4v0dW0yjZ-rTzcFpjiINpTM8QimI3_CqLLoKEp-ahIbtBN14KXesMUvzcXYBUYl8rMfEg0d8j9adKJqPBDk4PdMbawFvAQMcoyJQAidOiB17lXEMOcqZ8bYbkOQyrQVy6RcseIAfP8_iI4fJo2l-u7c4oE2NyFqnSV1SmLWEjoCjvUS0_JoQHC_no_deSzvaowEtbliVrx9zu80XnWQ-hnOmQIjec-juyE5VFAw_7Pill0JmO5BayqG6wgh0HA-ZuuW-mJZUEXVFhB02wodt71sjlrVMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IKiu7AH_OJiIeoi0Ibc0NHOkuqbuJgPnBeXtvpQX02LlHkfRfHDsEEDJ5Z82xFxYov3l4ozlgSZGYFWm6kOcvENkQq8eP0N5e9h3EzkeoBoK8raKKHLYP-MIwwtBOjAaWLp_h0KOrBUsFwPNP_ZlnO_OCNCAcNp2dB6_MEobH0dHjUcmOP7rogWhkTRpz2zQ1TFcplFyusg1nGXB_as-pFSil2I2gEyNSDX8CNYbsIJgy0zs1VmmgKXgbFVwCsrNr_0KnnfbgyASwgOO4mdZvFsb1r-f27n_siZ1VvjG3BYU1xqDS9MJCF7kBwsUvM9dbKNcPpmT2TYe5VQ_mjM0Rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qHzlnblv-hwmUYOETGVezdB1e-hMtq7RQHlhM4tUsceLIbXNILhGD0Kzz-WZCKpQXhkwJEPQuLnDcavzGwdnR4MW9LPBoIDik91xpxWLktv2EIG9YFGEGOsn0y3izgZlVk28Bt8YnUm0LYkIJ4PT09fGc6hZd0-3-a3_tVZ5BeglSEZNe1SQ4ptuSsR-VtYRvuiOrxsgBQ6ys0SNN6QcpdjuJM4wp3kbKAey0JTU5v7lh2ZZ9Rk6Q-pJL514KnXEq-XnhJHWWYfURvfI_KZdIhiqu8T0_qdw5kBo6L1dargPVbX6S6blDSHYal5eI_HoW2ZefrK9UDUWq0MMGy_lFg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">'من وطن‌فروش نیستم... زنده باد جمهوری اسلامی... تا آخر کنار ولایت می‌مانیم... این پرچم با طوفان نمی‌افتد... سقوط این کشور را به گور خواهند برد... عزت این ملت معامله‌شدنی نیست راه مقاومت ادامه دارد...'  تبلیغ «وطن»دوستی در «کشور جمهوری اسلامی» با شهروندان وارداتی…</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/5085" target="_blank">📅 12:29 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5083">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NueS3WxztHPVSF4wEsZJrl9XXMxudSex8BrPXeEHebWEbZuMBqWLZ2JKUHRJgArmL1gCPnmV_Sk0G3Dyj8NpG_ZrwMAiVheUYHN9HHX8vu0qnXV8UFBIhp_gkUTqP-gNVQcfv1nEdwBUhuBTDR-vlW7ga_JaK01T75sEfF8KlBVMEhIcnW5LjCgKCP24LyNQXLwquyO08xHPRE6FQQtndNpVIlAHiq845gPZ0HTu4b_Wu0IPazH-TVsOjEIlnaoJvUmCz6znNa4wrg0McE-3f3Pw7sDtOTIwIspY9F-NrAVwNYTpbcvMokgkYjdndcRgmWgXOJ03F9sbD0cmGL1e1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54c0c9f59b.mp4?token=IP5ej42K3KT4lIdhdup5hg5Qde8T8UiWPNeWoPb_uyzotK79wOfXIYVrN06f8mm7qkIQBS6JX9yaAKJwixYp6l5veNtOG8tpEZ2klKImaX8_zQFA0yUk0vBd5vT9cZoVNtmnGRYY-r0eWALSElmAt-fdI2Et-ikxrGicgmkPQytBRx7azr85rqRLjNzrTvdqXNjsYEGnxtSbbPHB1QkEJNWkW5MrOejcDJxjDajWdX7xi0d7kIXpr20ptF0e1ysLTodyOLK1a3TIB4CbtkEI50DSZS9I71g_Fkp5vImtQl1yD1H_X0xyU1W7js34ekTEHN4pxc3qnxCdhatRnnZTwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54c0c9f59b.mp4?token=IP5ej42K3KT4lIdhdup5hg5Qde8T8UiWPNeWoPb_uyzotK79wOfXIYVrN06f8mm7qkIQBS6JX9yaAKJwixYp6l5veNtOG8tpEZ2klKImaX8_zQFA0yUk0vBd5vT9cZoVNtmnGRYY-r0eWALSElmAt-fdI2Et-ikxrGicgmkPQytBRx7azr85rqRLjNzrTvdqXNjsYEGnxtSbbPHB1QkEJNWkW5MrOejcDJxjDajWdX7xi0d7kIXpr20ptF0e1ysLTodyOLK1a3TIB4CbtkEI50DSZS9I71g_Fkp5vImtQl1yD1H_X0xyU1W7js34ekTEHN4pxc3qnxCdhatRnnZTwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حاصل ۱۴۰۰ سال علوم اسلامی!
علی خامنه‌ای هم به صراحت در یک سخنرانی «اجنه» را متهم کرد که با سرویس‌های اطلاعاتی غربی علیه جمهوری اسلامی همکاری می‌کنند.
در زمان محاصره اصفهان
توسط ارتش محمود افغان،
روحانیون بلند پایه شیعه، به شاه صفوی وعده دادند که به زودی ارتشی از اجنه
به یاری ارتش امام زمان (ارتش صفویه)
خواهد آمد و شورش افغان‌ها را دفع خواهند کرد.</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/5083" target="_blank">📅 10:42 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5082">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/add91fa506.mp4?token=NcGDhrGccTqKTQpKPo6R-Ct9P9gjW2rRmXf21AoSwRyDPBiWoFKG4ftd3UARBtI2n2WQi560n3I3o7yIyXWKTL8ntXlFD6yDq1lTqRWfnUpfL0T_Q7Rj5opHaQCA3nOENPbHPGfNHtZYBNzT4RvXaEpGHBJmEfMyyA30qM6kt23lH81uhGzVCB4ic-P2HZkYNGIIKuufXdj2irNsxh7TnffpEQSZz43Z1HVZ_gQR5WKKQBiWYkL2XwzFDAxEMBEpaMy27nKBqiJMM4wHGbmhSTiTcw4gIOFbLhPXKfMn7BjNeyRFINuBxCagWiIVW7YYQS5uHB0_tQRWAf11Gk4qoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/add91fa506.mp4?token=NcGDhrGccTqKTQpKPo6R-Ct9P9gjW2rRmXf21AoSwRyDPBiWoFKG4ftd3UARBtI2n2WQi560n3I3o7yIyXWKTL8ntXlFD6yDq1lTqRWfnUpfL0T_Q7Rj5opHaQCA3nOENPbHPGfNHtZYBNzT4RvXaEpGHBJmEfMyyA30qM6kt23lH81uhGzVCB4ic-P2HZkYNGIIKuufXdj2irNsxh7TnffpEQSZz43Z1HVZ_gQR5WKKQBiWYkL2XwzFDAxEMBEpaMy27nKBqiJMM4wHGbmhSTiTcw4gIOFbLhPXKfMn7BjNeyRFINuBxCagWiIVW7YYQS5uHB0_tQRWAf11Gk4qoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یادآوری :
در پی انتشار رسمی خبر کشته شدن خامنه‌ای، در شهرهای ایران جشن گرفته شد
و ویدئوهای بسیار زیادی از این جشن
و تجمع‌ها منتشر شد.
و به قول این مداح
«صداش عالم رو پر کرد»!
حکومت از همون موقع اینترنت رو بست.
تا الان جمهوری اسلامی بیش از ۴ میلیارد دلار به خاطر قطع اینترنت زیان کرده!</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/5082" target="_blank">📅 10:32 · 31 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/5080" target="_blank">📅 09:31 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5079">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/48d635b5ce.mp4?token=vHVh5FIj2m6A80TfWVrLw8EBnz16J2_z45x3LxzN-72j9M3UNMscMsrpllvPWayq2I_HTMAEqo_Ngpt8jCzBtnIACjM6lcFPvziNEwJ2hrDbseihBJICHNaOzbwgRHEuP9Z2CwC97JotHPM0psem4itTTqhhXfP0lxDmJPp2gLEIESXx_0Rtk9mDe4Gi0ReIeKKwSnsRIqnm9AVZVlS28qJCejs7dVD6tFEj_sPLB2KXXp1rnysM04Sm_ZdR-_KhWZq791KXc2xS5o22qmMdQvBsYJB_oyLLkMj90BHFI1b8OghshPqUDwQaWKsiL_ril6w_pbButybI4PxzOQGmqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/48d635b5ce.mp4?token=vHVh5FIj2m6A80TfWVrLw8EBnz16J2_z45x3LxzN-72j9M3UNMscMsrpllvPWayq2I_HTMAEqo_Ngpt8jCzBtnIACjM6lcFPvziNEwJ2hrDbseihBJICHNaOzbwgRHEuP9Z2CwC97JotHPM0psem4itTTqhhXfP0lxDmJPp2gLEIESXx_0Rtk9mDe4Gi0ReIeKKwSnsRIqnm9AVZVlS28qJCejs7dVD6tFEj_sPLB2KXXp1rnysM04Sm_ZdR-_KhWZq791KXc2xS5o22qmMdQvBsYJB_oyLLkMj90BHFI1b8OghshPqUDwQaWKsiL_ril6w_pbButybI4PxzOQGmqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">'من وطن‌فروش نیستم... زنده باد جمهوری اسلامی... تا آخر کنار ولایت می‌مانیم... این پرچم با طوفان نمی‌افتد... سقوط این کشور را به گور خواهند برد... عزت این ملت معامله‌شدنی نیست راه مقاومت ادامه دارد...'
تبلیغ «وطن»دوستی در «کشور جمهوری اسلامی» با شهروندان وارداتی از 'عمان، سنگال، غنا، کنیا، بورکینافاسو، ساحل عاج، نیجریه، تانزانیا، مالی'
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5079" target="_blank">📅 09:04 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5078">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nez5l8gQoacNembMV7n0QfQqTOWOE75yo4-d8gBU-FJGnIjjis9IU5WvwDh8YPr_wP_QVMvRWJ8nAS4iYVUoI4gilznPe58rX-c9OCKu4SLYYWInK6mvD0lmqibX_TSbWQ7OgQfJU2INslmjeEkdIxKOf_gHj4iXS3AhvgLUb59w7XScONWDQzAKG4NTJ0fXsMxAZBUpNCQNM75XFr6MeDOlHPbxg3zUk-uSEQZP-QodHQcs6qBSXbBHDrrRfdgmvbdKTzfoLHTuK27TTOxsvkRghESWLpjYJeHszFXWlXuGZ_rJ3R5bRRme99ktpD4Kbe4EnrcdurdYkX28slodUg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5077" target="_blank">📅 23:07 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5076">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">به گزارش تسنیم آمریکا پیشنهاد تازه‌ای برای جمهوری اسلامی فرستاده</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5076" target="_blank">📅 22:16 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5075">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e76a3523c2.mp4?token=h_Q4WMd_C9jXyD163_BmBgafxgKox_gim68-D6RGSy_D3oKy21RFhPzUPsMiecMPuoZr-_wXhwWigcH_gtBrgMZudej-HU2DVrdk7RN1jIjM_VhkZYwbf42m_cylVhzH4yZCGXL_YbMTsXSt3TM72xLrDWzFwKeUipkikvdPYxKFdUHQ7fbTi7PeitSDk4HJuqjyephHgitAcO3NQ2b3E_9dn0hKZKNEBXJKtpkOgZOMa4YWpXHs5TJ-SjAWQYedzIK_cIMRs0nHYegWpZZ-VTPpvt9HwyJDe6cv8ka9mjJiNkS1YEjub0Yc2z5kI8lZ_xfVvyNZPNRtwpgbgjQ6cg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e76a3523c2.mp4?token=h_Q4WMd_C9jXyD163_BmBgafxgKox_gim68-D6RGSy_D3oKy21RFhPzUPsMiecMPuoZr-_wXhwWigcH_gtBrgMZudej-HU2DVrdk7RN1jIjM_VhkZYwbf42m_cylVhzH4yZCGXL_YbMTsXSt3TM72xLrDWzFwKeUipkikvdPYxKFdUHQ7fbTi7PeitSDk4HJuqjyephHgitAcO3NQ2b3E_9dn0hKZKNEBXJKtpkOgZOMa4YWpXHs5TJ-SjAWQYedzIK_cIMRs0nHYegWpZZ-VTPpvt9HwyJDe6cv8ka9mjJiNkS1YEjub0Yc2z5kI8lZ_xfVvyNZPNRtwpgbgjQ6cg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ در خصوص ایران : همه چیز از بین رفته است. نیروی دریایی و نیروی هوایی شون. تنها سوال این است که آیا ما می‌رویم و کار را تمام می‌کنیم، یا آنها قرار است سند را امضا کنند؟ ببینیم چه پیش می‌آید.</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5075" target="_blank">📅 20:21 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5074">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromVahid Online وحید آنلاین</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4c1cd69554.mp4?token=vJ2Zva38S-hOzrlmlU35_9bkC9ME4294WyUhEUc_DlbBPj0SqLBYETzFB2lgxWWR9CR9_rdKYYXoBSE-C8kDtTtHe7rYL-VFzidTeKiaUvxm7YhIelqI5z7QivOikLji4WmTQDgbb_5VKYdS4zvXr9B3HmFobwYVEQbP81mWDgVcbgNJttZclW3cW8cSqPJss5_ej5CjiHLjMOncpQJgXHd898ZgaoCgHUTU6ujZySzI8qBwGQUN8H_YbkLReLmYWOX3A9BY0Tl93kdRE_NuBwapn2lc1oe9-ZH9qCtpSgL8z0Wn_f0pqD7MhZdxCk8BGK3ovLWW1ky1ZDvlIWYU9A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4c1cd69554.mp4?token=vJ2Zva38S-hOzrlmlU35_9bkC9ME4294WyUhEUc_DlbBPj0SqLBYETzFB2lgxWWR9CR9_rdKYYXoBSE-C8kDtTtHe7rYL-VFzidTeKiaUvxm7YhIelqI5z7QivOikLji4WmTQDgbb_5VKYdS4zvXr9B3HmFobwYVEQbP81mWDgVcbgNJttZclW3cW8cSqPJss5_ej5CjiHLjMOncpQJgXHd898ZgaoCgHUTU6ujZySzI8qBwGQUN8H_YbkLReLmYWOX3A9BY0Tl93kdRE_NuBwapn2lc1oe9-ZH9qCtpSgL8z0Wn_f0pqD7MhZdxCk8BGK3ovLWW1ky1ZDvlIWYU9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمدباقر قالیباف، رئیس مجلس ایران گفت که «تحرکات آشکار و پنهان دشمن نشان می‌دهد که به موازات فشارهای اقتصادی و سیاسی از اهداف نظامی خود دست نکشیده و به دنبال دور جدیدی از جنگ و ماجراجویی جدید است.»
او این اظهارات را در سومین پیام صوتی خود مطرح کرد و با اشاره به گذشت یک ماه از آتش‌بس، فضای سیاسی پیرامون دونالد ترامپ، رئیس‌جمهور ایالات متحده را از عوامل تأثیرگذار بر تصمیم‌گیری‌های او در قبال ایران دانست.
قالیباف در این پیام، با تاکید بر تداوم فشارهای اقتصادی و سیاسی، گفت که هدف این فشارها واداشتن ایران به عقب‌نشینی است، اما به ادعای او ساختار نظامی کشور برای بازسازی توان عملیاتی خود از فرصت این دوره یک‌ماهه آتش‌بس استفاده کرده است.
در بخش دیگری از این پیام صوتی ۱۲ دقیقه‌ای، رئیس مجلس ایران با انتقاد از برخی جریان‌های سیاسی، آنان را به «نادیده گرفتن شرایط امنیتی» و تمرکز بیش از حد بر نقد دولت متهم کرد و گفت که طرح این انتقادات می‌تواند به انسجام ملی آسیب بزند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farahmand_alipour/5074" target="_blank">📅 19:15 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5073">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🚨
ترامپ : در مراحل پایانی هستیم.
یا با ایران به توافق میرسیم یا اقدامات سختی انجام خواهیم داد.</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/5073" target="_blank">📅 19:11 · 30 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5072" target="_blank">📅 17:32 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5071">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">‏عراقچی: ‏«نیروهای مسلح قدرتمند ما نخستین نیرویی در جهان بودند که جنگنده پیشرفته و پرآوازه اف‌۳۵ را سرنگون کردند.»
چند بار هم ناوهای هواپیمابر آمریکا
رو غرق کردند! که عراقچی نگفته تا آبروی آمریکایی‌ها حفظ بشه!
راستی این جنگنده اف ۳۵ که زدید، لاشه نداشت؟ پودر شد؟ سرنوشت اون زن خلبان اسرائیلی که در جنگ ۱۲ روزه دستگیر کردید چی شد بالاخره؟
آمریکا در جنگ ۴۰ روزه، ۱۳ هزار سورتی پرواز بر فراز آسمان ایران داشت، روزانه به طور میانگین ۳۲۵ پرواز در آسمان ایران
!  شما سنگ هم می‌انداختید، شانسی یکی از سنگ‌ها باید کنار یکی از هواپیماها رد می‌شد.</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5071" target="_blank">📅 16:39 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5070">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/usC0uJHng-w2_rrOKJmpbVQjOYF4MvERHbzzzLRnbMYqJiDlxzqjPWGxnKxBaTFrPodwns5OB4LF43pnX6FxJz-jrgJ_8t_GHE1v1Pqbt48UcY_BSsZl6YqQyPsFrLNmdQBbbs5_7wSr53Ka9WLZeeoonRtTw2zWvZEB7tlwbIEDABqfpEPT8Lr7sh0IauV8zzMP96CYDIhz5HN1x4iLcyMn7nKMjKwGQKFzwnhYcDXMF96egRvKE728uCT3cRqVkWl1--_yTdhApcx8zj1bRgrZN2bBpYJ4yvJ95Io3q7aJkhMKUrm_NCQwKePAd-G1_0JZYqtwkf0-yRYsuR3rcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">افزایش ۲۰٪ قیمت لبنیات از ابتدای خرداد</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5070" target="_blank">📅 12:18 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5069">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nK-1I3hP713tddU9Erohjw3GuGLwk_jmNNzW-C_F_VkpuQbRkcpuzp4nJk33pGwrlojid731W5A-A9mXqOxgD90-XfDtV5T7I7C-mUNenBaySbeO5PLY_fvrJfQgKh-0qBsORUBNmJ-M7Ej3sMD0dmvkC6pF1Ukzvi5pzqAatVQ9Rplog3UGxF3J8usNVT-mP-upFBLMtUP5I7t69BxS_1uazfGAfxIyezJs07S1dMs33aT88vnAEORN3sRnf18hfuD-SKKTm4qfN9rtFW_Sex3SYt73k4JVTRd_0rvjBGATlkHy8em2zeqspSEkptxm0aowIBgAMzTQDEw2ggjJ7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شماها تحمل کنید چون ما میخوایم
۴۰۰ کیلوگرم اورانیوم غنی سازی شده داشته باشیم و «استقلال» داشته باشیم ،
استقلال یعنی چی؟ یعنی هر جا خواستیم ده‌ها هزار نفر رو بکشیم و اینترنت قطع کنیم و…. انتخابات مهندسی شده زیر نظر مهندس جنتی با ۹۹ سال تجربه برگزار کنیم و
و بقیه کشورها هم در این امور دخالت نکنن!
بگیم مسائل داخلی خودمونه!
خودمون حلش میکنیم!
این یعنی عزت و استقلال!</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5069" target="_blank">📅 10:42 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5068">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RL1DJT7lsuJ9T6_oFL_sZQuMqyhThRLG5IrAjgtMENl4jHedECUXPc3WqgyhNtcf7aQl-_KakS8LTijGZJfIOyp4o7_XK406k9xDveJk9z8p1XkqZgj14kg7e2exkD918oO3z0XJH_R2OwdDltVoArToAdbT04FnkLRf4LfEjQccVqI4DvC_9xzJ6hDKUaSx-H49gcsCwdmK7iaP9Xo5zhMW6R2F2yroeLjD5czWE5xqyS_aZWuJTD3V-J-6lUx1aTNGDoHRuQY29Du_vuV_4cyZIp_Irgq9eufWB7UVq7mRRb8Fp2JI_BCOVljllAUa3F2YVrrcH_Z8zC3txV1Lsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این خانم تا قبل از اینکه اینترنت قطع بشه،  به خدا و پیامبر فحش میداد اگه حامی این حکومت باشن!  یعنی حتی خدا و پیغمبر!!
حکومتی که می‌نوشت : «خونخواره! »
خلاصه! ما که علیه آخوند می‌نوشتیم، ایشون هم ریپلای میزد و از ظلم آخوند میگفت که ۱۵۰۰ نفر رو میکشن و «فقط باید لال باشی»!!
یه سه ماهی رفت توی «بله» و «روبیکا» و برگشت! ما که «لال» نشده بودیم و ادامه میدادیم یهو تبدیل شدیم به گیرنده پول!! و دروغگو
:))</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/5068" target="_blank">📅 10:33 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5065">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HZzJj0phLjNWas1TJkqVTlkDbOme1nK3tHRGzp3Lc0Tmuq8vpwZylmXoZgCcj_xmrXfhJG7vF_y8ZIzGC0Yy4wuhU4F-_8RbP2eZNLoV6OlOQir6kykquhhlYQuT6H7-dD35XPaL3KkQm63cJC4dgZ1-s5pTSKWixc-tmW9W7j1WZYnH4eniUWdW1AEp4HAabam1om-iS5jzrIR8pA2SJBw6g4iJLS0tnOImB0iOOvlzdryZSRmFb5yeMIBgOA1cEbNX4SMffOBBlJYMEcgZ-sdTmicZI_ThAr7TOlZ80R3AnEh4zc7rbscgyhObDdPRpmeMIBiZiGMQ7jJugr-fYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/c75dYXrlmBdMwEcPX_i-CwavZcNwZ6R5n6Ca83pngAVz7K4T6plf1DJbglz9G55ykIfjLQYjr74BluQNB3kCRPJmfek9N0vyPXru_9XzL_z0Cw9lonONpACWROXlr1SXUlqdg-3_viQx2tdwRf428JnrE7jz8Yt78wce98CEw3HB7RlAHP4x4hmm9EXbVW2fYlAPO1WOpobpVou_ZecBH0_CkQOISN1Kzi-6oo-7-7lkTtiGpQ10zdnJnCAl8aPCnkER6_ujrBDkKCCTzK-HNhCVuB2R4fl5KOHPFdOW29sjURju0h8vdwujyarfZcAwNQDPakKupTwoe1cVwKG9nQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/5ac9d9acc3.mp4?token=dLHt6GEpSC9CdfSeVzcn3r07J0tDwhkFgnTJUIDPYncgfFXKdjzdWyhh_BpcQlTvsCebUUsksheY1LS8NKm5zLrM27g204CB6RRuteWzTz5c4d6PrL1tw5L8UXY59AzC3aZXyetb-vDKaTK8t5dLvKjSDLOolOXPTU93F7goQSLUTBzLq2mtYtIqaxZWMFKPpESK3WsgZZpeLz1F0hwTev0ssMyTQYV0Mpin_3ilMHY8huMpIPPJhTzoXzoz_3BkzrmDl4wajX4XT51-JedgMi5UQZ0ibVnggtKGGGYX70Kxn70xubQY-sd-jU-gmejGkr_KSbZYxxQdeyKpvab86g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ac9d9acc3.mp4?token=dLHt6GEpSC9CdfSeVzcn3r07J0tDwhkFgnTJUIDPYncgfFXKdjzdWyhh_BpcQlTvsCebUUsksheY1LS8NKm5zLrM27g204CB6RRuteWzTz5c4d6PrL1tw5L8UXY59AzC3aZXyetb-vDKaTK8t5dLvKjSDLOolOXPTU93F7goQSLUTBzLq2mtYtIqaxZWMFKPpESK3WsgZZpeLz1F0hwTev0ssMyTQYV0Mpin_3ilMHY8huMpIPPJhTzoXzoz_3BkzrmDl4wajX4XT51-JedgMi5UQZ0ibVnggtKGGGYX70Kxn70xubQY-sd-jU-gmejGkr_KSbZYxxQdeyKpvab86g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صداوسیما روز ۲۹ اردیبهشت‌ماه، در برنامه «سلام صبح بخیر»، از تندیس «مشت گره‌کرده» علی خامنه‌ای، رهبر کشته‌شده جمهوری اسلامی، به‌عنوان نماد جدید میدان انقلاب تهران رونمایی کرد.
@iranintltv</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/5064" target="_blank">📅 09:26 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5063">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I9KAmY2mTPk8iW2Y2vo99ZvIL2x2UaHUtgBpZrnGBV-TUOYoHY0ecUVVdmrdlYcrEpNkNJ_jV5hbyUX74U8Q3DyR7k8IuBrT6mQxv9xCISR5oJ7BfxRDAotchYRWzC5ujb1wBzjPdWYsDdg7_c8T4pXHBc8HljIpYNMhR64NFHEuaBS0mvLpPLmqDQ8aICGrHfuitqWDfbWD9RlxXVVlKN4GGJoY4KxgB_fA_ZCKSGawoB3w1GubnvdY5Mbn6zm6uxazafjiiZekdfhmkfLqvgbNxjv0O8sFF1ZeGUpgYlftnWPxnELVkmJjBi8AeoMUMTRedG8u8gypGKO1EcGORg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«بهمن فرزانه» قاتل «الهه حسین‌نژاد» اعدام شد.
الهه حسین‌نژاد در خرداد ۱۴۰۴ برای بازگشت به منزل سوار یک خودرو شده بود، اما راننده او را ربود، به قتل رساند و پیکر او را در بیابان‌های اطراف تهران رها کرد.
«بهمن فرزانه» ابتدا انگیزه قتل را سرقت بیان کرد، اما در ویدیوی کوتاهی که از اعترافات او منتشر شد، دلیل این جنایت را خشم ناشی از نوع حجاب و وضعیت ظاهری الهه حسین‌نژاد عنوان کرد و حتی از واژه «بی‌حیایی» برای توصیف وضعیت الهه استفاده کرد.</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/5063" target="_blank">📅 09:12 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5062">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">روزنامه آمریکایی نیویورک‌تایمز به نقل از مقام‌های آمریکایی نوشت که در روز نخست جنگ، نیروی هوایی اسرائیل به خانه محمود احمدی‌نژاد حمله کرده است.    هدف از حمله این بود که احمدی‌نژاد از «حصر خانگی» خارج شود و پس از حذف خامنه‌ای، در موقعیتی قرار گیرد که بتواند…</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/5062" target="_blank">📅 08:56 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5061">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OhQstoA__DPdqImfccmHkU7aKzgrsIMvJ3hryU63R8uPI87Kzt_MseNmywKTFTYWo0PeHw40umia2moCJuzRBMexwUc9_gGKNzbFv6vuUKY4zYUCNOgOcHa0wQ75kIQM06TZv9Axo79Haj_ywFro7Ji8jZaOrHaochi8Io3vuRf2G27jfd9N0dGBOItrQHyjT2Vj6ry8P8FJmh0R4K2SXgBXdOXci5YIkw1FXpI55F-AQhh_Xo5cxzG9S6Gcbe3jd646MD7LREPeNIr3GS9o9Gqk7PPTQVzZgwp1_phrlvQ20MDFP7eG74FtKv_RPQIskTzUg6rKZ-_ltm-sOzYCDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزنامه آمریکایی نیویورک‌تایمز به نقل از مقام‌های آمریکایی نوشت که در روز نخست جنگ، نیروی هوایی اسرائیل به خانه محمود احمدی‌نژاد حمله کرده است.
هدف از حمله این بود که احمدی‌نژاد از «حصر خانگی» خارج شود و پس از حذف خامنه‌ای، در موقعیتی قرار گیرد که بتواند کنترل کشور را به دست بگیرد.
این منابع همچنین ادعا کرده‌اند که اسرائیل، با اطلاع آمریکا، طرحی برای بازگرداندن احمدی‌نژاد به قدرت پس از تضعیف جمهوری اسلامی آماده کرده بود و این موضوع پیش‌تر به خود او نیز منتقل شده بود.
اما عملیات طبق برنامه پیش نرفت. احمدی‌نژاد در جریان حمله به‌طور اتفاقی زخمی شد. هدف اصلی حمله، یک پست امنیتی در ابتدای خیابان محل سکونت او بود؛ جایی که چند عضو سپاه، که گفته می‌شود عملاً او را تحت کنترل و محدودیت شدید قرار داده بودند، کشته شدند.
از زمان این حمله، احمدی‌نژاد دیگر در انظار عمومی دیده نشده و در حال حاضر، اطلاعی از محل حضور یا وضعیت دقیق او در دست نیست.
….
آدم قحطی بود؟ هیچ کس نبود اونهم احمدی‌نژاد.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5061" target="_blank">📅 08:40 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5060">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QXOO-Mm2GlsqsNvBbMogmKbtrGQNdpVbXm_yPqqHq52aYDKq-vSq_JXQus04m2Gm91pFFP_JHKP0oAsSRMTFIyFs-aKlrwKIx2r-jEoMsXXurmwz6ysJUzLSvTYngbsSU8oLP00p-dAtGM3YV9weVnOTQUA8ML4cbPxS8fo86DnyDErybuSbprJ2dU7h91LFEeSuQxF8vOF2bMz_LVShEtjFsMwVEZ6kwn2swRBJkm0StAEs9ZLN3UScFnHY_LpP7US_z-dFfixsoklGFoNLbpAK99YOXrZaMVYmJ-kQ9rKxiNRIv72YjRH6Hrs2VY5D6VwFdYONNPp9itss3Bo2Qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه نقشه‌‌ای کشیده که یهو از  لغو حمله نظامی، به گفتن این جملات رسیده.</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5060" target="_blank">📅 03:43 · 30 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5058" target="_blank">📅 20:59 · 29 Ordibehesht 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/edEKnX2qBD24ggnXeoyYtnFNp8uDRumOlPZIEzNr4Own0zDOWPghrIPJ2Nkawx4MGplmaHl7RTy_J_gDypNvqG4VVDyGmELXUXEFiW4hlJS7skYbiFTxHmHsaozUml2xpcfcrudcVq-0SReB8XW-YEanAauq7wjZTym6XSeYOJRPcSJJgCrL86C1He4iIKXGgOAFsgTFDlWp3Bx6pYMG-sVE-7D1_XCuktnfssKVGYdsxXtGwg2tK5hjO1nrR8V2U_EkHzjLdvFMRL2WP8ihCCjaV3-74CazHZhwkcqzI6YJO3RvVXKeQjyTZrTzeKHsoMqioOADpMMrs4N2Cg1n0g.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/03ae416835.mp4?token=HOZFnO-3pjJHcVZgSf_4lbRy112FkSq9YYvamgRR7lQQEO74ME1WfwmUp-BrZmCQQh5h15g_HxD9l_nzRYqvb85CUa_e8kL1Gv875TR_VQXHckh7jZx01ONeX5c4NZrVJxlXoqp0AntrrlJYUWa1op6GFD68g8XpxXvjc88HhLy8o8kqeCf1v8x_NoIf_kB7ibCDy8B69Oo0j2Sq8lDnUcBlsXhemu2bMEkNZla2LImOeXlsCnUldcp1tzeHTviOXFj2nlekvnxB9fG3yekMCiJDEhm2YLHWti98ebTSJ4iGiGSCND6-pqSAk-sJIvjRG8sborpeyylfNRBRW_xfHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03ae416835.mp4?token=HOZFnO-3pjJHcVZgSf_4lbRy112FkSq9YYvamgRR7lQQEO74ME1WfwmUp-BrZmCQQh5h15g_HxD9l_nzRYqvb85CUa_e8kL1Gv875TR_VQXHckh7jZx01ONeX5c4NZrVJxlXoqp0AntrrlJYUWa1op6GFD68g8XpxXvjc88HhLy8o8kqeCf1v8x_NoIf_kB7ibCDy8B69Oo0j2Sq8lDnUcBlsXhemu2bMEkNZla2LImOeXlsCnUldcp1tzeHTviOXFj2nlekvnxB9fG3yekMCiJDEhm2YLHWti98ebTSJ4iGiGSCND6-pqSAk-sJIvjRG8sborpeyylfNRBRW_xfHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZFNMBCfDjxeOnhNqs2e8ydNFJfS57W5A-NGBcOOW3SS_OfGqIF_jRFOn5cC3Ue2slTLVg9apij0Y84bl_9_EWrGimyxGY_RFOnO9hJ8nrt_n5BGVe4w4SUv74kNxWDkcieYoEG1MSy9JUK1-1F3OH5hbhX6ei8bKaHo8h-x7bxst_PeHyWFTz942EJk4x_4IyMUEuOMiVeTxiD-ZDdjRS5ky6T0pFl8uStqdbIIwfOSJOz88EI0tKf036YRq4rDfUHwouakLtavrvN-Hu7-uXGvzBIUJd4CHY7qb9mKKm9Mp9_CF-0Ildk4QWFUSber70aW7gJESvF1WgKiegrjqJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اعدام و غارت و سرکوب!</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5053" target="_blank">📅 15:17 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5052">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WAKKWoPGcDOh0sxFi0lob-uJnVCdv99aA8ZKty-H5dZ_WS_NJ_xEoiYN64nuFKc1rAjuKhtkc7Lvoj2uTBxJyeNI8BVnaehS5D3AozRnsHJ_CxzFzYWk0uGB13oatMTuDsXvAjs81XhJbDIae0vCuaPev4_9V4-ABkG1CHqF62fPE1SvXsOQDZlc8iDjXtFK7C-ju-3HA9PUYLgluMYS_XvEKo84Dzm5IYnFZhiZJS573a4yIZMk7a7oj-PtaS2mXxECC1Efuhq4sPers1IpFgLJ5P-DMI_U8_HFprhLVOFE2a2CwbutRU1-n3gCTHmnRAHGdjA7GX1OR_kfBPAFFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سیاست‌های ترامپ اینها رو گیج کرده ،
آشنا که «معاون ویژه وزارت اطلاعات» بود و بعدها رئیس مرکز بررسی‌های استراتژیک در دولت روحانی شد نوشته که شاید «از عقب» وارد بشن!  :)</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5052" target="_blank">📅 12:55 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5051">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KaSdmZmkOhwucKJORBV32IG7UZZQQcojHl_jvLrufp0gmukjjAVHexzOth1oiFgHBhxO2Ci2JDXjGRWJXINSRxLEV-_Ifc7FYaKa3iH-f8EKUM6sHS3TqdoZd5ukKc1E1LeJ0ChMduJfcqwDnfaUMYwwFRRVEJ3wEu8ajkfHWvwuQO1tlEow7bfGi2KQ6x_4d5pPZfVE53iU63waVziknT4pK7Uzf4jlwz7QWyQG62p65kaCSgm_7IfJiw7ClSrB4cz2WB0Dj1oC6QK3nmPMEsCsFrB8NbSYta9AgDbKUJbolh_ulZaWc1YLgUnhm0hBT7nwxoWmtQTf8sJFHgqPRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پاکستان که ۸ هزار نیرو و سامانه دفاعی موشکی و یک اسکادران جنگنده در عربستان برای دفاع از ارتش عربستان
در برابر «تهدیدها»! مستقر کرده گفته آماده است در صورت نیاز این تعداد را به ۸۰ هزار نیرو برساند!
تمام حقوق این نظامیان بر عهده عربستان خواهد بود. مقامات عربستانی در سال‌های اخیر هم بارها گفته بودند که «سلاح هسته‌ای پاکستان» در خدمت دفاع
از «حرمین شریفین» است!</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5051" target="_blank">📅 12:39 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5050">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vf-xcLAcl43MHFq5JgQ5JtPExy52V75hytCCSHe9psRBe0o2fvajmuIGUWoy1MyKzMtjSoX7CFZvslugIFDIgL2kCKiP3qX64k_iWl8txf__pg8WcDZebVmuf3M6NoTYXJfNzpqHjfaegDyk5kIuTNi6TQs406cZzIjUPfoh9lWc3AaWcvGE6zp8G2EUuYxYMezPtGq0PR82QOjK7O53nHQ9m4Ankdq9L_j8vUuRIA2f-x4X_5_Ptm34rSaYYaDMN8oijz9Km3XA60H0mGag6bwd4kCa_JdcTsa7-BvgEDkZrKF6FP2Jb54P8wMQQPc1H2VRniP_b7T_rnPSNFvC0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عالی بود این جمله :
رئیسی شاخص و مدل عینی
حاکمیت اسلامی است!
نهایت الگوی اینها فردی شبیه رئیسی است! که دیگه همه به چشم دیدیم
کی بود و چی بود و چه کرد!</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5050" target="_blank">📅 11:31 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5049">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e6ZCTFhAOvQk8Sm-BaG2jLDe_B5U-ETfvLFAWsKW75xrfpXzq01bfgSBy4Y02mhuA4zoYTntb23hGIUHjKfEgGNTvU1ZXd0ocRY-Mc_VM4V0h9bE_5H5RnnZtwuq4v3RZENrwxBJgZIQ7X0bXw58VNyRxX10f3UR9ZZArJ9HFQEI1JfA_3DKw0l6u0MW0_eixN3EJbJGoL7DBSAuBEbZkEhBmofMnw5cUN0h7ka1hLNJ9bU-kEUpoyPXIdm_I--mYYI8WZocEAZFbq4Nbiub8-ByF0BxucPYuvw9Zx9V9MnBDF25Rn-VeMfofpkF0eHitoYM-c9zKMMRKfwwwMQ7gQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تاثیر توییت ترامپ که میخواستم حمله کنم به خاطر کشورهای عربی حمله نکردم و…. بر بهای نفت در بازارهای جهانی.
کاهش حدود ۷ دلاری بهای نفت</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5049" target="_blank">📅 06:26 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5048">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b8eb45098.mp4?token=Xd1Af7g60uyo0dD0FHt4NU_VArxeOGUsopJYpPDMqmFOkCxggEc8aCJHlKBruqMkU-0vOq66_gdxm4lHomaBW_eQ7eDMrchhM0rCb6yNdvuxCC-cc3qB1q8O0NTYF2tBwSH0oyqMksqBR3OyzgxvCZL8lfiV7Rtq4-Fzfwo0KdIux_E6G_YCFUcJwxCQxhzhrWpt0seLek9O178bRAc4Jy4MmTOvpIVwdACvGfkTcM0W32Qjqt7SP-k6oLX1Ollmy4wHWL4SnRj9umYRN7WXxVxWpHDD8vioUNCdIQ_vO2oLKOsPerNt6D2BI5rsGcZlR62N-dLAkKP6SMiLW4XuVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b8eb45098.mp4?token=Xd1Af7g60uyo0dD0FHt4NU_VArxeOGUsopJYpPDMqmFOkCxggEc8aCJHlKBruqMkU-0vOq66_gdxm4lHomaBW_eQ7eDMrchhM0rCb6yNdvuxCC-cc3qB1q8O0NTYF2tBwSH0oyqMksqBR3OyzgxvCZL8lfiV7Rtq4-Fzfwo0KdIux_E6G_YCFUcJwxCQxhzhrWpt0seLek9O178bRAc4Jy4MmTOvpIVwdACvGfkTcM0W32Qjqt7SP-k6oLX1Ollmy4wHWL4SnRj9umYRN7WXxVxWpHDD8vioUNCdIQ_vO2oLKOsPerNt6D2BI5rsGcZlR62N-dLAkKP6SMiLW4XuVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فعال شدن پدافند در اصفهان</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5048" target="_blank">📅 00:06 · 29 Ordibehesht 1405</a></div>
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
