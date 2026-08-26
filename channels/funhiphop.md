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
<img src="https://cdn4.telesco.pe/file/OaSam8W41L0SHaGXqLzFyGeXEh0d34kRjMb9G5wl7n0yosc_UWAXiP2Srr5x4d8UlQqD7NmNE1lJPVZiL0MbFvZxK-25RFoo38Jev3Ot3CXL026ZVBQqmob_B9LbFc1ltfak0dhmIQaNitsf24bKLgrEchVZPp9wtNltrKvaTmr7kNLosaxO9psJ6YxJ4av4uWz396lG0xfpwEgLD1j9aPw9Q_n--kbemh5UGmFhifOEltScy6tYRdP_455qHg9RCALN2weI75HWp8kcI2aBRJaFRjzKaYNrQp0JHQ3aemrQcgn3nJU-2bg917qU0Gd0VBgvW_4pcNg4AVnrT5KBGg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 225K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-04 23:53:56</div>
<hr>

<div class="tg-post" id="msg-82616">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aBKDy_HnQYd2ZAElrZ-GFlHb7HxH9rk1pCnUbcu-BTHtS5C51fWEB1VxbEW8domdwNLVPptCZxMB9-1tpYt0P1YH217bK0Bcg_A8zHYB7nMkTPyzTqzx5xB8t0q7mBS0m74i8GFeXPjx_CniVpHvFxfzSzLHZy_xbzwhV4HbE4QPx35XhcJV1FkOF1CEHHU_RNvPnNw2JB51BEbTX7erLkI1CebjcnQSfDZQYR9DTSiuO18EbedE7hyVmuepbueXB3x54NC4u300XV0mmNHmY59b6bX6UbXqNlDSK5JVFbkurCgVldaCQg49RIjDMmjlDctRWcFO6wgbWu0zoJ_atA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی وزارت خارجه خدا لعنتت کنه با این جوک بامزه و سکسیت، حضرت آقا شاهده که ترکوندی شیر.
فقط دفعه آخرت باشه لطفا.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 1.23K · <a href="https://t.me/funhiphop/82616" target="_blank">📅 23:49 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82615">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mw3MiOgCquP3Swm2GLBatQnhPZXIsuWZ9K3okokM985fTeaKpJBvYQlp1Zj_roijPEo5i0lVKnBYSGuzW_hkyle0T8-xHpkDMFUK3LyQDyKBH9LsLoTB2rCpNZgU7mk5Tne-xWRsW1Wh6uryYhz0sJhW0DRGUVA1CLNrHYdiQEV0o9Lcu9GuwE-yZJX-cGXb4ppz4Txhhna3Iwo10tMFaWokgvz2pv6oVGGJZKApL-9P_1WyjzAJ7MUG0zjsx_U26o41UYnplKF1S5oexcJY66fHLabnsn4Q0owj94Has83W91FzDgQrEc6DU0BswX8tbkbgr6jMuGBl50hzqgK7Tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ناراحتی دیامونده از بازی نکردن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 3.46K · <a href="https://t.me/funhiphop/82615" target="_blank">📅 23:34 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82614">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">رئال جذاب مورینیو</div>
<div class="tg-footer">👁️ 4.45K · <a href="https://t.me/funhiphop/82614" target="_blank">📅 23:20 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82612">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CT_yulVWVfBZFU04vdEsyHqvMACYhTKiJZbjagesrIJIrXM54GDO25HGavP1CjtyTS6WGSZw1YuiGLvMC-_9p1rBPW_7K7jF7yXaQGwKNylw8KeNY6oIo0tCkkeAWwnElmpAg86L5x6Di2ILjsAoQXqDAAs_CfDSntBQYO_CxWwUGfGgmNqwTDHp2I09kyaHekCYNXMDbrM5bZ9NvPbkHZr5dWIvgZXaKLUU_KnFa98Vlyoiza0RHMhoKf9B6G0oIu01di0WCwSkOmUf18J8N4m-Q6HgbJpRJvLJNmQWw7GHeIqaimdrBQObgnxjaKqeLeUr9BO3v4YHL682YJc2xA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حافظه فان هیپ هاپی
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 5.7K · <a href="https://t.me/funhiphop/82612" target="_blank">📅 23:07 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82611">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eR6Vag0cQRYJ5f8RKZ-SVGDjZfk5DfRbejNo8hwiaB2UDbDH0ZJBcEOXX06JkB8pTinG_g9M3Zgw0yqFlz_pyvSzrF0a0gVwzkVCdR59C6D3ByAW8UMJgjz7Gq8yHAGqRK60KohdRprwRc4YMt52BlPMEZOfsR19SUtf_Jx1u3DNnHA_G4dxds_L1D3hqp4Kz2gyr2AfpwPTk7dqW7tUnqxXaHCVvYh2C7tYs8LYWN7gnzO3AKP3nMgKXxQG7ib7i5df-Lhe3rziXyVNJ_PBAFyPXoeq8z0_PBroDYB40Q114L34EjXB7S_VnAuhAQ9LHRnzJe6WV165th6stfdxRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الهلال از وقتی یادمه داره سالی سه تا نوک میخره.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 7.3K · <a href="https://t.me/funhiphop/82611" target="_blank">📅 22:24 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82610">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NQZdxnZbWZ7XKxoIlUcjkYPbTDsNnutaHeX2zlIRaIJLWKcgEpdsibJ-HRPrJ_XU72oVZ8UqUhrVO4h0hWoYM0pygy0_E7fyXtDTvUL13xYaGb-Dfq8ZGTAeszTZ56BsoMXSxFSzyTPB6uw0XAToktFjLysLSNxR1JEcF6-HowSiJKW7ohjxeb_LGkSoYD3GPtyxDUzHu3di7is19Qr6Tinnbkeumrv7khC_DkG3GLr6BDNjAikgO6Oz6W2gFc7dekNFtcnT6bp4-Jnu_7Szalh9uQbVNkyCxuMsMcHNjjntknhDWDCFrTitOMznmd1sHfla2lJxTahJ-NL3ulHdKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وضعیت کشورو ناموسا
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 8.86K · <a href="https://t.me/funhiphop/82610" target="_blank">📅 21:26 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82609">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FyPksXm5JWbnkManMEoZmwXbrJahOL77CDWyzKkbHfKXG_9DfAiYorb_5VuOrejbUikTlyTeBQb4m9rh8lHTz2dPVEPFD4AVJA2EWOkmDCp-CUwhPQ-qSDtcNFAKJe4yQjvlod_2eCSzmvLxwoEC5NTKDDhKDhPfc7kTCqcYd0qUIjt9c9wyKX6_tdtInm3rc636LIHqx2UawVRKid0_-P60xpznZYbq-EB5mOiCESU1q6br79Jh6ViDODspLJP8Pl8wPsHOxzBDsAMwfa2fllKytBgElJVwF3o-CIQdOO78gX18UaYZy75YUigGOzNq0IaefDYHNRju4Ls6cUJWpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پس یاس چی
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 9.77K · <a href="https://t.me/funhiphop/82609" target="_blank">📅 19:51 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82608">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a262ee6c0f.mp4?token=U3xGVnMMl08OT2wNV6OCJO0FwFKKfg2FXhdorzjukAx3C5K_zpwkYnn60PRkhrYWGwpsA_O7gr2tiJZpVL-Jz_xqRzLgwasJJDM9y8k9hAu2bP9pCuh8HnIv5w-fnqG2yRfBf41zRCODvPrWKlQQrQogVbeAd0unIRT4kWkfAJLPhL2-wW7dVI0sHudALIpTQTRzPGN9NVRAZvOjix4JtAUtGJa05gdA-A_Zd0BO3JWEuq66jM4BnJM5wdYlKcgjGo2DvorHQfTlCGVH-xFcQNZRBqd1fIzR6THJsBw2MPEH9V9Z_n3q8LZS7G0AAdHMc0CqTibOsl_gMT2coPoB_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a262ee6c0f.mp4?token=U3xGVnMMl08OT2wNV6OCJO0FwFKKfg2FXhdorzjukAx3C5K_zpwkYnn60PRkhrYWGwpsA_O7gr2tiJZpVL-Jz_xqRzLgwasJJDM9y8k9hAu2bP9pCuh8HnIv5w-fnqG2yRfBf41zRCODvPrWKlQQrQogVbeAd0unIRT4kWkfAJLPhL2-wW7dVI0sHudALIpTQTRzPGN9NVRAZvOjix4JtAUtGJa05gdA-A_Zd0BO3JWEuq66jM4BnJM5wdYlKcgjGo2DvorHQfTlCGVH-xFcQNZRBqd1fIzR6THJsBw2MPEH9V9Z_n3q8LZS7G0AAdHMc0CqTibOsl_gMT2coPoB_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبر خوش، نیما تکیدو آزاد شد
❤️
💘
💔
🥵
😱
💋
🔥
@Funhiphop | Menot</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/funhiphop/82608" target="_blank">📅 19:35 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82603">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GDQIkxQE7EOh4BdehxOH43l2UBBPArqeHIHvsUmWNhPtLccIZ4oAquRv-NJ-HpQ92oRc1ju_m1ZsUcgS4WHE55dzOxaN0B0X8FyUdUI5i9c7OQ15XSjSFolTsy4XIUVwuxuTQRtawLJfaW5zwl7hTAZdfPdtcNxO1FSavKq7_Ppr-ceNZi1-yCK5-2KLug4TxpI2sM84GrjR797Gukd8b4mCF-PTCr2tRUt-C6Iae2wDFVB4ClcG4qh0YklWwLK-mpMNKbThpmPbSG72KxHKen1NY_TuLCBs9TgW0klLoNRGLUm4GZnGeJVxl0VzhfBn2ugqZKCRMKCkLEdaRPcGRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dbpQ81zHYm3CpVGD40qIW9-eaLtNWzkU4zvZq1Ak1cEpUqbKbP4FO0odqGjMCHCCVtJAOwhzHN-wyL1Ib9hsLMAw6dTokRUG1uDsRa4vueX8f4x7gM-vyxQmQ4-vk9DPKn_4PlWx5TRwgYDQUq6xL_kaTbPc70Lktl64JnzHvC9pmQsnmXU590V4zM3jubpGy7stCMdQA2iIRnNpbNNZDaZl7EZVfjUQ1qJMorwWoFrRfFiT05El2crdCrIUvIAZNE7sE_iBk7-rqifWxJMmXiIi3qsXDRMkPCDUoOT0d71KxmdFjtc66EkvCLqfZN7ZCn-XK-CeNnqjjmu8enxX1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jQTjAb-pnmPZbkJ6Lz7jw9KzV5jBWq2Betj-JPxHIeXLX7bg-b285kfwEgmtJpJTW3u3A7A2hEsW3p7rzdGrWayI9E0_s6u8RhhRsw9WPHm-ovBd0IGRWg6i98jREAQOhT_P3YtYsvzG_pXl9JaS9RHmFvd99XN2Ls9SeA4o443of7gZmNpIarSGHfimwEL59JBwgeUFK4rd_40zCxqGCnblS3chE55lXCQvfVuecBvtVDMGJ7F5NPeFcpKiXg4tTG690Y3UW6dw0x-hofoNmztkcrxsp60wi5SdE_KxH2gcGC4f-wR6Wx4mrJikQc16KBMP92eiI9pcUorOPurqmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N2CiUDLVYjpmGMsUtZdPM3gipn31qx8TlRrc7cR1o1mwlz5gZpZEmeknjEhpXJe5MoYpvF5fRsxfgWY44JYC2DPb9OULvRtIzPq4MFZaN_AMQpVz8xbDP9ckUB5t60p5VNO0XCEIFHgHtWM-4eV8UCV4_CSlsUOOUMmRUE91Hb3KhB_oJtZ1wI04MWCNxihDwm2j2G2io5iyqKvs9d5rypHjBQ3ydsTspTFXGkOZhqY6tvqQxPO75PL9dww1hELk4V130Xo9-RhXOdTp881BIt5QGj7n1j5tfc6BlWWed3sd7EI920HlePClSMNXVTiC96wSiUCntTI6Ek7ju4zIYQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c8d5151d06.mp4?token=eIJWT-2PIVRLe3yFp_qoImVJ7laad_KCyLdYgOzLeyH7B_MERYmBBdoOEdjI9_ACXkl9tdvjNyWKc_DP0UYUeFjFVKCB8_CkP4HHQ-NI20ibbPzMKGDyTl7rUSqVI_3KeW2eIOBSn6zM4OwO-Q3ljo1M_9ODhZ6FgmjSeEr-6u19Ilu75wOijKrZRny-Tr9ASA52FfMcwIvEctJ-gt55HKOgzNOLGMBRw1L9WVMU-aGGWUXrN-8VwoWbFhEimo4Xmi-fq3d3MtveyHh7cHS1Tzn3AMCTucrab2-dFE_4mXb47fW8dMp11fKNu9pDNWHrgG66DlLBvuxfIt8ekV0e1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c8d5151d06.mp4?token=eIJWT-2PIVRLe3yFp_qoImVJ7laad_KCyLdYgOzLeyH7B_MERYmBBdoOEdjI9_ACXkl9tdvjNyWKc_DP0UYUeFjFVKCB8_CkP4HHQ-NI20ibbPzMKGDyTl7rUSqVI_3KeW2eIOBSn6zM4OwO-Q3ljo1M_9ODhZ6FgmjSeEr-6u19Ilu75wOijKrZRny-Tr9ASA52FfMcwIvEctJ-gt55HKOgzNOLGMBRw1L9WVMU-aGGWUXrN-8VwoWbFhEimo4Xmi-fq3d3MtveyHh7cHS1Tzn3AMCTucrab2-dFE_4mXb47fW8dMp11fKNu9pDNWHrgG66DlLBvuxfIt8ekV0e1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبر خوش
،
نیما تکیدو آزاد شد
❤️
💘
💔
🥵
😱
💋
🔥
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/funhiphop/82603" target="_blank">📅 19:28 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82602">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lwfUeeTxcsOhG_3Xqy-LJWJGtwmdcXoNKjmHQcoRCoDbH6dVZF_1MwdSY4g8q6xdsyHBhH_gf0MOWcjj2mCVeX1SQTKlzhnBnfXichDY1cesFt0pjI2ICWpskljyffYFQ2FOcekYPSJXY48yuzqNUYEg61g-7_v3A8HZWtME2ri7K4ZQnW0A6TikxpexACSCFcYu3VtsXGMWcQR4tbBi7LGmgLuV_q8EPwY04qYyTZpxPGCvbNM757w8nqx2zhk1m6_n_WaXMdUIFJyHQQtLXT7nErsjS0w4uqHuUxFSKypcWzd3uootEkFQgN0ELiYuVXr8XyD7mMP8T8KfcYO25A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
رئال مادرید
🇪🇸
-
🇪🇸
رئال سوسیداد
🏆
لالیگا اسپانیا
🇪🇸
🕔
چهارشنبه ساعت ۲۲:۳۰
🏟
ورزشگاه برنابئو
🎲
با بیش از ۶۰۰ نوع آپشن پیش‌بینی
👆
ضرایب شگفت‌انگیز
📊
نگاهی به آمار دو تیم:
✅
رئال مادرید
:
۸ برد، ۱ تساوی و ۱ شکست در ۱۰ بازی اخیر.
✅
رئال سوسیداد
:
۲ برد، ۲ تساوی و ۶ شکست در ۱۰ بازی اخیر.
📈
میانگین گل در ۱۰ بازی اخیر رئال مادرید: ۳ گل در هر بازی.
📈
میانگین گل در ۱۰ بازی اخیر رئال سوسیداد: ۳.۲ گل در هر بازی.
🧠
نه گفتن بخش مهمی از استراتژی است.
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
g4
💻
@BetForward</div>
<div class="tg-footer">👁️ 9.3K · <a href="https://t.me/funhiphop/82602" target="_blank">📅 19:28 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82601">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27e5d7bb63.mp4?token=efS3A4A5Iu2_yjfjCN9yLjSToBiAoUIIN9XkW7V1fX_sq3VDyoMaierl8Zv2_853vUaR3zjrIvJqBMTBLFlSzrtPzV0OfGneSiLEFxPY0h4CV1Y1m9s-xfsKJGdu4qtuaCAfZvuqeXGq8TO6Y0ltM2-zGTSSfr1uS1nXQ-jpRQQb3sy5vd98FLJvZxEjZR389RSPs26SrA8tSC1zLtu6nrLxWQ0mma8Us9nHYn1zF6XqQ2pKsoDcn9pq1Gwt2eIyaAIBUR65Gri7xQzp0wPJ-EarbKa_kTJZ1tIJUp855b7k4iAVXWfFir_iKjLjnLuMKAW15O5CeiK7ho0_HWiIeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27e5d7bb63.mp4?token=efS3A4A5Iu2_yjfjCN9yLjSToBiAoUIIN9XkW7V1fX_sq3VDyoMaierl8Zv2_853vUaR3zjrIvJqBMTBLFlSzrtPzV0OfGneSiLEFxPY0h4CV1Y1m9s-xfsKJGdu4qtuaCAfZvuqeXGq8TO6Y0ltM2-zGTSSfr1uS1nXQ-jpRQQb3sy5vd98FLJvZxEjZR389RSPs26SrA8tSC1zLtu6nrLxWQ0mma8Us9nHYn1zF6XqQ2pKsoDcn9pq1Gwt2eIyaAIBUR65Gri7xQzp0wPJ-EarbKa_kTJZ1tIJUp855b7k4iAVXWfFir_iKjLjnLuMKAW15O5CeiK7ho0_HWiIeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این ویدیو از یه ایست بازرسی بدنی تو یمن امروز وایرال شده و مردم جهان که زیاد با ساز و کار خاورمیانه آشنایی ندارن پشماشون ریخته و براشون خیلی سوالا ایجاد شده.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/funhiphop/82601" target="_blank">📅 18:14 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82599">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u3g6Or1rNEKvF5mevlYU2d_0gE8cyescV3imOkSn9rpKqbqvOcR2JnDwgdpEvj5E6Jo3hdpZbCdkLfSbLgtVh9KTp7IURL5WoqeXCwUG0HZwI7N-JWceDfT9coFc1ydpVHo_Dds5hFbc9a1oEAejoaSVG2f9YrD9EFlAW-hAtcsev57FDQ78evinqJ1reXuzkfvzbJkMcIXE9sSINR1BZGbEm5QJTkSf3GnwUR04NzC6oVh4hWhVdaRFY-9QeyPeTKlzZknEnrRgl3oCs4QMplFUEd7OHKroQDqPyDU2Y8-v3mBffB5m1T18Ly6OfhpzJjivEXjs3NKgRZk8tggbKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EP3TbXYpbD8wDzIVNc8in3sFbMtt2-GxAky5TdELDse5mYGkVqe3Y_WnV0Kz-X3Mtudms3THynVn1ldmscOQ11l_dyVp6XkiX8TgY2WLWhdjj0QsWhln8jZHdoDm3Pjr0r27bacNVBLDm3qKdtevHs4RQUNwvlf1pHxb9wEOL9SF5GJU3rR0rW15KmUreSSc4-9K218oieuHcR62bBuHM2gbtg_sNgvbO6ZKEa4BE8PfPYOC27MfTH_nR7MGbsRhztChKP3G_WL3QGkKWpChG4YZuNf7UyewxS8rO-fu3RDHmlRWT78oOOJm_LmUCv1PCNwjt2B7-aNws1ZV_znY7w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">هالند با یه مو کوتاه کردن از غول کصکش سفید تبدیل شد به کراش نصف دنیا.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/funhiphop/82599" target="_blank">📅 17:58 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82598">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">قالیباف: مذاکره با قاتلان رهبر برام افتخار نیست و برعکس برام خیلی سخت و امتحانی سنگینه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/funhiphop/82598" target="_blank">📅 17:13 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82597">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">ریدم   @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/82597" target="_blank">📅 15:00 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82595">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">تو کافه بابک زنجانی اسپرسو ۷۰.۳۰ سفارش بدی ۶۰.۲۵ میارن برات
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/82595" target="_blank">📅 14:30 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82594">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OR1n5xV0wy4MXy3SMRbLMubhkxXHXEgLqGQfotbCUMLqQeYzvb8FODro5OGmFIGcWi6zjyXPlET4BEb9yLv-PnO7b_qgaHgUyRJ9DeujE_ho05yVFj-kJr8JiMAShk3TBS_QnQGVVwvMg2_0csxoczPZ84OUy5jkY-O4n6zhAUAdWO-nUVaCDwDerFXYuXnC06diyoQamrRqlp8m6Dur3DAndmmaq8T6CzKurtKHNW2i9OlHWwAw8-JVsAJy6N2EwzrN850rXXblJT7G6_xMw9WHrpWIylyLBCX6pnKGK6vI2jJHIppeD8NclkqA3x2bG-B6myshzN4EBJRDdSodzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اولین و آخرین کنسرتی که تو زندگیم قراره برم.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/82594" target="_blank">📅 14:23 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82593">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">این پیرمردایی که میگن روزگار خوبیه، ما قبلا نون نداشتیم بخوریم ولی الان همچی گیر میاد هم دنیای جالبی دارن حاجی</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/82593" target="_blank">📅 14:06 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82592">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ee7laIDruhWHP7tD2BFYtvmC4mk5qefTPYXQf61k2X0tmCmPseF-8rmj12Kn1b7TpdWAu46CPaZIBEjjJL_dhFtvf8byQ0k5BAP6iY1lLD-vyW_cdITvvwxKpwnrbmuuF-pyTdKl11_3OW3pXEkL2O2nkHkAppSQ6M_kBnLptlAFWUdX_YfmPxEO6I3cTW-JZv9xTAa9Bkdj_6yYk6NPGyaN-UNzwlwBNh3uIHWjA6HktL253QiDcJ8Rd3hthzRbzM88rwpoqlH4hm86AmdwgYSlocqpoRPasvmiRGjsCsFVxRbJob8yHk2XuZRbAaqzFSgi1cgDpOKtvMMwM1hCZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بچه‌ها بین این همه خبر بد و ناامیدکننده بالاخره یه خبر خوب آوردم براتون:
قرارداد سفیر برند رولکس با تیم ملی فوتبال تا آخر امسال تمدید شددددددد
😍
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/82592" target="_blank">📅 14:02 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82591">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tm7J0W7xpjta3JWevAnpJuqos0vplH1YOlWjV535w-VEVczQ-YGvjWJm4CWTHdhAL78diZvv7MA-72eJ37Qu8iV9rtXUTtPyw41wSS02MQFGyOM4mkhFEdOqG4L2Tx29kLGh401PVvcJkLK6HHLPccnFOjs2amut2AI1omhsINdkhobAowdwGHt1lKKfBYg7JwUa1axrKPVkOTHkKczIpvtFV_bBnb-t7VXvC31H9_Uzyg4_QfEkBbmjkDxKytEVWMuNDeYEr5r51KsLLNV8XDurQmvja8fdxhj_-ltAJl8AaHlrUeYzRhI5pLxX6E8OpnnInee5N2mFvPEmU5AN-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ریدم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/82591" target="_blank">📅 13:08 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82590">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lq7fuwrYGxwcvzakrviPoM9TjHxZi5R07i07y0xYX9iAFBZDnt2KNIrFmGdxqHACEG1o_U4xuD53ZQNkqKt9ipkiyzX3-uKDYlByza0z7P71aC1jhskHleR5C6nuWL0EYy9me8PPtIZY3UuikermrCDM2kH_TSxmegPfjTb0OGFzeMFUjxhtnKZQBk0IvbGg0cKcn_-Ea0K83z0cd7aNW7GY-F0W-BDnqWzWK6mrtrLgu2kdUHxHz-K-8Cryv7xDIvK3qkgsQ4HYZ32ai28FDVA__ud9tYq7N6SlZ5pHzHCw8Y2dXcVXs7wBZ0ewHrVYQXWStABKDqZlxXHByppQpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حافظه تاریخی داداش سریع بیا پیوی همین الانشم کلی عقبیم.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/82590" target="_blank">📅 13:02 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82589">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mp2IXzBQhMqF204yiS3tBCkutII7caWsO5Bb1vEjG4Mj4vfzTADmycJSnsHImHndFb_vpGByKR0CunsJbIav5nNfxlts-Ayo8PP-HiSgRh2wvGtEArh74kv2MSWzGoga2rvwB-Zd-vMhaWkg1kfyXZdLUjPeEDsVUfFr4Jn-VRatMRgVFKa0P23ny9ewbv0ih2eLuGn3uar3p5W3O1oeF9pg9i8B6lY-zr39Bt7MCQ4VbV3CtLSnxBcaKpq4x1urrD7DnDmKMl2MCzQ-7n6-enjJUYrs2Cn5r-DE2gObonquSqmRVbyZMW7DjHpCwPkA49QlCr8l2S7pROr7SaMq8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هادی چوپان به دلایل سیاسی اجازه ورود به خاک امارات رو پیدا نکرد و نتونست به سفارت آمریکا بره تا ویزا بگیره و نمیتونه در مسابقات مسترالمپیا 2026 شرکت کنه.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/82589" target="_blank">📅 12:37 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82588">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pll2Ixbouymt_D_k3NlSQ62NI7jS_svHpylwibh213WajXnJIlhoEgtZPvdmHQKzuQ0VMqapRTijGOdsAQdLLrdagepGHwCH83hQX_-dNKt-VVegqwzeAv98z0BQChB_h8QtfvceyvKR0r0SWSERnc72IFUjVwR5vAUwJdLCDeeeN_uVfAx5nRqQN_unjHpz1P6kNCFI1N0JSbZsPU5wbmxF6VhoPOJAfQkOGap050JxMr9CutwygotY5MgYB1r0NgqPPuZvvkrFJkhTt9GerAet3N0wNxqBBJsRM7j0aTSXEY2qaVDHRhiGVYtL20yByG8HKB5VVpIotzpUI1K9Kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هادی چوپان به دلایل سیاسی اجازه ورود به خاک امارات رو پیدا نکرد و نتونست به سفارت آمریکا بره تا ویزا بگیره و نمیتونه در مسابقات مسترالمپیا 2026 شرکت کنه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/82588" target="_blank">📅 12:34 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82586">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ef19c3dd8.mp4?token=EdGCbkx3btq4WYBRoZZgo_mph5lehjF3GKE6_ldtZ9BnjEEanoM6J92Nsax0Y3G46EEo1UiFWw1QrJBNbnaikb0B60speSBdEIJkjbYQLT8yMFUW-XREKp7X2ixgPZUCZL6ErkIZD4864pEqkSfFiaT3I2QnWygq1DHsm0cKrKTjcl_gIXPbt3eY32be5C8FVLMIQgxahc0Jy-RQK5iYU2Ys5n3kWfqS2zRCGDjt06o77P7HuwgspXPdDN7g2_j1ri4Y80KydTvvOYicyK1iW6n9Ehg2l83y3EC5gVNmalW2JmwbvMZJzUB5NJj2JjuI-thFcJoyknhlk-ngsi8CDIO72dUSzOeChMscsD3yMUAZJgWDyHkrD2r3vhE-pAB2h3qk-fPe1MKuLQyQ8K5m3xnZQhyrWsx21DHnIQFbNuYvOr7Gfbm7VxLasq6HMVWgrD_CdIC6_wa-9T5Szsmo7R4eJgCigmT4E1WqqUvIqwG-WlsnKq9Z4abNhuAyXC3J4b53MRxPmd1sVIywuOtMXFeGn-p960dBKHxscQyHYXEDUFTLNs9A5tA3EVAJpLlqBs_eZovK7V3lo8VNPL-PdhJtTKs2sbD5nnRkJKvRbpO8oP-CiTfdHcqkEllVYJ6CGUhmAxPS9Eel492YKA1Z851woOfnknXSCSkai3kOXLk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ef19c3dd8.mp4?token=EdGCbkx3btq4WYBRoZZgo_mph5lehjF3GKE6_ldtZ9BnjEEanoM6J92Nsax0Y3G46EEo1UiFWw1QrJBNbnaikb0B60speSBdEIJkjbYQLT8yMFUW-XREKp7X2ixgPZUCZL6ErkIZD4864pEqkSfFiaT3I2QnWygq1DHsm0cKrKTjcl_gIXPbt3eY32be5C8FVLMIQgxahc0Jy-RQK5iYU2Ys5n3kWfqS2zRCGDjt06o77P7HuwgspXPdDN7g2_j1ri4Y80KydTvvOYicyK1iW6n9Ehg2l83y3EC5gVNmalW2JmwbvMZJzUB5NJj2JjuI-thFcJoyknhlk-ngsi8CDIO72dUSzOeChMscsD3yMUAZJgWDyHkrD2r3vhE-pAB2h3qk-fPe1MKuLQyQ8K5m3xnZQhyrWsx21DHnIQFbNuYvOr7Gfbm7VxLasq6HMVWgrD_CdIC6_wa-9T5Szsmo7R4eJgCigmT4E1WqqUvIqwG-WlsnKq9Z4abNhuAyXC3J4b53MRxPmd1sVIywuOtMXFeGn-p960dBKHxscQyHYXEDUFTLNs9A5tA3EVAJpLlqBs_eZovK7V3lo8VNPL-PdhJtTKs2sbD5nnRkJKvRbpO8oP-CiTfdHcqkEllVYJ6CGUhmAxPS9Eel492YKA1Z851woOfnknXSCSkai3kOXLk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در یک حرکت شاهکار مهندسی پارک لاله نوشهر با ظرفیت 10 نفر افتتاح شد، مساحت 307 متر.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/82586" target="_blank">📅 12:03 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82585">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/090cf184a9.mp4?token=O7-5C6jnH6jIQN619MJKzgLJv6ZJ5azwFCvfpCZTkX9wXcfZAGW9YiXwbCy5GNIFPYnwa5xUvi5DmNYRmPsOOLE91AdwEGEzWAQf5edKCtu52R_5u3GHbWGpTWEo3nwghX22vr4ILjaMFTjHOJWLvK4z4aRVzOtyAXrO88h7fXJ44oeYSZdUUrKeKSaSFOaE6Oksuf6R282CGjWjK1lkfpFrjQAfDcYmxCFe-0BeMuOGNntNkL11p8VjkUxi80vF2G-OuU9aemySwVI1BlfQISwcfRGaWPOPd2-ie4i956g42_CRoDmh0SXfLRnjnB4S9ItG-vItpLUgSsBb9jK1bw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/090cf184a9.mp4?token=O7-5C6jnH6jIQN619MJKzgLJv6ZJ5azwFCvfpCZTkX9wXcfZAGW9YiXwbCy5GNIFPYnwa5xUvi5DmNYRmPsOOLE91AdwEGEzWAQf5edKCtu52R_5u3GHbWGpTWEo3nwghX22vr4ILjaMFTjHOJWLvK4z4aRVzOtyAXrO88h7fXJ44oeYSZdUUrKeKSaSFOaE6Oksuf6R282CGjWjK1lkfpFrjQAfDcYmxCFe-0BeMuOGNntNkL11p8VjkUxi80vF2G-OuU9aemySwVI1BlfQISwcfRGaWPOPd2-ie4i956g42_CRoDmh0SXfLRnjnB4S9ItG-vItpLUgSsBb9jK1bw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینو تروخدا
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/82585" target="_blank">📅 11:48 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82584">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ADRTGWICJEg3HRwmN8r5sVKytlkwq8L7uG7gjfuZ6iiG6fQj3c697ZC7jXBvcNtzFywbUitgNzhAvpxnctxVBASCsKHOxrRQ2cjMGa2czDUy1ak_Rz_DCsYBvfZMjPOCIUVAth4JBT42znTHSM5LEY8FKljdsu__sCO3k5c8Hh7ailc6Aa7wAjcCDZ9Zljm-PU84U6ZTpu5iyhunS6sUxpbIuZe4E0i4SXgc_MMqRwlXQn4dwzeaIomXJdLs10tAc7hOFDuplbH-Nn83iL9dOr2ZOI0tNqZmwbQiEitwrS8Sx-fK0J3KQAwsSownxXsCzsbHCN7py4SZvn2Ak_ZEWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
رئال مادرید
🇪🇸
-
🇪🇸
رئال سوسیداد
🏆
لالیگا اسپانیا
🇪🇸
🕔
چهارشنبه ساعت ۲۲:۳۰
🏟
ورزشگاه برنابئو
🎲
با بیش از ۶۰۰ نوع آپشن پیش‌بینی
👆
ضرایب شگفت‌انگیز
📊
نگاهی به آمار دو تیم:
✅
رئال مادرید
:
۸ برد، ۱ تساوی و ۱ شکست در ۱۰ بازی اخیر.
✅
رئال سوسیداد
:
۲ برد، ۲ تساوی و ۶ شکست در ۱۰ بازی اخیر.
📈
میانگین گل در ۱۰ بازی اخیر رئال مادرید: ۳ گل در هر بازی.
📈
میانگین گل در ۱۰ بازی اخیر رئال سوسیداد: ۳.۲ گل در هر بازی.
🧠
نه گفتن بخش مهمی از استراتژی است.
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
r4
💻
@BetForward</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/82584" target="_blank">📅 11:48 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82583">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BGPdvqMIxFU4o7gbbfouBUhdudA8yEkEsFjCedePAKpvH3LhK_AB080zic86OeM6IjZ-B0W0rVzVm6LhOcPpnJKMBGCWMn15jnEY2zdzSmW6hPuBQYKMBOD4r-2B05HgL5F7SfHakYCIP-B6ymmSxcVNLj6pJDMfFkgsFs6afOBLT7hl1iWtFmONcd__HrSSDOiQ-iEBUOx6Y7syYX3SLLxIIVUob3mK7Tic-BI4Oq-hAvwMN_xrxv3BjvcICXGnipBYPUH6bfdFROiu-vN3rRNFfz3t7sifZ-f9UWhmB8iIGpzAmn--c2T4GaW0p1s8rDetKseOHliiiwgOdyPewQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمد خیلی بیشرفی.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/funhiphop/82583" target="_blank">📅 11:01 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82580">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F2PWnSGUueFH8bALwOFFd4ToliFk3F4xW46UvoPOJ6AIFkcQYPbNBGJ_uv-D2ae3PrWjfglHjNegaFZ66YcbdIUXIqqDiAhi5-J7SN24ebfnZsNEeocDqEaqsQVnvXkezQ9x7a7JjfVL9FF4AiDZPwjHvOgJcQiblzoFmnXd0oghX615LxBKFL4iuuliqg1jGTZs42MG_xXPQaKK0hf_Yhh0-OwpTLY5e85ezswVVX3u2vdAxj-Td2bsX8QlooSoxQPvZLnp28QXsQq6pvpq2z_X1obFymg5PJCTzOqk1LO46czr_qI16H0aZ5DfuxgMWaUJ1RZJw-WGu1C3SfgY7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FhhoX9r7pDpolLT02nLmpgWsGrjiINlred3uDe8KDctTzwenb030aS5pzKa-xCf0Mlw655pl_Mf-SakKKmM0pauItL7BnTv3txxyjnPIkXd1u4t0tdIsSfO3SMXHgMqlzj1RSTXxY4g6W4pLMsud6_uGS-Vu1oO7aG2lV0jI7WkKfiDLCoW7e_xVEwyrA9a95oZ2twa3tyAD2sdcfL09mi2kYtOSQxW9aXrlRpUMR27y-YrpafQ9U8IxuX4PiEt2aRN4eoQEnbvVK8DoqnNhvb0A_MpMQs90JPFN5LxYO2jDD2TcZj6h1eU04T0g8BGHYGScToNTllTIhsd0gdrP3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/maB20sh89sCka3CAWvd9Jh9W0c8EtarVKWhTJ58ce4dsBwfVryjHSlJTPaJ7zj5XrXHvTUdxvajssC-wCBZI-YRoP5j6wNJlcifgIA1lPY_KO--QN5zSM7xBXHzMyZo2Sg5S5Ut8HsLHK9wejaB8_zTG8jX2ZpPPExPXSPU4PJZ_2PGBLvtBmOcYyr1KZFUUoTvHj-HukOHpVUiD-ARoEQ6-Qro2bTepJFUN2HeCaZMt4Y2BLPLLwmYNd7j2vF33HKJpcwkVkEYCgPNyQ4P12JWF_mUBBdQXtJodF6FaCc0nvCfPTH-D8waUNylUd0fuzU_MoDOINKzpxC_EHeQmLg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تو عشق ابدی ورژن آمریکایی یه دختر ایرانی به نام پارمیدا شرکت کرده و اون ته مونده های آبرومون هم برده.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/82580" target="_blank">📅 10:36 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82579">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QT2OCj_HXtJN8ShY6k2mJ5YGgkP8m73udt1QkqeXbck5PvS8HcylFt6qlt9mCYMObyindjbDP-TNMqmMBz3BcosnkFUZ6nTlYJYY8c9lsHaegzQmMkMyCn2pqViq5-njVY56BXVfV3Ih_IUuFvNR76KlFu8iW64H4PHgli2FX-YBp9FoRQQVV-moZwTB71ZtqwkHYTEF5HynxeJSMrf79IQnYjhdPKt16AMzB72MwPADm43IIMgfYdtGlmY1uHy3pQL_gdZkxWph7YC3ptio9ax5EKR-4E0Iq5ng6HNqKSbzCN0Qsk6Fc6ZZcz0UYjFzh5HImrWGz9KbKd-4sTHTsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این یارو وقتی تو دی ماه ۱۳۹۸ گفت هر کی ناراحته جمع کنه از ایران بره دلار ۱۳ هزار تومن و طلا ۴۰۰ هزار تومن بود
خودش سال ۲۰۲۰(۱۳۹۹) از ایران مهاجرت کرد و الان آمریکا زندگی میکنه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/82579" target="_blank">📅 10:16 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82578">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
آف ویژه سرور های V2RAY مناسب نت ملی
🚨
🐿
خیالتون هم راحت باشه حتی اگر نتارم قطع کنن وصل نگهتون میدارن   لوکیشن ها:
🇩🇪
🇹🇷
🇺🇸
🇫🇮
🇳🇱
🇫🇷
🇮🇳
🇦🇪
🇦🇿
🇮🇹
🇵🇱
🇸🇪
🇬🇧
نامحدود 1 ماهه
▶️
120T
👑
نامحدود 3 ماهه
▶️
300T
👑
نامحدود 10 ماهه
▶️
600T
👑
100GIG
▶️
50T
👑
200GIG
▶️
100T
👑
300GIG…</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/82578" target="_blank">📅 00:10 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82576">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🚨
آف ویژه سرور های V2RAY مناسب نت ملی
🚨
🐿
خیالتون هم راحت باشه حتی اگر نتارم قطع کنن وصل نگهتون میدارن
لوکیشن ها:
🇩🇪
🇹🇷
🇺🇸
🇫🇮
🇳🇱
🇫🇷
🇮🇳
🇦🇪
🇦🇿
🇮🇹
🇵🇱
🇸🇪
🇬🇧
نامحدود 1 ماهه
▶️
120T
👑
نامحدود 3 ماهه
▶️
300T
👑
نامحدود 10 ماهه
▶️
600T
👑
100GIG
▶️
50T
👑
200GIG
▶️
100T
👑
300GIG
▶️
130T
👑
500GIG
▶️
220T
👑
1000GIG
▶️
400T
👑
5000GIG
▶️
999T
👑
❌
بدون محدودیت کاربر
❌
😍
با سرعت بالا و پایداری بالا و دارای 10 لوکیشن
❌
فقط 20 عدد از هر کدوم موجوده
❌
💎
خرید فقط از طریق ربات انجام میشه
⬇️
▶️
▶️
▶️
@ZENTROVPNN_BOT
◀️
◀️
◀️
▶️
▶️
▶️
@ZENTROVPNN_BOT
◀️
◀️
◀️</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/82576" target="_blank">📅 00:01 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82575">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XygKEvPh-Kh0AIMjpHjFRh87Qz9HtKQC-Tu6yIeDWJMlJiuRx9-q_ob13pafCRVBUDJwRCH7Vyndqt5wu2wBk7DgVh8yvcRFS_HTB68oKrALE0hn6RjmJurVshsIo2zZel3pXaFcBbx2Av5UY23kgqRfYlnXnynm2ZMxGJhpUo0_5DzgE120UPMK8cKEjMmw3gmfeapvUkFi9nGx1h1FD3cJPy4_xP0Ygn-MQ4KPjKbn3_HMD96KvlZrhrA4jFVSseghrDz_F-J5ewynPhqZD0ajjU1pd1LiqsvLxYwTCc-oKhz9oZc8OsaGEOnCsATIu8-2IwvBrWLpFVRqyM5_cA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینو میخواستم ۲ ساعت پیش پست کنم منتهی برقا رفت نتم قطع شد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/82575" target="_blank">📅 23:45 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82574">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G1d7_rl-qIIDeBcGeGV-yGEGehpHAIS1WN_TXricCiedn7YBymLe7Xz0Rc90KZ7xJydbQnTANOJieM-nJpF68VKY5u3C9qDJQJ4Yh10m7ivpxrETX4CiY5AGbTMXERMQ1yBipQ6BXUqzVLuZ3rwB5daXsazMkYKC5mKYDJYWkPvVy_eYObn13CiN9pve03agqBOmCzQdFohQ0DVUs2zx9NAn6gXu36g11R6eHWywbSLPlAxkHK6UanJ9NnU8WudvtJLmMwTcgbHty6SXqm27ueMphv21dJ8jCftrsWfUtNgubO_LRa5VTjtb7Z-bgOKWOWEg5u4xj_ug8sao3g-Bzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کریر تلخون تا اینجا کلا دوتا نقطه عطف داشته:
یکی اونجا که فان هیپ هاپ تصمیم گرفت مسخره‌ش کنه.
یکی هم الان که خودش تصمیم گرفته از تیمارستان امین‌آباد تهران دوست دختر بدزده.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/82574" target="_blank">📅 23:30 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82573">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JzYo6RbPYdXHn_ASzkBq8YCC2D0krLtwBVEuRhVaZJAynwe8LGy3-WQSd5eSTGEQnaeLF0WZdpRqYV6WaXJmp85acqnAVvPZPsT__Msk0hC-TUvOU8xM1XrxT-oqFP_KeoZlkLuZBwwQRK5dYdpsyjXD3zdGB2lhHOImg32_Jlz9JQn2NYj_mrfXeaRi648tdiq9z0WErqZz1BDp7K6N6OSXBHJsaJGGY3OZnYr_xBZAAsEYvl78DwgUAQqRRl3kkbWa6oX8ETCRo4fjH0xTtlWnL6k39jL6HysnXwRtW_e21eEejw99tmsaY3ARehVtYOfgqflI4wu-wFNHFHAmIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بهره هوشی اگه عکس بود
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/82573" target="_blank">📅 22:57 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82572">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lvw0JicCGQYJf-S0ei6X35BysmhAcaCXq-XwCANR8e0cd2Bk7I7q4tq4pQXUa1O59AD6tq4YBR7PjeGG891sy8ehBl4uJRmpFo4eDIvAubEx6RaQ3NTgkeHnd0o60CzOmvKtrF1TQYhWUHBY8a5Yo5nM23FVtqicPeRrSTve_GMjU-0A5cNw1EvMYK7_XwWwXbNaUz6DjLy9vqHG0BvWB52ifmJLdOE5RTHB2QCS82wR3eqVJ3WFlVdpGrIWOuSqUW578UfRxfy-IrSKlBV1W-GS6IfHiXwW3txOqwzXSPKQiQdwcDqu8i2wzlxmhJ1VYlROKHSoDJUfPAHOo1FGGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/82572" target="_blank">📅 22:26 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82571">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">ترک جدید داریوش تبهکار و بیگ شگی به نام "Vice City" منتشر شد.   YouTube   @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/82571" target="_blank">📅 21:47 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82570">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eKB1ZMzaj_YNsupvGdLXarW8xJ4cKc0KjtORPUbEa7_fOKoolk1ndQspadj4B5ow9TbgSKlmBJg8dqCEML1apc5fH6ijtepCI7vPQbY6dHGyIxriQ56D5Tf49KFtEMwyepbS4R_6GAZ_8gfU1qSo7XYrTVzpfagMGiYjhrZugwxeYcT1qtbBBQ8BJZfcHdozDtFxsUYjWKUTZ5Vu1uOo1jHxE9QK03xIVcMkWB0YjdW30v_2JCpuxvfPfJdOErFn0MLXui_tpJchHgtB7BeeoOPf6K3WBMqbOwn-syx6pSgY4PUjBNqmcbDOjEzc1RU3t17QK20NyWmR7Mxx5fabNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید داریوش تبهکار و بیگ شگی به نام "Vice City" منتشر شد.
YouTube
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/82570" target="_blank">📅 21:45 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82567">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromGangstShip(blue)</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/49661a4016.mp4?token=hdBTyjVILLQClvmP0YDSbooWfSmKrvXA_QpJ1tq2e7mGiEdK7pBK2U9d7TQOaENgXFMhkF-Y6HDB01YebFLveAU5k5Nckl6_HcuEh6Zp3U97xMcmr8fjOeB7CtbTruMg5hmCaehA7rYkyznCG-Tx3uXNfRAKZ0m0N1wot_z6LPuORzoGJSz_CiqK3I6961A-DK8tM0XbNZ8L_G3898iWAB8ZHbyQyWti1djjryfhLMGs1x0NMnn3N91omp8m10aX5dmTJmsN5wXpPXlSfQsCQKB3ei49tmZm0kIhWAW87QbfXXtGqf11jwOsyzw_YNspB9806AfQHVpWdawS-6ue5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/49661a4016.mp4?token=hdBTyjVILLQClvmP0YDSbooWfSmKrvXA_QpJ1tq2e7mGiEdK7pBK2U9d7TQOaENgXFMhkF-Y6HDB01YebFLveAU5k5Nckl6_HcuEh6Zp3U97xMcmr8fjOeB7CtbTruMg5hmCaehA7rYkyznCG-Tx3uXNfRAKZ0m0N1wot_z6LPuORzoGJSz_CiqK3I6961A-DK8tM0XbNZ8L_G3898iWAB8ZHbyQyWti1djjryfhLMGs1x0NMnn3N91omp8m10aX5dmTJmsN5wXpPXlSfQsCQKB3ei49tmZm0kIhWAW87QbfXXtGqf11jwOsyzw_YNspB9806AfQHVpWdawS-6ue5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#Mews
🗞️
“ NITROUS “ Don Toliver’s New Album
Coming Soon
@GangStship
🇺🇸</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/82567" target="_blank">📅 21:41 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82566">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7024532bfe.mp4?token=OO0zXwxOQeg_nZPKYf2V0xBLBGGZOU5xul_oVr8Rz4dMd-MeW3_toas2f0ERVMDPDiaoNUZ4TOP8k7gdJ19WmSI8iRCLUyMBkvCZ7tNJLe7lbQf1ykgnfbZESCLA7P85HSHPRecZhJIf-JDYfGPBJez7PtZWHLV_Y2--s9STiWrhRsxrNcuHqpBdybGq9q0_FRHqZlY65aw42q_nNt2TDMJltm8GOt7aX4DbXc5SwBgwpMLfdI6pn-5enpKm4Vd1ZkuB0sGp5dhOfrzBmDZ4JSUubUfLp2eCv2VXk96pHghasn9eADYK41ODtOqwaEET0X8ZcmvEenRU1hUoCac3GQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7024532bfe.mp4?token=OO0zXwxOQeg_nZPKYf2V0xBLBGGZOU5xul_oVr8Rz4dMd-MeW3_toas2f0ERVMDPDiaoNUZ4TOP8k7gdJ19WmSI8iRCLUyMBkvCZ7tNJLe7lbQf1ykgnfbZESCLA7P85HSHPRecZhJIf-JDYfGPBJez7PtZWHLV_Y2--s9STiWrhRsxrNcuHqpBdybGq9q0_FRHqZlY65aw42q_nNt2TDMJltm8GOt7aX4DbXc5SwBgwpMLfdI6pn-5enpKm4Vd1ZkuB0sGp5dhOfrzBmDZ4JSUubUfLp2eCv2VXk96pHghasn9eADYK41ODtOqwaEET0X8ZcmvEenRU1hUoCac3GQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حاجی حاجی پشمام از نسل جدید ناموسا اینجا ایرانه؟
😜
ناموسا تهران کِی انقلاب شد ما خبر نداریم؟
😅
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/82566" target="_blank">📅 21:30 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82565">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4bb65d06f1.mp4?token=SEHe3q1mmVGdf5BlXDaHgJt0uw9QoclHvLj9rO2WaffUx9XTmhHJfxH_f4w8uplGpQUhs3jS2e8sSbeMy59gGY9wypbl9ng-_NX9rjEX2FDSHC-WuAt8l5-0aKLaLguyQYPO33wF07Mslo96QPNOBqtlg1WYI4oIOJGUH8keBXFKWELgRIfg4HA1B6TtgcZoWDIokGfWQqWgTYqDG5XXEj50l4HHIFdjvzGKqw6T5rQmiB-MdtgXMYCCBsp3hIZmASADgycBMhBlQGnnVSbfenQ6P10AttsdSoYaE-EFlqDDbCN30fsZYghMDhqkh50VJMGpEFMiJQdbifjuGlvz6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4bb65d06f1.mp4?token=SEHe3q1mmVGdf5BlXDaHgJt0uw9QoclHvLj9rO2WaffUx9XTmhHJfxH_f4w8uplGpQUhs3jS2e8sSbeMy59gGY9wypbl9ng-_NX9rjEX2FDSHC-WuAt8l5-0aKLaLguyQYPO33wF07Mslo96QPNOBqtlg1WYI4oIOJGUH8keBXFKWELgRIfg4HA1B6TtgcZoWDIokGfWQqWgTYqDG5XXEj50l4HHIFdjvzGKqw6T5rQmiB-MdtgXMYCCBsp3hIZmASADgycBMhBlQGnnVSbfenQ6P10AttsdSoYaE-EFlqDDbCN30fsZYghMDhqkh50VJMGpEFMiJQdbifjuGlvz6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آرات حسینی تو ۵۰ سالگی:
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/82565" target="_blank">📅 20:55 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82564">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/udQcznUAGcin-iklqqSWRmrebwAjxxon-NciJjHd-E6UulD2C2LFjGE2MDSyKe0_4Ni1oBJcm4qNUxUbzj601qrGtIwl3Vgz89eYR9ejgmlx6xsMLR-0S1x1VLXzCqJDJ2DVOjiM6gLRsNoQa85rYpmkq-KQjQvDyhesKKqTd09c-rFTuYgpWOeBIdiXeHrddosFgZXkZi-09M09z6vtWQK_FrqbiLbEoxUz0rkq_B7RtVoZHjvcD6Y4J9xCgKBdEZmfn59PyTW0S8vRbMAWWcYr7RkpXRw-DooW1602xQvfb4QDGm6iYX2UDeO5FApsgvWBLgnOcVXJUFLkGzORgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مشکل ما از خارج و تحریم ها نیستند مشکل ما مسئولین فاسد داخل هستند
اقایون مسئول خجالت خجالت
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/82564" target="_blank">📅 20:27 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82563">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">کانال 14 اسرائیل:
ترامپ به تهران دستور داد فوراً کشتار مردم خود را متوقف کند.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/82563" target="_blank">📅 20:00 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82562">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">از زیر این توییت واقعا گیف های شاهکاری پیدا کردم.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/82562" target="_blank">📅 19:48 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82561">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IA8q74nkPnqR8eDBv2-d3JxlMwTr7dSPiO4xO4vqOTaPQ_jFk67DEvdJpuzu7CxBlNDExmCsQfvfkRfqStAN32l5RBqliw3HIPn-WuWJsmpeNZdlCTxSZoHfSn_HBlG2DWRrruv731scj_VPH51Lmx9C_TurEqE8uwNB3hi1Nleg-5hUXmpKoS5pJtXzqy2vjD8LDMWsn4jfLtMKFr7fJSAu2FBNbAg6xvoTr7Y1m5jTynaTt9lRhbEPv_vLPb4px-fPsZZ-YeB_-Tkk0kGD_c4JJfK7B6km26jYz5obo4MBjpXfUiaz-RqlF6zkxuFn6GGb5GUj3tZ-hxzTn4LUbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از زیر این توییت واقعا گیف های شاهکاری پیدا کردم.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/82561" target="_blank">📅 19:46 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82560">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qi-6DANtnTDUItYvFh7VtEUoSZvSG5ajp_olreAURR7VrenSqIRn5mweDOMpQn5TuMrfAx53P-Lk732w9tM5SPefGfDhVjIX6Ul_vDGfno0QoEjQLQSK1J5uB5NRspFi-Juy0HiL8y5A1oDL7Xd5eq8aMICVYvhvCOt8-3oA66k8wfUVrsAuqVGYFSEg2pf1aQnyCaUYvIcQrvTso_dByNjW1q91kMDhTEnD57cOJL145Onf9p0QtaCvVYsLAh2UN0MAw1HxDT6Lr_p7tc32l8TB57rSjyAGPigPoIzh5IEfiN5LswTrToxHjx8BdX1mSWMAfn34GlLRV0G5RodBGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرادر آزمون دیس ویناک به پوری رو پست کرده.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/82560" target="_blank">📅 19:32 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82559">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">به بسنت باید بگیم عمو یا عمه؟
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/82559" target="_blank">📅 19:21 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82558">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fg1vZx7J9vCtf6vOe7JtGFgI8D49--kHqGIwsH9V9JUh-CVMZ9dh9fMAqllvuonLNyOyBaMFhJ0qFDI2ads3MUQa-IFd3C7ZSlEZqsbRpV9lno5q2VBC9eOMbcofeRGInI7N6sWB4LKcjx_Bt0QbzzTCfChPN-ynsg6HVMMHdGi4BJ2iVf6RN8x4nx9765tRGL8JISIR10tHPYYUv51RoGd-atIMoCQY__7pXlUwmbtBkqFGnkqsH5QLsldZ6X8SkPGG7fzG3RdB7W3ol1mssojitN2qxsd8s8Q1P50xeoJog9zY9tUvPrEcNHiC1aOVHz0S9tGg4XMNWIlr8EdWxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ویسکا آسایش ببینید.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/82558" target="_blank">📅 19:01 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82557">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LtMuKUnghAofn6R923vc4Z39_-Zu16Fq9MYtW_agrXsPza1pXHJe22YwfFsqpAVY3xN-tdcWOEKYOCPs3OlDu7OjIAW-VvLx9dfHSuPLzP-kFbC_a5xoSqd9EivNSl7GzY9wTAAT3mVZ7W4vIsv5CBfww3XffC0jpw-rIbXy84XloCvDXR6_E3RB-_Pt8bdulaWFL-l6Vs20_AuNPBYakyRZTUD5PmzrM4RJ3IzfYmdTzmr1QSoz49I5bJ0RR3di5hYg07XliLxneecVt4tRPZfO8mFor6DWxXpwfurlgbYPc1X5DNzsOA8yftMbYNEotx5XDfr38Q4WAP1GndUDkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
بیمه صد درصدی ویژه هفته نخست لالیگا اسپانیا
💯
⚽️
در روزهای سه‌شنبه سوم تا پنج‌شنبه پنجم شهریور ماه، با ثبت حداقل ۳ میلیون ریال پیش‌بینی میکس بر روی رقابت‌های هفته نخست لالیگا اسپانیا، در صورت ناموفق شدن نتیجه پیش‌بینی، بت‌فوروارد ۱۰۰ درصد مبلغ پیش‌بینی را به عنوان اعتبار پیش‌بینی رایگان ورزشی به شما هدیه خواهد داد.
اطلاعات بیش‌تر و قوانین بونوس:
🔗
bwrd.link/LA-100
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
g3
💻
@BetForward</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/82557" target="_blank">📅 19:01 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82556">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BTwjqJhabq5NmEWnn7ABRoOsktY-z2LBqvzc_VtPc_p1YpDp3x8nRhD72JVYWRTQAfGHclLQpu-KVU45LKnEupTGRsKGrMt-VOWstmlsEuUuh0gWrGhkYRuvURVROs7oI6OyAgsA-Isrwncy68YRe4wMm1Bx5F1EFKiiQjKVwrZBbG_D4fk5ZwyOJgFrIhMRd6aiZCIpwuglT5Z7yYmYbsnMVlVnkY05rP5Kf1oR2TA5p3aA9KMIOaMVGFP1LJ2eryKAumS3Ac-PymKUEeuvxVlvWDt33VeYb3JBc-DPEaMlNnQrEP0NLhXo1RrdHnnK8TirLec2vf_f_uuJytr30Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید حسین تی‌ام به نام HESOYAM ریلیز شد.
SoundCloud
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/82556" target="_blank">📅 18:35 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82555">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">ترامپ:
همین الان از طریق نیروی دریایی ایالات متحده مطلع شدم که تمام مین‌ها از آب‌های بین‌المللی تنگه هرمز جمع‌آوری و/یا منفجر شده‌اند. به ایران اطلاع داده شده است که هر کشتی یا شناوری که مین‌های جدیدی در آب‌ها قرار دهد، فوراً و به طور سیستماتیک نابود خواهد شد.
از طریق نیروی فضایی، ما تمام مترهای مربع تنگه را زیر نظر داریم، همانطور که در کوه مکوش و سه سایت هسته‌ای دیگر که قبلاً نابود شده‌اند، این کار را انجام می‌دهیم.
سیاستی مبنی بر عدم تحمل مطلق نسبت به قرار دادن مین‌ها، به طور کامل اجرا می‌شود.
از توجه شما به این موضوع سپاسگزارم!
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/82555" target="_blank">📅 18:11 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82553">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17ebe602ff.mp4?token=i52Hw2lj8eglBws9VtWQkiHjLAjQC3sKIg13mshO8ejVpEJBnm5yjCOHYIKgRc-z1a_qtSWHC1_xvlpZZ6eqXwH1x63280YxQCFEooj4PRLnV023pKLNAHsVQl81csMGz57clvILAsU72Uty02q6BUwoKW_ct3GauavJd5kc76SmYdR9OaSgXnHgqj0dsutVoMdbrzcu--llyWc1Et6Bm84hDCrXMX6RplTF6F0LGA7Oa2qIMXjCdi3WcnwBGWfdCL7dUIH6-4txd8w7bZgMmA-W_AoPxtiR4Bn2DdQbU9lBT8UQdhinIMx19nEmCRQ6ptU4Ij3yGW1lyd8kS3h_UjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17ebe602ff.mp4?token=i52Hw2lj8eglBws9VtWQkiHjLAjQC3sKIg13mshO8ejVpEJBnm5yjCOHYIKgRc-z1a_qtSWHC1_xvlpZZ6eqXwH1x63280YxQCFEooj4PRLnV023pKLNAHsVQl81csMGz57clvILAsU72Uty02q6BUwoKW_ct3GauavJd5kc76SmYdR9OaSgXnHgqj0dsutVoMdbrzcu--llyWc1Et6Bm84hDCrXMX6RplTF6F0LGA7Oa2qIMXjCdi3WcnwBGWfdCL7dUIH6-4txd8w7bZgMmA-W_AoPxtiR4Bn2DdQbU9lBT8UQdhinIMx19nEmCRQ6ptU4Ij3yGW1lyd8kS3h_UjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شایع فازشو داره ها قشنگ.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/82553" target="_blank">📅 16:52 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82551">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WcwkVMSyoEa0MbPYj-3FHZ4V1sK4zhlwkS2zcVnzjmyN1xsMLZEdWG22MqkOGsA0f5pyFb2OB_QPlyGDEWVn76EJhxJyndLpesAPmMg9hzxW4-r2pVCJWvIUV_A3-JpM1rG1CHKo5XjzLMkTPX9vQXNJttTl5LVtIi03LLAamQ7YzgqyYc3ueCY380KUqj3iLvK8WS005jT4k6QzDI_2L1EA-Zr85oiUa2w4xQcgkjvB5S2lID2F5suIIW7zw4-2K2rcASRIssPI6h5IqHe6ocXIglB1tSFgXhZGLPJ0N8oLcD9B5Q5J0Ktd-ekf1WfMBtlOo2WpvYbdg17x4ZnkZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باورمممم نمی‌شهههههههه
پسر ایران بالاخرههههه برگشتتتتتتتت
🥹
😍
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/82551" target="_blank">📅 16:30 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82550">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/adacd9a9d3.mp4?token=RbqGjsdBH6s9D-XfF3dDeoXlX1V2XyYNfEV7Up_LdZ9p16ZETf_vKjITog_7ZkrZdcmaAaFr7f-SZuyIPLswEBupZMQnIS-Qx5Lf1ATXvwZq0C1FW5l9pZJXXzbBYZ4BFyPpyv8fJCiAr0aUocrGhsn81bfCo-aqS_IRotP9x_K8UNTiNlWJs-1m1CtNEJKR25JZvOKKCkeIwH9oTKbEaMeNVmf83TeXZoLmbo2cLqsxESRIbZAcjbXcWgki-MHeMpHcpLef7_mfUt0slNj9biXXGP-ZGU3u9C0Ri5l3m9zlr6JM5QD6EZ1IRcSt5XTPPXbchMSkeQBc0kWNSfzHvg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/adacd9a9d3.mp4?token=RbqGjsdBH6s9D-XfF3dDeoXlX1V2XyYNfEV7Up_LdZ9p16ZETf_vKjITog_7ZkrZdcmaAaFr7f-SZuyIPLswEBupZMQnIS-Qx5Lf1ATXvwZq0C1FW5l9pZJXXzbBYZ4BFyPpyv8fJCiAr0aUocrGhsn81bfCo-aqS_IRotP9x_K8UNTiNlWJs-1m1CtNEJKR25JZvOKKCkeIwH9oTKbEaMeNVmf83TeXZoLmbo2cLqsxESRIbZAcjbXcWgki-MHeMpHcpLef7_mfUt0slNj9biXXGP-ZGU3u9C0Ri5l3m9zlr6JM5QD6EZ1IRcSt5XTPPXbchMSkeQBc0kWNSfzHvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خب این الان یعنی چی؟
😭
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/82550" target="_blank">📅 16:16 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82549">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r1kCQdEHXcSqDyyRIy0Br2wi1PjLPwZtbUL0rYpcH-bpuj6HDsCodOzUab1cFSvOkbIxfZ3ax0yDGFVmatMc9saDo4Uf5Onumwyg3gzUOAKJldM7bE7W1ZmKp7AXxpGKu7vyg2wSYzdTmDFcRrLWUxqClFq4VaD8KloScSu03nq5HgaLup5h9tohezz1gJ4LWOCelP03Hr3kFEBGKF05CwFMN2UBAHsyiHdHDJSrLILJbtohjrOk0WqCXdCqPKAoXTts0x_2asR6LeekaI89ueylN8KIv-JcQdIff9O0knpQAF6VYndyGVp_YN8GFoZigqUsfJYYgmgEzVB7y02Mpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زیر این پست عکسای رندوم بفرستید. ۹  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/82549" target="_blank">📅 15:22 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82548">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DAzIEUX2wD0MEujVtLRi3Lt0HAPztvrLgo2_ZzMB2aVQh_wpAcGnRvoE_wkPymzt-FUMsYgjEpU7mDFjFr_GdEW0rz3XKxJvi54ChVL-6MX_6jTaEqmoL3IcfmOYhWvCZJtZqXo8Z020ei2CPhHknDqcTRMyHuw0o4j8bqff9uqeiRGvRCh10AgcNldD5D91gL9X_ARRLO_vXzK2Wu2i-Zdfx351fcgPVrpxnk9ATLf93uKmwJLUIpp8UCROCCl_hMQbZt6_Gtev9am1oDHk2vcIxqMqAOrnsUioPvES6iRtUI9FUcmjMUqUxAnadltb2UdBNtadZ-g9CCpBeRl0KA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این یعنی دور جدید مذاکرات؟
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/82548" target="_blank">📅 14:45 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82547">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">کار کنید حال کنید حال کنید کار کنید و کیرخر.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/82547" target="_blank">📅 14:36 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82546">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fl4XxJjMX0HxjrKkZy5JjdOftvd0yjSXlImetYsUUrBtfp5_Uir9R2Q_mzUgIONyQhZSiisPXEQp5aSGQv-GK8cO4aQ67gVZfjq2NiN7ux6F_aB9o8hV9LuSSNwqSaxAvxeyK6r_4LSK54_Eqfroj4sZmlGmezBiXDoS9cc9XKXnB8TwKCnlegvlwMPRuH4oxVauB-0u6ZsMy4a_snbeYSht4YmBTRCt7o8tqiiRxpF1aXxsDx8ieZ6Fp9_7E1bv1mQ6F5mlEXQc-aqfdGtJDSttXbQTFnlsTwCOAGg16RrdM0jFvv5ltvEqOOF4fA-wCBWLvd7wrPb9QHYN5wdaYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه عکس دیگه از مهدیار لیک شد
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/82546" target="_blank">📅 13:53 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82545">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9968bc181d.mp4?token=H224xu5Z_E87-bfjX2FBeS9Eq9OHxY_8ULtDLuMYtMjQ_akuLKwSIzCl7ffP_eFpnV-YPN6jGIXec8iIPKFwZWzQbvNAbquPuGpLiU3c5ktEkwixDbN4mPvmRGxNYrtkKwWhbWsgFpRAByHdO-QIL8vGKy2E3fJDkkI0K1Z4KIc7PD7TbLirejTIRowmhjcDWw-kLFFdjfiuzA7fcvrw-13Wh7vwnuHyFqUVZMj7nqSsMgrQ70TKYd4NpoBdB-qJ5RJVaDEUH8cNL4ZpEeYGNZ5fy-Jt8Nhj5Ahl1Xbmxc3aD2Q9YT2os-O0njmY0D4jg904XbGorxgFajcspZahdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9968bc181d.mp4?token=H224xu5Z_E87-bfjX2FBeS9Eq9OHxY_8ULtDLuMYtMjQ_akuLKwSIzCl7ffP_eFpnV-YPN6jGIXec8iIPKFwZWzQbvNAbquPuGpLiU3c5ktEkwixDbN4mPvmRGxNYrtkKwWhbWsgFpRAByHdO-QIL8vGKy2E3fJDkkI0K1Z4KIc7PD7TbLirejTIRowmhjcDWw-kLFFdjfiuzA7fcvrw-13Wh7vwnuHyFqUVZMj7nqSsMgrQ70TKYd4NpoBdB-qJ5RJVaDEUH8cNL4ZpEeYGNZ5fy-Jt8Nhj5Ahl1Xbmxc3aD2Q9YT2os-O0njmY0D4jg904XbGorxgFajcspZahdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تو عشق ابدی ورژن آمریکایی یه دختر ایرانی به نام پارمیدا شرکت کرده و اون ته مونده های آبرومون هم برده.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/funhiphop/82545" target="_blank">📅 13:16 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82544">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec8056f1f9.mp4?token=mRL8i-7Tq5WBPW9GBNjlUlfTiuflUcgrlJtvVLAPZl1cKnGAkHKlE5rA7iLUBY9WTFs0w6dlc-MGSCa9bIdXmWS2q48DRXicaIvY_pa7zsncsLqiLISwAoBuUUFv9pB1A5AIK2F_rqKMZ2zQaThUE0Hyapq8Rz5Lt-30KfX1wEF9q-PWrsVMIV24BKaH4bXozvVbItQYf-eR5EkVWVwSApFz17YG1Kl8XmofYoD_7klrQvmUTgFHJMlTKgxN7HncIedVdBQRkbZezCf2VB1fvFwmzb80q87AF4WMKWykHX7iZ58DzcpYGUhJsO0FjI_WMFXgBDnJxYW__LCQbODkLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec8056f1f9.mp4?token=mRL8i-7Tq5WBPW9GBNjlUlfTiuflUcgrlJtvVLAPZl1cKnGAkHKlE5rA7iLUBY9WTFs0w6dlc-MGSCa9bIdXmWS2q48DRXicaIvY_pa7zsncsLqiLISwAoBuUUFv9pB1A5AIK2F_rqKMZ2zQaThUE0Hyapq8Rz5Lt-30KfX1wEF9q-PWrsVMIV24BKaH4bXozvVbItQYf-eR5EkVWVwSApFz17YG1Kl8XmofYoD_7klrQvmUTgFHJMlTKgxN7HncIedVdBQRkbZezCf2VB1fvFwmzb80q87AF4WMKWykHX7iZ58DzcpYGUhJsO0FjI_WMFXgBDnJxYW__LCQbODkLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این روال عادی ایرانه، الان دو روز دیگه باز همه یادشون میره تا دلار ۲۵۰ تومن، اون موقع باز جعفرزاده میاد یه ادیت میزنه با آهنگا محسن چاووشی و شایع سلبریتی ها هم اونو اد استوری میکنن.
پ‌ن: البته خود این یارو تو ویدیو حرومزاده ایه که دومی نداره.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/82544" target="_blank">📅 12:52 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82543">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jMvVUM41NQ5-cDfzEBeHkbdgAEszdYW4M2o2j7TwUG14nGVBrCfaWET4DskiZtMyi-XA8WJ4UatTpRx8oXxpIUYtLlqpzAA-r5wCqpwsP5kO_-QjmC9IWdOdmEc816cnjVdNIepilLgGRsMx_SIJO49O0omvUpOSI1m3qJmfrN7EUdt3F1XKccDELWucct8kpwznta18NyVjIFlLe_0i_MSvReHzS-tLz113beEPi24ql0R_V0C535-KYxibD2iixlwbEdzV2joIs8-SiPe6LNttlHysrOODkzyZ59KlzowHwhxL8eVTS3ReVWeNSol8Q-cmbODEsiBBxkLyE7niLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
بیمه صد درصدی ویژه هفته نخست لالیگا اسپانیا
💯
⚽️
در روزهای سه‌شنبه سوم تا پنج‌شنبه پنجم شهریور ماه، با ثبت حداقل ۳ میلیون ریال پیش‌بینی میکس بر روی رقابت‌های هفته نخست لالیگا اسپانیا، در صورت ناموفق شدن نتیجه پیش‌بینی، بت‌فوروارد ۱۰۰ درصد مبلغ پیش‌بینی را به عنوان اعتبار پیش‌بینی رایگان ورزشی به شما هدیه خواهد داد.
اطلاعات بیش‌تر و قوانین بونوس:
🔗
bwrd.link/LA-100
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
r3
💻
@BetForward</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/82543" target="_blank">📅 12:52 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82542">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F3exOlHocJi0xcMgx35zAJe_btBokVolDmp4g90ors0-nFSN4Wxt6gweWpODOPcRjk1JMkIkPEV_sTE0_TnON2S4ftfjKd0NOBiQ2UN6ksxNzKNQDPsf5gwGpomUdli3eJIEEkclzDUg2I-rjUSgnuSgH3bgcMYgT01Iyo62M9cbG5nlyq4y2vH_94bLZz5QjHPkfkFrBTHoqdqzbdGnxIFmjOvAwxzEWOVjrnjOTVjumao6kr48c62WuKRKla2zaKDyYSgRI_8952LxVvpx_CkKd5fXdYJaMTxsV_bBFpmjLKnGf5JQGPSUlk1kq6CMDZbQbgU_i2UKfLTjH31cbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری نیویورکر:
دولت ایران به گنگسترهای روسی و مهاجران آفریقایی در کشورهای اروپایی برای ترور، ایجاد ترس و آسیب رساندن به ایرانیان مخالف مقیم خارج پول زیادی می‌دهد.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/82542" target="_blank">📅 10:32 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82541">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZC9U9DiLuemFDfCsxJcF-liiJPXM4LRnLTkPgJvk8buMQki0pszRH-MC7_KpxfDBedqMRz7JQNIgPPAyfuX11zSDILbt08nAGGHHq-hSHAr0RlWOYju9TJ2pG-1jrnfboMYGqYI8ulk4InqondRzuU93ZBczqcnQG8HYzvgOmqmTiIv31u30gfUyOScdHqDWE2sdXVgpV9Gzu_hgkpNLttnhaBl_qrc4mxPVPmvAORwQtOMI0CRmgmhy7wUH2lxUicpy5ir4xv-vq6mWm7KrIFZbS_SigYrr57viBWuF8z9c_qtkYXS9creCjXxHf-xzBBJumvdkmocAGDOtjah3Rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/82541" target="_blank">📅 00:32 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82540">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">همین فرمون پیش بریم مردم تا عید رفتنی ان</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/82540" target="_blank">📅 00:17 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82539">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hA7upt-EsaHqSv9-fk9Gb27_bCxgOHw1WaR6pXD0zU05AOTCmc5bP3hE0cX38kEy51zIQR95fJ-s6TB5FCxHabpiLMAa3FXNym4-ZQQwePb0iSGj3tCSv8pLTpfuv-AwTyNUUbgk2c2CkskRyfdqrXXGK4tP43uosAYmKvVqgQoKt1RqI9veki01KvB-cEtsTyCzIBAsLk-0JA6x-k9sleNOb2kgM5jyjtlZ9lNc_qMCZAVz6SxYl4bXtQRILUU_iZ6DavYfU7X3lHIGoH_K9TfNXN3d1Th-c1nvJCrhtsiGDB1zoRENSo45H9WBbnloQ50WdwsqfnurdWWRJIAUoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت خارجه آمریکای جنایتکار شیطان صفت هم تا ده میلیون دلار جایزه برای ارائه‌ی اطلاعات از سرداران عزیز سپاه پاسداران انقلاب اسلامی گذاشت.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/82539" target="_blank">📅 23:59 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82537">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">عاصم منیر حتی نذاشت حضور پر مهرش تو ایران یه نصف روز بشه و چند دقیقه پیش از این مرز و بوم خروج
(فرار)
کرد.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/82537" target="_blank">📅 23:43 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82535">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LStvQ7H58JJ6Jfm38EYimIWdMq-omLob3z_Y6xfg6l5vhZfSZKLuV67r_Q0bP9aXDieJvr1--FkiubGXkTWjOUiY964V49wEPbiMkD5POiU9zex9QM8H9YMVnzkYisM_f7vjwUFn97O_SDumRGoRkSUnbeMxCbMcDNaCjkaahs1IY4AUGdrpuYkkN_aUDzE_GFKeMYGlTyUYyYL1JNBMSW4U2vLEPXr9FM01oisVCmGuoDqCLAItHcFxhQ_44EuhpwIIIjfvR4_mrUXDI8L8dHJ17uqESTLN9gSH2jJGEw6Xn-6W-1rzkHLY9V5-xK8kc43ujRwV5Q4mUhDvImsgPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fpKfo0oemml1_6f_TTR7FVUVp5wZLY5y0S0D6jAyk4ewD50VJQgLuJEci9GeYY0If2gjgZ4a_c3PGtYKjaFNSlDabl_F5x5b1tEWwMG2w3nNtI8WnUHeHtKkFJBaFbswjVHkYcVHVmpl3B61jzX-9zo85TAvH1GPdOoCGV6oBsVfCTMlbBdaV1pNCHXBtdZ1YTqXd4YWKNj3xBG88asPmYeMm_YxeQ6EbpjJE9wCqhgzI1WaqvDPwEjsal4cldiik3p2thRFbnT5rOyTvTxqA-EOz3TK9FT1hqfFza3d2mn5_LI0GugeIyYb5Tb95zZBWd3YxSmrDcmC4wZIcii4wg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">به این بنده خدا واجبی دادن گفتن رنگه مو هست
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/82535" target="_blank">📅 23:15 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82534">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41ff961f21.mp4?token=hBq1ObNBqU74ujPVxo7uqVqVfaiYFEZCtFqD6Ws-BUKxd_up539z0qHF6-gD5xkXmqpIdYWQ4xuhy_fusORK0hZoplLpDJdKAmtBcWSWtDbDGNXuWIshiit6ONiGa5G_ZFrCx3XCaaGBhoaKvI5leYHgupWSSyHA_ZC9gU2Z0k-KjEukYaNbX4AjNRzzx5aKLfDCkd6cSzXCO44E_IMJChRXK3iQutLhVnCv-0YPBWxyXEK60T2K9Qqyc2FFbPy3894d7IlevMo5-MUDlwvB5x1V_cwFNOGYeiZDuPrRaovmaDGoVUHd0utL-d38k6yRryk5x7Z5wR75rKFzH6xpIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41ff961f21.mp4?token=hBq1ObNBqU74ujPVxo7uqVqVfaiYFEZCtFqD6Ws-BUKxd_up539z0qHF6-gD5xkXmqpIdYWQ4xuhy_fusORK0hZoplLpDJdKAmtBcWSWtDbDGNXuWIshiit6ONiGa5G_ZFrCx3XCaaGBhoaKvI5leYHgupWSSyHA_ZC9gU2Z0k-KjEukYaNbX4AjNRzzx5aKLfDCkd6cSzXCO44E_IMJChRXK3iQutLhVnCv-0YPBWxyXEK60T2K9Qqyc2FFbPy3894d7IlevMo5-MUDlwvB5x1V_cwFNOGYeiZDuPrRaovmaDGoVUHd0utL-d38k6yRryk5x7Z5wR75rKFzH6xpIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این محتوا مربوط به رپفارسی هست
‼️
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/82534" target="_blank">📅 23:02 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82533">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2adb2d63f7.mp4?token=Lv_Vpy1u_rgvt_zl0c-Bu2-HxNP7ud4uWFvHGWSGxQNBD0EYNdMWIVh5rRAeEZFTrlLBUsu2jFgfbV-OcHrbOXoNeusYGJODg2AkSKSiyBmiMpIIXFVgTYUZezkZzp18w-VBC9-r1JjnqkJAxsmJ2OPVrKGIs1fLfiVG8EHl0x71ghgwgfuDvNkX75i6GKyvHtCTLttKc-23Uqc_AJDqK4vZnHAnEcBrq8JCYJRvvfNbsfDUMKp_ZAgMnn6vx1Ml6xlRTD6T2mCvTfNXgjB_GwMPjyCOECCLnv6VbYNo8ewN_G3Z-9wfNYSs-2fanBPIUZrqLYY80TM38ZqRpaSghQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2adb2d63f7.mp4?token=Lv_Vpy1u_rgvt_zl0c-Bu2-HxNP7ud4uWFvHGWSGxQNBD0EYNdMWIVh5rRAeEZFTrlLBUsu2jFgfbV-OcHrbOXoNeusYGJODg2AkSKSiyBmiMpIIXFVgTYUZezkZzp18w-VBC9-r1JjnqkJAxsmJ2OPVrKGIs1fLfiVG8EHl0x71ghgwgfuDvNkX75i6GKyvHtCTLttKc-23Uqc_AJDqK4vZnHAnEcBrq8JCYJRvvfNbsfDUMKp_ZAgMnn6vx1Ml6xlRTD6T2mCvTfNXgjB_GwMPjyCOECCLnv6VbYNo8ewN_G3Z-9wfNYSs-2fanBPIUZrqLYY80TM38ZqRpaSghQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فقط باید پسوند اپیکور رو اسمت باشه با ۱۵۰۰ دلار فلکس کنی، خیلی پلشتی ایمان جان.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/82533" target="_blank">📅 22:30 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82532">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VLxXm5zE4lRl1kVr5b-DmU_WX94PZS6VK1SlIft6tAdbT61UNkaN4CQ-8zHRYhZt2auMeeHRyeV5KNoUQX3Bva-IZN5d2rIgK0CHUmVmx1IDbVTEr4jJzLo8Yzuysoe3FXbOCQMMRx6IglmMNhfE1ph8PCqY_iikGqYEr1HrxtUqZQeJOHkLsQ82rnGG5HCEy2yRr8SChqE-1bHeS-3SM9kUNRWLpmcob2VzLYamauzlmUjPVbUHJkyrbokbvFhou8v1avKIBVg3eTMUFzPINWvmXR2VES8IYs_DosoVPlvAkVg1zUdGJ7w5s5qjja0ycRJe84J0jkTAYDYnlfn8aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کصکش چطوری از دهه ۶۰ فیلم گیر اوردی
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/82532" target="_blank">📅 22:04 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82531">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oXYfgD-Fv2Z2yxyJk4dfiNQVIE01_CdW4OK-FhNCTi813s70UoKa2IFQsomJtCNMEgxAbMqiMUSMw7j1fo6CSwXSAKdMPUwLrhZs-WCeHQwlFel19jrjrKzRcVZXdtOb_tMO27TweKt3T0-ipyBU59PkStys0i36DHrXyJoWop9CDSP1XzAuqtKM87aFPtApZEkA-p9jbJljZDeXJLK7TYnm0GGl4IphBWwSiOBvegg7I7bULZWpa_3uIUXWraFiZd72WoSmkawAYJ3nKzGj9CMpHaRGYVzvKy0tgyvTwych44V1vBVFgwGtMrjaqfdWjfrBA0M2kSZ5l6DBT07USw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ با سران کشورهای جهان تماس تلفنی برقرار می‌کند و از آن‌ها درخواست می‌کند تا از هرگونه تعامل با رژیم ایران خودداری کنند.</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/82531" target="_blank">📅 21:12 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82530">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KDhHl8BW9MDOA5m1C3Um3ivnIquQBKRX-074H2g_PwLM2zufduUwUlisYfbCGAROe3zDvIlF0neCZyhwfA9geQ_rJ-ckK4pDZ7oyrTv6mLw_nrafM5uhZeL16AmcdcjJY_U5OxqDvNaV3LYAAVIemMiFHWCEdNs8tl9M960PZBB_RAR2WEU1Tab2hn2EfJXpGvUe-sUItdg0-c-pPd3Kf8bbzW57xtdxMMV90b8cX6S_JIA8KT1rr4iNCdliPpUN-0qomYTWUBwWWp395ebcXs96dPHS11W1xH6xe5Xkc1yMdYOwDHFpW0yKYfXfgWDXA0d9BI4Ohg8XlClH-VAe1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر خزانه داری آمریکا به دلار ۲۰۰ هزار تومنی هم واکنش نشون داد و پیشبینی کرد اگه وضع به همین منوال ادامه پیدا کنه، دلار ممکنه به زودی ۳۰۰ هزار تومان رو هم رد کنه.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/82530" target="_blank">📅 21:02 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82529">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">تحریم‌های جدید و شدیدی که ترامپ می‌گفت توسط وزیر خزانه‌داری آمریکا به صورت رسمی اعلام و شروع شدن: امروز، وزارت خزانه‌داری ایالات متحده، عملیات "انزوای اقتصادی" را آغاز کرده است، یک کمپین بی‌سابقه علیه جمهوری اسلامی ایران. ما یک عملیات اقتصادی گسترده را علیه…</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/82529" target="_blank">📅 20:48 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82528">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3789f0e9a7.mp4?token=ejkAuLSIvkyde93pwjAGYYr7mEQGNm0MJ8WeV3KNbkTn-0GwqX4UyLLUvfC4W-RBpQqaRi0TRK3ZwGx716YhH9YTrB38oLIieM5fu3-7jqO8nfBmxOKNwbBvCEJIE92POfSgzOpw_LZBE5ryTHfQdYsM7yuSc--8tS85NswZLwq6nWXkK91pGDVsNjuac37gctIIepiY2_IPlI0LAOgyynoSf_-Qp0z9sciBcsT8LNLE-AZLtY0XWKuWq8AQ9LuHL3jJRMs4Av7hD87nPGEKJg-wBB6riFsXQX921q5Fc8kYAmG82iW1AbF0SOVY5y8hJHx-7CKLSsnmFljISMRkzoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3789f0e9a7.mp4?token=ejkAuLSIvkyde93pwjAGYYr7mEQGNm0MJ8WeV3KNbkTn-0GwqX4UyLLUvfC4W-RBpQqaRi0TRK3ZwGx716YhH9YTrB38oLIieM5fu3-7jqO8nfBmxOKNwbBvCEJIE92POfSgzOpw_LZBE5ryTHfQdYsM7yuSc--8tS85NswZLwq6nWXkK91pGDVsNjuac37gctIIepiY2_IPlI0LAOgyynoSf_-Qp0z9sciBcsT8LNLE-AZLtY0XWKuWq8AQ9LuHL3jJRMs4Av7hD87nPGEKJg-wBB6riFsXQX921q5Fc8kYAmG82iW1AbF0SOVY5y8hJHx-7CKLSsnmFljISMRkzoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تحریم‌های جدید و شدیدی که ترامپ می‌گفت توسط وزیر خزانه‌داری آمریکا به صورت رسمی اعلام و شروع شدن:
امروز، وزارت خزانه‌داری ایالات متحده، عملیات "انزوای اقتصادی" را آغاز کرده است، یک کمپین بی‌سابقه علیه جمهوری اسلامی ایران.
ما یک عملیات اقتصادی گسترده را علیه ارتباطات مالی ایران در سراسر جهان آغاز می‌کنیم.
هدف ما این است که هرگونه ارتباط اقتصادی را که این رژیم مستبد را حفظ می‌کند، قطع کنیم، تا در نهایت تهران تنها بماند.
از امروز، ما فشار را بیشتر می‌کنیم و هر منبع بالقوه درآمدی را که به تامین مالی سپاه پاسداران انقلاب اسلامی و رژیم ایران کمک می‌کند، مسدود خواهیم کرد.
هر سازمانی که به هر نحوی، فعالیت‌های پولشویی را از طرف ایران تسهیل کند، از سیستم دلاری آمریکا حذف خواهد شد.
دونالد ترامپ با سران کشورهای جهان تماس تلفنی برقرار می‌کند و از آن‌ها درخواست می‌کند تا از هرگونه تعامل با رژیم ایران خودداری کنند.
ایران تنها دو مسیر پیش رو دارد: انزوا کامل در سطح جهانی یا ایجاد تغییر و بازگشت کامل به اقتصاد جهانی.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/82528" target="_blank">📅 20:45 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82527">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">قیمت روز گوشی   @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/82527" target="_blank">📅 20:29 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82526">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MNRfjsl_UP7deZh4yxs86WaMAow1JVOo5C_N2Ax_p75Mf1wRztZli2pgkbd8YQGQCQRf6eMlB9uVTO4a8ySwXSny3N7jf64NR7vgpLFKFKxmyci50z8RwRmQeug8YSvyRG8O8wuO5ZNH9WPM9w9HICRHdS00JXLD5DuXE-2Rbzj4B0wf0wKzxiXUaji2LbYuYS7pwMIhKLsSWRjN2SoKPj1W2XKqbS5JT3d8jdMOee9S0F3cO1BRWzexbVLlu7JY1CxyoX9E4q_rxZ9W6e_At2kDR6pIyYTyHhWFwHM52zWNCSJDaC3tfT-AxW45ka9YZRrsfjtauwO0z3pPs-U-_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت روز گوشی
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/82526" target="_blank">📅 20:20 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82525">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">از تهدید کردن فک و فامیل ترامپ با زبون فارسی تو صداو‌سیما منظور خاصی دارید عزیزان؟ زبونم لال دیگه اینجوریم نیستید که مثلا انتظار داشته باشید پسر ترامپ میان برنامه‌های ضلال احکام شبکه قرآن رو با دقت نگاه کنه و بترسه مگه نه؟  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/82525" target="_blank">📅 20:16 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82524">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/8b569772aa.mp4?token=W2sBEF_rkcOMEXU5aNnh_npiMLMEe6dUD9MM3g6s1BcRmZHLOZT2dK1Q6RFIUKEKRH77viPywbWAjaPtS4ACrFvWpb4ai02pBy9ZucZw2UehnXmCsPFa0ER1u9UVrrTaCSyzOmnlgehDilKrMxXZ9Dhb19Koe7aCB1oHDzaMkDh3XtDpegVQERppdoNpww_UfsdPwKYAbeCJm3kmNIooWHYoSHOmH6XoNV2e8dloO12cyRY0IPC0RQVKJnGS9HX1aw-qUDnacXfqAGu49i8nJ-MbE1n7Qn9vvswGKAaP5bIhlhc1GBurDIvcVV85UIiwUE4DooaeGw9QPZPRY_-ZKw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/8b569772aa.mp4?token=W2sBEF_rkcOMEXU5aNnh_npiMLMEe6dUD9MM3g6s1BcRmZHLOZT2dK1Q6RFIUKEKRH77viPywbWAjaPtS4ACrFvWpb4ai02pBy9ZucZw2UehnXmCsPFa0ER1u9UVrrTaCSyzOmnlgehDilKrMxXZ9Dhb19Koe7aCB1oHDzaMkDh3XtDpegVQERppdoNpww_UfsdPwKYAbeCJm3kmNIooWHYoSHOmH6XoNV2e8dloO12cyRY0IPC0RQVKJnGS9HX1aw-qUDnacXfqAGu49i8nJ-MbE1n7Qn9vvswGKAaP5bIhlhc1GBurDIvcVV85UIiwUE4DooaeGw9QPZPRY_-ZKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از تهدید کردن فک و فامیل ترامپ با زبون فارسی تو صداو‌سیما منظور خاصی دارید عزیزان؟
زبونم لال دیگه اینجوریم نیستید که مثلا انتظار داشته باشید پسر ترامپ میان برنامه‌های ضلال احکام شبکه قرآن رو با دقت نگاه کنه و بترسه مگه نه؟
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/82524" target="_blank">📅 19:52 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82523">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T6jHjfosF0tNgbIYEXIRqqHNkNu3Eo0wS8CvEu9gttVazZXVmu90xslRtBHMX5Qora8VSjAvSCb78iITQI4Gj0M_XICCVxOSTsQY8jaWd8YwaDYIkfGlQlp70i-_CRVhNemeBf1DSL5LJgBo36-yTz5OazDzY2nmyDBvae4LqVnIB4y1SkJWD4iCkyKQVomRr-3CHq7osenA__XVaJvFRK3YWCz2P35nCtZqqxEQ9HQAZ7mDu2JjY6fCd2YvPL8ADGyDvysLHVILT97Xsnt7LglGdRdXoDwv-P13cWVcxFWin6PEHpqYNomcFVuUHCbnQ8GDnn6qIhU7w4FYBOK9mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مردم قیمت دلار رو می‌بینن، نادر قاضی‌پور از سیاستمدارهای تراز کشور هم چهره‌های جدید اینستاگرام رو.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/82523" target="_blank">📅 19:27 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82522">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/482bcfbcff.mp4?token=CIhfPaQ5UKe4-dcJPHm1yIfz4GwqpGWENRuBAPvlk7UjjYlkbgteFjGXwtbCYdeEAyquvk22xKgEFXUvuO7AbV7S6IwKYx4_8Kk5m7oXEnAbaZcBbddEXE5qA8ZnenoDbXafQfbaX0nAkegsquN4aJiCJt_2S7E74rO55VJMMkLMBIOtR3a1to5D6HApH288ZEUgHZA3yVLGu-z_L5V2psPjgqn5Hvlb3x2WAhl3C_cDOl7cIrdFHDhA3Yo1oxa-lf1nPywiaDZWgFtPUto9-7rPZlOgmL3pFmesEODS1MS3k6wf9I0TFEksgNAPcOmhyTPPremllJf3mhIl7r4F1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/482bcfbcff.mp4?token=CIhfPaQ5UKe4-dcJPHm1yIfz4GwqpGWENRuBAPvlk7UjjYlkbgteFjGXwtbCYdeEAyquvk22xKgEFXUvuO7AbV7S6IwKYx4_8Kk5m7oXEnAbaZcBbddEXE5qA8ZnenoDbXafQfbaX0nAkegsquN4aJiCJt_2S7E74rO55VJMMkLMBIOtR3a1to5D6HApH288ZEUgHZA3yVLGu-z_L5V2psPjgqn5Hvlb3x2WAhl3C_cDOl7cIrdFHDhA3Yo1oxa-lf1nPywiaDZWgFtPUto9-7rPZlOgmL3pFmesEODS1MS3k6wf9I0TFEksgNAPcOmhyTPPremllJf3mhIl7r4F1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مردم قیمت دلار رو می‌بینن، نادر قاضی‌پور از سیاستمدارهای تراز کشور هم چهره‌های جدید اینستاگرام رو.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/82522" target="_blank">📅 19:03 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82520">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bQjGRpFsLvJFUv-NsURxLkyN7i1w6MTZB7ULy-oblmuG2fRDcAj2r6QQCThfOEkZfnbe9qg2TAOPKu4ts0jRWnPh9mN28ba2vcsKtVL1FbaCnpphIF5Z0a0-PwlF8o1irdsh_1XufXvfWqfCmqNGZLZQRiXrNBRUsIz0ThY1ii-LOWEHKhaCqq0hFplZpukgE_63UTeFGBC4eC5hAwm3rQxE8CoALGEbmJkgT2qBeK9c75jRcKWTtaK3FJaUShAmgFoYYdSzXyi8m97YyffCWZf_4FyOlRu44fgagni0cxuOZzYN4D_TMvwUM6BE73amA6Ks21Vhux9jxqRgr-yORw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۱۰ تا از پولدار ترین اشخاص دنیا
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/82520" target="_blank">📅 17:55 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82519">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bm0RZ0e1Op_sYJswXCfp4-Ez7WjRMFqcwNpyxYUuEV5M6dvDELthvfBg6-7blcS2riUPLZR3Psvxlq9XoHFLyktQyHN-5nbRYlpVEKVzDcl-ICXxgID1S3a-mtoGcKwWvXvz4G6imjUfZO9ou0Gz85q2M6MavWNtshMUaBNoD0w1iohouvBBW7Nc89iKROnC_iC1vAwywon6A2qI95Ohna5ZmkMaO8HOE6Uk0r8UI44sbKV4Kq7XiUPuUuE_oDzn-y__GvSET5fIS2dhGV8EaEQr7mZP0fp-InvE_TIv9251nhJvmvhtZRYkQEcmQH_zRyM3DsRTR9UJ2LiesTYMkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بسه ناموسا
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/82519" target="_blank">📅 17:03 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82518">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">این پولای عوارض تنگه هرمز رو کی نقد میکنید تزریق کنید به بازار یهو دلار ۱۰۰ هزار تومن بکشه پایین</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/82518" target="_blank">📅 15:25 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82517">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LrapLMzKJVrblaw7Y01Y5IkBFzPfJfjjbXxBBC3MN-V36G3XPfsQEsQ9fJcKP-Q_D6LN-Em8Qjpasufcy1C31M0LdJiigM9aAdonreq2dOM6Q7bEHAFLuv7wcw0dsl1eABq-gkesTmuxxGOfPlOd8Dpf_hCA2P7wBiaMTtvnISZoCi8amOv1rtnnTLWPMmK04KoasNPva75OYjnCVtArWrhD3Of7marirrOmVk919VwUmLZQfS-x_6uX9zwJc5OPWFVxdksdTTjNUGRKW92XJzJEq_sLL0dYE0uSozFmEep7-yurXCR0WnAIzD0HtOzddABIcU4BihL8Mn44byhj7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمید رسایی حرکت کن.  @FuunHipHop | Nima</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/82517" target="_blank">📅 14:57 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82516">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">برای همینه نمیتونم از خنده بکشمتون.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/82516" target="_blank">📅 14:47 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82515">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KY9vdWZ9nk7WDoO1eSwVD2S1TjQhMrdcn7thIqb_CMw6Snw1iMw4f9wMEWPbpU69UviFlioiQrR1sY4QJ3RA0QAQRll7ui1KuLPKye4D7TgF-LVwtUKpwXbFCw4Rzri6OQhza7-D-9cGEd9C_S76lDxiKlSeth8SMP-2X9YL73nVifprpf8t1Gxq_5Sw81s6ROIz7h1b8EC1Tzg_FvfzCoDo9jcA4goFZrh4IB_nmiyjwmXDYqGV8x_sqYr16Po4vPz6RGnrbSzzoVPhj_5fStlNLh65ICr64OH2m4J2PPXA3FHuKEdbyErSvkQH7lmVPrfTht9wCiOfbAUQA_0Low.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای همینه نمیتونم از خنده بکشمتون.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/82515" target="_blank">📅 14:08 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82514">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j-UvNDlkeChiz5hd9wWQVMbK45Ky2P5yLYvH6au4IydSRIEkzQjxm3dIcrJCk7MLc-vsXSf08hLKlZS4eVszslB7tzrrGPyd0K8BLyKlmJcSMgtXyqElsTPglKR4ODUj-c5NkBempau0PTFnfOFXR_kqhrU-vdRlhWWzGpAUeiurpJ2RDlqerfY-asETLuhK8xjUtcJtCmtjOCSDsI2J_auYLW2Ef-Sw50mdqYFcp3iizkt1fSk-tbFvtpJpddUhrTHVxJwb9U_MJ-R58jWBUB2yEFAED8q_hK3jnEPA2r2Diso3RSYDg04DDbVh8qDAUWbLlB37eKGXGnsDcC4EFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اندروتیت دوباره به جرم تجاوز به کودکان، پورنوگرافی، قتل، قاچاق اعضای بدن در میامی دستگیر و راهی زندان شد تا بهش بگن کصمادرش چه رنگیه.  @FunHipHop | Menot</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/funhiphop/82514" target="_blank">📅 12:37 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82513">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FSlZ4VM-7qQty3Q86NlfpUb4IDdeZiStnrGw_t7UqIgnzCQfzrXhfSGPw3DhvAM_Q1h5y4e7unlULQTMsrfpFpq8QN3fThw4KHO0VBQmPecmTYtxcC8KiFM3zIJckClvhBaNIwP4ibffJhtoZehh0EG39wQLfnCqk-Jy5WoV45nqh8abpvcTiNMRYk5T6FffiY5htNaGL8yHWK9LqsApPmO5ta3_jyM-0JPX0DF0wJFlgaQ1NN9wh4jDQmOxQUoGVs_9cMoJKnVX2tPTnDh1sUIcvUs6odNci1tZ2fkcLP0BWR867mNahH7AFs29BcpP-XV7f_euvO_XTDOtLV2w9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکسال پیش.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/82513" target="_blank">📅 12:01 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82511">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lN3E0WZwl8yEIzmEyEIEnLvKgauOnymK0PpqONheA-bqVeM_qMTY7N0kRHQ797asKdtgoJKepYzJHXa9C63U64QpAMJulBKZU2gylSxFAmPm2nNp7Wf2hbKwIWZB9Qg2OmkFYYApbigTi7dZUNbna2Jk0LzcX_-J6QvREJFm_gugSSY6SFKRb1SZuS4vbvzzmx-z8okcyXbOUc9e-BX12SabwQW5lLBJ9vO8yqXCKYMZfJK0uOAhufP3GlCsqhucZn66KxVs5EqrNPgA02lQnNP5KioMbsAYILUfETowWNeDulU3touHr9tn6DDJCbpfna8q3bWDsdLzjFpMPl3EwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مطمعنم تو این ۲۵۰۰ ساله کلفت بودیم یا ما شانسمون تخمیه به این روزا افتادیم
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/82511" target="_blank">📅 11:03 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82510">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bo6xSbv6COAzUpyCNjz9s-2p7EWqoUDjn8qlOgpEgGuFy8ytOYhPnmOymTJjiTgiw0oifvVTp4d_346OLpP1ovlahj_yM3mb4htwUFi6lWMdx3c93SN3RvFLXzbQZVEIq5ttPKbx-F9veXXZeD5vdnXmC6omeqpslQYtqL0u4UxrPPYRPDpYYHHauS0poF9qPuWBKAevv3UxWzIrbiPI10CZf2ywuO1jcwZBjR6DfvkMMDaqEI5tW66f_vge12fXsEn5gwgLWUmDbm9ZCcuP5y1bs6feZcuUSJhCvTRrtX-x46LBW5zgHB84TAfm77O_W4O6ngqfYelYkkiMknwyDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمید رسایی حرکت کن.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/82510" target="_blank">📅 09:48 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82509">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uth-O5l3aeufOJEJUaNOKlsEA-Aolq2HYHWSc4d5vTVBSeyvsmZkUFrapjr8A9HiX9DQvYQK771L8_GbJWcWE_5mI4hE57PgJ5lc_WLvPzblwPGN01i6r5EWh7bHYsyPG_vYbLQz4_SytNhrEiwLHQduJ0BUhiA4tShJzbEdIJKklbkrrVLqwpF7dPl7k04eGE768xcJiDovYDcSPySGuyzjjNKFBQ7FPqwVIHTTJdt9fBeDrXY_bdPfoHhaVYO63OiJUp0LdOW6uuNwQ714c6IgekRuDoh9hWYMOH7oKL3c6OhC3hTKcteheaRtEbAH4n_9ctO70Q7hTlNR-2Si3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قراره کلی فیلم سوپر دربیاد
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/funhiphop/82509" target="_blank">📅 08:47 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82508">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🔴
آخجون میخوان پول پرت کنن تو صورتمون
وزیر خزانه‌داری آمریکا : از بامداد امروز، حمله مالی به ایران را آغاز خواهیم کرد؛ بزرگ‌ترین حمله از این نوع در تاریخ.
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/funhiphop/82508" target="_blank">📅 04:31 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82506">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pCcD1U2Mlrtoaw2rdkwbdlrDDELxVffezOvFMVUdFxzM-jZusOA_fe7YuOzhr0nCLsIdOl9pQx6YyRj0N8cOIs9vZ0uC95BTktLColK3RSjH9rMYKDuzuGbnaoAYzv6J4jXF6AKh6RNbFFm_O3z0MkAtn5AqKQWza84fmkU8E5qSHd3a9oE7tnPTuUgephyo_yMGZqselDPIazPk4TjcR5HMg_a_SJTuK1V_2hJW5OkpzWKoUKrogLzamQ2kdEJBBkHWE8F1R_zmrVF5FtTYsaFCalBqEDSmwa7vZvk_OnTD72h1n8iUo_GMRT7mJKEeaacUN3qsulGb5W23gZMEXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری هیچکس
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/funhiphop/82506" target="_blank">📅 01:07 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82505">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gtd6QsFcVURq09CYorWthWTbNDHZvx9Kpe60smFB6nvC0CEucLPyoRtUfBVoWwf8XexpHAb-7B2APzgTBOmsFeCt1mt4YgjGkUclvR7SjDZAYjdR858o3l2-gudAC6W7URrX28DsqRP8hwZ0ahARTHVORMwv2-YpRgIDP_MjHuxnEsCfzsJ_znOhn40FLFUEeRQBTZGNMWCJdC9thGE0vbBMcSp-NyIBWzBP3iFg97Q9mcf8psxyXhcfQyuNkyfliya1lI2xWIPKEUVaW7E_eKme2zFB2FHQYYipnhO_AA8pni6B3zuv40gTOhnL_z7owFTkinjc8K5i4VM3eAo6Tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بریم واس سی ال
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/funhiphop/82505" target="_blank">📅 00:38 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82504">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JA8a3NQoYWvAAuFxlpRdhhVjyrPoVQMImnbRbN8B2ufRIb0uWiqeUowroXcj2kJwqJCbwUMvYBCFNAobCw6YJnkUL6IRrTD6vmj8yb28UOKFzyeXRIts0kqAJotEnYnMKtRI2ZPVU5k1pxTBt28RwhtjATo0J62GSwwNynB0xB8ooMdMEJd1zkLhq_Q88SPUiAZZzYfSd8cfErcdTQY6cKz0yVl0Fc7jMyRpUHEOK5x3fnjdVX51wJFlXXxXdUTfdxtb1MqM9bAvK6LTmBP7meJrTv-BRCHJVkl4JQrGEp0I8Uf5QIUg6fL9obo5VKxZJRN-XNZraqaCPJp2dIVg-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدیر حوزه علمیه شیراز گفته زنان شوهر دار هم میتونن عقد موقت کنن و نیازی به اجازه شوهرشون ندارن.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/funhiphop/82504" target="_blank">📅 22:41 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82500">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bTRYz61VEC0SHUxPW5Zk3haNuOD6jjziwKcXBItE7qykccnALVpcl0GxGiREfQo_Nnyj0Slp71hzC1G-Ri4vPNHLQF55EE4wQ3HnK199Yd9PDhToxEeBjSvJmlQ3fbnG082ll2PVUZYT_mY5ngVkKlFuJsZJL6CHvK5sPLhTQLcLCJypFQQKSJacHxWoKVfY_FQK4yWUOO_EWfLxxF6hZur5BR3YWBs3BWuhYnDkvhOa6tzm2zdyzgSx79IIiIgKtg3PVXPf76JOiEARQvIbfGFXgWKNVy_Hi9MgsC_Pu83xAoZTPKsjuSVsOOvBUpiEcjVNxu75AxKrzg9adGJ_xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الوارز بخاطر خستگی بازی واس اتلتیکو رو نیمکته امشب
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/82500" target="_blank">📅 22:14 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82499">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">زن ستیزی تا کی چرا مجوز ندادید دختر بیرانوند کنسرت بزاره؟
شیما کاتوزیان لطفا ۱۰۰ تا استوری بزار رسیدگی بشه</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/82499" target="_blank">📅 22:04 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82498">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GZQs3SPt7LcPcnSkOrHbpzqzs3SmUmSnpd435P1cq5JJBZ0AOqohvoDr5wpOVo9fP3lrhDoVXszatZfpsbwYLmiDdOe8YSWTE8Lb8L-xkl3DsZx_Ih8CtlitDSyqarpEKDy60-Gnm5_N153xleEiQ5rx3gDjDdeh-vInJRicoaRW0e0KwXDf3NmZRxmGowf0rq7AuPRl7tW3UCHcfOEYcA_6gSD35FAcazdvt-smQBS3Uj3vNzVqXOsKYq-E0wNT7mgUzJ3xXb6rtOG0jpDMtFTCx1nEn5iKJQ6KwOnweiWi1OzeZ_l7yb6YPS5wWh7YM60pZYAB8CQiMFfJtXJwzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجوز یعنی مخدر
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/funhiphop/82498" target="_blank">📅 21:58 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82497">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BZZDg9YW2SHBbZVS7_CnGkXezINgsOZppBDxL7TK31twhBnNoDk3P_3YAFLgL4K3CRiDOcTqAbBgBJD2C1mqBqTW3EUBbIPWNBDWHx2YmAswR_VmuKX0N-OoWNKAab6r4oV-D1CAQBR8UrnlWVkMFTXKPY21H_IXXD6jS6umhhYoyUQPLt3q3LhFFS9JPi3WoVrNE1Xfkignnis6a8oPzRASxbVfC6q-g7CdWWmGiEQ2NH9pqOvvcO_C_lim77g95VZ7_Ev0TUKyyNAT9anZWoP8w8zuwKDFJOskCgO6_5dJAixNECTbKwuYTkqb4EfUxPbHvi339uShv91p-Lwyvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شیر پسر یه چندتا گل به خودی بزن تا بزارن بری
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/82497" target="_blank">📅 20:08 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82496">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">عجب تجاوزی داره میکنه استقلال کبیر به سپاهان
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/82496" target="_blank">📅 19:40 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82495">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OS5uAWTW_fj-uzmGktcfmr1wgI7Vz_nHNzCx1NCiBFKNkor0YKak2_DgsYJwhZn4FmopDGZz7bU2gVo8pRd5kc5GB1hIG-4ivFzvs15clSnTE-ZdwEB2zHm0n_iFIG33wvHruRWSCyz487SITFYfxOj1LjymrQh0F0FCp7uUpvdakmGXC52LxoV0fH1KXHiMycbf88cd8TLBXtsU4FXFnC0gFc5vbpjtN84RMz2qt3bnUt38ZtOtQ_FRIhLmDDvFtcykQR__T3cGjn65fd0y7voFglTB8A6EH3KQn2wS7pz0vBKvfHjVgVGTHk1y2KvFJHnOVS4lbaFDsV6-VyonEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هیپ‌هاپولوژیست چی می‌کشید بنده خدا.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/funhiphop/82495" target="_blank">📅 19:28 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82494">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a34a3c950.mp4?token=NJ1ak7FJCcA3jVBJdhyKuHD5AiLaF1mWOEMvdT-HL2V2EmJ5Eafe-1bK3Gw3x_LmFZQXcxq3BnqszIsoyPtdiIfZEe99d05qe6X_ghkO88tcJ1IROYewEtr1Y8ps1nWgqUAd9IfQHlC6FdUTVN9sADuJJaWPTf-ja7vRiJuEy-gavubTd6M2O2dHCDAAu8ulTdoUAoTuxqtIfIeG0srOU0Xx80nwNjWTzZybbmNLuHiLr8-6A4hT6xg58S6Fnv5r_-ZisuBwLSi7hikqOZ4vaiHHrkrJn87WZVWSwrnhpRoFg5mIJT8-gMIHmOgsj9hSqmcUWPRXKAC71WjBkwf6bw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a34a3c950.mp4?token=NJ1ak7FJCcA3jVBJdhyKuHD5AiLaF1mWOEMvdT-HL2V2EmJ5Eafe-1bK3Gw3x_LmFZQXcxq3BnqszIsoyPtdiIfZEe99d05qe6X_ghkO88tcJ1IROYewEtr1Y8ps1nWgqUAd9IfQHlC6FdUTVN9sADuJJaWPTf-ja7vRiJuEy-gavubTd6M2O2dHCDAAu8ulTdoUAoTuxqtIfIeG0srOU0Xx80nwNjWTzZybbmNLuHiLr8-6A4hT6xg58S6Fnv5r_-ZisuBwLSi7hikqOZ4vaiHHrkrJn87WZVWSwrnhpRoFg5mIJT8-gMIHmOgsj9hSqmcUWPRXKAC71WjBkwf6bw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آفرین ایرانی باز افتخار آفریدی.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/82494" target="_blank">📅 19:01 · 01 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
