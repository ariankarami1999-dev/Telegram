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
<img src="https://cdn4.telesco.pe/file/iFvL30BFbhQ9ClRko5oSss88pc8z7X27-jE7x8_eRITLJSIlIp9ptk9CyGQiDMu7aegndMlxtbCzjsnwO6-bY4QpO0EZ9N8rJqu7MmcW74LVhO0-1gBYY13ytDYA2gFyR7UMUAEyO-zz7jtVSnSlD7LLNASoT_xlfDnjN6pW2L3T6HX3SaWGaxJLJPcSjjtOHc7wJZUuTSuvO0cSo9i_AVhXtnJQV41jbJYH51qOeZc1pl4_fQ-7ZkDl0oigQUQA2kBEyzZTVMnjiV-J9s--HqgK74RtwdmJZJMw1isY7KNi8-XSHRrzgmI7r0byQ0oxeWBs1MxIK60RwwptBSUz1Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Secret Box</h1>
<p>@SBoxxx • 👥 10.7K عضو</p>
<a href="https://t.me/SBoxxx" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ■  تاریخ | ژئوپلتیک | بازارهای مالی ■https://secretboxxx.com/</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-18 19:06:53</div>
<hr>

<div class="tg-post" id="msg-20726">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک + تقویم اقتصادی امروز در سطح بالایی قرار دارد و فروش توصیه می شود.</div>
<div class="tg-footer">👁️ 952 · <a href="https://t.me/SBoxxx/20726" target="_blank">📅 18:54 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20725">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">یک روزنامه ترکی:
عربستان سعودی از پاکستان خواسته است که در عملیات نظامی علیه انصارالله شرکت کند و مداخله نماید.</div>
<div class="tg-footer">👁️ 1.94K · <a href="https://t.me/SBoxxx/20725" target="_blank">📅 18:07 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20724">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a244fd3e09.mp4?token=oHlTndrCO5LsrQ8kPn8F917HCpKpdijLxhmMzPO49_ZZ_8k2-EhFQa2b7Xef1vt-Pa7fVZt1q0BF4ECDQF_Wf0wFBNf7zZAmT4P63viI_cSrZeN3A41iFztBXcNkRpcoS0rceKw-69BBTntXdGJppouHvr-QynrO26murivi4yWWsb8SQ4Ro4A6b3A_JkjD7CNrRvk4CSf08L1ulnVfZGurpZZiENi-U9yRgyggWk7lc98GlVE1kbldzz_3OrQtrV3_2oqtdu-wqv14j3qAT6rXM_0xpEaIchF90ciFhKumePp4TDqSFGua0WcGmFo9qLZP8mmClI_FAflk0Q6zqfgC5ixupAZ07YXURuwljtnKI8EuqwZglBkfetXsnIBP-LImorfj8CNcsxDu14CQmWqfSmRZxWylzSnvv-ZLNEWGRNL8opzeXgUDWadZI4ioq79M9KFX44nxYG_KrA4sPN5PQ3qZ1wX9Zim-A6qArSEarrRqWr9p2VgNW-P7dG1GXu3Rgh86gnlNPck4OY5hlAAa0ctUz-9mxABWGwu6hFuTlqqBqg6CARzwI_U9FBR3-G_-dKUtu9jkyoABYq7b4QR2fHdgg0zOXzHZY2eI73S-TYo2GtQV9Ohsswh1muH79cOSHjHtYo4QEqoWs9L3Y-1HOH3g_rKlK_BcI8sf_qcI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a244fd3e09.mp4?token=oHlTndrCO5LsrQ8kPn8F917HCpKpdijLxhmMzPO49_ZZ_8k2-EhFQa2b7Xef1vt-Pa7fVZt1q0BF4ECDQF_Wf0wFBNf7zZAmT4P63viI_cSrZeN3A41iFztBXcNkRpcoS0rceKw-69BBTntXdGJppouHvr-QynrO26murivi4yWWsb8SQ4Ro4A6b3A_JkjD7CNrRvk4CSf08L1ulnVfZGurpZZiENi-U9yRgyggWk7lc98GlVE1kbldzz_3OrQtrV3_2oqtdu-wqv14j3qAT6rXM_0xpEaIchF90ciFhKumePp4TDqSFGua0WcGmFo9qLZP8mmClI_FAflk0Q6zqfgC5ixupAZ07YXURuwljtnKI8EuqwZglBkfetXsnIBP-LImorfj8CNcsxDu14CQmWqfSmRZxWylzSnvv-ZLNEWGRNL8opzeXgUDWadZI4ioq79M9KFX44nxYG_KrA4sPN5PQ3qZ1wX9Zim-A6qArSEarrRqWr9p2VgNW-P7dG1GXu3Rgh86gnlNPck4OY5hlAAa0ctUz-9mxABWGwu6hFuTlqqBqg6CARzwI_U9FBR3-G_-dKUtu9jkyoABYq7b4QR2fHdgg0zOXzHZY2eI73S-TYo2GtQV9Ohsswh1muH79cOSHjHtYo4QEqoWs9L3Y-1HOH3g_rKlK_BcI8sf_qcI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آمریکایی ها عموما از اوضاع جهان بی اطلاع هستند و خصوصا سیاه پوست هایشان که رسما توی دیوارند!
اینجا این منگل در پاسخ به این که چرا به ایران حمله کردیم می‌گوید چون ایران داشت نفت ما را از زمین میدزدید!</div>
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/SBoxxx/20724" target="_blank">📅 17:45 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20723">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">منابع محلی:
بیش از ۱۵ تروریست هیئت تحریر الشام (HTS) در پی انفجار انبار مهمات در حومه شمالی ادلب کشته و زخمی شدند.</div>
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/SBoxxx/20723" target="_blank">📅 17:41 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20722">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">خر تو خر در یمن!
نیروهای ائتلاف جنوب مورد حمایت امارات امروز سعی کردند طاهر العقیلی وزیر دفاع یمن را که مورد حمایت عربستان است، گروگان بگیرند!</div>
<div class="tg-footer">👁️ 2.77K · <a href="https://t.me/SBoxxx/20722" target="_blank">📅 17:35 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20713">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآرش رئیسی‌نژاد</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p0e7HeRAEhDSJFq5WQAtroo-g5DEIFa9ezVKMpXBBUy_fWp3Ra3Bjompe6s0lWyHPJu_t8gnTYV9zBWq2aKZhmeFrQ6d8ksSKdcZ-xeiDL5bIlWwFfIIgoWDZQOz211hIR4mlyKR7acBkvnkuzklbi4S1I6eXWMENWUqa2L-FBfTBJaYx-y9NWKBJKl96WwpqgVivrr_YaQUYa3OfGcxaQtlIyHv6_RaQjkI6zdO5ZSQWj-JYjY2Ib9MvGc2sfJDTQMsGvdP6aS8Acl7ytH-4kVz_9Vf8xTYx70PzwENtZONnSMya54F9Mlmc1C3laVpPtguOkKgO8jcg71s_r5mcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UoOQT375zfRrhT6YU4gDCIDTqvlENgxazX52UMXC_xSRZE8Q-SMuIjqEC9u3yemJD4m1uGwoiwyC1JqPtdvHBZd9cOVqwugm8VM3Gpszp7o1kV4_rhLwX3lwH2GRdPHd7H5NvXIpn1BsW-03ia7Lr0xOfr_hmbX6EeQM4ZG230DmzcAypJv5fyqvoJ9OaV0PGsj_Js37naxy7qfS5W1xorHRPADjc-YFWozkEa9dUqqzqilElteg0z8hcXPV3lOSuB9CzdH9x7y3M16ssGNd38_NrO57SFl6kR2m3jp7o6cy2cM6wUwcVE_vkj4JT6NC8m5meHr7vvDY4ZvtzyYBSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/alWXy6HErgWsscX0RIUoQjtWUhraZWm6_ZodJ74GX8Q5lB6DtrZG42cOwHLuzZ2NIjmMGHUcjzaVA7U531wQSHraiEHGwQbdZ5vt9HyY7dniJNe6OhORT8w9OYfugefCzpadD8tce3HuICQI7Ou_3qvjnXD7SuQMJgZUewUw-ozMftzHmt5bwKnP7f-Rhg9eqaYk-s85YwsuXhwHd5FuVJnm3-U0RIMxqyl870vYi2PHqmd8U1oZBhjI7WjgNnDGmd9w_Pt20hI2MyFiMoPyUlfcq5bEK4gquAwjMSiUGdyV_Eqr2-Gp9jGknPYBbJxPCirJapFbC815wJkIfYuifQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ewOAXSexuf4UUh-P9dPg7rdp9k07Om3GVbmXmqJzKmgZg-cJVU9rS_F4BX9S-JVYdNHAQtc7gd4HeAidDTjyhgwG4i8SAtyqE7m4ZcfRK--I9Q0murxoGG9BO0MXvy3Vy2Sm-YeNNjb-lL8nwbbTcalAc5OOvA99gVJyXfFZ5PMMYMAMfyQyJGNI6f1mQXOKEsRoHNkQWUwQPvPTTB7iZg1zrzzUWbvi1TpOluBN_pS9kt2I3ZPvERZvYTMGDjWwb_xN0PxMCtyCOvlmsIscC6pHXf20Qq8GD4TZ9jb_03MINsSXtzRDA6YTEeVCu5QYrJ9VwdPwN9OtxxuQcQtFTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/E9tT2ntY3VhdLC5RaOeDSvxluWGEUD_2MLccOZhrCQKxo4iD_3rUiMr7YbyKh5AUiUUR6QmoZKSulqOr5DlHWp1QRo4MinnD0MX0u7PN5p_NbEUfI7J6HIdN13scJJbj1yE-b8dzu6KqG2zSIu-wjII7eOB5763xQ0IL0-vbXk3CXBTyZiBH7s_otQCG_GlntKIc_MNPd5HLNx5dmGRLCXaxDuDSnQfzqswJEE7iPz9ugrfupTxk1BEbdpzOyMUmic7Y4r9TUCs7BPybNxMYOrLFMiCRQpC7VXv9oN-NxC75NOvsV9mYYjwp_or_EFHToxXSolQRk3-KRCfTkVfcCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vDiZDs45EL0rwEcJDhStt6a0zLltzPF9gm_iEn6Dp8zr-Kx8JBRQJGvT811ARU_BaJCC6vOhymkyGpO2l2FMnlLscW3bMBGbC6yVbyP8yGztVOdNN1hjTCuHqt8skO42wIxWw_jYM1yrWo6sZbcCdgcfB5aARhqtAGlDXv_jwvHHQEBh1eJ24gtWPkHexOzvskL3gcO9siywAXmCKUAUk0iFWMBWpYO3j-Obl_9tu2hIyBG5NE4L5ZHsrBWWSXCwgHdX9tC8W4SuRFIPIgvcjnxsBOwGuYM_C3O53CLfIaGMVgUBysyhTM_Nah_ml2qlyZaEhuRMigrKWMBhQ2x3wA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hh47I7xQv6RFubpDxfA0azzfCYO_bR8tV-YVopbSFovzXrkqF2Bm7ayHKN3TiTGk6SqKvumI5K2BJ3OuOFsZMVhB7DPgP3jyi0ZkMQQ_-5y6qSpfs_0MUvzAXQ7ZuxqnjO12Z1uZt8Ylr7mpbf-C6CxYYRX9-CS6L188ViW1XIUNFY87TlRjzA6rNAtpohiRhJ9DPw3a3m6pifGaqrADxy2kbyS2yp8CZorELRaEBJAAdkgq_vt_36EQ61mDiN-d8c18V1nB-0zluGhnilGzEJKoMBV7O9dRsEvaUsquhVzurikPRoloqurpAn5GEB-7aydKWw7KQ_AFK6tTQ8KsUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cPsCF5mB6-LNtH-QWjvWGG6mCTHozyR8fsvAH9RR-e-6AhLY-Ebk0g5mobWsp_RFL-1hV85AL0pYoV1V-RQmUgL56HvVSXwEXwMrPDeEzCQ8hrWC6Rk5CDqdLGR7e5lQ4LriWgcP5Ud5sfFSnhNebWmyfuSBkGPCthZmSwqKaoXdfKD-FXJkr4ED3QbTdIbDPqnIvgYLM_YNJAKbeaOmdlWnzIYphOrjw5KAUXSzrh6pNgcYRXfBV1bFeUj9zux3YAd_jkLrQ-fwTXjpdJ03grXRwWloEviOOV0Z0r_Wp5xxfqPL8Kf6yCGK9STs1n9r78v7NdvCB6fiSo-mbbIIIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lrbbsF93rxFVsuLH0y_KP08Z1iO5kfYJRiqtIHtfeC3SmY4It0JC6w7ccJb2DXjUJjgiv1G00uIk4W8erzNgwiaIajRqRED6uDliGFek4UGrUo7zYFffMBs0XOQbwnqiO1wdG8c3ueqDn_NcDzQIDNDqHzlBYPrageOgQ7Qa2U7wHjl9m0VvidZKJip9yAgpy9CJGrLjIFesMtMGfQO5k94L5jnAXCWBpc-5e33QpbtfKlPX0xtr0GBMgcCWtFELMMi2MsG2g0V0Y2VEehrvnG6KxhRZ-nuuAb9hIWsWeW6JJMjN0CPI0Ckmhuxu6pM-b_UedNtS2_JtlcTDLjD2lg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">در دره پنجشیر، یک تنه در برابر ارتش سرخ شوروی ایستاد، آنگاه که کل افغانستان زیر سیطره رژیم کمونیستی کابل درآمده بود. در میانه جنگ‌های داخلی، کوشید که ثبات بر این کشور گسیخته‌از‌هم حاکم شود؛ اما نشد. تا انکه طالبان شهرهای افغانستان را یک به یک تسخیر کردند. این بار نیز در پنجشیر جانانه ایستاد، آنگاه که دست یاری‌کننده‌ای را نمی‌یافت.
در میانه سال‌های جنگ، روزی در تخار در شمال غرب افغانستان، در جمع مجاهدین و خبرنگاران نشسته بود و دیوان حافظ شیرازی را می‌خواند که خبر آوردند طالبان در منطقه‌ای حمله کرده و در حال پیشروی است. مسعود توجهی نکرد و به خواندن دیوان حافظ با عشق ادامه داد. یکی از فرماندهان از بی تفاوتی مسعود ناراحت شد و با صدای بلند گفت: آمر صاحب! طالبان حمله کرده اند. مسعود گفت: بگذار که این غزل را تمام کنم، مگر نمی دانی که جنگ با ما بر سر حافظ است؟!»
۲۵ سال پیش در چنین روزی، احمد شاه مسعود، شیر دره پنجشیر و قهرمان ملی افغانستان، ترور شد و جان خود را از دست بداد!⁩
@Iran_Simorq</div>
<div class="tg-footer">👁️ 2.45K · <a href="https://t.me/SBoxxx/20713" target="_blank">📅 17:19 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20712">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">نتانیاهو رفته از جنوب لبنان بازدید کرده!  از این جهت خیلی شبیه احمدی نژاد است؛   منتهی احمدی نژاد سفرهای استانی اش به شهرهای ایران بود اما نتانیاهو عمدتاً به مناطق تصرف شده کشورهای دیگر سفر می کند (غزه، سوریه، لبنان....)</div>
<div class="tg-footer">👁️ 2.49K · <a href="https://t.me/SBoxxx/20712" target="_blank">📅 17:09 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20711">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">منابع خارجی:
بر اساس تحلیلی که از بررسی تصاویر ماهواره‌ای به دست آمده است، در سال جاری شاهد افزایشی در ساخت‌وساز در محل زیرزمینی مشکوک هسته‌ای ایران در نزدیکی نطنز بوده‌ایم.</div>
<div class="tg-footer">👁️ 2.5K · <a href="https://t.me/SBoxxx/20711" target="_blank">📅 17:06 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20710">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">وزیر خارجه یونان، جورج گِراپتِریس، درباره ترکیه:
«ما درک می‌کنیم که این نوع تنش‌های بالا که اغلب از سوی محافلی در ترکیه همسایه می‌بینیم، همچنین به این دلیل است که یونان به قدرت واقعی دست یافته است — صدایی که بیش از هر زمان دیگر شنیده می‌شود.
من فقط می‌خواهم اشاره کنم که هر کسی که فریاد می‌زند، همیشه قوی‌ترین نیست. در واقع، اغلب آن فرد ضعیف است.»</div>
<div class="tg-footer">👁️ 3.08K · <a href="https://t.me/SBoxxx/20710" target="_blank">📅 15:58 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20709">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-footer">👁️ 3.07K · <a href="https://t.me/SBoxxx/20709" target="_blank">📅 15:56 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20708">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">ولادیمیر پوتین، رئیس‌جمهور روسیه، و دونالد ترامپ، رئیس‌جمهور ایالات متحده، درباره ایده برگزاری یک نشست سه‌جانبه با شی جین‌پینگ، رئیس‌جمهور چین، بحث کردند.</div>
<div class="tg-footer">👁️ 3.18K · <a href="https://t.me/SBoxxx/20708" target="_blank">📅 15:43 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20707">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d_3n0ZhRP51iBVwkzWMayG0cxtuPzKpUDSNVsWwhIdz3Q97E7eA30Q2g47mC3lVIOrs3jD06OrAWEIoTlqzhq9YIkcFdfXaDgy9pESKdbVd1pC4mOnAmsn4m_I9GxAMP4jA_tvwEqndPopmVfJ-Nt44o87UfVEWZap0SgAYDFuntkXmD6j0zGg4FXPFnn6NqXqNlF9i5w19jgwFv846Fa_kgmob82wQKWLgEIviQs_GnYONFZDsbuAfXSWXhnUK8lPajQbEKF9x1-Dg4lqYuzH5U8Oo7MSADYviQplALBEB0flwnDzvXD6bt6rqzidrr7vN_JNduomkZ9YrNLzF0aQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولادیمیر پوتین، رئیس‌جمهور روسیه، و دونالد ترامپ، رئیس‌جمهور ایالات متحده، درباره ایده برگزاری یک نشست سه‌جانبه با شی جین‌پینگ، رئیس‌جمهور چین، بحث کردند.</div>
<div class="tg-footer">👁️ 3.21K · <a href="https://t.me/SBoxxx/20707" target="_blank">📅 15:43 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20706">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">سخنگوی سپاه:
هر کشتی که از منطقهٔ ممنوعهٔ تنگهٔ هرمز عبور کند تحریم می‌شود
در صورت عبور هر شناوری از محدودهٔ تحریمی تنگهٔ هرمز که مختصات دقیق آن اعلام خواهد شد، ارائهٔ هرگونه خدمات دریایی، بیمه‌ای و پشتیبانی به آن شناور متوقف می‌شود؛ به‌گونه‌ای که حتی در صورت تردد بعدی در تنگهٔ هرمز نیز از دریافت این خدمات محروم خواهد شد.
منطقهٔ تحریمی تقریبا از سمت چابهار شروع و تا بخشی‌از دریای عمان و دریای عرب ادامه دارد.</div>
<div class="tg-footer">👁️ 3.4K · <a href="https://t.me/SBoxxx/20706" target="_blank">📅 15:23 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20705">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">این تحلیل برای 1 اردیبهشت است. تارگت من برای قبل عید 150 هزار تومان بود و تصورم این بود که از یکی دو هفته پیش یک اصلاح موقت بزند تا حدود 120 تومان که این پارت آخر نشد.  با این شتاب، اگر 150 تومان را رد کند تارگت مرکز تحقیقات مجلس در 240 تومان را فعال خواهدکرد…</div>
<div class="tg-footer">👁️ 3.38K · <a href="https://t.me/SBoxxx/20705" target="_blank">📅 15:21 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20704">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">شروط ایران برای پایان جنگ توسط سخنگوی سپاه اعلام شد:
۱- ضمن توقف کامل جنگ،
۲- از تهدید مجدد دست بکشد،
۳- ارتش اسرائیل از لبنان عقب‌نشینی کند،
۴- محاصرهٔ یمن پایان یابد،
۵- ۲۴ میلیارد دلار دارایی مسدودشدهٔ ایران آزاد شود
۶- و از هرگونه مداخله در توان هسته‌ای و موشکی کشور دست بردارد.</div>
<div class="tg-footer">👁️ 3.75K · <a href="https://t.me/SBoxxx/20704" target="_blank">📅 15:09 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20703">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XIOhom-wib4S3oNx9a1r4CDtcBw-jmLpCg7QXAvkfZe2LTERUgCTXByAgvLV7c8vqEut4yj39QtYVsiE5o-vngyB9To_Fc00BUjDjH2yrW-j-BCTkympNwfeVWw-J1CZukz2lZ8le_mk04uNrUeQ8sadkUvmKR3lpok2NMJDFEypZ9mXNwYaGn8fH5xBAp1oJYbx-tHPr8cwamwc5kQIWjXL6S1-GQ7osMSpo_l-cAJ64r3XwgIGcH5ELs6NFTAcSWyjN_dAxv_XPQ2tOHqYhB_cPdsu2luuT8639i_t28mHcofVWfupIVz78mXaHcLl9SOsHYFuvaotLmH8_CdxLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صحبت های رهبر حزب AfD درباره برنامه های اجرایی این حزب  دقیقا کپی برنامه های خاویر میلی در آرژانتین به اضافه:  — کاهش حمایت از اوکراین  — مبارزه با مهاجرت بی رویه</div>
<div class="tg-footer">👁️ 3.75K · <a href="https://t.me/SBoxxx/20703" target="_blank">📅 14:29 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20702">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">‏اکانت صابرین نیوز در توئیتر:   حداقل ۴ آمریکایی در حملات دیشب به هلاکت رسیدند</div>
<div class="tg-footer">👁️ 3.92K · <a href="https://t.me/SBoxxx/20702" target="_blank">📅 13:59 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20701">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">‏
اکانت صابرین نیوز در توئیتر:
حداقل ۴ آمریکایی در حملات دیشب به هلاکت رسیدند</div>
<div class="tg-footer">👁️ 3.94K · <a href="https://t.me/SBoxxx/20701" target="_blank">📅 13:57 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20699">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">شعارهای شب گذشته امت مبعوث در تجمعات شبانه
تو تاریکی می‌نشینیم، ذلت نمی‌پذیریم.
بنزین رو کم میگیریم، ذلت نمی‌پذیریم.
دلاری گوشت میگیریم، ذلت نمی‌پذیریم.
مهریه کم میگیریم، ذلت نمی پذیریم.</div>
<div class="tg-footer">👁️ 4.44K · <a href="https://t.me/SBoxxx/20699" target="_blank">📅 13:35 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20698">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک + تقویم اقتصادی امروز در سطح بالایی قرار دارد و فروش توصیه می شود.</div>
<div class="tg-footer">👁️ 4.17K · <a href="https://t.me/SBoxxx/20698" target="_blank">📅 13:19 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20697">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OcK33qKfcuPrcLMIsVdR7A4NTsmJwl0mlGX8ljiMjZKWQLKRU5FCmgFQXvc4B6_0_-EXP7PkkdSdsau3E2_M2PaWa3n73aGUFPGmQvrkDMx3xTZBibGC9GrGdpauxE_w1a1MaQSe3Fap4p7ck0Kjh_tWp5uJNY33KpG7dtK0pbUMNi5MWmKr_NcGknMrrxkXhl9TQ2c8UNM2nzjUMY7_UpMuijaEJXffDQQAHmn3U3yIJuK4WTz43z1bhhBOzmgGVMkff94lCviuwG6zHHFXipXwdLoL2Cnc7nZ9jdxbZqS4_lw7qT3Jj1-vMpnofXaQ1xqNNjxtrw5kaX6oLVA8QA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک + تقویم اقتصادی امروز در سطح بالایی قرار دارد و فروش توصیه می شود.</div>
<div class="tg-footer">👁️ 4.34K · <a href="https://t.me/SBoxxx/20697" target="_blank">📅 11:36 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20696">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">وال استریت ژورنال:
تلاش‌های اخیر ایران برای هدف قرار دادن تجهیزات نیروی دریایی آمریکا این نگرانی را ایجاد می‌کند که ارتش این کشور از سلاح‌های پیشرفته‌تری استفاده می‌کند و ممکن است از چین یا روسیه کمک دریافت کند.</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/SBoxxx/20696" target="_blank">📅 09:09 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20695">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">جنگ اراده‌ها در تنگه هرمز؛ ایران و آمریکا چه کسی زودتر عقب‌نشینی می‌کند؟
جنگ ایران و آمریکا وارد مرحله‌ای شده است که در آن، اقتصاد به اندازه موشک و نیروی دریایی به سلاح جنگی تبدیل شده است. تهران و واشنگتن هر دو تلاش می‌کنند هزینه‌های ادامه جنگ را به طرف مقابل تحمیل کنند و در نهایت او را به این نتیجه برسانند که ادامه درگیری بیش از دستاوردهای آن هزینه دارد. به همین دلیل، آنچه اکنون در اطراف تنگه هرمز جریان دارد، صرفاً یک رویارویی نظامی نیست؛ بلکه یک جنگ اراده‌ها است که در آن هر دو طرف منتظرند دیگری زودتر تسلیم فشار شود.
از یک سو، ایالات متحده با ایجاد محاصره دریایی و هدف قرار دادن برخی زیرساخت‌ها و نفتکش‌های ایرانی تلاش می‌کند صادرات نفت ایران را محدود کرده و فشار اقتصادی بر جمهوری اسلامی را افزایش دهد. از سوی دیگر، ایران با تهدید شناورهای آمریکایی، ایجاد محدودیت برای کشتیرانی و تلاش برای افزایش هزینه عبور کشتی‌های تجاری از تنگه هرمز می‌کوشد هزینه اجرای محاصره را برای واشنگتن بالا ببرد.
ایران؛ فشار بر مهم‌ترین منبع درآمد
برای تهران، مسئله اصلی اقتصاد است. نفت همچنان مهم‌ترین منبع درآمد جمهوری اسلامی محسوب می‌شود و محاصره دریایی آمریکا مستقیماً توانایی ایران برای صادرات نفت را هدف گرفته است.
بر اساس گزارش شرکت Kpler، حجم نفت خام ایران که روی نفتکش‌های خارج از منطقه محاصره ذخیره شده بود، از حدود ۹۰ میلیون بشکه در اواسط ژوئیه به حدود ۲۹ میلیون بشکه کاهش یافته است. اگر این روند ادامه پیدا کند، فشار بر درآمدهای ارزی ایران افزایش خواهد یافت و دولت برای تأمین هزینه‌های جاری و واردات با محدودیت بیشتری مواجه خواهد شد.
اما فشار اقتصادی تنها در سطح صادرات نفت باقی نمانده است. دولت ایران هم‌زمان مجبور شده قیمت بنزین در بالاترین سطح سهمیه‌بندی را به ۱۰۰ هزار ریال در هر لیتر افزایش دهد. این تصمیم از این جهت اهمیت دارد که افزایش قیمت سوخت در سال 1398 به اعتراضات گسترده در سراسر کشور منجر شد.
بنابراین، تهران با یک معادله دشوار مواجه است: اگر در برابر فشار آمریکا عقب‌نشینی کند، بخشی از دستاورد استراتژیک خود در تنگه هرمز را از دست می‌دهد؛ اما اگر مقاومت را ادامه دهد، فشار اقتصادی و احتمال نارضایتی داخلی افزایش خواهد یافت.
آمریکا نیز هزینه جنگ را می‌پردازد
با این حال، تصور اینکه تنها ایران در حال پرداخت هزینه اقتصادی جنگ است، اشتباه خواهد بود.
بر اساس برآورد لحظه‌ای دانشگاه براون، جنگ تاکنون حدود ۱۰۰ میلیارد دلار هزینه اضافی انرژی بر مصرف‌کنندگان آمریکایی تحمیل کرده است. این رقم با سرعتی حدود یک میلیون دلار در هر دو دقیقه در حال افزایش بوده است. به‌طور متوسط، افزایش قیمت بنزین و گازوئیل از زمان آغاز جنگ بیش از ۷۶۰ دلار هزینه اضافی برای هر خانوار آمریکایی ایجاد کرده است.
فشار اصلی در هفته‌های اخیر از سوی بازار گازوئیل آمده است. قیمت گازوئیل در آمریکا به حدود ۵.۹۰ دلار در هر گالن رسیده؛ یعنی تقریباً ۶۰ درصد بیشتر از یک سال قبل. اهمیت گازوئیل بسیار فراتر از هزینه سوخت خودروهاست، زیرا بخش بزرگی از سیستم حمل‌ونقل کالا، کامیون‌ها، کشاورزی و زنجیره تأمین به آن وابسته است.
در نتیجه، تداوم قیمت بالای انرژی می‌تواند به موج دوم تورمی در اقتصاد آمریکا منجر شود؛ از افزایش هزینه حمل‌ونقل گرفته تا افزایش قیمت مواد غذایی و کالاهای مصرفی.
تنگه هرمز؛ میدان اصلی جنگ اراده‌ها
اینجاست که اهمیت تنگه هرمز دوچندان می‌شود. ایران می‌داند که نمی‌تواند الزاماً آمریکا را از نظر نظامی شکست دهد، اما می‌تواند تلاش کند هزینه پیروزی آمریکا را بالا ببرد.
حمله موشکی ایران در ۵ سپتامبر به سمت دو شناور آمریکایی، هرچند بدون اصابت و تلفات بود، دقیقاً در همین چارچوب قابل تحلیل است. تهران می‌خواهد به واشنگتن نشان دهد که اجرای محاصره هزینه نظامی دارد.
در مقابل، آمریکا تلاش می‌کند با اسکورت کشتی‌های تجاری از مسیر جنوبی تنگه، نشان دهد که ایران نمی‌تواند به‌تنهایی قواعد عبور و مرور در هرمز را تعیین کند.
اقدام ایران برای ایجاد یک «منطقه محدودشده» نیز بخشی از همین رقابت است. تهران می‌خواهد کشتی‌هایی را که از کنترل ایران عبور می‌کنند، با تهدید به قرار گرفتن در فهرست کشتی‌های غیرمطیع، جریمه، توقیف یا حتی مصادره، تحت فشار قرار دهد.
بنابراین، هر دو طرف در حال تلاش برای تغییر محاسبه هزینه ـ فایده طرف مقابل هستند. جنگی که هر دو طرف می‌خواهند دیگری آن را تمام کند. ماهیت این جنگ را می‌توان در یک جمله خلاصه کرد: ایران می‌خواهد آمریکا زودتر از محاصره عقب‌نشینی کند؛ آمریکا می‌خواهد ایران زودتر از استفاده مؤثر از تنگه هرمز دست بکشد.
واشنگتن امیدوار است فشار اقتصادی، کاهش درآمدهای نفتی و تهدید ناآرامی داخلی، تهران را مجبور به پذیرش شرایط آمریکا کند.
تهران نیز امیدوار است افزایش قیمت انرژی در آمریکا، فشار تورمی بر خانوارها، افزایش هزینه حمل‌ونقل و نزدیک شدن انتخابات میان‌دوره‌ای، در نهایت افکار عمومی و سیاستمداران آمریکایی را علیه ادامه محاصره تحریک کند.
این دقیقاً یک جنگ فرسایشی و روانی ـ اقتصادی است. پیروزی لزوماً به معنای نابودی توان نظامی طرف مقابل نیست؛ بلکه ممکن است به معنای آن باشد که یک طرف زودتر به این نتیجه برسد که ادامه جنگ دیگر ارزش هزینه‌ای را که می‌پردازد ندارد.
مسئله زمان
در چنین جنگی، زمان اهمیت تعیین‌کننده دارد.
ایران باید پیش از آنکه فشار اقتصادی به یک بحران داخلی تبدیل شود، راهی برای کاهش فشار پیدا کند. آمریکا نیز باید پیش از آنکه قیمت انرژی و تورم به یک مشکل جدی سیاسی تبدیل شود، بتواند به یک نتیجه قابل ارائه به افکار عمومی دست یابد. به همین دلیل، جنگ در تنگه هرمز بیش از آنکه صرفاً مسابقه موشک‌ها و ناوها باشد، مسابقه استقامت سیاسی، اقتصادی و روانی است.
در نهایت، پرسش اصلی این نیست که کدام طرف می‌تواند ضربه سخت‌تری وارد کند؛ پرسش این است که کدام طرف زودتر حاضر خواهد شد هزینه ادامه جنگ را نپذیرد. و تا زمانی که تهران و واشنگتن تصور کنند طرف مقابل زودتر از آنها عقب‌نشینی خواهد کرد، احتمال ادامه این رویارویی بالا خواهد ماند.</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/SBoxxx/20695" target="_blank">📅 08:42 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20694">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">سوریه مدعی رهگیری چندین موشک‌ در جنوب این کشور شد  تلویزیون سوریه با اعلام این خبر مدعی شد موشک‌های ایرانی بر فراز استان سویدا در جنوب این رهگیری شدند؛ موشک‌هایی که به ادعای این رسانه، اردن را هدف گرفته بودند.</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/SBoxxx/20694" target="_blank">📅 07:54 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20693">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">سوریه مدعی رهگیری چندین موشک‌ در جنوب این کشور شد
تلویزیون سوریه با اعلام این خبر مدعی شد موشک‌های ایرانی بر فراز استان سویدا در جنوب این رهگیری شدند؛ موشک‌هایی که به ادعای این رسانه، اردن را هدف گرفته بودند.</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/SBoxxx/20693" target="_blank">📅 07:53 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20692">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">وزیر دفاع پاکستان، یمن را تهدید کرد:
اگر حملات از سوی یمن ادامه یابد، ممکن است مجبور شویم توافقنامه دفاع مشترک بین پاکستان، عربستان سعودی و ترکیه را فعال کنیم.</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SBoxxx/20692" target="_blank">📅 02:51 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20691">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NNqiejiMkDw3M2wsCNcOgnKriPdFxNzRDET9A-_v4IPf70QRX0fxZ-aCWBgDVhvaBF3qCOLYOFQcWgV2kFUjFzDzQyBHTQBKzAZBXDoJ7I-qg-kDO6XJAyuTKHLpd3k8t8akgDzm7bzz0CiLZVmsH64eUVAvwNigasUidTePyk0anGkX1mg_W59yb4k81PK0qr3Fcz_7e225_K5UhAOFU7paq2sjK-7kNCq_Pfzw09bD_w66DJM-rNLrrd81uqsC5k6PUFjXIbh1lTX_zNJ3DBSqXjCrEpyMBGRUd7kR8ron5Ixoe_JeMb5Q875zGWoyBiNONMLpryMNi5GA05Y9vQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لحظه شلیک انبوه موشک‌های پدافندی اردن برای دفاع در برابر حملات موشکی ایران به پایگاه موفق السلطی</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/SBoxxx/20691" target="_blank">📅 02:42 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20690">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8172d6b5b3.mp4?token=TbwUxa-8teyO6IYV5_aa2ixwv9NwwSoODtaKysYvGamdeAVc_yUN4t5vJWUBOuo_zKZIxGHxrRy0_eyIoOWyV1_R3OATn2HygIakvbpzSd2vf2J-f0tH9NpbnBm-QpoR36-NnPpqUSYZGmYer2SagH4kmPm2okUZiURNt_tUc7BxHtdnzi_SrGLBrCW47Lm2cdU86qwBCC9mbPHeNlOXZgI3JFPijvyXr9beBHd0MR1LvQpnwNAG_ezbhGU-WCKZGEQSleEJ7kVPrt6QdIgBfUGXsRRtJWTzAViO9OtOxz14YPpBUn4Bgg4Cy1Ropdv9DDZ0HkZJw56uES_ShgOiVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8172d6b5b3.mp4?token=TbwUxa-8teyO6IYV5_aa2ixwv9NwwSoODtaKysYvGamdeAVc_yUN4t5vJWUBOuo_zKZIxGHxrRy0_eyIoOWyV1_R3OATn2HygIakvbpzSd2vf2J-f0tH9NpbnBm-QpoR36-NnPpqUSYZGmYer2SagH4kmPm2okUZiURNt_tUc7BxHtdnzi_SrGLBrCW47Lm2cdU86qwBCC9mbPHeNlOXZgI3JFPijvyXr9beBHd0MR1LvQpnwNAG_ezbhGU-WCKZGEQSleEJ7kVPrt6QdIgBfUGXsRRtJWTzAViO9OtOxz14YPpBUn4Bgg4Cy1Ropdv9DDZ0HkZJw56uES_ShgOiVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظه شلیک انبوه موشک‌های پدافندی اردن برای دفاع در برابر حملات موشکی ایران به پایگاه موفق السلطی</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/SBoxxx/20690" target="_blank">📅 02:39 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20689">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sPYFTNsRbMU05u6yqd4ipQueMIM1qFeu8vS2LbWvYWRNFQlikO1pQgWagPdajrdHBOZNUj8xYvbHUpA9nzDlYV5GqfaH8AOIn1-wJl6d3RuHKfTNLcREEX4PoKomyn-wzjsfIlVv-RKTXMeu1llOOSYQyYqLI90LRZnJez4bKHCuTyEoQhvYprNB54-LHVVZmLesyW0VV1nOkps-6Gk-KuluShTlpJRgFKy1QafWUc1Mqy-_TP3zZyZORlFVcavK6WHb0MSXGpqoxDMqLnTP0p12BR6ybLzTE6hhgAvMXZMvpEVqHRlIdE1qUoyQYfALM77RVnqZZuV4YLVYauvXYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#USOIL — H4</div>
<div class="tg-footer">👁️ 4.65K · <a href="https://t.me/SBoxxx/20689" target="_blank">📅 02:25 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20688">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">سنتکام:
نیروهای سنتکام در ۸ سپتامبر، پس از آنکه سپاه پاسداران انقلاب اسلامی طی دو روز گذشته دو بار یک کشتی جنگی نیروی دریایی ایالات متحده را با موشک‌های بالستیک هدف قرار داد، ۵ کشتی نفتکش ایرانی را منهدم کردند.
کشتی جنگی ایالات متحده با موفقیت از حملات ایران جان سالم به در برد و به گشت‌زنی در آب‌های منطقه‌ای ادامه داد. هیچ پرسنل آمریکایی آسیبی ندید.</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/SBoxxx/20688" target="_blank">📅 01:47 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20687">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03fbb033c5.mp4?token=cW--XMEQjFNHCBrL7UV_1-exVNxEFIJOm8WLBp2o2CQzpKlWRG0YCCmWf6qMneGEjs9vkYWoxyoLh9JFG2hJqOELm8NJ82Yfe4debBQ-Qyix7ESCfkbY2-FkRM2Dta77Ej3EbZD7Q_F3lS8fOJQWfSFGznXXRoQvLroJ59Xus5pi65fYR638mF8bptAqnEevYa54UZnSfvm0TVN0klDRM5D259GF27B890ScldZkNSCBcVrhyj77kWbIR-Vs-In0NITGTR3Rf-P5VL8UuXeIc6SiZdV2N9LbHv73K1wJ37dRiCKgQnZBct1A06Mm8dNyk9x6vx0D0jlnP7X6hCz2tw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03fbb033c5.mp4?token=cW--XMEQjFNHCBrL7UV_1-exVNxEFIJOm8WLBp2o2CQzpKlWRG0YCCmWf6qMneGEjs9vkYWoxyoLh9JFG2hJqOELm8NJ82Yfe4debBQ-Qyix7ESCfkbY2-FkRM2Dta77Ej3EbZD7Q_F3lS8fOJQWfSFGznXXRoQvLroJ59Xus5pi65fYR638mF8bptAqnEevYa54UZnSfvm0TVN0klDRM5D259GF27B890ScldZkNSCBcVrhyj77kWbIR-Vs-In0NITGTR3Rf-P5VL8UuXeIc6SiZdV2N9LbHv73K1wJ37dRiCKgQnZBct1A06Mm8dNyk9x6vx0D0jlnP7X6hCz2tw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اردنی ها برگ هایشان از مشاهده موشک های با کلاهک بارشی سپاه ریخته !</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/SBoxxx/20687" target="_blank">📅 01:35 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20686">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">حمله ایران به بحرین</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/SBoxxx/20686" target="_blank">📅 01:33 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20685">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">من تردید ندارم مرحومه مغفوره برانیگان بخش هایی از اثر خود‌ را برای توصیف پدافند اردن، کویت، بحرین و اندکی هم خودمان خوانده بوده است.
مثلا اینجا به انفجار در پایگاه پدافند و شکسته شدن دیوارهای پایگاه اشاره دارد:
In the night, no control
Through the wall something's breaking
اینجا به تاثیر جنگال و عملیات SEAD روی رادارهای خودی اشاره دارد که کنترل را از دست نیروهای خودی خارج می‌کند:
You take my self, you take my self control
اینجا هم از قول یکی از سربازان پدافند می فرماید از این وضعیت تخمی خسته شده و دیگر اراده جنگیدن ندارد:
I, I live among the creatures of the night
I haven't got the will to try and fight</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/SBoxxx/20685" target="_blank">📅 01:32 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20684">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Audio</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/SBoxxx/20684" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/SBoxxx/20684" target="_blank">📅 01:22 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20683">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">آهنگ زیبای این شبهای خواهرمیانه:</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/SBoxxx/20683" target="_blank">📅 01:22 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20682">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">اصابت بیش از ۲۰ موشک به عقبه و الازرق اردن</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/SBoxxx/20682" target="_blank">📅 01:13 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20681">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">اسراییلی ها دارند اذا رمیت میخوانند</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/SBoxxx/20681" target="_blank">📅 01:12 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20679">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">موشک های بارشی هم به سمت اردن پرتاب شده و در حال فرود آمدن هستند</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/SBoxxx/20679" target="_blank">📅 01:11 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20678">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">شلیک های پرشمار موشک های ایرانی به سمت اهداف نامشخص گزارش شده</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/SBoxxx/20678" target="_blank">📅 01:09 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20677">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fvQFOjkn9Ca_uvOFHGfEH2Y5XzIlaYOWYyEEAPx3aCeffNue0cbmuYnpm6NB0KJvkmXCCxmgqXz9xTM7XRUq90NRtcCzxeIFHIVpMJ1MSGFdfUZX6iXZZpXrRfza0UENmiTnar33uX08asiuHLdZVDf_tH46F1Ngy3o0uVHzirTtHm7jhY6Bwl2P0_HiZ-WMVkVWDG-VD8MKMgWiihok-1wheJtPVAPCLBwoLwSsQWMu07v8g8WnpOHHGEP3wj7LgTXA5PCtXoDd5s-VpJLTpIivS3YuVDi1wNuifHNK2iH9Z5XVRb4rwWLrDiJ-45PyB56WvKJapF9W-EDQu_cOAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هشدار دوباره مرندی ذوالاکتاف به عربها</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/SBoxxx/20677" target="_blank">📅 01:07 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20676">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">فرماندهی نظامی ایران تهدید کرده است که به نفتکش‌ها در بنادر کویت و بحرین حمله خواهد کرد و به خدمه هشدار داده است که کشتی‌های خود را ترک کنند.</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/SBoxxx/20676" target="_blank">📅 23:57 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20675">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">این هم رونمایی از ربات تماما بومی-محلی ایرانی در نمایشگاه کیش اینوکس  که اینقدر طبیعی ساخته شده که اصلا طبیعی شده   خودشان میفرمایند یک «داده» هستند و چه اسم با مسمایی که ولی خب.</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SBoxxx/20675" target="_blank">📅 23:53 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20674">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E8DqSQoTGdd5wWNUUbvDCEmL7wFVc2QzPykmNmY2Zr2Ns4Fjqmqp-zlyt8GkYAdIgegIdtoPPYdkcu56EOJ7Xp4zry4sCjVYd5mRL0t_YKkvvT2kLa6HQxm2_9Q1JEkoMOtjxouVp5118rbzUrRCGGNMdydxfZgkS1mSy1BuPgd8AVx9aDPLMQVZgOeW499P4BLTJ7hPdym0jyHA9rdV9_j2JqeD-q0Q3x6-ZPAfAFzR3wzduk8KeLBtGB_e_YslTSboHdb5PLvr3oe49ksEqltuy8189lc076zPZW7pSqMKtg1jb6D0AYpAwY_OobI173N1tz68Dtm_7wsDHQxqkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گزارش هایی از حضور ربات های نظامی اسراییلی در حمله به مواضع حزب الله خصوصا در علی الطاهر منتشر شده که توان حضور در تونل های زیرزمینی را داشته اند!</div>
<div class="tg-footer">👁️ 5.68K · <a href="https://t.me/SBoxxx/20674" target="_blank">📅 23:30 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20673">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">انفجار در خارک!</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/SBoxxx/20673" target="_blank">📅 22:35 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20672">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">انفجار در خارک!</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/SBoxxx/20672" target="_blank">📅 22:35 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20671">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">گفته می شود چند نفت کش ایرانی هدف قرار گرفته اند</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/SBoxxx/20671" target="_blank">📅 22:28 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20670">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">باز هم ریزشی است تا 4355 دستکم .</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/SBoxxx/20670" target="_blank">📅 22:27 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20669">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">شلیک های جدید از ایران به سمت تنگه هرمز</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/SBoxxx/20669" target="_blank">📅 21:50 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20667">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">مصطفی عامر از رهبران انصارالله :  سپاس و ستایش خدایی را که عربستان سعودی را پر از نفت کرد و به ما کبریت داد</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/SBoxxx/20667" target="_blank">📅 20:00 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20666">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vKRyzn4amMGUp2u0s_CC1vzLN9_4_fjZWr-udat9TqIhduW6-2qGtsIEDHlnJmpdveQAMnwF14SqbuU_DtMirQpvd6wTcltkWs-JIpHoJgAoo3jjWQKfQvqYoax-lhwWN_nS-l2-1rkCVAX-NzSU0Zwus7LLka-xtf2kL6ww5wrx4m2A779tPAVghYJDK1eK7BFsGL_NQNjjy98ixflhC-miczqvH6XBMBJWJOoUJ61NfZDQuQ0BRGB7uMfIaQe9h1Ys1dqyZcF3UV_XjpJkCc-4EBaUN3KTwbyiZXbcUHve17Cz9_IhOvCumD2cYFDSuNdhAfzl_Po6osNqFJXpvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">video_2026-09-08_19-52-57.mp4</div>
<div class="tg-footer">👁️ 5.52K · <a href="https://t.me/SBoxxx/20666" target="_blank">📅 20:00 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20665">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">video_2026-09-08_19-52-57.mp4</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/SBoxxx/20665" target="_blank">📅 19:58 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20664">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">video_2026-09-08_19-52-57.mp4</div>
  <div class="tg-doc-extra">1 MB</div>
