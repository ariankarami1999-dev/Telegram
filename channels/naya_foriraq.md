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
<img src="https://cdn4.telesco.pe/file/YA7iM2qOnU-2eGdwMyjWK_4nIuiQYwK001xAQm0ZIRHtXdkO6oUv_qt2EhNRkiOMekuPqPJu5jFYNbYwNfuBhTHeOYXpYua263Fshp9bd1AULwLhZVHIuu-mlJF0vfDebVixZ5h0tQdka_TM5Z5HQM-jOKo7oem7p8_a2QtpjfZXhjLaEuBav9DhvmUr6Ovep2prKPxq9xn65J33ZU-w41bN5EZ3VdCKYCt32G9UBUmJ1mKUneRshvBAC6243iIY_KNSapY4wAt5gXg_0_qP69SatqktAvVPaewHUeNm69lJ0FjzxfUT9TJmWQ_0TKkcbK7ur6fXKiecl4Jw5mommQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 273K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-21 08:54:13</div>
<hr>

<div class="tg-post" id="msg-87601">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">‏بيانات ملاحية: تراجع حركة الملاحة في مضيق هرمز إلى أدنى مستوى لها هذا الأسبوع</div>
<div class="tg-footer">👁️ 224 · <a href="https://t.me/naya_foriraq/87601" target="_blank">📅 08:52 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87598">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb4c8ae875.mp4?token=RE6fpl8-WYB9krfXqtYxgKG54WIZUrUhaX_FVFthcV15SnqHlp6jrwMjtWFnfw-V2Nd75YyfRYVfZrVQUGEJSwB7H4E3PtStOyhY9891o3UA5GORvkm2s3n9_grLDBBS5ddTDOUiPGXS0u05_8e6Ra-1pBjyng0sKmN2DbQWCkXte8WXFNVB6-1zyQhdEoRXo0HQXP49RFT1_VbYe8E5MlkAia6OWGiBBCFGIbr0PYZCCvF3tCJMuuEWzp0TOdlvrd9uISfquO-pnpTX93EtcgShr392n174xw5DthU2VXpiZKVhmbDjaO42-Jvj8F4ANy0g7K636O7poIVeh80g_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb4c8ae875.mp4?token=RE6fpl8-WYB9krfXqtYxgKG54WIZUrUhaX_FVFthcV15SnqHlp6jrwMjtWFnfw-V2Nd75YyfRYVfZrVQUGEJSwB7H4E3PtStOyhY9891o3UA5GORvkm2s3n9_grLDBBS5ddTDOUiPGXS0u05_8e6Ra-1pBjyng0sKmN2DbQWCkXte8WXFNVB6-1zyQhdEoRXo0HQXP49RFT1_VbYe8E5MlkAia6OWGiBBCFGIbr0PYZCCvF3tCJMuuEWzp0TOdlvrd9uISfquO-pnpTX93EtcgShr392n174xw5DthU2VXpiZKVhmbDjaO42-Jvj8F4ANy0g7K636O7poIVeh80g_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
بالطائرات المسيرة الإنتحارية.. إستهداف مقر تابع للإنفصاليين الأكراد في محافظة أربيل شمالي العراق.</div>
<div class="tg-footer">👁️ 6.56K · <a href="https://t.me/naya_foriraq/87598" target="_blank">📅 05:52 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87597">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/387a0d0bf3.mp4?token=tcr_Fj-2cnCJH22qu4Jj1L5WRLkUi6tmltTB5vLe7FREsqBB9ANMVaR4CtQv9_d9Hr0ttnwIy_0tECT5IAtWGeQ0jKr5BigeNZ98lkWSfqgFloOJYapvqFJeC7fOufL4yhxLKhnRVq5lnPCkYvih_hFhP9_Ky9Dvu9vT6i8qPi-Ry5WbM2EaL93IgYrm3dPZmoXWhZLBfqBmYa8TS8O0IDr-8tAQfLpG8fJuCrQesyXVxcBX3zIbuArhDx7GgmsadcLziVO3wZQoauRu1KO_HCKWChWadDPpk0GjALryV1csCGodl4SDkTreqllFSLFuj2DJvA9CTMUzsHd5zphJ2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/387a0d0bf3.mp4?token=tcr_Fj-2cnCJH22qu4Jj1L5WRLkUi6tmltTB5vLe7FREsqBB9ANMVaR4CtQv9_d9Hr0ttnwIy_0tECT5IAtWGeQ0jKr5BigeNZ98lkWSfqgFloOJYapvqFJeC7fOufL4yhxLKhnRVq5lnPCkYvih_hFhP9_Ky9Dvu9vT6i8qPi-Ry5WbM2EaL93IgYrm3dPZmoXWhZLBfqBmYa8TS8O0IDr-8tAQfLpG8fJuCrQesyXVxcBX3zIbuArhDx7GgmsadcLziVO3wZQoauRu1KO_HCKWChWadDPpk0GjALryV1csCGodl4SDkTreqllFSLFuj2DJvA9CTMUzsHd5zphJ2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
بالطائرات المسيرة الإنتحارية..
إستهداف مقر تابع للإنفصاليين الأكراد في محافظة أربيل شمالي العراق.</div>
<div class="tg-footer">👁️ 6.97K · <a href="https://t.me/naya_foriraq/87597" target="_blank">📅 05:39 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87596">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🇺🇸
ترامب حول تغيير الطائرة في أنقرة: الأمر متروك فقط لخدمة المخابرات السرية. أنا فقط أتبع ما يرغبون في القيام به. لذلك، أتبع تعليمات خدمة المخابرات السرية والجيش.  لقد طلبوا مني السفر على متن طائرة مختلفة، ولكنها توفر نفس مستوى الأمان، ولكنهم أرادوا مني فعل…</div>
<div class="tg-footer">👁️ 7.78K · <a href="https://t.me/naya_foriraq/87596" target="_blank">📅 04:58 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87595">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5aec64b6d.mp4?token=ha49lu47kLtg6skClMqDsvMEYWntNVad4tiPQ4EmK_uk3O04LQi6YrmF8wMGuVBdcbEASJhcV0Ib67TcQeOsqEohDjdabh6WVLpBMrUwvEpOY7W8PIxzEkQLYfEjvW6xFcR0SaOVDbTNRaeVy06XS4uBX606qoM5-wjMmZAOsIo8JB6ToKrTpkeKCT95tqROhhKjQaX_KTWlN54nivBnl1X75aQNBXsksm-U0a5maAWDhuYI_-p11krktV_Spv18TmPd06iH1gwZGuWDxd6Su8HbeZfaQIBmc97gMr7gM7EHBEP2h0VY9H___uF82MX7WZBUiddZnFl-buMGdwDm8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5aec64b6d.mp4?token=ha49lu47kLtg6skClMqDsvMEYWntNVad4tiPQ4EmK_uk3O04LQi6YrmF8wMGuVBdcbEASJhcV0Ib67TcQeOsqEohDjdabh6WVLpBMrUwvEpOY7W8PIxzEkQLYfEjvW6xFcR0SaOVDbTNRaeVy06XS4uBX606qoM5-wjMmZAOsIo8JB6ToKrTpkeKCT95tqROhhKjQaX_KTWlN54nivBnl1X75aQNBXsksm-U0a5maAWDhuYI_-p11krktV_Spv18TmPd06iH1gwZGuWDxd6Su8HbeZfaQIBmc97gMr7gM7EHBEP2h0VY9H___uF82MX7WZBUiddZnFl-buMGdwDm8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامب حول تغيير الطائرة في أنقرة: الأمر متروك فقط لخدمة المخابرات السرية. أنا فقط أتبع ما يرغبون في القيام به. لذلك، أتبع تعليمات خدمة المخابرات السرية والجيش.  لقد طلبوا مني السفر على متن طائرة مختلفة، ولكنها توفر نفس مستوى الأمان، ولكنهم أرادوا مني فعل…</div>
<div class="tg-footer">👁️ 8.55K · <a href="https://t.me/naya_foriraq/87595" target="_blank">📅 04:43 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87594">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1995c12d41.mp4?token=e8OjsFGt1WrVuVvNuyPCL8n_PZdHvulF18gNMAZwz56Uc5Ta8nDe_-KdGwEWQZsCEVPF68tqyqqiVHRWX9dDhMMeEmJCri-TfJfdu0FNwXebghXisfdVKpZEMSroe2l5UTqAnggrzJgJlUh8YORVMmDht4TyXI0YgY0580IN3eFxffhvoE1kf-LPO6VEZjV6tvjGLodL0UXF_dSA1RAPWgrKDjxCS-kBW88UXS6ECoOW97tVYHOVhlClYSPu63y7Y9kpeIMvb4UIu_PFks-trWGkJdiRWOEipBCFlwxJZUqtm5XcTJDwvg3Pwgad7ajZhcHki2qcZipOezuspWC8TQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1995c12d41.mp4?token=e8OjsFGt1WrVuVvNuyPCL8n_PZdHvulF18gNMAZwz56Uc5Ta8nDe_-KdGwEWQZsCEVPF68tqyqqiVHRWX9dDhMMeEmJCri-TfJfdu0FNwXebghXisfdVKpZEMSroe2l5UTqAnggrzJgJlUh8YORVMmDht4TyXI0YgY0580IN3eFxffhvoE1kf-LPO6VEZjV6tvjGLodL0UXF_dSA1RAPWgrKDjxCS-kBW88UXS6ECoOW97tVYHOVhlClYSPu63y7Y9kpeIMvb4UIu_PFks-trWGkJdiRWOEipBCFlwxJZUqtm5XcTJDwvg3Pwgad7ajZhcHki2qcZipOezuspWC8TQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامب:  انا لا أثق بإيران ونحن نسيطر على مضيق هرمز.  إيران كذبت في العديد من المرات وأنا آخر شخص أثق بهم.  ‏إيران لن تصبح المتنمر في الشرق الأوسط.  إيران قد تتخذ إجراء بشأن مضيق هرمز وتتعرض لضربة قوية لكننا في موقف جيد للغاية.</div>
<div class="tg-footer">👁️ 8.89K · <a href="https://t.me/naya_foriraq/87594" target="_blank">📅 04:32 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87593">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d9de36f951.mp4?token=ODN2b4G4GibvpaHZ5BIkVSmhmNqVtM6sNYmC4eJVHBjHL9T6rh5pBhcOhJsk-LcjRjM_Bx10rxERTTIQ9_BzKMJXLs80a7-NRZd7BALtuchoDXIIK9pqjHcn5FLaQufTTA-kywEkibn7xsRdkQ1-NPMZiS1ATMgXkONinYz56mff1Vrk-OQWvKfjYA3CurtQPaBUJx7zNAiARJsnE93jEHPrqpv5l2aP8uVzg2ErKKL_xy6dDrA-5V4sW_G-4p4RtqhcPQrVZpxMkmHIxW8kdOGDo8hb4looXG4LYUmt7WWYCZ53dT2_O-zosfUbOKZ-U3ZAsb0YbYY_sp3oVVRlsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d9de36f951.mp4?token=ODN2b4G4GibvpaHZ5BIkVSmhmNqVtM6sNYmC4eJVHBjHL9T6rh5pBhcOhJsk-LcjRjM_Bx10rxERTTIQ9_BzKMJXLs80a7-NRZd7BALtuchoDXIIK9pqjHcn5FLaQufTTA-kywEkibn7xsRdkQ1-NPMZiS1ATMgXkONinYz56mff1Vrk-OQWvKfjYA3CurtQPaBUJx7zNAiARJsnE93jEHPrqpv5l2aP8uVzg2ErKKL_xy6dDrA-5V4sW_G-4p4RtqhcPQrVZpxMkmHIxW8kdOGDo8hb4looXG4LYUmt7WWYCZ53dT2_O-zosfUbOKZ-U3ZAsb0YbYY_sp3oVVRlsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامب:
انا لا أثق بإيران ونحن نسيطر على مضيق هرمز.
إيران كذبت في العديد من المرات وأنا آخر شخص أثق بهم.
‏إيران لن تصبح المتنمر في الشرق الأوسط.
إيران قد تتخذ إجراء بشأن مضيق هرمز وتتعرض لضربة قوية لكننا في موقف جيد للغاية.</div>
<div class="tg-footer">👁️ 8.35K · <a href="https://t.me/naya_foriraq/87593" target="_blank">📅 04:31 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87592">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0b4cce9c8.mp4?token=TamIVm-zpy7YbX0luR_mFiXK2Jxqgvkqu3zejGbsRX4ceqncWB23dVLot4wr_knPWJp19Jr6XRdwqSc47Q-MPPMYOxMuveI46xC0sFTvMSF_895JIyeTRUKZNR6AzG90AlkiTn20DeA1gemDN7DrMMcztZ1UrbbToMX9NZiqOKmIcKLKdoogDipsm8yLJr12RQD9V-YDVOyca-4xuJgmxqU8c_2ypKTG9FByy1cc82SRk2UZE0mqoWzsj4TU_MCXo9eIfyX5lOJlwVlMlWlNMJrEF2lCW6M7IRIHkc9NQe5kAk3ENhyBtMhyOOXX0DDIMO6RwoYUdls1BYAKud7U37pV4zRQBUqdRA3G-oPdb_cK8nGhu2Ay37MMaXAbPg_QjcWmVrMqqDa5psYsR6DsQDmuugvqL9pWxHvB2W2aOw1SKH-XY4SAGopcS1HsDfVVS71XbdCgIivlR4m37CgTHDtxBDqw2IWjkZzcubrmGsXnpPIocCiFtyNJxmB-z05NfcMZkVzqEoRfmAVOZ3UVQLvh81l6CeX_IuOjwfz9FtQJy7tQ8hC1LxTUVkWBkxq9zzcamdYC_WvHdQjZasjPIsO_6l6R9hEoePFJSgSzwoB4Ptb0_oOJCj30uhCP2s-5-AW9P4j4ddFUnKD-nwnFfSBRXzh0H1Fn0boNqTANdkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0b4cce9c8.mp4?token=TamIVm-zpy7YbX0luR_mFiXK2Jxqgvkqu3zejGbsRX4ceqncWB23dVLot4wr_knPWJp19Jr6XRdwqSc47Q-MPPMYOxMuveI46xC0sFTvMSF_895JIyeTRUKZNR6AzG90AlkiTn20DeA1gemDN7DrMMcztZ1UrbbToMX9NZiqOKmIcKLKdoogDipsm8yLJr12RQD9V-YDVOyca-4xuJgmxqU8c_2ypKTG9FByy1cc82SRk2UZE0mqoWzsj4TU_MCXo9eIfyX5lOJlwVlMlWlNMJrEF2lCW6M7IRIHkc9NQe5kAk3ENhyBtMhyOOXX0DDIMO6RwoYUdls1BYAKud7U37pV4zRQBUqdRA3G-oPdb_cK8nGhu2Ay37MMaXAbPg_QjcWmVrMqqDa5psYsR6DsQDmuugvqL9pWxHvB2W2aOw1SKH-XY4SAGopcS1HsDfVVS71XbdCgIivlR4m37CgTHDtxBDqw2IWjkZzcubrmGsXnpPIocCiFtyNJxmB-z05NfcMZkVzqEoRfmAVOZ3UVQLvh81l6CeX_IuOjwfz9FtQJy7tQ8hC1LxTUVkWBkxq9zzcamdYC_WvHdQjZasjPIsO_6l6R9hEoePFJSgSzwoB4Ptb0_oOJCj30uhCP2s-5-AW9P4j4ddFUnKD-nwnFfSBRXzh0H1Fn0boNqTANdkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ضربات متتالية تطال مصفاة الزاوية في ليبيا.</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/naya_foriraq/87592" target="_blank">📅 03:44 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87591">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🇮🇱
جيش الإحتلال الإسرائيلي:
أُطلق صاروخ اعتراضي نحو هدف تم تحديده لاحقًا على أنه نيران من قواتنا في المنطقة الأمنية جنوب لبنان.</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/87591" target="_blank">📅 02:01 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87590">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da38748ac5.mp4?token=L1mgnRY2IoLs__sugu_n_Ff1F0uO6GLMoojTGJH-CKpCvKR8PqU-192Scxz5IzkmDbtzcq7YdQiuzSjwfaPDlOgJ49NUK1ozNEGLwsp4Nj2QeQ8fsXGBzUmDdRI2YLt-F_voIKNMY64YNYOhKpRDbUIcetblHKU2pXPcHdFlAQ7fPx8W3SHMQggxOPwWZoIVixPFFR81IHBSohdy_ocY7I4Fksv_17ber7lRWagj44FtTO9ujTv8WFbja2lVTlpa9Sc2uLesPLeemEh1v1aB4I2Ep0_e8Q-QQ3qRHOg4_btD6xy2nUdoAl0HSROGgkYW109BUgezdQBwlnlTRg2GPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da38748ac5.mp4?token=L1mgnRY2IoLs__sugu_n_Ff1F0uO6GLMoojTGJH-CKpCvKR8PqU-192Scxz5IzkmDbtzcq7YdQiuzSjwfaPDlOgJ49NUK1ozNEGLwsp4Nj2QeQ8fsXGBzUmDdRI2YLt-F_voIKNMY64YNYOhKpRDbUIcetblHKU2pXPcHdFlAQ7fPx8W3SHMQggxOPwWZoIVixPFFR81IHBSohdy_ocY7I4Fksv_17ber7lRWagj44FtTO9ujTv8WFbja2lVTlpa9Sc2uLesPLeemEh1v1aB4I2Ep0_e8Q-QQ3qRHOg4_btD6xy2nUdoAl0HSROGgkYW109BUgezdQBwlnlTRg2GPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
مشاهد من مسافة قريبة للحريق الكبير الذي اندلع وسط محافظة أربيل شمالي العراق والأنباء تتحدث عن حادث إنقلاب صهريج محمل بالوقود ماأدى إلى إشتعال النيران فيه.</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/87590" target="_blank">📅 01:40 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87588">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/29c98ac4fb.mp4?token=aY7WIxH6ODoML2hhbQdEILRMs7x2DzpmOexTiazmoXkbgTkngUDLddEbo85CGMAJ23UwXjUpQ2EVIY3hw248WLo0UV3jGA39tqPAU5JwMup6sO932r6-oh_dJiUSTvHjlYY5P07Yaum4J8eBA2dlHmgoQnQRwleawn0jNYrTnVwGsaAqgW6hd9ObV6S5gzw5nunIeoNXXOj61amtUBv5kA9g6w1Y46WT7s_NojnaHBxkJWymAplK3YaLUtsyr7vSN97JkmTt9cK6-_Iy8qJTJ3_Mu0B3dRGGxqt-ZENYIJwVSN42CBXGP7vSVCo-C2TmHfVS8YopkaoGeZlaI5l3cA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/29c98ac4fb.mp4?token=aY7WIxH6ODoML2hhbQdEILRMs7x2DzpmOexTiazmoXkbgTkngUDLddEbo85CGMAJ23UwXjUpQ2EVIY3hw248WLo0UV3jGA39tqPAU5JwMup6sO932r6-oh_dJiUSTvHjlYY5P07Yaum4J8eBA2dlHmgoQnQRwleawn0jNYrTnVwGsaAqgW6hd9ObV6S5gzw5nunIeoNXXOj61amtUBv5kA9g6w1Y46WT7s_NojnaHBxkJWymAplK3YaLUtsyr7vSN97JkmTt9cK6-_Iy8qJTJ3_Mu0B3dRGGxqt-ZENYIJwVSN42CBXGP7vSVCo-C2TmHfVS8YopkaoGeZlaI5l3cA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">من الحريق الكبير في محافظة أربيل شمالي العراق.</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/87588" target="_blank">📅 01:37 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87587">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b9acaf5a0.mp4?token=iksy9hAxXr5_XCjNkH-0Hjv9f0rSit_087e3_WWIlr3Rt6dKuLys49TPBizOmNoWkwRDUHxoJeh8A6DJMz9GSdOl-lQXFvp9KDQxIt5pTb6dCosXe1oxJVZXqAnzNB6V1SzTWYmfn38bzlHONn_6hpxPx5ox5ZULpNOyOJ-HdozaCRgGKajyz59g28dV0VkOagjC_yePBRRwCJF4eDpafoq9NBIU0e-BiJyD7orHORvOPqrQ8bRoLIiW3vJs2cprLhPSICmgEv3_YdQ5y__Izc_0cfvJBSv6cvdr22pH9VYXyGQqvWcIxXfFaMfveTWevFrudgaQI2ptUp_Q0VCJfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b9acaf5a0.mp4?token=iksy9hAxXr5_XCjNkH-0Hjv9f0rSit_087e3_WWIlr3Rt6dKuLys49TPBizOmNoWkwRDUHxoJeh8A6DJMz9GSdOl-lQXFvp9KDQxIt5pTb6dCosXe1oxJVZXqAnzNB6V1SzTWYmfn38bzlHONn_6hpxPx5ox5ZULpNOyOJ-HdozaCRgGKajyz59g28dV0VkOagjC_yePBRRwCJF4eDpafoq9NBIU0e-BiJyD7orHORvOPqrQ8bRoLIiW3vJs2cprLhPSICmgEv3_YdQ5y__Izc_0cfvJBSv6cvdr22pH9VYXyGQqvWcIxXfFaMfveTWevFrudgaQI2ptUp_Q0VCJfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حريق ضخم جداً واعمدة دخان واسعة تغطي سماء محافظة أربيل شمالي العراق</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/87587" target="_blank">📅 01:33 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87586">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57fce359f9.mp4?token=sCK7N3JUxp43YenWhpKD5zuCAudDuwTPnwkBlVx1Z7I9S4UHdUsIEGBw0W6-2c1NJVwWqq9_aEUeVc6J5N3fLdTYRDCWFrS6ENIuv1AzsSEc3_Wd0AQwRPfMHRKoTow8pUFn0Nl_WATb31cO1ctk2gUcj5QUBDIcQPzFDztQ-zvhYBRKXw-VDzQZECGsewliheuZpmz7OpTaaj9F8HlZxCJQZwp3DiN4_lKB4h2XMaSGqtxk-S6i7fzxUL5Jh8Nu40EtYB4Lmk12FBbUARN6cciNOc2UMI1W-FgoJgiEFQWRaWw0Q6XLTxgyk_4LdbfOOOKx-3UA0gixWEY0UzK5gQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57fce359f9.mp4?token=sCK7N3JUxp43YenWhpKD5zuCAudDuwTPnwkBlVx1Z7I9S4UHdUsIEGBw0W6-2c1NJVwWqq9_aEUeVc6J5N3fLdTYRDCWFrS6ENIuv1AzsSEc3_Wd0AQwRPfMHRKoTow8pUFn0Nl_WATb31cO1ctk2gUcj5QUBDIcQPzFDztQ-zvhYBRKXw-VDzQZECGsewliheuZpmz7OpTaaj9F8HlZxCJQZwp3DiN4_lKB4h2XMaSGqtxk-S6i7fzxUL5Jh8Nu40EtYB4Lmk12FBbUARN6cciNOc2UMI1W-FgoJgiEFQWRaWw0Q6XLTxgyk_4LdbfOOOKx-3UA0gixWEY0UzK5gQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">إندلاع حريق كبير في محافظة أربيل شمالي العراق</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/87586" target="_blank">📅 01:32 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87585">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38bb20ca7d.mp4?token=p7GMHDTL_Wr_YHPHcx_P156vZNKIvZDWzyE0vIHUhCumAw6hbKG4D2U6Tp0mLkdreC1wULgaSLjwzrZt4axfIDpZNug9dAJJaum_vyCv_mqsrqaTHMHX2Pim40cXwIbBjXSbzmV23v2EVO-ekxFeq3yDsa1ycia_11YnGnMKrA-A8jAAv6XMGF32gCWjlqbUAgdimEhw8KUAyjTaXMcCQWzDM9JQgyQU_tC80PDHxG1CnXeF3RG5zMnxcdDk_Gx8yk5eoRwPZ3KZngIJYymDq01U_hnSaBylLKethQGgz1g-bGo134rTa6rBwanxAH5NKjyXPDZxvr8yZfVnW53oxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38bb20ca7d.mp4?token=p7GMHDTL_Wr_YHPHcx_P156vZNKIvZDWzyE0vIHUhCumAw6hbKG4D2U6Tp0mLkdreC1wULgaSLjwzrZt4axfIDpZNug9dAJJaum_vyCv_mqsrqaTHMHX2Pim40cXwIbBjXSbzmV23v2EVO-ekxFeq3yDsa1ycia_11YnGnMKrA-A8jAAv6XMGF32gCWjlqbUAgdimEhw8KUAyjTaXMcCQWzDM9JQgyQU_tC80PDHxG1CnXeF3RG5zMnxcdDk_Gx8yk5eoRwPZ3KZngIJYymDq01U_hnSaBylLKethQGgz1g-bGo134rTa6rBwanxAH5NKjyXPDZxvr8yZfVnW53oxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">إندلاع حريق كبير في محافظة أربيل شمالي العراق</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/87585" target="_blank">📅 01:29 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87584">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🔻
أصوات إنفجارات مجهولة في سماء منطقة السيدة زينب بالعاصمة السورية دمشق.</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/87584" target="_blank">📅 00:41 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87583">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iz0gr8YqBULh01Jr5Um8FT9ykVlThB6tcGXzcT5VPGx96sojplaFPRevZNA98P8gj1Dz4BNJ6O0XldX9H6nryPd1FgDsXjNLw68W3hCugR6L23u9Repw3KZN89DVO9wQ7fs0GB872KRiAKYZDyZudGpSOQbkRGM0ZIIgOYwfLhk3GTtQgkOUbVgTwNk5DcodmEJRSQSp5Hm1N6OWg3kGTRajsFbjddbgYG9_sjEKK0RE_PggK_ryNujkcfB2PHrFsT_tjVK9Blxy_MvDsRRhNE924v_nYFugWQl4AAUByQ6aR-VfBnWlblHHowjlBrpYpT7nktxwqigsWv55wDo6jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
🔻
الأدميرال علي عظمايي
قائد القوة البحرية للحرس الثوري؛ رجل الخطوط الأمامية في المواجهة مع الولايات المتحدة</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/87583" target="_blank">📅 23:26 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87582">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🇺🇸
الاعلام الاميركي منشغل بازمة الصواريخ الاميركية:
أطلقت القوات الأمريكية حوالي 50 صاروخًا من نوع "باتريوت" لاعتراض الصواريخ في يوم واحد، خلال الهجمات الإيرانية التي استهدفت القواعد في الأردن في الشهر الماضي. ويقدر التكلفة الإجمالية لهذه الصواريخ بحوالي 200 مليون دولار في يوم واحد، حيث تبلغ تكلفة كل صاروخ حوالي 4 ملايين دولار.
استخدمت إيران صواريخ ذات مسارات قابلة للتعديل لإجبار الولايات المتحدة على إنفاق مبالغ كبيرة وتقليل مخزونها المحدود من صواريخ "باتريوت".</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/naya_foriraq/87582" target="_blank">📅 23:26 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87581">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🇮🇶
في خبر مفرح للشعب العراقي
الأنواء الجوية:
انخفاض تدريجي بدرجات الحرارة بعد منتصف آب واندفاع كتلة هوائية معتدلة نحو العراق.</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/naya_foriraq/87581" target="_blank">📅 23:01 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87577">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LTnRY1vxCPuug2bvg1lj5PPhQSw2NWo9R1guqWfKHRu6q1rDb7kbT7lcaPRJMFapstK_6auAsO9o1y4j3-KGlwXA_eh8YcfkJ6BWEE0BOORySLmAp6uQNGEtVsuKanB5FY5_GZalQRk_azaWdf7Kg7VBvIlyjd13kUDv2LPcCOCMMpyo65vEfzFxPZB7Buz-2HHU0q9mFnH9V4PxKLJb09HzQ_qpEQ4-LRXXrZ1wcSpLIcQm6X6ABVTQfczoeBtDPB9EY0uAbnzXtbYq3a0ZnMEWuE_LpzSvwT6A-FsunCYhqQcJPycuPpgyr88o-qm_ggT4TGswovSg0-mmpapl9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D6g4_TiYqwczGv5HwhmkwU14Ez3DZDzz1ia1Oue5QxhsI7UytuSJsSkTDwo8lI0vPKuq2f7YnTOthmj82-Q0M-5PJISHPNl1ID6qvqGBTuN-O83XYp_t_9UoCwHOnxIUQSqD8Z7x-i5QR83VylCZiUAR9gPvUv_kL8z7Fj1ILATaQPj_AQxaugMx7w473wjyJBFzz2Bo4udGEd5MAaBZWsL2ruWpLpSbQmOadW1a2Xz1DRFQHKU6Sr9jFE5YoQv1T3G6WrzN3gjYxOMYi2x32_q6ZkhEShR3oMItBLPlEeSGZO4kEIb1aUnejW7ZhTO2Fi4dzXtGmeuK-4IRa10Axg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HXZbrC418TkfW19z7Hxo-3NXHKiCe3Id94QZhj0tYptALYEhCGFIBge0CEr26UfGrDkFDtq6RkYUoWr4AA9DljC65t773Pxqd6-VUmqL5NQJmhcNGcvYvEdnvspQGPqJSaYpDaE4cQkXg70eawRHeVX4JMNT-QZ88Yyl0UwrIjAJop8CQBIsweKaK9dmIXVgrvGh8HnsK8jEnlj0z4Gl5-LIEP9h9u0cDDGwx5Tm9XtLYlu1mkX-QZRaFHORX9gEjnY6l-Uw5JIi0T2V_UYMxm1ppRkIHOp4rer23_vtYTsW8pvi3I5gc4UZSI7Ep04l2n0JaHy_DGXMFbSNftKmwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sl_aTyoCsqGRHPZN0fxFQywIhXXpqEyoXFPt1_oE0os3FnDyKVEbTWudAMMIhM1Lf5NCFBs8Tyw2pbV957BRzpTay1RNBS7RTxqprPPxSrkwtYlinLNodDOWmArXGqv1uWOA8M09pNkjE8uS0I9cZ22YHsH0uo8RBxumHQckNB08j4XaEZzLultorDR7kjQ5QEoi3SzrtIEl_ORpxm_neojWyjMQlVBXC7MolL7pOOlo7uLiEZ0fmBc4YAspqGwxkJ9gWWzsG8j2MiVCc1U7PYqCnpPHYaU95mAdSwUyWXmVxzUrJKt-dXCKItacEiYQj0CFIdRniWUXAgVhAwHxYw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇾🇪
استهدفت القوات المسلحة اليمنية سفينة نقل معدات عسكرية سعودية في باب المندب.</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/naya_foriraq/87577" target="_blank">📅 22:56 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87576">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🇾🇪
المتحدث الرسمي للقوات المسلحة اليمنية
:
تمكنت القوات المسلحة اليمنية بعون الله من استهداف تحشيدات العدو السعودي ومخازن أسلحته ومقار قياداته في منطقة المخا و معسكر تداوين في محافظة مأرب وذلك بعدد كبير من الصواريخ الباليستية والطائرات المسيرة وكانت الإصابات دقيقة بفضل الله وخلفت عشرات القتلى والجرحى بينهم سعوديون.
إن القوات المسلحة ستواصل عملياتها في استهداف كافة التحشيدات السعودية التي تسعى من خلالها للتصعيد والسيطرة على بلدنا العزيز.
تجدد القوات المسلحة تحذيرها لكافة المخدوعين والمغرر بهم من أبناء بلدنا إلى مغادرة مربع العمالة والخيانة قبل فوات الأوان.</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/naya_foriraq/87576" target="_blank">📅 22:41 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87575">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🇮🇶
رئيس الوزراء العراقي يوجه بإعداد مشروع قانون لحصر السلاح بيد الدولة وفقاً للسياقات الدستورية.</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/naya_foriraq/87575" target="_blank">📅 21:28 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87574">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🇾🇪
استهدفت القوات المسلحة اليمنية سفينة نقل معدات عسكرية سعودية في باب المندب.</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/naya_foriraq/87574" target="_blank">📅 21:07 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87573">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🇾🇪
سماع دوي انفجارين متتاليين في مأرب.</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/naya_foriraq/87573" target="_blank">📅 20:43 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87572">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IBzbFSox23wVcquhHWEV6ZBmJwJOlmnDSAQfsGUS3aogP6gvrvCf5sC01cGxIOMb0ifjuMRBX54ubd7HkQPqVsPcYNpyeDwo9uQnpHACoB6FvaQh2RS8svCLa3pzhvANLxgeVZNDpdpTYi4Lek7v0mhRU5iXkJisr5_XSr54-MPTq_5dUxVOGSwbM5HiOUkSTfhlCYljlHAeIem9tVKs05nFu56rC7mbPzVl5oc33MLw8PeM3Vrf39__bhip7TULIR88VrUzfnNA3pAlqE3FxiCpgqEdGVsuhgMK5NH7h2pCyX9uaOWmNKCGh9DxooMgP9dbSuwJ5o0byuj7KJyjGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ضربات متتالية تطال مصفاة الزاوية في ليبيا.</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/naya_foriraq/87572" target="_blank">📅 20:04 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87571">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jvsyUz0jvfSkDj9oiFqqtpQg9-BVbjCNF-BYTI5skX3SQYDV4CVSr_xTYfw7F44Px3Mj8zhxuQ1XMoH7JJD2jBz5mA4TBljO3lLuOSUFD0eYtA2Vc-ZP4pXBElfQYOg4NbxiJC7pkoblwhUg8WKawZVKffy6E8jXFOrDaKSdQXmp6kndrQvPvMaaU_DHaLUQi_pq3mRVly3ySxhJZ5H9LFG0Ra8SRdOIySJsEBJTJHC9gWoBB6-9gIJ67aRizXbBCxFdbOQDmAr4a6HL-awftI1Njz8l_Uss10Hd-C9EBH27L-t_p9YqRE3OguQUp2gxDYRR8TvfJUlqjWjSTGM3MQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇷🇺
‏دميتري ميدفيديف: أفرجت روسيا عن الجندي السابق في مشاة البحرية الأمريكية روبرت جيلمان من الحجز لأسباب إنسانية. وهو الآن على متن طائرة أمريكية تنقله من روسيا إلى مطار واشنطن دالاس الدولي.</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/naya_foriraq/87571" target="_blank">📅 19:41 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87570">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">‏ترامب: "ستصبح دولة جهادية. انظروا ماذا يحدث في ميشيغان..."</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/naya_foriraq/87570" target="_blank">📅 19:32 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87569">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">المركز الأوروبي المتوسطي للرصد الجوي:
"أفاد شهود عيان بحدوث هزات أرضية في كولومبيا قبل 5 دقائق"</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/naya_foriraq/87569" target="_blank">📅 19:27 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87568">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vyppLiRkldZYmPiI-N50mQAFByR06Qzx0L4fJwaLJ4vtXmmGgfKtj-HEkBs_EFNwTQvagz_Ltnrk2ZtgvavPZ8KxiHxcu_OJKDqZFR4Gy0VkLCG0Y3Se5S0r5J_-hQ27Yq3UqCVv6ghBnsEbn0GzY5JVPCYTJ17LM4ezvKL6vqVy0q9eutRRz-o8rK7rXpiCFLAWMXPnTY84503cuMyO50fdSfXPHnMyMgZ8faygJEcakzp3jFICn0-sk7sYuj-rrKYRUHJiVuafsIZQ8kfkzINYUOG8umalHju8xbGj3p5KzAVonlMzy3_jy9UlHImMYynlW6lYRKIv0iV2az9rAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامب
:
تكلف ضريبة الشقق الصغيرة في مدينة نيويورك مدينة نيويورك وولايتها ثروة طائلة، حيث أن الأموال التي سيتم الحصول عليها في نهاية المطاف ضئيلة للغاية مقارنة بالضرائب التي يدفعها عشرات الآلاف من الأشخاص الذين يفرون من المدينة، ولن يعودوا أبدًا. فلوريدا وتكساس والعديد من الولايات الأخرى تجني ثروة طائلة! هذه "التجربة" السياسية الخطيرة في نيويورك ستدمر ما كان يومًا مدينة وولاية عظيمتين. إنها ساعة هواة بحتة، ومن الصعب، كرئيس للولايات المتحدة الأمريكية، أن أجلس مكتوف الأيدي وأشاهدها تحدث، خاصة في مكان أحببته يومًا ما. الخراب المالي، ثم الاجتماعي، أمر مؤكد بنسبة 100٪ - ثم يفرض الجهاديون اليساريون المتطرفون رسوم الازدحام فوق كل شيء آخر. هذا لا ينجح في أمريكا، ويجب إيقافه، الآن! أبحث لمعرفة ما إذا كان للحكومة الفيدرالية أي حق قانوني في تجنب هذه الكارثة، قبل فوات الأوان، من أجل ملايين الأشخاص الذين يعشقون نيويورك ويرغبون في رؤيتها مزدهرة، بدلاً من أن تصبح مكانًا قذرًا، مليئًا بالجريمة، ومتهالكًا، ومثارًا للسخرية والازدراء. لنجعل أمريكا عظيمة مرة أخرى! الرئيس.</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/naya_foriraq/87568" target="_blank">📅 19:12 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87566">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🇾🇪
انصار الله شنو اليوم هجمات متتالية بـ10 صواريخ و4 مسيرات على مواقع في الساحل الغربي بمواقع تمركز مرتزقة السعودية.</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/naya_foriraq/87566" target="_blank">📅 18:46 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87565">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b2stgpeY_Sh-5a5jc_V7Uly2DZtRT_Vv2C6r7OB4V6gZGAP6s8Or6h-fUcPfHBUbWM6OPZqkgCW6M33l9X9cv9C8om14eMRPd9ou1GZy7vzPsuJftVAeXx6yCVCUMntvhcunyF877atKnB0s6iEN0ujtG9IdLRqPr6teL0evQE4yofvf_kt8dADsxnpHgP_ybYzDo4Vmlp1lkBDMhC5COTuw7hfd_Q3dMUffk2DdJgmB__kmo41DWjzz-SYW43z8HgyIPJHuzKMs6JUmTZ1RL5KwaOTwJtlY38k2ED4pQgRrZVqFr_as7QqKOk-wYnxliqCMElONXTtuuihwDH5mQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇱
‏
نتنياهو
: الجولان أرضنا وستظل دائما لإسرائيل.
🇸🇾
رد الجولاني: حكم على بشار الاسد بالاعدام
.</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/naya_foriraq/87565" target="_blank">📅 18:40 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87564">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🇮🇶
انفجار عبوة ناسفة بالدجيل جنوب صلاح الدين ؛ اثنان شهداء كحصيلة اولية</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/naya_foriraq/87564" target="_blank">📅 18:11 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87563">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🇷🇺
‏
دميتري ميدفيديف:
أفرجت روسيا عن الجندي السابق في مشاة البحرية الأمريكية روبرت جيلمان من الحجز لأسباب إنسانية. وهو الآن على متن طائرة أمريكية تنقله من روسيا إلى مطار واشنطن دالاس الدولي.</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/naya_foriraq/87563" target="_blank">📅 18:06 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87562">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🇮🇶
شرطة البيئة العراقية تكتشف كهفاً في صحراء الأنبار، بداخله نهرٌ يحتوي على أسماكٍ نادرةٍ جداً عمياء بلا عيون.</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/naya_foriraq/87562" target="_blank">📅 17:55 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87561">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🇷🇺
روسيا:
القواعد الروسية في سوريا سوف توفر مركزًا لتأمين العمليات في إفريقيا.</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/naya_foriraq/87561" target="_blank">📅 17:36 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87560">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">اصابة 14 راكب خلال رحلة قادمة من جزيرة فوكيت على متن رحلة الخطوط الجوية الهندية بسبب تعاطي قائد الطائرة للمخدرات مما ادى لانخفاض مفاجئ في ارتفاع الطائرة بمقدار 300 قدم</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/naya_foriraq/87560" target="_blank">📅 17:29 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87559">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">ترامب: يتحدثون عن نقص الذخائر. السبب في انخفاضها ليس حربي مع ايران بل هو أن بايدن قدم ما قيمته 300 مليار دولار لأوكرانيا ‏عندما غادرت، كانت الخزائن ممتلئة. قام هو بإفراغها ولم يعيدها.</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/naya_foriraq/87559" target="_blank">📅 17:17 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87558">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">ترامب: سعر النفط أقل مما كان عليه خلال إدارة بايدن، وقد منعت إيران من امتلاك سلاح نووي لأنه لو لم أفعل ما فعلته، لكانوا يمتلكون الآن سلاحاً نووياً، وكنت ستخاطبهم بـ'سيدي'.</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/87558" target="_blank">📅 17:12 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87557">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/296520615b.mp4?token=kxQRe_lIqumuPfeIoKy2kh1E5PeaGW73w7-fmNZ_IE7SvFeFTv9wGyzpZsut9hyv6gQ5woTaAoXGoHDAP2JoAIlgzHEMRetDlC3MfUbYovt-Xww_nd8L1kGbCWBPY8PSY9Ca9oiz0YYYMTZ6SP3xqSmvCmLErW3PJxztcYDbGl4K5pymd67Iy_qgif0NhTcTcTLO-o4lln4KqEsjA3A9T8FYnpsEMQAMiidlEViZNgx6170agv3rJUhuJosWZLwuVHrfuKu517W76_sCmNnazR42a_ND2d72Q3cLyekQygnKqH0hWtykDZ41nHCf9ubPdN-XvMS7LZDfuVM4pjDtYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/296520615b.mp4?token=kxQRe_lIqumuPfeIoKy2kh1E5PeaGW73w7-fmNZ_IE7SvFeFTv9wGyzpZsut9hyv6gQ5woTaAoXGoHDAP2JoAIlgzHEMRetDlC3MfUbYovt-Xww_nd8L1kGbCWBPY8PSY9Ca9oiz0YYYMTZ6SP3xqSmvCmLErW3PJxztcYDbGl4K5pymd67Iy_qgif0NhTcTcTLO-o4lln4KqEsjA3A9T8FYnpsEMQAMiidlEViZNgx6170agv3rJUhuJosWZLwuVHrfuKu517W76_sCmNnazR42a_ND2d72Q3cLyekQygnKqH0hWtykDZ41nHCf9ubPdN-XvMS7LZDfuVM4pjDtYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طيران مجهول يحلق في اجواء محافظة كربلاء المقدسة وعدد من المحافظات العراقية.</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/87557" target="_blank">📅 17:06 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87556">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2516bb44f8.mp4?token=DiwaEYLNAtWBYuEtkRRZpkzIWxl1ex-hm_JTUw14yUgXApY3jaY2lWgDDwcBQuXv9FehQ_VZQqY9JLbg2SZtoxNfw3v5fGkmWyQy__Ti3zcjB-n2Poo4cXutqGFYRXJwTds8XbRJYEYlJfgtO6LgFEHHYonOCADwnhlFdOIZxcUIpboLYgW8XTp5ImRQd6YZBlkJHlbv5TtZy4ieEirpf-oo5v2XX6iJKGePadAQBQQCylDFjmvWYZRtUGNiAgAfpeOrjICQXT2tb-kf58kwuZdzPxnKOSGPoKo_Wlkt70pBFBbyJDDFm4i8kKQadhHQ9cZWQpA2GOCXNMdf_aFXXBTHTYkRofpn9C826XbFn1emiLCRD19W1lrwgbb8tTIQ8iBLsFiaxwxTFMlFVr7OSHWkfix_V0s06-sKzmHbPbBml6uMq-wkR_0CiR8rOBLXugAArpjfHBj-YSH-hrezQsy1Y9vq9J-CDmOezZzzhgCb0LtX-Y9q1uATdRwsvDPTubQaK66QJgdODgtYV7SjHDcPf0M8vkY2j9c0hMvCTW-60X8bjh8DCBci-RbjJWBkD9gJinWDLRVgTHvgq6EKQYlq9aJz92kl38IzMJO_3GyU7v0EiWPv8QCffGxzxLoiZmTe5JgVCFDR4U2MQ3vrpocxMA2s825C71Lb8rOFgKY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2516bb44f8.mp4?token=DiwaEYLNAtWBYuEtkRRZpkzIWxl1ex-hm_JTUw14yUgXApY3jaY2lWgDDwcBQuXv9FehQ_VZQqY9JLbg2SZtoxNfw3v5fGkmWyQy__Ti3zcjB-n2Poo4cXutqGFYRXJwTds8XbRJYEYlJfgtO6LgFEHHYonOCADwnhlFdOIZxcUIpboLYgW8XTp5ImRQd6YZBlkJHlbv5TtZy4ieEirpf-oo5v2XX6iJKGePadAQBQQCylDFjmvWYZRtUGNiAgAfpeOrjICQXT2tb-kf58kwuZdzPxnKOSGPoKo_Wlkt70pBFBbyJDDFm4i8kKQadhHQ9cZWQpA2GOCXNMdf_aFXXBTHTYkRofpn9C826XbFn1emiLCRD19W1lrwgbb8tTIQ8iBLsFiaxwxTFMlFVr7OSHWkfix_V0s06-sKzmHbPbBml6uMq-wkR_0CiR8rOBLXugAArpjfHBj-YSH-hrezQsy1Y9vq9J-CDmOezZzzhgCb0LtX-Y9q1uATdRwsvDPTubQaK66QJgdODgtYV7SjHDcPf0M8vkY2j9c0hMvCTW-60X8bjh8DCBci-RbjJWBkD9gJinWDLRVgTHvgq6EKQYlq9aJz92kl38IzMJO_3GyU7v0EiWPv8QCffGxzxLoiZmTe5JgVCFDR4U2MQ3vrpocxMA2s825C71Lb8rOFgKY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامب: سعر النفط أقل مما كان عليه خلال إدارة بايدن، وقد منعت إيران من امتلاك سلاح نووي لأنه لو لم أفعل ما فعلته، لكانوا يمتلكون الآن سلاحاً نووياً، وكنت ستخاطبهم بـ'سيدي'.</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/87556" target="_blank">📅 17:05 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87553">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/794bf9e946.mp4?token=TllfHuE95osmw6FE8XOJCeRY50sMIKP0xv7EwHDQIYHS8NDO1bgklMySaMs3QUoU7OsPAoE5QfoWu9sF8km2QWRsGXdVM8eFTv5cFIBt0iccyMh33NkP3sbYT7oFKdumvwNA1MmCBWCUirvl_aOlSbCarp8IrTwsppQzn89VYtkElbStgpsz9dL5uMHCa1F4nslWV8IV3omycDY07UbefnZtNO0q2hHGOW2ZG7UdL8kjjGNmz-Ed5WorcQ7-Fytpt70BbxKf1_IzJBesoVFaX4eQcN015lh2BfK4_B1air9E4uzoPs3OeOBUL91WCgn7g3xwBiNROMwFcWxJ_NrOng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/794bf9e946.mp4?token=TllfHuE95osmw6FE8XOJCeRY50sMIKP0xv7EwHDQIYHS8NDO1bgklMySaMs3QUoU7OsPAoE5QfoWu9sF8km2QWRsGXdVM8eFTv5cFIBt0iccyMh33NkP3sbYT7oFKdumvwNA1MmCBWCUirvl_aOlSbCarp8IrTwsppQzn89VYtkElbStgpsz9dL5uMHCa1F4nslWV8IV3omycDY07UbefnZtNO0q2hHGOW2ZG7UdL8kjjGNmz-Ed5WorcQ7-Fytpt70BbxKf1_IzJBesoVFaX4eQcN015lh2BfK4_B1air9E4uzoPs3OeOBUL91WCgn7g3xwBiNROMwFcWxJ_NrOng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
مناشدة انسانية عبر بوت نايا
بعد منعهم من الدخول بريا خلال زيارة الاربعين من قبل السلطات الايرانية لاتاحة الفرصة للزائرين الايرانيين.. مشاهد من محافظة ميسان لاعداد كبيرة من الزائرين الافغان والباكستانيين الذي بدأوا بالدخول الى العراق من الحدود الايرانية لزيارة العتبات المقدسة ويعانون من شحة وجود المياه والمواكب على الحدود بالتزامن مع ارتفاع درجات الحرارة.</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/87553" target="_blank">📅 17:03 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87552">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">طيران مجهول يحلق في اجواء محافظة كربلاء المقدسة وعدد من المحافظات العراقية.</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/87552" target="_blank">📅 16:55 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87551">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🇮🇶
العثور على رفات 12 مقاتل عراقي في مدينة الفلوجة ضمن محافظة الانبار غربي العراق قتلوا على يد تنظيم داعش عام 2014 وفقدت جثثهم.</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/87551" target="_blank">📅 16:51 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87550">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">مرتزقة السعودية في اليمن:
مقتل 4 بحارة وإصابة 4 في هجوم لانصار الله استهدف سفينة في باب المندب.</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/87550" target="_blank">📅 16:41 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87549">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">انباء عن سقوط طائرة MQ-9 أمريكية في جيبوتي ولم يتم تحديد سبب سقوط طائرة الى الان</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/87549" target="_blank">📅 16:33 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87548">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">قوات أمريكية أطلقت النار على السفينة "فيلا نوفا" التي تحمل العلم البنمي بواسطة طائرة هليكوبتر وتم الإبلاغ عن سلامة جميع أفراد الطاقم الـ 17</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/87548" target="_blank">📅 16:30 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87547">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">الكويت تزعم احباط مخطط لتنظيم داعش لاستهداف احدى دور العبادة</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/87547" target="_blank">📅 16:19 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87546">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ceb842a65a.mp4?token=mPWJbY4XmpvKF2m1V7KAKiNoj_ibjYPx4RkVepVoYHV5vpgu5iKKAyM8MqjSossuMSEvnNc64mJdw-F0qRGTMGkZkfLEjO3k4F8Tb76Qro9WvBHDpnpQsYywefWCkVKp7xfxdB7TC9zRQGwp4NFZXcQ2Y7thq7mT0DM-wXtuP5JieyOdU-YJ6piPI_QR9cyoBHKXGV_UDpuylk7BsLV7r9yyFbJZHlOfXh1iuDXfejO9UEk_yYwDr4OGedDEC8ScFXSlChEFw4ViMHqW65rGrYVz4jRYtb0rfH_T2AHxZssviIDpaUuSeh-OgdilCNEKzHqpyHoa_ELVY8_kxolBBWyudTmVzY1wOAd0k3xMPdvCMqGh5FSqTY6YTjhEGWygjZ940DZ3jv4a7Nzcqw8kerwW4RI6UAdsLrwN5zWJ1C75g78VWWPkLzinOIutOzVmDGGXll1zr3AD2BGAlhOXX_QRALk7q-6EQDge4idsqtb_0D2K3lI_dVv82XKOansSD-HjKgQMpu7hMHX-2b0VPBTXdj7QDPxBHcDr7nRZo32H0H4Qc_rKccTwZ-LZuJZPGU_R7XbZGeh0eCUGdrDnsPoqH_x7gxv3uNou0cMCwjHVyFOu49zJWB_0U_OZMBfmyQVGYbrxIMGXvV_fo5OPzzF0eQVQKkiZyQcNDOyZtu8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ceb842a65a.mp4?token=mPWJbY4XmpvKF2m1V7KAKiNoj_ibjYPx4RkVepVoYHV5vpgu5iKKAyM8MqjSossuMSEvnNc64mJdw-F0qRGTMGkZkfLEjO3k4F8Tb76Qro9WvBHDpnpQsYywefWCkVKp7xfxdB7TC9zRQGwp4NFZXcQ2Y7thq7mT0DM-wXtuP5JieyOdU-YJ6piPI_QR9cyoBHKXGV_UDpuylk7BsLV7r9yyFbJZHlOfXh1iuDXfejO9UEk_yYwDr4OGedDEC8ScFXSlChEFw4ViMHqW65rGrYVz4jRYtb0rfH_T2AHxZssviIDpaUuSeh-OgdilCNEKzHqpyHoa_ELVY8_kxolBBWyudTmVzY1wOAd0k3xMPdvCMqGh5FSqTY6YTjhEGWygjZ940DZ3jv4a7Nzcqw8kerwW4RI6UAdsLrwN5zWJ1C75g78VWWPkLzinOIutOzVmDGGXll1zr3AD2BGAlhOXX_QRALk7q-6EQDge4idsqtb_0D2K3lI_dVv82XKOansSD-HjKgQMpu7hMHX-2b0VPBTXdj7QDPxBHcDr7nRZo32H0H4Qc_rKccTwZ-LZuJZPGU_R7XbZGeh0eCUGdrDnsPoqH_x7gxv3uNou0cMCwjHVyFOu49zJWB_0U_OZMBfmyQVGYbrxIMGXvV_fo5OPzzF0eQVQKkiZyQcNDOyZtu8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
حادث سير بين صهريج وعجلة في محافظة الانبار غربي العراق يسفر عن 4 وفيات كحصيلة اولية.</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/87546" target="_blank">📅 16:13 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87545">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">قوات العدو الأمريكي تطلق النار على سفينة ترفع علم بنما قرب مضيق هرمز</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/87545" target="_blank">📅 15:56 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87544">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">قوات العدو الأمريكي تطلق النار على سفينة ترفع علم بنما قرب مضيق هرمز</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/87544" target="_blank">📅 15:55 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87543">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ce4ade89d.mp4?token=vhFqBJdBUJXu5_b8C9PsKa5WLmByp5GRtr9lsRRqmCMHJ5-pxlUEEphoMws-FLLNkN5hu41Vi2K9uK9DL_IAJH3U6MXVRRaR7EudfAwkMhH_PxW0b-fFmaHC8yOBB3_guTxrH1oAklCYCWGf8Hd1xZ_tN2TywT69k7BpzI707YvqNtb9JiE70HROBxRIaxdNkBdASOY3n7zgt69rlxiqsO4NujguFGkl5qlLnxP70b2Y0Otrm02yj3K0NvJHJq8KP3e60CC_RRcKDK-IjbXWTi3Ji2EjN35y8uj2rXYg_PMCbeaoSf2TAgbaBO-2wlw_C6kWlSYmTrqLYhg9P3BUyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ce4ade89d.mp4?token=vhFqBJdBUJXu5_b8C9PsKa5WLmByp5GRtr9lsRRqmCMHJ5-pxlUEEphoMws-FLLNkN5hu41Vi2K9uK9DL_IAJH3U6MXVRRaR7EudfAwkMhH_PxW0b-fFmaHC8yOBB3_guTxrH1oAklCYCWGf8Hd1xZ_tN2TywT69k7BpzI707YvqNtb9JiE70HROBxRIaxdNkBdASOY3n7zgt69rlxiqsO4NujguFGkl5qlLnxP70b2Y0Otrm02yj3K0NvJHJq8KP3e60CC_RRcKDK-IjbXWTi3Ji2EjN35y8uj2rXYg_PMCbeaoSf2TAgbaBO-2wlw_C6kWlSYmTrqLYhg9P3BUyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇬
15 حالة وفاة وإصابة 22 اخرين في حادث تصادم بمحافظة الإسماعيلية المصرية.</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/87543" target="_blank">📅 15:46 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87541">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/c8aRT5rACc0ZND_47eGiPaBY-n5yyrhBRb7fTAFuMJuPqctmzjK-wwBVqaSkXc9sZKzJQu10fAvJrRdUZHLD27EKLP93YuKbVWcs3Pw67LMxeEl-Z8uUfznbkWcxWUnfJeW7agCVUzXPStTGgBWTCX-ZLSHGhSVoZd3p53EVQDjO6XdhqgRNPkuhz78oQHfO9yQCzwMwBuchrbqNuqRseczTeP8cP8cnrbmsa2XQzrpXIUEfjFSMnSZkmgmdk0-wswkbVGxpaDmDzTOckUr6PF-_fSLCnMJrsUbnyuf0dUZKBWtKXIt6QdIUWht9Gnwm87_YoLGxYmfnOYpfPIZsqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kWjUB42XBVtpDZ6iZTGoGn6-8R6aY7GQvZ-9zBTbyWtrABTLO5eiFZuv8vewZAE4Ryddj4iEIzU0c_NSGOj0M3QPRK3lfaotoFCwN2tVFutdcVaKSWrUzySqGcfGkCcVgbVX4q-MRwNLKtXndO6zWy_b-MI16mEN3hDg7tAqtDij5rwi7x0BYlncXqjghNa5Jhes22uS2cYMBBJx9DhPBctHyll6raQrauMXWqqCZKrCVPm2GWWdwyZiWO0Bg8UxTfOhXW_HKKuSbbMbl_L3znohj7U8MfvnGjnQyizdfzT5ColRO7Q-oPBt4G5qZIMiaiHVSStHJ1qNrR7r5IgrCg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">العراق يبدأ العمل على تشريع قانون يمنح موظفيه اجازات طويلة لا تقل عن 5 سنوات لمن يريد مقابل منحهم 50% من الراتب بسبب تصاعد الازمة المالية وكثرة الموظفين</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/87541" target="_blank">📅 15:33 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87540">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dr8zedwsLpW-vgAF237u3pK2PGYYPOKwuZRHNTkFdNXzcnmU5oiy0K1Hwb5Y4hon4dN_cPqQf-me0pswwxN41TfHq0RmnInOoVxbtqltcFq0_e9mBxRhUahBxQpLK6IFVYd969O4X-Hl64wr1Gud4eQsvVgNwhBjJjtB-tsAsCZjDRErI0gVDz47S57hOuyTaZ79S1V7iAKgEREnhJAbAYsGBvkUKRglT80WiyDtxeeQiy8kt_y2Ke4vtVHAcWKHmJIUOzBlVv3eA75wf2qUbkjwlT2Rlg091Cpw6Y88txgjgzHO0Vb_55-iD2qyRjpLC8EyYQ821iiYKgAGeJqHXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طائرة من طراز بوينغ 737 تابعة للأسطول الملكي الإماراتي A6-RJA تحلق من أبو ظبي إلى طهران
‏هل ستتجه المزيد من الجزية الإماراتية إلى إيران، أم أن مسؤولاً إماراتياً رفيع المستوى يقوم بزيارة؟</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/87540" target="_blank">📅 15:30 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87539">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">استهداف محطة كهرباء الزاوية في ليبيا بمسيرة</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/87539" target="_blank">📅 15:18 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87535">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rrkE7-2eZtQjxciH7OnCL5BzLnR9xqsGLsHxdNHD0OVh0p9765lgTD3c4-CnQbBff3CavmIsIdFDx6fQnEIJLOpigdCJS7vVe2lMKRWz6jzPKv-zQy6SAnrHwEq0bXWfD97F_29C21MsrLyyo0UfRVKg5rGDeg4uZhktp1JcyIUvo-8KBHGQsMFg2I2IbOFOdXUpRU3B5YNQP_iJZQXNLhUi1OVB8JZygz1q1xhkxBUhwce1W0sSrpAFbgbapmTqAdzUtbqUlafO7-lzsNLeXOZC4I-0gaQnhSXpbfgqOrwkTmv-fwKd54mzsV06Thjx8jA8709R-jN2-QUhcqrLQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MIeNSvC4YY7fhS6flINDCM-iStJfyyOcqdJ52Rw2iutSe_Q_5EfDv9NAeL1qWtJX88PfgtRUN2ccoh66DCKZ3PU1OIkL7vXj04hmjIKJCB3HpUHlHrQZstP9tlZQ4CNcbMveM-MA6pRLKkdfu8H_0GsoooT5NJyCA0lLG0qMxLhIlEWCdr-6I6Qhjxm4KYk-K_UpRK1mvLgA0Hi43BC7quXa8kHBw3eIYGWfS7m8-paYnFlR5AdNm8Km12hvl0bcgcx7O03REfJz6gjdsi5s06uLTmxjR6ds4tck5Eq9LszmNIj5ouDY7AtDIfzun9nhGJkJTtNMftU2y6MuALzYNQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5979332c5d.mp4?token=PuiTFYSRK_BcB2fmT3f_bSsV-sAiV81i4H82lzg6s9cA_Y8DSFRxDMawdjI86cldVfxWsTvBqgPqK6cte4CIAALuMJBS77TEYByKUcc9n-Z2uyOmYvyJxlrrnfZBnQhYAE5AVHAhyFb3fojBg3DLjudb7KbkXEtnk_JImn7SEwW8QYAU_8vU1ZcJaiYck3FcOXJbtmUAEolMPGultE86c_1S5XUemgXvXdVmNi6hkIo8QCFDhFKsivEV5fI1rh487g0WMajO_BCV7G3_nLxyaiiKogRIROJ9j5AwGO2XEl-XaTvPvdpM80LNhfuOkMUAD6YlEZFouF1QuCrgge3tlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5979332c5d.mp4?token=PuiTFYSRK_BcB2fmT3f_bSsV-sAiV81i4H82lzg6s9cA_Y8DSFRxDMawdjI86cldVfxWsTvBqgPqK6cte4CIAALuMJBS77TEYByKUcc9n-Z2uyOmYvyJxlrrnfZBnQhYAE5AVHAhyFb3fojBg3DLjudb7KbkXEtnk_JImn7SEwW8QYAU_8vU1ZcJaiYck3FcOXJbtmUAEolMPGultE86c_1S5XUemgXvXdVmNi6hkIo8QCFDhFKsivEV5fI1rh487g0WMajO_BCV7G3_nLxyaiiKogRIROJ9j5AwGO2XEl-XaTvPvdpM80LNhfuOkMUAD6YlEZFouF1QuCrgge3tlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اضرار جسيمة في مقرات المعارضة الايرانية الكردية في محافظة اربيل بعد هجوم صاروخي ايراني</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/87535" target="_blank">📅 14:54 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87534">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GW71N86s6xDeW8Fk8inHjxMKtdxfaW970Nz0CEXi8ZPUpFpzEV7rN21Z8H76HN6fPk4CcyKhdtpIUh65Tpkpv7ACOCgkMLIoJSd1OEUa7fuh8YZBIc2YBuY7Deo-x-yymcj4JQx3wFoSOS8_ygIqbrKQ1R-RRhLTK7-LCZrVh2W-e-ztnerDHDtWTDdHDZskoT2V47h8nk-3xfuFzYTgEf__W6Z5yiGVZjnHNmZNpgthrDag_UCMWJV3ryhQ6HwJg5jHc_P0k89V4mx7PlQGvUEagr84RRBFsIGGwckKX-2fX10NV2DZPvzG3t3D4Aza2rs-mSLXIp1CD6L_bCkdOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">أصبح الآن بالإمكان رؤية أضرار جديدة في مصفاة جازان النفطية جنوب السعودية عقب هجوم بطائرة مسيّرة شنه انصار الله في 5 أغسطس. وتُظهر صور الأقمار الصناعية الجديدة من Sentinel-2L أن خزانًا كبيرًا آخر لتخزين النفط تعرّض للإصابة، ما أدى إلى اشتعال النيران فيه خلال…</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/87534" target="_blank">📅 14:36 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87533">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3dfaf180ac.mp4?token=Nf-I2qvrHPF1H1PR87Iq8StrpHqSob39THIgb4yKXlEd10Y992UyPbCfLAQu1Seb8d3efFhfbhCkb9qQFcRhS_wTZnkzoupuIP_hypay5-ZqavF_RFObXzST9FWFQ_muViHHuzSViNgHuTSjFK2qZRlTEDvtOZIxxlAc_puDx_1LRqQJUhioF50ShW01fmugMvnrivt2CEkLBU5CZmmFm4kbSthB4MIzIsLItCpbv4G9N-12aPoLeJ4Qp_QC2j8H-1bdpGk8spWnZtRPmljSP9iRpRSn82jJrsbcjFcmri-lFVgBnja_K7asYKg1Vu4UQjy1RQLPXO-hDv0J5Yb9sg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3dfaf180ac.mp4?token=Nf-I2qvrHPF1H1PR87Iq8StrpHqSob39THIgb4yKXlEd10Y992UyPbCfLAQu1Seb8d3efFhfbhCkb9qQFcRhS_wTZnkzoupuIP_hypay5-ZqavF_RFObXzST9FWFQ_muViHHuzSViNgHuTSjFK2qZRlTEDvtOZIxxlAc_puDx_1LRqQJUhioF50ShW01fmugMvnrivt2CEkLBU5CZmmFm4kbSthB4MIzIsLItCpbv4G9N-12aPoLeJ4Qp_QC2j8H-1bdpGk8spWnZtRPmljSP9iRpRSn82jJrsbcjFcmri-lFVgBnja_K7asYKg1Vu4UQjy1RQLPXO-hDv0J5Yb9sg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">أصبح الآن بالإمكان رؤية أضرار جديدة في مصفاة جازان النفطية جنوب السعودية عقب هجوم بطائرة مسيّرة شنه انصار الله في 5 أغسطس. وتُظهر صور الأقمار الصناعية الجديدة من Sentinel-2L أن خزانًا كبيرًا آخر لتخزين النفط تعرّض للإصابة، ما أدى إلى اشتعال النيران فيه خلال الهجوم الأخير.</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/87533" target="_blank">📅 14:33 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87532">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">حادث بحري قبالة سواحل المخا، اليمن</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/87532" target="_blank">📅 14:27 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87531">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IxfarQ_IrzqKpdjVOWbnMiRADVeFS4uvFCav30kSKuu0gnyMUKsjSboiFu4kI48JqYijHdeULvsVbySpoLYseTHEys9aujL2fJGzwu38KX35yCIFfB_SDj8mOBAsjPNUF8N2fAr73Uz2UQW3jZSS4pefq8zni1O0oXVacheSQY_JgTnUDM-tcIWKHYkII_HewPCucgT305vcmqQhzM40jSa1iOrYI8S7vWObb-mdwc-C29GbmZBrXNQNIpQgH_7zILqVWYc3yhe4fTWEe6BDtQ75T3WXfdfSoLpjQNXthQp-coSXAvYxoILJOfh8uRYRqZvCo9DM86lyatvqSCxhfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حدث بحري جديد</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/87531" target="_blank">📅 14:26 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87530">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/87530" target="_blank">📅 14:26 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87529">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/87529" target="_blank">📅 14:26 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87528">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">وزير الشؤون اليهودية في الشتات الإسرائيل: الضفة الغربية هي قلب الوطن اليهودي. هذا هو ميراث أسلافنا. السكان الفلسطينيون هم سكان معادون.</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/87528" target="_blank">📅 14:19 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87526">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/owBfXjiV70sMQEmKMpnHudOEIH1nOnaFWshSV7ZwVfFBStL-8dSRK_ml_SjtQobNjqBmGtOe1pUxrZVJnrx3zx2-Kpp3maqGCH5AeD265K-FJKUclNdz3F7wlbpxxH59zaKvRkKVThpbNFVKQk4y9OwUK7wbe79Xsqs8fAzetIMPWKFlP9P4oZNRh1rnHaf3yf-Q46muiwTMBWemLFg8YcbZGVKW4LEdxXI4nJmTyn1DDKLuLjgVyROoJ1nCBhIXB0gTYKdr05PfUKt86pN7sErCyTG5G4ydz0-HZOwpygxEVbCMzlGvDUhYKXT8elpDq9agQuuDymuVd376rcLnLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BMmsCojjfVs6JT7linLxsBi1KNoIT-j113CsDVnJrf1bdggTLxCpCXlyU-DOEs65Vt4MP-05tCKRhr-2Y5o11n6wKq99i1Vbt_Xb_9WiOh9y0NoW7iVX5b968NYRnH3Taadkg3-U3GIYbhD7J_PgF02NxNehYV7ljIc4sf4wvQy4BCCYOwIjcny9j7cufN-nzrnMU2JdbFKJaftThkTn18UbAYaIkNz2_nkg1P60SUPYAjABr9DrLgNN_AWbOFX2HTt5QGjXDULQtgvrOiIkatUMBeWBL5SPnZDhJiFVgq7322oCfxrhS91KNR9hlxjVUZqBNCu1b05qcWUlxZDZIw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇶
أنباء متداولة عن استشهاد 3 منتسبين أثناء أداء الواجب في قاطع عمليات صلاح الدين.</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/naya_foriraq/87526" target="_blank">📅 12:59 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87525">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/87525" target="_blank">📅 12:39 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87524">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/naya_foriraq/87524" target="_blank">📅 12:39 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87523">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j2SYH1oTL0nJSe5uEsCttE_ZaIBOlhcG_UGNkUCrFSl-V-8AeUC5UOr6K9DgPj7l79S2k5vcv9s9ZBqcdt0Hl5CvG4DsvevHHPS5oOV6YvvwyLdq4VKpeq7y-z2kX9OFmDmIWmnXprP4WowM7IdomHfDwZOFbeWSK4fSVf1d5UuUPKDGs2Zi_lxXI4mUOr2iDkUXS5QYnmI4dAhRqhBc_xnvulkjuaNCYkigXYUKTuOFU48dw2Hoq_yO0Sw4u55kAL-W3OAFhYtTl_eat_gq1_kML2M-hr64EullB__PzpHUU2p5cxEgS6IgO2z4Y-ot3FJ2122-jalJYlMGSfF06A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇸🇾
محكمة الجنايات في دمشق: الحكم غيابيا على بشار الأسد بالإعدام.</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/naya_foriraq/87523" target="_blank">📅 11:51 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87522">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C-AlkHa6xF1mzXPf4WZZ2tIvwjACEtPiDK21rgeKzvY7nsMuHim2hXKKUfAPnZTw_kgJI7tzpcxIlNxHN16Mfwl1OjnGhA20FnCJtsEp2HFde0aMIhXUApUdDrlue1el0JU2f6P8tX1EJvorUoUI6DfpwAW099o5nDDoadVOXbZPpHMGPyUSyBw7pxA0yrXM683rT_roTLf4xSEYD5dSUwa31B3qpPEcCSFUaskKTvG3SgCcnfNM_F3OqLuMnf4b-aa_Jlql8_sZ4t-38uCf9cOkjeHCq48Zss3fDIvXY9zaAs644d4lRfZVD6MnvwZmDrM-9R6q0vpkFLPrYF2vRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇸🇾
محكمة الجنايات في دمشق: الحكم غيابيا على بشار الأسد بالإعدام.</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/87522" target="_blank">📅 11:49 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87521">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">قصف اخر باب المندب</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/naya_foriraq/87521" target="_blank">📅 11:39 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87520">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">قصف اخر باب المندب</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/87520" target="_blank">📅 11:39 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87519">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🇮🇶
أنباء متداولة عن استشهاد 3 منتسبين أثناء أداء الواجب في قاطع عمليات صلاح الدين.</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/naya_foriraq/87519" target="_blank">📅 11:32 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87518">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/77ffc5a740.mp4?token=J0aI7xrvc0Ur_O3Bj78Pm3-U5qeV_Le5l-4kBlu1DMsB60ATZnvKvCT7F0ncXS9lm5SeyPMu70zLTi-ssvmGzrrZwXJLlFI_E3DMds5QLa1d38gCOL-x-EHS3cwQNWvA0uZaEtaloqSyMCvOC5o_QbGXCxmtZrRI9OdjJJv0qG4NLqHd2EJkzXsWbgnYE39IEbRoTW8UviBuJb8i4Quk6TYXxuMoIvK8VrSmtYL-u3IjbxHWi6d3zntYVX0xWdR1U6bZZ8FeEaGlJgB1NSaZS6QuyLq6gX466tWaAmtmJtss3J1ENq84L1P09ScpLa8qFFHq0Mnq-0xV1cPw5l3ZSky5J8KVZiOJnZB8o1WBaZHPCwGgOZuCVvzED1V0NIufAO4Fh0S-m0V5wZqXvh76hizm9KUcIxcIfdSijCFjDu67E4Gfu2waapxhajwN-zX-fTEK9eG-KZD2bY4080k0HiQ5Znzc9OIF_ARqiSv2L5Ks4cXMOSboUlZOTsed8CnP3chFQumQU3fUW3BOgkkkw2GkCsj_JdaCpf4yLB9sbirjFQmBuWVzPNlIInf3-gmNOagUJkOhK5ISjtTdmTeeq2-4gw4HJ-FaMwfczu5j8YGCyQjtRfg9pWctEyzAew8nwf2263A1oeB2lwd2AlRpof0rdZzYampgQ3orGUDNHto" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/77ffc5a740.mp4?token=J0aI7xrvc0Ur_O3Bj78Pm3-U5qeV_Le5l-4kBlu1DMsB60ATZnvKvCT7F0ncXS9lm5SeyPMu70zLTi-ssvmGzrrZwXJLlFI_E3DMds5QLa1d38gCOL-x-EHS3cwQNWvA0uZaEtaloqSyMCvOC5o_QbGXCxmtZrRI9OdjJJv0qG4NLqHd2EJkzXsWbgnYE39IEbRoTW8UviBuJb8i4Quk6TYXxuMoIvK8VrSmtYL-u3IjbxHWi6d3zntYVX0xWdR1U6bZZ8FeEaGlJgB1NSaZS6QuyLq6gX466tWaAmtmJtss3J1ENq84L1P09ScpLa8qFFHq0Mnq-0xV1cPw5l3ZSky5J8KVZiOJnZB8o1WBaZHPCwGgOZuCVvzED1V0NIufAO4Fh0S-m0V5wZqXvh76hizm9KUcIxcIfdSijCFjDu67E4Gfu2waapxhajwN-zX-fTEK9eG-KZD2bY4080k0HiQ5Znzc9OIF_ARqiSv2L5Ks4cXMOSboUlZOTsed8CnP3chFQumQU3fUW3BOgkkkw2GkCsj_JdaCpf4yLB9sbirjFQmBuWVzPNlIInf3-gmNOagUJkOhK5ISjtTdmTeeq2-4gw4HJ-FaMwfczu5j8YGCyQjtRfg9pWctEyzAew8nwf2263A1oeB2lwd2AlRpof0rdZzYampgQ3orGUDNHto" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجارات في خزان وقود في مصفاة الزاوية في ليبيا ولم تُعرف طبيعة الانفجارات بعد.</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/naya_foriraq/87518" target="_blank">📅 11:23 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87517">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e6d2a4fee.mp4?token=oBsCfv6hizzIdYq0dYMiyEQYb-4zE63xV_jGM--KgXXKhiycJ4dcdtT6-KafJkhexDZgA104qFu5ZSpVZRFDYZM9CbhJkXz68ekvmDMNNntqh18pSU9cmGe3l7xAu4eUZ7b4-daNtP0kJ8J_KOvXNOrK3iWGx5axPqrTiv8iAxIH9vpxt8OZlI_mYUAkbRUT63ZHc7MVqz8qh5qFU0-vKK8TiI1bipQ1-E8VOyFYDW2J9l80pHvRdDRtByz26wmuZBznxfEa0OwXHQGreIeds-dI_Ee14YQjQkJ66j1GICnY8z6oLh90I9QZQK61ZhlYfNEV6sqYWhKvmO0Q4eTQsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e6d2a4fee.mp4?token=oBsCfv6hizzIdYq0dYMiyEQYb-4zE63xV_jGM--KgXXKhiycJ4dcdtT6-KafJkhexDZgA104qFu5ZSpVZRFDYZM9CbhJkXz68ekvmDMNNntqh18pSU9cmGe3l7xAu4eUZ7b4-daNtP0kJ8J_KOvXNOrK3iWGx5axPqrTiv8iAxIH9vpxt8OZlI_mYUAkbRUT63ZHc7MVqz8qh5qFU0-vKK8TiI1bipQ1-E8VOyFYDW2J9l80pHvRdDRtByz26wmuZBznxfEa0OwXHQGreIeds-dI_Ee14YQjQkJ66j1GICnY8z6oLh90I9QZQK61ZhlYfNEV6sqYWhKvmO0Q4eTQsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامب:  السبب في نقص الذخيرة هو أن بايدن قدم ما قيمته 300 مليار دولار لأوكرانيا.  إنهم لا يذكرون ذلك أبدًا. الآن، أنا أيضًا أقدم المساعدة لأوكرانيا، ولكن يجب عليهم الدفع.  بمعنى آخر، الاتحاد الأوروبي - أنا لا أتعامل مباشرة مع أوكرانيا. أنا أقدم المساعدة…</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/naya_foriraq/87517" target="_blank">📅 11:18 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87516">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bbe9815653.mp4?token=shbRMM0LxQdI0n49L41NjVvX7fe6ZqrrmfFEnEtlF2Z1gL-U_ZeP6oceCi2wFi-7AZF22ZBg0v5Yg5akVSyjcchxO3IYh8vBWUc8hvh3riMG_pFNuGpNwUM0x5Dd2SuwY02elaQ8arUxm9HV-0LXogdp1DgbOy9spvdvZnQ4nvdafNyqs5cNjsG8Ja2RcnJarHCkz_EUyinEVQgozv9jlZtgCEWxvT48BznxsXsEiE0JMGUQUM22Wngq4bihJvKTlPj6t7BgelcrOvi2OGw0VsyFsY26RDuwj5u0JPe1FrW4H7DcDLKMM_KppEiNWCuJPSGkZFjxTL_5beAE-n34_YQw7RUi9mfZqowD58iVpcbw2vkdG8SHsqm-_szltHIYl056PPyElWRWFtF3HhpS-m7CilPWiBKNBVd1pzyjyvLoJ4fmjy3YW_BtooohF6LuVQPjL2zcLx0MCcCXw6nu3qrQMzeD_NCUF02OogWonxOEYOPQzaiDVjoHbw_LSb-jQdHEsn16iQxAv3pNuWrknN_vtEft7VagI8BNZVFghs79Srod6clzWl3FN1yUA7nTIqspprIacZa3pXv1-98fVvsBDqPjiYGdoTI18xfWrWQznN70Qnc3U-GzTB8CXANOnuRSQ-6NjzxipXQWN8q7I5Jnr0ISGvt1bW5tgWR5y2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bbe9815653.mp4?token=shbRMM0LxQdI0n49L41NjVvX7fe6ZqrrmfFEnEtlF2Z1gL-U_ZeP6oceCi2wFi-7AZF22ZBg0v5Yg5akVSyjcchxO3IYh8vBWUc8hvh3riMG_pFNuGpNwUM0x5Dd2SuwY02elaQ8arUxm9HV-0LXogdp1DgbOy9spvdvZnQ4nvdafNyqs5cNjsG8Ja2RcnJarHCkz_EUyinEVQgozv9jlZtgCEWxvT48BznxsXsEiE0JMGUQUM22Wngq4bihJvKTlPj6t7BgelcrOvi2OGw0VsyFsY26RDuwj5u0JPe1FrW4H7DcDLKMM_KppEiNWCuJPSGkZFjxTL_5beAE-n34_YQw7RUi9mfZqowD58iVpcbw2vkdG8SHsqm-_szltHIYl056PPyElWRWFtF3HhpS-m7CilPWiBKNBVd1pzyjyvLoJ4fmjy3YW_BtooohF6LuVQPjL2zcLx0MCcCXw6nu3qrQMzeD_NCUF02OogWonxOEYOPQzaiDVjoHbw_LSb-jQdHEsn16iQxAv3pNuWrknN_vtEft7VagI8BNZVFghs79Srod6clzWl3FN1yUA7nTIqspprIacZa3pXv1-98fVvsBDqPjiYGdoTI18xfWrWQznN70Qnc3U-GzTB8CXANOnuRSQ-6NjzxipXQWN8q7I5Jnr0ISGvt1bW5tgWR5y2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامب:
السبب في نقص الذخيرة هو أن بايدن قدم ما قيمته 300 مليار دولار لأوكرانيا.
إنهم لا يذكرون ذلك أبدًا. الآن، أنا أيضًا أقدم المساعدة لأوكرانيا، ولكن يجب عليهم الدفع.
بمعنى آخر، الاتحاد الأوروبي - أنا لا أتعامل مباشرة مع أوكرانيا. أنا أقدم المساعدة للاتحاد الأوروبي. لديهم أموال، وهم يدفعون المبلغ الكامل.</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/87516" target="_blank">📅 11:14 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87515">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EIjZJnjnLBKo_7jTEIXXf6T3JZiRK4CwqmnocK4sxA-PXi7pGvL4iFd_Do3BKBWEsptDX0igxP3ytRvqhKy1fHfeic0iMi4hXSELdXPdWgLdgQPM4cE1xBKu4kKy0_mlBny4MjPFA1VRKalWRn55j0gx4n12ghYKwWll4vDE8KM-NUWNRu_pqNWnXBMxm0eLgHQznPK3aQanBZ243OtUC_VO4N7xVwYgF5_UHBAAtK1lBj5QVQGfcVoeXcVwVZMHTNiHvPL30TBmk7cPGh_FQb3I3IVj5GIPEhbj7IDeqwgVOn7XHdlrr23i0pbzF2nO-aCmQ600VAqBSW-hqSsm3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📈
استمرار ارتفاع أسعار النفط وسط تصاعد التوترات في المنطقة حيث وصل سعر برميل النفط الواحد إلى ما يقارب 90 دولار والارتفاع مستمر.</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/naya_foriraq/87515" target="_blank">📅 10:27 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87514">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">حدث بحري في باب المندب</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/naya_foriraq/87514" target="_blank">📅 09:53 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87513">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">حدث بحري في باب المندب</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/naya_foriraq/87513" target="_blank">📅 09:52 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87512">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c1ebe3dbff.mp4?token=pQlgrDR54ZyvlmgUGHkrXFoTxqsiwZ0LPXrJaywpVRsubyjvIoHWziT51yz2O8m8E6zvvHEFt2l9nbd0a85A4ozVfaGqtcNHfStdDHorJ1b4IVZ7dDu3lDNcEbqGXa5el4M5oHsakZhHzPeqr-UtqyCV9-RzgZzfnyuvqLeiGr_5XTBl4tCRS8h4DAgv9BNIYM3TvnwEy7lnCtJC-9r7tNKnKCUpnP4H7nhqelpkyxThLZtcRjo6L9616EbQOOWNCAwjHydbs-Op4AXYPWXK9JN7MkjJboO38mQ6oBjKmMvMPRxorYJ9G0rG4cURbz5G6BbrMYwUjNFGWLtl5P1z-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c1ebe3dbff.mp4?token=pQlgrDR54ZyvlmgUGHkrXFoTxqsiwZ0LPXrJaywpVRsubyjvIoHWziT51yz2O8m8E6zvvHEFt2l9nbd0a85A4ozVfaGqtcNHfStdDHorJ1b4IVZ7dDu3lDNcEbqGXa5el4M5oHsakZhHzPeqr-UtqyCV9-RzgZzfnyuvqLeiGr_5XTBl4tCRS8h4DAgv9BNIYM3TvnwEy7lnCtJC-9r7tNKnKCUpnP4H7nhqelpkyxThLZtcRjo6L9616EbQOOWNCAwjHydbs-Op4AXYPWXK9JN7MkjJboO38mQ6oBjKmMvMPRxorYJ9G0rG4cURbz5G6BbrMYwUjNFGWLtl5P1z-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تسرب نفطي واسع النطاق بمساحة كبيرة جداً كشفت عنه صور الأقمار الصناعية قرب مضيق هرمز ؛ تشير التقارير إلى أن مصدر التسرب هو ناقلات نفط كانت تنوي العبور دون الالتزام بالإجراءات التي أعلنت عنها الجمهورية الإسلامية.</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/naya_foriraq/87512" target="_blank">📅 09:33 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87511">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">ترمب لريل أمريكا فويس:
نتحكم في قدر كبير من أموال الإيرانيين وأصولهم وهي تحت سيطرتنا التام
لدينا 3 استراتيجيات للتعامل مع إيران أولاها مراقبة مدى سوء وضعها والثانية ضربها بشدة الاستراتيجية الثالثة هي الضغط الاقتصادي ونحن نفعل ذلك على أي حال
أكبر تغيير رأيته خلال ربع قرن ما حدث لإسرائيل فقد كان لديها أقوى لوبي في واشنطن
إذا سمحنا للطرف الآخر بالفوز في الانتخابات النصفية فستصبح البلاد تحت حكم الجهاديين</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/naya_foriraq/87511" target="_blank">📅 09:10 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87510">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DTkGfc7SAQYE8vMXTw5o6SRm5br2DHHXbXVM0bIeSuR0GgXQB8PPvd6gJqPCUvBbD7mp0JjpWCQOlzMzXE2EDJ0KVqbjr9nuw2BfBHI_Q3J3DJIKH24GA8CZjlXOnZaQ5lMbFtlM9VsILIGinH_pCjLHxdHqv1tyVMJ5TjcqenN2DfvEyY-mPCaFqX-L9L3gEvmI7XnaYhhdQkVBw02f72asaNZSrPIkt4kYiXRYcQdSaz2psnL7GDY9jPUQf3uQ8UivPA1OfOKOJkbrcZ1U3RBD70rpf3QnhTVIJ65dQDHUI7EolzpdPwmwCR9egZa21-F_kXuEDivJmKSgalk3QQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامب:
سيرتكب الاتحاد الدولي لكرة القدم (فيفا) خطأً فادحًا إذا فكر، لأي سبب من الأسباب، في استبدال الرئيس جياني إنفانتينو. إنه رائع، فقد ترأس للتو أنجح كأس عالم على الإطلاق، بأربع مرات. إذا رحل، فلن يكون ناجحًا أو مربحًا مرة أخرى! شكرًا لاهتمامكم بهذا الأمر.</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/naya_foriraq/87510" target="_blank">📅 05:11 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87509">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/drlar41wsqjzvo4xZuqKbBMJVpxgZt77ZGcWQu747_jIvRhwvVizykONzrEWX6iJe1-StS3rrhMP-F23aT3kYp4pmSPQM3jtPsf0RfWAAjyumwgxFn92gk2Gv6WWTxv__lGIMVq0ZuLth-0BBQNKj0_MQggr57iu5Mvw04_Um0jdpxEVrFEdc5-bg3kNB0jxc0Jt_H6CTC1LBeLd6FLHUZkG3sckUejYnQkhaucCUAsztzIjiXat4R_DG4h2aYLLEDHv06oh0rrogWYi6JuTD12xu30WjD-h5uxlAjjr0ZIx4ZeJNgGqDmHEyA8MmnjlXWUOObU92n86PG0Ay7Nc3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇾🇪
🇸🇦
القوات اليمنية تطلق موجة صواريخ نحو معسكرات مرتزقة السعودية في مدينة المخا.</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/naya_foriraq/87509" target="_blank">📅 05:09 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87508">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e6c0e1a2e.mp4?token=LGt-Y2K_rQje3Euy-mIHNKmdnOXUIyvVZRUOxMHmbdtEhu2N7UUKNStXfLsNuGrHRzevywdl6AUQcpiFxxDCJanWgXcuo-wq0nRDNpU3tsia-7MVpeHL0XaHf1wtuePwjwiE6iVTBQdYLKPdIVilF0BqIdpBAyh19ZHa6w4n5OAgVBBWQYImk5YvSlvELXMuJoA5vjwLGms42B_y3QYo-Ss3h5UQZkwDE3n0xNzuwHB7HD0LxDMZwuoJQxFWHtZZaSskwvmrVCd94KD50H8o62ofl3wIfY4U9ABZlHXZWyNZkRHEfAW5kOLuRA6vnlU_rjOgcqlM_jK0HTdoegaEPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e6c0e1a2e.mp4?token=LGt-Y2K_rQje3Euy-mIHNKmdnOXUIyvVZRUOxMHmbdtEhu2N7UUKNStXfLsNuGrHRzevywdl6AUQcpiFxxDCJanWgXcuo-wq0nRDNpU3tsia-7MVpeHL0XaHf1wtuePwjwiE6iVTBQdYLKPdIVilF0BqIdpBAyh19ZHa6w4n5OAgVBBWQYImk5YvSlvELXMuJoA5vjwLGms42B_y3QYo-Ss3h5UQZkwDE3n0xNzuwHB7HD0LxDMZwuoJQxFWHtZZaSskwvmrVCd94KD50H8o62ofl3wIfY4U9ABZlHXZWyNZkRHEfAW5kOLuRA6vnlU_rjOgcqlM_jK0HTdoegaEPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
اندلاع حريق كبير في مصنع خلط وتعبئة الزيوت بمدينة الزاوية الليبية إثر استهداف بمسيرة.</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/naya_foriraq/87508" target="_blank">📅 03:59 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87507">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ec3b4b656.mp4?token=Hzw-x76jVEyeJwWuihohN9r_QCOWep-iaXaVEJoh6mEf1rCb6ZCQPdTvtnvbXNzYDznJtii3hNxNQX3q-l9810qzJCDVSu5RIzhe9rkYc77KOM-Mu4fHOkXwkfCw_EfhYD4j8aOUsb8VVcDKM8iRBnnvW1LkqN3EmwSPNz5rAMTWC4VVKLOpJ9J1twNBhH1l2CtVfEK5i2vCsBfkgqkwNi4CVhHBOOjC_0NPXd9pM_E_tm29tHSXlH9Y0aXlbX39mMZo-_LNoMpWC3XTLe_c88pf9eV0lLOuJ0BuE1napgMfmIIxWqSGeMO-kwLhU3JjaH2c1e00XzncGBv3uMWAXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ec3b4b656.mp4?token=Hzw-x76jVEyeJwWuihohN9r_QCOWep-iaXaVEJoh6mEf1rCb6ZCQPdTvtnvbXNzYDznJtii3hNxNQX3q-l9810qzJCDVSu5RIzhe9rkYc77KOM-Mu4fHOkXwkfCw_EfhYD4j8aOUsb8VVcDKM8iRBnnvW1LkqN3EmwSPNz5rAMTWC4VVKLOpJ9J1twNBhH1l2CtVfEK5i2vCsBfkgqkwNi4CVhHBOOjC_0NPXd9pM_E_tm29tHSXlH9Y0aXlbX39mMZo-_LNoMpWC3XTLe_c88pf9eV0lLOuJ0BuE1napgMfmIIxWqSGeMO-kwLhU3JjaH2c1e00XzncGBv3uMWAXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇾🇪
🇸🇦
القوات اليمنية تطلق أسراب من المسيرات نحو معسكرات ومعاقل مرتزقة السعودية في مدينة المخا اليمنية.</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/naya_foriraq/87507" target="_blank">📅 02:59 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87506">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🔻
واشنطن بوست:
تم نقل الرئيس ترامب سرًا من أنقرة، تركيا، على متن طائرة من طراز C-32A تابعة للقوات الجوية الأمريكية الشهر الماضي، بعد قمة الناتو، وذلك بسبب تهديد إيراني باغتياله، بينما أصر البيت الأبيض علنًا على أنه كان مسافرًا على متن الطائرة الرئاسية "Air Force One" التقليدية.
في البداية، صعد ترامب إلى متن طائرة بوينج 747 أمام الكاميرات في مطار إسنبوغا في أنقرة، قبل أن يتم نقله سرًا إلى الطائرة الأصغر C-32A باستخدام شاحنة طعام تابعة للمطار. ثم أقلعت طائرة 747، وعلى متنها صحفيون وموظفو البيت الأبيض، بهدف تضليل المراقبين، بينما سافر ترامب ووزير الحرب هيغسيث بشكل منفصل إلى بريطانيا.
حلقت طائرة C-32A التابعة لترامب تحت رمز الاستدعاء العسكري غير المحدد "RCH18"، مع إيقاف تشغيل الأنظمة التي تسمح بتتبع الطائرة علنًا. وفي الوقت نفسه، استخدمت طائرة 747 المستخدمة كطعم في النهاية رمز الاستدعاء "AF1" على الرغم من عدم وجود ترامب على متنها.
بعد الوصول إلى قاعدة سلاح الجو الملكي في ميلنهال في بريطانيا، عاد ترامب إلى الطائرة الرئاسية "Air Force One" التقليدية قبل أن يظهر أمام الكاميرات، مما حافظ على الانطباع بأنه سافر على متنها من تركيا.</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/naya_foriraq/87506" target="_blank">📅 02:47 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87504">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8603ec3c72.mp4?token=nEtuVE2rK59pFhF-yAzCTJ4bDc6gXY8O1zMVbN0RDSXt1aPK-Q1gfLMqm3zNg5HU1RPaTjbsGatAFPNMB270M_SFZt0h8YhbXuM81pOPEMwnoSRP0pxFjlSK4Ier6kOcl_5htyq6IsApXVuSsTzayg9kuhZudKbs4vC9CrBdAxNWlPMY4qSqVXnhchP0O4JncluDJApaigbe2TcTTqr0bH4X0cjjHPKnnOAh1otFHP4fZlPrVEIs328Zdye3869L4axMHe7SNlPJ_uetEdlBbbysYImFxTOfEqWqzC1AwALizx2ffdeJptFYYDQqxBD2RfyyiFqjEHL9nZa0FsQTSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8603ec3c72.mp4?token=nEtuVE2rK59pFhF-yAzCTJ4bDc6gXY8O1zMVbN0RDSXt1aPK-Q1gfLMqm3zNg5HU1RPaTjbsGatAFPNMB270M_SFZt0h8YhbXuM81pOPEMwnoSRP0pxFjlSK4Ier6kOcl_5htyq6IsApXVuSsTzayg9kuhZudKbs4vC9CrBdAxNWlPMY4qSqVXnhchP0O4JncluDJApaigbe2TcTTqr0bH4X0cjjHPKnnOAh1otFHP4fZlPrVEIs328Zdye3869L4axMHe7SNlPJ_uetEdlBbbysYImFxTOfEqWqzC1AwALizx2ffdeJptFYYDQqxBD2RfyyiFqjEHL9nZa0FsQTSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
طيران مروحي مكثف يحلق في سماء مدينة كربلاء المقدسة.</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/naya_foriraq/87504" target="_blank">📅 02:03 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87503">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e67e2ac79b.mp4?token=vkFrnZ1P122HG02D4YLB2cTNvEsSk1mS0ThRbq8mMsRSjoF--I8OWcz8sX8Astm5g3UouzsefxCABO_5kRXlQclfbo6qFbWqoGeIk0PSXd3DbBbmlJ1HG7wHvGdNGiEvNoRgeIz4yYcpzHoJdBRUHsy8HOCnbL9Nd0yRe3uThaHDyF_MgcnIYPULZMC30qOIsU0Y6ztS2YxZkeFl08IYeGuTb36n3jv1bqFfBPkGMivc8PSofBuStUhbz0ab_Y7xpTfyn-zuqQGKkYTAT2YjXDAKpogI-m2YWVNlfajk65nJme0hPsEoD6_slXUBYibRATEOKBYw5gjfKVIhqfIrvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e67e2ac79b.mp4?token=vkFrnZ1P122HG02D4YLB2cTNvEsSk1mS0ThRbq8mMsRSjoF--I8OWcz8sX8Astm5g3UouzsefxCABO_5kRXlQclfbo6qFbWqoGeIk0PSXd3DbBbmlJ1HG7wHvGdNGiEvNoRgeIz4yYcpzHoJdBRUHsy8HOCnbL9Nd0yRe3uThaHDyF_MgcnIYPULZMC30qOIsU0Y6ztS2YxZkeFl08IYeGuTb36n3jv1bqFfBPkGMivc8PSofBuStUhbz0ab_Y7xpTfyn-zuqQGKkYTAT2YjXDAKpogI-m2YWVNlfajk65nJme0hPsEoD6_slXUBYibRATEOKBYw5gjfKVIhqfIrvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
هجوم جديد بطائرات مسيرة يستهدف مصانع مدينة الزاوية في ليبيا.</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/naya_foriraq/87503" target="_blank">📅 01:42 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87502">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">انفجارات في خزان وقود في مصفاة الزاوية في ليبيا ولم تُعرف طبيعة الانفجارات بعد.</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/naya_foriraq/87502" target="_blank">📅 01:39 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87501">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🇷🇺
🇺🇦
هجوم صاروخي روسي يستهدف العاصمة الأوكرانية كييف.</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/naya_foriraq/87501" target="_blank">📅 01:00 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87500">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SLsmnRPEMcZcV-I5CN6yTAfo2jv40hvwmxlbXw37LewvW2LKNSQYsmhmodFSYvPe4Y5KeKfljg5wyMiT9cFGnOxyWRUvZRkR1QjmwRyIDOxuEeq_JfKl-be8rVKSPydxj9lSdb-_9B9nRDUzNG79v9fuw6T5wlJN5ZxNQRCPDc42mfFhWx6oDY4_wxPbcB89toX5qmt4oupJLgJTQ0ZCQI3voNqSUHEH_MJARL6bA7rztXnmjpmePyLqeaK2XQCYUXuDNxP3xK1bWiZeGfVLGAjHkOtvNXfQ0P9ynW2Cuh_w32NzC1y7wkFC5BNnoydJd6sFcOjRWFMPkJ2krFlAyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
به نیابت از گروه‌های بسیج مردمی در عراق، انتصاب "شیخ ابوزینب" به سمت فرماندهی بسیج در جمهوری اسلامی ایران را تبریک عرض می‌نماییم، و تعهد می‌دهیم که بر مسیر رهبر شهید انقلاب، آیت‌الله سید علی خامنه‌ای، استوار بمانیم و پشت پرچم سید مجتبی خامنه‌ای باشیم تا زمانی که دشمن آمریکایی را در این منطقه به زانو درآوریم.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/naya_foriraq/87500" target="_blank">📅 00:37 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87497">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TRINn797FgXhRVQKOegLakjxdHE5Z3CsrqIM_vJG5vFSS4ZR56tmHOV1litSVicDi3qfYHJW_VEr9YkRYmo22Z9IAq-RtOa5DFZoawDuBrf4gB599LogVlf3iQ8Z3KWa8yLRb_UStFMfOP6drxBU5UBeUM9g5mw9PupklYV8aCbNYegoPUiTdIxGEsQLGTV0tx2fHzCm6A2sdVhU2Qh8fu0C_IN1otA-f4TF0Dk-AbmdLVo83vAHTiBt8N3kT9HYhBoty4Vu1F-ZKg4xlfQfW4hrGbN_Wqs7wV7xt4Q6InwwuaLE90wCdja5_sNSbwfEaVusegNCjk99ROySeLpq1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d2884ce92.mp4?token=PVa0uB_eM4yZShBFqdweyZWJkxV-v4Fj7BG4zMpWa3dT_rAgrgqElY33YGLAGi6bWuKK3tRc8xfseuxkuSsSjs_xq-NCMwpLtwrEwdSN_4ZZsEM6Vgcmm9uLKEP1ZRKZpHGiC7V2TslMduV5MZZ8v57tCGFN7ENfdY3yoLXUTxgnThKhwP5tH52t6jRrIatbqlS3lmWG4gaQwIPh7-W2Xnfhk6732YEC8QGD4TV8Q7NFQHCyxLnmCYVUODJqL4WyIIlqxU8AWAVGeStmQeAZqy4H7xqy-6RIkxlWetpTBIPqyPQ7SdsFXKokDYO-NFDCARnWoDFKhs2iUcRDH-WL_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d2884ce92.mp4?token=PVa0uB_eM4yZShBFqdweyZWJkxV-v4Fj7BG4zMpWa3dT_rAgrgqElY33YGLAGi6bWuKK3tRc8xfseuxkuSsSjs_xq-NCMwpLtwrEwdSN_4ZZsEM6Vgcmm9uLKEP1ZRKZpHGiC7V2TslMduV5MZZ8v57tCGFN7ENfdY3yoLXUTxgnThKhwP5tH52t6jRrIatbqlS3lmWG4gaQwIPh7-W2Xnfhk6732YEC8QGD4TV8Q7NFQHCyxLnmCYVUODJqL4WyIIlqxU8AWAVGeStmQeAZqy4H7xqy-6RIkxlWetpTBIPqyPQ7SdsFXKokDYO-NFDCARnWoDFKhs2iUcRDH-WL_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
احتجاجات واسعة وغلق عدة طرق من قبل المتظاهرين في محافظة واسط العراقية بخصوص تردي الكهرباء وخدمات اخرى.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/naya_foriraq/87497" target="_blank">📅 23:52 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87496">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">الاعلام السعودي:
قائد فيلق القدس إسماعيل قاآني يصل بغداد.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/naya_foriraq/87496" target="_blank">📅 23:46 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87495">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/107e5a4702.mp4?token=p4bVP11GZtfSorAG5mGYqp0PfxOdFKGkK7WYRzalb7s0_x-sLECMRBzz3m2y3qzTELPzngtTuHtXstLpLULNxSbwldiPcp_21oqgFu3LGYI5M-JsKRxGAx6bA4jPx0DkkYa1iM0i_5Vf6HPwiTyneK15bD3VZjhkpfjiz0V8gTflMfOBShInva4lmUDKdG80vy0EF890RLE06HIdoP7kCFR_4UazoQHgAbUCk0A06zJPIRlkcRi-EodE478jt5ujJiTVwIo2Xrg_yPTDhfyzYCoMwhG_wRMwPkO7BT0eNnHtwX1bb0-xiGKbDo336fev5Iv-5lnxZN8CdfLrCE2ZVrw1hx7A1FYo-ltFdkR-2DU9f1Fk2Pf82i3vD8RFEVqn4yx_eUFf6YeWWLz_zWNXkbXORt_KSYbY9_vhwsort6ZCr4p6M6sbmggao3FrQoVh1yzucsYdJjoAIMoBjtpSEo2E7wJEg7HJuhNRrPJWCUGvsRYTf_DtpIzTS_At2bSbmrD-PM1CARkD7evyEqXI0hnYuXx6z00eiCBM5s95SCal5RNppr8s5IrJkvxKE5qwt8NaxWNFFMHr9_i1gKUIr7ghLCwybkyn8NqCyS46VuUd-pCp5RcZveTweTU8oEIKi-Eg-RLwPzURcylQFZqs_J730T7HlzQHe5gNBFYf2Bk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/107e5a4702.mp4?token=p4bVP11GZtfSorAG5mGYqp0PfxOdFKGkK7WYRzalb7s0_x-sLECMRBzz3m2y3qzTELPzngtTuHtXstLpLULNxSbwldiPcp_21oqgFu3LGYI5M-JsKRxGAx6bA4jPx0DkkYa1iM0i_5Vf6HPwiTyneK15bD3VZjhkpfjiz0V8gTflMfOBShInva4lmUDKdG80vy0EF890RLE06HIdoP7kCFR_4UazoQHgAbUCk0A06zJPIRlkcRi-EodE478jt5ujJiTVwIo2Xrg_yPTDhfyzYCoMwhG_wRMwPkO7BT0eNnHtwX1bb0-xiGKbDo336fev5Iv-5lnxZN8CdfLrCE2ZVrw1hx7A1FYo-ltFdkR-2DU9f1Fk2Pf82i3vD8RFEVqn4yx_eUFf6YeWWLz_zWNXkbXORt_KSYbY9_vhwsort6ZCr4p6M6sbmggao3FrQoVh1yzucsYdJjoAIMoBjtpSEo2E7wJEg7HJuhNRrPJWCUGvsRYTf_DtpIzTS_At2bSbmrD-PM1CARkD7evyEqXI0hnYuXx6z00eiCBM5s95SCal5RNppr8s5IrJkvxKE5qwt8NaxWNFFMHr9_i1gKUIr7ghLCwybkyn8NqCyS46VuUd-pCp5RcZveTweTU8oEIKi-Eg-RLwPzURcylQFZqs_J730T7HlzQHe5gNBFYf2Bk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
‏ترامب بشأن إيران: ما زلنا نمتلك القدرة على التصعيد، ستطالب الولايات المتحدة بتعويضات مالية عن الأضرار التي ألحقتها إيران.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/naya_foriraq/87495" target="_blank">📅 23:04 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87494">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🇺🇸
🇸🇾
‏
الاعلام الاميركي
الوكالة الدولية ستزيل قريبا مواد نووية مخزنة في موقع سري بسوريا.</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/naya_foriraq/87494" target="_blank">📅 23:00 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87493">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af84017206.mp4?token=M3TOmFYeJv_RFqUPe17VIOm21rZ9iUGuYExg0kEg8oPsTAL987IMLV4ws0Jo4FHSncWP6WLSs78UmtD_noT7kLIftItnwv8z8UEBA-Nze8Jwr56ATeYcmj6iqr4yQY_Xik1CZe16mm4W5Ai-msqj6ck7D5YYKDn_Bi6bvHdNyW_4ztyFdiKulIHKlwVHXg8gclWwP6gHRGUQ8V-6jUKomG9r1esmPt3_WboQcAnh0YDAgmOdzPC72-UPArckf-L9L5jW0e4lbezK8U75ySS93im7owd1eSr8tkbXhRDp_C1uUVl8Yt4wGwiCHKNfWSelIvlt40oi5kL4q35b83pmhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af84017206.mp4?token=M3TOmFYeJv_RFqUPe17VIOm21rZ9iUGuYExg0kEg8oPsTAL987IMLV4ws0Jo4FHSncWP6WLSs78UmtD_noT7kLIftItnwv8z8UEBA-Nze8Jwr56ATeYcmj6iqr4yQY_Xik1CZe16mm4W5Ai-msqj6ck7D5YYKDn_Bi6bvHdNyW_4ztyFdiKulIHKlwVHXg8gclWwP6gHRGUQ8V-6jUKomG9r1esmPt3_WboQcAnh0YDAgmOdzPC72-UPArckf-L9L5jW0e4lbezK8U75ySS93im7owd1eSr8tkbXhRDp_C1uUVl8Yt4wGwiCHKNfWSelIvlt40oi5kL4q35b83pmhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
‏
ترامب بشأن إيران:
ما زلنا نمتلك القدرة على التصعيد، ستطالب الولايات المتحدة بتعويضات مالية عن الأضرار التي ألحقتها إيران.</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/naya_foriraq/87493" target="_blank">📅 22:55 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87492">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3123d44ff.mp4?token=rhEOgNtKq-OwHwfOrF5qZdmP5GFdymLz04T7hNOVK7qHS_fTBFohAn6advyhb0O6uje8-PUcdZ0N2dGkW0nhgw66oMlg67jRCjt8hkxvWk9R9Q3ZrWl6-mWS-II_tYmz_-j8U66z4hUjEp0jyGKiFYitcap47-cpUVTF5nDK7FraHwt5VxxyS4x0dNUM5s8Ud850cxd2jmpu3Yohh58vPS336dIhHAoavRE_ZccJ5fxvo-lh_7K3EQxM05sLz8or1bCVivXMtiftI2ZThrcDVmBJaqzdr65as9HUIRnNihZbbrlgiqBkMDU5h08uFqSvMwcsU4NAA5wV25Y2ZpJv9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3123d44ff.mp4?token=rhEOgNtKq-OwHwfOrF5qZdmP5GFdymLz04T7hNOVK7qHS_fTBFohAn6advyhb0O6uje8-PUcdZ0N2dGkW0nhgw66oMlg67jRCjt8hkxvWk9R9Q3ZrWl6-mWS-II_tYmz_-j8U66z4hUjEp0jyGKiFYitcap47-cpUVTF5nDK7FraHwt5VxxyS4x0dNUM5s8Ud850cxd2jmpu3Yohh58vPS336dIhHAoavRE_ZccJ5fxvo-lh_7K3EQxM05sLz8or1bCVivXMtiftI2ZThrcDVmBJaqzdr65as9HUIRnNihZbbrlgiqBkMDU5h08uFqSvMwcsU4NAA5wV25Y2ZpJv9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
الضربات الجوية التي دمرت 8 مضافات لعصابات داعش الارهابية في محافظة كركوك شمالي العراق.</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/naya_foriraq/87492" target="_blank">📅 22:20 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87491">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sUkHI8Fix5wHyFvexmhYR0q3dGg-_B07gxOJ35lgGAb_Ti65S7hK9E7V1Rt4NuLfZoQqC4Iav4z52Wqn6uyaY1DXXzn9rH6Ni09ef-ZvJR2F7QEykCjM87pyqCqQeHiG-owZryxoYO1EKBFbVzl_peWo4klZPwZxY3ZZdTWzBmR0NLzrXKPfKJ2EhwzrEK-ko6jtWpl-qOzUVvlcCnIUY-H7jMi4STC65isX7FLD40AG5mXktIVRnQcITe8qViD3ujU4iJso1xw0-htZduFk1U-eX-6NMeQDSuM2CPg1sx-F-WtUn-LO7VxnDV2I2DpMWplL8nSl5vwMd2FTD3-7zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وحيدي من جديد...</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/naya_foriraq/87491" target="_blank">📅 22:07 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87490">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75311b4b2d.mp4?token=LPb3Jj6j7jpazkhz-vEJ_wk0KzNDnfFnShdY9zZx4o6hr-wpsb3MatYMo0VDUTaQ3iz1rhlvwnIJg3PC2d8DRubhLaYSi6JQaIACEQHsjv-yd1xFW19ctwfoMYXbrLK7m_xIFhzWVrP4mrK0GFT4jGJJYWQIWh7Ze0Qv1_6TmWId4G2dmErnDSbcvsnPWFRdVTW3-VUrPAW0CtD4S_6L2YnMi4-bv4Zy9De1P9kW2P3hDdPK5XqQsp4ZNfPe5Fto4IdQ0C79FaYLAdMi7WBc2V5PrB2LOEZfDQdz9GwICq8tu0SNAqw0C80GBmrk38u4rspnK-RvC8NkcrRE_E8UkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75311b4b2d.mp4?token=LPb3Jj6j7jpazkhz-vEJ_wk0KzNDnfFnShdY9zZx4o6hr-wpsb3MatYMo0VDUTaQ3iz1rhlvwnIJg3PC2d8DRubhLaYSi6JQaIACEQHsjv-yd1xFW19ctwfoMYXbrLK7m_xIFhzWVrP4mrK0GFT4jGJJYWQIWh7Ze0Qv1_6TmWId4G2dmErnDSbcvsnPWFRdVTW3-VUrPAW0CtD4S_6L2YnMi4-bv4Zy9De1P9kW2P3hDdPK5XqQsp4ZNfPe5Fto4IdQ0C79FaYLAdMi7WBc2V5PrB2LOEZfDQdz9GwICq8tu0SNAqw0C80GBmrk38u4rspnK-RvC8NkcrRE_E8UkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">في ثاني حادثة في مصفاة الزاوية حرائق واسعة تطال المصفى عقب انفجارات مجهولة</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/naya_foriraq/87490" target="_blank">📅 21:58 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87489">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/658af79ef2.mp4?token=TC9uBm5UOJsLO87Mvnf3_B3MAAn8Ao16yC0xu7R3bJWpv9mkbASyu83toeLljKle84l9Nxp3czy2HojVd8MmgGdr1w2Yp4dLfUfKjAOg9Y8GdsefKTDEjnG8UhInhSuTRZWUHDJWPSAzfHZRonXDGLhJoqzq3U3fLOe0RqyKl1UUlbxEDijxaeJbLBpatwqFkFFggLyY4lMXd-1iYA79ylKGZ55E8NAijOVf-9Q1CRGNQjMyp_Q7j3GkoNE_p4I575UE9vWbi85sPveRrG5uA99PZEI-MnEe59t3ODX368tV4NPUyw8ECghY7IW9YO1y9Mt12Y3lB367OITVJPjcnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/658af79ef2.mp4?token=TC9uBm5UOJsLO87Mvnf3_B3MAAn8Ao16yC0xu7R3bJWpv9mkbASyu83toeLljKle84l9Nxp3czy2HojVd8MmgGdr1w2Yp4dLfUfKjAOg9Y8GdsefKTDEjnG8UhInhSuTRZWUHDJWPSAzfHZRonXDGLhJoqzq3U3fLOe0RqyKl1UUlbxEDijxaeJbLBpatwqFkFFggLyY4lMXd-1iYA79ylKGZ55E8NAijOVf-9Q1CRGNQjMyp_Q7j3GkoNE_p4I575UE9vWbi85sPveRrG5uA99PZEI-MnEe59t3ODX368tV4NPUyw8ECghY7IW9YO1y9Mt12Y3lB367OITVJPjcnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجارات في خزان وقود في مصفاة الزاوية في ليبيا ولم تُعرف طبيعة الانفجارات بعد.</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/naya_foriraq/87489" target="_blank">📅 21:56 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87488">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">انفجارات في خزان وقود في مصفاة الزاوية في ليبيا ولم تُعرف طبيعة الانفجارات بعد.</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/naya_foriraq/87488" target="_blank">📅 21:50 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87487">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd2e77472c.mp4?token=hEwMzTW87pSH9VXy7A5Q-kLJbYOp9ip739L747Sd27XrkiRU-N7-cULe3aY9AEpSF_rVSHhVBNFdEUqld_lR2xuwbMRIUUNMSTAwwj81-8JeL5whSGUB3olnCCslPaoqD3X47RNHYYA5AO0TU-lEc3b8NDZFu7Wxhj4w5cA5D5y_JKVKqYztxQlRXTmy3npzHN825J6CnxdpCgHePIq7OVBE9O3rUGbcVw0mfyb6tDv5Dh9zMRYXWmFcZXwWUMKbi7pXb9s4vGLBZhyZ2nZzYim6Oc5dg8UjjoMhQ8CvRoUij9rD7kjC1GHW8b7S6L8gSaRyYJIkNLE7fF_oOPzwEX-sz3ig50NOvRneWay91sUe7rh-MtV9St70SRhO-qyv0Z-6-4E1B18h2zPvGiZf5J7cpyrKjMDC52Ln-eVuJlV3lT_gyawSgqMUIkdxVF_Rbi0oFPkr5t3zkLU9tEXftjOClrZORw1ZqszyoiJOhAwovv-FchSvrUOWrol6ztB-whp3UZgxdL1O5pj9UmVLg_TSoij4ih-Da_OpuzIGx7Zpy4t51Tyg-bPYIjE6JbSWQsaQ-opBuBuNg3JpTlzn475WtE30NIwVEMT7h9aomFcznmWnGX9hHolUgJcFOD7ok8LOFwsATX15NuovhVoXRQe6vBQb2ROnq6a6CNf2BMY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd2e77472c.mp4?token=hEwMzTW87pSH9VXy7A5Q-kLJbYOp9ip739L747Sd27XrkiRU-N7-cULe3aY9AEpSF_rVSHhVBNFdEUqld_lR2xuwbMRIUUNMSTAwwj81-8JeL5whSGUB3olnCCslPaoqD3X47RNHYYA5AO0TU-lEc3b8NDZFu7Wxhj4w5cA5D5y_JKVKqYztxQlRXTmy3npzHN825J6CnxdpCgHePIq7OVBE9O3rUGbcVw0mfyb6tDv5Dh9zMRYXWmFcZXwWUMKbi7pXb9s4vGLBZhyZ2nZzYim6Oc5dg8UjjoMhQ8CvRoUij9rD7kjC1GHW8b7S6L8gSaRyYJIkNLE7fF_oOPzwEX-sz3ig50NOvRneWay91sUe7rh-MtV9St70SRhO-qyv0Z-6-4E1B18h2zPvGiZf5J7cpyrKjMDC52Ln-eVuJlV3lT_gyawSgqMUIkdxVF_Rbi0oFPkr5t3zkLU9tEXftjOClrZORw1ZqszyoiJOhAwovv-FchSvrUOWrol6ztB-whp3UZgxdL1O5pj9UmVLg_TSoij4ih-Da_OpuzIGx7Zpy4t51Tyg-bPYIjE6JbSWQsaQ-opBuBuNg3JpTlzn475WtE30NIwVEMT7h9aomFcznmWnGX9hHolUgJcFOD7ok8LOFwsATX15NuovhVoXRQe6vBQb2ROnq6a6CNf2BMY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🇺🇸
إيران جعلت ترامب يشعر بالخوف والقلق الشديدين، لدرجة أنه بات يحتاج إلى نظام دفاع جوي قصير المدى من طراز AN/TWQ-1، مزوّد برادار AN/MPQ-64 Sentinel، لمرافقته أثناء ممارسة رياضة الغولف.</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/naya_foriraq/87487" target="_blank">📅 21:43 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87486">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنايا احتياط</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f4213d8a3.mp4?token=L6KYnncsu2ttJ552NkviBtzx4LJzzu7-HI9yYoUrNlkpe0iCb6c80THoYSLJpo1OggrVjpsAG_jNIAHKiQAmrhHpR82LbC35tOjtr2L7_HooLQZer9ha8wRTp6V45Xl0mhwOJZPPhY8VlcU0SBQLMg9a72IEIKSCbHPSkBWeuzcTFEt8yiQGlntuG9mcpwMeF3U_fj_LqHbWPzGRStvXJ3uaScSUgl4kREV76hnJ5sI62o9oIVbvyBE88DSbbF8o02HodfIGnLe0yhXRRxjlzb_3hoJQUwPm1HzoAMJsz99Jm-bXM9c_Vro4VDj1ENdFZ2AT05rqwEo__uKTtBirGAbNty5mHC_mJzm2bymRYsYPA9VPfWTzHW1-7XY1ufrk195QvADTM1u7IxHNg4zBEoxKx9GBHDrfv9UbHr6DUWCy0k_deM0sRTuSMpRAEj6RugJwlbAzq-Ap6AYM0R-n0rbqhY1C3u3aSH1FdVRmclUGN1lTv2sJKtSkOMg6RdBamAiFql3zrJ5a3dNwNp8lJu8zQaeD8cITAODQp8-PE3e16eTCO7Nhm8tY_6tQtDJHDoJhlHLrqKo5E1dPkTMfi8SB3zgQT_xyDctc79hVSpadq83jMbMzUyVSIvR4AWvLHIX23WTM27buEYUdFcLGRT9OTpuyekCKLxi0eWTWLOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f4213d8a3.mp4?token=L6KYnncsu2ttJ552NkviBtzx4LJzzu7-HI9yYoUrNlkpe0iCb6c80THoYSLJpo1OggrVjpsAG_jNIAHKiQAmrhHpR82LbC35tOjtr2L7_HooLQZer9ha8wRTp6V45Xl0mhwOJZPPhY8VlcU0SBQLMg9a72IEIKSCbHPSkBWeuzcTFEt8yiQGlntuG9mcpwMeF3U_fj_LqHbWPzGRStvXJ3uaScSUgl4kREV76hnJ5sI62o9oIVbvyBE88DSbbF8o02HodfIGnLe0yhXRRxjlzb_3hoJQUwPm1HzoAMJsz99Jm-bXM9c_Vro4VDj1ENdFZ2AT05rqwEo__uKTtBirGAbNty5mHC_mJzm2bymRYsYPA9VPfWTzHW1-7XY1ufrk195QvADTM1u7IxHNg4zBEoxKx9GBHDrfv9UbHr6DUWCy0k_deM0sRTuSMpRAEj6RugJwlbAzq-Ap6AYM0R-n0rbqhY1C3u3aSH1FdVRmclUGN1lTv2sJKtSkOMg6RdBamAiFql3zrJ5a3dNwNp8lJu8zQaeD8cITAODQp8-PE3e16eTCO7Nhm8tY_6tQtDJHDoJhlHLrqKo5E1dPkTMfi8SB3zgQT_xyDctc79hVSpadq83jMbMzUyVSIvR4AWvLHIX23WTM27buEYUdFcLGRT9OTpuyekCKLxi0eWTWLOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد تُعرض للمرة الأولى توثق اللحظات الأولى لانتشال جثامين شهداء العـ ـدوان السعودي–الأمريكي على قطعات الحشد الشعبي، وتحديدًا في قاطع عمليات ديالى.
وقد صُوِّرت هذه اللقطات قبل وصول فرق الإنقاذ، علمًا أن مصوّر المشهد كان جريحًا لحظة توثيقها.</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/naya_foriraq/87486" target="_blank">📅 21:30 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87485">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WKkkAAMOYHXs0NFdsSbQOvsa-NOtuR8RSMJXJ6FbRb2vnKsK4D70XqCEfoNlP4yF4sDTp_NRpzIJYIGfxnn614FlYloXjKrZHvBRL-rXdT2p_BfHF0M0c1RkaAIJCtkgMLDQ3BU8kmjhQXObLBl27PRWiHc3RqyS-fL2ZvQppIQ6NgHMhxq4y5ayPempoJNrAzqcDVtQPSexbQeR1UcyQXsFx9oqcc37ULeqvaeTa4bXehiJ4P3ZXUPwPVSWBx9ssWLlbTBE6aTdm17YnX8Pv4zr-hRBVwBkkD20RXQheFuG2g1VgmvxkKEKUFVxrWQQxXsXI3oPZO31GNvh0TGdVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامب: أرى أن ممثلي الجمهورية الإسلامية الإيرانية يطالبون بتعويضات عن الأضرار التي لحقت بهم خلال النزاع العسكري الذي استمر خمسة أشهر (والذي بدأ لأنهم يرفضون امتلاك سلاح نووي)، على الرغم من أن هذا الأمر لم يُذكر قط في أي من مفاوضاتنا أو اجتماعاتنا! لكنها…</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/naya_foriraq/87485" target="_blank">📅 21:11 · 19 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
