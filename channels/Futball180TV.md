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
<p>@Futball180TV • 👥 674K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-10 00:42:18</div>
<hr>

<div class="tg-post" id="msg-97226">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🇫🇷
🇸🇪
بریم سراغ بازی حساس فرانسه و سوئد</div>
<div class="tg-footer">👁️ 3.05K · <a href="https://t.me/Futball180TV/97226" target="_blank">📅 00:30 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97225">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qtucdZJ_I-QwPB9aVzllmzflQNMEIaGBiikMLYeV-Cs61UWDa09EJ4i_FsVtOVcfjmgSJH4ve9BXd-GlQjRP-aSR96qzhI2S8YrINEUOF5e_fIG2X4vg-8q6aEk61ghTVYHXwf2iAxRLYmkdag5Cn54XJ965BK5hbKamaJsLRLGiEVTwtfK3Mwa8-mqA4VzQ6xVukKrChEVu4WuQGG5ca68PbICFrACRBtokvnSaAo7DnOv1lJzJtU6LFWnHOc2zNwwlCnPfvsrI7ZAu1N2j5rzlpgh2iYsT5AsZauPffGAE54kuznNbkqWHfL9H9TvfiN2jwPB6zhB0_N_dK6uTjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟠
با اعلام باشگاه فولاد و برخلاف صحبت‌های رسانه‌های فیک‌نیوز، قرارداد یوسف مزرعه با این تیم تمدید شد و خبری از حضور این بازیکن در استقلال نخواهد بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.68K · <a href="https://t.me/Futball180TV/97225" target="_blank">📅 00:22 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97224">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EsdnP11tBaW10xdro94qOGzjSuHKsu47ZhMvN1wbwlqxfdI4ZKc_rSHNAaLlxg4MJiKOG8v0FhyZPqvikH1PNHvkuTyvJiCbnZowZn4tH4ntYJ7Ks8qjZarutCqSn7-76T_rZ40w8XkfuJdRQfWa8dQVTFzrFgohNuPVbwvKMCmW9DQUQEXiqoTGyKef1WVdfk60sOAFLQcJQxzvq_jxLCYXLsh97HFXzvUPhrG0HVEjQndiH3yT-bX0aIy1hynbUe_6O0pkOmZ4oKZS1q1YTWGjr6BtblUo8mIF12_azECyU-EZAu1lS1cbM7GwFJ640YcgzK_yEYqNUKVrt3xXgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیمار هر ماه 16 هزار دلار (2 میلیارد 700 میلیون تومان) به هلنا دخترش نفقه میده
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.6K · <a href="https://t.me/Futball180TV/97224" target="_blank">📅 00:20 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97222">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C02Qau8UPKu9O2I06dAZFnaCAIsBbaFf1xb0ueO-dxeMYHBBEk8D2vfc_pomzBcAHr_lfyBw0rIo9cuJ82s4dClxAtkpsUUy0rI_cRnkWq6vMAbFRm4FEA18lDE6i4c1BEl4bIXc7bcHPMQH75JJjquF2iFBDHMKmGBZSGmOKIe4L-pyDZMArfh9rAt7w6W8NYENSwE_N0wKypXpcp-XoGFaAhAvPiAyuNIK_-EafG3fHtTpUaR1waZuSOl2B04ktAoEUUkdeJdFjpYaJo7UpEEFNIkFZxh5P_DjMDkatRhZWA8TkEXCeTCjNL8s8csL9JG6H2Z2BeBmfCo-M8dv9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sAGuC4CMmkT4mYMFQAULB6ZPKheU98MJTUjaygmiVRM-NWhhtAy7qv1hNIO3-xsvnLHaz_bdPb3vigLGm8LA71xzoGVwASgkSz9Gg52EtCzNU8h_CrrOc9ms9Clyk8-AzNG-dNEugvBAAAaykXhJaCgvHfjOo11HAILs_o0EFrvX3bwu2aU6yF08xjM-RnAOzFqE5WzKDSAuSq3KVcg3p9sMeFrG96L2ayXpxAnw-Cp-OsA6jP3Bobx9zx7Lk1tFqdDfTODRPlKxovcR5lzJMtrVxNGquYFu3s2vU93zFMRrsO729T6gbMJfC8Z5mCJq-0tTaINtb15a0kvPoDaVjQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🔵
بدین شکل
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.07K · <a href="https://t.me/Futball180TV/97222" target="_blank">📅 00:10 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97221">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QJG0p5FajsB-4Pt9n0QS3Mk4V7uqYb7paTQYrwoes4f_el7chi2FJFc7V3vMswyIXzPlpVh-BwEtGwRU55277aqh38fQQJ4Z3FwSfjXst1ZFW7KmX5PZ9AU0u-JiGTwclEUrVEFWZYkv2q_Urf5aiMQK-ydp_lluoY_WEIDb7h034PMFl4rQ-0ZLJg1HT__l7iMqidYcw83v0DUj52Wj9OBzoWRxRll8gcJilAt39Q11HI-aSPAHqhsFRBha_oFT6TLBLF6yyJIoqFFDnLESl9y2K7ghdXl3rlGF1TeEgAPaT6OHLL2CCK33UeJJKjcWppPthP1dvAgW8xIgqCJpYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
قلعه‌نویی: خوشحالم که بزرگان دنیا یعنی آقای مورینیو و تریلی هانری از تیمی که من ساختم تعریف کردن.
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/Futball180TV/97221" target="_blank">📅 23:50 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97219">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X7-Xql9tvLbUqF1nifYT0nBTJf5K3mFs6V673ivwppKzUgdZuvDDn1uf6YnCsQwMfZBYMI3lqDgqBeQcs6VVwA9Rc8oxC_FhPLOKtphtOO5oYpc39Wal7IaeNbASsX_vmyGDG20oi0lVwbO6_65YBNowv9AkOF3EMcBh-24tCPQgbHShmeFjSsPzh7Nub4PitpnfVSXLsC9LKI11bL5W9FEdCc1Q6tRZs8JgtDGayNfscI8EGQmrCxwH3O--6t8pSS2xa-flBiLeEm7jWXQGBgrU-DoPSnPTaINcEnNds7RcUYGrpE-o2N1bwR8t9P26SJFByGbWUWqHfdyItCCf9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G50_AGj72z6RCTAhf13GmpZwPYKefZbQjytEhCzAfaOFW0Hmetztqfw8O-34QnzfF6bHi8XfTDzikRNbXP5USl0P5CJ6DzPb-fjBBVMNPWRkBGqejGyE74ULeS3NNHcTVoRZEMwQo00Z5gaaO2NX9vyvsC0-382n067YMOanFfig-q54DVS1wZhpkX5fZKLumIfOxRyQFIrUgxQ1K6-t77b5RSWDjzn7HI9HOyp_l0lAahM4p3GFyKgeeUi0prqIoGIRJfpmE8nntLnFzHEIbdKWEJF1nAOTNKHrBiZbMRgmNro_L69QJlX1VhpeUkrnD6rVmFDcd66_vN72-iv7RQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🔵
رسمی؛ از پیراهن اول بارسلونا برای فصل 26/27 رونمایی شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/Futball180TV/97219" target="_blank">📅 23:48 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97218">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c160c90364.mp4?token=j4hWVw17SevNwcfiV3Z69cndy5KBY-zdDe_w_qqnuZ3EZV5ruLVek8FPRe_7vdq00ZdCQDaSyiyfG1kJNLjLkMX0cxK25lhE1XMsPvaqF94a7AaymwPS4Lm3jo-ETTORCZ5mT7kfqh08Q4gHYX2NH7Zt_fW8FDNduxEdpr7i4RI8WfHZ8CtZ-LgWroVoGdQUxgQRmzEK9n3QVCj3e0oXsqqAYPbL99tERIBHwPCbLyWHcGf4a_wHLQ_aV_3IdE2c4phL2OtYEmUxoGi25xBIRXdSPkvifIPF3MyTtyktHtCoBQ9Ix7jZ9zDl-jPnqV-Urbs50g5dvlKgUQjAc8-IYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c160c90364.mp4?token=j4hWVw17SevNwcfiV3Z69cndy5KBY-zdDe_w_qqnuZ3EZV5ruLVek8FPRe_7vdq00ZdCQDaSyiyfG1kJNLjLkMX0cxK25lhE1XMsPvaqF94a7AaymwPS4Lm3jo-ETTORCZ5mT7kfqh08Q4gHYX2NH7Zt_fW8FDNduxEdpr7i4RI8WfHZ8CtZ-LgWroVoGdQUxgQRmzEK9n3QVCj3e0oXsqqAYPbL99tERIBHwPCbLyWHcGf4a_wHLQ_aV_3IdE2c4phL2OtYEmUxoGi25xBIRXdSPkvifIPF3MyTtyktHtCoBQ9Ix7jZ9zDl-jPnqV-Urbs50g5dvlKgUQjAc8-IYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
قلعه‌نویی:
خوشحالم که بزرگان دنیا یعنی آقای مورینیو و
تریلی هانری
از تیمی که من ساختم تعریف کردن.
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/Futball180TV/97218" target="_blank">📅 23:46 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97217">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T4vAH6OkBrxwVu0lO5DPCZJ_Hk84P8120kHWHoCVfCkvlL5yzrM71B5ZUu-yVFyMpzyisw62h6cOD5Uw5N7RDZzqgIioHhTBSDSbdomHSjM00OoxUcXP_sPtF-05lA2nktrggyxRLhDvqYYlFkssESVaOqcA592OXAnYdS7-1YuPvNl9pCXSgMa3gHLSKHPkO2_IMqeRvKsXPQEYnBwfpihxjXT4KzXyW-DL1paUq5yi0123bvr2YcE5tw4cNYgC46wekqhBbxIGvuh1KIiAfNc9mhatbH__eP8UO4_bpWBo7xyocazViOzPKkDmO5SCo4zS527_7pYJrJO8LiiCyQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/97217" target="_blank">📅 23:34 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97215">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QC2hQfsoxuZWXCKxgy7XPU9RuoQWHTdTd_rbbxLva3DTDxskpHO3lDiQ7im0EseKc-5-3S606hRUthW6fwv3ACef117gS-wHHylxXI9nGvqf0uPt2_CxCj7SkGHPnHafGQMMGVucFQmXrxKY6minJVt--6C6qe_E3EIXmc-XF15fX4qhvlquf-WkOyVWDlXxinVwG1gdTwZrANFPMUMLB0_FON6fICumDUuqOso8wYgjsHd1VkpESxg8lYJHA2N9Dg1HQ2UYlXTWLwn1XmpmNX7fYGDgXscYhRp1u9-9k7CBO8xG6Ho1gUf_lRNnnZMwfpB_z39NahlqfnrpT45aTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h3hGjdxUFD3tDSecMLbxtZi1NxLCP5BffPDJcgG-SJKGvqADHg9CmsAsa-2lLK_8ZQEgNbNkJUl9foQ_UdNzdiOvL0b8BZYmUzJAJAmcYbugseT1XeXzh2-OaT5XU8BVUSmgDacWvTZ-2s2q5PWdnu1JWpfaWSY59JdrekYeLSVKDYnU0gZY_hYyj3S7gGfuYpVyOdgZGw8wjf92uWMk84HvOZ3pdgZFr7UFb_cFgd_AljRx4DGJLbbAn_QfrkciEdSqbmhY_2M7FVU2y2eSD9VGtNBaNsxZd5RgABNFCuugwSajegkiZf8peVT4Zyedl5XWTPYTSplcmH12NqUQkg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇫🇷
🇸🇪
ترکیب فرانسه و سوئد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/97215" target="_blank">📅 23:10 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97214">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c96ecc5660.mp4?token=MP8s6kVjJJbi6etWd19yEVla0vtkppmhtUSv-iHgi6944LTvsHGtSqaTaTCfOZiO3AXbfcuQe0bhG76Sk9V9XiSaOi6AuT59YTMdtNwBYvpScy9vduSHIiiLgrWJKDF5kvzh3SmYSqp-n191ZXQS1yKuNkxCFwwGzvWcldCfoAKGsFPI65POHCKeaHKeDwsvFMVl-iqD-IAe7hFSdwNxzpWlNhunbOXi9_-WMUqQL9Orp6PnkT4xg92nRcwfEZO5IV3hFXVmwbWUl45IBAWN4ONTaVuCWvZdXdw_Vf-_NnQc3DKnCrmqteJbMIswzYnt3n7BGbACOueA0fAUHK-uBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c96ecc5660.mp4?token=MP8s6kVjJJbi6etWd19yEVla0vtkppmhtUSv-iHgi6944LTvsHGtSqaTaTCfOZiO3AXbfcuQe0bhG76Sk9V9XiSaOi6AuT59YTMdtNwBYvpScy9vduSHIiiLgrWJKDF5kvzh3SmYSqp-n191ZXQS1yKuNkxCFwwGzvWcldCfoAKGsFPI65POHCKeaHKeDwsvFMVl-iqD-IAe7hFSdwNxzpWlNhunbOXi9_-WMUqQL9Orp6PnkT4xg92nRcwfEZO5IV3hFXVmwbWUl45IBAWN4ONTaVuCWvZdXdw_Vf-_NnQc3DKnCrmqteJbMIswzYnt3n7BGbACOueA0fAUHK-uBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تو بازی دیروز اندریک بسته آدامس انجلوتی رو پیدا کرد و به همه تیم آدامس داد
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/97214" target="_blank">📅 22:45 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97213">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">خوشحالی معروف نروژی های بعد از صعود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/97213" target="_blank">📅 22:44 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97212">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f0f902f8b.mp4?token=eP1GzxtDkngr-GYN7pga8dlWAVGDJfwaxwLUEQZEQny8pmXGbmUGhrglp_aquFWBtVKfgx17luVdjHdfJukc9b_QkthcnlKcn_Ylxoajfib47dmxIbpTKKBLYdQWSVSsyOOuH71hdUUpybRjy0fJ-hzi205BUkyvxz6jkufKyVNumJMsP7NukXt2J3yV5Jxikyxat1JbqD9W7f4RFvYVYmNnJowC0sdGuNVUEzHQGFyNBSL6eUlc0TemZoUZFk7bxfYVGDzjqUt9pvKrXRVN2l2yZBPyYVb5Q0Nox8l7TveedmReSWK9HDhSTlp-TQtMKI8wlOI_wduC6zXclRlz8G6oiR2SN5g09I0fjrvU4BX-gkMvPdt5FaPpBL9rlYZm2vIj6azOY7fvLI9FPlflgrpBlcFzMemqFvRBlTVhjscADmsUrbhx2jnPShoWiAsB_3II_oDNAEGoszYxRmk8uxmXwrZaxvH8cNxB2CZMbjPLiBXtKnCIEH9vzJhhc22dI2DkmB2yS8g7ZXZvwez6nDkwGC__di_5zDlBtGaTgbvEM3zSg9oNTab06EdWzJG3n84CFHT4jgtLrU-5p2O-e890SXjxE-z-_KuZaoWLu77GG2vLtITfnLMI9AfYZY4k3U6_k8EBDlsQb6FhR7OX_z2ZrJ7ASO34MyKvhKghU_E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f0f902f8b.mp4?token=eP1GzxtDkngr-GYN7pga8dlWAVGDJfwaxwLUEQZEQny8pmXGbmUGhrglp_aquFWBtVKfgx17luVdjHdfJukc9b_QkthcnlKcn_Ylxoajfib47dmxIbpTKKBLYdQWSVSsyOOuH71hdUUpybRjy0fJ-hzi205BUkyvxz6jkufKyVNumJMsP7NukXt2J3yV5Jxikyxat1JbqD9W7f4RFvYVYmNnJowC0sdGuNVUEzHQGFyNBSL6eUlc0TemZoUZFk7bxfYVGDzjqUt9pvKrXRVN2l2yZBPyYVb5Q0Nox8l7TveedmReSWK9HDhSTlp-TQtMKI8wlOI_wduC6zXclRlz8G6oiR2SN5g09I0fjrvU4BX-gkMvPdt5FaPpBL9rlYZm2vIj6azOY7fvLI9FPlflgrpBlcFzMemqFvRBlTVhjscADmsUrbhx2jnPShoWiAsB_3II_oDNAEGoszYxRmk8uxmXwrZaxvH8cNxB2CZMbjPLiBXtKnCIEH9vzJhhc22dI2DkmB2yS8g7ZXZvwez6nDkwGC__di_5zDlBtGaTgbvEM3zSg9oNTab06EdWzJG3n84CFHT4jgtLrU-5p2O-e890SXjxE-z-_KuZaoWLu77GG2vLtITfnLMI9AfYZY4k3U6_k8EBDlsQb6FhR7OX_z2ZrJ7ASO34MyKvhKghU_E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میثاقی: به مردم توصیه می‌کنم در ایام جام جهانی روی مسابقات فوتبال شرط‌بندی نکنید چون پول خود را از دست می‌دهید / در فوتبال چیزی قابل پیش‌بینی نیست و نمونه آن برد اکوادور مقابل آلمان است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/97212" target="_blank">📅 22:44 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97211">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
🚨
🔥
🇪🇸
زمان برگزاری ال‌کلاسیکوهای فصل ۲۰۲۶/۲۷ مشخص شد
💢
بازی رفت:
📅
۳ آبان ۱۴۰۵ (۲۵ اکتبر)
🏟️
در ورزشگاه نیوکمپ
📍
هفته دهم لالیگا
🔽
بازی برگشت:
📅
۱۹ اردیبهشت ۱۴۰۶ (۹ می)
🏟️
در ورزشگاه سانتیاگو برنابئو
📍
هفته سی‌وپنجم لالیگا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/97211" target="_blank">📅 22:34 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97210">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mN-BL8sLXKsb5aPFNrwEeQ-41OZGMtueyiGXe3CG-E6J2T5E7zW1VVrjFrmXYxRltheJKCFJhg31s6Q1GBmJUAJSniDZG_JEBTpklrnx2GgQSWhSx8ffy9CUs__h5GNn7iD59vmace8ZfckdhzlKYrvir3uWBRlb-qmQpHvp7Mu5ooBQ1gcv_OUiJtHilnExk6Cfeo0qrJ2f_3-8dNsIvaQ0J8U32YBXsskVb5k-h6-RIIgLmaS2OoVTlYg2LtkKLm2SFDdQPpEqQ3qbvPkM54tkG5A7Irejf4EjcAY5PHKGwAtFDpe1V3s6Q31dH2k5WzsPnlTy1msErtTXjDVYzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🔥
🇪🇸
زمان برگزاری ال‌کلاسیکوهای فصل ۲۰۲۶/۲۷ مشخص شد
💢
بازی رفت:
📅
۳ آبان ۱۴۰۵ (۲۵ اکتبر)
🏟️
در ورزشگاه نیوکمپ
📍
هفته دهم لالیگا
🔽
بازی برگشت:
📅
۱۹ اردیبهشت ۱۴۰۶ (۹ می)
🏟️
در ورزشگاه سانتیاگو برنابئو
📍
هفته سی‌وپنجم لالیگا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/97210" target="_blank">📅 22:32 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97209">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MSgeMvKfLjsao-E_XxFASl4Gb15tfsZmWEkhx_IysXdGB8cv5iDs1x6f5n6r8JL0m8Kq4jZrn-IAMd-C1b-z-nswnxqAscWlLLMjX9U2Or5Pigjyxlb9HipgzyMKFmGTgK6zS8BL6smBWbewDreDrJbEeWpK9on5jQhyOWM8aJO82eT1BN7nY9ivYshwcFKU3IOh-V96c13OLR21BUsPW205FpOmjTC_sVqXDrFcO4yX5p1wkGwDo3OpHkU77XLCRLPt-rQ2Po6V8ICqgC8tKYBTdpdUbT4-hlf6x9rG1TBkmKxJVF1MYvLRd4__m5BwtrKgaRzYIK0YiJjeXu2nlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پایان بازی | صعود نروژ به جمع ۱۶ تیم پس از جدالی سخت برابر ساحل عاج؛ هالند باز هم درخشید!
🇳🇴
نروژ
😀
-
❗
ساحل عاج
🇨🇮
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/97209" target="_blank">📅 22:28 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97208">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VdYNwPXogb9wHk7TvnS5qd-tqY_AeGh9b8xIDk2YZCP-NBPHNVuCcEHW8XmyoggCC9NC1NMT9ALOv_IemEH6E8HZ7D2noIGuYe5bfQfOYxjjyaYBXAuATziJAjMNCUH0Ku1XdCULSzblyFQ5dvQ8pobIY8OgGBU406xhDy7-2rhyD2oypRIJgF1kVeXyMZdCT8n1rR59a8CTUBLd6lEgzRWuiVr7kfLTZJZzqrJKih8I3TktvuxQT4bPnh7bL7KeqtstDCfFaevysW8QRHuOt7pu32e2TGH4Yfo7NgSjYbg_nxQpbfGQ-kQi7nflOlx74JdL4Tq9ZopD2NA6VPq1xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پایان بازی | صعود نروژ به جمع ۱۶ تیم پس از جدالی سخت برابر ساحل عاج؛ هالند باز هم درخشید!
🇳🇴
نروژ
😀
-
❗
ساحل عاج
🇨🇮
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/97208" target="_blank">📅 22:28 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97207">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XStuP8CEO271rYO54lbIsrjqSg9bY1dGzxRiOW68oH3H1GTPzFpKFyzo64lxHZPgF9NKtpR2P7xUUfuUva4nZmn4F2TRM1wF-pdebCdFuXDlt5BHkj3JOV78OykM3Gc0FnYPiPbm3XsGgY82con08m7n--mfT8LWiXUaZP96OZ4fA0XkFGkNKkuqw-M4gm5gvmrWlxtPI_LmdBMBqDJu1mbBohzC2qyi8gLdbW53-mMVIpL1Jejmj7i_ThfjB1YJVUhytLswp-V8zQH-uXgsrPUyHPeMTmKBC2aPoO1aiGx3HQG6Q_eWR3rBqbTsGxYFVsh5N1W4OvN1pm160-YorA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#فووووری
؛ برنامه هفته‌اول لالیگا اسپانیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/97207" target="_blank">📅 22:23 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97206">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🇳🇴
گل دوم نروژ به ساحل عاج هالند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/97206" target="_blank">📅 22:17 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97205">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">هالند بازم گلزنی میکنه</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/97205" target="_blank">📅 22:15 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97204">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">نروژ دومی رو زددددد</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/97204" target="_blank">📅 22:15 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97203">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">گلللللل</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/97203" target="_blank">📅 22:15 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97202">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4771a77adf.mp4?token=rE9o9zIS67SAdbepAjpsW6PV3UWWP70S7Pw_uWB0tBtIFCyul2N5RVod0e8HsV1UDn9OZsP62tg3kw5lGzacgLkQHBVaijwV4Y6jnf-lJEygvIOsbHwq-lAIS567E-Liq1cJF7NbKTqdSIYfjOVCD0TP8jvMi7FgmG9NZnQnLdUKq5etGy5_qu0M9ejvVotetwRZph51z29P_d3zAv-Z-JDsPorFaO6U79sY8Ky0k4U9H6N6CGhw1t3PK749pltTtV_iODK6vFypAgxzyR3sf4t-HD_N82NMYiABY0sKp0IZhNN54uhhiL0WD5zquZt7rs1bjG0Sjtntf5SKd5fZa66Bs6k7BaZVNXC4viiDGxcdHWA8Ul1i8yI8KlFhHEciN9fFje5HNClQFjZ1x6JhvOG1gI2ezGfxWtkK-Nm3xULo511rArE05QIrP-Da8NOQfRKSqfPfZusIpfrjqvQueCarWmCIB0-kkfIna4z8ZPS93Ve6LDOjJ-VFolzynuvA7ve2-X0ejogsZAu8Y2UbW0_ICHJ09EaEmetLD1qMiFh4cJkuGDLHW91-NuZlDqWo90SVOCp6iAhmIGKSJ2EvZr7Q7xdPPynCzg5SzTWveYGtoz3LnLi8VeO8tKJngYNZUIbC4_B7yrWf0ynI3ODwSir1D5W1AzrNOB9AwmFZ_SQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4771a77adf.mp4?token=rE9o9zIS67SAdbepAjpsW6PV3UWWP70S7Pw_uWB0tBtIFCyul2N5RVod0e8HsV1UDn9OZsP62tg3kw5lGzacgLkQHBVaijwV4Y6jnf-lJEygvIOsbHwq-lAIS567E-Liq1cJF7NbKTqdSIYfjOVCD0TP8jvMi7FgmG9NZnQnLdUKq5etGy5_qu0M9ejvVotetwRZph51z29P_d3zAv-Z-JDsPorFaO6U79sY8Ky0k4U9H6N6CGhw1t3PK749pltTtV_iODK6vFypAgxzyR3sf4t-HD_N82NMYiABY0sKp0IZhNN54uhhiL0WD5zquZt7rs1bjG0Sjtntf5SKd5fZa66Bs6k7BaZVNXC4viiDGxcdHWA8Ul1i8yI8KlFhHEciN9fFje5HNClQFjZ1x6JhvOG1gI2ezGfxWtkK-Nm3xULo511rArE05QIrP-Da8NOQfRKSqfPfZusIpfrjqvQueCarWmCIB0-kkfIna4z8ZPS93Ve6LDOjJ-VFolzynuvA7ve2-X0ejogsZAu8Y2UbW0_ICHJ09EaEmetLD1qMiFh4cJkuGDLHW91-NuZlDqWo90SVOCp6iAhmIGKSJ2EvZr7Q7xdPPynCzg5SzTWveYGtoz3LnLi8VeO8tKJngYNZUIbC4_B7yrWf0ynI3ODwSir1D5W1AzrNOB9AwmFZ_SQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇨🇮
گل مساوی ساحل عاج توسط آماد دیالو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/97202" target="_blank">📅 22:05 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97200">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">ساحل عاج زدددد آماد دیالو</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/97200" target="_blank">📅 22:04 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97199">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">گلللل</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/97199" target="_blank">📅 22:04 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97198">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">چیییییو کشیدن بیرون از رو خط ساحل عاجیا</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/97198" target="_blank">📅 21:57 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97197">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">۶۰ دقیقه از بازی گذشت</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/97197" target="_blank">📅 21:50 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97196">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
‼️
🇮🇷
#اختصاصی_فوتبال‌180؛
🔴
چند تن از مسئولان رده‌بالای کشوری فردا هنگام بازگشت کاروان تیم‌منتخب ایران به تهران، با حضور در فرودگاه از اعضای تیم بابت نتایج درخشان و حذف از جام‌جهانی تقدیر خواهند کرد. از خبرنگاران رسانه‌های مختلف هم برای حضور در مراسم دعوت…</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/97196" target="_blank">📅 21:36 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97195">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
‼️
🇮🇷
#اختصاصی_فوتبال‌180؛
🔴
چند تن از مسئولان رده‌بالای کشوری فردا هنگام بازگشت کاروان تیم‌منتخب ایران به تهران، با حضور در فرودگاه از اعضای تیم بابت نتایج درخشان و حذف از جام‌جهانی تقدیر خواهند کرد. از خبرنگاران رسانه‌های مختلف هم برای حضور در مراسم دعوت…</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/97195" target="_blank">📅 21:32 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97193">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rv3gJNoeSqs9KDfq3fDZd_nOIOtWxQCPRc63LUV0Y3WlyFJQQlKttp6HxFLhG4aWurnhilb9VxXvFO8Wwj-ZPXLj9BhEeTwGy3im2Rjyb5z0eFpscCTOy546sYHDbetrWftdA2x7PSLEratgx9VYg-oyY3vT2bbDiyDWswVRoz8_r6gtC-392a96cKC_IBj0s8cV019POAaT8Dvmd_gTea-j0GPjBifjUAuotUNs7XQtCd_3Nrt6TLNVuA0TBSYPCkFKdh4Iqs9Mof9UtvEE5onohwvzzhW3kUQsA2B4TE44g2O7fsT65veIaD6pzndkeRGcoYvPR3k5KHwwtliLLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇮🇷
#اختصاصی_فوتبال‌180؛
🔴
چند تن از مسئولان رده‌بالای کشوری فردا هنگام بازگشت کاروان تیم‌منتخب ایران به تهران، با حضور در فرودگاه از اعضای تیم بابت نتایج درخشان و حذف از جام‌جهانی تقدیر خواهند کرد. از خبرنگاران رسانه‌های مختلف هم برای حضور در مراسم دعوت…</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/97193" target="_blank">📅 21:31 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97192">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uPbZxq7ZjPd7bId3Ty7SzpIliJ6fQglgzC8W6PLeJCV6JVkJW7U042P9bm2DZ82Szp_zZHyE4sM3nAMdm4MHGf5DMx8bq6IXm_LtO4Gg6_vZhCL1CBbNXx-nlh0EQmyr73VmukXH_uI56mMR3ojunY90Yw9ORxB230XAnPGb6N2h_B3QM7R3RaBkp2rm81EcEbICQa8GgYCeM7OudKb5e_1MiytN3lQULG71_HzWKmlfdM_5oGpY547Wiw_uS4T9Dh4e0Ys6jE2hMwLhwLzp0zlz7YrCkPP7UwBE3a1lxAzV0ziQ58RWgg2GKiyzIlnLqou1SZJH2mJTLJkyHxx7kA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🤯
🏆
🇪🇸
ادعای پشم‌ریزون یامال: فکر می‌کنم امسال جام قهرمانی جهان رو بالای سرم میبرم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/97192" target="_blank">📅 21:29 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97191">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OSCgONXzi4vFqBbCM-wsEtHJFe7k1BpfV1kuY7pWs7GSjXbdMbAjwz0PIEvoBI0zxwXlOEGkIreG2mb_CZYMhmZ7EdpO5gPzoLfmfq30sxaEtQtiNOhXzy3LcmV7-SjJmH8_DzlWiPlS-BAJ03yp2KkJPo3jmryXMnbTXPZ3pcw4tjniEugTKAYVDGPtbFzr4SSrd0IQ1lHuZuCT9OXmE3IEo-UK2TPQQr99r_GvS7csjgQ8Su37IJJGxqKC7MkuaIh9wlWzxrLWk1aiWk22nj_HqUvOeIJpKK2w7OZ444r3Qzw49KLKnaLvvL5woE7gUY9kr0S4CxyRe55zyPGHuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
‼️
👀
لامین یامال:
🇫🇷
🇪🇸
فرانسه بهتر از ما؟ نه. آنها ما را شکست ندادند، بنابراین نمی‌توانند بهتر از ما باشند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/97191" target="_blank">📅 21:25 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97189">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sz8LrpT3USPnghwfx8OSBskDom5BvQz0XCMuNMDQjUn98ACmJVjA_naoZLhB4vhZgl8TogXVnE95I06cEAtOHufn-T84nUz2qDrpLhP-7NEhCjpZZ7DX-eONEc-ZS1CMNEe866UZWFwGwd3zkd7UbIBLrG3C4CPNCl4RbD7DHrO-YMTZk04pgahS0j9MZYV4z4nkFa4Xt9TkQdHT87Vq1no1ZXV0w3ACprVbT8FBF7LAyQ4ewtPqERdhv1z1ZDb11kBLBaPKgJltXBPOFJW_VMMNXxcDfM73MlT6E8vSlpENzK64UU0p-TsQYCjBBWVrgWmaRA0r6KtD3trRcEGCpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gqvXvksAOhXQKELxhKds_TWINJddXZ-f0bFhB1n-SL8YGcv49ovqjIaTIXuw-xibmDE-9Rjo8wTElPeZpEWMw2fOKaoNEJ7gMlLrm8fPT0NvUe83OQWVPNmdC0ombmG2vjMuYpdrXyks78Ky1VHGFdmriloEIXgIW4ssh5DLDs2qjdONkMlCTfoU2bf8xXbAtv8UYqtBzbRsFgcQ5sTxsLSEPkvt2E3LJTYhCvNO2Pl2QoKTA9dSS0U76c1MwDYf47bXgG4khWRfSxAraM-CAySVu_HThCH0NCKS4rV-WwjPH-pcfXBzE2Du3LRyk4oXdb16H4ip6OIm5hfokN4PSw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇨🇮
🇳🇴
نمرات بازیکنان دو تیم در پایان نیمه‌اول
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/97189" target="_blank">📅 21:23 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97188">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🏆
پایان نیمه اول | ساحل عاج‌ 0 _ نروژ 1
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/97188" target="_blank">📅 21:21 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97187">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🇳🇴
🔥
🔥
🔥
سوپرگل اول نروژ به ساحل عاج
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/97187" target="_blank">📅 21:13 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97186">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">پشمام چه گلی زد نروژ</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/97186" target="_blank">📅 21:10 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97185">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">گللللللللللللل نروژ</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/97185" target="_blank">📅 21:10 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97184">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IkPrsQvD5OyifD6wF7jUVVzjy_n9FmcPTFZQUt2UtIcD7neuN6Qtl4LFWiiBQjnLOxreoxgTwbKi8ltMiiMdD63nfqrg58IDqpCg4l9lPd2DA6Un8r8_0OyBsEJ0dcGKel_9hAYJ3H8RCzleuIt2zAd9KjQTzffIsVXFnxNBjXczp2x8EjCyrXeTpaZcIF6I2zQoFkwb8WhFv5p65ifFAaZUoW2X_TnpSPTrutA4eySOgq4I3QucbTxBSmMiC86iSEOY2qnOxJ0jxX8oHMHvcoEfYuTNxAinjnf9e8D83io05r9vS8rXE5isJ3yYCNngMoDJvipqQhHAO71yQzyv6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ملت همیشه حاضر در صحنه پیج این دونفرو پیدا کردن
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/97184" target="_blank">📅 21:05 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97183">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/Futball180TV/97183" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/97183" target="_blank">📅 21:05 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97182">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r3Nvm2iG2IU8rgWQUJNoMUt75dGLUq4Xwfd-elYZAWUj6GEWTnDK7aj5fchJOofHDLpyQxfmayLYPMvI3jmmHURiznxLoEr_QKSeK4HPh9vFzrXjuUyNxKbvQ6q_Gwezo0BEFgixHjZvVXGxoLOluztwyFH4PiFIh4pRRJee4azxmg5vlZMQIQ41klOxelnIxpZuJQ_28nfzBNfh-AFwZYXZGZpjf7z2329sQELTAPKVnbMOwGrKrGFRfWHlYeRUie3anG1zRZSrOq7Dmx3IHq2_EdlHIdDNBw9Bwc77kNUKvIMO4Y5CYgwzUMM6ZaO142zK2NP_JoHKiqZ5XmOALQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پروموشن ویژه جام جهانی 2026 آغاز شد!
🎮
World Flight 26 یکی از بزرگ‌ترین کمپین‌های 1xGames در طول جام جهانی
🔥
برخی از جوایز اصلی:
📱
iPhone 17 Pro Max
💻
MacBook Pro M5 Max
📱
Samsung Galaxy S26 Ultra
🎮
PlayStation 5 Pro
🎁
و هزاران جایزه و امتیاز بونوسی دیگر
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/97182" target="_blank">📅 21:05 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97181">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eQ49E_h2nNMB0uPvwma25AVXAOVKB53JXzSGoexPwkyJlFZZh8x8vWVjCpCJs9SwlJOHBUgBoPUwngUcJHghNO3ZZmk3AYrZNTTlYfhpNOr6d34q8BN1OxCqdCxmHQ6e4AHVTQpXHdIUMH1MWk7A2_aPXYuT82uCGGRF-kocpiLFBxvypaLgeYWxeGp8DqtqKc7S8UBntCL98nM2SLzQ6tl1rDCbUTOlMikvZxjCkFVz9He9vPu6JqE-4xm33hoClkStQNYWuAHZ2UrsMW9cbZDtWr77h2rq1ndpwU2UfBOjhyr5E43uRGMYmTIseKH7Tct8K8qQ4e68A2lEeGhGFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسی تو 39 سالگی فقط 81 گل دیگه نیاز داره تا به تعداد گل خودش تو 24 سالگی برسه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/97181" target="_blank">📅 21:03 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97180">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uZ-eaeiAYzA94eVSwhDK4RsbDKOZfjuSy65X7zIYi8SwhaY6-ftm3fUbh4gngcBZZ5vJA3-ccKyuu1x8zud9f-VqQ5Aj8ovppiSg0hvabKfZOPGa8VJd8VA1PWgZnapLLV9TYL3RUmlLAm2WpCYcdSCx8Wt6N4iLx94JpboFpGB9OTVy8D-_8oXMh-5ZDCzlWbmLswAVAjF45SOPz6gFPBc30mevToHdsmV8O5aE-CDvhnyhJe_WI6bhPareJpx1e4Wd5QxQFPtvXMOU15XZN44PV-AEemnWkXw7HYnk0bwxCFGJN2wv8UlVhXgct146Yx2nrdOcPqaQUlYGAgJFbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یامال:
آماده ام و میتونم 90 دقیقه جلو اتریش بازی کنم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/97180" target="_blank">📅 21:01 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97178">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dpBeUwIdGRFX6LLxteRjExjDuCc_m7hsuYT3wy1fFTaxuzDGKQp4WLDsehlOYD-GVx3XDCjdy0jBMbIb16VZG2GZjU1dzbi1lxjLxCicc8kXs6vMNyaePzkZntHbwoCbD_7B9jfNk1dHrmtUKoGHLb5FK_kdEybh3Hky8xwBozwW7CRqtOhK_jNm_Mk3VzuUCG-ti6LYtXqU2B8p9_GU6Ld3wYBnLFItOGARLSLEfCu-nw6z5AIjgG_sXrw2BAwPad9HtJqSyE5dAS9d88-ONOaTDvQDYc4QZ8RlvAbcC0ZMheXXhixqM61wJMO7R6mRUk78xUbL8w06xnw6ySiPNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z-RvXGb48U3x3quMDsGpN50qoDYnldQzGXXLNZI8WrK53wU7-3cXA85JMH5di9C0zl-ubvNo2VUv9SEmIuzdaGGR3GSm-yPYnBp7W8hASKgufLK8Os9DGW3oKEQrl8ACbqjtwO2DvReUnG-Zq74kzj90ZTGrwRmIpQiTmBJw-G2f4ih0YnXW0NoeLOCNPuaM7Zl6Dp2ZY6L1i5gKK09mfvSjR2wNIM7WzyJqndJ86-o06MhY60M-VFL-nErYKLOVNNH4U_6b6U6LM6a62aezgLTZcoJTVBV-m2VFod5n5CoupbWu6yXtGSE0EWSuyL3llGekZWHODkvMnvzSSU_DQg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇫🇷
🆚
🇸🇪
🗓️
۱۰ تیر
⏰
۰۰:۳۰
فرانسه
🆚
سوئد
📌
صعود
فرانسه یا شگفتی سوئد؟
⚽
🔥
فرانسهِ نایب‌قهرمان دوره قبل با عملکردی کم‌نقص وارد مرحله حذفی می‌شود، اما سوئد با انگیزه بالا به دنبال توقف یکی از مدعیان اصلی جام است.
👀
⚡️
فرانسه مقتدرانه صعود می‌کند یا سوئد شگفتی می‌سازد؟
با پوشش کامل بازی‌ها، آپشن‌های متنوع و هیجان لحظه‌به‌لحظه رقابت‌ها.
👉
🌐
🚀
betegram.com/affiliates?btag=3_l7
🔥
⚽</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/97178" target="_blank">📅 21:01 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97177">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WnFvOInmCyjY0jCpvpBQdiJtZHCpS1MUDCGzSjIrihDbJ2_VXKuGVfzSfU4AN0_HGEb57ezUYZfrwTM_3FZucdJHSfqcdD2HTVex8xfWQksCW1L2ziZZoRBklQa4B5NnblAPnSLRpxS0xHc3dem-ygITIPK58lwzsj7d53UhezqYVEPuiOs8woRdXJAqC8j426L-d27L8SKE8q-ZeO1ts2RggmrViSui2e0g4akqnyzAFgKxpgaH0AH_eMTbzIY0V5NDY2_TcP55UQuKzlKZBeqIuvizwNdDDn6VzniKiztJTE_dL3FIL3e6W1Ndfa81vQ7PyZAJxwiyEknFiSUnWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚽️
رسمی | فصل جدید رقابت‌های لالیگا از ۱۶ آگوست (۲۵ مرداد) آغاز میشه.
☑️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/97177" target="_blank">📅 20:58 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97176">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LJ2zeoae3rfOoSnCcb98LtdhZ1aaddnCwYuDiEKU9fXyMYxRNdHoTji0Pdcgn17u38Z93sc00ewUQV76wQEzQa82ZbcNSGTKIJ9nPM2VTz4tmjryet_1PkPuqE_26Gu7w5tA_YVbUNrRzSVt9Xdw4GTyQZne7nFwrzG2H3SoqdKdsihVf-6PA7-0c9TWsqYUeKIsSnXM6zpKgHhcivW-m4gjmFa_dffntLDMHkrLO-eooJe-_lX4NSDjKixW5DvnE952ZfUWv1kPB8IxGOcIei3Cln9ywF2y_MEpMBBr7c3wFMwGqoNyLME1tlUZamWWbLybfv7nsuiweYJjrHT43w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خستم کردی بادوم زمینی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/97176" target="_blank">📅 20:45 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97175">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">شروع بازی نروژ و ساحل عاج</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/97175" target="_blank">📅 20:30 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97174">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
🤩
#فووووری
؛ خداداد عزیزی اعلام کرد که داستان حضورش در پرسپولیس منتفی شده و با تراکتور ادامه خواهد داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/97174" target="_blank">📅 20:28 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97173">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
🔵
#اختصاصی_فوتبال‌180
#فوری
🔵
باشگاه استقلال با چندین ستاره‌جوان لیگ‌برتری به توافق نهایی رسیده اما تا باز شدن پنجره نقل‌وانتقالات آبی‌پوشان، هیچ امضای قرارداد رسمی صورت نخواهد گرفت. هرچند شانس بازشدن پنجره استقلال کم است اما پیگیری‌های وکلای خارجی این باشگاه ادامه دارد. در صورت موفق نشدن آبی‌ها، قرارداد برخی از بازیکنان فعلی که قرار بود جدا شوند، فورا تمدید خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/97173" target="_blank">📅 20:23 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97172">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lJcIAVvokR78bcJ7Ia53AhSdgSM17HpCVP0r7wr6E6jInMgvCCHRnceeMPrY6rJq690ReRkqPsr0qwDbOvZwnwNpizKKFwQn7qjQJaqiYsAYsuI45JZ8-EphLZZaB88QaSoMz-vxN3jHoXG2BAHMuuq0H0tLzvFh494NZrIKjgwIFKkCkPfrcNk-duWy-taiLiybQzm6voUgb2X6fwJkuEely0GVSVR3a9ie8Ig52BkbKm_PXDXfL2P5bZWmZrCVrU895uzYsxmiP5K6eROEjsPaF49cWkAvycVi1hNj5cUDw4Gp0O4uAveGwv9R8If_HbFrluGvTuq5nrClLMLjoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
فوری-دیوید اورنشتین: متئوس فرناندز با 85 میلیون پوند در آستانه پیوستن به تاتنهام قرار داره و این تیم رقابت برای جذب این بازیکنو از منچستریونایتد و سایر تیم‌ها برد.
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/97172" target="_blank">📅 20:13 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97171">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pZQ76O5YoG12ilxI1ljnNjSvIn_KmEgPrxuZhpHK0NLYOmUr1p1NgcvZNw-yZfv4ZHcQrYAQv8xj_pImmAP28pDppkGzyFCiopZTC8YaZbewZI-aaPCKY_DCgMBEh7-UaSgs5Yn7o0oCX0dC5CwPA5aVKWxWnSFYTdHFvD7ep90QP4_eIgz7lp_8A3iJcqw5jarZ_M05kYGWsSivpIrvZ_4M_bfEz75JewY5e3Kytsfs7DRvwfUgqfUPsZvzqYWb4NrnK5-M5d49oM3vG4OE3p_P_rxTBB3l3XRzOz-W3p1sD_R7rgQUlbRV3s9md5oR3t3golDYjRjwx8vvRe4DXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
فوری-دیوید اورنشتین:
متئوس فرناندز با 85 میلیون پوند در آستانه پیوستن به تاتنهام قرار داره و این تیم رقابت برای جذب این بازیکنو از منچستریونایتد و سایر تیم‌ها برد.
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/97171" target="_blank">📅 20:06 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97170">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N4EvAEGqlQlPj1Th5xTb1dY47VG9w82BbjINYg8oxFY_m_DLtUaoUBFZZtNgwRnbaZ3_KRzwFplpfUvVqPD7MSy4nG36ew0X5tXFuILpZQCrM8_W9MNkEgNmaG1arpdAlIqpOR0uJOG12w7nqbzxsnZZ3wUm90ukG-a_vsPjhdJC4SCvz-WCojjE-q7uE3x0MLoR3F-s2nldkl-MPLUgGFvgYxedd-99TmDwlNWmptwOBc9mPiW1mBP8nG3jjhwEtftfT_zS6PLVVsgyTcetkGwfuUyPZE-Xu-LeX9xUjId8KCXrthmzxy4XmBKkOj6Qp97D4SWodPxRh8EIYAO4zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇩🇪
اسکای‌اسپورت: فدراسیون فوتبال آلمان درحال بررسی ارائه پیشنهاد به یورگن‌کلوپ برای جانشینی ناگلزمن است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/97170" target="_blank">📅 19:58 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97169">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fT4HOPrTgwhR54VCRtshcJszXvzOKg17_dF4NFB1Ub6PtPoETFeUZov38N0ZV4D_tLBLO1wvD7tllcX7KXzGFNh4nHXM5aIXruH80AI1bD_e17Qf37KCp1T_AlnK7rtBH80B88P6dD__EZ3SWCZds46AuSY1cJ3Zi6y4xq3hbO7Cb8I814_ESbZqHfLe0CzFn4W-UD9OflOA6VIxBJM3iFW0neg04BCUGBFo__MZkdZv5Mp_AP9Erka4UVx2NnJy3ejlKmzsY7qhcZy2hScbwIX9nrIx-c9dSiyXkzzEdXMJReTgLyfLGw88xz3rUyyBsecZou5DW2h1NAeBtD-g9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
🏆
بهترین وینگرها در جام جهانی تاکنون:
🇧🇷
8.29 - وینیسیوس جونیور
🇳🇱
7.85 - کودی جاکپو
🇧🇪
7.84 - لیاندرو تروسارد
🇨🇮
7.71 - یان دیوماندی
🇫🇷
7.67 - مایکل اولیسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/97169" target="_blank">📅 19:31 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97168">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e36513eaa.mp4?token=uE4TPwsNV1cKMWdDtfpDB7sGHYqqxEtk7jYk55Nc5iV5JBDh5CmS9BomjuNTohwo6hai0lSpNCaRVBtceE669l3bfOIa9BdA99pQp3ExvHi-3PJAGtX3Vk2AGfVHZK6h3DgL8i-fHWYN0CXOd6DWhAtvNjj-Oj4mBHfQxKYq8koMCpzNqDWGey-MZ9OuEOQ5iXJShwv4ev4DTwSfjQlxxsbc3RPwvsj7z8D5Vc5KD6N1o6YOANW4KtQiYLVqEbYpuF71ghscUwWHCNgF8X_Mo-6B9HkoBu-FQkUP2PiAob5LTBzTEK-UQ9I_Q87UgvIl4jliP7UjHUNghKdN2bEn1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e36513eaa.mp4?token=uE4TPwsNV1cKMWdDtfpDB7sGHYqqxEtk7jYk55Nc5iV5JBDh5CmS9BomjuNTohwo6hai0lSpNCaRVBtceE669l3bfOIa9BdA99pQp3ExvHi-3PJAGtX3Vk2AGfVHZK6h3DgL8i-fHWYN0CXOd6DWhAtvNjj-Oj4mBHfQxKYq8koMCpzNqDWGey-MZ9OuEOQ5iXJShwv4ev4DTwSfjQlxxsbc3RPwvsj7z8D5Vc5KD6N1o6YOANW4KtQiYLVqEbYpuF71ghscUwWHCNgF8X_Mo-6B9HkoBu-FQkUP2PiAob5LTBzTEK-UQ9I_Q87UgvIl4jliP7UjHUNghKdN2bEn1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
🇵🇾
خوشحالی پاراگوئه‌ای‌ها از صعود به ⅛نهایی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/97168" target="_blank">📅 19:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97167">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mk1ULH8lRNX8nAyRLZdz3HbrWghuXBba8z3yriumOzPgFB0O68mKOD6CBY3pK_7_brwFN_ysxzuKvTGpXhMQ_FzJbRkvkOhGTgfo2cWdAo6qPe-NWU0P3xbFIHoqbwsDsCuVuvtff-3KV5579Pzu454XJGZzZxFBx8j91HQDMxVz3BHJg3QpVAkSY8lmTK6hyzjv5tlnPUOEwYBM9BnX6Dxe-b2vbg56rct862la1oE_jlzj6OSXm4WtwMEpnYUSAxNg2e4EyNXli1VMUicQvP3q1mIyZoOW2iD8iIDzMHlPuLXsgvxAq6rF1UGR-O2SU8WcwuHYjkxDvmopAwGtfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
جاشوا کیمیش دو بار از گورتزکا خواست که پنالتی ششمو بزنه. پاسخ
نه
بود. بعد او از والدمار آنتون، ناتان براون و مالک چاو خواست. هیچکدوم قبول نکردن. تنها کسی که پا پیش گذاشت جاناتان تاه بود...کسی که هرگز در یک مسابقه رسمی پنالتی نزده بود.
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/97167" target="_blank">📅 19:09 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97165">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p3CKnba0_5yBNoKgog-y9YO6vcP7z8ozzQYuQNX20ua9AscdZaN1jk0eSHKgScvm51shHM3inj6vpGqLgAusBrD3-J-qDQVeomD-LlgHnyYiRh-Hlsag807eMDEf0-5oI7Co-n2Mb8Djm7yrY2Dx8ht-yNmxRpmm12EqANWBDCRY7AJSuDdrRs6qEWNSjGY4WZxXTyhOGCGO_WPkYlyhYftNIDvcCpnQYm0s7vZP_cTDUZ_Mipyg1R7UPbFPQ4kQMvcXuJtvehEnZNAILrQOtMnmUMX0HuHgbzv3PHS0nSiFImWt9XAci6W_KUVfAC89NqXFb1GZ8TajAfjC8-lPwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rfa-5WQtRBH2LzFXwFwj1R9EjhGszLINAEEHCinN5NNlGRWtdUMOhpKQbDtVgHV7kZQFiNDnOsDWiqhtKWXtcA1jJK6sNbpA5ElJnBTewBdklrzQVIYcyiYLYIenIpp2uOPt2QgavnnzYolLaq8f99LIWKy6uQ2fFwJ6qausn4OpRWM4ooSnDArmTJC_mbPJBvW1ExsNP3dygn9ThGwAh9AeX-0a6LhMos35fIKXlDa8bkWnX122gp8shcCc_NZd6H5RpYYTnqeU4Sn192mWabKUw2HpaVbEu8Ycc5aNR5cq-RMKlWCmP5LGUEXawfjW3DhqOpXHXlNgEd3l2jnR1w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇨🇮
🇳🇴
ترکیب رسمی ساحل عاج و نروژ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/97165" target="_blank">📅 19:05 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97164">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">⁉️
ستارگان جام جهانی کفش خود از کجا تهیه می‌کنند؟
🏆
جام جهانی یک تجارت میلیارد دلاری است. آدیداس چگونه با تولید کفش‌های دست‌ساز فوتبال، سهم بزرگی از این بازار را در اختیار دارد؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/97164" target="_blank">📅 19:02 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97163">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kyi31ll_6eYOEUYHbTQ9A8A9O9lqAFJelwrEOK5KpM0erobNEaKyHnrEEI2m_XAd8XswfXl5xOoLNvsBg_KN_sq2xiOk3i8RKNB1WjoYdYpRIA8w8adzDWMl2l4HzLRYZUUwt4Q-wbBZb3JlGXodKHu9DkCBxC8mKJBj8axdeSEeREZ0ELGo6Y2EdbNifSbtsF8qa0afBkQY73HMgEKABHGTrBPuO75QZdB2hSN2CgKNfKHmRbbdT-Wtnxrs7kUYLvOAyteAO5PINR7uN4qU_bHPRtSLVAdQKflG5j_4BVP3tQibqHZwEtM_7JDwVqlV45y8F4-akTdKn9ln0Jf6jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
ترکیب اصلی PSG بعد از اینکه یان دیومانده رو جذب کنن واقعا پشم ریزونه
😐
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/97163" target="_blank">📅 18:43 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97162">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EfooJY6WQX0LPOri3w2c6VngweL5V10DchUfAVoYyq_GlQik32vEcg20pRJD8edaJ32wj0dSxvKx5gSGSLtdziFkgPEmruspk-VShH72F2eMjc-5CBnKWvmyklikNMiZGP8cvkE5_RRBMbU0aUgi5k8TPqXQx0HTndP7tzWKmn0A-vYJ046ZV0e2-8dx1BRhUOlzsLxXgGqilRlZ__aHrJ7tYXUk81ksMqHc3IPm_O3BnNUIt13oS-ksTuRtoEEpSdU0LjLfb_RNHAGifjG0a4SMAabSraTccLNwlLgxA7Jojw1GwAO_JeOKL1c8CgG3IaM3g4Xy5lbtH4Z3hn2pxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇫🇷
#فووووری
و
#رسمیییییی
؛ با اعلام باشگاه بارسلونا، آنسو فاتی با عقد قراردادی دائمی به مبلغ ۱۱ میلیون یورو راهی موناکو شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/97162" target="_blank">📅 18:36 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97161">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/quytK-cKnmue-s4URt65pXhITW01N2WLIZXEV4Mg9PvxUONmB4wdRgwBF3vmY8zmfhJe4TK7tlHZbYakJ57W0JoIdBYtZbjSMDtrm1BNxZaZD7l0gounnATe31jmaHqFp1xrOOOlfejdqv8fKkhcB9gh3qRYH1S3Ciiap2b5aCWmUc_oOu80Vxwg20nvoLBaZpJZzYTQg3CeMSNLAjXktEpwfbq5Wfy53829ESKvI6bbuOaZkiHrKTBvs1BF3qUNEdyfjwB2gZnou_juNpwCZQ6uF6IT74wDEQ_WSr85R5mVOJzLrH4xHX8ju4UJ2HAF7aHDHcZmiWFPUzctfPBnqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
#فووووووری
؛ با اعلام منابع خبری اسپانیا، باستونی ستاره اینتر در آستانه عقد قرارداد با رئال‌مادرید به مبلغ ۶۰ میلیون یورو است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/97161" target="_blank">📅 18:34 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97160">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IHNosNj1FyB8yt3Dd_9sl2rzop4rKCQGWnvECzae3EiAvGZHS3kaXhHnx4ZPmgJyaX5xGNDHbaCawC0CfbCzRwNprVhTYkbjw-MW_KpGhiWVllWUyshShYYGX3IMqHZ9i1pDrY1JNRiHco95jDmZfFdKsctTt4aAkp3MfqDll5q2j_aeEljVirmpka9SlMJn0au8tLLiFL_RDByhZU9_UdfX_mRy-OD27-GS5UgDoDxBBa2lyBql6VJd7V19ugAqVoEs12xnXi9Px1sR8kODbhGoH2IBfeY7FBE_2nKnh66wKUZW9Qz1hpZwT3pTSqVn65TUaWmqsen1AzOMUFlZ3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جای خالی ژائو پدرو شدیداً توی ترکیب برزیل حس میشه؛ آنچلوتی به خاطر دعوت نیمار مجبور شد ستاره‌ی این روزهای چلسی رو از لیست خط بزنه و حالا توی تورنومنت مهمی مثل جام جهانی یه مهاجم شش دنگ نداشته باشه.
درست بود وقتی مهاجم نداری نیماری که تو سه سال گذشته ۹۰ درصد بازی‌هارو به خاطر مصدومیت از دست داده رو دعوت کنی ولی ژائو پدرو با اون آمار فوق العاده رو نه؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/97160" target="_blank">📅 18:33 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97159">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb9ef52a64.mp4?token=SCDrtd8j0YzHb37cCdsApgfgHGRHSRIZDQ5gl14WYXUU1HZbZmSp__u3sLxDSJzqNxOKXvAIkm3jkiKcYhYWVLkngNFhWSK8ue4lShBa41QbECGS8u78pZXY2PefODyUbwiSgxwz61E_pHHM10QlSa4RgSs1FdanKEv5Wht41aol0a0Syu13fLgAvNBJSX05tUzLKlj90Y4rX8vcDkHKUzziOfryQG9jdq2JJ1SbkM50XrXv2Ml6pp7Z9ZnW1rrKGyuNLt3OJx0xj3TGg7OnhCvirc9nk_wFqSv7voFPf9QTECJrw-96MW84lR3c8OuZXSufGEXYvIaBvCPw0vtMHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb9ef52a64.mp4?token=SCDrtd8j0YzHb37cCdsApgfgHGRHSRIZDQ5gl14WYXUU1HZbZmSp__u3sLxDSJzqNxOKXvAIkm3jkiKcYhYWVLkngNFhWSK8ue4lShBa41QbECGS8u78pZXY2PefODyUbwiSgxwz61E_pHHM10QlSa4RgSs1FdanKEv5Wht41aol0a0Syu13fLgAvNBJSX05tUzLKlj90Y4rX8vcDkHKUzziOfryQG9jdq2JJ1SbkM50XrXv2Ml6pp7Z9ZnW1rrKGyuNLt3OJx0xj3TGg7OnhCvirc9nk_wFqSv7voFPf9QTECJrw-96MW84lR3c8OuZXSufGEXYvIaBvCPw0vtMHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
پشماتون بریزه؛ سر صحنه آخر پنالتی دیشب پاراگوئه یهو تلویزیون قطع شد نزدیک بود نصف جمعیت سکته بزنن
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/97159" target="_blank">📅 18:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97158">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad9b9bbd43.mp4?token=kwEjlun-u7LrcJ4SbyoHT83o_1msXs6aTRuxhPe3cyhHKWR-XdU54YpMuo0MI3H9evSx3TTdnaN8_Q4_9GwxEz5i3_3mm0GBU6DmgZjIonKUcRqEukE5VlP8YWHGT2OQGxK-IMAJAVAftkw5J78IKa_YR-zndxrsqBuNTnnNYMmC-i7GZSbCE26zUgDJf22GrlreNyz5zTTT6Lbz2go7kARKtObD0RGIKqJSacijdfZ6F3nnPs26K2yZ3C4DDcKiuoSyK_XOZJIFfGTatBDBe_DubjYUPzKdedVssfZ8LcjO6cNHJEBBmbvprqrA0CbaFi6FnyQNJlh6Z7lEPTQcGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad9b9bbd43.mp4?token=kwEjlun-u7LrcJ4SbyoHT83o_1msXs6aTRuxhPe3cyhHKWR-XdU54YpMuo0MI3H9evSx3TTdnaN8_Q4_9GwxEz5i3_3mm0GBU6DmgZjIonKUcRqEukE5VlP8YWHGT2OQGxK-IMAJAVAftkw5J78IKa_YR-zndxrsqBuNTnnNYMmC-i7GZSbCE26zUgDJf22GrlreNyz5zTTT6Lbz2go7kARKtObD0RGIKqJSacijdfZ6F3nnPs26K2yZ3C4DDcKiuoSyK_XOZJIFfGTatBDBe_DubjYUPzKdedVssfZ8LcjO6cNHJEBBmbvprqrA0CbaFi6FnyQNJlh6Z7lEPTQcGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بعد باخت ژاپن جلوی برزیل، اسپید رفت که یه هوادار ژاپنیو دلداری بده که طرف هی داد میزد "مسی، مسی" اسپیدم کلش کیری شد و گفت خفه شو مادرجنده
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/97158" target="_blank">📅 18:05 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97152">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/a-HgxJF4MgFSBc_yPYJNXtjnW8l4FQULOTSJrkY5M4f2tgTJZbaHfAoeLyItcLj2zGf29WLiyqLlmUcQMDjdkCQO6N9jSiOWBZqLU8BfjJHKm4xbuOky-Ljsd31-DO09-fqs3cnk9_XYsXfuu8sUPQHMXyhWEFQ-cg0JyawQEXqzw3SOfewTLoKIWyfagYZEYqaZRvqMh5Nskq1z6QbLD16WKr7UILL-U8lt9NCiS5IawpgI5VOfA4YELGfdE7nwPLBbgGpl3-FojPvDWK-34d6HgXYttttrfIa30CPSzuaj1LvyCyz7SQzRSVaan4Fhdwdp2chsmKiIHLjEPVzKSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t8N9dcksa0P2L2SQLdt7QWRrQx_4wv_Ao7JGNd7MsNAOcLgI8i97Z8aWQkWJg_eGV2G5Z_8woxHrptPuSN_4w4pM0Ox3KCmtp0ehHFdl5i93RQGr2t2tDoMWd5MvQ_UBa0N_nUgKxG8TgSVw8UD0MisTnP-0TWYKOQ8lQTFft8_Xd9uiWy-73vC56FodUPqmdSq1m18qEFm6b-KxPWOSgVTkSzcsxcE4nVseUHXRQDQ49T4_SQKfJcspreDW41fIOdkbPffaKHacd1T2tOh2VJJBK7b5aNT0HbACZRRN6NDyNw32EMqfO9e-ZeaTvW4mFh7U_L5b7b5AqVH8BPqDwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/v39NnvO0sB_QirLY0RSUNspUAatH7JpxnJHbqClZ6T0mI8-p8OlS-vxVNmVzNVwgEMJPQ359wjhX72AVGyxvaPANpfYl_E68hpA_i3bqveh55Bt4gdlIefprNFhmFb3xsNWg1yL8CFvxTvwzaoFnC0W1xnfN11STK9PxMwpG3khwaBrqm60grQcneSJZD3QHwiQXzyV15f4r_U8YmXzyWucfhd18hA-qtMhQuCrkbZdllcixSVlre_3ZFQ0ubCgWsRJ3CMJl0eRsu-vzPT4m6Z7taLvPNTqwIg3DRnRtslcJPlWP2X9aCADqueGo3H2Eeiqb21n2152ZbFC5DWFN9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UayrTxzIaXFMVzxIfgFX9ZnjDNOR9Z613KcDCy2JBcKULPqdb-K_8mYMmBAM0bajGrRMOVgE_hA5oNk_xaiKZJ-9ayrNQcMOtYrzfqFV4Z3jk68i18K2rWndALDH4XjmdIT2Jkd8nMLIWd8VM9zF2p8xSy4sCvKM5nxCCaFincy2Xw89ZqK9LMQ3zhi5Yfp1IEFE69YWfGHmx-eqaGN6WfFEV7iuYCsAcd-QgHhunpW3AXsWxQpfcl0pcu6GoFjaX8XDb-HeCRu_aR3eISjHXY6F1GeIPIl0RUlb1JE1GzGC-IBh5r8FqSxyNnr4rkEVi7N3M7nGZmJSACqcD6ntbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PTUgqskZt-bvMGPDyldyuIdx_W5f-J89r2ibsn14GouIhAM5HyD26qdEUQEM-1TErxN09l_pvHKyaskDYkkvMdGWzjiPNrYIE5XeFuF34v0ktF-buMJNBj3LSsPChN0B5oyIIe0y1OPALFKT50OzCFLNtWvlf_7Fjrxv-ZtkdNiWYH7K-K6qETz3o1rUl1VXfObk-t_c6vViyNCn79iaWyHNI7Dgriyxg7j7WT5cdwxVu-14Hq2XzaSOA_SF7JsA1jJQ8PKostRsmK6s2YezxjYgJGUn1RhnRbNuAspFJHow3a7MRRbQws9Nrk6VoHUHXOp8Qpni7HxXvCupg96E7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TXSy-DaBz8eVyLwibWg1kXI8K5P7s2gmo8I54R5MVouAsLUc8ieBJb43quspYDq1mo01Hsg_s1428kzAcIPauqh8dYggGiDmKL-WhbCZOrupxfMijZPgf02N5QUnIE60xmRfsGG7qdzdfbEX_QYbYSL1kyVKeJlX4bDpV8J3b4auR-qQwxIdjIa5wue-iDcA6bPShbAxSE7qTjI7mcau5lKHtGh8z4R7VXvEwOfxml9tZ3sqkFa2n-Yp73oSwODYFu4IOv1FOSmsN12XrhCFNWkpiL9dnXvCcrIAb4zF-7GhXoUejiHpp-zKx8a8sIpZonghf--vkMnzfTIMe2324Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
فضای‌امنیتی فوق‌العاده در استادیوم‌های مسابقات این دوره جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/97152" target="_blank">📅 18:03 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97145">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/E2aT2rRlLh5sSVSOKBcyi83fm87Fw4l0E0WuFPXt6hGkz7-IG_aIN2qp6-4Q8k7ecJJe58Z1F-WyiYg3QROStzteKRsaEiZhLV54NvasZAa7gwY7SJjYKGQZolXjBoyL0Z2DqZBVqFnEkui7jZ4ju1El4mqbQixE9B5lk3XtE4fJAnPGGt8eUjJdVo2GXg77zScl7uWTPWuu-99LzoGw-7v_WhFWHPhp1fGRVslPWHUQSJk_9lEXG2cCLy8BJN8Wz3x8I1IFlGtQCnLdi65_VI-V38e33vxWoCdzxGLln5V5VGJl1xIcrNVVYfDmitc01f8gWOmN05o-wgGKL9hYXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Hh-HlFQyyVH1bSOi1JdyC0ZM-jU-rmRL6rhMKBYwU5HqszBzhrizPCjNMxyVrGTMQqnr2VJs94MqffI1HRoa8i-vZEesmUQDr5I6UCXp35X1iFPHt95MTCErLpXhErE0gvS8ckwr83KbBAVuZNhJpKuLhRnDMlxVwimald8P164jYUljrSsbg-Zfm2yVlkk0Pao6c0V7uDa1jAMCZc0Dt1uRwXDBgiDPREfo81ak4ziJqJgM0STj4aEKJS445Yme4eiGicr_Ij66SKUbMkh8-r5_DZAdXW_1N7uOoZdzAKrAEqAw2OrtuVM9WbGEbhliC8Qszny_5InniCnRgBdFdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sUsH0Xqyft3ul629gigHPFpMfHyNGu6tRnLJPygd5AJJYP-XBg1unVrSrK4tR7wsxA9K1HtuQi0C1j7RFTSu9b5kFy4HNZtYOcqOYiMRtXtf7_CDYAGpdZQ8YuYaQjuiACJnF4hixxSDqS96v8x7B0BRswq32WYCAX6Ee1XB8wAOQ7z0VxBf8gv6hSNAENJlazQ6IUpY6fP7jeNPh2J9XYgGjL61QBoZhKqD08yIGJiyJuAVcfZBoqBYIjU1vi2smrJMjYgmjb1PddVsEz1_yLNQjPMOG7sC6dK8pOoh34D6PQbQDPdhIDGREkFQ21YTQCfUVSCCW79uvw2DwBU8qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Deni8adDKGzaJS3RiI8ntskt8A16YC_x1-1_tvRTs0uYCKT7Ks6syUbFoenjDfSjGyIRUrAMO1MtQ7N3ZLyUybnUGJhVULLkGQ-3iNLMOLfnu1JNAlQ_dEwwJCYkP190SB2qXy6_fAxoiFsgfThayiVQAATK8BxmEfzbGMeeoUexEXJptPOFjE3Y5xFxzsdLjWoLy5frukH_XIMKgSzUfHAZgn0hCtvn7yrZj31XwS16h1t1PlstAjdzCuGtoh9oidlqWJc0MN2n_I5fPSc-52rlXYZspC-mvzzQg8Fc5YvZuIvO00bcApAKptNOrqnvJVvmsJxEct-RXmraGwh-hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TMZYl3OSPWSl5xs7em9FtIjinvdR8OCtWvAIy5CFFIU7TZMA32DVOEk_7xDPwZisGPFVTu1LEAjGtHtYeSXMC_On1GI6rsVfZX9tZSTsbpf6JScYPXt5wqBrD_pKASvA4RlPQxRjPCOb9Yf_xO1EHHxYcNzEZErGgf7QUSETjLfrx0dsgF5cLHcItsa7hkwI-0INa6OP_sVFBDXI4OdgHpl1j7Eu2AkNMzEOgt83wobJnG0ROANtPjPu3dEr5tfoQYCZPYZ-a2lqq1b397MFcotiiPV9KDYbsopegDEYHHtDbEr6jkMQTmmpJxyySYfVX4bVztSUdmZQ9B-bFkLLjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Irz2FvjcqNQKx5KM2mn9vnlNe69KQA7SxC5vee-SrthxbNcI9eJwEtIsIoiqv1EdWFxVrHl3L1Cmkeo_Y0PR-FXQngd9LPw8WF2bh5rv5UTKM39pkWuS5VTo22YeNUUKUUI-SJuuQ81XSOpMsiaQYZgBLu7cxvAryM9xxmKf2cEHDqpXt_zL1q1Wba-t1hPuuix_zqpo6ly2hR85wo3jCyB0CQshgALYm4IVF8c6SWax9m43VxR1QfNtAkAbGtwJFZjXxEnlIFEehm6U7e1uzpdhEwBWp1OotE2h3Ixeo9nDmYutr_dnDoOi7Zt06eiETjWZ4XbTNKV6x8CmKKX3jA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/spaQYaoIrKjNYyhmyRENfgewJ6hv0wDM2IzjgqMCKxBqCMuya63Pff5AD9PEGHQJRYZ22tnNd8WW_rrrN9bC8okqtzCgil26F76N-W2NugHy9OWKpNTCqlHIaUnltSkhVFKeRfv4Kw3yqg6Aqbotbqr2xCXeCmyQl4CbTe_kp4cjPv6k381ZdsZxpqGx0znBEpjEOH5mbdiGF4FwNmVtcRERYn5d-t3O0rXznQvvo6ozSPbbxrzgz1-y2hGdMycoDgKnXDkJNoTx6siawFMPM9r95Q2EpRooAd_LwbNr-HfbVXyIglsuBzE22LGcXgRYD8Vs2uEhu8-sIYfXmwLNDQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">💥
همسر ریاض‌محرز در ورزشگاه‌های جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/97145" target="_blank">📅 17:40 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97144">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iy9wmyc578m5pzbTVSQCvzM1EIXR4tDtCco2HZThi-3yNw8YVeukDVmJ63BJ4gIUWLAVZG5xykwiKN_n3LVUL4wCor4OilE29XucnhTKMmMf6Mv8Thx0joPbut-v5QYxCfkKZv3UhOf7OelPJMzVLxpyo12pB3u1QRpPNqh5vb0ARRc_9_OISpMg2wpET7Wpe5es1-4NyWOXT52A124S3QI6Sd5Pt5dxiP2cKlaxizEbk9tkG9GMVQpZvmvcSDc2OnUnJxAJX6JFvuBX0_W9Ir7Sl-pYNKG0AZA6peqGswQJ08UCtGg201Ivx7T3kWSje1hJ1cj61dSJZaM9e5ShwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
✔️
فوری و رسمی؛
گونزالو راموس به میلان پیوست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/97144" target="_blank">📅 17:35 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97143">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gd_1SCTQfzlAYE66c2JuWBwFz3T4sAkB2f-IL88skv_N-QB7WkqZmmhx1SDAKcsEejTq9ktM9ykpHudQGQrdFsKdEN17FfOgCd8DGkqBH-kCwvXUbHKRGfHDznb3tsNY7vLzUASNZgMRgYtTJZShBWBz6SIWq3QUYV3POsYqCoZac3tnZBjT_D16E9KczxmEX0urvwuN6rlnl22NFnfSS-xKxIprBPdL11yywotZA4s8z7SGm-uTM7s0r5vN38GNox-fLwg5RwdHhwFA1IxBLla24rrxgv6Hb0MYiK8hPdv1Og0rZBBhzbMb8f1mpi5w8AWXnqyfOHsdXlF0kC0Z7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
📊
🏆
رتبه‌بندی نامزدهای برنده توپ طلا تا ژوئن ۲۰۲۶ از نگاه‌ وبسایت Goal :
🏴󠁧󠁢󠁥󠁮󠁧󠁿
هری کین.
👑
🏴
🇫🇷
دمبله
🇫🇷
اولیسه
🇫🇷
امباپه
🇪🇸
یامال
🇦🇷
لیونل‌مسی
🇬🇪
کوراتسخیلیا
🇳🇴
هالند
🇵🇹
ویتینیا
🇨🇴
لوئیس دیاز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/97143" target="_blank">📅 17:26 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97142">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qfvN1kG-RPEzKMaNk3pHnrYSxRrm_qBaKxayfmAI4-UOo0QAnrRL_uEz7YhGur6WIsmdNYE-hnClj7jibKO8A7lvMbobKbj5ls8bt69jNi6iGp1ctWmZdh_khC6NNV-UrNBTvUsjFxQsF4OWh1KLBhlR-rUn3p_Tpm0dqdcXfwJtz2DLwLDgFUlj6dvZ36Be9bfaTFpnJwxvhlUvMreVfnv7YbkBftkYvhMXHeQPFEn_cJLkpCB5GKKtKFh_eCc-H0jUg3bhzFM6YFAKcQixpoiwHjbdYBurG8dxSP9G3lM1WLCCm2vt2TWPrD9CCq8wcNJ9hGwDQpvbrXmC_OaIfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
❌
فوری؛ فابریزیو رومانو:
فعلا هیچ پیشرفت یا مذاکره جدیدی بین رئال مادرید و چلسی بر سر جذب انزو فرناندز وجود ندارد. انزو مورد توجه رئال است، اما در حال حاضر جزو اولویت‌های باشگاه نیست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/97142" target="_blank">📅 17:24 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97141">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1401efae7.mp4?token=PcRmP7CkmzpY6NZLtgOwaBIF3k80GkAsrNwefEbaaMvfM9wKH82yus3L__iT39WX4rwHWYF4RlPAL4DSgKKxFtttnjcTDedtwSyZl-5jzqXC7qaTkzT_lArqnoWGg-OH6QMrIsu_j7FjIMfO-sBvPC-JsPD63dNK5mnzaqdZmsl7VVtL8I8ecr3qUcNSaWoOq6Q-SOK1Q49Frvto3K0M5ARU9A99YOcpN8GCVYV6HS9fWAE8twLzri1E7XCT8Fpx7itjBAMrPcKarIEaILAeKiK7WlFI95DPDiE7kW91Rd6_1vK6g2GFdBSibu5NrZb_vdCzUHGraUjCq1HM2ekeyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1401efae7.mp4?token=PcRmP7CkmzpY6NZLtgOwaBIF3k80GkAsrNwefEbaaMvfM9wKH82yus3L__iT39WX4rwHWYF4RlPAL4DSgKKxFtttnjcTDedtwSyZl-5jzqXC7qaTkzT_lArqnoWGg-OH6QMrIsu_j7FjIMfO-sBvPC-JsPD63dNK5mnzaqdZmsl7VVtL8I8ecr3qUcNSaWoOq6Q-SOK1Q49Frvto3K0M5ARU9A99YOcpN8GCVYV6HS9fWAE8twLzri1E7XCT8Fpx7itjBAMrPcKarIEaILAeKiK7WlFI95DPDiE7kW91Rd6_1vK6g2GFdBSibu5NrZb_vdCzUHGraUjCq1HM2ekeyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
اسطوره‌های‌بیشمار در حین‌بازی برزیل و‌ ژاپن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/97141" target="_blank">📅 17:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97137">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tZTsnpws1hf0yIhFVIJK2PCcqK55ydDrVw9M10o7YTH0t4wORXbUD_tnulRIfAi3HCv5QKjknZ8rs2HNOZfy50iAZQfYvbEwOZmBKAlOEeqTOyE0noAVNxrYomFB5ssxw_Y4GDIzpp9jNUgGIKHeCOnR0r2y_wP9cr_2VbG84KlCLNTMc9SfDd_sRx6v66FdhaD7G4sgtGDnXTSd6v3SQLobzFQS4XQwZ_-5B4kGSGZwR214qSRkGfNA_vwxzmUnsmO1rUQ7sr0PbNlOkzkM-k8mYoh_KiE3s7q5kUN_2oktkwfGOCmc7lEa7Id7e5vup0ARgufuzry4EEmKJdtDDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R_Sa4l7FhzzJZttVdYVU-rOjaQHFdOgNCMWZWC8RE4AiznWXBgQ8YxrVHTOWP3NhhqizSdxWE8CsC6JWA0EcgmGtCgqlGPFWNkAkQhUaPmNS6qGDtTcpnOl1YJGhxyBRjsmliqmdgF2epl2rU4zdLKxcP5bJFA9N1zrz85iEVaVPS06CB8xK8A-B9vTvsISS8EQZVLUFFI4grnnExNinp4INw9JzPMdeQpCc0gNkmbQBXX7jAwuC4HPOnoS6d9AWdyeZexB8NuJ2KGrxl_8p6cXvsxCEkOBglGIa5nA2ebvqfeixG5ocPwx3wA0HH4otmkSTSZHUhgRHtpAHitoZag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vagkNIJA6bYnmqRpwx45JbFM7IDVFs1f0xAEq2fJc54KroUpiqM6eylaQCkXtqoCIuB0i15zkBmbAv8i5Q-KCBggalC5UhDhhVFqqLcYb3qbbexNKp06vQ5NeVCl0ds1BWLqDLlB4G6WYDYSDAsDObQpkk-iUCo04kSpPlvXFOm5meCjbdERXlZoSDKnFfRx_p0dTY4SglxWg5fDWniL6I5rCxYn9_PJa_whpiptkxVS8oDNfW2gMl7C83WZniDf-MXsb6_9HLP-NyxrKv4oiJ1_67W-7wtw3Avr4n4kUNOp51Z49-9r2LpbLWr182hyRHDWhVTtQ0jdUz1OMkFPpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QG5drHxe-cY4QhLdFkOXYHwsYDgrQTL-rhkveqixPhZPScONCEwbLulOF98OmMX-pYSpF7uy0I2d5PJ_sSPOVx7UJNZl-EoipwVVyMFjmNU_u7lNXRw3OazARvPWGCGAURqaZc64nBFLKMxESv1IrycDBRByS6LI3xO1q2o6hNK4MZJkKJsoJF-j_Qi5nlvPixBB-ShKb1SeQGDBUCZh75TBaMfQ4WEh-RBvh2I5aZWtLWn-YFDAWlQvGx2P2C69DmfFbIZ2qmmhJ_6OMCgGKOY3X_iInrF2dDo-dqGtOwl8mpasjmhzKOv4WUGvU6NrZqeZI9qjxso23zx3g62SUQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
بانو میروسلاوا مونته‌مایور مجری شبکه TNT اسپورت جام جهانی هستن
🐸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/97137" target="_blank">📅 17:11 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97136">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">😛
یکی دوتا منبع خبری آمریکایی صبحی گزارش داده بودن که جان‌سینا و زن ایرانیش قراره دو هفته دیگه بیان شیراز برا یه پروژه تبليغاتی. ایشالا که خیره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/97136" target="_blank">📅 17:08 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97134">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e6QRrIYfMJz1oKZZrlaC8sPznAyYTBTXFVMOBX0CBsAj0zFmPc1-0JlcSlZ8xaX2FfFbLBmoizvFGUzFOjoYu9hUHqnuZHHg8fL-eJ4v-6BaIoqJhRwNV25TkAzFzh--Dd5hDls6aVdWwLH_eHD6geFBz3nGoxnXXDIXIItAV2Gm9E-e9SA1xcuaYTXR3PaadWxgc3eM8j6bWMB9yiJhBQG93rh72cPG94t_4DATuoip24HK2RBKA2PFQIf_xat47NiWsddwmbIUcqW4s0Zd66Dd4WsMzhFKtAmaRq6YqpqFIhzZWWZmC2bsa0jAkVuAXavNHjt_MTlLMZ78EsR54Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PB1byFh9oI5-gEgC_1rD2ARCZblCNY9cBwCEJq3N4-IWefVlNaREipQfNM0NxdZBhe5kgiArVC8jQrNhhnps1ngtNR5iQ4mU4dy69_L1OkRgexDyG8vsp1CdVZr7rK7OLBYK-cWrpCH5zGzyOvvkgNuR-orvY50ZuDBAvc0At3boT5clNm06u0OcG0QkaPz_bM9mZPWjTL-Dxif2hWSt0BuypDvbABCYe7VcgLrr4V3IO-DI8w0KZC1hlb06qTNGLef70BEOI7xF4ZpaGWFoi5I8Yiju-Of-JAtqFXiMeJzH2bpOcszZDwa7GeYmfcpMqxD2Bf8p0GGpMKo4oCb0Qw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ظاهر جدید جان سینا
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/97134" target="_blank">📅 17:05 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97133">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43c88f5b44.mp4?token=jswM-K7Y_DHR4ZBbTo5PyIVEDYZCY_7Datr1LdJB2LtEaLxOS7KRQjElIl2HgNXupGadrWvb91vR6dZ8rOiDrl7I_9VLln1ipQgefkitfvSulR_k1l3djaW7CtjSIvID2HjgnXAJadFk1Lx5NfEbbgCWsGeD1zczQ7jw46-hnd79dkwivvvBLt6cN5UCubfogGEpehwtKU8wDOHE1kc8DtCGab3vUdk4y3JfjYneq3hkGFu9nfB-RBERzNG6TaGU_MT-3C1OuOvjAX_nrO9bqSclD4UOUBHvbdUknaFJOqqG3CkU2J6aPy3tYRHVLBuPcS_py5DzhWdskzWp_r3ggw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43c88f5b44.mp4?token=jswM-K7Y_DHR4ZBbTo5PyIVEDYZCY_7Datr1LdJB2LtEaLxOS7KRQjElIl2HgNXupGadrWvb91vR6dZ8rOiDrl7I_9VLln1ipQgefkitfvSulR_k1l3djaW7CtjSIvID2HjgnXAJadFk1Lx5NfEbbgCWsGeD1zczQ7jw46-hnd79dkwivvvBLt6cN5UCubfogGEpehwtKU8wDOHE1kc8DtCGab3vUdk4y3JfjYneq3hkGFu9nfB-RBERzNG6TaGU_MT-3C1OuOvjAX_nrO9bqSclD4UOUBHvbdUknaFJOqqG3CkU2J6aPy3tYRHVLBuPcS_py5DzhWdskzWp_r3ggw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🏆
واکنش آنجلوتی به گل‌ لحظات‌آخر مارتینلی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/97133" target="_blank">📅 17:05 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97132">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jBZRE0FLDjvC40g14fnbuaxhHIJ4Xm6jzrdWFcSX47ei7KBlaECrIidlCoDT2HOKmGK5VgFoDbZZsQJoYnRQ-vnB6al-rCl9lTUFIBf2-mg4dxFBUd0Rl3-pa-cG7CSCPitBEXe-rIJ497oQpTkvQBnMq2zRZii8s3zrrtqvXeOGG2aHJv-xLLVDCxJT1qw4r2FlCsba6nsiVUUonLvXGUijgUO4Zv3C-UDat6KrY9sNoFQBFuMSoMrG1ablY0ttySEbB4NUtBx0Y_ZEcNk4zDN9Wt8h1gaku_D2u9k4DIvD2LBk8Un8r8iCLtME8PLbXW6FMnGnmqbpTIhBMZsHCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇾
طبق رده‌بندی فیفا، پیروزی پاراگوئه مقابل آلمان چهارمین شگفتی بزرگ تاریخ جام جهانی محسوب می‌شود!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/97132" target="_blank">📅 16:59 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97131">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🚨
‼️
🇮🇷
#اختصاصی_فوتبال‌180
؛
🔴
چند تن از مسئولان رده‌بالای کشوری فردا هنگام بازگشت کاروان تیم‌منتخب ایران به تهران، با حضور در فرودگاه از اعضای تیم بابت نتایج درخشان و حذف از جام‌جهانی تقدیر خواهند کرد. از خبرنگاران رسانه‌های مختلف هم برای حضور در مراسم دعوت شده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/97131" target="_blank">📅 16:54 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97130">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffa3275ad1.mp4?token=NOPZ1GzEWoshvU9UtgkjK79g6_Sf2QzanQXYBfTu7o05LUPnljYGyn-PiaPhfaWCJtG0h_1AMS7kg0ck2HeZDRde0P6SEYPUCV-lwrUKrWXKQU1XA8rCh0R3YQ6MTWCXI_BssuGlADHyTEfBbESgfsTaXj3HC5sW34H0sZBm7Iobgc9pKqV8_EQ4G4o8y1iAPcllqvVRZACX8q38km-XI-fHf_BqSMpRBaX-B7GVlurg_5ea0pps9ruaZusLEj-XgPomV8soU7KS14zGfwim9AM7L56oVuKObKc7eWrVTBI2cm68A3ILGefKEU3GzzlpIG_1_CzER2p4nyLFYVQPSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffa3275ad1.mp4?token=NOPZ1GzEWoshvU9UtgkjK79g6_Sf2QzanQXYBfTu7o05LUPnljYGyn-PiaPhfaWCJtG0h_1AMS7kg0ck2HeZDRde0P6SEYPUCV-lwrUKrWXKQU1XA8rCh0R3YQ6MTWCXI_BssuGlADHyTEfBbESgfsTaXj3HC5sW34H0sZBm7Iobgc9pKqV8_EQ4G4o8y1iAPcllqvVRZACX8q38km-XI-fHf_BqSMpRBaX-B7GVlurg_5ea0pps9ruaZusLEj-XgPomV8soU7KS14zGfwim9AM7L56oVuKObKc7eWrVTBI2cm68A3ILGefKEU3GzzlpIG_1_CzER2p4nyLFYVQPSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😏
شادی دو‌خانم برزیلی روی سکوهای استادیوم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/97130" target="_blank">📅 16:40 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97129">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KvKM0QZXRh8xDDQ0ItMNBlXIWLMLHLnARCFt2nnACcf3qgp9jg1hzwerJbvTHaCd9XZHr_ztE49XEryH5CBBHDSAbuTUJHTDgZtWJXv3MoTGFh7Aw7dkR6lumyLW7QNa_YMBWm2AUGsyVggPuQg5k5utkhXWT1WvvZiJEiOOZgPbK7XZLFma58-I5Bdm40ri4hMtsR-uPx51M5nwebbVWe8OOf0kQgkVcbE6qGGoX0tKptd_T68qDnJmMbWZgVtDXycSxvuQQD_ebLq0QTkzZRz2UUV0iUhyrBUX3qicEmnkFJkF4MNBY7BgW6A7fNyMVB77iGJE2xraS9sCf-WoxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">8 سال پیش تو چنین روزی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/97129" target="_blank">📅 16:40 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97128">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/Futball180TV/97128" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/97128" target="_blank">📅 16:40 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97127">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17bdf5f245.mp4?token=EGAolbIFq8k0YGUNlIIAGeQkyrUOLPX7PW83vWN0d3Z4g5eV0KdXdok1HW7Bnw8-lviEIv8ei-ToODp-rBiUlv-A4S9MhFw64Qp2zaULuIILRw1GmW8OmkI56VTnUI2QNhHnr-7tNPzA7OHakWBBWt4AaBuYOokiamKLVaUtGHj3cwYH4NAcaTauhiqTEGsMJZvLRNS1NprGttChoGoNakaXnQU7vMX-XuwYjct5BckRla4ZwjbogPDSBg8Gfu1eKWO4833hqJvpS6RGBCwKgPtejFRM0q8qu3-MSD6UkUl860EAk9jfl4lAqBn9fBHfU5Tr_Q1cl-GO2FGHZ9hIOpmiVrNYVt228Ni2v2jM2PqISPRIXM9FPS_9MWojaTvWjd8XEKIIaE6xlk3g9pxvOiEZxzyNRoO1MtPI52Yi2eFMd7auJMHdtYnVZCiQD-NI2l0UUtxK081C_H0vaPyWQe5kRc6zgolfSjlccwx_KJbM-DXmadAAmJeoNf1Cq_dKlL0W5JpiJ2CLaMlGxBg5UkQsQ68cjk9-zFyiv6cbt7wN1fiy4cFZm_L9iRAyuLrgRM8ISisYvPnGvc1CnVWJRqkNORQAZzVByg3fwaaEbocGwAAbjz9SZyP3j_jZWLCk8UO8s_h4wpmLgZCcoyIpkps6ARGrO42z_iM0LSfUlLs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17bdf5f245.mp4?token=EGAolbIFq8k0YGUNlIIAGeQkyrUOLPX7PW83vWN0d3Z4g5eV0KdXdok1HW7Bnw8-lviEIv8ei-ToODp-rBiUlv-A4S9MhFw64Qp2zaULuIILRw1GmW8OmkI56VTnUI2QNhHnr-7tNPzA7OHakWBBWt4AaBuYOokiamKLVaUtGHj3cwYH4NAcaTauhiqTEGsMJZvLRNS1NprGttChoGoNakaXnQU7vMX-XuwYjct5BckRla4ZwjbogPDSBg8Gfu1eKWO4833hqJvpS6RGBCwKgPtejFRM0q8qu3-MSD6UkUl860EAk9jfl4lAqBn9fBHfU5Tr_Q1cl-GO2FGHZ9hIOpmiVrNYVt228Ni2v2jM2PqISPRIXM9FPS_9MWojaTvWjd8XEKIIaE6xlk3g9pxvOiEZxzyNRoO1MtPI52Yi2eFMd7auJMHdtYnVZCiQD-NI2l0UUtxK081C_H0vaPyWQe5kRc6zgolfSjlccwx_KJbM-DXmadAAmJeoNf1Cq_dKlL0W5JpiJ2CLaMlGxBg5UkQsQ68cjk9-zFyiv6cbt7wN1fiy4cFZm_L9iRAyuLrgRM8ISisYvPnGvc1CnVWJRqkNORQAZzVByg3fwaaEbocGwAAbjz9SZyP3j_jZWLCk8UO8s_h4wpmLgZCcoyIpkps6ARGrO42z_iM0LSfUlLs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
جام جهانی ۲۰۲۶ فقط یک تورنمنت نیست؛
جاییه که رویاها ساخته می‌شن، ستاره‌ها متولد می‌شن و تاریخ دوباره نوشته می‌شه…
🌍
⚽️
از نبرد غول‌های فوتبال تا شگفتی تیم‌های کوچک،
دنیا دوباره برای بزرگ‌ترین جشن فوتبال آماده می‌شه
🔥
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/97127" target="_blank">📅 16:40 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97126">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N28IojNJ9pPJ2ZXWSOxVBJthdd2ubdYC67j7Jwtn3Wy089iTdk4P8DshhaMKvQFEEYY3fekH-TbbUoup4eYbF6JhAF-mX6SwWg9-VSrMg9d8jL-m1rDmh2K_YIUwY9N2cWfPLhv4L0XYsKo-rP7MOB68DRpaG5ke7kzDAftlflrgSDhU6raOKCyyCOLYQgTZiyHCQAlf6CGoKlQwAy8xdZua_xgSd40es61-VibWgJTsmliy8TI1Is69crp4kEpDht1waMdn3lBKgrRh-0uGIz7hnbQBbF2Z0wwm6VrVe6Dd51nSdWiEUwc8kzCO-ltLa_u0N7DRPgbJG2P47ksztg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
مسیر احتمالی فرانسه در مرحله حذفی جام جهانی
:
🇸🇪
مرحله یک‌شانزدهم نهایی: سوئد (قطعی)
🇵🇾
مرحله یک‌هشتم نهایی: پاراگوئه (قطعی)
🇲🇦
یک‌چهارم نهایی: مراکش
🇵🇹
🇪🇸
نیمه نهایی: پرتغال یا اسپانیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/97126" target="_blank">📅 16:30 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97125">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37f012c953.mp4?token=CPAFdI7CwzmrnJb0h_Lw5TCsDJf_5wVhW-HB195a1XZbSeLXsshE6jjfIJdePBjG4Do1lw-kwx-wt6Vw_aREbIpSBbIHCWAQVntntJp8y9DtnjIqzO0SxM9IpieZe2TVScLjlpEJWNE64ufwoKEZj32x3xco4GdE49RbQnGsczitD8Ut-mBbb3s9xRyACkAUYZ2pgidTkxhCpzPhjSugg5twN4zdEmv86jvRQYK134tJmSjlXsEiEn0K2inncdDtHmxHcORAUhp8iRmWvaW1FEp_l0XlGOMwId2MREk5OzOl1YTWmX9TLuGOkFIN-2vzx0HNoBX9eKywhefxNessAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37f012c953.mp4?token=CPAFdI7CwzmrnJb0h_Lw5TCsDJf_5wVhW-HB195a1XZbSeLXsshE6jjfIJdePBjG4Do1lw-kwx-wt6Vw_aREbIpSBbIHCWAQVntntJp8y9DtnjIqzO0SxM9IpieZe2TVScLjlpEJWNE64ufwoKEZj32x3xco4GdE49RbQnGsczitD8Ut-mBbb3s9xRyACkAUYZ2pgidTkxhCpzPhjSugg5twN4zdEmv86jvRQYK134tJmSjlXsEiEn0K2inncdDtHmxHcORAUhp8iRmWvaW1FEp_l0XlGOMwId2MREk5OzOl1YTWmX9TLuGOkFIN-2vzx0HNoBX9eKywhefxNessAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🇧🇷
مراحل آماده‌شدن همسر‌نیمار برای بازی ژاپن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/97125" target="_blank">📅 16:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97124">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lfErZXdOLqpW8eoO-uusyiptVLZuY0nr5PkMYwWs760R0vWWwrobbHjl6SomYCq6935eLOZgfYVIS58k94YcriRMeoFIhn4sVrYeVHHv2u354pyVWMEqdnU0nfvIs4GDZ4vSy-TInIPrUK6tmY2cI-ytaoNRcfr-dtpF4xfxHemSJTQsEWuweljkApVovgB5a-sP98w76GsWpSurhILiBJKysUCbXEbjOwusnhw7P3lL2W-pPh021GGqW5nqZYC5znoQjJSKPTxnTF6MIt729NjgrdY4OGvsbnL-KfX8bjNICGpK-ruftcBZ-77jjeAMrQ8qZ4KUDGAe5hWZUAkzTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
رونالد کومان از سرمربیگری هلند استعفا داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/97124" target="_blank">📅 16:10 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97123">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a9b21708c.mp4?token=n5stLouMMFyfLYRx9aV2-Xs5hK3mUrs5xR_ds-NKc0G53BdjdpagvfzHbvGqtmoIIVGbaKJtZ8yWdpSMmzgRZLxFXJ0dILMGO3FSwcFxHW2WbqQDdaza2orkaJTRZX2yori8vKak34Ju564aclM-T3c0KTVd13ii01kuUk4AuICwBO3KRhIwo_VDa2-EsGS0BZ0p2HSUlDTxWabCXvdpfVu_UU0cnK34G-IPLbnpp5odoPdTcfRrjTxWFwSqwMOZl1HLySPGoYA9EndkH-IUJ8qg0fiDuufd8kefKFYDlZmxPhvtRz1lc7NPASAWbsUcOOxwqlcuio8VvWAGMXfv1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a9b21708c.mp4?token=n5stLouMMFyfLYRx9aV2-Xs5hK3mUrs5xR_ds-NKc0G53BdjdpagvfzHbvGqtmoIIVGbaKJtZ8yWdpSMmzgRZLxFXJ0dILMGO3FSwcFxHW2WbqQDdaza2orkaJTRZX2yori8vKak34Ju564aclM-T3c0KTVd13ii01kuUk4AuICwBO3KRhIwo_VDa2-EsGS0BZ0p2HSUlDTxWabCXvdpfVu_UU0cnK34G-IPLbnpp5odoPdTcfRrjTxWFwSqwMOZl1HLySPGoYA9EndkH-IUJ8qg0fiDuufd8kefKFYDlZmxPhvtRz1lc7NPASAWbsUcOOxwqlcuio8VvWAGMXfv1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مردم مشکل دارن: نه مردم فلان کشور وضعشون بدتره
❗️
جامعه توش جُرم زیاد شده: نه فلان کشور بیشتر مجرم داره
‼️
مردم شاد نیستن: نه توی این کشور مردم غمگین ترن.
❗️
اینم از فوتبال ما مینویسیم اینجور فوتبال بازی کردن قشنگ نیست بدون بی ادبی ...جوابی که میدن: فلان کشور بدتر بود. یه عده ام که متعصب الکی بدو بیراهاشو به ما میگن..
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/97123" target="_blank">📅 16:01 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97122">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">💥
🇧🇷
شادی‌طرفداران بنگلادشی پس از صعود دراماتیک برزیل به مرحله ⅛نهایی جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/97122" target="_blank">📅 15:40 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97121">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aaa918da02.mp4?token=vULrxyRaIr3Q-0Dd62X9YU7hjn6AVfLq8cXhDnrq7y9MpLwHR2lwwILRgsrmMBIUVcOkYyYX41ps7xoTNWJvbPOeLw7YHtcXIqXKEygoI2tnDIr6l0OCIcifD52VeGHiULk2aMoFEa5ea8DjjthxgcAiwCqmxAcbvxycaWIVac5Ridy-JP5qFNa9hKs1xRELelp3JIlkQMpt_FBlfwRmnZ4zS8Vi4YCnxFRnQJK1baD-6fk57gj5XE-xpRaNumyRv--hC7nYwT4mnLshmHKKV03-dgef2rzPyP2Duj2OwhSVq_grC0OiuC70DlXeq4b89Q0d3a-hp-mJ2MSFM7eYyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aaa918da02.mp4?token=vULrxyRaIr3Q-0Dd62X9YU7hjn6AVfLq8cXhDnrq7y9MpLwHR2lwwILRgsrmMBIUVcOkYyYX41ps7xoTNWJvbPOeLw7YHtcXIqXKEygoI2tnDIr6l0OCIcifD52VeGHiULk2aMoFEa5ea8DjjthxgcAiwCqmxAcbvxycaWIVac5Ridy-JP5qFNa9hKs1xRELelp3JIlkQMpt_FBlfwRmnZ4zS8Vi4YCnxFRnQJK1baD-6fk57gj5XE-xpRaNumyRv--hC7nYwT4mnLshmHKKV03-dgef2rzPyP2Duj2OwhSVq_grC0OiuC70DlXeq4b89Q0d3a-hp-mJ2MSFM7eYyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
❗️
اقدام جالب نیمار در بازی دیشب بعد از ورود یک خانم جیمی‌جامپ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/Futball180TV/97121" target="_blank">📅 15:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97120">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ujjmH21Esj-9ewnEGVDNaXRgr3neMnZrlr7CbWmBtPgPa2CTkUiHYoIrsu11Sx0cAq4-cyGl6MWm1FAqhFZmJekPqJILvfllxFkGDatidB0u8pnlvyu-qmCdfju7TCoE9pSA8XEc1pvztT5sRp4_9-rMX-sVcCfz51j3U7eIIpTOn56hn8BcOhaLUtpDUbtSSto6rugj_3nlSN_BETaNoKeKVomJ9GWDT9fO_5i3HCGl6GK0UAqA0xzeA1YKtR9p0Mk5G5A6TPF3x3QTuzU8dvImqJxmhxCqKtdjaehBDr8LK5Llvn-66Ixq5AYH5ec9pyM3L2wWTaNlZwYnq3cN_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🗞
#فوووووری
- کوپه:
😂
فرلان مندی پس از اینکه یکی از سگ‌هایش یک پسر ۱۷ ساله را گاز گرفت و به دو سگ دیگر حمله کرد، به دادگاه احضار شده است
❗️
دادستانی خواستار محکومیت مندی به شش ماه زندان، جریمه و غرامتی تا ۲۲۵۰۰ یورو بابت آسیب‌های جسمی و روانی و دوره درمان است!
🚨
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/Futball180TV/97120" target="_blank">📅 15:13 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97119">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A6-60_Iua8akYs9luEl2dp_xwO7hFxe7wQ28qkplHN9QoOf4Buu_PCUOqKUajLKXgguSnD-6dPMz211MLnRvC7FqR4cqTsAzRYMVNc690RtQvw0YHHzC1UEXNZ4DLR2rVP3xKp1bMFNzmcOsv8xup5uyMs28N6Bhw6A3HBRmmn5qtCtrAB-aszrXShWu_tOmq6hbJgbyp4mkIvDB_k4XuYUnsprbLTl6XQiyiBaD8UE80FmqaFblU5PPHQCuivyhXGFp-kmw6QyYDN8f8XdT8SIZzkVTQEh9Cd3mxhhhK2Z7upwKN8kioGKDNJXLb0SYHL6fjA8TKx8yZzvtP0g0qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💥
🏴󠁧󠁢󠁥󠁮󠁧󠁿
حواشی‌جذاب مسابقات انگلیس در جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/Futball180TV/97119" target="_blank">📅 15:02 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97118">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/96ccfc4b2a.mp4?token=Cz4BiImOGa6EncODTNeFpkLu9hMzvt0GKS0WI7FjTi_tTrGgRQFFsvOI1qNtoRnnj9yiY7JwOrO8UC51V5DwN0DQbW_VoxATb0tXD3yE7DC2PxDgfICgxo3MIrrTris8BxMgKzE8JQSNocC0122spXIjOj2VUy98jmTCnz5VfjorSNjScuo6vlctEGVfRdPrZL80fEEvudsLJ2J2mNntmeid7-sG3jpWrh_f0QbuONtN9hCsgq9lb9B6nG7bgQsXlgnbWZLRV89H3LpzV7y-tdc07wJ_F5_bkmzEu8l3_8slTOcTfozmKSzG7rkdqKSHzczHdM9MecnghERHEutQIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/96ccfc4b2a.mp4?token=Cz4BiImOGa6EncODTNeFpkLu9hMzvt0GKS0WI7FjTi_tTrGgRQFFsvOI1qNtoRnnj9yiY7JwOrO8UC51V5DwN0DQbW_VoxATb0tXD3yE7DC2PxDgfICgxo3MIrrTris8BxMgKzE8JQSNocC0122spXIjOj2VUy98jmTCnz5VfjorSNjScuo6vlctEGVfRdPrZL80fEEvudsLJ2J2mNntmeid7-sG3jpWrh_f0QbuONtN9hCsgq9lb9B6nG7bgQsXlgnbWZLRV89H3LpzV7y-tdc07wJ_F5_bkmzEu8l3_8slTOcTfozmKSzG7rkdqKSHzczHdM9MecnghERHEutQIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
⚠️
طرز برخورد صحیح ماموران امنیتی استادیوم های آمریکا با هواداران بی‌انضباط
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/Futball180TV/97118" target="_blank">📅 14:40 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97117">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d804cfa856.mp4?token=qMgJKOPbdUlk9sxpgiSM8SCozclJLa8XaJmzicP1NBM01WuEqYe6x9DLe1oe36iQmkx9Axk_PjjGsrhboV_rm3MYdj7n69Y85x3Gnd4r0b8zmibdJp6jBswsaJVPO6b_SiOxToaLa2OBmtd2tIt-G1DFk6z4mgWLTJ4GQvWtEDh_3MYZfqoz9QZYcah4k8rG-8Qo5CGjk6Ssqq1T7SoNv8bKYwcxVqE1LBTik8EXDkGh2XKOFA4GUFfDc-HSOVyfBsH2wuOl_M7iJeMatC6QGCc33PGt6EkXlxpqomeJYLmEsGBz0QNXxqnQj9hY1XPsQEqJYFHNoZC25dh9mP7uWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d804cfa856.mp4?token=qMgJKOPbdUlk9sxpgiSM8SCozclJLa8XaJmzicP1NBM01WuEqYe6x9DLe1oe36iQmkx9Axk_PjjGsrhboV_rm3MYdj7n69Y85x3Gnd4r0b8zmibdJp6jBswsaJVPO6b_SiOxToaLa2OBmtd2tIt-G1DFk6z4mgWLTJ4GQvWtEDh_3MYZfqoz9QZYcah4k8rG-8Qo5CGjk6Ssqq1T7SoNv8bKYwcxVqE1LBTik8EXDkGh2XKOFA4GUFfDc-HSOVyfBsH2wuOl_M7iJeMatC6QGCc33PGt6EkXlxpqomeJYLmEsGBz0QNXxqnQj9hY1XPsQEqJYFHNoZC25dh9mP7uWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇷
🇯🇵
انیمیشن حمید‌سحری از بازی ژاپن و برزیل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/Futball180TV/97117" target="_blank">📅 14:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97116">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/autNJo8JDtQYGXYwKXNcmyUunLi-bQ5BjBJFTPUZSF4Vlc33Enrb9_clLbz71tFvpdtxKhijOK4HlzYd_tVag9YIJiS8nlhJO7Bg7LgGcMqgkgaar77_hiEAsPb75gmFWgVMURseYEu67faDRtLchZRfN3jTeDX2boUchsMlI0Za8CauDFPMQII6K-wA7yi6VmvY-0F2xDfsIegJhgagYRVDKM87uWmUCWDtRZupdbwHRVvhB5UHM3PhggGrbrBBQ1MciMtIEFc9600dchPQ4OOeYhKXRe0841eaVaL3NobW4QnRPLZfap52rX97bqnLYx7_kGEaBgzNZY2jy7_RLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کوکوریا :
ترجیح میدم کچل بشم تا یه تتو از لوگوی بارسلونا داشته باشم، من حاضرم برای وینی و امباپه فداکاری کنم تا همه چی رو برنده شیم، تمام کارهای کثیف داخل زمین رو انجام میدم و فقط هدفم اینه به پیروزی برسیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/Futball180TV/97116" target="_blank">📅 14:19 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97115">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3a0c56dab.mp4?token=oR6rsyX8Lu6BwFu_gQRWWCfxR-pwHoz7GZk2djnLwbTI7LgqsNPmI22oGQX3DfUfcMr6OfcKl9PVR6F30DxhOYrUE4Su7eI5eq2cD5YRvgwZL8Zy5pXcOS3Ligb7PKVhZvJDXpG9OqPq-CUUW1RCMbzXXFEYjg_dcikpmdCRPT4JyRT-HRrjCdUt4lBoa8pOR-034NkKySkdHcF9XkyhEZRccUTKrkdnh1knjurgX0b-Rd2sl4093hNjBuOtAaC_wX__4lUU9JFc9tYbCCZhhg3FqPw_7W7-k77dxrQ9c9OfVQDC_oM4ynGKcFwmF8lXIT-Fg2qmCkroNm92CXCrWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3a0c56dab.mp4?token=oR6rsyX8Lu6BwFu_gQRWWCfxR-pwHoz7GZk2djnLwbTI7LgqsNPmI22oGQX3DfUfcMr6OfcKl9PVR6F30DxhOYrUE4Su7eI5eq2cD5YRvgwZL8Zy5pXcOS3Ligb7PKVhZvJDXpG9OqPq-CUUW1RCMbzXXFEYjg_dcikpmdCRPT4JyRT-HRrjCdUt4lBoa8pOR-034NkKySkdHcF9XkyhEZRccUTKrkdnh1knjurgX0b-Rd2sl4093hNjBuOtAaC_wX__4lUU9JFc9tYbCCZhhg3FqPw_7W7-k77dxrQ9c9OfVQDC_oM4ynGKcFwmF8lXIT-Fg2qmCkroNm92CXCrWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خوشحالی شدید میثاقی از حذف تیم‌ملی ژاپن از جام‌جهانی؛ چشم دیدن پیشرفت فوتبال کشورهای دیگه رو ندارن تا به مردم اینجوری نشون بدن که تیم قلعه‌نویی عالی بوده
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/Futball180TV/97115" target="_blank">📅 14:10 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97114">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/53f3cc7f42.mp4?token=PzrcpsWwq43c8ZEZlxSJMpLuzrLyP8EZCBVper-Zx8tUE8Ce0dXxYUFd7_-3Wff4T8B9NqWaN2o4I0dTWQqx2yP3y2H8oeAgwx9HfHnPT1uPgX1knYHiA2uGdOsGKsHQiTuaIywxJs52zOyI3TbpVg_u72zjgl_RfRbF1v9Lm4qfPuFtW1lPpf638MXPkQLth2_zTeE9RBtH8AYe6gPeDXch-0e-vlJqS4OxYhfy6YVwKw29HUvOhcEbejxE-7HnGzb92FYJF0rRysAK0w-RZ4kaex2SlWUVLYMQjYWDZKmqA8LPahQxZcSiZ2IK0dS8hOToXoYnVvfQjJ63wUrf94ovrcluyDP2oooWczGAc0j6pg8ZCje2Vf5Q3-eV4lopMMTVJG8t1nZHu1ZFym66Vvv_2GT1k21uyone8i4r1akAlkE8VNl4N2a8C9idwc7pgD04AKyqqufdajvNStgMeJ0D6lP0JKFHcf5CCrWdOfD-6VxD2d2neRZD3pRnPecHSTUhU_j020gUJEa1E1E0qZ-JT3AEjnpdFKxecsyrXdUDzORoHw2DxygcJ1Wv4W2PsB5zKnioO-zblEMoAoH0OA5PFVg6S_QhGjsWeiWdi5UP1tVO-kIMw1t8Ky8PY4TzeT8UC3XG4WunKaO55puROoYw_e5492HObqBSy8WHj2I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/53f3cc7f42.mp4?token=PzrcpsWwq43c8ZEZlxSJMpLuzrLyP8EZCBVper-Zx8tUE8Ce0dXxYUFd7_-3Wff4T8B9NqWaN2o4I0dTWQqx2yP3y2H8oeAgwx9HfHnPT1uPgX1knYHiA2uGdOsGKsHQiTuaIywxJs52zOyI3TbpVg_u72zjgl_RfRbF1v9Lm4qfPuFtW1lPpf638MXPkQLth2_zTeE9RBtH8AYe6gPeDXch-0e-vlJqS4OxYhfy6YVwKw29HUvOhcEbejxE-7HnGzb92FYJF0rRysAK0w-RZ4kaex2SlWUVLYMQjYWDZKmqA8LPahQxZcSiZ2IK0dS8hOToXoYnVvfQjJ63wUrf94ovrcluyDP2oooWczGAc0j6pg8ZCje2Vf5Q3-eV4lopMMTVJG8t1nZHu1ZFym66Vvv_2GT1k21uyone8i4r1akAlkE8VNl4N2a8C9idwc7pgD04AKyqqufdajvNStgMeJ0D6lP0JKFHcf5CCrWdOfD-6VxD2d2neRZD3pRnPecHSTUhU_j020gUJEa1E1E0qZ-JT3AEjnpdFKxecsyrXdUDzORoHw2DxygcJ1Wv4W2PsB5zKnioO-zblEMoAoH0OA5PFVg6S_QhGjsWeiWdi5UP1tVO-kIMw1t8Ky8PY4TzeT8UC3XG4WunKaO55puROoYw_e5492HObqBSy8WHj2I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🇩🇪
آقای‌ناگلزمن خدا ازت نگذره که دختران سرزمین ایران رو اینجوری ناراحت کردی
😔
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/Futball180TV/97114" target="_blank">📅 13:58 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97113">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ef2e2b2ce.mp4?token=uJ47_8ALKaTpxCTRAeFSFmIf-Dm733QirQ6aYR9-ghyZwqoHr98B4hUQRen47V-Sa4X896jwCsnPpKGELcOCVu4pSvHLSXpkfGQuJBD6kCbUc8j01CN_dF3KTv_mGh0XNayC3J0UzsAC-3WtlP0VcbX2UoUslKuG9U4mamiqd6ypk5JUz6vZo1YU79e44zCF6h7iB6WdPMXg3YIDY--loraj249RfrvX5v9OTYMQasP5WIfUHAkWQRwXQGuN4sw3rEXqIl3D76TMrklh5eEFUgmjxEAmdmWcgocauUrg48JhlgSTaA-2dC1o-pFPu0VxC-gjNT9MScBEuaJ1OdsSzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ef2e2b2ce.mp4?token=uJ47_8ALKaTpxCTRAeFSFmIf-Dm733QirQ6aYR9-ghyZwqoHr98B4hUQRen47V-Sa4X896jwCsnPpKGELcOCVu4pSvHLSXpkfGQuJBD6kCbUc8j01CN_dF3KTv_mGh0XNayC3J0UzsAC-3WtlP0VcbX2UoUslKuG9U4mamiqd6ypk5JUz6vZo1YU79e44zCF6h7iB6WdPMXg3YIDY--loraj249RfrvX5v9OTYMQasP5WIfUHAkWQRwXQGuN4sw3rEXqIl3D76TMrklh5eEFUgmjxEAmdmWcgocauUrg48JhlgSTaA-2dC1o-pFPu0VxC-gjNT9MScBEuaJ1OdsSzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
🌏
پست‌سمی پیج‌چادرملو بعد کسب سهمیه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/Futball180TV/97113" target="_blank">📅 13:40 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97112">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HH0DSxEMlgQ3beUjI0pZMW8Bhdc_TTLB7anrQvOn1935YRRUBiFyVg-q6H-8EAZhiY3q1He9SniNYrEFS3mbtPofvBD_Hgd2RM8timhuGQUBu9ofERLo5tcxOfgppe9bQrgFKlq9RWFmhWreQis-O6JtyxsgAWPp0OfZb2TA8Ko3C79oRDoGOfMZ9mxFY5_h_9auDZzT-h15XnUdRNJ5Nchl0jt_djRKdFo08BCxccKGykq7q_qUf_QhERZyIR8LcRbC4MTfiif1MUlz8HxEsxQFoF6Zt5sTjTcYuXQv8GFcti9SxZjdxvLWrMa-7EUX6urjQ4r5uwC-c3jpf6WLzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟣
#فوووووری
از رومانو: قرارداد کاسمیرو با اینتر میامی سه‌ساله هست و بزودی رسمی میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/Futball180TV/97112" target="_blank">📅 13:28 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97111">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gri0wBS97g83x4PJZlioJsFL74tF-BlzDuYvHd14x46VbCCuoSdwBKUT7onjcYpc-_21jxbdDcPOkr8VBAl-XcPlHAh_zCxAOUebFmTaDU5EyLK2ionNVuwcZzV225_AqOibSfIUQeLUKgpaKUqNBW7-saHrHUjQO_RVfZ9OcLljAhAt8ko9f5jESdX8-93jMewMb6X3mXSpqtxruaKPbU-fmwTpjYCPNKvqozskKDlJGlyYc7GhUuk1vxO-BSkcrWnh1ZDsGvlNlpWsnVLYj4ly3kqtjJmp1u5DioX5Nd7GLTwOgRvxdFPNCuAaj1tTgKJQcjFgoHTcixKMGm53Ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">متئو دارمیان هم از اینتر جدا شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/Futball180TV/97111" target="_blank">📅 13:24 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97107">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B509k5TtLGwRfdA-DqclXMgqY28n0nQXSeZBU1jaWBif9NGtTTISut3dgSPhFb3hRsqcGBbdL-vRgqYi3SwgsvHv1XeYea_-SWjX_CCIiQNvKy9ImAitKLOwAxboGIUib1kKkpY_uBK3eqMrcOeUAa1-Av9-flgcDEPx9gZ_M_EXBJVxIPR9_7auMe30POXcVe8FROYx2HNfvyJeeDrGAJEvXj8NZIwATCwieb2mUIAqHvr0FmGmneFGdBum5MuW6z1wCQywsr-Vda4lWNtextYxfXirzYNduRsi3UmMqEIDT1O9X2dpAOl-ojfOQjCe61aHhirKKoBSWJU7xVaxow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TJrK_IAhSQxMK6nMGwBccMpY9Ueg3biWcSquVM3qoIP2FmjP2waPwF1yAkboZRfUxfmpC3Cbe-lnfhbE9H2lHK0LONTZDsaXqgtrFS-GQw9tOmVBS4aawY9VNXvXlpKs8bOLacXT16o0K1Lt3AbLNwEtFBJoYt6k4an90zJ67vyRqEzaKis6LD4G_Qd-nImzX8rJNY0UWIPAehaioE55a8UpBOyFXDmaCSIZlwfHuhEbcZDbBqcHPBEd4Mc9P6Ky7sfpW_g34lmhWsKBDnsLWtABhnpwjA44pXYwN7UxjXFx4_ZJwCqvisT9t_WkOHYAM7pT95Dyw2C_J-rZOM1Zbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KZSHFA8QXR7JSKWESfbmCXB_DZnqAi30yzE273drdNh-iXDV-hqMlRpctxi36AQzYfH0dWUe7BlhZJqxTI4Y7qhx2ErLGXJk0OUhCEqbDb5sP2YCf51fVHwkfSuBH-07YDKVqy6gVqWGCwfY6khGfw9isfrBlefue1Qd_iVnG5Ca1vtzpnyAC3nuza8QP_v2J0T2igeSE1I00tr9OhaoifVxUm5Hz2mxj3mswEcuFprHPKGvoJtb_cpzEeSG_u2lltL0rgZpQ-L7JWbkRkgQVLgBabU-w5ZUMfWnLpwTOf27nPEjJnDWQULTX6yXYsWTUBQiWJYEiM10hy124gHypA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RimJ28GNTUrOjiAh-QZq0ScvUdtx45R9zhWbbgJ7jxLqxrGRQXVbv3ruXESyRE_MoRqYEsrQ9qHwHZvVKflaTSe-H6td7KQpUKFJoXvqslg0NK7Vh4Cv9OuTrx10RQ31-ZcfrodGUM_WtJDuYfmMoxAu5ZBZVrsxYN3A0BHtlnxPwhgauEKy_WSCvF7mw6sbBdXMuQGUAB_ykx3H5314_pPzWUwcSSg9U1v0rf8AMc2Sh_APqHJntWrF9V35kX0quxQ6pKf9AlU7BfGdqhBvpmDpiXq7Uec4rBoCQ0t2HS01YwpiUXrCxUs6_1k3BmqfLOWzq4KLeAoWY4YRumz_bQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">💥
تصاویر جدید اللهیار صیادمنش و همسرش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/Futball180TV/97107" target="_blank">📅 13:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97103">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NAkJc0ElJMTBCfbAYN_Kmp6YqW_CyC9iakSq49tdUlGI32_IUxWtPpczhs_QlBzfgwJnO_AlPrMt_JeXvEnANzvCP5-KXIiD8URHnPVWu_s1I-RuZC8uGHZOdOhiOSqTw98pOKOaoR5ebJLbzLQx-iX506cj5U7OM-my2XMVgWu8tCIuwgOLYgdBPSwRWqBJrNjlf3aqBxhH_pcUtGxcbgjmMVstK4mRGSFqdQxkTF3YZA1b0Z3FLlPbe6HIbcWssU77QPEFs7tDGSUwGp2zcsOIWAnxZr9O7196q0d7QH2lSRGXgoZAixhtKiB7iwzFRf7v43B0OoxSImJ_m1jCgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dkebCoE3n8cPR_9r9KGpz2SbvA0S7FfCBHEKQY6DsS23qkqPOTcJwy3N6nAvrmFfWM9NS5SpHY8zhefNobbGuK1v0qB8HYE_y6jaBy1uNgzo6Ptos0pY_bP9AXH_Y2GA17_kMBcKAcnxqyleiRMlSR7QVC8AHjWJpuz2gGbyKNg7VqgWiGguuqXOyOuMleOB_yfrotwfFGuLnUdgh3t0hy8smsMGK4O8Ec48Yt7asAMFfyhcWD-G5qoVZ5-HZTbFqnVIZeY4Umqk2D9ftY7dKv_KiRPSTF8G2wYtuxvWMiGs4aFtDGpiQ1lI6VlBOBbKDVhvP2fk6lc6sONSN1JMHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qFIdbM3MrcVoleA-85N0eqj59R6J3RXj2JwAuGK9c8bNgQzBF79Gzgrrt4XPdzlNHekdCLHjPESOxHVqaoQmhGL7uLWFP1y5g-yZDJ3c6bLwKxBFZiyoo8t1BLChVh43kqnPalaFqydcoa5YDUtowog8YHAAu59fRSpjM8oI3V3g1F63K7hfXdLlZT6O2ADywReMwtGZ36We0-ThEnrYhV-99bjd91K1gypyet4ZmiV5ZjuVOXLGDgpAQ5RJFq9ZcRzTzCskIO_AS8wWOFx1jAOOTYIU3Z7vSHZGFpGYMA9_BQnrd69NakfL3NlzC88WZkP-D5jCzS1P2hAjxINQUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZY9FX5ofP0bglUqHw0Om7sCRbAqGeD6xrNNri-Me9Yq2B2DCRD7MzMtw8LChvPJuBOGTeMx9mnSYr43ikWr9SBVAk7gKhaGENuAe6-60v-1Ao4ffxs4YWx46if3oL_t0tWQbBNf8AFOeFEDtNgqxZPYln7qj_HLlewBNkjM2KluZwwbqO20aZDZYQuPhyxkBCvJB-3jFGZzSVoV0oOBlkjm2Czvi1FQBMQkvOHeYvoMDWClnfrnfA2BUjPtFv8PFbLc3B1xOFxBTm4Z8WTxQeuF1W6TbW1ryFUZca4WYNtXRq3JyIF1eYGpeCh4l7LCiZIzUbeobM4K8YqR0tk2V-Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇵🇹
هوادار پرتغالی در بازی اخیر با کلمبیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/Futball180TV/97103" target="_blank">📅 13:03 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97102">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L2SJ9Kl_GZctm_-hkUQ_ZsFmk-81vS59KQOeBCFwk43tKn7hhJcqEH9vKig-IVoWvSXwGpNm1zUMFAKJrctUm_sndfiT85DbCVRSQytAKYOcdIGq9k7zazRLbPWIEHu3CSWTa5DKot34SZ4wYiZE7lBhM9kcB27L_W4lwLXXLx0ADMAq2gWHmOeoUb1VLWGOUtMeWdZQiAlUXm_FmBLtxFxoF6jPPDiJ60dZYV-4WSc3JRDHEkkqjtTtICdrI6BTUI-W5a1jTO857qfUyOmKHSwx2Fe666Y4DfNnrPvtc128aKZyRhSomXEWIMDF6pixipgPVAI681l7JDYwIjQOCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇹
باشگاه اینتر اعلام کرد که آچربی مدافع این تیم و کابوس بارسایی‌ها از تیمشان جدا شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/Futball180TV/97102" target="_blank">📅 12:51 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97101">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f2b3d094a9.mp4?token=X9Whe0BVnYYC0Yh3V6lMnOr_bek-274ix3z68uEQLquaDkA6eZ6sEsKn0t7IE7XpkpjASOzf9k9jYouT840zUr8seQv4FEajQviDz1iNGIRCJ7zYeQcdq1nEmZUHH8lbmDKfsj7I1dSGIWuXDJFCGCQxcoJoHu6ZkQhY2eepRvaDI5wePseFqrcJnWwae7-Vx93-r1K09YW-CQ8r2jz-rdLocBbAxN34HywSuaNKxvl2jvO-DRMuKZ0mygzRjNKOgh9_kfgrv4pfRiADXVuJoBA47VN2RZSv9sCe-sjVtswhP2o-p7yIYkbCtgDV3ymRlwddZvCFI7yjwN31eODu1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f2b3d094a9.mp4?token=X9Whe0BVnYYC0Yh3V6lMnOr_bek-274ix3z68uEQLquaDkA6eZ6sEsKn0t7IE7XpkpjASOzf9k9jYouT840zUr8seQv4FEajQviDz1iNGIRCJ7zYeQcdq1nEmZUHH8lbmDKfsj7I1dSGIWuXDJFCGCQxcoJoHu6ZkQhY2eepRvaDI5wePseFqrcJnWwae7-Vx93-r1K09YW-CQ8r2jz-rdLocBbAxN34HywSuaNKxvl2jvO-DRMuKZ0mygzRjNKOgh9_kfgrv4pfRiADXVuJoBA47VN2RZSv9sCe-sjVtswhP2o-p7yIYkbCtgDV3ymRlwddZvCFI7yjwN31eODu1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😂
😂
وقتی شجاع خلیل‌زاده سوژه ابوطالب شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/Futball180TV/97101" target="_blank">📅 12:40 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97100">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C0waiIG2ptBVADya68H7f5jYyi3Vf4TIgeGhuFoAClyKIL-BUe3qaiAx6wYf--SZo-JrcNuSFf7KjevcznhYkucJf9l5Y7gjQ7niitcBW9ECPMwGk18vzgbqb5ztRgHyY6_rnoyn2YR3hmuFs3t-2NCHZXFSujtTHnWLq9o2c4mQLkvu4APcMzcH6yaaH-YX_Bnu6g6eLfGhqv1WqChF2rlv1ouj3A1EML6FfwTi5aHA983oiuCBcYr1Qz8NI9bAd4umnwx39neIhP06yAADJqFI5v-V_5NekpGS5tC2pUWLtDgYGt9xGM69wT3_KclurHt_Rd-T5G20FIbGjzdhZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
🗓
🏆
در چنین روزی ۲۴ سال پیش، برزیل برای پنجمین بار تاج پادشاهی جهان را بر سر گذاشت و فصل جدیدی از افتخارات سامبا رقم خورد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/Futball180TV/97100" target="_blank">📅 12:28 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97099">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/197441ec59.mp4?token=M8X7vemrgeIGj7dF9Q41FYhSbvbBtkimf_NUIDu4ldcmyST5-Jfaq-fgXSiFnCvcn76IYRsB-tUB2HhNPLVGdMQKj2IXJZR2w7E_QFF07tjLNpJLbz1XyvSTk-NgxLl1UPu6mYbHGSbqFrZRyXiCPudBe1s_hUkwm0H27_175_UAZQPEvbvTizI1FcYKR_MJPGbLmouAhoBkkRHgIm2_QHbESsIdMYli2jdbBr9XMwplX_rCm0DX2j8qe-zsi530IPYDVIq1UlHu8nrIwV8Qh48lIH3O44JkvQRwbjyK7Ow9jQlS_dSgxlPva-yUO_3dNfXOyNNVIwJh_IgQzHa7Xg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/197441ec59.mp4?token=M8X7vemrgeIGj7dF9Q41FYhSbvbBtkimf_NUIDu4ldcmyST5-Jfaq-fgXSiFnCvcn76IYRsB-tUB2HhNPLVGdMQKj2IXJZR2w7E_QFF07tjLNpJLbz1XyvSTk-NgxLl1UPu6mYbHGSbqFrZRyXiCPudBe1s_hUkwm0H27_175_UAZQPEvbvTizI1FcYKR_MJPGbLmouAhoBkkRHgIm2_QHbESsIdMYli2jdbBr9XMwplX_rCm0DX2j8qe-zsi530IPYDVIq1UlHu8nrIwV8Qh48lIH3O44JkvQRwbjyK7Ow9jQlS_dSgxlPva-yUO_3dNfXOyNNVIwJh_IgQzHa7Xg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇷
💥
شادی هواداران ایرانی طرفدار برزیل از صعود به مرحله یک‌هشتم نهایی جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/Futball180TV/97099" target="_blank">📅 12:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97098">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c36135326.mp4?token=fLCXf-e-aN_1eWNWENYC9oKf-MMIJIrxwSx8wHhn7jZpJoOowW7eMsfOk0upWrqDUuMUx-1ARCNQRw_vPoX9laS0SROUQL0VbJZ9aAnSS-XN2L3uTdHdFkkbVs9_-vdFUjw3i_WwQGeKuCH8buIyVnh_aduxIsPlyBqBIRB2dEwi8yjVfcn-Tste_V4Nw_m5GWIo28-suZHrqQw9xj8haVlJPpwQSazDYkm1vqrireP3fnwe2sb3YW8PUEwOxtWzaASi7lStM-F9ft9RT20XXhFN330MEq-bHp8Wl5_VBK4ZmPMsId3HgUNdhIxB7SWwGynYiGoz9PzM_LVTIOvzdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c36135326.mp4?token=fLCXf-e-aN_1eWNWENYC9oKf-MMIJIrxwSx8wHhn7jZpJoOowW7eMsfOk0upWrqDUuMUx-1ARCNQRw_vPoX9laS0SROUQL0VbJZ9aAnSS-XN2L3uTdHdFkkbVs9_-vdFUjw3i_WwQGeKuCH8buIyVnh_aduxIsPlyBqBIRB2dEwi8yjVfcn-Tste_V4Nw_m5GWIo28-suZHrqQw9xj8haVlJPpwQSazDYkm1vqrireP3fnwe2sb3YW8PUEwOxtWzaASi7lStM-F9ft9RT20XXhFN330MEq-bHp8Wl5_VBK4ZmPMsId3HgUNdhIxB7SWwGynYiGoz9PzM_LVTIOvzdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇯🇵
کسخل ‌بازی هوادار ژاپنی تو بازی دیشب
😳
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/97098" target="_blank">📅 12:10 · 09 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
