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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-06 09:41:48</div>
<hr>

<div class="tg-post" id="msg-5156">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pw8hCPlWTLHpgVMfZiKHgPIugUEQ7gyIQZP9xgqu3GSnT_ZgmoxCsR1lMDwVlNC0lAKNvZKCw5AxurK9GkjWsuDJaFrrO_CwSBBBp98NLX2uLOmLGBjCNdkaqLQzpTOzoYIWRtrdCNHSKR1miGBK1tE8GHRxj3aT_jxxeWPwpBD8chi4L3lXmeifV2QyLiKnv7PB-PZbKg91dZEZ0kro0irSzQ0YSYVIEV75S2iSOICee3XcU4FDR7weDIusxFJiYOCdFbFu3bSpKjoPI1Bk1CiNSauc_iWSXnGfaVYipdKWbJ4GscM8fBGD-MxBjmXEf4N_hNT9CVHYTCv3k0Fqjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صدا و سیما دیشب بعد از انتشار خبر شنیده شدن صدای انفجار گزارشی تهیه کرد و گفت : منبع صداها مشخص نیست!
بعد صابرین‌نیوز و خبرگزاری دانشجو و… حتی اسامی کشته‌ها رو منتشر کردن
بعد سخنگوی سنتکام رسما گفت حمله کردیم و زدیم و…!
دیگه صدا و سیما در همون مرحله « منبع صداها مشخص‌ نیست» موند که موند و داستان رو ادامه نداد .
«مصلحت» نبود!</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/5156" target="_blank">📅 23:18 · 05 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/5155" target="_blank">📅 22:26 · 05 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5154" target="_blank">📅 20:07 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5153">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">‏پیام منتسب به مجتبی خامنه‌ای به مناسبت حج: رژیم منحوس صهیونی ۱۵ سال آینده را نخواهد دید.
باعشه!
بابات هم همین‌ها رو میگفت که باعث شد امروز ۹۰ روزه که معلوم‌ نیست هستی یا نیستی، اگه هم هستی طوری قایم شدی که گویی هرگز نبوده‌‌ای :)</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5153" target="_blank">📅 14:43 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5152">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/StdbKNy2NYED09oUAj1exNe3bpmDbOQN8a2r_G_HYG14Q67H9sCdm2biYTTo_9AmCa5BRw-u__I0xuSYEB9pY1JZtQ0mx-8KXQcOBEjNFZzambSVsKCNsjZwhcyqh8U7K79OxOpppgMBLYJGXAjs6h-qqVr23USPmWpJmiRK8fsrRx5WkndKhiSnPwjj0PM3Ojusq2iXwoHwcED9ulmEj5S9XfwxhDL-QqMAFqDz6Z86OEw7wx0bcjpC6D8GUc_8rbMYZ4eISZC8p3u0ex6tYtXmecJHWT4vzxAFMhQA3lMbvhTMezgccWAnThOOemmp1A0B_69IawIPEH3spN0i-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ذوالقدر دبیر شورای عالی امنیت ملی، میدان جدید رو معرفی کرده که هیچ کس نباید حرفی بزنه که وحدت شکن باشه!
دستور خفه شدن همگانی تا رسیدن به پیروزی!
اسمی هم از مجتبی خامنه‌ای نیست.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/5152" target="_blank">📅 05:23 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5151">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i0YdZm_XlwtWGvjqLSxs7OoJSB3FiMlFyB4cL33Sy9hkqCa_5UDWq6b3KG8doeaVdlX3vJl6LKyW1n7oi4TYsPA4-7KzeKgAMYDcoMaU0pWP-vjrUxgUTH4oobMYAuwIo4jreQ_NqjOF9XgpGqKn6NJBHQYQCNA00Z3iI8fIduKta1rilw_pWyWvhyG0kMG9LfHWTT1ma8cIUEui_gajpbKwTrKjjCe7X6z8_zMobOlIH5lwqYOitCKrnnmMl2UNCzA3EJwuFqDsenFeakJi80yBa-I3CYLLTdrhTEEbOAut3uy4ziR7sUbkvnKPHiwPHeDYTcxxO7OrfnsrMBENog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
ارتش آمریکا حملاتی در جنوب ایران انجام داد / کشته شدن چند نیروی سپاه.   سخنگوی سنتکام رسما اعلام کرد که جنگنده‌های آمریکایی به چند سایت موشکی و دو قایق که مشغول مین‌ریزی بودند، در اطراف بندرعباس، حمله کرده است. خبرگزاری دانشجو، وابسته به بسیج، تعداد کشته‌ها…</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5151" target="_blank">📅 04:57 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5150">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I4qRUQi3mWBvfwhUjfiNuIyuM1lq7OP4M76SWu5bFry03AbqCC_vRhrNREJ2x0p-jLFf8sctfDt5NG3-UD4xBnV1VCTpIBsKIUp07-B8fX0AKvCjjL72hOlpiW81ePDe2N6I4_6uGX3dZDqby_oTVtI_stDHaevncShUHLm6dv2i58Ol4Ltun7dJSY2F48kLLEEc5ib3RKXkFuT6xnReeLf6YtIyimz7jnYoxgOWgJRPqegUly5RqKCZsQhAT_PxluCCHgN_uh2Ga3gAJddT1pC_kV7UqRCf-lDs_oqm1UAMWEzvk3Mc4NWtU2Yf4CuDoGqQPbihvSEwT4ZdXbN89w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
ارتش آمریکا حملاتی در جنوب ایران انجام داد / کشته شدن چند نیروی سپاه
.
سخنگوی سنتکام رسما اعلام کرد که جنگنده‌های آمریکایی به چند سایت موشکی و دو قایق که مشغول مین‌ریزی بودند، در اطراف بندرعباس، حمله کرده است.
خبرگزاری دانشجو، وابسته به بسیج، تعداد کشته‌ها را نامشخص اعلام کرده اما اسامی سه تن  را نوشته.</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5150" target="_blank">📅 04:50 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5149">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">ترامپ : یا یک توافق عالی برای همه خواهد بود یا هیچ توافقی نخواهد بود.
اگر توافقی نباشد آمریکا به جنگ بازمیگردد.
کشورهای منطقه باید عضو پیمان ابراهیم شوند.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5149" target="_blank">📅 17:30 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5148">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">قیمت نفت : ۹۷ دلار</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/5148" target="_blank">📅 14:48 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5147">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GXPqqXk2dKQDnL13zNIt75kjiWPcxCnQkbopGx8QMWWVn1MYPamt2AYBBfE3XRBxl_UkAFavsSv084txQX--vD5bRa5y53e_S5nm6KIggN2-R2Mylxf1TSoOzlH2Y_yNzCBw-ohhVHXsy58xwKdRas-2PGUwPhiKvJxcIkIAb6i3PwC_043IVknCdcrB4IJZ9K-1JChqKKuF98ZwXYllo3IBnliki3aYGO4-yTl9v77TPwDWforuu2M0UyQliqMym2xtQpSDX4i0YfRqJS7kDD5uKQuaXryZ2pUP2IAS5JTTcVHUV2Wi8fLrxsuH7o4tWSuNJLloO4mPxBpDrjgmrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در حالی که صدا و سیما شیپور پیروزی میزنه و از موافقت آمریکا با هر ده پیش شرط جمهوری اسلامی میگه،
سخنگوی وزارت خارجه امروز گفته : کسی نمی‌تواند ادعا بکند به توافق نزدیک شده‌ایم!</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/5147" target="_blank">📅 14:29 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5146">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🔺
بقایی، سخنگوی وزارت خارجه:
آمریکا به عباس عراقچی، ویزا برای حضور در سازمان ملل نداد.</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5146" target="_blank">📅 14:16 · 04 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5145" target="_blank">📅 13:46 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5144">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">رئیس ستاد کل ارتش اسرائیل - توی این مایه‌ها -  گفته: «در پاسخ به هر حمله پهپادی انفجاری حزب‌الله، باید یکی از برج‌های بیروت رو هدف قرار بدیم.»
حملات حزب‌الله به اسرائیل رو یا دولت لبنان باید متوقف کنه، یا اسرائیل.</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5144" target="_blank">📅 13:41 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5143">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EgjpUJ_0cwWCdVN3XkpTsBIEueAVGN7ogXtoZo9OzB08jFW7eU9Qx-0-C7Fri8G3JEaX4ptI3aVewv9IpItLgmgbdMXzLYuAJ2TAErLDL0sP1aMh7TN18QvcYqA1ESah-NSbCt1Sd-ErcuikNZKgzr54ej0v0S1jo8L7P2KiNF3x3L15h23hjOD9oxq_WD530siEoj4Siiz2SHqUp8VDRCynlZvwL5YIomUO7vwW7Ekh4O91RdacU9pEJZekYCVylN2Hs4ZBqaoADbEZlb11LOkkr0mbraA-qr3I6a1anf5VOXP4ii3wFRjWCjTxl7AHmXjueTtNT4hiJERsHuLtIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صبح در ایران با اذان و با اعدام جوانانش شروع می‌شود.</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5143" target="_blank">📅 11:58 · 04 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5142" target="_blank">📅 11:04 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5141">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">صدا و سیما:  آمریکا با ۱۰ شرط جمهوری اسلامی موافقت کرده   ‏۱. آمریکا متعهد به عدم تجاوز به ایران شده  ‏۲. استمرار کنترل ایران بر تنگه هرمز ‏۳.پذیرش غنی سازی ‏۴.رفع همه تحریم های اولیه  ‏۵.رفع همه تحریم های ثانویه ‏۶.خاتمه تمامی قطعنامه های شورای امنیت  ‏۷.خاتمه…</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5141" target="_blank">📅 09:00 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5140">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6cc885feb3.mp4?token=km684lZDQggV3QtiCSgCKl27QOCgkIJWOFTjD-e3f8WH3rapV_AIFSfBp94j4WKegAdAQA3Fry2vyTlOF6k_R-M44sHa4x0LXJRHehA_BSdbxlhSuK9AfDYxrfI-5uYG03a-myOwRXpJG9A9OQdNDm6wQaLKXvt2yYd_abyzuMG4LIcmc-AJvK-Fco__gP8302QvrPmwEJ3NQYiWSYLl8_9FDYUmRbSHYeML_BkgIIMmdWSe3IuNOjjByen6-cSHT7V7cBpRx852Nk0VOHnwxljvW39syvnD5-G7XRr-7lxDWe7ApPV7RWYQNTa9bbsjUH54Uda031VIOm2XXg5zSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6cc885feb3.mp4?token=km684lZDQggV3QtiCSgCKl27QOCgkIJWOFTjD-e3f8WH3rapV_AIFSfBp94j4WKegAdAQA3Fry2vyTlOF6k_R-M44sHa4x0LXJRHehA_BSdbxlhSuK9AfDYxrfI-5uYG03a-myOwRXpJG9A9OQdNDm6wQaLKXvt2yYd_abyzuMG4LIcmc-AJvK-Fco__gP8302QvrPmwEJ3NQYiWSYLl8_9FDYUmRbSHYeML_BkgIIMmdWSe3IuNOjjByen6-cSHT7V7cBpRx852Nk0VOHnwxljvW39syvnD5-G7XRr-7lxDWe7ApPV7RWYQNTa9bbsjUH54Uda031VIOm2XXg5zSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/5140" target="_blank">📅 08:15 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5139">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">برخلاف خبرهایی که یکسره از احتمال توافق می‌گویند، فاصله خواست‌های دو‌ طرف هنوز آنچنان زیاد است که بشود گفت :
توافق بعید است!</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5139" target="_blank">📅 01:47 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5138">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
اکسیوس : ترامپ روز شنبه در یک تماس کنفرانسی به رهبران کشورهای عرب و مسلمان گفت که اگر توافقی برای پایان دادن به جنگ با ایران حاصل شود، او می‌خواهد کشورهای آنها به «توافق‌های ابراهیم» بپیوندند و با اسرائیل توافق صلح امضا کنند.</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/5138" target="_blank">📅 00:35 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5137">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
اکسیوس : ترامپ روز شنبه در یک تماس کنفرانسی به رهبران کشورهای عرب و مسلمان گفت که اگر توافقی برای پایان دادن به جنگ با ایران حاصل شود، او می‌خواهد کشورهای آنها به «توافق‌های ابراهیم» بپیوندند و با اسرائیل توافق صلح امضا کنند.</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/5137" target="_blank">📅 22:25 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5136">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromدماوند</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GrqW_AAYmu-Y1CBS4P-AIgMLP_Zs2Qs7v5F17mtZzOIylAoB9g4uPR-lsQyDgvFR40McghxZqOUV6-2xKgMwvcfD8panXSXmZS7abrED9JyYonX5UAPda2E2XKXFNM1R5JhVNFqI8nfulEGzqN1mflyt1DgZ5Ra8dfClf1KWUdxrEPaPKVs7MFThomTCpnBzNWDw1rhzQu93XRmgEF5JDiT3K7Jq2OnGKCx5EHCsCbti0Yo0N86tfhDS-aFSr0IwVhY3WN1xoi8gBFLcqLtByQ_mgSLuGS3_hlYXqF32NBmILVQjvPJYbu4DS2JtSIhYUl8bpbDq7eQ1f8ggkkE5mA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❗
یک اعدام دیگر
مجتبی کیان، بامداد امروز و همزمان با اذان صبح، به دست جمهوری جنایتکار اسلامی اعدام شد!
جرم او را ارائه مختصات صنایع تولیدی به شبکه‌های ماهواره‌ای اعلام کرده‌اند؛ انگار که اسرائیل که اتاق خواب رهبران رژیم را می‌داند به اطلاعات دیگران نیاز ندارد...
خبرگزاری سپاه نوشته است: «وی در پیام‌هایی به شبکه وابسته به دشمن، اطلاعات محل شرکت مرتبط با صنایع دفاعی را ارسال و با قید نام نخست‌وزیر رژیم صهیونیستی در پیام ارسالی به عوامل این شبکه تأکید می‌کند که موضوع را «به بی‌بی آمار بده»!
T.me/irdamavand</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/5136" target="_blank">📅 15:52 · 03 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/5135" target="_blank">📅 07:35 · 03 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/5134" target="_blank">📅 00:31 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5133">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RkSuGQLYbFMIP8nzmFPFGgA5N26mdW5xsHmM6Voz4l4hRuyg3-weEIiwPfq3ztmIZlusaPgpS8pZ2WQhQ63ULEIxZY7isYKKFh1wLhMz7qmKv_ZjBF0uGFvcobt8pIGHzZwsKzQbFFCnZlwakAB0_zfBXwiuO7EzBY7O6gcRJAq-7aDdKcLkGzfoCe6bysm8Tczje0vNLfMyuAFieElKq4ZAmN_p6goOOXnVZjY0fcSgLRqkfjsKZzFNnqvHjkZMzN4PiQwJNHM2dhT6ZVR4FllNg7jdCwIln9SiFdaRGTtmYaf6Zffq6xFifB1jSqt8-b1B-PNmA1LozcEVd8jnWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با هوش مصنوعی طراحی کردم.
گاو : نماد فراوانی و ثروت سرزمین ایران و منطقه.
تن زنانه و نیمه عریان: نماد پاکی، نماد لطافت و ظرافت ، در نقطه تقابل با خشونت و توحش و درندگی
بقیه هم‌ که معرف حضورتونه، آشنای دیرینه.</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5133" target="_blank">📅 22:09 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5132">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">ترامپ به اکسیوس  گفت که درباره توافق با ایران یا بمباران، «کاملاً پنجاه‌پنجاه» است. ترامپ گفت امروز با مشاوران ارشدش دیدار خواهد کرد تا آخرین پیش‌نویس توافق را بررسی کنند و ممکن است تا فردا تصمیم نهایی را بگیرد.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5132" target="_blank">📅 20:57 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5131">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🚨
آکسیوس : ترامپ ساعت هشت شب امشب ،  در یک تماس کنفرانسی  با رهبران عرب شرکت خواهد کرد تا درباره پیش‌نویس توافق با ایران گفت‌وگو کند و نظر آن‌ها را بشنود.
🔺
نظر شخصی :  توافقی در کار نیست!</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5131" target="_blank">📅 20:55 · 02 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5130" target="_blank">📅 20:13 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5127">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b5c3d0822.mp4?token=JAd5zT_xWiy2Ju2uKZ7mGA7s2ZqMoThN8_wKALlbyU2uhriokUyKeNEnW9J1U77ZO3--Ohe7ojO0AMFJuWB75dwtynYrB0l2RUTj_3hvnEymqlXTv_azIoOeZ1pz68PRGt-t4W0Z70Rcm3ixZcAHWU_jREFBLnn330W2CnOb5ct60XO18R1C0o26PKp31HAfjY-z7g-Ep5vPNQz4v15HUHAupZCRTv5UMCzsS83uBuCsNetBM4qy-jD0wWTQbvKDSCAup5gJBQeJYYTPnectJuQooUURwU0N7-dGRMc3Dxy8o7aYgird1ypy5X356_88AQ4gpl5DayZlgR2lvyT2rA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b5c3d0822.mp4?token=JAd5zT_xWiy2Ju2uKZ7mGA7s2ZqMoThN8_wKALlbyU2uhriokUyKeNEnW9J1U77ZO3--Ohe7ojO0AMFJuWB75dwtynYrB0l2RUTj_3hvnEymqlXTv_azIoOeZ1pz68PRGt-t4W0Z70Rcm3ixZcAHWU_jREFBLnn330W2CnOb5ct60XO18R1C0o26PKp31HAfjY-z7g-Ep5vPNQz4v15HUHAupZCRTv5UMCzsS83uBuCsNetBM4qy-jD0wWTQbvKDSCAup5gJBQeJYYTPnectJuQooUURwU0N7-dGRMc3Dxy8o7aYgird1ypy5X356_88AQ4gpl5DayZlgR2lvyT2rA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقتی بعد از صدها سال
مردم شمال مدیترانه و جنوب مدیترانه بهم رسیدند
الجزایر سال ۱۹۵۲  (۷۴ سال پیش
مناطق اروپایی نشین
و مناطق مسلمان نشین</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5127" target="_blank">📅 19:52 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5126">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oTyLenxO4J9VRaNH-oxb2u0pJb_EyRsFD0m_yLFLeOSghU7GeZhdG6U4bcUKS_pMO-_VR-Wdsb4NEMBw75shGIYV98798I_y3gAuYUluNdiAaTdIGfzzoiDGwcimjCIFh6HC93FOzK72kj1zUrE2GBgsmQ2QzJ_xDIHhL_oyR0_anwlkBtWsPuj8ge6BbrCiIQzkBK4X5bNoN7yFqMfGeijP7K1Jr887GgfnQZJGPjlvufFr4wy0643BfmVx7qnAI6N6yrIE-wZ2G_utqq16iFCFD4FWfmzmFRK6A3vjHZlBCeF2GDUiD71zl8LgAoZFhLzvXDpQwk-XBJj_40V70Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5126" target="_blank">📅 18:48 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5125">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZwGDXgcl3LfS4wWT2BDMCfou3mzY6m5tc7UiFWQVvjbBjSyrLOmygqLd4uski1MZRbbC40ht1GlvkfLWxgFbBzXbc-SVg04o43xCBBSY1pTZYmL3OBCJYy1RTLTd6j6Xm9MF-eyX6IwtJguRJnk1DdUy5xQkyk__XqHNdStA-k-TCuvcfFkwLcCwIkD80qgVAPaAziIR-HvT05qXRtqJnu0o-jsAV3QIPlozTbvDv55irHVIFAkbccoeWLfHQtcgy-_VfINGerISMjJxU7XfIj0arCNUscghcIsgDYR67PqdCxLA3oRQsT2oAvW9eDe7E3GrJAx43s9sQzEFb9cGSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید ترامپ که پرچم آمریکا را روی نقشه ایران به تصویر کشیده و تیتر زده «ایالات متحده خاورمیانه؟»</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/5125" target="_blank">📅 18:16 · 02 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5123" target="_blank">📅 17:25 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5122">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AA89i_1QwWrog2zL5rbVz_cbg0Ve_0OOibdOmnO6pbK3LKnaZAN1vViEfqi5UXZ5QTGBJw3qYynPq_a8HgO39RKt6pAJHC7IfH7JiDgpYNEp0thcStmjl0Xpy1BerqdDiLRroRIQOlos9fWdlyN6-n0dHwS2Z9Eb-5tsr0xru06F8I37rK2k-HikbTIk7o26KfWTWA8wXRk-o0c6JlmYdhyLpkTxJEgteM0NR8PIuxbLWNaH29L6lMRDrJQa8qNyLNwkDXuhPaglT5v3TDIrOdxFEJfu4cTtH3chrWuTdaoQpvXYpEs-c2O7YfsVTd9z4kZMnwznnbq3tBfhfcs7wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چقدر ایران باید هزینه بده برای این گر‌وه‌ها
و برای این جنگ‌های بی‌پایان جمهوری اسلامی با آمریکا و اسرائیل.</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5122" target="_blank">📅 17:18 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5121">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">به خاطر ارسال ویدئو ۲۷ سال زندان!    مجازات پدر «رومینا اشرفی» ۱۴ ساله، که با داس سر دخترش رو برید: ۹ سال زندان   حکومت اسلامی! عدالت علوی!</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5121" target="_blank">📅 13:23 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5120">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PC28aO3lF2ueu3jdAocu4AGd8eXHrSuyC1SRXfKxZNNFrAq3FJLP1LjnTrD1_HyoTP68xIIqFb94Jia_NjduP2b-ztcnkx8bPf2j2R1sKpj4grtPHJjczseHD1CMAeMmkQsYutpH1uCVBb0HQmc73GeY8sKz-As1n4yOeQEPihkbmWX6m3QFi_yO9-KM7EMr7Ek_peTLzvydiWa1UB4k4se8rSzepTyRlDEY9jLLh-fAkBNUtaLrJYwM68IRB2ODmHGw4v1K6ROHvfMZY3k8gcBbrTCgYcBj9M-4eYk66MdPKD_1IZWhnSvAvm4gukWOVHu7JDBJh-OZIyoQ6Gd7AQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به خاطر ارسال ویدئو ۲۷ سال زندان!
مجازات پدر «رومینا اشرفی» ۱۴ ساله، که با داس سر دخترش رو برید:
۹ سال زندان
حکومت اسلامی! عدالت علوی!</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5120" target="_blank">📅 13:20 · 02 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5119" target="_blank">📅 08:14 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5118">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">حریم هوایی ایران در مناطق غربی بسته شد.
پروازها فقط در طول روز</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5118" target="_blank">📅 01:01 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5117">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
🚨
براساس گزارش آکسیوس، ترامپ به‌طور جدی در حال بررسی آغاز حملات جدید علیه جمهوری اسلامی است؛ مگر اینکه در آخرین لحظات، گشایشی در مذاکرات حاصل شود.</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5117" target="_blank">📅 00:13 · 02 Khordad 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K9HFEQzKsC9rZCzW3cr5IwIClh60xSeW4d06qDNmH9QcptUdlgy43yGFfA9eEGrydPiTejGyAsvem77pYCxpUW2j_ANha1bURlaVCkETAJsusdCAdr9c0XXSGnc_4kJ4zdOjDlNbgDWSgvWxiwmg-xnAsRfJlricu_Qq8G9EyuxM1xP_4Ny6b33qKFt9knJ5BcXd8_-i-mu3BGAqInF-iPqrEnh5pZSPDDjzXzmMycRd51nH-ijplPL_h7gETXcd9rJRwzYQgHgbmGTcyScMxNXFv8yL5YIf44O43KkmqTEQlkDZYavLSzi6x034Dpy6zREGhfJRbi30HLPJWLEazA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری وابسته به سپاه این مدلی تیتر میزنه
ولی در واقع «گابارد» از مخالفان معروف جنگ علیه جمهوری اسلامی بود که الان کنار گذاشته شد.</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5115" target="_blank">📅 22:55 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5114">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DMi_znV2EoLzVpm_OE67znbmaKBF4vUceC7s7AVKa5OSZt-jo_A1XZoAvWw8wQDksVRGxMvrsn_kb_6TJn-pySJaZ5q-4a8G5Q1v5wgn4pgGvkwT6xgllxVa-SkLDOL-IIEtMYlszVmGZZXnsA6s6-162u6G5HG9_iZK_MsTHyRmBoeinOqt7kEr14li6jaghEqGkFkc85RVkkO7v8QId-iTnrrXnA3CfW9o4fOjntpkprJVrgnQyva72_U-zDL83Kp7UOetzkDrT29Gd9iqMzuOuWjmJnGSorLpm5maLUS2WZxbozXU0h9rqtd9pbHFH0eLXX07cId2qS7o4Nlhgg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/5113" target="_blank">📅 21:04 · 01 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/5112" target="_blank">📅 18:57 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5111">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DgHXHx5q1b6L3Gho0Jx2jBmitkPditLJwho9hIb1rNWDVzdZPZRZOMlJTVJILKygYR1P_tZ5jyRo9-ygOOPasWZDvnju7GirLQdZwLmtZtnmXVNiyLjWiSjmiBBDpicKaB4W9Yptkm9Fpifu28rnV4hsaqb-d2cfsGToQ7R1iyRBsFKj169XohmBBzktUuRENB_0KCHHJox93VJaVMg08Mv-pa8MOlnwA3nSt6F4JUBmFOORJy4h3X6WB_y6lArbQi7F-gicgedHzDfKVlzj9Q36rIOowyKc_wbdFp6CvjQc52OHWmwnWEfz7y417W3ENc0XijvFGpdUTPXs7ZgH7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این خانم! از چهره‌های معروف چپ  در دانشگاه تهران! در تظاهرات حکومتی شرکت میکنه!   بدون توجه به اینکه جمهوری اسلامی طرف  دو‌شب دست به یک قتل عام هولناک زد!  پس چرا کنار جمهوری اسلامی است؟  چون جمهوری اسلامی ضد آمریکاست!  از اسرائیل هم فقط به این دلیل بدشون…</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farahmand_alipour/5111" target="_blank">📅 18:52 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5110">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mt0DZrRmNz0TvlO_OQbH2lilm9E1afLKF3qSuNDI6F_fFZtDKOAA3OjrJILOtnMdwSSytJrqQCVtHzJyHLlwgT3BsZ3eR-0HOZR1mUNZBNzFiMH-TircJUdFC7MT6fqOkWUmOzvJ6bBehmL3SX_C-iW93bGci4RWSa-C6NkXIlq12auScz7oq-sybAyK-Dxs_bczAlQWg0-GtZubE7wN89ZTE2EPMPnkDFY_stuWMNioAL4i1q79Wf1XFf34Lonk0lMjgIN_W9UkI6sRqeSj3mpdvpmU1rq56T92NklCwFpSCkVVEH128gZ7D4ANWIeewDEJIq2s5sNRqK3knsaS7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این افراد، از همون روز نخست حتی قبل از وقوع انقلاب ۵۷ در آرزوی  تبدیل ایران به یک «ویتنام دیگر» بودند، یک سرزمین دیگر برای مبارزه با آمریکا!  بسیاری از سران و اعضای بلند پایه چپ و…..  توسط جمهوری اسلامی کشته شد،  اما این به چشم خیلی از چپگرایان مهم نیست! چون…</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farahmand_alipour/5110" target="_blank">📅 18:45 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5109">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cOS7TunRE6cEuOJdMvkI56yvJU3UAK_F4oS3lHk9uX8HvkybV2KxB__XGCdauOJLc9chBKLqIywDwFEmkxWfRqfP4pS1Jz95kY85MEgp8k5MVktnkg0AS9axdppgSjNKGf3H9MiC4jrCbP5_EouwzCvFfISThmv_rficQuIX5heihYOJI5hc73als36BnqcHYgFlylKQF8yX9z_F-pEJXr3ZQFBRMmGxHgyeZoXW2C7w6mzsBL_6Jbea0l-UlgONEBZVzs5UuU3_ZvIvXziJFA8Fc3s9sOR8EkBhxRAiPuFD9NKPPoaDSpLsRCB_nMy6OvlDtT0Eo8rVsrx_F36psw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جلال آل احمد، در سال ۱۳۴۱ کتابی منتشر کرد به نام «غرب زدگی» که تاثیرات بسیار زیادی روی نسلی از ایرانیان گذاشت!  جلال آل احمد با اینکه خود مقید دین و مذهب نبود،  اما فقط به علت دشمنی با غرب  در این کتاب می‌نویسه :« مسجد و محراب و حوزه، از آخرین سنگرهای استقلال…</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/farahmand_alipour/5109" target="_blank">📅 18:39 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5108">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iq3eNiRxNeEzXXqAq-YLiNmRNjwRVYbxAq2iW0R29Sha7qrkbAWI9VNT4v6i9201pOQka1h0aLwEsEc4oECNeAg4-ZHzXozfJbsvcBxc4FuzqXNt3vTnkvdtjMw_AI0fCSIOw9IvCbG5GTi1Yr4WJBfi3oYR1C5hgrz_odjw1NpvFXzWWATO2Ev99BGL4IziWONUK0mv5EP_z64Cdx9RZB55qniCG3l5OM7PEFpGIlaVfPvY1ptURXVF7BdtmQfUNYZNeJ4AUCVteEWV4A8TmqAUqm1rJA5S3OLx7tf-sqKvs2EKRPpTR2YRMk8GMQjuxMHTOfvwupllIcCbC3JhgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سوال زیاد پیش میاد که چرا مثلا چپ‌ها،  یا به اصطلاح روشنفکران و…..  تا این اندازه در آغوش آخوند هستند و مدافع آخوند!  «ضدیت با غرب»! غرب‌ستیزی! اسرائیل‌ ستیزی، باعث میشه که اینها به آخوند وصل بشن.  اینها ایران رو سنگری میخوان برای مبارزه با غرب و با اسرائیل…</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farahmand_alipour/5108" target="_blank">📅 18:26 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5107">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZI539rVNh2XuwWRx9uUkKkE32PLU6e1dofFevQHmIIRRq5oKZY_uioEtIxKfq0_xF9JagSj67y0gMlZYHZH4rfmb9EFXf1fPt4zon-ls3j9wzPwak5nghfBPM7naYONrkNEDxtptgieVgn52mf23bj_mZTLHXduEZ5BGf7xa0xwt-bh7JdOdPTA7_bFNKqgh376O4udixDuB1H9F98K5dcgwSdkg0eUGGj6RRoM_djXRLllT7hZOQB2Fp8-KI5RvQcqJhECYDUXmJLtGn8rq2k9FUfI3oVvZDunYHHbPC2KVpUCWrVgpy_8YJt45kLAJ4AHNADnW0seCa3ATL0xzjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سوال زیاد پیش میاد که چرا مثلا چپ‌ها،
یا به اصطلاح روشنفکران و…..
تا این اندازه در آغوش آخوند هستند
و مدافع آخوند!
«ضدیت با غرب»! غرب‌ستیزی! اسرائیل‌ ستیزی، باعث میشه که اینها به آخوند وصل بشن.
اینها ایران رو سنگری میخوان
برای مبارزه با غرب و با اسرائیل و با آمریکا.</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/farahmand_alipour/5107" target="_blank">📅 18:20 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5106">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b7e3e4f1a.mp4?token=RZ7v3qu6cxQPoG6f8s5rB7jgfVo57wtTg66DpPGbFb3R3MLycKDLRbu1N9QU4fW-pCfXx7RTeqnHGrn3BPG5inLgQ_RByw7W4X1dfoGggrCCo1dtlJLaNqaWSStN_Inkxgkk7xxs_V0VTdMQoiJnRh0170N6dpxFkJVnacCMVKXmnEq6JVTZGQuNCt9z1qKnhIeo55jRMxZr9ZHp5cdthne1kiISlx0UTWr6qrM-wq4MKt1SGGFzLjiCh0ZGsFWAyBT_s_IfKaxYVD29OZZRgTKWcBr-SdteLGOkTHW5fmvORV9KddoJu-sKX92O2_I8iyhMOsD1JrUQDxvV78cGYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b7e3e4f1a.mp4?token=RZ7v3qu6cxQPoG6f8s5rB7jgfVo57wtTg66DpPGbFb3R3MLycKDLRbu1N9QU4fW-pCfXx7RTeqnHGrn3BPG5inLgQ_RByw7W4X1dfoGggrCCo1dtlJLaNqaWSStN_Inkxgkk7xxs_V0VTdMQoiJnRh0170N6dpxFkJVnacCMVKXmnEq6JVTZGQuNCt9z1qKnhIeo55jRMxZr9ZHp5cdthne1kiISlx0UTWr6qrM-wq4MKt1SGGFzLjiCh0ZGsFWAyBT_s_IfKaxYVD29OZZRgTKWcBr-SdteLGOkTHW5fmvORV9KddoJu-sKX92O2_I8iyhMOsD1JrUQDxvV78cGYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت
جمهوری
اسلامی رو :))
با یک نامه ! بدون هیچ مصوبه‌ای
مجلس رو ۸۰ روزه تعطیل کردن.
«اگه رهبری تایید کنه …..»
اصلا رهبری وجود داره؟
رسایی می‌دونه وجود نداره و خبری نیست!</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/farahmand_alipour/5106" target="_blank">📅 18:11 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5105">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d143286b29.mp4?token=VnnJ9Pik0zIuI0QdtYdP0KAzk-WM7YkTsl8ovoOsnikjRXyqyDEEbCF-laIaqgOd-cdI88a2RDUE45Rf6fITzL2mK-ntpBdvx-PeQK_6E2CHBjqf0BU_Imwa59hJH3l9vbRTkxoHYti10lwSNzFHBVD_R0XP_pyZqbF1rYqDkj_hMPcn0X2HEtyDdEB7vwxfqCFSM8ER9-YBXXNZ6XxTXB9goV0i3T_Nlq71RUgH4oc2gjFdOrhdvhTsbv23b2iAFyX1t4KBx8RFXNOu7QH4idx7Jl_q_vxj3aKGqkHs9Re_Vx9OqHhLNzlGu9SkQ0xWUgzCMeFr-ZuxCRNd5zRbmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d143286b29.mp4?token=VnnJ9Pik0zIuI0QdtYdP0KAzk-WM7YkTsl8ovoOsnikjRXyqyDEEbCF-laIaqgOd-cdI88a2RDUE45Rf6fITzL2mK-ntpBdvx-PeQK_6E2CHBjqf0BU_Imwa59hJH3l9vbRTkxoHYti10lwSNzFHBVD_R0XP_pyZqbF1rYqDkj_hMPcn0X2HEtyDdEB7vwxfqCFSM8ER9-YBXXNZ6XxTXB9goV0i3T_Nlq71RUgH4oc2gjFdOrhdvhTsbv23b2iAFyX1t4KBx8RFXNOu7QH4idx7Jl_q_vxj3aKGqkHs9Re_Vx9OqHhLNzlGu9SkQ0xWUgzCMeFr-ZuxCRNd5zRbmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیسی، همون فردی است که منتظری در دهه ۶۰ به خاطر اعدام پنهانی هزاران زندانی به او گفت : «نام‌تان در تاریخ به عنوان جنایت‌کار ثبت خواهد شد.»  در دیماه  ۱۴۰۴ نه منتظری بود و نه رئیسی، اما خامنه‌ای و لاریجانی بودند و دست به بزرگ‌ترین قتل‌عام ایرانیان زدند!  …</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/farahmand_alipour/5105" target="_blank">📅 17:21 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5104">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">«دست خدا عیان شد» و این صوبتا</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/5104" target="_blank">📅 17:15 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5103">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ajtc0ZBaTt2Y2wv_FOjqhZSRpryIctz-0YwIjJ6g6Wg_8LoYyeNrmRb-C2qZyKrBBCjjE6tb95fdKD912ROlFXdeHVIeL2JTyhx8z7O8eQTuVGkb7FaRkj-ZNgaghJ3lvvUQO8uVgpKlppXfFA6gbpTUlcA_fXRTSxxSiwudlU4d0OVQ6TsGltIc136TohQzCLT0o4IhbZUqnjqpsDCLbkXEPWIWOopfkru7Rs2HZnsTaUq9exbhuxwS8ePmBE893wW5iNgc-dXvpA0KdzKHeIscphHwqZMrtOfb41tkH-flqixy1y_B7PNuvFx3zgjWIdvAMwnq2VbB2OEBS3_5_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«دست خدا عیان شد» و این صوبتا</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/5103" target="_blank">📅 17:05 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5102">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">مارکو روبیو: پیشرفت جزئی‌ای در مذاکرات با ایران حاصل شده، کمی حرکت رو به جلو وجود داشته.</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farahmand_alipour/5102" target="_blank">📅 13:53 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5101">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">توییت سخنگوی کمیسیون امنیت ملی مجلس! (مجلسی که ۸۰ روزه تعطیلش کردن!)  فریبه آقا! فریب!  موشک بفرستید!</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/5101" target="_blank">📅 13:10 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5100">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SoNnLCCgINDSFZ2Vhl2Ko1SfySzc50dOEOSsPkGi1608iSFIjqfDhVS9_ZPTHF6D7qE3PCQXtF-5b0D4SDNDaSkfzJ-gfwz1GYq-ndua3v8fnJTToscvuEEN5tCPsfIiaB69Fo1axFrtK_1Jh_74uyS7P_xZ8oa4XSTuUGQzI-C3EPjF4OeWtu-EfvXJOMPYgkmE6Ji7AzV9xVLzgPnuHyy6Q4T6N_ouYmpNREHLjIVApSowniELbzcNDxRz20xS3zBNHQMmIQeoTJN1kgURLc5yamZD_VzAX8LgmrQgAGI2zROgTVoWTD1l_JT4_fl_mBa_i73Vpm9NwKTDc_Enmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/5100" target="_blank">📅 12:57 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5099">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eGyyUDTR_48yHoIWX178La6KQm3Ud5cmMzqLfUl3KRtggsKGe1gy1qGaRi-bb2Rd1jcgSQVh3X7r6mkNQFo6WVQO5C_1WXyPx7Ser5smMfKqwZmG9QK8HCS8_IiroySoQQwxHcCS0lEqw7SX_ZA7UaUrB-UEQdfeSVz7RzX2-niRt1CnIspU20s2Em9NrjiZSuZghq8pV0ZlqDiUPqOihSYmekjDHk963hVMq1bk7lWgrtmW5Yj7aIrcRzM1Xs14X4SofesqcfaS7SI7j3ifl-Lj3vLcnZ1xKvSLrSv_t6pFB8uCDo62dYjrIaC8qRSbklYEgzA4RHduzjxeRTs3Jw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ca3794683c.mp4?token=Q7hGFg1-D0zg5PUzBZ34Wv7Bg3AOhEWVcJzdTOThcTWcslPJEm0xE_EQaT9AIz1rlxf-gz-cS686NaeqgOFeMDgGqSf-0a1vDdlK_YW93_ON4SxsB3yyUmCh028U8y90cV8IV0tNY1ZJiLbmqnMyB6M5H0FPf71BnYxdkMSrtmEGhxnC8oBCTO3G_OfzyRXDGOPZJNlgGNIC3ARV5MLiiaq6BmtduD8eJCGgb1PQQYWuA6MUzFcXnrNdw_mYVGhjxnaO_FndAqz1N9QteV9pcPli0Z-2XJqMm8QlyOzbmZpDxMqaJbDoBb7IHmJVVfyhFy5rAzCOjjPq7wLQspTMOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca3794683c.mp4?token=Q7hGFg1-D0zg5PUzBZ34Wv7Bg3AOhEWVcJzdTOThcTWcslPJEm0xE_EQaT9AIz1rlxf-gz-cS686NaeqgOFeMDgGqSf-0a1vDdlK_YW93_ON4SxsB3yyUmCh028U8y90cV8IV0tNY1ZJiLbmqnMyB6M5H0FPf71BnYxdkMSrtmEGhxnC8oBCTO3G_OfzyRXDGOPZJNlgGNIC3ARV5MLiiaq6BmtduD8eJCGgb1PQQYWuA6MUzFcXnrNdw_mYVGhjxnaO_FndAqz1N9QteV9pcPli0Z-2XJqMm8QlyOzbmZpDxMqaJbDoBb7IHmJVVfyhFy5rAzCOjjPq7wLQspTMOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5097" target="_blank">📅 10:27 · 01 Khordad 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qS4spMdIO22qh1zrZDiW5MIWjS0tnNlkRAKJcPZ7wegTC8iBdokTgsBdWmClwRLKU8LxJhOV0oSqhWdsWLAsiLWXVapSRRVb194mof7esexAISAZmhi_NZM15MlONTh3EAEqFAWfvdqdApVCEWg4Nf0myNq_1VuN20FOJS_t42FBEJp-aIqG8UPaEphDbxrruq7OoOPNYkRMoRPbive0GuEo1e3sQnLyM5j7c7t52lnUoVjdyNBf6BTn6qI08qnguZQZ5ebR2NbVk7CsUpYo_d5nC2XMqAEIGSPTZiutVHeBLsLPe9m-BIRQlwW_ahwFfiOFl-K2n6g5g5zU-aOAnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5095" target="_blank">📅 00:23 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5094">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oA1RhpdbGSWoRlj9qj-4JY2piHY6i3RWp6jp1fmqsE6Bz1ThiShncn9_EM65j-N8pYrGvbOMImevq966uyS8-gc0mnAr835uMKV3IY2d3MKGOXg9fe5dXcpmKDAKHTfw0fjUZfl_Kd_Ffi_kGuGHj60sbNyqEQ8dmp3sEMiMl07rBNLuoUHrO3FeunDWqOJy7ldD6m0Qw0ZI5X1eoWMwaK9DkRNZ3pjGKfYysA-82yjKUx1b8XRjrVQD-rEBKDF0U-078nplzLQiOm6PjNDKDeFVssPWVfJQUJmOGGyTFqiMb_1fDIb_qam5nnnjDcPm23A_JZo1BjQ5zA_LpVQmsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از پیام‌های دریافتی</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5094" target="_blank">📅 00:23 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5092">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NG4ITYH5LYLsGezeoXDz5ambK94QQiM2MZ0yChltgvqyn0DvaFLy3tLhvkps1xuPupR1yQBOKaoxwa3DPa4Jwubcb-Ue_sCvYbsR5M7kAO0zD9hOzORY-o6j2-GMiyzGaqzjlbxi-8m4JYfRCVxSeIAJW4MXj9UgoizpqFCcVWiCPBVoqL24UB_KZ2KW2WZGe7pWPzaXLSqgaBIg9NkcCrQlWp_VuzKnIBdi18uwPGOAc18k2DUX8DM5MmOKpD1uSEcoMR0juVP_gQgVinbi-VRV_nL77GRGuEr57uXCifP1O7TJZvJ_rPQ4lBcDQDB42F4XUXAUIEctVXlje3-klw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از پیام‌های دریافتی</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5092" target="_blank">📅 21:15 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5091">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u9UpjV_lpsOuNlSp26dd_0xKdMj8gy8ECMo3BQVDj_K45Yi5_Yr33MT1UMptZJdAwpRuiaSlKniyI9iPCn-SuS0RYPDwbPQUXE8dEgtTxrYkJRd5flm0V4tIf8qqVqBUnMgR0KnqUAgvJV0a2wkIkjdjJ9ZL7KLBt4nWo-VN2mzL3L1clS_9vdCWsh09z3cFyP28bDhjuJmLSYoMMHmHAL6WnGVkXgQGQaHVVzc4ulyauff2OOmTnr5qF5SdtpTYFRo9UMI6KvIRSfvSx--UUHK5HsnrmJgjJ0eYpZ-gossGWiVve4aJQV3wxUB75GY8E4j_sgUjjK-cBcycSm4hkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر بار مطلبی منتشر میشه که نشون میده
گزارش نیویورک تایمز چقدر بیراه بوده و بی‌پایه</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5091" target="_blank">📅 19:37 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5090">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cGFmKRAcTwfJUdugebtIyrhfuuGJFzP7Jx3_coIFV9KDM7DC4c7zp_8C9jakzvZYCzzCJruJ-ImtI0czlLaDOyPSHO46_VIqXBazap3uR-ACQTxxfmeNxoUDbbSKQmTSKCNFj0DfgIJx_9CjXHZvCJaqgYY55b7Zz1PY_h4q0IX-xRaWzZwcxpOWLclGPj8p2wHOj1N5JTOHdJnLddYF9-Km_ONhvMrYzkz72gdRtRl0P14HJFXwHBq7CX_TW9skFvvJgMXygPNmPdafanXdR9P0w3h1ZdZ3qpZz4Oy0bbSTObqzi87lNLcMdEi6XnTtm2P5nD592e5zP9D_c7t7QA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی رسما بخشی از سواحل عمان و امارات رو هم تحت حاکمیت نظامی خودش ترسیم کرده.
از اهداف اصلی این طرح و نقشه شهر
«فجیره» اماراته که برای امارات راه تنفس و عبور از تنگه است.
تنگه هرمز، تنگه احد شما خواهد شد.</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5090" target="_blank">📅 13:02 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5085">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZS5Di8DiJnMANKJIYPyzfDCNdFPRdwtyV1z-1SYzxWRIm80Ucon2ZKyRs2-7-x9OrFJw-jL8laxZbkBAMLmyJ86V9oMrnIeLJDDPgT90byZUY1tdKguM3qGlOnU3LLhYbBeOlrpai5WlqnsoKJZ3RnVcSO-wuTBcHgZuUlEHxvrTP0zBhO1sUGEMEAS0XHJowwX25dyl5STpJZsdGYGPkB-qVOb0p4-YMsINioqedYHiBD3AzGtuffmdXWjPbtxYL43hhY0SPmc1JBWRrFCNfIPGswYxqN9HTSx-IKAlbIsVuL95_YiVWBkgAzIJIvJQPV3vVXaKfhT0hvtPdvSLqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dgnMeeIroRPo38EkjXyyQIyJVXbdHfnUxzaQCWHYCPrUdYOczzdbrD5dCtdvI-HryFZR8rymhbr8FKjX1_-C_7Sh1ycPfhqSgkfH2_EPznG5_URMwagQBofJDQsn08sXNjPB8WNxe_8Zb97e8N4Q7pgMDOthuq795spXIBiT_oDNcC6Oo52bP3kKdA93R7BWjlQs7DGMNgAxYPTvFTdvm0v7GFv_ewCR4XiO7c7VXuM9fQ46gxCwItUNZ9r-eKrgewxyqXhl3MHQs611lKZclRwEMLbzJwGsFGRY98vGAPdVBixpzwePHBjfzpHblS-Pz2R5wMLCNNwDhUZ0qCkhBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rURs00bqKyl4Ln8S0JFYrGn3CC35loTXfVdGYUJa_HLldEsFmIFJZHH7z7hH8K4j2IwBlQrG8tT8_z-DXQMxhPDlXSpDu8zpMOphoAIBINOmFj7ARRp2FTUMTt6T5pYE7qJ8X4FUbgYdn18o8PDeR3e7pSYIkZd83BQcDJ2SePnT71Zl13joUI0ezbuXMjCPyTQdKwXcbZToLz-3BlaMjjKfQ_Dqf2dkFGQL2wg6eG8XEHWslGgV0fL5Q0CvJpkVtMrSx5ti8RYW9H0Trno5EwaENxRqNQmbpuoeoVIsOhiPDfCMPtoA0vfGuaF26PAFYksyM2p-xwD5WjEiDvGOtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WkHS9XG9wRIz1ld-Lf4DYeXvy3SjhyM185jXFFo05OTrvNBR7GOdL48aNFR61SyMiZF8IkF-Zv-4KDipfQ_Y_v4Yia1FVQ7GW7xH3tpSjVPwPiNljkUEPSyLZzMlZkNh09iUe6BSFtx4Z1y40BL2TjN4eppF3kwnYy6HylhHDGQzFBjmH8y2mlZbiM2cKjWGLJ6h0mug_3LGGBD_-0RyX199eOzsEg1oMxRmsEKjVNcKsfThiojudU_LiMc7E_p5GsMQm4BOxFLSJ3fjySv5k5HdfQYouTFQ4k4W-wr-KXGhwed7iRpGYs4Mbs4oZOjoGN3Zvt7DJGBlLA6KIiIBEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SA5ynTUgL4IpkTSpIaFUKrIzpjwJyJRgLXi5RD6YLRiBlHrW7GqxKHXZSitNkkWulf0bUtv3gJh1CMtNT8jSIt_yISDzXmP13KDLDtaEgnmYGMooglfrV_5PThhQs4gcBQ9zC0B5ZqrJFDsH8SrxWK9OK8U1xHZ20_MRoQcclhJBzNNWW0cQ87BI4S_WwJXj3KT4ARtpO2Oo0FYgKDMfi31R9c5FKlx6dyfnSMMmR1Cl0xsHfTgoPn7OIIqDBTDvzSwhlzIC1bfsKm47VOHSXKAmFJEVqahEDu6H0tJTeopViZmIVpUuNzlpMxpFUDgeV54sEcqWTQ9HTA-pfi7H9w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">'من وطن‌فروش نیستم... زنده باد جمهوری اسلامی... تا آخر کنار ولایت می‌مانیم... این پرچم با طوفان نمی‌افتد... سقوط این کشور را به گور خواهند برد... عزت این ملت معامله‌شدنی نیست راه مقاومت ادامه دارد...'  تبلیغ «وطن»دوستی در «کشور جمهوری اسلامی» با شهروندان وارداتی…</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5085" target="_blank">📅 12:29 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5083">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IAaOCQFF9kwFA4ApXhiQ2W51ar5eLwssb02plsksVTvi_JNFcRS6eUpy87j2oZM2C2G8gg4x1JHYaywMn5_IjFCKdHH2R9Zn9u4PIsihxRrN3qEqoTE4XhzNth7_MmY2GV4Zera5c2r6VeWv0tvhmti9ux95UWONDyYo-wKt7QN07d8i2pEQ2SU2W1QMYno_S21Dhktm8AfgBS9cqRx5CMkoexiCN9DwMXT9dbiF-0ESXI0f4pssU8SsUnjHux1VEC7Cmq60VF0oAVIo0a85CXsY_XtIIhqXtWsHUBz3dF9SjN8HqfpMfSTJR3TCAG8ZfGJ10iy8B-sfetYgOLzhrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54c0c9f59b.mp4?token=KkFBrKz81wJTssJR9rf4Th15xxQSCRxZwM-3YTRhfVntpR5SFq-x5axjNzcqVh2ugIImO1c8iEulHhXnZpGVYzho4hbci6f1WHZvSaFwpoUzzTyjzel-ybfJdz-JzdUJEFqgr1zQHsXINN1WHsIqrsLcxDC-bLtolBoJ8ilXT-o0-eB8vK1l2uBY0BwqegF3GayZx3bePt7al-LeWGG2OaEiDFzqq2pdGbvxpPn7-mYUdoiotB-J0hr9I6peXnJ0Tm3Y2BjyGhX0z71QNj7-7x8FuHW050X8Mnnwfh5ZQxhA9STJ-7tf0_EhRidZjiHgbIWhDGaiG7ZXn_xxXmVDPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54c0c9f59b.mp4?token=KkFBrKz81wJTssJR9rf4Th15xxQSCRxZwM-3YTRhfVntpR5SFq-x5axjNzcqVh2ugIImO1c8iEulHhXnZpGVYzho4hbci6f1WHZvSaFwpoUzzTyjzel-ybfJdz-JzdUJEFqgr1zQHsXINN1WHsIqrsLcxDC-bLtolBoJ8ilXT-o0-eB8vK1l2uBY0BwqegF3GayZx3bePt7al-LeWGG2OaEiDFzqq2pdGbvxpPn7-mYUdoiotB-J0hr9I6peXnJ0Tm3Y2BjyGhX0z71QNj7-7x8FuHW050X8Mnnwfh5ZQxhA9STJ-7tf0_EhRidZjiHgbIWhDGaiG7ZXn_xxXmVDPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/add91fa506.mp4?token=fcCfpkDndqeyeM0-8oxkFnJ11cXcQ8hzn0gbH_wKOFdhe6K9PqypX1ocuScmef-lIFM5q5Fi1Zy9VjkR_slg7PRvqCpuUj0yx19lp2nSoAgYbm_LiPorpdbEViKq99CF5j6TU2a7DgoCODrZvqo-XCGnBj-WBZqV0YJwtuzH4uJ935Wbqva0P4Tpa1fRLD2d08qVUNmJpmGMLFDfC92KnUsa8dwk3_V9izsMyw_xeP5kevmMp03kYGP07DOWhnjggaYgFP9lhXwoEJeXrczfVrynU37aBfKGgX1TxtV0hTySmbK_4hm37S6aB8WHSpwkoVmrFsNpbjhLlYx6wbnr8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/add91fa506.mp4?token=fcCfpkDndqeyeM0-8oxkFnJ11cXcQ8hzn0gbH_wKOFdhe6K9PqypX1ocuScmef-lIFM5q5Fi1Zy9VjkR_slg7PRvqCpuUj0yx19lp2nSoAgYbm_LiPorpdbEViKq99CF5j6TU2a7DgoCODrZvqo-XCGnBj-WBZqV0YJwtuzH4uJ935Wbqva0P4Tpa1fRLD2d08qVUNmJpmGMLFDfC92KnUsa8dwk3_V9izsMyw_xeP5kevmMp03kYGP07DOWhnjggaYgFP9lhXwoEJeXrczfVrynU37aBfKGgX1TxtV0hTySmbK_4hm37S6aB8WHSpwkoVmrFsNpbjhLlYx6wbnr8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/5081" target="_blank">📅 10:25 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5080">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">'من وطن‌فروش نیستم... زنده باد جمهوری اسلامی... تا آخر کنار ولایت می‌مانیم... این پرچم با طوفان نمی‌افتد... سقوط این کشور را به گور خواهند برد... عزت این ملت معامله‌شدنی نیست راه مقاومت ادامه دارد...'  تبلیغ «وطن»دوستی در «کشور جمهوری اسلامی» با شهروندان وارداتی…</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/5080" target="_blank">📅 09:31 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5079">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/48d635b5ce.mp4?token=V-5Me5wyXRmxibgt1IvnydoDXVYW8Mb7C8JaX8kDCWQx7fTj5GF4A3p49HyZ3LOFcytl2ie-Z62bpQeN2fLC92670szKR6r_CamKV1NN7tlaLSv_k_gSf9pzlrK19WjNezX0eF0Cf68aUf12xQXwaIvIK50Hrg1ulvAz9GaJQa1s_REifpM1SFYXEZ_gYdv1T8-X4erM4_Y172fK9UNyFy5xyDyMODF-xrfu8bgMM9DguSKBetM4CbV3mczM9E9lf_7sbniQUwicgQQZFCMhdbvPJlxNLztf6lKstMKJvEAkrScbMWdcucHfEMbogdLO05x9lU9gzinv6QGAxK2a5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/48d635b5ce.mp4?token=V-5Me5wyXRmxibgt1IvnydoDXVYW8Mb7C8JaX8kDCWQx7fTj5GF4A3p49HyZ3LOFcytl2ie-Z62bpQeN2fLC92670szKR6r_CamKV1NN7tlaLSv_k_gSf9pzlrK19WjNezX0eF0Cf68aUf12xQXwaIvIK50Hrg1ulvAz9GaJQa1s_REifpM1SFYXEZ_gYdv1T8-X4erM4_Y172fK9UNyFy5xyDyMODF-xrfu8bgMM9DguSKBetM4CbV3mczM9E9lf_7sbniQUwicgQQZFCMhdbvPJlxNLztf6lKstMKJvEAkrScbMWdcucHfEMbogdLO05x9lU9gzinv6QGAxK2a5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">'من وطن‌فروش نیستم... زنده باد جمهوری اسلامی... تا آخر کنار ولایت می‌مانیم... این پرچم با طوفان نمی‌افتد... سقوط این کشور را به گور خواهند برد... عزت این ملت معامله‌شدنی نیست راه مقاومت ادامه دارد...'
تبلیغ «وطن»دوستی در «کشور جمهوری اسلامی» با شهروندان وارداتی از 'عمان، سنگال، غنا، کنیا، بورکینافاسو، ساحل عاج، نیجریه، تانزانیا، مالی'
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5079" target="_blank">📅 09:04 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5078">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tCUoNe84JFdOR1zBadbpVv_MYRrez47LYDmtqcI3wNwxG_tKHgH_UsY91Sx5ec4kARU6qmMmRHbIorMKPz9GVgGI9lDLOk5qOKUN5rrUWvn_f-ONYhBw7mYSk7LTdbpBprxsw7qM6vYQCIvK07XJ7PgHDQ-xhykvplJlZ7sZKQivRZ3hxqgmHtSxMUXDGz_kc-oxmnpi1uYZRJqAeq2n65yhPoiaF0LiP1_GNIhFSyEiOtE-aC1TYUgiOAuv3of9SPwdJA5IXEt4uB-SkuxQPyl7nxznu2_9p1rJl1TOLoOsyAxOtMAl5eCTApMx4VLgVUDAgplyD-otXr1KkpjzSw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/e76a3523c2.mp4?token=Wq8YAHK42ap5qLKPBwKup7ucWGRsoYdeBJLi7YJJOzWxEGj9AO-fAUB8gXHi3-g6vaSbTV1dfbq_Zis4ot_1CHcrJv49jEwJbpjGw6KXiIgRXYKJ8G6Q5tVThZitVxcUC0Wa0XsauPPuAFzOUfSpfJ8WYp_Xd_8PJLPn0_62jq--IMnErBuP56qhjNlgis54NlcCKxxkJ9Ce3zOzMLPk5UWvuNav6YlDklPtkFKgard0TFbwKkbkkHC4c56x1sepOk9dO5HJN0y0dmSqeyLwMd12j8RixIUYH7fOkJr6gFjzgK-S1pnZpMmWuirzQBOWndfA7CRuk9QvDvAirX5csA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e76a3523c2.mp4?token=Wq8YAHK42ap5qLKPBwKup7ucWGRsoYdeBJLi7YJJOzWxEGj9AO-fAUB8gXHi3-g6vaSbTV1dfbq_Zis4ot_1CHcrJv49jEwJbpjGw6KXiIgRXYKJ8G6Q5tVThZitVxcUC0Wa0XsauPPuAFzOUfSpfJ8WYp_Xd_8PJLPn0_62jq--IMnErBuP56qhjNlgis54NlcCKxxkJ9Ce3zOzMLPk5UWvuNav6YlDklPtkFKgard0TFbwKkbkkHC4c56x1sepOk9dO5HJN0y0dmSqeyLwMd12j8RixIUYH7fOkJr6gFjzgK-S1pnZpMmWuirzQBOWndfA7CRuk9QvDvAirX5csA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ در خصوص ایران : همه چیز از بین رفته است. نیروی دریایی و نیروی هوایی شون. تنها سوال این است که آیا ما می‌رویم و کار را تمام می‌کنیم، یا آنها قرار است سند را امضا کنند؟ ببینیم چه پیش می‌آید.</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5075" target="_blank">📅 20:21 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5074">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromVahid Online وحید آنلاین</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4c1cd69554.mp4?token=q30vapkrlD2t20a8bJsSyc9whpmdrpLrZt7Ye9URlGLtAFzYDopHerfdYRYk5all1kl7xWazooK8fK5vw3okh2v0ZsCPgMAyl8xUs0AkRu8kkscNSNt2L9sOPdMiPL3Y0F33zGLU24bORllNYGIgjTfKxkecN3WHJN8ua5usArVTBkttx0TMdX8Wao3WSzksuJ0cVPxge81uGZUPJ8hT8wO_V721X3AUjjb1_eCVP1Jh5IcXpHbbLLmEBM6YiJEh1watEaJCVTQaBwbuJicndP9Rd3sM3Hbms7mPp_YSE516r5IAw94k0L0UpRLM0dkHGEPtMxxfjKfZ2uqzkkZyFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4c1cd69554.mp4?token=q30vapkrlD2t20a8bJsSyc9whpmdrpLrZt7Ye9URlGLtAFzYDopHerfdYRYk5all1kl7xWazooK8fK5vw3okh2v0ZsCPgMAyl8xUs0AkRu8kkscNSNt2L9sOPdMiPL3Y0F33zGLU24bORllNYGIgjTfKxkecN3WHJN8ua5usArVTBkttx0TMdX8Wao3WSzksuJ0cVPxge81uGZUPJ8hT8wO_V721X3AUjjb1_eCVP1Jh5IcXpHbbLLmEBM6YiJEh1watEaJCVTQaBwbuJicndP9Rd3sM3Hbms7mPp_YSE516r5IAw94k0L0UpRLM0dkHGEPtMxxfjKfZ2uqzkkZyFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ipE0cCNyXWPhSj3VK0ogEQiLCpBKf2wGC8aOL2UBoYGQJaBmKdr-PomQzWwyWKfXTKrzeLTjs97eaOLXOZx6L466OlC8zGZUCWNOYLiH8t9_lj0-YCTQt3zvcH4qQnad8jT42glwDklO8_ChdLWRt4m6GSOA1IVHkLdFdDFbLoQ0882y1vjN7PQNE82gsCmoNeCfNXZPyIxTuvbpKSnbcEleer-5WxCPP5i42b9VU11DWa7eTEn-aHkwlp2fRXLqqV-0kcgh0MXJHnLEBLnDhTd0M6SZsvH1oPZaE_9nfOFfjeE-BwHwKMWGDHjKYG1bnv5H8jWMlGV7OJww-_5EnA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q2FhtfpjWDwTTAdJOrTSKBehTo98MCQeOLVrIS7JMVwOqqfY6k9LGfm1EpmmY30DrK5kBhBOEKoAo0UjB5xX8gl7HwUYfBHwx9ADpwJNcQW9wA2Ts6YE29rApShC7-09vZ_AEE5X-HoWoN-FSGUqeX0XEswCeBvZKzrikZy7uwroiSLS_gU9cOzYmtMbc3gxqca_YXy7H0FIqyItGVhpznEtAJ-USrDI6Sa1KKjIe9_BJS-YfiL1Ujnq4RPZChZ2EBCVqsEU5CYiLjVy6bEaTEI4quMQNNrBeWYAdW029AcRhtJq376PJesU0_STG3f8wEouhK7_gyF3IoqX6XSR9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">افزایش ۲۰٪ قیمت لبنیات از ابتدای خرداد</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5070" target="_blank">📅 12:18 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5069">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gQNNKXa78oF2Xw-JFJGAR_37JXhrqkL-MUSEpGvp7RprOczm3yuABeuJez9qxJUUPFmVpIZBQ81gTGwWsAKHB0tXEacnd18EemdJRnx0K8L62eubWch82obZ6jirXWXGREw_Gx0NAsYmH5JwamcR_d5wGxn8gILr_zzAZ9Ff5YJhtJdkPRp9xKBZRFrVeQ7LgrfuOcXvlunTiMVdZL1tqgOA7NgDLNLvpl7XkUbxU8ksIHEzB0bnD6U9wVvAWTqprvj7s4KnjTlzQ9-1BHnON5A5c2aLzSUDw0jRmguTMxauCp_zk-etfz7do1q41E9nbfJ60bH01fXa9lwLhqepnA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ra-LuJX82ZWVVC7ZVJXaRFn50KNiXhIiP_ogXdy8OCQe7XqQS9wVrx5ohneXsEjNj_5WOtjZ5Z7iNswCaHrzGGZiWzItMUaP4N1cRzL4NZjEBqzERddxyQdZFdTBeiTurVkyNBEQnqg3AMvWaPas1sMBGxgIoMU4_rjNGojVQ0hJyLG4k_Hl-kWBwyJsY-31heHxAQNe6b6lQnWSYV4tsA0jWQyld4LEWS4Oo_vuq3drPKbUK_0CZn8CvsXk_bvnfR7cSm_0IwXnZjjswQwHgxgplAcRc5hhEqp2M-L1gwkMVhWvexxwVRWiLHwLhGKY6D_yl0SMW4CdlyxZVZwTew.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t7xe9F3nWPIOK3-fsld6i0CN9Ydjd8QwLzFTPW0TnrjVIVFeNpy7Wu3mbnLqgScxu9-HqxwTy4bOnDn-bMvI402it2_joxstm4QTJ1bSraNhLsNQnwWKjO0DtLY-_onJqWWWGkFicDBwozPCtDRfh3YhjogV7kPc6i2JzU8EX2BTDriOdgsrtMYjhJSJkhXbcOiWGaHu_U9l7O-0I3wXgIt6-_x34lx7KTCOYvHsuo4vmGyn-C1aOrqfUr76jwz52ltgR98YUd4leArPKnJMoIr_2swUn_H8k4_fbSwktSmZtw5SEI_HlcQZgFq8lM7c5-6kpknVyInMQ7iQws5mMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IhOQMmHZwAFAkAfRh_9MbKhaXhJzmO47QwFNqhBqo6T7n-TNPx4v38cPN-FxWvhKeM9-EepRlgrqB4arV57OuGIeELUnxCDlAbFaw7Mv0QtOFeyP4l1reS3L5PDPwYk8CSRX08oqC_3QvqxU1v0ok31rxV8CoKN-O5iVy6tYSQWUwRcyXbJU5veLu1XZkHR1mwO-r0SKeT7_ZkuafO7EdG4zwLOoBdQvc7va9U_vFbdhoeFsJQ3WoEjtm13FjWpl6J7fgpTKsAbch_d7u9y4g5AyCwdpSypSwZBNBolaQQ1Ey2Zj20m_bbru7pd70USBFRjuSyJSl6ZLXT6EhahBHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LNBCX8sFvzTsS6U_TNasbvyJGR9ZlhLu5AR6DPqzFMhKjr3qDfo9msRaXTiitgknksXZHAePSsUc0Kd3lMxXmy2_dBvUnvZNP0ciUuNbXd7doyMzxaynPOoHYUj_BLGqPvUWTyiF3heyh0NvhVLtq9kqxxDo0u4GFceQbPBhZeLR5fNQZMEVhas_0LSEkfR61l40ztlgBHv11pF_MOyDSw4AJwzYhNcty1v-l8RcjIYd-nCTcBO2g0cjq9NZunfGrrCKrPtPr6QZwjJRPIepanZiy_SvWq07ldEhmkzGOHiY3eKGI5QmHcCXjADZN4TQn6T8vbq4tMmm7SVXyvpPNQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">صداوسیما روز ۲۹ اردیبهشت‌ماه، در برنامه «سلام صبح بخیر»، از تندیس «مشت گره‌کرده» علی خامنه‌ای، رهبر کشته‌شده جمهوری اسلامی، به‌عنوان نماد جدید میدان انقلاب تهران رونمایی کرد. @iranintltv</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/5065" target="_blank">📅 09:28 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5064">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIran International ایران اینترنشنال</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ac9d9acc3.mp4?token=JR31-G2YrmnX_NvwbERfSYGkV5USnBLJvhcJ7ljxJIv0lUWjAPJmd6wX0IyNJ5jFMNOdoa-vOi7lPZmKOnR_GNsN8o7BsbxgVyD8GtiSadY9h7_h12m_XcAJazb4ge1g3Zp3FgHXYAFhG-4t-scAg33BzCkjrZnPnsTNJEguob0EfYVGAyY6_dIUzOJ7hW3D5eaXOaMWYGvU-5dLnOQ44ylKU83klYhhSd_A47rHEFRnX__-A6tuK_GZygAEXq7QwEejNZKSEHK93D9XkKVSy5_iGlPM8ZPU6_VCk98W6BQqTi2NqRzbRnO-MADFEl_L1b2qpetTVfhGXcJmKCKCjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ac9d9acc3.mp4?token=JR31-G2YrmnX_NvwbERfSYGkV5USnBLJvhcJ7ljxJIv0lUWjAPJmd6wX0IyNJ5jFMNOdoa-vOi7lPZmKOnR_GNsN8o7BsbxgVyD8GtiSadY9h7_h12m_XcAJazb4ge1g3Zp3FgHXYAFhG-4t-scAg33BzCkjrZnPnsTNJEguob0EfYVGAyY6_dIUzOJ7hW3D5eaXOaMWYGvU-5dLnOQ44ylKU83klYhhSd_A47rHEFRnX__-A6tuK_GZygAEXq7QwEejNZKSEHK93D9XkKVSy5_iGlPM8ZPU6_VCk98W6BQqTi2NqRzbRnO-MADFEl_L1b2qpetTVfhGXcJmKCKCjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صداوسیما روز ۲۹ اردیبهشت‌ماه، در برنامه «سلام صبح بخیر»، از تندیس «مشت گره‌کرده» علی خامنه‌ای، رهبر کشته‌شده جمهوری اسلامی، به‌عنوان نماد جدید میدان انقلاب تهران رونمایی کرد.
@iranintltv</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/5064" target="_blank">📅 09:26 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5063">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tp83FwaoUnaaggAB_w-BJVabnu7uBxgUddHp_6QWNUwLqtvGs2S9XQElrJ1Ix9LIgtdSQGh6KKWqmF0evj5MkkmyHQ6ijUHImebxDfU_mPGyFjbz8doqe6AbOiJI4WeeIpGFu5i_eOFZ-7Ry7k2ULcpUTuLmPZBYBgRQ7KZw7w0DKgtfNjhTKos_1rTCILxgKX08U4NKDDOxrTjI-rihScY6hw9Z8P3XH90mUwP2OIy_mYT0h_UOsBvb_udh2yyf_9HNqnOSoh1DVPudTqb1-znapefMNlnXebV3uKifyLbOnROehyb4MAoGGbNm91xAKnRYb-lx244XweDxim-KQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«بهمن فرزانه» قاتل «الهه حسین‌نژاد» اعدام شد.
الهه حسین‌نژاد در خرداد ۱۴۰۴ برای بازگشت به منزل سوار یک خودرو شده بود، اما راننده او را ربود، به قتل رساند و پیکر او را در بیابان‌های اطراف تهران رها کرد.
«بهمن فرزانه» ابتدا انگیزه قتل را سرقت بیان کرد، اما در ویدیوی کوتاهی که از اعترافات او منتشر شد، دلیل این جنایت را خشم ناشی از نوع حجاب و وضعیت ظاهری الهه حسین‌نژاد عنوان کرد و حتی از واژه «بی‌حیایی» برای توصیف وضعیت الهه استفاده کرد.</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/5063" target="_blank">📅 09:12 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5062">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">روزنامه آمریکایی نیویورک‌تایمز به نقل از مقام‌های آمریکایی نوشت که در روز نخست جنگ، نیروی هوایی اسرائیل به خانه محمود احمدی‌نژاد حمله کرده است.    هدف از حمله این بود که احمدی‌نژاد از «حصر خانگی» خارج شود و پس از حذف خامنه‌ای، در موقعیتی قرار گیرد که بتواند…</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/5062" target="_blank">📅 08:56 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5061">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EuTeUNN0hWTJqGWcD3YTvaCNzPlMUUZ8PSGdEvAq9qjnZDkWcRPXPElDO-a-Kmvk2kcIYs9TjzLLkTSd2vqjU1seBHgmEWhjJbtmnH75lxOLd0h4mYcfq_PiQ62Klcxjkcun9wDl0BL7pEexOcTJMzFjYxmwnuqdQMgWI9JVt0Q_19BVqhHlDphCTGWDt5lXFWhiqXlpUJkrUd1OpnajtlaVGbP28Igyf8u8Scg5ycV1BUf0fmjOMLVJT1MaUjXVA4grSM8lfK6stYB3WkTjTOQyEqP4vl2HkQ6N6z6hqmn8cyxrmfIwOTRZhoYySya2doiRX38tjR85KPVkV_zsJg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/krz2otzqSkXMcMdY0c5njcTbMvNMrIEd7eW85UlX8p2gswReaAVfKU858PPpzjLfNAOzT-7z-BrgfyhY66UUsClDZaLnSOZtz3oaAW_CLi9fQr401mL0JIq8dT8G9mo_Oeu95YokyngaHymkBAN6WFbMULrbghmhHqcsKKHUn9hEkYBakCGJJdjWmssdvCGGSI9KZsQ811zCpDStMhAaHrxiGxX_3LTCqMMgIalH_Yq0_c5yBpA8DLT1ofvI-tvC_ti8cdScJSQ4zZVimcUBogaRUfnU3yHDi58leaEkJeDMeDEeXnRRWNoz5n6Ene5NKJ9Itf_EIfg2vZ696h3Y7g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5056" target="_blank">📅 18:15 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5055">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AAtDnRfkR19P-mGjjDNEuzOq4Ntp_Sukj5NRsdmm0ABA6e-5XNxT3WLtTLUUqaZmYF0FYZEIN8QaMAfFywzgq17CYom7LKRghf13V6SO_zoaP7SO70h_KkmV-fQuX6rG_ab0m2T8IQrZMqKqJg7OkxPevE0DjiEH6KR0F5p5HoTLAq5INYvXZQPlSveoP9oM-nMTIgxfdgX3aq0FTgywnL_y6BH54ayFO007jsC-wzrWlPl0LNfsvtvkom0YDtj_hlw4R_y-2YnrRp4BtLg9JXUxaS6Nxzs9723iU9lLgslWv_ywiNRrEdmKhrkaYYtAhhWgTgHBRCHcpDJNh3E3SA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/03ae416835.mp4?token=HpZUvpmc0dIMur2y2XfdZiK49kc_wOfsFSUCi8OT32YShflsIgMaa_1dC2MLQF5ZBWEyGVBPhF3PB-2pR1Ikt-JYZubSUxeSWYhK8a4pICNeHqblm7J8Te-so23SxMoJXHXomFzDJ_erw1F345CcInf2jKADl1mD3PNVXuy8asUBpTiH-eEFAZ7KOpXeKFYBIFr56DZZPMAmxxncnedCEnlvoy1QEeOnTI0jbmxQ-y0zfRoSSBpBMOGYBghTz9K2Wj4L5h_67rGsMyq-ftwxMTFCg2KBb5qnDS37ABvWwuKjox_xOjrLfYnVE7EIUVnZxKSVNbWmvvPCD346CidVPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03ae416835.mp4?token=HpZUvpmc0dIMur2y2XfdZiK49kc_wOfsFSUCi8OT32YShflsIgMaa_1dC2MLQF5ZBWEyGVBPhF3PB-2pR1Ikt-JYZubSUxeSWYhK8a4pICNeHqblm7J8Te-so23SxMoJXHXomFzDJ_erw1F345CcInf2jKADl1mD3PNVXuy8asUBpTiH-eEFAZ7KOpXeKFYBIFr56DZZPMAmxxncnedCEnlvoy1QEeOnTI0jbmxQ-y0zfRoSSBpBMOGYBghTz9K2Wj4L5h_67rGsMyq-ftwxMTFCg2KBb5qnDS37ABvWwuKjox_xOjrLfYnVE7EIUVnZxKSVNbWmvvPCD346CidVPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OjNqa7fu1q3EDB3ipgldjV3XXckj9mOw7ams4WoNe6g_Do7yr_cVTRt_qDJ_VqOFtU7SamVTHAMtuWu64_JeMGC55vba7SVoyNDUUsVBnsnPDX7iIhB6V2HGLmUHdYVhKCk5eWqk9Y03336ryenDxB6q8gwUdtj-nf9Gi-Gqdz4ZxkubEqkxqdo9FT4-APJPKbvmf4rvsgSV_Fl-qHwzuaIg8yXT1D7Cko34-Ysm3NDFA8-XWXSl4PwDSiRDc7OJ3fWpwwe3GXemeXA1W5wFwB3bOhZxWloNLLS6YolKA1KJh6vLv_6IuoHH9fAFfRc54Jbcie6UsydiI6r8U2h_WA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اعدام و غارت و سرکوب!</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5053" target="_blank">📅 15:17 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5052">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bqZjZuN8nQehXC2HuDGXczwXAtsCeiaRSRhmHIhawRbOtDyxnLZqQbDEhyfjd1hPjJfESySyLE-oaJnKbPLe5l6bZzATcxXgC9mbS9E-f6P1WwfNA1xuEeOADV3gBefe4REYb3qDX3zIbhYohEGykjRuIp66CnPYgybeMBSFwmz2jbq-Te_WOBDFbEAI5pPn1H5-PR4RkgGtUi8-x_09TZA2RDeqwCsgty4GGqOZmcvXSRZb5VFMvLFfEWRGqf2FryubgNaS7oh0FWjfM6i6NAPoOp3D7TR0HT52ehHJ3PzuRIAQKjH7Uqk8MvrGJjPajG0wzUTM9TL2F6fbI2XTXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سیاست‌های ترامپ اینها رو گیج کرده ،
آشنا که «معاون ویژه وزارت اطلاعات» بود و بعدها رئیس مرکز بررسی‌های استراتژیک در دولت روحانی شد نوشته که شاید «از عقب» وارد بشن!  :)</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5052" target="_blank">📅 12:55 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5051">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sbp1Xm66FCdz6wr--HjnIYjZZUmEFtKZX5SU1tPyyNj6BxGZB2UrCaTo_u1GsYMi5wLtFRiBiJteuGJRr5DjKfUn6t6B1Y390vQ3OWm5jAkIQDZW_ZLxv8MgPVxLOyvcMcPHG-RY_36vd8DEt-CsyNQ7Kq0i_V4dGY3QgtwenhEJstZG6yj1x5bqLJCQXq6c4p_6yKoHNpy843ZOcwJEUNtNhsthLdE8KmldifDpmJGXh3D6vfpxTZxLNaMhU0bq9OwaOH1Y2-dAaXFl_DVURu21LGGbCFRkOkWyJ67_i9x4abMST3FKRJdj_sptn0_zmeXuAQ5j6lltZhRAkSKKtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پاکستان که ۸ هزار نیرو و سامانه دفاعی موشکی و یک اسکادران جنگنده در عربستان برای دفاع از ارتش عربستان
در برابر «تهدیدها»! مستقر کرده گفته آماده است در صورت نیاز این تعداد را به ۸۰ هزار نیرو برساند!
تمام حقوق این نظامیان بر عهده عربستان خواهد بود. مقامات عربستانی در سال‌های اخیر هم بارها گفته بودند که «سلاح هسته‌ای پاکستان» در خدمت دفاع
از «حرمین شریفین» است!</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5051" target="_blank">📅 12:39 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5050">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ramOq0gS6cGUTPbmVnTSe7nMS0YUIeHHnHrWvf2oxhuobNtZPe0AjAt-o652UTQZlOQUdARO-5n3fuxX0G2FsDdGn-r0TULTZfPAzOKzmUs3olcotb7si9behu6XOJzzmmRaXZ2grVuFIs-jQXmG9QoN8jpC_u8W5L6iILR8TwIlqCbFjiQPqL98US1ZVGWD3viuSnbybhqjn8qW-mjmZx1hTHA0TY4iE-CNej9TDc39MSdSUptBVwiqexXWtdVPBICCVjTSwrVtoL8r67SxnwfssFRBEKHw02smEmOsljoT9BwUjdyBWV-aDauaARtVYhWyoQGnQPg87yFx21rvdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عالی بود این جمله :
رئیسی شاخص و مدل عینی
حاکمیت اسلامی است!
نهایت الگوی اینها فردی شبیه رئیسی است! که دیگه همه به چشم دیدیم
کی بود و چی بود و چه کرد!</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5050" target="_blank">📅 11:31 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5049">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p4W_Jr9TA4jtdbnFoP_nukOnuhdIfVH7yOeUyv072T61Drsk7HgY1jc9JETBXC5ey31YcJgPPbkm1Jtb1Je9bT_lNamaYjjCwMl2cPmdy3S03zshr1_mdo6pWpOmuRh4ox-It4pNsduOWBJ3ecHuDZz_sD2ucKvvNuDezKPxyPkxCaxW4BT001nZIHhEbOMY--g3BYj4RkBnG6y57MR1bO6dCKioqmrXpD1GzBNNqhcGKlYNRS-ZKHg_BVsRwCOS2DjYLvyViqDQKjrU6ipNk5YyJAYaorHSG6BCoHnplFSadeyOETbk2HI5EGGQcM4r2e0iHchSlUSV5VQV16qp_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تاثیر توییت ترامپ که میخواستم حمله کنم به خاطر کشورهای عربی حمله نکردم و…. بر بهای نفت در بازارهای جهانی.
کاهش حدود ۷ دلاری بهای نفت</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5049" target="_blank">📅 06:26 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5048">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b8eb45098.mp4?token=DReBWopd_WHHb0uQCAPJiAtX53k3q_6Wm4ZgM2VRJVKhHcZA356SvCHV73xGEJsdTnWnFVa-YlK-qg-UoY2JzV_UV72N4Msc_z4INLpGWLtqznilJWOvyfqCnUdzbjrgS3DKxQRAzs9peuHx87u4uqFh-_ldzwoVTklK2S4HZVtot_MzrZvWgAnMGmKr3UJr5Eb6xYgYcmcyX7vxdMtzZ1c8-hPXqAth9lWjhiMWX7cKR0jTNx9ldyFsU3PgIg7RDNqQNPdycTWWzWP2Zc6GH0QYu4PtGqBnOdqpbAwUjqb8HJ-kPGGM6UcyFi7BqM998kj7qzDWuhio3Jh6Rl_qbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b8eb45098.mp4?token=DReBWopd_WHHb0uQCAPJiAtX53k3q_6Wm4ZgM2VRJVKhHcZA356SvCHV73xGEJsdTnWnFVa-YlK-qg-UoY2JzV_UV72N4Msc_z4INLpGWLtqznilJWOvyfqCnUdzbjrgS3DKxQRAzs9peuHx87u4uqFh-_ldzwoVTklK2S4HZVtot_MzrZvWgAnMGmKr3UJr5Eb6xYgYcmcyX7vxdMtzZ1c8-hPXqAth9lWjhiMWX7cKR0jTNx9ldyFsU3PgIg7RDNqQNPdycTWWzWP2Zc6GH0QYu4PtGqBnOdqpbAwUjqb8HJ-kPGGM6UcyFi7BqM998kj7qzDWuhio3Jh6Rl_qbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فعال شدن پدافند در اصفهان</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5048" target="_blank">📅 00:06 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5047">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
رسانه‌های داخلی : فعال شدن پدافند در جزیره قشم و درگیری با «پهپادهای متخاصم.»</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5047" target="_blank">📅 00:03 · 29 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
