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
<img src="https://cdn4.telesco.pe/file/Mc9KBt3uUFjBj7OblSlHJSBVtcsquzDO8NIehmIP4XNSfYSW74sB4OQQ9vFFm7d39C1oaeixtLiUBpH7mxBNk704wbzbZNje2ajnO_xekYLdCA2G2qwcb2pgw8gQ9NNkeD1tQwE-9CZLnHzu18qeogCzc8C9TyFbMrbxsBBR83RtrJtDxDCxZwtgPkTVJR-PUB05B3Yh26FlwqVMMMqfOuzESJ_cfmJVqQDJbxZ4gtYbpkOjPCI-Zpz2PJvigT9mXPLO8VtJm_Dv6xy2oWP7e36OJ_Mg1UN5WFE0PX0TosUYLqRQLeiHJ_d5H1MM_RAVpsysoM1wvh0g7phFiegx7g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 205K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-14 15:39:41</div>
<hr>

<div class="tg-post" id="msg-67332">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PrSdbI3MRsl2wWIugJq0dRVlAXQW8fAYiacjo_jnWO6_FucEzIjs8MkV8551FR_d4Hd3OkESIoQbbKKLjn419RDZ9SuICgqOqKG4MGorkjaSR8Dsruh4cyQVO_PBhj7wO8QSvCQ92QwD3PqMl8ZjF5je40z5XzbIYunAWrfEQTmGDGO2wGfa5dS9tfOHQLeTlRMtpumS64yMM0QiVUs9w4dGmspgFHBIdIHkQFYLN31uoVSU_FszKWqe6ROh6hYTaaPN3AFrm5U37Eult-N5zNfhOkYnwE1lGSZyWhez4Pw5ziLQC0e9wphdPCOmCSn95D9o3onSODCAp4TpLrtYpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
محمد اکرمی‌نیا سخنگوی ارتش:
«هرگونه اشتباهی از سوی دشمن، با پاسخ قاطع نیروهای مسلح ایران مواجه خواهد شد. ما بارها اعلام کرده‌ایم که از فرصت آتش‌بس برای ارتقای توانمندی‌های رزمی خود بهره می‌بریم. ما حتی یک لحظه را هم هدر نمی‌دهیم و تمرکز خود را از این مأموریت برنمی‌داریم.»
@News_Hut</div>
<div class="tg-footer">👁️ 1.85K · <a href="https://t.me/news_hut/67332" target="_blank">📅 15:33 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67331">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🚨
🇮🇱
نتانیاهو در جلسه دولت:
شنیدم در رسانه‌ها گفته شده که رئیس‌جمهور ترامپ خواسته علیه تونل‌های تروریستی در لبنان اقدامی انجام نشود. این یک افسانه و خبر جعلی است.
او حتی یک کلمه هم در این باره به من نگفت و من هم از او چیزی نپرسیدم. ما بر اساس ملاحظات و تصمیمات خودمان عمل می‌کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 5.8K · <a href="https://t.me/news_hut/67331" target="_blank">📅 15:08 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67330">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rgj0lbBM6XPEAKI75v5spsMaQIKN7JrXbzbrrSuDavPKpWCaaVZ_z8Z6l1KP_u0cpwZz6ETcTxBPIzMF3lcOi_7_IrhSrx7yH7VAJFVdSHVGvmfHsLoOs8tB8d3kpHUk1_W6SBUn5a_w2ScfN-QK4dKqMvr3N6KDsFqTLlTcVsxeQ3ewCx5hyVehKeyn4OHmGjhkUxYgT2_0cPu1_j0Y5txLLRk3pwzKiOG5j7N3WNptbhziuxIu0R70s4TivpuzCs3hKOsOOr5HGYp-YjPDWDC67vsLPvjtqzYoV2MXTnPmodBiBjEpAeuuMDLvcGb7nMtu1esq_y8kwiqvkZn7tQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تصویر ترامپ در مراسم وداع با جنازه علی خامنه‌ای که روش نوشته شده:
خواهیم دید چه می شود
@News_Hut</div>
<div class="tg-footer">👁️ 8.75K · <a href="https://t.me/news_hut/67330" target="_blank">📅 14:43 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67329">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xm3wpwJ5qVzehFZpCrX61LV87mMqTgWMiN6NFVDshzyEfedzYp__FxZsKIvCUIceTn8mquCih7uqOq5qKP1vCYoGEu5EkR4w8SHKDc-PbPF5TPy-UeZ-vWHAs1fxOGLuusegCaP2sxdxmpCdZZoUuqHCW8hbbXppv0zQQxQ44weoGkZHRETjSJDq13MUb5UdmsVusra_JwGO4NDp5bORBbi8AIn6U2FbDmPTvNmSVAsWU3o7gXIEpzBs_ohEkHYGUavrehI4qOTZyRnm0_COYI6KAXlrpBQvvh8bL9pqVTs_QS_o5CUPPbt3sH_bcVImKBfImlpP2l1nmUWrtqkV8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اسرائیل به فارسی:
بهرام که گور میگرفتی همه عمر
دیدی که چگونه گور بهرام گرفت
@News_Hut</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/news_hut/67329" target="_blank">📅 14:09 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67328">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b8ead8806.mp4?token=kdzTbY9D2BdJPZObPGwo_Zl6To6pCxvAx0M2QizX7SPFDO0qBB2-lMirO6kUScLDnmzD-Jn4BfAdGBNeUkSByp8ebSSjiitFxS1COfVRapepxwZzP8aW01Xdb5wt58KmdXrUdnV1TQrEj1bhOuwpzZcTwoL0LlZ-7fgFDKmG3sv78Lsid-xyXM9nrsgrghyeKPDGZqPfAk43ufKzTgqgETkSFCku0OGm7g5OJHKULsllXz1bHyTYNC29_ra6e9nVDRvLMHzKGsLcgXLFOy4E42Ljt8bbX1OsHYXxvcUsPtF73GLU4s7v_fwO2gtIzo4Oxki1A4G2JfbfAD5xvaxk3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b8ead8806.mp4?token=kdzTbY9D2BdJPZObPGwo_Zl6To6pCxvAx0M2QizX7SPFDO0qBB2-lMirO6kUScLDnmzD-Jn4BfAdGBNeUkSByp8ebSSjiitFxS1COfVRapepxwZzP8aW01Xdb5wt58KmdXrUdnV1TQrEj1bhOuwpzZcTwoL0LlZ-7fgFDKmG3sv78Lsid-xyXM9nrsgrghyeKPDGZqPfAk43ufKzTgqgETkSFCku0OGm7g5OJHKULsllXz1bHyTYNC29_ra6e9nVDRvLMHzKGsLcgXLFOy4E42Ljt8bbX1OsHYXxvcUsPtF73GLU4s7v_fwO2gtIzo4Oxki1A4G2JfbfAD5xvaxk3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این بزرگوار که قبلا گفته بود بخاطر یه تیکه نون به سگ دادم اومده داره ترامپو تهدید میکنه میگه بیا کوت عبدالله ببین چیکارت میکنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/news_hut/67328" target="_blank">📅 13:35 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67327">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🚨
🚨
❌
دیوید کیس مشاور و سخنگوی پیشین نخست‌وزیر اسرائیل:
تنها دلیلی که ما امروز تشییع جنازه خامنه‌ای را بمباران نکردیم آن است که 10 هزار مأمور موساد در میان آنان داریم.
@News_Hut</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/news_hut/67327" target="_blank">📅 13:20 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67326">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0be756a04.mp4?token=rfcz84OVHs4SoZYKu8flPj6t0Q9tPJgn87Zyw_wH7xohP_IlK197XECIZtZ_5pqxSZ_FinwkWGV-RsOev_PlA_CMxm1OuIfrvnKsbwhpD6NGDt5Nxx7cFn5GqkWufksL9sJ4LU8_dcb1nnMrf0TB9uQXdxNoTREpo3_ECc7vT_BUAC6j6saacrdyNlW3Zw2NykVEB7dqCX3LTKS_v8cTYyhtppM5ufJDYqz8MK2bg2kRiHRrrwa8vhr8DZUbSuadoPLGnkcyoWz4-_691XYkq0TqMwCIzYAPpkKVmOKuTkIm_r37-D-4t7BJlPVcUq2khZ0jHA3-noFqRm2aYAmjag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0be756a04.mp4?token=rfcz84OVHs4SoZYKu8flPj6t0Q9tPJgn87Zyw_wH7xohP_IlK197XECIZtZ_5pqxSZ_FinwkWGV-RsOev_PlA_CMxm1OuIfrvnKsbwhpD6NGDt5Nxx7cFn5GqkWufksL9sJ4LU8_dcb1nnMrf0TB9uQXdxNoTREpo3_ECc7vT_BUAC6j6saacrdyNlW3Zw2NykVEB7dqCX3LTKS_v8cTYyhtppM5ufJDYqz8MK2bg2kRiHRrrwa8vhr8DZUbSuadoPLGnkcyoWz4-_691XYkq0TqMwCIzYAPpkKVmOKuTkIm_r37-D-4t7BJlPVcUq2khZ0jHA3-noFqRm2aYAmjag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جمهوری اسلامی پس از ۴۷ سال در مهم‌ترین رژه‌ی خود حتی به‌اندازه‌ی بند پوتین‌های ارتش شاهنشاهی هم نظم نداشت.
@News_Hut</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/67326" target="_blank">📅 12:27 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67325">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ac4BNJdKFqVIJe_cfPKqTKvb_EVAOEg66WXMcbywQo9D5t05-Mmx_p2g-ODN1agpc9qk3-E7xBq7rMkF9dFerR13KLGullf06zN2_iJD35ANN7mQQvMbxK8iXpu2eG952_SipvwMhUIyWfr_6AWX0TvMfxieCU6qz8TXf_FFa24tIuzt7atsz87ois5SZ9RCQNaLJFOorJPD58A6w9RD5aBMWosRENSXpT3B-jrPFtwA7tusnklUEG2EEUl9byazNkeIxfyv8_jxx_FcW7kRnzoSiML_T4XA3v-MUQVRCBAqa0VkZHUaWqJwy7Et5anU43ECpU2ykIjWKCb4j7ngTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
هرمزلتر:
🔴
نیروی دریایی سپاه با استفاده از قایق‌های تندرو، کریدور مورد حمایت آمریکا در تنگه هرمز را به طور کامل متوقف کرده و در نیم روز هیچ شناوری از این مسیر عبور نکرده
🔴
سپاه صبح امروز از طریق بی‌سیم به تمامی کشتی‌ ها هشدار داد و همزمان قایق‌های گشتی نیروهای ویژه را برای اعمال کنترل ایران بر تنگه هرمز مستقر کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/67325" target="_blank">📅 12:03 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67323">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eaB0osKUzDmp6z3ij2h6F5IuJc_2UnA_E4GzGrpS17rA478rtwXPUFHwDSAXWxaliA5OoE0KWo3ob2b4wtndC1O8w6KgBVcOVb9FQI7V1LCAu6WD0bX1J_6h5v4YOyVLHc254w9_r3XQJOOIirdcW81ZkELLtNd-KG4UbbhY0Fqnbu78oov8ZcDTUckpx1yZn-i6CTWBVEtnqh3DVS5bZwGrx94r-3G7ln9ok4Vl0t6H0z9CQmjs_yHNBGoLSsUnfXOx37FraI4V1LYG4aGlWwgu3eLPyOS4s1FeP5roMc4okXDGfrnsLe2BWB2WJFL0Ilfjq1MaEyd1cYYmS7GB0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f22dc07ca.mp4?token=PnlSlFQR-48f5XCqZvlHzS3KnmZ60LBSAFYh96fq5xkDKbDNoNLTY3SNw6zq8um0ThL8IUcDJ6I0XUHPqBbhhGCL8X5tqgxEk3_fVIft59owZYph7y77zY-qvAlhnhoBBTbVHYCbnz9zH5fSIQNqjXZtGtJOMcQR_ohTW-IYvcqGzKcSuYAeTgUrbExhgHuw5l2OIK5EgcJmq9rAii-RikJbOlWDUjd4O2dcVj9EyhPmlVDLATQg_JRGYKmNqz-WBXBQRbhx1Du2ffik7Lox5WcjgI1r2oJx8OrehCX-8nT9ZMk6ch_9o-7jvT2BuGmjWuB2mctN2WglTX1hJiGQHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f22dc07ca.mp4?token=PnlSlFQR-48f5XCqZvlHzS3KnmZ60LBSAFYh96fq5xkDKbDNoNLTY3SNw6zq8um0ThL8IUcDJ6I0XUHPqBbhhGCL8X5tqgxEk3_fVIft59owZYph7y77zY-qvAlhnhoBBTbVHYCbnz9zH5fSIQNqjXZtGtJOMcQR_ohTW-IYvcqGzKcSuYAeTgUrbExhgHuw5l2OIK5EgcJmq9rAii-RikJbOlWDUjd4O2dcVj9EyhPmlVDLATQg_JRGYKmNqz-WBXBQRbhx1Du2ffik7Lox5WcjgI1r2oJx8OrehCX-8nT9ZMk6ch_9o-7jvT2BuGmjWuB2mctN2WglTX1hJiGQHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
و بعد از چهار ماه همچنان عامل این جنایت و قاتل فرزندان ایران چال نشده و اجازه چال کردنش رو از قاتلش گرفتن!
@News_Hut</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/67323" target="_blank">📅 11:42 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67322">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5f6d58549.mp4?token=LjpxoXQpGdrLbuPc76Q-bVVz3NX4mh04wj6NDO33-UF_gvL_A6OXxJKuhOLt4E_UfbjCtg3WdSIeMywzIzG12jBc0f-ff9GlkXYCf4zS6fWbuXK6QI-3nqIwYSA-cU3AlygIs6tKFlIkktSnPpA-k-kSxCzBYwJ7Z5TwVROGwwzE8ojqM6mSlnSYnpKQtRJBI3u_2Fuf5UnLKfwcZNGClehxN7U8Jf3FBwcKt2XVZuMNUPddEunTLX4ncN92K0ZJOBhZpA3ysJ_wlsIzB9MzAlBNc2vgG-oguNGlDImk4OVyWgAyicK8l1CXc9RmDL_zJgEjPlJFWW7Lgfzo83eGAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5f6d58549.mp4?token=LjpxoXQpGdrLbuPc76Q-bVVz3NX4mh04wj6NDO33-UF_gvL_A6OXxJKuhOLt4E_UfbjCtg3WdSIeMywzIzG12jBc0f-ff9GlkXYCf4zS6fWbuXK6QI-3nqIwYSA-cU3AlygIs6tKFlIkktSnPpA-k-kSxCzBYwJ7Z5TwVROGwwzE8ojqM6mSlnSYnpKQtRJBI3u_2Fuf5UnLKfwcZNGClehxN7U8Jf3FBwcKt2XVZuMNUPddEunTLX4ncN92K0ZJOBhZpA3ysJ_wlsIzB9MzAlBNc2vgG-oguNGlDImk4OVyWgAyicK8l1CXc9RmDL_zJgEjPlJFWW7Lgfzo83eGAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مهدی رسولی  مداح بیت رهبری میگه برای خون‌خواهی اومدیم؛
شما هنوز خونخواهی سلیمانی و... رو نگرفتید بعد میخواید اینو بگیرید
😂
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/67322" target="_blank">📅 11:10 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67321">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5807c7f54.mp4?token=qzjfrR74N8kUHThDdwDs3mutU0HLll60A-iRTQpeoNtEQFopPnYWr7DoEXtyJbgu-mN2xvsG0__G4_7zTHHOUqQ-6xMgg3KQ7__LZ85o3qJnh4zF5hdNx0VZGF1XPgmkCrgifT7F0btsN4JYRJad3N8F36aY8g6xvSBelKvOscRLaQKTTr_W4qhyulMhAR8bnpb6bmtyQjK0s_mXGPbcpM7ee_97nf2JqU_TXuJTw9HW_f_SdxUt0wmMInAu3SRGWpnGkrtw2pDrX6xSsvza_3Wmp4_I_t_TLdCbRTeO_wCarWy8i6sVfPssqhPpj0Dwgve4D2Qi8jdwSdnD86n4wQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5807c7f54.mp4?token=qzjfrR74N8kUHThDdwDs3mutU0HLll60A-iRTQpeoNtEQFopPnYWr7DoEXtyJbgu-mN2xvsG0__G4_7zTHHOUqQ-6xMgg3KQ7__LZ85o3qJnh4zF5hdNx0VZGF1XPgmkCrgifT7F0btsN4JYRJad3N8F36aY8g6xvSBelKvOscRLaQKTTr_W4qhyulMhAR8bnpb6bmtyQjK0s_mXGPbcpM7ee_97nf2JqU_TXuJTw9HW_f_SdxUt0wmMInAu3SRGWpnGkrtw2pDrX6xSsvza_3Wmp4_I_t_TLdCbRTeO_wCarWy8i6sVfPssqhPpj0Dwgve4D2Qi8jdwSdnD86n4wQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قالیباف یه 20-30 سالی هست درحال گریه کردنه
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/67321" target="_blank">📅 10:45 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67320">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/810ada8a67.mp4?token=l386xyC_fozaBtfIp6X07mxH80rnFVF545fmzsICpGJEmhAbH81XloOi-mVg5VTZWlyO6ONIjqkyWul_awtaSQTdEwKeuFSQyiYlpdPsX9vt5TIVExlbcaOjoq8ptPlUTyGOElhwSFBL5DCONWf_JcNQph1O1WgHrH2fhugGt8vNUifrNFwREhA-LClySY3Cxqx_miQZb2ZtVKD9bHgs-HJbH7i8FgT-LxkAWPExcoO0RsM9uCbvReMe21kZ40nZelWq_yP7hFI-9PtK08wHBk9f4UcLaiSvPysgMDC2Vnmde8cAJbRDO6Y4qQvYg6dAaxHEi1xvt7yK2V0XMgdh4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/810ada8a67.mp4?token=l386xyC_fozaBtfIp6X07mxH80rnFVF545fmzsICpGJEmhAbH81XloOi-mVg5VTZWlyO6ONIjqkyWul_awtaSQTdEwKeuFSQyiYlpdPsX9vt5TIVExlbcaOjoq8ptPlUTyGOElhwSFBL5DCONWf_JcNQph1O1WgHrH2fhugGt8vNUifrNFwREhA-LClySY3Cxqx_miQZb2ZtVKD9bHgs-HJbH7i8FgT-LxkAWPExcoO0RsM9uCbvReMe21kZ40nZelWq_yP7hFI-9PtK08wHBk9f4UcLaiSvPysgMDC2Vnmde8cAJbRDO6Y4qQvYg6dAaxHEi1xvt7yK2V0XMgdh4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
در جریان مراسم افتتاحیه مسابقات «فولسوم پرو رودئو» در ایالت کالیفرنیای آمریکا، یک چترباز پس از آنکه پرچم همراهش به درختی گیر کرد، تعادل خود را از دست داد و به شکل خطرناکی روی یک چادر سقوط کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/67320" target="_blank">📅 10:15 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67319">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ca0cec0e0.mp4?token=ZU8HtOswhTN1IPsrpVpH3ea0Pf41sm85uoSJacmJApIPN47h2iJwqXjEOImor0MDbvOmxFrTlrl73wcGFND0lm9AU9EWRDahrFXKuppV0jmpZKDjZs1f_6Ch5WZcJLXgvdfhy0e0QcjHpCbr3Yt3IJS6q8V9K3bfV9KYSNWGJMrp2x2UvqEMYQUELr7wL_Fz8pO6F2CLsNkFafmK3losLGDCNZpMe3JkPuRotFnXAefciPq2d4pcI9e-jBmY18P4HNxUHBDNuQ7-0WTCSjm_uJOvC37lupp26aMvettLfDW87TBryUAHCazuVXgeZX_0OJHnLF-3ZZDe2wjSCelMqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ca0cec0e0.mp4?token=ZU8HtOswhTN1IPsrpVpH3ea0Pf41sm85uoSJacmJApIPN47h2iJwqXjEOImor0MDbvOmxFrTlrl73wcGFND0lm9AU9EWRDahrFXKuppV0jmpZKDjZs1f_6Ch5WZcJLXgvdfhy0e0QcjHpCbr3Yt3IJS6q8V9K3bfV9KYSNWGJMrp2x2UvqEMYQUELr7wL_Fz8pO6F2CLsNkFafmK3losLGDCNZpMe3JkPuRotFnXAefciPq2d4pcI9e-jBmY18P4HNxUHBDNuQ7-0WTCSjm_uJOvC37lupp26aMvettLfDW87TBryUAHCazuVXgeZX_0OJHnLF-3ZZDe2wjSCelMqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اولین حضور عمومی مصطفی، میثم و مسعود، سه پسر علی خامنه‌ای، در مراسم تشییع او در مصلای تهران.
مجتبی خامنه‌ای، جانشین علی خامنه‌ای، اما همچنان در انظار عمومی ظاهر نشده و در این مراسم غایب بود.
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/67319" target="_blank">📅 09:55 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67318">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd6157bafc.mp4?token=hN1Hqon8DbV9eofxzEtAiPV6Cs3agA8dNv6IMRuNRZDf_nSru7jm8R4_FlY24n0jA6p1Gu5vc5G6cXCwwnTt6C06YiCO6uJRnbyjRJiKizIsH2NA-0cuXt17b06GVrCi1_r0gxrbjeKhXRexiFyBVepHfVlWwnzO0PBx0wH5itr3XsgUqkXlqSZe1mrC6mSqIFSHsnn0cim6ZYOP_oQBlzL6_qgg-0BiJIjEk8tmN1rmkMjTeDn7oNXduWq85SPz9AHOBBbF6HX_dP7QIDufl4xUJorhGJABE83cuKJBuLvajELwAfnNR6qps6Tfs2KOICUO9m6Gnxmet7D_KTgPwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd6157bafc.mp4?token=hN1Hqon8DbV9eofxzEtAiPV6Cs3agA8dNv6IMRuNRZDf_nSru7jm8R4_FlY24n0jA6p1Gu5vc5G6cXCwwnTt6C06YiCO6uJRnbyjRJiKizIsH2NA-0cuXt17b06GVrCi1_r0gxrbjeKhXRexiFyBVepHfVlWwnzO0PBx0wH5itr3XsgUqkXlqSZe1mrC6mSqIFSHsnn0cim6ZYOP_oQBlzL6_qgg-0BiJIjEk8tmN1rmkMjTeDn7oNXduWq85SPz9AHOBBbF6HX_dP7QIDufl4xUJorhGJABE83cuKJBuLvajELwAfnNR6qps6Tfs2KOICUO9m6Gnxmet7D_KTgPwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
زاکانی و برخی از مسئولین تو حاشیه مراسم رفتن چلوکباب خوردن، عرزشیا هم اون بیرون زیر آفتاب، صف وایسادن تا تخم مرغ آب پز بخورن
😂
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/67318" target="_blank">📅 09:33 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67317">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c7YME2u8bvE2FWFGwBcNjvVV1IfKPlNMALyxhHszxjDBU43HSMuYYyGBPXPbw-MQ1iIEiXiupFn97biaks6DVFAGTJa_IGgZsMmwoM0imeLiJVHyAKmGacSTnq0H_FbXTN6J5py9hh9ZOyXYQDKVwBKYww2DWNgLHL3JJ_5Hz33d7jtMO_kFaSQsQulwoXxq10bLkSBymeI9Gckl9JtYfCQ6lpDJ4FYwuQNzb017HGarwQnf5DUEaYbqqks9CqCcX8oAehppeTJFRjDQ3ofP56bpkpARrb0gzghXSJSagRNo94jCkn2M-_yG9k8LrPTOecQX2mq7RNwt33ik7Pbg8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
8فروند جنگنده A-10 Warthog در پایگاه هوایی موفق سلطی اردن مستقر شده‌اند.
🔴
این جنگنده ها برای پشتیبانی عملیات زمینی استفاده میشود.
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/67317" target="_blank">📅 09:02 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67316">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/67316" target="_blank">📅 02:47 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67315">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DkXKubrHFJaReOe9Kh1khvnPHZkhuZ6czj7YQ2DyEhdNxh0_GHmNhyEQxZxWkqaPKPoXqXqLmG9cMN7Q7liycma7w1nTsj5nK0IV60pzSE7lvhvSI8oglP1farUeV0vN2rIEgmFNGFZE5RSZWg3FG_J58989gTf3RS6hNpvTojT-_FnaZ-r8OelQmXgNsvMUsyvoehjN9Ua-9UUWLgvyWn_OLprjBzQklpFoJFHWALvPMXf1m5pdupSAjjPq5ZdiqXDTpTWEVC57_vnealmB_onS_ZY2NBFmrKofKM1D7GWZZSbdX4oUi2LTN95dmm946JokUrFj_um9uyjdaU17cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet
@FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/67315" target="_blank">📅 02:47 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67314">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cye3988uUL2dfVzqRza6D6X0oHn478y3vtwdpo-sVpEqnKcOjhSWUS5e02yjLZ8ve9He-hfOrWe9gct_Tk-aX7_Z-hTUD9zVDJOJnviPA8Mw30cTIkUEGA8wxOQTZdhuKtHUxgDOuKwsq_VkeSPVi1daK_LT1-29nz_DKL34go3O8pgg0MAcMXPYz4QWFx0XsBuCsrNUGBKJJ3-fUc3nA7ef2HiwZSWJ-OQrHsxnyk08BlPff2UXMdrvOXC4ngzE74_179hY8e0ZJxTtyDTONxJw-4VBQzqKR3HnnTimlQGJhQY5RMLQ4NE9bZQgZpFUIQVwJ9cdE4QEAJ797aI47g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باراک راوید:
ولادیمیر پوتین، رئیس‌جمهور روسیه، با دونالد ترامپ تماس گرفت و دویست و پنجاهمین سالگرد استقلال ایالات متحده را به او تبریک گفت. کرملین اعلام کرد که این گفتگو یک ساعت و نیم به طول انجامید. پوتین از ترامپ برای سفر به روسیه دعوت کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/67314" target="_blank">📅 02:06 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67313">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79806b6dec.mp4?token=OqE4wxyC_nI-_a_PxU6GULNmA8wiRz3NAaAj31iylIW7WYnmeKZmva7UuO9CHxvmTSe5TiVmmLhXCQ9h00FtSdGf5CmnXuwdMqFjXr38qsukHTCK2HfpXaAj8pG1X6tuRHwqIyaJWAI7Qc7MVUto_NJOFxya4QFZC6Dj3SRQD4YKkAZlYuHioJ3Ns5VJesX2gnIEY_Q_aV5s-sE2rlxeTfG10I5s4C5mlrO8h9X61BePuLMCq54BG7n8ZNpaOBORSMJ9wqLsdvoBIC_o4Ep2BS7HmwNjoPlK_DNLIxYuHHTSsK4VqSwWKM5LEUHGOVVvyLX98XwWqQ6vnR07xYnkUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79806b6dec.mp4?token=OqE4wxyC_nI-_a_PxU6GULNmA8wiRz3NAaAj31iylIW7WYnmeKZmva7UuO9CHxvmTSe5TiVmmLhXCQ9h00FtSdGf5CmnXuwdMqFjXr38qsukHTCK2HfpXaAj8pG1X6tuRHwqIyaJWAI7Qc7MVUto_NJOFxya4QFZC6Dj3SRQD4YKkAZlYuHioJ3Ns5VJesX2gnIEY_Q_aV5s-sE2rlxeTfG10I5s4C5mlrO8h9X61BePuLMCq54BG7n8ZNpaOBORSMJ9wqLsdvoBIC_o4Ep2BS7HmwNjoPlK_DNLIxYuHHTSsK4VqSwWKM5LEUHGOVVvyLX98XwWqQ6vnR07xYnkUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
جمعیت هموطنانمون در تجمع چند ماه پیش تورنتو رو ببینید و با جمعیتی که در مراسم تشییع جنازه علی خامنه‌ای اومدن مقایسه کنید
🔴
فرقش میدونید چیه؟ ۸۰ درصد جمعیت در مراسم خامنه ای اصلا ایرانی نیستند. کلی لبنانی عراقی یمنی و فاطمیون افغانی گرسنه رو با پول و... آوردن بازهم نتونستن مصلی رو پر کنن!
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/67313" target="_blank">📅 01:29 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67312">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FSCRo-pWVyW-vF2zHNSD-pZ5LLY0SfPRkPGIdDoHzd_XLHAWCzcrD56iTxEXrmS6qLucDs5mAv6-1mljJFI-0lc_9dO3ieZKwcYdLjjFqcgyLgbTAR_VymOfBH17tvTLwuGCfAvapbqLwYOhtzwVoBRNg7SfjFQqTMPlX0UFZvF3FHMymBrrQgpQA1JSRO4vSj2clGL2tcol0gabywKlphZV8bLZkxOrvm1f8mUMeEPmTPU93lIrH70pf8V06rFCKT8okPSSDipoH3aenCANn1PmpISV3lVLAQvJKuV7lh5D9-UY69RCaC70MC90qt2PhaQChJrjyyzoaUZQlcn_Qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
نیروهای ارتش اسرائیل در حال عملیات در منطقه حداتا در جنوب لبنان هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/67312" target="_blank">📅 00:50 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67311">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5be218b45.mp4?token=bZvjCMaFjaIVPgv2yw-AfE25sDwRLuB3Qi89heHHV-mQqw4VmFg5PUAoMfbHgsPmON4qldfniZ20bIwCbD-MpNX2nY3KGvx67-UulUB2ZrpF-W62A0OVFr9fCbuL2aTpFHoHl-M6I-okjzb9HEs-hrQ70H2jgLX6nPkPbVqWTEy4zSGXBZ0OcBFp-p6GMuUeiaWawz1fBkV3Kkv0-dUJjYay_itlBalYWTQzeNx7bXchbYM_tvWLh4x6-VQUbXxH5FdZN-Be0Qf9eUFbtk_ASkKrvK943nFesd0MsI8_AQ6XObkSbl55ay0I9F4AZgaKUpL2wtp-ktLpbsrgWhqixg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5be218b45.mp4?token=bZvjCMaFjaIVPgv2yw-AfE25sDwRLuB3Qi89heHHV-mQqw4VmFg5PUAoMfbHgsPmON4qldfniZ20bIwCbD-MpNX2nY3KGvx67-UulUB2ZrpF-W62A0OVFr9fCbuL2aTpFHoHl-M6I-okjzb9HEs-hrQ70H2jgLX6nPkPbVqWTEy4zSGXBZ0OcBFp-p6GMuUeiaWawz1fBkV3Kkv0-dUJjYay_itlBalYWTQzeNx7bXchbYM_tvWLh4x6-VQUbXxH5FdZN-Be0Qf9eUFbtk_ASkKrvK943nFesd0MsI8_AQ6XObkSbl55ay0I9F4AZgaKUpL2wtp-ktLpbsrgWhqixg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
علی خامنه‌ای،‌ 3 بهمن 1403:
ده‌ها متوهم به درک واصل شده‌اند. من به شما عرض می‌کنم به فضل الهی این تجربه تکرار خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/67311" target="_blank">📅 00:41 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67310">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/67310" target="_blank">📅 00:41 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67309">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HwSCGUdUNB10VpgvDBCyAoBLcCoNoKNM7bYthHhmPoIv6eRku6CLmn7scLxzKjG8KtJaNH1coHz53Por92hOX8OvnkOhDiL11Iw9HGrc5tfyR08Wj8ShqRQ2fotP6HFjw-ZR5NzahfWWkI4CcJVRiPs0m5pgprWT6cn35DcQUneTOdrXxzcC3lQup-4D-_UjSCeCmUSNvs_84HoGky0jwB2HX_X9csG0IOEFIHS7mglvS-Qnp4TXfEYZ-jfDDqG8cToEZOsoA3_f24g2oUz2OlRG2TUAwwcNh_rDE2BvKqgBaV27zM_H8iL5_NUTWJewsZWeQRFPbGP8JWn9Ea3Yyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet
@FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/67309" target="_blank">📅 00:41 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67308">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/842bb5b4aa.mp4?token=ADKLWKg9OXiryKctkVw4-oO-5goQb27pYLtDLcW23MzCiHMtZ2UQOxr3IqJBxdXl34eRMt3QdprCDrAGZpzdgYmCLFaSN-nkE9g83ZYare7iYSIuf5JDXQCEheZNhu1nS7SMC5y7f4d2I3_nosBlCldTqTL-cXcmMPa5Nbg7bDUVHU2Ctm4v_N2QWepNKj7AtwOiLyzvb9v_eat_wXdapOtzXZL02d1aNngrfyDkgFCRsiMu5BzWCHqBkD3wxoa03EcGK5r0zlXi6QpBYt7x59UuSX24PlSRFEqB9-N0l3_azu43HkWtXk-c-Sd68WYmnzYeX-UN6XB8f0brgs78GQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/842bb5b4aa.mp4?token=ADKLWKg9OXiryKctkVw4-oO-5goQb27pYLtDLcW23MzCiHMtZ2UQOxr3IqJBxdXl34eRMt3QdprCDrAGZpzdgYmCLFaSN-nkE9g83ZYare7iYSIuf5JDXQCEheZNhu1nS7SMC5y7f4d2I3_nosBlCldTqTL-cXcmMPa5Nbg7bDUVHU2Ctm4v_N2QWepNKj7AtwOiLyzvb9v_eat_wXdapOtzXZL02d1aNngrfyDkgFCRsiMu5BzWCHqBkD3wxoa03EcGK5r0zlXi6QpBYt7x59UuSX24PlSRFEqB9-N0l3_azu43HkWtXk-c-Sd68WYmnzYeX-UN6XB8f0brgs78GQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویس‌هایی لو رفته از ابویسانی، معاون وزیر اموزش پرورش حین گفت‌وگو با دانش‌اموزان معترض ؛
دانش آموز:
نه اجازه میدین تشییع رهبرمون شرکت کنیم ، نه اجازه می‌دین پیاده‌روی اربعین شرکت کنیم، چه کار مهمی الان دارین؟
+ ابویسانی :
اربعین بخوره کمرتون!
دانش آموز:
ما می‌خوایم تشییع آقا رو شرکت کنیم.
ابویسانی:
برو بابا تشییع تشییع..
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/67308" target="_blank">📅 00:17 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67306">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JRVXtNfeSWZijdP0HD7RFBjcLkjBj9nACQORROjfR_y_hGMVshIJfj7popZQX50D_5VbIIfVA6nCPGFCvElFhS-pvKzxYcneLptfcovbr607Mhe_r4PD6FsekzC3TjcRM2KvQTRC68XmebXe7r5rjGJjOVjrO5KY5u3UdF025iEsFDo0pgm9dtkSx1jt7M5-ewCV-opq6YXWYADlKAfvHqmmYeBxi6q0FxInOTJ8Z9E8cp8BVimW-ZaLwy7uMtu4nHnVD4cyS1KHzr1TOJPGrhDDF3D5ywLSHfvBwFQs1ub8aDCJMYtuuJsRIMwiB4wx9fKKbeK7FVva3QjFwd1YrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7ffa7579f.mp4?token=bxvGuBzqY1R4kCymzn-CYtxkecSfGMUdUCq0hgNxONOLMywGuK49l6t5ZWDZhO1Y84J_TLPm2uU-ahBAOy5KDtWrtPoIm9AJnucsXDi00y3xJtHQdkB39k6yFsnUF-jgaigFBcUpfjW30C00xa4tTZEPyc0-3trx7hcGdu_-JVs8TiciR-iA6eaqUDLZeXkg4LUBOL0ILmOOI9zy9JRgnJ6ZgnCDRkdzTt0ORuL7BxPrSzFnGz7B6HQBQlK-ed3Ow40sj41MuA54CmSUPtDy1X7C8OaHDzJzF1u4dONa2sABwPMvHWBQciwb9fv4rO_RFprZJwhPsIh4piDW0c-s-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7ffa7579f.mp4?token=bxvGuBzqY1R4kCymzn-CYtxkecSfGMUdUCq0hgNxONOLMywGuK49l6t5ZWDZhO1Y84J_TLPm2uU-ahBAOy5KDtWrtPoIm9AJnucsXDi00y3xJtHQdkB39k6yFsnUF-jgaigFBcUpfjW30C00xa4tTZEPyc0-3trx7hcGdu_-JVs8TiciR-iA6eaqUDLZeXkg4LUBOL0ILmOOI9zy9JRgnJ6ZgnCDRkdzTt0ORuL7BxPrSzFnGz7B6HQBQlK-ed3Ow40sj41MuA54CmSUPtDy1X7C8OaHDzJzF1u4dONa2sABwPMvHWBQciwb9fv4rO_RFprZJwhPsIh4piDW0c-s-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بعد از مزدوران نیجریه‌ای حالا یک فاطی کماندو از بوسنی و هرزگوین ببینید
😂
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/67306" target="_blank">📅 23:59 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67305">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af68b2c3a9.mp4?token=OHZNHf2rqPRuI6kfCZSFkt1-vyU339T9exZIOKyBOqAYVEjzzYGC_ftC1Nd0CK9NAM-1AIyQNkzpc1kp_iO_xkJRUBR3iPKtaY66dVvgFkG5oUdWUHD4TZrd84RreG8VMETIHaBSyo7BqQlGMpeWnwQ6mJR4XJP1YZkMdlfe9HltAcQhwP1IH3Vks1IiDtFTHI6J_L7ma66g5Xp6Bwn5HFhGAViR7MVZYS1Brt1k_OQgEm4C2uSNeECmQemv3cVgGaEhHNIw-yTPLTGrLwT6RRkS27GVtScFU9Tc2d2g-JAYNhuMiLupO5PY1MIklog5Xf0IfZ6sZOQ9psLn2XIwmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af68b2c3a9.mp4?token=OHZNHf2rqPRuI6kfCZSFkt1-vyU339T9exZIOKyBOqAYVEjzzYGC_ftC1Nd0CK9NAM-1AIyQNkzpc1kp_iO_xkJRUBR3iPKtaY66dVvgFkG5oUdWUHD4TZrd84RreG8VMETIHaBSyo7BqQlGMpeWnwQ6mJR4XJP1YZkMdlfe9HltAcQhwP1IH3Vks1IiDtFTHI6J_L7ma66g5Xp6Bwn5HFhGAViR7MVZYS1Brt1k_OQgEm4C2uSNeECmQemv3cVgGaEhHNIw-yTPLTGrLwT6RRkS27GVtScFU9Tc2d2g-JAYNhuMiLupO5PY1MIklog5Xf0IfZ6sZOQ9psLn2XIwmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
فیلم خاکسپاری رضاشاه بزرگ در تهران، زمانی که جمعیت تهران فقط ۹۰۰ هزار نفر بود و بیش از ۲۰۰ هزار نفر در مراسم شرکت کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/67305" target="_blank">📅 23:43 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67303">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Qreb2YdlAK6ykfQ4H_rUd2FrVOMMj66veUSjLzbyYQP4B-Pf1XBQ7Gtna5j1uPth3pwN5Z4F8pg5mNMqU_l1B_LvuXiGWy9OYGBbqfkbjsaAxnOhOPD_PLJi1HVti4g68c4fChH2cfcLQ3V42s6zpXVBMZVK8v_CG-lCh1212K-EVfbGGna68fvzi3LEJI9YwOqXIb3ZP9wXDQfJJBHtKA7oEXcY2lGvVivisrpIq-Q_pVEAI1uH3qSNyqcr1jOJrusyfi_Ans_z0AN3292JeBC1Nn3_JKl8UShh4QhNBGitFch2slF_dIhHftS7N-f28zna3N5lhLVntzkElxRjNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j6k0bvx1Kpms6ekw7KZI7fGANpqo8S2U2Lq7JkpNqZz5OyFF-w0W4_DRbLlAVrEQ-x_L4ionETtWlNy72d3u46bE5mZ6XI5oIgRK10Oq-SZSDl9jwUflMXutemyQpItNYugaA6e7cYCPendoaB_ngL9a9Ohw5er5fQCpoRpR1a68YHB6BA07Q1MmiaTfFfmSXenkWlsSamcolTc8qIqgU-0ybGksBN0RbjTYmJTb00WvgtAGK0Rx_D-0Z3905_vUK6PIXmE0xIiN9B2bvAY7WA6nq87BJmqs1zfOJ0q78MZHwMDjdWveGswltVl7pOEK1i547iXBTNrU8NSLeymjog.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
زمین گرده...
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/67303" target="_blank">📅 23:17 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67302">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ReZ8rSgAK1IlPL5GoAy2TEWjf8w53Pt2rcRmPT_JzXa7MDQaNBQpNNTBaYiYtr2NH1OqMBwRPih7IG64zwASN68lbBXX2CibY4koIdrUElWKuu6NoTMq352QZfNuSyTkkJHzcxdd8FTd-oP9KlVVhHN42b95iNR4K-Ijah1vwvN0he3Jb-OCEXZfO6Y5HGbIQn04KAkgo23uoE-MZeGOApsJRFae42V1lHpAteScWmGUcpRIodhMlTNxtNDidyNmEeGVDvWOi53braNX1Ty8ArQvKtGJctnWtyNcOONlSLKYmhl0s4na5rFxesX21EaO7Yw2M80dFTQTj2g1q9fV7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باراک راوید:
دو مقام آمریکایی به من گفتند که مسیر جنوبی در تنگه هرمز همچنان فعال است.
یک مقام آمریکایی مدعی شد که اکثر کشتی‌ها با سامانه شناسایی الکترونیکی خاموش تردد می‌کنند تا توسط پلتفرم‌های اطلاعاتیِ «منبع‌باز» (Open-source) رصد نشوند.
این مقام تأیید کرد که ایرانی‌ها تلاش می‌کنند از طریق رادیو VHF برای کشتی‌ها ایجاد ارعاب کنند.
مقام دوم آمریکایی اظهار داشت که سرعت تردد در مسیر جنوبی طی روزهای اخیر افزایش یافته است (حدود ۵۰ کشتی عبور کرده‌اند) و این مسیر همچنان باز است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/67302" target="_blank">📅 23:01 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67301">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0711bc2f95.mp4?token=bLRXANS3r_nPhaWxp8JxIhxqblkEXauEYCRvmQrescMwCXfDzMX2MFw5pzLQbSWnMQeT-Sqcj6PE2qEM6OHSZFXtAMmdfwS8J80dIUq_tNuGF-6e6dt_-9PfEs93q19dk3AdtJ6pbE1Dgn11k1Wqr_16xm96B4xfSkhlY1sR_MQTltHHPBqgp4xukTHMvXM-SKqiWfBBU_emw__sJAEg-3LrtKkbWzo7m0DYvAeKBi6ghhIEpXm4QABzqnCn3WROHiTKanSzIzwHyI0P44qi7zGkSa7GQ85wmZQapVV08hh9QbMrx77BZpkM8MuaCWUcOI05UdpT28bVbosm-HigFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0711bc2f95.mp4?token=bLRXANS3r_nPhaWxp8JxIhxqblkEXauEYCRvmQrescMwCXfDzMX2MFw5pzLQbSWnMQeT-Sqcj6PE2qEM6OHSZFXtAMmdfwS8J80dIUq_tNuGF-6e6dt_-9PfEs93q19dk3AdtJ6pbE1Dgn11k1Wqr_16xm96B4xfSkhlY1sR_MQTltHHPBqgp4xukTHMvXM-SKqiWfBBU_emw__sJAEg-3LrtKkbWzo7m0DYvAeKBi6ghhIEpXm4QABzqnCn3WROHiTKanSzIzwHyI0P44qi7zGkSa7GQ85wmZQapVV08hh9QbMrx77BZpkM8MuaCWUcOI05UdpT28bVbosm-HigFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مردم اروپا با دمای نهایت ۳۶ درجه
🆚
مردم خاورمیانه با دمای حداقل ۵۰ درجه
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/67301" target="_blank">📅 22:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67300">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eda932d9d3.mp4?token=jGxwDCCA7wQ8oDQz43DZFuOywpGRAyG9sx4_nVgdS7e-v-_a7ZDpl22X5og4GYu09-BylM3hn0KLoFM8MqJMxI0xUNGy9h4Ij0CLg9ChqQU2TVpp0crPyVUQolrE3p80FGsdYwmgJMUdWRCJ9hg88SlMD5J7N7h3piGWGPif9tAc2HbPyHURbRmTYlisRCRLZi5UyPsqKSEHRE4dToJNEO0tQdDQmiO15xcKqVGGvJfGlKN7ssdgFgC65pBE7aACUv_OfmCr2jav_vaiW78-glzgIkP7Vqf8Pj3xjIFy7FXLozap-KGTs1DYYN8lfQKhTNWCp0TwE8qP15k69wGXSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eda932d9d3.mp4?token=jGxwDCCA7wQ8oDQz43DZFuOywpGRAyG9sx4_nVgdS7e-v-_a7ZDpl22X5og4GYu09-BylM3hn0KLoFM8MqJMxI0xUNGy9h4Ij0CLg9ChqQU2TVpp0crPyVUQolrE3p80FGsdYwmgJMUdWRCJ9hg88SlMD5J7N7h3piGWGPif9tAc2HbPyHURbRmTYlisRCRLZi5UyPsqKSEHRE4dToJNEO0tQdDQmiO15xcKqVGGvJfGlKN7ssdgFgC65pBE7aACUv_OfmCr2jav_vaiW78-glzgIkP7Vqf8Pj3xjIFy7FXLozap-KGTs1DYYN8lfQKhTNWCp0TwE8qP15k69wGXSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پیام نتانیاهو به آمریکا به مناسبت دویست و پنجاهمین سالگرد استقلال:
🔴
«۲۵۰ سال آزادی. ۲۵۰ سال دفاع از آزادی.» او این مناسبت را به عملیات «انتبه» در ۵۰ سال پیش (که در آن برادرش «یونی» حین نجات گروگان‌ها جان باخت) پیوند داد و اظهار داشت که آمریکا و اسرائیل در ارزش‌ها، سرنوشت و مبارزه با مستبدانی که شعار «مرگ بر آمریکا» و «مرگ بر اسرائیل» سر می‌دهند، اشتراک دارند. یادآوریِ یک اتحاد مستحکم.
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/67300" target="_blank">📅 22:12 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67299">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LGGum1LHrbmTeF1LoVP6vQaJNn_scrrFhyzr7iuKjRJm0X9TS4OVApnuKKRRPXIA8yw9v9mpsh1DEHWByJ8vG5uyvg7DnhH2UOQ1abLj5i0va4t-5TKbV7FWl_K48mrH8gwa1kfCqGuCpdfDzCuOlwcEJTZqUFqv8P0ztLIrdxyv-g8Ya7Gt622rIyehKuVi_RVTMnfXfFOL_qdajAD9WlQcmo6DZx-tbv83C2ScpC6tOGf_YhJIIwHHBDE4hxpWd3GNUWACffdhF7zdO40Usr8eDpOIpd0HYMpuE_1OilVlaYJAlyBJ58rhCAUjWyIQ0orsd8zO-cVb9kgWtc1UNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
العربیه:
دور بعدی مذاکرات ایالات متحده آمریکا و ایران در تاریخ 11 ژوئیه (21 تیر) به میزبانی پاکستان در اسلام آباد برگزار خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/67299" target="_blank">📅 21:25 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67298">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DA0VuEQ1B-sgCj3tJxa08VDlhcMWey5Sd8W8bRVGVMjAlf6Q-DDnko8IKQnEhZRA-MbNO1M7nVUow_6kE80yA6oy4JfDAhqtzU8-y07i1FCgJ2fRLd5ruP3K_sfTaPNUUrQa7orKTJMxU5ty2lCmrXEZjhGIBTrd5u9KfEH9SiYYpcnV0G-U4wgRp8oX7XMq-T8aNdzWX2j46h09nq2SZy_eytQpM-3CnlEoK8sVm8r_8MSNX2I3Av1oDSbI7toZ1nueNFgVQ_rFOXUIKpyesJJ9LgIBOuNkkzR0KM3vzWkgnckEMfRJNILRFgQK5j6IXIWfRsGbH-zpPHObIPDsow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ترامپ:
فکر می‌کنم آن اشک‌ها مصنوعی بودند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/67298" target="_blank">📅 21:04 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67297">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dX7hJDIVj8fKzz5OQFCzzqkyo2JiFXyRHqfb4YCf7fG0ICulqIxdv3QBgH0U-QyXLNZhKiWXoCZ64OiEDcLnu7GEifEpOLqXfPlOrHsjRe12gdDlH0ypEJ4fKmB0RQAfvTpL5-KXx_OXP6xdv6cIQTwEoT9KehlmA41Xk1DDgDKPHxi6AWBJTabb8VSKsL4VeHJ3cP1RfJUj14kg_jDWiU3ZOyzPLnJtXgrVJOiC_Ovmv0a29rdbZ8LSeO-XTX7lP8mcRSbNgXl6J1cDky9_d0pmxeQCbjWAqswmOAf1bxPI0tF14vVqefD0HwZ5wGypKiiZwluGSkvtBWYHnrNYSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
ترامپ به آکسیوس:
نتانیاهو میداند رئیس کیست.
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/67297" target="_blank">📅 20:58 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67296">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚨
🚨
پرزیدنت ترامپ:
نتانیاهو درخواست ملاقات در کاخ سفید کرده است و این ملاقات ممکن است همین هفته آینده رخ دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/67296" target="_blank">📅 20:53 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67295">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ به اکسیوس:
از دیدن ایرانی‌هایی که در مراسم خاکسپاری خامنه‌ای گریه می‌کردند، شگفت‌زده شدم. من فکر می‌کردم مردم از او متنفر بودند.فکر می‌کنم آن اشک‌ها مصنوعی بودند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/67295" target="_blank">📅 20:51 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67294">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🚨
🚨
🚨
پرزیدنت ترامپ به آکسیوس:
«همه آن‌ها آنجا هستند. یک گلوله [و می‌توانیم همه آن‌ها را از بین ببریم]، اما ما این کار را نخواهیم کرد، زیرا در آن صورت، هیچ‌کس برای مذاکره با ما نخواهد ماند.»
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/67294" target="_blank">📅 20:48 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67293">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/589cc62912.mp4?token=n7IzB5NO4Vfz8hjHm-tI0CiZPAUyoPjGrzQrSI4QBvPhT7AeopArzeLy7LcNWexedhDnjy9cbERKD_SQMgE-VfjA9ImnvU6bkIDH9zsb2G0X7PmrWv1R4_7Gjb3CGaAXpK7HqPTnJTCfGpo-C7fZvpCuPknCEubWBJmd1WKOz_R2Z8fGYlkQrMPF67R5F1RoeJ9C7joRsyk-R1-VIT0TociYKYg2FhAbC1-XjQLg0HaaEzFY4TU7yR4KkdQZU2xdzqNRjd_-YDE5sJZQ-Jhr4uN0J6x_G0Y8flaV4bs__Y3iLFPsv5Ps15I8ZCwYKrEqgxkCk1VE5xBhm4l1g1Q-ew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/589cc62912.mp4?token=n7IzB5NO4Vfz8hjHm-tI0CiZPAUyoPjGrzQrSI4QBvPhT7AeopArzeLy7LcNWexedhDnjy9cbERKD_SQMgE-VfjA9ImnvU6bkIDH9zsb2G0X7PmrWv1R4_7Gjb3CGaAXpK7HqPTnJTCfGpo-C7fZvpCuPknCEubWBJmd1WKOz_R2Z8fGYlkQrMPF67R5F1RoeJ9C7joRsyk-R1-VIT0TociYKYg2FhAbC1-XjQLg0HaaEzFY4TU7yR4KkdQZU2xdzqNRjd_-YDE5sJZQ-Jhr4uN0J6x_G0Y8flaV4bs__Y3iLFPsv5Ps15I8ZCwYKrEqgxkCk1VE5xBhm4l1g1Q-ew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
۲۸ دسامبر ۲۰۱۱؛ مراسم تشییع جنازه کیم جونگ ایل، رهبر کره شمالی؛ مراسمی که تصاویرش به یکی از عجیب‌ترین صحنه‌های تاریخ معاصر تبدیل شد.
وقتی این تصاویر را می‌بینیم، شاید اولین واکنشمان تعجب از شدت گریه و شیون مردم باشد. اما واقعیت احتمالاً پیچیده‌تر از چیزی است که در چند ثانیه ویدئو دیده می‌شود. در کره شمالی، مردم دهه‌هاست در یکی از بسته‌ترین نظام‌های جهان زندگی می‌کنند. از کودکی به آن‌ها آموزش داده می‌شود که رهبر، شخصیتی فراتر از یک سیاستمدار است و باید بی‌چون‌وچرا به او وفادار بود.
از سوی دیگر، در چنین حکومت‌هایی، ابراز احساسات در مراسم‌های رسمی همیشه یک انتخاب شخصی نیست. بسیاری از تحلیلگران معتقدند که آنچه در این تصاویر می‌بینیم، ترکیبی از باور واقعی، سال‌ها تبلیغات حکومتی، فشار اجتماعی، ترس از حکومت و گاهی هم منافع شخصی است.
شاید مهم‌ترین درس این تصاویر این باشد که وقتی دسترسی مردم به اطلاعات آزاد محدود شود و فقط یک روایت سال‌ها تکرار شود، همان روایت می‌تواند واقعیت ذهن بسیاری از افراد را شکل دهد.
تاریخ بارها نشان داده که پرستش شخصیت، فقط به یک کشور محدود نیست؛ هر جامعه‌ای که آزادی بیان، نقد و گردش آزاد اطلاعات را از دست بدهد، ممکن است در همان مسیر قدم بگذارد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/67293" target="_blank">📅 20:12 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67292">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/648e669177.mp4?token=AGri60sStHj6202CfQJwAylIuTInxuUzeIqKhWcSQxKsJR8H77-dOTOT32a2gGUxzwI8QazIwhmZFX8XPHlTXjl9thPTnnpAs1Tq7z_izFyNqHFCMFneepCrxTM8bbSbhUBAQe451SCPJHB4YoWMxw1LAZyHc42BMZt6JjXEzOb1MdYDF2YXTI68KcOArRqAnEAQE20aiFhAeZHGpVyBAAaVOChzpDNFbLPh6kh1hCgiFH0bqYldjeU4RMet8qxgIuupZOgaOAnEcJlan2q3ZNx9spsvolD9jmzemzB5p5MlcAS3FT5omECbgLJIPRXl5VU_NyZop0bfbW0tpFXAvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/648e669177.mp4?token=AGri60sStHj6202CfQJwAylIuTInxuUzeIqKhWcSQxKsJR8H77-dOTOT32a2gGUxzwI8QazIwhmZFX8XPHlTXjl9thPTnnpAs1Tq7z_izFyNqHFCMFneepCrxTM8bbSbhUBAQe451SCPJHB4YoWMxw1LAZyHc42BMZt6JjXEzOb1MdYDF2YXTI68KcOArRqAnEAQE20aiFhAeZHGpVyBAAaVOChzpDNFbLPh6kh1hCgiFH0bqYldjeU4RMet8qxgIuupZOgaOAnEcJlan2q3ZNx9spsvolD9jmzemzB5p5MlcAS3FT5omECbgLJIPRXl5VU_NyZop0bfbW0tpFXAvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
▶️
داده‌های تارنمای ردیابی پرواز «فلایت رادار ۲۴» (Flightradar24) نشان می‌دهد که یک خلبان آمریکایی در آستانه چهارم ژوئیه، روز استقلال ایالات متحده، با طراحی مسیر پرواز خود بر فراز ایالت اوهایو، عبارت «USA 250th» را در کنار نقشه جغرافیایی آمریکا ترسیم کرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/67292" target="_blank">📅 20:04 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67291">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
🚨
خبرگزاری مهر : مراجع تقلیدی که‌ قراره نمازِ علی خامنه‌ای رو بخونن که همچنان خبری از مجتبی خامنه‌ای نیست!
تهران : سبحانی
قم : عبدالله جوادی آملی
مشهد : نوری همدانی
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/67291" target="_blank">📅 19:16 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67290">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4cc795d411.mp4?token=vk7-sgDwg2Aeqh8BuDaPmI3_zLsXTgKgtgbUldkjf85ldFMVaDPkVqnGy1_aRoF820Dvs4ql0YZH6-ub2g-q_4ZtixC4t6Wm1EP5WpjtTP8laQ7O8qVvqzUWfczYL8HxDvNL-3nE2zczLNTcMsxAB0D_6qwFwaBoEsm1cqWFl0uG-dZwJujvK6xla0v7lw6SG-ZQT0eES1-xEihZFUCRicPcob88E1fPjnnfche9wKshfycbwHlfIAbeoRh9GYg7RZpDiTt4wb_9bfP09v36d4AsaoGNK4LlmWio-g0NMCh2KxPZJT1dYhk_MsurbA3tQIlPDOt3OYfQ75WefD5f1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4cc795d411.mp4?token=vk7-sgDwg2Aeqh8BuDaPmI3_zLsXTgKgtgbUldkjf85ldFMVaDPkVqnGy1_aRoF820Dvs4ql0YZH6-ub2g-q_4ZtixC4t6Wm1EP5WpjtTP8laQ7O8qVvqzUWfczYL8HxDvNL-3nE2zczLNTcMsxAB0D_6qwFwaBoEsm1cqWFl0uG-dZwJujvK6xla0v7lw6SG-ZQT0eES1-xEihZFUCRicPcob88E1fPjnnfche9wKshfycbwHlfIAbeoRh9GYg7RZpDiTt4wb_9bfP09v36d4AsaoGNK4LlmWio-g0NMCh2KxPZJT1dYhk_MsurbA3tQIlPDOt3OYfQ75WefD5f1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
یحیی رحیم صفوی:
بین ایران و اسراییل جنگ موجودیتی است یکی باید بماند
.
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/67290" target="_blank">📅 18:17 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67289">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F0d5u9qKLYIGqq6bsd5U42ylmMgfkzNXCf1h9o3H3hqhg-MEKPkP1_cHABt1nyo3y9_GKfI-PxnAOilw7HWDjVsveuFRdzWzBaniCaFJMjcjndy48KooVUJdWc9_toHXj4Dv6__GHDmvP8W0RujAIPxt8IcwDhTcwKUK-OGnhF7KFptCf2K66Y6O2GqcsgStXmzbKjGpx7IHujoxmVT5GzRIGQXhnoI1BmXlPLvO6owVvS4-dBqi8lKGoLakn8ik83KkXhHOP-aV7AutbBtD7CKeyWVUOlL_TngYSE67MR_DVDfDWgJffuWxSq7nEiGPC7Y84zdEz_kxGSeOqGyvRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
شاهزاده رضا پهلوی:
🔴
خطاب به نمایندگان خارجی حاضر در تهران برای سوگواری علی خامنه‌ای، دیکتاتور فقید ایران: ایران در سوگ او نیست.
🔴
ایران سوگوار بیش از ۴۰ هزار فرزند خود است که در روزهای ۸ و ۹ ژانویه به دست خامنه‌ای، قالیباف و ماشین سرکوب آن‌ها به خاک و خون کشیده شدند.
🔴
رژیم مبالغ هنگفتی از ثروت مردم ایران را صرف برپایی این نمایش تبلیغاتی می‌کند، حال آنکه حتی یک رهبر دموکراتیک نیز در آن حضور نیافت.
🔴
آنچه امروز می‌بینید، ملتی نیست که در سوگ حاکم خود نشسته باشد؛
🔴
بلکه ملتی است سرشار از خشم برحق، و همین خشم و دلیریِ قهرمانانه، بساطِ باقی‌مانده‌ی این رژیم جنایتکار را درهم خواهد پیچید.
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/67289" target="_blank">📅 17:54 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67288">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20335e95a0.mp4?token=W1_BGLjI0SzLxq0i3-sRfYMVZ90eRzxIRKYnCLm1fSjmbApEudbNSVDfUFGXchf2UWsd3VCR3kUw7sZbYVg7W338vu8Zxy2ClV6RRjqOeSrjZSVVMpjmNTh6ckMPASBZYtuoc6yVddeDZPimYS_KtI-vinGywUBiJV1iX5Ox2MxKL6fun0z5_q90wpd_bGC-ytcG3aJOGmzkOeTj1p2ZCfaDZCT7xwIw7vtBJKp7l2U6BMw6QNrWmjdKYFgbxpVJ23tf6Pe74sWl9VGM4jEi6IJYXK02oH9oNXQdsE67cSlLgMglHHmvbwrtzMbhzD1klPfNcPsbe1F8oueIvlKevA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20335e95a0.mp4?token=W1_BGLjI0SzLxq0i3-sRfYMVZ90eRzxIRKYnCLm1fSjmbApEudbNSVDfUFGXchf2UWsd3VCR3kUw7sZbYVg7W338vu8Zxy2ClV6RRjqOeSrjZSVVMpjmNTh6ckMPASBZYtuoc6yVddeDZPimYS_KtI-vinGywUBiJV1iX5Ox2MxKL6fun0z5_q90wpd_bGC-ytcG3aJOGmzkOeTj1p2ZCfaDZCT7xwIw7vtBJKp7l2U6BMw6QNrWmjdKYFgbxpVJ23tf6Pe74sWl9VGM4jEi6IJYXK02oH9oNXQdsE67cSlLgMglHHmvbwrtzMbhzD1klPfNcPsbe1F8oueIvlKevA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
روایتی تصویری از شاهنشاه آریامهر محمدرضا شاه پهلوی:
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/67288" target="_blank">📅 17:26 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67287">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">‼️
ادعای نیویورک تایمز به نقل از ۴ مقام ایرانی:
پزشکیان به مجتبی اطلاع داده بود که در صورت عدم توافق، از سمت خود استعفا خواهد داد.
نامه‌ای از رئیس بانک مرکزی ایران باعث شد مجتبی با یادداشت تفاهم موافقت کند.
پزشکیان، قبل از امضای توافق، به مجتبی خامنه‌ای اطلاع داد که محاصره دریایی، ایران را فلج خواهد کرد
.
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/67287" target="_blank">📅 16:55 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67286">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c90b7a34aa.mp4?token=UuYS0-n9N3XsnPYtpWzT0iOOjfIUwt-YZJMCG_Y5Yz2Re14DNct5UcOmBxlF36zqkufr5V19WQu7U71rMdNbWlNTbonvr_GsOTVsJSAE186a-2NaHlTpG4kJ6fSjKWDg6ozGNRezm44Y3jpueLcO4DCSpOiRwrtCUvOPtoEEriHN9Uapdl32YlTGb2eW7G7wXB4VeuTe2WUvNPMlyuPNawxisVLz_zKYTbL9D9A474er8HLlVxkY0o45brnOUuT0wMTEj7tiVsKYeZ0pQ8Y9083wmtqulX48X_jDsrdrBj2gdhCd-Owfd_6zJQp2zCtCyk57RL2Nvin19eajrH3gTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c90b7a34aa.mp4?token=UuYS0-n9N3XsnPYtpWzT0iOOjfIUwt-YZJMCG_Y5Yz2Re14DNct5UcOmBxlF36zqkufr5V19WQu7U71rMdNbWlNTbonvr_GsOTVsJSAE186a-2NaHlTpG4kJ6fSjKWDg6ozGNRezm44Y3jpueLcO4DCSpOiRwrtCUvOPtoEEriHN9Uapdl32YlTGb2eW7G7wXB4VeuTe2WUvNPMlyuPNawxisVLz_zKYTbL9D9A474er8HLlVxkY0o45brnOUuT0wMTEj7tiVsKYeZ0pQ8Y9083wmtqulX48X_jDsrdrBj2gdhCd-Owfd_6zJQp2zCtCyk57RL2Nvin19eajrH3gTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
شعارهای عجیب در تجمع شبانه علیه قالیباف و آمریکا
😂
😐
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/67286" target="_blank">📅 16:35 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67285">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/441130dd0d.mp4?token=avQz87U48KsfDGLPRHw7w6I6MGlnOoy39JQkauncEye3kSZiF-pg6TAAKjZPtTi5x8MS0R3b5b6-GA7F8uAGXgb5AgY2LRki4b-vq9JmvitH1N8iFqbw4uzmytvSTU59HtF7e2iaQhot7uzqEEvbu9PUXZ7acZTKRaFf0jNkawKjwr3SEuzduX6GhDbIJ-MWYYOW44gUw6kRmwAzCWBqfPYGkIruucTZKcavSKGWZSKe8Un7whldvDTJS3Aj10yGqf2cszargkThxncRQBAP2XLMFH8gYXRjvKOcMshUZ2IP-iOCJ2FsG_rl52Sm6ecg3UfFZtHq8ddeHty9vKzhog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/441130dd0d.mp4?token=avQz87U48KsfDGLPRHw7w6I6MGlnOoy39JQkauncEye3kSZiF-pg6TAAKjZPtTi5x8MS0R3b5b6-GA7F8uAGXgb5AgY2LRki4b-vq9JmvitH1N8iFqbw4uzmytvSTU59HtF7e2iaQhot7uzqEEvbu9PUXZ7acZTKRaFf0jNkawKjwr3SEuzduX6GhDbIJ-MWYYOW44gUw6kRmwAzCWBqfPYGkIruucTZKcavSKGWZSKe8Un7whldvDTJS3Aj10yGqf2cszargkThxncRQBAP2XLMFH8gYXRjvKOcMshUZ2IP-iOCJ2FsG_rl52Sm6ecg3UfFZtHq8ddeHty9vKzhog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
😐
ویدیوی این بسیجی که در مراسم تشییع علی خامنه‌ای وایرال شد!
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/67285" target="_blank">📅 16:32 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67284">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/67284" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/67284" target="_blank">📅 16:31 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67283">
<div class="tg-post-header">📌 پیام #54</div>
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
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/67283" target="_blank">📅 16:31 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67282">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XYOM5aBM_CGXS38LL885gd78EowPKvkacU8u7MUxUUGp0UB9XaKr5l4BgY_YoJkJe37NwMQmyQRV6O63FblbqBnrUgknARYBeIchKrBwilgZMcwDmccte9gqElAvUgE7JS4_IDx6oDyRgbiCMuRZd45PMiWvnuWu8FkVqQT1XXLutPpBhTZ5yAMAy9joN0ZrPec3cvNMk5y_FlzfTqOPvCu2pgORwtdh-rCGSTKEHNLmiE6J3cJdXL-OSwt-ueIrxW9dgHBbDMkk6ZLP8gmOAFguX4RnvePSf_XtK6G1-DGBWJgNQibW4TO50mUvPEXvuSooXVq8dHCPFHv-TCkoPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
علی عظمایی فرمانده جدید نیرو دریایی سپاه پاسداران
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/67282" target="_blank">📅 16:27 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67281">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
با تصمیم هیئت دولت، کل کشور فردا تعطیل شد
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/67281" target="_blank">📅 16:26 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67280">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Oh3XsHMq1MmOcouR_-ONpZ2x5KXK4rBzsHjTVN1_mgoC-WQgqxlFyW5EIhK1xagVgc_xPLgXhm1nXWVNVlY9T89vjj7Zz2KkOaPn8hQAkPMdeTmCN7xklsdLcnzXxGGGOZWO2OGwv0LO7hMqqIRyMp7M7YZCJck9RshBwQAesrdc54g35YiMJtfhEVeNCfJZsj1HbAFwBovUcJ6_U1KJR00NHHqNOBDm9xzHcKp7YX7WcKz3WX7aMnALijBvaAEcPtPzicIe3LyYQ_InUzxSAZwFl4tMrciyk0_CL8iJL0M0miWzQ4znzgHbp7TzEBfRts5Gkh2P6IY3EiSitOqcYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
نیویورک تایمز به نقل از منابع آگاه:
🔴
مجتبی خامنه‌ای به مقام‌ها گفته است می‌خواهد در مراسم تدفین پدرش در حرم امام هشتم شیعیان در مشهد، که برای ۱۸ تیر برنامه‌ریزی شده، شرکت کند و نماز میت را بخواند.
🔴
مقام‌های امنیتی تاکنون با حضور مجتبی خامنه‌ای در این مراسم مخالفت کرده‌اند، زیرا نگران هستند اسرائیل از این مراسم برای کشتن او یا ردیابی محل اختفایش استفاده کند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/67280" target="_blank">📅 15:59 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67277">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d9sgKIGdO04Z0lyExzEGOFH6k9AHxQ0S64F41jPnjUsw8Lk52Gtw5xxHwk7l9SFkjFoTDcOA2Vhkxcewghi3se_r4wGcR8QDKSivYODdAsd11eqDZRnEDwGlSChju9t-23_X6hJWY0B2oEEWpzuw4HH49vczwJcf9SLMB77GDHHFSeri8tXkal9ubwGL9ddayrFl7lvbt-qW_-4Y0kB4oXu-mT-FJzzWnf8Mtu6AWsvwAVWKnx-o9Izox3vqpb6wPxUJN0812KUdEiU2NxML1ZEk-US8HMB_yd4mNnUFV5EoAp0pUzvlw8xrW0hPtsMJc002RsQ56uRRbCxf_DnZ0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UOxdu7wa-8LquomtgwhP_FiBVEkk76zMspBPIupMOBm9fPCcLdwPCKxUvjtVg_jTdGYjNqi6iXefRulnKDMb0Hq87Vn_pgUQB1K0hH0lucCZosRtnDixiaj0q7imwrcDsyYu4iXdEizXRnTqPgwT1yI_R77g2sAHmCL1VecQOQcYFx3R6SXDKFPrgyOujqL6EUYlX8Uhj-Qr75XVSjPoisOx9vtGWoJn4kJ73uZ_ZDO4Bhy9DqVCty_fQNrveUDB6C0hR_SdNF2mKL9iCdpXwNHibiDAjipm9CTnD_f8ZXSWtS1fy7p-DxySnUppq2zHbwXbK2_cPssOVEjj4DBQJg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/502fac7d76.mp4?token=J4NNIk4BBrTypVOl1JZVvXeDjQWTUO55XLIgP3AGCrqWYr_0HSpLkyWPSsjdqEuL3mk4rnZ6SU-tswKR1E5QoavlhGyi7L-Oonros6KFy_NItZ1KhasuX3XFMoSnBb3i5k81nYF_DcTMxtx5aKYGXkXNdeT3JhgQ0SP-dLAGFUvkl8UxyKzKScgB66_4jUGOIkiE1lrL4VOiiBZQ57UWnMMBSErFJkxTZ7sAu_g2TXuAm-zql1bPRzqsF-tAk_FpKdzHKrSFv-7kH-gSD89ZB9H9jgtq1mXtnF4FZFo5u5tkf20xCiNjgRIYcK_cxnykRCifxuh1wCpvlyfpSwTLnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/502fac7d76.mp4?token=J4NNIk4BBrTypVOl1JZVvXeDjQWTUO55XLIgP3AGCrqWYr_0HSpLkyWPSsjdqEuL3mk4rnZ6SU-tswKR1E5QoavlhGyi7L-Oonros6KFy_NItZ1KhasuX3XFMoSnBb3i5k81nYF_DcTMxtx5aKYGXkXNdeT3JhgQ0SP-dLAGFUvkl8UxyKzKScgB66_4jUGOIkiE1lrL4VOiiBZQ57UWnMMBSErFJkxTZ7sAu_g2TXuAm-zql1bPRzqsF-tAk_FpKdzHKrSFv-7kH-gSD89ZB9H9jgtq1mXtnF4FZFo5u5tkf20xCiNjgRIYcK_cxnykRCifxuh1wCpvlyfpSwTLnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دیشب، برخورد یک صاعقه با برج وان ورلد ترید سنتر در نیویورک
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/67277" target="_blank">📅 15:37 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67276">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fmmnCwcclv46K5amxwewZ_rB1qomL-GI_0Cb96l31dHkuJfmDzUal8fWfsykp1dzgqlWhms3t7a14C-Ay6puI1kGWMXbCpnOq_XcIDENM23_hO-z9gLvd_r1fVAACoz5plFe5aYO8f3Wk1J4HNDHzIb3FwPHJI6AWTDwJ_e6YYaF5oEG9ssgvKhtjW9NDv2-w6ItV9dQ8HOFL7MhwqvSGYNftzRkapxHogZnEVF92oPnqmjWgoPrAYSW7tZVbiQi-Nn81CVdTj-N3-lEI7R2Mare4amKoB7YKF2EfXvVEjQ9q1HDL0B5Qs4PNkT1HlL3SYVGdCD0fqcsyWPdV-H5FQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مدودوف معاون رئیس شورای امنیت روسیه:
🔴
ج ا به‌جای سلاح هسته‌ای، به سلاح دیگری دست یافته که دست‌کمی از سلاح هسته‌ای ندارد: تنگه هرمز.
🔴
بحث‌ها اکنون بر سر این است که در آینده، درباره نحوه کارکرد و وضعیت این تنگه چه توافق‌هایی حاصل خواهد شد.
🔴
مقام‌های ایرانی همچنین یک «سلاح ترمونوکلئار» دیگر هم در اختیار دارند: تنگه باب‌المندب.
🔴
اگر این گذرگاه بسته شود، همه محموله‌های نفتی و سایر مسیرهای حمل‌ونقل عملاً قفل خواهند شد
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/67276" target="_blank">📅 15:01 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67275">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fl8hV5oIn_7tnWqOEqsw0SNRHOSXs7LbM2Z8YkxRmfdRBaL-yWSfXDlC0hlldVQ2HqPd3dObCX5A-9-vfeo2_XZXaTCDeJiH6UzHhCCxrjJ4V_f3u8sNl1PtsxW6bUTSgXAqa3Z29_tOSfGoqyT-5kif-DC-VVCcxlu8HRuWEs_m9f0CHimgA1V6TM-EjFuqMZmY0zXQbzSqXdS4Lg_3N44FbpTAgBgsIVzpUb25eqVTBvz8XXBVMulWvvOnMXRHUInThEjmGyh_UcebC_6dQfJBIORTSBC5sVHwBou-qftmFAIOwNAB3l4K1OTDCqfd7xFEVCwL75jrEPTgraw7pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
احتمال مجازی‌شدن مدارس و دانشگاه‌ها در سال جاری!
🔴
میزان کسری گاز به حدود ۶۳۰ میلیون مترمکعب رسیده.
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/67275" target="_blank">📅 14:18 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67274">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qwsG74riU-WlJ47iu0xYhxguSzIvsudt29apNUMM3hkBq8k02ekEP78ipeB4R9w4pbZ0aTefedU2rqSPF_jydgkOCNUe7_hG5ePenvlWNsabTqB5gP53DKBajiI37xKCWCSpVYsluexdFdrSR-L4T5LUR9q_CbpxC5r7enCtnbZlewa-vLTtWf2OJwRFJyQMKngUAu_Oe6N71dOXGfywt7UGMwmRaLXv-68yZ5fw7oXPZTO89zXV_LAnUC0rocKTbCh10w4uekKHlaG2ioczA1Dy8qY-NVwBh96wTebapGHg-Yb2zk_LorDL4FDlBqyGDOZyDTm5j-O9euHLKV06Fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
برافراشتن پرچم «ترامپ را بکشید» در مراسم وداع با جسد علی خامنه‌ای:
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/67274" target="_blank">📅 13:57 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67273">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2883f7592b.mp4?token=c1S2iglSAw2stIzUY5INk3QjetcAAsSVh4pMH1iPZfUN15xovcd7KxVjbC8Bj05nfW5hpbYkFV79hl7gZUv7-iJShrsjyM18ZQ87aeaG3nwDc7sV1wUr57d3ZTnJsmcKEwOt7o4j05nejriK0PAPc-8Z6EsjZpcXiLhrVE99FMfb6hk8Om1YMgTk31YU1Pn2SROqHF7fO9zVrWo7RCLX4VRvT0juwZqkWG1wmMO521gZzDZWWu6JixVflEdm2YfT_fph4X1JXZJnx8KZkT4915dbzUzM9yOvtl16tTQEiDoVaO5y196YV-QfF4zbmWWqs8MDy5eC4Jmxp_ScKikWfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2883f7592b.mp4?token=c1S2iglSAw2stIzUY5INk3QjetcAAsSVh4pMH1iPZfUN15xovcd7KxVjbC8Bj05nfW5hpbYkFV79hl7gZUv7-iJShrsjyM18ZQ87aeaG3nwDc7sV1wUr57d3ZTnJsmcKEwOt7o4j05nejriK0PAPc-8Z6EsjZpcXiLhrVE99FMfb6hk8Om1YMgTk31YU1Pn2SROqHF7fO9zVrWo7RCLX4VRvT0juwZqkWG1wmMO521gZzDZWWu6JixVflEdm2YfT_fph4X1JXZJnx8KZkT4915dbzUzM9yOvtl16tTQEiDoVaO5y196YV-QfF4zbmWWqs8MDy5eC4Jmxp_ScKikWfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
واکنش نکیر و منکر بعد از ۱۲۰ روز
😂
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/67273" target="_blank">📅 13:17 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67272">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gMiz2X0vr7_g63QhnOP2R5tchK-MG8I87xzAhx37I1s1Y-HzEwfc20VQLLwwCUq3PX9GT1AfiPmmp_vB88ZxvD_0_o8-XCTH7hHiPdM9xvWrW_TOEvnkGrdYVdNbu7puDTQHWkH_6mBNOHC5PmqVK5co-tsf9qEeG2SNgkW5CUzZquZcBbkIqmTVqp2l8YFDwxlqJStOnZ2gkrYAjFF0at39SeK87vAUkU__1CJt3SCckkAzG48jUwe0PLAUpfY-QGWrx67XWcEF88YDZceg0OS12v7GZwp_E2vS-g8swaCtiDvLfNgyyRrJEpEWYY9JGAg87qzlYG7UdtgSsT5YyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
التماس رسانه حکومتی در ایتا برای حضور در مراسم ؛ جمعیت کم است...
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/67272" target="_blank">📅 12:23 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67271">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc8da4a29b.mp4?token=YjqHtud5Oxg24Iqrjjz8KCArApG48QhysjgwiKX4QO2zwhwY5z0EIS5cfzVSMHPnsxhjl4LhplGSupZkTFs58vUDV_5B5uOlmgfCVI1_HwI2LLRpaqXtC7q5gBhfXXeYEtqQWEYsul3E0v7FwkFq4YBtps_QSzaLhdLBXkJZhgR_PAtPMCiduBBlyj2vlEQwOJ-1paBxhsoujuzq7QGLPp_hNkOb6laFN-wy9WuUQfA79tF-xJcZExRA0Rv_iMhvRsRaNv5jyQYozP4t5gVj5I7LHmLarvTecedY1j4ZgpxTVpI3VO3aMmkvUw4rOz4I4UHkFRSsoDHgO-DMUz8cOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc8da4a29b.mp4?token=YjqHtud5Oxg24Iqrjjz8KCArApG48QhysjgwiKX4QO2zwhwY5z0EIS5cfzVSMHPnsxhjl4LhplGSupZkTFs58vUDV_5B5uOlmgfCVI1_HwI2LLRpaqXtC7q5gBhfXXeYEtqQWEYsul3E0v7FwkFq4YBtps_QSzaLhdLBXkJZhgR_PAtPMCiduBBlyj2vlEQwOJ-1paBxhsoujuzq7QGLPp_hNkOb6laFN-wy9WuUQfA79tF-xJcZExRA0Rv_iMhvRsRaNv5jyQYozP4t5gVj5I7LHmLarvTecedY1j4ZgpxTVpI3VO3aMmkvUw4rOz4I4UHkFRSsoDHgO-DMUz8cOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
ویدیو ای
از بمباران بیت رهبری9 اسفند 1404
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/67271" target="_blank">📅 11:51 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67270">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ccea9f87ad.mp4?token=PKPpE3hCJLJOkA_-lpxzPLCKYobph6cC68u_ZFFRGhF1UmAGMMt5K65b02Vw7OgVvEqJieFwFDRG3ATeABkluRAt4pLzV42xqPRNtztzkU0r7Cq_mNs74b5H4LnuZP26o2FQ2GILxVcaketHGGRCN6zY_8lnE9W5j1-jtsq4_LNgtExcZm9sDM8Wwy4sYv_ZuJoUaVsBeg_YWWHMsFGhuTxQ1sRMV3URhWXQ1lFHlk-dafAjCCy5gxl-7NCFySnonpsqWRMY8wXZIp6w1qdBBpW5thVAahLPzprRxtloJsmHAQ5KAgoQd5K17miulzqSBa-UiaoFS4gHkoP6FIjh1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ccea9f87ad.mp4?token=PKPpE3hCJLJOkA_-lpxzPLCKYobph6cC68u_ZFFRGhF1UmAGMMt5K65b02Vw7OgVvEqJieFwFDRG3ATeABkluRAt4pLzV42xqPRNtztzkU0r7Cq_mNs74b5H4LnuZP26o2FQ2GILxVcaketHGGRCN6zY_8lnE9W5j1-jtsq4_LNgtExcZm9sDM8Wwy4sYv_ZuJoUaVsBeg_YWWHMsFGhuTxQ1sRMV3URhWXQ1lFHlk-dafAjCCy5gxl-7NCFySnonpsqWRMY8wXZIp6w1qdBBpW5thVAahLPzprRxtloJsmHAQ5KAgoQd5K17miulzqSBa-UiaoFS4gHkoP6FIjh1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سر دادن شعار مرگ بر آمریکا در مراسم وداع با جنازه علی خامنه‌ای
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/67270" target="_blank">📅 11:41 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67268">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0d436c597.mp4?token=q7ylCeozR_gIz8SP49dFRyb5PVAFoezgRx3BL4K92MRsOXiUo1xYWHr726A10D6PMP80-0vbgqVs0cx9d5DfdO0i4xOuEWQEuJjLPJhfhkvF2sOpzOwJls4_LaAmYjpcbY2gOZ2TUabyI7oaz0HX341i5j_8eT_f7_Po-vHCQ_kQQJ3iVj85c01rG9VRcYDKF2t_I6os0j0LDD1UAXkM9cHHYbGvqUd-aesA3QNXO1fU7Zcl8VKE8u9k6OUTe3lxRi5tW1E0gCwcFUcao391_F_3GOVBFnhyFPL20maZYontajvmBdgKVq4Y5fAF_hm3fgxlmnyQXBv5suR0-IJJdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0d436c597.mp4?token=q7ylCeozR_gIz8SP49dFRyb5PVAFoezgRx3BL4K92MRsOXiUo1xYWHr726A10D6PMP80-0vbgqVs0cx9d5DfdO0i4xOuEWQEuJjLPJhfhkvF2sOpzOwJls4_LaAmYjpcbY2gOZ2TUabyI7oaz0HX341i5j_8eT_f7_Po-vHCQ_kQQJ3iVj85c01rG9VRcYDKF2t_I6os0j0LDD1UAXkM9cHHYbGvqUd-aesA3QNXO1fU7Zcl8VKE8u9k6OUTe3lxRi5tW1E0gCwcFUcao391_F_3GOVBFnhyFPL20maZYontajvmBdgKVq4Y5fAF_hm3fgxlmnyQXBv5suR0-IJJdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیو ای از پرواز جنگنده‌های اسرائیلی بر فراز بیروت در مراسم تشییع جنازه حسن نصرالله دبیر کل حزب‌الله لبنان بین سالهای1992تا2024!
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/67268" target="_blank">📅 11:02 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67267">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64adeed1d2.mp4?token=UL76k0VWN5oOTlJeYtxLVRcPYzG3vXbsbTN0WnkFq8_eT-UFyTXj68TzAF2gdRRXyqFQLF2j611MYaxbZtTzQupufR-RrSgj5F1KhnU2waXupG1vMY0smTPVitgN-TQzsyzA7kH7kX_7Y1pH7TB4n_baR9NUC4VYQ5-Ip-9EYp5t8JJkqOEaXBgQ1IdPJauF_c3kDv4K6XmoAao8Vh2T50qifCBPLwGTFY7ayt5gqtmxPG7LuIHRB_1Pgf-_AyS-RsKOE-THN9ENiBiv7l6T1qnyWpE7jgIvam9NCjp_h7VjrdFdqAT7rYLqu8URyLl39M9_xQFCNOwiLqanfKNr1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64adeed1d2.mp4?token=UL76k0VWN5oOTlJeYtxLVRcPYzG3vXbsbTN0WnkFq8_eT-UFyTXj68TzAF2gdRRXyqFQLF2j611MYaxbZtTzQupufR-RrSgj5F1KhnU2waXupG1vMY0smTPVitgN-TQzsyzA7kH7kX_7Y1pH7TB4n_baR9NUC4VYQ5-Ip-9EYp5t8JJkqOEaXBgQ1IdPJauF_c3kDv4K6XmoAao8Vh2T50qifCBPLwGTFY7ayt5gqtmxPG7LuIHRB_1Pgf-_AyS-RsKOE-THN9ENiBiv7l6T1qnyWpE7jgIvam9NCjp_h7VjrdFdqAT7rYLqu8URyLl39M9_xQFCNOwiLqanfKNr1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مایک والتز نماینده ایالات متحده خطاب به نماینده جمهوری اسلامی در شورای امنیت سازمان ملل :
🔴
اینجا تهران نیست که بخواهید همه را خفه کنید ، اینجا آمریکا است ، اینجا سازمان ملل است. این اسناد حملات شما به مناطق مسکونی بحرین است که دروغ نمی‌گویند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/67267" target="_blank">📅 10:34 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67266">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b206a5500f.mp4?token=YCnBR8idY_JPjPaDhQ9iyak-S-6X9yEiWMAcQIi77CyNLA59jvXgIia1nOBFMw61y3p95e7DHQ4WQgN791T51ey_3hemOPjTQG8lgnUTVGUXkPyemWFM4j0yAff7C9SA1jdtR1KCTz-qYhxGzoU7_0acXxJSI5l_eDPZxdHAArxZt8XWQi7supdDqHRonFPn6abv7x2tEqk2TTwY2wL0Irw2iPCEGOuxHuVUaESjHI_DfB9xvi0VnF-s2fVizDFNb4X6sqLKfDj5GRqi6qgF8jF4i_nRBGF8Aw5R1fO5rYFloD2ZHXVD0Up-MInP_ShOin2ZKye-0ZMGP3AjdQvMzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b206a5500f.mp4?token=YCnBR8idY_JPjPaDhQ9iyak-S-6X9yEiWMAcQIi77CyNLA59jvXgIia1nOBFMw61y3p95e7DHQ4WQgN791T51ey_3hemOPjTQG8lgnUTVGUXkPyemWFM4j0yAff7C9SA1jdtR1KCTz-qYhxGzoU7_0acXxJSI5l_eDPZxdHAArxZt8XWQi7supdDqHRonFPn6abv7x2tEqk2TTwY2wL0Irw2iPCEGOuxHuVUaESjHI_DfB9xvi0VnF-s2fVizDFNb4X6sqLKfDj5GRqi6qgF8jF4i_nRBGF8Aw5R1fO5rYFloD2ZHXVD0Up-MInP_ShOin2ZKye-0ZMGP3AjdQvMzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚬
وقتی تو ایران میخوای پیشرفت کنی
واکنش آخوندا:
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/67266" target="_blank">📅 10:03 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67265">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b88ddeb40.mp4?token=E9dh4zQQe6DOwz2wMLt2TfZwEukOaAHGy1T7w_gyFEtXoChFg5Wyc_vYSWiFVZdyYvEOUgGg12m5IbrHOBjzLQJt113VbVUHCh1OmfTXELUurQT94ZJfWLxorrgYEsJKsc2_PE96wF4ZTdWvcPIhPRgBuQks7ZOtr-203nDzOhvo2FGGAdkjLSSASgWT1cd72NYMMX1qUj1beP86jIbomqw179V0MQKikeKrHEEDPddqjVDiS-LVmQa68BkInm5MCpLQyhs94ormQ0GogZA0CPQIy4NWGh0T6pXjr7sL7iclvdlteGj3PFZMyGwVVENqtAf5r8SGD8x83hIWDmFImQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b88ddeb40.mp4?token=E9dh4zQQe6DOwz2wMLt2TfZwEukOaAHGy1T7w_gyFEtXoChFg5Wyc_vYSWiFVZdyYvEOUgGg12m5IbrHOBjzLQJt113VbVUHCh1OmfTXELUurQT94ZJfWLxorrgYEsJKsc2_PE96wF4ZTdWvcPIhPRgBuQks7ZOtr-203nDzOhvo2FGGAdkjLSSASgWT1cd72NYMMX1qUj1beP86jIbomqw179V0MQKikeKrHEEDPddqjVDiS-LVmQa68BkInm5MCpLQyhs94ormQ0GogZA0CPQIy4NWGh0T6pXjr7sL7iclvdlteGj3PFZMyGwVVENqtAf5r8SGD8x83hIWDmFImQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ درباره ایران:
ما ایران را حسابی درهم کوبیدیم. آن‌ها برای توافق لحظه‌شماری می‌کنند؛ به‌شدت خواهان توافق هستند. ما به خاطر یک مراسم خاکسپاری، یک هفته به آن‌ها مهلت دادیم، چون آدم‌های خوبی هستیم. واقعیت همین است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/67265" target="_blank">📅 09:46 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67264">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb8124f389.mp4?token=UZKJIbFli5qYwbIGRomqUZrG8_3UNdlVCvdi7Jdgd5EabuY0DcKxTCetlTbnETQ11Du4WFKDVtrsablJPqeKx6H5NXnyit6r1l0xPw6-ymAhzpTOpe2bAPN7DttYsH0RW1by1v_5uvnLgvT71eUFNdvctZr8vw9VcAuRKsGoKc6wlEhJEAp0h71P5MHRPeVhRiFW6GhAj1RYwVQJz_JfzmsP7Fa26xY64DSETr1Qau-NXa_S18VSeWQwU-LR63uOZp0FSyBCAr9c7liy0gjxbijVYIWqN61Z0HXnDgdckuWcwZ3sn__9srl5zbPVbNJKN-CwfGLtPgKXowSTBCP8Zg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb8124f389.mp4?token=UZKJIbFli5qYwbIGRomqUZrG8_3UNdlVCvdi7Jdgd5EabuY0DcKxTCetlTbnETQ11Du4WFKDVtrsablJPqeKx6H5NXnyit6r1l0xPw6-ymAhzpTOpe2bAPN7DttYsH0RW1by1v_5uvnLgvT71eUFNdvctZr8vw9VcAuRKsGoKc6wlEhJEAp0h71P5MHRPeVhRiFW6GhAj1RYwVQJz_JfzmsP7Fa26xY64DSETr1Qau-NXa_S18VSeWQwU-LR63uOZp0FSyBCAr9c7liy0gjxbijVYIWqN61Z0HXnDgdckuWcwZ3sn__9srl5zbPVbNJKN-CwfGLtPgKXowSTBCP8Zg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
زنده یاد مانوک خدابخشیان:
آمریکا یکی از داکترین هاش برای به زانو درآوردن کشور مقابل اینه که هزینه ملیشون رو بالا میبره مانند شوروی که همینجور کمرش رو شکوند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/67264" target="_blank">📅 09:35 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67263">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">⏸
مستند کامل و 46دقیقه ای شبکه 14 اسرائیل به نام از «چشمان جاسوسی در تهران»:
این مستند جنجالی دیشب از شبکه 14 اسرائیل پخش شد.این نسخه زیر نویس فارسی دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/67263" target="_blank">📅 09:05 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67262">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/beLZa8dVCCuIiQK1jR5-2s8_XsF26xmmapNGB_U4x-7gC54LnmpHg4zXpJBXcLyb7Xw0QU92sKUKQh3rIDNDA74j2mO2vapzUwUinhr1d0Gm2PS8VNwQp1f2dOg158tXkLegVWTtOOheSCFSTqQCkMxAIRrRr1A6P_LMzxhHG2PxvBMHzKOSk_qVR168b7sxD1XiUt9VahJMDXr0rZ7n_Q045uMbB05y1j9rFIapm4t_scZMo9D9Oi_LQZDyybSCylHrayJ8Dc6u5BvtB1Szb2Q6ZFk5pnG2CzeUm1846sVsqi4RfBUadHgaDxrQ32WoehCiKINQC0JI21_QWxk2Kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
🔥
🔥
انقلابی در صنعت هوش مصنوعی
🔥
🔥
🔥
🔴
میدونی هوش مصنوعی ترند دنیاست و اینده ی اقتصاده ولی بلد نیستی ازش استفاده کنی و درامدزایی کنی؟
هوش مصنوعی TimeTrade این مشکلو حل کرده
✅
هرکسی با هرمقدار علمو دانشی میتونه ازین هوش مصنوعی استفاده کنه و با سیستم auto trade به صورت لایو و روزانه درامد داشته باشه
🔥
👇
https://t.me/+hcwmoHXpF6k5Y2Q0</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/67262" target="_blank">📅 01:47 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67261">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@Vision_Bet @Vision_Bet @Vision_Bet @Vision_Bet</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/67261" target="_blank">📅 01:35 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67260">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UWSm24Erq_EC6SsstFq4_hnaz7HVDR-sM26wb7yDsT-YxUSxIdQTp5BivAAr69jLg64B6N6V262dFE3keqjVQEvVL5BzUSviLeEVYj8nKWbrq_GcO6SHguXlC_FBtqG3y5J9mB_wCI1wGsAHR8d90xZqC3IJaQPSbEvqoWVyOMHVfZ_9NQh1CFOxpCXP7M4_WCCjPcloJGHFXFyfcU1vGIFWVcCrfpyuLYXFtGa_8LM8qGVxeU3G7SxgE54uPbSFQAT_Z5eV84DFG2s9hc37j0Q2Yi16EXxsieVVNsDr255mfl0UZ2xO0fMJiJuK904kMpWhdnlFeqkOkoAeLXQl9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@Vision_Bet
@Vision_Bet
@Vision_Bet
@Vision_Bet</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/67260" target="_blank">📅 01:35 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67259">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚨
🚨
🚨
سخنگوی ارتش اسرائیل:
اسرائیل آماده است به صورت مستقل با جمهوری اسلامی وارد نبرد تمام عیار شود.
@News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/67259" target="_blank">📅 00:53 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67258">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b0b72ac39d.mp4?token=UxLIhiBRjunIx16tbwJiFtP1rWIqmOz4CfqU71_2mkL4atYT_dAwZ3VEKatG4-4-sI1ycpj0j6dB9n1Q5kfdCrKkh8wGI-pAzMA-ALz6isis6WInM09PfQUIMxcJ7m8rulWRoF8xWBoqluhhQUTRa3Ukx2z556HEEsOP968OkCtU97Q4K1waGP-__kGT6cf3xB1kmU1Tz4UBqf794ljXZ33oJ8NFE_YPloFJ-D4DEF46MO2W1BWQaavpKCiANQ_lLslShna0YaH2TsMRVUSg14LE1q-ldWS3_BnZRQLKKGt0miikpTRYBWbxM7ei5hJLwCu8i9uoztplUw66JXtOe4PKcPY5OcQcQySO2yPIJHgsUVNiSbFRpx_LRa1BWOqPkHoaRRENF-C2LdOCB6d5xfg6KBOooQrdniKvnGEPyTl0OjAyIgZSnsjlobYGE7gPMXfyFCvi3IaBggNBbiVdmhSLydTryoWqGMVl3fChw_btaW_CUJ7_wCz7ALPQQGWXGkioFIvazVQUeCfQOWko3VFU2vLP-Btv4-BDTcIZ9xyNjeOBLgNyu_sdFdPeTODi-KEBoyNK3p245VqcFHPTbHcN1F2LQmb4mAx5gSg0cKjtIsITCo5f-wvo0Cx011be9Vro0cO6eA5ICxZemn_7cEKEopOkZFXvg3Lk1t4XkQ0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b0b72ac39d.mp4?token=UxLIhiBRjunIx16tbwJiFtP1rWIqmOz4CfqU71_2mkL4atYT_dAwZ3VEKatG4-4-sI1ycpj0j6dB9n1Q5kfdCrKkh8wGI-pAzMA-ALz6isis6WInM09PfQUIMxcJ7m8rulWRoF8xWBoqluhhQUTRa3Ukx2z556HEEsOP968OkCtU97Q4K1waGP-__kGT6cf3xB1kmU1Tz4UBqf794ljXZ33oJ8NFE_YPloFJ-D4DEF46MO2W1BWQaavpKCiANQ_lLslShna0YaH2TsMRVUSg14LE1q-ldWS3_BnZRQLKKGt0miikpTRYBWbxM7ei5hJLwCu8i9uoztplUw66JXtOe4PKcPY5OcQcQySO2yPIJHgsUVNiSbFRpx_LRa1BWOqPkHoaRRENF-C2LdOCB6d5xfg6KBOooQrdniKvnGEPyTl0OjAyIgZSnsjlobYGE7gPMXfyFCvi3IaBggNBbiVdmhSLydTryoWqGMVl3fChw_btaW_CUJ7_wCz7ALPQQGWXGkioFIvazVQUeCfQOWko3VFU2vLP-Btv4-BDTcIZ9xyNjeOBLgNyu_sdFdPeTODi-KEBoyNK3p245VqcFHPTbHcN1F2LQmb4mAx5gSg0cKjtIsITCo5f-wvo0Cx011be9Vro0cO6eA5ICxZemn_7cEKEopOkZFXvg3Lk1t4XkQ0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
هواپیماهای اف-۵ و بمب‌افکن‌های بی-۲ بر فراز نمایشگاه بزرگ ایالتی آمریکا در حال پرواز هستند و جمعیت از پایین نظاره‌گر آنها هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/news_hut/67258" target="_blank">📅 00:03 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67257">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd926d6f8c.mp4?token=Q-YCpRvQjIEM6n3G5cS6WJF-QeO5wvy0f9SGFG-svtnoXOaBYqpsuBZ-__jEBZ1URV_oL7jTSM_S00_M4I3uWiv6cVxuy6Lrj6rjvSl9g_bzlIbauFcQ5BbSxcE1wz21mWqLAhCrwf3gvIj5Eon47SHRIoH2oC7OWzX3_CTgTXuqiAuORxKmE63PKr0yI9beaVkKO_aJqHk7q8yt2UwRy5dMnLkqNDJ4siXrlcQhu-3swBPXxh7w06gLRLVfOM4DgucVTEHi1ahsCE4qzDIvf7NjI54rYCd35OKw2BXi_dTXAwxHy32eskkbRsZipyuj7aCLnaZbYygQ4x6EHQaMiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd926d6f8c.mp4?token=Q-YCpRvQjIEM6n3G5cS6WJF-QeO5wvy0f9SGFG-svtnoXOaBYqpsuBZ-__jEBZ1URV_oL7jTSM_S00_M4I3uWiv6cVxuy6Lrj6rjvSl9g_bzlIbauFcQ5BbSxcE1wz21mWqLAhCrwf3gvIj5Eon47SHRIoH2oC7OWzX3_CTgTXuqiAuORxKmE63PKr0yI9beaVkKO_aJqHk7q8yt2UwRy5dMnLkqNDJ4siXrlcQhu-3swBPXxh7w06gLRLVfOM4DgucVTEHi1ahsCE4qzDIvf7NjI54rYCd35OKw2BXi_dTXAwxHy32eskkbRsZipyuj7aCLnaZbYygQ4x6EHQaMiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
با هر ثانیه این ویدیو سوپرایز میشید
😐
😐
@News_Hut</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/news_hut/67257" target="_blank">📅 23:35 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67256">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e000f4f43c.mp4?token=Ltg7GRcsUrz9JWZ1Iil2OgkeKmThFaATyDd7EOu0e63Lh0bP9IuAMqQPOSrWoQGCfCTsDowRCIIATXb-0a3bO_CObxH16d1173rzHckFirou0GQHcd02WlDS2GJCIc384E0T4QpfgqYbRaZ2UhHwqtwMdbMPowR1hkcSrdS3A_a-HOn5NXULWC-RbP7pP4zD61j1QiK0-RhPdYZ39B7xEnE_hRGhXILwJIGPkyG-IO1cYKHB7gzra5aJ4st6YpjCaDml28_bz3juMz3FNflITHzNObXSfkp6VZdNxUaTpp48NYpcdMUhdP3T_Iotdn-Crz82coeWFnJAQoPETqNe7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e000f4f43c.mp4?token=Ltg7GRcsUrz9JWZ1Iil2OgkeKmThFaATyDd7EOu0e63Lh0bP9IuAMqQPOSrWoQGCfCTsDowRCIIATXb-0a3bO_CObxH16d1173rzHckFirou0GQHcd02WlDS2GJCIc384E0T4QpfgqYbRaZ2UhHwqtwMdbMPowR1hkcSrdS3A_a-HOn5NXULWC-RbP7pP4zD61j1QiK0-RhPdYZ39B7xEnE_hRGhXILwJIGPkyG-IO1cYKHB7gzra5aJ4st6YpjCaDml28_bz3juMz3FNflITHzNObXSfkp6VZdNxUaTpp48NYpcdMUhdP3T_Iotdn-Crz82coeWFnJAQoPETqNe7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
عزاداری مجری آیت‌الله بی‌بی‌سی از سران حاضر تو مراسم تشییع خامنه‌ای بهتر بود
😂
@News_Hut</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/news_hut/67256" target="_blank">📅 23:10 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67255">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1191e0b9a.mp4?token=V0xNOlEBa08gnsgerkGUmXJ3Xu-ZE6JCVAM0ci_RfkXE-XfNOZDx3vaa2UrtzRz3XNG-2xli9xMU-omEysJPrtDjEiz9KXzvIPgJjMRUz1CjhePpE3O3lpS9AD3Z3BTFYlxxuDIDls5b9N9-nIt3CZ60vnwadq_t4pV1Ts1uf3OTx2DIYDVDyNvF3PVVy-HInWLh-GjyGGStumvyeTweHWGzo3VDRTTx8umgZlcukGEBR-x49qem_bITeBez5e0zRoec6b7eTdKKYYpHZi8ctptbpexF9FH55CVFzWWw5Kpn3rLsDSHlM11pPIpugncA4ETBtZdQoBBoE6QZoV7uSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1191e0b9a.mp4?token=V0xNOlEBa08gnsgerkGUmXJ3Xu-ZE6JCVAM0ci_RfkXE-XfNOZDx3vaa2UrtzRz3XNG-2xli9xMU-omEysJPrtDjEiz9KXzvIPgJjMRUz1CjhePpE3O3lpS9AD3Z3BTFYlxxuDIDls5b9N9-nIt3CZ60vnwadq_t4pV1Ts1uf3OTx2DIYDVDyNvF3PVVy-HInWLh-GjyGGStumvyeTweHWGzo3VDRTTx8umgZlcukGEBR-x49qem_bITeBez5e0zRoec6b7eTdKKYYpHZi8ctptbpexF9FH55CVFzWWw5Kpn3rLsDSHlM11pPIpugncA4ETBtZdQoBBoE6QZoV7uSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تصاویر شلیک موشک‌های بالستیک آمریکا از کویت به سوی مواضع رژیم جمهوری
اسلامی
منتشر شد
ویدئوهای منتشرشده نشان می‌دهد نیروهای آمریکایی مستقر در کویت، موشک‌های دقیق ATACMS و PrSM را از سامانه‌های پرتابگر M142 HIMARS به سمت اهدافی در خاک تحت کنترل رژیم جمهوری اسلامی شلیک می‌کنند
.
بر اساس توضیحات منتشرشده، این تصاویر مربوط به ۲۸ فوریه ۲۰۲۶ است و بخشی از عملیات نظامی آمریکا علیه زیرساخت‌ها و مواضع رژیم جمهوری اسلامی را به نمایش می‌گذارد.
@News_Hut</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/news_hut/67255" target="_blank">📅 22:45 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67254">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3720a35424.mp4?token=Lr8_bJBcNmx8FXLAJWanFVxQDBDhqQ6bh5JjxNYPbnBK72ImUgCzBsyK-WeuutzQS8FUu0weErHbhiq-jBw67CKu9E8tN_5ICxkz_-UI6eCYLI7bR00aTApwStu9mIj2xznkLsKP3E65qTo4pt6zouj-Wr9n9lrEzzwpMKRAzTwXA2b8_hM-x8nhmvlQqlAVLHm3648sQQgAY4XUJDPYhrX52PQn5fOMl0z6WNozhEwOGHJgJKxnDW-o4zyMajmatoVt0pniISKKpmPUwhPN6Fr0jUXyfyS2AGdKz4Lbzk78QiDJuTojJVUs2UX9dTWHo_KSCkEdDw6thzO6IfyW4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3720a35424.mp4?token=Lr8_bJBcNmx8FXLAJWanFVxQDBDhqQ6bh5JjxNYPbnBK72ImUgCzBsyK-WeuutzQS8FUu0weErHbhiq-jBw67CKu9E8tN_5ICxkz_-UI6eCYLI7bR00aTApwStu9mIj2xznkLsKP3E65qTo4pt6zouj-Wr9n9lrEzzwpMKRAzTwXA2b8_hM-x8nhmvlQqlAVLHm3648sQQgAY4XUJDPYhrX52PQn5fOMl0z6WNozhEwOGHJgJKxnDW-o4zyMajmatoVt0pniISKKpmPUwhPN6Fr0jUXyfyS2AGdKz4Lbzk78QiDJuTojJVUs2UX9dTWHo_KSCkEdDw6thzO6IfyW4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ورود خودروی حامل‌ جنازه علی خامنه‌ای به‌مصلی تهران
@News_Hut</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/67254" target="_blank">📅 22:13 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67253">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QD1w5hnb603mCp-972cpCKdED5uxZQ6YG8lcI6EK-oYempNwmYzuIQuTfdXVraxavLBgAwyTpzKU7FHupjrPLwV03II3hUyPOo6PQVwATPD-tX0aCecZQhYzgo3bO7_124vStu7bKpXiwT-9zVzwl8z-tlEEKUj_5aTjLllW7dRzcCgu4V8s1dk16w_ZcRUm3mEOUMWUb_1can0QcDWxYBydbpaRluJJ_BdHjMACds6mbryjHJ7W4fdBB31_PFNTc4tsSe7iyIe3DgYriXN6PY4xfXzyKjEFhRvfM5chsq9QEzMWppmHUqU08JrsWT4gNP2bVMiNdxQLL-S-2luKsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سید مجید نقطه زن فرمانده هوافضای سپاه هم بالاخره از سوراخ اومد بیرون
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/67253" target="_blank">📅 21:39 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67252">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/teNTJhEie3pEDYsWtyvc2JSgbcbxQwiKBxIketqJO68K_tT8suK7lR49De8171wNP6Q4EDnuDyHY6UImNQWoP1jRE1vkp4rBPSldo-_P8-PD8QGUg5XR0RP4m31x-0IQPWP1GNWshUPzgnwerNWGpty8obaC4D6hkKlpoWbmU82IUnN4mxbJQmxnXWD086ON90yOc3oN_KPD6CY0wgrBtTiPQySqZAJ2PznuceO1UtNWMdXLL6tSZ4cQZpEOujlRkk8ZDBdfZbfnLUpwPwa1it-WrVeVYaBTcLP0y5wXAktLcHoSVFCUdloBYH23OCnDOHMD3Z6GpXSoQyIYxQvI1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بلومبرگ: ۵۸ میلیون بشکه نفت و میعانات رژیم روی آب مانده است.
حدود ۵۸ میلیون بشکه نفت و میعانات متعلق به رژیم تروریستی جمهوری اسلامی روی آب انباشته شده و نزدیک به ۹۰ درصد این محموله‌ها هنوز مشتری یا مقصد نهایی مشخصی ندارند.
بر اساس این گزارش، با وجود تعلیق ۶۰ روزه بخشی از تحریم‌های آمریکا، خریداران بزرگ همچنان با احتیاط عمل می‌کنند و خرید نفت از رژیم جمهوری اسلامی محدود مانده است.
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/67252" target="_blank">📅 21:11 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67251">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fJYunnOTUD6dcGYZeUNt6wksjCBWDQ60mIG_NPsiREq-CdOYRLBBIbOoWDtApRe4BRzIoUbx4wa6QJ6BgBA42W1uy38AN9eM84iJxlIHI7p6E_YWIBYEk3GBr39pwTCe0YO5VlApTbP5hYZYr2gU9bfuJZIhZsM8v7kbn26Jw_8hiVNeC5E-RA09Gk-zbXpjlmaugP4R8FcSirhtkHgaaGzSe5csbxB16cu-dvXexa7qj5CS7enfCO-KkrHj_P9s25bFaIfHl-rpN0Q4_nrA-Kc6Qw3KmrmyFzKDUDq1Oz0Uf6sdFrd94qsDXHOw_go1KlGKWzAVJU5NGwuGBJIsIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😂
نگاه معنادار عراقچی به قالیباف:
@News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/67251" target="_blank">📅 20:42 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67250">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U6wNF_Tmma8a-o_TmRl2qj2l5MMrtzmIUwoHUgjtxLBucxN2591dpvfUdpeaRKIBO0W4YSDU4nvDbI1Lo14dR4XHDo_UYoVhQJo10AQiWiZIN4du8ivqeoSTQf5qt-pX-6XkHfXXXjgBhfToVmFvGnpzfp3smlV74ygDmv9EWMcfp4H9l6IJgYEFNS2pge773wjwtTuk9j1-hBfC54mQoVpyM1At8JKinHTSpccQmpvtywuzoEvIqf6nchZy7q8WuRPQwpyuVqTX0oQcBJxgLZqQmmJIcjNWUMU9yTeRxr_WvuqA6JardaX2vjocrQFG6Haax5RI1dNHJSlZk7yXww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
باراک راوید (آکسیوس):
رئیس‌جمهور ترامپ امروز با بنیامین نتانیاهو، نخست‌وزیر اسرائیل، گفتگو کرد. دفتر نخست‌وزیر اسرائیل اعلام کرد که آن‌ها توافق کردند به‌زودی در ایالات متحده با یکدیگر دیدار کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/67250" target="_blank">📅 20:10 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67249">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QJM0zQk2NBp6wjx_l0dPMp4w2AqQ9y4ibSY1VBipXee69LKksizlnNJbra2D992E-k08NHZjH_X0uEB4JrSnkYv1NHgm6ZXfyj2BHKCSmBcMWM9vQS4nwhvi3asbhHZFaMXdCgHK8uqxAmpsUpjmuZNs9O4mJHOt5yjG3h2mAiky5Z1A_jcIENIO1f1yFI0KH0HudJIuZHGBE8-w4NW0FMiwwGvE3MivJuGRg3jrZkhi0dfoJKU6APWKx7uCKz3SYEUn6FOq-4k3XnUiZnxeICN_QUz7-XGX_8EeJk7WX4qXNE2CpbQ7A5hjEvNUG0wb6n4UVImpJXfc_4WXrWDWUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😆
😆
‏سی تی اسکن از دندون عقلم:
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/67249" target="_blank">📅 19:41 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67248">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HmJ26nima_X2x2Qmisifkhmxh0ElfycTtufIX2VJf3QTRAKAnBDf_0hK1xXFBXEshWbiwMl9df7wdeUWf5l2_DXBBaex33t0sLxDZchXPIGgdQ1czX95C0YeGqP623pE7u8iXTBwVIXgjMJBzd0_CIIw_u86LSHc5WYW-XTWFpffHVM32ZunTWooeKn3r_4NRUcBt9U0w5R2Hb4HqfgJDT0js_JDiQIizsgGWvkKLyHltl4JQHs4ZSoEOczWT5cPnglnzycl549lBDo1WPPdSK_xxh5LEkYAVOWQHE5xjMbM0OEyKYll526-YLADOcYTiZQ9TXjDeuDuOabFgR8VhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
دفتر نخست‌وزیر اسرائیل؛
گزارش نیویورک تایمز را که حاکی از آن بود مقامات آمریکایی معتقد بودند اسرائیل در حال توطئه‌ای برای ترور مذاکره‌کنندگان ایرانی در جریان مذاکرات با آمریکایی‌ها در بهار امسال بوده‌اند، رد کرد و آن را «یک تحریف کامل از واقعیت» خواند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/67248" target="_blank">📅 19:25 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67247">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4bc1c344f.mp4?token=rzl7J6LB2OzmMy4cngGiM4I0WftbMI3Am_v-nUacg-J2Ac5XN6pWktvEUHqk65HZsSh3vtkUoUkExGBBeIjawHsd5n0tD2vAqF_KB9y7vAvlQGgi9lNFgL8llzCbXh601dm-3G6wvDEkkItta7l-RGIE7ouZPrfps-xcymTdtLVEXN-iU5p9rwijmDe5b77MtO7_ChqIsv2ON06HVor-nFH8uNETRLRLcYgG64PXw1jH5Cq7Dw28mu2mHM038pbzt5UmhUpHAWJaw9Tr5UU5nqrxFgeIpomI72e9Kir6sZKvsGQQRggm7bi_mKX0Rgwo3zAhCIjUD-lJcCnwTUairg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4bc1c344f.mp4?token=rzl7J6LB2OzmMy4cngGiM4I0WftbMI3Am_v-nUacg-J2Ac5XN6pWktvEUHqk65HZsSh3vtkUoUkExGBBeIjawHsd5n0tD2vAqF_KB9y7vAvlQGgi9lNFgL8llzCbXh601dm-3G6wvDEkkItta7l-RGIE7ouZPrfps-xcymTdtLVEXN-iU5p9rwijmDe5b77MtO7_ChqIsv2ON06HVor-nFH8uNETRLRLcYgG64PXw1jH5Cq7Dw28mu2mHM038pbzt5UmhUpHAWJaw9Tr5UU5nqrxFgeIpomI72e9Kir6sZKvsGQQRggm7bi_mKX0Rgwo3zAhCIjUD-lJcCnwTUairg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
لحظه بمباران بیت رهبری 9 اسفند 1404
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/67247" target="_blank">📅 19:16 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67246">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/edXxRZPU3xIQDxMnaDdVi_e0p-DmxPUsNtX1SSjePTAmJI6ggrF4bxcHpyoegEi6kGLvYAB7E246Oihb1V5IWZ-4QjOB9c_1o7mZDcCojCj7Z_innsULREibMMQ3bNZIw9BLOE3RzbFrbT6zVU9hFSCvFPNJoUWqqH3PmPTkdI_3cqSExgLZ3iy6FnD6mLuf-KjOi1JMUtgCgDlymqIpQRkSCzbTji0ayNldhvUH-drTXlQthDWd-jrBJ7y6gWH626BS93tFsblJTd4J29XhFqCrUnDMtJyXGfajqUfDRhBz3Ia2wcs8TrIHMrv-Sl8Hbey9racXxmK0o8PDcK5Pww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/67246" target="_blank">📅 19:16 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67245">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1099f5d95b.mp4?token=mA9Ro6T2R8NK6L3x5w4ouBH-_aWPGAIe6QxwrMt_uscEe2aMfgcglDJa_SS2iIINJ0aYsdYkAPUZ0KR8Na_f3-G6d1y9Uo0hIwBKVIVWFUQOzBEmmYZlQbxAlQKdive-qzwlQDAGnCjRcod21NOVNa3M4ST7Xm8HQU5xgN-r8twguT5B48xL00Fnxr-N8aPZeU2QbLjTxjXUKTmKeZikisPHUzg4ZHknk_OjVcRNeJfbCSOcBJDUbpVdaCKK_Yl4rgDm9_pl_YJYbXIx8IBpCtnRXPoGTufWSgpuwh5WwNdByd8snDbEIaUqTqgrIss75lU3dRjgKxoHxqAfXWd9kQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1099f5d95b.mp4?token=mA9Ro6T2R8NK6L3x5w4ouBH-_aWPGAIe6QxwrMt_uscEe2aMfgcglDJa_SS2iIINJ0aYsdYkAPUZ0KR8Na_f3-G6d1y9Uo0hIwBKVIVWFUQOzBEmmYZlQbxAlQKdive-qzwlQDAGnCjRcod21NOVNa3M4ST7Xm8HQU5xgN-r8twguT5B48xL00Fnxr-N8aPZeU2QbLjTxjXUKTmKeZikisPHUzg4ZHknk_OjVcRNeJfbCSOcBJDUbpVdaCKK_Yl4rgDm9_pl_YJYbXIx8IBpCtnRXPoGTufWSgpuwh5WwNdByd8snDbEIaUqTqgrIss75lU3dRjgKxoHxqAfXWd9kQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
بغض و گریه های تمام نشدنی قالیباف در مراسم وداع با علی خامنه ای:
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/67245" target="_blank">📅 19:02 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67244">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ff481eda8.mp4?token=DLS78Q3P4sbxsVwCCzTBwh02WXI5v9pIOcMjljza-VG-uJ4j7rxFsi8mDBvytc2YCD0aJNbTtqQsYxn4NJq9eZMmb_TPOroouOR_etQa_0CJQu05KfyAD6_u9xmw8M1L1SAZIwv71FxkzWwqPG3gTqfQtjubj4j_-_iNpz0at7HXR9WaEI5gJoWfs8wLogKtvIr28ayeGqiEgobhKmACqc-Wtc36zabGS2wQPWkRMK0kdUJb2k7VRzDO_T-kDymhG00t2bx_DMJ6O22-zoyXjGYS1L0QvDBtJfHZCTJVXDTr5wBLsyc6Zo9KmpZaFkLvFGU2z2gLhDW9rYn_pFGs1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ff481eda8.mp4?token=DLS78Q3P4sbxsVwCCzTBwh02WXI5v9pIOcMjljza-VG-uJ4j7rxFsi8mDBvytc2YCD0aJNbTtqQsYxn4NJq9eZMmb_TPOroouOR_etQa_0CJQu05KfyAD6_u9xmw8M1L1SAZIwv71FxkzWwqPG3gTqfQtjubj4j_-_iNpz0at7HXR9WaEI5gJoWfs8wLogKtvIr28ayeGqiEgobhKmACqc-Wtc36zabGS2wQPWkRMK0kdUJb2k7VRzDO_T-kDymhG00t2bx_DMJ6O22-zoyXjGYS1L0QvDBtJfHZCTJVXDTr5wBLsyc6Zo9KmpZaFkLvFGU2z2gLhDW9rYn_pFGs1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
برخورد سردِ حدادعادل ( پدرزن مجتبی خامنه‌ای ) با عراقچی و قالیباف
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/67244" target="_blank">📅 18:29 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67243">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6d67ab774.mp4?token=F-IvusIAY0Je9FOcCmLFIFJ7deQKeLaEb5qlZW50TACNmUGRrV63Qsde0rrDFC4Z5Nxv0ahqPfEugC5y0QQrvGexNFA8JaDMraK2q4YJWxRcLKbJOK0Z39zqIAs-5mUqaIieBuEIoTCySHrrjGaMHK1A59C-S6VO-I5W_9BY-h9Pf9DW_9QIf79f2Pyoe45t6fr6X0202jL9xhE7Ur_O6zjadGVGzCZaz9XCqDBwBHikb6m0oP79R2h6LUa4biHFzgtd7cVioc8xj9DruAecVBN54JdblYBs3mg3gjysM98ToVM1DHV-DMBImJ_5S__U458DHdBrIH92KT8USofosQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6d67ab774.mp4?token=F-IvusIAY0Je9FOcCmLFIFJ7deQKeLaEb5qlZW50TACNmUGRrV63Qsde0rrDFC4Z5Nxv0ahqPfEugC5y0QQrvGexNFA8JaDMraK2q4YJWxRcLKbJOK0Z39zqIAs-5mUqaIieBuEIoTCySHrrjGaMHK1A59C-S6VO-I5W_9BY-h9Pf9DW_9QIf79f2Pyoe45t6fr6X0202jL9xhE7Ur_O6zjadGVGzCZaz9XCqDBwBHikb6m0oP79R2h6LUa4biHFzgtd7cVioc8xj9DruAecVBN54JdblYBs3mg3gjysM98ToVM1DHV-DMBImJ_5S__U458DHdBrIH92KT8USofosQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
کلیپی قدیمی مربوط به انتخابات ۸۴
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/67243" target="_blank">📅 18:03 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67242">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iuduxLbRcQJoKhrxFAQBkKWCkzy2Epltw53yXHVq0pBGA5bj_t7Xfk06dxCZPjuYBY9LLDKsc9TaDoZiib13AlJ7GPue03im4zSUdT1ZNHl7raf1LK2_XRLszrxq1JholcyM1cMvgDJMFj_cMcpN7-2YKCT0uIA6SFu_1rpiM-VfzoykEduZ0OW0bxd4Tws36XRST-GhymEdaBbWoZRgU0H4VsqFrSa6p-M5SbXq22FTpO3STfimyb4knnZ6p3-DUqubDndM1Wsklu_cGKanTbbrqhak7J-IBQS97b-8aTvrmYOUZ2tU3x7kXwOwNMOudySOTeK0UHUMFL00NoF7xQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
چهره خوشحال پزشکیان در استقبال از مقامات کشورها
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/67242" target="_blank">📅 17:33 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67241">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4864316f1d.mp4?token=ozMN9Wussq-tx8JYinHjGsyABZM4NCAuRQCbnLExzz-PctDrMw7pKX953AmsIWOV3GpUioyAgQ2yDHMaaCPFnoUqEpugG2-ULB3tY6A29OH9abluFoxuplJJJmkyHRWexzB_e1rIveiLVAjohJm1NerG-qGbV_9jwsjChOmKUID5aQECZjIs4Ml1nSS2jwqtRm4j4yjvUyVDf8QQIbgCbhBQGejkMWQhdSlMJqFKwgNMX-W_kGHq4CXshJx0xUdeXcQzheyDxzZsglIn2ncPbRwnUc--q6Akeryn_DTAdib-yfVz0NsuDhW5tTSUTkZpEs7PYuWBZCTqXKv-Gg1J_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4864316f1d.mp4?token=ozMN9Wussq-tx8JYinHjGsyABZM4NCAuRQCbnLExzz-PctDrMw7pKX953AmsIWOV3GpUioyAgQ2yDHMaaCPFnoUqEpugG2-ULB3tY6A29OH9abluFoxuplJJJmkyHRWexzB_e1rIveiLVAjohJm1NerG-qGbV_9jwsjChOmKUID5aQECZjIs4Ml1nSS2jwqtRm4j4yjvUyVDf8QQIbgCbhBQGejkMWQhdSlMJqFKwgNMX-W_kGHq4CXshJx0xUdeXcQzheyDxzZsglIn2ncPbRwnUc--q6Akeryn_DTAdib-yfVz0NsuDhW5tTSUTkZpEs7PYuWBZCTqXKv-Gg1J_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پزشکیان در تلاش برای جاری شدن قطره ای اشک از چشمانش
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/67241" target="_blank">📅 17:01 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67240">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/597b986b2a.mp4?token=IyWvzUspN2Aq_BRlHk34mn8BpzqZMcfmgkJqim7H8sE3a_lkS0BOvt28-fEvMd5hnplD0J6sxW_2oL6nMTXqVWDFkABNS_FBzd-p_mId5HsAbR4_EBf5Uj_CF8N4D2Xap4jTdtAr9qGGaWtQXiexxitNPhadCsQfYd4SH2oI5BxO10Bk2YXHL6qt-2XGTwHxllDVfjxd91BhuWU8MxzbzGAoF1jtp-M5PlYzbBZs553JiCidwfgyPUvNY0Tkt-13n73yKY5IXMPI0XOpNUGqZ6rLnaLHbL-dnQA75u3irGx7nkSCPm66h7GOgPeaA5GlvYf3VkTLflofet9vkKqPHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/597b986b2a.mp4?token=IyWvzUspN2Aq_BRlHk34mn8BpzqZMcfmgkJqim7H8sE3a_lkS0BOvt28-fEvMd5hnplD0J6sxW_2oL6nMTXqVWDFkABNS_FBzd-p_mId5HsAbR4_EBf5Uj_CF8N4D2Xap4jTdtAr9qGGaWtQXiexxitNPhadCsQfYd4SH2oI5BxO10Bk2YXHL6qt-2XGTwHxllDVfjxd91BhuWU8MxzbzGAoF1jtp-M5PlYzbBZs553JiCidwfgyPUvNY0Tkt-13n73yKY5IXMPI0XOpNUGqZ6rLnaLHbL-dnQA75u3irGx7nkSCPm66h7GOgPeaA5GlvYf3VkTLflofet9vkKqPHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
در یک سو مردمی که در زباله‌‌ها باید دنبال غذا بگردند و در سوی دیگر «تامین ۱۲ هزار تن کالای اساسی برای تشییع قاتل فرزندان ایران زمین و عامل شماره یک تمامی مصیبتهای مردم ایران!
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/67240" target="_blank">📅 16:26 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67238">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b4f0f3e3e.mp4?token=CdswS4YULQnm1Jdrds5ZyVeabVrBjklxwr5YuDYhgf2myELmiJXLZ9_w92uk2UEUD49SdE6ACRKaWIB5w7n2TrBaRIsqWw1gBnykDDEB_HP_vvOfUs06klYNyG46n9KKVlh2fLxWF6LMJ-hOjsYU7cuukKoWAnxCkekbdBKVK6t5YEMh76PGwGenRMGQxfMTyDK4iNOUM5DzMBl2-7YNdJJIVSio1-dLkFSH5ozIthQMzTbsoWPcCmr5vCLNBvupu2-P-9jKCnIFXhYjUIm8kasFOLt3iDwWl2U0HzWHwfVfsi4wli4aSmLEPc_FSDO-0rSi2KdHGNZxc3Jyl5YJVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b4f0f3e3e.mp4?token=CdswS4YULQnm1Jdrds5ZyVeabVrBjklxwr5YuDYhgf2myELmiJXLZ9_w92uk2UEUD49SdE6ACRKaWIB5w7n2TrBaRIsqWw1gBnykDDEB_HP_vvOfUs06klYNyG46n9KKVlh2fLxWF6LMJ-hOjsYU7cuukKoWAnxCkekbdBKVK6t5YEMh76PGwGenRMGQxfMTyDK4iNOUM5DzMBl2-7YNdJJIVSio1-dLkFSH5ozIthQMzTbsoWPcCmr5vCLNBvupu2-P-9jKCnIFXhYjUIm8kasFOLt3iDwWl2U0HzWHwfVfsi4wli4aSmLEPc_FSDO-0rSi2KdHGNZxc3Jyl5YJVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ارتش دفاعی اسرائیل:‏در واکنش به آسیب واردشده به نیروهای ارتش اسرائیل و در پی نقض توافق آتش بس: حدود ۱۰ زیرساخت سازمان تروریستی حزب‌الله در جنوب لبنان هدف حمله قرار گرفت
🔴
در حمله‌ای دیگر برای رفع تهدید: نیروهای لشکر ۹۱ یک کامیون مورد استفاده حزب‌الله برای انتقال تسلیحات را هدف قرار دادند
🔴
در حملات دقیق نیروی هوایی با هدایت لشکر ۹۱، روز گذشته (پنج‌شنبه) حدود ۱۰ زیرساخت متعلق به سازمان تروریستی حزب‌الله در مناطق بنت جبیل، بیت یاحون، کونین و براشیت در جنوب لبنان هدف حمله قرار گرفت. زیرساخت‌های هدف قرارگرفته توسط این سازمان برای پیشبرد طرح‌های تروریستی علیه نیروهای ارتش اسرائیل که در منطقه امنیتی فعالیت می‌کنند، مورد استفاده قرار می‌گرفتند.
🔴
این حملات در واکنش به آسیب واردشده به نیروهای ما در منطقه امنیتی توسط سازمان تروریستی حزب‌الله و در پی نقض مجدد توافق آتش بس انجام شد.
🔴
همچنین بامداد امروز (جمعه)، نیروهای لشکر ۹۱ یک گروه از تروریست‌های وابسته به سازمان تروریستی حزب‌الله را که در نزدیکی منطقه امنیتی در جنوب لبنان، در حال انتقال تسلیحات با استفاده از یک کامیون بودند، شناسایی کردند. بلافاصله پس از شناسایی، نیروی هوایی برای رفع تهدید علیه نیروهای ما، این کامیون را هدف حمله قرار داد.
🔴
در پی این حمله، انفجارهای ثانویه شناسایی شد که نشان‌دهنده وجود تسلیحات در داخل کامیون بود.
🔴
ارتش اسرائیل به فعالیت برای رفع هرگونه تهدید علیه نیروهای خود و شهروندان اسرائیل ادامه خواهد داد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/67238" target="_blank">📅 16:00 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67237">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LjRJaC7_Y_023Equ_hC_KqvYUadbnM9GqgQ8CQ-XkIPSZLACLOlnBr3Jhc-uTpHC4Jbts7pgl_DUyLiiX7fYKkXmqh-HxtGfIe-wvYBnxc-A95K6CCPMOMPR0Gm3nnZJx0XYNGuvYyrVijGuJ7pEPWSzhqeB-I4nMVTxi78TijZNBse0h5T2zsKzfuud_mmZcJDVoHW6o5NkWCDGml2JsPTNHPvgZ7qjifwGDikIyK6o9PVaQ4ul42KyqwOhy0FdFibGrA7rOKU2TxoeMLJuCwr6NH0BwZmh4wtmfT3ag_HO5koHaZXadOrT4mVkUHU3KOXGWivbajt2kdkEn54eSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
پنج فروند بوئینگ ۷۷۷ سعودی سابق علیرغم تحریم‌ها به ماهان ایر تحویل داده شد:
پنج فروند هواپیمای پهن‌پیکر بوئینگ ۷۷۷-۲۶۸ER دست دوم از خطوط هوایی عربستان سعودی به ماهان ایر ایران تحویل داده شده است که دو فروند از آنها در فرودگاه مهرآباد تهران تأیید شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/67237" target="_blank">📅 15:28 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67235">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pynPB8p0-OFIDkEGdzfZCNXXAdngnoQA2eKG7v7Vsl8nwNbEltoj9ubGpspu8YuC9z-CW_JmnWrK-kUXdlxOFm1TBRFNeci1YwEAUKcB1uegg2rSw8AdM93ZtdVLs0SfwxZMmaT6f1dvIWTh5pdHyQNZ7b9NGtIHDgWUiZa2UuT7eims5lH4QngD_X3Nx1_1o2vfQLnkrYHasvvbUQFd-NVlf-zkJMXCvTIfErOSGcXSeSBuN5ADV7wcjO21-Umn8k8RD2ufRpoMHcXyjx74PYktN1dpjU3_D5E4ytMqhtEvOm6kqs_n4YU0tb5njUMy2OgZaf19M1cBelHM0KEshw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e169f3d67d.mp4?token=f4baJmaOLLVbaNaGPAsofWOktI6vK6CcJI4OoFw6wOToAGiqIIshuOW7gjTbekrj2K8BmqYxSrKn0-SuxJAS7CSR_MCgnPD65SO08YIfIJKAtIJVLHpzO6_GDwDztuaFDfUreOWnSU3ZXe_FfFmxyaqmCW7S9mdI9GBK26O_g0RWsMNYmv6xZou7_D19nb9Fb3xVNaeV_GiqoT7loQcMUd6PYqw6E5h-290NlIuWv-DGYt2rkU8yGxnQsjD4DS0pd-e9Tnqh4i-E78f0BoP6zOE0bgjIvJIgHk2Q05LxlN9PS7Nu6p2SMPLPHZKbzHaroDUhxVBWuyuWTbQkvw2iag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e169f3d67d.mp4?token=f4baJmaOLLVbaNaGPAsofWOktI6vK6CcJI4OoFw6wOToAGiqIIshuOW7gjTbekrj2K8BmqYxSrKn0-SuxJAS7CSR_MCgnPD65SO08YIfIJKAtIJVLHpzO6_GDwDztuaFDfUreOWnSU3ZXe_FfFmxyaqmCW7S9mdI9GBK26O_g0RWsMNYmv6xZou7_D19nb9Fb3xVNaeV_GiqoT7loQcMUd6PYqw6E5h-290NlIuWv-DGYt2rkU8yGxnQsjD4DS0pd-e9Tnqh4i-E78f0BoP6zOE0bgjIvJIgHk2Q05LxlN9PS7Nu6p2SMPLPHZKbzHaroDUhxVBWuyuWTbQkvw2iag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
بر اساس گزارش‌های اولیه، جنگنده های عربستان بر فراز صنعا، پایتخت تحت کنترل حوثی ها، به پرواز درآمده و مواضع این گروه در نقاطی از یمن هدف بمباران قرار گرفته است.
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/67235" target="_blank">📅 14:57 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67234">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/I4ZcE3pLCM7Rc2Eqdk-UX8gVFK5ZVKS10Iaof-tsaZel3MDWSqpMX7DTNvIXUKNjqIXERLH5FnZ-3Xp6LnS6kGlMaF6APQFELzZ5N8xM-S61OGTsDtkK2-NmXic_JldiGjQPfKcs3tOFCa0god1ByAXcZ_QSnIrZh3gWv7BFeSVburWnBbKfOaZfEcX9pGrJCBYMs4nmwlWe6uj2pxiU7fPFdZbUQcZPJMBWpVMSRhcDJKZ1I7QrgsSacltipsfwl6ckLFMgHRjIjw0m5dxBKhLY5HU5M5xg7rqR4GK0_7vX_LCSwA-SvA9uF2l25kNFxS8fTGJSaqyRO8it1dkjtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
این عکس از تفاوت تابوت محمدرضا شاه پهلوی و علی‌ خامنه‌ای وایرال شده، تابوت شاه کاملا ایرانی و تابوت خامنه‌ای شکل و ظاهر عربی داره.
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/67234" target="_blank">📅 14:17 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67233">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4654e8258.mp4?token=JW12pCMHX_8G-gc-E6_MnVLW7YxSGO8EgQQErm83YeJTh5U3TGuxaJwLSh2__AJzMZTEuPmei0GdZ1_MzKUmoveKcBP4AVAw5RnkF6dVRH9Q40-FEkf3bhh5yt2E-BtHvGvfzhBc7W19TbKwciOs0rpeAgorE-T9wyOh2MElA_5k3FmN1BYX9PPhBqpMRw0Wy64pXY1iJ7X4AxzQ3r_B5SP3L5XXWn8nOPVV4ylodph5KlldiYjNTuukoxwIFpMewzPE--h_2_cK0wvjCRZ1FZ7W1zCN5mDhHOphaK3_g8vZ5UiFcsS879rfW17b5jWS69Eh4-PvU6ViuhDQwkMEGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4654e8258.mp4?token=JW12pCMHX_8G-gc-E6_MnVLW7YxSGO8EgQQErm83YeJTh5U3TGuxaJwLSh2__AJzMZTEuPmei0GdZ1_MzKUmoveKcBP4AVAw5RnkF6dVRH9Q40-FEkf3bhh5yt2E-BtHvGvfzhBc7W19TbKwciOs0rpeAgorE-T9wyOh2MElA_5k3FmN1BYX9PPhBqpMRw0Wy64pXY1iJ7X4AxzQ3r_B5SP3L5XXWn8nOPVV4ylodph5KlldiYjNTuukoxwIFpMewzPE--h_2_cK0wvjCRZ1FZ7W1zCN5mDhHOphaK3_g8vZ5UiFcsS879rfW17b5jWS69Eh4-PvU6ViuhDQwkMEGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
حضور فرماندهان ارشد نیروهای مسلح جمهوری اسلامی در مراسم وداع با جنازه علی خامنه‌ای
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/67233" target="_blank">📅 14:03 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67231">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YqVF9eIfl-RJSX2sfJqhXuBbGveqjb06NluPyRQIqBM3IgtLLQDND41KF1UZqGrX100F5C9W-8kDqzXndf0bLhHk9qa8FfqCeWY_E3C42rDoJFri04zDL4Iu_nJ_tTmsF9gdPVimhm4VwWY5Cb05CYgcQd3SCaG3tHRZT8F-yTqbVhYIxUQ9ETq7KjELckvkMrPymnvG-hpRazGJqF4D5MLKjOMsksb-yb2_-399Pz_KK7uYTTxNknV1e87rmHGkvZuUj3WbRZdhE54KSRU9btnczdIKGjeLLmWkC51BpgaYglGd9NeG2Bvcl7u68cCgV0-eacuNJkB69xYNptW7EQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1483e21a1f.mp4?token=GG43Ee8qV6Wwns_0oJvdppzfBfMi2VEg6kd63sbO6geMX_ET41sz6akgiiUhNQiLLCS9F57sTMe-zKGtiZ3YCpwlRbN4cNYZbsb0H3CLBsuHt0zqC0YOUFXkh-WWbHUiRX7mHAIoWgpRl5w8Gfx5-tog6hKHGoIxURNPwWI28VjcatZF-JgrKATi5GWT7SVWhQJpfrxpBCYZb-sxBaR2FIy4GKP0a5-jF--H3CchSJBkYLaFhKIPrUsbEJjjjA1vHHmSKajr-f5XqJzbYPnLe9dPn-GzcFnsefp84E4cJ6X1XjPTXP2Z4_hZlClw_IOpe7FUrKdZ9tauwvfnmAdRoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1483e21a1f.mp4?token=GG43Ee8qV6Wwns_0oJvdppzfBfMi2VEg6kd63sbO6geMX_ET41sz6akgiiUhNQiLLCS9F57sTMe-zKGtiZ3YCpwlRbN4cNYZbsb0H3CLBsuHt0zqC0YOUFXkh-WWbHUiRX7mHAIoWgpRl5w8Gfx5-tog6hKHGoIxURNPwWI28VjcatZF-JgrKATi5GWT7SVWhQJpfrxpBCYZb-sxBaR2FIy4GKP0a5-jF--H3CchSJBkYLaFhKIPrUsbEJjjjA1vHHmSKajr-f5XqJzbYPnLe9dPn-GzcFnsefp84E4cJ6X1XjPTXP2Z4_hZlClw_IOpe7FUrKdZ9tauwvfnmAdRoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
کارشناس حوزه انرژی: تنگه هرمز از مسیر عمانی، اتوبان شد!
این فیلم از موسسه کپلر را ببینید،
چقدر تلخ است، کشتی‌ها و نفتکش‌ها در تعداد بالا از مسیر عمانی از تنگه هرمز عبور کرده و همچنان می‌کنند.
با این روند، به زودی ترامپ بابت تامین امنیت کشتی‌ها از مسیر عمانی، عوارض هم می‌گیرد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/67231" target="_blank">📅 13:32 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67229">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50fa301248.mp4?token=wAB_RLKNU1nQ9RzX6t3KG8M_wUZgoARHXszpRLND76IXcyDSQI5czozJQlaHiUGE-7JXeEsYY8XamGWRLHivHDBjdfBbx_OpEzrlrG4vdrD5BHK8UbBzZ5f-fQuxYlnZjyum7zMyeut3y8ZHA_HseqMgsGQFf8CNVVk6ESXKJXITPBYUzLgfBjVHK00JyHA5AtZDhxEJPHUrA7mtpUPPw4-uYV5Zkn_ofnmk1x7s0vmX6vmSiHw4FWtHYhE2-FeS6jEC8Hw9brVmVih7WFQsFKMSLv-cJSknQehSK41lS4HZ1c7oXDJ3Y37JXAVIlMwMWDygcuNng5-M-DsQVvulcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50fa301248.mp4?token=wAB_RLKNU1nQ9RzX6t3KG8M_wUZgoARHXszpRLND76IXcyDSQI5czozJQlaHiUGE-7JXeEsYY8XamGWRLHivHDBjdfBbx_OpEzrlrG4vdrD5BHK8UbBzZ5f-fQuxYlnZjyum7zMyeut3y8ZHA_HseqMgsGQFf8CNVVk6ESXKJXITPBYUzLgfBjVHK00JyHA5AtZDhxEJPHUrA7mtpUPPw4-uYV5Zkn_ofnmk1x7s0vmX6vmSiHw4FWtHYhE2-FeS6jEC8Hw9brVmVih7WFQsFKMSLv-cJSknQehSK41lS4HZ1c7oXDJ3Y37JXAVIlMwMWDygcuNng5-M-DsQVvulcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
پالایشگاه کلیدی لوک‌اویل در روسیه هدف حمله اوکراین قرار گرفت!
این تاسیسات سالانه حدود ۱۷ میلیون تن نفت خام را فرآوری می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/67229" target="_blank">📅 12:25 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67228">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZpcfYf_i4D5M0EJisqvf3fgkCfwp9ymTFXxFu9QkcOYEiHFvb26mVw66DB8H8-CcynCBnpRd55ORKTzm4sBdZbnacmAb1oCDnijg_RDuCSyZGxfUxt3-Z37evUeuAbo7xB0o_epPoQzfxyKwfsYhcjZefO1g-zkRqCnVmp5EyFXmlhnGhxSEu5HvX21fR7ckJJtMCbGZhMeqWNiRHjkSl6Lc51ilJ4z8Oy_3OLc-MJm-VL6B1fthb7l2BnQYCknVzr9ulUl9k5vcHSAtcvi2XQcPSRB4n63wg68EiBmwNH1o7sgHM8wqtdRCYZg2K8SYhjUPdMCU37tW0xaBzlWZyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مرندی:
همان‌طور که ترامپ درباره درخواست ایرانی‌ها برای برگزاری جلسه در دوحه دروغ گفت، دیشب نیز دوباره دروغ گفت؛ این بار درباره حمله به تأسیسات راداری ایران. نه جلسه‌ای در دوحه برگزار شد و نه حمله‌ای به ایران صورت گرفت. هرگونه حمله‌ای از این دست، با پاسخی کوبنده مواجه می‌شد.
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/67228" target="_blank">📅 12:21 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67227">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XqEU7dS4mzWTVc8FLtS8joC7kW57dy2wUIjy769qEwr-qW2uzRpoPa-FImEGTD7DxabKl80X9SBFQ2KC3GLEg4AdePhguv195BQ4p7K4U8RwS2J0VYMskztJRJgg-WMaPrk5Sf8KkcSjAFC8vz1Zpm1vCtHS7WB-PrGwTO8GYi6ioXUO17JVqNZ1mFI0OKepc6K4w8eyaKble3XVw1mDLQzzzVeEJtIYw5G3ArxZgZZMpaVrM3mIY5O-VB9cBvQ1SH5Cc9ArUBxEBHw1cgINhgnuLOwV7SrWRM5X2vXiMVVqnjEQPb6lBtp0sclg-xSebSD-N7Ix27pe3XH_qYeT9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی طلات رو روی ۱۶,۹۰۰ فروختی و توی یک روز،
قیمت طلا
۵۰۰ تومن بالاتر رفته!
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/67227" target="_blank">📅 12:21 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67226">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F99XmNVWkcySF7f_cs0SW6sdY50sOtoK7DCrmH3VF_KrdxlV1q22BE78YEzyJuxyVGmuaYFxwG6gRWIWK9uvmKpK5mmvLZPDpgreNY4hXb-v3i3pfl6WywQ8vP5LeE-ZxlCesmJxwrm0bJQs3pxyZYItMS9YVB0af42H_ovl0ZeYZ2oGWikdtygaV3CxI22o-u8kg9NqgAved55Av983XfDILxY_AYSEvU-jULhhtYzulrT4IdilyYGlK0WJwFt9Tm6IwEvrLUA5L5sPyvsOEVSkvmz7w1IEZ3HNOAEJFVYuW6YuP8yFbBm4YxhzyOmCPFT4UyTeViJp-3GEGRos0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
توییت جدید محمدجواد ظریف:
ایران، پس از دو قرن تجربه تلخ ناامنی و آسیب‌پذیری، با هدایت رهبر شهید به مرحله‌ای رسید که در گزاره «دوران بزن در رو تمام شده است
🤣
🤣
» متبلور است. این تغییر پس از دو سده، احساس خودباوری و اعتماد به توان داخلی را برای ایران و ایرانی به ارمغان آورد.
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/67226" target="_blank">📅 12:01 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67225">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f10282a802.mp4?token=fvdwRDJ1Q79HK5E7_O67urN8xp7C_ZjufoDuM5pd5WdwdNuJg3u0Slnbziwhg9ueP2nW_jayMSBe1z_NMjZnM-IbW1ibeoF_AEFFV1AW5ClfAWHulLtUkuPZUzv1Rz3Y2s5xx7-KDyF_xlWa1S-hlZClnX9Hupc3ErY5O_EbJ9XV2T6TvRd8p7QAZ1khlBPI1x-5aWNjTJVvfMEBbEvMQRQB10ShodB2Maq6gUsI_DPx-URzbx3pEtLOyXwvBV5Q-xw8zgCjy1GgSv5aByHtxYj6sUs2v2ykKmaTzxm7tW9ZANizcZcbcc-3cHO1Vz2srN0iw_H6HNTowayi3cFyPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f10282a802.mp4?token=fvdwRDJ1Q79HK5E7_O67urN8xp7C_ZjufoDuM5pd5WdwdNuJg3u0Slnbziwhg9ueP2nW_jayMSBe1z_NMjZnM-IbW1ibeoF_AEFFV1AW5ClfAWHulLtUkuPZUzv1Rz3Y2s5xx7-KDyF_xlWa1S-hlZClnX9Hupc3ErY5O_EbJ9XV2T6TvRd8p7QAZ1khlBPI1x-5aWNjTJVvfMEBbEvMQRQB10ShodB2Maq6gUsI_DPx-URzbx3pEtLOyXwvBV5Q-xw8zgCjy1GgSv5aByHtxYj6sUs2v2ykKmaTzxm7tW9ZANizcZcbcc-3cHO1Vz2srN0iw_H6HNTowayi3cFyPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
شاهزاده‌ رضا پهلوی درباره اسلام:
🔴
من نه با اسلام دشمنی دارم و نه با هیچ باور دینی دیگری. ایمان، امری شخصی و محترم است و هر ایرانی باید آزاد باشد که دین خود را انتخاب کند، تغییر دهد یا هیچ دینی نداشته باشد.
🔴
مشکل ایران، اسلام به‌عنوان یک باور مذهبی نیست؛ مشکل، حکومتی است که دین را به ابزار قدرت، سرکوب و فساد تبدیل کرده است.
🔴
همان‌گونه که هیچ دینی نباید بر حکومت مسلط باشد، حکومت نیز نباید در باورهای مردم دخالت کند.
🔴
ایران آینده، کشوری خواهد بود که در آن مسلمان، مسیحی، یهودی، بهایی، زرتشتی و افراد بی‌دین، همگی از حقوق برابر برخوردار باشند.
🔴
معیار شهروندی، اعتقاد مذهبی افراد نخواهد بود، بلکه پایبندی به قانون، آزادی و کرامت انسانی خواهد بود.
🔴
اصل جدایی دین از حکومت، آزادی عقیده و برابری شهروندان.
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/67225" target="_blank">📅 11:31 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67224">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/226825be38.mp4?token=kPJNZKrD1d9zLU4JO5-T2oD7R3wau7rpmKSE4t0cjoM8YMWEJ4R0GjfH2Yl6fme85OVBRX1JToh7sE9IWBEQCrAw4V3yWpiN-JXwX_ZVel0W1RF_OIhW73kJ65syH_bVFi3Lgd1vc8HagEpeuFqMuyLU9wJ9vFpeSk6ZK9Vc6uHSrnQ6pjEjRYdvs9o4adpmzS5vbsOn_u5XB9u3_HHzZnbZWEPE2W3fMVX5o3tde0IOzbqYWVFHbYebkLo4WYIhvqM_a0Hyg8BnVuEHWl7Qk8-s2fO56X3DJILQrmj6pWsrYrdeQ2Z7yeOpo3XPkzWc-HcjB0YeFBHV0zskKJLFGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/226825be38.mp4?token=kPJNZKrD1d9zLU4JO5-T2oD7R3wau7rpmKSE4t0cjoM8YMWEJ4R0GjfH2Yl6fme85OVBRX1JToh7sE9IWBEQCrAw4V3yWpiN-JXwX_ZVel0W1RF_OIhW73kJ65syH_bVFi3Lgd1vc8HagEpeuFqMuyLU9wJ9vFpeSk6ZK9Vc6uHSrnQ6pjEjRYdvs9o4adpmzS5vbsOn_u5XB9u3_HHzZnbZWEPE2W3fMVX5o3tde0IOzbqYWVFHbYebkLo4WYIhvqM_a0Hyg8BnVuEHWl7Qk8-s2fO56X3DJILQrmj6pWsrYrdeQ2Z7yeOpo3XPkzWc-HcjB0YeFBHV0zskKJLFGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نریمانی مداح حکومتی:
منطقه شیعه نشین جنوب لبنان ۱۱هزار خونه صاف شده، آقایان چرا نمی زنید زیر میز مذاکره!
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/67224" target="_blank">📅 10:56 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67223">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OkcxWEyCtNAmz_XJmSlxRpgnWWmZxgL4h_I8WOHW7PXQGoG9pvPOPjpLfrU7Nx_5LHpAK1KidQzLO8us3RpaR_uRgdJlX5e8zS_qkigPyPmfwtW40UvLcNT9QHT3b0bv8w_-VfGubg7oXWK6cI5P25Pv0xDQe1uYJbyBetjLuWJ-4rqiJrZPkOtdxQGuaP0gfwAY-QdkAV7w0vef_amaOtuaLNEPldqVkncZPKkTjLjQ8aIvWSLfMAVxRWxoNdmF9VxQU3EsuR6zZbilLrsxXPk181wBlzqiaTSipXZcTH-NDMhI7TkEkcvzaF2xk3ul2LKMxK7zeR3w5U0WjzpyQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
گفته میشه بانو الکسیس پورن استار معروف اعلام کرده با مردای همه کشورا غیر 2 کشور رابطه جنسی داشته، ایران و غنا
برای اینکه کلکسیون خودشو کامل کنه، گفته فرم پر کنین و درخواست بدین تا یه نفرو انتخاب کنم.
از غنا 2700 نفر و از ایران بیش از 1 میلیون نفر درخواست دادن! جوون ترین ایرانی یه دهه نودی 10 ساله و پیرترین یه پیرمرد 78 ساله بوده
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/67223" target="_blank">📅 10:34 · 12 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
