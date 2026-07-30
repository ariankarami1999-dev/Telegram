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
<img src="https://cdn4.telesco.pe/file/tbjgIm84FYLZ5ljdfck2Bf3By61ECFVMj1eR7UtGBLBlycInnDYd8SM0dRVfP07iCLeBYY7CjtCLSB6J3Sj9Fsbf5wEXLxZ5JANcibLvuXRzSsurapbPylad5_TiMrbl8YALRoy_TKmk2GOrQtVJTU7Q9A-AWXH-yqiNyfACR6XZ4atchqGO92CHouE3Q38Be8mkGC_FW8y2Ck0PlLJHgG0qLXpc1GQjI9FDDYH0niLMal5lPGqi-GbFw97eWE43i6GHRREULHL1XtWNmNaL3vvqN8WrTlcpjYj4SiS4cPv5WTASC43kWtyXngqjM6bHqwSTiCsMKpvpH-r5vHt-RA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.79M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-08 13:28:27</div>
<hr>

<div class="tg-post" id="msg-453547">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BHszNYS8NJdQV1V2A0bBMoGA-oIusJk5h55Cr4YhZ5Vt5Bu3JeEUaFipomzZ8Z112LbFZJpwRAMzQPMB-uwwYT92sn87eb3EtdcHP0y0OJhv-nTWKQ_znDHQac25bbKmjl-EaBBhafR5ZzT__kZriHRD4QA-acW7PvjfNguz1H8PEKDdU3XsexNP2vjfqnRx8rNAAnrJATSpcG9XgB79rEkVdSr_z2mH39EFbY2t2Vvw2kmlEET751ZqqeL5-wy5w_L_NRr8dOnuUcwRKTCpX8SU8vCBc2jWpQRzkqMyPfmCte5nBkXpOO_q8XwUcAPUpUr9NAz9obL75y2FzuKZgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازداشت راننده آمبولانس در اسرائیل به اتهام جاسوسی
🔹
یک راننده آمبولانس اسرائیلی به اتهام جاسوسی و انجام مأموریت‌های جمع‌آوری اطلاعات برای ایران دستگیر شد.
🔹
به روایت روزنامه «یدیعوت آحارونوت»، این فرد ۳۴ ساله از دسترسی خود به بیمارستان‌ها برای جمع‌آوری اطلاعات و عکاسی از مکان‌های حساس استفاده کرد.
🔹
گفته می‌شود که او از یک «چهره ارشد اسرائیلی» که در حال بازدید از یک مرکز درمانی شمال اسرائیل بود، عکس گرفته است.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 601 · <a href="https://t.me/farsna/453547" target="_blank">📅 13:29 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453540">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qOYtVtGxOZNPYt7K3z7ei03N7c-A8THkcv8goMB6B6V0eYf35u5EGNWal_NGEsihWXzb21F8t3w-qgE2W6xI0oAtbr8S6oXGaOGG4VX_rxgIiSY63AH8jDgxzoaRmYf5dH4VGD9j1izvKbMeByWgROIJTXY12XQrlYE7JT8O4bhPQ4zqaDoI6tQoIz98Rhnnbm8IUtagK9kw0L0x2TcGvOc4dnpy24RX70gO2KAAba_sA3c8uivODkfA2qMuuoDErSdcI-ZbtAXeHSwZOJvWCTunJUEpO2cfeAG9PExSY4UXOgFPx2TzTyzH44pWnV2a-uyGvTXcAmJVxEXMZ7_XNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gaDWOqEs7tAGXNHCDGzwXckwRxlfYHBbEoItPNSC11qg7BgVMHqn3FjVTdRVuUSDYS83JOa9Jz3yYjGuOAN4uT1Ar4YaY5yVWub-jvRHoX-YH8-QHl-TWYDhRRp5oTWsPfclopzpGdmdJc4-AZPWBaq-e5nabHwrzaYD2KqM1bkPoDAVm-KWFzKslkYereG1y9EtVv6bHfghdSuJdyC1O0BdPOv-eRXRKq-PyZv7tak8Zd8Phe0z3m47jtSuLASrJuDkGNXm89fduh6cbA4P9-Mrjz6So5JFtNEdmixXNckQTuWxfW1v4qNPPIRraYvMS6QsYx-2UA3CfEMSdIW27A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q9AZ80yPoGLiEVmddmiOnc8jQaZ_uJOW-a14HLrOfUvBlvpDlGwn-YxOCV8VDRMJGduuCo762J5TnHIC-9VnE8R_FjWo-7HF6mCQqNPSXhXvQbFk5eeMQRTSxqt1LFGhAMuEF_PSN3n8GYixYVTSo3NQltTOXDkE3sjqTG4_NVqpr_53kFvQ6r4a2UJk2DUXaW3dvJngDtoxuiU3Bx3TdtzKBxizJvhBpevHGun_HV-o7o0feoQCSEe8q_zTiAGCE-tzf9VlHx3jWPHwp9527pNBoHH8W_zw2ezgIXjRomZxp9M-Qg5i8JycAceesBCdgEjd4aY-XIJq1crj8w8ZPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tCF87gZvBHseRjIcvNL_eFVIWWWzdISOhCisj1oKZbHpsaICQ95rWCFGQq83fGIgX9eEhiLPxjvBymIHjGxeSo9ANWpidlTpw2UfVGpz2RmfBg4Q4o0FqF-0DP-OS2sG-mVZol3pk6tmeBhUnBlZOgD_EwtPY_b1GKvSdBj_6Ks5grmaKoEKSlJywL2pENMoPAtZCSyqVveVtOAblTCFrmrZnBftFNEP2s82lQmJTBTqOToGoP9RHGS22sU81bsKYALbQd47-ZT4yg1dp1XWe2YrXlwB5lcKnQAeVDfD72MRlIzIzbuvJ79h_zag8cFmJu6PI4Dibt2VwsA3NnDUKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Nv7cv_HaMCbJXJJkg4xm8DL7yKB5wup_hyJxrBwx4AEIkx7kO9iR0g6wN1hSXQux4T5RCYJbzbr3b6yRG1F6UYpGHY2Fxbk8c0IuoffaKv-bEx9LsXaGxkkhQdRfzwm5wNTNVoPP5gUzLgWg8uRR6Ekl8vnsb4Huq351qrZkT9vEUnAC2ImXsTLUxbeIP86SHcDjQHT3NA2Zn7AODhpj1gcKN0hs_U3eN8lRxFxBMU-65_ClMdFlyFvh3WY3HbG_MqzWKEex0cUCVIs88ezpVws4aXfG5gFe7eUgDVmQGxyV9mdsAAG2khsMC3yeQ-DBuAyQ_CECXN-c8PPczDq2OA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sIGYCqB95yKjuf0QZEERLnZW6Q_WF1uS1VO7wRQtzky1w_CF8sCN1azFNBiYt_6ymfP4Gkfxi5C0uy7QfCEkB1FVaNg3nWrhtqJMBZL3CVVRKz4vuSy4YRWh0DYk_R7TsDLEiq4X6XMxXeRE7kv-sqzlgRS3mZp_O_tXHttklwZTBZ37GJmxayIBMXqz82o2MoeWOEQiby0uS5Kq3dm5hAMTfp2urs1j4cvW68-PKDQ0_i0bfV6dAKnFQ3mdpXYd0NeL_RUjxXnHrxLtzgxPFXTtYy6lrS-yy1lIDywMbJiipXprs1PnFVnkF1H-yMregsPyM97VTw28eYI09qQezw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mYeyTXK5mrNbkynEqIpUsrkHq--jATAoGIEDADOmt3oEj4WIhMFX04usbYzk0FQ7Z9F4slTZT27ZZEqx7jb0JWWZ8_wEgNWoXEJBYPTxEC-Z7r7Aom845b4s2BRp2D5wdp-8zthdrkIcQvRLGRhTBxBpcF5Wbd2WALi1cVH02v-gaOMyKXfiSlGOByqEZ5urk7iPthVmL6xtjRtnKWb1eI7P6LYYKRiVqM3MXDx5jWNIVFDdu63v5QTa5NUNnnYuPdJtpvXNPaZu-YwGUKU4zar-BDNgKYtiZfCMKGbZAfSCgbNuisfIVYse0yeG3lcfnk0ZwFDn2nSqsJ5Uksk3LQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
پارکینگ‌ مرز خسروی، ۵ روز مانده به اربعین
عکس:
بهروز احمدی
@Farsna</div>
<div class="tg-footer">👁️ 1.66K · <a href="https://t.me/farsna/453540" target="_blank">📅 13:22 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453539">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VY25T_C_SVu11LuGt2alUMWDv6EaeV70Jcm9Njdp24ehQmJHoTfpaRWU2N9Ue7LkMUP0Py77z-cY-aWACCmQxoStq5rbtUQuleRosW-QSMQfA6HPJZFkF0z1wnn_BVEWx_pxk9M8Ai8fjakY3gWJUb47yCFSh8o3wxRDrsfcyRX7hmsNV3ounB4d7mod8R-CY2ViHRT_KeH7DxhavkVpr1GC0NMMuWQDB4-fhbo9SEZgnNqFp-PRoaU--_KzK2L9kteMLHWdnKvXrEDdft027DlhuGU36fiGQrx3WwznkrE-OcPeeK8UhsB-VrRxW4YJ5Y0XfRd-GAGCfe5zmmtv6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
تصویری از دو فرمانده شهید سپاه پاسداران انقلاب اسلامی
@Farsna</div>
<div class="tg-footer">👁️ 3.32K · <a href="https://t.me/farsna/453539" target="_blank">📅 13:15 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453538">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Eh5tTN5WzHhQQcP-PkuPTrDd9skRXWzGacGZ699gMcUFg1sqGAKYaXNiFWSM4UcpwoAYDi-m8L0gVfnsDG3UI51R3zU7zzyXAOX72inzmtXUWL4Rtbj1Y32wf3faDpxfwyvTOuZyH7Uiqg5U1kBNfJB072FP0DnIg3kaU8CKEvM9phOBFPIOrDmR4ilghcg1m4f_13YUaJ0hm8_e7plF4iVHYUjbFPoPxz6Fb324GSuR9VlmCOC2vs89lg3JyJJxcsNFrvg906WYpkmdVRpxW7suTMc0mbs2_Hiax3EnaJzJ2AGjeeAF8R3UAtVUJWNhG5Ki-klbg9JwXgtPFzLDUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نماز جمعۀ تهران به امامت حجت‌الاسلام ابوترابی‌فرد اقامه می‌شود
🔹
نماز جمعه این هفتۀ تهران به امامت حجت‌الاسلام والمسلمین سیدمحمدحسن ابوترابی‌فرد در مصلای امام خمینی(ره) اقامه می‌شود.
🔹
طبق روال درهای مصلای امام خمینی(ره) ساعت ۱۰:۳۰ برای حضور نمازگزاران بازگشایی می‌شود و برنامه‌ها از ساعت ۱۱ آغاز خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.29K · <a href="https://t.me/farsna/453538" target="_blank">📅 13:13 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453537">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">وزیر کار: پروندۀ پتروشیمی مهر و جم با اجرای رأی قضایی مختومه شد
🔹
پرونده ۱۵ ساله میان پتروشیمی مهر و جم پس از پیگیری‌های مستمر و با اجرای رأی قضایی مختومه شد.
🔹
کارگرانی که در پتروشیمی مهر مشغول به‌کار بودند از هفته آینده با پتروشیمی جم قرارداد خواهند بست…</div>
<div class="tg-footer">👁️ 3.33K · <a href="https://t.me/farsna/453537" target="_blank">📅 13:10 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453536">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس نوجوان‌</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c94f1c7eb.mp4?token=drj0YvbCw5ugySeOmmjBbMC-CEJHTdMdPGNOtPggogKsHwLrCxLC5edFi71OZClzH5yrIyd71jFTtXesu-a3okTq3E2sMEzG9AGhZ5qmtmBEfrxVHPwwSRokafrm2BxxxQK0D2ac0aTOi0BTVfHeStbTD173yFwVqosq0cRI1bv6X78munSGXdTWW7BGh1_5HMsveTccZyCBEAmry0mEqGe1ktHBdbN_Dm8HiLIGhjxzIYWP6D2sy-tgoN45T_GjHUyqwSFKJtW6GbITzxvLxb57qwboN-M-qf2FHtTIEEWz_asLIlMNcQsv7La236MBRj3y0o6hNJ2vDhpeyyY5RqQebFaH36s5hSOeQcVsoP7xjymUju_NYzPM1r0bnIdpMN_sDe9bidF7HzKPcat_14TGtfspCGEFHlB5LUNxGPC7TxpsX5zGjwTQVRS1hEyrCTPzxUz_KPKZRF_ZbMy5LUUPn6uilyT1fPerJ7EzA0B9gZOsfoabfr09E91KKKqx6m6RYKlXPtmSNAlgg8PX3tw3gOpDU9oX8nZbKAJk4bCF-PcteLKEfsQEpKWzfQr6VF-CNrabRmulI8Bs4uuLolHYqzekaZ4pnHMR1rNX1HQ0nr9542Vf2jIhQ6Yo9reAopC-rir64af0MevlRueL7Fip5KMxWq2-2takuid61RI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c94f1c7eb.mp4?token=drj0YvbCw5ugySeOmmjBbMC-CEJHTdMdPGNOtPggogKsHwLrCxLC5edFi71OZClzH5yrIyd71jFTtXesu-a3okTq3E2sMEzG9AGhZ5qmtmBEfrxVHPwwSRokafrm2BxxxQK0D2ac0aTOi0BTVfHeStbTD173yFwVqosq0cRI1bv6X78munSGXdTWW7BGh1_5HMsveTccZyCBEAmry0mEqGe1ktHBdbN_Dm8HiLIGhjxzIYWP6D2sy-tgoN45T_GjHUyqwSFKJtW6GbITzxvLxb57qwboN-M-qf2FHtTIEEWz_asLIlMNcQsv7La236MBRj3y0o6hNJ2vDhpeyyY5RqQebFaH36s5hSOeQcVsoP7xjymUju_NYzPM1r0bnIdpMN_sDe9bidF7HzKPcat_14TGtfspCGEFHlB5LUNxGPC7TxpsX5zGjwTQVRS1hEyrCTPzxUz_KPKZRF_ZbMy5LUUPn6uilyT1fPerJ7EzA0B9gZOsfoabfr09E91KKKqx6m6RYKlXPtmSNAlgg8PX3tw3gOpDU9oX8nZbKAJk4bCF-PcteLKEfsQEpKWzfQr6VF-CNrabRmulI8Bs4uuLolHYqzekaZ4pnHMR1rNX1HQ0nr9542Vf2jIhQ6Yo9reAopC-rir64af0MevlRueL7Fip5KMxWq2-2takuid61RI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
لطفا با کفش وارد نشوید!
گاهی یک اشتباه کوچک می‌تواند تصویری اشتباه از یک فرهنگ بسازد؛ حتی اشتباهی به کوچکی یک جفت کفش.
در مسیر اربعین، شناخت همین جزئیات ساده می‌تواند فاصله‌ها را کمتر کند.
@Fars_Nojavan
-
Link</div>
<div class="tg-footer">👁️ 4.31K · <a href="https://t.me/farsna/453536" target="_blank">📅 13:03 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453535">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iPfQCImQVJZ8Ewcl47jKGfpNcrqnMltsj36hrZCpUXzp-yFIJYG031AfHBmxpmNK6GUXTiY9SNaeYLt_i4w1s-LHXB9nDkZ37WMNCy_hLMamxdOmlArzjvneS-Bq2PmvXNR2GrKhVxZTC6mQ_TAtj5y5Qh2rKW8JyfB-ovgnGvLC8AScIeKe30I6O7xDZRCghWSznWICsdkXBoYJHVEgp_4cWdqjfB5AXuKNNnUxRzaEKHykW50i3fLL9efTZBa-ayfGsH3WU6ge-xOz1LfwkjwXgItjaYGUiUreX6BnX8a5OW99BqSWh1rjtM8I7vMXwhoZKZCdBihYGcgHrkwIDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر کار: پروندۀ پتروشیمی مهر و جم با اجرای رأی قضایی مختومه شد
🔹
پرونده ۱۵ ساله میان پتروشیمی مهر و جم پس از پیگیری‌های مستمر و با اجرای رأی قضایی مختومه شد.
🔹
کارگرانی که در پتروشیمی مهر مشغول به‌کار بودند از هفته آینده با پتروشیمی جم قرارداد خواهند بست و در روند پرداخت مطالبات و حقوق آنها هیچ‌گونه وقفه‌ای ایجاد نخواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/farsna/453535" target="_blank">📅 12:58 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453534">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🔴
وزارت بهداشت غزه: در اثر حملات رژیم صهیونسیتی در ۲۴ ساعت گذشته ۶ نفر شهید شده و ۳۴ مجروح به بیمارستان‌ها منتقل شده‌اند.
@Farsna</div>
<div class="tg-footer">👁️ 5.72K · <a href="https://t.me/farsna/453534" target="_blank">📅 12:41 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453533">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63f8e62266.mp4?token=Z0oqbgpdvgkt1iD6V1-lOega3E6dz-724wPaQM3cVaNrTMU2CDU25HmOe3y_OWCd14cFFP_XDiU0N_C2X_SLRFKm-m04vsOqqE-rXgkmcsHok2u8zFX0q1borVdbj19CIEeW8oep_K-BsWaSU36C4J340-xR7xMv-Mk1ZzNZss1Lw4vjJj4YDFzyhuUxPco2DLDpqhRPugvJU9yR2Jyo2ZStzNpKSmeHX9CIm5tnpYNrFcjfoJFIR-MOiljdh9VcbP_H31bTuq8UO3XrBPgesmdS06eMNXDYWqShDUo0D75q0dQtmDQe0fixj0jJeio_Q8chh10GcYLJHdExD73W3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63f8e62266.mp4?token=Z0oqbgpdvgkt1iD6V1-lOega3E6dz-724wPaQM3cVaNrTMU2CDU25HmOe3y_OWCd14cFFP_XDiU0N_C2X_SLRFKm-m04vsOqqE-rXgkmcsHok2u8zFX0q1borVdbj19CIEeW8oep_K-BsWaSU36C4J340-xR7xMv-Mk1ZzNZss1Lw4vjJj4YDFzyhuUxPco2DLDpqhRPugvJU9yR2Jyo2ZStzNpKSmeHX9CIm5tnpYNrFcjfoJFIR-MOiljdh9VcbP_H31bTuq8UO3XrBPgesmdS06eMNXDYWqShDUo0D75q0dQtmDQe0fixj0jJeio_Q8chh10GcYLJHdExD73W3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اگر الان کربلا بودی، اولین کاری که می‌کردی چی بود؟
@Farsna</div>
<div class="tg-footer">👁️ 6.39K · <a href="https://t.me/farsna/453533" target="_blank">📅 12:32 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453532">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc200fd510.mp4?token=KcI95bPPeJhbrJIkbo9q1QQefigXAT-eYYKjXkIm6Z2WzxK-Ge3wll6GV9Js09b0isCQj_GytrAsOS6825WJnw6-KBbjw8PDgyicjkkGEYDHEeZLq6P__UbVT5vKaa_abiizREVBFHBM-KCwMxSnfOUvuH7KuxDGpu3vrNMsroNzoaoJjR_4GGBqDj-TJ0hQok4OYyq0iFxt6OUTOvUYaknmn1fgA6r2WVg42PeP8Q-rO7jhTyrOFgTpmw3gGK_qoKsvb3xAJpcEjZG6l0zYBW1I-rX7UTnr8Ruxpf-wWSvQAMA7JHhQ2m5lCV8MInoiYS04f8gvMYFN9uwWMzOT2hVEebqnbHsAOukWMDWGGTJNlMB3fAkA3MRcxVwARsM7JDxDASaUbujgDHW80JToNKCi1Kove6gkuSJlvIopsgqFa-QjD_-vGNvDeMDPfteNVXDDAG2c6IGKW6XDqHik5EukAT9FqjzZQH5FI2IzyQ_kej1HONuJ9QjZhu-040RCGwRl9tSgXdpR_ksgSjOd2o8R4DWP7KYrPLI7A_E5VXnbKn1PjXW4ViFNXmJBuMmE-jOoTOVTiV3JN9r09nb8OeBy-RBS6Kry7eko5s0tGfqfvYlFpy5AhqU7QfTWQt-xAtjpNusQS8pZkdVW4Xuv9qyywlRPiXjguFq10GkPAwE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc200fd510.mp4?token=KcI95bPPeJhbrJIkbo9q1QQefigXAT-eYYKjXkIm6Z2WzxK-Ge3wll6GV9Js09b0isCQj_GytrAsOS6825WJnw6-KBbjw8PDgyicjkkGEYDHEeZLq6P__UbVT5vKaa_abiizREVBFHBM-KCwMxSnfOUvuH7KuxDGpu3vrNMsroNzoaoJjR_4GGBqDj-TJ0hQok4OYyq0iFxt6OUTOvUYaknmn1fgA6r2WVg42PeP8Q-rO7jhTyrOFgTpmw3gGK_qoKsvb3xAJpcEjZG6l0zYBW1I-rX7UTnr8Ruxpf-wWSvQAMA7JHhQ2m5lCV8MInoiYS04f8gvMYFN9uwWMzOT2hVEebqnbHsAOukWMDWGGTJNlMB3fAkA3MRcxVwARsM7JDxDASaUbujgDHW80JToNKCi1Kove6gkuSJlvIopsgqFa-QjD_-vGNvDeMDPfteNVXDDAG2c6IGKW6XDqHik5EukAT9FqjzZQH5FI2IzyQ_kej1HONuJ9QjZhu-040RCGwRl9tSgXdpR_ksgSjOd2o8R4DWP7KYrPLI7A_E5VXnbKn1PjXW4ViFNXmJBuMmE-jOoTOVTiV3JN9r09nb8OeBy-RBS6Kry7eko5s0tGfqfvYlFpy5AhqU7QfTWQt-xAtjpNusQS8pZkdVW4Xuv9qyywlRPiXjguFq10GkPAwE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
جزئیات بازداشت عامل انتشار لایو ضرب‌وجرح دختر جوان
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.73K · <a href="https://t.me/farsna/453532" target="_blank">📅 12:19 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453531">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68ecf9958b.mp4?token=fnpcoYplsKZLHmSSxevCco8u4QKGkEGiMDzZOabWxU4Y5rfITFXYJLTPnqj6ohbbQ8hxKpzV-t22aSTIH0khwTXhyjHqTXwz--zSF3iE_X8pKdzfylKY8pxYrVi83rINZZIYUe0exN-7xLIsCZ6YZK1vOw_t8PNPqi4fKJjvjdTxAxfOHqMAapW-5YgmIO0ccQc8nySfhvNgUQ5l8EpeU3ueaAfI45pGY5u3XFdOaJ3Mrh4hTMAShEoUYzNT1Jr8qI0GbTw_1JXHBYfs1O59uLCZ1CK67KapYTcSmtpujQ93hxgSGRwQZZh-Frs9OZPXL_5arS69NeQnSSpmnkzrWiGJLt6_Qgd5uOIhztusbMbiSTEV_TBsZfp-PTrSSK7gBIjyyJCK-TvoMtJuDgPxVZL0o537hayZJzV7TUKjqVxdMOP3eldrkCjPmgJoxIRx-vyKsY-QPDizMk-YorEHmoYHbsG0MUrAMVYQNdJDj1Qcn9r3PHRmCzEsIhnkc5xFHYxYaZmBD1pMC37YyAdYJILE-pyo7DHMxMJmJeV9D26Qo7iuGd1jmla55fQp9jJJnITx4VE_O0vq9rrRLjIr41h7a73H1wfRCirssx0oIGkzTveOgQ6pclhwWZJ3TRVFLs-_Y2P2N0SIcV3z_sgmcbFzfSfBIb5aBBSl4EytoXk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68ecf9958b.mp4?token=fnpcoYplsKZLHmSSxevCco8u4QKGkEGiMDzZOabWxU4Y5rfITFXYJLTPnqj6ohbbQ8hxKpzV-t22aSTIH0khwTXhyjHqTXwz--zSF3iE_X8pKdzfylKY8pxYrVi83rINZZIYUe0exN-7xLIsCZ6YZK1vOw_t8PNPqi4fKJjvjdTxAxfOHqMAapW-5YgmIO0ccQc8nySfhvNgUQ5l8EpeU3ueaAfI45pGY5u3XFdOaJ3Mrh4hTMAShEoUYzNT1Jr8qI0GbTw_1JXHBYfs1O59uLCZ1CK67KapYTcSmtpujQ93hxgSGRwQZZh-Frs9OZPXL_5arS69NeQnSSpmnkzrWiGJLt6_Qgd5uOIhztusbMbiSTEV_TBsZfp-PTrSSK7gBIjyyJCK-TvoMtJuDgPxVZL0o537hayZJzV7TUKjqVxdMOP3eldrkCjPmgJoxIRx-vyKsY-QPDizMk-YorEHmoYHbsG0MUrAMVYQNdJDj1Qcn9r3PHRmCzEsIhnkc5xFHYxYaZmBD1pMC37YyAdYJILE-pyo7DHMxMJmJeV9D26Qo7iuGd1jmla55fQp9jJJnITx4VE_O0vq9rrRLjIr41h7a73H1wfRCirssx0oIGkzTveOgQ6pclhwWZJ3TRVFLs-_Y2P2N0SIcV3z_sgmcbFzfSfBIb5aBBSl4EytoXk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وقتی نخ و سوزن، زبان عشق به امام حسین(ع) می‌شود
@Fasrna
-
Link</div>
<div class="tg-footer">👁️ 8.1K · <a href="https://t.me/farsna/453531" target="_blank">📅 12:03 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453530">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">احتمال شنیده‌شدن صدای انفجار در کمیجان
🔹
فرماندار شهرستان کمیجان استان مرکزی: در ساعات آینده احتمال شنیده‌شدن صدای انفجار در اثر امحای مهمات عمل نکرده به‌جا مانده از جنگ اخیر وجود دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.08K · <a href="https://t.me/farsna/453530" target="_blank">📅 12:02 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453529">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r3s_Faz3sj1Fj_BGVLKNrYtTGZf1S4PNUtstSjkZ1Wp0YTyiWTxkY_Jl-QFJCtK4O55A8qxXIoWdXdVLr02Fps0desMUZe6PYal3BGmD1sBdJ6MnW8NTknVclUkAyotIFyU5Ng3rUsNc5c5P6PJ2ebncRrOT9Wf-7xt_N8jnYiBybdyqiSSHrd2meRSYWskkMjnpsxeqD5q83Mr6bQTNKXVAKW9sDZ5VewsFSt8Bl3o7JFVqA8faK2xhKgH6kPbDlCJmZ97aARYx6qv2kHFQgnpmO_cKyA8c4VgyUdSpe_rkwFkBWHk7REF29taAowqpMb-G4q2SdqU9uYmuWB7qbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زلزله ۴.۵ ریشتری در امیریه استان سمنان
🔹
دقایقی قبل زمین‌لرزه‌ای به بزرگی ۴.۵ ریشتر در عمق ۸ کیلومتری امیریه در استان سمنان را لرزاند.
@Farsna</div>
<div class="tg-footer">👁️ 8.36K · <a href="https://t.me/farsna/453529" target="_blank">📅 11:58 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453528">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/36dd50b50f.mp4?token=S4_Tq4N9XQnXVcpRg4fFgQKqXkjwJNNo1EJArMej2hpPb1X4ydDyCKFrABzT0UaxLMYI8s1lw7l7iD0hbwf3S4zovPRbx6wKlHuFdVh5n0jkmi_c7Pf4GcllhX6Vr51XUcfHxkmFszIvOiNi5GRzlWN9Qqp_aglsh_n1SKETI9dDaWjatc_oVNZ5fd_U6WJp7hSDIywP2vhSX8urNwtB06fNPQbR7t0LDWCkf2qanTfqXSF0g5nwWPf4VczLD5aYOmWPq_B8B1BRDQ6Zd39mUWd9POzQ5TnDPdt4hO_9Kd2rljolGYtO7K0wpLq_snRtvaPoqxaSc2W84IkwV5AAng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/36dd50b50f.mp4?token=S4_Tq4N9XQnXVcpRg4fFgQKqXkjwJNNo1EJArMej2hpPb1X4ydDyCKFrABzT0UaxLMYI8s1lw7l7iD0hbwf3S4zovPRbx6wKlHuFdVh5n0jkmi_c7Pf4GcllhX6Vr51XUcfHxkmFszIvOiNi5GRzlWN9Qqp_aglsh_n1SKETI9dDaWjatc_oVNZ5fd_U6WJp7hSDIywP2vhSX8urNwtB06fNPQbR7t0LDWCkf2qanTfqXSF0g5nwWPf4VczLD5aYOmWPq_B8B1BRDQ6Zd39mUWd9POzQ5TnDPdt4hO_9Kd2rljolGYtO7K0wpLq_snRtvaPoqxaSc2W84IkwV5AAng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هدیۀ فرمانده هوافضای سپاه به کودکی که خرج اربعینش را به رزمندگان بخشیده‌بود
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.36K · <a href="https://t.me/farsna/453528" target="_blank">📅 11:47 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453527">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EXLgvbo4X4Lantjm_w49CCcALbDIW16JIx2Buo5P2YXFLQhb8rLaH2lhkN4hPebqM2XEQ1ncDMpF2NJbEL_ieFzufYXhSt5Pe_m5Iq2xs1PErdmthfo5T-Qst7tHiDMP1OhJaVdUi2ecV7nOdR0Ph2IXRJ5OEFqUFQy2kDeY6aAwhdHJNhcxVR2bm9qBKnN_U5_WqBlIUbkcJC51aBWMDxe9Bs0dmxsNQ9ntZLBOurgUNnyxvappV6eWb-t32vViOEst7-I5ksl-WF-yYxeXO6lmQInrKcya9TN7f6eR0cfoXtZpzmEET8pvI7v9eiEtsNZYuMWUuNZ6mTGHQuFTLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عراق: تاکنون ۲.۸ میلیون زائر اربعین وارد کشور شده‌اند
🔹
ستاد مرکزی زیارت اربعین کشور عراق: تاکنون ۲.۸۸۷.۳۰۵ زائر از کشورهای مختلف برای زیارت اربعین وارد عراق شده‌اند.
@Farsna</div>
<div class="tg-footer">👁️ 9.41K · <a href="https://t.me/farsna/453527" target="_blank">📅 11:33 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453526">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1ed34a262.mp4?token=GVfwLjExTtwKvkTwzlhVWrQBSwY33vLhqI8K3jHDB0xtSvotDh1pfKiTFzNvffSAO8FULRc0AlZhbXLqVvgm0Ct_P8IggWueadKtWPkbYmKrIRlNaCLj31FCxHvTvv9hW9E13iaUEgxRpsTjAA4Mv1k81FCk1UddB6wPxfrcFwvaji42_isGsW5Ta8pLeJZejxiYh0lqmvSeytb2lRBDjyQb6Rk36dn7PAHa1h9Ux2UrJBbedZNll0vzaah-pGqWEDBY1QCpvCWvbKA3gAX-3gJihowKhaiGiRZu88QFhJOWGe0BFusFLQj6LZRNRpWTMlUDLVZXCoCB7bbcGwge40up2n8p2p38GswWAdaPhBGB7coaxa5NzFKLAHXIjP3YoPM-grivfmQwf58z9C_DPyp16QHWTv2tchjeymBC5X4jgLR_DdK14ts07lHJ-NYVVtI7hnSJcPYQrzPLV4KKeCXbJoe2zTCjGKiGqDQgtHTDOMjptYdHkMqmBoeUTTwIqjLY3u-7wkCAjKMB9EHN7uHnjiUuvr06tdqsKdF8udeo85rUcM6jC2DTEoQtOtVnF_WjJ0Z1fskixbUpmgb6YiozQOPqd2DCh1YuY4Mt5k9ZxMlEu9-3ZQ1wQfhYyJU5HzalmVXjE-hz9lyFdnUBI8QFaAAIfq8M2pYgx1Mbwns" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1ed34a262.mp4?token=GVfwLjExTtwKvkTwzlhVWrQBSwY33vLhqI8K3jHDB0xtSvotDh1pfKiTFzNvffSAO8FULRc0AlZhbXLqVvgm0Ct_P8IggWueadKtWPkbYmKrIRlNaCLj31FCxHvTvv9hW9E13iaUEgxRpsTjAA4Mv1k81FCk1UddB6wPxfrcFwvaji42_isGsW5Ta8pLeJZejxiYh0lqmvSeytb2lRBDjyQb6Rk36dn7PAHa1h9Ux2UrJBbedZNll0vzaah-pGqWEDBY1QCpvCWvbKA3gAX-3gJihowKhaiGiRZu88QFhJOWGe0BFusFLQj6LZRNRpWTMlUDLVZXCoCB7bbcGwge40up2n8p2p38GswWAdaPhBGB7coaxa5NzFKLAHXIjP3YoPM-grivfmQwf58z9C_DPyp16QHWTv2tchjeymBC5X4jgLR_DdK14ts07lHJ-NYVVtI7hnSJcPYQrzPLV4KKeCXbJoe2zTCjGKiGqDQgtHTDOMjptYdHkMqmBoeUTTwIqjLY3u-7wkCAjKMB9EHN7uHnjiUuvr06tdqsKdF8udeo85rUcM6jC2DTEoQtOtVnF_WjJ0Z1fskixbUpmgb6YiozQOPqd2DCh1YuY4Mt5k9ZxMlEu9-3ZQ1wQfhYyJU5HzalmVXjE-hz9lyFdnUBI8QFaAAIfq8M2pYgx1Mbwns" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بدرقۀ باشکوه شهید خلبان سرتیپ‌دوم مجید کاظمی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/453526" target="_blank">📅 11:13 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453525">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d83d01baf.mp4?token=QlSKKEEzCx8gT8o_eRvXIcp4OCeLmOmFZSJkICjQ3GuZpFMZN6q945D5I6acf8lbsGDQ3zPqSrVKrHhG72dkUsNs9_-9q25YyX3RQKZK15BVM-KqJBt34q8_i8D5Ni75Iej_wYlMoC9lXj4bP9O-I0ukNtq0GU5claHAduv0ibkCaXNHbEcxNJdqvYRPoV7L7EkoBVXe9RfglZgsnoFP1cxkn46c6h1PQmF3Ch3avNoYW8qHyxOcmaJ_g-I1Brko4uB7shA46Zw_SPJIKqx74rzA8ZWNayTOPvMP4qHoBDBhH3lxe0HMkKhS4ZpvxYkr4AiEFxWqiruLCe-yUq2dlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d83d01baf.mp4?token=QlSKKEEzCx8gT8o_eRvXIcp4OCeLmOmFZSJkICjQ3GuZpFMZN6q945D5I6acf8lbsGDQ3zPqSrVKrHhG72dkUsNs9_-9q25YyX3RQKZK15BVM-KqJBt34q8_i8D5Ni75Iej_wYlMoC9lXj4bP9O-I0ukNtq0GU5claHAduv0ibkCaXNHbEcxNJdqvYRPoV7L7EkoBVXe9RfglZgsnoFP1cxkn46c6h1PQmF3Ch3avNoYW8qHyxOcmaJ_g-I1Brko4uB7shA46Zw_SPJIKqx74rzA8ZWNayTOPvMP4qHoBDBhH3lxe0HMkKhS4ZpvxYkr4AiEFxWqiruLCe-yUq2dlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بامداد امروز ۲ نقطه در استان فارس مورد حمله آمریکا قرار گرفت
🔹
استانداری فارس: بامداد امروز دو نقطه در شهرستان‌های کازرون و فراشبند هدف اصابت پرتابه‌های دشمن آمریکایی قرار گرفت که این حملات هیچ‌گونه تلفات جانی درپی نداشت.  @Farsna - Link</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/453525" target="_blank">📅 11:03 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453524">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🔴
روابط‌عمومی سپاه پاسداران: با استعانت از خدای متعال، متجاوز همین امروز تنبیه خواهد شد.
@Farsna</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/453524" target="_blank">📅 10:55 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453523">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🔴
کویت از حمله به شمال این کشور خبر داد
🔹
ارتش کویت اعلام کرد درپی حمله به منطقه‌ای در شمال این کشور، یک نفر کشته شده و خسارات سنگینی به محل اصابت وارد شده است.
@Farsna</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/453523" target="_blank">📅 10:49 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453522">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TLsTcV54FoGy8OmBIBGdPjnz9nc8w5S3U5Xv9yMemdY30JTdGBPJgw4ImmkxIxdrBHXSmmHBDyJN2hLg_VCvRcgJdW1FGYUwYWTTLJSYmYRX2qWlaP141-rOc-d9-wrk7So_kwvA7HFWJVwsLHuEtdIgxzT4JVLTXvWj4K3wA6Fh_9SP1408tpOiDh6jV5i0bhpwEMzDfHw3TKLf03HARJSzTj1AbmOASiQNH17g2Kx6rwD2m9qnhWLtwvEgRh5VxHL0Xi9kp7cD57ojzyBpP2rFkqatGsAlYmWPr5-NJbZpNAkKgkZCcTuUZSo-CdE3R-OW668A7hj7RqoqdMd0jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شهادت یکی دیگر از مأموران فراجا در ایرانشهر
🔹
پلیس سیستان‌وبلوچستان: ساعتی قبل سرنشینان مسلح سه خودرو سواری به سمت مأموران انتظامی در شهرستان ایرانشهر تیراندازی کردند که متأسفانه گروهبان‌یکم میثم کرمی در این حادثه به شهادت رسید.
🔹
اشرار مسلح تحت تعقیب پلیس…</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/453522" target="_blank">📅 10:45 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453521">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">دقایقی قبل، زمین لرزه‌ای به بزرگی ۳.۴ ریشتر لالی در استان خوزستان را لرزاند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/453521" target="_blank">📅 10:44 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453520">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">محدودیت‌های ترافیکی فردا در جاده کرج_چالوس
🔹
راهداری استان البرز:  تردد انواع وسایل نقلیه از ساعت ١٤ روز جمعه از آزادراه تهران - شمال به سمت مازندران ممنوع می‌شود.
🔹
همچنین فردا از ساعت ١٥ تردد از ابتدای پل زنگوله به سمت چالوس ممنوع خواهد شد.
🔹
تردد از مرزن آباد به سمت کرج و تهران نیز از ساعت ١٦ فردا به صورت یک طرفه خواهد بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/453520" target="_blank">📅 10:37 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453519">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lOn7qPkUHoOR8j55VIojOFgnMWloRe1hGtTW71YlFOmJHQx9yf4w69wXtERNbx_V1Nek5QsJ7R_kmaEL9Uz8MM7Z_Ewfqp1d7e3IMhgkMW9GP2PA--L8wb85qxyphBWOsX-6224PLWFwuTLtU4FfukL6cgV0CdZjzoaAxOIDBaFg2IMD_vkvUzDujIwUN4Jr4jd-JndzZIAGuXAukp0WcflIYcrlGjTaRp7ZLeU1wPwaLRP9Sh-B0CHNULatLhK6GpsWpo7BvZ6wIUhXyMpqdzNuuEWpKVxXo_FDxjvnOIsiPHvDDvWKjS5xyaGKI1WuZoDg9bYdI1Ug9yn84Nqp2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نوبیتکس سرمایۀ ایرانی‌ها را به شرکت اپل برد
🔹
در حالی که آمریکا نوبیتکس را تحریم کرده، این صرافی امکان سرمایه‌گذاری کاربران ایرانی در سهام شرکت اپل را از طریق رمزارز فراهم کرده است.
🔹
یک شرکت آمریکایی مستقر در نیویورک که تخصص آن ردیابی رمزارز است خروج سرمایه ایران از طریق رمزارزها را بیش از ۴ میلیارد دلار اعلام کرده است.
🔸
وزارت خزانه‌داری آمریکا تاکنون چندین بار از طریق همکاری با شرکت‌های ارائه‌دهنده رمزارز، کیف پول‌های ایرانی را شناسایی و مسدود کرده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/453519" target="_blank">📅 10:15 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453516">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lJqxheC0pPAIOv5cPzF744kGCnBtKmV-Jq_EPNmU_ezhiFdik0ogGcJNwv-Rb6kDftpCU2OTqmVVvSPVviJioOp0rfnZLGuSYv0zlKEGoDfc6Zfo9OY_gJX3muzaCFaDYn4i51BGaBeVHfrJYRbB9klZpW9ikxuPruALXAxwylvgx8CHrmtXpG36HMuqAmLjzA2A99F1hSwywJ67oBYCjYH9lYn-EzfsFSgH-9_BLX0BXBOJI0aK1mQi1O9E5a5LsJeQIIl0kxY_NLle2wT-c7bj39MtdvQsp5xq1NDuItTd0Ma2yx4a9Yas6LAnVfcfdq3w0ndeGJEO1jvnaE3ZUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lHj15x9Co-xX_7jPF_f7h9X-AvrGXJS1TJksb1iBdFLu9j_SaVVxbGEJRRkTGyjXzFtMUyvA3HLfSmc5hur2zEobLwAR_zQhcEYJXu9RDDzh2wL9xVGJT34SG686rpF5jcty67--9L_kAO6PsOsF2DYhc-rQ5VmAgDoS5EEYVyNE78kaVdZSiMMZPSZFBXbHkSHLWgqh0pnNaWxIiyAN3GMv3Q5qFL_Rha5P-Ig8iH7BM9vHBBadWSVdtaWkxL125o1EvA3QwYRnHDGjEbWAWy-pM_6fAxdQCJFf3mcrJDv3yRJFnbNBxfkvEs8KvKvw1zZlQKWZP42SCpF7MRwNcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L33gakBKhWmx2V7s6NKx63bDmfU5xzGJD-iOVNCRyNeOrAqSbccq-_iJeyYlmYhTZdkn-eTRCArPqhUbt966cjgstrcJBKeZSGsmmkHcezS3CEcv4g_VZKuk8bloXEsobg4PLFA1RUSVEgFMmck4v4mQuHmxM9D5F9ZT0gLIaxWJxHwFtj9aCnUcjTmFmKx3A6HAcmA9_WHwESoT_vYcF69yNlQNihNUNG0Y_-Za3eYPQu-EK4K3CRMVGXDMoApe9gnwU506oHjsJermPIQDfnj0UrafhU-rSkPR0TBK8SX4YmF4hKrq1GiqFywJqkhRvaltbhn42ZodG9VEKufVGg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
تصاویر هوایی از پارکینگ مرزی مهران
@Farsna</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/453516" target="_blank">📅 10:01 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453513">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K8JMe1xWolhxTWsiigAX34WARMg2oIAOesRKgrY1HQOQW5Jyn3VCIzAh3KGqjeGJOY5LO19Do4hsIJ-NEaHCaoKrI8TUS7SYdGk62mMP7jHmBb23BNSm0tjvkgxrhSy6vZ378EWzOpo7R95yrIe33dJ8qc6rE7XiYb-UIqN6IT47DR0auR2Jh1FjxIgIt_6FDKq3-HuifynL1IlRBuHr_-D1BZjF4wc_HS8cQiLi5j4yDnMeQz427T5deXaDCBvq1fHiiee_uUbjWowSQwtUKYX49tXZgkRQjruYKwPcNXjzvhOB-hJTG8En13KH5mnrCYfEKo1Kb5upATTrtJdi9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جزئیات برگزاری پیاده‌روی جاماندگان اربعین در تهران
🔹
معاون فرهنگی سپاه تهران: پیاده‌روی جاماندگان اربعین امسال ساعت ۶ صبح روز اربعین از میدان آئینی امام حسین(ع) آغاز شده و تا حرم حضرت عبدالعظیم حسنی(ع) ادامه خواهد یافت.
🔹
«اجتماع بزرگ خون‌خواهی رهبر شهید» در ابتدای مسیر برگزار می‌شود و با توجه به اینکه اربعین امسال را در امتداد تشییع قائد شهید امت می‌دانیم، شعار مراسم «باید برخاست؛ یا لثارات الحسین» انتخاب شده است.
عکس: بهار قادری
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/453513" target="_blank">📅 09:56 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453512">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b892f32cf.mp4?token=fV9ixEdOQ0PAOfm0b9q5eO2rcab8iTDrvbUnfT1NFC7GXkMqfvHDr6VZ80NmR9KU78mgjqk5CJBYch9KfWd86Uk_9OXEP0P6IhHau58ybUqTmr93L5WUlC5VFSGsq-vynNRnHCQ040rbkgm-5tct_wuOpqDP2hmrtf0BZQsBI0Ml5XZ7wzeCZvCuT6E2_44QEtPFlZrljzta6DkEuP0T4t3tnhoxmoaEsdY7gouj0VvNpZUVZXjsrvKH0xjExbnLuuiNL5zQt3WDSYrnUk68kJtL9MtF8NyIADvhR2VMVZf8BI2C0lF4MBkeUHZ-Hlv7FC-llZCyS7q58Vx2BOPkdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b892f32cf.mp4?token=fV9ixEdOQ0PAOfm0b9q5eO2rcab8iTDrvbUnfT1NFC7GXkMqfvHDr6VZ80NmR9KU78mgjqk5CJBYch9KfWd86Uk_9OXEP0P6IhHau58ybUqTmr93L5WUlC5VFSGsq-vynNRnHCQ040rbkgm-5tct_wuOpqDP2hmrtf0BZQsBI0Ml5XZ7wzeCZvCuT6E2_44QEtPFlZrljzta6DkEuP0T4t3tnhoxmoaEsdY7gouj0VvNpZUVZXjsrvKH0xjExbnLuuiNL5zQt3WDSYrnUk68kJtL9MtF8NyIADvhR2VMVZf8BI2C0lF4MBkeUHZ-Hlv7FC-llZCyS7q58Vx2BOPkdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
کارشناس مسائل بین‌الملل: زدن مراکز غیرنظامی از سوی آمریکا بدین معناست که آمریکا در حالت تعلیق طراحی استراتژیک قرار دارد
@Farsna</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/453512" target="_blank">📅 09:35 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453511">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/czrJGtgbqWisztGokWMq71HQAOnjKy9BXjRfUTMEw8p7d96rxKouMboMR-aMf4VVEWP7I2XF_l1KwTYhxRUSHDy2oIpG9JJiMAFnu89q2d12ICQ8ctzvrUnvCkPEY-JFNu_OYNL-5XEfUUkcpkI1AinN2V8ltkrSYamR4MdQee3TBEDtvug-7w_MXUYnta0V_YcTVAtEq1-93Wx0PVka9NYXOugM7EX0eZe_ns9tg1Ucdw2Ma0Vhd03S7Hs2qbYjDeF5wizECq4tg7oWtiH_DeHJu4EGrh7Uyww_labAnvdo6H2Qo2l077EeKt0t3-pOfOzlV2cwxnl3XYmfiKdr4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رصد پروازهای مخفی بر فراز اردن
🔹
دادهای ناوبری هوایی نشان می‌دهد پس از ناکامی آمریکا در رهگیری موشک‌ها، هواپیماهای نظامی آلمانی و فرانسوی برای رهگیری موشک‌ها به سمت پایگاه‌های آمریکا در اردن به کمک واشنگتن آمده‌اند.
🔹
ناوبری هوایی فعالیت حداقل ۲ فروند هواپیمای پشتیبانی نظامی در آسمان اردن را تأیید کرده است.
🔸
نقطه‌زنی حملات به اردن و گرفتن تلفات در حملات چند هفته اخیر، مورد تحسین فعالان رسانه‌ای خارج از کشور بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/453511" target="_blank">📅 09:29 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453510">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">شهادت یکی دیگر از مأموران فراجا در ایرانشهر
🔹
پلیس سیستان‌وبلوچستان: ساعتی قبل سرنشینان مسلح سه خودرو سواری به سمت مأموران انتظامی در شهرستان ایرانشهر تیراندازی کردند که متأسفانه گروهبان‌یکم میثم کرمی در این حادثه به شهادت رسید.
🔹
اشرار مسلح تحت تعقیب پلیس قرار گرفته و در منطقه پیرامونی طرح امنیتی-انتظامی در حال اجراست.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/453510" target="_blank">📅 09:28 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453503">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IH4d_DHtHT_fleqTAQLgu1a9LCmzFj10wOLECmsO27b7CkflGUEXDkmbBsGCL671w_BRgMlboRfUILeqJlc0LSQ_h0FsLKGMLGcn5n_ifTgCWTLxeq0ld1_Xf-r3J3Sx5ZuGjXDhaqzf31QWUhLaTwSmS42EysqOz81ZF6CsIoMFQxPwL3jP8KUWBGkQVwTO-L6vn2ilqYW7PCX7Z57ppXNrY8lZ0TzcIWxc7SFGlQ-FinQgjcfN_s7T-crAY2xRMHbOVeNN5h_7LccRAxHiQ0JeGi2kINQGjEEBdEbl6TqFnm8sL73QtYEMwuvdc7B6RUEtywiMr1CfD3_c9pjeHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C7-yJSwiBUBDAa0nRyrs6GgZCRR58vSFRmEL54ejD2NeI7z5TWHHRRckBpXbc4RMlDGeoOYsVDRvnI8hAKziQFmBPYG3xoXw2mbZ1YZzLZvirZwNaPW_90zwhafP6QqGIPcE94OJP1Pr0ahEUOmgPaFOG0rl3Iil5m0DQcA9i_zdKYm9o4pJegV4QL6fns7nf102KPd7qAkXltedCEaWAFJiX354OJzStYMmNWdtGuU4MmB7kOaeuzXfqLP9QAuXWRmnTZwGwAWPf7J-uz1hnYxAgiEAGU10-EGDBBHSVlQ78mACUsUi11QDKpgVAZ_PDR8UT0ztFhCtLv-_prEXuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oraEwWWtVDmR3FcDUhr0F_Y3I14IRGK7ftf16Duopz8wXoYMyXj6_VK6uDZvGvfsjh9G9kn4i2cbqgKyZPDyrygVfIP83pkJY3cpfRej3HF8ZYXSt6lPc5nyLGk6wZHrbQXMAhLkDjx8uaFhqbOU7MlKLRgz1a9ckknwwCTMpiFkdU3yfkOFJRjB7jSOteykRlWlGgirsXlNe8dhmgvoiZf9gtyDgbi8SmQ_-qs7r2sgJdTRRcwx7z_W4XxgYaZe9FGwywgh21PZqULjwtmePNjNlJZCWndDTsRvNSnEh-k1Jy8YhjwMC8PDvlrgpgbk3xLkWe4OnN2EAmwH2gqxkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TO0NH0mZkVhL8YKm0i8wdVo3Q5zr5FWzvMlkYfc-Y5q-otqapuD0m5a6VH8H7VN0ZxFoKslg-IPMR2B75uRRCtmDlSxuraYcy-o_zNXuz9R7df9X4K6xPULDI87277bzbxtfRsODrIEWqf0XlHSWdrEnxyu3Bd-R2mG4FiRkKwOzC8ps-uvBAa_AFJzV04jTrQ_FuR2sJ84_51yH-h2dtoHlVDN76rfd53N24ssPLivLzRrNDWPotwncJ3IhluHlJfvZbifqqQkr2gV75-DYaoJER0pkouRdlC3rLpyYRDMg31gJKHzJrg0Lj8Mza2n5m-uZw7Yq1sLNF6ia_fpK3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y8YFfXcylR_QEpDibFGg5LacLMl2HQ-zxHLJ3NxStQwe1gco6Z4pC_82QeryNZBiEursiktGDKDMnoLnt2q-QSm_W4ac6EEsUdh-C9RDCK2h8mTNME_eE2JR2A_9VpQxyhTeV60ydX8fX_ypFOlkz8AZiJPChsTPWmegEloRCa73mAuZHiMljIKscveWi6khy-eDljEYVQed5GIenXZaxhjSC7jJ1yyBG0_FphMSSHZWxnT1sUsHOjLDf8XVbiopWue464KwYkO7iBIQw9e4wpUy8f4MjOFOLZAEc3xTwmJTD91chF_EnlaFmHFnTXrdbBp1m7BJ_OjxWBhft8bj-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VTI6XbwfU5LgU9fykWKUXC-gne6NJw-4kxuMZDJvtlrN12-MVwWvck2zGgz8zjMeuYqnhdnda7GYHDVZ0QrJCcBAskCWpl40xAWDy4FCzV7Rdv8w5HFoYQ4wiCfGHGVMGKzc0kIX5Zj27VxevdP_ioj35Co0_E4a1nbK-TH2iXif66EOLaKeOSbpGc1Sdw1uOFnLEhOWlz5cFiFoDDNQrDUfDmIvMj7nAR0qVaTKVz4hoC0-13F7kgqWDMih8GgVR4P4bWMmoBBHVrXDib_B1pD0ZrBnQ31DCwC8YTSr8vPV-DRcoMYFeL92E4WdZ2csl_RTRCbKqapHgz1_s2Rn8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DiwbgED2F07GorziJDECLQ9lOidQDvela6sRwP8sVgUdA8JysX-m2ccFiBwK1EXswRlbcZ7_cpGC3_XcqJuQWb3yFrJLWKTjCLprntes8k-pkEEAOUTMogTV3C4GDAarrTD0UfSty5jutSSfE3g5IiBQR0Aik7m7jWO7vUFjuyXjUHvYWDvENxdWZX85bV6PlILgo_7SXmemxbfU55EeVuG7PdysNlVKUhSWkyyhrchFCCEL4CFjHyRyVUIj6zTPcQf8mT4gE_35RsYFm9lQNad0DNyZ5K1vH5DJUIYhheK6UWgVKytViqRR3_FX3bYqw_Voormt0G_OBbz2Nkc_wg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
توقفگاه ۸۰ هزار خودرویی شلمچه
عکس:
فرید حمودی
@Farana</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/453503" target="_blank">📅 09:24 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453502">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gX380HbOjKhj1EJc5PLsw4Ot6-2gzlQd7H4IHy6PAutC9qo2yKqu0Big7MDwua1QcgUiFp-M_vKXyx4c1pOCfb2w0t21wg0fkKnFlr2S78UNKK8IQbMSbPlzn3rsIiWK4jF3-WIFgUAowByllq9zGptxmYBnQuhRPoU4kvo2s9PBNWV5-dWgUwt9OpxD41bqb-xuUG39sf4IDvSLHG90okmutYEENe9Gtd2m7JBIqFUPjoXcN7uNLJ7DOuloS4rPXe5WwAm7gzJRgY0ibjTHwHdIM9-W-wh-MTSbRNwEWsGRRGiFqNwcJzBJyFTwLabLJZq__y0Y0u15Vsu26S5rYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عبور کشتی قطری از مسیر ایرانی تنگۀ هرمز
🔹
اولین محموله LNG قطر پس از ۳ هفته با اجازۀ ایران از تنگۀ هرمز عبور کرد.
🔹
سه هفته پیش تهران پس از نقض تفاهم‌نامه توسط آمریکا عبور و‌ مرور در تنگۀ هرمز را متوقف به تأیید ایران کرد‌.
🔹
این کشتی قطری با داده روشن و از مسیر تعیین شده توسط ایران گذر کرد و بدون هیچ مشکلی به‌سوی آب‌های آزاد می‌رود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/453502" target="_blank">📅 09:12 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453501">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🔴
منابع عربی از شنیده‌شدن صدای چند انفجار در اربیل عراق خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/453501" target="_blank">📅 09:09 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453500">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f116a0b871.mp4?token=AgeDV8QGklsLXRBNsoD0f0g7psY2G23bO8YHdgLpzmLHZaL3pcKvuLOwBf4h5WLkYpAIQQSZWEX9_R4WYs60bsYb7UO4HPDWTQHuTs3NYb4yOr35YDLFHH9CNJrw2r-mkzi-K4OFO4N95ft0LM_nQEQ7vTjGWcZxkVmB6NkUoUKiHLhzjGT6z_yjitBB38xyyaOyTu4ktW5YgZlq4Hs4q-vvIH4TER9e4Y8J_T_VhAkLcipWaO4zi3pyy26tK1srHEG5u-C7tMDWl6RtejCe7WcWFvHjwOBgRFBpytdeRRm1Z4lMPmZCS2mfB6nVzWdh7C1cP3Za0XWVTqXYs7t9_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f116a0b871.mp4?token=AgeDV8QGklsLXRBNsoD0f0g7psY2G23bO8YHdgLpzmLHZaL3pcKvuLOwBf4h5WLkYpAIQQSZWEX9_R4WYs60bsYb7UO4HPDWTQHuTs3NYb4yOr35YDLFHH9CNJrw2r-mkzi-K4OFO4N95ft0LM_nQEQ7vTjGWcZxkVmB6NkUoUKiHLhzjGT6z_yjitBB38xyyaOyTu4ktW5YgZlq4Hs4q-vvIH4TER9e4Y8J_T_VhAkLcipWaO4zi3pyy26tK1srHEG5u-C7tMDWl6RtejCe7WcWFvHjwOBgRFBpytdeRRm1Z4lMPmZCS2mfB6nVzWdh7C1cP3Za0XWVTqXYs7t9_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📷
استقبال از پیکر شهید سرتیپ‌دوم مجید کاظمی، خلبان قهرمان سوخو ۲۴ در پایگاه هفتم شکاری شیراز  @Farsna</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farsna/453500" target="_blank">📅 08:59 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453499">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">بامداد امروز ۲ نقطه در استان فارس مورد حمله آمریکا قرار گرفت
🔹
استانداری فارس: بامداد امروز دو نقطه در شهرستان‌های کازرون و فراشبند هدف اصابت پرتابه‌های دشمن آمریکایی قرار گرفت که این حملات هیچ‌گونه تلفات جانی درپی نداشت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/453499" target="_blank">📅 08:56 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453498">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🔴
سپاه: کشورهایی که در کمک به متجاوز دخالت دارند، اگر رفتار خود را اصلاح نکنند پاسخ سختی دریافت خواهند کرد
🔹
روابط عمومی سپاه پاسداران: مردم غیرتمند و به پاخواسته ایران اسلامی؛ عزم و اراده و ایستادگی شما در صحنه جبهه دشمن را در هم ریخته است و صفوف رزمندگان اسلام را مستحکم تر کرده و روح و جان تازه ای بخشیده ا‌ست.
🔹
شب گذشته دو تانکر نفتکش با تحریک پرنده‌های آمریکایی قصد خروج از مسیر ناایمن جنوب تنگه هرمز را داشتند که پس از وقوع حریق شدید در یکی از آنها هر دو شناور با سرعت به عقب برگشتند.
🔹
تنگه هرمز سرزمین ما است و دریادلان نیروی دریایی سپاه مقتدرانه کنترل آن را در دست دارند و به غریبه‌ای که از هزاران کیلومتر دورتر آمده‌است اجازه دخالت داده نخواهد شد. با استعانت از خدای متعال متجاوز همین امروز تنبیه خواهد شد.
🔹
کشورهایی که در کمک به متجاوز دخالت دارند، اگر رفتار خود را اصلاح نکنند، پاسخ سختی دریافت خواهند کرد.
🔹
تنگه هرمز تا زمانی که زیاده‌گویی‌ها و تهدیدات مقامات آمریکایی و دخالات آنها در حرکات دریایی در منطقه وجود دارد، قابل بازگشایی نیست و تهدید کردن‌ها و مداخلات، شرایط را سخت‌تر و پیچیده‌تر خواهد کرد.
وماالنصر الا من عند الله العزیز الحکیم
@Farsna</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/farsna/453498" target="_blank">📅 08:43 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453497">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/13626a5fd0.mp4?token=C9l-aHvnIVW4x9l_Yvggss_P6XAnPYMda2ygPJlPLGCQJvqDKSi5mWnNC55SNZmf_CVGlrqvcEE7XzS_xhdwjJRCXS489epallp50AIBp-ExlJFxLPTHwYIZP2Ygy6mmQqDIQ4Ql3FjDcKg-hhBuv4IUEGYHKGA67wlVCorVZfZTT4Iw2wDQLZdSsCZ85GmbjWoUAGqIZnDFAZrpXAHOBTidwTqSJUQrqbYoeoeEb_LPFjG1oN0JTvzF5mvCX6YO6fd43gGrqFDGva2AGWEVF6lCQYlyGfhp0XJXyzYxSI5fCUvEEuo2pGghqjqApXGRM5cM77mReix2l4F25BhABxl1kRh__w4fEEG4C1Yydoa7RoiHuAMb1z3g8BFIoQ3gLqovhTdhKpyadLZAe7lnzUHXHj1wWCErurCdLjwSHZVDIe1Wax0ZqoSYkkszADomuxd8GFGVNDhqcRjynLWhRdpad5yWJmxvNOfm-DnWWzDUovDiA1rYqnU3R1k46FJpotXCe_tjmB_yL2grlVlTUJM_q-v00dX9k00rCQFlVii9t0cDgjcIY8SUrDq2FEUwP6xa11pUrnunLuwYvPUCCDUFFhF20yAuVgvcfXTe74yARwO8uHIe83sXmFJzii2zNHMiBSQH9KkPSqo5YwKroBVpJT0Ii4TaBN0BzwjJLFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/13626a5fd0.mp4?token=C9l-aHvnIVW4x9l_Yvggss_P6XAnPYMda2ygPJlPLGCQJvqDKSi5mWnNC55SNZmf_CVGlrqvcEE7XzS_xhdwjJRCXS489epallp50AIBp-ExlJFxLPTHwYIZP2Ygy6mmQqDIQ4Ql3FjDcKg-hhBuv4IUEGYHKGA67wlVCorVZfZTT4Iw2wDQLZdSsCZ85GmbjWoUAGqIZnDFAZrpXAHOBTidwTqSJUQrqbYoeoeEb_LPFjG1oN0JTvzF5mvCX6YO6fd43gGrqFDGva2AGWEVF6lCQYlyGfhp0XJXyzYxSI5fCUvEEuo2pGghqjqApXGRM5cM77mReix2l4F25BhABxl1kRh__w4fEEG4C1Yydoa7RoiHuAMb1z3g8BFIoQ3gLqovhTdhKpyadLZAe7lnzUHXHj1wWCErurCdLjwSHZVDIe1Wax0ZqoSYkkszADomuxd8GFGVNDhqcRjynLWhRdpad5yWJmxvNOfm-DnWWzDUovDiA1rYqnU3R1k46FJpotXCe_tjmB_yL2grlVlTUJM_q-v00dX9k00rCQFlVii9t0cDgjcIY8SUrDq2FEUwP6xa11pUrnunLuwYvPUCCDUFFhF20yAuVgvcfXTe74yARwO8uHIe83sXmFJzii2zNHMiBSQH9KkPSqo5YwKroBVpJT0Ii4TaBN0BzwjJLFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عزاداری دستۀ بنی‌عامر در بین‌الحرمین
🔹
در آستانۀ اربعین در عراق، دسته عزاداری بزرگ قبیله بنی‌عامر که با پای پیاده از بصره به کربلا رسیده بود، بامداد امروز در بین‌الحرمین به عزاداری پرداخت. @Farsna</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/453497" target="_blank">📅 08:39 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453496">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🔴
منابع عربی: لحظاتی پیش چند انفجار پایگاه موفق‌السلطی اردن را به لرزه درآورد.  @Farsna</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farsna/453496" target="_blank">📅 08:24 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453495">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">‌ خروج دو کودک از زیر آوار‌ منزل مسکونی در قشم
🔹
مدیریت بحران استانداری هرمزگان: تاکنون دو کودک از زیر آوار خارج و به مراکز درمانی منتقل شده‌اند و تلاش برای نجات سه عضو دیگر این خانواده همچنان ادامه دارد.  @Farsna</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/farsna/453495" target="_blank">📅 08:04 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453494">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🔴
منابع عربی: لحظاتی پیش چند انفجار پایگاه موفق‌السلطی اردن را به لرزه درآورد.
@Farsna</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/farsna/453494" target="_blank">📅 07:54 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453493">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">دریای کاسپین فعلا مواج و تعطیل است
🔹
هواشناسی استان مازندران با پیش‌بینی وزش‌باد و مواج شدن دریای‌ کاسپین، تمامی فعالیت‌های تفریحی، صیادی و قایقرانی را تا ظهر دوشنبه ۱۲ مردادماه ممنوع اعلام کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/farsna/453493" target="_blank">📅 06:48 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453492">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KWJpH5_Q7AhoORlsBTY5ItbO4OEag7B0rGcM-4jlcp142ijjt-UPPIMDjXRF_bo0I0w9AqqOxbBCZVatw15YFI-YdH7x7DHUuOoDm0oKktRtYxoBBDDzDqzNu3tgC7irSiih9gpa66sR7PqlxxnRYUusMYutz462ppPK2YXlLXiftdkaUd05EsNbE5s2aSrFwA72OBYBsnRVGXephHOZ-1nZIoVDP0dBBp2M7FlnZZsnpdcaMLBXaiJUxTL-GOg9TUcBAt3DLqZVniHOXTmrM7B68FQN1R-OYIgZnE5zNEFcpREA1UsyLwo2fgezq8i4XDXopI15kUIV819Fz2izSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تردد ۱.۷ میلیون زائر اربعین از مرزهای کشور
🔹
سردار جاویدان، فرماندۀ مرزبانی کشور: تاکنون بیش از یک میلیون و ۷۰۰ هزار زائر از مرزهای کشور برای شرکت در مراسم اربعین حسینی عبور کرده‌اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farsna/453492" target="_blank">📅 06:19 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453491">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">📷
تصاویر اولیه از حملۀ دشمن آمریکایی به منزل مسکونی در جزیرۀ قشم  @Farsna</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farsna/453491" target="_blank">📅 05:49 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453490">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b-jvdjxNc4nBAklqaN9wMGaek1RxhTa9I8HbT7k8jxyGNfgv1M5H2zpZOzBp9zv2J15xNa29tHesgC6uhYiLoMpylSf7kMT6dlEBY42QZVFxMQxAYQKQYsyebA5M23GPSGsgLGZ6nUl6gaEHfxXZZG7kWaSyvgoVwLwcf0VvUKlYh8cEGIjs6v_tITHrT-xfIUApf1udjUUJ3O-ntlyLtDFSHM81nV2F9-A73c0UMHnDRY69M6t9ZbcYyTATp6cunTGtb8pVXqYDD3xOm-0bsbmL2G643_zMPEah5Q-1IGk17mDXDvtgvzrigKcTbHSn41apci5-hlfaymNIrYbSkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ادعای آمریکا درباره گسترده‌تر بودن حملات جدید به ایران
🔹
نشریه «وال استریت ژورنال» به نقل از یک مقام آمریکایی گزارش داد: «حملات آمریکا منطقه جغرافیایی وسیع‌تری را پوشش خواهد داد و گسترده‌تر از عملیات‌های هفته‌های اخیر است».
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farsna/453490" target="_blank">📅 05:33 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453488">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/f5d_M6EeYcn2JiSAYrOqcyaH9ZjXoM0JzEJJH9Hphl24LgsNHQZrHlOQs-qs0qHl3VT4CcVhPcfbqzq2vs61LuT2464UYDBpQ5iZvt5CM4EmXGKcZv6YhlSYasxcV-vbTPoJa_DpqhNBRMNe6FdB6uPx_uH97mq8fN8H9KzhuBLwSy3rF_Tfb6Vets6JvqbnwJ0cx19mxx1pR-Q8h4WnOEGqzkMrP0g-FPvA9DQAYL7rCCKeg4jmU1p0PgrdfoCYN1BScug_LLI5NdF-AH3dkGcPgRxb3P2pwijDr9MigElnn0mzgdYMlzKtAkscUVroGZnj9Rr4OvO2UUy1bvrx4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GCDd5l2gWiuImxF825anl493vuanapfrK9-83OuTopQaZJz4-mnzQA45lo2PpvrFaXgUXZUpWuKbomjo3I2zzzdRAbDYYCn4kF_ACcQr6deQ4oSvRwMLZzPAPRVJMVDriWrHeN5XnGjpxRYltAbtMksvOq8n-WYdxQCczGIJaTDm7LYpohTAzWpg4D8of5E9LCk158Pe700VAEkD7_uflt8X6mOWaHAajus76v8lq9L07uuubb2sGvIqZRQzN5wVWMEJT-FXWzYJrkO73WghFzYo7T4nqhF19ZzoZ2IapuCCSkEgkvjqCEhhMZagGqwG-oCQLoyAuVL3bCCZIUlOXA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔴
حملۀ دشمن به یک منزل مسکونی در محلۀ چاه‌تنگوی قشم
🔹
معاون استانداری هرمزگان: عملیات جست‌وجو برای یافتن اعضای خانواده از زیر آوار ادامه دارد. @Farsna - Link</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farsna/453488" target="_blank">📅 05:29 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453487">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🔴
حملۀ دشمن به یک منزل مسکونی در محلۀ چاه‌تنگوی قشم
🔹
معاون استانداری هرمزگان: عملیات جست‌وجو برای یافتن اعضای خانواده از زیر آوار ادامه دارد. @Farsna - Link</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farsna/453487" target="_blank">📅 05:20 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453486">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🔴
حملۀ موشکی به نقاطی در اطراف شهر اروندکنار
🔹
معاون استانداری خوزستان: نقاطی در اطراف شهر اروندکنار توسط دشمن آمریکایی مورد حملۀ موشکی قرار گرفت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farsna/453486" target="_blank">📅 05:03 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453485">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🔴
نقاطی در شهر اهواز هدف حملۀ موشکی دشمن آمریکایی قرار گرفت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/farsna/453485" target="_blank">📅 05:02 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453483">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/36195e2362.mp4?token=vMHPnuUAEA1n6VFJt_vnXt3XGK4GHCDwj3a6ImqVtjRk1CsFrNAqwn8ONK2WrhqQIvmODVUX7DJ8YDhu2Q6PU6orPaLYTd3q-D52E3j_DnPnrQbo5kHx2FXexBehVcj_OcvfSf8FcSiABISX854hyhv3r_-kqLU0wruSfGaUTSHzGTGf9p2a-QWiIczkRfyML6DtnRwkDiGYQYAoPu1ErT4ZsiFrwjEYtsxLyrKq6g2D3dB0B2vSA5CuHBYx5AAsxGCyoAD-p1Na2gZbsbBPtsTgqscfI7DeMh6YZa0ZGAhrJOwnkwTp4RorGcHpDN6n6iHUk3AaYdvKDuIkfxhWfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/36195e2362.mp4?token=vMHPnuUAEA1n6VFJt_vnXt3XGK4GHCDwj3a6ImqVtjRk1CsFrNAqwn8ONK2WrhqQIvmODVUX7DJ8YDhu2Q6PU6orPaLYTd3q-D52E3j_DnPnrQbo5kHx2FXexBehVcj_OcvfSf8FcSiABISX854hyhv3r_-kqLU0wruSfGaUTSHzGTGf9p2a-QWiIczkRfyML6DtnRwkDiGYQYAoPu1ErT4ZsiFrwjEYtsxLyrKq6g2D3dB0B2vSA5CuHBYx5AAsxGCyoAD-p1Na2gZbsbBPtsTgqscfI7DeMh6YZa0ZGAhrJOwnkwTp4RorGcHpDN6n6iHUk3AaYdvKDuIkfxhWfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هم‌دستی کویت با دشمن آمریکایی؛ شلیک موشک از خاک کویت به ایران
🔹
منابع محلی از شلیک موشک‌هایی از  خاک کویت به مناطقی در جمهوری اسلامی ایران خبر دادند.  @Farsna - Link</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/farsna/453483" target="_blank">📅 05:01 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453481">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🔴
حملۀ دشمن به یک منزل مسکونی در محلۀ چاه‌تنگوی قشم
🔹
معاون استانداری هرمزگان: عملیات جست‌وجو برای یافتن اعضای خانواده از زیر آوار ادامه دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/farsna/453481" target="_blank">📅 04:45 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453480">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🔴
حملۀ موشکی به نقاطی در اطراف شهر شادگان
🔹
معاون استانداری خوزستان: نقاطی در اطراف شهر شادگان توسط دشمن تروریستی آمریکا مورد حمله موشکی قرار گرفت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/farsna/453480" target="_blank">📅 04:40 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453479">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🔴
دقایقی پیش صدای چند انفجار در کیش به گوش رسید.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/farsna/453479" target="_blank">📅 04:35 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453478">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">هم‌دستی کویت با دشمن آمریکایی؛ شلیک موشک از خاک کویت به ایران
🔹
منابع محلی از شلیک موشک‌هایی از  خاک کویت به مناطقی در جمهوری اسلامی ایران خبر دادند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/farsna/453478" target="_blank">📅 04:35 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453477">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🔴
شنیده‌شدن صدای انفجار در بوشهر
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farsna/453477" target="_blank">📅 04:31 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453476">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🔴
حملۀ هوایی به حوالی قشم
🔹
معاون استانداری هرمزگان: ساعت ۴ بامداد، نقطه‌ای در حوالی قشم مورد حملۀ نظامی دشمن آمریکایی قرار گرفت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farsna/453476" target="_blank">📅 04:28 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453475">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🔴
حمله موشکی به نقاطی در اطراف شهر آبادان
🔹
معاون استانداری خوزستان: نقاطی در اطراف شهر آبادان توسط دشمن تروریستی آمریکا مورد حملۀ موشکی قرار گرفت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/farsna/453475" target="_blank">📅 04:23 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453466">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dDPFRlKxfQAfWj5gHS7MVQOPrFTxMIz3_3KbLIpuD-TIGFP__bPmYVk17zpfH31SY2Xs4-FiJ1Tyjh7m0jP-wvrsHE2FPLNxdTQH0bm9s8zW_5eA3kP2Ij8NL8RpPxAXe-m-_j9IwUQpnTM33a63G99obRWZIFaaRPnsiBoqrARuutoZQxepGJ99YYx55mXrf9MbE-ktlDJXz2nJfhEOPzJ2yiX9lSDcELaI6UZW7QC7scuxQ4jf2suQj3UeSPiQiCBOEKXsSmus4lCjeCBCVNp1gBu74cv1LhE-cTdNNgR3qXaLXKQjEaxCaJQTSTE1CpxRZ_zZWmCi_jrAHncM5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tEaFqItygf3f_7EX9pCU1yNZ3bz11A-xzGzDg6sCabrXep2E8L3dxg9fQbw7YnPylzDhOt5tQs2HniBNKmGDEMbSihiMlpqVbkoh3MfzuzzwmejJ5nJ1AlmLaOlfqBDEKhijB5P0Tetj6G3C3bilQRETT5egGvjhpP7u0_9IQ5CnNtvSFfPpWaWPA5XifOIQaHmx10KyJ5VUmruyBUsShxaSp7e7XccaX5Nxlg16quI7lSwE_EzctNi7UANbGWNJa4VuSpXUSFDI3KAVtzM6bWT_pcjN4YueWwzHD8yEvkbVaQZ3nnRoyhxKKs1gJ1_8aeLFYyDVOiztDMis5FjdwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PvU7pNBbJmk4ncpDFBwwgBwYbxnSMKLP0sLy1W1EFgg4YEWzgx_GAo7XLB-jWkBYiIiyNtsK6u27aZ6IS7LYKroA5jkP4N8ODS01qgMTBcuDH4niErLVwdmT2B4LLKjMxxChLbJj_qpuZUd5lOPXtfeWJ4ITslb5vNLSJ1UDdPk0wJeSwTWRHViU7QMVjnh9nqvWRANNp1Sy4gl1Y4G71xr68SmWIOnrOddOiQZ5-Fabx84ECKfOQ3pLoN9XW7iJYen-bVggVOQC0rLjc99DVhW68kSiayzhj6haSrR0inspqQ8fsPF_SmyV5_RbyKIxrhdrQjREJjQEqmOJPrS7xQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tQtVWdWiU0rx2IQzg3qbPu4ek-f0bgjKp_WKgG_cPsgIYidVprqg2xM38GYIBsjLqa3Bh1qmnQb9F10sEg8jIkOX9zVGHtScuLDIX5bWhIBT6N9qRiiy4Geor7iZ9gTk5PVIGMWhzUYp5kxceibFyuWPiNkllOeQDXn57a-wP4IrAeleabgZcJBlE--fesuLuXnurazlhxcRIeDmbLdGxj-k8YJge415LFMGUu-FGawJZ7ojY_F1NT_Q56eukVqeT9z1fHdjIZfkZLKVCzXJVdb71asEfE_atMNnyRNa1h8U9Ix_Rl03UI5oHD-rP3Er-OzOvfrk3V_wl_pyWYs24w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DNeq4CUytGXx14MqnqzOogwFmOjDp6TVbWcKkpFmWl3cNlHdXVuOlM0h5Xi__rWPxDCWtyIXWxnuZnhi0ySHxxZHDWfKGl8IrJFULMnk-2o7cD43-ccMacsltgBme-t98QpYYguBIeMFc0jHJ38xl4QwBuAzzlPZBnsuUsEIt_ouujHrZ44gRMZInXI5Hk9C_B0kQ9W-1w--yKQWEvtIQbkseP5doPN6LPrxiLpDGFk7riIWRU0ej_7oNfh4CYB_Z9_K3L83kCaHu6TlVvtuwBBIKhvYgT-BIqZ5r8OJGDfSNV2M8vwXokInD__g_bugdVseuhqcaliDU5o7njCLYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jgs4qTgAvYtFSASfEPUE-zVUNIVaDnlpZEtR3Wx4wEfv688CbwAxbd0N_YKEa0ZPGk1MPtFzQvMIDNqa1D5KbjrDi_wP16rbeQ3uG6ebePrEr240-mSup-NQcNz-OgQA-RfSgos8twfNgk4doJAfTeAXYTOBHpH5-Zzzb7u_DChkQxfxDhrPLWCWcOfzzH4fCID2BnuorEV0bpZGax0uGiQNkOoMYh1N46CFi8u9w4qiRHYIvVLGTMjaWOe96Qd0HtnJdIZWkvPObuuC_iWXo6MBMMOUUNu_s6kw4WiWBcGshIkkH2ErqkhSi9EyZAlJu1LT9B_K10rCT2TcuWDwaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ca3FlpKgGnuWkXhVfcJI3OFJrPfd5u0ST3JERFWJDhWRIqhKi4ZvD7x7z_VGOXFSvV3QRe77jDQKnQhEM4tLHymbRfYYzn1auiOlK9n93t-PD_HkThGbCITpoeL6YdTzLo2trXBFHNMe4c6Dn4lqZ9QgJp-LThTGl-iyPj58M9cmeY7ioegf6HQe22x-jxRuPpBUb36ItM44C5y0TqAVzU8SvcLVk5fsjNNca994W2JUDrjLaoEbDpqU68mWVoW5jomeW9hjwGiZx7yJuQDHvCpwSZe5OGLEChZNicExYRjayT5woAw1qgSYyd3K0cAsOvC8CYy2r9q44qSzdu2-3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q_0rDj8H09cji6xbB1iHWwRY22qSZPysT50NBxd9R7Yaiv2FRjwb5eKStdg7Z50KVBV83og8i1plZB1usuZdeAJRSa5_ujY3PPKNed6-ujyW5rc65kXcRb63V9vclSYD3YbAIRFL4i5paFy9FmCTL0-uyC98sGdcicd-nkpquDS6TYYHbu-_3wNlpsB7zdZ4KxO2la2z9u82AtG4z81DVgHhhdl76TiAHusNutoIyNmrxYaFEKKYx2Yywc5fYiaYXGRqjuAEiFdfjm93UkmncDWzzI4uQnC03Bi4RU3SpkGKqqjeaFeZCF6yo60wjsbLprilH60H51MOof2EGa3bvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mJZG3q88y2BkAV6WvNYBRspwzT0hmc4IqxtZy8NvaoQmzzdvs2z4byYHuzMOevWa8pvJ9DhnQFIa5Smt-MrZ_VKXjR1r2kNc-IXbErw68D38My4M_v6kTNswxgTYyHE62aqcWc-OXRv5DZWAc-exulYsDxi5dLYyeUQSU8YkMbPlCj7mUg_vCDM_M13424hdnA56yo1_PsnJ46eNa0H2tiSQO2sil21wafEeNLWGPJONw5zAH9dC1Ez1JVb08jyJpHrVuTBr4p4lTlhbw6mwrWFsJtiMOpKQoXpOcON-hgPpxrGUmELtAqPeIs0ofCkmsxdoHVnPghi2yKFAISl1Ow.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
ویژه‌برنامۀ سالگرد شهید اسماعیل هنیه در میدان آزادی تهران برگزار شد
عکس:
میثم نهاوندی
@Farsna</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farsna/453466" target="_blank">📅 03:18 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453462">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vzrNUj-ypVg_VC35VtzXYMuuZfuZt61ZDVWmor6UCwg9x98OYo1RlTiBLbBmjJ4IJ-oUpOiT96Xsrc7RDNIOMR63CtembgvHpTRBrD0aDpdJWTAGCi8ozXpfNErR5pgNJEpMGcKOUYBqfYP0gpGSf6VMrkPutAPdleQ1YaVE7Z57h4Xz9j2wrsUjXs1h_LxydzEXYm4xeeLIYf7Lr-PoObA9eq4PgvtV0bN9XW5qvdw9mgbjqPAqzmi8oyvdLxVgiGOeeIy1QuvYGvP7GZwIzEML61unnS33Lpxqz42xCCdPykorKWtyZJA9F6VJcVU9XMWgZRJ5s0j4uw0dvYmKEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CNK3XDpWm3ypv4bWP1uZwvoWFNezDiiL-B-Et6FCktIxZO-dJDCSmA-vAF8BDF4zUtTDUqrNElruvPKW5wCPJmTXYVFYDs3ozyISAOTwITWp9kNV4LWQB_J5XRUC1cVCgYxIUHmT6XGCfMxZnmDSW4PXEp_FmDO02nul2qXSBd8e-777UZyouH5A306Fp0TnIwiOkBkhTGNoTS8bFIoS_pHNy-Hq6LAu1DHK38GLBMPNbX3-nVbwef3j_DjFYQbSVqZvN24EN2acKeXDz2XKETCU9RuRJZ2f1xh7qPZz3YMDuVYnsuhg5k5tYYeCCAkTNUNNU_vdt3C-5yUdz1dDeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BU3Ul4LCDl2hPp0C9JgWOlbz77uo8ekNG8Y8bGCEZaAUzjaMJzFYmZFUEo5T-4EPRqMnnoF4-lmDu0psc7vvkyiCgGmyG0fXFkPbUwDs-uIeTfKWFkbTWIew9sSNqrHAFgRIAW9iRH33SfRLemWjAtINUEocwX8yhf-TappjD-BXvcQuLhPsvP8tA7XAmxGhOJL4R5kHFK9cz3N_Gn2UKWH8rkvxeoVUoU5zvsMXMkqlGd_-2qEVE2PTC6-IglITowwp_VPbrp6pmznwmZ1wInrapNw0HPRdLO9UPKkDMrEwMJPCT3MjtUtutv-c_qC4FC4KCe0ohuVBiuqda9bwKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UHCSKwiF_0PND7-3XMAno4i-epB9ohCtNX0kobQ5fq9Ao7pa8KPySxpuz4hMW-5e_B14nly2iGmzJPVYHLiHnaSnf91M7kQKphhKU3Esq4eb9h7kRbT_BL4m51vacEsdlFAznTfE0JR-A77VneLnDumem7sMGyJ1KUKHtjeJ6YJ2NfZivIb9W8qBnTZ6bQje2tytSgn_zaM9NMIpMDbhavyhRWySXuLmekrOVu2AIX-ywXS0Tcsu6JZm-gTOtX5XemJUo120fNgY4dybho9M5dRtjkCVC4MCNLdRdmvbzPSAdjFAB_gmmcge1VQxoHiqSOUJQRuRQ8RLPNH13ZK-SQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📰
دکۀ روزنامه | پنج‌شنبه ۸ مرداد ۱۴۰۵
@Farsna</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farsna/453462" target="_blank">📅 03:07 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453452">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CZ5_A2445rI16wHvCo_0RUjQzsJ6XyGVCXSxZ2cKppuPb-w7tnhGkiYka4lozvGGqk8Hxps_4_1a2T0fuAqKuoqrRUhz2meiyrzFkly4S6t2pSKcJw8xlqpoY27w-P59OW7PuGvdyXdfLmuh8OY8f4umQt7gFiFWqrBXY_S_uD7jrmlJ_7zeOWUJToePOkx95x0P4VXClXAyxqskikXvDx3duq5sSxYISgW7TYkKvtzID06Lbvni41580zTWWz2xqw_4n-ZnPtjD7S_C9Tr_OT0eDliWYzJpoJY93QJ6T2aS_cgbpInEkhx3IVRe1C06wmV3hUbRseOxdyn3TV2d6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fqNf8nmd2qzQe1Fpn8OFzId8s1nSVVde5lAJixJluCWnzOOyFT_UTaFYLc_D82cXB5PANzsUTTCYcYlNKcdVUZjpNShqGwT1q4JPi1tfBnFuYhADalK_O5es5dI26BveFLGMtDKvkIvx5SUqpAZsIohiUDg8tnOS6Ea4WWAZJ4OWmyx_YIzD7zi90lUReW62eDkXDyYkN_3xsdSPUKcP7V5M__4m_YBAwmXtAee38M11F1lYy2ZK7BH153l6eBH_PcHZXkVBskDlPIcMielqLAlqFi5eBPHPdjQtVqQl3xyDGG3NmSLcYxefPEg3TNxrMG2IZQ2wbSi4Z3egfEYPOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lzKIHxcSO1ATfXou0o6lVhpDv-swOc2lUbk_Xcet6yCfwrd6ClpFu1X8B5exx5ylDfvfB70KfLLAfnmI6J53KI-v8jpVwvOrFWT1uk5UUKWVqqKkQrXe4x7nDBzYqtOVW8BfGAQj0s1bPLCna2GAhNM9Ugo0Th1yfYO-a7PzaxnolP9AGCkqZEpR9ibP8pvzm1YzkVRdRw5M0KLe8-fKsboT-O492QNkBAWoQem2bgCHWAuDhY_k5xS_ocxt6GQerfEQml095tIgTCPwAN0QLNMPgjGqsUioBAeMhm-qir_cHdqUlX1TXQEz5wThWHt2-cDjHGHMbMTGn482bvCZ4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Nut7TwaG9RwrqjUab8E17QxFGFyfLVdogslY4Q_wwr1Emtt3vTyfKi8Zeqo-mllHp42viqEIi3VL1ssaOaqDCBWySn0-Y2kZ7yn_xnD3wm6mlJ2YtzxnegDgP-HfCsKeqaUpIWqWqIho1QqZKHgV6BhZCiFZ18_xoI4xtyAfRMda4GTbCehTAQUuOZchzcwICNqFpKxoTCOtOyIefd3YQP7x9dymN_SRXO5gN-QeVLG9QirtFHeBjZezSRAqBOIm1sEUq29yC96c6TFDXf4lm9SO99sqh0Ch4CJyDz3TjduikVq29hUy8PaoikZjQwLggSCmYcyhsAkt7B-yRXtXZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MT12iyVxDKLg196AU49-ETwLiP-T-ghtWYchczDRqXfvST3eTYIkgsFOcsFIz0TnLOfs0SyfyRk9lyPJ5pWhNepTWE5-C81F-GaJmrSgLNzUdYpm1wMHw0xVAWBzKjJ-t3OpqOCiJPVj0F51GsiV68gsekESqxfHBdrOsvMunIw1YcTfro64-jnOUSaznalDDpe8_Kn_Eo9P4gNJcA3j6njTVUFflyekI7IzLMbx1j8Fw2krAH2cCEEzNqQRH16W4Is9LyR-1U-tLYptf6rTyGsB41BsppEb5Lo4SMPKt6vVak8cv_mXCxBPdNf2Kv6WOiC_zQi59_MuWEcoJehdVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TtAA85D3qK4EEsc6FyZOE3s5BHIaKTsAUnDwgKXsXuHyv3z0Tc673bjJDlbOLXNrXWJv0Cnuz_xW_if_RWpBntYzWHeFJLyqYc455yoZfaSo1je2xQqdBOAWwe4JHUiyEUXA0c9HYwm_WUh-PrJyLApUzZ2g5EWtWo-4KSt5LYjjHC6EqTMGee8rvyWpFjpTXqzhP4yY9PL9ApyyJiAeEnB4amdGtWKEKq9_nHDDUEO-gL3id25j-3Qv2FqNdTbZdZM7nYhyB8fcX3zPfxSLr_jNsYp0kCYGE2fpJlDMJpAx9USDm8earehk_qkQtMHtlVoiXz3vL2AU0qmt_Qmk1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vtFrsw3al9KNWHbkFpqTguW2F1q0C3QGv19E_KBw8wN1iuwZYGzESiQ8rEEP8F6KP1cR5uSHDVL0xtpiYhVAj-c0IDtvEaZlYfsnhxaBn5g2U9Dy8c2VPc_7dElP3lhW6OyCBAibf16cBv_I7t8WF2dqlMCC3h7JZzFaxzo6tZlyzqI4Sg3X6D6LIPe_BY8pnPirr7KYenshr3a1Key_SQumisiH_Fr7MZ1K3gUvdaK2sr07Q6ngBl6J-GNCC5hSXDTCVHneSIw1GT1XLHueMD6Es5-3vCGBmmtvUEuCh72duxWt8MouV4GMXkj3TBBvufv01QoC3j-rljU7OxYvyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XHZur4kvmbAopeeinY4zgFJj35LFWULsi1qB1EkDmlX8abo2S7RdpKgzkHG2UWZcqY8CjU437kTXXB9U8gGN2eelqkobu6eRr3TRrsJGbqEP6O1xwlIXQeIr90aUddbZRUYT21Kgedu5asOt3Q5drHqH7NfanC_9hC5OgI5mQIU04FF9LlZi4bCv-T85MtzqJpyNAlp7ys_UlPC22dVVZbcISxBSxZ_JgtJihKR1gv0ssZzusoi-Y7VQrzaMhlHm696kjGuPsXt0KUnma48fiEbBm6KGRQoKDz2YOeidqG_S4_0d5O4UNLpI9yNvWYj17SvXAgbtw0_qKhhDooV39A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gX9iKk89Eicn0Zjr51l4IgzXKPla4ZaG85Uq2B9ixnwAwkwPgqR2-7uFdmT0ddO3xenifa2Ev9z7Ps9TLdAlNfn26FL3VQ7elD6KzL5Gpkm-m5DDq2SLeZHDZNLMaF6FSUX0SZvTQcpQfr00EdQ_HEXmH0ZeDBgkxpe80CnqOXn4ec3gAXlFwUHo6VJVN1V6MAiAqXFI_rTC-YcOcY9bFzQLeFqNwA2pfgLaY6hRu9T5t-aP8HcNnbnlYFnGQc93uxHodVz8SFh0YSu9lvfHgiWKA4legY3G7LJlFv1C0yZITbZpUKkaFattNMKmetLDIjk-7DwUmMS1jldVJNM27w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lrUTblbgvS9Hv3raeFcmtfuJUt5AbybJD3xGADARd7BRt1r52uJaRdN0OqmiR3n5TlVqFHKyK3htvD-q6FIxNKaynCDfturQ93m8prkYTJ4nxPhcY8JRu330YDZcOZ_bRWXnFIc5VL4INpeMQV1UoWsOYsio4NX1AHULxT1uhSP_w9h_z4eFwqafRplsNV6Cm_hse2ZEnmHZL3fcQqD3uWU6uTvekOwwsrEAYHFeZCPRvulMe7jX6cRbs-AhGU45Pet2FdvbTGitKkivp8vtrPIDE-zTwc1NwYFIWuv21zGKrJ8puHowf1PJW4bBHZDcMRZ_ySFu8aAYZrSYSPENaA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/farsna/453452" target="_blank">📅 03:07 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453450">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZFW27AaxicVp67BNranCwNQu90Vo8Z0Cjh2gUSlR4Ll6hlA6bRFIhtS2oS_RitoLmolL1n9mfBwdKSrXzHLYTYLinAdMucUVSOwqsnj763GZrbki0WRS4Doj1QNdehRIgkNQyrChdpW2-uVx0kb1m7ATeKPIJUPgs4WSLyjq9ei5D0lTILSYNXTnnnYdMDL7HWDiV7-_S0Ye7MtlQU3YE0Wp5HhBfYtFki4D59RrAvpLkTtmOqgbGMEIksziEHwrMxWkhTual7EqK1Q8c3MSaCBZLstaVZPGfYSHjbfOlE-MxGbAVfK32IXsBZMuOuXvED784-O6Rm4eE3NmjKvQxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیشنهاد سنتکام به ترامپ برای حملات ۲ هفته‌ای به ایران
🔹
نشریۀ وال‌استریت ژورنال نوشت که فرماندۀ سازمان تروریستی سنتکام طرحی را به رئیس‌جمهور آمریکا پیشنهاد داده که ذیل آن، تا دو هفته به زیرساخت‌های موشکی ایران حمله شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farsna/453450" target="_blank">📅 02:38 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453449">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🔴
رسانه‌های عراقی از وقوع انفجار در مقر تروریست‌های تجزیه‌طلب در اربیل عراق خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farsna/453449" target="_blank">📅 02:13 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453448">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">انفجارهای مهیب کی‌یف را لرزاند
🔹
رسانه‌های اوکراینی از شلیک حداقل ۴ فروند موشک «اسکندر» توسط روسیه و وقوع چندین انفجار قدرتمند در کی‌یف خبر دادند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farsna/453448" target="_blank">📅 02:10 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453447">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dei_hPiCkZChmXchnnGh7sVYicguf5t9kXJyV9_gv8Pr-ajSSkTG1eUpUTYeBFchRtNnzHGOKeQH2-BjrGrpBa8-fHy9z7xCfg09SutEmt8o_qC507AYPDSjp_jXbHCmOtTiEyRMPFnJWNk5iu16ZiGowdC20ple3RteAbZz7H4rCdDZnUNtxlDXu0JIQCZ7VOJBHBiRKGz4ou6UXdDzZa0sf_zAZuNxga8ewP893uBhWpWhno-4_MTUV8tLazdDe2gCpQ6GMspA9fm2lePXjZrh0mwKHUEqjzT0mg2IfsXa60PlUFBkoTHHXhZXOykIrxnyBna86hDCqsz0eGbcuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
مردم به گرد مزار رهبر شهیدشان در دارالذکر رسیدند
@Farsna</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farsna/453447" target="_blank">📅 01:33 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453446">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bPxWQbyE-3vwJe7m2Br0EW6-f4BIE8wgWdPJ6iiCE3ipOGUbm2Pw6hb7sC6yrvOQ5k9gHIkYiO1aGiAgHvV99lmJHzCGMVqJW8Ym5rtkqoh4GqJ5Xls0mjfDr6I2l_Dpwt6F7DLl1dOB3LcUONHJF-wQYapXSRFRLqqPGwMQhjGjUmGt6-6t1Cfsn1sIhT_Bzj3LmXXptsq2zpaE2kqlyEF63nfYUYgJI1MO4EfuU487BC3sVj6v8a8RY4bUy0TwAAlSP8YY5cTV2GbKjKwP_mCmgS-_618XlqKHCSSN69r7jpDOr9k14j4xw-TA0lgMOaaVN6x4YKA3JxeWvUowMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
شنیده‌شدن صدای انفجار در پایتخت عربستان
🔹
منابع عربی می‌گویند لحظاتی پیش صدای ۲ انفجار نامشخص، به وضوح در ریاض شنیده شده است. @Farsna</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farsna/453446" target="_blank">📅 01:10 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453445">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🔴
شنیده‌شدن صدای انفجار در پایتخت عربستان
🔹
منابع عربی می‌گویند لحظاتی پیش صدای ۲ انفجار نامشخص، به وضوح در ریاض شنیده شده است.
@Farsna</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farsna/453445" target="_blank">📅 01:09 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453444">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3648e98935.mp4?token=EAKmofzunR3WT1Et8QlPd-kTeT97MUVZ8O6vMjftrRAoYML_lYgKkvCHZDeKdnJsHXwafopDOtVXJWs6_bTeLzP9hyVwsVK5Gxdwg89sIVAjjBgQjyNDgiY2jIC3vFA3JT14Y61xi_XF0fgXFqOg36fDKmm3eu6b7b7-hUOVwlI3buXzBwImCtskV2s_TqATA-kVLzgvCfLSqsCtf9i4Q68XZ7GGSsxzdy-n5908lUTNc5C-aKT_eofyyBnExqkgJ5Isjo9PFCX4XkDAHPaiji9k-dGFOY5Z9Y3kFIf-mzdtkAIyJ6dbX9iOtSXFd5knKJUi6Yk9jJzh4IdbjNuRdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3648e98935.mp4?token=EAKmofzunR3WT1Et8QlPd-kTeT97MUVZ8O6vMjftrRAoYML_lYgKkvCHZDeKdnJsHXwafopDOtVXJWs6_bTeLzP9hyVwsVK5Gxdwg89sIVAjjBgQjyNDgiY2jIC3vFA3JT14Y61xi_XF0fgXFqOg36fDKmm3eu6b7b7-hUOVwlI3buXzBwImCtskV2s_TqATA-kVLzgvCfLSqsCtf9i4Q68XZ7GGSsxzdy-n5908lUTNc5C-aKT_eofyyBnExqkgJ5Isjo9PFCX4XkDAHPaiji9k-dGFOY5Z9Y3kFIf-mzdtkAIyJ6dbX9iOtSXFd5knKJUi6Yk9jJzh4IdbjNuRdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ماجرای رفتار خاص امام شهید با مأمور ساواک پس از پیروزی انقلاب
@Farana</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farsna/453444" target="_blank">📅 00:52 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453443">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef23210083.mp4?token=NC48F-DpgT11DCe3RHEkusOabT2I89uz7Gdn0PaMKWfdhTOnMea6Qh8xkMKdUlNeL5Vxs16Wv5c5jnUmXMx021ds75evtXiqIhObonU2MfzFnD9FrWuvZuKeeeJ4qETQtyFBTQSeD5RxiD2ZEGcIpumMLUA2JsOuC1bpiLqU0OCGOkO9J4Iym2zrBQhfkb_pkgslbkJkMGEfGsQKgWQWVOc7wHxhrKG8LFEjFMCmd4iXOhJvkr_RCXQa5-X7kQR7Kh7aqI45PjPUrGM8cTo-cKRunJ2M6sV10i9XJax4GxZuB2IARtBVSF0bMGjJUBGKRC2sbCJ_Tz7zWKOjBu78UQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef23210083.mp4?token=NC48F-DpgT11DCe3RHEkusOabT2I89uz7Gdn0PaMKWfdhTOnMea6Qh8xkMKdUlNeL5Vxs16Wv5c5jnUmXMx021ds75evtXiqIhObonU2MfzFnD9FrWuvZuKeeeJ4qETQtyFBTQSeD5RxiD2ZEGcIpumMLUA2JsOuC1bpiLqU0OCGOkO9J4Iym2zrBQhfkb_pkgslbkJkMGEfGsQKgWQWVOc7wHxhrKG8LFEjFMCmd4iXOhJvkr_RCXQa5-X7kQR7Kh7aqI45PjPUrGM8cTo-cKRunJ2M6sV10i9XJax4GxZuB2IARtBVSF0bMGjJUBGKRC2sbCJ_Tz7zWKOjBu78UQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ایرانیان در نجف اشرف هم تجمعات شبانه را ادامه می‌دهند  @Farsna - Link</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farsna/453443" target="_blank">📅 00:48 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453442">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">شهادت یک مامور پلیس در ایرانشهر سیستان‌وبلوچستان
🔹
پلیس سیستان‌‎و‌بلوچستان: ساعتی قبل افرادی مسلح به سمت مأموران انتظامی در ایرانشهر تیراندازی کردند و در این حادثه استواریکم «مهران سالارزاده» به شهادت رسید.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farsna/453442" target="_blank">📅 00:41 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453441">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/feb118187a.mp4?token=EgXLH1qVSyPYBxTuqXMChCQcNMdjOG2HzwLGYRWI1LHWWSgTlcPu_mEphcGte560xhjaWhuen8PSmKpp4UJqzNq_NnE2K5hi-LL5b4AhjOFMEtMKe8c1BimSPHq994kwI-JllsTyqmS-ICx2Ue_7USYygDyJtEmG_dLzXKT-wTQ1q8YwGmICsbrTB52puN9VKirHDSXSIbjfJ4LspUrPiazcU2okOv1yghn_qJOGjs7g17AnHTUxheSjCE4FVIQh41v_575ixJJOXYkIvol8zPEbySXsrl5qMt7nICxKxrDV4xUG3_ssiBU3DIpFZLrA5xlx630vm1lf9rBBCGgCKTIWPi9_4aDO7zbTTaZvDwur6jGlsanc6G7W865BzLk6A-L_t8DU_PwmXfdF2wdo2rTkJmeAQH6OCxmEZj5VyvNzg4fnVAbaV1YwkjRyuAcDJrHCIuzP3DL2uP35vmo_ZUWSrEHl8BzCVZMfNNWjq7ozyAPnsWHkbb-HCsqNZ3TG3Gty6F52zinOmVrjFrngWlVakpWecbTjf5ad1vn3xC_nykMTXPozkjydGor3NECOgUwU7CHbH7GgEjxO71q5YCBYzZl4FZp568egSKNf8N1PmQXPrLqAZMtjw9lPIh2B10X0ibXWRNLStHIyhaUUqiCxHueKw_LUOxFIERDIC5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/feb118187a.mp4?token=EgXLH1qVSyPYBxTuqXMChCQcNMdjOG2HzwLGYRWI1LHWWSgTlcPu_mEphcGte560xhjaWhuen8PSmKpp4UJqzNq_NnE2K5hi-LL5b4AhjOFMEtMKe8c1BimSPHq994kwI-JllsTyqmS-ICx2Ue_7USYygDyJtEmG_dLzXKT-wTQ1q8YwGmICsbrTB52puN9VKirHDSXSIbjfJ4LspUrPiazcU2okOv1yghn_qJOGjs7g17AnHTUxheSjCE4FVIQh41v_575ixJJOXYkIvol8zPEbySXsrl5qMt7nICxKxrDV4xUG3_ssiBU3DIpFZLrA5xlx630vm1lf9rBBCGgCKTIWPi9_4aDO7zbTTaZvDwur6jGlsanc6G7W865BzLk6A-L_t8DU_PwmXfdF2wdo2rTkJmeAQH6OCxmEZj5VyvNzg4fnVAbaV1YwkjRyuAcDJrHCIuzP3DL2uP35vmo_ZUWSrEHl8BzCVZMfNNWjq7ozyAPnsWHkbb-HCsqNZ3TG3Gty6F52zinOmVrjFrngWlVakpWecbTjf5ad1vn3xC_nykMTXPozkjydGor3NECOgUwU7CHbH7GgEjxO71q5YCBYzZl4FZp568egSKNf8N1PmQXPrLqAZMtjw9lPIh2B10X0ibXWRNLStHIyhaUUqiCxHueKw_LUOxFIERDIC5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ایرانیان در نجف اشرف هم تجمعات شبانه را ادامه می‌دهند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/farsna/453441" target="_blank">📅 00:39 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453440">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a28822ab33.mp4?token=d7RnZAGySj_CM4LbWxHVEx9_HlyoO-wIyy7blngA-puE8XRwGI390kCsqZufBcbNSPGeYcWKEyhW5zqC9tOZrblpu1mHBo-3EIP2KXZB_GkZT6-aBe105epOoDlSFmyRIELoUiZ0L_eshKVKnU6zpsHHXaoXXYYrKu6ay4BWEYxJCEu95jkP-OMVxpqXiGJFi9wQWdLE9awnMW8lxWQFYr6PnpmR42QXpIYlYEyPKKbFAfmIs389KRWN9WN0_NaNU6bk08GSblc6a-XYRQnGt8rkK19CbE1OS_dyc58Mo9uhAFbi0uAV3QQ-wkhbB1moPwDUbIZ1ERA0e5E77CQHrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a28822ab33.mp4?token=d7RnZAGySj_CM4LbWxHVEx9_HlyoO-wIyy7blngA-puE8XRwGI390kCsqZufBcbNSPGeYcWKEyhW5zqC9tOZrblpu1mHBo-3EIP2KXZB_GkZT6-aBe105epOoDlSFmyRIELoUiZ0L_eshKVKnU6zpsHHXaoXXYYrKu6ay4BWEYxJCEu95jkP-OMVxpqXiGJFi9wQWdLE9awnMW8lxWQFYr6PnpmR42QXpIYlYEyPKKbFAfmIs389KRWN9WN0_NaNU6bk08GSblc6a-XYRQnGt8rkK19CbE1OS_dyc58Mo9uhAFbi0uAV3QQ-wkhbB1moPwDUbIZ1ERA0e5E77CQHrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
زائر اهل باکو: آیت‌الله خامنه‌ای تاج سر همه ماست
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farsna/453440" target="_blank">📅 00:33 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453438">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8d9721669.mp4?token=V1p27GI8lA-aphGyYYZX3yo0CMn30fHX3_zkQgB1wk0FaMsyU8f67ZMBOl4KZrPAkiVJihXvx0Ik94fVIOeqS3o0hVIGIZ9PlPAusIUBnMz-wu6LdQuK9Y0aLihRvx5FdkvU9hF8qJ3yo52B77JXHnhsamusrQyD0EWxMWne6vfklSbvlPDCim98FlUHcwsTbQNO6Ktlmtm5QPRfLALoy-MxTjtbKvxRSZqf2tIJWsvJtCVoZw9fo4dAOkxCBfGQ-vprHbUdRVXDTJx3z6xFbFA3sY5znw502zT-71lPADQHrXVBbw0PUzOJWfuJ7VkPFrccd8o3gGcOOYcqj0eimRf4B-n5OE52QEThY4xKxBFSQHFQAHOXOsgBX0GbAZSBez-9mc42Nas5QWQDk_2exw2cVRiE0--xto6nhwdV-rPzymNOSbVh5ircBdA2xn0OKLplqZQxRHVsraiUlXaYOii9YKF7rIP78Ll_HzoVdeA1DH8yh8WCzKT8qcI2bKasI1dNAADeezFYKv2S7TF6vQrKePN1UbUjVgwhM4FGJPCDT5yXqBOkptj8Ns_ldEEHuImhiW-q6mMv3-LnkYJnwl62WH9YROTCA_66qVTx0-OgI93PA2cGW6rFU4YUNqfhGKKTew_ijEIL66XWOOw8Itk0lHQ_YDDepkdggtG3H8c" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8d9721669.mp4?token=V1p27GI8lA-aphGyYYZX3yo0CMn30fHX3_zkQgB1wk0FaMsyU8f67ZMBOl4KZrPAkiVJihXvx0Ik94fVIOeqS3o0hVIGIZ9PlPAusIUBnMz-wu6LdQuK9Y0aLihRvx5FdkvU9hF8qJ3yo52B77JXHnhsamusrQyD0EWxMWne6vfklSbvlPDCim98FlUHcwsTbQNO6Ktlmtm5QPRfLALoy-MxTjtbKvxRSZqf2tIJWsvJtCVoZw9fo4dAOkxCBfGQ-vprHbUdRVXDTJx3z6xFbFA3sY5znw502zT-71lPADQHrXVBbw0PUzOJWfuJ7VkPFrccd8o3gGcOOYcqj0eimRf4B-n5OE52QEThY4xKxBFSQHFQAHOXOsgBX0GbAZSBez-9mc42Nas5QWQDk_2exw2cVRiE0--xto6nhwdV-rPzymNOSbVh5ircBdA2xn0OKLplqZQxRHVsraiUlXaYOii9YKF7rIP78Ll_HzoVdeA1DH8yh8WCzKT8qcI2bKasI1dNAADeezFYKv2S7TF6vQrKePN1UbUjVgwhM4FGJPCDT5yXqBOkptj8Ns_ldEEHuImhiW-q6mMv3-LnkYJnwl62WH9YROTCA_66qVTx0-OgI93PA2cGW6rFU4YUNqfhGKKTew_ijEIL66XWOOw8Itk0lHQ_YDDepkdggtG3H8c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایت فرزند شهید تنگسیری از روز شهادت سردار دریاها
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farsna/453438" target="_blank">📅 00:14 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453437">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">توقیف ۴ شناور قاچاق‌بَر در آب‌های بوشهر
فرمانده مرزبانی استان بوشهر:  با اقدام مقتدرانه مرزبانان در آب‌های خلیج فارس، ۴ شناور حامل محموله بزرگ قاچاق توقیف و ۶ نفر قاچاقچی دستگیر شدند.
🔹
ارزش ریالی این محموله‌های قاچاق ۲۰۳ میلیارد ریال برآورد شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farsna/453437" target="_blank">📅 23:51 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453436">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/575a64f54a.mp4?token=m-o9R2tnbg95gdy9bs71eNo_Kme83frrwqm0lTDdfYTjKY0EXiV2X1WzDItcmussS1Ctj2mLt0B_WZA5shFZyzWyEgR7wld3l_OBQlyDtorezAT5HbpkkCmgCIodU9LwUm7Gh96noP5Smt-b9wPA_OH6dSOCZHvgwDrb9uM77AUed1U8GolS5b5eM7jebAe6Yfi1O9ETSVukRWFhzJmz-96mGAzO0v2UK09YpMYmiGPW_x_qvF5axWmSI_kxLZykzb9DyVbANlxc0A5Cu4QNdF2S7g_yX11HpjLJlWJNn5CPQ3oqlrvttfZM1NwkZCKmK9cm1xMo-yzib7QqJc4UUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/575a64f54a.mp4?token=m-o9R2tnbg95gdy9bs71eNo_Kme83frrwqm0lTDdfYTjKY0EXiV2X1WzDItcmussS1Ctj2mLt0B_WZA5shFZyzWyEgR7wld3l_OBQlyDtorezAT5HbpkkCmgCIodU9LwUm7Gh96noP5Smt-b9wPA_OH6dSOCZHvgwDrb9uM77AUed1U8GolS5b5eM7jebAe6Yfi1O9ETSVukRWFhzJmz-96mGAzO0v2UK09YpMYmiGPW_x_qvF5axWmSI_kxLZykzb9DyVbANlxc0A5Cu4QNdF2S7g_yX11HpjLJlWJNn5CPQ3oqlrvttfZM1NwkZCKmK9cm1xMo-yzib7QqJc4UUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شهدای ناو دنا، اهداکننده خون بودند
🔹
خونِ شهدای ناو دنا، پیش از آنکه در راه دفاع از ایران بر زمین جاری شود، در مراکز انتقال خون به بیماران جان بخشیده بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farsna/453436" target="_blank">📅 23:46 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453435">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JZQca5uoLhQxvvzFr5z3l9Aho7HdGzcf5Jyupm1q1nFpwZUvB31-gGeW_6vw1aqcImgeyAE-ttJjeRybB5TSMITHEXTTrgjrjlVYzik1vEIPUKhrmJ6WUz0u9-Gc7XAviUL3kqzhSU3CnSrsYu6ZlsszMnqMpXkh5HjMWmYFhQLYRTIrkwDMTEi_J_Q_hmrL3m6bWKg1ldrQCF3r-IpumdNP2aOIRQCHo_KX43qVoW9R02EDDOCq5UaKyWjP_GQ7b_GDHPLbcQQ46xyUF1TO0sY4YuPjPtlesoTmemlabEmarKOyO9M7A-x8CKEP0_Dbkml1B5h7YXHm-0qym-pyPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: نوبت ما است که ایران را بزنیم
🔹
رئیس‌جمهور آمریکا درباره ایران گفت: «آنها را بسیار شدید خواهیم زد چون نوبت ما است که آنها را بزنیم. می‌دانند که حمله در راه است. از ما درخواست می‌کنند که این کار را انجام ندهیم.»
@FarsNewsInt</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farsna/453435" target="_blank">📅 23:27 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453434">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">روابط‌عمومی سپاه: بستن حساب کاربری ما نشانۀ وحشت از داده‌های دقیق ملت‌های آزادی‌خواه منطقه از مواضع آمریکایی است
🔹
ملت شریف و آگاه منطقه، امت بزرگ اسلامی و آزادی‌خواهان جهان!
🔹
پس از آن‌که مردم غیور و شریف کشورهای منطقه، به‌ویژه برادران و خواهران عزیزمان در اردن و کویت، اطلاعات ارزشمند و دقیقی از تحرکات و پایگاه‌های رژیم آمریکایی را به حساب کاربری اعلام شده توسط سپاه پاسداران در تلگرام ارسال نمودند، دشمنان مستکبر نتوانستند این موضوع را تحمل کنند.
🔹
آنان با بستن حساب کاربری روابط عمومی سپاه، بار دیگر نشان دادند که از داده‌های دقیق و ارزشمند امت عزیز مسلمان و هماهنگی میان ملت‌های آزادی‌خواه منطقه، به وحشت افتاده‌اند.
🔹
بستن یک حساب کاربری، هرگز نمی‌تواند صدای حق و اراده پولادین ملت‌های منطقه را خاموش سازد.
🔹
به‌زودی درگاهی جدید، امن و مطمئن برای ارتباط مستقیم با ملت‌های آزادی‌خواه جهان معرفی خواهد شد تا مسیر تبادل اطلاعات و آگاهی‌بخشی، مستحکم‌تر از گذشته ادامه یابد.
🔹
تاکید می‌نماییم که مسیر مقاومت و پیروزی، با اراده خداوند متعال و همت امت اسلامی، بدون توقف ادامه خواهد داشت.
@Farsna</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farsna/453434" target="_blank">📅 23:23 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453433">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c7c1d107d0.mp4?token=MMX4xqsCmwPNFa-la3WgeOJxJM_63Nq3guUECFDI_bgQWecLR_TuDOzSwaJpEKkqK6SVnorWLv7ywLfCOgAieMtllfL-OI16fpw1l1SDGOAlYNW4PId9kPfS7WgM2Ie6ffR7njuFNFy3pB-tcGPaZncm6SmNdRNOI2nrQGapRc9A0yJxwv6bQo_oFC7TDDCeZmg3uwpNi9dd7LueJUYkiEwvAzYBk_5WNqWzsNyHNFkNnsGNS3FJhIKpd8l2DGYJ32XORiXeDDZ4u0cUgbMmQLV_Y90BFhwnEcd2GGZ7ev9jI3gWPqxwbeApHIMuuC8ZpDXlHHsv7tZuFxQpm5STUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c7c1d107d0.mp4?token=MMX4xqsCmwPNFa-la3WgeOJxJM_63Nq3guUECFDI_bgQWecLR_TuDOzSwaJpEKkqK6SVnorWLv7ywLfCOgAieMtllfL-OI16fpw1l1SDGOAlYNW4PId9kPfS7WgM2Ie6ffR7njuFNFy3pB-tcGPaZncm6SmNdRNOI2nrQGapRc9A0yJxwv6bQo_oFC7TDDCeZmg3uwpNi9dd7LueJUYkiEwvAzYBk_5WNqWzsNyHNFkNnsGNS3FJhIKpd8l2DGYJ32XORiXeDDZ4u0cUgbMmQLV_Y90BFhwnEcd2GGZ7ev9jI3gWPqxwbeApHIMuuC8ZpDXlHHsv7tZuFxQpm5STUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شعارهای جالب کودکان نیشابوری در تجمعات مردمی امشب
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/farsna/453433" target="_blank">📅 23:19 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453432">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a58d6fd193.mp4?token=i6KUaeUmfe2-r54pHUJ6CRBvm6kr5Ux9AavWdS-nnPJ8wYLvtZZV7O5P-e-NVqm59LQGOWAuqsC4qNoYchlaRg-3z3SMTTUzxcAyCJp_JhyUVVWgSwcF1IJX9hSWyT-UpsOsdAmsG5RyC_9MydbmBo6n0rMhCRzaf4ZTJIt22QXob_BfdXB1NwJxO13cNbYf71x4sz4EHa4pn2c3C-vzJsDJVS8rDCjkroYnifwKgS9D9TvqhHGIWoGM6nA-K8uBnuJExQjwfTVjZrUc3JVszT0ggMhCz3eVcmC5jbVlFwHf2eEL2085ucduEMkbIspLC88qyZc9BW1zWTAYdmIIzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a58d6fd193.mp4?token=i6KUaeUmfe2-r54pHUJ6CRBvm6kr5Ux9AavWdS-nnPJ8wYLvtZZV7O5P-e-NVqm59LQGOWAuqsC4qNoYchlaRg-3z3SMTTUzxcAyCJp_JhyUVVWgSwcF1IJX9hSWyT-UpsOsdAmsG5RyC_9MydbmBo6n0rMhCRzaf4ZTJIt22QXob_BfdXB1NwJxO13cNbYf71x4sz4EHa4pn2c3C-vzJsDJVS8rDCjkroYnifwKgS9D9TvqhHGIWoGM6nA-K8uBnuJExQjwfTVjZrUc3JVszT0ggMhCz3eVcmC5jbVlFwHf2eEL2085ucduEMkbIspLC88qyZc9BW1zWTAYdmIIzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رجزخوانی حسین طاهری در موج ۱۵۱ تجمع مردم در میدان انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/farsna/453432" target="_blank">📅 23:10 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453431">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e819a74c33.mp4?token=IoI8PKWeCRocoKP9FBiSZcpb85576LRvw2LdJWiJVs__-5TIXXFh7D3qoe4L8n1sXpfzdE0FSt_S1xSYQWOA2NsO8UJuivKoh2J0VIbc6w0ZaxsC2EnlrTUQSapM92Ugs31cW7xGagM2B7uZ7f-9ULjXZts1g2IHhD-QgY7fZfDLv_uJaxKTOe8tWGPwk1k9qx2d7SndCmdBOVk_ypKRYSXKnZh0CmkXaXrRNFPI4ggebE90-FmrYXw7z89XVa4RThTDkG_O69v2UiLgMN7fbMkw0Ha_1wKcwjFQrMV4aBvfwAk2fo-Dl77nF9w2IlATcFZY3WPCzJ8OJ2GlGaRfLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e819a74c33.mp4?token=IoI8PKWeCRocoKP9FBiSZcpb85576LRvw2LdJWiJVs__-5TIXXFh7D3qoe4L8n1sXpfzdE0FSt_S1xSYQWOA2NsO8UJuivKoh2J0VIbc6w0ZaxsC2EnlrTUQSapM92Ugs31cW7xGagM2B7uZ7f-9ULjXZts1g2IHhD-QgY7fZfDLv_uJaxKTOe8tWGPwk1k9qx2d7SndCmdBOVk_ypKRYSXKnZh0CmkXaXrRNFPI4ggebE90-FmrYXw7z89XVa4RThTDkG_O69v2UiLgMN7fbMkw0Ha_1wKcwjFQrMV4aBvfwAk2fo-Dl77nF9w2IlATcFZY3WPCzJ8OJ2GlGaRfLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
امر فقط امر سید مجتبی
شعار مردم حاضر در پیاده‌روی اربعین
@Farsna</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/farsna/453431" target="_blank">📅 23:08 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453430">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس اقتصادی</strong></div>
<div class="tg-text">مدیرعامل یک صرافی رمزارزی برای دلارهای صندوق توسعه نقشه کشید
🔹
مدیرعامل نوبیتکس در نامه‌ای به وزیر ارتباطات خواستار وام ارزی این شرکت از صندوق توسعه ملی شد.
🔹
نوبیتکس می‌گوید خسارت هک ۱۰۰ میلیون دلاری سال گذشته را «از دارایی شرکت و سرمایه سهامداران جبران کرده» و این موضوع توسعه شرکت را کند کرده است.
🔹
عضو کمیسیون اقتصادی مجلس میثم ظهوریان این درخواست را مصداق «خصوصی‌سازی سود و اجتماعی‌سازی زیان» دانسته است.
🔹
منابع صندوق توسعه ملی بخشی از ثروت ملی و سهم نسل‌های امروز و آینده از درآمدهای نفتی است که باید صرف پروژه‌های زیرساختی و تولیدی شود.
https://farsnews.ir/N_bourbouri/1785349176168704923/</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farsna/453430" target="_blank">📅 23:05 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453429">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MFN1WciCS8_GXZbRsE7n6mr24RRs46x9OLFzC2eJGLW8oKJw-I8NlHxB4NMKKWUP2gs-nhCKKxWhNPBrVe-Ajg5XO589Iodo5PneDEoQcLO7MRJzdcmkbmEeaQnxse471Jhlduema8lmY9vhwAkA5-d33LtViYNhhCVBDmDTvNg4tFr88Go7fGOPwgS4eUskIDd6O3JvjGGRES23Pwr95dsFLUhm16JLPTVBbRxd_VBcxM6RNU-diLHS6kRwMV4M1Mpb_UIxZaHu_ZYd0seribhu5CMPWemFsuFyWJY9A1LlXLGqxRgQ9duZDgQxcysaTI9rzuVE18FbNtpmDgVF8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عارف: آفریقا یک فرصت طلایی برای ایران است
🔹
معاون اول رئیس‌جمهور: اقتصاد آفریقا می‌تواند مکمل اقتصاد کشورمان باشد، اما متاسفانه در توسعه روابط با این قاره کم‌کاری شده است.
🔹
گسترش همکاری‌های اقتصادی و تجاری می‌تواند به هم‌گرایی بیشتر دیدگاه‌های سیاسی ایران و کشورهای آفریقایی در مجامع بین‌المللی منجر شود.
🔹
پس‌از ۲ جنگ تحمیلی اخیر ایران‌هراسی شکست خورده و اکنون فرصت طلایی برای گسترش روابط، به‌ویژه با کشورهای آفریقایی فراهم شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/farsna/453429" target="_blank">📅 22:57 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453428">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af6650ba10.mp4?token=QZ6aKyz_mVMCcBr53W5NjmyIVxyz7dR57S5yrFs2cc89X_Mi3-neflzxF9vLxp5ulJOeyeRjbzW_8Y5iZnmjsgI23jgPgEhujBnw7irOWnDeqPOUVRNl9CIL7vpJBBldwjXohaXl-Hs_9SF_NQZvf1pRZcA-y5yOBN1Q2uqoq0R6adpoh6_VKEymdoQRTzj8ZCM3MF_jrr_EUjCARjAyV5RJjefuVVWf8jEak8I_4_GcEvT13DNRv_KItAAy3dYLT0v9BZrBAlrlZeFfQj4S9fjZGQTO7V6rNXkCNBq2klnNVrYtLqBji9DNBaScmjEX_-zUTpw9QZSjp_-e02mLBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af6650ba10.mp4?token=QZ6aKyz_mVMCcBr53W5NjmyIVxyz7dR57S5yrFs2cc89X_Mi3-neflzxF9vLxp5ulJOeyeRjbzW_8Y5iZnmjsgI23jgPgEhujBnw7irOWnDeqPOUVRNl9CIL7vpJBBldwjXohaXl-Hs_9SF_NQZvf1pRZcA-y5yOBN1Q2uqoq0R6adpoh6_VKEymdoQRTzj8ZCM3MF_jrr_EUjCARjAyV5RJjefuVVWf8jEak8I_4_GcEvT13DNRv_KItAAy3dYLT0v9BZrBAlrlZeFfQj4S9fjZGQTO7V6rNXkCNBq2klnNVrYtLqBji9DNBaScmjEX_-zUTpw9QZSjp_-e02mLBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پرچم‌داری خون‌خواهی در مسیر نجف به کربلا
🔹
پرچم خون‌خواهی رهبر شهید انقلاب در موکب شهید حاج قاسم سلیمانی در عمود ۵۳۳ طریق نجف به کربلا برافراشته شده است.
@Farsna</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/farsna/453428" target="_blank">📅 22:45 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453427">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b95f960222.mp4?token=YW7DqNbcgWseih2mRu72RpGzPzVvBKKoBNR9tLMLpiWPBrsqqvnc4XRYQyS2mKrPPCvi1fQbwZDWHFY0XYc-qzNkTDnVLd90wn6OLdc-CeLfqor_X293E9cIQTffHcm15AuGsSZRX0Y0wISkmh-JeeoWVmgl-6RPpcAbpA1faoJXD1ciFohTFuTjajBm_DLNTXO1ZbPntQkPbH8o5a1BQLbO2rtHGMmODHkR_4FklCGUqZ9QThJeVCCTmJOkt6yffgpvDgQ4Qw6-uVrmMQgXIqxQ9tr1jcZwMlAmjLcHqWP12eJz3duTBxFuqMFfqNzI9uR4GWoQscrj-0xQoJN2-DzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b95f960222.mp4?token=YW7DqNbcgWseih2mRu72RpGzPzVvBKKoBNR9tLMLpiWPBrsqqvnc4XRYQyS2mKrPPCvi1fQbwZDWHFY0XYc-qzNkTDnVLd90wn6OLdc-CeLfqor_X293E9cIQTffHcm15AuGsSZRX0Y0wISkmh-JeeoWVmgl-6RPpcAbpA1faoJXD1ciFohTFuTjajBm_DLNTXO1ZbPntQkPbH8o5a1BQLbO2rtHGMmODHkR_4FklCGUqZ9QThJeVCCTmJOkt6yffgpvDgQ4Qw6-uVrmMQgXIqxQ9tr1jcZwMlAmjLcHqWP12eJz3duTBxFuqMFfqNzI9uR4GWoQscrj-0xQoJN2-DzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
موج ۱۵۱ میدان‌داری مردم در تربت‌حیدریه
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farsna/453427" target="_blank">📅 22:40 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453426">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0bfdd4de7.mp4?token=R3_wS_XiAyUkisYIM6KCbsLwl6-CSwsd4XH3E4avze0X5zlVqeiL0O4bzHVfOkb2Sg9THkFmSAYyQacEwuDmdnZlDu_twFNFTDfTzwCczsAOo2ljPQWb6IrNp7pYoOjCTPRPZtcbetRM0ZH6H65bxV3pxkPXUHE7zzyiO8RupVZahB_QkjC73ujhRSVuoiqNBe1En0ydjumNfpFhtfquuSxgJrQg_15Uv8ZIPM_4xaFpN_OMHhMOvtifMXcB11Uw7-Oy3fmiZFf14Fk71Zw98gfLTuOxVH4lRifMA72Nds67V_stw8nBrb9zWSUNfnBg49QdIcx8HbdMNztuEVPE3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0bfdd4de7.mp4?token=R3_wS_XiAyUkisYIM6KCbsLwl6-CSwsd4XH3E4avze0X5zlVqeiL0O4bzHVfOkb2Sg9THkFmSAYyQacEwuDmdnZlDu_twFNFTDfTzwCczsAOo2ljPQWb6IrNp7pYoOjCTPRPZtcbetRM0ZH6H65bxV3pxkPXUHE7zzyiO8RupVZahB_QkjC73ujhRSVuoiqNBe1En0ydjumNfpFhtfquuSxgJrQg_15Uv8ZIPM_4xaFpN_OMHhMOvtifMXcB11Uw7-Oy3fmiZFf14Fk71Zw98gfLTuOxVH4lRifMA72Nds67V_stw8nBrb9zWSUNfnBg49QdIcx8HbdMNztuEVPE3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی شورای نگهبان: در جنگ با دشمن نباید مشغول خود شویم
🔹
در پیام رهبر انقلاب موضوع وحدت چندین‌بار مورد تأکید قرار گرفته و طبیعتاً هر اقدامی که ما را مشغول خود کند، عملاً به نفع دشمن خواهد بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/farsna/453426" target="_blank">📅 22:31 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453425">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9246e47830.mp4?token=EZ_U_Ve_7LACQ7BzmHoNWgZvWNRrWTnQIeb0mojhaOXyrWOZrTC_-DdjPId41N9Rg2aOhibMBdlzm_WycI_XUtQDeGB4A-GAle_--_vE52L2qvxasjxQ763FrBZCXeqKTMysFSO9WX9cbW-ucRWtJpjEwGswQ12hfMC96gsc5f1o0zwQYNuJLfWz02JuUxoBaR2MS7ZVNf7dv1mZZiomHGwzQkQNcsvLKXytFY13STXBWQzFFoV98S2w8MMlpuzFZJyCTA1yKzo95uf_hyIgQSP4982KPP28sgqqff_GH1GPYaLsBend7TC8FJhpa63CDrwYY6M56ws0AgaJqnZHOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9246e47830.mp4?token=EZ_U_Ve_7LACQ7BzmHoNWgZvWNRrWTnQIeb0mojhaOXyrWOZrTC_-DdjPId41N9Rg2aOhibMBdlzm_WycI_XUtQDeGB4A-GAle_--_vE52L2qvxasjxQ763FrBZCXeqKTMysFSO9WX9cbW-ucRWtJpjEwGswQ12hfMC96gsc5f1o0zwQYNuJLfWz02JuUxoBaR2MS7ZVNf7dv1mZZiomHGwzQkQNcsvLKXytFY13STXBWQzFFoV98S2w8MMlpuzFZJyCTA1yKzo95uf_hyIgQSP4982KPP28sgqqff_GH1GPYaLsBend7TC8FJhpa63CDrwYY6M56ws0AgaJqnZHOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
۳ کلید طلایی برای سفری امن در پیاده‌روی اربعین
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farsna/453425" target="_blank">📅 22:27 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453424">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d4522cb2d.mp4?token=RIRBMaKZToRs5uEGQDEOjzrZsHl_AT09TPXNLvMA4W64ndngow-8ZmoQIDnqHCaGcs7MyUqqONLtMWTSxseAO_b4BkOHPAJUC4MLCalFlifQV8iLV554yLpPiuFDh5JwL021PhFz2bSdWMtlx_1yR7H1FFb3SZzZq07rqVRMumH5UF1CS1bmdxoaVPnXe960DW_b2B5uDcPqiMhOotoFcIkj6A6rXZdGyYI1JZ1A8Qjmi1J1_--Dwl7SNJmE1ZJEgxHOgOU1R8U4wxmFWpUi9qwKSLfaw9iPfe-bOHFmiM4jiHWxIXejV55QGEoe8Ab63UM33PupXy7xvTwtxSIJ5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d4522cb2d.mp4?token=RIRBMaKZToRs5uEGQDEOjzrZsHl_AT09TPXNLvMA4W64ndngow-8ZmoQIDnqHCaGcs7MyUqqONLtMWTSxseAO_b4BkOHPAJUC4MLCalFlifQV8iLV554yLpPiuFDh5JwL021PhFz2bSdWMtlx_1yR7H1FFb3SZzZq07rqVRMumH5UF1CS1bmdxoaVPnXe960DW_b2B5uDcPqiMhOotoFcIkj6A6rXZdGyYI1JZ1A8Qjmi1J1_--Dwl7SNJmE1ZJEgxHOgOU1R8U4wxmFWpUi9qwKSLfaw9iPfe-bOHFmiM4jiHWxIXejV55QGEoe8Ab63UM33PupXy7xvTwtxSIJ5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیس بانک مرکزی: از ماه پیش ترمز تورم را کشیدیم
🔹
در تیرماه نرخ تورم ماهانۀ ما نسبت به ماه قبل تقریبا نصف شد. این نشان می‌دهد روندی که برخی فکر می‌کردند در آن تورم بی‌محابا افزایش خواهد یافت کنترل شده. در ماه‌های آینده نیز کنترل بیشتری روی تورم خواهیم داشت.…</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/farsna/453424" target="_blank">📅 22:08 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453423">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6916d586f0.mp4?token=e_TKeMAdXKkt6KzGWScF2N0O_tQ60wC_2WhCkHfXhiPxb52NOTQQSHmHK6IDYGmGq9s7o7jwFyOTrTmpNNSiWhxtInrENWQuRvsZDYCshl24Ym2nyaBEzmKXeFMLLhSg14oL29aP3Ga-Tte_5eYLFaqxGJWNgdOP82M9uDtqWsbF1kFHXMs7g6ZAOgyAIBTj7r2UiAUIa1y4HphzA3KH0p7zVJlf1ugIeHoDa8O12SWwkyFTfpzie5BX18iHHVngsfzqtxdu7GM7IZO1TF0hlSvJBENDbAftIIm_L12dngwWfQHRXnCP_sgpqqh8y2-LCFo4T-C0Ntl6NivmIeujLyaKwXFnyOd9Fzcc6pPEnwmOCtm8ve7ThraJX73_viI04u8Jg6EBcGbnzwvv1kNh8mu1liKJtvrXvXBhXiByqPRr-3Ml2oFnQi1B8tMmMrSimyZPs7YBOpRSLFnBXboNNyiJsz4RDb7dKMjToc0upsrUFvtgeL-miqdfG2-BcTzaF-Uh7TJVobbgtkuhZp_3wQSKn42yxqjDdNRilEPnTLyaNCWDgXaBEfL4UrehTZtzFLxpZELyFcwJ2GhmlnwYx-Dn2bJVa99RIhktPgcNxeyJEtmA4ydvkBl5hZ05PjyiRDQMb0fpCCg7sQZFslj5Z1xRHAQpHn80mBdvz6N90Mc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6916d586f0.mp4?token=e_TKeMAdXKkt6KzGWScF2N0O_tQ60wC_2WhCkHfXhiPxb52NOTQQSHmHK6IDYGmGq9s7o7jwFyOTrTmpNNSiWhxtInrENWQuRvsZDYCshl24Ym2nyaBEzmKXeFMLLhSg14oL29aP3Ga-Tte_5eYLFaqxGJWNgdOP82M9uDtqWsbF1kFHXMs7g6ZAOgyAIBTj7r2UiAUIa1y4HphzA3KH0p7zVJlf1ugIeHoDa8O12SWwkyFTfpzie5BX18iHHVngsfzqtxdu7GM7IZO1TF0hlSvJBENDbAftIIm_L12dngwWfQHRXnCP_sgpqqh8y2-LCFo4T-C0Ntl6NivmIeujLyaKwXFnyOd9Fzcc6pPEnwmOCtm8ve7ThraJX73_viI04u8Jg6EBcGbnzwvv1kNh8mu1liKJtvrXvXBhXiByqPRr-3Ml2oFnQi1B8tMmMrSimyZPs7YBOpRSLFnBXboNNyiJsz4RDb7dKMjToc0upsrUFvtgeL-miqdfG2-BcTzaF-Uh7TJVobbgtkuhZp_3wQSKn42yxqjDdNRilEPnTLyaNCWDgXaBEfL4UrehTZtzFLxpZELyFcwJ2GhmlnwYx-Dn2bJVa99RIhktPgcNxeyJEtmA4ydvkBl5hZ05PjyiRDQMb0fpCCg7sQZFslj5Z1xRHAQpHn80mBdvz6N90Mc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
از شجرۀ طیبۀ تا شلمچه
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farsna/453423" target="_blank">📅 22:08 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453422">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb1f33ae39.mp4?token=ZLEslx-4RU4CjnQ7fJCgo3jo-b2Unz6T9_iC7CW6-cSYxvPrD7vmFxXR0hrQcXcrwHdHvd2Kd2LXDr_6TmYJXIb6Cgxp59T0IlnGErr3z3_ztqvXBAv287bO_HuFOKprvHE_bojMTCieIN_9XkgqdcDsFDXRnXm9CkbDLZ6_jxwZ8jmW7m1KqF8CaDgcNAcUUZcPkc9f0n7l-ojPGluFqj03SsZJBJilvW6FSgZ5jt0h5O-CSkcUEUSiyBPmK9y_cRynLIi3tzGZiTs3TaDsKn8EtCceZM-nbbQz45X--7zj9phtaBYfhP78sa9AmOZArF95-Q28w81tDHXnFY4tVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb1f33ae39.mp4?token=ZLEslx-4RU4CjnQ7fJCgo3jo-b2Unz6T9_iC7CW6-cSYxvPrD7vmFxXR0hrQcXcrwHdHvd2Kd2LXDr_6TmYJXIb6Cgxp59T0IlnGErr3z3_ztqvXBAv287bO_HuFOKprvHE_bojMTCieIN_9XkgqdcDsFDXRnXm9CkbDLZ6_jxwZ8jmW7m1KqF8CaDgcNAcUUZcPkc9f0n7l-ojPGluFqj03SsZJBJilvW6FSgZ5jt0h5O-CSkcUEUSiyBPmK9y_cRynLIi3tzGZiTs3TaDsKn8EtCceZM-nbbQz45X--7zj9phtaBYfhP78sa9AmOZArF95-Q28w81tDHXnFY4tVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رهبرمون هرچی بگه همونه
شعار مردم در پیاده‌روی اربعین
@Farsna</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farsna/453422" target="_blank">📅 22:03 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453421">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d9c20a073b.mp4?token=Hs4zMrWlLNyZMgPViXiSANTY7uJa8cAIN3za1xGiRRdhxC1IN0BAvdRG2a8DVCK0qTF5JpPwrzDyA18p-n56H1pwnFlZLj8CHVSiQKbUKPN89GruWxkxLePChyFT2vhXnQhd7ZaYR27tFFe3hSI1RCrOoP6HPOMeUlpYFU2LacIIYAu4nUYUOvHC0MCZZtlAEPGw-frdzEn7O4QCnLjee5JH54XttyzvePG0YGGUqMxDwXCChen6a3WG_R16KPuuP3tN8LpkPb34Nb0uJnzA1AmxsUMn_U4FqC31LUNZAMABby6wQ4GhUQCvZXEUzSLCjYHblSspnK4aa1HRlLkyI4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d9c20a073b.mp4?token=Hs4zMrWlLNyZMgPViXiSANTY7uJa8cAIN3za1xGiRRdhxC1IN0BAvdRG2a8DVCK0qTF5JpPwrzDyA18p-n56H1pwnFlZLj8CHVSiQKbUKPN89GruWxkxLePChyFT2vhXnQhd7ZaYR27tFFe3hSI1RCrOoP6HPOMeUlpYFU2LacIIYAu4nUYUOvHC0MCZZtlAEPGw-frdzEn7O4QCnLjee5JH54XttyzvePG0YGGUqMxDwXCChen6a3WG_R16KPuuP3tN8LpkPb34Nb0uJnzA1AmxsUMn_U4FqC31LUNZAMABby6wQ4GhUQCvZXEUzSLCjYHblSspnK4aa1HRlLkyI4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حملات سپاه چه بر سر پایگاه‌های آمریکا در اردن آورد؟
@Farsna</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farsna/453421" target="_blank">📅 21:57 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453420">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vq2tg0XmptoX2y1cZhGo-dLhwdtlApFuq-tUzfL958GvOjF7qR0Qkqv0ZM0GI_nSUNgldt78W60pGgBYOJjq-u4Gmwox6DPrhaHFJiwKyUAOlLHy8g-z_EW4gxv0M5MyEYVTkdOGMbcc1eKPs6Vql89ReCm_YZHf69TXDJ2kxY1OYnHxk1TsH3yvdYVRL5F4mcDMV1PYkTJXND0JNcC1n7gMC1ccPYdfLOYMDEHDwSgwdet3qctAmkHyf0Nt045vQMFggoGYgVF7WZh5_PVeT-FW9qqrGInBKycgjxHKqEZONHu0pdawVWLg1KFBpbouhDKSFamAdL4yRMxSvLB4nQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
جزئیاتی از چند مأموریت غیرممکن نیروی هوایی ایران  @Farsna - Link</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/farsna/453420" target="_blank">📅 21:49 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453419">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/94ad19ca82.mp4?token=ZKXsOukdlPnaz08tx2YOgBRNWqb3r6tmAhXEN17A0Thhtp2XSVmsElu-pU6B78Dezuh1ZJwZ5Ig5BKjQnHUdxkG0IOBHrzV3yVBysNoHrp0xzN8CfYF4YQ7bNDLaIv2cYvQVQS86EAiKPLMGb-A5EV_MI0mj93PEgkmBCVPTbXHIECbRvcWRvG5wSKX4rbN9QJJmXRr-eA68bH1QpcBrTPjWwcMoJRCJwXkxTDgvHtkKLoPl55qUsBa_nR_kUuNWcTdyWQU_CS2_Dh-9vvU7L5vpn6FmF-nOvmTSEItvebDU01Sq6_0h6cmx0hSINM0-Ump3AeFaX34k-ki-CxleGa7kIhTK5141AcXpOw8XetgZWyjUMU_Ms6b9nxeocfg26fOrXEFCc0WREkRTvH01MaZf_yXMSj-vmb0CENMTlQITTiP45mYu1HoSyUfeDz_9LTHK_ymYHqTdX4agzaLXNWnBzNADqK3AgL_DiGVGSfxcq5odCV3oz28wKSPXK2pImU4GZp1M2DI_-Fvp17z-IkIdy2rtoSELi6gvoktTEATaUTzs9E6ZwIR_sZ9KHtbkO3i32B2y7JfGODcjdWBerZUe5qDwT_t8i1-WcYvU5sQmeI5X5DTbc1FtW9UhEX6OoiYu93-5IEJ8Syg301DZBAGTR_hv0oKn2LnO1GdTTrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/94ad19ca82.mp4?token=ZKXsOukdlPnaz08tx2YOgBRNWqb3r6tmAhXEN17A0Thhtp2XSVmsElu-pU6B78Dezuh1ZJwZ5Ig5BKjQnHUdxkG0IOBHrzV3yVBysNoHrp0xzN8CfYF4YQ7bNDLaIv2cYvQVQS86EAiKPLMGb-A5EV_MI0mj93PEgkmBCVPTbXHIECbRvcWRvG5wSKX4rbN9QJJmXRr-eA68bH1QpcBrTPjWwcMoJRCJwXkxTDgvHtkKLoPl55qUsBa_nR_kUuNWcTdyWQU_CS2_Dh-9vvU7L5vpn6FmF-nOvmTSEItvebDU01Sq6_0h6cmx0hSINM0-Ump3AeFaX34k-ki-CxleGa7kIhTK5141AcXpOw8XetgZWyjUMU_Ms6b9nxeocfg26fOrXEFCc0WREkRTvH01MaZf_yXMSj-vmb0CENMTlQITTiP45mYu1HoSyUfeDz_9LTHK_ymYHqTdX4agzaLXNWnBzNADqK3AgL_DiGVGSfxcq5odCV3oz28wKSPXK2pImU4GZp1M2DI_-Fvp17z-IkIdy2rtoSELi6gvoktTEATaUTzs9E6ZwIR_sZ9KHtbkO3i32B2y7JfGODcjdWBerZUe5qDwT_t8i1-WcYvU5sQmeI5X5DTbc1FtW9UhEX6OoiYu93-5IEJ8Syg301DZBAGTR_hv0oKn2LnO1GdTTrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شما روی این کاغذ نام چه کسی را می‌نویسید؟
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/farsna/453419" target="_blank">📅 21:45 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453416">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">بسته خط ۱۰۶.pdf</div>
  <div class="tg-doc-extra">2.8 MB</div>