</div>
<a href="https://t.me/SBoxxx/20664" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">ویدیویی از انبوه تویوتاهای نیروهای مورد حمایت سعودی که به سمت جبهه های جنگ با انصارالله (حوثی ها) پیش می روند!</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/SBoxxx/20664" target="_blank">📅 19:54 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20663">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک + تقویم اقتصادی برای امروز در سطح میانه ای قرار دارد. نظر به رشد طلا در بامداد، از اینجا به بالا توصیه به فروش طلا داریم.</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/SBoxxx/20663" target="_blank">📅 19:42 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20662">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">خب منظور این بوده!  یک شهپاد زیرسطحی است  (شناور هدایت پذیر از راه دور)</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/SBoxxx/20662" target="_blank">📅 19:27 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20661">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">هاآرتص
:
حاکم امارات متحده عربی ۱۰ روز پیش از ۷ اکتبر درباره حمله تروریستی حماس به نتانیاهو هشدار داده بود.</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/SBoxxx/20661" target="_blank">📅 18:48 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20660">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hdMxPIbStrLVjjO9Q2Kr2XFgz4B3JsqeLOdHzWr_cnCagfVzINPhtYgDar6CnZSC5qJqlSiwsRCYzPvTaN8yBZZMw3AUW6pgoaQAzxciaG4KQ4BFGyvNIMewBZycjwj2h8sGQYKQyf3JX5RKa4lFcDVdUv-ime5Yf_Zeq0MZbGAcknbc2LJ46vkC1ZUZPt36eRTbSStVWOhPrCYCcRmEqOLwbs06q9Hmc1vHpF2197wWvuFso6MWsafThXvQqF4863Uk4IAJS95yVv7OFTy3XxaAD6SNZ93QUs1ab8NsIOI83cKDHLGkPHOj3noaIIWWGVSJ88Rq0ZcwfATQXGuMvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیروی دریایی سپاه پاسداران انقلاب اسلامی:  به لطف پروردگار متعال، رزمندگان نیروی دریایی سپاه پاسداران انقلاب اسلامی موفق شدند در ورودی تنگه هرمز، یک فروند از جدیدترین زیردریایی‌های پیشرفته متعلق به ارتش تروریستی آمریکا را به دام بیندازند.   این عملیات در یک…</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/SBoxxx/20660" target="_blank">📅 18:32 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20659">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">نیروی دریایی سپاه پاسداران انقلاب اسلامی:
به لطف پروردگار متعال، رزمندگان نیروی دریایی سپاه پاسداران انقلاب اسلامی موفق شدند در ورودی تنگه هرمز، یک فروند از جدیدترین زیردریایی‌های پیشرفته متعلق به ارتش تروریستی آمریکا را به دام بیندازند.
این عملیات در یک اقدام اطلاعاتی و عملیاتی پیچیده، صبح امروز انجام شد. این زیردریایی پیشرفته، مجهز به جدیدترین فناوری‌های موجود در جهان در زمینه زیردریایی‌ها بود و در سال 2025 به ناوگان ارتش تروریستی آمریکا تحویل داده شده بود.
لازم به ذکر است که این زیردریایی به دست گرفته شده است و تصاویر آن در چند ساعت آینده منتشر خواهد شد.</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/SBoxxx/20659" target="_blank">📅 18:21 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20658">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">نتانیاهو:
ما به جنگ نهایی با ایران بسیار نزدیک هستیم.</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/SBoxxx/20658" target="_blank">📅 18:21 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20657">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">کرملین: پس از بازدید نمایندگان ایالات متحده، پوتین و ترامپ در یک تماس تلفنی «بسیار صریح» گفتگو کردند
پوتین به ترامپ گفته که روسیه هیچ «طرح تهاجمی» در قبال اروپا ندارد</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/SBoxxx/20657" target="_blank">📅 17:56 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20656">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">الاخبار: ترکیه در حال میانجیگری میان دمشق و حزب‌الله است  روزنامه الاخبار لبنان: ترکیه در یک حرکت دیپلماتیک موازی با تحولات منطقه، در حال میانجی‌گری برای تقریب دیدگاه‌های حزب‌الله لبنان و دولت موقت سوریه است.</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/SBoxxx/20656" target="_blank">📅 15:32 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20655">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">الاخبار: ترکیه در حال میانجیگری میان دمشق و حزب‌الله است
روزنامه الاخبار لبنان:
ترکیه در یک حرکت دیپلماتیک موازی با تحولات منطقه، در حال میانجی‌گری برای تقریب دیدگاه‌های حزب‌الله لبنان و دولت موقت سوریه است.</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/SBoxxx/20655" target="_blank">📅 15:20 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20654">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">GeoMarkets - Podcast 25</div>
  <div class="tg-doc-extra">Ali SharifAzadeh</div>
