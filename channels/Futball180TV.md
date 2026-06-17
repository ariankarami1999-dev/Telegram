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
<img src="https://cdn5.telesco.pe/file/UBNIVpxf4FvS2rIN6QVoufTh_hwWFV9w9g0GpKpalLqYCMZwloDseJscb0f--MArqt5Yq2DYNeFQXq50mppWj0BrcpfnsPElqi-ZbomdYoELk_0nUXRbylUjLT41ka_Yedtpj8FmUTd4Ema1zOd7RsfJ72PdGsK2p_NgVJpKuE-5lwNjywTjr4fYRM1AJK_QFqetUonKFtJlW3Ean20XeJoA-NOnDtS6_4UewVd0XTxhIKgq78koBs23bbdVtKoVEhh0FuFkwjJgoG5DZU9KwQiIpZHqL4Ox8Sqp37VxmyQKuycyrYfFGp4wh0XG4l3H9y9QkODK8OU-hnWYDfb2DA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 622K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-27 08:52:21</div>
<hr>

<div class="tg-post" id="msg-93862">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">اردن و اتریش بازیشون 1-1 جریان داره</div>
<div class="tg-footer">👁️ 957 · <a href="https://t.me/Futball180TV/93862" target="_blank">📅 08:45 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93856">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SmdffhvwQPeNIb5KC6Pb8wKNOTfeQucj38W4IOnL-looOPt9KiLxpNQD5KK9-U11jNEiDije9fLvO7XVeBE3jhJbdKxzlVBIxoGUJ2Yvy3iE7FOg-G2PiFn8gFS2FHKlKkk8YeZ0wM44C1EGuLrDoNbYj1cjtwKeJZ8BE98HgsLq0aaGoX_p9OfvCY6zgwJVkryS4qFxlGU2MX9edVmf03DrZNCDK_ZJPpyrCvkiG3VHVd1x9e3W4tzDeuutzaj9oa5VMIvKUY-FIHrYYMlZ6Ec14ChzyelIB6cg-ETqhVaQKjFdkXLIJcIWCYfgJq9l-wcpIxZMfoh_VhscP5CH0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/StI96xgq6m_HXdmyLNi9yJDDpK9iX6YQKKo6Y6yi0m8mJsSAFK-SH6-NwzICiBwjDunP_rQ89S9kGGeUM9OdzP7AGRDyscbH7kGroXRnmi6Qz_C8n_2d4Zat-6PNXy96Jm5Qx-EziUr1rjn3c9gdrUIxc5zoNiI3yU1-LkiE7UsSWvEDYVsmKeF3SoW1lo2c7QXGCMIB12syHJNsybZygcyAmrexbslyJeAVSJ9MZ_LdhrHqMMHdtgVW6vItuc3z_a5TgevVNn3mg9fwNXWm3tG7cjnhA4BDbAocO1OLtuaAnK7MZXgIz7x68jJRtt0NxVXy2lQSppGBrry7pWtHxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZaR5SmowZyI35B1UMsiQfTBR2el3_pDOachdQFXenlYaSobLMUK58RVx4_Y4Xf3Z9LL6YJSF_ztFRY6qi1gnTjr2ElOXWmqiOL0ycIr9XPGARLZ4brQGYJRT6phBYI3RhgPwV_xzm2HF7mMtTxZ4ozxQ4lrLl3PamB5yN9Al2nq2_Dpzamheh-SY_d3ZJIEJUtuEL0ZtyeaGFGWau5n1qw8VHocFmdwSQnLlzuv6L8n09GZ2Ec_RRyXeC0uJudU10PFfl6ARu1ooB694W3OXkASBYGrndMfBKjuBhC7eY2nyriP-edB8303NX86DKwfRMMR80YgAw3blRbYgNAqyaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kQUt6zR_krjGXoFYWpaZgbS53f8bZ0hmF2e7M-7KN_nnwk1-QrndW0pcmVx9QJGl9u5cBBW_hV2WVe0VRYISCwTLHmtl9rfgmW53J7qVgyquqXOQkbEjF0stl667IM3odcmvx3WCOTKKCEu2PWOKgRRfLLMXhMkRz3cyufwFDpa1_W04vKkws9KxkVier0z4zVcL08Ld1_f-X5RdHtTRv_PQcK-o9VG7DHkx_mStFUuqv4fvi0_w0ocQtuQCy7vsTubchlxnClPPFY7qEkTsjdFENjelOJoRSaN5nIPGs0y-NN_U8JsDuvWFYYXOMDAanP3llGMEQhLE2WB6D-cekQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tDavUJYQOlxu-rdxY2_Ff0Vq7TCuj0GBYToFgDLk5rxSyP95yKf-S4-jpMac3tUMKg_8_kG_GrevfVBCoZaAdD41jrwIhWCrVoTK_W-4bg6p8mhKXsxDIw2EaSpnkyWkPubxlxBB_jgIqEOEptTw4VHITL7fBoOJ0QlQb_oJSNZvlmJObnY3FSTE7q5TGBobzDOw11xS7g0KKcLdJw4TkgUttoPwxcQLmv0smM8Y-6XTWwM5FDlLlyHMHEh84CnY-tWi9oo5a0wJMb6w76TD7OfTq5Vlp7kKCMq58vWZeYX3TsmYxH_z7gKSAZBagr5BWdbnc3xd3re-OQ_KsD0EPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KPicZCvQ9w-Zx--BjRmbH4IfUWQSPIJnAbVQJjYuZ0Aj0QGliHJxTgRrFNrSTEQo9iEGNrcXcDDSCfKfy-P3OOHgijqX_QtSG1WmLn28_wMufle3Uo3J3b6pbP89UxHw_whR6CjwyS1NRVDkFoBVhl43jH9TX6B9mEc1U7e9iqfafZCw6jJeclaQR0hagu-pTddLlP4SCHWxFX_ctxNgpITdJ9oBykFE0QUKMyOT3n6F1DsbmpSAD-BewreZKG34R1PXjF1mJGxCG6g56kbdtIqotP_aHaFfFtF1hk24ifQ3kme104mSJ35rYOdQ3Bf9ooGma-rwpT0wb_0wpUh6fg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">روز دیوانه کننده جام جهانی
🏆
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.27K · <a href="https://t.me/Futball180TV/93856" target="_blank">📅 08:44 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93855">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mg2OToyi9NCsQLSffX1-v-S6vfblsfjPoqZA-PtHmlvGqedBdUVyENfBFCUU4BuEjhR0Ifzho7Y-xTx8HRRGDfudWU3AaTsyFmXJu6O0cpC6z-bbz1WWWfI4vJkAwg9d5gwJ0tH0avV5t59MmBE9YiF6QlaTxyCFK6gWK7_qBTHsKgcTOvWXhXBx9aoiUDkNFZhbqCAVq7WXAXU5YPXqRxsAP5HepxPwQ-0Y-CB3EFebw6Xp9cQlIhfQsorQpBcpDzMjWJeqYUBpTVEhV3mtVhDGhxGlYmzPJIPjhQbbGkO9_b-jk0Y5HijRCx19g8pPh_OI1MrcupH5S5y_antRDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🎙
🇦🇷
لیونل‌مسی درباره گریه کردناش: روزهای سختی سپری کردم. این جام‌جهانی آخرمه و شدیدا احساساتی شدم و گریم گرفت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/Futball180TV/93855" target="_blank">📅 06:58 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93854">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚨
🎙
🏆
🇦🇷
رودریگو دی‌پائول: برای لیونل‌ مسی ارقام فردی اصلا مهم نیست و هرکاری میکنه که مجموعه آرژانتین نتیجه بگیره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/Futball180TV/93854" target="_blank">📅 06:53 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93853">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gncLSwLAOh-RkgoJQC4DHcaa0BLPbIuduDjAEiwBD5iIKswypgEICNSIaklRh4feyMiPGwqjmnwydyPKVlcLvV0tdDxMyQMuvfwmPV2hw1KJtAlZC6XvZ5VREBpxzbfrEG0I-TM0n5G2rEAnJkSARS41qimQe4hehR4y-wCpxTZKqF9Vm4pR1-QqeygLCYMmIhz81LOJVJMrhF3pcJjGbN4oiR8Q-Il3A7g5u97HVL0cJt7Miw3Uf3CG7SCO36KzngJx6AucZizdiy98B0b1UNLBE4LXttGC5YaFAnHDRlLz8I_dakZkHJPH_dmw-POHCJ0kyHl122ia-4_Ftjf6kQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
💥
واکنش هالند به درخشش لیونل‌مسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/Futball180TV/93853" target="_blank">📅 06:51 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93852">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a7f19dfd3f.mp4?token=V9Ck5M7oJ0OY0kN7i6_2vW9cHE-keOuGAX6ynDWkIV6gUdMBuD1PcHNDUhO4YIKioWuAB8RRmkQb7ieiNk205NFpSU9dV73B75N512vf6OUyZwt9qzTiqhDF-2RHRA7MNoAvXzoMeGCB7fZBOk_4QUAq5niZtoG75aKPrWwLJwrK1UNh3Fgv9_rIpvU1r-Yp8U1blMMxNrgA528HHm66Z5YOiB1mNhMy3Q8gzP9uyKBl_5txkpPd317bXkYZ6HiZpns3ME158Nr56RM8o_8JZSTyaIyK9HFQXRp0AxtDlZPRy4XYAA6MysvJ0mePw-iBqgpkVyCviIR2aPE1rMuwKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7f19dfd3f.mp4?token=V9Ck5M7oJ0OY0kN7i6_2vW9cHE-keOuGAX6ynDWkIV6gUdMBuD1PcHNDUhO4YIKioWuAB8RRmkQb7ieiNk205NFpSU9dV73B75N512vf6OUyZwt9qzTiqhDF-2RHRA7MNoAvXzoMeGCB7fZBOk_4QUAq5niZtoG75aKPrWwLJwrK1UNh3Fgv9_rIpvU1r-Yp8U1blMMxNrgA528HHm66Z5YOiB1mNhMy3Q8gzP9uyKBl_5txkpPd317bXkYZ6HiZpns3ME158Nr56RM8o_8JZSTyaIyK9HFQXRp0AxtDlZPRy4XYAA6MysvJ0mePw-iBqgpkVyCviIR2aPE1rMuwKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
🔥
خنده‌های لیونل‌مسی حین دریافت جایزه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/Futball180TV/93852" target="_blank">📅 06:48 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93851">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PQvT1uNRXptGVWgmrv91plxZY9tp_Lt_QC6M4MGLPFWSXCO8wpAv499HIXdr8F3mSaN6V4fLWce1jb9Io_Spm5oXFhVgx3_RUFs0v-D5weZrI1lSeFx2k7KTL7EHs4t1zuZEDjcl0YrqfeGX3Dbj0U0dNb-Ud9HimeHzo4HS96QvIe0a_g_jIQ21c-ebtPUtL16htVoTVqrQOgjeXFBPDA6u9Yj3yfgbPfuQR_miAo2XiItizN0pXg9tq_OQZ3rYg1V28iTLXGfX00sC44kG8aUlVjbDuoYsAbz9fx5UJg82ni6QE1MwqtkgT9APK8hue1QSI8cqtRZAnIXTLG0akw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔥
✔️
لیونل‌مسی بهترین بازیکن زمین شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/Futball180TV/93851" target="_blank">📅 06:43 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93850">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O8uSW5ZpJ_d450B5LJgEYDOvDgET0eMnX20teEP5-pYmd3zcgoJt6DB8ZhVRwWgapt8g1P_lS0mtGdVO-NMvf-VCV3ts36FGqb9KL92jg0dzXuWzJPVgVsTK37TZG29wAAfx9hnoxRLKe-6m__UvW0_NB3mfTyuKsr7SZ-I-iKM0DIyyt0f8Yeh61X8791xM6WNDHkL-PCCQj26mNSUSLuYpHgYBvO0fcJvDZDU4KvUDe45m97TXAFT8tRF1OrRkcp7L0sfuAsuxNTMCAkY96wcKP9g3NVS990znK79YXI3aEUtcj28CgHRZYtjr1aekjICZ9aaXRNx2AB-IUIuS2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
📊
🏆
لیونل‌مسی با ثبت سه گل درحال حاضر بهترین گلزن جام‌جهانی ۲۰۲۶ هست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/93850" target="_blank">📅 06:42 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93849">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JgQ58bS6RYJJi93tq3spFpYBrB0AhKoV0R0sW6IhKGuaWVw5ZcYsPOK4z4DXZORC_K1r9CMC9pVYM639osU71uavQk0ernft4GWwAZgbNr0oczBCW1M37NsX_MJVqmnHwgGNMYjgSHX04Ay5p5yMuI_pkMcytoO-Kfe9ZJS-a9SUkgz-9lskQ5Z4_SHUMntXVWJZF9sL-SLa4W6Q5aML7DmFCvYf9lHAximAJsLHdxlzRkaxMhb7wm0vXjlF3PyMr-9zUlTE6_KwJWOOv5CNye1yl0X2JOsFH8ELZxa85H_sV8FDqboxYkiDYRwT_EGbx9o4Ry6w4I5BOG-GLB7-Zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
📊
پستی‌کوتاه برای درک عظمت و تاریخ سازی اسطوره لیونل‌مسی
🔺
بهترین گلزن تاریخ جام جهانی (16 گل)
🔻
بیشترین پاس گل در تاریخ جام جهانی (8 پاس گل)
🔺
بیشتر از یک‌هتریک در تاریخ جام‌جهانی
🔻
بیشترین رکورد دبل در تاریخ جام‌جهانی
🔺
بیشترین جایزه بهترین بازیکن زمین.
🔻
بیشترین تاثیرگذاری در تاریخ جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/Futball180TV/93849" target="_blank">📅 06:41 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93848">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dXvt-qDMXKbKPKIf0jvEqSdTtaDw73l0xR_4jqhoEanLQuNuz9NpZUPHEZGKHHlgoDMBc2uiWQ-jiGH6beVqqZqC23Cg24v9nwS67LbUt1WxtBZwRXqGgntXek6R8eenT_okB8PH4SBXAVHccvAHWAe4RO__r4J5sO0YBS_7D6mr-XzEyEg4J8mLs1ihdCqEd1aJjaMixMlBAuiSQ1TnaE8MGFrJEWVBt-h78sc_1DfNEtUXh9KYszxcT9v3rofec0wjpOwgIRyOHX4ez-Tr7AYd4Q1KIK5sTHdqtnevr5lDe1oRe-qd9TxqL8paXQMt9XppPe5Un-xPxZ_5hjqKeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
📊
#فکککککککت
؛ در تاریخ جام‌جهانی لیونل‌مسی با کسب ۱۲ عنوان بهترین بازیکن زمین، با اختلاف در صدر قرار داره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/Futball180TV/93848" target="_blank">📅 06:37 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93847">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Vyfboy4P0etuxRno_53EEz_Q_VxXcGXv_BMWx_mxO_oOFLt8OdaJ1m_ikZFjQt-Q5bhGvItwCIJykTMj9MUMyR23_PkLw6IGhwKOWrgu1WMWPuTQth5tpHg5TP0sFNM4etf1SOnenYxZoQzY-8aAjuCXyD4EPFjw88iNbqTSgsnRLyM_zyen-Q5pZLyKhswBEUerX5hI9mlBmTY2S7-SazHfag9tM-ulJzgRLudn9jMO9KhXL2ufZ4Bh3KzaQkZOcVx0UFEVhzDOQ4lhwu6wf_2AYauMacXsJYAqCpleP7ea092TNgdSWSJDjFDQxsDQWw2sTQqlvWiVplbb321qvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
📊
🏆
#فکت
برگگگگگگگگگ ریزون؛ تعداد گل‌های لیونل‌مسی بعد ۳۵ سالگی در جام‌جهانی از مجموع گل‌های اسامی زیر بیشتره
كريستيانو رونالدو
‏- تيري هانری
‏- مارادونا
‏- ریوالدو
‏- نيمار
‏- هری‌کین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/Futball180TV/93847" target="_blank">📅 06:36 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93846">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vxi2ENQ3sCz1MwhcYMgDQoWFkQG50bgOKu0W-h8NhHL0iYmwOFcDKQZDHkhjlwzUH6B_ZycFWJ656-h4GnIIamuCMnsKflwFGPc6_qu2jZQkXRypSFwL680m_999Q8BeRWK9M270MbLMJWH8NoOLSP51aSRs3lZkVgDsTGXKaxBiaLabe-lHpl534AYxaAh5rAADfmBmYPabSfKTH0esbyA8kEsm9UJ-LDj1o1zUIsrvje5KCZHLKSyrDAyep0eNV5kHh0fxO1Brh29S3JHJYaFMAc41J2FkaCn9Ry-q1mPuOj_2hm03AI6olt5TRBB2z5Tdrohu0CFZCba5WFFJVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
📊
پشمااااااااااتوووووون فر بخوررررره؛ لیونل‌مسی در تاریخ فوتبال روی 1328 گل تاثیر مستقیم داشته
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/Futball180TV/93846" target="_blank">📅 06:31 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93845">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SxXcegmAqbRcX9kRDXQJpsrdOY2A_La0DBLxXJ6S5no6PwwiMY8EKuEvrswRN0KRQre1xYcBBlE4I8q_tzRVQVH4IgAX2_lyydVAflc0An5f6KAG_yz1J50rIfQr_fcnFwbR6f_k3KhQeZFO0Kim3YEHzr4zXIyTYBYYf-CTzrTBa-dw6GB1Fia0EHX01t6I6qLG0LA84pCBtm5SrVmE9rOoDN0AMZqQyu6FmZVE2AJWdZij-85kNx9eUaL0zc1o81UC6X5xn313onbzDrWWRHYAr75hoyM-ORlFgFEbbmu4o3XgYesuPpSB_hkuyJMNP8C5hiSz85OpQxSerpqTow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پایان‌بازی|یک‌دقیقه سقوط برای کسانی که ندیدند؛ شاهکار لیونل‌مسی در کانزاس‌سیتی؛ آرژانتین در شب متلاشی‌شدن رکوردها‌ توسط اسطوره مسی، الجزایر را درهم کوبید
🇩🇿
الجزایر
😏
-
😆
آرژانتین
🇦🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/Futball180TV/93845" target="_blank">📅 06:29 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93844">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🚨
🚨
🚨
حفیظ‌الدراجی گزارشگر بین‌اسپورت: رونالدو برای اثبات اینکه در تاریخ بین بهترین‌ها قرار داره، فرداشب و تا پایان جام باید شاهکار کنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/Futball180TV/93844" target="_blank">📅 06:29 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93843">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">📷
🔥
🔥
🔥
🔥
🔥
شااااااات تاریخی از صحنه هتریک لیونل‌مسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/Futball180TV/93843" target="_blank">📅 06:27 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93842">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NE9BxzDMzAzTGl6Nm6M_zxZNtFVVvdFmrrFw7xwvI7djLM30aXaYMlbZf9zcpaeS6Jl_y26mOaGixY6vRh5C-drQzDpwbHoeZnJRRzmS5ZGjw1wJqY2-tASfnsRFZV4-P4yzf3RNV6psZvXPGD6Z1l4wTD_qWofAlEVke7T-VCJL2_BdWfwe7sfdCRzBBqAIdTHFPBJ0_5qU1k_cF3VTtZSjrvjnF8qN5wwhdJjCeSJx2T0WrCxZe-zFhv-Ytc2qDxTcrfJVSMaIDfpCNEiacrA52sl5k7BxE_6S0ysVFmqoIXuaXZtBlcypZuDufFMTruhVXoSSAKomJZcHcGN5oQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
🔥
🔥
🔥
🔥
🔥
شااااااات تاریخی از صحنه هتریک لیونل‌مسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/Futball180TV/93842" target="_blank">📅 06:26 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93841">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DJuTffjakjrkLd5BrhSIaMgym3QQ0J7XT6hfQHGOJFdQOsxyVbttlGNnnTHwZ3e9k6Fb_vhRIHNRft_FiEjXTzov2zU1NPInY6YAH9g2d5pIyx7a88p5zsNly8Yu4LW059gfJo55rFj95948zfbgb7BZKGWTaL6FgWuy87jk1yCnoCGLnKq9riGFnYRtQZy9d0EVRV5YfUl6J-JiHNKZRvnyQmlvMRX116WGs6phsIvQ-7U9XCJMkfZKZksotT2AKq_TwgBBFpdzCiesu8PcY6wRZhLFQqy7xA6GqUPLAgHjdHxZzvp5smIc63huPe6geS0Lf4JfLGsd_lQQKVa2pA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😛
😛
مسی اینجورررررری کنار زمین لش کرده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/Futball180TV/93841" target="_blank">📅 06:25 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93840">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p4oYEuSc60vXkXLkMob6pr4PJyTixfuTBkQVSfjT45Z2Rfqct7kSjmhmcfeKaZGJdditSmdXbVtYVW1Yey6PRNh4bos1dbyB-pO-wjERFfeJK7YoNvUWDaDzROuIBISwzqJCJMMw4vZBDdhNpHRiBCoPpD8au99QIuvzccBewQXY9PNADSnwkhnFOglPehLfyar9qg9fq8m7tj2XkWuEgbZBoBTCqD0EkjAMil_PBZNzNrj9CFFDX3M21fx_KzpRQHTlvC4XhNpcL1jO06eub6YqADCeDboYdJTq74Qe4is7ZZlVHq2xTEuKLQNgJYZIZYydQZrMWMapBd3bvR9cEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
🔥
🔥
🔥
🔥
🔥
همچنان درحال تکمیل کلکسیون تصاویر جادویی امشب مسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/Futball180TV/93840" target="_blank">📅 06:24 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93839">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L54PSeD1e3QNXiFHk2QGdhJMlRvJsz9Q7a5pbX0E9gMSPOjjDyMl5OYQA4yEVJMP6i1O1R5ePpu_8pgrg8e-j0tddaHGtlthhx5GQ7G7TduadUgDGEyluif6mZ_DOZUM_908ii-W9LDU50n8QhfoVn-tTfDXCFxMcQ0_H_hKAeUuDzSvKoyeV0OWkDoLB0K58HQvtI2cOicGJk_c37Pd8J7pHlQtbRiUdCqO-d_xnPySTF-ERLxrLa0sBzJPRGd6Q5paI5axHnrj2skr12ZzoxAPOARCW0HrkBXCP2RP-FeGc2mKzL5GBRcjutqszaXxODtQvSMHMeL5arXlspk0Pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
📊
بهترین گلزنان تاریخ جام‌جهانی؛ از الان برا مسی و امباپه رده اول و دوم‌رو کنار بذارید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/93839" target="_blank">📅 06:22 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93838">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E6aeavBCWiLfX6Y-L3gpmhUuq5wPThEzYxQZa0MvKru4hKtWGucWTvnq3vGYqA-9QUiW_T97c55HYwjqO3HkSg1McDODehBE8rE_fY23ZVbk-kEIE0uPv-1hn_J8MCLx4nLnOwQNR4By61W4m8WQ_U2o-D6pK790TCirl7WpqeHBbNM210GxFNFBD3kp34hfyq_IHIXtZGT1zcrFKLcRkj_VwGD1hf3Uw6f0JZT1-ybLNGYYG_ktAiX0JzQLaRwbVLSPzThP5_f2rKNO3fIHP80m0uYy-1DT53eKYYaGdO7Gqw7wGGz05DXsM9BK2yBozXVsIg3SmukYuFdk4DELMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
📊
لیونل‌مسی با عبور از رونالدو، بیشترین تعداد هتریک در بازی‌های ملی تاریخ را ثبت کرد
‏— اسطوره مسی (11) هتریک
‏—اسطوره كريستيانو رونالدو (10) هتریک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/Futball180TV/93838" target="_blank">📅 06:17 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93837">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">فتح‌الله‌زاده الان داره پیشنهادشو برا مسی آماده میکنه بده تحویل بکام</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/Futball180TV/93837" target="_blank">📅 06:15 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93836">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
🚨
گزارشگر بین‌اسپورت بعد گل سوم مسی:
چطور برای فرزندانم در آینده بگویم که ابر مرد تاریخ فوتبال در زمین نقاشی می‌کرد؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/Futball180TV/93836" target="_blank">📅 06:14 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93835">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">هوادارای آرژانتین تو کونشون عروسیه</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/Futball180TV/93835" target="_blank">📅 06:13 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93834">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
🚨
لیونل‌مسی تعویض شدددددددد</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/93834" target="_blank">📅 06:12 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93833">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🔥
🔥
🔥
شب بیداری اینجوریش قشنگههههههه</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/Futball180TV/93833" target="_blank">📅 06:12 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93832">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e341d92384.mp4?token=X6m9CvG8rG_eT95orAgDxC4Ysn5kcEN-Rr4zwh7-BZCXtAsRFzsMUZA6iv3yoB6rhtLH_l1pY5kxxCJPSNVOwtmEbmNQMFFca89uXu3QLUGywa8sjM3F-emxBtGhUuW2I8nfBK5TbeiC-ZTTJHFX3XGnkdkNo_gCSWjyC4smm0hOv2ev7dkP5FiDcj2-yvCJf3SKEv6OxOV3LMevgFFZNF5ti-wPDUbfWCEvudqpMwNKmLJyHsoVERLggwT8qRnEhKJ1oFjqKl8lkohXh9G_CIVjuKWg8FIR1EXRA_RqD3Wrz9w4w_RfL9KLdsTZYcqjsMNdtAoudCQUsgPQYKuxPKFSqd-P0MqzS-Od9xNM--FtBzPqiJRzy7LKLCV9dW5Ki5HGu4KrgC2m5KMhewJcEwO4L7ssdadqCO9C0o9QZBoxK2li3KE2taBzqoncYIEqQkHWKV4GmzEBO3LkHWD5il8OyasfowavSB2oLJbqqI4nXXvumg4YjT3_U7R2LkjcaCeFJnbdYDNoRlvFRHpAYG28DPnrSQFP9veaQFjz7mq9KhpGJJj981ksU-0Yov_OnaWrjG5uiV-jvnOx6NeU6CE7REo0dRERi77Ag6PJK3Ddnf5byPOYzS25qk_Aef7euqtf1fqMy5U1Iynvp9uVm4ra3kM0ck9iRXgziVsQBuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e341d92384.mp4?token=X6m9CvG8rG_eT95orAgDxC4Ysn5kcEN-Rr4zwh7-BZCXtAsRFzsMUZA6iv3yoB6rhtLH_l1pY5kxxCJPSNVOwtmEbmNQMFFca89uXu3QLUGywa8sjM3F-emxBtGhUuW2I8nfBK5TbeiC-ZTTJHFX3XGnkdkNo_gCSWjyC4smm0hOv2ev7dkP5FiDcj2-yvCJf3SKEv6OxOV3LMevgFFZNF5ti-wPDUbfWCEvudqpMwNKmLJyHsoVERLggwT8qRnEhKJ1oFjqKl8lkohXh9G_CIVjuKWg8FIR1EXRA_RqD3Wrz9w4w_RfL9KLdsTZYcqjsMNdtAoudCQUsgPQYKuxPKFSqd-P0MqzS-Od9xNM--FtBzPqiJRzy7LKLCV9dW5Ki5HGu4KrgC2m5KMhewJcEwO4L7ssdadqCO9C0o9QZBoxK2li3KE2taBzqoncYIEqQkHWKV4GmzEBO3LkHWD5il8OyasfowavSB2oLJbqqI4nXXvumg4YjT3_U7R2LkjcaCeFJnbdYDNoRlvFRHpAYG28DPnrSQFP9veaQFjz7mq9KhpGJJj981ksU-0Yov_OnaWrjG5uiV-jvnOx6NeU6CE7REo0dRERi77Ag6PJK3Ddnf5byPOYzS25qk_Aef7euqtf1fqMy5U1Iynvp9uVm4ra3kM0ck9iRXgziVsQBuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🔥
🔥
🔥
هتریک اسطوره تاریخ فوتبال دنیااااااا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/93832" target="_blank">📅 06:11 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93831">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
لیونل‌مسی بهترین گلزن تاریخ جام‌جهانی لقب گرفتتتتت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/Futball180TV/93831" target="_blank">📅 06:10 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93830">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">پشماممممم
مگه میشه
چیه این فوتبال
🔥
🔥
🔥</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/Futball180TV/93830" target="_blank">📅 06:10 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93829">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">خداااا نفسم بندددددددد اومدددددد</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/93829" target="_blank">📅 06:09 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93828">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">قلبممممممم داره میگیرههههههههه</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/93828" target="_blank">📅 06:09 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93827">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">وااااااای</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/93827" target="_blank">📅 06:09 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93826">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">هتریییییکککککک لیووووووو مسیییییییییییی</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/Futball180TV/93826" target="_blank">📅 06:09 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93825">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">هترییییککککککککک</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/Futball180TV/93825" target="_blank">📅 06:09 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93824">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">خدااااااااا</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/Futball180TV/93824" target="_blank">📅 06:09 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93823">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">هتریککککککک کردددددد</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/Futball180TV/93823" target="_blank">📅 06:09 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93822">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">گلگلگگلگلگلگلگل</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/Futball180TV/93822" target="_blank">📅 06:09 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93821">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">زیدان تو ورزشگاه داره ریدمان پسرشو جلو مسی از نزدیک میبینه</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/Futball180TV/93821" target="_blank">📅 06:08 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93820">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oq3rl_2-SBpSO21vmsYxbid5NblITopjx2QpyWtfZ5cHK3N8tiJrj1jH-XxJmq_PXOQVx6F0L6lTJ3cRbHx5o1VXCb1ofuX-I3di1vGlJwDV_PfIg5NfskqVZ9IQmreukrL_aG3bNkjlKOJkmPwG7hj47jQrxGpabJb_sktTDMz3rbT0-MCxpOlucKF9AhOxAgBNzREKt_65LBLP2G_PTjGkTq0d0JsPomdxku47uH3BwnWe8g6w0cb8W2H8SQd9W5XIJ-xg_y4pwjBvo_g9n_sPeMpDXGQvBDsxoOgeL1dHZDE9kxBCLkw1v3t4-y3SsUxKhnHnPe7XsQSFZzpyGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
69045 نفر تماشاگر درخشش امشب لیونل‌مسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.88K · <a href="https://t.me/Futball180TV/93820" target="_blank">📅 06:08 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93819">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">داوررررر رو مسی خطا نگرفتتتتت</div>
<div class="tg-footer">👁️ 9.16K · <a href="https://t.me/Futball180TV/93819" target="_blank">📅 06:07 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93818">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">پنالتی نبوددددد</div>
<div class="tg-footer">👁️ 9.14K · <a href="https://t.me/Futball180TV/93818" target="_blank">📅 06:07 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93817">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vKh_1viRts5dnA_35v-WX47Bu_afdnwhMPdjjCnwZKlxpq7INdXte9NcW487k1R-7Es69NhjYdeOvDZ6EAnIg1xVLVma8NLgMIPlCI1cP9gvUpDPbyY6atQj20hP1Zxi_j1OzV7XwjS07FZj7WqeHsnziBC7V__fkAS4LiNGWwe1kQzgYgxmnAuIRwsJ3QCSIcda-xmuASkIZgfUd-7Ww7ehkfNzn61Pzh636ynvV06dwgLYfx5lfF5X791bO0cAlHn-VRizdEQ9JvHtt1PhtYk46Yc_DDhdNDjHGJFhsiUGa8ZMmpz6MgiIsjP8yesjCSpedxT6lCxk_6v7eLx9ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
🔥
🔥
🔥
🔥
🔥
🔥
🔥
🔥
🔥
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.57K · <a href="https://t.me/Futball180TV/93817" target="_blank">📅 06:05 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93816">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
📊
#فکت؛ لیونل‌مسی مسن‌ترین بازیکن تاریخ که در جام‌جهانی دبل کرده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.19K · <a href="https://t.me/Futball180TV/93816" target="_blank">📅 06:04 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93815">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">فرازمینی
👽
👽
👽
👽
👽
🔥
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.07K · <a href="https://t.me/Futball180TV/93815" target="_blank">📅 06:04 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93814">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ffh183F7aeZdNKjadM2BrjySlYB1j_2JEI9Ak3FUCweifrHXfmxK4ASfJ-A-X5O185bf5HmZXl4PDS1BGnvdZudGd1w40gkFITBD2W1shQwAPohvNB6_xj1dJguJ8LaPNNGwA61PkIQIdoQ-hqSUfUGLe-NhT3QkVpZoL9I0uclsnkCman7etrOJBCJ4pBk3d4X2MAJNq7Wkaxirbx23qwDCWvILC4Z7fBMzYf6V1G59OoWlcvVPH3sP23Vq1VQAQxDwM-DvMz0GDnWj8azkT890BW-vaiNoDW_t5qsF7MCxbElpHShfbYF1hDGGnJinr68XUtIRT9lxr-unbsEnZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔺
ری‌اکشن اینفانتینو که داره حسابی از پخت و پز مسی لذت میبره.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.35K · <a href="https://t.me/Futball180TV/93814" target="_blank">📅 06:01 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93813">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b-cnO49iG0BkSPW552n62E1jAbesQ9QaoyfAWBEvvCwRWVuY-4t-vo1b6arqIW70ucm8EEwI3NtpJDEFEPQnMqMhCxoJOxe8CmTjpXS24RVPN1R3-shBtjTBAzKvjvvf5Vf3NZuShHgPNQc4ESrlwDDE_YYJfOyHagoZU8q-WzWJBGfH2aRgKwIUGj7CDK_vkf_n7HYdeev64i92t_Kg_gXNcsVh7AFAL4ENlWSB1bNul_YxF4AOQ2A5Vdizq3hNI9Y4u9G-PFQvDqelR_YEevLWChkeh6aOC5rMkMK39p27cR8yx_g9DTpkEABgd7wqzI14pzuPVdCoR9B9PQ6sGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرازمینی
👽
👽
👽
👽
👽
🔥
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.98K · <a href="https://t.me/Futball180TV/93813" target="_blank">📅 06:01 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93812">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">گلر حریف نذاشت مسی هتریک کنه</div>
<div class="tg-footer">👁️ 8.79K · <a href="https://t.me/Futball180TV/93812" target="_blank">📅 05:59 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93811">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">واااای</div>
<div class="tg-footer">👁️ 8.9K · <a href="https://t.me/Futball180TV/93811" target="_blank">📅 05:59 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93810">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
🚨
🔥
🔥
عامر گزارشگر بین‌اسپورت:
"خدا را قسم توپ چشم دارد، توپ دنبال مسی است، توپ به دنبال مسی می‌گردد."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.34K · <a href="https://t.me/Futball180TV/93810" target="_blank">📅 05:56 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93808">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/b0f517f71f.mp4?token=OlPu1mK0oOJQMP09gT23KKXXuvbUU6Gn8yjnLyUAsqhcnbsutEOGLQR9zki6POuufttK5SVUFc42OarEoIiKe7wdfjGW8T_TP9MwMUOAbTnM8WwDlzS54_46UGCKX1oy7Z0212iWSiTjP-wwSHHGZWyQNiAE_XCT6XXTB9HNVActHKOXTD2OPboHXHeqpQzohR6WPKUwyMA1GYJ2-AfN1Z2cFmgjw4_VMTnkYyioBJNJnxYpXEi4wrYvzrNlDhbWIp5ybw394QkWYHbSsxbDf1fZ-TBlZtToCfixoVaLDfv6Bwvrq7_RI9MffjEpmq26jnvvAIo1PDjmZNCSauU4YA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/b0f517f71f.mp4?token=OlPu1mK0oOJQMP09gT23KKXXuvbUU6Gn8yjnLyUAsqhcnbsutEOGLQR9zki6POuufttK5SVUFc42OarEoIiKe7wdfjGW8T_TP9MwMUOAbTnM8WwDlzS54_46UGCKX1oy7Z0212iWSiTjP-wwSHHGZWyQNiAE_XCT6XXTB9HNVActHKOXTD2OPboHXHeqpQzohR6WPKUwyMA1GYJ2-AfN1Z2cFmgjw4_VMTnkYyioBJNJnxYpXEi4wrYvzrNlDhbWIp5ybw394QkWYHbSsxbDf1fZ-TBlZtToCfixoVaLDfv6Bwvrq7_RI9MffjEpmq26jnvvAIo1PDjmZNCSauU4YA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🔥
🔥
🔥
🔥
دبللللللل لیونل مسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.67K · <a href="https://t.me/Futball180TV/93808" target="_blank">📅 05:54 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93807">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">گلر کسخل الجزایر چیکار کرد
😂
😂
😂</div>
<div class="tg-footer">👁️ 9K · <a href="https://t.me/Futball180TV/93807" target="_blank">📅 05:54 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93806">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">دبللللللللل کردددددددد
🔥
🔥
🔥
🔥
🔥
🔥
🔥</div>
<div class="tg-footer">👁️ 9K · <a href="https://t.me/Futball180TV/93806" target="_blank">📅 05:53 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93805">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">جووووووونم به این پسر</div>
<div class="tg-footer">👁️ 9.08K · <a href="https://t.me/Futball180TV/93805" target="_blank">📅 05:53 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93804">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">مسیییییییی</div>
<div class="tg-footer">👁️ 9.43K · <a href="https://t.me/Futball180TV/93804" target="_blank">📅 05:53 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93803">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">دبللللللل لئوووووووووو</div>
<div class="tg-footer">👁️ 9.36K · <a href="https://t.me/Futball180TV/93803" target="_blank">📅 05:53 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93802">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">آرژانتینننننننن</div>
<div class="tg-footer">👁️ 8.98K · <a href="https://t.me/Futball180TV/93802" target="_blank">📅 05:53 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93801">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">گلگلگلگگلگلگا</div>
<div class="tg-footer">👁️ 9.27K · <a href="https://t.me/Futball180TV/93801" target="_blank">📅 05:53 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93800">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q5D_xptVOQumpwLURyNzc6MEeim3RPuxY8Udmkrd_YvjLErRWTCMQX3emOAf_HIdofLX7FwCMFrrv8ECrk1y6T9GNXusC_JWS_aI9b8grtq30ec_ObP6_9ulAkd5WXkdW0qtn25qIKo8Op0F7IH8ZIyGDZsIGkDU9K-19SqRW4c-6VPfdmLlWIUSQHvRf7NmsETeOG1v5a5WcrPzSRE3NaZ_r4_cPN_yz-ugahM09_0bvome5BMnQfo2cfkJDcFB6sPL13Coy5E5haPkmBPtHz-i3gBFAdEbAoe6NI1nhLLVNnZnIPc-NlhTa3c6AGgf6mlAseMAPTwpv321VxZ9aA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از طرفداران نروژ هستن حاوی نکات شدیدا ریز
🤣
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.57K · <a href="https://t.me/Futball180TV/93800" target="_blank">📅 05:43 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93799">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">آغاز نیمه‌دوم تقابل آرژانتین و الجزایر</div>
<div class="tg-footer">👁️ 9.17K · <a href="https://t.me/Futball180TV/93799" target="_blank">📅 05:38 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93798">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hbaHk2Sz-xjDYYIsls-yUcvjTJs2B6x3QEAyK_fx-Ne67juHvvzyA7YaLIt8O_ZjfVsVkl15iAIjRVE7-vzlPVfTTGYJIaIPFMbmn5wdtSQz9Y589nKlIMGHXB8pIEUoiymlrHOalsjiDS-Q81WMW_8-6tydjLRIMDU1XHUTpUJYNqNxC8FXSD3nShnQjsMFXwVvLJ3sNP5LRIdnql2Zdx7pN-4PWaEt51XMEFYbfCeGzEJhyQPwweq071HbQbJBZVAiyhr_hiO_Tex0MzOeN4d-icEK8tn0ZYzJxnoawavrMbFMk0SfLnt4hDY8v-pfLFQrNsRcw6VfmWmuUm6ABg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
#فکت
؛ مسی اولین‌بازیکن تاریخ فوتبال که در جام‌جهانی به ۱۱ تیم متفاوت گلزنی کرده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.32K · <a href="https://t.me/Futball180TV/93798" target="_blank">📅 05:37 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93797">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🔥
🏆
🇦🇷
گل‌لیونل‌مسی از زاویه تماشاگران؛ از نور فوق‌العاده خورشید و جمعیت مردم و شوت تماشایی یه قاب تاریخی ساخت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.1K · <a href="https://t.me/Futball180TV/93797" target="_blank">📅 05:35 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93796">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aQaAVlSrvt3269b1KZeGErgkMjFnjrGBuFUfXUxd7p-JWL2ILyLgev6mnzDDOy6H2K1cASu3HltpVRchGGLescRZK3mfifzK0yiW9esQ7eoeyw3GY5dMCu3mHXGlP79WWYqED7f7iyB6fE_1YV9MmUx1ZYsFGiLV399k244WyRVl0tPo4HzdGz6kiaz_WQTFamCiyELlcgfCswE0oeVt_A7FY0suYj-pCMNf7u071mzHLyUdqLGIcQeXjSmidipDdPDKcXMV0bidR_Oy5dwOK3UQOXk_9MHqvDQ8tgyvIFMX9BhryXONobUlL8UY_RRuJqlZ8oTpuRk21-9IMhelVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
💥
لیونل مسی رکورد مطلق بیشترین فاصله زمانی بین اولین و آخرین گلش در تاریخ جام جهانی را شکست: دقیقاً ۲۰ سال [۱۶ ژوئن ۲۰۰۶ مقابل صربستان تا ۱۶ ژوئن ۲۰۲۶ مقابل الجزایر]
لیونل‌مسی: ۲۰ سال [۲۰۰۶-۲۰۲۶]
کریستیانو: ۱۶ سال و ۱۶۴ روز [۲۰۰۶-۲۰۲۲]
کلوزه: ۱۲ سال و ۴۰ روز [۲۰۰۲-۲۰۱۴]
لادروپ: ۱۲ سال و ۱۹ روز [۱۹۸۶-۱۹۹۸]
زیلر: ۱۲ سال و ۹ روز [۱۹۵۸-۱۹۷۰]
مارادونا: ۱۲ سال و ۶ روز [۱۹۸۲-۱۹۹۴]
پله: ۱۲ سال و ۵ روز [۱۹۵۸-۱۹۷۰]
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.21K · <a href="https://t.me/Futball180TV/93796" target="_blank">📅 05:32 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93795">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d0967a51c.mp4?token=PXPQ5uH0FxLQJdayHfbUog5giBkaHBdlWUv_YlUI0IC20kgKjLTKKHgeVFEZnfnOVWrRPto6FjOgNtj609-hywe5rEVFhBTBGgXSmav7ibCBvzbnrw2ylDn_n6WkjGEhRliyQ6Gx1x8lsjVhRRL6Fjq-HsDncY-5s1wMqOA2gYZ6uOMNBoyr11UuUMCxqQjEgERgNZgrGNecnfZAxEVQNUbi7wpnMe3BmGZRKOCaem1a3Sw2PcgTVcnDnVqNHTWJEKQAa-68jHvZza1MVnbgEA9Zu03ih_fwSks2OW7BIT5jnhXpjuR8p3JEuOCnwHZaZGuFLFqmbsPBaNGIjLGLPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d0967a51c.mp4?token=PXPQ5uH0FxLQJdayHfbUog5giBkaHBdlWUv_YlUI0IC20kgKjLTKKHgeVFEZnfnOVWrRPto6FjOgNtj609-hywe5rEVFhBTBGgXSmav7ibCBvzbnrw2ylDn_n6WkjGEhRliyQ6Gx1x8lsjVhRRL6Fjq-HsDncY-5s1wMqOA2gYZ6uOMNBoyr11UuUMCxqQjEgERgNZgrGNecnfZAxEVQNUbi7wpnMe3BmGZRKOCaem1a3Sw2PcgTVcnDnVqNHTWJEKQAa-68jHvZza1MVnbgEA9Zu03ih_fwSks2OW7BIT5jnhXpjuR8p3JEuOCnwHZaZGuFLFqmbsPBaNGIjLGLPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔥
تشویق شدید لیونل‌مسی در استادیوم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.44K · <a href="https://t.me/Futball180TV/93795" target="_blank">📅 05:23 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93794">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🏆
پایان‌نیمه‌اول؛ آرژانتین
😃
-
😏
الجزایر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.19K · <a href="https://t.me/Futball180TV/93794" target="_blank">📅 05:21 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93793">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bIetAZ41_g2NPNXJR7IU8CcZdhPEJC_1t1iA8mE3M1ISpUaigGENDmBa_amDlietN6p_OU5LRNzdqCOdo9rR9flrPk2hAZ4WJLRpS6hptSG3KZ2OqDQLJeBC6-TbviFMu_b4_I1j91yBpzH2VtdTJTqoo4rYn0rgPixeNqhbWe42Xh1HZX7PDSSoVLUyYg-IlCs0BElVv9njQGm8UHzD-NLjIBAzMZ4hvsvDP6fFfLsVs9V6a2jrDsRHzxlEOg6maRd4tvSKuPRgbOyS2tx6TGjVvA1Wzd9N2KGOhfhbX9x882OzJdKOx3BXchwQPp11tqxQ1dvywoMnagPLIZmbIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
⚠️
#فووووووری
؛ آرشیو وار: کمک داور ویدیویی اینجا در آفساید گیری اشتباه کرده و گل الجزایر کاملا صحیح بوده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.91K · <a href="https://t.me/Futball180TV/93793" target="_blank">📅 05:17 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93792">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G7J_C7XjylhCtF5IEiKPgmmq8xsuDL33kWMbSaL6UYD6TgjSEEtc_yWUeQuMV6UKR5L6JJxrkz1mzFlZQnubU4vQy9M7l2pAoCwjd5E2Y4ErG7XG6aTdC9YZ_dyW1cSFcaCyAXsvITJxRiZOPQWystln_aQ8kBvjG5KffIvALKQ8L7KpzSsY2-8grZya0q9fayGoYbjJqVAXS0m4zWc7bQUJKjF9GvPYwrdzf50d0-hIo1T9dVxqcabV3dVxtN2AXhw1yW1uNdP1D6rIkwzMpo9lRA3fY_9tCvZ6ncRNw_H-A87vnGpijGdVQTcy1UK47ezJuxvtjz0XwrKBFYFX6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
پشماممم مسی عجب شانسی آورد که تو این صحنه کارت نگرفت
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.95K · <a href="https://t.me/Futball180TV/93792" target="_blank">📅 05:14 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93791">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EzmWP1uCUaN-HM8cpkeCVrbJ4nEdFDFmvfQVcUVpTo28ke-39_ZuDuSq8gNIZXvbfiYBSyNaxqJ1uHgTORy1KzWBJ2aliHdzHlb4GDtGn-jPrJn-6UAuBvmbOPbZjoILChSQFrh66k_9VGSg_i0EHrgrGVZ1IZGdeLlp8ufSUbTpbISmTYBsevFbKOOpHEhGKNPOWPhY7J9wQPZo8b7f00hUwfM1XvzGNMYPWB19y3Jlj5GiD6YMp20TzTkc-2pOJ3l7wv_bOQEeoMH8bBPvh_BMDYr6OZFTNNbBy-ei5YAmqR6_5cDcaNzaiK-WEfpFnc5dolOfV3oxcGSs9vP-1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
📊
🇦🇷
لیونل‌مسی در تیم‌ملی آرژانتین:
🔺
۲۰۰ بازی؛ ۱۱۸گل؛ ۶۱پاس‌گل؛ ۵ جام
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/Futball180TV/93791" target="_blank">📅 04:59 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93790">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E61pMxvktq0Xijnm6BA9242IMbC7puh5tcdDRyzRVb9OUaI0haxk7Ff-3KKLY-lVpfxlA6PCV7ebuypb9Zxd0xWtKl7mCwOZujaU5o0FHV_kQZmwxofarzKSFG69Um2NkPtnhqWTommPmqU_Iqi9AgM56Ra6xL-6qI2q6gfynWPFitNkcDRj9Y9vQ5-8qA-_NJtR65oHLheDv_dNJSQGrhL-3GfS4YXpCcvoqSM2aojDPl0ru02Zy2_Fz23Zg08o-5XFb4tF7KwQJjapVl9PYyVRkbJe-EHSN2f7BEuTeZEnqWZSxlc_sgn5BGP-4AZVekPnMFgfYvDPcKu2tAXCrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
دومین
بازیکن تاریخ فوتبال پس از رونالدو که در ۵ دوره مختلف جام‌جهانی گلزنی کرده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/Futball180TV/93790" target="_blank">📅 04:55 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93789">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">عشقم‌ مسی عجب گلی زده
😍
😍
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/Futball180TV/93789" target="_blank">📅 04:54 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93788">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ExwmHYDruwSQjPopT1O_7LQK1QxtlhP5g61ygsqjnyR1pMfJL7am7jh9GWo02bSNYdvL_L7wnCoiYtH75UGx-9BOTiSkJ7FqZceYZ4faLxeu1OzCvgmJ2JEZ6rOglIUCB2A5TuBg5gSYOAxvVlguFg7CX8Irr0a3JETRybNFcWx-tDy09i_fIs_WzyV6qz28BTBoeusbEMa-PZZrIauQ5hiMGYoEPEtpW3s10CBFV7iw8yWuuJzs1WOxA0oH6nWec-_OzyDdXwqX5e1010DWACSc52g12ZKYjqceGIfay8g7ijWsjV3KC07ky0vcwPhebrJurM1uSO7Vj8tBeQgM6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
🔥
🔥
اللللللله یا مسییییییبببببببییییییییییی</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/Futball180TV/93788" target="_blank">📅 04:54 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93787">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
🚨
🔥
سوپرگل لیونل‌مسی مقابل الجزایر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/93787" target="_blank">📅 04:53 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93786">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/0de4d6e25a.mp4?token=Dt9g0lv7qCxJpo4KMtXZz5AgyNQG3t0t1Z-0sjt5f-7JYzCluViBlGpyUSbuYQytg2R83DrahjswzIFRwUfNypVWNb3-v23Gfar1ZJPSAt4H-IUW5JSlYNOWvvdFfHhgTKzDzOqS65nYxbYmB9Y3km6qsQjZmZ0E1n1TA4QvDpogFWS9Rz7VHD-ZhqoOfc9gjwY6AdfT0PpD5yBwy0oUnV0CN2K5aqhFcSa7q9HZoWlgmTdbcjXEglE7lkrDUZ97BHWn1O6iUng9TGu4Ktz1HfxAZ-76x7EZ4-MKFuJAvGE35yQC1uLoQn1uGB1-WxgdO8qvjrlHnh3vZ79rjXpYhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/0de4d6e25a.mp4?token=Dt9g0lv7qCxJpo4KMtXZz5AgyNQG3t0t1Z-0sjt5f-7JYzCluViBlGpyUSbuYQytg2R83DrahjswzIFRwUfNypVWNb3-v23Gfar1ZJPSAt4H-IUW5JSlYNOWvvdFfHhgTKzDzOqS65nYxbYmB9Y3km6qsQjZmZ0E1n1TA4QvDpogFWS9Rz7VHD-ZhqoOfc9gjwY6AdfT0PpD5yBwy0oUnV0CN2K5aqhFcSa7q9HZoWlgmTdbcjXEglE7lkrDUZ97BHWn1O6iUng9TGu4Ktz1HfxAZ-76x7EZ4-MKFuJAvGE35yQC1uLoQn1uGB1-WxgdO8qvjrlHnh3vZ79rjXpYhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🔥
سوپرگل لیونل‌مسی مقابل الجزایر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/Futball180TV/93786" target="_blank">📅 04:51 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93784">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">این بشرررررررر فضاییههههههه</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/Futball180TV/93784" target="_blank">📅 04:50 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93783">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">خداااااااااااا</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/93783" target="_blank">📅 04:50 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93782">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">سوپررررررررگلللللل</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/Futball180TV/93782" target="_blank">📅 04:50 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93781">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">مسیییییییی</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/Futball180TV/93781" target="_blank">📅 04:50 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93780">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">الللهههههههههه</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/Futball180TV/93780" target="_blank">📅 04:50 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93779">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">گلگللگلگلگغگلگ</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/93779" target="_blank">📅 04:50 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93778">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/31962ed482.mp4?token=LCvogFmp1IcPFq3x2U-Zp4WehDzkYvjCbK9w8IbhG_dcxgNnWoC1Zjw4wCGn_DzupDMMCABOrd91wfp2IqtRaMt2RogtkadGF_sQjgw6tCu5ErmP3rvcfhwrBskGNIGufiNdD-VRolu0G4mk-EJaIyGi4ZQm-Iv-S-cOkWyckCfSRJDjmP6m3VrFCFbHx9au0e3quv9oetxp45W5ejgFntIqr0lsJttbF7YxB1-vQiaS2W1DmpRSnxXe2zbbnrCQR1faAHervqBYNwMkb_N1FlPtwTnuLGYXafbSTOJ-2PnyPjDb1nyWo7AV5Qs_b2VfR_ENO1LuGwko3__N6b613g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/31962ed482.mp4?token=LCvogFmp1IcPFq3x2U-Zp4WehDzkYvjCbK9w8IbhG_dcxgNnWoC1Zjw4wCGn_DzupDMMCABOrd91wfp2IqtRaMt2RogtkadGF_sQjgw6tCu5ErmP3rvcfhwrBskGNIGufiNdD-VRolu0G4mk-EJaIyGi4ZQm-Iv-S-cOkWyckCfSRJDjmP6m3VrFCFbHx9au0e3quv9oetxp45W5ejgFntIqr0lsJttbF7YxB1-vQiaS2W1DmpRSnxXe2zbbnrCQR1faAHervqBYNwMkb_N1FlPtwTnuLGYXafbSTOJ-2PnyPjDb1nyWo7AV5Qs_b2VfR_ENO1LuGwko3__N6b613g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
گل‌اول الجزایر به آرژانتین آفساید شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/Futball180TV/93778" target="_blank">📅 04:41 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93777">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">آفساید شدددددد</div>
<div class="tg-footer">👁️ 9.9K · <a href="https://t.me/Futball180TV/93777" target="_blank">📅 04:41 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93776">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">الجزایرررررررررر</div>
<div class="tg-footer">👁️ 9.72K · <a href="https://t.me/Futball180TV/93776" target="_blank">📅 04:40 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93775">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">گلگللگللل</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/Futball180TV/93775" target="_blank">📅 04:40 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93774">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d39ecdaf4b.mp4?token=vLkiLAzxevv2naQJ8sdJ0sk91wBVYHblJM5jnDN-WKPH7vEXak52aL2TDnqG8nOf5MAjjApoO85kIN0BRR3iDdh4IsNueMXo-f6xQtYhoBcuNVulMfj9eyXs0ZBXOuzk_i8Q3cv56ZUiy9S7oxEVtljaAKB1CXjwAr0pEgJ3DZ6Ns5RkBhD5E4F9ENgZTJouhzGokjUqYftMz4FWQuLHW_CSJvxRW69jdfsfFdDlNEzc3C7eGZWYK-SCG-LJYOJxEbwo7Qsz3epn3GuwbUngA8cUJuzknKpuR0__QgTxcYW8MlhT_B-a0453CgbIDXGj9FTOyepg9cFs0pgNeZHEKVd4SUsRn79ezUGlf264EIjegHgSJWrELh2g0qRvH88BZCMB2pH0V3uiB5zirex7AD_aJWMgG-v_A1faeZRimrJxlprN8Sp_-9Xn5YUhtKj2wzozCygSQA4swF_L-S_OFGclZ_TfFrrlBRHyAT771yIte3BVfXaEQExSQOnyUbtScNjCkAMffbxhi6u30EnTcHuS3R85_dQHOhE6UJkOJMJWljzcOwpcyEf8_j3W8zQo3gMX5FObSCdsGoyfVymaKn2UNJNnK9FOR_r7wno1XijR1d-ACJigispz-yyzMDT9VwAqjK3VljinGWADKJsFZCeeQh25PJTw1tY2VRwpnZA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d39ecdaf4b.mp4?token=vLkiLAzxevv2naQJ8sdJ0sk91wBVYHblJM5jnDN-WKPH7vEXak52aL2TDnqG8nOf5MAjjApoO85kIN0BRR3iDdh4IsNueMXo-f6xQtYhoBcuNVulMfj9eyXs0ZBXOuzk_i8Q3cv56ZUiy9S7oxEVtljaAKB1CXjwAr0pEgJ3DZ6Ns5RkBhD5E4F9ENgZTJouhzGokjUqYftMz4FWQuLHW_CSJvxRW69jdfsfFdDlNEzc3C7eGZWYK-SCG-LJYOJxEbwo7Qsz3epn3GuwbUngA8cUJuzknKpuR0__QgTxcYW8MlhT_B-a0453CgbIDXGj9FTOyepg9cFs0pgNeZHEKVd4SUsRn79ezUGlf264EIjegHgSJWrELh2g0qRvH88BZCMB2pH0V3uiB5zirex7AD_aJWMgG-v_A1faeZRimrJxlprN8Sp_-9Xn5YUhtKj2wzozCygSQA4swF_L-S_OFGclZ_TfFrrlBRHyAT771yIte3BVfXaEQExSQOnyUbtScNjCkAMffbxhi6u30EnTcHuS3R85_dQHOhE6UJkOJMJWljzcOwpcyEf8_j3W8zQo3gMX5FObSCdsGoyfVymaKn2UNJNnK9FOR_r7wno1XijR1d-ACJigispz-yyzMDT9VwAqjK3VljinGWADKJsFZCeeQh25PJTw1tY2VRwpnZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
گل‌اول آرژانتین به الجزایر توسط لیونل‌مسی که آفساید اعلام شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/Futball180TV/93774" target="_blank">📅 04:39 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93773">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">گلگلگلگلگلگلل مسی زد ولی آفساید شد</div>
<div class="tg-footer">👁️ 9.19K · <a href="https://t.me/Futball180TV/93773" target="_blank">📅 04:38 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93772">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">بررریمممم سراغ بازی آرژانتین و الجزایر</div>
<div class="tg-footer">👁️ 9.27K · <a href="https://t.me/Futball180TV/93772" target="_blank">📅 04:32 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93768">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jKE4ebK-lfoZfIFcZBDux5KqWL7HEa1piNKDdT5CMt-xC4D6mjvt21UGyWFc0e2QcCNwtU2VWS-OkyUVPtViBAhGJPVW98Z2nGanbxVB3eNMD28g4ugFKBOvk8bydGPFn2yqg8d6609aPpM2hEd2ZKJ1EcmrJ7G-rJUbtYKRejeDoVgCfoEHTHBDCf-iILNkNrgXPdiw3S1BH2K2jajH1QO2b5ugpX_wR4VtuQmFGKObFWmz0LhpvOk9kAhEMkPNHGHnY3azJAFVuBZW08epzy0SMQY5EmZf3cO4b6KBX8CUC2p97V8jO45vzVmpDHwXgesG3gI8mHaOf-PdPbMBBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Yh9AAmfO-HPn8pf_3Y1SOXktYAqf76s8v8Ob3dOkaRXRw9HrpA_uHSeA6vEt7RCRTjlYYMhuDYZrkUZnxEGYBUqhKX8FZcniBCkK5HX97l_NOCRzX-ryjOxn7Zp-r683cc9fMS3h_olLKtEshmd8tzdrgv4NI8D5OEEez-qGm0aV9L22Ko_DovOUoX5uSTdU_CMuRHGEnFcwx8ZXpGVjyoTjvf13AizHeukO0GjNlF1sT3MTJ8VnWgwGiqHE8ue8Mlzz4kbBKOgKX6nftZOZXl5VUxGHbiXJlnZBJbhSQI0Tsr9Ux46ElHI7xMNtXB1FFEoSk2axwmOLQ3NXuBPsWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uCaLpsOAyi_lJ1RSqYmMvP2GZ6Js09WoR8-bDvej78GHDZwKM7nD1rqfZYkdVbaTXIvLbDO0wDaaHoIoR49B3RAkQCaMuDdbTeLb7W2KcEmd2chfC98hcFjtXhViJZHt0VL5YYRcGnsYj_SS_zsHlvEDqN_zQ2vkW72H7xU5655BU7N3oSY2TVPPDHuzVGCsT7kG5-pWvUFV3_3QJfD4sTfscejXwbD25p3idWBP67QWTNXVxSoYVZ9SG3UU4zfbdzoVnfV4Lb6bD0LQYOTaMLAzRLtnJ0m6nQ3m4RFqPRuP3UC-pAzH1u17Svv8C1LusdeJvAa5ba5JrHEeo6Dpzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sTmmU-j71_cOMCK2SAvAVYRVN498orV-7Dx3y7MZesP1BcEZKhlRKDNF34d1UV-nDFQNxo2qOoDDFoeS_JrOEqE7CV3H3XSkhKBFN-Fs0MJGhuVTJ1klvUnGrz8xMtzjQfrIPX3tFnaFOVIO2__2VY3jypkRdsEAHuPAmvqTW4N8H7QCAWAcyB_FE5eY52UV5NduNXX8kXfsXceCvIYs_yrpjmM-1_FLp_ffmumQUGfJCFmPfE_aTdNdjQ0N4rTHMjjJXBmsjVF4XHbKHvYa-L7DPFin73Bh0Kc_xOlsES-2n710I3iyzX7Tg5Gpwnp75W64mBjL_dRXGIMewCCmnA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✔️
🇦🇷
تصاویری از لیونل‌مسی قبل از بازی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/Futball180TV/93768" target="_blank">📅 04:23 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93767">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd103cda89.mp4?token=NtTczu_VgWEPHr4Y_DeHOmlMXagZxL0bMWOfLm57tsXx0deAZJqGPebJ21cBqEDcKHsrFjWl5aJb_2e1WW__tqSCK3YoZOQ6Up07UphKdRk5XP-hi0GQElyXxVBj3DZuGVOcAWJAmN626b3SUkw1FfITCz36a9e2PHpImQ41-SBaW8IK5Wdi4LqEwkjFXo0Indcm4yBVupGdZ18o6MmYb84wPK_M-bnFY2_otBZIXmOAaiYVroxvR2RKG9lP1StCspSwdwuksupTdpxZI05aSa2KIQ5cqtZyDf6uETCVczlIh2JiT1MNFpkbjNPvSLhxSbmw9Aro7hDWCSUzPGcsyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd103cda89.mp4?token=NtTczu_VgWEPHr4Y_DeHOmlMXagZxL0bMWOfLm57tsXx0deAZJqGPebJ21cBqEDcKHsrFjWl5aJb_2e1WW__tqSCK3YoZOQ6Up07UphKdRk5XP-hi0GQElyXxVBj3DZuGVOcAWJAmN626b3SUkw1FfITCz36a9e2PHpImQ41-SBaW8IK5Wdi4LqEwkjFXo0Indcm4yBVupGdZ18o6MmYb84wPK_M-bnFY2_otBZIXmOAaiYVroxvR2RKG9lP1StCspSwdwuksupTdpxZI05aSa2KIQ5cqtZyDf6uETCVczlIh2JiT1MNFpkbjNPvSLhxSbmw9Aro7hDWCSUzPGcsyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🤣
واکنش مغزم بعد ۴۸ ساعت بی‌خوابی و هتریک نکردن هالند جلو عراق:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/93767" target="_blank">📅 04:11 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93766">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NI84QeRqnVpdcRilM27ukOEduvzU_wgl6_zFPpqn7b0U2IKnSc7FpBMwjZ9tPUXjFPo1F0xUd-BOW1SJpiVvtE95uiRx19GjdIbALSBPLDrYhQZ6Xm9u_8fSm6B7Pa4wbGxqOuYVOtEbiS6jsXRbAOToDBOEbfizELKuLBo5eH7b6clAL7LHU-cHP_GP6BI7IQnIHbB4M3vWZbLhfumQJMFimOPMRyttKmoLZAC7ecMmY8AdyrXUgnZcqE4y_1VN7u5fhGEwjDqsrVhdBOT9JqyisalhSIluWe7cDpObVWniBCs-oBjTS3RZGyEsTS9NbLx8TG5RuSOiHm8MoAcyWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔥
🔥
🇦🇷
خوراک‌استوری امروزتون جور شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/Futball180TV/93766" target="_blank">📅 04:04 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93765">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c84cb916a.mp4?token=ElRjqv3UPuQjHvTBPfT73RDqrYXa1EVRKtDewjhx4E06jTnLZAZDwTxUWZ1A8x4ywHe5bwFTZpTDMtac0ZPP7bsrj10jqRk8NAmnEu1OpGBxyKOPnnPaTR4Pzx6nv0H7UK-NF968njrjURriUBDmCpHYlCKSZg-keIK-uafRh9XtkHjp4mqtLfSLUj8CY8EplPGbxcic-0Yrlv7kHfynub1_wmbDp_Qq8gTzZM6N8fb7eabuA2nqBxY-_03QCWqGv58klrMDxHHLQXzuMF1BnOjdKqCy_y-dW2oaUJW1i3Py_J-CYrng3dxv-8YjqZsgRIxMjfVTXs4-O4mqguAScQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c84cb916a.mp4?token=ElRjqv3UPuQjHvTBPfT73RDqrYXa1EVRKtDewjhx4E06jTnLZAZDwTxUWZ1A8x4ywHe5bwFTZpTDMtac0ZPP7bsrj10jqRk8NAmnEu1OpGBxyKOPnnPaTR4Pzx6nv0H7UK-NF968njrjURriUBDmCpHYlCKSZg-keIK-uafRh9XtkHjp4mqtLfSLUj8CY8EplPGbxcic-0Yrlv7kHfynub1_wmbDp_Qq8gTzZM6N8fb7eabuA2nqBxY-_03QCWqGv58klrMDxHHLQXzuMF1BnOjdKqCy_y-dW2oaUJW1i3Py_J-CYrng3dxv-8YjqZsgRIxMjfVTXs4-O4mqguAScQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
🇩🇿
🇦🇷
خلاصه‌بازی امشب آرژانتین و الجزایر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/Futball180TV/93765" target="_blank">📅 04:01 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93764">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kO2fTenL0tiR5LdRq-hE0-cFM7C_QTKzSslLcG29i1uR4i84DtQN1BbzU0C1ijYHFoGKD8pAlz3wxe1ibjKyqAJj_5TbInXTqcNRageELOC3IVR41qG7SZGvqcZYCc4aWDAOnFuQKC5kYH2HZ1CRdyXqVwRcU5X-uM65solC9RNX7lNExgFdaPjxe6t9r4UhNPD6WlYbSVGh6CP6zYW_f4b_sIUfwEKhG0Ec183cWyjQmbG37FxetyQkF_AOLYjY_ej96t4kL7p5Vw_TUW_881r8lMd9kmhfINP5q2Kh92zM8wLvAXZDDZiwi1xSi1hW_dT9yur7qYZCqB3hntagOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پشمام عکسو حاجی
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/Futball180TV/93764" target="_blank">📅 03:55 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93763">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
🚨
🚨
💥
هم‌اکنون پیام ویدیویی ادمین QA بعد بت زدن روی هالند به دستمون رسیده. صدا کمممممم کنید بگا نرید خوشکلا
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/Futball180TV/93763" target="_blank">📅 03:51 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93762">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/02d6aa669b.mp4?token=L-UnZVHUyCfw67iKgfEy9LfWLJYDMagJr2k6GUFsB91peuRRYWT7_Kx4xp-FaNH6vh8xoL5VikUvzl2_YYTmsaZM2jQKrGnBOpwSMYbENb4xTCmNpmeQJ55yG1f4-f42NmggQmnH4CYPYCAuvNWq9zZGPuPpB52Xroo2tGXwMko9syn_fzO0k46LOxDlrw2oCCPVt8nyoBVn9xP562JUMZUA6mmCuge8uH-RpovWnrXsYuNJ40GjgEMmfcSoSPc7xAQi4vgKw5Wj_XLwqvhPf8DKwsnA_M1tyOMmvf7sqRjc0lAulhNvtezk_Aj7Vkz2Bweg8BljwypkRH2wmwxaUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/02d6aa669b.mp4?token=L-UnZVHUyCfw67iKgfEy9LfWLJYDMagJr2k6GUFsB91peuRRYWT7_Kx4xp-FaNH6vh8xoL5VikUvzl2_YYTmsaZM2jQKrGnBOpwSMYbENb4xTCmNpmeQJ55yG1f4-f42NmggQmnH4CYPYCAuvNWq9zZGPuPpB52Xroo2tGXwMko9syn_fzO0k46LOxDlrw2oCCPVt8nyoBVn9xP562JUMZUA6mmCuge8uH-RpovWnrXsYuNJ40GjgEMmfcSoSPc7xAQi4vgKw5Wj_XLwqvhPf8DKwsnA_M1tyOMmvf7sqRjc0lAulhNvtezk_Aj7Vkz2Bweg8BljwypkRH2wmwxaUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
‼️
پیجی که میبینید پیج ووزینیا گلر 40 ساله کیپ‌ورد هستش که تو 24 ساعت از 50 هزار فالوور به نزدیک 10 میلیون فالوور رسیده. بعد جالبه که نشسته داره فقط به دخترا بک میده.
کصکش خجالت بکش این کارا چیه.
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/Futball180TV/93762" target="_blank">📅 03:48 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93761">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iEe_zAhZKPCIxCVCOjJ7Rhu6xdJ5XiLm7-qzEp6roQh68oMBXNdHlGStoc4iFHazoUNmOmIM9Czv-9zv99590pq47KNarKso7SKbobDWN-DT9-YndZF0uKNQHegmnKnj0cTJOSXSJtm6T_4lcc-EpTEWj-akrFKV53ntLNk3ru93AHioEvSYfPfL6kyaip02dtn36ab_48q5_EFyorqTaYEEcai7aXU6sPCNy8FPjjZT_KiFdFAxHN0qP2MF9Bs3v9OxchnRFSsRNyXGJiPaNAsJQNfBtdg525zJSYx25EPMztcyjRiYRpwElsW3_vv0gqL7v7JVDkIb675sGFBVkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
🇳🇴
🇮🇶
ارلینگ هالند با ثبت دو گل و یک پاس‌گل بهترین بازیکن دیدار با عراق شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/Futball180TV/93761" target="_blank">📅 03:44 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93760">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HGczb5KgCAC7MnHPo8jxXBGafTBcS2jH8BPDvYxuWQOPKShqCbMgdKi_eqtZbUJJ3HYT4Q-0WcHOr3yqju13rqPRVKMmyF8PuL0l5c-3NSjJDqbY2-HykLs4aoeOiVgX50gCBfEzA_p4835Nci7ae6bDdB1dvYqLAckd9dOeLtM9g_qMj80SpxS2ay_HA6tqoXzFDDov07bSnGfxXZVNKnUk6YW2o2fibLvAMGshpN3BAU25R-Y_tyUjTafTmCS18vhkF3SxZ55wxNm3LirRon5yPQ1wfjUUL8rcOrq81Wj_LdRqnb_ZY2aRKd2BhXefiz_O_aQBGw1oGkTTGJjuYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
🔥
لیونل‌مسی به رکورد ۲۰۰ بازی ملی با پیراهن تیم‌ملی آرژانتین دست‌یافت و‌‌ رکوردار تاریخ شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/Futball180TV/93760" target="_blank">📅 03:40 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93759">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RPfN93OIgKBXWf4o3Maq76cc9yVnCcC2sVZLYEdpQeCJDoLpNjO4olGQOPrHo83HOfBSf-vHSYHctPXqbjjrAvgWbJnFGUfQxIYXYRuS6qQRDyhMfx4XBtMBZhHGxZ1uV6uMVErbRYYclKts9fz2kBl7Uw_m9ylIL_D7LrTwXY2GSKzcb81OPoK-X3IzuZ7ZUkfmYqpxG9AgAPXulk4wHyt1PoelnTL0e-ohg5LpqvqY4Edv54CtfzrbWUo0BYUc5QgU3I22oFLRYuiF-4zoSlYofk42jpMfwnm1_l_S-LH_m4aR3HkxsaB-Qxu-G9pL9iFlpnThMtEYBUHYJeU88w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
وضعیت جدول گروه I جام‌جهانی فوتبال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/Futball180TV/93759" target="_blank">📅 03:39 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93758">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JPnNIuoo2e8r6mftD61SrMm0ICif5J-e6G3u2ESn1UHhKy4Yb-d0gjM7nwXe17rA6wJOkxu1FER7-F1q3uA34JnW6dQPArZ3HXFwfcMQf96NGpvq9oZDfpFw0mVdIpV5p-7JkaQ8N0kGPTUdQg4kBfDveT6v3PSwmOdciLuf2_lw3zkZ_eHrExYgXfFoRhm9cHp9PlFg0gvoZ9GfLDfj1Qac2BrmUWYKDrSCul_vvsr86a0VNzDEXr-9Tlzj1XLuWx9_9rtfgllTyB-g1sGsMKD8ju0CUUsVfnvIjykIicF-bF4TenQK7msCx0ypj5gqXbo87Z9EZ24R7Ybm1IoCzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
🔥
🔥
🔥
برید کنار که صاحبش رسیددددددد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/Futball180TV/93758" target="_blank">📅 03:37 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93757">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01dab461fb.mp4?token=BgWZqjOHGl4UoBmY3QChjVeRnqPKnZTWZSxUhKK-noGdKMhGpiHd7kL3AC8U6oI_n6eSFa_H_yN3u1tLY7z49MwlqhcOq3NW9dOAu-xkwoNqx5c6JzlZMasfUlr8QaqvaUtQ98C8tvrckgsK5-hkk45sk-MHVWitnhCmOGTST2vTfIfUPlKsaXm0eZD37oScte88wpfRsvTx5y_FoCvXbcJW-jjwVxoVx6lQthlFcDAS_DAZLBlHAjBy_awfjS_m9Is9FQbZhb0FA2Z1_436HBZNAfi6q-So52m0S8O8rRpvCi-oUp0Ry98pLuu5QgIxowxFUKOV-Cd6kkMvalgnwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01dab461fb.mp4?token=BgWZqjOHGl4UoBmY3QChjVeRnqPKnZTWZSxUhKK-noGdKMhGpiHd7kL3AC8U6oI_n6eSFa_H_yN3u1tLY7z49MwlqhcOq3NW9dOAu-xkwoNqx5c6JzlZMasfUlr8QaqvaUtQ98C8tvrckgsK5-hkk45sk-MHVWitnhCmOGTST2vTfIfUPlKsaXm0eZD37oScte88wpfRsvTx5y_FoCvXbcJW-jjwVxoVx6lQthlFcDAS_DAZLBlHAjBy_awfjS_m9Is9FQbZhb0FA2Z1_436HBZNAfi6q-So52m0S8O8rRpvCi-oUp0Ry98pLuu5QgIxowxFUKOV-Cd6kkMvalgnwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
💥
هم‌اکنون پیام ویدیویی ادمین QA بعد بت زدن روی هالند به دستمون رسیده. صدا کمممممم کنید بگا نرید خوشکلا
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/Futball180TV/93757" target="_blank">📅 03:34 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93756">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/5bf846ae8a.mp4?token=fvq2kdP1IrVsJnrSdmS6S8-_jNIKPDrM0EXAmKFb1ad0qjmp-cJttNsNmSwPYtQZE6jPnvw-IiXk4eCRF9L0epskvZxx5177-ZjzPy-_5FA39iTStJQcLJ_B6A2l1pWKpDp2MiFN-f7EPSHaBiBNOtIdqZ1DFLD0ZfyT5CSOhYfbTwNwvYGBjwhxIMl2QzYTB3kaHqt6ztNr90i4-spWj1ofT7HCxbIfNdlqYp8heypqrEslPtuCEvKvNX48Vx5e0gzOGFo74wQ6_KY9IBAlhn8NDjxvm9X5onDuYAbuJfo8WMtdP-nppiqDp0Gbk94AZQ4fSWzlHinbm5lFZHyiu3A4_nHbZCgSWfeqFr5AY4bpcrw7qCj3sqZu3HOSRfH0xhOrUyDaFuofv7dsLp4AlHKMQXWmXSbK8YkqOZomkct0djIyPyAvNzLR0QvRwZh1y46fb3GyxCEumPguS8Zvj97ltLGtQeGANoiJS9k19cWNDVOTsCFsX-77T-ePK5Eb5w50RDJ5SCbcNp71VWGRkkiZeVGrRizrpsCHiO1633OtwEVsfZ37RIawv3IBochh-bjRP3JYtcCuczn_kfpqRsDlidoKfu8USTRGX6LGnBBXBZ_3914Sp7ziTxtTSZRCfPJxOHsDcu5-YJ0q-sKTHdqCW40m_d3u9n_klH46ejU" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/5bf846ae8a.mp4?token=fvq2kdP1IrVsJnrSdmS6S8-_jNIKPDrM0EXAmKFb1ad0qjmp-cJttNsNmSwPYtQZE6jPnvw-IiXk4eCRF9L0epskvZxx5177-ZjzPy-_5FA39iTStJQcLJ_B6A2l1pWKpDp2MiFN-f7EPSHaBiBNOtIdqZ1DFLD0ZfyT5CSOhYfbTwNwvYGBjwhxIMl2QzYTB3kaHqt6ztNr90i4-spWj1ofT7HCxbIfNdlqYp8heypqrEslPtuCEvKvNX48Vx5e0gzOGFo74wQ6_KY9IBAlhn8NDjxvm9X5onDuYAbuJfo8WMtdP-nppiqDp0Gbk94AZQ4fSWzlHinbm5lFZHyiu3A4_nHbZCgSWfeqFr5AY4bpcrw7qCj3sqZu3HOSRfH0xhOrUyDaFuofv7dsLp4AlHKMQXWmXSbK8YkqOZomkct0djIyPyAvNzLR0QvRwZh1y46fb3GyxCEumPguS8Zvj97ltLGtQeGANoiJS9k19cWNDVOTsCFsX-77T-ePK5Eb5w50RDJ5SCbcNp71VWGRkkiZeVGrRizrpsCHiO1633OtwEVsfZ37RIawv3IBochh-bjRP3JYtcCuczn_kfpqRsDlidoKfu8USTRGX6LGnBBXBZ_3914Sp7ziTxtTSZRCfPJxOHsDcu5-YJ0q-sKTHdqCW40m_d3u9n_klH46ejU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
گل چهارم نروژ به عراق با پاس گل هالند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/Futball180TV/93756" target="_blank">📅 03:32 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93755">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚨
🏆
پایان‌بازی|همسایه ایران در جام‌جهانی مورد تجاوز قرار گرفت؛ وایکینگ‌ها تیم پر ادعای عراق را سلاخی کردند
🇳🇴
نروژ
😀
-
😃
عراق
🇮🇶
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/Futball180TV/93755" target="_blank">📅 03:32 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93754">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">هالند پاس گل داد.</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/Futball180TV/93754" target="_blank">📅 03:31 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93753">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">نروووووژ</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/93753" target="_blank">📅 03:29 · 27 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
