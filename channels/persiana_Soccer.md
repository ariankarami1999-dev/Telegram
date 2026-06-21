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
<img src="https://cdn4.telesco.pe/file/O1ufRcbpQuYmcEa_PWk8cWFAOxOdfa-dHNLw0QOpTEz4L00tD9Sy-ssiK_KdfWVQ5PzVQH8AUO8nM-umZ5h1Qdgrukb9a2Tb5gJnGMtZftCqRhnDQ4g8b1MeUJwI7OGuHnk4bM7dRPgcjZCxIQjo1PIQFuLj9fJxs7cYRFGzR_3iMW3Ng3oea7bPVYI24lzsKEeEJSNoUj5JZ3Lb4oHDMtJIr2ijSNp85Puu_nqL2lBQ3kUbSwHGK44UBDMH8SLiiku1oBFkXmnPNNiZq8zLeYZjF117xWQMiTmZ87YLTpG4FYjGj7ZjK3VpCfAsl0jTWtXt_-WJYeSJt2UlshduJA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 309K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-31 06:21:08</div>
<hr>

<div class="tg-post" id="msg-23955">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EOljrrBvmZTpmkwhG3iczplb_cuXFmIvr18YS4dTCHD_9kh7yCAVmOwU8GzWxQQtaVwzJM0OAoC7FEUHVMP5ZQfsKwNMW-i8DyLqQvfY2p7tUZBrISP9lRnFtEZ86qJbEFDleB2G005pbZVF9XlrgHyhDF0zjbHfkqg71w5bHYxsFvnAP6aC4r69hwegyfATWjWB4lma0M577VN6DPxuzi18yZcf9b2Pi4F1V90Sy3b4oa_8UvXA27iKJNl5MX5dRBFkD0R6a0N_udMtjLkxbtIE9ChcRJhmBLMdmuy_aN3RaMiFN9UBRFcxJqwTz2EYV5FvpUKMmGjGE4L9q_vtfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته دوم جام جهانی 2026؛ یه پسر کُرد سه امتیاز ارزشمند روتقدیم ژرمن‌هاکرد؛ کامبک  دیدنی شاگردان‌ناگلزمن‌درشب‌درخشش‌دنیز اونداف ستاره کُرد زبان آلمانی‌ها در فاصله تنها 20 دقیقه.
🇮🇪
ساحل عاج
1️⃣
-
2️⃣
آلمان
🇩🇪
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/persiana_Soccer/23955" target="_blank">📅 02:56 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23954">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TkNigWgx5bUzDNT58cOpJcFBHlDV_8c2gLTFYw6V3D6QcZff6inbLPyagNAIzwo1ZDAjo2QthxHNvLMKBgfeQVE3MxUN7X-H556XRbnQ3yAZB0VHKbAAa16qAAMOD8UIMCMhqdDI5kA4ZkCNyVcHwrs21VOHEGgGpSkmZ7wVer05lToWloo3T7rQRCkHCUyZnH2dbMeScWkfTd5w338kUlLyBjgstjCYh0rrSvQS0wfJVTm4XG1QYo6tx-wFEVr7eG1qDdC7011q2WsCNP4QUhHPYMzPq7dUi0fNgxNqoh6qznW6ov2K8FIUmhqN1pH7Zf8WjvbD55GPj3OlT8GUIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
دنیز اونداف ستاره اشتوتگارت همیشه در شادی های بعدگل خود کُردی رقصیده تا اصالت زیبای خود راهمیشه به همگان نشان بدهد. امشبم کلا 30 دیقه بازی کرد دو گل زد و نمره خارق العاده 8.7 گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/persiana_Soccer/23954" target="_blank">📅 02:35 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23953">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XcsVHwqXOGw6_nmq-KVVJsO_-aOrK44jW-x5LpRh1L9zUUWw6ZRMuQNd_kekWcaiyyFGwy0t__KrpHu-kxsyM7Uvky1yrUmB9hIDVWchKNaqLogtY3bpQPoz3flHNOsvWvdsXu3YcduFAr_bsvODHqO0XXkOdftG6BNaF0Zt1yOOeT26jJRi-tXmowLxd8J2zAzbb6pNHiEEWPjoPK49jIJUG6aT1FU9bnCPUK-87fXDmGezU-bUQ5Qp5TSB0IzlRwdfSqhgpvgcngreMxgAjCmP7tlX18xZWihi2pZWyR8Irx0uoskSSRitEA5pxrAJiOHpduv-YqiYA2Cebr448Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارهای‌امروز؛
از جدال ماتادورها مقابل عربستان تا مصاف بلژیک با شاگردان امیر قلعه‌نویی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/persiana_Soccer/23953" target="_blank">📅 02:05 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23952">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MtJeI3XgFGnU1OilhRUQ4bvjnfTADbz_lGyZqTElJ9RZ7AjyoHGb3J80sn4pdPSP9aS5blYUPMA5hTAhZ38V87fqQcPKfpbFX743ISU36GN5AzW3MEutNeDB2tY0VQXT_6E95dWVUVKz8qDGCnIEQdR3PqC2VmT6Ub_aW_LoAOb03bn981qF_fSM01ToU-LRlhHPBiKW2MAWllqsZt1fEjwCk7V_ryHTFo2uFSFKTG5AuWY7i966FPH5sAiMYNpyqItFnaWBOfN1JJ5Ipkt4tG_jPYzr1DJ76uImugCi_QH-s7wovw9EQImypHwdKjNc3UcisgRsfajUR9GLYw3YxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌دیدارهای‌‌‌‌دیروز؛
ازبرتری‌برزیل و هلند مقابل رقبا تا راهیابی مانشافت به دور حذفی جام جهانی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/persiana_Soccer/23952" target="_blank">📅 02:05 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23951">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bf800e040.mp4?token=IS_Zse6flpGQ9Q141qiix92L2jHbLX_dpU1xM5Use6tekal_lDW8NAfwk1QgV4ODbPyB1mCNryed97VyaBMppSS_5AVWzVDg_X5W9VDF6eRM7VSOF_M4VD3i9Jp3kBPPJgQKR4isLCqY-cHqihQoCtmTdefs9TI1Jorm-GB9YwCoWg897TtICNDf34xIxcL8aAADEsCmA1UPG0Yu6sWwZmj1xoTN_bH5XiGumOydt-VWqwrdnmEu0_rb8hmKv4YPa_ZPcTkdSJ4gUqAi-ZVZ1KrRNmK1MaaPnGrGlf9MDGepxBzkI-X35q5qbRwbXeJ3AOVgm4y0J1jk5MvHkCc9bg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bf800e040.mp4?token=IS_Zse6flpGQ9Q141qiix92L2jHbLX_dpU1xM5Use6tekal_lDW8NAfwk1QgV4ODbPyB1mCNryed97VyaBMppSS_5AVWzVDg_X5W9VDF6eRM7VSOF_M4VD3i9Jp3kBPPJgQKR4isLCqY-cHqihQoCtmTdefs9TI1Jorm-GB9YwCoWg897TtICNDf34xIxcL8aAADEsCmA1UPG0Yu6sWwZmj1xoTN_bH5XiGumOydt-VWqwrdnmEu0_rb8hmKv4YPa_ZPcTkdSJ4gUqAi-ZVZ1KrRNmK1MaaPnGrGlf9MDGepxBzkI-X35q5qbRwbXeJ3AOVgm4y0J1jk5MvHkCc9bg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇩🇪
دنیز اونداف ستاره اشتوتگارت همیشه در شادی های بعدگل خود کُردی رقصیده تا اصالت زیبای خود راهمیشه به همگان نشان بدهد. امشبم کلا 30 دیقه بازی کرد دو گل زد و نمره خارق العاده 8.7 گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/persiana_Soccer/23951" target="_blank">📅 01:55 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23950">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LqQx38eEbbhB9sBtuLIj16CKpzmZs62LEAN65wLG6GJdhtb4y0G4LEKHeQ_kvVkqn2dU33F7XA85iywL-2RC7nzfCFont0zedx0END8zcCXaqpOhL2KohsBNOGm_0MGRxOH8jWkLXUmwYgwGRJmNJhnd5IwPh_IaOy66vG0BRsTy4HnQS6rTcTUgeo4aLkT9-ECGzE_Se1YDl8uZvXHZGkzRLGd_5DK1g8ixE3ez8yJe5X00BAuWaHDmR3IzPyR1icll6_ICA4z31-oHA7rKbjBREa3rhtZer7iGnhCipko9_qnHUtmtPHSMLlYXi2gLRd2LNwAq2K2Wu0VFuBTgEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
باشگاه‌ گل‌گهر به مدیران استقلال اعلام کرده با دریافت20میلیاردتومان‌رضایت‌نامه پوریا شهر آبادی مهاجم جوان این تیم رو آبی‌ها صادر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/persiana_Soccer/23950" target="_blank">📅 01:55 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23949">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YSWTzWZb7A7hRD5BVdiUYMPad1_jSG-URzQJh59bhpk_d08dUA4gzID_GoCjQAdH_v6YtoUFh8ece0h3eYBteMikyS2CQsN2zP6FrqS3FOjWtfxzgSVu7MMaIKccUoSsVpK_QMBGp2umWCjArXEb13tRoV7lKKHrtx_A4BZoR5dJmdtCwdDioHgAIOSklD4GWmEjraFFIt1eG-wYY1S61oyaGRccA6TFz1EaQJtqbpLpP1gGECcMAgAuOD_G4KXr2U6MdcmRM34zBWa86EbrXd-OuI_zGt0PVzTZ3iwmFPayDBINvipBbAJwom7F-HwLfB_zmC2TbPCD6pOG-xWB2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📣
آیسان اسلامی به تلگرام پیوست.
⭐
اگر توم از طرفدارا ایسان اسلامی هستی بیا توی کانال تلگرامش فعالیتش شرو کرده کنارش باش
🙂
ادرس عضویت کانالش
👇
e30
👇
https://t.me/+QMjHLL65ocsxYzRk
https://t.me/+QMjHLL65ocsxYzRk</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/persiana_Soccer/23949" target="_blank">📅 01:55 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23948">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40b51e8a93.mp4?token=CWbHytZg529X5lz7t1e0y3y3IcaOLAEisNzhCn7PYgo3jQPQWRVM7tuRyc76eyVjESrkBQDmXi9Ztk56JmNq8OoNHEh8TRIyTXf-eN43ay1C3iFNa2GDTjO4tBCTS8jdq-PUT5y9nAgrgWe5CIW-sRPpndHNHSTXnrqLMVp2No2MZ8q7iqs3CYO6zIj_fVZlNz8363MMf7JfiNYHfcVvLmNxKW2HC7Ef1gTxWnyQvTgfuYh4ECjx0IRNOy4AQmgwIjRut2HzyJCg65MCYFr-Di9p2E4T4QAtYJrqCM88SCgVyuyxMKSq4ARbOcl7uChLdmboqRPhJPPuiVtV4bHK5THLnn31TLhxr4zCNH_hnJyEBXLPVsK8szZPBkb961hD6v2oNaEQCQtcAZSvbKKXi0cvMYvlZkdyT9C9uh7q_5fJIvThG8C7cznacPT7G-KcYL48HrETSGI1USN4QWZ7jX7h3eRPNp-qXmIcuSFLrIGAwaem_c8riKGov6azHtWQ2d5WNSwWejB2Y6iUNt0vrqYaeX14XMyXPXPicM3fHtSB57GN07K7HQTDAZ5vt56augeTNrcY0-4LbHtVjC2XX9aypV37CE2_PPKdjZM_0VitevC0ktURFg_0g1BbbyuNwQP3yRsCI1ASKbDkj7QV20G-FQSMbSWKfYvTzifVUOs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40b51e8a93.mp4?token=CWbHytZg529X5lz7t1e0y3y3IcaOLAEisNzhCn7PYgo3jQPQWRVM7tuRyc76eyVjESrkBQDmXi9Ztk56JmNq8OoNHEh8TRIyTXf-eN43ay1C3iFNa2GDTjO4tBCTS8jdq-PUT5y9nAgrgWe5CIW-sRPpndHNHSTXnrqLMVp2No2MZ8q7iqs3CYO6zIj_fVZlNz8363MMf7JfiNYHfcVvLmNxKW2HC7Ef1gTxWnyQvTgfuYh4ECjx0IRNOy4AQmgwIjRut2HzyJCg65MCYFr-Di9p2E4T4QAtYJrqCM88SCgVyuyxMKSq4ARbOcl7uChLdmboqRPhJPPuiVtV4bHK5THLnn31TLhxr4zCNH_hnJyEBXLPVsK8szZPBkb961hD6v2oNaEQCQtcAZSvbKKXi0cvMYvlZkdyT9C9uh7q_5fJIvThG8C7cznacPT7G-KcYL48HrETSGI1USN4QWZ7jX7h3eRPNp-qXmIcuSFLrIGAwaem_c8riKGov6azHtWQ2d5WNSwWejB2Y6iUNt0vrqYaeX14XMyXPXPicM3fHtSB57GN07K7HQTDAZ5vt56augeTNrcY0-4LbHtVjC2XX9aypV37CE2_PPKdjZM_0VitevC0ktURFg_0g1BbbyuNwQP3yRsCI1ASKbDkj7QV20G-FQSMbSWKfYvTzifVUOs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
هفته دوم جام جهانی 2026؛ یه پسر کُرد سه امتیاز ارزشمند روتقدیم ژرمن‌هاکرد؛ کامبک  دیدنی شاگردان‌ناگلزمن‌درشب‌درخشش‌دنیز اونداف ستاره کُرد زبان آلمانی‌ها در فاصله تنها 20 دقیقه.
🇮🇪
ساحل عاج
1️⃣
-
2️⃣
آلمان
🇩🇪
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/persiana_Soccer/23948" target="_blank">📅 01:36 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23947">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jf-S3-5CiQzS1KpT4TcxBUAnDK2-3SXB78-vzCR6xVEfWQ8ahBmm5fJoWXZPXn7yI9f1bprMsGgHl65Zmu4RlXAqYuEuiMljlmQogH4dq1nd0QY-H3YMItDqzrXALH4wptLRJbUg1IwSRPBTVxSJWV7jztz62j27wZrwpEJeHwbSnd3d6HBNdPn_vfNa43ydza5FXMBC7ZKV0wUejQPbg46mvtNaQMU-vjsAMEEvTSWZUXH0XOjzpNFU45n77WhmXFKCNkHpcmWnSSTbZZ9TPpvujTu2_ZEhxIig3z6KBMD7gVO7KvoioHK7zwLQsaME5gMIaGQ6U9UQTVTrnb_SsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
گل امشب تیم آلمان به ساحل عاج: ندیم امیری بازیکن اصالتا افغان پاس‌گل داد. دنیز اونداف بازیکن اصالتا کُردگل‌زد. اونداف در دقیقه 60 به زمین اومد و8دیقه بعدش گل مساوی رو به ساحل‌عاجی‌ ها زد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/persiana_Soccer/23947" target="_blank">📅 01:31 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23946">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mJ1qbZvrJps4z8f-2iieSzmk8KB6jAi5eh_kuScrPGpIqWj4T40EjWrTYyMT0De0bHn5M3pjnTkVxxoJkWPxauI4FP6-7p9oT7xMAGXh_hUzI3P1pXaPDqzEZJ3YLLGLqtMgnnLm8yEC03P97VFy3FhgMMkRa5w0gucummRCV9FtOzx1y7IL55SlAzO1sW0ZUXzqHIIYMYXzSNP7a56kNjL7DeHIhcQNkJ6M4RThw8Q7KCaT_CuBGJbQ-chPjOrq1_bug_qP9tKX4T0d1DMYl0vjKMe09ceUQFv9PdTWg_4StkoQTtY8Kz8I2ROChs1kN5qP-HDApYPVeG_GdPokng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته دوم جام جهانی 2026؛ شماتیک ترکیب دو تیم آلمان
🆚
ساحل عاج؛ ساعت 23:30 از شبکه پرشیانا اسپورت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/persiana_Soccer/23946" target="_blank">📅 01:21 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23945">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F7r2-mxfGyr9EriJRxD23EDs2XRvmJE0R9jFUTna2YFifA012meheBDc3mzRkoQ3Q1lGJwIJpCtjhKdQImj8djrxKxNGVtmXViiu2DfbPuYJRWhK0Tgzpn4fTcLTPTGPof45cwfsw75oRxeYdg8FiabFkI_abDt2tGkmn4566cbMiSCfqBZj14t-Pl31wNoD2vHt9O7wtOX5oVTlXRYdnRAXc94I8tdHYykrl2mSBo86I_ezly__NxOd1bgoZb5Opo4RzxX3rBtgea23VML70c_pxbiqk2ddxHvKVyueOTLGjeSIL05pYDNsBewDGyWedKineDzRA_5m55fv2O833w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
👤
امیرقلعه‌نویی سرمربی‌تیم ایران به این شکل نشون داده که ساعت رولکسش رو پیدا کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/persiana_Soccer/23945" target="_blank">📅 01:12 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23944">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb124e2149.mp4?token=bLoMVog3rrZDsmiMQXrGu3NI8apkdN_qHpuT7b3XIxiSjZ4uRVUSaf9wFoau9F3AbsbhtE_oLbslgPntGjU_W1JyHEZfSPZCAmmD7clxgv8odQ655TV1IS67jtZorqCZtYp2hU9VKOjKUIGA_D98uV7E5UBmYYjqYmvdnubbly3pflIEaRKx-3sG6z05gP_k-13MWuiLBmvKvFvkG4X20RgzYhscdxyuiTnq3o-AbyQ-El6whm3aLNRiGX5i0px9B9G9uSGbb_Pz5zcRKvRrI74eXUpdZc95k8HoYvf_DlrTy-jT6Qslwq-oU1A-hu9QQ4aVPjTKx65lUlbDT_c66w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb124e2149.mp4?token=bLoMVog3rrZDsmiMQXrGu3NI8apkdN_qHpuT7b3XIxiSjZ4uRVUSaf9wFoau9F3AbsbhtE_oLbslgPntGjU_W1JyHEZfSPZCAmmD7clxgv8odQ655TV1IS67jtZorqCZtYp2hU9VKOjKUIGA_D98uV7E5UBmYYjqYmvdnubbly3pflIEaRKx-3sG6z05gP_k-13MWuiLBmvKvFvkG4X20RgzYhscdxyuiTnq3o-AbyQ-El6whm3aLNRiGX5i0px9B9G9uSGbb_Pz5zcRKvRrI74eXUpdZc95k8HoYvf_DlrTy-jT6Qslwq-oU1A-hu9QQ4aVPjTKx65lUlbDT_c66w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
روزهای اخیر شایعه شده بود ساعت ژنرال فوتبال ایران دزیده شده که عکسای رسیدن تیم به لس‌آنجلس نشون میده‌که‌خداروشکر این خبر کذبه.ساعت‌امیرخان
🟰
خط قرمز مردم ایران
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/persiana_Soccer/23944" target="_blank">📅 01:07 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23943">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/keLyCK134Bud5qquNrHyHr1kAtkb82QLzROxX2kX9FRL4H1NQv7iO8IQwL6WPRWLNdq-Cb-vOFxBvfYMjbMOE3_WGPCC03_MuTjBMXe5jYCGzfnA-5Hpvt_h7VzphM1Tq0D9y26WrVHiI6be6kyp-uEVM3h6uPtHSDWV5DE5Sg3Qw-Hk88ta8IWOtCYt5AC96pxnP0skFKziGAE_4WTsxV2-9BBmxtm-I0dIEHnbAG4DlPFqZ2G5TlqQ8EWbPwQl_7tM0oFen7YMpVOQ5olLxf-tzXP_RZYOxZQUXbL-Kzfz_MVxU_df4cO2HtUY0eaMknOZ8SIQVWoOIcXtR9dKVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته دوم جام جهانی 2026؛ شماتیک ترکیب دو تیم آلمان
🆚
ساحل عاج؛ ساعت 23:30 از شبکه پرشیانا اسپورت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/persiana_Soccer/23943" target="_blank">📅 00:39 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23942">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TLuvqiTYH0DeDxvae5u28OhjqE87m8XlY2sRpl2WlfmgpSPQoAe2Fj8KuKdkkoNAAIsKlcqrm663_NGMxxmSVeI_AxcVjif9QnqoJvAenLHabSu8J5l18PVLvGDMEAMXA46vS1UpKOfXafAmVcr3PflmziY2bO6Mg8I-OlppRcBZzuaHmXpnWdtXaNuBWq_o_kXHO9r4aEHGe8eondv3bzFZaLxpNaQeo1vIeKQDGse666hS4LNuj8lpt96DppoDjunek7sAmma8kEd6HzCaNCeDhhN7whsPwmP7hEytDCKqd42uIFOAGaZtIQtjbHXdNSuGO3zTkhDXACckppljSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#تکمیلی؛ مهدی‌ گودرزی ستاره‌ جوان تیم خیبر امروز از طریق نماینده اش آمادگی خود را برای پیوستن به تیم پرسپولیس در نیم فصل اعلام کرده و درصورت‌توافق دوباشگاه‌این‌انتقال انجام خواهد شد. احتمال اینکه فخریان راهی خیبر شود نیز زیاد است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/persiana_Soccer/23942" target="_blank">📅 00:25 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23941">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a6c4ff321.mp4?token=UNDi_GBMplV9dyBr-p_bt6sCgtkZlJjFvfIAHDxBvQYcho3oKwmtCWSCzWqKtX0saCYh2QjhmYqG7whDASPewjsKApMIRTilGvWi02791kHJX37dgh66wx6Kby8bWu7X-zhX1xDvlft2tcwYaUGWWLq_2RC7oKgnYlq6qa7oBdJpLcGRbnFQGsAkpwedZP_ZFluzci-p0LZmHA93Hcmp9tHxlrRWqnhpmmiUWAUS2EW2jfsDxWge_H8VHUXRAgMRloiFMdXvnzGXapwh_5d2Nt4D1RWjE4NmUEaIx6M1e3ghNSBNgo6mWGbIBn3vtCe47QH98kL7RR1DNEF2yLIMAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a6c4ff321.mp4?token=UNDi_GBMplV9dyBr-p_bt6sCgtkZlJjFvfIAHDxBvQYcho3oKwmtCWSCzWqKtX0saCYh2QjhmYqG7whDASPewjsKApMIRTilGvWi02791kHJX37dgh66wx6Kby8bWu7X-zhX1xDvlft2tcwYaUGWWLq_2RC7oKgnYlq6qa7oBdJpLcGRbnFQGsAkpwedZP_ZFluzci-p0LZmHA93Hcmp9tHxlrRWqnhpmmiUWAUS2EW2jfsDxWge_H8VHUXRAgMRloiFMdXvnzGXapwh_5d2Nt4D1RWjE4NmUEaIx6M1e3ghNSBNgo6mWGbIBn3vtCe47QH98kL7RR1DNEF2yLIMAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خداداد عزیزی از دست‌کارای‌ جواد خیابانی فشار افتاده میگه حضرت عباسی این کارها چیه میکنی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/persiana_Soccer/23941" target="_blank">📅 23:53 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23940">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ri6vFnpNu4_Ei3KqePUHrInt8QXboAaUqaCcv37LuBXCXpCqkRWw1U2xYKiabLwIx-M_vUOCknMznBB6UXMS5KkdIsv8tQS1di3qwr0zEirazZWZL16ZXmMZJMROG6xIJ9ZYLLLlcb7hnZhekk3G6chmx-Q_rNjadugqLZquOVVbfAimA059w52E2rnjYSy07ppAIwmBFFIXkCIeGi3fO4K6fAmL2_NlRJZ-Pd_vPuk2M36cPg74079kSyYg8DkrJ082CLUOTosziC2B-3pJdTcXx71I-WERfx7lbyjbe_xHmQ_4RynxIENmU2CAsCnzFEfb8T1i4K_6QrECuAgL-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بازیکنانی‌که در جام جهانی ۲۰۲۶ امتیاز کامل ۱۰.۰ را کسب کرده‌اند: لیونل مسی مقابل الجزایر؛ جاناتان دیوید مقابل قطر؛ کودی جاکپو مقابل سوئد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/persiana_Soccer/23940" target="_blank">📅 23:43 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23939">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/elYpDGijupc-8COT4yf8BMzeC_LULD6dJuKSVV21mFUt3_vOC5yz1qZdymI1LK1Z9kU2QNSB3hl7vbq1kLk0WaxLyBxQ5qINGJR_ulqffILUDyVISHQk34JNDnWIe9HRHKOjJGePhwiwY7DZgyVKVdCLr8fqtrE7n7W7xer3gUalzGpH-k1iqVmewcsiHU3JbgKj1fe2bIj2vQiKjGyrb7Ga9QER0dxS_oYs9ffY_9ky5boNgf-S0vJ1LslvqZg0_YPPd2OfZJ0vQ_qGmneDts5BorJDWKPl2KV-7uzEWx-av6CYSiE_4a7ToTwISR2dKoGN7tnAssx2f7OOg4dVmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌دوم جام‌جهانی 2026؛ پیروزی ارزشمند و پرگل لاله‌های‌نارنجی مقابل یاران گیوکرش در سوئد.
🇳🇱
هلند
5️⃣
-
1️⃣
سوئد
🇸🇪
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/persiana_Soccer/23939" target="_blank">📅 23:28 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23938">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T4tRzUYeTUdDBCvcJ0CbvReN1axuMGOc52xbx-zo8qrn1tafIbuDu-eTAV7Cis-F8v2lG_7d8e5gFtjgBUDOcjJuG1GcMdQAUklpxUOPTF1f6aMzbnSDEGtTH-3CzixUYvkmrwPxs0CpyPR-jqfQogD-KwJ-B_ohAH95bfYfMcSCuNfYLtv0J_r0GmtUWAtfjo-_41f45Mv5PJ4lRSVQDs6Dfbm3Wv0ilclDG6sGi_YjYvYqU8TzZpVP7bhvge1v6l9HB5dJgzrxCxiOJQtsrJ77uTZH3s7jlFCywUUnCoqUKYJ5BzpGcEnYdx1xgmaPAXo2Pdddpnmh3MGXDkSG8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رسانه‌های بلژیکی مدعی شدند که جرمی دوکو ستاره تیم ملی این کشور دیدار فرداشب مقابل تیم ایران در هفته دوم جام جهانی رو از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/persiana_Soccer/23938" target="_blank">📅 23:04 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23937">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W04Jj6WpUScXU3IfrdrKtv5pUiy5nT_IJ1yr3nEWLUBWRUG1Rns4QYuV4QLS1NvKpanTDmJjjwBgZ8z6_4IYj3xu0fuyyahKWkWTpnxtKmWo3osMiwx_nu9a0hKOImMTyFVi58dcpYSg6fTmL-RaKHEiyhtYds74KIrBpJznBOHoW2aKoR3WFDak2oAetT_I33QUIecKDo3gek7Iyc_N0t42tF-q0Q1kQE8smSr_7OIIJviy3_3sxbGQVc_cSfPhIB1Aj25SQcZhG_UEShB5utZDPmry3C04C6YuS3_eqnfO3Lp-iCXL0IsvKyb1i_KTCS3_qqKZjBnE6qFbR1Wd3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ پیمان حدادی مدیرعامل باشگاه پرسپولیس برای انجام مذاکرات نهایی و عقد قرارداد با دراگان اسکوچیچ  راهی ترکیه شده. به احتمال 99 درصد اسکوچیچ سرمربی فصل پیش‌رو سرخ‌هاست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/persiana_Soccer/23937" target="_blank">📅 23:00 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23936">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e541eb115f.mp4?token=kNl8VyPU7FVjGngmcW-wtA40dSCAiVhLdUg9uzJyN6W7KPeDMqwyK4zX7rrep1ITz1gYFcuf22bkZLFcp2Y94-ZHwAfyRs35O2_bEQjadUNjRaSUWyMdni9_fCbfVK7-GkLkQJHvvDaR318rDyJYE_gRoFwUSdO-oMMWB7BDWrmcYUN7OhZpRDMhleHt49KLX3fN_8ghx0_q3YWseViDyorN6DTydx2pUwJWF2KIlcsleOYwoV80K5ivJrHvEtVoNdUsYrKNjN1SasFVfpt7a3GFgQnDSO0aJXGzjoZtuApsWkybCpLxHCs8rvH__ZTmvA2b8Nchoopr06m40jqd65LfOGvTs2p7QwMfTdrt3UYE0q4bK3ALtIa5BZT_nvBZF7v8wrs6CFv4gv1cDZqPeRP7XJedwKgLJdMjGDMaq6MXxi6z_bbw1QJ-V9nVy_DuLgIK3rTdJbRkRvi8GK79EGFwbSXmRPV7beYeB6BrpeVvBxW6NZS8PfS_cNoGnTz4Qswb7PPYpFhFHVhusFl2rvW_A6DVb22hNKnmIxINb2YIjdL_En38kOD_pegNqTvImobkeuN4kPn2rOUy31kba8RlGI8fuA-q2GK55aMl4wq7YNg5JJDZhQsdX-1qIGPl266-_hEbho1E4DC9sIfXwZQpdwOpYqX02ha-Ev9YVis" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e541eb115f.mp4?token=kNl8VyPU7FVjGngmcW-wtA40dSCAiVhLdUg9uzJyN6W7KPeDMqwyK4zX7rrep1ITz1gYFcuf22bkZLFcp2Y94-ZHwAfyRs35O2_bEQjadUNjRaSUWyMdni9_fCbfVK7-GkLkQJHvvDaR318rDyJYE_gRoFwUSdO-oMMWB7BDWrmcYUN7OhZpRDMhleHt49KLX3fN_8ghx0_q3YWseViDyorN6DTydx2pUwJWF2KIlcsleOYwoV80K5ivJrHvEtVoNdUsYrKNjN1SasFVfpt7a3GFgQnDSO0aJXGzjoZtuApsWkybCpLxHCs8rvH__ZTmvA2b8Nchoopr06m40jqd65LfOGvTs2p7QwMfTdrt3UYE0q4bK3ALtIa5BZT_nvBZF7v8wrs6CFv4gv1cDZqPeRP7XJedwKgLJdMjGDMaq6MXxi6z_bbw1QJ-V9nVy_DuLgIK3rTdJbRkRvi8GK79EGFwbSXmRPV7beYeB6BrpeVvBxW6NZS8PfS_cNoGnTz4Qswb7PPYpFhFHVhusFl2rvW_A6DVb22hNKnmIxINb2YIjdL_En38kOD_pegNqTvImobkeuN4kPn2rOUy31kba8RlGI8fuA-q2GK55aMl4wq7YNg5JJDZhQsdX-1qIGPl266-_hEbho1E4DC9sIfXwZQpdwOpYqX02ha-Ev9YVis" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
صحبت های فیروز کریمی سرمربی سابق پاس و آبی‌ها درباره‌ اون‌ویدیو معروفی‌که ازش بیرون اومد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/persiana_Soccer/23936" target="_blank">📅 23:00 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23935">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hXir4Tdg84lYWO-8hVC528Q3DoVrOTNo3_tIHFgHLDCP0UkOBft6VklnuqzflM5BrTjvjNGImd9E1S5sQL7vz1aLYbxh3_ouo2NtXG2X1UZOKkH4hHhmSVMhO9HgAGkHcqfx_ik2J-uQzrcBcrddN5QSdxGBmSGdP2eDkTTcKvovDYyfRjC9Pj_viNEFO3fc7PiCRvZXsmOFM1Ym4-WicJDSr7WFKpgNF93ZTp2vMjEQzexMpZl8KIZK788elAs76vMPMrZP_8ipONI_N5OBlJJq7MW_W4801pzfHhS51n_-X44oGO0Tx00Eh9SAO4mSdkBG9Sx02M_wiBsP0lnAvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
بزرگ‌ترین تورنمنت فوتبال جهان آغاز شده…
📺
پخش آنلاین و بدون سانسور مسابقات منتخب جام جهانی
در کانال تلگرام Betegram
🎁
شرط رایگان ورزشی
🚀
100% بونوس
🪪
داراي لايسنس بين المللي
🌐
فعال در بيش از ٤٩ كشور
⚽
هر گل، هر لحظه و هر شگفتی را از دست ندهید.
امشب میلیون‌ها نفر مسابقه را تماشا می‌کنند…
تو هم به جمع آن‌ها بپیوند.
🌍
http://betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/persiana_Soccer/23935" target="_blank">📅 23:00 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23934">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">✅
هفته‌دوم جام‌جهانی 2026؛ پیروزی ارزشمند و پرگل لاله‌های‌نارنجی مقابل یاران گیوکرش در سوئد.
🇳🇱
هلند
5️⃣
-
1️⃣
سوئد
🇸🇪
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/persiana_Soccer/23934" target="_blank">📅 22:34 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23933">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mJAftfsek8qyM61wD4YEVG_0traQYCQ46Qo_1A3qZfV7Q6W1vNoxtjUmeMt60Cz5G1zouR5RE5vh1NDv4Y5oi5ht8aPGY4mIaQpAh-QWpS_LIY79qYztvm1xAOfi0_hvYuDqhvAsZcrbljbXLQRknfUdWKItaBehmUQIwsjjyvSrASBIlCFC0dWDseEnX5KTtP0FMkUT1iQIEKM6OxbncQXOZNuLB9CNjS1PZtkZ2Q-i56YcGt3D22TGPVshLErauHA68kURCHGyiyMVq1Ur9U98veCWK92XUEgfyaRa7TdA1dsIp1MCLzucvxGpjUCz4AG3I1iCH2ytcRJnt3tDpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
هفته‌دوم‌جام‌جهانی 2026؛ شماتیک ترکیب دو تیم سوئد
🆚
هلند؛ ساعت 20:30 از پرشیانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/persiana_Soccer/23933" target="_blank">📅 22:29 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23931">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ad4RxPTvFipaYEvPZrQBkbnFQIwJxPyB9SRipN1iJz_T4iuroQCxW0xhEh6SjcKfoc0l9FCTGLEracaaoce9rAfaCn3pYk6SRoPQwIYSCtZswfDO_C8KOIfd10xh8szGLivCM1uPmLc5fF00-RTc0JWbz69dGUZ-GR8W_OIh7gY3QM5dh9ff7hywnYfCU5FMEt37ZEQdKjWawhfnTpzT4hkb7GiLsEzvZp1sXItKwk7pc-NnrFZ49lvdQO4ShkAowtxHnJ5YuZOR4TXSGazS_EAOKbFpDFK-OzYSKGKDktLxnLjulapXp6orzw_NiYwKJ9gJzdF4g1nrrj6N3ehAjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fR1cHDxyRN5vojxhZxQ4HKSha4k3A5OJMZ6lbj9X0nvClup96LAZYz9sDc4rkf-EWwXiAnRhttbeyljNMIHHb-3fg152wP5WAw0HAls9vEKZ-hX0hUFg9Ke600bKzUkaQPPJ1O1KV8MpVmct_WbOhkj5FBvWLfoFQ50cWJh97tr-kYzcGf70D2_3b06s4aEZOE72513R04Bq_gpiwBbNk8MNGKb27PNBReS4TwOOHKOMd0NjlIVhckOlY7iwM93cBVzJu7rBLg_zg-iYGUQ9dS_bdYy9GFrlnAS2lmCkp5HGt0NDObyUcBHm0kSnN4OFZ5fJexRHOcvNrbS3hPtlIQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
هفته دوم جام جهانی 2026
؛ شماتیک ترکیب دو تیم آلمان
🆚
ساحل عاج؛ ساعت 23:30 از شبکه پرشیانا اسپورت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/persiana_Soccer/23931" target="_blank">📅 22:19 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23930">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lKWJGzB8F_Llkta3fIVYsEMWG5iodbDW7gnn4-dqN6su_CkqG0TZNpYn6pyzbC8Tm4ktcwJD4Y3B88qcs-N-Xv7a-KOdB6iU6F2QzLSa-D-bjkfqYMubk-zOCA-o-NZn6ASGnz_NfZL7gfq9l0MsktZERyTVZkOWp7g2aaT5pXTHsi_63EBN2So97ud4DYihbr8dAhMv_3EhL2K611_Y3SJXa8pZIorQ7ZrMXR-IiGcsQUDzgjZumLzQhFuDbuDWEW9NZoqSzUHZygVtXf4JvXw3P34Nw08bC4TE_8zAqa2J_3Zt1RiT7TXYFBxXc0sTfWXqzuRk-zl3wf_ogCGotg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
جرمی دوکو ستاره بلژیک بخاطر زایمان همسرش و متولد شدن فرزندش اردوی تیم ملی بلژیک رو ترک کرده و ممکنه به بازی فرداشب با تیم ایران نرسه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/persiana_Soccer/23930" target="_blank">📅 22:11 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23929">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3537466720.mp4?token=RwMlJW529uUSV29n_UE3rtfKE9xvstd_bCDQw2js3Iu15TlJhPB5Ut98hl9FIugkTU6iZt6k9T-XEfoSomKku1nozq2gbFxx8cCbcGLhTjPtThE_iE6wI020Gu_VqHMSnH-sgq5RIfRqL2z7nI3T06lyqzQgbNOY_dTMDfYMKC2cT0pfNiOnX64VIBxfrh0nTveEwpotfknzVyEeE5bDjeiS42py2Fok0yXZlLutS20Vaf73Sda_oBpVPCc5vHJoYSeLXzjnkMxFaOrORdl_PVw07DrC-qDv3unQrfhgHXApaxnpdADJx8w1x3v4KiNE1Z7PG4urn7RQhWXB_ZrvSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3537466720.mp4?token=RwMlJW529uUSV29n_UE3rtfKE9xvstd_bCDQw2js3Iu15TlJhPB5Ut98hl9FIugkTU6iZt6k9T-XEfoSomKku1nozq2gbFxx8cCbcGLhTjPtThE_iE6wI020Gu_VqHMSnH-sgq5RIfRqL2z7nI3T06lyqzQgbNOY_dTMDfYMKC2cT0pfNiOnX64VIBxfrh0nTveEwpotfknzVyEeE5bDjeiS42py2Fok0yXZlLutS20Vaf73Sda_oBpVPCc5vHJoYSeLXzjnkMxFaOrORdl_PVw07DrC-qDv3unQrfhgHXApaxnpdADJx8w1x3v4KiNE1Z7PG4urn7RQhWXB_ZrvSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
سعید دقیقی امشب‌ مهمون‌برنامه عادل بود بنده خدا داشت‌راجب‌برادراش‌میگفت‌عادل برگشته میگه خودتم سفید مفیدی؛ عالی بود ببینید
😂
😂
😂
😂
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/persiana_Soccer/23929" target="_blank">📅 22:08 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23928">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/463a3196cd.mp4?token=KlLnSxhFuI0nXmmUCnlF2jdGcBmG99UthOkaGQ6GcK6SZA7vcEOMmHas0lUxDNMp1-C9xUa3d5196oBZthJQ26JOsKAiD3V0WVHL5j0Sw3gqAjpq0VGwK69EIXhi1MqHirPEvyXDs74fHT7aLCz9qUmEWGXGPDgqjrdwyQIP343Sa14YQfuZBLMGyDmLeZhbBRfe9ZiPQWOLxjo9Zz1eMXs9jrEGVFec-IAodUONJYlzyhJyuD22V_9wLMsbh-ZJXWrS_4O6nZPlbOI8UALhhyh1ZcO2Z93MPq4xELCu-WRdI7PMa9Vy2xhjP7WVtjbh-N2H9ekK3DJTSWLPDrLf_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/463a3196cd.mp4?token=KlLnSxhFuI0nXmmUCnlF2jdGcBmG99UthOkaGQ6GcK6SZA7vcEOMmHas0lUxDNMp1-C9xUa3d5196oBZthJQ26JOsKAiD3V0WVHL5j0Sw3gqAjpq0VGwK69EIXhi1MqHirPEvyXDs74fHT7aLCz9qUmEWGXGPDgqjrdwyQIP343Sa14YQfuZBLMGyDmLeZhbBRfe9ZiPQWOLxjo9Zz1eMXs9jrEGVFec-IAodUONJYlzyhJyuD22V_9wLMsbh-ZJXWrS_4O6nZPlbOI8UALhhyh1ZcO2Z93MPq4xELCu-WRdI7PMa9Vy2xhjP7WVtjbh-N2H9ekK3DJTSWLPDrLf_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
این بخش از گفتگو دیشب عادل و اوسمار ویرا تامل برانگیزه؛ زندگی‌سخت و تلخ اوسمار در بچگی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/persiana_Soccer/23928" target="_blank">📅 21:57 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23927">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🇳🇴
هوادارای‌نروژ وتشویق‌وایکینگی‌شون‌کف آمریکا؛ چه عشق و حالی‌میکنن، چه تابستونی رو میگذرونن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/persiana_Soccer/23927" target="_blank">📅 21:48 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23926">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hh5qfau8cfehzgHe2oaFZo--wdq2UZZsH2nGUYHd8jetvCyjgh8QR5L7iQ9znCnqVi7CyTliwO2DHMR1grYzon3tP85fUaa7rLe-cdLUhkdmVOMUdkURr8gUQkeNHu8D40mT7cYzywHZknAyfCC_bNmjflz6Z7_yzHjBG4Xd3W5nhNQDeINXpYxpGG-839mfcFlGJrdthFYtfG3DhWTLCJcyQ4u0yxhMT3T7j7mhscCslgtM8rrvpYer4o036Dqvq9Lo5a3-DlkgaaDJjs1TKjRaZuMpl__l6J31ucZpreZHIJjdQHv8q4oH3wsc7hDny0S84a2AAkfaMgMxupnJoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق‌اخباردریافتی‌پرشیانا؛دقایقی‌قبل با یکی ازمسئولان‌باشگاه‌پرسپولیس ارتباط گرفتیم که ایشان اعلام‌ کرد بزودی قرارداد اوسمار ویرا با باشگاه فسخ خواهد شد و او فصل بعد درپرسپولیس نخواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/persiana_Soccer/23926" target="_blank">📅 21:36 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23925">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EwavZm3Xtqk8Rn37bM7I5G-6Zi5fESNHB8k1dDUYKoh0PRU2btbserOeojxLff59mG95pPV-N00jPUeGZW9zX10Gqmlp791w-7wSjD3t6Vpc80ojHfDpJX2VdRGc9bOPchrQ3APybJlrQ59uRKuzsg1b_sS5Blh3vn2up797M11pBpn0FdRucYhYwkCxXszHG67ZGNylkZS65CAEPDW-sqL0CMzYFVSQot31KxZCVWyBuJIae_2X6vtkt8FJ2KjTcbI5ui48IvxoeqeKuz1utxYRyn11yIxp1THKEU2YjnCW9c4EkVo_prlPUFvg5qJSgF60zJ9R0f5dxLETyjRITQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
🇹🇷
تیم‌ملی فوتبال ترکیه با ترکیب 300 میلیون یورویی و لژیونرای مطرح بادوباخت بدون گل مقابل استرالیا و پاراگوئه از جام جهانی 2026 حذف شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/persiana_Soccer/23925" target="_blank">📅 21:05 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23924">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">✅
محمدجواد حسین‌نژاد ستاره سابق سپاهان: من خیلی میتونستم به‌تیم‌ملی کمک کنم و خیلی ناراحتم که در جام جهانی حضور ندارم.از لیگ ایران پیشنهاد دارم و احتمالا برای فصل پیش رو برگردم ایران.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/persiana_Soccer/23924" target="_blank">📅 20:28 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23923">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q1Qq5b2cAIlS3Fm3xsoUxrK-FLlJnr17ns5J7csDipGP3boV3Pfy8vSqoG29E2jKy8gY0xHTV3GAH2C06Pw7F5k8ZE_0KrkzUB-guQBoQHI52isrQf8XmAaUaZhKeNs-fMkENFE-4cyKvUaodAOJm8ba_cwJi_esfBjDZk2VzxK2QjkmzgS02ghXNVIJmzNHJUyrO6voM9nJ58Ip5FJKcw3Hcd459r06jhzTy1JQ2chfeLvrp7cA_28d6c-zdZzPwUjuR2psy5UXsuDYZ8EnJ7ouldD8rRpj0fFvxfFuTB73HtIzleCuPFTU7wuy1lBRdILd3hApuFSpvJsN5D6Dxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی_پرشیانا #فوری؛ علی نظری جویباری مسئول‌نقل‌وانتقالات استقلال با مدیربرنامه های محمد جواد حسین نژاد مذاکرات خود را شروع کرده تا بعد از باز شدن پنجره این انتقال رو بالاخره بعددوسال نهایی کنه و حسین نژاد آبی‌پوش بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/persiana_Soccer/23923" target="_blank">📅 20:15 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23922">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c65b32d4ba.mp4?token=mRwcrJU0bYkMjU-Ty8A_Tbg680m4NzHBWU7dDdm6HYDBcW4busBHD5yJUor9-bLfJldbV4EpOt_rh95paM8g4WgvKG8JrvtpJ2KIf_DSdskkxYHYZxJeghO3W4Yb8VjgBCPMrKXcrb3OrABxw-QI2Gs3Ht9BSaNB9oz_SVURrE-E8gI5D7wl3_hFbsZfnScOiuwe3UtThyLyJieZwaq18SWSz7ZAhUYDdz23QIASNm7K2Vc6JAv0pAX9swbBcg0nbg4rh2tVMdy1HOQPjdh9-CiWf8q-kST8l_sD6XB9GRtv-7qFOhzCvry5JBkTyT393Lffpa-6S9kVGx3NN003gWd3k0tUM43N06Gd5W9XWl-z3xjSac1tOu4ZdnGYUxAZDRSv5OZF7LkgjnO4j2DoWUjyyHNPMlzo37KY2idJ12LTjOFDaXfY1_dwt_mgjOkV7Mqscg3xmdhVOq8fcZU2TsHazWk8RwnCvrF4iGhUc21wYrdMn3Hr2EpKSJjky2zFx66k5trCN683MMkaMpZtxZouHGE3qyLueKPHRiE_vTKs7qYbUrp35XzE67kQQ_J6FqJxVr2aPFw3r86DHThS1X56URcNRKkjvNBzXz9pxpidF95zv_bM_IiCT81R-Nvufu8aDeqea-6InIiqhr_dbSsqjQyl3Yj2BfROitOJEVc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c65b32d4ba.mp4?token=mRwcrJU0bYkMjU-Ty8A_Tbg680m4NzHBWU7dDdm6HYDBcW4busBHD5yJUor9-bLfJldbV4EpOt_rh95paM8g4WgvKG8JrvtpJ2KIf_DSdskkxYHYZxJeghO3W4Yb8VjgBCPMrKXcrb3OrABxw-QI2Gs3Ht9BSaNB9oz_SVURrE-E8gI5D7wl3_hFbsZfnScOiuwe3UtThyLyJieZwaq18SWSz7ZAhUYDdz23QIASNm7K2Vc6JAv0pAX9swbBcg0nbg4rh2tVMdy1HOQPjdh9-CiWf8q-kST8l_sD6XB9GRtv-7qFOhzCvry5JBkTyT393Lffpa-6S9kVGx3NN003gWd3k0tUM43N06Gd5W9XWl-z3xjSac1tOu4ZdnGYUxAZDRSv5OZF7LkgjnO4j2DoWUjyyHNPMlzo37KY2idJ12LTjOFDaXfY1_dwt_mgjOkV7Mqscg3xmdhVOq8fcZU2TsHazWk8RwnCvrF4iGhUc21wYrdMn3Hr2EpKSJjky2zFx66k5trCN683MMkaMpZtxZouHGE3qyLueKPHRiE_vTKs7qYbUrp35XzE67kQQ_J6FqJxVr2aPFw3r86DHThS1X56URcNRKkjvNBzXz9pxpidF95zv_bM_IiCT81R-Nvufu8aDeqea-6InIiqhr_dbSsqjQyl3Yj2BfROitOJEVc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
‏یسری‌از آمریکایی‌هاازهمچین‌جایی‌شاهد گل دوم تیمشون مقابل استرالیا درهفته‌دوم‌جام جهانی بودن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/persiana_Soccer/23922" target="_blank">📅 19:42 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23921">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uDZna6Qz9O_0N3Jzv_kKnArvZ1dw6lhEKZCq6JT0qmJp6HXNAEX-XZ3V7qPrSg007R01gJJ6464i53T9WHV9vqUGA_0KAiSc_ft95rsTydyxeikBey7_BnaQfcy5HUwrJ5Qg_9o3N75eiR6JG7cq95QzqCIwgDHieCp-p7hfkWR5wIhLFbMqk9hfsBFmVG4Xdfou7pPg6hGH6TIqfNh8Q-dRbtUBeo0oMo4lcXLDm8xiPDxT2PGEpoRVh-IscXRM4zZQy-LFnys2TlUnFdwOShvPIfhr3JoQM5rHqh5Xw49WmYar5OzGQcovvqEmoM-HoxsfhOTTrduk6aY0tiv2xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
🟢
طبق شنیده‌های رسانه پرشیانا؛
سید مهدی رحمتی در روزهای اخیر مذاکراتی با مدیران باشگاه پیکان و ذوب آهن داشته و احتمال اینکه با یکی از این‌دو باشگاه قرارداد امضا کنه بسیار زیاد است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/persiana_Soccer/23921" target="_blank">📅 19:26 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23919">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EutOeEFsSX45r2V7kvs0fMHxWxOCIX6XDP68mQTPjXfRgTAs0ssxk4YBhcqdqTBiyCFXeLNkLZPiJ-SpLNyoFSMku1SNNS99fHjSUxJ_zTRdYSsZdoVH9J0fx-9zIN5T4rnVUpspBfJanQ0BSv3bGm0gEUq0aEoB2P_1dRm6hZ9hbN7RUeE4WjNDSZnCybuQNCx6_LtPFhGrwfBy_c8Spcj-9izfgLfHMULuVTleML2y4S2K5tU-a2YwcqR8vJRabI6jm2ZaXGMmSuPILjudtVU21orUlffZBK65EW7UjyvnEWIlayHaQ5CFKrc-YyefZl0F2HpryZF0PcedeqFNKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WaChM3oE0oC3-vD-ZHV-yBGZMrOlDbXpm8aGhq64Ikfkk5PMRksxeiQHVdgURdvIPTWio4_bfYlBGtrR9OlxzdpA_LqajUtCHL2UJUWV8gLa2OUxRtf6mrNBNezbZyOXUHsGAIuoq6nT7TI7zRaFjI5hK1zX7WbY6PEQy6PlX35r70taL8bL-i3DtuVUrtsxKoDRRgKDlCxPoOmweZzmLjp11ibNn9crOM69sGfkDEmDEJhLWEIYd2iEfNN51-BWkMouys7hHRhOjH0CKtPXmLjbSLBdH8VI9ha8AV87RU9Ozg-fLySGz8LPHR9dWotWDHCuJDVIYm_dxbkxpT8T0Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚽️
هفته‌دوم‌جام‌جهانی 2026
؛ شماتیک ترکیب دو تیم سوئد
🆚
هلند؛ ساعت 20:30 از پرشیانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/persiana_Soccer/23919" target="_blank">📅 19:22 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23918">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/413165ef88.mp4?token=IILgRH-O_VAalXvxpyzqeMG6vVHf2_wrcHaCTi2jpx4g7PFjwyZdDFqnmpDs10U_KRfhdvk2Z4lWbb9WzMs-_bESg7WMJ-soM5FiYyzFWYedFmXZk7kO07Z4PPPk-WF3y8dRoDSlmCN3yXJLccz9Y6EJcewZXI92UH51AUl8EJsjAlfqV-hDCwNRYXDeMcOUifvTTlk7Z7HHtriJfxPv8XdicOOmwkZ6EARyyVf5l4gC-oPVzmdddRGB9sliVGOfzwWvDTh6mOav3-WrDBnyeIlADNu2hzA4NJqD412PNsEnwnhllYqBb71LyXzDwnt2JveO6FJcfP07M-omHSytzB3IDm61SiG0dx5-WDeBavrADv8RYACvLE8IddQEhktW_7YbaoqdL0BT9Uurr1H6GzibTxlpOXTYxy0mwAgAyO69pFFO_-70vTrBLKl_sTnoQFcZUp0xQlaF3awZZuFlORLRvW6bor43ainLL2MdBYIJhuxOyBZZjusZdUIrQjAWfH-l0_8CmnrhpvAI4JbhHfVA40y8EKv3Je7nsCPeP52Egm4Wey0PqWlyl1dQ2zrJAhHO73kcbV8yiNC2fpCbj-RIXDt7GeYTYBA9Eidc6BTm6RfrPEtsMhQTHZhoSvlPvuDtYxCijIuER_2rxqrhzEsssyMJ_bTiveM-ygK6xK8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/413165ef88.mp4?token=IILgRH-O_VAalXvxpyzqeMG6vVHf2_wrcHaCTi2jpx4g7PFjwyZdDFqnmpDs10U_KRfhdvk2Z4lWbb9WzMs-_bESg7WMJ-soM5FiYyzFWYedFmXZk7kO07Z4PPPk-WF3y8dRoDSlmCN3yXJLccz9Y6EJcewZXI92UH51AUl8EJsjAlfqV-hDCwNRYXDeMcOUifvTTlk7Z7HHtriJfxPv8XdicOOmwkZ6EARyyVf5l4gC-oPVzmdddRGB9sliVGOfzwWvDTh6mOav3-WrDBnyeIlADNu2hzA4NJqD412PNsEnwnhllYqBb71LyXzDwnt2JveO6FJcfP07M-omHSytzB3IDm61SiG0dx5-WDeBavrADv8RYACvLE8IddQEhktW_7YbaoqdL0BT9Uurr1H6GzibTxlpOXTYxy0mwAgAyO69pFFO_-70vTrBLKl_sTnoQFcZUp0xQlaF3awZZuFlORLRvW6bor43ainLL2MdBYIJhuxOyBZZjusZdUIrQjAWfH-l0_8CmnrhpvAI4JbhHfVA40y8EKv3Je7nsCPeP52Egm4Wey0PqWlyl1dQ2zrJAhHO73kcbV8yiNC2fpCbj-RIXDt7GeYTYBA9Eidc6BTm6RfrPEtsMhQTHZhoSvlPvuDtYxCijIuER_2rxqrhzEsssyMJ_bTiveM-ygK6xK8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
👤
یادی کنیم از این صحبت‌های علی دایی عزیز اسطوره مردم ایران درباره رونالدو اسطوره جهان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/persiana_Soccer/23918" target="_blank">📅 19:22 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23917">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UT7kiL1fF_CxXGqAzxo5ox6Dg9hJAC1dWRu1hj0GjBEOpG_SBgqLpwW9DXnWNkbh96OmFGufUEbFyQJv8KwfFR7456UrTmEgAGF4hXAZeY92q6KOTcEcucb8holfyDbg9y_tCuODCQ-nSXXTO0oA4vQF0DVG7hmQV45x_GsaxHnPLG58VjvZ6grYu2AmIS56vnZt4zyn09PDA6PhlsBXsBOSr9g7nupElJ5vP2Mttf6vKWW1YOP3iiMbdUmMUxptJyj5e7eZHEk_6uC_Z1inX_WJdUOd8RopOYr7RSfMEJmI2DYxOGzZD9gw7oq0s7mfZuMFr3g6gH3EkO5MBbLPjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
تورنومنت ۲.۵ میلیارد تومانی رومابت آغاز شد!
مسابقات جام جهانی 2026 را در رومابت پیش‌بینی کنید، امتیاز جمع‌کنید و برای‌سهمی‌از جایزه بزرگ ۲.۵
#میلیارد
تومانی رقابت کنید
😍
🏆
هر پیش‌بینی شما را یک قدم به صدر جدول و جوایز ویژه نزدیک‌تر می‌کند
🚀
⏳
فرصت را از دست ندهید ؛ هیجان واقعی جام جهانی را با رومابت تجربه کنید!
🆔
@RomaBet_official
┅━━━━━━━━━━━┅
🔰
لینک سایت جهت ورود eg30:
🌐
RomaBet.tournament</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/persiana_Soccer/23917" target="_blank">📅 19:22 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23916">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AsLSjB9nJDtpvs8WsDt7xEZRSx2hPHsxsLO1T0uNx2k8eei3Y8KdaFLZ8yBiOFAI2Yp87aMPWaq1J_vQa9W-U05NZakbxmoraSLsuKduAwGovMklXGiondJ-Ap-A2XFiv3vjSTijPXMJahCbjSODPwPV2VB9UrTaImobpbWu7xthvoMQoC09TwimXOpVhjZ9a-73c1PWip9ozR2RLQJBv_bFthv6PKLYxP0mnimsdwzt_P8qnDmpZU42iYGvq-V0Td0mRAdL6WZfIx1acL40PNQSO1Nny2MSfOQlfVPbslJMgGVEi7NLI4h-AyDZJvCsMmf4NK3vQyevihyQTSJm3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇪
👤
تیبو کورتوا دروازه‌بان تیم ملی بلژیک: تیم ایران یک مدافع راست‌خطرناک و گلزن به نام رامین رضاییان دارند که زیاد در حملات تیم شرکت می‌کند و ارسال‌های‌دقیقی‌انجام میده بایدمراقبش‌باشیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/persiana_Soccer/23916" target="_blank">📅 19:03 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23915">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WuZDjIYkVQD_ntQx54Oi_sbQSh6nk68cZDvI69XwPFcDqQ74SCoPXwVVIik2z2DL6jD5qnto0BYId5zjU2aUclg5jnuirq3zpUxBVn9uUcNXNMy4BMDGRoWoJCGGqUw_D5VzDYguUxR3vgWJ_mlnxqh6UB-jKGHB4KgjCE3C1XrZOzypsPxuSgkTSi-lLFTMYSHSu_xUYDUrEHwXEnLN5JuwWgdscNUYD_OwlOOV0nMwJrNNlrGQvZ_RjzevEhBBEOVGePSNlabpLbmS8MbDk52EurxUlTghI2O8rlGlqe54zQAQ9Er4auN93wN0HacWPzpShBR2D4Moy33eg6RwbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
پیش‌بینی اپتا از نتیجه بازی ایران و بلژیک
‼️
سایت‌اپتابراساس۱۰۰۰۰شبیه‌سازی‌نتیجه‌بازی ایران - بلژیک را پیش‌بینی‌کرده که درآن شانس برد شاگردان قلعه نویی ۱۵.۱ درصد است.  در این پیش‌بینی شانس برد بلژیک ۶۶ درصد و تساوی ۱۸.۹ درصد است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/persiana_Soccer/23915" target="_blank">📅 18:55 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23913">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/602d7756fa.mp4?token=KAWVgktd1oTmYKsntbRsAxsqOaMS9UsQs_S7bMq9I9pLtE_OD4cOqYRWlAWC9L-Y4E2bq5-W7-Seo7uUbscPx4RtPdEh8jVfJvToEKoot3kODUXgm3W5AiFwya3xGE8asDQY76ga_VRqZkWj_Rx_QSypHdAQxAJzGoPeZoiURVhPtBGLtIlJ8am42uFWah2tLQy8_jWk2LRCy2rKamPJcNgmP_VGzaztA2Yr7Q8B-W_nYR8G27IavX-MWLQAp9fkql1i5A1XhVoY1vRvmTZ2FM1MruczFO4jMqm33hzmWRnDh_SDF-4ir1uffTmA3LzOdopleZ2yQi3QtdA4gX0yxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/602d7756fa.mp4?token=KAWVgktd1oTmYKsntbRsAxsqOaMS9UsQs_S7bMq9I9pLtE_OD4cOqYRWlAWC9L-Y4E2bq5-W7-Seo7uUbscPx4RtPdEh8jVfJvToEKoot3kODUXgm3W5AiFwya3xGE8asDQY76ga_VRqZkWj_Rx_QSypHdAQxAJzGoPeZoiURVhPtBGLtIlJ8am42uFWah2tLQy8_jWk2LRCy2rKamPJcNgmP_VGzaztA2Yr7Q8B-W_nYR8G27IavX-MWLQAp9fkql1i5A1XhVoY1vRvmTZ2FM1MruczFO4jMqm33hzmWRnDh_SDF-4ir1uffTmA3LzOdopleZ2yQi3QtdA4gX0yxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اخراج‌المیرون‌ بخاطرتوهین به ترک‌ها:
آلمیرون بازیکن پاراگوئه به‌دلیل توهین‌قومی به بازیکن ترکیه اخراج شد! تو قانون‌ جدید اگر دست‌جلوی‌دهان بیاد و مشکل پیش‌بیاد بازیکن اخراج خواهد شد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/persiana_Soccer/23913" target="_blank">📅 16:36 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23912">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/94a793ad17.mp4?token=RT7El2MnBmFVKcxSwpDTDljADPzQSVTleyLkQYhZetfVT6_tBoyBDiNYCbgbzW_5LEMf12a_dEKhDoQqNJaOpmhCUiC-nv3KNkMMVDrlTGKKDS3QADgagG7477kvuyNRqphq7Bn2FOogGcEsYkaqnieGf5rxWRVps_DLrNdXDc4Vi2MqManNHXi1Op7cqo8_nac_t-aTj_yiFwS5onVNc2PCtrHr9ehkLFAbnzpU5mfQyL-Po66gI0W7khdVS5kF84-sSEzA2CfmErNtMy_MemsxrYyLT52VApdPabonr8AAyvfCZ1IfSJzGMyx5w9MuY0gMvRgibVlBww1JmbvLQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/94a793ad17.mp4?token=RT7El2MnBmFVKcxSwpDTDljADPzQSVTleyLkQYhZetfVT6_tBoyBDiNYCbgbzW_5LEMf12a_dEKhDoQqNJaOpmhCUiC-nv3KNkMMVDrlTGKKDS3QADgagG7477kvuyNRqphq7Bn2FOogGcEsYkaqnieGf5rxWRVps_DLrNdXDc4Vi2MqManNHXi1Op7cqo8_nac_t-aTj_yiFwS5onVNc2PCtrHr9ehkLFAbnzpU5mfQyL-Po66gI0W7khdVS5kF84-sSEzA2CfmErNtMy_MemsxrYyLT52VApdPabonr8AAyvfCZ1IfSJzGMyx5w9MuY0gMvRgibVlBww1JmbvLQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
گرفتگی یهویی عضلات پای عادل در ویژه برنامه پریشب جام جهانی؛ سه تایی غش کردند از خنده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/persiana_Soccer/23912" target="_blank">📅 16:17 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23911">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AITEoQo9rwK_3HAHGnFCMVoQzA6BePuw7tqTKR1NGf_3wQFauYppjLb10mJYreeIh4nHToKQShbzcI_Mgu4BAN6UxJm9f03QWniDBMx9_xJmedFpz2zSMitD0nmOYEKZw5IixobJ8ckiT4vUwkA2ydW3n_bABqAzZPAezGimkv2_NtjYsYK8tIBilpmVkE9tx4zTHuFGRd4g-_mXDR4hXl6dywW-tC3xO3Bu-lVb8g79ottDaQXE8NUqYOaTCG_0jLCyJAhkieqrQBuCAdpLxy4YIi5CoHKdW0ERAaTsWi3FtE-o6FLcR5OQ99x65ZwdKU-dBV0e8Oe543fxjx9MFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
هوادارای خارجی رونالدو بخاطر مصاحبه ژائو نوس که گفته بود کریس‌رونالدو برای‌ما فرقی با بقیه بازیکنانداره‌وبهترین‌بازیکن‌فصل پیش لیگ عربستان هم فلیکس بوده ریختن تو پیج دوست دخترش:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/23911" target="_blank">📅 15:54 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23910">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NLxa4iEGD08MZPvyIW98AKsA7bAO9NScgtjuTb6WK4XWV6I42vrCzw9hpmb8b35Upy8OWCoCfUv23fLj2oRboLtq6NdgRWi1YB5AxWrEU2mGTcgYp6WVtKlLLaqXKUnXOtVjKdBQ2EfG3TqT1ryMt1JtMV48IyUJtiIQhvyuMLsBFz6lWHUe_AHwtI3OmnYIIo4XVJyQGoNDD41a0ocz0kKQ38qpJDJe60leLKjHuOEJREXVjAOdDVTmiZgnRijO1bMmLYI5_SvVV45rwo1g05KIw5BxVuX6vswsetcrlTlzpWQv_rHtrKEFQK5CeF8U1vkGv2-zELPzD93qW_stIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ طبق شنیده‌های رسانه پرشیانا؛ علاوه بر امید عالیشاه و مرتضی پور علی گنجی، سروش رفیعی دیگر بازیکنی است که در پایان فصل قطعا از جمع سرخ پوشان پایتخت جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/persiana_Soccer/23910" target="_blank">📅 15:49 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23908">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d95ab0dfbb.mp4?token=TBehl6D5s-YvAwHHcDYdabWOOf953q3L7lol39MqlbBz-FhikY5UKqU9zGEGSCLT_v-uVNE0bo93gEnQpo28D4ziZjmVgZPWmA8sLsMJ1a93k5cdDJ9vwNmeeYtnQLLZb4Hf9zNq6snQo_-9ZBvbgA_pCTkz_W0ItyylNByE1ft8812sGVZFz0dmdNSYSI0bwTOiAz5m64xbKoJgJdyq7VILfFKvBRrNsvTYtPJgrEgrFvAVrBUpwkwjWRj4BE62fzG8_7AGb2a-F4KSb30W4wZTcVeaxJHtL_JtTRIKVzrUew0mcJ1AgLCvW-AP34D_wG-AZqXWqlCYcTLJnO56Gw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d95ab0dfbb.mp4?token=TBehl6D5s-YvAwHHcDYdabWOOf953q3L7lol39MqlbBz-FhikY5UKqU9zGEGSCLT_v-uVNE0bo93gEnQpo28D4ziZjmVgZPWmA8sLsMJ1a93k5cdDJ9vwNmeeYtnQLLZb4Hf9zNq6snQo_-9ZBvbgA_pCTkz_W0ItyylNByE1ft8812sGVZFz0dmdNSYSI0bwTOiAz5m64xbKoJgJdyq7VILfFKvBRrNsvTYtPJgrEgrFvAVrBUpwkwjWRj4BE62fzG8_7AGb2a-F4KSb30W4wZTcVeaxJHtL_JtTRIKVzrUew0mcJ1AgLCvW-AP34D_wG-AZqXWqlCYcTLJnO56Gw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#تکمیلی؛ لحظه ماچ کردن خبرنگار کره‌ای توسط یه‌خبرنگارمکزیکی؛ حالا خبرنگاره اگه ایرانی میبود تا از خانومه لب نمیگرفت ول نمیکرد! این خجالتی بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/persiana_Soccer/23908" target="_blank">📅 15:38 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23907">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cw-oEygUwCU6-632pK_e5auFuAJG4jLFtqPcWArjHgwyZyYCBUD1KWU9LfWHLe0IucoaYtEd-9xzbsluzBOw677Q1gfUxls-CbPepvgy1dQbKw2TzpALpsExGg4Ttsj-sGYh_XnlHYiHu_OXEjHkNv6jA_TiCDQjVtrz5f0zOWoYg1nszKpb3sJ3CdU_7Q-racjIiyFgtXGyOPha7tYV3FbQhYiqTd1HUZKDtGB7vvkatlXpIyp5WL-8VosB7OPbH0NkGu8-4yTABrvfmz635PivBFlh87eJYI9rbaxHw4gkESlkpLtSCN3mxxEUwfqBnDLX3LEP46NWzKjf5fr1JQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
جرمی دوکو ستاره بلژیک بخاطر زایمان همسرش و متولد شدن فرزندش اردوی تیم ملی بلژیک رو ترک کرده و ممکنه به بازی فرداشب با تیم ایران نرسه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/persiana_Soccer/23907" target="_blank">📅 15:23 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23906">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g_xrbtiuCMhClaBMcTOD6py2xDmtMx8J1IRCc58y3bP4nVaDHIu_-MEtAreaJuRm4Qad576dvVruGgeypbR-Q4nJY49heDwczDOx1eQ5sdv9tCiOqanY1kL_pN2czOrY_F5h9zVBPyBCBr5K2EmcZy1WkY5moJMRlhubIKskeA8n2ctdGKnDp_Bo835y1hHWgbvzKQBS685ZkijTNBdBQHT4_UMzEpzwjUo78kuOOHdpMHkdr0HlzzNp_56UUbza3pITRLb2AcEoGyAAjvRpUd-rkZa3wdO736SnAHMzVDjlkiS66hI8mCTeaMsjg76QVNjT0eVmV3WYOagJkgcnFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
#تکمیلی؛ طبق اخبار دریافتی پرشیانا؛ محمد دانشگر مدافع 32ساله سپاهان بعد از جدایی از این تیم از طریق یک‌مدیربرنامه که رابطه نزدیکی با علی تاجرنیا داره خودش رو به استقلال پیشنهاد داده و گفته حاضره به جمه آبی پوشان پایتخت برگرده.
‼️
محمد دانشگر تابستون سال‌قبلم…</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/persiana_Soccer/23906" target="_blank">📅 15:16 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23905">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lUwJtyDbLvNsNwX8Ck_Vooctil3G4RBrNyGrPyEbDi8wuEp2doOTBTiHMxaGYbJDW7o9pazZ896DN1N06MYxsjUisFBGCrMu9rSeQT7dnbXCfYAel0c3ecJcacNIWzXQBnyuG4WY_m3PxDWZ-0aslhp-uyzDM1UORA6txU80TmImb7NI3AZItThzktToqvFOtNKR1c62XEIAewRiuiB7sL5XvewFRdK0eu_vBUAKRRoY2Re_A-z3adxGHkfkp9ZyH8ZEk4FXsR0uYH3vO4haeCXPcLVyWtxj27HaqyJGhdR2lENEP1OuJIp2J6V1MWXoY9PM0W7mF1lIIKw_w_13ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
کاسمیرو ستاره‌خط‌هافبک تیم‌ملی برزیل و سابق رئال‌مادرید و منچستریونایتد برای‌عقد قرار دادی دو ساله با باشگاه اینترمیامی به توافق نهایی رسید.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/23905" target="_blank">📅 15:08 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23904">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rl6ZBdoZBVY7LFTBi2HwcnN2MCJQOLfDGCg-ojpVn9AgNSugqnTphwbH1fij5aAlo9TbdOGDHWJV8I5KhyuRJrRpTy3pKfGcPsGUhJj3LcgIz9h5AZ4ltA5PoWVIzm46hr57xsAidfsMa_-g5wL8_hDPPHr01hef1pfcKDzoGkyk59wz4aJSdQsibwcduFiDjgL6C2Sy7xqwsBDA8EXdo7Am7TGEgkXYmfMDHugIrvdfKLXxsJADo3PYLAX73QsZoJ_1gIc7DobY_vktaMszNei0ZqNVe1GRiwXMcfxOzkmWU-WNkpCU0HKvZrbHA13YppiUB0XJMXyHZCJ53JfLyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ویژه برنامه پیمان یوسفی برای جام جهانی بدلیل این که علی فتح الله زاده به میثاقی مجری سبکه سه تیکه انداخت متوقف شد و به او اعلام شده که دیگر حق ادامه تولید این برنامه رو نداره.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/persiana_Soccer/23904" target="_blank">📅 14:42 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23903">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50f475cbb4.mp4?token=YdpQufRV6waWeQTj7zIJFkGbgV0LlhvRLw0x6w1O5jXKoiDqkNUHiw_LZDMj270TCd76nEW_EpYqd3oL0ohxqhOtgr3gKaYTD5gURbK2zhAKlVdqfPqJ-olMxWJ24DxbW9Vl9GjJWJJTYqYmbDmZprB-wvKpOspXJgouWKPL-xHYNhR--JTquLtAYLQcFei0xpskjrwUYVLFEof3CD_W5yb1blD3tmemQ8XD_0Pfc7B_jDcdEf0QWbXEfAp-MnlL--Hn-V5I6C-rTHl-272JR0ujurhBlYJWIMdfdsbPBQNnBnzuIe_eF5YVeSk8ymIZqEUY_pSBUrI6aZjdPGI3Lw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50f475cbb4.mp4?token=YdpQufRV6waWeQTj7zIJFkGbgV0LlhvRLw0x6w1O5jXKoiDqkNUHiw_LZDMj270TCd76nEW_EpYqd3oL0ohxqhOtgr3gKaYTD5gURbK2zhAKlVdqfPqJ-olMxWJ24DxbW9Vl9GjJWJJTYqYmbDmZprB-wvKpOspXJgouWKPL-xHYNhR--JTquLtAYLQcFei0xpskjrwUYVLFEof3CD_W5yb1blD3tmemQ8XD_0Pfc7B_jDcdEf0QWbXEfAp-MnlL--Hn-V5I6C-rTHl-272JR0ujurhBlYJWIMdfdsbPBQNnBnzuIe_eF5YVeSk8ymIZqEUY_pSBUrI6aZjdPGI3Lw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
عادل فردوسی پور:
یه زمانی من و محرم خیلی بدمون ازهم میومد ولی الان من خیلی دوسش دارم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/persiana_Soccer/23903" target="_blank">📅 14:40 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23902">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cAzQCm3z8EsNzhcsg3pfcgi6oP0dG6-IqAnSxzzrBcA8054tL3hL7SGHkZozqowG0snOfjpDMLfj188at9O-_jzl8lBcGFx0ll_4B9b1kLcb52EbBCEZej0MZe4bQrKLWnQe4EcQYfpbsERUezfbA4RFlLcDHRlrpqu4ef2fPj3aeMb3WP09Y7NrIEaiXmAZjhzJ-4cvqayU3SpGcphogjU5W8VXXPGibMSFfVp_jLNYaRa62YtJWedQ_1RwrmrV45u_HUABjauChQkuG8cQcx_EtZ3TyfLkDBUZWgKtIvwrfVhqXJOg-ldMgk5Y4cYk-dOtgFdz-DcmY703bVjSRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
#تکمیلی؛ طبق اخبار دریافتی پرشیانا؛ محمد دانشگر مدافع 32ساله سپاهان بعد از جدایی از این تیم از طریق یک‌مدیربرنامه که رابطه نزدیکی با علی تاجرنیا داره خودش رو به استقلال پیشنهاد داده و گفته حاضره به جمه آبی پوشان پایتخت برگرده.
‼️
محمد دانشگر تابستون سال‌قبلم…</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/persiana_Soccer/23902" target="_blank">📅 14:27 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23901">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jBXE-SpqodEsobduDdOOks1Dz1ZY31-FxY-_Y-2pm3ZE1M7L97waMn-YLctcBVIVvqc7edzqMFU4Kj2oJ5PCItWE6t4SpL5lkuuosy3fOyGE9OC3i2hg766kZDbJWEGMAQxFcCQJaRhvxGRzCjj46FhsoA7slCNFoLMBK6Pb0SDJ6k11Xj96CAUCwh1MBKNH27sRjGQMRYDeRFo4dKwPyt6yhgLD_C-6p5piHzWH-glwbzN5rGKy4wXa97C1-NWfq-8rjc9wHNkqrs4utCTEbh7ISJNibHzijv63wIIxb7bfFmkBfcw3zxX_wE5puCK1HoUcvdISo6cLoLHvBB82Lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇳🇴
عملکردشاهکار ارلینگ‌هالند در لیگ‌ها و تورنمنت‌ هایی که تا امروز بازی کرده: 279 بازی و 260 گل!
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/persiana_Soccer/23901" target="_blank">📅 14:20 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23900">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NJPLDV1JdQJHZhfogcFaf2poSGYglFcpkj4SdoQBsGYZOCw17Qh16vTPwbFV4p2wRitULCINt5cEZcD91DwC5xJiQGBb1aKAdA79tJA84WoXObVtRqXhjGcI1SpXsvx_MSWFO0TyC8UKjxyQVNyrnloX8dHMdkCbRV094sV_MWdRIYKiHLfbzV_I0WNnLocVLZN-UJ0w3qXa7eHiV2_FKibDDJ8pEUwkrj36p80R60pTlW3yrbM9aKwbhZ_zOOR639mk9EOoaxxPy0tMaTMxXRG7XvrqbVWtr92kqEIxHuMKjR5qon3hZ3q0IiOjp2URcvq81WEOPQfxS7YYLQ_ZCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بااعلام‌فدراسیون‌فوتبال؛ سهمیه خارجی باشگاه‌ های لیگ برتر درفصل جدید چهار عدد خواهد بود که یکیشون حتما باید آسیایی باشه. به این شکل 3+1.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/persiana_Soccer/23900" target="_blank">📅 13:56 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23899">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lVNOHL0A7E-PaUb5F_VLvMf_r2bSSCWCfCEiqJvcQjtNOyrWRLWHlKCai8ZW9IcInYzoz6DQ92DQbmcxfR_gjdcFfUgGGhQEin-tnZuYqxJfe2iwonjf5i7ehzZec_IBKtx-fgobXEBd0LnJroAP4l7i69pvsWgg1tlVPeYB835mZ0kER4g4q_ifpO0Jtmk3EPcH2fSxk8YTY5J8a7VHDpqdPS8eD9XW6QuhJengK9KKMWFn6qVAiBv033wEE7PI2rRSkktrPOiAGAc1gBbAn5HYTczWPbnPLDbVE1WbyigvQjiEc9niGxDIo2loNdSu3LA7Kobx7D0LV_WEKxeTOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مهدی تاج رئیس فدراسیون در اردیبهشت قصد داشت استقلال رو بعنوان قهرمان این فصل رقابت‌ها انتخاب کنه و حتی‌به‌مدیران این باشگاه این موضوع اطلاع داد اما بعدِ تماس مدیران باشگاه پرسپولیس با مسعود پزشکیان و بادستوررئیس‌جمهور تاج از انتشار این خبر خودداری‌کرد.…</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/persiana_Soccer/23899" target="_blank">📅 13:46 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23898">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d55cf4416c.mp4?token=CrJcMzUq-hUykXz6jRz7wj62EJtx4oJ2jyTNIdhXfFM4dBipaHF0HvmxI4VguSqWFuJBiIv0bsKxQcAUeBVIlhTWb_uqxqjzu-kvLWk8mwtGMPC9EfgArVRa--8LjvkbRV2JWIQAewMgThbQm6KoGgZea0kTEvGcAcBV5t09kp_LSgy1c1-WL9hJ8Vf8aMPE2FQQht951ouZu9z4prwV_muSBX07QLcpUG8tFOZFXiI0kXmzlTcKjkGYCYaX7qnlrbZq4UZhAVodr7BETtkh6dyBypTzZGXC61XOquz8Or-L5_4KrdLUtlsfqB-hkYPCAC0buVsVOMk26vmY0ay0zA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d55cf4416c.mp4?token=CrJcMzUq-hUykXz6jRz7wj62EJtx4oJ2jyTNIdhXfFM4dBipaHF0HvmxI4VguSqWFuJBiIv0bsKxQcAUeBVIlhTWb_uqxqjzu-kvLWk8mwtGMPC9EfgArVRa--8LjvkbRV2JWIQAewMgThbQm6KoGgZea0kTEvGcAcBV5t09kp_LSgy1c1-WL9hJ8Vf8aMPE2FQQht951ouZu9z4prwV_muSBX07QLcpUG8tFOZFXiI0kXmzlTcKjkGYCYaX7qnlrbZq4UZhAVodr7BETtkh6dyBypTzZGXC61XOquz8Or-L5_4KrdLUtlsfqB-hkYPCAC0buVsVOMk26vmY0ay0zA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
لوکاس برگوال ستاره تاتنهام به سرعت داره به یکی از مطرح‌ترین ستاره‌های فوتبال تبدیل میشه. این هافبک سوئدی‌که ۲۰ سال سن داره نه تنها بخاطر ورزش حرفه‌ای تو جام جهانی ۲۰۲۶ آمریکا معروف شده بلکه به خاطر صورت زیباش هم وایرال شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/persiana_Soccer/23898" target="_blank">📅 13:41 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23897">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8cf4e4f15.mp4?token=ub63aHCT54WLSkieYf6P5i9QUwQ5zyL0hgl0U_L9DQqWabgULpLBU7Cefa04EIAaBRXmLNTKzl0UyO9EE_AtaqTV-GmMdurWmMmuxQOJvOaQTKch_sweF_F-0TMqixZEH2-1UPG8io-SFLb-9INbOnQDvRjJKRgWl-PqTsovBo66MmknNCPNYGGuxLDoHKeFjR-5-DEiejg750ogcSch3qLnDg3swz354m0ewodjlkvYdcqk-_GnuM_CFo4p4oq4iZVuKC0CJNJ4rPn8q9tC7Wx4Li7T6LSf-RjlhG5cgCZKRFG8SMipyQWsVFiRlu8XoUvypWRYNvbv5SkNt2JsIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8cf4e4f15.mp4?token=ub63aHCT54WLSkieYf6P5i9QUwQ5zyL0hgl0U_L9DQqWabgULpLBU7Cefa04EIAaBRXmLNTKzl0UyO9EE_AtaqTV-GmMdurWmMmuxQOJvOaQTKch_sweF_F-0TMqixZEH2-1UPG8io-SFLb-9INbOnQDvRjJKRgWl-PqTsovBo66MmknNCPNYGGuxLDoHKeFjR-5-DEiejg750ogcSch3qLnDg3swz354m0ewodjlkvYdcqk-_GnuM_CFo4p4oq4iZVuKC0CJNJ4rPn8q9tC7Wx4Li7T6LSf-RjlhG5cgCZKRFG8SMipyQWsVFiRlu8XoUvypWRYNvbv5SkNt2JsIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خداداد عزیزی مهمون ویژه برنامه جام جهانی یه لحظه از دست جواد خیابانی عصبی شد پا شد زد تو سر خودش و نشست گفت من استعفا میدم.
😂
😂
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/persiana_Soccer/23897" target="_blank">📅 13:26 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23896">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bc9m9S2Z_jI_BS9LJCpbqfWmEf7rCWgY-xC90NN3lg-FE9_GmrNz7qCKgUsfXfhPtxNnWlTu571bPBgHmz72hDKn8VrWyZcdp7xUY1ZHipt8PGIYeWswvZ-TPP9wlcLY3lwUky2ufshyXp-Dr63usIEmDg9a3GqUdzvOVDQMvHoQbE-1elZFOZPPW1GYaECAJJ9m7sIHXJcOhiOXpApEXkKg7SHeLz7-VP_LHMPjJiSjcfVma-8iNXkFvhb5dj_ZM2ItOYsy-5p6LwI1dkZUeuic1h0LzAKLnGi-ngwpVtVsF1jj9EtvGlNep6oVUZn886kXhZX_p7Ml6ZoDrOOlrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول گروه C رقابت های جام جهانی در پایان هفته دوم؛ برزیل سه هیچ هائیتی رو برد و مراکش هم‌با یک گل از سد اسکاتلند گذشت. بازی های هفته اخر بسیار جذاب، مهیج و تماشایی خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/persiana_Soccer/23896" target="_blank">📅 12:59 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23895">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mXdP_DKYV4KPPbaxRFjJlvYvhm0Z8Q2WBsJ-M5re-B5wWD2sYQTjW4_B7vWQRA2mt8CBpEhBQziJSSXR66X0JsTnv8uDeNN6TxGAwVLuj2ApubvF79ggP-ars1lD8Az28SuEwQyHuc2K3i-5nIOUtrMi07WF2eMp4VyixCC_jVmAISpqUDLeXKO3XGd8cu57mQM6tWrE0PSTTbZN3lxUnSZriqw5H8oC0ExRh-1wWliP0Dt8_ugUHGTE2eSVP1abS8MyTZURyFPdCxCtHAW4D92E6URwbrbgNisk3AjGu0qWKoLgWLAQq-HVX5K0VbzNrm6ma1eA_HZv5CUxJUFAAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دقیقا 19 روزپیش؛ صبح 21 اردیبهشت؛ مهدی تاج با تاجرنیا رئیس‌هیات‌مدیره‌استقلال تماس گرفت و به او گفته بود که فدراسیون به این نتیجه رسیده که امکان برگزاری لیگ وجود نداره و بزودی استقلال رو بعنوان قهرمان لیگ معرفی میکنیم اما تماس‌های اخیر حدادی مدیرعامل باشگاه…</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/persiana_Soccer/23895" target="_blank">📅 12:40 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23894">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b18c6a9792.mp4?token=DHlFd_PVuOwMmOkRKyk5ObGhzugtOvdp7lGXo4bamkwZdXxXXFReErR3RtTD2EXtKAyvlV48tMBy7lngMLNK8XOtv37ZXN_lF9DX-nE62TdbiWVWv6Dte3ifdLtV9BBxkBMGKrKnTinqmQtiEEqGQieFEVgFioclQ7yfEMaZ6w71n4lztN8sbUQVcePwOJmhu3-EO7RYZwtWjqwiL6MqVPNBwelI6pIlX2mGYvpXFtcBeqINQDT6nBYjEHEjMNXZ7W3Y5EbWxcXdNGrIJLiX_xCRiLFx_cWJSMrtH7gcCWBj8bGeIfWcpEmGIFlU6R5vPcIce2dWsuj8RHpjz63td1kmekeuaDEA4BKRTYldC2V-1Z8yapvYFc9Iq9IVKj_-CEbJImMTrk5QcvlX6WX1CiWFahOpaEtcqzoNh5nzZQspuhY9QrcbVglQYNe6eibdigEcXVCUvyrmGrfIqvqHRk_w882HzbxUTWJxROhXUTFhU1DWt25nko6cAPEpm97Jvzu1wXJZmph1E8OgZKrHovcTJsq78G0DcJPc07YbH5NE7zq0EIVNjuYIhqW4DZn2V9UxAYVYixLHIPdfPfnXLl5kj9rffIFT-ENUZc9Ss_F2TRdpGA_c-g6dpSnqs6XRvYAdY0crgwa0H6OWedZrzabiF4pTjVAEQOCquBD9vJM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b18c6a9792.mp4?token=DHlFd_PVuOwMmOkRKyk5ObGhzugtOvdp7lGXo4bamkwZdXxXXFReErR3RtTD2EXtKAyvlV48tMBy7lngMLNK8XOtv37ZXN_lF9DX-nE62TdbiWVWv6Dte3ifdLtV9BBxkBMGKrKnTinqmQtiEEqGQieFEVgFioclQ7yfEMaZ6w71n4lztN8sbUQVcePwOJmhu3-EO7RYZwtWjqwiL6MqVPNBwelI6pIlX2mGYvpXFtcBeqINQDT6nBYjEHEjMNXZ7W3Y5EbWxcXdNGrIJLiX_xCRiLFx_cWJSMrtH7gcCWBj8bGeIfWcpEmGIFlU6R5vPcIce2dWsuj8RHpjz63td1kmekeuaDEA4BKRTYldC2V-1Z8yapvYFc9Iq9IVKj_-CEbJImMTrk5QcvlX6WX1CiWFahOpaEtcqzoNh5nzZQspuhY9QrcbVglQYNe6eibdigEcXVCUvyrmGrfIqvqHRk_w882HzbxUTWJxROhXUTFhU1DWt25nko6cAPEpm97Jvzu1wXJZmph1E8OgZKrHovcTJsq78G0DcJPc07YbH5NE7zq0EIVNjuYIhqW4DZn2V9UxAYVYixLHIPdfPfnXLl5kj9rffIFT-ENUZc9Ss_F2TRdpGA_c-g6dpSnqs6XRvYAdY0crgwa0H6OWedZrzabiF4pTjVAEQOCquBD9vJM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
گلچینی از صحبت‌های جواد خیابانی در گفتگو با امیر حسین قیاسی؛ مجری برنامه هنگ کرد قشنگ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/persiana_Soccer/23894" target="_blank">📅 12:27 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23893">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ou-Kpbd7cwMLaz7KrDAGbQuoqY8BqXm6so_3A6SyZ03HN7NoU4hDQmYP6JocbyiraCmSZGkA5fydqxXQMUuOzo_g8lPFUIdLtNaCvRmdQJ643v7zM1QP3YZG-PISnV-oy2E_DsU9IjICUy4c_aRCidwxXgaB6Ig-QPJaKcadOTa8vqvCuntTYr_Ic80xeZ1rf-z2lJu4tGkETFIMLTIBjsY1BRVe-Zd44JtFV14yeBJTUCW6r9sHyll4fKiLXG2SB7SSlXIV2OZTGHsU2F_AIPQal9oxsfKZ72FJn7U16oP25BFQ8uKCcLU8S4g1dBE_HIek9QjgeD6vQQFac-ro6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق شنیده‌های رسانه پرشیانا؛ به احتمال فراوان فصل اینده رقابت‌های لیگ برتر 18 تیمی خواهد شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/persiana_Soccer/23893" target="_blank">📅 12:08 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23892">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/unikbr9RIMk-onV4RXgTzrfOLg70NbXP2HgrkynxJYFO4b6YNr9XFCqDH7iqaKP3eYO_12VXDmkTln2CNS6m9eg46gNkBz1gx-H81PNT1-wbRW6qh2msBNx3Gqy-IwSk9a4v3engvr4B9v4uTKaoY8nKpgtSfxr7iPC1gVrO66YwckUV5kU4pdzxhj6FrQAmFBg9mphgnbyIrow9foScD9ZdCeABD1vrwIW4NfSqcNUsIwA-adM-Y7JZUQG07heKo8AGdUn5hh30pSLMuITlrudySCrB7FyEg0u74XAhWLBZiQ3Q-5ZwbvYJ2gXhhVOO_lPrMDDbQjQ3yLC7vAjsmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق آخرین اخبار دریافتی پرشیانا؛ دراگان اسکوچیچ ظرف 72 ساااعت آینده به تهران خواهد آمد تا مذاکرات نهایی رو حضوری با مدیران باشگاه پرسپولیس داشته باشد. هیچ چیزی قطعی نشده. اوسمار 50 درصدشانس داره. اسکوم 50 درصد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/persiana_Soccer/23892" target="_blank">📅 11:50 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23891">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0ae405613.mp4?token=XrPMM2bptrRpTPwFGPw9Nw3u30szzY9lL7o1NwbQNmCrRWO2aQ7Szrq4OCQnEpWk2RlNLEqA3TzNHq6AcM3oK4Z_RLzc_JbTsqWHGzXXiGL179HaKAJGhhmD8h0cyKIT2egSa1en18mWO-u1swrpOqvMEC3IPNbS6TtyyjwR8UZr-Zs_bxqwLC6PqxUHuZpjulVCqRzFFjArNEQwSxoyQTrYFxpBW6m0YRtaCP5aKuvdERWDvHxQU_eGIKKUOfhOmcKacLsFzEmw6np6OXrPJfpNszcYCcojFGATAhl4lF9GweWyzddZe9OwA33IaNiY4MPyYx97zOkCenHAWL9j-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0ae405613.mp4?token=XrPMM2bptrRpTPwFGPw9Nw3u30szzY9lL7o1NwbQNmCrRWO2aQ7Szrq4OCQnEpWk2RlNLEqA3TzNHq6AcM3oK4Z_RLzc_JbTsqWHGzXXiGL179HaKAJGhhmD8h0cyKIT2egSa1en18mWO-u1swrpOqvMEC3IPNbS6TtyyjwR8UZr-Zs_bxqwLC6PqxUHuZpjulVCqRzFFjArNEQwSxoyQTrYFxpBW6m0YRtaCP5aKuvdERWDvHxQU_eGIKKUOfhOmcKacLsFzEmw6np6OXrPJfpNszcYCcojFGATAhl4lF9GweWyzddZe9OwA33IaNiY4MPyYx97zOkCenHAWL9j-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
👤
واکنش‌طرفداران تیم‌ملی فرانسه وقتی بعد چک کردن وار فکر کردن علیرضا فغانی براشون تو بازی مقابل تیم ملی سنگال پنالتی گرفته ولی...
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/persiana_Soccer/23891" target="_blank">📅 11:45 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23890">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bbh66Mgf2IjQzsozjtSM7njjV_bbmUAWwqRNwXz-CzjfDukk_JBOv3kmUiGID6s3pbQK4FkYlhcgfyNWaevFQ46h2CimImz9pGuJiPZgbR2pSnWzC8IT5gFEpJmRhFENgShao-GbCEQr5CdUga9_dUM4LpgbwqLes7jN8APineMnfd68tez6OnbF1LegXKby44RU1sAcwZTYDHjerOQjSR_qhn0nay3c6kKd-yeWk7ILJoV4JRFepH35AJRW4uE6bZg_AHxBQ8OY-V5p7YbijefCIlZcCn5gR9t2WtYMFlo2WpLTcID8Lqx7156r6lzrB2nHMItOnKYDWTbFuys03Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
👤
بااعلام‌فابریزیورومانو؛نیمارجونیور ستاره برزیل که به دلیل مصدومیت دیدار با مراکش رو از دست داده بود حالا در حال ریکاوریه اما ‌کادر فنی نخواسته روش ریسک کنه و او رو برای دیدار مقابل تیم ملی هائیتی خط زده که به آمادگی کامل برسه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/persiana_Soccer/23890" target="_blank">📅 11:31 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23889">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f8eb0d50c.mp4?token=tyKWYnk3plTIhZSoGT8T0A-ctDwiF29ZU0mvzliPmWByRLXsllrpmc0okPV7GlubxGXhyUTXSTKQ1tqRqSoQhNeiGbiTZhzTiAwAeimvg4l-gGpIWEBY9XOmJCv_ep17en2DVl0qpE-RPyV86srcXh-0bM2klUybfjFNL4kKVtTfbwDdqMh3mQqxIkj0SbKsiqg19k7gDw5oWz5BUsa16O1Sm7M1R6A0NNotfvlF76Ue2Se3zl75d_8_NKm0S-CyjaPLgQD1V88izoajrzd2BG27lZgy_zKlTvRP-tgZXI4XrLDTa1q64zWvsErU1ULMIfQDhfnUdYIcKfINnGqRfYrhoxU8BiMjT6qlm0j56_vqLdDMq-ISBcuOZrihZHa1dTBh6wgDb5Q5IWxo5GylSwmZZbGMYOAEhdgG0YeLR2VtD2UMmoki4xuBF8NqCdQRjqD9etxfMs2XBkR2aHciyesuL99rnOHIbBpp2EIB50fGrbqYypyEnplz0YjexlnapFq4kQqkZTketXnzx8d8DUgDfhE7sXcvdtGiBZMDXmyjWAfPjuLjw1ofhJ7vKKxGGRdgc03PLn3fL2PXMmp_7TOPBsIW_X-BBhmrvzXvdD6_eLp0Y3B7lDWKMybnIJpEVl6u8bTpJ8QhZzBDNFYOwoqAr0oaAH4dJblJrLHCAoI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f8eb0d50c.mp4?token=tyKWYnk3plTIhZSoGT8T0A-ctDwiF29ZU0mvzliPmWByRLXsllrpmc0okPV7GlubxGXhyUTXSTKQ1tqRqSoQhNeiGbiTZhzTiAwAeimvg4l-gGpIWEBY9XOmJCv_ep17en2DVl0qpE-RPyV86srcXh-0bM2klUybfjFNL4kKVtTfbwDdqMh3mQqxIkj0SbKsiqg19k7gDw5oWz5BUsa16O1Sm7M1R6A0NNotfvlF76Ue2Se3zl75d_8_NKm0S-CyjaPLgQD1V88izoajrzd2BG27lZgy_zKlTvRP-tgZXI4XrLDTa1q64zWvsErU1ULMIfQDhfnUdYIcKfINnGqRfYrhoxU8BiMjT6qlm0j56_vqLdDMq-ISBcuOZrihZHa1dTBh6wgDb5Q5IWxo5GylSwmZZbGMYOAEhdgG0YeLR2VtD2UMmoki4xuBF8NqCdQRjqD9etxfMs2XBkR2aHciyesuL99rnOHIbBpp2EIB50fGrbqYypyEnplz0YjexlnapFq4kQqkZTketXnzx8d8DUgDfhE7sXcvdtGiBZMDXmyjWAfPjuLjw1ofhJ7vKKxGGRdgc03PLn3fL2PXMmp_7TOPBsIW_X-BBhmrvzXvdD6_eLp0Y3B7lDWKMybnIJpEVl6u8bTpJ8QhZzBDNFYOwoqAr0oaAH4dJblJrLHCAoI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
تماس‌تلفنی امیرحسین‌قیاسی با «سردار آزمون» وسط برنامه بفرماییدجام: من ایـرانی الاصل هستم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/persiana_Soccer/23889" target="_blank">📅 11:05 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23888">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tGraSaI-9Fcst90tlBJaTvqEfl5EUyvhzphcvR1QKQCDH6Xqg-FYM68BnMbEK-zhY93x2Qg4xFJFmNNzsY7vahoOzKZryibyY2XLTmMnNAiyPuRVTZEx9Z0_Ij7BSd61f_seH4IOXneExisd0G7ub4F3P4Po3tzNSquZflsGwT0qv9mZ9zxgHUkR18rbLWwmQJvbaNVA3KJ6MSbsoFgc63jnSSUPoqWCpQwt1Aphj8L_BuDur_TFND6k-ADSQktoO2zxPWbY7lZ1kugckFdKMZZrewlXrgFvgP8oNJTm9XTdwHa13DJV6dqpCh_gpN9Git5yhQanyAoK1LX1BA47jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇪
👤
تیبو کورتوا دروازه‌بان تیم ملی بلژیک:
تیم ایران یک مدافع راست‌خطرناک و گلزن به نام رامین رضاییان دارند که زیاد در حملات تیم شرکت می‌کند و ارسال‌های‌دقیقی‌انجام میده بایدمراقبش‌باشیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/persiana_Soccer/23888" target="_blank">📅 10:38 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23887">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55029334cb.mp4?token=d6T-6rYv_zk9dM-YZ8BifZ6D3YdG5OWqlGRR5O7ZWh69-uJrJS3p-TRal2TJ_MKYn4blXLbzi3PESzWs0Ip5BphJPP5ICZmvpVnvNTmbiEcHIO7n7auxfffOm0VAXASURNL8LJz4WZrWHRq6XkvVAiHuLKyncqcc_39bar_Xan4_D8cmXxTc4wQeObEA0_LifYi059QBYA7hmN6seeipngfhwQofo6Jfn1lGWA5mSyjV590IGe5AfhioTtdi5uisr172FGPSLF1tWjXHTar3MUYeNmb0Y6XOHH3jmP8f-6aDYQBXfYUWp4mWXDp85jCQ7yJD6bXvppmUfRae-nkrOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55029334cb.mp4?token=d6T-6rYv_zk9dM-YZ8BifZ6D3YdG5OWqlGRR5O7ZWh69-uJrJS3p-TRal2TJ_MKYn4blXLbzi3PESzWs0Ip5BphJPP5ICZmvpVnvNTmbiEcHIO7n7auxfffOm0VAXASURNL8LJz4WZrWHRq6XkvVAiHuLKyncqcc_39bar_Xan4_D8cmXxTc4wQeObEA0_LifYi059QBYA7hmN6seeipngfhwQofo6Jfn1lGWA5mSyjV590IGe5AfhioTtdi5uisr172FGPSLF1tWjXHTar3MUYeNmb0Y6XOHH3jmP8f-6aDYQBXfYUWp4mWXDp85jCQ7yJD6bXvppmUfRae-nkrOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
#فکت
؛گل‌اول‌تیم‌قهرمان‌درجام‌جهانی در 3 دوره اخیر این رقابت از روی نقطه پنالتی به ثمر رسیده.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/persiana_Soccer/23887" target="_blank">📅 10:38 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23886">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TA_7XELbzp2pe8uKyX2r0liZGSPjJMGJseGR6WUmiLPrIpegq9KOS3iz1R6YhziEnN19Q75gkKe3cR3bnQ2Mq0uLymLNNySVH_dfzynXXweBKWeQjtrokTmETofdAhlE_WbsLlH14ZWhIYhWmQmpq5-UdZyy7kLRiuPe8AK1yNBq9tom5cYBPjrde6Mflxtvn-oexFAj8zcbJnxgncW8cZGxN5MhOR8H0CIOSX57K2ID6pg7r7en7kwwGeofvo_vqrLyq7DuOZ444eIAU93SVv3z5HAqQ4P8psbICJrNiIkxODB1TKePxuqiD04zPKSjLf7ZedAYF4o-1GY7yHHxVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
55 درصد از علاقه‌مندان به فوتبال، فقط 4 سال یکبار شرط میبندن!
حالا چرا جام جهانی
❓
خیلی از نتایج تابلو و قابل حدسه
💯
مافیا که کارش دستکاری کردن نتایجه، زورش به جام‌جهانی نمیرسه و نتایج واقعیه
👀
بدلیل تعداد زیاد بازی ها، دستت بازه و کنترل ریسک و سرمایه آسونه!
🔽
🔼
💡
کافیه یه سایت معتبر پیدا کنی که شارژ کردنش آسون باشه و بدونی پولت امن میمونه، MelBet اسپانسر رسمی جام جهانی، همونیه که دنبالشی!
برای ورود به سایت فیلترشکن خود را خاموش کنید
🌐
MelBet1.net
🌐
MelBet1.net</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/persiana_Soccer/23886" target="_blank">📅 10:38 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23885">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hBtA9ZK6IsxEWGNprnqSZT652Dsc1itnjr74szg16sxCF_IhlIf_DkjQg0yobYgIwRblHOShU17VsiJkgH2KFVV88s0yyNyPwMAmCPUSdvexRTLKXyMMUE40dMSCp2fPbkj_o2hc1rKgeBo-EynfnbW3j4plG0kwD32lxi-7loSVhDShN0NFExoIyVfyr4Ph9y6_KE9rAk6Gqpech0Co6mS9Q-uWPpnhCaGThmEPbPBsBHkP5r3w7PvPKZ_Vd622auEFlJE7Ufb61JRRW-G884ThqOOHKw9_32hTuiex9nAYGuGr1invcW7tubetLJDXb_RcBOtZEUb8pZMVQPX9ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛باشگاه‌پرسپولیس بلافاصله بعد از پرداخت مبلغ  توافق شده به باشگاه روبین کازان از کسری طاهری خرید‌جدیدخود رونمایی خواهد کرد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/persiana_Soccer/23885" target="_blank">📅 10:03 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23884">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2831c060e3.mp4?token=JCbKz0WyyN4i6-92D3xH6oKNIp9bI3EqdycWPBiKh1dP9L7-EkWTchLE1h9bKGUjRrs-Hqmp6LxAP8BhxJTObhRLB1rR8Kv3Wspz9UhJfER9aieZFfDqX_tb1-P3H1tkIDEcaSDjS2zCo8HN_7MaAQ_EJN0hsupU7TTGeyBF3cx8Yg2XAiu7RMmAod0UQImzpHUQD__SyPiivhJJV2diEf6TQO-6L2B5DXKFV794n-ICx59tYjNv1Ul55DmsruIyg_i6HUpwOhVtDYRnACF7XvLIWLJp9tE22rS1g9onOUr_4Bz-aJgmmQ5wKGcUphLYNy_dyDdy_CwGUcQ_qzgUww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2831c060e3.mp4?token=JCbKz0WyyN4i6-92D3xH6oKNIp9bI3EqdycWPBiKh1dP9L7-EkWTchLE1h9bKGUjRrs-Hqmp6LxAP8BhxJTObhRLB1rR8Kv3Wspz9UhJfER9aieZFfDqX_tb1-P3H1tkIDEcaSDjS2zCo8HN_7MaAQ_EJN0hsupU7TTGeyBF3cx8Yg2XAiu7RMmAod0UQImzpHUQD__SyPiivhJJV2diEf6TQO-6L2B5DXKFV794n-ICx59tYjNv1Ul55DmsruIyg_i6HUpwOhVtDYRnACF7XvLIWLJp9tE22rS1g9onOUr_4Bz-aJgmmQ5wKGcUphLYNy_dyDdy_CwGUcQ_qzgUww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
بعضی حرفاوجملات هستن که ارزش داره روزی چند بار بشنوی؛ جمله‌ای که این داداشمون تو برنامه دیشب ابوطالب گفت واقعا باید با آب طلا نوشتش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/persiana_Soccer/23884" target="_blank">📅 09:46 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23883">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GEl1tYLZGQcc-xBKQWOh-YVmIMBQOCdLEQxacVu-SqJxijkT4kSLuOemkb4CoOTCqXMU0_sps9EdqsZuqe97ifjywBNptoWvOZMJJAaJgk6nm3rgMUW7BaKKu8BH9BkCPSvcdb86XNKKKYKrgzblCyyUPJq98YFlfHKXF2IV6aDhur2ZwNGSC6vH3y9fqV1iIw4uXeAk4vkE2PmnYQa5rIFheg6CL-CCwvQ2luvW7lfNfk5Iuv6N8I3eQXcUURRevxVU1T3bPUDshKkl4etoa7gv3defIkzD5nrsm7Lh5oxNgYQc0F-DFbrxNdpsNwM8qILrcTUeDvMd-xtNTG4Udg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
یادی‌کنیم‌از واکنش‌کریس‌رونالدو وقتی مسی بعد از کوپا آمریکا 2016 از فوتبال‌ملی خدا حافظی کرد: دیدن مسی درحال‌گریه کردن واقعاً ناراحتم میکنه و امیدوارم به‌تیم‌ملی برگرده چون‌اونا بهش نیاز دارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/persiana_Soccer/23883" target="_blank">📅 09:22 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23882">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/klZ54sgaBkbkIuq9CpUkKZgFPxPE8AR9b9SP9A-2lpE7YLLWLfJi9P6LwtV8wTJetId38uUBU6k3C0pdDzjAAzXIfLN78ueJeBXIcTMkJJLiwgGX7803-slHQuiEjB-Pp8V78fBlYzWcQrQriQu_MGSH4Ul_12exm_UzMpeQcD7SQ3dBSmF4sywF2DtBeuIuqzTcRulj2UeCSlw_5-xHx-ADWmiaOcYJUDE04d0P_yzG4L1i_Fbdb2PB760Cg_urM7jzfPzZdJUBOuBdWbT4NDERDcA8OmDXTVMCWjH2NSIy7kn6h8_r5_ASZITdu1V2gdvQY24NnddytoJtUNJ9aA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول گروه C رقابت های جام جهانی در پایان هفته دوم؛ برزیل سه هیچ هائیتی رو برد و مراکش هم‌با یک گل از سد اسکاتلند گذشت. بازی های هفته اخر بسیار جذاب، مهیج و تماشایی خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/persiana_Soccer/23882" target="_blank">📅 09:05 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23880">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EHsB_neLrL5cuwkk7hYahr0l4-mVkv3GZERzOQs1oc36uu6WHPix-cV_EIUCoSu8ih88K4iAipWoeikfAszFGBzngLO53IfO6VuX3IMEk4BDhu3I4JRc93701-6AdqACJZVfkrbTogxTdGt0BAQFCHRpPnP_KH6mpo6QmKdriWRknly_cjv1-v2j1bhM1g-BI7XmWuPWunUp7jSpVCXY-qM55HVvgjjHXDK_3DAysdC-y8qOR0LyWL-sJcCb7hSll2N8FdKaKcQCeAEDKRzNj3IA0YVAjoOuSY5uuZGV9r7FhtV-OFdY3COJGhqFHkITVq0w4uZw9bUGAKFvjC2JDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج دیدارهای دوم ایران در ادوار مختلف جام جهانی؛ پبروزی دو بد صفر شاگردان کی روش مقابل ولز بهترین نتیجه در هفته های دوم جام جهانی.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/persiana_Soccer/23880" target="_blank">📅 08:33 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23879">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">📊
جدول گروه C رقابت های جام جهانی در پایان هفته دوم؛ برزیل سه هیچ هائیتی رو برد و مراکش هم‌با یک گل از سد اسکاتلند گذشت. بازی های هفته اخر بسیار جذاب، مهیج و تماشایی خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/persiana_Soccer/23879" target="_blank">📅 08:11 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23878">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mu-ds9iLQ-1L4T9i5a9PTVr-fqZ9narnEyzAq8DmjEy7VhSbE1p2VY1oH1W9f3jp7km2e1_SUE1F1ofOotCheE9zeT_8QHIygRnmouL2YOHG0EDNW0oIY4SjW3xKThvhkTRedd35rW2zKLVgrS3OvGEKmv_UotdShQ5bnKRZtuq5GFrrX_U0xi0Nquy_Cp8y9i_S1vU8nU0ItJd28rz8sLP2BI9zxDP5xWhBqVifLIgIoQmXU05S7eQB9yFVK0kBja7qQEXRopO3IFiv-O5SHPMUw262LS9hmXDY7M7l1VE3o6ciHyyO7mUVDAwkcoNOUfzf4uv_x7vCjJHcw_Ykgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارهای‌امروز؛ مصاف برزیلی‌ها برابر تیم هائیتی و دوئل تماشایی یاران فن‌دایک vs گیوکرش
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/persiana_Soccer/23878" target="_blank">📅 07:55 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23875">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GNJCE_7vozg9oOohel7GOx6j9q2Omg_GDAy5SfaZZf1zdHigSl5CWhmAY6ggmIWqYNnLzSpz0MKgaBgVQrL3eAGNEg6bbccK6jtCZGQzwkKzMm6JpkOlQtkdpOtUolsDB9sLeWWvhsxoY0R6H8Wko511cUQ38sw86YVeuxPMRzgeYSp9roBeMxwKPrvsWT0qDHylDxQapeaFiDZYnfnJb5flHaLxZYj4pN2siWWHKKHdt-Whpfn1WIE2KUfj0sOvAixOWvAtZHnNVsFNlddlgItZ7kPu5zxwiHGXYdp1O1MRDevPsBFUzbQuyNAbaC3GvmF9B_JZ4C63HCOb9IjsOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
قیمت خانه در محله‌های مختلف تهران در سال ۱۳۴۶ چقدر بوده است؟
جالب اینجاست که در متن آگهی ذکر شده مردم قدرت خرید مسکن ندارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/persiana_Soccer/23875" target="_blank">📅 01:54 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23874">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HgU3_5xA_6D9vLwB3XsXpLUgQ6VpvF57D0NKNaGuciahBFj_keqBBEgY65d7Bkm017S3YV_YFpwxjNVbwuTvEkY9qYHyaaV_T5_EOe92N5hAHJAVjRv-XL51FB1147PjhQlM1seAEatgJ-F9mR6BQBwXrhn0_vylsxkTPdKv9bmSAoWdoGX--sNCt_oWg2qyQDLQh58atJdzwPOsgiJ7a91wHaBNmsi244v-hcJIstHqAQKGdhYCIRfTII3forGirNzIW3sSDnySLiTp5pq-_A5B1ILQE1N9vRyNKQcSTSHOzw0T9yCwq_E8iWJNlStx42TE7OXAkYVNcWvaUlStYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بانک‌شهر برای دوفصل‌حضور در پرسپولیس آفر 2.2میلیون‌یورویی‌به‌‌دراگان‌ اسکوچیچ داده که مورد قبول سرمربی سابق تیم ملی و باشگاه تراکتور قرار گرفته. حالا تنها مانع راضی کردن اوسمار ویرا برای فسخ قراردادش با سرخپوشان پایتخت است.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/persiana_Soccer/23874" target="_blank">📅 01:48 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23873">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">▶️
قسمت‌‌‌ نهم‌ ویژه‌برنامه‌‌فان‌‌جدید ابوطالب حسینی برای رقابت‌های جام جهانی 2026؛ عالیه حتما ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/persiana_Soccer/23873" target="_blank">📅 01:28 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23872">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B19vtx0RU7JE6JDTL9Kydxt-PNOUSp_VJcgEmHhlV3q59eRA_s1_KEw3prZngVnverzqOX7wYmXHqS31ziRdJhODtyqxS7H7x_TeSFWAYzPklLBF3MylXWKMtRjVz4tz2Wy6vzLRE7OFyCgzQmimZgughFtOTjUz0hWBiGuZ5-YdFe78xtp2u5aeaUZJRDhTceQsU58_q6E8s7vIVtEBqvzFwFfiUFbYAtMUkE-MgE31USoOncfmAn53pHH0aCHgm3fz0OmxiP6U5APreTtcwVRCnAJAONz7aWtjWaOCCsmIIe3-TNQfXFuNcR4_l707pRNcUDSq26hcHNSR5fcVTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
خوزه فلیکس دیاز: رئال مادرید با درخواست نیکو پاز برای‌ حضور در کومو به مدت یک فصل دیگر و بازگشت به رئال درتابستان‌سال‌بعد موافقت کرده.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/persiana_Soccer/23872" target="_blank">📅 01:08 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23871">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AtKJAosBOHL9MxvAWM5hNAt7ABBWfk-YVfkp3nWdMiXs9TDjpwcyM5csSJTpDKVNvKONrgqvKsMhch70z2lukKcS4yIj55Fc08SzAVC7Cec72FAWsUs1CcS1jITy97nQv-X_bTGgGLHlxtvE5MD-mKLtOFqq-hZxhgbIDX-kXqiKO3Ki4LOTULU3QbrE5ztua2c2MXMCO24NIv_Dxi4QnAezqKF-9uZ8ySmBpynfX-4TB28UGCcO4SGHo86mB2btyu0oVncQupbeu6yrs7DxNhEdijiTEqvj9NNAgeGXkg05jOXfGEzCZqmvXWuUHaFvf7Ydc6apVCxfDqA6e3q_0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارهای‌امروز؛
مصاف برزیلی‌ها برابر تیم هائیتی و دوئل تماشایی یاران فن‌دایک vs گیوکرش
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/persiana_Soccer/23871" target="_blank">📅 01:04 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23870">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A3KNSfHzUdK1RI6y5f5rUzpODS0gcMldbWWSHFliM16D3QW5_hd-CuXGzFGLzWX2sPxgB57PjkKI9tDDQz7e7_njflTtUHrfSWAV3SB-d0mmE1U9-aB6OvQ2vD60VwkWGjSIlkN943o0qjnLtJqzWofZikBXiNAzQwZj-xLgC3KfdZ5C41KNSRplz7jJZpjlMWWv3JYH8DfAjQ8suegA-s47sST7TbfXBrQBXQUPp8v8LCMqTAyrXrZ85LI5LULPQWdhRhuHNGwRZ3ZH_BIoa7ITu6RUSt_BrNwz7mo0QlXa-iabbLE7YDcE2j1YRKA5cV4ACaMnA2-O3ga5o-k72w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌ دیدارهای‌‌‌ دیروز؛
از باخت سنگین قطری‌ها برابر کانادا تا صعود مکزیک و آمریکا به دور حذفی.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/persiana_Soccer/23870" target="_blank">📅 01:04 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23868">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">⚽️
ویدیوکامل‌ویژه‌برنامه‌امشب‌عادل‌برای جام جهانی 2026 با حضور اوسمار ویرا سرمربی پرسپولیس.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/persiana_Soccer/23868" target="_blank">📅 00:49 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23867">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s3TmmfhJjo9j3b6DGmCF1yYWyjWyPcf_VUPK15pQTUpNiIZOQb1AIPp9CmvdNPg3ni5WlYX6eaIzOR9NZhUZiMVXyukLZ9AzrZShTQy_c8g4x_DcAjaaCRYwuUKizvG0btxxEeDYQb1gw46KGwyx29J3fck4-PUW5HWRPzrKH0aZONgwCjQlWDbbCkxFyTR-S0UJZdTJHHVqG2dqlWwJokmS8FQNtMDRwlJe_tmvHr9T8LSSBDZjZK3TRgbEER2ptbEHRAOGBrFMl4wuB6-y0AxYaoX5PZ7GXccqqIE7HQ3LzdeW3a0kJTxYJ7lKZXZ95ha9I7adF-p1WefZzouBZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛پیروخبر اخیررسانه پرشیانا؛ حالا خبر رسیده که‌مدیریت‌باشگاه‌استقلال برای عقد قرار دادی‌ چهارساله‌با پوریا شهرآبادی مهاجم 20 ساله گل گهر به توافق‌کامل و نهایی رسیده و درصورت توافق بامدیران تیم گل گهر این انتقال انجام خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/persiana_Soccer/23867" target="_blank">📅 00:45 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23866">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">✅
هفته‌دوم‌جام‌جهانی 2026؛ بعدِ مکزیک، آمریکا دیگر میزبان جام‌جهانی‌دومین پیروزی پیاپی اش رو بدست اورد و قاطعانه راهی مرحله حذفی شد.
😀
استرالیا
0️⃣
-
2️⃣
آمریکا
🇺🇸
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/persiana_Soccer/23866" target="_blank">📅 00:41 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23865">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bQnjc5gm3nsXBclf9V4yhnNAGH6w7t6LSIk41tOGm_gihoZacjXgmmlhPTLP2wLDutODh9JYZ2XCp2WQH7YXOH7dsMVle-xCBuGHcY9YCP1vhuPrnq0JlNwV4iDW3ZKY_8HmP6RBuqn5_PXIuWRC0w6mTel5-UMJc88ZXZZfcjdvcz5gTy4O0CtsPeBfV90AEhoP6Y7sDvnyDcQJTHIDfWD6z_0qgp6rE5xGnbLNDTe-uycZS-mKSR233oA1_k4FML2pVjcHEimdb_C8Dosu3T1FkDvlPVVb7SdVlrdO6MYMdFgT4GH9kqN4ikcXMo90OgDyjiPcBrTC_0W3Pu9FpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌دوم‌جام‌جهانی 2026
؛ بعدِ مکزیک، آمریکا دیگر میزبان جام‌جهانی‌دومین پیروزی پیاپی اش رو بدست اورد و قاطعانه راهی مرحله حذفی شد.
😀
استرالیا
0️⃣
-
2️⃣
آمریکا
🇺🇸
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/persiana_Soccer/23865" target="_blank">📅 00:37 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23864">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P2BLh4SuoDI4aTlEvsf8NcjpQp80vEdEqlXD3UbB_r9Zwo7WQXOJyXm-UDkH70i2JOyqvgQb63AArcFppkHq1uytLmKARq0SJeRDW-TgCdh9u8RTFVQjh4ndHV32SeNaPm-77vHlANbQ7GhL49pCuSHsZVrE1bAx3pgTf75ouXUrxe467XzAQ2t7i6RIJAupIljuY6bESq25gCGKncf7Qr5FIjGpNRVmXz9ZvJB5v1gwDps0wMx-KJ508n8Ys2IhkqTEMYLAOMBnJInfb9fLDxeKNxg3c60IxLhXRXmefFCub23LoJTaTJS99Fo5jTnzUPJZtCPDCs923t6bZTzntg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#تکمیلی؛طبق‌شنیده‌های‌رسانه پرشیانا؛ مدیران باشگاه اتحادکلبا امارات اعلام کرده که اماده است که رضایت نامه محمد مهدی محبی وینگر 26 ساله خود را با دریافت 1.2 میلیون یورو صادر کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/persiana_Soccer/23864" target="_blank">📅 00:10 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23863">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OIAxhP8BujFH9722eo54i243tzhKHZuYHYEhAqsTFRdd5NOXCJ_P5EAbhA-mMV9993uBfhc-evv5BtMkxh7XQSnPBTkxAK-paDYUWCqcKkKm-Iw6wArpfX50mHgyxHc4NIqavizDXi0a8wJ7JlAI-bF3g32KmH5MSuGQyHklJNib7gI5SKlkdnQO9WFhKgptFQ3HCWr1SEkK_INMJTjYveHK78af8DN1agf6vLSrPc9PYdF10XOVm5_Ey4cXqH81xm0J9uEKLzD-lbMS9XvlBT6TrzwgPlwC6Hem2CF7eBt3YP-Yr7arbY9XRb3HB-6a_5kWkxmbsXuUjHj6sN9GSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
با اعلام رضایت پرسپولیس، چادرملو و گل‌گهر؛ برگزاری تورنمنت 3 جانبه برای سهمیه آسیایی قطعی شد! و جزییات آن از سوی فدراسیون اعلام میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/persiana_Soccer/23863" target="_blank">📅 23:27 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23862">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XpXdhFnmSp01RHhma1PVrtimyt50yTqgQPjryzkRD7-FDtCFJy-l2NeJwfoe-5m18FqP_HBbm_rqE0ojUxs4nsJM8QonOiZFXHC8xtsL1Y21hvpKhpxegKVtv1MP7JCs5PGKV-You3T8FVIVxVO8QxiS8THAdTT3G1cwWtC1NbUuARr5hoQ3H17yVs3aCiF8My4OoSqgmj7Wrs-sVvORp2a62XVc5fgW-zSJV0qVJWNWQ9yXvrk0WR-ic1ULh4jnHPHwaIH9_R2d2BG8UOL3UExQx2ISbx4PIAC9E4wHlXMhl_TBvfVs8jRuY7wFMA6MQsaEAIUZAMzbQLBs9ZugEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مدیران‌دوباشگاه‌چادرملو و گل‌گهر سیرجان امروز به فدراسیون فوتبال اعلام کرده که در هییچ تورنمنت سه گانه‌ای برای تعیین‌تیم راه یافته به سطح دوم لیگ قهرمانان آسیا شرکت نخواهیم‌کرد. مدیرعامل گل‌گهر گفته حق مسلم باشگاه ماست که راهی آسیا شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/persiana_Soccer/23862" target="_blank">📅 23:10 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23861">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YHZl5X9mJuMavliUWlDuSMQn0g9EJHfIa4Qu8lJoyRivD1Bdc_FzldEZ9IziZM1y3EfWZR6WuKbn_fun3WZI9KoNnK6IbpQ9DR36Gnxxv0sBtT99uBCgcT0tVssp-rs09lRyvx6RH0WoGLo52ds3DGEbVQq94smFvOr8-aT2r1nuzBTWrymHx1weH6z59PDPx8cOzudP-amyJWWWeW8_8p6TR7vMx7KXMk5yv6CSnvHLLL7dRlJuppDcAdrKmp9biTjcxdjZE0oFXbq3uV3hpk_JIIkncVGn81kQe3jpYlDj968iMq50K0wHce-7vikOaH-9jTUnWroEMkK65WLurw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پرونده‌نقل‌وانتقالات‌تابستانی رئال مادرید با این دوخرید بسته میشه: 220 میلیون یورو برای جذب مایکل اولیسه + 120میلیون‌یورو برای‌جذب انزو.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/persiana_Soccer/23861" target="_blank">📅 23:10 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23859">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jyxgu-zO5RF-_snbQjx0btSt7sQs-AwC6mffJe43buIsnpZmAi72YdF6SKkCuvN0QEHsO1ck_IATUp0DAo3PzhCcwWbioWNTrSPqPBMYaG0iCesg-6RGTx21S9Aqj-NcMtvZp2mo3TTvsSQhj0pT3A_G3GTSsMpGU-tMUh8Hok_zx_XAjWOcXtBLsAYEtESJIm5wn40hVcm3cgkjXkKtwFsC4xybpSxkZfam8eB72g3_LJOKOWGf1sX9vz5x1LsvXizWaM_8oXjH8CQkAxM5y92HWf7qAJJSaYtTyKW5__njN1JBDeoclIIaQoitvFzLzIfDGQzFIr70xDR8122afg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#تکمیلی؛ طبق اخبار دریافتی پرشیانا؛ مدیریت‌باشگاه استقلال از علیرضا کوشکی وینگر 26 ساله آبی‌هاخواسته‌که هفته‌آتی به همراه محمدحسین اسلامی برای تمدیدقراردادش‌به‌ساختمان‌باشگاه برود. همانطور هم که در روزهای اخیر گفتیم تموم توافقات لازم با مدیر برنامه این…</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/persiana_Soccer/23859" target="_blank">📅 22:42 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23858">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AODnqGeWR-ROs-1XIh16sEPU3QKzqoL4ZIq9W_9zAH3mRBaeDf3mlgXBdqjmmajbCKHh5T2mQpbmjibhfvzMk40joFplBNUDbGPpIRaRG9xaGdn73aG-ZK3Wl5xf69wwFBu0Mw54dQbCXddTcjrchHlzon1pq82H53Gbqt7z44VwPVFoP3of1327y-gAC8vQ1gsaFnusmuB65MWUPNyFVlgmMbAw91Hjd-2UHfGiRq0TsOOmMGLvcz6wigJtqe38ab2Qk32a5lNYns2dhiIsctDXbpmX3Q2VB8_VBH5f4Sour-g5ohqB7V1huqyAPEXqpdj36L9m8LytxHju6TV_Gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
💣
🔴
#اختصاصی_پرشیانا #فوری؛ رونمایی رسمی از لیست بازیکنان مدنظر اوسمار ویرا برای فصل‌آینده‌پرسپولیس؛ لازم به گفتن است برای هر پست نام دو بازیکن رو به مدیریت باشگاه داده تا اقدام لازگ برای جذب یکیشون انجام شود.
🔴
محمد امین حزباوی و دانیال ایری؛ دفاع وسط.
🔴
آریایوسفی…</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/persiana_Soccer/23858" target="_blank">📅 22:10 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23857">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jz58XkoFiHilqcfw_Nttn6YrMMiToiEPiSrYJKz_jrO7eTHLHtv0tSxwob6JpFIb21RVCxTTRUsPBjQsG8C2xb0gdERQManxuO9J3f0Q8iHN8s3cdUsuj5ddltqaW6h8s5XIkeAkOFki8gvStrqDJK3nAB7kPAg7Voj--9uMRzHzoCVMmcjsn5R3GcYn0hTTaJXEZ9zeq8ZPDk_9FSPNggt9Fvqtf2mjxkbFBaO5BVYgdeB_P5MrZOp_83pxjk_axPk1zukisIu4zB2lnhV3q4e3kxjJY3ddBMB721JGCyDTYiTR54d-9ohptVwmrt-HQAt2K-dotRMR1SoB8UkqOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مدیران بانک‌شهر معتقدن که پرسپولیس در فصل جدید باتاکتیک‌های‌اوسمار ویرا بجایی نمیرسه و قصد داره توافقی باویرا فسخ‌کنن و سرمربی سابق تراکتور رو به جمع سرخپوشان پایتخت بیاورند. باشگاه بخواد قرارداد اوسمار رو یک‌طرفه‌فسخ‌کنه باید 1.5 میلیون دلار به او پرداخت…</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/persiana_Soccer/23857" target="_blank">📅 22:03 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23856">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bGRRUBMSQABTJvtHzM1eU1I3crFQXHhqLEq0kQAHZMEUPjxMNrV0uSGg7BhFZsG2bLRQD2oPEoXArODM-kePgHi11xKztldBYJjr_iAwp5mCu2TqwfFED7Y5B15wESOezax6axCYKAOjuhGa4p7xiN86U_0jS5-_GUd360NIml6s9Ph0QWkL79XsB6tdyrnO3QGb62aHtC3qVzJWmuEEe19WdARK1Lt8G7rq_wqz56_7O47RCqF_X00xCtwlfUXPSOIaUKyZN61jGTC-RvljuMvaENN0UF0Elt1RzvhRzIw3_p3Soy2iLTzMhEH27gWEA26qrpdJBXB6IPayni2ZOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#فوری؛ نماینده اوسمارویرا در گفتگویی کوتاه با رسانه پرشیانا اعلام‌کردکه اوسمار علاقمند به ادامه‌حضور درباشگاه پرسپولیس است و حتی لیست بازیکنان مدنظر خود رانیز به‌مدیریت داده و اگر اتفاق خاصی از طرف‌مالکان باشگاه رخ ندهد او فصل اینده روی نیمکت سرخپوشان پایتخت…</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/persiana_Soccer/23856" target="_blank">📅 21:56 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23854">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/J9mA6Wdq6c2g-GNa4ru5D0rJPTKUJjp8HXAroyKmmfdyQaQASoRdI7FUV25QnYaK0LO6d425pEW8rvwZajw0kYxYmNwznVxuEBk1Fk2L_-kLJgLaNsMwMozwKhMg9F9R8i4e3SB954bUi7YLpf9GzPrqZskJSL96JoZ-NkNK23fZEGRJJh0DMp-J--byZIbdirzkG-MyEZjU6eG2eeHbPSyq4ZYO1KXM-Xc8a-JrEmiD1PsYN-YWMMp8juEDmOMEmkwx6Bgs2n6J4FBRd0OSfsE16gSByFpCWZYaNQy7VLQEnf2rDVeePl_aUwmTV-gZK9Xyxo7Ek8zXKx5FfoX0yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p_0cXtPJOtgkXsBcgEQvwms9oZy6uLJgx2Vmf4TCObI94gzRYIK3WrGpKOIgkWDLpvh0obVdgPvD-9AXnkxo8mT9V-O0DECPIbp3Q-kqSlbocI3Re4rFV3TYHDmmR5bjEdpy_S6V_1izEVgqmKPqonyqxFduC1mlR1loI5thEG807Y7M8slkEkY8n5MuY4YLFHs5qbaIL0upp_OV6OLWePeGChIswEgXavOQm8yZhb_CO307LMaRlFHyW4O7h3uQhBcfw8xjilG89T5dtU13ZOL7_6HWN5aD7EI15Z-2FHER0PL6ggF6Tc_8XLGZq4Ewl4QG4S4DFVIXEReGNCpYPw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚽️
هفته‌دوم‌جام‌جهانی2026
؛ شماتیک ترکیب دو تیم آمریکا استرالیا؛ ساعت 22:30 از پرشیانا اسپورت؛ هردوتیم‌بازی اولشون رو قاطعانه بردن این مسابقه امشب دیدن داره از دست ندید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/persiana_Soccer/23854" target="_blank">📅 21:21 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23853">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QoQ-UrgJw-ASuH3naokvPoZMHnf9O3TOARReqTv1JsK_ZhinFCgl7wd3SN48WY6gTwp2Kh21i7mweFtrfNHxayDj8JnOOX2YnI9xJ9rN31QMuieAQAs2uR5lbD-y8aqs5kt_f8aerM-BSwEW41nF5QC6UdDV-CnN0rV519q_m2pIqe_fptbL3ZcMe5eBuHS-Knm_C0BWL2CwtPfsaqNGWiMpfWp4rw5r2XMlyhcgoAY2Jqu547S3YiYrJTspCbw4QxL2wd5IPCrTBfWwPtpwFWCCbYA-BVbLumZ6oacJQVM55gUrUlEKmdsb9ypOGDFukS9ZqbaRuWz4yl_30wp4aQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇦🇷
مارسلو ستاره‌برزیلی‌سابق تیم رئال مادرید: برای هواداران لیونل مسی احترام زیادی قائل هستم اماهرجور حساب میکنم این صحنه واقعا کارت قرمز داشت ولی چون لئو مسی بود چشم پوشی کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/persiana_Soccer/23853" target="_blank">📅 21:12 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23852">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s9O_hgEBKorkwpeySHmvtAkH98aaOgeZudVBDQGwioVb0_KxYNwtB9UCy6fmBY1JwMcx4G6Ju-tlPhDFQ9ThU6aVamuvudYVBtfRLLYzY1JGZyuF_8jMv85JwaU3hPNd61kNmEX_RG65b309S7kPy6OJdUsptViy9X-DKyRdrWnooe_xfORbBjqQAcgMHU-PeI4yj7L6pm-nigenmya0HtcPEN7-YKseHx1fT4IYoLZhC2f4_g3zbGNj5Nru94Sy8HT4JLKm6h0nbYDWtXzAge17Yb3UURy33LVqWKKHX0Kb98g8RPwZoIO88E0cFdRf2e7bI6HCVCeHq-98nrEKxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سعیدعزت‌اللهی‌بازیکن‌ایران‌باثبت‌حداکثر سرعت ۲۶.۴، پنجمین بازیکن کند هفته اول جام جهانی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/persiana_Soccer/23852" target="_blank">📅 20:57 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23851">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7648c46620.mp4?token=k7srjlQppiSoiHNPvPDab3rYoHJp2MGSzOfQywQ1Dt6wHQCkD0bJEbINsHCLNDW1Jv8zPtCQcMbXzQIy-8QvdVIRQN6FATQgeg42AWMosYaPkQpLQO9t8CR6Wm4PIGUhiJwPQjlwTNFt1bhU7JCQY3zAUc_Jp8OmBm0z5X0C8Ab2Rjb_ErH6UkZ6spRay9RagXpcCKRNMY19wM-XVnWgASQa8EPrI7kgnluVsqfOsuH7457kofRVl7d_uNfEmYrDmGq5jCCvKWTYNBYfaEV9XH9lveJeoC_bP6Ne3NxDUaCfZ47JUrYskEvrioF9NlTaYUnrOANV-_ACQhqOKbCPOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7648c46620.mp4?token=k7srjlQppiSoiHNPvPDab3rYoHJp2MGSzOfQywQ1Dt6wHQCkD0bJEbINsHCLNDW1Jv8zPtCQcMbXzQIy-8QvdVIRQN6FATQgeg42AWMosYaPkQpLQO9t8CR6Wm4PIGUhiJwPQjlwTNFt1bhU7JCQY3zAUc_Jp8OmBm0z5X0C8Ab2Rjb_ErH6UkZ6spRay9RagXpcCKRNMY19wM-XVnWgASQa8EPrI7kgnluVsqfOsuH7457kofRVl7d_uNfEmYrDmGq5jCCvKWTYNBYfaEV9XH9lveJeoC_bP6Ne3NxDUaCfZ47JUrYskEvrioF9NlTaYUnrOANV-_ACQhqOKbCPOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
خبر مذاکرات‌ نهایی‌ باشگاه‌استقلال و توافق با محمدجواد حسین نژاد که امروز اکثر رسانه‌ها اون رو کار میکنند. 10 روز پیش اعلام کردیم که باشگاه استقلال اوکی قطعی‌رو از حسین نژاد گرفته و فقط بازشدن‌پنجره و پرداخت‌رضایت‌نامه او باقی مونده.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/persiana_Soccer/23851" target="_blank">📅 20:28 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23850">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nh1E23WAueme7KR6LA8VoyCjdfAunS7yWxHUl9f3T-DN-XViPFNSti7VpNZmGeJCMCcqclb0l0BEkv3o_CA2ZsCoEDbtDFPS2hDrwVD7JNYxZJu_QHUaT5OqE8Ip6b9Sy1u6rpxSeE8jNSxgQE97f3xc8BvuuM_mC11hZpqSm4KT8BPXmWHiW3NRTE-b7sc3Re-ue32WDLb4OfJhExKC2Y9brGpKlP-0-v2vhSw7BFgJdFaXm0Q7L4Q5A4tN_fZTwsuTfrSRzLVSbLw-ZQbFjrKJZxj-kOYTulwNURJj4T3EA38grfbg5A57KuG5wuQK7dtMkIf__wTJtTnH59YVEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇫🇷
🇫🇷
خوزه فلیکس دیاز: بعداز توافق شخصی فلورنتینو پرز با انزو فرناندز؛ کاماوینگا و شوامنی دو گزینه پرز برای جدایی‌از رئال مادریده. شانس جدایی کاماوینگا بیشتراز شوامنی است. درباره فده والورده پرز گفته او فروشی نیس بهش هم فکر کنید.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/persiana_Soccer/23850" target="_blank">📅 19:54 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23849">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dQN7YZYcT2z7mKWjhc5dUnM16MWg0051jPs2arTj57P1YYuffWdpNLEj4_Xepa4fS_3ruCh0YA6bF8thbmcL2ADGibOYCfju5T2g99XrQYakF6hT2LCkAHJKn8Tya8ks-fVX_CTQYYgGr-C0E3kULiN39kOgggt4I6Nq9E4qn9bH3WGqeXPy9Cvpe3zWyffwg0eg7icY2ADM8AHEZQ6Ks_4xKGfJeHfqud5vpw0hjdj30YPxc2M6i6gEOFEFbunjxcgniPdIeUXW6QBDAHSlb_E561a0w4cvJW6T1E4K4ZhHBv4eFN7Z7UI9YL7HcsQEtzs-fogRIEdNN4nz51JsuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
محمد محبی ستاره فوتبال ایران در واکنش به حواشی اخیر: من هیچوقت همچین کاری نکردم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/persiana_Soccer/23849" target="_blank">📅 19:35 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23848">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R2uYPPfeYAtdNP1qzuXIn_xFXgkcOWv0Jkiwfd08T8HtKmyMC5VTJNLc3Ft5Gg23RTekUN4uO0g4pVmZX2EmWKbFXTAiLdXfv5ljVwSSb7SV0DTFku7m9GI3RnkYHQ7QSXK82RKd4lhCbFoLHx9DMqekuopIu2zsdo-xtRVdhkyPzomBqVFEanXS7aVWj9PMvii2fGwq-m2CfeClkYePECMq7Katric5eb2Zb7dNwDlzvkC5az4l6ImIqcgueKz0jHbZVj4laQK2D1976uUkkJmZjnHHQAW2-u5xcwpty35aPwVlIDIlJ-LFC6K-UNhxKHVBMJqLdHQvQ4XeI1Ltlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇪🇸
نشریه مارکا: ژابی الونسو با آلوارو کارراس تماس گرفته و از او خواسته به چلسی بیاد. کارراس هم گفته با رئالی‌ها توافق کنید من آبی پوش میشم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/persiana_Soccer/23848" target="_blank">📅 19:13 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23847">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jFEaVOMKVlx1yuLIa07elSYbO0Bz7wc-NKtfnis0l77OlLZmxYkfXodEll3z9OP_mH20X1jcu4IhHkuQE_B5Ul8wqvR_VNOpwwZ2hmqv6OnquNkhS6cmccV0dT7tEdRMBjJVlTsm7VOcAKHF2d53X48fd0M6hlcKTBf5YfoCLIXh6rXLtXKjeWkl3cKVLKTsYcuxTamgW1otf_aemFctiBxZ8tgtq6eVatAaL-k9CTLVMy6zBjGuEArFnVlAUXHJNm4lN1yCloRxuQmdM8yUdaciQXrD1XsmC21n32CGM3hy97NHyd9JO3JQAq7TSOqrfDO7g_JPY6hL3abOPPaYAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
پدر رامین رضاییان: خیلی‌ها بخاطر طرز تمرین کردن رامین او رو مورد تمسخر قرار میدادند و حتی ویدیوهاش رو برای من میفرستادند اما او برای جام جهانی برنامه در سر داشت و مزدش رو هم گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/persiana_Soccer/23847" target="_blank">📅 19:05 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23845">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pfauBoCdITozTTTy-ANXz7E_PiXKJUQmf5J7d2659C-4O5nBiA0ia7838Ve2Da43PU7Fu2fgWGUrzsA1M7IYbG7gbDtpWSzRbaC1B1cQcgJnm8M2V6lTxefrFIErZGFEQfHrN-bS4jPJVBCiitZX75rEgmKRWpYBUe2ykkF8f_sczzeS7D5YPxYffzjAbBxwVQNh6WrMGEhUsFryuKIAzrVT7TrtKn5eUnzy65_tEEgeLeAv4m0Z_0MFkm-ybal49SAiScngb00Qjs0EEW8A-kxiLUyvEHLj8IYmROut10YwkXhQLYbVHwJ7z8tLrc3B1XVS5hyHnwesyfo3JA51eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔵
طبق شنیده‌های پرشیانا؛ علی تاجرنیا رئیس هیات مدیره باشگاه استقلال شب گذشته با مدیریت گل گهر سیرجان برای جذب پوریا شهر آبادی مهاجم بلند قامت و 20 ساله این باشگاه تماس تلفنی داشته و احتمال عقد قرارداد 4 ساله با بازیکن وجود دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/persiana_Soccer/23845" target="_blank">📅 18:49 · 29 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
