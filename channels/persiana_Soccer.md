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
<img src="https://cdn4.telesco.pe/file/qfCx6nJAYKZruNdT-eLoGwGfPj3bJg64BJNDx4Gx9I0d5Iwhj9vCHY7YTZX187aQtcaRqthj8mwIgDUNDUyvYpKa9AEm8kp4OAO47J9ZJn3uaDMgxQ-Nxwyz64f_ueSRRA1EGaZYW82y2wPKI4jmA6XPfI-gB_HBeXjZnGftrglMYf9qeMLQsbbW3pIw3X4DDt4VaaA1TsOPoZ4JfCmtl4POZtWVnGN8w0kV7mqvhaxlyF5V01e6ycXV9V3iGvaCW3hO6OPMYxJExD5HsZEUOEo3ejt1hroIdNH6FJ2M5PB9fIQZ8MoRjSRtZD0jELFE9Ax9fbhpPf7q6rSFidr7mw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 622K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-11 23:03:40</div>
<hr>

<div class="tg-post" id="msg-28947">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bdd255c037.mp4?token=EMqj6dlHzlIp5us28GJlmvoq2N7zsofkMpLdCvHJLP8bEwuGOdHL7VzB_BqCQbgsRbgMlzxDrQmBF7ZElFjuTCQa66uEFNLlLgNjYijvpS87ucroOHZOqCYXa5IemByZyWndMMveX5yGuRao215TonBCacBjMpQQuX728yBtRt8RkHN7-5iOE0Xxc-xJag1ja8YAA31H_r0k15n44avYdE_tc4tZXUjiFQFV6AIOS_WSRMI9Zfjm-8s5K47VG1Mnzx8cobIgEZu9eN_HlP3jUGD2lYdqfC-Se1pXb2VqG2W4nJTaHGp0Hg8BXvVAoTqFqlZJ6dwVI-JB8yr9juxdag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bdd255c037.mp4?token=EMqj6dlHzlIp5us28GJlmvoq2N7zsofkMpLdCvHJLP8bEwuGOdHL7VzB_BqCQbgsRbgMlzxDrQmBF7ZElFjuTCQa66uEFNLlLgNjYijvpS87ucroOHZOqCYXa5IemByZyWndMMveX5yGuRao215TonBCacBjMpQQuX728yBtRt8RkHN7-5iOE0Xxc-xJag1ja8YAA31H_r0k15n44avYdE_tc4tZXUjiFQFV6AIOS_WSRMI9Zfjm-8s5K47VG1Mnzx8cobIgEZu9eN_HlP3jUGD2lYdqfC-Se1pXb2VqG2W4nJTaHGp0Hg8BXvVAoTqFqlZJ6dwVI-JB8yr9juxdag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یادی کنیم از این کل‌ کل بامزه نقی و ارسطو دو بازیگر پایتخت با عادل فردوسی‌پور در برنامه نود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/persiana_Soccer/28947" target="_blank">📅 23:04 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28946">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UdGucIQDVN6utVJRSFBExqavBnZ7jFTCuiirwK_gxnVpW36Bz-qmtrM-T_UzjfxGbmzLCR4lCu3JdDONQI3MiXbLuleTCnMC3CroYm_eXxjRyqJYwwziziVqgBSAPwtb63t1Gy7HOYE9nv4U7eCRWi2bjK7JBAjpCYlHZ3I8m4PU04P7q-B4Ds366W2RN6pFMdSF-zhNdmrI-Fqm-HV_eExsvgRvXNKqvrDammCl5jHv5WY-YpHsTvNkp5yc08f1eMxvHm1zNsy231FsfHFRov9bhdB4bjxBsKqXLMDB_kKazsUAjTktHxMG4bhn6KYaaqvSxumeILjZaQ05mkGxPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول و نتایج دیدارهای هفته پنجم؛ تراکتور با جواد نکونام صدر نشین لیگ برتر باقی موند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/persiana_Soccer/28946" target="_blank">📅 22:37 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28944">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WY03DxhVsKaZIe7UUv3BERusBKYPKRJghGnwLs2ZiGnY-0rNt5KKKC3KWiokIbrW82DVCPABfcQ1n6p2No54OB5rn3Wfx4_GwmUdeGzZ-KX8XDFBJxlJ4P_hABHBzpgrGS51CHDzDvchk6O1bDdSBibhEbty1xNrEEcNeUOnlBWuMbqKu819oxl1Qm3TEzEgdkp92jLxF5mMjMjKz27WRlTBoXMaVs3f0aCMMUiHCmU1_YujOOoZdqqdW18BZ-NBztQfF9A58sSmlk-0Nbp58xPdOzoYHCPBxjyqUjqi3XfheFyvlMWJD58P0GkDmc0INoeymox6cSMmNcOxN3LN2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UKqtjncBQYablzamVCMz9vKAd6b9nvCMG5u7Zo-7PpSI-DwnMKVkxOx3L-gCPKHhnwH3fsyu4UYlSwFPpcru5emZMfwLBiTuAnFu_iGreQHHyxzd0mfXxjsY9-NiKtE7JG_bC72onrCikesuugz6TwgXUhoRgIJlJh5b_ZXIN72OtCxlDyAGtSEh8ztxF2XQJOFVWZYoPpJYrwUKPLp056SI7Ol5G5gowFTKAJsykUq9XPq9AAIHtfmYu5Dv0OUagaqLJP_8PUOTsW9gmXoSrtWQFkiEeqYG9zUntsD2tzQBfVMbSTIfiFzYL_FSRh48kWhYaXYMOdgtHg7_bHdJBg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
هفته پنجم لیگ برتر؛ ترکیب سپاهان برای دیدار مقابل صنعت‌نفت‌آبادان؛ساعت 20:30 شبکه ورزش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/persiana_Soccer/28944" target="_blank">📅 22:34 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28943">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pJTNGFwXal1NqqayPoJ7N9GAt_J28wa1KGHoQTdCDyO0mp8-BS_kxJ3NopbaK37im9S8Oc7xbKkK2gAwYz2EhKMpxcHQ_BQ1oYY07ySMgsvOqGQTjqUT_PvztJ41mxUTyMXwg9WyNEjMx4c5ogbepWV_TM0zM5vpg2hKIQE1FUGr3sKQ7_WOJKU5vNFGV1bw2NyovXHthVu-XLgoTgIi-gcb_Y4gVRfKyw1CaSbeS9hD_dDzFAATvz3vOYGPLxGfLtVv4vgOZePwvFsI8cAy7Ym3tGNtYvD5roEUsljB7A2i8nzjf5Rf_h2hYRT2MxQTJIRAGscEH_gDAC78E_rVfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باشگاه‌پرسپولیس‌بابت‌استفاده‌باشگاه استقلال از یاسر آسانی ستاره آلبانیایی آبی‌ها به کمینه انضباطی فدراسیون شکایت کرد. آسانی زننده گل مساوی آبی پوشان پایتخت در بازی امروز مقابل سرخ‌ها بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/persiana_Soccer/28943" target="_blank">📅 22:15 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28942">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I9SLSyv1g81TnkCR31mjEvtyVJagge75LHX_9z7BxnGBdUABYWZRnahdTjzK8sgxDnjKgNivOilKBW4TpoJxR92sw9bxhMWm_2G4wrqkU83vAVOBgaNOL2QYWldGzHjFcQLVArdFvlrKM-hl6IJeqvhbkmZ10mMCCqlF-BA5cq7xpzKyPTq3NNm9ENJEVb-0Xu0Dsw_cPzw1X71myPXEuzwdep0Eye_LvEibOi9Gp_c_dVbmznl9HoyEsrEbWN7UOKlMVh72p0luXZGt_XfySBqb00v4nKuMbOCMb6vUNU3Dojts4WPqkIaOLR7AQ7I5vZt0iGb6oQ4ZjKd_kSvBHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تاییدخبراختصاصی دوهفته پیش پرشیانا؛ اعلام رسمی کمیته انضباطی فدراسیون فوتبال در خصوص تبرئه شدن استقلال و یاسر آسانی در پرونده شکایت مس شهر بابک و سپاهان.
‼️
دادگاهCASهم از هرباشگاه 100 هزار دلار میگیره آخر سر هم بهشون پاسخ منفی میده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/persiana_Soccer/28942" target="_blank">📅 22:01 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28941">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4240a550b1.mp4?token=FSFGXOkty2Bg5nx4_o8u8qvF0UqSFh2kdkP3VnPRptaxDFcRSkVLPW9CAoOWqn4GzygpUI04VMK_lgsRRDTTnL7nGCrVtIcQZqffrU049gINuwG0exKawZoguDG5E03CNVavhdFPqI2pYSSGRci_CosZocWHc2XcMmK6X7LLvLMFIJyQFG9ZyTgVUJzsDKjGt67u0xEwMvxKuyjtGgohoTiqTj_iHB2yizzAv6iwzILAHstfkJJzOyU6W5SOOiRXzWLKHqvAopfkLMGRjdTvO7LbYk2wUVfCMiSCQhXnJpD3ZwbQkLZT6EB-T4V0oXz0VsJAMgb2_dZP6MoxyQJ9iA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4240a550b1.mp4?token=FSFGXOkty2Bg5nx4_o8u8qvF0UqSFh2kdkP3VnPRptaxDFcRSkVLPW9CAoOWqn4GzygpUI04VMK_lgsRRDTTnL7nGCrVtIcQZqffrU049gINuwG0exKawZoguDG5E03CNVavhdFPqI2pYSSGRci_CosZocWHc2XcMmK6X7LLvLMFIJyQFG9ZyTgVUJzsDKjGt67u0xEwMvxKuyjtGgohoTiqTj_iHB2yizzAv6iwzILAHstfkJJzOyU6W5SOOiRXzWLKHqvAopfkLMGRjdTvO7LbYk2wUVfCMiSCQhXnJpD3ZwbQkLZT6EB-T4V0oXz0VsJAMgb2_dZP6MoxyQJ9iA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
هفته‌پنجم‌لیگ‌برتر؛ شهرآورد 107 پایتخت برنده نداشت؛ تقسیم امتیازات سرخابی‌ها در نقش جهان
🔵
استقلال
1️⃣
-
1️⃣
پرسپولیس
🔴
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/persiana_Soccer/28941" target="_blank">📅 21:51 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28940">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">📹
خلاصه‌دیدار جذاب دوتیم استقلال و پرسپولیس در هفته پنجم رقابت‌های لیگ برتر خلیج فارس.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/persiana_Soccer/28940" target="_blank">📅 21:35 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28939">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BaKgVYXMxW3PwSKTlnqh24qn-RxFjNOT8THlDGZ6_oNGVkM-ZYGjBUpah2uwVV0PPQnvxAfTxyMbTxZpLFl585yIDFS8gw7kQvQkgeE8VJVwv3JqBSm8WvWUr3I9LhFQtTHElFBg90IFjA22jEgOR9_YcAKyB4en2nnAwmNxASA60AvZs18CV68yK-uQ7W8LhxvS2APFj17KwslK-eR0LT_H3S04vtOKkkRTke0IXM2yyyXojHCAEpxnVqjk--d5owbxVAkx0YKklJruKPuA7ZfgfqYWVzg2jqD4uz_iWeVQvx91sybSw68GJ5CjiKjqCDnErg5MWftpyIEb-_A1ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌پنجم‌لیگ‌برتر؛ شهرآورد 107 پایتخت برنده نداشت؛ تقسیم امتیازات سرخابی‌ها در نقش جهان
🔵
استقلال
1️⃣
-
1️⃣
پرسپولیس
🔴
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/persiana_Soccer/28939" target="_blank">📅 21:28 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28938">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mCFHZK6Nw2dcoq_9de2WjY1VxVXvEhEtNA1cSiTJF7OTeXxdnqnwpHmkLy2s268iZjg4KT5tDSuUrD2-swElQCK1G3Fj9qleNu8qQ7mhCiFr3biiIU7YR9_w3o-14UZeKHKTqjmIAJAdeGSll9jSVOpqQdxLvjdb3yKUeAhHJUiTXnS0Q-XLanKmrTkHjr8vXG8LWw6_aRc78bXBQ6EHCYNx2-LGfkpelK7gFRQAGfKnpI2qqy6FbIf21xBfcRbwKCJsz8WIa79s3XG8mZrDBlcMDEIn7qzjDZNh9v1AZWkpkARNuPIIYVGoQ2aDWV4_TiWgs8Xi3RRMSoX42N-OOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
ستاره آلبانیایی بازی رو مساوی کرد؛ گل اول استقلال به‌پرسپولیس‌توسط‌یاسر آسانی در دقیقه 60
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/persiana_Soccer/28938" target="_blank">📅 21:25 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28937">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba22d8800c.mp4?token=sJPhtGfnKXH9lJjiyi8SKn7FC5LSasuxYGldPDCoN4rcMki9Mqim0ObWKJv-8yonO1qt1a8t2m8w3HUOV4SgaEfJJ4ISRpeqylqhZVJhj0hThd945tYGvhORhIGuisNt9B46CNVznTRoCM-E6LF4mMEk4fli2Macia6zVDMT6dtU7LlOQgFyGtmQQfzaFGnrA3sONnJYJWqi5nqkcEa9VmXGeI8Cl9lUCb6tA5GfCehKbJl0OLBSHyZRMzMB35STuXncFqIGM94PIhVUzoC0LvQJj1JmNV2UVqhyyfkKT1qM2k_R-PM7gMKK6NAwQ5L7mNSlTSwdpmsw3Lj-2eAnaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba22d8800c.mp4?token=sJPhtGfnKXH9lJjiyi8SKn7FC5LSasuxYGldPDCoN4rcMki9Mqim0ObWKJv-8yonO1qt1a8t2m8w3HUOV4SgaEfJJ4ISRpeqylqhZVJhj0hThd945tYGvhORhIGuisNt9B46CNVznTRoCM-E6LF4mMEk4fli2Macia6zVDMT6dtU7LlOQgFyGtmQQfzaFGnrA3sONnJYJWqi5nqkcEa9VmXGeI8Cl9lUCb6tA5GfCehKbJl0OLBSHyZRMzMB35STuXncFqIGM94PIhVUzoC0LvQJj1JmNV2UVqhyyfkKT1qM2k_R-PM7gMKK6NAwQ5L7mNSlTSwdpmsw3Lj-2eAnaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
دروازه آبی‌ها بعد چهار بازی باز شد؛ گل اول پرسپولیس به استقلال توسط محبی در دقیقه 50
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/persiana_Soccer/28937" target="_blank">📅 20:55 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28936">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09a3fe7b44.mp4?token=r7VlSSUr9sgDGkvwG62RVDd8nNfTruFdSZsftRI2QJqLKbLYq86xm900e9-Wexo_IMk93WzZ9NbpO9ht3J8YR7x_CcLsbULIWiWaOeUz_TraOWegB0sBimqEtIQcY4mKAxgwWnKSuCaBTxGdouTm8MlfdY2yNUyGsZ-gbjvnMYOLT8blJ58QBJX-XipGhi9fkQdVoUzKmda_pg18V3OH5nlGuO2sisXRjzy7_QmWQddknO8D1icBdTFjJaeJwvv_m8EjCCIjP_2iUisDVj23-W6k1fVsorcSoM38UUpUUdMXPo2yt11OtuwzXXqTvQcTmO3g0OxTop5W5el045M_SQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09a3fe7b44.mp4?token=r7VlSSUr9sgDGkvwG62RVDd8nNfTruFdSZsftRI2QJqLKbLYq86xm900e9-Wexo_IMk93WzZ9NbpO9ht3J8YR7x_CcLsbULIWiWaOeUz_TraOWegB0sBimqEtIQcY4mKAxgwWnKSuCaBTxGdouTm8MlfdY2yNUyGsZ-gbjvnMYOLT8blJ58QBJX-XipGhi9fkQdVoUzKmda_pg18V3OH5nlGuO2sisXRjzy7_QmWQddknO8D1icBdTFjJaeJwvv_m8EjCCIjP_2iUisDVj23-W6k1fVsorcSoM38UUpUUdMXPo2yt11OtuwzXXqTvQcTmO3g0OxTop5W5el045M_SQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
آمارنیمه‌اول‌دیدار استقلال
🆚
پرسپولیس از نگاه ورزش 3؛ هرچی‌جلوترمیرفتیم بازی قشنگ تر شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/persiana_Soccer/28936" target="_blank">📅 20:46 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28935">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de9ae878bb.mp4?token=je0z6aQ7dPFPytVIS8TgfvDGg5bj3WnvtQf4wfKaLO_tFAbBlrQUfb4mTyUUZCWzyMXB0eM0qZ7AZ3guiLkALVpjd9fsUTdjf5d6pMi33wNddDR4A-1vS7oJrGc8iphJuptB4WmdKPVXmhId2vFw-BIXJCqdlzKjb08VMimJclaKyxMCukElttpSNXlOTt8S0r4k4PVWPlSQZQIS9BhOvYeE4GydoFA3tT2N-23WDlQMvTyL_TyioV3TdMuJvTyXr_ucNt7ixvup8MDVn5ovTcxtwYrR-aKBCG4KFeFZjTheUovURh_Hp8anUMim5jPY9IT8wRZ_g300RU2qtXap0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de9ae878bb.mp4?token=je0z6aQ7dPFPytVIS8TgfvDGg5bj3WnvtQf4wfKaLO_tFAbBlrQUfb4mTyUUZCWzyMXB0eM0qZ7AZ3guiLkALVpjd9fsUTdjf5d6pMi33wNddDR4A-1vS7oJrGc8iphJuptB4WmdKPVXmhId2vFw-BIXJCqdlzKjb08VMimJclaKyxMCukElttpSNXlOTt8S0r4k4PVWPlSQZQIS9BhOvYeE4GydoFA3tT2N-23WDlQMvTyL_TyioV3TdMuJvTyXr_ucNt7ixvup8MDVn5ovTcxtwYrR-aKBCG4KFeFZjTheUovURh_Hp8anUMim5jPY9IT8wRZ_g300RU2qtXap0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
فرشید اسماعیلی هافبک تهاجمی سابق استقلال با این‌گل دیدنی‌اش در دقیقه 90+8 سه امتیاز ارزشمند رو برای ذوب‌آهنی‌ها دربازی با پیکان به ارمغان آورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/persiana_Soccer/28935" target="_blank">📅 20:35 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28934">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/igWYY_ycNGP5pM4FEmWQxTSAEOuYRMUHxX5if3ZRh-11WhUibmkZeDSI2PYE-cKqOqiqJnJd7pZ23oV8XdFlUXCrLvC9jNdzoEW_rVRMldDGfCOvTp7Gfru2ook5Rf1-pHVu2gFeT8WDRbpAwgxh-R3kA9714W_AQ0EEGmJjsG4e6NPSDdX5tverWO_BSomPpTk4QO4Htypr1uZ_T8SD7-HT0Q4tGegTLQ25wQ5Yo5my7KRMaTZ-fuLj3K67UX4-FlqYzAzVghRkDOVP3ICp2wmw7uGTbg59V1XiVL_olcgNJdKfH-eLo7DXYLD509V_cmTKh4wnQtkRu5GtlcQKmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آمارنیمه‌اول‌دیدار استقلال
🆚
پرسپولیس از نگاه ورزش 3؛ هرچی‌جلوترمیرفتیم بازی قشنگ تر شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/persiana_Soccer/28934" target="_blank">📅 20:21 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28933">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ld7sRZ8yl7CsOuKNSeYfbh6vD5H2qrR4wtXAgng8T4LWoM4KHghi9RTbvhgCGZgHxO0_CrO2VdYsNiZ2Jf6QDGWgnuXDXZo3m2o0baDa7fs9xT5Z2EkuZjbyre7FL63tSi8n4YqtzVmlUgPvdKquS1oKBUUTIq6Eaq411mDueM2-4_T5d1TuyMKi6Nu08q2z-8a981fW7IfAhSCAZahVwDqHP4JyPHDXwiHVLP9Ni7bTE36dj8ClhYjekMzHXgN_K8eeYU71Pc0RCMGCHLDlhxva2Eg0F3hA210ZU4A5GnEDkG4u4FYO6ve-i3c5pA-LwW4DP7C858crk6iDW5gm_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته پنجم لیگ برتر؛
ترکیب سپاهان برای دیدار مقابل صنعت‌نفت‌آبادان؛ساعت 20:30 شبکه ورزش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/persiana_Soccer/28933" target="_blank">📅 19:43 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28932">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cJTRI8ltikY9Lx_i3iyWGzXye5fbRBzsfu8aBiWvxbYSSa4k5q4nV-1yJK2eNeDmfKxfhp_S9IyQxFfCVh4gKLbAnt7bEM1fkGNC4k5m_Z69B-xrxoQ4p13HaYLqF3YaBVAmfPleDJo3aKNkX1E7wFR9Pa4eb0EJMoHBpdUIyng0puKGoIM2w_h_KFWWG3k_pPJGfXBcPOyhYo1ugyqPd_2xyftwLKb1riLuZ0KfYo6AzZP2_M7FCwzVRSG9JaFZjhyB9umhY4VZO4AKV77e_bUkAJ5caCL8YUPqJF2Y34jKabdnv0GHVy_ijL6v0ULyoQtXfTger1CNkAcIY23EKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
سید ابوالفضل جلالی، مهران احمدی و رستم آشورماتف سه‌بازیکن‌مصدوم سرخابی‌های پایتخت به دیدارحساس‌شهراوردپایتخت رسیدند. تقابل‌ بزرگ دو تیم استقلال
🆚
پرسپولیس یازده شهریورماه ساعت 19:30 در نقش جهان اصفهان برگزار میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/persiana_Soccer/28932" target="_blank">📅 19:24 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28931">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b4d98d669.mp4?token=LTmTZRXzW2rYx3QLpnRkbqBD1XgcLEyxX4j8emmICO-A66oQLN7GPv3-p_aiFBofrjpVRwhIC7LpME2NO2zyRd0_uFRF3Ehm1IccPg_XvRbCavMMtdDkHlIugo1vB2GnNyGQ8Oi3dkFqo331PY_RNLR9VsCsQ46cE21mojNE59ZzGRPeUkQpsLsTID529chMBq1naCOgaKJgk7epOzAn0g94mWLgIDbaahwy1JGc6N6BMRkpkNhO8UQA6q28VOFN_5KDToWbm_upltx31lIKLs-QaaURwX3S3eeTmsMfZdy0i7b3uYuobdv6k6GgtOcMKwGrTmQxz2JzRtoq8I1uPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b4d98d669.mp4?token=LTmTZRXzW2rYx3QLpnRkbqBD1XgcLEyxX4j8emmICO-A66oQLN7GPv3-p_aiFBofrjpVRwhIC7LpME2NO2zyRd0_uFRF3Ehm1IccPg_XvRbCavMMtdDkHlIugo1vB2GnNyGQ8Oi3dkFqo331PY_RNLR9VsCsQ46cE21mojNE59ZzGRPeUkQpsLsTID529chMBq1naCOgaKJgk7epOzAn0g94mWLgIDbaahwy1JGc6N6BMRkpkNhO8UQA6q28VOFN_5KDToWbm_upltx31lIKLs-QaaURwX3S3eeTmsMfZdy0i7b3uYuobdv6k6GgtOcMKwGrTmQxz2JzRtoq8I1uPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خاطره سیروس دین محمدی از بیخوابی در شب قبل دربی و گرفتگی عضله در دقایق ابتدایی دربی. ماساژ درمانی؛ جان هرکی دوست داری ول کن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/persiana_Soccer/28931" target="_blank">📅 19:22 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28930">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eIIvYLexWLRsq3-DrVonIcYdnNrPShYokVnbTQWtvRGt2p81BEK-APS42-CclqxPqaxVclzRZLRtrvWFdynJODPcPG_xcMZ8MM9rhww0iwmM4QeNsr5oNUxMesoUEaP7UyyRnJUlkRhaCZYjSMEC_RkWE_cfuusFv3LYypQeayDw9GDYPb_vveBAru2UQE_USaMUMoPpFZZr9Dob9nJDhGjaJ2X3VUQm5c66Jgv05ls7kZov1WmF-e0kZhXAvYOS7X8Gu3SbBx8x8W2adMZaTHpD8fAHAyYawjmo2VODfDe8fGFC_8zFgUKgnUltE9eaMop0wMyxpJo7Gv4_rFeJlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
لیست کامل بازیکنان اصلی و ذخیره دو تیم پرسپولیس
🆚
استقلال در هفته پنجم لیگ برتر!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/persiana_Soccer/28930" target="_blank">📅 19:22 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28929">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uI3lR1VJzDZuqBXG49jP-eVS9rYb0u3cxb-yNpRyeSR1qYf_nSdBOWnGuCeddO_8SRlwvWj0vWa9suenD0B7LEbHOQJHJtinl9QKgR95DIqTx7dll5c0q0KyBDKtGEe-QbBuvSkM8jKETToG3Izd3KNKqbfA2kSFL-heLqutnui3tgFlmD127PJ_n8CxH2fbWFwUbqBOn7LMhuME-oPGutGxd2QE64IWO8rQdeNv1KDBF_qiIpmeSZAIcubKRx9rm-wqteT5On4Fb7lxbuhiQ_6l4T3b8JWFloPTlohocfsLEysFeLV__ns65eRB3ZJJuGyz0v2ZamMjLGU8R3wTeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
دور اول جام حذفی آلمان
💳
اسنابروک
🆚
بایرن مونیخ
🇩🇪
⏰
ساعت ۲۲:۱۵
🔴
بیش از ۲۰۰ نوع آپشن پیش‌بینی برای این بازی در‌‌ بتگرام
🔼
با بالاترین ضرایب پیش بینی
💵
واریز و برداشت ارزی و ریالی
❗️
🔥
۳۰۰٪ بونوس رایگان بر روی اولین واریز
❗️
💸
۱۰٪ بونوس روزانه واریز رمز ارز
❗️
🎁
فرصت را از دست ندهید! همین حالا پیش‌بینی خود را ثبت کنید و از بونوس‌های ویژهٔ Betegram بهره‌مند شوید.
🔴
http://betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/persiana_Soccer/28929" target="_blank">📅 19:21 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28928">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d7jdXKom16nX3Gw7ipqjiq4CQdm_xL1JkX0xk0oqlRLCdiIWh8qIoWCi8DMU4lGwx1hEDbinDBrmz92_m7O-ALyIUAKMBbpsGnB-FwpaJfZLa56D7sEgMrIUTfGaEPtWeHKosc8CSK3_VhXWpGianSoDnWntSU2nYEjrLwRFUdS-sGCgzkGC2oHJoslQR0ihn001UybmhwNuBGyyTVmsaQnG0-o2LOHVCx5EeXnvAXY6ej8b1kHwR5j6oidQmmnhGQYHwaiqIvWKKW38cgDBnCtHgCbG6butCNGvX8Sf3g4mgm4f_k4ex6Dd8qxo--sG9TBpn7rdAAh_Mlr097xYew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته پنجم لیگ برتر؛ ترکیب رسمی پرسپولیس برای دیدار حساس‌امشب با استقلال؛ ساعت 19:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/persiana_Soccer/28928" target="_blank">📅 18:43 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28926">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ktAdmI08Tvrxdi-KAMiES2DLRBgGqaBmsHiotlCq4wNGKsJRqsDdKhddmot0v979_sfzrdsS0ZeUaX8qpP25tVfIotkIcr_8hYhJaIyogWMeOcK925jIEWMIKtugQivncapByBlheQv5Azy0r-GUJyXjpF9AgfNKROB8wQJE-BoCc0zVlgC5evXQnbG7vjhLfauiAaOOn3eTPtDUoPx3xRPrNV15bRYTHIgVdn10PL60HsdGdcC96Fkio8yQsBcC9GciilddbLfJWz4Pk2L-0J3KM5KXFiW67_4FAuRQOqFDIMAh-QKzmVhbcAHEWuuckmiDfw7507q9BPhSRHxf4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/carUBFQQ0x31e4Z8xHFNKvMsWlYzH5eE-gz_P0edhCLb4am9AEujVHxTicahqX8dUEvTP516MZFXcPoa_7Qzn_crEV7fuPKcpH88TGDa2plswpI0kRQkIqif7wLgs3MvI5iDGiao6FzIX-G-wkoElQnQlK1qhUtpxaTtUI8QnCwyHm82gqdn6f_zEA927_SGD1-8asmKa4zhTPVoxjWu3h0Kxv_YidQxE-wuBk6I4K-JT5pIDPF5EfHw05ZiPcPRVkf798bMSMjdZRXX8c5onQsU9IrQl4gw5MZzLbFhlcCGPMzbXUyb-E-IU2r7k63galiasHLr1mROBo57YRYz3w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
هفته پنجم لیگ برتر؛ ترکیب رسمی پرسپولیس برای دیدار حساس‌امشب با استقلال؛ ساعت 19:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/persiana_Soccer/28926" target="_blank">📅 18:28 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28925">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PqMaSinfqCxEM6yyoCOTHZwkw0CgfuiwZSe2kSdNqK4k6xddDwFF37pIeP8353dlhu_WTirGIAFKGxb4q_44Xe0tC_4OZSwpKQ61ESLly5hWw55R9i9Yby-DzgIYooG_QHvHg8boJjNrb7odwwnslqgEt9kxv3ACWMCqwbZg2mVPGnyYW8DnJTsgvXtP_3ECSqzjEJDA8zRNoq47NdIrTNsbv_Lsp1FAur_mF-ZWK7picM0GiKvNPhJP-GYeRRhdUsw_1hXQi5PWowvKz1s_MXUNLMEIfDBKm3pHTNOnC-PGPWmQYGGT3M9JihC8VxXmf7vT9HkRMMgmNKYoRNvhKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همسر لائوتارو مارتینز: لائوتارو در آستانه پیوستن به بارسا قرار داشت اما اتفاقی در پشت پرده رخ داد که باعث شد این انتقال منتفی بشه و باشگاه بارسلونا با گابریل ژسوس قرارداد امضا کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/persiana_Soccer/28925" target="_blank">📅 18:27 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28924">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uD8Hm6w0MboqcZH540oG34XASLpRQOmcSQVoKSQiULI_iQOqyYntmnGdL8jxQEIZ-VBRR44DFUYghk33E6L5i-YkUvo7iCRykvqwcPWSaTHXwjLTpsIn5buoPJ6ihSqj6m_mVFu1_ViIUY2bnAu4-f8lykyCuIHc_4q4r_l1Iqtx_639mJ6IcbOpkeZvJb_BlXCZMhICmKb75W9148_FwoCmJSOgxMjzbZWiRwvH84bMZrgs6mTC9QGrkSiofw6yJ78U5pcnilOTbe8u00HsUsPJFGqYSnjbQ5Wevxe86aS5HxIuVgbfZuqQXJxE7zExkVBNgSI95pGIB_a44cGB0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته پنجم لیگ برتر؛
ترکیب رسمی پرسپولیس برای دیدار حساس‌امشب با استقلال؛ ساعت 19:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/persiana_Soccer/28924" target="_blank">📅 18:23 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28923">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BwmmE_yi7rFGRhxW5XVDsSdAOOzg7TTLzuUcKJXgQo87W7XGdbDM99N8Gb1NBsogSvUkZdMFSCVvlKFIfKqa5xVPCFy_p3Ij5oBODVFFGT7P5iX1a0EwJyfcPDKIcIwblwDa4Q-ZO7w-vGgnaCn_YEHfs-m38A3l340R_WpMsdH3bCjO9i2EUjrre8lVB_g92RAZFImR5h_pkiP89gHjTA_XPkKfeowDOMravVyAY4iusGn6gX-yT4aoCEbRnBUmVWZ9WcEr9vqXUk1gQDY8fTW9Upd_yKVDDCWboH2ZeueuPrvNzeEjhfocnKoeG3pB-u0z1k41gWEbp0xTsDgAEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔵
شماتیکی دیگر از ترکیب احتمالی استقلال و پرسپولیس برای دیدار حساس امشب دو تیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/persiana_Soccer/28923" target="_blank">📅 18:19 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28922">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vZpV54iwL7a1Yilnkaiuzh6YAuoyvFpgRKBLi7CphCqyBptRBDm26sRBGuXhWF9x6zMrpEZ5EmfH3uIoUzsEDttOGmaiQqWwSpVRQsqNqUDuXkv7-x5OE5KUv5fV1WMvyCG2R0XmFjAEM0JlB1Aw5T2F7snklUkqdwmgODagi2pwb-VXIyXkl2baKF-EfvvQ9MS_EZ5m7jKC2O0MxV3v2COZmIxVl5E350NiXgnccTIlG-RE1iwgMj_9VoucTFVKQnz-sveBRhl7tC_6cqPYWLcyjXnfk7Z_c-tUMOgqohpLqlcQDj7xVCn2EltLrevCSyAbpkvTfvql5Dx9ryqnMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نگاهی به‌عملکرد سه مثلث خوفناک فوتبال اروپا درسال‌های‌نچندان دور؛ کدوم خفن تر بود بنظرتون؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/persiana_Soccer/28922" target="_blank">📅 18:14 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28921">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa3087d7af.mp4?token=pQi_Y64tlhHw7arEI-WSg17WHNNNVfRF_G4iRkgmHKWQNDru_Z3-6YKp5BgpTLjAr_V63BpFoUSSLrDnYCaajrwnofpdBhqvIhR5LJkRv_AJ-qmapZeIW1yV_-lt2ECsgjrtnoJcIUlV4TBAXbarw6u4J_MCvv5Qbu06C9QXN5cQAQEg2e2wmccdtwJMUgyxcbkJywZUmW7uo_sC_y6vfXSo7vCikG6k63f0kcy44YfI9PqIXvREaKOdvGUUEP50ihdMegStQw3GXE6IUiagrJ2v1WMg0TxU4SCfjzt7c3--082ywpJhXXV7LioH2g18AQKfejdmbsrmpEaQfxgK_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa3087d7af.mp4?token=pQi_Y64tlhHw7arEI-WSg17WHNNNVfRF_G4iRkgmHKWQNDru_Z3-6YKp5BgpTLjAr_V63BpFoUSSLrDnYCaajrwnofpdBhqvIhR5LJkRv_AJ-qmapZeIW1yV_-lt2ECsgjrtnoJcIUlV4TBAXbarw6u4J_MCvv5Qbu06C9QXN5cQAQEg2e2wmccdtwJMUgyxcbkJywZUmW7uo_sC_y6vfXSo7vCikG6k63f0kcy44YfI9PqIXvREaKOdvGUUEP50ihdMegStQw3GXE6IUiagrJ2v1WMg0TxU4SCfjzt7c3--082ywpJhXXV7LioH2g18AQKfejdmbsrmpEaQfxgK_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
🔴
کری جالب و دوستانه بانوان دو تیم استقلال و پرسپولیس در فاصله دو ساعت تا شروع مسابقه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/persiana_Soccer/28921" target="_blank">📅 17:40 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28920">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gg_6wFprsn2CGTTHJZNmMuBPD9_q6IxXsf94rTNEOoqDymSSPmH5JshBwRBXN3AC6r9WZVxn6oTqp5lIUVxd90AtxvDT2ioytJ8QUfoj2AQiLPmU0rJiXXACjondrkO9k05G2emayxC50mUyX0q6PyjpYPMxEYQPbSggh-T_BZTYatEtvkYl0Q6sj8QLbnS-nweRpIXK2uOezVV-F73J_PjPm2VwVcmd64WKfJBtSarPozMifr5V8mPc4komFIdOlyfOqzoVvPkC7QKFY5BiSgZz6ifRn_GjoEiLBS-CIGrYHtPSY6icnHuSy7E7H805pU7x075E0CPD0Jmr8ypLNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
چهار دربی‌جنجالی دوتیم استقلال و پرسپولیس در تاریخ این تقابل‌ها که نا تموم به پایان رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/persiana_Soccer/28920" target="_blank">📅 17:17 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28919">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HKYHNi_-oK-G3N02ZI4vHk0wfaSdpg1Q2auLRVpWK3CpDa9hpvq9_kQP-_sx6sn4Q_7HYhjloPy9e1NCdEtL1QtKV2Xrq0hj15Ms2hdg5agnT6ErnXN51GPcLGbWLMpLhjy6liEd3sxMp7vt4bNm0o2E_YLoSRPS5xtfshBaxt_JB4mmforYh4gfXyWs8sUN0gX2O8xLQ-8ruzbKR1Mth7rXgCNn0dQeXWbrRGUV2ui5vun2jLKB7Ec-Yj3jU_-uh6gBa4U4yBKYNPfmJJDfz-K-ADIKeKmlwdotKjl1gm1NI4Y2eBOQRhoTVCRePC8Zz7yYPayANoRem3StWRsviw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه عملکرد پیام نیازمند و حبیب فر عباسی دو گلر سرخابی ها در تقابل‌های خود با این دو تیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/persiana_Soccer/28919" target="_blank">📅 17:03 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28918">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uR0GxGIxZ0i8sILbwbEwYE56yYxHXA1-HGJSF1WDQummo52TRXmXZYKNIQ2EYkMz1n57qeDEZWpxHXElb4sntBQJEjUQGI2j0ckpJA5Ub27KNZX-g9k2KX1YyLLVakP0tRiVMfZ1M_9fgJ7wH7GeCHGkHatsLq7GjYTEq68KjgSadRgb8R01mLcxlzv0AbNq2vweJ2RU4rBkrp3A4xdeg8Myvpctk2sELWpd8oImxEDBEQBVbTA9uS4MeFEEas4YDRDIhpihg99c7_bkbGCMBb51reTvPzUcCz4L0AIYdwX1rxTvVWJnwnX6Z1FGER0JHLj1ObW-rzftssQabMc1Kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مسعود جوما مهاجم سابق استقلال با عقد قرار دادی یک ساله به تیم الحسین اردن پیوست. عملکرد فصل گذشته جوما در فصل گذشته: 33 مسابقه، 19 گل زده، 8 پاس گل و نمره 8.1 از سوفااسکور!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/persiana_Soccer/28918" target="_blank">📅 16:47 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28917">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/osT4L4gFJpvIJfsK_oBCxGdBa6kKe1pvNElaLKqRqL_5gAawh_93RNFNGgsuhE1jgXZI4qpOLF_8YtWSCUtTIjpGUda4KKO6wWUaJ3o-uaTf5GvpYFyRbF3QmYwV3Rx_wRpjHikCoIKqTaE_uPoYwe8JDoTkQ3po6SRtMY4m5lxdQHNN_Fuo5OLKrCjhn2mrc1baBFWFZK6TSh2NSRtDEP6rlE2TZMHnBo5a4tAIG72zGUElkaUMSQ9yYXlDFmCOtbpETZx6U3fYcqXzFeTxieOSX-O5zOh6UH7LE2PzNxGBMahBaA0cDHomFkDkC-dgedOUgHyYad2UAYQOsnR_MQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نگاهی بیندازیم به عملکرد تارتار و سهراب بختیاری‌ زاده در تقابل های خود با استقلال و پرسپولیس به مناسبت بازی حساس امشب
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/persiana_Soccer/28917" target="_blank">📅 16:20 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28916">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mOJ2MaqA0Z9ehkl4b-rp5t75V67oK1b7gbfunHKsXXixKFGhZ8Y2G4cDNSHv5U3EjTDAa3mlftmky1kKZ726zi5Sy4PtBuGfZ9aXKjBhJe5y25ZWvlC404GF9KR8y18lHOQlSH40732wBWXy4vbcY2jXFvfmSN7uhAAH4Eh1WeeCIQ46LKGZYoRd6sSYpa36oMj48LkmpCA65nMIVCnObqjKWDbIB6fwD2Dn_zUtQe7xewNbbi1bjMlaSvb82ggduC8pY5BLFXC4DJz0Drm4M9gSVMdVi4sV1ZCWwQB6QbKkXlNMCpjFcX2A50YG10Yxr2NLAWTVIr2D1Ue4WonwCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
درآمد فوق العاده 200 میلیون یورویی باشگاه رئال مادرید درپنجره‌نقل‌وانتقالات تابستانی امسال.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/persiana_Soccer/28916" target="_blank">📅 16:03 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28915">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GgVVEDvj89V2-Nq9R1vDYyzSTxu4J960xlCEkqQ_a94mcog6tRAgVUzj1Cv3ZQGCFEMxCNYQ6OAUv5c_mArglqpJW3AdShQUwjOFcYCAiNd9sJF86if_9DqxHSKqJa0kxI3DSdtdM0nx7MpgKVdfw_LyRBeS4lnpyMfLjsvqI6cljg3GfcUC2iWpb2B2iZnsj92T5ZRapo1RHN_j_F8bs5sFzKZSn62WxhXS0EBTE03AQ7-YpvSCD0dUDZzcJf5TL0axAxnPYGyOlJadkOGGYTx_H94dKAqCc8_80Q_cY68RQgySJb3oUOe6-ROtOdehJy4YIRF-sFdnlyGkWOwZ4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پیتسو موسیمانه سرمربی سابق آبی‌ها رسما سرمربی تیم ملی آفریقای جنوبی شد. پاکو خمز سرمربی اسپانیایی‌سابق‌تراکتور با عقد قراردادی نیز سرمربی باشگاه مراکشی رجا کازابلانکا شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/28915" target="_blank">📅 15:35 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28913">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k1oKnuRBp2Rwn6ZJmIlMgRUAdoSvAAxziHGrg2edd-tcdZofyWX5ZDdWR2MQRBQ2UX_nq0NmrXCSpltU6Ox4CrGYbHxGuzBDG-A3-70YpnPeWR5ceAjssdaqARQ0mc96hEdFy9HH5uTsgnVPtN15X4oV2bztgeyWA7kkhjRIAo1afwxZ367CEA-fOJZBBqeEtRCJgoGB6DR-Y4-1R5Ij6zAy5LbW3VIZgDXMcM8yHIEs7g0ehTrUMTvVJ5p3_N-OQiwjjjkt7KUQ1KcWiU0vlV1-ff9ec4Tza-10iCen7E0iZog81zIjzMZGfQ_OPLbcFRH1WY960spTQDEpeHV_RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tYdVMbftUpERjLGszM8wHQ65LSTbPh1VEgiDMMIfVEeLTQmaNll1xzT9Mv91wCWZF9t1soHqd8TmXmpkVoWgftlv_lHGfJllkW1RG3sBuCfOoz9w16BbEIYIiOHfRgQTFOFHdXAMyFZvGRHCtAcXAonhlAo2toxanv1LTyLLZVGJkx9xtj1sh-7Et9L2zeoZEQCKQq6o3ppjTEUOoD-9ENubuTtP99BLLXQPLM60gKmhJjZPDzxt705HapxIIAjf5V4dBoFDrgw-q3TM-mD2uWx1U_jV2ncbM4I8zOjVZ5yotMFuHlvYkrwOCdNcDynGsMFZmOZUEiUS01LL4RQO_g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
کارنامه و عملکرد دو تیم استقلال و پرسپولیس درفصل‌جدید رقابت‌ها پیش‌از دیدار حساس امشب.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/persiana_Soccer/28913" target="_blank">📅 15:14 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28912">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IKqN5mP5ts3AqKoVIiT5eze2XssBXnsNI82LEfoij_V67kH8p0-q-CJPWItgFxkky4H1KdxEK38BUOAUtZwB6zWXrqaJwuA9s5GKtAbgxcLU2BrafvAbJNP7TfhjamZIVIwEXVDqEAVmxxKw3RAAKSZMrrccig5tobFD7a2R4NjhAu3UP4xHWMuVmU5gkgUfwD7jkP6zuoqnZ-F4oyI1mijB-D8w2iXbITS-QeqKk6BSKxuDTEOCiTYSf3h9Y4ac1ttgsGcv6Beilv6IJ4Nrw-aBSwsaVPpCqyOjwmsAAftM7dknMFto1SQK9_yYCsDc7ls5RX51_NPgWuABMyLtBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
کارنامه و عملکرد دو تیم استقلال و پرسپولیس درفصل‌جدید رقابت‌ها پیش‌از دیدار حساس امشب.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/persiana_Soccer/28912" target="_blank">📅 14:45 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28910">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZmfLKsAGRqpp-U4SX4AugmF0W2jR6QmfmttiAYUzZzrpWHyUJLF_lUST6AQz9yPJdQQk_CrRWtgQwZ78vCpPxDZ3geCuygkJ6UBjnFj8JFyylumFb1DHD4vmOZCTnFkFoN34Kmq064BC6PbArAYaE9d9sA7lyjA-jGCzcDSfJK4schgG06pf3ifbJj4v4PgVh22fkMIJCiFL7I7e8YlImN07P32tHO-p8VDj6zUYP7FcCXCIz7lpw-yudlNtE6ZT7SDsmBMVd1f1uRKhTOzQwR7pWJgfuSvHNEMeXIsSROh-WA3NqyHTOoUs8C3DWV3L641OJ7e5bOOk6Uberg6Wmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
عمق اسکواد بارساِ هانسی فلیک در فصل جدید رقابت‌ها بعد از جذب ژسوس و اتمام نقل‌وانتقالات.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/persiana_Soccer/28910" target="_blank">📅 14:11 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28909">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/abd0f14bbc.mp4?token=DzDpX7togeL0B16GUIdYbxEWkXmWlS9kuf_eTYza05Z7P_Dj1DF3Ab7VW5VJX8nnL73mqVm02ZJzbUADMnH9xouz5fSZCaJ-VfDb66Ihh3PVie5A71Y3Gp0vLsAfibaWgZrLOvVJsZVrt3cWguk3B3w5bYYUvoxP3U8t1bRJAb3xyz47YqkCvseaE-winc6LdYABA28lo5jrspg2NUQSs-7BFSWOV4vjs4RtWJMWVMiMQyi-ucZbsjhsqckcE_A3HS65zyEZihozwLxiPsvl8P8maneIWtIH81K_x7FR1RXBekpM1zSQxn93f77FghdqT1niWJnURfq3_edmT9ZUmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/abd0f14bbc.mp4?token=DzDpX7togeL0B16GUIdYbxEWkXmWlS9kuf_eTYza05Z7P_Dj1DF3Ab7VW5VJX8nnL73mqVm02ZJzbUADMnH9xouz5fSZCaJ-VfDb66Ihh3PVie5A71Y3Gp0vLsAfibaWgZrLOvVJsZVrt3cWguk3B3w5bYYUvoxP3U8t1bRJAb3xyz47YqkCvseaE-winc6LdYABA28lo5jrspg2NUQSs-7BFSWOV4vjs4RtWJMWVMiMQyi-ucZbsjhsqckcE_A3HS65zyEZihozwLxiPsvl8P8maneIWtIH81K_x7FR1RXBekpM1zSQxn93f77FghdqT1niWJnURfq3_edmT9ZUmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
به بهانه دیدار امروز استقلال
🆚
پرسپولیس یادی کنیم از این سکانس به یاد موندنی سریال نقطه چین.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/persiana_Soccer/28909" target="_blank">📅 13:55 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28908">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PoQirxF4A2YfRS6NniwAFAuoynRG2TBiftikp7x3Njb7xu6R9uAc3Xw9833Qa1NKl2Enb2RkHZh37-eFHWivGqTkmvf03hj_kvuo10OEN3Wp1VtfBjUlaxbtf_84ppeT3p43bOFA4UQpk1wdOshsgTRC58yR8g8HCP5xTEBsHlHTk7UnANLhJZJaZpd01wVDXSOpHw1ovwuLEx3bxdamqySyOkGp2mH4aIz_UUm97onNCxLTlSp6krnslf4Xxy1TitJuA76UZZm3lvIUN1NISGi1BfJFUZfxcL1YmG45LVg7t9pcEoxnfnNhPhfj6Wvhrv7I5Z-6_a_zDNZpB5iNkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
رکورد داران بیشترین تعداد بازی در دربی و رکورد داران بیشترین تعدادبازی بدون شکست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/persiana_Soccer/28908" target="_blank">📅 13:41 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28906">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/E1BWY7afdGt91orDKDEKBy2DAjbcouLyqugvb3m7yfWeYfRsrv5jOd14SFR5kIC_G7UWsThHPRSoSk69nauXFJ9PBuHmlyPQXaFV3JW13d9btLeIMtZ8Aw66AUFmNMQCokSqc17MlYxdXCm47f-j13w9L-iheS9scX7LRkfq536BBzF1KyubSt5c_nJ2-5FYdsU3Iu2peD9EAAOZoWuWvIv-Kq0L6FCOyujcFABnlbbLZ2Hy6mY61fi2fky2CW4eRIo_AD72kT5-ZuYM_-cgQSrq_vvFTrRCPJP7NuHiNuw2ij35fiz-e0ZmTPs3-g1Fp-3ZJSk2UPqgyB8RAFeIMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d_Iilv1hkrdJEPOm7rkiXtbl2jZuvfpWbX-0N3g1pdqX6yfE3VmYeIR7uWKsg5nHs3j5TN-DKLWM2oBCQKeMP4DrECY03TV8Qs9AFUsAq_DaaZHXsMP3sB31MNgMONoZKLq4MuTYP8yS6XwS-5LVbFKqrMJYbjdH4ge99dVO-AUsOLzuWjN6aYTI5l7vy78UtYt-4ekGJ9X52-0BxqFdRIG1HQzDyWZ-Wq25Nc6Zv86wl-JtXwqgcoINpzjh7J3vvKFjG4j1YXQQC5ZMqNIX4QhLYDd6VUsE13-BZMOl58A320FOmPbUeIfKMNEaoj08xKsUq_R62L95YYJtZXdLiQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
رکورد داران بیشترین تعداد بازی در دربی و رکورد داران بیشترین تعدادبازی بدون شکست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/persiana_Soccer/28906" target="_blank">📅 13:29 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28905">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pjjuRz_65LsTgLacJ13MgyD3T-SyWdMx8Q2NC_rRmTiP-zobDKWREoRZ-lRgwv_eSQxk2GVcVjyxLnJsrZBD086yOPxbJIgQeTh3mlY4yEOkPcuCb92b3VEM63kHhGsKEKyeAI54TyeKdprpa4tkq4JcSyFnCqojAfY_qSqU1kr5GNgBBTwieqCoq1yawh_4A1WpKg11FGvjHIJSnXKMiGvV6tkQqMHi2xsL27kXgClkjQcsI4CnglcevoH6nBbEKOr_iC0bk0em9NZ6OBWby5m1zdpKy1gECYupc80wALJJyKQfx3ijUDhstGHJKQERgSwJZe-2obmIJd9-Tn7kZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکرین شات بگیرید و نتیجه دیدار حساس امشب دو تیم استقلال
🆚
پرسپولیس رو پیش بینی کنید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/persiana_Soccer/28905" target="_blank">📅 13:29 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28904">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VUdcY7O0-E6h_Ip-d8Dh686uQaMu3hFJg4fPgDCZaWHrBh5AsRopbqPk0SJD-GidrLoV7LUAIX6yv3JWwwM8SECOQaIDRPsO8m370jcp0vG0I5lF7eGBvIL8u2wPbkYIHXuHjFawQ-nYf8imTI5ZsGxYPdXOrGBGM6SqOfHGHUDTanEFHIf2BLbxB6yDSScDeOMtQKCQ8KKPYSWiuUSfqnXgGgVLe2rVrZJI5it2Vf4FfRSWJH_O2pbcwUS5NIfRZy6B0D1_YvtO2VoRpKa4pz7AQl9xWZTsBjkJ3PPhlymchQ3ZF0ZSwL2_O_Mqhe2ALk6B-tK3_cWn911u59gNCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
نتیجه دربی رو پیش بینی کن !
استقلال
🔵
—  پرسپولیس
🔴
🚨
۵۰۰ دلار جایزه + ۱ گیگ اینترنت یک‌ماهه برای همه پیش‌بینی‌های صحیح
نتیجه بازی را تا قبل از شروع مسابقه ثبت کن.
🏆
مبلغ ۵۰۰ دلار بین برندگان تقسیم می‌شود.
🟨
هر برنده یک گیگ اینترنت یک‌ماهه هم دریافت می‌کند.
🎁
جوایز به‌صورت
FreeBet
پرداخت می‌شود.
👇
ثبت پیش‌بینی در ربات بتگرام :
https://t.me/betegram_bot?start=p12_r4EF37DCE</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/persiana_Soccer/28904" target="_blank">📅 13:29 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28903">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I-mq3l7y1YHjmBvGqDptE-3jpgoSFZ7ZcMYYfPLJxQdBUZlI7s-SS9SfblQ67sFO89LhstBXEzwhwn-7Qklsr76zvW4bPVi2cVoUhprMjpI_l0ymLz2RImarjDG7N5YQG2bRzetFfdmkck1dNn_BV7h8DjSNtQmNbqf9F4GBzg2GTKbBhKPZ5vHcimgOFjgAs6b2zP8kQXJidCzuI7Z3rVWfOj8i7gEFcr2p1il_yQbNFgHriPU-VcWRUVS0IcsrJw19mVl_FwPhtKhR61HbmWHh5IhOoUmSiW-m9lCu44EUX9MmF5lKBwhzgfotU_Rzsp4bah0jhEP-MT-LMrECRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
از ۶ روز پیش که همتی گفت ارز به اندازه کافی داریم و توبازارمیریزم. ۱۷ هزارتومن رفته روی دلار.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/persiana_Soccer/28903" target="_blank">📅 13:00 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28902">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c042e7e205.mp4?token=ClwbLzflFP2nHh_I8TlgDC9yEWsVnO_2jP9ESTGvGaz8hgqSvRwj7mCxqV7h1zNhdrVcM5rxJLsJZ_oEGMnvITGaeiHYBATnxKJujztkA21qElKbqTbCLttQpKtYxPR1v6vFNBxysHIGsjbJ1Eb8fMcf7pOrDkoVCtr5D3TafPTxottaqcKaW10sJJqY4VVAdSlPg-IZPc3ANp6JLJabRjDrZe-tG-rti-7uGVM9MmCOfPvKhmj9wA3UUs30uC_LSvsTM3CUflFrYgAI0zHh6K3gQROUeOyRqW0q30fND_bf-VSb4uCTEwoI2eftO2DRm94oG8vdUwcRh3RFNvjdjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c042e7e205.mp4?token=ClwbLzflFP2nHh_I8TlgDC9yEWsVnO_2jP9ESTGvGaz8hgqSvRwj7mCxqV7h1zNhdrVcM5rxJLsJZ_oEGMnvITGaeiHYBATnxKJujztkA21qElKbqTbCLttQpKtYxPR1v6vFNBxysHIGsjbJ1Eb8fMcf7pOrDkoVCtr5D3TafPTxottaqcKaW10sJJqY4VVAdSlPg-IZPc3ANp6JLJabRjDrZe-tG-rti-7uGVM9MmCOfPvKhmj9wA3UUs30uC_LSvsTM3CUflFrYgAI0zHh6K3gQROUeOyRqW0q30fND_bf-VSb4uCTEwoI2eftO2DRm94oG8vdUwcRh3RFNvjdjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسکرین شات بگیرید و نتیجه دیدار حساس امشب دو تیم استقلال
🆚
پرسپولیس رو پیش بینی کنید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/persiana_Soccer/28902" target="_blank">📅 12:45 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28901">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hI-SfeAuelk6Bv-WBe91PWhlk0Od_45W4OLrR36KcXi7MEvRtfiKO-qZ6yQBpLXjjlBEjvp8PE8AbW3mGnp7eTOYeYJ-eF45oo4oMO8pnH5IBI5hpxKvchczPFNGeNM4oOSzQN_mtucbx1GbYDy7rQeAZZc05RE5IwRt-bXZXKvZBsO_Kn10kVH0nZ2HYIaLyFZChiPxnPiL-RZfKKt-8va6b1O-9kAavr2e7TaFsP_lpXnnJOYCv7ZFZhLu3n0700PTiG_Rt4bXOtypSHk7dcehztgUwsCsiPFOZh2svBZ94jw-1qLhflQQcWUvYBAh9pruDDK7x2as0OCRQsYMQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
گرانقیمت‌ترین‌انتقال‌های‌تاریخ‌فوتبال‌جهان؛ نیمار جونیور همچنان در صدر جدول؛ انزو اومد پنجم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/persiana_Soccer/28901" target="_blank">📅 12:24 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28900">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eAdtol_o105m8629JyffgL67mxfPx3TcfB45TshkWpYiOlTyz9_fQzBTuI3jPw_vt-9Xwmz1gMqRlWVUS6khj2rtMm_CJHX_WMdZQnjHSRGLPERLiRfx6Vel3xOQ2p0_8gOeRd_i2rHzXMez8j_vpTLBeyS4fl4spWgvgxTWLx7DSCbXD9GYS1TYPCcP0W7hmIRNw5f-ssB5nuCA4JHqly4_GTcpt-6BGcqvyruhMjXqWomoZcU4QwXiduZnTuLoVVQYLWWwkq4bvZbNmKFU0PXGZSE4yNSQYa2EtczdznFrCiyIMhzTJV-Qp0Zv7tc8yX00XsmmLfjaae85qGfu7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
لیست‌گرانقیمت‌ترین‌بازیکنان‌لیگ عراق اعلام شد که شرزود تمیروف مهاجم ازبکی‌سابق پرسپولیس با دریافت سالانه 1.2 میلیون یورو به گرانقیمت ترین بازیکن حال حاضر لیگ برتر عراق تبدیل شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/persiana_Soccer/28900" target="_blank">📅 11:43 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28898">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PH_pYZaEaGXG5N-2Bv3wFtZa7qhym0BEJtiYp7luXUabby7iL35NFg45kGYtCYb3JxLVbg0j8lAyL8oke52jj8mFIciKLd0h3v6L5H3YUI-AZdyrDe9dQRg6k9faSIxhbZ9yVakTCQdz_UqD1VJ42pqFroJTRW0zYz56YQm39Z8pSyd26OJLz3Fsew0dQhnyKtEXmFAeG4hiNSa2KiWBbSGTvUe7WokFVKafkoOvq8Gp2SjLKpI5qYm5IuqvGIqhAFx8bT1WFqnb8kt3dhCU-Fw5o3ZOUxihgacqXtLGVlG7ndXftps54WNWoiTw2Bk2sy5GaXMhz2hgquuGbpDtBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a48b60637.mp4?token=qORR31bn63993aS-uMC9Z23-2xoHajplIdhkhSfDWYFE9Q6HFxEmUKat31X5SBF0vtfa9pgoFKnI2X3VG3r41ZAWfsa566Lgf9rMYcEdbIPnSDjPPfVZP5fQMA9Gh99zdNYYhSNsIWW6AC35Den08jUgh1iBPCvg0ie6OZX-0qDQScAXkIVCh7XwsW5QT_B3XhMIVdTI6WvXyCejdedYKJq3oLqGxHNIqg1iCMolPHZ57v3RMuOVSNnrxifcIu-SKmFKgEUIJrXkLPSASpGxT7W2SL9_0Ai5pjLWUKpcQmJTCpkEQ6XKwHszP6TatKDZ7Ji1zZPiQxADMedRlMXDig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a48b60637.mp4?token=qORR31bn63993aS-uMC9Z23-2xoHajplIdhkhSfDWYFE9Q6HFxEmUKat31X5SBF0vtfa9pgoFKnI2X3VG3r41ZAWfsa566Lgf9rMYcEdbIPnSDjPPfVZP5fQMA9Gh99zdNYYhSNsIWW6AC35Den08jUgh1iBPCvg0ie6OZX-0qDQScAXkIVCh7XwsW5QT_B3XhMIVdTI6WvXyCejdedYKJq3oLqGxHNIqg1iCMolPHZ57v3RMuOVSNnrxifcIu-SKmFKgEUIJrXkLPSASpGxT7W2SL9_0Ai5pjLWUKpcQmJTCpkEQ6XKwHszP6TatKDZ7Ji1zZPiQxADMedRlMXDig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇪🇸
نظرت راجب آلوارز چیه؟ لامین یامال: ما دیشب ثابت کردیم که نیازی به مهاجم نوک نداریم و همین ترکیب برای دست یافتن به UCL کافیه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/persiana_Soccer/28898" target="_blank">📅 11:23 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28897">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mfbWYz_xnPSKpb_Bhpgf-RxsvCVHP9izEMmLSluQmoAGnbeldoPw6qJmNq1Asy-MZ3GNv3qEjkkZ493SICBg_E81RTGcgacHnRpqTPJnyWwoT7QwTsrUvwrsAiJ8gcZmm5UzxWlbdBFB5asG-gIAF6pIJABNt1OOvc-1VbsHiHc_A9hmV-u_VhFYyVBdS-cPoS_tVl_OVcHXN4-0Zf1i6kyVtPiW5m5nt9DEMU1CHtEzDTwlWmDFPO9TBeLIirWf2sNSrrFTXqiChjVe6k3GU3v5IFb5twuDbm6U6_UgqqObDbBv1XzxffAhGluwpUim5AbNckqgm13NPzT4a1Tp3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ درصورتیکه‌باشگاه استقلال این هفته با عزیز گانیف ستاره خط میانی ازبکستان قرارداد امضا کنه بازگشت داکنز نازون به جمع آبی‌‌ها منتفی میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/persiana_Soccer/28897" target="_blank">📅 11:11 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28896">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J4d54BxREgtOon5HDV5q51Rm7d_wTBsLfHXPvnJ5i-wT4duqUDvvRO-WSgBZ3R8YzmT5bWVi-qckZXGXJfydRJE6rikjD5798yA_FmH0TFO5hHjKnk0kHAst3mHmgXCi_QNTdRO8-lJ8K5mpZMosma9L4gM-oCeXnehZ8jU0xyJysblBbtfWrm3Noja_FHX_hLNPxUn-JhxLv0PcRev_eS1CFtfApgcbZy4txRTU57rOV42cq_7MWPGQj3x3MXy_NL6Xptfn7gBUcpKk8Yhi3XtbVc0NO_CBj5nAjVZBrXV-g38dk8qR-H2TMR2TYFr41UlyKGxAFgtW1AyxtNQHqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
دو شماتیک ترکیب احتمالی از استقلال و پرسپولیس که به احتمال فراوان فردا کادر فنی دو تیم با ترکیب‌ها به میدان خواهند رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/persiana_Soccer/28896" target="_blank">📅 11:00 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28894">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j-Wxa9rb0icoXZcBl3laaxeXssQ8aKnJkabY25VUBLphuDZocW1j862ENzF5LYYkAOCGY2AB31fgjmaBNfvUC29sq42NSLosEcdIpaLBzNaQ-F8UgTYODKcbTgIM60-V7TNtgfqfoKSHnr9N204y-H8XI2gGbFLxbdjGMVglOfUrcRsLVtWpSksXQ9aIwkB5L2BclEY6p_KXdpIGKizUzxe8wPD_v4v48addsLf7RiOVVapoKZbSTrkzwgYf8K_bSZ7rRaqACGuolKc-qVkFoBJ3kh0_KtYsAddPVFryu6ZVPZWqj6N96xwy_o4P4IXr0zWN0TtgQ8oaWF2WrOKNAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DtsCVx9moxWWHwrDVS3IG87eYHFvyH2cdEhbkwdl8PRd1WV57q6IwI2CH__sbQei96mAvgsXHGy5ss8-rgw6UflGnXUJbmS7meY8qeDlgeMzOTweaW7gwkhp3BKOXvTgj0VKLCfXjcHTxs95d3a_9UaV4JCZlGYVP9KXhUDxo5GzNvNFHiJXHunlO-U9GiRonl254htAiLVeKnhRFVVMXR-d0OALXbqE1_YLQbmhs7G2gGTn3pUg3QyB__6XcMhQL1JxrPGaD7nJ2SIwVYwi3uZDWOvDG9g_hcRv92bJWpv-PsRW3v1VOH1KibmXrky-knaNAHThFB99AdT4gPISZQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
ترکیب احتمالی پرسپولیس برای دیدار حساس فردا مقابل تیم استقلال در هفته پنجم لیگ برتر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/persiana_Soccer/28894" target="_blank">📅 03:07 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28892">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n1tUWmZN6WOQSPzHvHo93WmWZ7rXdAxpkyxESwa8fc5pgrukGhRyM1USBrRLkPNdOlsXVuXzdgqRnmkbtL3thO3ZN10OSgr9z_6Z45G7sJLgV5Trf6mH82vwrsaOlo3E0nYOXp1ciHIqjxHEmCoy029p710vMLDEHb1dXFcSB_E8TZAEQXaHCSwsCy_yUrFeKn3EJs0OOZmws-xJP5dQX1EqxgOlhTsxnK2rmhlba_BWy2xf4Vuxc5RVh71PpS9EVw8CIOvmc5pM_qpGE6NrtbR8I2s-nc-f1eWUMAxnxz9ujXr5-QiC8BpmIFH0m63Yuau-bHScD6dO9oPhu_2_ZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇦🇷
#فوری؛ با اعلام رومانو؛ انزو فرناندز ستاره آرژانتینی چلسی با عقدقراردادی تا سال 2032 رسما به منچسترسیتی پیوست. سران سیتی 125 میلیون پوند برای جذب انزو به چلسی پرداخت کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/persiana_Soccer/28892" target="_blank">📅 02:48 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28891">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cbfb2092e5.mp4?token=pWWHH4MpHf05JuYF-3kB5Svq35qoCi7se8J6DL6JZExxktzqSthYZ5VhJfYaMmOHFiq4S9yrw_j-OiiO12Ts7o8NHms_W8r1KaW6E4lCxDW8ycvlJR8CisQrhu6e1RlnYwlpAxvjngN3B4mwouxuD5k2PyVnFBC5a37KG_rgoUYRGYH2pV-MxaDMjU3EjGQOrRYDzJw_FibYzwkOLXBKOnKhqv3eINXMethKQNxKmJzutbZDktoL2TCnGAGLjRTIMnImTcBN7S4qcu8fBTPd0hJWnUvoanH2KqiIij79eL4omf9iZcRYpJdXQR3C6YF4XKc8R14FKpvsQ5rMZexhxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cbfb2092e5.mp4?token=pWWHH4MpHf05JuYF-3kB5Svq35qoCi7se8J6DL6JZExxktzqSthYZ5VhJfYaMmOHFiq4S9yrw_j-OiiO12Ts7o8NHms_W8r1KaW6E4lCxDW8ycvlJR8CisQrhu6e1RlnYwlpAxvjngN3B4mwouxuD5k2PyVnFBC5a37KG_rgoUYRGYH2pV-MxaDMjU3EjGQOrRYDzJw_FibYzwkOLXBKOnKhqv3eINXMethKQNxKmJzutbZDktoL2TCnGAGLjRTIMnImTcBN7S4qcu8fBTPd0hJWnUvoanH2KqiIij79eL4omf9iZcRYpJdXQR3C6YF4XKc8R14FKpvsQ5rMZexhxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
محمد نوری استاد جملات قصار!
شاهکار جدید ایشون درنشست‌خبری قبل از بازی فردا با سپاهان!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/persiana_Soccer/28891" target="_blank">📅 01:09 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28890">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VXJtfX4NGMm2Lb6BpkScU_SK6mkBuq7iSrUDuJj_RMgsoJwGfRq_vaz6GZlo489EbgxoauO8knzGtviXnqDG0Umof1dRukYBX8dBVBb09MNwl1wZ5A69AKMatAvfE2BHVfK9uS2qbpq7wrGfpDEPmyVpHwQeoiU42v2IimSRd5QMyBK-FClTiwEGw4hQn23bArr-Kjz6rCgBB-BwzDW3PFwgMnnBmIabGl_zCz2WsZy813l7ZY_yLj-ocCo5nZK45fz2Czr6mbIqMga45K19F0IhjLOGZnSMExfCbRzXPvBlJdhUX-UGRgE1eXwB5A7tgWWoi8CIZkyH0nJSMOrUVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌دیدارها‌ی‌‌‌‌امروز
؛ دربی شماره 107 با جدال حساس استقلال و پرسپولیس در شهر اصفهان!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/persiana_Soccer/28890" target="_blank">📅 00:50 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28889">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RyBiXLe8qi4IUXvLOZ4010PpRwH162CIug9yYkofB4OiX9EIai6Du3WGlMod-rB2lxsNrPqvdu1xr78ioLbFLzoPnPKCICNgryODPXKsOuDJPhs4c1zSBUtKNaQxHmwoH6i1ly1iMVp4wtENGTVtT59UghFA_lIV3eqKhriWxz8gkOGqLWB9TUnDdIe3K3EAqTDWiuBssrtfNwPOVG3zRIWHKAx5RSjcgNKrMWZzFQDnAyGIjUuxroFF3LY1aSQV6j7qflk1jYXS6P0b1pE2YkxHDFrTdDNVE1noEZpR6cUIQsVWbNXGM0pITF1goUtRC0FD-m2B6KZVQTRK6DKaxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌ دیدار های‌‌‌ دیروز؛
ادامه روند بسته‌ ماندن دروازه تراکتور در این فصل و برد قاطع الهلالی‌ها در شب گلزنی تازه‌واردها؛ واتکینز نیومده گلزنی کرد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/persiana_Soccer/28889" target="_blank">📅 00:50 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28888">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h4s9xt-Rf_SPR7UxgwclfmCnRmpRbQPc41vlkBrRkmB25mV9fZfVAsrh8N28UJPpQySV7qW_URoY-BBUsWgHJzfo0-rzZQgs610ncD3Ouz42WkgqAO-SIKgcTRmRyxnuzatQ1zS-4aqIvybb-cDxdUPczTTx6NsyKFQBmcrY540jFecHOy8Xgk7cY2cng9Z9z3LyIGjURaEKpD1F4CW6pSit09DSJWq-6PxwyTF-9fxw-0Kc8NCj6jszVb1RCPN8GNkufmGuXV446ZkxiOp_T0JKwK783eJGo5DK7Z4UlxznsZpORekUmPDgMvMEFYhm5hCDFS2iGMbB73s097aoxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
بعداز دست‌دادن‌فصل توسط ترابی؛ شهریار مغانلو و امیرحسین حسین‌زاده دو ستاره پرشورها در حاشیه دیدار امروز با شمس آذر نیز مصدوم شدند و میزان دقیق دوری آن‌ها از میادین مشخص نیست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/persiana_Soccer/28888" target="_blank">📅 00:25 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28887">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DPT_a4hwlaiq4icxXOGeym4D1c3LqlO-QRgzu-l2CSZ9Z5ndlYQuuSXPaeukNei1hu7eBJGhSYpq9QRPuwGa-kVleBjUEiXPP6ju7Ev03kV6bLtyen1ey8eheOyi8v1xhOPPuaTSYYbKmcIwxNzVka3VHYetVwlMLYxOTfktxIzZeOOY7ALvo6DQIgXZCS8MjuOtBoRrZp3hV4VMCb7vH5EKpifE-uYMtCCydNqI-VoXZ4Qt1FYMpkhBjGp-ilshUBdcvmyXFn7_e1lJwjto44tywobpEu_sRDieNiWfB89aSw7loSWhOhtNZaID2rvkQQNpcPey-RO_nngP0MO3dA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇦🇷
#فوری؛ با اعلام رومانو؛ انزو فرناندز ستاره آرژانتینی چلسی با عقدقراردادی تا سال 2032 رسما به منچسترسیتی پیوست. سران سیتی 125 میلیون پوند برای جذب انزو به چلسی پرداخت کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/persiana_Soccer/28887" target="_blank">📅 00:06 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28886">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UNjuo6-rKFUKOB2dHrSY5R1bCDqJUpRhcZtPa3oIbMgEkTu0V1s0BPlHK50XmEgmKog7kpwIK4nG-NhJgN4azKUMQT7HF1Y_uSalQs9aWKNUv8d4NsYAQO1r4kiYDstFNV8pBK_9Qkbd4oqxlv8_mrZJvuOdXKpplo7JlseyE0YkhiIWQI9BphfqT5fCVQ4NWVLzQdPx6oFHFPURAA913KBhAPry14wPkNn7Fsh_k_XvdDM-5f607Epa77SOjt8CmYndL6GFp8J7hPOTh5KiKXHsJoUYPz86sPypGtoNkibLjWzaM_o-Pnn-XRHCq4brM_oaeYHLms7JW4HQvgV0XQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
لامین کامارا هافبک دفاعی 22 ساله موناکو با عقدقراردادی‌بلندمدت به‌چلسی پیوست. آبی‌های لندن برای این انتقال 65 میلیون یورو هزینه کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/persiana_Soccer/28886" target="_blank">📅 23:57 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28885">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gpBkQCqdkzhnd4qQc1NpDdwjulsbPxhRenVREOH15F6mbSHsegpSzU-uyvRr7ayTkWYyPriXWwTnS8tU9ujGz0_QHI0-rig34WKqPdEq473UR66WkR0o0T2Ot0tKIc1E9aaoer-PSzLssomuDysaTlPyGby-fChWCg8TmaI_fcqLhQKmpgPgsJnS26OVLhtK6rInASrVUCW8_wqFzgzr1vBR97iDmyX2hhh08udAexAyIIxJGOJKIkmiZDhw0vE2_7Fbm8q5YA8XAvzCw3vawdxVWkQUvr1T6fGkhcVu_aAvyNAPW0DY-_gkGEM2gS7x5Kp8jG04ZPtHbQ3MHUTXmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
شماره "9" های بارسلونا از فصل 2004 تا کنون؛ گابریل ژسوس صاحب جدید شماره 9 آبی اناری‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/persiana_Soccer/28885" target="_blank">📅 23:45 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28884">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NbLUiGW3N-nTssgoPmKQWNCFMdXtRp4uKKLH10woxRHAvEYr2EM-XG5OmWC6SorVPDMwKvbUSypnF5JAQ82lusE_0Z568RRvz5hwTLySTIl0u0VGkUWPvfYv0aQuilkQtFDYnFJejdZXdVz1HBLZnblFb3AakMs_--dgp3wdsh-zey86Es8VBZCsL6eBRcUNYXDvjV7sCahzUfdsaPgzwMdmgLnQ1M2qCkjgtsw-s4U-flzajKCa34rgKdwq3K1CCNMJ5tC_FYZd4WmEVP9mzZ3GFlIRegDVDdm21_X00f5oogebqounrMFjP6QapJRdluWi4yKulHzJwyqMk-RwTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ترکیب احتمالی پرسپولیس برای دیدار حساس فردا مقابل تیم استقلال در هفته پنجم لیگ برتر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/persiana_Soccer/28884" target="_blank">📅 23:22 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28883">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TbO07rQuBuHQF6cyFHGer25QUNN7LxbEatxjcIQAv1Wp6MrfymFnx4J56d6GQ2bzdKfdjCIfJ3CLd1VBaJl98CdxDG-ZGaAdq-K15WE6tbSakMgIlTFs9AkibArmothkCX63zkcLun5N_RlrT0F20cdJzGnnM5lkL89opMfv6CdFEblgtFLx3YN6lbbw64H0NE7AUq63mjRk9FtOcg81qSKClsxmCPKRfKCDM5YIAodg40V1iQ08ZUCqNl9y8J77Gf7_DUNVwScSRG0iXJNadisUXe3zwDdEGkTFsIDXebg01TIeiOV7Vv_MPbHcQrJnXNCUDr-wSGSKgBJOqmJwsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇦🇷
#فوری؛ با اعلام رومانو؛ انزو فرناندز ستاره آرژانتینی چلسی با عقدقراردادی تا سال 2032 رسما به منچسترسیتی پیوست. سران سیتی 125 میلیون پوند برای جذب انزو به چلسی پرداخت کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/persiana_Soccer/28883" target="_blank">📅 22:46 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28882">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ao1O_MAvNk7Q7uFmBofSckWlid5oYlPW2PRc1rr2B9Fo7IDd_8mVV0s_SmUY6Kj9tH9kkMeLWK9U4Ft5_C6FQmZ73wZZi5NEZJup9mNMC61-wN0ZTSlqLPeUk9Kwgup7-UeLlqfWsrYQxKERlzQ7ygt-7Bx1LqS0uvaBniIgS3mpNCABIADJnATXqWquHxNu9sEjA3JVWJ2FREMKyBE0RVA3YvGpJsflbfN-UrCWlS-Sg-v5U7NsvV00DjVYSAWbRKlTbM1ugQ6bgL7Y4TN1Soa_2iR8PLaQXcLHTqFHHLV4X_lak-B9OAmwn_1bcu1L_d4IxvCLnBsGyIuZ-2MCQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
به‌مناسبت‌مسابقه فردا؛
10 گلزن برتر تاریخ دربی تهران؛ علی‌علیپور تنها بازیکنی از این لیست که همچنان شانس گلزنی مجدد در این دیدار را دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/persiana_Soccer/28882" target="_blank">📅 22:35 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28881">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ErRHNEIX8_d_uL_vu5_r-DpFy3DF_tLwARv2nj77n7YpnbMAkFghTM-yzuQMaTuPIQdGiIOMzG588Da1tGzDG9LKRiwM1oQTUXNsBTUDIjVG6vCjJ8G_s1mqIfkzD-0bHkMU8l9KTNj4VlgroJnLYwF_jrrhWJiQw_bNmIJyvMOSxU8YaXt6GNjxdg2XSJc-5Uw5lb3HZe5lvHIkrfGT6_yQcgbseaz9OuLnYaIT0xjY9YP71907cApooJDeEbsYshlPbMxOAiVb6VrXxdQ1O8CeQcYPEKgB_LQjDjiuqb06BC6vrikAriNDI5h7SN4YGk0cIGOnQxK371uqnZcwlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌پنجم‌لیگ‌برتر؛ توقف شاگردان جواد نکونام  مقابل نماینده قزوین ایستگاه پنجم به کام بقیه رقبا.
🟢
شمس آذر
0️⃣
-
0️⃣
تراکتور
🔴
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/persiana_Soccer/28881" target="_blank">📅 22:01 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28880">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b85bfda8fc.mp4?token=soVbW-I4TljKr0qh0cYGHFOGx672M8JYHfJQW6GRUMFYBrK1if1uo3SW0EOlfABw4kzjwCSSsk8Bh-olehL2T7RE4AYn2y0ywHlszXO0-LScm0QGT8nejziOdcVbwfG8z7PmTCye_Gao6R1pY4ieLjJalLMdCSjKvNMQ5xYeeAcpK0zALKYenO7xMEtdfZxIJ_6XD2z0d0gAgXq77qn07re-XByP9qvAMm25_P_tMAwEAYPFLq5GMZlWbH03ZZZk5fU8DCU1LfrLaJEOnp2SgkJ24JjuFlYlFfC7VId3TZlUHPmBnmP71jOPRQaRKkO4d1QQkEAUpeT5U21fNRj_Vw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b85bfda8fc.mp4?token=soVbW-I4TljKr0qh0cYGHFOGx672M8JYHfJQW6GRUMFYBrK1if1uo3SW0EOlfABw4kzjwCSSsk8Bh-olehL2T7RE4AYn2y0ywHlszXO0-LScm0QGT8nejziOdcVbwfG8z7PmTCye_Gao6R1pY4ieLjJalLMdCSjKvNMQ5xYeeAcpK0zALKYenO7xMEtdfZxIJ_6XD2z0d0gAgXq77qn07re-XByP9qvAMm25_P_tMAwEAYPFLq5GMZlWbH03ZZZk5fU8DCU1LfrLaJEOnp2SgkJ24JjuFlYlFfC7VId3TZlUHPmBnmP71jOPRQaRKkO4d1QQkEAUpeT5U21fNRj_Vw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇹
الان رونبینیدکه بازیکنانِ ایتالیایی عرضه‌ی صعود به جام جهانی هم ندارن، یه زمانی وقتی می‌خواستی مقابلِ این‌تیم‌بازی‌کنی تنهاتاکتیک و راهت دعا کردن و کمک خواستن‌ازخدابود! به معنای‌واقعی‌رقباشون برای سلامتی ورزش میکردند. این ویدیو رو حتما ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/persiana_Soccer/28880" target="_blank">📅 21:50 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28879">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a6SdjR77slsf17wpi_0IUCDzmCG2KqrmyJgOvcqv5JeUvVRZpYr6rptKgr7xv5gg1Arxjz0agEKM30Uvf6BQoLMAT_1FqLeLgthXSYVXxsBVbm4VK7EYxSmsVyleW_BW7wI3tM-NegOlEW4pRw6Rse7CyeWPMTQ7F842bnbif6p2cOqZ7Xinkgr93rmy3GwcOPQR2BGFk2z68kkgxW7WLbcrnpsTboSGPzplLPHH0sGwpRzXZxLZMo7Us36rPn96Mnho9HU0vPYcsmEmxgaVCbRk4XAAX7VjZYZqVDM_4qzVKnIjZY86WWWYTJ1DoUKnoyUN7B62ybnb55nG7oN3ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
به‌ درخواست ژوزه‌ مورینیو؛ باشگاه رئال مادرید قرارداد دنی‌سبایوس رو رسما فسخ‌ کرد و این بازیکن بعد از چند فصل حضور در این تیم جدا شد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/persiana_Soccer/28879" target="_blank">📅 21:25 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28878">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WHq6Spw0TG1uTulRWxFvLwq9dM_6T7izWmmqHSvOro_uM_ymzV3Pz5MhxF__Kxhdjh_0E211-UmWfsrGDt_ArdSVYaP6n2zHw1TC4vlKs_jbNX3104fYBD8e5QJjkS1lTyyZCA9s4JhNQdY6gQalHVWWEucIX69AU_xFlXppcEHODdsrkiCFuhxxKau2hX76IUaSF0RoeLS8bsjdHgaZKfAHWRT2AJ9te0hsoQh2v7ntC-Fd1rjTpSYScWciJ6sFkkjnxSxzCiFSVv2A3a0rQxj8_xupHQuIfpq2yXN-3E4X539B4GSj_8D81SjrP1HCKGm_Aj0GaGFv4uxtTOAGUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌پنجم‌لیگ‌برتر
؛ توقف شاگردان جواد نکونام  مقابل نماینده قزوین ایستگاه پنجم به کام بقیه رقبا.
🟢
شمس آذر
0️⃣
-
0️⃣
تراکتور
🔴
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/persiana_Soccer/28878" target="_blank">📅 21:13 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28877">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af26bce4b8.mp4?token=FK0-rhI66r-4h9xHEBF21XoRB7OjSVMiwoZrlhJvRo_Qsmq1HbeNkZC0E5CY_tqwGTDMG-xoo30dzC0X_VD_uTmqtgXQTeX5r1yknA5jCBXVXPJC3oPYfNmCeYrRlQQ4K5scpdJ4l1KjMwb9DA5HtqyAAJIw7fZ-hXMINpIkYIO2LIH8drMimV716BMWUFrOThDBu_h4yQZZD18q5lW_dy1GJv1sxy5-83LJRq8E2H9gK9uDETvUhyUQtbH_46-4ldfbXRw5yiepZLiZkfV2pznXQ-MgLOhKh8B-zpsJ0YXEf7eMGJzdHYPv_b8f2wRDsGmFnh0DzKJymsH2ngpfDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af26bce4b8.mp4?token=FK0-rhI66r-4h9xHEBF21XoRB7OjSVMiwoZrlhJvRo_Qsmq1HbeNkZC0E5CY_tqwGTDMG-xoo30dzC0X_VD_uTmqtgXQTeX5r1yknA5jCBXVXPJC3oPYfNmCeYrRlQQ4K5scpdJ4l1KjMwb9DA5HtqyAAJIw7fZ-hXMINpIkYIO2LIH8drMimV716BMWUFrOThDBu_h4yQZZD18q5lW_dy1GJv1sxy5-83LJRq8E2H9gK9uDETvUhyUQtbH_46-4ldfbXRw5yiepZLiZkfV2pznXQ-MgLOhKh8B-zpsJ0YXEf7eMGJzdHYPv_b8f2wRDsGmFnh0DzKJymsH2ngpfDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#تکمیلی؛ نشریه‌‌بیلد: هکتور فورت برای پیوستن به‌‌‌بورسیا دورتموند به توافق رسیده بود اما مخااالفت پارتنر فورت برای زندگی در آلمان باعث شد که ستاره جوان بارساییا قید حضور در دورتموند رو بزنه و با قراردادی سه ساله به تیم رئال سوسیداد بپیونده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/persiana_Soccer/28877" target="_blank">📅 21:13 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28875">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/habtdRL2Q19-CpUW3xN7Vvk_BxZ-yWLNqIiKIUd9y7rmY-CbuvwGCInwoU_AuI4ba658DiQQOgvIKrQ2GaNbkdUikAMPauEMQPZ_x_NciVLmXm7RjsDGsJ410jwR048DB1hsbgp0xpOF_SfUblOww0xEHVcUBKmvRIqf4W6zbzzrFwQ29GqBIO-7STwkc9mm5q0kPzdXCNBnmiNbY4HSg0GyzCuOgkgWhty-Gp4eWstY0CAKHfb6-b3ZyyfkWgyI0Q1-8MsyWiRVoL-jW0BBVbO8BpTorAMKkfUu64CQwqV11CASaLJtQBiKCMR5hxkR9s_8jYVlvT6r84DoYMqNsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
انگار نه انگار فردابزرگترین‌بازی باشگاهی ایران قراره برگزار بشه. نه تو مدیا، نه کف خیابون نه بین مردم‌هیچ‌اثری‌ازدربی‌نیست. خیلی‌ها حتی نمیدونن فردا بازیه. مسابقه‌ای که از چند وقت قبل از سوت آغازش سوژه اجتماعی بود الان رنگ و بویی نداره. فوتبال، استقلال و…</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/persiana_Soccer/28875" target="_blank">📅 20:39 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28874">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dVlEfQsuWMt7472j2pQerFffzxWiMn7X_TI2t88t3YeOMMXw5Pyk40f70A0czXKFE6m1UMILFH-7I5OaXSyPhypIrrXVi18BCo45cGqSu89RsrBy3Bbwqb1pfUfefMWxFtUFluJwle_hEYGOr43n-CncKesebD4rQgbfinjliX-jPlZnGOZcdeGyMz2LMburnlmYxy-O1GXVKwTqYLuNBVv4eK5qqpm8g1zklmWLsS5uWTklMLoK6YKfagNP-IPUzCmB6voxxF9Wz--7-C-8BPJJ3_dBGuotR6-BL5Vg0-F1zA2MoB4HBsYdzCjScTEQmr21mvp4vi54TYXe7YM0Lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
خبرنگا رسمی باشگاه چلسی که گفته مطمئن هستم با ژابی آلونسو قهرمان لیگ برتر میشیم.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/persiana_Soccer/28874" target="_blank">📅 20:23 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28873">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O_wm_H06DnVoLgFDngxwJbRJHubVq7LjtpEU29NEdVAymNijFn9T3pi52KT51X10p0hYN5DVquzQQ3R8GK6-QCMwVLs0hJQQbG4dft7ZsYVSAhuFXpDMQUvc_JfLCbwh-iuj40vFPcKmD-W5v4eG3N76Uaks9oWKjqXHT9NUh0OkY0QiK0jLNsiIO6G3mCAw50z-Sgo_Q0qD35YGnAyu7k19L_lxNMhZTdGLpKiViuZSn7SuZFUr--WmWRj0peDqFay7TCFec7N6O9LpVBfUwKaY6JOjdUuDCSFP6Jx_CuNQkB6DDrq57wYgs8-gyzVz3s54xluvTKMYSQ03WfwxaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
بااعلام‌باشگاه‌بارسا؛گابریل‌ژسوس‌مهاجم 29 ساله برزیلی با قراردادی تا سال 2029 به این تیم پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/persiana_Soccer/28873" target="_blank">📅 19:48 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28872">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WICNl46ItVnBoAxxEKmM8jiTFEftaYf0WO7dNs8VqOad5zvHQpQWq3KHca4dEn0-WwX6qbxJhFmDu68M0bqKGCB5HyDew3dSxIayWEzwbJ0nG2DMl90UofK_gHTtT7rFOqz8a--FfvADaqtEwWqMt7093vrDqmZt5Aboo-pCn6jyY7tpTQZOy-W77sHu_FMg_U1Uo50GlVjPGi_VvIhYQVZp6lWLBhWAo-L05L_tN3W3EAyRmhbjFdNpCnAoHkMDM9oVbXP5gIj36FOVYoGMyd5bRq0MvnT0exSkApLSikgsfGAVngZOxiSDs0XXR-GwX13-GehmQdHvf8LDp-uQKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇦🇷
#تکمیلی؛ تا ساعات آینده انزو فرناندز ستاره آرژانتینی تیم‌چلسی با عقدقراردادی تا سال 2031 به منچسترسیتی خواهد پیوست. بند فسخ قرارداد انزو در منچستر سیتی 100 میلیون یورو خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/persiana_Soccer/28872" target="_blank">📅 19:21 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28870">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WKuai5DZegJ5kTulz3KSVfBfSjtzjH9Y3xBjLxnle-hVOr9YtBiG6nkbaVAV9px6rRa7RAqz89G8FqWr7-dWBEVH5l-w8cpxm6kVXf4eBLkbz9_XHD2aqki7Vx8w-Td9u_2wiG32Q7pQPm93yGPtUBLasJ3W70rAtmON1PxZg2oEJ6_0FyJwwzUlBK3qwd7s2gmhj4HS6ZGc8RyLiB_dxDczpLFQuchsKPwBsh8vr6KxoouiXy-pweludVoPYN8f-hv_SV7GpdZ-AahvFE_d0ERPaZNeTn0zW_omUIrLoPRJKmHOT9uSsq77QQsoZIey-Ns4VtKesJEWW2A-qTNUnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/de02X3br0RGr_pdVT0zKuyTx-0yLqcl8bydLcNdQLnX76uaPN-6gVOHVkqjSWigvR8Aj7DIpznEHt8Ne16ZsU7Ap3GrvOGb_1KMUAMtlBCYLaJh3SnsvRmKU3enn2RBk6bPKvqgJl6eNPQK9UazDmXm_J7IWf8VHmGay9HogqDl9m7gG6AXDwFOXBPyqWDYkqkCuImUAD3nkKve5-2NXk2YdUwxcSxUXduT65creyx4jI31mSmswYDJSAjwVzDFM9_pgXxOy4iQsZZUmJuykgivaSvSen0-UESpvOjKxuq03uq5tK8frGDK33fcLW2EoeYCLPkeESM_LwZgD2imWAA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📱
کاپل‌های‌ فوتبالی که رکورددار بیشترین تعداد دنبال‌کننده دراینستاگرام هستند؛ امباپه در صدر!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/persiana_Soccer/28870" target="_blank">📅 19:14 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28869">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VezvEDld9XARK9HMss14PL0NMlBrU8diRcIJidbCP0unabE-3HlRXbRc7yCxUuHwtfPBeADAmsQRqP3a3yIE3Agc9MGKDOfhVEmXNHEHzmapQgl-Z_W-bmW8BIXq2KmjmXqmKOSrGA8K_arBRlIduTs208KCyJYzmpY9WD2miRdOfjr1Pvv5PNrA-4DPxfDbZd4vBowTLRmmB45yfMZflME8ftVKF7N8o6fyeui474hP02K95lMwdLQdttt0ATffkAsK6GsxCyRqGXJ_fCVh6lJbn-jI_cZK7sPVYuDb4PKZc5qxqMzVcJ2TGHvb4_yK6PhScTPfgy6O3HtvEMmdng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗓
دوتیم بارسلونا
🆚
رئال مادرید روز یکشنبه سوم آبان ماه ساعت 23:30 در ورزشگاه نیوکمپ اولین الکلاسیکو این فصل رو برگزار میکنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/persiana_Soccer/28869" target="_blank">📅 18:46 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28868">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/omVldReXKSiW8BWblXPINFPw8xFSkdjyf7r4LeirQVw-GaPljzX0XZHwPa2dIwTva4SG17j1884eIDkzuqEp6y74nd8OwCPmQldKhe9Uh3muVe4F-2Y-AZcpJIw1ZMM_YmHgDLOAkCZNKlmVO6cf7tfHALNW-eKIORxvhKa2-9-tn0SU8xOqifLVBd5RtGow-0H_URDIpasIokLSkDko-XKu2ybp0p_6aV2OrTdurU0v5Srvln9NhLgxz3t3A3FeYwdi7PUd4fLILPqcBE28XEa9vrGSUuWdFakUXEaNHwsDyiv3B0G1I7BBurMZq9miMJtefkILDjPOlk5_HYGnEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇫🇷
#تقویم
؛ سال 2017 در چنین روزی؛
کیلیان‌ امباپه باعقدقراردادی قرضی همراه بابند خرید دائمی به PSG پیوست و با به ثمر رساندن 256 گل زده با اختلاف‌بعنوان‌بهترین گلزن تاریخ PSG تبدیل شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/28868" target="_blank">📅 18:34 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28867">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KzL2V9DWOSEiAfeA0VlInVbVDyawOheHOud6rS0YO70QRe0Rq1Qoq4V_5UbwAMg8LS2jkzsDr7G9PdpQwLkJLZGnnpkeYSeeZCJvnsvHf6AaG8hx30Wy_Zp43HbRZiU6Ba8zPENd-dMdhnPBl4hDav1s1jy478l_y1nHzNelut7KSAvQ_Fe98muRmb3CM65v46byUY8ufYv9U-c3GCSV_qo7xsKnr_bmgkNAQtPDgelU4edJ7CF1bwO_tWyAKigAgu_F3xIS8OSYS0HTMl8yoNBSA4L3EUqsr02g-pcvD9qvW1eLp8LU8wnFMJzeKZyZ4LmViSTkus4xdmu0FTyR1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌پنجم‌لیگ‌برتر؛
شماتیک ترکیب تراکتور برای دیدار با شمس آذر؛ ساعت 19:15 از شبکه ورزش!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/persiana_Soccer/28867" target="_blank">📅 18:13 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28866">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uiDjTOGzkXIAqZhAx_DVko-5VOhobIcXVGVZRJfk8pdkjrCho9xlCq2BdM5X3vr6IjFESNWwBJW2VTT0pdg4vAeIsYLjEWBg93GHJ0Diydj4_GB2n4SoJKHspWqWzeZzoe5xcTfehwMMwZ0TW_br4oHYL5PO0aTBWiKkNLo2cYF_2p-M7q82OXLcZvF3wA1Euk-6O8mmOkG3wG3WuijLhTXUyVQ4ZOGFBVphFbmHyuPM9Y19OqGNYuk3lxAwgaTAWbZfPR0NcvU44ycjji2pcyV0FN5pLgE9OOdvJgTSCeMBvF2A4Ojf30isK5tZvTaH4OLuKJmvMaGrZyKp0gWS-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
انگار نه انگار فردابزرگترین‌بازی باشگاهی ایران قراره برگزار بشه. نه تو مدیا، نه کف خیابون نه بین مردم‌هیچ‌اثری‌ازدربی‌نیست. خیلی‌ها حتی نمیدونن فردا بازیه. مسابقه‌ای که از چند وقت قبل از سوت آغازش سوژه اجتماعی بود الان رنگ و بویی نداره. فوتبال، استقلال و…</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/persiana_Soccer/28866" target="_blank">📅 18:06 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28865">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O3roCbS8qqA6o5589VwYO0KfceFNkVQhvmWQS8GSnc6eQM5Eg110ClsZFlSd132ICzZzkQPNER5UPCE3OdE-Lo3W9zUF4Vj88Bwcr9x2Ha4a5bgkKwL2DuMl11wfNIud7yXIT6glohXWduKjDhQm8FJueMQcJOR-U362PZHDB38GFV1bV6fO50FeVaqxhFEbSjljywysO4QRx-UT4kOfvUv_SxTfta_ZqsKaUffr86R4sxYve-rORNpF23uEmOa6JI68_ydJKIbuCaasmLIccd3Kbi09uU7XfvblnMNePC1f09gvyu3bkkKUtcCiC-DGOadix3tAyXVshkiokYdsnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
انگار نه انگار فردابزرگترین‌بازی باشگاهی ایران قراره برگزار بشه. نه تو مدیا، نه کف خیابون نه بین مردم‌هیچ‌اثری‌ازدربی‌نیست. خیلی‌ها حتی نمیدونن فردا بازیه. مسابقه‌ای که از چند وقت قبل از سوت آغازش سوژه اجتماعی بود الان رنگ و بویی نداره. فوتبال، استقلال و پرسپولیس به بی اهمیت ترین موضوع‌بین‌مردم‌تبدیل‌شده و این‌حجم از بی‌تفاوتی قابلیت ثبت در تاریخ برای نسل‌های بعدی رو داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/persiana_Soccer/28865" target="_blank">📅 17:46 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28864">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57ae770053.mp4?token=cn6KhkrR-JGgwGR5eO2V-sYOxRieyk_WfiaxBxoy6qgbhQ0jYxkCa6vNlL06WwSkBXoRB7vbuA956f2GU_mtr_BcKhfphuK6fJ1YZSagZ6aCmYmJhqFgLER1JuTRjZGeX3oIJ9g7_15a7FropMXmSI3Q3EWJh2zl0aukMl5jJCZgH62zg8T9RBYmEqAN5U6mGRhaOOBFRc4hBdarv1ONxDNk4ml4rF6mQA_LdaLgtegmUgvXpoEWl5-_Ry3AW7z0Ps5IO7v-aIs-34Ahfd5Q3ZgkudcPONB2415zVLaVfDNcJKW1g8Aa6eGNmNn5CjdYPXnCQ3hhZ9WNclLXAijS6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57ae770053.mp4?token=cn6KhkrR-JGgwGR5eO2V-sYOxRieyk_WfiaxBxoy6qgbhQ0jYxkCa6vNlL06WwSkBXoRB7vbuA956f2GU_mtr_BcKhfphuK6fJ1YZSagZ6aCmYmJhqFgLER1JuTRjZGeX3oIJ9g7_15a7FropMXmSI3Q3EWJh2zl0aukMl5jJCZgH62zg8T9RBYmEqAN5U6mGRhaOOBFRc4hBdarv1ONxDNk4ml4rF6mQA_LdaLgtegmUgvXpoEWl5-_Ry3AW7z0Ps5IO7v-aIs-34Ahfd5Q3ZgkudcPONB2415zVLaVfDNcJKW1g8Aa6eGNmNn5CjdYPXnCQ3hhZ9WNclLXAijS6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
گل بخودی های فصل جدید لیگ برتر تا پیش از شروع هفته پنجم؛ هر هفته گل بخودی داشتیم!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/persiana_Soccer/28864" target="_blank">📅 17:19 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28863">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A1ajqmuN0pTAo1fE24K3JUR_wTzgvP7AfX76vfMqjGeoIVu4ucADdDkjrKfMJw9K17-JxSjcbfwFXyoQg2wO-6syZ1PgeFrT74We3WKh4eYx1rDDEaBmx9FmTJ7arNavZwB8gYQUdOCbXVHXUIRZkyxRjp5XlJQjW7d0zvuNG-nQRBWiI1Dd5YP5wop54DLFR3fglPUS2rknx-3nrSFGVt9e-p69d12_J9q0Yn99Yh6Aj3bMemfKDJNMy5YNM4B4sSzq88h2Cuqhfz-pPQ77MwXN29ohpap-NnyEQhz-chHGOEYJ1VrkZCOnXwQ1oNpT-BwBmaIr-EzvmEflH3EW5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
بااعلام‌باشگاه‌بارسا؛گابریل‌ژسوس‌مهاجم 29 ساله برزیلی با قراردادی تا سال 2029 به این تیم پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/persiana_Soccer/28863" target="_blank">📅 17:07 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28861">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U6hvOS6crR-oiQPqs7xBK9i90q6SAQzS8M4-KSsJI62ucwSER5d575N1smRZXhi-OGxeeJy4JGuHwBrU_eVE7qYayprl-wCZzVMx43I2N-9BXd6QplVQemZbZ3nYukaRFkpooY78u5fOzJKGXPiG2kA6f_PGPEXbVyEPFgtK328ZBhZ534tcmsPaqnYtMkBbFJNo2D592g9chAtEHmGTfMWa9BOYGpgch6v3gh5Ict3MdpIcsYrxivL_WgzesJRqAVRL6SML-YYCyNkgEuNKOyo17n-cbdjRjY9zIvkFULISdfr0jNf0CrjeB-R-gxakbF7Rlh9kVvaQENmK69Q5RQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fWEV4Fb5DA1fjlVT-j9Rz27op1_3N6U7aGKKcXyGU03cx4uFNBOZUtHfY52IzNT_DZ2Eb_a3NRugx9_dK6oTX5qgLajRkWVYUbk3V1iiNg9PbCiZpjr4BReJ1FyXOHNw-uZShUpSOL37bN2wUPG1cGzFxcUbnnY8DlLoXIwwbyuIHEkRjntHsD4ctClFId9iW2j3_SMT6KjCsN_Ks8fcYvf606GaD8o8xDhhJSXRrdfN95WmD_tBNUTV3PghDctJ2Ma-lwPogIFJh4xZWFWej-FPGfTlNwsKBko-BMr-6Mb7AvhF0C_Arz1KD9Nc2UCNOZmCJ7zVxZu46TJByjUP6Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔴
خبرنگار رسمی باشگاه‌شباب‌الاهلی امارات هستند که از نگاه‌او سعید عزت‌اللهی بهترین بازیکن این تیمه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/28861" target="_blank">📅 16:45 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28860">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MehEFRUUzlESB3qmSEnjAiTYgrU5JJXFkeSgFCKcyADJDMif9mNje9Rovn27VHEyBxXRD5Tgt2dpc8Wo1ClQbMlrK0Mdhrn_7I1cnVJ9VOCOfjCBfoMmjJz4RtDeCWojwAZfSaV9eFZ9ISVq7u2guA3vGupDcH_lwDWV45eZxECXE4nCaEd4sTwxAeYcbCPe61Fknw9-EKG-PgNW1YNIK1EV3eqkSx5brYuP8cmrPjJIVnzVNYLJjeFPRQm3TtHTZaIeic_WPyTlBQF288wYcoCdf24hLaL_VcrQHyRMiHZRWMKrjbbexN651xEv-xHa-Jplxl6N0_uU-v6HyOMrGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#تکمیلی؛ قرارداد ژسوس با بارسلونا قطعی و دو ساله توافق‌شده. سران‌بارسا10 میلیون یورو بابت این انتقال به باشگاه ارسنال پرداخت خواهد کرد. تا کنون بارسلونا 174 میلیون یورو پول رضایت نامه داده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/persiana_Soccer/28860" target="_blank">📅 16:22 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28859">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mtLwpH6OJAEwwxc_K_QIjkYAnJjDIkprAht6Bs814kr-ioqRW6_2DGjGjY14-c3FSIk9xprPnoB11ZL3MRZaIWbazYd3hGOExvOQ5ROz7zqLTjYZQ5JElTzt2Q0A0k2iDrmNQ9RRnRZIUE9cL_-ONYgmSRCJ7EKi43-mziHRhxAfdy5fOGOHB9wzO4-MqnV19Crq2kVKu435gVzkU0_OEL0OhQpUSxZ6KuQc8XMSvsl8gr3DaR8RVQmArGPfQuVW7OzbIfPHO-JCx9zPmZ8_wlP-Kf1Pb_rGU2-rUoUDBP_4pGwCQ7wKD1by-oH-gkyAwHyItXt7QpJ53aUu02IQeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
#تکمیلی؛ لژیونرهای ایرانی حاضر در اروپا:
‼️
علی‌رضا جهانبخش: اکسلسیور هلند؛ الهیار صیاد منش و علی قلی‌زاده: لخ پوزنان لهستان؛ محمدجواد حسین‌نژاد: ریوه آوه پرتغال؛ میلاد محمدی: ویتبسک بلاروس: نادر محمدی: دسته دو فوتبال روسیه
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/persiana_Soccer/28859" target="_blank">📅 15:55 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28858">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ew1AoyYaLbBnz23QUyIbHIG6ZUq4bcvCIs1W0XdE_f2Bq0br-jn9EgsRag-zxpgzbsu0ye5B053Lqzw59WWeRyOjCu06LniPagIzydNgoHYR0xmfiT4i6ZHgYeTUrU3cb4Mvy083lFyj4buaqgs2RxeH_CnI9uHWi0YoTNtw_zxj8ojzca_LTnzf8vjj8F8yCkA2QQ1N1czwjuYiR5pwK5gAiSxLO0RmAB6mRLkUz8i9vxjAns3za5W7DzMpZiGcx0lMTrb-BgWVrZ9Kg4djO36FavYDalxwViZYUT4SZjONt4Bg-BREXyYCX9us5njHzafIubXOyCBLFBQd9MLguQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
باشگاه‌رییکای‌کرواسی با انتشار این ویدیو خبر از عقد قرارداد با محمد محبی ستاره تیم ملی رو داد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/persiana_Soccer/28858" target="_blank">📅 15:13 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28857">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OQeZfMs3sXhBWT27edsyH9-H9UJ5CZV86yh0Ds7Xee7nt8FXISRMaqAAJDv9ipebqg1hMs3umZys5zK9SL505XERrdf2M2Aaidx6G-pXwBQfLSUBRs2B9nnHjQGKDqCdMNLAua6Pq78gjxMM5wX59tLIBRXl-4itgTr3yK7odLDhCjRF8YqS67g9nkCBPJAQ2E2WqRPh17IOC09hKJ6tUqtO9xfsL6wrU4eOLhLiQE0RcKH_HHFJu8RFS-TeZ_ItD4seYi5BLI81hHTpnLwHMqjs0kxS-LciPbhChvkp7TVnbsyOEQaw7nO6LcnuqIxhZVD1WO6dMb_-PbpfiWbE5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
هوش مصنوعی دیگه داره کار رو به جاهای باریک میکشونه؛ یه چیزایی داره درست میکنه که با واقعیت مو نمیزنه لامصب. اینو ببینید‌!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/28857" target="_blank">📅 15:13 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28855">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d453f3d9b.mp4?token=LvzzBPjpu54yiIXMKeiJ0Fwjctq-OczraPpmpTh4mhPNAPa_Z5ikE8FY5NW3OZFXjMW8InE4jh4m0K_OKXwvB018L0iVJ3ET3uvXhLBqQJj4XnBdNecDjpiEqkGL37uW1WQiy37qeixt_qWHPaZCTxpRq0cWqwRDHkSXAg5t0_TDRU9nxBQN4bK2QdcBouGDUDTN4rp1wTCqb-EFuGffjtOstZfj5r63lCMVaomk4UUGoglzTqHLRo28A8YTPHzFfGftCSY-L0UIusNaqz2Kgmhgf1RIJ7slQGKzDnnSYUkRrAF_UqEYZdRovpKDul48zjJLS8rMc7YGw6dso1jjRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d453f3d9b.mp4?token=LvzzBPjpu54yiIXMKeiJ0Fwjctq-OczraPpmpTh4mhPNAPa_Z5ikE8FY5NW3OZFXjMW8InE4jh4m0K_OKXwvB018L0iVJ3ET3uvXhLBqQJj4XnBdNecDjpiEqkGL37uW1WQiy37qeixt_qWHPaZCTxpRq0cWqwRDHkSXAg5t0_TDRU9nxBQN4bK2QdcBouGDUDTN4rp1wTCqb-EFuGffjtOstZfj5r63lCMVaomk4UUGoglzTqHLRo28A8YTPHzFfGftCSY-L0UIusNaqz2Kgmhgf1RIJ7slQGKzDnnSYUkRrAF_UqEYZdRovpKDul48zjJLS8rMc7YGw6dso1jjRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
باشگاه رییکای کرواسی بزودی از محمد محبی خرید جدید خود رونمایی میکنه. قرارداد دو ساله و رقم بند فسخ یک میلیون دلار توافق شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/28855" target="_blank">📅 14:32 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28854">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UmGNEG9qvNccIsayYo8eEn30sVqviuQXNM1BiVm-tzgdSXi1Pf80u-SZ2pDEGMzu-NXXMh3TWpQCfavQfsE1Wenm8wzpGXa52eiQCfxY54TEIgzRX2spsKWyTwQyFggXheA9H-vpqhCMhvpl5PZYCSBlEyDqHCkfFyJ9HfEOEQE7Hi4yB9czv620LjKtLairY47QTEN7M8pFy7ZMZc71WESXQWoy5sZZq-QI_oapxy6t5YcZohEcfLv94IuVNNo61kfgf7L4rzTpBag1bb_V-532mVqV0GLxwxfQDKjiIYuRZpRUtv4fG-WlyC4gUiEozNZ0MvHlf2i73U96gAMCQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇹🇷
خبرنگار رسمی باشگاه‌گالاتاسرای ترکیه هستند که معتقده این تیم امسال قهرمان سوپرلیگ ترکیه میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/persiana_Soccer/28854" target="_blank">📅 14:18 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28853">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🔵
🔴
درفاصله کمتر از 48 ساعت تا دیدار فرداشب استقلال
🆚
پرسپولیس؛نگاهی بیندازیم به زود هنگام ترین گل های تاریخ این تقابل بزرگ فوتبال ایران.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/persiana_Soccer/28853" target="_blank">📅 14:06 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28851">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iHZI_jsoZS7QnZ2N4LN87j_b6A7-2KeMxwk-0EZfBCW7aaGrVOw7RGTU5EYKCiBpEGxcMaoW7-fjRSSbJ2CfviN9YXr0m7GcUz7AhVMYQzb1uUwcIp8-su-Loo_UmTOfwrcUo3c5veoJgilTT2dDEIwm0gaxwUiaolQa4df6-sVvOchhSSBdC37FmxsBEoX1JpT00ZGcvlym0yhAPpnojO7crfBzVuV-Oj8YeEGFETtFG92n9zlJMjoqIunSoSFb2-zK2U5ELxhWIHyW6qBndyKOCFu5Irtn2wSE6l2IoE4BbDCfxoEL_IEifhwKFbcbkskVs_iNHV2VzodDzlh8Cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XY1qhZTylZN2cagxZGRCkBAVsvw_YByQLoMAI1grpDuzN2nDFmqVJUCNLzJ7yQXR7MMpjyJqVxel4AkV9exXepHvuUi-PfXTgwHNc0QyBlSFbDv30wgVwI0Ez9_-7A8CcM28tibn7QvFCjTYqEUDlLl6od8a5OixjvvZZHkPN7E8wdtx_GgNJpiZGOeE7vN2_IwGeIROa68fvFqp32pkuAKlOzivvvjb8TzxzkCAM4gvjdw2Li9BS3RAC-86e9ilYKLnTFOORGd1hjGJmLZ9uTV7WoFdQq0AuyFH0zYFaGouheTN_fSclBXUUxrhVheDwR8XdD01nu27ZomYKN_8cg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی‌پرشیانا #تکمیلی؛باتوجه به‌ سوالات‌زیادی‌که پرسیدین؛ بعداز پیگیری‌های دقیق از مدیربرنامه یاسر آسانی بااطمینان‌ کامل اعلام میکنیم که‌فسخ‌ قرارداد یاسر آسانی درسامانه فیفا ثبت نشده و تنها یک نوتیس برای باشگاه‌استقلال فرستاده بود و هیچ‌مشکلی برای همراهی…</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/persiana_Soccer/28851" target="_blank">📅 13:54 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28849">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N4Rol8Hk7wW0BTGg2xorUZosLEY1ylDk6H3UjT8XZlHMgyaJ6FVErEVxgh6oX22goQqOyf_yAZ1WO0dGDeezRAkigUoCOhVhqNk2BR7mx-y7kB_Nmn_pXsenS7AM_GuuoN0x-UX2XHbdWICS3JHf2g-WPQ9A1ytmCjaKLo9W-hGmxRgbWNJkrfJr9oIrfSJI297LFgyX5o6CvNHQYJ-2eVEeeWeLh4_v0IqxzcRg_Z8JJ5Dt05xnFXMQKl8Jy5wuQe-pn5BCbhw9apSGA-Yyh7V9btkAqY9wz9vBH0wVsenluAYBfKhN-YysYFLq5P4H2e29cnSbf9dDHJ6i1MUzbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CRPUq3d63ha3xYQuqT6kFZ5aeFHmmSUnCbJ5CLUsh6_1s4wbwOEzpI4HFXLJPVhmGrjp5WisELNxKz28XGh5gI9Z1YyDoHljVQnHjopuvCGyo3ResxGcfx1jSFRfSjKZaUDCPyhSguaRQauDlwvk3ju1xQUujLL8Db-zC99qZMbYRkeoWrasYy2Eq5JF2pZtwzaMRuhGE-XMKv7nZt4wGaf4mHCNK6LoYeBW3IjZNy74HYc-iKiq2GorKMq0U0M40MIhdeTaWAo5ylQQ6YvSUyF8GkUkBzUjCyYqTLRM-bsc04pIJ7bjGSeysHoMVCp6LKSSd0S670p2Tl5ALjDeUw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
پوستر فدراسیون فوتبال آفریقای جنوبی برای پیتسو موسیمانه سرمربی‌جدید تیم‌ملی این کشور.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/persiana_Soccer/28849" target="_blank">📅 13:38 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28848">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kHztKsq0UBViH_iqpP_NBIj9mUePGqoUUgsbbz8WryI78Ibv5fANRpjnnAFr_zROJNC4a4iEKG16hoivUw7OOyWnUqIDJ3cXscaKs64fVkGQYXnzaR5NgsquXYZna8VsWCqV6ZHiX4TloxN0CMvrHjUUZiBXx7nUZjxygBIz7af8YabMsRClBhDOIGrYbKkF_GfMjAcXfU5mNTSMJO9BYO7eGhMxiGOgA_3XBNNIz8NjC1YTssdqI2HuRhufGhYbwN7ujtZ-bZaKlkZZn4FUxaykC6L_vLoLbMEjEOShDfv6R36lU35ar-2fFgnZ8XqZ-ECfh51_ii0k0JU-OLNHfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇦🇷
فابریزیو رومانو: انتظار میره تا فرداشب که پنجره نقل‌وانتقالات‌تابستونی بسته میشه انتقال انزو فرناندز ستاره چلسی به منچستر سیتی نهایی شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/persiana_Soccer/28848" target="_blank">📅 13:04 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28847">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P2mX7CqIQhhNG69OpOH3YbSMRbT_L72zrjyigrxkaiQhIoVp3oZGOaB5VwIEKtVa9JWlm1XU9_E2TA1X5-DpdlbTkLWIR8m8VpCjt2rJhl0-SfGbEvLk5mww6scZYbBAgC1Teb4IfVmvCUrpdNnYW3DoZOUW8z1DPO5IrHiTPisbljXg7UrZA77veVS4a7E_Emv6F9u7ijYZDxxxmxmT-wWuTKioQ7v_crZVpOwe_-YUK3h6llfV2eRU_esxmUrcJ1LNzQhrI34oJFatnpp21G95dcUmnuLy3jOJdWNCng6j7825jwsDuyd4zcSqtqr7_zRjcuyTj4DpFTT9siMKNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
مورد جذاب گابریل آرتتا پسر میکل آرتتا اینه که چشماش دو رنگیه؛یکی‌ تیره‌‌تر شبیه‌ پدر، یکی روشن و شیشه‌ای شبیه مادر که توجهات بسیار زیادی رو به خود جلب‌کرده. جالبه‌بدونید در دنیا تنها چهارصد نفر چشاشون‌دو رنگیه‌که پسر آرتتا یکی‌ازاین 400 نفره.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/persiana_Soccer/28847" target="_blank">📅 12:43 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28846">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tVrtvrCK-xp1nadc3IcWXVhQZTby8WY8DC69AJkz6NGC5HRKOOhkRRjGBIuIKbDRXtxNwU1M5ebw4fAEz55waOyG0P0QFXel2qJPUs-TrAAppzXw-jKyJ3as_Jk_RW-EjD7guxIi7bXNvDFW4FZ8EwR3tWHTnAzNXaGoYNMA-lwSvF0W5e0F1zG0VPsnjHYCkJcRAz8nyFTDd8eNO9UPxJU0oS15eqJxqd7Lr2r_FiJPbAV5BgLhYBWVD8k5HD_L0ZWWMm6XjvwnxhiYNAfJUONEQ2tGeVYATEYrcgb36agQAPo54RgwiNmGNjJhlCGnNad8akd2NseI-7svRPBplg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇫🇷
نشریه‌مارکا:خوزه‌مورینیو ازوضعیت ادواردو کاماوینگا هافبک‌فرانسوی رئال‌مادرید راضی نیست و به فلورنتینو پرز گفته او رو بفروشد. پرز برای فروش‌ کاماوینگا رقمی‌بین 60 الی 80 میلیون‌یورو میخواد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/persiana_Soccer/28846" target="_blank">📅 12:11 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28845">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">▶️
ویدیوکامل ویژه برنامه شب گذشته عادل درباره اتفاقات اخیر چهار هفته ابتدایی لیگ برترو افشاگری‌ های عادل علیه فدراسیون فوتبالِ مهدی تاج.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/persiana_Soccer/28845" target="_blank">📅 11:50 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28844">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gCKqARumYvgPlaDeVf5qiRNjLSRXvmecZOM2Q8dzhsEdroLiV8_G1_TxyaSIIHVyNFbFTxGsiRodYfIqNVKHYq7-vD0hW0Xee-qnUDD0Bcpg78dacis_J0ZutCmN6WRxO0Fqn4zbFW-G2s-mKLjZs35DFaesmIe_Zkn4Wqd3UgVj2mLxMqHFeHJTpiFxh08W8h4hV6TCcqdPXt4nL15qs3sg2RUp0_B_VGyShjkbnMoINxPeDA_bysEpMOTyzKxjoPGlokhAaRQUj9tUY3j29MdFc3OFhPH_REWPSgVJ7Jrl6YVdE80VlaLDJuaW0W_qObpsX6Lh8PthiV2O2Lcb3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇰🇷
دستیارسابق‌انریکه سرمربی تیم کره جنوبی شد
؛ روبرتو مورنو سرمربی۴۹ساله‌اسپانیایی‌ودستیار سابق لوئیس انریکه، به عنوان سرمربی تیم ملی فوتبال کره جنوبی منصوب شد تاجایگزین هونگ میونگ بو شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/persiana_Soccer/28844" target="_blank">📅 11:39 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28843">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KQ_FDoavO1ZFqBMuokC6qGfPCu7-5EEeBSYK7Js8KYq4-zlNGOnDFmUaW7F-QIj8aXOIHjGDehLDSOGxq_ZKbZkvA_CfmDVYubwZjU4YxkjNkaKLehQIzQqOH2_OKzIBUZ-2MiQi5uFbNSP0vlyevE3mgvUrsBgKqlYPEAE4Offonf1cwI8ZNsRe87DU-gIds6gns5rs2IcPmdor7CeaJHWIhbe9hQA1RnNxR4y4FNn5b85nIx8d0avHf9yo3EcVj0SnSg2aPMMURMbhntD4rJKnDkZmCLtlNJKNl7bO5e4_3pMNoCUccbHU6naiNMJOuHpN0rM_XIOXEB5uaDxG-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رئیس‌کمیته‌انضباطی فدراسیون فوتبال: بعد از برسی‌های کامل مشخص‌شدکه قرارداد یاسر آسانی با استقلال قانونی‌است و او مشکلی‌برای‌همراهی آبی‌ها نخواهد داشت. بدین ترتیب پرونده شکایت باشگاه‌ها ازاین بازیکن بسته شد؛ خبر ریپلای شده هم بخونید!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/persiana_Soccer/28843" target="_blank">📅 11:10 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28842">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4afbdcb0fd.mp4?token=PQbwXX-jud22W8zZuaJ-WhHnjnEyc2-_URV5AJFjgvjOxLMXKpNGwzkOoG8qDUNhr6iEXExf0tiPfrCxa18eppoyJS5tTVvlqPB4wimHI591OYtJRyzUGVITHbH7M3-BLbIHtLLmAq-Uveg7s0qCXK9J3DJxcLp97NSk2rzH5tUaFkdxW8u8eEfkcK1efkE0GTiHxvPeNFrAj_xcMI25qVkPrVjJbOePqCBK2oA6o1XtHk4ygKGUWJ2QS4XCQTb_WyeZGanGf25yS4P-MllSduRaNOE26virBqc0U-zZIUDGabny39vxaCuTsExb7W4lutZi5NHEjBg3lscOHxb7yQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4afbdcb0fd.mp4?token=PQbwXX-jud22W8zZuaJ-WhHnjnEyc2-_URV5AJFjgvjOxLMXKpNGwzkOoG8qDUNhr6iEXExf0tiPfrCxa18eppoyJS5tTVvlqPB4wimHI591OYtJRyzUGVITHbH7M3-BLbIHtLLmAq-Uveg7s0qCXK9J3DJxcLp97NSk2rzH5tUaFkdxW8u8eEfkcK1efkE0GTiHxvPeNFrAj_xcMI25qVkPrVjJbOePqCBK2oA6o1XtHk4ygKGUWJ2QS4XCQTb_WyeZGanGf25yS4P-MllSduRaNOE26virBqc0U-zZIUDGabny39vxaCuTsExb7W4lutZi5NHEjBg3lscOHxb7yQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
👤
صحبت‌های جالب کریس رونالدو فوق ستاره پرتغالی باشگاه النصر درباره سختی‌هایی که کشیده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/persiana_Soccer/28842" target="_blank">📅 11:00 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28841">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bahj3WU8ZK8rQIIeYIOp8zYMGLrBqaG0Bn5GYoPglV0yytjilfJfqaxMZwrTlyQc0jUDW3y26rIuTlqdTZdJ2MV7Wzlh8IW0gXyk0a_v5NRI1lqDbD5RnPUm8O7vkV92YR9qPGpkr_9AtU4J_vMxWcJGq_qbOPFzfWC1Hm4e5iK-BOr4NrDziGhl2nfpyGSF_NI4l_oiJr0W4YZcLmjWof493Qjo_9YlNEGzxAsC0dfgrSxE0qVTzjErRnW4ggMGC_T_wWo6AUx_VuzOwAbCYuuVAVGHlSCR4lzuVmhdIK2WB2w7YsYaJDYTsAdboJisYXj2FTiz5UvquqfPof0G_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
ترکیب جدید بارسا درفصل‌جدید بعد از پیوستن گابریل ژسوس ستاره سابق آرسنالی‌ها به این تیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/persiana_Soccer/28841" target="_blank">📅 11:00 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28839">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cf08VCV4HgOwvbDcCLAp5Hj-lPA1qUtLrx7W9CUa88lihhsm9FfBXv0vRqFy-JxC_KAUMSaKd4a3xaKk1wC7n_WoKQ0SBDfYO7ur6rjo6wXtfikmfCRvVFyyf6weI2r6ji8VOMFW4ZRGgXP6eUOLILUALAXTkRigPsfYX1F3e31nopw6WlDFjKDB99nDqCYS5Gv_ANm8z706jCO1GV78Ajx6iSq00y_YTerehasvBHxvJNyGqKSHENhFF52NhbpIQiSByUF1h7_b6Qgu7Ml2uPZnQEpVrVJ-4OjRmNFAwLicihacXMVYs4CCo9VAUnedVfx4-cLbtGhw7w2DGP2PkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
تکلیف نهایی داکنز نازون دیگر بازیکن خارجی استقلال نیز ظرف72ساعت‌آینده مشخص خواهد شد. یا به جمع آبی‌ها برمیگرده یااونم‌توافقی فسخ میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/persiana_Soccer/28839" target="_blank">📅 10:34 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28838">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NTHToD-U9p9S1QXdCAsjsl3l9Ou0uC6bLX6WPiX1uj6-AcusQ3IjNVBty9VyG6hHZsGoWIeaOQ8hzggfiTQD6hDPRvY__LtxeZbQH9_2O0iCcBxqZIeuy0S3lUCUNszCVGux_v9l1rrumR0XCyr3b_SRnVfNQOjux0ZXrnUtX4DpWZPkFoogbLbw7eGrz4CtBNMcxrws_uSw4-rxKzN0_nzbjOqQEf-1rp7f-vflwVzH9m4x9jSCRhunhxmzEsSdtKpU0HB7L5lQ5uhUPQiy-R5272LgsCZEoLbAGbgK_WBK0xBVwAQgLoivczAvm84DpqnOWYKBIrOlN2zjFyKVXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
دو خرید برگ ریزون و فوق العاده الهلال ظرف 48 ساعت‌گذشته؛ گابریل مارتینلی و اولی واتکینز دو ستاره آرسنال و آستون ویلا به الهلال پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/persiana_Soccer/28838" target="_blank">📅 10:15 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28837">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FZshdHncCZo1sOVZaBWrM6kXbaie_pQJl0BKDVYY0UYl285WAW9xzA4PWWzFj27L6OHxx8Vilhda25dtE4Au2W7mh0BTjlM-NiwTot_hFDm1tkQ2SaDrTIVF1LgJ0MPRh2yfTCHFu-roRWiB4S_7sK_WcoyMTyEKO8yzk5hv1iQnyx89fmMJud7cqWJcM-vpy67ZO0cHWScfghRbtjZhnRKfDpqcR2uHk6IB67AzDT71unr4oXRtGp-eTOZZTqZPSkHXsGp8uFNHwe8KmAT7ov2TyqzV2XAUYJZbNzsvqZj1MCfc4BRRmqycOSxyUMPOcnY2Rn_7CnoZP7_7_51cBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
فاطیمه یوسفی فوق‌ستاره 21 ساله فوتبال بانوان ایران هستن که با عقد قراردادی به ملوان پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/persiana_Soccer/28837" target="_blank">📅 10:11 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28836">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UutjVjQD43ZJjvAGojNwyunyCE67zfz53NwRpZ1WZRA-Gd_VL0xW57IFq0xDCbkpt3Z0i5E94Puu3Vlar3MHbpd2wV800lW2K73W3C3GuI14k88TV-6zzr7ahUfTjZuR17t2oLbX95kxwK_VH-9K02dOYwrUA9ONCUOUf18_f6DGy3Td89AtWTudXjaVQE9g6d492bSI4F8wRqikR4su_VQblvv54TwpHMUk65tFvtZMw7LZpX9CD0IcE27J3sq6M7gjGRcHnl8w66P5D5wVB-6PWnKtP_LlOvRh_IDfbhX02J_rzclGytPCKzbQGNUnEi61-h96-fiwbouGOUYmsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
امشب‌ساعت02:30 پنجره‌نقل‌وانتقالات تابستونی تموم لیگ‌های‌اروپایی بسته خواهد شد و از این به بعد باشگاه ها میتونن تنها بازیکنان آزاد رو جذب کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/persiana_Soccer/28836" target="_blank">📅 10:01 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28835">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ddec47474.mp4?token=EXcEmNXbaKc6vJgworyvASY6BV_SAa2HmiwdtsaVKBvqwPhIUeU4M9DE_C_tjNtwbM2FpE8Atx_cWIh7fJxTievJW4PgJvsIjQtrnsAGK4B5fEReIofDKSme43EJ96_hwyE1oTavtcHOijz2kn8L2lYcQVKTl2bZFSORrWQJAeaVyrqDatBYoas37f-l0N2jYfcDCMM4aRA9HNZhmO2go5dZme-KecOpfsd6H6tZLhSXtUujrHfjl5ya74UyeZTxVQO2444UD4_eUUlAD2SHUQ5-LNk1xNzd31ogZ1gfq2JkHmnvc7CNku_Jp1Gu_YvpfIfBGwuoLlNcsYHeB4WVfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ddec47474.mp4?token=EXcEmNXbaKc6vJgworyvASY6BV_SAa2HmiwdtsaVKBvqwPhIUeU4M9DE_C_tjNtwbM2FpE8Atx_cWIh7fJxTievJW4PgJvsIjQtrnsAGK4B5fEReIofDKSme43EJ96_hwyE1oTavtcHOijz2kn8L2lYcQVKTl2bZFSORrWQJAeaVyrqDatBYoas37f-l0N2jYfcDCMM4aRA9HNZhmO2go5dZme-KecOpfsd6H6tZLhSXtUujrHfjl5ya74UyeZTxVQO2444UD4_eUUlAD2SHUQ5-LNk1xNzd31ogZ1gfq2JkHmnvc7CNku_Jp1Gu_YvpfIfBGwuoLlNcsYHeB4WVfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🤩
ویدیویی زببا به مناسبت خداحافظی لیونل مسی فوق‌ستاره39ساله آرژانتین از مسابقات ملی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/persiana_Soccer/28835" target="_blank">📅 01:52 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28833">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kIJ1h0VEn900f3UAn_XgA8obddlJ-dSCgyxFnB_Gyt0U_XN3BhTLR3AMV3PGwR9S7bVH4neKmcepKCnVmidmvo-w7g4YJOoIFMYpVjYJrkJNYh0gMfXBuCD-unTBegSiiK4NrVvWzuOUk6Q4vrzGsdiE6lEL9da1kq3fpnBxQRwJvv01pjzw26KAax0TmKD0GA8ZIaSwEWvR1WGrAiLd2WoiJjglPku_ehEkNm06J3TZNrmGM2rEksV9Qpt5mwyMCu4tE2e87vVjc4tBX8h4NCWyBmQxB3CA-TxTp1UWevaMfYcIgId9zTDus7nbysSRu_pcRPF5X798UnAEXtfrqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌دیدارها‌ی‌‌‌‌امروز
؛شروع‌هفته‌پنجم‌لیگ برتر با جدال یاران نکونام باشمس‌آذر برای حفظ صدرنشینی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/persiana_Soccer/28833" target="_blank">📅 01:37 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28832">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dDiin9OamIyuEmG2dd65yhnIulC0XjVg2uhfh1lBMXzxfgUUGqKpAslxY3DVxbs4IqEfXAnIZlAMtyTiZdD1tkd_XuhV5jR61WVbMs7hSP-VnkDO2q6EP0pPbwjwpTBkaq3Hy8JNouuH02UhF4H20jmK5WLV_D3uLn9VzUjalXhhtH7D6FbfSyzUC1knGnqSO8f8bSKbUI6aP1bf8bUz_yOcZfGz_GanqDJByJ4iukXfv4VQBodS-RTgZpfWLBcM5P8H6myopapcLSZUXMPb7G18j_q5rUv9N4Cc1f9PTTadcMesVmp1IZ5FRlAV2x0ZGlkL3896roC7UF3cuSCrRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌ دیدار های‌‌‌ دیروز؛
برد اقتصادی آرسنال و جشنواره‌گل بلوگرانا بانمایش‌بی‌نظیر رافینیا و یامال
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/persiana_Soccer/28832" target="_blank">📅 01:36 · 10 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
