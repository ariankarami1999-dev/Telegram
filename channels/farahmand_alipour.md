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
<img src="https://cdn4.telesco.pe/file/pTnNNOoQhFAKJ-svZzj24VhS1yuHiUw0oZOZilKHSnJbdtdclPKIn_vnSoUjtCdzlTWUc_iVnQsFUY9e9geBRiUQM8cfXKJBFpgTu7TVQxzpGBPTyvllJgp4ACw35-t0-UIHAop_FyzwURNLVst76ki4oJ_aauZK6pnU3kTHqkEGuH6KWbTpycDesf7gi26hLSLxlpyRaV9c8aB5JiMM_A0rWwhrx10NoYg05FBv7iwItQwXhoCNgOmHCWEC2x15qX-NeLjvSSmaKBxrS9UU71fpzb_6qKmTvKoNE89pdfXDymB4UIEixgaJw1tJIorgiej84MMQOvs_lpHO4X1rYA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 64.9K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-09 14:51:53</div>
<hr>

<div class="tg-post" id="msg-6448">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cabfb827a1.mp4?token=epwSbDFccUQ7k0o5tbn8RVo6rNJUHV5KrpNQfy6PqGMnjPhLqBGAHst5B1CVf4A4EKaefDz1-TnVcvyazkzZP_rcTlsJLudy61CIoKrEx7BGt3QL9HliAkuLG9fZZ5niJXG0TtMsAA74MKHv46_8okFsy1D3v8gxfL82x_8akuWzHRjRp5zdNul8sVlgDv5ZtVjOdIN8CPYm0px4wKoDRUrH-R3e-DwE8sINQb8BF8DuwSRYPlMtL3g2LxDQ4CVQcPeh3pywkJS9fevYclGnsHmUwLaNZQHibmYDzZpNVvctzocsNCt4OpAadWcmRBHp3Nt5DAyofyCPR2t-GDfdAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cabfb827a1.mp4?token=epwSbDFccUQ7k0o5tbn8RVo6rNJUHV5KrpNQfy6PqGMnjPhLqBGAHst5B1CVf4A4EKaefDz1-TnVcvyazkzZP_rcTlsJLudy61CIoKrEx7BGt3QL9HliAkuLG9fZZ5niJXG0TtMsAA74MKHv46_8okFsy1D3v8gxfL82x_8akuWzHRjRp5zdNul8sVlgDv5ZtVjOdIN8CPYm0px4wKoDRUrH-R3e-DwE8sINQb8BF8DuwSRYPlMtL3g2LxDQ4CVQcPeh3pywkJS9fevYclGnsHmUwLaNZQHibmYDzZpNVvctzocsNCt4OpAadWcmRBHp3Nt5DAyofyCPR2t-GDfdAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الان خاصیت ابوذر چی بود؟  دستاوردش برای انسان چی بود؟؟  به اندازه یک قرص سر درد،  تونست به بشریت خدمت برسونه که میگی هزار بوعلی و رازی و….. خدمت کنه؟  اینها روشنفکرهای ما بودن!!  این‌ها بت‌های یک نسل از ایرانی‌ها بودن که ثمره افکارشون رو داریم می‌بینیم!ً</div>
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/farahmand_alipour/6448" target="_blank">📅 14:42 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6447">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KEXtfY8-FEUVtVRd5xFjB7FTDSe3H-iwxnqqV4pDaLdkv0y7wbH0AXhiWInvM1lBBqrvzxqKv2iNdnxi0KUn1Ar_hxL1JYTFcgkKNVTDAzSFwNpn4JAq4ySOeEHQ0G2P827Nz3JrOA_hK1_ex3B-i-CB-8rjALMoiXsNCrr55NwigTZEG4TpaGuYWY8FxGPhSh33Rvg49G_ah-EwktzSJjGN0mYDf5sN8LvAcuuG5TRqW_b6ZQCm1IiFiBoABDuYEQub4Gx9WXdbQZMWwV0To61Ic3vgcleuZTBnmShL9terCQdWPlTGWrZBtNBeGNtE3D1XpjQgYNvBYjV_OpIW-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الان خاصیت ابوذر چی بود؟
دستاوردش برای انسان چی بود؟؟
به اندازه یک قرص سر درد،
تونست به بشریت خدمت برسونه که میگی هزار بوعلی و رازی و….. خدمت کنه؟
اینها روشنفکرهای ما بودن!!
این‌ها بت‌های یک نسل از ایرانی‌ها بودن
که ثمره افکارشون رو داریم می‌بینیم!ً</div>
<div class="tg-footer">👁️ 2.2K · <a href="https://t.me/farahmand_alipour/6447" target="_blank">📅 14:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6445">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CfZx36Wi5lQqPuJ_gPvT0mMZDEZQF00NlXCK9EKwp0-dG8tAODX__HY_vJX_DCc755jPQfUKDLOkxWLLZFGnwZo2DWamH8MeoMDsyZkeQAuYOI7NGfHkDiN08echvNQQ9SFqNNQ_Wl-zU3jGdfSTjKosq7QYhrf45rJ3VQpjQMxiTIf3erJSTroBo_P2cA80MzmxUn8pI2-bxL3kqYRkHkIc4qX1wkOTHqgyq6OOd60N9jyEQQ_ae8w-z4nfhIGaIrpJe5K57R_afSY1XF2D8YmFx9f_-Az9Hxu6aNCU2JO9jXBYQYy69WBbvW6hQ8AvQwJe7TIDJJAOKbxpiO0a4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b1bde678e.mp4?token=LTHqfxYDFX9FQyRYtj35fZ1uNH_BzHuTEMeWqjC-DVUSIyTBf-6nL48D7ZIy2J6T2qpluIEEqBFPB6HzBz3KZOlKtPkZG_x42VFAIitGx--CAeLc9t7G-0fvRDaGs_sNESBXyaSoX8SeF47KQKdVWaY-v-gB6vU0hW021LW0VN0QgdrCBA-7tb4nZVPmRb1JwETJRZtD3DF2ObfXfZ0pdHc6veIuWMcsDlmCecmWo_xUhG_nA-HJ_t4lw7xsM15ZbwoP-InoCbeKZU2F8w4FQuyr0Xb24g5Hd2hPM4mFdWFwFrnLMdRWTWFCTJPeX-OY62fawYZ6nTgh00nnXaZCeIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b1bde678e.mp4?token=LTHqfxYDFX9FQyRYtj35fZ1uNH_BzHuTEMeWqjC-DVUSIyTBf-6nL48D7ZIy2J6T2qpluIEEqBFPB6HzBz3KZOlKtPkZG_x42VFAIitGx--CAeLc9t7G-0fvRDaGs_sNESBXyaSoX8SeF47KQKdVWaY-v-gB6vU0hW021LW0VN0QgdrCBA-7tb4nZVPmRb1JwETJRZtD3DF2ObfXfZ0pdHc6veIuWMcsDlmCecmWo_xUhG_nA-HJ_t4lw7xsM15ZbwoP-InoCbeKZU2F8w4FQuyr0Xb24g5Hd2hPM4mFdWFwFrnLMdRWTWFCTJPeX-OY62fawYZ6nTgh00nnXaZCeIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شما مشکل کفش‌هاتون توی مسجد
رو حل کنید که پلاستیک به دست نچرخید،
نمیخواد نظم جهانی بسازید!</div>
<div class="tg-footer">👁️ 6.34K · <a href="https://t.me/farahmand_alipour/6445" target="_blank">📅 13:50 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6444">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lgtHC_qJ3yPN5gzII6XHeuqTd4-0_vxnG8uyTzXE702JvuuVUTF2siLBGhcnSCP7FM8g8V9G_pGvlZOJncapPROPh6s5NVnJmBKvkUr_juobyxrmNYlUHRdpJo4Chha1Tb5fOJ76rwxVH-i97Nl8FCQAabAunyxf5YYuFaCzMMHONRkTWTwSL7Ygxzkk3ePLj9uRRWQ4wQZsd2vRjWN4oFsEqkflsQ4B-DW5Ol8m-QTk37u8XCZvJQD7ZFDVWgoCU3OqAaBjPHygSWPBeSdlbzfqEn1t71MvAvmHXBbQCmPNR-uoKoHNM5SvX74A6NosDqVM8mXLJjfDCGNKsV7VqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عباس عراقچی ۶-۷ جمله نوشته که خط به خطش دروغه!
نوشته که مصر یک شریک مهم منطقه‌ای برای ماست و نمی‌دونم امنیتش برای ما فوق‌العاده مهمه!
در حالی که مصر و جمهوری اسلامی ۴۷ ساله هیچ رابطه‌ای ندارن و مصر حتی ویزای توریستی هم به شهروندان ایرانی نمیده!
همون موقع که پروازهای جهانی در اوج بود، حتی یک پرواز بین دو کشور هم نبود!
نوشته که اسرائیل علیه اتحاد و همبستگی اسلامی است!!
مصر حتی برای کشته شدن خامنه‌ای، یک خط تسلیت هم نفرستاد! براش این اندازه هم اهمیتی نداشت! کدوم همبستگی؟؟!
🔺
دیروز به دو کشتی حامل گاز مایع در مصر حمله پهپادی شد، دو تن از مقامات ج‌ا به روباز گفتن این فقط یک هشدار بوده از سوی ما.
دمپایی پوشان یمنی هم گفتن کار ما نبوده!
حالا این اومده میگه ما روابط مهمی داریم و همبستگی اسلامی!!</div>
<div class="tg-footer">👁️ 8.25K · <a href="https://t.me/farahmand_alipour/6444" target="_blank">📅 13:27 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6443">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vbjCfFse6t1YbjGml3SlfdHI1-j75JHeGDhn4CS_Sz-Rd--b5MZznij5rB4fQ4rEKfwImdBEWA-mRXcsH0yGj4aSfxDjXKmsln8BTxFIyRyf27zQwZMl5Phoen1u2BSs-VNlElHQzEHHRLuJqzEbHgJFBpglCiSpdMe3gbomE3CGpb1yXPwMsydJY8PR4jOBjywxPBDamF1tyPmULlV3w2BgKY54m-6EcAgSpIZ2NnxkQHMUws0yY5A-jGdlu1A3uzjBtvABiqALg-v8C9G-MZ_Sn4QaMV6CaiaelQ_J-JpPbTah2xg8Bp7h8loPSGRqbuEO7jK6KHPygUymChN3bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپاه امروز هم اعلام کرده که به دو نفتکش در تنگه هرمز حمله کرده.</div>
<div class="tg-footer">👁️ 8.34K · <a href="https://t.me/farahmand_alipour/6443" target="_blank">📅 13:21 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6442">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ijcuw-5ciz40_ZiXHg2sKAPVPZyWFNrZQtAhsx7FqEbRaazz7BOdbQN8yzPmu5qTLeTuFmcwl2EMLvTaiuOuynvhn409RihWd4PZ5omK_iazIXLuGekF3Ag-hgek_HltpzsEh0ivN4vZNnYH0T58qZI0Y5m5FjeKxDxlYnLGq3BsjQmBaM4-R25cYQHi8FKhxjZDjLeJ2bO4PAKQV-IWNoEpWFRRXED2FJ3W6kG2kNahCVnT-0712xBrQJnXME6QjAUmRBFoynV5oEFdLMbm9r--RLz_nmNqrnTT7cUPKFuCuN9YQLKQgzBerGthXkXfLAbNEt8lEgtW1W2QVDAmSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حدود ۵۰ هزار نفر عمدتا مردان جوان
در ۲۴ ساعت
گذشته وارد شهر ۸۰ هزار نفری
سئوتا در اسپانیا شدند.
🔺
احضار سفیر ایتالیا در مادرید.
در پی انتقادهای دولت ایتالیا به دولت چپگرای «سانچز» در عدم کنترل مرزها
و درخواست بستن فضای شینگن بر روی اسپانیا، موجب خشم دولت اسپانیا شده است.</div>
<div class="tg-footer">👁️ 8.22K · <a href="https://t.me/farahmand_alipour/6442" target="_blank">📅 13:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6441">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qAHnLNTXX17KBO8A2FlITftp3ArkHMx6mKWlLst-7rve8nuDGMVlC--DjOFkl8yRGwtvmQB8s_av19MjbQO1jpmUH5tr-YZhWPCBnRWGFJgzJHeL3D586KNKr9VNhozBSO4vgSAOMjARBVM9Y_6hecjkSUcnVFR8w9pTsfM_IKfuleFulEYl9p3G3I4Olvyami_039-0MUBEjrr23XjXhgL-inJa5TEhnmmiRUnDUPKR7acYbKadZcrKhtNFMGG4AeJLGcCGpubd1iXrJWGiA0cWYAbh5GdP9YWjgwQaEUoiMI5UdGoiRLN8MYCoIc6kLSnj-xEgtC0eF1TcOTkjJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه بار هم درباره حجاب نوشتم،
در حالی که اکثر زنان جهان اسلام
(نمیگم همه‌شون، ولی اکثریتشون)
دوست دارند مثل زن‌های غربی لباس بپوشن و…..
زنان غربی هیچ تمایل و انگیزه ای
به لباس‌های زنان کشورهای اسلامی و چادر و مقنعه
و عبا و نقاب و برقع و پوشیه و ……. ندارند!
نیاز نیست حاصل تمدنی که اسلام
و جامعه‌ای که ساخته رو در ده تا کتاب قطور جستجو کرد! همینکه جمهوری اسلامی با حکم
«۷۰ ضربه شلاق» و «گشت ارشاد» و بگیر و ببند و پلمب، ظاهر حکومت و فرهنگ اسلامی رو حفظ میکنه، نشون میده، این تمدنی که میگن،  یک آدم برفی و یک توهم بیش نیست!  که به سرعت آب میشه و میره!
فعلا پول نفت پشت سرشه و بگیر و ببند!
حاصل ۱۴۰۰ سال عمر و ریختن ثروت و اموال مردم ده‌ها
کشور برای صدها سال به پای این درخت، هیچی نبوده!
نه هنر، نه علوم انسانی، نه صنعت، هیچی!</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farahmand_alipour/6441" target="_blank">📅 10:31 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6440">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VQkPLrhj-titKRKHHAP81Rfz5Glgg1fVqesasC1Mh4NJOZRWF24RbgqT8632qm_Uvas5TFV8ZOWdTSei84_Y73KLfdVdkBZzwvrUx4Q7YISmLlN5W92iPhIOVBCDKPy-1o9BfskNYqwZ5VkLlm2SfXG6SCoqYaVqOJSlHiblQwi8W_kSKkv_extXawn4EI7f__UPF6AZ1j046tKtlFrCd1eMoB9OVzLLwdQsGHeyBDm88Z9eWaP9HPhtYiLUgqlmWTKBgxrMWBCWP5JxDhZ6cw3eX_bTMygLFesO4tP2jDhYzMI3XSi6rlAU_hobFX1SXs65CHpOM2DT4zGUHtyE4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منطقه‌ای در شمال مراکش نوشته :« راه سخت است، اما رؤیا ارزشش را دارد.» پرچم اسپانیا</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farahmand_alipour/6440" target="_blank">📅 10:31 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6439">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3f328eb8c.mp4?token=DhXAyoJPTontX84o6DyJIAEe2y45_OTOi9ukfE80_TgXVT_nEob-JV7wWlOxYykNkC156oRQxW2GfXrXL6hztzArz4yBRPYxhVgU2rdf0CREtYBC1jwSH42CMwTV-4akA892dz3DhC0zI3ookcNXXS_ZyUfvV49pRM8g4zl_riQN-S9-jlV7wdXX56Fuk7SNt9b1Ht7x0DfKa1xt2vbFZcTq8Gm7f0I3JP0fjvIG0VrAiNexpkgPV49pfNXHvB6BnDph9HYL3mt367AJD39FepSPgvCz9AiJ54qAnTgHFyS-5opN3st8D8WmUmU548uLpkKkntW2wmlquc3BoMGaJTbJSpqbqSaOCek2vdptcdZUu4kyEq5SZTIs0BfZPVY7YFEAkjrJLQ6oNUGUPW_FXV1TuLMrCt4NorkCr_W2QwBW2KGd6WMhWKthJn6rQIHY2_ihhjonyp2rYAQxoiqzjKaSwm6bWAq3fnAqHjvjtdO63qTBfy2gw8CR5q1i4cd0Ma3QTER7UzJF9qp0yp0NApfwuLFxjHf2TFOkDDgavENc5pvQB8qrb_oPpmZB1wnYE3Tjiv79-ccH96dWD0qBxHYTpChQRaiKLqYKsmo-vI9pd8XjfFY8YNsJx3e7lkGWxFbuBelrCIaFIAoeIzJ-Ylwe-napoYGevUq4aEFhlWk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3f328eb8c.mp4?token=DhXAyoJPTontX84o6DyJIAEe2y45_OTOi9ukfE80_TgXVT_nEob-JV7wWlOxYykNkC156oRQxW2GfXrXL6hztzArz4yBRPYxhVgU2rdf0CREtYBC1jwSH42CMwTV-4akA892dz3DhC0zI3ookcNXXS_ZyUfvV49pRM8g4zl_riQN-S9-jlV7wdXX56Fuk7SNt9b1Ht7x0DfKa1xt2vbFZcTq8Gm7f0I3JP0fjvIG0VrAiNexpkgPV49pfNXHvB6BnDph9HYL3mt367AJD39FepSPgvCz9AiJ54qAnTgHFyS-5opN3st8D8WmUmU548uLpkKkntW2wmlquc3BoMGaJTbJSpqbqSaOCek2vdptcdZUu4kyEq5SZTIs0BfZPVY7YFEAkjrJLQ6oNUGUPW_FXV1TuLMrCt4NorkCr_W2QwBW2KGd6WMhWKthJn6rQIHY2_ihhjonyp2rYAQxoiqzjKaSwm6bWAq3fnAqHjvjtdO63qTBfy2gw8CR5q1i4cd0Ma3QTER7UzJF9qp0yp0NApfwuLFxjHf2TFOkDDgavENc5pvQB8qrb_oPpmZB1wnYE3Tjiv79-ccH96dWD0qBxHYTpChQRaiKLqYKsmo-vI9pd8XjfFY8YNsJx3e7lkGWxFbuBelrCIaFIAoeIzJ-Ylwe-napoYGevUq4aEFhlWk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت دیشب سئوتا  خامنه‌ای هم نیست که بیاد همدردی کنه با جوانان غیور و به پاخواسته مسلمان</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farahmand_alipour/6439" target="_blank">📅 10:17 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6437">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/127d794f5e.mp4?token=cfEFSZqkFD-tpSe0yArs7edwi8rs30Vuor-FA9ObipI1_BUfei9lmZhW1BOrMihp_9gu1jQ_eDs0GtBwEuwAeTwP23yJOvf9v1aYzytGyNM_FCoGyAcLNprFjQL1mUg6Jghd9ihsrM-yzNhURQpVHxy6-fnmjj4-uTkoQbPE8r8ECFxuO8iJrwA2DKQ8WXxlVzzDghD3akgkk9_qtZvcUB27SJShSYhmNo8bLMrrb7teoX2CMcK87SHzywENDkjqgWy19qk9DInALTYRp5_Te4T4HVTAsk2rsKt9KgxH5YmdqrLGNMrKyOTqi4_Szke2z2gzwdHkZTKK_N7JBOPCnEmiwrkOCmmcckACx6StekFIyu0bfnbFPwNOgioUX3-q3BNqqUckxmcybSJQQhqOUZM1e_DbBmjhKNuJ_UpHT_pcRrR8TXUQkdSLjI2DOuIqKT5vRgxkGejm19VyTEZhCU8fk51X2V3hluTWXJEbUtDxAS2-MgJ_K0fFRa7yaXyznYuOhiTyZNV-iji1UmhCrg09UlMqsSN3K2iauKzOEzCuZSojYIDvAXpBEirNAJ8WLRS8Sa0mHYdXSlaO4osU3rFv9Se0r3_3fpoVWuHVI1bP2CrcoaidnMI-o4vEO7lR4x7iJtinSKLwPU6Ex7H_T9Ahv-LHS7t8hsUzZGF3_H0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/127d794f5e.mp4?token=cfEFSZqkFD-tpSe0yArs7edwi8rs30Vuor-FA9ObipI1_BUfei9lmZhW1BOrMihp_9gu1jQ_eDs0GtBwEuwAeTwP23yJOvf9v1aYzytGyNM_FCoGyAcLNprFjQL1mUg6Jghd9ihsrM-yzNhURQpVHxy6-fnmjj4-uTkoQbPE8r8ECFxuO8iJrwA2DKQ8WXxlVzzDghD3akgkk9_qtZvcUB27SJShSYhmNo8bLMrrb7teoX2CMcK87SHzywENDkjqgWy19qk9DInALTYRp5_Te4T4HVTAsk2rsKt9KgxH5YmdqrLGNMrKyOTqi4_Szke2z2gzwdHkZTKK_N7JBOPCnEmiwrkOCmmcckACx6StekFIyu0bfnbFPwNOgioUX3-q3BNqqUckxmcybSJQQhqOUZM1e_DbBmjhKNuJ_UpHT_pcRrR8TXUQkdSLjI2DOuIqKT5vRgxkGejm19VyTEZhCU8fk51X2V3hluTWXJEbUtDxAS2-MgJ_K0fFRa7yaXyznYuOhiTyZNV-iji1UmhCrg09UlMqsSN3K2iauKzOEzCuZSojYIDvAXpBEirNAJ8WLRS8Sa0mHYdXSlaO4osU3rFv9Se0r3_3fpoVWuHVI1bP2CrcoaidnMI-o4vEO7lR4x7iJtinSKLwPU6Ex7H_T9Ahv-LHS7t8hsUzZGF3_H0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت دیشب سئوتا
خامنه‌ای هم نیست که بیاد همدردی کنه با جوانان غیور و به پاخواسته مسلمان</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farahmand_alipour/6437" target="_blank">📅 10:12 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6436">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a175d481ad.mp4?token=rQ_CbPB74cL7H8L1N5Mq5EkNLG4qy9kZvscCqdY6NCOfmpLY-BGAjARXG21N_rvacjf4CMiRWf9S1KilDbnm51w6SY2ob9hP0HuG8uOe6r0b5fnNpeXZ-NazDKvq8JWhjK0GrWCICtcBO4gIPqI-pBFw_O2BiVjKn9fZIwL_nNKBRuiYbYRaCezvRWAMExD7OIKAqgVK0hO-7svOxyj6QJOKUndhTBsmmemGwNn8WPhbNULM6hdsgsqO48jUHMvf1GsWWFaipDjNeKzsG__IbC-HovC2hOPeG_WVw5v6I-IWrohuJcW7ArhjvloMIBTfKqaUkTZw2bwKtkDOTQ_eJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a175d481ad.mp4?token=rQ_CbPB74cL7H8L1N5Mq5EkNLG4qy9kZvscCqdY6NCOfmpLY-BGAjARXG21N_rvacjf4CMiRWf9S1KilDbnm51w6SY2ob9hP0HuG8uOe6r0b5fnNpeXZ-NazDKvq8JWhjK0GrWCICtcBO4gIPqI-pBFw_O2BiVjKn9fZIwL_nNKBRuiYbYRaCezvRWAMExD7OIKAqgVK0hO-7svOxyj6QJOKUndhTBsmmemGwNn8WPhbNULM6hdsgsqO48jUHMvf1GsWWFaipDjNeKzsG__IbC-HovC2hOPeG_WVw5v6I-IWrohuJcW7ArhjvloMIBTfKqaUkTZw2bwKtkDOTQ_eJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ساکنان سئوتا تجمع اعتراضی برگزار کرده‌اند و دولت چپگرای پدرو سانچز را «فاسد» و «خائن» توصیف کردند.  سانچز شخصا فردا به سئوتا می‌رود.</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/farahmand_alipour/6436" target="_blank">📅 09:01 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6435">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QHFF007gnUwyiBjcWtsCKXIJxyU5wSHzhBChEB8DiVjIMu6_rTPYXcNPgpr8gN2no7oqo_Xg8YX_1RWRcJCjCG3QE2xJ8tFu1IirUjK8rddXca6lI4S1U8bU7u5IUcMfkqad5lp9AS6D3aQICVR4bb8vtl3oOmwqPlBaOL_zo1DCyWKE05wBMpQY4og0yACEJD4PBuPPn-ge7KxCmIbJHZuTGwqF1gxcV4kdXbaBTwjLHgOTpuF4bVNrabA7xwDlY4Ji29k2lqw7YPQegBWmTtx56PcWKPtpCGwExyoLwHZ7wwjvlbjmwZRSF7ybBSmvd6HkdnTZCvZTbwrQyHMZ4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولی امضا کرد و خلع سلاح رو پذیرفت!
نتیجه عملیات ۷ اکتبر که خامنه‌ای میگفت :
« تاریخ ساز» و «ضربه فنی جبران ناپذیر» ، شد نابودی غزه و کشته شدن ده‌ها هزار نفر و از دست دادن ۷۰٪ خاک غزه و حالا هم امضا کردن خلع سلاح شدیم!
کی به این گروه تروریستی پول و سلاح میداد و برای این برنامه ها تشویقشون می‌کرد؟</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/farahmand_alipour/6435" target="_blank">📅 08:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6434">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fcDy5iNvQehdNbDoLsI0brLi0u-AtVLDyYypgGW52M2uEkVkoZi8otfB8qxEE9Tn13IOOCm1Y9_TZ8LV9qT_drizBVziD_21OkyVPGiLZg-4I0cQ4KVhUIJg39UzhIn3Mr0_n3n46De3GCGetSdFPqS1KyUDeo17sAIKsgP18CTVqzmA-eTyyxuaJO9YoZI--Q5JazAkwk76jlDQ-HAYLmMgG2zECYS_3Bw6QBV39rQa9O7LtEOqq6KsDtBaTyecuuf-GnWnYi3-QCfeajPlTjnYZect7epGZ78kKQQwphLTX1Y6g1J7xYobbcElHoXh7kGSHOdeIY7AM9trztwJiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جوون‌های مراکشی رو اینطوری میارن کنار  مرز اسپانیا
🔺
در یک موضع شدید انتقادی نسبت به رویکرد دولت چپگرای پدرو سانچز، دولت ایتالیا خواستار تعلیق امتیاز شینگن برای اسپانیا شد.</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farahmand_alipour/6434" target="_blank">📅 01:49 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6433">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cceceaa5a9.mp4?token=bRN2eQ8oBFqwzGNyUlGPXvV_hzRjjGTyn5nXE6hyatfRGCjgXR1ojvWC703sFvY3pO3_3ELakv_WxoWSeyDCWItHsc9D2BmlV193pGOfXUkkyvNKBZlqyZ4EPRmCFE02ZE-QBP0S7hnCQhp6VrqknRI6Zn1_BG0gnb8dPE7pemL27a8OiHMWjhvljd9vyI8v6MSo_oXRCpwcbFHwQKlr8ErvXY3hroqk9rEGzv7aiwk04ZukUq4Hf1sKmRTL_kj9EKk6rOfc-NMBbYv6l6n74ZcPmUQap-VKG6I9wJ7fKDzqzQLMsfroyauT3WdwDdcnEWKtbedSxDxdlQGZokkdp04fXbnZLH1QMIiSnYkWcgfXlac96jZbtReNaGi5_8nvm-SXoAfWxxFdZ96Y32xTfI8c2k_sjEAFRshefBHFLJCEq-CRWnZGXcNv93YFYyxHowkjk7p549aQdhge-mrmtmTzAOYopxglxlQDEuW5dV1eltvvTYv9woa-lAui-Z90w1F0o6Bd0v01t0QBKCazbdHiYn8a94yFHQ0HT-rVZ3T26ihm1A_Yc6cbN0kzcG5XSVaK03Ljc9phomdva2-Z_Pl-o6jjzGzSUUd-hdhZuQ20xnDnX_aflu3CSNIltGK8Yh_ew6MRqPThhvuwBKP_eV1z6vQT7d8dAAolX9_miAo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cceceaa5a9.mp4?token=bRN2eQ8oBFqwzGNyUlGPXvV_hzRjjGTyn5nXE6hyatfRGCjgXR1ojvWC703sFvY3pO3_3ELakv_WxoWSeyDCWItHsc9D2BmlV193pGOfXUkkyvNKBZlqyZ4EPRmCFE02ZE-QBP0S7hnCQhp6VrqknRI6Zn1_BG0gnb8dPE7pemL27a8OiHMWjhvljd9vyI8v6MSo_oXRCpwcbFHwQKlr8ErvXY3hroqk9rEGzv7aiwk04ZukUq4Hf1sKmRTL_kj9EKk6rOfc-NMBbYv6l6n74ZcPmUQap-VKG6I9wJ7fKDzqzQLMsfroyauT3WdwDdcnEWKtbedSxDxdlQGZokkdp04fXbnZLH1QMIiSnYkWcgfXlac96jZbtReNaGi5_8nvm-SXoAfWxxFdZ96Y32xTfI8c2k_sjEAFRshefBHFLJCEq-CRWnZGXcNv93YFYyxHowkjk7p549aQdhge-mrmtmTzAOYopxglxlQDEuW5dV1eltvvTYv9woa-lAui-Z90w1F0o6Bd0v01t0QBKCazbdHiYn8a94yFHQ0HT-rVZ3T26ihm1A_Yc6cbN0kzcG5XSVaK03Ljc9phomdva2-Z_Pl-o6jjzGzSUUd-hdhZuQ20xnDnX_aflu3CSNIltGK8Yh_ew6MRqPThhvuwBKP_eV1z6vQT7d8dAAolX9_miAo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تداوم ورود هزاران نفر به خاک اسپانیا  اغلب این افراد مردان جوان و نوجوان هستند.</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farahmand_alipour/6433" target="_blank">📅 01:37 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6432">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c72fd0437.mp4?token=snfmXWm8OXqwv1HEVlrDQWBcfJYMHarp4KqNY0DI3zdaNUF1dzmKWWFqrJ5KcY5RGLXm-U4ZT8U_CgOLMnsgV8RXKkiry2tOjyCgHmcHKi8jMw_0QMUEPmqI_2v7FGIKSR7AcnlOpEMjDMIFFZra-Bumm22eBUC-3ItW9bugwSLtWMHPkj3g66kZ4T0GGRwWoGzhAmwgsDYS6_vqnIjQ_n-ahEHJUnICDTSDo8OxOaShWYqEETPVdKg4ZnLVPMWHkQxtJgvBRDPoJb2W3Srydxi871RuJ9Z6myGkuN16cstm1Xszi39Y-hVgcfnLEVedtFzs8S5H1bjvsu4l7jUqHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c72fd0437.mp4?token=snfmXWm8OXqwv1HEVlrDQWBcfJYMHarp4KqNY0DI3zdaNUF1dzmKWWFqrJ5KcY5RGLXm-U4ZT8U_CgOLMnsgV8RXKkiry2tOjyCgHmcHKi8jMw_0QMUEPmqI_2v7FGIKSR7AcnlOpEMjDMIFFZra-Bumm22eBUC-3ItW9bugwSLtWMHPkj3g66kZ4T0GGRwWoGzhAmwgsDYS6_vqnIjQ_n-ahEHJUnICDTSDo8OxOaShWYqEETPVdKg4ZnLVPMWHkQxtJgvBRDPoJb2W3Srydxi871RuJ9Z6myGkuN16cstm1Xszi39Y-hVgcfnLEVedtFzs8S5H1bjvsu4l7jUqHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حدود دو هفته پیش دادگاه عالی اسپانیا حکمی داد که افرادی که از طریق دریا وارد خاک اسپانیا میشن، نباید فورا دستگیر بشن و عودت داده بشن. اما اگه از موانع مرزی عبور کنن، پلیس باید اونها رو دستگیر کنه. این چند روز عده‌‌‌ای جوان از مراکش و از طریق دریا وارد اسپانیا…</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farahmand_alipour/6432" target="_blank">📅 01:05 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6431">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">دو نقطه بسیار کوچک از خاک اسپانیا چسبیده به خاک مراکشه.  خیلی کوچیکه اندازه یک پنجم جزیره کیش ایران. اینها در واقع از خاک مراکش فرار کردن و وارد این نقطه کوچیک از خاک اسپانیا شدند در Ceuta</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/6431" target="_blank">📅 00:58 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6430">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AgyfBDuDCJAt0JNr3swz4HIiKL9HrZbuqCUgpWgoWH-EZ48shYa12Y9jdCvxYiiUNFYEdJyEo7wU00C_BFnb_CTyVpzrMF5rOaoq9kfY20upu4yrh3hB5FuUoO5req5uCes4pUb52gmb0Fy7wTOXqJ3zoNQli2K0qbjfW0UG-maUyxTkGqrZoG-0yyCxvc7BaTOLtGogCdjOavj9BXcFLXh7XHPNWWIadDPMDLkUiV1vEWOIIbA-gd7WI75ohIeh1Pk1T33bNTZMkSWE1h7eaOVXSgYf4bfPEE0IOn0k3beN_HQF1mbN29UXT4qshW1DSNBZOglA8ZOoGk8W2oZOog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تاکنون ۱۳ کشور اسلامی
به درخواست عربستان لبیک گفتن!
برای حمله به گروه تروریستی حوثی‌ها در یمن،
از جمله : پاکستان!!
مصر و ترکیه !</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/6430" target="_blank">📅 21:43 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6428">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kCJL3-8VxSn7fEsY3P6E7Yu35KygkPYAz9kSrPiP6mOf8U_s1hTygNHV29aoJtMFV3uDNu2SOmOr0pRE8Uvfb_4v3pd1wxSiC7wpZnrAVsKJuukgP-edn0XvKe6r92a-BQk70aHqprMQhb3F-ozQFNjyygGncCdKUSeTnA49lpLU-LKQovR3tXzfRYEQ13VxHLLbiH9ZOq8KL8MaWIGiCzWEk2jLqvCACusOmTarI5B3ycu06qcPPIP_Ppb52ylFXvsw2sTsuqNG8bwZzP13zYu87MoCAD9yHgVbxg1mP8ENRHtvk-EBW8FmpMPAivbYtiDzL3qDs_aptE84S3_x2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/W4kUTxRXfz-D5HD_bWoXgRgrYiak-pVLXVxgp4-BeojCHshuIc9HusfxGkpxvb3FpuKDTuEJRotNcjc1Q4l0UI7S8dvhFlWitvfNEqTMoz9DO13EehM3mEg1YTptXHXCp6iWN1PYngvlboCUMmcJgS_fU7dwZKWFh8-wNn5fgjmqOkPtTkiFIcziU_eUdyuIN3IbPFQ3Ybr9jGdcwqUI-UwnZ5Yq6tio2u7PqDKaggJpV-PxFW92N2bMtLam1MDfxNe3ATnZs0KToZJ0EYnesRz_GSkv1NFWkCFCB3bxRL6XJnxJzF9ATpwzI_MDdbaOGGrM8q9bDWB8BdYZxQ796g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دو نقطه بسیار کوچک از خاک اسپانیا
چسبیده به خاک مراکشه.
خیلی کوچیکه اندازه یک پنجم جزیره کیش ایران. اینها در واقع از خاک مراکش فرار کردن و وارد این نقطه کوچیک از خاک اسپانیا شدند
در Ceuta</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/6428" target="_blank">📅 18:06 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6427">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39130dc900.mp4?token=YEOHdLMVPtOYw3J_5YPdxn-Gv_SFUFocUTead4paxlJGZnTIUZV_hd1LI9wNVEaKNoN4gm3gWtJ4cppuv8BUVDoGelkv7IjFGqQiNpguBEnw4Ut7g-q7tQEfJkUKWQyTL5jZECN9R1DWNqf2W-m-lqWgu64xR_w2IeqNujmzqOg8E77WWbpuSUUQL9KLjZidEWAPqRsVL7aJ-P3hMr0sCeLuZKZvRsSfRe8zfqAyf76VHo7sUY_VzIZ5_aoAK7TvhZpTr0GrFHOLuSocKADvoQZSoI_--UyZ6W1jvoJ8UQ2O6lDo8F0zwst55t3ABxnCGemJSaEJ3wpxXwKYm1kVOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39130dc900.mp4?token=YEOHdLMVPtOYw3J_5YPdxn-Gv_SFUFocUTead4paxlJGZnTIUZV_hd1LI9wNVEaKNoN4gm3gWtJ4cppuv8BUVDoGelkv7IjFGqQiNpguBEnw4Ut7g-q7tQEfJkUKWQyTL5jZECN9R1DWNqf2W-m-lqWgu64xR_w2IeqNujmzqOg8E77WWbpuSUUQL9KLjZidEWAPqRsVL7aJ-P3hMr0sCeLuZKZvRsSfRe8zfqAyf76VHo7sUY_VzIZ5_aoAK7TvhZpTr0GrFHOLuSocKADvoQZSoI_--UyZ6W1jvoJ8UQ2O6lDo8F0zwst55t3ABxnCGemJSaEJ3wpxXwKYm1kVOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرار صدها نفر از مراکش و ورود به اسپانیا</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/6427" target="_blank">📅 18:02 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6426">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd3e7e1df2.mp4?token=q57YD4nwooRYNVQfjQxDucVMOS15EqC4OVGlpedKA2F2UxnYu0byFUA6qI6G9U9FEcDcmQl3xL6A_NHnu_D21GvuFr_GByZcLK_QMWfZ-mfpctpyaa-U9Gm8kVPKTpkiM2SSK_OP4wzReJrmIG_Msa2_v_05PWuCjZ6wGGcua0ztX-stI6Gbf-CkbH7jh-gwTC3o-bNmHNEh5SHmLsNCrJD8vRjZ90yBeVm3QU0e5dNTQhCl1fKyBKIa1-n0kQ-sVcmPu3E15OwAmVXzIaPoNLLYram4NmXHn5W7X-hVn978t3HoVm9rnzmdwKLdWGw9MGbX7sISckjXUFjAOKK7cQ3Y-Ua_tbMktpmTzpmxvQeAWFYV_9SooEGJt-Avpq1B3O1WESnDf9LiCUdyjLuk4aUjhnrJwIjw73L7gLg983uaPcdVNzBdTA79STwk_XPiFeyUmWnHzz4gSQIz19bkDCyqMNR9k_W0O-ELTJO7w3qIxe9eNwI2_47RKuoHmkpHexpxqDWdPkFVbBM2XK0qa0qu1caprqa7lDBoOPSamycymwPv4zLfzNbwecdyKawve2CIgVwtJo0ej3SRXyhTmEQLjn6bJMKflOQmM7juvcpyUQ7bZDBiUO9It7fqQxj4eI_N1Xe9t2zhsSvXSXX10WwKNsTxJ4fuA25kQsPIah0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd3e7e1df2.mp4?token=q57YD4nwooRYNVQfjQxDucVMOS15EqC4OVGlpedKA2F2UxnYu0byFUA6qI6G9U9FEcDcmQl3xL6A_NHnu_D21GvuFr_GByZcLK_QMWfZ-mfpctpyaa-U9Gm8kVPKTpkiM2SSK_OP4wzReJrmIG_Msa2_v_05PWuCjZ6wGGcua0ztX-stI6Gbf-CkbH7jh-gwTC3o-bNmHNEh5SHmLsNCrJD8vRjZ90yBeVm3QU0e5dNTQhCl1fKyBKIa1-n0kQ-sVcmPu3E15OwAmVXzIaPoNLLYram4NmXHn5W7X-hVn978t3HoVm9rnzmdwKLdWGw9MGbX7sISckjXUFjAOKK7cQ3Y-Ua_tbMktpmTzpmxvQeAWFYV_9SooEGJt-Avpq1B3O1WESnDf9LiCUdyjLuk4aUjhnrJwIjw73L7gLg983uaPcdVNzBdTA79STwk_XPiFeyUmWnHzz4gSQIz19bkDCyqMNR9k_W0O-ELTJO7w3qIxe9eNwI2_47RKuoHmkpHexpxqDWdPkFVbBM2XK0qa0qu1caprqa7lDBoOPSamycymwPv4zLfzNbwecdyKawve2CIgVwtJo0ej3SRXyhTmEQLjn6bJMKflOQmM7juvcpyUQ7bZDBiUO9It7fqQxj4eI_N1Xe9t2zhsSvXSXX10WwKNsTxJ4fuA25kQsPIah0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرار صدها نفر از مراکش و ورود به اسپانیا</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/6426" target="_blank">📅 17:50 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6425">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
سپاه از کشته شدن سه تن از اعضایش در جریان حمله شب گذشته آمریکا به زنجان خبر داد.</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/6425" target="_blank">📅 14:35 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6424">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MbmG6YDyR-fHed3nVu6aRQEZj3ulQAiriYoNFwy_h3FpjofGqYHrkU5e1a9xh4Fu_ZVJsVpWpNf0wC3WahE5AgogFtGQ08tBvArkVqfOAp3tlozqqJgIDG37XXeh_VFsM5_gF9Dlq-RuLj2bHBxkVXmovNxHWo2iy8Hnt2W8sdKLWK3FABHWdsaQmHsuQwEowtGDBpAfn5pxflbi2trMnIiDSmS3eyexLt5p57voueGDVeSXvu0Yx9vQ2ffqj3_-_axABarGcPNJpJ6rsdby4F4XAsHd5LUhj6kg9SwzTgw-6rrNI7TQe_GZ_Q2QaFkemI8Tms1PE0_Y6kenzeTDxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو رهبر شیعه، هر دو مبارز علیه آمریکا،
هر دو حامی سرسخت فلسطین
هر دو خود را پیرو مکتب حسین معرفی میکنن،
هر دو اتفاقا دشمن پهلوی،
هر دو هم در غیبت به سر می‌برن
و پیروانشون در انتظار ظهور!</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6424" target="_blank">📅 14:27 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6423">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
🚨
گروه تروریستی حزب‌الله لبنان با یک پهپاد به یک خودروی نظامی اسرائیلی حمله کرد،  ارتش اسرائیل : بزودی به نقض آتش‌بس حزب‌الله پاسخ می‌دهیم.</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/6423" target="_blank">📅 11:57 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6422">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fz6hapnwDn3etxJnwHFbq-7_aABsZ3Rzta_nWOAB4OqbdiTIHaTwWaJMdCz367dS5KGNtjHAvm765eu728xmofnXogdQqLXGMnt-6FuDvwcq-BLYSacV03nQj_HGzmiMleflYsmgOyp9XAH0zCZp4ziITONWHum2kSFcxTO-MGVYPhBsQAX6LLHIydgNyDoFoB7P5bcHb_KzckBiC6IieHwjRGNOc_eZpzhqxSw3ieqciGAqWIFoWThqUkVl4fkZY_iUOTl5xkORNFcxPaNdzAQXrpPmMGIl3rGnQ3Yn6XOKhWU--ac_WtMaHRY3IJzBGkR3d6ky7j69fOQP6vasmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جاوید نام «امیرحسین صفری»
که جمهوری اسلامی دیروز او را در
اصفهان اعدام کرد،
فرزند شهید بوده.</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/6422" target="_blank">📅 11:54 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6421">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3dca15fd7a.mp4?token=q4M2F8uyP9akTetXVooL3CzPMqLMt4YBdVXO4ihW45hY9UWObrY7Y2m79Ev9-pWozuB7zvMrlXv1EKe6QwU_L97Z-3TLzZmtXZCXNP8JJ2UF3L4XMGa4bmvBGalybZ1ZBEMF_8Ye8kIC-J1PKpzG4JRtduix4Men5AcL3RNWguiXOGynMtFIFTmGN5GDQHqulP6XzdwXRSoK3PBI_eb2BtdicvTWOmIXuAAaZXizDdCWxx-cYbRSOh15mSlbjwhBddQVA07bcVWshNTJ0tRR9Q95JZZFGYpq5bK8xUW9Wx7OythgNRclNlPRIGCVBIA5aHLYNigbwuZcwOKWFuvYGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3dca15fd7a.mp4?token=q4M2F8uyP9akTetXVooL3CzPMqLMt4YBdVXO4ihW45hY9UWObrY7Y2m79Ev9-pWozuB7zvMrlXv1EKe6QwU_L97Z-3TLzZmtXZCXNP8JJ2UF3L4XMGa4bmvBGalybZ1ZBEMF_8Ye8kIC-J1PKpzG4JRtduix4Men5AcL3RNWguiXOGynMtFIFTmGN5GDQHqulP6XzdwXRSoK3PBI_eb2BtdicvTWOmIXuAAaZXizDdCWxx-cYbRSOh15mSlbjwhBddQVA07bcVWshNTJ0tRR9Q95JZZFGYpq5bK8xUW9Wx7OythgNRclNlPRIGCVBIA5aHLYNigbwuZcwOKWFuvYGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گفته می‌شود که در جریان حملات شب گذشته آمریکا، ساختمان «اطلاعات ۳ پ»
اهواز مورد حمله قرار گرفت  و ویران شد.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6421" target="_blank">📅 11:51 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6420">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🚨
سپاه:
به حول و قوه الهی، امروز مجازات متجاوزین اعمال خواهد شد.</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/6420" target="_blank">📅 11:49 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6419">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R_NBo7PL3bty1ji-WcqqXIcv4gcxeNSHo4iWmPfrOezQdszVPWzfqDcS6117aSpilgCzaFLDGI7WLm2lhLDnhDsPNyfHRleQpa_4mqgPaws2gn8DFPewHCdNRzB6ZnBgkerKGQFZp_3ZxP7Oxv336ybSUjLkP9_KUQnqlxP-KPehnQcz-kUVh50HKdMY7eKshVfscQm9fOfl-Yewd1ODZtCICvKWPHUU6Qzt8TM2j5hyHfyjmB2lZNcuelOKXUEQ4QDHOgiP59hlWos3r0fR0DfK89SkqvHp7TyqX2UH7DoHPdFwzWlLIgAx8kXBpk5gVAZBUPF9FIAKkTs1Z00zeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔺
دیروز جمهوری اسلامی با پهپاد به دو کشتی حامل گاز مایع در مصر حمله کرد.
امروز دو تن از مقامات جمهوری اسلامی به روزنامه نیویورک تایمز گفتند که این فقط یک هشدار بود.
(که علاوه بر تنگه هرمز و باب‌المندب،
می‌تونیم در مصر و کانال سوئز هم تاثیرگذار باشیم)
🔺
صبح امروز هم سپاه بیانیه‌ای صادر کرد و از حمله به دو کشتی در تنگه هرمز خبر داد که قصد داشتند از طریق آب‌های ساحلی عمان از تنگه عبور کنند.
🔺
دیروز صبح هم به سه کشتی در تنگه هزمز حمله کردند.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6419" target="_blank">📅 10:29 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6418">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Givvgze5rC2LcRn7YJfEnWpjEjBvnGA-b42qAwQY8CLwNwN4ULUq46XjblZLyC9R_6oFOD4U5YFa67-IHtOBHwXz44xLnFwvSmRytbHkJT6fn5qacIqzxXOvshAZMRzO1_ynCs6nAsKtmj3HaLBfI0GQgn2-oZo6AL1XV4ZKh42GZ0iMuCiBwg3c8lGNYIBwLgSY6nfn0HulH8_1FLaLJlfk11otDnW3Jd2RDhbCCTOnnl3SyI5CQKsQYVChNhdL1uVD-9BGWgcO4wQi-I9DGAM0bUO3Z0TpTx91uohdHamtEne0i3VFf_O4jdyOpQ0_W8nXJJujokxuPT8xv-xJoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیروز صبح گفتن به سه کشتی حمله کردن
امروز صبح به دو کشتی</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6418" target="_blank">📅 09:18 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6417">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
🚨
🚨
حملات موشکی آمریکا
به چند نقطه در اطراف آبادان.
شنیده شدن صدای انفجارهایی
در قشم، بوشهر، کازرون.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6417" target="_blank">📅 04:39 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6416">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🚨
🚨
ترامپ : ایرانی‌ها می‌دونن که ما امروز شدیدا بهشون حمله میکنیم. اکنون نوبت ماست. ضربه سختی به آنها خواهیم زد.</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/6416" target="_blank">📅 23:00 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6415">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WQd0mi0sxNcgqCxW2E3qOKGBFpynmo96TarpXPKf_0ZxcOhhKuRFmG23aKR9xQsnpZ3_Jq0Merc2uS9s0q2LYfcp58Tw2cE-lbPhNPXedqJlGfjDbIJHF2_63CYx5DBjvTfRcS8UFW6S5joYyXlZK-vRrlV0Wpgye5p6H6h-wjvpdQpwO5r9KSZpJTChz4y9pxBxpkv5OjnDuzFy69VJtHPyGAswJyEqfl_NETnp1rtoTLadcns9DnJ5dZUf3RpByfhaNkOIyPDKrDQrH6MTXyup-54xWeN3KwDgLT-AM8l4KbXKz_Jb4ZkNt0XVvR9SEmg-jQwNMqB8DaRiyUu1Sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
تعداد تلفات گروه تروریستی حشدالشعبی به ۸۰ کشته و ۲۷۰ زخمی رسید!
ایالات متحده و عربستان شب گذشته در پاسخ به حملات پهپادی گروه‌های وابسته به جمهوری اسلامی به عربستان،
به مواضع حشدالشعبی در ۷ استان عراق حمله کردند.</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/farahmand_alipour/6415" target="_blank">📅 19:58 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6414">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b85006cf0.mp4?token=u7upMfX1E4hXA5sNZbH9MPZseef-5TqLgntayvo-2jj5y_Znolm_7Jedti2ttL5k4PtOvGwHkY3LFPTL7e9i0OqRnRQChlv4n2ufY21FC9UPcHjbpc_eSUmGmO9yiPpzgZRG0FKc1Zp3QMF6v7CGDcxK8yrH4HlTF1bf24QRYnCrhELnmG_fSuB0CXifs87Up4a5mIBktfZMg5CfgV0CxYCoo5ORfFHRhi6C0XNvD9GeNyYgKWvs-X3aUlDa9mMW4sbYg2lKfaEvMJp5Nria1mrFZP6ZJU4cmFkF41NSuj4w7wsv4JXQm2a0x1_lGLgGTVGEniF0vlO6aUPAA81hLS2yRwFZXBqKrmDzZl3eob3JrJ7gZYFAMd9J74oVCy7QSphrkbim-z8EaQKb0NIHJ-k3y0l7MhzVBuysUBCRORBlSpklulvhLDMguWDOrP8YldeHiLZi32o_194Ughy827iUICkySPzYQ9nRTV-JxKmPWmxQvIxhSELrzeoV63LW-RShfmhSSLMRLYIPjn4mhShu0-2JwacQzkQzXnHrhFaD1E2bn0yza4dyV4SRoD4gfEwUeuD7iEiWDTQj-mAo2PTCqc9JbyxBIyYwiwjAC11lITXFT_mG4hhpmiaYTQvtg5w04yjRZPrd7vHPJPmzeVB6BVipQXo8Kpq1lfIEO_s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b85006cf0.mp4?token=u7upMfX1E4hXA5sNZbH9MPZseef-5TqLgntayvo-2jj5y_Znolm_7Jedti2ttL5k4PtOvGwHkY3LFPTL7e9i0OqRnRQChlv4n2ufY21FC9UPcHjbpc_eSUmGmO9yiPpzgZRG0FKc1Zp3QMF6v7CGDcxK8yrH4HlTF1bf24QRYnCrhELnmG_fSuB0CXifs87Up4a5mIBktfZMg5CfgV0CxYCoo5ORfFHRhi6C0XNvD9GeNyYgKWvs-X3aUlDa9mMW4sbYg2lKfaEvMJp5Nria1mrFZP6ZJU4cmFkF41NSuj4w7wsv4JXQm2a0x1_lGLgGTVGEniF0vlO6aUPAA81hLS2yRwFZXBqKrmDzZl3eob3JrJ7gZYFAMd9J74oVCy7QSphrkbim-z8EaQKb0NIHJ-k3y0l7MhzVBuysUBCRORBlSpklulvhLDMguWDOrP8YldeHiLZi32o_194Ughy827iUICkySPzYQ9nRTV-JxKmPWmxQvIxhSELrzeoV63LW-RShfmhSSLMRLYIPjn4mhShu0-2JwacQzkQzXnHrhFaD1E2bn0yza4dyV4SRoD4gfEwUeuD7iEiWDTQj-mAo2PTCqc9JbyxBIyYwiwjAC11lITXFT_mG4hhpmiaYTQvtg5w04yjRZPrd7vHPJPmzeVB6BVipQXo8Kpq1lfIEO_s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عروسی، طایفه «آل العرعیر» -  غزه</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6414" target="_blank">📅 18:29 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6412">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qwR3nXbZqzUeASYflcuFLG_WWL8hoFu2hQEkVkqatXqPLmmFHl70EMNav1tbZJhf9BiTg_untZs-WJ0ED6nktVPX6Es5ecFIQNf66B7u6m5BVSs9ACFms73YsjZNNWyILu8BDzdXdbtdTUQGhdXgz_dzargbcOCu8Z4D_beW-_pBbq68-bCe_2fdmh3Zjz3ZR4zCjcTr-PitrybgqSSPk2aYD7fEtCDcQQrY88PGeskAeryfWSOINOA7BZkuFA185Dqff0vz-cxydwZY98mG6RInIAoBD7ad9xZQrQcmnjAipS7K04mhGRPDXP_XQpVLro1-NijU5nlYktqfM9p9RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VglRdVwge_Q-EfFViyiogpwAZhr3c5XgNVVEXIpay1fXfWcu0F-mHwX-45WSuEgoReq9coIjHK1oRsmLXtoCVQ8w6UI3dBEgRtyKNFohbeL-NNuKXCbhox7i_L89FaPa0fnTax1crJJK1Wov6HwNYcPqQGA0CVioKu2-I7FSH8DCpIUFfTxh7MzhyeDsWFVohw8me_V3OayZ8lMEK7_O0bDVqSy9ZXvQ_KeJQXAgLYmsOFIecrDjiA3BhEBo7EwfVHYwrVzqQq6LAW5NFmOBFznEa0so-lOYMpj71FgJIF-P9ftF4VMKYMuRVao1KMupFhTQuxi5LkK5efEOj_VCMA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
رسانه‌های حکومتی از کشته شدن ۴ پاسدار در جریان حملات شب گذشته آمریکا و عربستان به مواضع گروه تروریستی حشدالشعبی در عراق خبر می‌دهند، تصویری که جماران منتشر کرده اما ۵ تابوت را نشان می‌دهد.</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6412" target="_blank">📅 18:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6411">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚨
وزیر جنگ آمریکا امروز با نتانیاهو (در واشنگتن) دیدار می‌کند.
نزدیکان نتانیاهو دیدار دیروز او با ترامپ را «عالی» توصیف کردند.</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6411" target="_blank">📅 16:10 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6410">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🚨
🚨
ترامپ با اشاره به حمله موشکی شب گذشته ج‌ا به پایگاه آمریکایی در اردن :  ما ایران را به‌شدت هدف قرار خواهیم داد. به‌شدت به آن‌ها حمله می‌کنیم .</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6410" target="_blank">📅 16:08 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6409">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/436236e24c.mp4?token=IIbOB3kaFeP4WrGlAYXwxa094UNZOupO0KEXrA1id7Lu4Bk5s0blHpD_dHfADJKyUdKs3cnXlJDT_xClfxcGrJ3yxr046xGxi727CW0aqvCyuiphe2AwBecbqpu417BqeIytHUqTrdahgQv8l4uJxr1QSh9a_MRSJKvdeznNen8JjONRucnUA20CtI0lmODanVYmariy-TA7d3VTOuHcDN8JsUqt2Zgv2CGT0eZ5PRjDfwwZeEbjSHgNflBNiXBdX35CxoSnyzm5W4OafbZQnTv8nGAWxjcoplRTB9nzh4c6gki6NilVkfUjeMPdkT5Qsi8kYjo_cdQBlLMwtWq_lA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/436236e24c.mp4?token=IIbOB3kaFeP4WrGlAYXwxa094UNZOupO0KEXrA1id7Lu4Bk5s0blHpD_dHfADJKyUdKs3cnXlJDT_xClfxcGrJ3yxr046xGxi727CW0aqvCyuiphe2AwBecbqpu417BqeIytHUqTrdahgQv8l4uJxr1QSh9a_MRSJKvdeznNen8JjONRucnUA20CtI0lmODanVYmariy-TA7d3VTOuHcDN8JsUqt2Zgv2CGT0eZ5PRjDfwwZeEbjSHgNflBNiXBdX35CxoSnyzm5W4OafbZQnTv8nGAWxjcoplRTB9nzh4c6gki6NilVkfUjeMPdkT5Qsi8kYjo_cdQBlLMwtWq_lA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ترامپ با اشاره به حمله موشکی شب گذشته ج‌ا به پایگاه آمریکایی در اردن :
ما ایران را به‌شدت هدف قرار خواهیم داد. به‌شدت به آن‌ها حمله می‌کنیم .</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6409" target="_blank">📅 15:58 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6408">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
🚨
گروه تروریستی حزب‌الله لبنان با یک پهپاد به یک خودروی نظامی اسرائیلی حمله کرد،
ارتش اسرائیل : بزودی به نقض آتش‌بس حزب‌الله پاسخ می‌دهیم.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6408" target="_blank">📅 15:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6407">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eaa361a599.mp4?token=o1TIQxoEQ0caq8qos_IoOqW76hyzovxSaGDGP9fjGpuLzDsRU-udPQ0rFmQutofjHRxxSSgnsDjZw6H8x8mhhWHzRwV_-3ZmEOfMwBL-7E-F6jyML6OlfG2M1tUggSLSO8DMMMSVVEXUiqMLARPEvKn7rgmNJ4zCRUZ8UgPKqPQYMEvxZpP-k1oX3cnAvBGHhBe5qPdnV2nyMyJ92tiLqwRtDw4NWTs75l22bYP2gYjfMOqZ9tQ0AZRHALds6LPW8NRKYYMY1093lRSNpWZjR_087FbdvvWHCTLRguG0GnSL2EwilOnszI1kh-fXn9MFlsRmVe51iPz0LZDX5YKN1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eaa361a599.mp4?token=o1TIQxoEQ0caq8qos_IoOqW76hyzovxSaGDGP9fjGpuLzDsRU-udPQ0rFmQutofjHRxxSSgnsDjZw6H8x8mhhWHzRwV_-3ZmEOfMwBL-7E-F6jyML6OlfG2M1tUggSLSO8DMMMSVVEXUiqMLARPEvKn7rgmNJ4zCRUZ8UgPKqPQYMEvxZpP-k1oX3cnAvBGHhBe5qPdnV2nyMyJ92tiLqwRtDw4NWTs75l22bYP2gYjfMOqZ9tQ0AZRHALds6LPW8NRKYYMY1093lRSNpWZjR_087FbdvvWHCTLRguG0GnSL2EwilOnszI1kh-fXn9MFlsRmVe51iPz0LZDX5YKN1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خاکسپاری اعضای حشدالشعبی در استان دیالی عراق که دیشب توسط آمریکا و عربستان مورد حمله قرار گرفتن</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6407" target="_blank">📅 15:04 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6406">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B7zxojKz_ghSwC2P77eVpozsdS0rmxy5kqyXSR0WaUsAc_kp68-RVm2ECxgSyf61ChRw0GUqwLP67ZLXSwtZl6D6EZyCOBCa38H1nSnDk90TYhW_-VxM348NP1alJscLa9Wr94GpYKRhcYpkrc1Mx3w0P3s1aSeADZTsMcEYObhdezRXMOSU_01JmR7-cFwbAWgx5OKKnw8Iveq0gAt9BOK_DOXv07VwFzd5ZebGf-5CLYLVS-XOda9_zUOxayHcwYvR2zVqWbI4OmyYHe_kGZiZTUGbtzAoHwcDSsuVAB-cITK2VR88Tge_CPA-wrLVTvhd57trKlBRR6pQSpW4OQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیروز وزیر دفاع اسرائیل برای اینکه جمهوری اسلامی رو تحقیر کنه گفت که حملات این دو سه هفته اخیر، از خاک اسرائیل انجام شده و جمهوری اسلامی
به همه کشورهای عربی حمله کرد
اما به اسرائیل حمله نکرد!
(یعنی از اسرائیل ترسید و بهش حمله نکرد در عوض بقیه رو زد)</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/6406" target="_blank">📅 15:01 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6405">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/okHsi_VNOVCQYTocr5jbFq1Q0DjPoY_RREWhFCiSbcd71ElmQs8mXjvcVouGvkNon3tyW8m1ax5_Em7IK7D-gGVHLKGJ1mXC0HcDphKt4ASD17wOFKAAjA5v3nl0ki2NBQwf_qunAS0ruIjJKDx5sgwu2hoTwxvWzUa0uf4N6v1S-ILT18eETQNHPCIxYWzR5opt54g0TsOqE0GE0JVx4bKY-nWXF8H3HdO-_Jc__hzObr959RuiY3V13n3mKLHoBSHhXQgDYZNllyG9vXlIkR2zGhIpCY7gLyh_Pr6pnStIBdNrBcTvc9zrPHeo3x4_Tk7yTSDNu2drjsQpFFn80Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقتدی صدر با صدور بیانیه‌ای به شدت از «سپاه»  و «شبه نظامیان افسارگریخته» انتقاد کرد که از خاک عراق به همسایه‌ها [عربستان] حمله میکنن و موجب میشن بقیه کشورها
- عربستان و آمریکا - به خاک عراق حمله کنن!
این داستان دقیقا همون وضعیتی است که سر لبنان آوردن! از خاک لبنان حمله می‌کنن به اسرائیل، این بار هم برای خونخواهی خامنه‌ای از خاک لبنان به اسرائیل حمله کردن.
ولی اونجا مسئولیت دست آقای «املاکی»  - ترامپ - نبود، اونجا اسرائیل بود و چنان درسی بهشون داد
که خونخواهی و انتقام رو فراموش کردن و «آتش بس» در لبنان شد مهم‌ترین و اولین خواسته جمهوری اسلامی!
سفیرشون رو هم از لبنان اخراج کردن!
در هر جا و هر مدلی، تحقیر بشید
خوشحال میشیم
✌🏼</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6405" target="_blank">📅 14:25 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6404">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚨
صدا و سیما: دقایقی پیش نقطه ای در نوار مرزی پیرانشهر مورد حمله هوایی آمریکا قرار گرفت.</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/6404" target="_blank">📅 14:11 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6403">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9cd7033f96.mp4?token=iA_ZvR7S86tNNVnZ68EsRCLkCeogLpN74X_6VQMUZ6GouzN4kBS0vsY7N47C_bdS9JeOsCD42o1phbaswe2dX81rkncG0V-9_EepOgcvZ1YD7L7lYFDHBJO86d4f5Go5eNO6byXScn3Doun7WbYtcc4elTiCPV62jcGBt6waXliC9ki5kiCSU1IcwGV3x7y-1WKZrMqv8GTo5eGnRGCe--O3v4VcjsgMU4BbPAXrdzxCBjvcClG3aNijg_NuJUMLmR70C50HPWQ-QsFmxBYNBeWjqJgtFposI7fFxJM6yqmAWMSzcK8KycN6H6Su9P2Dr7UpbOOzpxNEXzTbFbuA6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9cd7033f96.mp4?token=iA_ZvR7S86tNNVnZ68EsRCLkCeogLpN74X_6VQMUZ6GouzN4kBS0vsY7N47C_bdS9JeOsCD42o1phbaswe2dX81rkncG0V-9_EepOgcvZ1YD7L7lYFDHBJO86d4f5Go5eNO6byXScn3Doun7WbYtcc4elTiCPV62jcGBt6waXliC9ki5kiCSU1IcwGV3x7y-1WKZrMqv8GTo5eGnRGCe--O3v4VcjsgMU4BbPAXrdzxCBjvcClG3aNijg_NuJUMLmR70C50HPWQ-QsFmxBYNBeWjqJgtFposI7fFxJM6yqmAWMSzcK8KycN6H6Su9P2Dr7UpbOOzpxNEXzTbFbuA6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش آمریکا و عربستان شب گذشته
به چندین مقر گروه تروریستی حشد الشعبی
در عراق حمله کردند و تاکنون اعلام شده که ۳۲ تن از این نیروهای وابسته به ج‌ا کشته شده‌اند!
حملات به مقرهای حشدالشعبی در ۷ استان عراق صورت گرفت بصره، کربلا، نینوا، کرکوک ،
دیالی و واسط.
در ۷۲ ساعت اخیر حشد الشعبی بیش از ۳۰ حمله پهپادی به عربستان انجام داده بود.</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/6403" target="_blank">📅 11:23 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6402">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83ac14cf04.mp4?token=ZIb7MLd3P83jjpL6ClGZtFEE4icYwoRdyXADlTx3h2WTjVbS4LGPdjiKCfKWGVNVnRQ1gggrd1ogCmyF3OT5L3mXqsSK32s9RPcGLTh0SMxagUYgfOqJDg9GFnxVt9Y2DZ9xUNbWgDJRv_6VWgmDaeQb8IAT3F90fiNenfGPdFCBjU20YF2hcJ_qEGJm7gMrm_rrmYDRwiachM7TYg2Mn35L7d4829ed13W361jAKLMyqhSWB1fIwfFHn5mMOQQfTN5leCCTM0r2-6o3gaS8bJjr6Jp4JlJqYFgwwa1szc3AviuSn8aKGBoQODIHiuSPI9sHHiWWPaEXEV-tDfZKrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83ac14cf04.mp4?token=ZIb7MLd3P83jjpL6ClGZtFEE4icYwoRdyXADlTx3h2WTjVbS4LGPdjiKCfKWGVNVnRQ1gggrd1ogCmyF3OT5L3mXqsSK32s9RPcGLTh0SMxagUYgfOqJDg9GFnxVt9Y2DZ9xUNbWgDJRv_6VWgmDaeQb8IAT3F90fiNenfGPdFCBjU20YF2hcJ_qEGJm7gMrm_rrmYDRwiachM7TYg2Mn35L7d4829ed13W361jAKLMyqhSWB1fIwfFHn5mMOQQfTN5leCCTM0r2-6o3gaS8bJjr6Jp4JlJqYFgwwa1szc3AviuSn8aKGBoQODIHiuSPI9sHHiWWPaEXEV-tDfZKrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خب چرا همون موقع نیومدید از تفاهم نامه دفاع کنید؟  این تجمعات شبانه دست کیه که هم دولت و وزیرخارجه ازش  ناراحته و گلایه داره و هم سپاه!!   کی بهشون یاد میداد که بگن «بزن» «بزن»؟  کی موشک میزد به ۳ تا کشتی در روز و توی خبرگزاری خودش (فارس و تسنیم)  می‌نوشت…</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/6402" target="_blank">📅 11:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6401">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eMYXod1lzsRf-ILIVjSBXEGvcuR-UcsllMWTQD4TmQtTDoig80xgmDEdF0N4T2tycKM9RcNwZcvagVnaUCG4vKkKNatx6o_PBxDrabj3cYAdZGP9lIb-Cy87CuE__s7EQLvi6Z7tJYmfc2hQi6WPR3p38I4OcD-kKP_DUSqAfjbyFm-IS1jAod57vT6KMsFmvOU3yZzD_fAqbAu7NRi03JGw3hOCH8zgxXIGjDLqETNbs2B3ulplNXt3nhiTcSjEvtOkBsWMSgfxE7L7GiFAwMfuwF2dQgkirR8-18NM0dUC3BD5c7sBczOCW2AlrsbQUJ8xui7vPUDxhqKj3MDYzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب چرا همون موقع نیومدید از تفاهم نامه دفاع کنید؟
این تجمعات شبانه دست کیه
که هم دولت و وزیرخارجه ازش
ناراحته و گلایه داره و هم سپاه!!
کی بهشون یاد میداد که بگن «بزن» «بزن»؟
کی موشک میزد به ۳ تا کشتی در روز
و توی خبرگزاری خودش (فارس و تسنیم)
می‌نوشت : «به تیر غیب» گرفتار شدن؟؟
مگه معاون سیاسی سپاه در یکی از همین تجمعات سخنرانی نکرد و نگفت
: حملات آمریکا به ما «واکنشی» است! یعنی ما اول میزنیم و آمریکا پاسخ میده.</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/6401" target="_blank">📅 11:11 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6400">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
سپاه ساعاتی پیش از هدف قرار دادن سه کشتی که قصد عبور از تنگه هرمز را داشتند خبر داد.
همزمان با سفر نتانیاهو به آمریکا
هر روز دارند به کشتی‌ها حمله می‌کنن ولی به اوکراین میگن حمله به کشتی‌ها خلاف موازین بین‌الملل و  حقوق دریاها و آزادی کشتیرانی و … است!</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/6400" target="_blank">📅 09:25 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6399">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sr1rGU9JC4ysDKfAEXapWPpUolJ2MO0tpHBTDEgbaqUfXDil5bd_8GDEOiElvS2OB-pgix8qbguNYkYQeZus6AJLNlq27LDae8N-bepyjzUEDDttEnmdOSNqXizLRGrbMkSZDykTIP41-R1y86GqRitPucQ_QXKuvNmOiO9_ebqJX8hx3uiYcNUYIiPTDydWW1IIjg_B6h1uAhUuMXHXwd4Tc3KIRiqTiYkvZWsCTVrEPW4W45PMu4nHQYVjOhCgDWoDOxUOeC8DvCu5Vwge9ef1KCxBRMHx7jm22TV5yYs6T8drhf2UcNUYh3sNEI_4eSl4CS0gRzgWZvvBAPndkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها دائم میگن اگه جنگ زمینی بشه دیگه قطعا ما پیروزیم!  این تصویری از عراقه و نیروی قدرتمند زمینی ارتش عراق!  نیروی زمینی که پشتیبانی هوایی نداشته باشه وضعش این میشه!  فکر میکنن سرباز آمریکایی قراره مستقیما  بیاد با سربازان ایرانی بجنگه. بالای سر اون سرباز…</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/6399" target="_blank">📅 08:31 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6398">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xfx9I4GsnhDajVywVh-rtlisOttlZVga-5yzRimLcJxxN40o3L_eQxvHhLkuCsFx4K4PntY5zsf6EMCCG7LPnGUZnUJNWP2BloktjBN5H32PHt7gu-m_WsIU5nyWLX5AR-0Wd2K-bw6G-EhfCngx3vj7yW2CRdmtvGJGBRb3aJwMA-8OhepDOppK49FRedBehSseVpB3pXzutCls8mBx7iTlO12Dvbm1hpmBMujtMtoW9rNHdh4YSrV5CslKgwL9iRNkMXMpokVseWfn9QR1CjeT2N4VGaSYe-Y1s4C-RgjAm9xHu1AVu8eTf2J6iMFi1Jnp_FfyFsqFJpcd1LYRtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۱- جنگ زمینی چیز بدی نیست! ۲- اینکه جزایر رو بگیرن،  اتفاقی نمی‌افته! جزایر خودمون  رو میزنیم و بعد پس میگیریم!   اینها قبلش میگفتن آمریکا جرات حمله به ج‌ا رو نداره! امروز میگن، حالا جزایر رو بگیره هم مهم نیست! قدم به قدم!</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6398" target="_blank">📅 08:24 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6397">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">۱- جنگ زمینی چیز بدی نیست!
۲- اینکه جزایر رو بگیرن،
اتفاقی نمی‌افته! جزایر خودمون
رو میزنیم و بعد پس میگیریم!
اینها قبلش میگفتن آمریکا جرات حمله به ج‌ا رو نداره! امروز میگن، حالا جزایر رو بگیره هم مهم نیست! قدم به قدم!</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6397" target="_blank">📅 08:19 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6396">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UUbYANbn3qDNyvEzlgFJMoBlKneUBoXUo0xkOrLEPpxIBrJrT8Krw1qi7W0MWXcH4qwHqUKBO9d2dO4v0LWQ7PHs0EZgTFnpeyQ0jcAkEzn_tm3HzLBiuRTCXk3TAs0NbEkbSHDA6Q3UWiNVFGFYItFedfR63KUFvNu_DxXS180etp_EpbDdo-96KTCCQ3M3NU3NiO12ykfGPuMSsi0k9lhdcxl7EGep2gkPBtvsfYTdttN4zapHSjNKqq8QsxGhS330Ky_FsBSI2qcMkCHZde7EtWODsQhL5pgIHalwT0vGFrU9SnVaDx8ib-yJSJ0FpRhl3aSW5AJiyZkaEkwFcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حدود ۱۵۰ میلیون دلار
هم براش هزینه کردن</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6396" target="_blank">📅 21:56 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6392">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VJo2F8fqJA3LVRR5V2rKM2cwRx5zX_diDOn7vOqgLTcPXyRbZfVNkzGW_fjc4P2k0F1P7MpGGZ325I9ROygNTO1EgfTQOgmJ6uN0gRli7PrqAhCMZlT7iVPbq8EjQppXpcejYs7IRlZgHlmwn84iD3ioxw2mNUW933q1yMChMCJWN3E4TziCzRwK-k0jUwfjhxja9vHAP4mtFtIuEosNc91Qd0DQpr_Q0wBl4FqSgNsf4_olhJR1sRBUGwjWqKBlqCPCSkTNNAZO5_UtvYTgxc7q7rAWzRf38trXFlNM3JdioUZr9Au2oSwxuen_71idgy-1tQr7mzdTOFUssMefXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k1S4HJWS382TqZTZZLzNgwDSCPJ5G7ui44HGRXV8Af-fZxdkRdqw6bVcVFLtc-JkAO8zBu7MuMv_WYeqxwllSOCbwMnALCiAy_UCU6j8xCC31mk_Ogx8VVpI5Eb5-lGUQRP0suTEix5PrDWixUZXOdA4Be-yOWXsOPDYYZ_5T-Mr3nCP2n6hW4xfbZawAJGHnkLCXY68mtxhRq4_peMpCGvEqVWZz5yRH372n02ZzHNUSnsl3s12s_m3B4XTMnngpLYDydOfAmEFNMYJC6q82c4qribgzmP0De9GKfPXxI4Ztas2QwKSHYfUORr1EwfQcqoFPDZABRxie4wt_rL0rQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YlOi6GS4wA_rqpf8gZRbbIFhbSWN_RIUopDt8JsQ7h99R9Qux1qAYkCSL3CT1n7k7mhNOxnqKOxeF_DeKTmJDu2DmJJCAApZhJ-PMyyWK7r8xc4cdb7VeuzLow289_ngfioINkI5OA653u04U073nR6hzRdTfoeQ4WgHLr7dTXnLSwhn5yJf8QGpo7nH57iNMG9LqQnyB0Wr6_kF2dsDOSF0HHFe15xXXRlULjVwVdSdGsOEmxDAPolTwlQ12hiEtXfd8_yBZAiJJOrkS9ldnibl_rQ3cn7_Rvlqo_xbqg7VpgvQlRtAE5yhB6T5Xa1jmf-OCwJzDhED8cc6odmOiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L1uCzZSX4I7zhSTQocIwhylEDOGdB_fDGL3q4mPZXoGaqmFeuMuCm0m9pIPm7HiDgfNpeEGDP-adw-DrdDG92jw7n0VZdmUHMID-k4ELRb_zVdubB4jAKdOKhNaB7xK7PXQegMRIG_4qUEM3Z6bhLF6PXIRjCwzDt3LW9hCytcvuiUw9BFkLgdYe1459QqwVYA8lYGHKqBBenrVA3oorJpelcgc3GzVigEsjKh0fPlOWUrrFfNPMSiI9bZhgLjp1CzhdZEx3XTnUrO3Y1cRBWTXCtltLhH_6aDNT2cKstVf3SEeSjRmCopGOJ7-4EKqklJIijjrv5EJ3ZS0WTHixAQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تصاویری از ویرانی فرودگاه بوشهر
از این هواپیمای مسافربری تنها دم آن باقی مانده.</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6392" target="_blank">📅 19:06 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6390">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">میگه ۷۰ سال پیش ما در خفت بودیم
که وقتی اسرائیل به مصر حمله کرد
حق دعا برای مصر هم نداشتم!
اما امروز باید خدا رو شکر کنیم
که از اون وضعیت به جایی رسیدیم
که آمریکا و اسرائیل مستقیم به ایران حمله کردن!
اینها از اینکه به مرکز فتنه و جنگ تبدیل شدن
احساس غرور و افتخار میکنن!
امروز با مصر قطع رابطه هستند
اسرائیل و مصر دوست هستند،
اسرائیل و آمریکا روی سر ایران بمب میریزن.
زمان شاه که در خفت بودیم هم مصر با ما دوست بود هم آمریکا، هم اسرائیل! معجزه آخوندها !</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6390" target="_blank">📅 15:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6389">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">مراسم خاکسپاری مهدی توکلی، مدیر خانه عکاسان کُردستان، خواهرش سمیه توکلی، روان‌شناس، و مادرشان مریم اصلانی برگزار شد. این سه نفر شامگاه چهارم مرداد در پی تیراندازی نیروهای سپاه پاسداران به خودروی حامل آن‌ها در جاده بانه–مریوان جان باختند. نیروهای سپاه پاسداران…</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6389" target="_blank">📅 14:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6388">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIranwire</strong></div>
<div class="tg-text">مراسم خاکسپاری مهدی توکلی، مدیر خانه عکاسان کُردستان، خواهرش سمیه توکلی، روان‌شناس، و مادرشان مریم اصلانی برگزار شد. این سه نفر شامگاه چهارم مرداد در پی تیراندازی نیروهای سپاه پاسداران به خودروی حامل آن‌ها در جاده بانه–مریوان جان باختند.
نیروهای سپاه پاسداران بدون اخطار یا دستور ایست به سوی خودروی این خانواده شلیک کردند.همچنین پس از این واقعه، از خانواده قربانیان خواسته شده علت جان‌باختن آن‌ها «تصادف» اعلام شود، اما خانواده تاکنون از پذیرش این درخواست خودداری کرده‌اند.
@Farsi_Iranwire</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6388" target="_blank">📅 14:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6387">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dDQs8_oFrZx4Agq3gz4SEq9YxXzO3fIVoCgiz_qnbh4uoyQNC36pPKtARVdZSyYmXiypAf326D8KMpKI-ETvvj72oworJEkCpe0fVyYdMxCPpTVAr8g9i4mzxgl-GcY6-3a0gMJnNvHpuY_DT61pnj1SqFYYeUZ0vkARlkNBrW5v5Dsp4VRhlCYcO9zffX19KRkDUCJavk1E47zTYzmDDnidqipYMjpwAGiIHKmBrL7HGaTZux9IR6XjpyQNI6bJks8GbMkQ-wO_i93kz5_crGYeQ4Iv8h0xDCgOidDCJtm6FqoqzQ6u8p-_bJCMu5rwjJNyUVngFImZM6ONDDI65w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باید آن قدر آن‌ها را زد تا پدرشان را درآورد.</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6387" target="_blank">📅 11:33 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6386">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">‏روایت اردشیر زاهدی از درگذشت محمدرضا شاه</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6386" target="_blank">📅 10:52 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6385">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H1pFF-FiM0Gy5q78Wqwwd1RuKVgKXrrDdgUgJS561xILQLD2zwCHaZiifK-zS2Qyw3CGT_gAEaIOu6Bnyudv9RS6DXK9fb9GsLacwED3PdRNY7EteV_8mL5KCkE-p76W-K2ETALL9Fr3Ylwh0_SF1r8KtT9_q7iIc1Kgb7Ghoe8vVrirOsbb8SZS0b-haxNHT46pTukHHSeHEetFIl_Nv_i7O4_1sT8wxYHIdA4bZT0sce0-0IjDS9T7K4bAwwvbqDdhFbsr6w9A8dJcOxhgzVmJg87S-XlXrsjW_xjtntWXdJCSlUcm7U1EV7HlgRRf1v1BAQ6WDzewcGnDFLUv6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لعنت به ترامپ که ۶ ماه بیشتر بهش فرصت داد! تا یکی از اقداماتش،
و حاصل دو روز بیشتر عمرش، قتل عام دیماه باشه.</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/6385" target="_blank">📅 10:19 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6383">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/139cdb38ba.mp4?token=vSqgPbxhCYgDydhuvj3zKkqh4xKkAz2_Tz3DGKOQLLvOn_134twz_h72H38NdIk17Hnex1DY0bWMIc6zktU94mcFpOpQdvvyIQ9oGPF3qOOycbuVlYDdCvAcPFXJuRB8I5F9k1So_gCWkON7dCzEMamgLEkzfHDRClWb_kZ9DcBSvv377afbhgKjSbVZsXrt0DpHJ3Wb2RvEGe3UkZkydalM198Yj0hUKJ-T7Rv-ni-u2b8eS8_M_1KCkToTkKxMStsXOg111MHvzkvsbGhfNPZO5W571ffLbRoV6WdW-tCb2TZCer11szQiHAnIqhb_Q-bFNEo2lujQXaJAkFK1mg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/139cdb38ba.mp4?token=vSqgPbxhCYgDydhuvj3zKkqh4xKkAz2_Tz3DGKOQLLvOn_134twz_h72H38NdIk17Hnex1DY0bWMIc6zktU94mcFpOpQdvvyIQ9oGPF3qOOycbuVlYDdCvAcPFXJuRB8I5F9k1So_gCWkON7dCzEMamgLEkzfHDRClWb_kZ9DcBSvv377afbhgKjSbVZsXrt0DpHJ3Wb2RvEGe3UkZkydalM198Yj0hUKJ-T7Rv-ni-u2b8eS8_M_1KCkToTkKxMStsXOg111MHvzkvsbGhfNPZO5W571ffLbRoV6WdW-tCb2TZCer11szQiHAnIqhb_Q-bFNEo2lujQXaJAkFK1mg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همزمان با اذان صبح،
دو جوان رو در اصفهان و در ملا عام
اعدام کردند!
ابوالفضل سپاهی و امیرحسین صفری.
مردمی که تجمع کرده بودند به
حکومت جنایتکار جمهوری اسلامی
اعتراض کردند و درگیری‌هایی میان مردم
و نیروهای سرکوبگر رخ داد.</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/6383" target="_blank">📅 08:31 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6382">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9dfafddcc2.mp4?token=oH8nTobTgT5hBXEY3yP79TZ0ikZes1hT1Vujs0f7uf9sCiZ5kx6aMWO1XdvAsXcEni-z5T9Zbnf_ajVOwVJ2zPkYbBZ7JzxOxeFOS5Nq1J5FwbfpVm5FEZs5beGkabrhy3nvcKMKqVTdTUP4DcjqdFuylhldxjeTrcklSJgDNvoN7-AFJ3nl-L8NY60ONtnlv2kdWumxruzrye9GdPqHAc4iFc8wB21kQA63cUNJlN4V3Bq4vKdE5zCalcKfQTkCCbczIlhLTKNtN3CFY66HepquxfaFj26WTUlTyL8Qp-bCETGhzHIdxUbWliGkug2yyHN86EVnZwXPii7eSjXWKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9dfafddcc2.mp4?token=oH8nTobTgT5hBXEY3yP79TZ0ikZes1hT1Vujs0f7uf9sCiZ5kx6aMWO1XdvAsXcEni-z5T9Zbnf_ajVOwVJ2zPkYbBZ7JzxOxeFOS5Nq1J5FwbfpVm5FEZs5beGkabrhy3nvcKMKqVTdTUP4DcjqdFuylhldxjeTrcklSJgDNvoN7-AFJ3nl-L8NY60ONtnlv2kdWumxruzrye9GdPqHAc4iFc8wB21kQA63cUNJlN4V3Bq4vKdE5zCalcKfQTkCCbczIlhLTKNtN3CFY66HepquxfaFj26WTUlTyL8Qp-bCETGhzHIdxUbWliGkug2yyHN86EVnZwXPii7eSjXWKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آرزوهای خامنه‌ای : جوان‌های ما تا ۲۰ سال دیگه همه باید عربی بدانند.
https://x.com/farahmandalipur/status/2081803094522757301?s=46</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6382" target="_blank">📅 21:35 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6381">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">جاویدنام مجید پوررستمی - قرچک
۱۸ دیماه ۱۴۰۴
قلب آدم هزار پاره میشه</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6381" target="_blank">📅 21:22 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6380">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">ترامپ به شبکه ۱۲ اسرائیل: «در حال انجام مذاکرات عمیق با ایران هستیم. اگر موفق نشوند، به اقدام نظامی قدرتمند بازخواهیم گشت.»</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6380" target="_blank">📅 18:39 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6379">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ed1a3118c.mp4?token=C_2M54irb07GsZRtYVhUV008F2OIt43s4JH1re3Ip2hfJQdPQQXLMyP_mXPVrsM0wAolJY4gxcfsuCQH-UsMXF9S8bJBEGfAjspelWRyhku69Uc0BD7szJF7oegj5JCYGuq2tw3M1qtq0WBJw1aYjI05P6-KAIscaIn5UVFg197qkVElcEhm6tvi44bLZs4dbFqn6ciLxJiUyoQtel1z1_RKji8joGEyQypXVnfJdIS4iWaav-MSYw3oZSHb9Spa1m0TtpFoSJh1AOFGg_WK5XcFth4_PBwPhYHw7MTfXvoVTQa9Zys7fKUpScRq59-RdkM5o8fnylriXb1Mdcfg0gxQ0Fv3c2DK_1XtyElY10BWIgy4pgjdUHM8Mtnhw5WE46C3GkFUTuKeQoUXm50_Z2rqHGqMIXrs-HslbITPyUz3d0cihjgeR8-D5nOV3TWO9tO5Uzy-keAKXgPFgrQeI5wD-zK3ctft5UFphrYLSWVSkGkT9RJTgqqQO0Id6ly48sNBnn9PbDfGJq4fJdUGCPIyA3tZ4S1iA4UqTNOpkhYvi85HQE0fntr8B-2BkLLoX8cXI2sTQHrrsSBPwwrmVV6Eft7bjHxPaRo37j8kfjSOY1zY6DbGYxkg-n9vwtsRUCpNAs-WcGB-NKcDKEuxoRJ803s0_BU4gmd9L3dqJfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ed1a3118c.mp4?token=C_2M54irb07GsZRtYVhUV008F2OIt43s4JH1re3Ip2hfJQdPQQXLMyP_mXPVrsM0wAolJY4gxcfsuCQH-UsMXF9S8bJBEGfAjspelWRyhku69Uc0BD7szJF7oegj5JCYGuq2tw3M1qtq0WBJw1aYjI05P6-KAIscaIn5UVFg197qkVElcEhm6tvi44bLZs4dbFqn6ciLxJiUyoQtel1z1_RKji8joGEyQypXVnfJdIS4iWaav-MSYw3oZSHb9Spa1m0TtpFoSJh1AOFGg_WK5XcFth4_PBwPhYHw7MTfXvoVTQa9Zys7fKUpScRq59-RdkM5o8fnylriXb1Mdcfg0gxQ0Fv3c2DK_1XtyElY10BWIgy4pgjdUHM8Mtnhw5WE46C3GkFUTuKeQoUXm50_Z2rqHGqMIXrs-HslbITPyUz3d0cihjgeR8-D5nOV3TWO9tO5Uzy-keAKXgPFgrQeI5wD-zK3ctft5UFphrYLSWVSkGkT9RJTgqqQO0Id6ly48sNBnn9PbDfGJq4fJdUGCPIyA3tZ4S1iA4UqTNOpkhYvi85HQE0fntr8B-2BkLLoX8cXI2sTQHrrsSBPwwrmVV6Eft7bjHxPaRo37j8kfjSOY1zY6DbGYxkg-n9vwtsRUCpNAs-WcGB-NKcDKEuxoRJ803s0_BU4gmd9L3dqJfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به این سخنان «موسی خیابانی»
فرد شماره ۲ سازمان مجاهدین خلق
و جملات و کلماتش دقت کنید،
اول دیماه ۱۳۵۸ دانشگاه تهران.
انگار همین امروزه
و جملات یکی از سران جمهوری اسلامی!
که داره میگه
«اگر ما اهل چانه زدن و گذشت از اصول بودیم، امروز خیلی عزیزتر و گرامی‌تر بودیم.
اکنون هم که وارد این میدان شده‌ایم
باز حاضر به عدول از اصول خود نخواهیم بود.»
یکی هم اون وسط فریاد میزنه : یا حسین!</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6379" target="_blank">📅 11:22 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6378">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BRngN71Xg0wj8K90LDXpYvOuBdfaa85Yhuvhj93ffyR7iy9KTfEdswIUckYPdPG4KRay9-IsndDag4UgxrP4K4YpFTj54Kg0CQysLAes4wdHStXRsH05l_by5r53pk-GqRyVcpjl0dk8tjFOEgVxudW2Qe4nyKyF__2fxNeqLKryB2vekHFWeKzexR2hfh5zyP4v791XZGlZiw6nYoeVjVaFW8aam1c64V4v2TkT3CQJB7595EoKHsYYKbAqY4c3A7teVz6fT1RxL4APHxPBUEO5wYNDPycCut53CZK9sC_goGKIbmW04-d_hG43YyUTkd3MuGF1PAUpSgqqXz2TpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نتانیاهو راهی آمریکا شد</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6378" target="_blank">📅 10:02 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6377">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af3c95e2d9.mp4?token=ua71LHa2p6pbazvEEbxU8DTKyrVulb5oQhpeRrLmMslwLDOINH8fe4jdWjWnFY1nGzfDM-cEnzE3YP5gIUw5WLikPp-zTM_ebKvl-jkfY3yOwL_yFT9LRe-WHxWySnlRs4fWGeQ4Qhgzj8tvDwYDJVnrU-1J8E8l8x1FI_tPsRmNZdwYd2is3PdSEaaMoH0dxExSVS_IwIYbUr8xv2HLq5riM1BLO7uPD5Dtu4tOBsLeAT8M3spLUEbr_6um864r_gKnPUfSBiVg670u7eN22vzXHMDlqF4KcXa2LEwGu4LDvrdPYfvCai2q9b4ozipSvjowgomDyRCygxhrJH6Mow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af3c95e2d9.mp4?token=ua71LHa2p6pbazvEEbxU8DTKyrVulb5oQhpeRrLmMslwLDOINH8fe4jdWjWnFY1nGzfDM-cEnzE3YP5gIUw5WLikPp-zTM_ebKvl-jkfY3yOwL_yFT9LRe-WHxWySnlRs4fWGeQ4Qhgzj8tvDwYDJVnrU-1J8E8l8x1FI_tPsRmNZdwYd2is3PdSEaaMoH0dxExSVS_IwIYbUr8xv2HLq5riM1BLO7uPD5Dtu4tOBsLeAT8M3spLUEbr_6um864r_gKnPUfSBiVg670u7eN22vzXHMDlqF4KcXa2LEwGu4LDvrdPYfvCai2q9b4ozipSvjowgomDyRCygxhrJH6Mow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله یک پهپاد سپاه به یک کشتی در تنگه هرمز</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6377" target="_blank">📅 09:59 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6376">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lVo86hxdWDfPj6qLmMJ8ahfvWCRXwAu3cxwx5JeZ1d_siMKK165ydQXa0b4nWXu4sWKj5_cRLJ4uxVQqlwQK8GGeNIc7iNyk6_rHm6V6cyV6XV_D4YjrEe2--rHwR0DTNwPzDTovDFXfdaj5TRdXhFUwwM_oVYMgwyv6YgRdDPGR9Ymq1Ih6jeooEG5Dil_srUDX3fQ_idKxyxEKGuAzg4SGPN9IUIvuIQ8pL3xj9VdN3Ba1elL6FkqOwRz5vbeNLQkFGtypx8F6X_pA43AXGhPN27hHLzqnvtK8WMRgXSPkdj52twOa_wrTmutyeIRExsKjnwgKDHQ8vhC9MUmSpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«مسیر ناامن»
منظورشون آب‌های ساحلی عمانه
چون از مسیر ناامن میرن، با موشک بهشون میزنن :)</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6376" target="_blank">📅 08:45 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6375">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">۷۰ سال داستان دلار و تومان</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6375" target="_blank">📅 08:42 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6374">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PNmbV3Vuc15mEhLD4muQZ5auZkXL0b8ysE_xunl5CRCVKGji81hCm35-cZN0jrXsCaoZTZuX4ZfaZB2aASxN38QKr619S6BGEOKYH56c1VZMcj7rwfAl1BTpng1h7xPh2F1niL6mPFdcaSrO-hvgo3OU9vChkoNzuPV8RV0vptGqlNiN8QOZI3xzd8d7upwYOOxYCXJHjvAyl-Rh7K2r7sc9IqN69EoXxSlAXgJclBVbwk78UubgCeXRK_MVp04uFipk8GWmw66ZU64rB8WptjtNIr4KuTc22_r4P3UgOZrCUe0xbM3hFqSUeZYcQSVu_b7KnlV3TU6NptJW_Wat5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نشسته هی طرح میزنه و منتشر میکنه :)</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6374" target="_blank">📅 00:29 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6371">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qf0XcUYTxVKOLZMCOb3n_OeSefoJu1TDQnA2lbBeGFGx8TQqsvLsSh9-HaOD_2Y_jE812VmccNpkPQ3Dsmq2Lnu9O0WKC_r02xQhhYtFdDA4_UKhVGu9nPpdULEBOyf8Mwag9mGlunsevmllfS28AEnFxMKn0zsYKSztc3F_Jf_xVghUMZ-tTwgugz77QQmDCcQ6zFrfI-lPbWbjyLaXem1gfU8tuPP4dGXJLEDtxCaaiOlVw_5hh25_V1KahybfWrzlyaKCvCco-SzEw5bfWsbA5AoFo9iiiEi5-7Rd7a7vHRzC43fnvHWl6RRfppufrpgXBp8j5uAFwS_omEkR5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qYhzMJzvcO91VCLVqmhFSlWJdQ92vCRezqRVZhRJXj547sPRYy6Aa1WEwA_-JsF46cff6pul6cFs5_joseEarENZI-C6T1nGMALFLTbkNIwfBtPNJ6ApVdTk0puMA9LJU9Kp0BYv47pg3kulwumyq2NlHaCrskMmtDOezMt6xaSqQYro45a8r86qIVZa2wHlnJ7rlx7NXEHNjmgrsVnzAhS7YJoZ2aNtBR7fMbJAqO8ByCgGad_wBMIB5QGjZpAVaWdblRa2dmgrSlbQB8Y_nvqPmMvDIMnCp1akXI7c-8ouy85PZO7onYVcjd9gKQLv0n0CA0wZS8eHMIYAyaIQrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VrGkTlHYwXeySADUWx8fE0w05p_xdzBTe6ZVFZfxGVuVOCIvaY0SeuOBpuEMmDSCJfaCgj27bXnDaW8_v48Vri33yJsqfIQfdAWcZGDKxLAxhKhzAqa1_YsX8LqVpJqqSKVqfNzxSe_WIllklIuIwWxXCTe-IJeZCH1_0nFsddswVVqbi8r12vICz5Xuj0Zakgk8TcM4pFlcPRWiS6BDp8NdjD8NqzFPCZRJ6vSnRw3jGFIwV47H0wkp4VP6qNEq4VOdOwez43YJoCz5dnz8Z40TTkm8FHyPRo-FSczwqzuIYi_CrCflmOejsyzYNijonDZj1Vq5n9rlwrYm_g3-AA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">طرح‌هایی که ترامپ با هوش مصنوعی درست کرده :)
حمله به خارک و تصرف نفتکش و… رو :)</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6371" target="_blank">📅 23:46 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6370">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HB5BrXsOHGbSHMJjXhu00l319PhByXj2cXkpNPmCsyQBP84YgnVkFDJviXqy3cR1TX96HuW8zWET56DXG0nsUD1okeiULHQYEz0JuY1bzERG_IEnLsvkR8Ez4FVSMt3hztS5iYO1QtikELQryMuc0GBhJL2-f2u7W1HbRah7xdHhNvi4O64GUJCLbR_hX3bHxQJD7Gipw5tydAngtILWHLnMs9KqJPhBotS2Wfat2EXJru7wgMy3tW9glDYyGkqdOd04XgW8WVSqkVDbnLu-Pswk8tKzTBcgYSyKBG0qMspImuIrY7GMu0qpm78fm2lCyTzuhoLyEuFuE_Yb1xZL9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نامه منتسب به مجتبی خامنه‌ای :
در برابر آمریکا و اسرائیل راهی
جز مقاومت نمانده.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6370" target="_blank">📅 21:20 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6366">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U_HWPmbHPkSaBkCf2WCLsdEyMry2XV80CE-6oLFGH5IEhe_u_uaXrbPhL8h3b0tJwzR4oYZDhX2_rQ_CnrtjYZ2Oc8qnPl1f-kwNf23ZsvF0JJuWQ3cmPpcWIA_yckRduYUCnyEfWiftJjNqePXPN4d5z7YYU9zn93cqLBeO2TiiD3fyzcfZq457Wf_MyWX1zjb2FJZYvG-E9z7x1x_6A93YX3jiJPHOzRaL8RDUeImA-Gq-BVnIhlspwFhs3AZb118VdIJEAps8odV9NtlxJKQwziRYARTZGkwXMV16IMj7qn5I1-IqILNjusFBRlonl0km3LakG8EpSjfOZd-4VA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d2wbXGs-V5ypXxYa1vUFyqcwHYRgcCjrOhTaU4yrJBD-J2Pc-p76rEO62o2HaPvkETcdufXYG4fFbH1WFM5qsGBgskz9sPQaUa45j2me-f6ZCd9NHPi-sZMye1XbrT3dC9Q00exRMlcQbg8EMYvgODC1qg_ZQKjHMFa6xjR4Qs4ckXD5m4PbW6wlYY5DR_qcl4JIAX2T0kGHJWna80vYttHlrmDlAIENe_DQ6bz-61FLJ2vtAqPCSOeQZH2tdaO9zPOINbIAGf4P6BqyKc2bi-FjdhbXDvYsP_dVPRjY4dxpGmeO9zw8-GA_Iur6Mi7KN629jx2PEK6HrIDyH17Jvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dG_W2oNfT4ftFvTmDdO77h5WDBmR3Inj6lzAqcsMmcJaT7S2g5ntCgFT9vwi99Lbr0vvM2bkyMQQE5RXL_3QPJeHyVe4nNqo29IYKO8df-EPelGF7dH3gATbScGLTGK-5rpGvpFvwI4BIeB5yhbsDlpluWmNU_9wzevavDyslcF7E2ddDL7fhE9GjCLaP3vO32R2jxqvrEyJKUzx39U9BcjCy1KdJHflHAMQ3PSMChV4Epl8RAk7d-sZ2Vc-S--e_gn3hj7hRiP75csum1bkHTV6IFKjM5cE4kgKFzWbA_gg3eJSSnTPmF4nK8vxNNYwBHWt5vu7UPkA02QiJ1TgbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oitJ1vQZRFiydk6Jj99H74yKZ_fggF2hc3yo_j0vDx7_5nR-Zo5JLT1awpeGwF2mHOF0zmbROhz2I6K_ngsxfbRNeeU3UYhIqqW9e0FwNOH_qrfEFakITHTxZDwqowgbHONjfaLg9ZuBRuI7QufX8NQjcZb95dqpr1jxXj-CXxdKUjwew0jx1_kxV1tvwwWuJ_2ZYfA3G4Chb3X3rfQNTqWDx3b-Ad4fzUviA_gSoh8guoS51_CdCn4zgdn4iAdehh70BR7gwBTv27KNsvOA9qksMCvc_-TvusLh7yyA1LMHMnMC_rQBAJbewrpm459mYsQe6Ij1nR3sNPvliCIVvA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">جنگ اوکراین
تا دیروز افتخار میکردن
امروز نوبت انکاره</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6366" target="_blank">📅 20:37 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6365">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">۱۱ سال پیش
خامنه‌ای با غرور و تکبر از مسلح کردن غزه میگه و اینکه باید کرانه باختری رو هم مسلح کرد.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6365" target="_blank">📅 20:04 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6364">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k4aBUZtTHSCFpNRE6Z1kQ9cKQWLaOWiazrBS9hTe7N1-_wJKCdlhPVgNyhtf_uqA5rICDDNBac1AT9oLkAQ5ytrPy7JqafXB75NUFxy2Ec5qU-TUD0k7UigZcDwPDv0RpVZtV7fg52c_6OZoR6Iv-RwwP0LLBCf_c7_7EqpwoqZRNe1u-Pg1wWNQl7BODE1NKooReKNbu94WlkUuFfmckAtaQfvYFLsFm7qiqUwd2_kyFlrsmEeGGsa-QkmPQ8xXfkda6HbnbKu5vLJjMqrGHC7I8p6e6VdggDdujHB_fJ0OHCzqGK3FZz67bdDg_0XJs62vF-sd3I3Yjl8VaTRXUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6364" target="_blank">📅 17:37 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6363">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oiUxRJG13G7I8z4SVndYHKaMdgy7xUOJq0z1D80TTRWEJCWaCsKscfDUSrKM-AvpmghhI4x9NSFxzzAHxYqmOnqxENO8B5UHHHUYvGOqZQVIAIeK0KyKq9a8Nihs7TuSA42eYP0_xsZQUJHF47P6sjjPG9Of30OBPs8gAsiCXn2wqYaA_XAiSXnDAG31qJtHZUKz0pWR2fgmkc4Jl_TtYydGglE_HMx1eE7NJKU2H27uK7n8NffmY4N98AU-gwh82gNJXc6kYdReM-KrhB6H_TlmbNZfzuV5vg9i79V9uvbg7iBHTYZhcCtccZNDQ1svrVRcnbFH0Uc4t1z3iDevxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه‌های حکومتی از برخورد یک کشتی با مین در تنگه هرمز و وقوع انفجار خبر دادند.
مین گذاری توسط ج‌ا انجام شده بود.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6363" target="_blank">📅 16:19 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6361">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Tpv8A1LsDYFvqEoByVoGzH9_spKvAtmWy70rr9505vVbB0iqv7-cbDLKMT2kaMvo-zvB-8QnILxuF7oTqBqOFewO9paY_PbcnnbKIWtoxpsZsZ9HMdwDSa9Thfc6Hlw0kP9NXh6PvxdsrQVvupHUyA6uQMmFJZE7qqxHHpiV9CeTVh1ZkFOPvSgjBg-VZKAmg376y1cftrVJyPX9n_u5jQGuA3ry3tX0CcQDvol8DkVBFIi2x_W1FPg9XGhIyGRkQrpYZJRUY0unQ4aMBASSLRXWPoXnAtYp7-rgteicBQit0fJ1BhQEv5fCIwql4paS7JJ7vmkd6eE86H4VCoW3-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BrIY2OheqfY6RcelAbigp30Bxww58zGz3xI-iIvxWesUoI710RBoNEtP9CZnbfJXfLMAfHZEfVQdzzEVAWQ1QE7fz1_VDhRhITS73Smh-12tt_gAXdTrS0UToLqdmLAXSUY-ySys_jXXUKW0hRsMHHpsX-wOYJmVCnUirWH5IXqanyrzJ3pmi832SIcTuEAvw0xX1SDsQkPAbWaDIoaHGYhVEqgh-H73VGf5MHFOxJS40EAjCofUXO631T2uEKLxkSmy7glJkFx-cUDwxqqbsaWe8jRpCdDzgPDMiI5kqy8AvxTN7ol0gQmkmVpan3Q59zqo1YkTuSXreEFXjB39gw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اینکه بارها نوشتم، چپ‌ها، با اینکه گروه گروه توسط ج‌ا «اعدام» شدند، آواره شدند،  نابود شدند و ماهیت سرکوبگر جمهوری اسلامی را به خوبی می‌شناسن،
اما نوبت به تقابل جمهوری اسلامی
و آمریکا که میرسه، یهو مصمم و قاطع
میرن کنار جمهوری اسلامی می‌ایستن
و ازش دفاع میکنن،
این یک نمونه‌اش!
به خاطر اینکه برای اینها مبارزه با آمریکا
مهمتر است! اولویت اصلی است و اینگونه است که جمهوری اسلامی تبدیل به یک متحد میشه براشون که باید ازش حمایت کرد!
و این روزها خشمگین هستن
از مردم ایران،  که چرا کنار آخوندها و سپاه علیه آمریکا نمی‌ایستید؟
تصویری از پست ایشون و یکی
از هایلایت‌های ایشون.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6361" target="_blank">📅 11:49 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6360">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">عراقچی در این بخش مصاحبه‌اش درست در خصوص آخرین روزهای منتهی به جنگ ۴۰ روزه صحبت میکنه. جنگ ۹ اسفند شروع شد و عراقچی از مذاکرات ۷ اسفند می‌گوید.
اینکه جمهوری اسلامی در مذاکرات به هیچ وجه کوتاه نیامد و آمریکا را به این یقین رساند که مذاکره نمی‌تواند گره منازعه هسته‌ای با جمهوری اسلامی را باز کند.
عراقچی به صراحت می‌گوید که چگونه جمهوری اسلامی تحت رهبری و افکار خامنه‌ای، جنگ را انتخاب کرد.
(با بی‌حاصل کردن گفتگوها و عدم انعطاف)
وقتی مجری به این نقطه می‌رسد که جمهوری اسلامی می‌توانست در مذاکرات، مانع جنگ شود (که می‌گوید باز ادامه میدادیم چند سال دیگر…) عراقچی می‌گوید : تصمیم گیری دست من و شما نیست.
این برنامه فتنه‌انگیز ۲۰ ساله هسته‌ای که هزینه ۲ هزار میلیارد دلاری بر ایران وارد کرد و حاصلش فقیرتر شدن مردم ایران بود، این سیاست ۴۷ ساله دشمنی با دنیا، این دشمنی کینه‌توزانه‌شان با مردم ایران، این جنگ‌ها را هم به ایران تحمیل  کرد، که عراقچی همین جا هم می‌گوید: مسئله ما زیرساخت و تاسیسات نیست!
«شکست در نابودی تاسیسات نیست!)</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6360" target="_blank">📅 10:58 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6359">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">پیام فرستاده برای «شیعیان» ایران
میگه اون روستای شیعی لبنانه که کاملا نابود شده،
اون یکی روستای مسیحی لبنانه،
که دست بهش نخورده! چون رفته متمدنانه داشتن.
این هم روستای اسرائیلی (یهودی) است
که با اینکه تحت حملات راکتی حزبالله بوده،
ولی داره زندگی‌اش رو‌ میکنه!
و میگه دست به اقدامات شامپانزه‌ گونه نزنید!
چون - مثل روستای شیعه لبنان - نابود میشید.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6359" target="_blank">📅 10:46 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6357">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VIERl5RmE9_lIO1gTrWVgTaYMopFx5gxhSJrB7TRLhSpLqTtFBODsGRzrJAY-j-WTBepUXM7gMAk5iUTe7JHKVaYGVrf_UKYQjZETLHoofN8T_qlrbt5_AUsKpAZF3jZul2KbTipI8JYFmdxly3KKptaHdRT23kGJtHLxS4T3mZjKhdnO3PmBQ7xrL8NEaUKhLFJPRDY4TXG86KCbgjf7yVW_YmVbIxtGlApz8F2uyIuuw0r6CHqkdCRVuy93WEo-gL2Ss43GUZ63CrUXi7w_QZpAUT4t2l2V0X0TICyoZBwRU921LYZ4_fmklUYij3Gim5hR9rX_WWBPhdtYBQcfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z2Lbp98fedEidt0Ezz4LV6MwHR2zhztvu1CAHXy2vYkKQBY87u1h-0S0RB28RkhR4EJoUFAWuBiT77CnW5YwzIAfLsmEi5xvLfwyEfv5eCUrsLHdVR-najkUmLKaflt0D-69xgz1TCRaNCJ1KNg3ll0Ktdad9-9laJ0o_blFLU1uGKAHwujKLKin0GCBFS84EBZIvSHhzGt-kKMszLI29aIrBHzW6ERU1hHnQH8mRNYImQcxgcoAf3nb5LLbo_aO0RiZdAhJO1epzhAIJ4n1H3A9KsbK0A4W5zjRnPglTuw20iM5YNfktzKBPGcN8lJ4LFL86T7c0Jatg5AKi_INrg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">این متن رو کامل بخونید.
در  بخش سوم می‌نویسه اصل این
بحران ۱۵ روز اخیر از اونجایی
بود که کشتی‌ها از سمت عمان عبور کردن و جمهوری اسلامی حمله کرد به کشتی‌ها
موردی که ۲-۳ روز پیش کامل توضیح دادم.
جنگ رو ج‌ا شروع کرده و دارند زور میگن به عمان
بخش ۵ هم بسیار مهمه، در خصوص کوه کلنگ، ج‌ا در عمق این کوهِ سنگ، غنی سازی میکنه که حتی با یک بمب اتم تاکتیکی هم نمیشه نابودش کرد! و چون خیالش راحت شده از اینکه غنی سازی‌اش متوقف نخواهد شد داره رو تنگه هرمز هم فشار میاره. اگه امریکا بخواد برنامه هسته‌ای ج‌ا رو جمع کنند، باید هزینه زیادی بده (جنگی بسیار بزرگ)</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6357" target="_blank">📅 10:06 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6356">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">ثابتی میگه تنگه هرمز رو بگیریم‌ (که بخشی اش متعلق به عمانه) بعد بقیه کشورها از جمله عربستان رو هم مجبور کنیم از همین تنگه عبور کنه و اجبارا به ما پول بده.
(عربستان سواحل دریای سرخ رو هم داره و بدون نیاز به تنگه هرمز می‌تونه نفتش رو صادر کنه، ثابتی میگه:
۱- تنگه رو بگیریم
۲- عربستان رو مجبور کنیم که از اون بنادرش استفاده نکنه، فقط از هرمز استفاده کنه و به ما پول بده)
شهریاری میگه خدا رحم کرد شماها قدرت آمریکا رو ندارید.</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6356" target="_blank">📅 00:19 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6355">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">‏وزارت خارجه جمهوری اسلامی اعلام کرد حمله اوکراین به یک شناور ایرانی در دریای خزر در بامداد شنبه، موجب انفجار کشتی و کشته شدن یک نفر و مجروح شدن یک نفر دیگر شد.
‏همچنین این وزارتخانه افزود،  این اقدام اکراین میتواند آتش جنگ را شعله ورتر کند.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6355" target="_blank">📅 22:31 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6354">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">‏ترامپ در گفتگوی تلفنی با شبکه فرانسوی LCI:
‏«اگر از جمهوری اسلامی ۱۰۰ درصد آنچه را که می‌خواهیم دریافت نکنیم، قطعاً بازگشت کامل به درگیری‌های نظامی را مدنظر قرار خواهم داد.»</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6354" target="_blank">📅 22:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6353">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MHsvwBxoA36ziq5QBErV3s96NEoSL3GsiwPYZNiUkx2IC59KZYYIxntXGU690dytbC95x7yndZugMXoGo60GAqN5IoadXiRAun6xzv96h7mKCATb7G53l6zb-7u7_6nFZ15kH4XIoKWsVc0H0_NmLYSNqrX2r0mRfA0IgA7fypuWS6YlErA677yR5MTl22emuaWss4MpXUq5ybD237QtTTVEjbQWHJCVQ5yBeKJ-_ndafnzK6V2KJPt6xCsIcT6ySChDU8N2Exi3lmdGPkNZtICT8zUA0rT12t_VdDCAFebWHJpfDuqR9IY9LHBNaJm0-yiiH9Jh-5Iqej5N0Wi0VQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اجابت دعای هر روز مردمه</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/6353" target="_blank">📅 16:29 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6352">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">‏فرمانده سابق سپاه:
جمهوری اسلامی و انصارالله (حوثی‌ها)  دیگر وارد چرخه جنگ، آتش‌بس و مذاکره نمی‌شوند.
‏حسین کنعانی‌مقدم، از فرماندهان پیشین سپاه پاسداران، گفت که‌جمهوری اسلامی و انصارالله یمن دیگر وارد چرخه «جنگ، آتش‌بس و مذاکره» نخواهند شد و این الگو، به گفته او، کارایی خود را از دست داده است.
حوثی‌ها دقایقی پیش نیز اعلام کردند که به تاسیسات نفتی عربستان حمله کرده‌اند.</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6352" target="_blank">📅 16:07 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6351">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad32a14512.mp4?token=NcUUmduucW5HJymS-Gwey1Rfrk0JoEGPKHmAqjW1n8adF2RQCwcxK23ijUI-PCZ3fiw6AmTtE9aOiVhzDXjPdRAhfwLEUn_pmcj4GHRV-KHflwDVcBbp_LJ9Bd_FZYkymXAbMwODFypB6KvMfRshx6uqLZK1T1n3Ra_LkbUwdm4B_KDclgx628v--0A-h2gqg-a8YzGqxHavQ3ev8p08ijBj93P3B2D8_4GiLvuqNcY6hPtvkkAmf5D8uk7WdrTGXwd5h_-F3IuP9zjqPtJjBXJN6Krl66JZBC5IAuPyi4iV7R5SGBboqmxs8VZXL5txKlNSH_R1BYw1i7grqME4Fg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad32a14512.mp4?token=NcUUmduucW5HJymS-Gwey1Rfrk0JoEGPKHmAqjW1n8adF2RQCwcxK23ijUI-PCZ3fiw6AmTtE9aOiVhzDXjPdRAhfwLEUn_pmcj4GHRV-KHflwDVcBbp_LJ9Bd_FZYkymXAbMwODFypB6KvMfRshx6uqLZK1T1n3Ra_LkbUwdm4B_KDclgx628v--0A-h2gqg-a8YzGqxHavQ3ev8p08ijBj93P3B2D8_4GiLvuqNcY6hPtvkkAmf5D8uk7WdrTGXwd5h_-F3IuP9zjqPtJjBXJN6Krl66JZBC5IAuPyi4iV7R5SGBboqmxs8VZXL5txKlNSH_R1BYw1i7grqME4Fg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
حمله موشکی اوکراین به کشتی حامل محموله نظامی روسیه برای جمهوری اسلامی در دریای خزر
زلنسکی با انتشار این ویدئو  در توییتر (ایکس) نوشت که نیروهای این کشور در حملات دوربرد در دریای خزر، شناورهایی را که برای انتقال محموله‌های نظامی مرتبط با جمهوری اسلامی استفاده می‌شدند، همراه با یک ناو جنگی هدف قرار دادند.
«با حملات دوربرد در دریای خزر - از جمله کشتی‌های مورد استفاده در حمل محموله‌های نظامی مربوط به ایران و همچنین یک کشتی جنگی - به نتایج بسیار قوی دست یافتیم.»</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6351" target="_blank">📅 14:42 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6350">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P07tx2L8LPm128nj8fVNYocMJhH0nt0Na9EPvLJRaiAOUiOMQUsWqqKavFn4Z1sldavMCiGcwQq-2U0qzbuJ7B23SrIWm1dFheDinP-kkLOT9VuvtTETH-V3_kt0-3BR76L-UFctSUG4mqaEsW5KTTkKV6RmFE_WaOBtFvYxYoFjMfzVkmov2bHUchd8LJvQyEcebAuYm9nRoj6kTSXks1MIptdgfwhVdicC8Y0x1F9jDug8LUYP840HOmwoeFyIgZpqGUIBYmPeNOPAz2IxYjb9Fal7JR9rrhlOmkj6CKMYpjz6toWkyTpnLD4R0HeySA_RF8IV5GZdvllr8_pDXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازرگان می‌گفت ما شب می‌شینیم با اعضای ارشد حزب جمهوری اسلامی مذاکره می‌کنیم، در نهایت به یک توافقی در خصوص سیاست خارجه و….. میرسیم فرداش می‌بینم  در «روزنامه جمهوری اسلامی» و صدا و سیما کلی به ما فحش داده که اینها خائن هستن و…..!  بهشون میگیم مگه ما این تصمیم…</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6350" target="_blank">📅 11:37 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6349">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bHEV4iI2hWBRHb-l4hl9e6miLGpT57ykZvoUpwr6akTkrYxpszLGighXqjGsY5jfA-bwGDLkrxTDds0OKg3NFISAIB4Shwx8fU56znMo5tJsxnWaZgCE4YmS1BPC0udHCQZ4F1154LZdMm3kcc-NMlivI7j9Rx9AMq2mfj7JAr0gESrCDzZH1HZuOhIx7PD3Ni7YayGNpffxjDksD7EJmkHqhVosuRgRFB9Ox62XQhu5HQOWnaZ0vHFV8wXt7YJWCmyfNdNzP4UIMEtwVL1WIuVD1llNtaEqqyalccszSk7Wy307HvLdKHlbk7ujBZtVkrK4XqlsY5xFgPy7BuEASg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خمینی بعد از انقلاب سریعا بر دو چیز  اعمال کنترل انحصاری کرد!  یکی کلید زندان و در اختیار داشتن تازیانه و دوم: منبر و رسانه!  تا اینطور بتونه به راحتی صدای دیگران رو خفه کنه و روایت خودش از هر جریانی  رو جا بندازه، رقیب رو از حق‌ دفاع از خودش محروم کنه، مردم…</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6349" target="_blank">📅 11:23 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6348">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LGWaGuiLfJASY3GdavTQrDC7POtAk7tu5coGvKGYP-FsR5JM4leZFHSRLNAEpWhzKCKE8yQ5oStWRE3FnRcPvNauxiai4gHfQz6u54szo604l4xr03sc9nT-3VQch5rl1xlOkUGQiWMMD-zbld5_iCrFlTo3CONZwGkLuEMyglqigaXpWO-4Cg6Vga8AkopfpT74TAggqlYoLI45FeFvSp-iuRAV7bV0QsWMOA7oMI-MmKaRewSQboynh8RQ479Mb7K-xjQVljEZg6sGE-y4gr5TtVRg62ptyGobnC4kefD_rpEqyzXz3XdcIZbajqal_PMOX75L4od6FGl1v34G7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو روز پیش صدا و سیما،  بخشی از سخنان پزشکیان رو سانسور کرد!  اونجایی که اشاره کرد که خامنه‌ای در نهایت  طرفدار مذاکره شد و کوتاه اومد!  وزیر خارجه‌اش ، عراقچی، اعتراض میکنه که صدا و سیما مطالبش رو درست پوشش نمیده! و میگه یک گروهی خط می‌دن به سخنرانان و مداحان…</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/6348" target="_blank">📅 11:21 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6347">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">دو روز پیش صدا و سیما،
بخشی از سخنان پزشکیان رو سانسور کرد!
اونجایی که اشاره کرد که خامنه‌ای در نهایت
طرفدار مذاکره شد و کوتاه اومد!
وزیر خارجه‌اش ، عراقچی، اعتراض میکنه که
صدا و سیما مطالبش رو درست پوشش نمیده!
و میگه یک گروهی خط می‌دن به سخنرانان و مداحان
در خیابان تا علیه «تفاهم‌نامه» صحبت کنن
در حالی که به قول عراقچی،
این تفاهم‌نامه، بهترین تفاهم ممکن بود!
[همونهایی که موشک به کشتی‌ها میزنن
همونهایی هستن که این تجمعات رو سازماندهی میکنن،
اینو عراقچی هم می‌دونه،
همون‌هایی هستن که در صدا و سیما هستن!]
قبلش هم صدا و سیما،
بخشی از حرفهای قالیباف که مسئول اصلی مذاکراته و رئیس مجلسه رو سانسور کرد!
(یادآوری : هم قالیباف و هم عراقچی خودشون  از مجموعه ۳ پ هستند! و باهاشون اینطور برخورد میکنن!)
این دعوا از اول انقلاب به وجود اومد!
صدا و سیما شد ملک طلق
و منبر اصلی «ولی فقیه» و شد چاقویی
علیه دولت!
حتی علیه خود دولت خامنه‌ای! وقتی
خامنه‌ای رئیس جمهور بود،
رادیو علیه‌اش یک برنامه پخش کرد و‌
رفت گریه کرد و قهر کرد و…..!</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/6347" target="_blank">📅 11:18 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6346">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0dc31ec63d.mp4?token=JLLT7g9fUgyAsac5uxlNDxh72i5xiN6nTg8pge7bYEtxChHj7ovF1Dq9MVTh6C_YBOcWrCN2PYA21vnQMDPRrtsWliR1vcQpwak6PQgBN_iBnyt34o67aZsqMbbKS7oo8tlz-6kfnJPihccpUNIxD_msRtkHC758YJjE5STUxCQr9QOxRLHfv_xcEd6swXDP2Rhsvp_RWWaJW8AMF38ouuf08uvXiuGHLmjbwTsg_QXbc7e2VaqBjITSwgi3Y_1E5p9_a45bNqzgyk15gFgrROG0S2icF7r7My5ap80OT17-qMnP2hsL7oGZ18bQX7p4e8Sqq72920kHW9RsIxf8iw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dc31ec63d.mp4?token=JLLT7g9fUgyAsac5uxlNDxh72i5xiN6nTg8pge7bYEtxChHj7ovF1Dq9MVTh6C_YBOcWrCN2PYA21vnQMDPRrtsWliR1vcQpwak6PQgBN_iBnyt34o67aZsqMbbKS7oo8tlz-6kfnJPihccpUNIxD_msRtkHC758YJjE5STUxCQr9QOxRLHfv_xcEd6swXDP2Rhsvp_RWWaJW8AMF38ouuf08uvXiuGHLmjbwTsg_QXbc7e2VaqBjITSwgi3Y_1E5p9_a45bNqzgyk15gFgrROG0S2icF7r7My5ap80OT17-qMnP2hsL7oGZ18bQX7p4e8Sqq72920kHW9RsIxf8iw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجری : در برجام ما به تعهدات
عمل کردیم اما اونها عمل نکردند!
عراقچی : ما هم عمل نکردیم که!</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6346" target="_blank">📅 11:03 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6345">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kwWT6ZM8kvYXYYy_9BOez_0dNqMTL4-FTuYHyVDqwzLvhoRwDFoT025iQ966AD9qCLCAgIaYyTWQVRXgKjRcfZDPQbjP_gJhweNWLNJH8RNB-DYVyDFuAKGfZkqdwIs_bijMqC0ZydAQCcGC_swGrsnG3w8oUtvrP9kDzNRnGBs-HqIaJS71xRxD-1xW1FD8TWfZakN89Rzwu9p9rW-w9z_Z0DiSwVyJW-hJnnckWkj6QKggojbwMQRohBz9KjPNkpCqulfl9EBkYaH21ZGfzPVuzh5IdMQV6oWZrOChwDGlZFnKXYUtmwhmAEho_tA78g0g4TNPvhOIzrzK99mbdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ‌ «در دوره من رژیمی که زمانی قدرتمند و هراس‌انگیز بود، رهبرانش کنار گذاشته شد.»</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6345" target="_blank">📅 09:03 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6344">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2f4e943e0.mp4?token=eW_LHGmlRLCEFngLjJ0e1Xx5vXgF0etGxneMstRWkicjd_vomtDJvIkpX4KZMlN1249R6GgCd2yUU0xT4GoeMg9anth-iaY8Z-IC-SonEeysluMc2uXaCaoSRnk02V6hw5dAoMaeEZuXxR96c6PlJgKCvXwLUJRWBfBJVYI5T0RiCDMCCqk-2jAzpzebvUWyvq6j1F1V8WLkAdqeKIwCsya2lELw-LygdjlXzvb0XWUD0OIHYmQV5netxfC0eynoYFH3FUb7jFlRxhZS6XCNhqCKihGIZROADAJbAueHkCyoHjRpumh9MTQPDKcHE5so0Nb51JjHdvh8w8rQRqTteQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2f4e943e0.mp4?token=eW_LHGmlRLCEFngLjJ0e1Xx5vXgF0etGxneMstRWkicjd_vomtDJvIkpX4KZMlN1249R6GgCd2yUU0xT4GoeMg9anth-iaY8Z-IC-SonEeysluMc2uXaCaoSRnk02V6hw5dAoMaeEZuXxR96c6PlJgKCvXwLUJRWBfBJVYI5T0RiCDMCCqk-2jAzpzebvUWyvq6j1F1V8WLkAdqeKIwCsya2lELw-LygdjlXzvb0XWUD0OIHYmQV5netxfC0eynoYFH3FUb7jFlRxhZS6XCNhqCKihGIZROADAJbAueHkCyoHjRpumh9MTQPDKcHE5so0Nb51JjHdvh8w8rQRqTteQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در سراسر این رجز خوانی
نه اسمی از ایرانه، نه دفاع از میهن!
نه رستم تهمتن!
شعارهاشون اینها بود!
تهاجم و حمله!
تا ظهور مهدی «در راه فتح فلسطین» میخواستن با اسرائیل‌و آمریکا مبارزه کنن و حیفا رو نابود کنن.
نه در راه ایران! نه برای ایران!
بلکه برای فلسطین!
https://x.com/farahmandalipur/status/2080726571627774147?s=46</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/6344" target="_blank">📅 22:10 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6343">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KVM5SxzASvurfVaEkvKilE6Ef9SfSudTQCqftUns_gGmv-1DrZF6KE5NhGtIeHdfsrkcwr3qBJK1fIXjgTI4YX6UCegySNzU7EGl1_vBWyRhiZDCgC2HAE6nDXstms0G7HEYJ_1YSC0_a9NGlkJAECYW47d0uuy3yH2_asWRpy9ZNhwEi7CFQuy_ZRKE73Xcf1jEJmaEv5kETlJwOruz_WdI3rNMrOf6xfq9rZUHy3vnWo0L7td1_YdSu80pxBU-AJQApkUUqVE-EkNEn1tFQnD6lFiaEeYYfFsG0WXKewgtGgInUktq43NcqSXsxpR6vKvGs22G1U8DWXDR10q0Kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در حمله نظامی آمریکا به ۵ استان ایران
۴ نفر کشته شدن!
فکر کن جمهوری اسلامی هر صبح
با صدای اذانش، بیش از این تعداد
از مردم ایران اعدام میکنه!
جنگ ۴۷ ساله جمهوری اسلامی علیه مردم!</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/6343" target="_blank">📅 19:38 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6342">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">عراقچی میگه توافق ما بهترین توافق ممکن بود
اما به سخنرانان و مداحان تجمعات خط داده شد تا علیه این توافق شعار بدهند.
همه می‌دونن ریشه جنگ‌ها، تحریم‌ها، تنش‌ها، انزوای ایران و….. همه از خود اینهاست!
قبلا هم همینکه در بیرون به توافقی میرسیدن
موشک آزمایش میکردن و روش به عبری
شعار می‌نوشتن!</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/6342" target="_blank">📅 19:35 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6341">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">سپاه خطاب به مردم منطقه : فورا تا شعاع ۵۰۰ متری از محل‌ حضور آمریکایی‌ها فاصله بگیرید.</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/6341" target="_blank">📅 14:05 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6340">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tFirNO4s6j_D7hfVetrBpXg-aKA0cLsiXwVklzJsj1wfbYXvA5sognYrD-WlZQF2s7uRP3DL9eHK7ZJ-mHDATMHOOoT0mf444ZY6_ab-zlUOYFGKABZM3kz8LWulrFTR_f7oKHntIE8f4yhCQV7aOLlFDwvCghl59B1sKVTOSnFM1osNhcOYVU5F-fcUCGKNZBu0m8n_pvRUJZTxt8ty2umDyLRLahCCQbOEa65v2W70GagPGA5HkcLZhflmStkzn9bcAoPddUDfodTEk2hwLbB9-gqbxaEienktRCpeTFM25OqQU8oy6uU3MjaTT5f4KVVb8Eiihj5MhPEZati_AQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صفحه دوم روزنامه کوریره دلا سرا - ایتالیا
حمله دیروز گروه تروریستی حوثی
به دو کشتی تجاری عربستانی،
حدود ۱۰۰ میلیون دلار خسارت وارد کرد.
ترامپ : هزینه این خسارات‌ها رو از پول‌های
مسدود شده ایران بر میداریم!</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/6340" target="_blank">📅 11:25 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6339">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c07c232479.mp4?token=RGvB9sHIQkZD4MqJkUM2D3eguqQJQWlWxXNl3hDGgdMvgP-u9QtSmlHLWWmkDiX-6QkxtY_rx0cWWurdWSgwJOeKCGG0nhfQSe08CvrjtTOMpHrXGgmVSf7F_PnzhXPDmqSqtdGbn2z1ty1TDG77v5eQ8b4RB-eGuO47FOsjjFCC4AeP_gVIN9qjyJhVIc2ZazWtVz_beTfQ6tKxhJ09_1LI--QCxxT6Iwi2F-n5wBudFByTXLEEYpT-xBg3oGRYS2rTYz4a3aZgM_J8gLtUwao8c0fQslw-ATrG7w4f2hbZ-beIGIg0pL5r8mYyu70mlPJdkxHwZV2x9Ki2b3RopgtoAb8QAkEia26ux_kToT9hzXrJqxpl3RjjVanhd1E0NiI1Ak4tiykIbABqBxFLTMUlu-fiF23q8rcG3ylBv5zNK8XbDmaglvC5oGgWuND_dN4RoO-jDbyAIUs_cOG8fTWPGMJBic17f3JdpVdhOZPyFARAr4C1jD-2LZjqaJCpEn5dyur3f2di881f0tlc5-GVfd-XORhL-2c-WuBwzKIziHaY0glZCcTGKrbmRZ-sQUCX2RIekDE9kG15X3Yw1vPgNg2fKp7U58FWGWEdohLeK88yOkkpihPf7-i9U5h53f16Ds1RK6E7EnM2QefESvj5wkVYBDGvOus5_GV6tRU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c07c232479.mp4?token=RGvB9sHIQkZD4MqJkUM2D3eguqQJQWlWxXNl3hDGgdMvgP-u9QtSmlHLWWmkDiX-6QkxtY_rx0cWWurdWSgwJOeKCGG0nhfQSe08CvrjtTOMpHrXGgmVSf7F_PnzhXPDmqSqtdGbn2z1ty1TDG77v5eQ8b4RB-eGuO47FOsjjFCC4AeP_gVIN9qjyJhVIc2ZazWtVz_beTfQ6tKxhJ09_1LI--QCxxT6Iwi2F-n5wBudFByTXLEEYpT-xBg3oGRYS2rTYz4a3aZgM_J8gLtUwao8c0fQslw-ATrG7w4f2hbZ-beIGIg0pL5r8mYyu70mlPJdkxHwZV2x9Ki2b3RopgtoAb8QAkEia26ux_kToT9hzXrJqxpl3RjjVanhd1E0NiI1Ak4tiykIbABqBxFLTMUlu-fiF23q8rcG3ylBv5zNK8XbDmaglvC5oGgWuND_dN4RoO-jDbyAIUs_cOG8fTWPGMJBic17f3JdpVdhOZPyFARAr4C1jD-2LZjqaJCpEn5dyur3f2di881f0tlc5-GVfd-XORhL-2c-WuBwzKIziHaY0glZCcTGKrbmRZ-sQUCX2RIekDE9kG15X3Yw1vPgNg2fKp7U58FWGWEdohLeK88yOkkpihPf7-i9U5h53f16Ds1RK6E7EnM2QefESvj5wkVYBDGvOus5_GV6tRU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روایت وزیر نفت دولت رئیسی از تماس موساد با او و انجام حملاتی در ایران
🔺
جواد اوجی وزیر نفت دولت رئیسی : ما ۱۰ خط لوله بزرگ و سراسری گاز تو کشور داریم، تو یکی از شبای بهمن سال ۱۴۰۲ ساعت ۱ شب موساد با من تماس گرفت گفتن امشب می‌خوایم آتیش بازی کنیم‌ باهم،از من پرسید ۳+۵ چند میشه؟ گفتم ۸، بلافاصله گفت همین الان خط هشتم سراسری گاز رو زدیم، ۵ دقیقه بعد دوستان مسولین بهم زنگ زدن گفتن خط ۸ گاز کشورو زدن،تا داشتم لباس میپوشیدم، موساد دوباره بهم زنگ زد و از من پرسید ۴+۵ چند میشه؟ گفتم ۹، گفت خط نهم سراسری گاز رو هم منفجر کردیم،چند دقیقه بعد مسولین مربوطه بهم زنگ زدن این خبرو هم تایید کردن،من تا رسیدم سه تا خط اصلی گاز مارو زدن.</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/farahmand_alipour/6339" target="_blank">📅 08:24 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6338">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4193f544e.mp4?token=SxBTtSNrIxFZbdYGhJw6QwyOJ-yTwGjI5ZG-gaZMaY3Jp4lIfMRaTi3MvPfQh534eW3YNLBFGbT5mRItQWSuqB0JqZxnmYB_6sJ8xWuSEZWQpqdVHVT07M1PVx9k2UQYZKVn15JMAN8KrCysZzDjiwThi4hU59Wk6ZxkRnIlh7PPzrNcMpB8qboog5zEn19j5GyLIpuezvuv0Br5luPNPWrXwoigGkw529eZNz-rYjJrHj8lS4BVMD1IF8ltIpewFsLOTIbwDlCDP_Vu_iJsxUyO9NFZI9evjZhU1s-jUsfhNU9JwSZ-o4G_LJ2bQ0_9cxQQfDSJh4pDIGKgDwiTrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4193f544e.mp4?token=SxBTtSNrIxFZbdYGhJw6QwyOJ-yTwGjI5ZG-gaZMaY3Jp4lIfMRaTi3MvPfQh534eW3YNLBFGbT5mRItQWSuqB0JqZxnmYB_6sJ8xWuSEZWQpqdVHVT07M1PVx9k2UQYZKVn15JMAN8KrCysZzDjiwThi4hU59Wk6ZxkRnIlh7PPzrNcMpB8qboog5zEn19j5GyLIpuezvuv0Br5luPNPWrXwoigGkw529eZNz-rYjJrHj8lS4BVMD1IF8ltIpewFsLOTIbwDlCDP_Vu_iJsxUyO9NFZI9evjZhU1s-jUsfhNU9JwSZ-o4G_LJ2bQ0_9cxQQfDSJh4pDIGKgDwiTrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب - انفجارهای پی در پی در بندرعباس</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/6338" target="_blank">📅 08:03 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6337">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HEkaZJYt9Dc4s0hbvXaUaQIyIJ_6uOx62PdLpXong49b2xe92VV1hApjJ9Pde7O5IOQ6s1I3V6OiYS6bTY5haQ71k4CIgfTtv4bedOKHhJPY_lLpZLwGGR8oxIjzDVfzlVqOblIV69XWhrQnh9yczJnMfXN4V03cCfSmiZerTnhIizBEmvd3-mahzG3PICp83u_K3jqhzoSkATBbk_779mp00p-E5i1XtB-lx9VB1Cwj8M_1KSO5ybVtWXNRV67Wtp4-Ds-QdDPnf73uRXaK_D2bPGzP3mOH-s4PypC-kOIOU7KjDUoP2ISe_43NtEPyGHY411tF3_wYu4YsgWoAjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تهدید تازه ترامپ‌: از پولهای بلوکه شده ایران، خسارت کشتی‌های آسیب دیده توسط جمهوری اسلامی را پرداخت میکنیم.</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/6337" target="_blank">📅 08:00 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6334">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d84604bc5.mp4?token=Vs697yT7r_I0axdHKuf0poeWgTyUEqu-uZwBG2lZoOIb7oSOzR0if9rzFJm3ZS0kMrdst1_dyr9W-HiLw6j0FZZsa4-kFXR49YQFSAYmBWY9GGkcR6vpVFgTpQNfnSMMjZzIg6hiHepwzNR8uGbRsRvblVLcdwmOfGpTH898qEUak7CKfpl8NHLQS3fS3OM0JvOqQP42-truCD2kRfvbJMzOJBqQP31CzkZKO1RSfmOPz2b3sc4IeNUnhTF6AlfxDyMSV44kPTz9rmGLIHKD78pHBmp8cfMpL8kwmD47RZfDVCQIXdd3KlFn-Bh5X2_El0IfKKpRB_GdyGQZ2TMBizzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d84604bc5.mp4?token=Vs697yT7r_I0axdHKuf0poeWgTyUEqu-uZwBG2lZoOIb7oSOzR0if9rzFJm3ZS0kMrdst1_dyr9W-HiLw6j0FZZsa4-kFXR49YQFSAYmBWY9GGkcR6vpVFgTpQNfnSMMjZzIg6hiHepwzNR8uGbRsRvblVLcdwmOfGpTH898qEUak7CKfpl8NHLQS3fS3OM0JvOqQP42-truCD2kRfvbJMzOJBqQP31CzkZKO1RSfmOPz2b3sc4IeNUnhTF6AlfxDyMSV44kPTz9rmGLIHKD78pHBmp8cfMpL8kwmD47RZfDVCQIXdd3KlFn-Bh5X2_El0IfKKpRB_GdyGQZ2TMBizzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نصب ماکت آبگرمکن در مرکز تهران</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/6334" target="_blank">📅 22:52 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6333">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚨
ترامپ به کانال ۱۲ اسرائیل: در حال بررسی یک حمله گسترده به جمهوری اسلامی هستم؛ حمله‌ای بزرگ‌تر از هر اقدامی که تاکنون انجام شده است. به تصمیم‌گیری درباره آن نزدیک هستم.
او در خصوص احتمال مشارکت اسرائیل هم گفت اگر از آنها بخواهیم ظرف ۲ دقیقه آماده می‌شوند، اما برای آغاز عملیات جدید به هیچ کس نیازی نداریم!</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/6333" target="_blank">📅 21:56 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6332">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">‏هشدار سپاه: هر پایگاهی در بریتانیا که برای انجام حملات علیه ایران مورد استفاده قرار گیرد، یک هدف مشروع خواهد بود.
‏واکنش سخنگوی دولت بریتانیا به هشدار : نیروهای مسلح ما آماده‌اند تا از بریتانیا در برابر هرگونه حمله محافظت کنند.
بریتانیا به‌صورت شبانه‌روزی و در هماهنگی نزدیک با متحدان خود در ناتو، آماده دفاع از خود است.</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/farahmand_alipour/6332" target="_blank">📅 21:24 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6331">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kTHpQh4Hq4juxxbDgEKDbQwrel1sMl4c-vRSRoFGxCq6MB31QQyQFOHVJFI_9MgiVoE-JniUDcsbgcxY0u6rGMpS7_8XqMwtHbMAjkAJj2166FexfKQ3G1-SOymoi0_0XzQs_9Awj2qJwc2AJwi1rUZQWTjLkUoo03YLcSbnESFJgMAo3_9vb_3Jhl-WQtrgxZD6RIxeYq_YO9gMZl_45LKBa5_KJk9AFBiUcWAjgQPuKxfjyu1kxO8DeX-77dyod5RR6ezo4hRGil2XlqVAjSXxA_rpMzhAzJoQdsKy04_1MMz3EewzW2DakgIInSv3EJ_lah0c7ZrTtLg7dI4mqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ضرغامی : فعلا حرفی از مذاکره نزنید!</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/6331" target="_blank">📅 21:22 · 01 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