</div>
<a href="https://t.me/SBoxxx/20654" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">#پادکست_GeoMarkets
شماره — 25
سه شنبه 8 سپتامبر  2026</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/SBoxxx/20654" target="_blank">📅 14:12 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20653">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">رائفی پور ورژن مونث بدحجاب موجود شد</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/SBoxxx/20653" target="_blank">📅 13:13 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20652">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">یک جوری‌ مینویسند دلار را رنج منفی کشیدند ….  به قول امام خمینی (ره) انشالله خداوند همه ما را آدم کند!</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/SBoxxx/20652" target="_blank">📅 12:16 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20651">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1aa849e433.mp4?token=A789YmeMqCZmw3C813G2vHZRbX_epJVW0GufmE-_Y1ZC0Iqlwq_-BnrL68GsasiHanIIlgj7AehmLcO6MXbAJNXm_p9b9KB0f8LQ6fWUzsLOtYV_vMOKuQHXfwzVWTl1o81DkNMP3gbg-gfGNEytaKwcu271PEI-r4PiyjFVF52tSBt1HurhWPwaW0ujHyCUzuW0MwTKua9fObd-Es4HqCU9_dJLONFfNlcqXkrQubXnEGaoZdQBvDNExH6i6tghzB9IUr28-WfZzlNP1e-uJpP96DsSwFuTpJEjyAVEBpRnT6Q7PKs9kvzWVET2I52khF1_ivlThX0LhcMM4Khk8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1aa849e433.mp4?token=A789YmeMqCZmw3C813G2vHZRbX_epJVW0GufmE-_Y1ZC0Iqlwq_-BnrL68GsasiHanIIlgj7AehmLcO6MXbAJNXm_p9b9KB0f8LQ6fWUzsLOtYV_vMOKuQHXfwzVWTl1o81DkNMP3gbg-gfGNEytaKwcu271PEI-r4PiyjFVF52tSBt1HurhWPwaW0ujHyCUzuW0MwTKua9fObd-Es4HqCU9_dJLONFfNlcqXkrQubXnEGaoZdQBvDNExH6i6tghzB9IUr28-WfZzlNP1e-uJpP96DsSwFuTpJEjyAVEBpRnT6Q7PKs9kvzWVET2I52khF1_ivlThX0LhcMM4Khk8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رائفی پور ورژن مونث بدحجاب موجود شد</div>
<div class="tg-footer">👁️ 5.42K · <a href="https://t.me/SBoxxx/20651" target="_blank">📅 12:11 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20650">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V4rctRU0EWvXOdAWhH4AQqE2ZoAbtMGI6jkO4wfq3zXA8bfiu6qvtJENlYBkfD9W67kRnKhbrGe45h_kh2yxB-7jjc8KXqVgTvjX6Ta_JjpDJw4pZIjTU3vhbpfcsRSM5xdDWTaDVrVOk6h0HTaJgcGRkm6a29AFguj8F98D9cyuxsI-9ZATiZG7_W9ri9bb_05npcarVy_2TJftaOSplhjjKnfyhHb0lRuCpYNWDHY-D4qKfoYU91rusQIoCzKRpCBXO4Ms-hAIsz7arPY7GpejfX9sMB70TLv7hVOBQquLbbg28wJmJ_jfAHGQJL9vqTk_pIvT7muh7duPQsCFlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فولکس‌واگن با پیمانکار دفاعی اسرائیلی «رافائل» توافق‌نامه‌ای امضا کرده است تا کارخانه خود در اوسنابروک، آلمان را به یک مرکز تولیدی برای قطعات سامانه دفاع هوایی «گنبد آهنین» اسرائیل تبدیل کند.
انتظار می‌رود این کارخانه در سال ۲۰۲۷ تولید خودروهای سواری را متوقف کند و به‌جای آن به تولید کامیون‌ها، ژنراتورها و سکوها برای پرتاب سامانه‌های گنبد آهنین بپردازد.</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/SBoxxx/20650" target="_blank">📅 10:35 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20649">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">وزارت انرژی عربستان اعلام کرد حملات بامداد امروز یمن به تأسیسات انرژی در جنوب این کشور، موجب آتش‌سوزی و توقف موقت فعالیت برخی تأسیسات شده است.
در این حملات، پالایشگاه آرامکو در ابها هدف قرار گرفت و همزمان گزارش‌هایی از اصابت به فرودگاه ابها و شنیده‌شدن انفجار در مناطق جنوبی عربستان منتشر شد.
این حمله سومین حمله به تأسیسات نفتی عربستان در کمتر از ۴۸ ساعت است.
‎</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/SBoxxx/20649" target="_blank">📅 10:21 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20648">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">220 پیپ</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/SBoxxx/20648" target="_blank">📅 09:59 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20647">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک + تقویم اقتصادی برای امروز در سطح میانه ای قرار دارد. نظر به رشد طلا در بامداد، از اینجا به بالا توصیه به فروش طلا داریم.</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/SBoxxx/20647" target="_blank">📅 09:59 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20646">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bdfe837d4b.mp4?token=A3v-HoMbpf3Dk-aI-jPNpU8pg_XLlr0qUIObCt-DqT1zQzRFe8O4ilgqB_0vngk_cHG7QL1WQLn4Pl4HCO2GscJGeHqoryzurcmWkJKMQED8Bf0FAuVbWKa2qrr4mQDAe7Nnj8DVJA_pxOw0zrkF54iywrhB7FLRPd3s3RRBk8_IsY09PYbzWLkIJddDHtlBohJdQqEzGEGRyQd7Rs3urJnZ9Nmr0IDvcT9jHDIYF4QmNVjp1yzmorW6CgVlHOUdIZsUZGLf9YMche3iD1M-84zvTks9JZZnseqMwhYZveXjdS5Golcvtxc1cE2oH1qZXNQTGmuepu3iGIrU8R1Mnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bdfe837d4b.mp4?token=A3v-HoMbpf3Dk-aI-jPNpU8pg_XLlr0qUIObCt-DqT1zQzRFe8O4ilgqB_0vngk_cHG7QL1WQLn4Pl4HCO2GscJGeHqoryzurcmWkJKMQED8Bf0FAuVbWKa2qrr4mQDAe7Nnj8DVJA_pxOw0zrkF54iywrhB7FLRPd3s3RRBk8_IsY09PYbzWLkIJddDHtlBohJdQqEzGEGRyQd7Rs3urJnZ9Nmr0IDvcT9jHDIYF4QmNVjp1yzmorW6CgVlHOUdIZsUZGLf9YMche3iD1M-84zvTks9JZZnseqMwhYZveXjdS5Golcvtxc1cE2oH1qZXNQTGmuepu3iGIrU8R1Mnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تببین مگاپروژه هوشمندسازی پمپ های بنزین !
حتماً ببینید.</div>
<div class="tg-footer">👁️ 5.51K · <a href="https://t.me/SBoxxx/20646" target="_blank">📅 09:44 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20645">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cHZhWB9gUhhBnzpRoEHnVrTPEikN7yyzrg8RVsntN7efjgkjne-hsG48fiDo7RR0b_nRFAOhZilWVDh-Y5FfAU9QI35Qyd3fa9kfidytyhmjoKDoWGJvOfXNv1zMxHfy2pU8P7pwcRK-u3lzYblUw7mNioWKXk9rEEPE12CV6CAX2q_23sG3l9jDy5ef6oTJbDI6aPT9agG1bGKL84yY3-yEFJyU3wieigoXTSxTsEPMf5rCB_Fdy50-eFQdeUAM52zM6C8ZqKprDcq2N8DJhIrXKAJUk_XydnFbXUm3zq97xZfiMDsFuGaSdzmI1EpZlFVAw9B1Fu_wxphJ90xZNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آخرین وضعیت یمن</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/SBoxxx/20645" target="_blank">📅 09:39 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20644">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mMrPhCbM1CwJVjmsQqrMcnixr0Kchm-JyUGKKXugHqpk2YeqfWKVhesQlJyHgQAaq1AdstVTfdmz-Lnuqzwc__ZSHKtEMNeMBVXB_gVRHRYM1kvoASbHJmUytFsA65EAi45aRNStYZnZTzyJxqChO20MqJ4i5bPlMOresVp76dNtbmES06HgZq0oxd8KiR2RcRbe5eQ-PAMGlOywtz_bD2q1Tuj6QPEeorslM399Pe3U1LgOf1zCsqMDpE5ViLOaM_BLk645dfAkTQDMdivRB0kJiH47P0FuqvU8AoqJe4O7wQ3d-biRNGNT4dCSX0wjp15_0z47XKN71MVJtBwdxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک + تقویم اقتصادی برای امروز در سطح میانه ای قرار دارد. نظر به رشد طلا در بامداد، از اینجا به بالا توصیه به فروش طلا داریم.</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/SBoxxx/20644" target="_blank">📅 09:17 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20643">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tel6eUoANrFH0y7q9HSeRtVdo1k6gI8xgzD_EVoSLxOeDBjvNXdy91kBd0er0BFT2a-6OPSTgGc1v5KZ167bePqGB_RM9IWZY59X8voazk21kvTWo9C1oyClY597vJlo_hxfAtiuB5GaE-zr3B2LOn0vjHWBUUyyKj-Y60jZp7Q6MzlBCvdRpJ8KSN0iIP_c1ZRP4-FQrHwHHNBirtl__lCplqb0MyO7EfUjiExrsAkVMRw_fstXYLlo0araSxk4LWwsuKuEUMQKLHjvgqj-KVsvorbwaLyuSgN-_XuakOAkPTVe7P5xYGURYEL5SwaJ8llmQOV7LcYQ5ExSTf7QlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک برای امروز در سطوح میانه بالا قرار دارد و با توجه به ریزش بامدادی طلا، پایین هایش خرید موقت دارد با تارگت های 4418 و 4441</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/SBoxxx/20643" target="_blank">📅 09:17 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20642">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">سفر امشب ویتکاف-کوشنر به روسیه قطعا با افزایش تنش میان آمریکا و روسیه به دلیل تصویب قانون تحریم های گراهام و متعاقبا انتشار گزارشهای موثق از کمک نظامی روسیه به ایران برای ساخت موشکهای کروز ضدکشتی و سپس اعلام ترامپ دال بر ازسرگیری ارسال تسلیحات برای متحدین…</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/SBoxxx/20642" target="_blank">📅 08:38 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20641">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vPI8CYqr3QyUL5gwpnkDTo5_PZHBfO56zo6ffCU-Nrq62W8SOMG9gegC-IT0BX3qbdLvP5eTtKkLs_NnloRoqa5tLZ9kUBlQPABRDS7YqfQriHG7sngoXJWgrNiEmnt31RLhWtZK5TaE9SKNelk7Woa_9mPONZorRSJcJ6pTEcR45btc4XNHQ_zA_5BgXARgvl6_KDUBo3e96AlDCZ6qSj8MihICjqbOIRRxwXxQ_heTSB8XPjfOnGgjBH-g2TvGv4ioUefkdksE8DIrthdF9Pu16bEYeCOe31KxXEGuMss0fUpGyrUrZzwlbikUxs6XF1sANiquUaUt7sT84XQL2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تهران شرایط جدیدی را برای پاشینیان در مورد "مسیر ترامپ" مطرح کرد.
ایران به طور غیرمنتظره، شرایط سخت‌گیرانه‌ای را برای نخست‌وزیر ارمنستان، نیکول پاشینیان، در مورد پروژه TRIPP تعیین کرد، در حالی که لحن دوستانه‌ای را در بیانیه‌های عمومی خود حفظ کرده است.
تهران خواستار این شد که امنیت این پروژه توسط نیروهای مسلح ارمنستان به طور انحصاری، یا توسط نیروهای نظامی یک کشور ثالث که از قبل در ارمنستان حضور دارند، تامین شود - به وضوح، منظور نیروهای روسی است.
به گفته منابع، به این ترتیب، تهران تلاش می‌کند از حضور نیروهای آمریکایی در مرزهای خود جلوگیری کند. در غیر این صورت، در شرایط تشدید تنش، طرف ایرانی، حضور آنها را به عنوان یک هدف مشروع تلقی خواهد کرد.
این موضوع، اجرای پروژه‌ای کلیدی که از قبل عملاً فلج شده است، را به شدت دشوارتر می‌کند.</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/SBoxxx/20641" target="_blank">📅 00:42 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20640">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">سارا خلیفه مجری مشهور مصری به دلیل قاچاق مواد مخدر به اعدام محکوم شد!</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/SBoxxx/20640" target="_blank">📅 00:26 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20639">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">ای لعنت به پدر مارک بوسنیچ که گذاشت آن گل را بزنی و بعد ۳۰ سال مجبور بشویم چهره و رفتار انیرانی ات را تحمل کنیم!</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/SBoxxx/20639" target="_blank">📅 00:21 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20638">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">سمیر الصبری، معاون وزیر دفاع دولت رسمی یمن:
«تصمیم برای آزادسازی صنعا و حل مسئله گرفته شده است».</div>
<div class="tg-footer">👁️ 5.51K · <a href="https://t.me/SBoxxx/20638" target="_blank">📅 23:20 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20637">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">یک آزمونی هست برای تعیین قطب نمای سیاسی شما
این
گزارش نتیجه آزمون
برای من است</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/SBoxxx/20637" target="_blank">📅 22:53 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20636">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">ارتش ایالات متحده در حال حرکت برای استقرار راکتورهای هسته‌ای کوچک است، در حالی که برای مقابله با تهدیدات فزاینده علیه شبکه برق و افزایش تقاضای انرژی در پایگاه‌های نظامی آماده می‌شود.</div>
<div class="tg-footer">👁️ 5.44K · <a href="https://t.me/SBoxxx/20636" target="_blank">📅 20:54 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20635">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gCW3CZ207Yi26sCa9aJ9QzZyWQLM5YFI65kcrjLOzZ_gCz0WqIk-4aStvY0IrYgha96bdn5Yu2JO6Pop9kzg8qiSLtoqIr8nkamhIwFRNcnifzDU3JvU24ReXp56LvH_zhuiw6xrOAlhzYytfnGCdCLX4UBd88I1faMQ7RUD0Iq8MrhGP8gPSe1qnoEB3s6mSoKvXE0FK2zWirasgn-pcfQIv2_ZeuBXNSf86FM28SoI19r_iiOrs4ljSwQjIMefblgxjqf3OA5MuD5jsouwvscLcCLZFuTRDiH4OBHRrbI5oy6Es5SHKZUCuN7hIdtZg4Ct4XX-pLnSzFYIWoRF6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سارا خلیفه مجری مشهور مصری به دلیل قاچاق مواد مخدر به اعدام محکوم شد!</div>
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/SBoxxx/20635" target="_blank">📅 20:50 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20634">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">علی‌آبادی، وزیر نیرو :   تمام نیروگاه های کشور برای تامین برق در آماده باش کامل هستند</div>
<div class="tg-footer">👁️ 5.42K · <a href="https://t.me/SBoxxx/20634" target="_blank">📅 16:56 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20633">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">علی‌آبادی، وزیر نیرو :
تمام نیروگاه های کشور برای تامین برق در آماده باش کامل هستند</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/SBoxxx/20633" target="_blank">📅 16:55 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20632">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QTF323f7LfBpV3ryX0KOvG6lymZbHEuHyPscatD6wZTcv7G6KWU9wF74rqNaStFvN3247eqetlq8zUqx2gzbzA6ldRs_aes2Kgiyalt55pJMHU-5sLyirV8PMTo7QPXPKL3vDnLXjP-V4RX9xtKVBwdV6A_pv-Shq7WN4OsZjqfqthAG1fkSodUyz1KIN6T9d_ghbVVrSZvF8_T2ePlhZkyh6XwvZsIRn71hg52ZXgL5UXyjVaVGp7reuwCC1iG9Azc4XheB4zymQu67PzQCjctMI9zYQK3kfsrnP836rt009dI_kQR5OdHxunr7nbYzX6ntfsHXbtuRXVWrYvfrkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این مسیر محتمل وقایع آتی از دید من است:  — شکست عملیات طرد اقتصادی در تسلیم یا فروپاشی جمهوری اسلامی — حملات جمهوری اسلامی به تاسیسات نفتی و گازی منطقه — آغاز دوباره جنگ — عملیات زمینی آمریکا برای تسخیر بخش هایی از جنوب کشور با این نتیجه: موفقیت کوتاه مدت…</div>
<div class="tg-footer">👁️ 5.55K · <a href="https://t.me/SBoxxx/20632" target="_blank">📅 16:48 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20631">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">این ژاپن بزودی بدجور موی دماغ چین خواهدشد.</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/SBoxxx/20631" target="_blank">📅 16:44 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20630">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">بوی یک حمله همه جانبه به نیروهای موسوم به محور مقاومت می آید:  — حمله پلیس عراق به منازل عناصر سیاسی نزدیک به ایران — ضرب الاجل دولت عراق برای خلع سلاح حشدالشعبی — توافق دولت لبنان و اسرائیل برای پایان حیات نظامی حزب الله — آماده شدن نیروهای مخالف حوثی ها…</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/SBoxxx/20630" target="_blank">📅 16:24 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20629">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">همزمان بیت روحانی فعال شده اند....</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/SBoxxx/20629" target="_blank">📅 14:34 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20628">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">حملات به تاسیسات شرکت سعودی آرامکو</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/SBoxxx/20628" target="_blank">📅 14:32 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20627">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">GeoMarkets - Podcast 24</div>
  <div class="tg-doc-extra">Ali SharifAzadeh</div>
