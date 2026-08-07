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
<img src="https://cdn4.telesco.pe/file/gWifMOeti4AiOPQU_FI4zCHOaAdgxrqeXbzynWSQUzlWwRcfBCYJjWQLBiTFbhnTA0dLHo39_FkghtME6cOEjBmunTvvIsTTFdmshRgxwbYIShUBuv43MKGn45qxcmb9-sexRQAzyp7FGXVU_YPlnglqMQoJvF7RSvCvsy0bgJdu0E89DghmXRVX-gHahk-9-9TeinoVcwtDJA-RzYD9w9pqDo5091w87TLKGzn1Isef0sko3QxWZnq944Z61xBKrB8WgGwRPrxpyAYY_P4kVCIbsFgjUjcK0LZI0iVcTTDRNr4OTtCJxm_MWkEQAZH_SSnjvlL_dkUgiFv1-C7rzw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.03M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-16 15:35:27</div>
<hr>

<div class="tg-post" id="msg-679185">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aab0df4751.mp4?token=qcO1olWNQtWOlYW38ElsUbmelEC_4xeVQBTiyNpGuHKDXDvfXrhb2l37WeMfwrxdFipTVrjqzZhClOYNp3lDtXKMU2dhk4jXLo27BT2iPJaJSunED2kotXVMnnYIuAOZx6BQ-lfnQWZIk0wD6JPuVTH-28lY_FU76kFQmpp5zACQnpeeMob5QbqatrzDovs4oouRJVWIDQCMpx9KJzFR-nStF5W_KQlkWna9e8uxYkfLVHRNWiVf4kaVLnIVJnY8Dpw_u3_6TSVqT7RYsipYcdr2fG6Ga7tXJ6UoUx_EBNQVSmYYkwS-nY5MfyZlrNtVhF9sxXtfIfuKV59e-FB-RxsVLFyBcnwhaeE4ePeqf4O4dmEBXekwW38TXbPuw56ANrqy1jEubITLjw74etaad9hmpdZX19MuxQYDg0nnnuq4WC05-qSYeP0hAcdxZTSpX4Lpq-yBejHtjU12rhM_nEMgh17vjY9h1lxpzCskmMfNkBew2A_if5KBN20S475Mg103B7OU0EfKp4NjoZme0ru9TD0g6Q8irJJfkYl3KbQ1vOhAhtPXn7Jg6fcwVXinEkM1guKiWu0E9y9uQ6nOZBkl7cnvxFInxStxYSQCQ8b1MLa5lQVsAx5sGQMiusD8nmw2A1xaqN_Xjljh0UaKtl3Mj-guD6mUYg5TRCnWtYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aab0df4751.mp4?token=qcO1olWNQtWOlYW38ElsUbmelEC_4xeVQBTiyNpGuHKDXDvfXrhb2l37WeMfwrxdFipTVrjqzZhClOYNp3lDtXKMU2dhk4jXLo27BT2iPJaJSunED2kotXVMnnYIuAOZx6BQ-lfnQWZIk0wD6JPuVTH-28lY_FU76kFQmpp5zACQnpeeMob5QbqatrzDovs4oouRJVWIDQCMpx9KJzFR-nStF5W_KQlkWna9e8uxYkfLVHRNWiVf4kaVLnIVJnY8Dpw_u3_6TSVqT7RYsipYcdr2fG6Ga7tXJ6UoUx_EBNQVSmYYkwS-nY5MfyZlrNtVhF9sxXtfIfuKV59e-FB-RxsVLFyBcnwhaeE4ePeqf4O4dmEBXekwW38TXbPuw56ANrqy1jEubITLjw74etaad9hmpdZX19MuxQYDg0nnnuq4WC05-qSYeP0hAcdxZTSpX4Lpq-yBejHtjU12rhM_nEMgh17vjY9h1lxpzCskmMfNkBew2A_if5KBN20S475Mg103B7OU0EfKp4NjoZme0ru9TD0g6Q8irJJfkYl3KbQ1vOhAhtPXn7Jg6fcwVXinEkM1guKiWu0E9y9uQ6nOZBkl7cnvxFInxStxYSQCQ8b1MLa5lQVsAx5sGQMiusD8nmw2A1xaqN_Xjljh0UaKtl3Mj-guD6mUYg5TRCnWtYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
از صفر تا صد ساخت آباژور؛ آموزش ساده‌ترین و شیک‌ترین مدل
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 1.32K · <a href="https://t.me/akhbarefori/679185" target="_blank">📅 15:32 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679184">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KXzC6i5SvZzTugyF1wSw-vFLIbOYuXwzFx9gI3BTG_lHC-ktV_N31JaYlG4dt9RKg5PjqLnMmzNPTkeudw3fsQ9n62K8yfYfwdebpacxpQ2pqr9HSBUhCVCDFMW2GF-o2BTKN_JLnfq1KqWtz8k9GHdIw5oIKM4obAOIg_SpqTHr83NvhhkIKAe9CgXs-xUX4P1hnsD8UCDpxka-Vr3UHSmDtao8I02In9GNxRmFqgUmtGRpxElFNOoXskRt8L8Ux0qpPKM4NBCoCu_-cPPAaAc9NGd6YFYPk5PXtl6Y66rcaU-DmUoid53kdkEPsR3ZmCNl3XSjcBXlIi5j0r_zDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
گفت‌و‌گوی اردوغان، بن‌سلمان و شهباز شریف پس از امضای پیمان دفاعی
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/akhbarefori/679184" target="_blank">📅 15:28 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679183">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/785649430b.mp4?token=hvB5zpij57Cy3Nt5zvQCKkrdK_jnxud1x75sR5BTLEJ-q7a3zdxosQsCFj7ndXV_2--qO7hqjrGU8AmgGSGf0Y3UFTo3nuxoiYOqT153xsgH6qsbE15KFpYCFISmvfN-dFQUwZwUVU-RE5CUvLOoJpI12uJ-q6_BdvAplU3NsbVAEiJ86JT92QUWJ8-HWWlJDYLEVRhcXDVtul_f6GhnAdeM85xyFvm2iOammq3n1lKHWMcpr-sv5vWLZbozTB5EWumhbNiP56ZOoKsUp4Yo8A0H3NsY667eyUuB0I30PNBntNJkflFRk5ZJW0_-ExIzAwTGi6NqIxjuPyzXud0Faw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/785649430b.mp4?token=hvB5zpij57Cy3Nt5zvQCKkrdK_jnxud1x75sR5BTLEJ-q7a3zdxosQsCFj7ndXV_2--qO7hqjrGU8AmgGSGf0Y3UFTo3nuxoiYOqT153xsgH6qsbE15KFpYCFISmvfN-dFQUwZwUVU-RE5CUvLOoJpI12uJ-q6_BdvAplU3NsbVAEiJ86JT92QUWJ8-HWWlJDYLEVRhcXDVtul_f6GhnAdeM85xyFvm2iOammq3n1lKHWMcpr-sv5vWLZbozTB5EWumhbNiP56ZOoKsUp4Yo8A0H3NsY667eyUuB0I30PNBntNJkflFRk5ZJW0_-ExIzAwTGi6NqIxjuPyzXud0Faw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رویترز به نقل از یک مقام ترکیه‌ای: توافق با پاکستان و عربستان سعودی ماهیت دفاعی دارد
🔹
این توافق هیچ طرف خاصی را هدف قرار نداده و سایر کشورهای منطقه نیز می‌توانند از آن استفاده کنند.
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/akhbarefori/679183" target="_blank">📅 15:26 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679182">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/883121b681.mp4?token=YT883pyR4zF_74DZ387-1ap6X9IEaYMdcNepwpOZbdu32E-05-_qH3PPjt2A0wL0YeoWJntrhkYcJO7kAD__fOzu9pYyNTnCpHZhH9i2RoK6nY1szlgNqgoo6lTpcVg0ViAHTuQEVrilETjWRc9AErZhcPigEHI9gFpa4d6cCS3CGjVpDDw1yYYig-eHml4ZggPwqMby32slrJ3HbhW1lOgwB7wvqo5bpNUA9WuerB_aPCirqO5kOL3-ESMRQD9LEirz66yRYRME_ZLSj204lZEDwPjbee-IxTeGwLjJACQMhCdM3cB4Gx_W8X1mV800RoGjk4utqEOHrFtJocZ_gg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/883121b681.mp4?token=YT883pyR4zF_74DZ387-1ap6X9IEaYMdcNepwpOZbdu32E-05-_qH3PPjt2A0wL0YeoWJntrhkYcJO7kAD__fOzu9pYyNTnCpHZhH9i2RoK6nY1szlgNqgoo6lTpcVg0ViAHTuQEVrilETjWRc9AErZhcPigEHI9gFpa4d6cCS3CGjVpDDw1yYYig-eHml4ZggPwqMby32slrJ3HbhW1lOgwB7wvqo5bpNUA9WuerB_aPCirqO5kOL3-ESMRQD9LEirz66yRYRME_ZLSj204lZEDwPjbee-IxTeGwLjJACQMhCdM3cB4Gx_W8X1mV800RoGjk4utqEOHrFtJocZ_gg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
معترضان آرژانتینی پرچم آمریکا را پایین کشیدند
🔹
در جریان تجمع اعتراضی علیه دولت خاویر میلی، رئیس‌جمهور آرژانتین، معترضان در بوئنوس‌آیرس پرچم آمریکا را پایین کشیدند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 5.68K · <a href="https://t.me/akhbarefori/679182" target="_blank">📅 15:24 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679181">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/a02b17cd00.mp4?token=Cc8d9xy03uUUbECG0tp9gLh17Bn5INyP-oe236ElB1ShCAg7JG5f3Ht5ZSyzyrl7p42MTGUGUF4KNspiYgONDJ1aV2aVvL9gMEwl3CRR8ip3Ndf2hsSjnnwadtc_vqFIlRlDcja6VrytYIV-QyiIlitjjbb7WZSIfKANfpPbhNyAXfGnSME-Qat3ECZbs6lYU8BBESGk5Q0w0MnR0xi6a1zpyyPdvHUcs0BGcbOo7z_hCGhA8ZbYiCzcXlUxIQvNGLvYhlWDqEuhTTPRSWOjTIXIgi00IDXAuzovNvZYP4uLPWulToSeJdtPoQuHPwfOn58TSgqA5YTlFUiFrUxBJg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/a02b17cd00.mp4?token=Cc8d9xy03uUUbECG0tp9gLh17Bn5INyP-oe236ElB1ShCAg7JG5f3Ht5ZSyzyrl7p42MTGUGUF4KNspiYgONDJ1aV2aVvL9gMEwl3CRR8ip3Ndf2hsSjnnwadtc_vqFIlRlDcja6VrytYIV-QyiIlitjjbb7WZSIfKANfpPbhNyAXfGnSME-Qat3ECZbs6lYU8BBESGk5Q0w0MnR0xi6a1zpyyPdvHUcs0BGcbOo7z_hCGhA8ZbYiCzcXlUxIQvNGLvYhlWDqEuhTTPRSWOjTIXIgi00IDXAuzovNvZYP4uLPWulToSeJdtPoQuHPwfOn58TSgqA5YTlFUiFrUxBJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
انصارالله از حمله پیش‌دستانه به نیروهای همسو با عربستان و وارد کردن تلفات سنگین خبر داد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 8.03K · <a href="https://t.me/akhbarefori/679181" target="_blank">📅 15:19 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679180">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fUSYKw6htpsTkJLfyDJZB6dBcZk7SguWKho4IhIHs2-PsIMDhOus_fY6sk3qIYcytk7y5OrSbrZRavFBvIvy2214_J-IhMNgudZt0j6-I9C4rDw7pa_kHhpp_aXKWe0EVhe0_3zYsTUQRFKgh0PjcOKSPOmb0xnYBxsGdUBvZT6vRuXpGAs90BRHUmEkZDHwHActKs-9CsXly3WXZ_3WPBc3JKsQfBDT7mCIVAJ4Wh0aYTe8aZ9MSqcMZpUbkVvkssCbLLjHXmzNnLKTuUmOxHvUFxE93f2QLH0c-gVFXYBCwzVwRU15GPwEXy_aR3ceDtk269xSGM0ByLHrweNDUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
همسر اکبر عبدی برای اولین بار عکس های عروسی خود با اکبر عبدی را منتشر کرد و نوشت: ۷ شهریور ۱۳۶۵
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 9.03K · <a href="https://t.me/akhbarefori/679180" target="_blank">📅 15:16 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679179">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E2fsZxLM8CIz2MTNrHzNC1A8_FduGCgW20m4fEijdYP_O-hICWsrgynzPgfKhs80S3id_33ZDk8ACBvZ7B57YKbhlL9Blc1e8Q7dzkybJ0ULkt7zQtUTAec9dsFZiuqU57xbpGPEbZ39uFy3wqSv6_VfeU29m_pimVS-fAjhcgNr2UlkSbqWnHwpDp04ny-pCsa-gp35ddX5EceX40rMETg-svpMtqhuVQAZEW-FeOv6_nJGU_nvG0ZB0_W82InA6t147br8cRRUdEMumAJQbyzB8XdWK1iXnNg2BZ4I9Em-U8ZHEuRc5IQ-KwuIq6KZsjTODUF2YwXCypett1e9XA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
غریب‌آبادی: دیپلماسی در جنگ متوقف نمی‌شود، اما ادبیات آن جنگی است
معاون وزیر خارجه:
🔹
دشمن نباید از مواضع ما احساس ضعف برداشت کند.
🔹
انعطاف بی‌مورد، طرف مقابل را جسورتر می‌کند، هماهنگی میدان و دیپلماسی امروز بی‌سابقه است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/akhbarefori/679179" target="_blank">📅 15:04 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679178">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">♦️
چرا قبض آب و برق خرداد و تیر ۳ تا ۴ برابر شده؟  اطلاعات:
🔹
هزینه مصرف آب و برق مردم تا ۳۰۰ درصد افزایش یافته؛ مثلاً فیش ۳۰۰ هزارتومانی خرداد در تیر به ۸۰۰ هزار تا یک میلیون تومان رسیده است.
🔹
دولت باید ساده توضیح دهد که آیا الگوی مصرف کاهش یافته و مردم را…</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/akhbarefori/679178" target="_blank">📅 14:54 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679177">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9f391c287.mp4?token=YDW3SAXpjKimc0PZazz3H-oALlzH1SBqXtzE_2299xfJhqtpxVv9ppi7E1o3VNreblcoo6a4I3sctESfSCUlt_X5gUhunXGpIKdfJ_6K-z5Y8gfGP2SCH3gehmj04thabDeKLvsiLjB010FL71fhfGCyGUApOiiaNf0E2rnW3x78F0lSUDJh7_Scq07V8Pop2dV8oBPdrseaXqssgLEeUBgQ_RzIoS1kL9FzvLTTZ0y4EJBbnjk6kglvhotCwRhBtrFZAzCh4E3m3NUh6lhAAYafPqME8aHztky0mKhCYk7TWWADkXRNTdSK0lT1BqtVJBe2EaDcNsEhm49ZwOAAnaXpH2rcuer6OaPUOoY2gUSFs2_94TvNtvfxXGJN_kEzsRfE84GcQmWSMYGUYKusxid-tARyhCXfn4Fbtz8oUJPCFEYMwvu2eOkZjPvImyKA8aFY7YXIyWbM4Fy8Vw8sW6fXhduGHyqSOMIJB5rujdlMIaQO9M2nJYOTEzYWyk8zPIZ6EtQ__EQ_Oh_UjpDw_QDos4VJyTxZKpecZWKNdiqsVbkXpK8h975j3A7AyTjgL2QWEjdFrOb6I3OxjBkTb4-XsMT01D8gDbmPRGbhQu6YUi_g_4Sbml5mnc2ozcoGM-STfM3cIl6IsDrwO-FqagDPEqhhbrKaVolzInbR3QY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9f391c287.mp4?token=YDW3SAXpjKimc0PZazz3H-oALlzH1SBqXtzE_2299xfJhqtpxVv9ppi7E1o3VNreblcoo6a4I3sctESfSCUlt_X5gUhunXGpIKdfJ_6K-z5Y8gfGP2SCH3gehmj04thabDeKLvsiLjB010FL71fhfGCyGUApOiiaNf0E2rnW3x78F0lSUDJh7_Scq07V8Pop2dV8oBPdrseaXqssgLEeUBgQ_RzIoS1kL9FzvLTTZ0y4EJBbnjk6kglvhotCwRhBtrFZAzCh4E3m3NUh6lhAAYafPqME8aHztky0mKhCYk7TWWADkXRNTdSK0lT1BqtVJBe2EaDcNsEhm49ZwOAAnaXpH2rcuer6OaPUOoY2gUSFs2_94TvNtvfxXGJN_kEzsRfE84GcQmWSMYGUYKusxid-tARyhCXfn4Fbtz8oUJPCFEYMwvu2eOkZjPvImyKA8aFY7YXIyWbM4Fy8Vw8sW6fXhduGHyqSOMIJB5rujdlMIaQO9M2nJYOTEzYWyk8zPIZ6EtQ__EQ_Oh_UjpDw_QDos4VJyTxZKpecZWKNdiqsVbkXpK8h975j3A7AyTjgL2QWEjdFrOb6I3OxjBkTb4-XsMT01D8gDbmPRGbhQu6YUi_g_4Sbml5mnc2ozcoGM-STfM3cIl6IsDrwO-FqagDPEqhhbrKaVolzInbR3QY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تیزر قسمت بیست‌وچهارم از فصل پنجم
🔹
در این قسمت روایت تجربه‌ نزدیک به مرگ آقای رضا معظمی گودرزی که به گفته خود بداخلاقی را نسبت به تمامی اعضای خانواده حتی کودک‌اش اعمال کرده و به خاطر شاکی بودن از زندگی، از خداوند طلب مرگ می‌کند و دچار گرفتگی قلب و جدایی روح از جسم شده و با تجربیات شنیدنی در عالم برزخ و بازگشت دوباره به زندگی دنیوی، تغییرات رفتاری محسوسی در ایشان ایجاد می شود را نظاره می‌کنید
🔹
قسمت کامل این برنامه ساعت ۲۰:۳۰ منتشر می‌شود.
#تجربه‌گر
: رضا معظمی گودرزی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/akhbarefori/679177" target="_blank">📅 14:53 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679176">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
ارتش یمن بیانیه مهمی صادر می‌کند
🔹
سرتیپ یحیی سریع، سخنگوی نیروهای مسلح یمن اعلام کرد که نیروهای مسلح این کشور به زودی بیانیه‌ای درباره عملیات منحصر به فرد نظامی خود صادر می‌کند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/akhbarefori/679176" target="_blank">📅 14:48 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679175">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">♦️
لینک یاب فایل های صوتی گنجینه معنوی کانال
:
🔹
زندگی پس از زندگی
فصل یک | فصل دو
| فصل سوم
|
فصل چهارم
|
فصل ششم
🔹
چله علم و نور  "یک"
،
چله"دوم"
،
چله"سوم"
🔹
مستند شنود
🔹
آن ۳۱۳ نفر
🔹
تفسیر سوره‌های صف
|
مسد
🔹
سنت‌های الهی خداوند
🔹
شرح به وقت شام ۱
و
شرح به وقت ایران ۲
🔹
پادکست کسب‌وکار رادیو کار نکن
🔹
ادعیه روزهای هفته
🔹
برنامه کتاب‌باز
🔹
شرح و تفسیر کتب:
"سه دقیقه در قیامت"
،
"آن سوی مرگ"
🔹
چگونه با عبادت تفریح کنیم؟
🔹
حال خوش معنوی در زندگی
🔹
چله جوشن کبیر اول
و
چله دوم
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/akhbarefori/679175" target="_blank">📅 14:47 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679174">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hTvmH1Jp-ArTZD5sF6shLM-g_yHJKLP7GoBB9xUkbuoU-BPKVOggFa6q3xFZBgVgDZ1bxQGQSXIsm2f3vyOo6Dc_RO8ccjnM7p-T0wUKGJ-idRs3E1Mnkg_MM4qt0BcR1YWH_YnDHoEKWtd9o0WLnyJ4aAarj-uq8oCFxMRnAPJBJM8ycZty6UsSXHhF8CcrkUOqqVOX3Kkv-jtXVEsgfMH2ykN_5f6Z7tQSSPf71CgUBrj6fwlOa9Yw9Y97Z_sSRtySxBMUyCA_tWlpynwGzxmjd7I-yJfZ-cbA0OIGBZe5qvPoWowDWkfEvZ8dbETFZQv7wQBCojPQpwfbVN1uDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویر تازه منتشر شده از صندلی اف۱۵ سرنگون‌شده‌ آمریکایی توسط پدافند سپاه پاسداران
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/akhbarefori/679174" target="_blank">📅 14:36 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679173">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f7102a082.mp4?token=IjxgTXKgw-LauEAUU3iukblCGCJD8zYTeR40sNRhJ76Hl6Nnzt7vUkapSLAHn2PmGPJPefdV_IWb0roLi7-FshHsscFToje2QtQgQpwITVYdPmq1mD0PNNN72KuLk40qX8bDqni8S965Q4YkEqJC10Z3hbw8kTZmtpwG1aXVfPVQVviBqzzeENjv2cXaIDYh6SrwxK3DNwCL1XVP_NS-d9PGbPj4Q-g5JPrgQTYS0Jp7SNVOdOcr_m8HuTRcTc7j5oyEuqepzaj9GGxuepxk7aZNM3WQrEACfX9qUJARE68QnPZq0BaUOTmMICwTb7gHTai8uAxTo4x20YxfDW0oJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f7102a082.mp4?token=IjxgTXKgw-LauEAUU3iukblCGCJD8zYTeR40sNRhJ76Hl6Nnzt7vUkapSLAHn2PmGPJPefdV_IWb0roLi7-FshHsscFToje2QtQgQpwITVYdPmq1mD0PNNN72KuLk40qX8bDqni8S965Q4YkEqJC10Z3hbw8kTZmtpwG1aXVfPVQVviBqzzeENjv2cXaIDYh6SrwxK3DNwCL1XVP_NS-d9PGbPj4Q-g5JPrgQTYS0Jp7SNVOdOcr_m8HuTRcTc7j5oyEuqepzaj9GGxuepxk7aZNM3WQrEACfX9qUJARE68QnPZq0BaUOTmMICwTb7gHTai8uAxTo4x20YxfDW0oJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری از پهپادها و جنگنده‌های منهدم شده آمریکایی توسط نیروی هوافضای سپاه پاسداران
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/akhbarefori/679173" target="_blank">📅 14:30 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679171">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NHHmCUrmTZmR3cvk-oJhLjYLQrXt6wn9a1wSS0IMXr04GdPiv9ErF-XXx6vh_7v0_I8POqXuUm6Isw8al2v9_-UXRnvSmk7d0VfJx_5Mqg-vGS0kfhqozmpccn1vIIhGSn8vBBmwGldtlpIhLrs4-_0ppudqs35X3BLeWr2lgSkBwgFasWjFN5ZvWnTtNqyROt5bi_4k8zl9fHyahMWRbQPB6YBgXZzMKdv3e9v24MR-Qq0Q46Id-P5PR-lTeNJlOKcp1aTjyzr5_uQFN2Ne4UfM1-cLSmV5r-UJefwS_jUItuunE89hXNCchEfYW8Of0TFwNOSpf9myZ_M3rx4SPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای العربیه: عربستان سعودی، ترکیه و پاکستان «توافق‌نامه دفاع مشترک مکه» را امضا کردند  توافق‌نامه دفاع مشترک مکه:
🔹
هر گونه حملهٔ مسلحانه به هر یک از کشورها، حمله به هر سه کشور محسوب می‌شود.
🔹
هدف این توافقنامه، تقویت بازدارندگی جمعی در برابر هر گونه اقدام…</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/akhbarefori/679171" target="_blank">📅 14:18 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679169">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HK3yydbxkbqUPtzWxWAzY4hM2On5mLe3-WbrSuA7b_ai8SLFk6LLJxxrXqnL2KoIm9DqC2P2p6O0wzp0p80h2N3Ft2NKtR278NrkDbh_hHRUDSu1nHJS7YY3bykuBjGPE1iqs7SBSj7hBtrwGp2oitX67Ma_rIYG8fAIOIOTczpZNXJrrjZxpCHSsIOEU_HUvxb5q94A9AtyhSkykIPMfPcVMAFIjalXzCQ_xcztpSrYgpU87FXDqM1RZpwMv-SzjcbFr93haI3nVe5xy_uyAPOIDqqKgNKk8oR5o4zrYCIsl5iEoB2hrUArKWSbbAWLh5VceiJCl3hVGkJF6Cz1OA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iKgPI5kuVy9yMSK0QLzbzZ_60yCVtW5qHxX2A6XoZj55XP9CLK_nNqgdDjYBOqeqfIod6mNBel4P40uFzy7Vi67gmOTqsCsVGangUU0Ng_v2VqdWoTX_IHXPzlLmq2xSvcTx0hb2QTfP1JJJZ0wPeD3uYu75y_1DebvwGuokDA7eWIrmUPmlI0tnAXxk6UuXxUcTU3H_WsLbI_3XT1TJbr80ZHslTWYSL1eQpo5Y14qnnAfnWhLlSzw0UApp8zidV0wbWK0NvMInkECsfTjWscXkgDn6-O6B7m8wq0U8vD8gpUr6hTIUU-s1o4UXSWch0_duydQoV4bqSc_XqLYTiA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
کوچک‌ترین گربه وحشی دنیا را بشناسید / کُدکُد؛ شکارچی مینیاتوری که نمی‌شناختید!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/akhbarefori/679169" target="_blank">📅 14:13 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679168">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uYBJixopkVGzJwA_T-eCFUhXnlfhbY7BB3ZaRw4mQKkbuGK0PayUB3QIszlX6C50cvtFjQ8Xj1NaCNQNpKQIpVteAYdmEk2PpIglJTbwdJxps89xbsMSs3pHsq2RuHpIP_RNmVS6turqeAjrSq9Hc7YFzMJtD7IokzzDWuO41Y89IkVcKIuDc7FppVTe-eOkaMqAEuaP32Ch82euK1sd29foCeTR7_GT7ghKc_LOgx0S4jOWi3HkdjGlqq3buL7jYXDO2A3Qk310he9yX8hAqQq1Q4JfwQGZ93iPVlojt4PcRN_Mgp0A8VPzuS9irHCG7Istzg8vJx9P-4TBqjMjQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اعلام برنامه‌های هیئت قرار در دهه آخر ماه صفر
علی جلالیان، مسئول هیئت قرار:
🔹
هیئت قرار که به همت کارکنان خبرفوری ایجاد شده است، همزمان با دهه پایانی ماه صفر برنامه‌های متعددی را برای خدمت‌رسانی به زائران حضرت علی بن موسی‌الرضا(ع) تدارک دیده است.
🔹
این برنامه‌ها شامل برپایی موکب پذیرایی از زائران پیاده در محل تپه سلام مسیر ورودی به شهر مقدس مشهد، پخت ۲۲۰۰ پرس غذا در روز شهادت امام حسن مجتبی(ع) و رحلت پیامبر اکرم(ص)، آماده‌سازی ۸ هزار ساندویچ برای توزیع میان زائران و همچنین برپایی موکب اسکان زائران در نزدیکی حرم مطهر رضوی با ارائه رایگان ۳وعده غذایی(صبحانه،ناهار، شام) است.
@Heyate_gharar</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/akhbarefori/679168" target="_blank">📅 14:07 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679167">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LCbNJ7sL6RmBtzDYORS90w2iLq92W1PFXwSW8bEdAe-Rhm5bcm0UMkNlCywWveRp9OyQJ_W7QwRZSCSg0-RrXbaXe_O50TBz8nPp44425FfU4Pi0bwGIaNd-bA2LxZupeOFp39A1th0VvUoPggI1ZEkwoq1OZ8OLz7Jb3Nt8-hfZOL65OQE1CmJD-MoxywRdqL1ISi7VOur_KWoxasHVhMngm1ehKXWISen9lOWu_GorKOoQze6VnK_HVCrmuUUrlrdZpJ5z_5SymWYGuzdC7PaNU65YMS2iiApxuFXQbnG98YfKi4qAjQ06HAVrPT7d0VElBD0NSOPl7KF16-cArQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
«توافق مکه»؛ نام پیمان سه‌جانبه نظامی ترکیه-عربستان-پاکستان
🔹
همزمان با برگزاری نشست سران ترکیه، عربستان سعودی و پاکستان در جده، گزارش‌ها حاکی است که پیمان دفاعی سه‌جانبه‌ای که قرار است امروز میان این سه کشور امضا شود، به طور رسمی «توافق مکه» (Mecca Agreement)…</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/akhbarefori/679167" target="_blank">📅 14:07 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679166">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/150a2c1bf8.mp4?token=FpeOiJvV9Wc0cNit9xtM7HWCoWsppOPo0uT3sE-0jI3vv3WGRObq6_LbQGbkoJPcFfpN20-4djeh5_AfJwjoqJCj_c365HFU6Hac4xFFVjqlbMD25iOkH3Za_ydEx4y2Z5DI8oxiAkLcgAskr5GgLu8xtfgYZM0eevx1xa8LYjOMf1MaCS1J03mqr74J-BxFIpSQPpDVA2I9AXfpaH9W8vSTA6PZV_-Qzkf-gli4-qEyaFr4iPCRgL_jW5095K1gQIETYQPnjvHtAmyElknSiKd7pOeu7pHB2N6CqFRsP02pQs4alo9p6XSYZcSQgWcXnApJiBBto-fuayRujGI0QQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/150a2c1bf8.mp4?token=FpeOiJvV9Wc0cNit9xtM7HWCoWsppOPo0uT3sE-0jI3vv3WGRObq6_LbQGbkoJPcFfpN20-4djeh5_AfJwjoqJCj_c365HFU6Hac4xFFVjqlbMD25iOkH3Za_ydEx4y2Z5DI8oxiAkLcgAskr5GgLu8xtfgYZM0eevx1xa8LYjOMf1MaCS1J03mqr74J-BxFIpSQPpDVA2I9AXfpaH9W8vSTA6PZV_-Qzkf-gli4-qEyaFr4iPCRgL_jW5095K1gQIETYQPnjvHtAmyElknSiKd7pOeu7pHB2N6CqFRsP02pQs4alo9p6XSYZcSQgWcXnApJiBBto-fuayRujGI0QQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قشقاوی، سخنگوی کمیسیون امنیت ملی مجلس: چهارچوب کلی تفاهم با عمان مشخص شده و به زودی متن نهایی و جزئیات هم بیان می‌شود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/akhbarefori/679166" target="_blank">📅 14:04 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679165">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F_OkTvNIi_4JzAZs0OMkIYd78vpWo_RtVRNWWXb5RQg4BrnVVz4LRhmLNfAFbVIRyJREzouOgGFplQd5ZdcEp1mJNOKlFekfjDX5sFZUXvw9IuhdKscM5SctGH9TguUTuuekRsO1nb9y1jMpatinQlWUixG7m_2edRfQp7QZ7BW-SQSCuLwTbSDdzaAHwif88H1TeJt0qMMoFgYO8ozkB4x90jkF2BirmY6RrqpWQXJ8YjmjLtR4Blpc2TdhOxfjK1Ghh1Q2uVZKpHDrcqKoCOBMXmOg9sUuijtCW-2rLrFOTzpJYLYeS0RvfPJICj3yReaPKdIoYpNt7AUVCjzomw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
خرید قسطی طلا تا ۱ میلیارد تومن از ملّی‌گلد
فوری، بدون نیاز به چک، ضامن و اعتبارسنجی
با سرویس خرید قسطی ملّی‌گلد،
می‌تونی طلای مورد نظرت رو همین امروز با نرخ لحظه‌ای بخری و هزینه‌ش رو در بازه‌های ۱۲ یا ۱۸ ماهه پرداخت کنی.
✅
بدون چک و ضامن
✅
بدون اعتبارسنجی
👇
برای مشاهده شرایط و شروع خرید قسطی، روی لینک کلیک کن
🔗
شروع خرید قسطی طلا
🟢
ملّی‌گلد؛ پلتفرم امن خرید و فروش آنلاین طلا و نقره</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/akhbarefori/679165" target="_blank">📅 14:02 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679164">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YyH-Gc6yoVCJqGJhXlgFeVOsTMWK8l1x-Rt-etSurXi0xIR3Kwiu5wvvb9a6ZmpX0o8_p8lwBKM9LOHQNNyOkFQWnbIGJ1MRDomSt-A4PC7SzpMaeOSftwn5tMzuyYQN8YUZRbyQnW4Ig6mBdRt3QJVvh5VzthCnfbtjgrvSy8TOTpXwYPGPiwlJ14sTbQkYq4oXmvfC6lJRIgXJM38MTgkpvZbw7SbOrsHwwNwrTBSyw7UsgZRZUoFO5BWEufpOGNELM5wd8zG8p8lkIQnoq2n5ED0anDRQYTfX1kqEgCnPSbWNWWed73B49ejB4U1kS0i3eqxt1TTe26vw_MFtQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بازداشت مردی که با لباس عزرائیل به بیماران بیمارستان خیره شده بود
🔹
مرد ۲۶ ساله‌ای که در ولز با پوشیدن لباسی شبیه به عزرائیل و در دست داشتن یک تیغه بلند، به بیماران و مراجعه کنندگان به بیمارستان خیره می شد، دستگیر شد
🔹
وی در دادگاه مدعی شد که لباسم شبیه به کلاغ بوده نه عزرائیل!
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/akhbarefori/679164" target="_blank">📅 13:57 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679162">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
الحدث به نقل از منابع آگاه: واشنگتن از طریق تماس‌های مکرر به اسرائیل اطلاع داده است که لازم است تنش‌ها در لبنان کاهش یابد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/akhbarefori/679162" target="_blank">📅 13:55 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679161">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04bfdcecbd.mp4?token=ReThIQRB7Tw4r0PVCJ_kq3knEEVLyM2Eoyf9F_rI2rGs3vU-9JOVUl-XlIpU7kao0cLqco9re9v_NxUH4sWrvQSQpMpOI_JBUtXsTFpo_XSz3wFBwy2b8mwJzXgSIHlZw6_Tb2yY67bJfBXvPO11FsKwjPG_2fGg1GCRnVqjvVPGg_98oGKluRRlbyaWFOBRa5gsyHvbIkQYM71vVg-cqWTEOhKS0qXDqC36FGN9ItDQjHQLMLx2IFG2xPwVLuvEo5qWDjmikEeFwuHoqUjUw4Gu5DPt6DpR2CwhvyYAbv4xK98xi-FXOiryVVG9njWqAwdqnVBhBXd06r-S5UCqzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04bfdcecbd.mp4?token=ReThIQRB7Tw4r0PVCJ_kq3knEEVLyM2Eoyf9F_rI2rGs3vU-9JOVUl-XlIpU7kao0cLqco9re9v_NxUH4sWrvQSQpMpOI_JBUtXsTFpo_XSz3wFBwy2b8mwJzXgSIHlZw6_Tb2yY67bJfBXvPO11FsKwjPG_2fGg1GCRnVqjvVPGg_98oGKluRRlbyaWFOBRa5gsyHvbIkQYM71vVg-cqWTEOhKS0qXDqC36FGN9ItDQjHQLMLx2IFG2xPwVLuvEo5qWDjmikEeFwuHoqUjUw4Gu5DPt6DpR2CwhvyYAbv4xK98xi-FXOiryVVG9njWqAwdqnVBhBXd06r-S5UCqzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ جنایتکار: اجازه نمی‌دهیم چین با رمزارز و هوش مصنوعی دنیا را فتح کند
و پیشتاز شود؛ این دو حوزه برای آینده اقتصاد و فناوری حیاتی‌اند
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/679161" target="_blank">📅 13:49 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679160">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
ثبت‌نام کارشناسی ارشد علوم پزشکی ۱۴۰۵ از فردا شروع می‌شود.
🔹
نشست خبری پزشکیان فردا (روز خبرنگار) با اصحاب رسانه برگزار می‌شود.
🔹
وزارت دفاع روسیه از کنترل بر شهرک آنیشچینی در استان خارکیف خبر داد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/akhbarefori/679160" target="_blank">📅 13:43 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679159">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">♦️
نتایج تحقیق روی ۱۰ میلیون فرزند: ترتیب تولد بر بروز بیماری‌ها تأثیر می‌گذارد
🔹
فرزندان اول: بیشتر در معرض اوتیسم، بیش‌فعالی، آلرژی، آسم، اضطراب و مشکلات مغز و اعصاب.
🔹
فرزندان دوم: بیشتر در معرض میگرن، زونا، سنگ کیسه‌صفرا، التهاب معده و سوءمصرف مواد.
🔹
از ۴۱۸ بیماری، ۱۵۰ مورد به ترتیب تولد وابسته بود./ دیجیاتو
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/679159" target="_blank">📅 13:39 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679158">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e47a188ac5.mp4?token=XwqSPpGZJieENBwOo0YE0PEzzmJLC30slm1Zvcr__r_uoVXcrIljszK0ENdEU5HJ-Dcqhqf2gIfLwYMx0u8oX3pEm0aIEsbcu6emBvOZlpqIk2KOcCm5Ds-3bfHHp_BqdxlMMJJnDcmILNs8K1CfhNFKmjBjcCAs0F9A4k78hmF2Vls_z10H-xzbteba11jNC_Ywwo_b4KUgtfXonqWRzFZGfQsaFn3NSsJiGf3sNv-VClaftGQRlV7l5LMekQzKr_S7CWUQaT2bDl0DynBa7M_pHR6grFvVVNjxbUfoTJUjYCLoVWsCPoC5x16pMzm34CJG-vh6mwcEyqRAJYOmWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e47a188ac5.mp4?token=XwqSPpGZJieENBwOo0YE0PEzzmJLC30slm1Zvcr__r_uoVXcrIljszK0ENdEU5HJ-Dcqhqf2gIfLwYMx0u8oX3pEm0aIEsbcu6emBvOZlpqIk2KOcCm5Ds-3bfHHp_BqdxlMMJJnDcmILNs8K1CfhNFKmjBjcCAs0F9A4k78hmF2Vls_z10H-xzbteba11jNC_Ywwo_b4KUgtfXonqWRzFZGfQsaFn3NSsJiGf3sNv-VClaftGQRlV7l5LMekQzKr_S7CWUQaT2bDl0DynBa7M_pHR6grFvVVNjxbUfoTJUjYCLoVWsCPoC5x16pMzm34CJG-vh6mwcEyqRAJYOmWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هر ویتامین برای چه کاری مفید است؟ این ویدیو را از دست ندهید
💊
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/akhbarefori/679158" target="_blank">📅 13:37 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679157">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc87a808aa.mp4?token=Eci-_k4VbLRCGsj7SkoBEOtGjJ8ZUWIgt9KQqdCLukO98j9BZfK01wd0ASE6ugDzktV67-izyTx6lWADlBI1-fFzuWB-fjLKTHrpjDmNRLcr4hyOBWXQwpxpM89BMJNYf8tb-Dr3wD42SSmTMBkZi6PiqS55OlygtS-aVBDOu8HZBg6pqAhWpbmT5T3Gto8OA3YuDJwK_Qp9kRfUMHNEiOopi04g-uTAfLcy7xCut7he4pUOTiiVCBIgeRG03kYEuS8uewnVn_z3QEGbWHwfbo0gEqcQFVB9B1as4pdMA-taQq4iAVOk4wZUOhcGfH6QNTV_CxyS36rJMbnnAoLoiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc87a808aa.mp4?token=Eci-_k4VbLRCGsj7SkoBEOtGjJ8ZUWIgt9KQqdCLukO98j9BZfK01wd0ASE6ugDzktV67-izyTx6lWADlBI1-fFzuWB-fjLKTHrpjDmNRLcr4hyOBWXQwpxpM89BMJNYf8tb-Dr3wD42SSmTMBkZi6PiqS55OlygtS-aVBDOu8HZBg6pqAhWpbmT5T3Gto8OA3YuDJwK_Qp9kRfUMHNEiOopi04g-uTAfLcy7xCut7he4pUOTiiVCBIgeRG03kYEuS8uewnVn_z3QEGbWHwfbo0gEqcQFVB9B1as4pdMA-taQq4iAVOk4wZUOhcGfH6QNTV_CxyS36rJMbnnAoLoiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اظهارات ترامپ شیاد درباره ایران: آنها می‌خواهند به توافقی برسند
🔹
آنها می‌خواهند به توافقی برسند. ببینید، واضح است که آنها نمی‌خواهند مورد حمله قرار گیرند.
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/679157" target="_blank">📅 13:30 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679156">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromچِشم به راهیم</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f5a76ab56.mp4?token=N4kyn6TkvoE15Pd_Q8a269o4B86rltz0_UwhhSnvCDMioOYMPfw1VrQvr2C7dEW1rm6PAJUvI-Sk7KHc7Xe3O2McbDMlp-X8ERhwAbV5IMPtu0iNguLnqaURlHxPBS1DjWhHXUOMeQ6Lh7CX7Ft3bDtEr97NNcGe9TX3nAJcs98igLLRLVUNcj6RCAr2TiOXx32Kgi39nMQLQmmYbkiXjdKlcjw_HHXWzlxMa0_5Xtd4R37SJF3JWM6wBX66t_DcN6-r77SVhtQrRsavjH4yZLB8-2G-8I7CuwKD7c1aXuaWgDgR231jBh466nQxPnZ5ahiwXXDduwQEQ_slF718-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f5a76ab56.mp4?token=N4kyn6TkvoE15Pd_Q8a269o4B86rltz0_UwhhSnvCDMioOYMPfw1VrQvr2C7dEW1rm6PAJUvI-Sk7KHc7Xe3O2McbDMlp-X8ERhwAbV5IMPtu0iNguLnqaURlHxPBS1DjWhHXUOMeQ6Lh7CX7Ft3bDtEr97NNcGe9TX3nAJcs98igLLRLVUNcj6RCAr2TiOXx32Kgi39nMQLQmmYbkiXjdKlcjw_HHXWzlxMa0_5Xtd4R37SJF3JWM6wBX66t_DcN6-r77SVhtQrRsavjH4yZLB8-2G-8I7CuwKD7c1aXuaWgDgR231jBh466nQxPnZ5ahiwXXDduwQEQ_slF718-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎦
۳ روز پس از اربعین/ پایانه مسافری برکت در مرز مهران همچنان پذیرای زائران
🔹
۱۶ مرداد – ۹ صبح
🔹
تازه‌ترین اخبار و ویدئوهای اربعین را
اینجا
دنبال کنید
#چشم_به_راهیم
#اربعین_حسینی
#سازمان_راهداری_و_حمل_و_نقل_جاده‌ای
🌐
rmto.ir
🌐
141.ir
@Cheshm_Be_Rahim</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/akhbarefori/679156" target="_blank">📅 13:29 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679155">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f8105dbeb2.mp4?token=teKhNWTOLrAQVRtz9H1k8-q6G64GWmp4UsSSAq6X77PBE7bnjhTthKMALt-4YnRjefKFAOJwXWkIZK-KRxibMdOv3l08liPtJbihyUiP2gXUelVOaMC6sT3_fPN0sTpWymkATCBLg-k6SbLlBihZpDtJd4QBBv1fuWO2EUdCwUCj141tDTYOci7CpDT9Hg7WGBqlcRas174IR9KKdsZX9Ug9G5Z5FIuRwYSEm4sxgyg7AhUqFX4GfiVmZ3dXHuBxSOQOuG9iHi-XxE1M_wc44R7P4vW_eMmeF87OzbOPWR86k5Z6EgkowZBrmKTDabQNyPaTsxn7NSXhJRsXeD8ZNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f8105dbeb2.mp4?token=teKhNWTOLrAQVRtz9H1k8-q6G64GWmp4UsSSAq6X77PBE7bnjhTthKMALt-4YnRjefKFAOJwXWkIZK-KRxibMdOv3l08liPtJbihyUiP2gXUelVOaMC6sT3_fPN0sTpWymkATCBLg-k6SbLlBihZpDtJd4QBBv1fuWO2EUdCwUCj141tDTYOci7CpDT9Hg7WGBqlcRas174IR9KKdsZX9Ug9G5Z5FIuRwYSEm4sxgyg7AhUqFX4GfiVmZ3dXHuBxSOQOuG9iHi-XxE1M_wc44R7P4vW_eMmeF87OzbOPWR86k5Z6EgkowZBrmKTDabQNyPaTsxn7NSXhJRsXeD8ZNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بلاگر آمریکایی: بیشتر عمر به من گفته بودن باید از جاهایی مثل عراق بترسم، الان در یکی از بزرگ‌ترین اجتماعات مذهبی جهان هستم و همه چیز کاملا برعکس بود
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/akhbarefori/679155" target="_blank">📅 13:27 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679154">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qb7ng9JypbxotOkjO8wMAxZVltSSiFlTd9AgDZ7sv-G5zfUEz6UpwvydtD2-CtsNlVkf_D3sCvtYx1AzO89WB5ZQFXKvv-GPe6s7XTiSAksP-xupqCk5luCQPwNvpFbYOc61GH8pGGufeXRT6KZ3cWIiUE-oC1OQNTX3Rn0d9x_3eGGAPZn3TF-R_Q-lrUKjbH5NyWJ0qTNYh8nKXxYMqLF0PSDVVw-AParPAWXIjmV9bEKjeQ9xBjYI7WdUSZVMMywtV7laYSrPnzt27_uz7fFmuIbPH2_qP2PlBWOlAsMdZ5Xa3WuHXi7u0_GQl0zkSHGxMMTWUBnSLtffJ7TQyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بلومبرگ: ماهانه دستکم ۵ فقره خودکشی در میان کارمندان فرماندهی سایبری آمریکا، ثبت می‌شود
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/679154" target="_blank">📅 13:25 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679152">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZurXuxHgQLpJm4oiyA3vBB4TTsrS_XDde1KTM-lLYyhA00FvTZEvQNGFUTtkBNglu-bqY0Rb-lY8iZL-o6eVu-h0b4NG3Gl3RuC2igydIFtcEmUwojnsNLwbFDhFiQT4_uqlYe5sRctAoI2NwhkxU6pGA-cFNeSiTCnKEZQG9qFlKzauddbfdkXsnj8YL5CiIK-sWhlGcPwJUUAoSb9TKtlKmLpWj7PuiYHIG4U7qYJwjWY_kbRSYXvBb3oAvFh8e28d6fMhhUZK_KlT4anuS2Tt_sI6I0E_nVuUwBRFBdmt4BEuZkEGHkP5e6txKa9qDF-LTetfLgYsI-pg6QnIkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uv-XQ5HnPJoyaKADsB-gUZTkfPtX6mquRsH-p3K6mpWtD4u7LxeEaSscLYEvVwI397uDfDr5HhYIEr4leuSgHtVfZuv_SdHSSXcIl0aYzzBVPN5alZRMACa4Qh--FECbkYFPp1v9g0JpN09FfmxSPkF8CrD1LYYvY2wePoZSNnzZIRx3PJecBsNQm4ARW9uLFNdBORODCCzATapu-Eb41STYFJf80PNYMElsscjF9VIkHRE7OAynihDNqSpUuOZN5iEqVyYraY7pNatrXQoeqc5EwfLuEpbr14KYk_AGzRau7_i_jUQ4uWPOY1mJO7a6GxTSIDMlZJDSfCjbHNA46A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
تصاویر هواگردهای منهدم‌شده دشمن آمریکایی-صهیونی توسط سامانۀ پدافندی نوین هوافضای سپاه
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/akhbarefori/679152" target="_blank">📅 13:24 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679151">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YbfvMi121UXV80QZzwoqB3AIa8RR_IM0EkvpbQyyxx433cnImfSdbg0_go53dLkClmHQ8wbgjpvKb896rIS7sqj14ju5bVyiZVYCS6uhIzNkqACdP4N76bfOH-M2SzO9ckddyIQGVh6gIcvqbFIwA8V-nKKigPkOMP979m3egGuwXXqj9PzjRZO5qItiiuPcbgDwWw__aqt5dWbluS7y6T-JFHZ7R4-9ZtEhuc2DRGbqC7LfCfeeBW5Z5dMDNN4h0OhgOHWmEQ9QQS2m4WvQBsgeacL68301zMibeETb8WGk6E02bIx3stdJ0YevNpfowgx3Dl6lUU33g0u3u0kWgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
چت متنی داخل ChatGPT نامحدود و رایگان شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/akhbarefori/679151" target="_blank">📅 13:12 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679147">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a8332585a.mp4?token=TZqFpIDeYvG7Md4mPq7DLS1cAydILUAwJHNdO8f9Z2QRgPGYoJiofheGwih2MCX6m2yxO2jqQod93JJfiu1dvP0OqMfOWwZg9saqMvLuOFjcxQhaSW4Q2TVnwBhQc1-cMwDC2vBSKmXiyL0TuqTHBI9JQvZbGZZZEApDD21jh4sAy5SUiUpv0v3BHR8IOJ2h2IsIMFr3PvqRW-skC_YviRnVMHfknfJy9PBsPCV5w93s2lL_u1p0asN6ho0T0O4_zXZB3FXDP1cDkx9aUVZQYxeZQfG4R7-QH0EXi_4vWum4WXtiFhPRJG1OtbDHaqBOIe0uTvQ_RQtLVm8weOaqIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a8332585a.mp4?token=TZqFpIDeYvG7Md4mPq7DLS1cAydILUAwJHNdO8f9Z2QRgPGYoJiofheGwih2MCX6m2yxO2jqQod93JJfiu1dvP0OqMfOWwZg9saqMvLuOFjcxQhaSW4Q2TVnwBhQc1-cMwDC2vBSKmXiyL0TuqTHBI9JQvZbGZZZEApDD21jh4sAy5SUiUpv0v3BHR8IOJ2h2IsIMFr3PvqRW-skC_YviRnVMHfknfJy9PBsPCV5w93s2lL_u1p0asN6ho0T0O4_zXZB3FXDP1cDkx9aUVZQYxeZQfG4R7-QH0EXi_4vWum4WXtiFhPRJG1OtbDHaqBOIe0uTvQ_RQtLVm8weOaqIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
انتشار ویدیویی جدید از مرد درختی، شهروند ۳۵ ساله اهل شهرستان خاش
🔹
عبدالنصیر که به بیماری نادر «اپیدرمودیسپلازی ورموسیفورم» مبتلا است، می‌گوید: «من هیچ‌وقت صحبت نمی‌کنم. ۲۰ سال خودم را به کسی نشان ندادم. دوست ندارم مردم فکر کنند قصد سوءاستفاده دارم.»
#اخبار_سیستان‌وبلوچستان
در فضای مجازی
👇
@akhbar_sob</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/akhbarefori/679147" target="_blank">📅 13:02 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679146">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">♦️
صدای انفجار در پایتخت روسیه
🔹
صدای انفجار مهیبی در مسکو و حومه آن شنیده شد.
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/akhbarefori/679146" target="_blank">📅 12:56 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679145">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b728ef516.mp4?token=e6DcjR-0CgstPS2z-lYoxRM8Xee4cVe-oNfLkU297za2UfeYlO9ilonXW09_FCxBoPiTKh3mGd6Blb_eVmSjgRy1NINOekg3ruYBMgv1LUsnmO1qHaA9SXWhoBSEuIzkQczg-Wkwk7nYKnXuxzSCi-1A88yubLC-1EZmffKcM4KjEw8nHGkvI0KjUSUGzm1NSGRm9eKKWgSFmypC3X34FZSBgt2LsoF5XvKlQ2zwcahJBEJIPSlchfaCFY051PziqhxCBjuZkWvtRK6GHrNBUJdrGQJR4zncG-f-edfaUD_voarEiZ4LammoOpFRNQCKLM9Jep8mKntq5y3FkcxA0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b728ef516.mp4?token=e6DcjR-0CgstPS2z-lYoxRM8Xee4cVe-oNfLkU297za2UfeYlO9ilonXW09_FCxBoPiTKh3mGd6Blb_eVmSjgRy1NINOekg3ruYBMgv1LUsnmO1qHaA9SXWhoBSEuIzkQczg-Wkwk7nYKnXuxzSCi-1A88yubLC-1EZmffKcM4KjEw8nHGkvI0KjUSUGzm1NSGRm9eKKWgSFmypC3X34FZSBgt2LsoF5XvKlQ2zwcahJBEJIPSlchfaCFY051PziqhxCBjuZkWvtRK6GHrNBUJdrGQJR4zncG-f-edfaUD_voarEiZ4LammoOpFRNQCKLM9Jep8mKntq5y3FkcxA0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شیب پیست نسکار واقعاً چقدر است؟
🔹
شیب جانبی تند پیست NASCAR رو به بالای لبه بیرونی یک پیچ است و نیروی گریز از مرکز را در سرعت‌های بالا خنثی می‌کند. این زاویه از ۹ درجه ملایم تا ۳۳ درجه شدید متغیر است تا به خودروها اجازه دهد با خیال راحت در پیچ‌ها با ۲۰۰ مایل در ساعت عبور کنند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/akhbarefori/679145" target="_blank">📅 12:47 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679144">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">♦️
صدای انفجار در پایتخت روسیه
🔹
صدای انفجار مهیبی در مسکو و حومه آن شنیده شد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/akhbarefori/679144" target="_blank">📅 12:42 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679143">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">♦️
تنگه هرمز عربستان را وادار به تخفیف‌دهی نفتی کرد
🔹
عربستان نفت سبک خود برای فروش به مشتریان آسیایی در ماه آینده را با ۲ دلار تخفیف نسبت به شاخص عمان-دبی به فروش گذاشته است.
🔹
این تخفیف درحالی اعلام شده که صادرات نفت این کشور به آمریکا بعد از ۵۳ سال صفر شده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/akhbarefori/679143" target="_blank">📅 12:40 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679142">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">♦️
تشرف سران پاکستان به حج
🔹
نخست‌وزیر پاکستان شهباز شریف و فرمانده ارتش این کشور عاصم منیر، به همراه شماری دیگر از اعضای کابینه با حضور در مکه مکرمه، مناسک عمره را به‌جا آوردند.
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/akhbarefori/679142" target="_blank">📅 12:32 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679140">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e3b532a75.mp4?token=VujUZvZrpIMnjxSRK83x2FBIxHqYzTLOekA15QeIYnWeegexzC8gvCGGkPmtr8RyQP_hm2oVb37Dvhci989O6ziQhwbmSzXd8AeNGVkivrwH6WPCk3MjU6I6GxTDbjpojlOisVcHaGA8c3lisXhRNUfQW0k_A-9QAUf7WDRKJTyVxNq3pM1i6feLHhhm-egWyXM1yLAk-SmD97wATK-hYe-AcAR9YydBLOh45wXDrhNQeCkZrXSjOOK5FhdfI6nXJHhg5jzc_JoWa1NSzxK3WxnEI0iudtftJrBfTdJj4XmWxP2RyNtZ-KHfRY1jWum7-5XXA4gZIEtFkTEbGeg5rA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e3b532a75.mp4?token=VujUZvZrpIMnjxSRK83x2FBIxHqYzTLOekA15QeIYnWeegexzC8gvCGGkPmtr8RyQP_hm2oVb37Dvhci989O6ziQhwbmSzXd8AeNGVkivrwH6WPCk3MjU6I6GxTDbjpojlOisVcHaGA8c3lisXhRNUfQW0k_A-9QAUf7WDRKJTyVxNq3pM1i6feLHhhm-egWyXM1yLAk-SmD97wATK-hYe-AcAR9YydBLOh45wXDrhNQeCkZrXSjOOK5FhdfI6nXJHhg5jzc_JoWa1NSzxK3WxnEI0iudtftJrBfTdJj4XmWxP2RyNtZ-KHfRY1jWum7-5XXA4gZIEtFkTEbGeg5rA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دلیل اینکه ساختمان‌های ژاپن در زمان زلزله فرو نمی‌ریزد، مهندسی ساخت آن‌هاست
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/akhbarefori/679140" target="_blank">📅 12:20 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679139">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d59a91566f.mp4?token=TWW6SqVtEta2MHsXPYvqoWaUi_0pE2DEvK1-Z_vkE99H47WJVLS4c9rImUNvwmTx6CVeXT-V_n9ued8ZIlC23hc1OZ7-mQQ96jj1stxPKDVUdwXEUNFdH1cD0KJ7QeDD3UlD0AVAironTVFjeHXFVHck_H1MgFhZzN85Fk2kYhAjR0fal5i16Wxk23au_-BXDIDEtwM3W6B3V1EqzrPw1N0mP9xy5XF5BLPLjst7vw8EiHNjqWt277KmIBDPDg99uKw75ef9bxi_h-3cz6eyaTfkiG3y6IsQ2BeJYo8AJsNJ5altPdE5Zwxyis13VWqlXNnyPczv02zTp7oOqzOzdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d59a91566f.mp4?token=TWW6SqVtEta2MHsXPYvqoWaUi_0pE2DEvK1-Z_vkE99H47WJVLS4c9rImUNvwmTx6CVeXT-V_n9ued8ZIlC23hc1OZ7-mQQ96jj1stxPKDVUdwXEUNFdH1cD0KJ7QeDD3UlD0AVAironTVFjeHXFVHck_H1MgFhZzN85Fk2kYhAjR0fal5i16Wxk23au_-BXDIDEtwM3W6B3V1EqzrPw1N0mP9xy5XF5BLPLjst7vw8EiHNjqWt277KmIBDPDg99uKw75ef9bxi_h-3cz6eyaTfkiG3y6IsQ2BeJYo8AJsNJ5altPdE5Zwxyis13VWqlXNnyPczv02zTp7oOqzOzdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ممنوعیت زیارت عتبات و اربعین برای مردم بحرین
«حسن قمبر»، روزنامه‌نگار بحرینی در اعتراض به حکومت این کشور:
🔹
فقط بحرینی‌ها در میان همه مردم ممنوع هستند که به زیارت عتبات عالیات و اربعین در عراق بروند. چرا؟ می‌گویند پادشاه به خاطر جنگ نگران آن‌هاست.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/akhbarefori/679139" target="_blank">📅 12:10 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679137">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e1531d231.mp4?token=jkNCRx_mYrV06P6MJi4UOja4Og_9GMswazgs53_DfZxjStqSyULLPNWtM3g6ZEhcbmxLtV-zo5Xx1JK3r90VFQaKj8uP5DX-cXYQV2obyOTCyztbEfpD8OHPvjP8n2seHNBaMd6hM38sSyiENuRoVG6fnZjxD1pW4Tjnocle05SISdhVfhVSATnknrvW0NbUQIRHLvaXM3r2yVPUWzpEi8mIvan9rnTq9n0UsbdHmnIDmpaVcuERXZpxA-aa0imjnEUwblWMwk4dgBfp-d45otpArMhpm799HoBgNpFzeKqtqQnQMUYZRChsQomlDb0r9wZvV_HXkg8I4pZHabRz0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e1531d231.mp4?token=jkNCRx_mYrV06P6MJi4UOja4Og_9GMswazgs53_DfZxjStqSyULLPNWtM3g6ZEhcbmxLtV-zo5Xx1JK3r90VFQaKj8uP5DX-cXYQV2obyOTCyztbEfpD8OHPvjP8n2seHNBaMd6hM38sSyiENuRoVG6fnZjxD1pW4Tjnocle05SISdhVfhVSATnknrvW0NbUQIRHLvaXM3r2yVPUWzpEi8mIvan9rnTq9n0UsbdHmnIDmpaVcuERXZpxA-aa0imjnEUwblWMwk4dgBfp-d45otpArMhpm799HoBgNpFzeKqtqQnQMUYZRChsQomlDb0r9wZvV_HXkg8I4pZHabRz0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تشرف سران پاکستان به حج
🔹
نخست‌وزیر پاکستان شهباز شریف و فرمانده ارتش این کشور عاصم منیر، به همراه شماری دیگر از اعضای کابینه با حضور در مکه مکرمه، مناسک عمره را به‌جا آوردند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/akhbarefori/679137" target="_blank">📅 12:01 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679134">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qRl0fzp7UhDx3ySkZgBosxXY3ZAJuANkWDz6Q5Uxm0o90I2dI4OjSFPtsNgdsihbl_Sf7eZCqgVRR-BekkVsksT5QFLOn6lTuJR1BQuwS9RDHzTksZ9OSFPb4xqCbl8jbeNVC4vQR0VQi-EDwof7RDmN1lhHLAK1vawCm3Myf89ye_DeR8EfkOSXAN_sQ_dK-SnwoXWJ-GNI35u286Yh19kUuapKSP9pM4EeB4IEywTofX3T4p2W25YgQWHoofMIWaptjysM4-wIWsvoilCaGWvMUUitD0DTk7460wkhKAxb-uNSAel0-CZERa1N9WkVpDIYlczZnH4vFt6V6St6ZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AhmIX3DBGIgIk_awXf7Ka4gWETQ90xyLSBfQGuXI1ZOEYgjQhvGYatEKl1VAZoM3Tts2Vs8j2r63zcjXQ7s4TDcy3madTIcssnoLQD0JbuwoP544hv6KnOtgGuHKj4rXkyIQW8BSXhrKOCu4TrQ8s6QBmUeXoWJwn-MD6aBPDLY7_QjWopFbLHTuq9NngU8Cj2J2SPBiq7Cw8DblSX7Tz9Axx2Ecds1FY900XFrb1HmS9BH6sLv4NNkebqJ7gdHoPWmJ7eo8ztVFNDT5WO-1jTpCXIf31p3Uj8JErRUsspiBWMgodHyt_Wq7TaKtrUZ0_AGcJQLAFs-L56MJH5Iu8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cxfpy3WuWAhbHfCTv0I6j4ygnoSzWwLVtuqgSHnOdpytLXsXlzL1KlZUO5ONS3-kU3LP7Q1YqwjDdY3Awf914itPVb_o3W9S74MO_80UdxEBCchz3uCI8BnyuSoCaBRc7uMTHIcEs4iZ5dmaQD-cFGu-RF1zvnZ13WAfbpD81TeztkuYw47DNoJr7SdD5Zzfjs4pFhHUo88i1Sn91_-zCqAPsqljtLi7VjFEY0YbDrQA-shd4VN36g4hpmV-LxCGonZpviP-XTcrVX4Ic4qMqWYcmHmPma6TlSmOHBYHtiq7rcBKIyX49zPULd2LcyGmJSnHsODKMxbd3vxW4ZryjA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
دهکده زراس در ۱۴ کیلومتری دهدز، شمال استان خوزستان
🌴
#ایران_زیبا
#اخبار_خوزستان
در فضای مجازی
👇
@akhbar_Khozestan</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/akhbarefori/679134" target="_blank">📅 11:58 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679133">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ced1f85eb.mp4?token=Fv1ChivQpQbGrMG0k9flBWo2_jxB4ZPP-jpclKMHfYtieA6TrcMZlkul9iyIqHNXDFpWT4zuAWv8FAfn79F3N7hGXTuMhNNFOQXnbk9ID93uk8fezx8tjf3qOZeyjSaCWnLDUI8cklWq1eBg4xcyuSLRsmnjmCJB5euSepAhDixyNpNO8trqZRvWr5PbLLJnFUPigrlf6KEsLsc_p25Qp8Y8qqMN6gbE1J7KM_eEgk_jMoltU4VmqyXbjAa1xI-DLAuwCJIAVsbeQYnpWBRcttzAxXPmsK1K4ROYOe8ToRrnfPkJhakdZESyHCp71slwiUlNjGgVfDzUJG7qOd0EKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ced1f85eb.mp4?token=Fv1ChivQpQbGrMG0k9flBWo2_jxB4ZPP-jpclKMHfYtieA6TrcMZlkul9iyIqHNXDFpWT4zuAWv8FAfn79F3N7hGXTuMhNNFOQXnbk9ID93uk8fezx8tjf3qOZeyjSaCWnLDUI8cklWq1eBg4xcyuSLRsmnjmCJB5euSepAhDixyNpNO8trqZRvWr5PbLLJnFUPigrlf6KEsLsc_p25Qp8Y8qqMN6gbE1J7KM_eEgk_jMoltU4VmqyXbjAa1xI-DLAuwCJIAVsbeQYnpWBRcttzAxXPmsK1K4ROYOe8ToRrnfPkJhakdZESyHCp71slwiUlNjGgVfDzUJG7qOd0EKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
همسر اکبر عبدی برای اولین بار عکس های عروسی خود با اکبر عبدی را منتشر کرد و نوشت: ۷ شهریور ۱۳۶۵
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/akhbarefori/679133" target="_blank">📅 11:51 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679131">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">♦️
مقر مزدوران سعودی در مأرب دوباره هدف حمله ارتش یمن قرار گرفت
🔹
رسانه های یمنی گزارش دادند که نیروهای ارتش یمن مقر نظامی مزدوران سعودی در مأرب را هدف حمله موشکی خود قرار دادند.
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/akhbarefori/679131" target="_blank">📅 11:41 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679130">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e42a9228d.mp4?token=B0p7ER4_PgWqIpUNZT_DeNCCfg2xHpc93XWpO87sogKMJRmTKLBm01SncYZ0X8tSXECkispfIFENZvbnR5XwloDcGT34QDH8qEN82Q9EaWwxLCh3WpwDsi5eqbcBj-xDuSjspDif1csQ6KjsWfbZqrk_WPj_GmMAH2aM4BiTZJhWjwZ6Xi3VEQS3ZBq_Tnt9xVS9QHp8ikNN0pZRzdny9reUoI9NgrYWMEp-QZNGGIwOU8MAVlapcdCOQE2s9ygjyx23_tYA3sd1XGH4EKe09rZtAjw4GSLIwUHgEtia2Gw-4XyxVRuGh6x_IZffR6xz3_qo73mFMArZlU0uqRpfNyfjXbJ-0L6aXopmjNjGarUTxOBE8FV17Oj8MkEWo1SURpZHii14zsbx_e_2n1IcEaTxReUXWzcUo2hfRvj2Nz8wX2WLu3Rcg7Ude3mKk0Bc9UyFkYwlQgwQsCJ_yP2v8UAYtcFA9JBedpZarBgcW5RMLhRs0fW6eX0jdjyyJ-D7gR6RzOQ1nbM_b1XOAvGKhzgwC1su0wkro822-8qD-xwg-GOLQH9TI5jBOSbrUzmlw-NsdHC945v_BNC8OJYH731pSKZOePhuzU_1mkaHn2WU2XaaMZf7PLGon5f__Sm3Ge4dEV5ONtxY1GPqnsy1yKrQDL9-JzdHNVGf8lqVDvE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e42a9228d.mp4?token=B0p7ER4_PgWqIpUNZT_DeNCCfg2xHpc93XWpO87sogKMJRmTKLBm01SncYZ0X8tSXECkispfIFENZvbnR5XwloDcGT34QDH8qEN82Q9EaWwxLCh3WpwDsi5eqbcBj-xDuSjspDif1csQ6KjsWfbZqrk_WPj_GmMAH2aM4BiTZJhWjwZ6Xi3VEQS3ZBq_Tnt9xVS9QHp8ikNN0pZRzdny9reUoI9NgrYWMEp-QZNGGIwOU8MAVlapcdCOQE2s9ygjyx23_tYA3sd1XGH4EKe09rZtAjw4GSLIwUHgEtia2Gw-4XyxVRuGh6x_IZffR6xz3_qo73mFMArZlU0uqRpfNyfjXbJ-0L6aXopmjNjGarUTxOBE8FV17Oj8MkEWo1SURpZHii14zsbx_e_2n1IcEaTxReUXWzcUo2hfRvj2Nz8wX2WLu3Rcg7Ude3mKk0Bc9UyFkYwlQgwQsCJ_yP2v8UAYtcFA9JBedpZarBgcW5RMLhRs0fW6eX0jdjyyJ-D7gR6RzOQ1nbM_b1XOAvGKhzgwC1su0wkro822-8qD-xwg-GOLQH9TI5jBOSbrUzmlw-NsdHC945v_BNC8OJYH731pSKZOePhuzU_1mkaHn2WU2XaaMZf7PLGon5f__Sm3Ge4dEV5ONtxY1GPqnsy1yKrQDL9-JzdHNVGf8lqVDvE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سردار کوثری: آقا مجتبی و مصطفی خامنه‌ای در جبهه حضور داشتند
🔹
رهبر شهید پیام دادند که اگر بچه‌ها شهید شدند اشکالی ندارد؛ مراقب باشید که اسیر نشوند؛ چون من امتیاز نخواهم داد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/akhbarefori/679130" target="_blank">📅 11:40 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679128">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46cd3dfb68.mp4?token=tyApGwDKnLp6MiZAVz0i2NSJKae-_AAbM6eOc89D6ZI-0UUSpsw99f1pqzSVb7blC9YmKSyLjyxHh4rxn8MpBXOvrYZoVatMw6XTBp0WJaBPglmejv6jQegobv7T1yl4bd2es6ZkqxIVVTdUZvUE4ltDrTWM6SuVww8D6r0vxqAnvclQ6TEovU3Qvf4F0--nx4uTPbxLSzjLINTD2bs4V8bsdF1JksIms3BBAdNzs20ImMtGP7Pr-Lmu08i5EZvTfrCYKkgKzZdZJDsxu9jvGLSBO45ji5WmMxUo7qwicKMpaMu0eqOrLLNOldabSoERUFo6TRIAlstgXQz1NGEHFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46cd3dfb68.mp4?token=tyApGwDKnLp6MiZAVz0i2NSJKae-_AAbM6eOc89D6ZI-0UUSpsw99f1pqzSVb7blC9YmKSyLjyxHh4rxn8MpBXOvrYZoVatMw6XTBp0WJaBPglmejv6jQegobv7T1yl4bd2es6ZkqxIVVTdUZvUE4ltDrTWM6SuVww8D6r0vxqAnvclQ6TEovU3Qvf4F0--nx4uTPbxLSzjLINTD2bs4V8bsdF1JksIms3BBAdNzs20ImMtGP7Pr-Lmu08i5EZvTfrCYKkgKzZdZJDsxu9jvGLSBO45ji5WmMxUo7qwicKMpaMu0eqOrLLNOldabSoERUFo6TRIAlstgXQz1NGEHFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روزنامه‌نگار انگلیسی: تنگه هرمز به نماد یک تحقیر تاریخی و ماندگار برای آمریکا تبدیل شد
جاش گلنسی، روزنامه‌نگار و نویسنده انگلیسی:
🔹
تنگه هرمز به نماد یک تحقیر تاریخی برای آمریکا تبدیل شد. تحقیرى که ممکن است برای یک نسل در حافظه‌ها بماند؛ اگر نتیجه به‌کارگیری تمام توان زرادخانه و قدرت هوایی آمریکا علیه ایران این باشد که اکنون جهان برای عبور از تنگه هرمز مجبور به پرداخت عوارض شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/akhbarefori/679128" target="_blank">📅 11:31 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679127">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/346dcb5023.mp4?token=OPDJzhyWAHllauJsGPz3LWi9068n5d3VMKGThkhy_rypMp4_-ENezXa_UrtJSkOmA9g1wOTm66JyBiHWjgwlyyHhn5LVe_C88DMBdy5W8UUUtbWCIYRSWRgk6XDzigTpCTevrb7k5cU-ZnRllrYyFpl7c-O7c5cKcJLvVdUJfZNMlsMs3UzWPtPmr5-Io3LO8Rce_6RPMSO0mApO60mpTMEYPuLKN_oU9FEJ9TfyApoWxiMZM3GfuPC2OXF1EHeZe9jjtelLxnzk1iUaMxShFqzhr3vUnxBcIlogZ9OxDLbYnrPJJlGRfdRHYbhuoalL1NtcMcQ-YSHgkIQQd8cGDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/346dcb5023.mp4?token=OPDJzhyWAHllauJsGPz3LWi9068n5d3VMKGThkhy_rypMp4_-ENezXa_UrtJSkOmA9g1wOTm66JyBiHWjgwlyyHhn5LVe_C88DMBdy5W8UUUtbWCIYRSWRgk6XDzigTpCTevrb7k5cU-ZnRllrYyFpl7c-O7c5cKcJLvVdUJfZNMlsMs3UzWPtPmr5-Io3LO8Rce_6RPMSO0mApO60mpTMEYPuLKN_oU9FEJ9TfyApoWxiMZM3GfuPC2OXF1EHeZe9jjtelLxnzk1iUaMxShFqzhr3vUnxBcIlogZ9OxDLbYnrPJJlGRfdRHYbhuoalL1NtcMcQ-YSHgkIQQd8cGDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خودکشی ضارب ۱۴ سالۀ مدرسۀ تایلند
🔹
دانش‌آموز مدرسه حومه بانکوک، عامل تیراندازی بوده که جان حداقل هشت نفر (سه معلم و سه دانش‌آموز) را گرفت.
🔹
او پیش از یورش به مدرسه، پدربزرگ و مادربزرگ خود را کشته بود و در نهایت، در مدرسه خودکشی کرد.
🔹
مظنون دانش‌‌آموز کلاس نهم (حدود ۱۴ ساله)، ۲۶ گلوله شلیک کرده و ۳۴ گلوله دیگر در محل تیراندازی پیدا شده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/akhbarefori/679127" target="_blank">📅 11:23 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679123">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EX2nBnNNOuxZoptok_3JtB3XDuudYvoP1I7QrrPw232c8TogkmB0i7o8jczGEYgu471a42D4P64kmOHZ2DVieGRIcxDvFtMi5XZ7KtdrRSZt-Nk2-i0ueuVugxeHdOzAEMDz-BfBznKTqO13LVELnhtQxQs5VFt1wa_SagLi0VQ5lHCD1zrGf0TPdBwJL8-ugItiiyD9waDHb1FpR9yK7cHpI7Ne1MtsaAYe-3cIcUvCYLjew9S7uvR3Figs40cpaETA3S_5v-xJMiP_5Oe9FuA8X4HFtp2C-yjjlO2V5icbuY4qr7gLprk2lnLLo-A7rNuUQNVqUFA-T7jEzahbMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F4vueUm6HjOY5ZPWL2r5zD_6skVmjOdTXhL-TQ42tbDSFmdxVt9pcsz6Y2kE7foT_s1BYyXbBwQTl41fFZf6a-DwPMECYozf-tDP2c_PfnoChej0QIZkfNEV19CEmY9ONnPTQp09pvcYrec2PnfndoK3GvF9n38AnFjpJ1kUUIQSg0KcnyUm7XuFkjbhbJSYWTHKyVJOK_lOJgpZ3a65DJ8W1pLRUPcWXFzs7c2xsbRvMDbeD686gK1boWpcYV2LyLZFiVzQoYfS-ryE9yKcCaBWY-sdXf3AP1DGFqhaJMHogvcSS4h4Bf_5dfaL4E8ioW6U-LadltzfcWU2sib5kw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
این گربه‌ای که می‌بینید پیرترین گربه‌ی دنیاست که جدیدا ۳۱ ساله شده
🔹
غذای این گربه فقط آب معدنی با ماهی سالمون، میگو، مرغ و تن‌ماهی هست! اکثر گربه‌ها متوسط طول عمرشون بین۳ تا ۱۲ ساله.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/akhbarefori/679123" target="_blank">📅 11:09 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679122">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">♦️
مقر مزدوران سعودی در مأرب دوباره هدف حمله ارتش یمن قرار گرفت
🔹
رسانه های یمنی گزارش دادند که نیروهای ارتش یمن مقر نظامی مزدوران سعودی در مأرب را هدف حمله موشکی خود قرار دادند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/akhbarefori/679122" target="_blank">📅 11:04 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679120">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7af38b512f.mp4?token=vTDokyTP3Ief5Nd3kYHOXPon5oJkdvV-aer288d8Phaj8DZ4hQt09GD1D59Gi1FNZe-ITfL9XOaxmU5VT-sXuCsRtKdtKWmY-SD6eWON6iTBLp7sdcmjyroZQPGoEOUzqmOqFbJH7IhsGiCV0Ii2YHEsBmvdbjpsx2oOjzgGUNcgrj3GimlKGYY3SZWJ8s1TtDJ1jqRe3zfsSbCDeODUhOXmIqycy8JqdfdFwqeBJKnEuh3n-rM7KU_EjSVBbgj95BgjDAKXjOFSczgRrScickpsDBIiPqZawy1rz8DaJCTlfTQC9h-fdAZ1ls4rKJre4y-MZdu6A-dZ3cJBKFODig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7af38b512f.mp4?token=vTDokyTP3Ief5Nd3kYHOXPon5oJkdvV-aer288d8Phaj8DZ4hQt09GD1D59Gi1FNZe-ITfL9XOaxmU5VT-sXuCsRtKdtKWmY-SD6eWON6iTBLp7sdcmjyroZQPGoEOUzqmOqFbJH7IhsGiCV0Ii2YHEsBmvdbjpsx2oOjzgGUNcgrj3GimlKGYY3SZWJ8s1TtDJ1jqRe3zfsSbCDeODUhOXmIqycy8JqdfdFwqeBJKnEuh3n-rM7KU_EjSVBbgj95BgjDAKXjOFSczgRrScickpsDBIiPqZawy1rz8DaJCTlfTQC9h-fdAZ1ls4rKJre4y-MZdu6A-dZ3cJBKFODig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آینده‌ گوشی‌های هوشمند
🔹
این گوشی رول‌شونده به نام MOTOROLA RIZR فرم کوچکی داره که توی جیب جا می‌شه، اما وقتی به صفحه‌نمایش بزرگ‌تر نیاز دارین باز می‌شه!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/akhbarefori/679120" target="_blank">📅 10:52 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679119">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/28871f432c.mp4?token=tDT0JtABcjKgKAkkDtyZsY0MbJvbVZzMtofjTHjkV3Nrf7rccLtYZLmbOgix9sS5_4wJM20w2vMf22YBU-40klKmtcXasrFCnVQyUBLy2PetwGh_t0Ew12hJvudwqcvAzMRBP-RjV34Kln1hIp8MOJXB32B_uy_3q_Y65xBawNZASmdf6mX20wxgcynR5FBf6hi0Ch9S-bS2FV9lMLjFFbbGQkZKI_FzvnrwkgGUvfFnEeF4ltzn4dM6kf_jbr_KmmAvWDN927M9II3X9E4RByv2IukfIdOaDxCoibiARKXpuz-HcEr-yaJl6CrTxOP_afJmT5Fi4gac4JsBohuiUHC-ncFPu873GpHqoTUIqMFlYuQtJ4xjaaVV9Akhc71DkBnBtY-DMY7K_eSXPQ3aJ9fFFcOjW4ptYVdacKnLHPWkUPAKG34Dd3SMcWuBniwT87z565x6nO7TN3h1h4sYyOPkdbiXas_ufIJf5gczjnOfquo5yxy5SLSPCZPtI0UGP9hlv4owAQlzmQZ6gX-NzOffW73Rh5Y6hJnmm8uDpNACj3AipNeWfESjY44DpStQi6ClmhbxJVOw4kM0FdrcApjSDXCOFmHehKpcbiwEHGKreqnaOxiE1QK8uSOYaJ9J4M-GqkiVvdKAMdAqtAQobKK3LOf_gGbM8x1zw6z0knk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/28871f432c.mp4?token=tDT0JtABcjKgKAkkDtyZsY0MbJvbVZzMtofjTHjkV3Nrf7rccLtYZLmbOgix9sS5_4wJM20w2vMf22YBU-40klKmtcXasrFCnVQyUBLy2PetwGh_t0Ew12hJvudwqcvAzMRBP-RjV34Kln1hIp8MOJXB32B_uy_3q_Y65xBawNZASmdf6mX20wxgcynR5FBf6hi0Ch9S-bS2FV9lMLjFFbbGQkZKI_FzvnrwkgGUvfFnEeF4ltzn4dM6kf_jbr_KmmAvWDN927M9II3X9E4RByv2IukfIdOaDxCoibiARKXpuz-HcEr-yaJl6CrTxOP_afJmT5Fi4gac4JsBohuiUHC-ncFPu873GpHqoTUIqMFlYuQtJ4xjaaVV9Akhc71DkBnBtY-DMY7K_eSXPQ3aJ9fFFcOjW4ptYVdacKnLHPWkUPAKG34Dd3SMcWuBniwT87z565x6nO7TN3h1h4sYyOPkdbiXas_ufIJf5gczjnOfquo5yxy5SLSPCZPtI0UGP9hlv4owAQlzmQZ6gX-NzOffW73Rh5Y6hJnmm8uDpNACj3AipNeWfESjY44DpStQi6ClmhbxJVOw4kM0FdrcApjSDXCOFmHehKpcbiwEHGKreqnaOxiE1QK8uSOYaJ9J4M-GqkiVvdKAMdAqtAQobKK3LOf_gGbM8x1zw6z0knk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یزد؛ دومین شهر تاریخی جهان
😍
#اخبار_یزد
در فضای مجازی
👇
@akhbar_yazd</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/akhbarefori/679119" target="_blank">📅 10:41 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679112">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FBnfxrwUHa2GmT6HiBHQVGrXWV0BtSOcw7Y2Er0q7JZwBC4-tLVUeOyRHmj3iCA4v1IDRoC4nskBSFlENLiVhjrqcbREnEwioSC-4ZksChYgdnngcHKpa-1u0CIqSF9xHKFKNe6QsJG7HvW3rS13unYaAcN3RnUtEfinX2E-qRnmSyshBMeNYLGe4g0GbVqxZy9ZR1_PBetXTMNs0g8585i_mDwvbanjcjTDuV-gs0dPI5_O7BjwtvTQjF2ZnQkM7nJhMfjBzyfnucrmIFw8upx5VcIqoYP-CV213V_f3JYt24Q_vK_XIWQi_7OFLvvKSo2ZY2NrfoHPYZxGoYt2rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i4rIhk2hdXtEbYVKiDTa2PTRS_P5HBuJpdf2j_g6kBHZML8AcWp7hFqVUwzvY4XEPUhtCkf5EymochEHM0lZ3hpkgkxqkSWm6h2A4gw-bTAl8vTJWRGJXRhDMpFX_FMxZNeBJyRB9nGFF3pn3ksqsK5bjL47q1XukOgq9c-ZiBvO_zmhkWbrKLkIo_Vdc8UuiKue1OFRnOoNh11RmL132lR4WkYGnYmY4TmGnVb6J2coaIBYix-deJCA3gROSAgcvo--7Xnki5yrCJk5fDErG8D1r44YofVQo6QkSjh-Xe4Do67B_HvuBBF4-MPiFi4VDoBQReZahexrBFNl5mA50g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fmujQg2XDTPeKjOqweJ3lKOWHhfYJAQAQw2I08LLS2WKbA3rB-XuTNXq2eJNCl7vJn6908O325kSHStRFXzWMXFg4KZhHiRMlU7eWAUGkymJvSNzthyMnJvsRGTnPetm3Jj1-m19Dg5RRGe8i7W8i38eq-z7t1RpTF5fgfQvbS2F8I2mHx6QHOrKcPU8To-FgpnRUpEVYiq4_D6XWlOUyMTvNDfEy2W8HzDs2IAcb5YAvS4KC22eXHY-L0hQIN12Un8w0r6jBK4QTJuEHn2Cr2cwVqH74p-FNmBfCluczjbeMqzgub6-XzlXJV6egqfc1M-V3A9ncOhYq-ba_ujC8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qsJt7Mkszrksfj5ysf25KqWGCEZZgV_i0PwPE6QElWWSxdLI9r7D96q2ulw_QeRec5ZvXVGlXVdpFezzyBWJKRdSa0EjsHGLhuqLelyxD5pLFu0Yr3DtmtZaEV3XWwf5DzIACfrZdhgmBq9UTBtle9M69VRV49nmXzxYzQy2L89h7MIHw0nc2fomqw4Y5T3Jb1Xk13joWWI3n5smxE-zydhyqxC36tXK_JQGCZBepMT27ftqfjZutsKjVyZ0wumNGuw6enfRbFjSuI3lhNeaxwQwOUWQv_7iZ9s369rdHuzUfdT0HhvtQ7P8Y9KWEsDDVl1lYHxuyVIlpqfr8nroew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qi_mtSzPNm9XETVRbQIkGi3YPObQzveW-M8Zrv-8Lz-e_ahtq8AUqLMYP4uZF7B68dPCagJgqb3mYFaA19jxtAzOiBE2GdMCyyehq7vb1XtqW7TBVROz4kB06QLEWtr7LUQDsKAT_JBOcI8DyRmqAN4s6nL7J7YaB-OyguHAT5k_GkjUtAT6CUuS05W6fnhhNEWyXYRrKaJ2ro4IllpjmiaA9g8rrDq1I2q8UlE-gZgUDnfJ1jH927rKqsgLIEr2enR4X06tlL1H_OV4-XB0XklyCQny1p5s3TiOgMB4IQGZgVBm55giGR7rBqUDEZQm1ynNnvCcaykS6l416QT9hA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IFtwK7FeSi69RMhAcdmkptOjMZT7VKjAt_1hLw_JCu10NmS4OoaNJJsVL6QMdb4L6AGLcMjNdFLU8D2j761jkJ7JLjl0IcO3gt3UqlrfVxNtBZt2tsYm5vz_tGQjNFQCKeXmnKNmh4MPnLKE2JoiSlimTi5X2KmJQyvMWZM_tNESHtO4660dR-io2XW6aHyQvOcFEL7tXtKecNIB3XVPiwaOgZLjpwrKC-XwE_BWgz9S1ky2GjQsd-V-AMLzrkt_sYVBV3qg24pBQANFkQC_nfg355bXBjhKzPLIrA2bBX_0QTs-HwYm7sdULtmX5ZlPXnDClqQw462Z0La8ZoWz1g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
ترش، تند، وسوسه‌انگیز؛ آموزش تهیه انواع ترشی‌های خانگی
😍
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/akhbarefori/679112" target="_blank">📅 10:31 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679110">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">♦️
تجرد قطعی در ایران؛ از وضعیت فردی تا سبک زندگی
🔹
به گفته یک جامعه‌شناس تجرد قطعی در حال تبدیل شدن به نوعی سبک زندگی است و بخشی از جامعه تمایل بیشتری به مجرد ماندن دارد؛ آمارهای رسمی از بیش از ۱۸ میلیون مجرد قطعی بالای ۴۵ سال و بیش از ۲۴ میلیون نفر مجرد بر اثر طلاق یا فوت همسر حکایت دارد./ایرنا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/akhbarefori/679110" target="_blank">📅 10:26 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679109">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🔹
خبرهای متفاوت هر روز را در وبسایت خبرفوری کلیک کنید
🔹
🔹
همه چیز درباره توافق مهم ایران و عمان بر سر تنگه هرمز/ این تفاهم جنگ را برای همیشه پایان می دهد؟
👇
khabarfoori.com/fa/tiny/news-3235999
🔹
افشاگری رویترز از علت تعلیق حمله به ایران
👇
khabarfoori.com/fa/tiny/news-3235850
🔹
اینفلوئنسر مشهور در پخش زنده کشته شد
👇
khabarfoori.com/fa/tiny/news-3235919
🔹
اعلام آمادگی یک نماینده مجلس برای شلاق زدن باقر خرازی
👇
khabarfoori.com/fa/tiny/news-3235825
🔹
عذرخواهی سحر دولتشاهی درباره استوری خود؛ قصدی برای بی‌احترامی به اذان نداشتم
👇
khabarfoori.com/fa/tiny/news-3235984
🔹
اخبار لحظه به لحظه جنگ ایران و آمریکا
🔹
https://share.google/8EImhrm9fBFYjsyZr</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/akhbarefori/679109" target="_blank">📅 10:25 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679107">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromورزش فوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ghr246KRyiqskIyhyq0OyL2JRcuovM7xrp2Hi-FEKxabWEjAgGb-JcArKiHYXLXrKnmCDyqC6q78Lvem9hvKu23HgLnJxPggdzwrg2c4qOXrqHQ_EP7TsYiANSsOPuiXC2JfJyokQmTo62mIsyqb3KePRV5TVNUDlhSa5w5Ss0DG_TdbLlCN9cbhZX8fOxXQ-jbqzr8YKSD0RHeCprGCpgCZLBRgZeNQLk7QZmZiaJvxIp5AO06Igpk_wQDqAFZISsGL_Z3Rcbzt9GO6pYnCWyHoT6ytZODNr_QEPM4VqAicfqMitZXDyQaaLFchC9WiUw9TD1F2PmGta4BrsdvvJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایجاد تاخیر برای جلوگیری از تماشای مسابقه شناگران پیش چشم مادران مشهدی!
🔹
مسابقات شنای کودکان شناگر مشهدی در حالیکه قرار بود امروز در استخر شهید هاشمی‌نژاد سعدآباد این شهر برگزار شود با اتفاقی عجیب روبه رو شد. این مسابقات قرار بود از ساعت ۸ صبح آغاز شود و در شرایطی که مسابقات آغاز هم شده بود، ناگهان با تصمیم یکی از مسئولین هیات شنا متوقف شد. این مسئول ناگهان با ایجاد اختلال در روند مسابقات، اعلام کرد تا وقتی مادران در سالن حضور داشته باشند مسابقات برگزار نخواهدشد!
🔹
این تصمیم عجیب در شرایطی که مادران بی صبرانه منتظر تماشای رقابت کودکانشان بودند، با واکنش خانواده‌ها مواجه شد. تاخیر در ادامه برگزاری مسابقات و لجبازی مسئول مربوطه در نهایت با ورود مسئولین ورزش استان ختم به خیر شد و با استقرار مادران در بخشی از محل برگزاری مسابقه، مسابقات ادامه یافت.
🔹
گفتنی است عموم کودکان شناگر حاضر در این مسابقه زیر ۱۰ سال سن دارند!/ورزش‌فوری
@fori_sport</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/akhbarefori/679107" target="_blank">📅 10:19 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679104">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e445bf036.mp4?token=iEz8NNmDVH4haCISLec5gpJCOsULMULfFRG0PSXHIWSdYsI0y1cQGznV96ZB5uJPNOrSzrNccwG2NpdZVgqxxTLuZ_8vEVloZiBwwe-6l7vVMVW8u3KUqPU2TMEyN7Q-3CXnla4AIY7Ee2z-OuLJ7Q1k_h2fDLZN7ONF7sDQ61jodZuMKRxie281MZgysiYKv8h0-vo7b5dgcHm_epP1jvUpGMIghGJDTDJ27VEBI592SP_v1Ls-QwajXNiyNncmY72lQAfXRh7sGFvdNEoIBCkW2liQoCW5KTd4WnS2xqzvPi8haOVecrISD-IuDg7e7fppefglKzx7xZ7c4qPH0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e445bf036.mp4?token=iEz8NNmDVH4haCISLec5gpJCOsULMULfFRG0PSXHIWSdYsI0y1cQGznV96ZB5uJPNOrSzrNccwG2NpdZVgqxxTLuZ_8vEVloZiBwwe-6l7vVMVW8u3KUqPU2TMEyN7Q-3CXnla4AIY7Ee2z-OuLJ7Q1k_h2fDLZN7ONF7sDQ61jodZuMKRxie281MZgysiYKv8h0-vo7b5dgcHm_epP1jvUpGMIghGJDTDJ27VEBI592SP_v1Ls-QwajXNiyNncmY72lQAfXRh7sGFvdNEoIBCkW2liQoCW5KTd4WnS2xqzvPi8haOVecrISD-IuDg7e7fppefglKzx7xZ7c4qPH0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خودکفایی در صنعت پالایش؛ ویدئو وایرال شده از یک برج تقطیر با ظرفیت ۱۲۰ هزار بشکه در روز
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/akhbarefori/679104" target="_blank">📅 10:11 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679103">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f65c3ad0d.mp4?token=IFrvMYtIoHe_xQ3MfCItlj1N__EP-JE1-ztjV0nUDF293DLNO2FDzpVZCX3AmMJCEKCTr5V5dKEB_2f7p411963HSR2iEzgaKorL0qwnw_MovpSmZccPvAYIijIBF06kjuvVjG2ra_hSUinBROxRjOgl0BsHP7x6LE3kXJRd46p5KPXr1HnBFIgW3S_Zr5GzovBlQafeExqFAkW-1ix3wllAHY63sG7QStj8KDjyxDm0S2NtN5LSM2r0MlC21vY1_52UQ_0cSA0NAnRyaT3RUun4OjgmbQ69X9T95ior1RXYparhWLLJ0aa3_wkF9gqSoKtbEpIKatkOrlI7WOLrpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f65c3ad0d.mp4?token=IFrvMYtIoHe_xQ3MfCItlj1N__EP-JE1-ztjV0nUDF293DLNO2FDzpVZCX3AmMJCEKCTr5V5dKEB_2f7p411963HSR2iEzgaKorL0qwnw_MovpSmZccPvAYIijIBF06kjuvVjG2ra_hSUinBROxRjOgl0BsHP7x6LE3kXJRd46p5KPXr1HnBFIgW3S_Zr5GzovBlQafeExqFAkW-1ix3wllAHY63sG7QStj8KDjyxDm0S2NtN5LSM2r0MlC21vY1_52UQ_0cSA0NAnRyaT3RUun4OjgmbQ69X9T95ior1RXYparhWLLJ0aa3_wkF9gqSoKtbEpIKatkOrlI7WOLrpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
برنی سندرز، سناتور کهنه‌کار آمریکایی: ترامپ فاسد و زورگو است؛ جنگ ترامپ با ایران یک فاجعه برای آمریکا بود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/akhbarefori/679103" target="_blank">📅 09:48 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679101">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">♦️
نمایی
متفاوت از تشییع با شکوه پیکر مطهر رهبر شهید انقلاب اسلامی بر دستان مردم عزادار عراق در کربلای معلی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/akhbarefori/679101" target="_blank">📅 09:38 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679100">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">♦️
حمله جدید یمن به مزدوران سعودی در مأرب
🔹
برخی منابع یمنی از حمله ارتش یمن به نیروهای وابسته به عربستان در پادگان صحن‌الجن مأرب خبر دادند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/akhbarefori/679100" target="_blank">📅 09:30 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679099">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">♦️
کشف بقایای انسانی در ارتفاعات شمیرانات
کمیته جستجو و نجات هیأت کوهنوردی استان تهران:
🔹
بقایای یک فرد مجهول‌الهویه به همراه وسایل شخصی در شکاف میان دو تخته‌سنگ در منطقه بندیخچال کشف شد.
🔹
هلال‌احمر و عوامل تشخیص هویت در محل حاضر شدند و بقایا با دستور قضایی برای تعیین هویت، علت و زمان مرگ به پزشکی قانونی منتقل شد.
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/akhbarefori/679099" target="_blank">📅 09:21 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679097">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1e205c1352.mp4?token=uiepUS2lrzJ10E4Iwpd0y9ghGvGiVxh2AsHZ46QvXtSec3_4-OYlq8M2rVfBGSxzEao2t2GEebePlf8FWvF23aR3508AiWekAZ7DQrlifTc_iuNLAlx24EoeXQ_7wIyghmrTVINO1e_aS0JQJt_yL6GZJVKejr3kCFau79vz_BBcH4w9EPhy3Btd-5V0Fy6ibdMURC9f5eddxPaDrLgh_lajYf2R3Vbx-25ICp8HsK5v4EDXzEal4qs9XXs6HNTsm2uFqhgvP5JhxaGqbN1NbK9pa1cauZnvyqpTfx1GDNuCmlFbF1ltVAtHvTbvpajUpEXXyAj5XLjbDUpshauc2AcEMdXzbGgPzr6JWsqdVhWjrdC8oXirpL1HqvXYbhkCqCKw7_LT9CLM7hxLO2lrOwQMz0sJAapHy-FBW7HtbvnMXjQ3SHpelvMt4Gw3X76nQ2P319s-i4OYQ8fuwkovT1bi1tJzX0rt8w-JYtXE9EDTW6UQGxcSwNsm5U4BmPqet1m51di3VTFWZUjD1iRWNZrPH58H9Grr-MhHHM55Uy8-wThsusPQaxhduK-XYJrur7I5Fwu_3BPYI2AmxkqB3QXvsI94CCAemaweua5cK_MGLhmMal8tGGP1RTFj8_BCiV6LxOaY0mdshrk7-YmWm7W_609LzzUyaR69GdT0L5Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1e205c1352.mp4?token=uiepUS2lrzJ10E4Iwpd0y9ghGvGiVxh2AsHZ46QvXtSec3_4-OYlq8M2rVfBGSxzEao2t2GEebePlf8FWvF23aR3508AiWekAZ7DQrlifTc_iuNLAlx24EoeXQ_7wIyghmrTVINO1e_aS0JQJt_yL6GZJVKejr3kCFau79vz_BBcH4w9EPhy3Btd-5V0Fy6ibdMURC9f5eddxPaDrLgh_lajYf2R3Vbx-25ICp8HsK5v4EDXzEal4qs9XXs6HNTsm2uFqhgvP5JhxaGqbN1NbK9pa1cauZnvyqpTfx1GDNuCmlFbF1ltVAtHvTbvpajUpEXXyAj5XLjbDUpshauc2AcEMdXzbGgPzr6JWsqdVhWjrdC8oXirpL1HqvXYbhkCqCKw7_LT9CLM7hxLO2lrOwQMz0sJAapHy-FBW7HtbvnMXjQ3SHpelvMt4Gw3X76nQ2P319s-i4OYQ8fuwkovT1bi1tJzX0rt8w-JYtXE9EDTW6UQGxcSwNsm5U4BmPqet1m51di3VTFWZUjD1iRWNZrPH58H9Grr-MhHHM55Uy8-wThsusPQaxhduK-XYJrur7I5Fwu_3BPYI2AmxkqB3QXvsI94CCAemaweua5cK_MGLhmMal8tGGP1RTFj8_BCiV6LxOaY0mdshrk7-YmWm7W_609LzzUyaR69GdT0L5Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مدرسۀ تایلندی هدف تیراتدازی مرگبار
🔹
طبق آمار وبگاه تایلندی «خوسود» در این تیراندازی حداقل ۷ نفر کشته و ۳۰ نفر زخمی شده‌اند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/akhbarefori/679097" target="_blank">📅 09:17 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679091">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a2ff432da.mp4?token=BlwVD6f0qSkkZIVlxOVzKWSa2UY_UHEniHb-0B2OLyUlae0Y0theZ_GhDlF6RxCKcx-tGVNsls2mFClnEccswQcPIclKl2nuMqla8Ycx86KHHt0bLN_5vyC9jfO9p_t0xf9ig-kbfm5Yz8DKqt1qB8YdBQoFGHzwOE5q0kFZWOgdH7kzwlhRcXyhBnveXKG9Xg6cseOUU3lE0mqC2aiI-fr0nMtSkP4N5USwGAqxOrTUws9Tj-lD5tw0NE_1cApikyZUF5vgxlo_19iDCLbnl3VALi3mII5e4rFF5Xnb4p4khbDs7vHunKCI6haDD1knu_HlW28wY1iNaMlafV-JzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a2ff432da.mp4?token=BlwVD6f0qSkkZIVlxOVzKWSa2UY_UHEniHb-0B2OLyUlae0Y0theZ_GhDlF6RxCKcx-tGVNsls2mFClnEccswQcPIclKl2nuMqla8Ycx86KHHt0bLN_5vyC9jfO9p_t0xf9ig-kbfm5Yz8DKqt1qB8YdBQoFGHzwOE5q0kFZWOgdH7kzwlhRcXyhBnveXKG9Xg6cseOUU3lE0mqC2aiI-fr0nMtSkP4N5USwGAqxOrTUws9Tj-lD5tw0NE_1cApikyZUF5vgxlo_19iDCLbnl3VALi3mII5e4rFF5Xnb4p4khbDs7vHunKCI6haDD1knu_HlW28wY1iNaMlafV-JzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حجم تخریب پادگان مزدوران ائتلاف سعودی در حمله روز گذشته ارتش یمن
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/akhbarefori/679091" target="_blank">📅 07:34 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679090">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vDzDhMJiRPQsQ_u3Dm3f2Fy8_rsKv0qgUp40hC000p7IFqMZ-LFvU75RWdJyiOxcC4SOi0JhX2EjjXHsXQ-lGE3nxH4WFWwKKTn1Nu8Z2r6p23kL2NmtoPbb6AJXoePCxmAM7-uK9Dz-XUaKNJfGo11Qb47jMKoabn3xu-RRL-zTkLv2yYrXWjsUzQu4He65evoa7TFuXrREAwXWP3RvgUKjAHHGSxj0yBUQENJP-uaouyG46vMeL2CyAMhY9EmGSuCwVbJwIFKODRr2ssInEBjecJ6aKtvS1B8RKNj2wW_ym_ATUhUMJubYRPV64wm-K1VMaYZTTtbwr4Iy4CL9YA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز جمعه
۱۶ مرداد ماه
۲۳ صفر ۱۴۴۸
۷ آگوست ۲۰۲۶
جمعه‌ها
#دعای_ندبه
بخوانیم
⬅️
متن و صوت دعای ندبه
@AkhbareFori</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/akhbarefori/679090" target="_blank">📅 07:30 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679089">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eD90GhWUNbic7nz36Dn8Y0yqgA_yMRrrj_oiliN1zkMoOHu9brQa2Po4dFSbDoRJ48Rt8KzwUyDk9Dy3y_lOZs27MrUXwpC3MhQga6xO0Vc5nD8XlBY8VngSwJ1M0Z17ix86uONwGPsppFZalqAD4mWv2zSNCtetqs0DyA1CyvqPcSnu5CPrTePZayrlxA8_0t-1zzhJiE2BWk1ZhCLdr81MxdFfqG3al-MpfSzW49JbZoLwrAWlDW0Y0SSqMs_L_2Ti7Iyxi53--S_u3Hs9IOcUtaUiUqh0Bn0pZH2ZQTNJaiOl4ymG2ZoeTkTfOGT58PEZHxM6Z0hoPcy1E_q6lQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نفت ۳۶۰
مرجع تخصصی اخبار نفت، گاز، پتروشیمی و انرژی
✅
اخبار فوری
✅
تحلیل اختصاصی
✅
استخدام صنعت نفت
✅
پروژه‌ها و مناقصات
✅
بازار جهانی انرژی
@naft360</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/akhbarefori/679089" target="_blank">📅 07:07 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679086">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">♦️
رد پای موساد در بحران مهاجرتی اخیر اسپانیا
🔹
محافل اطلاعاتی و دانشگاهی چین گمانه‌زنی می‌کنند که اسرائیل بحران اخیر مهاجرت دسته‌جمعی در منطقهٔ خودمختار سئوتای اسپانیا را طراحی کرده است.
🔹
به گزارش روزنامهٔ ال موندو، در پکن گزارش‌هایی در دست است که بر اساس آن‌ها، هجوم مرزی یک عملیات حساب‌شدهٔ جنگ ترکیبی به رهبری موساد بوده که با همکاری مراکش برای بی‌ثبات‌سازی دولت اسپانیا اجرا شده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/akhbarefori/679086" target="_blank">📅 02:01 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679083">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">♦️
رویترز از دو منبع منطقه‌ای گزارش داد: ترکیه، عربستان سعودی و پاکستان امروز در عربستان قرارداد دفاعی مشترک امضا می‌کنند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/akhbarefori/679083" target="_blank">📅 01:43 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679080">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8da4c49a2.mp4?token=sHOxKlw5YOnfv6sePq5Krt-CHt8XTCQmIBDDxQ_xVSToDM-hc28K8PGhGKDF0k1oPvb8xuVk59iawOsn-zHud9HSmUIlm1QZqbV5G6n-77d11LL1bXWZ89PrYRDzY21XZK7c6fg41rNVhz11bZbprYAUQFyGVmhCVLh3gDL9RbkvM-LE8RM60tnY_RSW6_Z9arCkzsIsZPX6a0HEqt8DIclcCrAIJ7o5XXQlvCShIUp6aA8yool9ZO-sgQDyQm7qkokOJSYM0hMGaiOw_f5laGvPOjN9UTW_sbMlJxmFQgfXpAd1CNt8xHBm9aqcM-EaLuFIgwIrRxm1FFWl44Agl4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8da4c49a2.mp4?token=sHOxKlw5YOnfv6sePq5Krt-CHt8XTCQmIBDDxQ_xVSToDM-hc28K8PGhGKDF0k1oPvb8xuVk59iawOsn-zHud9HSmUIlm1QZqbV5G6n-77d11LL1bXWZ89PrYRDzY21XZK7c6fg41rNVhz11bZbprYAUQFyGVmhCVLh3gDL9RbkvM-LE8RM60tnY_RSW6_Z9arCkzsIsZPX6a0HEqt8DIclcCrAIJ7o5XXQlvCShIUp6aA8yool9ZO-sgQDyQm7qkokOJSYM0hMGaiOw_f5laGvPOjN9UTW_sbMlJxmFQgfXpAd1CNt8xHBm9aqcM-EaLuFIgwIrRxm1FFWl44Agl4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مغز خودش رو بر اساس چیزهایی که بیشتر بهش گفته میشود شکل می‌دهد
🔹
هر بار که به خودت می‌گی ضعیفم، شکست خوردم، فقط حرف نمی‌زنی بلکه داری به مغزت یاد می‌دی که این‌ها رو باور کنه
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/akhbarefori/679080" target="_blank">📅 01:26 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679079">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/254b28154f.mp4?token=HLtxkthO5ppuvMIBNa7HRdCUExBm3pMCFIJtMwAo4BE1mhNGhEaHDFCZUN_FqmzSkQcL5x_rymU1Qq-xckxg93m_f08c8OIW4w5iIeRDWuk3_WqgnNMFlFvpwrvM0KdOMPTNCsG2aHASJgA_nlEBiVkSqmgRwjVhswqJNo_2xxFi6ctO6fLgH_lDWFUvp_uo9NUs0CIEbdlszUZDud5RNJtRwaRgB-vxVZHstg1YZTuQoGlLsVEtheojSnEA7L74oFihIPWG6dQE8UTq74QXy2hSZdy7UGRZ_Uk6hClJPFU4D9msHl3cXjN5e_9cH9QRQaKrljxjZqC7rjFD3AFauw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/254b28154f.mp4?token=HLtxkthO5ppuvMIBNa7HRdCUExBm3pMCFIJtMwAo4BE1mhNGhEaHDFCZUN_FqmzSkQcL5x_rymU1Qq-xckxg93m_f08c8OIW4w5iIeRDWuk3_WqgnNMFlFvpwrvM0KdOMPTNCsG2aHASJgA_nlEBiVkSqmgRwjVhswqJNo_2xxFi6ctO6fLgH_lDWFUvp_uo9NUs0CIEbdlszUZDud5RNJtRwaRgB-vxVZHstg1YZTuQoGlLsVEtheojSnEA7L74oFihIPWG6dQE8UTq74QXy2hSZdy7UGRZ_Uk6hClJPFU4D9msHl3cXjN5e_9cH9QRQaKrljxjZqC7rjFD3AFauw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شهید حاج قاسم سلیمانی: ما در زندگی خودمان باید به الگوهای بزرگ نگاه کنیم؛ عمر ما می‌گذرد، تمام می‌شود، همه می‌میریم؛ اما انتخاب راه درست خیلی مهم است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/akhbarefori/679079" target="_blank">📅 01:24 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679075">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b6460030eb.mp4?token=RDjr1ZzWkqW7BAvAFE9Nof8Lq3xPclAN-Nyu00TOsWKzZZXZtFYwQx0mAL4UxqwsCibnPp18Lsuuw4dwB8oKHmCCgGoPJT6UtGfkJt_qPUa7mXjTELR7kqI2H_V7z8jcOOZKFLZrubBgJcfSOzac_h_B7ejB3O8cNCxjbYlhIBzMBRfb1vDxuLKJAJ3vYA7qOAffaa7fVSEiC1NuDNIZEr0UjbeIuydoNO0fcKiMjCfS5_gOZ5fxNWVTacEvP5Vw_jYEyJLaSsjzYHsWT10yb2ErTbs9gxTjEwTS8SuCdL2cU0zCLA71sFR_782RcFKelo9-C8NW4bqCmp1W_fm38A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b6460030eb.mp4?token=RDjr1ZzWkqW7BAvAFE9Nof8Lq3xPclAN-Nyu00TOsWKzZZXZtFYwQx0mAL4UxqwsCibnPp18Lsuuw4dwB8oKHmCCgGoPJT6UtGfkJt_qPUa7mXjTELR7kqI2H_V7z8jcOOZKFLZrubBgJcfSOzac_h_B7ejB3O8cNCxjbYlhIBzMBRfb1vDxuLKJAJ3vYA7qOAffaa7fVSEiC1NuDNIZEr0UjbeIuydoNO0fcKiMjCfS5_gOZ5fxNWVTacEvP5Vw_jYEyJLaSsjzYHsWT10yb2ErTbs9gxTjEwTS8SuCdL2cU0zCLA71sFR_782RcFKelo9-C8NW4bqCmp1W_fm38A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مراحل آماده سازی موکب هیئت "قرار" در محل "تپه سلام" مسیر منتهی به مشهد مقدس برای استقبال از زائران پیاده امام رضا(ع)
@Heyate_gharar</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/akhbarefori/679075" target="_blank">📅 01:04 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679074">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">♦️
در ۳ دقیقه ماجرای شایعات این روزهای دریای خزر را بشنوید!
@AkhbareFori</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/akhbarefori/679074" target="_blank">📅 00:54 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679073">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc78f30d4e.mp4?token=YJr2ukWTFxaemJ-rw0jhgPs8yG8kFKEL9mYef9Fl0dJ55IUAzvbiV8LhHeRg6OxQWSHvcr_lOOqiGVSSbO9v1OyiKwFdN7ykQTED4f5GrMdaAPPOiSAyrCETAQLv6DokiBCozXkegD2XxGGtXeVdjRLagmicGDX9Gdq3D-aiwCwiMj8xN0sJ0cEcXCawHxyZ987brDtqgQEw0nLBv1DqLLR40yWEDDUPi5RCFMr7RzhRu-Th45Q8-HLzcVQIh3sqdkpqUfPZ3Z9N2tAMyNln8ZCdbAijdhGNHKMaTpiU_xCi4DUP9--piasJNLoCGwNm3DmgrPL1zUvvFOuCfCG6pQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc78f30d4e.mp4?token=YJr2ukWTFxaemJ-rw0jhgPs8yG8kFKEL9mYef9Fl0dJ55IUAzvbiV8LhHeRg6OxQWSHvcr_lOOqiGVSSbO9v1OyiKwFdN7ykQTED4f5GrMdaAPPOiSAyrCETAQLv6DokiBCozXkegD2XxGGtXeVdjRLagmicGDX9Gdq3D-aiwCwiMj8xN0sJ0cEcXCawHxyZ987brDtqgQEw0nLBv1DqLLR40yWEDDUPi5RCFMr7RzhRu-Th45Q8-HLzcVQIh3sqdkpqUfPZ3Z9N2tAMyNln8ZCdbAijdhGNHKMaTpiU_xCi4DUP9--piasJNLoCGwNm3DmgrPL1zUvvFOuCfCG6pQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روزی به موشک‌ های ایران می‌گفتند آبگرمکن، اما امروز خودشان و اربابانشان از آبگرمکن ایرانی ترسیده‌اند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/akhbarefori/679073" target="_blank">📅 00:53 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679072">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4deefa9dfc.mp4?token=VCSVMTUhsxGV4-sp4cLaJibmlw4sFXC7AluKDraP4Unv6RrPa8HFzteRD_y_X4FuvQU-zxdhJkmU6aKXWLPlBUMPYZuJwAGCKE61Gn-lOtStT7uG2s0SCxkEjRxAhXmqn5LyW63OMKrtxx0AaLvqnpOZdpgnTTKvHS0xlju4fMMJKrUgyr1j_hBgrvvsjS2LfmQVv7diDmW_2BF4iGiddiDsD1O7QYtPZQrLtKKIlOxLt_4jcZL1oDJuapVpNF_IlAgTuJccc5S_niEtJIEffk7bpYQsTZ_NU8sm8NdSNSqLFyacCp-8dWanepvLyeCbFQX_EDzqu7bT7bmyBhr2LA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4deefa9dfc.mp4?token=VCSVMTUhsxGV4-sp4cLaJibmlw4sFXC7AluKDraP4Unv6RrPa8HFzteRD_y_X4FuvQU-zxdhJkmU6aKXWLPlBUMPYZuJwAGCKE61Gn-lOtStT7uG2s0SCxkEjRxAhXmqn5LyW63OMKrtxx0AaLvqnpOZdpgnTTKvHS0xlju4fMMJKrUgyr1j_hBgrvvsjS2LfmQVv7diDmW_2BF4iGiddiDsD1O7QYtPZQrLtKKIlOxLt_4jcZL1oDJuapVpNF_IlAgTuJccc5S_niEtJIEffk7bpYQsTZ_NU8sm8NdSNSqLFyacCp-8dWanepvLyeCbFQX_EDzqu7bT7bmyBhr2LA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تماشای فیلم اودیسه در سینما 4DX قطر؛ تجربه‌ای که مرز فیلم و واقعیت را شکست
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/akhbarefori/679072" target="_blank">📅 00:47 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679071">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7982f7e7c0.mp4?token=T8Qj8F0Z-aNW0u3iApHTUsvcuIwElrNhvuadgaWwkmZ_vjUyfSkS28IbZailCKIrolRxi-My-4HlWDjpao-qZtBwvTDhJzFf6I1WOCuMINPEwzmWe4eHQbJmQTgTu_Rg9utJoiR3gB-F2KdoyOX9oPJXimTlZdepJuaZVgeljf57ndozYRbqnHrqvRgF6VPXfPqtAwhYj9tkSrkA9mNfGd_dTZ9OiJD2bNZNNN1CYZZrvJpuxkNBc5_BDcCtOp1WwYBTl25fjoO17GYK_Htjt72odELQ9zTa1FeM1dWLekCZmolK8W6FNY1jBhvtsqxfU4o06vhjKsYhG1z8r-z1cg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7982f7e7c0.mp4?token=T8Qj8F0Z-aNW0u3iApHTUsvcuIwElrNhvuadgaWwkmZ_vjUyfSkS28IbZailCKIrolRxi-My-4HlWDjpao-qZtBwvTDhJzFf6I1WOCuMINPEwzmWe4eHQbJmQTgTu_Rg9utJoiR3gB-F2KdoyOX9oPJXimTlZdepJuaZVgeljf57ndozYRbqnHrqvRgF6VPXfPqtAwhYj9tkSrkA9mNfGd_dTZ9OiJD2bNZNNN1CYZZrvJpuxkNBc5_BDcCtOp1WwYBTl25fjoO17GYK_Htjt72odELQ9zTa1FeM1dWLekCZmolK8W6FNY1jBhvtsqxfU4o06vhjKsYhG1z8r-z1cg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آهنگ "گل یاس" که در وصف حضرت زهرا(س) خوانده شده بود توسط شادمهر عقیلی بعد از ۲۷سال بازخوانی شد
@AkhbareFori</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/akhbarefori/679071" target="_blank">📅 00:44 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679070">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🔹
خبرهای متفاوت هر روز را در وبسایت خبرفوری کلیک کنید
🔹
🔹
همه چیز درباره توافق مهم ایران و عمان بر سر تنگه هرمز/ این تفاهم جنگ را برای همیشه پایان می دهد؟
👇
khabarfoori.com/fa/tiny/news-3235999
🔹
افشاگری رویترز از علت تعلیق حمله به ایران
👇
khabarfoori.com/fa/tiny/news-3235850
🔹
اینفلوئنسر مشهور در پخش زنده کشته شد
👇
khabarfoori.com/fa/tiny/news-3235919
🔹
اعلام آمادگی یک نماینده مجلس برای شلاق زدن باقر خرازی
👇
khabarfoori.com/fa/tiny/news-3235825
🔹
عذرخواهی سحر دولتشاهی درباره استوری خود؛ قصدی برای بی‌احترامی به اذان نداشتم
👇
khabarfoori.com/fa/tiny/news-3235984
🔹
اخبار لحظه به لحظه جنگ ایران و آمریکا
🔹
https://share.google/8EImhrm9fBFYjsyZr</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/akhbarefori/679070" target="_blank">📅 00:39 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679068">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">♦️
رسانه آمریکایی MS NOW: عمان با چارچوب یک توافق موقت با ایران برای بازگشایی تنگه هرمز موافقت کرده است
🔹
هدف از این توافق، فراهم کردن زمینه برای برقراری آتش‌بس جدید و ازسرگیری مذاکرات هسته‌ای میان آمریکا و ایران عنوان شده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/akhbarefori/679068" target="_blank">📅 00:37 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679067">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
وقتی کلمات هزینه می‌شوند؛ ایثار، واژه‌ای که نباید ارزان خرج کنیم
🔹
امیر قلعه‌نویی می‌گوید پاداش صعود به جام جهانی را به‌جای دلار، ریالی گرفته و «ایثار» کرده است. اما آیا هر گذشت مالی را می‌توان ایثار نامید؟
🔹
در روزگاری که هزاران نفر بی‌هیاهو از حق و آسایش خود می‌گذرند، شاید بد نباشد واژه‌های مقدس را با دقت بیشتری به زبان بیاوریم.
🔹
گزارش امروز، نه درباره میزان پاداش تیم ملی، بلکه درباره مسئولیت ما در استفاده از واژه‌هایی است که نباید بی‌محابا مصرف شوند.
@Tv_Fori</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/akhbarefori/679067" target="_blank">📅 00:30 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679066">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OaxoYJHw9orPcl9UsLZldQccejYVSdGx0A4-MUgWAftmovH02TLn-CayOwfeDdKEdteKto8FInSWV6HxyNNh-cW8WQhpayd9_335iSGuZ783FdIC5nMzzPJaa0JxlIyzWrtlqIH3a70VGjZOdlxHkazdsyaCtfqZ1aHg_AjGhCWQS2fXlRRYJ_EKbT0f3q90xXMWuFfMUE4SScCE-yvoybtj4PXZpV9KxbfkH87wS-bBzLBgmZ2zfnpOOqkZph0ocmuLlgooMgKPwlQFx7gWV9STC8XlWv0_0sSb6gEtcQ5HG3hqxPvwRWYSh7e5rIP5fdoJgjGdSkm_WXcoXrHC3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
محسن رضایی: اجازه باز شدن مسیر دوم در تنگه هرمز را نخواهیم داد
🔹
اگر محاصره ادامه یابد، کشتی‌ها و نیروهای آمریکایی با خطرات و تلفات جدی روبرو خواهند شد.
🔹
ایالات متحده باید رفتار خود را تغییر دهد در غیر این صورت ما این وضعیت را تحمل نخواهیم کرد.
🔹
ما هرگز اجازه باز شدن یک کریدور دوم در تنگه هرمز را نخواهیم داد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/akhbarefori/679066" target="_blank">📅 00:29 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679065">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">♦️
خبرنگار: زلنسکی می‌گوید که کشورش نیاز فوری به باتری‌های موشکی پاتریوت دارد  ترامپ قمارباز:
🔹
ما هم موشک می‌خواهیم #Devil
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/akhbarefori/679065" target="_blank">📅 00:23 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679064">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c926eb53cb.mp4?token=S--kmcvn-3Na0mT07Nvedbp2kQS-kUO1WJ5WrGIpbi2hBLBPms_On_K_tm0U7E2XFvBAOwdVyzCD4uUINhinSMM2FNBHwcyTxrTi9kphAQOkLD1A9WQGlTCd3243vAf8huDjfc0-7R-nViX1pYrO4srAwLYQPT2CHk_lDFM8bJGs57UWxCB9Nsj13iWKVV6A41UrwLWVWOrlNp5AO9tntmoQUtm4x-2C3Naa2c8A0QoI9EFKFmxZvAfTpCQdP0PVRhEju1JzTODXxUb9z8fP7AMA8mkn481diHG_NQkk97IpLvlFGvdX0BatJWu9-7d7oIo6-uoovobr1vUnUKcGGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c926eb53cb.mp4?token=S--kmcvn-3Na0mT07Nvedbp2kQS-kUO1WJ5WrGIpbi2hBLBPms_On_K_tm0U7E2XFvBAOwdVyzCD4uUINhinSMM2FNBHwcyTxrTi9kphAQOkLD1A9WQGlTCd3243vAf8huDjfc0-7R-nViX1pYrO4srAwLYQPT2CHk_lDFM8bJGs57UWxCB9Nsj13iWKVV6A41UrwLWVWOrlNp5AO9tntmoQUtm4x-2C3Naa2c8A0QoI9EFKFmxZvAfTpCQdP0PVRhEju1JzTODXxUb9z8fP7AMA8mkn481diHG_NQkk97IpLvlFGvdX0BatJWu9-7d7oIo6-uoovobr1vUnUKcGGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خبرنگار: زلنسکی می‌گوید که کشورش نیاز فوری به باتری‌های موشکی پاتریوت دارد
ترامپ قمارباز:
🔹
ما هم موشک می‌خواهیم
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/akhbarefori/679064" target="_blank">📅 00:20 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679056">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nwuUxToA2f7TJZtz8GSH2ROvQtXxoAjzGlsiSYpAOF5sGVVrEOlC_aKMnFxjGkkLmZtkdR7_ZU3IByl64_o8c26UE8n3e2eLxKJOaXDXqsqj4wbgjbdtQeLH0aqh7ecJLAJ6qtkUZMWJ5gkYlybtxBefgFbVqhkeszxeMpqc4ZYZJ9Rqs849-lt06qAwUdhXK-QkHZ0Gz9qe9O6cLlbZRemGbPRxL3ygmhLlbR9BEqW1LBFKh9ffVstMMGMQOtLBlvkhmTbuaiYKq2UJJDT9jlI1HtyPxJPMQsVLw-UUL3C8ve02imZmMGjMOCsRbYPGnwmkgsESPgVLwVjtu06b5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BurOt3BNXTvCd_kruvXJQa2vBjWDHlmlOSMolPzmhp1C70Ogf5uJbhHBBS8ViLG-gQBqyoZHOur00hVqrOqDWSvpjh0HXlDxNJ3HUAq1T0sPu5_-Pr7w1mRxJ4jKCNfqOmjaz2fP6aXQvExOKb9Psg-qThHoP2zn2WqybnzQj4swvTQsL43g2ZCpsqss7Dh6cquLOrFLMwwa-l_-wFafeWL30FZoTWGF2t5wcRPNtVLpEn5i91Gn7syePw2OidimDfVgr0kWkP0ulJcUm_xCGFW-pvQ5hUM0GWskj5NFomIOD3A6oO3Du9OXVF3pnr5-NFNemUqW-BzaaXqw9_FM_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iyYIVGO52IDmfDqoexaXB1uVRI75XPg7yxscYJUfjh6LiFqL7lu-8OCsiFVqLUbzLzFoP3apAQ0Eyiz3mcYjMOnb0dXOPYqGOGkSNSfFtySBngjeMWxSMCmsyoDhTI1XRde66picHjF98Dci2hIu7GI7Wz5RkNczrsmDEmPiZFe34ceWA39YXR5pryr5yGK0TjfHsp55M-SqR0bBCwTE1gSC37ixsQNTAi0tKQYOV0HQIFJ36FWsUWcP9V06UWO_D7r1LwknDlDU8Y0NINa65aelKPXpfWywx_NMmvpPWTtChZvmW9USWfgC-nrpuaUkigmK_adrUxY4iQTZ8HYjMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X_xtXiengKtsrnhryD7hklwkUELgBADO3LHI8p85_U0hv96sY_aweKPr6UPQpJN13ZjcMa4XSdARzz4tUjMBnKAbOo6oQC3DTFNLY1D913uOJtITkzyDpy7s0HBvUQPTFQoAjAx1ZICddze9-HD5kAljJAJldWnomLyRC2lC-sLWZhUvj29Qwec0BeIUVyvk75r3DjzHIdGVWnf-s3tWQV8TDNCErPeFRj4JqB7NFy_cXyGHwm9XetNoyYKXMRVC2N10OPCGLn8PE7hlRBCV_rIjsutw-DK2NcK36AWU2u0-E8C4-RAO8XSXkM708-bnCC0AQ-3Hcad1fieThcbk3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NtoSOaqRD837HZUEDc5d6793Sqlkl54IYhm81pxH8jn4dt-kEV9GDMhNqgotKKRN5sk5nWx7dbEFhCsi8uQW2h-sWElYuRWtP8LbKoEJoGaBAU7ghKVk2Xqh72pOCBcXxWv7IPze7zlMlKMn3n9BYK88EhBrWp8vmQugQUYBxKiIKfXgu_xr3eWCmIoea5PmHPsvtlp4bfS92shf3G9LvKhKj0fBKNDBV3LOA385ja0HEF1Jtk9VaqXArcQDnZ107vdppzwVuGAa0WP2rxrojpDJpLjkgCkqKTmGLwl_MEfZrnqPfOsTzsBHcZhK15z964CnKFru6dobbEnHwNwSVQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">واکنش کاربران به قطع اینترنت در دوران جنگ
🔸
بر اساس نظرسنجی ایسپا، ۴۶ درصد کاربران اعلام کرده‌اند که در زمان جنگ از قطع اینترنت بین‌الملل به‌شدت عصبانی بوده‌اند و ۴۷درصد آنها گفته‌اند از این تصمیم عصبانیت کم یا اصلا نداشته‌اند.
🔸
در این دوره، صداوسیما با ۳۹ درصد، اصلی‌ترین مرجع کاربران برای پیگیری اخبار بود. پس از آن، شبکه‌های اجتماعی داخلی با ۲۱ و شبکه‌های ماهواره‌ای با ۱۴ درصد، در رتبه‌های بعدی قرار داشتند.
🔸
اختلال در ارتباط با دوستان و خانواده با ۳۸ درصد، مهم‌ترین مشکل ناشی از قطع اینترنت برای کاربران بود. پس از آن، سرگرمی  با ۳۳ و کار و درآمدزایی با ۲۹ درصد در رتبه‌های بعدی قرار داشتند.
📊
آمارفکت | مرجع تخصصی آمار کشور
@amarfact</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/akhbarefori/679056" target="_blank">📅 00:11 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679052">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e3f5ae7020.mp4?token=Lhfqrva2pLM9zsMwZREnXwkAsWBWvtGmtDZ0aKb_lqB5dvz-5FYbCZadRrDT_gSG7cURV1CNoeKzgfCD8viuw2dTGzR1DtzRzSIEXTxb4IoqEKnKyWzo_Rpv2Ce4JsmMNh-8uNhb7jxuTJZ_9YYJp3Jma2JQuHPszBvH2XG2JEhsclISbI_1f50S5B9iewCEhXfq5NfrYAg77vk6SKadr2ZmTcuGAP5JtL3WjBWvy0hmkfn5JCGBM0Hxuc0fNRmpseHgw_hgVS9_1pDnp-dZXhGAOxuQ1cD2ZUrWnmmwOtJcufuyX3XqlikMCr2c9IoZaLoW04381r_oRWKvaEL_Uw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e3f5ae7020.mp4?token=Lhfqrva2pLM9zsMwZREnXwkAsWBWvtGmtDZ0aKb_lqB5dvz-5FYbCZadRrDT_gSG7cURV1CNoeKzgfCD8viuw2dTGzR1DtzRzSIEXTxb4IoqEKnKyWzo_Rpv2Ce4JsmMNh-8uNhb7jxuTJZ_9YYJp3Jma2JQuHPszBvH2XG2JEhsclISbI_1f50S5B9iewCEhXfq5NfrYAg77vk6SKadr2ZmTcuGAP5JtL3WjBWvy0hmkfn5JCGBM0Hxuc0fNRmpseHgw_hgVS9_1pDnp-dZXhGAOxuQ1cD2ZUrWnmmwOtJcufuyX3XqlikMCr2c9IoZaLoW04381r_oRWKvaEL_Uw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خبرنگار: آیا توافقی برای بازگشایی تنگه هرمز حاصل شده است؟  ترامپ متوهم:
🔹
نمی‌خواهم بگویم تمام شده است، اما به نظر می‌رسد در حال حاضر باز است. ما تنگه را کنترل می کنیم. #Devil
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/akhbarefori/679052" target="_blank">📅 00:06 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679051">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f10f13cb18.mp4?token=oKpM-LNjI0XYnD-4Dz3iQnTSEw66PAsUNd2i5P-nm4fxOZ_Fss7l40mY6wDRDy156w6maYTEECSK6l1YGixJ-7vHbqle_B59Q2fevecbRIn1YiioTvzLp4DxF5_lbr-HXjGNqHBPRiMARMnSxuKaSyfpFcMbS88d6Nm7KV5_N8_x_kQDslN1uTPruimj3MGdryATGv44-vKIoOSwqOd5STLI-v22GUPJbFw7uZZA7_AVCp06ebYE3O56HRR15EVMWY7S6Z3GseObs8QLM_R-DfvWbbZKArLCkhWWXbVhK1hpTMSC6GV-MKQaKuwljRSRARtqZ0nCJOOtalrznnLETA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f10f13cb18.mp4?token=oKpM-LNjI0XYnD-4Dz3iQnTSEw66PAsUNd2i5P-nm4fxOZ_Fss7l40mY6wDRDy156w6maYTEECSK6l1YGixJ-7vHbqle_B59Q2fevecbRIn1YiioTvzLp4DxF5_lbr-HXjGNqHBPRiMARMnSxuKaSyfpFcMbS88d6Nm7KV5_N8_x_kQDslN1uTPruimj3MGdryATGv44-vKIoOSwqOd5STLI-v22GUPJbFw7uZZA7_AVCp06ebYE3O56HRR15EVMWY7S6Z3GseObs8QLM_R-DfvWbbZKArLCkhWWXbVhK1hpTMSC6GV-MKQaKuwljRSRARtqZ0nCJOOtalrznnLETA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای ترامپ جنایتکار: فکر می‌کنم جنگ به‌زودی پایان می‌یابد/ تصور نمی‌کنم آنها بتوانند بیش از این ادامه دهند #Devil
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/akhbarefori/679051" target="_blank">📅 00:03 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679049">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9f68b3d99.mp4?token=eTqWoQjBtFSrfGr-S0uCfRUnPWHwd1BqfNg3O1jMPSssNN-nZ1cI8RYG38JleJ6Y6Wne2YByq9lRhmOHapP67ZUcjn86vVm2XlqIWpVidwwxtmXY97vFboKsESLtrTBmqtQuVjDUifHM0L_31ZM31RzZ4CaGGVQT6OH9ekikk2tPVEi1TSu2mINx5a4W9GNUekgLzfOzNhS1E_7t7sGhI1jb5E35oO7eK02eqRjklp_0CNqkVS3jXc7wCN9gNg9ctyYaFFhYPtc8Y9EzMvTAfXoJpMOUFfh0HV589YTwVO50EV0j0i7qafRXPlx_-lq_2OigNRq94OCg1XppB4SSvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9f68b3d99.mp4?token=eTqWoQjBtFSrfGr-S0uCfRUnPWHwd1BqfNg3O1jMPSssNN-nZ1cI8RYG38JleJ6Y6Wne2YByq9lRhmOHapP67ZUcjn86vVm2XlqIWpVidwwxtmXY97vFboKsESLtrTBmqtQuVjDUifHM0L_31ZM31RzZ4CaGGVQT6OH9ekikk2tPVEi1TSu2mINx5a4W9GNUekgLzfOzNhS1E_7t7sGhI1jb5E35oO7eK02eqRjklp_0CNqkVS3jXc7wCN9gNg9ctyYaFFhYPtc8Y9EzMvTAfXoJpMOUFfh0HV589YTwVO50EV0j0i7qafRXPlx_-lq_2OigNRq94OCg1XppB4SSvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای ترامپ جنایتکار: فکر می‌کنم جنگ به‌زودی پایان می‌یابد/ تصور نمی‌کنم آنها بتوانند بیش از این ادامه دهند
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/akhbarefori/679049" target="_blank">📅 00:00 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679048">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v6pXcsm9fhnw0IGs8nF5DKGzmSkdthYv5UTnZq7PNCYhzoQTCGZAKfGpn6WS_lNDHHPOy2zoLguB8gbY07tg3SkykPRvPazdpV49dh6VU87-Moa5rniIhj_tR900nsy2OC3UGgV6J2b0U29ZoODOapCnTdyVH1fMBAAewRrMju0KtJfnVcN_Oul_P_ms3s65ZZmerTf0jYHBm2ms0JvSHKXFk_zfsJsR2kZ3weCITacJZ-jQ0_7GP-w-pmmEvOOtRtdRd4wCK381BTi6kxgM82tnCehiIAc94-Y10NyCAswGF48azNcq9lzKMXStvl4Bt3j5ecMwZFlxfCKvoRYIyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/akhbarefori/679048" target="_blank">📅 00:00 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679046">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pOF9JFKDZSuZ4JMRE7vM_P9lVPMzoGgAB5RBIc5Whe2znRGhjr_5Lt_drhdNFwVnpxG-tdcIdL_3CcphF2zUgv2sthMxsXVoIjmfQJgcw2A1HvWnNEWhGi6cIpvazU4zgHs72RR18odKvPFAM32ov9Lb4L3gngZms-Eg97uCc5kFr6BrxXnA7sWUIseFBSnYelsadhHFUJGFI7Rax2eXA1jk0eB8oYIlhK4fcNk7ROrI7J_sJR_Q6llvi2aLz7CJjTm2jPdAuLUEYzF1nk3OnSW16JG6VogdJwc7_m9v831_lUXRJcODwgNXp9rUDSqLJihiYXR2rod-iq5OXnpXow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ته دیگ
🔹
رسانه‌های غربی خبر دادند که وزارت جنگ آمریکا پس از تماس تلفنی خشمگین دونالد ترامپ با پیت هگست، قرار است یک جلسه اضطراری مختص به کمبود تسلیحات برگزار کند. سی ان ان هم بنا به گفته دو منبع آگاه اعلام کرد که ارتش آمریکا در جریان جنگ با ایران بخش قابل‌توجهی از مهم‌ترین موشک‌های رهگیر خود را مصرف کرده است؛ به‌گونه‌ای که حدود ۸۰ درصد از موجودی موشک‌های سامانه دفاع موشکی تاد و نزدیک به نیمی از موشک‌های رهگیر پاتریوت از زمان آغاز درگیری‌ها مورد استفاده قرار گرفته‌اند. این گزارش نگرانی‌ها درباره کاهش توان دفاع موشکی آمریکا را افزایش داده است.
🔹
هشتصدوبیست‌ونهمین شماره جلد یک خبرفوری
#تیتر_یک
@rozname_fori</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/akhbarefori/679046" target="_blank">📅 23:41 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679045">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">♦️
آیت‌الله جوادی آملی: با ناقضان وحدت مبارزه کنید
🔹
حضرت امیر یک بیان نورانی دارد که بالاخره ما جامعه را متحد کردیم، و تمام کوشش دشمن این است که این جامعه را ارباً اربا بکند. شما مواظب باشید این جامعه متحد، مختلف نشود، پراکنده نشود.
🔹
اگر کسی خدای ناکرده عالماً عامداً دارد این وحدت اسلامی را به هم می‌زند، با او مبارزه کنید، ولو عمامه من بر سر او باشد!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/akhbarefori/679045" target="_blank">📅 23:32 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679044">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e6898fed19.mp4?token=mGt0xp2mN4ZlqZ8LfyDPcy1IhtnRV84n8Voc1XYB8RpB4kPuuzlv3PHD9QJtfAz-XvPkVne0wl-Wz4TWpWG7IRFOMUT1dVHGGxaq1NmfCsKKGPfOWzaVwVKIEtlKzB_D8MgNI_GZ-El4UU-HIHiTg6OHVwxhxDApIU50o7df5LBfkpJv08ZHzGm2YqnT1Yny6u-BuIIGHPYLt4blQZ4IPjiyVhl_OS9i3yvnIcI5FV5UrO46iMY93ciduNOYUy_H7lKWWafEQsvFkSM2JBbd3ntf0e69DTSWFYseRWMWTY92mtTpkaqeLdkSyqUX_LWwNDG5mMbqGEtwr-4wVtLFuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e6898fed19.mp4?token=mGt0xp2mN4ZlqZ8LfyDPcy1IhtnRV84n8Voc1XYB8RpB4kPuuzlv3PHD9QJtfAz-XvPkVne0wl-Wz4TWpWG7IRFOMUT1dVHGGxaq1NmfCsKKGPfOWzaVwVKIEtlKzB_D8MgNI_GZ-El4UU-HIHiTg6OHVwxhxDApIU50o7df5LBfkpJv08ZHzGm2YqnT1Yny6u-BuIIGHPYLt4blQZ4IPjiyVhl_OS9i3yvnIcI5FV5UrO46iMY93ciduNOYUy_H7lKWWafEQsvFkSM2JBbd3ntf0e69DTSWFYseRWMWTY92mtTpkaqeLdkSyqUX_LWwNDG5mMbqGEtwr-4wVtLFuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آنچه داوطلبان ورود به دانشگاه فرهنگیان باید بدانند
/ تلویزیون اینترنتی مدار
این برنامه را کامل ببینید
👇
https://aparat.com/v/xffqtvr
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/akhbarefori/679044" target="_blank">📅 23:29 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679043">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
فعلا خبری از کاهش مدت تحصیل کارشناسی ارشد و دکتری نیست
رمضان رحیمی، دبیر کمیسیون آموزش مجلس در
#گفتگو
با خبرفوری:
🔹
طرح کاهش مدت تحصیل کارشناسی ارشد به یک سال و دکتری به سه سال، که آذرماه ۱۴۰۴ مطرح شده بود، صرفاً یک پیشنهاد مقدماتی از سوی وزارت علوم بود و به دلیل شرایط جنگ و مسائل دانشگاهی فعلاً مسکوت مانده است که با عادی شدن اوضاع مجدداً در کمیسیون بررسی خواهد شد.
🔹
امید می‌رود این طرح‌ها سال آینده به صحن علنی مجلس ارائه شوند و اجرای طرح کاهش مدت تحصیل مقاطع کارشناسی ارشد و دکتری به امسال نمی‌رسد.
@Tv_Fori</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/akhbarefori/679043" target="_blank">📅 23:24 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679042">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7238929701.mp4?token=p4cCJOIXY6DpmgFiMQq5HoMq4A0Jsf4z8neuQKvLnyZa9sUF7IGOTG09LhIRNbtgmPeHyOMYxyJZQQ9fh3Y9OWoSSel30FkDvYoeGgq-rpM0kflNbQxQF1m4PNE4O-WIJT7FqTDSQPCeqMWH-31EGJgBCGbvj9bM6uOmgTzslhVn91HklQsJu9ZFJZxV7PDt98ZmDYr-q4P1GVRFc6qijMYvgrH_5BfD7hI-My08v5_1o5jB7zsp2M4CcUDwj4IbP9lgZ80uxQ4Zv2QBsQZw7SfvPjQB6oTuRJxGpMJ_PpRSCkzovitH-zYQHh3evoLWutcElEfZPCEYShwW_vRByA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7238929701.mp4?token=p4cCJOIXY6DpmgFiMQq5HoMq4A0Jsf4z8neuQKvLnyZa9sUF7IGOTG09LhIRNbtgmPeHyOMYxyJZQQ9fh3Y9OWoSSel30FkDvYoeGgq-rpM0kflNbQxQF1m4PNE4O-WIJT7FqTDSQPCeqMWH-31EGJgBCGbvj9bM6uOmgTzslhVn91HklQsJu9ZFJZxV7PDt98ZmDYr-q4P1GVRFc6qijMYvgrH_5BfD7hI-My08v5_1o5jB7zsp2M4CcUDwj4IbP9lgZ80uxQ4Zv2QBsQZw7SfvPjQB6oTuRJxGpMJ_PpRSCkzovitH-zYQHh3evoLWutcElEfZPCEYShwW_vRByA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تیم اندرسون، نویسنده و پژوهشگر: تفاوت فرهنگ عربستان و عراق را می‌توان از نحوه برخورد نیروهای امنیتی آن‌ها با زائران دید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/akhbarefori/679042" target="_blank">📅 23:19 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679041">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nL7WAZZCT-1oHrvNFePTlWCJhpORDKavNya4UCeFmFfcBFIu56BGqtlBw7Y1dTaZ0ylcoBriK2vUpqKZBw1Xg8J0Xq-GsVkMzlh9qmR6cCZiKKl8A1L-N58e3izMutj0gez5SMXVePwmdknIDPzNt-G3xRnF7aacgIDgUAO7ql583SXI9oWWkHk3hf4rvXG7wFd_91A81BcPCB_bKOMUoZqBijyCBb7ayjWjR6DkoSAgalJ_DTq9KCOaPOv07qCoKKplxjom1Ql-PNDMifqAdM2ULf-Lg-vB0Ht34y8367Pa0EsL0JHGpdUyAI0xj7KRzdFSq5qjgf7qat7nAmPxHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پایان ۴ دهه واردات نفت از عربستان؛ آمریکا به سراغ ونزوئلا رفت
🔹
برای نخستین‌بار از سال ۱۹۸۵، واردات نفت خام آمریکا از عربستان سعودی در ماه جولای به صفر رسید؛ تغییری بزرگ در نقشه انرژی جهان که پیامد مستقیم تنش‌های نظامی در خلیج‌فارس است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/akhbarefori/679041" target="_blank">📅 23:17 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679040">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/039b2e86ac.mp4?token=Uadk14OT4LMSq31SBAABJYA39TLB5vnUUpNvTzWyZyDCdGzIVzar1MhoO8UXsQpMydcguNKvSkFgoSiTRHOhkx_u5dFhKSUQBlfQKxxjImXSwLvHJsuPmTjubT3EUmJvesiPG1o5q2168EHchnMryf17MRe_uSeGg9FgxoYQO8Eaq-6Sm8wmW5JcE4GcTEu1sgo6CEHFTcjLi3wGZvrgQayKNabSfXRJo9x-T_bTC7jZBmWHlRrlZy65xVleT_dSpwMCz2LeE59RwK-FB5h4GiI1w69cHR4f_kwpyffwBal3vG4oQGzVi5OagYQUOcmt_M3_UzYv4v-ZHhQRbgxYNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/039b2e86ac.mp4?token=Uadk14OT4LMSq31SBAABJYA39TLB5vnUUpNvTzWyZyDCdGzIVzar1MhoO8UXsQpMydcguNKvSkFgoSiTRHOhkx_u5dFhKSUQBlfQKxxjImXSwLvHJsuPmTjubT3EUmJvesiPG1o5q2168EHchnMryf17MRe_uSeGg9FgxoYQO8Eaq-6Sm8wmW5JcE4GcTEu1sgo6CEHFTcjLi3wGZvrgQayKNabSfXRJo9x-T_bTC7jZBmWHlRrlZy65xVleT_dSpwMCz2LeE59RwK-FB5h4GiI1w69cHR4f_kwpyffwBal3vG4oQGzVi5OagYQUOcmt_M3_UzYv4v-ZHhQRbgxYNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
واکنش پزشکیان به اقدام مادر کردستانی که پول دیه دخترش را خرج مدرسه‌سازی کرد
🔹
این که شما پول و سرمایه داشته باشی و ببخشی، یک موضوع معمولی است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/akhbarefori/679040" target="_blank">📅 23:14 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679038">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PCAYgEn1oVORAbMb9ViOY5c4rXiT9ZPar8hM1jaIfmpHaseb81QTtvHU_MKEa1hNs--Gpqn1qtjfHTESCqsNhxa-Oy8wqXKRdsyOW66oHMAiKLniz4Tw0p9EYeM-KTrHeI7DDyEn8VaV-_NVv55Oc5HldCNAO24B_12Tu0Olx9fdoS4MKwB47BBkwTsf_6fg_V_z_ikKvFI8A5EgGV2KuPcGv-iGwMe8_naXFV-Q8W2tR__9QmNx1crwm5249PJ1CoMdUE49BVlBTraS0Watov7pWpYauGLCvUhO45Qk0usuB9kjD7ncCCyGiN1oLxztiH6pzaYIHf-l10-bVYQfcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
«نوستراداموس چین»؛ پیش‌بینی جنجالی درباره جنگ علیه ایران | دو پیشگویی قبلی او که محقق شد چه بود؟
🔹
در دنیای پرشتاب رسانه‌ها، جایی که پیش‌بینی آینده ژئوپلیتیک جهان اغلب به گمانه‌زنی‌های دیپلماتیک محدود می‌شود، ظهور چهره‌هایی که با رویکردی متفاوت به تحلیل رویدادها می‌پردازند، همواره توجهات را به خود جلب می‌کند.
در خبرفوری بخوانید
👇
khabarfoori.com/fa/tiny/news-3235477</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/akhbarefori/679038" target="_blank">📅 23:09 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679036">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qGpZJDKu5d-0ziPVuIzlt2w1TyioRH6YEAL1ffYOai7bVBCMnoL8otX08VBq7GmvKbTHe3J_hcEde9f6MQjAtgPConsX9ol3BPDYayU4S71Dnk9JsGM7WCdqyNniOTsjZBoJRfrLRQGDKRcoC2kcY16z7D2RPStJSIuiosxvEumQZK9VCsqK0uILPnKUjREE8Do_oIIK-HL5ixMv0C-IGfYsR6Hq2VSuxZUFvOSHMS1sEtSoC1617QgEUPTJoPF5ez0EGdRPAp9CqWWW15p3cbOUPTsE5im5JZXPAmgHnGOj9nVmZwBePOhkeLaAr1H9Tr6AMB25hjEr3-UIoDGYTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آدمی پشت واژه‌هایش شناخته می‌شود
🔹
امام علی(ع) در نهج‌البلاغه یادآوری می‌کند که حقیقت شخصیت انسان، پیش از سخن گفتن پنهان است. واژه‌ها می‌توانند میزان خرد، شخصیت و نگاه ما را آشکار کنند؛ پس گاهی یک لحظه سکوت و اندیشیدن، بهتر از سخنی است که نتوان آن را جبران…</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/akhbarefori/679036" target="_blank">📅 23:01 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679035">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبانک تجارت | Tejarat Bank</strong></div>
<div class="tg-text">🎬
#تماشا_کنید
✅
حضور فعال بانک تجارت در قلب عسلویه
💫
پروژه بازسازی فازهای ۴ و ۵ پارس جنوبی با بازدید میدانی دکتر اخلاقی مدیرعامل بانک تجارت کلید خورد.
📌
گامی بلند برای تأمین مالی، بازسازی و بازگشت سریع‌تر این پروژه ملی به مدار تولید.
⬅️
دکتر اخلاقی: ما در بانک تجارت، نه فقط یک تأمین‌کننده، بلکه همراهِ عملیاتیِ صنعت نفت، گاز و پتروشیمی برای حفظ اقتدار انرژی کشور هستیم.
مشروح خبر
👉
📱
tejaratbankofficial
📱
TejaratBank
📱
TejaratBank.ir
🟢
TejaratBank
🟢
TejaratBank
📲
TejaratBank</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/akhbarefori/679035" target="_blank">📅 23:00 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679034">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9740cd9b11.mp4?token=Ckh9zdEUcb4_J2-2vjUboVsbqCMRWgLfd6kH0ccuVjISNCT9DMz7c2AHDl1ZA7GlxhlOmz6AaSw7fqbAcWpgPpV2p25UgJpZzBPXw6gDiG1clD9ooQz83wqUa7mKtemxoQLj0Vy_EK5YE9Q8QFuoqGA3BCabvAZYP76Y7xKqJIwMpRBK6tVsaQahhZmnd6F-s152UFQ_2lfMorU0ROJ5YL6kQRZCql2itxVmCra6rBfD57wfpjU3mRK_ThYm6wYOJ5koMH-VKyhJN9TrfNb3NlKdwVn0x_y1-imPM5G3HQqeNXqJwWnx-Jmcr08CU17fyxoJeFwp2BY_4_LFpYxYmTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9740cd9b11.mp4?token=Ckh9zdEUcb4_J2-2vjUboVsbqCMRWgLfd6kH0ccuVjISNCT9DMz7c2AHDl1ZA7GlxhlOmz6AaSw7fqbAcWpgPpV2p25UgJpZzBPXw6gDiG1clD9ooQz83wqUa7mKtemxoQLj0Vy_EK5YE9Q8QFuoqGA3BCabvAZYP76Y7xKqJIwMpRBK6tVsaQahhZmnd6F-s152UFQ_2lfMorU0ROJ5YL6kQRZCql2itxVmCra6rBfD57wfpjU3mRK_ThYm6wYOJ5koMH-VKyhJN9TrfNb3NlKdwVn0x_y1-imPM5G3HQqeNXqJwWnx-Jmcr08CU17fyxoJeFwp2BY_4_LFpYxYmTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پزشکیان: بهترین روش آموزشی دنیا را باید مستقر کنیم
🔹
باید بهترین روش آموزشی موجود در دنیا را در کشورمان پیاده‌سازی کنیم.
🔹
باید هر روزمان بهتر از دیروزمان باشد، اگر این نگاه را در فرزندان خود ایجاد کنیم، قطعاً پیشرفت خواهیم کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/akhbarefori/679034" target="_blank">📅 22:55 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679033">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64880a95c9.mp4?token=qgkpCED9ZsN_tDZU4T75SDS8nz7pJOFOIh1yGxQobQNWmXWGqLS8jYcDiPOmXPuEWK6u2CsWWkoaQhsfoQKacXFR_RTBMpuvB7p-uoZulhBwk7B4CWIlYbtDW3BWyE8TGjWgPXHbBOCDBX_gbYXiSLLayA7Ap2t6xOA0ZtayMrSXbUpX1C6dVjODOmpj5E5DcU4pIw20v4_JsET0gcbUnlRX4kVR1XnhvMhjmTN4XtnRJVE3apPlcfxqFBGMVmSdXijUXmEt14jbRciJT-0gZOhzBZhtb-cecKHYZNAOr43-80SOWix3D4yzK5_yTcMRNowlLRcE5UjWKaCJ73k6ig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64880a95c9.mp4?token=qgkpCED9ZsN_tDZU4T75SDS8nz7pJOFOIh1yGxQobQNWmXWGqLS8jYcDiPOmXPuEWK6u2CsWWkoaQhsfoQKacXFR_RTBMpuvB7p-uoZulhBwk7B4CWIlYbtDW3BWyE8TGjWgPXHbBOCDBX_gbYXiSLLayA7Ap2t6xOA0ZtayMrSXbUpX1C6dVjODOmpj5E5DcU4pIw20v4_JsET0gcbUnlRX4kVR1XnhvMhjmTN4XtnRJVE3apPlcfxqFBGMVmSdXijUXmEt14jbRciJT-0gZOhzBZhtb-cecKHYZNAOr43-80SOWix3D4yzK5_yTcMRNowlLRcE5UjWKaCJ73k6ig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پزشکیان: بهترین روش آموزشی دنیا را باید مستقر کنیم
🔹
باید بهترین روش آموزشی موجود در دنیا را در کشورمان پیاده‌سازی کنیم.
🔹
باید هر روزمان بهتر از دیروزمان باشد، اگر این نگاه را در فرزندان خود ایجاد کنیم، قطعاً پیشرفت خواهیم کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/akhbarefori/679033" target="_blank">📅 22:51 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679032">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">♦️
منشأ صدای انفجار در قشم، هدف قرار دادن اهداف متخاصم بود
منابع آگاه:
🔹
علت شنیده شدن صدای ۲ انفجار در قشم حوالی ساعت ۲۱ و ۴۰ دقیقه پانزدهم مرداد، مقابله با اهداف دشمن متخاصم در ورودی تنگه هرمز بوده. دستاوردهای این مقابله دریا‌دلان نیز در ساعات آینده به اطلاع همگان خواهد رسید.
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/akhbarefori/679032" target="_blank">📅 22:50 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679030">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef8d84e289.mp4?token=MjByVNCyXS3PNtBWC6-nFnJ8oMYujyHg1If77bGnZm-x5Lc9OHlCYMejo-6YdRyWCgu2jqplh4fW-I_H4C-rCllUKaIrebV7mqdj_BucLIKeo5D6khEzrGcKT4VNzsJj6ofRRSqc4c3gk0LMDUN95CAAotmITVy-UuSAVFFGx4aUWGxiGtK5t1kWB5MLxVR_ckq_xkWFmerw-NetYYdfodn_BXZm3rGkIJJXQKb8LI-qY68TFt5wYqhgVbDu3638bZfqZdSdNH0j2FY1KOEWnEzcM9oBXKb0b9rPrZooC7i_WxUz0AQBruVDRa8_e3HWZghlui65Sa0QxpZX2K4gcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef8d84e289.mp4?token=MjByVNCyXS3PNtBWC6-nFnJ8oMYujyHg1If77bGnZm-x5Lc9OHlCYMejo-6YdRyWCgu2jqplh4fW-I_H4C-rCllUKaIrebV7mqdj_BucLIKeo5D6khEzrGcKT4VNzsJj6ofRRSqc4c3gk0LMDUN95CAAotmITVy-UuSAVFFGx4aUWGxiGtK5t1kWB5MLxVR_ckq_xkWFmerw-NetYYdfodn_BXZm3rGkIJJXQKb8LI-qY68TFt5wYqhgVbDu3638bZfqZdSdNH0j2FY1KOEWnEzcM9oBXKb0b9rPrZooC7i_WxUz0AQBruVDRa8_e3HWZghlui65Sa0QxpZX2K4gcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روایت زائر استرالیایی که به کمپین نظافت مسیر اربعین پیوست در برنامۀ پرچمدار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/akhbarefori/679030" target="_blank">📅 22:48 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679027">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac440038d6.mp4?token=gFqyc0yj0Sg8BakSb2IiVvu-63YIz_u79qc5ucSVLADpElgqkw8OfE-uwQGyEc4WeMZDY9h9TYlLlsj5-Ax2hK2HGZaSDhZVZV3A5yceu6D2p_O0VzX8_fVKqNRmGoaaHJrCZBKOzoLBHbrMp2KXU6SgIcpMesQkSQk1OMTqx10cXUmJtvq_g6n9CH2YDFCaaCSRpZUnHaLt1AEWxz79wVvtnrrZ4-O2VOrAnzXLQ6f6-tn82WOG9yMQ6znY4DlCaTqd2Pv00kAQ5ACpAruIM6Ty0DM4jdnaHm0ahfBoK_i_XxEXqSbfRaLWKuXVossOWBIwfGR84utyWpVKx7Cdzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac440038d6.mp4?token=gFqyc0yj0Sg8BakSb2IiVvu-63YIz_u79qc5ucSVLADpElgqkw8OfE-uwQGyEc4WeMZDY9h9TYlLlsj5-Ax2hK2HGZaSDhZVZV3A5yceu6D2p_O0VzX8_fVKqNRmGoaaHJrCZBKOzoLBHbrMp2KXU6SgIcpMesQkSQk1OMTqx10cXUmJtvq_g6n9CH2YDFCaaCSRpZUnHaLt1AEWxz79wVvtnrrZ4-O2VOrAnzXLQ6f6-tn82WOG9yMQ6znY4DlCaTqd2Pv00kAQ5ACpAruIM6Ty0DM4jdnaHm0ahfBoK_i_XxEXqSbfRaLWKuXVossOWBIwfGR84utyWpVKx7Cdzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پزشکیان: آموزش حق همۀ مردم است؛ نه فقط پولدارها
🔹
حاکمیت باید بستر آموزش مناسب برای همه مردم را فراهم کند.
🔹
اگر امروز جوان ما مشکل دارد؛ مقصر ماییم، نه جوان مملکت. ما نتوانسته‌ایم درست آموزش بدهیم و آن‌‌ها را توانمند کنیم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/akhbarefori/679027" target="_blank">📅 22:41 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679025">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f645eb026d.mp4?token=IrTOMMaT1NaQI0Uyo7xu7opBVhY8u1n0sUR1GP5l1cqA0JPlXa7GBdNmh3lwYZ7njqLQ6M8BsLdGZ1dJPw2fg1vOj5iO9IidvOFaFuVKQ--1nulsnL1CA-XrpxFP1OqnmNsNotSKj7-_jJlrFFWhplxGP6sT20UH0U68N9nlkEb4UBIGjs5hrwV9mxZdk2oVUGfLHz_YxLNCP768JUu9KNx-m03KBe0y3doYNogJk-bx4K085IH3i_17NnOnBR69SyrkPH6VBYXTih53DIvS0AZ7Tu8aGSMBHe2QwSq8gncHU76HNSfxHTC_GQaW3mp9FbGHrSlyRVivPbVqy8JeoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f645eb026d.mp4?token=IrTOMMaT1NaQI0Uyo7xu7opBVhY8u1n0sUR1GP5l1cqA0JPlXa7GBdNmh3lwYZ7njqLQ6M8BsLdGZ1dJPw2fg1vOj5iO9IidvOFaFuVKQ--1nulsnL1CA-XrpxFP1OqnmNsNotSKj7-_jJlrFFWhplxGP6sT20UH0U68N9nlkEb4UBIGjs5hrwV9mxZdk2oVUGfLHz_YxLNCP768JUu9KNx-m03KBe0y3doYNogJk-bx4K085IH3i_17NnOnBR69SyrkPH6VBYXTih53DIvS0AZ7Tu8aGSMBHe2QwSq8gncHU76HNSfxHTC_GQaW3mp9FbGHrSlyRVivPbVqy8JeoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رئیس‌جمهور: ما باید بتوانیم در کنار ایجاد بزرگراه و آزادراه؛ کریدورهای ریلی کشور را هم تقویت کنیم چون هم سوخت کمتری مصرف می‌شود و هم سرعت تخریب جاده پایین می‌آید؛ در همین راستا قطار چابهار به زاهدان در هفته دولت به بهره‌برداری می‌رسد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/akhbarefori/679025" target="_blank">📅 22:37 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679024">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b11217e8c.mp4?token=l10Fw9zaADCzji9qXBYMBC8_MNrwKWdwwAqOYKW1ZB0IVYCwMWvRLO5nTQBY_4-K9Hy0GyNfiLbD8ZfhZOoSAG3g8Dla_dnqAzs5VhQXVWn8TnIRVgRrPFYP-LMqtaIV_RxfFgEYoarKxmH3Kkaj2yajtkFcK4dqAP9JeSUJHvA-dmHPEBzT_2s75rnVF11b0FmittaRrVubMLX3mCCtUSjD30NGfqAj7gKOAsJUwXy_B6WK-2DsciKbmQA3eeNrK_lzsq3Vst604qBT8MEWQwFoluSdJSdbtbTWtRqrFBJaT5Ay3JmKY4wytMQulGmci-1DDEUN9BIQT13YkP4f_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b11217e8c.mp4?token=l10Fw9zaADCzji9qXBYMBC8_MNrwKWdwwAqOYKW1ZB0IVYCwMWvRLO5nTQBY_4-K9Hy0GyNfiLbD8ZfhZOoSAG3g8Dla_dnqAzs5VhQXVWn8TnIRVgRrPFYP-LMqtaIV_RxfFgEYoarKxmH3Kkaj2yajtkFcK4dqAP9JeSUJHvA-dmHPEBzT_2s75rnVF11b0FmittaRrVubMLX3mCCtUSjD30NGfqAj7gKOAsJUwXy_B6WK-2DsciKbmQA3eeNrK_lzsq3Vst604qBT8MEWQwFoluSdJSdbtbTWtRqrFBJaT5Ay3JmKY4wytMQulGmci-1DDEUN9BIQT13YkP4f_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پزشکیان: چرا به مدیران شرکت‌های زیان‌ده، فوق‌العادهِ مدیریت می‌دهیم؟!
🔹
مدیریت کردن با وجود صداهای تفرقه‌انگیز کار خداست
🔹
کارخانه‌ها و شرکت‌های ما باید توسط بخش خصوصی هدایت شوند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/akhbarefori/679024" target="_blank">📅 22:36 · 15 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
