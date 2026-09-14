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
<img src="https://cdn4.telesco.pe/file/bW6ZOHDRiJ7isjHmAw30g7F0CM8osxjz0rsXHRM9mPErjNGoYWG-fqpbALY9hCiFnJcFMpsecnmW6xXqbdvnnlJIltgZ6E_Dwg-hA0F2HQiVSd-x4K-7DNoFDW_M1WALRwJKkl09rQ4UCPFQ-MLt35YAC2GBy71J13p2UqmROYvHLG2SO9kELF0meo3hldsfCAlb3Cb4n8SV04fFOTcE5OH3MZR1QOpgmgfO_sFJkaWGIllV7VSeNY5l6MbSEX3-OtgV9DTlk1zvpbKil4tXIG_FpthxdDpMMeq67S3p8lVXq9r7yvb8uUb8dzOKSJtq899C1zVEVvxACkhANJYEKg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.84M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/farsnews.agencyتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-24 02:22:16</div>
<hr>

<div class="tg-post" id="msg-462144">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">دفاع مدنی عربستان صعودی برای شهر ابها و استان خمیس مشیط‌ هشدار خطر صادر کرد.
@Farsna</div>
<div class="tg-footer">👁️ 2.42K · <a href="https://t.me/farsna/462144" target="_blank">📅 01:52 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462142">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5db5249518.mp4?token=GPYJcqcH918pzQT1e5ElF-8qwwJ1W9WMtQCnjjYqd20SjMJoDrUv_-QZlYunkyOlXbGWbl8sdGAHCCS2626n8HaPTB7qb8g44YZK8lc8oULvRkA3JLjVdkmoL0nU6TfIGuHJmEy_wo3piJanwIFC5qZTwCjy6lGhjX33XedOmEIzK4xppzoZ4wdFSywQnOeFiin05IdlEYO1rXvT__7MisrnKa_trWPmeN5_zqRwh4hCoQSfECjKh3klmdb0_4R4zHz7CLWQfKXV2wQZBk3eKZhsko9tRdckkIIZliFADxb_6cd83N9Bftg-2lrqaKbKjUjdWupPkKM_bhWkwmIAUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5db5249518.mp4?token=GPYJcqcH918pzQT1e5ElF-8qwwJ1W9WMtQCnjjYqd20SjMJoDrUv_-QZlYunkyOlXbGWbl8sdGAHCCS2626n8HaPTB7qb8g44YZK8lc8oULvRkA3JLjVdkmoL0nU6TfIGuHJmEy_wo3piJanwIFC5qZTwCjy6lGhjX33XedOmEIzK4xppzoZ4wdFSywQnOeFiin05IdlEYO1rXvT__7MisrnKa_trWPmeN5_zqRwh4hCoQSfECjKh3klmdb0_4R4zHz7CLWQfKXV2wQZBk3eKZhsko9tRdckkIIZliFADxb_6cd83N9Bftg-2lrqaKbKjUjdWupPkKM_bhWkwmIAUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترور یکی از فرماندهان گردان‌های القسام در غزه
🔹
منابع فلسطینی گزارش دادند که در حملۀ هوایی رژیم صهیونیستی به یک خودرو در شمال شهر غزه، «أبو اسامة البطش» یکی از فرماندهان شاخۀ نظامی حماس به شهادت رسید.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 2.89K · <a href="https://t.me/farsna/462142" target="_blank">📅 01:49 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462138">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LJxZAeQMLJVtVvK0LZTbgzjAnQsJ_jRkIw0zDLfoY1Sf_U0XYLH3d9oCnzrmboFUtyFofjgvuzWQ-lcMOZTwTmWkcYzcKhpj0-qStSgFEuihH9UakPiUO47Tbf81olz-5amwgVEyQiLDvpyq9HhUKMUN0bbQCNN3tPo9Q5gl8wIPwfW8geOIpn4NR1KAXVj1aSf33U52Xd1iQ-NAYialWZLM4yxM8IpGWWrP_K1NIbHE8ApY_LIV9jDH3RksyzYmMm-uvnrvhkeTA_0-KvWBwsatS4GkOYK1GPQDA-fqts6ofyjnXVQHeQ3-bZiRYtFeMfvU68UNLuE9yi0W9mROrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/awuN9MCnY97BotKf_IAZeYftBk3xyEJwZV_nLFJOK9bH_5nyHmlPu7rRpluKrxHp4l3LNWT7oEW-s7Uv_th9kgesvCLRJ0HlZXL7HWs-aql0qilWSJd2H_9aIX7XIm5uoBoGr9mY4vXhX0DaG4PzSuUTKl2cQt4f-TtBNTtbd6X_pJvLSxw7KmS7sM8TYctkikSTPanvrog0JFFWlRE74lKnQTyGH_F_-nJ1XiNg_v7BLyR2OPSi6Z-Mg_FwXOXGDBCywnp4STuA8Nk-1zDkjd0J-BaDb1CNkcvnaaskpWcltZlzIdaX7Px9HgVtR087fikeer7NMy3bBLtXGLcWJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IBqb8YPsHTVFJS7-7Yb___xkp3jjpQ4aTurRwV8veQHQHTSo2W7RHxsFwHY3UtQpesdPsG0XOYfEKADXU6TkUxKLYRSycUjo4oweq0-ktztQimPOGGOoXlMtv1d2YQA_W71_n-eE5nKF4tyk8mOlWQMkS11zVPWQIpS9s1aWk3bI2QCz2D5zZBWl_iIy3i4jVuZ1NImA0X0XwBM6WZt21qMgvbmNg0SsU8mukkeUPQQv2QijyY4qd2j0RlVv3netcXxZr3u0OTTbdtSZT_KMcAZNluZkwKF0OuX-Qc5l3Yl6EfO3aTtE2L_uclIojgsrXJ_7KO1oWvVaIkJPZql6vA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1dcaf7c0df.mp4?token=Pdb-MNQrJISnzWHuj1kjyiNQMVPHtf_OpyVDYUWV_syzqpQCWyVX84rark9B2AeeMKQ7K_uCAK55_z9AmgSif9sS-T0IM94V05Xjlak1ngDhMBVSEWoVPqHzmCsMxvMH6-v-CCo2wBVOR6PGkZG7MI1GTEqUOHkAe6g_a1AgsH72A_Q-DwVVLwNcdWX-FVNtuBauaAnMIQIVqvEx-EZiBkbVPWRbpDokXmFA9X9RwdnCrDKHbau8w9YNEAMzmjslnihfqZzH_HfjpUR2R9sb0dMq9K-ui_uZj_I-MhChPtkjyD3RR1l86ydLNpMRuUAzBImmT2ElrVnc_YQIckvZbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1dcaf7c0df.mp4?token=Pdb-MNQrJISnzWHuj1kjyiNQMVPHtf_OpyVDYUWV_syzqpQCWyVX84rark9B2AeeMKQ7K_uCAK55_z9AmgSif9sS-T0IM94V05Xjlak1ngDhMBVSEWoVPqHzmCsMxvMH6-v-CCo2wBVOR6PGkZG7MI1GTEqUOHkAe6g_a1AgsH72A_Q-DwVVLwNcdWX-FVNtuBauaAnMIQIVqvEx-EZiBkbVPWRbpDokXmFA9X9RwdnCrDKHbau8w9YNEAMzmjslnihfqZzH_HfjpUR2R9sb0dMq9K-ui_uZj_I-MhChPtkjyD3RR1l86ydLNpMRuUAzBImmT2ElrVnc_YQIckvZbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🖼
حال‌وهوای مزار رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 3.33K · <a href="https://t.me/farsna/462138" target="_blank">📅 01:41 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462137">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/948ece81c4.mp4?token=AFTmIsU9HBSWgipjAYkM_1dwxr8jIFWZtDa0vB617Eo4rY-lAvdXU1tOhDdk9PUlbGS5GEtxLBsuZmVxOQZ-H8XhF8K01fPPPSLpzv4Yer7uCjgTF2r45EfUoMECndTLJa23x5ZP77666kzVkG4e71L6oKrcw5VvItZ_QNax67wiFMUnHS5j57G9o_1SaDxo5XjemVoZMI6MJtyynUJGoC3Ksndu7C8kYUdB4-QGw8DlSWzeYN2G6MT_p-ysC3YnmUm_Usl0hJHuhqQS4ePpjwZc2V1GpwM-UOujlQJY_ycyvyab5P78h7GI3L6Xrrq4msrjn_OaPBokB3XZ_niaDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/948ece81c4.mp4?token=AFTmIsU9HBSWgipjAYkM_1dwxr8jIFWZtDa0vB617Eo4rY-lAvdXU1tOhDdk9PUlbGS5GEtxLBsuZmVxOQZ-H8XhF8K01fPPPSLpzv4Yer7uCjgTF2r45EfUoMECndTLJa23x5ZP77666kzVkG4e71L6oKrcw5VvItZ_QNax67wiFMUnHS5j57G9o_1SaDxo5XjemVoZMI6MJtyynUJGoC3Ksndu7C8kYUdB4-QGw8DlSWzeYN2G6MT_p-ysC3YnmUm_Usl0hJHuhqQS4ePpjwZc2V1GpwM-UOujlQJY_ycyvyab5P78h7GI3L6Xrrq4msrjn_OaPBokB3XZ_niaDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
۱۹۸ شب از خون‌خواهی مردم قم؛ داغی که سرد نمی‌شود
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/farsna/462137" target="_blank">📅 00:49 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462136">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DT1Db4YYp7Xk4D41sD9IVPDJhZXrW_SvdZYlCos2SJ-KjKe6b5TyvNuLctpQhoPuTJVY64wEFoOmPJLzRxqnWEMG_c5Ge1liWil91KrGg-cSLIGmCb7C6wuRsSDl3XKpOH0fnTE9ptwX-3tAczaKpHaziuVpKj1uL6PRPUzjhzAePj-HZYx6GvY1P82RQu3B2pI5JG95iY29AK-rNsU_NAklHitl4slfdWigsHPdw-gNiEOk1U6LvrNtDNawActvLYLlBVf-2oaD_tg41jiTnpLdPBx0O7uAOgjbthN0figsQVDK6b02eDv5jPIBte4HxaKB1-3D-5tNs6erT-d5aQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
دبیر شورای‌عالی امنیت ملی: تا زمانی که شروط ایران محقق نشود، هیچ مذاکره‌ای در کار نخواهد بود
🔹
با سیگنال‌های متناقض رئیس‌جمهور آمریکا حواستان پرت نشود؛ از «مذاکره نمی‌کنیم» تا «برای گفت‌وگو آماده‌ایم»
🔹
معادلات مربوط به نفت و تنگه‌ها تغییر کرده است. دست و پا زدن برای کنترل تبعات، جلوی آنچه در راه است را نخواهد گرفت.
@Farsna</div>
<div class="tg-footer">👁️ 6.15K · <a href="https://t.me/farsna/462136" target="_blank">📅 00:43 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462135">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fkzf-OM2Bryb25K1t3-jQ6hRsO7Q-DgoJSd_ZlzPcwqAkADaNnKR3jT8lyYP1wICEuX0DnIBjUivmfb1JYJFGO7XaxIDusCRTorM0kYegFxsyb80fdvFARqwigXgZUB6zOjPjlRha5Kjf-ct9IEOS00C_NCRPf3JKPhHVuU9zjOVPEjFdUBrQNTskUVRTWLg0yNCFSYKG4tkuxu8T0_vLvJ5LtHkcmgGMw6yFaf0QbpcSmtM9IfXKF7bqj-mt9SMwrXFi78Z9QsknkkfpqkvSOjDKyLjfrWNCYwyvBHpv1zFA9DNBE4m-DU9LLWVjBIw_qEVdn_b7s_Jw_6CbYYnsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چه شد که پس از ۶ ماه، مصاحبۀ جنجالی خلبان آمریکایی منتشر شد؟
🔹
روز گذشته، شبکه آمریکایی «CBS» در مستندی مدعی شد با خلبان جنگنده‌ای که در ایران بود، مصاحبه کرده است؛ یکی از بخش‌هایی که در این مصاحبه مورد توجه کاربران خارجی قرار گرفت، این است که فرد مصاحبه‌شونده می‌گوید با سرعتی بین ۱۱۰ تا ۱۶۰ کیلومتر بر ساعت سقوط کرده و بعد از شکستگی در کمر و چند نقطه، توانسته تا ارتفاع ۷۰۰۰ پایی فرار کند!
🔸
مصاحبه با خلبان ادعایی آمریکا، با تأخیر حدود ۶ ماه منتشر شده است. جدای از داستان عجیب و نسبتا تخیلی در این مصاحبه، انتشار آن در چنین زمانی، می‌تواند دو هدف را برای آمریکا و شخص ترامپ، در پی داشته باشد.
🔹
کلید اول حل مسئله، این است که داستان را از روزهای اوج جنگ ببینیم، نه صرفا روایت نجات. در طول جنگ ۴۰ روزه، ایران جنگنده‌های متعددی از انواع مختلف آن شامل F-15، F-35 و A-10 را هدف قرار داد.
🔸
در ماجرای یکی از هواپیماهای هدف گرفته شده، اخباری مبنی بر سقوط دو خلبان آمریکایی در ایران منتشر شد؛ ایالات‌متحده نیز مدعی بود دو عملیات نجات برای فراری دادن این خلبان‌ها انجام داده که یک مورد آن، به طبس ۲ معروف شد.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 7.7K · <a href="https://t.me/farsna/462135" target="_blank">📅 00:16 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462134">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/15b6db87a3.mp4?token=FxIZUeaQb6la_YCKPF8tVFR_pbHpEccF6QwCSg3svwYZpGsylEvdI6BogjKqCfuVw9FD-k5rdNeen2qJHQT4AcwML0I6a4RcpaPOU7DoOqERhj1rMyomAXz_-owjHo-g_q5NdcgMwVjaXtCaRtW9QyCJ-YvRmDKu0QvWZR4OxFY6Sw2eNVJ9b9p6tuCRsfw80121g5k-sGd5Z-MEIc1aJFwx7yXYp6tt6LGMaW8Z8kQP-t64s6HKODS54JQd-lz98igj7GerMTzWr2VFWAdbzeCLy3jYinQgtC4pwz0tD_gHwFLAKEaYC5ZNzcBbrs_WgY-7lfyS5n9b0aEIC4LMzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/15b6db87a3.mp4?token=FxIZUeaQb6la_YCKPF8tVFR_pbHpEccF6QwCSg3svwYZpGsylEvdI6BogjKqCfuVw9FD-k5rdNeen2qJHQT4AcwML0I6a4RcpaPOU7DoOqERhj1rMyomAXz_-owjHo-g_q5NdcgMwVjaXtCaRtW9QyCJ-YvRmDKu0QvWZR4OxFY6Sw2eNVJ9b9p6tuCRsfw80121g5k-sGd5Z-MEIc1aJFwx7yXYp6tt6LGMaW8Z8kQP-t64s6HKODS54JQd-lz98igj7GerMTzWr2VFWAdbzeCLy3jYinQgtC4pwz0tD_gHwFLAKEaYC5ZNzcBbrs_WgY-7lfyS5n9b0aEIC4LMzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
۱۹۸ شب پرچمداری نیشابوری‌ها
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.73K · <a href="https://t.me/farsna/462134" target="_blank">📅 23:59 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462133">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9938f8719.mp4?token=CQvO-x9PEGTGVyDp2QXrt8L2YABhsTPOxEglSNKd96KSvinmNf97wPLIpdAcQS2JLUkCSLtiG_PKSw1rVF-sIhM5XA7DxFrl3C2klxWNhEzreatUkgICoFB6qgC-NDKutQZqMA4UdH1jDnauhr8aKKugW6cpA-HO1P0e8NLAejr0KWOUKEX_6XVDh7cKNwBt6ihWNmYwz8L8lWEpdGi9NhV81v-MQ00HxbRQa1SApxxoOGVTJf-vhJbW9IFeVkcJARNxuttyeVp0UC6_r2s62KwbGYTVdC8J-1iqhoRSvNnGnm62EwQy1jIlB1fSSAEENkmp6fwiirOWWrb5q0qwZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9938f8719.mp4?token=CQvO-x9PEGTGVyDp2QXrt8L2YABhsTPOxEglSNKd96KSvinmNf97wPLIpdAcQS2JLUkCSLtiG_PKSw1rVF-sIhM5XA7DxFrl3C2klxWNhEzreatUkgICoFB6qgC-NDKutQZqMA4UdH1jDnauhr8aKKugW6cpA-HO1P0e8NLAejr0KWOUKEX_6XVDh7cKNwBt6ihWNmYwz8L8lWEpdGi9NhV81v-MQ00HxbRQa1SApxxoOGVTJf-vhJbW9IFeVkcJARNxuttyeVp0UC6_r2s62KwbGYTVdC8J-1iqhoRSvNnGnm62EwQy1jIlB1fSSAEENkmp6fwiirOWWrb5q0qwZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایتی ناگفته از جنایت آمریکا در سیریک
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.34K · <a href="https://t.me/farsna/462133" target="_blank">📅 23:54 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462132">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VOG3-VBpmVXoVyHSs8XJCMCJ062Ygy8tQOG97nLZtrgRAwtrJiBibbKFM5XHj_L4BoPd0S6zqufPxLesjyW5lqSI52PeWLSEsShKiRCKeU9Vr1uINJIcuM-tPhlWfzELkABIJjdRqJ1Oa-wE0VQlOU8Gi6VAom36O1UkRHTd8ptRkNrU6PL8mwTNht6DLHeF27USQmV_1xP8o7MEDMdoA8RM2eWXNqSMnWoVkOJl5CNC-tQeOXY4LMITDv3dtEYdlj8Ha3mU5AVjmKtORnCvjDdBBXJttQSnvzfZB_met9dDWcG3UeIydjmjQdH5S5iN8TfBtrDkJeI0f_BtvHsGRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">راهنمای بقا در طوفان، چگونه از صاعقه در امان بمانیم؟
🔹
با نزدیک شدن به روزهای پاییزی و افزایش فعالیت‌های رعدوبرقی در آسمان کشور توجه به توصیه‌های ایمنی برای پیشگیری از حوادث ناشی از صاعقه اهمیت بیشتری پیدا می‌کند.
🔹
کارشناسان ایمنی همواره تأکید دارند که با آغاز رعدوبرق، بهترین اقدام ترک سریع فضای باز و پناه‌گرفتن در یک مکان امن و مسقف است.
اگر فردی در فضای باز گرفتار رعدوبرق شود و دسترسی فوری به سرپناه نداشته باشد، باید این ۳ نکته مهم را به خاطر داشته باشد:
🔹
از نقاط مرتفع، تپه‌ها، بلندی‌ها و درختان تک‌افتاده فاصله بگیرید.
🔹
از اشیای فلزی و رسانا مانند دوچرخه و میله‌های فلزی دور شوید.
🔹
اگر موهای بدن‌تان سیخ شد یا صدای وزوز و احساس غیرعادی در اطراف خود داشتید، پاها را کنار هم نگه دارید و تماس بدن با زمین را به حداقل برسانید.
🔹
توصیه می‌شود افراد دست‌کم ۳۰ دقیقه پس از آخرین صدای رعد همچنان در محل امن باقی بمانند و سپس با اطمینان از پایان شرایط خطرناک، محیط را ترک کنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.12K · <a href="https://t.me/farsna/462132" target="_blank">📅 23:50 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462131">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🔴
حمله پهپادی به ۲ قایق صیادی در آب‌های هرمزگان؛ تعدادی از صیادان مفقود شدند
🔹
معاون سیاسی استاندار هرمزگان: شامگاه دوشنبه ۲ فروند قایق صیادی در حوالی بندر کرگان در آب‌های خلیج فارس مورد حمله پهپادی دشمن جنایتکار قرار گرفتند.
🔹
درپی این حمله، تعدادی از صیادان حاضر در این ۲ قایق مفقود شده‌اند و عملیات جست‌وجو و امدادرسانی برای یافتن آنان آغاز شده است.
@Farsna</div>
<div class="tg-footer">👁️ 7.75K · <a href="https://t.me/farsna/462131" target="_blank">📅 23:45 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462130">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nJVqPD6BgLDgpnGcyA1syrk10nLSkJcqOWfrUZYn0TQj8NoEE-cFZS_fYBhuD7Y_UzqYCd4Q4Q67W_GvvmetFf48MTbfXZAIjcaWmJgh7OQ_ixb9Hl9hI25MvKrYJwb4UaTvDMRJ31lV_hMeTE9_yXfAK9PHhSIeZPE1W741cQEj7jR532_xN3AZB3vfXyTeO_GLhkwwPVi-B0QFfdu0auM_z1XjXCPMXIctYpd0OS9gAcB5GtIA9lDIpi21FPYGdzS6ahemkYhZPrUivkKi5CKsrsTxz-44X856k1KZ7dbWYekSLPy0ZfYnjwnVDUiYAPIDedYHx4bU1iWoc_HYVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌
🎥
گل سوم استقلال به السد توسط قلی‌زاده
⚽️
استقلال ایران ۳ - ۰  السد قطر @Farsna</div>
<div class="tg-footer">👁️ 8.27K · <a href="https://t.me/farsna/462130" target="_blank">📅 23:41 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462129">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65187ac504.mp4?token=ICd7x4Obotafep_eO3MdAvNsNXJMSK6ymepf-IfRSWM20BU7TLTz6ToRwUUh4RUo-lGdbd2lYc5nTwbbVZ8nfBLRP-UHEXJ1FfC-BqaD1hmWMXGIYbFhHjZfkgjksahiu_eEQC0tPEVuNvDFS0ljAzgOySWxiJvqYzYJ_u-ZoVlDdigMNdZ6sfVLncQOkZNxLuYlJ8Bhv70QkT1MeBVjygpl09RSp2_cstfYVAsUFMTF5cKHcONKJswooo9oj7X90ROs2PnrBVav3anDL9NhUdIuzMpkQnhh3piDhz1heBAC4vscDB6lvrGsogmeo-Qn7Hntzx9o1lqFFSBlscDIGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65187ac504.mp4?token=ICd7x4Obotafep_eO3MdAvNsNXJMSK6ymepf-IfRSWM20BU7TLTz6ToRwUUh4RUo-lGdbd2lYc5nTwbbVZ8nfBLRP-UHEXJ1FfC-BqaD1hmWMXGIYbFhHjZfkgjksahiu_eEQC0tPEVuNvDFS0ljAzgOySWxiJvqYzYJ_u-ZoVlDdigMNdZ6sfVLncQOkZNxLuYlJ8Bhv70QkT1MeBVjygpl09RSp2_cstfYVAsUFMTF5cKHcONKJswooo9oj7X90ROs2PnrBVav3anDL9NhUdIuzMpkQnhh3piDhz1heBAC4vscDB6lvrGsogmeo-Qn7Hntzx9o1lqFFSBlscDIGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
درخواست جالب حردانی از نیمکت استقلال برای اعتراض به داوری پس‌از دریافت کارت زرد  @Farsna</div>
<div class="tg-footer">👁️ 7.56K · <a href="https://t.me/farsna/462129" target="_blank">📅 23:39 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462128">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a62c00b98b.mp4?token=t3oCClXy4uxybVNjKqf8bq7AmV9lIDVOS91dSp0SkeKYlBH7y01yvJpf7qK6Th4C_rlQdcZkMDdoXaKdPDi8A5_we0ba6bRBxBwUuupW045ac1V9RSv5VVukafNeDhav-zt1Dz5tyJCuz1YyV2jCCI8DOaX8TFITF9dImbodjPyXjzok8xij8NJiKGowU_Tv2KHn4v8hzEd1u5TDit-kWPUSgYu_BCGpDphO9obma2XxFKCzT-K1xplyz9OQJ1UHbcgvMhy2FHtX2uxiIX8br6JrphgtWaX_vnj-zVKbHyVgbKgpR72S4-0JmraOueHgUpb9v_I7nl8wg5Ys7E5vnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a62c00b98b.mp4?token=t3oCClXy4uxybVNjKqf8bq7AmV9lIDVOS91dSp0SkeKYlBH7y01yvJpf7qK6Th4C_rlQdcZkMDdoXaKdPDi8A5_we0ba6bRBxBwUuupW045ac1V9RSv5VVukafNeDhav-zt1Dz5tyJCuz1YyV2jCCI8DOaX8TFITF9dImbodjPyXjzok8xij8NJiKGowU_Tv2KHn4v8hzEd1u5TDit-kWPUSgYu_BCGpDphO9obma2XxFKCzT-K1xplyz9OQJ1UHbcgvMhy2FHtX2uxiIX8br6JrphgtWaX_vnj-zVKbHyVgbKgpR72S4-0JmraOueHgUpb9v_I7nl8wg5Ys7E5vnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تداوم حضور مردم گناباد در شب ۱۹۸
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.68K · <a href="https://t.me/farsna/462128" target="_blank">📅 23:30 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462127">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bTQ0XUKDbOv828Hsm5tYMAzBjuaJRt003jIi2FFu9Haz4lfLnr7thecFqIUPRwduTOqZ-9L8KAs3PILgWPEUW7aWq6cnEY9oR0hfcqcRCslQrxbDH1fyjLox37MAJxLUEg2EHHggLcfcojZMTJBC_UTsDhPj4thHhupo0PaC-VMfqrLcCMd4MsmIrIj1mjzK10MJ6Xp75LvjTRESZG25fKzp0a5WxgCwc09XlFQEBEWNHPBxw-DXez0mWUdCMUWoZWeDKXBjM0emxhTxCKLft0vZpZUIKjDfVKRaYzLVjqPwUMgr7g6CrCOgsff_414wM6NaHpMpoM0MGIrg1_n-jA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تسلط ارتش یمن بر ارتفاعات مشرف بر تنگۀ باب‌المندب
🔹
منابع یمنی امروز از پیشروی میدانی جدید نیروهای انصارالله خبر داده و گفتند این نیروها بر ارتفاعات راهبردی کهبوب مسلط شدند.
🔹
شبکه خبری اسکای‌نیوز به نقل از این منابع گزارش داد ارتفاعات کهبوب بر تنگه باب المندب…</div>
<div class="tg-footer">👁️ 7.72K · <a href="https://t.me/farsna/462127" target="_blank">📅 23:28 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462126">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a5d1d8cf1.mp4?token=LastXynXNKkeiveA6BUtklKFb2CiRRvi5NOjGXKUiXmfNhIRe_FNuPJEMpvGRE7hD4o7kuNR5U0LnnyzWrKeyht1Yx4s8K66cLspe53KnMqLvviN9wkgqvdo1pOGf6djVh_lEnP3Hz1OIMZmXkby1YzBvCiK1BV0AVBYbWdXg4qryjpqPWq9jtt89t92B9YCvcEGUudanysPvI6xr1Q84SCEGPM4Aq3vkUy8YR9Qx-N1mwxoGFVwa3lP20hVKteJfBTDB3Gu-kYsV8ay-imDZtxQL7spOH7rogHmDKtbhEseeH9b3fCcyYPPnZErhmBUpNdvfHPDVGGB5U3AAsJHGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a5d1d8cf1.mp4?token=LastXynXNKkeiveA6BUtklKFb2CiRRvi5NOjGXKUiXmfNhIRe_FNuPJEMpvGRE7hD4o7kuNR5U0LnnyzWrKeyht1Yx4s8K66cLspe53KnMqLvviN9wkgqvdo1pOGf6djVh_lEnP3Hz1OIMZmXkby1YzBvCiK1BV0AVBYbWdXg4qryjpqPWq9jtt89t92B9YCvcEGUudanysPvI6xr1Q84SCEGPM4Aq3vkUy8YR9Qx-N1mwxoGFVwa3lP20hVKteJfBTDB3Gu-kYsV8ay-imDZtxQL7spOH7rogHmDKtbhEseeH9b3fCcyYPPnZErhmBUpNdvfHPDVGGB5U3AAsJHGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌
🎥
گل فیرمینو به استقلال که به دلیل هند مردود اعلام شد  @Farsna</div>
<div class="tg-footer">👁️ 7.37K · <a href="https://t.me/farsna/462126" target="_blank">📅 23:22 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462125">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mZByaiu_AckIfEi9Vahxz4lvs02yhXmMmZYhh42uz0fbd1XLWsiVDqsl2Ce_HRwFsuwKE1OzUl2UX2MFAMpx0YVdUTR9R6oqZdHot8bnm-YUtj-2mgqDCNqrUvQiow3bOAB3iaHJ_3HNi3NXktX0M4hATR5cSOwnBwaJ48rAy8zLDTzteAPXv5V2FwFn3B_LEoaI-OHLd9ZQFvDcLoQyf54-JYQqwj1ZTmaH-FQzKCUwNrAvu8yRxJTZsCXnTA3hH7FS2UKTQPWAR3He4G8VlWooBinXHZjdI9JnjMsAK3ubCU4ntodnwybXgpPwGM1WjeV2PjjIfbIcpaf1elZ0jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کیف و کتاب را خریدید، اما این یکی را فراموش نکنید!
🔹
با نزدیک‌شدن به بازگشایی مدارس، آماده‌کردن کودک فقط به خرید کیف و لوازم مدرسه خلاصه نمی‌شود؛ آمادگی عاطفی، به‌ویژه برای کلاس‌اولی‌ها، اهمیت زیادی دارد.
🔹
درباره مدرسه با کودک صادقانه صحبت کنید و فقط از خوبی‌های آن نگویید؛ دلتنگی و سختی‌های روزهای اول هم طبیعی است.
🔹
مسیر و برنامه روز مدرسه را با او مرور کنید و اگر لازم است، در خانه مدرسه رفتن را تمرین کنید.
🔸
اگر کودک ترسید یا دلتنگ شد، چطور باید با او رفتار کنیم؟
🔗
در
اینجا
بخوانید
@Farsna</div>
<div class="tg-footer">👁️ 7.48K · <a href="https://t.me/farsna/462125" target="_blank">📅 23:20 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462124">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MVJM2J0UxmRl0bL7mGtdoglPQNC5qH6xsATfPyU45asWc6NtpNs-nGuUeSr04YKsPPOi54yr_PMVdobUpnEqh3kvU92afrLH_HqSTLKRo_rEm_c3wWeHapc5diBnJ1J4MVHlYSG1xtF-nophT237ayh86FvGJl67As6tudWBD_CIb4vNxfXqFDc0Bp0h0W1YpGwnc5MpyobpeSzOfpSXRMKgVUfVmsLDnG2zGYTCblP4tkH2gheMhQkqAngd49kIX0A2sS6m05DrMAy8RU_iJivMURpPP9OlAOcd1U8pDmYGTefLw8iqpWAjCgSTJXNelHAtzp5tKXdyk7cqWrmADw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی نیروهای مسلح یمن: جنگنده‌های سعودی را با پدافند فراری دادیم
🔹
یحیی سریع: نیروهای مسلح یمن دقایقی پیش موفق شدند دو جنگندۀ سعودی که از پایگاه‌های خمیس مشیط و طائف برخاسته بودند را در استان صعده رهگیری کنند.
🔹
این جنگنده‌ها با استفاده از موشک‌های پدافندی تولید داخل، هدف قرار گرفتنه و مجبور به عقب‌نشینی و بازگشت شدند.
@Farsna</div>
<div class="tg-footer">👁️ 7.41K · <a href="https://t.me/farsna/462124" target="_blank">📅 23:14 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462123">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/py3zumxgrRkm2uZWRvQyEufVg4s0mXV5TEmOs0an5c9RX2QxLuLWwhU_6FfOHCkrvMxdYx4qGtKX8LZ5e_UwbwyPV2RgrOdTegcGUXVTxvO0lmHT8TOKFxHihWTKB0-homeEnNw_Ji79LNrUzDmcIyrJ1zvlt5yoBm2HhSUEtst7KJgCDNDzxSdPevWQD85sGLKHns84e-_N1mNsyawbiFhC7mg3yvdtvajU0jj4FJ8JukJQCdiaPtgQOwmCyRA1Ar_PX6WNmW9XI7nzj1zFm8NbCN5Nj0MDZeYVRHe4VGqqJ3be1wwcAUtOwEkZ4XbGBXFJLuagcayYS39gxDFLVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اقداماتی که در ایست قلبی می‌تواند جان‌بخش باشد
🔹
در شرایطی که فردی ناگهان بیهوش می‌شود و پاسخ مناسبی به محرک‌ها نمی‌دهد، نخستین اقدام، حفظ آرامش و اطمینان از ایمنی محیط است.
🔹
امدادگر باید پیش از نزدیک‌شدن به مصدوم، از نبود خطر برای خود و فرد حادثه‌دیده اطمینان پیدا کند و سپس ارزیابی اولیه را آغاز کند.
🔹
پس از اطمینان از ایمنی صحنه، هوشیاری مصدوم را بررسی و در صورت پاسخ‌ندادن، فوراً با اورژانس ۱۱۵ تماس بگیرید.
🔹
سپس تنفس و نبض را حداکثر طی ۱۰ ثانیه بررسی کنید و در صورت نبود نبض یا وجود تنفس غیرطبیعی، بدون تأخیر احیا را آغاز کنید.
🔗
چطور عملیات احیا و ماساژ قلبی را انجام دهیم؟
در
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 7.52K · <a href="https://t.me/farsna/462123" target="_blank">📅 23:07 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462116">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P0NmSQeeHTcSVxqyAwBhkaM4-rZk8B_qrwkn34Mjc4p1dRYQCuGOrGnMDWSxdezEn1wzIcbp27Z1iX3-aIA8GrBdmPL9k2AbodR5Fi2uB0REQ4wqsFzDg6rqcnPnZ-KFzu81e9AcvwXCYOZe8XAFCgEqceecAtOm_GHIl-jci3bSJZMIppr7gyh3go-NsNeDgmTb9hNL09EFnxy9EG2GnecKOMlKwhaR875ccDvOLyQeFakUzPfXI_9HuTt4RMfILzxKftNyqGeLe-bVVncTkrYnDQQ-bm04IWb_JzDn-SWfOCgvGWAdoRaowQo_q8bDZjw26RoM6osF4EkGiBX4JQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d-D--Nzpp-XOCvUphJ1wF6UfhmxcK-QRo5LJTJQgCRadYa4vUDPIN19ic3lNinE3oq_WJsHSMylzQOxstncdrWdG31Mlz3aILOJKrDNiPU1SS9euv3rYt33-NLirsd4t6cfQ34Jro9wj9G4vfllsBUEp81ICtoGRM62vbBqV-G1-lsjYMmjRXP1QSkUZOvbtn7VV3Fgok7ItPJYqMfKdIQHXmwU2cRUH_fAkVVAMixSw3INuRxDirVACOC5vHx1fchczicePUXTEriNNPkD7AU31mSYr6tgW280rzoiPgGhtSM9cQUJmCMiiiE5M630CZHheMdYlwwr3aEDTeXV0Yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nzRgQVWveiV6rb6EW6gJVBkmwxqE5-a7DIR8bBZv3uZkwn6qkIX0DQo9QgJ2QF7XMkFKO3qfrkoxJjeYRYMgyLhzxPObMWCAqOdN1QRopJjw9x-9d_KdSV0E_oa4dFrZ7EsMeylNWcgp6w4rTKvdoBjeMll2Ni1cME1j8jCwy-aYDKNBQj50kSIZJ_1TYrDx0Apq4JSC-vAZIb6biTk8vR22c1xNZE-G5N_K_SeFXypxjXIICVumFMm9KhUZCRlzJOjn3lXMopNBYFzHZpcb77q2bL-HN6mDH-pC-7Ngg9ka3d9cy-1kRSY9MJepJvhfRkV_ree5HYShuoVd6_Ap3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HFsl6511J0CFQl35i_Wjn-QNZ-Yyn79F5kD_vtxknX3DKupYkL5ALCYOZcxxt21yt5bdlKbZ25WOQnJUTz8P5htQSWwFx1d19TQSSB2m4u1lWsGli7ArkEoMXiyr-U9OB2QmmlEN3d-1ZNAxBDllxA3438ze7hXdlkRRY6HpquoGys31FSKQ6DyoDN2mvzzSPwNCLO74DIjgVim3b3lhJEmwXYu3KrCbZqoBgBFNPAtUenmvfitgBW3n5iE-mnsztH9H4A7wKx9SzOSIQJIteUrmMdN5E8kqrnW0Jb3-cpSpFJOtLJmCRXKzUwktPxCaPpB9PvuC1ZqbGim-CYrtzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sHkGA_EzTqa0Ec5fDmsyi2VNM9MwaCTpZ339SJ0KASgAgeFX7qXV3iui8Tu3-k0-kV1abPoFJrE4CoG16O486GD6dUhRZto7fZYC7nBncH9__NIFopOwUqgcJRsG6PGBBp4owOuYoenpr0u0pze-yP33n5-H7XRR-8C5n6KlLpAFnM8A9J_IJElmZI8OuPxFyZHPrlHjwhUkFA5ton6mwYcF9I4ONc38pqEwILgloKwath7R2pO7sWYWci9aY9oKsVS9_LuatKaN0Qdggdsuw0lOwhxX73jMO0D4B_oSfj3YSrdYTdoAUjDErvleWPhS-wX_2r1uG4e2mCCHTP9Dnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WCUdy5WJEg-c1MBe3NeMG9NBdN3-Rh6Wt7W57xt0xaNOiK2hN4FV5eV_tD8ytewhab_8pWBimtV2O6ZL6uju5iNygaksINjudZpch9geWf1baT-0CyauJWcx79_3bbC-WuV8HD5ohpZTwzHzq-lA0tR1d_I1QFZNdzyPaVKFAxfY_eCGNXSjNhCT9Py9-U4xwHQ0tm2lRXSbNK2qqkZ528lDtMUctokMQD0lO0dkQuGM4xMHU69OF40b7TfAsCKeJ9cvV4Hhx47G36BkhvcfZQpflSCpkr31Ah0mEiutV93_7p9MeRJED9V6A6p3RBdsUor2ufEpsOUjW1sg92C1Gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mHhrrWRuvgxs460SOFazBP2Ta98zFjXFxdb_rBTu0ZWua__tHC3cGNRkN6DB16Z_1UGB44HGhmVMSnX_5N-x9z0QtQuH3_0KRCy4bFUuXmiOdx7zAZN1lWwer95TsOWLmmQSyJKCz-bRRex9V7fPO1QVRLJpnXKID6lcaOpzrtHXwnEyLAyaD54WW68Ico4EPYvQp96J9-C5XB6VF5WADKZ8496qRNSrWTIbjIwX09zvgDpLK3qu0sibxt4nE7aYe_NUVjhDGL9jiDkgD_7CQRUxA5d3n0bMKnUlh8Q4OJdI8X7SAgLI9kbIAxe0jOJzXzkbAFNeRgu5t4cpJHGQ6A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
قاب‌هایی از حضور رهبر شهید انقلاب در جبهۀ حق علیه باطل در دوران ۸ سال دفاع مقدس
‌
@Farsna</div>
<div class="tg-footer">👁️ 6.87K · <a href="https://t.me/farsna/462116" target="_blank">📅 23:03 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462115">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/519889c5e4.mp4?token=RE_MQ_VgmC5Q4B_xZG2-ZYp_dLUi3zNVU5MMnROyxzlWbMSbvAYKxq1ko6i28CSv3twMKM1fLZfvumLzhJZaeqtKAix3UIz6-Evkm2wAJ2_2eOS588j2ZqIMnOSEL43ffXQ6nJZoYE5EadRzS670PqevHFAjPv1xcJoLwQHawT7C0xRycz6l2yIT6T-7B0vP_64TxDuRUdPki-aeyhV0wupi676ufL5A3DyX20X-DOLcfeSw-XjgtTbMQmxBpXk9EDgd_qrozcV32x14u2OtOnku8Bb8Hh-6EyHn_Pci98k54QVIIWbmYmZW3V8F1xmcur-Pyg2Z5Xzpxm_Go2ykRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/519889c5e4.mp4?token=RE_MQ_VgmC5Q4B_xZG2-ZYp_dLUi3zNVU5MMnROyxzlWbMSbvAYKxq1ko6i28CSv3twMKM1fLZfvumLzhJZaeqtKAix3UIz6-Evkm2wAJ2_2eOS588j2ZqIMnOSEL43ffXQ6nJZoYE5EadRzS670PqevHFAjPv1xcJoLwQHawT7C0xRycz6l2yIT6T-7B0vP_64TxDuRUdPki-aeyhV0wupi676ufL5A3DyX20X-DOLcfeSw-XjgtTbMQmxBpXk9EDgd_qrozcV32x14u2OtOnku8Bb8Hh-6EyHn_Pci98k54QVIIWbmYmZW3V8F1xmcur-Pyg2Z5Xzpxm_Go2ykRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گل دوم استقلال به السد توسط سحرخیزان
⚽️
استقلال ایران ۲ - ۰ السد قطر @Farsna</div>
<div class="tg-footer">👁️ 6.82K · <a href="https://t.me/farsna/462115" target="_blank">📅 23:01 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462114">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5992d64136.mp4?token=bDwNYl30RZ0Shg5nyfi6KaJG-9bIWflB4JbL3EWQ53eOvX8WtrtWtlIPajqZuUvZ-lotu7jOkHOOHlvgSxSjXurNhKZKa031OQrkNpIHdDlAn2hhWIf4puAi6WzJt0pVH8O3EMWfUoOhTtPARPPrvzo3H39f0W3UOkFN09oQ9ed_hlXjhS24235Oggdj31abIQKkjaCBo9s0trfatV8Z2cYl5Er-yU1tGLBhGAIGxZ4bdtZ8VMoiOjC2jvrphmTirsX1yNEu9LzTUR3LmQS-3JmKFKUCfj6uMQUzjlABqrZHzVKp4F-rbFMzabQk2caCm_r0D4wgXrdOdbmwZGCbOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5992d64136.mp4?token=bDwNYl30RZ0Shg5nyfi6KaJG-9bIWflB4JbL3EWQ53eOvX8WtrtWtlIPajqZuUvZ-lotu7jOkHOOHlvgSxSjXurNhKZKa031OQrkNpIHdDlAn2hhWIf4puAi6WzJt0pVH8O3EMWfUoOhTtPARPPrvzo3H39f0W3UOkFN09oQ9ed_hlXjhS24235Oggdj31abIQKkjaCBo9s0trfatV8Z2cYl5Er-yU1tGLBhGAIGxZ4bdtZ8VMoiOjC2jvrphmTirsX1yNEu9LzTUR3LmQS-3JmKFKUCfj6uMQUzjlABqrZHzVKp4F-rbFMzabQk2caCm_r0D4wgXrdOdbmwZGCbOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
۳ قدم مانده تا وعدهٔ دیدار دویستم مردم در میدان اقتدار
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.63K · <a href="https://t.me/farsna/462114" target="_blank">📅 22:55 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462113">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91cf20989c.mp4?token=bNZQwQ0klB4iNjSQgn4GgxXDLZP4eupUEGI7aLOd0yvBpJ0HhSZTx0c8YRH3nPhNHPbUaIfyE4y2YUcGSNEoEJIvVrnKULLRD_noRFCam_XmVLMmWjretQPpa7jwEcvW5HEeeqtqvVJpB2n3XdWfrSZpZHcsl2U18MCKriBrWi5UpUA0SguY7-pSJIlF5pE0uHhuVS63vuSYO7n2KtY4vAf7GslNQl8SMOl2UEEqdpHxYr_JfNpWvMSx1bJ7jAepF97UZf4Y5wJkN5U5vGVwEzrBH8md78kXkL5p0eWX3LJOM9EkCOZagSDiMRE2b4leoRO5fR6aAlDEeaafAMNfBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91cf20989c.mp4?token=bNZQwQ0klB4iNjSQgn4GgxXDLZP4eupUEGI7aLOd0yvBpJ0HhSZTx0c8YRH3nPhNHPbUaIfyE4y2YUcGSNEoEJIvVrnKULLRD_noRFCam_XmVLMmWjretQPpa7jwEcvW5HEeeqtqvVJpB2n3XdWfrSZpZHcsl2U18MCKriBrWi5UpUA0SguY7-pSJIlF5pE0uHhuVS63vuSYO7n2KtY4vAf7GslNQl8SMOl2UEEqdpHxYr_JfNpWvMSx1bJ7jAepF97UZf4Y5wJkN5U5vGVwEzrBH8md78kXkL5p0eWX3LJOM9EkCOZagSDiMRE2b4leoRO5fR6aAlDEeaafAMNfBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: آمادگی داریم در چابهار با هند مشارکت اقتصادی کنیم  @Farsna</div>
<div class="tg-footer">👁️ 7.83K · <a href="https://t.me/farsna/462113" target="_blank">📅 22:54 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462112">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26fb118626.mp4?token=qMG8j8BUl6TZ_lar8M5bc04n-hJWBhDX4ZpJephQaOr2HnxDrSFrbKE7efx5sNVEV33NPRzIhata8-FizR-0uzZSQ_YC1PHi_Tw7fuHEvXI8c_ZSQlZASOXeK6tzO8kF-tZ5Cnmpg02yYN6R7DhW4pjHjRAIaQ4gFVwevEW-_E1qF9sI-nPZmWEGVNqf4dO2_-Ko1Vsw6tBYecYexU0VNc1WFLc9zJkayOx1COKPkO0PuC4vm3ImqL0f8IpbjYnsUqXIbDkhuvKXANRn0AarEhq6x3JMPq_JXfIi5InSykhiwssfQ6Z-eTBn8P4tgA5vqdLv2_sUQOjPM-mhKHD3Lw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26fb118626.mp4?token=qMG8j8BUl6TZ_lar8M5bc04n-hJWBhDX4ZpJephQaOr2HnxDrSFrbKE7efx5sNVEV33NPRzIhata8-FizR-0uzZSQ_YC1PHi_Tw7fuHEvXI8c_ZSQlZASOXeK6tzO8kF-tZ5Cnmpg02yYN6R7DhW4pjHjRAIaQ4gFVwevEW-_E1qF9sI-nPZmWEGVNqf4dO2_-Ko1Vsw6tBYecYexU0VNc1WFLc9zJkayOx1COKPkO0PuC4vm3ImqL0f8IpbjYnsUqXIbDkhuvKXANRn0AarEhq6x3JMPq_JXfIi5InSykhiwssfQ6Z-eTBn8P4tgA5vqdLv2_sUQOjPM-mhKHD3Lw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
موقعیت خوب برای استقلال که سحرخیزان توپ را به بیرون زد  @Farsna</div>
<div class="tg-footer">👁️ 7.41K · <a href="https://t.me/farsna/462112" target="_blank">📅 22:52 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462111">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/980fe41e1d.mp4?token=aACrFqoFSAjjZHAFLAkUIrPRhVek7bGW_pwRecGVBxBH_5Gk1LBpSblfr5Vx76HYhnaHy7wMCdCehOLqYFXIBS0zvgtzrKf3J7IIffA4rGNjecisR9UMfaU-aqNo_wlFRnGYqR-G3M62AgUPAQkvk5-0QY3kypkJ3QNKH0mrzcqigPddqbpejCMRzMD0bvJ06G9-W9fJyGmhtcJBKdljzBDJye5jH8vsHBtIkb54Bx8eSNuY8klj8c4AMWxqC7bPNEcs4hUdfSS3QcxCI-0ADDi4zdrXt5ioockRAKYqI3gOkHPGPHJLAh7u9sHbO9zdOnzqC4ncjW0ewpdiVbXPGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/980fe41e1d.mp4?token=aACrFqoFSAjjZHAFLAkUIrPRhVek7bGW_pwRecGVBxBH_5Gk1LBpSblfr5Vx76HYhnaHy7wMCdCehOLqYFXIBS0zvgtzrKf3J7IIffA4rGNjecisR9UMfaU-aqNo_wlFRnGYqR-G3M62AgUPAQkvk5-0QY3kypkJ3QNKH0mrzcqigPddqbpejCMRzMD0bvJ06G9-W9fJyGmhtcJBKdljzBDJye5jH8vsHBtIkb54Bx8eSNuY8klj8c4AMWxqC7bPNEcs4hUdfSS3QcxCI-0ADDi4zdrXt5ioockRAKYqI3gOkHPGPHJLAh7u9sHbO9zdOnzqC4ncjW0ewpdiVbXPGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: نه حزب‌الله، نه حماس و نه ما آغازگر جنگ با آمریکا و اسرائیل نبودیم
🔹
با محاصره و تحریم نمی‌توانند ایران را وادار به تسلیم کنند. @Farsna</div>
<div class="tg-footer">👁️ 7.41K · <a href="https://t.me/farsna/462111" target="_blank">📅 22:48 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462110">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E4yH7oGCvPgzsi2RIG5GMxDVrzyD6yyLdGIUsuAvMiaXMXCIj7B10pL33Upzm2rB5-aP2l6BQK8IEFogs8BOz5NqSiIccGmobIjzo6F-IUBlx__y3R1_WwYPZdaIRSv4aOWlQ_OP8CA_RSDML2TFaL8o9eN1o6R1vSLNRdf-VvB_Mv27bkOrgEKGNr3d-07ABzYU9JO4ZnKMezMV397EENWuLlCmWaqym7Wnfl-weluu9Cdke0ZfxWbe0sgzWP6V_3hqyGI5m06y-23pvrAUJz0VT4ioLxB9_0O6dDn9cV083yNsGnx8GBfSzw7UIco5yBsL5WxkdlKvo2LPEYUs6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عربستان در تنگنای یمن؛ گزینه‌های اندک، هزینه‌های سنگین
🔹
شبکه خبری سی‌ان‌ان: این هفته، جنبش انصارالله جزیرهٔ راهبردی پریم در دهانهٔ دریای سرخ را به همراه شهر بندری موکا تصرف کردند و به دنبال کنترل تنگهٔ باب‌المندب، یکی از مسیرهای کلیدی انرژی جهان، هستند. …</div>
<div class="tg-footer">👁️ 7.14K · <a href="https://t.me/farsna/462110" target="_blank">📅 22:46 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462109">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6dce738851.mp4?token=gm8yul8LnFMBFWPVTtiK8Bj3xDuhPoaItjkGDRDZagYwDEnnIVuPmhG4wsVCz09qyvJpJfOruFQmAb-IiyHFWWr1RuFrILvXsVNu1C6E0W_U1UJfhhlXShV--SKDelw-UVnnYyx0cVwNDL7HuMllunHC1Jg2VswMUCss3NZy2M2ro4XakcptH-9doXdf4Fws3rqLckTIp1wWPQMTbzsOr_y-zn918DZILt42QhVyI6s_amjV0qjEABilxfm-869IYWRww-5KwUvMxNw1oFZZDn8eB2GTqM1IDt2lPIj6DeCSI9E8ewtnoea0sRuuM2LiwiwxotwfeLPQcDoF6DrCWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6dce738851.mp4?token=gm8yul8LnFMBFWPVTtiK8Bj3xDuhPoaItjkGDRDZagYwDEnnIVuPmhG4wsVCz09qyvJpJfOruFQmAb-IiyHFWWr1RuFrILvXsVNu1C6E0W_U1UJfhhlXShV--SKDelw-UVnnYyx0cVwNDL7HuMllunHC1Jg2VswMUCss3NZy2M2ro4XakcptH-9doXdf4Fws3rqLckTIp1wWPQMTbzsOr_y-zn918DZILt42QhVyI6s_amjV0qjEABilxfm-869IYWRww-5KwUvMxNw1oFZZDn8eB2GTqM1IDt2lPIj6DeCSI9E8ewtnoea0sRuuM2LiwiwxotwfeLPQcDoF6DrCWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: دلخوری کشورهای منطقه از حملات ما به آنها غیرمنطقی است
🔹
آن‌ها اجازه دادند دشمن از خاکشان به ما حمله کند و مردم بی‌گناه ما را شهید کند آنوقت توقع دارند ما واکنشی نداشته باشیم؟ @Farsna</div>
<div class="tg-footer">👁️ 6.21K · <a href="https://t.me/farsna/462109" target="_blank">📅 22:45 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462108">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🔴
خبرگزاری لبنان: ارتش رژیم صهیونیستی یک مدرسه در شهرک کفرتبنیت در جنوب لبنان را تخریب کرد.
@Farsna</div>
<div class="tg-footer">👁️ 6.24K · <a href="https://t.me/farsna/462108" target="_blank">📅 22:44 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462107">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47f45f42be.mp4?token=b2BME40WcHeRA98mqOQLAHe8dSQG36gcHIWSfchWJzYGeOIL_jG9xzpUEq51gino4zeFssEjLz0asgbukwc95mS9vbrMiLdlMC68Pw0yagLYe7hPmOmXtYmkGTwacNMNJBqP-gpcPtRTv5T5clm3dhGp5_6X4iDLtc1Rbc4jKebkPF_sgi1XAsVbqnSPLmv91XW0al1kCCiR0Nvbo2fXE_4Ww9d56Qgl-TzIOGrscpFn0BTP_pQYdCyYwimdal3DIJlfc4HzWP52sJx2gTqCOvDUvV4mXhQuQoUHsWKrq98W0WqzdkVdJQaEkBek0FGaurNEoTge8ntIlFyklGUevA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47f45f42be.mp4?token=b2BME40WcHeRA98mqOQLAHe8dSQG36gcHIWSfchWJzYGeOIL_jG9xzpUEq51gino4zeFssEjLz0asgbukwc95mS9vbrMiLdlMC68Pw0yagLYe7hPmOmXtYmkGTwacNMNJBqP-gpcPtRTv5T5clm3dhGp5_6X4iDLtc1Rbc4jKebkPF_sgi1XAsVbqnSPLmv91XW0al1kCCiR0Nvbo2fXE_4Ww9d56Qgl-TzIOGrscpFn0BTP_pQYdCyYwimdal3DIJlfc4HzWP52sJx2gTqCOvDUvV4mXhQuQoUHsWKrq98W0WqzdkVdJQaEkBek0FGaurNEoTge8ntIlFyklGUevA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: رهبر شهید در قلب مردم ایران بود و برای ما سخت است که با آمریکا تفاهم کنیم
🔹
آن‌ها از اول انقلاب به دنبال سرنگونی ما بودند و باید اعتماد ما را جلب کنند. @Farsna</div>
<div class="tg-footer">👁️ 7.17K · <a href="https://t.me/farsna/462107" target="_blank">📅 22:44 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462106">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37ef922ebc.mp4?token=jESy7qMix299Q5ayal3iqDOnXvtQsZ0eVVFveuEFejeBDE9NTvQkoEvnBVvY4oUPq7r9b6bN9txu-R9-MAVDHxDoMhScAhkEW1buH28G586xAXFU13RYSLzptSWUyioIqQAZPWAfXSxMGAUC_l3_TmtCWi0uehgtNw9uV9WhYvxSDzC3W5aeJSOdYsnjviAXBrk5qTVXpeDLxqhQwRbpjO04PjYOwACYagH7lC1ESppe4WZJil-3j48cgbNRh06QR7e7DeVpDYWY8eT6RXWPeVPi6HrXe0opBcdEIynC3nt_iuTkezESgkTsSgFGYr2NalzEN5oGZF3sBUD89cboaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37ef922ebc.mp4?token=jESy7qMix299Q5ayal3iqDOnXvtQsZ0eVVFveuEFejeBDE9NTvQkoEvnBVvY4oUPq7r9b6bN9txu-R9-MAVDHxDoMhScAhkEW1buH28G586xAXFU13RYSLzptSWUyioIqQAZPWAfXSxMGAUC_l3_TmtCWi0uehgtNw9uV9WhYvxSDzC3W5aeJSOdYsnjviAXBrk5qTVXpeDLxqhQwRbpjO04PjYOwACYagH7lC1ESppe4WZJil-3j48cgbNRh06QR7e7DeVpDYWY8eT6RXWPeVPi6HrXe0opBcdEIynC3nt_iuTkezESgkTsSgFGYr2NalzEN5oGZF3sBUD89cboaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: آمریکا چون نمی‌تواند رهبر ما را پیدا کند، درباره سلامتی او شایعه می‌سازد
🔹
رهبر انقلاب در سلامت کامل هستند و تصمیم آخر را ایشان می‌گیرند. @Farsna</div>
<div class="tg-footer">👁️ 6.88K · <a href="https://t.me/farsna/462106" target="_blank">📅 22:42 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462105">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0aea3f8962.mp4?token=k6Pho_yOsyuTvXxQdJ7jTgARpHXxv_HyQfkN3ltUMvkr-HjC2-4SR2lZNA7J2Jep08Q3s1KFSbIwLsSt49WnBFRAH3c0FeIjgpbfV-P5fi0L-0pL9vfbUEv2FTGwDZffyAEgy_E_PkCEOrsYwtRSVVBEMSbhNyZ678BFyH0Rsg_BO2nN39Wom9VoP-Mtn2mYelsBeGLZtVi6RJhGXJDE26UFR0cLiavUMmKYVdkPf99WcrngXPo29MuMhzqXjpyqA5J0c6eqHE5v09oNHBcPXsH3epWlnMxdlt1C80vFczHqB63y_LoHJb8nzhvf9qBzu-fulSEH_Lmc0oxcbCnw-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0aea3f8962.mp4?token=k6Pho_yOsyuTvXxQdJ7jTgARpHXxv_HyQfkN3ltUMvkr-HjC2-4SR2lZNA7J2Jep08Q3s1KFSbIwLsSt49WnBFRAH3c0FeIjgpbfV-P5fi0L-0pL9vfbUEv2FTGwDZffyAEgy_E_PkCEOrsYwtRSVVBEMSbhNyZ678BFyH0Rsg_BO2nN39Wom9VoP-Mtn2mYelsBeGLZtVi6RJhGXJDE26UFR0cLiavUMmKYVdkPf99WcrngXPo29MuMhzqXjpyqA5J0c6eqHE5v09oNHBcPXsH3epWlnMxdlt1C80vFczHqB63y_LoHJb8nzhvf9qBzu-fulSEH_Lmc0oxcbCnw-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: تفاهم‌نامه ایران و آمریکا چه مشکلی دارد که بخواهیم دوباره مذاکره کنیم؟
🔹
خواسته‌های ما همان خواسته‌های قبلی است. @Farsna</div>
<div class="tg-footer">👁️ 7.33K · <a href="https://t.me/farsna/462105" target="_blank">📅 22:41 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462104">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c779575c9.mp4?token=E7wAP0yvEgk8AXFmKKYhevrE6Qy8NQU4fFMg5j7DRHUoUP2CVPds4We1TdQRi2n8yDoBY9rb_QdW5vPyXPcW6Pf6og4Hb5FnMpunMA9qquBf7DmS78LiwM3ZaF3Y3Fk-UAcXjK4vPn0Dlu6YeXysADldi0hhJTO6xvMti7GlhtiPcy6Nu4uD0XSWDrCPTkhZDvos0TNMuV2m9vSLpPMfjAlicyAU6ZF3dmwS6ztrp_S77Nx1NZLla_45EoLwsIUsL_4RumChFIhtFWkA5ZGQ5LEP5_MTUc9AOzv20cqa3iVE5SrNAfqDYh1xy-klfxaN7Mr_tJvyAdT0WRwnH62-wQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c779575c9.mp4?token=E7wAP0yvEgk8AXFmKKYhevrE6Qy8NQU4fFMg5j7DRHUoUP2CVPds4We1TdQRi2n8yDoBY9rb_QdW5vPyXPcW6Pf6og4Hb5FnMpunMA9qquBf7DmS78LiwM3ZaF3Y3Fk-UAcXjK4vPn0Dlu6YeXysADldi0hhJTO6xvMti7GlhtiPcy6Nu4uD0XSWDrCPTkhZDvos0TNMuV2m9vSLpPMfjAlicyAU6ZF3dmwS6ztrp_S77Nx1NZLla_45EoLwsIUsL_4RumChFIhtFWkA5ZGQ5LEP5_MTUc9AOzv20cqa3iVE5SrNAfqDYh1xy-klfxaN7Mr_tJvyAdT0WRwnH62-wQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: چگونه می‌توانیم با آمریکا مذاکره کنیم، در حالی که آنها هیچ وقت به تعهدات خود پایبند نبودند؟!  @Farsna</div>
<div class="tg-footer">👁️ 6.97K · <a href="https://t.me/farsna/462104" target="_blank">📅 22:41 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462103">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea280d0891.mp4?token=GKtK-froIqPe7d4P29BGAtxY8stxdjL9EAlik5XQExwaj-vP4bOU4ybpU53u8kyzqdaor3ejqIkxEZtppS342m6ZpMkECZxqhYWlcqUFcznHC_bAwKzVgs0WUtQMmrV_dbp44Znj9VblsDAaQ92xM5EgE4sl0SePq1-InchoRFxweDl9d_UtVTr6JqIOnvQr3xVIMP9YxRqFQ9MP3Jt4Bn7KloCk_yXAZKFwXZQ9Gf_cP6kwT0dbOKkMHzSkSvoEV-dOpnc3C8yKA8xLXjsjWuafSKE4WpJPrETJtYBxAnpwETgij2SYvmM6kR7wXiznTbE4mnOnExAeXCgILAI9Zw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea280d0891.mp4?token=GKtK-froIqPe7d4P29BGAtxY8stxdjL9EAlik5XQExwaj-vP4bOU4ybpU53u8kyzqdaor3ejqIkxEZtppS342m6ZpMkECZxqhYWlcqUFcznHC_bAwKzVgs0WUtQMmrV_dbp44Znj9VblsDAaQ92xM5EgE4sl0SePq1-InchoRFxweDl9d_UtVTr6JqIOnvQr3xVIMP9YxRqFQ9MP3Jt4Bn7KloCk_yXAZKFwXZQ9Gf_cP6kwT0dbOKkMHzSkSvoEV-dOpnc3C8yKA8xLXjsjWuafSKE4WpJPrETJtYBxAnpwETgij2SYvmM6kR7wXiznTbE4mnOnExAeXCgILAI9Zw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: اینکه ایران دنبال سلاح هسته‌ای است، مثل بقیه ادعاهای آمریکا دروغ است
🔹
این ادعاها بهانه‌ای برای حمله به ایران است؛ رهبر شهید ما بارها اعلام کرده بود که ما دنبال سلاح هسته‌ای نیستیم. @Farsna</div>
<div class="tg-footer">👁️ 6.56K · <a href="https://t.me/farsna/462103" target="_blank">📅 22:38 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462102">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c02f54044.mp4?token=DvCIUVg8CUy81UPHjjJaLvzSQ0bpgrhA2bz0pOKLZU0XsdDcOlyAb5-GQg1dSmxoEWpyKmmCjd51MV7ZV6B8S1cMCTevrY6iqnb4S3f9aRZ45oOkcFA8PgYmVhp3pRGZj-FdwUJJZ94MB43Kn4VLrkj6us5xLxZK0aQsn8v5UppbPsznfRg7Y6_I-c4423Ds1t8j79hRERkYNPCSg6DFzSMObWcHmSoxOzSiEpkxM7vubcApDTQOBrswZDx14xezaUVBxlyHKLvav4IV3R25u2B5tZZ_dIsPZPSXwIUHug4yHNHZ8z0zyYqxJtR3yfJD3j9YWovPBIww32Y3n3YgHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c02f54044.mp4?token=DvCIUVg8CUy81UPHjjJaLvzSQ0bpgrhA2bz0pOKLZU0XsdDcOlyAb5-GQg1dSmxoEWpyKmmCjd51MV7ZV6B8S1cMCTevrY6iqnb4S3f9aRZ45oOkcFA8PgYmVhp3pRGZj-FdwUJJZ94MB43Kn4VLrkj6us5xLxZK0aQsn8v5UppbPsznfRg7Y6_I-c4423Ds1t8j79hRERkYNPCSg6DFzSMObWcHmSoxOzSiEpkxM7vubcApDTQOBrswZDx14xezaUVBxlyHKLvav4IV3R25u2B5tZZ_dIsPZPSXwIUHug4yHNHZ8z0zyYqxJtR3yfJD3j9YWovPBIww32Y3n3YgHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: مردم ما بعد از حملۀ آمریکا به ایران متحدتر شدند
🔹
مردم منطقه از آمریکا متنفرتر شدند. @Farsna</div>
<div class="tg-footer">👁️ 6.48K · <a href="https://t.me/farsna/462102" target="_blank">📅 22:38 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462101">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57740b849d.mp4?token=hEw3rZw3mmMFMq6hHQTGHwA7i0tSpNsQXpq0OKqVIdshAD_rK4xyfusflOYsyXCSNqnsliFyc8fTgu9XuSufY3D7ti2iwC9agoW7JcXvaEal0P19ralFJPdoOX5x7oRnQTAjxQIjN7MsHyuFAKL8Xi4fysU8YXEAYapyXxeufLabizf8RmFtTTBBfCXZVsup7c9S0qsAYj7reua1mu6Qxjiu6zPIiI_5O1rfvoPXYNarKJgcuO_RdFkOLiBD-8dGIfPiGAqkPIJuMoxskRAjvVhAHoGoPclPM1Bi_UBnBc42LV3AIU9RdTcPXPXboE_5IotJyv0dpxl69p2v1-xy-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57740b849d.mp4?token=hEw3rZw3mmMFMq6hHQTGHwA7i0tSpNsQXpq0OKqVIdshAD_rK4xyfusflOYsyXCSNqnsliFyc8fTgu9XuSufY3D7ti2iwC9agoW7JcXvaEal0P19ralFJPdoOX5x7oRnQTAjxQIjN7MsHyuFAKL8Xi4fysU8YXEAYapyXxeufLabizf8RmFtTTBBfCXZVsup7c9S0qsAYj7reua1mu6Qxjiu6zPIiI_5O1rfvoPXYNarKJgcuO_RdFkOLiBD-8dGIfPiGAqkPIJuMoxskRAjvVhAHoGoPclPM1Bi_UBnBc42LV3AIU9RdTcPXPXboE_5IotJyv0dpxl69p2v1-xy-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: ما با کشورهای منطقه مشکل نداریم بلکه با پایگاه‌های آمریکا مشکل داریم
🔹
آمریکا هم پول نفت را می‌گیرد و هم کشورها را به جان هم می‌اندازد. @Farsna</div>
<div class="tg-footer">👁️ 6.8K · <a href="https://t.me/farsna/462101" target="_blank">📅 22:36 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462100">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/028c0dfdbc.mp4?token=HsVyr6LlgOs_B-B_NujYjxPMOtisvoyb638SW-99ZvDWlFjhKbkzz7sfzNpwMk49mIaGMU4DZp3bHs-crrAfuKQ3I6Av70TL_1Dta0auN9Pe7Dm-lj7P5L9Hy_nsVHBAgWGtGOclAtq0DPeVv3ONSS6dACCOe65qYBDCSW54QHb7XRba343C370dzNnZVevbuteEW8CT0SXz2Mzoi_TMI_vQLrjKCqGS9BV9NzaSRGyFSOAMmb0E0svVeSqcuEQKiaBrGTUD24n60xeDnK5WzEi4-cIeSBwQbJ-HkPf_iceHmSNsR7fb0BxaUv9hEKNqurVu29FYJ4vD_zNll12SDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/028c0dfdbc.mp4?token=HsVyr6LlgOs_B-B_NujYjxPMOtisvoyb638SW-99ZvDWlFjhKbkzz7sfzNpwMk49mIaGMU4DZp3bHs-crrAfuKQ3I6Av70TL_1Dta0auN9Pe7Dm-lj7P5L9Hy_nsVHBAgWGtGOclAtq0DPeVv3ONSS6dACCOe65qYBDCSW54QHb7XRba343C370dzNnZVevbuteEW8CT0SXz2Mzoi_TMI_vQLrjKCqGS9BV9NzaSRGyFSOAMmb0E0svVeSqcuEQKiaBrGTUD24n60xeDnK5WzEi4-cIeSBwQbJ-HkPf_iceHmSNsR7fb0BxaUv9hEKNqurVu29FYJ4vD_zNll12SDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: ارتباط ما با نخست‌وزیر هند روزبه‌روز بهتر می‌شود
🔹
در تلاشیم بر پایه فرهنگ و رابطه دیرینۀ ۲ کشور، مقابل تمامیت‌خواهی بایستیم. @Farsna</div>
<div class="tg-footer">👁️ 7.17K · <a href="https://t.me/farsna/462100" target="_blank">📅 22:34 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462099">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01bebc1764.mp4?token=PNUEiFTam6cgF-q__6wnAAZjFu1UupqVzTFZDj290YhZwXLCF-iezco5GPAJS_rmp_wSQzuoAdpYgnv59KfobvdUBrLIso7kP1MeLM4KL-A51PuX_aprnWZDEwhnGcIjy9GJIDVvlXdrUA9bwboSt8lJcWBtlxAqYGHkqyyfjSDwNEFs06n6K7vT44RcSEyvC3SW_KnGUUKs3S3t0JDCxF5b9qrPLC2dl6WIIMXuOBRfDJgYstgXAqgq3_xIWIJkQSv_xgQS3R8RJIR3o8EcvLoswHhLPYuyKP8ws_fZw77wh6uitebvw6_NCXIwjeLNVnFv0mVWsyePo49b9rddRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01bebc1764.mp4?token=PNUEiFTam6cgF-q__6wnAAZjFu1UupqVzTFZDj290YhZwXLCF-iezco5GPAJS_rmp_wSQzuoAdpYgnv59KfobvdUBrLIso7kP1MeLM4KL-A51PuX_aprnWZDEwhnGcIjy9GJIDVvlXdrUA9bwboSt8lJcWBtlxAqYGHkqyyfjSDwNEFs06n6K7vT44RcSEyvC3SW_KnGUUKs3S3t0JDCxF5b9qrPLC2dl6WIIMXuOBRfDJgYstgXAqgq3_xIWIJkQSv_xgQS3R8RJIR3o8EcvLoswHhLPYuyKP8ws_fZw77wh6uitebvw6_NCXIwjeLNVnFv0mVWsyePo49b9rddRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: آمریکا با ادعای حقوق بشر پس از شکست نظامی و زدن زیرساخت‌ها، راه ورود دارو و غذا به ایران را بسته است
@Farsna</div>
<div class="tg-footer">👁️ 6.86K · <a href="https://t.me/farsna/462099" target="_blank">📅 22:33 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462098">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb959d3636.mp4?token=INoTX3WVGKTEAyIX1-E7NRlVeZXB6ZfGHjSE8Io2dhqqhMCNbfZiJO0UkRFm6SnKlmy22Tgm9S8DnZaf8ChVc0PpkGtsGAzNXuIdR6Q02ZM6NwTBgZ7AXuHRWXgGNrWr-Cr4D_wCWcScrjjL-YYcmzGXakXayaIV1tZNt2249RQb4f-jZITWu0CA0aU5mIPFeDNo1EBeXNLiFDF9igz2SbMggQR2TjDW6TPApDRI1A9VGWHEceWpORIzn0dTZe5ln2NCDxxNfD_HWom0EAhqjs5cfi1pS_2jftwE_M8ll7qDgLN8lrU6OnUYsuxtJABlb6nEvepGZ5PTK2orkJFGqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb959d3636.mp4?token=INoTX3WVGKTEAyIX1-E7NRlVeZXB6ZfGHjSE8Io2dhqqhMCNbfZiJO0UkRFm6SnKlmy22Tgm9S8DnZaf8ChVc0PpkGtsGAzNXuIdR6Q02ZM6NwTBgZ7AXuHRWXgGNrWr-Cr4D_wCWcScrjjL-YYcmzGXakXayaIV1tZNt2249RQb4f-jZITWu0CA0aU5mIPFeDNo1EBeXNLiFDF9igz2SbMggQR2TjDW6TPApDRI1A9VGWHEceWpORIzn0dTZe5ln2NCDxxNfD_HWom0EAhqjs5cfi1pS_2jftwE_M8ll7qDgLN8lrU6OnUYsuxtJABlb6nEvepGZ5PTK2orkJFGqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شوت دیدنی رزاقی‌نیا با واکنش دروازه‌بان السد راهی کرنر شد  @Farsna</div>
<div class="tg-footer">👁️ 6.79K · <a href="https://t.me/farsna/462098" target="_blank">📅 22:31 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462097">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc6f43ecde.mp4?token=FUt7arLwc2eZPz6JdWiLkUhx0fnw75TDSTcBmWuVXLhaptIIrNv49dMi3Mbjw1Ju7sPEHkNNWmr53iWZh5bFD8BM1tvwxjUgje_4GX3VYck6E3_cCaN8ZthvAa9X6BuRYXsZ7EVpjA_Y9ekaYbYM6S8shfDVs3-eXxCkeu9XwXmJKfMZXgqy2x-4KtIEdIkwBeTH9Mw9FVucg2CE1CcssWOpgRboCh_Yz-xWDmN5d11brbfcMRcdZ-qB5bKJ3ZdwrZeSXM_Hibm_zTgsAfTNEE9kENi-WIkDCHOTPDRby1NUJAAI-RMO1SOvNQqpxUPPF0NNl7dVl4TOTIqxwjK51TzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc6f43ecde.mp4?token=FUt7arLwc2eZPz6JdWiLkUhx0fnw75TDSTcBmWuVXLhaptIIrNv49dMi3Mbjw1Ju7sPEHkNNWmr53iWZh5bFD8BM1tvwxjUgje_4GX3VYck6E3_cCaN8ZthvAa9X6BuRYXsZ7EVpjA_Y9ekaYbYM6S8shfDVs3-eXxCkeu9XwXmJKfMZXgqy2x-4KtIEdIkwBeTH9Mw9FVucg2CE1CcssWOpgRboCh_Yz-xWDmN5d11brbfcMRcdZ-qB5bKJ3ZdwrZeSXM_Hibm_zTgsAfTNEE9kENi-WIkDCHOTPDRby1NUJAAI-RMO1SOvNQqpxUPPF0NNl7dVl4TOTIqxwjK51TzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شگفتی شبکه دولتی فرانسه از سیل مردمی ثبت‌نام کننده در پویش جان‌فدا
🔹
شبکه دولتی فرانسه اعلام کرد هر روز که می‌گذرد مردم ایران نسبت به آمریکا و اسرائیل بیشتر منزجر و حول حاکمیت بسیج می‌شوند؛ گواه آن آمار بیش از ۱۴ میلیونی پویش «جان‌فدا» است.
🔹
پویش جانفدا در پایان کار خود به بیش از ۳۰ میلیون داوطلب رسید.
@Farsna</div>
<div class="tg-footer">👁️ 6.93K · <a href="https://t.me/farsna/462097" target="_blank">📅 22:30 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462096">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6277c9b4b5.mp4?token=mzkEnaI8oOfYf5N5hfPnu4a8KYFq-kiYGAiWpTdjvTCgm8-uw2c-vzGN8coZoc1RDQHS86Ettr_kaHqvG6bgUY3bCfEQR0n5wpa0s0P61bDYx7SDgkBHDK2gGETyDw9lUK5lDs6B0XJywYRhGd0f0b67aT-d8EBh5NmLHSKG8AfrFyQBmQ8tmNh_T7vyUDUR1sh5NhwmsdnMUr6k1sIuk9KXTrdv56Z04eAHn_DyKG4P2t2xBx_8WMPx12Ygb-vrEpEZs77JmuGb2OYbYB34wUACC737v4sqLgEW0X-KCUlkaIz8PfpPIk1w9rjJCNKhLJipT-Qw4WpXxFWABb--PA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6277c9b4b5.mp4?token=mzkEnaI8oOfYf5N5hfPnu4a8KYFq-kiYGAiWpTdjvTCgm8-uw2c-vzGN8coZoc1RDQHS86Ettr_kaHqvG6bgUY3bCfEQR0n5wpa0s0P61bDYx7SDgkBHDK2gGETyDw9lUK5lDs6B0XJywYRhGd0f0b67aT-d8EBh5NmLHSKG8AfrFyQBmQ8tmNh_T7vyUDUR1sh5NhwmsdnMUr6k1sIuk9KXTrdv56Z04eAHn_DyKG4P2t2xBx_8WMPx12Ygb-vrEpEZs77JmuGb2OYbYB34wUACC737v4sqLgEW0X-KCUlkaIz8PfpPIk1w9rjJCNKhLJipT-Qw4WpXxFWABb--PA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تماشاگران استقلال در بصرۀ عراق بی‌وقفه تیم خود را تشویق می‌‌کنند  @Farsna</div>
<div class="tg-footer">👁️ 6.51K · <a href="https://t.me/farsna/462096" target="_blank">📅 22:29 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462095">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZASH96lO8HtUNvTyXbZhjMqAUbu0Pj0V5Cuh_AsAKv3RD4cMqUrPNBV6-Y9tfvDVO8qZ4RwZWXlV-IK_nrIWCYcJ-aH01qYwsw55p_qHLdvwRBwAAfKs2qPms_uqtxipc01KKVp0W8amxf8CRXkMtZGLWiStaAEoU9crL9ikYQl_nPkyQJG-RP38aXvxS8T1T7sqxZFIX40pUqxYmJUT1Us5T_Ged_-CCnFeHgsu9jSwKXhgiN3QGQdEk2J5QkyD8qKOUPJgKVVNbNMH4jFec7vSkxhLif4bIod8zVoSXH3iYd_MmNMMoMspep0XoRguuZslDdIT4FdagTqTJ1Otng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
برخورد یک سوپرنفتکش متخلف به مین‌های ایرانی تنگۀ هرمز
🔹
نیروی دریایی سپاه: سوپر نفتکش «الگایا» به شماره دریانوردی 9325336 که قصد عبور از منطقۀ ممنوعه در جنوب تنگه هرمز را داشت، بر اثر برخورد با مین‌های دریایی منفجر شد؛ تلاش برای مهار آتش بی نتیجه بوده و کل نفتکش در شعله‌های آتش گرفتار شده است.
🔹
پیش از این نسبت به خطرناک بودن معبر غیر قانونی هشدار داده شده بود، نیروی دریایی سپاه با قاطعیت اعلام می کند تنگه هرمز مسدود و همچنان تحت کنترل هوشمند ما می باشد.
@Farsna</div>
<div class="tg-footer">👁️ 7.39K · <a href="https://t.me/farsna/462095" target="_blank">📅 22:24 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462094">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cca582c11a.mp4?token=HywflNyg-P8x9AhWr0cifm2GbG0fWsh1swdkx7heQi4WxQz2geXt9af4NQ93KkXsGH_gDJjNOC6ClGvk8xCmtRMpRWjDsc-ipcekOyIqEHCSmuOc1KoRNIqugpV44LdXxIPelzry1OuZxvN8iMPHSlPirzhjmbUoWGIHZ-WX12iU9cfXVlyRMzeQS8elW12HzvlcB69y25OO9r37n_Pa3MUkPc82g4YfFb49p5SFbUjfIwhuyiNyzdAOAi1YNM-3_7p1Lb3_wflZCQPNEmc4jOMx10pyAI9MB9AL9ioGJtGkzvbGGVZuOt8WWyHc-OkBBWt0WvKuBX329qoxjIPTlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cca582c11a.mp4?token=HywflNyg-P8x9AhWr0cifm2GbG0fWsh1swdkx7heQi4WxQz2geXt9af4NQ93KkXsGH_gDJjNOC6ClGvk8xCmtRMpRWjDsc-ipcekOyIqEHCSmuOc1KoRNIqugpV44LdXxIPelzry1OuZxvN8iMPHSlPirzhjmbUoWGIHZ-WX12iU9cfXVlyRMzeQS8elW12HzvlcB69y25OO9r37n_Pa3MUkPc82g4YfFb49p5SFbUjfIwhuyiNyzdAOAi1YNM-3_7p1Lb3_wflZCQPNEmc4jOMx10pyAI9MB9AL9ioGJtGkzvbGGVZuOt8WWyHc-OkBBWt0WvKuBX329qoxjIPTlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: ارتباط ما با نخست‌وزیر هند روزبه‌روز بهتر می‌شود
🔹
در تلاشیم بر پایه فرهنگ و رابطه دیرینۀ ۲ کشور، مقابل تمامیت‌خواهی بایستیم.
@Farsna</div>
<div class="tg-footer">👁️ 6.68K · <a href="https://t.me/farsna/462094" target="_blank">📅 22:24 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462093">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9597355cae.mp4?token=ppX7pjQU4mBfyJ7m6UWMgwq2u2CKyMFTdhIMeQe0UcEsZcpdRU1kYh6qhJISBcq3s0zp1ht3dJPhLRaSIdYNYTBk4yfPasT5l1-3kqBpTRrhnfB625XAx2Pe58qXX2oOpCDxJxhRSpye3Vvodp9uxHPwB44Cv43xM9KXwoG_s7mKtuJybaRC7ThZ_Iv6YELYDHfBP5to5kPRhT3sGKOknYCV6ymfXrTPa3BfeTAy5lg3HOPoJHF_clyJTL3Fi1I7loN_mBrT6r9QdVe_j_gc91P1k6COMVk3QAhXsZTSiHDPRS9Y8CNKvMi-VDRVn1fBoRClP-JRMETceprvAnnhkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9597355cae.mp4?token=ppX7pjQU4mBfyJ7m6UWMgwq2u2CKyMFTdhIMeQe0UcEsZcpdRU1kYh6qhJISBcq3s0zp1ht3dJPhLRaSIdYNYTBk4yfPasT5l1-3kqBpTRrhnfB625XAx2Pe58qXX2oOpCDxJxhRSpye3Vvodp9uxHPwB44Cv43xM9KXwoG_s7mKtuJybaRC7ThZ_Iv6YELYDHfBP5to5kPRhT3sGKOknYCV6ymfXrTPa3BfeTAy5lg3HOPoJHF_clyJTL3Fi1I7loN_mBrT6r9QdVe_j_gc91P1k6COMVk3QAhXsZTSiHDPRS9Y8CNKvMi-VDRVn1fBoRClP-JRMETceprvAnnhkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گل اول استقلال به السد توسط آسانی
⚽️
استقلال ایران ۱ - ۰ السد قطر @Farsna</div>
<div class="tg-footer">👁️ 6.98K · <a href="https://t.me/farsna/462093" target="_blank">📅 22:24 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462092">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🔴
الجزیره: وزارت خزانه‌داری آمریکا یک بانک روسی را به‌دلیل همکاری با ایران تحریم کرد.
@Farsna</div>
<div class="tg-footer">👁️ 6.99K · <a href="https://t.me/farsna/462092" target="_blank">📅 22:21 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462091">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🔴
منابع عربی از فعال‌شدن آژیرهای هشدار درپی حملۀ موشکی انصارالله یمن به منطقۀ نجران در عربستان سعودی خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 6.72K · <a href="https://t.me/farsna/462091" target="_blank">📅 22:20 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462090">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J-dOgtuA7O4pahgKIJLQPn_8mVoMIif9Mq94czljxcJuh-BS-6OcFFr_f-jbAqCJzZVIYfdPqEqGX7DWvyJNGesDLbfQZeb5sX0j_uBw9gzAtKOe13caCDhFm-9Vmrqf9FpdBH10oLizDZk-9V9ojxN9oVoe98TdNbqtemZW4xgGkm314Zy-yeUSOLrq3KHvgU-fkDCz8OCJp7vVMPbGS23wKGaq-GwNZ8UxhFmR5nsf-fTuNRB1EX6vkSRYWxn3PYcDM0U_0K2pCFeRpJDxnoc_BHe2CE7sZXcMh3TXgbFdbSPTw-iNTvQgyyNsDA5PpdZ5xCVdz1GWB3pY9nCuSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چه شد که پس از ۶ ماه، مصاحبۀ جنجالی خلبان آمریکایی منتشر شد؟
🔹
روز گذشته، شبکه آمریکایی «CBS» در مستندی مدعی شد با خلبان جنگنده‌ای که در ایران بود، مصاحبه کرده است؛ یکی از بخش‌هایی که در این مصاحبه مورد توجه کاربران خارجی قرار گرفت، این است که فرد مصاحبه‌شونده می‌گوید با سرعتی بین ۱۱۰ تا ۱۶۰ کیلومتر بر ساعت سقوط کرده و بعد از شکستگی در کمر و چند نقطه، توانسته تا ارتفاع ۷۰۰۰ پایی فرار کند!
🔹
مصاحبه با خلبان ادعایی آمریکا، با تاخیر حدود ۶ ماه منتشر شده است. جدای از داستان عجیب و نسبتا تخیلی در این مصاحبه، انتشار آن در چنین زمانی، می‌تواند دو هدف را برای آمریکا و شخص ترامپ، در پی داشته باشد.
🔹
کلید اول حل مسئله، این است که داستان را از روزهای اوج جنگ ببینیم، نه صرفا روایت نجات. در طول جنگ ۴۰ روزه، ایران جنگنده‌های متعددی از انواع مختلف آن شامل F-15، F-35 و A-10 را هدف قرار داد. این در حالی بود که ایالات‌متحده مدعی نابودی کامل پدافند و تسلط بر آسمان ایران بود.
🔹
در ماجرای یکی از هواپیماهای هدف گرفته شده، اخباری مبنی بر سقوط دو خلبان آمریکایی در ایران منتشر شد؛ ایالات‌متحده نیز مدعی بود دو عملیات نجات برای فراری دادن این خلبان‌ها انجام داده که یک مورد آن، به طبس ۲ معروف شد.
🔹
در این عملیات، ایران بیش از ۸ پرنده آمریکایی را منهدم کرد و به تعبیر تحلیلگران «آمریکا برای نجات یک خلبان، یک اسکادران از دست داد.»
دو دلیل برای انتشار مصاحبه در زمان فعلی
🔸
آمریکا به روزهای انتخابات خود نزدیک شده و ترامپ نه‌فقط در میان دموکرات‌ها، بلکه در پایگاه اصلی جمهوری‌خواهان هم حمایت خود را از دست داده است. درنتیجه، برای احیای چهره شکست‌خورده خود، به هر ابزار کوچک و بزرگی چنگ میزند و یک مورد کوچک آن، قهرمان سازی از خلبانی بود که جنگنده فوق پیشرفته‌اش با پدافندی که ترامپ می‌گفت نابود شده، ساقط شد.
🔸
رسانه‌های آمریکایی سعی کردند از تکنیک «گذر زمان» استفاده کنند. به این معنی که امید داشتند با گذشت ۶ ماه از آن ماجرا و انبوهی از اتفاقات پرسرعت در این مدت، تصویر شکست اصلی در ذهن مخاطب کمرنگ شده و حال با ارائه یک تصویر قهرمانانه، بتوانند جایگاه خود را احیا کند.
🔹
حتی اگر فرض کنیم آمریکا، خلبان خود را نجات داده و شخص مصاحبه شونده همان خلبان است، صفر تا صد فرآیند ساقط شدن جنگنده، عملیات نجات و زمین‌گیر شدن نیروی هوایی ایالات‌متحده داخل خاک ایران، یک تصویر را ارائه می‌کند: «شکست قطعی ترامپ.»
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.59K · <a href="https://t.me/farsna/462090" target="_blank">📅 22:16 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462089">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd8c4473cc.mp4?token=AhGjZ6MG-z7IeTRpdQYVNOYoTlWrDE6nCjSEEyp8Xy9UcA8y5yBHSeebKo7-NP5W67BRlTDvOV8ehqkfHxV7Osi6pehh23LSvnCS1IVXQvQMxT0BWOIj3s0ImVFBFMw9kTCBrY2I0TmSauC4B2BnAh65IrJ33_gYR-ZMBI2AVSiJ6VNVkedhIW8pWX17DdV7MRSd9IGoX4Bukwb0J77VJ6uoGBrlxJKyH8AGqX92PG8iP2fNgx5WYh6ixNK5wFpfnmaeHmm7BCI6ldZRpbJPjAMlkrnMW8gRzyWNwH3Hcl0LK2rjuEBIj8rE_-skg3KjR7B4EZIRlm3r2lY5_1bOeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd8c4473cc.mp4?token=AhGjZ6MG-z7IeTRpdQYVNOYoTlWrDE6nCjSEEyp8Xy9UcA8y5yBHSeebKo7-NP5W67BRlTDvOV8ehqkfHxV7Osi6pehh23LSvnCS1IVXQvQMxT0BWOIj3s0ImVFBFMw9kTCBrY2I0TmSauC4B2BnAh65IrJ33_gYR-ZMBI2AVSiJ6VNVkedhIW8pWX17DdV7MRSd9IGoX4Bukwb0J77VJ6uoGBrlxJKyH8AGqX92PG8iP2fNgx5WYh6ixNK5wFpfnmaeHmm7BCI6ldZRpbJPjAMlkrnMW8gRzyWNwH3Hcl0LK2rjuEBIj8rE_-skg3KjR7B4EZIRlm3r2lY5_1bOeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بالیوود آمریکایی
🔹
تصاویر دیده نشده از خلبان امریکایی که با سرعت ۱۶۰ کیلومتر در اصفهان سقوط کرده، زنده مانده و با بدنی شکسته از کوه بالا رفته است!
@Farsna</div>
<div class="tg-footer">👁️ 7.41K · <a href="https://t.me/farsna/462089" target="_blank">📅 22:10 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462088">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🔴
منابع عراقی از وقوع انفجار و آتش‌سوزی در منطقۀ شمامک در اربیل عراق خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 7.35K · <a href="https://t.me/farsna/462088" target="_blank">📅 22:07 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462087">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🎥
پرچم ایران در قلب میدان انقلاب چهار محال‌و‌بختیاری چرخید
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.4K · <a href="https://t.me/farsna/462087" target="_blank">📅 22:04 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462086">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZPpzBkVuWRnO18G6azM5uMMje6xRHw5Y6dlozhSB3EWLubkSDmnVY6JNzESFHvZyDHtlZZzMj0cx966-59-TwS3Whu1Pw3X8jVgqPaE_6nsgOa7VV3J2_bOZDLYd_H4zrgSF6hbE1YcgnW_vARkxstaJR9k4UfNMAEtN39QjsmPCM95A-EQbjTkKc-mW58YT_gM_P_G5VEiti36sKKNCuN5TIP75_PuLHRvx-HrPZN6DB5mBNV1zOaF_FGhrrZdZON9Cnja4x2K5iXxsWnpMqgdw-yI1TSsVRZPXzVOM2Tk0rECaVISj_K5YC5OCP7OYytrIvIKAszpPSRs4iA9Jvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس اتحادیۀ میهنی کردستان عراق به تهران می‌آید
🔹
سخنگوی وزارت خارجه اعلام کرد بافل طالبانی رئیس اتحادیۀ میهنی کردستان عراق سه‌شنبه به تهران می‌آید تا با مقامات ایرانی دربارۀ تقویت ثبات و همکاری‌‎های مرزی گفت‌وگو کند.
🔸
اتحادیۀ میهنی کردستان یکی از ۲ حزب اصلی در ساختار سیاسی کردستان عراق است.
@Farsna</div>
<div class="tg-footer">👁️ 7.5K · <a href="https://t.me/farsna/462086" target="_blank">📅 22:01 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462085">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb252f09ef.mp4?token=UaWwiyOAPoFW4dptNWHIGRTklZpzs_-EgAcnRGuK4EvB37EYjHp7fscRgMTKSXdhVj8HMrokcuacyU9Vf864N3GWUI3jvE98_A2Qr5j53ltxfeApcAlH_VRWag_G8S7w1yIyrdL38M07UbFKnAuMtYkqyejeSLx-lazTFvJO32EfywNaNnfnZXTdlBL2kz8DQdKZmaLbIpVWfJLD55Z8rZuHzGWMxiN7bUsiRa4jKIj8uWoJwMHqGJh4L2Kp-XNaUGiVedamM0GKWZ7N0myIb8M0FfaRD2cfKzro8C_F9sQPSKhLMI2rXURmedk04d04A-hyDfChiIDy2RGcuaJiRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb252f09ef.mp4?token=UaWwiyOAPoFW4dptNWHIGRTklZpzs_-EgAcnRGuK4EvB37EYjHp7fscRgMTKSXdhVj8HMrokcuacyU9Vf864N3GWUI3jvE98_A2Qr5j53ltxfeApcAlH_VRWag_G8S7w1yIyrdL38M07UbFKnAuMtYkqyejeSLx-lazTFvJO32EfywNaNnfnZXTdlBL2kz8DQdKZmaLbIpVWfJLD55Z8rZuHzGWMxiN7bUsiRa4jKIj8uWoJwMHqGJh4L2Kp-XNaUGiVedamM0GKWZ7N0myIb8M0FfaRD2cfKzro8C_F9sQPSKhLMI2rXURmedk04d04A-hyDfChiIDy2RGcuaJiRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
چراغ این خیابان‌ها ۱۹۸ شب خاموش نشده
است
@Farsna</div>
<div class="tg-footer">👁️ 7.47K · <a href="https://t.me/farsna/462085" target="_blank">📅 21:58 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462084">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9555c33a5d.mp4?token=ema_XQdwC2Ii8TQjhxhubn3s4gyge8miYegO0Mjsenohp2iAXzOgMvN_lL37z2z_6jvXKpX7tzB-G-0_-KVjkrSr6lNUanlXXi3yrcoNa2G4KCOY0ZmIzCIEOwNtocpHNIv8uOgIB0N8YPiXVmWs7GUedlRG5ITlU0ioMR7HYxNxFVHGUK1ar8K8efOyy1vfyZ2ofm_Yaf0RdG83zmu1-fM5_d8fzk2h9BzStS5Igy1kO3poBDSxbbs6JM6AoMncS9EcWVvZKzOJWhXK8f-BKd4YPQAjCZvZnFstBe0fuC2v_2Z-cqFeCPO0K4sc29A3nrLg4NNxvWDX8BSzQU-pzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9555c33a5d.mp4?token=ema_XQdwC2Ii8TQjhxhubn3s4gyge8miYegO0Mjsenohp2iAXzOgMvN_lL37z2z_6jvXKpX7tzB-G-0_-KVjkrSr6lNUanlXXi3yrcoNa2G4KCOY0ZmIzCIEOwNtocpHNIv8uOgIB0N8YPiXVmWs7GUedlRG5ITlU0ioMR7HYxNxFVHGUK1ar8K8efOyy1vfyZ2ofm_Yaf0RdG83zmu1-fM5_d8fzk2h9BzStS5Igy1kO3poBDSxbbs6JM6AoMncS9EcWVvZKzOJWhXK8f-BKd4YPQAjCZvZnFstBe0fuC2v_2Z-cqFeCPO0K4sc29A3nrLg4NNxvWDX8BSzQU-pzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گل اول استقلال به السد توسط آسانی
⚽️
استقلال ایران ۱ - ۰ السد قطر
@Farsna</div>
<div class="tg-footer">👁️ 7.88K · <a href="https://t.me/farsna/462084" target="_blank">📅 21:55 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462082">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k4NG3jzx3pg8YEs9kRLT7j95kCAEHZp8Yu4-fykPU3pWe8TQSJIGbMVEKxVgYsf-uRCqn78YBmYzfFYkYNVUjZg69q_ooroZWgB3onfrw13S2Tq8zE761AycVn4vV4W6Xk2bdAfgyoILevSVX_g05YX0gbO1WVk_J6M1sVFx-En0aDm4Y-IQXyGezu25HDZM22PBE_2DqNELsuGlj9EEEtagYIt70rBjc77CPxn-Ptr-kX16aCPHMndM9sAB7wTKnDpxW5XNj29GzPQdthTlfUXKeqUEr6zEZsonyAv8pDI_aIEhBS6eebAt2PkRULMAnvjGDgE7Ztr6eiFCzsQgcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
مسیر فرار نفت عربستان از هرمز در آتش سوخت
🔹
تصاویر ماهواره‌ای جدید یک ایستگاه پمپاژ متعلق به خط لولهٔ راهبردی عربستان سعودی موسوم به «شرق–غرب» را نشان می‌دهد که درپی حملهٔ پنجشنبهٔ گذشتهٔ یمن، به‌شدت آسیب دیده است.
🔸
این خط لوله حدود ۱۲۰۰ کیلومتر طول دارد…</div>
<div class="tg-footer">👁️ 7.88K · <a href="https://t.me/farsna/462082" target="_blank">📅 21:49 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462081">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ef0e89bac.mp4?token=FlONqNMDnxPiuBtnaNGQJalJOfRA38n9BbyUfntFSs-WFo_25xsDKkp4ZJlGnQGM2T0uStdN85Iuds-xkzA9_h350_H9vYqZHCE_HD6SRFORd3nVxqhcWXNQZlyFAwkzJ9qCp68gMcuuzlLu2bA3xGHp93XOc-NTS_j7GRW4m2SYfOcR4JguC-Id6lMaSXtzej3I928nq8LLw7Jxzf2scE3DWO_Hl-vgKgKHdYv4UtkSo7p71iHjwu_BAEzsP0rBW_dnNrsHVigmBwLqOY9ujkEjeSAtlJ84xoNc3MjZ7d4tOTzXz_pqMpuwQx2JvCaGr1qr3DKM_vvDawoUaNrcow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ef0e89bac.mp4?token=FlONqNMDnxPiuBtnaNGQJalJOfRA38n9BbyUfntFSs-WFo_25xsDKkp4ZJlGnQGM2T0uStdN85Iuds-xkzA9_h350_H9vYqZHCE_HD6SRFORd3nVxqhcWXNQZlyFAwkzJ9qCp68gMcuuzlLu2bA3xGHp93XOc-NTS_j7GRW4m2SYfOcR4JguC-Id6lMaSXtzej3I928nq8LLw7Jxzf2scE3DWO_Hl-vgKgKHdYv4UtkSo7p71iHjwu_BAEzsP0rBW_dnNrsHVigmBwLqOY9ujkEjeSAtlJ84xoNc3MjZ7d4tOTzXz_pqMpuwQx2JvCaGr1qr3DKM_vvDawoUaNrcow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شهید مظلوم اهل سنت، امروز چگونه به شهادت رسید؟
@Farsna</div>
<div class="tg-footer">👁️ 7.64K · <a href="https://t.me/farsna/462081" target="_blank">📅 21:46 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462080">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QA7efWOk1O0bUK32SpgLm9o-g1tSv-uI6fPKpbXHut7glsk34N663GuXI3gSnF4eqa8tT9IXN9z2qXqOc1V2BqqpOGFuYHZSRRVQcSe4pEsa7SXvMvSAjdU3a-Z6Wcx3x0a3nKhrEwfp7ySTgYgBqbOE8H1myWqx2ue5IxnYv_5_zC5IVwKJg3AZaL0YketI32mIYP1fLzypReSZlyQXE_8AWOvVmm9ru7sE0RWHf5XTgO4WQOt34uUfP80qpdmZdCYsQxO3hBN0Js6qg8OGr-0-UEtrRmAR5qhr1U1LxcK3nefqyglCwgDe3Ny8Ezq5AFv3fvd0gqSQ0cws-wWQKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از آمادگی مردمی تا آموزش؛ دوره‌های «جان‌فدا» آغاز می‌شود
🔹
دوره‌های آموزش نظامی و امدادی ویژه داوطلبان پویش مردمی «جان‌فدا» از سه‌شنبه ۲۵ شهریور آغاز خواهد شد.
🔹
داوطلبان برای شرکت در این دوره‌ها می‌توانند عدد ۱ را به شماره ۳۰۰۰۱۱۵۵ ارسال کنند و به سایت
JANFADAA.IR
مراجعه کنند.
@Farsna</div>
<div class="tg-footer">👁️ 7.72K · <a href="https://t.me/farsna/462080" target="_blank">📅 21:45 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462079">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eEF4HWmlGWiQLfG9Vs7LrIdpMBTRWiMfJzxN38HIRZ2E7IbQ037oDHVv1x60hntltmE0izRz1mnnF8-_-MWb_pED2huGFVieYUAOaZL5J6o5-BaxWDCNp4Mtap1x099K_zgi0fEtFAtyAchKFtEPwPW75-_724MxmJ2zVCET6vWwEuuMVDhYn0lNuubuc6iqaf1FT2_l4TdSqSQwRqX54wB2i6dBylz6N8yrd_uIW7I6BbtnIY7D0-AqQxpaLjXU_ygZwGTz3sD-au4LDYAYnADtz77ahRx_5o7odPq1lQUtkb5czIaZqJw5Tf6IdOxX5ZfGSNSbmhkaqW9zfRmAig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان خطاب به آمریکایی‌ها: حداقل مردانه بجنگید
🔹
آمریکایی‌ها دولت تروریستی تشکیل داده‌اند و هر کس را بخواهند ترور می‌کنند.
🔹
مدعیان حقوق بشر و انسانیت، اگر صادق هستید، چرا کودکان، بیمارستان‌ها و زیرساخت‌های مردم را هدف قرار می‌دهید؟
🔹
اگر مرد میدان هستید،…</div>
<div class="tg-footer">👁️ 7.05K · <a href="https://t.me/farsna/462079" target="_blank">📅 21:42 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462078">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e1590b887.mp4?token=TSG_dNrih1EO9Qx6xnviAd3ba_pZmRwnS81v5m1Jwl0G4stxE-VwTl20scAeuzKZfK8vLZ5j45YFZjEsI5UC540aKz_AngN85QxerQGq5su_mLxGkdSp0-EUwXsYYEf3XLb1OvzzedPEvJNTCZSxWUZdFP_WyBdXegrxBbJE7CH8R-9jD4SzwLXiZsGAtVmiU6tzs1_10WAxB35250vtrJoV_4KIHBL7IPbQ1DiWfBAYAD6djNJIf7oRXndtzE2nOela1B3OyF3BHRjtWvpxxP3nY7OGcUl3MGDRDl9GUbMMJ9lRVnz3UNXnwAxxWNaoKCsOqPseok4Utq_oNAlwrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e1590b887.mp4?token=TSG_dNrih1EO9Qx6xnviAd3ba_pZmRwnS81v5m1Jwl0G4stxE-VwTl20scAeuzKZfK8vLZ5j45YFZjEsI5UC540aKz_AngN85QxerQGq5su_mLxGkdSp0-EUwXsYYEf3XLb1OvzzedPEvJNTCZSxWUZdFP_WyBdXegrxBbJE7CH8R-9jD4SzwLXiZsGAtVmiU6tzs1_10WAxB35250vtrJoV_4KIHBL7IPbQ1DiWfBAYAD6djNJIf7oRXndtzE2nOela1B3OyF3BHRjtWvpxxP3nY7OGcUl3MGDRDl9GUbMMJ9lRVnz3UNXnwAxxWNaoKCsOqPseok4Utq_oNAlwrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر تعاون: بازنشستگان می‌توانند طلای مورد نیاز ۳ ماه آینده خود را از سامانه بانک رفاه خریداری کنند؛ هزینه آن متناسب با میزان خرید از حقوق ماهانه‌شان کسر می‌شود و قیمت طلا تا ۳ ماه ثابت خواهد ماند.
@Farsna</div>
<div class="tg-footer">👁️ 6.99K · <a href="https://t.me/farsna/462078" target="_blank">📅 21:38 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462076">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef043e7560.mp4?token=eHdh3YkS6xCPXqSSdcAD5qal24lTbJ-b2nhVpXCRmmbC1xmf1xJ5Ydze6HQ1i7HQ7NnXt-GsZObth4TtatoE0F-4sGkubBtiD3hPOEFv7kAG16TsUNIPxRq3AuK5TUa8u3KxtoBwoXNA4_BS1yfCjt79dguaQmkB3EojQg7AReorTSOybmmqgN4uP8mIm6qrAZhfyO__jWeO_ngDAUQVUMTwLVPsDDySP8s6tgF8wHvTJSGuPdNCii7wo2t7eCtrZa1oLVAioS3PB9e6FQltaCHbovp0Gq-nGWr0v0_Z2HarUYMrzwvhZxSZDJxCzbyRJ2VrRzo3RK1zVsCec65kTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef043e7560.mp4?token=eHdh3YkS6xCPXqSSdcAD5qal24lTbJ-b2nhVpXCRmmbC1xmf1xJ5Ydze6HQ1i7HQ7NnXt-GsZObth4TtatoE0F-4sGkubBtiD3hPOEFv7kAG16TsUNIPxRq3AuK5TUa8u3KxtoBwoXNA4_BS1yfCjt79dguaQmkB3EojQg7AReorTSOybmmqgN4uP8mIm6qrAZhfyO__jWeO_ngDAUQVUMTwLVPsDDySP8s6tgF8wHvTJSGuPdNCii7wo2t7eCtrZa1oLVAioS3PB9e6FQltaCHbovp0Gq-nGWr0v0_Z2HarUYMrzwvhZxSZDJxCzbyRJ2VrRzo3RK1zVsCec65kTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سرمربی استقلال: در کشور دوست یعنی عراق می‌توانیم از شرایطی شبیه به میزبانی برای بازی با السد استفاده کنیم  @Farsna</div>
<div class="tg-footer">👁️ 7.12K · <a href="https://t.me/farsna/462076" target="_blank">📅 21:34 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462075">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس من</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vUtK65TmFuts19aagx19tkm-BPiNntjMF-d7wWNmmIfd2ye2BXsctFiakDWX78mHb8nr5A7OKutDtnZtkfto3bNwj_2jI8hFG_GVUQoFGJnBejIrgX750BtQqLweli9EN5k5KCX83HACXXzwT_oEGXzHtaz-uM50uol9VG4Ag5milfUu8wlDOwFkmR7acUhvvAdZSAU7frAMgvGxIZJ_zJRNDZinhNs6q80tXKqrA1svP9QqjiD_Wg_f9seBcP2Afxlh1l9jthQwYUDdhh3WYSRGLaL6rvKWLgimT8HkGx8h5KmEEQnTjluUzxvVZ9EDTvYRX72R7Aes3wBDQ0EM2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خانه‌هایی که برای فروش نیستند!
🔹
«در تهران بیش از یک میلیون مسکن خالی داریم که به نوعی احتکار شده‌اند» این جمله رئیس مجلس محمدباقر قالیباف است.
🔹
دولت می‌تواند با گرفتن مالیات از خانه‌های خالی، مالکان را به سمت اجاره یا فروش ملک سوق دهد، اما میزان مالیات اخذ شده از خانه‌های خالی در ۴ ماهه نخست سال ۱۴۰۵ «صفر تومان» بوده است.
🔹
طبق اعلام مدیرکل سابق دفتر اقتصاد مسکن ابوالفضل نوروزی، در ایران برخی افراد بیش از ۱۰۰۰ ملک دارند.
🔸
کارشناسان معتقدند اجرای مؤثر قانون مالیات بر خانه‌های خالی و مالیات بر عایدی سرمایه می‌تواند به افزایش عرضه و کاهش سفته‌بازی در بازار مسکن کمک کند.
🔗
حالا جمعی از مخاطبان فارس در پویش خواستار مقابله با احتکار خانه شده‌اند؛ اگر می‌خواهید از این پویش حمایت کنید
اینجا
کلیک کنید.
@Farsnews_My
-
Link</div>
<div class="tg-footer">👁️ 6.97K · <a href="https://t.me/farsna/462075" target="_blank">📅 21:29 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462074">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4a188659f.mp4?token=itBcc3MsUltiMoIHYqFE9oAhMxwumM-u0VRY3Xjm9h3-hpsXFDNZiyZWOZhlo9w1QC4KmaW65lepixcz-N96FpL_OcDhU4RcduvQIEkwNmzN_34hu1uBH40atYsWi5gHyiqkEph2EC9mNpUloK-W51YJOaGrR3BxAeZcsLoFNe9GtzVI5b1WL3CUEe13sqKM9dQevCeDwMDrWKAvErqGzYpTPPtP1ZizAUTvwShqHN9NEzjf9mAR29cD_abVumIrIWdt3M9Qai-Tq2cZBJh_PeSaqtRP8CqRaaxKMb8j1vDEuuP0txUdHUZpueTLaAhaINwNCPes_BDWCsM2bCdVb6lY8rFb2L7psZiqkSv9miylZ9S5jNynQDCNq6vFAVyew39ioKOoeFtg7F150kHsKDaYwJI3HY6XsVUhCg9QAWsXOdcGzGD6vtz1lFiF_ADKHzhz3U6N2Z97fMCRIGeTeqI36YTEiuKPJ0fJo0aHGNBk9vex0M_PMyy5AH8Q7vxZXPMbGnLn5ZbWQ8PKRtfisKkpAXbX2XYPAhz_hQGrcrTbmn8bfvYWPdznISB9d9FThk92ySKDjD5TVtp2I7SHtv7mqqEM-FtmlaGNssIiWGkTLMko3eg5joUWTmBfq0zr8PzhL9OJWj0GXAt-QnEckVJ1wdaor4XgYOZFLSxR6Dk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4a188659f.mp4?token=itBcc3MsUltiMoIHYqFE9oAhMxwumM-u0VRY3Xjm9h3-hpsXFDNZiyZWOZhlo9w1QC4KmaW65lepixcz-N96FpL_OcDhU4RcduvQIEkwNmzN_34hu1uBH40atYsWi5gHyiqkEph2EC9mNpUloK-W51YJOaGrR3BxAeZcsLoFNe9GtzVI5b1WL3CUEe13sqKM9dQevCeDwMDrWKAvErqGzYpTPPtP1ZizAUTvwShqHN9NEzjf9mAR29cD_abVumIrIWdt3M9Qai-Tq2cZBJh_PeSaqtRP8CqRaaxKMb8j1vDEuuP0txUdHUZpueTLaAhaINwNCPes_BDWCsM2bCdVb6lY8rFb2L7psZiqkSv9miylZ9S5jNynQDCNq6vFAVyew39ioKOoeFtg7F150kHsKDaYwJI3HY6XsVUhCg9QAWsXOdcGzGD6vtz1lFiF_ADKHzhz3U6N2Z97fMCRIGeTeqI36YTEiuKPJ0fJo0aHGNBk9vex0M_PMyy5AH8Q7vxZXPMbGnLn5ZbWQ8PKRtfisKkpAXbX2XYPAhz_hQGrcrTbmn8bfvYWPdznISB9d9FThk92ySKDjD5TVtp2I7SHtv7mqqEM-FtmlaGNssIiWGkTLMko3eg5joUWTmBfq0zr8PzhL9OJWj0GXAt-QnEckVJ1wdaor4XgYOZFLSxR6Dk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
از واقعیت تا قهرمان پوشالی
🔸
خلبانان آمریکایی برخلاف ادعای مکرر رئیس‌جمهور آمریکا دربارهٔ نابودی پدافند ایران، به قدرت رصد، رهگیری و شکار جنگنده‌های خود اعتراف می‌کنند.
@Farsna</div>
<div class="tg-footer">👁️ 6.66K · <a href="https://t.me/farsna/462074" target="_blank">📅 21:26 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462073">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U6hxW6Q4xFoErN159S140CDdeBquZLg4Rxwydz7wePgVpwG4iolJks6EPsJER3mqrx_pj08nM0JlNBJJzKJqA9aGc4H1T7BGfvyehG8HE00Bwum85uKG08hKryfHE1wiHwfCNl_OZhUW09Ik4VnB0OlDIe8j5TixvziFpaTJ53I_PIX3Ra_8pOPO63E_LJMEV5QYyIhc90IFPP60QHArP6ZceHpEZSlSKLo_kiMUrjfhzU-A3DRD9Cjo-iklkmqYaS2EWkf0XxThUueKPmlrTcOCggQSoskFmwM3MZYgKIV_fNgtTnEfArcrkcSd2zsS35xBjRVc8DcDM0F8Uejz7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
گل اول الاهلی به تراکتور توسط سزار روی اشتباه خلیل‌زاده
⚽️
شباب الاهلی ۱ - ۰ تراکتور @Farsna</div>
<div class="tg-footer">👁️ 6.99K · <a href="https://t.me/farsna/462073" target="_blank">📅 21:25 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462072">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GyEh4rrEmzJQKHI1_fsKLTOOWK8ETABO3QBEXu7NxhnaHeLXq_vjJi1geYjAVyRJ8XVOv9e1FKYxE5_ywhGzAAWpDYHG3utmM_unV0Lwy97Jhb7y9xSCk3oKXKRvWxM4GN_HRVVQPte4lsK34Z5NIZlSMbNz0Zi0p_dje7PXcBS1_vLMafV80g8UwpYUd3YMkbZtdHvjsZLSdrahhwCxKNeqexVPjuurKkey2dFFcVurIGCDC6gg27-Kd2kV4l7upp2dJruUJEPbJuFk2n2kpcfTwYeK7orutgzoSX_-Ht8dgdcO09mA4Z1UhsBZZUE9GwopvrJosebfpG5Lanh_hA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان خطاب به آمریکایی‌ها: حداقل مردانه بجنگید
🔹
آمریکایی‌ها دولت تروریستی تشکیل داده‌اند و هر کس را بخواهند ترور می‌کنند.
🔹
مدعیان حقوق بشر و انسانیت، اگر صادق هستید، چرا کودکان، بیمارستان‌ها و زیرساخت‌های مردم را هدف قرار می‌دهید؟
🔹
اگر مرد میدان هستید، بجنگید؛ نه اینکه با ابزار و تکنولوژی، انسان‌های بی‌گناه را محروم و آواره کنید.
🔹
امام حسین(ع) در کربلا به دشمنان فرمودند: «اگر دین ندارید، لااقل آزاده باشید». اگر انسانیت دارید، حداقل مردانه بجنگید.
🔹
راه را بسته‌اند و تحریم می‌کنند؛ تحریم به چه کسی صدمه می‌زند جز مردم؟ کسانی هم دم از ایرانی‌بودن می‌زنند و دیگران را به این اقدامات تحریک می‌کنند.
@Farsna</div>
<div class="tg-footer">👁️ 7.1K · <a href="https://t.me/farsna/462072" target="_blank">📅 21:21 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462071">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fm2k0lpWJjumGPX0LBGwsNbjg9f9IYWLInKQqu6P0TnHJvC7LbnTYQm2bqoE83CdrljXoF6TEJBa0uPqBz1-s0gp85qIX5OOc-NV8sXnmoSxtnI4tE6eb-UvRogG4pi0OmwxDSEbkr1P54y5dprroHZC58Pjztmc2jRgUj8r5oFGHpuUyO5mXDL4-GU7rWdwDydr9pRcmy2c5rkazOlpHrkXCs4BhomGnSC9zOu4b5nnVs5dh3VdA32hfsn9deqWojzkBe74zz88CgV3smvAB6Be1JKcevCK_vsXLZjM8pwIAR54qW9GMCdVN0u7ic8pQXdgUAW4HEHO1vSe21obAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدرسه‌ای که قابش از کلاس درس به رقص و قمار رسید
🔹
انتشار ویدیویی از صفحه رسمی دبیرستان غیردولتی «صعود» شهرکرد، حاشیه‌ساز شده است؛ ویدیویی که در آن صحنه‌هایی از رقص، بلاگری و استفاده از ابزارهای قمار در فضای مدرسه دیده می‌شود.
🔹
این تصاویر این سؤال را ایجاد کرده که چنین برنامه‌ای چگونه در یک محیط آموزشی برگزار شده و چه نظارتی بر آن وجود داشته است؟
🔹
مدیر روابط‌عمومی آموزش‌وپرورش چهارمحال‌وبختیاری گفته این مدرسه مجوز آموزش‌وپرورش را دارد و موضوع در شورای نظارت بر مدارس غیردولتی بررسی می‌شود.
🔹
به‌گفتۀ او، مدیر مدرسه مدعی شده تصاویر مربوط به یک دورهمی خانوادگی بوده که در فضای مدرسه برگزار شده و انتشار ویدیو نیز به‌اشتباه توسط ادمین صفحه انجام شده است.
🔹
با این حال، آموزش‌وپرورش تأکید کرده مدرسه محل برگزاری مهمانی و دورهمی نیست و در صورت احراز تخلف، شورای نظارت درباره آن تصمیم‌گیری خواهد کرد.
🔸
حالا سؤال اصلی این است: چطور رقص، تولید محتوای بلاگری و نمایش ابزارهای قمار، آن هم در فضای یک دبیرستان، امکان برگزاری و ثبت و انتشار پیدا کرده است؟
🔸
با توجه به محتوای منتشرشده، انتظار می‌رود در صورت وجود جنبه عمومی یا عنوان مجرمانه، مراجع قضایی نیز موضوع را بررسی کنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.94K · <a href="https://t.me/farsna/462071" target="_blank">📅 21:17 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462070">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6978f750b.mp4?token=kHkXRHm9BnOt6IURT_0lh1n7O3Sog6uoO80ASPSmbEuluN6agwoAxXOc4NsbQ4OHKX2TX9EbQ5JgxT5Kme7f_q1DT-oqpIGJp4BieIe-7C_it8ajge7_z3PPO2OTY90tGEy1PTAB5pvtdXd441OhfQxOTcgMgWX7pOpLmkheBlp1rybi7hwnaim5aol7Wp6FauNyexGnCAl7B5n6Yfbl9hCeFSX-O_QkcACwIbAxbtNAWbSHdUe1k1Vz29ttt3643e9sA6X6YwevmvEaEB9fSjh0rs-MORACcgIoPhIWTOX6GoTLsJLVIRO0DQDc6qI8bpM4ZBIFVz1jxO83inUIHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6978f750b.mp4?token=kHkXRHm9BnOt6IURT_0lh1n7O3Sog6uoO80ASPSmbEuluN6agwoAxXOc4NsbQ4OHKX2TX9EbQ5JgxT5Kme7f_q1DT-oqpIGJp4BieIe-7C_it8ajge7_z3PPO2OTY90tGEy1PTAB5pvtdXd441OhfQxOTcgMgWX7pOpLmkheBlp1rybi7hwnaim5aol7Wp6FauNyexGnCAl7B5n6Yfbl9hCeFSX-O_QkcACwIbAxbtNAWbSHdUe1k1Vz29ttt3643e9sA6X6YwevmvEaEB9fSjh0rs-MORACcgIoPhIWTOX6GoTLsJLVIRO0DQDc6qI8bpM4ZBIFVz1jxO83inUIHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر راه‌ و شهرسازی: هر وعده‌ای که می‌دهید باید انجام دهید
@Farsna</div>
<div class="tg-footer">👁️ 6.36K · <a href="https://t.me/farsna/462070" target="_blank">📅 21:17 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462069">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ebc8faeb94.mp4?token=ZAI12z75sK9kQMobV4zTxNuTSNCybjNBhWukGDpmBicS4AfXIKLTmi9ybdQQ1lyi-t_nD3gvmdm6QAIrB7ULvOF6-tblQP0_bM-0ulbpf9WbbJd9E-53-a4Yb2cGk94U_L5MT-bVqQPuuadNbN4J_OvdnkGR5nyeJT90jXYDWe-3_nKTd5SZflaMO9TU25NnTKLBZCTqmqW45dlawg04SEnDdw4HxHsw74BBprRv29mqq4OpyxvnKvDjxfJIj0xWM8h2eJ8lIDk97ieXwEVPfB6OieJExHUBQHRN8NLrJUWlj4Xz5cG93Ztyz6jfMNpCHGfmXkXIYnzqDEh77iEuoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ebc8faeb94.mp4?token=ZAI12z75sK9kQMobV4zTxNuTSNCybjNBhWukGDpmBicS4AfXIKLTmi9ybdQQ1lyi-t_nD3gvmdm6QAIrB7ULvOF6-tblQP0_bM-0ulbpf9WbbJd9E-53-a4Yb2cGk94U_L5MT-bVqQPuuadNbN4J_OvdnkGR5nyeJT90jXYDWe-3_nKTd5SZflaMO9TU25NnTKLBZCTqmqW45dlawg04SEnDdw4HxHsw74BBprRv29mqq4OpyxvnKvDjxfJIj0xWM8h2eJ8lIDk97ieXwEVPfB6OieJExHUBQHRN8NLrJUWlj4Xz5cG93Ztyz6jfMNpCHGfmXkXIYnzqDEh77iEuoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
کاربران فضای مجازی از روایتگری غیرهنرمندانهٔ یک بازیگر اینگونه انتقاد کردند
@Farsna</div>
<div class="tg-footer">👁️ 6.9K · <a href="https://t.me/farsna/462069" target="_blank">📅 21:12 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462068">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PaFpZoVeTcUfzue6sOWcqRxKTdaQFSLFzJ0zxlojUM27z1f6Bt6yye0nrGGQediLFraUrNMtNMlUgP_As6XUF4X5gRlRAchf02WbytHaE-zFp3AsLyCxbibyYRfR5KL-nIJzdN0iWr7RTJMg6LcMSLHxwOmtLbGUwSQiVcEergFny4JasSx8IorKNp1Sg0stMheFtKDd0E7YBY59A3gv-uXSJwKqAs5mcxB2mfYitan7X8rJpk057u436miMR8grNdfsRRzjTGJMGDS-BiukXB8guZQIR6tjdfccKtV-P9DasRXb-A4U_-XmIg4UPPWzahQCdp2Joeltb9OsUsWVFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
زاکانی: ۲۰۰ شب است که مردم خیابان‌ها و میادین را رها نکرده‌اند تا دشمن را عقب نگهدارند، خطای محاسباتی مسئولین را اصلاح کنند، وحدت‌بخش و انسجام آفرین باشند، از ایران و انقلاب صیانت کنند و دست بیعت با امام خامنه‌ای را بالا نگهدارند.
🔹
خداقوت به ‌ملت مبعوث شده و قهرمان ایران
@Farsna</div>
<div class="tg-footer">👁️ 7.1K · <a href="https://t.me/farsna/462068" target="_blank">📅 21:10 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462067">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5dcf505a3.mp4?token=FKyA6ZW2wXTgq9Tf4bXh5Y9IIr7nvgnQWbDcidrt8cvU9i0B88EYDsFjCGVgqcS8DO873d_7SP8gSrc4jLRWLkTJO65rFReIpzeKRk1INCFB12Fjdnqwgpi4fgdt0itgdGygL_RtyzZRIXV0wB_XtEvdsue7jgoZC6IsKj5Boyn3MDFJmsAdkNrbQE0bQQL9OB_UXzpSyVMrjflFlguE5wBt79ySfcNP1QMt8F8DI7-spDLWeU5YH8sQOb1zyiAR3MuYn0DxgSXP11QewCA358dJe49h48z49fwq7OOl6fk7TDsV6HG2XAao1v2cS0rupkMNUJeOvnHlvtLDsARp3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5dcf505a3.mp4?token=FKyA6ZW2wXTgq9Tf4bXh5Y9IIr7nvgnQWbDcidrt8cvU9i0B88EYDsFjCGVgqcS8DO873d_7SP8gSrc4jLRWLkTJO65rFReIpzeKRk1INCFB12Fjdnqwgpi4fgdt0itgdGygL_RtyzZRIXV0wB_XtEvdsue7jgoZC6IsKj5Boyn3MDFJmsAdkNrbQE0bQQL9OB_UXzpSyVMrjflFlguE5wBt79ySfcNP1QMt8F8DI7-spDLWeU5YH8sQOb1zyiAR3MuYn0DxgSXP11QewCA358dJe49h48z49fwq7OOl6fk7TDsV6HG2XAao1v2cS0rupkMNUJeOvnHlvtLDsARp3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر دادگستری: پزشکیان گفت از کارهای دیگر بزنید اما کالابرگ را افزایش دهید  @Farsna</div>
<div class="tg-footer">👁️ 6.68K · <a href="https://t.me/farsna/462067" target="_blank">📅 21:06 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462066">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0537cc5087.mp4?token=MDbUH9Yb7oq0Pn1_YQUfJ0ivHKM3uDGLlvaPfrFXIO_blt3qyX9B7KnjRXzUyeFkc2n4cYrE99CmRrJq0cgOiqp_KvZ4iQM7yaFDD_2hgSsWf2M2Q0jq2qtIEyFj-ifCS6HfGzfkUBDkl4Z82yUO-7DFIG37s0KkovchTTc6GEW0ZDCQ9UQLTwWMlI2EgjBy-AmEmOn_7h_AvKoi2Ebsw853oJBsBgrrUBb52NS2TwPqtON6fT6-X4Y1KKf0yICLqkTpGg1RXA1gjzFLTQ5PfT2K60TYJjZ_-nFbIYFU76FqTafW4SJ4gB_F30jCBCp_11C6LhvQ3xkTxloDCICOmTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0537cc5087.mp4?token=MDbUH9Yb7oq0Pn1_YQUfJ0ivHKM3uDGLlvaPfrFXIO_blt3qyX9B7KnjRXzUyeFkc2n4cYrE99CmRrJq0cgOiqp_KvZ4iQM7yaFDD_2hgSsWf2M2Q0jq2qtIEyFj-ifCS6HfGzfkUBDkl4Z82yUO-7DFIG37s0KkovchTTc6GEW0ZDCQ9UQLTwWMlI2EgjBy-AmEmOn_7h_AvKoi2Ebsw853oJBsBgrrUBb52NS2TwPqtON6fT6-X4Y1KKf0yICLqkTpGg1RXA1gjzFLTQ5PfT2K60TYJjZ_-nFbIYFU76FqTafW4SJ4gB_F30jCBCp_11C6LhvQ3xkTxloDCICOmTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مردان روزهای جنگ دوباره به میدان آمدند
@Farsna</div>
<div class="tg-footer">👁️ 7.13K · <a href="https://t.me/farsna/462066" target="_blank">📅 21:02 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462065">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/384d8d2925.mp4?token=cMTDQv5jcdZ4kcBIAKBOtGy5NUIiApMDHSn7LID0Dzj1N2RkvvLZdcxDrvX5yaLJu4u-dKZDkN_onHy1LH4_Ec0Lkm7SQc6OLv8ydTPEZ3_o1bMOBed_p5gEbbBR6oZIJgO3UAXmrfcfxc62CFMhIW5cS7W4pSXORcu4Xe_vuKgtCGpV66MqvjIxgKgfCMopKF1nzwpZoJwzvjCqc6C9b0LRwXwAGBAyqBbmitHyJYuuA2gahO6uITXMlOm8kX5lNKyTbjcR6Z_e3T6eqeUuY1zXSsX2q7cY8bj7QFlx5KhEAxvzpVKxaph_2VipkCyTSvp91Iw5Odwfa1HSKA5Avg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/384d8d2925.mp4?token=cMTDQv5jcdZ4kcBIAKBOtGy5NUIiApMDHSn7LID0Dzj1N2RkvvLZdcxDrvX5yaLJu4u-dKZDkN_onHy1LH4_Ec0Lkm7SQc6OLv8ydTPEZ3_o1bMOBed_p5gEbbBR6oZIJgO3UAXmrfcfxc62CFMhIW5cS7W4pSXORcu4Xe_vuKgtCGpV66MqvjIxgKgfCMopKF1nzwpZoJwzvjCqc6C9b0LRwXwAGBAyqBbmitHyJYuuA2gahO6uITXMlOm8kX5lNKyTbjcR6Z_e3T6eqeUuY1zXSsX2q7cY8bj7QFlx5KhEAxvzpVKxaph_2VipkCyTSvp91Iw5Odwfa1HSKA5Avg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر دادگستری: کارگروهی تشکیل شده که اختلافات بین دولت و قوه قضائیه در آن حل شود و رسانه‌ای نشود  @Farsna</div>
<div class="tg-footer">👁️ 7.07K · <a href="https://t.me/farsna/462065" target="_blank">📅 21:00 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462064">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jBw37ZZXt7MwjvACScKmrhmRLoG2WXAR4TWOy34JWCfGamBmJn3MkHiQ-xutv6o9Fnn05Vx9KDELsiskX8EOldsFFVCQMWSQq_tcjYG2xHfhTHDw6s4B3kf-9eDSoJ9IdisKk_x3wauwG8GTZPZC2nDmQg_rwdQcyXhzLbaMfPRm-cltH9zZ66YJN73b978X8r0ngJA35sDrRBGFRacaQmn-bqfKd7FwdpxglJtLH37AzplkvKHCQUfFzbGj12-78peSzIpe4p8qHHASFqRRvGsQebKTzoSoGT057YS0THL_kpav7bvOunhC6x64ACCWqTrEpAVauOyM-nxPjo6OIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: نشست ایران و کشورهای منطقه به‌درخواست عربستان به‌تعویق افتاد.  @Farsna</div>
<div class="tg-footer">👁️ 7.59K · <a href="https://t.me/farsna/462064" target="_blank">📅 20:57 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462063">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">‌
🔴
منابع یمنی: منطقۀ المخا هدف ۳ حملۀ جنگنده‌های دشمن سعودی قرار گرفت.
🔹
همچنین در حملۀ عربستان به یک پل، دو غیرنظامی کشته و یک نفر زخمی شد. @Farsna</div>
<div class="tg-footer">👁️ 6.82K · <a href="https://t.me/farsna/462063" target="_blank">📅 20:51 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462062">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M-a7WR-UGDA8Hy0hzGjmLGc_jOg0j6BhaU9TvZFB-XZAX38N4M7RuwPlx4T3PdHXk-GJV5r7g-Mo31wv5qo6T1G3Kq3nkYSdio75bDBTVGco4wGfRekgKFWyA0RzP1I4ubWwmnzS70aZnCQXob4dLfgfUp59gTnEfubFoNqEdBPBsWTqqhSTFcvE3Addss9ycMcpB2IFRNkV6lzUx3XF5Mowxy4fB2nC7nJTxIew3t0KCuD7IWs1sHM2oeOUWUvlirgoTdE9eaD0Opn-_87ZpdVZ_xL7qEfkfMZHu9iEr3qxCjNpeihFyAyNfE8hWMDPD12oW4AuBns1GVMeEE7nxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آموزش و سازماندهی ۱۰۰۰ گردان جان‌فدا آغاز می‌شود
🔹
اطلاعیهٔ شماره یک قرارگاه مردمی جان فدای ایران: پس‌از شکل‌گیری ظرفیت عظیم پویش جان‌فدا که تحسین دوست و تحیر دشمن را رقم زد و با توجه به استقبال بی نظیر و پیگیری مدام مردم برای قرارگرفتن در کنار نیروهای مسلح…</div>
<div class="tg-footer">👁️ 7.48K · <a href="https://t.me/farsna/462062" target="_blank">📅 20:50 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462061">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61bd07adf1.mp4?token=D3ISSAq2gTLC_RrT1rGe4zPDVYe7guQARNjmZf2qdJWpvlgy2Zkm_cBlTD3-SoSoEN_05qIcxMUlci6ky-50RR3WtoLItTIDIGWkOuFyV2_knyW7zbxjy5C61QHOmLhzSjvdEcvopSErd0V1CUrpjJ4ajhPTb4AeTlu9xtIDtiyQnq9oQaaSMmhFeGjSionpgOKzSbkaO0ELhxMz6KKCS4pqhZkBwY1Gdp12gkr4870X_ZiYO135oJris5Uc9OylcPSRXJUC6Z4TIQ1A8bX7icxIx6G71g5Ei8AsYEcpAe2-XZUwai7X0fkAhIw34APK5QCQBewWQSG90_CFfHdDCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61bd07adf1.mp4?token=D3ISSAq2gTLC_RrT1rGe4zPDVYe7guQARNjmZf2qdJWpvlgy2Zkm_cBlTD3-SoSoEN_05qIcxMUlci6ky-50RR3WtoLItTIDIGWkOuFyV2_knyW7zbxjy5C61QHOmLhzSjvdEcvopSErd0V1CUrpjJ4ajhPTb4AeTlu9xtIDtiyQnq9oQaaSMmhFeGjSionpgOKzSbkaO0ELhxMz6KKCS4pqhZkBwY1Gdp12gkr4870X_ZiYO135oJris5Uc9OylcPSRXJUC6Z4TIQ1A8bX7icxIx6G71g5Ei8AsYEcpAe2-XZUwai7X0fkAhIw34APK5QCQBewWQSG90_CFfHdDCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خائنین خارجی زیر ذره‌بین سامانهٔ علاج
@Farsna</div>
<div class="tg-footer">👁️ 7.57K · <a href="https://t.me/farsna/462061" target="_blank">📅 20:44 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462060">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01d6ec6c4d.mp4?token=hp-kTB8bd69v6N01h3zB_nisFvcet7pwp9q_DryJcWQTq0MvB9Wr1qx5aG8AWiR-PZ3iCol5Mh12-vdyaf8cSVYWAaKdVSOr5SqtgNbNtzuUlhz2lzJ96P8LFSTSXY_lrdBdExZgDyLOe6VoTwdc6DpwQmVmS6api1Zm2CiirOTGnXOZnXBrQq0ZnJ85bW_FKQHc6pmqCzgV7ip6A5JSYUyXy-YTc5wWajbfgtAx478hHGBwrBcqQwOHGqwL27cgHChwydi7shbmHRhBjBOJtu4cWjwwOxfH_jWFDx5vAs9bOjjTpBLbjeuul7bcRAckIompwVXNKoBbIhsZ3seJ0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01d6ec6c4d.mp4?token=hp-kTB8bd69v6N01h3zB_nisFvcet7pwp9q_DryJcWQTq0MvB9Wr1qx5aG8AWiR-PZ3iCol5Mh12-vdyaf8cSVYWAaKdVSOr5SqtgNbNtzuUlhz2lzJ96P8LFSTSXY_lrdBdExZgDyLOe6VoTwdc6DpwQmVmS6api1Zm2CiirOTGnXOZnXBrQq0ZnJ85bW_FKQHc6pmqCzgV7ip6A5JSYUyXy-YTc5wWajbfgtAx478hHGBwrBcqQwOHGqwL27cgHChwydi7shbmHRhBjBOJtu4cWjwwOxfH_jWFDx5vAs9bOjjTpBLbjeuul7bcRAckIompwVXNKoBbIhsZ3seJ0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خاندوزی: هرمز را به اهرم قدرت منطقه‌ای ایران تبدیل کنیم
🔹
وزیر اقتصاد دولت سیزدهم: مسئلهٔ تنگهٔ هرمز را نباید صرفاً با محاسبه عایدات اقتصادی و مالی آن سنجید، چراکه مدیریت این تنگه می‌تواند یکی از مؤلفه‌های مهم در بازتعریف مناسبات اقتصادی، تحریمی، سیاسی و ژئوپلیتیک ایران با کشورهای منطقه باشد.
🔹
ایران می‌تواند به جای آنکه مدیریت تنگهٔ هرمز را صرفاً یک مسئله اقتصادی تلقی کند، شرکای راهبردی خود را در این موضوع مشارکت دهد و آنها را در قدرت جدید منطقه‌ای ایران سهیم کند.
🔹
تنگهٔ هرمز می‌تواند به یکی از نقاط آینده‌ساز برای ایران تبدیل شود و نحوهٔ مدیریت آن، در کنار استفاده از ظرفیت شرکای راهبردی، می‌تواند بر جایگاه منطقه‌ای و مناسبات اقتصادی و ژئوپلیتیک کشور اثرگذار باشد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.14K · <a href="https://t.me/farsna/462060" target="_blank">📅 20:40 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462059">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LTYIbb7MYBCwZbp1yWSHh4WYQ3G0xp_XNqrRVxFXNSz31TH_Wcmqq-wvZhttj3PsvJF_Zh2td82JIl8sJOrGQZCr8BBiR0Xc04MBn_AZ1aviwR36oYr7RqId49-NBb9756Xy_Tcs4cIFCIffwlyTJskcdQcDtfvqZLorumLUgqqXQgfhRd-knNcIIbXlJCLJlxkhckXciPQx8j7a2VIsZfxECtsZHrRH9WuVVVMxtz4qjTYWePljxBXV0g0UlEKav9kAFNNqn3YsUwcaeyXoXJfOwCQ2hq0WtSADMaKnG2qE6XfK1_hZ-kJTqYxd0fjUJ8fOyoSdsfSa6cV5Jg-f4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا به‌دنبال خبرچین برای شناسایی مسیرهای اقتصادی ایران
🔹
وزیر خزانه‌داری آمریکا با صدور فراخوانی از افشاگران خواست اطلاعات خود را دربارۀ مسیرهای اقتصادی و مالی ایران در اختیار واشنگتن قرار دهند.
🔹
بسنت خطاب افرادی که اطلاعاتی درباره خطوط مالی ایران دارند گفت: اگر اطلاعات قابل‌اقدامی برای خزانه‌داری دارید، ممکن است واجد شرایط دریافت پاداش باشید، فرقی نمی‌کند کجا زندگی می‌کنید یا حقوق‌بگیر چه کسی هستید.
🔸
آمریکا در ماه‌های اخیر تلاش می‌کند همزمان با ادامه جنگ، با شناسایی و قطع مسیرهای مالی فشارهای اقتصادی خود بر ایران را افزایش بدهد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.76K · <a href="https://t.me/farsna/462059" target="_blank">📅 20:29 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462058">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GacweDYyXTpD0Bnjkv5hnzMwf_OnlsIHDxsuqwattB9-vpprFmilC86H00_0Ab0KdpFn1jiR_f_TpgloH5mNyJt_uIYcYtDOFE9hblHDYsXyt0hMCNftyCTcVJf4791U2Y6UvMlWg30q3RYeqx0StGdcbM4r6m46KIpNwnKJoKUdm8vFVm04k2j0P8yKD3NYsAh0xLanImirc9EiPJ74ejY4PXFxoKBp2GsPYlohRv3im8Nh3gBBG9KTENFJsODNwEprXhJ1hLVwTfsKKhD1c2BnmJhBPnG9er-YJd8ZBghSZFB0LCTcHAre5dLuJ4UegJ_oUK2SW8hX7u1Ijr1JKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تقدیر بنیاد ملی نخبگان از دانش‌آموزی که جایزه البرز را به بازسازی مدارس طرح میناب اختصاص داد
🔹
سعید خدایگان، قائم‌مقام بنیاد ملی نخبگان، در سفر به مشهد مقدس با حضور در جمع خانواده نیایش امیرپرست، از این دانش‌آموز برگزیده جایزه البرز ۱۴۰۴ تقدیر کرد.
🔹
نیایش امیرپرست که موفق به کسب جایزه البرز امسال شده،
تمام مبلغ جایزه نقدی خود را به پویش «فرشتگان میناب» اهدا کرده است
تا این مبلغ برای بازسازی مدارس آسیب‌دیده در جریان جنگ رمضان هزینه شود.
🔹
خدایگان در این دیدار با اشاره به اقدام ارزشمند نیایش امیر سرپرست، بر اهمیت مسئولیت‌پذیری اجتماعی استعدادهای برتر کشور تأکید کرد و آن را نمونه‌ای از پیوند موفقیت علمی با خدمت به جامعه دانست.
🔹
در پایان این دیدار، هدیه و پیام تقدیر دکتر حسین افشین، رئیس بنیاد ملی نخبگان، به ایشان اهدا شد.
@Farsna</div>
<div class="tg-footer">👁️ 7.26K · <a href="https://t.me/farsna/462058" target="_blank">📅 20:27 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462057">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromرفاه خبر</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VmQOXsNmxSqnIEDgKKfnQMO1SGhGD6CLfepYi5dc4I3wlBNt2Y1H9VJFE4zP45A780H9rTsAV4nU7gX3S736wluqIg8CXPU8RM_zseuZ40yW-_TyjBGcbUk5_L5hXwPUmGPBV0kniDiflfG01sSuXsXD0lm4L0X1-EkTnSUcjtSI6owehGA4EzktJGhgjOFeAj6RoMus-OmnpZEFBjdTr1RemHWdJJl50t_mB_zNZoKyKfGjyfXioms3PmUyYecmCsLn4bK7qdQS5A4YpUeCqHsHktDb1tTaNdvc9SKpnAJHOel0XA0NanGoVuJ2HjaGYpiTe2jRxpc3wTijLqoAYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌐
رونمایی از طرح ملی «زرین‌تأمین» بانک رفاه کارگران با حضور رئیس جمهور
🔹️
طی مراسمی با حضور رئیس‌جمهور، وزیر تعاون، کار و رفاه اجتماعی، سرپرست سازمان تامین اجتماعی، مدیرعامل بانک رفاه کارگران و جمعی از بازنشستگان، طرح ملی «زرین‌تأمین» با حمایت و نقش‌آفرینی راهبردی این بانک رونمایی شد.
🔹️
رونمایی این طرح به‌عنوان الگویی نوین برای تأمین مالی سالم، مولد و غیرتورمی با ابتکار و راهبری بانک رفاه و با همکاری سازمان تأمین اجتماعی و شرکت سرمایه‌گذاری تأمین اجتماعی (شستا) آغاز شد تا ظرفیت‌های واقعی و مولد بخش طلا را به پشتوانه‌ای برای تأمین مالی پایدار تبدیل کند.
🔹️
علاقه‌مندان می‌توانند برای آگاهی از اطلاعات کامل طرح زرین‌تأمین و نحوه مشارکت در آن به نشانی اینترنتی
refah.zarrintamin.ir
مراجعه کنند.
🔗
متن کامل خبر...
@refahkhabar
| بانک رفاه کارگران</div>
<div class="tg-footer">👁️ 6.72K · <a href="https://t.me/farsna/462057" target="_blank">📅 20:25 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462056">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-footer">👁️ 6.43K · <a href="https://t.me/farsna/462056" target="_blank">📅 20:25 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462053">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QdXcc9fjVI5FWmsy6J1-HJ2lSQuKQH-euBnMQCHeM8-YD02YNjaGFf_RMk3pe-qpnXv-UsOgdFF9TOuqKqA5WKT49xaBXzGrEJYy_y8uN3ebKgQogiDOuvdTxjwBGuohW2Ch9qrTZXiXFU_0KY1p7ZU2jXove33mPbAl6d_4I8MljfTsKkZTM8Hf430LHOMXJvMLE4ohL4USAozFcxy993711hWRCy4OdG1D8KaCsA56CPYLVQA9DHggt61q9TD4GFruDyxoQDN2MM1xvrT1c0qrzbPOwav45M-gxOjLYv8Lykjm0AH3BFiYqY4uE0kY8jSfK0GVOJGlN9BRqpD3Tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوباره نفت گران شد و ترامپ یاد توافق با ایران افتاد
🔹
هم‌زمان با نزدیک‌شدن قیمت نفت به ۱۱۰ دلار، ترامپ باز هم در پستی در تروث سوشال از توافق با ایران نوشت.
🔹
تاکنون ۶ بار پس از افزایش قیمت نفت در بازارهای جهانی ترامپ محتوایی با مضمون مذاکره و توافق با ایران…</div>
<div class="tg-footer">👁️ 9.04K · <a href="https://t.me/farsna/462053" target="_blank">📅 20:22 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462052">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ee4acbd6b.mp4?token=cjKOf__tHZ9SyakOYDpc-5Auo8weC9hTe_T2LNfFe0jd5CRtPzqyhcHq_GX6ng9VKyznzh9sCYC-y8fDf2p6p4a6PEEzcuVVhcIlWxVAtJyLF5UurdVJHRy1ac0RwbudA9odRhSmN0VFRHSLIEueyeEkTX_Lz3uOxk9Xeg-fN8JYuxbmc8uQPUcyk_eN0-tsYeTuWOL3X3LhXgiRRw5PMm30jFEXhz1xHBfiY7eGhoNZinYIQhLCCaKBhKPYCrvdGKKKR0eCIDNJ6Ru1cpdFPH4I1cs9ltdewiz0KnfmAkkiURdZ8tffTt9o77i9js0ZUptLMlGxNqTaftaB1eviaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ee4acbd6b.mp4?token=cjKOf__tHZ9SyakOYDpc-5Auo8weC9hTe_T2LNfFe0jd5CRtPzqyhcHq_GX6ng9VKyznzh9sCYC-y8fDf2p6p4a6PEEzcuVVhcIlWxVAtJyLF5UurdVJHRy1ac0RwbudA9odRhSmN0VFRHSLIEueyeEkTX_Lz3uOxk9Xeg-fN8JYuxbmc8uQPUcyk_eN0-tsYeTuWOL3X3LhXgiRRw5PMm30jFEXhz1xHBfiY7eGhoNZinYIQhLCCaKBhKPYCrvdGKKKR0eCIDNJ6Ru1cpdFPH4I1cs9ltdewiz0KnfmAkkiURdZ8tffTt9o77i9js0ZUptLMlGxNqTaftaB1eviaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مهار آتش‌سوزی در واحد تولید روغن شهرک صنعتی طبس
🔹
جانشین استاندار خراسان جنوبی: غروب امروز، یکی از مخزن‌های این واحد در اثر اختلال حین تخلیه روغن از مخازن، دچار آتش‌سوزی شد.
🔹
این حادثه تاکنون خسارت جانی نداشته و آتش با تلاش نیروهای امدادی، به‌ویژه آتش‌نشانان فرودگاه طبس، مهار شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.83K · <a href="https://t.me/farsna/462052" target="_blank">📅 20:18 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462051">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f7f610b582.mp4?token=Th4BU71_CGLHOWyYI2JFfQll2QV2aSkjGqC9DJ1ZkZG1Q_KvlIaJxToVs7KRo8SFs-_R1wdREY1fL_JlIX5Ffe_Tz-cZc2hg0UeOWAi6IiLPDhaiMkfpxDUd9opAAxXmT7qo-kCImlzzZHPpDenTZx9E-1cOazgrgAGu2xifikgj2BeUQNqRWNsSumKz_RNXgVGpLXWGReJ6dXv417I6Oq7RybIfJA6ie0tDnkX5mboArHc0dOaatS079HOzJ_hvDIU8ha70iOL361lyPfkwqA83fP-F9VHb4n90-saDhHhtxuqpIjL6VGNikz9BVtomnvC862u0Crpsi2bjWSivkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f7f610b582.mp4?token=Th4BU71_CGLHOWyYI2JFfQll2QV2aSkjGqC9DJ1ZkZG1Q_KvlIaJxToVs7KRo8SFs-_R1wdREY1fL_JlIX5Ffe_Tz-cZc2hg0UeOWAi6IiLPDhaiMkfpxDUd9opAAxXmT7qo-kCImlzzZHPpDenTZx9E-1cOazgrgAGu2xifikgj2BeUQNqRWNsSumKz_RNXgVGpLXWGReJ6dXv417I6Oq7RybIfJA6ie0tDnkX5mboArHc0dOaatS079HOzJ_hvDIU8ha70iOL361lyPfkwqA83fP-F9VHb4n90-saDhHhtxuqpIjL6VGNikz9BVtomnvC862u0Crpsi2bjWSivkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گنج‌یابان زیر پای سنگ‌نگارۀ اشکانی را خالی کردند
🔹
چند روز پیش یک
کوهنورد
در مسیر قلۀ یخچال همدان، متوجه حفاری در پای یک سنگ‌نگاره ثبت‌ملی دوره اشکانی شد؛ حفاری‌ای که احتمالاً با تصور پیدا کردن گنج انجام شده است.
🔹
حالا بررسی کارشناسان نشان داده حدود ۱.۵ تا ۲ متر از پای تخته‌سنگ به‌صورت دستی کنده شده اما سنگ‌نگاره آسیبی ندیده است.
🔹
این سنگ‌نگاره با وجود ثبت ملی، در ارتفاعات و بدون حفاظت دائمی قرار دارد.
🔹
این باور غلط که سنگ‌نگاره‌ها نشانه وجود گنج هستند، عامل چنین حفاری‌هایی است؛ درحالی‌که این آثار تاریخی خالی از گنج‌اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.61K · <a href="https://t.me/farsna/462051" target="_blank">📅 20:13 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462050">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a4de0dfdf.mp4?token=H7RFskjoYX0L8jQBRGkBG5885IOyZIznvhrDF7zjt5AZRqb_J7w7QnkB5VtKpFwg7cWUXpmGloZMqXKQOeNAM_rv8B5TQP3A8QHqVVP9IWa4RTV7FReOWGYr57JZ5OqbsC_EBERZCqcRP1U7_dgihIkEVsRDF6GuSriD2blQ7ChTLc_sZgUor8dFxml4zEgiQ7oQeAdgsoHhfqy0Al6237507UCcDe1AeVPibkektsFvRRd5_zYA6elM_szU5L85xRLrTu8ZqlLw2K8VMm_LPbSN0X2rPGNV585vOVeHpFOYQ3IYi3aePG2ft3o2DTyGHQrQ3UOhfB6TlM9nB1mJdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a4de0dfdf.mp4?token=H7RFskjoYX0L8jQBRGkBG5885IOyZIznvhrDF7zjt5AZRqb_J7w7QnkB5VtKpFwg7cWUXpmGloZMqXKQOeNAM_rv8B5TQP3A8QHqVVP9IWa4RTV7FReOWGYr57JZ5OqbsC_EBERZCqcRP1U7_dgihIkEVsRDF6GuSriD2blQ7ChTLc_sZgUor8dFxml4zEgiQ7oQeAdgsoHhfqy0Al6237507UCcDe1AeVPibkektsFvRRd5_zYA6elM_szU5L85xRLrTu8ZqlLw2K8VMm_LPbSN0X2rPGNV585vOVeHpFOYQ3IYi3aePG2ft3o2DTyGHQrQ3UOhfB6TlM9nB1mJdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گل اول الاهلی به تراکتور توسط سزار روی اشتباه خلیل‌زاده
⚽️
شباب الاهلی ۱ - ۰ تراکتور
@Farsna</div>
<div class="tg-footer">👁️ 7.95K · <a href="https://t.me/farsna/462050" target="_blank">📅 20:00 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462048">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JeAgCgbpUKFQ-WNHweunY03z-sVtn-ZTeJP5PzKgv_k9snvejjMnTUdhg2ORJx2VLKwZnabt2yvNpR4YnQNcONSlQtpvP_8HQ3RMhLLNPUOOajzjw73_5fSBbWxWpeMg-VXsYEHucKj4Wb0UohjM6SmtdzuhMxT3KcGpJjpu2HadGtWZKNilvyxtWjPltoxaYdM4uTCZLlZsEqCM1z79Lhi4aYtJLFKdm2Smn6kk5nJULCxkHw1oMyRiYp2fvKRWT9Z_QacM9LYVCnCWbnMUr8DOQyR8ejvGrvu3qmLW0pK1YpBoxvL-ecxJpJXvRSeDEhYUp-IcW7w-PMbnXYUBxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عارف: هیچ کالایی نیست که نتوانیم وارد کشور کنیم
🔹
درست است که دشمن با ایجاد محاصرۀ اقتصادی مشکلاتی ایجاد کرده، اما هیچ کالایی نیست که ما قادر نباشیم آن را وارد کشور کنیم.
🔹
اکنون برای تأمین نیازهای کشور، سایر مسیرها و کریدورهای مختلفی برای تجارت را نیز فعال کرده‌ایم.
🔹
دولت در تلاش است با ایجاد ثبات نسبی اقتصادی، کاهش هزینه‌های واردات و صادرات و تأمین معیشت مردم، آثار فشارهای دشمن را مدیریت کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.58K · <a href="https://t.me/farsna/462048" target="_blank">📅 19:56 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462041">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/o60hDTaXMRCT_vBmMORcK9v7ns7lODXyJi_VkI-3gybfuM97btmpKfZQOrt01Fe3cP0LXq60XZVATvb2NZ2MrppvurpJ3CcqcwH_7QaAZscWTzU0GRq-83lYKykex-Kg-Kif7sm2sERDs3Y_ZXqSiruFni9TMovjRgcU6_VfhRb-WEjWdO5HomA0sMMCejw_Fu34atwqpgosXIudt8jufYyPuf2KgFzu_6GbiBbHLyGNcHZJXHdQgY4IYn9ITQh1KSDYAySShtLJk3_E-lLMITRAunxJP6KPoq0vHNjn8OhStLPh_pquQGtUUJc1e0W4-JP_WZsIjEaR9kileeK3Eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MsZ3gvpKmRlgniPMsJTYHslKEuqhT1z7QCnoV4qHSlep1WjhMDUVGQClKm1mmQPbGKx-OXB-uiaKYFxGV_RCSoJ8cBjkKsPKAMnMWniRdL-JQNNWtUejelXx-htkxMSD_9zn751neENRyPGusOkxC_yT0acZes9oPzkiU8B7kSITLzc3X3ZZqYbK5NcDpU2IZ04H8QNQFUjMhDJFBBe_hbS5L4bLct5UMrk85UvOgrfHEJFwCx3vxrQ9s162LOLo84SNSGA8Fx8pz9YsUtmSvo0bIl4zi922ynf7dHz1yGMh5cuufoVvsQ6mil9A6TaulY15RYwJvaoUscQO_vO9rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/onlmhX2LAc1dvI9IjWJrCT2M7lKDT67ayz3_kH65UIkfnWenfVbC5n5Nw1fWRAfRFxeHMpVmBas8yI4_10ujGBcM0PaM_8bZvVrYIWsvJ1WS0Duf3E8_g_cPGGdptn76_b4gQndSEosCLMq58VlbkTXoaPxgHUxhlRO0uoTIf1z2HukL8weqRbnTvSlELQ8R8OQWmnj23bLFWyI-j2kL-mqu3P869qlu4W40DF01VYHMRmGmaguzuDbimBrk4JJfgwaJq8DCJ27O2vMzS-aTz_kcr_a7TIbbgCDH6yLb9W-dn8ind1JgMOX3MxP9WoQvbF1G-unSX1ILW9e6bHrdfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Rq5oaE0xfF0tDtv1YTKNlTZcIeRuvgMEMnnGxDSxY24EtN3A0SnReXQNjeW7OTOtTeDbrAQoMLseqgJhnUK4bap_uoTb6-TFdc91VWjOL9LtFQJEYeLQ5M6L5NGaZb0Lzt4HL25mxw3W8BveNfggmu3pKqtzRiS1OZ0ytI3t0kehGVLidjD1sXb3hRnJBiwOpI6pKf15LX4qwYZnCbruMogFlFtr31CsJ9r85KDlbdKZt3tLJPhPSTok6eD5vRVAKHgHwm_Rg0hU-LSytyY75ijsqTZ3zIsfgB7qkvNZ99P3423ac9XlvW55LAIJm5qZet2WtBYzX9fKAJCn3xXviw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h2tU6Xz-UkFUyxPGKtPvqkOLO2tXnf4QBMpaYn078AFC2i3bSrsHVTIC1J3vA9czlQCspDV5-oxl2LbF2c_JHpEI9d1h7Fsuz4TXkfgBRZ26wpl1jC0zPIVdOF-YkYa4OojLXTIGPooBc2Myv6phIEqHi2l9aseHbtlIkOnsgJZbzKo48kbS4gw6ruzaS0q9CAmJxMIyLRPl9JxNjNVK01nDqy9TqXMVfHMwoh_mK6MdVKCjmHZE9Gk_miohb0Pva1gaBqsnH5psugHV--lRyn1addPpDes9AYZRxO7ZirbX0SIrHJJoVRxBJobmpFGcHf1xMhP7eezqD3mQAEACMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PdTgf2p9PMMnTIRE2IVjKGtvatiqinavXR8WfX6NWvl46wyknMugsZSJWRh5z7-y2uINk3RR5Z1elcD-EM_GadwHwSpWwJ22H21EuIFfYVtkfEDQPn18op07XESI2z5m-w8akpy15Rn-6Og05vSOwiV6QOlVxPPzhT6nLA7KrTe3roi-s_71kw7Y9KnlvnRQpmy3949W1k_vNajqxH8qoLBjG1no-nro8lqFdbKgHHXnkV4X37X_Cve0cz-JBO0h15s8fQaolnEvY1Px5bJSXQS69_CjRd1VOThp15zs5KbvY1JHqjniUuy57Dfdc6C94W90F3sm14iicy3ZkUObkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DV8qHaAwe_yRZXYQMlPaoGsKgB-upFJcD0syqCdvziAg72kCzHO25IHBSjsR9C1QUpKA8hoGmVMUcfi-sykNPT0qoRrxKWmHdO4F4LKo6Ehv4crKiFu1ydyl8fHizFEls68kzzyU58eWu0bF1pqJtDJXU0pGzYS3nqdT9WQs8Cv0ZX-56j8pVTW7rFPvXFcty_Xpi_dwt9SeD5OmJXmtQm0CBP-4616VY40e5gc1xh9siXLdxCCoA22Y2ulTFv-JFkeeFjbA3TqNRLUO9mPErEf77lkAtYL8sULR9I6QxX0yultOAdPbbvVCOt-T3d6dDpfrHLWZhxQ2IzBimAqz8w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
نمایشگاه عکس آندری استنین ۲۰۲۵
🔹
نمایشگاه آثار برندگان مسابقه عکاسی «آندری استنین، عکاس روسی» در گالری خانه عکاسان حوزه هنری افتتاح شد.
عکس:
محمدمهدی دهقانی
@Farsna</div>
<div class="tg-footer">👁️ 8.78K · <a href="https://t.me/farsna/462041" target="_blank">📅 19:52 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462040">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dJK9iDUpj9dka0K5amFnHrmd4Z0P8leTdWyAfeTKUXCwHx5cVE3k93n4fD1f7V2ILE1PBxYmaLJScgvIbE22oart5mxfZSCbH5y2ogIxgpLSmb5o104b2vR7McAq6LSRXBEMIlQITT5tvhcdnP4Yg8Uzik76eP2mVWVPmJYikYBn7NKzj2VdnLl7--aRUCQmKxSOhfaY8QYQY2F_QSDAl48MruuFlt07IpnmUlbSJgnPN_Adg2jjaSsD5KQVt8y_DE_w4Oj06l5ToJ3H2zWK7E5pC8ijm3-YR4_t63WgFbC6CH666TovoOskB-vtyP2QFWuRefP_H_LPlezCweyxUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
ادعای جدید ترامپ: قیمت جهانی گازوئیل به‌خاطر جنگ روسیه و اوکراین گران شده نه ایران
🔹
رئیس‌جمهور آمریکا: اوکراین موافقت کرده که به اهداف انرژی روسیه حمله نکند. روسیه نیز موافقت کرده که متقابلاً همین کار را انجام دهد! افزایش قیمت جهانی دیزل عمدتاً ناشی از…</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/462040" target="_blank">📅 19:32 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462039">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1cd61e6998.mp4?token=k3A2qE5JXiS0xuXtZxUHcPFfAJRNrUreVtUu8HVMpWxojPqUNvDWgkdrYQbxFaQDBQV8sG4zA3PioOKxqh1jND_7rv-BfEbRdBWPAvpIxQwihocAqLyb4Lq3phVJwznB4CBftrpailGLVonI4GrBsKzoDOHnMglQIGThIhpvS2UtoDF70dAEmOfC6S-VQ7RZIeh2DMxESwVJbV1ssoQix1JD_c-1nwE3La4kzicjzLIX9R-mqxk3mKncn4OR8tZ_gVCxxG_yRJvjUr8nUq20fT6wAEIphlGjKi_MForyAR6Dolt8UCD5u97iWVmWBDcXWHNw-6E-Kt19x65PzihQng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1cd61e6998.mp4?token=k3A2qE5JXiS0xuXtZxUHcPFfAJRNrUreVtUu8HVMpWxojPqUNvDWgkdrYQbxFaQDBQV8sG4zA3PioOKxqh1jND_7rv-BfEbRdBWPAvpIxQwihocAqLyb4Lq3phVJwznB4CBftrpailGLVonI4GrBsKzoDOHnMglQIGThIhpvS2UtoDF70dAEmOfC6S-VQ7RZIeh2DMxESwVJbV1ssoQix1JD_c-1nwE3La4kzicjzLIX9R-mqxk3mKncn4OR8tZ_gVCxxG_yRJvjUr8nUq20fT6wAEIphlGjKi_MForyAR6Dolt8UCD5u97iWVmWBDcXWHNw-6E-Kt19x65PzihQng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر دادگستری: کارگروهی تشکیل شده که اختلافات بین دولت و قوه قضائیه در آن حل شود و رسانه‌ای نشود
@Farsna</div>
<div class="tg-footer">👁️ 8.92K · <a href="https://t.me/farsna/462039" target="_blank">📅 19:30 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462038">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">شیوۀ تصمیم‌گیری دربارۀ تعطیلی مدارس تغییر کرد
🔹
وزیر آموزش‌وپرورش: در دولت تصویب شده آموزش‌وپرورش مرجع تصمیم‌گیری دربارۀ تعطیلی مدارس باشد و شاخص‌های مشخصی نیز برای این تصمیم‌گیری تعیین شود.
🔹
در بسیاری از کشورها در مواجهه با آلودگی هوا، سرما، گرما، بیماری‌های واگیر و بحران‌ها، به‌جای تعطیلی کامل مدارس، تلاش می‌شود با مدیریت شرایط، روند آموزش ادامه پیدا کند.
@Farsna</div>
<div class="tg-footer">👁️ 9.62K · <a href="https://t.me/farsna/462038" target="_blank">📅 19:24 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462037">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🖼
عضو ارشد انصارالله یمن: هرگونه حملۀ عربستان به زیرساخت شهرهای یمنی آزادشده، با پاسخ متقابل مواجه خواهد شد
🔸
نیروی هوایی عربستان در ساعات گذشته به فرودگاه بندر المخا، شهری که روز گذشته به دست نیروهای یمنی آزاد شد حمله کرد. @Farsna</div>
<div class="tg-footer">👁️ 9.18K · <a href="https://t.me/farsna/462037" target="_blank">📅 19:22 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462035">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SB7B-ypsrQGNowz2pvOjs3PMFykMLN_FBqo4DbLA9h61TGEYCHD9wwTRckSAbzlpt9_ToatqTqSjVo7bAKXZGNfpa8u0u-3Jbkexx0dVoBnpoC0kxJLxWd0Nr7U2BUSuvlNL8UmYtRvE-Gq_J9jTOjVnOSd-3T59EDT0Wuc3mRmEFQ7dH7d5ynlcmiRTHx2fY57kME5drcrIFXDOMaifMDZko3go_CljcolZp-HKzPU5yHPH3aoFaj-leRLKAcDlw2gczW1FKZqbOWN9ZImKG9KL2XY3npCD79GVUA5G5dKLxqrEtC0Be_M3is58IaPZZNbILR3j9D7bXBfYfem-dA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
قالیباف در پاسخ به خیال‌پردازی‌های بسنت دربارهٔ نفت ۴۰ دلاری: قبل از ارتفاع گرفتن، حسابی گرم کن!
🔹
نرخ گازوئیل آمریکا به «بالاترین نرخ تاریخ» رسیده است، وقتشه یه فکری کنی!
🔹
ژاپن که بزرگترین دارندهٔ اوراق قرضه آمریکاست در حال فروختن اوراق با حجم بالاست؛…</div>
<div class="tg-footer">👁️ 9.18K · <a href="https://t.me/farsna/462035" target="_blank">📅 19:16 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462033">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65b2cc5e81.mp4?token=U2p9NGlAh2f_SZ6zVf1uOqtAoHDafkZ6uIVsIW-uBCtCFT_jnJgsT910xFNucqrBKpm5ALM0Wq1BIy5A0CZmyUW6zfWQTJ5kjA-lGALin6YEMbO80b9UNfBPdnLSizKo2JZoaabJSScL2-WpmR-pLWLvsTLABiEfFVIvqTSsKZHadAxJWQX1NJZAwKFzAzOvniH2kDPNP8ATwl9MXp5pG8lNnwYbcfJdip3AaIwdgA7GHWEspDot2xlrYgHqLlI2VIACrIZpz6lxg1XbJPAJSzX4pvG1cqMgLrfjNMsHBYjURHfavcZAuxl192xU5dzT3H4NTNUMOI2G_WCwdmhKZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65b2cc5e81.mp4?token=U2p9NGlAh2f_SZ6zVf1uOqtAoHDafkZ6uIVsIW-uBCtCFT_jnJgsT910xFNucqrBKpm5ALM0Wq1BIy5A0CZmyUW6zfWQTJ5kjA-lGALin6YEMbO80b9UNfBPdnLSizKo2JZoaabJSScL2-WpmR-pLWLvsTLABiEfFVIvqTSsKZHadAxJWQX1NJZAwKFzAzOvniH2kDPNP8ATwl9MXp5pG8lNnwYbcfJdip3AaIwdgA7GHWEspDot2xlrYgHqLlI2VIACrIZpz6lxg1XbJPAJSzX4pvG1cqMgLrfjNMsHBYjURHfavcZAuxl192xU5dzT3H4NTNUMOI2G_WCwdmhKZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سامانۀ شناسایی و برخورد با خائنان خارج‌نشین آغاز به کار کرد
🔹
سامانۀ رصدی و اطلاعاتی «علاج» با هدف شناسایی و پیگیری افرادی که از خارج کشور علیه منافع و امنیت ایران فعالیت می‌کنند، آغاز به کار کرد.
🔹
در معرفی این سامانه آمده که «علاج» با هدف پاسداری از امنیت ملی و منافع مردم ایران در برابر جریان‌های ضدایرانی، تجزیه‌طلب و مروجان تحریم و حمله نظامی فعالیت می‌کند.
🔹
براساس اعلام این سامانه، پیگیری حقوقی و محدودسازی دسترسی‌های مالی و رسانه‌ای افراد متخلف، با تکیه بر پایش مستمر و هوشمند انجام خواهد شد.
🔹
«علاج» همچنین از مردم خواسته اطلاعات مربوط به این افراد را از طریق وب‌سایت
alajgroup.ir
یا نشانی
@alajgroup
در پیام‌رسان بله و
@AlajGroup4
در تلگرام ارسال کنند.
🔹
هویت گزارش‌دهندگان و منابع مردمی محرمانه و رمزنگاری‌شده باقی خواهد ماند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/462033" target="_blank">📅 19:10 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462032">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db0ad9632e.mp4?token=tl_lZwq6SPd4JmGohAHh0eRlRP0NMCVAlrYeAXA9pH3keeXsAeKdHM7bnxNkX2S89Oths48V_zTUGX__1FSHkqyOgT1ToO5Q5pq4NKeTaN7A1serM53uiAWUmYornIUFHMqaTCTokV6jCk428plD5Tc4KjOc2l6rwbVDaMqbAThBXG6hfyLkL4_XecotHhd-pzMAK1HrFNy5IXrcY2Hia5h2u1U46VGiFpgOmWShdjUjnAwAlJwTWu8wA79Y0TePJgC6DmimTh3XPDVi1ve_zlBv1_nHtkM5r9WY4sgmxSy9E1oRsVkT42yudP3oYCV0z50vZbybj45iDrCiPcLHVmjMl3lnCLelsWFPX_hAUFMvR46GLP8n7OQMqLqVGwWpM7RqHFC8OMECns961Nyz6u5BCO3RovKlViBYBS9Fm0o0vT87pHdKhEoA76c-cQUdcfaxPkj75JBTngiJVBxkAsbBz3JGrPOm4cFqdsDGKHsMDK17sEuFPnq2yhA4UzNGGqITVEfYMZSEdZtQymHZgpv-blV_Z9LBXqV4tpqDrEzzcwR2Rl86DcnxF8pK0YQrdXUqOOJSF94TXqQeQvBH8XhKbffcxXpiyEnMRHOW7r_vR2JkQERzRyw7Rf2o-4UDnavdh0Ho7N4s1-72GbsLKIO16BlHthnD7EDn1Zc3DOs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db0ad9632e.mp4?token=tl_lZwq6SPd4JmGohAHh0eRlRP0NMCVAlrYeAXA9pH3keeXsAeKdHM7bnxNkX2S89Oths48V_zTUGX__1FSHkqyOgT1ToO5Q5pq4NKeTaN7A1serM53uiAWUmYornIUFHMqaTCTokV6jCk428plD5Tc4KjOc2l6rwbVDaMqbAThBXG6hfyLkL4_XecotHhd-pzMAK1HrFNy5IXrcY2Hia5h2u1U46VGiFpgOmWShdjUjnAwAlJwTWu8wA79Y0TePJgC6DmimTh3XPDVi1ve_zlBv1_nHtkM5r9WY4sgmxSy9E1oRsVkT42yudP3oYCV0z50vZbybj45iDrCiPcLHVmjMl3lnCLelsWFPX_hAUFMvR46GLP8n7OQMqLqVGwWpM7RqHFC8OMECns961Nyz6u5BCO3RovKlViBYBS9Fm0o0vT87pHdKhEoA76c-cQUdcfaxPkj75JBTngiJVBxkAsbBz3JGrPOm4cFqdsDGKHsMDK17sEuFPnq2yhA4UzNGGqITVEfYMZSEdZtQymHZgpv-blV_Z9LBXqV4tpqDrEzzcwR2Rl86DcnxF8pK0YQrdXUqOOJSF94TXqQeQvBH8XhKbffcxXpiyEnMRHOW7r_vR2JkQERzRyw7Rf2o-4UDnavdh0Ho7N4s1-72GbsLKIO16BlHthnD7EDn1Zc3DOs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رسوایی در قنادی پردیس
🔹
قنادی متخلف در پردیس به‌دلیل گران‌فروشی، عدم درج قیمت و تخلفات بهداشتی با حکم تعزیرات پلمب شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.05K · <a href="https://t.me/farsna/462032" target="_blank">📅 18:59 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462031">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">پیام‌هایی که شما برای فارس فرستادید
🔹
در
خیابان ۱۷ شهریور تهران
، حدفاصل میدان شهدا تا میدان خراسان تعداد زیادی قهوه‌خانه و قلیان‌خانه فعالیت می‌کنند. اگر از این مسیر عبور کنید به‌دلیل بوی شدید قلیان و دود، گاهی واقعاً نیاز به ماسک پیدا می‌کنید. جدا از این موضوع، حضور برخی افراد در اطراف این واحدها باعث شده دختران جوان نتوانند با خیال راحت از مقابل آن‌ها عبور کنند. متأسفانه
بخش زیادی از این مسیر به محل تجمع قلیان‌خانه‌ها و فروشندگان موتورسیکلت تبدیل شده
و وضعیت اجتماعی و شهری خیابان ۱۷ شهریور بسیار نامناسب شده است.
🔹
طبق قانون
بستری کودکان زیر ۷ سال باید در بیمارستان‌ها رایگان باشد
اما این موضوع در
بیمارستان فاطمه زهرا(س) رباط‌کری
م اجرا نمی‌شود و مبالغ زیادی از خانواده‌ها دریافت می‌شود.
🔹
وضعیت
پمپ‌بنزین‌ها در بیرجند
واقعاً افتضاح شده و جایگاه‌ها
به‌شدت شلوغ هستند
. این میزان سهمیه بنزین برای استان‌های جنوبی که فاصله بین شهرهایشان زیاد و هوا نیز گرم است، به‌هیچ‌وجه کفایت نمی‌کند. از طرفی یک سؤال جدی مطرح است؛ چرا کسی که بعد از مدت‌ها توانسته یک خودروی صفر ایرانی خریداری کند باید مجبور باشد برای سوخت از بنزین ۱۰ هزار تومانی استفاده کند؟ حداقل باید سهمیه بنزین یارانه‌ای برای خودروهای صفر و جدید تولید داخل نیز در نظر گرفته شود.
🔹
چرا
آموزش‌وپرورش
که باید زمینۀ پیشرفت فرزندان این کشور را فراهم کند،
حتی در مدارس دولتی از خانواده‌ها هزینه دریافت می‌کند
؟ متأسفانه در برخی مدارس این مبالغ آن‌قدر زیاد است که حتی به نیمی از حقوق یک خانواده می‌رسد. اگر این روند ادامه پیدا کند، در آینده نه‌چندان دور شاهد ترک تحصیل فرزندان خانواده‌های کم‌درآمد یا محدود شدن امکان تحصیل باکیفیت به فرزندان خانواده‌های متمول خواهیم بود.
🔹
لطفاً درباره
عدم تخصیص کارت سوخت به موتورسیکلت‌های بالای ۱۰ سال
ساخت پیگیری کنید. وقتی یک موتورسیکلت از نظر فنی می‌تواند تا ۲۰ سال قابل استفاده باشد، مشخص نیست این تصمیم بر اساس چه کار کارشناسی اتخاذ شده است. با توجه به احتمال افزایش تدریجی قیمت بنزین، تکلیف تعداد زیادی از مالکان این موتورسیکلت‌ها که توان خرید وسیله نقلیه جدید ندارند چیست؟
🔹
من ساکن
قم، پردیسان، بلوار ۲۲ بهمن
، خیابان اشراق هستم. امروز شنبه ۲۱ شهریور، ساعت ۱۰ صبح
بدون هیچ اطلاع قبلی برق را قطع کردند
. در اپلیکیشن «برق من» نیز هیچ اطلاعاتی درباره این خاموشی ثبت نشده بود. چرا برای زندگی و آرامش مردم ارزش قائل نیستید؟ چطور
وزیر نیرو اعلام می‌کند قطعی برق نداریم
، در حالی که مردم بدون اطلاع قبلی با خاموشی مواجه می‌شوند؟
🔹
من یک کارمند هستم و یک خودروی جیلی مدل ۱۳۹۲ یا ۲۰۱۳ دارم. به‌دلیل وارداتی بودن خودرو، سهمیه بنزین نرخ اول و دوم به آن تعلق نمی‌گیرد. ارزش کل خودرو هم کمتر از یک‌ونیم میلیارد تومان است. این خودرو از بسیاری از خودروهای صفر تولید داخل کم‌مصرف‌تر است و آلایندگی قابل‌توجهی هم ندارد. سؤال من این است که آیا واقعاً منصفانه است
صرفاً به‌دلیل وارداتی بودن سهمیه سوخت یارانه‌ای به آن تعلق نگیرد
؟ خواهشمندم مسئولان در این تصمیم بازنگری کنند.
🔹
چرا این‌قدر به مترو و اتوبوس‌های تندرو در
تهران
اهمیت داده می‌شود اما به بهشت زهرا(س) که خودش به یک شهرک بزرگ تبدیل شده، توجه کافی نمی‌شود؟ وقتی مردم از مترو حرم مطهر خارج می‌شوند،
اتوبوس مناسبی برای رفتن به قطعات مختلف بهشت زهرا وجود ندارد
. قبلاً اتوبوس در این مسیر بود اما آن را برداشته‌اند و مردم مجبورند از تاکسی یا مینی‌بوس استفاده کنند.
🔹
لطفا
پیگیر دهک‌بندی‌های غیر عادلانه باشید
. من مستأجرم با یک ماشین ساینا با درآمد کم چرا باید دهک نُه باشم؟
🔹
خودروی بنده KMC ایگل، از تاریخ ۲۳ تیر ۱۴۰۵ در نمایندگی عاکف مشهد متوقف است. حدود دو ماه است که برای رفت‌وآمد به محل کار و جابه‌جایی خانواده، روزانه نزدیک به یک میلیون تومان هزینه می‌کنم. چندین بار این موضوع را به
کرمان موتور
و بم خودرو اعلام کرده‌ام اما متأسفانه پاسخی دریافت نکرده‌ام. انجام
تعهدات پس از فروش و ارائه خدمات مناسب
، به‌ویژه در شرایط اقتصادی فعلی، بخش مهمی از اعتبار یک خودروساز است. لطفاً صدای مشتریان باشید و این موضوع را پیگیری کنید.
🙍‍♂️
شناسۀ ارتباطی ما:
@Fars_ma
@Farsna</div>
<div class="tg-footer">👁️ 9.66K · <a href="https://t.me/farsna/462031" target="_blank">📅 18:52 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462030">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XPmt8f7MJzxsPEMIu6L5zM4HxvpuIDPBwPtNrm9uaXltdekkUy8uBzGmbsoo0Fsbqq7wdQj8Kd-ta9JpmhDKJIzh5387lJdoXyxqCx9p5ZqFvWgA3g_iP3skXyqSqFR6vz3nV2nFXE1RybeM272ij3cVB9HvPlr8O5fBMbJf3hJBWpuKd7Sh9JU9wkINfsQwD3zaspUNi0Pv3RzTGu-vOccalV-cusX8pP5hG4ypzg_u66zq-4PfalmR0LsGFtzirSyR95Uou4hQ7CUKb2S5TWLNkpKVUAyio-AndaGXdN4byWh8u83OsSB4-uMdmjUcSrYrS539lI2604mPLz1kSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اورانیوم‌های مورد علاقهٔ آمریکا در مدینه کشف شد
🔹
وزیر انرژی عربستان از کشف ۱۱۰ میلیون تن سنگ معدن حاوی اورانیوم در منطقهٔ مدینه خبر داد؛ این خبر در حالی اعلام شده که وزیر انرژی آمریکا خبر داد و گفت: برنامه‌ای برای غنی‌سازی اورانیوم در عربستان وجود ندارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.18K · <a href="https://t.me/farsna/462030" target="_blank">📅 18:42 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462029">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b3843af59.mp4?token=nNvRhgnxsFhDsxD-T0oWea_K3LuN4ZW7EaoM85VD_rn3XUgbLNx0UYSRymwHHACIa7LlL0Z-Tbzjhz4UJESMTx6BXQQQfxELc9ZZhTlIwcQTKHiZNoTQOqtqwtRTDdibsGNXzdJLd6WTlE92VNElZbim_No8xZdT_6rIVQEzBqRd5ZCwx1fkNcJ3pXckXvmq_ZBcBSgSRn-hwjdLvjsiR-Ry5_mMYVisBMGVTlKggzI0kD3ojD3T42x4_rrKNSPjKGN0_LX0AQ07jl1E4UhCIwZT-VzzVpzDPECS6Rtp1T4lgGlBQwiAbbWLVf7Re0OxuUB9OQ4LItttruix7E3RQj1XwrCPcc5bu3C0EsEBXuXgEEG0pKBoi1W065b7nAUk2IvtY7Eg71zHfGxTJrShKLIC1n_0jiIC0McPY3MEx5-wLyCQ_smqtNuOKaYmG4xe08NrK8yOgdmqmuBVBksaU72MuI7E60jiiw-gNEw60Jn5Nsa65VlDFXyPqz_hcdNoG6lrRnBWKA3tFFW6rIyXuTVynaMZ-QC_ClCbjGGD7fu7D4yFmX00YkULmp4OMiCya9XhAl4Ggg6mgpnf7L438oEmT1rM1503__XhinmjpBH6saZ7BqbOTzIYgnfAU2728B0j5AhZV47hD4naDOg-W1i6GGIURiCK9o8bI3arV5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b3843af59.mp4?token=nNvRhgnxsFhDsxD-T0oWea_K3LuN4ZW7EaoM85VD_rn3XUgbLNx0UYSRymwHHACIa7LlL0Z-Tbzjhz4UJESMTx6BXQQQfxELc9ZZhTlIwcQTKHiZNoTQOqtqwtRTDdibsGNXzdJLd6WTlE92VNElZbim_No8xZdT_6rIVQEzBqRd5ZCwx1fkNcJ3pXckXvmq_ZBcBSgSRn-hwjdLvjsiR-Ry5_mMYVisBMGVTlKggzI0kD3ojD3T42x4_rrKNSPjKGN0_LX0AQ07jl1E4UhCIwZT-VzzVpzDPECS6Rtp1T4lgGlBQwiAbbWLVf7Re0OxuUB9OQ4LItttruix7E3RQj1XwrCPcc5bu3C0EsEBXuXgEEG0pKBoi1W065b7nAUk2IvtY7Eg71zHfGxTJrShKLIC1n_0jiIC0McPY3MEx5-wLyCQ_smqtNuOKaYmG4xe08NrK8yOgdmqmuBVBksaU72MuI7E60jiiw-gNEw60Jn5Nsa65VlDFXyPqz_hcdNoG6lrRnBWKA3tFFW6rIyXuTVynaMZ-QC_ClCbjGGD7fu7D4yFmX00YkULmp4OMiCya9XhAl4Ggg6mgpnf7L438oEmT1rM1503__XhinmjpBH6saZ7BqbOTzIYgnfAU2728B0j5AhZV47hD4naDOg-W1i6GGIURiCK9o8bI3arV5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شهادت امام جماعت اهل سنت مسجد محمد رسول‌الله زاهدان
🔹
مولوی یوسف گرگیچ امام جماعت اهل سنت مسجد محمد رسول‌الله شهرستان زاهدان توسط افراد مسلح ناشناس به شهادت رسید.
🔹
قرارگاه قدس نیروی زمینی سپاه: مولوی گرگیچ که به عنوان شخصیتی موثر در وحدت شیعه و سنی در استان…</div>
<div class="tg-footer">👁️ 9.59K · <a href="https://t.me/farsna/462029" target="_blank">📅 18:36 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462028">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gb_2zvZOw3OCpJgOHkAq9BQDCvsKWeDgnSpvKsdvENHUCSYo_fuaZC0U544sgtnsXsBsI0-08G5oDtijix1W7jnC0vnlrvaK8DiNpNFxhBraZvevxOBH-cZkn4aqGNdwSE2fb_Ru-H3sn5mroW9xZwWYmvx4AWqj5URoQLWhWoE4Pl8hb1wIBzm8iUsYrvzu65zBZuc5ESsSZugd-MJMqKm0iVHRm8-35Di9hPxS-iK_LgR1VIOVwnVjnH1JW4D1O2Y5D3CZlZmRgtOFnqBhO0BJYAE5n392ONrf2GY3cQpUHarhoDaz3FEICRtU1rXJ-AsmYvquNLYaG-Emkz1nzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ورود خودروهای مناطق آزاد به کشور با ۲۰ درصد تخفیف
🔹
مدیرکل دفتر واردات گمرک: به مالکان خودروهای مناطق آزاد اجازه داده می‌شود با ۲۰ درصد تخفیف، خودروهای خود را به پلاک ملی تبدیل کنند.
🔹
این فرصت فقط تا پایان سال ۱۴۰۵ اعتبار دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.56K · <a href="https://t.me/farsna/462028" target="_blank">📅 18:34 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462027">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r7o_xomr9OTUc-oAT1VrkpWh6Z4aliCfwGZ9lujnI3Vgc0ZO7zFlnTb_0e02KVTstXA3EaKM2wZZcOk655PdU_4lyubHieEgwKRAEbXzXmgUPzsUGZt2ioUewzrv2RcDLPguV1gGZTeAIJ69MTeJEDjmo-iJwopDzchR6I-Vm0sS9OrIgW1eCnduppJqIiS4Qgbln8b1D0ylZWs7UPjQK7Rl6LDfV5G7knh0MUGSje04eQZhIl15EM62C2o6UXxUWZ__tjm60FUqzE1kF3Wa00bXfmSOkgiROFi_3wRw9tDibsEIqyGcFNTAIsoXjv3O9dJcWSitF18R33qW-InF3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
عضو ارشد انصارالله: ادعای ترامپ دربارهٔ تماس ما با آمریکا یاوه‌گویی است
🔹
حزام‌الاسد در پاسخ به ادعای ترامپ مبنی بر «تماس حوثی‌ها و درخواست برای مداخله‌نکردن آمریکا» نوشت: ترامپ که طبق معمول به یاوه‌گویی و دروغ‌پردازی روی آورده این بار هم روایت‌هایی بی‌اساس…</div>
<div class="tg-footer">👁️ 9.94K · <a href="https://t.me/farsna/462027" target="_blank">📅 18:23 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462026">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">علیرضا بیرانوند: هراسی از رفتن به سربازی ندارم
🔹
هر تصمیمی که قانون بگیرد، مطیع آن هستم.  @Farsna - Link</div>
<div class="tg-footer">👁️ 9.43K · <a href="https://t.me/farsna/462026" target="_blank">📅 18:17 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462025">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0e6c285df.mp4?token=iYvQT4Qr1pkfYTCdHUU_n1HFIqNS5LFgV1JUVohMqNav9ZRFb4B9JLadl0J-XloLuIHPbVPPVMBemzjETedXRdJrEtr4Gz0iCPUoXcGQDKI3C6K_-y53gEG9vhVHW5ZD5W4PEdCG9NnF_ktVSow5oCh8u71k1IX-mEhEYMvr-lJ_atJhZquq9QTbE62caLCN0-0OZwavVtZ8wEWDbmHQZen_K7MKcRhk2v6LnQG8GWm5s35_jZ3JNMqS1MTWaQOSut5JMpBfmRhTgloPtvPmfAsGAjG2Wk1J5nGkF4y2dsVTgj41sRTeKJ70996EboJoPdEUzVKbCy6WTVA0w5np1jRS30DZIBJ0qcNbagzP6s7hs1J0PmV0AKAESSq7UnSt2-B2K4BQNh4X20WHDGvTy8JwSTWr3Dd01Bc4hrWmezs0ettlMSH68VnmuZlVPgdSjXXHmXcXRaPH792qtSVgYnak-52nkXJZmdc-5f0JDU8byRhgvQhHRItntUY2BVlYwLUaBihpvM4no6kNEaaGdGZJvbJxHW35sLSKoBjnNLzODdBM83JDZ19tsLZoWIKZxC42wGEJK7L-SrYWOkzYekcDrZm_Czm2pLWKyrch15KyN83oeHgnkcJYXzhqlJU3uGT0qDW4tw6OXNtJtTdAwe9OFC7CHXeuyZdFYONnbUM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0e6c285df.mp4?token=iYvQT4Qr1pkfYTCdHUU_n1HFIqNS5LFgV1JUVohMqNav9ZRFb4B9JLadl0J-XloLuIHPbVPPVMBemzjETedXRdJrEtr4Gz0iCPUoXcGQDKI3C6K_-y53gEG9vhVHW5ZD5W4PEdCG9NnF_ktVSow5oCh8u71k1IX-mEhEYMvr-lJ_atJhZquq9QTbE62caLCN0-0OZwavVtZ8wEWDbmHQZen_K7MKcRhk2v6LnQG8GWm5s35_jZ3JNMqS1MTWaQOSut5JMpBfmRhTgloPtvPmfAsGAjG2Wk1J5nGkF4y2dsVTgj41sRTeKJ70996EboJoPdEUzVKbCy6WTVA0w5np1jRS30DZIBJ0qcNbagzP6s7hs1J0PmV0AKAESSq7UnSt2-B2K4BQNh4X20WHDGvTy8JwSTWr3Dd01Bc4hrWmezs0ettlMSH68VnmuZlVPgdSjXXHmXcXRaPH792qtSVgYnak-52nkXJZmdc-5f0JDU8byRhgvQhHRItntUY2BVlYwLUaBihpvM4no6kNEaaGdGZJvbJxHW35sLSKoBjnNLzODdBM83JDZ19tsLZoWIKZxC42wGEJK7L-SrYWOkzYekcDrZm_Czm2pLWKyrch15KyN83oeHgnkcJYXzhqlJU3uGT0qDW4tw6OXNtJtTdAwe9OFC7CHXeuyZdFYONnbUM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اعزام ۲۲ نفر ایرانی برای مسابقه جهانی مهارت
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.93K · <a href="https://t.me/farsna/462025" target="_blank">📅 18:16 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462023">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WtvOwkl9TQlOXzN0V-e-NmZ-wBchbL-5PVPJd3SKlhLpexrdSnfWv86pIrnT1xJo3leo5NUZlJ11toFuEeh-b7e3zZfgi3fixbxpd38QKlgprSBTvCT4KBOob97ejL65WRDaDLeh5g8D490dYgaZCV9bcFt9AvF04qsY9xrUS93XpJn-tZ5ObPMMG9GtAs_pG_tLl0hpjCi2V_7RcSCa-IXEjUv7NwOBGp935YmtL1EUmxKXD-2Fyjm8C_cqTWPZAPljQRsvSdTdec-4be0PrMJJozbPuXRjD-1evmpeBnAGET9DKcnEnAOrvhTKiupUbFepWJQEY89DzTQp8eerOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/J3WrkIz_EoTyjoyjLch4vhkoIB_YNHCVCkLVtKIV75QplBJX8gpXH9G4ii2JGFEDGJuI9S0KXr3QOnLSSG3sBx0K-oWQGLgqAIpF6mrGbdma3nh3AWKOgMK3PvknHyd_eDs9ammv5bvl0UeEt1p0fXX47OqrMi753NGDkjD1HqMPSP0HRunQj322lZ8Flfc_g4fHP0O1K8kkz9yb77IubPg98pijAnTMGf8uPOJZamd0Szxq6DSrUuOu6hfrYW82urAgmmnKDBnw8lU9eJqPkV1LgWu0Btds33S5OTEZTQGE7INJgfdte1XhH2fD3Gffoe8-KjHWZlNYJVPim_jV2g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حذف شیر و خورشید؛ وزیر خارجه عمان اشتباهش را اصلاح کرد
🔹
وزیر خارجه عمان بدر البوسعیدی امروز نسخۀ اصلاح‌شده پیام خود درباره لغو نشست اعراب با ایران را در شبکه اجتماعی ایکس منتشر کرد.
🔹
وزیر خارجه عمان نیز در این پیام به‌جای پرچم مزین به نام «الله» از پرچم شیر و خورشید استفاده کرده بود، اقدامی که واکنش منفی رسانه‌های کشور را درپی داشت.
🔹
حال، وزیر خارجه عمان با حذف کامل پیام پیشین، پیام جدیدی را منتشر کرده که در آن تمامی پرچم‌ها را حذف کرده است.
🔸
شبکۀ اجتماعی ایکس از سال گذشته در اقدامی ضدایرانی پرچم کشور را از ایموجی‌های خود حذف نموده و پرچم شیر و خورشید را جایگزین کرده است.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/462023" target="_blank">📅 18:09 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462020">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XNh_6xfZRz_sJBsUfLzaytPNIkU32beZGJxEnOhAmsCgXnsGu3CW0nUFIC8pu-juy5XWGSfiWnCefA2hWmNNSlZh8F3btzxCMfLwmDRNcHW00dCDbPFnP5w_uJJ_NCpVAQyr7Jtj5WyaoREXJDD0OjFWMwslx98oIqVfyu39aJm1V-7KVOz1qxKRu7MWKn6b96PTJgx571lATUS4KBqrPm2FmdlQGJb0YR7qH_W4W-WLPCRrnMPCX9dN9waappIsCJYnL6BPGCmeeLiak-jb7AjioGAD_K_PitlR7K1VMcTDT6J3EWOdpAfvSCHYM0ww2_X4kSPe1BPBlW7Co3L0ZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شهادت امام جماعت اهل سنت مسجد محمد رسول‌الله زاهدان
🔹
مولوی یوسف گرگیچ امام جماعت اهل سنت مسجد محمد رسول‌الله شهرستان زاهدان توسط افراد مسلح ناشناس به شهادت رسید.
🔹
قرارگاه قدس نیروی زمینی سپاه: مولوی گرگیچ که به عنوان شخصیتی موثر در وحدت شیعه و سنی در استان و یکی از مولوی های خوشنام و دوست داشتنی بود توسط دشمنان وحدت و گروهک‌های بلوچ کش ترور شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/462020" target="_blank">📅 18:02 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462019">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">بسته خط ۱۳۴.pdf</div>
  <div class="tg-doc-extra">2.8 MB</div>
</div>
<a href="https://t.me/farsna/462019" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">بسته خط ۱۳۳.pdf</div>
<div class="tg-footer">👁️ 9.81K · <a href="https://t.me/farsna/462019" target="_blank">📅 18:00 · 23 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
