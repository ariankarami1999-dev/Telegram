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
<img src="https://cdn4.telesco.pe/file/U3MfJiXJ6lyJ-mSvlAvGo1gTMsKafdfL3tuwCJ7tC-VfMv-0FYjL9mKoUssHD-f-3MuCsn4NpqaVjPueQshbAEk-Yusl9nt3V1fZxUk829e79LlE4n9rLyRtSnVuqkfg5B-5pb3ckDpVHxZmY5xCSHlGHB3qp3MgU_vpLuIH78fEt0GsJOM1dLOTvwo6rgI4MEf4q6bnBbNDbCahq61vvAsRUmTal4jdluFOZOCsMB1q4Q1WXcxMNOgdE9rartWPTf_Lctklo_p1EPwC_SVl4XD1dXmR50zZPLWLzcp4x5K6NDr1tHdY62clUBFrIq-87QNByfkggNtxY3YwQGhhyA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 219K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-05 15:59:24</div>
<hr>

<div class="tg-post" id="msg-66864">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YzAlNAuqqwSgXqo8NvmErGWn7enByHW8GRYhiXiKN-CS_a7OpbXtNvNyWBELH_und9x2t9cokX2yvYW7Yvkem9F2vconDE--oCR3eWK6u8CfR2AkJVXmmZGvL2910oOL-bQO0WEhjFP_KqDxrygyUN6KwWDDsdYcBO2LDWFXM33Aurf1u7vuvnVtWfADO1if9bj4GyKRatj3e87rxpFyk9UIQZJKONf4A3THfNahMwuCuQHCLck3lmPVyKjHceAcGjzCxAD8d3GpX7krns8nKSJhA6jH7ltD3PqVi0imRp4QDYbfYuKoUw3mMm8T5pC2CEgVGT1Qlib04rvIJwEe5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a41ee6c687.mp4?token=K3fXCXlqSWhH1d0hwhiYuvSUvmEVOQuYRcwm3FV-cH5wfgW6Ky4f01aEDl6X_yFoLtk2t57Ho_09T_rSz-mIxbwZYAocp5fUFlth1zELr0EMptBJ8EU4Kvj4s5j_H6-OYq1msV91nOLo75aIAcg0SfXggnxWlnX0BDobYxz-JQRdNSau8raZzI21ALnCIKeg3uPn314KLUo2lPZigRGpdU-r57kSY39Y_iIKkXg3-RFro9iXgjF8fyDGm4O4hYBOdrY40k3GIrQKxcodBz4YS7CA-Emv2DbOGthfBi-WdhelhlviiA65sYnYLbf9LZMFOXVgvbuevoa_dHFc46za5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a41ee6c687.mp4?token=K3fXCXlqSWhH1d0hwhiYuvSUvmEVOQuYRcwm3FV-cH5wfgW6Ky4f01aEDl6X_yFoLtk2t57Ho_09T_rSz-mIxbwZYAocp5fUFlth1zELr0EMptBJ8EU4Kvj4s5j_H6-OYq1msV91nOLo75aIAcg0SfXggnxWlnX0BDobYxz-JQRdNSau8raZzI21ALnCIKeg3uPn314KLUo2lPZigRGpdU-r57kSY39Y_iIKkXg3-RFro9iXgjF8fyDGm4O4hYBOdrY40k3GIrQKxcodBz4YS7CA-Emv2DbOGthfBi-WdhelhlviiA65sYnYLbf9LZMFOXVgvbuevoa_dHFc46za5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
رسانه‌های لبنانی گزارش می‌دهند که یک پهپاد ارتش اسرائیل، اعلامیه‌هایی را بر فراز شهر منصوری در جنوب لبنان، نزدیک صور، رها کرده است.
روی این اعلامیه‌ها نوشته شده است: «منطقه خطر! دور بمانید! هرگونه نزدیک شدن به نیروهای ارتش اسرائیل شما را در معرض خطر قرار می‌دهد.»
هنوز تأیید فوری از سوی ارتش اسرائیل وجود ندارد.
@News_Hut</div>
<div class="tg-footer">👁️ 3.48K · <a href="https://t.me/news_hut/66864" target="_blank">📅 15:35 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66863">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22157b34b4.mp4?token=HyciqR9ojR75gyeIv1CfKQxS8Hv5FKNjuov7Mpqq6IRvXZ4Q1PgfB6z_tiX9FjE0Jle6VHvO28QBBUmSRIXlhTmki7cVqqqDFNx_iAqtIYxvElWUDsRf-YtsYsyPMYrRfClu78Gpl-_D-34HHwdJZgz3DrmkxyIPD_lckp59dB_G4Gqn142p_WFxrHvcfbzJtCSu5EgcPet_UISyI1vVWuX9Ipc0QOdibhqMHjsuxzaBVvkIryn3wFdY4lWOVkVL64ookuDrrBWIh2gXm-Tu7AS2DBKAOOuDcLAUac3j5rn4bjZdocWwap80VRvsV6wAACMCDeLDk4GDDIN9T22Wfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22157b34b4.mp4?token=HyciqR9ojR75gyeIv1CfKQxS8Hv5FKNjuov7Mpqq6IRvXZ4Q1PgfB6z_tiX9FjE0Jle6VHvO28QBBUmSRIXlhTmki7cVqqqDFNx_iAqtIYxvElWUDsRf-YtsYsyPMYrRfClu78Gpl-_D-34HHwdJZgz3DrmkxyIPD_lckp59dB_G4Gqn142p_WFxrHvcfbzJtCSu5EgcPet_UISyI1vVWuX9Ipc0QOdibhqMHjsuxzaBVvkIryn3wFdY4lWOVkVL64ookuDrrBWIh2gXm-Tu7AS2DBKAOOuDcLAUac3j5rn4bjZdocWwap80VRvsV6wAACMCDeLDk4GDDIN9T22Wfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ترامپ:
اکثر مردم نمی‌دانند که حرف B در کلمه dumb وجود دارد
😢
@News_Hut</div>
<div class="tg-footer">👁️ 7.62K · <a href="https://t.me/news_hut/66863" target="_blank">📅 14:48 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66862">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">⚠️
خبرگزاری فوق معتبر فارس:
درب تاسیسات فردو، نطنز و اصفهان به روی بازرسان آژانس تا زمان رسیدن به توافق نهایی بسته است.
@News_Hut</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/news_hut/66862" target="_blank">📅 14:13 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66861">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/bfb3904efc.mp4?token=GS_o9lYqhihINSJvMvIgyBWS4DwOSq1UhsGVIqwzfC9_RmbAv3MKuKFC3dJs78MHMCr70ZcqnKS0n5s-QEBI-tR-DuAaRjws5oYQ-MPPvPgWYMRLQGDdnGFhcV123feI2qaNfF7i4BxkUlEoMlzs52j4SuxmHWPDLJqt2SQjaZ8KIy5Wv2bL5ptHHXGTx35r7kczO_elgvoyXWv_lX-drzmEMxTNQyy8YA8y1pR3kM083Wm4PswRITlkdNzCmcNKU_2yRBF9nMsWfnqiJKYIehNfz4IioqjQF93tG3jP47SuSsGjl7PFWonkRTcuJUQedzUmpDE50mSC0XYCrdQvsA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/bfb3904efc.mp4?token=GS_o9lYqhihINSJvMvIgyBWS4DwOSq1UhsGVIqwzfC9_RmbAv3MKuKFC3dJs78MHMCr70ZcqnKS0n5s-QEBI-tR-DuAaRjws5oYQ-MPPvPgWYMRLQGDdnGFhcV123feI2qaNfF7i4BxkUlEoMlzs52j4SuxmHWPDLJqt2SQjaZ8KIy5Wv2bL5ptHHXGTx35r7kczO_elgvoyXWv_lX-drzmEMxTNQyy8YA8y1pR3kM083Wm4PswRITlkdNzCmcNKU_2yRBF9nMsWfnqiJKYIehNfz4IioqjQF93tG3jP47SuSsGjl7PFWonkRTcuJUQedzUmpDE50mSC0XYCrdQvsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تو یکی از مراسمای محرم، شیر تعزیه افتاده بود دنبال یکی از لشکریان یزید، که یه لحظه جلوش رو ندید
🤣
🤣
🤣
@News_Hut</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/news_hut/66861" target="_blank">📅 13:29 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66860">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">❌
قرارگاه مرکزی خاتم الانبیا:
🔴
پرواز هواپیماهای نظامی اسرائیل در نزدیکی حریم هوایی ایران یک تهدید مستقیم محسوب می‌شود و اگر ایالات متحده اسرائیل را مهار نکند، ایران این تهدیدها را تحمل نخواهد کرد و حق پاسخ را برای خود محفوظ می‌داند
@News_Hut</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/news_hut/66860" target="_blank">📅 13:15 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66857">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Oo9oZVqERXKjmwXTpesSOcxfIK3aYviuAMHyDSiybq3cAD88M8EkFNjBou2OEMxQgawpJETCZBi_KOYPFCUkXYojrWD2Qz_wfk0gQat4aRY97uS5XuTmg_ZcD-QbXX1GmjEgu8INxsMgo-bu-CSy2CM1jdLhSh00Mano3jbR9X158m7A3nM9emv05alybIA524LNRuJlxjBJytZijWS2odW4x_H4Y3epDDyvISN-kS1PdlrtMnT0m-kuLQgFbHKvoIAEpxafc6xiQZqXZVL5iJLi1tRc-zW__3I4-CbYo9AGHC_TKO57IVccZasJG6s2buhPzzfNZ5mGcJDoRZTouQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C7GizzHGf8hvvaBAEApqeqCRlR2ZJeOgigwCWvJutssSZOSOlhWJxBZiVfC4fDfjSVAGrbBEEruiVAgHvqtphLpqv6YlxmYIqeC-H51h7KaQQ2hq7lIto07jji0ukbnYh4MxxeZSS-dLMz1vTPnZHyjMpMZCDgfF37-ASghRIinvQE9mgB2AlhiAPLyVUEOLvieZ_bE7k8TZ8i9qOBlvn7iEsEtxFHMRsrlxwHkvR-Br4dhoFQ1ZvPs_8mjfF2ekIGILwJdG-_yW2l3UfasHw0AMuAEhXDmJNPYY-FuJQtQIM3YdRdbPAfKDOMzxcZkIh4_2absD8FCF58KiajXuWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/URih0d8VX1o8K7N46CIbvO4OH4PgK9l9tpn6x4kZnELTLrvpbM3SC7kCoOYfLBc4RcXDUyATDbcvmxFJ0W4rJE1j29p5pyQ2Om_WUcWplPjKx4uJyyYc7WuAiUmb4KbY4WMEFsvvJKxErARC9jAbaNewRqXOR0QUOw-HB8MU66oqaqNWEtRceD-K4yg_CaumXlUUuf-Mp0zGuZ_KAIfeRWrXXYDtyFXCdGAvf9m_EbiirsDVNhEg7idDTBPLtYEOleFiq0Y_Sk6aCg4pRoaE96SB-wV44GavelJHFLLJqsu2Z-XiNUCc2IRb1Q9rR_Sm0YBPq-q0HHsdvzc5zqjsPg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
حملات هوایی صبح امروز ارتش اسرائیل به جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/news_hut/66857" target="_blank">📅 12:55 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66856">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67fdc892f6.mp4?token=lAf6jOf4_85WDzYRyCrMHBCu2m79MxePKfOgxW_aXTUIagQ59yQlIHxyUtH7HPdSKFEdXd6w8bvEpTBwBNfepmeIwIJu_W7C9YfxdilaXn53IvHpJiYz00lyIQYRUVofRj33c-S18WBcHuVfQokzPjC-8IYFqtUdC5xtAdKLejdfxVRvTgiJpwqBEjtjIKvlcVvvGLJRlBSij8V2wFaEKmUwl6m77EtdYEYIHvq-g0NG0dy4Ape5D-eUO_U8rDwRdZOwqUxUhFqPenibKKoMaJIHly34Qx6CpLedBH2MuJKGeBq7J_LoVLc-hXn_RAxMc4LIWBaqBhIXsa7wv0JpHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67fdc892f6.mp4?token=lAf6jOf4_85WDzYRyCrMHBCu2m79MxePKfOgxW_aXTUIagQ59yQlIHxyUtH7HPdSKFEdXd6w8bvEpTBwBNfepmeIwIJu_W7C9YfxdilaXn53IvHpJiYz00lyIQYRUVofRj33c-S18WBcHuVfQokzPjC-8IYFqtUdC5xtAdKLejdfxVRvTgiJpwqBEjtjIKvlcVvvGLJRlBSij8V2wFaEKmUwl6m77EtdYEYIHvq-g0NG0dy4Ape5D-eUO_U8rDwRdZOwqUxUhFqPenibKKoMaJIHly34Qx6CpLedBH2MuJKGeBq7J_LoVLc-hXn_RAxMc4LIWBaqBhIXsa7wv0JpHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ درباره ایران:
«یک بازار جدید دیگر هم در راه داریم و آن، کشور دوست‌داشتنی ایران است.
ایران کشور زیبایی است. کسی دوست دارد به آنجا برود؟ جمهوری اسلامی ایران با مشکل تأمین مواد غذایی روبه‌رو است و ما قرار است بخشی از پول آن‌ها را بگیریم و آن را خرج کنیم. همچنین قرار است مقدار زیادی گندم، سویا و ذرت خریداری کنیم و این روند به‌زودی آغاز خواهد شد.
این برنامه هم بسیار بزرگ خواهد بود.»
@News_Hut</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/news_hut/66856" target="_blank">📅 12:23 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66855">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/daTywHm-ItI3_atB5Lc7sXyrTsp12sdNA6f-hQnbWUC8KNXQcfsrAQ9Rv1drS6AgOYBHI3wjyTIOtCZ-xruIFykqDfRNaam2u0c0f9ODvF8nXkQ9ssB85LyqtpGryyn4sz2i4Fwj3KlboFOq3qVA95fDN3_g1sm1arMMBJ5xDqFqYnDALo7ycURL7AQ_wBYX71-O9TvRiVN3hiGVpwWwK84ydQHqbM-O9okQ97YopEXUuiN-2nYcv5kc4x6Mk_jwNshSiUZ2r4AYVFVfy2vTtxLod6FNU3Ta4YQxN9WJenRdT9LDOE6TTQ5Jy_Hs5wbjAsdlEg1YdjM4cExmQCf3Xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇺🇸
پرزیدنت ترامپ:
روند خرید محصولات کشاورزی ایران از ما خیلی زود آغاز خواهد شد و من انتظار دارم که حجم آن بسیار زیاد باشد.
ما پول ایران رو گرفتیم و بجاش ذرت و سویا خودمان را دادیم!
@News_Hut</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/news_hut/66855" target="_blank">📅 11:03 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66854">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">‼️
جی‌دی ونس درمورد ایران:
🔴
آن‌ها دائماً سعی دارند مأموریتی که دونالد ترامپ برای ما تعیین کرده است را تغییر دهند.
🔴
او در ابتدا چه گفت؟ «من می‌خواهم ارتش متعارف آن‌ها را نابود کنم. من می‌خواهم توانایی آن‌ها برای اعمال قدرت را از بین ببرم. و من می‌خواهم تضمین کنم که هرگز سلاح هسته‌ای نداشته باشند.»
🔴
آنچه دیده‌ام این است که برخی افراد سعی می‌کنند بگویند: «خب، این عالی است، اما شما باید هدف متفاوتی داشته باشید.»
🔴
به نظر من دلیل موفقیت رئیس‌جمهور این است که او از تسلیم شدن در برابر آن تمایل خودداری می‌کند.
🔴
او می‌گوید: «ما کاری را که قصد انجامش را داشتیم انجام دادیم. ما اهرم‌های دیپلماتیک، اقتصادی و نظامی باورنکردنی ایجاد کردیم. بیایید از این اهرم‌ها برای کسب پیروزی بزرگ‌تری برای مردم آمریکا استفاده کنیم.»
🔴
این همان چیزی است که او از ما خواسته است انجام دهیم. هنوز تمام نشده، اما تا اینجا همه چیز خوب پیش رفته است.
@News_Hut</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/news_hut/66854" target="_blank">📅 10:33 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66853">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aefac4ff7d.mp4?token=mvPEUuA9R4oRc96JqMWkU_qpS-ynxrR_MZnrkMBzD3WnQ1uxmxuQlUW4CEumcUpIjTdSrsj-v7HBn5IKsO9VlYUtuwhqvKcKHl-nAf-B58kdkj29yZNiHgqspGGdey8yG1rnOxXje3c2budLH90gOw1qP9AoicpqEbq-dLB0gzDemAUDinYmZFxjyGf-LQhZY-lkNV79tBAVLSL3nkmz6ysN5zmNbqDVUBisGN-69wWJyM_5ToKIYk5-Wrge4otK5yzYfoPC9LSDXkXLv2i4_zzCSiAbt44cKArgu_7bcdfEvXRonTRz8ZKpxMoxq-WBW6K-nMz5bbWR60Esz7m24g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aefac4ff7d.mp4?token=mvPEUuA9R4oRc96JqMWkU_qpS-ynxrR_MZnrkMBzD3WnQ1uxmxuQlUW4CEumcUpIjTdSrsj-v7HBn5IKsO9VlYUtuwhqvKcKHl-nAf-B58kdkj29yZNiHgqspGGdey8yG1rnOxXje3c2budLH90gOw1qP9AoicpqEbq-dLB0gzDemAUDinYmZFxjyGf-LQhZY-lkNV79tBAVLSL3nkmz6ysN5zmNbqDVUBisGN-69wWJyM_5ToKIYk5-Wrge4otK5yzYfoPC9LSDXkXLv2i4_zzCSiAbt44cKArgu_7bcdfEvXRonTRz8ZKpxMoxq-WBW6K-nMz5bbWR60Esz7m24g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎯
ارتش اسرائیل: ۶ عضو حزب‌الله را در جنوب لبنان ترور کردیم!
@News_Hut</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/news_hut/66853" target="_blank">📅 10:05 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66851">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/73a731d25b.mp4?token=Y-EIPrhAOrrlgNiZ7X8luJukKlcxFv7fVLhYcV4Ghi1mU5s42s8OvvDLW4c_tj9Tk24WvobqEmAHuAOqGBaBbZBqMMD41zKUW5AVRb5wRdZKby56sWKrMxDWqIBwYMS6k0Fk1EwfYL_09Fdx-aUOR26PiExAWkLQY7Z3pmtzXo6JU2VHl-0AT8M2NgN3OD_JBDhg_TgOaiAFcD0pTJxboRSF-rqWLWX-WkQVqJTDSPsqzO5rwVGeOgScfNqM55-wEviuxHY3I8S1VP6a06qFMucK-zL4pQZyLEU0MfpWpUnJ5BHF4MI0sGy7WcZ7gFmuat_NyBAJjWfQgu97bkbl6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/73a731d25b.mp4?token=Y-EIPrhAOrrlgNiZ7X8luJukKlcxFv7fVLhYcV4Ghi1mU5s42s8OvvDLW4c_tj9Tk24WvobqEmAHuAOqGBaBbZBqMMD41zKUW5AVRb5wRdZKby56sWKrMxDWqIBwYMS6k0Fk1EwfYL_09Fdx-aUOR26PiExAWkLQY7Z3pmtzXo6JU2VHl-0AT8M2NgN3OD_JBDhg_TgOaiAFcD0pTJxboRSF-rqWLWX-WkQVqJTDSPsqzO5rwVGeOgScfNqM55-wEviuxHY3I8S1VP6a06qFMucK-zL4pQZyLEU0MfpWpUnJ5BHF4MI0sGy7WcZ7gFmuat_NyBAJjWfQgu97bkbl6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قالیباف با روسری و ماسک اومده بوده هیئت
😂
@News_Hut</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/66851" target="_blank">📅 09:33 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66850">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cff13197ee.mp4?token=E0JeZChsoT9J-jZlUqztweGxfySIm2AJlWHzvE3zr6X8FG5RnK-NuIBT8LYhIhtREFerYuEyZjG1vD65276fCS057y7e9W2KmSMDEXT62r70574E89Ii0_gyXUH7C6gqOEcFjnNOTg0rO2XxHu_LrfPoc8d0JLoKLeixFrQcgjQ7TN53Mnxde_NfXDOdZRfaiDtqEMpLaRpOWGyZHsdpznRF-mbASh32GSKy-fHzSYJRuq-Jxs_L2rl9eMfKrUr19peczuP8Y4hpug7RpoMIituWbguaMaN53TEee8W_uuSA4a_Q9EbMqggAp8o-YBdnEjRflMG1ibMBIL-azYc9Ng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cff13197ee.mp4?token=E0JeZChsoT9J-jZlUqztweGxfySIm2AJlWHzvE3zr6X8FG5RnK-NuIBT8LYhIhtREFerYuEyZjG1vD65276fCS057y7e9W2KmSMDEXT62r70574E89Ii0_gyXUH7C6gqOEcFjnNOTg0rO2XxHu_LrfPoc8d0JLoKLeixFrQcgjQ7TN53Mnxde_NfXDOdZRfaiDtqEMpLaRpOWGyZHsdpznRF-mbASh32GSKy-fHzSYJRuq-Jxs_L2rl9eMfKrUr19peczuP8Y4hpug7RpoMIituWbguaMaN53TEee8W_uuSA4a_Q9EbMqggAp8o-YBdnEjRflMG1ibMBIL-azYc9Ng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
فرماندهی مرکزی ایالات متحده:
جت‌های جنگنده اف-۳۵ بر روی ناو هواپیمابر یو‌اس‌اس تریپولی  (LHA 7)، ناو پرچمدار گروه آماده آبی-خاکی تریپولی/یگان سی و یکم اعزامی تفنگداران دریایی، در حال برخاستن و فرود هستند. ملوانان و تفنگداران دریایی ایالات متحده در دریای عرب در حال عملیات هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/news_hut/66850" target="_blank">📅 09:02 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66849">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">میخوای به راحتی از فوتبال و باقی ورزش ها کسب درامد کنی؟!
⚠️
پس همین الان وارد کانال @Palang_Bet شو چون بهت اموزش میده چطور دلاری پول دربیاری
❗️
💵
اینجا میتونی روزانه درامد داشته باشی و سرمایت چندبرابر کنی @Palang_Bet     @Palang_Bet</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/66849" target="_blank">📅 02:16 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66848">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pNl1hpjsh1osc3qEo1IY9vTdgMt1lrsl9k7XNpOGYeYNcE9etLSX4-6FXacAycEooQZ8zjfNwrXwaeFo_H_goln9xD-5_jA5PSBV2-MwRipLB4qzWx0Okz1NjOmp96WgL6XayYIKQuBqRekkf_mL7eaQtiVl7wqjgyqjQ4_BEMBiAwPqKdRKcc86mZpfZHq7PJ_oniNed4KiygC8XH1yzMZsYfxXfSrl-SoWOpeaVdEtT1okbQtgzaYq_BNj4lHpT1-nwGnYIqixBHqpSWNLQ46FrdY2klwqNfLLQIDpLRt0jr3Q7qGpcuvxqYgJxuvhc4elzl6X-Fgf6hH-Z7Bpwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میخوای به راحتی از فوتبال و باقی ورزش ها کسب درامد کنی؟!
⚠️
پس همین الان وارد کانال
@Palang_Bet
شو
چون بهت اموزش میده چطور دلاری پول دربیاری
❗️
💵
اینجا میتونی روزانه درامد داشته باشی و سرمایت چندبرابر کنی
@Palang_Bet
@Palang_Bet</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/66848" target="_blank">📅 02:16 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66847">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dFodfH1BHMEeLUV-gksrkOwWv90cafYgEer2CSI_7_-ESLtNepEXYAi0Bor2TlW1tqeBar5_MWNWf_rRLK4gMGOeYmuEvl1WRQ4uCFVKoL1WcmYDCiK2Y7kHnQI7ZifrOmbPIEKo3j40ltCe8fYbcu0O0h2yfvC6dJ2ePVUXh3XSqOAnBI9qVOAJzdxS49xptvs_N9kBTxPSrPsm1bNvmr3UHolhzOKouIBt8gfbXMj0wIa0p8eYGlyh5o7QbWnp9DuKZA84MsTkTUzR9Moru-_14xh8pLaSFTliWO9Ut8NDVZUqwnPFi3FDMJll1W-eHxRbNg9l3jadud5r5v7arQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
‏بر اساس گزارش وال‌استریت ژورنال (WSJ):
🔴
ایران روز پنج‌شنبه به یک کشتی باری با پرچم سنگاپور در تنگه هرمز حمله کرد؛ اقدامی که به‌عنوان آزمونی برای توافق هفته گذشته میان آمریکا و ایران جهت بازگشایی این مسیر حیاتی کشتیرانی تلقی می‌شود.
این حمله به پل فرماندهی کشتی آسیب زد، اما هیچ تلفات جانی در پی نداشت.
این حادثه چند ساعت پس از آن رخ داد که ایران به کشتی‌ها هشدار داده بود از مسیرهایی که مورد تأییدش نیست استفاده نکنند
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/66847" target="_blank">📅 01:54 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66846">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">رسانه های اسرائیلی اعلام کردند طی درگیری ارتش اسرائیل و نیروهای حزب الله در منطقه بیت یاحون در جنوب لبنان چند نفر از سربازان ارتش اسرائیل از تیپ ۷۶۹ مجروح شده و با بالگرد از منطقه تخلیه شده اند.
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/66846" target="_blank">📅 00:57 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66845">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">با بحرانی تر شدن وضعیت ونزوئلا و مفقود شدن بیش از پنجاه هزار نفر گویا به نظر می‌رسد مثل زلزله سال ۲۰۱۰ هائیتی که ایالات متحده آمریکا به این کشور نیروی امدادی/نظامی ارسال کرد دولت ترامپ هم به سمت همچین سناریویی پیش می‌رود.
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/66845" target="_blank">📅 00:55 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66844">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🔴
وقتی نت ملی بود ، تنها سرویسی که برامون قطع نشد همین بود
🔥
🔗
@Kaviani_Vpn
🔗
@Kaviani_Vpn</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/66844" target="_blank">📅 00:54 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66843">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KHFLEHf8y9mg00my4rHF8Q-JTPMcF6taitL4U3WX5zOOSd8UgsEXP_WyRl4Qb0dKgg0WzhT82NeXrpBYJoOY0R1KtF39Zjvcv2k9p6SujCkpobVa5V343mpGLcxUL8YH5JXY5N9OQ9XnK5dBaGJw_hBQcjFEnBEtCQIsvZAOV_R0xsqJEuN6tPfsAIxSy7e_N0SmIYk92gthex5Ss_CqGkreGlTruuIfQayRuBlUzSCEyJEwJcXcpVaMOeHEZP9M7ntIZT-N5LssSXRsv-dQSiBbNoYRS5LbstwnpElf5ljgsR6-dp5fluLcJOIBND2ujMmEWTDbsyfE1M12SlTH9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
کانفینگ نامحدود برای همه اپراتورها
🔥
⚡
سرعت بالا | بدون قطعی | تحویل آنی
💵
یک‌ماهه: 380
❗️
پشتیبانی 24 ساعته واقعی
❗️
✅
سازگار با تمام خطوط
🚀
اگه سرعت مهمه، همین الان پیام بده
🔗
@Kaviani_Vpn
🔗
@Kaviani_Vpn</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/66843" target="_blank">📅 00:54 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66842">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CS-fH3qzGeFuZItzovKGlFk23q_0vh4wbwAU6oSoGWqg2c1z1J_g5Y6N3hKgfvQlLEqnBBVxHLi5jCR6_vADQGbJLYnrXXXjrca4E1QTVYCWAHm179PBxQNSwfAsX5HuOAxbCRFYeKUaImC_YqE5evDETrmOQInxWvLX2GACHZ3wxzpa0cSG0hl9U7cx47THTgc31m4vkwwEUcKmZts-ET4eF85uwXHh0lhrUaR8bVgAl9ya3kInpbWyRXImJG-Epe33hnMzkDa-E2T7MUMR2sbDNnFMfQPBLoxiYbYiezThlEmIfEuLxPydMLC25mzVKLnt1FjClL0IP3PqiyJ_aQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
گزارش از لبنان: جت‌های اسرائیلی به بیت یانون در جنوب لبنان حمله کردند.
این پس از تهدید امروز سپاه پاسداران علیه اسرائیل صورت می‌گیرد
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/66842" target="_blank">📅 00:48 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66841">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b6d00bedd.mp4?token=JLALEFAEuJy3pWqRgagiHGzoVUTNJJe4Dq-GCeQg7NwaSHSMj03J9mo1HrrxxXs0kHT1JXfGExh2Rd4ISlafwVqCTfr7TXKtMku3thnlITfDRino0lD9nS8OSAfWO2PvjCWolP9NXy89yG9n1VW_JLr3FPIX0usIG_6wjYCOxcBLKaAhPN_Lpp5TYph4uPD5e-x8ufy0Q2eIEk6_8mTz0Ti_RxWpdAjP47QhR8hg3A0shcSQnjBFws490IWdpciMxTJxbpchu-kkttXn3G12v8od0EeBFhn-BfVHiDnzkNpLhfIR9t_VS3t3zwWbvPSA0bgv14WAW78TJRWhZe3bbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b6d00bedd.mp4?token=JLALEFAEuJy3pWqRgagiHGzoVUTNJJe4Dq-GCeQg7NwaSHSMj03J9mo1HrrxxXs0kHT1JXfGExh2Rd4ISlafwVqCTfr7TXKtMku3thnlITfDRino0lD9nS8OSAfWO2PvjCWolP9NXy89yG9n1VW_JLr3FPIX0usIG_6wjYCOxcBLKaAhPN_Lpp5TYph4uPD5e-x8ufy0Q2eIEk6_8mTz0Ti_RxWpdAjP47QhR8hg3A0shcSQnjBFws490IWdpciMxTJxbpchu-kkttXn3G12v8od0EeBFhn-BfVHiDnzkNpLhfIR9t_VS3t3zwWbvPSA0bgv14WAW78TJRWhZe3bbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
خبرنگار:
«شما قبلاً آن‌ها را «دیوانه‌های دین‌سالار مذهبی» می‌نامیدید. آیا هنوز هم فکر می‌کنید این توصیف دربارهٔ رهبری کنونی هم صدق می‌کند؟»
🔴
مارکو روبیو، وزیر امور خارجه ایالات متحده:
«ببینید، موضوع این نیست که من باور دارم این‌طور است؛ واقعیت همین است. نظام ایران توسط روحانیون، یعنی روحانیون تندرو، اداره می‌شود. همیشه هم همین بوده است... البته در بخش‌های سیاسی حکومتشان هم افرادی هستند که ظاهراً انعطاف‌پذیرترند یا تمایل بیشتری برای همکاری با ما دارند. ما در حال مذاکره با همان افراد هستیم. باید ببینیم نتیجه چه خواهد شد.»
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/66841" target="_blank">📅 00:23 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66840">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/345e633380.mp4?token=bjmCyKpod0FvrEZTqNqs7gBTpPlzQ4ACvFsD3gC7e3iIMcAfg4kf96tOf3eDB_oDn3uQYQRPxQ_8c1XiLZ4BeTiH-EQTh3u0qy2W0riBkGOTfGKj8QoEOEZja-OfXg53rZNkhUQlQOp1VjM6SPQKctqsWRZU_lm3x9d0zoKpCTPzyrKNg4b6GQLXI-WEv8iucFPEfqQgvTxNGoXofdfnDtWAiJlnbWcGLFe3DkDbCtqE8yn2w_A8SUUlcWJ5BsvhNr6gQrdYAyn3yRgSc4KPhSLjEQpZcLwq4xzZF6ZvOJtk3KeFRE-np0ERcqIPcRo9i5iupaNH4Mh_63NGW0Tpmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/345e633380.mp4?token=bjmCyKpod0FvrEZTqNqs7gBTpPlzQ4ACvFsD3gC7e3iIMcAfg4kf96tOf3eDB_oDn3uQYQRPxQ_8c1XiLZ4BeTiH-EQTh3u0qy2W0riBkGOTfGKj8QoEOEZja-OfXg53rZNkhUQlQOp1VjM6SPQKctqsWRZU_lm3x9d0zoKpCTPzyrKNg4b6GQLXI-WEv8iucFPEfqQgvTxNGoXofdfnDtWAiJlnbWcGLFe3DkDbCtqE8yn2w_A8SUUlcWJ5BsvhNr6gQrdYAyn3yRgSc4KPhSLjEQpZcLwq4xzZF6ZvOJtk3KeFRE-np0ERcqIPcRo9i5iupaNH4Mh_63NGW0Tpmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مجری:‏بهای بسیار سنگینی.
رئیس‌جمهور ترامپ این جنگ را آغاز کرد،
و وعده‌های بزرگی دربارهٔ تغییر رژیم داد
و وعده‌های بزرگی به مردم ایران داد.
آیا ازنحوه‌ای که آن را به پایان رسانده،ناامید شده‌اید؟
شاهزاده رضا پهلوی:خب، نمی‌دانم هنوز تمام شده یا نه.چون همان‌طور که می‌دانید، هر چند ساعت یک‌بار ما یک توییت متفاوت از این
رئیس‌جمهور دریافت می‌کنیم و ناگهان موضع
از یک چیز به چیز دیگر تغییر می‌کند.
بنابراین من خیلی به هیچ اظهارنظری
که مطرح شده، وزن نمی‌دهم.
و در واقع، من فقط، می‌دانید،
کمی دنبال می‌کردم که
در به‌صورت زنده چه می‌گذشت.
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/66840" target="_blank">📅 00:15 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66839">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">#فوتبال جام جهانی فوتبال
📊
2 گل آلمان و ساحل عاج  کد:YXA6P ضریب:2.3
➖
➖
➖
➖
➖
➖
➖
➖
➖
➖
➖
➖
دانلود برنامه ملبت @Palang_bet</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/66839" target="_blank">📅 00:15 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66838">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f455bc9393.mp4?token=EadIj45nYFyBHcPkfVnQmVwRbROMKHZlNhLTa0r_CFjgnG61Buxz2Otw6bobUhNcX0U94hmF7Lnd-a8V105z-y-wXsac_y_gn7-Jbmkdxg5pIbbnd2C0IBxIbCwQ11u_dX_KQnOAi9uFg8WBqxhgaP5d8bZ16TS5BkoaKVdUpIn2bZ_MpDcxMXTbDt3DAiEXoIp31AdgaKkDklVcjaY25udT8JO5BrDmXTQK3NLU42oTP6FOsrwPv-4A9RrwuLeTQIwLuorBoWSCkDeUV28gH7GWFr4FJzEWn0MVjuMDTOoLjVP8WyKxT75cPmFHGbVGisHt81GVy9FsCGOj2lKHNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f455bc9393.mp4?token=EadIj45nYFyBHcPkfVnQmVwRbROMKHZlNhLTa0r_CFjgnG61Buxz2Otw6bobUhNcX0U94hmF7Lnd-a8V105z-y-wXsac_y_gn7-Jbmkdxg5pIbbnd2C0IBxIbCwQ11u_dX_KQnOAi9uFg8WBqxhgaP5d8bZ16TS5BkoaKVdUpIn2bZ_MpDcxMXTbDt3DAiEXoIp31AdgaKkDklVcjaY25udT8JO5BrDmXTQK3NLU42oTP6FOsrwPv-4A9RrwuLeTQIwLuorBoWSCkDeUV28gH7GWFr4FJzEWn0MVjuMDTOoLjVP8WyKxT75cPmFHGbVGisHt81GVy9FsCGOj2lKHNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مفقود شدن بیش از ۲۱ هزار نفر در پی زلزله‌های ویرانگر ونزوئلا
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/66838" target="_blank">📅 23:31 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66837">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JFm06uSYg6159Puts4R1f_fpEhfqXtoJ7eyjgLVjtnMxjCLgrh9Lb-btuuY3_h-vV6xwg7H75UQSxhg_2dAuKDJbgb_seP1ty53gdBFDuY0mGyWxIxZs8fM0K1XGHSfJmaS5Sja1UimKL-chjGK1RkRXWkx197oI9cAl8xQ5WzG-a27Y-BBcwW7s01gOKlZpRHiJp08NJ1zljPzQ9E21hAag39Y2bjgb65f6VU6XfivzUmA5YyIQEpm781NvGvs3CbBOHOGV_nQcxLd_5dRXqDV0yrFuA6RPWy1Zm-LItURLndxvGmD88GxL09x55nvbD7pXZxljl72xUGtO84A8ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
عراقچی:
پس از بیانیه مشترک اخیر در مسقط، تماس تلفنی سازنده‌ای با وزیر امور خارجه عمان داشتیم. ما مجدداً تأکید کردیم که ایران و عمان «برای تعریف مدیریت آینده و خدمات دریایی در تنگه هرمز» گفتگو خواهند کرد. ما مصمم هستیم و این کار را با همسایگان خود انجام خواهیم داد.
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/66837" target="_blank">📅 23:02 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66836">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eab5d7e42e.mp4?token=oSmrcDH3bi__OqeZLupTGPKauVojLwNvDZn0_AncEwRo6JSMe5TqDC53UKXvQWc1zHzMWiGLe_0TRQL-0-0GrKELQT71uRTgxFOA42BcH6rBGa-Wx3Khpz31EhWjWYX2UWpMNfmI019aA5rb3VDt69ZPs2hqx_GWqi9-fAd2b_4GreaOiT4E6mq-x4WQ1WNSMi_xNQYE9WIsUe46FRD3RJIHCVfsvlTNVAvyacZHSchnIcXD-kzfSmynuLzEwENgXQ_zarPJKBwMTAzsVNB6JpNy8-l_KNlWOmxHSWVHYiGWQJCU0WaZZiZUN2mjldOAk_dPTYLwHuhvm7qrsV4bLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eab5d7e42e.mp4?token=oSmrcDH3bi__OqeZLupTGPKauVojLwNvDZn0_AncEwRo6JSMe5TqDC53UKXvQWc1zHzMWiGLe_0TRQL-0-0GrKELQT71uRTgxFOA42BcH6rBGa-Wx3Khpz31EhWjWYX2UWpMNfmI019aA5rb3VDt69ZPs2hqx_GWqi9-fAd2b_4GreaOiT4E6mq-x4WQ1WNSMi_xNQYE9WIsUe46FRD3RJIHCVfsvlTNVAvyacZHSchnIcXD-kzfSmynuLzEwENgXQ_zarPJKBwMTAzsVNB6JpNy8-l_KNlWOmxHSWVHYiGWQJCU0WaZZiZUN2mjldOAk_dPTYLwHuhvm7qrsV4bLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
روبیو درباره ایران:
ما می‌دانیم افرادی که هنوز در بالاترین سطوح آن حکومت حضور دارند، همان کسانی هستند که به همان ایدئولوژی و همان طرز فکری پایبندند که رهبران پیشین آن حکومت به آن باور داشتند.
نظام ایران همچنان توسط روحانیون تندرو رهبری می‌شود.
همیشه همین‌طور بوده و همچنان نیز همین‌طور است
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/66836" target="_blank">📅 22:33 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66835">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd736f47d9.mp4?token=BRuj3x6ARAPp7zMP_wB_A2tiW6YjGhacu3xqvC4RHpT3vBChRpXlxD1x8Zub29qPRnynPdDc7a9l6nkqZvz95e4xTaidxRkaAQ2VNkab8ThvVEYJ_ZdPYWR2ObyYP2Ud57H2SUvjNORJuZbJsyS_DNmYaR46DiBIlVMEGBswaxNr20KU7GbTLfRZPb2az0vIwTOLJGUZ6ZpU0ZutICh187e0L0dQwQv4hXmidb4KPII4cmh9qAUc9j72N7jy51c0ysqlMYn48-Zx9foYFRWtuoP8CpEg0lyZSGnhHziUapvSQaPp0x8Xwq79f5LWElnkcgCxtAjMewkHKLtFVSxaAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd736f47d9.mp4?token=BRuj3x6ARAPp7zMP_wB_A2tiW6YjGhacu3xqvC4RHpT3vBChRpXlxD1x8Zub29qPRnynPdDc7a9l6nkqZvz95e4xTaidxRkaAQ2VNkab8ThvVEYJ_ZdPYWR2ObyYP2Ud57H2SUvjNORJuZbJsyS_DNmYaR46DiBIlVMEGBswaxNr20KU7GbTLfRZPb2az0vIwTOLJGUZ6ZpU0ZutICh187e0L0dQwQv4hXmidb4KPII4cmh9qAUc9j72N7jy51c0ysqlMYn48-Zx9foYFRWtuoP8CpEg0lyZSGnhHziUapvSQaPp0x8Xwq79f5LWElnkcgCxtAjMewkHKLtFVSxaAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پزشکیان:
نمی‌شود برای امام حسین اشک بریزیم اما در جامعه شاهد ظلم، بی‌عدالتی، فقر باشیم
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/66835" target="_blank">📅 21:49 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66834">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dm2dEeQh4y_skKjM6wcngDG1C3Sx3amBxupjkJggt70mQz3C87wPfFs2uBumnrMEGbRuvXSoN7l_wKJ1PU41F58xvHafyb0PYsPGQPcD1RFcWZBfCOXRw6vRMd8vElH5wVAwVu6ZXHQx32_ALO7IDQEnqDSC2oaX5l7YwgFbBLKhDkOis7vq34m75r-OirT2OXXG_KqQdXTPzRPNiMAkpOKl-U9PR5nWMaXwoCGH2yCsRXslap9HAqDxlFw7Tuv5UEML0MIm1GV18hpgkVRLDmP3Hl1sNCKPe-gYXLMU3y9VBcxKw9skFnOMhX6pf75rbqwn0Lg7ZasgrBYON-WtvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بیانیه پایانی نشست مشترک شورای همکاری خلیج‌فارس و آمریکا:
🔴
تاکید بر اهمیت بازگشایی تنگه هرمز بدون محدودیت و بدون اخذ عوارض عبور.
🔴
تاکید این که هر گونه تجارت یا سرمایه گذاری با ایران باید به انجام تعهدات آن به موجب توافق منوط شود.
🔴
تاکید بر لزوم خلع سلاح همه گروه های مسلح در غزه.
🔴
تاکید بر ادامه حمایت از دولت سوریه در بازگرداندن خدمات، فراهم کردن زمینه های بازگشت داوطلبانه پناهندگان سوری و مبارزه با تروریسم.
🔴
مذاکرات لبنان نباید به نتایج دیگر نزاع ها مشروط شود
🔴
حملات متجاوزانه گروه های شبه نظامی مورد حمایت ایران در عراق علیه کشورهای خلیجی محکوم شده و از تلاش های دولت عراق برای حصر سلاح در اختیار دولت این کشور اعلام حمایت شد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/66834" target="_blank">📅 21:14 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66833">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/965348f417.mp4?token=CH7x9TwX3aIKYg8M10Weplll_oP2qMI_f30n8chzeCwlRDMEVtwdiDl0PTk0kGNQB_IijCujLlDt-lCAhHjIEUVtjRCjrjsvz_asOLWnOEA8EUhnr-uiKqBl3finE_VZ4kNxapAt3MMaP48iJn3Qbifgy-wd237_CNPXjhgEM42Mrdc6C-wGB0-l0YhpqqOhh9yy1nTiJdlutoBR_TXNBfu6y26CCPm7Na-VwER1A-e2rn2AZ07GM6yCtYVDjQT8y5kpeZN6SqpBe4Jyp84SAqvVl4nh6tSuL8lc97BAGxcg4vj_TURENcaG6MdNrLil8JK0pU1Flks8PAPHBgV5ZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/965348f417.mp4?token=CH7x9TwX3aIKYg8M10Weplll_oP2qMI_f30n8chzeCwlRDMEVtwdiDl0PTk0kGNQB_IijCujLlDt-lCAhHjIEUVtjRCjrjsvz_asOLWnOEA8EUhnr-uiKqBl3finE_VZ4kNxapAt3MMaP48iJn3Qbifgy-wd237_CNPXjhgEM42Mrdc6C-wGB0-l0YhpqqOhh9yy1nTiJdlutoBR_TXNBfu6y26CCPm7Na-VwER1A-e2rn2AZ07GM6yCtYVDjQT8y5kpeZN6SqpBe4Jyp84SAqvVl4nh6tSuL8lc97BAGxcg4vj_TURENcaG6MdNrLil8JK0pU1Flks8PAPHBgV5ZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
نتانیاهو:
فقط یک آدم کور می‌گوید هیچ دستاوردی وجود ندارد. دستاوردهای عظیمی وجود دارد.
من همه آنها را فهرست نکرده‌ام چون می‌خواهم شما را نجات دهم. شما اینجا زیر آفتاب سوزان ایستاده‌اید - فهرست کردن همه آنها زمان بسیار زیادی می‌برد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/66833" target="_blank">📅 20:40 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66832">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f0J4m7ZtyuWxj8PMAdFOSR21Y1e--yjrgtV_VEOMLZ6qxTxYN5MlqAzXoOnbZrtySATY2ekmgbquDGE31pz64zZQ1xH2G-jqptmLaQiQN3PPygLUQok7LD3YcywAtGpw7KYsosoE4CPpu_CCnwtFpWB8AW0Q5WrON4eUlXwCjz-rHdOPI3j5S8F9c3vKESup1wQLxZycCgszD0ACYlB3fmTtAxspMTmYHNZg6Ak52evG6xW9K6XJzN3yl5b_h1uoTqJh4yaukfFNswRKvKcV50dATNvUraOAZ-HCIky6p_MojGgF3EOP2NYtzT300yIqW7se2FYyspVnkjTNFONvMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
عراقچی:
با نهایت تاسف از وقوع زلزله در ونزوئلا. مراتب تسلیت خود را به دولت و مردم ونزوئلا، به ویژه خانواده‌های قربانیان، ابراز می‌داریم و برای مجروحان آرزوی بهبودی سریع داریم. جمهوری اسلامی ایران با مردم ونزوئلا ابراز همبستگی می‌کند و آماده ارائه کمک‌های کامل است.
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/66832" target="_blank">📅 20:40 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66831">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">این آمار فقط مال روز اول جام جهانیه
🔥
😤
میخوای از پیش بینی فوتبال پول در بیاری؟!
⚠️
تو پلنگ بت جویین شو بهت آموزش میدم چطور پول دربیاری و تا اخر جام جهانی سود تپلی بکنی
❗️
اینجا میتونی روزانه درامد داشته باشی
💵
🔥
@palang_bet @palang_bet @palang_bet @palang_bet</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/66831" target="_blank">📅 20:40 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66830">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GwJmv_LX_PH9Wt5x7I4FtLznHpbeW0mQpU8A-Thzfpwvl4keth9dMp2KGYVg7bffiry4hc_2jKo87G1vCOKts-TOKaa9GoO0VKgpZUUkPDvNB48DTmlcmDuyvtUpGBFhW4shZvkgR0rfaxjQ3V6c9R8P0elnphSLiCKXc3I0xI40JwnUxuOqfmiWRft5g7V0hxEIFdjHEHuwVzrSRyJmaJur8dlKRQxTFoooPWf1dK_PlCpt095GH2N0zHZC_EwvQo8FlFyQsRkbEr8z8cvgsaSJqGz4xshfMIfm2y1wHVG0O0Xro-D8OocGd7pChNWDuwfJLwAQvMwi4V9ZsvCYyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این آمار فقط مال روز اول
جام جهانیه
🔥
😤
میخوای از پیش بینی فوتبال پول در بیاری؟!
⚠️
تو
پلنگ بت
جویین شو
بهت آموزش میدم چطور پول دربیاری و تا اخر
جام جهانی
سود تپلی بکنی
❗️
اینجا میتونی روزانه درامد داشته باشی
💵
🔥
@palang_bet @palang_bet
@palang_bet @palang_bet</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/66830" target="_blank">📅 20:40 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66829">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c8c286a22.mp4?token=vR5IPMukM5gtvdY78U7RFsyeeMmhBkW7KaMLumD-gxqI1fCuJHpWr7SX_zHMIMI7mdjh8ffcKg_jf53VRlRk_5waV-7eFqxOOQlUmRvGLTsF7Td2GNAFfbBYFTEx8XlqHmMT7miK1D-KSPcj-Ql5S51A_GZEWwfz_Tfi1oHrWP3KMbEEQUNlCp65FTUE6V5kd6s6wCIkxy1K1XaMPN79TKNTFvfAv1jt2JmsfJ4McUa4bIOFhoTOHwdwVunBXhc74wbbpNp_zLp9tF0SlBqkMvw5G2pReQO0-f2ifT8ZNRsV_Gn3MKp34Gad9k8uiT5at4bLtkb1HAAXXyqK6juBnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c8c286a22.mp4?token=vR5IPMukM5gtvdY78U7RFsyeeMmhBkW7KaMLumD-gxqI1fCuJHpWr7SX_zHMIMI7mdjh8ffcKg_jf53VRlRk_5waV-7eFqxOOQlUmRvGLTsF7Td2GNAFfbBYFTEx8XlqHmMT7miK1D-KSPcj-Ql5S51A_GZEWwfz_Tfi1oHrWP3KMbEEQUNlCp65FTUE6V5kd6s6wCIkxy1K1XaMPN79TKNTFvfAv1jt2JmsfJ4McUa4bIOFhoTOHwdwVunBXhc74wbbpNp_zLp9tF0SlBqkMvw5G2pReQO0-f2ifT8ZNRsV_Gn3MKp34Gad9k8uiT5at4bLtkb1HAAXXyqK6juBnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
بنیامین نتانیاهو:
من ادعا نمی‌کنم که پیامبر هستم.
اما فکر می‌کنم می‌دانم چه چیزی بقا را در منطقهٔ ما ـ و به‌طور فزاینده در سراسر جهان ـ تعیین می‌کند:
قوی‌ها زنده می‌مانند.
برای ضعیف‌ها جایی وجود ندارد.
آن‌ها طعمه می‌شوند.
و از میان می‌روند
@News_Hut</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/66829" target="_blank">📅 20:28 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66828">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63d4c620ba.mp4?token=O4QCZlwpXNBXUd2JP3gWj4stwj-hhQdVK8_llI9vVFen0x7nQrlgGZEXJk-symLbTSEGwOqic1zP3Pt-_ulIZACbKpE43Peq9E64VizSStMFehQEgevzrU2yZJ6lfc53X6Jefp_BACz-z1byjaFF1_2qtmJ8e3jwXzPBDrNtuDMFkmsJhWevUXUVcRcWEC1IL0jiWX0OvSIvEpY3KfvbPpYcWBwCaAQIgTHrDumw-Qo2bpgXIobPgXjttKdglc2p9tz2GEImtRkoldA_781EoSJF3UWAs0NtqxG4Bw6ERg9DuNPQIm9LCGHXQixLn49M2OZ39IggzlhnhCcVROM2xA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63d4c620ba.mp4?token=O4QCZlwpXNBXUd2JP3gWj4stwj-hhQdVK8_llI9vVFen0x7nQrlgGZEXJk-symLbTSEGwOqic1zP3Pt-_ulIZACbKpE43Peq9E64VizSStMFehQEgevzrU2yZJ6lfc53X6Jefp_BACz-z1byjaFF1_2qtmJ8e3jwXzPBDrNtuDMFkmsJhWevUXUVcRcWEC1IL0jiWX0OvSIvEpY3KfvbPpYcWBwCaAQIgTHrDumw-Qo2bpgXIobPgXjttKdglc2p9tz2GEImtRkoldA_781EoSJF3UWAs0NtqxG4Bw6ERg9DuNPQIm9LCGHXQixLn49M2OZ39IggzlhnhCcVROM2xA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
بنیامین نتانیاهو: در مورد رژیم ایران، من فقط یک چیز خواهم گفت: با توافق یا بدون توافق، تا زمانی که من نخست‌وزیر اسرائیل هستم، ایران هرگز سلاح هسته‌ای نخواهد داشت. به هیچ وجه اجازه نخواهیم داد ایران بمب‌های هسته‌ای توسعه دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/66828" target="_blank">📅 20:20 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66827">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🚨
فروش کانفیگ‌های نامحدود
💵
قیمت: 380 تومان
✅
سازگار با تمام اپراتورها
✅
سرعت بالا و پایداری واقعی
✅
مناسب برای گیم
✅
تحویل آنی
❗️
پشتیبانی 24 ساعته  جهت خرید اشتراک پیام بدید
⬇️
@kaviani_vpn @kaviani_vpn</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/66827" target="_blank">📅 20:20 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66826">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N44UMwe8q28-Q-74uWtaP9m5w__GCj3Ww9kHgjiIC3AkfJ7CyxAl4HIRuAnEcRiRUBug1HDGlLLeCzlUlk6AV-PS595ZR-GZWDKzN-NjXwBVl_d4OUO4nDg-2VB2b4324kI0Z9MJpUH_6anTjhEoJMsqJEYIAsPpIZ1Za2jeYih8tJ1DkK5xjpLEV0ZMC1VTfXz_YYU7fDK_YD8f718NDWN3-muN4ZZ3xdXto2fcdiC8LFVkqz_nboxKeX24dp5MowKHIm7mgyzRL9PgFrXFm7Wg4igr7zhjwRNfReqQBUyOS7hFlvO5owzjlkoNxr_BCxfuMDumMlU8imPW6F9F7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فروش کانفیگ‌های نامحدود
💵
قیمت: 380 تومان
✅
سازگار با تمام اپراتورها
✅
سرعت بالا و پایداری واقعی
✅
مناسب برای گیم
✅
تحویل آنی
❗️
پشتیبانی 24 ساعته
جهت خرید اشتراک پیام بدید
⬇️
@kaviani_vpn
@kaviani_vpn</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/66826" target="_blank">📅 20:20 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66824">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tO9aANO2Rp94H8_pHpOZD1OWzEquun0J1w1KPfUkLywkaOM2ad9Z5BfC-rHcLCwc8kgvNMSGESoraTu6vIyTNZ3uteyA-POYR5EbghfQtD_k1VpgK-AeIngy9U12aRAJzdodlpMSLr7pYdVsLQ9aru9E7CwcIPYtEDawqoFbTNjEMBZJTUU_l_2XjReMGnI6RAmJMHqxpACdwbVdoZObedPN2ypUzV4A0Rq3PLv97ULb3ixi8S4qkE2Z0Yyz2ZfuUiue7Q-bXX1p2Ohb-62gw6JZHF4Rv-C3uqnLiBksZxJiq1kYcuO_g82RHW_Cp7R1v_eRNNXdCbYFqnlGgPZWQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1b8ae4df4.mp4?token=fDlCVhdwwJakdI0qt23JHOP17ZKO4_QDgaxWYAKllzSDjUCn4yuAXJWVVBLhWhioqDXVLiZ6MFKi8ONMiIxQV_v8_NwUgHyvBH0uXLlGtAbks_4rroLi3A6KlMDVMyXJBbXbYrLC1-eZR2lH731vbPz9c9Ty5n1wXdoBGQCqFgI0V_3I4fyuAU33ZQONebllJvkHo0ROdV1kjwzS_vs0J2ZxqPtLmTF_DnFw4jz3R0y_LqDLIXo6bNVNoU-8BTn1145vVygZWKfj2tQeZ5U9UQBC78TMamfMZVPA8Yet1pqw-PSZUdQoCxG_k0IH6VPpCwC5Ao4Y64F8KUe8QfK6lg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1b8ae4df4.mp4?token=fDlCVhdwwJakdI0qt23JHOP17ZKO4_QDgaxWYAKllzSDjUCn4yuAXJWVVBLhWhioqDXVLiZ6MFKi8ONMiIxQV_v8_NwUgHyvBH0uXLlGtAbks_4rroLi3A6KlMDVMyXJBbXbYrLC1-eZR2lH731vbPz9c9Ty5n1wXdoBGQCqFgI0V_3I4fyuAU33ZQONebllJvkHo0ROdV1kjwzS_vs0J2ZxqPtLmTF_DnFw4jz3R0y_LqDLIXo6bNVNoU-8BTn1145vVygZWKfj2tQeZ5U9UQBC78TMamfMZVPA8Yet1pqw-PSZUdQoCxG_k0IH6VPpCwC5Ao4Y64F8KUe8QfK6lg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فستیوال محرم
😂
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/66824" target="_blank">📅 19:08 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66823">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/113cb570d9.mp4?token=UsBpEaMyDCTCDtrZDLoHtEuNRKLPnzErlz4oji0z4tPlBb3hYqaPY07VQFWmLiWUzwUCUA-W9AxoX7ZvioHQN8pbiDsiPW78Y_XHt3Lm5QVr3o4t6wMiDR20toPGtF5u1klrCgsstidVXwu5aTtPNXC8bf0wRnfH9fTG_B_EVzI66y9FSKxFBg5e1FXrSwgkY-cMiY87ILRp9En1sAKng4KVuEyPWkrBaX7MY6OvGnTwPmE5hfopB8WxIae2ESsR3JNdbnl7kOJOG1mFU-EdRLs98_Fw67Z5ddyCKDein0oG1m-Z4PTepEVpnSPgg0BvGJLV73x9Wal4X22ySAXpmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/113cb570d9.mp4?token=UsBpEaMyDCTCDtrZDLoHtEuNRKLPnzErlz4oji0z4tPlBb3hYqaPY07VQFWmLiWUzwUCUA-W9AxoX7ZvioHQN8pbiDsiPW78Y_XHt3Lm5QVr3o4t6wMiDR20toPGtF5u1klrCgsstidVXwu5aTtPNXC8bf0wRnfH9fTG_B_EVzI66y9FSKxFBg5e1FXrSwgkY-cMiY87ILRp9En1sAKng4KVuEyPWkrBaX7MY6OvGnTwPmE5hfopB8WxIae2ESsR3JNdbnl7kOJOG1mFU-EdRLs98_Fw67Z5ddyCKDein0oG1m-Z4PTepEVpnSPgg0BvGJLV73x9Wal4X22ySAXpmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
قالیباف پاسخ مجری صدا و سیما رو داد
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/66823" target="_blank">📅 18:33 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66822">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0453856b46.mp4?token=J7uWg2SH8lrpIpAkMbkoxcD-9GP32YGDHGVBReZ8do1fvg7mZQrlnKYLEs5zeywbZBw4vr-qKQVzGuhW4PViaket8Px8xKHTwJlGZgFJ0w0FMqaipwtbSSRgOrqf5A5hqB0bPu1HFY52GVQNOkcSF8MEMqX-OKlb9Jy0-xIeUIMzZJyJyBqYdJgHxksUFZT_n3Ryi5RFEiXyJu_x1_5ppX_7cQev_U6s7dhYjo_bJKomFFj4CRE9XZAwA29yeTT3-KQjNobpyRBB4-DcoYJOMKAIfhnuOQTuLok9VwylRn0jsMd2Fos1IBFlDyqiZWlghgYiywk2MiXrFZCdkyvtKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0453856b46.mp4?token=J7uWg2SH8lrpIpAkMbkoxcD-9GP32YGDHGVBReZ8do1fvg7mZQrlnKYLEs5zeywbZBw4vr-qKQVzGuhW4PViaket8Px8xKHTwJlGZgFJ0w0FMqaipwtbSSRgOrqf5A5hqB0bPu1HFY52GVQNOkcSF8MEMqX-OKlb9Jy0-xIeUIMzZJyJyBqYdJgHxksUFZT_n3Ryi5RFEiXyJu_x1_5ppX_7cQev_U6s7dhYjo_bJKomFFj4CRE9XZAwA29yeTT3-KQjNobpyRBB4-DcoYJOMKAIfhnuOQTuLok9VwylRn0jsMd2Fos1IBFlDyqiZWlghgYiywk2MiXrFZCdkyvtKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
مارکو روبیو درباره ایران:
🔴
اگر کشتی‌ها در حال حرکت باشند، واکنش ما هم بر همان اساس خواهد بود.
اما اگر کشتی‌ها حرکت نکنند، این نقض توافق محسوب می‌شود و در آن صورت با یک مشکل جدی روبه‌رو خواهیم شد
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/66822" target="_blank">📅 17:55 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66821">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50938460f0.mp4?token=i7qWMzA2gdXFZOJ0RUtdPlmlyvJCaND5_8ZDH0x22fVcr9ijWtRK2LC2UN6YYmeQDrnI-3bbgLzCx1Vk7TJhGlRyorox4rACP3uSokT-wL1L78ytg6LIhkbGWM5dDApbnfMa-s5FrOoKUEm-pd4fcFIvcupaq1EUWFNUtHQ4ZxJLUeYbJn4UP4qvZ0Vu-c6f4aDnqid8ENWmxSNh67jz8O_mKYJnoFVSQtzTwjyJXOozLyM0xv1BX2TDa2uv6Muf2Fy8PR4u7_OgXoVTNoNGQ6Xyjl_mFZrLvhh8iE8mgogDt_WdbfX9wFD4br2Ajv7BWiPr9N0Wb2isJMybHSKpRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50938460f0.mp4?token=i7qWMzA2gdXFZOJ0RUtdPlmlyvJCaND5_8ZDH0x22fVcr9ijWtRK2LC2UN6YYmeQDrnI-3bbgLzCx1Vk7TJhGlRyorox4rACP3uSokT-wL1L78ytg6LIhkbGWM5dDApbnfMa-s5FrOoKUEm-pd4fcFIvcupaq1EUWFNUtHQ4ZxJLUeYbJn4UP4qvZ0Vu-c6f4aDnqid8ENWmxSNh67jz8O_mKYJnoFVSQtzTwjyJXOozLyM0xv1BX2TDa2uv6Muf2Fy8PR4u7_OgXoVTNoNGQ6Xyjl_mFZrLvhh8iE8mgogDt_WdbfX9wFD4br2Ajv7BWiPr9N0Wb2isJMybHSKpRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
مارکو روبیو درباره ایران:
🔴
فرض کنیم که ما کاملاً دیوانه شده‌ایم و عقل‌مان را کاملاً از دست داده‌ایم و تصمیم گرفته‌ایم با ایجاد یک سیستم عوارض یا دریافت هزینه موافقت کنیم.
این قرار است چطور کار کند؟ اصلاً شدنی نیست. چون اگر کسی هزینه را نپردازد، چه اتفاقی می‌افتد؟
فرض کنید یک کشتی بگوید: “من این هزینه را نمی‌پردازم.” این مثل عوارضی یک جاده نیست که بعداً یک قبض جریمه برایش ارسال شود. به آن شلیک می‌کنند.
اگر به یک کشتی شلیک شود یا یک کشتی غرق شود، دیگر هیچ کشتی دیگری حرکت نخواهد کرد.
بنابراین چنین سیستمی نه‌تنها غیرعاقلانه است، بلکه اصلاً نمی‌تواند اتفاق بیفتد.
حتی قابل اجرا هم نیست. پس بهتر است همین حالا این خیال‌پردازی را کنار بگذارید.
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/66821" target="_blank">📅 17:50 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66820">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mJ6praqAha_MBkP65yUkrEm0NDEHf-w-hwTOqXynpVQWId-ECFXV0LLaYegWfNVSHUDWkxJRYEHj7N8gFukJ4u2MBFOYhko2b0UZMQaqZi2YlWkjP4vG0ctFbIubsWBHZwX70UglUX-kibrLuh_QK42Q729HP4vKsrrbkRrUpxEa3AcpcJFH4SMxVIKs8LmtgzIcqnrydAlFxL4l5UjqakNWUVdniOYUxdrPlvnruESood_klGSO3Lfw6QnocfOiKQiGsNdLLvfGGfbrMcCp8vW2UAYS-tBp9dh9bYq56pukMeYmeG1HmtRZgDsC3zAdENd1sHjT6nzbWXmQ0N_Cjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
قالیباف:
آمریکا به دروغ ادعا می‌کند که دارایی‌های آزاد شده ما، کشاورزی آنها را می‌خرد. جالب است. تنها محصولی که ما برداشت می‌کنیم همان چیزی است که شما کاشتید: دهه‌ها بی‌اعتمادی. این محصول ارگانیک، فراوان و تولید داخل است. اما ظاهراً ایالات متحده فقط سویای تراریخته، وعده‌های عمل نشده و حرف‌های بی‌اساس صادر می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/66820" target="_blank">📅 17:19 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66819">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/477cde7837.mp4?token=jh_jiZAGx0grdWvEHb7QUEEUWsl9bEnFUdBZFyv4zkcr23xgXtM3EG3Z-7MRQiCV58gW95GFTBHuj4X7CBCjP92a5RMVwRLGWx-LVIZkTbz7R_EAA-xr_xg_mT1Wt7y3t3tz7mXJKQamo4wMDVrK60BrtaXbmjzuVeywgcqTUhfeBRPuLt57JtunjHMaC4Fb55SIj1SwyepNf8YGolCRIRaycsb_jrHtGrAFoGLPx9R1ySKn0sBSN4UhONyMwOQIaViJs4mCwJm-gNGSNb548KjAlJzMJSOHZfacY0iGbujrD85aOo4IhG_ZyI0hoorXTdhTpvjkw0seSLclOSyDyjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/477cde7837.mp4?token=jh_jiZAGx0grdWvEHb7QUEEUWsl9bEnFUdBZFyv4zkcr23xgXtM3EG3Z-7MRQiCV58gW95GFTBHuj4X7CBCjP92a5RMVwRLGWx-LVIZkTbz7R_EAA-xr_xg_mT1Wt7y3t3tz7mXJKQamo4wMDVrK60BrtaXbmjzuVeywgcqTUhfeBRPuLt57JtunjHMaC4Fb55SIj1SwyepNf8YGolCRIRaycsb_jrHtGrAFoGLPx9R1ySKn0sBSN4UhONyMwOQIaViJs4mCwJm-gNGSNb548KjAlJzMJSOHZfacY0iGbujrD85aOo4IhG_ZyI0hoorXTdhTpvjkw0seSLclOSyDyjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویرانی‌های بر جای مانده از زلزله مهیب ونزوئلا در شهر کاراکاس
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/66819" target="_blank">📅 17:08 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66818">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K30xs3ZTn23nz0dITGwVfHrF8RqJPQiEmvRPou8SMslr9ukPTeWUpsAWuq0_k8VnMdm6PN1E5Hy6LKvy8pORRi2IJIJiqqHDvT9gFWIALQRl4UARH8n4k3KrDsVtF9TdQLyv01QDnZUUNQAyPEm5fNX4BE6jA7TD0BxoQLgHIIpFQ87UfK4_BfkC8lcFpByV7lcWbd5CVMlQOFa0QC25bp2QNGLqFUfx8IK81PfBpS5m-XNWzQoTH2RHAatVAWVQR2gSlzcegOuukbJmVV7zdGfb9dHNcinjfpDO8s2-A8O5P7H7rJ6aF-Hrh3PHQaVnvbhwwUaNTLqvTWrjWhV_vQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اسماعیل قاآنی فرمانده نیروی قدس سپاه پاسداران:
اگر اسرائیل امروز داوطلبانه از جنوب لبنان عقب‌نشینی نکند، فردا مجبور به فرار با تحقیر و شکست خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/66818" target="_blank">📅 16:41 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66817">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4301a5bfb2.mp4?token=JCs_n_gONWPccUK4gopH5gX6KKIxMc44Iu0J-KkD-PE0jfvIV5gGYNEYNgxuq57v5paE2Uj8mmWWy0D2l41_4Lj3FhDeR-hXUHS4HPzf9KHYgI9gyaJylWRTKVqphGKjiFtaTyawGm6H0JLkDuWe3k-BSUS_xDO32H6CYvPNxvn3XACXyMqk4x-W3-HEo9uBiOzUAIFFFk9VAf9swyC_Usid_Lsbl5RfhzihiW48Eq0DVwRM13S_i9yq-heydr1xNG9hQL75LHXP0GVGwnV19mUc27nE3OoU0Lq9ZwJ8tsB3v2Mc1VggVsIyTjrxX7hNsKmaRMDinj2dAa0E3YPpjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4301a5bfb2.mp4?token=JCs_n_gONWPccUK4gopH5gX6KKIxMc44Iu0J-KkD-PE0jfvIV5gGYNEYNgxuq57v5paE2Uj8mmWWy0D2l41_4Lj3FhDeR-hXUHS4HPzf9KHYgI9gyaJylWRTKVqphGKjiFtaTyawGm6H0JLkDuWe3k-BSUS_xDO32H6CYvPNxvn3XACXyMqk4x-W3-HEo9uBiOzUAIFFFk9VAf9swyC_Usid_Lsbl5RfhzihiW48Eq0DVwRM13S_i9yq-heydr1xNG9hQL75LHXP0GVGwnV19mUc27nE3OoU0Lq9ZwJ8tsB3v2Mc1VggVsIyTjrxX7hNsKmaRMDinj2dAa0E3YPpjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇷
نیروی دریایی سپاه:
تنها کشتی هایی که از تهران مجوز دریافت کرده اند حق عبور از تنگه هرمز را دارند و با هر شناوری که از این دستور تبعیت نکند برخورد خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/66817" target="_blank">📅 16:09 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66816">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oyQWQv9t956qB7_sADt_7LGEO7autf7AcXedklp61k_mNfuTEtXBnVx6ZGwUg84bs6BYuWxYcg9liLj_IAReEOWCOv8buGt4hQtIjr1t9r1U-_d11SzlEtPBrIxN7BJolPSlvkpziY5sqKbO_EV6DgBshg517G2_ooAn0ZL5Yp4O1h9M5oDxyjQu2J2OKi4eu8pyA4gn5Ks56fQTbt2qNopi5jb2tm-sfLWVerq9T0NyYRp8xlNVhtgTN0LijzT7enzhfEbkx2f1mpLjPzhdADDCe2A6I1xwmHtT5hlfo5gFfWCT17PWecsNwMdrAVmLldM3d0_rvmYmkXZJ0NevCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇺🇸
پرزیدنت
ترامپ در تروث سوشال:
«شگفت‌انگیز! سنا رای خود درباره ایران را از ۵۰ در برابر ۴۸ مخالف، به ۵۰ در برابر ۴۷ موافق تغییر داد. رند پال و بیل کسیدی رای خود را تغییر دادند. از جان تون، لیندزی گراهام، برنی مورنو و همه سپاسگزارم. این رای به ایران هشدار می‌دهد.»
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/66816" target="_blank">📅 15:33 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66815">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">❌
خبرگزاری رسمی عمان:
وزیر خارجه عمان اعلام کرد ترتیبات آینده برای تنگه هرمز شامل دریافت عوارض از کشتی‌های عبوری نخواهد بود.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/66815" target="_blank">📅 14:53 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66814">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a64b900d33.mp4?token=IwUopvKACKhCiBFn736r3u8zuGJ1ZFX2Yqkpm7GtO4x8A8cWaty8hVMTl1VF7zYo0f2VYCAyySTDs2FVbUoh5Ofmx5T9FbH5C6xxTUzFbMH0j01Tx2H8hAvVgjJRvrs7UZTaFxUB1NuXH4Xns14ncW0VMpFCbKk80k8AU3KpYxqQ-f_RWCfEZ8OTjUM-nv1KWabFNxLls82Zva6D4N3wyNsqCwYIJrFtLdJ-UWaP6RF0QBW8mA9I7vzSHKurtutpvbjZT9tx4_Jvfc0h21tLyIyE6RElzOoSEXgxysTCb-tvxs6GznHQgeFRbqkHE-CDEcpwfPNhu3Nrhynhc3gcIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a64b900d33.mp4?token=IwUopvKACKhCiBFn736r3u8zuGJ1ZFX2Yqkpm7GtO4x8A8cWaty8hVMTl1VF7zYo0f2VYCAyySTDs2FVbUoh5Ofmx5T9FbH5C6xxTUzFbMH0j01Tx2H8hAvVgjJRvrs7UZTaFxUB1NuXH4Xns14ncW0VMpFCbKk80k8AU3KpYxqQ-f_RWCfEZ8OTjUM-nv1KWabFNxLls82Zva6D4N3wyNsqCwYIJrFtLdJ-UWaP6RF0QBW8mA9I7vzSHKurtutpvbjZT9tx4_Jvfc0h21tLyIyE6RElzOoSEXgxysTCb-tvxs6GznHQgeFRbqkHE-CDEcpwfPNhu3Nrhynhc3gcIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ درباره اردوغان:
🔴
او دوست من است و از جنگ دور ماند.
می‌دانید، او یکی از اصلی‌ترین گزینه‌ها برای ورود به جنگ با ایران بود.
شاید هم در طرف ایران، چون همان‌طور که می‌دانید، او طرفدار  اسرائیل نیست.
و من از او خواستم که وارد جنگ نشود. او هم وارد نشد
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/66814" target="_blank">📅 14:32 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66813">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YL4zRlLMw-NoW7Z_chXkQiHRKXwrDeKkS_95GPUwA3mGEl1IzqFstZUvqMc7AOkI1HMMzqMNJ7AKPUcp616OPeOz5pbqK5IUV_8j0gY66ppBTE3ZxWeJsMxM01aJm5Puhen3sTarpxkxmZsGMFutUoFlc1WmtVDh22i4utoWUOsSUxHGmTtEW7lz5VDygagRhGyiuJZDEsPjWUfc77Vh797ivsTOuTBILfTHFs2c9CweLCIgJg9teKKUvQi5-CxiCc8HJOl__jAl5NS8gy1BDvLPpZi1wlMtUNgdkHTeDkDkvhjFC-UvM2dhbiwFrOSGelf4vcOuzyu5QTsfqWQ1GQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
مارکو روبیو:
🔴
واشینگتن خواهان توافق با رژیم  جمهوری اسلامی است، اما نه به هر قیمتی.  هر توافقی باید واقعی، قابل راستی آزمایی و همراه با پایبندی کامل به تعهدات باشد. اگر رژیم جمهوری اسلامی به جای صدور ایدئولوژی بر رفاه مردم ایران تمرکز کند، آمریکا و شرکایش آماده همکاری خواهند بود، اما انتخاب مسیر کنونی نتیجه مثبتی نخواهد داشت. هیچ توافقی نباید امنیت، ثبات و شکوفایی شرکای آمریکا در منطقه خلیج فارس را تضعیف کند.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/66813" target="_blank">📅 14:24 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66812">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0835d639a.mp4?token=ckNNQinrkqo1PGRBgC9-avfDg1JAIeU8ldggS51f5Pp1GnS1Gkyr6tC4zBjXTU5ib4COfBWc2mkuYNMmeGN2LXVk1Ow5AoV3tu22IHih0HOt2n-o-L0DGjgLq1Bwns3_wAVl0Pv8VDi3M0IxOjCvS-8a30NTfsR-EX9m28ROtUk2cAzGyHQI1fPy53dJifzTPy_eKT2gMqr4DpHkzpvmbSeP7Pv2vNbxSz3nB2ChAIGHg_cQASZPNRDz1QSkgcVdd5Gqpx3LNOU_YBiDU7gCmi57gJBqe83yQrtPQAchJYRTbg6uL3q-fr2ztMuxNVbLCRWkivL6_-SsmE4RS6VeFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0835d639a.mp4?token=ckNNQinrkqo1PGRBgC9-avfDg1JAIeU8ldggS51f5Pp1GnS1Gkyr6tC4zBjXTU5ib4COfBWc2mkuYNMmeGN2LXVk1Ow5AoV3tu22IHih0HOt2n-o-L0DGjgLq1Bwns3_wAVl0Pv8VDi3M0IxOjCvS-8a30NTfsR-EX9m28ROtUk2cAzGyHQI1fPy53dJifzTPy_eKT2gMqr4DpHkzpvmbSeP7Pv2vNbxSz3nB2ChAIGHg_cQASZPNRDz1QSkgcVdd5Gqpx3LNOU_YBiDU7gCmi57gJBqe83yQrtPQAchJYRTbg6uL3q-fr2ztMuxNVbLCRWkivL6_-SsmE4RS6VeFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حتی در کیس بیماری هم عجیبیم
🚬
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/66812" target="_blank">📅 14:10 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66811">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce6df862a9.mp4?token=eeCri0-svgEwM0NN6QXC_d_31mrMmCE70LDuMWoZnbzlil1Q6_P6WAoXjVbW7sOCD3EQwhOp-97LJwlvL4BZRlYrTDnKNkTR_0tFtPzjw1pEhCBSZJmK4kdHdX1gCZz0smYnPQ3j4xEYWUm5P54yC2lPuHAAPak_Nkcc5xm1THIWuoJ6HdL0K6_5hhi4f-VEv8jHsKvqpyGkDGnxxQMdUoTQZYM7GF4vB3tmfVqRGCRdksOyt8ZDpWDfVPiCvPo2sR6j5sSY3TlDfRdEfoLS2Q9vLM8AKrn65araa6GqJA2Avmg60xfE5qBaJE2OObUakP-1diWpTVAv43TaZjJvpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce6df862a9.mp4?token=eeCri0-svgEwM0NN6QXC_d_31mrMmCE70LDuMWoZnbzlil1Q6_P6WAoXjVbW7sOCD3EQwhOp-97LJwlvL4BZRlYrTDnKNkTR_0tFtPzjw1pEhCBSZJmK4kdHdX1gCZz0smYnPQ3j4xEYWUm5P54yC2lPuHAAPak_Nkcc5xm1THIWuoJ6HdL0K6_5hhi4f-VEv8jHsKvqpyGkDGnxxQMdUoTQZYM7GF4vB3tmfVqRGCRdksOyt8ZDpWDfVPiCvPo2sR6j5sSY3TlDfRdEfoLS2Q9vLM8AKrn65araa6GqJA2Avmg60xfE5qBaJE2OObUakP-1diWpTVAv43TaZjJvpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حدود ۷۰کشتی در ۳۶ساعت گذشته از تنگه هرمز عبور کرده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/66811" target="_blank">📅 14:07 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66810">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">melbet.apk</div>
  <div class="tg-doc-extra">53.2 MB</div>
