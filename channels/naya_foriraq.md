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
<img src="https://cdn4.telesco.pe/file/Bu8TCg5N4JLZtvs1DFSQgFafAVXA2EyAsJWQLgoqXV30jtMyIBvOZnMMPDVefshRI5Io63CXWD1sBKVNSRV8Qsddz1VbIAKQmW438tFHb6XbH39jBoQA5Qhycc-2hG-tg8IaRZgglGzTx-UPVmMcf8PU6TjL1BiugbDZp4poLyf-L__vowO9JBV3CahEUagX5ceRf3HjNnsUaNoFhiY_C9eLfyib5_mKad3RQmbDxe_PWgzsX3PLLrPuSofi9OJtoJdjhqMDcGxxPNVefjKLN2Wo2t8M9G_qo3MWKKnJ3YJfitQ6Xv3vnCMF_gEhOSgN4RJWNnkyAGizgBL8pIuhRg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 255K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-23 17:39:47</div>
<hr>

<div class="tg-post" id="msg-75300">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ab19cc8eb.mp4?token=Ok2Ejg_rqkWYqcAwXTkOGS8rg1R0tg0Y2bCQ_s6drvQlgyq-UOsdLH0lhG74dINsAFxTtm2YiJbjUCk22_fNtQ7pARDPsXq1XZpiA5kA4ksQJHlN6stsElsyWutsdKxl2dq9yagYsDGe_NzUes8xaQ2ixoTa_E_GVpqbQMq5J1fPYcsVdW3ujrRHpmF7KL53kem97lcvw0lUnuTaM-QhNz7FM_SwrHuZMKWrm-Ep7xquQmaIMhiWY4s3UAV9ZQUptn_CQqrCkoWbTZZNT7bDuC_rrJpmwc3xNY7r-C52j46LEtUELZIxuE2jRDQywvO0QWtDx92dmHHd6ruhPAjr3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ab19cc8eb.mp4?token=Ok2Ejg_rqkWYqcAwXTkOGS8rg1R0tg0Y2bCQ_s6drvQlgyq-UOsdLH0lhG74dINsAFxTtm2YiJbjUCk22_fNtQ7pARDPsXq1XZpiA5kA4ksQJHlN6stsElsyWutsdKxl2dq9yagYsDGe_NzUes8xaQ2ixoTa_E_GVpqbQMq5J1fPYcsVdW3ujrRHpmF7KL53kem97lcvw0lUnuTaM-QhNz7FM_SwrHuZMKWrm-Ep7xquQmaIMhiWY4s3UAV9ZQUptn_CQqrCkoWbTZZNT7bDuC_rrJpmwc3xNY7r-C52j46LEtUELZIxuE2jRDQywvO0QWtDx92dmHHd6ruhPAjr3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭐️
إستهداف مواقع المعارضة الكردية الإيرانية في مدينة حلبجة شمالي العراق.</div>
<div class="tg-footer">👁️ 1.16K · <a href="https://t.me/naya_foriraq/75300" target="_blank">📅 17:34 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75299">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f60e50230.mp4?token=Zf2GHZlAdawQ2Tu0XGCIbWUzKhj7Z1iz-fcwQF1SxBBtoNuQXkCC5FmEbP40KFSpUofMRvpGEhFdI7qdgGhQalJIUQ_2ck2I8W6g2jq_WIF5qkx9Wzr_e8nU4xCo0qk-rPUGlcXZzbTX3VnxrHs81LuYcRylwbXsoGrP1I1NlMRLk2Z032Kcmoc4SDYONSf_DKTyD4wFS6A8PgZr3I-ygHPZNKbi1HW4cWo5-ZAkVYEfVUZeV2LHeI234ooDwTFjBLMlwKg5yu3J6fzhweEnQjAp3sBBMzkjRqh6XZD02w5U5nnLU0p0xVw54gBL-VgnHwKah-Snjvy2EQfqcSlNyDEUJri3RHQCOSeqbpMZFEuCdZuow-E3mCbgnkrAZ7bz5jd1zR09hp9n4avO6fEGn0-P5kcAtUCwrfKsE5tbpfynts9OCookIT4A1ZaZ_rEQmizj3vmaAWGokwjADEc196lAOHtHPL5Qi6kV06nrkq6BZOPbfkoAT__016KPsJ-XbBS3wtQoMvAEZrueuB2JI-L9-HFYBbn5XASXo1HhzTa0sS7szjrjJ-fu8Lj2lF9vQvK9j4SAd--087YISxgGmFG_303YYCTAGFPlkyc262V3gtuypsTTqXT5H68PFHMhWcAf76TnXv0tRItqDxklxQ-Miy1hmQEqCZ2Y8nNsqxk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f60e50230.mp4?token=Zf2GHZlAdawQ2Tu0XGCIbWUzKhj7Z1iz-fcwQF1SxBBtoNuQXkCC5FmEbP40KFSpUofMRvpGEhFdI7qdgGhQalJIUQ_2ck2I8W6g2jq_WIF5qkx9Wzr_e8nU4xCo0qk-rPUGlcXZzbTX3VnxrHs81LuYcRylwbXsoGrP1I1NlMRLk2Z032Kcmoc4SDYONSf_DKTyD4wFS6A8PgZr3I-ygHPZNKbi1HW4cWo5-ZAkVYEfVUZeV2LHeI234ooDwTFjBLMlwKg5yu3J6fzhweEnQjAp3sBBMzkjRqh6XZD02w5U5nnLU0p0xVw54gBL-VgnHwKah-Snjvy2EQfqcSlNyDEUJri3RHQCOSeqbpMZFEuCdZuow-E3mCbgnkrAZ7bz5jd1zR09hp9n4avO6fEGn0-P5kcAtUCwrfKsE5tbpfynts9OCookIT4A1ZaZ_rEQmizj3vmaAWGokwjADEc196lAOHtHPL5Qi6kV06nrkq6BZOPbfkoAT__016KPsJ-XbBS3wtQoMvAEZrueuB2JI-L9-HFYBbn5XASXo1HhzTa0sS7szjrjJ-fu8Lj2lF9vQvK9j4SAd--087YISxgGmFG_303YYCTAGFPlkyc262V3gtuypsTTqXT5H68PFHMhWcAf76TnXv0tRItqDxklxQ-Miy1hmQEqCZ2Y8nNsqxk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
🏴‍☠️
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ
12-05-2026
جندي من جيش العدو الإسرائيلي في محيط موقع خربة المنارة على الحدود الجنوبية اللبنانية بمحلّقة انقضاضيّة.</div>
<div class="tg-footer">👁️ 1.29K · <a href="https://t.me/naya_foriraq/75299" target="_blank">📅 17:33 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75298">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">⭐️
إستهداف مواقع المعارضة الكردية الإيرانية في مدينة حلبجة شمالي العراق.</div>
<div class="tg-footer">👁️ 1.13K · <a href="https://t.me/naya_foriraq/75298" target="_blank">📅 17:33 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75297">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">سوالف الگهوة / نايا
ابرز الحصص الكردية في حكومة الزيدي
- فارس عيسى نائب رئيس وزراء
- عادل شواني العدل
- نوزاد الإسكان
- فؤاد حسين الخارجية
- سروة البيئة
- اما كتلة الموقف النيابية ظلت بلا موقف حكومي ..</div>
<div class="tg-footer">👁️ 5.93K · <a href="https://t.me/naya_foriraq/75297" target="_blank">📅 16:22 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75296">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mq9E1GRNH3ZVYF2SEWgo3qJUHM5F4y8UMBMNVffJb9A19Vl8T1Ecvi2mToY7KJqfzpcRbzCVI1yZJqRUWfo6I83Tv9mNLp3xaPhxn7Acf6pUhw-i1kS597n4yCMFqjBcjyY3Snvjd-wF52cD5Kp5LGXBH0vu_GrqY8gcHMn9jSiervPklCp1mEUKfJk-8BND_lluvgeiq9Y0sWyq8D0QlPDko0HpusOp3iyVJHCZQH3oNrmzLuE66FvrKR3fQM2fXj1IRrUuUI90ELw91gOxNyD2YSRqCqLO70LC7aJgcZ0SommS6rQ1YR9c-rED76LT4Nmpuz6oV1846M924yNM0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭐️
دوي إنفجارات عنيفة بريف محافظة القنيطرة السورية والجولان المحتل وتصاعد أعمدة الدخان.</div>
<div class="tg-footer">👁️ 6.94K · <a href="https://t.me/naya_foriraq/75296" target="_blank">📅 16:07 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75295">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🌟
🏴‍☠️
دبابة ميركافا تابعة لجيش الإحتلال الصهيوني يتم دكها واعطابها من قبل أبناء نصرالله في بلدة عيناتا بجنوب لبنان.</div>
<div class="tg-footer">👁️ 8.37K · <a href="https://t.me/naya_foriraq/75295" target="_blank">📅 15:30 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75294">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9dc6ea4372.mp4?token=hgMmRoB2Yr7GbmtGvdJTdagbQ8nKAOfmnwz3uTE85EuoTWTt5zzu2zmQE3Jev6J_lY2WclNKqYKG-xHSOcBSF1ZpWUNK1NOLZM0FnKk_v0roLS86BkTVwe4Xoj9kYhxi-Wd8Kz9AQrROrIIQQxHc7S1KBqT2oK1RWYdfyUpT058F05QKoquqbYwYKBfQobaiUMsWXwhnjSL3a_31Fys6YXkzovdTltq5zYUVOYEAMapM5JQGZh_iTkOVfQExBDdlQ17K39B1Gkvw2XkNWlLOWzgzUxhSRujcso7OshcQiJxiKD8dQEh4McZY-J4z1VQMSQou78yeJRGihgBOeB1_Xw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9dc6ea4372.mp4?token=hgMmRoB2Yr7GbmtGvdJTdagbQ8nKAOfmnwz3uTE85EuoTWTt5zzu2zmQE3Jev6J_lY2WclNKqYKG-xHSOcBSF1ZpWUNK1NOLZM0FnKk_v0roLS86BkTVwe4Xoj9kYhxi-Wd8Kz9AQrROrIIQQxHc7S1KBqT2oK1RWYdfyUpT058F05QKoquqbYwYKBfQobaiUMsWXwhnjSL3a_31Fys6YXkzovdTltq5zYUVOYEAMapM5JQGZh_iTkOVfQExBDdlQ17K39B1Gkvw2XkNWlLOWzgzUxhSRujcso7OshcQiJxiKD8dQEh4McZY-J4z1VQMSQou78yeJRGihgBOeB1_Xw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭐️
أسعار النفط العالمي تتجاوز 108 دولار للبرميل الواحد.</div>
<div class="tg-footer">👁️ 8.41K · <a href="https://t.me/naya_foriraq/75294" target="_blank">📅 15:27 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75293">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27da7c312c.mp4?token=sbRMtzpYsAjr3qeaVNssA0Lx7EHRG44VRUMoTeBX7elV291gGJ14ilGunNV0cquNqqRJ9OqoEYDq2DIplYgH4daXemhmkAoziU_qPISL-XqYnm-4wiwFa7ETjPHsJYJIcaXtGDk-iTWZzhy-K06cVUtfnE-3qCsavpBcL0iKPOOowqLR6hgV9qeoeOuY0IKAWAipw-hTebCCXUcagoBc455ROXJx19WtVXDAebw-o8ars-kYjRPDRabn20K8YmbDVR7kUfgfgmB20WgQVk0cVp5yplQQP4WsGXoLPjSngXuhnNLWkpBEz95ea7GTCkYNNVssdqbC835G2MShgmLSVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27da7c312c.mp4?token=sbRMtzpYsAjr3qeaVNssA0Lx7EHRG44VRUMoTeBX7elV291gGJ14ilGunNV0cquNqqRJ9OqoEYDq2DIplYgH4daXemhmkAoziU_qPISL-XqYnm-4wiwFa7ETjPHsJYJIcaXtGDk-iTWZzhy-K06cVUtfnE-3qCsavpBcL0iKPOOowqLR6hgV9qeoeOuY0IKAWAipw-hTebCCXUcagoBc455ROXJx19WtVXDAebw-o8ars-kYjRPDRabn20K8YmbDVR7kUfgfgmB20WgQVk0cVp5yplQQP4WsGXoLPjSngXuhnNLWkpBEz95ea7GTCkYNNVssdqbC835G2MShgmLSVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامب يغادر واشنطن متوجهًا إلى بكين في الصين.</div>
<div class="tg-footer">👁️ 7.62K · <a href="https://t.me/naya_foriraq/75293" target="_blank">📅 15:25 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75292">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tT3D4JiIOKFkbqjjCBs9MnZ57kCbKlefCxBFgt-iajcw1x24cvZq-wI8L2sKoGd6JorxsYa5Xyk47M8uVqZDMBRJOmN4nP0z8Yn1rKGnjiYq_SJwwydo75Hf4urvKG-aVZLeypakPXhEkrjU4BjuObZvR58ww-urrgI_FA0l4BUEhOBTsUXXguAqe5q2OAKyJrNE2flVJjrEgcn72cj1aQHXvc-sagcz0bkyQCJ5xEIG-pSDgx5otERY9fozqMqm5fsMqfr9N817iVJrBtuIfQD-dKjV9GfCaNp0AI0tbAnc9eGbjJn72ov_l5lIt5PtJSzMZCs4smW9o068JVl1JQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭐️
الإمارات تبدأ بتركيب حواجز مضادة للطائرات المسيّرة حول مستودعات النفط القريبة من مطار دبي الدولي من خلال هياكل وشبكات معدنية.</div>
<div class="tg-footer">👁️ 9.08K · <a href="https://t.me/naya_foriraq/75292" target="_blank">📅 15:04 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75291">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">▫️
🔵
بولندا: دفعنا بمقاتلاتنا الجوية بسبب الضربات الروسية على أوكرانيا</div>
<div class="tg-footer">👁️ 9.14K · <a href="https://t.me/naya_foriraq/75291" target="_blank">📅 14:58 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75290">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LOxYRx6Vu82JzEtwQan0md1yXPpJ3e0AsaK5TpEAcBsQHAQ2I7OO0xs2bi8sEPcdECoHJEe7AYQKrccKw5pe_7Ym385RTrepQffzjQdNP_GoQUdCNOep0X5_Nm12spLnBy4-9yjFDnDpRav1o-G8pVCgs-6UeB2a41FacJ_l5t6hzhElaaFht0FuEhAFrVDv88ADAoaSS_VgdDTOJztqu2esyqhXwsqgsigqUePtq1MXQpIY5Yr_8qyVnbrAKdn6HhIC-MdC145OUkIFI6lkdnfqb6-bvpM1SNjO2fPr0spTvoNfnDEbPhJdxpNMbBQgi5H1UJZwG44vqK3HUMSzWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭐️
أسعار النفط العالمي تتجاوز 108 دولار للبرميل الواحد.</div>
<div class="tg-footer">👁️ 9.59K · <a href="https://t.me/naya_foriraq/75290" target="_blank">📅 14:42 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75289">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a14692654c.mp4?token=aoDMduTzrd2JX2L3gUH0rO2scE6XnSzJvK_gFhuyBeMzH6mBtQAaQWWgHOSXboAA8cJ72D-ugo-LXyGDy0UQmV8ZJlB2nXjVLo-2CDigkXVp35YcdG7CWRRHWN09PDn9_EfwAUICQntSsFgAVTvXnct3wwhBIywOETcArTUo6Pj1xnIb6vFb6YXeGrI_kzCxt4nOrjphCyKyiPpRuwCxXc6hghMjtnmG5r-zFPvZ8z3sHWoZFCsJG1vHs6SvBbfDSv06Khg39mJNA4_DqwZngKjbg25QkqJocKaB7A7KywAVSzsSNpjcwLzZXtSOochoq1nh7pb-VTYrmxd13KnU57gI52ioa_unxC_SeJg6m2_nsAx2KtaSIbTQdNUgSimPHI3vxyaUk4ev0B-dbqo2Y2x52khN4LPY7xe96ZoF8Z756O9As3CrMZ4cN86IeV1MOXn_7UHENc6utkTm7fIuW50TT0USBUOD4ykzJ7Wyx4EwZfnlLNazX6Zb9oeV51HAQhj4vFaQBzp7mH58pOZOTk_U9zZYm8qS5XfvzSxRnd7nIE3GCkYKHlI2xLp6ZUq9NxSiGLrUtZlEj7qFaQTYvpTuGx4p1iG0PAKKHrWsxfwmWJm5YgYj_RSrBpLyTbOB8tygKC-xhTpDPaPe0XEla_h4tDZEYS-SmqCEEmDJdIk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a14692654c.mp4?token=aoDMduTzrd2JX2L3gUH0rO2scE6XnSzJvK_gFhuyBeMzH6mBtQAaQWWgHOSXboAA8cJ72D-ugo-LXyGDy0UQmV8ZJlB2nXjVLo-2CDigkXVp35YcdG7CWRRHWN09PDn9_EfwAUICQntSsFgAVTvXnct3wwhBIywOETcArTUo6Pj1xnIb6vFb6YXeGrI_kzCxt4nOrjphCyKyiPpRuwCxXc6hghMjtnmG5r-zFPvZ8z3sHWoZFCsJG1vHs6SvBbfDSv06Khg39mJNA4_DqwZngKjbg25QkqJocKaB7A7KywAVSzsSNpjcwLzZXtSOochoq1nh7pb-VTYrmxd13KnU57gI52ioa_unxC_SeJg6m2_nsAx2KtaSIbTQdNUgSimPHI3vxyaUk4ev0B-dbqo2Y2x52khN4LPY7xe96ZoF8Z756O9As3CrMZ4cN86IeV1MOXn_7UHENc6utkTm7fIuW50TT0USBUOD4ykzJ7Wyx4EwZfnlLNazX6Zb9oeV51HAQhj4vFaQBzp7mH58pOZOTk_U9zZYm8qS5XfvzSxRnd7nIE3GCkYKHlI2xLp6ZUq9NxSiGLrUtZlEj7qFaQTYvpTuGx4p1iG0PAKKHrWsxfwmWJm5YgYj_RSrBpLyTbOB8tygKC-xhTpDPaPe0XEla_h4tDZEYS-SmqCEEmDJdIk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
🏴‍☠️
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ 11-05-2026 آلية هندسية (D9) تابعة لجيش العدو الإسرائيلي على طريق الناقورة جنوبيّ لبنان بمحلّقة انقضاضيّة.</div>
<div class="tg-footer">👁️ 9.85K · <a href="https://t.me/naya_foriraq/75289" target="_blank">📅 14:30 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75288">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/874e2b8aab.mp4?token=lR6leEw5dLC2VObsPJ8mp8y1e01tmBA-E6s9wUr2KGh0hVg8LIfYgpTPf5QAtHKtAKDr_ME8B_9XdCEGqBVDldBEKLGsK8J7lVqgH3pVvNPp2c39GWd4ZtiPRfx3fdBSJGCS6tpi7mDtwMgjtNav-qfDNpAL4DDnCV1RtnxUWzQxgUT8jrUOV_laXJRYrN6u4zBkFTttIG8Hk2_W-efoVO1jXuecrlYk9WF8sQq-Z-W9NfhvLw01YMhbB-X2UazgDPBO46Cy96tVO70Jshj_TttmJ6_mH36J3Cmb50pGY2LCdZ0TgwvPdyuG752pZz-JId6M6DN5qJGDqOI3lfMgLododM1oL3VbEup6XQu2Vud_DlZPuZW7VX6QVSOmsOwaKW0MTdTR_FsPT-_GrZl6pJoG8zHr-V8NUG9AdeHQ1jTKkw4K34t7RXH3poUubs0p_HHp1MAlW521RgZFW5X_IPGY2dpncOwqxycH6EYchclEioa82q70Y3Yg5Gzrwd-UcIw1CQLhQhYA90YDa65zQFqs6P96ngj9RLoGnlJxX19XspNJQZfi3ZjpplJxgKRPY5b18IKhK6kRLN9sX2JVCwciEHuD-WFqxPmZTwXkV-CaE7kQSTjb-QmE6PWDUAsCjUtErV2Uko9EPGlJnTqGCcCp02ceteIRI7ZGzXX6fAs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/874e2b8aab.mp4?token=lR6leEw5dLC2VObsPJ8mp8y1e01tmBA-E6s9wUr2KGh0hVg8LIfYgpTPf5QAtHKtAKDr_ME8B_9XdCEGqBVDldBEKLGsK8J7lVqgH3pVvNPp2c39GWd4ZtiPRfx3fdBSJGCS6tpi7mDtwMgjtNav-qfDNpAL4DDnCV1RtnxUWzQxgUT8jrUOV_laXJRYrN6u4zBkFTttIG8Hk2_W-efoVO1jXuecrlYk9WF8sQq-Z-W9NfhvLw01YMhbB-X2UazgDPBO46Cy96tVO70Jshj_TttmJ6_mH36J3Cmb50pGY2LCdZ0TgwvPdyuG752pZz-JId6M6DN5qJGDqOI3lfMgLododM1oL3VbEup6XQu2Vud_DlZPuZW7VX6QVSOmsOwaKW0MTdTR_FsPT-_GrZl6pJoG8zHr-V8NUG9AdeHQ1jTKkw4K34t7RXH3poUubs0p_HHp1MAlW521RgZFW5X_IPGY2dpncOwqxycH6EYchclEioa82q70Y3Yg5Gzrwd-UcIw1CQLhQhYA90YDa65zQFqs6P96ngj9RLoGnlJxX19XspNJQZfi3ZjpplJxgKRPY5b18IKhK6kRLN9sX2JVCwciEHuD-WFqxPmZTwXkV-CaE7kQSTjb-QmE6PWDUAsCjUtErV2Uko9EPGlJnTqGCcCp02ceteIRI7ZGzXX6fAs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
حزب الله: مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ 12-05-2026 دبّابة ميركافا تابعة لجيش العدو الإسرائيلي في محيط موقع خربة المنارة على الحدود الجنوبيّة اللبنانيّة بمحلّقة انقضاضيّة.</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/naya_foriraq/75288" target="_blank">📅 12:31 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75287">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9495fe1b87.mp4?token=djP7f7a_1n2UZXsxK_Ww4EfqvWnD7UwNktp6-eyqVllUB_cWsoxiWEUw8QsT--9I2ECXnxTugKaKlFzCJ1ubSW6Wi9kY1rMntN4WVNjGAb6EFfd8226jlAEkNfeW63PENhXG3UFYzJuaETjlmJJ865L8RjJEpK11qcVV25EXsOp4Ci42vdeEBNNt8wiF6s40KbBV5gOYs-v5pCc7zAHqkwawR3MTTumUEf4ztO4wdeedWmZN5bxBctptynf1E44CKw-V-6jAp1-UzTEoqzRcEfbG4dCzzeapScByrpv5l3WZJV-aCoSYllPUbo90vfz4Fzxx_EvFmpqar7ycfGaNsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9495fe1b87.mp4?token=djP7f7a_1n2UZXsxK_Ww4EfqvWnD7UwNktp6-eyqVllUB_cWsoxiWEUw8QsT--9I2ECXnxTugKaKlFzCJ1ubSW6Wi9kY1rMntN4WVNjGAb6EFfd8226jlAEkNfeW63PENhXG3UFYzJuaETjlmJJ865L8RjJEpK11qcVV25EXsOp4Ci42vdeEBNNt8wiF6s40KbBV5gOYs-v5pCc7zAHqkwawR3MTTumUEf4ztO4wdeedWmZN5bxBctptynf1E44CKw-V-6jAp1-UzTEoqzRcEfbG4dCzzeapScByrpv5l3WZJV-aCoSYllPUbo90vfz4Fzxx_EvFmpqar7ycfGaNsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">غارة صهيونية جديدة على الطريق الساحلي في منطقة الجية جنوب بيروت</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/naya_foriraq/75287" target="_blank">📅 12:27 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75286">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">وكالة الطاقة الدولية: خسائر إمدادات النفط نتيجة إغلاق مضيق هرمز 12.8 مليون برميل يوميا منذ فبراير.</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/naya_foriraq/75286" target="_blank">📅 12:24 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75285">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">‏إيطاليا: سنرسل كاسحات ألغام قرب الخليج.</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/naya_foriraq/75285" target="_blank">📅 12:22 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75284">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e6808ae10.mp4?token=vda_RryUIAWfrvjaA1F--COw6oEB4uY1UUQa5jBke-8xqPKoM4nkTql8IMqQC8tdRbXfegR0CDwBWMcUQTKv_hvZpsnZ1p8ghqu4CXUSTj8EofpgKbhs1UzIm7IqQ9_zCF7k_imA8_knMA2ulbYFWGVz5DvxdTKoSTgdEIwaDRksLTuNFbKES6RD7i1-ZSJOBhvvYdUSYoVpxLGe7AK_vdGNxhz0hRLrQ8ga5u-s-j522Si_3jvDnaP0hHGc-gph2B_PCz0k2rb9nnDxv9yeXVKxcsnXBPoz518s5lLcuPx-EAlyHmc7HM6J62fr_GuOjKs4H3k4IW3BCP297Rs9qQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e6808ae10.mp4?token=vda_RryUIAWfrvjaA1F--COw6oEB4uY1UUQa5jBke-8xqPKoM4nkTql8IMqQC8tdRbXfegR0CDwBWMcUQTKv_hvZpsnZ1p8ghqu4CXUSTj8EofpgKbhs1UzIm7IqQ9_zCF7k_imA8_knMA2ulbYFWGVz5DvxdTKoSTgdEIwaDRksLTuNFbKES6RD7i1-ZSJOBhvvYdUSYoVpxLGe7AK_vdGNxhz0hRLrQ8ga5u-s-j522Si_3jvDnaP0hHGc-gph2B_PCz0k2rb9nnDxv9yeXVKxcsnXBPoz518s5lLcuPx-EAlyHmc7HM6J62fr_GuOjKs4H3k4IW3BCP297Rs9qQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">غارة صهيونية جديدة على الطريق الساحلي في منطقة الجية جنوب بيروت</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/naya_foriraq/75284" target="_blank">📅 10:33 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75283">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">انفجار يهز منطقة الكرادة وسط العاصمة بغداد</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/naya_foriraq/75283" target="_blank">📅 10:24 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75282">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🇮🇶
سلسلة الجثث مجهولة الهوية في العاصمة بغداد
- جريمة تهز العاصمة بغداد العثور على جثة طفلة تبلغ من العمر ٤ سنوات تعرضت لحالة اغتصاب وخنق بمنطقة الدسيم شرق العاصمة بغداد .
- العثور على جثة مجهولة الهوية في نهر التاجي شمال بغداد</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/75282" target="_blank">📅 09:52 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75281">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">انفجار يهز منطقة الكرادة وسط العاصمة بغداد</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/75281" target="_blank">📅 09:33 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75280">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">انفجار يهز منطقة الكرادة وسط العاصمة بغداد</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/75280" target="_blank">📅 09:31 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75279">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ORe8v8Nb4hWTTm0d6XE9FmUTK6XEwUxdW-6JtvLrCSUag75np-VL2Q17xuzPhukSk2Utx9pr9kCtl8KsDweYSrYLiOtaDksKoEg10-x7RNXgA7TcwVwdv4cWaPUAO9FrHxhZ48o9ilcbmsscxIR1jv0Vcy7dohPO3MoeDib2wqtcF2O80qO_Nuh3Ue-0V0URyBLrnfqj2SY0fxWrv8Xag7nF-t3BZMQoFwDNRmmx6T-fzYVQu6E8KDvfqrs_5-UkZL4qXEaI4PgVnQ2ZlZaWFfa2izU1ztUjy4dFaO8EaM_Azu0Docptgyg6b2FAwR5DwOBf_jZ7eoZXy4tHN8IS6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
ترامب
:
ذكرت CNBC بشكل خاطئ أن جنسن هواونج، العظيم من نفيديا، لم يتم دعوته إلى التجمع المذهل لأعظم رجال الأعمال في العالم الذين يذهبون بفخر إلى الصين. في الواقع، جنسن حاليًا على متن طائرة الرئاسة، وما لم أطلب منه المغادرة، وهو أمر غير محتمل إلى حد كبير، فإن تقرير CNBC غير صحيح، أو كما يقولون في السياسة، أخبار مزيفة!
إنه لشرف لي أن يسافر جنسن، وإيلون، وتيم أبل، ولاري فينك، وستيفن شوارزمان، وكيلي أورتبرج (بوينج)، وبراين سيكس (كارجيل)، وجين فرير (سيتي)، ولاري كولب (جي إي إيروسبيس)، وديفيد سولومون (غولدمان ساكس)، وسانجاي ميهراوترا (ميكرون)، وكريستيانو أمون (كوالكوم)، والعديد من الآخرين إلى البلد العظيم الصين، حيث سأطلب من الرئيس شي، وهو قائد ذو تميز استثنائي، "فتح" الصين حتى يتمكن هؤلاء الأشخاص البارعين من ممارسة سحرهم، والمساعدة في رفع جمهورية الشعب إلى مستوى أعلى!
في الواقع، أعدكم، أنه عندما نجتمع، وهو ما سيحدث في غضون ساعات، سأقوم بذلك كأول طلب لي. لم أر أو سمع أبدًا عن أي فكرة من شأنها أن تكون مفيدة أكثر لبلدينا الرائعين!</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/75279" target="_blank">📅 07:16 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75278">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e582f4652d.mp4?token=IQ3Vn3xDKWZMpGV-tCJYCD_eW9M6ZZ9K14cO9JXRj7jB5v-woxMN3TT_HDV8bL1sGpnGbnOFQzhjO1wO9shLrQFkbt1S0jIzp5XU9mQJXuwYSt460KAdIT1fM-2r052yjdE0cSmUYXsHaTuJ0wXFma5lKXLdcJ6qwc-ex_yXVPBhlsjeTvurCoOmUvmMojLhHdZCcfES8sBKoT5ajHgABacGzLr5so3e-uMi-x2j2aBlyX6HC-2vpZLnSzIKCTWbAiFBhr8cA-2DRibcZNnFzn2ZSzxD653nXUC1FVdqxWD4CECgHLRr4DbgVQ3VF37YG7MpEjRxoGrPsKQiHnUI-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e582f4652d.mp4?token=IQ3Vn3xDKWZMpGV-tCJYCD_eW9M6ZZ9K14cO9JXRj7jB5v-woxMN3TT_HDV8bL1sGpnGbnOFQzhjO1wO9shLrQFkbt1S0jIzp5XU9mQJXuwYSt460KAdIT1fM-2r052yjdE0cSmUYXsHaTuJ0wXFma5lKXLdcJ6qwc-ex_yXVPBhlsjeTvurCoOmUvmMojLhHdZCcfES8sBKoT5ajHgABacGzLr5so3e-uMi-x2j2aBlyX6HC-2vpZLnSzIKCTWbAiFBhr8cA-2DRibcZNnFzn2ZSzxD653nXUC1FVdqxWD4CECgHLRr4DbgVQ3VF37YG7MpEjRxoGrPsKQiHnUI-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭐️
مظاهرة إحتجاجية ضد نظام آل خليفة ،رفضاً لإسقاط الجناسي عن العلماء والمواطنين في البحرين.</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/naya_foriraq/75278" target="_blank">📅 01:56 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75277">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DKIFRYj0xa0T3quG0eS8KuuN4sw80G_39Dl_5reO_9ZUxYyR8SumAtQwGaSlx6zjI-w-K0y3YHETSekZNciHftv4Wkuz_MEhNKgtaLugbcu7L5ryRQ3qW9N5pg-7XD1xHAZqNlaihWKWFmkFvPtMRihNnXH3ACKYSgv3Ru1cuUUrzcP1hXXjiJ3d7XL3nomo916c-qpz_1dz8kO-HZc2NErtzxR1k51yfRk-lKXmXVp3qyNMoKSARKL0mHWIVwZ0PxfGG_E1k6K4IZu2unzWsFD9LV7pNYlacxyqXRVS5zBJvrDw262vHkhMjk7hs61LZwpI2ZbD5bpgQNDYAfjJdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامب:
عندما تقول الأخبار المزيفة أن العدو الإيراني يبلي بلاءً حسناً، عسكرياً، ضدنا، فإن هذا خيانة فعلية لأنه بيان كاذب، بل سخيف. إنهم يساعدون العدو ويحرضونه! كل ما يفعلونه هو إعطاء إيران أملاً كاذباً عندما لا يجب أن يوجد أي أمل. هؤلاء جبناء أمريكيون يخونون بلدنا. كان لدى إيران 159 سفينة في بحريتها - كل سفينة واحدة تستقر الآن في قاع البحر. ليس لديهم بحرية، وقد ذهبت قواتهم الجوية، وذهبت كل التكنولوجيا، ولم يعد "قادتهم" معنا، والبلد كارثة اقتصادية. فقط الخاسرون والجاحدون والحمقى قادرون على توجيه انتقادات ضد أمريكا!</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/naya_foriraq/75277" target="_blank">📅 23:55 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75276">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">⭐️
هزة أرضية بقوة 3.4 ريختر تضرب العاصمة الإيرانية طهران.</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/naya_foriraq/75276" target="_blank">📅 23:47 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75275">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68cdd385b3.mp4?token=VQ9TxjV-H6K_EQrlLUxie4FyMgwADH6KYHVEGpebKlfwgS5rKNtgLeky7Q8vuO6sfxzMGxsi_NyguVlqL9icdWi0fIp0hOLriLfpdUVBnYHztCympN23uIc90XVc7vBcCKfnZesEusoNtwhuMa1Fthd4tLUInD7EDbIF4BiXBXwrPJKzzJ6lGkcpYMXuzZ0XabaWCMO3_Y75DVeNE42n0GxS2Cz2QfX70mFKzGnlbBeZV8MJBT6BnH0WGhiZuppRc-9bGwkhajlqmzlwE7D2OlfWYoDasoxW3P39OkQLuzWJuMuI4vtet7WVQ7Tyd03Vbx4kNnNv_kL4z4yz6DVWWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68cdd385b3.mp4?token=VQ9TxjV-H6K_EQrlLUxie4FyMgwADH6KYHVEGpebKlfwgS5rKNtgLeky7Q8vuO6sfxzMGxsi_NyguVlqL9icdWi0fIp0hOLriLfpdUVBnYHztCympN23uIc90XVc7vBcCKfnZesEusoNtwhuMa1Fthd4tLUInD7EDbIF4BiXBXwrPJKzzJ6lGkcpYMXuzZ0XabaWCMO3_Y75DVeNE42n0GxS2Cz2QfX70mFKzGnlbBeZV8MJBT6BnH0WGhiZuppRc-9bGwkhajlqmzlwE7D2OlfWYoDasoxW3P39OkQLuzWJuMuI4vtet7WVQ7Tyd03Vbx4kNnNv_kL4z4yz6DVWWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
🏴‍☠️
دبابتي ميركافا تابعة للجيش الصهيوني (8 دبابات خلال اليوم) تم إعطابها من قبل الأبطال في حزب الله بجنوب لبنان.</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/naya_foriraq/75275" target="_blank">📅 23:06 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75274">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ee72acfb5.mp4?token=OxMAl9QRmLtjYmlOeSGnHJ-Sf3P22jmKK9pJZCppbR8gwVN8tgy5zNmnyN1JCSTeNSs1RO10Q1GLOk0xaXxuwgshVub9lWWv_ofgJwM_sqGUtBK-x66kYWMoY2Xa5rEGNn0560ujHMbl1rBW4jACeyPtH_K7i6KZ5GDgG_mj_eL7pUdmCqckVWgVBcpIYfsPdLFApHXt97PLvc_BOXlNGg_WyKZYsqSaPLOJQCofdj2irsFDUEFsWnp1Y-pDm_t4HG0cFYD9D69QYhm2W5CPYpenH1evMDpDtLndVZdBACyz83b2BuuYD_f8R-pmqByKatsknBlcxuRQCQIwoGQcHaAJiBOcaCOXHX1mDTS0c2CLhZ-2WFfnQSKz7lVDf8oldt4QxQjR694qcjDquIGUEBaHPdwWj7_ERwe_C0aPUBS7hnG21fohYqchQ3MpCaUrJfEKNxaHtUwZDN6IwmEW7S-L6jcpt9nBg3XFugsXM-zSamt2vFA1tjRCZyGYeF0DF7PBoWuIs3UPJNFDWtlUtAsuSr23KVrCc4EJLMgSR08ikovCqctQaGwL5-6pj6Pe01P2WkDWiSDCg9zEswjRevvOTxTjEREmogwu5rKd5A4f0L838c_PtblNbw_WPmTj_QkZg1xAIICCFKmJAfL2n7mayVtYZUGuPxyRNcxrvUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ee72acfb5.mp4?token=OxMAl9QRmLtjYmlOeSGnHJ-Sf3P22jmKK9pJZCppbR8gwVN8tgy5zNmnyN1JCSTeNSs1RO10Q1GLOk0xaXxuwgshVub9lWWv_ofgJwM_sqGUtBK-x66kYWMoY2Xa5rEGNn0560ujHMbl1rBW4jACeyPtH_K7i6KZ5GDgG_mj_eL7pUdmCqckVWgVBcpIYfsPdLFApHXt97PLvc_BOXlNGg_WyKZYsqSaPLOJQCofdj2irsFDUEFsWnp1Y-pDm_t4HG0cFYD9D69QYhm2W5CPYpenH1evMDpDtLndVZdBACyz83b2BuuYD_f8R-pmqByKatsknBlcxuRQCQIwoGQcHaAJiBOcaCOXHX1mDTS0c2CLhZ-2WFfnQSKz7lVDf8oldt4QxQjR694qcjDquIGUEBaHPdwWj7_ERwe_C0aPUBS7hnG21fohYqchQ3MpCaUrJfEKNxaHtUwZDN6IwmEW7S-L6jcpt9nBg3XFugsXM-zSamt2vFA1tjRCZyGYeF0DF7PBoWuIs3UPJNFDWtlUtAsuSr23KVrCc4EJLMgSR08ikovCqctQaGwL5-6pj6Pe01P2WkDWiSDCg9zEswjRevvOTxTjEREmogwu5rKd5A4f0L838c_PtblNbw_WPmTj_QkZg1xAIICCFKmJAfL2n7mayVtYZUGuPxyRNcxrvUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
🏴‍☠️
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ
09-05-2026
آلية "هامفي" اتصالات تابعة لجيش العدو الإسرائيلي في بلدة البيّاضة جنوبي لبنان بمحلّقة انقضاضيّة.</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/75274" target="_blank">📅 23:04 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75273">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🌟
🏴‍☠️
دبابة ميركافا صهيونية تحترق بعد استهدافها في موقع العبّاد بواسطة محلقة انقضاضية.</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/75273" target="_blank">📅 22:50 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75272">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y6LSRaKo8u1Li1YH8RT33Kte4bnVSf-4monLtrMogk4htDib76sLJIQbNa0kKXYTD3t4JtRSZBPzqp6kncwSstNIWXx49aVTrIPzVG9XJOPIzptXAP9aqU_JNfmJLJPcnQKngE2yuaB2aTukAn9Z-y_HJsPJmQcdWRuRy3jnqxh7RsuWBqtMDOsIxNIO6lUawHPjvNc26ZTgEES4v_yblhaBsP5geqgydaCiPk3B_T-4a3KaLAx2VHalmqrSvHPk7v6hRC4QX-02j52GYR5pAse9bBAsDjYXqik_QkDKCSdg_qc0XspKMlc59fHZcQGxIBBm84z9XJwzCJDn2pJ6-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">في خبر غير مهم  وزارة خارجية دويلة الكويت تستدعي السفير الايراني وتسلمه مذكرة احتجاج</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/75272" target="_blank">📅 22:44 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75271">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🌟
🏴‍☠️
استهداف دبابتي ميركافا للجيش الصهيوني في بلدة الطيبة بجنوب لبنان من قبل أبطال حزب الله.</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/75271" target="_blank">📅 22:30 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75270">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">⭐️
رويترز:
العراق وباكستان أبرما اتفاقيات مع إيران للسماح بشحن النفط والغاز المسال من الخليج الفارسي.</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/75270" target="_blank">📅 22:12 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75269">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/792b04ea24.mp4?token=sN35FGdEW0AuDLGTxd3Ybn7TAMLoqWdMzW4MgvzcoFGaqyEz3bMVqrymv0O76mxzUCfKiUMMJQgx8GtRUspVJ_bJsIXuCXwbAGzHyzi8GwhdCwtb4zOKqNjzqGXwqD2jt7JsfgVm_Ivh4f2e0L86-cnGcWrLRNFqoh-D2InL_hiqGSVWMpMVHPkgoIShvKZy4-HT2Afb1obxp1Yvy7jTssgI7YidV2OQfxuKpI5mJFgxUDxsMSJNzacK625c_mi2K4db26do6mp2xMuwURckjuwsTIuN-74Xz-on5Ug5cFePFIJTtFl_XWS_W_FFL4ch5c6J1OIslw9caZbPSeWCaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/792b04ea24.mp4?token=sN35FGdEW0AuDLGTxd3Ybn7TAMLoqWdMzW4MgvzcoFGaqyEz3bMVqrymv0O76mxzUCfKiUMMJQgx8GtRUspVJ_bJsIXuCXwbAGzHyzi8GwhdCwtb4zOKqNjzqGXwqD2jt7JsfgVm_Ivh4f2e0L86-cnGcWrLRNFqoh-D2InL_hiqGSVWMpMVHPkgoIShvKZy4-HT2Afb1obxp1Yvy7jTssgI7YidV2OQfxuKpI5mJFgxUDxsMSJNzacK625c_mi2K4db26do6mp2xMuwURckjuwsTIuN-74Xz-on5Ug5cFePFIJTtFl_XWS_W_FFL4ch5c6J1OIslw9caZbPSeWCaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامب يغادر واشنطن متوجهًا إلى بكين في الصين.</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/75269" target="_blank">📅 22:03 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75268">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a470cd8205.mp4?token=ZFqGmhhBpl9u-bMG9Qqz1esUgJo6e-K6dmklUjjNPHHUbjjBmXp0jaFjDYTmib3jTtT4cIIR0TqpszWgtHwNLiqEd3K10XpcuQilsNz3vcqakJVD4reU-TY9QN_JDYz-An5wxrLcCIvzWtKeZqwBene2gd7DpoM7XXR05Xw9oTC4jbekxg2y-UiJV6TkBpxOYTcUCFLfQ4tzaMbXV6wa2yD0SxRKz-f-4vD7JpeAYShdiQmFVxeW0GqOQby05LHYT1cFzCycQ709Tnx5qkB6p7Rfhkt1Y0obFKGYc0P8iSh9U5ADL56aWGg66Oh4ZsM7uaM-Sc0AbaT2in7OCNICfIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a470cd8205.mp4?token=ZFqGmhhBpl9u-bMG9Qqz1esUgJo6e-K6dmklUjjNPHHUbjjBmXp0jaFjDYTmib3jTtT4cIIR0TqpszWgtHwNLiqEd3K10XpcuQilsNz3vcqakJVD4reU-TY9QN_JDYz-An5wxrLcCIvzWtKeZqwBene2gd7DpoM7XXR05Xw9oTC4jbekxg2y-UiJV6TkBpxOYTcUCFLfQ4tzaMbXV6wa2yD0SxRKz-f-4vD7JpeAYShdiQmFVxeW0GqOQby05LHYT1cFzCycQ709Tnx5qkB6p7Rfhkt1Y0obFKGYc0P8iSh9U5ADL56aWGg66Oh4ZsM7uaM-Sc0AbaT2in7OCNICfIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
‏ترامب: أنا من سيعلن عن نهاية الحرب مع إيران.  يمكنني أن أنسحب الآن لكنني لا أريد ذلك بل أريد إكمال الأمر تماما.</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/75268" target="_blank">📅 22:00 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75267">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">⭐️
رويترز:
شنت المملكة العربية السعودية سراً ضربات جوية انتقامية على إيران في أواخر مارس بعد هجمات متكررة بالصواريخ والطائرات بدون طيار من قبل إيران على المملكة.</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/75267" target="_blank">📅 21:56 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75266">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">⭐️
هزة أرضية بقوة 3.4 ريختر تضرب العاصمة الإيرانية طهران.</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/75266" target="_blank">📅 21:49 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75265">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🏴‍☠️
جيش الإحتلال الصهيوني:
إصابة 190 ضابطا وجنديا في معارك جنوب لبنان خلال الأسبوعين الماضيين.
مقتل 18 ضابطا وجنديا وإصابة 910 منذ تجدد القتال في جنوب لبنان مطلع مارس الماضي.
إصابة 114 ضابطا وجنديا بجروح متوسطة و52 حالتهم خطيرة.</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/75265" target="_blank">📅 21:45 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75264">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🇮🇶
وزارة الدفاع العراقية: صحراء النجف الأشرف تخضع لسيطرة كاملة من قبل القوات الأمنية العراقية.</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/75264" target="_blank">📅 21:41 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75263">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🇺🇸
ترامب: قضينا على الجيش الإيراني.</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/75263" target="_blank">📅 21:39 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75262">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🇺🇸
ترامب: قضينا على الجيش الإيراني.</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/75262" target="_blank">📅 21:38 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75261">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">أنباء عن إنفجار في مدينة صنعاء اليمنية.</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/75261" target="_blank">📅 21:26 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75260">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qp9ubC3dnspd18nZaJGbot1MN_yXw11fX4aqLJHIOnZ2WwPYtocnL7LMpfqPqsNTlLkxXIjG9RHAGV-q6AmKdrrsHzBAmwLdrzRXXYpSmq_rvfcoqNGL57eQI6OdmKk9ZsJh-X7iu0fQZGLseOxce4tfFJX6gd7xtqF_MUHDS1sFNZH-Db90lzhA_k8umUBIV9bT_FK6uis44peEOjt3yQHawfCWkw0q3gBGtwLP1QRDYXpQxLH3X75Srqe9T5ARK5E2b0lGFns8WjsmmbgBySGQrL8Xsts8rbbOGAU11c-bMXeTM4OrWR4mBEG-nayU6eGwPf1u2uSYzJ6qug9K_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامب: لن نبرم مع إيران إلا اتفاقا جيدا.  ‏ لا أعتقد أننا سنحتاج مساعدة رئيس الصين بشأن إيران.  حلف النيتو خيب آمالي ولا نحتاج إلى مساعدة منه.  لا أعتقد أننا بحاجة إلى أي مساعدة بشأن إيران وسننتصر بطريقة أو أخرى سواء بشكل سلمي أو بغير ذلك.</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/75260" target="_blank">📅 21:25 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75259">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/khjqhpd00Li0J860CS5JXlh6kWf02UQ29URcl4OYzSgtbSuhT0ZnSjahbJKFiQh6KCsL49BczU_0DTkUbvAdBxlN1Fp7CQRDtj7pJS17jaXk3r6KpludJjIiwz7YJZ0k0DzDAElWaCQ60MS-SiwiqxCtXSxTNup0o_pDia7pmWtZYPv2zC6m0d4EHHqWXGhsvzoidS95dFtFFkMVkRu0oCo_WjhV7WZftP_0fA0Q3Xd25qT59WRv8qH25iDJpjoJQo6sz1kGdss-TdDpz_Y7HgW8NVtaEF-NIGECyJzE2us7_9JLfOYwvSprwWYSu9cqSQtUgjMpOjElm14pKsDwCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴‍☠️
🇱🇧
الدم بالدم
عن مسيرات حزب الله التي تتبختر بالجليل</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/naya_foriraq/75259" target="_blank">📅 21:24 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75258">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23265c0b8f.mp4?token=HzqdmypTmwkzRe8slFzdJIWENqwVNa61xKaU0KmO-AYLkI8ZrUn16loCexu1beihtEwMrEm71NjiA8msqTD4-5hTNmXyhJFfIKHesk0DADrHAvlE2tMmkJuWM7pQpSPuf0pe87Rcd9QpKSTZFHVjoZLZbuKyQ3cGJO7yJYu1jXBPCwTxK4OPauhVaH_hq9TmwLZKkVnTSkGnwLngSMwLefSs9GyLXLjJDL-tub4anThUlqwA32hUof_yLZzLVwL7ZqlkIh9B1a0Mketvnl3_ZOanN9G1WMu_1nHmSYpgAKe80oUagUDS-QoVc1Vgi0kws0Ofp-L4aGTi3ub-imZOmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23265c0b8f.mp4?token=HzqdmypTmwkzRe8slFzdJIWENqwVNa61xKaU0KmO-AYLkI8ZrUn16loCexu1beihtEwMrEm71NjiA8msqTD4-5hTNmXyhJFfIKHesk0DADrHAvlE2tMmkJuWM7pQpSPuf0pe87Rcd9QpKSTZFHVjoZLZbuKyQ3cGJO7yJYu1jXBPCwTxK4OPauhVaH_hq9TmwLZKkVnTSkGnwLngSMwLefSs9GyLXLjJDL-tub4anThUlqwA32hUof_yLZzLVwL7ZqlkIh9B1a0Mketvnl3_ZOanN9G1WMu_1nHmSYpgAKe80oUagUDS-QoVc1Vgi0kws0Ofp-L4aGTi3ub-imZOmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامب:
لن نبرم مع إيران إلا اتفاقا جيدا.
‏ لا أعتقد أننا سنحتاج مساعدة رئيس الصين بشأن إيران.
حلف النيتو خيب آمالي ولا نحتاج إلى مساعدة منه.
لا أعتقد أننا بحاجة إلى أي مساعدة بشأن إيران وسننتصر بطريقة أو أخرى سواء بشكل سلمي أو بغير ذلك.</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/naya_foriraq/75258" target="_blank">📅 21:23 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75257">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🌟
🏴‍☠️
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ
11-05-2026
قوّة لجنود جيش العدو الإسرائيلي بعد رصدها في منزل في بلدة الطيبة جنوبي لبنان بصاروخ موجّه.</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/naya_foriraq/75257" target="_blank">📅 21:15 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75256">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🌟
🏴‍☠️
استهداف دبابتي ميركافا للجيش الصهيوني في بلدة الطيبة بجنوب لبنان من قبل أبطال حزب الله.</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/75256" target="_blank">📅 21:05 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75255">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🏴‍☠️
🇮🇶
جانب من انتشار جحافل قوات الحشد الشعبي في صحراء النخيب غربي العراق للبحث عن اي تواجد او نشاط مريب ..</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/75255" target="_blank">📅 20:38 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75254">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">⭐️
الحكومة البريطانية:
سنساهم بمسيرات ومقاتلات وسفينة حربية في مهمة متعددة الجنسيات لتأمين مضيق هرمز.
‏مهمة مضيق هرمز ستكون متعددة الجنسيات ودفاعية ومستقلة.</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/75254" target="_blank">📅 20:34 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75253">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🇮🇶
وزارة الدفاع العراقية:
صحراء النجف الأشرف تخضع لسيطرة كاملة من قبل القوات الأمنية العراقية.</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/75253" target="_blank">📅 20:14 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75252">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🌟
🏴‍☠️
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ
11-05-2026
جندي من جيش العدو الإسرائيلي في بلدة الطيبة جنوبي لبنان بمحلّقة انقضاضيّة.</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/75252" target="_blank">📅 19:55 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75251">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🇺🇸
‏
الطاقة الأميركية:
أسعار النفط ستكون أعلى بـ 20 دولارا حال إغلاق هرمز حتى نهاية يونيو.</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/75251" target="_blank">📅 19:49 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75250">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/16dad3ff36.mp4?token=DiEx5FKiDnGnQHTXsSgO0bJorARITNJU9Fd6-9lOg1AO3gUcre7KwhrEY-lG5lDv2P-NxV9ufXlri8HLSZa-EpoHMrBtxqEwPsq0eNc-TRdC1jUx6zijdOjxjyoQS6ozpLCkUJ3C4R0KjI8SHcbkyKobzmONJMYQSZeeiI6ubNwF8AEEN9it6WP4brLRYMS5U5hX34UxHuSHacRLyviOilfYezqnBhyyZUuFlSPjDD65cEVEDX0EBY172yTq7T43Z9X8OcrWBS-pN8zzndXTEDSSAV6icqyplZ0LsG8DIoN0m5tQ4hqcAgtttUvJFUmkvvc0Rpnlj7CzNGMSRubKFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/16dad3ff36.mp4?token=DiEx5FKiDnGnQHTXsSgO0bJorARITNJU9Fd6-9lOg1AO3gUcre7KwhrEY-lG5lDv2P-NxV9ufXlri8HLSZa-EpoHMrBtxqEwPsq0eNc-TRdC1jUx6zijdOjxjyoQS6ozpLCkUJ3C4R0KjI8SHcbkyKobzmONJMYQSZeeiI6ubNwF8AEEN9it6WP4brLRYMS5U5hX34UxHuSHacRLyviOilfYezqnBhyyZUuFlSPjDD65cEVEDX0EBY172yTq7T43Z9X8OcrWBS-pN8zzndXTEDSSAV6icqyplZ0LsG8DIoN0m5tQ4hqcAgtttUvJFUmkvvc0Rpnlj7CzNGMSRubKFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
🏴‍☠️
حزب الله يحرق مواقع وآليات العدو.. سرب من المسيرات ينطلق من لبنان مرة اخرى ويستهدف أماكن تموضع الجيش الصهيوني في الشمال الفلسطيني المحتل.</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/75250" target="_blank">📅 19:44 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75249">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">دبابة ميركافا صهيونية تشتعل بعد دكها من قبل أبناء نصرالله</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/75249" target="_blank">📅 19:41 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75248">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h8gb2MRHvRQfcHwNqy-VjE0am46jYuwdBOqW68xwRcouGBojo37rvKizp24cZjLoqEom9aiq3NRCG_JZ-qRByMuNkql3U7mE6iN1zQQSWU_t1J8rp5O166DvqTGjH5Y2MMpgVYgYzR5wLttS5FXL65CKxo72al7L65KoEuZV7ljiJzJsenVwXNvdFc4uLbsLCx3VXdL08TTv47KFF6WinvcbNoZSXhN2HEoQ6R0OV5sZpZlfvZyHDf3GE9tUnVc1vNTgM4fEBJVFRZbdSxqvqOAQvqcOvqdFfTZ0ap5PPn6X3g5ks5luuwpsZS_rO0Ozi8VsLrpIAUzIBdu4KaVQUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴‍☠️
إعلام العدو: حدث أمني خطير ومعقد على الحدود الشمالية، مع وقوع عدد من الإصابات، فيما لا يزال الحدث مستمرًا والطيران يعمل على نقل المصابين.</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/75248" target="_blank">📅 19:40 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75247">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🌟
🏴‍☠️
مجدداً من لبنان.. الطائرات المسيرة تهاجم مستوطنات الشمال الفلسطيني المحتل وتصيب موقع عسكري صهيوني واعمدة الدخان ترتفع منه.</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/75247" target="_blank">📅 19:26 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75246">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gw2EUW556K7egetDc20k50i4PjkvFXh3HBrhXmHbz91gPhNdkkZlXg76wBPEoJnVuRPStxhhM_6EHz_mRWy6W3z8hDc7Hwj4kYgVg2K3AjnVA06907Q1lyXVruXgv54vCq26IWsGA7xm3rYWHkk1dBiE0uqDNweISrni7h1kg92ZGUsBNk1ltHdK_Jj87H2JxeAEbRIvrEsq5ItBTx3X_I9p8sRjUQ02BaJrEyiWYhWpDGHdjF8AWACbt-WpTOyNEDWlM1bkZpZQr7vPosGIGx_-1LLUiph5RXhC1wuCzJtnkFr7AaYnxlAxoSEawUA5ZMraxlG5R0GbS2FO_rZDRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طيران مسير من لبنان يهاجم مستوطنات الشمال الفلسطيني المحتل</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/75246" target="_blank">📅 19:14 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75245">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🌟
🏴‍☠️
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ
09-05-2026
خيمة مُستَحدَثة لجيش العدو الإسرائيلي عند خلّة الراج في بلدة دير سريان جنوبي لبنان بمحلّقة انقضاضيّة.</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/naya_foriraq/75245" target="_blank">📅 19:00 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75244">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">بعد منع ناقلة تحمل نفط عراقي من المرور.. المتحدث باسم القيادة المركزية الامريكية: قواتنا منعت ناقلة النفط آجيوس فانوريوس من عبور هرمز لانتهاكها الحصار. ناقلة النفط كانت ترفع علم مالطا ولم تكن محملة بنفط إيراني</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/naya_foriraq/75244" target="_blank">📅 18:58 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75243">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">طيران مسير من لبنان يهاجم مستوطنات الشمال الفلسطيني المحتل</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/naya_foriraq/75243" target="_blank">📅 18:57 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75242">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b91423ce81.mp4?token=lDQiuMCVKJnbTuYwDQ8SPwwkG5VubaM7eXTHSmBsbXJqlQZlYG7j6LPvh-6n5cqUi9nvWArBttTdGEunv7xlFgcOYDsuw0-SOwTtUpYQhRaDuvpHk4N5_Fd_OPy3CnRkxWskFbwZpR-KKHQogzX1EF6UEOgwNWbHOhhckEvKeYc3HIPt-V_SPw2grCrg4tdK_pl06JhSTi5wk5CO6BP7u9HtTZfLQL1R2jxwjI3Q87pjFcppIF5QWc8z0lar16nktDqnbkLmTh6yvsCaIsQxhVDMrumDH8M17RWtgCkVXOq2uUe9VjFCIqltDn64OVL202MJ0vQxa5S4hNS-b4zPtA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b91423ce81.mp4?token=lDQiuMCVKJnbTuYwDQ8SPwwkG5VubaM7eXTHSmBsbXJqlQZlYG7j6LPvh-6n5cqUi9nvWArBttTdGEunv7xlFgcOYDsuw0-SOwTtUpYQhRaDuvpHk4N5_Fd_OPy3CnRkxWskFbwZpR-KKHQogzX1EF6UEOgwNWbHOhhckEvKeYc3HIPt-V_SPw2grCrg4tdK_pl06JhSTi5wk5CO6BP7u9HtTZfLQL1R2jxwjI3Q87pjFcppIF5QWc8z0lar16nktDqnbkLmTh6yvsCaIsQxhVDMrumDH8M17RWtgCkVXOq2uUe9VjFCIqltDn64OVL202MJ0vQxa5S4hNS-b4zPtA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴‍☠️
استهداف موقع للجيش الإسرائيلي قرب مستوطنة مرجليوت واشتعال النيران داخله.</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/75242" target="_blank">📅 18:52 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75241">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">بعد منع ناقلة تحمل نفط عراقي من المرور..
المتحدث باسم القيادة المركزية الامريكية: قواتنا منعت ناقلة النفط آجيوس فانوريوس من عبور هرمز لانتهاكها الحصار. ناقلة النفط كانت ترفع علم مالطا ولم تكن محملة بنفط إيراني</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/75241" target="_blank">📅 18:23 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75240">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">في خبر غير مهم
وزارة خارجية دويلة الكويت تستدعي السفير الايراني وتسلمه مذكرة احتجاج</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/75240" target="_blank">📅 18:18 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75239">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">صافرات الانذار تدوي في المستوطنات الشمالية بعد هجوم صاروخي لحزب الله</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/75239" target="_blank">📅 18:09 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75238">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🏴‍☠️
اعلام العدو:
تهديد المحلقات يتوسع باستمرار ويوقع خسائر كبيرة في صفوف القوات على الأرض.</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/75238" target="_blank">📅 17:48 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75236">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Xgaw--0sY6xiK3bzW4XDGtT7flj8l1zYi4C4y4qj-uwu_ahETnAsVG5dxu7EGzDdNKZLc6_n7vV5DkI5iwUsGpsZEv79pwEhQIwNBdTdfPZaXRe-Qh4m5itDp2x1naMC3efNz6SaHQiyUCicsLRiIm__wemZIvBwuTCyA7EXGMSZfSKaBtM2rioJgK7PhhW4OVirGxrRvv6DONb6pOtsUF4mwYYBY2wajJ3yG0A31C89q2OgRGuktvyNwK61uNTFjWrsyVicKGm4wUOMRPwotXoeCKsa0V2RD32IshAQE4V_0GgFkHaQGNkEJhzF3Uquq_KjhBcOysm9MACiOiOMyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HjeZbJpvNLutcnoRdMLYffHg126c3b8n9hwXHA2GL58lp3FK39B28b-7KB73XJ0xn7NYui5WhwRoQHiQJFkKStXDyo59g-i_EcXGV_q-JUKSU7gr-wZZHKHo5TpwlkPghyI_2ZEDEfb9kQFe8_6C3VV-RLs4_59TOrr-BJVfTGwQ2UYU3A-wUQ_lz5advcDDFXGNnuLRInKxOyAJ-TOHVHdR3s_-J3d7tsuPWH0C0bEP-68XXbu_J5_QVA6SfpdYQjdrrulAfwIGdjk2CjDVp3h0cp3fpGtpfOmsU1J-WXXKbI3rNPxhHydCk_3p-PUW8LHvfp4rCIP9yF3DQ8TqCw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇻🇦
🇮🇷
بابا الفاتيكان "ليون الرابع عشر" يمنح أعلى وسام دبلوماسي فخري في الفاتيكان لسفير إيران لدى الكرسي الرسولي محمد حسين مختاري
ترامب يعاين الاضرار
😄</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/75236" target="_blank">📅 17:34 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75234">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🏴‍☠️
اعلام العدو: تفعيل الدفاعات الجوية في الجليل الأعلى بعد هجوم لحزب الله.</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/75234" target="_blank">📅 17:27 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75233">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🏴‍☠️
اعلام العدو:
تفعيل الدفاعات الجوية في الجليل الأعلى بعد هجوم لحزب الله.</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/75233" target="_blank">📅 17:14 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75232">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🇷🇺
‏روسيا تعلن إجراء اختبار ناجح لصاروخ "سارمات" النووي وتؤكد دخوله للخدمة نهاية العام.. بوتين: مدى صاروخ "سارمات" النووي قد يتجاوز 35 ألف كيلومتر</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/75232" target="_blank">📅 17:09 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75231">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">ترامب: نجري اتصالات مباشرة مع مسؤولين إيرانيين ولسنا في عجلة من أمرنا للتوصل إلى اتفاق</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/75231" target="_blank">📅 16:58 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75225">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bVNdpHAe49eB5JqYtYIVcFq8gWyZfxRROXO1AWESywkAvyAgQCcaOQ5f3UT8MQ_5K8XfwhyWLqamcYfoZhtzMyz_yS6kyntzXii3FDyfcVZRfNg_pPK3AKn9lPmUA6jyXn1AmFbZ2wkpBgEWy_rra77La-7rhbIoemETHDsOODzCp-UhRfzeIMPPnb5Ez8umF4TMicOi1G9y4JyyIsq6HLs_irHq0z4Mi7Zzi-mXzsQbM51AiZoj7q1D79WFD6rP5e2-nG1bAMx1O2SqWb_D3kMw_fkhamslTYYPb_nqBr1vLCxScj9xDyAFpo_liKoesH_GuPwzoBFzGizaBMU9PA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YlQrXaGsL63pCT05fbX4DdqkcGl2BHs7lF4CtkQ-wSF0j8ELUP0ryk5Fgd0vompM0MbCHlK5EU9rmg87coTSEo8Eib3wkpyTGveYDF9-ahWfOlcbTK7COAcpHMcCiQAL27aIB0HO8AeFpxGuUmf5atYCJdSUa7Jvhgk9aELXyBCLYhKDaS0BV5BwNwekybyqrJ5I2wTabBUzWdN21eSbrWc7Vzn7bV8e24AE960I3XCvtiwni94ZARlV7VIli4d7jat_SYHivD3szaqBiNMc7z4o4r1hP9V0akCebhweQml7Se9graWo8Lhc2PCRZdWRWKqmjTXrkArTnu6zsHcoYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QOdJ2v1HEE5BgVJn-NjGH1K-vGEPoH1gDcJgGJ2LJ0BSUGbH4_CJiLenYvlz_cfWzPAdPB5LWGdCRoe-ExruwZPdEomHSAjqvs7Ob4P9KPbKw8EbwgS7YuI-B5UeEJxcsY_wK9lTS_wZ5scMwgSB7eCTdxxH7CQFeV48lJ4u9Rllje27C3_37ln8jl1PXyvHcc9ahIA-8_tKuBWvV_726zuEE7HS585p5nPMyjHnGiyuDVQKJi5fdNEuWNcleLFhcsWcozibSjNbOHZo4L7eOm_vj6sllaRGqoVeooGxjLAWMfF5Hhucusu6TRgreHQSz2r883acUEHqxnhAbm-cOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iN1XoODDPlnJFO4drYneRud3x-fQcCLe2RdAorwQOxKoxWcRLips-v9DnhJ_EWdS1FQqb5qV9Nv1FD5R9M8LDi95PpS6ykcTtPPQaPLd8vOQwP4aDb1-vkWgiLwkrzGEwYVSHQQ12JanebgZEirmFIQzBMWGQflP8wZAG2_0Aqk5DEDUewZ2F9QTmuHe9j_Fs8yz0xSqarKsuVXPO3EIPivkoXtFZocFtFLqk5rHCf-nP6dsHsNH8YNNSbflvqduA-XJwF5F-Wjy6WtR8e3u_wU9XAQuxSfbcz9i3ccoTJlikmBFbelWN7tvoaQMrggy-eTlAm0-ve2jDN72URZSfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RcjEgxDCrvjQ-KXGmUFHNWvkAR4-9_9JUByscw6GDvAHvckGi3u6nFWE9aeeUzOv42J1gajySZsJ2K4cr0xRs5cU39ywPflcrk9SoHMRaGOaV3qlb-4hxAO8pbkmn_33Ud_3jsjoxk6pAolp9hzUC9HzQi3L_k2iR9FA6YMwLP55J6BWHliAvZll5TJs8vKCFdx4a8ZBFiy8KzNcQ_e9mfrb_AypSUkEjI0UthK8qGsfaa2XNeOHLSlgkMG53szBO_1dNg96HjtuIkwVFmbqvPqEgKt5i2P241DbaojiXYNbTOp5hoY9Y_UQ2ymfjrZLNt25EWc5sBtZwAZ4XQHtSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q_uqwyI6hmohcbl_zMwWQP0Vrltw0-7fQj9K-wkpsj99SMoKVZl0pOo03oefcj5oaOPs0F_mkCWL1bIDSd3esdOP-DrralfIYdfvxL0N9A7Kytf8Lmi06oLOE_85koUO5TyxieAolPormm1VCT7Sr0EMqBlOQJplyaYRNf-7_9gsTMqaUNixq8TKUR8VVPpk6u6jZS0LboAiX2o2j1fNOsdsNMOOaqAY2K1ji3uOpE1xeGGtqRIFN2tuUoMM7fT69bWmPdnT36rIx2RpaPAS7Uz3HYzn5B-c_ROU_hQaSApWz_LDavkRDDcTBexZMnntIuldJQ-gxCNWbolQhFqTkQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ماذا حدث في منطقة شنان قرب الاديان لمن هي الـ عجلات العسكرية المدرعة ماذا يفعل الأمريكان بالأحداثية  ‏37R  KV 750018  3478349 ما قصة هبوط هليكوبتر عدد ٦ ونصب خيم أمريكية في صحراء الانبار جنوب ناحية النخيب منطقة شنانه الاحداثيات ‏38R  KV  69654  98230  لماذا…</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/75225" target="_blank">📅 16:49 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75218">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OmfB7eRoIGA-jn13pmu85f1JJhFC_yHk5qJXfbhpxEWJL8HELmnpyL1batetck5zwd45eD86jO9zXi8-q8g1e_mT-yjOQXCtG0RFp0UZyXQ17hEtZIyEeP01zkLeiRlm4O-771rVA89b5uPR9T9Ky6hs0mjrYEOAu7PGU5CGr7z467xaonQRaL7B3-So-j0moxvUuI9yBhUHbhqaGf4NNvzHOse_yrRVClnwGsgD9WfwMAB53965_md--tcM_9hTrBfvwoXUSHHUew-KUJF4Byg5eTDMXh4VVtDsQemt_1smVs8UgspUyfN_W-cxLCyG9RGxECKAzMuTRTYo4ZQ8WA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
المتحدث باسم لجنة الأمن القومي الايرانية:
قد يكون أحد خيارات إيران في حال وقوع هجوم آخر هو تخصيب اليورانيوم بنسبة 90%. سنناقش هذا الأمر في البرلمان.</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/75218" target="_blank">📅 16:38 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75217">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">وزير الحرب الأمريكي: لن نكشف عن الخطوة التالية ضد إيران لضمان عدم حصولها على قنبلة نووية</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/75217" target="_blank">📅 16:19 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75216">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">الرئيس التنفيذي لشركة أدنوك: هناك نقص في مليار برميل على مستوى العالم بسبب إغلاق مضيق هرمز.</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/75216" target="_blank">📅 15:54 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75215">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🇱🇧
حزب الله:
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ 10-05-2026 منزل يتموضع فيه جنود جيش العدو الإسرائيلي في بلدة طير حرفا جنوبيّ لبنان بمحلّقة انقضاضيّة.</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/75215" target="_blank">📅 15:31 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75214">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🏴‍☠️
اعلام العدو: الجيش الإسرائيلي لا يزال يحقق من أين بالضبط أُطلق الطائرة المسيّرة. "من الشرق" - قد تكون اليمن، إيران، أو العراق.</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/75214" target="_blank">📅 14:33 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75213">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنايا - NAYA</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Audio</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/naya_foriraq/75213" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">وما اعرفه عن العراقيين وعن فصائل المقاومة العراقية</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/75213" target="_blank">📅 14:22 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75212">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">هجوم من الشرق يتعرض له الكيان</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/75212" target="_blank">📅 14:21 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75211">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">المتحدث باسم جيش العدو: اعترضنا طائرة بدون طيار أُطلقت من جهة الشرق.</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/75211" target="_blank">📅 14:19 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75210">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/519ac44ef2.mp4?token=q4ODvPKzrnV4WlFkV9MYLmxRrFhjhW6eOgMiVSaQHp4ilPejr2a-dJWCcaBINXULjedsPZI2m20Ztjc0FIKw9b14Lyz_FZp0Rx96ZlWtuQ2etYDB4gSDULvNV6ZG4K5bYVGzmKbbKrLTHaL_4MuLh6n4X-KxMneCe6SSBI8ibGORSoHQeUq9eqmxHZ5l7UyuL4ueeOnH1f2Mw0X1lziucq8oP72KejwzwgExkjxHtATi49xpkk4pXWpvtW5JucHnbxVh18OB1CBjHCE1v5Dk6qnAsnUlDTsUaRfSnfHtQAr2imtqjD_FDGYm85ZBtiSXDWAZn4Z2iTYMKf3JbGVSsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/519ac44ef2.mp4?token=q4ODvPKzrnV4WlFkV9MYLmxRrFhjhW6eOgMiVSaQHp4ilPejr2a-dJWCcaBINXULjedsPZI2m20Ztjc0FIKw9b14Lyz_FZp0Rx96ZlWtuQ2etYDB4gSDULvNV6ZG4K5bYVGzmKbbKrLTHaL_4MuLh6n4X-KxMneCe6SSBI8ibGORSoHQeUq9eqmxHZ5l7UyuL4ueeOnH1f2Mw0X1lziucq8oP72KejwzwgExkjxHtATi49xpkk4pXWpvtW5JucHnbxVh18OB1CBjHCE1v5Dk6qnAsnUlDTsUaRfSnfHtQAr2imtqjD_FDGYm85ZBtiSXDWAZn4Z2iTYMKf3JbGVSsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">المتحدث باسم جيش العدو: اعترضنا طائرة بدون طيار أُطلقت من جهة الشرق.</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/75210" target="_blank">📅 14:19 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75209">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">رغم التأكيد في بيان سابق
الاعلام الامني العراقي: لم يحدث إنزال جوي ولا صحة لوجود قاعدة في صحراء النخيب</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/75209" target="_blank">📅 14:15 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75208">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">بلومبرج: ‏تطلب قطر من السفن في منشأتها الرئيسية لتصدير الغاز الطبيعي المسال إيقاف تشغيل أجهزة الإرسال والاستقبال الخاصة بها.</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/75208" target="_blank">📅 12:28 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75207">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🌟
الأمين العام لحزب الله: لا علاقة لأحد خارج لبنان بالسلاح والمقاومة وتنظيم شؤون الدولة اللبنانية الداخلية</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/75207" target="_blank">📅 12:14 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75205">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">بي بي سي: تجري الولايات المتحدة مفاوضات منتظمة وسرية مع الدنمارك لفتح ثلاث قواعد عسكرية جديدة في جنوب جرينلاند.</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/naya_foriraq/75205" target="_blank">📅 11:19 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75204">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M44mcaFbLyyJogyWTZYt3t83jl_10A7_mhykQf8HtUetOk_OwwQ4n4oFQqT6HLOnMbow034Zi9OqQhmcpH-aQnxhBVyuHeRz_akcfZP88BgfsiUQjzFLN8e3XVoSmjiYQ5lw61vkiwN5CwVEmcHQmm1_fTJOshG5YgSdzZbtg4wimIk_8GlnhfqMGVJShdwCT_P0Eo4wwunW2OD8keCIl-WPOVdrXw4byAJaB11qlrKSOPaCJkLgfQUUUFSvifz3qd8phl3nmcbNRE1l1qS5UVtX-xNT08RBt1dSR81ZdVSHv4f2UqLVgsLZtAOnRDqEnbwGEM1W7zAYj282GmPeNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📈
النفط يلامس 106 دولار للبرميل الواحد.</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/naya_foriraq/75204" target="_blank">📅 10:31 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75203">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🇮🇶
وزارة التربية العراقية:
دعم الطلبة بإضافة خمس درجات لتلاميذ الصف الخامس الابتدائي وطلبة المراحل المتوسطة والإعدادية للصفوف غير المنتهية، بما فيها الإعداديات المهنية بفروعها كافة
إتاحة فرصة أداء امتحانات الدور الثاني لتلاميذ الصفوف الأربعة الأولى من المرحلة الابتدائية المنتظمين بالدوام (حصراً) والذين رسبوا في امتحانات الدور الأول، بغض النظر عن عدد المواد الدراسية التي لم يحققوا فيها النجاح.</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/naya_foriraq/75203" target="_blank">📅 10:27 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75202">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🇮🇷
المتحدث باسم لجنة الأمن القومي في البرلمان: أحد خيارات إيران إذا وقع عدوان تخصيب اليورانيوم بنسبة 90%</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/naya_foriraq/75202" target="_blank">📅 10:20 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75201">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🏴‍☠️
جيش الاحتلال: إصابة 8 مقاتلين من لواء غولاني في 3 اشتباكات قرب النهر على أطراف زوطر الشرقية جنوب لبنان</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/naya_foriraq/75201" target="_blank">📅 10:05 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75200">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🇵🇰
الشرطة الباكستانية: مقتل 7 أشخاص بانفجار في سوق شمال غربي البلاد</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/naya_foriraq/75200" target="_blank">📅 09:49 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75199">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🇱🇧
🇮🇶
لبنان يعفي العراقيين من التبعات المالية والقانونية المترتبة بذمتهم عن تجاوز فترات إقامتهم داخل لبنان خلال السنوات السابقة ولغاية 31/12/2026 وإلغاء إشارات المنع من دخول لبنان على كافة العراقيين المغادرين إلى العراق ليتمكنوا من زيارة لبنان مستقبلاً دون مشاكل.</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/naya_foriraq/75199" target="_blank">📅 08:47 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75198">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CeD23vszxHkPJf8oxD3mzjPjcQkT3lUTSA3CcWOOM9sXqCgqMMZ9JXqauD7NsBdoKrUng1loloMIaIplCBw5C1KkVTnt2WAUPSg__Hklz-3XNQpLkaVGgBB8TOaiV_LfUBizYMFWyGpm31Q6_GYrRKsmX7gW4_GIOWzNACywdwmVy0eTWYXyrJXhKgobwLd4z1sjs0-iYUdZ-b-0aoOCXRSLjbSfhJlchLnDdrBjBqDch4IhDzJZYETiHFnNQEJugThMnlSXFxmcvMGtEC51h0cTcvCeqeO2akr1NBSFz91js4MbP4Gp3B5Zti9vuacabNy5MbADM574gfJRF9uJaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد تباطؤ الاتفاق الإيراني الأميركي، أسعار النفط تقفز إلى 105 دولارات للبرميل.</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/naya_foriraq/75198" target="_blank">📅 01:33 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75197">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C2khlz01f__oxZqaBG1lVzVb2Us-GP3XQ6trIxHV2qQ92kVrnrSBtKwyrcUPFngf6tNaHRt7KVda9cQpwFZmxIxfHA5z2_DRmyBE4QkS3Cht4QcsLkSqyTOs6vI8gg9m8PFy4dNXFQ3VPV2DsO5pCzUf9OZpTd7jFCccUa9oHF4goJO7p9XnIFwhYPK26NfZFh7ZuVQKzHZ41DaRxBNiwzcYO_gUVYRl4FPSTFAyvBQVHjDodmk6-gejdNK_gXr0qxN15F7K0oZ7H0nPZrnaE_6HwiDpmohgTxdSyzsF2O9G2DBIbzqmKYZx7rBi43oc0PHo2jmdyfDka8AX1Acwtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامب : اني حيل فرحان بزيارتي للصين ، الصين بلد يشك شك وبي خوش قائد</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/naya_foriraq/75197" target="_blank">📅 01:30 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75196">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31c76991be.mp4?token=JSKe8V_rXJsRCfSTNy0H-5ZJiGMtDFzMdv-d1gV954RB1SwfaAYJcBXD1jDDX-u4GBQvs2mQPHB5qIl4ozTxIHSDq6fw4etuS27ESBACCBTZnzVfbsJlSPQIep_fnWzmXEfoKJgJS4HpedpOMrzfKK13eSVY2dUhc7C6oKJTIyghbrwQepnMjulFdXJ-FIOKYY70bWeccV2TnFZgWUqxvkDR9FApRdxF0WbhGI8x_o3l9OrYN0zb_G2Rwj00033H__mASdQgIAu1jsrlmx6wm7RZY5pb_Y6TSA_NTYMxFaTuoVFNstGN9dEuN0EcpmwHeFGAnRqArOKt09hmU9mwgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31c76991be.mp4?token=JSKe8V_rXJsRCfSTNy0H-5ZJiGMtDFzMdv-d1gV954RB1SwfaAYJcBXD1jDDX-u4GBQvs2mQPHB5qIl4ozTxIHSDq6fw4etuS27ESBACCBTZnzVfbsJlSPQIep_fnWzmXEfoKJgJS4HpedpOMrzfKK13eSVY2dUhc7C6oKJTIyghbrwQepnMjulFdXJ-FIOKYY70bWeccV2TnFZgWUqxvkDR9FApRdxF0WbhGI8x_o3l9OrYN0zb_G2Rwj00033H__mASdQgIAu1jsrlmx6wm7RZY5pb_Y6TSA_NTYMxFaTuoVFNstGN9dEuN0EcpmwHeFGAnRqArOKt09hmU9mwgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴‍☠️
🇮🇶
من تل ابيب الى الانبار   تمارس القيادة المركزية الوسطى الامريكية التي يعد جيش الكيان جزء منها ؛ عمليات استطلاع مركزة على مدى ٢٤ ساعة و على مناطق الأمن القومي الصهيوني خط امتداد ، النخيب ، الرزازة ، الخالدية ، الكيلو ١٠٦ ، خط ال H 3 ،  ومناطق الطاش ،…</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/naya_foriraq/75196" target="_blank">📅 01:19 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75195">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">وزارة الخارجية الإماراتية: دويلة الإمارات تؤكد أن حادث اختطاف ناقلة النفط قبالة السواحل اليمنية يمثل تهديدا مباشرا لأمن الملاحة البحرية</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/naya_foriraq/75195" target="_blank">📅 01:10 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75194">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iCb9EXs9YI6A_nlJOwu2Q5ujXWP5heGg-1gc4kgb5OYnv_H2N4-_ct00Z959OIRwgbuQ2G2SYZ2ba1rJT4y95iLiy4T_GKKytLKTbCBf_nSRHPJwhhWll5hl2ofBMmdKLcrRFusVn9mazQjQ3p0p90RWDTlvmGdFP21KXuCMggPJvX-4rzLnnyjf_Peb2h_BN32jkOGxJZLOrpc2VKdyzzVcoHdvrWI3hwPG9PdXNX21Ltw6ZkWXsK4_IcbGvTi-ZGxE9uqinUuJs3jC5xEQGbQG-UoEJ_JrRU3fKPCXcly7vd8luCCXDiSWjeaE9CC1-GszhvFXCBDv5lZ5naj1Vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴‍☠️
🇮🇶
من تل ابيب الى الانبار
تمارس القيادة المركزية الوسطى الامريكية التي يعد جيش الكيان جزء منها ؛ عمليات استطلاع مركزة على مدى ٢٤ ساعة و على مناطق الأمن القومي الصهيوني خط امتداد ، النخيب ، الرزازة ، الخالدية ، الكيلو ١٠٦ ، خط ال H 3 ،  ومناطق الطاش ، عين تمر ، وادي شنان .. الكيان يعتبر هذه المناطق مصادر خطر ستراتيجية كونها مناطق منصات إطلاق صدام السابقة نحو النقب ، مناطق ذات طابع ديني كونها جغرافية نهر الفرات " من النيل إلى الفرات ممر داوود " ، مناطق بعيدة ومفتوحة عن السكان ما يؤمن أمان نسبي امني لقاعدة إدارة عمليات متقدمة .</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/naya_foriraq/75194" target="_blank">📅 01:04 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75193">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qAM1W4dBovaHg_TxjGHJxsEGdbYDnyRpTuMrvF3X3kUk6BcLl4RLicalO4FQqGNY3uWicRUCDGYrEgVKIaLwXIpORW1GoNqcdQgwgHtm3EiO066WPbBsPPm_JAxnjKmS2wmhBDJWt3binntDYxU6LoD6t3r14Ob0Zvh_GXMQb5v7EbAivfn6gnShjk3zL_XFtRDZmL9_bozs47amw-4RFyo2pppRJAuyZQBxFFh908OS9aoSVBQVGWBRWL5QITZw0NblFQLiMVm-aUWtPsngqoQmmbh31K_PEW3FEVQIcJeY3ONr-KkM-JAaej3UuA4_xc8z69_R67-ADbhWW0mRDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
قاليباف:
لا بديل عن قبول حقوق الشعب الإيراني كما وردت في المقترح ذي النقاط الأربع عشرة. وأي نهج آخر سيكون بلا جدوى، ولن يُسفر إلا عن سلسلة من الإخفاقات. كلما طال أمد مماطلتهم، زادت الأعباء المالية على دافعي الضرائب الأمريكيين.</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/naya_foriraq/75193" target="_blank">📅 00:06 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75191">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cnwLboArLRBxDfYKYSS4uEjrsBdl6p_fNy94eML3jBmynXG6RPqwf5fGMD-FjLZlvmlWJuVa91QDVD20zMYqnSZL0tQ4pgVLNdxozMbrrTUDgTAlRPNe-eboQDIgm1zXIXwzj-l3uPUEmObnaranCUoIKCk8FJ9DsLHPJFuqtDuXl7gH7EQi1MBRS-WKyDtUnlC66t9YopRAgUp_3M5R2Y4u8GAGJgaqlzdFz_vUramDX3mtHiq2XBvUrCX7VMFHVaHGVSK2t1YsPSzCh8PLM9zEENFwSe3XaRLgmCfophdbwRUjTT5pEdV39YUtbtBBfBaLZznbHM3XPFQ0mJqCqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شعبنا العراقي العظيم
هل لديك معلومات عن الأشخاص الظاهرين في الصورة عناوينهم اسمائهم … مكافأة مادية في حالة معرفتك اي شخص ظاهر بالصورة راسلنا عبر البوت …</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/naya_foriraq/75191" target="_blank">📅 00:01 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75190">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">⭐️
وول ستريت جورنال:
قامت دولة الإمارات العربية المتحدة بشن ضربات عسكرية غير معلنة على إيران، بما في ذلك ضرب مصفاة نفطية في جزيرة لافان في أوائل أبريل - تقريبًا في الوقت الذي أعلن فيه ترامب وقف إطلاق النار.
أدى الهجوم إلى اندلاع حريق كبير وأدى إلى إيقاف تشغيل المصفاة لعدة أشهر. ردت إيران بضربات صاروخية وبدون طيار ضد الإمارات العربية المتحدة والكويت.</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/naya_foriraq/75190" target="_blank">📅 23:54 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75189">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">طيران مسير من لبنان يخترق مستوطنة مجدل شمس في الجولان الشمالي المحتل وصافرات الرعب تدوي.</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/naya_foriraq/75189" target="_blank">📅 23:31 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75188">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0682c7b887.mp4?token=hasT0jlMowI5ILU6kq2YmfTA5Rs-816wjNfwd85hwKeLjvVvDlDwCjwAoXnT7duE9rkOWvlq7e3U59Nvgy1WcY9yyuNvzIPYloSXfBnivNmRYSLFYwDc3aD_DIE6H7C06dFFgh2yo9D6m249Rj7IH5GSptJ_vU6OlUifiJ1fuO69Rtsm9_hWuYe7m767L6zKlgg7YxeJpr6JWdZYyahZsYQaB6MRqf4pQKJkI355eucROq2o4dbCYCWOLAvO58wEgN4WY4k8qJy1gxlJ-Ch-qu87VRz8YPh0_nO2IW0gA_Nrv7Nyq_mYl91VxC10AcJrfN6FNj_APpkmBSgEOScWTAjbHJhWoE5EQfl6pfuRksKEo8-_dTI5Zzh9-jz7mViIYeJSH1R5LXG5GwlpMQYCn8zo9_oPWuHquktjr3SMtz-rMk9iNqvk0O-QHFVM87D8k0Cea3Sc-cwD0uegVJXspysPUExcBV29q4_wO3bV2XPmLGubIakbSD5EZa_pZsv_Ez7g8v0goQUPYhshY30yvqm9ZXy-9vfNDmSPRdzGjFQQUdQqCylyB2SF7lOQWz-JOF2eJZ6jijuSWx9wLhz58O6micr0fKiR7GW-6jCQs9jRhERdH-_tDLQXBOqiBaAa6VdhlKO3X805EP9R5e5U8trZ5eu-tIY9kAu1xd3wIek" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0682c7b887.mp4?token=hasT0jlMowI5ILU6kq2YmfTA5Rs-816wjNfwd85hwKeLjvVvDlDwCjwAoXnT7duE9rkOWvlq7e3U59Nvgy1WcY9yyuNvzIPYloSXfBnivNmRYSLFYwDc3aD_DIE6H7C06dFFgh2yo9D6m249Rj7IH5GSptJ_vU6OlUifiJ1fuO69Rtsm9_hWuYe7m767L6zKlgg7YxeJpr6JWdZYyahZsYQaB6MRqf4pQKJkI355eucROq2o4dbCYCWOLAvO58wEgN4WY4k8qJy1gxlJ-Ch-qu87VRz8YPh0_nO2IW0gA_Nrv7Nyq_mYl91VxC10AcJrfN6FNj_APpkmBSgEOScWTAjbHJhWoE5EQfl6pfuRksKEo8-_dTI5Zzh9-jz7mViIYeJSH1R5LXG5GwlpMQYCn8zo9_oPWuHquktjr3SMtz-rMk9iNqvk0O-QHFVM87D8k0Cea3Sc-cwD0uegVJXspysPUExcBV29q4_wO3bV2XPmLGubIakbSD5EZa_pZsv_Ez7g8v0goQUPYhshY30yvqm9ZXy-9vfNDmSPRdzGjFQQUdQqCylyB2SF7lOQWz-JOF2eJZ6jijuSWx9wLhz58O6micr0fKiR7GW-6jCQs9jRhERdH-_tDLQXBOqiBaAa6VdhlKO3X805EP9R5e5U8trZ5eu-tIY9kAu1xd3wIek" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
🏴‍☠️
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ
03-05-2026
تجمّعًا لآليات وجنود جيش العدو الإسرائيلي في بلدة البيّاضة جنوبي لبنان بصليةٍ صاروخيّة.</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/75188" target="_blank">📅 23:25 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75187">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🇮🇶
قيادة العمليات المشتركة:
لا وجود لأي قواعد أو قوات غير مصرح بها على الأراضي العراقية وتحديداً في صحراء كربلاء شرق النخيب والنجف.</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/75187" target="_blank">📅 23:11 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75186">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/271439eb30.mp4?token=gP5PPDgZb4V0sgkbAnQa7sAhhhnMLRmASnSJ0OBXhbEeNl1PlYZc3PTTSsJJTnVTM-fwDFsfLpVS3ufW2RwmCFplfS5WIG41kR2GgVWfvzM2k15xhqXs44ZxY1OIPydaPsle02sFAihtgeu1DW-xwMxwecpowh6AVS7AGMX_FS8Er0fQgTCQreovuMgNIRkC969t3EadxnWOpVEaY5Vxo_EWBIbvRYZRjx1YaidC7qLPvIyBIrGHvlDRESRMQe76fgwlKMmEyuiTCk9wgAl4pgycscLCs5cwTmT8Y9i4SKZ-S8-ifxyvK4EtEm4uM2rYzpL06UQG_6qi7Jn28_XvIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/271439eb30.mp4?token=gP5PPDgZb4V0sgkbAnQa7sAhhhnMLRmASnSJ0OBXhbEeNl1PlYZc3PTTSsJJTnVTM-fwDFsfLpVS3ufW2RwmCFplfS5WIG41kR2GgVWfvzM2k15xhqXs44ZxY1OIPydaPsle02sFAihtgeu1DW-xwMxwecpowh6AVS7AGMX_FS8Er0fQgTCQreovuMgNIRkC969t3EadxnWOpVEaY5Vxo_EWBIbvRYZRjx1YaidC7qLPvIyBIrGHvlDRESRMQe76fgwlKMmEyuiTCk9wgAl4pgycscLCs5cwTmT8Y9i4SKZ-S8-ifxyvK4EtEm4uM2rYzpL06UQG_6qi7Jn28_XvIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇸
"لامين يامال" يرفع علم فلسطين خلال احتفالات نادي برشلونة بالدوري الإسباني.</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/75186" target="_blank">📅 22:45 · 21 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
