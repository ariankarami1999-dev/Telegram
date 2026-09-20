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
<img src="https://cdn4.telesco.pe/file/gUkzXDvRQKSYAdTwVyn94PbukzFkyfYOnyG4B3Nms8L9ycX_4L241Igcs7NVU2qYxC0WwVLSLCAEXmupKppzVOVsA_2FUXfuAThYKx8wiEun4rKRRXgUbHgpxBhDPSybJETOzS6gGY3p4KJSyrKNSH0-MEqu4lS1mi_GnbqsXMKL10h5pte2pFj_1gUsSatDK0MtJMbCM5GXKiOxoJ5CHn8_DpAiC8eQ_FOn7Tpak-wW8tx1I_yjhmuCXZCdJ9WRLGGPitz2U_Tsm172xgFB0BJTG8FsQ9lc_3iLN471sWVF7XGNqXJ57wO7KHTU4XKzvd9YT3voqL1IRWuutB0OXg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.03M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-29 21:02:41</div>
<hr>

<div class="tg-post" id="msg-691530">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9d1966b37.mp4?token=pn7kYybYepCeu0AsJyVOKQACnvgixP4I-RJB56CE8I3gC79D82B7xcH17IyajAK59qbZC42nlmP5Gqc3xQrMqbCM3822azDctruvBodYf4RMiOqP0WTLNbBmCzeuk_4Xxah3W7-K8jnmTlbW6ahk6vn1LdToBP6JshSG2fwhqeRoRaxnv8gwQ8WpGaDy6rSD1BP6YnYzdITNTgxv5W96JkaJtj78YHNz_ToHpE3fTwS9tKa-3PHKNT-RWeaC4l1oDyzi4R2r2zOM64ECWfLWjvPE8t_WCnC7SC12XCH2uDUds9sbs_GtJyINBt41N2m0rhzw0qd9e0PPiSB0Cz8_Zw8WfMo5oQkRA4o8Hx5YIEIFJTvgLhSB3kxOv-LUzUBEel_0NT7wa8h6nhGX7oZSR7Z6PwVElXq1aSAkTO0y97Ez9_4shlXZjje_2dT9x8KqkomoUyXH5iOppCCRGvLa6sO3FEp353M6r_EFEA2y8gPdAZZiwnwKVHW0QksDqnv-dGjfBl8JcAePvMjWbDiKaAfDzBtVItcnlUxm_I-9UzwehI-l-_c7cM5OMaPtqDMKXoz247paeFA24NsGn-LTHim71jvkJLFq369hDEF5rgRmAaGH4cR1urCYOFrMFp7_L3sSWm6hE22IYOuQ760SWlnttZu-5dGjflc1EnzB9c8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9d1966b37.mp4?token=pn7kYybYepCeu0AsJyVOKQACnvgixP4I-RJB56CE8I3gC79D82B7xcH17IyajAK59qbZC42nlmP5Gqc3xQrMqbCM3822azDctruvBodYf4RMiOqP0WTLNbBmCzeuk_4Xxah3W7-K8jnmTlbW6ahk6vn1LdToBP6JshSG2fwhqeRoRaxnv8gwQ8WpGaDy6rSD1BP6YnYzdITNTgxv5W96JkaJtj78YHNz_ToHpE3fTwS9tKa-3PHKNT-RWeaC4l1oDyzi4R2r2zOM64ECWfLWjvPE8t_WCnC7SC12XCH2uDUds9sbs_GtJyINBt41N2m0rhzw0qd9e0PPiSB0Cz8_Zw8WfMo5oQkRA4o8Hx5YIEIFJTvgLhSB3kxOv-LUzUBEel_0NT7wa8h6nhGX7oZSR7Z6PwVElXq1aSAkTO0y97Ez9_4shlXZjje_2dT9x8KqkomoUyXH5iOppCCRGvLa6sO3FEp353M6r_EFEA2y8gPdAZZiwnwKVHW0QksDqnv-dGjfBl8JcAePvMjWbDiKaAfDzBtVItcnlUxm_I-9UzwehI-l-_c7cM5OMaPtqDMKXoz247paeFA24NsGn-LTHim71jvkJLFq369hDEF5rgRmAaGH4cR1urCYOFrMFp7_L3sSWm6hE22IYOuQ760SWlnttZu-5dGjflc1EnzB9c8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁨ بیمه زندگی و سرمایه گذاری پروژه محور
یک‌ سرمایه گذاری کاملاً امن،
با ۴۰ درصد نرخ سود در سررسید
به پشتوانه و تضمین
#بیمه_البرز
معاف از مالیات  همراه با ارائه پوشش بیمه عمر
#بيمه_البرز_توانگر_و_ماندگار
#بالاترین_ظرفیت_مجاز_نگهداری_ریسک
⁩</div>
<div class="tg-footer">👁️ 1.01K · <a href="https://t.me/akhbarefori/691530" target="_blank">📅 21:00 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691529">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/761a1bd315.mp4?token=nSa4aSVZZl8Yla7oBBvYJfGsefh3R7FE4bTX-qEZjm49QvG_uxh26SHwutD5LDlZ7G5w79TIyaCZ8vyairskpnKT91X5RXLf8Fnt5GnZNOxYLNUsNnUyqk7e6olpsXjMcTNXnepm2fkynZhWefuf2P0Jo-CvIoXq8QSoHpeJ1bpATqXInHvuat0cUp9pT7-CyjOrepEdHxR-u1FbGO0STxMHhuEe5R1wMDjaDUfFZl3ZT8iOHwbVRoWZzqcl7HTqYSR6tKcyzURTjZwfaco44HfJYRd-6xkJgNGpOFTB6hbpV_AGpHiQDwyUAhlQDP7qMdYX4vZEiXLpXeNkKgxSIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/761a1bd315.mp4?token=nSa4aSVZZl8Yla7oBBvYJfGsefh3R7FE4bTX-qEZjm49QvG_uxh26SHwutD5LDlZ7G5w79TIyaCZ8vyairskpnKT91X5RXLf8Fnt5GnZNOxYLNUsNnUyqk7e6olpsXjMcTNXnepm2fkynZhWefuf2P0Jo-CvIoXq8QSoHpeJ1bpATqXInHvuat0cUp9pT7-CyjOrepEdHxR-u1FbGO0STxMHhuEe5R1wMDjaDUfFZl3ZT8iOHwbVRoWZzqcl7HTqYSR6tKcyzURTjZwfaco44HfJYRd-6xkJgNGpOFTB6hbpV_AGpHiQDwyUAhlQDP7qMdYX4vZEiXLpXeNkKgxSIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رژه مادران و کودکان در رزمایش جانفدا به یاد شهدای میناب
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 3.02K · <a href="https://t.me/akhbarefori/691529" target="_blank">📅 20:55 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691528">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">♦️
رئیس شورای عالی سیاسی یمن: اعلام می‌کنم که نیروهای دشمن سعودی از تمام مناطق ساحلی غربی یمن اخراج شده‌اند
/
باب‌المندب به‌جز سعودی برای همه امن است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 9.71K · <a href="https://t.me/akhbarefori/691528" target="_blank">📅 20:44 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691527">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3423be4c7.mp4?token=ozj2xC2NwdSaMmGC-xklx3ZlF0rbgMvo_n6CmYI3ll1H2vRVBBlYUaRc1LDSo-2vwER5wRnCR0osX606X6nKztXDZP2yqD8snRVCAc7xPjyk89ElMMI1cGt0BlZ8sgdB0mAV4lJtojLzkXtLeamPg-2D72RFnLiEg3z81Dmg_T3kw2MRZvd2dpGqKONZpoTb6bN4oQcSGCAf-Vhrf2Z2DCSDsMBpf27DyqMxOD6LUJkRq-xCUYjN9kITFsr-OShP22TkMLHkLBycHUDMoDhYeG5o4Cf3bDlLSDUtJG97YVrG01Lr330F3Hgte50LtwkgvmvZ9utjSsmEMxNsrQoG5wWpiu5qyVa8gZVav5NfrWpMiwGYQb9ynRthxBiHNXj5mZXUoD-dqtBQKbce385sn4I6Gee7DaRrMO9jpt_FQeDeqAKdlsgnMcCueEC08oYUSMGGKqc5hvdg2W9APN8w3qIJvZZPK1fA8IYExUobHpWMfiOcdANqg6aJf0vGBGgdYWOBH0VEHa3p_hrv8TLEvzU065pD8Tz0MRolGt1vpXHHpK_GhPgOkXytjLIu9xwOXfEv47WCuh2Ma6R1_4Dc96BwR53_PTCHL5wIBV8pq-pTxHuIWVjkZvNnUnh41dpnvJFE7KP66P03IxlN5Ls0VDUsmZNG2vF7mnIUiK1WpDE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3423be4c7.mp4?token=ozj2xC2NwdSaMmGC-xklx3ZlF0rbgMvo_n6CmYI3ll1H2vRVBBlYUaRc1LDSo-2vwER5wRnCR0osX606X6nKztXDZP2yqD8snRVCAc7xPjyk89ElMMI1cGt0BlZ8sgdB0mAV4lJtojLzkXtLeamPg-2D72RFnLiEg3z81Dmg_T3kw2MRZvd2dpGqKONZpoTb6bN4oQcSGCAf-Vhrf2Z2DCSDsMBpf27DyqMxOD6LUJkRq-xCUYjN9kITFsr-OShP22TkMLHkLBycHUDMoDhYeG5o4Cf3bDlLSDUtJG97YVrG01Lr330F3Hgte50LtwkgvmvZ9utjSsmEMxNsrQoG5wWpiu5qyVa8gZVav5NfrWpMiwGYQb9ynRthxBiHNXj5mZXUoD-dqtBQKbce385sn4I6Gee7DaRrMO9jpt_FQeDeqAKdlsgnMcCueEC08oYUSMGGKqc5hvdg2W9APN8w3qIJvZZPK1fA8IYExUobHpWMfiOcdANqg6aJf0vGBGgdYWOBH0VEHa3p_hrv8TLEvzU065pD8Tz0MRolGt1vpXHHpK_GhPgOkXytjLIu9xwOXfEv47WCuh2Ma6R1_4Dc96BwR53_PTCHL5wIBV8pq-pTxHuIWVjkZvNnUnh41dpnvJFE7KP66P03IxlN5Ls0VDUsmZNG2vF7mnIUiK1WpDE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گیاه‌ها پژمرده می‌شن؟ با چند نکته ساده، گیاه آپارتمانی‌ات رو شاداب و سرحال نگه دار!
🪴
#ترفند_فوری
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 9.72K · <a href="https://t.me/akhbarefori/691527" target="_blank">📅 20:43 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691526">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">خبرفوری
pinned «
‼️
خبرفوری/ انهدام یک فروند پهپاد شناسایی پیشرفته اوربیتر بر فراز تنگه هرمز   روابط عمومی ارتش:
🔹
ساعت ۱۸:۳۰ امروز، یک فروند پهپاد شناسایی پیشرفته اوربیتر با آتش سامانه‌های بومی نیروی پدافند هوایی ارتش در منطقه جنوب شرق کشور، تحت شبکه یکپارچه پدافند هوایی کشور،…
»</div>
<div class="tg-footer"><a href="https://t.me/akhbarefori/691526" target="_blank">📅 20:31 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691525">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h8Pn3mV005tFg97z5svSxN62oXEaqurHhXUCBiDtNgpaNy41s9MX-v62A1Qyt2K8QBW-IwrgxqboNU9c33HBOlCAQMu-ii74jwN86r2HwL1SkgF4J_wYQijv_SDyH2pmgzPQxDwPqIjrsxjdc0b-f6nuOiGMGOmrOHIj_ra1hOE5L4J_0mUVs6Z5e3XsP9F14l1iuos9_73M-jtRSDt4l2AilcPxNIFg9DdiqmfkvnVV5Ujrw-POYF7z7wlpfWr9p7KuZ8ENetElJM-TdSukqoblmtm2V6AIvo-JiVK1-BLqp6TO7aNeqEp706WDgS0zePe1JwRHGFmbHoHRjBjDcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اینها صندل‌های ۳۰۰۰ ساله توت‌عنخ‌آمون یازدهمین فرعون مصر هستند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/akhbarefori/691525" target="_blank">📅 20:31 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691524">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">‼️
خبرفوری/
انهدام یک فروند پهپاد شناسایی پیشرفته اوربیتر بر فراز تنگه هرمز
روابط عمومی ارتش:
🔹
ساعت ۱۸:۳۰ امروز، یک فروند پهپاد شناسایی پیشرفته اوربیتر با آتش سامانه‌های بومی نیروی پدافند هوایی ارتش در منطقه جنوب شرق کشور، تحت شبکه یکپارچه پدافند هوایی کشور، بر فراز تنگه هرمز مورد اصابت قرار گرفت و منهدم شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/akhbarefori/691524" target="_blank">📅 20:24 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691523">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6cd208e723.mp4?token=YNQZu4XKAtbW9lqgVDBc-StOtsyVZ-KW9UF3rmB7Y8oPOq1hiKxT21sLqCEFB1b04pCO-PQI_EfbuwZ8blDwbGp9OJb5kk_faX2PTbOWCuyOhDQ-ulR88IM8kpW7Fy4aAOVC-CaVIOi9yi14QG2pZOrg-vdGxuTdeRQVT2Lc2rrJ3ELy3gVjtf-yAowbH8N639oGuKcZYfjJluDwerCfbw1Jm_-KmwvcNLdmc2EvFJCWcvsh1nLOU2QMPu6fwWHRHUnXP8qiqmkKhYIU2wGErMIQHmT53swrK6SrjNro0bq32QioOEGfrdwgQ083u3sb0I9Oa2wirkJXH_iKDXgDEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6cd208e723.mp4?token=YNQZu4XKAtbW9lqgVDBc-StOtsyVZ-KW9UF3rmB7Y8oPOq1hiKxT21sLqCEFB1b04pCO-PQI_EfbuwZ8blDwbGp9OJb5kk_faX2PTbOWCuyOhDQ-ulR88IM8kpW7Fy4aAOVC-CaVIOi9yi14QG2pZOrg-vdGxuTdeRQVT2Lc2rrJ3ELy3gVjtf-yAowbH8N639oGuKcZYfjJluDwerCfbw1Jm_-KmwvcNLdmc2EvFJCWcvsh1nLOU2QMPu6fwWHRHUnXP8qiqmkKhYIU2wGErMIQHmT53swrK6SrjNro0bq32QioOEGfrdwgQ083u3sb0I9Oa2wirkJXH_iKDXgDEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نمایش اقتدار موشکی ایران در رزمایش جانفدا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/akhbarefori/691523" target="_blank">📅 20:24 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691522">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">♦️
تکذیب الحاق حریم تخت‌جمشید به شهر
محمود رضایی‌کوچی معاون استاندار فارس:
🔹
الحاق بخشی از حریم درجه ۲ تخت‌جمشید به شهر، صرفاً در حد پیشنهاد‌های اولیه کارشناسی است و تاکنون هیچ طرح مصوب و ابلاغ‌شده‌ای در این خصوص وجود ندارد./تسنیم
#اخبار_فارس
در فضای مجازی
👇
@akhbarfars</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/akhbarefori/691522" target="_blank">📅 20:23 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691521">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd51ad34a3.mp4?token=nIUbDJkraOcFPEIG89jZghUr0iBYlFNYKbUIn1n5zNL-FIQ5rd0HDkMQ-j8HT2BoBkaXoHJ_2PuKxCl_tx0GAG4ZNhX-eCPRmAsvyuRlickFGagww-GMHqfVb5YvCM2VVDivoQb4RKErg5NBcTA2bfeqzpnt9kn-OhcfcLezHFWRyWbAQE940OUN2Yloj7Ok0qbRYktODlyig7xKXogEEtxjogvcZhH2tNrjmN4HUdZbGviOIiccm4hfV7MHEOd4KJmq9bNqe3278s4yI7owsen3Gm-vjuA2RDKQ1bCxrHPFCaxaB35C6UuPgP6GuXpBKB5KzCfQHiMIVQr25e6RWSKPrZcCPnk6IFjf1Irsh7ey2I7YsyDrw6N8c-yNnwCPw6qvegUWdgyWJZIms6yusnXV7g2Bu0EJJembo3c74uy4w6HJzxlA9FTFIdstbForL9BnMyWFTM4xaguCR7b2KJKyYUjT-uC-x7qvnhc2C7pLpfgN0jdv8sS3CG19wPwK4WcMLRNVOv7yR8NqPoK4FfPMdvwPLaH9MWsk_LPmFGJtt2pfE82a6IXYm8-xrUqSC8Fm8p7e9AzIcYMz3tUiFSCo609FemkDf6Kf88SvtkG_-uzRqupULOmk_ccz25KJx4MgaAPdDNz4NMwOv5TbYO9_fmqFOYI7uzF4EKaNgtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd51ad34a3.mp4?token=nIUbDJkraOcFPEIG89jZghUr0iBYlFNYKbUIn1n5zNL-FIQ5rd0HDkMQ-j8HT2BoBkaXoHJ_2PuKxCl_tx0GAG4ZNhX-eCPRmAsvyuRlickFGagww-GMHqfVb5YvCM2VVDivoQb4RKErg5NBcTA2bfeqzpnt9kn-OhcfcLezHFWRyWbAQE940OUN2Yloj7Ok0qbRYktODlyig7xKXogEEtxjogvcZhH2tNrjmN4HUdZbGviOIiccm4hfV7MHEOd4KJmq9bNqe3278s4yI7owsen3Gm-vjuA2RDKQ1bCxrHPFCaxaB35C6UuPgP6GuXpBKB5KzCfQHiMIVQr25e6RWSKPrZcCPnk6IFjf1Irsh7ey2I7YsyDrw6N8c-yNnwCPw6qvegUWdgyWJZIms6yusnXV7g2Bu0EJJembo3c74uy4w6HJzxlA9FTFIdstbForL9BnMyWFTM4xaguCR7b2KJKyYUjT-uC-x7qvnhc2C7pLpfgN0jdv8sS3CG19wPwK4WcMLRNVOv7yR8NqPoK4FfPMdvwPLaH9MWsk_LPmFGJtt2pfE82a6IXYm8-xrUqSC8Fm8p7e9AzIcYMz3tUiFSCo609FemkDf6Kf88SvtkG_-uzRqupULOmk_ccz25KJx4MgaAPdDNz4NMwOv5TbYO9_fmqFOYI7uzF4EKaNgtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پلیکانی که به مهدکودک می‌رفت!
🦩
🔹
«کاتّا کون» پلیکان ژاپنی بود که از سال ۱۹۸۹ به مهدکودک می‌رفت و با بچه‌ها وقت می‌گذراند. او در سال ۲۰۰۸ درگذشت و داستانش بعدها به ساخت مجسمه و یک مستند درباره ۲۷۰ روز رفت‌وآمدش به مهدکودک منجر شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/akhbarefori/691521" target="_blank">📅 20:18 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691520">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q03mb_i0Ff-VcTJ39Qk0N9Nailj1uyHvSb0fWbR-YQc1O_w9w8KiJ-xvChTdHeFBGxHoMUc4JAG4BdObJ-UasCgJdKsvyjqUk7gQzG6Jhn6qlTH__KgHXIqoMh9uz5GdQk4nEr5rSuNVcAJG_1VfQLPc9jY0HQgVT9gkfAtryyuJXN0sIqEAlHsrN7O04BtyE8uryZ8w_xofgFqWihii_oCxVC2ruHrYGwLcyXjzDlSuuFwBo0Ddg6-ZUvX6l-9_eYaWn-ZdsNwr9OrDSDclorN0msMa25FvYRf1GDqpqoaU7cPZCQBI2edEPJiS7hixa94w2X31_Ye0Cxitl0mfkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دارو، درمان و خانواده‌ها | تحریم صنعت هوایی ایران چه تاثیری بر زندگی مردم گذاشته است؟ | آیا آسمان ایران بسته می‌شود؟
🔹
تحریم صنعت هوانوردی ایران وارد مرحله تازه‌ای شده است؛ مرحله‌ای که آثار آن فقط متوجه شرکت‌های هواپیمایی و زنجیره تأمین این صنعت نیست و می‌تواند مستقیما به زندگی روزمره مسافران ایرانی سرایت کند.
گزارش خبرفوری را اینجا بخوانید
👇
khabarfoori.com/fa/tiny/news-3246674</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/akhbarefori/691520" target="_blank">📅 20:14 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691519">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rlcFfwyfLTVdlTHDgH7ABkSZw2SKiDACX0rnNALdWFGog0teQRdkXmnKn4gHVaXs2B-u7yq2JDqLQ1vKMfCFzCGYTJD2GnR3QPjpTcZOVXc8RErY48MjqmQFmH3fBkJYs-iFGp2IejZzcfSL7yW_913TPbPyaQZxKpJ9bP87gFE6tibSAQMtkMfdBcTftYZybD8LuuTuwz2E0-C5tIPp8JMsImjNpYjEeosvoIy-zkoI5DlWF5mb93wDSCshxekw8vW75TWNS82OKLVxncZ6Bi-TnQ97CBc5C9XmAnn5mlk4rpZ1QRzlpfK9baTBjdy6FGv06eXOJ--fbI2lWkQehg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترامپ تصویری منتشر کرد که سی‌ان‌ان، ام‌اس‌ان‌بی‌سی و پولیتیکو را به شکل کیسه‌های زباله در بیرون کاخ سفید نشان می‌دهد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/akhbarefori/691519" target="_blank">📅 20:10 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691518">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">♦️
پزشکیان: ما از هرگونه مذاکره‌ای که به امنیت و صلح پایدار منجر شود استقبال می‌کنیم/ الجزیره
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/akhbarefori/691518" target="_blank">📅 20:09 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691517">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">16-2 Ane Manaee (1404-02-01)Shahre Moghadas Ghom</div>
  <div class="tg-doc-extra">@Aminikhaah</div>
