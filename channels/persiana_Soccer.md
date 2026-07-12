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
<img src="https://cdn4.telesco.pe/file/BeLSskF5GDFEfoeftmQ0aCWSxrsQ31UgjHXCXaY0nEdiz6N_AHst36mPCFvflWGfT_sKxfd0M1SdUXMTwMOYxOG32_sCyBDEyM0DsnZe3ejmQaXDJ-XitrhcNCma3EddPN5CbKH3Xg4hM54nRn-bIw4wj6dHgAw32DZRNkeMgsIxJFDPWDzrIOCxINE7dVQkVWIi0oOo_2Ef2-CGobgzd8Pc3MfNDoBw7YHiu301sczTvW_fzSvilswaJ5WBKE4Tc0fYW8glcBG2s_-1h00Srg4Z4ULxm3VKKtdrJrJ_axQxZ5bgH_FzVdUnyu46SfELSRPyKGvDfE673w2k0-IJhA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 435K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-22 00:41:58</div>
<hr>

<div class="tg-post" id="msg-25559">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iIcOzAo93kW8ifsGHXXAp9PGkMKx1BqRdOq6bbprvB_WCyp_Q2eZpzLLcN0ZPoIeVxWmp1u_GUuGa7E1gDn6ukPYGgIxOYnOSbIKF_XYwTE6AYa_Ssk4bkOhi2TnBUWE2e3RrXwM3sW3w6tM0J8vYb35C49hLh6LRNkZnUTvXWiLYxdEcjbvzSQLYliKRCUidbwYqiBQtYFgTmXNAXjz3jghfSImCyktqsvG4SL7L8m4x1gGplyvy-4juuFRwIAMZxGX3Z3cg2xBgBvzii4F_7nLmML2HcedMSK62pjCkUDvfJEKPhB8O2I-TBy583VRgUn2HzhccY8HQj04aowTaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
#تکمیلی؛ شوک‌شبانه باشگاه نساجی به باشگاه پرسپولیس؛ طاهری ناگهانی بازیکن نساجی شد.
‼️
درحالی که روز گذشته باشگاه پرسپولیس برای پرداخت رقم‌رضایت‌نامه کسری‌طاهری به ارزش 700 هزار دلار به توافق‌کامل رسیده بود شهاب زندی مدیر عامل جوان‌نساجی امروز صبح به مدیریت…</div>
<div class="tg-footer">👁️ 7.08K · <a href="https://t.me/persiana_Soccer/25559" target="_blank">📅 00:35 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25558">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bIJnXuks6_U-lN_uLyJNSdZUyisSDiY9LMeI8FhkHBNcIREgLVuQTorSumM4C4cI9eTehMZqUvqjxq8VcP3zA0YufQV_C2Wqy-tSKtuE-NhMEKmbz2q3kS1Ljtalq8Di-TFLnkjpImcluR8dvmiG_8TWhhQAxpda34ti83d1ydw66F3VvbV_XUXuwHHBNGLJDUdCBz7gm-8TsahoVTMFLGPGuWXXRIXbuDgaXNAzDt0qlRzXhCZaXHJBDG18WmZ4p8QZJN4Gb1QLkJ5VFfymAqAhbUMBUsMt1LO0zxx-_8quv5AA3zpEmfPvqedMhY94NCEpA5KWN5UECHExvs0rkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
#تکمیلی؛ شوک‌شبانه باشگاه نساجی به باشگاه پرسپولیس؛ طاهری ناگهانی بازیکن نساجی شد.
‼️
درحالی که روز گذشته باشگاه پرسپولیس برای پرداخت رقم‌رضایت‌نامه کسری‌طاهری به ارزش 700 هزار دلار به توافق‌کامل رسیده بود شهاب زندی مدیر عامل جوان‌نساجی امروز صبح به مدیریت…</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/persiana_Soccer/25558" target="_blank">📅 00:24 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25557">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MpJPnXdQ8MxpFGAtp5BPVEvC09GXYZ7MTFeJmInBe3LW8KfGMr53k6GUgFiW1hyJaML3ZLL3ZebA1lmxE4VJrtjyqzi_LG10Bg2lOoteli2cDRDRRYAmLOrzLKzSTsj7UhRNzoujaQdRjAA9YE7p-d4woABlVIUW-Wf3haLWF_zz63ZrYFT8aAHe_fyfft_uS_DQBm0f2TjSO-UcbGibmtudCzElGp1LPfYXp9cS_j4p6bbC-jlNjPUGlCJmCzBdNzhTYAdKhr4BQPb6G-og4NMglFuzMOovavDflxojewupm-v_55YlPY34h6EBsxk5plIB7Pbdn-vWrinGrTit0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
کسری طاهری مهاجم جدید پرسپولیس: ظرف 24 ساعت‌اخیرکارهای‌رضایت‌نامه‌ام از باشگاه روبین کازان انجام شد و فردا باشگاه از من رونمایی میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/persiana_Soccer/25557" target="_blank">📅 00:16 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25556">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JynSYoJJOdg4vnG_LXmMQX08mHqtq2MpH3-7Y5AQSChdTcVRP3CXqvQ4TnQhk7GR31Ro7mJil-WnzkZTQgMhPbcY-1XMD0lfFtK3SJIhSyx1JhbfiQDBZQastgd5QlsQUgThcIewd7D37S9cB7_7V3etsfzPl2tYgmhQmEY6Ugu9aqm0XOFasI5xuwBT5lSsZjSGDM35p_z_stqQcp3SgOkzCrWaO6G5SfcaVtzhbLrpwqoQP0CgZdtVrTaTVc2X2bZDLar23wKS6M5tMdUfFOrIdRTWyeuD6b3vpTsozJmhkObgvbMzF7RSdb2YO-YbLy5jZKyaOyFG1Y_JKIRpnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مصاحبه‌عجیب‌ زیکو بازیکن تیم‌ملی‌مصر:
لیونل مسی، بزرگترین بازیکن تاریخ فوتبال است، اما بعد از کریستیانو رونالدو و راستش را بخواهید، حتی حس نکردم که لیونل مسی در زمین حضور داشته باشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/persiana_Soccer/25556" target="_blank">📅 23:59 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25555">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/29a89f9e96.mp4?token=YHUyvdH1JoZimsC0rneIcmlo445oaGGO5yDDsdGcy3CnWMpVr2d5nEtjeDRUl4wMpErk2D5-Z4YedRpxoIVOsfJKSbKSzqGb6Ug60JO3GuiidErBX8QQih0eQrAfflPcYRBp94cjmmgaSkHMBLtm4G4NHOEf4k1N04LG6jjFvTrfbKRvargmTF0skSHczQ_RzvFlDMso7AU_kaRrHfEhoPwfM6TMR9y2AaBHuJcN5aPpQq6-x8yrjMyOzsEwV-2ilJ7MZyg8ei0RML0TLQvmVI8AEnf0rsa0ivuIPAi0Gypftm-tNxHYxLOO9fjKPlyR5KEWyZBSIpDGSFFITb7HPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/29a89f9e96.mp4?token=YHUyvdH1JoZimsC0rneIcmlo445oaGGO5yDDsdGcy3CnWMpVr2d5nEtjeDRUl4wMpErk2D5-Z4YedRpxoIVOsfJKSbKSzqGb6Ug60JO3GuiidErBX8QQih0eQrAfflPcYRBp94cjmmgaSkHMBLtm4G4NHOEf4k1N04LG6jjFvTrfbKRvargmTF0skSHczQ_RzvFlDMso7AU_kaRrHfEhoPwfM6TMR9y2AaBHuJcN5aPpQq6-x8yrjMyOzsEwV-2ilJ7MZyg8ei0RML0TLQvmVI8AEnf0rsa0ivuIPAi0Gypftm-tNxHYxLOO9fjKPlyR5KEWyZBSIpDGSFFITb7HPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
واکنش جالب فیروز کریمی کارشناس شبکه جم اسپورت درباره صحبت‌های طارمی در رحتکن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/persiana_Soccer/25555" target="_blank">📅 23:51 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25554">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uDzh2d0ypJFhMq5CuyuyLhCQMe1LmZ2dprUioCnyhTQ9Bw_3gZIIsuXB1lRJ9mv3AbOhnGbefttGCj6RbmW_rYV-DjLTT4IxE_VAVDtk4X0LxNEx_pLBJhndaWA5liX1DJ2j09W_fnA9EXJYegfDBwtRMcwCG09s23KCkay3HpjmuYPdIVhJC0RVyva0rEVVNMCunc9n9mbjiD6wfcR_cl4MYgxsCwlYE8hgcfxy7xsymKa_DmAD4oOFFF2XAkOTIgQY6qYrtiwVE7KmUMheN5SjRuLnLpArKvoj9xSWK65sO_uxW6s-CNqW_oPRoPA3uxdxfvmJmHj6YTTdg4IGWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇦🇷
رنکینگ‌شش‌تیمی‌که تیم‌ملی آرژانتین در این‌ دوره از رقابت‌های جام‌جهانی‌باهاشون بازی کرده؛ به هیچ‌عنوان‌نمیخوام‌ارزش تلاش و کاری که آرژانتینیا کردن رو پایین بیارم، اماازحق نگذریم آرژانتین اصلا مسیر سختی روطی‌نکرد و سخت‌ترین حریفش، تیم ۱۹ام رنکینگ فیفا بود!…</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/persiana_Soccer/25554" target="_blank">📅 23:38 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25553">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pQMammMSGbIEN0zu0eXYpe7mH7S0vEW6UMyjsJ0OUsxHDvNoOEjdtKa7VQkw7VABwUkpQoFJDYfnizh2IALb4a8gB-NBY6mjhG88bCab3Ijph7Tw7d98NpmGklarHVux-Mf-ejh6HVDAclM7nK3fLorfbEIgRWKYaZIqBujmTQGaiOm14CEGC--UQiMW4FsrSfuLPMXFkgHI4hrT3lS5vxpViIr6cR4-GTd1Sakc_2YYpNFvfT6FEeRCMAxzXf01cl0Pc4UUimzMDwftXEIUttmXTJIYHujSplwaIlTwU9NpRPWFX6eN9N7CuhP4rF2TpxDsBYVVaMwv5UAiEMDAwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇦🇷
آرژانتین‌نخستین تیمی‌درتاریخ جام‌جهانی شد که بدون مواجهه با هیچ تیمی که در رتبه ده تیم برتر فیفا قرار داشته باشد، به نیمه‌نهایی صعود کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/persiana_Soccer/25553" target="_blank">📅 23:22 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25552">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YcFgNrvzTPws02Iigu9fSoxh2CHi14cV2aZbNEV3SD_a2zSIoKIyMkJe0KY8UqyNzNANCGpC1atT64hd2agJEPNrmTWjyz5FOiErYcHmQYNMsA2iLfiwyHlD7unooqQ6Qf36I2uZuOIhesPnmvERJaA4IpDSvvUjOeqpwk8KbQ00u_nFvVuM8p0k_L7PXfmlNOXM02HTSAaeMTNb-Oc2qQAsJ7_DkVZwM2xwrRFA2hHF999ZMntBhTJ12-Xf3JVQQpWSm_2gXhsdK_zeT7I1pXItrcopaJFmyYqCpAv3n_iBg2y2ARiz2gjOQKxRvlQ7sPCbGD6iqFoY8qfsp8MMMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
لقب جالب لوکاکو از زبان فیروز کریمی؛ جالبه بدونید که برای ایشان به‌خاطر شرکت تو برنامه جام جهانی شبکه جم‌ تی‌وی پرونده قضایی تشکیل شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/persiana_Soccer/25552" target="_blank">📅 23:08 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25551">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">📊
🔵
عملکرد مهدی تیکدری ستاره جدید سرخ‌ها در باشگاه گل‌گهر سیرجان:  ۱۳۰ بازی، ۱۵ گل، ۷ پاس‌گل
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/persiana_Soccer/25551" target="_blank">📅 22:49 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25550">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GP9VVbBkx-rFjbAwESiLHmm2PtNAl1UJrjYrFWWRyeFa_1SfluVsrAPEAuwwTxsqkLPcFtktRmjpI-aC6d0FuUwiGlKxnx19qQkkZVIrS9P2_yDkoqx5oxn3sqtgUAdA7-y9tP21IFXwvAH9dhQ4unhTv6ObWJypLkUtwFagBurdrFCeuL1y7xSFWNezL6Ymc9d9v5SpbRa2DEkyID1u9riUDUWniMpVZ3cu8KaMgpfUJYBsrLkObnhssmiK1MGpfFX02NLfQU3URAJ1G5v1LPsLx3XZTKhRGv2uIeri91jB10-tzG_t6L-0io5BEKaj_es_74bEaV29W-DMUyWPfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی‌_پرشیانا #فوری؛ برخلاف اخبارمنتشره‌رسانه‌ها؛ طبق‌پیگیری‌های رسانه پرشیانا از مدیربرنامه‌های یاسر آسانی؛ ستاره آلبانیایی آبی‌ها مشکلی برای ادامه حضور در این تیم نداره و فصل اینده با شماره 7 استقلال به میدان خواهد رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/persiana_Soccer/25550" target="_blank">📅 22:24 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25549">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fu5ai3V-NXiQ3DUxdCQDTPMi-B7QzA5GiO4nUGtYoOiJ7CwcBSWVMXLR3JlVKa-IZCMbfDalHWOYeim-EQP5zW_26v6n8YZdudJRXbWozB26mIScS2Jngo6rG5OzzyixoNu-ZjFYeVPD5XVzc5rQBxg8AuyYGUKHLuWFK6CjW6m1MGrWxBZroLkPk6N23QeNrapwIK3i6Y6rQBw_xB_t2YsAVoGLVjy3b2K5FsyVOEnvCW7oxwHEk_uTK6380j38nIyV9JGl6q99wBQ51jEEQKHUTJgpMEVN57ZZWyJllHPG4_IEHI09IUfEr5uHWL5n3G7z7jlu27vYVX5uXWiByw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه پرسپولیس ساعتی‌ قبل با پرداخت 700 هزار دلار به باشگاه‌روبین‌کازان؛ کسری طاهری رو باعقد قراردادی یک‌ ساله قرضی همراه با بند خرید قطعی به ارزش 500هزار دلار دیگر به خدمت گرفت. بخش رسانه ای باشگاه بزودی پوستر طاهری رو منتشر…</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/persiana_Soccer/25549" target="_blank">📅 21:51 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25548">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pfD-FvGdc7KuBykd-fFXj60v-5Ei7lttpgpdTHGrbDqhsqRtgtEJdqupnK0R0ahhMs6kt18EUiocnL8_XVm_dmfRltYXhUZoXEYrYsx3lrp0fV11Bf4zmIsFre47m5nr2ymWbEXwviUdGgy16-EgxtVcijsbzdFpbdT3gPRXVToN8S04tpcnyI9g-uyi13XeC_SOetEgxPOJA4IeBtYg7vvxjeMYhJuKCvCGyB_FOwJBUgyrxhtucMVeMOIPmkCK5fX_QNhGbd8wfHMptQLckZSYAGNk5ksuwUFp30MGLE0Tddux5x60Yt8VLlUEEGys9aBm99eSPJQACB_2Pmtiig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇳🇱
فرانکی دی‌یونگ و همسرش که در تعطیلات بسر میبرند از چلسی پیشنهاد رسمی دریافت کرده. ژابی آلونسو درخواست جذب این بازیکن رو داده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/persiana_Soccer/25548" target="_blank">📅 21:41 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25547">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ROSfb8TzjmxrcgEVvg3p4innSQgYNZglWDg0BjyJc6MmIeOXMZKj-2rV1LkqlmxXYMY-OFhlGHlVGFVSQhgBMroIT3AmgjGR5luhs3mzN9AttzK617Fi_i-a_tX2koAwpUPGIhZCusRDW3W4VWl84DjjNQsfi2q7NS2utWMQnEP4rg8_ZqeEwQmAridD8uRPUKby7NLi-4qpbL_0xydukkIQ6iFsLWlf5JMalToACe6zN-pvecS2uJLKggEDgKrSGb_CbsbEcEuRh9GUOOHyHZy9FGH6OweF40Wx6DFOVGdz1a3ZQqUn41GamgBkZK6quiEkd1B9djJQqC16nK_Rgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه‌جزئیات‌ عملکرد لئو مسی فوق‌ستاره تیم ملی آرژانتین در رقابت‌های 2 دوره اخیر جام جهانی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/persiana_Soccer/25547" target="_blank">📅 21:36 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25546">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B1YRQG2FkIxRs0A8uM7K0WPBwGYnihXivtREEAlmnEMt0Rzleyxx1JsbekvjUMM3g1D_fPgP1ZmPeN4JGBnL8VFpTw6v8DEhWD6WHv-LIukVF2IIyTj2-2AN_aRqDyj7fuDuPHZ2aoEskq7c5rnZdFkOgh4yANUBXO8vJ-v6v4WE0yWab-WnBs6MfHe5Xi-6Yyr7FSRNm9OsVUJeOcmDvJW2W6LJy655fbjnYsOjTAG0pljYUwqzcjURnww97p6-vy-2XAGyUUXhn4ctT_arBgd9aN0ncaQpNNiQGiX6veHIJ7zky0zWQb52KuvIMFkjJjs0lsCpK1IighuGWAVjmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
اینفانتینو میخواد فشار بیاره تا جام جهانی ۲۰۳۰ با ۶۴ تیم برگزار شه. و ارژانتین و پاراگوئه و اروگوئه هم یک بازی به شکل افتخاری میزبان باشن. مشخص نیست فقط برای یک جام میخواد این کارو بکنه ولی ظاهرا عزم راسخی داره که این پروژه سنگین رو در سال ۲۰۳۰ انجام بده. جام‌جهانی ۲۰۳۰ با میزبانی سه کشور پرتغال اسپانیا و مراکش قراره برگزار شه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/persiana_Soccer/25546" target="_blank">📅 21:36 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25545">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KXNEgaKKyDACKqU4tgkpG5YzcTBeB4dPVeH8x5BDvF_Q6tzqF1wso8Oj9vOIK2LOcA1ZSqAeLatov0UrVK1LYXM6s_NydzEwTj9LwlIZC_q9e2Kp8hBs8jDjWNBKWDH3hBBnbsRzWQ4o7fcoosDS8y9Z9bAkKMJCku5gndgUQs3FUv5ureXroPTSr6OetmBfaceJ2Ptswr7k6eKG8YC4hNQ9gA02_ghEiWit-AqnnMv48NUSV8YwdEgJ62KIPXnUfYBCb3mC81wiQTX_5dbhIb_FHl3IWsIVqUMDzworR-IHSfgVuF1qZXNdwanK6hnA4UFtXLv_HLqL5S8av7B_Tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🆚
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇫🇷
🆚
🇪🇸
🏅
تکرار فینال دوره قبل یا شگفتی در راه هست؟
🔥
🏆
اسپانیا و فرانسه از یک سمت و آرژانتین و انگلستان از سوی دیگری برای رسیدن به افتخار حضور در فینال جام جهانی ۲۰۲۶ با هم مبارزه میکنند.
👀
⚡️
آیا این بار هم یاران مسی و امباپه در فینال بهم میرسند یا مسیر فینال متفاوت خواهد بود؟
🚀
بتگرام در تمام مسابقات جام جهانی ۲۰۲۶ همراه شماست؛
با پوشش کامل بازی‌ها، آپشن‌های متنوع و هیجان لحظه‌به‌لحظه رقابت‌ها.
👉
🌐
🚀
betegram.com/affiliates?btag=3_l7
🔥
⚽</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/persiana_Soccer/25545" target="_blank">📅 21:36 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25544">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9d86d8e16.mp4?token=FXbRifL0KOPWq5uHkEHy-8OFFDTpY4u0UPZZgmx3fCzcUYwGJ2WVT_zCsPtiRxF3to-_lAFlJupS80ak_XwBYakL010KJ-iq4OXN7Zwrn9_W74hmmLjJESruQETaGqt09s8q53qY_kUplG4QBstfP4hN49q_kqnrECrNv1SqIagBqDDyAmsehbTwWXePbgB6S-8oDQi4W9Qrs6nxbSL4VlFRy3-mSwS9TWSEhHBIhYtTSQSWGeDsUg7qqhClfmf4fXjhQwfjje6JB2fbbUU430NVSnYeGvP54wkNLcDWu_y4xoB2D_HrVijC6fOAWpQsha-KCUATyUO3uZCj0_ao0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9d86d8e16.mp4?token=FXbRifL0KOPWq5uHkEHy-8OFFDTpY4u0UPZZgmx3fCzcUYwGJ2WVT_zCsPtiRxF3to-_lAFlJupS80ak_XwBYakL010KJ-iq4OXN7Zwrn9_W74hmmLjJESruQETaGqt09s8q53qY_kUplG4QBstfP4hN49q_kqnrECrNv1SqIagBqDDyAmsehbTwWXePbgB6S-8oDQi4W9Qrs6nxbSL4VlFRy3-mSwS9TWSEhHBIhYtTSQSWGeDsUg7qqhClfmf4fXjhQwfjje6JB2fbbUU430NVSnYeGvP54wkNLcDWu_y4xoB2D_HrVijC6fOAWpQsha-KCUATyUO3uZCj0_ao0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
برنامه‌دیدارهای‌بامداد‌فردا؛از نبرد انگلیس مقابل وایکینگ‌ها تا جدال مسی و یارانش با سوئیس
🔥
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/persiana_Soccer/25544" target="_blank">📅 21:08 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25543">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aY2FGKQBNHpJtxLsMxLq5N_D5mc7yhgOCexPviESN0L5wZ7h568TXZPn5OefyXglZRtmBmPrQlOzFKdeWgvqHuBj80PkvuECVAVhXoxfucWq_uCRvxK4DVz6iHuEWBBZ1daJZfr-6OpXwfmNphgiljyLke0AQzBCgvR_4_TpbGIWCgkXorMy430eIj2eYyJnfdjwtq3j6MyRdvN75C2roHGfMhGjZPCq0t_gwC231tavb-jB-rnQO-kvND6u5TvZ19ZvHTMQs31UEK0Swi4tWbKcc75dKb_rmCdyPwaopX-CxG9OfKVo45JM7kxh4MrSikXdGIEil7rwC1UyNqpgTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طوری‌که سورلوث در بازی با انگلیس؛ نروژی‌ هارو به فنا داد؛ وایکینگ فن‌ها عکس رو میفهمن. برگ‌های هالند از خودخواهی سورلوث ریخت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/persiana_Soccer/25543" target="_blank">📅 20:46 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25542">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jlta18X9RDKHdT5ctvHdXHZJeYtW1mCawL4hLOjuDMo9LApgJ4k5gLa84SeBnniJ9I-lN8s_D9klpmH_va1ER2us0oGdGDhLOxNdD_0eISvqduxgftTuMRhZxRcUcbeMuVmM8wtDIlWLdyz_cHnZVCi3mEyxBKBXYKjd7lmPHY24eTy-sP0ivYXHe1e3UEz10Sysl9XjJ2puRxa9lRorR7WeI_LNKgH-asqqyYATz8B9HB7ccDDWc0vlTbB_65gqCc6pYayqLIt2UFtrHzrGJrq4WSZv-Q9GvbKhGdhDJWsDZT7pfaV2OPyGFmArX0WRQwxdZaj_JtA0ivg4CeeHSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دو انتقال مهم امروز؛
آرسنال 20 میلیون یورو گرفت‌و لئاندرو تروسارد روبه‌بشیکتاش‌داد و مارکوس لئوناردو ستاره الهلال هم رفت آژاکس؛ هلندی‌ها بابت این انتقال 17.5 میلیون یورو به الهلالی‌ها دادند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/persiana_Soccer/25542" target="_blank">📅 20:29 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25541">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/104d086276.mp4?token=JLoAyFFCLKXF6R5VT_H7rVSTEVq1IlFpLoCoN59_AGL1LdBgZkqralzYqGqvRpNZ1kJmCMaQfoEzMaRy1u8mX_KcjH_FeYVKmb0u7Hj3CCjRgZCDbzffa2fcBRm0w8sRXVj87vT-XgHo8yv4MaixFMpji5ktMeBimJocaBN_4GlhQEB7I5bdfv8yB42Zpp1hgoHGv7bjgpfEVgxZ8RhJXtv0PBEV7DTL43iGW0dsab7AGQUMaVbxLRF1cl9ErJ9TT8z_rZ--f5W_iV_6KPqzta3wI9mnZ86yUYi866OvpPCy-0-bUfRqS88mGU9HoKDGuIe4JftEo-pOH4ymx4R7Uw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/104d086276.mp4?token=JLoAyFFCLKXF6R5VT_H7rVSTEVq1IlFpLoCoN59_AGL1LdBgZkqralzYqGqvRpNZ1kJmCMaQfoEzMaRy1u8mX_KcjH_FeYVKmb0u7Hj3CCjRgZCDbzffa2fcBRm0w8sRXVj87vT-XgHo8yv4MaixFMpji5ktMeBimJocaBN_4GlhQEB7I5bdfv8yB42Zpp1hgoHGv7bjgpfEVgxZ8RhJXtv0PBEV7DTL43iGW0dsab7AGQUMaVbxLRF1cl9ErJ9TT8z_rZ--f5W_iV_6KPqzta3wI9mnZ86yUYi866OvpPCy-0-bUfRqS88mGU9HoKDGuIe4JftEo-pOH4ymx4R7Uw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
کنایه جواد خیابانی به قلعه نویی و کادرفنی تیم ملی به‌دلیل‌عملکرد ضعیف در جام جهانی: فکر کردی منم عین مربیای تیم‌ملی‌ام که 180 میلیارد بگیرم؟
‼️
هومن‌افاضلی‌خیلی‌جدی‌داره میگه فکر میکردیم که میتونیم تا فینال جام جهانی 2026 پیش بریم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/persiana_Soccer/25541" target="_blank">📅 20:15 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25539">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c2qRFCsvvmoXcPcpaOteUXJB0Q86EKl_YlbmeYtyuzQJsWu97wxWzFRnE6KeclpDNEFzrJDMRUlU82eXvi7Jjc2jDSRp748RqKSLWz20jcDs61OQXEwO7hOcbAqZhdVwbXQ381Vu4FrjBFTLejA1OYrK7yceK7KKXdoD0Y7d7bpAUzHNBBzK2PHP3hCX0TA13FE9AUGobxhS4J6t7EnkhBTNi9zO1oUIqcBBXqEGxvENbQ-X2GLNcjYIrSuVguWwf3FTZV8IOSUIdmGMxRyZsHUIffIHIhHZG9apIkP8TogATGOK2eIS5zUqOaqacXDHAo_fXXVxlb7j1J1i6BmiZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
#تکمیلی؛ مهدی‌ترابی درزمستان‌برای تمدید قرار دادش با تراکتور به توافق رسید اما هرگز قراردادش درسازمان‌لیگ‌ثبت‌نشد و با اتمام قرارداد دو ساله‌اش باتراکتور در حال حاضر بازیکن آزاد بشمار می‌آید و هیچ مشکلی برای عقدقرارداد با پرسپولیس ندارند.
‼️
باشگاه‌پرسپولیس…</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/persiana_Soccer/25539" target="_blank">📅 19:58 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25538">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OmHK0Nv7Ar_sqCUtuG_HRUv3m15unE4eR_WEV5g7n0uIfnA-sDTKa6WHlNsx_h9i9q14YFS5UEExjZIBddGeE_Pl_j7QzIThpn5r7JRi3D1Lre-X2mhXc4x4yGjb2kIjA-C_QCIQ964k930p17jaD9MEbE2DjxwmuXqxROOsmJ0shmsAyjA0-alvQZJ07uV1gyXV2P0Ar6Vak4D6Ar6QciLHG4tJ9waVdzO9mZC7tHXnBTO00Uswo4JSLgVORZkc8RPLcol6CSqCyWdHBQogKlDQPSRjkGuqCQTzB6VNcPIvTXLq_YSmDuQI_4TpggPiH2CZcSNNWVScqttQlkV4nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حسینی در سپاهان موندنی شد.</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/persiana_Soccer/25538" target="_blank">📅 19:26 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25537">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QT8lysGTSIcySF5T6-moibako0eIPYYtwpqzqet3cdYaa2vsy2jSXd1Qy2b1W6nu8e1RxEmjBLkM4z03OTKHhV5E0yjt5X9Tpvy_Pkd39VvueivwqYCAy23e_4DVSaQ9PFXBYMwBwoST2fGlJ_x02KTI4-Q3JKGtes8xJtEtC7c5612f7bALddACDLvs3Ei-UvKgYvylBbGG2QTmF1-pUo8OBzG4_VYe1Y0oJdCzph3giM43Nl2iWurdlFb3xrkC5gV_hzK3pG5F5j70UTfhFdj0hSSI94DD11ecL91xVcLAiZc-nL2LGD5DDf3dVtKV2ErkufsM-Xfd1ylirzMR9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ امیررضا رفیعی سنگربان24ساله‌پرسپولیس مذاکرات‌خود را با باشگاه تراکتور آغاز کرده تا درصورت توافق‌نهایی بین طرفین با عقد قراردادی سه ساله راهی این تیم شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/persiana_Soccer/25537" target="_blank">📅 19:23 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25536">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/146af45fcc.mp4?token=BlNTkQsQs-M7BMVSqdtSnsr8uVIWOqJTom4bHGu1nx_XjpFyeO3lMEMq_U7IY8TCZvjFWs0mqa7XbCTJwNxdI_0AFyFAL6LfSeTCBwWoewDhkZqmHXNDho0eeqerL92q8yNz9_Vjx5CYcSezG13W4RX53Fzy08Zc-fV7yk_4SI-SeVISyBWNXMknzgkDuJpIujA-9CuG27_NTd3mzfP725L9Hp5US0e0zO0xOi-_IB2jqYU7MvaVjJzl0eznh5RWoPA9MT_jyEIDOjx6s2GF1SGC6_Cbwvp_69T2_WlIwxpvoaC-hMSTBLFpioVfWXptq7INoaAVwM-xBZHA4FNcwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/146af45fcc.mp4?token=BlNTkQsQs-M7BMVSqdtSnsr8uVIWOqJTom4bHGu1nx_XjpFyeO3lMEMq_U7IY8TCZvjFWs0mqa7XbCTJwNxdI_0AFyFAL6LfSeTCBwWoewDhkZqmHXNDho0eeqerL92q8yNz9_Vjx5CYcSezG13W4RX53Fzy08Zc-fV7yk_4SI-SeVISyBWNXMknzgkDuJpIujA-9CuG27_NTd3mzfP725L9Hp5US0e0zO0xOi-_IB2jqYU7MvaVjJzl0eznh5RWoPA9MT_jyEIDOjx6s2GF1SGC6_Cbwvp_69T2_WlIwxpvoaC-hMSTBLFpioVfWXptq7INoaAVwM-xBZHA4FNcwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
بلینگهام ستاره انگلیس در پایان دیدار با نروژ:
مادرم یه هفته‌کامل بهم میگفت مراقب زبونت باش، نه فحش بده، نه به‌داور گیر بده که کارت زرد نگیری. آخرش هم مثل همیشه حرف مادرم اجرا شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/persiana_Soccer/25536" target="_blank">📅 19:18 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25534">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pHVBM1Osdcs32c4gYd1_TwttiU6nhkWtAYJQXR2Tam3TbXnVrQpT7ulbaSuhewIEBYKtYShD4cmUX7HTjM2Gl-fZ0pSePrr-Uy_StuPWecrilG2FDR9AMEyMJ3r2V0Ix0KLehRFYZYt7N0Bxg1NgweRN7d_dECKbHA-sGC2ZuTwly0lkYNXcPLFmRI7tuso0nJ0L_Aj2uBVry2c6ELY107sJtMpq--Bx0dVpIXHCeG5gjYtCEydIPc-mOWokGdiorjzjwi8V0HzZtpqELgJZWYDS91rwnvAe4mMikQ-lKodgjn0DJWXrXOX3EwgUZxLiV1biAyAmqI5xUFDXgPc62Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اوسمار ویرا سرمربی‌سابق‌پرسپولیس در انتخابی عجیب با عقد قراردادی بعنوان سرمربی جدید به دوا یونایتدبنتن انتخاب‌شد. تیم‌یونایتد بنتن فصل گذشته درلیگ 18 تیمی اندونزی‌رتبه 7ام راکسب کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/persiana_Soccer/25534" target="_blank">📅 19:00 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25533">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Iyi03NHvRJKZWB8-FK86aXpbipTzw2obiaQerUYCwKWF_PT4sw4072m0MDWEWT150XK31QLz2s7YeiOn4uys3_QllsWU2cGkFelUw0X3pz0QIxay0F9D5a3z5mPrSK4XGXyT5_Dv7scMrVRMiCKkXTyyQIdp50ks76EXkCYI9QwI4KF9R0O0mNXxpuOOb0R7Ws7bWlAc-2OeXcZq_NU6U6CBtBSC39zr6unzb5LhQ9hgUXGeYtKpR0hcLbMhfHtn_Xoz4O2t8zmqXlVNXnZ-s5_eIBxHaxNUnCYF-Tx-rzn_JRFPQNqma5u6vVvxR786VWPYzJrt3M1z77Gtxkf29A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
برترین گلر های فعلی فوتبال جهان که بیشترین فالور رو دراینستاگرام‌دارند؛وزینیا بادرخشش در تنها یک بازی‌مقابل‌اسپانیانزدیک 16 میلیون فالور گرفت.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/persiana_Soccer/25533" target="_blank">📅 18:52 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25531">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nm4dKF9netNceUd1VQonlbmfyjr-FE8titpYNJ3BPLMOQlHxh043OXgcEZNnso8szDnNS92X4NbQ3X-26w2JH69VQiLNIpgRfZSJxFAfjz07nyDMt9Q8kVe0lYZx99E2bs7zsW5k5D57F3iTX9r3WQb_EoozphQ3kO4Ar0kgjj3EdL4GuRyBxRzAz6wjKyuQWbYaMGt6zP8v-seUHRujnBJgSlgDfchR26QEB2MdAY84lu3YGEvLQZ0NP50jrAYKC2iBIqS2aV5DEFlYcRa1UjlJ0NkcoVw3q5cCVfiY2oYUkEkNl1lIbMmUKbQuBD8frCtpNXoTrkAY-aD_pmG19A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ec951e804.mp4?token=sqrRDSudeuhmXjY9ZIvXPAGWlr_JAYczpXmhgMWgi0kehHwZVzQbUaQgCiORt8sBV_ll9cDjur0hPh4EGxxgbs7ium4msfBGwTZn29HUaL1eJyEIzcLeCSRtF92gB6EIOTh8uodaIpx60kjygbyNVYoS_KUqZ62auRn_WVUVlf-ywRoykoJeefxnosoQ7_nXLeoJRfSNtZPj3DIp0ImbaAB7rJySyScrzFxQ9XQ-f0INmcLxLmGbT-iaQ7MLS4WKoXT-FfKn6XTHoDoTxoBOOq1x8siwQ3Y4VtIMabob7fR6gh2EiOLaWrE8DS51Zi8yFwtcEtIeiJD6OCTCT1aPcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ec951e804.mp4?token=sqrRDSudeuhmXjY9ZIvXPAGWlr_JAYczpXmhgMWgi0kehHwZVzQbUaQgCiORt8sBV_ll9cDjur0hPh4EGxxgbs7ium4msfBGwTZn29HUaL1eJyEIzcLeCSRtF92gB6EIOTh8uodaIpx60kjygbyNVYoS_KUqZ62auRn_WVUVlf-ywRoykoJeefxnosoQ7_nXLeoJRfSNtZPj3DIp0ImbaAB7rJySyScrzFxQ9XQ-f0INmcLxLmGbT-iaQ7MLS4WKoXT-FfKn6XTHoDoTxoBOOq1x8siwQ3Y4VtIMabob7fR6gh2EiOLaWrE8DS51Zi8yFwtcEtIeiJD6OCTCT1aPcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
🇦🇷
آرژانتین‌نخستین تیمی‌درتاریخ جام‌جهانی شد که بدون مواجهه با هیچ تیمی که در رتبه ده تیم برتر فیفا قرار داشته باشد، به نیمه‌نهایی صعود کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/25531" target="_blank">📅 18:44 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25530">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f2121b6e4e.mp4?token=hXTGJqEWJ4CmsAnXhFr30iXXUfqRXqVNzZTaiO747OOAVydX7PtpIvtJm8ft8o_nV7Fs4Jj3fQynLUsX3xDVMobqs3nbh0dM7gV-hFn4IWhI9hutV-b8AVA0Of2CD-CNGl7AGAYJavoCDLhrYctgpexwqmTqv7SGVto92ekdFzaAS2RTjBk0tC5yEz1NtmNv0dss5rQ1kW1Z30DrstzBJ2oEwprYPcnJEguZpgDMBkUAKuSkNZjozK2-7qigXhR_Tfg-Bb-NXQBA1GaR44t_346ZLcp8ZHegLTp-X6ayPFGN7pg-bs77RAlJzgkk0B3UDfY0tPgxZA9nHdZhGpXquQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f2121b6e4e.mp4?token=hXTGJqEWJ4CmsAnXhFr30iXXUfqRXqVNzZTaiO747OOAVydX7PtpIvtJm8ft8o_nV7Fs4Jj3fQynLUsX3xDVMobqs3nbh0dM7gV-hFn4IWhI9hutV-b8AVA0Of2CD-CNGl7AGAYJavoCDLhrYctgpexwqmTqv7SGVto92ekdFzaAS2RTjBk0tC5yEz1NtmNv0dss5rQ1kW1Z30DrstzBJ2oEwprYPcnJEguZpgDMBkUAKuSkNZjozK2-7qigXhR_Tfg-Bb-NXQBA1GaR44t_346ZLcp8ZHegLTp-X6ayPFGN7pg-bs77RAlJzgkk0B3UDfY0tPgxZA9nHdZhGpXquQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مسی تو نیمه اول با پینیرو داور پرتغالی بحثش شد دیشب: بامن‌درست‌صحبت‌کن، بی احترامی نکن. من باتومحترمانه‌صحبت‌میکنم تو هم باید همینکارو بکنی. انگار نمیدونی‌چجوری باید بابقیه حرف بزنی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/persiana_Soccer/25530" target="_blank">📅 18:32 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25529">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a0b0e1c0d.mp4?token=mr2IuP2M0p3UJttxJr5Q0vB1qUfZebylnA-BuiIBhJJk5GbAulX81006LP_K3G2_15RAaYLldK27cKLCH-NaGiQjmUFeZX4hJUVA0QTajclOQ9h2CofH1K-LvASm5vCxBV8C6nd9tMccs5P1gqRFRKz1e4wu_i37iFFFEjfwyc_kmicRiQGYP5oQlDNNkDMalklzGO7XziLuroHXESno5UefK_IUb6bS4UTWZ3iURbU_MuYHNZkdHFwhrkR6JHj1RDhxthnpknOjBhn9GbEAJ04LWSiMqvFFX24xRXAP5USsicKr57lmOf1mtsnOeGTypH5ETS6Lmuf-alqwG6zgIzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a0b0e1c0d.mp4?token=mr2IuP2M0p3UJttxJr5Q0vB1qUfZebylnA-BuiIBhJJk5GbAulX81006LP_K3G2_15RAaYLldK27cKLCH-NaGiQjmUFeZX4hJUVA0QTajclOQ9h2CofH1K-LvASm5vCxBV8C6nd9tMccs5P1gqRFRKz1e4wu_i37iFFFEjfwyc_kmicRiQGYP5oQlDNNkDMalklzGO7XziLuroHXESno5UefK_IUb6bS4UTWZ3iURbU_MuYHNZkdHFwhrkR6JHj1RDhxthnpknOjBhn9GbEAJ04LWSiMqvFFX24xRXAP5USsicKr57lmOf1mtsnOeGTypH5ETS6Lmuf-alqwG6zgIzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
ویدیوزیبا از لحظاتی فان و با مزه لامین یامال و داداش کوچیکش که این روزها سوژه رسانه‌‌ها شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/persiana_Soccer/25529" target="_blank">📅 18:17 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25528">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uPoD2Tq8mNs9nAZlbr9UNWNJAIqSGuJXrWTNk_Zu18Yhu9YMaOdbnH7kNkqW7c2k024jKqT_KJRBRTVF3LDYNrmKzcEfARX3xd1mzeNHH6WEtWf2cJ9NoaS_soFIEe0rdVk1075AWxs9DmlWYqTA9FuaUmB_soqFKXjZrMWY6e5Bf_dtLGp4Izbqecfqzyf6fvDKViUQ_SeccpHYYfK1bpc5i5o4-X3YMG6L1gPt2maibCea4irKVmIkTm27npgkp0naeN_gZdQryEjkWj7DOWYXNA6ufarMhXZK1pa-WiAccIJJC_aMgxhPwanDg-xTA52x4ifXtm4wn_nIkJfKaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🟡
👤
طبق‌‌اخباردریافتی‌ پرشیانا از اصفهان؛
مدیریت‌ تیم سپاهان‌ با‌ حسین ابرقویی مدافع میانی 29 ساله باشگاه پرسپولیس مذاکرات مثبتی داشته و درصورتیکه حسین‌ابرقویی بتونه رضایت‌نامه اش رو از سرخپوشان بگیره راهی اصفهان خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/persiana_Soccer/25528" target="_blank">📅 18:00 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25527">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">‼️
تو یکی‌از خانوادهای‌عشایری یه دختر بچه حالش بد میشه، بعدمیبرنش‌بیمارستان تست میگیرن میبینن باردار شده؛ میپرسن کار کیه!؟ میگه پسرعموم، دعوا میشه بین خانوادهاشون؛ برادر دختره که بازم زیر سن قانونی بوده میزنه پسر عموش‌رو میکشه، میبرنشون دادگاه خانواده عموش…</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/persiana_Soccer/25527" target="_blank">📅 17:57 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25526">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UZQumKjx26UpqqAOTYbfEpRrljlXPfesSi_6u0FN8efem4n7tiWGVTsyjb_64pb7tmzvxvSFbTEVgslZpd7OQ4nHes-Ji-_H2nilTVFLHrLsA8p-ZPXlWcnWTgoryQH9RJ2Z_KsKSGxng2RyJ2xm1MFdbHaP2UBBB_3Rp_XTqdBk1ev7rgIEru-a7gKXbp3ApAyxeIPCDF8KoSj2ciQGJUh6mILmEHCuxBvMDJ9ja-nvJpfckG4FJ3kyvja-K9zmBn-hsd1FeLBvo8sLruBiXinz3VNToOsQZ-dI-cKIvtNSwUjqhUARaON13ob0NLGhNG_0tNIJT928USBKTh1cCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تقویم
؛ پنج‌سال‌پیش درچنین‌روزایی؛
مدیریت باشگاه استقلال تهران هفته‌ای یک الی دو بار از سجاد شهباززاده مهاجم جدید خود رونمایی میکرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/persiana_Soccer/25526" target="_blank">📅 17:45 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25525">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dmAHBY5sCU8uBAqN538y_CH5Up0j0uNrulI0dnlK03greAV1Y89HhPaNDBisucl9YPLlkH8_L-PE4BmV1uFCOi_6f6_b0QigEhufJGKl9jEOaa3Yyh-XsIS8EACmxhpqEmyKJo7ZiBFt1M9od-2pLbMV_5iYHRekYFVwRxQTwMurnmiMmnoxAGPYAJZLUCWjDRnzBqv5ZcI6GfUxgRTg2FmQ2lWN29nmNZpm2Q6wBs0ptG5TcmJakirjah7vnJJUkcSMbs2CoNF2gd0YiyWX5ST12StOnSp1ssHY6xu7ekHzxOtgcZ_hFCDcW3d49uomzAqskvTyktI1RewWe7RcRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇦🇷
آرژانتین‌نخستین تیمی‌درتاریخ جام‌جهانی شد که بدون مواجهه با هیچ تیمی که در رتبه ده تیم برتر فیفا قرار داشته باشد، به نیمه‌نهایی صعود کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/25525" target="_blank">📅 17:24 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25524">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dqOZU71ORilO7d2VasL5btJ1pauFafUYnvUQLJk2Q12KtmD7MF4T96qs-3JeiYMPTFLIqY3o-eZT3q3orEZLcZO0Y0860fAS5-jialIX5gRaXfstRDmFv3IhcePuA28Il20aIbIX_OkDfl7yh-oNGs7mmMT9oY2FwucBXWhLfVQSuyu75vOVut265YTcEA9Dg3AYsW4UETmaQV4YmFiuph7RTmTib5eAjU2i5GF3jDO_E7JiAgv1cHSiX0VFHtSbpGEHYtPhYWMzn_eFIFHCZorYyJzfa24FeW6wkqfj-8dtdZyvNOWZKs7U6MPUqchr-N4O4stu6InLcDkLag8Rsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
عارف حاجی‌عیدی هافبک‌جنگنده سپاهان که مدنطر مهدی‌تارتار و پرسپولیس بود بامخالفت شدید محرم نوید کیا در جمع طلایی پوشان ماندنی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/persiana_Soccer/25524" target="_blank">📅 17:11 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25523">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df9c9cac2a.mp4?token=D0a5folWIUZNOM5ZUgJwBUcrvEfUQo-3k2Kh2kStte3n895AhmUMD31TKKZUcrNJOZ5Unym16ClJN_aaJXaQXC6cqI7mV8Rm22PIhgIq9Efaz-kHGPs0EbRooDvPn6hWHtOmZLHK7y0s8h4eXDWKr5OAkFhBqKoZ6n5hasoCUR1iruk7evwOH6cEpkEigg2AJRVQrjDY2oYDsw1L_-iKO2bFM6H67WjzNzH2KZj_MzRhYV-_xyERmz4oELjJtNWPcH2kk5rmCrt8IERkFl0ZYuYrfl78QyatNu6Jld4cNHd3vuecppiuT5Zu3ZRLAg3sIw385YVkLsIC3m28X_4sZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df9c9cac2a.mp4?token=D0a5folWIUZNOM5ZUgJwBUcrvEfUQo-3k2Kh2kStte3n895AhmUMD31TKKZUcrNJOZ5Unym16ClJN_aaJXaQXC6cqI7mV8Rm22PIhgIq9Efaz-kHGPs0EbRooDvPn6hWHtOmZLHK7y0s8h4eXDWKr5OAkFhBqKoZ6n5hasoCUR1iruk7evwOH6cEpkEigg2AJRVQrjDY2oYDsw1L_-iKO2bFM6H67WjzNzH2KZj_MzRhYV-_xyERmz4oELjJtNWPcH2kk5rmCrt8IERkFl0ZYuYrfl78QyatNu6Jld4cNHd3vuecppiuT5Zu3ZRLAg3sIw385YVkLsIC3m28X_4sZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
هومن‌افاضلی‌از کادرفنی تیم قلعه‌نویی:
شجاع پاهاش پرانتز برعکسه اگه پرانتزی بود پاهاش اون گل‌هم افساید نمیشد ما میرفتیم مرحله بعد:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/persiana_Soccer/25523" target="_blank">📅 17:02 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25522">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5608c7ac3c.mp4?token=oBuYJHdFlRMGumMPQU89r8LLdug22zIBasq6Xnkz7iHqrLXPRO5yWlOJK2E55065D1e2x55FZVbVuh9bvkgsForuezMyJVy25s_RqH2KwOua43BrJEx7XXR_2HQvjh4NV7LT4PQ_ta2MOkhjfp-K1EJZybSPqkgHtl4UaJ4MeLat2D3zzqWYzTmkNnKLKM53jINIQa3HQ_UIGtXba2Cd9hp6vhpNSN3AHYAPJIsOw-QqGgOg53WgqJ0TidRNOiRAjLSjmyuSnS19yS298x_5kVF2Vv0-ngaEvqFsiX6mPEi-GkR25Ax76bjSo3Nq9vhfBM3Ka13nvMAUkzhy4h32vg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5608c7ac3c.mp4?token=oBuYJHdFlRMGumMPQU89r8LLdug22zIBasq6Xnkz7iHqrLXPRO5yWlOJK2E55065D1e2x55FZVbVuh9bvkgsForuezMyJVy25s_RqH2KwOua43BrJEx7XXR_2HQvjh4NV7LT4PQ_ta2MOkhjfp-K1EJZybSPqkgHtl4UaJ4MeLat2D3zzqWYzTmkNnKLKM53jINIQa3HQ_UIGtXba2Cd9hp6vhpNSN3AHYAPJIsOw-QqGgOg53WgqJ0TidRNOiRAjLSjmyuSnS19yS298x_5kVF2Vv0-ngaEvqFsiX6mPEi-GkR25Ax76bjSo3Nq9vhfBM3Ka13nvMAUkzhy4h32vg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
🎙
عادل فردوسی پور
: آقای اژدهایی، خبرنگار صداوسیما وقتی‌صدتا موشک‌خوردیم و صدنفر آدم کشته شده ‌میاد میگه که همه چیز عادی است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/persiana_Soccer/25522" target="_blank">📅 17:02 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25521">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4009214e91.mp4?token=E88X_iDvQLL0u9NC-JDM05S83JqK5LM0aOA0b10zkzRCy36Auj-JQl_LchpHtsM9t-9iSxgb2WpCd8LhenhuyXpKqm7cmCqmlLY1Aots0HzIkLyNLzcc4D1G8cWOsUC7FBKL6vdpSTOHVUSUQ3-PCikAYFjIfYh7Df9PpkcTxRtUFb3KuNkSHCRTyytKGPpeeIZhK5FTuTvTMKv867vxF8rjJQ6u8qMDB7LufjO-0TjpQvnmWOHPpF-4rrczo2Wf7a7wpJnPh4AdIrt-3Ps1YBnRTM0O4jm8K4qwIhGfYgaaPga7ojLsHQRIMhjDI1aBfI3_1BECLldZ1YF1Dnj7SA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4009214e91.mp4?token=E88X_iDvQLL0u9NC-JDM05S83JqK5LM0aOA0b10zkzRCy36Auj-JQl_LchpHtsM9t-9iSxgb2WpCd8LhenhuyXpKqm7cmCqmlLY1Aots0HzIkLyNLzcc4D1G8cWOsUC7FBKL6vdpSTOHVUSUQ3-PCikAYFjIfYh7Df9PpkcTxRtUFb3KuNkSHCRTyytKGPpeeIZhK5FTuTvTMKv867vxF8rjJQ6u8qMDB7LufjO-0TjpQvnmWOHPpF-4rrczo2Wf7a7wpJnPh4AdIrt-3Ps1YBnRTM0O4jm8K4qwIhGfYgaaPga7ojLsHQRIMhjDI1aBfI3_1BECLldZ1YF1Dnj7SA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
بازی های جذاااب
جام جهانی فوتبال
رو با آپشن های تخصصی در
MelBe
t پیشبینی کنید!
⚽️
🔥
💵
امکان شارژ
کارت بکارت
و
هات ووچر
🎁
قرعه کشی و آفر های جذاب با جوایز ویژه
🌐
دانلود مستقیم اپلیکیشن اندروید
🤝
اسپانسر رسمی جام جهانی
🇮🇷
پشتیبانی از زبان فارسی
✍️
حرفه‌ای‌مطمئن و درکلاس‌جهانی پیشبینی کنید!
برای‌ورود بسایت‌فیلترشکن خود را خاموش کنید!
▶️
‌
Link
🔜
MelBet1.net
▶️
‌
Link
🔜
MelBet1.net</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/persiana_Soccer/25521" target="_blank">📅 17:02 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25520">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56ef9dd527.mp4?token=M3gfPj0qur9j9R_4fVk4FF_RUlKj29xInrNnYqUN7GT7soVoy2h_-d1Saoto57WqFFFqKLaA_2RRxHMErJtoD9bR8A8YghQhGhgFs8X9XT6gvbAxg_894Ew8s1GT827LRdk0CpjoqBTBybF-NiRaNKWSeCBZDwbFm7BPRGI2ioTAvy4fvPq9nIYRv9An6OkwPCQY5w6hdCO_d5E2wpMDTu8gbaSxRLM2Bn7Bwwgsce_XhBVDPatCJrpS8IgvsK5NhsGKC1XXEKdx6vNsmKVF2SOCNt1LWNyNnmdznbe6TXLYwmtQPAQQzHf4d7ESRTqQ8tLYyavp_vtISgbcTErkew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56ef9dd527.mp4?token=M3gfPj0qur9j9R_4fVk4FF_RUlKj29xInrNnYqUN7GT7soVoy2h_-d1Saoto57WqFFFqKLaA_2RRxHMErJtoD9bR8A8YghQhGhgFs8X9XT6gvbAxg_894Ew8s1GT827LRdk0CpjoqBTBybF-NiRaNKWSeCBZDwbFm7BPRGI2ioTAvy4fvPq9nIYRv9An6OkwPCQY5w6hdCO_d5E2wpMDTu8gbaSxRLM2Bn7Bwwgsce_XhBVDPatCJrpS8IgvsK5NhsGKC1XXEKdx6vNsmKVF2SOCNt1LWNyNnmdznbe6TXLYwmtQPAQQzHf4d7ESRTqQ8tLYyavp_vtISgbcTErkew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇳🇴
شوخی‌جودبلینگهام‌ و ارلینگ‌هالند در حاشیه دیدار شب گذشته انگلیس
🆚
نروژ در جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/persiana_Soccer/25520" target="_blank">📅 16:45 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25519">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oq51a8ytesgIiIJzIduduT4jmc7R1tFrDq2evNI8pz8T1eh89SU0y8DVeYbKe7FStUO11h9IC1GxvsAOl4MO5sT2i6XjxK0TGarYArozHWX9jjSRnwVPcC_XnVAQPrDzunafvSNu395YH1u-Gr9LDhL9MyUSa4jYNjxExlFtZyxg6zA4FJ9hqw5Jg5V2vhl06QjyKeO7qrP7FMG8wrpstrIeFYB740oZsL8pxbVDPkWrjf76QmCtGUcPk7fcWkkqukG9U5abbpNnNHQ9ddQeGgHcmLUpFim4lDOeuex0_BRjxrxiqQu78GHcIaRCOg4Srr5eIueaA0Ejp3ZtsaxRqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
عملکرد کلی کریس رونالدو، لیونل مسی، کیلیان امباپه و هری کین در تاریخ رقابت‌های جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/25519" target="_blank">📅 16:31 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25518">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lEzz7l1TrbKJBSz4ksbS-iBaAUaqLETpx8ZrZEw42SanaaxNH1au8eMIR5VSO6IxM9s5BrD0IB-WpPIb-5QwcdqGSGq_5AXFrZQKVc6nl5k2osX_e2Spr8GlWDtqkMHhKtR3VkWDvwhJdLnQ05AyTdOCq6_967qyx5XF2HT7YtCPFeZXZM_kjGMAjpIO8fyKNSeWpgiG9_3ZmVe_bMjF71oXJB2kqw00VzOENqyZlnPYTBTZLXQEbQMU9hbOQodaISC5Ii0lnck_AbTSa-h-eR4l5jxsNKLbO0wvij04HFgeSIStj2X7VidxvGnZkMp-WH4OklQ3ojuSKv3qk6kAbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
هایلایتی از دو تقابل جذاب بامداد امروز مرحله یک‌چهارم‌نهایی رقابت های جام جهانی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/persiana_Soccer/25518" target="_blank">📅 15:59 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25517">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HR-Ya7jPtEVUDY_6o7KAptaCbjNhVifM2rkX__-HBGjI_sk2sAzjZxBapvG9_lKJdQYfaSaThkEh1_5RXInbifakPw10nx-yYCSCuEcBnQIX4phN5a61f-Yq2pCjQbJN6KsKGaoY8gvUW7k7aWteJkNhcgOr-LcpYRu8q8AecHr0ePN7w5Deu0W0lp8xNh0SBm3pzgCBnKDlx46E5DMhplmOnYuxaNWbwTZQ6VPyXPY8HFVHMDG2FmdSS_Z-zjSe58KYUuhx5cLdHDH39PauFpUZbDOH3dOPfanJOvEcTnkQ4SDSWBot8XDVwj9vhc-iayeD5HlwOJ1HrJgHFOXnGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
محسن خلیلی معاون ورزشی پرسپولیس؛ بعنوان سرپرست مدیر فنی سرخپوشان انتخاب شد. نهادهای ذیربط مجوز افشین پیروانی رو صادر نکردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/persiana_Soccer/25517" target="_blank">📅 15:29 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25515">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🏆
یک چهارم نهایی جام جهانی 2026؛ صعود شیرین سه شیرها به نیمه نهایی جام با درخشش و دبل جود بلنیگهام؛ یاران هالند از جام کنار رفتند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/persiana_Soccer/25515" target="_blank">📅 15:12 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25514">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NsYI-he_HZoYeeak7KKBSfQWjzVGvOabKA-ZMEw8qXY1aJAzaC-8bayX0Zj0HCoFmWlchXS4UPix7zh968aeTOPZA4U8lqrlFxDstR2VFUEEwXKLprsy6dzSLeJwCxwrcINCEnNyJT_rbNQXnzYs54-VsHCPSvcdHZeOrMVGka1UV9mbST7XQOQqZ6-xkRtciYVuckM8mZJQr9uP0ZwFIjzUy_4ftrc6hTAKCRBfpI7Nh_4lSBOX7i5PNs1itbGJMte1waRAESKPM21gnSqn2COeag2avJdGE0rHdppEBD8dEZSJWHTgULFwMwzXgmcQ8dShJ7Pa5Uey0kZNuuWZZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
🔴
#اختصاصی_پرشیانا
#فوری
؛
یکی از بازیکنان فصل قبل پرسپولیس از دست مدیریت این باشگاه بشدت دلخور است و به دوستان نزدیک خود گفته اگر پنجره استقلال باز میبود تا حالا قراردادش رو با آبی‌پوشان امضا کرده بود و یاغی شده بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/persiana_Soccer/25514" target="_blank">📅 14:49 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25513">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LNA74_BlTYnPRhvcMgVIPMQCvNpThdZAf7ZnVEp67Y0pcobcgDGYbVJ8P2IqMtKBxY26ZL3WizwbTFWM-u1MDpJCIyNBcvVERdZG33nGjnCqwHwOS_l97JdobBzrt9b2E1B9RyWd_0LeM0f1GfECAdUOZ8Yg00vOyP8Im-YxFVF4DBhD_Pl38IAkTW2J1QSKtzl9UcSTivdaro4vCqUov040grY9jECmgEUFZvD5KWd7NkjRN24szLKEJJR19V4kYWTXRKbLVqtIG3elUxTVLf3zal247P0BOeh-tYtmc9boU9BYjNR_MnDiJetmfXFBgCrFZF-ZqMOLsjQN-wYyyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
عملکرد کلی کریس رونالدو، لیونل مسی، کیلیان امباپه و هری کین در تاریخ رقابت‌های جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/persiana_Soccer/25513" target="_blank">📅 14:28 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25512">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60fb9d0fb5.mp4?token=LUG1NxYtvEHyyWgy_UKYuf29IN3A1me36OQB9RgPZMu2toNamTqSMNRdfDa_--iJD4lUv2gVLY3I9KBzti05UBl2OaH6f87S-GmofO6gwvAnSWqBJ6yG7T5BST7Uq6l7R4HYPqvsrZdnmIuou_2Jj0tAefIZ2Uh6aobgQAbwqVzXsueO9YJhhlpLNFRTrTvsXnc4YVHEkOvR0jDFeoINg4VVjl4_vMPC3f7MLH9mrkb60URzKsIdVkn9LI1CEThSMGAnU9Qry9a5B_LqYTPqbFZMWfb5lVt_67lwjhVNoAp3jUX9SrAYhr6Cilgq0DTOPm1E-CpQNPfER67Be2Wf90WukaMP1x9M3vn5m-k2JW9ocsevjS9s2zV0NWZcvNVYkMw7Z-7NGfpuxsinQCf3zj1ZJYgAC-KQ0QMlRhweb3diKOltg6GkFLxfSySJL51VNrWVSjIMlUDRnoR57EAJx2UH0fTC83w-dOVVl_5pDbv397CAJ8x956Lg4XaiaPVpm6RV3GGBkKH7y4eO1G5mUesPbpwO3yvzhAdgMKjmwkxqFy-C_9SGYdHqgBt-scUYAZd49vwUKYoB781rwDSQSigRJ3dViwu46prx0PgQuvWm6vUjC3aQcozaS04VfyfK7dlPiIq7RzeVBoeCqitufrNtz6Z9GarIQNkVzf_GF50" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60fb9d0fb5.mp4?token=LUG1NxYtvEHyyWgy_UKYuf29IN3A1me36OQB9RgPZMu2toNamTqSMNRdfDa_--iJD4lUv2gVLY3I9KBzti05UBl2OaH6f87S-GmofO6gwvAnSWqBJ6yG7T5BST7Uq6l7R4HYPqvsrZdnmIuou_2Jj0tAefIZ2Uh6aobgQAbwqVzXsueO9YJhhlpLNFRTrTvsXnc4YVHEkOvR0jDFeoINg4VVjl4_vMPC3f7MLH9mrkb60URzKsIdVkn9LI1CEThSMGAnU9Qry9a5B_LqYTPqbFZMWfb5lVt_67lwjhVNoAp3jUX9SrAYhr6Cilgq0DTOPm1E-CpQNPfER67Be2Wf90WukaMP1x9M3vn5m-k2JW9ocsevjS9s2zV0NWZcvNVYkMw7Z-7NGfpuxsinQCf3zj1ZJYgAC-KQ0QMlRhweb3diKOltg6GkFLxfSySJL51VNrWVSjIMlUDRnoR57EAJx2UH0fTC83w-dOVVl_5pDbv397CAJ8x956Lg4XaiaPVpm6RV3GGBkKH7y4eO1G5mUesPbpwO3yvzhAdgMKjmwkxqFy-C_9SGYdHqgBt-scUYAZd49vwUKYoB781rwDSQSigRJ3dViwu46prx0PgQuvWm6vUjC3aQcozaS04VfyfK7dlPiIq7RzeVBoeCqitufrNtz6Z9GarIQNkVzf_GF50" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
اگه ایران میزبان رقابت های جام جهانی 2026 بود؛ این مسابقات جذاب چطوری برگزار میشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/persiana_Soccer/25512" target="_blank">📅 14:04 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25511">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PAHdq9quo-_6jGw4WedUNWRyR8G3dQpUS_Xbt63VQjf6h2K7PaqY379xY_lbaZ9qNO2zm6tPJjL_UqYaQH5uT0LyyxPTdzVyzMWbAwcRTWezFGUEQF7g6GmUJbTIpO7dKIrYtAWLnIfhXaaojvD3uF9Bmkq7vZlhw73cAAk_5rfdpOMDz3LTTP7Rxa9OE0Reg18FDuGS-aFPkJY9PFamNvi5SdGtoQBsYvmr4aNYteTw6icJmkO93D0qH-rkUs6xBSnZvBdOHXorkWn8k0HEsiW43LQ7oDyfUQhe5EimOurvQqAnIydAuCTpjYmVJT3CjWR_4-HcAcgtnfu-T6F7ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
با اعلام مدیربرنامه‌های علی نعمتی؛ این مدافع ملی‌پوش باباشگاه‌لوسیل‌قطر درحال انجام مذاکرات نهایی است تادرصورت‌توافق با این باشگاه قراردادی دو ساله به ارزش 850 هزار دلار امضا کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/persiana_Soccer/25511" target="_blank">📅 13:55 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25510">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C0hbrOyyFhtvSZrK4MPG-1VhumcdKM0_uDbfgYp_KBkmZkkaeNDerXlxHSDAAqiKli9P5NQdzZyaJs-nHBwrAalxHP5DJK_WyopWYivacGBCkWAPGkDMVAEd-OsQhyHLjh61NNRZdEsQQIatMWaKqmi39HWAUG-yG-bv8aBdTDXj0cNo8c65pvLrjqTqP6Vnf5k1jey2h4wHFXtSep2FY0N2VgKcLUezQT-9hE39Rh4M9miR5EBNEW-AyyTbdO8PiC9KUbo4S6Rtd8-Ql7-FD4o14Mg-wsFzVhUtHAqqWno6y98i6Mu-FxglPztMgxtc2tVn1KxRIo-YxysJmY7B0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی‌پرشیانا #فوری؛ آخرین پیغام منیر الحدادی به مدیران باشگاه استقلال: وضعیت منطقه آرام باشد این هفته به ایران باز خواهم گشت امادرغیر اینصورت باتوجه به شرایط خاص همسر و به‌دنیا اومدن فرزندم نمیتونم باهاتون کار کنم و ازای فسخ قراردادم مبلغی برای شما واریز…</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/persiana_Soccer/25510" target="_blank">📅 13:31 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25509">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qtyvOHam_oc6d5M0y-r9qRZD_u1NbXS_EvYv8Ie0JRb3wZ9n2ncsgF3M2yoZc04ccHReUbV-nZPt9Ldurc6ZZRmf2zuU3N49Wyu9GxR5KkIs_0lF5qtqYpXNhynpp2f3wcNP5D1H6XBgeDvgqVyybJ3xdZ_0HVYz8D3JezDA19yU-Wr2qQjjdmWdfwEu_Wh2kNSIMfi1aCixISs3R60c6iL42q9vTxnBrQcsNUInKIaCyrF7QaFqfyYjewQxnOR1MZxyBJhEybonuR2d7CNUlSAemTVAEsVUzSXG7ag0wZTrTUZaNF7BKskca4EWBy-kSay479z0Ad7XZr9UoOBEDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق‌اخباردریافتی‌پرشیانا؛ مهدی تاررتار نام سه مهاجم خارجی رو به مدیریت پرسپولیس داده تا شرایط جذب یکی از آن‌ها رو فراهم کنند. بزودی اطلاعات دقیق‌تری درباره این سه مهاجم میگیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/persiana_Soccer/25509" target="_blank">📅 13:14 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25508">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ljcpmLVMBCpURTi1FOpjiyT0brUXMkmz2CzIC94xK6xHxvJ8QI17jC-wWzjSfBGptg92D5OKCJdHbpb3upKqc7IzJY0crqDJZS1J450XUnISCvpvNEmoSo-0QDVQZG9V7e-KUWuS3o55-GnN45vIngRkNrTCqHHng3xmlSLkhe9CqLt4ybLyB3m0ExlUvXG-h4cFelPPR1wD2YryYxQ9kUioUIuygjpOGXACtyAWpMwKeeafl7ZHvIvcUEI-y-qaWeyxbFtkrej4_kPv71BDdXiOE07bXZFtopRg4CroDwZBbaGm8b86eTT9rpUk4osGH0woSWsMPXbev4VysnJdgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک چهارم نهایی جام جهانی؛ صعود سخت و نفس گیر یاران‌لئو مسی به‌نیمه‌نهایی با برتری مقابل سوئیس10نفره؛آلبی‌سلسته‌حریف سه شیرها شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/persiana_Soccer/25508" target="_blank">📅 12:40 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25507">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uShXrWPatlPshEUahMDRfSuTJWJRNhwp-Suc2AOEQIFRPP4SbHAdsiG63heSoyW0sHoWQT9_u0qI3-Mesb2tQhu5gIHEnO8qXrLOoTmN9eNv_Lwo18H0_pCfuCt9NCMtcViNbgcX0rtni5jbZwasfcv09n5BCUMGBm9kta7SAWQBW4eRDPxZ6BtNdLWcm54zPFwcaAKkrSIRv8jiuHQC9RYxizwSVysh2JqPrcPm4UeG4nJIrSBhZzszyb8Wj9l5eIii7kwaXLCSHf2uYn_OXpC5uH75Av3HeTJwLIWAQvQITllDQA49FMA5FOnrwHeDLkO7B_6MhR2AUTChig1Acw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
عادل خان فردوسی‌پور پیرو خبر دو روز پیش پرشیانا؛ مهدی ترابی برای عقد قراردادی دو ساله با مدیریت باشگاه پرسپولیس به توافق کامل رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/persiana_Soccer/25507" target="_blank">📅 12:24 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25506">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g6pirnEhanEAfdU1fFgMrlDSrHTWqVc9_8CX53tnuyVivvqxBNwVT59aRqjAxaQ3z1nNDHZv_q6gqS4DHE4E925jLKZv2EPdYWXGjaXa9z16Ekk2bviYc67MKKkEMaWlzEyCqPqR7yGjShx_Ca-t1Aeudy5vkljMhhjnGsAA2hw-6c9yExYQIIa91AJT9AJHwyvklPzk1N6K-0c6UmIGICYbC1QXlooidCx8602rrpoO7LAl5xwUzdZ82EHmh16xv-Dd2mHY3Ga778z-k7BacvvDz3ACqSdyFVFiuEkAdRxjPdfaz4JDU0Qbwe7tIdZQux4cqg7svitn8QYZ8vWS7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی‌پرشیانا
#فوری
؛
سهراب‌بختیاری زاده سرمربی‌تیم‌استقلال روی جلال‌الدین ماشاریپوف نظر مثبت‌داره و به مدیریت‌آبی‌ها اعلام کرده قرارداد این ستاره 30 ساله‌ازبکستانی رو دوساله تمدید کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/persiana_Soccer/25506" target="_blank">📅 11:49 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25505">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c5482437b.mp4?token=PhkA9i8UizDC-8NbUWXeCzJb_cwiw9UFwTtDTw_RXtGYoZ9NGcbJuvYqY5u3S_AYFoT2fKyMmwfWp8w6cYmWc7IhiXNkcC2dlBteW9WOwmM4zfaTnHjMsuMleatoPuebvBw-kNjy02HfgxD0H-i9jlLAFSYp_eFp3gS3nt45nYfkSdoiw3lrLRD6WIw5NqFgOmgRIBY-yB3PVO_kZObvaYi9aPYMwM_u9538z52rA4kWTc1-ULxc29ag9wQlDm1DJg34pLVW0dmHHjBVJ1VnHRM8g9btZ6xCalYyAseIpBjXusLVEzhXQxpn-G5mEJGyTYZx7wOMG1o7yavm7ed77w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c5482437b.mp4?token=PhkA9i8UizDC-8NbUWXeCzJb_cwiw9UFwTtDTw_RXtGYoZ9NGcbJuvYqY5u3S_AYFoT2fKyMmwfWp8w6cYmWc7IhiXNkcC2dlBteW9WOwmM4zfaTnHjMsuMleatoPuebvBw-kNjy02HfgxD0H-i9jlLAFSYp_eFp3gS3nt45nYfkSdoiw3lrLRD6WIw5NqFgOmgRIBY-yB3PVO_kZObvaYi9aPYMwM_u9538z52rA4kWTc1-ULxc29ag9wQlDm1DJg34pLVW0dmHHjBVJ1VnHRM8g9btZ6xCalYyAseIpBjXusLVEzhXQxpn-G5mEJGyTYZx7wOMG1o7yavm7ed77w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
🇫🇷
تلفظ‌نام‌مدافع راست فرانسوی بارسا در بازی شب گذشته فرانسه مقابل مراکش توسط عادل.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/persiana_Soccer/25505" target="_blank">📅 11:32 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25504">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JcVN-yk3MRXVHX8Z0OzlepcGh6JTCZ-rMFyuoYwxuO6d5n_JZoscxBAu6HKhoVftI5vpx6jl396OtQmqgWjBNd4cbFDSLKDOmstOyPO-sI75BfQYQ89Ma9KkxjFsBnKP6beQ-cOawLa5oB2AU5Pf-uvhneoEARNnyRNdoncM0b2dhTeSUvxLqPDLh9Bgz28tMMancQ7rxkhh4cF08k46Hs7Qfira_y5eGBAtnzG3cgjP6w7B2zilkLMMZ3ZwDZDPulyNKpfzLPHWMfXNr3Otg9_DvE-_eIvmAx6EC1QDp3iCqPRSVEiroKSFuRi9MGwz-32rtZCEJpLPw0rqe7Lchg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی #اختصاصی‌پرشیانا؛ جلسه مدیر عامل پرسپولیس با مهدی ترابی در منزل این بازیکن برگزار شد و دقایقی‌قبل به اتمام رسید. مهدی ترابی برای عقد قرار داد 2+1 ساله با باشگاه پرسپولیس به توافق کامل رسید و به پیمان حدادی اعلام کرده درصورتیکه تا هفته آینده مشکل…</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/persiana_Soccer/25504" target="_blank">📅 11:15 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25503">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EPYGKX8Wj64_QpomE0S-6UhDGjuQFHl8fqwfDzDZQQ4AuaaU3PNHW_J_kofn2Shg5m6p55kVvIyvI9rti7KIfLsdZmXPzF-8lVAMPcj3-3MbrERgVqX20ENoHLBL_CjO40NJQ4t_uWjd5ul25E5osyPvpXhJq2_jZQTIyDHkM5fcI53nSC8nlurGAt6B8nUEw0OJHvW7jGP9GIZZgn_2XRh7F_1zcmWFMvpdpLKmBMpvOroRu_wRLIb9pn_idhrLNO7X1UbzF544D-KMj-psd1U2QbAUwhF9kWW6mwhc2Uk4EqBhIYpfnBxDAgWG6JH-TgTOP0zx8DWCFJ73N59JMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
امید ابراهیمی هافبک 39 ساله سابق استقلال با عقد قراردادی یک ساله به تیم لوسیل قطر پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/persiana_Soccer/25503" target="_blank">📅 11:08 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25502">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a0f9a7afc.mp4?token=FTBRngTroRW0mFIZ3-TR-YuI1FzFBH2ELOJ0mJoVdVy1UJxaOAHfuVPBNGCtVJiKM3cPpMSWOaXLeRd-M69fEeTrc-SXSxcGYViRUFtBaxuYB9uKZRg0XXNP2O3FtE_1bMutUky8JdhL0U4Dv_LkuN5Y2wO-m01PdszOmcUO052HJNjvcXV4x8EmTcuFMxSZ1194N5G402Xh1m_BXpbNzKzo0rJ-8jADvZapVg4kMO-mFP6RG0jvv0MHylWHv6s4iRIIVG_hMl48rnEfQMXnlkWww1cTiCC5r7jbkq6kjbICo211Fe_w0LCgFVVyMTFjfGLzm6gmU5hPHt3Xuz3fMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a0f9a7afc.mp4?token=FTBRngTroRW0mFIZ3-TR-YuI1FzFBH2ELOJ0mJoVdVy1UJxaOAHfuVPBNGCtVJiKM3cPpMSWOaXLeRd-M69fEeTrc-SXSxcGYViRUFtBaxuYB9uKZRg0XXNP2O3FtE_1bMutUky8JdhL0U4Dv_LkuN5Y2wO-m01PdszOmcUO052HJNjvcXV4x8EmTcuFMxSZ1194N5G402Xh1m_BXpbNzKzo0rJ-8jADvZapVg4kMO-mFP6RG0jvv0MHylWHv6s4iRIIVG_hMl48rnEfQMXnlkWww1cTiCC5r7jbkq6kjbICo211Fe_w0LCgFVVyMTFjfGLzm6gmU5hPHt3Xuz3fMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇳🇴
نروژفراموش‌نشدنی‌ترین‌تیم‌جام‌جهانی۲۰۲۶ بود. جسارت‌وجنگندگی‌کم‌نظیری‌داشتن و شدیدا دل‌همه فوتبال‌ دوستان رو بردن. به قول یه بنده‌ خدایی اگه ایتالیا مدل گتوزو تو اون گروه اول میشد جای اینا میومد احتمالا این مراحل رو به چشم نمیدید. من خودم بشدت فن ایتالیام ولی خب مدل اسپالتی و گتوزو افتضاح بود ولی مانچینی درستش میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/persiana_Soccer/25502" target="_blank">📅 10:57 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25500">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sOCY2WOCEA4wPVflN9XnAiCBBM1pAVMPKIOg7p9bnUlUIk6coBgGBb0tOMFB8Y6y5deXUPnhWPCA1ojstSz0OabrFG1-khoYxy0eztJwtpzqbbh6krMrEVbeL4p_DZeHukl6JcPNt9fRgnC10AeMaDn4yHNn-E5sj4rcGjOmZFrPyTgC2DOBJX92Ce5uyFMF0EjE7uIrVw0xzvvYpx8ZNeanzcvVxa7JvTu9YPJ0ITjVtk04ElsTLPJgigxHPYhNmOUk-HTLkluXqgNrBkUr8KZVvsYL9pmrVgb_Bi_jh0PxvSVctuFbJ1I51Chd0xyJA0We_vzG4f-fREKeOEaBdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4928773d8.mp4?token=aqCkc2l8M3yfhz1N-UNYXZfW0oCYUaljf6nF8LdX61xG-ODAShVIcICYHxmn95VeqeevGbqNe44Ew2TrXjrhyNDGHyzOXubAXxTlAnraCFXLQfL_LhXDmfB-sd2BvKokpkgTOt1KHGkS_P9jCbESd0xdC3-HBdz82q5ou7_O8rpNAW5uMjwM5CQa1_QAIhhH6etB4lOhjr8RjqOpOFxOBe15AH0_M1apWQjTgeL7YUba8ZDu4drZvfEFjwPogDhmojuXlq5PguGATb0yYM_hRzjf93-AZclm4KlXUsGowbCRDHfH2xBtIhuwmab0Y-qSU9mNkZiqB8mm-iQfUF3rew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4928773d8.mp4?token=aqCkc2l8M3yfhz1N-UNYXZfW0oCYUaljf6nF8LdX61xG-ODAShVIcICYHxmn95VeqeevGbqNe44Ew2TrXjrhyNDGHyzOXubAXxTlAnraCFXLQfL_LhXDmfB-sd2BvKokpkgTOt1KHGkS_P9jCbESd0xdC3-HBdz82q5ou7_O8rpNAW5uMjwM5CQa1_QAIhhH6etB4lOhjr8RjqOpOFxOBe15AH0_M1apWQjTgeL7YUba8ZDu4drZvfEFjwPogDhmojuXlq5PguGATb0yYM_hRzjf93-AZclm4KlXUsGowbCRDHfH2xBtIhuwmab0Y-qSU9mNkZiqB8mm-iQfUF3rew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
یک چهارم نهایی جام جهانی 2026؛ صعود شیرین سه شیرها به نیمه نهایی جام با درخشش و دبل جود بلنیگهام؛ یاران هالند از جام کنار رفتند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/persiana_Soccer/25500" target="_blank">📅 10:49 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25499">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sx4duabIAyLPv_DYKeLnSYbCGrGW3MandhfwXaDVZ31_Hc230CNvA7Yc_5Nui_dwj8X1IcufZ6M14lum583bSLldrLj8eUn-VnV7WiWgrOcgfeeBS5UEgsHVh0pxWnpDa_h2n3OW9GYnMQi5zZOHMbltrfUUcn4k_loGTWIJEFrIc7hKuLVAWvU0P0qH6ukVFIqC32BZ48ZTh1P5siIaiJd32SxNVOS1YlMsxWNjrBWQwtVvTGRrTFcUEByEgNQUyTzfgsfpRF6ScVfCd3j_c1u5JvAT1IYkyo-ERQnykmRLqn9jPyRYyyfBZ6kb2KdeQOdfJv6-DKM168NIT7Cy0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#فکت؛ازوقتی‌توخل‌به‌‌یارانش‌اجازه‌داده بازیکنان انگلیس دراردوی تیم‌ملی‌میتونن با پارتنراشون رابطه داشته‌باشند جود‌بلینگهام یه تنه این‌تیم رو به مراحل بعدی جام برده. انگلیس دیشب با دبل بلینگهام برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/persiana_Soccer/25499" target="_blank">📅 10:29 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25498">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/inEr6OYmkJVMcd1WK4putGBCUpKSmVROBc3YsR9Sw4AgDQUlqUbymPG6umBh15WWCVwO9fpm4lBQhZWqERREAvw-86ZBOox4kTSxTWkMkN_mEWCk-8Nq5zce-JLdWEJLN7eu_0GRGrpXaQVMNr4Apm7WduXre6grcCGxk9PjBe1cx0at8Xd4KGhoUyRIHw0wVp36oq3-i8jdVL1tRkoAAw5L85DY7MDe8kSJKm7dBUexO1W-m5Wm14I4aM21nakqeHS38JfDPizEv0ik2l7yOIpY0y9jeZsAl151dbJesZCYnIO2X_QemJ2UV3NmfVYtxsuQuVDOYlzA2gZauzZ5cA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی #اختصاصی_پرشیانا؛ جلسه مدیران دوتیم‌پرسپولیس‌ونساجی‌دقایقی‌قبل به اتمام رسید؛ نساجی‌رقم‌رضایت‌نامه رو550 هزار دلار اعلام کرده که حدادی‌امروز درجلسه‌به مدیرعامل‌باشگاه نساجی گفته تا400 هزار دلار حاضر است به باشگاه نساجی پرداخت کنه. قرار شده که ایری…</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/persiana_Soccer/25498" target="_blank">📅 10:16 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25497">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dda5f52119.mp4?token=tIDJEPhD6xfoh4D7bh9Jkg-C2bDcxCMUAybbYDFrRHnGL8ODoIxaRqY43M7bwBTIZKx-qQMC6pTyHUzgsoCojkqZeE4TiNPDJJg3aPevtljVCziBHjKB3hskQnef3LS7iFF2yUmYBHmnkm2Ah0NyH-UkAgcUCpY8-sdiH3BK9fMJRdi0S8OeCAo6-XdAlu10ILRgl4ELGIqI94Jj1LZ8Eu7kIfJhGcY7xnbZwLTB2e8Wb38DbbccgSZhXUwjKxAVIdYDnNpvnOJsgasVWQVZWpPjcBIT-tf2nOKHcY5D9FdGQ5lYMuJSHiQIt_XvJ10vhXOFrRz9ipGARsTlxbX9aw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dda5f52119.mp4?token=tIDJEPhD6xfoh4D7bh9Jkg-C2bDcxCMUAybbYDFrRHnGL8ODoIxaRqY43M7bwBTIZKx-qQMC6pTyHUzgsoCojkqZeE4TiNPDJJg3aPevtljVCziBHjKB3hskQnef3LS7iFF2yUmYBHmnkm2Ah0NyH-UkAgcUCpY8-sdiH3BK9fMJRdi0S8OeCAo6-XdAlu10ILRgl4ELGIqI94Jj1LZ8Eu7kIfJhGcY7xnbZwLTB2e8Wb38DbbccgSZhXUwjKxAVIdYDnNpvnOJsgasVWQVZWpPjcBIT-tf2nOKHcY5D9FdGQ5lYMuJSHiQIt_XvJ10vhXOFrRz9ipGARsTlxbX9aw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇧🇷
وینیسیوس‌جونیور ستاره‌برزیلی رئال مادرید امروز 26 ساله شد. او تا کنون موفق به زدن 128 گل برای کهکشانی‌ها شده و همچنین برای تمدید قرارداد بااین تیم با فلورنتینو پرز به توافق کامل رسیده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/persiana_Soccer/25497" target="_blank">📅 10:15 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25496">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nhk0-b_xbBU9cOYMNTyf586GkcbmwqO6h7Kj_r--USkZjrYtHwxxblKOBPHBI2wMPWv_8CwLH23qnPkgkxdVZbDV5VJDSC3GjbGha7BwZSqDVZOpDgoGt5EkvkbUyIIjVF7CNgH3mrLpvySiAQnrJZOCJEinTdzUvkEuO-G2_9WsyD-Y7QJFUnXweEBczbMhVhEheSbq_KBMTJqjREAAG8fOVAOz6roMlat9Cd23-24WmNmtdGzcWTTn_N8SCYhzW5_YhkeHNY-0dhfLZ0K2z5yTyqqNRnVSjVFh_S6ZwNgA272B-0mLa_INUh4fIYcB4QLIQjB1-mIDTbKqv1PuTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💰
5️⃣
میلیون‌ریال‌فری بت ویژه ی فینال ویمبلدون
🎲
بدون ریسک در وینرو پیشبینی کنید و از تماشای تنیس لذت ببرید
🎁
🎾
فینال تنیس ویمبلدون
🎾
🎾
زوروف
🇩🇪
✖️
🇮🇹
سینر
⏰
امروز ساعت 18:40
🚨
ورزشگاه سنتر کورت
🎲
با وینرو همیشه راهی برای برد پیدا میکنی
🔊
🎲
سایت وینرو
بابیش‌از 400 گزینه متنوع برای پیش‌بینی
📊
ضرایب ویژه و رقابتی
🎲
ثبت نام آسان و سریع کلیک کنید
🎲
✅
🛍
پیش‌بینی به ضرایب بالا
✅
🤩
🤩
🤩
🤩
بونوس اولین واریز
✅
🤩
🤩
🤩
بونوس واریز کریپتو
✅
تا
🤩
🤩
🤩
🤩
بونوس روی برگه‌های ترکیبی
✅
پخش زنده‌ی تمام مسابقات
کلیک کنید
🎰
✅
درگاه اختصاصی برای کاربران
💰
🔊
اپلیکیشن حرفه ای
📱
🔊
همین الان وارد شو و فرصت را از دست نده!
📩
Winro.io
معتبرترین سایت ایران
🎲
🎲
🎲
🎲
🎲
📱
کانال اخبار و هدایــا
🌟
sr21
📩
@winro_io</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/persiana_Soccer/25496" target="_blank">📅 10:15 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25495">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e63b6abc08.mp4?token=Wf92bIiD4brKsdfABJnky1FOHVxXSg-JUegGltrH8Ti85FYIp7DD4n-wPGrZLbg608tdz7DsZP0y39CNU_eRJ_ojpW27IVLclfqfdirbVvoqw7GQOB9RTzCCJuMyIa92FJV7yiq2VY31EJ2USO--tplZ3mTJKfaa5xFw4m_4Uc4MaqydCdLPeB-_zXJUMFj0fjqwej5Vd0rUWrXCZ90HCiKrjHzu2bFzIeyZ-NBSIjhK0zUq12FJTGumOi3mUTS0Rn5KgiX1VcRPHGgfOmPxUj2nKrjcPJXKx7UvFBBHo4JuVChkuASUzr_M80Trh2wTf6aWYPScw0Zd1p7ilpxzBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e63b6abc08.mp4?token=Wf92bIiD4brKsdfABJnky1FOHVxXSg-JUegGltrH8Ti85FYIp7DD4n-wPGrZLbg608tdz7DsZP0y39CNU_eRJ_ojpW27IVLclfqfdirbVvoqw7GQOB9RTzCCJuMyIa92FJV7yiq2VY31EJ2USO--tplZ3mTJKfaa5xFw4m_4Uc4MaqydCdLPeB-_zXJUMFj0fjqwej5Vd0rUWrXCZ90HCiKrjHzu2bFzIeyZ-NBSIjhK0zUq12FJTGumOi3mUTS0Rn5KgiX1VcRPHGgfOmPxUj2nKrjcPJXKx7UvFBBHo4JuVChkuASUzr_M80Trh2wTf6aWYPScw0Zd1p7ilpxzBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
یک چهارم نهایی جام جهانی؛ صعود سخت و نفس گیر یاران‌لئو مسی به‌نیمه‌نهایی با برتری مقابل سوئیس10نفره؛آلبی‌سلسته‌حریف سه شیرها شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/persiana_Soccer/25495" target="_blank">📅 09:42 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25494">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tkaUhHZqDiDUbm-Mji354xLm2hyN0GXryCzNKUBCaay8AXnRzXYKIgBv7mCFrGOj7khn2X2jZhWJIH5P4PEv73yyqZgt7dluhpjIrcL0ON0fJuZfXiwXQyaktEQnPkDPyqEKjoyaTWB6YA6-6F_aL-aOV8shHuhXgm6mgLFToNOseRZgGfmi4hYAe4vwrThQx_DyWxHOwKJLwURylV6Qer_W7Y7MM4CKhylYjgx-5oNmQbyY1NSnbJ1740ijJPmBy1Ab_6gdIiYHdK8bvZ4V_WcPqkNYO00jZg9SXzqewZ72rfgBodYEUMi5i_A1T5uoj8GR6bIGiy17JZDJLHfCSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#فکت؛ازوقتی‌توخل‌به‌‌یارانش‌اجازه‌داده بازیکنان انگلیس دراردوی تیم‌ملی‌میتونن با پارتنراشون رابطه داشته‌باشند جود‌بلینگهام یه تنه این‌تیم رو به مراحل بعدی جام برده. انگلیس دیشب با دبل بلینگهام برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/persiana_Soccer/25494" target="_blank">📅 09:23 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25493">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fNQAOAgfwDgtLqmYIPjJ6SsJGeRgxP_JJs34EZ2fD518VVU4ZtwkUd_zeEtJse_SRanj90FvZFq5ns_yxzeYZqmrJLXBelRlrrgJgPW13d9OEMMANmjcu6j5qzAefDR-dp8KLN8I5T9rVRswVSc3Vwv4NyS0nU-Jlcdc7fLc030JnygUmvkWeS1Dr77cBPEjwIKhSgPMZNDrqRlzL-KMHqVX1WpmCFpro5G8ayPWHgkk2Q-W9awhIJjmCvrNbUZb-n_A4M-5bBB7zBB5WTePtJ3V0QmPRye1I_KD0I5B4gBtGsO4oWezAe8NoBf0afR3k7Ac-6z7MZW3QUpgpsOyMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق‌اخباردریافتی‌رسانه‌پرشیانا
؛ فرزین معامله گری مدافع چپ پرسپولیس بعد از تمدید قراردادش باسرخپوشان راهی سربازی شد و در فصل آینده در یکی از دو تیم فجر یا ملوان بازی خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/persiana_Soccer/25493" target="_blank">📅 09:19 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25492">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b0c6aec402.mp4?token=Rcz7Y5GTG4hCEYBPYpAEGtheKW__yqWedtH9UV3SHVSU5f9S3VQL6v89QSZqv-vN3l5AMtaV9aNLz8Y5Br9yWj1cqgz-yHfsyHhBQ8YiTGGX5QA22nnDaoEQI2fP6lZ4wzuiel138pCi4WQ-qgUHaGvrnij2Et3pEWGXoIt5-mDUjBc_MoMfNGukaNVBwYLehbronW5B4wnOFNuKO_fCsYnUmxt2rQ1-_BM7XBPY_3syt9sD_XQMxh87TH6c4wpqVmZY0-PTRPA3hCAfuZxX3LI1xrZmDCUvjbUiZwFug8EcirTEVYNJDWLqhx1R9No5rLdlIRox0xRojDH3bOLInA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b0c6aec402.mp4?token=Rcz7Y5GTG4hCEYBPYpAEGtheKW__yqWedtH9UV3SHVSU5f9S3VQL6v89QSZqv-vN3l5AMtaV9aNLz8Y5Br9yWj1cqgz-yHfsyHhBQ8YiTGGX5QA22nnDaoEQI2fP6lZ4wzuiel138pCi4WQ-qgUHaGvrnij2Et3pEWGXoIt5-mDUjBc_MoMfNGukaNVBwYLehbronW5B4wnOFNuKO_fCsYnUmxt2rQ1-_BM7XBPY_3syt9sD_XQMxh87TH6c4wpqVmZY0-PTRPA3hCAfuZxX3LI1xrZmDCUvjbUiZwFug8EcirTEVYNJDWLqhx1R9No5rLdlIRox0xRojDH3bOLInA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
یک چهارم نهایی جام جهانی؛ صعود سخت و نفس گیر یاران‌لئو مسی به‌نیمه‌نهایی با برتری مقابل سوئیس10نفره؛آلبی‌سلسته‌حریف سه شیرها شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/persiana_Soccer/25492" target="_blank">📅 07:45 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25490">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q5r4VXYUSuBVHAWi2Ro8GKyjGZWWZ2kTkErbpLrW6L_hAg2pIaJKN2K8tZQNr0Qs9my0hT62u-wq8nI2EO61Z0gi33Yh0vs9SBo_OolyUbuL5sh5BBwuryrJUvR310ts2-MSTKRfMnjh80NHjjaHQzjjpJAgkK08TTrkn-xcGg7vy3x39UoImcWG-itTs-7ffud7wwvLSFtdd2Cwad_fYPBQpN2V4V0t6if6LdBHd2zXCE-_PlH3hTnhcP_kB_jW1XEJ2Skktm6it42ef3MeG4RLXO6ZZ2xWrPcb-VzVy0x_t4ljz8ldo3q2ps5XU8PGbrsjwZwb6vCIiarvOqtt0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QyrfuBreWaNN-tw5Ifj_6u3jdCyEJ5CWKaFP274weON6yOj7pdP3ZxfDK-w-FN-1mptovWiyMijvl2ylDXMFEGBBsm64peBlP6MII0dDmCv_IGvnbhzb2pBfwleetq71DCuuyhycRl9azSTw5eHZde0T0xaU9_yoGO7ft7iNWx7kzcAi26lxJZffDlZbInLvzqZo6RL1KUNKnEgoyDN7rNnGZZQyl7PyTqw1875e-IZEUZ7eB-AOP7jWGTbqQ9-d09OIKKucfzw0k3u8Ldg5CAT7k6iFq2PoodU7Ep-YH6n0ACf2tVKu6m4V6Eunk3fuxrCgkFgnkDDq8f3GGmatwg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
یک چهارم نهایی جام جهانی؛ صعود سخت و نفس گیر یاران‌لئو مسی به‌نیمه‌نهایی با برتری مقابل سوئیس10نفره؛آلبی‌سلسته‌حریف سه شیرها شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/persiana_Soccer/25490" target="_blank">📅 07:21 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25489">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RIT2UvmlVcaqC1nU_AbW3PKq3ijTt12K4_DJyooo9yvMT0ovdeZMQeEKKtsN9Z-lXhatvNDYs9pKd2RTYIjm9B6W_cWZZHPdt4nxLstyW7JbSRhbwAcjGOrFvu8y6BIPCE3vcW9KzE554jmAGkyb4TTTk68YBH7UCCV_76K2Vj8GDeDxnMpR3UMmKssxoRIB4mCPMhaMl3rUz-_6NXC5L0tmbBy1KclZWF5QaPQNHz40tpLhUFrxLQ0JG-ETzAkF1jTEwNJdUFtARPlBufeeMNMTNnor1ckplLA0zvJP0QRVjvw6mJGrSDWgzjOdUk30xNN_z8ePnbBfn2oELNknYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک چهارم نهایی جام جهانی 2026؛ صعود شیرین سه شیرها به نیمه نهایی جام با درخشش و دبل جود بلنیگهام؛ یاران هالند از جام کنار رفتند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/persiana_Soccer/25489" target="_blank">📅 07:15 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25488">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vODlzIvwJvR7jEH_st_5WkdfjIN8rLUmx023vDaY3oZYbUqBgZFEBfkjY_NvGLLUMU26QvwA-5wWRfCFtOn8oGkrREyTQ5Bl97p9NmievFsHy50giVqhx9uqQcOkdpISV5aRcDZGSLqzPYJ51LoPUOBkU6EBwBFLb8XnohVHkvunvhrBhInD9Q826HEfrgcyC6RoyuMX9qRIF09wKkf-Zn41m9QvL5XkIAzMrUP8yalFMpEssjHxHYXcDOVUHAqX2b_E_rlO8rd7mQKcbY6VuMFPyCvYxDcVDsPz7oYJHAvPagN8dA5PiHw1x_JwPyQ-xq-ycGjLHQ0eczwbPe6lVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دوست‌دختر بلینگهام: امیدوارم‌امشب انگلیس با گلزنی جودبلینگهام نروژ روشکست دهد و راهی نیمه نهایی شود. بلینگهام رو بیشتر از خودم دوست دارم. هرزمان رابطه بخواهد با کمال میل همراهی میکنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/persiana_Soccer/25488" target="_blank">📅 06:33 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25487">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h7sjGinlNuR0PSM0CfN2YD55VFEjQEm4lIY-xzbll0hotJTpYY6c59EGgTkDQIwAvN7S5gcTAgDTcAw_pNAH-r0KFHjC8HphpuOvIABklANizfTXaeGCosqKRyNb2cRVoOxQke868u1c6J_5T0YMT4HoKoAtN5D7yErTGwry_SGUwW6dX1eGWaoJis4kS0npfBLiK2DrKbeAbJsvoTx5KlGaOH5lTy6dgvAgQdlVtwrZvscJV1QCPjSfITt3Qvp764dtA6A1tUrYaWjYb1GuOIH_RfKyRskLNF7e7sy_Ke8IJ8IpNG4Y81oqft8qBzm7bEN3pFhOlWpTTvE_rZXdWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دوست‌دختر بلینگهام: امیدوارم‌امشب انگلیس با گلزنی جودبلینگهام نروژ روشکست دهد و راهی نیمه نهایی شود. بلینگهام رو بیشتر از خودم دوست دارم. هرزمان رابطه بخواهد با کمال میل همراهی میکنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/persiana_Soccer/25487" target="_blank">📅 06:19 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25486">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bWHnPvkktJjPSLK2IX--XjCzRZqfLJ9jG7T-i15PG-4gjC57n7Cb27ghY8Ltl0q-zBc9McGu_L9E4TPl4Yc9axBpdVdAaiV6ZmOEIB59VjppFvDmsCDBgOQYsCfawUDQsiJEGyl4E7wJjkGbXlluVCr6WDobdiItDRgRiXOSdaJy8kBclVkfZ9uRAwnU-oYe117jHrbHtfghPRoApy7hE4uBk0_fEb_UIcQqfPXh0P7UtOxXpVTflVrGQh318_chWXi4x-np6AJcaZoja-OnNNY6rSVu9Ch53pKADVAAQGjmo1nrrj107CRGPQs8UGihrIKr0sr9PjBNRFsv_BJW-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">داش‌چیشد که به این روز افتادی؟
چیبگم اون شب جای‌درس‌خوندن‌نشستم‌بازی آرژانتین-سوییس دیدم.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/persiana_Soccer/25486" target="_blank">📅 01:25 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25485">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67aef1f61d.mp4?token=T3FwqVTRmhhQNjsC9UKmTz63wneZb7JrCR8_EHpG-ciC6xOs-UXMpFXeSwxIIcNLxZwFBVN8nEAH3cxruP7gDXN7NX5ayjgvdUmGvzBSK9ttBIlCacqC1nqTKEtmmegl3xcpasznusycT6fxrv1dCiM3cjwwE0A0dBJUpjfFpa7udZBV9habLJhOIEa6S7eueeiijnLL6ptJI06cYOP_4REJ_912xlCaYzjJGT_N095pHJQ85zY4zbnzHgmSJ_WqYWeORRFGDacGj9ylHw7f1zOOntlmwVim37cN6PPu6sUd6HGqKym5PAddLPuM3Fx8YGsqKPf4SJn5VFGz9C-eHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67aef1f61d.mp4?token=T3FwqVTRmhhQNjsC9UKmTz63wneZb7JrCR8_EHpG-ciC6xOs-UXMpFXeSwxIIcNLxZwFBVN8nEAH3cxruP7gDXN7NX5ayjgvdUmGvzBSK9ttBIlCacqC1nqTKEtmmegl3xcpasznusycT6fxrv1dCiM3cjwwE0A0dBJUpjfFpa7udZBV9habLJhOIEa6S7eueeiijnLL6ptJI06cYOP_4REJ_912xlCaYzjJGT_N095pHJQ85zY4zbnzHgmSJ_WqYWeORRFGDacGj9ylHw7f1zOOntlmwVim37cN6PPu6sUd6HGqKym5PAddLPuM3Fx8YGsqKPf4SJn5VFGz9C-eHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
واکنش‌جالب ابوطالب‌حسینی از رابطه سرد بازیکنان تیم ملی پرتغال با کریس رونالدو در پایان دیدار مقابل اسپانیا و حذف از جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/persiana_Soccer/25485" target="_blank">📅 00:46 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25484">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tya9S2D6eJ3HE_Qyd6fYeRKNxEGIYAZz9btP0g7MreU1eeXhsYzKT9yHLHN1SkjSn7rOfQYnQV1IxzWzYLUCv5KGlavIheNtwWnKp7bNwq86wE8QM2Fz0mxau71-KgnT4YYwqBIzlvL5XJuvL2GALuXUx2zFL4dmbA3oidksGwRusJTdJSy8-oGxCQ9bB7ks7RTofyz3_vaTR2ZIYbYQGX5i8J2kRgzAn9-wjyCYINy1enVR8sGZ0l-IwNyCkKdPYjbr7yzhZ21I_r4ECeDQB4jYYVaVKrPaiD2jE5OnjTORqfdxyzhFM_mw0kOAD1emDJUa_BRNL0etghaWb5KH6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نشریه سان: درفاصله چند ساعت تا شروع دیدار انگلیس برابر نروژ دریک‌چهارم‌نهایی‌جام جهانی، جود بلینگهام دوس دخترش رو به اردوی تیم ملی آورده و باهاش رابطه برقرار کرده تا سرحال وارد زمین شود. توخل قبلا این اجازه رو به‌تمام‌شاگردانش داده بود و گفته بود نباید به…</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/persiana_Soccer/25484" target="_blank">📅 00:31 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25483">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gMkvORIn1TH--yjpnj0St9G0atVsYoHOC5gKfMv7W5LNFil4cEYPZsTjpSO2nipM0wj-BgKAMdVLvWaGQvYVsAm1U0swKJArUk5SPi_q2fG4iM-l5zlgGR3f6ChMd-BmctEykuENhGqGdIqMCX7NjpXGVFLJDFMndn-voKYJg58qCQCHj21WVvpRhOVcV3xFVp-j40Q4-EMLPiswt1l94rl08TgpOb-0-sdlAdxAOuC7RPK2fhLTB6uPfNiqCNphpIdd9cFylfM0zQRBEwJplgFuD7wSGFwQnZ_r-JCxe5giE_0mi5qXu-gtjcbbegJpIPrL_OL0idoXhHU6cr4x5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇩🇪
دوست دختر کریم آدیمی هستن که به شدت طرفدار باشگاه بارساست و روی انتخاب آدیمی تاثیر گذاشته‌. ستاره‌جوان‌دورتموندی‌ها ساعاتی‌قبل با عقد قرار دادی پنج ساله رسما راهی باشگاه بارسلونا شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/persiana_Soccer/25483" target="_blank">📅 00:24 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25482">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SnlIkPIBtRnZ4wiRt0ajbynD77KQialR0hiRsROFcw870Q5SCj4xYks34MXW9wTneE5lNQx2T8oZTdqJUgzKluwBQliVyxw4pm-4WZ5_xIdy3Ujmd6uBj0wmV0NT-XhufFN7jo9aeO1i0yI_6LPNRP7Y0P0DwixYOD8aAykzvMXj_YyJhstcsX324noecS_tJ_em9LfD8FJsjEJndrof4POKZSYPNRDckKk7mXVdwzbxjU87pItzzRZ4orInQSv-Wmg9ahU-yGUhqccI7IT2LuFAK3hG7WWQJi5q9bJ2jS84fxGOuY-yD0Od2dv85EamTh9hJ7yxJQWAd9JEpA-Z8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق آخرین اخبار دریافتی رسانه پرشیانا؛ رضا شکاری بعد از دوجلسه تمرین با تیم پرسپولیس در لیست مازاد مهدی تارتار قرار گرفت و به مدیریت باشگاه اعلام کرده قرارداد این بازیکن رو فسخ کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/persiana_Soccer/25482" target="_blank">📅 00:18 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25481">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TSeiwVUGpc7VZL-MnPLj4-QklVyyuvNeYjAtiU-7diWHLp7hPe4XXlSKNyvjYv6y3k0fBg-4cUK546C7WJkPTHrOmaxHXlf3HSeSQvkplot9YgJ2PUe_naBM-r7cjB8ilbVzku1u-9ZgBIzcG7XcsCGzbaD4rgqs8guNWNTzA1nvk2gKes_gudtsZQLNg7sPEEudU6n-2P8JfkdUC82mOw4F8LZwxtpd124zAhQUv0n5wjNQFQZTDhY0_EWGB5g93bvE-uU2PhmxbMXMFOq94u7ILP6yyRah1AtBXjLeBoLcIoIbdM3loXZnkqi2cdS4t3WuVFL4fASA3XjXDgbPzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق آخرین اخبار دریافتی رسانه پرشیانا؛ آنتونیو آدان،عارف‌غلامی،آرمین‌سهرابیان، محمد رضا آزادی چهار بازیکنی هستندکه سهراب بختیاری‌زاده به مدیریت باشگاه استقلال اعلام‌کرده درصورتیکه حتی پنجره نقل و انتقالاتی آبی‌ها باز نشود باز هم نیازی به حضور این‌ها ندارد.…</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/persiana_Soccer/25481" target="_blank">📅 23:39 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25479">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZjPkmhwT5MGJ5EitE3cdOi2MZhdrnj_oDpi0yoDPS_R-9enVUhyHznfyFWgIYBWb9H6SGR1XTFDdxP93qE2TmmOMaFhtEDC4pK2yF8Df3oT1_es3N-gSJCmbSDf-g6tAicGjE1wVzeH-Fi1YKoKJzI0O6MfySPBJDuZwDa0wkGLShs-rsWakNzX5fOZhkcUBHnvhwLb6xemUo8GbzoMpmMkGkuqrFczy6XSEhLz3fmsyPuXLZlSLykenvKYYTXNxr183xCqqg7w24_fyWuaezRjPIyNK9AqtJhPNCx9LOTyQv4nfbrGHlxzuH-7GKAWQNdU8gSEpSxCW--WtQor_VQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UsA3rP6RUO5x1dO2fucWWKPLrCOTK1KbVF1YDcqm10EypZH6s6gVbcjc8ue_nkJKjJnzpm8_OT42wE5V8y9lauafU_3JZ9RvMd_ehb4P82Wlpf4R5nTmK2fVDfYKoOmi8o-nwojGcyV3WkRj8gFjlZDPF_eY6ff6Hh0fN6IEVJs9lqvjzVhKMI6vl3UYBRuoN4_q5bInJghC-V9MXqMJPqc0xl6E5iiD3Dqhb546_Q95vH__0y8DNy7kP9VdGCQSDgWYTeWSkELpM72Vj_AGqVSX-f20vsVcLb9-liDHznbgpiJ_I0RYv72K761MUNc0Q-SMmjTwQXpZd9tOfMr18Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
نشریه سان: درفاصله چند ساعت تا شروع دیدار انگلیس برابر نروژ دریک‌چهارم‌نهایی‌جام جهانی، جود بلینگهام دوس دخترش رو به اردوی تیم ملی آورده و باهاش رابطه برقرار کرده تا سرحال وارد زمین شود. توخل قبلا این اجازه رو به‌تمام‌شاگردانش داده بود و گفته بود نباید به…</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/persiana_Soccer/25479" target="_blank">📅 23:23 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25478">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L5ACo59S1T2v5tp0QmmADJ44alsvDsK7OThOo7oi3CEIMvhJaXY9C0Z5xchMKomy3EpCdPMwoh42SBdjLL3NzZ2SFCT-BpL-JcN7AhpLxMkednMDGPKW6r9ZUQ4b27-UgZfqt_EovUKfAf9kRWmt-8xF5IKdkvyTZZRIctfgiLvx94ZVnbjoACORJk_mAE0C7Xl5dU3Woi1kM1K87otMqJCja39QUAiiEAULwkqxGBubg4SieucT8f63JwF4uhhk9F8P0YtokI1HvrukXiHjWb1Su8Z0tbi6j11fEvWYhsQAL5VrWaRpKdE4WWb5Q72SZMwqdZ43pBRuLIl1Dpa8NQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
طبق اخبار دریافتی رسانه پرشیانا؛ میلاد سرلک در حال مذاکره با باشگاه فولاد خوزستان تا درصورت توافق مالی بین طرفین به این تیم اهوازی بپیوندد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/persiana_Soccer/25478" target="_blank">📅 23:16 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25477">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NvQKFiGWGL068uQQjv0VYwHYH3kDpaV1MicQEYWhnI3CbEYqx2uRWWca2eY5_OX-kK53Jh9obhANtWPZ4OEPg4HiTc_TRxofYs46VsoyMZSHLmDg739y8PAtusiYbvOUK8z5ymiJDfCFQyKCEIGbY5-ZEebCB83dv9ZtQgtoLC5PzYXraRFL2UvFTwMNnRPF7aovb8I4hTQgKsY3rJZUFFlcy2aGa6CbyQ6P2f9Fp5BZyQpyHxxzdDudYHw_jQkjjR-UKlguCXZiRK2-A_9ixLLjxsl83u6EnbZTlbDxZsAuIN6ZScc6LDZbLWF3UAE4F3ZKQzNcHBetvd_bICtuCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
👤
وحید امیری کاپیتان‌سابق‌تیم پرسپولیس به‌مدیریت.این‌باشگاه اعلام کرده‌که درصورت تاییدیه کادر فنی سرخ پوشان علاقمند است که یک فصل در پرسپولیس بازی کند و در پایان فصل از دنیای فوتبال خداحافظی کند و به کادر فنی سرخ ها اضافه شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/persiana_Soccer/25477" target="_blank">📅 22:53 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25476">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c4rOpk1XcMJKydcvuh3aGPd-CXbNqsPaL_BjEPZZ-X6yS1NTZ8amZFW5AMgeFodzElVkwQUmS1bO-Dtr-9ge6syfoNH3s1WUM53ENzUgcnTbHe5H7KPGvnNDwd8zknAnwk8PTIFhg6VedTyNdZzNwdPhZFCsMY4XodG9OLqr1_dDNWmwE3IAaNoV-PLdQhLl1zKTjXUVDf8XotzXwUQ4DIRzCThxqwSDgYp996g8_K7chFkxiWJ1umlPTk8is7RjxOnBL030OwozwgWzEfkbWbKvTRuKX_B7NJ0G4UvpdPV2Z_FQGqqw14ZHPmua2DcL7I4nShmHTw3yXgPiIonQUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
#تکمیلی؛ روبرتو مانچینی برای‌عقدقرارداد چهار ساله با تیم ملی ایتالیا با فدراسیون فوتبال این کشور به‌توافق نهایی رسید و انتظار میره به زودی پوستر رونمایی از او نیز منتشر خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/persiana_Soccer/25476" target="_blank">📅 22:41 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25475">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d020345f8.mp4?token=H0_PvJ09aXjCW4kHStERAj9N2PgP_dvbZfTZCNYaVOUv1QWqLVu8XuBtrDIcxD9Gq1niyP8LEiDZqrFPtV9ZNnJDKP3RHjVqBHveJ-3N0NsODsg8U3A9y89ecdxXJseUzLlFs_RYfbdJYkK7zef1Hn08javNKpEF8ySjLRaQ92vZoPS_vS18GsyHL7akxoyRjeF7v6XkgYLG-1UsC3ulIqzwKu1sAF_7e0g39oh33AW7DarbaNM6RiCx38ddWZ4ZL9Lr9WVmHhe3uyJnm1pWbeVIafsNCl-v4BRbpxuXtYX6hKVjisQYTqHuvQHUnuzalQOaU_O-4EPiQleGfzPF7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d020345f8.mp4?token=H0_PvJ09aXjCW4kHStERAj9N2PgP_dvbZfTZCNYaVOUv1QWqLVu8XuBtrDIcxD9Gq1niyP8LEiDZqrFPtV9ZNnJDKP3RHjVqBHveJ-3N0NsODsg8U3A9y89ecdxXJseUzLlFs_RYfbdJYkK7zef1Hn08javNKpEF8ySjLRaQ92vZoPS_vS18GsyHL7akxoyRjeF7v6XkgYLG-1UsC3ulIqzwKu1sAF_7e0g39oh33AW7DarbaNM6RiCx38ddWZ4ZL9Lr9WVmHhe3uyJnm1pWbeVIafsNCl-v4BRbpxuXtYX6hKVjisQYTqHuvQHUnuzalQOaU_O-4EPiQleGfzPF7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤩
روزی‌فهمیدم مسی هیچوقت‌تسلیم نمیشه که بعد دعوت به این برنامه‌ازمجریای حشریش جون سالم به در برد. لعنتی‌ها ببینید چه گیری بهش داده بودند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/persiana_Soccer/25475" target="_blank">📅 22:35 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25474">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/me_6AFolo3kv2WyGZHrPn3cmpdS7agm_RSkTb4IysAqm9VA9whcUxTbQ3oQ5C8ivIrewQcfQAysks8pjHmGThKd4m-U9B5bEtxaa79UzB_edab34HMjKNc9h4REUkSaS4E5cGZu-z4tlA5fT4OEciS54Ant3O4qis50g9w-w0G1F-xZTOeZbKZ2--AXKYybPaFjqc1mPIr3W5ybt9XC7-84CP2sIV6yIJnCFnRYsLXJqGjxMwR_HJaF_GEvsng0nrTa_0rKHq28AqR2f8Cn-gF4xosy-WaUBqd6iVOx5Rc2n10MwqaznmFIHAoqW_e5-72Ua9KkUrc4g1GATV3Y3Bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تاییدخبر اختصاصی پرشیانا توسط پیمان حدادی مدیر عامل سرخ‌ها درباره وضعیت علیپور و محمدی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/persiana_Soccer/25474" target="_blank">📅 22:24 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25473">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec99dbc8ec.mp4?token=jS33fRSuk63evOlB8XqOQWv1zk8zJLlJzQ0EQh_hylPTuIiVavPXWvyrZiMR25BibhQF-7RB7P5--b6yaco1rPoFMralrGFcmPYMrbMAQJNf8KU856AOtVKO24U03x7fARqAF1Sra916BF-kvOH3INuiEYEmLvFaED22QzhTBLuD8yYap9tqEcUMATUrwMXO-dR3PRU7vZ6_UUvzNN-8740VSGYSr17ao4t_n9fVfmZgE89mIh0KAahwKYlkYooNC0ufTxHWIE24pnrQPcgmw1ROZzZ-m2RGS_ychw7qyaNNCjK538C0IDM74_mDugyWloP7crBKnEhvq6rsV-lzQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec99dbc8ec.mp4?token=jS33fRSuk63evOlB8XqOQWv1zk8zJLlJzQ0EQh_hylPTuIiVavPXWvyrZiMR25BibhQF-7RB7P5--b6yaco1rPoFMralrGFcmPYMrbMAQJNf8KU856AOtVKO24U03x7fARqAF1Sra916BF-kvOH3INuiEYEmLvFaED22QzhTBLuD8yYap9tqEcUMATUrwMXO-dR3PRU7vZ6_UUvzNN-8740VSGYSr17ao4t_n9fVfmZgE89mIh0KAahwKYlkYooNC0ufTxHWIE24pnrQPcgmw1ROZzZ-m2RGS_ychw7qyaNNCjK538C0IDM74_mDugyWloP7crBKnEhvq6rsV-lzQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇩🇪
صحبت‌های‌ندیم‌امیری‌بازیکن‌افغانستانی تیم ملی آلمان در رقابت های جام جهانی 2026؛ این بازیکن از دو تیم آرسنال و چلسی آفر دریافت کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/persiana_Soccer/25473" target="_blank">📅 22:24 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25472">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jYRy66PpsI14BCIbNrDoG9KU490f7FY1pxZHs9EpswSOdBWKR5Xonnysoea9vkiB_dZby215415OgogrTxG68XWt9yP00FPo55_27K0YevPwc9oGhOrSCBoruxvq_mG6dH5PUBEzMSDWe_lOM3mFNMyCA3YvDF2oaLaQEeIR6wCs51zAVADlQSbHMyicNLoQ2k3JsqZRPqVdow531NSM0puJwaApFyQnDGiZY0PsN52YjlSq1oBCvwuH-B1wrGt0WskVOgEQDpf6uvMW0XeFYK7E-S_EciJsISAe5BO4_CEy6p6pYOW7ciSnHyCZfNqZcJ9YTVxUurghCZpWCAE2Gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
قدرت پیش‌بینی‌ات رو ثابت کن!
⚽
🔥
دو مسابقه جذاب:
🇦🇷
آرژانتین
🆚
سوئیس
🇨🇭
🇳🇴
نروژ
🆚
انگلستان
🏴
🎁
500 دلار فری‌بت
بین تمام کاربرانی که نتایج را به‌درستی پیش‌بینی کنند،
مطابق قوانین سایت
تقسیم می‌شود.
🤖
پیش‌بینی خودت رو از طریق ربات تلگرام ثبت کن:
👉
https://t.me/betegram_bot?start=p6_r4EF37DCE
⏳
فقط تا قبل از شروع مسابقات فرصت داری!
موفق باشی!
🍀
⚽</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/persiana_Soccer/25472" target="_blank">📅 22:24 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25471">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uOHjieBKprNXsiuvFmAlCw0cFMx2yUrnJmVKvXV0bYG4SrqE_YmwNYg6B2liMG-1130P-AJ-rinu3TL2Nm4UPNBwps5LiC88vXW42YHB92kXU6F26kmJKkjzIztxB84by146LiHBxR7HH88861AictXHSOYltSxYL-UvKMvLQUCN2m4DO9WFqNwx0UlakvIOfyDHOh5a9iurxfZgmz5X7XNeWTUKdyVYo5aHIqmqRWQg94p7Awp_Ew9CTmCpeT5uKoM2jEX7l-F450UqjT63OgDaTr8xZzMjApBWwj7OJPKdWVEWVPPOeZkzTD6yzcYVfM8o_J897XMn_3LaHhOv8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
#تکمیلی؛ اگه جدول رده بندی رقابت های لیگ آزادگان همینجوری‌پیش بره؛ نساجی و مس شهر بابک مستقیم راهی لیگ‌برتر خواهند شد و تیم صنعت نفت در یک دیدار پلی‌آف به مصاف مس رفسنجانه میره و برنده اون مسابقه نیز به لیگ برتر راه پیدا میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/persiana_Soccer/25471" target="_blank">📅 22:05 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25470">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/phMjIHhRp8nycr2q2uN9Tfwk1z0P2hIxKIHuOZ-BXt4_lypg0be8bTc3D103A8ar-96cU0J2JDp1FJAgk6g8iculPEjplXbqxv3LC9BUa10WLnMFmRUlJDF0K93c-I794OenYG1ZhXYR0tli1_aetoaPc3Afm5g9D8nMVEqf6mtPHmBwSqzkmMe_Lf3y3vbE8MolpY4NuATKfYZfIpccvLkmm7kt4MXPvIHIrzqPD-HSFTvxEJYKueE6KW1lZ9oxr7HnWrs3ZQAPi2q6wFqWPemvda3-Yso4lKFphM9Vy0P1Ns052ukfVwlaFTqDVqBnALvN_-4U0kjlA9qclvnnmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جالبه بدونید بازی‌هایی که تو این جام به ضربات پنالتی کشیده شدن در نهایت تیمی که پنالتی دوم رو زده برده که این‌فکت هم درنوع خودش جالبه واقعا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/persiana_Soccer/25470" target="_blank">📅 21:57 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25468">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5fe85cec8f.mp4?token=pSS4QK_FbfaMf12FaD7fznJi9Ca2_3j89pNwHsNtk4zw91i4fzTBAUaoGGumJaq9fP5XXIu-AP6d_opXs-y8SfG7JGZf6sIrshJn68ntDXAaGMtH2_umiM1K6Bf0DFhLu7BfqBU703Vfi_iYso5jK2yFeFQErLGg2fRZTQ3UBMJHGbkWg2uxWGiblOdwDyxiD0eBQYoQEWh1_fYBXIePBg6XZp6D894ACyk8EiYCS_9xIami7lQq3wDmkzJzP1hgXtAI_OkvqOsDYCMFXZnygUN5B9hLbkDt0V2FIqObnRCZ9mKnuE-sTZPMyhoEqv8qfa5nvH1N_A9OigVpbSaZag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5fe85cec8f.mp4?token=pSS4QK_FbfaMf12FaD7fznJi9Ca2_3j89pNwHsNtk4zw91i4fzTBAUaoGGumJaq9fP5XXIu-AP6d_opXs-y8SfG7JGZf6sIrshJn68ntDXAaGMtH2_umiM1K6Bf0DFhLu7BfqBU703Vfi_iYso5jK2yFeFQErLGg2fRZTQ3UBMJHGbkWg2uxWGiblOdwDyxiD0eBQYoQEWh1_fYBXIePBg6XZp6D894ACyk8EiYCS_9xIami7lQq3wDmkzJzP1hgXtAI_OkvqOsDYCMFXZnygUN5B9hLbkDt0V2FIqObnRCZ9mKnuE-sTZPMyhoEqv8qfa5nvH1N_A9OigVpbSaZag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#تکمیلی؛ باشگاه‌پرسپولیس که دوهفته پیش با ایجنت علی علیپور به توافق شفاهی رسیده بود حالا 72 ساعت به‌این‌مهاجم 30 ساله فرصت‌داده که برای تمدید قراردادش به ساختمان‌باشگاه برود در غیر این صورت قید او رو خواهند زد. درباره میلاد محمدی او تمام توافقات لازم رو…</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/persiana_Soccer/25468" target="_blank">📅 21:50 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25467">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aIFODyZsyz53YVPmokWvTk3qap0SPly49fTevJzdnXj4vDzTpKSGIqUw3HPxy0cExR7UUNkzBS1gy4LQ2ZVGEZlo1HNVyB9mxVzGtaDZ-60qFI6tlZCcBn0u3YTKSMmmi98QKUY1RKOdSuKkjBpsyGyOaH-lBMao1xyWli3fOWFM88rqjl17NGYsgIK_Gc97L1SV_kQhPfLRWJ1IKoZY3-qeNzkGIFhvRn-qHyZtnnjlVYK341DqqLjlTTeYZ9RrwYO1a94V0H2n4AAIHl3n-ZYoDlIrXoQegbs49q9MgONKjiik5gBygHnULV8wpOMJax1Vc3ulygCn5hcFwMwjVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی‌_پرشیانا #فوری؛ برخلاف اخبارمنتشره‌رسانه‌ها؛ طبق‌پیگیری‌های رسانه پرشیانا از مدیربرنامه‌های یاسر آسانی؛ ستاره آلبانیایی آبی‌ها مشکلی برای ادامه حضور در این تیم نداره و فصل اینده با شماره 7 استقلال به میدان خواهد رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/persiana_Soccer/25467" target="_blank">📅 21:35 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25466">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d4wPrF3XRv9So2iHyQXayIbuePRV63KcCsa5vH13L-vM6GLI1fO_tJoiVrNf4uRuKT0dSIx_c7XLVbWeehxIJT7FiUIRHXD27GtPW45Voj0URNl4ksSZH0st3ctmcxIIJZX5IkFDI7zJ9nx0FNnyvQBex9TEXUm-u7XnSEwNBMV6OlJ3dINmfcxFh825sfM7UZqCKZf5Nvm92bqAIToP0L3ELiNaE84KDFjJzDF-z4O8ht2rb0tGlxT-Jm632TdD4vmblLdrGYQw9ZP3IAbY7DbFoCOrUphtcuFkST5cFBKZcs_haGd8u0QqWxFb2lG_RU0dxHcAnjDiHhSptfuSeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
طبق پیگیری‌های پرشیانا از ایجنت منیر الحدادی؛ خبری‌که رسانه‌های‌آفریقایی مبنی بر توافق اوبا یک‌تیم‌مراکشی منتشر کردند کذب محض است. این بازیکن اواسط هفته آینده به تهران برمیگردد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/persiana_Soccer/25466" target="_blank">📅 21:04 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25465">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Los65Xqq6kpMCuxcM1WoGEtHaFXTzYza1y_oV1KrDvdwfGi9xVnPi5124tXHbmR66jOGwPpq3DCU4NqWOpjh_EZNJbJM0TsAFarybZwsDeSg1Ic-QKsLvZrj0JUJdncHuz61NTDiRQ0KBp4-6ZdD4lzyt_GMQi3zK7pXWD71NXjCThNdizfg4r-IG8eaarT7opzfAmIdFffKYTWIC6PLqvDPSCPprFPu9tKhJLoSLRZjrTDbjhlHgV9mTfbWQhUAXp-T8yn2LR5bEJUBWivkKGI62tVgUtva5PZtqWiSNyXSXNuWaHDelOvPAe9w589YsMZrOKy21er1U8jG6mRQhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🏆
🏴󠁧󠁢󠁥󠁮󠁧󠁿
توماس توخل سرمربی تیم ملی انگلیس روش جالبی‌برای‌انگیزه‌دادن‌به‌بازیکنان تیمش در جام جهانی کشف‌کرده که چون یخورده 18+ عه تو کانال دوم‌راجبش‌گفتیم. حالا فهمیدم بلینگهام چرا یهو اوج گرفت. بعدجالبه بدونید 10 گل از 11 گل انگلیس در بازیای اخیر توسط هری…</div>
<div class="tg-footer">👁️ 65K · <a href="https://t.me/persiana_Soccer/25465" target="_blank">📅 20:43 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25464">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rSS87EtXfO7qn2zHwDtORtj5TiFtQTz8aD4pRdTvRrpP6FtpHa0LJkUkBPVZGB-0ofrvq0VBWje_Td5uEeDwnFpTYRE81M7o4mMPBF13wXLSm8iFSvMljmsOSkf_-eKhIiq6EPHdc5vuDOmhpbH1Rdj7bA9pBZQjoeDpsYpq-VIrehTbcl1wYwqM51N-vAY1rcxjsvVKxEFEeWY8Z5R3UxONRoAG9R8PLOF-6PHrdeb_RfNtZhvkOHeHHDnFjyITmhZ4f-SVJphVFB2plL1H58kbXV7YqxGwmIZmusaXhafkKW9Tuo4yatCSgpFe1pK8VZSLu4qVPHioat8DKwm_zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
بعداز موافقت مهدی‌تارتار سرمربی جدبد تیم پرسپولیس؛کریم‌باقری بزودی‌به کادرفنی سرخپوشان اضافه خواهد شد و قراردادش رو تمدید خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/persiana_Soccer/25464" target="_blank">📅 20:32 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25463">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DtlPPfkOv-lkizjReZIm8bbnXRqwXXjv6unlmagVMdZqX9WJMKEovrobVRMIrt9NqMBQAoKafWJKxjgbwj6nhcc14fSI8mJcAUAzGh6Bc5g3hlcZJeqk11PYh0oEmbhaJXnSkQUPJJbEQbFeAlVMtP6kE6vJJOkpBFx8UIYhynVVJbaStBCkLKeWZlg4VXn8NqRb-CE9nN_nN4onR4uxTeEwpwCXlb8JvDQCmiD0tNndLKFZqOyExkHh4GTJBN-BFvYFbYkwphBXQxqxSE9ttg_ksd-9NuCl0wRTtg3T93d8irbkne5dU9ieUiIcouQwJl0xsGXPN2eiBE8hjA1_vQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
طبق‌اخباردریافتی‌رسانه پرشیانا؛ امیر هوشنگ سعادتی ایجنت معروف فوتبال ایران با مالک باشگاه تراکتور آشتی کرد و در اولین اقدام قصد داره هادی حبیبی نژاد که روز گذشته در باشگاه سپاهان جلسه داشت و توافق نیز حاصل شد رو به تبریز ببره. اگه این اتفاق رسما بیفته یکی…</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/persiana_Soccer/25463" target="_blank">📅 20:22 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25462">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AMpsWeIbwhbHuU6iac9emJxuRjt310BYiUiByV456Pt66vjPaahwgsWmN_BKg4PtV0UesAUFMuED3wWTn0BJQqX6mzbshPxBdkwblt00WRJQ-8L8mYBtlTa8SPWkAyZ8G3BOLnz3t-5Nit0Hr7OeHaVvWCaJXzPpNrY6T0ypWzPol3wiRUQCz-2MPFqKxo5d0mG2rV_dJPIpB4AhPuX1d5qV6cAp6bxL2rMhfYydO35thSWrkc1BdM_BXmy-H0tzw4DgOzhJmT4Iq4iGEKc3GVSOJJxe1JX65cVURHeGYp1AvV1UHu5CHiSB7uEzqc9HRqbogxpZJRbJaemrvugQnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
امید عالیشاه کاپیتان پرسپولیس ظرف 24 ساعت آینده با حضور در ساختمان باشگاه و دریافت 50میلیاردتومان‌قراردادش رو رسمافسخ خواهد کرد وبعد از سال‌ها حضور در این تیم جدا خواهد شد.
🟡
🟠
گفتنی‌ست‌دو‌باشگاه‌فولادخوزستان و سپاهان اصفهان در روزهای‌اخیرمذاکرانی‌با عالیشاه…</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/persiana_Soccer/25462" target="_blank">📅 20:21 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25460">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C8d3ff06-lIhebrIOPRSIrgXgHwQxoUd1sVDSfH5aGuj16NmyJyEkr4FcTcmq885XYmVWFQlqSlBM8ibuXNGmNjciUuboVDo2KQtyRhT4y-sP7ZMRy9zQLat-DSXAF2rKLpGfpbn9pjEWizWob5R6aaMIxCi0ZCN5w_iMNaGPIQnlAqUlLkTaAC6R8thNhC0r18dsi89q0G4OVcRKuB4X3gg2PnsCU_6mg1qLlLBWJOv8Wqd3Ix2Lb4wKD02aDqzpVlr8p01OOo9CTihHW5FCOeU51-1AfqAs84215CVIOoYGkCXARVHL6SvOO4PPObDGTNFbEXUjXcSFyrO5dbmSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
محمد عمری وینگر 26 ساله پرسپولیس دو پیشنهاد از امارات و قطر دریافت کرده و به احتمال فراوان فصل آینده لژیونر خواهد شد. از این انتقال 600 هزار دلار به باشگاه پرسپولیس خواهد رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/persiana_Soccer/25460" target="_blank">📅 19:46 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25459">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kT-JiMJrssjYLPDq_vkIsSC9n86q5x_BL9MjYCH-rqnDoMJMBTcsOgdCsfQXRzcifFIycHWd64X7lYknKx_RWgjCGQmhrLNJ0-SVesDHg2o8b2TUJwIJO7aXEt9JqNxGxnrO0Nsa9M5nPllVaQRuHbQAcGaiZD6rER8VzXGsMJJy86_pW6jHwVy-7oEDtrecSPiD_JkbqGDTmKFFkRD4nuIA6cyEMXDvL0oV8wwohfdeJaxPHfV4kRSAPKUmOmTbAfsLIm3Yp6I7heStjCm76vyMBZRREb6LGzftUvshQdbL3wvI18IruzTlhxJ_1_WHtCQT_er4sMmpqRSCunbrOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#تقویم
؛ 12سال‌پیش‌درچنین‌روزی؛
بارسلونا با پرداخت تنها75میلیون‌یورو لوییز سوارز فوق ستاره خط حمله لیورپول رو بخدمت گرفت. آمار سوارز در بارسا: 283 بازی، 195 گل‌زده،113پاس‌گل، 13 جام.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/persiana_Soccer/25459" target="_blank">📅 19:45 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25457">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e046936a8.mp4?token=pD12IQrSA_ZMGTzXwxbjQgxDBdVWJpnPce19OfPLSnxFdc8_ugeFfhL91sNVYuowdc_DpAKRFR1tpq45g9yr64mSDS51S6O2XHOp912NyPfR9C7_BXcE9xuhaib9G0SwtciRLQi-rlBGhcjvepqGjtOHLhCKmG_TbhYu4CSFea7_COb6KhQ6KXhefKXUCZxJbpQNlxRPDy56XKo-ZmBYBY5PF_sb8Pnqqkrh8vSMgDo1AifvcR5mP0RMNQ55Q7y_vXxM9cTCfXfb4muJSOyq3zgstjkxwezJNhiB0lCJrke9W2uEOGtm33Q4WIVxw7kp16aL67Y-ZXSMYgI1M_iUjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e046936a8.mp4?token=pD12IQrSA_ZMGTzXwxbjQgxDBdVWJpnPce19OfPLSnxFdc8_ugeFfhL91sNVYuowdc_DpAKRFR1tpq45g9yr64mSDS51S6O2XHOp912NyPfR9C7_BXcE9xuhaib9G0SwtciRLQi-rlBGhcjvepqGjtOHLhCKmG_TbhYu4CSFea7_COb6KhQ6KXhefKXUCZxJbpQNlxRPDy56XKo-ZmBYBY5PF_sb8Pnqqkrh8vSMgDo1AifvcR5mP0RMNQ55Q7y_vXxM9cTCfXfb4muJSOyq3zgstjkxwezJNhiB0lCJrke9W2uEOGtm33Q4WIVxw7kp16aL67Y-ZXSMYgI1M_iUjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
لقب جالب لوکاکو از زبان فیروز کریمی؛
جالبه بدونید که برای ایشان به‌خاطر شرکت تو برنامه جام جهانی شبکه جم‌ تی‌وی پرونده قضایی تشکیل شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/persiana_Soccer/25457" target="_blank">📅 19:20 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25456">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MJaBLqKimd6H91G4y7GJ6vaBpFoP2qYN26eaW18NVdFTpXa3WVBiqm_74Enwlxqmo6JmMoDdLpq51hYYtWK9_wxyaMW3tp3ujqxk1-QlOpnfDMePF6bg5ft8qRegiFWuSB_JNSc0c_6NZSBfvTwEqIG3Y0FDPXHe1SbiF6h8CGMqbgL5bj2aZFdtfjcc7GkHQP4ApGE9xLnaXBmeo15dItH1IWIF0RMP_S9OuxX_mtxso8wZAm5-pWmlNyCJ9gYlVmV15fKaGZA3nUILdoFtnVlYgr4cRy64kJf2e1OvZgxDTQWhNBbE2WJACEiaU4vAaXplzoHys9TxZO9t52J1Cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بااعلام AFC مراسم قرعه‌کشی لیگ نخبگان و سطح 2 آسیا سه‌شنبه27مرداد درکوالالامپور برگزار میشه: استقلال و تراکتور درلیگ‌نخبگان و چادرملو درسطح دو آسیا به عنوان نماینده های ایران حضور دارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/persiana_Soccer/25456" target="_blank">📅 19:14 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25455">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U_ZhMOSWHLRffqHa2vUB5XWHyQHKBwHX4RHHYjnAeAjDhCEJ_h9eBSxLq8zDYU_4bUzI9nsgqVlHe8YC3EK7KlqvKAADHOe4lpauAWihCkw4RU4ncXe8isKhIvwWkgtngfWQotQvlAdfYvoeXXP76_L-WfsL83Up-G6vx22usZVTUc5EUAyDZsdt39vYfIK3U2Q28wkFiPOE02WZKCQOLzVAExbprFy1BalBnWN9qAqKdYw8_E6OsjOe3PMGPINqWBDRI5V_spn3dmbGAjKKEp2JqbSe1JMEdcAPcgc77T33nN-Y7fNiH89QV5vOLo4yM3-hbu3fsN8iwnh6GBsu1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇫🇷
کریم بنزما اسطوره رئال مادرید: به کیلیان امباپه گفتم الان‌بهترین‌زمان‌ممکن برای انتقام گرفتن ازاسپانیاست. به‌هیچ‌عنوان نباید این فرصت طلایی رو از دست داد. اسپانیا برتر  از فرانسه نیست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/persiana_Soccer/25455" target="_blank">📅 18:27 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25454">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">‼️
خاطره فیروز کریمی از حموم عمومی در برنامه دیشب ویژه برنامه جام جهانی شبکه جم اسپورت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.6K · <a href="https://t.me/persiana_Soccer/25454" target="_blank">📅 18:01 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25453">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dA2ttK1kuvp-U42O9Ax4zP6EL0ZVxi63AagJ8Fb4rSEvOoLeMHcYuXPX_hOD3mo1i8Q2OpBXz1S6F493UZRMYB3-oTdzhZfYm5DHjLyQcHvUVOKhbeCaSOT8-LjwcoJzzLdwrn7nXFB3RNYJj66vQRvfOIFrbKZhk8qWBDLpSUbjC5GluDR6hQJUUCeHfMoKxri9vz32ahl5URXxJZnT0EY9U5CkuHqhIVbK8J4r5w5xCq-TW_qyYG6E5Six_WOwlDryt8DdVKx9HGMjZq1QzjyuhrYm4PdeNT2fzlgzTQZWbjZByOnZ_llpfgvaQT-0cLGCBMkU-MZS3ZXE_J-Pwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه استقلال به مدیربرنامه های یاسر آسانی اطلاع داده قصد داره که قبل از شروع فصل جدید لیگ قرارداد ستاره 30 ساله آبی‌ها رو تا سال 2030 تمدید کنه.
❌
آسانی آمادگی خود را برای انجام مذاکرات برای تمدید قرارداد بلند مدت خود به ایجنتش…</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/persiana_Soccer/25453" target="_blank">📅 17:53 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25452">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/drpwE1MllUW4k9jJc4xcFPRSsYsTrDeaqH35GB1pC-DW3Ay_1U6-3Bz64oHt8v1PeJwpVQUdOqx8oC2W4hw_3tKhrxMnve8XHEpCHzHn5u2ewzvXTHqHCUtoDsoylO6YV1N4oJdl1d047JP-X9R1aZAh9c23_el5ua7rjqlNdv5lUbZq2SMk3BApqCDmMch6WJ1uRJ_ptg2aKk4Z0-q9IqfGEa3Hljhoa0kSZJVdWNC29tA5Sb-xgl7nsRhKJWKeQ3pKwhuclE_uAp5bUgz699PFDQrI2MKsfZfrQkBCfMYiAoj9rp729_BHGNKoBW2v-72nlJm3TlQXAwmtkjC4DQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
بااعلام‌سازمان‌نظام‌وظیفه؛ علیرضا بیرانوند گلر تیم‌تراکتور از اواخر شهریور ماه مشمول خدمت سربازیه و باید تکلیف سربازی خود را مشخص کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/persiana_Soccer/25452" target="_blank">📅 17:43 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25451">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KPXePhgidWbw7YV3GA6NXellU-oyHb4JsVUmX7GgqZiyHoNC48LQxW52-UJjqiEdRjTYyKFCXY0QG1JDnfTw_IwonKLwnTT-DUE98hJG9t7EC7IPDM5fqjWi8FQq-Q0qDc7VA751FuNZLNuFOzNj1ljq4c_zIoanpMZJSqikiF7_TeSgjuVy06FS3IX92dVLT6EUkRDWUU8y1m9TZQtI8tt-NQoOnKqjkZ9Tl7T2Q3AUmSd0F5Tf1CvvWRlNBSU_709-Rf8VzFr3Ib6xv2kSSQlt1u7mvQ9OT-eDC2mDV1_pK6VxwivW-qE9h3QNEPPIs075oom0_tSMvW37VMt2bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
علیرضا بیرانوند دروازه‌بان ملی پوش تراکتور: اگر در تیم پرسپولیس میماندم شک نداشتم یه روزی مدیریت با من هم مثل وحید امیری رفتار می‌کردند!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.8K · <a href="https://t.me/persiana_Soccer/25451" target="_blank">📅 17:23 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25450">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vJ45JwIWkkfS6M5OveRvGrxKKhGgFG53xokV84wc3epxS0UQ9m9OjsZRRnU51nUq2COZyAxMjFxAOvUt25peZe6SnSZapC2QrktFQMi1wqqgSJ54MbQ6KxyrYPshr1cA60rN8E25iBSnNlZVlMIjhCzKdaRr5Jqj8SziLpk9FBdThARCiR4rT8ryi_Zk83GdIllHt_g9D8gVpNx9vLNv_5NSeyKo5gQa-Y8m3h9_xVckWlIZLP2l5q615y9Qx55pAmR1qDxOcYsbLkGu46fQrTIWgq9uCMWPTl5JKOV_M_fkLlBFHb1UQC0eWXSSFty5rG-smxpDo1q-CAyCLQTnUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
#تکمیلی؛ مهدی‌ترابی درزمستان‌برای تمدید قرار دادش با تراکتور به توافق رسید اما هرگز قراردادش درسازمان‌لیگ‌ثبت‌نشد و با اتمام قرارداد دو ساله‌اش باتراکتور در حال حاضر بازیکن آزاد بشمار می‌آید و هیچ مشکلی برای عقدقرارداد با پرسپولیس ندارند.
‼️
باشگاه‌پرسپولیس…</div>
<div class="tg-footer">👁️ 69.6K · <a href="https://t.me/persiana_Soccer/25450" target="_blank">📅 17:09 · 20 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