</div>
<a href="https://t.me/farsna/453416" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">بسته خط ۱۰۵.pdf</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/farsna/453416" target="_blank">📅 21:44 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453415">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PxSyOcnLtJ4YgTgIxwyMU_s17KnwLuklK6c1Tz3qj58DuJGoToSG89I358e9slEL1GqQP_5q8Igzgc-DzLPXGq4uLLykZANM2MCWektPvjJLluD2ew1ViKLbEMIjR-Ifj-pL1lG59CbHtxsFk_QniiszgzZKSq_wQnMb7MwFIVKStcb3x_IGFyV8K0Qs5OZmxvhxysXLymCeJpMu9esaxC5yMsu4UclEbXRkkEOFS5Jk44EEW0_q8Sa8fJcyJ4NQFhpT7cSWDxZa6hwY8-0NIhuAxKbC2r3jUdcSoMkw06_eN3jksTQJfr0JhQqQYQNOK3atLlEmuRaV4KwLCjciBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جزئیات برنامه‌های وداع، تشییع و تدفین ۲ شهید بسیجی در مشهد  دوشنبه:
◾️
مراسم وداع: همزمان با نماز ظهر در رواق امام خمینی(ره) حرم رضوی
◾️
مراسم وداع: ساعت ۲۱:۰۰ در میدان سلمان فارسی
◾️
مراسم تشییع: ساعت ۲۲:۰۰ از چهارراه برق به سمت حرم رضوی   سه‌شنبه:
◾️
مراسم تدفین:…</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/farsna/453415" target="_blank">📅 21:38 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453414">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🔴
منابع عربی از شنیده‌شدن صدای چند انفجار در سلیمانیه عراق خبر می‌دهند.  @Farsna</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/farsna/453414" target="_blank">📅 21:31 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453413">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🔴
منابع عربی: نیروهای رژیم صهیونیستی درحال پیش‌روی به سمت دره الرقاد در خاک سوریه هستند؛ همزمان توپخانه این رژیم حملاتی به حومه غربی درعا دارد.
@Farsna</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/farsna/453413" target="_blank">📅 21:28 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453412">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🔴
منابع عربی از شنیده‌شدن صدای چند انفجار در سلیمانیه عراق خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/farsna/453412" target="_blank">📅 21:19 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453411">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JnwsPM9bdGfNnz9HpwiGNTd6X4bno7ZTHw2kyyVPDhuHPnbHOrY6LPpPcm9AxCaZDj6R1FnOVwkPLkiC062dRWOxP748wpauYmVqInWPLwsxhz7D-PKVFDxIin6ekchunDleDe-YiIV5HWEaSZg-k9QLhdxEaQEYS_b-v9iKs0S1aJ6564p8CrTAto9hp21qabK5H7F2l_rA_5NHvROAm4UjhzDhLVqaNlzVa_9Vt8cfyVmrRqWRctTjEFzqM6y7cgdEDxYxT-igWMIJHDlI2G8FmcZlzZZ45Y0Rzna7NfZH407SPl0Xxyl6lSMvvKtrVthR_pQ7teYQLbypH3Guuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برنامۀ امتحانات نهایی برگزارنشده پایۀ دوازدهم ۴ استان جنوبی
🔹
امتحانات نهایی برگزارنشده پایۀ دوازدهم استان‌های خوزستان، بوشهر، هرمزگان و سیستان‌وبلوچستان در روزهای ۱۵، ۱۷ و ۲۰ مردادماه برگزار می‌شود.
🔸
امتحانات نهایی پایه دوازدهم این استان‌ها که قرار بود از ۲۵ تیرماه برگزار شود، به دلیل شرایط خاص جنگی لغو شده بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/farsna/453411" target="_blank">📅 21:18 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453404">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YEUlQXZP7J06SBFAxkxMx5rJpLMD1H4AqKlyk8GgWIFeJl-gtK-rkVZcANh2_3cST7zdIGpSvQTrR-Z0cBcluv3Aa8jUu1qI7fk8xdDHBtmo-sXD3nYrsNwmZkoxZSJStnAYocdCalSTrBNaObN1hoTTSEoF-yCsQ9AtAr_k4nrU9QF6xmnBgnl5DS_96dP-7eoD8dlJ8Vie6eJF8umpCnw9ioN1-g05I8GC2bfaVVv92IqZdY20T1KJgO6J1cleQD4fUcrF7vX8nmtyQFyHCNcqLSl-pM7Q_KBNBJ8NPsq_P3gKobmADnhrjHWjkL3224uaaiWyEmEzat1aEwyLHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/njyKmE3RSLD6qstcT1rASteTvKdYvhH1jXZpmlNwBhfNoT7k2rIOhXDTCw-K4Oc1JKXS6QaOCY0dYcH6-480FxtBCubAwOf9G1jc0l-Tlt9ZxtY9n69Nbz7tc37GrdQSaTuySwc3uaFeJ6baSELrdbEGn4MQ36PssSf6UEbJLXIG8-40B2pcVEz1pMdfiC-FzGgR7cXfx6_LltDk7AxiQ3G6AABrmBEr-3l3K3yJbqb5BVKlJnrUYCgrJJb4_yZ6-aMVQvMBlfRz8u4G8EAbI_4WWcWtYqp77Tz2vrdf5J2PC4PtgkVyies7mFTz9_hQhR9OuJedV3CapUvvjzyy4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K5HWajHq11f1cz1ZyJHm4oU6fK4eaVKdjljV8Crj84Fv69V9Ezt3N4oZ-f_gbTg_Kj0U6HPUM6OGAm5e6t1FwgVLFJ_Ohhv-HVyhzA8P8yIWZcV-1yVrd5s-CtVGpK88jx3fv6GJhY3i38LpQh3Fp0fww6MIRneA8Twht5Ax34sE8W6HhK92t-Ar9K0prqwpAbN_pNzlvpvYeNbRF6c10YUJWzkXCirA-DJNqe81ejGR_G4dSpdv-DcuLiiQe4TZBvqK9czYtglAtYCTqROko16L7HNSMHDV7G8gvuuIfIkiRDt_gZL4bfFQy6CojJ2Iv9RtCVGv82fSz8bw9xwnxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WeGUJpe2qYgqwtHDwHkTkjt8M2ifHVcY1c6y1HXN5TyKJ_TIoQFa8scgUjGE4wFOxD5l0xGsxvfQpoLoc8jz8po_XjSnuuJ3PLJNVWXXHNnwIp07egh-hM1LHsnokgN4NMBr7PW-fQ2rKpkiuK-lWYnsshW5xEJLm0GSvq5z44KFR-Bbd5RPoyXSPJKPUmVOJ-XpuFxcdBOkbiHJeyZUuwJt9GPEaHOGeUzeD1azWkv3B0oeB5NvPPMw4OlaMvXSYZzQbotXKHbbA0oY49X_SZQr9s71px3yua5ve0aby3jn6WqjJxoskvRsAzTVPD067c2GJU3izIUghtW6wl9_9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KTaRkXCHhxFGfEO5ND1d8qSWjRN_Mrvsl4-Mr1oS01WSa8LRhQs1o-tWDgsdvMIW0UYtDh2cBZkqGfLGa7vwgtFLFSD8xJv_vzC7jPxa87xfTmiGkhYZ5XAIOsPyGMIjGEB6ogH6PyUxBU6yT2G6z1WwuffhYH_ozt1O3Il-iePzn__w5_liDp1XpLa6zAEdzo4c1tkYyr9EoqEAOV6PmULdGDaJbPL5fU15ebFz0FkjLD-I_OSoZi4pLDkD-l4aD6k-x_KTVvGHxuzq6kaRVjUcRG-7i45m8bsVfcI7sjzztm01fANba6PmJjgeY5TzaeVd-jc-mPTSJvDCcB7o0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fGfjmDD5lNNo_sHopCJd7fLfT9Cvbw1ijxHLVhe4Nrp1ggqKVkxJWS5ft_tV3O3kv41ezdccH-AF1RAKTK9ynQvvB-_DLE7rxG2ON5SEiF4bHhUM_RTBEG2pDyF5RGRq0n0f1NjPITjEdGqdgt6LlKD9UnS_nboRKs_KhXG3Z5OGnyXX4x8xGIbNdlA_51ihacrz-2PRDhAKo-hcZz566Hqq1pB-v3ZA7DKKpPjIevtFuw-J6FNcj-OEkRF4o-E3pef-aYRGNguNh2WBdJpZfD1yitDY_DvC4FmnKC8beox6WQYrpHgjURXHV76z9HQPtHPzBy0RokcQUJZpvk43yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Rvh5jWj3WOQzc1ZMam10SB906omrAwzUOLlo5fOVFzfKkLPeFY_MMh7LLwUniwO_c7II1KNIqfgXWovHvffqNiaegfJOR7nJT-tuBJQgY0OngZ-FF-r_reEoitCWh9DUr1MSgYBtDBqE3rAzoYh4A023r19tl-NfM5TSLYrILrI5CO4lNqeud1bVdtWtEWXl42MFJniXUtyWn1OPmTe841-q02UDImRhP-98pA52terR4You1hHA_V4hbeI2D3YeqR7hu7FaFH6PMUJSD_Ju7D3morBG_wFTJyFk-eq8_6I9DUwYiTbzblRGfTXcV6ZR4Yf45fE6_bty_9Njluddng.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
مراسم یادبود زنده‌یاد اکبر عبدی
عکس:
محمدحسن اصلانی
@Farsna</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farsna/453404" target="_blank">📅 21:13 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453403">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dea1178ca1.mp4?token=ZQUCmh0giOEYeleoTg9A_DWmVGio5Q2MY0Ku6qnXZN5qyi7aJR4sSj5nXdm2h96x3RTKgTb9KTZ6ndREd89AG1fLqiEyJCJqaptx41Wt8HhPItDPnopvMJ5gvkYrJ4HbIRUSHhhziEODgfG3m60AkXOgxq_5IaiscftTBQhmc9mgGTVDupDQFMD7eDnGGwrt8TppsE0xQ540mjLjRNXUsGXyWVUH5spsvBZw4A1iBjQVUnUeCPIh1sugsSZMdjQqrdOvUf_HofSOPtpn-UdxQAhBuPmrgcxFQFJTkS3dkEFUiwHjFHKxLeDw5gdK-67HtERpw8VHPF2hY9LAN1YKbL7AZpXz97W2X6NEhYsyK6VEq9qCAEodTd5AupmRcx2sJxJg4zw_ZaptsRssZA2LUKBNg3cXkNVi1Eo09yzlzphKKUfi4GbcnqJ0vupmXJcXcQYJ0OG7RMXbUHtOt6i0kK8188Aoh3uzA0oQWwAv6R-Fs0EI7F6ZzQ3S_t0iDr5NTA-aX6u2RfV7yAEB0c6HuM0oHA1wZqCkfMqkbC5tM7W5MondTvk3osD8XJ4yTliXYcRxbNb7DaWTJI_fSz2v7RrT7P_U8jv_1cmjY10ZIJJ9cV5X3Sne9nwJn9EfJdp5JZUAMkvtANtBLVYc9Z6ocNH-AQ_sB4p50wAaDtSCBWU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dea1178ca1.mp4?token=ZQUCmh0giOEYeleoTg9A_DWmVGio5Q2MY0Ku6qnXZN5qyi7aJR4sSj5nXdm2h96x3RTKgTb9KTZ6ndREd89AG1fLqiEyJCJqaptx41Wt8HhPItDPnopvMJ5gvkYrJ4HbIRUSHhhziEODgfG3m60AkXOgxq_5IaiscftTBQhmc9mgGTVDupDQFMD7eDnGGwrt8TppsE0xQ540mjLjRNXUsGXyWVUH5spsvBZw4A1iBjQVUnUeCPIh1sugsSZMdjQqrdOvUf_HofSOPtpn-UdxQAhBuPmrgcxFQFJTkS3dkEFUiwHjFHKxLeDw5gdK-67HtERpw8VHPF2hY9LAN1YKbL7AZpXz97W2X6NEhYsyK6VEq9qCAEodTd5AupmRcx2sJxJg4zw_ZaptsRssZA2LUKBNg3cXkNVi1Eo09yzlzphKKUfi4GbcnqJ0vupmXJcXcQYJ0OG7RMXbUHtOt6i0kK8188Aoh3uzA0oQWwAv6R-Fs0EI7F6ZzQ3S_t0iDr5NTA-aX6u2RfV7yAEB0c6HuM0oHA1wZqCkfMqkbC5tM7W5MondTvk3osD8XJ4yTliXYcRxbNb7DaWTJI_fSz2v7RrT7P_U8jv_1cmjY10ZIJJ9cV5X3Sne9nwJn9EfJdp5JZUAMkvtANtBLVYc9Z6ocNH-AQ_sB4p50wAaDtSCBWU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
کشیده شدن درگیری‌ها به حوزه دریای مدیترانه چه معنایی دارد؟
@Farsna</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farsna/453403" target="_blank">📅 21:08 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453402">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b491f68d88.mp4?token=axlTS7Kkhht18YXuAdKwHajkhsnKKJqvdnoasH3Sio-Z5Fwf-ODiNlfLByMNpystOGRs3V9IcahQSYXhaqixDK8zKpcM5ogKiv5DCmc03JBXvKAOmRnGN7gau2X1q24yp2A6jwDWCpv5QpG9shvtU-EYN_w4f889zxgQkE9Dt4ptnDXD5gBlC16gV9Tae4VKUsnr3zNskXktxLzVHLN8mXFuDmyIJ45MEu8h7GY11zREw9JdZ8Fd2PJXgh7OtJHQFtBBhPah4BNyoAtDoFxKYTag3BZqWRfj_zfK-_AqDfZyhyprNS2aeT_sNVyOtV2I_yC1ThOxQY4N7o533y81qVZ1UH1BUUWFnx0nUNLsvnT89Wwqhcsovj4c1NkUUwDFPEJfDjYeTCZGywC8otdx3JjJIpfEazFyJb3nWTK6rwAqoESOOJivov_IF3fuCGk47JfuzKiSnceL9D0pel4w5oaO-h3pR3LIizbIPYhQLs0jNZdEEcvDzyrqJRZfWdYnUBL4JRMUjvgoEc7ZRo4CQ4S8yPJj7dyliLjr9c1uHHp9nyGJqIhzxWYP44Nut3NIHdbN7K--JZIGPWPq_aXa5D7dpAOUGP6HfZoPNmlaNOSQxjkoDHTyvf7WpZYt1qHjEJEjqXk05dyshIgg1D32yzklbOcXqxO48aZtZ7j7ruc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b491f68d88.mp4?token=axlTS7Kkhht18YXuAdKwHajkhsnKKJqvdnoasH3Sio-Z5Fwf-ODiNlfLByMNpystOGRs3V9IcahQSYXhaqixDK8zKpcM5ogKiv5DCmc03JBXvKAOmRnGN7gau2X1q24yp2A6jwDWCpv5QpG9shvtU-EYN_w4f889zxgQkE9Dt4ptnDXD5gBlC16gV9Tae4VKUsnr3zNskXktxLzVHLN8mXFuDmyIJ45MEu8h7GY11zREw9JdZ8Fd2PJXgh7OtJHQFtBBhPah4BNyoAtDoFxKYTag3BZqWRfj_zfK-_AqDfZyhyprNS2aeT_sNVyOtV2I_yC1ThOxQY4N7o533y81qVZ1UH1BUUWFnx0nUNLsvnT89Wwqhcsovj4c1NkUUwDFPEJfDjYeTCZGywC8otdx3JjJIpfEazFyJb3nWTK6rwAqoESOOJivov_IF3fuCGk47JfuzKiSnceL9D0pel4w5oaO-h3pR3LIizbIPYhQLs0jNZdEEcvDzyrqJRZfWdYnUBL4JRMUjvgoEc7ZRo4CQ4S8yPJj7dyliLjr9c1uHHp9nyGJqIhzxWYP44Nut3NIHdbN7K--JZIGPWPq_aXa5D7dpAOUGP6HfZoPNmlaNOSQxjkoDHTyvf7WpZYt1qHjEJEjqXk05dyshIgg1D32yzklbOcXqxO48aZtZ7j7ruc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
«خیابان با ما» به مشایه رسید
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farsna/453402" target="_blank">📅 21:03 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453401">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6175f46d57.mp4?token=LzozulLTj6T4oVu7pQjuGD5XltqcMLmUyRWaaePR8iolizB1Xe39mifhXeYVxByPNyHwOUFu4E2UGrCz-V8bqacDlcxLYNCH836itrhD32MCd3xQKtye1X1XqDsHWmQi-duPGug08waYttny-7qGq4-H3rGbmC5RusHjYQEHnBMHd-rqafOYxZObQkpOujp0CnuZAf5OMs6XqPfxF1QR9YlSm5EOA2DykQP5r5b6W580wXgKcOVjIj5kmO2GpwNGJxc2hxiPvstK-7aBR5T94Z-K8XiC5osuOhzqxUnSoSOeQMPnkrlNb9qQnOK9OuJAGW1O21vb39sTYZCfdeihaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6175f46d57.mp4?token=LzozulLTj6T4oVu7pQjuGD5XltqcMLmUyRWaaePR8iolizB1Xe39mifhXeYVxByPNyHwOUFu4E2UGrCz-V8bqacDlcxLYNCH836itrhD32MCd3xQKtye1X1XqDsHWmQi-duPGug08waYttny-7qGq4-H3rGbmC5RusHjYQEHnBMHd-rqafOYxZObQkpOujp0CnuZAf5OMs6XqPfxF1QR9YlSm5EOA2DykQP5r5b6W580wXgKcOVjIj5kmO2GpwNGJxc2hxiPvstK-7aBR5T94Z-K8XiC5osuOhzqxUnSoSOeQMPnkrlNb9qQnOK9OuJAGW1O21vb39sTYZCfdeihaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مردم عراق! ما این اتفاق را فراموش نمی‌کنیم  @Farsna - Link</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/farsna/453401" target="_blank">📅 20:41 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453400">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gSM9vUsdE0bOTAgiylPSo8bob-3619w8lhVxv7NqZ66VtC-mG3JzDHXWOm-pq0buDJtPsgphX_YDUu3p-mQDvpfcO3u5gY0SDs10tpoIOftHX__4DNDTkYDfOLSyuYchSaz6O9jMbEdn3FNWDi7nOB3xzdtunAQPTEhCf8Sgwb5IU8emCkGpvXguNde4iMGX0RrqXR51g4h0RHE9qe3eeNRYUPLsTWFqGjYU_vUVUA7IdAWRR9sEcNrRYi5SmbawRfpCg2Tsayx4JvvdkDd1jkhvNA1XC8UmRq7oM3q31Rw_FLfPIX6pSjVFXvEkxXidfEKgDV2onufDVmouJD1v7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرمانده کل ارتش: تا آخرین قطرۀ خون از خاک پاک ایران دفاع می‌کنیم
🔹
سرلشکر حاتمی در پیامی به‌مناسبت شهادت امیر سرتیپ دوم خلبان کاظمی: شهید کاظمی و همرزمانش قهرمانان حقیقی ملت ایران هستند؛ آسمان ایران، میدان رشادت مردانی است که جان خویش را سپر ملت کرده‌اند.
🔹
ارتش، بر عهد خود با ملت استوار است و تا آخرین نفس، از نظام مقدس جمهوری اسلامی و خاک پاک ایران و استقلال آن در مقابل متجاوزان، دفاع خواهد کرد.
🔹
شهید کاظمی و سه همرزم دلاورشان که خالصانه برای سلامتی آن‌ها دعا می‌کنیم، نیز در همین مسیر پرافتخار گام برداشتند و نامشان را برای همیشه در کنار این بزرگان به ثبت رساندند تا نسل جدید ایران، الگویی راستین و حقیقی از قهرمانان را در مقابل خویش داشته باشند.
@Farsna</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/farsna/453400" target="_blank">📅 20:21 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453399">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VzyOAYnsKZSjTnNLDRpIn92Meiee2i1h7xVAXehiPxIdR8xOapCxLQzWJ_sv49dPjxSVj9-FuYvkCQaamUbuwl_IKvBAkFiFmZAjd55V_0pj3VnBVYiZiDOLCJ33xYvfxXeUpbmaEi56kFal1ycEaRU5efiqUlPKHXV_m1J5IBx-TK2NW-RYgB_irB2XE6et8ckNBCbpDuyAuLy_fATxwc_2g1vHhy5yPIkUM3cTvCzrWReYpVIwaxZYHgG4tpoEI8sCsBaqmDb5Yphld3xzzGqC2rLCMVpjcih-5Sy7Ut_DUOJ15KBBwVHDR23BtRr7LUE694lSPk6dYBcQ2TSuEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یمن درحال بررسی دریافت عوارض از کشتی‌های عبوری باب‌المندب
🔹
رویترز به‌نقل از منابع آگاه مدعی شد یمن درحال بررسی طرحی برای دریافت عوارض از کشتی‌های تجاری عبوری از تنگه باب‌المندب و جنوب دریای سرخ است.
🔹
به‌نوشتۀ رویترز، هرگونه محدودیت یا تغییر در تردد باب‌المندب می‌تواند مسیر جایگزین صادرات نفت عربستان را تحت تأثیر قرار دهد و نگرانی‌ها دربارۀ عرضه جهانی نفت را افزایش دهد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farsna/453399" target="_blank">📅 20:15 · 07 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
