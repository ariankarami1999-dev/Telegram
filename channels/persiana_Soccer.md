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
<img src="https://cdn4.telesco.pe/file/h-gvLBS3_WEOir7T1VuDkCGEwFaLuWplxFamZpQnQkgUs3Y228_R8MX40yoMwgHyDhewFVjaHssF5gJKvYBuyLft2g0HGO3oqRB_s8QY1cR7d6V0XCWC7Qzj6mCSI8KnlK4L4k-bp_LdOgjThIQtyZl1nG9HtCLekHpTAt-BM3Ai3YpWw77XK3Of3jTOj-wF_gQ-0uVHzTUnfrtnyHc7NrCRw4tqaQRIXeQHOJVdskspMHehlho6OH5PgfwWltzwv3RLXqc7T6Fmb9T6-s_cxs16P_60lrYZOlZgi2md6SulGr_C3Dp1J05vzSs50l3WxSIJlKNlEodCUAT5lN6QsQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 179K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-10 02:20:11</div>
<hr>

<div class="tg-post" id="msg-22514">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aulmGRz6tDQ-5vyd2wUfdbsGu2GzdAmH2GrleuMJFABplvHyZmdnuDdLEdl8oFGjHBURyZyi_NsyYEOzQu69bfhiQU9TnHGo9zaoTZrwXUyWJ1iOlbT_1OH2V-Nc-nmJmf4JOmJbTKoX08eKfO034ucf6VS3kN0I43wv4wCa6odyfvpUzsj23K0jx7rXzfPRz5YwTvGA_ph1lGmEMAVzEoEMGMx3Lv11I3QUDl3chCECzNc07V05qsw_dKIaX6yCwGvXDmqeeLdgCc3Qn9ESxrF0-x2nVoPitSVFyQnqXac_af3oTnhU-p6YgSjHmwlAKLUT1lwrHHZW5oOOJKdjKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
👤
مدیربرنامه‌‌های دراگان اسکوچیچ سرمربی سابق‌تراکتور: به‌باشگاه‌تراکتور قول دادیم که امسال اسکوچیچ راهی تیمی از ایران نشود اما اسکوچیچ از ابتدای فصل آینده با یکی از سه باشگاه سپاهان، پرسپولیس یا استقلال قرارداد امضا خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/persiana_Soccer/22514" target="_blank">📅 00:58 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22512">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r3mErtgvfzMSL0PqA49tmjNhD72oHRuMLV1hg08yJ2LZGlbDNL-JCtWCFgjCHRs9a2ZjKz04utYkH0r-f2rmZAVLnNbXC2dsBcFim58mevpAHWGSi1HEDobrcqoH2ZOFC3UmGIgogoKj1PF8vrh85MCRxVH4nPpLI5vUDHBqbE6RUfOtarBlQc4z8vNLOdiN3QrB1ixFP2fR5C8BdnAgRJsYiJpTwZw7qlZ0MiIuCBkajbsoG9_NCDMxSnHrQBd_CHNkGABh98jT8EFyFfUIU0KNCcVFk26AdoGYE7g2alTnHdYEWVzO3g9Fxbyu4-tOCWeRZG7ydzEgnXdk9JlSxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌بازی‌های‌مهم‌‌امروز؛
آغاز مسابقات دوستانه ملی پیش از آغاز رقابت های جام جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/persiana_Soccer/22512" target="_blank">📅 00:53 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22511">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qJm-cTZYycEcTIbfp90RapBSPaFRbD9NGu_ZIanE7yUKgsMRFzgIZfdMBoah4o5xNOtsstOAi-qkK-F8tY3HiYgp1vEqTKg9ru1lov6-_bZEQ0Q7c-E9vkwfd19aXqShBY9VF12ytR__fVHm9FbzMho4aT_5jakeP-H9lh-3PSp2UMXbOlLMqiPdcwOB_2vU5PSfQDw-2wPTcHY8s331qAByZKBX9qyQoz1BgEL2nagwyzaYORzhXstaJAFzoUstPOs8UcY3tB4H9GdCb32w5AQGXN1d4JYjUjVG1hmDVevVvJdqtklr7RC5TJpRhtPnzgpEVjqqa7PLFDRy-UZxwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتیجه‌تنهادیدارمهم‌دیروز؛
دومین قهرمانی پیاپی شاگردان انریکه در UCL با شکست توپچی‌های لندن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/persiana_Soccer/22511" target="_blank">📅 00:53 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22510">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/opNzkJm_reRBq03VhD4Z_sftbTtdCdetrSNz7jGhIrW62xi0DlqYDiKO0kqcvZ-hIm5crqzvq5K6VB6M_ytKnLVjOzbP410dV3IpBKj7TzF3NcZEeeyZFZ72aWihq3Yc8tMDV95NQ6-ID-0g9_sre2PLZGoUOt91cMiaKG5ZdVZLqceOXLqdCWnG3tFzkAWFqq3W6bP7JJo50iLboG9K5Wdj_Hv8dJd5HodgaWYuqCHWDzgzKD98uTjfYwNg3wuTKIEtwdKuRDScf99KA2MHeThDSvuGSdZmZwhdafJYu8RbbJ11iqrIqivYw27p5boiZjdly3Ikdyc3e-0Wp4p_rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
تنها جایی که در لحظه عضویت بهت 500 هزارتومان موجودی میده اینجاس
کافیه‌فقط‌عضو‌بشی‌تا
#وینرو
بهت
🤩
🤩
🤩
هزارتومان جایزه بده ، نیازی هم به واریز نیست. پشتیبانی 24 ساعته
🍆
تنها سایت مورد اعتماد ما با بونوس های کاملا واقعی و رویایی:
🌐
Winro.io
🌐
Winro.io
کانال بونوس های رایگان
a9
📱
@winro_io</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/persiana_Soccer/22510" target="_blank">📅 00:53 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22509">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tt1bSjJ8RUaie_NuoeqVKUEQmll713ITtsljaSMaLBpu7QgpDv5DZgnNVLT8SFC3DcxQpD9kGuwd7pjoWNDFLIaZP4ISUQfr5jKAmOHyKlStud7RkFSjy7PpQG8RYz5mnUwED8a9ifB-PTC2uxtwpQS0BRizjjT19TkOnrHlno7HbGy6-_TSwYFZZes_rbTxdM6RBMEt8ak5Aue2yrwIUNNubtvN5nrNg2IsKOuwaIQwy58ev1Bv37gFerHumK5tmrOjG8MmNb14sH5zrj4WzvNjMhXxewE9XzLSvekvH274PwY60GhG0uAtPeFow6vtp9D87pFyvSDD8Eo9Yi7mtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آمار تقابل‌های دوران سرمربیگری هانسی فلیک‌ و ژوزه مورینیو سرمربیان فصل‌آینده بارسلونا
🆚
رئال
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/persiana_Soccer/22509" target="_blank">📅 00:21 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22508">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NXCd4xbvjB2xJGzXjwnBLaBn__r1B2fL1ZMYJ-lsB-kN7dZNcJxMGEvF2KeYEDA7i90zPpM9g4Vrg4Tmu4RFa6JPgQztNknBb6SaopPqSKJ1kgJ7sAJ81LKmEomimcpvF1UEwaqD5DNOy1l84_R1TPcCvrNwBI__pM2fs2B20N1mI_4Rn0PaIe1nJsG-YevLy-thNwrMulTQNXig7f11SLepIfKxjZCOeMOUr6b5VBtc9fdtz7QEFP96yXDqHsWZH3L9DWRzKD7c9wOmvlbOqCgJPkqZ_dOX3zvDBhqGORBGKKS41WoYgDU6XjszmBwHJ2n6gn2bdkJ36TI3Ny1pMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باشگاه پرسپولیس به دلیل سفر افشین پیروانی به آمریکا باسرپرست چندین ساله خود قطع همکاری کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/persiana_Soccer/22508" target="_blank">📅 00:10 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22507">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QmRF4nlbfora49GtzCSlaOfxNVI1aJz4_SSVNWWrK5yR5ZKfC8N2JMJHTYkdDv6DyuoQpkP4cxl51pzS_Un46-dqCxC5ooh-2h2vRvDtmeWe1ENtgMAh2XVKiJjpZvILaCKIQihvv8KtwkigzoGaDCIyLlE16VlLZEw2khLJq79m9G1MPvn94OOKTxYHX7NM1bZve3DKTL31rUYBTpQi-NhcYEdf1PUcwFxUsVP2_J0h67Fzw8L7Y02xDXfmz_XYNAYfP-G-cTdcbMmsTXSja6NxTLDhzWitBV-jgGzQ6dKhnzusF9xV-Fa6mYV_AyanOsVp2eKs5rKWyIGOXq3Jug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
تمامی قهرمانان ادوار مختلف رقابت های لیگ قهرمانان اروپا؛ رئالی‌ها همچنان‌بااختلاف در صدر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/persiana_Soccer/22507" target="_blank">📅 23:43 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22506">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kMhH7AKb4YvsTp-gDxFVmjm6d2-7qW934cz032BpOu45fepeQur4bysZF7NwqK5lkvhofHyMenbgMkDdSWI2KyJ1PU7JrDiKcMYsE4B3zlXJqn1DKArQ6Xm-09GLMhhbZtbnTxbxg6E-DMiL-3-8l8Th9XgrSs4UEtogbhcBxESgsA2eMLTXIgEUbDaahj7LpHu94aZ_kjrKKcQYvbUYpBqj175tqX1Dd0bZ9xI5Vc5Brj0l2caM69gU7G6E3TkKybOur9YqwsW68887Je3TY7pVmvtAltYsbWiExbupF_gSZ7fjDnk-Scn-Fy88RPgHjTyUOq-IeN054pV-3vOtdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
ویدیوکامل‌ضربات‌پنالتی دیدار حساس امشب دو تیم آرسنال
🆚
پاری‌سن ژرمن در فینال چمپیونزلیگ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/persiana_Soccer/22506" target="_blank">📅 23:26 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22505">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78d5a3b7a3.mp4?token=ZHdDdsFPzFIJ6uL-Udg5ZdzMwzjcgl-cK2VAgn8ez61gjWAXi3br3eguMHUvA5nuLfTmWt8GJSL5i9Ha-NhOtLTu4LAmxlMPUpSHMPkLGBal1OVw_u563CinAecVRa3S807nnSDncNzgeu9JJAirKMGVrldwKGL2o2pcjToVujxubUXPe6x4x4KAV_GudcsJeq2TBfjRvehTpRlOriN7aeIYCDlikwDQL9PWLLKPJ9AFjQob0MXfJ7a-74aRtOEKvrJ-FjIsta00Ws0aaX4wdvpLky0mbFmUHWTYmGzhXbnhpe666In9LxGui_RbstBsLZcJAcaIJf-knjmLwE1L4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78d5a3b7a3.mp4?token=ZHdDdsFPzFIJ6uL-Udg5ZdzMwzjcgl-cK2VAgn8ez61gjWAXi3br3eguMHUvA5nuLfTmWt8GJSL5i9Ha-NhOtLTu4LAmxlMPUpSHMPkLGBal1OVw_u563CinAecVRa3S807nnSDncNzgeu9JJAirKMGVrldwKGL2o2pcjToVujxubUXPe6x4x4KAV_GudcsJeq2TBfjRvehTpRlOriN7aeIYCDlikwDQL9PWLLKPJ9AFjQob0MXfJ7a-74aRtOEKvrJ-FjIsta00Ws0aaX4wdvpLky0mbFmUHWTYmGzhXbnhpe666In9LxGui_RbstBsLZcJAcaIJf-knjmLwE1L4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
اینم‌نسخه‌اصلی صحبت‌های امشب عادل فردوسی پور برای دوستانی که قصد استوری کردنش رو دارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/persiana_Soccer/22505" target="_blank">📅 23:18 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22504">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/52a1e84d8c.mp4?token=LjYv_qBsHOOxvQ5sO5sDy6mYolhMKxC_Wv1YtfznR3ZpfKts-GXpuU2EXunuIA-_IkPxgQltou4_8r8BlPWUwcYMUZHF8KkNKccEdv6RA6WLF1xtJsw7_kPgOCLp13fjdAkepjYaDXUSSMy546yZvegX1McB1EScYsqd13SVVqspzCgqQgSLhqFadHJTSMe-3qIYqDAEOg6qSTypM5uUhWsFBlUT3rudqV327wHx1u386nXrR0Fb-ZQlGONcB2ywhAKuo-D__kZ_ZFExbjbApW1H9O-_ZH3zRpJADm_vmaD_e2-DhZlJYCfCpUTQNfo5t1vB4kI6WqueYPuobOtaug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/52a1e84d8c.mp4?token=LjYv_qBsHOOxvQ5sO5sDy6mYolhMKxC_Wv1YtfznR3ZpfKts-GXpuU2EXunuIA-_IkPxgQltou4_8r8BlPWUwcYMUZHF8KkNKccEdv6RA6WLF1xtJsw7_kPgOCLp13fjdAkepjYaDXUSSMy546yZvegX1McB1EScYsqd13SVVqspzCgqQgSLhqFadHJTSMe-3qIYqDAEOg6qSTypM5uUhWsFBlUT3rudqV327wHx1u386nXrR0Fb-ZQlGONcB2ywhAKuo-D__kZ_ZFExbjbApW1H9O-_ZH3zRpJADm_vmaD_e2-DhZlJYCfCpUTQNfo5t1vB4kI6WqueYPuobOtaug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
👤
صحبت‌‌های فوق العاده ارزشمند و گران‌ بهای عادل خان فردوسی‌پور درشروع‌مسابقه امشب فینال چمپیونزلیگ و تسلیت به خانواده‌های داغدار دی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/persiana_Soccer/22504" target="_blank">📅 23:12 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22503">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QVqUl8-pm1K0ZmfQEVRFM9HTiAwRj-K1kiUMIZWF7Prw7ketzkEJXWdXvXN-k-rnEwFnPZxdSqVSNpmoNZ9xGxm6GhTEtcaCsdR-2H670xMoX5QzLn7C9Xt50zBMGpKQ9CToCF-2ugmvNsSLN9k1XcEMKpSw-j753ue8456GBpKkJWplT2O1hE7gr14xHst8WjYR_IZnA9O56WsSRuu_OXfVP34pVer3SPnhvNPp1Q0PkL6wPk48FKZ7IyOxasXH_5OA0DMNRulT3yFsOEgdq4YmlyVZZc610BfFOhMtPoYY-illU_AkF8OiqDLKhR9QpENuRdP7Mw4f_KzPWQ0Xsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
لحظه حک شدن نام باشگاه پاری‌ سن‌ ژرمن روی جام قهرمانی فصل 26-2025 لیگ قهرمانان اروپا؛ این دومین قهرمانی UCL در تاریخ PSG بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/persiana_Soccer/22503" target="_blank">📅 22:55 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22502">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d915ebc4d.mp4?token=O_h3BIez4CzGzhX_XdSdBU_Bu7ET9hJ4AfwIhn6KKAPuJTcKwi2mDtGkA_evsf0AGA7Z2yF9cLCN1f8jZSVoZA3ywIy6OwIoCrBRK6h5AyZ20dgWbkKtU1PE85cqtpmyDqyUcWXhXOrke-7vQjKK9iJH54x1oZakaOSNNf6UjNjhnVW7y-lUmFqDMVJh-FiRj7pzl_VNEPqknwRgRHwMX4GDSJe6S5bROOWaaDH1PCegHmUnxZ76OfcQzH4qGceAObMXwCtE0I5up5O_QPrZmtNA4y-fDE4rUSfP8cyRDhSVrX5BlpORX4gLhQce0Ynzc-ksrA6Gf9ABR8dujBG7JWue82sMGdFxVniEmcy3wId7tiGbSDWVhikpQ3V6nET68lUpT9xFTvYBKxPmVhD3ncYdHH_a3tGtz4qtu1xxyYAmyJydXmKLgX_Nx1KbO3GEmCb4PRa-6fxnalAkQmN11GGs-aTjOQ6qcdELKArfXGNroig_4zv22pYriyPJhUyXm7-l8toIIxaKJg9DQZGeQ6bhbBuQA252rEWj_UCiNigmri1jeq2VFl5tpKLv42Jy_3Z7pjaSJ6Oxmg3NK7cE3aBbGvLPyraTSddfCDMgMXajgRaD7D45yCAl5QjnwVTFkkWz8C84peW5GFznyI2WGkEAlcfi1HZqIlbiWKY8Yvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d915ebc4d.mp4?token=O_h3BIez4CzGzhX_XdSdBU_Bu7ET9hJ4AfwIhn6KKAPuJTcKwi2mDtGkA_evsf0AGA7Z2yF9cLCN1f8jZSVoZA3ywIy6OwIoCrBRK6h5AyZ20dgWbkKtU1PE85cqtpmyDqyUcWXhXOrke-7vQjKK9iJH54x1oZakaOSNNf6UjNjhnVW7y-lUmFqDMVJh-FiRj7pzl_VNEPqknwRgRHwMX4GDSJe6S5bROOWaaDH1PCegHmUnxZ76OfcQzH4qGceAObMXwCtE0I5up5O_QPrZmtNA4y-fDE4rUSfP8cyRDhSVrX5BlpORX4gLhQce0Ynzc-ksrA6Gf9ABR8dujBG7JWue82sMGdFxVniEmcy3wId7tiGbSDWVhikpQ3V6nET68lUpT9xFTvYBKxPmVhD3ncYdHH_a3tGtz4qtu1xxyYAmyJydXmKLgX_Nx1KbO3GEmCb4PRa-6fxnalAkQmN11GGs-aTjOQ6qcdELKArfXGNroig_4zv22pYriyPJhUyXm7-l8toIIxaKJg9DQZGeQ6bhbBuQA252rEWj_UCiNigmri1jeq2VFl5tpKLv42Jy_3Z7pjaSJ6Oxmg3NK7cE3aBbGvLPyraTSddfCDMgMXajgRaD7D45yCAl5QjnwVTFkkWz8C84peW5GFznyI2WGkEAlcfi1HZqIlbiWKY8Yvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
ویدیوکامل‌ضربات‌پنالتی دیدار حساس امشب دو تیم آرسنال
🆚
پاری‌سن ژرمن در فینال چمپیونزلیگ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/persiana_Soccer/22502" target="_blank">📅 22:43 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22501">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50097d1448.mp4?token=lGNM6E1X3NJLmwAOAcyC6TU-uuDcfX7FvX6UZjwJEd0VzqDsr3N56aBzkuruZZg7yND7L-ZEkTaYtlCFYC8riLXPXbLJfMKj-mKcnTIV6HFeOLZk_W_9RYi5645tM3ZMN6iPZj-FDXMjMAUapvvXJkHQVZD76PfH-MK305rjSCVnC9gFSIA3zqzsj528RMjw7JF1F3AKITTkxTspQByq3wpTxMAU6RkE7cyLwb8vJLHgjuOjly_4mxX5w8EyLcGWZj7Kb_tstH0NmQ1V9vJ65IJiGiw2f5O4xNFvOreiwzSyZTiaMyinzzrSZhc0AKlt7-Fnd_FOHee_aYXIWYrtgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50097d1448.mp4?token=lGNM6E1X3NJLmwAOAcyC6TU-uuDcfX7FvX6UZjwJEd0VzqDsr3N56aBzkuruZZg7yND7L-ZEkTaYtlCFYC8riLXPXbLJfMKj-mKcnTIV6HFeOLZk_W_9RYi5645tM3ZMN6iPZj-FDXMjMAUapvvXJkHQVZD76PfH-MK305rjSCVnC9gFSIA3zqzsj528RMjw7JF1F3AKITTkxTspQByq3wpTxMAU6RkE7cyLwb8vJLHgjuOjly_4mxX5w8EyLcGWZj7Kb_tstH0NmQ1V9vJ65IJiGiw2f5O4xNFvOreiwzSyZTiaMyinzzrSZhc0AKlt7-Fnd_FOHee_aYXIWYrtgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
لحظه حک شدن نام باشگاه پاری‌ سن‌ ژرمن روی جام قهرمانی فصل 26-2025 لیگ قهرمانان اروپا؛ این دومین قهرمانی UCL در تاریخ PSG بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/persiana_Soccer/22501" target="_blank">📅 22:41 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22500">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WhQeOU9pq0yJXgU9_FJeqx-2ZvbjHb9xeKLSpOHdoPg7n9ymgL0pPbNvfE3CLootEWJ7bXGR6VtGzgKXKNKaGmvWEzSChQZj4Qz6c4smrufkULGHBTkZlobRUvtx81Q3DzxTXXyhzf7ImGRxGTHfCBYP6mu9-IxKk6G7m0x71VxiaCru3fUNi6vOiRe3hd-CfqtuR3TJZFmKqepY_iPtKdQs44HglIBVyaykDF5kGSrFqaETNV6x-tch3OI7WPIwv6Jn51QNnhXDyhL_zO6qJIrT6q7J4wPVdeuYE1VHyG2JBc4dmhdN-CVQjVm_CcZ4ocpgwu0llFyyYM8N6vIoWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
دیدار فینال‌لیگ‌قهرمانان‌اروپا مابین تیم‌های پاری‌ سن‌ ژرمن و آرسنال پس از تساوی یک-یک در اوقات قانونی و اضافه، به ضربات پنالتی کشیده شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/persiana_Soccer/22500" target="_blank">📅 22:36 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22498">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c46R93KJ1KuIHx0rHROguWv4Nm5TVO2od1hT5Sc-L8I-DydwTNUrUSsz2AGlvTkgdTx2Bj4KIgGu8w1M-lt8XqBliwmUoTavfOP9jJLe2NHzNKcFLoXLEuxO49pHnp9pdBDcQDI_lHyZm7uLTW_frUtfUbTGw3gJiWUv6301f5pY-yx1ED5wqdwhKY_w10hqd8OJnbdVg5C3jQuzb3a52lW6OIf-AXWN9WLF0ZoHw0tJtEHWXwxZ5_FtEw8IPzEcanQdyNu01f098lbl1uOOOY8Xbrb60aKKW2jSqdHrLS54DM8x77wJeNI_1phCpzvW_-no0AhmK2QV-6eikojppQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بازی مهیج و دیدنی امشب دوتیم ارسنال
🆚
پاری سن ژرمن بوقت‌های اضافی کشیده شد. آمارو ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/persiana_Soccer/22498" target="_blank">📅 22:17 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22497">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AQoc_B05wBBog7n0gGTnh-dqjjlLt0ui5t81ffvL9g8FigQRbun2kKF5aikS1GDeWFncpMSTaFrhtlkUkTQjgr-0VwET45dsQg5D2FJB63F4JQf2b5aLmZRMEl3NmelMmgFQ77sGgFXAmhYRuZbeDSWqfh698YxtBRgZnRjvjHJ74NUDSgVu1sQcpuBasE0SueUIEnKA6wVuc-GZfK0xmqOmLDb0O_HktHa-ez_XX2WFFnPpI66OonypydMWxefwyFvI89CYAiec9pgzW_DkKYUcfQyuz_ZWzut6xBL9liLwFKwg06jvGCfasbqryloGFvym4me3e9xE5Qd5dsUFuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#نقل‌وانتقالات|سران باشگاه منچستریونایتد به درخواست مایکل کریک سرمربی جوان خود با ارائه پیشنهادی 100 میلیون یورویی بدنبال جذب فرمین لوپز ستاره اسپانیایی باشگاه بارسلوناست.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/persiana_Soccer/22497" target="_blank">📅 22:10 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22496">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jw2GjmN0gou1ASIvJInDjHrB5Kl4h1rXlbcK0poW35msQQA0EpJw9rBXcf8lpCMChYByPQ7aYN70cKTICeo_zc8jW-4AkqWmOP6xSRQomJqseycKDtuKubMqNx1kgSe3XF1YQGwn9GATv5aLw4xIuFL0dnJejylZIB0yCw-eJWk_vh3XgcZraXve-7g2QQYwc_zbfsIwQ9B5EJOQutc0bDdJo5bXB-HoQqDKZfkUexkyCJ5SYUptdBNsvwi6LzlChtif8XdicVg7ky_4J3K_cCxEk1gQEyR9MX4Z3HTGKeKSN6pABjqBuUi19KQvd94VRJRMVydbU2ZsQzr75bSAkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دقیقا 19 روزپیش؛ صبح 21 اردیبهشت؛ مهدی تاج با تاجرنیا رئیس‌هیات‌مدیره‌استقلال تماس گرفت و به او گفته بود که فدراسیون به این نتیجه رسیده که امکان برگزاری لیگ وجود نداره و بزودی استقلال رو بعنوان قهرمان لیگ معرفی میکنیم اما تماس‌های اخیر حدادی مدیرعامل باشگاه…</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/persiana_Soccer/22496" target="_blank">📅 21:49 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22495">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O96aoxv3S9af4fkRxQ0boK1gm1pA-t9gCTL18oiVnB22MbMYvPaYW8ZpuLge80kvsmNfWo1NG5D6fA2xWkSGKrtDEsrfvtNo_fzCbZrCopjRKZUMF4P5PivPEbv8RSDqtEUzZifjLsCD7T7k8zUi6KgZRTuIq20wp4mU0kP46dE2fef4WPF67pbW0P8Sibo9vElgrywAJTC_fRqiqUJz2j6ew5NtqBPWpuyslmuUgxXL5P0-s5PRkJvUCS0B_ameA011_UwBKcDFnP0k5XVkROEReD8hf3hBmjPabkyG-mVq3okO4jJTd30_dA7xumsGIEPIJGt0XaiXaPmvfu-TqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
تنها 45 دقیقه تا قهرمانی تاریخی آرسنال میکل آرتتا درلیگ‌قهرمانان‌اروپا و کسب دومین جام ارزش مند و شیرین فصل؛ جای عارف خیلی خالیه.
💔
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/persiana_Soccer/22495" target="_blank">📅 21:35 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22494">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AnDIProYWn4nFNFP_jByLxOfSyNQLVwbDgsGwmMJEW9m8TDrOKuO7Pc2_Sw7pkPnRIyJ1v3T-jyFBVpoI_cTSVVSCW2VquxkqbDRvP5vDc6mW1gc53voos0fWafpEZnx5y17CIYJSUin9yHO97VpxywCJo7ib3cVISxHVMtpGBWKEXSW1AlWaur2hrMqGC3he4XJr469MbXu5XUM4o9FwkBBZvlE-mVaIu9t-dTUVX07GAehOPMBIWXuUrGGEsJUFhNH0kzl-So-ek0gvOeOGisLPNlrz9pXVUvgPhuz2tNRqlA1L7Cx-t2ye6FKxZUZ5fMUz84n2aTYY9MUIG6hMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ باشگاه پرسپولیس پیشنهاد مالی بسیار بالایی رو بمدت‌سه‌فصل به آریا یوسفی داده و احتمال قبول‌کردن‌این‌آفر فوق العاده از سوی این بازیکن ملی‌پوش‌بسیارزیاد است. سالانه 80 میلیارد تومان پایه دستمزد + 20 میلیارد تومان آپشن.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/persiana_Soccer/22494" target="_blank">📅 20:51 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22493">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nnis9gXjq62ixFYn9xPoEDr7BqcF63LWynyzSjbXjRYZEEYchJW_HNGP9EouqR3MRLGsH9wRcUXCIxE9j6mkaLyHghHu1hJx-1CWAMDgeQzWYtIgOZg1kW_K2FHhq98BKV7X-U0KSCt_2-0f0xcHfkwRSpKAhlFCebsfZRGGOFOLrVvX_aqrgiWLFXl-hpE4ryGrXWtSrBu4un_-ua9POpqA4CQoIhEwCucYl12E1ul6MgGg8XzFoRRTm0w-TckcE17G4qw-kmRb6Cmhk88X7nVkKxq9xMGU0ZOZfu_uF6frCINtFREJ8NGR4uULfcUpKbUrxidawFJcFgIsxvZkyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
علاوه بر دریک؛ این‌مدل‌انگلیسی طرفدار آرسنال اعلام کرد روی قهرمانی‌این‌تیم درلیگ قهرمانان اروپا دربازی امشب با PSG پنج میلیون دلار شرط بسته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/persiana_Soccer/22493" target="_blank">📅 20:29 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22492">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a443979ea7.mp4?token=ayWr8ai4KHiZ50f8ETEZeiGYNYmRQfGTM78pK3bJO84lUL-HSIwqsQtRaYyfehR_KL5aaxkPkBcC5nZVkL3M8q-0DH4SFGoPrqUG2Ae5n-OMmUfafox-Q5QToGk0zQoHfcgAmtfZed_BoJltXNzXEKEPLc9Nhyp5qHQIJTvPtIhjVTW0bZDrVtN3chfpZ52_EUjlPAaWXQFjulodsY9n0_zIeA3jm0zCXLSXZF1ZgX_vu2lREqCRMxkxFCYCxAhivXjXFmYWEr5hme4fsQ_UkqO1cb1mrCf3L_jYUrEhbffbSwYCIWwZdUXAIOjr4zR6oK--sn-oso8NB8dKJPYnBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a443979ea7.mp4?token=ayWr8ai4KHiZ50f8ETEZeiGYNYmRQfGTM78pK3bJO84lUL-HSIwqsQtRaYyfehR_KL5aaxkPkBcC5nZVkL3M8q-0DH4SFGoPrqUG2Ae5n-OMmUfafox-Q5QToGk0zQoHfcgAmtfZed_BoJltXNzXEKEPLc9Nhyp5qHQIJTvPtIhjVTW0bZDrVtN3chfpZ52_EUjlPAaWXQFjulodsY9n0_zIeA3jm0zCXLSXZF1ZgX_vu2lREqCRMxkxFCYCxAhivXjXFmYWEr5hme4fsQ_UkqO1cb1mrCf3L_jYUrEhbffbSwYCIWwZdUXAIOjr4zR6oK--sn-oso8NB8dKJPYnBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
دریک رپر معروف کانادایی یک میلیون دلار روی قهرمانی آرسنال تو چمپیونزلیگ شرط‌بندی کرده.
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/persiana_Soccer/22492" target="_blank">📅 19:51 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22491">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SHt6_Yt6meqrOf4-vGuq-zqiL32jUMI9hhom030SnZOJPEBnjRlGnzkXE5_pzlC6Ijv1F1_fwpo9e6VTjOdMKtRr-pU-AbEqKfr6x6rES4Rms7xWXbt3azwgQgzAMypi9LaRwDFjYKfthox0fxGso7LQkoi0DRNVPnHX4aRZiQ-srVk7YVjzQ45egIJFr5Js8kmUG2shNDmV4vbltGp9D9okffBU2EiHN6gksSo6eqEsiuJHAlufh_YX-9MhLXL6kUHDEKNEuy7K0gjhhdl0PuXcqZpusXgng7Br_0QJPVbwdMjfFkaGdklv1PaY9VMwESLTT6o8M8QX3c9_vAUmLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
همانطور در روزهای گذشته نیز خبر دادیم؛ آریا یوسفی و محمدامین حزباوی دوستاره جوان تیم سپاهان مدنظر اوسمار ویرا برزیلی قرار گرفته است. آریا یوسفی علاوه بر باشگاه پرسپولیس از یک باشگاه اماراتی اماراتی نیز آفر رسمی دریافت کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/persiana_Soccer/22491" target="_blank">📅 19:42 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22490">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PyGrXfNkUvyEg_rMLXIvMo7Ss4F7lshzepUYiz7WevBr3lQpxAl5hnQ-_3LS0gwKQ0BXD3q2vsasXyD7GL4JCjn1j4o6pKJoUohs4zP599VfYqvFyhMYOwS4JordIa0NuePIqRDC4NqmwiHXY489UE0Hpfm2fIm_FpYMJMH2Nvr9G4rAO-tCFvfqbwmCZyAHA79A45CCWuHXovlXs9wvejOT154Es2A2lGRj0f0wm2ao1QhIVUoSpma7P5vdwghGuo0SM2N10xaaz82_QS9-8iTnaXESjGGG14tdpLx_q5GzENEp1zdyeH-03LK-6WzUD38q60tko9HezqTh6s67SA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
روزبه چشمی هافبک ملی پوش استقلال نیز در تمرین روزگذشته‌شاگردان‌قلعه‌نویی دچار مصدومیت شدید شده و ممکن‌است به دلیل پارگی رباط صلیبی رقابت های جام جهانی 2026 رو از دست بدهد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/persiana_Soccer/22490" target="_blank">📅 19:42 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22489">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZPpvilauJpHtqvc2IQrKj6sWBzdgk_XwaMGRHArbLTGiw6MOCckdP-1LzDfL-oHXDDvxa1vJnXqbB_bw4YaojWVB1Ci6DBgl6Q74qfDFU0avqavIX19MPFOBxWJpTHl0hFJ6HMXF6XWCJ0Ahf8v6HjJee8ZqfRJqp1dVEPSe0nLKJ3dfm6ZlEB6U9BSMWihv89VyC5O87WyQVPGWsDaFYPRkZJIBBtcBsKem7UhQ9LfgYU1SrB7NMRljGb4LHytU9SSea11f2GI8NOilMpkXxd8cHxA8KtUgUieFvOiqh0Qt8XmkdhOBstszcYUtqnaJu8uKimJbHQeoBL0QAXOQZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
بدون واریز شرط ببند و بازی کن چون وینرو با ثبت نام و بدون نیاز بواریز
۵۰۰هزارتومان بهت میده.
🎉
500 هزارتومن رایگان فقط با ثبت نام بدون هیچگونه واریزی!
💳
پرداخت مستقیم و سریع بدون واسطه، بدون دردسر، واریز و برداشت در سریع‌ترین زمان ممکن
⌛
پشتیبانی 24 ساعته
🌐
Winro.io
🌐
Winro.io
کانال بونوس های رایگان
g9
📱
@winro_io</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/persiana_Soccer/22489" target="_blank">📅 19:42 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22488">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sAj_yVlkhat0AjL7u5ERNx_UPtEjxf3tOx2CP7QRIikMVu0-wQTw8k57RrrsfWocYpvYmNVlNAXvuXb8Z922fdxKrePS7uutTQYqBSdnrIqy1nJ33ilmxuSBNm2S5s4IBwSHkS7rlF-iqijGmrfGBLU4Tn6PPIgxa7nR5CPZQYDJczz-JfHQETKT_t5zQHLT1uFUp_NZNV2jsXnI_SySu4CRz0RzTUgaLxK7o8FTuLcZSybWmu9gRrwrS0e6gftmosXGc5eu2eGVYxHZXijoO8H16C4f_G-uFFiX-iM6NPrAoL9bpZleX2HZsrf9_Z18YWKAmZJ-I4z0pKNKGkHIsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
همانطور در روزهای گذشته نیز خبر دادیم؛ آریا یوسفی و محمدامین حزباوی دوستاره جوان تیم سپاهان مدنظر اوسمار ویرا برزیلی قرار گرفته است. آریا یوسفی علاوه بر باشگاه پرسپولیس از یک باشگاه اماراتی اماراتی نیز آفر رسمی دریافت کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/persiana_Soccer/22488" target="_blank">📅 18:50 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22486">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jh_G3P5tCxtTnnAxbgbAoLI_yNTu65ryFvhy6-64rUaKpHZFYRdYkHWM3HOxZHmF5BbhRSBrjSa-td7IsCKZJc-DzzKVIgWY_uB4Q_AVEwitfRXhBZ8wlgrGwerd8vhvx5YtxIXk8kHJ5UWMDYYjPqlWtqoek2hxaWWxnmD7Bt0m1HP2h9EYugHeJyNVqDwvgOP1r_2KaV-f-uwHbg3d9qsHv3HKWhh9h6LZuiHlfnnfvyhNZ5X9nlG-CFveNqz7abc8gqR5FXK6vONl3UwuAV5ykkn68OKFkGFetiHNBIhlZ3lFf6Wrl06JuI_jvxvh_1znQGxVuyqd2HGFla5ELA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SoxC0d5ktucUyN7nU89A5vK18vYkgZbORvhSEodWxhV5ZZlLV5nbf-wJoQTZUmpZdpUHLrUQcoBBTo81ex6cOiW-DWfq2mnp5_NEszaSGXN9Y2MIfkcq_t8jjng54CmgkJ6NLdCFgW8-wwXDB8Rubi4KigSHDvGir6awZBLAOF8VcMULkiTqb7Pt0ED_okdbgiLG-_fEDL20_yZTF3xgHhM-ZwDB3s34xztwOGcmOJ57WxvSd0Y1vAsdqKbFR8CziZN4-eKrDzD_jtBPZBJgh0oO3x3gcVUOnflrQ3G6GC2AHs5ZHGxddeDfworC-aea_T2r-OREI6Abgb1TJVUBiw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
شماتیک‌‌ترکیب‌دوتیم‌پاریسن‌ژرمن و آرسنال؛ ساعت ۱۹:۳۰ با گزارش عادل‌فردوسی‌پور ببینید‌.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/persiana_Soccer/22486" target="_blank">📅 18:18 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22485">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s2yeXLg_kT6Qm6vHyKW6xu5PxpkMJFqrOfqIsFC1yMJcVCXffRlffOxhVQETzFE2bS3q2sJ0VYRs-bNINOTLe_MNumYK9hoBPT50G03f4ID9R4lE1YfrJRsQsxRtVyH0JpsF9NZSX6mZrORmU1SMJOxB2W2wmK0qx-q1UULFd_Zr5Mm0dR6l0_t5swx5cWWQAepPNdQcC4RTDFoGhceO9n2-iQjW5r8IZUy6PYZc0x2gK66O5orNk6QzOPYQPtpFQDYcxiExMkUo_cZNazYYYsxvdmdY_ddUEjyEshuP7VvVJGCdt3tDvW7w4PNt5bioWuNcrMxOvn0MwFLyoYfF9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🏴󠁧󠁢󠁥󠁮󠁧󠁿
عملکردفوق‌العاده‌داوید رایا ستاره آرسنال در این‌فصل لیگ‌قهرمانان‌اروپا؛ رایا درصورت کلین‌شیت در بازی امشب، رکورددار در تاریخ اروپا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/persiana_Soccer/22485" target="_blank">📅 17:52 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22483">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d6GgJGt--H982H2SB2Xpjh-Z3zwBpa5oM9NHYLhZSmupwDPuix5lMPG814AN9d09BAYO82KWzABYCt3R3r1bMG3ay4cRkTYAUgchQGBHNhjbsVy6oBSvJPo3ybURtU-o86v3fmci64mANXSkZOXGSMnC0mYa9dWZYJvPSsF6fV832GMpyQ5cY-QYKYG3BfpRajoY9y8g4NEEQySfUtAM3UH3J0jmiCv70xKRPgN5tg_umvT3I29xfI46vgO2W326SDuJ9qEAkjhps1Em1M-h49SAu9to0LLfgyUyyfXRe_DnbWHJ76IdP7Z0wMPsybPvETi6nboePbj21PNieOb4Ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#فوری؛طبق‌جدیدترین اخبار پرشیانا؛ مهدی تاج رئیس فدراسییون فوتبال امروز صبح در تماس با علی تاجرنیا رئیس هیات‌مدیره باشگاه استقلال اعلام کرده بزودی‌ازطریق سایت فدراسیون تیم استقلال رو به‌عنوان قهرمان این فصل رقابت‌های لیگ برتر معرفی خواهد کرد. چهارده‌باشگاه‌موافقت…</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/persiana_Soccer/22483" target="_blank">📅 17:35 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22482">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ATWwUcNBah5L6F9Ui5qiLrdhFbmFiFEaQlJl0_eYiuZUvLEcqXPC-q56amIBneYIkhoydTBrAfd_2mzrge-6Rw4owUyZS_x6z3dZU1Y19IdhxD7JOxujUFP55lJK71UOGlpWhhnjSr9JhJBfhOyOjohP_4QPyNSs7SFsMUUfJPxOIWmEEsb-b5xylkLeGjEvTvc3gKNRpafho3WsPh_fODfFd5QnK2VxvnKGuX9Wuoy1KCwoML0RSFt3EDLo0onz7M5CeqFL3KhJbQ2hXsszXbK4U2PlIGvD1g0brqlwCVqDUjqpmFLxXFEJWi3N6TDFp_fpIK2PvKZLNcSaQBI5DA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#فوری؛ طبق شنیده‌های رسانه پرشیانا از مدیران سازمان لیگ‌وفدراسیون فوتبال؛ به احتمال بسیار زیاد رقابت‌های این فصل لیگ برتر بعد از جام جهانی برگزار نخواهد شد و باشگاه استقلال بعنوان قهرمان این فصل رقابت ها معرفی خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/persiana_Soccer/22482" target="_blank">📅 17:28 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22481">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Aparat Sport [3.6.2].apk</div>
  <div class="tg-doc-extra">8.2 MB</div>