</div>
<a href="https://t.me/news_hut/66810" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">✅
نسخه آپدیت شده اپلیکیشن ملبت
🔶
• لینک سایت مخصوص کاربران خارجیMELBET:
🌐
t.me/ConnectMELBET
🔶
• آدرس سایتMELBET
🌐
bitly.uk/connectmelbet
🟠
نکته: اپلیکیشن بدون فیلترشکن کار میکنه برای ورود به سایت باید سرور فیلترشکنتون رو کشور های اسیایی یا کانادا یا ترکیه تنظیم کنید</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/66810" target="_blank">📅 14:07 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66809">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n-WXpQ4AqSuRL296hKpHenFzlX3OvpzYUg3D9sU8A1pRAXN2pQnjyXsUctHMLRd8P2KJFMHWX1b-ZbP-bk4waFk-eMHbh27OW3NF7Ff4WuUTrSswGHfdYPX-x4xU2ENou6mytskF7XX9P-hBR31pXG5Q1T0umnR8FcvOPVrcDE8758MBgPU_grAgEwyCaGo_KOx5z-MrgqFve4df80fm3fP-aubDQeZf0WbkB6ueZhUuEeVS6iLm5djZuErWvGfsRJcjXMWzyG7i5mL60HyNHQtFhWvD-4eNgYhC-UkC4FF8sfchW75uL07w5NP_oR_jr14w1u3BCPZux18sLxSIOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❗️
بهترین سایت برای بت زدن سایت MELBET هست که مورد تایید ماست و خودمونم چندین ساله توش بت میزنیم
💸
با اولین واریز اگر با کد هدیه
ml_459049
ثبت نام کنید تا سقف 100 دلار 130% بیشتر شارژ میشید
واستون لینک و اپلیکیشن ملبت رو میزارم که ثبت نام کنید
🌐
https://refpa3665.com/L?tag=d_3312431m_45415c_&site=3312431&ad=45415</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/66809" target="_blank">📅 14:07 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66808">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ead28978b.mp4?token=FJFeYKtGKZ4Y8j2TpcGsJx1NiADoGTsnENT4-HbLuaVk2E9mOrPhd0FhQnAhBHK10F7kP2UoRyFvHIKl4Xni4wEiN32BS9xm3thgmm3f3OVGyQJwrSMhrSNFxcFA7B3pK7XmzHvI19i2N7oNvnUzvnahLHG9vNsFVfTMH-w4w_puKapoImBO6WYOgzj6ORTfPQGE67KulJBcWyvIOlVlhmw-h5wWvuL-Ku8Us7gFo2UmVKoE9D9yzKKD1tzRwBIU3E8sJGTfa8Uq72OOB1CeljppjA2KRT1xWRqn0UYo9kNB0wl_CQCrvj4cbxPbT5H9d0-HeWGP5C7Wm_vGpaDiBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ead28978b.mp4?token=FJFeYKtGKZ4Y8j2TpcGsJx1NiADoGTsnENT4-HbLuaVk2E9mOrPhd0FhQnAhBHK10F7kP2UoRyFvHIKl4Xni4wEiN32BS9xm3thgmm3f3OVGyQJwrSMhrSNFxcFA7B3pK7XmzHvI19i2N7oNvnUzvnahLHG9vNsFVfTMH-w4w_puKapoImBO6WYOgzj6ORTfPQGE67KulJBcWyvIOlVlhmw-h5wWvuL-Ku8Us7gFo2UmVKoE9D9yzKKD1tzRwBIU3E8sJGTfa8Uq72OOB1CeljppjA2KRT1xWRqn0UYo9kNB0wl_CQCrvj4cbxPbT5H9d0-HeWGP5C7Wm_vGpaDiBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚬
بسیجی‌های صادراتی دیشب تو میشیگان آمریکا نذری بین آمریکایی‌ها پخش کردن
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/66808" target="_blank">📅 13:11 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66807">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba9d2db1fa.mp4?token=MINJmZKt5r173NWkXH1vXQcmJ7oQhyzNesklbhpEdfPegupZgFU0AzWh5QYs-rjcevIPZ2CM3cQQqck83ydm2_BB3ZFYXw8I3_LrTYjpnsm0fhaSRt3L7eG2dcqtsWh8_dSLnK6Wy2Tp5TcUtkVUOFCy6tHCXMV3Uplj04U7BVnJ4SbzZIMflTIOMdVh1jVe-sdyT3vfcWmc2maLBuuw8wlIaOQ7PYmguq8UwpB1QbFkPJfJs8OA4e4TDAK8GNnKs04wA96DIOz6_4ikr8gEv570N8AXtkd4VldL8Cxdz-FhcuR7zCWIfYY45vrc8Ef3x3bfo6X2YZCIphCkPl4_Noi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba9d2db1fa.mp4?token=MINJmZKt5r173NWkXH1vXQcmJ7oQhyzNesklbhpEdfPegupZgFU0AzWh5QYs-rjcevIPZ2CM3cQQqck83ydm2_BB3ZFYXw8I3_LrTYjpnsm0fhaSRt3L7eG2dcqtsWh8_dSLnK6Wy2Tp5TcUtkVUOFCy6tHCXMV3Uplj04U7BVnJ4SbzZIMflTIOMdVh1jVe-sdyT3vfcWmc2maLBuuw8wlIaOQ7PYmguq8UwpB1QbFkPJfJs8OA4e4TDAK8GNnKs04wA96DIOz6_4ikr8gEv570N8AXtkd4VldL8Cxdz-FhcuR7zCWIfYY45vrc8Ef3x3bfo6X2YZCIphCkPl4_Noi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هنوز تو این دوره و عصر مدرن یه سری کسخل وجود دارن که با عقاید عصر حجر خودشونو بگا میدن
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/66807" target="_blank">📅 13:02 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66806">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/81f4c39a8d.mp4?token=jsP-a0FaJrP9Sd081EAtdqLlsJeRQYU0dD-U-pw-on5WFTxj5FWQ6AIO0PVkUyG1b4VbRQH8HKABfpknNbpCLbSH_TSNTdV6ZZJlGKT2IyRYMWzIHlykJSSmmgiBQj-l4FWB8EnELy8YBzomVsNAJso23IrBUrtKZvEc6VV74vlR_C64cgGRtYj6HPi8Me2AfMr44iE_7-OkBM-XOaRzFv2AiMIQhMXHvSXzYLME3jP6lEU5rBs9ceCsrg0OhrbnsEXhwKtO7sg8r1c2iWMi82vEr8MuQg2skFdG5JNcVu_nylJY_iEbw10Zk_3e2-dx-xNbiXgkjfgfqv0b4-lsEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81f4c39a8d.mp4?token=jsP-a0FaJrP9Sd081EAtdqLlsJeRQYU0dD-U-pw-on5WFTxj5FWQ6AIO0PVkUyG1b4VbRQH8HKABfpknNbpCLbSH_TSNTdV6ZZJlGKT2IyRYMWzIHlykJSSmmgiBQj-l4FWB8EnELy8YBzomVsNAJso23IrBUrtKZvEc6VV74vlR_C64cgGRtYj6HPi8Me2AfMr44iE_7-OkBM-XOaRzFv2AiMIQhMXHvSXzYLME3jP6lEU5rBs9ceCsrg0OhrbnsEXhwKtO7sg8r1c2iWMi82vEr8MuQg2skFdG5JNcVu_nylJY_iEbw10Zk_3e2-dx-xNbiXgkjfgfqv0b4-lsEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پرستو نظام با کلی عمل زیبایی که البته هرچیزی شد بجز زیبا: قلب من با امام حسینه
😐
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/66806" target="_blank">📅 12:34 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66805">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f836563943.mp4?token=meHc4rZABhFHx9IgpYST5Iai-cJWDPR_rI_gV7HnZQ3N1h9Nn2YhM_qqAIV82gGEm8HcvNIJfqWXqzaSXSRdY1UB0OtiuBzIhgNAAdJjehjOhD8k67AXR56VTzyD4jDyHbxPmL4w91ftUe_wHilRpzNDdNsjjOeIz1MZODiaIsQgENZzcriufnYiZTI8PxFjg6Tdo1RVuxlaBaeVnsyvGKVDVSawi5y6Z6-MJs7sb1b8-NWsz-sqSciRO_ADTBdOydka6hHuSDo4aF0uWF5my6Q-wk88UiNZH8vynuxScasINqg2UbBu7NAH7lgtjuMQHCgySfZIYyQDfyjwp7CfKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f836563943.mp4?token=meHc4rZABhFHx9IgpYST5Iai-cJWDPR_rI_gV7HnZQ3N1h9Nn2YhM_qqAIV82gGEm8HcvNIJfqWXqzaSXSRdY1UB0OtiuBzIhgNAAdJjehjOhD8k67AXR56VTzyD4jDyHbxPmL4w91ftUe_wHilRpzNDdNsjjOeIz1MZODiaIsQgENZzcriufnYiZTI8PxFjg6Tdo1RVuxlaBaeVnsyvGKVDVSawi5y6Z6-MJs7sb1b8-NWsz-sqSciRO_ADTBdOydka6hHuSDo4aF0uWF5my6Q-wk88UiNZH8vynuxScasINqg2UbBu7NAH7lgtjuMQHCgySfZIYyQDfyjwp7CfKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یکی از هیئت‌های گناوه بوشهر یه مداح به این شکل از جاویدنام‌های وطن یاد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/66805" target="_blank">📅 12:02 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66804">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63f61a8cbb.mp4?token=p-wk4mockM9oIBVQ2N469o6ddg3V_IhvtodgkfpclK_vxlqAtlohZwjo5GXeOAhdnh6U1hC5FuCPdaGvwKJGZnHnuc-iYMFnro6R9o3eE--XNDzzXPxq5WWh-KhF2D7f393vkRDCx8EHaZrezdvHU7L-8QP_r5E0dpUabqx4NmxsSfVjMKpxz8AVduzceMRZis019QknkUfVnimE69Q0mTAGa7fySasWgLUKbIoUFZD4sdonln9lgDEnBEV1LupQJCiZUNabin4rscSX6_d04mEavWkDbzcBkd6Jqc8i2GH2921TXc8AeTbivmh9-aJTCCa8Gg9I3CjaEIazH-uSQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63f61a8cbb.mp4?token=p-wk4mockM9oIBVQ2N469o6ddg3V_IhvtodgkfpclK_vxlqAtlohZwjo5GXeOAhdnh6U1hC5FuCPdaGvwKJGZnHnuc-iYMFnro6R9o3eE--XNDzzXPxq5WWh-KhF2D7f393vkRDCx8EHaZrezdvHU7L-8QP_r5E0dpUabqx4NmxsSfVjMKpxz8AVduzceMRZis019QknkUfVnimE69Q0mTAGa7fySasWgLUKbIoUFZD4sdonln9lgDEnBEV1LupQJCiZUNabin4rscSX6_d04mEavWkDbzcBkd6Jqc8i2GH2921TXc8AeTbivmh9-aJTCCa8Gg9I3CjaEIazH-uSQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شیره چرا شبیه یارو خپله تو آل زبیر نشسته
😂
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/66804" target="_blank">📅 11:01 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66800">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80f5246ce8.mp4?token=H7KIQyQzfZYb7MnJVAFe79nBjhyUwlK2FBC0R_fbWnfQraenKeUnY4btrve0d1eZB1m44NCis1hCQz9EnrywLLs5KZ21H5zcL8JtLmfFxqK3KdVp11k3nV-_oFLounkNdta5pu2dwnGpS8-C-gyryM4yGCxk2bllScInFf2IW4vip7qU5THz4PookIvphdqAa0P7V2HHJrVgSsFLWJriOprpzRGmun_vxvdmXptzTf6o2TAEvIBxtfWWDZBem4Mr-Ydi1uHIR8feTuSC08tt2EIt_RGHA9reou8wlupYqfeK3z0z1lQC0DGdahPonTLDxmrrCV6duCJ1pS9rdCi4mA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80f5246ce8.mp4?token=H7KIQyQzfZYb7MnJVAFe79nBjhyUwlK2FBC0R_fbWnfQraenKeUnY4btrve0d1eZB1m44NCis1hCQz9EnrywLLs5KZ21H5zcL8JtLmfFxqK3KdVp11k3nV-_oFLounkNdta5pu2dwnGpS8-C-gyryM4yGCxk2bllScInFf2IW4vip7qU5THz4PookIvphdqAa0P7V2HHJrVgSsFLWJriOprpzRGmun_vxvdmXptzTf6o2TAEvIBxtfWWDZBem4Mr-Ydi1uHIR8feTuSC08tt2EIt_RGHA9reou8wlupYqfeK3z0z1lQC0DGdahPonTLDxmrrCV6duCJ1pS9rdCi4mA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
تخریب آخرالزمانی در کاراکاس ونزوئلا پس از زلزله7.5 ریشتری
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/66800" target="_blank">📅 10:31 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66799">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b3743ac3a0.mp4?token=gm_iqpngBWLI5-TmXMx-BUfPJtkDM_pKsQtS4tqz8eYT-0RDCxp5cd7-2lNrMq8sU3Sj3VfYPi_QY8JLyl7JQuZWP8rU7GQQBrDQ72LgzbtF44L0As2fXeLiszSZhE7kursQNJ1HaV86pwf3emnNKPtGWaeqkLz4XIGjb6gFvNO4slMJahyrKpTsrMAODMF6dkTKiTtygk9-EHOYKDa_LX-HiX2x9KQ_BCDv6WW6Yw38ZIDsn2FQtJulm742X7Z6q669tt3p_l2gnTDbI3RTjzdD6b0VqQr2BS_zAeJTHP9521MxMhPJUxBUJ8UvIp9GaJ_GDvM19kkvF6OzOA_ghk5Bnd5g_QEJ8hGG06smJjuJ1xAT7qI7gWGPOe5tm3UTFRt03KGOP2TV32ZkjbluDmPKTlmhad3w76SEj_kFcCMGGmaNNV6Mi965wzT6hczlVw3hBbJByHM2oJUcgObrarwKXNx5LIA9fMvll0_XUCw2yu0cZ2eWsv50ycHU0vdt3K94yxdVwHYu6fPbi1IehZixuEt9kyqDNm-lHeYsGCU2_pTb_-3FeV4AfZhsfP8bP8YWqfJ5QDxGKqXA54Xw2C36XsiJSnUCN3I1WvvZRASCuyNiC-iVpQ1LJSUPOnfgJ70W-hl-YAQn6dmkHg_u-pig4_3h9gowZtLzdd2lXqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b3743ac3a0.mp4?token=gm_iqpngBWLI5-TmXMx-BUfPJtkDM_pKsQtS4tqz8eYT-0RDCxp5cd7-2lNrMq8sU3Sj3VfYPi_QY8JLyl7JQuZWP8rU7GQQBrDQ72LgzbtF44L0As2fXeLiszSZhE7kursQNJ1HaV86pwf3emnNKPtGWaeqkLz4XIGjb6gFvNO4slMJahyrKpTsrMAODMF6dkTKiTtygk9-EHOYKDa_LX-HiX2x9KQ_BCDv6WW6Yw38ZIDsn2FQtJulm742X7Z6q669tt3p_l2gnTDbI3RTjzdD6b0VqQr2BS_zAeJTHP9521MxMhPJUxBUJ8UvIp9GaJ_GDvM19kkvF6OzOA_ghk5Bnd5g_QEJ8hGG06smJjuJ1xAT7qI7gWGPOe5tm3UTFRt03KGOP2TV32ZkjbluDmPKTlmhad3w76SEj_kFcCMGGmaNNV6Mi965wzT6hczlVw3hBbJByHM2oJUcgObrarwKXNx5LIA9fMvll0_XUCw2yu0cZ2eWsv50ycHU0vdt3K94yxdVwHYu6fPbi1IehZixuEt9kyqDNm-lHeYsGCU2_pTb_-3FeV4AfZhsfP8bP8YWqfJ5QDxGKqXA54Xw2C36XsiJSnUCN3I1WvvZRASCuyNiC-iVpQ1LJSUPOnfgJ70W-hl-YAQn6dmkHg_u-pig4_3h9gowZtLzdd2lXqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کاروان اجنه و فرشتگان:
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/66799" target="_blank">📅 10:03 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66798">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/638875c442.mp4?token=S0dYlzkb_yj2j7aHXckY88kyjgCi2KEruUj4Ppj2f_UEdPLc3-iRT1hI4eYQuyoT1bzmMyTySMulVPwxLDDlTbrRD3jHlgpvVEhTGmGvDf3ZVownIXJhW46ocbW2s26qYA8DPBGkgKY42lwUNMC1WTYojem9cqJiPToJl1dnDD3BisYkjHAtTx-6DBJXzfaeLlHnaA3b6LXH_7DBWdtIfZ1TafEz0nsXfEqkbk6N4svpNvbUMvWseLQZptzqJjwE_5Xk7xCDp12ATTB96TBSjBdlUZxdyccwlY9coTeBgKyms1m8TWw-1hFuxxvjotgoAjeqWbBcQWwqOBTgCKkz4w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/638875c442.mp4?token=S0dYlzkb_yj2j7aHXckY88kyjgCi2KEruUj4Ppj2f_UEdPLc3-iRT1hI4eYQuyoT1bzmMyTySMulVPwxLDDlTbrRD3jHlgpvVEhTGmGvDf3ZVownIXJhW46ocbW2s26qYA8DPBGkgKY42lwUNMC1WTYojem9cqJiPToJl1dnDD3BisYkjHAtTx-6DBJXzfaeLlHnaA3b6LXH_7DBWdtIfZ1TafEz0nsXfEqkbk6N4svpNvbUMvWseLQZptzqJjwE_5Xk7xCDp12ATTB96TBSjBdlUZxdyccwlY9coTeBgKyms1m8TWw-1hFuxxvjotgoAjeqWbBcQWwqOBTgCKkz4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قلعه سریزد  ، یزد
شاهکاری از معماری باستان
جایی که قرن ها پیش مردم اشیاء ارزشمند خود را در اتاقک‌های امن آن نگهداری می‌کردند
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/66798" target="_blank">📅 09:32 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66797">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lh2nlEs4i5VJB0Gl0FDiuCBkjNPWUhy0d_vpbfSSyU0FMTHx__EOzF0FrhEFBf1JqYYwgKdPiwN0b_mhFvqgfdAdG-piMfv_KdNDIGyw3f3icXQ5bpE1PDTBpis0NUF8cknnt2gg40h_Y3NwJXd2YTw6xrDcB5UejGu6Aamn_TBbd2tId2dgsQKKWBO9LaxUGEFC1QvIOhE3W0BOuhQoXzZeK8HX4cJJ4k9j19pxsWiWSIQUh43l2onWXFTjchuUPS5PS2O6_baGFo6qPNOv4svZ28a6kreKiIml3gPvmZfw3zgC4IeyUYt1H-jRonDboR50J2UxsmxkxUZ2HBcTvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
دونالد ترامپ:
دو زلزله بزرگ که اخیراً ونزوئلا را لرزاندند، بسیار عظیم بودند و تعداد زیادی قربانی برجای گذاشتند. ایالات متحده آمریکا آماده ارائه کمک است!
16;من دستور داده‌ام که تمام دستگاه‌های دولتی ما برای اقدام سریع آماده باشند. ما برای حمایت از دوستان جدید و فوق‌العاده‌مان حاضر خواهیم بود. گزارش‌های اولیه امیدوارکننده نیستند!
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/66797" target="_blank">📅 09:27 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66796">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">‼️
از ناوشکن هسته‌ای کره شمالی رونمایی شد
🔴
رسانه‌های دولتی کره شمالی گزارش دادند کیم جونگ اون اعلام کرده است نیروی دریایی این کشور به سلاح هسته‌ای مجهز می‌شود و کشتی چوئه هیون رسماً وارد خدمت شده است.
🔴
این ناوشکن ۵۰۰۰ تنی به سلاح‌های ضد هوایی و ضد کشتی مجهز است و قابلیت حمل موشک‌های کروز و بالستیک با توان حمل کلاهک هسته‌ای را دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/66796" target="_blank">📅 09:01 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66795">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/66795" target="_blank">📅 03:14 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66794">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/66794" target="_blank">📅 02:23 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66793">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/V1DLiiXnv2NVGzeqmVaRQDNP1Y3ZbMZZVJwDrz7wKhtOdYn9xeNHcd3o_sqTMCjt8x9DovOtkfewT3OemMC6SvM3_l3gX6uk_qYtp3WZaO_uGdPO5BaNynuXo0O33ciROEatWvmMtq37jR-OElVCCI0vwEKnysozbE1LoMgMn7Ppj_dZrs0lPHDkzIXroH9KDlvzGbWuOuSuaxYbYjq1x8owHV4MzW41DGHGHl3awOdxS8tgrinSyNyEyffaK5iMiU-3kCaJMaRSKIJK2k166ezrvtJSv-gVnM3VtaO6u_Oa2DXXSlJd3RQk6QVFaL-90tSrhDscAQAbEz5dbtsvHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/66793" target="_blank">📅 02:23 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66792">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f17bcbdae9.mp4?token=Ok0fEZCOye6q_NH7E51SkD1WoECaMJ_CT9MtpLb1dxTrUuHE2decW2RMX9xrYarApzqKBDMVDlfkkUQPR8YOAdBc88RQS5y-BLunhkwNEztCYsWAAoip0yeoidkVFWzTKJCtWRcNUFFl_iaSyi-8LJwlCdWN5pW6NddiTKgNtlOAiwQ1627ljqQFbYYNOL68R_gvs3S-MNan0Njx25N13e7wMbIxjL-olugRYerPv2Pba6QkoGawcC_hiGqW_mnez3vUgaXN0q_L0Ybx24w48eNViOHjKRshPSpsoR2VgNkyn8r6xjPF23KOCYdZgjUgZNQZ37uw00qHPtfQY_MscA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f17bcbdae9.mp4?token=Ok0fEZCOye6q_NH7E51SkD1WoECaMJ_CT9MtpLb1dxTrUuHE2decW2RMX9xrYarApzqKBDMVDlfkkUQPR8YOAdBc88RQS5y-BLunhkwNEztCYsWAAoip0yeoidkVFWzTKJCtWRcNUFFl_iaSyi-8LJwlCdWN5pW6NddiTKgNtlOAiwQ1627ljqQFbYYNOL68R_gvs3S-MNan0Njx25N13e7wMbIxjL-olugRYerPv2Pba6QkoGawcC_hiGqW_mnez3vUgaXN0q_L0Ybx24w48eNViOHjKRshPSpsoR2VgNkyn8r6xjPF23KOCYdZgjUgZNQZ37uw00qHPtfQY_MscA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
درست در میانه یکی از مهم‌ترین مسائل، ناگهان خبر فوری منتشر می‌شود: “سنا رأی داده است که می‌خواهد ترامپ جنگ را متوقف کند.”
ایران این را می‌بیند و می‌گوید: این دیگر چیست
؟
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/66792" target="_blank">📅 01:15 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66791">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6928b1a5c.mp4?token=v1e21ldOZeUZ_ySPHMtT674Zx2fxoUYK3up5Wo2VTHi3gOKLdN6gfF1ObgestVXpKUVfaZ1Y0ozvrgcOtFk9b0f3MZ5r5u3OkBDOO5YxFgrUgGRn536vV94t9IlwCRX2FRhtpnAIUOkwetNjXcp4fcy3JJbP_Va8cKeCdqHknMxBUK8qE-jLUcimOM0XMDlVV8WONJtiKgBxwG7-S9D5AaXZo_GQvde9TLHhph0luG4DPnu48JtkehsDjWyiahsqG7EBAwL7PGm8d0iajYTbbZZpc0PA8xWP0XmZvWIjutBqdOdYlFmGaUNeZJV6R9ezoe4rWoVCVviQzdAjU293mQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6928b1a5c.mp4?token=v1e21ldOZeUZ_ySPHMtT674Zx2fxoUYK3up5Wo2VTHi3gOKLdN6gfF1ObgestVXpKUVfaZ1Y0ozvrgcOtFk9b0f3MZ5r5u3OkBDOO5YxFgrUgGRn536vV94t9IlwCRX2FRhtpnAIUOkwetNjXcp4fcy3JJbP_Va8cKeCdqHknMxBUK8qE-jLUcimOM0XMDlVV8WONJtiKgBxwG7-S9D5AaXZo_GQvde9TLHhph0luG4DPnu48JtkehsDjWyiahsqG7EBAwL7PGm8d0iajYTbbZZpc0PA8xWP0XmZvWIjutBqdOdYlFmGaUNeZJV6R9ezoe4rWoVCVviQzdAjU293mQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ درباره حمله به مدرسه میناب:
«نمی‌دانم که آیا آن‌ها هرگز خواهند توانست این مسئله را حل کنند یا نه.
موشک‌ها از هر طرف در حال پرواز بودند.
کسی گفت که آن موشک متعلق به ما بوده است. شاید بوده باشد، اما من هیچ چیزی ندیده‌ام که مرا به این باور برساند که واقعاً موشک ما بوده است.
موشک‌های فراوان دیگری هم توسط افراد و طرف‌های دیگر شلیک شده بودند.»
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/66791" target="_blank">📅 01:12 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66790">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">Live Volleyball</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/66790" target="_blank">📅 01:12 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66789">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5fa6495873.mp4?token=bOJvxr60FdczTjpNsBejRtrx3VmSY8SaBPrqEwlMR80yxcXRzq9ZbcIIIuqxBCTfd278VEdFiss7UL-aqenTdkwByiG-wZhW31fheI-bk1zYcOhXLjmwq0BIdMYLdteZQAfvm8vBKG07eToxqVP9Daj7yVw8jN7mgTAMiZsIbVLl2n1fHaqV924XTuFVTFQ8Tw3Q-htlYgkAVCB5YjYjTI6OakO-DbXIEetBsTqj7ElsEGBcMoM99LpXAOdNsce0Rcz516w-dozJBVAfpxuIuUpssV2_cumTZt0tPS0TqkF8R17GPHyT0fhwbWb5lhwOvtfT7vI37jDUFVwJw7pWgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5fa6495873.mp4?token=bOJvxr60FdczTjpNsBejRtrx3VmSY8SaBPrqEwlMR80yxcXRzq9ZbcIIIuqxBCTfd278VEdFiss7UL-aqenTdkwByiG-wZhW31fheI-bk1zYcOhXLjmwq0BIdMYLdteZQAfvm8vBKG07eToxqVP9Daj7yVw8jN7mgTAMiZsIbVLl2n1fHaqV924XTuFVTFQ8Tw3Q-htlYgkAVCB5YjYjTI6OakO-DbXIEetBsTqj7ElsEGBcMoM99LpXAOdNsce0Rcz516w-dozJBVAfpxuIuUpssV2_cumTZt0tPS0TqkF8R17GPHyT0fhwbWb5lhwOvtfT7vI37jDUFVwJw7pWgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پرچم نروژ فقط یک طرح ساده نیست
🇳🇴
...
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/66789" target="_blank">📅 00:18 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66788">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6390fb697.mp4?token=I-w_WcWgdX3RVerkS0gp292pkUd06IZq2KMoJZ0HAxtE7PmL1iWLqVTHwLy8ThTRf3iQGkOfxsyLddmBQv5-jb8pkujLrUdEw8iJNdLBkTADdktW3yJveqSDihla8w3O4glwGSf2v_9DFP05jDm9R6UgcPXqAG0ybuw3dSkkkxohM3XcAiDTbwYllpnESs11b7AmE1HMZV1v34SNplfbr72XZmGwlt-LKN4t2jYnBYWLUjprwKF84bHD81WBKFcLFQ0V2E8VRCpdX8XtelwtOSDJjAcEO_M81KO3QxPkWnq9Dm0NOFHCHe6uABp9OsK-Cb6LptEyTbFS86kswNnD9SfL4gLDiGNW8zk0DZiNtXj1T5H9S5_YTvlEWY24zJ_fP9VNz8xxe8v_j-7bRdpF1pPfuzQc7FtKXjJwGMsLRF47K4RL7Bk1VbnBKTlj7WiGh4O5QSwAyAZBb64r9k7UncF9RL_xNpXNtonNwbzwsakyN4gedVKJRCqKZI677asOKRuQ8CdSOIBIBnJZkw-pXksJ0ndVPyudUuCb_uVPgexmo2D_Y9jPhdhupl9efWb90MY3H8bcQcd7xjkw1-5QtcUDOhIEh8NCwDb_OYId4YcpJohVTlhtx0SIUWTvfoswM9i0qNMrldUXjNy9rFYNF0yb2wdeSKrMpN2Bgu7_wtk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6390fb697.mp4?token=I-w_WcWgdX3RVerkS0gp292pkUd06IZq2KMoJZ0HAxtE7PmL1iWLqVTHwLy8ThTRf3iQGkOfxsyLddmBQv5-jb8pkujLrUdEw8iJNdLBkTADdktW3yJveqSDihla8w3O4glwGSf2v_9DFP05jDm9R6UgcPXqAG0ybuw3dSkkkxohM3XcAiDTbwYllpnESs11b7AmE1HMZV1v34SNplfbr72XZmGwlt-LKN4t2jYnBYWLUjprwKF84bHD81WBKFcLFQ0V2E8VRCpdX8XtelwtOSDJjAcEO_M81KO3QxPkWnq9Dm0NOFHCHe6uABp9OsK-Cb6LptEyTbFS86kswNnD9SfL4gLDiGNW8zk0DZiNtXj1T5H9S5_YTvlEWY24zJ_fP9VNz8xxe8v_j-7bRdpF1pPfuzQc7FtKXjJwGMsLRF47K4RL7Bk1VbnBKTlj7WiGh4O5QSwAyAZBb64r9k7UncF9RL_xNpXNtonNwbzwsakyN4gedVKJRCqKZI677asOKRuQ8CdSOIBIBnJZkw-pXksJ0ndVPyudUuCb_uVPgexmo2D_Y9jPhdhupl9efWb90MY3H8bcQcd7xjkw1-5QtcUDOhIEh8NCwDb_OYId4YcpJohVTlhtx0SIUWTvfoswM9i0qNMrldUXjNy9rFYNF0yb2wdeSKrMpN2Bgu7_wtk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیویی که یه عده از طرفداران حکومت با هوش مصنوعی از «مختارنامه» جدید درست کردن
🤣
🤣
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/66788" target="_blank">📅 23:55 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66787">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fIul1qvneFXJHPmi2ID4XTcrTNEfzoYBBryTjgQsPTDv5Dn_7LXRKGU2uCppRV8BL-FS9a3iVEwDgRm_eVx3P0YFRMSm4F9rrfVzCPnTGsNlTKSHmjz2Ra9vpvFDDP-gtxrdSzw8zNGP5BkMHaia0bNuoDTX0FCEcnIneG7rzSxnQwbjCYMQ_0phYkxRJvKJFtEVRg3vKoZJQ5VIY7fam5rHmue9nyohsckwBXa9MR4_cZodfcZwY6Fnf1sZG08WRQHS3p11nTBjyEq2abBfKhw_2zJtKqPjj2JFGKi09Wk7S_9k-H6qyAFZPHoYgRRH2TVymXQaCNpxqoOfnG4Kcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سخنگوی وزارت امور خارجه:
اظهارات متناقض آمریکا درباره یادداشت تفاهم برای پایان جنگ به کاهش بی‌اعتمادی ایرانیان کمک نخواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/66787" target="_blank">📅 23:53 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66786">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">شایعه شده ایلان ماسک قبل اینکه میلیاردر بشه تو فاک بت جوین داده بوده
🔥
با آنالیز حرفه ای ادمین های فاک بت ، بصورت رایگان از فوتبال دیدن پول در بیارید  با فاک بت ، حرفه ای تر شرطبندی کنید
❤️
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/66786" target="_blank">📅 23:53 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66785">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/b_5CNEAer8jHa-Z_Sz1iU3ir4TaVmgvFEncbYwWluiKbJHebwYkXAVsI2KhYZdDgPsuGQYZDvRDVfVUyjDz9uOIKFDYI6jxp6j_XLocoP45UfruMJcpNM52dsbjBpj5Chr1WbVYv23YeDN4eerxuLner3MJLv7Fv1gezEWgF6tKRY3jDfCo3A7-dAzswP72fo_LX3xDboNlaj3LMPPz9nWLDZOtodD9ekY1ZeGDA9fzguZ0EiQM2DtM80pl-3Aua5-D6N_BgS_AzH8q1_B89gondPzYsu7Cn1uXO0iNGx8lCDqGXv9zCDzVapNyFkLtSVxm6uYYP7AOPZV0zGgh8Jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شایعه شده ایلان ماسک قبل اینکه میلیاردر بشه تو فاک بت جوین داده بوده
🔥
با آنالیز حرفه ای ادمین های فاک بت ، بصورت رایگان از فوتبال دیدن پول در بیارید
با فاک بت ، حرفه ای تر شرطبندی کنید
❤️
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/66785" target="_blank">📅 23:53 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66783">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f56950043.mp4?token=hLXM_4zJfhAS7lNfQ2_wx3NMkNu5exaT5z211bz6Rkl1dBdXeIiKG1MVpfbCf_JRRJMZ8GTjFMxJr51CB-dISfujpWRaa1AJBFBp3KMBQPW2eRjFaiDEFi3N_PTIwliVI6syS4peEjtb1p0uZae712QNWrqXxuKgPusowrCl9wGNfprMiMOPpQes9bFju1BQq5X1ty1CFqZFt4vvshitXvDjbA6LcznxoszR8NHYJjZnZvAAcoFfq7IMdkZQrNz5RY96YFwjBzlVWLp4bgMzKmC4caBrCOV5C7cAoIueMWVjcxy_OCei21-dQWCs2tyVl8r3NK2loyrxBMgwBI_7_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f56950043.mp4?token=hLXM_4zJfhAS7lNfQ2_wx3NMkNu5exaT5z211bz6Rkl1dBdXeIiKG1MVpfbCf_JRRJMZ8GTjFMxJr51CB-dISfujpWRaa1AJBFBp3KMBQPW2eRjFaiDEFi3N_PTIwliVI6syS4peEjtb1p0uZae712QNWrqXxuKgPusowrCl9wGNfprMiMOPpQes9bFju1BQq5X1ty1CFqZFt4vvshitXvDjbA6LcznxoszR8NHYJjZnZvAAcoFfq7IMdkZQrNz5RY96YFwjBzlVWLp4bgMzKmC4caBrCOV5C7cAoIueMWVjcxy_OCei21-dQWCs2tyVl8r3NK2loyrxBMgwBI_7_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در ازای شهادت مقام معظم رهبری چی از آمریکا گرفتید؟
قالیباف:
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/66783" target="_blank">📅 23:15 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66782">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78f387d3e0.mp4?token=g9xbMHyNUsopld147XNdO0GUaPx1_4SID9nFA9fguoXKhCYutIcdiJ_06GZdbP2R1UdN8RGIJJM0TYJh0GlsrnbkzDvZlZOWPJenJub7U6_aWaZLdRsCig4OlDxjxYqO2Jh8-dun_9lcYsf2T3uYq3_TWzn1MOVZ1R7rbA-BYadv_oaNeC5lJiBssZTqRtAKPNTF6YD2Bv3VGsLw_6MXoeLTBa_JSallOVHSSli5qHlLz-sQHhjiQwim7uMC_8BjsAWw1rPzCRo2MSOOrvGpxnlOBL9-td-oPMJPGf6EFzZ7zga-GZmvyL5IuXHBFbG-BhB-_BNrxeffuN7ny-94jQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78f387d3e0.mp4?token=g9xbMHyNUsopld147XNdO0GUaPx1_4SID9nFA9fguoXKhCYutIcdiJ_06GZdbP2R1UdN8RGIJJM0TYJh0GlsrnbkzDvZlZOWPJenJub7U6_aWaZLdRsCig4OlDxjxYqO2Jh8-dun_9lcYsf2T3uYq3_TWzn1MOVZ1R7rbA-BYadv_oaNeC5lJiBssZTqRtAKPNTF6YD2Bv3VGsLw_6MXoeLTBa_JSallOVHSSli5qHlLz-sQHhjiQwim7uMC_8BjsAWw1rPzCRo2MSOOrvGpxnlOBL9-td-oPMJPGf6EFzZ7zga-GZmvyL5IuXHBFbG-BhB-_BNrxeffuN7ny-94jQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ در مورد ایران:
ایران خیلی خوب رفتار می‌کند. آنها با هر چیزی که من می‌خواهم موافقت می‌کنند و باید هم موافقت کنند.
در غیر این صورت، ما فقط برمی‌گردیم و کاری را که باید انجام دهیم، انجام می‌دهیم
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/66782" target="_blank">📅 22:53 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66781">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/98a05f2cc6.mp4?token=Kb_KY_sWPI5xT7QPb--mpz4u5efwHFx2OuigDkUrLI_QPagqT8c1YjuXAo2drES1f-aH-EDoCq-RT4WH2qaav4gOE8X4pZkCv6_O1UbL2v51KvWfF9oFyZezMuuzKsEc5N94IPkXikTLwf78jM29gM8jrZsTl7z9J385sSqZtiQRRqaPF8zzbRve3oDAB8_f42T8tf4q3dFRG-goqQKSqK_KspzJAIiVJoiT4XEfqVR4Ao4naJAkcIbXZhoIIChYeTtUq33vxDuB6Ik_rKJ68KVOBD0Lbth5R1enOVXbj-bjFwQ0-qVUP07x8TrKQvNHRymvo30kdrasxIFH_axUMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/98a05f2cc6.mp4?token=Kb_KY_sWPI5xT7QPb--mpz4u5efwHFx2OuigDkUrLI_QPagqT8c1YjuXAo2drES1f-aH-EDoCq-RT4WH2qaav4gOE8X4pZkCv6_O1UbL2v51KvWfF9oFyZezMuuzKsEc5N94IPkXikTLwf78jM29gM8jrZsTl7z9J385sSqZtiQRRqaPF8zzbRve3oDAB8_f42T8tf4q3dFRG-goqQKSqK_KspzJAIiVJoiT4XEfqVR4Ao4naJAkcIbXZhoIIChYeTtUq33vxDuB6Ik_rKJ68KVOBD0Lbth5R1enOVXbj-bjFwQ0-qVUP07x8TrKQvNHRymvo30kdrasxIFH_axUMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
«جنگ خیلی خوب پیش می‌رود. همانطور که
می‌دانید، ما با اختلاف زیادی در حال پیروزی هستیم. ایران امتیازات بسیار بزرگی می‌دهد. خواهیم دید چه اتفاقی می‌افتد، اما بسیار، بسیار، بسیار قدرتمند بوده است.»
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/66781" target="_blank">📅 22:25 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66780">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00a25b4d46.mp4?token=SJzCqr01oj1zh2E3_toPDDi9kKiOaDV1nM0B3iDBG-F9qrifGGtNfWmPJpWyFbXXxF_GbeFQ1o3pdtMTqTSyNtadaROdbN04LD2eU5Tqj-HVv4Nj5YzjJm0G1EO_jDFcSK8tWM_erI_PU1BIPnvMOFZSfOF-CFxPRvJ002vEdohriZhlNJb1StjZLUKdk184VD6aOGjDHB_-vBPz_aHmews4aMt6zqCI7_v4Y-kt_O8FFCWoshHpteXZwN-hddiDfYCXk472DjQVPUBB25lAhpX5XH4M33xhq8mlfuybz4hlycAe5YWU8-M4SQy9Q16u3Z9Q0ef0ideyzdH_Gn7uEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00a25b4d46.mp4?token=SJzCqr01oj1zh2E3_toPDDi9kKiOaDV1nM0B3iDBG-F9qrifGGtNfWmPJpWyFbXXxF_GbeFQ1o3pdtMTqTSyNtadaROdbN04LD2eU5Tqj-HVv4Nj5YzjJm0G1EO_jDFcSK8tWM_erI_PU1BIPnvMOFZSfOF-CFxPRvJ002vEdohriZhlNJb1StjZLUKdk184VD6aOGjDHB_-vBPz_aHmews4aMt6zqCI7_v4Y-kt_O8FFCWoshHpteXZwN-hddiDfYCXk472DjQVPUBB25lAhpX5XH4M33xhq8mlfuybz4hlycAe5YWU8-M4SQy9Q16u3Z9Q0ef0ideyzdH_Gn7uEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
عبدالناصر همتی:
اگه کیفیت ذرت و گندم آمریکا خوب باشه ازشون میخریم.
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/66780" target="_blank">📅 22:04 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66779">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sBYHz9KTjCXmiEsN3vQ_aoM8eNsuCKWCFyiJioj4mLK_mI5dZ54F9FlbWK1-GSrQxDMo5qrEa5PKEae42NoGsubHvoy6czj5nuXVeXmgKSZUcZXiXJGlaUVuJYWZUwiPGwRb8NDtj27JtyYUcPaoqmA9-X74yI0-EkfDWptid5zNufRAVtw_abCRr45TTygf7vuCvMWkgRNiC0OU_12FrXOH5NOPb89sgOLLloaj_DVbD4bklOWsdA5PCcHLgDofLfWiZoFvgZJIQYJrq4tp14vVmtZZNNqdNhcvphVdAn9L_Z4nMrhK79NbaTyYRSKbvRGUm06vmL-Y23nvtbWb2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
اتاق جنگ اسرائیل به مارکو روبیو:
رژیم جمهوری اسلامی و حامیانش در عمان در تنگه هرمز هزینه دریافت میکنند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/66779" target="_blank">📅 20:47 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66778">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd80a69999.mp4?token=iWHEQnnr943fppfrn_5az7hceVGqgnTVeuEm_cRYP874oXb-wx3eKUzhhK0TietUene34ZC7k7ImmpxDbuAHAEJb2X2-V9es3cTqxM4lAqydI70Hk2-c17a29zv1goMiZDN5gHrYXKn0S8rOSDWRUHmaymOWHA1T4Ww9rr0t0ZMMbo-zEt4YUBxWT5doxiRtDpGx_K-kQ9jRu35B2FF95B0P5jIVZAhZlJtDFJRhoDiU_269gMFFJZJ7_yGMEkLWGgO2Hjm-J6n929_6fXLNVFuoE-fiqEcxgoRDpBa0XpSjNvpcrKTnACLm7EG-biDmxaIn4uXGRoVYu360mTuVoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd80a69999.mp4?token=iWHEQnnr943fppfrn_5az7hceVGqgnTVeuEm_cRYP874oXb-wx3eKUzhhK0TietUene34ZC7k7ImmpxDbuAHAEJb2X2-V9es3cTqxM4lAqydI70Hk2-c17a29zv1goMiZDN5gHrYXKn0S8rOSDWRUHmaymOWHA1T4Ww9rr0t0ZMMbo-zEt4YUBxWT5doxiRtDpGx_K-kQ9jRu35B2FF95B0P5jIVZAhZlJtDFJRhoDiU_269gMFFJZJ7_yGMEkLWGgO2Hjm-J6n929_6fXLNVFuoE-fiqEcxgoRDpBa0XpSjNvpcrKTnACLm7EG-biDmxaIn4uXGRoVYu360mTuVoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
مارکو روبیو:
توافقات اخیر با رژیم جمهوری اسلامی بخشی از یک روند مذاکره‌ای و یک اقدام موقت ۶۰ روزه است.واشینگتن انتظار دارد تهران به تعهداتی که در سوئیس پذیرفته پایبند بماند و در غیر این صورت، پرزیدنت ترامپ ابزارها و گزینه‌های مختلفی از جمله بازگرداندن تحریم‌ها را در اختیار خواهد داشت.این تعهدات به صورت روشن و صریح مطرح شده‌اند و ادامه مسیر مذاکرات به میزان پایبندی رژیم جمهوری اسلامی به آن‌ها بستگی دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/66778" target="_blank">📅 20:09 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66777">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ffe99615e.mp4?token=HkRRhL6synjWzi9QQPTvK_5DBWizFKArqhq2QoJkj3lnuaQJBMWOmpPI4Kh2kXbylWErDaFPMbKRogzRcU6P-XL-l8XaczTIyo_IlR-6gEh5n53xq56Ms61do6cwu5SulPuwcwgEsaZNpw0-5o3ctXsCI6s_w7GreQ6yJM7FeP6u1tZUfv1WMhx6zfZr3UFiAcsFunKloaAkFNTZiflkqmSfMDFvHmtfOXx-oGex1JQBSLkJC7QInmnt6POQGKWYyZZkr8U8F9mjlKAxOyQas8_Eq2SVRl_e4JFkbv6ITNASizLahW4d9Fi_5RhzeXjvE9_Qr1X8zUZkFtGqNAxDaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ffe99615e.mp4?token=HkRRhL6synjWzi9QQPTvK_5DBWizFKArqhq2QoJkj3lnuaQJBMWOmpPI4Kh2kXbylWErDaFPMbKRogzRcU6P-XL-l8XaczTIyo_IlR-6gEh5n53xq56Ms61do6cwu5SulPuwcwgEsaZNpw0-5o3ctXsCI6s_w7GreQ6yJM7FeP6u1tZUfv1WMhx6zfZr3UFiAcsFunKloaAkFNTZiflkqmSfMDFvHmtfOXx-oGex1JQBSLkJC7QInmnt6POQGKWYyZZkr8U8F9mjlKAxOyQas8_Eq2SVRl_e4JFkbv6ITNASizLahW4d9Fi_5RhzeXjvE9_Qr1X8zUZkFtGqNAxDaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
خبرنگار: برخی از عناصر اطلاعاتی ایالات متحده ارزیابی کرده‌اند که اسرائیل علاقه‌مند به تضعیف تفاهم‌نامه فعلی است.
🔴
روبیو: نمی‌دانم در مورد چه اطلاعاتی صحبت می‌کنید. نمی‌دانم این اطلاعات را از کجا می‌آورید.
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/66777" target="_blank">📅 20:04 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66776">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b8948b47d.mp4?token=Fhpvp5twkp16OjVjzz9BkXvV49THhu4gjfwAp2LiztvpjxHziYLAWcqy2zc9Hui8xWO7g2aqCoGozEnP_v0V_8jCOykyDY31zK-MG6vpKVyZbEWkT5_Ye7oh_5bJwDytlS_NehESxnCT4j3-fRv3sc-UlF6ueozA2LPzbGMBM2zUqEFR9zeZe4tyc8q47TMBbiK8pwyGk9TBv4pmZ9GdWmWmrAku3nQ-7s3iEZ2c7iDzJz3xKiFjcJyf7l_UNNUswkT4K4FywB4bvOOhNlb6xOif_HuR1SGBS5dyJguAPxR1f0Gy9ZIvySQfcBHXmiDH-6GNb65HYoHhfxmYglYd7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b8948b47d.mp4?token=Fhpvp5twkp16OjVjzz9BkXvV49THhu4gjfwAp2LiztvpjxHziYLAWcqy2zc9Hui8xWO7g2aqCoGozEnP_v0V_8jCOykyDY31zK-MG6vpKVyZbEWkT5_Ye7oh_5bJwDytlS_NehESxnCT4j3-fRv3sc-UlF6ueozA2LPzbGMBM2zUqEFR9zeZe4tyc8q47TMBbiK8pwyGk9TBv4pmZ9GdWmWmrAku3nQ-7s3iEZ2c7iDzJz3xKiFjcJyf7l_UNNUswkT4K4FywB4bvOOhNlb6xOif_HuR1SGBS5dyJguAPxR1f0Gy9ZIvySQfcBHXmiDH-6GNb65HYoHhfxmYglYd7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
مارکو روبیو درباره ایران:
وقتی می‌گوییم تنگه‌ها را باز کنید، منظورمان این است که تنگه‌ها را آزاد باز کنید. آنها آبراه‌های بین‌المللی هستند.
هیچ کشوری روی کره زمین از گرفتن عوارض در تنگه‌ها حمایت نمی‌کند. این اتفاق نخواهد افتاد. ترامپ این را به روشنی بیان کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/66776" target="_blank">📅 20:00 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66775">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50bf8d5d6b.mp4?token=IvJhnhvtYDUT9OvaKgMY9RQfhXydw9UOaLKlsLD9fAoC890ZTPG1euhxIncNHlsgTgIRD5cg8G4cbQ30YOnSMtGnMOx7QRuot_AwtUhw1ZPFq8cJrD00CnIoJvVV7QRGdVJKjwDBEMqxNvCJNfI-olnwlpYMAZyUKp8gio3s63mtzt7EqoLWzib4oe5aaYFeI7Rrv3JAIwwgRHYWEzlqu_AfMcnJb_S9LOvJ6mHF6PFsecfSQ1BuSYZ_uyecWrIcptkFIVhW4fWKTnQeXAfJBBc0flWgSyf4hEsnU1TzhiL_PsRTTnpSvX0YDObHUWs1rRbrdZlO8IMOK1ltpnzV0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50bf8d5d6b.mp4?token=IvJhnhvtYDUT9OvaKgMY9RQfhXydw9UOaLKlsLD9fAoC890ZTPG1euhxIncNHlsgTgIRD5cg8G4cbQ30YOnSMtGnMOx7QRuot_AwtUhw1ZPFq8cJrD00CnIoJvVV7QRGdVJKjwDBEMqxNvCJNfI-olnwlpYMAZyUKp8gio3s63mtzt7EqoLWzib4oe5aaYFeI7Rrv3JAIwwgRHYWEzlqu_AfMcnJb_S9LOvJ6mHF6PFsecfSQ1BuSYZ_uyecWrIcptkFIVhW4fWKTnQeXAfJBBc0flWgSyf4hEsnU1TzhiL_PsRTTnpSvX0YDObHUWs1rRbrdZlO8IMOK1ltpnzV0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇱
نتانیاهو:
به من گفتند: «وارد رفح نشو.»
می‌دانید چرا این را گفتند؟
چون رئیس‌جمهور ایالات متحده گفته بود ارسال سلاح را متوقف خواهد کرد.
من گفتم: «احترام زیادی برای او قائلم. او در آغاز جنگ کنار ما ایستاد. اما ما چاره‌ای نداریم. وارد رفح خواهیم شد. و اگر لازم باشد، حتی با ناخن‌هایمان هم خواهیم جنگید.»
گاهی باید بدانی چگونه حتی به رئیس‌جمهور ایالات متحده هم «نه» بگویی.
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/66775" target="_blank">📅 19:11 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66774">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf7873635e.mp4?token=HuQEikVS6sWb7iFDERBFEIMOw2V6hf74S8K4oj5V_oLZfW_zKQSeTFxnHoPn3q21gdkGtxNKKq-Fki0m3hfyy2LCpL5wuYKBXz8aZKzeL191ADS2cgGZRXCrABHoRIAqtg1X8Md17ig52klV_pQp4eiGttk0OU2lPaiSYEayksuLNM9NBdWnLv7XKWsnSLPLRJl-2r8fUmEmHLezfMO_FH0w6UPdYf7NC4-kEaNa5J5auHKPkaNl6jg-teMe46_U3vUe4Pl8eYKIwd8TP22VWxA5LTyLJg9vgobi_EsCMKb__tSNhaNlOT91cFSkp0GnuRKv4qKuy_Y1ShTi0QQg1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf7873635e.mp4?token=HuQEikVS6sWb7iFDERBFEIMOw2V6hf74S8K4oj5V_oLZfW_zKQSeTFxnHoPn3q21gdkGtxNKKq-Fki0m3hfyy2LCpL5wuYKBXz8aZKzeL191ADS2cgGZRXCrABHoRIAqtg1X8Md17ig52klV_pQp4eiGttk0OU2lPaiSYEayksuLNM9NBdWnLv7XKWsnSLPLRJl-2r8fUmEmHLezfMO_FH0w6UPdYf7NC4-kEaNa5J5auHKPkaNl6jg-teMe46_U3vUe4Pl8eYKIwd8TP22VWxA5LTyLJg9vgobi_EsCMKb__tSNhaNlOT91cFSkp0GnuRKv4qKuy_Y1ShTi0QQg1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇱
نخست وزیر نتانیاهو:
در عملیات غرش شیران بود که من به ترامپ حمله در ایران را اطلاع دادم و هیچ اجازه  گرفتنی در کار نبود.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/66774" target="_blank">📅 18:45 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66773">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1071e13e2a.mp4?token=Kq9U0oAqPR438IRjajXcS1Qplc5MoUH-sYo2zn7BRIGI1rw2egfSigxKFqYOPDGuskgPYkm9O5jF_2XbbSW-ZZwmqjf4twRh0BL37q1I7nXea7uYiJ0Ng1aqBK4TE_7vE_VW6cHo8TfT9dV-HnCO-tg66TPGTtVas6EesGq5XCByaVgGDXukAO9wxDz5lfnBLp-ZjCudmmpiQ4jn5E9JyTdRZH3s-OWU1mbrt7rodC6FFLhZWgoPttcVGcJKFcH21IVsk-zVXCEQuMaOVhEbOT7bK1mJKeIWIAZYuxBGEk5rFwEuUR_PgDMPfOor9bIIiKZs5s5acnDLh3UFq_h-FA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1071e13e2a.mp4?token=Kq9U0oAqPR438IRjajXcS1Qplc5MoUH-sYo2zn7BRIGI1rw2egfSigxKFqYOPDGuskgPYkm9O5jF_2XbbSW-ZZwmqjf4twRh0BL37q1I7nXea7uYiJ0Ng1aqBK4TE_7vE_VW6cHo8TfT9dV-HnCO-tg66TPGTtVas6EesGq5XCByaVgGDXukAO9wxDz5lfnBLp-ZjCudmmpiQ4jn5E9JyTdRZH3s-OWU1mbrt7rodC6FFLhZWgoPttcVGcJKFcH21IVsk-zVXCEQuMaOVhEbOT7bK1mJKeIWIAZYuxBGEk5rFwEuUR_PgDMPfOor9bIIiKZs5s5acnDLh3UFq_h-FA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مارکو روبیو در کویت
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/66773" target="_blank">📅 18:43 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66772">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/66772" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/66772" target="_blank">📅 18:43 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66771">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17bdf5f245.mp4?token=K7J9G2NXtIrV_AKi1nzKDJ-VYfbt3bXB1riCkTH-5IKbYeFrpdli71CD_Nq4sjecwZ_DOS8hvzhwkxDI2f5Z1HaJ5BIvFnsMFkR3fF0aUTUM-qu9UxnFR1IfaGmaaGjOdlADjSUZx2DuHyTWw-8N-CDkhTpuiQkvzaoz_hiHDbW4jp1o2cfkFTW6ct4fsC6mfOV4QE75bnCHFIqO3e88YWpkpNsOyL-50VOZnteyIftHH68CODoYOSFTosoOrFR2b4IBi1kvK629_Rkw8EEsXrYFqHNy1GzO0s2DF6dDBWegNh_E_zIm6Qa1PtcISWrw_q6V_RJowhaG8CZPGnqphE_SfdDEYVMbMxg9-L3suXTpuBGp1T0Gshhv0UYdHBEkrHyS4OvPLkRoGc7ozQ1T-ZqcmieTQTLyF1tl2QaboRbevbTJomWdhe8-a7FEVZ9pB_1cMvBVlXjBeNmU9pq2lKvKWGFZa1o12Mg31uBGJhieDZuAMvC3jD8Ik1z-RU78IOoYWXJSkuIGwP6dX11yMsHVytgbYbtf0uAvY72-OtprzD_NAJwfa3SU1fGtGoaQsXKg4qRaRCL-_1em66F0Eb4PGGNC5DcIeGvxHjUQSqgQpht1YGgPcfK8mDj0C8oSVxHVcwsnOAeDFVvJdogE6vBMALjt3rbFf9eiJrJfUtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17bdf5f245.mp4?token=K7J9G2NXtIrV_AKi1nzKDJ-VYfbt3bXB1riCkTH-5IKbYeFrpdli71CD_Nq4sjecwZ_DOS8hvzhwkxDI2f5Z1HaJ5BIvFnsMFkR3fF0aUTUM-qu9UxnFR1IfaGmaaGjOdlADjSUZx2DuHyTWw-8N-CDkhTpuiQkvzaoz_hiHDbW4jp1o2cfkFTW6ct4fsC6mfOV4QE75bnCHFIqO3e88YWpkpNsOyL-50VOZnteyIftHH68CODoYOSFTosoOrFR2b4IBi1kvK629_Rkw8EEsXrYFqHNy1GzO0s2DF6dDBWegNh_E_zIm6Qa1PtcISWrw_q6V_RJowhaG8CZPGnqphE_SfdDEYVMbMxg9-L3suXTpuBGp1T0Gshhv0UYdHBEkrHyS4OvPLkRoGc7ozQ1T-ZqcmieTQTLyF1tl2QaboRbevbTJomWdhe8-a7FEVZ9pB_1cMvBVlXjBeNmU9pq2lKvKWGFZa1o12Mg31uBGJhieDZuAMvC3jD8Ik1z-RU78IOoYWXJSkuIGwP6dX11yMsHVytgbYbtf0uAvY72-OtprzD_NAJwfa3SU1fGtGoaQsXKg4qRaRCL-_1em66F0Eb4PGGNC5DcIeGvxHjUQSqgQpht1YGgPcfK8mDj0C8oSVxHVcwsnOAeDFVvJdogE6vBMALjt3rbFf9eiJrJfUtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/66771" target="_blank">📅 18:43 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66770">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bk4mhKTWtBu-ZwXBltQyMNBHksuu7tsjP7UARQQ3_1amd69nah2_9ksqbnow5GE2-vBtu8qFD3xAwpmAL9mup1rYZ1cm4n_PJ335e-q_brX3MX9pE35XnH-UB7yDn_3JY5iZ7Qs-NYRR5c59uylj0cNGHwL8890MYL6jAN9HOxN_BAzJGDuRwu_1we7VvgqiTwD_0sJLy5XlInLFkkOwpJxlDbX_rAux8ig8xfoussN397LQG31lTxrugqSPS1fYR6ZIxWsrdx3Y0IN11QIK1zZ5nQ1ecIl5W5awixlEdCIfaIb-ZbvIlKlF77UbU6oiDqCv6wjQJ4s_zjJr7_EICQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
پرزیدنت
ترامپ:
ایران به آمریکا اطلاع داده که، برخلاف گزارش‌های دردسرساز رسانه‌های فیک‌نیوز، «هیچ عوارضی، هیچ هزینه بیمه‌ای و هیچ نوع هزینه دیگری از هیچ کشتی‌ای که از تنگه هرمز عبور می‌کند، توسط ایران درخواست یا دریافت نمی‌شود. اگر این خبر نادرست باشد، مذاکرات فوراً پایان پیدا می‌کند!
همچنین، آمریکا هیچ پولی به ایران نداده و هیچ بخشی از پول‌های ایران را هم آزاد نکرده است. ما بخشی از پول‌های ایران را که کاملاً تحت کنترل خودمان است، برای حمایت از کشاورزان و دامداران آمریکایی آزاد خواهیم کرد تا با آن ذرت، گندم، سویا و محصولات دیگر خریداری شود. ایران به‌شدت به مواد غذایی نیاز دارد و ما این مواد را منحصراً از آمریکا برای آن‌ها خریداری خواهیم کرد.
از توجه شما به این موضوع متشکرم!
— دونالد جی. ترامپ
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/66770" target="_blank">📅 17:52 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66769">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6cc755f3dc.mp4?token=ddpjPXVmdDGeqldX3KZ-zRu85wTT_a6-sQAxiVsy-hkY0qBJdgdw7gaurhU4FqOuGuNKqTh0KUu_RpL384DZndAr4ug_pWfz3U_7WUdS18G4JcL0oMBWQ_YI3LMihwp8ixPEYWXrTE1kqKkq12CuPlhIh1_qWCmZcWtfPx0GLaeG2-ugVCX7rUKnheQl9yznoz8Sej68vf5zTH-_d0ct9tdYfiLNZWu0NmFgjkxREj08Td3Qjnao03SlH431oP5ZxdHOeSX_JGxkCnTPvPEAjBiE0N5iMapgHXIpxqqQRJvc3jNgYDMYaho1T2YH6IsFyE71Me7EXetX7wU4X_MVMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6cc755f3dc.mp4?token=ddpjPXVmdDGeqldX3KZ-zRu85wTT_a6-sQAxiVsy-hkY0qBJdgdw7gaurhU4FqOuGuNKqTh0KUu_RpL384DZndAr4ug_pWfz3U_7WUdS18G4JcL0oMBWQ_YI3LMihwp8ixPEYWXrTE1kqKkq12CuPlhIh1_qWCmZcWtfPx0GLaeG2-ugVCX7rUKnheQl9yznoz8Sej68vf5zTH-_d0ct9tdYfiLNZWu0NmFgjkxREj08Td3Qjnao03SlH431oP5ZxdHOeSX_JGxkCnTPvPEAjBiE0N5iMapgHXIpxqqQRJvc3jNgYDMYaho1T2YH6IsFyE71Me7EXetX7wU4X_MVMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اگه
فکر می‌کنید قراره چیزی کسشر تر از این امروز ببینید عرض کنم که سخت در اشتباهید. فقط کافیه موزیک ویدئو شاهکار صداوسیما برای تیم امیر قلعه‌نویی رو ببینید تا بفهمید با کیا شدم ۹۰ میلیون
😐
😐
😐
😐
علی بیرو تو دروازه یا نیازمند ، کنارش شجاع و کنعانی میشن پدافند
تنگه هرمز ما تو دستای سعیده
شوت‌های قدوس و رامین مثل خیبرشکن، مستقیم به قلب دروازه‌ی دشمن میرن
ترابی دریبل‌زنه، نعمتی هم حامیشه، مثل هایپرسونیک از لای دفاع رد میشه
یه طرف میلاد و ازون طرف جهانبخش، پهباد شاهد رو روی دروازه میکنن پخش
حاج صفی ، حردانی و یوسفی مثل شیرن
توپ‌های علی علیپور از پاتریوت هم در میرن...
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/66769" target="_blank">📅 17:43 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66768">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f90bbfd79.mp4?token=d3ftpDJJ-cLsrkba6kNlw7OFtyAXBbT-CCmKuVPtfGZ9BRvbexHK6tscdNt63YM6JAuxX54rPN1zJVzUYqkH0e3bHWnn3QH3X4f9eSZj9nwCU8M1_5yO86fzG60zSQTeeVrniiW5BqdDXF3xl4jQiVLWCI3uFZOhTQXEv5Jw_ANGVhaoHnDq6pqLB4BTbutBEUu5e1YLzXaCe1tiomSivYsMN9chkgMYODMa4Z5wfpZECEaHsh83Bz1t8DiqLLC623NpatQhW0S5nfXJZ97ZU9HeRd0OqRR4BlCwX1XCIWmiPj0EmpL3GmRm8Z13e0qN0tkNoGlhQZrcd0Ow1hYzbnEUWsCTbCzFAWmEFtaroK7NcPGpbjH_cOQRDXNZoiCIuvTQuGLPgc4OwZ9W3XIQc_7aenUARgF44z9omQiwjYv90-VDifO660qfnHqK5mz0XE8O8sDoMK456V5f8qufhZGYSRpJQFarWnQNliHwsMPuWEHt72VppE_eEDYCFPel68jjUtIYPgWF0kHO_jY48ZxA3rka3Yg-zX85r3XJG7AGrbk7vvZSizswyLYxj-kaMFN0jIrzxnAV1-_s2eHCZRzz676RUrkX333-TqIvt__zgsZVydhczrfK-Vqb0lwmuYCI4GZ_KxcjrLlos3Fx8zQqniFGmhF7vcHD_FumJXc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f90bbfd79.mp4?token=d3ftpDJJ-cLsrkba6kNlw7OFtyAXBbT-CCmKuVPtfGZ9BRvbexHK6tscdNt63YM6JAuxX54rPN1zJVzUYqkH0e3bHWnn3QH3X4f9eSZj9nwCU8M1_5yO86fzG60zSQTeeVrniiW5BqdDXF3xl4jQiVLWCI3uFZOhTQXEv5Jw_ANGVhaoHnDq6pqLB4BTbutBEUu5e1YLzXaCe1tiomSivYsMN9chkgMYODMa4Z5wfpZECEaHsh83Bz1t8DiqLLC623NpatQhW0S5nfXJZ97ZU9HeRd0OqRR4BlCwX1XCIWmiPj0EmpL3GmRm8Z13e0qN0tkNoGlhQZrcd0Ow1hYzbnEUWsCTbCzFAWmEFtaroK7NcPGpbjH_cOQRDXNZoiCIuvTQuGLPgc4OwZ9W3XIQc_7aenUARgF44z9omQiwjYv90-VDifO660qfnHqK5mz0XE8O8sDoMK456V5f8qufhZGYSRpJQFarWnQNliHwsMPuWEHt72VppE_eEDYCFPel68jjUtIYPgWF0kHO_jY48ZxA3rka3Yg-zX85r3XJG7AGrbk7vvZSizswyLYxj-kaMFN0jIrzxnAV1-_s2eHCZRzz676RUrkX333-TqIvt__zgsZVydhczrfK-Vqb0lwmuYCI4GZ_KxcjrLlos3Fx8zQqniFGmhF7vcHD_FumJXc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
‼️
⚠️
پشمام اینو داشته باشید. تو عراق از معاون وزیر نفت سابق این کشور حدود ۸۵ میلیون دلار اسکناس نقد از زیر زمین کشف کردن که دفن شده بوده!! فساد سیستماتیک تو کشورهای اسلامی ماشالا خوب رونق داره
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/66768" target="_blank">📅 17:14 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66765">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c68737622.mp4?token=QKfaHOdLa_PkS3n-RlMpR5QZ0qGSU_-5iyLkCa7JDW-ayoH76VRscC0AQheF45FNx_pWtVSsWfxWDl67Crqvs4Rhd8KbX4OTW4xSmG7ZfwCc8XE_veqIDnHRcpJANzGx1fr1vVxmsvc6p5GJV3GMkTG1MW1ccpIEK8tnBp5DBwUE9zdzhpmK1_7cYanigktjoueBbCJH8hgeSGgbzBA5fDmWcR_8vW3dO4QLElwqWg4EZrF763edlRLxvXtWYfwwDrtMCH4QJ-2_N2Foi_-UX7bWu4rMsxSvba6jfNFhlokGcszBbaMfrqBD5s1V4Km_VJUNaoLrVpMDx13yBHivDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c68737622.mp4?token=QKfaHOdLa_PkS3n-RlMpR5QZ0qGSU_-5iyLkCa7JDW-ayoH76VRscC0AQheF45FNx_pWtVSsWfxWDl67Crqvs4Rhd8KbX4OTW4xSmG7ZfwCc8XE_veqIDnHRcpJANzGx1fr1vVxmsvc6p5GJV3GMkTG1MW1ccpIEK8tnBp5DBwUE9zdzhpmK1_7cYanigktjoueBbCJH8hgeSGgbzBA5fDmWcR_8vW3dO4QLElwqWg4EZrF763edlRLxvXtWYfwwDrtMCH4QJ-2_N2Foi_-UX7bWu4rMsxSvba6jfNFhlokGcszBbaMfrqBD5s1V4Km_VJUNaoLrVpMDx13yBHivDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
‼️
⚠️
ویدیوهایی که خیلی از دیروز  وایرال شده از کربلا؛
دیروز کاروان شیعه اسماعیلیه که تا امام ششم امام صادق رو قبول دارن، واسه زیارت به کربلا رفته بودن.
از اون طرف کاروان ایرانی ها هرجا اینارو میدیدن واکنش نشون میدادن..
تو یسری جاها هم نزدیک بود دعوا فیزیکی بشه که پلیسِ عراق اجازه نداد...
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/66765" target="_blank">📅 16:47 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66764">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbff1343a7.mp4?token=SoJwIsgCYoSh1kAo5vys6UQuSezXJrYktQBKQXb8VIrNOdeSdH2zDiPW_B75la5bqsOinbIo1x1JNOW6zMZ8KksmZ-5v1CgwAo7MmiJOivA0T2HG4eFOHqYtDCQUCgTIWAWsSzWDaEl6CgZKOxNHA-nNFBSYuxKnulWYppLyRquc0eqrST0yZVYgJuhUQBcMzU_NfwQmJluu3yxuEUjgI7R3OwIoUsTZs7w5neR2W9gUj4qfnV4G4gjfTqBFE-fa0GOGw7iHL0UQYNSaeLrFHm_6ZrWqFih6jf4Z3aj8khIpk9Qdx90Io1hDqu5UZRaSlkaf7NT6Hwblh745_Vlsdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbff1343a7.mp4?token=SoJwIsgCYoSh1kAo5vys6UQuSezXJrYktQBKQXb8VIrNOdeSdH2zDiPW_B75la5bqsOinbIo1x1JNOW6zMZ8KksmZ-5v1CgwAo7MmiJOivA0T2HG4eFOHqYtDCQUCgTIWAWsSzWDaEl6CgZKOxNHA-nNFBSYuxKnulWYppLyRquc0eqrST0yZVYgJuhUQBcMzU_NfwQmJluu3yxuEUjgI7R3OwIoUsTZs7w5neR2W9gUj4qfnV4G4gjfTqBFE-fa0GOGw7iHL0UQYNSaeLrFHm_6ZrWqFih6jf4Z3aj8khIpk9Qdx90Io1hDqu5UZRaSlkaf7NT6Hwblh745_Vlsdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مترجم: «ما هرگز در مورد توانایی‌ها و تجهیزات هسته‌ای خودمون توافق نمی‌کنیم.»
پزشکیان: نه!! موشکی! موشکی را گفتم…!
مترجم: ببخشید موشکی.
😂
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/66764" target="_blank">📅 16:25 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66763">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn5.telesco.pe/file/d59ef82aac.mp4?token=eBmoVrOsAINUSoCre7FF7DK7sLzl4bjY-6D_ZSLrAEZlsMjjO7PiXDdjtKzuM6_h2mjzHK8NjhwkPnPDMSGpB-GHjhLTVjtKLsSpIjKd_GGd-uSZOZ9ii7SuxaYj4ffo__hPU6_bNCJbeGi1DqW14aFUjX6Xius6rKrUUxggfeBNMR6Zs72Yk8lD2VmgQI4DsrxChb9_bBAbzWUm4YKhSiNyHii99zJQdVj5B4tl6OKrgVA_klgu59vgdDTuuY5Lutz8gmCOBi-T4acJijW5VwXTwJ92a-m1UCBrNN6TwjrvanI8dyiCIwhuPf4WFLTIyCziT9dmKTwld8sHVqk1Og" type="video/mp4">
</video>
<br>
<a href="https://cdn5.telesco.pe/file/d59ef82aac.mp4?token=eBmoVrOsAINUSoCre7FF7DK7sLzl4bjY-6D_ZSLrAEZlsMjjO7PiXDdjtKzuM6_h2mjzHK8NjhwkPnPDMSGpB-GHjhLTVjtKLsSpIjKd_GGd-uSZOZ9ii7SuxaYj4ffo__hPU6_bNCJbeGi1DqW14aFUjX6Xius6rKrUUxggfeBNMR6Zs72Yk8lD2VmgQI4DsrxChb9_bBAbzWUm4YKhSiNyHii99zJQdVj5B4tl6OKrgVA_klgu59vgdDTuuY5Lutz8gmCOBi-T4acJijW5VwXTwJ92a-m1UCBrNN6TwjrvanI8dyiCIwhuPf4WFLTIyCziT9dmKTwld8sHVqk1Og" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
مراد ویسی: با توجه به تضمین آمریکا، که گفته در جریان مذاکرات ۶۰ روزه مقامات رو ترور نمیکنیم، احتمالا تا ده روز آینده از مجتبی رونمایی بشه.
مجتبی قراره احتمال زیاد تو مراسم تشییع باباش شرکت کنه. اگرم پیداش نشد، یه جای کار میلنگه و مجتبی حالا حالاها پیداش نمیشه.
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/66763" target="_blank">📅 15:55 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66762">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e65be3ab63.mp4?token=YwK17XMx7fjTR5Xa0b0r8QYxm4odnNaxhooG6JzFcamVQklSnHpdAuoy9HKuhKrwTc2xuxyPHTGca9xJckIbv1fgkvTkO8P8F1jLCtIF0sXASdMmRivCmu9lmFkU-8X0UshLvyl9N_tTQvS7Q5Wlw24a0KYg2EqesPwubL7At-4pwk1AYNZ0aGjwdev8bM9Hs9FxNLU2c8BIM5L28JcGcebLiIwUFg9BzcQoYFUWQpiRO3SymWSVqVD5MKgGp15heNN_2Y7J-gUPaJo_acCM-m2f4MBP2UANRiJniFx6_oNtSUYJten6y-XGpCh5QqDZRUx29kuZOPqo4BTul3UA9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e65be3ab63.mp4?token=YwK17XMx7fjTR5Xa0b0r8QYxm4odnNaxhooG6JzFcamVQklSnHpdAuoy9HKuhKrwTc2xuxyPHTGca9xJckIbv1fgkvTkO8P8F1jLCtIF0sXASdMmRivCmu9lmFkU-8X0UshLvyl9N_tTQvS7Q5Wlw24a0KYg2EqesPwubL7At-4pwk1AYNZ0aGjwdev8bM9Hs9FxNLU2c8BIM5L28JcGcebLiIwUFg9BzcQoYFUWQpiRO3SymWSVqVD5MKgGp15heNN_2Y7J-gUPaJo_acCM-m2f4MBP2UANRiJniFx6_oNtSUYJten6y-XGpCh5QqDZRUx29kuZOPqo4BTul3UA9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
مجری شبکه دو:
کاش قبل از جلسه تفاهم نامه یه سر گلزار شهدای میناب میرفتید.
اگه محصول آمریکایی کیفیتش خوب باشه میخریم یعنی چی؟! یه کم بهتون بربخوره
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/66762" target="_blank">📅 15:33 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66761">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s1DPcbyQ5hrNXMcKtIpHuR1j7_hU21u8AFQLphMzLUN8ZI4Wvc5ZfoHCr3j7wNtq0jyivlhEh2SewacdpVmF1xYGse4zp4ivGFd5TW3dlzALwlB92lIg2W4nOSTsgKg-rdd8gJdoFet4RUy7INRt7FsDLywIR8pYFuKolLQDlXZc1CiK5CNrlttGx9cbXj2KfYGEv0jHdrUQrjXUYK1MSAs_Vo2su87ZK1NbDIxUAKoPq5CXdGVhOFwsHyDz5FH-JZXGTb-FiUvpGyfEAOAtLfeViLztKQYfy-0IcDvv5OsHpxwSxcmsrk7zfSjfZcJGTpg-hNSS4CSGkq7RQq5rkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خاله دنیا جهانبخت پاشده رفته کربلا عرض ارادت به امام سوم شیعیان
😐
😐
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/66761" target="_blank">📅 14:35 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66760">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eoQW1JYVI9DokD5UdwEcYCN9ch0xeQisB1FMDc8URUOVZchd6ymhdmYegZf68lboZzObGjNj2u3dPjGPY3oFUOSo7Etfo5_zAaWdWO3_70j7C_xdKGYu_DoETFJyj6HMqG4A_6QLWqTSSbpqdGf3i5EFO18YdOkIHtxSv6SQ4lBsYlz5wt1v_DP5OWclIQ3Z1ZtKRsngHWMR25BoDrrqZIr4kUwrSIxbOBLahawFhhJool-4sP7JjGJ-dxqYWKcOzgB6WgF15vcrZI3nnJb1XABUfoDEd2vb7ATuKh_l8ubnZ6UPk8BHGr-BVesvRiPw7Dg8XFpTcWq0aXo5La0KMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مرندی:
ایران در آینده‌ی قابل پیش‌بینی به آژانس بین‌المللی انرژی اتمی اجازه‌ی دسترسی به سایت‌های هسته‌ای مورد نظر خود را نخواهد داد. چنین بازدیدهایی مشروط به پیشرفت قابل توجه در مذاکرات است. تبلیغات و تاکتیک‌های فشار بر محاسبات ایران تأثیری نخواهد گذاشت.
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/66760" target="_blank">📅 14:32 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66759">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f6644dcda.mp4?token=MbB4uhXqrINORXXwkzHWpWHcr8f7wbL4XkeY49r6epGNPi8fMAryi6N2daH5UvOH8ZT84YNVtSXp_ad-YpCRGBqjRHW1XNqtOGTaBjpV1bg_FMoLXrSj4VrGayFjDhrsO-S-GGHU3_8mMoLQlC8iIAf-7IqsGWuM-2Q4NqIxOuQPbWjGprctVyCodsOipZDNfdawQnZvQe0oIGZBqglU1FsRgqMBSoOvxLiViHPtzAfZYfhregWaChY1O8KGGKHjK-FC96WlmSRTCTtpG5UHJaRF9H6EUan0W74eCYSEFqz2X7pmHymmsK1pQ4YMeSK1jOFmZOFC9saiZ_pkdAowvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f6644dcda.mp4?token=MbB4uhXqrINORXXwkzHWpWHcr8f7wbL4XkeY49r6epGNPi8fMAryi6N2daH5UvOH8ZT84YNVtSXp_ad-YpCRGBqjRHW1XNqtOGTaBjpV1bg_FMoLXrSj4VrGayFjDhrsO-S-GGHU3_8mMoLQlC8iIAf-7IqsGWuM-2Q4NqIxOuQPbWjGprctVyCodsOipZDNfdawQnZvQe0oIGZBqglU1FsRgqMBSoOvxLiViHPtzAfZYfhregWaChY1O8KGGKHjK-FC96WlmSRTCTtpG5UHJaRF9H6EUan0W74eCYSEFqz2X7pmHymmsK1pQ4YMeSK1jOFmZOFC9saiZ_pkdAowvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قالیباف:
یادداشت تفاهم اسلام آباد به اعلام شکست آمریکا تبدیل شد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/66759" target="_blank">📅 14:08 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66758">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IWr0StUc1wgSgCcmv_IwsmN-5QFhpxujn2AIS_Uz5WXIvh0gJycaPI4WetCHVP22IkvRMIZA-V8B0vNZjQMEJDj-lpRWrAg_3LAmzmEjsZQF7-IMFgBwBFzK0Pi_cL1j-ypPAwliaq1eXtBripm3lF2k1gSDhha41tjgu1m5ud6OgbWU4ykCq76Q6CINNxYboi6Mctdzk1wj0l8eF21mgopVc66GOzhaAY6_l2k6kANb84mg6DpUdO3KrICbyqy58HDaEXNROJmkC2vy2JnGY9cgBYmSMiR-6tER-JLBT2txFmgozCsVwhiDLs4YWh3HV4jeXYl2sgSjr1__MushPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
قیمت فست فود برای دو نفر، قیمت سال ۹۶ !
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/66758" target="_blank">📅 13:28 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66757">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/768fbbdd1e.mp4?token=qku55otBxAaV0OS4C6eXr8gz2X-n6ZGAHW-P5HJ-B_D3AYI3DrWmeHqysWdpW6tTBn4lVALX2yHPm9gxvOu4Dd-qSrIm-2CfrYpuoPC5o3xoMtdYLXq9qa9tMcUDPTA0dlTJfX8TThdo10bSJ91ZtRDjNeKqi7J_zpCeHYqKM6o77p1xLZw54po4DEy5gFQOJ2XSbwqKJWxuNSdtL1rwNkKS78IwRwm8D-1xTUh3CC5T-Nreugypn2W3ZjwsJsgWIEa-mo5eQdZVxxfoiid-EW2u4zmwa5BNDH30eFthj-qvkPDOQ6Touf1a7NSCMV_sAxZOC_T2gYphC2Jjcg4r6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/768fbbdd1e.mp4?token=qku55otBxAaV0OS4C6eXr8gz2X-n6ZGAHW-P5HJ-B_D3AYI3DrWmeHqysWdpW6tTBn4lVALX2yHPm9gxvOu4Dd-qSrIm-2CfrYpuoPC5o3xoMtdYLXq9qa9tMcUDPTA0dlTJfX8TThdo10bSJ91ZtRDjNeKqi7J_zpCeHYqKM6o77p1xLZw54po4DEy5gFQOJ2XSbwqKJWxuNSdtL1rwNkKS78IwRwm8D-1xTUh3CC5T-Nreugypn2W3ZjwsJsgWIEa-mo5eQdZVxxfoiid-EW2u4zmwa5BNDH30eFthj-qvkPDOQ6Touf1a7NSCMV_sAxZOC_T2gYphC2Jjcg4r6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🤯
بلندترین پل جهان که به یک آبشار عظیم تبدیل شده است؛ شاهکار تازه مهندسی چین
تصور کنید روی پلی ایستاده باشید که صدها متر بالاتر از کف دره قرار دارد و در کنار آن، دیواری عظیم از آب از دل کوه به پایین سرازیر می‌شود. این دقیقاً تصویری است که این روزها از پل «هوآجیانگ» در چین توجه کاربران شبکه‌های اجتماعی را به خود جلب کرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/66757" target="_blank">📅 12:31 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66756">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76a52e8497.mp4?token=deA9ekKZMSVCat2_BkfedhC50Rei4WefOHhd0DimBq8quqHfxgRS1f3PwoBeJHt4HSjytq2dvUWx01jXzDPi_0vE7KKXMeyBoHCxfYH2tGEtt417IOURCtFo0Rdv4p5yMz8B345CBom9PjgL-IKwxBZnRCDs7bY6K97KLj2SXak_e3KiubQ3XhIEXWu3lrOOxmf96Ii9ZrPsutm83UuZA8PDCJ72m3b63ZgdhJ218FZyWaHa2llQzo_Qf-uPbDThPNUH8EGWSQVTU8P46JwrdcCd0jSSGWKLyhp5poq9PtDg9K42NiWVWXBi-uT6lHIM1iInCWePqYDqj3J54fvUjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76a52e8497.mp4?token=deA9ekKZMSVCat2_BkfedhC50Rei4WefOHhd0DimBq8quqHfxgRS1f3PwoBeJHt4HSjytq2dvUWx01jXzDPi_0vE7KKXMeyBoHCxfYH2tGEtt417IOURCtFo0Rdv4p5yMz8B345CBom9PjgL-IKwxBZnRCDs7bY6K97KLj2SXak_e3KiubQ3XhIEXWu3lrOOxmf96Ii9ZrPsutm83UuZA8PDCJ72m3b63ZgdhJ218FZyWaHa2llQzo_Qf-uPbDThPNUH8EGWSQVTU8P46JwrdcCd0jSSGWKLyhp5poq9PtDg9K42NiWVWXBi-uT6lHIM1iInCWePqYDqj3J54fvUjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
یه سرباز روسی که با پهپاد اوکراینی روبه‌رو شده بود، از اپراتور درخواست کرد که اول دوست کنارش رو بزنه تا بتونه سیگارشو قبل مرگ تموم کنه
اپراتور پهپاد درخواستش رو قبول میکنه، اول سرباز دیگه رو میزنه و بعد سربازی که درخواست کرده بود رو میزنه.
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/66756" target="_blank">📅 12:04 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66755">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd2607379b.mp4?token=Pz13Tapk2ikJvQBDFRUR4Lqj2YAiioYA-AJKEplPX6D0BgFnZZoZ60OOkGxKSTxNKa38B5nqQkHUJb0I7aQSz5UCFbavFpCiogwn9JzMm5qu032bNaCDVSY37Pyyd-Ma-Ha-RSczfvOBv7q59KKuXJ54ULimtZMJjHftGu3TmMqrAJgPwvqqAyn9vr3IvfuYUJ03R7Iy3tlW3Pdp_0Bq4NwPJJb-Mr7rgYJsQCocG2hcT6s44AV15JKvUVGGujgSPe45r5K7MhHUxKpdIZ9naF3AcfyN42pX0NaVrRk_O2KJOrNWaWhmLaga4KYPOzQNjgMuaDfA38q-q10MhFKflQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd2607379b.mp4?token=Pz13Tapk2ikJvQBDFRUR4Lqj2YAiioYA-AJKEplPX6D0BgFnZZoZ60OOkGxKSTxNKa38B5nqQkHUJb0I7aQSz5UCFbavFpCiogwn9JzMm5qu032bNaCDVSY37Pyyd-Ma-Ha-RSczfvOBv7q59KKuXJ54ULimtZMJjHftGu3TmMqrAJgPwvqqAyn9vr3IvfuYUJ03R7Iy3tlW3Pdp_0Bq4NwPJJb-Mr7rgYJsQCocG2hcT6s44AV15JKvUVGGujgSPe45r5K7MhHUxKpdIZ9naF3AcfyN42pX0NaVrRk_O2KJOrNWaWhmLaga4KYPOzQNjgMuaDfA38q-q10MhFKflQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
😐
دیروز تو دولت اسلامی عراق یه مسئول دولتی حوصلش سر میره و اینجوری با منشی‌ش کارای ناخوشایند اسلام از جمله
لب گرفتن و ساک‌زدن
رو انجام میدن. میگن که این یارو اخراج و بازداشت شده
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/66755" target="_blank">📅 11:35 · 03 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