</div>
<a href="https://t.me/SBoxxx/20627" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">#پادکست_GeoMarkets
شماره — 24
دو شنبه 7سپتامبر  2026</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/SBoxxx/20627" target="_blank">📅 14:13 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20626">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">بقایی:   مذاکرات خوبی با هیئت قطری داشتیم</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/SBoxxx/20626" target="_blank">📅 13:12 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20625">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">بقایی:
مذاکرات خوبی با هیئت قطری داشتیم</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/SBoxxx/20625" target="_blank">📅 13:10 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20624">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">بعد از کتک خوردن عراقی ها در رشت، این بار مردم غیرتمند سمنان هم این وحوش را به دلیل دست درازی به نوامیس خود گوشمالی دادند.</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/SBoxxx/20624" target="_blank">📅 12:57 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20623">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e33e75cd83.mp4?token=skAc2PNFFY6BtoerP1Q6fSEXpsWq5dGOrUjBvXXG2hxj9oewUIk0s8X2Mmixxy8acGDDdxOsj_YWw7oQW1LnoglN0rMQ4B7Nkq_mRFOOwTM5Yo6EU8T2LrgTPNq2ZunJJnbtikDuyxt0v0LTAXYM1QpqwRXA1lpQ_R2eH5Hvy-c6BgmvKj-3xaHf9gT4wj4kTEyIOSnX4IdpBFjTxH7PKtFInwVXE3PftyNE74ECynUbAnitnvhptSaaItTZZ5jUTr4QnxXOMm0uidWf8sGN5Prrt00I_j2tKlehvTGs7KINXfyHUM1uEQBwE1f1SZp_UNlPoVGwDmNn0EZcwJ3Vxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e33e75cd83.mp4?token=skAc2PNFFY6BtoerP1Q6fSEXpsWq5dGOrUjBvXXG2hxj9oewUIk0s8X2Mmixxy8acGDDdxOsj_YWw7oQW1LnoglN0rMQ4B7Nkq_mRFOOwTM5Yo6EU8T2LrgTPNq2ZunJJnbtikDuyxt0v0LTAXYM1QpqwRXA1lpQ_R2eH5Hvy-c6BgmvKj-3xaHf9gT4wj4kTEyIOSnX4IdpBFjTxH7PKtFInwVXE3PftyNE74ECynUbAnitnvhptSaaItTZZ5jUTr4QnxXOMm0uidWf8sGN5Prrt00I_j2tKlehvTGs7KINXfyHUM1uEQBwE1f1SZp_UNlPoVGwDmNn0EZcwJ3Vxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بعد از کتک خوردن عراقی ها در رشت، این بار مردم غیرتمند سمنان هم این وحوش را به دلیل دست درازی به نوامیس خود گوشمالی دادند.</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/SBoxxx/20623" target="_blank">📅 12:57 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20622">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">در استرالیا استفاده از مواد روانگردان برای مصارف خاص درمانی قانونی اعلام شد.  پس از قانونی شدن ماریجوانا در بسیاری ایالت های آمریکا، قانونی شدن استفاده از مواد روانگردان طبیعی در موارد خاص در استرالیا پیشرفت مهم دیگری محسوب می شود.  شخصا باور دارم که بزودی…</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/SBoxxx/20622" target="_blank">📅 12:09 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20621">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک برای امروز در سطوح میانه بالا قرار دارد و با توجه به ریزش بامدادی طلا، پایین هایش خرید موقت دارد با تارگت های 4418 و 4441</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/SBoxxx/20621" target="_blank">📅 11:32 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20620">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l3ipoujNRW86g6qTRmHiQByOwKSfa0xrocxOXrfKmQf4cFX9JwRM8BU_WoHCtwYbGNAdC8ig9wJ0qkpDyUw0_ERRRwy0lDsaGuKvImqVOB1kDYMustgCrYLjzzWsqV7Q60HpiKb95QfGYgo_d8IlI1hJEYDLxDXBojcedoW8_efaXt1Wkqjsb5nMsrnRpnkaqgwbDIbE6nn8uq7NpIp4Hm1ndnJLXDeGZABF6x4b3u3Bb-9ClA0lNFYmWmTmG0EW02au_6gaX7jWh9U9P8JyKjN3FwUJH2qR4GkfGbaq-KwwtCxI4Q0ak5ZLRDIdw5Vn-w_11ZfyfF_5sxApnpCxzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک برای امروز در سطوح میانه بالا قرار دارد و با توجه به ریزش بامدادی طلا، پایین هایش خرید موقت دارد با تارگت های 4418 و 4441</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/SBoxxx/20620" target="_blank">📅 11:31 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20619">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QQBSA3GQNyggGqj0rcPIeIYpk6K052iDRpqa86CkSHQQxV8lm86uaTFuUCo1PtdC7sYjcNGucgKdOLWu0HnEGR8ggPdmCGFnxIBhctStINz9aM-LIMn6gS9ZsVnsoDUPXA3fO43L9BfDqXEhAXa9UiAkoXm9GDiRsBe9F_d0vEmlJC0b4GHay8udJ9sMZTbxMUvaQsRLgzwq1TS-Fe34-jT0GVY7aucJeLgv_E0Lj4WFS9AJhB5l9P4bEHoJOsxpojE07tNikvr7Ff8BcpnBje9SnfaVZO3CtCfbxcbC3YElEMYRRhwvfew_apZdPAqzTSV0Qks4sqSBFo1D68MrkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ای لعنت به پدر مارک بوسنیچ که گذاشت آن گل را بزنی و بعد ۳۰ سال مجبور بشویم چهره و رفتار انیرانی ات را تحمل کنیم!</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/SBoxxx/20619" target="_blank">📅 11:08 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20618">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">حزب‌‌ راست‌گرای افراطی AfD آلمان برای اولین بار در تاریخ خود در یک انتخابات ایالتی پیروز شده است.</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/SBoxxx/20618" target="_blank">📅 09:22 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20617">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">— به گزارش رويترز، پس از حملات اخیر ایالات متحده و ایران به تانکرها، حجم حمل‌ونقل از تنگه هرمز به‌شدت کاهش یافته است.  داده‌های شرکت کپلر نشان می‌دهد که میانگین روزانه کشتی‌های کالایی در ۱۰ روز گذشته ۱۰ کشتی بوده است که کمترین سطح از ماه مه به این طرف است.…</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/SBoxxx/20617" target="_blank">📅 08:36 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20616">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bldhlWQHXb3qdGcUAUmudtL9ayyYqco-ewPhGj2gtIGAiTk5gIXaXBUisYPYUDqkm5vBd2omFpCJWBbiTN0H_QN6YKfZAvkmDVBPV2ON50LxBQDGQRtRaLRkTzRUNffF8NRNPbBvGBtV-MekkzWEVCjrR0TOwEkoF4RJXiXbKgXoEBpnup69NOd9TqEkG-9xTlhdOUEJjWpDOdZipmHB10tE6eyXVGIFAkYoIrDTywc7IWmJOglBKOAQCtbyoI4zdrgHXX_Ivb4ZNAcn-Lgd_73H-4DRX2di62pqtVTIsa9wmYA2SrK5n3G6naKMSK6JSz6ASjWBmfNbOurbX_HeRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ با انتشار این پست مدعی شده که بخش عمده نفت عبوری از هرمز به سطوح پیش از جنگ برگشته است!  به نظرم دروغ می‌گوید چون قیمت نفت خیلی بالاتر است</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/SBoxxx/20616" target="_blank">📅 08:35 · 16 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