</div>
<a href="https://t.me/persiana_Soccer/22481" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">✅
#مهم
؛ رفقای گل این اپ آپارات اسپرته که تموم بازی های مهم روجلوتراز صداوسیما و با کیفیت فوق العاده و با گزارش فارسی پخش میکنههه. یه قسمتی هم داره میزنی رو صفحه میتونی هم زمان هم بازی رو ببینی هم تو تلگرام و اینستا آنلاین باشی. خودمم ساعت 8 نوبت دندون پزشکی دارم از طریق همین برنامه نگاه میکنم. عادل خان‌هم گزارشگر بازیه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/persiana_Soccer/22481" target="_blank">📅 17:17 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22480">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fSvGjygDAp4449rJEQW5fI8nqGJvMzSu6Zwa3okYa7VPaqFaNnUxOoFZCs1VwHlxAQiY2uaikTV_j4swllpbkKemU8ceFMVEZLNnxKfBCHjn1ruXzFbyLshXNISdnX2X-dOFRvMP_NjOlyFjcKj51cWGQGHuNbPeiJXzFP-HUXvKwd2jBR-sgzQu8U0D_CSoISnOPTPE9UxL0N8vN333woyxK7qcmx3UDgtlfb_peg_VkZe96KDJPeiIUNnNV1yGaGsicn4a7ZXCURx_HR7UmhGOH_GbA27Cla8nMWoktJeTMf9kcUzgFV4ZKID5Y4KQdILjNLoSNJTX2eJAsnbK-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
دو ستاره سپاهان مدنظر اوسمار ویرا سرمربی برزیلی پرسپولیس قرار گرفته و به مدیریت باشگاه اعلام کرده که به هرشکلی‌که شده این دو بازیکن رو در نقل‌وانتقالات تابستانی به خدمت بگیرند. انشالله اینترنت همه وصل بشه اخبار زیادی خواهیم داد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/persiana_Soccer/22480" target="_blank">📅 17:03 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22479">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/caf37364cd.mp4?token=m8BvG6pIZuLK9OEG8e9LSp3XAIpLadfYKnHA3xOfFMbLi9Fft5xLLlQ7n_h1EbJu0krJThXcEMt_tSRkPzpb1IpSBQXvijL0uwXGC7b1_RGkb9bvRNpImPfJONyOSW5khCWyP-iZrHTMz5k9ED7XnnRCTEDyfVKRY_5WFNwXeChzr392FQfOXC9sK809w2zXt8x8vPaCFIFrhoEZ8Lw3BURyfrGjA-7FZJbj3rS3A01XECnQHJJawsgUCGWrWAnN4Mf02-GfgwKeXF6cNMRsgCP9RgrH1cxPzGu3VLfsKPpOC5eEu4a79F8sVrtQDheNEixbrOluZ2LPWoCVcYvzSDH2cNJ-wBh_ZtiiaOioCWItHaoOCoYdmeX9XO8D8iOWQySWT5r9_m4uN-20SBT-6lE9GjAfHU5JJ0GZNTxqHUWeAm7TRkZEwpp76-2eAvlIeY3t1GK11nCJE0nnX7eyq4wpK4F6MJeqjRgvJ9Iln_zE5QLos9JodbN1yFkJZVdaQ_RMBLYyC-7lpHj6kzZRgshM86--rU6OTz5jobGFB5QIMHH5DYjH3DjFADy2J7E6jd0L0TSMPuyRrvmMVdvCinIv4flbv8kLzs3KB-ajuy0IlHl1EzxF30wajmdywBueutp3HrsGZqaEsXVcVcSFfWAFa9Nuen_wp53nrezNpZ4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/caf37364cd.mp4?token=m8BvG6pIZuLK9OEG8e9LSp3XAIpLadfYKnHA3xOfFMbLi9Fft5xLLlQ7n_h1EbJu0krJThXcEMt_tSRkPzpb1IpSBQXvijL0uwXGC7b1_RGkb9bvRNpImPfJONyOSW5khCWyP-iZrHTMz5k9ED7XnnRCTEDyfVKRY_5WFNwXeChzr392FQfOXC9sK809w2zXt8x8vPaCFIFrhoEZ8Lw3BURyfrGjA-7FZJbj3rS3A01XECnQHJJawsgUCGWrWAnN4Mf02-GfgwKeXF6cNMRsgCP9RgrH1cxPzGu3VLfsKPpOC5eEu4a79F8sVrtQDheNEixbrOluZ2LPWoCVcYvzSDH2cNJ-wBh_ZtiiaOioCWItHaoOCoYdmeX9XO8D8iOWQySWT5r9_m4uN-20SBT-6lE9GjAfHU5JJ0GZNTxqHUWeAm7TRkZEwpp76-2eAvlIeY3t1GK11nCJE0nnX7eyq4wpK4F6MJeqjRgvJ9Iln_zE5QLos9JodbN1yFkJZVdaQ_RMBLYyC-7lpHj6kzZRgshM86--rU6OTz5jobGFB5QIMHH5DYjH3DjFADy2J7E6jd0L0TSMPuyRrvmMVdvCinIv4flbv8kLzs3KB-ajuy0IlHl1EzxF30wajmdywBueutp3HrsGZqaEsXVcVcSFfWAFa9Nuen_wp53nrezNpZ4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
این میم دیکتاتور داره هر روز سمی تر و سمی تر میشه؛ تاثیر کیلیان امباپه روی هم تیمی‌هاش
😂
😂
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/persiana_Soccer/22479" target="_blank">📅 16:55 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22477">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YDXDNySxefPQf5ya4bJWPWltq_6fBrG1dz9ugCEux-9Llr7ZGNHgROD3xGc5uuNNcc-ufoeJC1R66ntajX_efL7RVqsGyVVhNxePWwLgjS8KnQ6CR112ogI8mYwI1hY9MeoD6bUu8p2_hzYwN-14Z-JzKhIpux1DbWcq7P6gqYNsnWZMIH9F_obRJ78piv62LlOSqA-ZQmiTdpJZl1Qa-MMdEFKft7IAqPpie-YmgZ60pIxiPnI8T_2xeRZT_oCSQ7NapfEDo7h27pIQlgLHKNg3DbavtTcM0zKkJqM_MfxT1-pNsIAZREsDn4daEal_3GBi_B2Y1VzwvUVyB33m4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ftkNSWCNABU-go6sz8Bbae9H7FA8bZU7at0QQfBPxOG7t8Mf4fQRzAUKjLuPex4lJ-TwfU9cpgk1ZaC81Vd-O6frOkj1u82KcY6CuSwyXg9AOBueHqpgiw1uMNhGrFNSLaVN-LX1KjbOClfm_X7IVbMtpcujct1zr9VLkNpXVxUfInrWOqABGjqgVwP6XiEMWWKFJu7fxbdo7Jgo-BzN9TwIMmNCqB-Tmx8F-0pq1uv7urqAN2f2GQvFWHatDi5UokjAJ-xV9Eh6ZfFvl94BzWbTMyHPXmdcUDFmJEPY1Im8aA-rW66WHYtzEj_4FtTTV7BZIoP6mq2TGEqHIP2kRw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇺
مجری‌ و خبرنگار بازی حساس امشب دوتیم آرسنال
🆚
پاری‌سن ژرمن در فینال چمپیونزلیگ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/persiana_Soccer/22477" target="_blank">📅 16:46 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22476">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lB1GL1bl6aTTvmc7BEG26eXbIzCpTaNFPtcPCQ68xoagwqLKAxBe99056NT1ADC1H5WNAMZXDhOszq7KXKnwThxR5EiGxOF4Z9klYR6QZma_9sTFiVl7I4oMb2-nrE2cxHwF0-Ntk4TNI5ZlsBdGi2UMeWF_yDN5oDaM1FtbrKtpY8gtjPJNYVAh87H-hfzn05aSSI7PaYqpoQObgkMfNAYZ4NnGAVIO3TurtoQ0hKyAnlOlc0Geg4zFvfZ7qOpn_o5Xa3uRpeQGU_w1JaJ14ab2bNIySn4YGxdy6A-kmAKVfrH1oUGIcB4_t0ydp6lk7ToaufFU836X-ctNDJm_hA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
بعد از یک فصل اسفناک؛ آرن اسلات هلندی از هدایت باشگاه لیورپول اخراج شد. اسلات سال اولش فوق العاده بود و قهرمانی لیگ جزیره رو هم از مشت پپ گواردیولا دراورد اما فصل دوم ناکام مطلق بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/persiana_Soccer/22476" target="_blank">📅 16:33 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22475">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d18fefc27.mp4?token=XXMy7TV0IpXroGT7Q3tmxvGJ_6FK77UgSy0aPk7XN3StNyKUDmHrEqn-wx5EUXzxbPK45oQKWknDnIH7ybSSD5LGeaxI6goxEtKlnVZBBvJ4t2qsvsn1RqSCzOJ4FE6qs-r_nbPWORFMEknbDsVkMcDxgmsuqM2O7LpO5710F8loUvYNDvAIQCCyZTOI-wuA4FV33M-4bQwqwZyW-mplgPbsK-pIzt_0qWywHsMhyV2XLz_XVsQnKJUSDrsujf05FSeY1WbgHEqaX7as4V8YvOnys8WCwr8Ewc-w5R8SVgGF06qV9CRx8Ua0pYO1GTRk4-JCU0M53NNtbDt7iy4SKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d18fefc27.mp4?token=XXMy7TV0IpXroGT7Q3tmxvGJ_6FK77UgSy0aPk7XN3StNyKUDmHrEqn-wx5EUXzxbPK45oQKWknDnIH7ybSSD5LGeaxI6goxEtKlnVZBBvJ4t2qsvsn1RqSCzOJ4FE6qs-r_nbPWORFMEknbDsVkMcDxgmsuqM2O7LpO5710F8loUvYNDvAIQCCyZTOI-wuA4FV33M-4bQwqwZyW-mplgPbsK-pIzt_0qWywHsMhyV2XLz_XVsQnKJUSDrsujf05FSeY1WbgHEqaX7as4V8YvOnys8WCwr8Ewc-w5R8SVgGF06qV9CRx8Ua0pYO1GTRk4-JCU0M53NNtbDt7iy4SKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مورینیو در اولین بازیش روی نیمکت رئال مادرید وقتی دفاع کردن ترنت الکساندر آرنولد رو میبینه!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/persiana_Soccer/22475" target="_blank">📅 16:27 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22474">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oEmC_Wt56hdUezatNN1eGLRrkq2elu9R2Zyj1v0bnfHaPUW1VkRFAAgbdItroMmuwuwigsixMTiATJz5u5bCxwWyEhIR5wv-8Wkw9_SwJBq_kVeKapU4kyEFLzn8zh8_EI5sC0s18AwJs5jP_RZ0o0cO5xCXttz2SLk4ciIa5--vZuQIt8lfPJt4VSp9dnuyo3PXeAlHR68J-hJuNvarmxE69HsdYCTx1elNRNLgh5TFaZ_E1gNhztcEClgqXN_qHW41coTMJWabkPe5Cpq5FjIxf6y0yofbvG-67w8CnX3eqeWDuiLs7RX-DnWFiuYGg36HnMPW7pCGMltsGRyx6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#نقل‌وانتقالات
|ژابی‌آلونسو سرمربی جدید تیم‌چلسی خواستارجذب آردا گولر شده است هرچند رئال‌مادرید این بازیکن راغیرقابل فروش اعلام کرده مگر اینکه رقمی بسیار نجومی پرداخت شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/persiana_Soccer/22474" target="_blank">📅 16:21 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22473">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DvzQxe5BEwUDwSZuhgjqCwKNl8DpMKj6N4Er33mgQqOCBSc3KpjCzdR87KsOlmPVn3_UjSudZ9LDtYoPr0_ljj-06NRQczYvVV_-5Svpjn2Tk5WUlknhW4jdsw13UcUTEQP8Ms8RhpEDNiExKT1nBu9RmGowZqrIr6COhsCNQG2cwTR3et_SUN1WANJ0ZyQLTpiXuXjtf2H9xwP1k8PeYJ5ECjmj--GR-KkTU1WYjGssYhiXJd_0w_gnI6ZLZyCyt4-vd_O-XvFzpiz6gSEND9KMxs8qsz2oljVKXRZ00st6QhZOXsJvXz2lAsV2RWgzvyE8htkkpqQa1vQ2E9Xa2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🏴󠁧󠁢󠁥󠁮󠁧󠁿
عملکردفوق‌العاده‌داوید رایا ستاره آرسنال در این‌فصل لیگ‌قهرمانان‌اروپا؛ رایا درصورت کلین‌شیت در بازی امشب، رکورددار در تاریخ اروپا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/persiana_Soccer/22473" target="_blank">📅 15:23 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22472">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h5tnxyc6go-ghPgU3bkiXL8PLqbukfQAV-Ooen4YmheD1vT9CILNU5tJpK3aoDjIaoQ0ezi5vm4j5VoriPv8w79qsJ7sRHAAFNoH_ZIVxQ4zO1h7dNyR0ygrDMVNh2ua8OU1OA_mvDuRNIHa24Deto6lxEmxsG1lsnDrn4X_hFXPyOzqBtByOQGy3gCXKrmfhDVX7RCJ9MK4Bx-ePp_RFbOMuK0bt0WN3kyp_NUOyCErdhUMyR8J2YUoLuElXdHxj6JcY-51zLT2eFOBqLHO0FEN1YB0QZ2AGfFZe05eJn3f3Jl5ule2EqcHWRe6oTXQKkXcYG0a3xjlu4zL9ueXNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بیانیه بعدی اتلتیکو: هیر وی گو؛ برای پیشنهاد دوم به مشکل برخوردیم، بلیط کنسرت فردا تمام شده، بنابراین پیشنهاد قبلی را با ۶ بلیط برای کنسرت یکشنبه بهبود می‌دهیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/persiana_Soccer/22472" target="_blank">📅 15:16 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22471">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VrccDkt0QtKcEnEa5HHww7-icNDGoWpnhbXizVjnfXSFdniEpiSWjdNHa5B79KShBGCg1eRIy6nCG2JwWZLxbFIGtg3JUz6tH0FnfkSdeqaZgyr_pQLjD58r2_PUUmddIGRIx_YU6yksrpb5F_okd6Fg2EJqsfUMQiOJsy8_WPdOGGdLxCKu0EaovgQnBjCufTDRSmzW1rBBKW23nPb49vKFGto-Drcbb9-E88BCcnVlfnEyIZSDyRAPtf5gEv7TxT6L9yxhozgfK9z5Gwmo71QRSalQp-W9mhzYgae6pqMRQMT1iironhSNCxVX2p4BlaYgudCVQkVizqvVImRZ0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
سیدمهدی رحمتی سرمربی خیبر خرم آباد بعد از اختلاف با مالک این باشگاه از هدایت این تیم استعفا داد و به احتمال فراوان فراز کمالوند یکی از بهترین مربیان ایرانی‌هدایت‌خیبر رو برعهده خواهد گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/persiana_Soccer/22471" target="_blank">📅 15:09 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22470">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OLfV2-VsGSQtyU_28pMDlcHhMCK6EQCPwEGTKj-8NWGyaUy29v1MjBCsqGcmd96TYyFB_bICoTyiga76fPLzUWTTQsvqPNVC57NFyu4FoCpO09iI4Ef5FOmAbEdlSi1OBTj0FlIDtSzPMt19SR5af3ADSDbZODS2Iexdl_4aNbtBHbtY_X68yuIbo-I8B0D0IVq7Pf_Loj8GrPrVanBN5ge5u1QESSL8ZbxhoY_3B4VW07zTk2P5Uvlo2wuyQBiZrkX8X-_FXDviDdfqfAWpI_mpeE37evQRu--018rMyhnThtqG7mqnWYFNHEyjhERTCvZMo2py1w2NJYZsJ-nd3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
بعد از یک فصل اسفناک؛ آرن اسلات هلندی از هدایت باشگاه لیورپول اخراج شد. اسلات سال اولش فوق العاده بود و قهرمانی لیگ جزیره رو هم از مشت پپ گواردیولا دراورد اما فصل دوم ناکام مطلق بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/persiana_Soccer/22470" target="_blank">📅 14:45 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22469">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M9fTka8MRrTnF3wRpDjmk6U-4oyAqMYDN3D1v_exbBjPlbswtzvSUnK8kkg7a44JkRyaCsBhGu-Ly_D9ziyKxFo84o-aC97nYy9pvZeggAkheQgqi_yrQbZAj4sbng2YqCmP_WlaRqN3u7lbydIyOORzOC4Tsr-1dm1aynk75w3LII6P_O3TvCHjzZMgPtaku6K-bGid2JpfQngunyEmoiazSkhDE08qOH61loNGvMu1tC2DP64pvUr6RoejIpRtLDWS6kyERi5J59XXx0_nbfNFo6xQYwo_cM4g0cqe3wGnSAyxMuWL9IDFfgy_V06-jTY9MTr98ss8kD9aFemCOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
🇫🇷
#فکت
؛ کریم‌ بنزما یکی از بهترین مهاجمان یک دهه‌اخیر درکل دوران فوتبالی‌اش تنها یک دوره درجام‌ جهانی برای فرانسوی‌ها حضور داشته است!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/persiana_Soccer/22469" target="_blank">📅 14:34 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22468">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gwxZxncMLyIqqQwLtQguNNGqye-H8uc9IQ0RzsP3u2KynNq9ZbdG-xm3SljMWAwht58c9bfyPKDNigtgYUhaN2_nbCV0km3uGIJgE25QrJZ8ckNXlBPGwFTv0pWjICnwWbGZYe1eKAOqjy0umoEnEqIWVYEKIA9VKh_loF_aUNudR0EAcx57b1qYzWzjgetJyavJOByvL0rfcUFyBXVyNTs30Bu0F5PTIkC0tOELV4JjV7KYjmwnp4jW3lVKpspsA3QO11ble14glKm1RfTLCoNzNGaHYyCeIsj7KdHLADlMVZvzq5xtKmQHefbHm25QiixU-EWVhqDCnRxCj30luQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
🇪🇸
پیش‌بینی ژاوی سرمربی‌سابق بارسا از نتیجه فینال امشب: PSG بانتیجه 3 بر 1 آرسنال رو میزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/persiana_Soccer/22468" target="_blank">📅 14:18 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22467">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MPrFesDiRifCaML5Jna_Vp1wNemFbWE2NM6tvKQy3nCMkdkAQ8WjallCIYDzTMBqZU7-7whEoDNuHND9udA1Dq_d-WjjfQf_NAhZO0O6KCemuRxk_YVQyAwQtNTHHpqyNp3vJTBSHUQxgOgieX4tUW1zwPoCfFeNf7Hy6Xazrb73-XSEz2J9gUm8a8OrELnTc8bn9UiRlzCp8kCAz0uaKtnK6CnRcBpQmcGb3ewNOxBfXTll3VSi2ASh5ZSGqpxkkxItgE8Z6hflPsa8eVIobtKlAwkd74nlHQ-_wNkogJ0i6l50yre19BquUEBrN-s20QLDXX3xpflJCFPv_9fwwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
باتوجه‌به‌‌مصدومیت‌های‌پیاپی در فصل قبل؛
احتمال‌اینکه امید عالیشاه درلیست مازاد اوسمار ویرا قرار بگیره و ازجمع سرخپوشان جداشه خیلی زیاده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/persiana_Soccer/22467" target="_blank">📅 14:06 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22466">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lq626h79W_T7r4zY6IvltSKbSXhbSILk1PIXfFChoZ1D0vxsrwLt57Nmn4L0bWI9-SzYpDXQEQCvIxBr7DmN8NrbO0boSY3ZvYMoaPvl90CMyGulByGqTfhZIrvnAuhwp5byEp_F8WCcXgjugPYqLCEiZRKgpZT5YGnw2692iuI-ocVZOrU0dNTvG3HjkYGH3C4TfC2OlHXl0gllLRvigiu2mThCh6rzcY2uhPDx7yI31yo5iskp-McXNAefwTzSUHy-90MTyfpkai3Yu56Px-Bpwn4DIV1Lw6BW79DkTOXaapp_Lzr9tG_mtqvBb3Zti5xF79L3BWXuj1GBJdDDgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
ژول‌کونده مدافع میانی تیم بارسا با پلی استیشن یکش رفته اردوی تیم ملی فرانسه برای جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/persiana_Soccer/22466" target="_blank">📅 14:03 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22465">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oS5k-a4UMSmlsQqmYiK8EfXZqv57RkMlVSFKjz5BJ8qblO8c1fUg1q7h3Povukjxy8JQYODjqlTNuXGWfo3hpK9MgHct9TVrOoUv_2X3a234_YzUJiGTDCnhIcDBTUuLE9tay4xnv-BAL82V7mlOPSOl5c9VBZurxvkQEpRgMrQ8XKcvTAdVOE3BkMyheBKZrlWmCP95S9lP2QNOXSaT7NEXIi8mJ08UOp6IGdckqp4qqQYQ8u3RzfXw40_MRTbj7MrBSCl5T41XDgg-6VvLo73_BQ-RIYjki6dLeeOHFOEkHDupCX-5FLmm3H0tPsEtPxUOlY9mYYppQxoxHkcplQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#تکمیلی؛ علی رغم تلاش علی تاجرنیا برای گرفتن مجوز رسمی فعالیت فرهاد مجیدی در لیگ برتر؛ اسطوره باشگاه استقلال به مدیریت این تیم‌اعلام‌کرده علاقه ای به بازگشت به ایران ندارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/persiana_Soccer/22465" target="_blank">📅 13:36 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22464">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KIq10VnZZ-lXiTZywjyQzcAShEYOb1JRADWVdaY6Sl5WFvL5tHE3nrOvKMiKDP2KQnxpUcnD_n_UAxS0l5Y5nudWHzu2V-fWL-1WuHLrY7FqFym0W_kgQfJXH1UHB0GNAdSqhxZky-ecTNjMhLDHFNc6CLG-FTGn1z47wY9YC10Q97S6JxT0NnFOcl3P_0_xngcJgRjl9-4JYPomKdCNNoktr-ar7obs-LrRwgrLy27xC6cRNf3ui60lmNud1WOfPV43WCr3fF2_nA4oMkmorWHbxBdyBxviQNcI2k-a10wqtyx8z1DQZPVpJ3fhrgesmm57f_tW2DCRxFTxK4yTkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ استن کرونکه مالک آرسنال در صورت قهرمانی این تیم تو چمپیونز لیگ قول داده به هر بازیکن آرسنال یه رولز-رویس فانتوم هدیه بده.
💰
این‌جایزه بین 530 تا 580 هزار دلار ارزش داره.
💵
ناصر خلافم قول داده درصورت قهرمانی پاریس به هر بازیکن این تیم یک میلیون پوند…</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/persiana_Soccer/22464" target="_blank">📅 13:30 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22463">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JcgjBAraskTv6Vf1vmRDb7D-QHMns_8AXRNkQiZWVziSEBgAEcQDY7u7XWX-qclNwYmIWTHKVn6TQqtAY8toVleNeAYrMKWhStEFmfy9w8JUEC87fLyFt5yJaxVkYrZK7G-nqrTVuqBgjXOtIYEOeIKkDUuUPUt5pH3i8Tgh7Q0ci58W-pxy5adAAICmXeAIBWcipAf7kfFN5viCCroRtZbKcRBTwXuF2uRbyGQtJ1_pMywZxutss_deYcEaPcTJCwGdlFXeJwEL7rcgUsTjJjt3hbyooJMAedOivfpodNoKBzprI5yURMl_aDAgkaIMV-HDPZcZYwWmpUlcZGKisQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#تکمیلی؛ علی علیپور مهاجم 30 ساله پرسپولیس بزودی با حضور در ساختمان این باشگاه قرار داد خود را به مدت دو فصل تمدید خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/persiana_Soccer/22463" target="_blank">📅 13:15 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22462">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M80vGr5yUc2YOeYj3ZLBSY9mLpl8hcSdbw9DRovLOfqcHnaP8EjU1eLx1H7irtE4pDQwqgZPkGQp1QldowgL1q-Tlvqk3nfDcuJfCxwBCdREKynz1d47W5POMPb7xqcxrS3pyBYKIhvn2h49fDznAYoougBnvhxI6Suf4Yq8AmRTyunnHYdrJmrmo4LoUfiGr49Zxn_CM2dgDNjyRKN_GV2ml5NOXQ-uQjM6hueLJ57WPtaRfpHvgpVPZzw_aYfl6vfO3PzbZ1abZPGr5apI6kXP51UMfBX8ZdUzzvkD5ctThwADGeD_ceKQNfce0GTl-krRJVjpSPbMojRN15vilA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد؛ با اعلام ایجنت یاسر آسانی؛ ستاره آلبانیایی استقلال برای فصل بعد در تیم ماندنی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/persiana_Soccer/22462" target="_blank">📅 12:59 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22461">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D9rpUt15IoWR-vct3sNOcDQVjetwYZMtNKB5XF7eqm6QZ1BcIH6ts-gjbLRgupiHIYFlvJSl307rIunGzw9EYLWwrx504E_QswTBlT-HPZwIkPW3DoIqVPlKi2ozNwq2t78NdDmFBFPTjQBvF4HRO9BYpgPMHHBA9vtJBiXnPup3aLXZ4nGMIR3_o999qmddObr6K3e0t9A_nmnTIKcomN6bqU1tVhPBRHziZDcI0VC_SipYRexvNccn_zZz84mggAaXxQ81EN1lN6XBEpVB6xHPQcmMs5A8zVNIohzwyCqQ6VY0Bh-s4p-32OElmaIGb1lU1RuEXonTpreWvVNCiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ رسانه‌‌های‌اماراتی: علی‌رغم علاقه شدید فرهادمجیدی‌به‌استقلال و هواداران این باشگاه اما اسطوره آبی‌ها به دلیل حکومت جمهوری اسلامی قید بازگشت‌به‌تیم‌رو زد. مجیدی زمانی به این تیم باز خواهدگشت که دیگراین‌حکومت وجود نداشته باشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/persiana_Soccer/22461" target="_blank">📅 12:56 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22460">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OocCeQCDrfVxd2KUE_fyBh9QsZpTKwfKBFfHM4olN39H0VUsf6PPGrtiCcWg50PF5aCOWBNW4508luMd7l5wBOwYb5g_98do4k3fw8x9fkbdluhDDVIX_OZd66HkG7rogMYXLqw5IZ2mzSK31hCoGHRLiS6OkrCt0W3v8pmW5SwoUzaBoaq-1QbLe1dPrmp12dpTmyl3dtuIlFt6iuljxyq7RZ3rHFtSS94N9PRH3QO6KyBOlRFKebj23XJzOQGZ4sNrgEpCV9c2UaxWL7x386mWzR23mSp1Hbj6gOV2ybjKTK9moc_B0mBt9zftFtZuIePL5todQT3SyBbgrZ3j3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترکیب کهکشانی و پرستاره بارسلونا هانسی فلیک در فصل‌اینده رقابت‌ها برای‌فتح UCL؛ به این ترکیب به احتمال فراوان برناردو سیلوا و کوکوریا مدافع چپ اسپانیایی باشگاه چلسی رو نیز اضافه کنید.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/persiana_Soccer/22460" target="_blank">📅 12:21 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22459">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5359012d10.mp4?token=gKpt_C4NaNFc7pQL9f8JpkSJ6Ir04dQ8IIYwGnml3T3pzLGarjg2_iSo22lDELPGoXFzZFEMFsaAahXq-kgIwVswl3F76ELDY7H_XgtRjdMT-s3RLpnbomNPTyKltBSC2nism2fpBxBKQCNqCR3V42HG7zsRn1zZEdPuMRCrLII5otcM_tp4Tl78ipyqFcWRhrfv1yKVBdDd8Mikf9A4B1H87r2ANGTwxSmfM9son6eZcJNx4g0X2j-2EJvDGu-cWgXNIDKlV565yeCKtg1qHrlGO4A4orC6NeVlccfDcDwq4OmUzm0TCZ-8QN0zUAlIInqbV4qvsPEx1aODY0mBFms_E7rqMIFZHhvkEe_w6pr-3ardveKuV6PouG14vPRatgH4q4R-maUImbjv0Oo56n18LoNNkYa9hSyiDghBc_lOXLmSFrad19nL5TZWNV7E6rozlKWWstfwBjBzILY38cwArCPRnQRaqxQaue1O-zeKeVIKWRd-owWFDWbxjYzJnLEDU2Hp4sbN_9SWbGR4SiC3bUqDiAFFF6zGtOqXmoL7U94Z-3xcMvd2x7Uzmg0LIxRcyeNLm25XAPGL2sCF4AzbJBLLmjHsiX3gRAG2h0FhcOtj33VtfsGlKPAGiqST4yTa6-DGM0cbINLzIVor2oUNH5OD1iAcYig4jaGAuTo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5359012d10.mp4?token=gKpt_C4NaNFc7pQL9f8JpkSJ6Ir04dQ8IIYwGnml3T3pzLGarjg2_iSo22lDELPGoXFzZFEMFsaAahXq-kgIwVswl3F76ELDY7H_XgtRjdMT-s3RLpnbomNPTyKltBSC2nism2fpBxBKQCNqCR3V42HG7zsRn1zZEdPuMRCrLII5otcM_tp4Tl78ipyqFcWRhrfv1yKVBdDd8Mikf9A4B1H87r2ANGTwxSmfM9son6eZcJNx4g0X2j-2EJvDGu-cWgXNIDKlV565yeCKtg1qHrlGO4A4orC6NeVlccfDcDwq4OmUzm0TCZ-8QN0zUAlIInqbV4qvsPEx1aODY0mBFms_E7rqMIFZHhvkEe_w6pr-3ardveKuV6PouG14vPRatgH4q4R-maUImbjv0Oo56n18LoNNkYa9hSyiDghBc_lOXLmSFrad19nL5TZWNV7E6rozlKWWstfwBjBzILY38cwArCPRnQRaqxQaue1O-zeKeVIKWRd-owWFDWbxjYzJnLEDU2Hp4sbN_9SWbGR4SiC3bUqDiAFFF6zGtOqXmoL7U94Z-3xcMvd2x7Uzmg0LIxRcyeNLm25XAPGL2sCF4AzbJBLLmjHsiX3gRAG2h0FhcOtj33VtfsGlKPAGiqST4yTa6-DGM0cbINLzIVor2oUNH5OD1iAcYig4jaGAuTo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
پنج‌ موزیک رسمی‌جام‌جهانی دوره‌‌های اخیر؛ تنها دوازده روز تا شروع داغ رقابت های جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/persiana_Soccer/22459" target="_blank">📅 11:24 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22458">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RbJUMbkON8d6b1H9zGokvfFKZTkeKBbY6niKe90VU4sDYXiJCuhTmmKz1pIMSgYBXJWLP3ECUo_oezUSrSiD9dqce-ob2grhq0Gskcs0XTVVljjRgqa58VCAoMyl9QWhlLhAx-ew1gSj08XwRNs8028hs9akLk5L3rRNl1Mvi3V03A0UIsHZ4ByHV7jANlBez12mof46szmF1R0NjOq86EcIt8k2tS_uF4NqWuPmae7N9nNQjJErVliprayNTu9xOjchrT16zADdMw-jLXFZgagsTwalIdriWJq3LIztIEWR9A4TKE2R1xeJ27T3K2g-jdTsZbfVSRQJm_-iYz5lMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
مدیر برنامه‌های نیکو پاز: ما با باشگاه رئال مادرید بر سر تمام بندها به توافق کامل رسیده‌ایم و نیکو درپایان فصل‌جاری به این تیم بازخواهد گشت. منچسترسیتی، چلسی، اینترمیلان به دنبال جذب او بودند اما نیکو علاقه داشت به رئال مادرید برگرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/persiana_Soccer/22458" target="_blank">📅 10:59 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22457">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YlqHutynwJEmpfsjvOQlnqEV5waxixf1BOWmu2p7rfYeQJGjuWY7Po6NMnRxlvXSTkozzX3s0WeGCR9Uy9y_A4Pwp9jiU_qa2ZkIbP54w_xUdOhrrey_09uatfY5U13ozlu3PhNZY6A77F6PYEX1Osc_DO7Moaq8lIn-Bp_yzowtmvmYt_7sW79T-X7FcV4jPE8tmVCaGQbX7QgnyTa7SvfNFdAOCqmlQZ02vmFVNmX46h4EkuVDNO42XGhPpciNnBYrK7uYDZcn6vLgNazOe3mrnIct2R89KkmJv1S0So6WjxRMRECwsm9vB6RL_t4OrI1kbhJbAB_Oq9zvFyh0ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🏆
به‌مناسبت فینال امشب و حساس، مروری بر فهرست پرافتخارترین سرمربیان تاریخ لیگ‌قهرمانان
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/persiana_Soccer/22457" target="_blank">📅 10:27 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22456">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FKA29KFK4T8MGNwIgbYtIsV1j8-RKIV9CzjvpYu5ZA8np9knljWQSOOGnUX6UWRnVyGON6_0ZIamJPMLrKOsicBleQjFKssmebU-yIrjEvhN2XIxaItkWvYoZQ5bEOVx1zidd6nzl9cGIjVxDdk1ku-A1wuxxaZYnsESdMB2vwlrGB8i0pYvRueE1fkJXGWrpfrAhCjB5ZLkRMkmwwLqBJM5TE6u32kbkS9V1m2s0ry0zXhx8LTc7Kj6mNUA3wZ7apSYwmsGYZxyqEh0e53mVL95KlPT6aNNNz41KxzpJdhBTUHu8vosfyhn7eW9mMh4dbHQkO_310J5TpzuC4deVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
لوئیز انریکه‌سرمربی‌تیم PSG: میکل آرتتا گفته قطعا آرسنال قهرمان چمپیونزلیگ میشه؟ اینا همش حرفای هیجانیه امشب‌میبینیم کی قهرمان میشه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/persiana_Soccer/22456" target="_blank">📅 10:27 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22455">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eAe1uls1JB_Oh-rx8PZCQnBfevPYW0uYDGEdGiy_n-cO6G8QxxCJ4usf27FEv2STFwyBaG7P36Loib12cyTNZO_TL-EcEnwOSYGvlMkxsI2uRAsTRAoRGv2XKJTw9om-D4783waVVMOmfwjCDNVX8oYdJXH18Kcw4ljZbajfIOP-lkYDbML2ZbMzj-YSjtbNHkIWEI6EOJrTuqpfHipk2qaSNG-HoDMrITDIdAnppKvSkdCQ5Vh84POGrDjp2Mc781Tuene2N923Higr46uCDuPhPB-3MwKrbmcN9eSmDpP_KDK3JbTj1u3T1TlDpzXwBOm5bUqHH1NjOY1P0DANOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👇
فینال لیگ قهرمانان رو
#رایگان
پیش بینی کن!
🎯
با ثبت نام در این لحظه
#وینرو
بهت
🅰️
🅰️
🅰️
هزار تومان جایزه بی قیدوشرط میده
⚠️
🤔
میتونی رایگان شرط ببندی
👍
تنها کاری که باید بکنی اینه : عضو سایت بشی و
🤩
🤩
🤩
هزار تومان جایزه بگیری بدون واریز
💖
تنها سایت مورد اعتماد ما:
🌐
Winro.io
🌐
Winro.io
کانال بونوس های رایگان
r9
📱
@winro_io</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/persiana_Soccer/22455" target="_blank">📅 10:27 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22454">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d629612bbf.mp4?token=Nv9lL0I1GSPLeRpiyiH48pVz23BkiFQd_9R85Lndii4CV3LS9Rtnn-lOMoRWyH0CWkoq-HeMd5oyK3CXMKHSlzCxVtAt2vwVG0fKoU7Rf7OPMKhi_fKnZ3Rm6aTJeUuYQm1eHSUd7n56s8CBi1y8_cXcaRPrb8oeuWrAq5MMUCW373wdrKo748vf9_J_K1ZO6fdfRb1RyE53jCrMb6dAw78Xq6TCvtaSn5czb8dPrxRELTLbiPyJtjhtSdP4YVxRdKanyShNRZNZnjNFV-JUHSXfnhknqI-6k4K8WoSjrcQ8PXhnGgHo8oFKgGnhxwLwnSxdfNh6fcrGraYUa_KAYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d629612bbf.mp4?token=Nv9lL0I1GSPLeRpiyiH48pVz23BkiFQd_9R85Lndii4CV3LS9Rtnn-lOMoRWyH0CWkoq-HeMd5oyK3CXMKHSlzCxVtAt2vwVG0fKoU7Rf7OPMKhi_fKnZ3Rm6aTJeUuYQm1eHSUd7n56s8CBi1y8_cXcaRPrb8oeuWrAq5MMUCW373wdrKo748vf9_J_K1ZO6fdfRb1RyE53jCrMb6dAw78Xq6TCvtaSn5czb8dPrxRELTLbiPyJtjhtSdP4YVxRdKanyShNRZNZnjNFV-JUHSXfnhknqI-6k4K8WoSjrcQ8PXhnGgHo8oFKgGnhxwLwnSxdfNh6fcrGraYUa_KAYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
پدری به‌همراه فران تورس و دوست‌دخترش رفتن شهربازی، اونوقت پدری نشسته کنار فران؛ فقط قیافه پدری که متوجه‌شد شب‌قراره تو پارک بخوابه
😂
😂
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/persiana_Soccer/22454" target="_blank">📅 09:45 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22453">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c867b80a08.mp4?token=R7zKmr3QKS4tMhzjhzMCkQK5BAb-9O0FiznKzlaS1v44F3dex97_TjbjiJIVPF4rZr9rNC_UnUksY16TFfaYGMaU5hXCrm-9L5yaAs4TraDJ_sjrVyTYzeBX2I8qk3vlMxedDYwsoDbawTXXrbI7WYisMvQafYNxWJ0KLvh8ipn0ld0PkfI33CkG1FMl5Ln5eikEOuoCFYdglGzDx8z-2gZCjUBvy1akTVxh6Bw5WHjLQbTDLv4tTXdOUpWwfG4FjcsQGLfm6u5cCSILLkRHtIGiTnGofd4Cne991Or07lCPZL2iP8b-Y0eaT1SmgBnG0WIdE3ikt7QytZHSqmKbeW8eBJKneKaqF51Xh34nBDlnmkCl85WCehylZ0dYWj8CHShR1aiRj1nvuWtQbSEw9gvbBO4DJMpVBKgY_FaZPL5kiVFuLqOhLB1iNTlWifHpo8c_uv8gDzodcOnx9jCwbGIsCVXxcxPMZfIEDY80adfhvOZtXYxqms1PZbYDmu90W5L6btgWcswxYJMCN2TtuQKq18jQfaIfBWynBjt12phBYg_YRma1JtVUPa5Ph_c3CmReiU_EXYXsypH3ClxSd8wmYwFdahF-W44XdKbGATG-c0xo8dmRbAx1FGIC9loZSyGqh0ajIS6NRnMhSikYCauLmwJNx5yUNHR-MxvTELo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c867b80a08.mp4?token=R7zKmr3QKS4tMhzjhzMCkQK5BAb-9O0FiznKzlaS1v44F3dex97_TjbjiJIVPF4rZr9rNC_UnUksY16TFfaYGMaU5hXCrm-9L5yaAs4TraDJ_sjrVyTYzeBX2I8qk3vlMxedDYwsoDbawTXXrbI7WYisMvQafYNxWJ0KLvh8ipn0ld0PkfI33CkG1FMl5Ln5eikEOuoCFYdglGzDx8z-2gZCjUBvy1akTVxh6Bw5WHjLQbTDLv4tTXdOUpWwfG4FjcsQGLfm6u5cCSILLkRHtIGiTnGofd4Cne991Or07lCPZL2iP8b-Y0eaT1SmgBnG0WIdE3ikt7QytZHSqmKbeW8eBJKneKaqF51Xh34nBDlnmkCl85WCehylZ0dYWj8CHShR1aiRj1nvuWtQbSEw9gvbBO4DJMpVBKgY_FaZPL5kiVFuLqOhLB1iNTlWifHpo8c_uv8gDzodcOnx9jCwbGIsCVXxcxPMZfIEDY80adfhvOZtXYxqms1PZbYDmu90W5L6btgWcswxYJMCN2TtuQKq18jQfaIfBWynBjt12phBYg_YRma1JtVUPa5Ph_c3CmReiU_EXYXsypH3ClxSd8wmYwFdahF-W44XdKbGATG-c0xo8dmRbAx1FGIC9loZSyGqh0ajIS6NRnMhSikYCauLmwJNx5yUNHR-MxvTELo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
موشک‌های‌گرانیت‌ژاکا بازیکن ۳۳ ساله سوئیسی سابق باشگاه‌های بایر لورکوزن و توپچی‌های لندن.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/persiana_Soccer/22453" target="_blank">📅 09:30 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22452">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/928b5d2877.mp4?token=lPlxgaH1DiZSOqW54a5z7uJCmSFBZdzpuKsgMDSwBBPUBmV6Wm4sqd_q-VcszHoPFRJLp2YI2MbhPwX7BpXrbRDhtyfe9JK8xmSd9UXB-fqA0UxLQt3tpBBVRpVDaiyUB6VRQc24hdx7aaor_ie-e1B8SkOsZxzjXRezkxuun-F1y0G2xltZf7a9Qgy1y0WRC4JGBOSuzWIy0dfu6nkH87ifZO2KhbSw2Gm-zaaO3begvfbRrOQzQRjbK9iqVwEA4RddrZvW2xGBg5FNngfNKvdtPtVHT8Xp8PJ8zT66pou0DQDT-46N9AMMC9J4gi827vw9_0tQtdX_vUt-7JPT9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/928b5d2877.mp4?token=lPlxgaH1DiZSOqW54a5z7uJCmSFBZdzpuKsgMDSwBBPUBmV6Wm4sqd_q-VcszHoPFRJLp2YI2MbhPwX7BpXrbRDhtyfe9JK8xmSd9UXB-fqA0UxLQt3tpBBVRpVDaiyUB6VRQc24hdx7aaor_ie-e1B8SkOsZxzjXRezkxuun-F1y0G2xltZf7a9Qgy1y0WRC4JGBOSuzWIy0dfu6nkH87ifZO2KhbSw2Gm-zaaO3begvfbRrOQzQRjbK9iqVwEA4RddrZvW2xGBg5FNngfNKvdtPtVHT8Xp8PJ8zT66pou0DQDT-46N9AMMC9J4gi827vw9_0tQtdX_vUt-7JPT9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
لوئیز انریکه‌سرمربی‌تیم PSG
: میکل آرتتا گفته قطعا آرسنال قهرمان چمپیونزلیگ میشه؟ اینا همش حرفای هیجانیه امشب‌میبینیم کی قهرمان میشه.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/persiana_Soccer/22452" target="_blank">📅 09:15 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22451">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb17964484.mp4?token=GKHkE6u1dnSyOm1rwxaG6Rvb-inqJ0K1v-YdCOMr50JMKJlnDwwUvGQ0lyACPHzH428_lJMUvWacybrzEfBWh2zIE1wHZqeLZlhKraBViagqTeWgCTNHv0VZTuM9GLjaHaNrAAOiMpsijEzSjA6YepXZ3z7HJwIQIBLFW8BSmkpYZr6iyc19T2KtTTNxCn8dTM6XbSXfIjS5eY466-mn3KpHqeLYWI1Gvuhi3c8Rl5_O6IHbZABiLd7RtfdRZdHrnj2GqKLsI45VMvV15yMte49mXX6lqdTF1TEFpRYRUdh9qCIVqwXQ7SthO1_W2PILr3c5mdSJHmDo62RtMYCa_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb17964484.mp4?token=GKHkE6u1dnSyOm1rwxaG6Rvb-inqJ0K1v-YdCOMr50JMKJlnDwwUvGQ0lyACPHzH428_lJMUvWacybrzEfBWh2zIE1wHZqeLZlhKraBViagqTeWgCTNHv0VZTuM9GLjaHaNrAAOiMpsijEzSjA6YepXZ3z7HJwIQIBLFW8BSmkpYZr6iyc19T2KtTTNxCn8dTM6XbSXfIjS5eY466-mn3KpHqeLYWI1Gvuhi3c8Rl5_O6IHbZABiLd7RtfdRZdHrnj2GqKLsI45VMvV15yMte49mXX6lqdTF1TEFpRYRUdh9qCIVqwXQ7SthO1_W2PILr3c5mdSJHmDo62RtMYCa_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
وضعیت خوان لاپورتا مدیرعامل باشگاه بارسلونا در روزهای اخیر بعد از پیدا کردن نفت زیر نیوکمپ
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/persiana_Soccer/22451" target="_blank">📅 09:04 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22450">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IUHjtRmdDxaeRLsdSuUvAJkr7LdVufeqdMTRVGcX-I98VgUyOZBm_BKuQvFzwxW4yhaoVswew7aYKY-8qQtWY-b2HO66PtlZ9rTwP_12kjsJlbOWnd3I0fZCxQtatM6WRn-KnuXoGWTYmShXO6lcqe7NxZGz9f_x4C2Nqk7J1OJlo4BicB157KmyYezd4t1VvnsTxjZAIliFYCFhqK3T1HmcEfg9O7TZ2cp6tFF-wxWnNH59nYld7GDHlweAh7V2uTaIWzrpRqd8Y8qeiwOOFE3awzLumEzeCyxaewrMtwdPcKqAo7HLKewnpB9Ahtfjc1ld2JxMJVfq76CN5dgoWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق‌شنیده‌های‌پرشیانا؛موسی‌جنپو وینگرمالیایی استقلال درتلاش‌است که توافقی قراردادش رو با این باشگاه فسخ کنه و از جمع آبی پوشان جدا شه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/persiana_Soccer/22450" target="_blank">📅 01:45 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22448">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VQvjSIZWIqaAHUgfJVWwrknRKi6kfeNn2unw7oKaCsLOEIVmvBg35BtzWkLUd7KAI08C5GixE__JX5J0y2TKmNVSNDkaF0CcR4fuKBpHdF-XgBqYwYEIrGspOewYuFRGCEKZ_V5GpSMK0eLP_eosYh-EukyoEN0SvhOAk-t1s93L-6FqMUOeTY-EezxAjckJBAfeeaaEl9PUe2kmzilNBC9kzAvL-DzHjRjgB7dNgTzW5EEKj1KH4w23NWqZbfSGiQWWp6f381kgrBY6oPqrF8OujdOZDrbgm10Ot7RLyHCdu5VvdcjyP19JvnQuDWGOr_-STsmp-KV5gtzDk0LAZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه تنها بازی مهم امروز؛
پایان فصل باشگاهی 2025/26 با فینال حساس لیگ قهرمانان اروپا
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/persiana_Soccer/22448" target="_blank">📅 01:27 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22447">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fT8i0LvM6oxTUK69v0hxt7y4Ve_PUyKwxEh6iEE8Ny6_dIraEsKmZTdx_cb91oahPMsi9HYFEtntY-MB7cDWm4dBwkXmrQZFusTzhwGH39Y8-JQ-VRCi2EHQQ_BUMnc7NR060c8TQ2cX9v8fvo4pn8wvWX_C9Ho3Y45rajBbfEX_7h9IuUDmD-V2ChNmWAhc6MqN7Wgdk05DF_qgJqEp1fAu6l8A8ooQD3ESBOicZg6VDQxdMBwWt1u6S2N14g6JhCzGRXpDZSXwWBbhaZA8jHc_-gB9V22ZyzSCU2ybd-AJ9FAyCwEROVndIitwtpY-5bkA3tnOSt41dzSJ7Ug_gA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج کامل دیدارهای دیروز؛
برد تیم‌های آسیایی در فاصله کمتر از دو هفته مانده به جام جهانی
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/persiana_Soccer/22447" target="_blank">📅 01:26 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22446">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s5OP4tVdYlC8tDrTZwFWAcKNk_sIVaGLxaatVn3pYJJScLIC7GLOJHX7hffOnB-jz9WItCzDboK7avhxxIEPh0YREGu3P5IRF5GdOsXD4u9-I0g_bBJDk03b-h48SRfnakpKI27BspdQID-DR-6b1d7pLcMZDjFB82kBwTcfWZamnImnQe6IsO8Xv4pzUiSXgLEpHWnTPtDDjfwQ_DgofOCs3jMfR08fQuPVlS_OkTFEt-pUdn_ooOtMGZXtooh11UdLCvOEa2noy0Xk6mqESVZhTCb5aYitlvVP3MMhjU5syojOIgQpbd9Vvkd_MQVZMjwjeoNrKIpn-DFim6cvmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
فواید پیاده روی رو ببینید؛
گشاد بازی رو کنار بزارید؛ فقط یه‌ساعت پیاده روی عادی میتونه بیشتر ازاون چیزیکه فکرش رو میکنی بدنت رو تغییر بده.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/persiana_Soccer/22446" target="_blank">📅 01:06 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22445">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VrJL369KfBtRJC6N-HcQayKb3ZIdWP5ujnvflkU6Qkk3BUCnJK1vRyEV42r1ga99zms0VTpIudAPubuCNURa0W6oL6tEah_Lc5ThudIKZWBMcKlLWY6VaEkIk0p_7x3JfE3D1g_-E5u8ji5Z-7D8Wdx3Xa3-uFJjISp6hds5TSVcu0LWUz5sdXxU9shoQ-X855pto8iLNHO2ymnM8boLgVjqr-t_jUs9s4lRTT-kJQNRPiFal3NKEqh2krRl-7jH_ihFamZjztHwj3PeNcxnfiOJIBthi9uhmTQPHJx9BIRl_Kf42JpYGZDZDi5YpegTnoZ_skjdhzer_x0S66ZAaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بازی‌فوق‌العاده‌حساس‌وتماشایی فرداشب آرسنال - پاری‌سن ژرمن رو در آپارات اسپرت ببینید. عادل خان هم بازی رو گزارش میکنه. از صداوسیما هم یکی دو دیقه جلو تره. کلا سعی کنید هیچی از این سازمان مزخرف نبینید. لینکشو فرداشب براتون میزارم.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/persiana_Soccer/22445" target="_blank">📅 01:05 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22443">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mPKpfBMwM8EHCkmm15eOsOsDamnMjbZs79Rbo38zjdwH0vMsV0fZGyjEm6Tp5twGA4hwTkxYprVz-X2Bbth4qAv-WrkP3vKKKEKC2_aRzV7rriIKT_XGNRlUZKbgd54NtJpu9tXasE7foIVHIHydzZkeUso8LxZEFK8nagA9zvuC_yGt9HkT8tOLq1YxhrmPjv3UfLBXRwt6U_XEC-QWgUkOkZQ0wnyyzcqZ7687xRO_ei4yFNkKInYZi419fduBPSnZiMe4jrW4C36ufHPYMgvofB9b9PS9sjozDzJklTuKAa6JK2-U4lvSy4belpokRldyp-I7PKYvUSEUZJgNgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رومانو: آنتونیو رودیگر مدافع میانی رئال مادرید قرار داد خود را یک‌فصل دیگر با این تیم تمدید کرد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/persiana_Soccer/22443" target="_blank">📅 00:49 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22441">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tv8yXZa-cnUJ5VCQCac8NyzC_ltixjsM5udHAHUaw2onKRE3GqZZP8zjKtFVeqsgJ2xvdqBuY-mKbLBT2xhOOV_IC4fct1zy62gRxqgEfKY3sVzw9aQBP0RsOIzkhFR8VtfHa0pYN8H-jbDxdf1WV3kZ_lNR6k2_DZO7fGovfPl-EK7xr1AfU9knj10Ya905VuUPUCzAoUvyGtyukpUo9xEcnDAHq72SBVUCADSjDwsHMQWjaw7req6sM_V2DH-EZ9jSHHBi9HM0IgEtE75o1dt9XWcKpz4jH_bbMRfz3amyXs15FMeRolSreXYzVrP7RsLOka2ddpch5JYmbGZRjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IeBS9Elq-n9W8ZIF2Vlox79oMKyRbOnxenOY7_HfKMPtYh8EaUnJd4_AO2hWq56tv7QyR0PShMjkX0mNH85SF25ZrDjNNQqg_oobhRxfQ18FLUrc7Bu_aQVWvI_FsHOAA_nQVDyUHB8HAWi8zCgGafoVUEank08gZhPpA__Q_8MvZQkWlr2PbnMv_Fj879P53AhpwEqXNgQdTD8cpE18Y8T74Xjulj59eMI2swSPwMbRw-Z2ngnNClOknBRqDQtb1xEeO4KWx_ADBUhrbDK74SyLeYlW1ryXUsTgeCQ778P2hr5hX-4Aq3TaclNKyVe37aD4i8JotcxrNd341-EjkQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">▶️
هایلایتی‌از عملکرداستثنایی آنتونی گوردون فوق ستاره جدید بارسلونا در فصل گذشته رقابت ها.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/persiana_Soccer/22441" target="_blank">📅 00:38 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22440">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i_47S22ivjA2MFvy2Fvav3kHc1SscwJSu3ioenuSrTf2RlUyrLu7wyCki1jbwoVd_AI8Xg1VxBBQjIkPYaMxx0HCYC_zMNcYFJV-Yo5LHKKAcTeV6-g7W5_NCPwJg15JX8n3Z_8kCuTsvRcE-J4aKlEqKgUzEj-BtBG9Rtu_cS76Ygscon-FXvBsp08RhkraG0xLS6Q3if9uDNXhfw33A4hFaId_xBNAivaqwmd83n1N4reNoqlwdrRkYzKIohf3BKhMBE32FtR-LTWb2BaPf7nl6Kdzo33bzh9vFDDe_IFDTn2NerARWC5vz-Blw8pyf_Pdr4jOKTNfgCdlP1O-UQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ریکاردو ساپینتو سرمربی‌سابق‌استقلال‌که در روز های اخیر با عقد قراردادی به پافوس قبرس پیوست با این باشگاه قهرمان‌جام‌حدفی شد. از معروف ترین بازیکنان این تیم میتوان به داوید لوئیز مدافع سابق چلسی و آرسنال با اون موهای خوشکلش یاد کرد.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/persiana_Soccer/22440" target="_blank">📅 00:33 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22439">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EdD0mYDYuEiwh2Wgamb3fbC_4r1KaNoMaWvy3Eq43gg2RTUfqQs6H6ngTlSVuAw_A3ENmVp5ZEwivfpSNOPQtzmLGvlWNZOMJ7xczp0nQSX-L40w5DbaW-vK4tXZ5Xejw5qbUp7kTQZktbLH3aua2wNj1HwGSLfaXUksGZZggeo3xMFKSsWd2vMs8URqChSETSDLXYZUVAz5chpPbCam4PQtJuRbXgCOyBFZDZzwVX3YB2Tch7j3LbcOieEpMU7pXvYB_S24VaeQPxZFR3uec8B3wOwV-AUUOBUL7HfWg9bWCSqVaADOLWKd7qzwFS0jK8LfJ9zrpRSyxfTdY5Gjng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
کدبیس سه‌شبکه‌جذاب ماهواره‌ یاهست که بعد بالااومدن نیاز به‌واردکردن‌کدبیس دارند. اولش دکمه F1 میزنید بعدپشت‌بندش‌سه تا 3 بعدش یه صفحه میاد که باید کدبیس رو وارد کنی:  کدبیس شبکه جام جهانی HD:  BISS:2585AB552585CD77  کدبیس شبکه ورزش تاجیک HD: BISS:03A01BBE20C16D4E…</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/persiana_Soccer/22439" target="_blank">📅 21:24 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22438">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BGfGrm7CBdgcN9pEm-NqQSIMHNqkjbSvMW4i8FTkcohKYl_kq38CinA0BLgrtwzHwLkwrX2vEE0B4F9RUp232JPVjEEpj-gy_McjAU24OBimnJSZYkk7QL7aAl8AF7HBhvNJZvfwptih08c4j85sSbjjHrMQvz6MM9vSrIsnp92rSl9-ucA0PW7uCZEnhmMcRYe2HXYiMjeNxJ6G6_d6x-1QHFfJoNPcVA6XUe7aI7c-BwAFZtXCuO_apaCfXSmtIqzTqAXO9Qt6B2rKnXlLVVGUZYtHJOb9Miw1Z8mILz2vqxMuQpla8RDOPDmP3whjtPNabhpJn_5FjMNYorGo6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق‌شنیده‌های‌رسانه‌پرشیانا از نزدیکان مارکو باکیچ؛ ستاره‌مونته‌نگرویی پرسپولیس از دو باشگاه اماراتی و قطری برای فصل آتی آفر دریافت کرده و درصورتیکه سرخ‌ها تمایلی برای تمدید قرارداد این بازیکن‌نداشته‌باشند او از این تیم جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/persiana_Soccer/22438" target="_blank">📅 21:19 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22437">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">✅
تیم‌امیرقلعه‌نویی مقابل تیم دوم و ناقص گامبیا که در رتبه 116 ام جهان قرار داره سه - یک بازی رو برد.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/persiana_Soccer/22437" target="_blank">📅 20:59 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22436">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J55LoRwrcTTiBkYyxt_TzaYrDyJTkDQ2bLxCMyj1R9aBmJU9bSMma-s2HIYlul7v3n3dQEn1WVTjp0AiZ-RKT884RUeb_7WQHKRiLpzJZTi8wdDMgV3VOAPmp0CvXB28ff8_WWaHewHWGVfagqeok-chXqJEtDdBl9wzIigl9j_pnzQ4BcNrJzspWM0n7TW5FDO1bz9E1Sr4ggQ7sxxVIPU6EehMAFTV3mA91jAv7I9GxV82n3IkNsEJ8tf_l0JYzJfGsbZttLwB5BEF1SAVY4rpS9TdpGKdiW827-5naL1k7yvC06Lz5UzqRojUXjU8R82H4a08Y2gq28-kK4d3Dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#نقل‌وانتقالات|سران باشگاه منچستریونایتد به درخواست مایکل کریک سرمربی جوان خود با ارائه پیشنهادی 100 میلیون یورویی بدنبال جذب فرمین لوپز ستاره اسپانیایی باشگاه بارسلوناست.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/persiana_Soccer/22436" target="_blank">📅 20:55 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22435">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🏆
کار گرافیکی تماشایی از قهرمانان جام‌ جهانی
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/persiana_Soccer/22435" target="_blank">📅 20:55 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22432">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tGK_QpX6hNuweGzP0QZYQRRhsv77RTLRHVLOxrtw6h7YWGSt-09g4XFd4ZnWyF8rVVzxZOY6lWcGHfKVAHfnJLhM6wJoV8QfhUndX0T3NC0nmbMOCIOh2KOJTarXp8CGuhu9YCVyvpD9xZrxnr1ldiK9qyC5X2va6CENizmB6Evs72OyqlHyKHmyJQbPkvU8OcT2VfN297dOHDITtTe5OgIjmEvwsyWLlMsPv0OSLHOYEClUq73qratr6VS_ZOQ8iReq6qr6nyeu-s8Ti6wBixikHp7cQzXmNn_5gFIokTJZgTtUCN_fBLu70wUNAA9sr41pdQ2-bKjtRtrfID7KgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇪🇸
🇪🇸
بیانیه عجیب اتلتیکو علیه بارسا: «هیر وی گو! ما یک فکس به همراه پیشنهاد خود به بارسلونا ارسال کرده‌ایم: ۴ بلیط برای کنسرت فردای گروه «بد بانی»، اشتراک سالانه ABC و یک کیسه تخمه آفتابگردان. مشتاقانه منتظر پاسخ هستیم تا «اعلامیه رسمی» را آماده کنیم.
⚪️
…</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/persiana_Soccer/22432" target="_blank">📅 19:36 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22431">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/caAL9zliQtFx-eel6qh-S3cgDbDXXY2PnJJ2yEwX7anmuHsOHkg-fk8ahzJPd6k9EvsCPqByjpHEKe99WkUZJsb2hIqvrcSTj2AsaPoILY77X6jlo9MKnnrU638vH2YiZkVl9z4OxUxJtvj4NBIp4SX0O5NDgcEFb97jNWqjXZsqbgdrJUxNJGaOZg2itc7Jg4jj6yfViv5VBD5LMQf-GP7RviZDRw1Eq_5Yz-jlXGDSt_7wnrOeUQRM2rnCPkBSKGDeyIPNBdk_HUG_JLIrOhVEZXJ0qAaY1jgso_7toCt3h-BwiCE7WbosTTUHsEitEbQ0Yxz5MQXoJX0RcKZjNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇪🇸
🇪🇸
بیانیه عجیب اتلتیکو علیه بارسا:
«هیر وی گو! ما یک فکس به همراه پیشنهاد خود به بارسلونا ارسال کرده‌ایم: ۴ بلیط برای کنسرت فردای گروه «بد بانی»، اشتراک سالانه ABC و یک کیسه تخمه آفتابگردان. مشتاقانه منتظر پاسخ هستیم تا «اعلامیه رسمی» را آماده کنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/persiana_Soccer/22431" target="_blank">📅 19:26 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22430">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e4a_zH-COacoiqe0ZFwuwix4OD_O-q3_64DaLox-Ozxo8JM2ZTKV1N8iJ-DXNpPSBa4KdS-qwTW7tTR4C_UlDyZqPqDE9I65aczUqJQVTkogL3MRYB2rDdHIiIRjL2YvE3BeKu9P5BB9es4YmJzwMAbwCIyfTtz2r5Gv0_AeUaIbykKpkQJE8dEd9rKSZ5lHh0fwTZ7xix_8AUqu4H5RbjZ4HJQDL8kXey3gWnKx2Xv6dS8D38FJe1_flHqGnADC1cl4fsVxR2oF1sAYZH2JbijXND2EY9sBwpZGdsez8fLXCtjDnnAO-BSn79Itli2V-s9CF-LMgEdtFND1WjAs1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق‌اخرین‌اخبار منتشر شده؛ باشگاه بارسا طی ساعات آینده پیشنهاد برگ ریزون 135 میلیون یورو برای جذب خولیان آلوارز به اتلتیکو ارائه خواهد کرد و این بار این باشگاه با این آفر موافقت خواهد کرد و این انتقال رسما انجام خواهد شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/persiana_Soccer/22430" target="_blank">📅 19:12 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22429">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G-5Ah_OyNXGh4pyc09EwzJMCrqgv2gJ6grjB9xhB5kkmiD13YemgYDlBsm-GiBGmIW2ib-2e8eVhvsKGh4guk2d8i-4gQSJfIxX7I2ZErmiDx8oBLiNTkHwnxiYfY__lIenq8DL0j3MrPIBf1oTJRAjB2tnlfRaTVNESrimQjrsRrlqSxLisOE8FeJcWMCqjQOhNts_OaM7AxCe0dU-MYEBeXMlSFUMtqHCvzdLAtoFuKNo4MxkShIOOh1R0O0CaGuEYtlf645qIc3kN8qtC3BDm78eDt5hOcLzvkwvCLYBdQjOXeFCNP3WU0DnN01Etu-8l-ETa-eeiCffkj2y-Iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
با اعلام ایجنت رامین رضاییان؛ ستاره ملی پوش استقلال که نیم‌فصل دوم به فولاد پیوسته بود برای فصل اینده به جمع آبی‌ها باز خواهد گشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/persiana_Soccer/22429" target="_blank">📅 17:25 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22428">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e99804290.mp4?token=qAWaFx1-8LKmkelJHbVJKnybWsXGuXTwnP1Kpa-E8f45QsvzAiNsDbyVkSB8EMraxOyZIsZKLtCyAfzcVx5PaaMo4UEpCvlnlJN5NBnfQewrUO6teT4ax6hk0D7WcFLezjGKhUh5GMuEga8QgUtWnpARurWwNfdc8XA3pKEIXJ7cUVhALkyLJrq8E108V3yxAUOMzo4qrxFHfaoIY0e9HL8HtalMkhOgDb8L-9JGaVe25jzLMB_FPJjCXTiB5-eYIzMsYXcA1PBoiAtXLXDxIQR3GvinF6mHIKDwFsZXV_qKCHuYYc18Z7oe4S1Na8Dwa2ccsSOVJihK1Coj12EjIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e99804290.mp4?token=qAWaFx1-8LKmkelJHbVJKnybWsXGuXTwnP1Kpa-E8f45QsvzAiNsDbyVkSB8EMraxOyZIsZKLtCyAfzcVx5PaaMo4UEpCvlnlJN5NBnfQewrUO6teT4ax6hk0D7WcFLezjGKhUh5GMuEga8QgUtWnpARurWwNfdc8XA3pKEIXJ7cUVhALkyLJrq8E108V3yxAUOMzo4qrxFHfaoIY0e9HL8HtalMkhOgDb8L-9JGaVe25jzLMB_FPJjCXTiB5-eYIzMsYXcA1PBoiAtXLXDxIQR3GvinF6mHIKDwFsZXV_qKCHuYYc18Z7oe4S1Na8Dwa2ccsSOVJihK1Coj12EjIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
گل‌تماشایی هریسون رید بازیکن‌فولام به لیورپول به‌ عنوان بهترین گل فصل لیگ جزیره انتخاب شد.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/persiana_Soccer/22428" target="_blank">📅 16:46 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22427">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HEZo9PHlWohEYpSK7Wnprllzl4p9ZmeYXQsQ39Zk03wGkTOan8GmrPiQPYONfcrwpB4aNYDZ3c7VsCH2UggZ0y1R96uRlg-ireRiBqrUVM6PbqfDlmA0DNf-EEVIxu2orqtP22AmCzq5ISzSLDfinvpUPC9T4Rdk9j2eKZ3PybPUJGT78-fQrnSWSJz6HT7WLmmu1HqLOlsamslcTZgIuqCy1wn4odcJ599YoFzAtXDdeOUqVFa9aZE7LRr1WPjm56S7Gu4fAfsRJXKpfZMrtxxZgyM3x9ia-R0Ysf69IiXJrieW6wSAx8-O15je90k1zylEq4ZzUkB439XokBOewQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ خولیان آلوارز به‌مدیران اتلتیکو اعلام کرده با بارسا به توافق رسیده و دیگر انگیزه‌ای برای ماندن در این تیم نداره. اتلتیکو حدود 150 میلیون یورو برای فروش این بازیکن از بارسا میخواهد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/persiana_Soccer/22427" target="_blank">📅 16:19 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22426">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SxO9g1lQnI_ZhnhZvDAHTY84wm_hhd4A2M5Ky5zYGsDS96ESo4kdM5uz2006svz2g-fAjOSR-cjPbx5qeMbD61l9gmC8ToI6RyXWR1Lc7n5VCBFkpTKbPmcAOa3uJdnTZ75yJxHhUTb7_7oe5VZTGCm53n_ZpSh0zZGeQbT52lwW5WxnjvRrzcTacppNUZjkHbUo4--e4YE4HQJ9xZm6W1vwvJxhFLQDZoPldLJx02YAYXHTfreQOri7digZSznw_piCaFCoN1hhOM3tW1TCrk2TAgDvNaCTvDdBuBYJB9SonO_AXMqJRw3pyKCkdbgTP1cXqYphf0ahv_Cw1x7T0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رسانه پرتغالی آبولا هم مدعی شده که باشگاه بارسا در حال نهایی کردن عقد قرارداد دو ساله با برنارد سیلوا با دستمزد سالانه 8 میلیون یوروعه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/persiana_Soccer/22426" target="_blank">📅 16:05 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22425">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ccdf1c58d.mp4?token=val2WYYT8YHlfpAOdektWisrGqV7G3xpx4SC2-focOBmoaxjT6ibUnO527-yJimexOgfdLgldEKAF63ZKSO1Rj_kKAVbDa_jZE7f2ISj9iCj37E0SzQosBpJE5ni_qOXWCN4yFWQwhsf5kkOLOzMZoSM9DZzGPQFibpI6OsPCLY-Gsbs-a-JDc_j3Z6DLEqKuVfT5jRAyYz5-6RGHf18EeZbmOuhOeIBuSrQpDp-p8uRet7rAhPnQEwyy6FTsSG3Yw-7ZWhhl-2m6Jxyj8nGuIGsX72Xz3rz9i49B4nQeceFf_2MuE7muyIRgd0PznmOgH31mbVnScSJB5yAFbkjVIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ccdf1c58d.mp4?token=val2WYYT8YHlfpAOdektWisrGqV7G3xpx4SC2-focOBmoaxjT6ibUnO527-yJimexOgfdLgldEKAF63ZKSO1Rj_kKAVbDa_jZE7f2ISj9iCj37E0SzQosBpJE5ni_qOXWCN4yFWQwhsf5kkOLOzMZoSM9DZzGPQFibpI6OsPCLY-Gsbs-a-JDc_j3Z6DLEqKuVfT5jRAyYz5-6RGHf18EeZbmOuhOeIBuSrQpDp-p8uRet7rAhPnQEwyy6FTsSG3Yw-7ZWhhl-2m6Jxyj8nGuIGsX72Xz3rz9i49B4nQeceFf_2MuE7muyIRgd0PznmOgH31mbVnScSJB5yAFbkjVIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
ویدیویی‌که‌باشگاه ماخاچ قلعه روسیه از عملکرد درخشان محمد جواد حسین نژاد ستاره ایرانی خود منتشر کرد. حسین نژاد تنها یک فصل از قراردادش با این باشگاه روسی باقی مانده. درصورت باز شدن پنجره آبی‌ها مدیران این باشگاه تهرانی برای جذب قطعی این‌فوق ستاره 23 ساله اقدام خواهندکرد.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/persiana_Soccer/22425" target="_blank">📅 15:54 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22424">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LyDz4a_blJf8056O7klmlTo6gT_HT4SOTskCXJOuRW3rJOINs0r6oYk_PMgtYzDOTj9bUOF7C8_Ikwzr5yzRMbLZZLlC0dCNLcrMfdojs_PU4zRWG6ptlnVzq4u8P9Uek3dPU7h-mAd621GIr0jKdZ9K-rMlRY4fE33TViiBrpUkKCTIJs3pZNz3p-uubKVw5Pf5cxVt4T8bN4VgnBxwWNDUk2-9EmouaucRh3qNacqB_8ID1bOU2oEfDMTsBxoF7TNwiVKS9AqYSFJe0pQCgCdnMc4SF562F0xYsGkpkeFAAFQNVwhBPUJhePnmXK0q0V4A6478lPNrwuUsmffsZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#نقل‌وانتقالات؛ رسانه مارکا: رودری ستاره اسپانیایی منچسترسیتی میخواد از جمع سیتیزن ها جدا شه و باقراردادی 4 ساله راهی رئال مادرید شه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/persiana_Soccer/22424" target="_blank">📅 14:57 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22423">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q8HgQXXMi0u_CNxuI29JMvjOfA8TLuueiGh3g9NV9iJOSZWpXFbs1MOwWnnPUKUjmVcycffKYhmPrl3eXTNWQ1SzOnof8RR0cYu3U8mICei4Cz2-RpENrq92y_ocX3ipZ1lrxrfTHrKmry8CP6Z1866j8bn-c8RB9ORqZ2MIkHb-eqP431IfJ0G2buO_TrGsgJt_1cuXM9k2RVL6eF7qIPwkKeANverVSg_tJPQbrtojqLMkkenGa7Oc-qutZftGzTIgEXKgrl_OQCPL_L0YFg7QDv6KLjQc7qHyBgzIbW7ZbFM2pAJx_uzaQZ9LRddVfGQKEMDz3kw7vgHui_oC_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
جرارد رومرو: یوشکو گواردیول مدافع سیتی نیز همچون خولیان آلوارز در خواست جدایی از منچستر سیتی کرده. فلیک عملا با تماس هاش داره راه انتقال ستاره‌های مدنظر خود به نیوکمپ رو هموار میکنه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/persiana_Soccer/22423" target="_blank">📅 14:07 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22422">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DbDWfyqxwdvC_Rw8dVj2TbWF98Rj0tE8q7-ggKLC2at_fEwVMNm3MDzYdqzSB-7R_H59whwl6waHhZwDV2hbFjLM0DWdidzSdpqOynCxNTtS9ZFE7euuQ_YzredTG0JpwzPC9nEHCCUj7R5OGHhZppiKtlF3uqniATf9ykJu9OJ6QmaEFQXCUbfqcneO3n0_VFywN3j9Qgnw0waeMZ1VwN1cDIOofRx83xP9BLPk_BFNAjIPg7c6Vq5hcj-3mf_xRW8M4gIiFtQrr-y_g3xiOFkuz6B9TyuOxt6f4Bvg-a6YXFv8CHwr-Y0uHXH-Y_sG8U-XypC1rRwkABeAYAJW1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#نقل‌انتقالات|ادعای‌رسانه‌های‌انگلیسی: یوشکو گواردیول مدافع 24 ساله منچستر سیتی هدف بعدی سران بارسا بعدِ نهایی کردن قرارداد خولیات آلوارزه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/persiana_Soccer/22422" target="_blank">📅 13:55 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22421">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BLcNwJPNrYf24HU1nfcJkE1E0ZbOvy6hVnU9wYapQwMBKXsh_QQx-x9t8tzzFvi_gw8Djv2hICicdYPHImcuPHn5qTIPVbvnyTZ4ZPTrNf4cF9XtuYJgnD15YggysO0OPPCqCCT7uX7VAnAT611WCIOI9wqtGEW7qxhUoEy9r_2Bkl_d70HiOt7JcVu-Fy-ZvUHrg_7Tq4sQbi43mbd2bnP5GaOOOii7ezpSgYMcaPVivbRMor_sFoA-NYi5HfQHo4TNERP5PIuSA0nG5V2qrRUs2wTg92yhuiDdorPDHNglaMl13Sh9yWNcngECsId1FYFCsJ-e2xuQr03e5jwpGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#نقل‌وانتقالات؛ رسانه مارکا: رودری ستاره اسپانیایی منچسترسیتی میخواد از جمع سیتیزن ها جدا شه و باقراردادی 4 ساله راهی رئال مادرید شه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/persiana_Soccer/22421" target="_blank">📅 13:06 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22420">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EC-sK48RIA1wVDT698DkbnEblomZDvDezSORWnQ1fPFOofhkFNAtHksoZ6fxxvg5MQc3qoalf0vZY0rOuFea_NDdxpgXHcgZBiDVcvgui5hopSR97Tc1aG5alP8an347xyxiWfp49CJloM5wyfbQ3JcrtV-kkRWoE_S5tI7CN9cUaMJ0lvp4SrET4TnixuW7W9zXhuqGbDM7aTjavEEjClAAMrKMY7Lt4FW6X0_1vGkidQ9x4hSzKPDrFraQOARmiTGD-YszXuH_d7oXiF9S20D7Oa32R-QMo8-dj1XiGkFvAPk0Z_9i9XLSUNoMCcRrgvrBBakmkZ6o6UCDxpkIRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد... یاسر آسانی ستاره آلبانیایی استقلال امروز در تماس با علی تاجرنیا اعلام کرده که فصل آینده رقابت ها نیز در تیم استقلال خواهد بود.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/persiana_Soccer/22420" target="_blank">📅 12:37 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22419">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FHwYoQZAd3Tx7xuNAYsxncaKWCueMyNuhPp-weRmbAxu1TvqeldxAx2LEh-g0E6xPaENB_gxT3KEPw0H3cCIMOpwoj1XopTiknnqUWiSMElNwlxvo_E_IzNyWFOgbmMWtjznwGDrNUjWS7z5JBmDgVBHxjbtSQv6saECi5QgSmnAPxK5NSbC93pnFgqDzM8TOwXGudJo2uLN8kXIUuPtkeyhPQj18Co7yn5Xi5O1viZ2pyod80jRrABMTUheewjNu2hBeyB_qpDmrqUgNRXq6EHHriOdmTtpoVYis_Cd1Eu9iRUtZcBufSIySTxPYH6Sbz56ID5AEFoiEgKSVF7n4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ خولیان آلوارز به‌مدیران اتلتیکو اعلام کرده با بارسا به توافق رسیده و دیگر انگیزه‌ای برای ماندن در این تیم نداره. اتلتیکو حدود 150 میلیون یورو برای فروش این بازیکن از بارسا میخواهد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/persiana_Soccer/22419" target="_blank">📅 12:26 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22418">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F5CnUN5yWTjTjOpsEbDgqqOfRG-SwHPf7YJyyrMDZMQ5l9T2q3d0D6wIMdjK-MlcqeqvrtF96mfsYwub-sJfFSqvMPMjEzl8uTBTHZGaSlgT-nbDFlxv--LrvLL-D3C7mY4bCVcOuu71qthIOaMir0WQeZYksYCx4R-sO_YtZdEDx1QsatVRvkCDMoGnv1duClqoFqvkJYKX-FkClcJQXUm5GvFS3fRmFBoD4XKDwzR1zSFLQtqIp2VW-xKXbej1JgoZ9B53sFujPhXegI_Jx_wgQtEHzejr7U6-eifZFOl3oLGkSFRYUufC6gP-Uej6GfZvtmUqXCcA_loswxhFHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
🇪🇺
به‌مناسبت فینال لیگ‌قهرمانان اروپا نگاهی بر ۱۴ بازی گذشته PSG مقابل انگلیسی‌ها
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/persiana_Soccer/22418" target="_blank">📅 12:13 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22417">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aQl_cUil8c56_tdXsqxFmaHuNKkX4q32xhUP4DgWX2tLQtR4J0m6djZc9LxmnSaQX5_jLBEqZ5fjk4SyCah18Db--LrqsH3izuhyYSB2-ixl8eCUwq1Mrk8VdpcGjHkhjl_ezg6D3zyp6NdoSoDmAuH46qx00mqrjPuFvzYNf36ssLmfGdnLI7ZgXO1M5IEX7qjz3A4ItT9hVTF8MU4S5vZfTmdvRWS1F4S5ovaixxqdhvW0Hm6sD19gcl-UrKF_FPVObov-o8aVbcskAyTSgp4m5sXO6Z22ua1dCbZSVCsiTm5z-N9tNUs7XlgjThfkZ_6gYeqQ-Cm5QbgPCg1biA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#نقل‌وانتقالات
|کوناته مدافع‌ فرانسوی لیورپول به‌سران این‌باشگاه اعلام کرده که پس از جام‌جهانی از جمع شاگردان اسلوت جدا میشه. از رئال‌ مادرید به عنوان مقصد احتمالی این بازیکن یاد می‌شود.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/persiana_Soccer/22417" target="_blank">📅 11:38 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22416">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kmWW2sYArz1pA6cQVUIlwnGqGrXJImTCZMgKKUupXfc1whcOSx63WTwRmdID-x7FXL2SJtTuA1fcs05VzlQq5pRuft8JOb_RgP5GMStOwtWkIEJH04N0DIG19Si8GTldgUIOZV_j90mX_HX5Ih-qBR5NqQsr3AMu8Slc9GH6-1Dw2BN7Bme38LjTyAhfDtRanornt4QWj6dxL7TUpu1-focNhDqtQ89XlXMdgQjkV74WxiD0mIVvWuJqMijQcOMmsgy_cmTpkzEgktuGRAK1uaJIIxEx6G1T3oEH5NnAFU_UzsgqCoZ3XmjqGK6c-EGOJbgDkP4356d6YQLUm0Gcmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
فابریزیو رومانو: باشگاه‌بارسابعداز جذب آنتونی گوردون و خولیان الوارز باز هم خرید خواهد داشت. هانسی فلیک امروزشخصا با آلوارز تماس گرفته و به او اعلام کرده برای فصل بعد روش حساب کرده.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/persiana_Soccer/22416" target="_blank">📅 11:33 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22415">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lrOI4smjAfh7uxolaTdYMWRoP7RpirbtUlvb5tL5wmlXMk8-Z8QePSUoek9dwxR-WAQGL2975gDIAaKcuCvFoe56Fmj9Phivfffnowf87cn3hRlOicReVdmCpzpHz_uEzcsvI8E8npgEy98mu9pthOqDabK33_yAfap4SOhoaCT6uSJli1L7JOGYs-oLZnx7tF6GmtbZ4DOlJ7JcvgzeUufTRG4Rdjj53FxmPIisUbdswcvIucd4R6fpQK5FyyTiJuupDWVxgqcUwgbcDuecl-aSkbRGTwKrcV75d782TEyk7grJ-ZCCEkPHpP21CBtl1FfdBCLSJBgHi-tz47tTDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مایکل اولیسه، انزوفرناندز، ویتیتیا و ارلینگ هالند چهار هدف جذاب انریکه ریکلمه درصورت انتخاب بعنوان رئیس‌باشگاه رئال مادرید؛ انتخابات ریاست باشگاه رئال‌مادرید روزیکشنبه 17 خردادماه در تالار بسکتبال رئال‌ مادرید برگزار خواهد شد... فلورنتینو پرز و انریکه ریکلمه…</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/persiana_Soccer/22415" target="_blank">📅 11:21 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22414">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SdK4p_aQ0ORmnA7lad_W84-JRJfZ0e1YLES3Mmgj6Ue4OncdV52Q_wrA9nFqpiTTFPMnwes2Vr6jPHeg_uxmIBHnqtpxqlHyW9cnY54f0H41vzKDQPhngBX9qSaTVYdV77QsO3AUloqzbgxBxzMmVJQvsordveE3udiV3GmdYcl1d-7HawR1xeQEBp7LF2sIRSb8IANpLUd76UhMBIWFxXnA-mQ_zItqRASX3MYogsHW2NMAF3-JwUhmMmT3Sy_hTgg8UDTnNFuHxmsLa93SGMv18la5Lc946osWgJ4rVMAkpec833aqEbK-sU9cwUph8bwvKQZY_tATekWi_85Nlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه جذاب عملکرد ژاوی هرناندز و زین الدین زیدان دو اسطوره تاریخ دوتیم بارسا و رئال مادرید.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/persiana_Soccer/22414" target="_blank">📅 11:21 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22412">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NLcq6FT_ErSvrGU5M3Y43JXtUyidgzlFsJ85R7loueAE44KiYiCwH8IO7nJfsiChJ-59r-C-XiFwTTsHpEJLzfw2U8s6ZhsfzDOtz-X6OPOGEzNpgqvI9bsfD4ISZS6gIxRfa35SZvxRTyIN75-ZrKH5VPwv1gYAxfnOM9u2F6Iy1DyLEc8WRinEkwE3DY0SUXvSvqYnZK9bDZriwmwTEr7t8GZYp2j8uufbisKJ4xr4l1ZoP3x7ejLsv-_lB4F0M5c45u9TyILYtgXNVdPxb5jJ-_NY9WyYymqTcGfhcSVSnZ5ST5s6GqONIkD_tvEJw4AqxLl2Dko4nrfh7QVZEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚽️
برخی رسانه‌‌های عربستانی؛
خبر از مذاکرات مثبت الاتحادی‌ها بانماینده یورگن‌کلوپ برای پذیرفتن هدایت طلایی پوشان جده در فصل‌آینده میدهند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/persiana_Soccer/22412" target="_blank">📅 11:21 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22410">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">ضد حمله‌ و بیلد‌آپ های تیم رئال‌مادرید؛ طوری که زین‌الدین زیدان با رئال بر اروپا حکمرانی کرد
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/persiana_Soccer/22410" target="_blank">📅 10:52 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22409">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c001aed77e.mp4?token=Rf2hPrAbYd14Tkbi6zWZw0IxBxTe1-Dj_LJqcJko1gtqRKjMA8WhxnzA3TXhfGPwtGU8HLKcEanxA1wBBkzZYg3s3E6IH2icGjMrf3iybb12hoGJPNEhu_fKV2pgGtsJRssZzYVN4AuzMOynuBuPLuVW9bOwDhzRUs3uYYk5RF0eu92qfbAOnQ2Gxg4FgwbA7KfLSKrUfmMbV90mT52rcRUv1mAvRyC7U8V7bojRQWGwPbdiKziyaf9H1FACyAGCJ4IALXWbj2lQjfjFHW4RFf9axCiQIoCsyfasuimthlIspayXhXFWc96_6uQozZOy9txnU_sav6Q4IkS-eOrk357VZszfMwOdikUm7H7cIPVFfKLLQHLRSRwUOkYD_KgeyHVc5CLNxuJLbKIhf9Jn2g9embJp7TVpvH-ywExHDBfHizLrBNfpL6vwjORGYa_zVWM6i2K8leoKeNzoTvqSS_bXP0CDO-gx2lUdsKYC1r6gBPO-9arwxenZtDpGv52DMTMCwz80ZKS5C4o-Io2jAjBec2MLb6gBEePZ3L6AnCB9lIFm_Xf4nzuVA5epJ6-1-HFTFeP1rUla32qovz2rJQpM6ewxoZrD19PmbBmgeJW1MN2jXps9ZzuBjzJqQ5jeAHvlx9etfSLbaDiQbByDKxh-9DFTaiUzquu09OKQGr0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c001aed77e.mp4?token=Rf2hPrAbYd14Tkbi6zWZw0IxBxTe1-Dj_LJqcJko1gtqRKjMA8WhxnzA3TXhfGPwtGU8HLKcEanxA1wBBkzZYg3s3E6IH2icGjMrf3iybb12hoGJPNEhu_fKV2pgGtsJRssZzYVN4AuzMOynuBuPLuVW9bOwDhzRUs3uYYk5RF0eu92qfbAOnQ2Gxg4FgwbA7KfLSKrUfmMbV90mT52rcRUv1mAvRyC7U8V7bojRQWGwPbdiKziyaf9H1FACyAGCJ4IALXWbj2lQjfjFHW4RFf9axCiQIoCsyfasuimthlIspayXhXFWc96_6uQozZOy9txnU_sav6Q4IkS-eOrk357VZszfMwOdikUm7H7cIPVFfKLLQHLRSRwUOkYD_KgeyHVc5CLNxuJLbKIhf9Jn2g9embJp7TVpvH-ywExHDBfHizLrBNfpL6vwjORGYa_zVWM6i2K8leoKeNzoTvqSS_bXP0CDO-gx2lUdsKYC1r6gBPO-9arwxenZtDpGv52DMTMCwz80ZKS5C4o-Io2jAjBec2MLb6gBEePZ3L6AnCB9lIFm_Xf4nzuVA5epJ6-1-HFTFeP1rUla32qovz2rJQpM6ewxoZrD19PmbBmgeJW1MN2jXps9ZzuBjzJqQ5jeAHvlx9etfSLbaDiQbByDKxh-9DFTaiUzquu09OKQGr0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وویچک شزنی دروازه‌بان 36 ساله و لهستانی تیم بارسلونا، بعد از ۲ پاکت سیگار و مقداری آب...
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/persiana_Soccer/22409" target="_blank">📅 10:38 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22408">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3294ce3a0b.mp4?token=DoQqSV7xwrJ_frKxYBOzx0H152uVbNcVQMYKHYwS35YZIyeFAszipzaQCeUsnkmPvgsj2TlwE-JQsnQqulcfjrpvjHCw_3tiPBzrp_M12vFtW-ujv9VSHT2kumJpqEJFcKO22WF6lUBFhBoo_kr8_FfOvWaBv5aAPxp9lpYgfdAefavnoy3_SUQq_Bxsa2-5H4_m7hG4zNwRtxYuaTjVUcCyZbwsaHqvLbmc80OyZDmf0hKBqjg8Lu6RPJ0p3gPVdt7mH5vM16j3V5wlIAOcM85EOr37hoetsWsXT1mBsgajO_r1jQHeL20iX77l22MQapmsOZCwBCjiwJkMIr2EEXBQlNLjowPQlaDBUAxOjLae_321vRAVIMbqpQ_MqQFZT-5it15M6JiNbZvJKUDXp7Ezfar_Sb_iy70Z0J9wFcyGzi4snW7-AcCty7iakmfARQRVITg1iuFRFpFmCiw6hBnZvGCOGzcJiYLMdgBoYiK_KIyvrhDaXD_-zHbw5-2ksHkaEGofRqvi1GS9pIwnvBpnw0HSo69nyAaVqCezubqT9A5Q0_SoGwl7_gDQP9EzgijmQ2F3nTOYmUdOLdGC_b8JhaIGeHi7bjd1umDQ9YHXNbmqLBcApQ5NwwK84qBzKaJtdMDESGgSp-Hi1eKBOB_vKK3Pu97QwTVGJiBO4vk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3294ce3a0b.mp4?token=DoQqSV7xwrJ_frKxYBOzx0H152uVbNcVQMYKHYwS35YZIyeFAszipzaQCeUsnkmPvgsj2TlwE-JQsnQqulcfjrpvjHCw_3tiPBzrp_M12vFtW-ujv9VSHT2kumJpqEJFcKO22WF6lUBFhBoo_kr8_FfOvWaBv5aAPxp9lpYgfdAefavnoy3_SUQq_Bxsa2-5H4_m7hG4zNwRtxYuaTjVUcCyZbwsaHqvLbmc80OyZDmf0hKBqjg8Lu6RPJ0p3gPVdt7mH5vM16j3V5wlIAOcM85EOr37hoetsWsXT1mBsgajO_r1jQHeL20iX77l22MQapmsOZCwBCjiwJkMIr2EEXBQlNLjowPQlaDBUAxOjLae_321vRAVIMbqpQ_MqQFZT-5it15M6JiNbZvJKUDXp7Ezfar_Sb_iy70Z0J9wFcyGzi4snW7-AcCty7iakmfARQRVITg1iuFRFpFmCiw6hBnZvGCOGzcJiYLMdgBoYiK_KIyvrhDaXD_-zHbw5-2ksHkaEGofRqvi1GS9pIwnvBpnw0HSo69nyAaVqCezubqT9A5Q0_SoGwl7_gDQP9EzgijmQ2F3nTOYmUdOLdGC_b8JhaIGeHi7bjd1umDQ9YHXNbmqLBcApQ5NwwK84qBzKaJtdMDESGgSp-Hi1eKBOB_vKK3Pu97QwTVGJiBO4vk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
یکی از مهم ترین دلایل‌موفقیت انریکه و PSG
: اون برای بازیکن‌هاش‌بجای یک پاداش بزرگ در پایان بازی، پاداش‌روبه‌بخش‌های کوچک تقسیم کرده: مثلا هر پرس = هر موفقیت = یک پاداش عصبی کوچک (دوپامین). نتیجه: انگیزه پایدار در طول بازی.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/persiana_Soccer/22408" target="_blank">📅 09:50 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22407">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc6b58323b.mp4?token=SViOnLCbXODLliDjD_gqjowxoOK-XRUAOkaruNxQNt3wpOfnsEiH3Ou46GnMUqkRhfVzCS6Bk0zumu_WcRzRR60KkfBeWWGnORHP4blUeEc9SyKMYaLCpOLDxW9ghIcA2P4pWavqq3mJaOk1FlVWkRmpK1EWAtbm9-TjMlyWoNpeqyyCI4r4GOAaxX9KvCpPh8XsMkJu6hNb3BM2Pn4gePNJVAoVkTu1O7GLw5Y4SE133BNmfVFFbOe-R2V34Va9uspljqWZImdUGly65Jfs1WK89P-F0r98kSF7P9x9sOi5JYL1L722ufdydZZG20Weuk-GWpiml13vGdY2lUsG1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc6b58323b.mp4?token=SViOnLCbXODLliDjD_gqjowxoOK-XRUAOkaruNxQNt3wpOfnsEiH3Ou46GnMUqkRhfVzCS6Bk0zumu_WcRzRR60KkfBeWWGnORHP4blUeEc9SyKMYaLCpOLDxW9ghIcA2P4pWavqq3mJaOk1FlVWkRmpK1EWAtbm9-TjMlyWoNpeqyyCI4r4GOAaxX9KvCpPh8XsMkJu6hNb3BM2Pn4gePNJVAoVkTu1O7GLw5Y4SE133BNmfVFFbOe-R2V34Va9uspljqWZImdUGly65Jfs1WK89P-F0r98kSF7P9x9sOi5JYL1L722ufdydZZG20Weuk-GWpiml13vGdY2lUsG1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
وضعیت شنبه:
آرسنال با یک گل مقابل پاری‌ سن ژرمن پیش میفته؛ داوید رایا گلر ارسنال  دقیقه 34:
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/persiana_Soccer/22407" target="_blank">📅 09:35 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22406">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q2ozVETuLpNPBGhSAizrIMDqId8oiUOACEbVPkI-AcDljFBBd1HdsO_-DUiEbC7Q_0EJZ9mrqZxfcdWERrMJgxg8vnON72JQVRbYNOgwax6jlEiIYDXv04PIRCA0PfEeLJG3dnfNgPG4KLXp49bALSU17tp8gvtW8cZoCpR1g0Z7kypiZpAM2EXLR7wB1Z_7SyLAd4iOfLqLup4LRBukwXO1j8uYqJBe68lCLlTF-iKL_wBYLyojqN0RWS3xLotm8ZqqKALgIfw7TTxDXJvYV9aMeABB2qpI581Eo2peLfN5omgatG_kC0GWgurnVLNfASo7qYcGvM129KKv5x22yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ خولیان آلوارز به‌مدیران اتلتیکو اعلام کرده با بارسا به توافق رسیده و دیگر انگیزه‌ای برای ماندن در این تیم نداره. اتلتیکو حدود 150 میلیون یورو برای فروش این بازیکن از بارسا میخواهد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/persiana_Soccer/22406" target="_blank">📅 09:15 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22405">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vWIHDl3Sq2CcLgHPYC7gbSiY4wd7pAvmhIZ7vzFAZnnqR0QAkjqnTIW7bXkv2Wi7BqOrF-Ghrzzh8AYaoIlayUQ45N7VQTncdgTJG-9bFD_tyT7PEzCYQMyHaES6eDj1TJjzPbTVnMy_v_jTgq5QIsVVDVlBEXbQ4tSKA4FrXQczOjKhAq618160UzpNXyorOmFm_VSb_J0iA7IO-IlO70BrrEgPhH9QTQvyfSdNgQ7ctPJCET3dANRNIMK0bvsbb68ByI98GiDb3Nhdl3rOjRu_7XWfOc-e7_nrq_hJDiGXh1xNPateBF4UIQkW0buDz3J8GzAc3j2INy9Uog-T0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ویدئو آموزشی‌نحوه‌واردکردن‌فرکانس جدید بصورت دستی در رسیورماهواریاهست؛ شبکه‌های یاهست که بالا معرفی کردیم همشون تاپ ترین هستن که بازیارو باگزارش‌فارسی، کیفیت فوق العاده، بدون سانسور و تبلیغات‌آزاد دهنده و جلوترازصداوسیماپخش میکنند.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/persiana_Soccer/22405" target="_blank">📅 09:04 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22404">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ECEGR3_1qDGiHMXHEfS97CRgLgmKQP-Vs2NMFT2J6yTN88n24JoKt8ho1Oil1dgyhXadBkNzn5sV9_8yHUaPrKbyen_z76Ktk7lG6hHTRFC4qmkm0bJfViH9ySUofs_JOMTBO9ovE4dSQq7Z6KhK_40N8soYhJpGoMT9Jd-UH1KLurGzx3zHCxqNfiMNkIqkfcEpgs49Cj02sMlIcbl9wYSnpnhDotRzJHPtJh9E7ln-rqTmYu8Knpw_UoEARW8GVjd3rBfDqWYelyOjTLDj-8HIbRAACWlFeW1TtVE1vEs5RkJw5trakJt0mtOK06NdQKWPvKoTSZuelaMYodkIkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ الهیار صیادمنش مهاجم 24 ساله سابق استقلال و فعلی اوئسترلو بلژیک رسما از این باشگاه جدا شد و در حال حاضر بازیکن آزاد بشمار می‌آید.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/persiana_Soccer/22404" target="_blank">📅 03:51 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22403">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HX5O9lDb9NUB8M8_SN2U20vkMenYly4Qqyi1P9NdAd1KVjjv25CIlsK5y3Ay_Ple5JQR7b4SF1hb6QwrjI1lG9Defg4B39SyxNfTLe9VV8BkUFvrMNrIE0FoCl7NQkLi-xpwHTwnEODZrddQCkCaSbWVjKKNIvbfQvkJSalb3-JWiX3a2UsyAtI94duq6gdEEHJ69yuTc6ttaAogGTrhRSsCyAJytGJuigeUOke6NioATF_5HVnaggYErEnwPX2Q-9za6xYRuSj5CDjz9m3G2rd7N9mOAhDE8w6n_xg8kz2VyKyJqHL_l4c3uKsXNL8TM-q0DnWNGEZerBjMg5yBQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
لیست بازیکنان تیم ملی آرژانتین برای رقابت های جام جهانی 2026 با حضور لیونل مسی 39 ساله.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/persiana_Soccer/22403" target="_blank">📅 03:08 · 08 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
