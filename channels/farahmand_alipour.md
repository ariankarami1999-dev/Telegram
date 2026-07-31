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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-09 16:41:34</div>
<hr>

<div class="tg-post" id="msg-6450">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01e85bed45.mp4?token=M7Z3VBxBgMCJ0aFtmOBsCg_C-FtGUtgWUEBTrIJWhpjOablGJj5O4BaAHwPJop3A2_Ne78Ixb1d_fh1zQ7eT-MB9y2vaGk146i4mFEeJKrHnMEhbIlHZJ5m_ak3O2r0vQ5QKSQPTwqZRdwF4g6njfPArL4Jo1E7JK7uOTV48ams6a01zSg2w0NVFvKE40jrhLv6vSb0iBFBBJ-5xxOAPhlXcLWhrFk_Yg_QVcMVbYvbpS6hFveXieq3Zgrixh7JOaLVOjrOzC9bZtHlsjnUhwZU7qjrSu_RE7lvrU3kWnr-SXC7f_o8PCLFdnuXMV26C2DZwEj5yHPBY2sZsfvIJWFseYJdyQrrDJAAUS27VEY1N2SxYYtocYzEGdPxPI8lRGkZiFm7S4D-sZs93S6ASB_UqcODuu-0nNnErTbfZ0hWjeAHHf8_baCZ_zArufHPG2w3yPhWXSX4ZBrWirwUZ1FRqs5o4AK60vpBFhON1yWQ_ldbzmDSwwCCodUuZpJLv-OJX079Tmg-NGNpeyqu-UQWhcz2Rnvso4T-G3tCJGwlvcRHxCMHbq93OExA2SnxGlMX13GSPRT2Ub6fbNO-dmaH6YBQGk6JTr4BET854FGiguhGQhlhwJbWzIuinTKeT2C-1q0He6YAYjzIPx8RSvlR3fCZQVwS6w0RL8Cp33Lg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01e85bed45.mp4?token=M7Z3VBxBgMCJ0aFtmOBsCg_C-FtGUtgWUEBTrIJWhpjOablGJj5O4BaAHwPJop3A2_Ne78Ixb1d_fh1zQ7eT-MB9y2vaGk146i4mFEeJKrHnMEhbIlHZJ5m_ak3O2r0vQ5QKSQPTwqZRdwF4g6njfPArL4Jo1E7JK7uOTV48ams6a01zSg2w0NVFvKE40jrhLv6vSb0iBFBBJ-5xxOAPhlXcLWhrFk_Yg_QVcMVbYvbpS6hFveXieq3Zgrixh7JOaLVOjrOzC9bZtHlsjnUhwZU7qjrSu_RE7lvrU3kWnr-SXC7f_o8PCLFdnuXMV26C2DZwEj5yHPBY2sZsfvIJWFseYJdyQrrDJAAUS27VEY1N2SxYYtocYzEGdPxPI8lRGkZiFm7S4D-sZs93S6ASB_UqcODuu-0nNnErTbfZ0hWjeAHHf8_baCZ_zArufHPG2w3yPhWXSX4ZBrWirwUZ1FRqs5o4AK60vpBFhON1yWQ_ldbzmDSwwCCodUuZpJLv-OJX079Tmg-NGNpeyqu-UQWhcz2Rnvso4T-G3tCJGwlvcRHxCMHbq93OExA2SnxGlMX13GSPRT2Ub6fbNO-dmaH6YBQGk6JTr4BET854FGiguhGQhlhwJbWzIuinTKeT2C-1q0He6YAYjzIPx8RSvlR3fCZQVwS6w0RL8Cp33Lg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انتقاد یکی از سیاستمداران اسپانیایی
که مخالف  دولت پدرو سانچز است :
می‌دونید که پدرو سانچز بهترین دوست
آیت‌الله‌ها (جمهوری اسلامی) در اروپاست
و دوست خوب رژیم مادورو بود.</div>
<div class="tg-footer">👁️ 7.23K · <a href="https://t.me/farahmand_alipour/6450" target="_blank">📅 14:57 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6448">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cabfb827a1.mp4?token=epwSbDFccUQ7k0o5tbn8RVo6rNJUHV5KrpNQfy6PqGMnjPhLqBGAHst5B1CVf4A4EKaefDz1-TnVcvyazkzZP_rcTlsJLudy61CIoKrEx7BGt3QL9HliAkuLG9fZZ5niJXG0TtMsAA74MKHv46_8okFsy1D3v8gxfL82x_8akuWzHRjRp5zdNul8sVlgDv5ZtVjOdIN8CPYm0px4wKoDRUrH-R3e-DwE8sINQb8BF8DuwSRYPlMtL3g2LxDQ4CVQcPeh3pywkJS9fevYclGnsHmUwLaNZQHibmYDzZpNVvctzocsNCt4OpAadWcmRBHp3Nt5DAyofyCPR2t-GDfdAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cabfb827a1.mp4?token=epwSbDFccUQ7k0o5tbn8RVo6rNJUHV5KrpNQfy6PqGMnjPhLqBGAHst5B1CVf4A4EKaefDz1-TnVcvyazkzZP_rcTlsJLudy61CIoKrEx7BGt3QL9HliAkuLG9fZZ5niJXG0TtMsAA74MKHv46_8okFsy1D3v8gxfL82x_8akuWzHRjRp5zdNul8sVlgDv5ZtVjOdIN8CPYm0px4wKoDRUrH-R3e-DwE8sINQb8BF8DuwSRYPlMtL3g2LxDQ4CVQcPeh3pywkJS9fevYclGnsHmUwLaNZQHibmYDzZpNVvctzocsNCt4OpAadWcmRBHp3Nt5DAyofyCPR2t-GDfdAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الان خاصیت ابوذر چی بود؟  دستاوردش برای انسان چی بود؟؟  به اندازه یک قرص سر درد،  تونست به بشریت خدمت برسونه که میگی هزار بوعلی و رازی و….. خدمت کنه؟  اینها روشنفکرهای ما بودن!!  این‌ها بت‌های یک نسل از ایرانی‌ها بودن که ثمره افکارشون رو داریم می‌بینیم!ً</div>
<div class="tg-footer">👁️ 9.05K · <a href="https://t.me/farahmand_alipour/6448" target="_blank">📅 14:42 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6447">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KEXtfY8-FEUVtVRd5xFjB7FTDSe3H-iwxnqqV4pDaLdkv0y7wbH0AXhiWInvM1lBBqrvzxqKv2iNdnxi0KUn1Ar_hxL1JYTFcgkKNVTDAzSFwNpn4JAq4ySOeEHQ0G2P827Nz3JrOA_hK1_ex3B-i-CB-8rjALMoiXsNCrr55NwigTZEG4TpaGuYWY8FxGPhSh33Rvg49G_ah-EwktzSJjGN0mYDf5sN8LvAcuuG5TRqW_b6ZQCm1IiFiBoABDuYEQub4Gx9WXdbQZMWwV0To61Ic3vgcleuZTBnmShL9terCQdWPlTGWrZBtNBeGNtE3D1XpjQgYNvBYjV_OpIW-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الان خاصیت ابوذر چی بود؟
دستاوردش برای انسان چی بود؟؟
به اندازه یک قرص سر درد،
تونست به بشریت خدمت برسونه که میگی هزار بوعلی و رازی و….. خدمت کنه؟
اینها روشنفکرهای ما بودن!!
این‌ها بت‌های یک نسل از ایرانی‌ها بودن
که ثمره افکارشون رو داریم می‌بینیم!ً</div>
<div class="tg-footer">👁️ 8.36K · <a href="https://t.me/farahmand_alipour/6447" target="_blank">📅 14:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6445">
<div class="tg-post-header">📌 پیام #97</div>
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
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farahmand_alipour/6445" target="_blank">📅 13:50 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6444">
<div class="tg-post-header">📌 پیام #96</div>
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
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farahmand_alipour/6444" target="_blank">📅 13:27 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6443">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vbjCfFse6t1YbjGml3SlfdHI1-j75JHeGDhn4CS_Sz-Rd--b5MZznij5rB4fQ4rEKfwImdBEWA-mRXcsH0yGj4aSfxDjXKmsln8BTxFIyRyf27zQwZMl5Phoen1u2BSs-VNlElHQzEHHRLuJqzEbHgJFBpglCiSpdMe3gbomE3CGpb1yXPwMsydJY8PR4jOBjywxPBDamF1tyPmULlV3w2BgKY54m-6EcAgSpIZ2NnxkQHMUws0yY5A-jGdlu1A3uzjBtvABiqALg-v8C9G-MZ_Sn4QaMV6CaiaelQ_J-JpPbTah2xg8Bp7h8loPSGRqbuEO7jK6KHPygUymChN3bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپاه امروز هم اعلام کرده که به دو نفتکش در تنگه هرمز حمله کرده.</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farahmand_alipour/6443" target="_blank">📅 13:21 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6442">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ijcuw-5ciz40_ZiXHg2sKAPVPZyWFNrZQtAhsx7FqEbRaazz7BOdbQN8yzPmu5qTLeTuFmcwl2EMLvTaiuOuynvhn409RihWd4PZ5omK_iazIXLuGekF3Ag-hgek_HltpzsEh0ivN4vZNnYH0T58qZI0Y5m5FjeKxDxlYnLGq3BsjQmBaM4-R25cYQHi8FKhxjZDjLeJ2bO4PAKQV-IWNoEpWFRRXED2FJ3W6kG2kNahCVnT-0712xBrQJnXME6QjAUmRBFoynV5oEFdLMbm9r--RLz_nmNqrnTT7cUPKFuCuN9YQLKQgzBerGthXkXfLAbNEt8lEgtW1W2QVDAmSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حدود ۵۰ هزار نفر عمدتا مردان جوان
در ۲۴ ساعت
گذشته وارد شهر ۸۰ هزار نفری
سئوتا در اسپانیا شدند.
🔺
احضار سفیر ایتالیا در مادرید.
در پی انتقادهای دولت ایتالیا به دولت چپگرای «سانچز» در عدم کنترل مرزها
و درخواست بستن فضای شینگن بر روی اسپانیا، موجب خشم دولت اسپانیا شده است.</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farahmand_alipour/6442" target="_blank">📅 13:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6441">
<div class="tg-post-header">📌 پیام #93</div>
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
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/farahmand_alipour/6441" target="_blank">📅 10:31 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6440">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VQkPLrhj-titKRKHHAP81Rfz5Glgg1fVqesasC1Mh4NJOZRWF24RbgqT8632qm_Uvas5TFV8ZOWdTSei84_Y73KLfdVdkBZzwvrUx4Q7YISmLlN5W92iPhIOVBCDKPy-1o9BfskNYqwZ5VkLlm2SfXG6SCoqYaVqOJSlHiblQwi8W_kSKkv_extXawn4EI7f__UPF6AZ1j046tKtlFrCd1eMoB9OVzLLwdQsGHeyBDm88Z9eWaP9HPhtYiLUgqlmWTKBgxrMWBCWP5JxDhZ6cw3eX_bTMygLFesO4tP2jDhYzMI3XSi6rlAU_hobFX1SXs65CHpOM2DT4zGUHtyE4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منطقه‌ای در شمال مراکش نوشته :« راه سخت است، اما رؤیا ارزشش را دارد.» پرچم اسپانیا</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/farahmand_alipour/6440" target="_blank">📅 10:31 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6439">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3f328eb8c.mp4?token=DhXAyoJPTontX84o6DyJIAEe2y45_OTOi9ukfE80_TgXVT_nEob-JV7wWlOxYykNkC156oRQxW2GfXrXL6hztzArz4yBRPYxhVgU2rdf0CREtYBC1jwSH42CMwTV-4akA892dz3DhC0zI3ookcNXXS_ZyUfvV49pRM8g4zl_riQN-S9-jlV7wdXX56Fuk7SNt9b1Ht7x0DfKa1xt2vbFZcTq8Gm7f0I3JP0fjvIG0VrAiNexpkgPV49pfNXHvB6BnDph9HYL3mt367AJD39FepSPgvCz9AiJ54qAnTgHFyS-5opN3st8D8WmUmU548uLpkKkntW2wmlquc3BoMGaJTbJSpqbqSaOCek2vdptcdZUu4kyEq5SZTIs0BfZPVY7YFEAkjrJLQ6oNUGUPW_FXV1TuLMrCt4NorkCr_W2QwBW2KGd6WMhWKthJn6rQIHY2_ihhjonyp2rYAQxoiqzjKaSwm6bWAq3fnAqHjvjtdO63qTBfy2gw8CR5q1i4cd0Ma3QTER7UzJF9qp0yp0NApfwuLFxjHf2TFOkDDgavENc5pvQB8qrb_oPpmZB1wnYE3Tjiv79-ccH96dWD0qBxHYTpChQRaiKLqYKsmo-vI9pd8XjfFY8YNsJx3e7lkGWxFbuBelrCIaFIAoeIzJ-Ylwe-napoYGevUq4aEFhlWk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3f328eb8c.mp4?token=DhXAyoJPTontX84o6DyJIAEe2y45_OTOi9ukfE80_TgXVT_nEob-JV7wWlOxYykNkC156oRQxW2GfXrXL6hztzArz4yBRPYxhVgU2rdf0CREtYBC1jwSH42CMwTV-4akA892dz3DhC0zI3ookcNXXS_ZyUfvV49pRM8g4zl_riQN-S9-jlV7wdXX56Fuk7SNt9b1Ht7x0DfKa1xt2vbFZcTq8Gm7f0I3JP0fjvIG0VrAiNexpkgPV49pfNXHvB6BnDph9HYL3mt367AJD39FepSPgvCz9AiJ54qAnTgHFyS-5opN3st8D8WmUmU548uLpkKkntW2wmlquc3BoMGaJTbJSpqbqSaOCek2vdptcdZUu4kyEq5SZTIs0BfZPVY7YFEAkjrJLQ6oNUGUPW_FXV1TuLMrCt4NorkCr_W2QwBW2KGd6WMhWKthJn6rQIHY2_ihhjonyp2rYAQxoiqzjKaSwm6bWAq3fnAqHjvjtdO63qTBfy2gw8CR5q1i4cd0Ma3QTER7UzJF9qp0yp0NApfwuLFxjHf2TFOkDDgavENc5pvQB8qrb_oPpmZB1wnYE3Tjiv79-ccH96dWD0qBxHYTpChQRaiKLqYKsmo-vI9pd8XjfFY8YNsJx3e7lkGWxFbuBelrCIaFIAoeIzJ-Ylwe-napoYGevUq4aEFhlWk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت دیشب سئوتا  خامنه‌ای هم نیست که بیاد همدردی کنه با جوانان غیور و به پاخواسته مسلمان</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farahmand_alipour/6439" target="_blank">📅 10:17 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6437">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/127d794f5e.mp4?token=cfEFSZqkFD-tpSe0yArs7edwi8rs30Vuor-FA9ObipI1_BUfei9lmZhW1BOrMihp_9gu1jQ_eDs0GtBwEuwAeTwP23yJOvf9v1aYzytGyNM_FCoGyAcLNprFjQL1mUg6Jghd9ihsrM-yzNhURQpVHxy6-fnmjj4-uTkoQbPE8r8ECFxuO8iJrwA2DKQ8WXxlVzzDghD3akgkk9_qtZvcUB27SJShSYhmNo8bLMrrb7teoX2CMcK87SHzywENDkjqgWy19qk9DInALTYRp5_Te4T4HVTAsk2rsKt9KgxH5YmdqrLGNMrKyOTqi4_Szke2z2gzwdHkZTKK_N7JBOPCnEmiwrkOCmmcckACx6StekFIyu0bfnbFPwNOgioUX3-q3BNqqUckxmcybSJQQhqOUZM1e_DbBmjhKNuJ_UpHT_pcRrR8TXUQkdSLjI2DOuIqKT5vRgxkGejm19VyTEZhCU8fk51X2V3hluTWXJEbUtDxAS2-MgJ_K0fFRa7yaXyznYuOhiTyZNV-iji1UmhCrg09UlMqsSN3K2iauKzOEzCuZSojYIDvAXpBEirNAJ8WLRS8Sa0mHYdXSlaO4osU3rFv9Se0r3_3fpoVWuHVI1bP2CrcoaidnMI-o4vEO7lR4x7iJtinSKLwPU6Ex7H_T9Ahv-LHS7t8hsUzZGF3_H0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/127d794f5e.mp4?token=cfEFSZqkFD-tpSe0yArs7edwi8rs30Vuor-FA9ObipI1_BUfei9lmZhW1BOrMihp_9gu1jQ_eDs0GtBwEuwAeTwP23yJOvf9v1aYzytGyNM_FCoGyAcLNprFjQL1mUg6Jghd9ihsrM-yzNhURQpVHxy6-fnmjj4-uTkoQbPE8r8ECFxuO8iJrwA2DKQ8WXxlVzzDghD3akgkk9_qtZvcUB27SJShSYhmNo8bLMrrb7teoX2CMcK87SHzywENDkjqgWy19qk9DInALTYRp5_Te4T4HVTAsk2rsKt9KgxH5YmdqrLGNMrKyOTqi4_Szke2z2gzwdHkZTKK_N7JBOPCnEmiwrkOCmmcckACx6StekFIyu0bfnbFPwNOgioUX3-q3BNqqUckxmcybSJQQhqOUZM1e_DbBmjhKNuJ_UpHT_pcRrR8TXUQkdSLjI2DOuIqKT5vRgxkGejm19VyTEZhCU8fk51X2V3hluTWXJEbUtDxAS2-MgJ_K0fFRa7yaXyznYuOhiTyZNV-iji1UmhCrg09UlMqsSN3K2iauKzOEzCuZSojYIDvAXpBEirNAJ8WLRS8Sa0mHYdXSlaO4osU3rFv9Se0r3_3fpoVWuHVI1bP2CrcoaidnMI-o4vEO7lR4x7iJtinSKLwPU6Ex7H_T9Ahv-LHS7t8hsUzZGF3_H0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت دیشب سئوتا
خامنه‌ای هم نیست که بیاد همدردی کنه با جوانان غیور و به پاخواسته مسلمان</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farahmand_alipour/6437" target="_blank">📅 10:12 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6436">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a175d481ad.mp4?token=rQ_CbPB74cL7H8L1N5Mq5EkNLG4qy9kZvscCqdY6NCOfmpLY-BGAjARXG21N_rvacjf4CMiRWf9S1KilDbnm51w6SY2ob9hP0HuG8uOe6r0b5fnNpeXZ-NazDKvq8JWhjK0GrWCICtcBO4gIPqI-pBFw_O2BiVjKn9fZIwL_nNKBRuiYbYRaCezvRWAMExD7OIKAqgVK0hO-7svOxyj6QJOKUndhTBsmmemGwNn8WPhbNULM6hdsgsqO48jUHMvf1GsWWFaipDjNeKzsG__IbC-HovC2hOPeG_WVw5v6I-IWrohuJcW7ArhjvloMIBTfKqaUkTZw2bwKtkDOTQ_eJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a175d481ad.mp4?token=rQ_CbPB74cL7H8L1N5Mq5EkNLG4qy9kZvscCqdY6NCOfmpLY-BGAjARXG21N_rvacjf4CMiRWf9S1KilDbnm51w6SY2ob9hP0HuG8uOe6r0b5fnNpeXZ-NazDKvq8JWhjK0GrWCICtcBO4gIPqI-pBFw_O2BiVjKn9fZIwL_nNKBRuiYbYRaCezvRWAMExD7OIKAqgVK0hO-7svOxyj6QJOKUndhTBsmmemGwNn8WPhbNULM6hdsgsqO48jUHMvf1GsWWFaipDjNeKzsG__IbC-HovC2hOPeG_WVw5v6I-IWrohuJcW7ArhjvloMIBTfKqaUkTZw2bwKtkDOTQ_eJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ساکنان سئوتا تجمع اعتراضی برگزار کرده‌اند و دولت چپگرای پدرو سانچز را «فاسد» و «خائن» توصیف کردند.  سانچز شخصا فردا به سئوتا می‌رود.</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/farahmand_alipour/6436" target="_blank">📅 09:01 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6435">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QHFF007gnUwyiBjcWtsCKXIJxyU5wSHzhBChEB8DiVjIMu6_rTPYXcNPgpr8gN2no7oqo_Xg8YX_1RWRcJCjCG3QE2xJ8tFu1IirUjK8rddXca6lI4S1U8bU7u5IUcMfkqad5lp9AS6D3aQICVR4bb8vtl3oOmwqPlBaOL_zo1DCyWKE05wBMpQY4og0yACEJD4PBuPPn-ge7KxCmIbJHZuTGwqF1gxcV4kdXbaBTwjLHgOTpuF4bVNrabA7xwDlY4Ji29k2lqw7YPQegBWmTtx56PcWKPtpCGwExyoLwHZ7wwjvlbjmwZRSF7ybBSmvd6HkdnTZCvZTbwrQyHMZ4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولی امضا کرد و خلع سلاح رو پذیرفت!
نتیجه عملیات ۷ اکتبر که خامنه‌ای میگفت :
« تاریخ ساز» و «ضربه فنی جبران ناپذیر» ، شد نابودی غزه و کشته شدن ده‌ها هزار نفر و از دست دادن ۷۰٪ خاک غزه و حالا هم امضا کردن خلع سلاح شدیم!
کی به این گروه تروریستی پول و سلاح میداد و برای این برنامه ها تشویقشون می‌کرد؟</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/farahmand_alipour/6435" target="_blank">📅 08:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6434">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fcDy5iNvQehdNbDoLsI0brLi0u-AtVLDyYypgGW52M2uEkVkoZi8otfB8qxEE9Tn13IOOCm1Y9_TZ8LV9qT_drizBVziD_21OkyVPGiLZg-4I0cQ4KVhUIJg39UzhIn3Mr0_n3n46De3GCGetSdFPqS1KyUDeo17sAIKsgP18CTVqzmA-eTyyxuaJO9YoZI--Q5JazAkwk76jlDQ-HAYLmMgG2zECYS_3Bw6QBV39rQa9O7LtEOqq6KsDtBaTyecuuf-GnWnYi3-QCfeajPlTjnYZect7epGZ78kKQQwphLTX1Y6g1J7xYobbcElHoXh7kGSHOdeIY7AM9trztwJiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جوون‌های مراکشی رو اینطوری میارن کنار  مرز اسپانیا
🔺
در یک موضع شدید انتقادی نسبت به رویکرد دولت چپگرای پدرو سانچز، دولت ایتالیا خواستار تعلیق امتیاز شینگن برای اسپانیا شد.</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farahmand_alipour/6434" target="_blank">📅 01:49 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6433">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cceceaa5a9.mp4?token=bRN2eQ8oBFqwzGNyUlGPXvV_hzRjjGTyn5nXE6hyatfRGCjgXR1ojvWC703sFvY3pO3_3ELakv_WxoWSeyDCWItHsc9D2BmlV193pGOfXUkkyvNKBZlqyZ4EPRmCFE02ZE-QBP0S7hnCQhp6VrqknRI6Zn1_BG0gnb8dPE7pemL27a8OiHMWjhvljd9vyI8v6MSo_oXRCpwcbFHwQKlr8ErvXY3hroqk9rEGzv7aiwk04ZukUq4Hf1sKmRTL_kj9EKk6rOfc-NMBbYv6l6n74ZcPmUQap-VKG6I9wJ7fKDzqzQLMsfroyauT3WdwDdcnEWKtbedSxDxdlQGZokkdp04fXbnZLH1QMIiSnYkWcgfXlac96jZbtReNaGi5_8nvm-SXoAfWxxFdZ96Y32xTfI8c2k_sjEAFRshefBHFLJCEq-CRWnZGXcNv93YFYyxHowkjk7p549aQdhge-mrmtmTzAOYopxglxlQDEuW5dV1eltvvTYv9woa-lAui-Z90w1F0o6Bd0v01t0QBKCazbdHiYn8a94yFHQ0HT-rVZ3T26ihm1A_Yc6cbN0kzcG5XSVaK03Ljc9phomdva2-Z_Pl-o6jjzGzSUUd-hdhZuQ20xnDnX_aflu3CSNIltGK8Yh_ew6MRqPThhvuwBKP_eV1z6vQT7d8dAAolX9_miAo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cceceaa5a9.mp4?token=bRN2eQ8oBFqwzGNyUlGPXvV_hzRjjGTyn5nXE6hyatfRGCjgXR1ojvWC703sFvY3pO3_3ELakv_WxoWSeyDCWItHsc9D2BmlV193pGOfXUkkyvNKBZlqyZ4EPRmCFE02ZE-QBP0S7hnCQhp6VrqknRI6Zn1_BG0gnb8dPE7pemL27a8OiHMWjhvljd9vyI8v6MSo_oXRCpwcbFHwQKlr8ErvXY3hroqk9rEGzv7aiwk04ZukUq4Hf1sKmRTL_kj9EKk6rOfc-NMBbYv6l6n74ZcPmUQap-VKG6I9wJ7fKDzqzQLMsfroyauT3WdwDdcnEWKtbedSxDxdlQGZokkdp04fXbnZLH1QMIiSnYkWcgfXlac96jZbtReNaGi5_8nvm-SXoAfWxxFdZ96Y32xTfI8c2k_sjEAFRshefBHFLJCEq-CRWnZGXcNv93YFYyxHowkjk7p549aQdhge-mrmtmTzAOYopxglxlQDEuW5dV1eltvvTYv9woa-lAui-Z90w1F0o6Bd0v01t0QBKCazbdHiYn8a94yFHQ0HT-rVZ3T26ihm1A_Yc6cbN0kzcG5XSVaK03Ljc9phomdva2-Z_Pl-o6jjzGzSUUd-hdhZuQ20xnDnX_aflu3CSNIltGK8Yh_ew6MRqPThhvuwBKP_eV1z6vQT7d8dAAolX9_miAo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تداوم ورود هزاران نفر به خاک اسپانیا  اغلب این افراد مردان جوان و نوجوان هستند.</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/6433" target="_blank">📅 01:37 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6432">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c72fd0437.mp4?token=snfmXWm8OXqwv1HEVlrDQWBcfJYMHarp4KqNY0DI3zdaNUF1dzmKWWFqrJ5KcY5RGLXm-U4ZT8U_CgOLMnsgV8RXKkiry2tOjyCgHmcHKi8jMw_0QMUEPmqI_2v7FGIKSR7AcnlOpEMjDMIFFZra-Bumm22eBUC-3ItW9bugwSLtWMHPkj3g66kZ4T0GGRwWoGzhAmwgsDYS6_vqnIjQ_n-ahEHJUnICDTSDo8OxOaShWYqEETPVdKg4ZnLVPMWHkQxtJgvBRDPoJb2W3Srydxi871RuJ9Z6myGkuN16cstm1Xszi39Y-hVgcfnLEVedtFzs8S5H1bjvsu4l7jUqHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c72fd0437.mp4?token=snfmXWm8OXqwv1HEVlrDQWBcfJYMHarp4KqNY0DI3zdaNUF1dzmKWWFqrJ5KcY5RGLXm-U4ZT8U_CgOLMnsgV8RXKkiry2tOjyCgHmcHKi8jMw_0QMUEPmqI_2v7FGIKSR7AcnlOpEMjDMIFFZra-Bumm22eBUC-3ItW9bugwSLtWMHPkj3g66kZ4T0GGRwWoGzhAmwgsDYS6_vqnIjQ_n-ahEHJUnICDTSDo8OxOaShWYqEETPVdKg4ZnLVPMWHkQxtJgvBRDPoJb2W3Srydxi871RuJ9Z6myGkuN16cstm1Xszi39Y-hVgcfnLEVedtFzs8S5H1bjvsu4l7jUqHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حدود دو هفته پیش دادگاه عالی اسپانیا حکمی داد که افرادی که از طریق دریا وارد خاک اسپانیا میشن، نباید فورا دستگیر بشن و عودت داده بشن. اما اگه از موانع مرزی عبور کنن، پلیس باید اونها رو دستگیر کنه. این چند روز عده‌‌‌ای جوان از مراکش و از طریق دریا وارد اسپانیا…</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farahmand_alipour/6432" target="_blank">📅 01:05 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6431">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">دو نقطه بسیار کوچک از خاک اسپانیا چسبیده به خاک مراکشه.  خیلی کوچیکه اندازه یک پنجم جزیره کیش ایران. اینها در واقع از خاک مراکش فرار کردن و وارد این نقطه کوچیک از خاک اسپانیا شدند در Ceuta</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/6431" target="_blank">📅 00:58 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6430">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AgyfBDuDCJAt0JNr3swz4HIiKL9HrZbuqCUgpWgoWH-EZ48shYa12Y9jdCvxYiiUNFYEdJyEo7wU00C_BFnb_CTyVpzrMF5rOaoq9kfY20upu4yrh3hB5FuUoO5req5uCes4pUb52gmb0Fy7wTOXqJ3zoNQli2K0qbjfW0UG-maUyxTkGqrZoG-0yyCxvc7BaTOLtGogCdjOavj9BXcFLXh7XHPNWWIadDPMDLkUiV1vEWOIIbA-gd7WI75ohIeh1Pk1T33bNTZMkSWE1h7eaOVXSgYf4bfPEE0IOn0k3beN_HQF1mbN29UXT4qshW1DSNBZOglA8ZOoGk8W2oZOog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تاکنون ۱۳ کشور اسلامی
به درخواست عربستان لبیک گفتن!
برای حمله به گروه تروریستی حوثی‌ها در یمن،
از جمله : پاکستان!!
مصر و ترکیه !</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/6430" target="_blank">📅 21:43 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6428">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kCJL3-8VxSn7fEsY3P6E7Yu35KygkPYAz9kSrPiP6mOf8U_s1hTygNHV29aoJtMFV3uDNu2SOmOr0pRE8Uvfb_4v3pd1wxSiC7wpZnrAVsKJuukgP-edn0XvKe6r92a-BQk70aHqprMQhb3F-ozQFNjyygGncCdKUSeTnA49lpLU-LKQovR3tXzfRYEQ13VxHLLbiH9ZOq8KL8MaWIGiCzWEk2jLqvCACusOmTarI5B3ycu06qcPPIP_Ppb52ylFXvsw2sTsuqNG8bwZzP13zYu87MoCAD9yHgVbxg1mP8ENRHtvk-EBW8FmpMPAivbYtiDzL3qDs_aptE84S3_x2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k6o_eglxUvLacGXZye2OyihPkN7a5j9f-Oay67sobqxuG0JPzYYlf2BqkS0r-E5XBMoNd7Q0zW1ROE4tzSAeXpHPX4gRF4fq8_5izE3dcPloqFeWYglln5JoAbjrB1HgejmIyw4rhLPAxSHMpEnFaiCAm_zP6d6pTKll-d89CRMLGFQNOSEMtTr4KWTbiYebfVlNzk6VSukN5lBsPdum6nr0JgWmuL6Uhx8iGi_Bau4kcAwm2815DMB0w7oQ8B161wRrGs7jPIRnntC6T1_bosEnzF3Rcsvy_lLxNqgumrgS3zRufK_ILvES1BETTG_d3yjiyn8pjHu6gsh_xcHlQA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دو نقطه بسیار کوچک از خاک اسپانیا
چسبیده به خاک مراکشه.
خیلی کوچیکه اندازه یک پنجم جزیره کیش ایران. اینها در واقع از خاک مراکش فرار کردن و وارد این نقطه کوچیک از خاک اسپانیا شدند
در Ceuta</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/6428" target="_blank">📅 18:06 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6427">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39130dc900.mp4?token=XBcr5e3nl1rPfK90uRotUUlyu0pBiFkgcgN7RbbrDc533iFTVVcWrcP4mlMqd6Wm9v2bbmUc9n2-3WJ1HLMy3diWg-qnYcqrTUdZ-reP8pAV8AmeAdIkxDAJqKuovZAfYSIloqoPefR-MC2vR3etkpTFI6311HyuoIYXrrmqXXoiNS-QYzSBeZidCSAZ2peR3PDitv7FRNtqHW76W7GQPVLyQIftYpalBOltrLL0d1EG_3rj_2lCjYFgVrWOzKufWzkijoVzWQWxMeRQc1COUieY6bEAHsPm1oqQahJyPSJvZBsGY-nimhpLriVyJuT5Im-qwvGw8A371ehOlrPYDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39130dc900.mp4?token=XBcr5e3nl1rPfK90uRotUUlyu0pBiFkgcgN7RbbrDc533iFTVVcWrcP4mlMqd6Wm9v2bbmUc9n2-3WJ1HLMy3diWg-qnYcqrTUdZ-reP8pAV8AmeAdIkxDAJqKuovZAfYSIloqoPefR-MC2vR3etkpTFI6311HyuoIYXrrmqXXoiNS-QYzSBeZidCSAZ2peR3PDitv7FRNtqHW76W7GQPVLyQIftYpalBOltrLL0d1EG_3rj_2lCjYFgVrWOzKufWzkijoVzWQWxMeRQc1COUieY6bEAHsPm1oqQahJyPSJvZBsGY-nimhpLriVyJuT5Im-qwvGw8A371ehOlrPYDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرار صدها نفر از مراکش و ورود به اسپانیا</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/6427" target="_blank">📅 18:02 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6426">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd3e7e1df2.mp4?token=WBRY1_c4M2TuC6EEwqnir8Z8JV5kBHrddD4oHcrbnSbxAtynWgmeLG-xtmIK1f9XEeJ-I-pDllMVq63Sqh0LFuW2JFPGE4pJPT5kaxgo8vfWxEL5TmgnE8ZQq5bniUiM-rj2U0NlkOtckdcJUZuMOVPdoCbmHeG2s_iPzczLHUA-auam_SpYPzaYhyxN036EtKaPg4X6akVuvpNIN0XaCrpVFAI5_93Kmsx8X5P6LxqwSl6UIzrg8KMS26JkppDPtpJkuvfUHbU9p67yfzYSkintWH5rRzlNf8VqW5GZ4JbmHzYsEy9wuqBY79ToxLnBIEv-5d-LZ2xWXG7gAclITJqEcEkXE9hriXDkjnZiwiwKq_k_XRFylggJmMeiVkCxZrHPhjHLvfXJg2nuike8TYQe8I8MzCUgcty0b6e5TvrcErUvlDJcN-qHVVVqEwHBFhMZek7FfJEBj7GbREovVGyaAd2CU9pHGkvxC1nivuaf0Ii1lE-9Hu7jxL0GrQe0Ny7tcTWcZVC4hEagVZG8M_FOerITeK7Kr7oXxIzx_u8F5nw4A7mnPf3CbktrhmHqtdTH8CMerSPXMHpbQgGnY7ZqhsdPpFMm1Q8DhuLlH4YFD8dgf-1L5qS3WCB-zHrA7wmGpftasdxcTyC58qjbhMuStUss9WqQEJBcu1PbMew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd3e7e1df2.mp4?token=WBRY1_c4M2TuC6EEwqnir8Z8JV5kBHrddD4oHcrbnSbxAtynWgmeLG-xtmIK1f9XEeJ-I-pDllMVq63Sqh0LFuW2JFPGE4pJPT5kaxgo8vfWxEL5TmgnE8ZQq5bniUiM-rj2U0NlkOtckdcJUZuMOVPdoCbmHeG2s_iPzczLHUA-auam_SpYPzaYhyxN036EtKaPg4X6akVuvpNIN0XaCrpVFAI5_93Kmsx8X5P6LxqwSl6UIzrg8KMS26JkppDPtpJkuvfUHbU9p67yfzYSkintWH5rRzlNf8VqW5GZ4JbmHzYsEy9wuqBY79ToxLnBIEv-5d-LZ2xWXG7gAclITJqEcEkXE9hriXDkjnZiwiwKq_k_XRFylggJmMeiVkCxZrHPhjHLvfXJg2nuike8TYQe8I8MzCUgcty0b6e5TvrcErUvlDJcN-qHVVVqEwHBFhMZek7FfJEBj7GbREovVGyaAd2CU9pHGkvxC1nivuaf0Ii1lE-9Hu7jxL0GrQe0Ny7tcTWcZVC4hEagVZG8M_FOerITeK7Kr7oXxIzx_u8F5nw4A7mnPf3CbktrhmHqtdTH8CMerSPXMHpbQgGnY7ZqhsdPpFMm1Q8DhuLlH4YFD8dgf-1L5qS3WCB-zHrA7wmGpftasdxcTyC58qjbhMuStUss9WqQEJBcu1PbMew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرار صدها نفر از مراکش و ورود به اسپانیا</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/6426" target="_blank">📅 17:50 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6425">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
سپاه از کشته شدن سه تن از اعضایش در جریان حمله شب گذشته آمریکا به زنجان خبر داد.</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/6425" target="_blank">📅 14:35 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6424">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZezZ585YnyvwQo4SC4MEyACSA2PhBU6Iwzr_ZioJmS0Do8dqrtjaG19OMD2H-xi2B3JWGLJL-sUiQItMm6jpdUA3YzOqLbvMsOxRwysYmdq917SDzE49kKxzRsR825iMPU1exzAxzspp6jEl89zBIreJgamK9exBDwEMLHO1f97XchBi0lcNPk7XNX8WaOz-MIKe9sdOmef1p3lVBcTXLW3yXUFx5-qCBo1pSX_31E72I0P5-1dTXYXRLG-HGjyuAZP0obKF7KQTZk8TuHch_CMGm031lgudMGVeDJ1EyqJc6HPG0WpQchMasChK3wGW2GufjVkHxA8xNLgClv0X0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو رهبر شیعه، هر دو مبارز علیه آمریکا،
هر دو حامی سرسخت فلسطین
هر دو خود را پیرو مکتب حسین معرفی میکنن،
هر دو اتفاقا دشمن پهلوی،
هر دو هم در غیبت به سر می‌برن
و پیروانشون در انتظار ظهور!</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6424" target="_blank">📅 14:27 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6423">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
🚨
گروه تروریستی حزب‌الله لبنان با یک پهپاد به یک خودروی نظامی اسرائیلی حمله کرد،  ارتش اسرائیل : بزودی به نقض آتش‌بس حزب‌الله پاسخ می‌دهیم.</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6423" target="_blank">📅 11:57 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6422">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sj3NRpKrRUnHi4431e1iTrQJjCKh_nvKlkErGsvAWqdzzQNpg6RvZjcawsrjuI9JQSe53GVPVoKp72HIToCo1nIw4mFOehF6aT8O5b-vRVC2mmlQnw4K70JehPKn_MTNvv7xNmxqL0i4dqhEI4V6EOMtK1lVChMOAblqJRb27RHB51z6NsEMpczDIwwb6p_KPx8WMyFVLJJL0Do8qhY6fquO1Kif60LFWtEGSON4XwtBZ5hlnJCwyEZeV8YcwU-wAxt4jU22BM0WnVRx3uOWj8pYBmdUbD2qrUmX7nu4150U0fcSEyENji0uj0c3N1xzTMWldPDwzkNlhxC2VMdY6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جاوید نام «امیرحسین صفری»
که جمهوری اسلامی دیروز او را در
اصفهان اعدام کرد،
فرزند شهید بوده.</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/6422" target="_blank">📅 11:54 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6421">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3dca15fd7a.mp4?token=c8TwNGIHGbxioG9WhTg6yfmM969G57KgNly70p23Na8f1Hhxl7nX2rC5DruIUfrEyra_sTmg1hwsC-BO7UPMQhuiNIDkGIggljj_Bl3Ui6WwvtX0XCoJnWbQzlNBScP26XLQZHv7zzTMol1N1LAsRF_U0yiJ11scpfXQwy8fioHSkGyu-vwDt2L2xqq_hmSCclxLhCDoA6HT_rOhp212kiQxnsMw4WQ9UVzbD4KIab66ujFU-h0bKC7B3TSLarDTgDHXSf96mFobDoy2PW9XUNDQ60sDqRlB2nEbCzsbg1x69oxcvKOfI1tj620FwAhkQxyW7nKNRuMOrNV_XRWHyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3dca15fd7a.mp4?token=c8TwNGIHGbxioG9WhTg6yfmM969G57KgNly70p23Na8f1Hhxl7nX2rC5DruIUfrEyra_sTmg1hwsC-BO7UPMQhuiNIDkGIggljj_Bl3Ui6WwvtX0XCoJnWbQzlNBScP26XLQZHv7zzTMol1N1LAsRF_U0yiJ11scpfXQwy8fioHSkGyu-vwDt2L2xqq_hmSCclxLhCDoA6HT_rOhp212kiQxnsMw4WQ9UVzbD4KIab66ujFU-h0bKC7B3TSLarDTgDHXSf96mFobDoy2PW9XUNDQ60sDqRlB2nEbCzsbg1x69oxcvKOfI1tj620FwAhkQxyW7nKNRuMOrNV_XRWHyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گفته می‌شود که در جریان حملات شب گذشته آمریکا، ساختمان «اطلاعات ۳ پ»
اهواز مورد حمله قرار گرفت  و ویران شد.</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/6421" target="_blank">📅 11:51 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6420">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
سپاه:
به حول و قوه الهی، امروز مجازات متجاوزین اعمال خواهد شد.</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/6420" target="_blank">📅 11:49 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6419">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ra0ZeBPXppuao8-1b4NQXVf6irb7Ucjapg-8Dx_KQTryuR4cT3xWobX1MkS14Q_iGFsLRSBsWXKTzwcuM2XjRtu8FAsbTqgsrkGqMyypnHQqK9jSxH10cPlw31U0gdoI4pJR3FDw4_ezzWDbB1PmLtuItdEgG9T_Z7JvzdWFSgEu_tIewgNL9XYi0smZlhrBm24Yn_OwX8x-V8JGiw_1Ow12CDoKnSd5zyaGJ0kVicO8yeoi3E2qMlr24h0oEP1lq9gFIlzQ0Ma3hrnSzcoY1inTFq0-wa1uyyRCKn5lU7jZ_wly_Yn3d4DFJQiqY5Qf9pMdE20za-GUSy-x4Yy80g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔺
دیروز جمهوری اسلامی با پهپاد به دو کشتی حامل گاز مایع در مصر حمله کرد.
امروز دو تن از مقامات جمهوری اسلامی به روزنامه نیویورک تایمز گفتند که این فقط یک هشدار بود.
(که علاوه بر تنگه هرمز و باب‌المندب،
می‌تونیم در مصر و کانال سوئز هم تاثیرگذار باشیم)
🔺
صبح امروز هم سپاه بیانیه‌ای صادر کرد و از حمله به دو کشتی در تنگه هرمز خبر داد که قصد داشتند از طریق آب‌های ساحلی عمان از تنگه عبور کنند.
🔺
دیروز صبح هم به سه کشتی در تنگه هزمز حمله کردند.</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6419" target="_blank">📅 10:29 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6418">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E4QhXnffRVFiBL2jRJigpbXdfwkqV3khlsvxJ_R-gQmLRLCYRdOpfrwNHLSfG6rPl4FPmOdO3SU6SPmLs7NRjX3E0gwFtJuy7Oukq6M7a-RnjN6icR3wk9GZN3Fast6O7v3NfrBIsgJ76u53dGV4KiYBpqtDsxXrP7hPuXbd2tfD-Y9OpVRzLX10VWz4CDpe3t-C96w5GQkyiLNb5vJD3DTS4hj6x91XUJ1YUrUw0GEuXleorkyL1Kvrl2EM9OOLYAmnS29Yl8ACWvpliq7Y18i-84vdkRzFpNkAdDcUYzsKtqM_hJ_qPv14nl_YUj8U4y8Edv-PmALZv8SzH_Av0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیروز صبح گفتن به سه کشتی حمله کردن
امروز صبح به دو کشتی</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6418" target="_blank">📅 09:18 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6417">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🚨
🚨
🚨
حملات موشکی آمریکا
به چند نقطه در اطراف آبادان.
شنیده شدن صدای انفجارهایی
در قشم، بوشهر، کازرون.</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6417" target="_blank">📅 04:39 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6416">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🚨
🚨
ترامپ : ایرانی‌ها می‌دونن که ما امروز شدیدا بهشون حمله میکنیم. اکنون نوبت ماست. ضربه سختی به آنها خواهیم زد.</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/6416" target="_blank">📅 23:00 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6415">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hDlhBQ_nJHSd_1gVRBxRswrbFvjNDsjtEMGT-HggzcQu6ajqQALP6lv3CGX57wbTsgOtCdruiu5y_C4ofBc0uMBl4phJyuYoezilu1Zh7aYSIuOYR53X_H_ntiFOlz9cwFJDSl44JDefb-o5w97ztqeYmjfy3_CuByxMa2N_6DTVQjAi_G9k-GF2zuaXicIMoZ88wjGKVYw9CHSYCrfC0hPBMiG8AqDVvRKVTxwQ-tNpt1-xmd-3G0NTmr-J2OuSxq3uEsTzYVkSLrUhrUAlINNVdPwqtzSsFDldWRxCeyuLyFIRVT8xKLXOpH-xXhdumjXPzcfp1Q3kG7vsaiT1_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
تعداد تلفات گروه تروریستی حشدالشعبی به ۸۰ کشته و ۲۷۰ زخمی رسید!
ایالات متحده و عربستان شب گذشته در پاسخ به حملات پهپادی گروه‌های وابسته به جمهوری اسلامی به عربستان،
به مواضع حشدالشعبی در ۷ استان عراق حمله کردند.</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/farahmand_alipour/6415" target="_blank">📅 19:58 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6414">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b85006cf0.mp4?token=u7upMfX1E4hXA5sNZbH9MPZseef-5TqLgntayvo-2jj5y_Znolm_7Jedti2ttL5k4PtOvGwHkY3LFPTL7e9i0OqRnRQChlv4n2ufY21FC9UPcHjbpc_eSUmGmO9yiPpzgZRG0FKc1Zp3QMF6v7CGDcxK8yrH4HlTF1bf24QRYnCrhELnmG_fSuB0CXifs87Up4a5mIBktfZMg5CfgV0CxYCoo5ORfFHRhi6C0XNvD9GeNyYgKWvs-X3aUlDa9mMW4sbYg2lKfaEvMJp5Nria1mrFZP6ZJU4cmFkF41NSuj4w7wsv4JXQm2a0x1_lGLgGTVGEniF0vlO6aUPAA81hLTJeHnWetM-4IJuSMacKhcqBzlvoLSHTfuSA8LKVW9tPh93BupcLnFzZDc6yHL5l1pn1-Hy8zqZEkIcxn-c-O9F1xJhDBkb4q-3_--mtFqfWiyNTovW3bM0Zy3Kp_8PXzUwfNqcoQ_mDBc43bZQUT4VdfLgz1oeXf2CUd0lVUg-Ohd3dUrGHL6ZGoS9jJ4mNGUpmMJZkkrtGNphTH6cxeA19BrHUucs-CNNcJxF_Y36_zFQdJg5zAis2bsCZ5lH9xHsYSKVoV1ALWtp-dcxh0MNbX6-TMNpdCrUKnkog__G4IC5ZClUoWQ73qnpzgxddjNw440ESuTYjnQO5LNEtY7k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b85006cf0.mp4?token=u7upMfX1E4hXA5sNZbH9MPZseef-5TqLgntayvo-2jj5y_Znolm_7Jedti2ttL5k4PtOvGwHkY3LFPTL7e9i0OqRnRQChlv4n2ufY21FC9UPcHjbpc_eSUmGmO9yiPpzgZRG0FKc1Zp3QMF6v7CGDcxK8yrH4HlTF1bf24QRYnCrhELnmG_fSuB0CXifs87Up4a5mIBktfZMg5CfgV0CxYCoo5ORfFHRhi6C0XNvD9GeNyYgKWvs-X3aUlDa9mMW4sbYg2lKfaEvMJp5Nria1mrFZP6ZJU4cmFkF41NSuj4w7wsv4JXQm2a0x1_lGLgGTVGEniF0vlO6aUPAA81hLTJeHnWetM-4IJuSMacKhcqBzlvoLSHTfuSA8LKVW9tPh93BupcLnFzZDc6yHL5l1pn1-Hy8zqZEkIcxn-c-O9F1xJhDBkb4q-3_--mtFqfWiyNTovW3bM0Zy3Kp_8PXzUwfNqcoQ_mDBc43bZQUT4VdfLgz1oeXf2CUd0lVUg-Ohd3dUrGHL6ZGoS9jJ4mNGUpmMJZkkrtGNphTH6cxeA19BrHUucs-CNNcJxF_Y36_zFQdJg5zAis2bsCZ5lH9xHsYSKVoV1ALWtp-dcxh0MNbX6-TMNpdCrUKnkog__G4IC5ZClUoWQ73qnpzgxddjNw440ESuTYjnQO5LNEtY7k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عروسی، طایفه «آل العرعیر» -  غزه</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6414" target="_blank">📅 18:29 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6412">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U0ayT52lTz2JR-_JXnwd-2-oeIeqt9rrGEd1lzqhXMgAKfvsZCHQhoz-qMpuoXpRa5xaIj0uSUHf0D826E76Frp-RT1TALTMGTyREPNB6XDEhoOhLQR9t98upmWuj5-5Ym32pV3FxoOUcIxfJhdOT-HHcYkX7H_iTFuK06yUNyk_ApydWEMTiqF7xSasMp7qaw22XsIcHEwkIfPzOsdb0TNdFozlrc6bhrhyakXgh6akmBZjlPBUDyhW667jVZlLPGACwKkYNTwBfMor6XQsSVgHGQqz0lHvZM7ZEmTKbSmHTYspIRsObQsOuRHf2t6KPWwDWAK1UY-EI4WHtoz0Vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ltC7pHIUccCMSCqS-pYuRePeYRLNwnOmKIsUfpTkWZkesyPAltFI5_7XzjrMNGYExFwFT7mCQNZPrPVfpP_GWl2qd4N3OJyOKXDwuFSng5j9MkLfv9_X3kwwHnjDW0CTXgYB8DEfSoPGjlr6asEiDM1_bFn18-eXM_DcR5S1dR1nhE7ChR30GmGWuQi8OVLyzvI6b2VmIjEH_uSpb8Ka4aopqlPbNaJv7Kb8PLa__1FQA08LNm6YZCnjdxH0gzvnOW9oQ0FfP8qPqAlyPNIJK9oGe2c0eewzWpD88rihXfHToThmK-9uoxy9qpAXkSsr09eFT36GL4OoKAYaCLx6rQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
رسانه‌های حکومتی از کشته شدن ۴ پاسدار در جریان حملات شب گذشته آمریکا و عربستان به مواضع گروه تروریستی حشدالشعبی در عراق خبر می‌دهند، تصویری که جماران منتشر کرده اما ۵ تابوت را نشان می‌دهد.</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6412" target="_blank">📅 18:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6411">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🚨
وزیر جنگ آمریکا امروز با نتانیاهو (در واشنگتن) دیدار می‌کند.
نزدیکان نتانیاهو دیدار دیروز او با ترامپ را «عالی» توصیف کردند.</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6411" target="_blank">📅 16:10 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6410">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🚨
🚨
ترامپ با اشاره به حمله موشکی شب گذشته ج‌ا به پایگاه آمریکایی در اردن :  ما ایران را به‌شدت هدف قرار خواهیم داد. به‌شدت به آن‌ها حمله می‌کنیم .</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6410" target="_blank">📅 16:08 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6409">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/436236e24c.mp4?token=KbPmPas6cZNRhO5NmG_2z0z27Xph1OF4EAQBK2aInXslYdPg1nmzokAaag-eFiqlKrKdKnW_YFJ1PxFhUzeUnnJjeIoRZN8hmlTu77o6EwCDiv-ADp0BfBBrRyoph_BTa1CUe50KSDv1Y2WGIZbRZowcDUaraAZxhlOD_tiZMEFNiN2bplRAn-fZWv-R0_l53sVW0tV224NcGefgDgP_DzpcLt7TTimAl7ErJ-LYCSfkxTKetVh4RBdD9CEukObaLccNhHQKI5e8LyIoHLH1fVcKahp5YXgY34j-wRfOmrNiw_BxVfpVuwdBcq-uiQKJCsa6Axe5-zxwDPt4SOGLwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/436236e24c.mp4?token=KbPmPas6cZNRhO5NmG_2z0z27Xph1OF4EAQBK2aInXslYdPg1nmzokAaag-eFiqlKrKdKnW_YFJ1PxFhUzeUnnJjeIoRZN8hmlTu77o6EwCDiv-ADp0BfBBrRyoph_BTa1CUe50KSDv1Y2WGIZbRZowcDUaraAZxhlOD_tiZMEFNiN2bplRAn-fZWv-R0_l53sVW0tV224NcGefgDgP_DzpcLt7TTimAl7ErJ-LYCSfkxTKetVh4RBdD9CEukObaLccNhHQKI5e8LyIoHLH1fVcKahp5YXgY34j-wRfOmrNiw_BxVfpVuwdBcq-uiQKJCsa6Axe5-zxwDPt4SOGLwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ترامپ با اشاره به حمله موشکی شب گذشته ج‌ا به پایگاه آمریکایی در اردن :
ما ایران را به‌شدت هدف قرار خواهیم داد. به‌شدت به آن‌ها حمله می‌کنیم .</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6409" target="_blank">📅 15:58 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6408">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
🚨
گروه تروریستی حزب‌الله لبنان با یک پهپاد به یک خودروی نظامی اسرائیلی حمله کرد،
ارتش اسرائیل : بزودی به نقض آتش‌بس حزب‌الله پاسخ می‌دهیم.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6408" target="_blank">📅 15:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6407">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eaa361a599.mp4?token=uGcYaUzt1f5DlPuJd4Vs4kVAkg3pC1lmHVqY57arlOOtF0iypDrv58FhUaAgXes3Og88H-BTTw_6Ee-7ad0piQjas4dfbJOO6rXAwTPEWh1agSosECpA_sppa-euitihRDG8CR8shVOzfqZMNmvPw_lU0d-B6yU8B2mANPiKm0SVK3PSZQiwkfKwj-45Y4gr1MOxSTxfLynT2rq2XHPc7k-OpekmQ5WYNeyLL9-AwXDdmnhilN5vDOw9_lnLWNeVsjJQvT_fVBFEx3OYaqjQ5L2JsxPAl2KFrHYXdH1PwdwCNFNaFWfPBqJK19saSxfSJfkrJiXNni_ttU0-duCtHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eaa361a599.mp4?token=uGcYaUzt1f5DlPuJd4Vs4kVAkg3pC1lmHVqY57arlOOtF0iypDrv58FhUaAgXes3Og88H-BTTw_6Ee-7ad0piQjas4dfbJOO6rXAwTPEWh1agSosECpA_sppa-euitihRDG8CR8shVOzfqZMNmvPw_lU0d-B6yU8B2mANPiKm0SVK3PSZQiwkfKwj-45Y4gr1MOxSTxfLynT2rq2XHPc7k-OpekmQ5WYNeyLL9-AwXDdmnhilN5vDOw9_lnLWNeVsjJQvT_fVBFEx3OYaqjQ5L2JsxPAl2KFrHYXdH1PwdwCNFNaFWfPBqJK19saSxfSJfkrJiXNni_ttU0-duCtHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خاکسپاری اعضای حشدالشعبی در استان دیالی عراق که دیشب توسط آمریکا و عربستان مورد حمله قرار گرفتن</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6407" target="_blank">📅 15:04 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6406">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X6NElynRAq9TeKgbZtTflDge28TJEL8dqvjhw_N_fvKWwCTaFos6mX3knm8uXDCEZ7QCJ8Q0RAgeQ78jCWEPDY3c5GZW154Dsf-oXDvkNR4sY54dPvO_7hq6sVst7uYqrG9CDx8_Sxb6VukNoIQu_Y5czzRrU5TwANAxgvDdy1e3Tqdm8Wre_6Iga2lulrDushn2OuaT8VBJNpCpsvaqxptkUwFxAE4bu3xbA51Tt7Q6brY8wKidd7ft6sIIM0epd7QSBjnoJsntn4u9UOMHK6fGEL6vHx6PN1zVRb3cb7PEwkUX4ecPpBdnJzygRYwv4AaoBvdc7PgKcL_MIdmUdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیروز وزیر دفاع اسرائیل برای اینکه جمهوری اسلامی رو تحقیر کنه گفت که حملات این دو سه هفته اخیر، از خاک اسرائیل انجام شده و جمهوری اسلامی
به همه کشورهای عربی حمله کرد
اما به اسرائیل حمله نکرد!
(یعنی از اسرائیل ترسید و بهش حمله نکرد در عوض بقیه رو زد)</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/6406" target="_blank">📅 15:01 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6405">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CsAIh0VVMYFL7uFS8mxAg5tZLT3wpLoGkmbsFs2MM-RhxU8fVYD5cBm3ZnWOFKb1Aw-4XOeWou1oVrgUiXMCa9722JGArKr6ikKoK89eFXFYzM2xbcpdj9g-mXyI7cmrJw3sWsnzJjNLLxzwDeny_s8_SDAqBVDGHxcM59S9qqN3g-tfA_yOYUzPa2_iUAPK_heKAOyDQyNNUmQ743AYmrWhhAIAid7C9Dz4epWVgFZr7QZChd9rfhBstMpTGcsgb6qBZDiskhWIKs7ZytotEp5yZgshzYBUh7FH4clpVkXODncfP-bHPteqrxtYzgo_qATM-s64SAj6UpRRfifLkQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
صدا و سیما: دقایقی پیش نقطه ای در نوار مرزی پیرانشهر مورد حمله هوایی آمریکا قرار گرفت.</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/6404" target="_blank">📅 14:11 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6403">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9cd7033f96.mp4?token=dXud0Q3DulQ1Zs9gWNkOwknJZssDJrw37xa9L_Jw5_eRfe9jrd91qphrP65k7Ra6Yd_vqTo8KfGOiIpsNr6o6hJ7ewwhlD5wgxuW9OqkY0AI5tCW4okNA1zaC-bzoVHAUQsW6iHUxACdK2fiA2o2b8JE47Wu7WcFvWPeN75oEbDIkkfSgLBb-XgNuqvsbDSf9xM941_kyrBZFNR2Q5Pdi3kwKjqxSc14mjHFAELzIB1ZjKRQzJBIBQhzK-FSgZVadvLD1nhYbypwkktcOMHWMTxTo-ZG2Mjn0VprXfPMbo2M7ICzAmKIOlLycfZMO8w--BuNOdnbubxbrOQNmnFptw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9cd7033f96.mp4?token=dXud0Q3DulQ1Zs9gWNkOwknJZssDJrw37xa9L_Jw5_eRfe9jrd91qphrP65k7Ra6Yd_vqTo8KfGOiIpsNr6o6hJ7ewwhlD5wgxuW9OqkY0AI5tCW4okNA1zaC-bzoVHAUQsW6iHUxACdK2fiA2o2b8JE47Wu7WcFvWPeN75oEbDIkkfSgLBb-XgNuqvsbDSf9xM941_kyrBZFNR2Q5Pdi3kwKjqxSc14mjHFAELzIB1ZjKRQzJBIBQhzK-FSgZVadvLD1nhYbypwkktcOMHWMTxTo-ZG2Mjn0VprXfPMbo2M7ICzAmKIOlLycfZMO8w--BuNOdnbubxbrOQNmnFptw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83ac14cf04.mp4?token=kjCcd6SKdEnc3-X1Wg7hFovH9irXFcp1J-8rRgRQZGovw-qcKt_rV8Ce3yrlrj0QwaMHGTapk_3Ytc4wXarA2ThpIjkZyE3Z-3DuQSlVVA5ah4woLSVoax4XH60lyyjH1EnfW6anBDe_eUUloPBs9l1C4EFABD6wqvBl7RVaiyU1H7Cn36WvDkg0F5TAEzRGi84H3X2ponbRNqwZQuwKrGmWeoOkcZrM3gY90h-nZdIvXm7bIo2_lWZRBjnLX1Bjxsp0RE9F-g3rtKuEYPcN_UWwBFiyBm3W5tVtcf7lWwXUSvZ90JEqTu7UxOW3_hKGQ6BMwRVuAOfdxnDitzKKog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83ac14cf04.mp4?token=kjCcd6SKdEnc3-X1Wg7hFovH9irXFcp1J-8rRgRQZGovw-qcKt_rV8Ce3yrlrj0QwaMHGTapk_3Ytc4wXarA2ThpIjkZyE3Z-3DuQSlVVA5ah4woLSVoax4XH60lyyjH1EnfW6anBDe_eUUloPBs9l1C4EFABD6wqvBl7RVaiyU1H7Cn36WvDkg0F5TAEzRGi84H3X2ponbRNqwZQuwKrGmWeoOkcZrM3gY90h-nZdIvXm7bIo2_lWZRBjnLX1Bjxsp0RE9F-g3rtKuEYPcN_UWwBFiyBm3W5tVtcf7lWwXUSvZ90JEqTu7UxOW3_hKGQ6BMwRVuAOfdxnDitzKKog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خب چرا همون موقع نیومدید از تفاهم نامه دفاع کنید؟  این تجمعات شبانه دست کیه که هم دولت و وزیرخارجه ازش  ناراحته و گلایه داره و هم سپاه!!   کی بهشون یاد میداد که بگن «بزن» «بزن»؟  کی موشک میزد به ۳ تا کشتی در روز و توی خبرگزاری خودش (فارس و تسنیم)  می‌نوشت…</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/6402" target="_blank">📅 11:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6401">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KGpB6h2pquHGH47JSWGlr_q2zKHDGRY9B6-41kSi5bxP9sLSU2vmUs79BJJm2-DDr3HCSflIJx79gZaPzN130GecZiRZwb4l_tr8K2gM8AoZpnDuMOjRfQj6yokpFxSNpKm2t6Ovq7ZdcQIkXqL-U564vdsNdNhzMhqg7AIu6EUk6HY47WAa1Lfaf-EGIOr2PFwUpWaEPCq_2McH7zr9TcALuAk84baiZa40Skxe1yc00IqZLmVqSwZ3QWgDwb23LdrCr1ow_ljucOPQYOAcpLtBJec4LyhWsGT50Tyb1cdmsMoX2Xjk7fp4jMfJVEAE-QNIHUaI1xufjvtNPdEfKg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
سپاه ساعاتی پیش از هدف قرار دادن سه کشتی که قصد عبور از تنگه هرمز را داشتند خبر داد.
همزمان با سفر نتانیاهو به آمریکا
هر روز دارند به کشتی‌ها حمله می‌کنن ولی به اوکراین میگن حمله به کشتی‌ها خلاف موازین بین‌الملل و  حقوق دریاها و آزادی کشتیرانی و … است!</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/6400" target="_blank">📅 09:25 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6399">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FEwfZwkTTDU39-NDnaHRZ2jIg9GU61t69SOAO8Zf1a0hsjeZ_JnQMW6OhhDqpqfR769zzjzP4Q2uY8NhTkbRtgPgVC5sHDBACOX5JErjBersG0yZUOHi1Lr9iOmO2pQ4KnI_c1-ZhOmp8UY4td92TzVF1NzD_MFa6dS2esZTQFFVxIuMQyuMvKDntUSaP7eITtZ6FVd1gUxY8VY9l5ZdnjQoy3jKc-SgZ-4Vjd_66C-eTkBWUWTqwCclDxQh2wbcZjbn0fhGEt6_MqTVTHs9xE89_Pu_Xb_iUwWCQpYRGm3gqePiCn0TZ1OPoT3-yd0ovWXyGu-VcZmQxywWMMq0Bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها دائم میگن اگه جنگ زمینی بشه دیگه قطعا ما پیروزیم!  این تصویری از عراقه و نیروی قدرتمند زمینی ارتش عراق!  نیروی زمینی که پشتیبانی هوایی نداشته باشه وضعش این میشه!  فکر میکنن سرباز آمریکایی قراره مستقیما  بیاد با سربازان ایرانی بجنگه. بالای سر اون سرباز…</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/6399" target="_blank">📅 08:31 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6398">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lg6gjszZvEZ-0eKAST2uNLySJTHiFKrcG8fFHz8d90y0TSyk8zhtYyfmshx7WT-6G9sCArEf0ifo6IEYsKJ-P1jOv8OfXIPx59i0JC0f7tWfcDal49xdXu_v_kMSlU4s9Rqs8Vxn6ksJwkBoOdY28Mk4KGvQN19GoOehpqiS5R0PTg94NfZY0HwixKMGugGDrUyt-XVn7dE5FRPnHnWYo15R1GvXIalHq3Us7JGrNkOigxUTUrK70u9T5LqGdeGEZl03Q6hFNAZwFq3Af13uVxAkoJuaOzlqkirJpdI8gcKOC7GiyDRdzcO_AGnPKc7T_V5RpYOBrmo8fI09ZzF8yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۱- جنگ زمینی چیز بدی نیست! ۲- اینکه جزایر رو بگیرن،  اتفاقی نمی‌افته! جزایر خودمون  رو میزنیم و بعد پس میگیریم!   اینها قبلش میگفتن آمریکا جرات حمله به ج‌ا رو نداره! امروز میگن، حالا جزایر رو بگیره هم مهم نیست! قدم به قدم!</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6398" target="_blank">📅 08:24 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6397">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">۱- جنگ زمینی چیز بدی نیست!
۲- اینکه جزایر رو بگیرن،
اتفاقی نمی‌افته! جزایر خودمون
رو میزنیم و بعد پس میگیریم!
اینها قبلش میگفتن آمریکا جرات حمله به ج‌ا رو نداره! امروز میگن، حالا جزایر رو بگیره هم مهم نیست! قدم به قدم!</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6397" target="_blank">📅 08:19 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6396">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EgbhiXHRvOmKRcTOJ2W4A7NjTQwm9bDHULGzBKpb_gvXqSCJ_T1a5F93A-7wtAAuJ2nY4laZsJIjoVx4h1wG7KuSAthiiD7ij8WrzZRkX-Caaxeu_xJGD2uX0kAVn6b96opfpy4VMBQum82RbggoXRCMeGjSEM5ntHayzGdSRM8j9QzIPwrWVNwhv5ZM9B4x9FuU649RLSQJw8H3J4DzftaCYS1DySyPCdd8huI6KUB4vtD0ZO-Tmpz1pmlu1zFaiNc91-_6MCF4j0KA9evmNlcRYbAAhzx7tU9H_-QaT6MXhWng23OCZTQ9wlmZlmJq2_ngCcZOhuVnRjRfdGJDVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حدود ۱۵۰ میلیون دلار
هم براش هزینه کردن</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6396" target="_blank">📅 21:56 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6392">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VJo2F8fqJA3LVRR5V2rKM2cwRx5zX_diDOn7vOqgLTcPXyRbZfVNkzGW_fjc4P2k0F1P7MpGGZ325I9ROygNTO1EgfTQOgmJ6uN0gRli7PrqAhCMZlT7iVPbq8EjQppXpcejYs7IRlZgHlmwn84iD3ioxw2mNUW933q1yMChMCJWN3E4TziCzRwK-k0jUwfjhxja9vHAP4mtFtIuEosNc91Qd0DQpr_Q0wBl4FqSgNsf4_olhJR1sRBUGwjWqKBlqCPCSkTNNAZO5_UtvYTgxc7q7rAWzRf38trXFlNM3JdioUZr9Au2oSwxuen_71idgy-1tQr7mzdTOFUssMefXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R-YpEj7oDRfC5NVQcJcMecA5HRmzLTbLkHeTMaFxmegHtjwZkyEEhf42Rb30Bah1ccEf_9coKUqzHpV7erYjcEEsCDV-c3US6mVv7avnGjv84aM0455AJCcXZVH76lvG6vzvMJV5pmnCe1M_TuTGfLV2T1rpQGdtmX5Prk48ynKxhLfUPKw9dK44JiZNNRoUqNuU4YtZFUYwq7oCt76AJSjxIYcdtuVlvVR9NOqEAVzdrhRzfR3VYmUCFCHKAOXWsDVx6f8uC_ep4On3rn5ubVjcvkoJecjCUB3O4LclPGPMh0O_rDeaNq2T5jvc3cPK9Svka7UaTOLXEo2-b1x_KQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nZz87ePt0jOgac4dtGwlw8I4qkVOz2KpNxFmrGDyYjP8JHKknXQzmC5VHfUq_2cYJD6JWKYYowadB1tghXaaX7XWFR-RYHvqllnvbf7vwJnHPoMeuHyh6OzCXT1colev9fq7VIE2SyjTj801HbVCKsgnN2DRAcuCZO1pCPOLK-HWqvEXeQkUVPgKvjvkBc87CNVpjFlWqhZ-Aw8gfiTjLs8gvJxH_8RpsTZNnZyhMx882IlU_SwJ7amcLgf_eQ-ytzc_c2_EpQmBM4gZXNDrcnr3AnDlVbuvIoaMQIIA9ibJgHWCyLtBBF73JotyCJ-L3mct0-Ze840cEzH_KIYRsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L4eQ1o54ZFSyyx4eJ_R5WlpJ8EpxYpZ_WV0qipRxK2U1MH1WLM38WsLc6SzlgWwlGqrGndJjDQLTUUA-m2GzFbBPzPoY4egV41sw0dzwir8BoWPaIB7EAk5B2Lrq-KPkh-zqUvY9OayFTENPCkMr-E-dRBrfWRri9vGhuWqt5x0P9TjPCrZ4E6b3uK1dB-7-H7y9Hb-j1pnbAdCLhijQ8etZOdk8heT4WElUFMqhsy6XYszIgjrcz7ZZXxMluGPbAf5FWK6GOc3vdH9kX7KHczP1UM1AMWFSQOW2-ORFbIKs-NeK-Ov4Mv5t1govVE759gnQN1iE5Wb2MIqaugxLuw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تصاویری از ویرانی فرودگاه بوشهر
از این هواپیمای مسافربری تنها دم آن باقی مانده.</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6392" target="_blank">📅 19:06 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6390">
<div class="tg-post-header">📌 پیام #49</div>
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
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6390" target="_blank">📅 15:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6389">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">مراسم خاکسپاری مهدی توکلی، مدیر خانه عکاسان کُردستان، خواهرش سمیه توکلی، روان‌شناس، و مادرشان مریم اصلانی برگزار شد. این سه نفر شامگاه چهارم مرداد در پی تیراندازی نیروهای سپاه پاسداران به خودروی حامل آن‌ها در جاده بانه–مریوان جان باختند. نیروهای سپاه پاسداران…</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6389" target="_blank">📅 14:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6388">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIranwire</strong></div>
<div class="tg-text">مراسم خاکسپاری مهدی توکلی، مدیر خانه عکاسان کُردستان، خواهرش سمیه توکلی، روان‌شناس، و مادرشان مریم اصلانی برگزار شد. این سه نفر شامگاه چهارم مرداد در پی تیراندازی نیروهای سپاه پاسداران به خودروی حامل آن‌ها در جاده بانه–مریوان جان باختند.
نیروهای سپاه پاسداران بدون اخطار یا دستور ایست به سوی خودروی این خانواده شلیک کردند.همچنین پس از این واقعه، از خانواده قربانیان خواسته شده علت جان‌باختن آن‌ها «تصادف» اعلام شود، اما خانواده تاکنون از پذیرش این درخواست خودداری کرده‌اند.
@Farsi_Iranwire</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6388" target="_blank">📅 14:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6387">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C0PHxSeOGR9KB6e48vy9kjxKOqkRFtCLYfuhPH3lc3hw2UINP6Gb1mulPCU7Z8RBktNHmHg5idXhEyH8NFCjJNjiIXxila3KTQ1YVvqC1VMGoB_a0NP25GXj6i86SWGZ-0SvIMxIR6B93hm1nwE2h3Fbv-byqR5jhRQrSF45igvh1ZKPLLMV2VSuZjymev4YQlBUBMKb-gooqel5zGtqIRfDVldfHi61SPqnBDv0ZQ1a5_nWZIOwQcHv75gqmmk_w7RSf9V5g7NVpvxVKLBmTR5luKeDSxi0Iy7vBw8oqJm7XIrreEtmjYLjUoOMN1a6XOBwaanMDRNkxRCmrUuP2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باید آن قدر آن‌ها را زد تا پدرشان را درآورد.</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6387" target="_blank">📅 11:33 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6386">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">‏روایت اردشیر زاهدی از درگذشت محمدرضا شاه</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6386" target="_blank">📅 10:52 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6385">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v4eCS6I87Qd27AM7TQzaEGVsV9dr4XVSHR48xAaSCGa91hPYhsFSlRcfkn-GVKwjKp_Ilq9UUvHZbmMV0bhYY61Gq_Vek67ohRaBmN9Yk7sZ_n5oQUOiiJqZYXSz6WtWXOZmxRElvS2n47t3DcDou33ppN9xjpkW7e3qNYeXNzcz91AVIrtQeg7po4kjSaIQmkmSx5c66KH27m9Mz92Bgv2wkQY4Eul-L9lMSF3VuERCOyaz7vFFtoV5BLzKqhSQ0GJ5m1edErTA33HFyzkB6-TOSzXwrk1SROzwRYCSdRLU8wvdQr9LHv3MMQdy9Y0tWkbvSxVNF0s0E6QSB788_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لعنت به ترامپ که ۶ ماه بیشتر بهش فرصت داد! تا یکی از اقداماتش،
و حاصل دو روز بیشتر عمرش، قتل عام دیماه باشه.</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/6385" target="_blank">📅 10:19 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6383">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/139cdb38ba.mp4?token=ClZ2JZ8M2a6wR75EZQC87SHz6PqgJLwKJENZ2uEFWKNv-drcMDOGdfyf6pG9gzDlZwH2P0Ow8USKoKy-z9H1ej5_S4Q7feiX1DeJruhizrdmxp9exaFeKE7DFda9Bj8BuLAjNhkLiPjmutlYE4I_eLq1qaeguw5ZieOIA0DE7e-DgWlvdZ6LTv9TFDKLUwkfECjIG2OBguBBSU0jxUJqIuxfk0hgHEdHV3b26LpUrQmQA0pDFOn--ixdZFaQ44Ay716QAnIsbbmStexkayQkUvEPbx0I-Jsao0D8E7s-geRkuO2XuY5q93A_k6V4lDjJTx__f8s1PKUtHWQYZ1inmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/139cdb38ba.mp4?token=ClZ2JZ8M2a6wR75EZQC87SHz6PqgJLwKJENZ2uEFWKNv-drcMDOGdfyf6pG9gzDlZwH2P0Ow8USKoKy-z9H1ej5_S4Q7feiX1DeJruhizrdmxp9exaFeKE7DFda9Bj8BuLAjNhkLiPjmutlYE4I_eLq1qaeguw5ZieOIA0DE7e-DgWlvdZ6LTv9TFDKLUwkfECjIG2OBguBBSU0jxUJqIuxfk0hgHEdHV3b26LpUrQmQA0pDFOn--ixdZFaQ44Ay716QAnIsbbmStexkayQkUvEPbx0I-Jsao0D8E7s-geRkuO2XuY5q93A_k6V4lDjJTx__f8s1PKUtHWQYZ1inmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همزمان با اذان صبح،
دو جوان رو در اصفهان و در ملا عام
اعدام کردند!
ابوالفضل سپاهی و امیرحسین صفری.
مردمی که تجمع کرده بودند به
حکومت جنایتکار جمهوری اسلامی
اعتراض کردند و درگیری‌هایی میان مردم
و نیروهای سرکوبگر رخ داد.</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6383" target="_blank">📅 08:31 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6382">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9dfafddcc2.mp4?token=Xv-nRrYtrCd2Z4sRx8WCUP1kjkzkEEgQbQDNbOZKHdqIRhbwIPfKOdw9GPKWExKDai_z5NKKS9lMT2BCXJshng0N3nJqFwdQOO5bAoaeLbVDji5feLmDoSvI6-vn73aE0c6hnVhfUAVgj0bghisIpqb70Hmn68QnWs_0kUEDPOMY25hZl67tOSVSTh_3uUcV2Jgy_IIPQ26B_XqCLsrDjzRFAcyJsHEbul8K8w0tOYJRe4iP4AbwLAbWSmGLFyM34bxlTDwAUin_7rsH45DMaJbLK_uSrClGzo1wYCs5K40b9qzF8rYf3hffZxAfHM4ONfnsLXxylhTKk0xmL5iqXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9dfafddcc2.mp4?token=Xv-nRrYtrCd2Z4sRx8WCUP1kjkzkEEgQbQDNbOZKHdqIRhbwIPfKOdw9GPKWExKDai_z5NKKS9lMT2BCXJshng0N3nJqFwdQOO5bAoaeLbVDji5feLmDoSvI6-vn73aE0c6hnVhfUAVgj0bghisIpqb70Hmn68QnWs_0kUEDPOMY25hZl67tOSVSTh_3uUcV2Jgy_IIPQ26B_XqCLsrDjzRFAcyJsHEbul8K8w0tOYJRe4iP4AbwLAbWSmGLFyM34bxlTDwAUin_7rsH45DMaJbLK_uSrClGzo1wYCs5K40b9qzF8rYf3hffZxAfHM4ONfnsLXxylhTKk0xmL5iqXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آرزوهای خامنه‌ای : جوان‌های ما تا ۲۰ سال دیگه همه باید عربی بدانند.
https://x.com/farahmandalipur/status/2081803094522757301?s=46</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6382" target="_blank">📅 21:35 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6381">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">جاویدنام مجید پوررستمی - قرچک
۱۸ دیماه ۱۴۰۴
قلب آدم هزار پاره میشه</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6381" target="_blank">📅 21:22 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6380">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">ترامپ به شبکه ۱۲ اسرائیل: «در حال انجام مذاکرات عمیق با ایران هستیم. اگر موفق نشوند، به اقدام نظامی قدرتمند بازخواهیم گشت.»</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6380" target="_blank">📅 18:39 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6379">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ed1a3118c.mp4?token=QTBGz0ko_SPYj9urKBavq4pkoi0tMD7n2wCc6WknGgDdarvg7H9wD-riSVzkaUDbJUXfz5RmiKN9nttMTwpMjZYJExZdHmdzRcPlUd0HjWDrC7jfBQWgRj5j22yA-yQAp29iQOyzm4PmgLOUVC3ZlgpiICUrwgPxlsc1m3KsEcB6elzV-7iG0GT02wX1fOBsmz5TpgJ6kkdHHfczzBF8JeZPkuQGgh68ZwBdY6dN7S7yeqrg7CChCxbjH3qMgK6FRhuOplgSv2nQzfkK4hELMqFO4ZqLEfSqf1v9h2HnSiWVUXq9P1Sf12Eg5ef7vDXBLamKa4SKsMFFZcIQrqfvNwD27AxHEQUpRxGU-UUmyRHmQh357EzovwxRpYK7PYV9lK4zrna4GzX9jYaGIUsoomr82BHcNyascVwczrORJGpDVMJnRS1DvGkz_khllzSAaXuWn1pxlJUKz4lz9MSvzOH18_f5oXSOHt4Qwk9uugB7YgYRdBntt2kg5VewmP9J7tWDqOhrllg9FFe-FC1cAWBO8yV2Pr8BipA2CCigVu-yDroC6Qu3Deq9re4la67Jkedr0SwEXBKXV5PADMpKvtGy6Y7t_7F1PuTadyVNSXKdxDPWvjRiFYcgAA7FXyvKj2Rj1mifLC6lGYlX3GUdFsLTVjzTWvubo_ODC1QCP-o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ed1a3118c.mp4?token=QTBGz0ko_SPYj9urKBavq4pkoi0tMD7n2wCc6WknGgDdarvg7H9wD-riSVzkaUDbJUXfz5RmiKN9nttMTwpMjZYJExZdHmdzRcPlUd0HjWDrC7jfBQWgRj5j22yA-yQAp29iQOyzm4PmgLOUVC3ZlgpiICUrwgPxlsc1m3KsEcB6elzV-7iG0GT02wX1fOBsmz5TpgJ6kkdHHfczzBF8JeZPkuQGgh68ZwBdY6dN7S7yeqrg7CChCxbjH3qMgK6FRhuOplgSv2nQzfkK4hELMqFO4ZqLEfSqf1v9h2HnSiWVUXq9P1Sf12Eg5ef7vDXBLamKa4SKsMFFZcIQrqfvNwD27AxHEQUpRxGU-UUmyRHmQh357EzovwxRpYK7PYV9lK4zrna4GzX9jYaGIUsoomr82BHcNyascVwczrORJGpDVMJnRS1DvGkz_khllzSAaXuWn1pxlJUKz4lz9MSvzOH18_f5oXSOHt4Qwk9uugB7YgYRdBntt2kg5VewmP9J7tWDqOhrllg9FFe-FC1cAWBO8yV2Pr8BipA2CCigVu-yDroC6Qu3Deq9re4la67Jkedr0SwEXBKXV5PADMpKvtGy6Y7t_7F1PuTadyVNSXKdxDPWvjRiFYcgAA7FXyvKj2Rj1mifLC6lGYlX3GUdFsLTVjzTWvubo_ODC1QCP-o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/6379" target="_blank">📅 11:22 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6378">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SzTGX10nEir45T9cd1Ju1vQCb3qUgMhl3XheK0U_p-9duuXSALqMGfEFe0KMW6dCutCyB2lnz7n0L2mnvrS0lzS24z0UlWlfAYY8894uXROwC2FZF6QFFGyyewBU4f6LmzFXAqcgCiQXF7xTCNmL7p-1T0_6t30e3IJWCjUocnqekzetYG60b98h5C2on0wTH8L1TiaAWb1vPXQbvNdBlI060v9Hs3gpEbxwLh-Cf8VpgeZSG1pRN1hripLykl4H9NkOCp7UJHHcblDwzgLg_KiKz8hiXaQ43E-R3hrIjbnF3FuM0VLURM6e1OLezIpHMBM74RRek6Vo9yQcSdTGAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نتانیاهو راهی آمریکا شد</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6378" target="_blank">📅 10:02 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6377">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af3c95e2d9.mp4?token=qZZsn_Xs9HentBhsIlb3FfF18n7xG93DhC4Val8NVWRVlfZvF41mN4NzAdpOS9YJL7TfwGTDa5KyTJhOVpje2MDD8ys6cSJjIPTGFyhfFDjhLDez5LWIoppHaotiNKfxsj4v7HJWThZ4hEmgLiY4uiz0d6-37zWPqyrokZu0Xzp7rfe29cQBwVINE5-TlVILJngdwZrfwAaqkYVP_QuEsozu_fM2Z2SaJDETRhqsT5sLbbGjq3KFIJAiU8tr6ARuoTzve02ZTtRJlj03WceXSGgtzctGFQTbL8HkXwvME8-BnasG6tecnPc9yL_PueMEk-PTzfVjWhhTDqxiDUG7qA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af3c95e2d9.mp4?token=qZZsn_Xs9HentBhsIlb3FfF18n7xG93DhC4Val8NVWRVlfZvF41mN4NzAdpOS9YJL7TfwGTDa5KyTJhOVpje2MDD8ys6cSJjIPTGFyhfFDjhLDez5LWIoppHaotiNKfxsj4v7HJWThZ4hEmgLiY4uiz0d6-37zWPqyrokZu0Xzp7rfe29cQBwVINE5-TlVILJngdwZrfwAaqkYVP_QuEsozu_fM2Z2SaJDETRhqsT5sLbbGjq3KFIJAiU8tr6ARuoTzve02ZTtRJlj03WceXSGgtzctGFQTbL8HkXwvME8-BnasG6tecnPc9yL_PueMEk-PTzfVjWhhTDqxiDUG7qA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله یک پهپاد سپاه به یک کشتی در تنگه هرمز</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6377" target="_blank">📅 09:59 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6376">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wkii5AkH4oAAyEVf6dmosOSHctWJ3-DdClcJuyoWHmJf2vGgiWYTsCjLP5a6ZWaytfn9uln8RDd_833WCnppDoTezqVoJG-xcIpZnUJu3cBqf7v5C82hFlC7KpXJ_lL3k4qXWJCXXsVCq7ec2ThI82dFz37yHM8qOtD-t1KHpYzNuIQD2-_oPWDREZS2QHuuzJikEZgUptOOEsV--Dy2JSeLIP0fhibM5yqui80xhkgnYVUgdorRaqYrmsWZDakQnwZyLNCscOcTnnmGATgGhO3zKS2YTIW4l87tpTQ8zCm2PYFwHOnzlp103mIW_vglXTrfLu5ht0EZjCdMZwuPEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«مسیر ناامن»
منظورشون آب‌های ساحلی عمانه
چون از مسیر ناامن میرن، با موشک بهشون میزنن :)</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6376" target="_blank">📅 08:45 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6375">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">۷۰ سال داستان دلار و تومان</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6375" target="_blank">📅 08:42 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6374">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UJ1KSOBgPQB4v7M9v-tV0KmQwRMfZQVLcuh0XoXJtpd072-MSbssrJmeAfymCd3G8ORmuTRu5g4LTbRun1HmVHp3Hcm4_ynyxCW9D9yyo7FUR6T_nSr9xw3ffNHXo_uME5MxJ9ephs7hexyuceh3GwEgXkQfuy0_xiPb5wVOjQCbD8CF4uY9qjeh9Mic82yTVq_tBomxMnG8ZoJRPOeFECbzIv3CaLY6pUkmtGn1s-VbgGQwMxR4t9IRj15HNdAByfU8Dzpoh4uZt3uXxfMEpXOtsF2gmpa3oN5hkb6knISv4X9AIfIstc3Xg4Z6PHqiWsnkQj6uTTxCxe84IYnktw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نشسته هی طرح میزنه و منتشر میکنه :)</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6374" target="_blank">📅 00:29 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6371">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CQrEeLUBIAc5etM51f7XuVaoa7j8UkI43b8_iobdQwjndjNKE7LOTxyNUL676tOAjZf3yrcZMvfTQes8RzdtFlHZ9rVChI3sB-3MMw5NPjiXp7Nw_7NzlC8Ir1X9PlqkPJeA4DHLZ7Jl9eANR2xsAatKE2DtC5k0fVBFbFQT23AEtgZrFn0JHyBP0Ge0pGw4gyBHLkGVUz1_uPOSPzL2gM0G8SwuPdOvEefSLMldEGNI_np0zICzwUfctvYe6NaVtaXEyvS_aacbzbfrNej22Ent4GFjPNZNT3xJSZdl15bPxiVuySlzRN4Lvrd3tRbe6bJiSzVNWOQQh_KAhj0O-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IUOIa9vJl9srQx-MG7FBdLNauB5ZIQCck4TsY444xM-coBu0lX248wRtSCn-GLFuV5lY6x9KQREDYc98uRtfkaGavicKb7eOY_dU3vTdeyURLHNhdKNjLVDnafWqH2YrDwmEosIm_EiKmb1Advp2e--gul8gQT93lQDp25Yecezv2LirVGfHhdAGM3hqdUMjIqaTvYIj2bC7pOi3AwE95VOJrcCLMPh1vnCTh2MGHFUpiGaLvzFBZ8gb_hNXMQtsDyCLeYvwLQkk7vqlhopAWg7kL_eNrzF5JQ436PyYcvvQSHniZ3VmpJFNXTJ4oPGmWFFfQkuJ3Bkb0yRqdFwGaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JECcugfPrUST8ZQS0c_18DA3rpN1qTpnnT7ymBPq6z04kQHrfVMWj_lV9UVvz8g4UQcMuzfupxGNVcPiZGX2-cAhd35x-pyKEe25nXL4tqNEWEd4oZtb8crcJlu9NmHXkelkEspKk2gD8_wQksrctZAU8gtrhgTCSAZIr5EWR520AC_tme0voKXbpJj_0p1Co7NIPJeelipaHCDO0-baDOUkx_J48utU7fwVeMUl8LPXA_eE-gd30-d5qdFFOLb4s3uTClDQuQ2RFlG19P0MI8-hDabZ6WYLCQLN2oV2H53eg-KhLSfw7vjyw3Fv4yFDLyCrDO7sE9ADnrYQQRXx7Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">طرح‌هایی که ترامپ با هوش مصنوعی درست کرده :)
حمله به خارک و تصرف نفتکش و… رو :)</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6371" target="_blank">📅 23:46 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6370">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JgX1T81JspNXVguUpqidiVl3pZgEXR37VbbTkYj_TcHauJgLxWwQ-xJ5VEnIEv8Q0esnEwNh8KW6r7zVU8F3QEbNb9NG_sHI32flV0BC91gj4BDUDT_BwLBit3hYRoQqjIA-SMm14FHfub2Oe_BIaZZQf_3i4SMdJS3LiAn8wKxDSFUwTiWN3MmqXeogR_vpQVnX_9gwa30uK2uzUtZW7xubKm2mLc7lROe4SOa7SxO3uCwdo-FwLqlGeLi-1ze3WfdV-OWL9oyS4MXUBkNiEOuoS3yre3H9g9V-mZo7x-g0BUdd_kS82mf3nI6HQnYXu8pVAftFPg2zKm8-_yCznQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نامه منتسب به مجتبی خامنه‌ای :
در برابر آمریکا و اسرائیل راهی
جز مقاومت نمانده.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6370" target="_blank">📅 21:20 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6366">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XWj5NPtUndWRyG53CIK9VBMP_mjbjoJqg3dIxNqzKk9WIW8ElfO2qSvsPzG_j7t70fbT5LEQiFR9ifEaRQwsSBmKi2kQGx325fK2PDfkJtO0Wdu8_EmVXhf296QtvwJ-rDC-cEd4PYAtNIHoQFXaudk4pt531HtRY0KAf_iKAFIG2oH-s64q0fNaIj6j2XMdR9s3Tao6DF5pYFke1mjjhiFRyt7DIM2Zhp_4rKsrMugUtCkh_VppzdKK3GXqeIisVkM6fpEq-Bp9xZxyc9AlFljRKHn_tzZwVaeN6jNSVtI1DWoHSBxQLhs7XsvFpvFoOOA8UBs3fV-CL7l85FgKGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mjJIT22cUU6_0KBO9i7H7A7XNwbof-nwsiz3As8feHOyzzcth22Iq9brJjaDJLTrPSQO82vkcWgw1ewXtKmXgjAc45qMFA1fvjesUVShnpB5O0umdrGS2NlNs7zLoOoRsis4nF95dGcj28XNEZANMaAtNctLLLcazEdpwsl-FbZRAt_gkML7w-DSMgxOFy9RCZtf09xiCgf45yykDKKU9cqd6Z9HlJ1jIGcuI_78ZjRR2aoo4gZ50LogQsTXEdINLmuUzSCSkDWYKJ6o66pW54plJp0_X57IKhMWkBkZocfXFH2k_dzKyFxbXOhUt2g-E_8mHNNSecRR1E8uZQD3aA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ixogtOOh2f-LE2SyOuAIk6W6pqdS0YDTaThgLAR6ecNQXIxHWWIIoJcY8APjks7V50sWcOVSXcmb-LpGE1WyYvXS7sF-dVURxLFcHC521r_qlcXqiWXrMbq7DEbAv95w7j-iXiXBbMuGua3I8_veP6zpWuLSqK7VLThYIMfuwzLNWkTw5sjmqM_KhpvJilsnai281YV5Z5Rz1OXK98s51xwNOnji5sx0ubXTUUZSdTxUYebKBJC6soA3CYBACVPL5U3fFB-3mmMyE0g9tJ2eBnHMwAtCgjgM9Z-gkSxG7mb336_mobzXTz5hNTyjbJYzNv89XTXb-4WC1eRLpxbdMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QujBgpMt3Gps8wCO6k0BOjqVbA1du6HSlfIXlCyRHB_VK-rS39x5L9bhE9_UcDA6hpLnMlHvovcHkKjVo5RKaznfd5KBhE8y-VfWUyREWfvvBqydB1OSHnjtlRHYtoOsYXCVLuqFM_hmrwkXGyg8yWo4OieOcQDw8zi01B_Q1isgbgCyMDeUevrjsViejGi1v12oqpOuGpnGD-3s9O_pnbcCQLgCn1i_2M8T3TxE5BCuVqPRraN7fc9vQqM3JOTvgvdKiSkPw1YaWBbplshWFOSL91hHvZXGdmSPDpG2m5pvikiOxMsCZJc6g8ZWdZz2EPkk8cYstIjrVJgDj61QmQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">جنگ اوکراین
تا دیروز افتخار میکردن
امروز نوبت انکاره</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6366" target="_blank">📅 20:37 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6365">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">۱۱ سال پیش
خامنه‌ای با غرور و تکبر از مسلح کردن غزه میگه و اینکه باید کرانه باختری رو هم مسلح کرد.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6365" target="_blank">📅 20:04 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6364">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L3Zt5IHHrJO1EXQmxdEIlsn2lTxui0Z54mOLsMjp4ByByCQ3R4_fXC-7B74zM3q9OTOs6U8hb9HjsUMUIBluiBCmv1mK0rxj39RMDNgQHTh6D6mao0ApiIQjZEkFhRSjvtRhd5Uvv7o7hpZsFMTDSkQQD59YAp2o_AMSnFaNGslS9GQ2MGPjEVQ7J_N_MkBnzlFQkCx6iMV9GKtFRyMeuupNo9MeyLkG2v8MAJWsrkXGvb1L6bEXi3D8Z0vP2bj4K_Ad4IySt_tbavrWtO2orCCMEuu1ORP3oV6kjv9aJif6wc4nLPJoXaD5CDBkw8RdUTfOMHs-XMDk0fwJUFiBNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6364" target="_blank">📅 17:37 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6363">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o2PZP_mIiuscIBpHJJ6n7rV0Q6Q6LlY-yE9tjWCmgG4imw7CeO8x_nKvCcZapAV6zhWL8xYXc0TiZaxD8OxShlwzPXy-cbihPnqpE4YNh-qhTaBsolt9GVlHIaX5pJR56QnD2ctb67AX_QckN4Emp1p_ywJG2JpJ-qU6il-YmpWjdYg2nIdJsPzB2wk_y2MrvZRbt4R6yADJnbZkAkpuKrbuL2ug1e7dPh30J4UVZfI8SCD8bwpJKeCN4H00Ds6lQdmUo9Dt2XhMd-JUv9QGs0lwrcQYh_jaimQYWSa7ZxJRMuIw3U8AOXb5VpNHchC8BzMXFlMsgDMQ4N0Jnux63g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه‌های حکومتی از برخورد یک کشتی با مین در تنگه هرمز و وقوع انفجار خبر دادند.
مین گذاری توسط ج‌ا انجام شده بود.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6363" target="_blank">📅 16:19 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6361">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VDIXQOgnMbBry3woVm_R8JT4pPM33BpHKOSFjWjJgATlPC299Vid96j2pQtCUpkkUBpWA-M7U0Ts65lHXc8ILkSOXDyKkgy9ZuPAyPO0Jo4I7hJwQ3quKyL2MQ1rZM2ZsWPUZ229cyYKKCztcWMmPmWpRKLZfF07rDIwIoG9dhLttWVcnKtWYgKeO-6huC1jNWmHGBDvCQtqZpfKRG9YQHad3vCTmoEE00npZxTegZaxG6QuNk1k0sxppN0SapNy_c70NeA6v4EVndz4eQZdNnvK57UEGSQVH97s2NlPaIiN_nuzusPwrwE3o6JFPXLMUrIPUUPwlOqJgJ4hT28g0g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #26</div>
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
<div class="tg-post-header">📌 پیام #25</div>
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
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/baosDHCh63nuE7XqfkdVB5tRu5sbYJlUj7HZsLz7k0Mk2sUM2ClbRrRx114UVhcS9qIvELdLqyusTUVT9CbYeAjPSStGE0YlofFeoK22_vtDYvnEtfiI-JrgDASaqX3YlAGsOscp9FX2D_13EsbdTs1R2wj2TfVq9ZO-MuOXQyOjs1Nx-7G4e-NPUN7ztsC-O-Mo_1sPXJ-mVqNdvclBaXfyN1sMLLpSBL658iMdMOUKTEiYvclDa1eK_RQcNqSb2tFU4XDiLLjtGO6XghaASC8djxWPP6lmt3EROnhVo-VDPPb6NsH3IQmO6IFUn2bMZxX_cWzmNSvyUJyu7JkU4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u0eFF7Q12AHRYliTIZza1HuoNW_R01E6fWxRLK0lTDmU2HSMFlrRWNexySNQ5BnntTAsIAqQkQkNmMT0qt-99xXIGCPV0v2j2Ec8i67kCTHbVh0K2Z2CrcwF5u24kXxIsOR5npjLrvME2i0WI4SCo6t53LpS8SqjLqHVr3EzEwikE6vJu0Z1OxflYnVGtRF74aOQqhP0YUPqAnqe0aNj7-zJX36zbCgEqDczpzRSriDGmRvnuRv25X0jgpBcoEzuJAplcvD4lgvnf2gt7XU-GHBSzW6_241JGkrgrUBPO9AD8mOIBc0c-rM3PKa5jx1JBQf-zNY71jOMhqTx1EjkOA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">ثابتی میگه تنگه هرمز رو بگیریم‌ (که بخشی اش متعلق به عمانه) بعد بقیه کشورها از جمله عربستان رو هم مجبور کنیم از همین تنگه عبور کنه و اجبارا به ما پول بده.
(عربستان سواحل دریای سرخ رو هم داره و بدون نیاز به تنگه هرمز می‌تونه نفتش رو صادر کنه، ثابتی میگه:
۱- تنگه رو بگیریم
۲- عربستان رو مجبور کنیم که از اون بنادرش استفاده نکنه، فقط از هرمز استفاده کنه و به ما پول بده)
شهریاری میگه خدا رحم کرد شماها قدرت آمریکا رو ندارید.</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6356" target="_blank">📅 00:19 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6355">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">‏وزارت خارجه جمهوری اسلامی اعلام کرد حمله اوکراین به یک شناور ایرانی در دریای خزر در بامداد شنبه، موجب انفجار کشتی و کشته شدن یک نفر و مجروح شدن یک نفر دیگر شد.
‏همچنین این وزارتخانه افزود،  این اقدام اکراین میتواند آتش جنگ را شعله ورتر کند.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6355" target="_blank">📅 22:31 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6354">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">‏ترامپ در گفتگوی تلفنی با شبکه فرانسوی LCI:
‏«اگر از جمهوری اسلامی ۱۰۰ درصد آنچه را که می‌خواهیم دریافت نکنیم، قطعاً بازگشت کامل به درگیری‌های نظامی را مدنظر قرار خواهم داد.»</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6354" target="_blank">📅 22:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6353">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jLGvbYsp7aG0X7TYdMBMYxGz6Rqoh8O-m2rHwDFaJaYmhsGFIZqhjzQI_wLFerf64komGM_wb5dD-LqaFS-tv0KCJmoBvUTaIXAIcK897KU8A2Y70bySoXF1mgX3_DzeVAWsMe3ZQMXAeHjPtKX5iBF0bC5pbkp34YbMQZjuR374mkVzIf6waQGhIbO6g0lTnO8dFc0YPYTdNGK6Fcs3dE9-XhSeCgIQ2lBgZV7WamBbIYjH8SDLoilbLYmcGLtlJiY8HJgNzxYYGxPoy2n0chnDVmurqduUYn9oy6uVEmcrxSl1p9k3OE02qIR5Apz6mp8DH9CVkdKiUMS-XPLpvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اجابت دعای هر روز مردمه</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/6353" target="_blank">📅 16:29 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6352">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">‏فرمانده سابق سپاه:
جمهوری اسلامی و انصارالله (حوثی‌ها)  دیگر وارد چرخه جنگ، آتش‌بس و مذاکره نمی‌شوند.
‏حسین کنعانی‌مقدم، از فرماندهان پیشین سپاه پاسداران، گفت که‌جمهوری اسلامی و انصارالله یمن دیگر وارد چرخه «جنگ، آتش‌بس و مذاکره» نخواهند شد و این الگو، به گفته او، کارایی خود را از دست داده است.
حوثی‌ها دقایقی پیش نیز اعلام کردند که به تاسیسات نفتی عربستان حمله کرده‌اند.</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6352" target="_blank">📅 16:07 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6351">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad32a14512.mp4?token=iRHRGPuV710JP-239ZkoUQcEoRoK-jfhiUq6k1NXILU832geicP1rEBN3AoqBsINzs0ZLWZssdedQnLU1ua-P7Z7rY9oW3UfJb0hlIAhV5kWwWMjFKrudY4luFfFVqa70LdF06IX4AO5PhySp-q4Rk2nnUBUPupJ5HfE-v4Nm-9a9RT2wVg97XN_OprIN52srWhYs6pyRwwqKb5gN1Rk3J5dWKuHbBkf4pTW8ZlsEzMUHn4HfINPNBpUmqbogVuIjL0AQ7CyBV8-unSkbJCdgQLI28gXgwJtzHKw5woraRKayaIJ3T4etr5Kfh_5wuHq28-3MkRgxS0o_Rk1nHkNcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad32a14512.mp4?token=iRHRGPuV710JP-239ZkoUQcEoRoK-jfhiUq6k1NXILU832geicP1rEBN3AoqBsINzs0ZLWZssdedQnLU1ua-P7Z7rY9oW3UfJb0hlIAhV5kWwWMjFKrudY4luFfFVqa70LdF06IX4AO5PhySp-q4Rk2nnUBUPupJ5HfE-v4Nm-9a9RT2wVg97XN_OprIN52srWhYs6pyRwwqKb5gN1Rk3J5dWKuHbBkf4pTW8ZlsEzMUHn4HfINPNBpUmqbogVuIjL0AQ7CyBV8-unSkbJCdgQLI28gXgwJtzHKw5woraRKayaIJ3T4etr5Kfh_5wuHq28-3MkRgxS0o_Rk1nHkNcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y8vTg78YDa77mXO12Wyq9iNHyII_PVUza8XTT0XMBrfGcDvvWNbT6VdGU38tSeLi9yzY8JqphJ0gZj4Vhb5AAaV3WIPV65pYGlGkdAzlidrDxSJXxpXxk7RpaEmMfXsreyrKxjV6Fc2dl_G1yk_9IO44apWI5Egn2IJSViseNFn4fxwDhgRvQSzy96uunoX45RbbD4SetJGXmgZuAgLRIGdVlalnCC2ioWR-cIwVCI9B2SmW00eXQ_IjZ3Fa5hdigaMh8qEfntA-CO7uKUGkTgtN1lrydlNvLVzxyEDetEourhH8ikNoZz2ot3c2ZIlqppAKwF8iasVihVgIprgQCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازرگان می‌گفت ما شب می‌شینیم با اعضای ارشد حزب جمهوری اسلامی مذاکره می‌کنیم، در نهایت به یک توافقی در خصوص سیاست خارجه و….. میرسیم فرداش می‌بینم  در «روزنامه جمهوری اسلامی» و صدا و سیما کلی به ما فحش داده که اینها خائن هستن و…..!  بهشون میگیم مگه ما این تصمیم…</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6350" target="_blank">📅 11:37 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6349">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lHIpfBX-4dMeYppLqGmy0nQeD90gVyP8pBD5We8bPRBZZkY8xVXmh5zlVnOFf1r4kl2NqppGm9f0YyAK1Emu_nIWJfer3RuG05tVcR3fdpaWB3meZyEMboRYMcoJyJQBgB6Sn4MUOKURmS_NpJqBoOe2ZNxkQv8Oy-LFjYHmRmzE8fofj6r9lONZvFHTIeV4ainbqE-1AF9uTzOduRCXK4WsNokb1tK5Q5HqSRA7-3PcpQvXAqItmkF1rFeSYKaSNqUWmZFqUfA6H0XUiIVLn7TemW1ElmtpVye5KHooXQjBeOR84sSqy3p4K_B_yDo_ac0rHr5VJKFvrbbTMDFHCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خمینی بعد از انقلاب سریعا بر دو چیز  اعمال کنترل انحصاری کرد!  یکی کلید زندان و در اختیار داشتن تازیانه و دوم: منبر و رسانه!  تا اینطور بتونه به راحتی صدای دیگران رو خفه کنه و روایت خودش از هر جریانی  رو جا بندازه، رقیب رو از حق‌ دفاع از خودش محروم کنه، مردم…</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6349" target="_blank">📅 11:23 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6348">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kOK3CsPoqd8PtKYufCCEZznFRxvcfrTiO9UOqtOko9Of5Cc0xH_RsNeUkSJoPoJR9lPHBmclyH3SuA_z6NuwznsyZrx6wKgB7HBWqO0mWpf8McKp2w7XNQ_gC8FQPsAurG7Eu27KEDjv2PB26pBmFOa8at35TXtDkBNDerEar7CSoRQUpZ7TFIl-gmcDkqSS4hu82oMjCqqoBbL3lggIewRA9tOjyIH4ishICvIRxoqEODxaGmqaPay2nfPVmrfz2w39WI8NbEHJlUGgZM-5IiKQ9mGs7aWGGbwAQmXY4gfjDKfugPvNlpEJSRtjrtoBdqO-baL6HCB9ahxWawbIFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو روز پیش صدا و سیما،  بخشی از سخنان پزشکیان رو سانسور کرد!  اونجایی که اشاره کرد که خامنه‌ای در نهایت  طرفدار مذاکره شد و کوتاه اومد!  وزیر خارجه‌اش ، عراقچی، اعتراض میکنه که صدا و سیما مطالبش رو درست پوشش نمیده! و میگه یک گروهی خط می‌دن به سخنرانان و مداحان…</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/6348" target="_blank">📅 11:21 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6347">
<div class="tg-post-header">📌 پیام #14</div>
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
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0dc31ec63d.mp4?token=f-veZkG5a-HmV3B4pdUp1QOB78nTnG9tB2wIDqqO-UHowBKtCkzbKXCbRBEvx6s33mQ64j5X-vogJRF41NoRaE1Y7VCkX-zqGiWvVN9kpK8WiW8h1VaZHqt4Y0Uil8m88yAW2fhfMO8IdWjlDshXB9d2X7ERc0WZBCZSgKLRaWXhU0xBiUaJlXHUHVCFMt0WHR_tT-aTtbiEoSF-fQDbgZ8HJbHRTtbPEeDMm118oC3tgjd0BtiLNk2_nMzs-yaVdMZUK-DoszThX5HU0CWMNJwtPrp5EFdhUycM6LguR-XntLLdpXLNVw2ED4b3kolgUbXx0HTvI-GIFecFPjELPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dc31ec63d.mp4?token=f-veZkG5a-HmV3B4pdUp1QOB78nTnG9tB2wIDqqO-UHowBKtCkzbKXCbRBEvx6s33mQ64j5X-vogJRF41NoRaE1Y7VCkX-zqGiWvVN9kpK8WiW8h1VaZHqt4Y0Uil8m88yAW2fhfMO8IdWjlDshXB9d2X7ERc0WZBCZSgKLRaWXhU0xBiUaJlXHUHVCFMt0WHR_tT-aTtbiEoSF-fQDbgZ8HJbHRTtbPEeDMm118oC3tgjd0BtiLNk2_nMzs-yaVdMZUK-DoszThX5HU0CWMNJwtPrp5EFdhUycM6LguR-XntLLdpXLNVw2ED4b3kolgUbXx0HTvI-GIFecFPjELPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجری : در برجام ما به تعهدات
عمل کردیم اما اونها عمل نکردند!
عراقچی : ما هم عمل نکردیم که!</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6346" target="_blank">📅 11:03 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6345">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UBmmJzP5igKL5bLzvxmu4YIRgod4-rl6P8LOFwAuah0aRlx-BxJ6QU5XZ4wLEBTUPxPkTgdZFQgHcCyL91Nfs5RbTLKGdL1qMyanMkpUi-2N5al8zM1BcdQx2HK0-6UacOe5Zt0Fhdzu-pMamxB4znM0_kgiM3WTE-0alsKzHQtAlIOHTXaevGKo3Xe-V-eEaDeVF_341Q1RNXlyQ32hyNoiYuM6mmdCof6H2wfcm5OmmFJBfBxkRiAmxQGZYu3iuL89MHzo98HmL2FvAU4pQV3TC-wccbuq6UH8Ew6YscK9S8NdiXnDW7p3b8wIf9U1jZgfhYYW-zn-qQezHTlrLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ‌ «در دوره من رژیمی که زمانی قدرتمند و هراس‌انگیز بود، رهبرانش کنار گذاشته شد.»</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6345" target="_blank">📅 09:03 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6344">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2f4e943e0.mp4?token=ifEwlbBZu7rDqbM_9JGYE3ZCgG2JGqwSNsb_XlsNvLC1XjFpdGWsNq8W2jGE2wHhkZTKBL2Jn9sRg2UPmPYKdtxcJlrL3eQ-x4Uj_FDo66Y7zd8HzW7XJ56XeNfPYZgJnhSYdhfTmPGm4ddy6ZxJrYD_OhcPqbCaOrAVyDR8ycM2sPGhduPB-zizocb9-EjCojVhMhJsRkmwgh3bRRy1cKy7u9-s_8nqIv8V79nKJjTBjFFb65etOzOQ10SlzLPmcPfbHsiP7kf7pxgois7ZuV0ldg4xp0tCikUvnoYdkUKl3MITPVa-FaUFsJbe0BCj5S_X2d7z8dqk4nzhbR1imQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2f4e943e0.mp4?token=ifEwlbBZu7rDqbM_9JGYE3ZCgG2JGqwSNsb_XlsNvLC1XjFpdGWsNq8W2jGE2wHhkZTKBL2Jn9sRg2UPmPYKdtxcJlrL3eQ-x4Uj_FDo66Y7zd8HzW7XJ56XeNfPYZgJnhSYdhfTmPGm4ddy6ZxJrYD_OhcPqbCaOrAVyDR8ycM2sPGhduPB-zizocb9-EjCojVhMhJsRkmwgh3bRRy1cKy7u9-s_8nqIv8V79nKJjTBjFFb65etOzOQ10SlzLPmcPfbHsiP7kf7pxgois7ZuV0ldg4xp0tCikUvnoYdkUKl3MITPVa-FaUFsJbe0BCj5S_X2d7z8dqk4nzhbR1imQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V07JNhBupwZjApmf9FrmLjd1x7oS0BBX-vIgIGg6eszgaV-hqEDDEF0PWZyOjaeIibGq8soOGmn26QFL3rftSMRakCGpkljMQg2QWYjl2LBoZPKG4pDRzYR-uXPxe1fK4mRxBA7hru0jKizDiwyu2McQ_Ke84b1gy2XO_GpHo0O5CvBatQe4VjlXPve-nN2zyyEQNoPGaQ0-3L_dzic7C2YLQgY5NbmlB2oZqNY1PVVTwI2h3Ur9CS2NlICf9iRyyh97biLfLFBKWStYkqQPzBiyiaqRS_HTQrgFc4oz7XzqArRBDakY5QB6-EHeBwzRKXrl1nfGFo6s9EGpOr82sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در حمله نظامی آمریکا به ۵ استان ایران
۴ نفر کشته شدن!
فکر کن جمهوری اسلامی هر صبح
با صدای اذانش، بیش از این تعداد
از مردم ایران اعدام میکنه!
جنگ ۴۷ ساله جمهوری اسلامی علیه مردم!</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/6343" target="_blank">📅 19:38 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6342">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">عراقچی میگه توافق ما بهترین توافق ممکن بود
اما به سخنرانان و مداحان تجمعات خط داده شد تا علیه این توافق شعار بدهند.
همه می‌دونن ریشه جنگ‌ها، تحریم‌ها، تنش‌ها، انزوای ایران و….. همه از خود اینهاست!
قبلا هم همینکه در بیرون به توافقی میرسیدن
موشک آزمایش میکردن و روش به عبری
شعار می‌نوشتن!</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/6342" target="_blank">📅 19:35 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6341">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">سپاه خطاب به مردم منطقه : فورا تا شعاع ۵۰۰ متری از محل‌ حضور آمریکایی‌ها فاصله بگیرید.</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/6341" target="_blank">📅 14:05 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6340">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G4ySAj5FvIzaYGRVrk3o3tvKojce_tpRltjPfjaxJKm3LLbFV2YPfHcwBm-p7NrYv_NVqFRpMzdq6DCjunsV0FaDHtv4cp7oMs7Wk1X0SftGX6TRrbStx-n40uK0Msbc_WPeKaJxB-g5AYuhXtoonnao7qiwVoMnin5cI72AGRuvqT6aJn2R80WNhQOMRCikzAermZuG2j29PIJkYHI6AvwhCA4Ii-_ja6EcRV-QXk2FPFivPevIz5UlI83b7N5dUhr6jSMDvovpZGyRvHeWH3K5M_5yLRtoQQjFxaI6fW_7ZisTHgmqIS2rV-poB9KLe82r1Bj-32G__iNRA0ZzVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صفحه دوم روزنامه کوریره دلا سرا - ایتالیا
حمله دیروز گروه تروریستی حوثی
به دو کشتی تجاری عربستانی،
حدود ۱۰۰ میلیون دلار خسارت وارد کرد.
ترامپ : هزینه این خسارات‌ها رو از پول‌های
مسدود شده ایران بر میداریم!</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/6340" target="_blank">📅 11:25 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6339">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c07c232479.mp4?token=KkQyptqVNsF45WHnLfCRqmM72EmjPY4_9rcilxv9aTFyw_ZokIpX4yf26TVA0tN_GMSgOya6SkoLeCBwpxnCjFxEwsSn-OCDDCDOnrsMwaJkv6FDvDv919iQx8sAhQGIhzOMKtz2nKI9DctPYjd1t0Q9o0uct7pGfWUr9z-DMt7-7AqvfbPwKOgqQv3gGCM18RFUkpPPVi3zhwOyxTkr6Cw-la-NJOCDKpQtF5YWncyz7E2Ig7e-0n8MbFMeisGNqgrzCZJECsqAM-n2Q5-1nRM9WnaZ3_f0EHD8JDC5Jpz_lV5LIrBu8__0PlX5KT1d8EjG6li_knF2vIIZqxJganvRztio39gMjPejSNeXCtRJnbIGfXwvZ0fsLLARc7Z6RShWcJJymaoaGZZVeKa4nxU3MnDVh7BDEp1vvNsIEpA9eETZSwfpzo-ORILkF7UVy4Y1S0TCB8BjbTcAZ8EsqmMLzjhFMl9AhfJCF_VivD1Pk-NBLvJfgeVQJXEdylqlhQ-AXNmQrtwP8QKjQ_yeaf2LGFbXIIafTtzY2iZkZpG_Rc84upWpOSXZ5g5tz1VytelB9aZFCy0Spwm_ZvhSLaiIfe22cdcdvXKO-fFocwmgZCRTcenIg4nQVmdx6xSiAWT4CViqqzDXBZrTzONRUjPUVmASXO6xArwtMsrmZB8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c07c232479.mp4?token=KkQyptqVNsF45WHnLfCRqmM72EmjPY4_9rcilxv9aTFyw_ZokIpX4yf26TVA0tN_GMSgOya6SkoLeCBwpxnCjFxEwsSn-OCDDCDOnrsMwaJkv6FDvDv919iQx8sAhQGIhzOMKtz2nKI9DctPYjd1t0Q9o0uct7pGfWUr9z-DMt7-7AqvfbPwKOgqQv3gGCM18RFUkpPPVi3zhwOyxTkr6Cw-la-NJOCDKpQtF5YWncyz7E2Ig7e-0n8MbFMeisGNqgrzCZJECsqAM-n2Q5-1nRM9WnaZ3_f0EHD8JDC5Jpz_lV5LIrBu8__0PlX5KT1d8EjG6li_knF2vIIZqxJganvRztio39gMjPejSNeXCtRJnbIGfXwvZ0fsLLARc7Z6RShWcJJymaoaGZZVeKa4nxU3MnDVh7BDEp1vvNsIEpA9eETZSwfpzo-ORILkF7UVy4Y1S0TCB8BjbTcAZ8EsqmMLzjhFMl9AhfJCF_VivD1Pk-NBLvJfgeVQJXEdylqlhQ-AXNmQrtwP8QKjQ_yeaf2LGFbXIIafTtzY2iZkZpG_Rc84upWpOSXZ5g5tz1VytelB9aZFCy0Spwm_ZvhSLaiIfe22cdcdvXKO-fFocwmgZCRTcenIg4nQVmdx6xSiAWT4CViqqzDXBZrTzONRUjPUVmASXO6xArwtMsrmZB8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روایت وزیر نفت دولت رئیسی از تماس موساد با او و انجام حملاتی در ایران
🔺
جواد اوجی وزیر نفت دولت رئیسی : ما ۱۰ خط لوله بزرگ و سراسری گاز تو کشور داریم، تو یکی از شبای بهمن سال ۱۴۰۲ ساعت ۱ شب موساد با من تماس گرفت گفتن امشب می‌خوایم آتیش بازی کنیم‌ باهم،از من پرسید ۳+۵ چند میشه؟ گفتم ۸، بلافاصله گفت همین الان خط هشتم سراسری گاز رو زدیم، ۵ دقیقه بعد دوستان مسولین بهم زنگ زدن گفتن خط ۸ گاز کشورو زدن،تا داشتم لباس میپوشیدم، موساد دوباره بهم زنگ زد و از من پرسید ۴+۵ چند میشه؟ گفتم ۹، گفت خط نهم سراسری گاز رو هم منفجر کردیم،چند دقیقه بعد مسولین مربوطه بهم زنگ زدن این خبرو هم تایید کردن،من تا رسیدم سه تا خط اصلی گاز مارو زدن.</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/farahmand_alipour/6339" target="_blank">📅 08:24 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6338">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4193f544e.mp4?token=WrUlIHKcw8hD0cS3dhycrc9fb066b3ywI4dAniqSFZFtN3YhPbqYUVaIH_e7WNFRd6RXbjPogm926q18cyfPNnu5eFu18cxc89qyXCZe62rv2D9wEtUZpnnQPLoBJeU2icg9JSneIWLsNRhZZ5nSrPzf_8V_3y9WmkTgvROJaynD5wl2FtkQNGb3uZobpIu8vu0ugRjzHBZSAspOzlVO5h7w6wTwHlLmiDA1E9tVVOVecVQ7Of-A-E1rR54U6mG1C8pQzYoRy8e9qwvEy5835bHoC4lQn842qfwkyNIFh5UEHDJsKW8LkgUAgeT00VIuCPQoINQTDcGjNMXpKXpqtg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4193f544e.mp4?token=WrUlIHKcw8hD0cS3dhycrc9fb066b3ywI4dAniqSFZFtN3YhPbqYUVaIH_e7WNFRd6RXbjPogm926q18cyfPNnu5eFu18cxc89qyXCZe62rv2D9wEtUZpnnQPLoBJeU2icg9JSneIWLsNRhZZ5nSrPzf_8V_3y9WmkTgvROJaynD5wl2FtkQNGb3uZobpIu8vu0ugRjzHBZSAspOzlVO5h7w6wTwHlLmiDA1E9tVVOVecVQ7Of-A-E1rR54U6mG1C8pQzYoRy8e9qwvEy5835bHoC4lQn842qfwkyNIFh5UEHDJsKW8LkgUAgeT00VIuCPQoINQTDcGjNMXpKXpqtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب - انفجارهای پی در پی در بندرعباس</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/6338" target="_blank">📅 08:03 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6337">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t1vhh_BlzRj2zELmxSoyzItY3YDU_xoTSuXz_BrAn2UM9MqT_5hZEyQUE2R6ZGy2q4pmam-ocLbERfW66psm2szDDWg8r6ZQZgtyxGXdiw_fIGL2eB4ShHfpTv1HwVG9muR9hxy36jksDuW53tG87hNswCwn59EfrbXnaw01_hlxuH34IHphCQCKj7uhWb-mWOcprdscqLXHT-KD6uGP585eLDpXCv_Nkxu0q1H7ewbwWSPrEALzpwu-FXqRdlutVYvZLAJBxmpCf9fzMvji9BxiKFfbF_2QwZIn7WNaZmTI4qKBxpYYtQCtye-VBA71Z0iZyuz32gCYjI-rbqO8Mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تهدید تازه ترامپ‌: از پولهای بلوکه شده ایران، خسارت کشتی‌های آسیب دیده توسط جمهوری اسلامی را پرداخت میکنیم.</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/6337" target="_blank">📅 08:00 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6334">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d84604bc5.mp4?token=QyFFM8KZBdL0Bgy0-ASky2Qd96M1rYpM9mYk6_Ff0TX-0Djvrsv1g4xWhPlhESLdZqrei0R4VZ3MRoc5EWyv6neeeq55ZHMsMkO9fVV01fatJCkY5euFqncTS9Dwz_UPJBRuFM_YZ0doFxmfl4z2Ii6iPxLdfEFIkzmDqlpjfpTPdH1Z5OV59otFd-XmYh7HUrUMFhn1VRwgd9Pu5WNNr0cVnsbD4LaWQFTQZG82mwNN8H2YNeseAx2GrVc04CsPXDrXtCEjcsuI343dOujwiMpWNkhYe5Qx_-pXaZ3ZpB--aO3GI1T3XfYS2DA1YPylDUCGMtloKiRssLzsY83ryzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d84604bc5.mp4?token=QyFFM8KZBdL0Bgy0-ASky2Qd96M1rYpM9mYk6_Ff0TX-0Djvrsv1g4xWhPlhESLdZqrei0R4VZ3MRoc5EWyv6neeeq55ZHMsMkO9fVV01fatJCkY5euFqncTS9Dwz_UPJBRuFM_YZ0doFxmfl4z2Ii6iPxLdfEFIkzmDqlpjfpTPdH1Z5OV59otFd-XmYh7HUrUMFhn1VRwgd9Pu5WNNr0cVnsbD4LaWQFTQZG82mwNN8H2YNeseAx2GrVc04CsPXDrXtCEjcsuI343dOujwiMpWNkhYe5Qx_-pXaZ3ZpB--aO3GI1T3XfYS2DA1YPylDUCGMtloKiRssLzsY83ryzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نصب ماکت آبگرمکن در مرکز تهران</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/6334" target="_blank">📅 22:52 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6333">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
ترامپ به کانال ۱۲ اسرائیل: در حال بررسی یک حمله گسترده به جمهوری اسلامی هستم؛ حمله‌ای بزرگ‌تر از هر اقدامی که تاکنون انجام شده است. به تصمیم‌گیری درباره آن نزدیک هستم.
او در خصوص احتمال مشارکت اسرائیل هم گفت اگر از آنها بخواهیم ظرف ۲ دقیقه آماده می‌شوند، اما برای آغاز عملیات جدید به هیچ کس نیازی نداریم!</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/6333" target="_blank">📅 21:56 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6332">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">‏هشدار سپاه: هر پایگاهی در بریتانیا که برای انجام حملات علیه ایران مورد استفاده قرار گیرد، یک هدف مشروع خواهد بود.
‏واکنش سخنگوی دولت بریتانیا به هشدار : نیروهای مسلح ما آماده‌اند تا از بریتانیا در برابر هرگونه حمله محافظت کنند.
بریتانیا به‌صورت شبانه‌روزی و در هماهنگی نزدیک با متحدان خود در ناتو، آماده دفاع از خود است.</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/farahmand_alipour/6332" target="_blank">📅 21:24 · 01 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