</div>
<a href="https://t.me/akhbarefori/691517" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">♦️
تفسیر سوره محمد| جلسه شانزدهم؛ بخش دوم
حجت‌الاسلام امینی‌خواه:
🔹
نقد و تبیین مشاهدات شخصی از انحطاط، حس‌گرایی و نادیده‌گرفتن عقل و حق در جامعه [00:06]
🔹
مرگ؛ معیار تمایز حق‌گرا از حس‌گراست. اولی مشتاق وصال حق…دومی هراس‌زده از مفارقت حس [07:33]
🔹
سیر حرکت حق‌گرا؛ از تعبد تا اتصال به حق، و توقف حس‌گرا در غرایز و توهمات [17:53]
🔹
حق‌گرایی یعنی؛ تبعیت از قرآن و دوری از تناقض‌های رفتاری و نفاق، بدون توجه به پسند یا نپسند مردم [23:43]
🔹
«قاعده تضاد ناپذیری حق»، تقابل میان اهل حق، نتیجه اشتباهات و جهل است نه تناقض در ذات حقیقت. [27:52]
🔹
ایمان به قرآن تنها راه رهایی از سوگیری‌های شخصی و تناقضات رفتاری [30:38]
🔹
بهبود حال و هوای روحانی، محصول رهایی از حس‌گرایی‌ست، اما تشتّت و گرفتاری نتیجه دلبستگی به دنیای مادی [36:49]
🔹
تأثیرات متضاد قُرب و بُعد به عالم نور و وحدت و عالم ظلمات و کثرت [40:10]
#تفسیر_سوره_محمد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/akhbarefori/691517" target="_blank">📅 20:08 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691516">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">♦️
آمریکا به‌دلیل شرایط امنیتی، تردد کارکنانش در عربستان را محدود کرد سفر به «طائف» و «ینبع» نیازمند مجوز ویژه است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/akhbarefori/691516" target="_blank">📅 20:07 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691515">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ebd9cab305.mp4?token=HwkFqoQboL2wkGB8TGbtu6YTliF8m0zrunjP3PWgNE6jhlQw_tTXPdbnY3MK6_EbzxtjAZRW3qLQD1ZeGts_-XA3tFpZHvDN14GEBPh6TXCMx3kOjD2jAYypG9oerlhPU8EIv2dv6nxtXaTbiBn6QuqTMvJvkSRFaMd1DLEpwJdpEHxObn_CuCiUQPXCE4lIWphrH2V4Z-CgCwFShK76Ia-9ejbC2uTmtj1Rr5U5-gq-65CEt6BLrWSZHhaWkFVqv4R2h3MBfvbo7bjHgcWFdjOmnv_2XVm_tOWtsksRiF5BfBk6PecVCGXvSobhnjYwLrUA8KIFwTWgV0eSNNizMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ebd9cab305.mp4?token=HwkFqoQboL2wkGB8TGbtu6YTliF8m0zrunjP3PWgNE6jhlQw_tTXPdbnY3MK6_EbzxtjAZRW3qLQD1ZeGts_-XA3tFpZHvDN14GEBPh6TXCMx3kOjD2jAYypG9oerlhPU8EIv2dv6nxtXaTbiBn6QuqTMvJvkSRFaMd1DLEpwJdpEHxObn_CuCiUQPXCE4lIWphrH2V4Z-CgCwFShK76Ia-9ejbC2uTmtj1Rr5U5-gq-65CEt6BLrWSZHhaWkFVqv4R2h3MBfvbo7bjHgcWFdjOmnv_2XVm_tOWtsksRiF5BfBk6PecVCGXvSobhnjYwLrUA8KIFwTWgV0eSNNizMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سیگار کشیدن چه تأثیری بر بدن شما می‌گذارد؟
🚬
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/akhbarefori/691515" target="_blank">📅 20:02 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691514">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">♦️
پزشکیان به نیویورک می‌رود
🔹
بر اساس برنامه فعلی، مسعود پزشکیان برای شرکت در مجمع عمومی سازمان ملل به نیویورک سفر می‌کند و ضمن سخنرانی، با برخی سران کشورها دیدار و رایزنی خواهد داشت. یک هیئت بلندپایه نیز او را همراهی می‌کند./ تسنیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/akhbarefori/691514" target="_blank">📅 19:57 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691513">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd823234ef.mp4?token=Rgu2sOFn8A67kndPtyYp21VVIK27YnB7lWuu8CdoDZYz4kxt8YhIrS9wZnsuN432RpmBUvxz14h4dr0dIsFkPW0IgUlaigjXD1HhxB2_B_b8p3jWNLYhaesYRghlrZ0AT_vSy-Iuw5WeyINqGiArYiBr8dFXG6lTg6gNpnwdZ0l7Uw9unnW7kFfDvt1-BnwTPbPDFAPRZV1xmJZe4Zxy9acb8mexlDUKo9iIf_UmDkZ40g5607bj0Sp6kqhjfi9dQnCwlxEZ8SQDqnfbdp_3xf79EHOSXS6e2Eac8AfeolvJE8flrw6eISwHGaQu8yaePUIjniR50BxIabwUjxfYpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd823234ef.mp4?token=Rgu2sOFn8A67kndPtyYp21VVIK27YnB7lWuu8CdoDZYz4kxt8YhIrS9wZnsuN432RpmBUvxz14h4dr0dIsFkPW0IgUlaigjXD1HhxB2_B_b8p3jWNLYhaesYRghlrZ0AT_vSy-Iuw5WeyINqGiArYiBr8dFXG6lTg6gNpnwdZ0l7Uw9unnW7kFfDvt1-BnwTPbPDFAPRZV1xmJZe4Zxy9acb8mexlDUKo9iIf_UmDkZ40g5607bj0Sp6kqhjfi9dQnCwlxEZ8SQDqnfbdp_3xf79EHOSXS6e2Eac8AfeolvJE8flrw6eISwHGaQu8yaePUIjniR50BxIabwUjxfYpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
متفکر آزاد؛ نماینده مجلس شورای اسلامی: جان‌فدایان ملت ایران؛ ظرفیتی که دشمن را غرق می‌کند
🔹
جان‌فدایان این کشور به گروه، گرایش یا قشر خاصی تعلق ندارند؛ آن‌ها و هرکه دلش برای این کشور می‌تپد ملت ایرانند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/akhbarefori/691513" target="_blank">📅 19:55 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691512">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">♦️
قیمت زعفران از کیلویی ۳۰۰ میلیون تومان عبور کرد/ ایرنا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/akhbarefori/691512" target="_blank">📅 19:52 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691511">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k72DOG3jSb8brOjCZYarMMhsxdmJIBhVJ-5y7bl7AEFVptKciqO7_64bwEa-Gkdky3p8ZgwSPTIZBTwx-5_eCAewur3hxanU1XA4mv_nMx9bgnY68HlMK_DeMzOz21RAPPEcqvZVCPVD-OdCnWHyXVACSZwG-RtU2JuoCTEEbClP7txbCmMkE33SKXTxeJEQcWPBhfF90_0gUcjBKii8wzm_R8xn3jXp1DEETbQyXYTqrK3X366t7u8VQujj4Z3bqWyhZe8nFgnY-vljzyveIxR_Fq2tmAIpXaafzq2V13kA2qcJo3GFV7uU1_LTVgrN2UJrZck1UbH9aqxSwRjakA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با پایان تابستان، موج گرما بازمی‌گردد؛ تقویت پرفشار جنب‌حاره‌ای موجب افزایش دمای ایران تا بالاتر از نرمال طی هفته آینده خواهد شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/akhbarefori/691511" target="_blank">📅 19:47 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691510">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W4472dofrvTUr6jOr5FAVqinK1bNc_bzbcViSR5W3gF_jb_ySosfkQfKgREZ4BnYEFxHHxfSw3lh7ocziEs9cvXnxTEU0hc5qsxy4R4q3Rm6DFjutOKEhptFmuDe3dBr-ktL8tHD2kMQ1G_7puPDctv6RxAUNSDqKFqQRAoXXw6Yxv4IE35U8XR7yvM3585EhspH0nppOJed4v9I-U6YNVngA0mhx3p3AUP48TWxGhvT0mVHHUp0JfsC94XASiwBUxxxSJ98p1l_b8MqDAZYxL0D2i0VsuU6EAnSE3FqzwIr8PNbz796m2c81sADhVTOPoGF4aAv1TkPsqeh4mtjzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
برخی منابع خبری غیررسمی با استناد به داده‌های فلایت‌رادار ادعا می‌کنند عباس عراقچی به قطر رفته است/انتخاب
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/akhbarefori/691510" target="_blank">📅 19:35 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691509">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
ادعای
سنتکام: مسیر ۱۰۹ کشتی تجاری را از زمان ازسرگیری محاصره دریایی علیه ایران تغییر دادیم
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/akhbarefori/691509" target="_blank">📅 19:34 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691508">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sbqnBV1txgjbT3yGCSivJCKnz1serMOF5uBBv-_GuD7Us10WVwfNhtoseIB5luTs0HiSdWnHyA12xgbyYS6e5qd-N7cHj85FFScBaX8ROv17ROV1tNU3q2S3JYtDlcv4uaB8Bm3x-7fm5PPMqSIf_hp0PERamnLVkKOPlMNnrMK4-_iNP5K_Z8PEt0_b8HMEgQSSGdTAnMl6jNvOuLG8WCVyqe6m7wJw-RoWxotNk6JNFQfQvUGFTZuU0phf4MlVzs8WGMYbc_uQPxbs2SYv04PYVBeU45Oc3kzqq5G-_XAID3bePqAZ4WCeK0xCUIXQtC_TJmkbs2kvzJXCt9qu2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آشنایی با انواع دهنده و گیرنده‌های گروه خونی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/akhbarefori/691508" target="_blank">📅 19:29 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691507">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vW4WyvxelqEh-hEpHC36MZvUB774kV90tfeAtH78q3BIsh6Z8RIdAHouFyzAS0gER186qow4Xr-t-S8xGS8q_af7U1cZGnozueARSgYJrhX_q2qJlBCp-cfpNH-TBG5bfhEgkQ2onWJWC5C0eolyKh40HxN9XBP5oKTJFi9AoLDmGaNMdRdcV62NA2zDqlf7iXkJC5JINvLbJJgvqlIyczMluS3du_qMcR1cxQWse7OF16wxg_ObCnlqh-ozPOuLsmAe5nfQK7i16dVHQBU8A5ui5ui1KWXelaJmiyalX7XHGPGz3VGTvcqtLcMwQVIfYLwFqFQ1clHec2qHxnjB9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۵ راهکار مجاهد برای تبدیل ظرفیت «جانفدا» به نیرویی برای حل مسائل کشور
🔹
مهدی مجاهد، معاون پیگیری‌های ویژه دفتر رئیس‌جمهور شهید: حضور مردم در تجمعات شبانه و همراهی با پویش‌هایی مانند «جانفدا»، نشان‌دهنده یک سرمایه اجتماعی ارزشمند و آمادگی ملت برای فداکاری و مشارکت است.
🔹
این ظرفیت اگر به‌ درستی سازمان‌دهی و هدایت شود، می‌تواند از یک موج احساسی به یک نهاد پایدار مردمی برای حل مسئله تبدیل شود.
🔹
محله‌محور کردن، ساماندهی داوطلبان تخصصی، پیوند با تولید و اشتغال، استفاده از ظرفیت مردم در بحران‌ها و ایجاد سازوکار شفاف برای ارائه بازخورد پنج راهکاری است که این ظرفیت را ظرفیتی برای حل مشکلات کشور تبدیل می‌کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/akhbarefori/691507" target="_blank">📅 19:27 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691506">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BCpp-KE0XvabeddA-ozVDwGZwmnk9mcg3uy3ZhtJ9qzeLkotKyk6LAork47wxU6nRbz9B6NUQhQr7fO7rDoZEjp68ujLAB0uQktnrkkAq0_-Q0Ln-sYB4e5imzJ2kNatMbvQvQD8bPiT0YZnywyAVFeqDI2r5WfluBRc_wWsRtYwuvgUUYlzCBrfFXh4YMN5RVsdffElg1WCKtNLBZpBywlLbp_-_DssfjIiAsJWodtATA0WxXs1uEDB9K81r0uD12rFWRhHyuvRwSRsXuPa-siZwwceShjFIJWH3OJPaufOzrwk1XaFF5coRQKFkzS8m0IJVfYhkzXPKHUwcUJcLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ایلان ماسک مجوز بین‌المللی اتصال مستقیم گوشی به ماهواره را گرفت
🔹
کمیسیون ارتباطات فدرال آمریکا مجوز بین‌المللی Section 214 را به SpaceX داد تا Starlink Mobile بتواند خدمات ارتباطی بین‌المللی ارائه کند؛ مجوزی که مسیر توسعه اتصال مستقیم گوشی‌های معمولی به ماهواره‌های استارلینک را خارج از آمریکا هموار می‌کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/akhbarefori/691506" target="_blank">📅 19:24 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691505">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/im58CDRT3lntAyPRjKdwCq1ZU21XhUyxQTofJ5i8cyeCiIF4xgPYeo6QVy9tVtYb_0gogKOPb1z7EEJ07yZ-p6I33GVK6SKegq3DP2_5gqX0J8Mhgy8SrZPGEEtMB0rCFtwGFp9bLA0nslg4pF7GigqmOvY8kfkT-0frE-MeYpCxu03TCuAebgHX9amC_BzXAVOxbYThj4kWcSiTSO4DvmL_rVByGhI1JDj9n0OmGU58-SP7RZ-6dqboTxEyNXYs8XoKUYSEH2fXExQ_-0ks85g29L-Kwz3gPpiqUj5K1ndCbZz8CDju_p_5kDRZ6N7KUUsneTfpU--pqsphZhIrJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سفارت ایران در لبنان به نقل از رئیس‌مجلس: تنگه هرمز تا تحقق شروط ایران باز نمی‌شود
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/akhbarefori/691505" target="_blank">📅 19:24 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691504">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LVCnpihh8lI48aicdSZmK-zme2dS0-yx6ZhEQsA-c8xyMBYKr2XXyavz2mj0NB1PvII-1yQDwFMq09l77ey2-ErqluCNg0acqazM76aNzzQiCRIiT9CXaJ1C-L2ZcJEJezin5FD0NLqiDPiTfwD2YqPIeU8Q31LUrgUUYMSIOTWUPONYUvHWdWlP3P2HisvF9cqOJUhKcgRgRZHqmAhOEpfdNHo2Y8LFdL7QuqLLTFxZEtOf_X9L0y_BhA9IrSiLEjtfjJ9adCO6tfIOHxZ9brWvx1mTp7v41MG5LIhhQG7RnvzbFmROlcKVUbALXbk-dWbCYOMc0W7C1PvRG3x56g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اوکراین یکی از بزرگ‌ترین موج‌های پهپادی خود را به سمت مسکو پرتاب کرد
🔹
روسیه ادعا می‌کند بیش از ۱۶۰۰ پهپاد سرنگون شده است، از جمله ۴۵۰ فروند که به سمت مسکو هدف‌گیری شده بودند.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/akhbarefori/691504" target="_blank">📅 19:18 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691503">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4fa58cfcca.mp4?token=k2osmf3lEO75VZOtpbwRZxdsuycxxPJQmmTDLO79uW_yj1Z2KXdtx1upz4QDaehR9cr_XmDaDamrhH38dr3lUtXhcqP0vqDSi0Po6q7DEQojQQu-I6pk1WoQOc6p8dXXsRUIG67JLFaV2cbIF13m5eXuPaJgeqLtx6g_DZNyv8EMdbJDVMBKa_hPgQfw4SxigAfKl3BZMerp_tQY2S5mYPjbvIaXtioJxQOEWYx1z2n5Ak4hayL3A0DlhRFhXYEhFOdZYY_Bz33Immui4AE_XrXfpWLhTsUGJ5DwQKEbgfyq4SZmuW3M0Fu4MspGEqvuTG3oYmtl84fmDH415Alz0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4fa58cfcca.mp4?token=k2osmf3lEO75VZOtpbwRZxdsuycxxPJQmmTDLO79uW_yj1Z2KXdtx1upz4QDaehR9cr_XmDaDamrhH38dr3lUtXhcqP0vqDSi0Po6q7DEQojQQu-I6pk1WoQOc6p8dXXsRUIG67JLFaV2cbIF13m5eXuPaJgeqLtx6g_DZNyv8EMdbJDVMBKa_hPgQfw4SxigAfKl3BZMerp_tQY2S5mYPjbvIaXtioJxQOEWYx1z2n5Ak4hayL3A0DlhRFhXYEhFOdZYY_Bz33Immui4AE_XrXfpWLhTsUGJ5DwQKEbgfyq4SZmuW3M0Fu4MspGEqvuTG3oYmtl84fmDH415Alz0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ماهی ماندارین انگار مستقیماً از یک نقاشی سوررئال یا دنیای فانتزی بیرون آمده! این ماهی یکی از خیره‌کننده‌ترین موجودات اقیانوس آرام است
🐠
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/akhbarefori/691503" target="_blank">📅 19:05 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691502">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MzF4rwLjKdcJseAvKVO0Wt4oQvW7dhugOND1J4u5AT-g-7x3-28187DaIcxbYXH3w2EdN6VefLTkWJz2FZzSQV27QbIsFOm8cuTq6NPCszMpKVbNckXQJfDiCsidJuJRGQmtL_bJsqI6P1PJ8rI9MTVluL4J2BIcF5-ChpqrVWLpx26EUvTAbUJDxEnyvZPWk1whYz2lS3tJoc5-_98k4uTWlgajAY7OLp2PkKmh12uxCic_Hfiq_ux2-8U_e9ric1FgmxpymRJCp_hpCD7IovhwvchUtmVmwyJpx_VZMDaR0AIfwzceMG431xqSwTln5CU52AY5lwFt1Q9d5GMFgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
تا ۵۰٪ تخفیف روی تمام محصولات چرم رجحان
اگر به‌دنبال
چرم طبیعی، طراحی شیک و خرید مطمئن
هستید
مجموعه
چرم طبیعی رجحان
آماده‌ست تا انتخاب متفاوتی برای شما باشد.
👜
کیف |
👞
کفش |
🧥
پالتو |
🧤
دستکش |
✨
اکسسوری زنانه و مردانه
🔱
چرم ۱۰۰٪ طبیعی
✅
ضمانت اصالت کالا
🔄
امکان تعویض و مرجوعی
🚚
ارسال سریع و مطمئن
💳
خرید اقساطی تمامی محصولات
با امکان پرداخت از طریق:
🔸
اسنپ‌پی
🔸
دیجی‌پی
📍
خرید حضوری:
مشهد، برج آلتون، طبقه همکف، پلاک ۶
🛍
برای مشاهده محصولات و ثبت سفارش، وارد سایت شوید:
www.rojhanleather.com</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/akhbarefori/691502" target="_blank">📅 19:00 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691500">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">♦️
رشد ۴ برابری قیمت موبایل در یک سال
🔹
افزایش قیمت تلفن همراه در یک سال گذشته، بازار موبایل را تحت تأثیر نوسانات نرخ ارز، افزایش هزینه‌های واردات و محدودیت‌های عرضه قرار داده است.
🔹
به‌طوری که قیمت برخی مدل‌های پرمخاطب طی یک سال دو تا چهار برابر شده و دسترسی…</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/691500" target="_blank">📅 18:48 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691497">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25c3c8eeb5.mp4?token=XXMIJt27x8SoEU9-_USech_sXjrAmeoTJ568Nn6qwSg3aRJ9NFuEDeYYQTrnn2sxiJwwGY6z018m0qATpsnAPT-yyFkZqKowpNhRvaisnWXqOzOCKtJQP6hYYR9fYcpEdE_2Zo8wG-QmrJ8H6l6r7tJZEkVbbbNrrk7emvSEwbMO4S7U9Prh5hpodw6AKjDmLdF3mRuuCzgMiWqsAvDSRnxbdioA0dcPIQYqSzxKI4LO8TwLW3Aga2IoxyMTvFwMt4dm777FNJFBsDc1MZKnPlDSYA6gH-Pm6LcQn4McdKA6Y7YRoMR2WRAVCWDKmVeYwKXhWeV9lfyBnwF-xKVvLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25c3c8eeb5.mp4?token=XXMIJt27x8SoEU9-_USech_sXjrAmeoTJ568Nn6qwSg3aRJ9NFuEDeYYQTrnn2sxiJwwGY6z018m0qATpsnAPT-yyFkZqKowpNhRvaisnWXqOzOCKtJQP6hYYR9fYcpEdE_2Zo8wG-QmrJ8H6l6r7tJZEkVbbbNrrk7emvSEwbMO4S7U9Prh5hpodw6AKjDmLdF3mRuuCzgMiWqsAvDSRnxbdioA0dcPIQYqSzxKI4LO8TwLW3Aga2IoxyMTvFwMt4dm777FNJFBsDc1MZKnPlDSYA6gH-Pm6LcQn4McdKA6Y7YRoMR2WRAVCWDKmVeYwKXhWeV9lfyBnwF-xKVvLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گلایه شهروندان از وضعیت نابسامان آسفالت خیابان تمدن
🔹
باسلام، فیلم مربوط به مرکز استان  می‌باشد، خیابان تمدن، بین تمدن ۴ و ۵ غربی. سالهاست این خیابان پر از چاله و چوله هستش ولی از سال گذشته تا حالا این قسمت بوسیله ماشینهای سنگین انبوه‌ساز کنار پارک تمدن بطور کلی خراب شده و روزانه ده ها میلیون خسارت به مردم وارد میکند.
(حسین نظری)
🔹
استان لرستان، شهرستان خرم‌آباد
🔸
ما در  الو فوری همراه و صدای شما هستیم؛ چالش‌ها و مشکلات محله‌تان را با ما در میان بگذارید
👇
#صدای_شهر
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/akhbarefori/691497" target="_blank">📅 18:33 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691496">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">♦️
رسانه‌های عراقی: یک پهپاد پایگاه نظامیان آمریکایی را در فرودگاه اربیل مورد هدف قرار داد/ خبرفوری
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/akhbarefori/691496" target="_blank">📅 18:32 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691495">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WRdkT_HLFC4RhzLdEdoZEF4owC5O5Ckk7FdaTeOKmSlfEkP8bhhcB63p3AI0fxaHSedsXOPicD0RwTaIMz2-lYfcDXPdL5ASnWr55zkETwWpN8O7W3A5BCZY_mksbmM1YEf6aGW_uWJ1Qv42FbgGthqif5OsdMgC9ZW-6lJTfWJfYDWwlpdZZLHfS8VVQEytwDQLaRSNpfAfx9lM-9diaX2OsVPdCeEORJSFtvklwrm9q4sta0hZ7Vy0rUSzfH0-GsIX6yOxfjJeSj7YZzmvvzgX_qtrZhjd1ampFEJS05VK8ufAj1hbAtX1_KcpeZNGAqgB9RvxXDW_xNF53Amjew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
توزیع ۲۵۰ هزار بسته نوشت‌افزار ایرانی برای دانش‌آموزان مناطق کم‌برخوردار توسط ستاد اجرایی
🔹
سید پرویز فتاح مدیرعامل بنیاد برکت ستاد اجرایی فرمان امام در آستانه آغاز سال تحصیلی جدید، از توزیع ۲۵۰ هزار بسته نوشت‌افزار و ۱۰ هزار بسته معلمانه با هدف حمایت از دانش‌آموزان و معلمان مناطق کم‌برخوردار و کمک به تأمین بخشی از نیازهای آموزشی جامعه خبر داد:
🔹
۶۰ درصد بسته‌های نوشت‌افزار ویژه دانش‌آموزان مقطع ابتدایی و ۴۰ درصد مقطع متوسطه
🔹
توزیع ۱۰ هزار بسته معلمانه شامل ابزارهای آموزشی و کمک آموزشی برای معلمان روستایی و عشایر به ارزش هر بسته ۲۵ میلیون ریال
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/akhbarefori/691495" target="_blank">📅 18:29 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691494">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
آکسیوس: ترامپ تعطیلات آخر هفته خود را در اقامتگاه کمپ دیوید نیمه‌کاره گذاشته و بدون هیچ توضیحی به کاخ سفید باز خواهد گشت
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/akhbarefori/691494" target="_blank">📅 18:27 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691493">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a45feae1ad.mp4?token=a1N20_xqWpCEQ_lIGEU4uvvPAGH5wvxuvZ1ThVgs2Cmv1HUftacW1oGy-S3aDwE6vJ3iwmusz9sSyV1biIx4gO5iGP6HcAHxxGElAILgv1VXr0YLHAD7tFPA1XH3kyWeHC67KM156LDPVGINtJNvIK0ZbvJO1xm7lB3BJklA-Ssw9IXq7u1Q4krk2oxa2tGQXBjrp7aJeb4HGh3wkgIzKEE1a2DAZTLAPVzdcjTZSa9GnFMAFZuhuyN4dyHbnmhuAfpY0OEwizYXCSnzFVja0vrNNkNbR0ZY1STMfhzKvsZ4Mpcujip4zpgHuAaPKo9GuQe7jzew1mDYIk9yl7y9_Y7WbwWPn2OFC6IvZwSpTuJVTirDWeZnLI1xpdXrCmaYbuRYWpAayDnYKzMEJ6AqbLe2qxG_NanFIDBi8Q4szDsjp7-vj6t7lp3loRDGHzOMhWW6h58kiWA9nGPYujEx1KCr3swIzQS9XlKhOPpsFCMd7VL5qDezFmuGg1j-szg6V4EONuwnkiyIi2F_CoWtoWGrm7rgJqTpisDR4SYa0fn5DeTmfkS5W7XuhMcMnFgx2yzzCUDavll6s0TCIYPTTS303uL-hbT2CBBWIrOaiQKZY55MaDLRbjXcGQSRg9nuX_2TNoEPyYKml0dOVPsGr7sMr58b_97dQk-h1wD8kAU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a45feae1ad.mp4?token=a1N20_xqWpCEQ_lIGEU4uvvPAGH5wvxuvZ1ThVgs2Cmv1HUftacW1oGy-S3aDwE6vJ3iwmusz9sSyV1biIx4gO5iGP6HcAHxxGElAILgv1VXr0YLHAD7tFPA1XH3kyWeHC67KM156LDPVGINtJNvIK0ZbvJO1xm7lB3BJklA-Ssw9IXq7u1Q4krk2oxa2tGQXBjrp7aJeb4HGh3wkgIzKEE1a2DAZTLAPVzdcjTZSa9GnFMAFZuhuyN4dyHbnmhuAfpY0OEwizYXCSnzFVja0vrNNkNbR0ZY1STMfhzKvsZ4Mpcujip4zpgHuAaPKo9GuQe7jzew1mDYIk9yl7y9_Y7WbwWPn2OFC6IvZwSpTuJVTirDWeZnLI1xpdXrCmaYbuRYWpAayDnYKzMEJ6AqbLe2qxG_NanFIDBi8Q4szDsjp7-vj6t7lp3loRDGHzOMhWW6h58kiWA9nGPYujEx1KCr3swIzQS9XlKhOPpsFCMd7VL5qDezFmuGg1j-szg6V4EONuwnkiyIi2F_CoWtoWGrm7rgJqTpisDR4SYa0fn5DeTmfkS5W7XuhMcMnFgx2yzzCUDavll6s0TCIYPTTS303uL-hbT2CBBWIrOaiQKZY55MaDLRbjXcGQSRg9nuX_2TNoEPyYKml0dOVPsGr7sMr58b_97dQk-h1wD8kAU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصویر آخرالزمانی از پالایشگاه مسکو پس از حملات پهپادی اوکراین
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/akhbarefori/691493" target="_blank">📅 18:26 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691492">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KqnYVecb4XTMlKFmZ-lthnjuVG2CLEPfVaM6LwdfYGo5nhgSDQcqJ63t-jynAb6q_eovyxbgxzpQYJCt7WyAaqstatmXbJmHDFqS3bcDWbyuCST5FK9msZj3lmGZJeDJnwqoaV4Xl8l2gEYmQa2SZcuQWznPaGf7M9LzyMZNhbu6UhSmkNHbXwt581WZT_dA_g9oONDFPKqK1NF6Z9yPUGMGhTigHDjT8JhsbQh6cVfCeMVadacgKrEt-CCH5g3NE9hr30dNj2mieLKUc8T_dclUUgddOcj6phjERnZkWVK3XOn7ipansl-_hAdZgc-bLF8mUackCdyS_-BoN_825Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پاسخ‌ بدون‌ درنگ
🔹
آمریکا هم‌زمان با افزایش تحرکات نظامی در منطقه، برای کشورهای منطقه و شهروندان خود هشدار امنیتی صادر کرده و نسبت به احتمال تشدید ناگهانی تنش، لغو پروازها و بسته‌شدن حریم هوایی هشدار داده است؛ در همین حال، قرارگاه مرکزی خاتم‌الانبیا اعلام کرده است آمریکا و اسرائیل با چراغ سبز برخی کشورهای منطقه و پس از برگزاری نشستی مشترک در یکی از کشورهای اروپایی، درصدد ازسرگیری اقدامات علیه ایران هستند. قرارگاه خاتم هشدار داده است هرگونه اقدام جدید آمریکا علیه ایران با حملات مستمر به مراکز استقراری و منافع این کشور در منطقه پاسخ داده خواهد شد و کشورهای همراه نیز نباید انتظار خویشتنداری نیروهای مسلح ایران را داشته باشند.
🔹
هشتصدوشصت‌وپنجمین شماره جلد یک خبرفوری
#تیتر_یک
@rozname_fori</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/akhbarefori/691492" target="_blank">📅 18:18 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691491">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">♦️
پایگاه خبری اماراتی العین مدعی شد ایران کمتر از ۱۰ روز پس از کنترل سواحل غربی یمن توسط حوثی‌ها، برای گسترش نفوذ خود در این منطقه راهبردی وارد عمل شده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/akhbarefori/691491" target="_blank">📅 18:17 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691490">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">♦️
روزنامه کوریره دلا سرا: ایتالیا آماده اعزام ۴ کشتی جنگی به تنگه باب‌المندب است
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/akhbarefori/691490" target="_blank">📅 18:12 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691489">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ljuoQMkqdi1hjRYA_fMmMHF4_HPGqWZbU5F-sIvj7d1DioOjt1kzUjzqI3a-eo3Tba4f1ipz5xxrQYzzJALFI3gW1xK6mjTqKq50aitHd8AU3W5YJe-o0NvkqA5r_5fqFIw16l7RGf456jNG0Wo8Vva92kqnyduKb6q4ft-ibEgSMof_ttM-nyJXe-8at42nrkJbnTJmz7Yhu8BlusFwWr-giq0szgfk_-QNljhWMxBLu-mAAEET4qdnshDa51ECJ-taOLty2BsqOzHCC3PE4cebSgxQEud1Eonlg_U-4tHQi8G-waEdGESvnz7KzrTguSI_bn-9MfN1b_rBhzqReQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کابوس آمریکا در جنگ زمینی با ایران/ این توپخانه‌ها می‌توانند آمریکا را حین ورود به ساحل نابود کنند
🔹
اگر تهاجم زمینی رخ دهد، توپخانه ایران می‌تواند در جزایر نزدیک ساحل، تنگه هرمز و مناطق کوهستانی غرب، تلفات سنگینی به نیروهای آمریکایی وارد کند. فجر-۵، فاتح-۳۶۰، رعد-۲ و ام۴۶ مهم‌ترین گزینه‌های ایران در این سناریو هستند.
گزارش تحلیلی خبرفوری را اینجا بخوانید
👇
khabarfoori.com/fa/tiny/news-3246661</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/akhbarefori/691489" target="_blank">📅 18:09 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691488">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromجاباما تور</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fWRBk5b7Nw5hcwY2oy_0lzSEljZMUzgWBXM-cYiPo3tuvABATQd1KJeYH-ACf4pBe8HEeiLHAJ8T8ZaZl29TOXZ7lebuDhu3-70k9ASyiioFgoZkKOJm1xN8IAVydldfE_FFpFgWBx8a6DthT43vWQJfxAzY4-UPfXLrBwMAsJ8ymOx3DMdX35Ig05ZwSkU6A8iG4S7i-0jYel9cdo3YY6G5gZ_ebzTAicHnDgNjOHE-gB5aGxT9k2anfZoKwUv1U2XHH_1b_kJdueqbZVaryr1QhvvsAME8hwc0GgeOFyGljSuVrRce3AqGByH2xIwkX709bCyyHfv79Oig8Ny2cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تا ۱۰ میلیون تومان اعتبار دیجی‌پی بگیر و
هزینه سفرت رو در ۴ قسط پرداخت کن!
تور موردعلاقه‌ت رو پیدا کن
:
🌤
از یک‌روزه تا چندروزه
💰
از ۵۰۰ هزار تومن تا ۵۰ میلیون تومن
🏕
از سفرهای آفرودی تا جنگل‌گردی
🎁
تا ۱۰ میلیون تومان اعتبار دیجی‌پی
✅
پرداخت هزینه تور در ۴ قسط، بدون هزینه اضافه
📞
برای انتخاب تور و راهنمایی رزرو:
02149275111
🌍
جاباما تور
@jabama_tours</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/akhbarefori/691488" target="_blank">📅 18:04 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691487">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">♦️
الزام درج نام کامل «خلیج فارس» در اسناد و مذاکرات
سخنگوی کمیسیون امنیت ملی مجلس:
🔹
طبق طرح جدید، استفاده از عنوان کامل «خلیج فارس» در مذاکرات، معاهدات، توافقات، اسناد و مکالمات مرتبط با شناورها و ناوگان‌ها الزامی شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/akhbarefori/691487" target="_blank">📅 18:00 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691486">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f78b96a18a.mp4?token=lSEJVdK_yqHY4xRgzHvXT4c3YnusZDgfF5nSMejMdfKJw0aBFM_ZnKavWWZFccOwosTr5H0JqFABjm4dACe6Uch0DF-NVqG4LxE7oEeV-PhQWJQP6lKF0XoE_hAuokVTgQAIJGMuwXAT3WWo5WENMWNYMlmYcrkAAUffhy18OLJhAE1P7zSCXpWQA3-ImRn-sir1fsHHJRaF7NDNnvmvKucMvOWhPOjjGrT3rWCXSKnNHeagS-xxZtbQJV4pX-vaJuq5isgwLVbpPReYLbcZll1LAoiQNDLHU2vjFIpZLJ9tw-XE6EiZXgnRBIE3R5qSjwuemNkXKS1IUK3_xvenqH742IqOQCA3OtNqjECwG5ydWQFEjWbSk6-HRmcPI3JQdmg07ARpfbnmtILhKDzcGAMUBItPifs1z7Gj69OVhPh-NbmkFWrDcpN0TZ4t_ARI-7wcZmGYvpByhuMTCUL-l0y_Bh0xW_uaSPW-EJKYuPW0OtFJCVzNtChmT-aCUQ0Q7D7qNuSWvieCI3buTZHvvwhrD7DD2eH_mcoZncnQd6bR1q_aFnZFH0Lg9SGtRtveSWKGznt1L1tEKvICa4dX5c2_IYHl8cotXBs84op0ksxVbLVjb6XhqW_BcanPpVBEu7vjA8LkkkfguzJusxOR7QYyFbcBvzWrbtn6JUrfW0c" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f78b96a18a.mp4?token=lSEJVdK_yqHY4xRgzHvXT4c3YnusZDgfF5nSMejMdfKJw0aBFM_ZnKavWWZFccOwosTr5H0JqFABjm4dACe6Uch0DF-NVqG4LxE7oEeV-PhQWJQP6lKF0XoE_hAuokVTgQAIJGMuwXAT3WWo5WENMWNYMlmYcrkAAUffhy18OLJhAE1P7zSCXpWQA3-ImRn-sir1fsHHJRaF7NDNnvmvKucMvOWhPOjjGrT3rWCXSKnNHeagS-xxZtbQJV4pX-vaJuq5isgwLVbpPReYLbcZll1LAoiQNDLHU2vjFIpZLJ9tw-XE6EiZXgnRBIE3R5qSjwuemNkXKS1IUK3_xvenqH742IqOQCA3OtNqjECwG5ydWQFEjWbSk6-HRmcPI3JQdmg07ARpfbnmtILhKDzcGAMUBItPifs1z7Gj69OVhPh-NbmkFWrDcpN0TZ4t_ARI-7wcZmGYvpByhuMTCUL-l0y_Bh0xW_uaSPW-EJKYuPW0OtFJCVzNtChmT-aCUQ0Q7D7qNuSWvieCI3buTZHvvwhrD7DD2eH_mcoZncnQd6bR1q_aFnZFH0Lg9SGtRtveSWKGznt1L1tEKvICa4dX5c2_IYHl8cotXBs84op0ksxVbLVjb6XhqW_BcanPpVBEu7vjA8LkkkfguzJusxOR7QYyFbcBvzWrbtn6JUrfW0c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روایت یک پزشک از ماجرای بارداری دختر ۱۳ ساله
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/akhbarefori/691486" target="_blank">📅 17:53 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691485">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
خط لوله ها هم نتوانستند هرمز را دور بزنند
🔹
قرار بود با خط لوله‌ها، هرمز از معادله حذف شود؛ اما اعداد چیز دیگری می‌گویند. مسیرهای جایگزین هنوز فاصله زیادی با ظرفیت هرمز دارند.
🔹
جزئیات را در این ویدئو ببینید
@Tv_Fori</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/akhbarefori/691485" target="_blank">📅 17:48 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691484">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
منابع خبری عربی از شنیده شدن صدای انفجار در اربیل عراق خبر می‌دهند
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/akhbarefori/691484" target="_blank">📅 17:47 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691483">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be98fe0e5a.mp4?token=BjJvEDmNyDk-s2x1OhHXt4PlzYw9QedAWz0MFHt_Kr5ykNfjt1BcpIrIKSwjZ5ED2Of3PkHmwkJIWzFpTpE77smk-7gNgNKVQPsauiMVo668th1DoloMPWMdHB_uDBhzZ7_e4h6wBjE6wJwYELIXtOrIzB9G3s3vSsI0xOV6WZ-i3rT_3s9jqo0WT8LIZtR_MOPDpjayFosRcuAu9CkLF6rZbkVON1rvpaPr7ihkXpqSmuFFZES0PGxOpecO9bWCEYLD_F4CCm6_aqgapuRYhpPykz9oBjD_0Ee-OEaKBWlUnFgDhr8sENMEBaDW-FzCXPFkaxCg5A35XH-dadvlzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be98fe0e5a.mp4?token=BjJvEDmNyDk-s2x1OhHXt4PlzYw9QedAWz0MFHt_Kr5ykNfjt1BcpIrIKSwjZ5ED2Of3PkHmwkJIWzFpTpE77smk-7gNgNKVQPsauiMVo668th1DoloMPWMdHB_uDBhzZ7_e4h6wBjE6wJwYELIXtOrIzB9G3s3vSsI0xOV6WZ-i3rT_3s9jqo0WT8LIZtR_MOPDpjayFosRcuAu9CkLF6rZbkVON1rvpaPr7ihkXpqSmuFFZES0PGxOpecO9bWCEYLD_F4CCm6_aqgapuRYhpPykz9oBjD_0Ee-OEaKBWlUnFgDhr8sENMEBaDW-FzCXPFkaxCg5A35XH-dadvlzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
منابع خبری عربی از شنیده شدن صدای انفجار در اربیل عراق خبر می‌دهند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/akhbarefori/691483" target="_blank">📅 17:41 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691482">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bzg80iKT5hZ_wptmkRpGoJtLVZTuQ3Co1mNs2cmVhpxcXLlDb36DgfEkFqLae_cuPsw1hRDCRtJEDxvILOn8Feh0xClL_9DOjnD-dhZ3ohGqEV6tURUPT9q4oTzzcTj9PfAKN7ytKK8hrx7UxEvflNsK7pfyAivNDpq_02drt8JgH5pogs-ksYhpu11omB1Oc8tSBFiEcbvY2yyWXz7RabyIFaOU9sMiJCV8W-VPqcEpKOYsgAHGa-ypZxVrA7qwxHVOLFbCenFKiizvRfA3hEW9_XE8QeC2OYwPIEPODBoz1y5uo0fwVJTf83xj4rJ_sj6373fBu1UbhKrfv5BA_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بهانه جدید افزایش قیمت خودرو؛ مابه‌التفاوت گواهی اسقاط چیست؟
🔹
قیمت پایه هر گواهی اسقاط خودروهای سواری از ۳۵ به ۶۰ میلیون تومان افزایش یافته و خودروسازان نیز طبق ضوابط جدید باید به‌جای یک گواهی، ۱.۵ تا ۲ گواهی برای هر خودرو تأمین کنند؛ موضوعی که هزینه خودروهای صفر را افزایش داده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/akhbarefori/691482" target="_blank">📅 17:38 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691481">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b6aa19afc6.mp4?token=f59hDdjAOHfFt8oAtPmaChF70UNigFyRrbwqd1HC5Ku603rcVOZDHN1NC3tmfkjn8U-g67B0bLi6npGkhDdWCb3a1a-Oc591NvqdvrxTUYdH3G3szURImi7KYbmAGGBZROD-A9AIUUp8a6KQp0kUrVLv6SNux6HgY9sb90wAFh8WHXL4y0hCC1fxL61f5IfYPkbJOdezkzPTwjrIGftOJfwsi-qFRZoism-xsAQ77iA23qLjESSb_tdpzqqq9vr2Gw0tbMf-5smoLBGj5YIWLGljsaxJPwlbqS6RqI3gOqqE78-MhDJjWoQ45x1M98WPerhamVrf8iTvLutPz-52YRIdwUe8fybkp-AgzWhNiP6DC_lObb8xYi1-fJWfkrfXaAT_FK-kGvYBm6NW6b0ykf9iKlgbgtQEmQuMKGiK-BEQX4Uc3_R7kG_OilzOHVMQGcEyEX4ecCQdDDydIUpYaKq9tmCff9BGCMPouSsfWv8mLrTgPknGRYeedrLHVhROEWOLqrgimNABQRS4-CzkC5OvfqppacgOxF9JK0zgzV3Mqyby0M7KVw0q6d_Zf14YnbCOolnZh4cAydcdDAFvwrfpJPW8fpL3dAG4GDGnS29Vyhn4p5sK5CPZzzmaAlN7JlIZFasN7HGWq4y7oYKLM_cAHlACg7TJO9kMevbUvTI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b6aa19afc6.mp4?token=f59hDdjAOHfFt8oAtPmaChF70UNigFyRrbwqd1HC5Ku603rcVOZDHN1NC3tmfkjn8U-g67B0bLi6npGkhDdWCb3a1a-Oc591NvqdvrxTUYdH3G3szURImi7KYbmAGGBZROD-A9AIUUp8a6KQp0kUrVLv6SNux6HgY9sb90wAFh8WHXL4y0hCC1fxL61f5IfYPkbJOdezkzPTwjrIGftOJfwsi-qFRZoism-xsAQ77iA23qLjESSb_tdpzqqq9vr2Gw0tbMf-5smoLBGj5YIWLGljsaxJPwlbqS6RqI3gOqqE78-MhDJjWoQ45x1M98WPerhamVrf8iTvLutPz-52YRIdwUe8fybkp-AgzWhNiP6DC_lObb8xYi1-fJWfkrfXaAT_FK-kGvYBm6NW6b0ykf9iKlgbgtQEmQuMKGiK-BEQX4Uc3_R7kG_OilzOHVMQGcEyEX4ecCQdDDydIUpYaKq9tmCff9BGCMPouSsfWv8mLrTgPknGRYeedrLHVhROEWOLqrgimNABQRS4-CzkC5OvfqppacgOxF9JK0zgzV3Mqyby0M7KVw0q6d_Zf14YnbCOolnZh4cAydcdDAFvwrfpJPW8fpL3dAG4GDGnS29Vyhn4p5sK5CPZzzmaAlN7JlIZFasN7HGWq4y7oYKLM_cAHlACg7TJO9kMevbUvTI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تراژدی تلخ گردشگری ایران؛ جذابیت در بین برترین‌ها، درآمد تهِ جدول!
محمد درویش، کنشگر محیط‌زیست:
🔹
ایران از نظر جذابیت‌های طبیعی جزو ۵ کشور اول و از نظر جذابیت‌های تاریخی و فرهنگی جزو ۱۰ کشور نخست دنیاست، اما در کسب درآمد از این حوزه‌ها حتی در میان ۱۵۰ کشور اول هم قرار ندارد./ تلویزیون اینترنتی مدار
گفت‌وگوی کامل در یوتیوب
👇
https://youtu.be/uH-2rlDLEnw
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/akhbarefori/691481" target="_blank">📅 17:30 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691480">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5de4dd6b96.mp4?token=kUwMqMH_fNrQAcrJtrA7aaOYtD9deBVzu1_WnXXPZeucTKnACc85AylqFbsmxlWoSHHqLunnRRC07ZnCHsgEUX1ukJ0n57_5an_ofA90XQBwFbvM-zfg82ATbaGmzC5IRBA14Euqc55KwcgaB4zGClG3NgoB2j6F9_NN_UkKrRTx3qZhny-6QP34oMZYVWezCNOnWFjLvDMxmEpeJIbi_mTWEQ9PjzanCS9NqEPsKKIeByTazFha1qKkQIavb57RrWpDr5tpTI5PzIkPXSsh3zDygvBUdqMZwznw5JWTDtfUUW2S9I36WK22ATm7iW3n2NBuOmy9Xnq4FmTY9YrRkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5de4dd6b96.mp4?token=kUwMqMH_fNrQAcrJtrA7aaOYtD9deBVzu1_WnXXPZeucTKnACc85AylqFbsmxlWoSHHqLunnRRC07ZnCHsgEUX1ukJ0n57_5an_ofA90XQBwFbvM-zfg82ATbaGmzC5IRBA14Euqc55KwcgaB4zGClG3NgoB2j6F9_NN_UkKrRTx3qZhny-6QP34oMZYVWezCNOnWFjLvDMxmEpeJIbi_mTWEQ9PjzanCS9NqEPsKKIeByTazFha1qKkQIavb57RrWpDr5tpTI5PzIkPXSsh3zDygvBUdqMZwznw5JWTDtfUUW2S9I36WK22ATm7iW3n2NBuOmy9Xnq4FmTY9YrRkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
زیر گرفته شدن فوتبالیست انگلیسی توسط خودروی چمن در طول مسابقه‌ در تایلند
😳
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/akhbarefori/691480" target="_blank">📅 17:23 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691478">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e978e35310.mp4?token=i3CH_Dti88NoeqvAFMeAue_X9dvYZwFehjifc81FOJZIlMlMUDVHIqft1UD00GStWbgTSoSibJYHhd9OriSbPz3FsE3YUNALeXiqJJ7nGTdO9sCfouu7rauraKBnG2VA9aZf1F2I3nqkqeCgrV_bAOCz4kfaY9hRZSRAqZxAYcrv2YeMj4_BAx4A78fqsIK-TMvItWTAFcKDewYZpAhbYL-fJIb7AmRCe-pBNeIYR2Yh0chL8FA1DeUjlBigF_HR4Ts6oBgWe_UqMQIeumDlrmKGup5bkaEOyxOSsSvqAqRxIAKdYZkXLXbHsu30Stwu_FADhaIRbaPTzRF3ei0Hqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e978e35310.mp4?token=i3CH_Dti88NoeqvAFMeAue_X9dvYZwFehjifc81FOJZIlMlMUDVHIqft1UD00GStWbgTSoSibJYHhd9OriSbPz3FsE3YUNALeXiqJJ7nGTdO9sCfouu7rauraKBnG2VA9aZf1F2I3nqkqeCgrV_bAOCz4kfaY9hRZSRAqZxAYcrv2YeMj4_BAx4A78fqsIK-TMvItWTAFcKDewYZpAhbYL-fJIb7AmRCe-pBNeIYR2Yh0chL8FA1DeUjlBigF_HR4Ts6oBgWe_UqMQIeumDlrmKGup5bkaEOyxOSsSvqAqRxIAKdYZkXLXbHsu30Stwu_FADhaIRbaPTzRF3ei0Hqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گزافه‌گویی ترامپ قمارباز: گزینه‌های روی میز فعلی، محو ایران، فروپاشی اقتصادی آن یا دستیابی به توافق است
🔹
سوال من این است که چه زمانی و آیا کل ایران را منفجر خواهم کرد یا خیر، و بهتر است خودشان درست رفتار کنند. #Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/akhbarefori/691478" target="_blank">📅 17:20 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691477">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromتامین مالی جمعی رضوی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HLP5X1TPHzql_1GWfb4VIsz-QkFpwVl2DxSr0xEJOdro4fde54PJ_ZIRrlc2pC7S9zQVrum_qz_JBYkWRfyARV92AiJyDs7PzCWvC0gPcO-p_3zrMbGcEogZ0uCjLl4WTBmWC6kPwcnAwZr0mCUBqnL8e9LVBAmWRrD3tzcHtPeeVAf0pnkItwpq8fTYn1zYVopzY9HNSFu5WKMA8OGujrEqvUQr0BCpfsFEjMmuT0QTB1dPildfqc4EI_fQxObw8LzbpP25YlQZCvdSk8gzne1NrT8YYs2gEXSCKrMFS7eEY_ZZ994E6aAwcvDaT4d9dn2IUI-MP_SBYTuR0FoSnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏳
همراهان عزیز سکوی رضوی،
فرصت سرمایه‌گذاری در طرح ارائه خدمات آموزشی تخصصی زبان های خارجه آغاز شد!
✅
سودپیش‌بینی شده:
۴۶ درصد یکساله
(پرداخت ۳ ماهه)
✅
دارای
ضمانت تعهد پرداخت
بانک ایران زمین
✅
شرکت تعاونی راشد جوان مبتکر
🌟
سودمندانه اعتماد کنید…
کسب اطلاعات بیشتر و سرمایه‌گذاری:
تلفن تماس:
05191008000
سکوی تامین مالی جمعی رضوی
cfrazavi.ir
آدرس ما در فضای مجازی:
تلگرام
بله</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/akhbarefori/691477" target="_blank">📅 17:20 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691476">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">برنامه‌های «شفرونی» و «روشن» با دستور قضایی رفع توقیف شدند
🔹️
پس از اعلام جرم ساترا علیه برنامه «شفرونی۲ » در ۲۱ شهریور ماه و دستور دادستانی مبنی بر توقف پخش، امروز حکم رفع توقیف این برنامه صادر و «شفرونی» می‌تواند از همین هفته پخش خود را از سر بگیرد.
🔹
ساترا در شکایت خود به دادسرای فرهنگ و رسانه، انتشار بدون مجوز و محتوای غیراخلاقی و خلاف عفت عمومی را عامل درخواست توقیف برنامه عنوان کرده بود که با حضور تهیه‌کننده برنامه در دادسرا و ارائه توضیحات و مستندات و انجام برخی مراحل قانونی، دستور رفع توقیف «شفرونی» صادر و به پلتفرم پخش‌کننده و ساترا ابلاغ شد.
🔹️
همچنین برنامه «روشن» نیز با استناد به قانون مطبوعات و آیین‌نامه‌های اجرایی آن مشمول موارد ادعایی در شکایت ساترا نشد و دستور تداوم پخش آن نیز صادر شد.
Asriran.com
@MyAsriran</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/akhbarefori/691476" target="_blank">📅 17:20 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691475">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">♦️
ادعای ترامپ: احتمالاً آماده دیدار با مسعود پزشکیان، رئیس‌جمهور ایران، در حاشیه مجمع عمومی سازمان ملل موافق خواهم بود #Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/691475" target="_blank">📅 17:18 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691474">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c1e18660f7.mp4?token=g-xBROToyQTZMq4E-CldrkKzagPl8doHc_DMSKnQrVuPNNu8yAOdCck-DLF_oxw1Zf_o6cPiSQ8UpC6TAuXyLC5-542kiwxoFQcuf2cck_hE7aBEmtsX8F7vx65iV1Cz1GgN0s7v20t23rdqvhBr28lOfUnAB5C1nGFfGMkxk7jNNiQedjGUdtsXD9V5R5C6OvYIVzw1zIr_cz81kskLlce4RvPsnQ9U_e7RjawP49AqHp2oP78A23cQrHN-yKOCuQ7azHTENRkjH-P4SR82BSv8q8Jp9FQQm_Io62U5YEcEnZsyZDzE4ZRHlK2DO7C1xKkaX3JftUB31LYib9zg4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c1e18660f7.mp4?token=g-xBROToyQTZMq4E-CldrkKzagPl8doHc_DMSKnQrVuPNNu8yAOdCck-DLF_oxw1Zf_o6cPiSQ8UpC6TAuXyLC5-542kiwxoFQcuf2cck_hE7aBEmtsX8F7vx65iV1Cz1GgN0s7v20t23rdqvhBr28lOfUnAB5C1nGFfGMkxk7jNNiQedjGUdtsXD9V5R5C6OvYIVzw1zIr_cz81kskLlce4RvPsnQ9U_e7RjawP49AqHp2oP78A23cQrHN-yKOCuQ7azHTENRkjH-P4SR82BSv8q8Jp9FQQm_Io62U5YEcEnZsyZDzE4ZRHlK2DO7C1xKkaX3JftUB31LYib9zg4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای ترامپ: ممکن است به زودی اتفاق  بزرگی در مورد ایران اتفاق بیافتد #Devil
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/akhbarefori/691474" target="_blank">📅 17:17 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691473">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">♦️
ادعای ترامپ: ممکن است به زودی اتفاق  بزرگی در مورد ایران اتفاق بیافتد
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/691473" target="_blank">📅 17:08 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691472">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65d8a658f3.mp4?token=ZhsLP5_dF3bWS02JSppbLT3nKiHlQ8Ynm7SE8zlYCglOQh6zyEH8TBks-ri3GFG-bH0MnYe0gbatXoPpZD1eVdczS6bhVHq_2AiMv-lg5YMg4aeBYVcij5n0DdDWPRe7Y7qdF53ZYGTGd27Z0KCV0oF75m1u8HRwPhCVnzkyJDUt9F0bjragaJYnoe8JyqQ3St0GypbdsT2toX3bPimy-iQZ-83hYf3rMR0aySBRSDOQ6_7PNO2FgTcR5qrvG7k2okmmg59bI3G3TfABXmc7wo8Ef4-LqZSEIwZ5PtU-WzUyn1Bm0PIv1oacQJhcsltxNDmkP2guBkIFPCSDOs0fwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65d8a658f3.mp4?token=ZhsLP5_dF3bWS02JSppbLT3nKiHlQ8Ynm7SE8zlYCglOQh6zyEH8TBks-ri3GFG-bH0MnYe0gbatXoPpZD1eVdczS6bhVHq_2AiMv-lg5YMg4aeBYVcij5n0DdDWPRe7Y7qdF53ZYGTGd27Z0KCV0oF75m1u8HRwPhCVnzkyJDUt9F0bjragaJYnoe8JyqQ3St0GypbdsT2toX3bPimy-iQZ-83hYf3rMR0aySBRSDOQ6_7PNO2FgTcR5qrvG7k2okmmg59bI3G3TfABXmc7wo8Ef4-LqZSEIwZ5PtU-WzUyn1Bm0PIv1oacQJhcsltxNDmkP2guBkIFPCSDOs0fwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نویسندۀ آمریکایی: ما از منطقۀ غرب آسیا بیرون رانده شده‌ایم؛ به این معنا که پایگاه‌های ما دیگر کارایی ندارند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/akhbarefori/691472" target="_blank">📅 17:08 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691471">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80061ce38a.mp4?token=TqaR2EADI0qW1KLgdAFvQT81OAjy4QgjVnHQ47Ay0Ck8tRnbdEp_iFYFgZ85sqmhItKRnqADToGW9Fs8rs3U4GKutWoiFcWF7DJUuIVvLrhN0_ohiSaqfbbVpnpnSBtY7RxuOZusRgLKExIEkG2gXkE-vT_gjrBOKfmdXwtg_aJ7AJYAaC-vv7-biPV9Q-hbg-isV_uMMbFFUEdtClRJ4aO49jm5hH-0vwUQN_5SbDcTNJVWl0nmxncs8-iw3qx_BhIR-51asUgSjm98ZVpyYxSEQv0LFlgC0AyXDd11EcLHbcxuhhN-eqmP6KUQ8x_2OeaEvCm8XtZtfFGt-M8PUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80061ce38a.mp4?token=TqaR2EADI0qW1KLgdAFvQT81OAjy4QgjVnHQ47Ay0Ck8tRnbdEp_iFYFgZ85sqmhItKRnqADToGW9Fs8rs3U4GKutWoiFcWF7DJUuIVvLrhN0_ohiSaqfbbVpnpnSBtY7RxuOZusRgLKExIEkG2gXkE-vT_gjrBOKfmdXwtg_aJ7AJYAaC-vv7-biPV9Q-hbg-isV_uMMbFFUEdtClRJ4aO49jm5hH-0vwUQN_5SbDcTNJVWl0nmxncs8-iw3qx_BhIR-51asUgSjm98ZVpyYxSEQv0LFlgC0AyXDd11EcLHbcxuhhN-eqmP6KUQ8x_2OeaEvCm8XtZtfFGt-M8PUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حسن روزی‌طلب، معاون سابق صداوسیما: ادعا شد در حوادث ۱۸ دی صداوسیمای شهر کیش سقوط کرد و تسخیر شد/ جماران
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/akhbarefori/691471" target="_blank">📅 17:01 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691470">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">♦️
صحبت‌های تلخ محمود بصیری پس از مدت‌ها؛ تلویزیون بیننده ندارد، من برای کی بازی کنم
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/akhbarefori/691470" target="_blank">📅 16:59 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691468">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d52c097554.mp4?token=lAHh4ZsVK4AgSZpZw-Ef2p4muBr6nsmhuTFlIdfT8ClmTLIU6lCmDXP7GxzisgE1CZ0NAe7aNNbMWk5ebgWZKV3dEu3Q38hnfxozgBGkZWR1_IJrizS8fR9_qSjymL_mov8gzLzLHZfkdNGc_nE_IQ_BxxePGlLDFsFOR5EI4RooUf9BIwcrHnVw7zLvnSrPArRGz-puu6AJLDUIC3l9w_77ZSIK4_j-xOwlU6GIr3cwl1TF-V0vJ2jF2ap4tmWvOCOMc1YoIQ7zypEZIbTUBNNExfwp8ncQAehi622nQG4KbSCZNMTYOAtljMqjgyVHrE_e4dUmCxrcU56Dx9N3cQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d52c097554.mp4?token=lAHh4ZsVK4AgSZpZw-Ef2p4muBr6nsmhuTFlIdfT8ClmTLIU6lCmDXP7GxzisgE1CZ0NAe7aNNbMWk5ebgWZKV3dEu3Q38hnfxozgBGkZWR1_IJrizS8fR9_qSjymL_mov8gzLzLHZfkdNGc_nE_IQ_BxxePGlLDFsFOR5EI4RooUf9BIwcrHnVw7zLvnSrPArRGz-puu6AJLDUIC3l9w_77ZSIK4_j-xOwlU6GIr3cwl1TF-V0vJ2jF2ap4tmWvOCOMc1YoIQ7zypEZIbTUBNNExfwp8ncQAehi622nQG4KbSCZNMTYOAtljMqjgyVHrE_e4dUmCxrcU56Dx9N3cQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
منوی سه‌بعدی؛ ایده‌ای متفاوت برای سایت رستوران
🍔
🔹
می‌توان به‌جای منوی معمولی، هر آیتم غذایی را به یک صحنه سه‌بعدی و تعاملی تبدیل کرد؛ ایده‌ای جذاب برای منوی رستوران، معرفی محصول و کمپین‌های برند.
🔹
این مدل اجرا برای Restaurant Menu / Product Showcase / Brand Campaign واقعاً جذابه چون خود طراحی چاپی رو تبدیل می‌کنه به بخشی از تجربه کاربری .
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/akhbarefori/691468" target="_blank">📅 16:41 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691467">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xt9KQpMX7NL6Xdyx3RzM379RbhFta4HodB_D0cSDq9023AZ1wEVvMs6wuPuWmzXkgTNhN7seljxEwTdyDgwhjyhbQJ_llLb-pH1uHBrL5hjnE2BC8Q0Vi2hdIG8KUzZAThMFD-1cxkylDJT-U7SYinJbnZ24EMHMA6aUwWz5JsTXBCPnBP8tatgUiNNipSTlbog3bp4rzIOmg2c2y4kQqCmDz72qhASRQGuVE241xThK7tyE_NDfLaNZh2XyAid5BG0PiJxob58BxUB1lUPPPfEvlyZ6c_sy3-cYHgCB9JqFFKl0t6db0NAgvLdIyhQlnFoUb13coaEuEQORcFHudg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کارخانه‌ها روشن، بازار خاموش | لوازم خانگی؛ صنعتی که نباید قربانی واردات شود
🔹
صنعت لوازم خانگی ایران در سال‌های اخیر یکی از معدود بخش‌هایی بوده که توانسته از دل محدودیت‌های اقتصادی و تحریم، مسیر تازه‌ای برای توسعه پیدا کند.
گزارش خبرفوری را اینجا بخوانید
👇
khabarfoori.com/fa/tiny/news-3246628</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/akhbarefori/691467" target="_blank">📅 16:32 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691465">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e6167b311.mp4?token=J6Qv6hGv3fR9GBeINpkby0p2vgCwbxiyJS1qEJubC_T2n9fYqFkQjai6fQ7U2Gqjw_xOYRKVstkLas5-cYpmmYSQVpQMGufF8UPzh6AbnDotN0x2keEydhb3Ja1azvRKKu90UlBCqyIzWAwpDsvufEwqG3h9iXU18A9Cvl5jB5lybXV7snL3APxTVSCXayjotfIEFeeBHYPqreypuJH6Pc3kgXGsLVyGzRT7H91FCN_9XxF4To74zTaHS0jq59mcdycgoCRB6tLXp_FJqPfpu5lEvEmOlUfTM5-MvHc4ZSrUy38g0Jd6UNPMhDk2EYFpOV3eA47ZetKxc-CxZeXylQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e6167b311.mp4?token=J6Qv6hGv3fR9GBeINpkby0p2vgCwbxiyJS1qEJubC_T2n9fYqFkQjai6fQ7U2Gqjw_xOYRKVstkLas5-cYpmmYSQVpQMGufF8UPzh6AbnDotN0x2keEydhb3Ja1azvRKKu90UlBCqyIzWAwpDsvufEwqG3h9iXU18A9Cvl5jB5lybXV7snL3APxTVSCXayjotfIEFeeBHYPqreypuJH6Pc3kgXGsLVyGzRT7H91FCN_9XxF4To74zTaHS0jq59mcdycgoCRB6tLXp_FJqPfpu5lEvEmOlUfTM5-MvHc4ZSrUy38g0Jd6UNPMhDk2EYFpOV3eA47ZetKxc-CxZeXylQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدئویی عجیب از آواز خواندن آقای دکتر در اتاق عمل!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/akhbarefori/691465" target="_blank">📅 16:30 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691464">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f97800973.mp4?token=Sb4wOCdyPUgMNinQTuaCc295j4SkB1M1TqA1G0jDOVlsd85B_YpW-Yub6WZEbQx_NBA798cX1KnjTWZWOr-reg6x6SqrRTZLL5vrDBd2uMUz2pJpRotHHMW7xbE8AVoRgnUDnFP_TrQHu6zPix1kY34h_yK9575bD2TkHqr2d3Q5aNwWcVGdwesOjVCBnoQfCALn6A5n8MhPlhL6Qannx3WhPglAqIFwj4PszbtsTqI-9zx-4YmdYfZbeD5aLCDLR8d9Vh4YyPzX6QdGTOwFwjiAomz75MaqBytbWr_4O6KfuENIorFbSAiOHMp6pJMSwOhRsHSky0lgTINjnBHqQidtDkmCNIJz9w3lnFmdff8R_1vOGsY3d3KcflzcRCk4CKpzixUF4YEVkb2IUVVM5uGIM8ayQ-qIpaHHVqO9MgR9OIOXvavnsUVClVDeWxkyLR6V8Jc2ep0F7xRRH4PTdyekXQ4yGrfDn0qm-VoywkbfCM9XawPt6TLJ-0IUcBY7dUYRSiCGdvo9gMxKFpUOgIG2rH0XQqPiljev9IKyp_tograe9lqU0dX3ID6gr7Qczb-6uUErh0LTFP6jThUcWtBCWgFSyYMNEUykVrBIH-19veMsBqkhwGYdvmdLwwUZyTX_8oRaoCQKxF3EGo8Q2geFzAqoxpNwZPB82BF_SJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f97800973.mp4?token=Sb4wOCdyPUgMNinQTuaCc295j4SkB1M1TqA1G0jDOVlsd85B_YpW-Yub6WZEbQx_NBA798cX1KnjTWZWOr-reg6x6SqrRTZLL5vrDBd2uMUz2pJpRotHHMW7xbE8AVoRgnUDnFP_TrQHu6zPix1kY34h_yK9575bD2TkHqr2d3Q5aNwWcVGdwesOjVCBnoQfCALn6A5n8MhPlhL6Qannx3WhPglAqIFwj4PszbtsTqI-9zx-4YmdYfZbeD5aLCDLR8d9Vh4YyPzX6QdGTOwFwjiAomz75MaqBytbWr_4O6KfuENIorFbSAiOHMp6pJMSwOhRsHSky0lgTINjnBHqQidtDkmCNIJz9w3lnFmdff8R_1vOGsY3d3KcflzcRCk4CKpzixUF4YEVkb2IUVVM5uGIM8ayQ-qIpaHHVqO9MgR9OIOXvavnsUVClVDeWxkyLR6V8Jc2ep0F7xRRH4PTdyekXQ4yGrfDn0qm-VoywkbfCM9XawPt6TLJ-0IUcBY7dUYRSiCGdvo9gMxKFpUOgIG2rH0XQqPiljev9IKyp_tograe9lqU0dX3ID6gr7Qczb-6uUErh0LTFP6jThUcWtBCWgFSyYMNEUykVrBIH-19veMsBqkhwGYdvmdLwwUZyTX_8oRaoCQKxF3EGo8Q2geFzAqoxpNwZPB82BF_SJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پرتاب کفش به تصاویر ترامپ و نتانیاهو در کره جنوبی
🔹
حامیان فلسطین در سئول در اقدامی نمادین، کفش‌هایی را به سوی تصاویر ترامپ و نتانیاهو پرتاب کردند و اعتراض خود را به جنایات این دو نشان دادند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/akhbarefori/691464" target="_blank">📅 16:30 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691463">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">♦️
پنجشنبه‌ها در استان قم تعطیل نیست
معاون توسعه مدیریت و منابع استانداری قم:
🔹
خبر منتشرشده درباره تعطیلی پنجشنبه‌های دستگاه‌های اجرایی استان تا پایان سال صحت ندارد.
#اخبار_قم
در فضای مجازی
👇
@akhbareghom</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/akhbarefori/691463" target="_blank">📅 16:21 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691462">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f20de068bb.mp4?token=d1JX22ZM0bO7adilZhZQilYMS_Y5usmTl8y6tEiR55l04FPCt2b4Lvj7yuE3-NWVutEJJNAzXdnsOnYExGE9hgU8Ewz2qBKYaZ70xCauJ2lvaqkaetyTtG92COvR4Vkmdo7KQCP2lA0Mnw3WS7JD_6J0tj89zNAJgXPLfDXzaCdPB4ou4iu9ZC0rF3LEocxKvaW7q0I8XNTBC_WEidouwky-Hfxz3uQ9lOk1DPh9PU_df3G_925w35dpq6I1N81t2zjCVy5JgSNy8Se7b4wAs6f6vlhzdx1XYWKZYEe48p85k-S1M41Tmwh1NRd4jfkR8-QXZiu1hVZUbx1CJc7gHjfT0SevryPmMUwNPNzdxNUI0lFxP-pr7W7J6qvFKviCfb9AOVikC_8EF8DLs4Lj4mdacMcWQV5cZvboGE2nj8gkAxuBtUdh_U9O2YEF_gWJ1m9HwsI4gOpaLB1U5dHbg4wk64I8k6FYXtlYj_THtSVDxJ-zHTotOnL_0Udk2rEfaRci-gdSDKMpDIWCF8QaT7CGhkvetvzcb_NyHRg1BNv6F31tWp6e-lKxW-krjIMytAwauQMKCzZeGYWPbKTbdLIr7Hx5tQrk8krP7ozZnj7GrAp_STmW4wjgG62vbCCary4jVYD67-rxGiv8sTH8VK-PL8-jHCXNXtfe0Z6gqcs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f20de068bb.mp4?token=d1JX22ZM0bO7adilZhZQilYMS_Y5usmTl8y6tEiR55l04FPCt2b4Lvj7yuE3-NWVutEJJNAzXdnsOnYExGE9hgU8Ewz2qBKYaZ70xCauJ2lvaqkaetyTtG92COvR4Vkmdo7KQCP2lA0Mnw3WS7JD_6J0tj89zNAJgXPLfDXzaCdPB4ou4iu9ZC0rF3LEocxKvaW7q0I8XNTBC_WEidouwky-Hfxz3uQ9lOk1DPh9PU_df3G_925w35dpq6I1N81t2zjCVy5JgSNy8Se7b4wAs6f6vlhzdx1XYWKZYEe48p85k-S1M41Tmwh1NRd4jfkR8-QXZiu1hVZUbx1CJc7gHjfT0SevryPmMUwNPNzdxNUI0lFxP-pr7W7J6qvFKviCfb9AOVikC_8EF8DLs4Lj4mdacMcWQV5cZvboGE2nj8gkAxuBtUdh_U9O2YEF_gWJ1m9HwsI4gOpaLB1U5dHbg4wk64I8k6FYXtlYj_THtSVDxJ-zHTotOnL_0Udk2rEfaRci-gdSDKMpDIWCF8QaT7CGhkvetvzcb_NyHRg1BNv6F31tWp6e-lKxW-krjIMytAwauQMKCzZeGYWPbKTbdLIr7Hx5tQrk8krP7ozZnj7GrAp_STmW4wjgG62vbCCary4jVYD67-rxGiv8sTH8VK-PL8-jHCXNXtfe0Z6gqcs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گلایه شهروندان نطنزی از تأخیر در رسیدن آمبولانس/پاسخ بحث‌برانگیز اپراتور ۱۱۵/تأسیسات هسته‌ای نطنز در نزدیکی این شهر قرار دارد!
🔹
تأخیر بیش از ۳۰ دقیقه‌ای در رسیدن آمبولانس به محل یک حادثه در شهرستان نطنز، موجب نگرانی و اعتراض مردم شده است.
🔹
بر اساس ویدیوی منتشرشده از سوی یکی از شهروندان در تماس با سامانه ۱۱۵، پاسخگو اعلام کرده که آمبولانس در مأموریتی در سرآسیاب است. شهروند معترض نیز نسبت به وضعیت امدادرسانی و تأخیر پیش‌آمده اعتراض کرده که بنا بر این روایت، اپراتور در پاسخ گفته است:
«بدبخت اورژانس! اشتباه می‌کنند خدمات رایگان به مردم می‌دهند»
و سپس تماس قطع شده است.
🔹
در ادامه این روایت آمده است که با ۱۱۲ هلال‌احمر نیز تماس گرفته شده، اما اعلام شده امکان اعزام نیرو وجود ندارد.
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/akhbarefori/691462" target="_blank">📅 16:18 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691461">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromتیتر تجارت</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb09df83f7.mp4?token=tvi9CQZhSfbVzBINlHDnyJUF4H5d6mWRI2pxZwsKuXA4wEjkIcA6Mtk-SkuGeX3FrDfqgdat5HdFRaezwp4vXf8T8HnjRj-cvgblS-HR2D35ydZ5L-1P4HogaVECBB0KIgS5lv4v-VngY7kO3krGbefQhq3dpYpmOWDAtB8L_hMAN8_aNPXDQs2qFv6LNYCx2TBYFr4-rnt1IIDFVQrz7HFQn-sjnrSu97TG1zl0EYTlc7oP1-L5NIxrrflLjZ1XEdmbuH0HxfJSLpB2d-qYtZCmOxBNEIZrDj7WIQvnYmMnIznIvoavnSZtANFK12U8IHrkLQVKFP5SPtVK8NTtgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb09df83f7.mp4?token=tvi9CQZhSfbVzBINlHDnyJUF4H5d6mWRI2pxZwsKuXA4wEjkIcA6Mtk-SkuGeX3FrDfqgdat5HdFRaezwp4vXf8T8HnjRj-cvgblS-HR2D35ydZ5L-1P4HogaVECBB0KIgS5lv4v-VngY7kO3krGbefQhq3dpYpmOWDAtB8L_hMAN8_aNPXDQs2qFv6LNYCx2TBYFr4-rnt1IIDFVQrz7HFQn-sjnrSu97TG1zl0EYTlc7oP1-L5NIxrrflLjZ1XEdmbuH0HxfJSLpB2d-qYtZCmOxBNEIZrDj7WIQvnYmMnIznIvoavnSZtANFK12U8IHrkLQVKFP5SPtVK8NTtgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چرا حباب صندوق های اهرمی در بورس منفی است؟
@Titretejarat</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/akhbarefori/691461" target="_blank">📅 16:17 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691459">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">♦️
انتقال جنسی، شایع‌ترین راه انتقال HIV در سال‌های اخیر
رئیس مرکز مدیریت بیماری‌های واگیر وزارت بهداشت در
#گفتگو
با خبرفوری:
🔹
انتقال جنسی در سال‌های اخیر به شایع‌ترین راه انتقال HIV تبدیل شده است. او همچنین اعلام کرد وزارت بهداشت آمار بیماری‌های مقاربتی در میان دانش‌آموزان را در اختیار ندارد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/akhbarefori/691459" target="_blank">📅 16:01 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691458">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">♦️
فرانسه: دو دیپلمات ایران طی روزهای آینده اخراج می‌شوند
🔹
وزیر امور خارجه فرانسه در پیامی در شبکه ایکس ضمن حمایت از اغتشاشات دی‌ماه نوشت که قصد اخراج دو دیپلمات ایرانی را دارد.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/akhbarefori/691458" target="_blank">📅 15:59 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691457">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">♦️
شمارش معکوس تا انتخابات آمریکا و اسرائیل
🔹
انتخابات میان‌دوره‌ای آمریکا ۳ نوامبر ۲۰۲۶ برگزار می‌شود؛ از امروز ۴۴ روز باقی مانده است.
🔹
انتخابات رژیم صهیونسیتی نیز برای ۲۷ اکتبر ۲۰۲۶ تعیین شده و ۳۷ روز تا برگزاری آن باقی مانده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/akhbarefori/691457" target="_blank">📅 15:55 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691456">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AoKEd3EGTfK-K473_kUlOWXGopv6jQ_UugC_7qgZ4Z8IJyzR17aro7BuZ6p0PpRiKveIQWyfxvAf8eUNMmBmkwxUcUKP6tXbMVk8tCA94NZ9XKY4pFVb10E_u4U_JuPO8nMzHV-JHDJCsRJLHk_Tc7GlmDAg3IECCA1cJJIKp6H8u61s3SkkeOzofqHbLESIf67ycqWzzgyrO3dxB5mzGE01GKVJ2FQL0vm9VKRLr9WbOJeMpA-E6MysUVemPH1c6U1d9QxiOnmRIkY6DQljmIAZIK_A7mBs_sQKtPwnkD0Rc6IltvyllnVApkVwJD__6ReCv8U7mQwt0YFvgcNhoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
گزارش سی‌بی‌اس امریکا در مورد پویش جانفدا: تجمع گسترده ایرانیان در نمایش وحدت و مقاومت
🔹
به گزارش
CBS News
، صدها هزار ایرانی روز جمعه در تجمعی سازمان‌دهی‌ شده شرکت کردند و آمادگی خود را برای دفاع از کشور و دریافت آموزش‌های نظامی اعلام کردند.
🔹
بر اساس گزارش‌های رسمی ایران، بیش از
۳۰۰ هزار نفر
در این تجمع حضور داشتند برخی از شرکت‌کنندگان پرچم‌های آمریکا و اسرائیل را زیر پا گذاشتند و برخی دیگر شعارهای
«مرگ بر آمریکا»
و
«مرگ بر اسرائیل»
سر دادند.
🔹
رسانه‌های دولتی نیز طی هفته‌های گذشته مردم را به پیوستن به این کارزار تشویق کرده‌اند و گفته‌اند آموزش استفاده از
سلاح‌های تهاجمی
به‌زودی آغاز خواهد شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/akhbarefori/691456" target="_blank">📅 15:51 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691455">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">♦️
هشدار قرارگاه مرکزی حضرت خاتم‌الانبیا (ص) به آمریکا و کشورهای منطقه: خطا کنید هدف حملات دردناک قرار خواهید گرفت
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/akhbarefori/691455" target="_blank">📅 15:44 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691449">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F52kI26KbtNCqvPpSSY_08jMZU_9nKB9RjxDTyjuEiWbIHzHKZi53_wVgE6l7QdRRPe6H9OpGjRGW6jLPcibWQPuHZeWKRIW6oJRy1CV1QoWZOPEaU4sQWspbBxWRKHObRpxEneGhazvgszKUbc_DagR-hqyqOAa7dtVZZsXMUWbT6w4ns9bF8RuEm4c3ygdNwn6paM8yuzJbwL6EUZxOtPYFKUp_XijaAAWsLG23uCIh7y1RD63kMpTB7cJFtcxQGsd6E16KzEme5Sn8HjOx8xPXtDysAOZIxnEwwjJYUDhsYaBiKPEfxotIn653tx3QKUEEew5Spl5eYmKzPCY0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B2NA8iWTWo4uWp3pwLshnpElfOUwuO6wSV3O9cFw7-T6-FFi5ATOdXwJA3Mn9aGnjpT5NN_5WN4CfLjQpi3lAXiTu2PSCkhbkTowt4ZN476DLZBvCGP6SgDcYxhLYAEkkAiWWvPZ4E0AtvbtrjbszUAdiDQYIlu15Y6BmdybKGDu-_2YKIqST00_UretVKmfa4oPhbxVbLTdxw1qXTQWvRZdHWWWh_JLDHZz2CtYAmEVaolI1VcCYGVgOhYr-66r1OWrHyVRbHblL0w-lKOBBMf4KCqk_8s9UrDsNIxGhYPN9WEjXVNIUnY_EhubxySNKX9WLq0cllFeDu3Qyy6XgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nKXfiH5bMNL8eTiVCwJbkwpeujcACuQx09uy4pTP0NEaeIjtGuf1_dPORF-NEUw8iM6i3SjPbDmUhV3req8XNEeA1nwJSE67HeeWKbzA6VV1ot8SstCG2YJ_7pryugdWyCJKw8Nkb_qUZeGowiF8QWZj_h6d0k47BSX5foBhVSxJdUYYnaUYXrjuui66xpHtuLvCZGB2B3SDG9uLaKb7Hyd3BtRSGUnaTPL41gIBAn2amFsaOzj0JNLK4PesUg0ot2biK4ZG_rVXNiGfJ6zf5H7J2HV6VlKk4tm5hHPtr41zpzYeSZHpKk0LSJhtQJ5MjkO8dO7z4RRI2yZsA4qWsw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/008e331b03.mp4?token=qNuVIu_ca_wn85AuUv5TI5Dk7haTwem-vc6cbQGRdxrQ6byK5h0iDPAeEZihoDx7X43TeIQ_UBUi3vLrXeiRjjahmjy6IIPlJjZgNFzdCW7VFj1I2fD9nbo-h1BaYZqJGBrhK0qL0FDGFUerlBSw0Why-hiIVpPu_YU7iH62sfV6x_pOcM6rTAp4qcgMtrFev8xuvxULsHnm-fG6FBqzmWE-IEeVhs-LwlvrbAigeEHmNjHIfXRge3NJgnZvKYRZtUVHmije0I-CZfwwYn3jN3xGeueTvm3JkzEoTb_W6X6oPdkwYlYgkuU6dggmh0IGBKRyzpemV4P_5nJ_MWdOEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/008e331b03.mp4?token=qNuVIu_ca_wn85AuUv5TI5Dk7haTwem-vc6cbQGRdxrQ6byK5h0iDPAeEZihoDx7X43TeIQ_UBUi3vLrXeiRjjahmjy6IIPlJjZgNFzdCW7VFj1I2fD9nbo-h1BaYZqJGBrhK0qL0FDGFUerlBSw0Why-hiIVpPu_YU7iH62sfV6x_pOcM6rTAp4qcgMtrFev8xuvxULsHnm-fG6FBqzmWE-IEeVhs-LwlvrbAigeEHmNjHIfXRge3NJgnZvKYRZtUVHmije0I-CZfwwYn3jN3xGeueTvm3JkzEoTb_W6X6oPdkwYlYgkuU6dggmh0IGBKRyzpemV4P_5nJ_MWdOEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
صدای اعتراض به جنگ تحمیلی ایران در سن‌خوزه کالیفرنیا طنین‌انداز شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/akhbarefori/691449" target="_blank">📅 15:30 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691448">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">♦️
فایننشال تایمز: سقوط ۹۴ درصدی تردد کشتی‌های کانتینری در تنگه هرمز؛ در برخی کشورها حتی کلاه ایمنی دوچرخه برای کودکان تمام شده
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/akhbarefori/691448" target="_blank">📅 15:28 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691447">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">♦️
سرلشکر محسن رضایی: به همه کشورهای عربی و همه کشورهای همسایه می‌گویم اگر آمریکایی‌ها سعی کنند روابط تجاری و مالی ما را مختل کنند، ما دو کار انجام خواهیم داد
🔹
اول، ما قطعاً به شرکت‌های آمریکایی حمله خواهیم کرد - مانند شرکت‌های حفاری آمریکایی که به طور گسترده…</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/akhbarefori/691447" target="_blank">📅 15:27 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691446">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75fec65264.mp4?token=c549p-b9g7ZtXYVI0NJwvpbqGBz0SzmKtUnZ1l7hH-loRc-rgY3_sZnt6l2Gt-uusH1ocQBj6orTN60A4A3ZvSbk07gdcZpHSDedbK53hkxokmGumfg1L0nGOPbz6sp7lewM6QUQKZSqiDxOhSFiQPN5_LZ8Bt0rkIMG5sGifhllFHb3vdGb9yhVpJBM9YJoydDwcNIdgGC2o2pIEzhfJa00y9ErGfwvjZ7jeQ70_LsClyDy-GmmviB7cZ8fvcJuVku1DQfv6G67JicWq6tSiH7QXa5vtGHGfiYiUirmsaJeWueBpd5AMXAKCFHldXU_Jrseb3nd-rMBOiGREq74fA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75fec65264.mp4?token=c549p-b9g7ZtXYVI0NJwvpbqGBz0SzmKtUnZ1l7hH-loRc-rgY3_sZnt6l2Gt-uusH1ocQBj6orTN60A4A3ZvSbk07gdcZpHSDedbK53hkxokmGumfg1L0nGOPbz6sp7lewM6QUQKZSqiDxOhSFiQPN5_LZ8Bt0rkIMG5sGifhllFHb3vdGb9yhVpJBM9YJoydDwcNIdgGC2o2pIEzhfJa00y9ErGfwvjZ7jeQ70_LsClyDy-GmmviB7cZ8fvcJuVku1DQfv6G67JicWq6tSiH7QXa5vtGHGfiYiUirmsaJeWueBpd5AMXAKCFHldXU_Jrseb3nd-rMBOiGREq74fA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وزیر امور خارجه ترکیه: ما قبول نمی‌کنیم که عربستان سعودی به عنوان بخشی از درگیری جاری بین ایران و آمریکا در نظر گرفته شود
🔹
عربستان سعودی باید از این معادله جدا نگه داشته شود، زیرا خودشان تمایلی به دخالت در آن ندارند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/akhbarefori/691446" target="_blank">📅 15:15 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691445">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89dd2a1fad.mp4?token=jyz3QMzhm_1Dee6UWcI7-SkA7kJeyjgYi3EZR3JqOe3xYd8qUxyV3ll_G5WPpsfqgZs17Suy-j00q12CwiLmFIahLmY0LkYhn4s2snCe7sWlywCeICL7HR9bxavV4i1V8h5y3o9v-rXsJ9xNwMJYzk6l4kKMv4L4Bucpf8i-aRu4DE9mlD2MSynlt1Vw_Z-Xx4vQpCl7EQm-lOdueV9cNeNVg9-FQaHYbGkezfMLNuM-CSOHflQevhETHC9XrH2Odv3rPtVNRJZMN_suwEvj31muWz3eUOdMzUES33FAlEzZZfpETB0sf85srGXi2E8yRgh1tCPAjUZnpNW49qZIeCv8Rtzj2mqxB5SdKSRgBfPUo_EN8-mZ-7ZdR1ZVwLHVi4tg2mOC4RLCDo5h9WiEbtsA1mEjgFELXdwQzN9EyEO6RPupXhVdSpv5dFiioXah0dWbVZ-LDquEB0-YS7aE43EYCfm-g7fjj9us_Q0PIO9qE2nquivqvXLS2h238fyLqVPjck4i1tzY7ScMQ7eCQ-thDuy_ni1VQSPUzMlXO6IsSkO__BOGuOgGlMObxbPpWhjJfY3D-z28PyUapacRkkd9aRbU-mixP1JCpMf1L3AqbGYcE4k0iBnt9izk8681eumPtLRaBigB93qvcPJ8872Z5QfzE_rtK95VurLPNfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89dd2a1fad.mp4?token=jyz3QMzhm_1Dee6UWcI7-SkA7kJeyjgYi3EZR3JqOe3xYd8qUxyV3ll_G5WPpsfqgZs17Suy-j00q12CwiLmFIahLmY0LkYhn4s2snCe7sWlywCeICL7HR9bxavV4i1V8h5y3o9v-rXsJ9xNwMJYzk6l4kKMv4L4Bucpf8i-aRu4DE9mlD2MSynlt1Vw_Z-Xx4vQpCl7EQm-lOdueV9cNeNVg9-FQaHYbGkezfMLNuM-CSOHflQevhETHC9XrH2Odv3rPtVNRJZMN_suwEvj31muWz3eUOdMzUES33FAlEzZZfpETB0sf85srGXi2E8yRgh1tCPAjUZnpNW49qZIeCv8Rtzj2mqxB5SdKSRgBfPUo_EN8-mZ-7ZdR1ZVwLHVi4tg2mOC4RLCDo5h9WiEbtsA1mEjgFELXdwQzN9EyEO6RPupXhVdSpv5dFiioXah0dWbVZ-LDquEB0-YS7aE43EYCfm-g7fjj9us_Q0PIO9qE2nquivqvXLS2h238fyLqVPjck4i1tzY7ScMQ7eCQ-thDuy_ni1VQSPUzMlXO6IsSkO__BOGuOgGlMObxbPpWhjJfY3D-z28PyUapacRkkd9aRbU-mixP1JCpMf1L3AqbGYcE4k0iBnt9izk8681eumPtLRaBigB93qvcPJ8872Z5QfzE_rtK95VurLPNfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سرلشکر محسن رضایی
:
به همه کشورهای عربی و همه کشورهای همسایه می‌گویم اگر آمریکایی‌ها سعی کنند روابط تجاری و مالی ما را مختل کنند، ما دو کار انجام خواهیم داد
🔹
اول، ما قطعاً به شرکت‌های آمریکایی حمله خواهیم کرد - مانند شرکت‌های حفاری آمریکایی که به طور گسترده در اطراف ما فعالیت می‌کنند
🔹
از سوی دیگر، ما به کشورهای همسایه نیز می‌گوییم: با آمریکا همکاری نکنید، زیرا ما به طور مشابه پاسخ خواهیم داد.
🔹
اگر یک کشور همسایه با آمریکایی‌ها در اعمال محاصره اقتصادی علیه ایران همکاری کند ما کشتی‌های آن را در تنگه هرمز مجازات خواهیم کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/akhbarefori/691445" target="_blank">📅 15:10 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691444">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gth2LoGGPfVUFj_hH_vykMEtfAUJsQQKBxk2j2Ef-1oJB9f-33EffAkvhiarN9MaIMPJCWeLBu5rkj-P22igDg4jEWQUaLu3Osx0Db7Nv_OcRmIBPEWWDPjPFnDsW4NhjEVGxXjbJqFaE-wfXDgZbdqEAKcIJDkLE-QXc9-EJcYxoeu-YmWpqyn90U0B9IuNosv3r6sjanxwEo2hJkcOCDchWhBse0LApLIDfbaajUqjeZ6S64u8hZhex4quVqXdEOGoWUQWzjRO9PE5Ic5a07novaougupulc9ksaklCVOXIcr9R97NgK1NEJr4HKXQCMYRxzOmy1AAImI48BozeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
روایت یک سقوط | کوچ اجباری از گوشت قرمز به مرغ | سفره ایرانی چه چیزی را از دست داد؟
🔹
سفره خانوار ایرانی در دو دهه گذشته فقط کوچک‌تر نشده، بلکه ترکیب آن نیز تغییر کرده است. آمارهای مصرف نشان می‌دهد گوشت قرمز که زمانی سهم قابل‌توجهی در سبد غذایی خانوار داشت، به‌تدریج جای خود را به گزینه‌های ارزان‌تر داده است؛ تغییری که نمی‌توان آن را صرفا نتیجه تغییر ذائقه دانست.
گزارش خبرفوری را اینجا بخوانید و نظر بدهید
👇
khabarfoori.com/fa/tiny/news-3246556</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/akhbarefori/691444" target="_blank">📅 15:07 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691443">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">♦️
جنگ در کمین انگلیس؟  بی‌بی‌سی:
🔹
دولت انگلیس از شهروندان خود خواسته است که مواد غذایی کنسرو شده و آب آشامیدنی ذخیره را برای جنگ احتمالی با روسیه آماده کنند.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/akhbarefori/691443" target="_blank">📅 14:58 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691442">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MI-LITfnuw6rj9XrgghQzazrFY2CAKNBCpXcs30B7WRCY7WPJruDQqT7wxVJYebpUIimTj1VNjce-jLLXPWXToYt4-gv2F9pDt5WYj_HouvP4RDpBxuMLy7YFisNc0xRsZKOIcNHE0IWHHzauHL5lJzro_QiAqDkyFiyQtUatXuYoWe3Eyod8LghI5ZadsuHeCf1b7fQBFYYYKiAFD2Ndoyw7BTkITUryBADxt2RLPgGISev_cmpnzS-TMHedX3_p8ez3zHZZO9hdgt-Bwo18aoowkxd1QcrZgN3ZXk0mwDRmmQNcwhemx6b7Z5yneGYroCej1-VYyXRlBtKH4Touw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویر برگزیده رویترز؛ حضور سربازان انصارالله در کنار جنگنده ساقط شده سعودی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/akhbarefori/691442" target="_blank">📅 14:56 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691441">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">♦️
مصرف سبزیجات، لبنیات و میوه‌ها در مردم کاهش یافته
احمد اسماعیل زاده، مدیر کل دفتر بهبود تغذیه وزارت جامعه بهداشت در
#گفتگو
با خبرفوری:
🔹
بحث گرانی که اتفاق افتاده دامن‌گیر اقلام غذایی نیز شده است و انتظار این است اقلام غذایی مصرفی خانوارها مقداری کمتر شده باشد؛ به ویژه میوه‌جات، سبزیجات و لبنیات.
🔹
سبد غذایی مطلوب را در سال گذشته منتشر کردیم. تا قبل از این اغلب اقلام غذایی در قیاس با آن سبد وضعیت مطلوبی داشت و کل کالری دریافتی مشکل چندانی نداشت، اما در حال حاضر با توجه به گرانی ها احتمال می‌دهیم دریافت کالری پایین تر آمده باشد.
🔹
اقلام غذایی را که برای تامین مواد مغذی برای ما مهم است به وزارت رفاه معرفی کردین که حتما در کالابرگ گنجانده شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/akhbarefori/691441" target="_blank">📅 14:55 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691440">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vcHnFyFmK9MAyr4gAB0bURfO5sUSIZ9RwFH8XebS0cLl5qWmEguyN6pvIHAa7BNC1KsvLShvv0U0UNXnADDdVOxOGHWHTm2fj4_Drsg8UVR6XIZxytsOChhX3i8P4cSmN2Io1lWM-_zoUUoROV89mjKvELRFH1jIGr-m8p59SruZqhUAYIVPlgVNw3Q_3kIWLfFtwIZ5ifnjdFDj3yhvNvtakjzlWLFvvR1U7tMppeq5CvK48r2P5eMGQImcVU8wYMRJUqdlcfPHMVseKVpOyD1GDZsPUcuUmA97F9Lf4YsDGRFLY01kS6DpB9ncEUNkupBJcHA-vH2rEsmzC9nBkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کف قیمت موتورسیکلت به ۴۰ میلیون تومان رسید
🔹
قیمت ارزان‌ترین سی‌جی ۱۲۵ کارکرده به حدود ۴۰ میلیون تومان رسیده؛ یعنی یک کارگر برای خرید آن باید حدود ۲.۵ ماه کار کند. قیمت برخی مدل‌ها نیز به ۳ تا ۴ میلیارد تومان رسیده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/akhbarefori/691440" target="_blank">📅 14:49 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691439">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mq6e-QWhptYY1dJU0oxwDvYtCw3Y1i0SVkXoN-KBLvFFlt_uiYZLrdjRDFSYCKiI749hEZGB93kwWNHl2QfWnb8x1XNFQbeDPVCzLZwEpb9pWW7TgrrzLLiM0TPxEjwa-TXEe5WUyHEw4NLUCCHVpHh7BE92-1tRhnCCwmC3_Y0uSOkdUFmrO_sRE7PRoP8iSOLk28FjKzh4R4_vWnFMfgcSQ3hIBT-7Nm14faHRiiz0ifnHLJhFKhNON0KRZP46kpb_TUt3qt2g7_dgyVOolvha3RPxmzLw_J8QaozBcrd48Fp8s67wlL8WXT6PPpe96zRWQzcbAS7xYjLSXcN95Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
پست شقایق دهقان برای شهدای دانش‌آموز میناب: امسال ۱۶۸ نفر غایب هستند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/akhbarefori/691439" target="_blank">📅 14:45 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691438">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">♦️
ادعای یک رسانه اماراتی درباره جزئیات بسته پیشنهادی ایران برای کاهش تنش با آمریکا
ادعای ارم‌نیوز به نقل از منابع غربی:
🔹
ایران توقف غنی‌سازی بالای ۵ درصد
🔹
آزادسازی بخشی از دارایی‌های بلوکه‌شده
🔹
بازگشایی کامل تنگه هرمز را پیشنهاد داده است
🔹
این رسانه همچنین مدعی شد آمریکا همزمان برای حملات هوایی و موشکی احتمالی به اهدافی در ایران آماده می‌شود.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/akhbarefori/691438" target="_blank">📅 14:44 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691437">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">♦️
پزشکیان به نیویورک می‌رود
🔹
بر اساس برنامه فعلی، مسعود پزشکیان برای شرکت در مجمع عمومی سازمان ملل به نیویورک سفر می‌کند و ضمن سخنرانی، با برخی سران کشورها دیدار و رایزنی خواهد داشت. یک هیئت بلندپایه نیز او را همراهی می‌کند./ تسنیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/akhbarefori/691437" target="_blank">📅 14:41 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691436">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c1c8fb3e26.mp4?token=O8h2q7Z_pGjoJFlXm1emO-nkyjPpad8dl6jSvQNiZBP3qNqcworits0kTtRyRIcJXpB4QyUVuopuy4tHZXozGTJoOLp6w5f0_tqcig5TnRZ9qy96lCDXY6agkH_0Q5nJSxP3FL9kdecoLDFuwXrtcGjso7b6lv5Ay6srATgug8Ox2NYfoyd8FCOf8GyFJqH13Q7uTUKBrhTJB3SDBzGX1x5_0SW-5EKb6gN2sOEJuCfZVjo0TNcs_c4CHesnemsdlylWGbBy3VgPq6HebhjmpLnMMD8bkdEiFDG5f13ZCyId46AKVdamNhDKP-ZwDpECOFTiacYJGsG1yJJprH2PEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c1c8fb3e26.mp4?token=O8h2q7Z_pGjoJFlXm1emO-nkyjPpad8dl6jSvQNiZBP3qNqcworits0kTtRyRIcJXpB4QyUVuopuy4tHZXozGTJoOLp6w5f0_tqcig5TnRZ9qy96lCDXY6agkH_0Q5nJSxP3FL9kdecoLDFuwXrtcGjso7b6lv5Ay6srATgug8Ox2NYfoyd8FCOf8GyFJqH13Q7uTUKBrhTJB3SDBzGX1x5_0SW-5EKb6gN2sOEJuCfZVjo0TNcs_c4CHesnemsdlylWGbBy3VgPq6HebhjmpLnMMD8bkdEiFDG5f13ZCyId46AKVdamNhDKP-ZwDpECOFTiacYJGsG1yJJprH2PEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چین ۹ ماهواره را با یک موشک به فضا فرستاد
🔹
چین با موشک «لیجیان-۱»، ۹ ماهواره را با موفقیت به فضا پرتاب کرد؛ این ماهواره‌ها برای پایش محیط فضایی، مقابله با بلایای طبیعی و آزمایش‌های علمی استفاده خواهند شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/akhbarefori/691436" target="_blank">📅 14:37 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691435">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">♦️
سفارت چین در عربستان از شهروندان و شرکت‌های چینی خواست با دریافت هشدارهای امنیتی، فوراً به پناهگاه بروند
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/akhbarefori/691435" target="_blank">📅 14:26 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691434">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PIdlRMAONZKilPyKn1xzxkRJk_fIaB5Xszx3TZmT-NoA7azA6MHGG7VreWNP71rC3gd5Qf73dcibwN2HrvUuLik_qMjLFCmefFQsCC2F43qjJW2rC4vwODLAyb9RtC6CipEOydiBFN0gVmuB-149LIpNlTIWp4uzg9CDOTsylXTC3v0u_TqFNSsHOeyYQWeblAMyJgQ1PPS5rz16CUZbX7aKPUpcLNWUlNRFjvLUJu4FfKXF8AT04NDf4y2J-pUcarm9ZTtV0vAvpiTrN7ti6mEHfsYRyyHZJyazlbH8Y-CR3Q48Fvj3t1ms83sNxmKQD5Ut5AafA2yQZQKf4uzdOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۲ الی ۱۴ مهرماه؛ برگزاری هفته فرهنگی ایران در روسیه
🔹
کاروان میناب۱۶۸ متشکل از فعالان فرهنگی هنری به روسیه می‌روند
🔹
دیوسالار معاون توسعه همکاری‌های علمی و فرهنگی سازمان فرهنگ و ارتباطات اسلامی در نشست خبری: هفته فرهنگی ایران در کشور روسیه از دوم الی ۱۴ مهرماه با سلسله برنامه‌های متعدد فرهنگی برگزار می‌شود
🔹
این برنامه ذیل اراده مقامات عالی ۲ کشور شکل گرفته تا روابط ما در ابعاد مختلف رشد پیدا کند
🔹
این هفته فرهنگی با گستردگی بیشتری نسبت به قبل برگزار می‌شود و قوام‌بخش روابط دو کشور خواهد بود
🔹
این بزرگترین رویداد بین‌المللی کشور در خارج در دوران جدید و بعد از جنگ تحمیلی سوم خواهد بود
🔹
کاروان ۱۶۸ نفره متشکل از چهره‌های علمی، هنرمندان، فعالان فرهنگی و هنری و ورزشی، فعالان حوزه صنایع خلاق و صادرات فرهنگی در قالب کاروان میناب۱۶۸ به روسیه اعزام می‌شوند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/akhbarefori/691434" target="_blank">📅 14:24 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691433">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">♦️
دولت کویت مدارس ایرانی فعال در این کشور را تعطیل کرد
🔹
مدارس ایرانی مستقر در کشور امارات نیز سال گذشته تعطیل شدند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/akhbarefori/691433" target="_blank">📅 14:06 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691432">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">♦️
در کشور ۱۸ تا ۲۲ درصد زنان در سن باروری  مبتلا به کم خونی هستند
احمد اسماعیل زاده، مدیر کل دفتر بهبود تغذیه وزارت بهداشت در گفتگو با
#خبرفوری
:
🔹
مکمل یاری با آهن را پیگیری می‌کنیم. برنامه غنی‌سازی آرد با آهن و اسیدفولیک دارد اتفاق می‌افتد.
🔹
با همه این‌ها آمار کم خونی زنان در سن باروری بین ۱۸ تا ۲۲ درصد است. به نظر می‌رسد در این حوزه باید ابتکارات بیشتری داشته باشیم که برنامه‌ها اثربخش باشد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/akhbarefori/691432" target="_blank">📅 14:01 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691431">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">♦️
هشدار قرارگاه مرکزی حضرت خاتم‌الانبیا (ص) به آمریکا و کشورهای منطقه: خطا کنید هدف حملات دردناک قرار خواهید گرفت
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/akhbarefori/691431" target="_blank">📅 13:57 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691430">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oSKVXosGD9hz8aM6tmda84VN8suF8BI2-Masqw3vpSWbJhJQtw7sobXBsMTP-eoM8uxFz_lUnpUSHjiugavfCYswPNyfvnf8CNGZC6JavkrTTLHYGqtdEsrRyf37XGJ4nlDQuYiRQJ3HyrbMFumF_2w8daMf5p0WxoKPbFFuKtQssf_ya8aJ3p15vFZIxsZRXcHZM_SwX6Ra3VWaOVBJUwKSYiTtye4CtIeZtMax8dALlEi1LhkkVaTJXEP6QGWJis5RaB9KMUCYu4_FdaCsQn3ozXcwbvSY41i6XrkJ8x_Oa7tVeWyJrflOs-cgKTYy9fhLkswaRv6mVQvIgFimnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای شبکه فاکس‌نیوز: در تأسیسات هسته‌ای طالقان فعالیت قابل‌ توجهی دیده می‌شود
🔹
شبکه فاکس‌نیوز با انتشار تصاویر ماهواره‌ای از تأسیسات هسته‌ای طالقان مدعی است فعالیت قابل‌توجهی در این محل دیده شده و یک سازه بتنی روی آن ساخته شده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/akhbarefori/691430" target="_blank">📅 13:49 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691429">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">♦️
۸
استان دارای بیشترین مدارس آسیب‌دیده در جنگ
رییس سازمان نوسازی مدارس کشور:
🔹
استان‌های هرمزگان، مرکزی و شهر خمین، آذربایجان شرقی، آذربایجان غربی، فارس، اصفهان، کردستان و کرمانشاه از جمله مناطقی بودند که بیشترین آسیب به مدارس در آن‌ها گزارش شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/akhbarefori/691429" target="_blank">📅 13:40 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691428">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">♦️
سازمان تأمین اجتماعی: واریز حقوق شهریور ماه بازنشستگان از فردا آغاز می‌شود
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/akhbarefori/691428" target="_blank">📅 13:38 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691427">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفروشگاه قرار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bJy_Pm5OTMlLtgeOIfsDHfBkxxlqei_r2_SQR1gNlNIOP2UrvsS4cksFUudTpO5N6zXA3DKlIVWn-NlDKby0gpKIpuW79eM_-o3UVUlUQAWATldscPuTUfq7ZR-ftynWWBYtFAAJObDu7V8OXcMSOdrfRwgU02k3zt2S-AJCOovuLb1q4MGRIMkruAyuEc26WJEmJrB04DZ2in_5nsthbOqnvxppbtrKmo8tOdeLRbEb593jxkr8_aE4YTijeBlpmC_l44yAItwEhAEodvCLeuMxa_55zFAsuiNl9KPv08_GTn4nAu8fInSOFAhzXGh2-bzrjvllngTd6szGtCtvGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
پک ویژه سوغات رضوی
یک هدیه معنوی و ماندگار از مشهد؛ ترکیبی از عطر، مهر، قاب‌فرش و تسبیح رضوی برای کسی که می‌خواهی یاد حرم را با خودش داشته باشد.
🤍
داخل این پک:
🌸
عطر گوهرشاد — ۸۵۰,۰۰۰ تومان
🕌
مهر تربت مشهد — ۱۸۵,۰۰۰ تومان
🖼
قاب‌فرش ۱۵×۱۵ — ۱۵۵,۰۰۰ تومان
📿
تسبیح رضوی — ۲۰۰,۰۰۰ تومان
جمع قیمت اصلی: ۱,۶۳۲,۰۰۰ تومان
🔥
قیمت ویژه پک: ۱,۳۹۰,۰۰۰ تومان
📩
سفارش:
@gharar_order
قرار؛ تجلی هنر و ارادت
@ghararshop</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/akhbarefori/691427" target="_blank">📅 13:36 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691426">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tUPqGfRP4TzqGSilfr6Ft91mCiRkbNw3bVSuMFDakuJ9h6Bl-cwJjX30N-vTubcBRxl4kCI9Ev8AVDM4ej9zBMig449r6szm_UCFcfkUCcnwpy749kvW4tEbpr053kSv6cOUuRwET64bCfXPcKGG_v_qtIBOtfIYrYBsSQqNhAdpnOHhbw7ynP3KovPuqr8c542z5nFHnAkG67ZAOuMV1LaDWjl8SsZrEnWFYnYsDFPDH2HyJ3syqClkkilKXo63cVktSpChaDtu-InPXMN4YknUSK-44_Wr4d4FMA-AorrjYuAhYnbU2uN3T5CcPzmBh6QS-RWTk1aRAjBSws-ztA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وزارت اطلاعات: سه کانون عملیاتی وابسته به گروهک‌های تروریستی که قصد عملیات ترور و تخریب زیرساخت‌های اقتصادی را داشتند در ۳ استان ( کرمان، آذربایجان‌غربی و البرز) به هلاکت رسیده یا بازداشت شدند
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/akhbarefori/691426" target="_blank">📅 13:31 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691425">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">♦️
وزارت اطلاعات: سه کانون عملیاتی وابسته به گروهک‌های تروریستی که قصد عملیات ترور و تخریب زیرساخت‌های اقتصادی را داشتند در ۳ استان ( کرمان، آذربایجان‌غربی و البرز) به هلاکت رسیده یا بازداشت شدند
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/akhbarefori/691425" target="_blank">📅 13:28 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691424">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b1048d146b.mp4?token=vUIQkYnJtZGzozQ9Fc9hLbOMuhWP-uQW8gRgr_sfwKHCwhdS8BrgfrgXMVKpg1TBXrEwez33J4Mt841Qr63GgQyGmIH0OUMEC73x5kF3I-Se8hYE1HkUOmMfTy02xyip_kS4A5sfgLHPGFlBuxrUPSJWpMTnQqiAgdrIga60bXkPSAuPi90DWcX5I6ZNIHF2UNPuWeeDd_H-kN6v2Vyc2wRS0x2PgAS0UwLWD_Su8tI-fS0snY6Sou0txAB80wsQOijFXdATFX-dXpVMD6s-I1gjRtEgPTl-TtZEXZ31wFMKcOK3BKTa948VtPYRNG1DOhVh2-9v_xoAWf0AhMjRfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b1048d146b.mp4?token=vUIQkYnJtZGzozQ9Fc9hLbOMuhWP-uQW8gRgr_sfwKHCwhdS8BrgfrgXMVKpg1TBXrEwez33J4Mt841Qr63GgQyGmIH0OUMEC73x5kF3I-Se8hYE1HkUOmMfTy02xyip_kS4A5sfgLHPGFlBuxrUPSJWpMTnQqiAgdrIga60bXkPSAuPi90DWcX5I6ZNIHF2UNPuWeeDd_H-kN6v2Vyc2wRS0x2PgAS0UwLWD_Su8tI-fS0snY6Sou0txAB80wsQOijFXdATFX-dXpVMD6s-I1gjRtEgPTl-TtZEXZ31wFMKcOK3BKTa948VtPYRNG1DOhVh2-9v_xoAWf0AhMjRfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
میکس‌های محبوب قهوه را بشناسید؛ هر
ترکیب، طعمی متفاوت
☕️
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/akhbarefori/691424" target="_blank">📅 13:24 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691423">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">♦️
حاجی‌دلیگانی: طرح سه فوریتی خروج از NPT تقدیم هیات رئیسه مجلس شد
حاجی دلیگانی، نماینده مجلس:
🔹
با توجه به شرایطی که کشور دارد و تهاجمی که دشمن در ۲ مقطع به ما داشته، ماندن ما در NPT جز ضرر چیزی برای ما ندارد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/akhbarefori/691423" target="_blank">📅 13:17 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691421">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N_L-vcuMkXyt2dZT52EuQsBbHxPOjpYBWfaBEKP2P74mirEn33UmMCBhfEtvCTXeOfee7r1rYtrXC6oYuYF2jMqDP_8f7P_knvB8lvsQL31EbGEAKSJnbozoYMZVVfpNIKrrlFjWInCqT8m20S3mXWtjO88z0uqEAkv2jNGVkdzAOqnGI_Zy-vogmq8_kvU-iaWzWFtenozIhIcKPpzIEX9NWgkcvdo-AnOfaK6eEy0Ib4p9ZeIcFfyRpi_s7ZsOXVeXD1GVoBj18kvHrRE7h6eyhi8P4pcUC51fpFyp6Y1NUcjZOQpuUYFfPY8IpPZM0kzZudxHJBJ-fJCT9frMgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j1F0N76uzgbRgR_cRKdRaIUJmxjnuiKBd7Z-fbWPeemha3B-PxIHZjA_tCJ1yrW8GbbysvrZtSwBONf94Gy6-XfeFNq5vxhNeKlu37A34w3L6cFbu3KIKfy8ICWF1Gi96Y6TQHxjzHkIiKLCZIqgvdin2PNSsGJoTRiHKO5o5F47aw-YZ8Px4GmDgfaJpmw3iGphLqYSiXRwWceev2TFKcRw52Nrm1L0jdfhYhD7zK1WYqOaRbyZEkKN_I2OX7bJYnOlXFLjWS3eJKBaRRvh9rIef0pFqw99YQz7vjseabf3i1RY8HiVMBbugWn1Rjv0PZ-q1tHy3l97-NB6woRcTg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
دکمه های کهکشانی/ یک ایده خلاقانه برای متفاوت کردن لباس‌ها
✨
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/akhbarefori/691421" target="_blank">📅 13:07 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691420">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IAuBC0KROSJz6IkSQx70OVk7gayglUS1SgLCvL0Q-7qCahZDghcPk9pMo3jz20rns4fRB_61ToJhMmPQqc6f2l3PfaWqO8y2XoltMcXjR0iziXjjpPiUt7GsAqSYoUyfV7h2GVsQA6d90HQ5iDjoP2JNo05j9zKJu1C63ltMJUnLoynWKhypQ2G6MC8JHC0_sTc33o0KPyPaq0a88WZgYOwNq-ATxoTg0nAmNDyMwr1pzYLRO9AXH_mQQ5eUfpB011RSSyrCJ1YvXxK3lSn3_UAkYjjtT1FVDfRtgXFHUlN85r9vZydDUfgOx7QWwQEoxgs6pvbe7Gres2ynlB8KoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ایندیپندنت: تجمع ۳۰۰ هزار نفری در تهران و آغاز جذب نیروهای داوطلب
🔹
به گزارش The Independent، بیش از ۳۰۰ هزار نفر روز جمعه در تجمعی سازمان‌دهی‌ شده در تهران شرکت کردند؛ تجمعی که در آن آمادگی برای دفاع از ایران و آغاز آموزش‌های نظامی اعلام شد.
🔹
به گفته این رسانه، بیش از ۶۰۰ هزار نفر برای طرح «جان‌فدای ایران»  ثبت‌نام کرده‌اند و انتظار می‌رود شمار شرکت‌کنندگان در آموزش‌های نظامی به بیش از یک میلیون نفر برسد.
🔹
تا ماه مه بیش از ۳۰ میلیون نفر از جمعیت حدود ۹۰ میلیونی کشور، به‌صورت آنلاین یا در تجمع‌های عمومی برای فدا کردن جان خود در راه حکومت ثبت‌نام کرده‌اند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/akhbarefori/691420" target="_blank">📅 13:00 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691419">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/53d3fe8bc3.mp4?token=meEGa3V8ICAHTltQU_oLkOWTf_eBrlDx81SEaCAI090CrOu8yy18kEcY6WQTkOYZZ6PyQKMaO4Fw7MOhYwNouYPy-SjNoZT4TNdXcEvhm-3PvWZ5UpElnqjhxu8yYbfHuIXQbaG73OxQ_-cUg7XuX4bty1_cD_CYbsIR6AmVOimN7Pc4wMwjY9CspILiYd8nMF_7E87dx9Pfx_verURAmifxHGAkv9wcEAJhuyHHTa7YccDZn3eHyonRpEOijEJDDELgjClf5s_6R8EdwFHqOFDz2pjsklRcMPHwbrgLT7BPptuO8SzVaHe_FNJI6vhkGZdKb8mr9XqROkrjBxgitw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/53d3fe8bc3.mp4?token=meEGa3V8ICAHTltQU_oLkOWTf_eBrlDx81SEaCAI090CrOu8yy18kEcY6WQTkOYZZ6PyQKMaO4Fw7MOhYwNouYPy-SjNoZT4TNdXcEvhm-3PvWZ5UpElnqjhxu8yYbfHuIXQbaG73OxQ_-cUg7XuX4bty1_cD_CYbsIR6AmVOimN7Pc4wMwjY9CspILiYd8nMF_7E87dx9Pfx_verURAmifxHGAkv9wcEAJhuyHHTa7YccDZn3eHyonRpEOijEJDDELgjClf5s_6R8EdwFHqOFDz2pjsklRcMPHwbrgLT7BPptuO8SzVaHe_FNJI6vhkGZdKb8mr9XqROkrjBxgitw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بسکتبال ایران با شکست چین، برنزی شد
🔹
تیم ملی بسکتبال ایران در دیدار رده‌بندی بازی‌های آسیایی با نتیجه ۷۰ - ۷۹ مقابل چین به پیروزی رسید و به مدال برنز این رقابت‌ها دست یافت.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/akhbarefori/691419" target="_blank">📅 12:57 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691418">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd62af64b8.mp4?token=Pkr-TOdKQtlRzdD3_rnJeQBBsQG0ZZPjePJ9BgUcsy2b8_D8Fdx9lur-mXMM6UyogTy5NjPIGBATw9vNnXXc_VGy7F3HpvVjEImT2o0ljeEK7rZHeXct5em2j4_x-UV0OQ9P2x1_uOMqWKFxWG5p7cLVw0nVzSQ7U10b7SEXhRzEvZXUsAuDH0JA-QZ-JvNmbU4M2MgFAEhOTw7BRTTqMalq3TSQ7ZqSpExG97XHunMOcd-G8cEj82qarQni51RY_3Vk5Ef0Xi0mqOVp4TfLi-LVxgdpSkpl2_sQVyEkZQnrVrVS7SUp7Y3smJBNh0DHq_gQrgdDmpYDHBMXuUbBtw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd62af64b8.mp4?token=Pkr-TOdKQtlRzdD3_rnJeQBBsQG0ZZPjePJ9BgUcsy2b8_D8Fdx9lur-mXMM6UyogTy5NjPIGBATw9vNnXXc_VGy7F3HpvVjEImT2o0ljeEK7rZHeXct5em2j4_x-UV0OQ9P2x1_uOMqWKFxWG5p7cLVw0nVzSQ7U10b7SEXhRzEvZXUsAuDH0JA-QZ-JvNmbU4M2MgFAEhOTw7BRTTqMalq3TSQ7ZqSpExG97XHunMOcd-G8cEj82qarQni51RY_3Vk5Ef0Xi0mqOVp4TfLi-LVxgdpSkpl2_sQVyEkZQnrVrVS7SUp7Y3smJBNh0DHq_gQrgdDmpYDHBMXuUbBtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
همه بیماری‌ها از سرماخوردگی ساده تا سرطان التهاب شروع می‌شوند!  #سلامت_روان
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/akhbarefori/691418" target="_blank">📅 12:52 · 29 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
