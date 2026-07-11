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
<img src="https://cdn5.telesco.pe/file/a6TQU73zpo7YSwFtau3smlKrkw8KjNq9ZO6rEtloE4-ELkmHJU859mNADUSa2RQLl0LYQD8H86HSqKqFlfxpEjNoHWYO4CtETlv3CIvcuGfXwDga7aykBMx-IPEExu--xBdkyz-FHXqBuwdoixSv-g2u7eYgPFX7PVNz31_jaSeYbRU1Qspi_MxrjsdMXz_JoncDCSdE5dUtoyuA_AB5SunzL6nJLD7dbzHoRO-z04t-ublL6CUdLjvntt7Th94_rG7qTv52GuWuaAzxpX9VcXgTUKJMyDmAK6RLnu5_hnecrgGIVcnLN2pfJj-ML3JrgmcaYeupBpzQUmWIAe1IGQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 593K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-20 23:09:05</div>
<hr>

<div class="tg-post" id="msg-99606">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t1x_o_VXIwtvefMm3as6felqOEPgLW-wFPmkx5WpasWC6ZG5LEmFZqkQUepl82n5CsUEGaRSMaN87BHBQVS2CT2czu9euYA8Gcsua6aKLsdurwLk1tECI9da5fcI5P15BZ_2xTINqAds19CajcYpZeV_T-GF6vgkBnsYmAGJ1v6UijPPCHiareYfUiNM5AVNzYcDqq60NSOqp9S251ENNcFDV6_DVYIjOecw-KapTEDH7Scb_45DfUfoaBjPEMr3SsUGtxboDg7TY036Os2Qg_wldPxGTvvfiyQRvBQZ-HTYMvAW-k_1jfk5g8SIv9elskvlOfbrlexYj7p-e87JrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇳🇴
ترکیب تیم‌ملی نروژ مقابل انگلیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.97K · <a href="https://t.me/Futball180TV/99606" target="_blank">📅 22:58 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99605">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QiIjq0jYhb9vEHWravVYI3CROqCHpBuDs6Q_upCnr9-Oaz3MTdxytYK695Cxl7DHd8TIomFV7QXJDc44jW6MFAKknzpUaRKmHN-d2WCVTsgsiNQyWKxBOIRs0oh0pTZnnM6A0u2cN0p7f5FwL8iLPY0a0uZkn6E93S4YjFgmHELfl3hBKpaYnzp423HNCEMm34_3Unv2n-7ux_CEDm8jFEHGgQA3sQiZ2jP7sqeMr7F6t9SvJKql_tiF19XEr-eNEF9_tXV_-f5324Ucb3j-kC7Jd8AvFbdlITdW8lCfHxkbBjSH6JdVPoVuzbqHDnCvtfCTxDC6Rfwp-F8bgyys6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همیشه یکی هست که عکسو خراب کنه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/Futball180TV/99605" target="_blank">📅 22:55 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99604">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YzMr59aHm1NCPhtZ2QxrPeMP4y0JIdQNtoQ60XxHopEtSzzzZkB5_7eau87MEWXypgonbpErLKYZFuVg_6QzAbLjNO-JaWSSSSxKlVxP8gKauO-FSqelvqGBrcR1j22ak9QSBeskce4OqEMOcAQx4GblGWnFl2MciOn9hlUaHG3zSqcSDPDNiZFT-9hz7iFDikz0WqKNdieQi2NAc5KUPakKxcJYtfr7M-Bxx5-YHLn_wpg0aAAe0GehqmVSidluZmer_cJ08S2-LqLmPXEWbYQTCO_0DUQwuRDaeGYh2GjYAVF3LvcQPVe8MGju1V8r4PFPQ88jB25eHqFGupLbsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
ترکیبببببببب انگلیس مقابل نروژ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.39K · <a href="https://t.me/Futball180TV/99604" target="_blank">📅 22:53 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99603">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Km3FKwAamkQlF06825qdvVyW1oxbUPRcYeyjazXcRR4KBkuIRM7wKPVdwLJ1A1ry9YeG3CG7-nfghkgkQe1yTLHKV1-UJyKf_GLzw5CajIE9G_ctDzkcSE_Sh-ck7Fm0JMSK5IYYdRH7hQqx39c2JNlbT3NU6pnuGMXXTswziaRSAWBbUy5ZGQQVcL73n6Mozjnp3AmpUfYGy_gw_hMLn0JP-kcnhZRftEUAxg5Q1zNxXEtLeBhhQSoO0HhI4H0bYmvMWKQg4PQtIS4OO4XVwT8cDURPAF8KNo4LS6AlB25_pJ935oTU67guzm7PuMtR_T2MJtt5AX8VSGPBxA-32A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کیفش کوکه
😂
😂
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.61K · <a href="https://t.me/Futball180TV/99603" target="_blank">📅 22:47 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99602">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c14b876fe.mp4?token=Ny0y5gZHj5LSVeFFo3_VJRcdZBX-hONPkfvRLx4zqPMJa1OF1dFv41WV2uIw_PGaW1gHBeOtkn_rqf3vggz8PNA6A1xJ-kFHJWWmH7XZbSkcXYcHd-mNbEzNnYlAmVRDDDiTi2VusL8MnGdE7w4LGu7D0XJfiim3niHQ0BgeOmqdbHUjukFQTp8733f0-NLz_zk5UmvnvdmM5S5IFo6mJ2IRRojqmylV8BfpbCAWnILuIStabJrqhppt_nqAyPj8A0W8ZmK30oKraUiHdkdBHhx4BCKBv5QYcXtIH23GZvki3eUZIL9PJmw-epc5oy6Q2t6t8VmQhKwr9-uO1rb0MA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c14b876fe.mp4?token=Ny0y5gZHj5LSVeFFo3_VJRcdZBX-hONPkfvRLx4zqPMJa1OF1dFv41WV2uIw_PGaW1gHBeOtkn_rqf3vggz8PNA6A1xJ-kFHJWWmH7XZbSkcXYcHd-mNbEzNnYlAmVRDDDiTi2VusL8MnGdE7w4LGu7D0XJfiim3niHQ0BgeOmqdbHUjukFQTp8733f0-NLz_zk5UmvnvdmM5S5IFo6mJ2IRRojqmylV8BfpbCAWnILuIStabJrqhppt_nqAyPj8A0W8ZmK30oKraUiHdkdBHhx4BCKBv5QYcXtIH23GZvki3eUZIL9PJmw-epc5oy6Q2t6t8VmQhKwr9-uO1rb0MA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇳🇴
هالند حتی تو تمرین به موانع رحم نمیکنه
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.83K · <a href="https://t.me/Futball180TV/99602" target="_blank">📅 22:40 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99601">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HxDSUON6Qpr1Krp3Sp8zX0IRsGikx-23SQhYHWDQoivl0yFq5FiRdFt5eiSpeWdi5I9F6XWyA-Ifb2r9cjXVTiG2PlsUJw0AMnBlGc5Q3DpNqE-XntMnsGjVQZzb9-ENhdDdZ1d5caChiRgvT9pbeRewnPgA-LsV31su6xo5JChyUwUXx4pjyz5dsJWxfrqMYNTqQyRfQXRogTHYC0Bjt8uV3zg0-1jFa2_8KDaAaFXN1mqVNHLJMSC-VG3pNbWLmnUpp4IlhhIcqsUp3iwjpMav95nU3CC7ersu7oTUQKGssnyG52aVRFrF5k6Dcyz4hpdoMnWSv1v0L4-UkIpezQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
فوری:
جیانی اینفانتینو، رئیس فیفا، اعلام کرد که برگزاری جام جهانی با حضور ۶۴ تیم در آینده امکان‌پذیر است و این موضوع پس از پایان این دوره از رقابت‌ها بررسی خواهد شد؛ او تأکید کرد که جام جهانی باید متعلق به تمام جهان باشد، نه فقط اروپا و آمریکای جنوبی، و هر کشوری باید این رؤیا را داشته باشد که روزی در بزرگ‌ترین تورنمنت فوتبال جهان حضور پیدا کند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/Futball180TV/99601" target="_blank">📅 22:32 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99600">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WyxPCuhSuQudQgFEkgOxX5pVnUNrrOu9oFn-W9HegA4gB3VdbKLiicCF4qh3qQP0pKrzgcTX6p_XLqrpRS8VZ5jEW-8GxxvzX800s9qujTa0drB4p1ylhppfXFwzQngu0tx7WhjvPhoJMqM7ksH59fnUv-rXKUH2np_LvVguAzt-v9sIgqpriUFq_NtZyOsSPWKRJfAjgIcNHns2t-favEaIQ8P_EsWzHZ-mjsVOqH10fSuqV1KOmKCIx2IdxdbLwCJ5eCWJMqWbmVZX1OAfMV_sIFiR0wn7LEF_wQEHqD9sZkBU9waTwOMrPnOr8JnpNdODLrUcrQVDHAZORVMsjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
فابریزیو رومانو:
🇮🇹
✅
پائولو مالدینی، به عنوان مدیر فنی جدید تیم ملی ایتالیا انتخاب شد.
HEREEE WEEE GO
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.74K · <a href="https://t.me/Futball180TV/99600" target="_blank">📅 22:32 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99599">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vreQ1k918WQcP2G4169jQDGQ06dPEpweh9BzNqV2XmfZ4oxQYMZUZTVIs93l6Aycu1M9Fu0hUNMc7hUuW5-8h2vlK4shErHcWT0OgmQr5wlyRizE_cN6M31EQSYq0_tX62sgQ7HVSfvOQ1SVobhp2da-kkcfVeNBjt8H5jkVALz3A6XfZIwgX_8deAHgCky_4-ci89Ev02glSVCtCX9M8lcoFfIRUJqeSXxp8ZZ7y__L_ihlG_JXkkgIqFezVEY7NTTIM8NXiKZWTvz-857ag5xBPQWoSavMboOMafXCLnbR_L_iZIoY8i9gJCv_1EJ_28YXoaHGk9WrotEzLCAK2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
انگلیس تنها سه بار در مرحله یک چهارم نهایی جام جهانی پیروز شده و 7 بار حذف شده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/Futball180TV/99599" target="_blank">📅 22:24 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99598">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/StG4NVdDDhX3Lw-LiFlWCIQ6dhEjXUuUUaPxgVfTz0o_auMnCLI_YrNAtPpj5VaPPq0eWA3d9OC22N6DJdfgKlnkv3ci69B4MEfvMDwHQTNimnNpRhY6syloUFsMcPUrJL0N8Aos6wAENMwPQBUgQd_hqyJI9ZDPKXb2RTlyYNmp8-OwwE4Gr9RkZN1UKtmkohSRgKqJ_5KV9q4K-_xHs_RblKb-W_8b7HLqmr0JXOoiHgII4sMsHCUq0THEjDrDI08PpGkx49jZ-vSBMMJGS9IWU36jwIUw0EWsSWU1gif9V7VCYIfbgtr0o4VHVzePrBUwY1t-uTAs-3_EKYUAVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
اورنشتین
: توخل که آرنولد رو به تیم ملی انگلیس دعوت نکرد الان قراره ازری کونسا رو امشب مقابل نروژ تو پست دفاع راست فیکس کنه
😳
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/Futball180TV/99598" target="_blank">📅 22:24 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99597">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1b14b56d3.mp4?token=huql2b5kc3RRt1U08sS6iJnwOq5YhlGVaDtnxEn7tM8vTjTBG_6247sDEDm6z7fgJUN5lEjDpUryotmeybrx63KS_sH8-GxCofdu9zE2TK90Vb_iRQZ7Jdd5VzV8hPA6_IYFPbBOvwCWPQDX9k_eX2sx7XIxVfCL70sILMgutnLcIV9McG5AQ-7q_ANRIb_PmGh0kiGoOe68e6jnOfAYl9nGOMaS7kmfxRpg_xKwzXCbWFntbuQ0oRlDyK2ETh8slkE63GlnZhy5_lMuy77W9Rx3cCEaZtcIYgq_boUYvb2XoJPCcqZpgwqYbRg_7N1VXOrW5Zs0fKoxMiCDbOXXnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1b14b56d3.mp4?token=huql2b5kc3RRt1U08sS6iJnwOq5YhlGVaDtnxEn7tM8vTjTBG_6247sDEDm6z7fgJUN5lEjDpUryotmeybrx63KS_sH8-GxCofdu9zE2TK90Vb_iRQZ7Jdd5VzV8hPA6_IYFPbBOvwCWPQDX9k_eX2sx7XIxVfCL70sILMgutnLcIV9McG5AQ-7q_ANRIb_PmGh0kiGoOe68e6jnOfAYl9nGOMaS7kmfxRpg_xKwzXCbWFntbuQ0oRlDyK2ETh8slkE63GlnZhy5_lMuy77W9Rx3cCEaZtcIYgq_boUYvb2XoJPCcqZpgwqYbRg_7N1VXOrW5Zs0fKoxMiCDbOXXnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
🇦🇷
هواداران آرژانتین در بازی امشب:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/99597" target="_blank">📅 22:10 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99596">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dswmoyvEJM3pHj790UjvKx0SeagxLk0CAlqABK37j4w7Huc2wA2nZ7WGiXm4Kzou49Lwc-d8iQFx3zd6rkxXZLCLxCsSShyfg1Q95htq2TbUpCGmDZJxlgLd2sPYdZjP47JTS4pKVjK_0Jd_fe10YRSp-BAXFwos_D-sX1-IjVHd36INukxOk-P4cvnLtrorlj_-JqfSlAPpMOzz3XpXMX6FYzN6id83fqUDCZeyJ8IyvO0TGR-YydTySXD7y4y6ppBMHgWSXBW-_yM5CxY140EJYZ3iA60bJe8KlyXAN1627H1_lo10OchjHiNj0pbko6nqS9MHEd9giDgBqnPZFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📸
🇦🇷
عکس همیشگی قبل از هر بازی: رئیس‌جمهور آرژانتین با مسی و بادیگارد قبل از بازی با سوئیس.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/Futball180TV/99596" target="_blank">📅 21:57 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99595">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DgOW3jeDYDWjv37TkeMdkqpIAfvU5bP4REZ5hWv1z2ciChPlO7lVoAAdi9nYskaxBLGFy6yiK0Y4t_yD8_fJl22nnUGvDIT7tYneARKBmWeNruU7tfvRd24_vY9ydQp5u5CxU8bcQoCuv-9p_pOYrviJfZ3o0nNplrFE9q6NBMUBFMBUr9jk_9Ugllpr2mKNWNRMXV-Dy9Qvz8fl_2Hr9UqqPLKzM-6C2Q9fZIIdgD7jgNU7pAEbQgUnkwlrmXVrA1LaSG2kZwyVo_G38z756RwrD_RoNCGfuCK1fCwzwdXfA9v761pv6RX_DMwxRq25olEGfeL2MrQf-kaloqwt3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جورجینا در کنار رونالدو با کپشن “Daddy
💘
” که میگه کریس حسابی حالش خوبه، نگرانش نباشید و برید به بگاییای خودتون برسید.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/99595" target="_blank">📅 21:52 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99594">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/241daffc9d.mp4?token=qHFAa-k6AmwyiF6cxCTC13F8S1gG8Lzh3CvFSZ1Ke34LuElhK6D1hio_k6PAjpoCTtjt9IU4hW-J3t-fSOsJVpnu8eCIaR0qRJu0o9y71iVjAajwgjGXHkloSzUVzDEZBK3J4zNk9KftYOwrEv0-T8m_ocRyC7Qrkm_3UCcLQZ6I5fVPW8_f2BirAUCVXLxP6Cr1lgXDVeUkPG0o5iddxyhbhD97lFuS5aTkY7AQpSe6hFxRGHq9emUHai-whc_3kMvMBhe81TUjtn0JLjqScm45spgEfVvP4QlACA0pZlh2vCXOqA2-f-L0CnnPhqSIgCEGSiqDD0O4AdToNrjkxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/241daffc9d.mp4?token=qHFAa-k6AmwyiF6cxCTC13F8S1gG8Lzh3CvFSZ1Ke34LuElhK6D1hio_k6PAjpoCTtjt9IU4hW-J3t-fSOsJVpnu8eCIaR0qRJu0o9y71iVjAajwgjGXHkloSzUVzDEZBK3J4zNk9KftYOwrEv0-T8m_ocRyC7Qrkm_3UCcLQZ6I5fVPW8_f2BirAUCVXLxP6Cr1lgXDVeUkPG0o5iddxyhbhD97lFuS5aTkY7AQpSe6hFxRGHq9emUHai-whc_3kMvMBhe81TUjtn0JLjqScm45spgEfVvP4QlACA0pZlh2vCXOqA2-f-L0CnnPhqSIgCEGSiqDD0O4AdToNrjkxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
😢
پیمان حدادی: نه‌تنها حقوقم را پس نمی‌دهم بلکه پاداش هم می‌خواهم!
وعده پس دادن حقوق در صورت عدم قهرمانی؟ حقوق سه سال من حدود ۳/۵ میلیارد می‌شود/ حقوق ماهیانه من فقط ۲۰۰ میلیون تومان است/ لیگ ادامه پیدا نکرد و هشت بازی دیگر باقی مانده بود/ برای اینکه دوماه تلاش کردم که تیم ششم جدول شانس سهمیه آسیایی داشته باشد، باید پاداش هم بگیرم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/99594" target="_blank">📅 21:49 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99593">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/702b2e97d9.mp4?token=vagJU7kHKTbxGdygra3tjYonKT8GlKa2ExNbxUzk89By0nZ88-3RCcxmexDwNf-fbk6ZvnrMci1RRpaaqMZ5hhk6zKhAglqtcXC-Z7umak6gahxhZ5pUREDcT3JwAABdUUIsbUOPXe5zQR-WtEiNW0Fr14N9tkPGH82YAYd4niS_QD8bMbz1b8OvxnPV8TTdC7vvqEMtFeTOjX1nX3RCBADWdSonIzkIBh55zsKSyi5ujD5pFXExS44ROVPprUdffg1afcxclOmRu10kX-7Hb7sTFKC-qWcO12VdbyfGKXzDoAiyHzVXromynaAg5fjVt2xMHkugsE9IM0wBne7law" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/702b2e97d9.mp4?token=vagJU7kHKTbxGdygra3tjYonKT8GlKa2ExNbxUzk89By0nZ88-3RCcxmexDwNf-fbk6ZvnrMci1RRpaaqMZ5hhk6zKhAglqtcXC-Z7umak6gahxhZ5pUREDcT3JwAABdUUIsbUOPXe5zQR-WtEiNW0Fr14N9tkPGH82YAYd4niS_QD8bMbz1b8OvxnPV8TTdC7vvqEMtFeTOjX1nX3RCBADWdSonIzkIBh55zsKSyi5ujD5pFXExS44ROVPprUdffg1afcxclOmRu10kX-7Hb7sTFKC-qWcO12VdbyfGKXzDoAiyHzVXromynaAg5fjVt2xMHkugsE9IM0wBne7law" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇪🇬
استقبال رئیس‌جمهور مصر از اعضای تیم فوتبال این کشور در بدو ورود به مصر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/99593" target="_blank">📅 21:30 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99592">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u9FLSEzwLIZvPYiXHRCp_WOZRujrb43fIJFQBUsbqfZx5mZ57NQXBFcV9owpIISeOEe1lPeyBo2ctXLIcLlQe6hqX_KR_Hhn6QrWScQjceyPWP2ZxG6qrGzwtOIJP-pZP1rTKRVbyj_gC41Fv8Wsbw5U25u-kPbSxHvF0mixuXzO9LpJJUOCNilHEbIRXBtvnf4l4IB2lJYhotCo5zL7w1beKJ5VVCUUYzSqy4nvc4GefcNHcn5--eatZSJVKedaJxWJKmT-e9JPBkGx_hiKiwbW_l_y3qjGJdwujFfaecPMPLkuPWszNbLT2LR33zYnWZO3DOdT7qRnkC5k9k0bIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
📰
اسکای اسپورت:
🏴󠁧󠁢󠁥󠁮󠁧󠁿
باشگاه منچستر یونایتد گزارش‌هایی را که حاکی از لغو قرارداد با ادرسون است را تکذیب کرد و اعلام نمود که همه چیز طبق برنامه پیش می‌رود!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/99592" target="_blank">📅 21:20 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99591">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/773137bee7.mp4?token=qlWOGWabnYwJ-LB0E09h5G5E1GJoYCOFk3P-RLUnJAk769hvbZX75D4-I4iqCD7_GXqHU2SSsJpBY2wri83gkbZLUTO969hsgf0BJ8EBt5bzpUYdkdR2KwfZU6RkHHaFYU5UocwnMZVMa4ZCU-a-mzwrEJ2xeljFMbC95EmlYzZ620S1bkwIus0a5k_HolevRVh4mdyibT88KcO_4X-LHdhhfe9lElOTwWhwz5E9fcf5cPQlqFub63Ta2n2gYt-mtvPfnZ5T_5ZRom4OSk_B-QidKs-Eif_fRGBQR9KoMQOfAsb7NzKcfMffTCsorrMxwR6FzJCKZKQaGL5TMKKNNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/773137bee7.mp4?token=qlWOGWabnYwJ-LB0E09h5G5E1GJoYCOFk3P-RLUnJAk769hvbZX75D4-I4iqCD7_GXqHU2SSsJpBY2wri83gkbZLUTO969hsgf0BJ8EBt5bzpUYdkdR2KwfZU6RkHHaFYU5UocwnMZVMa4ZCU-a-mzwrEJ2xeljFMbC95EmlYzZ620S1bkwIus0a5k_HolevRVh4mdyibT88KcO_4X-LHdhhfe9lElOTwWhwz5E9fcf5cPQlqFub63Ta2n2gYt-mtvPfnZ5T_5ZRom4OSk_B-QidKs-Eif_fRGBQR9KoMQOfAsb7NzKcfMffTCsorrMxwR6FzJCKZKQaGL5TMKKNNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
💥
وقتی عادل فردوسی‌پور هم از ناز و عشوه شکیرا ذوق‌زده میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/99591" target="_blank">📅 21:08 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99590">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bBi4xUzdf-yO9y57d5ASqxZOEsLlZ5Mj5PlU0gdVwYwH2yOKMfnzjm8d-raWpbFqnNwx6dhA7MZ9ZrGw4wWGYD61tR0PNumwE6CwZrKuWl4wndSAjVBh2XC3Fquvrxcd5DRd9de_ssJhY1TB57wu_zYgy4w8H0Wd3RMQRnZf1w1ASu-oI6XOI2wF2mLhgear74SbpAu6TDmJrBAPtINop8sJkM2NwU9XIidNHSErWP8NLmFjq2dWv_7whT7Sc4NNXu1kStoAUzr8NIuu-7dx98RpNgunuWtb7J1aCO1dqtVmji108aDAZTUld2fdTQ3vLgoKFA3JtqrCchNz82LKig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
ژابی آلونسو افکت؛ او فقط مربیگری نمیکنه، رفاقت میکنه.
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/99590" target="_blank">📅 20:48 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99589">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PyK7wm743sMHZE1TTKe63nlfh7j0K1ziUL58CRpxY_pP7wUJ37jdAi-q6Bg74qJ0y3PQ1PnTmVf4jFjxJSg9SRdtUQdsljku54V-z7YkFsGVtavhjbGB6uyNT3PEEOFGHQcpK-VEug8KrV88x3Q5ce1H4pj-7bSBvY6Dk964e63j4ip_HWCsgdApCIUxt83RHlNYixncYNTd1l-9qD2wmhun0H1ZkGzTVBFwtOxrf_fePnsC-OlekAf49r-D81nrt07bkdWLdTuXG_sy3_eYHheiEvBl1x77HiC4zIpxiGuOKZzZakJDD3BiMgpE3uUJeBHdnGBBm1d58eNgEbqjCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇨🇴
#فوووووری
؛ کارتل‌های مواد مخدر و اشرار کلمبیا در پیام‌های خصوصی به کامباز بازیکن این کشور بدلیل از دست دادن موقعیت تک به تک در دیدار با سوئیس این بازیکن رو تهدید به قتل کردن و گفتن که در این کشور حاضر نشه وگرنه به قتل میرسه
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/99589" target="_blank">📅 20:46 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99588">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D9Kek5HXsHW2DJe0gck9kzy7Cw6aaggVitzxiUjWos3Hr9nihaicdMncj98y9dl3UUMCCluurRweuHVXg1mzLP2w87iPKwVIij3r15MLWagXvseYyoY9Xrh-HNM0GXlPCHQeQ43Oda0FP7B5b1VxhoZruv34th6QOOhd6F3e7EHas8R7fbNO262HAVsVauHNpJMEMPBZTiRc1JebutDN4z3lngKuqHwGCvFIGfUFsHxn9Q342YU1Lp-FOkSytlsc6sqtiQkaLURa9e3be-j8ftxczRAGlJkE8-OywefGgJraQD3v7YO5YyhFRZUBX05wxSqZb8QZ6J5sH482niguiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
مسی همچنان ادامه میده یا به این قاب میپیونده:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/99588" target="_blank">📅 20:40 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99587">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80421a357f.mp4?token=YbXx9OrIEhZ9hlUH4h0EW1v2ucjK0zeowp1iHSfFdAvluAD4ZH4VEZ-Y_hI-w8WFUCDMPU5crwz7LmE0_TCPV84PuatV21EtxHah_B8lXUj21SRH3r_AVK0NWC5R7QVfwDEMvJrKF1VOQUg0pYvuVDAlo8BOKL90BlRKiErB4Z39sZAYwX2ZVzu3QqlTDCoSGz9-KoI9CfC6rkpxcvuSo062OD4jcTalhHyLgPNxNcTRFsvydRO1Ju1PQFKelvV-VWy3eyZZbAJebBmd_wMKDuslwAmJ6nzpdRl0YOtT69okPLyxRadrJksDxvlMrJu7GFV6NMo51HzR--W__xT9bw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80421a357f.mp4?token=YbXx9OrIEhZ9hlUH4h0EW1v2ucjK0zeowp1iHSfFdAvluAD4ZH4VEZ-Y_hI-w8WFUCDMPU5crwz7LmE0_TCPV84PuatV21EtxHah_B8lXUj21SRH3r_AVK0NWC5R7QVfwDEMvJrKF1VOQUg0pYvuVDAlo8BOKL90BlRKiErB4Z39sZAYwX2ZVzu3QqlTDCoSGz9-KoI9CfC6rkpxcvuSo062OD4jcTalhHyLgPNxNcTRFsvydRO1Ju1PQFKelvV-VWy3eyZZbAJebBmd_wMKDuslwAmJ6nzpdRl0YOtT69okPLyxRadrJksDxvlMrJu7GFV6NMo51HzR--W__xT9bw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
حمله مردم به مجریان صداوسیما در مشهد
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/99587" target="_blank">📅 20:36 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99586">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BLW9vKaPDfKYhilnbu5P8HI4H8okQ4_m-Ikk_uohmt8tfnXtUEIkt1XiJxLg9RjmEvLa-XU3ZDdZRuSLtDQtvjHPD-HVRGErtkUbClIQOmuQ70_iqtSZK5xZtk_dfH0Uj5yY3AgeFt2NJjKzKdFAH70dqM6dSASTaAtnblcEGRNmpTNfXwSrsGCKjwHGGRbmDJNXmLQL_ooqBG29SyJwY7ePwc8r_0w23h4Wz-vC-HBLvv2PvCO1I8bOCdm6Tl37anvEeXw5w4mODIN9iNybpwhaDXIf_doCRjwfzpUPUKU0_2u2Gu7pp90QBAYgXug1L8fqT8-ofBD3B_61z3x9Zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇹
🗞
رومانو: الکس خیمنز مهاجم بورنموث با عقد قراردادی به فیورنتینا پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/99586" target="_blank">📅 20:36 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99585">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">با رومابت
✅
بازی های
#جام_جهانی
رو با کمترین ریسک پیشبینی کن
😍
⚽️
انگلیس
-
نروژ
آدرس ثبت نام
👇
✅
https://halvirox9371.bar
ادرس کانال تلگرام
👇
💠
@RomaBet_official</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/99585" target="_blank">📅 20:35 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99584">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wb8mL9bcp6k0_pe7Z3I7ywGyIcgzyfUKaaj1a1aOyFFh97aHAlIJ6hksB4Agm_4mD3XO_Ypkd1hjjWGcvir6sVlR0KsTgRLd41hkwAAl9AoluP1igg_gCkdEgCQNgGFL2tdRPa9gRu6hFzrBi5AhIhlHGurE_my9HocCUALtKUF2UlfGCSpyUCr60YrRQTvAOuU4T1AUlTDrcz84cXH92NqKA70cRYKczFLXBx8VnGpHOznfnb-NGBe8YedyDDHsjfxYp3t4Z02ec3e3fDOCz_PySitbdODWBudBH1XMcDZSVhHEKw0KOqUd_wZhRyenPBOThJMRUMSMBvs8KPJxow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
مسابقات جام جهانی 2026
⚽️
🏛️
رومابت دنیای آفر ها و بونوس های ورزشی و کازینویی میباشد
✅
🎁
با شرطبندی روی مسابقات جام جهانی وارد تورنومنت 2.500.000.000 تومانی رومابت شوید
✅
#میلیاردی
🚨
همین حالا وارد حساب کاربری شوید و شرط مورد نظر خود را ثبت کنید
👇
🌐
https://halvirox9371.bar
✅
کانال تلگرامی
#رومابت
👇
G20
🔵
@RomaBet_official</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/99584" target="_blank">📅 20:35 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99583">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b93b2a590d.mp4?token=qQ5VZST70zXsDfrnRecFHMiCW2_ZxrzsubTNNk5u7Z0uEBn0ZoLS2uMIVTm7FZSXe46giMQKpPQX2hQE_Uzcvf3AOkgK9bn4AKCiJePNE977uLy22FR7dWkKyEBB1_8Nu-Cicim7sDkIz8uOf5wkP3g4WIuvzrKIdWtfAqFEqebNc0-xLtXzYhgAgmYXKC3oQ6G-nqlI0lXXQV7DfBwXs4bJiUg5R_lzqtl-jm-Mk3C-nQRstZ1CBLw17S05tplRGSRp8p_xXA6Digm_3-MMjzWYQm4ft346snerOChudEbI-6h27LAfZWOuDrV0YOLRqP4xJWMJx1A3BjFCmemRsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b93b2a590d.mp4?token=qQ5VZST70zXsDfrnRecFHMiCW2_ZxrzsubTNNk5u7Z0uEBn0ZoLS2uMIVTm7FZSXe46giMQKpPQX2hQE_Uzcvf3AOkgK9bn4AKCiJePNE977uLy22FR7dWkKyEBB1_8Nu-Cicim7sDkIz8uOf5wkP3g4WIuvzrKIdWtfAqFEqebNc0-xLtXzYhgAgmYXKC3oQ6G-nqlI0lXXQV7DfBwXs4bJiUg5R_lzqtl-jm-Mk3C-nQRstZ1CBLw17S05tplRGSRp8p_xXA6Digm_3-MMjzWYQm4ft346snerOChudEbI-6h27LAfZWOuDrV0YOLRqP4xJWMJx1A3BjFCmemRsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🏆
نصرت سر آشپز معروف تو حاشیه جام‌جهانی برا یامال نمایش راه انداخته
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/99583" target="_blank">📅 20:29 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99582">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SO9n0pLA-5er3QsEwMA7CIAOW8JTKCB-_VihKob4GE6LE8BwV6Uiq4c2wwS0cp0sNl447By2p6n69lquAsVQTImoVh4_cn77whw5Xh9wHnU3WPzwzkZ2fFdt2X-ic6K0glzG2YGZAh5EDwHB2gRPoEwY4MZsuLRv9Vu2DGVr_U18LFHpsZLAdwyGIK9XtVbe4xRZNDKq-r6AiKqWoRc_nOBBsFRqIACIVTUIISEsJaIIEGumcscqPnP-0DTgDnAeTcGUqPeTAH2Ne7tk2AHoM3iIVP4H6kjKzmnQnMlbFEQiha-HLQfxZmlo6TtF1HZgw09x3xQbhuCiS0QTK34vdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
هادی حبیبی‌نژاد ستاره چادرملو اردکان با رد پیشنهاد سپاهان به تراکتور تبریز پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/99582" target="_blank">📅 20:18 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99581">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rrq-v8HS8Bw9-kIH7Xyb96BEm6Le0WtCGHGUBQnAaL7axkCUqwOaDcBg9N6_eb_xWFyPn2p_xkl6hQbMpgGgH5dpxJDWnw7qOar4-eJaJLZZ3zPFUXhseWpTxK0BDfsyv02DO88zn9pPLNCRTW-82V2wLy8kkg2MA4zexJVZlg9VUKAmXA0NNWSyhj8VWvSiAlDpdr572JZOMGqsR6AYxTHB-Tk2zCcLCh3y4FgJbnTa26F5kigF7Ytc4pYuLPBI4b3n5rDO7jLQAtNyZclnRxs3VFzrvZjcqr5p42fOlFouzkmfWs46WRoxcuf6V7UzMyCGN73uH5-e-2T8dtxmVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟢
#فوووووری
؛ باشگاه الاهلی عربستان با ترینکائو بازیکن سابق بارسلونا به توافق نهایی رسید و رقم ۵۰ میلیون یورو به اسپورتینگ لیسبون پرداخت خواهد کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/99581" target="_blank">📅 20:17 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99580">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u5GM2g_ymB-GfMPqH9UotXJ0DuKf4dLOynCXuJBX_GZ9xaOHjt7sLQpbRLeMQKKLBkup7kwiMMbWEmAlqQXMIyL8ObdJrqirGSSJpYawCAdMKEziSRInbN06p1uRVkx6_OokalmbbbgWNi6bnZK8Tkeet5ecRfz0H5ML047ZExIUaTIeir7b7UMdlRNU5sJeh1uWlLe6lQVMv5mzkHWl51wE5OD9f5sz9jRE3GHpk7kLdketGl9XLE6WbMn-4GoELMXMmUzIKcaqrEjKrAn6giMAEo7Zi0_D3duPV_4qZg1q1HFkUK3kN_EHYw6n6QbIRje6usWbgmtNPnUl08afvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏆
🇳🇴
دیلی‌میل انگلیس: دلیل گرمای شدید در آمریکا، احتمال داره بازی امشب انگلیس و نروژ با تاخیر شروع بشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/99580" target="_blank">📅 20:04 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99579">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tC-0BeRDxQsqVjlyvHSuKqdiemkCK8B87RHvcq5Y1oieEQ4ARDuECrannarVx1DUSbleIkdLRcCl3VcG725Naef1VUWSVNSOyBABksP15J8DPc8wJ4hEIp6LT_BThAheWvuLOPIloKz1E7VHHUU4NEb-77p6qKrZCJQEy93-S0UfzoOOAUU9CPaqjtRdMlMuBGTOrQMhSgQ7rvBjZRULgoGwUHlhKZvftYXorjIRhpUNLqOrDde459qKbcDLifxwWUoFjjFVkXhVi4E6rYB_H_3fYkyO_eYZxo9LNcC65ni-DyoWbnB1B7ZRLPQmDNUSYHi7_ENZ-srnjWRAZwdYSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🤩
با اعلام باشگاه پرسپولیس، قرارداد امید عالیشاه با سرخپوشان به صورت توافقی فسخ شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/99579" target="_blank">📅 19:54 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99578">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SXk4t7JhzNYXbt6ptxZDynOyOUrV2U1IVSkTN5YiONed1dVbRFMWPAfDMsPfP8QvuotIrktCZXIVLz7yZPphmw9nCgDl6G3ZkkZfFv-thJetUKWPMHkTU4RkKT52qR8gQWC67O68Z-qjPiXobeS9AFaUqTEcv9S_0V12XXf0MziVmSbwz6JeCR4cewzg9s7NSsl0hlLsCZ5yMagA-I_dADKKbhdFyv71s4oANhpe30OQ6XZIsWLK1R1K3wYGqOQLrvJbxSunNYma1wugmgA609EdFGfdSPDwTR8D4Fgvpvix7iWxalSo46DMtqzvTdUXdE7_31Nphg3ADSIbVVpXIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🤩
با اعلام باشگاه پرسپولیس، قرارداد میلاد سرلک با سرخپوشان به صورت توافقی فسخ شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/99578" target="_blank">📅 19:53 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99577">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rl95RdFuZXLFZ4IT2sFY7whFroz3mxoSTRL_zdfvRn5iQk7nBqjUqQLbKjKy3XRJmCYlm9BZh0qk0ilJ1XAvwN2MRAMBaM4QIG7yr418gjmpimJjp-HCFsE_hyfqDeFb4kRmkPB5_sAqYM3CoDvE8GzdNDhzWZlvA6eNHwC1fXPRvTKjcxFIEAj_EjooUipktJANmXW1Ai5E1gy7Wi98-z6V2ZUZYPcZQUfjwAi7ktOwz-n7mXcq13nYFAzzAOxl0kCIWLnIFZ0ZnRWY0wHcSuwKf0R5nluY0RWqaR2n7W019HdSHKU2kBqLh6jIoZX0IAmcbpe8Og7UCh3SQV-_Vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
🔴
مدیریت بانک‌شهر بدنبال ایجاد تغییراتی در بدنه مدیریتی باشگاه پرسپولیس است و اگر اتفاق خاصی رخ ندهد احتمالا پیمان حدادی بزودی از مدیرعاملی سرخپوشان جدا خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/99577" target="_blank">📅 19:48 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99576">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tf_4qNKKyI9wcdAz30JBTGb6GhD0UaM0EiSAxxbxNjCdlEF0kIZEe1fmdU5-71GO7tEOWa1N6H_AR-e8eZnmUWVQFNje6JptEriqloflhppTYJORmAY_42TwneLu9wuoSnZfWcepbgTzC_xZER_e67KutkVSytqd6a92Dc8jUasn9egqT8VVi18675My49mCgrS-lE4WACPxNDUphWwjmhZ4IhMNgsHVkZ7Rc-cTxCr13LTg_igS4Vdq6Zx_HWgOS1igPTBeL6Q34IU14jP5np9uktXxD3GPK-RUmMPp4WnzKRWw8fi_4mpmwAR4ZhZF9W7Ul0OJ8dPfWvp2zDyjUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
تیم‌های ایرانی بدلیل احتمال از سرگیری جنگ از میزبانی در آسیا محروم شدند. عراق، تاجیکستان و قرقیزستان گزینه‌های میزبانی تراکتور و استقلال در آسیا هستند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/99576" target="_blank">📅 19:32 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99575">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏆
🇳🇴
دیلی‌میل انگلیس: دلیل گرمای شدید در آمریکا، احتمال داره بازی امشب انگلیس و نروژ با تاخیر شروع بشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/99575" target="_blank">📅 19:32 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99574">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vV9VQfrpxhTswVcMReKsWmeXgbfy_u3xJyXjsrltL9z_sogNAfHt5WUZVcwxWRO1AdEzBOamc6IsbRf2yUH1lk7mi5NDBpjkqRNWO8S8Jge9J_XWI9fBaoKB2uc2zJ4wgmWQXZ4R6OSjLldAghoIwKUpfI73KtriTza-i5_MePtJ94V7Box1kEnrCJG40FFq26hUbgHjvrZtp21TzUuHADgx4dLwD5MrNJ6wZMlYQeWFHpBcx2gy3NeTPADu_vCXQAuKrCZKAbwliBd8uFeiAkhoeCHGCMezOz_aKprY5Cea2qSDsbzX7vUSR05aLSmLrhZGI5EK4UxNkyUZgzZklw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حضور در برنامه ماهواره‌ای دردسرساز شد/ براساس شنیده‌ها برخورد با فیروز کریمی در دستور کار قرار گرفت
🔹
بر اساس اطلاعات رسیده به خبرنگار مهر یکی از نهادهای امنیتی برای حضور فیروز کریمی در  یکی از شبکه‌های ماهواره‌ای گردش کار قضایی برای برخورد با وی را تهیه کرده و در دست اقدام قرار داده است.
🔹
قبل از شروع جام جهانی نهادهای مربوط به برخی چهره‌ها تذکرات لازم مبنی بر ممنوعیت قطعی حضور در شبکه‌های ماهواره‌ای را داده بودند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/99574" target="_blank">📅 19:31 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99573">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rYwEa5OBSvh-nQGnzh9GyeVeDmkCpAbRD5H085VOz2XKSDG6fxLeOpWJ-FttRSYBA8aqF2OgdRruqPT5oWd5fCgc_WMHbjIR3iJ2s-HTrdev_JHNOPbxp7dFeyzH_SxSW9z-ntkotnAC-60TMei2ecq-0Uceuf1N-AtQeL4EAl7gZ2T6l7p6SZ8IpEGVjqKPxSE--7hOs-K0Yo3k5eTvlYg82fh3_hxG8lBD1q29wlX_PDrvsjHiZ-dgWx23OLlGxpwSUlkBkt79XAxMO46gYC2tkyJrUgqjaCB63U68wqdyFAyH29ecIgCyZ-4Eu27XwFitoQg4pKpZyBo_ft5QbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سوئیس هرگز آرژانتین را شکست نداده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/99573" target="_blank">📅 19:26 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99572">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E57KrMvk_j29yrWrTQXXrN8HamLMnmL2_ZSIBps3Vd2A_e9MoZCQqx9oIZqh-lYUv8-adyMm_pbQivVM4brwL15mH-_MjzGMJcVAlm63uZS4_x26PDPH4gpotoO4kHCbCxJlgzkv6tAC19_d5d9pKCCkrtN5aO8WkM9zjHG6-7KV3ZOemeyBJuvcJR3yeR9EnX1z4mGiHNaSfNsQ9jdYPTkDysPiuPyaYrc7OcWxPd319yATroz0oRi57JqcBVjy_tWmoFXmKsqppnsdjv0eHIbneyq_QZCUC-hpHO5TujudrFpj8CwlE0E3lQqTmhVgtlrOMx00vdUfe8BKLRg4xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💰
کیف 45 هزار دلاری هالند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/99572" target="_blank">📅 18:51 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99571">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bk8Ol5nn_ie-iTC1Qp5RteOYLsDa_aWNc2gkF5xa2TjgcF179zAWnxFzo1IP5CQdrWmTnBW_y-MvQCctntfGjGsOoJoy0ti_o4DE-AjfN_igA3E1-QYKSFXByLIUaqt0a4jdOY3lmo2ePBhvFJs-_PR4DmBVkLrCvyW2UyYBtAHU-i1G4S_ixosa8HT0tEp1AtpKjMsWRDR8UNl_GAS5zrR_bojSUvjjtTFmFIFs4MZjNQXFbXMoKFgnFv4cz-a5dYr4o8uVAnMoyzOnoZ4YZGwVHGahvxg6DD3VhCKcjWfIC1yF7crmaD_IXvQX90keM-VuhiIEway_Mi26NDhn8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇫🇷
میزان شرط ها روی تیم ملی فرانسه بشدت افزایش پیدا کرده و با اختلاف شانس اول قهرمانی محسوب میشن!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/99571" target="_blank">📅 18:45 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99570">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mVJKcWqEtekPYtpnp0HYgGMK5KzRVXqLvgNUC51N2XSX9K5OLq3d_yawF8Vlc4Z9jVcokYYbIQWDxEtJmiLPLu28Dlz4zuj6eCiKyjU82xtJIyo1a0B4pRjmkEBFwfmPYg155cKuc-k8qTp6GGCZaWlIjslvBtuDieqDYdvGsbZYzuzxDG4H2za7jDwPTlhwsCnGGxuqe94a7IqCCAnZ0g9n847MDU3ORYac5lAuJELaE3d8XK7t13lIp6JcJ7vl9G1b7eVlFsW5WMDDNsRXqBEil26jTETA-R4A2HhmrPVA2d5mDeW9Btp8clvZbKmKaz8ThAzu1Kv1VsanPsvXCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این آمار نشان‌دهنده میزان مشارکت هری کین کاپیتان تیم ملی انگلیس در ایجاد موقعیت‌های گلزنی و حرکاتش در زمین در طول مسابقات این تیم در این رقابت‌ها است.
👀
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/99570" target="_blank">📅 18:42 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99569">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y6j7Z3412I99Vd2p1YVILP1hdjJCxmjiYEdtIrSSRuIQrOQEWsMLgLKOh39I_UxtDSAMF8RDWIeYfhB-BEzVXsGSmYyVxpCV6DeE5VSwUDltuiQwIxop8YtZpHhzHSeCB2Ox0oTyEQkVVCmJOo-WWkycByBgvkxOjinJcPkFrFTmvQuAYx1dIlji3pFj5zUu19IXrBJNf1uG7RB4ZXj42wZB6KcttVFR5xpKUC5I9tN9jt5GUddJVsJdwtMe5QD5Zaoc2gpl-UBV5NEsgQqgaMhBrqv99-mnRejnkLfS3fe3TOKuaSVP37vvfI3w6VSfg7P9YXLhVqdLQaBx6Svuvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🎙
🗣
دومینیک سوبوسلای:
- من مطمئنم که ما توانایی رقابت را داریم و امیدوارم که با مربی جدید، آندونی ایراولا، در مسیر درستی قرار بگیریم.
🔥
✅
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/99569" target="_blank">📅 18:41 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99568">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NmV2GToeLw4unrSqfUz07d7T-EjSfX9GPcBuFx95wOdMWrfuUJRbVY2Iu9BzHiW4GsY2-gNgn0w3_-IRCz084Ar9UGGN9SpIm9D5YAAVPs9CMYiN8NIWkNRWlbgnrOaCw9kjNC0W3m8sbPSHHxKYF-SPRTgrJzitBCD6veaxChjy4DesblJuOb9kyvV-kJseBhJxhH90HhUqyFWNjxlxNEhY3Jpso5PoKnZrmZFsVpPA72zNSXI_MAKPu0EAhZioszEDcEgO-jtdfWMaLFHCVPJlzntrLy8nwudHfP2gteMAtGGIpbWp6TTv5-WkvJQzw9Ednci7uuLFTH4kIdJGSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
آمار لیونل مسی در مقابل تیم‌های اروپایی در مسابقات جام جهانی، در طول تمامی حضورهایش:
• [18] بازی.
• [9] گل.
• [6] پاس گل.
• [15] مشارکت (گل یا پاس گل).
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/99568" target="_blank">📅 17:55 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99567">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3ebd7973c.mp4?token=OGiTf2cm_WDMuOGix8r6aOS77hjvldoBNzXgNtVTzineR8V3tv-PczPNQb9PgeeHIPCEA_FbSaeB519NxuZ9HnZ3ZKBD8q6BT5KSReyFT1gbjn4QMVSNK7SvA2at-6n5nAKSATNuIGv4GmlNFmqZYKIAQeFUOJod0UkNg4Dnm8Qw4WxohKHs41iptZgM6DS55PUJJekTXq0cD6j7mAjxslxsT_o-6qULwvcBCDAp2mFAmbfvLPmS_wDamUS8KLcz1MARz7qYObTXZvJgtC8Khxf2-FgGwdgAoEdUUcshVMiP2NBPvLHkgmcwspKrypUDxUzFxgWpp1FVHTvdDNDMdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3ebd7973c.mp4?token=OGiTf2cm_WDMuOGix8r6aOS77hjvldoBNzXgNtVTzineR8V3tv-PczPNQb9PgeeHIPCEA_FbSaeB519NxuZ9HnZ3ZKBD8q6BT5KSReyFT1gbjn4QMVSNK7SvA2at-6n5nAKSATNuIGv4GmlNFmqZYKIAQeFUOJod0UkNg4Dnm8Qw4WxohKHs41iptZgM6DS55PUJJekTXq0cD6j7mAjxslxsT_o-6qULwvcBCDAp2mFAmbfvLPmS_wDamUS8KLcz1MARz7qYObTXZvJgtC8Khxf2-FgGwdgAoEdUUcshVMiP2NBPvLHkgmcwspKrypUDxUzFxgWpp1FVHTvdDNDMdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
محتوای خوابایی که میبینیم:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/99567" target="_blank">📅 17:24 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99566">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uO8foidMWrGdYoEK2dGDFGOCqD5n5EB0Qnp2XDC6HjVhuh3bvg_urIIILiCLNEsTWRhVcCYuI0TIsHv4GVS3zGV0Pjup_kqbxwVaEPqDnly6IWeyDNBZei3DqECcBsy8WYiTAAvDtYFYpui3p5cU4snoVzTmNuLaB-c9Lp_l9PWUiVpVXDKzZyK32rJbmQQLwG3TFGVJDOBz4wgosBEDalhgiuriIMz2qaKE8pmn_npjP6DxribxlksrV_2pcsknqc5ujKrg6WN-hITOyRt9zpq-VWePl8DxzU2eRzizO80Y7-Jfh4tJFrIq5w7b5EIYKlPlZvxb7xSJBV7_-KcnAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
⌛
| مقایسه باورنکردنی کریر رونالدو نازاریو و امباپه:
🔺
امباپه:
🔵
590 بازی
🔵
440 گل
🔵
183 پاس گل
🔻
رونالدو نازاریو:
🔴
598 بازی
🔴
392 گل
🔴
115 پاس گل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/99566" target="_blank">📅 17:14 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99565">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FAWn61dZTkOT1QxIaiOdbj82GR5Ld-EXxaTxU437Mco6-kPWi4m5mDE7JQOAaUJZCJKsooxbPtepcIypklv8DPMuWOeu5UOFemTQXNIFruMmPkV2dxnSJV-KuzXEWb7z0rtFW7WZ8K5ubOXRg-J9LbJXDL7uAeIVOvVp27fgZFhoRnGeU0hf7GM3R6Sa4Z_hdqjOBzMhqdOo6tjIMBIDfaattjPWyqUMKyBIALV92QEkBMnOchgLcBCZzIdV7fYSA8Ueh_kAXKT7pj2ZLSzUXWLrr-kuBurZzQGKkJ4D9O9DQ2DrmAY8mFHhV1iD4ak9JVoM1WZ5W8U2nAHfxwK6rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرینو وقتی میبینه تو تیم حریف یه اسطوره محبوب حضور داره که در صورت باخت باید از فوتبال خداحافظی کنه:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/99565" target="_blank">📅 17:00 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99564">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tRLneVlh8hNiwoX6vCWyaJVi0u91RHvd08orl5zAcYKWl6VkZFzoZaf0Y4XZ8K1_w-JBFWzRxXvz6AdInngSOwFrkexmo4Z9qUfDgyJOrjDgD2v9DkRo3Dc2DKzZaNb6SIPc13v2yutnw3UE6kONKbEkJueLVJUSfofbi7pCSuQPQ68wnpPl_FATVLTi_eu592tWth82iWxoocRYWRyaex40btauJ_7TTEnlFU79ua8H03d-6Ovn9qZDEVoPEo1-knhiX7FM5ggNkDmnCen4gCt6lgtSWt7RIZwRvqrOD-cYb-Vh0DxHgEP9O9mtdpS3go2PolTudubg_W2X1su-Rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖤
🚨
🇿🇦
جیدن آدامز در ۲۵ سالگی درگذشت
جیدن آدامز، هافبک ۲۵ ساله تیم ملی آفریقای جنوبی و باشگاه ماملودی سان‌داونز، تنها چند هفته پس از حضور در جام جهانی ۲۰۲۶، درگذشت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/99564" target="_blank">📅 16:51 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99563">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8bbdc557e5.mp4?token=Nl630VfpQunY9__QnuBVxb7eBHTFHHFE5DWfMJhSiJDHZUbH13kQhZQc9HVYkg8qqk7zaIMULs3DRcCFygJzCJZmMTbrA-mQICYaffmXPT4U1veJjolPdVs8Ktz983kGdUnza7qj7RnbvBqUJEDn5rSoEzEgZAgW0pHculLB2zHn7luYSgQkCgdogfMD3w2krRvsVLndfDBkU6t_l8EWhCzPivbwiN_VDFMsYdHH2cUF6nKZBDtorr4CnpAfgiQpK_Mzg13IGgbNsaa71uZaVDB7h-Kt4DM9dpdzkcYHZ7qhArdPHUslFyO1Pry106WuGIqJRaiHYh0LXZo4lFMcKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8bbdc557e5.mp4?token=Nl630VfpQunY9__QnuBVxb7eBHTFHHFE5DWfMJhSiJDHZUbH13kQhZQc9HVYkg8qqk7zaIMULs3DRcCFygJzCJZmMTbrA-mQICYaffmXPT4U1veJjolPdVs8Ktz983kGdUnza7qj7RnbvBqUJEDn5rSoEzEgZAgW0pHculLB2zHn7luYSgQkCgdogfMD3w2krRvsVLndfDBkU6t_l8EWhCzPivbwiN_VDFMsYdHH2cUF6nKZBDtorr4CnpAfgiQpK_Mzg13IGgbNsaa71uZaVDB7h-Kt4DM9dpdzkcYHZ7qhArdPHUslFyO1Pry106WuGIqJRaiHYh0LXZo4lFMcKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
کمپینی که مصریا برای سوزوندن پیراهن مسی راه انداختن؛ اینا بهتره یه شاخه گل بگیرن با خودشون آشتی کنن
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/99563" target="_blank">📅 16:51 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99562">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/308efbcab6.mp4?token=uk1qRHYXg8xDVtfeMfCGtEM9dX8alo_Oj4dZK8aha--tK-R__iGQlX61QjiBjohwVF2U8YP33yP2Cw1ffzGe4acZ-CQ1dgGbFS86DqexAX40ykXP4sjJAbltHY4puKwI58xlwa-x-4JUhg128Y4zNOwI_aIWry7Awe50jApbwobApQn3r2t_SNuvxa-jOZdb5vAPSR4fNMkGxK_yJbiiMUJ0apNUyAn0fd_JKL1bA7Ai0EmSuDRVSliaeGlFkA4vdG-R_IvQutSKQ_Ik0RAIz22jnCys0BEGR888dJzFW2pE56ioARCdNmtwmQCSJJKZA1RP1yd8N3wyzqZbtrv_aQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/308efbcab6.mp4?token=uk1qRHYXg8xDVtfeMfCGtEM9dX8alo_Oj4dZK8aha--tK-R__iGQlX61QjiBjohwVF2U8YP33yP2Cw1ffzGe4acZ-CQ1dgGbFS86DqexAX40ykXP4sjJAbltHY4puKwI58xlwa-x-4JUhg128Y4zNOwI_aIWry7Awe50jApbwobApQn3r2t_SNuvxa-jOZdb5vAPSR4fNMkGxK_yJbiiMUJ0apNUyAn0fd_JKL1bA7Ai0EmSuDRVSliaeGlFkA4vdG-R_IvQutSKQ_Ik0RAIz22jnCys0BEGR888dJzFW2pE56ioARCdNmtwmQCSJJKZA1RP1yd8N3wyzqZbtrv_aQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🎙
انتقاد تند رضا جاودانی از صحبت‌های محمد حسین میثاقی: حرفه‌هایش به فاجعه بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/99562" target="_blank">📅 16:40 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99561">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/411cd56909.mp4?token=pul7SFEcjH2yfSQHUFU4Tb1sXqUA2hcZ1Jk9mJsfoFzbDSi_pAx3bHE9kVnMFijPvMiLOZIOCmaiPzJlsLw0wlLm4LHeH4TJbPIJ7UcGydBGXBEMts_KldKhqWe7b3noUNfDZ2cu51xx18FSN9WWg1RZ25iZAIdxt_JaXPsTi7k2K9gA-dhI3N-jXErMUrXnL9rj7Kkez73PGlLKMgrDhKseCDJOp-hgHAGiZrF_rlXzesnKCqnLIGrnSkQCPvu430F8z7F713gdxJ4qAoq4SXoExD6kpUOGAA-CjBZt_o09HfaEKjxY_3u-bxoZlE4fmCdUgRaFTdzbTIXxSDeKn4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/411cd56909.mp4?token=pul7SFEcjH2yfSQHUFU4Tb1sXqUA2hcZ1Jk9mJsfoFzbDSi_pAx3bHE9kVnMFijPvMiLOZIOCmaiPzJlsLw0wlLm4LHeH4TJbPIJ7UcGydBGXBEMts_KldKhqWe7b3noUNfDZ2cu51xx18FSN9WWg1RZ25iZAIdxt_JaXPsTi7k2K9gA-dhI3N-jXErMUrXnL9rj7Kkez73PGlLKMgrDhKseCDJOp-hgHAGiZrF_rlXzesnKCqnLIGrnSkQCPvu430F8z7F713gdxJ4qAoq4SXoExD6kpUOGAA-CjBZt_o09HfaEKjxY_3u-bxoZlE4fmCdUgRaFTdzbTIXxSDeKn4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🛂
سیستم VAR در مسابقات محلات شمال کشور
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/99561" target="_blank">📅 16:20 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99560">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CTZsxPXlrFNaUkbRo-MOmFhaNQ7bW9KzlZNTfDYR6t8O0r3Kh1jahLKWa7WOJBcFCUPYd3qOormvr985loRTrD6KtClwkazWhxQlbBM9-EOkEYXlbL0CGnGxxSaK41LVFBful1pnhV8sePLg9gyFx1htNtqxTTT2u2x62UdtrzFXmtU3535X24O-j-1CFiqhEIM5pcSKgq29GfzQajV9d_hPzi7I2QCqCrK6qTcQyOCl0s8tEOKrRla7kDF-UMsWs4yLVe_UQVys8Yv0qDm5zqLsb4xp-MHxOpuplXqrHzqqzUF46P7M4OOZTd2T2i-Mwkg2RETzkyF6sXXvk7zfbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">+ ترجیح مردم کشور های مختلف در بازی امشب :
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/99560" target="_blank">📅 16:14 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99559">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f2fbd5dd7b.mp4?token=EQqgGHKbqh7C6pxazj4aCjm648n7aPH2vk6gxUyKUvn4-mBWeVZvIaGiSTbzgZfGe0SUk2JxBFsxIJhDusuQOd8DgDlZkUp80VRJAMz4q8gisPDW6PFPFZ1qNhoRkA5Qw3xPsPIdBSnODYwO1Xh1Daf6gGfCkEtJD1GWnDiNTItcSsIG35hyudvVw3yECVrKtLv2xvOoCdaEqrqTMWl2uOKVNpnB5Wdho6eadvBu01yF8ezVjydLo8BYduuMCin5JQJW6xtiKR958fA-GmJQYgSH9yUkGS6TR2mvv-MvGJByb46syeC1eyTt_0mt5jh-nQtqtnGPUi2kEqrKtdFvwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f2fbd5dd7b.mp4?token=EQqgGHKbqh7C6pxazj4aCjm648n7aPH2vk6gxUyKUvn4-mBWeVZvIaGiSTbzgZfGe0SUk2JxBFsxIJhDusuQOd8DgDlZkUp80VRJAMz4q8gisPDW6PFPFZ1qNhoRkA5Qw3xPsPIdBSnODYwO1Xh1Daf6gGfCkEtJD1GWnDiNTItcSsIG35hyudvVw3yECVrKtLv2xvOoCdaEqrqTMWl2uOKVNpnB5Wdho6eadvBu01yF8ezVjydLo8BYduuMCin5JQJW6xtiKR958fA-GmJQYgSH9yUkGS6TR2mvv-MvGJByb46syeC1eyTt_0mt5jh-nQtqtnGPUi2kEqrKtdFvwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
💥
مرینو کلا آخرین رقص و آخرین شانس و این چیزا حالیش نیستا.
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/99559" target="_blank">📅 16:05 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99558">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h1Aaw9qOI5VgaPqZOlPyLfS5FW3HCu2wS27EKdm9SdcPy8ePwogAtWbJKunrZRxvKtMJEjCu6yo3AqbQfT2FsuHMpEZQ16q0KPFwFtu_Uph0k5NoAgE-j8Vw7t1KureJAbchdScLOJNKYNxyPpjzOcp9TwyjxbCse2aV1cFZlIdBDy5EhA20Cp4sDFQ23wgBrKAA2MhWpAUcI5seEARBDBCMC8pJBS_OjY8-YZ4nSxIXPqADwWrH7i8yeQGhd574qJ1QvuwzgRgC1xLspJN3-iP_ki-8QJ704QUBelzCs6edyHaRDRGrbFbIEpBT80XlFzHaSYPhKu_hFOQWr40x3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🇫🇷
سن خط‌حمله فرانسه در دو جام‌جهانی آینده جوری هست که به راحتی میتونن کنار هم بازی کنند!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/99558" target="_blank">📅 15:40 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99557">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c84faa7ffb.mp4?token=njd1oCoVmQpzHjBXSup6vuNXbS_qWsLBEYVA0qzM9rfv6-2faDyvsUvKVa-nb_OSciVbhGqOhZ8QRL0ueusmDdzf8FoSIBx_4jecDJurkNqIZjQMjHinquAy2nvMGtb-EB7S63q9VO7uChBUdS0YwQKLu0CU3UWKfpQJCDVzJMHFlkO3jWnWt4dHZF0IeKK7fOGnz2Ko0ZWgr6w7jwXkiEf0BuUYiRZ9TIeTlDdOqgzxIfZctjusnrXKVTXe66LP_cfQFR5Pq1YvmrhnbWpQOshk4t_OpWjkMP4OeAuKcLysYmTrSrsvP7tMR3eF6zHjUF8zAqnKBQFCNutiKejs1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c84faa7ffb.mp4?token=njd1oCoVmQpzHjBXSup6vuNXbS_qWsLBEYVA0qzM9rfv6-2faDyvsUvKVa-nb_OSciVbhGqOhZ8QRL0ueusmDdzf8FoSIBx_4jecDJurkNqIZjQMjHinquAy2nvMGtb-EB7S63q9VO7uChBUdS0YwQKLu0CU3UWKfpQJCDVzJMHFlkO3jWnWt4dHZF0IeKK7fOGnz2Ko0ZWgr6w7jwXkiEf0BuUYiRZ9TIeTlDdOqgzxIfZctjusnrXKVTXe66LP_cfQFR5Pq1YvmrhnbWpQOshk4t_OpWjkMP4OeAuKcLysYmTrSrsvP7tMR3eF6zHjUF8zAqnKBQFCNutiKejs1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خبرگزاری مهر خبر داده که برای فیروز کریمی به دلیل حضور در شبکه ماهواره ای جم توسط نهادهای امنیتی پرونده قضایی تشکیل شده
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/99557" target="_blank">📅 15:35 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99556">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c2e8d837a.mp4?token=lFFwICpqVJBn3KyMdRpvxjH1Au6Xo7HbEaaDywtrdmusnX-4v4KMp-WaeJs-iIVAfOUwtaR1Q8G8XX_31Q6eOAyQw8c-Llm935AcP748U58lCMosmIdwHjUqf45S5PB58oRR-vaCE2YSATlkhuX__dQMxX9GMWLNnfYYu1SeGX44stg_GWEDhjN73PvEJijrrPbZu1JbvO-0diYX5FBJgWgf84YgH2X0mAq1G-V-wDDThQMJI90YlEUxQJ5xq2ckWW_pqlUeXF8g0ENL7SMXA3ul13zMWVP7Va30nExBRHKn0QOz2KrWcRH8yC7620q5QH-6x3RpKbMjXfTbOOvlLJyA0ojgEyZhiSaGC2ZpNhx_1psSvVw7R1KeS3DZjGapRmz2djAm2P2N6opK-vyT0M9hVjfBsFViGSRyM2rbA4bQZAY0-NGNQrvzJGaCYNaM0MmrpamYQG6feRJbcUxz5DgO-dS-kv0-Cvdamte3AUWbJhIkLM-xFL71GQYYDbSwIgedMCeBPJLTPBudoMONtNcizcrg4ExK56WKZ5UwYwLks-5lGf-b_cbWZBcA4eTQlkEj9iOYRIG7GBWT3zY60t-RyQZdLexXJ7vL-96rEIHBl64zD_yEYsYgSL9PQh_eiDkZHYQnaG2lnnqD2QoaDvPlmXvI3H2bzI6IHnH31CY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c2e8d837a.mp4?token=lFFwICpqVJBn3KyMdRpvxjH1Au6Xo7HbEaaDywtrdmusnX-4v4KMp-WaeJs-iIVAfOUwtaR1Q8G8XX_31Q6eOAyQw8c-Llm935AcP748U58lCMosmIdwHjUqf45S5PB58oRR-vaCE2YSATlkhuX__dQMxX9GMWLNnfYYu1SeGX44stg_GWEDhjN73PvEJijrrPbZu1JbvO-0diYX5FBJgWgf84YgH2X0mAq1G-V-wDDThQMJI90YlEUxQJ5xq2ckWW_pqlUeXF8g0ENL7SMXA3ul13zMWVP7Va30nExBRHKn0QOz2KrWcRH8yC7620q5QH-6x3RpKbMjXfTbOOvlLJyA0ojgEyZhiSaGC2ZpNhx_1psSvVw7R1KeS3DZjGapRmz2djAm2P2N6opK-vyT0M9hVjfBsFViGSRyM2rbA4bQZAY0-NGNQrvzJGaCYNaM0MmrpamYQG6feRJbcUxz5DgO-dS-kv0-Cvdamte3AUWbJhIkLM-xFL71GQYYDbSwIgedMCeBPJLTPBudoMONtNcizcrg4ExK56WKZ5UwYwLks-5lGf-b_cbWZBcA4eTQlkEj9iOYRIG7GBWT3zY60t-RyQZdLexXJ7vL-96rEIHBl64zD_yEYsYgSL9PQh_eiDkZHYQnaG2lnnqD2QoaDvPlmXvI3H2bzI6IHnH31CY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤣
🤣
لحظاتی با داداش بامزه لامین‌یامال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/99556" target="_blank">📅 15:20 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99555">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a53021254.mp4?token=W3nmTBEacSNHfYYcuas7cdc3y60b3Ctq8SGkPy8_uI6_Z4hl5yh2ldOutJ65TeW5IxOM4ukKgWTqVE-Yte7j8qk5v4woZuOnfLhOLY-c2q94KGtJB_5v8L86mR8yOz0a9wKZGBrK74Ts2D1olh6lQF9uL4FvJxInFS0T5pnPuWmob8ke1oGxyAkjF5JjdX3_Ds2sZofz6x6xib-DfgivqZvxc00yrHTHWdfJojTwhOyfwRUtzmNGDOJr_58GMg2WZZMVw4ik4hv8edJPwBOE64JEJY4bUFArdsVIpf39FciDv_tIwYO-fLydW8aX65bUTyEscr0-xIoqotP2WZwjtJEPevwWgpPNGVtky5zBjItJIaIIOcXk4J3gHdhnyVN1rsQgLyMrH0MtoRvnlfYVmYmUdk-EtTuJTpDy0w7HPLrNbSgtNx804eBaRxjo1vHHmqkxNJy9UEsCN0nx3nalTo-pMrU6jOvRYf6uk3p6BUxbAd3Pdeo2hckDuxs-UJoviX7BSP9q959lUW075O6HzgarCMDJurGUxXKJ5nkU25a2GltCCD0-nD1alWasBDx_OwDnmb2-m5MqoYJH8fjMVmkeb8zDtDsqd3C7MGMHQL4jj1QXd_jnYdZEMVbxekJfqb4BPFKqbH118_I47VIx3D0Z2WTeURL7dpt86mHkZ2Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a53021254.mp4?token=W3nmTBEacSNHfYYcuas7cdc3y60b3Ctq8SGkPy8_uI6_Z4hl5yh2ldOutJ65TeW5IxOM4ukKgWTqVE-Yte7j8qk5v4woZuOnfLhOLY-c2q94KGtJB_5v8L86mR8yOz0a9wKZGBrK74Ts2D1olh6lQF9uL4FvJxInFS0T5pnPuWmob8ke1oGxyAkjF5JjdX3_Ds2sZofz6x6xib-DfgivqZvxc00yrHTHWdfJojTwhOyfwRUtzmNGDOJr_58GMg2WZZMVw4ik4hv8edJPwBOE64JEJY4bUFArdsVIpf39FciDv_tIwYO-fLydW8aX65bUTyEscr0-xIoqotP2WZwjtJEPevwWgpPNGVtky5zBjItJIaIIOcXk4J3gHdhnyVN1rsQgLyMrH0MtoRvnlfYVmYmUdk-EtTuJTpDy0w7HPLrNbSgtNx804eBaRxjo1vHHmqkxNJy9UEsCN0nx3nalTo-pMrU6jOvRYf6uk3p6BUxbAd3Pdeo2hckDuxs-UJoviX7BSP9q959lUW075O6HzgarCMDJurGUxXKJ5nkU25a2GltCCD0-nD1alWasBDx_OwDnmb2-m5MqoYJH8fjMVmkeb8zDtDsqd3C7MGMHQL4jj1QXd_jnYdZEMVbxekJfqb4BPFKqbH118_I47VIx3D0Z2WTeURL7dpt86mHkZ2Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
امیرمهدی ژوله: هوادار فوتبال و شور و حال آن را کاملاً درک می‌کنم / حرف من درباره فردوسی پور این بود که ماه نحوه شادی کردن را بلد نیستیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/99555" target="_blank">📅 15:02 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99554">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CGDaopJSND9x82QMpOq_dyDNkKRTc2a5BD45P2WTdbtE7IpjCRqhpD9Z5m4DA4MaLaE23dljKkZ9s2G2gZ-oKurCSBZMa9dH-4gMszb73Ldy7CmJJl--vH3rCtlVKsotRHu_pQJpXFVp29CUmPg4-C0k5e-KI-74DcXPfcWkm9v2i-GOv6ITZ0OvJ85ZEPU1O8IvJZ-BhUsxlkanznZUzf1hCPclSVqJe2JoFPwixqbgdZWZQ4VKy4YMctPwdrIDaZ4ocUDdPBA9gHR1-4nT-UFztJ2PvaKzHgZFmG6CXtUJzu4ltQr0WVgNMQQREwylOzTCCm1rVGm24zchVs1rRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
تیبو کورتوا:
برنده بازی اسپانیا-فرانسه بدون هیچ شکی قهرمان جام جهانی میشه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/99554" target="_blank">📅 14:42 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99553">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/735c75025b.mp4?token=RJ5hCY-J4MUR3nlqY8Ub4-tFdP5g6Ol_mc557I1Kdo52n5zxm-y7HWfm3Fk-3R75PVO4u8_XsgoreMQc79rO2kwh3oG4KnHZa9PES5iIe71yTA1zwerrcKEup_PNtGHVPzwoj4zCuSfi0sWhF3dMhoKxS4AtS1Uu43ZQITS5QOsIYD_y0w1ZXS_q2GorX4EzMMPYtuY2cD3E0rBogW1swhxqO55hJhM5zNafQVoqlnFVeCw7ziwBO_2bBsTr3j8HpyP8QvPjlmkqPwREjOuzphMKAwzWZs5fkDNkYMYdA40EClbF5vM6F5WV1YkGqO4ATY9tdsHxN97GYMNZEvVhIEuUz1E3niXIfBBRypIjy8wfjJF88ngn0J74WgmBAoFe0W4ylMMXELp9eR37WGPm-wlHxKxG0aBtN-VLUKR2uiBxpSV9sGk6WchmU39JtCIVIoXRKbQgmRggxeI-_zyM55dPhuEVnqoropduZXM67lBHE163332uqZxPC7j_ziV_lxA0aVKFh4dKEa9s1uMZw51Ox8eEq_al2OAMQN3-2GpOCtTgmHfGw_3f3mUPNkiE1eVz31n-BA7G8gcyHeNm05qDP9kT4u0-2W3LwAvEPzOhT_i8gY3TLZdXlRXzS7ufSd5RFak_P7bs5ufFChcx5b7jvRAevANMubBZ5DKqdEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/735c75025b.mp4?token=RJ5hCY-J4MUR3nlqY8Ub4-tFdP5g6Ol_mc557I1Kdo52n5zxm-y7HWfm3Fk-3R75PVO4u8_XsgoreMQc79rO2kwh3oG4KnHZa9PES5iIe71yTA1zwerrcKEup_PNtGHVPzwoj4zCuSfi0sWhF3dMhoKxS4AtS1Uu43ZQITS5QOsIYD_y0w1ZXS_q2GorX4EzMMPYtuY2cD3E0rBogW1swhxqO55hJhM5zNafQVoqlnFVeCw7ziwBO_2bBsTr3j8HpyP8QvPjlmkqPwREjOuzphMKAwzWZs5fkDNkYMYdA40EClbF5vM6F5WV1YkGqO4ATY9tdsHxN97GYMNZEvVhIEuUz1E3niXIfBBRypIjy8wfjJF88ngn0J74WgmBAoFe0W4ylMMXELp9eR37WGPm-wlHxKxG0aBtN-VLUKR2uiBxpSV9sGk6WchmU39JtCIVIoXRKbQgmRggxeI-_zyM55dPhuEVnqoropduZXM67lBHE163332uqZxPC7j_ziV_lxA0aVKFh4dKEa9s1uMZw51Ox8eEq_al2OAMQN3-2GpOCtTgmHfGw_3f3mUPNkiE1eVz31n-BA7G8gcyHeNm05qDP9kT4u0-2W3LwAvEPzOhT_i8gY3TLZdXlRXzS7ufSd5RFak_P7bs5ufFChcx5b7jvRAevANMubBZ5DKqdEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
▶️
افشاگری رضا جاودانی مجری سابق مردان آهنین از پشت‌پرده این مسابقات
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/99553" target="_blank">📅 14:40 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99552">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e8uDUt4o45ksIOf71vwSMFK3N-_xar7_2O3f3wlbD0FMkverLqdKBWexBr7V_2LnZGKzkdBvoxPr5EZFT7xs4PWA-bJmGrW4l6bwmYvyAkJTPJpmbJQo0u93RT9PVUaAxZBex1E2CqGrXmGWtsCaXcCixt7Tr8ymPDre8iIh-WiFJt4W6JN6T6WlPpfLUsGxqWyKhAFYuZ5ZKmkCAWg_yQI6j26V159GStMBEVxcFJY5vF2lEGLOkx32X-j1rDpLnRMZBfjy7aaWEDJ8PRgLR97gmci9ctKbWqRxR2D97ueaV5iV_g8SRpus-MoRF297IEo2TByzS_5v0SB11tIKOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
🇮🇳
اسپید:
هند به کمک نیاز داره! اگه این هندی‌ها واقعا دوست دارن تو جام جهانی 2030 حاضر باشن فقط یک راه حل داره اونم اینکه من رو جذب کنن تا واسشون بازی کنم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/99552" target="_blank">📅 14:40 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99551">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YnLC4ORVAm5aTV6bXi5rZXb73Dz8saHUkWLf0vKw7_6iV1U4ZtWGfd7TEZamAHcD1dQI-ai72tGW5qgE0wq0OlYvIfTCEYAJr3ex6Y22aTAA3ZzdKaCDo8_SdWZNdPL_vu8O1GY0rX0TiY-H4X2IMVcGqHesW-TF8f9RKuJZN5ZrbTuo7Nf4d9LWRx7ApLcLVJCmjxdIBO36Np6KyIMMPqL_4groVnPqSfNzsR9dSm0RI8gpbC4F3Hpjw-4oyPecwoA-qD5LEe9CrNtjuhVh2VnUPfmhpZOt05_wSsOnnxGv88_ZyFYnQ3AWecBVdXqPqmYu-MJVoUmBgjvoaQK0VA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
خوزه فلیکس دیاز: رئال‌مادرید و وینیسیوس تقریبا به این نقطه اشتراک رسیده‌اند که تمدید قرارداد بزودی حاصل می‌شود و ستاره برزیلی ستون اصلی پروژه بازسازی رئال‌مادرید خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/99551" target="_blank">📅 14:30 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99549">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/734fedf32f.mp4?token=ZedJ_vxL7q8fVUV_9uHgt6Cg6Plc3iiY7uerqHS8XHUxSGZteK8yQdT7KijRN7F84hDOWD--qlaujpZ-ch-uXkJt5nX81cpk4nb7bl7DNvE83l7dfQb3lcILsvJYIWpqlasmaKjz6c-YeO7GDFIqm2ETjUEWj6yfD27hTDRCQ4OKAScg9i_WOjvAVh2eMU1YsMboT1Yk68AV-EMpiRcGFV31FubnIntQVcx86KtHieOWysT4QcAFePy4Bmmxqcotod368IC81bLNp1TUCO3MgcVQE4dsb4AmQzjjPkOiSg605bxQA0QxbVqaHHn0Td6rTGZRdNhMp_syMdUdbQz4VA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/734fedf32f.mp4?token=ZedJ_vxL7q8fVUV_9uHgt6Cg6Plc3iiY7uerqHS8XHUxSGZteK8yQdT7KijRN7F84hDOWD--qlaujpZ-ch-uXkJt5nX81cpk4nb7bl7DNvE83l7dfQb3lcILsvJYIWpqlasmaKjz6c-YeO7GDFIqm2ETjUEWj6yfD27hTDRCQ4OKAScg9i_WOjvAVh2eMU1YsMboT1Yk68AV-EMpiRcGFV31FubnIntQVcx86KtHieOWysT4QcAFePy4Bmmxqcotod368IC81bLNp1TUCO3MgcVQE4dsb4AmQzjjPkOiSg605bxQA0QxbVqaHHn0Td6rTGZRdNhMp_syMdUdbQz4VA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😁
چه اطلاعات مفیدی مهدی‌رحمتی بهمون داد
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/99549" target="_blank">📅 14:20 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99548">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c8suwO8oHF9JMEO3JF7m-I3daiK7ccUmlVncxiIhRKxlWlWrSvBfk3sd-VhcVx3fBW4LSzGazhxDgoy8IairVAhE29c2Ho-8_pPRN7MW89R0A7XQY_Ka4TSxKlMAA8JZNbphebFWDuX4L5l7YEhMzRTcU6GqSUmgFgMRXFqmpeNmQ4DOefxnGOLY8gxQUAY6GuOJbc-MiRnol65JpxsDMbRmxPd3msacDAY8Ci9haMe-O29KOszLtqN5g_DIZCH46-sVyxd914n45D_Jdz8QHQb39AbHj0JGT1m8qZ1nCYumBvi27LZ33bvUIxjamdLBaF8NZoQWl_tSKWbgxzI9fA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
خوزه فلیکس دیاز: رئال‌مادرید و وینیسیوس تقریبا به این نقطه اشتراک رسیده‌اند که تمدید قرارداد بزودی حاصل می‌شود و ستاره برزیلی ستون اصلی پروژه بازسازی رئال‌مادرید خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/99548" target="_blank">📅 14:13 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99547">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UHGYj2hIS9A1E1JkYwn0I-0C2cKmGK-wzgdcZVvvxNJ2DVwrYy9duAC3fub0UBvnhW9kxlijq7ctm1kCdxX8hdBDQRceJmpHxPw4uMOeF9ws0rulNhxYNwWtB6rYRpUbaRjUE_Wi0c_N4GIMpOSmXpcZ4R6CwiMwGnqGUuMUYpNIr1muzh1TrzGn-_it_uZaKahOUi3G5tZD8AGwQ_0-NDSe8wateAmp2W02g53zsgYNgHSGkGOX85Om-hK2qZrBeAaMmxKdhJz0Hm-C-YIXU557y3TIXtPYEX2tT6cu_ul7k8tFE7xu1eQ8ilTJ1PR8bq9aEkWr8YoitPdhOQGRHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
‏فابریزیو رومانو:
🔵
بارسلونا آماده ارائه یک پیشنهاد جدید به کلوب‌بروژ برای جذب جسی بیسیو، وینگر 18 ساله با استعداد بلژیکی است.
✅
بیسیو با انتقال به بارسلونا موافقت کرده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/99547" target="_blank">📅 14:01 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99546">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rhRR7pWYSRaESI3I7oZ39zy2tuEu2gXehuhLRTf-v7OpQP4_O2e45nfOxqzRawlLtxp5d3hE8N2mM2mGa6Do2g8fPcZShDAWa5quh9P94ecZKGDuuFjyxdtndpH-gUFbKhhUduw-GfJand-F1QHYDK6T0kG3w8CxwES2tMimO25PMdsvd9ynroLHcMXRxprrnGkp3SiAAcRDw0MOJodRycFE3ZAo0irPPHuRdQl-RSrjom6LUqdet2rAVPBMbq0wiZVC0SqsoEUA3Jemrn5CqAl_-P0ekjw_YJ2_Nz1PD9znxtRyZ9dFWFpKRt-LNj5ZzlhA3zl6qjWPnIoF5hsgIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میکل مرینو اولین بازیکن تاریخ جام جهانی است که در دو بازی حذفی مختلف به عنوان بازیکن تعویضی گل پیروزی را به ثمر میرساند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/99546" target="_blank">📅 13:59 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99545">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JTGzmZON9mSou5dsamEcYLDsNcWn_mGGks33J3DQ0bG-WBy0-wwZJRSFDeWaZVmecsfe03ZKxC-n6tQ3g5m1FlqJ7gbL79LkXvDAgjPAzLcO5UJS2qChPGhBQZ3jKlFc8vTRaW1CPLAj_G43rsaebolB9cJXuLQatPqixar6qOQGtALZZnq0ApxzBNuGARiY1-Vcxt4DbE6wU8YeAeJ_u8R6c3tR8SKPGn2Qt5QGNC8_Bpajd34AEqOOSq7ppFQeHn_oksaYvD7zAAXKOG6e1Mt3XfHzVVYVyPHhr1mQKIm3Mahj6rDUFJVwGJQjGhckeDtG8PPeJITDLcLhYw27zQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
شانس صعود انگلیس و نروژ از نگاه اوپتا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/99545" target="_blank">📅 13:50 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99544">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tyVteCPAaxv0AT35NkMKLQphED9ku0ySwjt2VRxZztgSvUk3Gvf9Ih6mdGoc0Kp_QXHoHRDP4qvWCXzVmpQ2vAoGAKrZMKnO9uZanFjfZhuf2ZrVDksc25Ak19Ah4ESONoHVnLV_h1LjY5v2ECi_tw-EAGl2CefOC977QbCVfWyOoGljeghgT6qrrHyCfADpMv3n1vubWbl3kMbdeqQtrTzIzMGMC2nAvZBLcFT0XyGXUkbklZz--whq-0D8PlrPGW2kHgtEjrI8c1ofnZCclZsyPDOGPCjBsJvLH-l1FUqN1EsL_D-6G1WTyjtrd1vywyJS_92G0t0bhRVVT_3TFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تنها کشور آفریقایی که از جام‌جهانی حذف نشده:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/99544" target="_blank">📅 13:50 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99543">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/geAypdLSJqUl_y9UNMh44O_xgnMbiwIWz6sc1WJPuHjw7fOtEHKreW_dtBb23Jg74NQpcbS161klAgvnT9gu0-TRFsoIgyCcM60CeA1af7994yxnD4ndTtuFzJnpA_8cZ0R3GSIEzMPeHZQxYWNpAvyclo0al82uzhTipJX_gPAMw2cdnBd0iTSq-UP6XWcv041WJyyX2xw0A-0TWgG7frYxtGRokeHcCLkgca2N6hL24hBpmmqHEjyL4Iu3Ixb0VwuvEOqXAg2LCJPBFpxonOZb8q3LDFvGZ3pJHpupVlN5YMq_sU7a-upw__zMzBJjRUgRKkNlMTLDkg82lRbPKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
📊
| رودری، بیشترین تعداد پاس موفق رو در یک‌سوم دفاعی حریفان در طول جام جهانی 2026 داشته است.
⌛
از 180 پاس، 170 پاس او موفق بوده است. همچنین، او بهترین درصد دقت پاس را در بین تمام هافبک‌هایی که 100 پاس یا بیشتر انجام داده‌اند، با نرخ 93.41٪ داراست.
‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/99543" target="_blank">📅 13:44 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99542">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a9-F3g8Ls4TBP5bAMd92vg5ZqXV8bMkMVhfJvxq5FVdr88lCxVhk0VCCNpXON85l8pZi0jX52beMppkZWS2u7dAgA85WGWcKZxkjDWX_vw4RVfqbTFNdOq2MMKGs2jwjCEGgwhOsV-evAxJjRliQfAvoN2g7c8xemSxv45dWy-CLQ9zqKtQvZ0uUBPU0kgx50CT4cXnoTR5Ry7U4xVaRPH4oTyqvCsANR-QGqeAcosvmQ7TdPNoZETDlby7VLYoAjr6iFk44gjw50aPNAaWaWY3zPUITGxvNne6ia6QO_WEzusS_rTL2RGhxACWp6nfji7f81nbkniC7nvnRCpVsCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینا دیگه چیه برا هالند میسازن
🤣
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/99542" target="_blank">📅 13:43 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99541">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآپارات اسپرت | AparatSport</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TwAAPinp5fzaOL9qQ0g8B9B7VHd-TcnahUzkTpLIJcdzBnBHRMejQO9poTX36OfM_AhJf5D1t10PrQACW8HGw0yVmHTwePOq1navI0C7qR-O6pnadFsl8tmPTPPqQR7V1paOzy4FFsbKNbK8za7VHE0LY3b_7QU1ecmvumjHZn4lwq9ZAiPa_VDEM-eTCQgmTwt3G4RON6-oyTCd29Kytrd4Fn68ZaFXHQgd8-DVRYp6BWMwA-6cBr9Ibw7yr6RwpXZr52oBggiqhOeJqt-vyiAJF3hTvkp8cx9_wegXjwjJg5jyAPOm4EjuPn2eF6Wdnw6UZbmvPqcqTl8DAgPeqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پخش زنده و اختصاصی بازی نروژ و انگلیس با گزارش محمدرضا احمدی در آپارات اسپرت
📅
یکشنبه
👈
ساعت ۰۰:۳۰
🔗
لینک تماشای مسابقه
(بدون فیلترشکن وارد شو)
@aparatsport</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/99541" target="_blank">📅 13:43 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99540">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UTMN_z6LEHdrAP_mUY3W_JaHz9GzQ1KvJ5EMl9YreGsfxgO8OVgRnvPZYXe61ixcPYP5VNQG_n2Tid8Cvu29VRuUp4mEJHV2xSp9dy0bnOmrL28e7Spy9fKmK0NFhyfVkXYWw_yOTgdzHueZTcLpMKSSJoUajZLu9UB0IaOA7HGqD-EV7p6frL1U2ms0boxnjtkkL3D6bXh5uYC8QW-refxMbI715DWZ-akxLOp5dMThQoqyIS2VvRFxduEqt9JIQUTUduPQ6aT898bU65Wuxe-NzIvNyfF-iUlBju6iYgPlhBXb9uak6SENPQqgRW8MMRXIZF1d3WwX6GbUOCSpHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
همسر جذاب و دوست‌داشتنی آقای نیمار هستن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/99540" target="_blank">📅 13:40 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99539">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50fb9f73e4.mp4?token=IiQiyxe3C4_Becpfiw3YBHeJqdsWtwB0tafP2eeolVcwpLfrtYVLJxWX5AT6dIJ8lylFM6VNNSmY0xhSNULy3oQie1wBCfsUubbjoL1WA3Bh-4bDKc-ZFakq-wdTB3HPEwTP_pd0L0UQ7sQLGuQ4ap9ewZtjIS9hlO-ASxyWq_8Fd85m60OEqRVTywKP4YC3PNZMz_4_u20cqqpcVqga5UBLE3eZG4NDe_KeJo6vkJoucLrFpKNaFtqqCW6dNvth7vYP7N1hAThzi39z6e4Cq-U5XbzeRSsPWM6vLHcMVlFny_ZGwoPBTKkbETxfiqePrNNIzlTfTe_wUdSTtOHFAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50fb9f73e4.mp4?token=IiQiyxe3C4_Becpfiw3YBHeJqdsWtwB0tafP2eeolVcwpLfrtYVLJxWX5AT6dIJ8lylFM6VNNSmY0xhSNULy3oQie1wBCfsUubbjoL1WA3Bh-4bDKc-ZFakq-wdTB3HPEwTP_pd0L0UQ7sQLGuQ4ap9ewZtjIS9hlO-ASxyWq_8Fd85m60OEqRVTywKP4YC3PNZMz_4_u20cqqpcVqga5UBLE3eZG4NDe_KeJo6vkJoucLrFpKNaFtqqCW6dNvth7vYP7N1hAThzi39z6e4Cq-U5XbzeRSsPWM6vLHcMVlFny_ZGwoPBTKkbETxfiqePrNNIzlTfTe_wUdSTtOHFAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینا دیگه چیه برا هالند میسازن
🤣
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/99539" target="_blank">📅 13:32 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99538">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚨
‼️
🔵
🔴
جزئیات لحظه زندان رفتن ستاره‌های پرسپولیس و استقلال از زبان ناصر ابراهیمی: من که لُخت نشدم. به هاشمی‌نسب گفتم پاشو خودت رو به غش کردن نزن!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/99538" target="_blank">📅 13:20 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99537">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d194f8eb6.mp4?token=lAlg2UOvKWpqthys5vdAsANLnZ75rbGZLYP5BkUG4CzIiLUOobtV5lkrIcue6eGPgazqbBTFpr--ufUakPhbK7MzTx1w1zrici1p5i59U2e_ZhsLEAcJiH5slNixxaz-E68cIgwEI8nbNIWNR5gES_E5jZDE6Kq0tvRTd5FNIeuaZvXMJftfPdfWaSBU4uwgN8oKclzSuWin1y98u8bDfix2SM93i1vqDrfsAs4L0cuSfp7e5XK0Z02KVUUkLpjUuSg2gKoXmNwEEi90jrj4yrkTwopDrDJXgunF-FERWQUPQv0CUadUsQZKBfa89B6hYlulLGoDMD156NRYeBc4Iw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d194f8eb6.mp4?token=lAlg2UOvKWpqthys5vdAsANLnZ75rbGZLYP5BkUG4CzIiLUOobtV5lkrIcue6eGPgazqbBTFpr--ufUakPhbK7MzTx1w1zrici1p5i59U2e_ZhsLEAcJiH5slNixxaz-E68cIgwEI8nbNIWNR5gES_E5jZDE6Kq0tvRTd5FNIeuaZvXMJftfPdfWaSBU4uwgN8oKclzSuWin1y98u8bDfix2SM93i1vqDrfsAs4L0cuSfp7e5XK0Z02KVUUkLpjUuSg2gKoXmNwEEi90jrj4yrkTwopDrDJXgunF-FERWQUPQv0CUadUsQZKBfa89B6hYlulLGoDMD156NRYeBc4Iw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
🇪🇸
لحظاتی‌کوتاه با آدیمی‌ستاره جدید بارسلونا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/99537" target="_blank">📅 13:01 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99536">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jMin2tODp2sVzJdTjYu3QPn-8RUJAkWaypXN9cCQRfuSf7XouG-oEozJDRFH6BqpZ1vuqNHBzvrgfLrWTk1AZBujQXmzRGKR9xl4F3Rwb-LlVKZyEd3e9zU2EB0S3b71mhCZDTVIjkVPUM1YG_70Ym0GPGEQBxM5AFKTAx2TkyslmwT9WLv-1FXMjWIgvfrM59j5ZPG6z4gAUaHrAa0zyD6kxefaTc240zt9ysn55iKWwCvwb-n5VW0Y5cKe5RDq81cJ_D0KbTJjRxHmAPNDQ7rtuGkrnb877d_nfaRuSVFpt7lo41ts_04BVwchMddbv57TwqQ6thsraxoUTTIX-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">12 سال پیش تو چنین روزی لوییز سوارز به بارسلونا پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/99536" target="_blank">📅 12:46 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99535">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">app (7).apk</div>
  <div class="tg-doc-extra">53.1 MB</div>
