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
<img src="https://cdn5.telesco.pe/file/Z94rPtLCt9ntGAgePpfzjchZ_JqVA6gFLKnzwPb3nDFBUWn-8CFcOZ_hGqrI7v92SHOaH-haX17CN7KzjNTijwlSs4YdsIVsMgf2g0igPslQW_M0LlyX129bxZSZBVK2Yht-qWqOss4w-810z4Poit7_Z_wMMk4kJG-_09YypHEYvGDsV7x0wUZRe7zAMPcSiPWSpw4IsTgx9XLrUnZ8AB4XLL4Yovm9GtZ96PABwTcU509d4HPAGs4ff9FSofaVf-33dgWpiEtMG8HA_sbRNFCediNf8beyW7P1W1OoHqb_pnxrWvwv7yQGyGw0VTc-gMmiDhXA52vyY6FOzIDu-A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 508K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-09 19:04:48</div>
<hr>

<div class="tg-post" id="msg-102444">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/m8qIWCyleJRdKB6tVvTkOa41IbCNeJ7pby18dqoEKVs-esrrPGOrCIuPvzFNnIesC9CZDO6DbM70DzI5rSYmQ5DEA2FhJdakSHDMP2hjwVkYN5JuMdAiGj7_1UJC-KUJ5N9VImplYPjUVga64RzqtMzAisSaqX6kpKX9kXVBJETDfq4wqy_B3U8MQvCB8PaE9z2E9M46JmACF0grULJH-UQ3-Q35tiP3-Ey1OpXo075ecScTkr1SSV6LDit4S55y6bjFy0NMWmdgzZvKDiLfO5lWS1Sf8xulxYFEOgFmpK2lRvuaLsbBxnSWMuWKFgdAilxAsnfmh8MlLx8WZTYIpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hZiYK-7JxQ5JAt24REBfX6p-z2mFRmLq0Op64pPYS75nItESM5qFCNycAyqysPghDVVKbcV6aZV_6ar5TyYERRuahuM7GTNl0jZ2OLIknZzklQrMk5Vg0FkUJG1PFiWAB0njw2NG1Zs1s5AZMQJnPCFXkGSAWNvOqY60kDQ1jHr843p-4tkLxpJ1ElEJOXLMMoAfFcDERNKZOL6dFyV2v1FaU5mPKdK0FdWPm0iUMnpbVmwErXbCarKDGRaABUdc1vPu6f4r83_bqnVYrbZRU9zV5Dt1Gv8zwH34slFJ3g7V7phq3h8a9nNvY78-m2ZYP44w36lnA7PFNa600Aq4rQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KTcvSAD8FEF9bd36t-v2h-jYCEjvqARmEH6fCILiuiyiwepIbrmtB5IxzQPlFTa3ogsaCB4dWOqnQpPepITVZJ8tLFEVtFFW3HBRIUq6W3hctzIWqBtZIJD1xLTnvEFlPegMWHThjZJ9UqS8vgFhGUeoI06f-2GHwqU6KHgVgXaY3JeCc0Xt_gxOHRO-x27oh0B5qEyPKQQ0aawWHRNbo57vtxFkw5ll10J2DrXo9L5SXPMPzJqoAePyrkTbNK57NRcMPQ5gucq_UndZ8M24NpPrTg3az8Bpqiiucfagr7jYCui-hEfakvK3Nz1FtN2ZQFiJX7hT1exN_vSwxW5EVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vFSJi6921B9EfUAfWDcGskbw15JcMCFEVjFKEdMpCd6MYh0RCjUsjB7NmNMe7EsndHg-6SgSqzZqMkfCQv_0ywAcVtTuBz4GOUEoUptz1wc6GRe1514zdvTHkOh4Kk8Q_Kj4mfaJnVx7GMsWux5GrOrYljJUkja1UAoO_Jxznys02S5I8H08LW9lS8G4_0EQfCOZDgPM1EVJQNjMA9r5aeTU_0c6_OvzSWx48JO82VFiU4LMUYYpRfa1gThmmsDNyAfwuRrO4XePkptt6SVR09yPGeDOn_pxXITaZdfK-jRydunkBVllOYG02gbR7jwoy3ImewDD6AJ_HRnn5DRIrw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
عشق و حال لامین یامال با دوست دخترش اینس گارسیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.23K · <a href="https://t.me/Futball180TV/102444" target="_blank">📅 19:01 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102443">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fbFwt3Cx86RuRJocw5Fk-gmShKIordBCWxMlID6MoD2qbMOtb25iLJm2A7Wl9zFsK3ZPHTCJRwSyh1it4qpzzR2Z3RslW7rNKmYp4gNTR4i3kOxBzKHSxz36Q7IGLY5tIVGOF3OsCCQu44q29KiXGjR_Y1P_Z4Z7S2kUOMDy-NX1c26IqVaA_uDmnAe2bz7WQQtUfdjqVoToYaRDf5Z9D_NNM9qiMnTFkQQHg_bCRLJRRKohXaPruKoonwRZED0Wuw8E1Uu1Q6V_fuME_XI-sYDmefxjXD7Yj5Dlb6skMjEfS52JAQ6h5UOvY-0exyygncqYFtpGj4qqmCfw_HDSfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازی دوستانه مقابل فولاد</div>
<div class="tg-footer">👁️ 1.53K · <a href="https://t.me/Futball180TV/102443" target="_blank">📅 19:01 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102442">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DCtdyR1eJUsR55mnjVKZ6tu1yuZadyRUkYSr9Pl22TAgDoxR0rtLBMsWneM4_8LjXWV4k928JSBhznZcNfCw0tuPWZTvWGbeJ62_p3lkyRGIukGRiwiFKqn_c02HzJorIiT0XsSaXvUsbgfNvWOlSUfZqErqbX4ETOa9F5IrL0fLT5yD7J_PO_WzTLWtFCVovD13qKfKlU9QxrK0Friaic9JTh1A7CJVi-TgKALP2kJl6Tr8_6RU5qfNHz3pTCwmaSZ229PbqaspvkcThgPaULG4gfNeT0Act1KDv4I5U5v8xYjo21L-OIlxO3J-ZR2Eii2BSO0a-myCD-HXfpEg6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
فوووووری محرومیت دوپینگ میخائیلو مودریک لغو شد و او به زودی به اردوی چلسی در هنگ کنگ ملحق میشه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/Futball180TV/102442" target="_blank">📅 18:58 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102440">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CXy46wjlBCZW5XWbfkfIgxKzYS_A9ZBhdQNQVtEtqc_u5X0YyOVDhtDrVFbMEP93hcs6iJ3QVdOracJDaijEWWGpsPiL7DaJ3I2OpIlVw7C-wNvK-OJTiyxWEzd9IARVtyf-59OzLa-rHmDTOzSIYM3xDN1tjrfXnnUgREF1cPnITRJHcUG_oCCZlOEaVOVOan8imrZmSpboM3pCbF0f1Y-MAoe5i9KcY1zerC84HJAp9J3J0rSY0YBgY1uIjo62wFBBZzw6huqVmBrEtpfjfkn-ip5rPC-0O2m9ynZEPtHm2iz-GT9TYx71OwB92rlt6ZDTE1JTUUCepCvURDDZfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mqDpH5M5NX0_RAB2X8LHChxv6AnmEeIOdIwdSjHzLyAZcCj7icTvH8ocQZAeR4ZWkq5T_6T7FHzGBPDH3SvhM2ufp1eZzcdRz8lFXivCi3VYHgPE3bzZ1bMS_OwOj6DcWPYvKM9VP5WS5T0uEMKMpSf2fmKWkBP5mP2h1FRjVPK0BUKsIHvnCWxwJS-CzQPeX5m2oWowhbasJJwzZvmXcxmQd9EwcFd4ROfSneSVRbzq3aYJgXdNxeFx-evLiU3EwL1OyAoCpcA3CAb6KRkD-etbiXKrJsCtYINcfRumSFfImc8mLgdJvJ6Usi3bueyFCXDl5BBY7oQ96kxFhZENzg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پیر شدیم و خودمون خبر نداریم..
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.17K · <a href="https://t.me/Futball180TV/102440" target="_blank">📅 18:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102439">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5d65b7222.mp4?token=NbVKRlzhM5cL6FPH10PQjjm6-vmj4sPuLLaTmGvUVPooVo7FrFT8aPMnqaWH4rb0aD1VjCT1bfiKsB4W4S-zgN1Wn3-h_tVlVlJ4FCh1U_pPEWKiha87LNRfl_WqQGWaHTJzZTriIN3YeX3jEgzSTBlauJ4aANzQA6BtvD4zo3cLdZlJmMm8ZtaRIWxASGT3EhxC2yPUinmnMf2XqSi30J-F_aqA_ybuh6sohScemmCQT437qCo3P6ZtRZk04rTuLNXSso1ERyQEUnSS2YoC5YIoTW-SO_kJN2SP6hFdS--PTbxJ7AQadkeLZ5YZL9ZXND8Aes0Ii-IvKm9rLlOrLmjtR6i_CGu2xqEgcu0FC2nbzxB7NIErnzXKs9J1jySiwebYTtdX-Ij5tw5p-EkoEnAuTpiH3u1MSmPDlGsLdOHynPUQ3dSoXbYbUt1pI9WnWZPJ1C0Lhj8Z5az2tWvBazZghk3riXC1fN70_QVtxmabier65dmeCbdbj4KvdEm15bReQgL3smXB9-7qUCFJ7YYZyMCz8gz_yAFYBoQ_dxRsRZwboj8HTij4ZLd7S6w5UPLOmKmXlwtFaJGy0f46MqTw8JUH0rMuDp55pemy7VqCKdeUY2qm2YhJa5yJfZTuRJS0P3pxZvf4qASkavPQ5VpvXPtI3w0kvA7ulc7DtqI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5d65b7222.mp4?token=NbVKRlzhM5cL6FPH10PQjjm6-vmj4sPuLLaTmGvUVPooVo7FrFT8aPMnqaWH4rb0aD1VjCT1bfiKsB4W4S-zgN1Wn3-h_tVlVlJ4FCh1U_pPEWKiha87LNRfl_WqQGWaHTJzZTriIN3YeX3jEgzSTBlauJ4aANzQA6BtvD4zo3cLdZlJmMm8ZtaRIWxASGT3EhxC2yPUinmnMf2XqSi30J-F_aqA_ybuh6sohScemmCQT437qCo3P6ZtRZk04rTuLNXSso1ERyQEUnSS2YoC5YIoTW-SO_kJN2SP6hFdS--PTbxJ7AQadkeLZ5YZL9ZXND8Aes0Ii-IvKm9rLlOrLmjtR6i_CGu2xqEgcu0FC2nbzxB7NIErnzXKs9J1jySiwebYTtdX-Ij5tw5p-EkoEnAuTpiH3u1MSmPDlGsLdOHynPUQ3dSoXbYbUt1pI9WnWZPJ1C0Lhj8Z5az2tWvBazZghk3riXC1fN70_QVtxmabier65dmeCbdbj4KvdEm15bReQgL3smXB9-7qUCFJ7YYZyMCz8gz_yAFYBoQ_dxRsRZwboj8HTij4ZLd7S6w5UPLOmKmXlwtFaJGy0f46MqTw8JUH0rMuDp55pemy7VqCKdeUY2qm2YhJa5yJfZTuRJS0P3pxZvf4qASkavPQ5VpvXPtI3w0kvA7ulc7DtqI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
چند تا از شوت های کارلوس رو ببینید، زمانی که فوتبال تا این حد راجب کسب و کار و پول نبود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/Futball180TV/102439" target="_blank">📅 18:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102438">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d5590fc67.mp4?token=u1S4RuGzqHXpa-yhuVPthbxyZlA_Zc6SEH6w0ZteVJzcwZWLzuBXo6Sg4_sTEy_jKVUX8AHx_1uqF9HliTcouVs8Bq8sukg5M8vczGu7l6U70QcrR2d55XbEpdofTbNO782G1wWf6_6TFhYkjcqVWwCIu93dUM-beKdNvlZh-OYWBYvr3bXPmqnoHNmHm9EGQe8umarmmSbqq0FejJd4yJawqTmGXETJ1PTClxB2BFvuFeJbTbOlSUijwBq6Zle4bG7k09dW7ktaa6Rceeni-TlcurXuYXchIkYbyaU8iiCURy-K_PK4QTsFfTaThhScouNs5Ht6PIW_Uy9gZ-00Mw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d5590fc67.mp4?token=u1S4RuGzqHXpa-yhuVPthbxyZlA_Zc6SEH6w0ZteVJzcwZWLzuBXo6Sg4_sTEy_jKVUX8AHx_1uqF9HliTcouVs8Bq8sukg5M8vczGu7l6U70QcrR2d55XbEpdofTbNO782G1wWf6_6TFhYkjcqVWwCIu93dUM-beKdNvlZh-OYWBYvr3bXPmqnoHNmHm9EGQe8umarmmSbqq0FejJd4yJawqTmGXETJ1PTClxB2BFvuFeJbTbOlSUijwBq6Zle4bG7k09dW7ktaa6Rceeni-TlcurXuYXchIkYbyaU8iiCURy-K_PK4QTsFfTaThhScouNs5Ht6PIW_Uy9gZ-00Mw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇷
ویدیویی‌از وینیسیوس‌جونیور در سن ۱۶ سالگی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.69K · <a href="https://t.me/Futball180TV/102438" target="_blank">📅 18:04 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102436">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HISrN8-TZZvfekThLd0nnki5xAHr7G2Vjn4XN18g1GstHXzjdqXecv4esEHDwjE_J1mqmZRyLv-QsGhmHEKMQFa9r_I5O8_fxe8pq5bHiJ2CwHsBqyTg6qHMfFkwqdPGQ6_PQM6GQ0FY7PRGpQbjLSROl2TIKFj8HQujj_D4_gySBYwmlS4fXWuv9REuBCmTqm03CTrRX_Ecxh9gf8iJDNrzDTE95uNPEadRmwKRSJ63WxoJfMlsYX3R3ekhihY4FGRUIrCVcIZaKVqQNe0Fkju1dFRX3YJMAY8bTGx_GYNN8JyFy29taucnjhw3p_P-fEIFoZpEEup92r5Ijar70A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p81RHJGNuFTl2HMIPVGUyG6_Skd_WkFK3fkqvC3Emt6SkwEXIim0Rz1JeCBHOQTXkjmRGjaT9KUl_EhsiorZ4WZkv23CTixoJ9dO-ZDAbwc6iztcmbWtJEai1_OcGeCOQN0KiORht3HmNCV9Ith3HTZIPJBFlhNm7f369AJDokomimCU2VA8rmUPfKtD-3xGfTTD1scFWXN-HByj4YBhpkt-GWK2Y8eeSY5GX1Zz8ns04XMwnci92hIulJy2jZgsujFLCBaRq0H6jMwbZE4kmKfZlFuAafjPSRnZN5Jvz6LkdTWQ9NiELms8FyZpO5pMVpP9eFWeX70L2KbYTZ7ymQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🔵
فوری، محرومیت سنگین چلسی:
🗣
باشگاه چلسی به مبلغ 10 میلیون پوند جریمه شد.
🗣
همچنین، به طور تعلیقی از ثبت بازیکن جدید در دو دوره نقل و انتقال محروم خواهد شد. به این معنی که اگر بار دیگر خطایی انجام دهد این بار پنجره قطعی بسته خواهد شد.
🗣
در ابتدا 6 امتیاز از مجموع امتیازات چلسی در فصل آینده کسر شد، اما باشگاه درخواست تجدیدنظر داد و این رأی باطل شد.
🗣
این رای بخاطر تخلفات نقل و انتقالاتی در دوره آبراموویچ مالک قبلی باشگاه صادر شده است. مالکان جدید این باشگاه خود این تخلفات را گزارش دادند که باعث تخفیف در حکم نهایی شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.54K · <a href="https://t.me/Futball180TV/102436" target="_blank">📅 18:03 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102435">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68f9e38a71.mp4?token=Evh7HnQtq4sjPHDxwBuPZNEnTLTGxqyJjDVYZl7bfW-fxIEg1fMI8AxejFf8OGdW5dXMk5DkviBDjz9KpgxCOFRX91bDChtc8UOl7svOnTOWI_COPU4DclRDFN_FGqhl4TbCZGVAh6v2fVpryy3UuBNSwj8UH3v3bOUU8Z0wu_wv_oMEBrHVt2tynwsD_lTwFEoS30fYh3oiljdM3aezzAXMLpnWOXJhcWFEggfPjad9aOb0XVH7ZNIN3JAFT18OUujrAPPMnQu2OVUQTYkr6sdy9m90cC50WTPZbXxbk__WKgIXd71CVzZ7Pn-gnJv9sxkIoawYweqw7e0mg-WfY41QU9ReK0lo6tDY8sxDGwGrDqf7rJTLwbwAHB_xO9hQSJILpiWK0_jw45tGOjdBazjDZHKY2F3ouu3UrWuRgvjM8rW98EoxPPOG7OyxsCkWIzC6_GEMR4tyAMOkyLeZ-8GlnLDpY5yuu6gsaOXdu2B5uUuuY-QHjsaNfXNZ7BF4lXyDMauKZWv17czUjKS2RQtoqgkr0E5Zjk1ypVI5oHBxYp4v4VhnkUCXOSEkLz9Ot4Uy1QeymV7J0ke0v070iQ1vrEPBW6uIUVGKy65bn74wWTo6iKSsm8GxRM2VLGgYs24_ibinubjdhMPnwYi4Zi1mWgrN1XkEaWeOzpRyx0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68f9e38a71.mp4?token=Evh7HnQtq4sjPHDxwBuPZNEnTLTGxqyJjDVYZl7bfW-fxIEg1fMI8AxejFf8OGdW5dXMk5DkviBDjz9KpgxCOFRX91bDChtc8UOl7svOnTOWI_COPU4DclRDFN_FGqhl4TbCZGVAh6v2fVpryy3UuBNSwj8UH3v3bOUU8Z0wu_wv_oMEBrHVt2tynwsD_lTwFEoS30fYh3oiljdM3aezzAXMLpnWOXJhcWFEggfPjad9aOb0XVH7ZNIN3JAFT18OUujrAPPMnQu2OVUQTYkr6sdy9m90cC50WTPZbXxbk__WKgIXd71CVzZ7Pn-gnJv9sxkIoawYweqw7e0mg-WfY41QU9ReK0lo6tDY8sxDGwGrDqf7rJTLwbwAHB_xO9hQSJILpiWK0_jw45tGOjdBazjDZHKY2F3ouu3UrWuRgvjM8rW98EoxPPOG7OyxsCkWIzC6_GEMR4tyAMOkyLeZ-8GlnLDpY5yuu6gsaOXdu2B5uUuuY-QHjsaNfXNZ7BF4lXyDMauKZWv17czUjKS2RQtoqgkr0E5Zjk1ypVI5oHBxYp4v4VhnkUCXOSEkLz9Ot4Uy1QeymV7J0ke0v070iQ1vrEPBW6uIUVGKy65bn74wWTo6iKSsm8GxRM2VLGgYs24_ibinubjdhMPnwYi4Zi1mWgrN1XkEaWeOzpRyx0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
درگیری کورتیس‌جونز، سیمیکاس و سوبوسلای بر سر بازوبند کاپیتانی لیورپول در بازی دوستانه اخیر!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.98K · <a href="https://t.me/Futball180TV/102435" target="_blank">📅 17:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102433">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nHwFcDHMp2wBbiK2JF9ErBGXAVY4KJL7ojrHa0TX_v_kQX0L9MNn6WtxCrotCZh7OgPJ15spZ2hP5B-CxZnkg9IUCr5b-vwu3xUVPNl0IwNJ51Zbomf6Jy0HShz95s7A2xpE6HfosHXLVsjyZZe0vz7QcsZGt3wrhWZJubFEiQ8v8e1v5ClcZlWDOHGazj-cCcsPFoXuI3JlPlOxmh4s8yVQEtj6fZtlqS-ASMfVGgH4UFu21O94u5Rc0HkfWjwc_XBNSCw85KSE-3rxgASC6mWakRxfTocPZnmvdvBBcle0qCXmuVhhHiDQqrOiatxDomElRmPmnfwpU8OIncNb_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RN0cl0AK3F78DCu7MMEwnpFJWqqKprTfA2AAfNCM5As8y1i-XS08PPhTDvrMJgkxHgPcW3PhkGGom8Ch0kPOidDq9SojmvN7yWlfzUVx-nvfM6M05ZpZy16FrkWSGO79z8UQ6feSYU8X0226U83uWtuE31zmJqV7BaZTAKUeQWgmmUZhAnUpwu3np5pKV7ixlyPlNs6fHgcPOnWGWvm_CxVwPphtKTxWtyzMkMjHdJydxMV2CrHG-7x-i5gBhnLS1S6uDCMqts0NMPR812z1DukBt1e0vDBbx8T7KxiZQo899gtffKYQ8_reIxSrdiSC25vLYj-3nsQLLrfipOCH6w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
ال اسپانیول:
پرتغال و اسپانیا اعلام کردن اگه اینفانتینو پیشنهاد خصوصی سازی جام جهانی رو پس نگیره از میزبانی جام جهانی 2030 کناره گیری خواهند کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.12K · <a href="https://t.me/Futball180TV/102433" target="_blank">📅 17:36 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102432">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromچِشم به راهیم</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/96363baca3.mp4?token=umVhdByQNsT-UhaeU8M9STAx70Qu1Ur8hRfCZlyCpuGPgyi-uA2GWms-SQ6DUjnKkG3qs50aF4nhP9B0mU7qNRdWcWkZnFfI_JO69aLP5V1Dmc93IgWN2oG7CA9jutExSZ5_NtU3cMMzVBLcqirMJbA86WWp-kYJFM_MCduj_RSNOGLLc9bFQPA9nPFJik9C_an7l6H9MzwaXrgG1BcejYBJk-EDEP0ridpZVVQ9MshO8twXVo2tIKX9qXufqGBUZBc8LdZuJeOghMiQ6aMs4PeZMQJu7qYWIMF-mfYL4qGpqonOAJsxuFvH84mEkwWyRDEfdsVDGc3J7IxkVYSBkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/96363baca3.mp4?token=umVhdByQNsT-UhaeU8M9STAx70Qu1Ur8hRfCZlyCpuGPgyi-uA2GWms-SQ6DUjnKkG3qs50aF4nhP9B0mU7qNRdWcWkZnFfI_JO69aLP5V1Dmc93IgWN2oG7CA9jutExSZ5_NtU3cMMzVBLcqirMJbA86WWp-kYJFM_MCduj_RSNOGLLc9bFQPA9nPFJik9C_an7l6H9MzwaXrgG1BcejYBJk-EDEP0ridpZVVQ9MshO8twXVo2tIKX9qXufqGBUZBc8LdZuJeOghMiQ6aMs4PeZMQJu7qYWIMF-mfYL4qGpqonOAJsxuFvH84mEkwWyRDEfdsVDGc3J7IxkVYSBkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
مرزها برای میزبانی از زائران اربعین آماده‌تر از همیشه
🔹
در آستانه اربعین حسینی، پروژه‌های عمرانی و زیرساختی در پایانه‌های مرزی کشور با هدف تسهیل تردد زائران اجرا شده است.
🔹
در مهران ظرفیت خدمات و زیرساخت‌های برق، آب و روشنایی تقویت شده، در شلمچه بازسازی و نوسازی بخش‌های مختلف پایانه انجام گرفته، چذابه با توسعه امکانات رفاهی تجهیز شده، باشماق به سامانه‌های هوشمند مدیریت تردد مجهز شده، تمرچین توسعه زیرساخت‌های خدماتی و ساماندهی محوطه را پشت سر گذاشته و در خسروی نیز سالن‌های مسافری، پارکینگ‌ها و فضاهای خدمت‌رسانی توسعه یافته‌اند.
🔹
همه این اقدامات با یک هدف انجام شده است؛ سفری ایمن‌تر، روان‌تر و آرام‌تر برای زائران اربعین
#چشم_به_راهیم
#اربعین_حسینی
#سازمان_راهداری_و_حمل_و_نقل_جاده_ای
🌐
rmto.ir
🌐
141.ir
@Cheshm_Be_Rahim</div>
<div class="tg-footer">👁️ 7.42K · <a href="https://t.me/Futball180TV/102432" target="_blank">📅 17:36 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102431">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">💥
🧐
رونالدو، پسرش و جورجینا درحال عشق و حال در گرمای تابستونی اروپا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.98K · <a href="https://t.me/Futball180TV/102431" target="_blank">📅 17:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102430">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e703311f9.mp4?token=FgUtw-r60oDau7n9IVJWuZJ2h6tzMQObG3cJfxmo-EOxP2jYzutSPjThv5O4iOA_IY4nHhGKQrSFmoi6gMj-86fb8YQzOsb4-XOQlzknvr61owqv_74umg69RwuVRlULqvJJRoJmMm_SEy0dc83YRkFgCzwUbvMdcQB6tu9OHB61ZukbOpUt4y-oDCmlOb4VjTr6Bh--wmAaj5L_X8zAz5M3g1pCAFor-DV6S0ieTVVQJifGgRfVQ4QZVkPFWtE5334cozrONcrFKWMhtARUNzQtgVh_b_wYHNZ0pPX_nTdYHqCVERtHn7_DTfyJ-SxznuIbeWttC5GYBBZsiWFg9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e703311f9.mp4?token=FgUtw-r60oDau7n9IVJWuZJ2h6tzMQObG3cJfxmo-EOxP2jYzutSPjThv5O4iOA_IY4nHhGKQrSFmoi6gMj-86fb8YQzOsb4-XOQlzknvr61owqv_74umg69RwuVRlULqvJJRoJmMm_SEy0dc83YRkFgCzwUbvMdcQB6tu9OHB61ZukbOpUt4y-oDCmlOb4VjTr6Bh--wmAaj5L_X8zAz5M3g1pCAFor-DV6S0ieTVVQJifGgRfVQ4QZVkPFWtE5334cozrONcrFKWMhtARUNzQtgVh_b_wYHNZ0pPX_nTdYHqCVERtHn7_DTfyJ-SxznuIbeWttC5GYBBZsiWFg9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
👍
🎙
تمجید جالب کاسمیرو از لیونل‌مسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.56K · <a href="https://t.me/Futball180TV/102430" target="_blank">📅 17:00 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102429">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b472a6619e.mp4?token=oHS00TsnqkM_SA1MJRP-pk3yHsZFHF9oR_EwVAVTFqWb6P7bA1iGdGYEXs9OIVF2Nk5F5n81uYs6r-ji5bg3Gy-acOXeJ6Eo3-EJmXIkdBmUusptln6m86OOsljARsTrW6dY4Fn3mkm5cX0VSaKCYJ_PqCFDhVS8qhbqSiJS_441XfloMkDqrUCXh-K_9Z7OQUafUHCFtnMiSc7JJ4NxV1AOcnLtCxU0nWXhpDfAM1inkKhjkfWs5AI5ZiEF0hU2kIq0RewfHg6ZxlS4KD7OqTLLvGSBqRzIXcWRdms5Y6pNMdk2dRSlrpeeBgfs6KnhQgtyIkDtQFvoEB-kJ0ZKjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b472a6619e.mp4?token=oHS00TsnqkM_SA1MJRP-pk3yHsZFHF9oR_EwVAVTFqWb6P7bA1iGdGYEXs9OIVF2Nk5F5n81uYs6r-ji5bg3Gy-acOXeJ6Eo3-EJmXIkdBmUusptln6m86OOsljARsTrW6dY4Fn3mkm5cX0VSaKCYJ_PqCFDhVS8qhbqSiJS_441XfloMkDqrUCXh-K_9Z7OQUafUHCFtnMiSc7JJ4NxV1AOcnLtCxU0nWXhpDfAM1inkKhjkfWs5AI5ZiEF0hU2kIq0RewfHg6ZxlS4KD7OqTLLvGSBqRzIXcWRdms5Y6pNMdk2dRSlrpeeBgfs6KnhQgtyIkDtQFvoEB-kJ0ZKjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
🇮🇷
یادی‌کنیم از بازی تاریخی ایران و قطر با گزارش جذاب عادل فردوسی‌پور
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/Futball180TV/102429" target="_blank">📅 16:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102428">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dfd29d0ef7.mp4?token=XXBL4ux_HV034ypaftx85bkH8zkZqLF9-88R3IKceiysSy9a3Tbklb8z4tk2n_yloglBOQUZdIFgdNHVqwl-_cLwpaRbPx827QxrQ2GXXX6zj8hC4KuYdmTA4xdRrAJE2jaUvigTYFSWYgQeqmc-nCaGu6iUHqkKsnig0D-Q6To9AvFjGW9ZzoVusS4aOjKzBF0c635u3f-aZDj491VaeXcLkTDCcJo_EkRgaxzN6Q685Elm9y3j-tHQ3qqWic8Nhv_kNBT2vJH8geWn3-_XI66C4MSe-Fv5t4tKp58107HATWbpl7J7r7OjV7dug_q1BZv3oGa9Oz9oBYKenftiHoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dfd29d0ef7.mp4?token=XXBL4ux_HV034ypaftx85bkH8zkZqLF9-88R3IKceiysSy9a3Tbklb8z4tk2n_yloglBOQUZdIFgdNHVqwl-_cLwpaRbPx827QxrQ2GXXX6zj8hC4KuYdmTA4xdRrAJE2jaUvigTYFSWYgQeqmc-nCaGu6iUHqkKsnig0D-Q6To9AvFjGW9ZzoVusS4aOjKzBF0c635u3f-aZDj491VaeXcLkTDCcJo_EkRgaxzN6Q685Elm9y3j-tHQ3qqWic8Nhv_kNBT2vJH8geWn3-_XI66C4MSe-Fv5t4tKp58107HATWbpl7J7r7OjV7dug_q1BZv3oGa9Oz9oBYKenftiHoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نیاز بود یه آیتم جدا برا لحظات تاریخی فیروز خان کریمی
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/Futball180TV/102428" target="_blank">📅 16:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102427">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d17c8ef3f2.mp4?token=VqAl1faROEG2VGU0ggFZuDFcfB0t6dD1BdEMsbg0uqhUUZVgx5QsEVqgvEYHAwWSwLOvdoeswd-4t0sc1PKOVm110JFrahn6pIQtm9qY_1gXHWBlLoatD1jRaQUlWl-o_4_02LED8_YDwDyw0kDEMR6qeJau1oFWWgnE_n9tlQLoluWoWcMCscLyBdntR-9EL0wJkm9VBjQBGxfyDhFXC0HIvhN2wO4Xn-d0jSN7Vjb_VRm06RFwimxrdEAKXk7yHor4h7MS5j8j3lXjUK8SASnQrg5J4oR6Yfo7sieALFxW5LBHuCAILcwMLux0C--8FE1vnk7zAw-Xr-ZX-HvKmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d17c8ef3f2.mp4?token=VqAl1faROEG2VGU0ggFZuDFcfB0t6dD1BdEMsbg0uqhUUZVgx5QsEVqgvEYHAwWSwLOvdoeswd-4t0sc1PKOVm110JFrahn6pIQtm9qY_1gXHWBlLoatD1jRaQUlWl-o_4_02LED8_YDwDyw0kDEMR6qeJau1oFWWgnE_n9tlQLoluWoWcMCscLyBdntR-9EL0wJkm9VBjQBGxfyDhFXC0HIvhN2wO4Xn-d0jSN7Vjb_VRm06RFwimxrdEAKXk7yHor4h7MS5j8j3lXjUK8SASnQrg5J4oR6Yfo7sieALFxW5LBHuCAILcwMLux0C--8FE1vnk7zAw-Xr-ZX-HvKmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤯
▶️
رکورد پرش سه گام جاناتان ادواردز (۱۹۹۵) با ۱۸.۲۹ متر ثبت شد و ۳۰ سال پابرجاست. این دستاورد استثنایی در دو و میدانی تحسین شده است. ادواردز در مصاحبه اخیر بر تکنیک منحصر به فرد و هماهنگی قدرت و تکنیک تأکید کرد. او پیشرفت رشته را با شکستن رکورد توسط نسل جدید ورزشکاران مفید می‌داند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/Futball180TV/102427" target="_blank">📅 16:01 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102426">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/543e2ce52d.mp4?token=XgIL1xFEgqpFi7MiVK8jmsJLAmswmVSgSCzCqy2FpiAUxuxmPFS6ecLNJAwPzqN9iw5PHVS10tmhMctgIOI3mC1TsuG4EihV2qSEWZb0ZVIVoB_oZYZAiC4CYJRstGvRplGMaCsEb0Ll5RHHOckzmmXD1smMgTE4Xj8TnykCblimnSbT5Mod9Zz91X4l-WbF3kCAMNhzSP5QVF2vuKl7gr-U87oUEC6tTXe73zkwxmpGLLi0DirDbBRKsHP0c1p6UzVz7IEOcSosbqIGlzMEr2fYZCsGnr_VGRoG5gfLRMK41xexJbXeLUy764vdlEYmPN0wlJe3IKrkvJs3n3ilhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/543e2ce52d.mp4?token=XgIL1xFEgqpFi7MiVK8jmsJLAmswmVSgSCzCqy2FpiAUxuxmPFS6ecLNJAwPzqN9iw5PHVS10tmhMctgIOI3mC1TsuG4EihV2qSEWZb0ZVIVoB_oZYZAiC4CYJRstGvRplGMaCsEb0Ll5RHHOckzmmXD1smMgTE4Xj8TnykCblimnSbT5Mod9Zz91X4l-WbF3kCAMNhzSP5QVF2vuKl7gr-U87oUEC6tTXe73zkwxmpGLLi0DirDbBRKsHP0c1p6UzVz7IEOcSosbqIGlzMEr2fYZCsGnr_VGRoG5gfLRMK41xexJbXeLUy764vdlEYmPN0wlJe3IKrkvJs3n3ilhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئو کمتر دیده شده از مارادونا و فن‌پرسی
💘
💘
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/Futball180TV/102426" target="_blank">📅 15:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102425">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e43f315425.mp4?token=e3UbMDRw95mJIJHS347Jdcjh5XzV3UnN_suk4LRUICTGI6LbeCWYcUEAJel8GnpSpXUxTSvQnvYsFm3JFxHwZa8N7ni3i_MZQH5bt0b5C-tu2NkqwqvIq6XR4ubFNPySfbtoNRnhRmuh7cdUmbNQbxEVsp0B3LSrsMyCsHEDH3pyT7QicYYntnvxSeApbDIOQyAnIVAq0SiSEeCUvP2z4C48zHSI0T9akMRZgTOE102Zlmqs7DsbUH-qjyfX-2tiEBXPtzZ-QS0bjkynuyLm_xYxCi5hOq9JPIvzeZe_JoZel278-a8JEbok27UwgUu0oWt1vEUs4YJ4SRZWaINKIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e43f315425.mp4?token=e3UbMDRw95mJIJHS347Jdcjh5XzV3UnN_suk4LRUICTGI6LbeCWYcUEAJel8GnpSpXUxTSvQnvYsFm3JFxHwZa8N7ni3i_MZQH5bt0b5C-tu2NkqwqvIq6XR4ubFNPySfbtoNRnhRmuh7cdUmbNQbxEVsp0B3LSrsMyCsHEDH3pyT7QicYYntnvxSeApbDIOQyAnIVAq0SiSEeCUvP2z4C48zHSI0T9akMRZgTOE102Zlmqs7DsbUH-qjyfX-2tiEBXPtzZ-QS0bjkynuyLm_xYxCi5hOq9JPIvzeZe_JoZel278-a8JEbok27UwgUu0oWt1vEUs4YJ4SRZWaINKIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
⚠️
تجسمی از المپیک اگر تهران برگذار میشد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/Futball180TV/102425" target="_blank">📅 15:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102424">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea1f4ae5ef.mp4?token=r1IHsPWJFEHraRIBXHOeZhfrpP3wiQOX_Cv8XuzwdO7QAvvAy1jjGBJ7B_-_ttxXlAxSBKz_8j_EL2g7XwctrGNLLfU3xfse6Yyg7NgEPwVPFMFQy1T5wfq9XqT-VA815_QCVlFkstJizasppXNM7D0HmTQ9toWXY0rG6xAd5zRfBmsA3BQwqrZCWKqky8zBvcxRY0YWjRHueNhAckrf3Yq48j68kR9SLD_b5pE0Wjt-QQCeoXLiyzJ69ff9EOsybSDjsTOVZOR_V5V89hfJzEwKXEnAjSw_Y7fTnCVGY3spVq2EIaRo1yH0BUrjSVwjFVv-mDXfhI6-GCOQKpSCGnN3_Kt7emR2rbKOccUqylzUyUlAnkeyPs_ZZnVPpJ-DWdPvs76TjDBkFC0pBAbZgc3azO2T9fODosyEYxdYFq0L_CvT2Zn8gBt_yJUV3FFT3MEtRqKJmdHNoCHdygl4VqBk-x0kckRlP9oqyfjefP8qVLn9Mu-jL-Wyo8KDWrgxetyEpeJIWW3_kf8Q1_2CrwK8gL0d1LJLaHHPa1gxxVOA8SzpHYuVvKgLtifUxCVq_nyVDpZT7PwwfE9XMbutgM_jJjrz8s_bQJ1JwqibfDrBR0U5GMtUaVY7ykFURPIZmHfl2R_vHyoz0xdbhZq7U11h2WVfQSw9LGYG7NjCryo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea1f4ae5ef.mp4?token=r1IHsPWJFEHraRIBXHOeZhfrpP3wiQOX_Cv8XuzwdO7QAvvAy1jjGBJ7B_-_ttxXlAxSBKz_8j_EL2g7XwctrGNLLfU3xfse6Yyg7NgEPwVPFMFQy1T5wfq9XqT-VA815_QCVlFkstJizasppXNM7D0HmTQ9toWXY0rG6xAd5zRfBmsA3BQwqrZCWKqky8zBvcxRY0YWjRHueNhAckrf3Yq48j68kR9SLD_b5pE0Wjt-QQCeoXLiyzJ69ff9EOsybSDjsTOVZOR_V5V89hfJzEwKXEnAjSw_Y7fTnCVGY3spVq2EIaRo1yH0BUrjSVwjFVv-mDXfhI6-GCOQKpSCGnN3_Kt7emR2rbKOccUqylzUyUlAnkeyPs_ZZnVPpJ-DWdPvs76TjDBkFC0pBAbZgc3azO2T9fODosyEYxdYFq0L_CvT2Zn8gBt_yJUV3FFT3MEtRqKJmdHNoCHdygl4VqBk-x0kckRlP9oqyfjefP8qVLn9Mu-jL-Wyo8KDWrgxetyEpeJIWW3_kf8Q1_2CrwK8gL0d1LJLaHHPa1gxxVOA8SzpHYuVvKgLtifUxCVq_nyVDpZT7PwwfE9XMbutgM_jJjrz8s_bQJ1JwqibfDrBR0U5GMtUaVY7ykFURPIZmHfl2R_vHyoz0xdbhZq7U11h2WVfQSw9LGYG7NjCryo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
🔥
👀
۵ گل زیبا و برتر اولیویر ژیرو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/102424" target="_blank">📅 15:05 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102423">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a3bfea056.mp4?token=inBN7lvOH8hovwQv33D0yAb1Cjwh7Qlya4ef-xnuoU6s6MFyqqeRFRV0dukCz-dWIefi0PwBxlZX3w5eG1eDIfHq41V9DcWhI9ZQ0nJZAtO9MtzD_hH_r0pNK1jPJpYUiHPwqfQnYmULn4Gyyiacjac2EhbioHNWwhEdE24vknr_6SOmiZwlVh14yezA0SG-spovpxNNVDKD4MhCiudfgtmD7L4SWF69N73Ui0THIJEoqTXKdbXQEaJeAcjDuI-k5UTj30ZvhrMUbgNm3KO_nQIsdA2sCNFBLfRp74qlirURBPxaiTR5_KkcEOiHoYKGXB8__I-E2t2iJzKYEDVqIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a3bfea056.mp4?token=inBN7lvOH8hovwQv33D0yAb1Cjwh7Qlya4ef-xnuoU6s6MFyqqeRFRV0dukCz-dWIefi0PwBxlZX3w5eG1eDIfHq41V9DcWhI9ZQ0nJZAtO9MtzD_hH_r0pNK1jPJpYUiHPwqfQnYmULn4Gyyiacjac2EhbioHNWwhEdE24vknr_6SOmiZwlVh14yezA0SG-spovpxNNVDKD4MhCiudfgtmD7L4SWF69N73Ui0THIJEoqTXKdbXQEaJeAcjDuI-k5UTj30ZvhrMUbgNm3KO_nQIsdA2sCNFBLfRp74qlirURBPxaiTR5_KkcEOiHoYKGXB8__I-E2t2iJzKYEDVqIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇦🇷
سه دقیقه با لیونل مسی ورژن 2014/15
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/102423" target="_blank">📅 14:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102422">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rywlk-lHzeNCeoeNN_Jiqx2xrNkirD6Vu503ukSJHy5a53Fqd6feQcP956JIBaM8h-1nm5YfqPTwkrWE5iNbrywnhDt5WdB0TygfginqH89hg8RWGb2zGKrxYSdEFOP0pQE4QCnGnTn5LSzFliJQX4A1egRiJbQzX5D85R9R3Aivzo_Yg3xKElYIysI9HX9nDyfGeY8IcDO0SW4XfftbzaIEykBFOhCAClljRSOpKBXvYzshWo8npqy00R0jkrW07_c9WQ19OSBXTcTDGHPabEyn2R3xYr4wl5w2WOE8gcGRiLnoWn5dKLZ89VEsYtu2jUROeeH2DE4vI5E9wPkjYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
لیست رئال‌مادرید برای بازی با فیورنتینا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/102422" target="_blank">📅 14:36 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102421">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L0ZBbWq5loshZJ6Jw6jKA2YRi7w-LzEGOHvKahPWpW7XNE3ZKN-OphaNBUX9ASFDdSTLjYlHNlPm9mInz8wBAx5JxemcpDCTOzE8UaiWOIGAPyKk95YyLtHVGKD0-44A8MsDmcZ9o9flRerclvKkI9tdH2nGezdZTKzwRCGNoOC3aknhsUr2B8WZNvbK-Dg0yLjM2sChpPM0nkfQda2y9vnFPukhPux3wuy_ohu8lzttFnUEtfoKBlp0Moyb5uY7QXQnpKzTrfmO1IBoK55IlaL1_XeC6TKAb74VKD95sJSTHjJXdkBDu_8x1wT-ZEPQwuxQSRlx_eBXAKaud0_Hlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🗞
#فوووووری
از نشریه اکیپ فرانسه: آرسنال با نیوکاسل بر سر انتقال برونو گیمارش به مبلغ ۹۰ میلیون یورو به توافق‌نهایی دست یافت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/102421" target="_blank">📅 14:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102420">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/529b07ca6f.mp4?token=P-2j7ZHXIPyArZpKhltpMbvbIIXhwtfz1Wet7fxpq_51Xj-1_hb-QAtC5Fmq-XHnWYZnxlqAVWUpetlm0oZKGX4anuDAAJQHzFYduglTADZ8B_6WGPZ6GXDD1M3zllKj2EOGQQctC9nixZHJUeywgNyTUfN1cNojppBMeDQ1F3x7w08swEDIkB7jO-OPSJvALuPtYpjiSE2ro3MBo-Bw_OA_4tao2c6okxqHBsU3O2kKp0oUDlkzxTkFZDDszUJQIwXsZCqcD73oKPjFljlGyhv66Os-HpMY8myC_ThNdzKkOOvljH6L3WBmcgqFc20FOT39ZD71P7ZSSXVvoyWtTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/529b07ca6f.mp4?token=P-2j7ZHXIPyArZpKhltpMbvbIIXhwtfz1Wet7fxpq_51Xj-1_hb-QAtC5Fmq-XHnWYZnxlqAVWUpetlm0oZKGX4anuDAAJQHzFYduglTADZ8B_6WGPZ6GXDD1M3zllKj2EOGQQctC9nixZHJUeywgNyTUfN1cNojppBMeDQ1F3x7w08swEDIkB7jO-OPSJvALuPtYpjiSE2ro3MBo-Bw_OA_4tao2c6okxqHBsU3O2kKp0oUDlkzxTkFZDDszUJQIwXsZCqcD73oKPjFljlGyhv66Os-HpMY8myC_ThNdzKkOOvljH6L3WBmcgqFc20FOT39ZD71P7ZSSXVvoyWtTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❤️
✅
یوسفی: زمین و تماشاگر که ندارید، لیگ را پلی استیشنی برگزار کنید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/102420" target="_blank">📅 14:02 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102419">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9889076a09.mp4?token=ligMdqapXWUeSUbke9KuZoLiuLT1s_n0IXtW96I1W1v2fdEYifk2SkfF76IXipGhHnN2rm9fpdPRO1auoPBMM8DrYZTrz8pPZKAsFMtcG3Z8zsneXPbEh9rJdWm0ndwRL83X1DPHcGfCeCW8NXBqBqxMI5kImHaTTApbrRX7ZMKkwXyzJrbu-Eivaa-bDR_nVEGtNnUNZYLWlhCUfskn5PRvX7BYlg6ySjcDFpbvl1zxJQtmkeNAH8hT8FPWXqB-u_NMvL8Nag45vpO0OPojhlIJQLJ7ZYNuX9-tbNr6v0PMOwkvD9KeLYgUpDL-2PdMO179vVYLxmer5HM90EtSMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9889076a09.mp4?token=ligMdqapXWUeSUbke9KuZoLiuLT1s_n0IXtW96I1W1v2fdEYifk2SkfF76IXipGhHnN2rm9fpdPRO1auoPBMM8DrYZTrz8pPZKAsFMtcG3Z8zsneXPbEh9rJdWm0ndwRL83X1DPHcGfCeCW8NXBqBqxMI5kImHaTTApbrRX7ZMKkwXyzJrbu-Eivaa-bDR_nVEGtNnUNZYLWlhCUfskn5PRvX7BYlg6ySjcDFpbvl1zxJQtmkeNAH8hT8FPWXqB-u_NMvL8Nag45vpO0OPojhlIJQLJ7ZYNuX9-tbNr6v0PMOwkvD9KeLYgUpDL-2PdMO179vVYLxmer5HM90EtSMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
💥
روزی که پیتر چک آماده ترین گلر آن دوران فوتبال میخکوب شد و این اثر هنری شاعر رو تماشا کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/102419" target="_blank">📅 13:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102418">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EteR7XqaN5FUFgLlu8vFNX0_Ki3NNllHo04vCpjlVF_9v8CtrAun7pD-xHWe7QOkgiMnBaseSRrWEvLWswUyIJeCwsYQ8_5n6UaVNNas8JXlnUL8PV_46GNPwTJnLvj_82i5Su6Ql-IxdRrRe995HYPnL_Qq9h2Adpr4aI2TQ-o166-uNthzenKVnND1yNxxV4PzHwDhB-tZbzxJKRQdULi0KupU8mPMtqm_JE0yLd4FfDZ2hCSAo2nzrQN3ltkg9cgMi2JAspz6nMR_z6QcwsDVNt-r9aRlbI1E8dUOQPN6s8LNjl99oqOXxwqs0RBT3_o_FuOcb2SaIHxH77NqaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
کارلوس اسپی تو تمرینات رئال مادرید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/102418" target="_blank">📅 13:37 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102417">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YFsubHB4HPc3NDVspKB5sf82GciA4_ImB1xkQ7AJ4WJJSbJ07irfQbVBXuWkj0tHYLbJreKFgHcl_hdB9qEezM1b115qxmCYoDzFm4NIZ6S3KpSmlWACwg8V8UGv9lJ1BiWDgUv1wxZAm0cze_9OGayhuHSNri5SM6mLSOqqYaUayALeQKrKb42utQe1ly27Ddlebd6edBZeBT_y0Gf6BQMPp7L72UauCYwXwruToBs-iiMePAPsbwjSYkLSm5aY-fW7IHxEq3zPMragAJPF1MBHwcpATyBgJrSlwP5iJ205qeVsLC4ysmpxFMz2XO1L7UbPyfmFtVe7NpThfDXy5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
روزنامه اسپورت: دو باشگاه آرسنال و تاتنهام به رقابت برای جذب فران‌تورس پیوستند!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/102417" target="_blank">📅 13:32 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102416">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4938ae1d8.mp4?token=XPbjlkJf9SiLoeo4rC2LUhrl3XSKByIqCortcUDzSW6yuwWql6wqXjPT6Ervbep4LgYFtSgodFCgkm2E1tSmLuiaU_GLUpWvUMc5My5MfFa6P0GOqPzl9cU6etN5DY2jvNZv-OePuUi-FcQqv0UVbRPIp8brV1kXyVuxv_Bl1hS-r7zBZhnwLVTLCXpB915ZZHR4RWkCgxaO_wRLkxt8eIyQFKCwMX2Yys6J_m3Uurq_nFJ0jcWCo2EG7yI744QdE1GZJpkQeusZk9m8Y8VysYFQznLLAHCAZon2AyGbVFx6L3CAkKlngxOdrjW6hcl-reZ5Dwl1e_S9PIOB22KdNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4938ae1d8.mp4?token=XPbjlkJf9SiLoeo4rC2LUhrl3XSKByIqCortcUDzSW6yuwWql6wqXjPT6Ervbep4LgYFtSgodFCgkm2E1tSmLuiaU_GLUpWvUMc5My5MfFa6P0GOqPzl9cU6etN5DY2jvNZv-OePuUi-FcQqv0UVbRPIp8brV1kXyVuxv_Bl1hS-r7zBZhnwLVTLCXpB915ZZHR4RWkCgxaO_wRLkxt8eIyQFKCwMX2Yys6J_m3Uurq_nFJ0jcWCo2EG7yI744QdE1GZJpkQeusZk9m8Y8VysYFQznLLAHCAZon2AyGbVFx6L3CAkKlngxOdrjW6hcl-reZ5Dwl1e_S9PIOB22KdNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صحبت‌های بامزه رونالدو از ارتباط صمیمی با پسرش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/102416" target="_blank">📅 13:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102415">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5029f55db8.mp4?token=v1LZzdyZc_QPndIy4f580icj87kauh6VV-S1Ji3-7pERiHV2AWA7vKymm3baHJu0ib_XeE7jjg0dki4e9Ar-9wp5vWJgO5N4ZC76u9KwalAS8GapDWZ10n4DGIdIfg_qgPkTU3cBPGmr8ipCUNnDh2lb4UEeDnDgWMHux0ZLUm-KIjldTZ1QfEOnjnlmE5QA_Tfw4xNCfqxL1P6SoheuNBEqC4kAlC4V1qcaW9FH7P3mYYxnpHjvYFD2Sbr2bukY9wa7S5__k5aleU1DM2hLQXwB9kw3cIwZyN7elGOOxdbg-E3Z5RPD6uMHeeyad_JAgKlu3K0lfoynVI2w4yISjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5029f55db8.mp4?token=v1LZzdyZc_QPndIy4f580icj87kauh6VV-S1Ji3-7pERiHV2AWA7vKymm3baHJu0ib_XeE7jjg0dki4e9Ar-9wp5vWJgO5N4ZC76u9KwalAS8GapDWZ10n4DGIdIfg_qgPkTU3cBPGmr8ipCUNnDh2lb4UEeDnDgWMHux0ZLUm-KIjldTZ1QfEOnjnlmE5QA_Tfw4xNCfqxL1P6SoheuNBEqC4kAlC4V1qcaW9FH7P3mYYxnpHjvYFD2Sbr2bukY9wa7S5__k5aleU1DM2hLQXwB9kw3cIwZyN7elGOOxdbg-E3Z5RPD6uMHeeyad_JAgKlu3K0lfoynVI2w4yISjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🔵
درخواست کودکان جنوبی کشور در وضعیت جنگی از رامین‌رضاییان بازیکن استقلال!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/102415" target="_blank">📅 13:01 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102414">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ac78119da.mp4?token=c8z2cbeLKgt7OoFzChOGLNUoF4hl_uk5aH3mxNSZMcN_rwZRw7u8wlPDy4XG4PslKLVly4QUA8UEDLuACjKVedJMtJR-1_6Cm97smGGAAjKK41YrBji2ONgr-DbIjxAHQFECvJyRHJPb3M4Lpqei1GIYqEuC_4jSPrdhe4nU8eQxqYB5CesUBryGAK5qVJdwFTr1Xx6hIOtMJyNd2NwUXE9cWuQpxp4hJS4SpOc7WTiNR9n3n8nKlrwghTblatLxqL3bEDWVZzKHNIwBxzfi13MWqMi36kQ6kmgra8sD3ZtQH-Ew84d8Jxkq81_FJnAitqqbYMw7JxxgLXxZzOBDAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ac78119da.mp4?token=c8z2cbeLKgt7OoFzChOGLNUoF4hl_uk5aH3mxNSZMcN_rwZRw7u8wlPDy4XG4PslKLVly4QUA8UEDLuACjKVedJMtJR-1_6Cm97smGGAAjKK41YrBji2ONgr-DbIjxAHQFECvJyRHJPb3M4Lpqei1GIYqEuC_4jSPrdhe4nU8eQxqYB5CesUBryGAK5qVJdwFTr1Xx6hIOtMJyNd2NwUXE9cWuQpxp4hJS4SpOc7WTiNR9n3n8nKlrwghTblatLxqL3bEDWVZzKHNIwBxzfi13MWqMi36kQ6kmgra8sD3ZtQH-Ew84d8Jxkq81_FJnAitqqbYMw7JxxgLXxZzOBDAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
⚠️
نصیحت اسطوره‌رونالدو به امباپه
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/102414" target="_blank">📅 12:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102413">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🤩
#فوووووری فابریزیو رومانو: آلن هالیلوویچ استعداد برباد رفته بارسلونا در آستانه امضای قرارداد با پرسپولیس قرار دارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/102413" target="_blank">📅 12:34 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102412">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75b732a95e.mp4?token=Izrc80HCjYv9FhwZfqoTxtH7Gxq5iWZmPCdh9pH0j2o6owm-wZ95H1PGFonyeWBKYu19ZTXgHvhex6ANzIlkiKj-nD59_jmQBACumb8kc66eRMvlMIymtmciL5o--c7IBLp7aq4WdNnPAlEpTGfa5PZlDakZq0IlSJtCTqfZ_7Dc0Q6gVJQ7WGIYNHHxb85crRgeOMrQqc23kf5zlc06NkzcyzOpff3zPFGBW0w6S1KxqKNtwVUv7qFTdpebeHJu0gxB05B-EBialBQ3h4EXXJ8rVV0Pw6vMM0IiwEfeBde044I5PGyOohJ9T2N_3qD16P3hsyr7xT0PX0r_dG4bsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75b732a95e.mp4?token=Izrc80HCjYv9FhwZfqoTxtH7Gxq5iWZmPCdh9pH0j2o6owm-wZ95H1PGFonyeWBKYu19ZTXgHvhex6ANzIlkiKj-nD59_jmQBACumb8kc66eRMvlMIymtmciL5o--c7IBLp7aq4WdNnPAlEpTGfa5PZlDakZq0IlSJtCTqfZ_7Dc0Q6gVJQ7WGIYNHHxb85crRgeOMrQqc23kf5zlc06NkzcyzOpff3zPFGBW0w6S1KxqKNtwVUv7qFTdpebeHJu0gxB05B-EBialBQ3h4EXXJ8rVV0Pw6vMM0IiwEfeBde044I5PGyOohJ9T2N_3qD16P3hsyr7xT0PX0r_dG4bsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
🇧🇷
آنچلوتی: "در هایدریشن بریک نیمه دوم بازی جلو نروژ اشتباه کردم تیم رو تغییر دادم که باعث شد کنترل بازی از دستمون در بره و ببازیم..."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/102412" target="_blank">📅 12:24 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102411">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2964e2f72d.mp4?token=EBZeBcWkmOwxfU2mt07N9FAuluqdkzMLCEdAPkYOHpLK9HhcNouUF7dc52Pzebfb87ITNWcAQiwJuTzaZNgJdjLTTBnqXvb25bltLzjxR9eThanlcUgOyJ2pH3YHCTL5PebSD3wZCsfcuiIitgTrh1d7yA4KB-oIK4T7s60A7nklMqL01w9f7bUQkwEd9ZkTJsvKi21A__HkKhQHkS8WQhSk3pDhprXCb2vTMQHlRVGgHiHFm8lQzd47s4qBMRyAwwJ23qBFWqmHhBq0SYBUc5x3QMyj0Zo9SgvFrIQClOG617lPU5dfRatL-Z9rW9aHNYorgU0QSfd_Gx0BMauvjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2964e2f72d.mp4?token=EBZeBcWkmOwxfU2mt07N9FAuluqdkzMLCEdAPkYOHpLK9HhcNouUF7dc52Pzebfb87ITNWcAQiwJuTzaZNgJdjLTTBnqXvb25bltLzjxR9eThanlcUgOyJ2pH3YHCTL5PebSD3wZCsfcuiIitgTrh1d7yA4KB-oIK4T7s60A7nklMqL01w9f7bUQkwEd9ZkTJsvKi21A__HkKhQHkS8WQhSk3pDhprXCb2vTMQHlRVGgHiHFm8lQzd47s4qBMRyAwwJ23qBFWqmHhBq0SYBUc5x3QMyj0Zo9SgvFrIQClOG617lPU5dfRatL-Z9rW9aHNYorgU0QSfd_Gx0BMauvjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
‼️
جواد موگویی که اخیرا در گفتگو با عراقچی یه سری اطلاعات حساس تهران رو داده بود، این سری اطلاعات مسکونی مقامات نظامی و ... هم افشا کرد
😳
😳
😳
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/102411" target="_blank">📅 12:17 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102410">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b5a4f433a.mp4?token=aeCm49yvCWSiL77lQU-lI0JqQz61z-hMB8_QgN9cl_zOIFPX-DfFIy_6nemxPliq2dZTyEIA5Fb6Cv2quKZOArZZjYvF12_ykZ--5eA1nar4bVszh2i2aT8apdZIJaHQg4uVfQGPcuQXijYV7VKTd7jKeUhA7WM-3AyicZ9Ou5i1LLCtQcIn9UiObem6ExSxtrDWUxInZ6oeLjDw2jpZP7WK59wi3FQ7F--zNya88YHlIazTwam0_hUpwH9FKmPHHYRwLpa2chbqBVq8IgWX8lWj9Bj5Qw5ROlkM7XnL3vHFAnjqGJMDD93a72RHQ0TzeF5yOX_Y3lQMNepVJKcFWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b5a4f433a.mp4?token=aeCm49yvCWSiL77lQU-lI0JqQz61z-hMB8_QgN9cl_zOIFPX-DfFIy_6nemxPliq2dZTyEIA5Fb6Cv2quKZOArZZjYvF12_ykZ--5eA1nar4bVszh2i2aT8apdZIJaHQg4uVfQGPcuQXijYV7VKTd7jKeUhA7WM-3AyicZ9Ou5i1LLCtQcIn9UiObem6ExSxtrDWUxInZ6oeLjDw2jpZP7WK59wi3FQ7F--zNya88YHlIazTwam0_hUpwH9FKmPHHYRwLpa2chbqBVq8IgWX8lWj9Bj5Qw5ROlkM7XnL3vHFAnjqGJMDD93a72RHQ0TzeF5yOX_Y3lQMNepVJKcFWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔵
🔴
‼️
علیرضا بابایی مدیرعامل چادرملو: تورنمنت سه جانبه به دلیل کمک به پرسپولیس برگزار شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/102410" target="_blank">📅 12:06 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102409">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c746b16b5a.mp4?token=RzCkqd1wndnwMQgUAB0b7tNjMm1N0Z-jLV6ij4NsvAWp4EKK3xcnLtHzj4iR6q80hxWwmbXKyXPux0We230jTzkej0muGtN0wenNU9T57Yns3vmcNWPbcWnfabHA2HSdWjeIYPE-x4XnawTfkgh8WQ9mtBejIBWa0UUb1KcLeQQfyTngoCqmrYzEo_uXquvDW7WmQjTDTDQHsfcwrei3TxjAyZ6GHEmpa3kXtYNMJjPUFv_EOThasMwhvPg52C1amhl95cfof7bbCEWYauRD0SQ8d71Y27Dt0Fg1Pu959gu-mOo80IusxhJ57-BYouEb_JVqTBs0eLoIsLmGze9dAF4f5aplsbngjmtaIV_V9DNhsbyqjPiMO7AUyR1lUmiXTZFPwreoPH9cPoGCuQooDtPiHryHQ7Es9XXDTaTS9uVwRXqn_JWPN1KsoEKN7-w6kRY4sc6GIjYEZ3JQKFjyRqArKBA6Y7MQIrHEeYgw6L22iwBqGANrWncraMlfkIG0BLUxv3lu8yvRss5OmF8rSaXpSTardjH-ywplPDoOWsYEWVOGNrlKfgKLfCGUHslaJk3j3N1ICtu14vq1X1rPnkHCo0uN7U13CapnWUtW7bltKNNfmmMCDdpnWKwtp8h_rNE0-l_jXNHxn-Uc4v6K55nhEIsnU3baVjbpDyMijPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c746b16b5a.mp4?token=RzCkqd1wndnwMQgUAB0b7tNjMm1N0Z-jLV6ij4NsvAWp4EKK3xcnLtHzj4iR6q80hxWwmbXKyXPux0We230jTzkej0muGtN0wenNU9T57Yns3vmcNWPbcWnfabHA2HSdWjeIYPE-x4XnawTfkgh8WQ9mtBejIBWa0UUb1KcLeQQfyTngoCqmrYzEo_uXquvDW7WmQjTDTDQHsfcwrei3TxjAyZ6GHEmpa3kXtYNMJjPUFv_EOThasMwhvPg52C1amhl95cfof7bbCEWYauRD0SQ8d71Y27Dt0Fg1Pu959gu-mOo80IusxhJ57-BYouEb_JVqTBs0eLoIsLmGze9dAF4f5aplsbngjmtaIV_V9DNhsbyqjPiMO7AUyR1lUmiXTZFPwreoPH9cPoGCuQooDtPiHryHQ7Es9XXDTaTS9uVwRXqn_JWPN1KsoEKN7-w6kRY4sc6GIjYEZ3JQKFjyRqArKBA6Y7MQIrHEeYgw6L22iwBqGANrWncraMlfkIG0BLUxv3lu8yvRss5OmF8rSaXpSTardjH-ywplPDoOWsYEWVOGNrlKfgKLfCGUHslaJk3j3N1ICtu14vq1X1rPnkHCo0uN7U13CapnWUtW7bltKNNfmmMCDdpnWKwtp8h_rNE0-l_jXNHxn-Uc4v6K55nhEIsnU3baVjbpDyMijPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🔵
علیرضا بابایی مدیرعامل چادرملو: بازیکنان را از پای دیگ نذری آوردیم و با خواست خدا پرسپولیس را شکست دادیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/102409" target="_blank">📅 12:05 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102408">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1b81246b4.mp4?token=hTfDp_W3Qa--rmRTY5hUPsEqYi0632tXR0DNmRz4hEVZcH-BsPUMi5m0satUgTJu8agFfe_FjxYc2NxWLLXTbG7ddPg4TMwxMZ-OaTBtEdsUxoT884FQqfzwlRpZWMNZZmHmvXZUEpb9ykLb9Gu-N3IFiH-_5GfEdnQdPHXTUaoSO5OaHCbishizOMaT1oZ9_eCwrxJJLcoRhJ5pO-E_y5pNg0kJsAsX3VBDX6t9QRyPtN-jIULsx7SiFLB7LIw9LrGNm-JYe6YSLoQoz0FqmQrSYBvqhlpyxfJpeYYK5NQ5R822CtidJheFTBrzk6rDu-teCWjKukRgtKX5knvXvXVoYiqY9nTVpzEQqCiHeC_jwIuv5iiRTF7P4dunYfuXsTVNGdQujlQL3MvEMRukirn238SlZULPoBP466JMCwYY6XaDOy4SdVjJqr_2RhI-4l6EvfHzRWlqb-3J2kLbBssy0L22mCY6PTxX64Z5IQ-FZL7syZbW_GN6JaByBm1dDArvlX_ErfFJiVXtKTcFMBzuC_5DQh-03wS_HRcs2IKpF4G6vud7MhisQ_1s1r8vgbVP6n3EwsVl8K7tnFqXbKkk0q18OzR-dGXqqQFCffxXGL1PcfYrJphor4-_AWBii8z_qEKtMF0br2Qjsldt4g1TmqwQFggGfenOPmQVvNU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1b81246b4.mp4?token=hTfDp_W3Qa--rmRTY5hUPsEqYi0632tXR0DNmRz4hEVZcH-BsPUMi5m0satUgTJu8agFfe_FjxYc2NxWLLXTbG7ddPg4TMwxMZ-OaTBtEdsUxoT884FQqfzwlRpZWMNZZmHmvXZUEpb9ykLb9Gu-N3IFiH-_5GfEdnQdPHXTUaoSO5OaHCbishizOMaT1oZ9_eCwrxJJLcoRhJ5pO-E_y5pNg0kJsAsX3VBDX6t9QRyPtN-jIULsx7SiFLB7LIw9LrGNm-JYe6YSLoQoz0FqmQrSYBvqhlpyxfJpeYYK5NQ5R822CtidJheFTBrzk6rDu-teCWjKukRgtKX5knvXvXVoYiqY9nTVpzEQqCiHeC_jwIuv5iiRTF7P4dunYfuXsTVNGdQujlQL3MvEMRukirn238SlZULPoBP466JMCwYY6XaDOy4SdVjJqr_2RhI-4l6EvfHzRWlqb-3J2kLbBssy0L22mCY6PTxX64Z5IQ-FZL7syZbW_GN6JaByBm1dDArvlX_ErfFJiVXtKTcFMBzuC_5DQh-03wS_HRcs2IKpF4G6vud7MhisQ_1s1r8vgbVP6n3EwsVl8K7tnFqXbKkk0q18OzR-dGXqqQFCffxXGL1PcfYrJphor4-_AWBii8z_qEKtMF0br2Qjsldt4g1TmqwQFggGfenOPmQVvNU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
🇪🇸
مشکل ایمنی ورزشگاه‌ها به لالیگا هم رسیده‌ و تیم رایووایه‌کانو نمیتونه از استادیوم خانگی خودش در فصل‌آینده استفاده کنه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/102408" target="_blank">📅 12:02 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102407">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47a01fbf75.mp4?token=XzEt7Y7hISi-cDjUUgKb6k75w9H0-AfgB5Ey-Khfky_R8TkncnLhZF_3ygZuwHZBfu7IRemZV1gniDuGFpuMDhNh84gqwTbo7Ga_DxOc6mc0LemHlxDmFTIWqiy1WPxXHsjOAMsj28qEKe4PkHxkguKS3G5NqzXdzrWdqZ5zehqUDEkXa-jEM_qPUYoohFI591QM_P2qkvyekEpv5gqbY_Nqt4SSQYHok2OXgtIFETF7LlIZlWZX5YoPytcH2XZfrzMYedfVoHk2F-xdDyQTScytQZY2HQeMztPAoE6qQU46EyBLrphxONzDqRlqTaztfaONTigENqK_JWH9Gv-stg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47a01fbf75.mp4?token=XzEt7Y7hISi-cDjUUgKb6k75w9H0-AfgB5Ey-Khfky_R8TkncnLhZF_3ygZuwHZBfu7IRemZV1gniDuGFpuMDhNh84gqwTbo7Ga_DxOc6mc0LemHlxDmFTIWqiy1WPxXHsjOAMsj28qEKe4PkHxkguKS3G5NqzXdzrWdqZ5zehqUDEkXa-jEM_qPUYoohFI591QM_P2qkvyekEpv5gqbY_Nqt4SSQYHok2OXgtIFETF7LlIZlWZX5YoPytcH2XZfrzMYedfVoHk2F-xdDyQTScytQZY2HQeMztPAoE6qQU46EyBLrphxONzDqRlqTaztfaONTigENqK_JWH9Gv-stg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
ویدیو وایرال شده از صحبت‌های تلخ و بامزه یک ایرانی حین ورود به‌تونلی در بندرعباس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/102407" target="_blank">📅 11:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102406">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/262957043c.mp4?token=n0_YmwG4LIqx_NN_zOTqfcuSU-qvKHy_3Ti_VGOnH0uvu-LNjTLrjypURbmEK4ebHvQT148GAd-ibqtXyq_FFdGPnLWSX1ct3gUVrKRy_TcHNqeGnSaMLzvM0kI_kYRyisbCEVrMf6qOFtXXXeK5PkFJ0qGHfGlNQClWUZwFoJPVPey05SOZ9Epnbg8rxrRQ8PP037U9nKW3yiyor2aPuMOyGrdXv7mQ-ovO0zDvjlZaC8k1kMJDDwOZfjDxsD9dBl39AGnZpM9pE5V8wNyY4DEStJPxW8OCcbfJfVYoV5slVbvwGSg-Mm3vSEUW3QXnzBPehNE8oqISUllAtKTNgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/262957043c.mp4?token=n0_YmwG4LIqx_NN_zOTqfcuSU-qvKHy_3Ti_VGOnH0uvu-LNjTLrjypURbmEK4ebHvQT148GAd-ibqtXyq_FFdGPnLWSX1ct3gUVrKRy_TcHNqeGnSaMLzvM0kI_kYRyisbCEVrMf6qOFtXXXeK5PkFJ0qGHfGlNQClWUZwFoJPVPey05SOZ9Epnbg8rxrRQ8PP037U9nKW3yiyor2aPuMOyGrdXv7mQ-ovO0zDvjlZaC8k1kMJDDwOZfjDxsD9dBl39AGnZpM9pE5V8wNyY4DEStJPxW8OCcbfJfVYoV5slVbvwGSg-Mm3vSEUW3QXnzBPehNE8oqISUllAtKTNgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🏴󠁧󠁢󠁥󠁮󠁧󠁿
سوپرایز خاص‌ ژابی‌آلونسو برای فصل‌آینده؛ رونمایی از ستاره ۱۷ ساله قزاقستانی چلسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/102406" target="_blank">📅 11:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102405">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef2180d890.mp4?token=UnPIE_XkIgYljwrt_Qj6FsE0FaCB4AWzN2ZlSZYRSDiKTvKJKOXYE2_JJPLctjZOXqornLZayscHCJgehbsjurnCZIepvwfHdO6cf2TMpiSwgvx5GitND_U6hQU8Ztf34ML0fnW8sdAsiF4GB7g_eqfPdpaZXZ7ZasummX7hRwmbu_okuTBDQUdE4DeoJ0OP-RizUtn39Ez2GI_trdR3qRK8La_k55ZamIcUaNxoI4DqkV9wQbuNim5T1oIB2-_XzUIRuizEwG6DqJq9zUDYulgPyUnUF5FAPoOLT82XuyRcju_2jlkrvW9w4MyAGIKO2rJrsdWQONr89MM_AckU-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef2180d890.mp4?token=UnPIE_XkIgYljwrt_Qj6FsE0FaCB4AWzN2ZlSZYRSDiKTvKJKOXYE2_JJPLctjZOXqornLZayscHCJgehbsjurnCZIepvwfHdO6cf2TMpiSwgvx5GitND_U6hQU8Ztf34ML0fnW8sdAsiF4GB7g_eqfPdpaZXZ7ZasummX7hRwmbu_okuTBDQUdE4DeoJ0OP-RizUtn39Ez2GI_trdR3qRK8La_k55ZamIcUaNxoI4DqkV9wQbuNim5T1oIB2-_XzUIRuizEwG6DqJq9zUDYulgPyUnUF5FAPoOLT82XuyRcju_2jlkrvW9w4MyAGIKO2rJrsdWQONr89MM_AckU-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
آماده‌سازی استادیوم نیوکمپ برای فصل‌آینده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/102405" target="_blank">📅 11:04 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102404">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b31c9897d6.mp4?token=kAXXN6j-M9Cn94WEzXUS-LoPZO-XiGqjlUU9sA1cod_29-_TBINZjjVCgaTq8hfe7dWPwB8QFybty2XMqFSYG3qIuYFLHllkM3US3FRlBlXUGUI6FWBEjLmLMr74Lj2ftAVMXREqrkmQT9AvA8IriRNdANpJk5I1gGaRmmtzqpp_oRTYsOiQP6ah2hC-mVyZSYmCwc5SVSo9R9SgOvDlYSvB_Hq39WMuZUehBM2UcRKkMF5s9fcwxFy31A4KbX74azjKGwsPTnecrt2yJkwFEzwCydKSh4tPgGTNZG_aIkBODTnblNblDZk-kqqrxbmJoP5wPcI-tIZbRrzBD9hLgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b31c9897d6.mp4?token=kAXXN6j-M9Cn94WEzXUS-LoPZO-XiGqjlUU9sA1cod_29-_TBINZjjVCgaTq8hfe7dWPwB8QFybty2XMqFSYG3qIuYFLHllkM3US3FRlBlXUGUI6FWBEjLmLMr74Lj2ftAVMXREqrkmQT9AvA8IriRNdANpJk5I1gGaRmmtzqpp_oRTYsOiQP6ah2hC-mVyZSYmCwc5SVSo9R9SgOvDlYSvB_Hq39WMuZUehBM2UcRKkMF5s9fcwxFy31A4KbX74azjKGwsPTnecrt2yJkwFEzwCydKSh4tPgGTNZG_aIkBODTnblNblDZk-kqqrxbmJoP5wPcI-tIZbRrzBD9hLgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
پاسخ‌تند و کنایه‌آمیز مهدی‌رحمتی به صحبت اخیر معدی‌قایدی: بذارید تو‌ توهم خودش بمونه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/102404" target="_blank">📅 10:46 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102403">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
✅
کیت‌دوم فصل‌آینده منچسترسیتی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/102403" target="_blank">📅 10:37 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102402">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/869e38d1a5.mp4?token=TJEOIp7dNRPZgckON6clqMBnqc4fs22cZ0n47l0IcMTAY8iuL0RLCsZD8qEoMjGd3zcvhhQWELnDcqww_HgvENDG4yEodMR_wyiD3WTVdX-IIZiTwsEQt2iKhlwUdgqRuUVbSqKfAN6Ejh6vfVYXbzz5fyRuby7Mimqu1pY4NP7Nz5aNSM5nCRsexxUzNqrj-rZA3Ha384ZFtfGRmxuO_OAeaoZ95pjRbS1y1K8RHmigfPToslndIHTSE4kE9SdusaccrWnr5h94cBQaex2H924JrvBrvg9A8p3f5U0yZsS_AnZBpQvPqPB-kxzoan8d4CDAf8E4sg-dYTUmrGOaDoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/869e38d1a5.mp4?token=TJEOIp7dNRPZgckON6clqMBnqc4fs22cZ0n47l0IcMTAY8iuL0RLCsZD8qEoMjGd3zcvhhQWELnDcqww_HgvENDG4yEodMR_wyiD3WTVdX-IIZiTwsEQt2iKhlwUdgqRuUVbSqKfAN6Ejh6vfVYXbzz5fyRuby7Mimqu1pY4NP7Nz5aNSM5nCRsexxUzNqrj-rZA3Ha384ZFtfGRmxuO_OAeaoZ95pjRbS1y1K8RHmigfPToslndIHTSE4kE9SdusaccrWnr5h94cBQaex2H924JrvBrvg9A8p3f5U0yZsS_AnZBpQvPqPB-kxzoan8d4CDAf8E4sg-dYTUmrGOaDoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
درگیری شدید فیل‌فودن ستاره سیتی به همراه مادرش با چنتا از مردم در یکی از کلاب‌های شهر منچستر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/102402" target="_blank">📅 10:12 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102401">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f0266060c.mp4?token=gdYFGpOuizG6BBVJl2i7Ede6zT0kETkZURJBZKI3KkOcr-tTYzz5EnrLSb7Kmp2ZIxiZm5qSkJ9CBdx9O0IZK7AF7mXSkK-8MXqEhjOvn5tPngrQkS66z1GXlzgYEzoeWxv8MEndnE67-33IMIC_EXGgyYlNPuJCigQrKQgVTIgH3tQrnXJDY-_5w04KKUU7dxhzDA1FOYAZEhSPYgn1942V3uzznIg2KnzzEwJ65tvJGaAqrR1mO0nPjwxzfD5ADZ7TPfIaWFpmfE_Xz6OI3qNDORqNUcG4vPHDWzkB805Hb96HjgdgyJNNittHSsFR5VEbjKgLmUQJerYTdVv4XAHaZE9m61lGXY0sa-gAKAx_kC4wpFqfdcxrUxLveQ2eYsVSOYCo51ZCf4v-9HNy50hY6eL12OKegDQD1DJ3Lycbch0tKNLovxaqi_aQKxyfd8A8-KYo-kkd9-DpLDJe5Ua1pgYxyfBaleOsCa0Wr8m0PXqhiGHlHQahuwIhrzWi9SFzJUpLgnHkroOA4_I3yoiFiBe8RKORhLb4CQyOJfpjGuddxaLKPIonCZPnZuEKM4LMfYoDTxpt1kXT566-TgFFxcGvOq-qBOVJuMwK4mVl1BIkO8NZzbhpHVi4JSs4XCYE_Nq0KkHbyP6fpTgpAPWcUE8gSoHzCbMs16uC-Ig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f0266060c.mp4?token=gdYFGpOuizG6BBVJl2i7Ede6zT0kETkZURJBZKI3KkOcr-tTYzz5EnrLSb7Kmp2ZIxiZm5qSkJ9CBdx9O0IZK7AF7mXSkK-8MXqEhjOvn5tPngrQkS66z1GXlzgYEzoeWxv8MEndnE67-33IMIC_EXGgyYlNPuJCigQrKQgVTIgH3tQrnXJDY-_5w04KKUU7dxhzDA1FOYAZEhSPYgn1942V3uzznIg2KnzzEwJ65tvJGaAqrR1mO0nPjwxzfD5ADZ7TPfIaWFpmfE_Xz6OI3qNDORqNUcG4vPHDWzkB805Hb96HjgdgyJNNittHSsFR5VEbjKgLmUQJerYTdVv4XAHaZE9m61lGXY0sa-gAKAx_kC4wpFqfdcxrUxLveQ2eYsVSOYCo51ZCf4v-9HNy50hY6eL12OKegDQD1DJ3Lycbch0tKNLovxaqi_aQKxyfd8A8-KYo-kkd9-DpLDJe5Ua1pgYxyfBaleOsCa0Wr8m0PXqhiGHlHQahuwIhrzWi9SFzJUpLgnHkroOA4_I3yoiFiBe8RKORhLb4CQyOJfpjGuddxaLKPIonCZPnZuEKM4LMfYoDTxpt1kXT566-TgFFxcGvOq-qBOVJuMwK4mVl1BIkO8NZzbhpHVi4JSs4XCYE_Nq0KkHbyP6fpTgpAPWcUE8gSoHzCbMs16uC-Ig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁳󠁣󠁴󠁿
نظر سرالکس فرگوسن درباره‌مثلث جادویی بارسلونا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/102401" target="_blank">📅 10:00 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102400">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f864b5c9ce.mp4?token=UKPcElKguh2ahkdSwQdZpP98hZm-BXH4aAQ6isMLjWAZaJf4_5qs6eHaUJZQoUPnd__lA749f97UH5ryudQfHf0ajIIQwKAlzCWTol-bJyPy8ahUiTqu7FyPEIn0qk7gz6ZQunjpn-2vdpPZVYqhKUhGGKdil0P1KbYSmmDgYogYwQFG1svjfaJjbcTJh19jwqqRVgDbqQh2gxkLYvkSBjM-RpTVATvga9jwO_Nra51i02RiONC6DYTcuxA8L16goEgxTRo5h3jn1BDnCjjbMZel6YCXj_SV8NwAwkXemGRF3bRRl7MJc3IhZRwSOEZENEqk2Yn4SzXq11qyVSJuH3-xsA-nH24t7Vw4oMECvEmpxBKWg1cSrMkfARP86gWBmzfOKgTRQhOvYwm68qjQd77XgZrffekFsSuN8BQI-Ugs7-VLjM3G0R48pDxLTvGimT0JskR6rl0dTdwx6hwrLzJ2B51GmMABA2s_sUsZG6wVqy38Gx4aGi0N0AmId7x23mjE7OZFnrPfQ8r8iexGP4_JzNKQf2__zipscBTjvUYPCq-VPatJd3FvgjKjPLJ2mV3Wl1M8YuUWKl93McWIkR0zMzpn0tRrvBQuqKTBM3iduGgUqkYhKWuCDgbiqa3koPg3eS0dqMAKdGMLN_tw3s9oYy1PnNFEmQ95h1CzePQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f864b5c9ce.mp4?token=UKPcElKguh2ahkdSwQdZpP98hZm-BXH4aAQ6isMLjWAZaJf4_5qs6eHaUJZQoUPnd__lA749f97UH5ryudQfHf0ajIIQwKAlzCWTol-bJyPy8ahUiTqu7FyPEIn0qk7gz6ZQunjpn-2vdpPZVYqhKUhGGKdil0P1KbYSmmDgYogYwQFG1svjfaJjbcTJh19jwqqRVgDbqQh2gxkLYvkSBjM-RpTVATvga9jwO_Nra51i02RiONC6DYTcuxA8L16goEgxTRo5h3jn1BDnCjjbMZel6YCXj_SV8NwAwkXemGRF3bRRl7MJc3IhZRwSOEZENEqk2Yn4SzXq11qyVSJuH3-xsA-nH24t7Vw4oMECvEmpxBKWg1cSrMkfARP86gWBmzfOKgTRQhOvYwm68qjQd77XgZrffekFsSuN8BQI-Ugs7-VLjM3G0R48pDxLTvGimT0JskR6rl0dTdwx6hwrLzJ2B51GmMABA2s_sUsZG6wVqy38Gx4aGi0N0AmId7x23mjE7OZFnrPfQ8r8iexGP4_JzNKQf2__zipscBTjvUYPCq-VPatJd3FvgjKjPLJ2mV3Wl1M8YuUWKl93McWIkR0zMzpn0tRrvBQuqKTBM3iduGgUqkYhKWuCDgbiqa3koPg3eS0dqMAKdGMLN_tw3s9oYy1PnNFEmQ95h1CzePQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
شباهت حرکت‌های یامال و اولیسه
🔥
😮‍💨
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/102400" target="_blank">📅 09:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102399">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5630cebcb5.mp4?token=VwO77NikwdRKioVUg2rlbKli-NzhLqM9cnVeVe1rbEaMJ8QEZicRvXKaoME8CpHRN5sCP5cautRtMBGICG-cWQgt9mp1VhDrWuKilaKBKsncGmGEmX1pBzz3Nuu5HYXcdBGPrBto5Um52EMGTE9lq4Sm3kFED9D0HoTMcMgOevF3_OSp4-dB60HJo7ycmqrmnvIgpJPqIcXeiFSHqyWveskK5SXF8pnPeCpKYIUXoqdWPTxqKZqsaWeuiLfPT7I9VO48PUv_RQCeGX5Au0mZQ5_utr-06w9UNOTUEgg70Fihlbd41NigLilf1_7xBNQyPVCDHAFyIHcUK1T4-v0neI1uyDUa5k7UOEmi76HTYuB4vUxzvwCoF0nhuKWNXlrryAe5IiHUUA899CcVR7D-pClnqD2peFVi6mo_SRDpfZSfFQTC5ijWCiARoKXoVj8NdcKLtlUcW-gEq3mJJStT1Kja1eASDa-W7BWwRErkioM6abUZ50IdPO5r99vSjg2A9R8L19xk8EBM5Bl32LGRfmlNDLhxfSI7HnESEVlJs_CDkwJ7bY38LA2xeLH5KJO1JQPqbz-F1phk7oQPXJSBLi1pZ4ueEQNlqj8bKoSFXoGhDtCm63fn_CjxrJEaXqdCWrim4ZtP0Jc8NPWXpp3GJ1zztS--7hz7SkvTbpztJoU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5630cebcb5.mp4?token=VwO77NikwdRKioVUg2rlbKli-NzhLqM9cnVeVe1rbEaMJ8QEZicRvXKaoME8CpHRN5sCP5cautRtMBGICG-cWQgt9mp1VhDrWuKilaKBKsncGmGEmX1pBzz3Nuu5HYXcdBGPrBto5Um52EMGTE9lq4Sm3kFED9D0HoTMcMgOevF3_OSp4-dB60HJo7ycmqrmnvIgpJPqIcXeiFSHqyWveskK5SXF8pnPeCpKYIUXoqdWPTxqKZqsaWeuiLfPT7I9VO48PUv_RQCeGX5Au0mZQ5_utr-06w9UNOTUEgg70Fihlbd41NigLilf1_7xBNQyPVCDHAFyIHcUK1T4-v0neI1uyDUa5k7UOEmi76HTYuB4vUxzvwCoF0nhuKWNXlrryAe5IiHUUA899CcVR7D-pClnqD2peFVi6mo_SRDpfZSfFQTC5ijWCiARoKXoVj8NdcKLtlUcW-gEq3mJJStT1Kja1eASDa-W7BWwRErkioM6abUZ50IdPO5r99vSjg2A9R8L19xk8EBM5Bl32LGRfmlNDLhxfSI7HnESEVlJs_CDkwJ7bY38LA2xeLH5KJO1JQPqbz-F1phk7oQPXJSBLi1pZ4ueEQNlqj8bKoSFXoGhDtCm63fn_CjxrJEaXqdCWrim4ZtP0Jc8NPWXpp3GJ1zztS--7hz7SkvTbpztJoU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
شیرجه زد، گرفتش، زد زمین، شوتش کرد!⁣ جوک خنده‌دار بیلی مک‌کالاک ماساژور سابق چلسی درباره‌ی پتر چک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/102399" target="_blank">📅 09:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102398">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/osf77JZMjnR1ljAUpHfggq72kLoeONKtp7WBnqIKkffUGW0rh46L9eP4lSvRCb2VG2qOQkBEwzYAqFXClZ-FGG0-brDcMhH2j0CU4UGcFSS52RBmFbOnuVWcWY2-P5rxJ-UYcsfROnMkguQ1P7DsZgPqJ8UGNZ0wY_nCjbz_mTr_AJzFE9gPPGTh3wLG9L3pWAw4E7iC60H3sY6DO6XJC6Newy_KsjbSv9s9Tshf-I4DMU-KF4PP2JaUfJNcE951EbpmLkNiD4MVOxPe5sNyAP_RO5GQFqnvr0fJU-xIj7qNByEEC-TOEsw-H9X39hNo4Tz1vHSXH0LLiKpINBYtvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖤
🇮🇹
لحظاتی پیش، فرانکو بارسی، اسطوره فوتبال ایتالیا، در سن ۶۶ سالگی درگذشت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/102398" target="_blank">📅 09:28 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102397">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d54a6dc02d.mp4?token=WeuxuNeMHExlXZ5NSCuMjONq0quGIyCYFpOoXpooFNNlTr5CVNihboOlma7ynArWPjXv3l-Q43KMXF31_2aOcB6tD40HweRhBJOpcHr9VfBDBYlqNzNQ_ySLZPOz2b8sQIv9hBxXBVMqD1qq9txmQJWc9lAFdjIA9NkIjwCTp4T5OCF6Ph5HJol1yWAKHw8S-jphvI0gI81ueVm718fMfx9LaF4C38G8DesOZxvw9mA4s4Xp_xSIhr65CDgmimusRHnz7sTfxH7_1ZvHt-1OzIG2BVrLHH1OiO1Zxi06tDWPXuuBoV5hp44Ne5slza-s4rkW7NUJkjcRd4YHRde-bg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d54a6dc02d.mp4?token=WeuxuNeMHExlXZ5NSCuMjONq0quGIyCYFpOoXpooFNNlTr5CVNihboOlma7ynArWPjXv3l-Q43KMXF31_2aOcB6tD40HweRhBJOpcHr9VfBDBYlqNzNQ_ySLZPOz2b8sQIv9hBxXBVMqD1qq9txmQJWc9lAFdjIA9NkIjwCTp4T5OCF6Ph5HJol1yWAKHw8S-jphvI0gI81ueVm718fMfx9LaF4C38G8DesOZxvw9mA4s4Xp_xSIhr65CDgmimusRHnz7sTfxH7_1ZvHt-1OzIG2BVrLHH1OiO1Zxi06tDWPXuuBoV5hp44Ne5slza-s4rkW7NUJkjcRd4YHRde-bg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت فوتبالیا اوایل هر فصل
🤧
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/102397" target="_blank">📅 09:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102396">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e396ec62ed.mp4?token=UKqg2sO5XpAo0qM6BTevDoSp7CY9xxRNYMNcyTRhQRRk40P4iII9Rh1lSA2a1EKlSxKBZt_N6mJIXTJXY07Vcih0Vy-7u4yN9eHNqWiNqdDNbpifTBjPfCMZMz11ULqkG7bPPJXbd88E4JimNQE3-BZ3zHsQ3GKQJbPBVuqidEU-VT3XjwUFbK9dYDDFaQFRoNXPWqhpEyvkcGkRIogE9Py0MqKonqr2TciKA5ZzKuS3DqirpAo1CtyDaIir6FLYZxXzM6IGelwjSl6M40y-EUcxmoVOXj1QYMwbzqmcDRimYpkVNAFt9vOeI-VLkq-VrPfO_NHXaa9FMNYycKV2dw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e396ec62ed.mp4?token=UKqg2sO5XpAo0qM6BTevDoSp7CY9xxRNYMNcyTRhQRRk40P4iII9Rh1lSA2a1EKlSxKBZt_N6mJIXTJXY07Vcih0Vy-7u4yN9eHNqWiNqdDNbpifTBjPfCMZMz11ULqkG7bPPJXbd88E4JimNQE3-BZ3zHsQ3GKQJbPBVuqidEU-VT3XjwUFbK9dYDDFaQFRoNXPWqhpEyvkcGkRIogE9Py0MqKonqr2TciKA5ZzKuS3DqirpAo1CtyDaIir6FLYZxXzM6IGelwjSl6M40y-EUcxmoVOXj1QYMwbzqmcDRimYpkVNAFt9vOeI-VLkq-VrPfO_NHXaa9FMNYycKV2dw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🙂
نظر پرز وقتی مورینیو میگه وینیسیوس رو بدیم به تیم‌های دیگه تو این پنجره نقل و انتقالاتی...
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/102396" target="_blank">📅 09:01 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102395">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r_u7idLXAIG0vsP4aiU8-O2EsBv0O-bv1-Qgb5ZYNuVJw4SjcCmn6bbBHxsMBgwkb8C7-7ZpDr516zr4tOVTqiqKhhXZrSXTl71IMRiJz9SypQ83qNgFQTBkAAjtk_PaR7pAY5jeX_zmRgJsiZGNLTxJI4vaxb8rjFMJqcHcyiZm3En_iGxb4K4xn_xyzHsAFldCsg2kddCuEQMTb1ARv1Y_apexfoQar1xPb9f12w0mqKE4QPoQuWEps_813KEiFZeBWN0KhdrjCH4GxJyDtwmjeU4XA5hE2V4kj6Ne6e-P_vyUzxAZEnwFM9QniE1_MPoxWJp9mGyxkaSSnsnVSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇪🇸
🗞
رومانو: حاضرم قسم‌بخورم که دیومانده بازیکن رئال‌مادرید شده و فقط تا وقتی لایپزیگ بازیکن جدیدی نگیره قراره رونمایی رسمی انجام نشه. اگر این اتفاق نیفتاده باشه از حرفه‌ خبرنگاری خودم کنار میرم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/Futball180TV/102395" target="_blank">📅 03:13 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102394">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/laP4yYUHSSwYc9Bzfh2bBl0ZnwHtyNcK2nAk2RFvWNPSEwvdx9Fe02csrGurmyTIJPryZzPSbO3Z95zDKDo_2saEFEvXiiD656nZXwNO45ZMvX_oz4W201vN1lhPes8DauLiiZK5n795o4klZ4HfmZn2d4Rs3RdpFh4ZE6smWbGMVocXa-1N4U8vJdgE30svhejWNyuzNlZl4rqPS0Re4dW0IsuXPMPMxDRpmLoM_zOunsQzDKFYu4Sr9wmryxuYs83284VjH3_0i05UUkR2QXDi1pG4OZv8I2TUtrS5tk2SznoQWhVrIPYb8OK3H8p49aW542L8PdYqN9lSuLcWHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
کاسمیرو:
خوشحالم که اینجا هستم و به لئو مسی کمک میکنم، او پادشاه فوتبال است.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/Futball180TV/102394" target="_blank">📅 03:11 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102390">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NYZbJUyHka4TPFVRci2eZ8fdLqtpqa21jx6uCz7JnYYITQxTVbj0KJ3rf5lsr4WhEQvrtumZ73B8n1Vxi0_rMZ8Kbxmf8VUywKN3iZD6L1k50VJi91XFMlk0Bh6gFMMxXUkmR4OhmsU-EH-UOSot4MKZMaP53TupTEC7NV6i7R_RVgph9XLX6wtK7GYbf02uNokvYMoj8digyF5bppNcZC3YSO5WX21OQZhS9dsdYm0Lfbe1APQjHWsWi0RslvmnxFp7nCZzgAmrDvUT-470CuIbsKo7q4HAFcR7fpj2S5qgcSIZ2XOG78O81gLZOKeEBLVfoibK9QMAxGEYhZ6DsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HkajkO8Hu5rADSKcoh8iUusBJFeE2QAS4lntFzBuqS_I3OtBpZOzr1SHshB5jnY6g7QVZ1IQvxMNRl7xOiQ7UkUWqCoI4nSSNHpXV2Xx6T-Q6DTxb_pXQtkpI1WAKsAdKj2YQirRYyndqBaB7ZVX8LdPESXTGA-pTxW1-FTVmJF7JcG6VLLmUTbguv8ALeWJVGI21ZYDLLjvZLL-ND3QJmMMRuEU2jJpjdEPwAIrVA6DurkamV8ZN-CCmBh99GYgm3a7PMdteN12I_1MhJL35CZAcMymUlBQ6mWn4zXJeHnxF7dFQZryzYr4jMP9GGWwN_8f_woxJYptgAKjKwkOdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WkOhnDBCfJOg5pesjJPxJG3zkMrrCQFlxjyODOtKUFPdBno7i4bfBFMxe7EutKDWGAJefSmZwVLrdysMD134c1tZf7yqe3m8iWhRqcnW8TaWZ5Rl1K3Zz7GJwiTI38KaxmqmQTWJWxNav1781f--oihROOaCg_1C_x5l5BAAPFYI3uGch_N0eC8ISLGOumMltP7CzsbR32FXjPgCq6qeG14gcaCWDta49AK2VpS8vYJliznJXuCgYS0BKdmPisXshMUTu5YMdEWNVIOVRTn9ZnrZ3MlCRiHMqgrC9q8_U1JQELnQRoFvxgK87Or6o2oImQBB0liVxJuMxONA29nSWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ckzvb4vQbE6PcpKVP6iAAMgylaNGXwYnb3F5GO0gcFCbJFcZ2ZMznIz82qwQslXSwhjkqCMySdMbNkd93vnSyOB2EEs1ANKz5G3NdQgi5KUpWo5_VepV7x94h7zWvUtbRViCRyk3pSEIpaFeH5xXgtguBj5uAXXasfa7pQ8ja9EfWKfsibB-fKWP-VvLqZSiSNbzRGwMUgymACHlxRJjVemUfMbBwJRJsPrF-qtFvqlJrI-5QmG5TCIIVq4c0YyglOwYRVptbljtKemboOU-WGhsIRxiELYjWfr1QcBQfLKB-PHmYQuh3ro3Z5MFDEBcYK-VL-Xj7n42JXD0kDm1uw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">کریس و جونیور و جورجینا رفتن عشق و حال.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/Futball180TV/102390" target="_blank">📅 00:47 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102389">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/511459b235.mp4?token=IHEXFEMrdcfu8b8HQ1pm7EBgOmcwxUKFLdOBYhDTmq9nC1O6xbO0a_PS3CT40yXv1dNy95w7bAOCvmQ3psuPbn1HUiKcsWAN9CQ6K14OLwxU5OtbTdj0K4oq1LG64BE1szkoAAIksnjwf7bbyTK1J_XKxp4riDrAwfYjvxmQwk3aXZKQohwvIDtCXgMKL4y_ffFxpO33zFZbcO0VjLwVbvSO_BUmVJFH3ANwmWIUqtg_84R9WenSYReHCZzVLzk58RdY4kVJqRaZhmgH3XzDoddYB7GQR5BQv3nMd7W2-DusHSvRdy9DELeUL7Bny104y4BgDSAi7FCFroDxgKSQNaUVAVZH-rgMOLOPmvC97Z9vHmpKxmdG6-C8bLCu0BXQNBGztTrJrSb2o10ykAUSuqb_VPap0kWo6HJyShZXxnMy2-duG0p2mfVJMY9d3Z_KxDws-JVeoDeygdlcyyHLKpsFQH1pkZTEw1gRwOvCbvaFw1PXuENevg0VK4t4jfDWgbLjx-oIlYt8lV-O3ZJKu59_9biZF5s3UB3utVWVStAUQMAJgv5YjezMmnbIHGyFchSr-XbTqUYIz4jdpQQwVTPqbEUAp11OCr-3oH4S5uRTV8w4LTacxYSrVAtopthW21PLQ2wVMyLzcXvGc87dk22clFLAAPW7d05nhtmCasI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/511459b235.mp4?token=IHEXFEMrdcfu8b8HQ1pm7EBgOmcwxUKFLdOBYhDTmq9nC1O6xbO0a_PS3CT40yXv1dNy95w7bAOCvmQ3psuPbn1HUiKcsWAN9CQ6K14OLwxU5OtbTdj0K4oq1LG64BE1szkoAAIksnjwf7bbyTK1J_XKxp4riDrAwfYjvxmQwk3aXZKQohwvIDtCXgMKL4y_ffFxpO33zFZbcO0VjLwVbvSO_BUmVJFH3ANwmWIUqtg_84R9WenSYReHCZzVLzk58RdY4kVJqRaZhmgH3XzDoddYB7GQR5BQv3nMd7W2-DusHSvRdy9DELeUL7Bny104y4BgDSAi7FCFroDxgKSQNaUVAVZH-rgMOLOPmvC97Z9vHmpKxmdG6-C8bLCu0BXQNBGztTrJrSb2o10ykAUSuqb_VPap0kWo6HJyShZXxnMy2-duG0p2mfVJMY9d3Z_KxDws-JVeoDeygdlcyyHLKpsFQH1pkZTEw1gRwOvCbvaFw1PXuENevg0VK4t4jfDWgbLjx-oIlYt8lV-O3ZJKu59_9biZF5s3UB3utVWVStAUQMAJgv5YjezMmnbIHGyFchSr-XbTqUYIz4jdpQQwVTPqbEUAp11OCr-3oH4S5uRTV8w4LTacxYSrVAtopthW21PLQ2wVMyLzcXvGc87dk22clFLAAPW7d05nhtmCasI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
عادل فردوسی‌پور بعد از کلیپ دست‌بوسی که ازش منتشر شد یه کلیپ گرفته و میگه ویدیوهایی از گذشته من رو گزینشی منتشر کردن. هجمه عجیبی علیه من اومده! من اگه قرار بود چاپلوسی کنم الان تو صداوسیما کار میکردم و نَود رو داشتم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/Futball180TV/102389" target="_blank">📅 00:35 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102388">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QPIWJbeArWd_QeQXvRtycCxbud3u0OYIV6zWfGY-qykzC6hJOM-mEkfDWjTT2P-yGf2nuglRe3M0XlFkYtuxeYhkBkw3n8EW4ue2kDv4lx2-KIjCET_-ji50cjV4N3kaNuHZYCCVrVsyInchpn7rNPrQ485Z0GnBOipgdPdkLxCYuaQN1ZgOzUs0TItkKtUcGvy-EOmJY04FZkcVLvxMDP4p9mpSahFZwU1500LvWsNuOdf5MfBwcMPn_gflzw2Gg978aoPblirIt7kWf0hUw8aSSe0CwdiZ6Ogv-eONpJY5x3SpwnKRt7WrUjUyeyN24k2E_xq7sO5E4uUEDsTYiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
فوری: کارلوس اسپی شده با بند فسخ به مبلغ 25 میلیون یورو به رئال مادرید پیوست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/Futball180TV/102388" target="_blank">📅 00:29 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102387">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YHQuXuCEjoYq9vySOUMJhly1LoMZYPxubqRJTI66qksIyE0PJAW0CLtUhV0nUVivjtECggpFLEjPjOtMmfM6aTRJyRVefKRT3400DAqaq9ehEprryHdDzBgQ5PspqWE4Ii2WNknC_7_-TAn27ZnpjJzwBdpz6P2WMwH7oAZyiiQGs-vm9FMEkmHGqsqKHMq6J53qwAfWndNqDoDbsPdyawxbO_FKAq7BEnskwM6K3rpt6tSk-uA2GCEQLgdWCC7HO8JvLEeN1s1i2GHVdoNVpl72wmpmsShX1an0KqSsbYd2n1mRHOXXSi3mRzBlUnesMXqmhLkF6rBg7uDSYYXF6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری بلینگهام که رو دستای زیدش خوابش برده.
👀
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/Futball180TV/102387" target="_blank">📅 23:37 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102386">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae65f1051a.mp4?token=qLcgKDnzJVU1yroR08Zhw-LqkAW6v2n5Z0pKdF0ewbVwi2lHguZeYpRHRqYmFA_hrtvWjFq8ze2ndO_k512gfu49_yzyOb5nto7CFgMwJjpS2MkNJ9UrNbI_9cZek5fHgjp9FEq4t9mS5NfKDUGjwgr7qhtI0EPOGYB4tHMmPeopWtSOjQer4DBUlGyjlgn7Oib0Ksf_AQN2yLiB3ODbZpurjEyUOMiknP5jA4Swgxd1JWsybJg-rko4v0vXTPIXT6tEwk25Xt5_Y1KaaHEFj3_Pf-gxCZg02IaCthlQF9hEabpwdBD85TXIVY0YybuNQyoZ2VsGAb2CHiiY2RUlVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae65f1051a.mp4?token=qLcgKDnzJVU1yroR08Zhw-LqkAW6v2n5Z0pKdF0ewbVwi2lHguZeYpRHRqYmFA_hrtvWjFq8ze2ndO_k512gfu49_yzyOb5nto7CFgMwJjpS2MkNJ9UrNbI_9cZek5fHgjp9FEq4t9mS5NfKDUGjwgr7qhtI0EPOGYB4tHMmPeopWtSOjQer4DBUlGyjlgn7Oib0Ksf_AQN2yLiB3ODbZpurjEyUOMiknP5jA4Swgxd1JWsybJg-rko4v0vXTPIXT6tEwk25Xt5_Y1KaaHEFj3_Pf-gxCZg02IaCthlQF9hEabpwdBD85TXIVY0YybuNQyoZ2VsGAb2CHiiY2RUlVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🎙
روایتی جالب از تمرین‌های پاری‌سن‌ژرمن؛ جایی که حتی امباپه هم از دقت باورنکردنی مسی شگفت‌زده شده بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/Futball180TV/102386" target="_blank">📅 23:00 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102385">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KsGDILt_CXRkVl3tZz8bObFL7Isyiz968FG7hsNRIN5gUefisJP8VFWtFpbex48S7evbwsCHW8G0ccng46ZXS2b-CGt3TX8LTlw4pAV_sCGfy4LUj5mJUPRvOtTCMwk4iVb5MC4ELxV62ytdnfTuT_aINcr-JeB0d3tpJ50yz4ga2VwndFh5NOJSTMzhRapVKcjs78aG5HgBcNV5Rb_nAW8yCOlzYZxBxewJn-i9344lP8wQJOoaTiWu2qud108qoAVWiSXB3d2BBlM0iHMAL-_G58uZ8umu_uXTK8kYy3J5GpN9sCEVGXOk_iuVpIQRfCDqY_0jw51d2OwqFu_rkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اولی هوینس:
ما حتی به امپراطور چین هم اولیسه رو نمی‌فروشیم چه برسه به رئال مادرید!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/102385" target="_blank">📅 22:43 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102384">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uwIofm2aazUAIMN8wXn7vPfL6zKRlbWCssiQQnaEZTjXvy3eDfwoJ6BXjVvVrBeNDqov4ykXfrL3z900bKnCFRWacSzLAplzuMvS55A73c4UK4L1VSZQQUNCmfbAs_rpG2g_I7Ht6I_8RQQ4zPR8rEOVr7huB4hk6auUtPvLkj8DbNyrDtgDiB-KGoTrGxtX_sjn8wi7TcJx46qVY_9MpRPD0gzlasmChkPXoYlJUL5pgfSmTZhywmUT3WjaJGlRgON4m4gPAU5U7WwoYILrs093SDMg862L91MFAy4TWhqB49ou9KMw-a9O26b104TOpg_qMi2AEs-iKVfjgcb9cQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
رئال تو این تابستون شاهکار کرده و همه اینارو فروخته!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/102384" target="_blank">📅 22:40 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102382">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HGbdHcZXAGdh8RlRmIa31-hnGkc5DXOdf6BzTesGiLGOT-ZZFP7I9Q1fO7Zh2g0T_CSlQMCwCoVOeAQ7hYTkU-0xFZkLLP3v69RBITWOOpEFjUI5kd6jqmJpDZ-RsNANonVDVZLZOXmUwv3BOXIqY58m0yS8k94WBi25TJLIy6w_Mpwh0DPM5rDrbd7xne8UPJGEcxRANP4dA4r3Q-sX6hYbTK-OZlglOgLKOIL4I3Y0ocReuolbgA3cwdAeqbWmwYcUzMy_tztaT4taMtWOL5tAvKgD_PJGzmcQc8yFcSuTA7OKUZ3E0qkHCfD9x1SeT__nnxRhn8QsiPtcwYu3mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/c4ciyhT78KoFJJLjNVR3L5rdtjRTsi-Aukvbu7Bg2xbngiRr9Dp9BDRqcHuaoDlIny3sui97YXTESv0l57qK1-ozSpqXndGsXQeI6UnrG73zVeXtRt_t8I7uVL8Dh_WBJcQE-ryHuwOZdDDkhDQ1OmComxRWb-A16W3B2qeESDNkwUg8OrH-1jMZuQHSVxehJS54H_jY_Xt25Nd9nMNas8jGNNnzoH2gpc1czA-jRx1NqYVHpvz_sAnIVs19XY3k7Z7KPsr20GkFCdXrmByOE1gvZxSjkYWcetnzAaJn4vU5WehsDjGh8nmvCXtHGD4FElXfVJhwBEp2jWedh0-oqg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رونالدو در 2003
🆚
رونالدو در 2026
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/102382" target="_blank">📅 22:39 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102381">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromچِشم به راهیم</strong></div>
<div class="tg-text">▶️
زودتر حرکت کن؛ راحت‌تر زیارت کن
🔹
همه راه‌ها به عشق حسین(ع) ختم می‌شود؛ اما زمان سفر می‌تواند تجربه زیارت را متفاوت کند.
🔹
اگر سفر خود را به روزهای اوج تردد موکول نکنید، هم مسیرتان آرام‌تر خواهد بود، هم زمان انتظار کمتر و هم خدمات بهتر.
🎥
این ویدئو را ببینید و بدانید چرا
«سفر با برنامه»
، بهترین همراه زائران اربعین است.
#چشم_به_راهیم
#اربعین_حسینی
#سازمان_راهداری_و_حمل_و_نقل_جاده_ای
🌐
rmto.ir
🌐
141.ir
@Cheshm_Be_Rahim</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/102381" target="_blank">📅 22:39 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102380">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KKAWdTV2BCY9lOdKJ5ojosD4MoS85AVHYJf5JfQh2zEMOjfcFmSVdAXO-0ED3XSvE1VTQKxjjf4PfPw-DrHqGE-t96Y-hNhC8ItCSc1Mesh6TYOuSfPGHrH39sXc1Chbuot-SseSN7VvwoPtGfxGSWu3_kO4yeJd-qidMXqaqOpFvFD_upRPTd49aKcZ3URzipBvBabW4-uR-Zdua1OKf8Zhj3thsSAIPZv7F_3SH1J6JHaF7RhhuFZiJ-O0YYDc69D78OSVGGsmRatNtbnjDlwlek4MlDVQSqcDRk4zLOoxq9MG8SiQ9xMr1uO-VOkMtFW_cLCr11W7zpW1MtNr2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
فوری: کارلوس اسپی شده با بند فسخ به مبلغ 25 میلیون یورو به رئال مادرید پیوست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/102380" target="_blank">📅 22:18 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102379">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D5mLBU-60zT2B7tfl77bDw86y__jjxEu-aqA5jmrXmA78TPT2EJakLN-uXP5IgVd9Jvk0POTkfa5l0fu2Ez6spAhDVSJx_FKZKeskDOxCG4COjSqSR-JrUrHjbQfm7qNOZMmpsyTUZl716vTnM0b0zkeLCxgALxkxTK0Yk3zTlvFbTjGAO2NnM5SiGUW1f_k-FqhuGT2-IaPPsKfgmEBenErtLqYl-26ZqDAb6LcDn84zvjZtuH3niFeeIEU48ErC6Swe-w2nrOeLgmYmJ-mDyTN4hbTe_4cJTVbwvNtVy0SuQDiemRVghHkP_qgEtNSaUQrViMs_r5MF2SKpYbT_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تغییرات وینی تو  فیفا اعمال شد.
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/102379" target="_blank">📅 22:06 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102378">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ki2O8c4PtPFgGf_Dg10NZhDlw016Pk4AnnpUq-iXc3X591RiVRwj6l86IyFvbfIneUHGMZaEXgfAE59N7Rpv4CmVHNeTWFOLNHqTdb92wYINIaaZvVq1QF0UH3URWtu_c3NYyxbUMBHggK19EvJbXZ8qcEmMTGY5q8Fm-IzN1sYrLOXemdJIjBga3uoAflMMKbBJ2ykyJJP1s0j9y5HzsYbBrUTPnY6--TUzyY8X9rmjO59Dk06jx5MSTfovBrTsmp_g1i9399Nau1FhtC2VmzeLAcxeAL3r9T226-xrRXYmwXHdpYTYPX2i4bStUlId7x_5Njsd0hyg3PbSTd3JIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
بایرن طبق معمول به این تیمه تجاوز کرد.
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/102378" target="_blank">📅 21:25 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102377">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bFxrEMxKtEOGgPa8mBhJhuTWLx-jelgP0KnpypL3Mp4nJBPJpkaXooNfYsaX8MwKTOZpNMpneQK-ZIJwBXO5FpsTVDekcwlBCKb97efb8fekPfstdUaaM8MAsr9j-Ui2BbSMTZg8WWro6QUvs3X3xKILgbbroqwbTD5G4_vCcX4ExbNkeXJ9-vvZFPD4awkm5X0nNLHbSgQ2JaqQhueHoj_-qhaWPKuWfQinRzLUMOAE4cnor0Bv9zU91yLgngf32zkB8j2-cVyJa1UcXAolERrvPsk1RLkcB6dJC86gNzvyctSdAK7wi5QCs2hmPKNIAJtOb7pW68daVEGpdoQgIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
بیانیه فدراسیون انگلیس:
ما در کنار همکاران اروپایی خود ایستاده‌ایم و بطور کامل از موضع مشترک آن‌ها حمایت میکنیم، ما با برنامه‌های فیفا مخالفیم، جام جهانی متعلق به فوتبال است و همیشه همین‌طور خواهد ماند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/Futball180TV/102377" target="_blank">📅 21:10 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102375">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WCId-erHf6C3Q_xVQhEt1xOljOwkrGlGKyc1vtUav1XYWFLG92amfqoFglqwUlTkAYLOdJ8hcQthpbHpYncXVtab6OWbLcuA2bVKh7hoAhlHq4V0ZCN1lYPUWUZbRo4FVmV4F5trqGx-qltRctdO0g5U8BuYN8T9CMotc63hvcERhZuAx0sBgftQ2SXrP87NpTuD0oPAhlb8bUkXoOOTJ_kiJVF9hgsfk6JLtUVxfWZaRt2zvYIdS0ocSmZBz7E9HneBfrvnt1qdizxkaOy1f81YtYoJP-q0MP7mReQ2ltFRLLRtqD07TCpGUO-ZAlu6ihB1i0AZXDBmZcRWz_55xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🗞
اسکای‌اسپورت: منچسترسیتی برای فروش رودری حداقل ۷۵ میلیون یورو میخواد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/102375" target="_blank">📅 20:47 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102373">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tcIRDQrPEm3CX_a2prFey_WuYdE5kIYmincqY31xerpXIJb8YPizk6hJpW5RAlTuD2rKwPEk9CTDFpGd-zyBk-1vP-8EUfh2kbB45q_QJ45A330Cy6PeJtRp44KAWxbZMtKxWHR4hUPR1zrh3RwsgVZuTtf5u7xmk2QFf3DgTmn6m0Gf-smLGTS0VDT9RjR_3ZJvw81xIk4enx0SlDa5eT4VSFbElGacizTOYQfsJVv1-_drULFWFBR4OSv4vsy5HmvNbx1WT3tYzz9iF2OjQmmOnI7cx8_h5kw_CZiNxKYIV9HQw68zZSA-GGTpwP7IdwdcecCXqxjs44EhCfxXhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56d9c0f441.mp4?token=sVSpvP7Feq0n_ymhQZ1q8CVp-HHHR-tZvvg_CFntdIQt8q4apRNV3QSBkoStTJtYuxYmoAlt_edD52x60Ru4oBER-Zdd9gva5UBJuTUZJRQxjZidOp5j56bYagNOk6mkQRjGnhM5IJZmH9c5a6FijzR04uxPDtZVrhA5A-Lbd8OgNNl8sr9wutMRzCPZ3NPQv2fLAjWQAkMMS_ippEiwmRi11OMCaAfPpD0wDi4KUpfejq-ti_grli2t6S6CITtk4fKnVeLbzKJLTi6Aj3GeLIGafdsiwWwXpj36j7jIsnvntNn51zpD1kUDnhWRaqSIiSQ81aEKYJmX1m3imywM-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56d9c0f441.mp4?token=sVSpvP7Feq0n_ymhQZ1q8CVp-HHHR-tZvvg_CFntdIQt8q4apRNV3QSBkoStTJtYuxYmoAlt_edD52x60Ru4oBER-Zdd9gva5UBJuTUZJRQxjZidOp5j56bYagNOk6mkQRjGnhM5IJZmH9c5a6FijzR04uxPDtZVrhA5A-Lbd8OgNNl8sr9wutMRzCPZ3NPQv2fLAjWQAkMMS_ippEiwmRi11OMCaAfPpD0wDi4KUpfejq-ti_grli2t6S6CITtk4fKnVeLbzKJLTi6Aj3GeLIGafdsiwWwXpj36j7jIsnvntNn51zpD1kUDnhWRaqSIiSQ81aEKYJmX1m3imywM-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
استر اکسپوزیتو درباره آشنایی‌اش با کیلیان امباپه:
ما در مادرید با هم آشنا شدیم. حکیمی به من گفت که کیلیان خجالتیه و خودش نتونسته شماره‌ام رو بخواد، برای همین حکیمی شماره‌ام رو از طرف اون گرفت. چند روز بعد همدیگه رو دیدیم و بقیه‌اش تبدیل به تاریخ شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/102373" target="_blank">📅 20:21 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102369">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TMMn46FRSQQr2EYtjOCq3_l8jS-UtbpyrfWhJo-KNLSWVqA01Am0cfvVXJ_iJbh2vPECKwFQYkRhqr9Ntx3pj60j1-vRn8dBRpkFHAYCzYT2r_n8m1lBUBueyfrEg3HrsJWNkaXfJSspS0sg_MPxCdmXVq6_UVZ2lDhAhDrnvFaRbmnxag5G-HkONPI8x-8m0xD2YEtFh2bsJzTEF8mYQQpronUJPvy-rkaeRKZiWO68DEJkvFMOoTBdkaPCPTfRdQy87Qy5q8_IS27w0unt_HN_i2cn3G9ADtr_1PFPXwVUMHNwUPXafoqRIVvCaHLuSJyYFEOyVnLRl-UNbPH4lQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/v137hehh_FdpLrX-2YPekcS9I3SEg8BkccsC9jzSrDoONmPVs-ZK9Usce8R3buaB-VwjgbMz9Bf8ehhYOnNOdNFX-oqQKXviE5wj1zR99e7BkI5s7DYvFehBTthobeFEfjBsnk-rOvZH3i3Ss1__p83_FQimVdjrbnH5heakbXEgeR9XLOayO0kuu1H8owmP6V3B84wWq8j4rJmlEwU4H7qaJlSl3GxcbOIR-eA2fGt3572hV8h9apI8ypA5fJVMs6Yh_rTBMafg8YBRmNpII2jfcbKejnENWhYL9uYo93WUB0Nsikfyv2oWfIlJstoYefi91N8Vgv9x-7QJNFTF3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rtdDH6eIgz77KeYWL4TvykpjY2BkInZ1bgFWYeaKy4DZcKw4LAqfJ_JAJRDFtQMIp-M2Zkmo0nKbiZN6fZ6TUqFhUQAPBIp1ehz4p17ew7c0NudaQF4rdg1EXZS8tgiQvjwOVijyWdiamM6VG3VzcJLdtc4xusiSa-blhFL2Kc_xz1NY_sMsNrRRDpSn4zEsHQ7BQLz2aWkwN99Vc-oh_WYmtAYY5t9t1TblWvzln1sVi1Ax5d12D_OJyOQNEa8XKiKb01jEC-ZjkZJxrcCeYnIf_tUTVc6zRUS_KhDM4L1WYYE_tmVvZKizM655EnE5OOOGdRbaQDRfQZfsfVZ5sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gZE83XlRyQnNExR8wagpHZE6RBWBMP2lkecEVzOAKYehTVcnwXD2Qvvw-FCNut2znijEfIjussyU8DZMXxc59SNR78iyvqgI47bwl3yLiOEjwPbqkl4HLRiOWG_7wB9Lelhq3jcY2pArbIGQbpr49oXyzPHcn1OHv5PmUMjDxMZZi3Qv4z12M5xPuN9QHVDjiaKJvsXSBwGe5dxzrIsLH8qs_8z4wjQ5MyglnSlO7nq7MFAEEP6qrCNIV_PcrOW8FfDi4jgRhVJHbTZdpAJfMpKCjRfkLyRj-bkFbOB7R7cO_NLLUnl5ukxbGQOKlI5pVARBT-sJmGoem3bdSF8Fjw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🔵
چلسی در همین پنجره نقل‌وانتقالاتی حدود ۳۴۲ میلیون یورو هزینه کرده!
💰
💸
خریدهای آبی‌ها:
🔺
مورگان راجرز
🏴󠁧󠁢󠁥󠁮󠁧󠁿
— ۱۳۸ میلیون یورو
🔺
مکسنس لاکروآ
🇫🇷
— ۶۰ میلیون یورو
🔺
مارکو پالسترا
🇮🇹
— ۵۷ میلیون یورو
🔺
ژئووانی کوئندا
🇵🇹
— ۵۰ میلیون یورو
🔺
امانوئل امه‌گا
🇳🇱
— ۲۵ میلیون یورو
🔺
آلوز دنر
🇧🇷
— ۱۰ میلیون یورو
🔺
دستان ساتپایف
🇰🇿
— ۲.۴ میلیون یورو
⏳
بزودی رسمی میشن:
🔺
والنتین بارکو
🇦🇷
🔺
جردن هندرسون
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🔺
دنی ولبک
🏴󠁧󠁢󠁥󠁮󠁧󠁿
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/102369" target="_blank">📅 20:01 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102368">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b486c4e528.mp4?token=nfUuEB_sDzpDHF1fSNE1gzmflgEJj-dpkMQhqDBZBwZyvGuXnncswCia9U7SjITTrDL9_uT_wl6ZJO03Zwku9nzbHy-5lnK7bSRYgZO1cjh-NdLgxKkauDej5XuV8FpA8A3Dr8mBkY7B2pzlaLGIu7AqIrka-ni8of_X7HeJdsbF_SZqoAWtkPYjPSXCy-H0Xr9aPhZ6iECzTVB67ukauXGq6ikhk1DVs5mPbFBLJJj9VbOgq7oHPP-rRBhoGhiVipTVTvMYIwZo_FzJgw1CeLcZrxYFh9SkTD6Iw6kcija2hSQfXQlZmuE7Fh-86mzUcd6feXCpsKMLSgtDZinojQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b486c4e528.mp4?token=nfUuEB_sDzpDHF1fSNE1gzmflgEJj-dpkMQhqDBZBwZyvGuXnncswCia9U7SjITTrDL9_uT_wl6ZJO03Zwku9nzbHy-5lnK7bSRYgZO1cjh-NdLgxKkauDej5XuV8FpA8A3Dr8mBkY7B2pzlaLGIu7AqIrka-ni8of_X7HeJdsbF_SZqoAWtkPYjPSXCy-H0Xr9aPhZ6iECzTVB67ukauXGq6ikhk1DVs5mPbFBLJJj9VbOgq7oHPP-rRBhoGhiVipTVTvMYIwZo_FzJgw1CeLcZrxYFh9SkTD6Iw6kcija2hSQfXQlZmuE7Fh-86mzUcd6feXCpsKMLSgtDZinojQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🎙
🔴
🔵
تاجرنیا: «ما و تراکتور، بصره را به خاطر نزدیک بودن به مرز، به عنوان ورزشگاه میزبان انتخاب کرده‌ایم.»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/102368" target="_blank">📅 19:56 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102366">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nOq-RMJPMISX7p3Iez7-89JaPutdfDSu_o8kP0qRfNL4Ug8YNuCtg-Y7yQiCv4igzbvsxdQffzeLDEtEeCggGK4tX0XgmPJuUb6VMipkwZDX8XFV-wziNoDQ6qG8Za9xnBrwmbsFqfKDWY5skEjJB3k9MGmept3VJTy5cmnEyemle5jqRnWAU0vay7Ts6cLktDAklBM5JHE0JEJ7YCrQFU2zCMH42-l6kEg4OfMzSQfQd8BheCjEo3S9b4jFgiFD9yGM39ZTBS_7sem1kx8yqhMctGwljfsTOkbCEpnMwIYO-Ofo0YtcdCyxX0d1hNPPz1DtRUWZIJX_ZYgPrx-H0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🤩
✅
تیم‌فوتبال پرسپولیس در دومین بازی تدارکاتی در اردوی ترکیه مقابل آلانیا اسپور این کشور با تک‌گل علی‌علیپور به برتری دست‌یافت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/102366" target="_blank">📅 19:29 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102364">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j4TWVSw0_YmhGyg4HwSuwjVK9i7G_ppDScgXGqrJJrhd7U2AsVxTi0TqhIZsQ5YhDnjjXWlbggKRUZ7haQJZQxFB31Io-4uk-1bc--aZVc1GXtkRHPawNp2qw1e5H2zaKBMAd70ncxKQLcXULsh2Vp2yUqqo5hzZsJyUhoBIecbCs3LBnWebQ8PapAJ996dUmaRhIPq3iIa3Atn7AukAr7SsK7lcWtoP-lIJ-kjTtw71eaP4Won2o5yk7D3Tn46ZXJF2cAu1s7xbnKy5ucfvyU4M7P2BVuOh40Y4S7YLtY1n-o8pr53JESTBYYSImUwMZGNcAyjDhxMkoc-T45U2tQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08c0c36c9e.mp4?token=NUDbY4zGIPVhBKk3CPF2J5VXv-_2f5-45dDymWI8u1R8DlPWRLP1ciZvGHU5FVCVPLFryPom7tTICZ-3lXpVPfKxtBUIY3tIwJ4dFt1E-LU4f_lMZ4uUUHB1WHzdOLwbL5OYUc4j3zIZ13oTMkw4vylvfGrOJJJRreilqdQqeiAl8U8zmOJ0wPsXDfyYHI2LzyBDLHOxMPOARbioln6gLWNJ__Rkwm6aZNaH52gvGhMI34nNU9uUAcsQHWxqflTq5rdAZe4NaV7GaZ6mA0uKnHKzdxseWOhqBu3o1QGiFORZ78i3qMtqyhDhm_SGhtviIXCZ6IyNCXQEEbLxCXucOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08c0c36c9e.mp4?token=NUDbY4zGIPVhBKk3CPF2J5VXv-_2f5-45dDymWI8u1R8DlPWRLP1ciZvGHU5FVCVPLFryPom7tTICZ-3lXpVPfKxtBUIY3tIwJ4dFt1E-LU4f_lMZ4uUUHB1WHzdOLwbL5OYUc4j3zIZ13oTMkw4vylvfGrOJJJRreilqdQqeiAl8U8zmOJ0wPsXDfyYHI2LzyBDLHOxMPOARbioln6gLWNJ__Rkwm6aZNaH52gvGhMI34nNU9uUAcsQHWxqflTq5rdAZe4NaV7GaZ6mA0uKnHKzdxseWOhqBu3o1QGiFORZ78i3qMtqyhDhm_SGhtviIXCZ6IyNCXQEEbLxCXucOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
اولیسه درحال لذت بردن از تعطیلات
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/102364" target="_blank">📅 19:20 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102362">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KCQ03BHequuufHEdNFz-Y_0WtHVsLH33iF9P3eR8ZMnNkj6o5413z-clLVkTlhAfG0ppF-HylCGmFfVeIqVD0PjICCIbQUFCn-xxsVvoSiwVgBQUyITCkwwDdZHrEVaWCWuMvBbEN_YpyHMh4bBwJU9SfT68l1K485X-ZQwTTWQDwvvga4yockxCR_3EhqFU2b6An9gTxpsEIYP1kufvoLjt4NEFeqlXjf-jLYAiu5DvX87-W3VwaooRBPsiOB8JqOxqKCsAhXSQH9mCDFnwQIqLvXLftquMCY75j8HAJVgIflhWqSGlupJ0USJbxB4wFaUetRlDBWlWNQvmu2MQSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3645ae0183.mp4?token=nPwBzkrpJOuzqEVintHnjIZucskFeqzJB0bwj6u_xrN4glMUxL7p_gxRlFY4cWhRK0n7HGicsafIK8qIs9W9UgvOZ2x9ZWz6jd6FmojOS3hGrRSY2o_Mpp1fPN2Zo0UeVdQd2SYYTQXqEP8bdBNg-d4whQ7WMx2GBRZQj8s1VnLwhi09fdcqPJIMcM_ShDCNHiWq1xB2jWXoUtKRHnDuzbrCTTQ8Ddflj3MEE7Az_E1yCSwpP_lMksKEtzpUC5i0mGipS8xRhqFPwO1ogPXEnoqZyOuSQ-bpv1jvB6Yxx-ITo0xpuZsO3QTIhGeqrc3ofqF058y1cIYFfA8VZ5rK3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3645ae0183.mp4?token=nPwBzkrpJOuzqEVintHnjIZucskFeqzJB0bwj6u_xrN4glMUxL7p_gxRlFY4cWhRK0n7HGicsafIK8qIs9W9UgvOZ2x9ZWz6jd6FmojOS3hGrRSY2o_Mpp1fPN2Zo0UeVdQd2SYYTQXqEP8bdBNg-d4whQ7WMx2GBRZQj8s1VnLwhi09fdcqPJIMcM_ShDCNHiWq1xB2jWXoUtKRHnDuzbrCTTQ8Ddflj3MEE7Az_E1yCSwpP_lMksKEtzpUC5i0mGipS8xRhqFPwO1ogPXEnoqZyOuSQ-bpv1jvB6Yxx-ITo0xpuZsO3QTIhGeqrc3ofqF058y1cIYFfA8VZ5rK3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
نیکی نیکول، رپر آرژانتینی و دوست‌دختر سابق لامین یامال، در مصاحبه‌ای مدعی شد که رابطه‌اش با ستاره بارسلونا فقط برای بیشتر دیده شدن بوده:
راستش باید اینو اعتراف کنم. مهم نیست وایرال بشه یا با واکنش منفی روبه‌رو بشم؛ من سال گذشته فقط با لامین وارد رابطه شدم چون می‌خواستم اسمم بیشتر دیده بشه و به کار موسیقی‌ام کمک کنه. با این حال برای اون خوشحالم و امیدوارم اینس مثل من ازش استفاده نکنه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/Futball180TV/102362" target="_blank">📅 19:01 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102360">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tIfpaWoTgQp2q8G26WbyUlMSet2IOTx53p-NkJQOoXaYueCY2ig5d_gpD-Sn1I5FP9SPxsx_oiRVMrDG0fbwNstbUwtuVvpps8JeL6kRDd3HokA4F_aIRC_kauqeF2uixEfQqfYIqoFEHrPTDee4tXilkLU_LK6p3m8oakjmK2pnqaQK-s-9OejwqmvxOtqUIoWYO_l9fUESYEajEoX7fxo2Ivu6FBNfGQzIni1Oijymajx5eoSZO4kQothFuUFknUhbOSYvhisl_oh33A7I49zmBMzXdzNNR-8PZ8fUHi6T2hyctq2WVZ14tJGj0OBJ0mznCvDIzoeP-EsVdWWbEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aHm1XvEVuqLafAKNfQRCnNMwSDZ-SHVpE2lrevq-fe4UZMjO3i6ivVKm5PEh0GSt4dTfdr2D5VdxHzK_mlGu3dtUiQpeq4nNOlhDCTESMM4NzwFbFhO8n5P2pRR64Fe_ejP1_La0E830xSH5YNsjbfDh8fkP42KoFc5ahvPNOoapxNeDqubwkRFhOB0ffq04g0oXs4t9sr47UkzEWax8TztU7StFEo9MyZJSzM8cGqjai1o7-P8K1ohhDQN1QwLYmf5VjKMzvsrt89UO_gjjqekFnPHlfw6j-H1AbDAZEKoPBBe707XsWfMys6qn5sncd6ZsTrGDLtHlcAnR94DmHg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🇦🇷
طبق گزارش‌ها، لیساندرو مارتینز و الکسیس مک‌آلیستر بعد از پیروزی آرژانتین مقابل انگلیس در جام جهانی، برای خانه‌هایشان در انگلیس نیروی امنیتی خصوصی گرفتن. گفته میشه بعد از حواشی جشن پیروزی و نمایش یک بنر جنجالی درباره جزایر فالکلند، به خاطر بالا بودن احساسات و احتمال واکنش هواداران انگلیسی، برای چند روز مراقبت امنیتی در نظر گرفتند. البته گزارشی از حمله یا خرابکاری علیه خانه‌های آنها منتشر نشده و این فقط یک اقدام احتیاطی بوده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/102360" target="_blank">📅 18:40 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102358">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ilPtOe6CS6piOPAwRAAs3SWivZjd5v_uy1OLE5DnJkvUUbSiha_MaoEFwChkQjkiQSX4c1utDbQi-zYERzsJbBMirksdoJyAQd0JgkVOiQPNm-zltu5hQPns-YmZbPRX6oATL9ZLvc-PssDkXuMVnnQF8veHgng9exGGZgqe42d-gcgAOATLO-pDbJ9SEiZwwA-kt1ft9_A_UelZdj7EelR_Y6T9yL-DEbi9CMTmkrR6rH4QyDa9qukOHPgeutUo2bmIoqBHIj68ew-C90wjQwccDChtVLWsP7yU3_b1yFavBXVw8P4f4m8HqGv0JoN2FSpqHGURRLBZyUX-ibVv9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ap1R7g5FewqcNj5YRJC4NHY-w_r61iaZ0J6KbxRjUlX1sfkdNmKIzanIOp7JWO2JXdBJI_auho4QaYCsNNzTtVGXH3kOacl6bQX67WL43HshuBaxlnKbNTPBIgmOs5H-9kNLiO7WgFMAmYR6_g95WI7YABw855Pfyww-WS9F86rM0KVeU1XmTCYpr2ScdBwOyJ8EMLldi_izUJRBDd2WNC5tgP2VYBdWzvmFOw37izFsOlr1ZKCV9CwTS1u2CYOR4wR4SWhYwtrDkBs4KPFYmMjbnsE_LtSbVoo7GZ76YRmaNIdSjI_eY0UH0Ym6e0wQIvTLMjJ58AUhlU_X0Z71mw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
نیکو ویلیامز و دوست‌دخترش آینهی گارسیا جدایی‌شون رو اعلام کردن. طبق ادعاهای منتشرشده، گفته میشه آینهی نیکو رو در ایبیزا و روی یک قایق در حالی دیده که مست بوده و کنار سه دختر دیگه حضور داشته. بعد از این اتفاق هم وسایلش رو جمع کرده و جزیره رو ترک کرده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/102358" target="_blank">📅 18:20 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102357">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14e33cfddb.mp4?token=ZDKL461uYvSgR7uv2uX6yixgmn0juRa-EkO5dJMVzhIEECI_rdyWbm7lIFTHMmTNsLW74APA_5A97Z7RnicT3E0ialvvCES7EmzGdppyyzWxSvhSBYdVMhk4_0QpYeUIbfo9BVYFDRDk8x63Zl36XeYSv-4k1-nbftjT-D0qQKZH9nJXMhRvMnNaEVbKiBn54D5_kqdgVgzzdgnUUtc-24dySz7prvR0CbyZOgr4NPGvanFe5eSRQ0-FFahZRy5MqGnuPrkoXAnRiDoJ1rj-QL_IF0TxSAHQOBd1xLWi9ikOT-HVQLmlguRGjuZdhA-4995m9J-QD0pcV49MYESdqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14e33cfddb.mp4?token=ZDKL461uYvSgR7uv2uX6yixgmn0juRa-EkO5dJMVzhIEECI_rdyWbm7lIFTHMmTNsLW74APA_5A97Z7RnicT3E0ialvvCES7EmzGdppyyzWxSvhSBYdVMhk4_0QpYeUIbfo9BVYFDRDk8x63Zl36XeYSv-4k1-nbftjT-D0qQKZH9nJXMhRvMnNaEVbKiBn54D5_kqdgVgzzdgnUUtc-24dySz7prvR0CbyZOgr4NPGvanFe5eSRQ0-FFahZRy5MqGnuPrkoXAnRiDoJ1rj-QL_IF0TxSAHQOBd1xLWi9ikOT-HVQLmlguRGjuZdhA-4995m9J-QD0pcV49MYESdqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شوخی ترامپ‌نادان با بازیکن غول‌پیگر فوتبال آمریکایی؛ بعدش که مزه میریزه از اتاقش بیرونشون میکنه
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/102357" target="_blank">📅 18:04 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102356">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff5a8032cf.mp4?token=X1KpAptFE2hk1eZCDTNlhD5Jsg3qWOLx0aCWfuOyzX7IR3Y4wHxbEmQIbuuyEhn8bMP-0ZtVwLq26jcJo34vgxaUm3HAveBlIMCZY_UVVhCmpcznR9u0I2EcYItPjxUIAna9Hxy2oLib4wA9t1MXnHIBQh4aM19QijzurVELadg4KQNUZ1s6f7oDM5eN8YN0pQI8ibe9IkGTTtIU8ps2ttvuXKana-bLWDL7jdRk2vN0oRkWAsIHUAeVrHHCZoF2RTeh4umiL1130hzn3WV58x4aU0TG2vrQ8Ovcol20T_rRU8MxouMr8lhznvAnxhsPAS3-w5ahEiCRAFhMKz5jmqkuE9Tk5ueZ3evY82OdYavpb_jIQ5e4mYTJ-3jvM9s3d255c8WCCQWcLZBRPTpjL-BHDqZQVgYR8Ol0uTkG87T7L1iBBbZJRQAjLHTTn_YCgNFRYJJFNdvBjxEzowh1L2OY6dQw7HcqvQMKyugX9hby9cl6jUl5JWLXH1QMQCTZvICBHzyu1QIeTN2M9yErBIkjBm6bVikpOA_OVp-yj7IsmC0lV7vzpfnG4urPh54Nk6e1QLaIbec5httA3SLy7unA4U03h5aYHa9mm4vqqVlWnxZeiuO0kTtNGwbhfU5q56mtZ9KyvMTjNnP2JnTGpuf_fU9f1gNWNIpBTDZ43B0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff5a8032cf.mp4?token=X1KpAptFE2hk1eZCDTNlhD5Jsg3qWOLx0aCWfuOyzX7IR3Y4wHxbEmQIbuuyEhn8bMP-0ZtVwLq26jcJo34vgxaUm3HAveBlIMCZY_UVVhCmpcznR9u0I2EcYItPjxUIAna9Hxy2oLib4wA9t1MXnHIBQh4aM19QijzurVELadg4KQNUZ1s6f7oDM5eN8YN0pQI8ibe9IkGTTtIU8ps2ttvuXKana-bLWDL7jdRk2vN0oRkWAsIHUAeVrHHCZoF2RTeh4umiL1130hzn3WV58x4aU0TG2vrQ8Ovcol20T_rRU8MxouMr8lhznvAnxhsPAS3-w5ahEiCRAFhMKz5jmqkuE9Tk5ueZ3evY82OdYavpb_jIQ5e4mYTJ-3jvM9s3d255c8WCCQWcLZBRPTpjL-BHDqZQVgYR8Ol0uTkG87T7L1iBBbZJRQAjLHTTn_YCgNFRYJJFNdvBjxEzowh1L2OY6dQw7HcqvQMKyugX9hby9cl6jUl5JWLXH1QMQCTZvICBHzyu1QIeTN2M9yErBIkjBm6bVikpOA_OVp-yj7IsmC0lV7vzpfnG4urPh54Nk6e1QLaIbec5httA3SLy7unA4U03h5aYHa9mm4vqqVlWnxZeiuO0kTtNGwbhfU5q56mtZ9KyvMTjNnP2JnTGpuf_fU9f1gNWNIpBTDZ43B0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✨
یادی‌کنیم از کینگ‌کمالی از اساطیر بدنسازی ایران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/102356" target="_blank">📅 17:40 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102355">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69a15854e8.mp4?token=SDG9U6C483ktaxEZjNtKOAYWwpdU9MtVHPluTSBL2ERxPDeNaFnidgb0tAPz7gY-4u-H-V4gtvQapvnY5n8b1qWytHOc1C75HpDuATB7a74fq-ZWBSe5FECGZAep07OH6-4VJPIRcwT5AxeTvafZbpmcy_XBn6KglTKsVtqL2XsmbpbmtzLp_Lqq-t0p-s1l3RjvpmereEWGYX2ojBBtINdSc1EM6UW_MTMCEzwajiay3Fiizp90dbZw4TMro1TV2l8jNK7e3LyoYuab5SysJ-ybYSOvdzjCSZ2jdnXD5aG25QqyL7UfFDb5_y4X7_-hPyezvNHJUorxn17qf5YxAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69a15854e8.mp4?token=SDG9U6C483ktaxEZjNtKOAYWwpdU9MtVHPluTSBL2ERxPDeNaFnidgb0tAPz7gY-4u-H-V4gtvQapvnY5n8b1qWytHOc1C75HpDuATB7a74fq-ZWBSe5FECGZAep07OH6-4VJPIRcwT5AxeTvafZbpmcy_XBn6KglTKsVtqL2XsmbpbmtzLp_Lqq-t0p-s1l3RjvpmereEWGYX2ojBBtINdSc1EM6UW_MTMCEzwajiay3Fiizp90dbZw4TMro1TV2l8jNK7e3LyoYuab5SysJ-ybYSOvdzjCSZ2jdnXD5aG25QqyL7UfFDb5_y4X7_-hPyezvNHJUorxn17qf5YxAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
🇪🇸
وضعیت این‌روزهای هانسی‌فلیک در بارسلونا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/102355" target="_blank">📅 17:27 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102354">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/262bb95a39.mp4?token=r9UgGCUoTYgIz5haqiNHIv-o13iccadlIziRV_zrCASc-zr0qGKtUWvRESr2sz_H9t_obSLUKj35wPs-Ex8-kq1ykIyjtlL2gRdtpY2fPjGpMbihnhoSPzNY-9hWwuBzBcXEBq8kCsrS6373bmho6L0SgRyxlJrd5zh-FzTjUdeswHFqJ4GRlUzv3-EDobBfE4It7J9r1YbJM3yoKCluQqXZ74NM0tQ0GV6z_RWDzaiHaPFcULQz12kLWRzu5V1Y-r3kyRGuzuImWJ2mwn2o68ocwOnhVLpSa_7PQ0Zy0lQokLmFoCyusxZ-tk4Ro53SFsetP2q4M_pazT8T7AKszQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/262bb95a39.mp4?token=r9UgGCUoTYgIz5haqiNHIv-o13iccadlIziRV_zrCASc-zr0qGKtUWvRESr2sz_H9t_obSLUKj35wPs-Ex8-kq1ykIyjtlL2gRdtpY2fPjGpMbihnhoSPzNY-9hWwuBzBcXEBq8kCsrS6373bmho6L0SgRyxlJrd5zh-FzTjUdeswHFqJ4GRlUzv3-EDobBfE4It7J9r1YbJM3yoKCluQqXZ74NM0tQ0GV6z_RWDzaiHaPFcULQz12kLWRzu5V1Y-r3kyRGuzuImWJ2mwn2o68ocwOnhVLpSa_7PQ0Zy0lQokLmFoCyusxZ-tk4Ro53SFsetP2q4M_pazT8T7AKszQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
‌‌ ‌ ‌ یه ویدیوی وحشتناک ۱۰ دقیقه‌ای از
این حرومزاده منتشر شده
🔗
🔞
مشاهده ویدیوی کامل</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/102354" target="_blank">📅 17:23 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102353">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bkwOsIOhjQmLdM26fX-IPIYgCcF1OThUPXiFoAiLqOToukRRzo2ib2kzGgt08nB5gOCF-X5R8wC3zANbgWojX6teDiV9H7oMOC7rYT-ZPaMDoSXdtU7GtFB2pSL4mm9SeSU9LtXJQ3zzFhIJm_QMdmnDN_OP-7hSCwyZqFuA6WopJV3WhBbdxoiar1IOhIw_cK0QjNpq3PSa88ojJuANkNJCWTolj15xBKSKYvX8Mz4alm2zFEnEtAzZgj86963nQHdV-Nukx3lnpnBLDxzDJCeXTFXC62O1xD-s4Xeh7q7ZtZnwgr4HnSyMxhio2W2925YTcFoR35yNWNL3gthffA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
🗞
رئال مادرید، پیشنهاد رسمی ۵۱ میلیون پوند برای جذب رودری از منچسترسیتی ارائه کرده است.
❌
🏴󠁧󠁢󠁥󠁮󠁧󠁿
منچسترسیتی قصد فروش او را ندارد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/102353" target="_blank">📅 16:58 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102352">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17f25fd06c.mp4?token=U15t-pWv2XMyOZPJyhPmLZPgRi3hVW_aKgvUmecrlKXT-HsBxvc0-lqjB8DahTjzoPhnV4Ayd9QXKxcRG19EbyZ8B4HxKWUfUb0T7M7BWdYvAx1I2K--9r0R8tOxQFmiIa7WBaATA_kfmgvnlJWs-y37WWEcW2KHV32VenWX0yVat04D_MmMaOetPG4p4rd-DFV6pUZFNyzKNkLxtwFs2l09Na4MvQ-DpoMGV4DnthuZKJz-OpoGqtEVD6ieODRbgrzOB78-D3_DbSr_WN_KuhtEa2OudphsQp_ZsnGiaqTltMtbNNNqG_2bFw63S3ZLb_aWea0LEuQSMwuvnNRg-Dno_RWNfVRGwdRzjBgUYRNNFd82ELNbGvX6Lw4sUOBNv4l5zf27k57Vk9xQXnQhbezmWPApler-zI84qfSyQosLmaxA60SnD5DJwBnUI3VmavHqWRTWfyPTRLYqUQN_UG0OHzvGIK8dva48AXolR4lcRcSxteRJvEjs8dEpjo05sqeKXBRNyAYgK16h1PIihK5vqFypcrJIWaN0B1DQICxLgoQOJdoXTwHd44QzBtPyN9M5EvjSftIdSIsU7nyzQRQp41lhD0lOTI7AhtBTi6Wc6wjZUae__d488jWKp3rvvetcmb5b2LuuLkSYiZPClQUWtDjTGk5PPnBKTK7gp00" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17f25fd06c.mp4?token=U15t-pWv2XMyOZPJyhPmLZPgRi3hVW_aKgvUmecrlKXT-HsBxvc0-lqjB8DahTjzoPhnV4Ayd9QXKxcRG19EbyZ8B4HxKWUfUb0T7M7BWdYvAx1I2K--9r0R8tOxQFmiIa7WBaATA_kfmgvnlJWs-y37WWEcW2KHV32VenWX0yVat04D_MmMaOetPG4p4rd-DFV6pUZFNyzKNkLxtwFs2l09Na4MvQ-DpoMGV4DnthuZKJz-OpoGqtEVD6ieODRbgrzOB78-D3_DbSr_WN_KuhtEa2OudphsQp_ZsnGiaqTltMtbNNNqG_2bFw63S3ZLb_aWea0LEuQSMwuvnNRg-Dno_RWNfVRGwdRzjBgUYRNNFd82ELNbGvX6Lw4sUOBNv4l5zf27k57Vk9xQXnQhbezmWPApler-zI84qfSyQosLmaxA60SnD5DJwBnUI3VmavHqWRTWfyPTRLYqUQN_UG0OHzvGIK8dva48AXolR4lcRcSxteRJvEjs8dEpjo05sqeKXBRNyAYgK16h1PIihK5vqFypcrJIWaN0B1DQICxLgoQOJdoXTwHd44QzBtPyN9M5EvjSftIdSIsU7nyzQRQp41lhD0lOTI7AhtBTi6Wc6wjZUae__d488jWKp3rvvetcmb5b2LuuLkSYiZPClQUWtDjTGk5PPnBKTK7gp00" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
مملکت به شدت عجیب و غریبی داریم
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/102352" target="_blank">📅 16:39 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102351">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/138f735fee.mp4?token=vM0ZqAebWYZNcfabjuq_dCuy7MxigBUAnTZUhOSx4zuMeOChK0wErxxm9GnTanI67aFCe8a0QAhEko00o-1ZfZ0tOjyKec81LCIT2dScSB4oD_TSb9A67n2EJlLXnWOvLOOZZqZb4tOvZnZ7CMcm82Yi4Ncc8O4vHmmhWOWI2Cpnj_4gJDOCh2KWWdYG2jF9PqlZBFR2EAy0_derGuaUZ1Qu6nkEMjuUmyekwwOLD20klM4DitPfNCn4PWKQvaKh3s_XiLupyQPc_Hhvp53D_XLqiNC1gMbw3bmL9YsvqIO5Ur9PLPx60db2m16sipyGyvXlvitFTeV2ZOPkznhiIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/138f735fee.mp4?token=vM0ZqAebWYZNcfabjuq_dCuy7MxigBUAnTZUhOSx4zuMeOChK0wErxxm9GnTanI67aFCe8a0QAhEko00o-1ZfZ0tOjyKec81LCIT2dScSB4oD_TSb9A67n2EJlLXnWOvLOOZZqZb4tOvZnZ7CMcm82Yi4Ncc8O4vHmmhWOWI2Cpnj_4gJDOCh2KWWdYG2jF9PqlZBFR2EAy0_derGuaUZ1Qu6nkEMjuUmyekwwOLD20klM4DitPfNCn4PWKQvaKh3s_XiLupyQPc_Hhvp53D_XLqiNC1gMbw3bmL9YsvqIO5Ur9PLPx60db2m16sipyGyvXlvitFTeV2ZOPkznhiIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🎙
برترین‌های تاریخ از زبان رودری ستاره اسپانیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/102351" target="_blank">📅 16:20 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102350">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🇪🇺
🇪🇸
یادی‌کنیم از آخرین قهرمانی بارسلونا در اروپا با مثلث تاریخی کاتالان‌ها در خط‌حمله
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/102350" target="_blank">📅 16:00 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102349">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nbFIsuKKf3FGu5i7POWdem0zpX-RACKRefvJDbNTsiN8YY-yWdIZHjCH8iCowT1SnusVWZteN0Ls19XqWJgp1JofY-XJEYgCZ-rUkiCIj_ZM_CTMYbxerAsZmuCBac1-mJySLakqZPVqfB8ikZOjN5Dl5JzJctVG1R5epgcTeRjw2NGfJ3m--SAjbiFv7nSY9kbcHnBO0yK9lsiWZKgVlUDnJdFNfJ3EK3CjV50WCfSSYYT0EuZBHM1rbVD5CN71ZWSz6VRo04l28btsRMiP3lMMEgmvlMl_VxYNZYcvvEHrcBB5fHK-EkkI2YubaVy-e980EkqknHhKr5YlAcW1JQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
گونزالو گارسیا به فولام پیوست
۴۰ میلیون یورو
۲ میلیون بند پاداشی
۳۰٪ از فروش بعدی به رئال مادرید میرسد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/102349" target="_blank">📅 15:45 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102348">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d88e7b9804.mp4?token=YJIYB_p0NKiMqKC5d5_k7wVz-ukcQCNaZUfpUPqM4jaBhI3gGFN44SqUETldFoQJoOu5Sejw7BLSFP9qJBKgjV72zqwgNaZW-kmiP7_7fQGXnfF0UvWBAUNH0cIet_IJoUreDBhmHZ8SOlzDQdthnlCaBij7hirBc1jw7gcmvL8VbH13rpZFKijy26hH8KCznpEq0YG-RzIRki6VQ94chlzf-Dpkro37dii3ZRxznMX3uOBAQz7D0UhDk48JC0vwl83TTcKz99h8_jj8hZCNjbNA8uYDa5WTcBePsv-P06IqjN1B1e_cuEtFBGjkwxcvKSqvQPbv2jTA7Y8IhKqlhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d88e7b9804.mp4?token=YJIYB_p0NKiMqKC5d5_k7wVz-ukcQCNaZUfpUPqM4jaBhI3gGFN44SqUETldFoQJoOu5Sejw7BLSFP9qJBKgjV72zqwgNaZW-kmiP7_7fQGXnfF0UvWBAUNH0cIet_IJoUreDBhmHZ8SOlzDQdthnlCaBij7hirBc1jw7gcmvL8VbH13rpZFKijy26hH8KCznpEq0YG-RzIRki6VQ94chlzf-Dpkro37dii3ZRxznMX3uOBAQz7D0UhDk48JC0vwl83TTcKz99h8_jj8hZCNjbNA8uYDa5WTcBePsv-P06IqjN1B1e_cuEtFBGjkwxcvKSqvQPbv2jTA7Y8IhKqlhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
💥
حالا که بحث تیم‌ملی داغ شده، این تیم‌ملی و بازیکنانش بنظر از همه سر تر بودن :)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/102348" target="_blank">📅 15:40 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102347">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0063915b2d.mp4?token=Sye1ARVt-22zlvptAc5p4mjKY5gPzEGJo0XrKUru-icOIizsJT1EdS8Q0PfsH1BCrzMWzLDtu7exYSfUNIXU1UNscp7Rk-SNUSao2-TdisxB6jrC9Zq7A_sTOY9TvmLZCqQFsu5Y9MyEfErAVBlnyWbX7LuP7to1EmsR_C6n-WsDIQCZb_Qd6wsXWvpm7gv5deD-eJtKj9ioXfFWbar8SqwGxVU4NNc18TlnxSPmNgiVruoEjuJYmuPQqhtXtHPDKb1VSH6UkPlj-MtoM6D3ChDrlbfSzUVR96bGFodjkjcEyjI2_YlkrHwYChahj737XBTFEHpSa3ExAbtlIIkamQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0063915b2d.mp4?token=Sye1ARVt-22zlvptAc5p4mjKY5gPzEGJo0XrKUru-icOIizsJT1EdS8Q0PfsH1BCrzMWzLDtu7exYSfUNIXU1UNscp7Rk-SNUSao2-TdisxB6jrC9Zq7A_sTOY9TvmLZCqQFsu5Y9MyEfErAVBlnyWbX7LuP7to1EmsR_C6n-WsDIQCZb_Qd6wsXWvpm7gv5deD-eJtKj9ioXfFWbar8SqwGxVU4NNc18TlnxSPmNgiVruoEjuJYmuPQqhtXtHPDKb1VSH6UkPlj-MtoM6D3ChDrlbfSzUVR96bGFodjkjcEyjI2_YlkrHwYChahj737XBTFEHpSa3ExAbtlIIkamQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خاطره‌بامزه از زبان فیروز کریمی
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/102347" target="_blank">📅 15:20 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102346">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2314f18179.mp4?token=Gq1GkzNixWGLsxiASxGHgB4U_44FsImgT8pRdTa6vX1g6BWdpBlgfDOr7r_XLyussXTCJ1L9X8hT9L75zckf42IwdPVwrtfmLHh4w0OrPvAEKHXf7X7iRFESACK0XheHt-NQdpTmyUAEU7Cz5DpbJjwAZwos97dR_q5bcsIlqjF6Vp8A0PHK5mdhlVVul7Oktp9IUcYPXcwzxme7fbQWIY5HGRIxqKdcjUZuNO5-n4Xw0Bhxq9B8Oog06yS47EdjEts37kMgCbNqnneW0FIFW2VlnLAwgAqb90QSyWxkYrLNjhe0PcD-BbofkgOmw9Oopfer8JgZv283sdTXbvZOkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2314f18179.mp4?token=Gq1GkzNixWGLsxiASxGHgB4U_44FsImgT8pRdTa6vX1g6BWdpBlgfDOr7r_XLyussXTCJ1L9X8hT9L75zckf42IwdPVwrtfmLHh4w0OrPvAEKHXf7X7iRFESACK0XheHt-NQdpTmyUAEU7Cz5DpbJjwAZwos97dR_q5bcsIlqjF6Vp8A0PHK5mdhlVVul7Oktp9IUcYPXcwzxme7fbQWIY5HGRIxqKdcjUZuNO5-n4Xw0Bhxq9B8Oog06yS47EdjEts37kMgCbNqnneW0FIFW2VlnLAwgAqb90QSyWxkYrLNjhe0PcD-BbofkgOmw9Oopfer8JgZv283sdTXbvZOkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
⚠️
تمرینات پیش‌فصل بادیگارد لیونل‌مسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/102346" target="_blank">📅 15:04 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102345">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🇪🇸
🔥
۵ گل زیبا در تاریخ باشگاه بارسلونا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/102345" target="_blank">📅 14:40 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102344">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1e80cceff6.mp4?token=D6O90FXej7zJmWpYJ61gF14iSWHCrAcNGVUHGSsTvix1Y03FyHlBceuQyBKTmKsD5InVKJuWf95nfGGBH8QjhqIQe544eKO4i2XFhfsJ4vaW7x7NWO8kJNLUKoV6o5DHJF1_RjQhgcZVflmXFlhIuMICCRMCKfzMfILjexKduS7gr5S96KtP0rcZjRme_-likK-dk5CIGFjpDWX1Zb2Q37liT1wNZCehVySva4B7jM_kf1GN8Enn0vdZpU0ApsIBCSM2SepkMaN__Bt-4hcjuwqXkIcXhrwtyxGNwJchgmi67FiBmGVM6YBzh_un7xjj-owlIgx0QgNhup086AN3WVnwEmrJHl_iFVWxkL78h9LvTKcoonXknrD0QbOi1DUgHHHozeBntBg0iGiTc9UKVF5_FtC9trlAtQNUkAswAwWgK9bSZL2hSaX-OzlN44-wisPprh_STeloJeh-3bBzNvR9VHdEZUrehECFf2HkAXBrJR_wdt8D-KaT2-Ckv1RjV-jNj01ujdmZrp_fw4fC2mIrtRtG0mTJxC_kZBKSzUCWge7mlCP5H59Zzdtf_WVlYmtY1EnIa3YIgoWWR-7GhYvu0fVp8I3aOWzsGJY4omiA5Pdytcuyc0gs7nIDDRxvSN-M4G2Cgbz9rLKiOKPZed7af4ETkVqvGBeF9a90Ge0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1e80cceff6.mp4?token=D6O90FXej7zJmWpYJ61gF14iSWHCrAcNGVUHGSsTvix1Y03FyHlBceuQyBKTmKsD5InVKJuWf95nfGGBH8QjhqIQe544eKO4i2XFhfsJ4vaW7x7NWO8kJNLUKoV6o5DHJF1_RjQhgcZVflmXFlhIuMICCRMCKfzMfILjexKduS7gr5S96KtP0rcZjRme_-likK-dk5CIGFjpDWX1Zb2Q37liT1wNZCehVySva4B7jM_kf1GN8Enn0vdZpU0ApsIBCSM2SepkMaN__Bt-4hcjuwqXkIcXhrwtyxGNwJchgmi67FiBmGVM6YBzh_un7xjj-owlIgx0QgNhup086AN3WVnwEmrJHl_iFVWxkL78h9LvTKcoonXknrD0QbOi1DUgHHHozeBntBg0iGiTc9UKVF5_FtC9trlAtQNUkAswAwWgK9bSZL2hSaX-OzlN44-wisPprh_STeloJeh-3bBzNvR9VHdEZUrehECFf2HkAXBrJR_wdt8D-KaT2-Ckv1RjV-jNj01ujdmZrp_fw4fC2mIrtRtG0mTJxC_kZBKSzUCWge7mlCP5H59Zzdtf_WVlYmtY1EnIa3YIgoWWR-7GhYvu0fVp8I3aOWzsGJY4omiA5Pdytcuyc0gs7nIDDRxvSN-M4G2Cgbz9rLKiOKPZed7af4ETkVqvGBeF9a90Ge0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
فرشاد محمدی‌مرام درتست گزارشگری سال ۱۳۹۴
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/102344" target="_blank">📅 14:20 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102343">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NE9DpPyaUHyRE92E2NZqE9CUDJSlln_hUoAe7oZp7FaeFyQyTA9RN8rQvF2iNGsKPaq7-t_qLoR9kqQAnMS2bXwR0eRCcNlBChTon9v_iC0TmdXhRr3VVdUvyInOiAVa5GIx_FX0OQ54LgCjUv6iifNxn9bPtO28m-EwhymE1aetEAjp633xfu2_b-r-1-FYQ6S-sd99Fie2MRd0gWCgh72_u67lzdrp0Mh6COryDnNc716wWK5csrCgKP13fQmG9PplvzY4g64veFgFay5PvV080diVmPRukOV4_Xp6Msjd4OSjOt40_bYwkC60uko-cfUNkBbVSWGgE4XdPyA7BA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
🔹
رسمی؛ نیو راموس مصدوم شد و حدودا یه ماه و نیم از میادین دوره‌.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/102343" target="_blank">📅 14:16 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102342">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3336c43202.mp4?token=Tq3JxQ2KA_imgUherAHFrVDEAzXOsgNB0Ao7rWxULKvss2DYHw5lBQ84wNrD1MR9BuqQCLzlM_x-n2WVhLr3YjhQLKxAu4JjOiDorafDln4heFrvYzAMS8zCTyj9hM5SCNsZsQtI9Sygf96Ngr0V9-X3NV82Yz5XCvBJni-lj-Gm0PU9dIFWoCqb5JrHBT-Vh7A8nV7aqjyJkIhApTldkVwVp6L1nNu3qernoKuYYvhZsEcvXHo7h9P5XSIccnH2auZcrGiqtEoauOqam_2tzeqWbIamtrFCeiBtIuMeHJuDB9AJcCA7EMRJ70STopyLyaHkhWzXZ4bb96bE_76G6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3336c43202.mp4?token=Tq3JxQ2KA_imgUherAHFrVDEAzXOsgNB0Ao7rWxULKvss2DYHw5lBQ84wNrD1MR9BuqQCLzlM_x-n2WVhLr3YjhQLKxAu4JjOiDorafDln4heFrvYzAMS8zCTyj9hM5SCNsZsQtI9Sygf96Ngr0V9-X3NV82Yz5XCvBJni-lj-Gm0PU9dIFWoCqb5JrHBT-Vh7A8nV7aqjyJkIhApTldkVwVp6L1nNu3qernoKuYYvhZsEcvXHo7h9P5XSIccnH2auZcrGiqtEoauOqam_2tzeqWbIamtrFCeiBtIuMeHJuDB9AJcCA7EMRJ70STopyLyaHkhWzXZ4bb96bE_76G6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
💥
رتبه بندی سوپر گل های فرناندو تورس ستاره سابق باشگاه لیورپول و تیم ملی اسپانیا، توسط خودش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/102342" target="_blank">📅 14:00 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102341">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U6IQGLjzfKaDN-Hup90zt_xnD9EQ45bvJMWj-6otY133wjEh7OsxPQ1mpaTqoK-PPvjgvu4XE464NySlZV-jLPTrV8ATvVx5L8afyv-CQv2NZK-6Oi3JVhKH4OhXHuMrVyLVGFwiWM0-yYaPyLcXFvxiUF6fd1kkF38hFPl7UN9FA6laSqhV3IgQq_C0Yk8rG1WrveZ5k8nHsQ68X9IJWjDNsFGqw1FeDr_YtCjaynDDZDJCzrAW7311Q2IyvwvhpJSWmRKGqDi9i-zSANJM93ib-iA6jbKKHej1M_5IedRFm2EWOTzk66jvIakmBEDbqqfU8WzIQjsSyvvInyV6QQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوووووری از کوپه: رئال‌مادرید و فولام بر سر انتقال گونزالو گارسیا به مبلغ ۷۰ میلیون یورو به توافق نهایی دست‌یافتند تا این بازیکن شاگرد آربلوآ شود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/102341" target="_blank">📅 13:42 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102336">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T-jdjmS-pwGQjboowRv7Dlkvmz-QmwUNzQvHBIObJvBIZ0AHixTw1JGCAcF9nk-bDxVclK2Ew1ofqpCZhEkI8cMmZ0MyFvksA7hKNB_T6I_AQp3XvLjGE3E39Hn6Nqi4DeK5UhCPd-ro2SU2JUxYo9QyECaD767QihepIw2Q-0iOqwmkxzTv8LKgwB12D1o-caySVTU8e-p6lD23b9gu4FhC_u_xtFtuD9bEJ2x6sDtjpdl8jdCoRFOZ83k5ZVrSH4vHU1FbAa6dmssaeHDe83rCZ3VyxJZyhrGay-st647qnvl2j9FREI6_1TIq71DfMpuniL9pSabk8xwIiekOuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VHDeL1-PwBIi7peD9_9D_G9pwkmyTApV_I_k4aVABvKeuHcCXe8IVdrka54K-wY-T9b_ByoPf6HDNzp5IqpzSJG35pDShTnVb8c4JFm-5kdoWInftUdyc4_TJdZ-SVZ-h1U-gT5RorjK4ddc6rnDHYeqwD_y45-ME9duMhZkTr8VqSBKsOrN75PROUzx2y9DSjhoJF8yQOMm17dqHvri5wBuzfoVxSRtHQR4x3INIsB5CXXKjE8QiJmTfrMOp0UR0hFNqE9XFBna81d4wpgDb-lXe67_jPwBoJleaS4ktq0o1AbWxG3c5xWQM8aWwV_IbiDZx0lbQt3_BO7QaPxkOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VQKUwdai_jhPYpSFDjbSo-5nke6AvbblrDRBUDhvDfgGGOzCuaTG1U08ITvk-sWEuCC95V2-PSFHvu7vZ4ut5r4xnl2Cu30vItwjLNqYTLWrg0Y1km4vcB8nhq1uiFvX4OCxIeu08OUx3VbjA7BxMoRp01rxQU6yqtrWEo88WpCvBzNsFTCvLnYgtz4vHw2rBHq_ELkp8pC0IAi3Y27o941LUb7FqHOjl6eEczUBC6QmilaRRnqk5as3WaJO2Lnz_yE5jnzdg2_e1dOt9nZaQcxTRxtR2rL0woMtGHR7aHV6jMaVF4zBkDlO4vkNr7TQYg6CLAuxBJ3fqywfWBiXLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mp2iRpjzT5AEIjsdY0sOpzL-tasYWmbxTosPwRZI5iFTsBmRC7shObkVZ5r3CoKnGKToJ0-MJ4wIpqEuf8eDE83Jb3PIIXhv6KmTYvuZT8LFJ0jMxJTKi5T7GQg-eDEqo3-SFCUUpU8BU3qukz5Qr6kdZYdN8F0xhRcepaUjyJKR7PyZq6BI6LqpTWgnVDevWk9MoQuV2VvuFXah0SD3sOf34F5sAlvkKLuWMD_UWfsgnthqgxiIjj_ZBokaYBjcMKj5sP2unTNkKF6tLlAttJQxWDPTro3SU3lYIeRHbzpC_KGhecejmybkWP5cK2xf1IJUQVzYJSXUo5xvd-65vA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K0FeTZSpL-IJdoZ0VqMdQTMdTLH_0NQvjaPJqn72PyXvAjrSkNIyK_n6lykhgKxupw0zu8yOcC-NPiWwHJKKI7r42xvLs-LLXYGOcr56Ot3zoGhZyCNMmZjKcm1jmWKZs6chLw9gdORd55GLkcZqdxV4Th4tBxVEi0_-u7aFMlJokIB9JVo1VeT4mOf7bSgI0IcyFXo0oeKXNuSNN7PAZCtTMskI_yaof_zVVMT3eecNTwuYHgTkTO9vkNEy6VKtIR4F8QqGA-VMVYy1t-i9UE0ADUUOtj3Tuv40uARtnOyTBvcJt_GX71T9sqQsdMJHDMNSnHKTcZ3gBs8B72cbgA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">+ قدرت تورم :
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/102336" target="_blank">📅 13:40 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102335">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V2861q5N_CCgCk43ukGDJ_BVhKaBJjz-woL6v4Euyb6jcX0J8vduPVq0-_nOVi7Kdy1HvACyed95bb-E6djr2WvuSmhx-XY__utMj_EKe6HQIjqI8M_JN-V9EHm_VE0DWgfgqWuLBkBog4bmJZe9_93sw2WskqOKLmzBPUCoMwc9o77YNzHFzo3IA5ng5xh4UNsORVge4gv_cMy2WAxFencTEeGv3B4zzCO3d9QOk-BVXwWX0LToy1Pqr0OnY_-uf6RCg-Zl1UoTlGiXps2dDSZSi85NL6J58neh7yNBGj3fUbPUpyY-F9fhwJGJD-Q2dGZPK7SYS0QY4pV5Eosx0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
💙
#رسمیییییی
؛ روزبه چشمی قراردادش را برای یک فصل دیگر با استقلال تمدید کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/102335" target="_blank">📅 13:35 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102334">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/btLdt2OO5UcfpCXNYV3dsrbJaxlLf4bNEHo6nFArjeMwINNvixUHtk-5HUUttnTamDKVK6umf3NHBE4xOl7i2Gv3STetIL9fCetsVA8DERK8msRmSdSk7KKfx4ECXiulOYebSE1LDerQ4R_NgqKhj_X0kkl1LaBvLa2mdJQPM0yFRgmvRQCd_1cu4AnPzmVCY7z9nCqSTRlvLdRtpG7JWv05kJFq6OLR1L21kDofG_hZE43bcPyo91--EHEGke06zqyDkvNDKt4s9FXiin9tzy6m_cuAEb2zZwtWV_jshbirYQIvVcDty0C08qTLmC55Qj_wV-UtjG-0IeDKmw4hlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇹
⭐
فوری از فابریزیو رومانو:
⚽️
ماکسین لاکرو از کریستال پالاس به چلسی پیوست. 𝙃𝙀𝙍𝙀 𝙒𝙀 𝙂𝙊!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/102334" target="_blank">📅 13:33 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102331">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/einZEH9MtBjIN1Tw4EiCJhJvSL3EB411jKmzM5Sf1bB4AUNq5F_nLAIfik7qaSQcnnboj4Pmo6A5KqlsiPwWrw86A_ZK6sc9EjLT0gzO46ISWZeketQosSTVPN7ZY0eY2AHIR-ZM1C_K5WtLvurl8YLDWlyh7rrTdLr_F0g_r6KFv19pXFcNbft21VgjvSgPawoFqw6GT2CbXE6FnwrNvx0UqTfc77wjMZ-LT4RWpXjIxUpVf_YyOWGAcwJRtQpqiBje3G6qcymnXHINkPGaY25sA8PhKgUtPom3e8j2NCi05yPM4YLrnvVUEA-sgua_QcS-dJnqgVZoO68_S1SX7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GpMZKfUu10dQvLFB87aCj3dgY-lBDEImAKORRofHHcvjxu-FdQuCfmmxKTQgXCLZZKgOkFmc77gdEOmen9y_n4CpqQLIdFq8gjdHaU41F-IOX5k2CUgFArXbrPN4sxLUwqrFeri0VoWsMOnaLzGECAexM8AGV39PVr9aVYWbXE_7XiQR4NyOvDKtffmQ7INX1qnPXUlvMFwmyyjHaPQDLCHQgNh5ee8jB7sS7rJnLcq27fl09oujTb-oMipKTN2rPDxrrMIrSP1GT7S5kjJEUPfLQwBnjMMybBoHxGWAFINJ31AH5I969c4SVl-59YTU_9vNko0nFYKPFqjub6jQXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q6b8n2FSYvFPVSRPy2fCoI79NPKKzxD35RQO1tSqvkSEGQ0kBaglZYBkiF2SvHuMNVzel81mxlZZvxruL7NYp2iCL67aarMHdOQc2InszkouUmvSuACNXvg4SJ5_9z-I0JKdgj_dVk_DmxPpU78b95hwVDWJcrAfqeGGmICD1Kw9Rrkzg2_iCclV1qH_WD5W6bprzHqBE4wCVIP01B4QAV2A8kxILzqO1iuP453rMCYs4QxBdhgtsgMgZsQMpzJC2mNwH9fBT8cXdscEtUkhW-hWZ-_9bewOYdgc5OwC7N7BgfmmeYqHNhgfVFPwCjpI6qmmMty09f2aep6uJ2UHSQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
🚨
🗓
🔹
اعلام برنامه مسابقات سه هفته ابتدایی پریمیر لیگ ایران
⚪️
هفته‌اول لیگ‌برتر
🔵
استقلال - مس‌شهربابک جمعه ۲۳ مرداد
🔴
شمس‌آذر - پرسپولیس شنبه ۲۴ مرداد
⚪️
هفته‌دوم لیگ‌برتر
🔵
استقلال - نساجی سه‌شنبه ۲۷ مرداد
🔴
پرسپولیس - اس‌خوزستان چهارشنبه ۲۸ مرداد
⚪️
هفته‌سوم لیگ‌برتر
🔵
استقلال - سپاهان یکشنبه ۱ شهریور
🔴
پرسپولیس - تراکتور دوشنبه ۲ شهریور
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/102331" target="_blank">📅 13:33 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102330">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PmQr0i-DsIADgZhbzbbqS-aMpJ6E0rULZtJ-q_zQ67PrgQ0QyvU-uWP-7__CrFW5wgEbkMqqNS_3gwjSCc1eaEsmoH90-shIldoeWufmFDCDvELkZfvwY5Gj1VorOdSZzy8v_zvB_JIzmqmRgI9KB5MJXqWA1mPM0CN30d2Sf25xlo5yL-p-BaZCSbpBONQzg2hDxxArUk8EjVQmIp_QXvzdsPJwZZd9cgEEAD496izoLUuRbi28S3AWYYJn_tE11CkUqOCx6-iMQ7lDiUl7t2zW5IJRV8z4CUOV2sjkquKwlI_fiLiiL6o0f9aUO_I6Rl6pWC0may7gx7u5Kox41Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوووووری
از کوپه: رئال‌مادرید و فولام بر سر انتقال گونزالو گارسیا به مبلغ ۷۰ میلیون یورو به توافق نهایی دست‌یافتند تا این بازیکن شاگرد آربلوآ شود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/102330" target="_blank">📅 13:16 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102329">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NE-rzNKxOrnZayIuzi6sD7hf_Q35ck5gzOKhqgeD1F068WDV2-z7hSbPg83YzDURrnAxXdGmOMw51cohzkxi1hXImjd6AcJBtkn5r3ODf0M8sFeCPfH1PzVNZjwcgIPOCUYPXh8E_1pfFtzrx9WK3yrETZy_94I1Stoczowi9asVy3lH5yS_nCjtgr7pQYfh20EZ7woMES1OKiHQLY6PmePy3VWLLMoCtsvvp3IjOTYKrAMJv8YSqx7hnsib3p6iMAJA0OFL9WaM6xNGEWClCrckLLD2bH0MpYnaaLERYVhSugTqEFKx1vqpljAidwefPq4qa1MF5ej0dN5SgOl4rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
‼️
✅
توییت مجتبی پوربخش مجری سابق صداوسیما علیه عادل فردوسی‌پور.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/102329" target="_blank">📅 13:14 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102328">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee8b739e27.mp4?token=GtpKErFT-c_gOlWtQyty3Uzv0FnOkp1XGKvtX_Vb4enacKXP8_Dhr_aSU01sxEVNn9QadMVGJ1GJAYSv5VSQE4b3GqjLfqU6yRWPmyWZDmKq7yVwkhVP2eUMGQ7n50TdNpACTpar1porKf7PiiZ5fJmZbBmname9sq7FPB6igTm_oq_98jIda8aEzitK4ts0rsX4ylyhF6co9A9u5gFmZreBN1qlWGy-cq2uuEwKltLpBo_FqqeOWKe_kTGlCFB9erhP0aEwfEstXLwsaLemMGgtt3jaq52CkROoAPLHUv3PqGld-kB8F7fX2uYR07qD07amv-Eb0zyDtR_bV8f2cQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee8b739e27.mp4?token=GtpKErFT-c_gOlWtQyty3Uzv0FnOkp1XGKvtX_Vb4enacKXP8_Dhr_aSU01sxEVNn9QadMVGJ1GJAYSv5VSQE4b3GqjLfqU6yRWPmyWZDmKq7yVwkhVP2eUMGQ7n50TdNpACTpar1porKf7PiiZ5fJmZbBmname9sq7FPB6igTm_oq_98jIda8aEzitK4ts0rsX4ylyhF6co9A9u5gFmZreBN1qlWGy-cq2uuEwKltLpBo_FqqeOWKe_kTGlCFB9erhP0aEwfEstXLwsaLemMGgtt3jaq52CkROoAPLHUv3PqGld-kB8F7fX2uYR07qD07amv-Eb0zyDtR_bV8f2cQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
روزی که مسی به برونو فرناندز درس فوتبال داد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/102328" target="_blank">📅 13:01 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102327">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uZuGFELVU1_s2UA9qvLS0q_rAv9DPlFyYZxAWQAoYhMxxkFC7m3o7z9Amlwm3lKU8vFqfNM-LOgdYvgd9ARXmuWErKpxmmNgoBoSAFWk4Qg30G72yEqeoo3IXkXqUdDHhr6psvsePBjnPJmDctfDbWl9a3K3FCeWeDxK7RZzMBptZOxrVvarjUahtuTljB3d-wZpjacmkc0a7ePrboqUBFgmcFYYOFRdik-3fyi5c7zGRG7Y8LBSzHsEzDQ_p0c8yVrDI_XUoEPs1eUpiDCLVmes905sQSz2LcpDRE6TVMtifvrbrzbSbKOPozDUHCGLOHAMJBSJunptEdh9NkGodA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✅
🟢
صندوق سرمایه‌گذاری عربستان سعودی ضمن تقدیر از یاسیله پس از کسب دو عنوان قهرمانی متوالی در آسیا برای الاهلی، با جدایی این سرمربی به مقصد نیوکاسل موافقت کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/102327" target="_blank">📅 12:48 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102326">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa8a1ce74f.mp4?token=kTwqeDIxcqWL65LB5UeAwuGawE-HeWfvzDkBPYNExDCXCYZyNYe8Qt92GSATrLNDXPnsxnvuZWNK064SSG5P8aq-Dior0izbY8YwtpB1CxcAM3FttfRWyIGpapHS5RmrfDZp7-Eupa616L-99hqSOtyq9SHrv8sVHAnazYPS9Ih1t7XBUAcl4uJoniN5FBPvCUiZ79dqSjHv3Wvszq5yEKtCKtaKpeEO71c-eG2RCWusMABmp0ejharcpUqvF2unL25K5V5LGk0qbhQ6K3V2lfwOLxC_3UhemfzPAl-bJGNuz0eZhGQVxF5z_bP3aga1rqbe3uBQ4GUWkEbzDXEeaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa8a1ce74f.mp4?token=kTwqeDIxcqWL65LB5UeAwuGawE-HeWfvzDkBPYNExDCXCYZyNYe8Qt92GSATrLNDXPnsxnvuZWNK064SSG5P8aq-Dior0izbY8YwtpB1CxcAM3FttfRWyIGpapHS5RmrfDZp7-Eupa616L-99hqSOtyq9SHrv8sVHAnazYPS9Ih1t7XBUAcl4uJoniN5FBPvCUiZ79dqSjHv3Wvszq5yEKtCKtaKpeEO71c-eG2RCWusMABmp0ejharcpUqvF2unL25K5V5LGk0qbhQ6K3V2lfwOLxC_3UhemfzPAl-bJGNuz0eZhGQVxF5z_bP3aga1rqbe3uBQ4GUWkEbzDXEeaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🙂
یه فلش بک بزنیم به زمانیکه داور زن بازی رو متوقف کرد تا به کاکا کارت زرد بده و باهاش سلفی بگیره.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/102326" target="_blank">📅 12:40 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102325">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/49420aa7fc.mp4?token=fE1ShMo9XrrBD6aDT0jDLCEK0jGwJ4VPJ3FsESDv5CuLClJPIxHsODtkqo9Uu5FdV_hc8HtAkl3EpVbJ2v-323oLyuqwimZqa1wlLXEydV7rhAlI1I9aLYlXs1eKZJdd5LoDwdqI87oScNGLwrimK4CudeeS6pWL7w3OaShAF79fphEEo7p-GI40WDOfqF8ioXSMoHqZbhOo5BY8YpEFNBT3H0h_7o5EkCqV5RRysK_ZSyc1v3B6Nfbv28O2nLXcMu5vYsu5thOl5VGfzeBiHiza3IVSoFPp9npbBQu42Js6kWcmsefGgCBmJuCItgp7MMUJIVIh5Ba-3KvFeIOb_GApe3b-FLD04u55QujzVG0pjMSFrT0-sSTD-dreqcGK3tSbguMR3kpo9BSNOs69XN234V051-z_KMAi8EXBCDqgrWHbgMLojaF31BnWI6mNxVvFtQ6TVuFkORD1kgoHk7xPY5h3sBxarXWznyT1OoOymenVFnKodqdnn-o0iyq6rJXcEpaYPaPauB55_5AZA-RS4qRYb316M3i4XvX7zSmCKfZU3cBRKs-7yoMdBtLi9TMVbvr_4uuGflNADIceSMFVCqsMxkh93OBl6n7WQ_jSx2Au0-VCrycqXyG3nPqvHHKJJuoypN2A5q2ey6QrGeibdjNd5PXzWaZjX9ms-2s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/49420aa7fc.mp4?token=fE1ShMo9XrrBD6aDT0jDLCEK0jGwJ4VPJ3FsESDv5CuLClJPIxHsODtkqo9Uu5FdV_hc8HtAkl3EpVbJ2v-323oLyuqwimZqa1wlLXEydV7rhAlI1I9aLYlXs1eKZJdd5LoDwdqI87oScNGLwrimK4CudeeS6pWL7w3OaShAF79fphEEo7p-GI40WDOfqF8ioXSMoHqZbhOo5BY8YpEFNBT3H0h_7o5EkCqV5RRysK_ZSyc1v3B6Nfbv28O2nLXcMu5vYsu5thOl5VGfzeBiHiza3IVSoFPp9npbBQu42Js6kWcmsefGgCBmJuCItgp7MMUJIVIh5Ba-3KvFeIOb_GApe3b-FLD04u55QujzVG0pjMSFrT0-sSTD-dreqcGK3tSbguMR3kpo9BSNOs69XN234V051-z_KMAi8EXBCDqgrWHbgMLojaF31BnWI6mNxVvFtQ6TVuFkORD1kgoHk7xPY5h3sBxarXWznyT1OoOymenVFnKodqdnn-o0iyq6rJXcEpaYPaPauB55_5AZA-RS4qRYb316M3i4XvX7zSmCKfZU3cBRKs-7yoMdBtLi9TMVbvr_4uuGflNADIceSMFVCqsMxkh93OBl6n7WQ_jSx2Au0-VCrycqXyG3nPqvHHKJJuoypN2A5q2ey6QrGeibdjNd5PXzWaZjX9ms-2s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در هرجای دنیا همواره فوتبال آبستن حوادث است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/102325" target="_blank">📅 12:20 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102324">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IbG5pl8Ok9bJtyh4__9Z5mdZIDHu32xZ1m8YgujC0LrqFiH-tmtqJLXPn3CqL8grNYgKfcKMmE2Eye18Dw9owaEsKruzqW8Nzq51ixd9mAXwkCxu0dvHegqZq8lyYbgTRBVmZ7pTz0Ke0HlBR6arOR6cxh1hqlB5hUOIu-mV5NSFkuBcnNX-CaXr-RzXvAxetHxR6I39DRAiKhqTuVpqX3Fcq7jTiSEUOjFPwrSW_xOEaoVcr_Pg_AlZUMliiYun8NY3qYO3Zh7t9D1zi3Ed2xDegcEacpaqkl2oY4s0EGUFyFPFhQOLg9eQd4v5vyT0NrVu03RUm7MPVUBDfJ285Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🗞
🏴󠁧󠁢󠁥󠁮󠁧󠁿
ماتیاس‌یاسیله سرمربی الاهلی عربستان در آستانه هدایت نیوکاسل قرار دارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/102324" target="_blank">📅 12:08 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102323">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9305c345ee.mp4?token=twxvPDW9Qg2cy5iwv-u9QCNAgt1hcY-zyu5YkSdD7NKRuJAgyVn4yXyjVCkVwatX2D4y-5w4QRueWKcW33QEheFewmcjd1wV4QXy4tFkMOBCspY1fM6ZCpdOQh6SNCvf3egLmE7cXX6r1rf3tn3WhM1KZSKt35plBIa_wE8eMzbOSqylK789j_MYWk3BoRi7frqZiW172bMstWVbwkeY_kK_XojibBVKv1-xD18yDkjutgS3acRjA24K_U3o8tlh9a1SP6uXJAj97vuNyWqnT1XGfe8BD8a55N_m0aOK3vC3Wnga9scyUOl4FcDkEeNLRiDU9RL7yEdX4gknJ02rwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9305c345ee.mp4?token=twxvPDW9Qg2cy5iwv-u9QCNAgt1hcY-zyu5YkSdD7NKRuJAgyVn4yXyjVCkVwatX2D4y-5w4QRueWKcW33QEheFewmcjd1wV4QXy4tFkMOBCspY1fM6ZCpdOQh6SNCvf3egLmE7cXX6r1rf3tn3WhM1KZSKt35plBIa_wE8eMzbOSqylK789j_MYWk3BoRi7frqZiW172bMstWVbwkeY_kK_XojibBVKv1-xD18yDkjutgS3acRjA24K_U3o8tlh9a1SP6uXJAj97vuNyWqnT1XGfe8BD8a55N_m0aOK3vC3Wnga9scyUOl4FcDkEeNLRiDU9RL7yEdX4gknJ02rwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
🇧🇷
فالکائو برزیلی بهترین فوتسالیست تاریخ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/102323" target="_blank">📅 12:03 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102322">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc1c528fcb.mp4?token=mqJrj1lfPzt1Gs3o74K4IxW3hCmb7m2kuHUfksP74nviJ-6WNheki4Xeh45Rp35Ktvk7xT-70mSbbV62mormAQmgJ5BBCYBTJxBP046wLdznHHT3fJg065bpClsEml15GHpaJ89fjI40XEfz9_lN47HqalMPJ1zvbgdK8kxwgd9UlZkD4i6xewfjZSYkD0mN6xzmogkOtDkD6E_0x1KbyxfU2NsYw3k8HSTQ1Xn4ZY3wJwfVXT8-mvn78UimgwvhLY9WHOmOiUuKDJil4ZMtnhaGCiO-PR9iFHrVACVbQjd_HwclyB0eK_sDRwSrkAuxVMv3DzkeLR5jelKFCk01EA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc1c528fcb.mp4?token=mqJrj1lfPzt1Gs3o74K4IxW3hCmb7m2kuHUfksP74nviJ-6WNheki4Xeh45Rp35Ktvk7xT-70mSbbV62mormAQmgJ5BBCYBTJxBP046wLdznHHT3fJg065bpClsEml15GHpaJ89fjI40XEfz9_lN47HqalMPJ1zvbgdK8kxwgd9UlZkD4i6xewfjZSYkD0mN6xzmogkOtDkD6E_0x1KbyxfU2NsYw3k8HSTQ1Xn4ZY3wJwfVXT8-mvn78UimgwvhLY9WHOmOiUuKDJil4ZMtnhaGCiO-PR9iFHrVACVbQjd_HwclyB0eK_sDRwSrkAuxVMv3DzkeLR5jelKFCk01EA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
❌
الکساندر پاتو؛ ستاره‌ای که قدر خودشو ندونست و خیلی زود از فوتبال محو شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/102322" target="_blank">📅 11:40 · 08 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
