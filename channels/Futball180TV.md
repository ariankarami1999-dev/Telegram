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
<img src="https://cdn5.telesco.pe/file/Nc-cII8i0XDz84v1XFyEo6I0MXz71hzZ91No93OOe6vtbiucK4t4Cnmjvc7yPVp6ph0b-u1hoKU2vDMGSzw-2Z9nbyNZp08M4Cyqpn2-WV3jB73Pl64FhbSqNn_AUvLi0wqAQFOdl9KhCeNXJD-F0SgPRdaWtpK32KDbWzSr2gw6_l6-sy0iVmcNmlTkpIoWw9SpE_Bo4L8P5Y8PGcGwV4qNmxiNG-sC12QvjqU498LZYEUjXI26vkU9JE8UpbvyxdCRng5dCh-X4G3Gihott-bMgqQWMdIxFut2UeYlEknT0LMPZLsioFs8AT0SoCW42nCcZkod2-I-NEd13LcPXQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 670K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-10 12:04:43</div>
<hr>

<div class="tg-post" id="msg-97331">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cfb04aa687.mp4?token=LbAuyF2CUs98tPtaCQ-V-CVSal_8dX4N7T9q46Szy_7TTUnbO1Xzwj-T249ZcQ-pdCSfY3j82Hyx0J_KziURZXS7sYNNAMreoB5xsj5O-CsSJeL6v26wpMEyPtGA_DWmy7jcOgCRmKsefzU9mcy7X7XeRs4b6njTt3E53Bwy5HPNp_LFBkaLKberQ3W5Mdm-g-QJ2X2mM_xPFLlEhVK5IV5fU8fwMMTh-8rUOlITMYjVezYlDynikMJpQcde9hJdomhzLlQSh0UCcwbBv3elfOKPBqQSZT2mkpJDVYM6AQ3LmmBXT232Ob1_7XtPWBuBLr0wgYBD1D9ReD6hBm4RvpMdg9EruRDhs49YINjNZVfwuX8NLDbLZw2P2nGNxWHJbobO79HjYIMVJYfQ-KNoD01_nLwYPYa3tHgS0GGP1QT6dhhKtNZN0WD2QcUZ9n9fCaAldTAVt2ZRZRg_iuJUiEPENZ5JYiW4COZza9rhOilwB4uj0_1uN1sfNYGczPPEAG9RJF97KsHygfJ9Shs3b7cue8owxeFIu-oJJnHP6OPRzV2-udlT-W9jmTub2rtTypUHn3S_tNYJXiIqLIXowcTxG9Bw_VUAL7TdAtPoWjLhh73MewygnfZ6XRBzawO4RWT-Tp4ImANScMG4rvbIb6_a7nlcaffnx2uxIemiXqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cfb04aa687.mp4?token=LbAuyF2CUs98tPtaCQ-V-CVSal_8dX4N7T9q46Szy_7TTUnbO1Xzwj-T249ZcQ-pdCSfY3j82Hyx0J_KziURZXS7sYNNAMreoB5xsj5O-CsSJeL6v26wpMEyPtGA_DWmy7jcOgCRmKsefzU9mcy7X7XeRs4b6njTt3E53Bwy5HPNp_LFBkaLKberQ3W5Mdm-g-QJ2X2mM_xPFLlEhVK5IV5fU8fwMMTh-8rUOlITMYjVezYlDynikMJpQcde9hJdomhzLlQSh0UCcwbBv3elfOKPBqQSZT2mkpJDVYM6AQ3LmmBXT232Ob1_7XtPWBuBLr0wgYBD1D9ReD6hBm4RvpMdg9EruRDhs49YINjNZVfwuX8NLDbLZw2P2nGNxWHJbobO79HjYIMVJYfQ-KNoD01_nLwYPYa3tHgS0GGP1QT6dhhKtNZN0WD2QcUZ9n9fCaAldTAVt2ZRZRg_iuJUiEPENZ5JYiW4COZza9rhOilwB4uj0_1uN1sfNYGczPPEAG9RJF97KsHygfJ9Shs3b7cue8owxeFIu-oJJnHP6OPRzV2-udlT-W9jmTub2rtTypUHn3S_tNYJXiIqLIXowcTxG9Bw_VUAL7TdAtPoWjLhh73MewygnfZ6XRBzawO4RWT-Tp4ImANScMG4rvbIb6_a7nlcaffnx2uxIemiXqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🏆
تفاوت سطح‌فکر سرمربی ژاپن و قلعه‌نویی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 611 · <a href="https://t.me/Futball180TV/97331" target="_blank">📅 12:04 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97330">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YCo68cet0EktP0WCYE_hqC1Vw5eXGnFSegrqJGhQ30Mbka5RJYpcM4Itam5sklFRytIggr_Fw6gCaigzyhPb0KZCFVGFF2NTNW5IIg2yIuWWG5QsDdD3Alr2cXMMANBsW8HQGHx_e23TVoX8aEnZw5YZuNksQTbRlL9UAsN8Bnx83IxwuDh4wECKaceDURE6PRZf4wAdQSP5npdjWUNwb-9wiLPRkqjmI70VXpu0PnB9jwRxG3SKWqPYU8xQz_fPDX9TytnlLIql68CW7K0snwEERBach_xM7m9lwJzqqyFWpFSrYLYljooEw5q43gAH2EmP3CvAaMNMJF_y9acjcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😆
🇩🇪
تصویری که آلمانی‌ها از جام‌جهانی میبینن:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/Futball180TV/97330" target="_blank">📅 11:40 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97329">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UD6SQ3q71i0ThZViEW1S_JvIQzr9hYX04KHpSHoMDMbXF-dKKDaCzXAwvHzWXSI-ratwsIV6GGTKKezH1537TuJaEqoNO_H2CabfUq3Up4YSKnPG_uMt9QMW2GWDgVRvxsRQ6v5M4n8dLkNNrRj76hFoILB-AYLvlQTT--OSKE_8kUixD8SSqZzndhx2Jrpis_ogs_Y6WowiynTvq3aXqqhRkfrac-RTLJegL0HfpBr8fvJ-RAqnx1UYO6qEhuWIfU5FCz43Crrxt9A5weXRAeOW0QDZQY9Q3efRs-z36n1_mePR9CGMy0nXSMma0M6u3rOrpg3WmfAPfteSkm3geg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
قرارداد کریستنسن با بارسلونا تا سال 2028 تمدید شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.41K · <a href="https://t.me/Futball180TV/97329" target="_blank">📅 11:33 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97328">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa9652808f.mp4?token=CWtLlmwbxRkWcbE5IDtDLdBjaNFocyfVShyGY9-h1hUUoPpKbBNis3titUyO281Q56vVAPp6SPtmhMVmA0xf3qtWayYClRKdtKJ4tP0GuN3TFzn5UUhZ4KIY5l8mgcIebULznkoc5q1TiuNwMVwZP1YGWJiD-we06kszhCQvOwT1jjsg3AroEWL5e2m0rIexzVUGeaNHAz5WuyT9qcCq5lhwkN4HJgifBPMTsABFmROoKR-B1S_-AcdAgoXUoOLkoFFWWTtIzGJiFRJITrysMj5VK_oZZsZCpEWIuGvfUwZOMOTrli2EMSZ2eCZwdv8ROvkaF7NhlRPYNCoD1rFY-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa9652808f.mp4?token=CWtLlmwbxRkWcbE5IDtDLdBjaNFocyfVShyGY9-h1hUUoPpKbBNis3titUyO281Q56vVAPp6SPtmhMVmA0xf3qtWayYClRKdtKJ4tP0GuN3TFzn5UUhZ4KIY5l8mgcIebULznkoc5q1TiuNwMVwZP1YGWJiD-we06kszhCQvOwT1jjsg3AroEWL5e2m0rIexzVUGeaNHAz5WuyT9qcCq5lhwkN4HJgifBPMTsABFmROoKR-B1S_-AcdAgoXUoOLkoFFWWTtIzGJiFRJITrysMj5VK_oZZsZCpEWIuGvfUwZOMOTrli2EMSZ2eCZwdv8ROvkaF7NhlRPYNCoD1rFY-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇲🇦
وضعیت مراکشی‌ها بعد بازی با هلند؛ خیابونای کازابلانکا رو ساعت ۵ صبح تسخیر کردن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.94K · <a href="https://t.me/Futball180TV/97328" target="_blank">📅 11:20 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97327">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J_4VJEmkyhB9E7WZH7GE5NAj7JaOjXtujq5ywBOiGgXFUdcMwVBtUOXXtcLa_RqP0GHD4WBUPzVy8rg_G9NTZ011B887J3lznX38EfUAhMu6oN_tG-5wA8A2tbPQeOJ9MyK8Ao2v8LOSO11EyjLlm-IvcZSAbDVVcsvxJkkSdxHmcrOoSE4Qb9gW28XwpuZdopLEydEE3zH9y3ah_flr35iduYpwRiTKs388Alco3B1OBGqai_q87dr0FTj1mLBVao-fkEI-Xj1PsgWRRuhuZXqaol4TWxyMBCWjcyqWMX8IeXJikJQ1CHgHEo9kelMUTebBLAkmNiXApZLbl47wMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
سرمربی اکوادور پس از حذف از جام جهانی توسط مکزیک از سمت خود استعفا داد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.47K · <a href="https://t.me/Futball180TV/97327" target="_blank">📅 11:09 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97326">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dcd1d74f95.mp4?token=ow1pDiHMXPm2dadUVhgrtUwD-1aRxyPNVS7u6rzMXbBUmd6_X0GxYiwVc6x-ZQAWWtkocuUAi-vkSCyxvKCEYtsRD0dPaDzhlE-LkJJhffaP_fvsxcPzbevapnJNZOqjxP8doosWVKr-nfOVwPNF7FFlv2s6Oyb-hzymDcqoYu16Z-7y7nqGS-uXX4W_Oi5W9K0Yhk4bquEBOY_rr4Iui5t5wE2_Da1p-Agirv374-rsfT23ZH0K04FGVTIMu97-BXBrFVAHcy0po78zHwe0PckdWJmFRdrFThjc6LocxCHCzRrsCxjAqYkEKpXsc2pIiOJMNjRRBVaOTc7pU9Z3Vw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dcd1d74f95.mp4?token=ow1pDiHMXPm2dadUVhgrtUwD-1aRxyPNVS7u6rzMXbBUmd6_X0GxYiwVc6x-ZQAWWtkocuUAi-vkSCyxvKCEYtsRD0dPaDzhlE-LkJJhffaP_fvsxcPzbevapnJNZOqjxP8doosWVKr-nfOVwPNF7FFlv2s6Oyb-hzymDcqoYu16Z-7y7nqGS-uXX4W_Oi5W9K0Yhk4bquEBOY_rr4Iui5t5wE2_Da1p-Agirv374-rsfT23ZH0K04FGVTIMu97-BXBrFVAHcy0po78zHwe0PckdWJmFRdrFThjc6LocxCHCzRrsCxjAqYkEKpXsc2pIiOJMNjRRBVaOTc7pU9Z3Vw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
هوادار مراکشی وسط جمعیت هلندی نشسته بود و سر صحنه‌گل اینجوری کون هلندیا رو جر داد
🤣
🤣
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/Futball180TV/97326" target="_blank">📅 11:01 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97325">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/334dda10f5.mp4?token=Ih7TImayb9pITWsD5D0ghRKoQGyNESXa8W3F6PmB2JL7zutAoR8BFTxlH-c0x1-c6fp230qmFp8B3KvV0cumPB-kAbozf0cw9Usl3VeBQ6y2XyYtLOXeEk6qBlHq4LDZYlqak9Zjqa9Sbee_r5oKB9fvYzxfLPoSAphhJSEvcFmg0MapT5ipU-J-WWtEwQO2WuBs9-Sgeznvxcm2mkD6g8vSiLdP_I_nmETE17VMib3KiQahUrgyzjwowffkpMvK32p_ZzFnzkqlcCw5PR8js2OOj1I2SELSrpju5Bix7VwRpfo0Nx2GaVWZIMMRgTHZM_kH3Lmswd-vQDf31H-G8DzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/334dda10f5.mp4?token=Ih7TImayb9pITWsD5D0ghRKoQGyNESXa8W3F6PmB2JL7zutAoR8BFTxlH-c0x1-c6fp230qmFp8B3KvV0cumPB-kAbozf0cw9Usl3VeBQ6y2XyYtLOXeEk6qBlHq4LDZYlqak9Zjqa9Sbee_r5oKB9fvYzxfLPoSAphhJSEvcFmg0MapT5ipU-J-WWtEwQO2WuBs9-Sgeznvxcm2mkD6g8vSiLdP_I_nmETE17VMib3KiQahUrgyzjwowffkpMvK32p_ZzFnzkqlcCw5PR8js2OOj1I2SELSrpju5Bix7VwRpfo0Nx2GaVWZIMMRgTHZM_kH3Lmswd-vQDf31H-G8DzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇵🇾
خانواده پاراگوئه‌ای‌ حین‌تماشای بازی آلمان و شادی فوق‌العاده بابت صعود به ⅛نهایی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/97325" target="_blank">📅 10:40 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97324">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5dc32bb0eb.mp4?token=cMhgNhxJq8qFQAG48AUocZGYgmc4F3iw1T1wGwjx69IXqA4gzsG-hMy-KLn01yF2IecEpiHp7aQuZ3CatEixwwOB4JY24-Wg5l_PKj6-AoypA1Jbxpai2y_BgUVRujQyBf-SiJ6hZQGSj2-5akGCRBo3gwhXr1e6GBDk3zIZ4gV2tQBeICozjmgJuMDBSWLaPJm9gRBoIZCsTfS-Me3j9Q2RYWe06Y6K7yqnmwAQ9MPNWpLmsrnWNYkEOw548hT0IGd6aleDkm5-sq-gl9RL4PDE7eVKhIGQI8dXLVPZJnJHsK2bx1GLXtpjRp2JAiNorULKenBsYmjDv1dWaZGRb54BPsufX4V0AiuVOSFsE-q-ePnGaidp82pkiIIbkb0ADkixtSvSjqTjyKeXgnowW8JcaJsur_IPQG6uPMrhTQqGKxPwkcD5yqXhskAy27dm_SCAzacWOkUcF5r49TeNVwP3pJVZhh3z1SPUJ77-R_Ptlp1xQCCccVElyoUkdKchVaK_2bCWo58_Zzch77Q8TJ2nZhunIKUT60mgzKyaC275vAm49D8KiqibQJM5FTqYkj8L7GPa39QsFBWL8ps-EmpaIQVTJcC_6aI5zhAL22y4TswdD4utxQgJNRZtmzD4n-q9f1s3tk9n1nBlrO3ln6upajoUQEVsp6Mo9BhlHy8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5dc32bb0eb.mp4?token=cMhgNhxJq8qFQAG48AUocZGYgmc4F3iw1T1wGwjx69IXqA4gzsG-hMy-KLn01yF2IecEpiHp7aQuZ3CatEixwwOB4JY24-Wg5l_PKj6-AoypA1Jbxpai2y_BgUVRujQyBf-SiJ6hZQGSj2-5akGCRBo3gwhXr1e6GBDk3zIZ4gV2tQBeICozjmgJuMDBSWLaPJm9gRBoIZCsTfS-Me3j9Q2RYWe06Y6K7yqnmwAQ9MPNWpLmsrnWNYkEOw548hT0IGd6aleDkm5-sq-gl9RL4PDE7eVKhIGQI8dXLVPZJnJHsK2bx1GLXtpjRp2JAiNorULKenBsYmjDv1dWaZGRb54BPsufX4V0AiuVOSFsE-q-ePnGaidp82pkiIIbkb0ADkixtSvSjqTjyKeXgnowW8JcaJsur_IPQG6uPMrhTQqGKxPwkcD5yqXhskAy27dm_SCAzacWOkUcF5r49TeNVwP3pJVZhh3z1SPUJ77-R_Ptlp1xQCCccVElyoUkdKchVaK_2bCWo58_Zzch77Q8TJ2nZhunIKUT60mgzKyaC275vAm49D8KiqibQJM5FTqYkj8L7GPa39QsFBWL8ps-EmpaIQVTJcC_6aI5zhAL22y4TswdD4utxQgJNRZtmzD4n-q9f1s3tk9n1nBlrO3ln6upajoUQEVsp6Mo9BhlHy8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇵🇾
هواداران مشتی پاراگوئه بعد شکست آلمان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/Futball180TV/97324" target="_blank">📅 10:20 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97323">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b3264c990e.mp4?token=QveoiIf9dHoZ1ZGND3hYw2FOo9-MEyVVGgkPCwlrUCVS496hOJv7TJpV27jAY-41kHm0snRGkqDaTS3RF_VxAZ33F3k_hbjIufJLXakgRTz8yWbB9cWwksjFWj83b1ef31clIO8S4OMGpxfOO0jByPkg-f_48seFg-L0ODAQV-hvdliWYqHedFEbOIFQaDyOzxrfzkN2xVGbcHHBhIh4aHPfb_gd22f33TBe3H5g3D1rc347T5CkX9hvSqEJd4G89PCMrF9ffKy84eo-R81h5UwVnr9Ni42rt5LJc--ad4kKJ2IVR8_ebmzN6fvkcASrSQuWO0esO77EqPLpflY3lQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b3264c990e.mp4?token=QveoiIf9dHoZ1ZGND3hYw2FOo9-MEyVVGgkPCwlrUCVS496hOJv7TJpV27jAY-41kHm0snRGkqDaTS3RF_VxAZ33F3k_hbjIufJLXakgRTz8yWbB9cWwksjFWj83b1ef31clIO8S4OMGpxfOO0jByPkg-f_48seFg-L0ODAQV-hvdliWYqHedFEbOIFQaDyOzxrfzkN2xVGbcHHBhIh4aHPfb_gd22f33TBe3H5g3D1rc347T5CkX9hvSqEJd4G89PCMrF9ffKy84eo-R81h5UwVnr9Ni42rt5LJc--ad4kKJ2IVR8_ebmzN6fvkcASrSQuWO0esO77EqPLpflY3lQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
🇦🇷
این‌قاب برای آرژانتین حکم دین داره که حاضرن برای پرستش هرکاری بکنن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/Futball180TV/97323" target="_blank">📅 10:05 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97322">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37351875f0.mp4?token=nz0tLzmhooF-zyyj-6IJMNK8NX8TpCHz8ADspe-T6gyO2Q0N-D4IIa6o8pNnyJeLA8-RGwcCNRTQFtD2DO94aA9Zpfwcvp668W7bVb0raGPl6nn5kABCdE-aFFFWMY_ZoBiT2krv57jo-hrpCrmvBnlWGVHYFFPQe5eWGk9v3VykKVnX0izLOsTDgqYYZoUeHYieVK0NyXREOX1G5-CnGKH4voOzOLtlOaW3TC1x2KaW_sAIeriU-ceXOvoOQtZu-1l6hW_74j024o87gbAx-ddEXG3zNprcxuRaXHAe7QlnzbljKynZ4bJNTsrsppuDHRV5Qn-LjDEBhaTj7RQlYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37351875f0.mp4?token=nz0tLzmhooF-zyyj-6IJMNK8NX8TpCHz8ADspe-T6gyO2Q0N-D4IIa6o8pNnyJeLA8-RGwcCNRTQFtD2DO94aA9Zpfwcvp668W7bVb0raGPl6nn5kABCdE-aFFFWMY_ZoBiT2krv57jo-hrpCrmvBnlWGVHYFFPQe5eWGk9v3VykKVnX0izLOsTDgqYYZoUeHYieVK0NyXREOX1G5-CnGKH4voOzOLtlOaW3TC1x2KaW_sAIeriU-ceXOvoOQtZu-1l6hW_74j024o87gbAx-ddEXG3zNprcxuRaXHAe7QlnzbljKynZ4bJNTsrsppuDHRV5Qn-LjDEBhaTj7RQlYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
▶️
آزمایش فیفا برای شناخت تکنیک های ناشناخته ژنرال و مقایسه با بهترین مربی جهان.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/97322" target="_blank">📅 09:40 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97321">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HnWNLM1jHvld_P2PHwlnmRal443PRjtml1rfOCQhCIjfc3IUrvs4IPDHeFi-wMAnOX3dqECzkAFr3G0oNWsOpL-2eZEYVrKc4oSadgHf52_8cA2KqbfK2D7gC77rMecT678NMvZevK6BYqMInaCojgm4L2cNBLzZEEcjDkJMd0pR6tYpKTHL9ms49jYmjFEqwJKzb3_Yic5Kwkkhgl3eekmkhA2uD3PWf77AuAE6BodMwAlwJLrXrPTZhNtgqeOby42oCcVkLflW-ylHHZNURYQu3xdIIXU433BtD2jWn8DsOBf6tR7wQSviITLFgxqI5JC99YtU8mu18vS-QOAEwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
📊
🇳🇱
آمار ۱۶ بازی اخیر هلند در جام‌جهانی که شکست‌ناپذیر در وقت‌های عادی بودند!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/97321" target="_blank">📅 09:20 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97319">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Bbr2-Lq5Aeer1xOoa4hxdhzKWQ9EswWMt7mwSAs2vW9z8k170SMzOWBB2Lc0YPJlMbzH0v5UG3aRK95XI0B72Oe3UH_xp6xTNW6fRSGrM8B0ZMJ_RxZs3jIAY5QejEiVLqhF00-VFQKxGFeFf5avqLRUsgMEtj95iKfCU3ClM4Y0UhA9Cfw0SB_yAAAEXKnHxyBQY-sPThI8JDhA9TIRVS0u2_WnLB0g4X_bDnqBbuet_8l7hCZ_7kW8cwrfvYN1fY165CdoIGjvkjE8wLvwSXbb2e4AETzz-iNPSnk5CHWvN9_VDZmGkU___YCQSKnrtlhekcb8rIiQYQ9LiP7KmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Xbxg3HP77RuVl90f2iqnSeD0fs5Kzi8CazdTWbAdEJQ-ty6K3t3ArX1KY0eM88AxrmBA2JL0yoRTnb5QfEMIyF2YafqKl6M_IG0EYwYhqlZmBNjo5h0QH-YRwQiv62zTIP2XGLcddI_7A0aVT1evREUCXK2KQkgp-pO0nQX4aWCAF1HqZxAU7PwN4A1_Xg91RENh86et9iMb96nqrkJHWPCeD1VIncVokG75pmKUHFOgGkuHnQ-TI2UFzDE5GF5uY7g4LYDkbdEK2Io2xqsqVpPlN0622jZiSp91wN1cYZa96K3yM4lC1jIEyw1CzSc8M5LzV8p3ynexZNyMjTGOnw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">❗️
🇲🇦
وقتی اسماعیل سایباری به دنیا آمد، پزشکان به خانواده‌اش گفتند که به دلیل مشکلی مادرزادی در پاها، در راه رفتن مشکل خواهد داشت.
👍
اما مادرش هرگز دست از مبارزه برای داشتن یک زندگی عادی برنداشت.
⚽️
سال‌ها بعد، سایباری نه تنها راه رفت، بلکه به جام جهانی رسید و پریشب پنالتی تعیین‌کننده را گل زد تا مراکش هلند را حذف کند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/97319" target="_blank">📅 08:47 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97318">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GMK1PNvykz0Om6paN8w6RDSmJmdKbs8Ob7O4rCC_8DUhuGeu3uZrOyccOqbtoVkQ7eQEvfqOFpkKqc8zxc1IHYxD4ZHSdfQS594rl_7nQrAOrI2pm-QKlMHfRlOghShLt6PgpCTtmMQZzh7PVa3wZhm9QZqhWKAstTtbL5-N1DDZCZM7YSiGeNPJCluMEXNNZNfi5WmcipqHPjexdO2SdeduWYB6ciRGL8lV31Mr9pVM9eEuQ1nzW6nyA0fT2wKsVe_GMxDh36tgcnb0Dy4JAA0JRIW-nd3Yoz5I-BGRRdGFhUbycBV33a2o4nrLuB4C8ddshIkKAwzRi578cJ_Oww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🚨
آپدیت نمودار مراحل حذفی جام‌جهانی فوتبال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/97318" target="_blank">📅 07:58 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97317">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YIOidHrbVaBQ8K-MbHDybe6ICg2-iPoTV80w0uwAnWcM-l6jHfZfoOfBsajoc5Kcl2UbCyn_Od7cDH5PtgwyYW1V6cJbYYFoNgwujmmkqkIeasMKU6LMmEjPVKWT-pypFvViYPlXRYM3rgQ-yLFAyNlBAnJn6C1hUDShQspekSXZLvpHdoqimGkuQv2I7tsLiIxzC1ceOU5n-DkrHzkAiGYxukZO26xD0WLH7x_-kak2Thy9tkZzc94VzPXZKFwlLyqQN1aVSp1DyK8iVXNS3nyDk_dIxJO3cSU099h5IrNNaCOoI2OxFOGB96CvaUHS3ox2zIF0b0XI9fnhzcVpYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طولانی‌ترین پیروزی‌های متوالی در جام جهانی:  ۵ پیروزی — مکزیک
🇲🇽
۴ پیروزی — فرانسه
🇫🇷
۳ پیروزی — آرژانتین
🇦🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/97317" target="_blank">📅 07:45 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97316">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AykQUUwEJFqpk3aSWIFpOJkFBQEhfUvBk1r8gDJLrfXmYsOP0ayGU_sKUWsF9oAKxm9FmnUPb6ukqoxlamGnb1twDwHzlUrr1oyZAiryrexDol3PtNx9T09nXclwnKtWYeQrXvflO489COIGUOwuvK6-6k3BTP1oV-yvmFT3v-scoQKIAy78K1BPWQugH6O58NOI4C1R-QYDwUFU99Qup4JExea9Ta1Mh72OfSitFziPJU5b1VIWpU31EUX4-OLP4VT4f83XX2RPIw3tBW0TCRcqxUm6EavXX9RmTI_zZ2PyUqm5zzvCunBOSn9WrAUz-I9mjhBZJYHYSL1arKMVKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طولانی‌ترین پیروزی‌های متوالی در جام جهانی:
۵ پیروزی — مکزیک
🇲🇽
۴ پیروزی — فرانسه
🇫🇷
۳ پیروزی — آرژانتین
🇦🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/97316" target="_blank">📅 07:41 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97315">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S9JRhewkYPT5kx8mY80hB4D_DGlBUdddaL6gh8IcL0WgCgvZ2RQ7J8D6woo3Rc97Ak_4VnAJI7na1W02cP5It38OjPll00vCkiclfFzogw1CTPc3FrLgQUSFWcdJEZraskiBfY1tZLa2Z6R4PVTKee5GpO-UJ-4TCw8irtXwLAC4AOz8vkKpjZKb5Tae94zbmtGILbRljS19_2qRjUa81u-t4Z64zQY3f85UVfjaNYn-ajY-nZH2qfQ8VeZZ1y8yqkFShZ-_x7ptR6eNtAh8FJMU7Qo6VCa9oc7IWLSyJu-UB4vZphxUb8NVLB2kFFuxCRyl9tfzZNLGa9UAH6UUPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
👀
قانونی وینی(پرستیانی) بازهم قربانی گرفت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/97315" target="_blank">📅 07:40 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97314">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🚨
🏆
پایان‌بازی|میزبان همچنان مقتدرانه پیش میرود؛ نماینده آمریکای جنوبی با شکست از دور رقابت‌ها حرف شد
🇲🇽
مکزیک
😀
😏
اکوادور
🇪🇨
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/97314" target="_blank">📅 07:31 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97313">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Amw-yPIgYw3gvztblmQuGZOoAcPkFznQcVwBv4dgBT6aua0v8H1upYG_gdIAZE1FpMllqOEJXadwmrawYOF-FbwwnNLklwKEmUbg5tGxk8NvsFUYhKPmOJT5fSdfZxPxct2tLmxjWDVqCJl1Qj4kmTP8YTNl1mQPG_2jQkFIE-8tym8trfeK_VfUY6-33dFh3RRk99oNyl0ChuCw6ml_HgbEgrHN3KSyfC8CuiSkNukEZsivdvEaueAH4zav73SXpuIyYBM1N0tWT_ChcZ6zrUcqLOAK9I0G-xCwSiEPhFwNhovfoNiDrkdCzZ0gTY3wfCPqCAI-kGtrdN4sRs8ZlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پایان‌بازی|میزبان همچنان مقتدرانه پیش میرود؛ نماینده آمریکای جنوبی با شکست از دور رقابت‌ها حرف شد
🇲🇽
مکزیک
😀
😏
اکوادور
🇪🇨
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/97313" target="_blank">📅 07:28 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97312">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">دقیقه 95</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/97312" target="_blank">📅 07:28 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97311">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">هینکاپیه اخراج شد.</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/97311" target="_blank">📅 07:28 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97310">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59fc7f9397.mp4?token=RIPtawLsZ44CdzC3oYULmdl4ZTNuoZhJ0kXR_WOC65peplTHu5w5B8uRt43El3K_aE0PA3I-bAjg-v78tm5_bqr7Vnd7rOMxNBLb-VpBfnTausiWQzqCfxO_UOAV-DySB8PAZzYVYa8511isovKPMZTWv6kBi4xbY6ZbWxQ3miFi9ngyesI1uGmgfymaCAn5XHFxuB5fWFmLFBDqMAs_1O-v93kRDI51LI7wn8t4l00_mxTsd9FyQ5UZaImOvrkewz_ToSuFjSIWlQfhmHX8ejdN8UOgB2uhng_9sgXfR0CRHAazz9G0OxMcwSRw1qFbZIGLP4ZbxjYR7DH25TBWgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59fc7f9397.mp4?token=RIPtawLsZ44CdzC3oYULmdl4ZTNuoZhJ0kXR_WOC65peplTHu5w5B8uRt43El3K_aE0PA3I-bAjg-v78tm5_bqr7Vnd7rOMxNBLb-VpBfnTausiWQzqCfxO_UOAV-DySB8PAZzYVYa8511isovKPMZTWv6kBi4xbY6ZbWxQ3miFi9ngyesI1uGmgfymaCAn5XHFxuB5fWFmLFBDqMAs_1O-v93kRDI51LI7wn8t4l00_mxTsd9FyQ5UZaImOvrkewz_ToSuFjSIWlQfhmHX8ejdN8UOgB2uhng_9sgXfR0CRHAazz9G0OxMcwSRw1qFbZIGLP4ZbxjYR7DH25TBWgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚪️
مانوئل نویر در ۴۰ سالگی، پس از حذف آلمان از جام جهانی ۲۰۲۶، برای همیشه با پیراهن تیم ملی خداحافظی کرد. او که پیش‌تر بعد از یورو ۲۰۲۴ بازنشسته شده بود، برای آخرین بار به درخواست کادر فنی بازگشت و آخرین فصل از یکی از پرافتخارترین دوران‌های تاریخ دروازه‌بانی را رقم زد.
◀️
۱۲۸ بازی ملی، قهرمانی جهان در سال ۲۰۱۴ و سال‌ها الهام‌بخش میلیون‌ها هوادار؛ بعضی اسطوره‌ها از فوتبال می‌روند، اما هرگز از قلب هواداران پاک نمی‌شوند...
Farewell Legend
🍸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/97310" target="_blank">📅 06:59 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97309">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">شروع نیمه دوم بازی</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/97309" target="_blank">📅 06:38 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97308">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🏆
پایان نیمه اول | مکزیک 2-0 اکوادور
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/97308" target="_blank">📅 06:24 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97307">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">مکزیک هم هوادارای خوبی داره هم تیمش زیبا فوتبال بازی میکنه.</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/97307" target="_blank">📅 06:16 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97306">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">آلمان چقدر لوزر بود که به این اکوادور باخت.</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/97306" target="_blank">📅 06:11 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97305">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/58e871bcbc.mp4?token=HfSRjsso3AGwOapS3pRtDFU2eFaeDc2Xdgt8TUIapmWpY4aRKeu0nGrSHsC1FK4texew3iGHwOGC6gTTOpMDCiyi4buhN5iGJrtU8fr-eB2U9EWqzLif8mjDUbOAWenwBFRRb2SY1A8vR4se29nyHfrKKXoGOhAoMCLmSxpva6F1BDL8DPavSoxlhthpNLBY8LiazUZKnuQP0IfV7K562xNvG_bzngDgERgq_6BvUaSoA3O-Y6vObWeY-1M-N4276pZGmbqr6NNTCMCLLPsMn2nYd0cy8LOy0-W_PwIeOoV3bA6lkAv6HoX-OT51tqS3lhjNbVSaWCL23fML8JShmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/58e871bcbc.mp4?token=HfSRjsso3AGwOapS3pRtDFU2eFaeDc2Xdgt8TUIapmWpY4aRKeu0nGrSHsC1FK4texew3iGHwOGC6gTTOpMDCiyi4buhN5iGJrtU8fr-eB2U9EWqzLif8mjDUbOAWenwBFRRb2SY1A8vR4se29nyHfrKKXoGOhAoMCLmSxpva6F1BDL8DPavSoxlhthpNLBY8LiazUZKnuQP0IfV7K562xNvG_bzngDgERgq_6BvUaSoA3O-Y6vObWeY-1M-N4276pZGmbqr6NNTCMCLLPsMn2nYd0cy8LOy0-W_PwIeOoV3bA6lkAv6HoX-OT51tqS3lhjNbVSaWCL23fML8JShmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل دوم مکزیک توسط رائول خیمنز
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/97305" target="_blank">📅 06:07 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97304">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">رائول خیمنز
🔥</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/97304" target="_blank">📅 06:04 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97303">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">مکزیک دومیییی</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/97303" target="_blank">📅 06:04 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97301">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ckdz9seO7iGTF0QvDceB1jqrCikDb0EwdIHek_0ZbgIidSpOBNINZVJmW3zXnDOULF7FsMQPzJLjVtYKXfEivnlk8RPrkRmArE3ZmThgPpB9_aXLp9xIlZppvaPVrltUi39-12QOfts6phdc0gTD2K-_uyNNbBvqsZkVxxFZTz-BUOrXBCk0gbhkdeX0eXuoq3PeNygtPcVmaBRIHI45qp8tICBuUiW1I-IDWN7Ur7bP1s4T5hc_eICsg1oxREgWaTW-RmtWMq_QEgR22GwBBE6uOyK8DTHCv3VzV65SL_RLZ7wrv4r945A-ewxS_3FOrVIfsMjrLT6d3x-htRl4EA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KC24vaSTClJ3kQpKOHwMevL1nIpIOEb6T-Z50WFFN77HIUmTegrSiQi3lxVzCEgLLmh7raAs5cOKhUMVMuwUhU2qulHmj2ljALmKPPxWTc6Jtx7Pkw_n6uoSMQiC_n_IILQ8wK1re8HrA4aerNfuP7GMt4EixjrjyVEZIOmWOkv3KvBvFkEcmEeZBhWKd5Dam0Sikc-ljy1TPlsprDaAoizLtnUddGCETIVZDcIPmV557rWtri1U6YKnc-eJourKDNv9qnPhNp0Nk6rrcX9e_T0ekDKX4p05OtRaohtTkbZpZZ-edZ9kB9KWunSy8CKMQE4y9rXO2jxBpBAEOH8FTw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">گل اول مکزیک به اکوادور
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/97301" target="_blank">📅 06:00 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97300">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a754997a6a.mp4?token=p0KC6ACIW3tgSVqc-pecv1hxG87i6Bw-4Nm2gIFSfH6yDHL9vHAJhm_iEhA1brAfCqcpefKbfsMlRnnfRre2pg-syUk5Ek5fRHVmBDDfZqDlNTuHz886tMpIUZnez-x3IWK7gPZAr0F_eH3ssuOgTMl6T4YwFMZ6VkxRF3UAfhlaTPvFuQ2GPV5k0tqicRIuYe8hDtYszOlvlAnNf2wgqNn5LdeyFwzVz16b92YzBkZ__Wr_N8nKHdIl_7mwsABrgnTH9ttdfAzy_GM-H3kLjVQF4mta_nTILmbPbcB8XNnIdM1UH9Fnem9dPztmqZ83EQVM3XPlg-zuhhKOQY0Tug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a754997a6a.mp4?token=p0KC6ACIW3tgSVqc-pecv1hxG87i6Bw-4Nm2gIFSfH6yDHL9vHAJhm_iEhA1brAfCqcpefKbfsMlRnnfRre2pg-syUk5Ek5fRHVmBDDfZqDlNTuHz886tMpIUZnez-x3IWK7gPZAr0F_eH3ssuOgTMl6T4YwFMZ6VkxRF3UAfhlaTPvFuQ2GPV5k0tqicRIuYe8hDtYszOlvlAnNf2wgqNn5LdeyFwzVz16b92YzBkZ__Wr_N8nKHdIl_7mwsABrgnTH9ttdfAzy_GM-H3kLjVQF4mta_nTILmbPbcB8XNnIdM1UH9Fnem9dPztmqZ83EQVM3XPlg-zuhhKOQY0Tug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل اول مکزیک به اکوادور
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/97300" target="_blank">📅 05:59 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97299">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZqwjAwp1vASe-48WRNDbAVh4AVY8R3adRU6tZBSzu7STDpqisog4NDwoq8lGMjgSEtYWBl04Jcyz8ts6fovIUUGaN8nIiB1HmC51y08vAc713_YYzRoB5wLfjwIojFFE8Aa4pHrxDRqkz3b6NqwCfifPOsnulC9gzMIX48B8LMPhUdYG3XWn_G_B4upoq3GG9x03rlNakYQd70D9MQzD_e7GLchOWQrgHwNqyUEWTJGhr9t3pHnxmiICqW4aZscC0SHcf7sqnmAXV0-n8OdxMBF4n1FEF1RuOMHf7B3YcR4WL82iDDgwlsdp_e4ape25FFfdDEt2oV_IfMf2ZUJVQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
خب خب یه شخص کاملا جدید اومده ورزشگاه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/97299" target="_blank">📅 05:36 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97298">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">بریم برا شروع بازی اکوادور - مکزیک</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/97298" target="_blank">📅 05:33 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97297">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RZZBNliYjMYNzFSIDGGwncVpWpZe089XBwzBxRYioDj6v_JthplTVmTQW9sul_rqoMIJ7Hw2ehfpIVmfb6UpUJV98CCLM6eh6cCizFnNUYHq5_bXUJ8ZF2j7Hk3e2R6J2hfmS6M8EMXPaUenCC_E-UgXiIqlY8VnytkENv_CXy_Av_zvMD9lJZ6G-OhffHuEYSnJv-yQS5sejrUDWpkHRcg6CfLAVu4Ct5RBp3_POUj_DX2asCh3U-vzd5FVl4r5hZtoU22hpr3Zdl3CtpW6Tj0K3lZqdhQtbrAzRQUOI3B-21auwtC3AMviYs4D4H80ahLJTnc__PtV8iwIINQqXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
⚽️
امروز قرارداد محمد صلاح با لیورپول به پایان رسید و او رسماً بازیکن آزاد شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/97297" target="_blank">📅 05:25 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97296">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e01873d097.mp4?token=Arp7oHHcXW8cBRclDP_qiMoudPcAwxRNNzl2BTjSFbsmzizhKsJ-wT284Ewl-T89OWF8rA67E4aFiTkXtuckUm-4jm2N9jqh90IVEk7seFewSb8jZ9hYt4uYXUnKbLYdEKuoSnjaPLY6m5fY0Muv_wuD304ua90fes7FcPbERcCm997NEAyo8nVJeAl8RepDMiVauraP4xeWIncRD1p0KM8qbzKlAXFNpKjoFq1tkeFFMBliq9x6L_VPc0G0tJ9iB9eg49i28yKnnSoayTQVPDa5S0LrbFht8cwENQmvJCki-ReWfg7k80cJePprzzV18uIj0vmR82VMYlgMNMmrNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e01873d097.mp4?token=Arp7oHHcXW8cBRclDP_qiMoudPcAwxRNNzl2BTjSFbsmzizhKsJ-wT284Ewl-T89OWF8rA67E4aFiTkXtuckUm-4jm2N9jqh90IVEk7seFewSb8jZ9hYt4uYXUnKbLYdEKuoSnjaPLY6m5fY0Muv_wuD304ua90fes7FcPbERcCm997NEAyo8nVJeAl8RepDMiVauraP4xeWIncRD1p0KM8qbzKlAXFNpKjoFq1tkeFFMBliq9x6L_VPc0G0tJ9iB9eg49i28yKnnSoayTQVPDa5S0LrbFht8cwENQmvJCki-ReWfg7k80cJePprzzV18uIj0vmR82VMYlgMNMmrNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
قلعه‌نویی: خوشحالم که بزرگان دنیا یعنی آقای مورینیو و تریلی هانری از تیمی که من ساختم تعریف کردن.
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/97296" target="_blank">📅 05:16 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97295">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WKIBiRud415DxlZ4xIuoRC1Ah-4EuthsQGMSul1zHvALWkzUgGZOX12P14nGt1XDi8Ou1hVevhtrSzHP7h8yqOOHxlFssLGMVeTit-uBY7XRmFnT-CKQ36AU0m3OM8lG4xJhVPHF52QVRTp8tO16Bb6sYcaYCJqCLy4pWlnzkwcL55-jkH4sxLfXUvRcZbslbCJyrF4u0SVkCEnc3_gPUJ7KmKNvpy4Ug2q2Ty_T6ZM59EH3EVV0705mavAKYx2NYNhRQdRqSCORaC9O7apbrSQW6Nx3oOtff3lQaWS51EcATlj5Ir8qZPnPtztTBn2E44NaLHAP80GEE7p4-awZJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اوه اوه حاجی رعد و برقو
⚡️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/97295" target="_blank">📅 04:59 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97294">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r7f2XeBtF4dUktfm3AEXb1WX7dtSRESfLqvbwPsKGwKygSS4dWd4FyI-AwVJL-uAFByCql_SHKMsYqaENyKtohq1JDwkN5urTRcHBiFah_96ogY9Xvwjlq5N4a_TByrnL0WXDUuJlW9QV5r2YKYGipwpcupwz5zqwSd4PutJgC97SZnwfoLzxbVXJod8nYX9_wzwFwF6oRTHLpxg-mR1HV386Sa-yO92_tRmtlJuUCgVpUk0uBviZOwpeIv63YV_N01V8428TjgMfJx9xt9aejpn_lL653C70Fsg-twNRdYiqmU_EC3Xhb4zdCGuLdDTzo1NuCNnDwiLVow_Kqqgiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇫🇷
| از زمان اولین حضور امباپه در جام جهانی، تعداد گل های امباپه در مراحل حذفی جام‌جهانی برابر یا بیشتر از مجموع گل‌های تیم‌های ملی انگلستان، پرتغال، اسپانیا، آلمان، هلند، بلژیک، اروگوئه، سوئیس و برزیل در جام‌جهانی است
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/97294" target="_blank">📅 04:36 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97293">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a18350dd6f.mp4?token=eAjbLJliSY5XGiUwJq_jMbZWZ6JOceTW_pxvkkcerxvkfxBNMKM7Pz7is9y4k2Bo0uMoNZk9ayMtRIQob0n8BH1LbQYBwgX1Sf4LVUwVAV6he3YLtDwEbWsDLI4A755NRJDv46ZO-6CJ-PBc5r6-dj_KtQyjywrr8ifRbLBkm2jD-NLaUwCSTjwxZPZfoFSIkxi6OqQ6Pd4dush_Xi0aMWSJGs9q3ETcG-mC2Jskhot4yyScP3gk5wm8JCV36V4ZxHSFjalsf5kaCipDvGsL1wIK5fVjvtU8MRpryGxlS4iD2oFhkkY7X03hCUqnrtMjqN4qjnPIi7g8QcbvOTdS0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a18350dd6f.mp4?token=eAjbLJliSY5XGiUwJq_jMbZWZ6JOceTW_pxvkkcerxvkfxBNMKM7Pz7is9y4k2Bo0uMoNZk9ayMtRIQob0n8BH1LbQYBwgX1Sf4LVUwVAV6he3YLtDwEbWsDLI4A755NRJDv46ZO-6CJ-PBc5r6-dj_KtQyjywrr8ifRbLBkm2jD-NLaUwCSTjwxZPZfoFSIkxi6OqQ6Pd4dush_Xi0aMWSJGs9q3ETcG-mC2Jskhot4yyScP3gk5wm8JCV36V4ZxHSFjalsf5kaCipDvGsL1wIK5fVjvtU8MRpryGxlS4iD2oFhkkY7X03hCUqnrtMjqN4qjnPIi7g8QcbvOTdS0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کی دنبال دلیل درخشش امباپه تو بازی با سوئد میگشت؟
🙈
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/97293" target="_blank">📅 04:22 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97292">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t05F-wNdgixyDTOFg-2K4z7vTS-IYk_xZlc856MHuxrU9n4jOGtoZE50wW2o3dWSuibGf-HsAoGLwZNxZZGz2_O3nOBpS2bw8o7XC2FEowTUdOn5JKLdSdaJO481PTMCM0a7VGoD_cGoCtYfkJ0D_K4IfJVYWwPX2TxCNpld5U9PdjMFEIDHsEmu-JP64PWPkNmmaDbvRA-RgZEYSve6RUkLEMve1RvVIxHKck8VCCIOL-_ywLwRxde5qYR4Sw0WE-obta3IYardcrpYqk5SaxLojyqQLOS-FlSClicV35z-GNEHy4mZBvvbN8BMQTivVBl6suH77Imny_4ep8q5dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
به دلیل شرایط جوی، بازی اکوادور و مکزیک نیم ساعت به تعویق افتاد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/97292" target="_blank">📅 04:18 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97290">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K-igh_6S3Nl8mTm8oY7JmMvw0tbmEfDoG8vpE7FcvfCnVcrnDKWSmDVGMCYHipBPVGYqBRAondVJGQlxrURkOY2eJnjCUCTC7tFQ5gMz0IMJiQsP2Y3DA_UYYqHI2DRfkdSc3qvv1K9Q-SqtDdZfgfFq2Vv_FBTX0unV9EGE1IxABc_axHQO1Feax0-zTHNbPNXtvjhWDo53yut5o8hHrnH0HD0aNbs1q6drwu-rqPozGbgMW0AJw2cAW2ldzcf4ZpXjESO_52EGQzxISLt2KUrtzy4fMRjhST53ed9XWALfcvyiX4UAQuH3_bbUzLNLdMWK9G6-2JW00duH7rpy5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e97yxHDR9NoKJFbw6CXRgDaTvd4CnINXG753FW1mCkaP1AOskXVoeMnEMcEVbI3hp--SB3co6RcxeAh-GTXJ1StZwIkFI3D9o2615xblSQxug6j-ypaDyecfHxzqkPSATD6jbSCQQndmgk6YVHImcwPdoY0aP69rfC-Bu1cf_jbjuA_OTCZJtgUKc0muOQCxjXsmkRwNZi-GJxNUNZY2zXS7OMACQpvdqE_vqlNkyHEt_LfY9qgZxnY5s2LQKvhhaonXNtMe-1JirKgmlAtj7qF1i5yUI5JANlGOZkXa6RFqYRh9lD6OqpyKLxG7fi8GkvSI7rPPJZWx-QF19aSyYw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇨
🇲🇽
ترکیب مکزیک و اکوادور
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/97290" target="_blank">📅 03:29 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97288">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MU06yvs5EHnS1Xyu3G-0Si0EZ12EC-URdsrFcBX4HduwT6X4jegsj-PkWQHMhbB-Z6p5ZERoWNyRwNOe7t_qD57wbIQVpKswDOow6TwpjguRN5ZIyuugmZo28ShmVSnICNOBjyRGmbfDsTwEzOiOM6pTiXCEhZkYC5SmRV0ZRjFqIn6J4xkfVCP-7986CDz6ndFBK2h3utconDMHKGL2SkUR4tf89X_OcbNsWltzJVvmQd6zB1TnQ2iibbVC7XgtE1GRJJNljuMbM1J2l6odijZ-bCwatO2X0Evgas7u3N_fXu_1KK19RwLFNiwY1MjYIQHBsgccpRpCEpL1R4giAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DTYZUZkg5UYSA9Ygs7bO589-MJVKnkNeCjPnd7yetuwquUqkSVoOT1GHbOh5o_I3hs-IxIXbkLpn9h5qcGtXh2jpWCJaSAc57CvBcWXNQje9eLkpI3CSkDWj8psgDrvk8NZmctlOWB2Gw7rqT9JnCrkB3Nnl8pYlfo7W8iKSjW8m5mU8ydlcie8RJUp5TKM3ceRfW-a2-utmN2eSHJs1ni05G8m5tXZ3A_IPgdeGbD97npMeaSqrXHbN26wZ-AIcgU6v38WyuNtaDvzKuVzbP-YQDHj4QP4H4eXlFfka9Z41E1iXC3-RNfYOZ9MnxmZ5zDz0Sx-VcDdcpMFSewsaDw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
رایان شرکی که حسابی کلش از نیمکت نشینی کیری شده اینجوری دشان رو بعد بازی به تخمش گرفت و باهاش دست نداد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/97288" target="_blank">📅 03:11 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97287">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/syae1jgsIo4xcDLxvfR7D1m9GqAnjwtR6kNhIeVjT0ItyVQXtGS3ISfra2AWeMboZHgU6wp9hXTCqD4qQA35w3EwbbX7J4uf-tohQrb33C-tlvG4lmAnGER2dW7DOIfGxrLSU2geY8WPuMzRo9dcKc_AAF3MTMQT0f8bRuF0JIiYyitrcepq-7km3QZbzY6u95OgyKlDu4txH7fJVgf7YausUPBd_yuPkCQaAaB3JAfTOLUoQ87OmHMT43i-5gHt_kk2Qdh713SaeILr5Ru3jbqGlq3nYed52jwzEh-TsVTbc2zQWrNqvWKY-ga7-F0El7nnPaKxJMW2MZa9sN1fjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیافه میثاقی قشنگ اینجوریه آخ‌جون بالاخره یه نفر غیر محسن بیاتی‌نیا و سیروس دین‌محمدی داره باهام حرف‌میزنه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/97287" target="_blank">📅 02:55 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97286">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mltwaeUe4mSa0x-vLA7iafQH8HTTWiA6DNiGxiAN3CdXFXmYSrGCdbK0wWnrEprPzSkuN6-s993EPo9qXeEvU9EfOgX6L2XhV3x4vheGCipNmsnAqaGUza71yZex7cevVGwe3PN__Yjop4BO2lxOTG2XTLtu5x7XRftL6brb2-9cSVTKw17G4vHV9kOsB89UiBuWfyPMGwKh_ko99XZ4N6Ng7qjZAsf_NGVOc_Bu3MzDrfcUVIt95lAIvwSiDyZXH6_32ZSTuoFLdJ2mQA2GMxx63tV2Ph6CWO9ZfO89D6lr7km7y5nSS1mvfv1W1YVg_W-UZm5GkMeKZAjraL87dA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
کیلیان امباپه:
🔺
پاراگوئه؟ من در واقع دارم به رختکن و کولر فکر می‌کنم چون هوا گرم است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/97286" target="_blank">📅 02:45 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97285">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eK1-udsHd1DJd0HIOarv13pD6HCNbaSJv0qFi_V7z8nwcV_k9FDLNF9OXGe0IOGHNX8Mqis95eMvyNTigE5gSZUJ2ifp3qsmz1IsW4qLFSRFTQFxgZn2gjolnv5ALRRvDGXrE0qreT4GbyW5TOiOz70FzPFQ8p11WMXJ8tYj5JdNApxJq5bkZcCLknoZuGpbQ3vttwSFn3ASsh0q85pCzqouHx5qhQxashfjdIwAaqTJNrSfylnE3KIpJ0FOEvnRm2IcxRpwxDn1LeRfhkcD17lqg1EU-xqnu--XzfoK35LF_OfIl-r8Ofkpz-3BUwIVdR-l616FoTb8n26YE4VqXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
امباپه با ادامه این روند موقع خداحافظی تموم رکوردهای فوتبال جهان رو در اختیار خواهد داشت
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/97285" target="_blank">📅 02:38 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97284">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mYVyUFSUVOZKeVZqNS2fjz01JNVtbbk6eyDZRzZqVsVUYHo7oe_4xT-grK9VoggvpvsPa3UJxwDb5O4LUI17iq_GdWI5Rt7JnT4aG_ALnGJnZ_LvCzhlgeHMyWRib0jHlEQ0W3HWSA5vhX6EMN3Yhkx_0KGMMreV4SwTdyyXG8yWbVrwmTzhMH4Gi-ABTGAZI1BgM6ANnnBWNflljcEpKCRgCOsn1SizaPoYG-6ppwMyr73RxQysj5zH2MIZPBYp2uqXsAqV4X9kMYLgViDyZEUt96TfioqEdpLRdCBSy8J_QSPjnwk2tPPuvn-XXZwBUY6cyUr_j_fzPbIUPikAIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
تیم‌های اسپانیایی با بیشترین گل در یک دوره جام جهانی :
🥇
بارسلونا در ۱۹۹۴: ۱۶ گل
🥈
رئال مادرید در ۲۰۲۶: ۱۳ گل
🥉
رئال مادرید در ۱۹۹۸: ۱۲ گل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/97284" target="_blank">📅 02:34 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97283">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">شایعه شده ایلان ماسک قبل اینکه میلیاردر بشه تو فاک بت جوین داده بوده
🔥
با آنالیز حرفه ای ادمین های فاک بت ، بصورت رایگان از فوتبال دیدن پول در بیارید  با فاک بت ، حرفه ای تر شرطبندی کنید
❤️
Join Join Join Join Join Join Join Join Join Join Join Join</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/97283" target="_blank">📅 02:34 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97282">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Tt_rAb8w3wbz02aXmB-kl9-19DoE_Ke49UMzlZkxm0UzvJk46-jIJx7io7wPPaIad8yBjXbHX6X1HX4DHBps0giywbF1vPbfo8765FvCaujIri3lYU3hbWCVyyvQ9XidrMZR4u17Ylc4Lp7JXubAIdfyS3K25Nk0uRfosejnSqY8i_ksbO6no2aZjErULNwQr6d25WcmkLIQXEo0eB3QI9jyT3g--u8peFpphwF2crWr8US-3g1cRTXtCB7qtAtNdT2ayX_-s7o8_yEA_kccoEho2Vif51j_zau3ndkbPcdTSXJhFtWRxkjDo743YlEsHp6nXp7ToVH3GMR3KhHyDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شایعه شده ایلان ماسک قبل اینکه میلیاردر بشه تو فاک بت جوین داده بوده
🔥
با آنالیز حرفه ای ادمین های فاک بت ، بصورت رایگان از فوتبال دیدن پول در بیارید
با فاک بت ، حرفه ای تر شرطبندی کنید
❤️
Join Join Join Join Join Join
Join Join Join Join Join Join</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/97282" target="_blank">📅 02:34 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97281">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/snd1zK_iUdEzbYa_IDXPTNbAM0Q_bqO2n823hjgeLP9XaM1Y_GkKLBn_FZN4PnmRD-H5Uf7sXrjeA6JF8fI4_qhMsqlPu8FyA_dmUBjT7F0BFSx1XFQNLldaT6YGpFVeTXNWbFeQTbgPkWZPiq4vdykML6JPVTu6rmFPXloMvunq_Z686HLiE8r-qvd6wUTTDjXB_Xs9VNBt6bc9xy3IkPWgJdkz_oi3hMS0XkYSeLVvUaAFX7yJHfcJ9j6J4yx3f5uZsA_-hu9gjg-RzP0WdIzmo-na-gR1zT02UgoEpuU4mYA1ri-lWVchlaGYHReevYUJBzEMEAci6OuiS3Nbcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
آپدیت نمودار حذفی جام جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/97281" target="_blank">📅 02:33 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97280">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Omg-7UYNLRowV1lx9K3XW_XoF_NJ2CPDmc02GE6kgkN4anx8jGCMC-Ooy7fPd9rq7Wf4XTvWBTw7T4Jy2ZkILkhI5m5gys6-cpR9H4UQ0kANdw4Da8bP6q60-44DvNQP-VpNh6bhETzZmrC6OzDhnE0l7v2Ce9Slk-4s723hRf0FtuTZStchDGmMmUb3D3NiTBsDOvQqlz4hb7BNsIozpOwuaVlTWTp5dyUlPk6fchBxV0_cJ1Sgb3_l74sc5HYYjzJgMWLwYY6LoDN61wuQeb3p003UG702TcSI6z2qOP-4G7yjjhyNKG8VaF5JneviZlEaGoIvmPtp7yqkXmzYwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دروازبان سوئد با وجود 3 گلی که خورد نمره 8.6 رو گرفت
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/97280" target="_blank">📅 02:30 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97279">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FG1tzzUC1CWlEyd-gQvo4mFLMiNvPt_GCG_7AIqnzWI0DBbhLsneZ8i70x_t8xfOXWsAWfFJHtHQJ_e2x6gm16wCTRyTcS52J9MlTVhUiAtu1d7q4eFS0D6ghy68NPzUuLjBlwLz3xzT2A6fOH8Xy6pWrASsJNBUCyH4bRkCY9bsn22Qzd4TYOEoi31e8bywn6zIq0qtXgVyLboVkau3au89U0WXLLMVmRa63xBvak7txeJn7mZ3ezmPTo6lQn8G50t096Xs60W-vzDPcJtjIvgHWlURuy7bzrRbXhZdQnOGE6RXa0tZ7rZorhpfTBkQ7qoq3OcKAqujL6wiMzvYvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پایان بازی | خروس ها با درخشش امباپه به مرحله بعد صعود کردند
🇫🇷
فرانسه 3 -
🇸🇪
سوئد 0
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/97279" target="_blank">📅 02:28 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97278">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FIUMBrdZZd22qh6I-fuUDKNKVihdFzvJXigxul1blikWXDcFsDz8WZj5daXMEZFe6pp0sSoy9wxAKlhJTQ6sCMOllRoyud1lYlAd5HhPi_8Zc_-U8kQbHs8_lSJhb7Av9wu_aLMUM9b_u2Is0TdWzLWm_wy4gLkgApwZoQHpdtanrATzqojJs3fbYjZABRagXxktdsHKNmSPJoUkO8hq8zSajlhxIMcsDHY5shskou9SVu20W-HnISNPWR1Pv9i5xIdCCmYPfGtH9RlM0FIMJv7o0GfEJBv7PnAfByuuQsC-fEQKLyjBqIUiw9gafsNGeggC73oeOo-qdU-8zlOqAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
برای اولین بار پس از جام جهانی 1958، تیم ملی فرانسه موفق شد در 4 بازی اول خود در جام جهانی 13 گل به ثمر برساند!‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/97278" target="_blank">📅 02:26 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97277">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ukxj7dL9NKKuLJQGbwhtIekffLoIWKbPxahWvwUIycOsIjpWW47z1tX3dDU1-lNHwo-TcfDPDQ_LDJEMYHV73dzTrzUSYw7n_Sbh73ZhVx3Lx_24FyAoiD-q6MNFAG-VdkQq3K-hnX6EPFUN-YfB91UkRlLeLk9Z6Zy_uLSNklpOP3CY5ohAgj4ETeCYP5oV-Nw0eJrPsNKyzWfzfOGKbm3n52_k20aJztzI2cTDA6lj63tFD9hpd_SzKET307rx1J8sev9-b4nVFdZ_ExN89MJCD30fDdDLzQrVFPx3R7Oh7KcuUZ2ELL5SqBR6SAetoM5zlirWxit_Fhw3o68YJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پایان بازی | خروس ها با درخشش امباپه به مرحله بعد صعود کردند
🇫🇷
فرانسه 3 -
🇸🇪
سوئد 0
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/97277" target="_blank">📅 02:23 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97275">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g8KWmKdqAQzoME0X3NmIIVuEwheEPwH7Hbo3bWkjp4wUtQ1E0SzuTqpvd1396fC9wHSqGJRM3RXHlzq7V7snETSCYwzqUHUs46N56Xi5qGLKEWLnJ8Ux6Sfe_yWEmhEU2TxVkcOkOEX2AFZsHbOrfURiQ7WHTTGQUalbKtUAe1zzssI05MBGxao3gV-Z-jJ0tlmSqQfYcR--dJQdg_EiMEf8219OUgZZZLBaRmjQj95KXRvnWFE-5HfMlvJSI4QpsBMsA8psKDmGBUlQVlQhjS3ABLGv33yTBIpN7bZqTOxubPZeV6v6mQ3Sr5xtYVwJ0TJXWqUkm8mtzKDjnT_X3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KW4s91hcPwXkcYAblxd3xUYofIW4r-FJbxWfr652tY4sGUij4MqtFBTMR0HYNj-E-wQw9L_yXEeE_oKDdIcRnVrgQNvYCRPjS9OqGpWkrDDmEKCV44IIS_q-OBozEHhl46oupNb8plFowzwteYLRKA_jbgimdxp7lfBh94u1mMPvGbCvNmR-5qF3XHtDmCQnFns-Ulc98KnDclxYGsNTg1xdkqtAg_eCHUQoWG4aR0Zw3liJtkQM78e5KtmyCWSwUrMHM21ce1xHAyAvIdTXto4l1Fcj7kMLGYrLbPMivjxLv3CCQTOzJXmHDN5AybLP9lrNDGR_IkMbzN-P7VIXbA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎙
🔻
لامین یامال :
🔹
راستش اگه مسی نبود بازی های آرژانتین رو نمی دیدم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/97275" target="_blank">📅 02:20 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97274">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dM_t_9RbxDwiODtjbcKXt_L1JGAaTz5TnZbK27mlIWxCFswjfEiBMuq06hwwvXzucJoBb9YmReA78ful3Sd265wQwo8o1j_P5mLhvnWMh3Ug-4krMQCdblhlDSVujZooixRPUqnQXaAif7EegMuNmv1SDy5bLMQRT1bZ8Pplde6cNw31-EomDJiF56yEiWl_0iULH1c2GXgjgEOOaf1LonpuIZN8WftfJ-QBHfVRmon3wVtFZgjA38gjLcVFekEI3dyIpxc7HNcfiFfbPfma3biycAOV8URvFFg8E45qIok1w5oXdV5An5xf9uZHg6e17f1zn0lcb-Z7Mp3j6te2WA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تعظیم دشان به امباپه وقتی تعویض شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/97274" target="_blank">📅 02:18 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97273">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bD1P4rqZ1at_qC6F7kS-bCehqnAZwceizwzv_vBPOXTP0wjvxEd1n5tvs5bbUwAwzHx_rlv2Ofjulwp5d7rpxmBT2YvYDeIS5-6Tfg5mAHF_XLjrgWnxnHV4PnwZXodDqb4OZpcqm4wbX48yoL6HNvF_VQn8GvJ4L7f8jF572psI0AuJ5r6hh81gVyhdsUjvyFIGahCubp6hkGmvN3w4g01PIrT5rM2jtxsuCrDesDv_oJllfYOK7gI5qU4iSuf0bU2y81tTDBDYrIfcr4rLizYYiUBLAfhv5m5c7b8ErsFsDsmZGnhJHd4Prewc5U52AYOHfoivqCo5oXtZ79_GRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جام جهانی 2026 تا اینجا 5 میلیون تماشاگر داشته
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/97273" target="_blank">📅 02:17 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97272">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A_m0uLICWVIcZwYC4MHtBijb6031ra3KyF-_2Mk0Itm9HwIq4rJHP-jzSTLfn8axkksHHdeuEOIbCKfFXPT1X_ruFrHkSKARKPHe0v-GZbgviKL2vGNqUrqW_AJ9LKV1-9SP5KrUuQAe4yAVVgcFLYIY3LHwpNmRTBddxK0C_8UVX8c725caT4EeRPoax2t-QkIbw6iee5FDzeU6UAVaiYDFCds4__AFtu-82tNkURc46wvPfGOkhWj1I0rZJ5UQQPZV6GGKy5C3lql7AgzCsAzB6oFIztfVUp77x_3vY0qNbERkB-xuBbswlTY69wbLjw_GbNeFh-5kFlejhrHOJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
🥶
🥶
🥶
🥶
🥶
🥶
🥶
🥶
🥶
🥶
🏆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/97272" target="_blank">📅 02:12 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97270">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kB8RdO3rIWquC6PjiPBKLKbAwRfa6SFaSR3_J8nqU-U9EjKj9-5nttdZx3bgu0P1SMiFTHyWegRJ_aaH2B4zvNgA-tktrHVnGgInG6sr1oJlF6GFf2vkegIgRyXgFhgM1NDF9EdpZ77pYjZvkPHvueNmKCVs5CQJLSiGfz-fVLr3hHXCBXIcIdFzkqgBU8Z67X-vgaai7pd6Z-4ZRafNwUDMl2WSOeK0qsu4KURQS7p4Lj_1o0xF9UHKeOfOF2eOf1NZ8tcd_ZhbztevI6r-hdgoSeCgbae7jH9TxWlXl9PVxOmIiL4qRyAtMfNVL6TLCJuHbuWs6SP751p9iQ9jxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V5IE3RLvXsgjyrRagKXjrUOFwUu7tIp-OETkmiXzlQ-ApCnv9qBhcOhqzitrr1k7c6f1rhvsDnwTa8nzD8ObReS47Kqw-GngwZtiaMMwW7Qh2CGC1HWzyEq75ufd497GDUu5N1IBj1ajpepu8AXlLxlPaocsleSL9oMfnmt0ykjglz92Y-Mi8ZZf4c6CRlocb46SJHjqP45Ze5Xx-8BuGD3uNnTubFSUYhx8UmekL3PiwcsFPPmv7WCC2ADbXWQGe54xzhTTeyCjMu8vyiua5uqzA5vLZeHm5bY5NvWTSxEjSGpqjCnkIneAALQmpdsl6CpmzpFk1Rc2VTPRW_utEQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🌎
برترین گلزنان جام جهانی 2026
:
🔻
لیونل مسی : 6
🔻
کیلیان امباپه : 6
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/97270" target="_blank">📅 02:10 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97269">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ey4f8sOz6qKC-A4Fea-RBujgd-z4uH8M0GpA-jsyHmvmIgXbDpCsaL_KlermjaRn7xA4EEkGsbLBMd8r7egnSHzeeaeIsxXTaH7EJfRV_QgXJgAwCnQMOhmwDwO2wrpGjmeRc2gBnR2xJcz21xjpW2n31XCH7ubUZrBku44IG_53JYOxJ4ZvSh3PHSDJnT2H0YojL55nNhLe_2EZB99lXVSI_9nSp8h8aDvlJjcmlC8toVLpGqqOaRAnrPbK4p4J0kYFOjHR8_F6aQzQHW_RId2DrIqdtp3Nvq9r8oFXWWwuScViF9ILdZeqZIv5n-_ot0QrL28t9rClPoNnnbqPzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فرانسه به اولین تیم تاریخ جام جهانی تبدیل شد که در 5 بازی متوالی 3 گل یا بیشتر به ثمر رساند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/97269" target="_blank">📅 02:08 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97268">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59c55785b7.mp4?token=cWtxttB5MHA_YTxsq_3S-oEaKInl7ow6C6YREd4X10WGCE0nlWsri9PRwWvkPenm5t7E_xu_ZONTt6pYxGZcqJPsZRBk-84cUSlO9YnR8wcrnIOkt9rcuzRRrwp6zAAZEoiYXIeg2EHrHUdRr4vFZZdyWxY5XgMXTmhO-VDeHWiDG3AxIF8ZEYx0MVhKCnKfwACPAjvwyk8PU91jvUhER8iQEyRxm7JWVMFXMp37oiGBCwvJP2kfwJXKNbfI4GTxLVDPVs2yYAe83jG-SobfdlWnspdQognaC3yA9ul1ceGtEiDLg3qp4bpDgAxyKYt7Kpi7PzUbpF_7CQY6UuCFLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59c55785b7.mp4?token=cWtxttB5MHA_YTxsq_3S-oEaKInl7ow6C6YREd4X10WGCE0nlWsri9PRwWvkPenm5t7E_xu_ZONTt6pYxGZcqJPsZRBk-84cUSlO9YnR8wcrnIOkt9rcuzRRrwp6zAAZEoiYXIeg2EHrHUdRr4vFZZdyWxY5XgMXTmhO-VDeHWiDG3AxIF8ZEYx0MVhKCnKfwACPAjvwyk8PU91jvUhER8iQEyRxm7JWVMFXMp37oiGBCwvJP2kfwJXKNbfI4GTxLVDPVs2yYAe83jG-SobfdlWnspdQognaC3yA9ul1ceGtEiDLg3qp4bpDgAxyKYt7Kpi7PzUbpF_7CQY6UuCFLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل سوم فرانسه به سوئد روی دبل امباپه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/97268" target="_blank">📅 02:06 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97267">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">دبل لاکییییی با پاس اولیسه</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/97267" target="_blank">📅 02:03 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97265">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">گلللللللللللل سوم فرانسه</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/97265" target="_blank">📅 02:03 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97264">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">امشب اولیسه تو گلزنی طلسم شده</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/97264" target="_blank">📅 02:01 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97259">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gJLIeZBd8WUtwyic-0oEBy4C5kwlgfxsaYA0gRSZ5DdDWCEq-jIgwFPwzVTzFHvQgqoN8ScwIqg5EaE2JyBABdeTS_EhbKR5GYgEl5Q-XcQC3ksMy9PR0mJCvn5gpMagDvuou5tzBhbrOEQSM1PQBRb3dRYxsx-m3boqrZwIEWAGXqg-wx4kjWi-4RhjRqs-vLfeVQGa6_kXPqanz8EX9_dAnAfT6uFVkVTpB9yF6FxWmlLTBRBX5M7KEpGeLK1gl_hdNHaKvQh7-OCNILuAyK5rFU2eFMc3V74MuIaMWkc1AOfi99C0IhCwI418gwVssKq2B0KoouwWTLcAV4JQrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nrGwuyszyfeYYI1u5dCX9L4KAsyKEgQwhPYUO9oqSOIyE0jay3sYtRUsOWHey7BAa-yPmdPIRm-pfpVPGuWxL9JJcKzQiBM3JnUJYrB9IxVDVOJoF6StSzUXMOL9SljagkDtVkGqAtPpAYvpHkompAs_mrD1kJ9S-6zqJFaXocaVmiMgJ0aKEknV0kF52ua8NebeB0QHMN5yJt1kHhq61LXkRdYfxpaEoXsXOuz3Tq1aMP9K02uTv_fESpipbnfF71DDU7BM2FZ0vVH6qoOOy9QXpkDf5ZZfFFsyXJdmnw9imXjCAjrAZUGpRAZwDuCfemQ7tdGRQZIxjrTjPR_tuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/htmarO3nt98G8vjQibozQ2iJ1GF5AXOQ0FjqMmrH0WHKAizmmiddAc4Sjtyw7eE6rSYMBe9fYYZ-Uc3uRYx_ncp2nvinKn0UERJaXpl8lkoNaw5_6n9tuR2IFfzCK4B4z6mr6v_T2PTIrzSMQ6-6uqx9lL-J3VOhQWg6A2mllAigyNvOgMDWrmqKek0pZuOxLyMrsOf64UlUCXmj0tZ3QTa4GsQEcenOij0Dh6jeG_U5YWA3SDE06Ok9EqXNwcR4DvPy6UfsYvpyrbHmiZc1oATuyjnwI5HQx39w71Gklr8Kle76fdgogqDEVllZeoFu3ShVhXJnN5jr49aBqCXLfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/abj8-4uXQI7x-FLIGJw7iuvNddWUb0dGLQtXYbm5udnOZABCNybLMRlMXogO2rpTYEQTAA_rE4I5cdREKB2Pd8jyRT2DpfXIQNwRlLi3ColrApsQXtIKVaqRkPJ84GWLRahSwcRiGYwpDUTahfQi6omC1Bu6ojzYRwAaeT6KLackT53Thx0Dv1voXfEmszB-m0poKcbbRcr2Q51s5JTO_vxPCccZ6EO8NnZqKjI-a4dkilg8Yz9xavyVGqL7oCUDy_0bMqvbxsE6v31bZDAKl9cfb2CQc5n-yEu1XoxhYGWq-H8UXHpexjORdgP9INBp_FE9zb4NcvGHrARB2dCIZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LKGX7iwXxjLB7tcm7SDWVfWKBnEGP5-HThaE3KX_uuJsq6ogaYARkdh8BjdwMCVRzEErC-eqNokQ014UPw9pqcqw0iQC74lMxzsLjaQdqb6Alv201gmsQ9PGWXq78ljzU7gzY4GySOCjslpMVQt9JejW0di7V7oze3LiH0fMDrXFtz_hU-9z4JtlCz4d-3zG1vUrfszrPR2n3heZEIbJDsTfXUMNuItmmZck7Ww-LUVzBVSAHbU-vhHtBpF6g5KDVrbQ1xAabNPNi0e5Kxp0GDB6vW8jfurucZBKPo3l7yBgG_gIq1-Vo4rf5XrNNBzjEwAPl5bN1XlyzSRV1hgqcQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
🔥
بازیکنای سوئد و زیدیاشون هستن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/97259" target="_blank">📅 01:59 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97258">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W0qmUQ5eVSvcrXpjPNbeRlmes6oVi9g0yP3asPfAwnExuUc2hNMIjSKKjAJHTHP4w5a3EHwDYZ-j0UNG2vGr3kwG1rQ5phgg0TTcFsQjkG5471vo6-KHuTDmQGSdEAsoivdxZSDRQl1xbrXGmcYH55peF37WI_uoEJbP7aXuZTVCBxj2xdNvA_WyNE8uwquBWZNEVo3-AKpiRxIZEvcc1ZztPKAjjq_nML-SsEttpACzrFrfgPlpMEzbsterMTBGXXVzFUHhl45wZ0x0H0qql9dSlgLNmZj0CW1vh7Cqqbd-75KUeafs1BD6hykpsR3OrxJ9opoQKrNvoTDQEJYOKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
🥶
🥶
🥶
🥶
🥶
🥶
🥶
🥶
🥶
🥶
🏆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/97258" target="_blank">📅 01:53 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97257">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">گل دوم فرانسه به سوئد توسط بارکولا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/97257" target="_blank">📅 01:49 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97256">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">چه تیمی توان مقابله با این خط حمله رو داره؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/97256" target="_blank">📅 01:49 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97255">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AGYZesG7NejetL4SQ1lsD7iltqgxOEj45_5DLZ9Q_MPnA0wMhupX3RAVOidXOE31jzmlxVVtwIbrHJTsQ_eQdLNB3U6fHwvXu0DevwiBJuUeCmoVqnmiehZTZ2KS6xgIjrnYaHO1PsiOuA1-5nFXOsN5Cq-ru6mFsNStCKb41GtWlBpFvjYeQ1UGqyl0LenZZGpaw2XUCPsLURVaq6yqOYgzi5l4ykapgXlB84OPVgQWgwXT8WuhjTrAgnnoRuyGPo50KRNrn8l_CqRBjt13M3Axg0s9kzOQjsq_fQDHXvY0P12ESCpKTiFSANRQ7YGKBxABJfB-8ywpvuuCc5NLeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چه تیمی توان مقابله با این خط حمله رو داره؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/97255" target="_blank">📅 01:47 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97254">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">بارکولااااا</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/97254" target="_blank">📅 01:42 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97253">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">گلللللللللللل دوم فرانسه</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/97253" target="_blank">📅 01:42 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97252">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">آغاز نیمه‌دوم بازی فرانسه و سوئد</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/97252" target="_blank">📅 01:35 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97251">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/myTqYa178QpGk4G38UVE7LTXAFTQqsORUUJYglCAd2lU--E_NvsXiPVLoIFrQSEjGLO8nU9gCGV4hsOlz2UbJXSv5C5GxrUDY8Kefr82Yy8CmeEgBJ3R40plLbDzYl0txjsdJr0N-AMD5h-NCjKrtTGF6VP2IqYt5DhEBGu6XrgH06W3A4BFlXQG7EEjVw5vgQNAJAgOoHKOhHmF0C5EWhqMYdpxKSZ-6rF7BgK75xc-V6SjwsJMHVIKZCdEQ6PVXjFdG_Mo72xcWokxGSROIXmwee0jJ_tWKIBUWBK7no3-LxlervOKbxMl0puK-oMFGr3-nuK4P3rjG_qMVNp64w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
امباپه جوان‌ترین بازیکنی شد که بیش از ۱۷ گل در تاریخ جام جهانی به ثمر رسانده است:
کیلیان امباپه در سن ۲۷ سالگی به گل هفدهم خود رسید.
👑
افسانه لیونل‌مسی در سن ۳۸ سالگی به گل هفدهم خود رسید.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/97251" target="_blank">📅 01:34 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97250">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚨
🚨
📊
🏆
دیکتاتور کیلیان امباپه برای اولین بار در دوران حرفه‌ای خود در جام جهانی در ۵ بازی متوالی مشارکت مستقیم داشته است:  ‏
⚽️
گل مقابل سوئد
🇸🇪
‏
🅰️
🅰️
پاس گل مقابل نروژ
🇳🇴
⚽️
⚽️
دو گل مقابل عراق
🇮🇶
⚽️
⚽️
دو گل مقابل سنگال
🇸🇳
⚽️
⚽️
⚽️
هت‌تریک مقابل آرژانتین
🇦🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/97250" target="_blank">📅 01:33 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97249">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/soanYvNEaLiN3jDImshTMCxDFWeBueMbZamBYkds2DLBgmOZ_SEKUHIpdVOl9_UitkuQ4xR5blboL5U6Q1qs7bRsBs8JgyzJK3fVAfRZgamaGO21GMTvEjsjIQ_NffnZHdw9YyFBQJKR7hjJ0mireZnaMgcfWvB0GyJ-EATfWE-3MMpXvuFI0OsVStgKgh0xhRIpaHRzvB7bngs3A8A9D6qB4_CNVc5KZVfl0HL3CLUJ3wXyE7EMMg9AJTH-M8q2XkLoui8O-J5yGkwaxZSbImNQ51o55rl7QFMryOdhibjQCKhcYp7mIeJnTpdqwoZFIgfs728rMVvvOF4KQlJFEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇫🇷
📊
اولیسه اولین بازیکنی می‌شود که در یک دوره جام جهانی برای فرانسه بیش از ۴ پاس گل می‌دهد، از زمان ریموند کوپا در سال ۱۹۵۸ (۸ پاس گل).
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/97249" target="_blank">📅 01:31 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97248">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ozhPrKotjnm-ITed8C98B54rOYghI03FeTC6v3t0ArnYghU7UweQlb4THZrzPGxrw2aiVTvtWWbY3fvjI12Xwibslwm5GA_Kl0Rq17vHZgPxvbNmEJNytGNSvs3KQTZTNqwXzIYv5iXsNmC0V0AEi-rmHmqlWG477nMV8zyK3_X8rG5wKRM60mxHpAaDaGd9o3DHmfLU7X3ehWhAanL4ZaeTEoj9qlelFPo3qlYYmf4iygnOA7fvZpKvq7szMmcImqsKkwKGLzwX11dBR3D3H8on8J5mJ74aS8TSzdYr1ORIBdSLeRit1FxuOQNRqbL79zFS_nQC34atw1SW0ECf5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🚨
عملکرد دمبله و امباپه در جام‌جهانی ۲۰۲۶
🏆
🇫🇷
۷ مشارکت (۵ گل + ۲ پاس گل)
🏆
🇫🇷
۶ مشارکت (۴ گل + ۲ پاس گل)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/97248" target="_blank">📅 01:29 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97247">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚨
🚨
📊
🏆
دیکتاتور کیلیان امباپه برای اولین بار در دوران حرفه‌ای خود در جام جهانی در ۵ بازی متوالی مشارکت مستقیم داشته است:  ‏
⚽️
گل مقابل سوئد
🇸🇪
‏
🅰️
🅰️
پاس گل مقابل نروژ
🇳🇴
⚽️
⚽️
دو گل مقابل عراق
🇮🇶
⚽️
⚽️
دو گل مقابل سنگال
🇸🇳
⚽️
⚽️
⚽️
هت‌تریک مقابل آرژانتین
🇦🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/97247" target="_blank">📅 01:28 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97246">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hr1cYY-U0FaExo2wTQSINBNv9d75XRmo7cU9qggK0p6BRbAyQRJmGnFtb6j1-dB5v72yy200XNdttCY6yc2E1p7bOgEQHekHy17HoULIw13nUE8pjhv6OHRdz-vdoNy5sy9ix6kPFSUirowteZXXA7oMngJQ8v8Szp6JNvN0c0pHbduWGPNG5nH-m6W5Y5YnVb8WKNvf1tFDWYFD4p1C67ZxI7SSWtABGp1wQWaYUjoGS1LEJv-SWAIUEDTYCOjC3DbHh9KGZwLW5b8qsWTRAqoXeF4Xqn2MVhNznWqMGQ0eSdmgBLQ3Nj0x5W-BNwDGUra1m3B7FiKVzh5aCvzLcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
📊
🏆
دیکتاتور کیلیان امباپه برای اولین بار در دوران حرفه‌ای خود در جام جهانی در ۵ بازی متوالی مشارکت مستقیم داشته است:
‏
⚽️
گل مقابل سوئد
🇸🇪
‏
🅰️
🅰️
پاس گل مقابل نروژ
🇳🇴
⚽️
⚽️
دو گل مقابل عراق
🇮🇶
⚽️
⚽️
دو گل مقابل سنگال
🇸🇳
⚽️
⚽️
⚽️
هت‌تریک مقابل آرژانتین
🇦🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/97246" target="_blank">📅 01:24 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97245">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hPGhjNHfzkYPKjnP-smZHQSvi4BnDK2Ml__Gc6sSIfinZp0_9VLnJOtMbL1mUvgqHd44u-LRCZglD3rVGowz_tFPdtk2UxLTgznnf-yuDRkAWZsCSKvc2sTNCtCzGPF1Bie1pTJbuxRDqlSlyG_0Fva545XcEJN9hTi015GVPJyzTeth3TO0vKjpAf-xQYsvF-N8hpX1sWc_MzRlQMu-XsjL9VOqjw_4OmczD_pe9C5g4MgGGHX4piCw4y4MulUZoKs_4maf4j-2jSZ6GcpNux8gGhUFhratdaQRiyrQYRPRskwfkxHwL1pDmHpY4ELcbPxr-HEC0he027n9xL4Q-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🏆
🤯
امباپه با ۹ گل زده رکوردار بیشترین گل‌زده مراحل حذفی جام‌جهانی شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/97245" target="_blank">📅 01:21 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97243">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🇫🇷
گل اول فرانسه به سوئد توسط امباپه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/97243" target="_blank">📅 01:19 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97242">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/49dea00f2b.mp4?token=Me73D3o1mtdplTCF996cKhrbGV08FiW780lz18LDAdaL1VXFpOIAA4JwUJ3l6hqg9PhFNgrpcSWbHmn8hrJvcd54iJZHs6KjiOz48S0-SNCdDoK2t5Fo04ytwnP-2cE5G0VVzOZVXdSjB16J0U9D60Av9HGMPT9Ed2q6Q-PTxEu1zV29nmJKCmyQt6z3b98hqyidULaUtuiEmAKrcZlIA6Axf7thlsTQI2xrwIn4JfcbRTPHvAbMwth5yedlXbHil_Z2k-VzgHdJ_vy6bBi9_mPKMnsc3qvVAOOEwtHTdHA87uYERi7-bK8TVzPzqMTInWEPjBs6QPf7yk9B2D-Islk8mXzAiNf3HfeFQtvDzDIIA7rSjXWBPgdNWCqgLbm28QqOqHbGVvYzWNTu0QQyaGFiTJcbUx-8ZwTHhsjfaYLXRLSJhhMf3t9zqlexogLt_nLoYeL7EEStUgfhYNo6njldH7JI4X6jERlW5OOUifNgjhybJMUhGimmDyWMYSgUYz8mH-aui34VygAsqVwqsrZAPZwsdQ3_1gSnRsaBTWWkZ4O0ZErWknl-6r-Lj6d_NwktBWdH0jaZ_1UCkzh5ICCdiAugVkddxWOS0s-ThSZ_ZCCllPpSO_IEdlU3bt8lBCFCiMsZHSimbt_FP7s7GcwzQpovRmQYubbLzIsAe7Y" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/49dea00f2b.mp4?token=Me73D3o1mtdplTCF996cKhrbGV08FiW780lz18LDAdaL1VXFpOIAA4JwUJ3l6hqg9PhFNgrpcSWbHmn8hrJvcd54iJZHs6KjiOz48S0-SNCdDoK2t5Fo04ytwnP-2cE5G0VVzOZVXdSjB16J0U9D60Av9HGMPT9Ed2q6Q-PTxEu1zV29nmJKCmyQt6z3b98hqyidULaUtuiEmAKrcZlIA6Axf7thlsTQI2xrwIn4JfcbRTPHvAbMwth5yedlXbHil_Z2k-VzgHdJ_vy6bBi9_mPKMnsc3qvVAOOEwtHTdHA87uYERi7-bK8TVzPzqMTInWEPjBs6QPf7yk9B2D-Islk8mXzAiNf3HfeFQtvDzDIIA7rSjXWBPgdNWCqgLbm28QqOqHbGVvYzWNTu0QQyaGFiTJcbUx-8ZwTHhsjfaYLXRLSJhhMf3t9zqlexogLt_nLoYeL7EEStUgfhYNo6njldH7JI4X6jERlW5OOUifNgjhybJMUhGimmDyWMYSgUYz8mH-aui34VygAsqVwqsrZAPZwsdQ3_1gSnRsaBTWWkZ4O0ZErWknl-6r-Lj6d_NwktBWdH0jaZ_1UCkzh5ICCdiAugVkddxWOS0s-ThSZ_ZCCllPpSO_IEdlU3bt8lBCFCiMsZHSimbt_FP7s7GcwzQpovRmQYubbLzIsAe7Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
گل اول فرانسه به سوئد توسط امباپه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/97242" target="_blank">📅 01:18 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97240">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">دیکتاتور امباپه زد</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/97240" target="_blank">📅 01:15 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97239">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">فرانسه اولی رو زددد</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/97239" target="_blank">📅 01:15 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97238">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">گللللل</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/97238" target="_blank">📅 01:15 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97237">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f91457d579.mp4?token=XKgASri7moVeFo--LNVMqhS70EwMGIEI4usdDQNQoxkH9Wns0GeKQ0fsO5vhrL3j0aW3-bFb60_gtLymzdyujBSOdXw2b21TYKpS0sPqzTeuuGJOcNRxpOCCbDwgvs5jOoEO28GZWcJ80e_wHN6jhv-Ice0rboH3X3lPT1n-2WOanFqSgVYZNekZSoMfFKHodhZIHJbBJMplOd95F3OmvLHfhc8u_WNuOlx91F7lGy5nvUfeNzfR25In5w2Jzls3czAgjcHc-1iUhwSD-XBHOdp32AuB84E_7XUmnCQZ4xsP-wfaZUIFBC9BXazDpqIifquYbiVRpJoh5lvLMAuN4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f91457d579.mp4?token=XKgASri7moVeFo--LNVMqhS70EwMGIEI4usdDQNQoxkH9Wns0GeKQ0fsO5vhrL3j0aW3-bFb60_gtLymzdyujBSOdXw2b21TYKpS0sPqzTeuuGJOcNRxpOCCbDwgvs5jOoEO28GZWcJ80e_wHN6jhv-Ice0rboH3X3lPT1n-2WOanFqSgVYZNekZSoMfFKHodhZIHJbBJMplOd95F3OmvLHfhc8u_WNuOlx91F7lGy5nvUfeNzfR25In5w2Jzls3czAgjcHc-1iUhwSD-XBHOdp32AuB84E_7XUmnCQZ4xsP-wfaZUIFBC9BXazDpqIifquYbiVRpJoh5lvLMAuN4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل میشد قشنگ ترین گل جام شد.
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/97237" target="_blank">📅 01:09 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97236">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B3gCMjcLro0XpiczxmrAVStzR4sOOs68r6z948RjRSWRdvL74KRGMpL2AnoQaAMP-klZb8kVnpBWM4pO_sc7OMFdBv0biV7sJsvITivAddJBtUiSmzdvqNIUsP9BQJyjdCqEZc6DVUcQpWLZRLuLguxEECdj8aYs6wNpgb5qJozUCO2BWA8amGeYuPAeUDtc24kCh7_zxt4STLd7tvArL7zaduJRzSo83KQWyD0-Qu3Czee7VNnc6_enoU2Cnp5xbcXE0swu0tr4pp09pol5HkCGHw8HcwC_Tew-CzXoHgsmDT-NtDN9xhU05_oUY7kvBAhPZs-imbhr4iIgrvKYXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برگااام ریخته این اولیسه عجب چیزیه حیف گل نشد این برگردون.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/97236" target="_blank">📅 01:09 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97235">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">پشمام چجوری گل نشد</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/97235" target="_blank">📅 01:01 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97234">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fsHHjDyrfdKXZh08I-hcTD385OkF-hiWcfj3gt_QqbFzhiDSUSpjC-cmY-sxDVxVErrqH7no3qUkHMgiiiZusecQSVZtoP9W3xe18csu-bpQRWstOawzNxKWNIQ0nX4xM2iz8pvYsNSlzEywmOzXetRm-skqoB3Tnr9WCQahbpso7bL4BktP1vyI2oxQ9lmuJRwUZXSaQijCs4y1_NQv-wPgRXa6suub2RUVteF6SaA1VM0LtGfeLmGYd9DloLIxO7ptIyzeZiqMUyGim4lqvlAGUUKGNNKZluCJPJFMqr-8gyHbyp5oZhxvY_YPizpGgtBXucQm5h_ldc8AvmKrQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
مارسلو بیلسا سرمربی اروگوئه رسما استعفا داد!‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/97234" target="_blank">📅 00:58 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97232">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SsbhcPKV4aTo1fszvNS82FZ5wShZ8L1EsT-uivfmoQVY66DX5g42soIjplIe9MV7kBjm1xKgtJcNLnyVtvxe4KleyhiksYkVIugz9XKybLe9I5Nzkte8RKC-YylmtI9lk1LzkELE125V1-bWiQ_3uJ4AzN4tjLVpG4vv5k4CD9oyvHNQ5z4L0rTfW1i4H_hk7ERQhB0XLqy2tuOcurtsxmus7Yx7u2TPS7_VnLoqx_VzGJp7dyhSGr-GxsMc9594rPX6Dk020ZdFXILSvQ7nWo7ug8zmCneOOP34Jmj7rrXsJaWMkPw87G_C9no4SQGjU05etbOFuU4gqBAFSCmSsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FUOB_cyZ3YVnSeYiz72vcQpSr0_RYd_akL5E6DyjYhm8bXCXz2VzqnTQTg5t4N8mxj9tOOKPMYRG0g5KOavPKjMULG4bLgwxQ_TpffkCuxpzCsiTjblmfbNEwnqF7tPXdT9DFJTIb_-0QzoZcwo8HGYWqkwRO4COVUJwj10MPLR8nfB8Qo4JJzYVVdAdWm0r4N3Z70v5McXss6i9VK4ufpQZ2EMaZ1bT7H6mh71jpVWyNdqNB-0WfdI6lgTJU3d7xsAAvoH9UCk6njgn7l_vYB39Cu2tLW93QLlpsKM008W779WJw2uzSRCsDdFMdFmwyI8kJOA86o7BrytZOpQ3Jg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">آفساید شد</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/97232" target="_blank">📅 00:54 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97230">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">فرانسه اولی رو زددد</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/97230" target="_blank">📅 00:50 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97229">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">فرانسه اولی رو زددد</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/97229" target="_blank">📅 00:50 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97228">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">گلللل</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/97228" target="_blank">📅 00:50 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97227">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NStH-Cqw5ezz81cDZqGGJtUcP3GeD45pIQGeb-pcrKBvUakeGn9DHLQRFHGw0ZXUymVR1R9JguI1_zaqoGlmLgTt_yzsGq18c9n3ClUYipNeb6jIM9-mYRkJpECpYglEGT8CRm7Qq_eSAEML1gA2cWj9ysomKWmbE0Oy5L8_laWPBNOZ_KKJkfkiYcSenWMo1L-qRxETiSRmpmr7wlwovd0KwmyOPbYAoF7g_ylzyY7kQ5haXl-Fk3eKJQOieC91iP_GtOSxGTt-fNQwkg0DtsPpUMXo5GSubHNzvfzkD7TfNwO3mzto7E36gzHqba58-6ig3pYqmPg6WJevjuGq-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇳🇱
رسمی؛
رونالد کومان از سمت سرمربیگری تیم ملی هلند استعفا داد و از سمت خود کناره‌گیری کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/97227" target="_blank">📅 00:50 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97226">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🇫🇷
🇸🇪
بریم سراغ بازی حساس فرانسه و سوئد</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/97226" target="_blank">📅 00:30 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97225">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WBdH2YXVThoEWGPtcff4vTkXCbKns7ji0924uv-U1cvOqoxO0VmAPsIHGuypOQNgWp260KtzpQRWtgwMopjwUVMqwsEswGvUuqf5MkBg4Nr8-pfFl84WT2QaYDIsGE2WZ_qp_defbo5O57hDy7g7UCYeLZNiwcd9qKOM7qke-yCxt_GE_2LxfRpZil_Vt8_tz_MxSz3pUhZXfXKsv4kb5gLgTLtV0fAk2I2HdwbJAu-BCwrMmsqIER8JjK1yMjIBN7uk0hrlHw-DhDfHNtusSNa5Xm4xQaAzldbBn7X_oswqEEDoExa0RcBKVXQQ9a-l9ytldiYy7GPPCH9go_IIZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟠
با اعلام باشگاه فولاد و برخلاف صحبت‌های رسانه‌های فیک‌نیوز، قرارداد یوسف مزرعه با این تیم تمدید شد و خبری از حضور این بازیکن در استقلال نخواهد بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/97225" target="_blank">📅 00:22 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97224">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gw9GTEUyfb-lXYm0IuqcUkP83QTbK7_7OOBaDHsbSckPjy9l-YvP84k__nb8n8Dojo3y6WUaJsKOiIck7ULjIwy3oZpV62wK5osihQkvrFOOTqhGl__JqsyANnfuHBv12Clb_5TKmZFFUWj_W8dIws_TCQMHLApN14nL9kl5siNUHaL3oRBVNV9sZQnsCrXw5sN2_th86e9Yv7NJjf-rkfi4TdGI4AqXwIUjBq_5pMgn7sAFcTliHSv8D398iLhYR6_nikjJUZuulxtJIsXWyFx4N-sZaC058SxY8JIXYC0zehXRa_4X50Bz3moRouQeCvSl5NTh4ytIKKE3iOoP1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیمار هر ماه 16 هزار دلار (2 میلیارد 700 میلیون تومان) به هلنا دخترش نفقه میده
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/97224" target="_blank">📅 00:20 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97222">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/faWO2JNu4MoDUWRaY6CcXkyMDdsTV0lAy7LyQVKzlZeLNKAjedFeZHVGv_YxsRAQBchH-teHGFKExi2SfKKTchasqCJzj7BeoL1vodVxckc4vVNOIRMH9TD81ZgeFiEyfWGCXlNHD5riNVgSKxFCbHBjiwNMHa4_JOUs6RtcDoAybb6A-WLG8CDF1s6ZdJNL-C0mS-wVWlus4qEMZUCXjglSKikooo6cFc5DuWeNlPLLqpcfS32HsjTo-OB-3VlyiXExXOiScBCgsX9oG0HTMauPW8xPBvmCu8HVvf1NhLc_PTiiSV_ePhfVCcIwN7fdMfz6aiNBcJsfhsUWl8TlCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/STcweG7CesBKhRCqeVGbffvYsi_m4mLJRtBxZnSNMnhExI63iaiA1fD4pqpuYhmKbfc2sVNmkMOyQ-0opWwMJEOR8ws07NnhLqygnfNiPD9ummMLBnVBQMtoq0OECILGU99fiDY7e73RqxHVw1-DnfbdWOzyt9jrRoikdTPjdZ0onMlw2uPc1sgCkONJ8OzCQl25-xX9xCYgE3bdiSmpF4qgbLlQXuEnCjR_jUa_pHG8Ps588i_hbZQ_8G2nHYgEYbM4_AaPCC0glFOs5JSZd2_CXJLO9y7hpqwB9J-tqXr0S0l2o35HsAGGqwpcThs4_1TfEicv0dxJgA-bE4ufVw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🔵
بدین شکل
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/97222" target="_blank">📅 00:10 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97221">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dHgzWXmFvaBsZ6t5WK-7SCoLeG8vOoCO42jMCv1b6iheuc93hQ_MziRVJoU5Rj07qQnhQUFFlMraZhI3y1oaO1q2fogeKD0WPWYKTAV32MQrNsyvb93_2K9E3ssoZRF9AirkGFN0uAXSGw65C26FyQ7uNEjG3PJmfhfzxAH3PAk-uzKprKhvUVJ3uvlWqBo_zqXxB3XSQjjL-WaHZXr3GxOnuRSC54ZBexHiLFa18U49EAaTusGXU_FC14ZCNQHRB9pun21iH0BLjlMy7kHg4Fby8YvfAcHLIEY38Suk1-ZvifYZ53IhkW-8pLjdWF5xGbiX0uEBnQL1U9-Y2T1uDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
قلعه‌نویی: خوشحالم که بزرگان دنیا یعنی آقای مورینیو و تریلی هانری از تیمی که من ساختم تعریف کردن.
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/97221" target="_blank">📅 23:50 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97219">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D4QLDmLtVeUhq0XWLZQskdH-d8Fo1f-8-849g_rA3fH0Sa7VvrpBtYoYGJxoZ0YocEHKC0jlvhWOZ31wEbzh6ybw_dWuZFxNCUP11c2VgCuC-jW954fpuolcOB1pik-oIEP5dj6n8RjliNXm0GQQF6rlXzsiXplva7666KTN18laZEHzSwxxfCFF6IvTt6WJZCT9l_exT9e60tK1VH9ozAoTYERI1_D9nu2fD4JFftf4ANR2WS9OHbzEM_a_61DCo6TbPrae5nDWf2lH8koI9fod7zBIW5UYO6gCv1aj8YTKqm7HvRCPTVUC6MmBwYOYLJzwdWJN8Y7q0rVMZAlpIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/m_znYKIGSyoTuGCxQdH58pe_Dm14tI_m07FeR6dx9aFoUscHg_aekYzTZuQnVwd0CvMWCJ60dm-3m9oVzN1TOMvx-q3TF3-oh0r9n7kWMl5lMXjaJ2uhnY8gBTcIgo8B6qnh7F4nbAuStZoy7K_fHgB7XNjv3GuAI9Hv3zzu8KNXNiXlW4UuPHi58VZtbxSAKel3EzmZalSysc09--SjuIbnW8DX5xJ1qwehr5ydyyuPuj4F4JayOOVFnjAZiB1KRdmlkhPFYjeiQk8o4DEZ-H6RZBRtfhmxpfQXvXCq7apmt8HB5O2qpMt1Q1-b9HtWPTPFb9leN_WLZho_4biNAg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🔵
رسمی؛ از پیراهن اول بارسلونا برای فصل 26/27 رونمایی شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/97219" target="_blank">📅 23:48 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97218">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c160c90364.mp4?token=F1n8Cu8jlYrAKD-_YzVo392EccsYRims1BJIYOwrn4ylUffQqHv_ddv9ZIa-wM8CQcd1z7wTOHdHf7kjkVGz3lVgISs-UbaEi2UPpCPInc3tmvXxCp9LVUEjDp45ETP1VhoivnqIXImOyVRvhX63OQUrCO4x-Un0jxZqhl669hkQl_Ys4Q7AMf3BdaQoXqkIHKDmDAKKCnLl9b3uCud-_8fa5-nAa2C8JKAxM2W6L6AjCBb9qAKd57a2x2GIKdFdStKfGe3TlsaB4G33D5DrWys_9ZyiiZGG4L2RVlVjnyt4RXOG0knofn__YKR-yrO9Wy0mHl8YEqASvrjKlTsJIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c160c90364.mp4?token=F1n8Cu8jlYrAKD-_YzVo392EccsYRims1BJIYOwrn4ylUffQqHv_ddv9ZIa-wM8CQcd1z7wTOHdHf7kjkVGz3lVgISs-UbaEi2UPpCPInc3tmvXxCp9LVUEjDp45ETP1VhoivnqIXImOyVRvhX63OQUrCO4x-Un0jxZqhl669hkQl_Ys4Q7AMf3BdaQoXqkIHKDmDAKKCnLl9b3uCud-_8fa5-nAa2C8JKAxM2W6L6AjCBb9qAKd57a2x2GIKdFdStKfGe3TlsaB4G33D5DrWys_9ZyiiZGG4L2RVlVjnyt4RXOG0knofn__YKR-yrO9Wy0mHl8YEqASvrjKlTsJIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
قلعه‌نویی:
خوشحالم که بزرگان دنیا یعنی آقای مورینیو و
تریلی هانری
از تیمی که من ساختم تعریف کردن.
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/97218" target="_blank">📅 23:46 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97217">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rY0bablJcOitrX_W11cvDVxZoeVTm9TI76D6NL404mLZpCEfXWO4PawC4LdB9hLWH21dt5MlnaXnQt6HxV8pPRWMWpQ1lUcdh7YXASEO9XoZ176BH6foPnDckTcSFnX8PaIzrDIho6hUTHw4TFKTqiSAUJMv4K2p3R8JuTxBViMRHJQ1N53hVkwK-wFK0KGyEWgx3E6MYA-2G5HbcVg7T1C4_mT1hO9a4FhHq2Cmt0C8YkhLkAhr8MBMjaMKmgPry40oNlfksoNHb9exrF3QSiW2Xt3k96aoj-pus-_wRRYihLmYGi6zoNAvDFnoCl16kNMS1geKSbPgKPSsRqiPZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇳🇴
ارلینگ هالند در ۱۳ بازی متوالی برای تیم ملی نروژ گل زده است:
⚽
مقابل اسلوونی
⚽
⚽
⚽
مقابل قزاقستان
⚽
مقابل مولداوی
⚽
مقابل اسرائیل
⚽
مقابل ایتالیا
⚽
مقابل استونی
⚽
⚽
⚽
⚽
⚽
مقابل مولداوی
⚽
⚽
⚽
مقابل اسرائیل
⚽
⚽
مقابل استونی
⚽
⚽
مقابل ایتالیا
⚽
⚽
مقابل عراق
⚽
⚽
مقابل سنگال
⚽
مقابل ساحل عاج
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/97217" target="_blank">📅 23:34 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97215">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TDAHFiqQYl3kB7_Ex-af0aB6S454OR8t7tDhwEayjYEGINpsnCsTmaZeABv8Tm2PUfrtMAyXmFgoePScRRk3YpcJRQYDFOc32vtHnd2PlLlBfCbVMkbiGvHFVJABSMkcgM6t_D_UDiK7YMNLm5wJGwXiMxjh8FNnkXCcdf8SXFZXEiR5RbUTLtRVa0FPegw00BTCQ0MGfcFrRbl-W2Fu5Ek7KdL3lAMQ8M5ZYQWm7errmJXQeFZqBsFcadgoNJ5PJxtljMghQoOVVbwWK-4hnLlAUlQt-yYG5SZqCtMpHPuG_8LdAdXHTEw6SivR8eZ59lzFORLdb8uhCrwLhyxEKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RTxBpTYCixGwtu4hFHHf0yQbAjETPylXrBEOe7CQqeaCXRKZ5ku4n-7bVGrzdIIetgCHidsMRzGtgTLt59wgKtZqDzq2cTo-fS0rUbm22CWQszWHf9hgdSVhedfp3E-OS_xHKPG3RvBIQ2UufOVNOJh1LDnyTYZReLEYGRN4-M_bv8RU2UXq6rkJyWfF_kje26LTjciLqr_DI3IPUjqEikocmaUJ1_y4ovIIwf_YlBTgPh6BFtQwkpeB9UWiCIHeNihUedOTVBU0XMxXIDHEnMjr8ZF-Jm9LTaIE66LTzCJ1NjwOkMWnCFMQlkoPNq1csxWlVe_GWvm2Otz_6LrWbg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇫🇷
🇸🇪
ترکیب فرانسه و سوئد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/97215" target="_blank">📅 23:10 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97214">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c96ecc5660.mp4?token=WALDyxtvkhux-LoudyzSizdGszC0Vgk3LavG_9xdL_Bj03cW40jN90DcUbBhMsFjlknqCN8dxixgGshQHvvWyWmVzIDwr5NjjhvA15N2xm0Izs-kRiyNhxaXxXOqy5RX-xbOLZVk98HXlhhORuaFZWqz4-KVdmgPjEcvNBTI_f3J1RdFuB67UHy0KwA0ogldyBiKVV6-XlE7WyT40vHjCg5P9lonau6G3jFAwhcBUaf-X7nxUMxCiVCh41IqBqsi0EiE27t_m7J5QGa7xRM-UeHQ5sIsOeYMOFKx3Mb39hunPcznX78FoQs2MpsTaQXaOq6DSZRRT6sy-0TLhq56Mw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c96ecc5660.mp4?token=WALDyxtvkhux-LoudyzSizdGszC0Vgk3LavG_9xdL_Bj03cW40jN90DcUbBhMsFjlknqCN8dxixgGshQHvvWyWmVzIDwr5NjjhvA15N2xm0Izs-kRiyNhxaXxXOqy5RX-xbOLZVk98HXlhhORuaFZWqz4-KVdmgPjEcvNBTI_f3J1RdFuB67UHy0KwA0ogldyBiKVV6-XlE7WyT40vHjCg5P9lonau6G3jFAwhcBUaf-X7nxUMxCiVCh41IqBqsi0EiE27t_m7J5QGa7xRM-UeHQ5sIsOeYMOFKx3Mb39hunPcznX78FoQs2MpsTaQXaOq6DSZRRT6sy-0TLhq56Mw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تو بازی دیروز اندریک بسته آدامس انجلوتی رو پیدا کرد و به همه تیم آدامس داد
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/Futball180TV/97214" target="_blank">📅 22:45 · 09 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