</div>
<a href="https://t.me/Futball180TV/99535" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔴
1میلیون شارژ کن 1.200 میلیون تحویل بگیر با پشتیبانی آنلاین ۲۴ ساعته
⚽️
تنها سایت مورد
#
تایید
ما
✅
اپ اختصاصی بدون فیلتر</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/99535" target="_blank">📅 12:46 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99534">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PENZoN7woaw0T11iO8GHcG-1EORLhadgEnSVML5Ms63K7AM31WQY-c2J0FfsfefrANHk2VxWDMEIDqbDW7J2d_hG88SCmS5Noga812Olzw8a73pbw0Kq9Os5FWFdJ_Rf2tDHyN3V6wGgwrXpxGU_XJoGHvx-qfv2h53imch7o0f52i8UkEfAe3_YKgvRBNGPHmEHmxzYAvHTbfMvUmZ8BlM46NbACOmPqPZAIK76Y69PZhU24jIKmt03w_Y2t6_0Pb7kpN2lNmmni9zMb2reL1VX4cQmEm6LBoW2lPXn7Ph5bRnkrNxGikz2_Uqu5UHy8aXqvyZX4kl8bE9k--3Xpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✊
برای یک بار هم که شده بدون استرس شرط ببند!
❌
با هر 1 میلیون شارژ ،
🅰️
🅰️
🅰️
هزارتومان شارژ اضافی بگیر
🅰️
0️⃣
2️⃣
🔣
بابت هر شارژ موجوی اضافی بگیر
0️⃣
2️⃣
🔣
کش بک بابت هر باخت
✅
این بونوس ها بدون
#قیدو
شرط و نامحدود هست
.
🌐
betinja.bet
🌐
betinja.bet
کانال بونوس های رایگان
r20
@betinjabet</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/99534" target="_blank">📅 12:46 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99533">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1bdae855b9.mp4?token=qBd6kXRz66VT24pd1Fn-M4SFT0bDEY1AkTPq0rLTxc6gG0eKVoH7JIeWWX2a-0rTzivl4slcHtu1z4R93dqnnB3QDF7TeutHNxPI4JffdCcdzjyRHsyC_ualTarYl6iWOuMYK4JWjw_luyZMDCrGNnglHe1o2Tj3xWhja3aIR8iKzBYlPawMCe3StXJXsD3tBVFRLfAiREqxyKmI5nIC-2haLdUIW_PWGfWFvigSFsBu6wzThtfZEi9BhQVteUVrzAqf6eQBA73FLGZE1xPY_AHv4FR6THXh3qVESgr-LJY5aIOJHXGVqE4E8KzlYPyQcXLqQ-TKDV-0q7n6bBP87w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1bdae855b9.mp4?token=qBd6kXRz66VT24pd1Fn-M4SFT0bDEY1AkTPq0rLTxc6gG0eKVoH7JIeWWX2a-0rTzivl4slcHtu1z4R93dqnnB3QDF7TeutHNxPI4JffdCcdzjyRHsyC_ualTarYl6iWOuMYK4JWjw_luyZMDCrGNnglHe1o2Tj3xWhja3aIR8iKzBYlPawMCe3StXJXsD3tBVFRLfAiREqxyKmI5nIC-2haLdUIW_PWGfWFvigSFsBu6wzThtfZEi9BhQVteUVrzAqf6eQBA73FLGZE1xPY_AHv4FR6THXh3qVESgr-LJY5aIOJHXGVqE4E8KzlYPyQcXLqQ-TKDV-0q7n6bBP87w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
🇵🇹
ژرژ ژسوس در مراسم معارفه به عنوان سرمربی تیم ملی پرتغال: برای من اسامی مهم نیستند و هر کاری که برای تیم ملی بهتر باشد، انجام خواهم داد.⁣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/99533" target="_blank">📅 12:40 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99532">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fad73d33a3.mp4?token=HMifiuu5KYkue9VrsZ8f1soLXOmmnaDjL3hHBsDTET1qsJY5QHenIiALjUJWbcOcNa2nOuAKOdBSRSieTJy_glcMtAyVdrV8aYcKgL6m4DhBNd6dRtNQhAnaspn0JJJrYFFNq6woTsi8nuU2DTUK5XmCBJcPXdAyQZFVqyoeWgw2bm_CK0C7ffaW5rUp6G3coKonTt61xjcFZRaD-TrZBcbgbuz4HJ7SHStWsVgDA4B_VSBCAcIzIdggIP3i5c2XsslEV6hShzAzI7nMU2RWe-luYvGm84HF9cy0Tn-sqVtehH_juWhEdJXvLw3opwYJCxq4wscVz62tqijskKQ2dw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fad73d33a3.mp4?token=HMifiuu5KYkue9VrsZ8f1soLXOmmnaDjL3hHBsDTET1qsJY5QHenIiALjUJWbcOcNa2nOuAKOdBSRSieTJy_glcMtAyVdrV8aYcKgL6m4DhBNd6dRtNQhAnaspn0JJJrYFFNq6woTsi8nuU2DTUK5XmCBJcPXdAyQZFVqyoeWgw2bm_CK0C7ffaW5rUp6G3coKonTt61xjcFZRaD-TrZBcbgbuz4HJ7SHStWsVgDA4B_VSBCAcIzIdggIP3i5c2XsslEV6hShzAzI7nMU2RWe-luYvGm84HF9cy0Tn-sqVtehH_juWhEdJXvLw3opwYJCxq4wscVz62tqijskKQ2dw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
بعضی وقتا اتفاقات تلخ و سخت باعث تغییر مسیر و زندگی ستاره‌ها میشه...
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/99532" target="_blank">📅 12:20 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99531">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/882a067f73.mp4?token=Lw4wbUpKvm8zamniMoGwY49TrsxaimFWclJ1n0BKuSz6_reWgPPjQnbCGrJuPUZRaHbiUHHN7VfuyZfxzU5Q25YCMb1T_r6fafNAmNkhfqSS6se86Dk70MNQd5kre_1K5gi72bXEH_S2jZAhW4Ycd-oWjN2Bcx-lxtJH96aDGkP_mFLrCE3uZ9RDs6RmQ3gnhqp5scBi-s4nPQH-6LomAUtzwLcKRdjxZyyfF3EBl5h2ATBt1ZVjtGyrDTrGN0L2rogbV1ZLpdmoEx__nhUKvCRHI8wsdIYfWsxJZMwdUnxQTP7hus8sX8RhP9_7M_snC8LHPwHWk3SQ81tcZUtmzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/882a067f73.mp4?token=Lw4wbUpKvm8zamniMoGwY49TrsxaimFWclJ1n0BKuSz6_reWgPPjQnbCGrJuPUZRaHbiUHHN7VfuyZfxzU5Q25YCMb1T_r6fafNAmNkhfqSS6se86Dk70MNQd5kre_1K5gi72bXEH_S2jZAhW4Ycd-oWjN2Bcx-lxtJH96aDGkP_mFLrCE3uZ9RDs6RmQ3gnhqp5scBi-s4nPQH-6LomAUtzwLcKRdjxZyyfF3EBl5h2ATBt1ZVjtGyrDTrGN0L2rogbV1ZLpdmoEx__nhUKvCRHI8wsdIYfWsxJZMwdUnxQTP7hus8sX8RhP9_7M_snC8LHPwHWk3SQ81tcZUtmzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
🎙
ماجرای شماره گرفتن امیر کاظمی از وریا غفوری: رفیقم گفت آخه بی‌شعـ ـور تو وریا غفوری رو نمی‌شناسی؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/99531" target="_blank">📅 12:05 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99530">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k-IOJenbXs86SsR8I4Y3l1W94eHpBj38YC1QLIcM_Vx9sjEccdH1EJu3plx-xyZsAHS5AwzVwsiCVkwL5Dr10bAzGi73cXo2Ht1DzqEZedZz9nXhGEFoY_DerM1sZGW8q71vgyMqyqDQx_AAA3p2pg5q4eiyzeXxcGzIcoKnPHrtA81ilY-3K9Q9WlSFcu2tzd9xIicKmi6FQ5hkWTIfYIFTlFRGqS77aBpkTzRmjviOvdMj7hFMUZ3I2IcctjcBs2HXBjEDz_LmQUWyOhwsaRDuVPgjbSa_5B4RJyyWQjVHLRxdtO7Ws8wwikc5xuGNIYJp8iR67qJi6Cohivc0sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇹
دی‌مارزیو: کورتیس‌جونز هافبک لیورپول مدنظر اینتر قرار گرفته و در صورت انجام این معامله باید رقمی بین ۳۵ تا ۴۰ میلیون یورو به لیورپول پرداخت شود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/99530" target="_blank">📅 11:58 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99529">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🚨
🔵
🔴
#اختصاصی_فوتبال‌180
#فوری
🔴
🔵
برخلاف اخبار منتشر شده در دقایق اخیر، باشگاه پرسپولیس تا این لحظه هیچ مذاکره‌‌ای با کوشکی و اسلامی دو بازیکن استقلال انجام نداده و این اخبار برای بازارگرمی و مختل شدن روند تمدید قرارداد این نفرات است. گفتنی‌ست که آبی‌پوشان به‌توافق خوبی با این دو برای تمدید قرارداد رسیده‌اند و با توجه به تعدد وینگرهای ترکیب پرسپولیس، شایعات در این زمینه صحت ندارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/99529" target="_blank">📅 11:53 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99528">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d06676f902.mp4?token=fFuIbTaPoOqA5Q-Vm4dAt7jgpu0oERS2xtXFPy55fOxOURxMjgGPO01JqvnnYBsYF1iNGNOX6iBihxATDLCLOyitTnyCRmoM5Rcjdl3u6Tp77G04sqdoGH-tVT8OYZIOM-vrMxDHSWY5SqLm9qpID20vEp2teVfXVjAIHO7w-qGLn0GYGh0gj12CPG3dtZwlWskI1S6t4Rg4TIHoggjMaZkGeq9thBw354bhjkWYORLMn5EZBhP2MKqidkyh8FCSPkrqyuiQSI95zt2NKgsr3DId0HQgy9Ei1l4_9nrm9DPNCOT5A1ftUSPoYCxCML0YrpUbMNGy62bZ24i9Xns_MA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d06676f902.mp4?token=fFuIbTaPoOqA5Q-Vm4dAt7jgpu0oERS2xtXFPy55fOxOURxMjgGPO01JqvnnYBsYF1iNGNOX6iBihxATDLCLOyitTnyCRmoM5Rcjdl3u6Tp77G04sqdoGH-tVT8OYZIOM-vrMxDHSWY5SqLm9qpID20vEp2teVfXVjAIHO7w-qGLn0GYGh0gj12CPG3dtZwlWskI1S6t4Rg4TIHoggjMaZkGeq9thBw354bhjkWYORLMn5EZBhP2MKqidkyh8FCSPkrqyuiQSI95zt2NKgsr3DId0HQgy9Ei1l4_9nrm9DPNCOT5A1ftUSPoYCxCML0YrpUbMNGy62bZ24i9Xns_MA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇪🇸
پست جدید صفحه رئال‌مادرید که نوشته شمارش معکوس آغاز شده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/Futball180TV/99528" target="_blank">📅 11:48 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99527">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b08f3a463c.mp4?token=I9yd-LJ94_2eVAtRH8b7KF5MSxskbARPPYp9BZG8-Ts0NmV2TikoyWEy7QAlhZ5v1-zGI-Z3TD4GordWIgWvz8kv1fjAReufhHjJywMtvR3NhABfP0OvSNZdvQ9bDGPiAoxQXA1rWV6lRJdiDqNFqYbZt87ze6dSG5sp3Cx9l4yL2elHrYKieKu_lhAiMgaUp7sTMXb6tFdeiJMqCRoq7IaDR8sLO-hrr1uZLRhTwIGTFFwMznGfcsvvo0oyrH2yCxHd7Pj45xyUD1XMsaSFxwATrHhVC6OCNJ6uHp06uJS4N7IpMCFSstmz2Xj4FdpmkGIkb6crXihue4BsoLdYcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b08f3a463c.mp4?token=I9yd-LJ94_2eVAtRH8b7KF5MSxskbARPPYp9BZG8-Ts0NmV2TikoyWEy7QAlhZ5v1-zGI-Z3TD4GordWIgWvz8kv1fjAReufhHjJywMtvR3NhABfP0OvSNZdvQ9bDGPiAoxQXA1rWV6lRJdiDqNFqYbZt87ze6dSG5sp3Cx9l4yL2elHrYKieKu_lhAiMgaUp7sTMXb6tFdeiJMqCRoq7IaDR8sLO-hrr1uZLRhTwIGTFFwMznGfcsvvo0oyrH2yCxHd7Pj45xyUD1XMsaSFxwATrHhVC6OCNJ6uHp06uJS4N7IpMCFSstmz2Xj4FdpmkGIkb6crXihue4BsoLdYcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
🇬🇭
پشت‌پرده زندگی جادوگر معروف غنایی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/99527" target="_blank">📅 11:40 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99526">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qtpn41PyrY8uOpU6-2-qIhHx6fsMAul-i8T4X6SKMIapZQyYF6Cp7ZDLtN0VdvmCJsYnGNNWC1d-hAPm4Xvw1b0vpUvNDu_LA0YWbCGkmnFvfLHfHym3mFuWQKBmQrMy9y3iXu6TkSSacjlgOBisyRqH2GhWULgwMzWJdMnv1WySSBcEtS7Wpbvxt9z5TgRK4FEuf7p68JFQx598cP7L5YhzTJP7BdcBfD9URi4yJgDVugOIBU_AqnV6CP7rS6CX513tCW2AODr9L9h_BoMdo4jxva6oG_aNb9y8EGDhI7JcLRApR_gVVbsDL0zPBPZ8Cnwzq-GaJoGVV3J7QmjtQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
🔵
رامین‌رضاییان که برای گذراندن تعطیلات خود به اسپانیا سفر کرده، هیچگونه پیشنهادی از تیم‌های لالیگایی ندارد و صرفا برای ماندن در استقلال خواستار افزایش رقم دستمزدش شده که باید دید هلدینگ‌خلیج‌فارس با درخواست وی موافقت میکند یا نه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/Futball180TV/99526" target="_blank">📅 11:36 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99525">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c662948346.mp4?token=DxJC_4M2TSdAQJapnEPeI6Jj3Ze9RbOt5Y0mNCkKiY6j3HqbDj15PnVVg12FbFr20G7WF7oro4bDuO5IyElVdKQPHIltf1NwYwaAPTBJkrjqyNYkbsB7s-mhuIvZ_kVRb-CXd_x0zM7cnhPPrGvDp4IUtzpBg6SJtrBMKstZzzTZPpWcqzLHA5VjX3cnvL0o9Hts2iBq6Bv2M3vY9sbxRxWNPhMAizOLPKqc4VN36qPeupPy3ZiLbp-bCcRlrE-SE3uZbX5Uvo6rKLDYIOK8q3qqqWzbNXjqDtRRFDa1pSNe8c26wGKv0wRuyyAy7nXB1OVbLw6dbST79RNLjHdfPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c662948346.mp4?token=DxJC_4M2TSdAQJapnEPeI6Jj3Ze9RbOt5Y0mNCkKiY6j3HqbDj15PnVVg12FbFr20G7WF7oro4bDuO5IyElVdKQPHIltf1NwYwaAPTBJkrjqyNYkbsB7s-mhuIvZ_kVRb-CXd_x0zM7cnhPPrGvDp4IUtzpBg6SJtrBMKstZzzTZPpWcqzLHA5VjX3cnvL0o9Hts2iBq6Bv2M3vY9sbxRxWNPhMAizOLPKqc4VN36qPeupPy3ZiLbp-bCcRlrE-SE3uZbX5Uvo6rKLDYIOK8q3qqqWzbNXjqDtRRFDa1pSNe8c26wGKv0wRuyyAy7nXB1OVbLw6dbST79RNLjHdfPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عادل فردوسی‌پور هم به ۱۰ سانت و ۲۰ سانت معروف قلعه‌نویی کنایه زد
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/Futball180TV/99525" target="_blank">📅 11:20 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99524">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KXAy4CW2LF_bsFYeI3A9wy7_Cqs9xsR7IvkX0GxFxRdlGAV5nzZ37PeOsHZbD8W0c9RHjmn4C_7DMajeEaTpZ_HQCGElsDkwZhCqqkAaPgyiMYwiJQ9DcOHyoNTY_72nXf68e6ZisS8SW34rBMuXc5fqkS3TMq3xdey1RlTF5zb-gFah0-3pBFpqfR_8RUjUG539M1Cj6eoqBJRfS8I3LCTlyBVZLDfGuYDkTD3ByRZ4aJHUvpyE5YVYjRtedprkdPoBrBo5jOwiwDpFZ7UP8snwXCdfQMdbcQoXUR4Clxakhh7-EkRQr532ugcQH4PaVxmeGBZ5kCuc9_9CZIQHAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇪
کوین دیبروینه و عیالش در بازی دیشب
🤍
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/Futball180TV/99524" target="_blank">📅 11:01 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99523">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/53dd4678ff.mp4?token=YS806WqVZ5LWtj9zjxz7ynHOi1JvmjwUzlAUQ7ajYEvMx0n3CbXExjaM4Y9zGPh7tOTHCHjbqaOmasUOU47KSHQXp6DARyyBuaWUZm-hTtQ_AwEQnUUv48DIJoqmlWpyXg9CKlTpIFgWMEEIqb8KT3iq1RAQ8m5WxWiGqIhdZL9WknPTZFdrG_XcnAQcEcmEUG_naw52Mc0l9goj698P17QpaUiCMen8ax9S_cJn5rQYpPpeEnoPeHc3anZaMsH_451f6Hh2fWakFnIEdQMRG56FTIBl6eKmrzYU6Thwoytw87sYrNnjMRF0UL2xbygkG4jcsGXz2TI84BK4bgAzcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/53dd4678ff.mp4?token=YS806WqVZ5LWtj9zjxz7ynHOi1JvmjwUzlAUQ7ajYEvMx0n3CbXExjaM4Y9zGPh7tOTHCHjbqaOmasUOU47KSHQXp6DARyyBuaWUZm-hTtQ_AwEQnUUv48DIJoqmlWpyXg9CKlTpIFgWMEEIqb8KT3iq1RAQ8m5WxWiGqIhdZL9WknPTZFdrG_XcnAQcEcmEUG_naw52Mc0l9goj698P17QpaUiCMen8ax9S_cJn5rQYpPpeEnoPeHc3anZaMsH_451f6Hh2fWakFnIEdQMRG56FTIBl6eKmrzYU6Thwoytw87sYrNnjMRF0UL2xbygkG4jcsGXz2TI84BK4bgAzcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
⁉️
رضا جاودانی استقلالیه یا پرسپولیسی؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/Futball180TV/99523" target="_blank">📅 10:58 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99522">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb0798a162.mp4?token=MjkVCanIuHMIrMNUY_VOd-qT-cDUDuo445kABVY7p5cJ05Ta4WV6D4JWmgZOw1lGJ5l0_PyqS71q_GIHi1rLTE2Kr3s1qs7DbGBq62nyWGHomYgZ7nn-dmbTSm3NG0kTb4PN0nyWAPVWpQVsjXHxEccXNkg_n6mBZ351mYXWnYLkQQ__Nkauj7UrztVgl89_b8ZgeAf72v39V1E6Oa3Z80D0hImh30VkwEld5y0_94dQcBUu6a7a5cXUqBoc6tz54bH-KjUfxNDw6I1ntwVNER2v04f2HnXbev7Q4Cg_CQcWcXJh4EINMXAbecSXhDqKLFWdRDTDRTrIl-AWSm8ntg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb0798a162.mp4?token=MjkVCanIuHMIrMNUY_VOd-qT-cDUDuo445kABVY7p5cJ05Ta4WV6D4JWmgZOw1lGJ5l0_PyqS71q_GIHi1rLTE2Kr3s1qs7DbGBq62nyWGHomYgZ7nn-dmbTSm3NG0kTb4PN0nyWAPVWpQVsjXHxEccXNkg_n6mBZ351mYXWnYLkQQ__Nkauj7UrztVgl89_b8ZgeAf72v39V1E6Oa3Z80D0hImh30VkwEld5y0_94dQcBUu6a7a5cXUqBoc6tz54bH-KjUfxNDw6I1ntwVNER2v04f2HnXbev7Q4Cg_CQcWcXJh4EINMXAbecSXhDqKLFWdRDTDRTrIl-AWSm8ntg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
🏆
رقابت بر سر توپ طلا هم امسال خیلی جالب شده.
👀
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/Futball180TV/99522" target="_blank">📅 10:32 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99521">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">‼️
⚠️
شکیل اونیل ستاره سابق بسکتبال NBA مهمان برنامه ناتالی فریدمن بازیگر و مجری آمریکایی شده که برای او پدیکور فوری میده. هرچقدر از سم بودن ۳ دقیقه بگم کمه
😂
😂
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/Futball180TV/99521" target="_blank">📅 10:00 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99520">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
🎙
🔵
🔴
جزئیات قاپ زدن علی‌کریمی الماس فوتبال ایران از دست استقلالی‌ها: فتح‌الله زاده به من گفت دزد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/Futball180TV/99520" target="_blank">📅 09:40 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99519">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae6aa61c60.mp4?token=hQRTt1KgIeUdGEYActwOMwETIcJR1VN5um3UE-Ux2TYFdT43Pn7z-TJlbgrx-x_HUPcAF3ZfNTRCJioqhYgnuos-WgEsMV9pBfnxrX59pyvElQ9JoED-b5iY7Amr_x0X9qviZSToJPEVv6PUXNh9-SXjy-eCtclF3UIX474oO-zw16DBHfAoCOgC0Efu7-UghoW9KKlHAGJU_2tnc0B4Cz5JxFSCY2BHIVWcAqNuL-vQp22Tjjl-merDTZktuLcANJYRMRT5LOT1gwxi20Tz7RS1wFugbE38jMUiqqFGn582289RfOwoWwZhrlyJIFtayo7kz2Vblpk-Ql95XgHV_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae6aa61c60.mp4?token=hQRTt1KgIeUdGEYActwOMwETIcJR1VN5um3UE-Ux2TYFdT43Pn7z-TJlbgrx-x_HUPcAF3ZfNTRCJioqhYgnuos-WgEsMV9pBfnxrX59pyvElQ9JoED-b5iY7Amr_x0X9qviZSToJPEVv6PUXNh9-SXjy-eCtclF3UIX474oO-zw16DBHfAoCOgC0Efu7-UghoW9KKlHAGJU_2tnc0B4Cz5JxFSCY2BHIVWcAqNuL-vQp22Tjjl-merDTZktuLcANJYRMRT5LOT1gwxi20Tz7RS1wFugbE38jMUiqqFGn582289RfOwoWwZhrlyJIFtayo7kz2Vblpk-Ql95XgHV_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
میثاقی دیشب ناینگولان رو آورده بود آنتن زنده که یه لحظه از دستش دررفت تبلیغ شراب کرد
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/Futball180TV/99519" target="_blank">📅 09:20 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99518">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/29484b00cb.mp4?token=mHMeWlOBVPLtnYN8Nc-p0c3wDn1MW7Cz6Y_A5n0wPzIppZPg0Fo95BuAblzzJzAN_T-eGH7A7ww3L2kZsYomUA_X3vjFhH9Wf9i-xS0Kpn5xvvrB0TUkORhJo2kL733vwg9uQH8Augb2p4DPJMOO2qNW5j3n81iguTgi-ws1MAbVRcZDUSH7NYUMpcdjfrG2hvGGAqrvi7NHc_9St-hGSugrIo3OiU8YUYuAuY4lwUXnMRlFF70VDPiRk_ooDuLETriUWL6LA4On0V78C_IL6LJmhDgSARWPgTIjDD-tPh-NPgtt1euUifOwkQKh7jNGxOg08AvI2hyueN_xRzGYaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/29484b00cb.mp4?token=mHMeWlOBVPLtnYN8Nc-p0c3wDn1MW7Cz6Y_A5n0wPzIppZPg0Fo95BuAblzzJzAN_T-eGH7A7ww3L2kZsYomUA_X3vjFhH9Wf9i-xS0Kpn5xvvrB0TUkORhJo2kL733vwg9uQH8Augb2p4DPJMOO2qNW5j3n81iguTgi-ws1MAbVRcZDUSH7NYUMpcdjfrG2hvGGAqrvi7NHc_9St-hGSugrIo3OiU8YUYuAuY4lwUXnMRlFF70VDPiRk_ooDuLETriUWL6LA4On0V78C_IL6LJmhDgSARWPgTIjDD-tPh-NPgtt1euUifOwkQKh7jNGxOg08AvI2hyueN_xRzGYaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
🔥
🏆
تکلیف اولین دیدار نیمه نهایی جام جهانی مشخص شد: اسپانیا-فرانسه!
🇪🇸
🇫🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/Futball180TV/99518" target="_blank">📅 09:02 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99517">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vnpigtnpvO_RTnQHWaIWVYMA501TToBYD5bSucYEYM76H5zvzzGdBCKxNJSla3VhLqrf0ghFI3idOobpMqVqZ0xJs5DsjNFanzJLH1Zpr3yWL3_-iZMy4D4n5AqhRG_PWWv-ovqozLcbb8zUFMCIBQDjB1AbAswQ_VySlNWs2F9xfgsjIuCAK3Cnv7faX28VMxiaUtdU500Cr0dS6b-rOnIzuQuZjLG5bzOuBm0po58GbozhU5mBXrUwcrDdRKirLTIfQy5GQiqwmDY3HWifJOd70n-Pg7oyYapa9ZbtAaNZ9Yoc8a5n8N8w1ACCTHfFQX0gFayzKBW9DIuOZxVsUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
💥
نیمار دیشب در تمجید از لامین‌یامال یه کیت با امضای خودش رو به دست ستاره اسپانیا رسوند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/Futball180TV/99517" target="_blank">📅 08:53 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99516">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/3f60623d0f.mp4?token=I0FYlTLWJuC-1CMyq3Zm4aFIyM2A8gIS4vRObn-MnN-wZe6ySodnUtO36XCqkzSq_L-2Zmb1S6lbLLidB1-eheK8VAXGNVUvB-yS-2wwe4s-uf7Qix-ci-Ax-VWQ_VCmFn96QFyl6YZzmXGrgt2FiG43KjyoZPQURQFvP-sM3f3PCkQ9W9lSAGJWJBAFNaCtgteJgI126f85cZ4vIO_3M_2huhllGTl00KpVqqFbzSkDvogX-LtY7E9hKxL8pPxv5T6tjUW1w3bmPQYHLHsqVoxe9t5cJq2n7_OIcsJ8fk600kvrVi9n05Od2lgx_Cjf-OQFps1cn10moKshOhqSWw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/3f60623d0f.mp4?token=I0FYlTLWJuC-1CMyq3Zm4aFIyM2A8gIS4vRObn-MnN-wZe6ySodnUtO36XCqkzSq_L-2Zmb1S6lbLLidB1-eheK8VAXGNVUvB-yS-2wwe4s-uf7Qix-ci-Ax-VWQ_VCmFn96QFyl6YZzmXGrgt2FiG43KjyoZPQURQFvP-sM3f3PCkQ9W9lSAGJWJBAFNaCtgteJgI126f85cZ4vIO_3M_2huhllGTl00KpVqqFbzSkDvogX-LtY7E9hKxL8pPxv5T6tjUW1w3bmPQYHLHsqVoxe9t5cJq2n7_OIcsJ8fk600kvrVi9n05Od2lgx_Cjf-OQFps1cn10moKshOhqSWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
آغوش گرم لامین‌یامال و تیبو کورتوا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/Futball180TV/99516" target="_blank">📅 08:50 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99515">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🚨
🚨
📰
فوری از فابریزیو رومانو:
👑
- باشگاه الهلال خواهان جذب رافینیا است و به شدت به او علاقه دارند، اما در حال حاضر، رافینیا تمایل به ماندن در بارسلونا دارد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/Futball180TV/99515" target="_blank">📅 03:12 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99514">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FQVu9O5Bz9_kHCPAkyIdcpe7O-A2_UoEgIXvkNXJi5peJp37YEfevG0MwHNCwS2w2OooACCmem78QxYhKn1Fw2HmbMB-YKiTnorbfe0VCfslN4zo3pKm0vpdYxEBtmSdwIamXDQkhy01UUF4es-GKicTSQuEeMk6gmCAkZe0IhdSZwW28ix5w81A4rtDDAa2HNZyQu4m0ZtXc1F5qSDQweqp2WZHObWXFOZRY_K-rf3vrMGWr9wbK8QJ7GL6d3V2AYcuGylgL0F7vn7c6qw4WB-JeSu0chfKngSrZ2XTYQF-YnUzh5oqjH4Ev94C-t4-8Hrf61S3GWQoZBfNM9hF-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
📰
فوری از فابریزیو رومانو:
👑
- باشگاه الهلال خواهان جذب رافینیا است و به شدت به او علاقه دارند، اما در حال حاضر، رافینیا تمایل به ماندن در بارسلونا دارد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/Futball180TV/99514" target="_blank">📅 03:11 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99512">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kRSfK8Q_tus_N5mWqTJ6RRY839BvDBNCcZT_LnxQsZxrgi-5wwWAwJP1IsL_uzHKY3lIgex9VvXJ0fOUrV873NR_OQ71KqVbxJNysxbENLA_HmnRP0H0kc-krbp0LFMFZmuJp0ELx68y0fj5yFT8EGE_n3KKofQnaqv-MRRl2odEpDNiMQPbcVKfbbgjj2EFd9WhVhYErMWaNT5GoqcZNY4kosa1k6TT22E36m65EcA7c4ftclKt4x-fenYgKPDsDPUrXNQTfJdnNMkNzyz92c0trLEpcPzfscTvyzyz2zAGJC5XwZ4Mv5flZbp76al9mmt8akLSetHRbh2P4MDjFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🔵
رومانو:
پاریس سن ژرمن به شدت به جذب فران تورس علاقه‌منده و اونو برای جایگزینی گونزالو راموس زیر نظر داره.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/Futball180TV/99512" target="_blank">📅 03:07 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99511">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CMgp-iwYmejdQ3gtxsWEMONQomJHNXBiKehfNEtBvxNB4mgO-3NUK2qMzcGiVwp7zRGhf5UfNffEgatJXs9dp6Sc_1t3bNKug-xTCI-mGigkV96wHQSKpGSu0hjCVtlhrOrOyqKxBbzT7N5LMUiA3o8whp8P4-InZA1P3fQp6J6_akp2KXVnyM0kUjMf4VWDLl-g1FLtWMe4n1ih_ktD68SIIfhl5Be0aYX7HNMHmnFgmt4S7iOfcezhJ9LTKGkVbBBklFkZ-1KRfJFfln18giJKpXl-5qzjKXt0Oyi-_zQ07dT2wyRLiJCwMkgVfiuORigswBUIPvYxN5vHNqKKPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هالند پیش زیدی بوده که یکی یواشکی میخواسته ازشون عکس و فیلم بگیره بعد هالند زودتر طرفو دیده و از یارو و زنش عکس گرفته گذاشته استوری و نوشته هی یو
😆
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/Futball180TV/99511" target="_blank">📅 03:03 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99510">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d0867b13a.mp4?token=CCq2teA5BAwc554akWA0M6LIHdmwb48dUq0V4k1yO0gOCw_Sexqhh9djcA9f15ZoY772U6MkxGVn9spASQDCks3zacMyRm5J5jMPH92XgA3sFlux1ZC-A2MQrPhKHE0OBX54rfZL1tjru_NQmJYNbx_pXCrZnssNW1ZNmhY3zXMFmkDab9wuMLIPIxnONXjJmIL5uN7ghkdb99Sc-fKmYAdVVNAz0xYcmLXhL1AdRLgYtbaazVDnQQwitMpOMnvey60B7oASsjj-u1PvqvMnvUlmHYTKOrl-zjp_YfaaIkzXK9V182ru3i1uL3oqJxCuA6EptfNvyDb86Ucdjn9JBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d0867b13a.mp4?token=CCq2teA5BAwc554akWA0M6LIHdmwb48dUq0V4k1yO0gOCw_Sexqhh9djcA9f15ZoY772U6MkxGVn9spASQDCks3zacMyRm5J5jMPH92XgA3sFlux1ZC-A2MQrPhKHE0OBX54rfZL1tjru_NQmJYNbx_pXCrZnssNW1ZNmhY3zXMFmkDab9wuMLIPIxnONXjJmIL5uN7ghkdb99Sc-fKmYAdVVNAz0xYcmLXhL1AdRLgYtbaazVDnQQwitMpOMnvey60B7oASsjj-u1PvqvMnvUlmHYTKOrl-zjp_YfaaIkzXK9V182ru3i1uL3oqJxCuA6EptfNvyDb86Ucdjn9JBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😭
گاهی پایان، با یک سوت آغاز می‌شود...
🔻
امشب فقط بلژیک حذف نشد؛ آخرین جام جهانی نسلی به پایان رسید که سال‌ها از آن به عنوان «نسل طلایی» یاد می‌شد. نسلی با ستاره‌هایی مثل کوین دی‌بروینه، روملو لوکاکو، تیبو کورتوا و اکسل ویتسل؛ تیمی که روی کاغذ، توانایی فتح دنیا را داشت اما بدون حتی یک جام بزرگ، صحنه را ترک می‌کند.
🔻
سال‌ها امید ساختند، لحظه‌های فراموش‌نشدنی خلق کردند و بلژیک را به جمع قدرت‌های فوتبال رساندند، اما جامی که شایسته‌اش بودند، هیچ‌وقت به دستانشان نرسید. اما بعضی نسل‌ها با جام‌ها به یاد آورده نمی‌شوند؛ با خاطرات، با احترام و با تأثیری که برای همیشه در تاریخ فوتبال بر جای می‌گذارند.
🥂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/Futball180TV/99510" target="_blank">📅 02:31 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99509">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QzH3y-TFMk1wrrRwq-e9fyMPsEglIhgdXfKjAt2eBljthvy7BaSO8TbfW9IN-0xlkj7WY5HDx8_QizWifTE94rv1u1T7ZWyx18uwyVEvTn7RbX7lf3MzGpeO0vOjl_hViCLGhpB1zHBIpHSCTarNrFDdACtuVwhG3g02M2Vi2elaxgefzHNlRbUgnwROTcwCaHCwktqj6yxWK7QoII5JnLSXxEGKCpR_lbq7H_ksavTsgHAKtZco2-NJe7S403KgYTmqB9WYUti9urpZUKGRrsLf0ke-ivWSHfzlX3jVlsdPfrsXMmKkF6XHJuwEF5BIjw33__Y8-_y4iCLE3rnSng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
طبق اعلام رسانه های نزدیک به بارسلونا، فران تورس از پاریسن ژرمن پیشنهاد دارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/Futball180TV/99509" target="_blank">📅 01:55 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99508">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
🚨
طبق اعلام رسانه های نزدیک به بارسلونا، فران تورس از پاریسن ژرمن پیشنهاد دارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/Futball180TV/99508" target="_blank">📅 01:52 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99507">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ItX6F2dOLi_zPJDuQCqRTwQ22o4txusvLJlWaOKROcJIf4_4SCqUTZu9rk7V51o0zIYNal4ql0PNCx0vx12tRrK8CKtzI4ve8h9fT9UutlL8D1LYfHswK4ZugQg2NwWc-FdtSKxQWnKmrs8AilmxW3mZnlaHb7FqbALLVfddAr3PNL4siQ3s1ma_mMnCFBnFdRuYRFfXlGh-uxPN3n88xjQN6ZVGXjc_ZWToUVZ-Fn--LxzA4GmIjhj0WWQPivhI6KTDqS-IsrGKxFbS5CuqFIg7poT4i4TtXBU1sQpB6rKSSL4_FOvSrIU_NthAnjwyoqf7MuVjJceFZ2iZUgNc6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
16 سال پیش تو چنین روزی اسپانیا با شکست دادن هلند قهرمان جام‌جهانی شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/Futball180TV/99507" target="_blank">📅 01:50 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99506">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FsRo2ANNFxRWjsY-nInJGRdDQxGFkwnGJmfnvUcHQ2q0Xi0K5xdzt6UcPTuMaeGHYWX-2ZxzdG7xePf_-1aSxmwIbOyr7zN086U9ptPapb7iD8Ru2wHQ_Q93jqsl3Nx7aqRj0vY7Pn--X4BZPsrMFoDzCxDTxYVJebIS5jyGO0WnpajOxs0Ycs5GMVSaGD_4H5jgpRZH9wqDskVzbsGX00ckgFzGdx-74rp5nGFH_gu-h3VKzr9J35iBWo_siLg3urUH7EwpsCTMY9dl14ms_8SXfYCAXBzp4lhhchSv3_i4JiquAtz8oOkktCw5r9kXqk01K7Ub0Rj2F34Hnhjh_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🎙
🇧🇪
تیبو کورتوآ: «می‌خواهم یک سال کامل استراحت کنم و در هیچ مسابقه‌ای با تیم ملی بلژیک شرکت نکنم، و سپس در مسابقات مقدماتی جام ملت‌های اروپا و خود جام ملت‌های اروپا در سال ۲۰۲۸ شرکت کنم. نمی‌دانم که آیا بلژیک با این موضوع موافقت خواهد کرد یا خیر.»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/Futball180TV/99506" target="_blank">📅 01:35 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99505">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bXa8EpF9aYZ9fSEUXPNu3GhP0sSVu7xGkyIGWxI6_T1mavGWrIoBTal0-gnaclslnZ4U88h1MrxvkU4KjfU1gcf-ufgTSZVGDjpm4rTHE2-pCpZQL6r8d3K4TLMjC_l1oYwYjjHTrAI6G1WQEvhBTP5Z5A1J5PkIc_zwv_hBRD-NE9iB3SxP1_y79n4KfA3NzIeE8lGBAFhGslfF6m7zM7XlO2fXofOv0XVop3vCWdyp1ovcRiXh2AS0TIt3OlOKGhncDlvJFAL2Pt6AfZ90bEJBNBWvGXTQAZJJDT4NUBmASO01EtW1lvdKWAH1gCC6K92o1lRzHZUdhLMmmS1Hhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔥
🚨
🔥
🚨
🔥
🇫🇷
🇪🇸
لامین یامال:
‏فرانسه یا برای بار سوم متوالی به مرحله فینال جام جهانی می‌رسد، یا ما آن‌ها را برای بار سوم متوالی شکست خواهیم داد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/Futball180TV/99505" target="_blank">📅 01:13 · 20 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
