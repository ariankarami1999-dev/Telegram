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
<img src="https://cdn4.telesco.pe/file/hPcx50AwDt5oNyv-C_yvlUfVjEgdqDRbv_QrwAAkl-mneZLe9IP0LG2O38v7EDn1w7TLvERJcewgzIAztRBXGIUEw0SkNN_zKHE9T6nLSD4UYEXRNJvk22yBrEIqzTdxaYKVt8GVghqnph7Na9fAyZ40luWZdggqdHtNXblQExWQdEe7k8zQlJQ-JCHCtByiDxwxcqOe65wWCMzs2-7rM5ce9AEtrkadXi7On-XvPzanoaoWX3mAZWZTxvY_FnWbSTTFtgOcoyzhuJhQ9XGWdiryG4HGnGPYX7MEqE_tcz1bFGwlag5Le3L01kxZ5urtmEnRTfg7NmTSdvQiF_EV0w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 190K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-18 15:21:46</div>
<hr>

<div class="tg-post" id="msg-67673">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae15a4dd4f.mp4?token=C-MdvsEP3R8NRDGHNlrFvWaK7-IqPqHjBmYfaielEGdhTZKyiAfnwN3tHxP_CJmEbMWBG-dFVqiDUpfGZwGQmqK0BMwrxQNyu6hx7JUU1Sbb88bglQMCU__jFScdOdWNe_diRRnjJ19oeWaTNdm0drrGeNEf_W6g1QlK2amglLai-APtHyNmzy1z_vVxZtjW_rCxWGrwXgLBMB6ceM215gGElNuG3jH8109OxXWemC-R3OqaY6KOb4HkvAt4QCC1FSikR_2wGNR-ZLNzd2sgRUhZzXUq8vLYoAMf8lxZpXy_em1TSjdt_D5jiUDXk8iBgarjAN0H5XhRZu14cQKogDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae15a4dd4f.mp4?token=C-MdvsEP3R8NRDGHNlrFvWaK7-IqPqHjBmYfaielEGdhTZKyiAfnwN3tHxP_CJmEbMWBG-dFVqiDUpfGZwGQmqK0BMwrxQNyu6hx7JUU1Sbb88bglQMCU__jFScdOdWNe_diRRnjJ19oeWaTNdm0drrGeNEf_W6g1QlK2amglLai-APtHyNmzy1z_vVxZtjW_rCxWGrwXgLBMB6ceM215gGElNuG3jH8109OxXWemC-R3OqaY6KOb4HkvAt4QCC1FSikR_2wGNR-ZLNzd2sgRUhZzXUq8vLYoAMf8lxZpXy_em1TSjdt_D5jiUDXk8iBgarjAN0H5XhRZu14cQKogDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
اسکله بنود بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/news_hut/67673" target="_blank">📅 15:04 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67672">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🚨
🚨
دو انفجار جدید در کرمان
@News_Hut</div>
<div class="tg-footer">👁️ 6.27K · <a href="https://t.me/news_hut/67672" target="_blank">📅 14:59 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67671">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🔴
فعال شدن آژیر های خطر در پایگاه آمریکایی "ویکتوریا" در نزدیکی فرودگاه بغداد.
@News_Hut</div>
<div class="tg-footer">👁️ 8K · <a href="https://t.me/news_hut/67671" target="_blank">📅 14:51 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67669">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hRz7vVKslJVLSYB6OfYBY2N-jzP0BN2gYFQD7PR4tMg3n3SsF7oh0B6Qkw9HJakytuIReoxPPr4Wzy-paMAaW8M7yP7F-ISqgcYw7avYF0STCF1HpzcGbZMr3x0o5SPK7NyCd1R6eXrwRsek2IqHmfBD2OnqODHy4_27qXwff517b6TJy7bB3kmMTWMXa7p2UwVR6s2jMOsTFr7-6w0tjMU8Fg0rT4N3AjAe0MkWfEl1zbbshivCSvbCHch9lP4q_4nn8RdyjfZlGnZGAyH32_pEPTJpVu_0okcobYwCqezziDg413Ga-MV_Jw9l_ycWwm7p75KUfKEd2OkTQEi8KA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q8w9KJjUe30YVEfPHLbRoPb_h9B5ee3LJcVvuv6-GZBgoLUTMtPVcXRONF3T5NoGSisMpI4pg0md7qyr7clYceJgUWjgB0R2nPTIvHiJcnnhl-vOLrIiXkLGvmkig19c0k44OsLoaNnmeDHJGQr-HLaT5tW5ZwFEum_ZoPM4-gIPtqxOK3nVxww-KlBy3RnDcszpSGmHktGkZwo5lMHDSZefLNETEbTikM1h_wAUOv4JSY_wloZNYOq39QA2gkIr-HIn7D4joywmbpbqEwqwz42wuuFi9MBRGYaey9yiBYtL2tdNe8SAlcMdGhUwsTwU8fzPG_aRvKdqTW0galspPA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
اسکله بنود شهرستان عسلویه
@News_Hut</div>
<div class="tg-footer">👁️ 8.92K · <a href="https://t.me/news_hut/67669" target="_blank">📅 14:47 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67668">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ptqKEGFqrf1dbbCbAMtpm_b6PKulP-CqlmHChPbI5MtDeMCAiZeXLqe8Njo1q9a4HaAOqFImAqhHfb3sfmInrfxpeRnal0CmL-8voONI7Ct27IKEZtWY-bDclXndywfLEM966zN2LNSRJC-LjcFSMGYiYVGCods7f_18ub6Fesx_U1iptEEw5p3sS23rmtktFjvVZOVDMBTmf0f4_8o6etCZvS-0FXctQjp49OedCFDdlx7QlWjIcW5fTOyNzJTTQc9RHBkN6UNCGetTBKMf7DCaEC8tHN_euG9s9lF0Ca-D2MrdA2wi5BPkg5RoNUyQBUbfBl1QFZ9pBXMGcsPOcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
شلیک موشک از تبریز
@News_Hut</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/news_hut/67668" target="_blank">📅 14:32 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67667">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🚨
🚨
🚨
گزارش ها از انفجار در کرمان  @News_Hut</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/news_hut/67667" target="_blank">📅 14:26 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67666">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iqIrv6xg11mmymbkGNYklRBLXp_lcK8p4RlfTPqEibIYVzm-zyylU-Ya_HydSkJ0tWLJ7Ju_jEXH8lZK_A5_iQBxMbIEITSu0KSg5ZRRorqJbppYDDDxXPEDUcRvyXcKjp3ccQKw8HqXOJMWuLdWk3xtMwNv0u6LaoRLIePetJZWcX2tXqK-zcSanbnv2H1Zw1gcTxQMuUDOnJy3x-ED9IarNNpitf-I5uI40ZAdJNNs8UQ7T14wWiiizqq7sUzQxm_BJeSSPmkmmTSvVJwFP0bKMPLqCFzaTIxkuMxg9Z3whl9e2WeZ2LTt5f9OgqWy0uNq6FyrltjATR2ymsoEhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
تانکر ترکرز: ‏
تهران، در انتظار ازسرگیری احتمالی قریب‌الوقوع محاصره دریایی نیروی دریایی آمریکا، در یک شب بیش از ۱۰ میلیون بشکه نفت خام و نفت کوره را بارگیری و ارسال کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/news_hut/67666" target="_blank">📅 14:23 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67665">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚨
🚨
🚨
گزارش ها از انفجار در کرمان
@News_Hut</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/news_hut/67665" target="_blank">📅 14:21 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67664">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0e2eb383e.mp4?token=Zv1Zjfts_yHmAGeJydjPRGpzbCp5MC4IiDnrAFZ0Dm_ekpeez8UfmHE0taNnF89UWx0IyVpyTUbgv2GnEqzCxmwiGSjgzuRfM2g6A4Uu99gj8aWaXQFwDHyL27hXi665qGgHYIFkapUBE2NKfWXo2XioaKb2DGbXmOgMgPGJnbzpyylTbxp9cFxe5vthKs7W5XCSiWPDBXfTVG7SvdZrHqkAY60HVWwSEr8dRS0BDf3s0RVIyLdPoc6ZxTDpIHGShfQ7u-zvqHhb3P5fUFY2pcHa_3_3-ZsaeAOVwfv2ymxcnFbsGZ-aW-VC4R1DVBfW-yckJiqPW3Zcq3cP-tG1FQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0e2eb383e.mp4?token=Zv1Zjfts_yHmAGeJydjPRGpzbCp5MC4IiDnrAFZ0Dm_ekpeez8UfmHE0taNnF89UWx0IyVpyTUbgv2GnEqzCxmwiGSjgzuRfM2g6A4Uu99gj8aWaXQFwDHyL27hXi665qGgHYIFkapUBE2NKfWXo2XioaKb2DGbXmOgMgPGJnbzpyylTbxp9cFxe5vthKs7W5XCSiWPDBXfTVG7SvdZrHqkAY60HVWwSEr8dRS0BDf3s0RVIyLdPoc6ZxTDpIHGShfQ7u-zvqHhb3P5fUFY2pcHa_3_3-ZsaeAOVwfv2ymxcnFbsGZ-aW-VC4R1DVBfW-yckJiqPW3Zcq3cP-tG1FQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
فعال‌سازی سامانه‌های پدافند هوایی در اردن و به صدا درآمدن آژیرهای هشدار.
@News_Hut</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/news_hut/67664" target="_blank">📅 14:20 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67663">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🚨
🚨
🚨
گزارش ها از انفجار در کویت
@News_Hut</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/news_hut/67663" target="_blank">📅 14:19 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67662">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1373fa65b9.mp4?token=gxCorWM3LrpgqzJIIBBr7NkqcOgqjit3hsRvGhS1g31ls3e8dlC93IUPc1f0SbMPlCmSnlvBNCVy4hp7fSL95yd1OJw5jU2aZlRlFlulGqAwGiKnpg4LWfVpKlbSbW11-Fd7KDPUbTXykcpcsYFlgJOphQOkxAd8VbnYJCoOODajL76IkjPItoqCpVCub_YY9Qd58DcuozhxbF8YfbaJsL2hRJtLOgljRklLc8jqW09BgblKg9Q8kP9O2KW2lUh2t_lwJcrm6taLb45okKjTXbIyiiu4zFrrxauUqjU-lMm32QVB6baejeh4DPF76oW1uJEyH5EH8v5wK6xClZTpMFVTiLLEkEP7L52AZrLKQ3fdkIkAlzGJk_ahyaOwel1a38ojgBtTEAjaMxi6GCr1z0waKbO3kX1gxa0wTQYm9pDlusAs7hGORTu8MhIwqCYt_9DLSSK12-L95H_CaEqluOe3e3kPVwKyudSUugJxpDGBxUfswMhcp9QocleprMJBJgGcHTfyMuw8iwuElRi_5SvAnjUnmgvfZ02MejNke7j3C4rE-h-B7JqAiW_OgzrDyemn--_fW5J55b-Sd_ovoQy4eM0EEUTpv46rbX2dIAqIuGj7yq0tfx4ym93c1PEKF2G1zr3SV3yAYH22IyA-1HIiyLecJ3274BbYemOE5l4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1373fa65b9.mp4?token=gxCorWM3LrpgqzJIIBBr7NkqcOgqjit3hsRvGhS1g31ls3e8dlC93IUPc1f0SbMPlCmSnlvBNCVy4hp7fSL95yd1OJw5jU2aZlRlFlulGqAwGiKnpg4LWfVpKlbSbW11-Fd7KDPUbTXykcpcsYFlgJOphQOkxAd8VbnYJCoOODajL76IkjPItoqCpVCub_YY9Qd58DcuozhxbF8YfbaJsL2hRJtLOgljRklLc8jqW09BgblKg9Q8kP9O2KW2lUh2t_lwJcrm6taLb45okKjTXbIyiiu4zFrrxauUqjU-lMm32QVB6baejeh4DPF76oW1uJEyH5EH8v5wK6xClZTpMFVTiLLEkEP7L52AZrLKQ3fdkIkAlzGJk_ahyaOwel1a38ojgBtTEAjaMxi6GCr1z0waKbO3kX1gxa0wTQYm9pDlusAs7hGORTu8MhIwqCYt_9DLSSK12-L95H_CaEqluOe3e3kPVwKyudSUugJxpDGBxUfswMhcp9QocleprMJBJgGcHTfyMuw8iwuElRi_5SvAnjUnmgvfZ02MejNke7j3C4rE-h-B7JqAiW_OgzrDyemn--_fW5J55b-Sd_ovoQy4eM0EEUTpv46rbX2dIAqIuGj7yq0tfx4ym93c1PEKF2G1zr3SV3yAYH22IyA-1HIiyLecJ3274BbYemOE5l4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
آسمان اردن
@News_Hut</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/news_hut/67662" target="_blank">📅 14:18 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67661">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be7cd95dd0.mp4?token=by_qLuAoLy444ditUoIzDFVt1LNl8JJShN5x6nn-7RJlpn5lIyMpfBYOLSFW2ZTZBg4regShUAo-g60nJprqMLAtl1UoD0piwgMy0brK4jxwI2hO1eu9oiVw53tk3yarSSfQzy5_RNqZWAmifdRJAXAgImTv_ZvwsKvai2dqfEnlp-rWSt8pxJZVMcraZARU1tE70Nyl0N9i24bSCTcRsvCXtProFFwJOk9Lp9K2hGN0WU5H-fgU4xGR2ge5SNXPs9Z8KNnHJM9dwSchDdqgoNrsME1mUOECvqgbOnQH7B8sJx8pAiGYzS-WSwmDHw62aEtwKDHU2jiz-z-ZJctAyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be7cd95dd0.mp4?token=by_qLuAoLy444ditUoIzDFVt1LNl8JJShN5x6nn-7RJlpn5lIyMpfBYOLSFW2ZTZBg4regShUAo-g60nJprqMLAtl1UoD0piwgMy0brK4jxwI2hO1eu9oiVw53tk3yarSSfQzy5_RNqZWAmifdRJAXAgImTv_ZvwsKvai2dqfEnlp-rWSt8pxJZVMcraZARU1tE70Nyl0N9i24bSCTcRsvCXtProFFwJOk9Lp9K2hGN0WU5H-fgU4xGR2ge5SNXPs9Z8KNnHJM9dwSchDdqgoNrsME1mUOECvqgbOnQH7B8sJx8pAiGYzS-WSwmDHw62aEtwKDHU2jiz-z-ZJctAyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ردپای موشک‌های بالستیک در شهر خمین.
@News_Hut</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/news_hut/67661" target="_blank">📅 14:17 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67660">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
🚨
نایا:
شلیک موشک‌های کروز به سمت کشتی‌های آمریکایی در نزدیکی بحرین.
@News_Hut</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/news_hut/67660" target="_blank">📅 14:15 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67659">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3cb5d140b.mp4?token=n0PGKZsEOpQ5PFRgQtZFJmqtwj2zbik2tPI2hnD8-TYT1uNMeOO3EwG4Pm1fMs-D_upwAIG9DXUvAOAqbJDQWF2wCag5r31rxLbSWw4fTW7W6bXijbCrCUU5xTT8rcHaM-B3znC3VldDWo_WACKcrXmB7JMeRETTrszoMftifb2HX_SOuxslzbKct6keKJjawPN38AkXQ45x0aQEf8efE47rDTLcgmN3IRAQfkGt5HidKeGzoY1jjw_SqIun9QfjOyJeSDCoxypeAfhflO6HAf6gvamMJEVbljdImBXx8-8GdCly_nbgQF95_joThBS04ZY05hmZ5RcSfyiJr-39pw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3cb5d140b.mp4?token=n0PGKZsEOpQ5PFRgQtZFJmqtwj2zbik2tPI2hnD8-TYT1uNMeOO3EwG4Pm1fMs-D_upwAIG9DXUvAOAqbJDQWF2wCag5r31rxLbSWw4fTW7W6bXijbCrCUU5xTT8rcHaM-B3znC3VldDWo_WACKcrXmB7JMeRETTrszoMftifb2HX_SOuxslzbKct6keKJjawPN38AkXQ45x0aQEf8efE47rDTLcgmN3IRAQfkGt5HidKeGzoY1jjw_SqIun9QfjOyJeSDCoxypeAfhflO6HAf6gvamMJEVbljdImBXx8-8GdCly_nbgQF95_joThBS04ZY05hmZ5RcSfyiJr-39pw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
موشک‌های ایرانی به سمت پایگاه‌های آمریکایی در منطقه شلیک شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/news_hut/67659" target="_blank">📅 14:13 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67658">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚨
🚨
نایا:
انفجارهایی پایگاه نظامی آمریکایی "الزرقاء" در اردن را لرزاند.
@News_Hut</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/news_hut/67658" target="_blank">📅 14:12 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67656">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K0Z4drlLg_tIqekvEUSvys_cZqRhm37k4P_GvLyc2Z93ukifiYbG5mZywiRt6DFoCmlC8DA1zc5i8vciRw6dRqRbYcioMAJslyW_IhGCdoEdby4kKOrhjtNm8r5CcAM5eczQzjFcQDhmE1UF7Aqqm519W7X-KcDgFEW9isNcPd65yV7O4m6XosuYf05kXJ5UD98xl7YsC-7ibu7uwtf74FMhpBIc1c7O_m40TVhfRuCLSTtoh-IieGTVvutTb7baocThDdGyegIlPerySmp39khyWBwCzhroEZCwmlwC6Vk1OGETAqrb-2OtEsdpyhVQwzmMyCdLg4k3GoJ-Sv22dA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XzntyK3wU0DVaJUEPrBVJw_1HGB0oZ7lyEWC5NYyGMumEoedLxeZWErlbkU2WRn0yHcsrt-cnPwdy14dif1_Kib-4NPbxC3l8hPM9VntnR_nNqosv0xZdKHXHT_I21HlVe-Tbjvv3TZ_4mMaZqARXzNeet6dQLbZUp4NeWO52m9JnSBhaaNxD-64pvpPNHy1QOvp4TIC5QqF52AVL0_-AjfSjPGrV4_R3X0cAKSIwvBEE3Vdzt3iXvOG5jKi8ijt47nvCIV2oTtaeG71SO38ogFoxX5e03wOWm-qP0KeEdzCoVHIF-pGr1Vmnj7afPPz6udY1AKDhgcTwkWBBhjKKg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
از الیگودرز لرستان موشک پرتاب شد.
@News_Hut</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/news_hut/67656" target="_blank">📅 14:12 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67655">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🚨
🚨
آژیر های خطر در اردن به صدا در آمدند
@News_Hut</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/news_hut/67655" target="_blank">📅 14:11 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67654">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FpFJeIATxCyvEvldAWWX4JOUiMoiaC7O_GQ_oE5tvgPCegXPrv6cCTduahYHmY0F0Dbk5GZ4kcK-QCcSdVdnz5HJV4RQJQkVD2-bxni88icvzZfpbzE__POnxjIqqTXI-IOwARfMBt7YTOE_MKVyb7X1rhBBFnJqsFq_3xTLawrsf0-vPJu3iPFMkhur2U9za8EGcjktqKFpEUZY84Z4xv_QhcbWmK1pnq9lMScLO1rwnEHuyjEomRq4cLR0-BzoOuWymhqiJP3kBXPTvt70OUdPPiFJhV3BB3mRlXUx7UY09YvtEd2orlKaVHsJ46jmtf9LcUzVJd3Hrrc3gFBvDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
از خمین و زنجان موشک شلیک شد
@News_Hut</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/news_hut/67654" target="_blank">📅 14:10 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67651">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MKXEK-2L9aplnzWinOdG3r1BP1Fz2zi1iqueSnGv4FKbQ8dyT5Slr78Xw2vELc3OSxst5yL3fUE5WHaWHZ9pLXlb7kJ0Y65lC3diPQCsO7Fxyw7UqJ0QKXxziKUAZKlfM9zlElao08rXY464XchS78MEBCajY75Cp8Rjuzmhw8FpCMVIZGpYk6DK-8OHOD_sp2TJb6TMSsxn3Bd8phd-i9hMKBFzxedA6HjgU40VsRiAJZcagqpOY_57Et-COTcXuizICBKTxBgWIH2o6DzDojPiDNuVucQ0tP8hvnqtaXBjfPVqe4A6ubMkjC6BVm1j9agsW7PpXsCS9k1EJtqKJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UdPw50F13GaRTzfYNL4KIHEHmAXqndT3wV70aNEUkXOXV5p0gJHVMfVBmEZjhH6rRxPwzGf6yBT2R__Zz0dnKOBavUznoVNB_gx84x_mlcTsnScJ82IORMTeH8yyIXJqKMejZF_xzrRRDUKTwEN8E4C23ygR85PEFrTVv1QurMuKgxSynAYsNxSKNlk7Gmiurxn5I-9LjVejXikNAq_cLDmSZKOvZNLSaAnS3LVlLYVRPVmVpbF52JLBK8mnxFrmf4nighIrzdw9SbrNyYBSP1zGP7X1J4VmNQEXonEbsUDlRTp3f-rDuylow9QimG6-GGu46yYcf-_wEGSoMFS9QQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i65SXitqmPGUo6iUFGu0DCNNAszxU_YZrrqLvYdHzpggTgTrn78uhd39prjwcXpnFD-Ml6EhUJLFl5SFOwSwevw-SwCZ9gBer6NTydFpcQqNMjfSQ_eecIySwz0nvbiv4fbHa2N8_f5NcbUnB1kBmNZO7yNdwDNLNIFJi_hP_J6ZfWxsztM_gD9m0rEUDnbzXuW27J9uxHI4BVZPHTjSKjjiYQHKrnZNr0ZzuiCeb4jllGNAHM1biz13uWa2oGtq2xiMUyyAc_5EQZ6CwVrzfjxj6XE8XqNFMD0p2efIRd-MjoNKtLP1nIEc0UjVqrbTs95Oyzcj1gTUwgZ8bAv57g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
تصاویر منتسب به شیراز
@News_Hut</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/news_hut/67651" target="_blank">📅 14:08 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67650">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
🚨
🚨
❌
گزارش ها از انفجار در شیراز
@News_Hut</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/news_hut/67650" target="_blank">📅 14:04 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67649">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
🚨
🇺🇸
مجدد حملات آمریکا به بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/news_hut/67649" target="_blank">📅 13:58 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67648">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
🚨
🇺🇸
بندرعباس صدای انفجار شنیده شد
@News_Hut</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/news_hut/67648" target="_blank">📅 13:52 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67647">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
🚨
🚨
شنیده شدن صدای چند انفجار در چغادک بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/news_hut/67647" target="_blank">📅 13:47 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67646">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
کانال 12 اسرائیل به نقل از یک مقام اسرائیلی:
طرح‌های تهاجمی آماده‌ای علیه ایران در اختیار داریم.
@News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/67646" target="_blank">📅 13:25 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67645">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🚨
🚨
🚨
خبرگزاری فارس:
دقایقی پیش مردم در بوشهر صدای ۲ انفجار شنیدند که هنوز خبر رسمی در خصوص محل دقیق انفجارها مخابره نشده است.
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/67645" target="_blank">📅 13:13 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67644">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🚨
🚨
❌
چندین انفجار در بوشهر گزارش شده.
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/67644" target="_blank">📅 13:07 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67643">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kEIzpfrbOHefyYfMjnEF47G0bV_UJgNlWBcZKhY5A__fVP91mfIR6KLuhPPKAffVAUDYgzh2QAsbSQNvXfL2ELwlrjXpeF__8T5XoOJ0fgHuxzwPowq2W8rhBPuqOjLfEz5TAkR_oy3MKhD6Nr7WLVUMGEiCW0QVRY2ePyQqjgoOj7UStieMo0gR8iFWInk-4ZExv49s5mX0eENIXwhIEgsDw2pHOZirpDs9rwouhf91gZuO1zhElU559KGoX-V02DSUWtBcLfrkzvJ2PF_HJdINQuPWBPxTLusq2j5daSgW_LtpiIkDcQGeUOO3hm7-d-LerAI57FCN7Cc5EhMrLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⁉️
اگه براتون سواله که چرا آمریکا انقد زومه رو سیریک:
سیریک یکی از نقاطی هست که بدلیل ارتفاع و موقعیت جغرافیاییش اشراف بسیار عالی به تمامی ورودی و خروجی تنگه هرمز داره. توی روزهای عادی و وقتی هوا تمیز هست شما راحت تا خصب(عمان) رو با چشم غیر مسلح میتونید رصد کنید. بدلیل موقعیت نسبتا کوهپایه‌ای منطقه سیریک نیروی دریایی سپاه با کروزهای ضد کشتی بیشترین حمله‌ها به شناورها رو از این منطقه انجام میدادند و سریع متواری میشدن. تمامی تجهیزات ثابتِ راداری و موشکی توی جنگ ۴۰ روزه منهدم شدند ولی نیروهای جمهوری اسلامی بصورت چریکی و پارتیزانی از سمت سیریک هنوز اقدام به پرتاب راکت ضد کشتی میکنند و البته خب سنتکام هم مرتبا با پهپاد و ماهواره تحت نظارت داره و مرتبا پیداشون میکنه و میزنتشون.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/67643" target="_blank">📅 12:43 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67642">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V7AGy89lmKvtUxhCxFLg2qq25BZosRfqCbATCxv39gT-72sjLYg9E_tuH8DOgr3Lc7CacWCOcGK62lXt7dG3uLEVaD-coQ3EnexHIp3ZlXYmUMlWk5HxpSOvzqysQzm0UMNFMNcpx1u2cYMNPoZT8B6uUGVwyy4n_QO9n0QnFLmS6QNCtoNDq4qYNWMungJY2mLp8NPnRXBqca-kKPynjosJh32cWRozaV_Os9d_S7Tl7dV_2Grs1lVZ4IhxoHSiACf6ArGEp6n8_eacSGzwuS45a3b5NUhoo4KARv9UC6TvqePb8XMbFopamIiEWRbYjOAR51xrPEs9fCo5hMkTBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بیانیه وزارت خارجه جمهوری اسلامی:
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/67642" target="_blank">📅 11:49 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67641">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
🚨
🚨
چندین انفجار در بحرین
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/67641" target="_blank">📅 11:33 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67640">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f84fc0204.mp4?token=rhsx548K9cldnTqC77EZSpuugZND38qKH92ZXK0Q9NUeOoM-BtSPWIdbOzJusA5Oa81UhfTEvlNk1y2HK_bzw_2rrVRoCNHzV69-_5f3NdlQSdKruABuonp0pmiXU4rk5TWMCMNEA4lsAzgJND1i74-iFPtzMVZ8LrhpkctgY7i_IdpXzVLpP4fLaoEGV_Bmgejh87-CJJzDOEc3qRP9X_02Qc0tmWxnO5P_JJsckA3V-U8DDQ-2qaDUZlV_LW3liztrs3i27idvipyD-1SlxDhNwOuLjFeCDwQE_GtffGidyDH7ym02wbutjEJaM16Wn2v_SHrt4yG-sN7xgReikg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f84fc0204.mp4?token=rhsx548K9cldnTqC77EZSpuugZND38qKH92ZXK0Q9NUeOoM-BtSPWIdbOzJusA5Oa81UhfTEvlNk1y2HK_bzw_2rrVRoCNHzV69-_5f3NdlQSdKruABuonp0pmiXU4rk5TWMCMNEA4lsAzgJND1i74-iFPtzMVZ8LrhpkctgY7i_IdpXzVLpP4fLaoEGV_Bmgejh87-CJJzDOEc3qRP9X_02Qc0tmWxnO5P_JJsckA3V-U8DDQ-2qaDUZlV_LW3liztrs3i27idvipyD-1SlxDhNwOuLjFeCDwQE_GtffGidyDH7ym02wbutjEJaM16Wn2v_SHrt4yG-sN7xgReikg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بدبخت یه چیزی میدونست میگفت شانس ندارم
😂
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/67640" target="_blank">📅 11:15 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67639">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d7a4381ac.mp4?token=gmH9NdUoLEYQTqEnjFuLVjw7LvLosG0HJh_zw2O7RU2fCZMbRTPHyfLQVqM0eLVUhYoDzXjSpSQVb4rxWGMlHxIr0roj0wK6WCDZ3UblDYrLu8Ssz027tjcqUDhBzPqEQCU7Qy7fLWORPhmt0jKMHrgz2SUoXD74_bK4C_ye069UDm8lUYdWvXqxLxPCF0qbSrMkIXuJqPhcIZr2_iRrCGl9NnNA1XcJvNohdOIDu_or_iX4BRLFo41LXcXn9SHMbEAdTWvt2ZytnohHmQqq-xl-fUSOcOz9labxEkFqx1xn1wMdhDu_ghIuUr33vSP_pXtif4esAXpZlHeIPMWl3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d7a4381ac.mp4?token=gmH9NdUoLEYQTqEnjFuLVjw7LvLosG0HJh_zw2O7RU2fCZMbRTPHyfLQVqM0eLVUhYoDzXjSpSQVb4rxWGMlHxIr0roj0wK6WCDZ3UblDYrLu8Ssz027tjcqUDhBzPqEQCU7Qy7fLWORPhmt0jKMHrgz2SUoXD74_bK4C_ye069UDm8lUYdWvXqxLxPCF0qbSrMkIXuJqPhcIZr2_iRrCGl9NnNA1XcJvNohdOIDu_or_iX4BRLFo41LXcXn9SHMbEAdTWvt2ZytnohHmQqq-xl-fUSOcOz9labxEkFqx1xn1wMdhDu_ghIuUr33vSP_pXtif4esAXpZlHeIPMWl3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏸
آخوند میرباقری، مرجع تقلید فرقه جلیلی‌ها و پایدارچی‌ها: دشمن به معنای واقعی کلمه هیچ غلطی نمیتونه بکنه، بنظرتون میتونه غلطی بکنه؟
مجری: بله دیگه، رهبر خودش این حرفارو میزد ولی الان کشته شد
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/67639" target="_blank">📅 10:31 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67637">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q4T4cvUx2wAj44U5QjBTZnmEEYit1209fAECxEb0nPn00gKi4Sov_GQnGs3rMnPmewhsZ_Wwt-BuKqQ38vg76LTlsjPGW2r15wPVJjsq9Bn5h75b0lYFiEBVX0CtUYUabF4iuwLnNwqbESxZm7LDaeDS9hl9W-VEokHf4JyCzHyH1cJFlL1vjeNu8y7qL3DEXQYNKu6eSiqjGrimeVenaoGDbzLvAEAn4RSwiKOhNhKs2lfrOa6UT_ocpYjJpo2kZSRvASol_TNPnVDF7T0p-4rwtlMs9SwA5ZVJD0Qt_cZwen082aX4SmL99Ie4dmhcjcK4IGLPtuq0E2nTYIVYxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0eec941b2.mp4?token=vbByqBpCPUvd8BBWYImGIWk3-gMyZQEUdU6X1OSg_8xoacg3LilKKcJZn21VikOuTQ4W0sbTgZVH-hLQ3aSrjFe60AxQZsFTy9e-1OM7T93R_pN69BHTwdNycmuKWXHaQwctsr329dfOomMbTsucQexauIGKGlf_xAvAjmXI1v1LYm5wRK9wJw03zhstK-05F8AC7CJLeIO3fpVPCWrq3KiHA68MuanZ1XBMbSzS0qGGg89YTE_cecxTr-9623FL5XAVgyDPxoE3aSJ2NazqDXKZZBQgPNJo1Y4KABS0trtOf9zqwYzg4IFUP8Nfn9rhavE46FbJS2KS7FWu-uNXXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0eec941b2.mp4?token=vbByqBpCPUvd8BBWYImGIWk3-gMyZQEUdU6X1OSg_8xoacg3LilKKcJZn21VikOuTQ4W0sbTgZVH-hLQ3aSrjFe60AxQZsFTy9e-1OM7T93R_pN69BHTwdNycmuKWXHaQwctsr329dfOomMbTsucQexauIGKGlf_xAvAjmXI1v1LYm5wRK9wJw03zhstK-05F8AC7CJLeIO3fpVPCWrq3KiHA68MuanZ1XBMbSzS0qGGg89YTE_cecxTr-9623FL5XAVgyDPxoE3aSJ2NazqDXKZZBQgPNJo1Y4KABS0trtOf9zqwYzg4IFUP8Nfn9rhavE46FbJS2KS7FWu-uNXXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
ترامپ خطاب به قالیباف:
یه محمدفلانی (محمدباقر) اونجاست که با بیل داره یه کارایی می‌کنه؛
ولی محمدفلانی، با این بیل‌ها به هیچ جا نمی‌رسی، حتی بزرگ‌ترین ماشین‌آلات دنیا هم تو شرایط فعلی نمیتونن کمکی بهتون کنن تا به اون اورانیوم‌ها برسید.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/67637" target="_blank">📅 10:03 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67636">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3353d5522.mp4?token=NRaqo06BhRuWS5eOpWWAc_bUryP4l_OdIIdJjfdRH5nbjLaVT0DLktU0rbcG_rEy6Oe3vvM8Q-pefY9do2CwOmIyjbOuV4QQGmfok2k0_lVm2l6DA-jrXciB7Fzh3ZEfXuCdwyFsvw4yUohxRXiGqTn4X9CWXo-C4wg45L_IC9borTfZsAek5npktlwWhA2-kd4VXErrIVL5hS3fYCSO3o-JEIyuXtzfC0FOR8PWIYOtSOxVklM0aitOEqrB0nqgiEFPp74nPEkgYS7OCGzgrrJCTiOa2D2HPorGCypM5025GPNsS6aU_DAheVNM5-eImbUdDRbAC2LoDrpOigjwdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3353d5522.mp4?token=NRaqo06BhRuWS5eOpWWAc_bUryP4l_OdIIdJjfdRH5nbjLaVT0DLktU0rbcG_rEy6Oe3vvM8Q-pefY9do2CwOmIyjbOuV4QQGmfok2k0_lVm2l6DA-jrXciB7Fzh3ZEfXuCdwyFsvw4yUohxRXiGqTn4X9CWXo-C4wg45L_IC9borTfZsAek5npktlwWhA2-kd4VXErrIVL5hS3fYCSO3o-JEIyuXtzfC0FOR8PWIYOtSOxVklM0aitOEqrB0nqgiEFPp74nPEkgYS7OCGzgrrJCTiOa2D2HPorGCypM5025GPNsS6aU_DAheVNM5-eImbUdDRbAC2LoDrpOigjwdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
فرماندهی مرکزی ایالات متحده:
🔴
نیروهای فرماندهی مرکزی ایالات متحده (سنتکام) در تاریخ ۸ ژوئیه دور دیگری از حملات را علیه ایران به انجام رساندند تا توانایی این کشور برای حمله به کشتی‌های تجاری و دریانوردان غیرنظامی بی‌گناه در تنگه هرمز را بیش از پیش تضعیف کنند.
🔴
نیروهای آمریکایی حدود ۹۰ هدف نظامی ایران، از جمله سامانه‌های پدافند هوایی، تجهیزات نظارت ساحلی، انبارهای موشک و پهپاد، توانمندی‌های دریایی و زیرساخت‌های لجستیک نظامی در امتداد خط ساحلی ایران را هدف قرار دادند.
🔴
این حملات جدید در پی اجرای موفقیت‌آمیز حملات تهاجمی در شب پیش از آن صورت گرفت.
🔴
نیروهای سنتکام در تاریخ ۷ ژوئیه حدود ۸۰ هدف نظامی ایران — از جمله بیش از ۶۰ فروند قایق تندرو متعلق به سپاه پاسداران انقلاب اسلامی — را هدف قرار دادند تا در واکنش به نقض آتش‌بس توسط ایران (از طریق حمله به سه کشتی تجاری در حال عبور از تنگه هرمز)، هزینه‌های سنگینی را بر این کشور تحمیل کنند.
🔴
نیروهای ایالات متحده همچنان هوشیار و آماده عملیات بوده و برای اجرای دستورات فرمانده کل قوا آمادگی کامل دارند.
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/67636" target="_blank">📅 09:21 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67635">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vsYO3zVw4t8cLOwouP5nBqa9fZ0DhvIjRu27N7zimgwjgLpGlorlTZ7rbyPvSbVY1NUxC36Qn3Pss69AKs1CG4R-Hd5O06HD0rZuUinhbKQolyo_GW49QSMNjbKZUE3bO9V3dtxN0JIan32Bl4VQRkpk3nUYa-rpC2DdTiVQmxlLijsIdwJKPaWtgmCnRZ2AJWN8Us_xE1Ayc5JiK05LfRpykgCLWlcQzUiilUtroPNDjf6SPWEOpyZ5jVSZbCRN_YPvSmusjgr3PhIV5hLrfyL4WlNl_cE9Fo6pGX5c85Bzm8ZCMv9ukct6Xke3QpUcUeHYFe1vJY1nuenpM_rqOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
وضعیت برج ترافیک بندر چابهار پس از حمله ارتش آمریکا
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/67635" target="_blank">📅 09:07 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67629">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GB95Mab-VDLxw1hC0_qTzXlkbwhHDuppy_WAmM7dj2_qPwqc2WDpiDpUYGafhyAdkC6JTfD1arpVSg3adOG-122NZDxhtqZNMzCWGlSyZ1XqKs7YO_NoiYSvtCORJJ3WzN9EXq5UdmcP9RRynKyYVTSLsP9qB4AutsVL0uhOiR-R0ZeqwK_fU_py1doNBd4gG3muxqcp70nlfi1D20CL2-Tiy2d5FL8IgpqjfRl03ArIJX4CV0lVnAJFqPj0GbzdqwL0TVgDZF8Imad4xfvcX8YWCCFtdRqr0AYLMLWCYWq-C44qh3taDv0GGaSZwFEZHnA7stKAI5inU3oEa9vdjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pov8Vbfwz1s-GPZSPX0XmLrvPw-HR6RgzaN-vHTsuhJ0q_NbFuoJs_zx8cEpXrCY4xgVIHLY876I_y2mA8jOtLqvSdKBClYBprv1BvvtOGJ5iex5PxKQ7RaE_DnTV-sFyWqvXKnqiW9_iV6qKrcAZF6hESzyCIsV1S3k_TEzVdWa1i_7wXOA9eyZRfHk6gr3JGMPJxTCW0n8QNujFba1kohSPCNknSCeO3hDQ_IgtRg5MbyUHfac0x7Nzkpu68G2ues8f39Kygw6HbBwgsFO5Iy0L5l-yZWV2d7RQWJ-fZ5yi2eBJRJ8M27FscAyiKOITFVjzsS3AbGJ20_MGygMow.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d64ac58e8c.mp4?token=v4ZedVRTnUWmJHu5lXrnKttgTKfPYIAhoRd0OAGiUx_9pjRos_im3wHG-8yW92-X1fJTQOW5y-Ze9D-n3pxEyHFjn-EEvusGHeTiDe_6yrKgsw_hrhKRq09tU78jSKakUrrOhksN4IRgPNO4d--sLFxcHn-mWTEj5gIKwYaDaKZEgXKQXrrernOsDAB6K1GTTv6INCe2s-K1_KTmNTkXY-hNfni_R-Qj3fk30Cc5m-fYOM-_UxcD8LN_HNbxJmuveW9s6kdEDZqWALM6V7j2XBUGAcE70BRv_n4CncVxaKFGHCQRN6J_jrjtUCnIQHA2UVMcIVDFF5Zki2QoC-8khw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d64ac58e8c.mp4?token=v4ZedVRTnUWmJHu5lXrnKttgTKfPYIAhoRd0OAGiUx_9pjRos_im3wHG-8yW92-X1fJTQOW5y-Ze9D-n3pxEyHFjn-EEvusGHeTiDe_6yrKgsw_hrhKRq09tU78jSKakUrrOhksN4IRgPNO4d--sLFxcHn-mWTEj5gIKwYaDaKZEgXKQXrrernOsDAB6K1GTTv6INCe2s-K1_KTmNTkXY-hNfni_R-Qj3fk30Cc5m-fYOM-_UxcD8LN_HNbxJmuveW9s6kdEDZqWALM6V7j2XBUGAcE70BRv_n4CncVxaKFGHCQRN6J_jrjtUCnIQHA2UVMcIVDFF5Zki2QoC-8khw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
تصاویر مرتبط با لحظه حمله و پس از حمله به خط راه‌آهن گرگان در نزدیک روستای آق‌قلا، پل دگونچی
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/67629" target="_blank">📅 09:02 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67628">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FuckBet @FuckBet @FuckBet @FuckBet @FuckBet @FuckBet</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/67628" target="_blank">📅 02:49 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67627">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qEJU9rkz96XVND6V6EvppLj6uQwbgG3-sEKSonmcYeCMequP6zRmqwm_Ur7MK6W7PgzabUx-Vzoy43n3p7E5oTM_7n9z926sPBSQ6dBwZZwXr4D9XF78L7rGNWzZfOGoX79m0_j-insVuS0Yo_o6LpkhMXG-OTpgSDrffislbQ6tIBt2f_wVzCyfT-k7c9RB8kDeGNu8U-j9cWLQKrOfCEdcnunUoRbFMyEzoiKgqN8YJqFmBoCXHKSbUNjITwq-BlmonkVHnNw6ldFJbaPM80NPyefb05WqVO63N7SpdTI-Tv8hhfiBfBGj2Wk0J75q0JBYf43Yj9Hb7ChQJ8rQ_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FuckBet
@FuckBet
@FuckBet
@FuckBet
@FuckBet
@FuckBet</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/67627" target="_blank">📅 02:49 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67624">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gg0rGcSO8kWazN2dmJcuR8VdfjfiqEcIW65DkwasRtl8vLmJhoYlroXxkBR4uT3cc15ox-oBdxFy773iJk1DbNX0nS30w3IH1nDNqnF_z5O4TI2o5HcmGA-s5WRb4esDefLKvAGA0SW62M_mxtfnxX0-T5ctTZzRa4UI7XaXAxcjNtJYKxonV8iUlPv31W5JOR0-Hq_ksycZA6nNDN9sXnwnkxfFEHKilCowIbEZ2opjL4pN5BvmVjC3jRFN8YrYlM9ea_kjsH5Vxmq5b1WjCpQfXd1RenA6rtEizCFgFTJ7eDH22wvMZTFAqAez0ad88l2Dl7RzKFMWWcwjVld3mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Jgf1MirOVnZxYYapBvQCsLmPDk76ZacVegVgIiPoMKON7r7FcslrpIE2sjtAh9YlAUJ7uRQrl_txwZumRJfwuwbbw-tLEzGsKBmq-M8AVWwyD-_HFGlfDP8_u3mqXgLH70pumLBnshIZRNrN-ztjKUQbdJhRehQm_Y6sPEQxmTufHeK2OlMBydNZ3f_BiUzmr3fLoMzRVsF5xaGaWfmZOG-HGmox83EcWhi7ZCRBsmB01KLyhywko9sE2Xi7owq5Vdm-rNlClxumFHfSYwpLZ2hQ64zxHDuqEZGcZ8Uu0YEGDP0yNFjJszzAuqEHniSN0Wi9a1l0ItH78AEcnEGg5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ENzd5fv3-3CqMA1J3C8Qgamcb2EwTAJZyrHFzdN-6DVvzlEhj_U-C8iLTJUnV_FM-r3QxGBfoATcoMmVyfIXzodGUJuwI4valKSPKyrSjCwqQXTGJA44RShjXBoxnXvjOeqGi-DHfOMnf32VCBD5iyzRpXxnUJtWSbwqes5wINSfmy3gShN42rrQmYruarCdDcS4JlUHC2MjSvRC_HaTorhOi02gwSN9GmRoiqs_GfhF-WGn8c1BQCKBIp1i5rhYmOwWxdHdv9he2cPdYQyLs3Xyzyot1p4tdRvuVTiX690UnvzfUNph8LY39Hx_kvh_-_Qamj-xxBdILTUvqK1xHQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
راه آهن نزدیک آق‌قلا در گلستان هدف حمله آمریکا قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/67624" target="_blank">📅 02:44 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67623">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be4f434f83.mp4?token=J0z6I9vm1-1TPMBZDZbILpDeQNCI9ulV6qwSERJAxRq2XmiCaE74C-RTsRQDMqHUXgJnsIEaB-staLom80ZXGF_CzGZFZp035i7BZ4ElCSIxaRk_gH_D3zNTqd0hGO4yaQK4VGG2ORMrUSJANoUjD5QLa5e9bioF9tc-6DDxkPVrIXYWzfaHuWA_sexiHV4OdfEt5M_9n907I1ePnbVXuaZyIhbxX8JOYekgkdNFacsu0DBYLyi-w1gIR47B8GAASDa4DdYACu73w60VXa_39PUxouz9T9K87IZk7A-TJb9f5BIDB2KDuMgjFzkIwBv8jGy3tIfuoCuSo3uSrGGGLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be4f434f83.mp4?token=J0z6I9vm1-1TPMBZDZbILpDeQNCI9ulV6qwSERJAxRq2XmiCaE74C-RTsRQDMqHUXgJnsIEaB-staLom80ZXGF_CzGZFZp035i7BZ4ElCSIxaRk_gH_D3zNTqd0hGO4yaQK4VGG2ORMrUSJANoUjD5QLa5e9bioF9tc-6DDxkPVrIXYWzfaHuWA_sexiHV4OdfEt5M_9n907I1ePnbVXuaZyIhbxX8JOYekgkdNFacsu0DBYLyi-w1gIR47B8GAASDa4DdYACu73w60VXa_39PUxouz9T9K87IZk7A-TJb9f5BIDB2KDuMgjFzkIwBv8jGy3tIfuoCuSo3uSrGGGLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
خبرنگار: اگر ایران خواهان یک توافق است، به نظر شما چرا به کشتی‌های تجاری حمله کردند؟
ترامپ: چون... راستش را بخواهید، این موضوع کمی عجیب است. کمی عجیب است. آن‌ها کمی از کنترل خارج شده‌اند.
اما آن‌ها واقعاً خواهان یک توافق هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/67623" target="_blank">📅 02:34 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67622">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/518cba3871.mp4?token=UQohQwcvxKp3RcR-qr6RqXfd1DZOXTQfTYczVZNxBQAY5QGsFn-M6wNxrET2uQuFvVQQvHMKFpf2xPQSXJdrHVZC6SVgyxeAwRuifSQTJgi_3j79LfHt_9nRAbg7vNa0AZ89S2lNBT8RAvr3qNPmBAPu9HoSXyBv2gnjnno493lAdxiT5XgZ4SB16UUrTcJEEDlj0aZ7TBBUJ7NVvYN3_Bhtjipfq-wwHNcw9JWp30-dnlPKPHybnlGld-UAleIPsaos2bAWbRTPZeWGN-7gr84I1ztrwDSHcotHQdoZx-vzwOuJf3JUC-YDxEyiMJc7M9B-8BuPsjRUHJ6B9mzVwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/518cba3871.mp4?token=UQohQwcvxKp3RcR-qr6RqXfd1DZOXTQfTYczVZNxBQAY5QGsFn-M6wNxrET2uQuFvVQQvHMKFpf2xPQSXJdrHVZC6SVgyxeAwRuifSQTJgi_3j79LfHt_9nRAbg7vNa0AZ89S2lNBT8RAvr3qNPmBAPu9HoSXyBv2gnjnno493lAdxiT5XgZ4SB16UUrTcJEEDlj0aZ7TBBUJ7NVvYN3_Bhtjipfq-wwHNcw9JWp30-dnlPKPHybnlGld-UAleIPsaos2bAWbRTPZeWGN-7gr84I1ztrwDSHcotHQdoZx-vzwOuJf3JUC-YDxEyiMJc7M9B-8BuPsjRUHJ6B9mzVwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
رئیس جمهور ترامپ درباره ایران:
ما از نظر نظامی، پیروز شده‌ایم.
آنها مدتی پیش با من تماس گرفتند. آن‌ها واقعاً می‌خواهند یک توافق انجام دهند. اما من نمی‌دانم که آیا آن‌ها شایسته این توافق هستند یا خیر.
من مطمئن نیستم که آن‌ها به توافق عمل خواهند کرد. این مشکل اصلی است.
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/67622" target="_blank">📅 02:30 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67621">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ba19bbdd9.mp4?token=R2sHnNSJCEfCIQWvRWrnxcu9wZXBBM4RKCbTEwEjC36w0N8TffvPHLJzuaj8TgXNiyUpJMwYgiwVI30q2dZtGE16lYis79GtZKcjnS-XzlxDkNkYvYLjviIrPf7IqgGhiBf-F1ROwGJae9TCS-zA_JmagrWJtHf56o1mc5syU2adLc0AGUOfVMBeIzmmTqvMg3diQjkrRPvyETQLqz-xdy3Mn4CSYq9J_Az3cCpPkYs2bOLFo4tNizdbF_cJ97uz-kvx6exFZbsIi7aGzzEU5bTO7grUoKwAkqeM73_ZSFPJMMFmcybeu81-SQiqAJXGnqJMHJy6SZod3VAxwgtzbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ba19bbdd9.mp4?token=R2sHnNSJCEfCIQWvRWrnxcu9wZXBBM4RKCbTEwEjC36w0N8TffvPHLJzuaj8TgXNiyUpJMwYgiwVI30q2dZtGE16lYis79GtZKcjnS-XzlxDkNkYvYLjviIrPf7IqgGhiBf-F1ROwGJae9TCS-zA_JmagrWJtHf56o1mc5syU2adLc0AGUOfVMBeIzmmTqvMg3diQjkrRPvyETQLqz-xdy3Mn4CSYq9J_Az3cCpPkYs2bOLFo4tNizdbF_cJ97uz-kvx6exFZbsIi7aGzzEU5bTO7grUoKwAkqeM73_ZSFPJMMFmcybeu81-SQiqAJXGnqJMHJy6SZod3VAxwgtzbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
رئیس جمهور ترامپ درباره ایران:
ما به آنها ضربه بسیار سنگینی وارد کردیم، و من می‌گویم که ما به آنها 20 برابر ضربه وارد کردیم.
هر بار که آنها به ما ضربه می‌زنند، ما 20 برابر به آنها پاسخ خواهیم داد.
وقتی آنها حمله می‌کنند، ما با قدرت بسیار بیشتری پاسخ می‌دهیم.
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/67621" target="_blank">📅 02:29 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67620">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db0d252421.mp4?token=F6Mja0n5xnhISHsT61jjk_1OBVXEyloGyR5tM0uHoMVGToknxSgizrLmmdHB7pOtGLnOYWGoU1VwWgy1-YbIFlDek4dvurLyOYZKd5rARSNZi6OQJb84OyfFa0f4deS5XQ1JNPBdpTHboaIpjp0vrg9syWnJQE3ONJu_FpMI7e8EFnoQmNen4ld-aG1vhP56n04iVT_mrWyYlX1JwN7CWsupknm0b8ybYDJKQUDHDscXmZ60pSpnJScPl2r0Limlp-vCg6CoTfW9m-kEMK6zXDZI49LHjiy824XQZ-46xXtFkRWTllm4HkUEfy6GIgJbSDTp6-CcfjyAC79Zp0LJyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db0d252421.mp4?token=F6Mja0n5xnhISHsT61jjk_1OBVXEyloGyR5tM0uHoMVGToknxSgizrLmmdHB7pOtGLnOYWGoU1VwWgy1-YbIFlDek4dvurLyOYZKd5rARSNZi6OQJb84OyfFa0f4deS5XQ1JNPBdpTHboaIpjp0vrg9syWnJQE3ONJu_FpMI7e8EFnoQmNen4ld-aG1vhP56n04iVT_mrWyYlX1JwN7CWsupknm0b8ybYDJKQUDHDscXmZ60pSpnJScPl2r0Limlp-vCg6CoTfW9m-kEMK6zXDZI49LHjiy824XQZ-46xXtFkRWTllm4HkUEfy6GIgJbSDTp6-CcfjyAC79Zp0LJyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
ترامپ درباره ایران:
من در صدر فهرست(ترور) اولویت‌های آن‌ها قرار دارم، قبل از شما.
اما اگر من [مشکلی] پیدا کنم، شما هم [مشکلی] پیدا خواهید کرد. بنابراین، شاید روزی بخواهید شغل خود را تغییر دهید.
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/67620" target="_blank">📅 02:26 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67619">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
🚨
انفجار سمت آق قلا گزارش شده
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/67619" target="_blank">📅 02:22 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67618">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
🚨
🚨
چندین انفجار در گرگان
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/67618" target="_blank">📅 02:18 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67616">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c35f85df80.mp4?token=v3__4mmnFme7n3zionxG6uUXLepFYu4ia2IRS380r9de9BL0C217NiIZMoLHLOrUXrXqFTuW6nMVglR0JAmLn6vLSw0kGCslBvSkTKTVTio_0bOOSr298oDtbr33tp7B5c704MBrOL6X1t_ziUB8OoYT6pYrer6yRRc9LkIawjXHW2zdp1d1oj0Cb6wZq2_d0EBImFOreFOi0jRZUXtlNqQx6iM3Gtm018mAtj0WrQxPgzQKScPXmZaSnhe7cAKv_OaTByMDHVa0bGfxl_txc2f7t7an8aah196oGJrLsUiLLs_kB_FtlLc7GtU0E2EQxbtappYdqqIbVwx4MqWXaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c35f85df80.mp4?token=v3__4mmnFme7n3zionxG6uUXLepFYu4ia2IRS380r9de9BL0C217NiIZMoLHLOrUXrXqFTuW6nMVglR0JAmLn6vLSw0kGCslBvSkTKTVTio_0bOOSr298oDtbr33tp7B5c704MBrOL6X1t_ziUB8OoYT6pYrer6yRRc9LkIawjXHW2zdp1d1oj0Cb6wZq2_d0EBImFOreFOi0jRZUXtlNqQx6iM3Gtm018mAtj0WrQxPgzQKScPXmZaSnhe7cAKv_OaTByMDHVa0bGfxl_txc2f7t7an8aah196oGJrLsUiLLs_kB_FtlLc7GtU0E2EQxbtappYdqqIbVwx4MqWXaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تابوت نوه خامنه‌ای رو با سرعت دارن کجا میبرن؟!
🧐
@News_Hut</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/67616" target="_blank">📅 02:01 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67615">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g0DTz1mRQH-_ZF3QcNaUPzPKPRTybhoa5jKovGU6haJ5EM50z_VhlHzJIf5kmiclsY3KGNzNtu4Yrd7LoFvbfcvW3YRT912g0BuZJZc-jvrra8AihadtsTMerF8W2yUiCV4dKn8KCb9e4IQEBnx8cyR6A-hY2gCVJ4K-5h0GF6NV92Hk4ia941ry31dRdMcfr27V1BOL47mNTCAhfTCuZeKzvTrYhDkxWE4oShpweRzHnTBRBT7r1Nw3gmxqS4Bj_9aWAzzLtnOENUv3ZXFUGArLc8Oj5Zx3Q_dO2-HDV_mv11yttIoZcwGM94XI_C-hnIosgI6sY9rGo_qLija78w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
نقاطی که امشب توسط آمریکایی ها هدف گرفت
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/67615" target="_blank">📅 01:37 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67614">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
🚨
سی‌ان‌ان:
آتش‌بس موقت با ایران متوقف شده است و وضعیت همچنان بسیار متغیر است. احتمال انجام حملات بیشتر بسیار بالااست.
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/67614" target="_blank">📅 01:33 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67612">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BcLoHwfiXdnhoT_0YBlBbjfdirce2X7LO3MyvpZFG6b4RFM1vmoDRs3HXCi21A7B6ZgRwDLkga8goMXF8SKWyK7QtIXuXr8grpiXtajXplVpyg_1FkPbc465WjnFnYpM4jWFFP6FGf9Oahtgv5q0F4Mn8EZhcBHfeQeRO55_EL9cQj5BOVoN3PX_sMMKsVTu9yCR4RmEPd-zVYn5-_-ajls9_F6nUug9eozmPUq8VZVwftipjOopQD3N-r9ouSLSu7YN4o74Z0HC5MY03so7eJ0d8AuhhFApR_KFfjgDz8MfXWKzH1H61R_FUwzZXp3GeT1Hu_ViVNGmL4Ayve8D7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e87cdc8ac4.mp4?token=lE1zZUvJhrMeRZMXVdJjQuLdVoLL5dJ_T02YhelxR__5szupH-ET14tj4Jclh66mMJmlf7AJdc2Q5lc6QJrIedQpB8kYi7w_wRaN_X0-DhTc7WvyCI7cQcsrfsrAlj3G6Lflo5n1Sml9WtLryyHaKj3QuKanyGaDjGgIRq5xjYDeAbPqDj8CwjgobxSZMGiFJC00kxgt84oIya6ZpbMBDyt8mY3qiIU3hBaeLkQweRAzewfInSEEwM6AQPs9N5gqv8xNrgD762E2ZgiT_WnpYqYe4Jfr5GfgsdXjMbYfBDM0hfeJase1JYRUFdlXGFAdlCVvY_AOsCq3--IAdvhlXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e87cdc8ac4.mp4?token=lE1zZUvJhrMeRZMXVdJjQuLdVoLL5dJ_T02YhelxR__5szupH-ET14tj4Jclh66mMJmlf7AJdc2Q5lc6QJrIedQpB8kYi7w_wRaN_X0-DhTc7WvyCI7cQcsrfsrAlj3G6Lflo5n1Sml9WtLryyHaKj3QuKanyGaDjGgIRq5xjYDeAbPqDj8CwjgobxSZMGiFJC00kxgt84oIya6ZpbMBDyt8mY3qiIU3hBaeLkQweRAzewfInSEEwM6AQPs9N5gqv8xNrgD762E2ZgiT_WnpYqYe4Jfr5GfgsdXjMbYfBDM0hfeJase1JYRUFdlXGFAdlCVvY_AOsCq3--IAdvhlXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ویدیو ای منتسب
به
حملات آمریکا به ایرانشهر( سیستان بلوچستان)
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/67612" target="_blank">📅 01:30 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67611">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lyvQOaESy4VINNR_v5j-kfxg57gfVLkLLnaNXUlW0ecrwMka7WoohEwRbqcwLyhkORb3oK_FxD1BATxmSUguJa_RG1ydLz0K2RbK8oDLolrfjv9JCM_Amf_JMw-JSiuAzl-YEnLcKaPw4RV5HfQ2qFO6gsD1gwz5be0O8wfVCZaAEDEOqywudqHKJIdFBho5osP91064m2JVrHeiAbiUX49Cat7ehul5ScTwnGupix7u0wLrDJ0VN2SLSpcvVGkc7YTWGWUr3L8h_mlhI8LFDmQAFj5qgwUTf7ClS7Sv0J1h9_tF0MIf6YmdclH_PHx3sdC89B2pfCddkECKKtnjlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
ترامپ :
این یک انتقام برای بمباران دیروز کشتی ها توسط ایران است. اگر این اتفاق دوباره تکرار شود، اوضاع بسیار بدتر خواهد شد!
@News_Hut</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/news_hut/67611" target="_blank">📅 01:10 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67608">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NqoNhfh3XY2zxq1k2mjhlF0cvJbcCZa0trxhhRFJJCa8gY6TASv7NbdaH-fviopT-pFajoCNIVBZ6xlrOGKz6ivdmhUEokLzr5CVzaH_oQuu5T00ZLt593YWBc7pzhDIeSixz02wk0UbRGJaGcR-LfIEQwv8R3rkEbq5bllIInSXU8EWg8hC76DxOSzED4KrC6FeHG64sbCdgLMnLNKmgtYsOZUOTgroSqWH0V2BfhwTW582lYUb2a4l_l9J3dRk5mq5gyVOznzP6EMtq1ELMUdQEs73MEdvGCJHsABA6Zxzv80I3MZN4syLw9ryMTP3epHW1-YVKqTpuJjjmgUcyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NsKQIUIAqcD2DEZgAz9mURBqTol5Xz0h-fAY3UPXaxewfaYo5xT-wT5_LF4f-OKyWKWhskr2Yboq7qxObgoFC8uWus9wsWdK1g-eBuspIZNah_cK9JIjxiUHwbHq1yuAMmB40Gcw6khgrZ49VboXWN8u0Lga-RjJH5MUf906fB2RdgGT65vUGF8FBtLsgB4VO-EkOzfqfBA9rxjZJA2LloFc6MP79loN0arqMvLKhpjvfUQ1fH62Sj-8DTRI-mlQA_v8nXJp_YlAiGphmwOafyL6LsAQIU_MEgcxQJ0CnwonghLx1hcWO8A_vb5WmUV9HLYyj9HdKrGFYOZiZjXS6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/a-xUowJeUfUhWUH05-Q99PPgmMMjlPv7dLm0YwYN4DdBPPct6h5Qb8Iqg5tiXpaP4MtNOTR_0kBKp6QEVlLhH8ftMr4XFrn_fjF2Ow5MNz9SdKv2IEhTmBmmdYnwGVXSTCy3xZl7ZC-8d3aEUbXnoOKEmpRHPQe5mwulYMJjuQ40kI74uU1nXUmddfT2WioW_PKIGHG40mWfM4qqx745K2dbvC-1NB9xY4ein38z8s9Thr5k1IViZQglR5aVrXZqmwQj6Fm1bOdjt_giJyf6WHErJO0v0EeihZfVSxvK-TVOAwaDVT9B4WbJM7n-9qbmdWsXqdnyo3NFuCgXtCjiZA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🇺🇸
ترامپ تصاویر حمله به جنوب ایران رو در تروث سوشال منتشر کرد
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/67608" target="_blank">📅 01:08 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67607">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">دلیلِ این چص‌حمله هارو متوجه نمی‌شم واقعا، آخه کسی که زدین رهبرشونو که از نظر اونا جانشین امام زمان بود رو کشتین، اتفاقی افتاد مگه که الان بخواین با زدن توالتای پادگانای سپاه اتفاقی بیفته؟
صرفا این حملات شرایط اقتصادی رو سخت‌تر می‌کنه همونطور که امروز دلار ۱۸۰ تومنی رو دیدیم، خود ترامپ هم می‌دونه تنها راه حمله زمینیه و اولین نقطه هم خارک ولی جرئتش...؟!
#hjAly‌</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/67607" target="_blank">📅 01:06 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67605">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9864e05e49.mp4?token=csjGN-8UoA8COTG3t3F-12WslJwFyhNI_fgCwnQYO4ugZWoLRl07uH876KrPlXws50UBcabqQgjnRaH5H9hrQJkNFD1-lzvnWdRRubADT3wwRG9YalgHH1YsFlm_8-5ImzzrH-bd2lBEgncErpADxGaqJFfKs0eJuh-_B1-i3hEyAC4E8PaOuxgovPzKEueSoyFsGVfyeP_2GJ3oSiUfP_1hNsRI1je-6pU-xVAWI_04KpzZ03c0bJz4rw3KVwCnJbBclW0te26BoNfu1oKYppnKnG4GsZkkAATaLkZYoWhZb_Od-1q1XxHac7fVnYpu5c14EP50OKbgD3guKD4XFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9864e05e49.mp4?token=csjGN-8UoA8COTG3t3F-12WslJwFyhNI_fgCwnQYO4ugZWoLRl07uH876KrPlXws50UBcabqQgjnRaH5H9hrQJkNFD1-lzvnWdRRubADT3wwRG9YalgHH1YsFlm_8-5ImzzrH-bd2lBEgncErpADxGaqJFfKs0eJuh-_B1-i3hEyAC4E8PaOuxgovPzKEueSoyFsGVfyeP_2GJ3oSiUfP_1hNsRI1je-6pU-xVAWI_04KpzZ03c0bJz4rw3KVwCnJbBclW0te26BoNfu1oKYppnKnG4GsZkkAATaLkZYoWhZb_Od-1q1XxHac7fVnYpu5c14EP50OKbgD3guKD4XFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
ویدئوهایی از لحظه حمله آمریکا به برج کنترل دریایی اسکله شهید کلانتری چابهار :
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/67605" target="_blank">📅 01:04 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67604">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
🚨
انفجار های مجدد در جزیره بوموسی
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/67604" target="_blank">📅 01:01 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67603">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">ماشالا ترامپِ شیردلِ مادرجنده‌ی املاکی
😊
#hjAly‌</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/67603" target="_blank">📅 00:58 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67602">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
🚨
🚨
انفجار در بندر کنگان
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/67602" target="_blank">📅 00:58 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67601">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uU_alDdhylbjEtmUmhY6-uYJn8084sSDa_MnelANJ-juxCCc17l60QRJjmQeJiFpiRy512yec25KYBgiY21dl50PaKKe9oxM1ul_qKzXpfzkracT29UZ-ZRBz38n1YcWzxP0N9HUXXzEuYOLZ347tcO2-PLDUo8Nguhw6ALhOz8PGgIl0M7Kbjo71vsloxJQgP6yNPv3vNzg0XqrRq7sjb4g9ZIXaYput67TKUZF6-tkZsUZpLG1M2Dg3kHwPvP5pz_ilLfz7b5Fr4ENJndeKcmt3ykCyKxu_6OjdNhpBazxjaBtVLVdJxoIeRJm_cW_j5zjWwx1XlWE4XognKv_0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
یازده فروند سوخت رسان نیروی دریایی آمریکا بر فراز خاورمیانه
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/67601" target="_blank">📅 00:57 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67600">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MSHtix8pdSXh-c4b_NQtV8b6NvWRGCtFdH6bfSNBckfzBQY3W01jtLMeblnT1wxnOrKtQA7IvwkP_u-7Zzl4slgBppEPeOzv-F4N-r1XniI8_h4bnkvQb2Mg-u9KKh0DcU7Ne81uXJ6-hLDXS4Kmic9j0VWdDcMt5uGb7nOp03VS5apMGRyKVPMzrmYDxmNMZ0F8F4xH9dfKexz0vlDK4QxJkw1rPHCOr1nVxStBqHv_qKAMLEOjev_q8bmOrkn0K6iWagXQ6fmL-wqHmfo3RgGvkH7cf50WH17rtnoPB9QlgNtpzKTglZhcZ9m7cUbGMmlqwScs1CJ0TPWVEFKHqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
وضعیت شهباز شریف بعد از حملات آمریکا:
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/67600" target="_blank">📅 00:53 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67599">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🚨
🚨
صداوسیما :
نیروی هوایی آمریکا در حملات به چابهار، اسکله‌های «شهید بهشتی» و «کلانتری» رو به همراه برج کنترل ترافیک دریایی این بندر هدف قرار داده.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/67599" target="_blank">📅 00:52 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67597">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Sfv14OsARmmjnOAAohHL6wLlq1hpVXPUpiWMmR9yd1JHh7GTHvZ7na3BjI6RTTJ7azf3r4QcS3wiuqCGU5J-yxUoh0LfcYQqaJIBfBzEHIBymhThN-Z-MiJzRWPXQNjfzmS7SJlFkdXh2cXZ0E8J0IjGGMTHLPjeotZLRbnR0JjVaXxEvMBVudUSVcgmnRDHAmgP86mT4CN1QAEJx3jgwnmrvWfW-GWLYGM_UjuVMqawBTMOTCpNldeOZ2LSW7adJffu1HiWUbfD5g-EwNxkimopGOWV66j5qae5qUWscX4QCsdzlh9J0zGz0VcoZFSUIo96ZhQq5OosRFZmw3M1lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kQSQBJhIh68u4ovyhS2hN7jxdJGhttCFi_Aogf-RrIRguLwbKuE4NQ5mEt0HOWwgsfYuDG3qDiixzIGV3uMrZEgKT_l7FUltLpgzh_--fZpDNECGFWS2vp79K1nV0ac28v9l8go2Pes-ALWCkJPNsai-iSD7HKbX3Pf2hEIQkJ7mpgIizyxJVpCIvAAjwTxqilI0goYtJQV7V7IqvCPXAUx3KRi6w-9lQ2C5Dr68MCMIx7UlLB3Ehn6DUsM3lbesaP2YTUYCBNKI_nzeSQe_KcxGMIETs_OQyRpOHbK2C1edQQMo7aBkOiTIsms6psrAXo0jNNe7n5EtQCaYNLc91Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
برج دریایی اسکله شهید بهشتی چابهار
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/67597" target="_blank">📅 00:51 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67596">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚨
🇮🇷
محسن رضایی مشاور رهبر:
دشمن متجاوز و همدستانش به شدت تنبیه خواهند شد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/67596" target="_blank">📅 00:48 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67595">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚨
🚨
دقایقی پیش مردم در چغادک استان بوشهر ۳ انفجار نسبتا شدید را حس کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/67595" target="_blank">📅 00:47 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67594">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
🚨
چندین انفجاردر بندرلنگه
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/67594" target="_blank">📅 00:41 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67593">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚨
🚨
فعلا تمرکز حملات مربوط به خط ساحلی جنوب کشور بوده
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/67593" target="_blank">📅 00:39 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67592">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df60497304.mp4?token=RalCVAbpajsCyXTmGVPfHpFZScojaXwXM1KCpsEvvv2d9seFETWr_9H0sKVAtlDZ7XhsLCeCe--pW5M3Ajzb-62A6pnAfeHSSei8hK-Wvm21ZqJyqmbcXzde7fqaxuTqoqzyMlcSG2GxqWjk3KlurnPgzCOdFqw1yljZZmG45hwolFc3wFKuOsB205truIm_D_jJwPeo-cI_t3VLLR7UqDZfWrTIWfd6z843bAHzDQhv35P1d3W1MCMIc16WfPyvrf768OEQU0_J8E-A8AIfLmxsyJHpRXsVLzYcnnK0uMIi6Q1XvkOvQ2WC_ivdHJpUFgpyu0Vrb9WKAvKPh5ZG2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df60497304.mp4?token=RalCVAbpajsCyXTmGVPfHpFZScojaXwXM1KCpsEvvv2d9seFETWr_9H0sKVAtlDZ7XhsLCeCe--pW5M3Ajzb-62A6pnAfeHSSei8hK-Wvm21ZqJyqmbcXzde7fqaxuTqoqzyMlcSG2GxqWjk3KlurnPgzCOdFqw1yljZZmG45hwolFc3wFKuOsB205truIm_D_jJwPeo-cI_t3VLLR7UqDZfWrTIWfd6z843bAHzDQhv35P1d3W1MCMIc16WfPyvrf768OEQU0_J8E-A8AIfLmxsyJHpRXsVLzYcnnK0uMIi6Q1XvkOvQ2WC_ivdHJpUFgpyu0Vrb9WKAvKPh5ZG2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/67592" target="_blank">📅 00:35 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67591">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
🚨
چندین انفجار شدید در جاسک
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/67591" target="_blank">📅 00:31 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67588">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tQZlDBOU3v5W4wLZ8rc5yGp5MTWw3bWQXaarVqk-MRAkveCz6JFFG08vUI4uq8fxtnLeN-UL3Kzv3-glD7fQ2IPaotxR9U3HPAPnS2GICU8ClhVGuqON5l83i9ultQ1ebLkFaHC0KhF-3ph0tmuUi4B2lebjpvzES1AlOsc2ZxCP7ebNZ80ZcWx5NgNt2JSJuERrv7WTXQUWW8W-F5-jPIHZv0OTmyF_VwWR7xO_1jall_Do6MP1N_LiUqrbkGhHA4KtgNbb_DJidINjGfuycCaNDa6M2f-R_d3NLLDlHnj8u4dl75WfJJsEBsd06z0H63zowY0159t2J2buY0u8Hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6afb0f1898.mp4?token=FjWM0t5oIklLTz-GpVipLJ8jtjf7ycVUHHeam79ggEM8z4x3yJaR1Rc5YaTh4A7J2lWl4kuXWKFP8B4zMNDC2sbfnn0JHdQoBgoa6nO9LDELxnm_CX67iTJj16Ahj89JeLgwrxWbCH52Dsm6j_f4LCPSY9nV27hxLyZdPNiDB3_OA1mLHObQyPlN3OylKtekL-arVJHyb0Eidicp62qD5ehTVk_sgF4Iln-CiBkpL3W8s13KPyQTHLBJUU41AbXVPYOG1YfBoGlg5KLAfWOOV5ubb8tMktSa38Pgt7SEahpxan1FTmB540Fbov1EmpXX9lPIt_uqcZ9NsKh-q0eNmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6afb0f1898.mp4?token=FjWM0t5oIklLTz-GpVipLJ8jtjf7ycVUHHeam79ggEM8z4x3yJaR1Rc5YaTh4A7J2lWl4kuXWKFP8B4zMNDC2sbfnn0JHdQoBgoa6nO9LDELxnm_CX67iTJj16Ahj89JeLgwrxWbCH52Dsm6j_f4LCPSY9nV27hxLyZdPNiDB3_OA1mLHObQyPlN3OylKtekL-arVJHyb0Eidicp62qD5ehTVk_sgF4Iln-CiBkpL3W8s13KPyQTHLBJUU41AbXVPYOG1YfBoGlg5KLAfWOOV5ubb8tMktSa38Pgt7SEahpxan1FTmB540Fbov1EmpXX9lPIt_uqcZ9NsKh-q0eNmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ویدیو منتسب به بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/67588" target="_blank">📅 00:30 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67587">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac1596adc1.mp4?token=o3DeFMcetKpaoe8e9Ox1C8TapuXu4sW607bDxBKYotMS9SQRwUQp89JqI3_-2Qsss0FWYBPcWpBl-LKz_duOgxe2O3JTi-5ETfCB5MvZkkQIx5JoCoS6tHOFw0eqITuYvkUcxSvrKbIJ68jerQGL5LFARDIuukKQflcqfJ7b385gJMstw-Mis1kmcUsydJCogE9AQCWz6avLAXTFPk441TcgZWoA3djUMWFMmMsOt5bGVJYFtWQt6t2UCRT9oQhyKTRIhtuIEvBpCm470ET1XYtc-f7tcRNAhJvVxGGUOXmYKye-dWFhmsHpZd94OEUt2cz45ehqshpJCKRcYz7KLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac1596adc1.mp4?token=o3DeFMcetKpaoe8e9Ox1C8TapuXu4sW607bDxBKYotMS9SQRwUQp89JqI3_-2Qsss0FWYBPcWpBl-LKz_duOgxe2O3JTi-5ETfCB5MvZkkQIx5JoCoS6tHOFw0eqITuYvkUcxSvrKbIJ68jerQGL5LFARDIuukKQflcqfJ7b385gJMstw-Mis1kmcUsydJCogE9AQCWz6avLAXTFPk441TcgZWoA3djUMWFMmMsOt5bGVJYFtWQt6t2UCRT9oQhyKTRIhtuIEvBpCm470ET1XYtc-f7tcRNAhJvVxGGUOXmYKye-dWFhmsHpZd94OEUt2cz45ehqshpJCKRcYz7KLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
❌
لحظه انفجار در چابهار
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/67587" target="_blank">📅 00:28 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67586">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚨
🚨
دو انفجار در جزیره ابوموسی
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/67586" target="_blank">📅 00:25 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67585">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9f9c6b6a4.mp4?token=Ijjn8tdlPGsYYbrOefPcVD6bCn_xfEfx53jbT9iU8reNJM3eyGfa5vMVzLvhZt2h_DFcyI99P7hlCqCFJSV3MvwEEubQtYM-oCiEZT1vim7ophPjeAc2vox2BHASAejiTghK1SWOTgawxPfqpkvWcMGA516jDqK9VZbK2b76ZeqxKoA8L6FYSiTE-60PTu-nCT3eRPKbc9vKRbeh1ZPqMOdgXOEdEh4DWgomL-lbO7rIjJRLYyv7LMFVpkNol0_u3F4MndaouNmy8AzCq89r8GKebyHIU7oZzeFeO5wxyKE88FsVlVjfJKHRKurvPGDTa5OMzhnaF7Rc8XOEzVp1UQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9f9c6b6a4.mp4?token=Ijjn8tdlPGsYYbrOefPcVD6bCn_xfEfx53jbT9iU8reNJM3eyGfa5vMVzLvhZt2h_DFcyI99P7hlCqCFJSV3MvwEEubQtYM-oCiEZT1vim7ophPjeAc2vox2BHASAejiTghK1SWOTgawxPfqpkvWcMGA516jDqK9VZbK2b76ZeqxKoA8L6FYSiTE-60PTu-nCT3eRPKbc9vKRbeh1ZPqMOdgXOEdEh4DWgomL-lbO7rIjJRLYyv7LMFVpkNol0_u3F4MndaouNmy8AzCq89r8GKebyHIU7oZzeFeO5wxyKE88FsVlVjfJKHRKurvPGDTa5OMzhnaF7Rc8XOEzVp1UQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
هم اکنون؛ آنتن زنده شبکه خبر
رئیس کمیسیون امنیت ملی مجلس: آمریکایی‌ها بدانند پاسخ کوبنده‌ای به آنها خواهیم داد و امنیت را در  هر جای دنیا باشند از آنها سلب خواهیم کرد
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/67585" target="_blank">📅 00:23 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67584">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/36b350a9ac.mp4?token=M3DWAicUmvaldFRPZOc6PY-RegE21cNrVl5UqaIdTtpsOt9F8XH6yIgO8HzzkEwDqOOu94C12cqJlxMqrkf740PT9eBu6FzNJgxwYrHp4tfeFGk-KxYo8lqjVpd52Q-0houV8Vua3TcLSZBeRcNCxjzdqMoHVk2-nfhzNJF6mqg9QiUpSHcTPKkQYJzsDcnU7riwhrvT3ZGvYhcQgvm7qN3xfjmbbsGXVy-8PkxGAO_4EbrEkdx1BgXlNpxh1XtaXtyqkWvdGhJaT3HOQVTM8uvOJeIrBtGP_hW6GlUIALfCG7ViV-S2i9C3QjCRu8aowU0iOEtGk1TEBls3hbIkIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/36b350a9ac.mp4?token=M3DWAicUmvaldFRPZOc6PY-RegE21cNrVl5UqaIdTtpsOt9F8XH6yIgO8HzzkEwDqOOu94C12cqJlxMqrkf740PT9eBu6FzNJgxwYrHp4tfeFGk-KxYo8lqjVpd52Q-0houV8Vua3TcLSZBeRcNCxjzdqMoHVk2-nfhzNJF6mqg9QiUpSHcTPKkQYJzsDcnU7riwhrvT3ZGvYhcQgvm7qN3xfjmbbsGXVy-8PkxGAO_4EbrEkdx1BgXlNpxh1XtaXtyqkWvdGhJaT3HOQVTM8uvOJeIrBtGP_hW6GlUIALfCG7ViV-S2i9C3QjCRu8aowU0iOEtGk1TEBls3hbIkIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
لحظه انفجار در چابهار
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/67584" target="_blank">📅 00:20 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67583">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b02d221609.mp4?token=XDGPmhZRlFUZyckSGeDZAX1c9vAyK5EhavePGxsp9bW-7X7f87sKXUYhIElGBz3mxZOkAQ_KvAYlV2NrwHUF-E9g7FsPmRcsrPOsm1g5BmqgKjmgGHdHmJK-9eRe3YE9NPjlqI-KfUg9blZSzkqwVd_BVNOjrKt9SNUR2VIj2Jg7RIF-el8U0Fox3o_Qq8J12okKGvJ6-qLtE5LzH4__GDV6Q5exoYR9v6_Rjv3Gb5wpBak842kNcZ1z3D4vayCLQx2BcG8Rq4cKazE__-2DOHKvGIXJuayzSVrEVMZ0_aXPjuyQdSpiKBPL8rABW9fOkQm8dA8zsSZG2ZeUnX2ZOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b02d221609.mp4?token=XDGPmhZRlFUZyckSGeDZAX1c9vAyK5EhavePGxsp9bW-7X7f87sKXUYhIElGBz3mxZOkAQ_KvAYlV2NrwHUF-E9g7FsPmRcsrPOsm1g5BmqgKjmgGHdHmJK-9eRe3YE9NPjlqI-KfUg9blZSzkqwVd_BVNOjrKt9SNUR2VIj2Jg7RIF-el8U0Fox3o_Qq8J12okKGvJ6-qLtE5LzH4__GDV6Q5exoYR9v6_Rjv3Gb5wpBak842kNcZ1z3D4vayCLQx2BcG8Rq4cKazE__-2DOHKvGIXJuayzSVrEVMZ0_aXPjuyQdSpiKBPL8rABW9fOkQm8dA8zsSZG2ZeUnX2ZOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
منتسب به بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/67583" target="_blank">📅 00:17 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67582">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
🚨
نور نیوز  :
به زودی حملات ایران شروع میشود.
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/67582" target="_blank">📅 00:16 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67581">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c578ded4b.mp4?token=BoUJPUAJIQpUSoc--7zzCksoag4ZiWEcB19hU7FyhymYFNOFs3bAbhL3INZdhkLiM18uTfsD9AdX_LmaIdLeaBoN7NJHR4antjfp56XlX8Ah7-7VVe4Cj3UK0k4EncInj3PpOKx5sI0wGM6dPfNp1P63k8-hgm4rAukWeGE-ftZn9Xex4VYsbcmJePZo2EW3TXzA8-Z_C-Qw6cYWZSeJX6D0QNWdks1MfwFE1AboACp9UAP0Ro__XX-z0un09sQR7lAS-55fH_9kqXtCN1xAExpaF13joXtRQ21jbB4PLSeYGWHx2OvrYh_GyvwO9F8vIp9XkjIgg8V1ksIkRqCOYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c578ded4b.mp4?token=BoUJPUAJIQpUSoc--7zzCksoag4ZiWEcB19hU7FyhymYFNOFs3bAbhL3INZdhkLiM18uTfsD9AdX_LmaIdLeaBoN7NJHR4antjfp56XlX8Ah7-7VVe4Cj3UK0k4EncInj3PpOKx5sI0wGM6dPfNp1P63k8-hgm4rAukWeGE-ftZn9Xex4VYsbcmJePZo2EW3TXzA8-Z_C-Qw6cYWZSeJX6D0QNWdks1MfwFE1AboACp9UAP0Ro__XX-z0un09sQR7lAS-55fH_9kqXtCN1xAExpaF13joXtRQ21jbB4PLSeYGWHx2OvrYh_GyvwO9F8vIp9XkjIgg8V1ksIkRqCOYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ریشهر بوشهر دقایقی پیش
@News_Hut</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/67581" target="_blank">📅 00:11 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67580">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fce96b4303.mp4?token=Qir37047pMcygE16w783lec1E2BDAk5yXzM3Dd8cdB8B5Nh5T1HVqcsnPXNGnbfnS9oEJFcUMxefGz4zEDrRC_ZNGTpUeoSTqmHVaBez-s9DsT1BUb6JVZzxA2EzZ2QXcPjaMEJ2zDiTjs05IQHyLzM4xij7Xz18cFjMQ52NpLI02Et8RNdsq5NSj-xNmWSA5be87_7jdvaTI7SR6q5tq9drrI4zh1lGV_8KEByOwG71YZbKNpv13MofwYxwMt27oSI7O-90kjNsRH-9QA9h0VFSXYgdK6468Xlxnsz3I9iRGTLHI7d5aoopHZh8fkpGxiILh2-i-JegCfhqo2fCDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fce96b4303.mp4?token=Qir37047pMcygE16w783lec1E2BDAk5yXzM3Dd8cdB8B5Nh5T1HVqcsnPXNGnbfnS9oEJFcUMxefGz4zEDrRC_ZNGTpUeoSTqmHVaBez-s9DsT1BUb6JVZzxA2EzZ2QXcPjaMEJ2zDiTjs05IQHyLzM4xij7Xz18cFjMQ52NpLI02Et8RNdsq5NSj-xNmWSA5be87_7jdvaTI7SR6q5tq9drrI4zh1lGV_8KEByOwG71YZbKNpv13MofwYxwMt27oSI7O-90kjNsRH-9QA9h0VFSXYgdK6468Xlxnsz3I9iRGTLHI7d5aoopHZh8fkpGxiILh2-i-JegCfhqo2fCDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
لحظاتی از حملات آمریکایی به شهر چابهار، ایران.
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/67580" target="_blank">📅 00:09 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67578">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/prBKi6yZ-l1VuuerKZML3S0ffrsZWdvtgLId32mgWuQ6qa4ZBwTjtR0V7oPbAwNMhNj3jAjJH0hvcXjXn91BCWO1E_JNF3fuEnOdhIdDbRVW3JNrIOfx3rc09A9KVIHk-JJgxxswnv0UT7KeLBCWEI9MVzETL0TEeyOFuCAaMYyDkOsp5YaU0_sM6HDL1GI37kDIYcXO9MO3MbO7sZJJHlyBGizAr0CZQzp-zy1bjy3JRLQkRozGkPEY68vec3rIiXxmnPYY_j4xjJqq3kbNxrqEUufySBy1r-9tMTpsRQ6CajKijzIoy_Cfuz6B598wEfm0ZcGvhSdfofkKEcjH9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LqLKn1FVU626nIQgdYlxk_whCLHQ5kokvDlXEtg6DYad_DRvBTjSTJFgNyJAC-2LNBl5jka_jzBBdSvjnxX9uj3LzjvqMn4I_jz0Lh9fMTQEkOvy0GgJZNURYCiEvr18rFlJiKS2R3Er0HLSwYwwuYIiBeoliIXGN-LO1c4Ylsbd6MPUVDtzCeLwrChk4FgZmG-oiJpME-IMiM_oC4QTLA6fXrRiRrxOOicz2o2_iY13ZuLXbohbccFYwCL6NJrTzfinrFe21noaUuRaRhFXRzxC4_fCo_n2Dv-LrXMRHlyf-MEk_tpa3g1fqCYFGEj00bC5EpmkGN5N86jXZhrXlw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
تصاویر منتسب به نیروگاه برق پایگاه نداسا در چابهار
@News_Hut</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/news_hut/67578" target="_blank">📅 00:06 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67577">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56e60a602e.mp4?token=PiELkKtLzFz58QlzDGGZ7S0KDuf-K3KCwqKWM0w8J0kaQY_UYIOOP7oBr9tzlMA1n5OwLv1UgKzUGTioc257jNWxbr--L8kvriFXWLxP0gWQ9_g2P74GTpyjFIUBDBOQ4avXzsraKbn_CbKvpe2LPSYrMSovhBKB5KEsuYraUj3-MV5xPlGcsOwfNkJIHzhL6TYxMqK3D5EJX3daGr4eCZXliB_HB8FuetDPi5zyROXawxThu01ZuCJN4lKXVQJxQHiXizUaNSpnu36AS-iT5vuM4LRDcU2rZm-xHn_TExz4SMqTrz6VAw7Q7Hu9zFiX5Bw5a1dTl8tR5qmn1GwZCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56e60a602e.mp4?token=PiELkKtLzFz58QlzDGGZ7S0KDuf-K3KCwqKWM0w8J0kaQY_UYIOOP7oBr9tzlMA1n5OwLv1UgKzUGTioc257jNWxbr--L8kvriFXWLxP0gWQ9_g2P74GTpyjFIUBDBOQ4avXzsraKbn_CbKvpe2LPSYrMSovhBKB5KEsuYraUj3-MV5xPlGcsOwfNkJIHzhL6TYxMqK3D5EJX3daGr4eCZXliB_HB8FuetDPi5zyROXawxThu01ZuCJN4lKXVQJxQHiXizUaNSpnu36AS-iT5vuM4LRDcU2rZm-xHn_TExz4SMqTrz6VAw7Q7Hu9zFiX5Bw5a1dTl8tR5qmn1GwZCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
آتش سوزی در بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/67577" target="_blank">📅 00:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67576">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🚨
🚨
گزارش‌های اولیه حاکی از آن است که هدف آن‌ها نیروگاه‌ها است. قطعی برق در چابهار گزارش شده است.
هنوز تایید رسمی نشده.
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/67576" target="_blank">📅 00:04 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67575">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚨
🚨
انفجار های پی در پی در بوشهر و کیش.
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/67575" target="_blank">📅 00:00 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67574">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚨
🚨
آکسیوس به نقل از یک مسئول آمریکایی:
حملات به ایران، رادارهای نظامی، پایگاه‌های موشک‌های ضدکشتی و سامانه‌های دفاع هوایی را هدف قرار داد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/67574" target="_blank">📅 23:58 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67573">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
🚨
❌
گزارش‌های اولیه حاکی از آن است که یک پالایشگاه در جزیره لاوان مورد هدف قرار گرفته است.
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/67573" target="_blank">📅 23:56 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67572">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hAoxTqSmF8BywQweDsBxS3v3iCkZzC9lEYgJ_umfvtdD4t4xZUwNRE1FdkGffokwzkluUHhQjaMPVQqfkWXoVQLmEymuCQAPWEgfTiJH1dy4_rt-z1iMtVJwX7skXV5HMKuzmkMU37B-_dY8ZnSnRDYd9fJCc9qOpRfHAKNylQoLJrJeV8d_ewXYHi-GgK24UNlrDr92uG_u74M1D1x-DLKKcURgu_DnBO2wfqAavkI2LiUdnZ4ptFfsMqyyWHUYDzI_P0Jv8Azb-xzlWHdKZ0G54vjiKiFWosiq4rKheVxYMnfqv1d-pYWXhMo_T7x3LQYrARxlY0Ayfh8218AjZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
حملات آمریکا به چابهار
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/67572" target="_blank">📅 23:55 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67571">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
🚨
🚨
انفجارها در بوشهر و جزیره خارک
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/67571" target="_blank">📅 23:54 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67570">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚨
🚨
🚨
چندین انفجار در چابهار
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/67570" target="_blank">📅 23:52 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67569">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PvZAzLimkGRyDz1V3RWV4dl9Hg3x2B5vj5RipXOp-LI3F2M_1eWEP_p7KqDr0YQmiOD1kJ61NDeusEJfCbc5r1vDVORCUA4z2rZRxq8fjsvCSbx0xEJeKSdD6KhyDdw0J9tbcZSAHprjfOu3hlG38MW23eTi2_vYihladIh9EQrOrhIt3xEoJqiNJc9ZQseAkLUVPTyriO-i-0DOcPZAiMVxqjZP2ZZmPPkd_bb0FHKmdwTIUNaqXpvHTaw72MbGn_RaNpaTRIcgEwDj7hF2bAWmL9HUXsheWwVokeysZBxfjTe3OQHx9H27qD7vWbg-pRCaCdS6HxBsWWtSJLUG6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
فرماندهی مرکزی ایالات متحده:
به دستور فرمانده کل نیروهای مسلح، نیروهای فرماندهی مرکزی ایالات متحده، عملیات‌های بیشتری را علیه ایران آغاز کرده‌اند تا توانایی این کشور در تهدید آزادی کشتیرانی در تنگه هرمز را بیشتر تضعیف کنند.
ایالات متحده، ایران را مسئول اقدامات تهاجمی اخیر و غیرموجه علیه کشتی‌های تجاری و خدمه غیرنظامی که به صورت آزادانه در یک آبراه بین‌المللی حیاتی تردد می‌کنند، می‌داند.
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/67569" target="_blank">📅 23:50 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67568">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚨
🚨
🚨
صدای چند انفجار شدید در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/67568" target="_blank">📅 23:47 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67567">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
🚨
آکسیوس به نقل از یک مقام آمریکایی:
ارتش آمریکا در حال انجام حملاتی علیه اهداف نظامی ایران در تنگه هرمز است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/67567" target="_blank">📅 23:45 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67566">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
🚨
پادگان ارتش در کنارک توسط آمریکا هدف قرار گرفت
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/67566" target="_blank">📅 23:42 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67565">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
🚨
دو انفجار در جزیره لاوان
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/67565" target="_blank">📅 23:42 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67564">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1d5e85683.mp4?token=ciKeP5rq87U_3HfP6MSPSUuGMv0uRd4f96M0Q2XYA3-NklxUoY3c52PMo_5N-SgqDoHdNB02gOriJeXh_wBKNINc_ehj2OuGSVD2dlRiYYyRAn5gfZC0z0L5sr52LhKyJ0Vnqx_ObGrOYihn17tajVb6PDcE09jAtf3Xd5s8ALlRNKEPFRzmvWI9Ce5ZIVEy4H05nPUt_hoxDCzFpnPynOT7hA-D8_vnFqjU-mDDaAxuSsiyERdIg81blymHJze9IcwS0acztPFinrjNgvi7Q7jGL3U88AtPEXibAQ5gE05vP4aZzdZgmWu_IKg6bM0vU0rNQolTD_axaQscvBaWXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1d5e85683.mp4?token=ciKeP5rq87U_3HfP6MSPSUuGMv0uRd4f96M0Q2XYA3-NklxUoY3c52PMo_5N-SgqDoHdNB02gOriJeXh_wBKNINc_ehj2OuGSVD2dlRiYYyRAn5gfZC0z0L5sr52LhKyJ0Vnqx_ObGrOYihn17tajVb6PDcE09jAtf3Xd5s8ALlRNKEPFRzmvWI9Ce5ZIVEy4H05nPUt_hoxDCzFpnPynOT7hA-D8_vnFqjU-mDDaAxuSsiyERdIg81blymHJze9IcwS0acztPFinrjNgvi7Q7jGL3U88AtPEXibAQ5gE05vP4aZzdZgmWu_IKg6bM0vU0rNQolTD_axaQscvBaWXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
حملات سنگین آمریکا به پایگاه سپاه در چابهار
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/67564" target="_blank">📅 23:41 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67563">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
🚨
🚨
حملات آمریکا به بندر کنارک در چابهار
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/67563" target="_blank">📅 23:38 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67562">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🚨
🚨
🚨
گزارش صدای چند انفجار سنگین در بندر چابهار
به پایگاه امام علی در چابهار حمله شد
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/67562" target="_blank">📅 23:33 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67561">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
🚨
خبرگزاری آکسیوس :
ارتش آمریکا امشب حملات بسیار سنگین تری رو به ایران انجام خواهد داد
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/67561" target="_blank">📅 23:31 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67559">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dIC1dsB10xK_uvp2MawFoGuBLO9lzvYlIe06pWBAjzM-w1FydsBYMMQ1vZrnkoCdG4fu4ea8Tdj5FzC_q9tkzzBxYxwUqMgXiG08X7ZQFSK4bjShUfvzOm5BSi1YG4VS94d0Ywp9ROP-AiCRT28ObsXOFJJQyo5W_u7oN0i2hE2UtFPBZqq1hFv0onolZKT8F6uDlseIx2ZLUuR75_MwjzynC2H9FeouyVEYk1WNLEWRXmsRiwd_vDKDKQKmkQO_Q5jJ9JfGgtuyCaNqKY2Nkzx6HDr2206C_cXm6gSsxtxpN-A0SBqgA7KQODh3ll37t97aPL_0uXvZLhRd1T4TOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZhVo5UncTmVJu48fr7EGSWLGIqk-GIdLkUy74gKE_CKnc5ZcLXHnzx_gqw3RgqXLCVitUAGe0BmzICrCbs7M5hcJesJv7Nsbkx1pXfYj8SEqvCzlAmPMIICaqCAxRP_YkySdlPwTC-SMELwnNnAYeq_xXuAsvBpSMRNXzRemNz1cYVk4mfMbca28YXkYeogCOJ_E80XIDQWZWOR5ckP_JHSWo1K2yCHfjf5IvvTl63lSW0Tg_R4TJCs7NCJQwuJjCi7KHoHpejLwmnV0GkNZA0-d8uh9YREQ8Jw1VPMgJxhUeuJth9GVjZfne2ND5DUV87fvwvDpHjDSAMz5pMDL5w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
بلند شدن سوخت رسان ها از تل آویو و امارات به سمت جنوب ایران
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/67559" target="_blank">📅 23:29 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67558">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
🚨
🚨
فعال شدن پدافند در سیریک
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/67558" target="_blank">📅 23:26 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67557">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚨
🚨
🚨
مجدد انفجار در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/67557" target="_blank">📅 23:23 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67556">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🚨
🚨
🚨
حملات آمریکا به سیریک هرمزگان
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/67556" target="_blank">📅 23:19 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67555">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
🚨
🚨
❌
شنیده شدن صدای انفجار در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/67555" target="_blank">📅 23:11 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67554">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c65cdf89e.mp4?token=Bz2OJ-fW1duUuYcaUCoQAKT7EFQszk-mr6C9VMom8DSyfx-_YQB7dHakvJjm40UJQxl9E_SxHVmgIsk9Nn5xJk7DGffxXXTfDy0h5ir4H6p1puy7hNDk5nj88VPHz6uMcL-910QXJWtSDOLv_5u2hXOUkmKtlvb8uuIteU5FFCY-Y66gJiSmPPs5kctHFfoV9L5xbVOf1FwmjnxT4Ol8LNxYDG7uHmRwf2cCP_0EN82g5re2YgIipO70AeVCMGTS1gvm2bM9lwEjcLOn9kBrjr5H32Vp2DQRWyrjXT47B1DxQymgLp6J1w7MURK8TgbhJl5AuqJSBc3h4fLC0vx4yw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c65cdf89e.mp4?token=Bz2OJ-fW1duUuYcaUCoQAKT7EFQszk-mr6C9VMom8DSyfx-_YQB7dHakvJjm40UJQxl9E_SxHVmgIsk9Nn5xJk7DGffxXXTfDy0h5ir4H6p1puy7hNDk5nj88VPHz6uMcL-910QXJWtSDOLv_5u2hXOUkmKtlvb8uuIteU5FFCY-Y66gJiSmPPs5kctHFfoV9L5xbVOf1FwmjnxT4Ol8LNxYDG7uHmRwf2cCP_0EN82g5re2YgIipO70AeVCMGTS1gvm2bM9lwEjcLOn9kBrjr5H32Vp2DQRWyrjXT47B1DxQymgLp6J1w7MURK8TgbhJl5AuqJSBc3h4fLC0vx4yw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇱
خبرنگار: شما امروز با هگست جلسه دارید.
نخست وزیر نتانیاهو: احتمالاً این اتفاق نخواهد افتاد.
خبرنگار: آیا این شما را ناراحت می‌کند؟
نخست وزیر نتانیاهو: چه کسی گفته ناراحت کننده است؟ شاید معنای دیگری داشته باشد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/67554" target="_blank">📅 23:04 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67553">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/176e4f444a.mp4?token=tnh25VTq7TNTq2eOh5uc3lIrf63GnGRfGx-jFuuIK38CmJDfo8ajM6WMGr4xsv_RNRcp9Tvw6RGlx3D4d4CD5M6zQgQzYlFs9m-vyc-snhR10gqIqS6-wb4z6l7-YJgG7lFefEDjrvfdCz08DjidwYvLTO0kbgI5JiSIwtp7G4KnIrFPZ17d5DIZ7-3X5NQx23K0Dby7H1RYXO1USFc4yh0AfNiA3snAIt4SZY85wSv-I-GOL93Lf-USNxzq8AW5s-BVJoikUGmTOtQnjOhhMGMr6AWtKzLAKwKWYk37-9IURMX1PUxMiK_ZqNpl97lik8O8bozika3jMjxeucmXiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/176e4f444a.mp4?token=tnh25VTq7TNTq2eOh5uc3lIrf63GnGRfGx-jFuuIK38CmJDfo8ajM6WMGr4xsv_RNRcp9Tvw6RGlx3D4d4CD5M6zQgQzYlFs9m-vyc-snhR10gqIqS6-wb4z6l7-YJgG7lFefEDjrvfdCz08DjidwYvLTO0kbgI5JiSIwtp7G4KnIrFPZ17d5DIZ7-3X5NQx23K0Dby7H1RYXO1USFc4yh0AfNiA3snAIt4SZY85wSv-I-GOL93Lf-USNxzq8AW5s-BVJoikUGmTOtQnjOhhMGMr6AWtKzLAKwKWYk37-9IURMX1PUxMiK_ZqNpl97lik8O8bozika3jMjxeucmXiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سرنگونی پهپاد MQ-9 آمریکا توسط جمهوری اسلامی
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/67553" target="_blank">📅 22:17 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67552">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/697775e593.mp4?token=s9VF4KnTskjARR0j-of7hPbbcOLW7gGz6DQDClb49JeXdegjrJVjBjeSQXTBtf4NYaEhdRTZKQ8tuf_U1cs-kCRlxMZiII-f8uNbhv3AqSKZFFhwCiSLB1GziYgaoHy5xUYufM0BqRHTW0mrPc18_SXpCb7ZkoKV3AidR4aONq2faQ8Z8OhiqktEHlmfB-rH0niEjUVgtwcBqBnr5mGnnuMsQXdfFdF4QutRLsl2Gpr69ouMzVWiNSa0QPXqknOxReNw9bimjDdSUXmBodp2G14Q_e7MJdtw_hME-h9Go3_K_hG-rY26We6kOoaC5h3WqV3WiGYLW02Os6PQzvHHWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/697775e593.mp4?token=s9VF4KnTskjARR0j-of7hPbbcOLW7gGz6DQDClb49JeXdegjrJVjBjeSQXTBtf4NYaEhdRTZKQ8tuf_U1cs-kCRlxMZiII-f8uNbhv3AqSKZFFhwCiSLB1GziYgaoHy5xUYufM0BqRHTW0mrPc18_SXpCb7ZkoKV3AidR4aONq2faQ8Z8OhiqktEHlmfB-rH0niEjUVgtwcBqBnr5mGnnuMsQXdfFdF4QutRLsl2Gpr69ouMzVWiNSa0QPXqknOxReNw9bimjDdSUXmBodp2G14Q_e7MJdtw_hME-h9Go3_K_hG-rY26We6kOoaC5h3WqV3WiGYLW02Os6PQzvHHWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ترامپ پس از پایان اجلاس ناتو، ترکیه را ترک کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/67552" target="_blank">📅 22:17 · 17 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
