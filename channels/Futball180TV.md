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
<img src="https://cdn5.telesco.pe/file/gYXRjYA--e2f-iYQISvgNOt1GSi4kECofcLLbhuqh0lk06R26WokZuLVuZrLwJY2mbNTjHNkbifvFaCZYJUuwKiLVCxYmdcqruuHEkp68b1bYO8qJ8Z0uk6tHksQYPL3stfvHiVlFA3EuHKEsVd7PhAgeGBrhz5gf6YUJqFRnu7U8eyAJ3bDQKJrBryWBnxAv0ZkG1S22fU5JTKdb3WlUo3QR6pUgGLGeUUlJeGAvQRFUX9lBAuiz55hAjEJBmFaqoallDY-SZDXN70UMdsF2wHygizOcjHD4Ma5Ho8NH5dTyA-04mjt4ihwktRs4C_tNOYhUamkl8adf1xDuieLRA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 398K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-06 21:14:38</div>
<hr>

<div class="tg-post" id="msg-107445">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uysxGBWmO2YOjkEN8dWtoDaKaCCu79b5mZtj_xZvNhq2A89B-K6gzLjNLr1rQK-zgDXpNSgEvuau4ScKcc_R2XHXuepOGQ_HQQ-wLIiz5V_WbuPfQUchYYnfMraEqZkWHR6VaFFoyFmdlWyMClGm8g_4A9tTcqw27AJ8rWRLCTy8cnci6192GRoWUNC5U_2RVrqR_opAR26sCh9-ZrUBh7oQz684-odlFun2wHNlPADNnuen31_tNuOzs7g4SYpOGedPCRZbLIT_sC6dq7HCGUyFCiTR_i6nNaw6ZUpnOgffNuYDScdOlc2vKrB_fuY0KgpaUK7itHqzyGrpvQpEaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
یاسر‌آسانی تا دقایقی‌دیگر با حضور در برنامه عادل فردوسی‌پور با وی مصاحبه خواهد کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2 · <a href="https://t.me/Futball180TV/107445" target="_blank">📅 21:15 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107444">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0794b34067.mp4?token=g8TNE8jpKB1olfpxKvhL0QR6-IMoxCHDTUk04rSWVwpuRDaIybCjBdlKOG9j9T5sbFDxyfhQqqwQcGP4PPX17KLPAWsWJLvPlIEwA0BKNL8YHr3ZH6mWh2pE3OXXdzLHCMGNB9gvm7saZCU6uBvFBoh6pn6-a_kUIG5He6Xnp4u8v-hjrxfROcd28yDxty6fBGhcE3lnqXXyXgWQc3TBMTgzZsXcEjKBjPD4qXnTfZqSoD3Ed70AzGJ8kn_c7jNBPqf-7bm30-Dq-ronHKEd-PanD54DB_Gcs-Cksm40Yk7mBATG5i7vgvf1x9sKKeM4XBexO5wLyXZolAnuh41ygg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0794b34067.mp4?token=g8TNE8jpKB1olfpxKvhL0QR6-IMoxCHDTUk04rSWVwpuRDaIybCjBdlKOG9j9T5sbFDxyfhQqqwQcGP4PPX17KLPAWsWJLvPlIEwA0BKNL8YHr3ZH6mWh2pE3OXXdzLHCMGNB9gvm7saZCU6uBvFBoh6pn6-a_kUIG5He6Xnp4u8v-hjrxfROcd28yDxty6fBGhcE3lnqXXyXgWQc3TBMTgzZsXcEjKBjPD4qXnTfZqSoD3Ed70AzGJ8kn_c7jNBPqf-7bm30-Dq-ronHKEd-PanD54DB_Gcs-Cksm40Yk7mBATG5i7vgvf1x9sKKeM4XBexO5wLyXZolAnuh41ygg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
🇺🇸
مطابق گزارش خبرنگار شبکه الحدث در پاکستان، به گفته منابع، ایران با توقف فعالیت‌های غنی‌سازی موافقت کرده است، در ازای آن، تحریم‌های ایالات متحده علیه ایران کاهش خواهد یافت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.84K · <a href="https://t.me/Futball180TV/107444" target="_blank">📅 21:11 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107442">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/l9S3wMbJKYz5MC5h6dS7KJxXqASR9WGLfHC-JwG2Md0GuQudakfdYOon1iiszNdnTrIAWEKM4n2Lr9jScvZzE8nCTxD7aAelJsLqg2sFRilDXRMRtzjDBOAur6SN7nNYZ8uZA7LUwyp6gPfOSmd6buoo_NV6Jy-jZ7Buyxom35VEkUlBKJfds7qnmrDiTpMXsp3cmeghkAt2Z8dogrs5JfnqLdASc4fAQkqxUDgw-CntlU3-R76IVuIGZ0gNVk2gb7H0SUeua5hJl8sE0RlZkBJOO7rJbIaKupg7kHmxPLijUPkV87XScKJ_dGUWIoAobAVXaWsvbtbXO6ivFzqBBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tkjgRNs3vS2mFs27G-spAANYaZzTgMvfhbi2L8CxBKhcCHUM4JHnRhpAQ9gGjy2m-JRZjYqwTesZO40tGI_NydctK5t6AQ76b24wuJTDLfW-pJKRFMZQD3AKCHEqhuOrV2kQa2EzmjrJf1Ck6rIXxZBZOswGZGZeEoFDc3QIkZBoMOtgygl_I8MqjGxbulHqMzFBQfxiTsN41aSxET2kwTFZTJWnxhyncNbXs7w3q9fxAhk8TV2jo-qUd2xJP_4GSQiqKsdA0HtUAINkXpz4tgmWSBG1dbjaaHMJvUzcE5iJwiuKrwJ-0VPAGohvyQuR7jCsvrGFWU50tiz1SmmFOw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇫🇷
🇧🇪
ترکیب‌تیم‌های بلژیک x فرانسه
ساعت 22:15
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.72K · <a href="https://t.me/Futball180TV/107442" target="_blank">📅 21:10 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107441">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">❌
🇮🇷
🇮🇷
على تاجرنيا : از هواداران پرسپولیس گله دارم و ناراحتم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/Futball180TV/107441" target="_blank">📅 20:32 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107440">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ebd0094f85.mp4?token=cZuPx_BopdTmjW0PzZ4Ms4EKxD4p89mx8iYcLOXnr36r91fOWRtv6bxCJNGXYqtBs48qSECtWeqOno8O_Nl1U5tlniCIfietHjb_ow7Ge2lwyDGnYzsGmi5_rn02s8kPhoEKCAz8jquyYaJ7nvSQv7loKt3wBhccWz4afGyRSDAt7to8q8H8cvuKbVOkCi24Gq69jdiJH76K-XVdYNO5LWOAAn-w4tVOzPN2J0e9ubS1jziIwq9xVUZMJAOBulBgTEdEtvXlIBMUSDhS5bZCFg3fuOQ2yPdWMCAgBqt59reFl0-Q3z9sWTGkGMfXEA9ckVCb59qvf2u8UBRkTsKCKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ebd0094f85.mp4?token=cZuPx_BopdTmjW0PzZ4Ms4EKxD4p89mx8iYcLOXnr36r91fOWRtv6bxCJNGXYqtBs48qSECtWeqOno8O_Nl1U5tlniCIfietHjb_ow7Ge2lwyDGnYzsGmi5_rn02s8kPhoEKCAz8jquyYaJ7nvSQv7loKt3wBhccWz4afGyRSDAt7to8q8H8cvuKbVOkCi24Gq69jdiJH76K-XVdYNO5LWOAAn-w4tVOzPN2J0e9ubS1jziIwq9xVUZMJAOBulBgTEdEtvXlIBMUSDhS5bZCFg3fuOQ2yPdWMCAgBqt59reFl0-Q3z9sWTGkGMfXEA9ckVCb59qvf2u8UBRkTsKCKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
🇮🇷
🇮🇷
کنایه مجری تلویزیون به زنوزی: باید از هواداران استقلال عذرخواهی کنید.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.06K · <a href="https://t.me/Futball180TV/107440" target="_blank">📅 20:02 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107439">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3dd102e93c.mp4?token=JE_nWkIp487ORsN8UnoWg1tuwaooHaVhAbT-fEBUh8dXJy3GuAMCQDwSVYKg3a7a1XW3c0hbPg4IkyQWEgS4kHtTpK3LyZ6b-wGAWlyhss1rXVAV_VC_42mJebpGjNKkFjCOxnZzY-4payRoQBjrOzaW-A9s2y8MT8c2G8mY_iN2DZ8NL3bzy4iG9wIu9JSWhCgliDRzr6e6RzDx8wTAyA5ugfO2Er16AlmwkHYtZI76SecgOZlhF4xZ71kcTO_namHPodsCpueafxKkkzu7FKpFAlPVe3S07uOxGCxosuYMG4uzyhgD7yhroFbuJkA27GJzj93zgHT8boV31NUL4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3dd102e93c.mp4?token=JE_nWkIp487ORsN8UnoWg1tuwaooHaVhAbT-fEBUh8dXJy3GuAMCQDwSVYKg3a7a1XW3c0hbPg4IkyQWEgS4kHtTpK3LyZ6b-wGAWlyhss1rXVAV_VC_42mJebpGjNKkFjCOxnZzY-4payRoQBjrOzaW-A9s2y8MT8c2G8mY_iN2DZ8NL3bzy4iG9wIu9JSWhCgliDRzr6e6RzDx8wTAyA5ugfO2Er16AlmwkHYtZI76SecgOZlhF4xZ71kcTO_namHPodsCpueafxKkkzu7FKpFAlPVe3S07uOxGCxosuYMG4uzyhgD7yhroFbuJkA27GJzj93zgHT8boV31NUL4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
📱
یامال دیوث اومده از عرق زیر بغل نیکو ویلیامز استوری گرفته و مسخرش میکنه
😂
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/Futball180TV/107439" target="_blank">📅 19:34 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107438">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cee7cdbb4e.mp4?token=LWJOqZ0vzKgx7Rna2mPXacRNVm5ZY3xohw2F0T9erk0T-m3XbXAgRaud6jdkwwrjj8Li0DVVGOfTD2rCBQ7bcgqqab0ugJplVZJDmanV9kWe9k-6Sz2ChB8Bvr7We95GUPqexggjZi0JLHHASjYTxJvgaqnHxY_GwXLe6bt4Sam7H3AtB8xloLBEdeO0mpx9ZX30TCHyfRLsvRyvlXMdzyBpbFr7PQQaF_9VPA6tgi5EZGsIHmlH9Krt1HuNmwbgZJXnzIUxNDqNJo9WzEhki7BVx5X9kUnL9n70FZj2I1wDOuRSbwt1LZwMUPQxt1oDEGhQ4duVHAciL3DPJbj_qA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cee7cdbb4e.mp4?token=LWJOqZ0vzKgx7Rna2mPXacRNVm5ZY3xohw2F0T9erk0T-m3XbXAgRaud6jdkwwrjj8Li0DVVGOfTD2rCBQ7bcgqqab0ugJplVZJDmanV9kWe9k-6Sz2ChB8Bvr7We95GUPqexggjZi0JLHHASjYTxJvgaqnHxY_GwXLe6bt4Sam7H3AtB8xloLBEdeO0mpx9ZX30TCHyfRLsvRyvlXMdzyBpbFr7PQQaF_9VPA6tgi5EZGsIHmlH9Krt1HuNmwbgZJXnzIUxNDqNJo9WzEhki7BVx5X9kUnL9n70FZj2I1wDOuRSbwt1LZwMUPQxt1oDEGhQ4duVHAciL3DPJbj_qA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚪️
🇮🇷
❌
فرزین دبیری عضو هیات رییسه فدراسیون فوتبال : علی تاجرنیا به اعضای هیات‌رییسه نامه زده که جام فصل گذشته به استقلال اهدا شود اما هنوز هیچ‌چیز قطعی نشده و هیچ کس هم به تاجرنیا قولی نداده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/Futball180TV/107438" target="_blank">📅 19:29 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107437">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vA3RfyQEIMreHFMmZLp9dSTAjJeP4OnXKqvWjvjjei2DqZWRgr27q3NxqM8m__qT3pI3bcpFIDjQyWuibns9OJJcDkz-goIE_9o_Mj3mVJAOj2IqvFTooRCfq_KJosjQTF8-0uBUF6u0E2zQ1zeThYKchS4DQ1gCeavVPEh9YtsEfL263ve5tV6uape0lHc0m0CDyRm63Ln0yX83MiH2a7Wc5mjI1PLFCtriJsJvuRlCAsCM4Njhr-EI53OGpN3bK5zeKskbV6IS_xU2774yVyDEupz74tEj5WlMF1YTImHofIwrXkiHgBSXnYJjYaxLsQEVe5QYhGcrEhd50y0cuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
افشین‌قطبی، پیروز قربانی و رسول خطیبی سه گزینه نهایی فدراسیون فوتبال برای سرمربیگری تیم‌ملی امید هستند که بزودی یک نفر معرفی خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/Futball180TV/107437" target="_blank">📅 19:23 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107436">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd0d622742.mp4?token=OZlsrlJj36L4pqWDsVt6YNLXkKGIGQEikFw1QeCPVx49lcm-H-3r7_mA7dk_c2So-_xqs6ajVZe2hwJ_llfUeE5lHFJ-81N74hnKcZ0LPFXKRxTYZdy5Gkd4Uqz5un2H4NIwO4fvqEBdzkj5X9xPWoQ4uJ-MLJ9zJd_ZVW2ZgZLDIOl-lXuJF2RcO1HejHxgYD_Lugc_Pz_n4YvU719KGoeH5LKsaiOcCo2RQN5oaNpn_IkKsPvomyKyjkYniT0hxUBbacqg8wF7tUG4VrYpecmfSVBMTLlE5U4Rh-kDpxzRm1w-GF2dPbbUblGbYA8WaRom1H5vtcHdhcKttKACy4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd0d622742.mp4?token=OZlsrlJj36L4pqWDsVt6YNLXkKGIGQEikFw1QeCPVx49lcm-H-3r7_mA7dk_c2So-_xqs6ajVZe2hwJ_llfUeE5lHFJ-81N74hnKcZ0LPFXKRxTYZdy5Gkd4Uqz5un2H4NIwO4fvqEBdzkj5X9xPWoQ4uJ-MLJ9zJd_ZVW2ZgZLDIOl-lXuJF2RcO1HejHxgYD_Lugc_Pz_n4YvU719KGoeH5LKsaiOcCo2RQN5oaNpn_IkKsPvomyKyjkYniT0hxUBbacqg8wF7tUG4VrYpecmfSVBMTLlE5U4Rh-kDpxzRm1w-GF2dPbbUblGbYA8WaRom1H5vtcHdhcKttKACy4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
👍
ویدیو‌دیدنی از حرکات بانوی ژیمناستیک ایران در بازی‌های آسیایی که حسابی وایرال شده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/Futball180TV/107436" target="_blank">📅 19:01 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107435">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YbDrOwZESMq39SV2O6_Ed3LMJi-N6OuvkAF-gmPfrTViXcnnVZ4bdhHHwuOSvtLLWENsfG4r96Vvn9VLAuR1J7Rgd4ciLP-UbkPwrQV0JkqxRHbJngvVOKK4u7xGkTV4RdBCMerPnBTQuOzkoZS2TAEYbRPgHtYXV4WXrcjS-Y2C8xOaQEsNrwMJAyuL8RBAGGHrA75L0QSjfN9aQDSii9n3zmmgLzyIRzqMxZo1TcyUEt-nh_6xEYbKWd74lakf3O2ckWNLgI19SjvUXpBmUaPnZVElvKf48NYqeYvOYwhhUbXb8RC-vvEtvZ2yxWV0EBvznDM45YYbbXIKPnBRLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇮🇷
دوایت باکس، گارد باتجربه آمریکایی، با تیم بسکتبال استقلال پیوست. این بازیکن آمریکای سابقه حضور در NBA تورنتو رپتورز، لس‌آنجلس لیکرز و دیترویت پیستونز را دارد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/Futball180TV/107435" target="_blank">📅 18:50 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107434">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3874fb3e78.mp4?token=dFZYQC62xKm1cn04kZ7fn3l6eTMCnAWYOhou9XxSzJekmmtI3Z4jOsKpR_pLvD9_2inawRB3pBBOQgoZtj4FnH2nmbD0iKzLF5QDEKGQ7XoskNrQ2E-WyAtLFsUI_cdwHkCobncUQPxL9kipdYIOdFqBewDu9KClmdwkgN-B-lebg82IMdosLMJutJU_EPZTIx1iRJx3AUpj6OfgqfxmSWLeJaxyF6ggeOUWtBrqdKfh_6z7J60HGvSVCCtpdr70jnsCD9m4A5rwjrkiLaSBPs37XRJm9j45T-llmfp6CKAHoQZvCgUP-VafIJwVHb78lRixLqQwHYCFTfsbpT2VoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3874fb3e78.mp4?token=dFZYQC62xKm1cn04kZ7fn3l6eTMCnAWYOhou9XxSzJekmmtI3Z4jOsKpR_pLvD9_2inawRB3pBBOQgoZtj4FnH2nmbD0iKzLF5QDEKGQ7XoskNrQ2E-WyAtLFsUI_cdwHkCobncUQPxL9kipdYIOdFqBewDu9KClmdwkgN-B-lebg82IMdosLMJutJU_EPZTIx1iRJx3AUpj6OfgqfxmSWLeJaxyF6ggeOUWtBrqdKfh_6z7J60HGvSVCCtpdr70jnsCD9m4A5rwjrkiLaSBPs37XRJm9j45T-llmfp6CKAHoQZvCgUP-VafIJwVHb78lRixLqQwHYCFTfsbpT2VoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
🇮🇷
تاجرنيا: خیلی ها من را سرزنش کردن که چرا موضع علیه سه جانبه نگرفتیم اما در نهایت دیدید که چه افتضاحی برایشان رقم خورد
!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/107434" target="_blank">📅 18:30 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107433">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UFmuXMEjICNeXVrIoxPRjduWboE35hNMVKwxh90GX9PAKpBtMjirnNWAAfViqSqUhiUwn8cg5EsNS2o1h-DheuRGjxWLwwcGwV7flLeaSlFEEFonAeaARcW-eXXK1wqSQxxdZEL2hi23huWO1ujxidhO8dzDOsKbjVKipRjYXvRZYdodMWPZD_8kP1vPFppvURrzfU-IvcVzHwHhb915HqJ6ECRPRZTdBqT8JqzixfMKaxA8BrIXteCvZLssrJY4jUd4SyYEfEUJolg1umyg-SAoBeWGQRTT6W-vZMtW0I2lowWeNkgKOxLYNUyMYVQPoH_5TVdCE295UmcbugZHhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🇪🇸
عملکرد اسپانیا در ۵ بازی اخیر خودش
🔥
🇵🇹
برتری مقابل پرتغال —  رنکینگ 7 فیفا
🇧🇪
برتری مقابل بلژیک —  رنکینگ 8 فیفا
🇫🇷
برتری مقابل فرانسه — رنکینگ 3 فیفا
🇦🇷
برتری مقابل آرژانتین—  رنکینگ 2 فیفا
🏴󠁧󠁢󠁥󠁮󠁧󠁿
برتری مقابل انگلیس —  رنکینگ 4 فیفا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/Futball180TV/107433" target="_blank">📅 17:53 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107432">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/107432" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/Futball180TV/107432" target="_blank">📅 17:52 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107431">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RMGX00fs3ZcZyVbHZfFx51_JCdy4ql8aN6WTpA8Qxm4ipf1e9awX__p7Hrqucw-oDW3f5LlILhx5XBKoOx1K34UjDKF8Flw0yo3cTKplTOZRfR95O0fJw6dTb2XEaNQQvcURurXvFwgQfuYOPVdUke-52sheMbWiBwQgRmbUe9yYHjDIkZl0TDLsOxDWw_Lbteq_m89oDzjqjf14i6taVLcFER0HiG3-XMNBmZI47SDtK2Lk3nsx548Vmj-4yOaC6fSiMMY8WW925qF3qT7ZvafPMf51xvmhw5ds8zL07Vj40H9aWxu6nKCmnCcf-NESu2iUr8HJuWNVxrxNtzun4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
فقط یک بازی از میکس‌ت لوز شده؟
پولت برمی‌گرده!
میکس می‌بندی، هیجان بالا میره، اما یکی از انتخاب‌هات خراب می‌شه؟
با پیشنهاد ویژه
TrexBet
، در صورت رعایت شرایط، می‌تونی
۱۰۰٪ مبلغ شرطت رو پس بگیری
.
همین الان وارد سایت شو و شرایط آسان‌ش رو مطالعه کن!
💰
🦖
🦖
🦖
🦖
🦖
بونوس صدرصدی اولین واریز
🦖
واریز آسان، برداشت سریع
🦖
سرعت بالا، طراحی حرفه ای و تجربه ای متفاوت
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/Futball180TV/107431" target="_blank">📅 17:52 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107430">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/387378bb2a.mp4?token=vHI9hmW59n8osWbYd1bj7C2xTS58vm73ITN591f0g62XpMe_ReryOJgeRW18qm3jNFiTOCaut5P6RhZZ5fPGi-ORmPzN5TSzz--7AEj2oFiNZi_EYKvKgmyH76kVzI-1OipYn0hFnBAqC_rCNMDfkggLx6O_Sb4K_jhw14i3F4Bknq_bTQc0Ppg_2s0XQgrQ_JBadMz9zVQ9lLTGEbyBBLuwL8i9Iiht5DMZVsqhWO3dvbGPWB_Z_n27OJDETggh3_4jZxt_43tubTlgIKIUMpHGhYXBewXgrLuL5vp_LZT_DN6MqtEAzRtWaHEIO4ScEgK82rr91NIc1mEalblP6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/387378bb2a.mp4?token=vHI9hmW59n8osWbYd1bj7C2xTS58vm73ITN591f0g62XpMe_ReryOJgeRW18qm3jNFiTOCaut5P6RhZZ5fPGi-ORmPzN5TSzz--7AEj2oFiNZi_EYKvKgmyH76kVzI-1OipYn0hFnBAqC_rCNMDfkggLx6O_Sb4K_jhw14i3F4Bknq_bTQc0Ppg_2s0XQgrQ_JBadMz9zVQ9lLTGEbyBBLuwL8i9Iiht5DMZVsqhWO3dvbGPWB_Z_n27OJDETggh3_4jZxt_43tubTlgIKIUMpHGhYXBewXgrLuL5vp_LZT_DN6MqtEAzRtWaHEIO4ScEgK82rr91NIc1mEalblP6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیروزی پرتغال در خانه ی نروژ، در شب نیمکت نشینی رونالدو.
👀
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/Futball180TV/107430" target="_blank">📅 17:45 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107429">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vaMLohSfMu0yw65KmImTvdTzrkyECQMeSfkLJ9OUOvyRU4b1QZrk-F3jC2mIAkfZKDYHvtgP5DkGEcbE1-xk_2yol9sLuYUWpBrVLWxglIbgULTsbv24TVsv36ZWa4ueh8LEuWbFdZB41QRs5z1UjYd3_M2Q9iU4PRmOscfyhrLXxfTeLpzFRInSorc_4aaCeBmgoZO_EkTz58i00in2aphw2388ftfbeWLzIQGHTZWdqZeTBNYBFiPhcSDtjb33H8CH1GKXikW0h-WJAmuVfLpGc0WwFbBq6z9SBWQnBru-uLW3mESLtAwLSxZlCI3PL9QcglUvj4m22BWjaj0Cmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
عکس فوق العاده زیبا از برج میلاد و ماه که دیشب گرفته شده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/Futball180TV/107429" target="_blank">📅 17:29 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107428">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/302c2a5126.mp4?token=ZOblQiYI21VFD_TlFhstm0OHDqf2X-gyPluT_GK1_PSJtiJ4a6KwTD03AQLj4UNabxmg5NjdMhE6k59tGXgXr8AsGjbANej9pPX_35WACKxQT9tpFuaGfiqX7wIKf66abLLTl11k4_EpjVwQkSK5grMoQ8jhIslGoWOilJ-yx8wbLtCYS45D0wTVIABH7YsoojofBzALNJZa45fOluC6-NxDVKS6iUZBxYo1lvKELZhLHYmaxWJOQaUOc0QyuIHJK8LLSPUSC-AdZhsnAUZwn_x7z_kTHHvRWgv69cZn_2346Q9aUp5HruhHMmw9W4lyK2shg5ZjdPDFIGXn3jzKWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/302c2a5126.mp4?token=ZOblQiYI21VFD_TlFhstm0OHDqf2X-gyPluT_GK1_PSJtiJ4a6KwTD03AQLj4UNabxmg5NjdMhE6k59tGXgXr8AsGjbANej9pPX_35WACKxQT9tpFuaGfiqX7wIKf66abLLTl11k4_EpjVwQkSK5grMoQ8jhIslGoWOilJ-yx8wbLtCYS45D0wTVIABH7YsoojofBzALNJZa45fOluC6-NxDVKS6iUZBxYo1lvKELZhLHYmaxWJOQaUOc0QyuIHJK8LLSPUSC-AdZhsnAUZwn_x7z_kTHHvRWgv69cZn_2346Q9aUp5HruhHMmw9W4lyK2shg5ZjdPDFIGXn3jzKWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دکتر بیرانوند روز اول خدمت
😆
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/Futball180TV/107428" target="_blank">📅 17:20 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107427">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">📊
🇳🇱
🇩🇪
آنالیز تاکتیک جذاب ژاوی در دیدار اخیر خود مقابل آلمان یورگن‌کلوپ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/Futball180TV/107427" target="_blank">📅 16:55 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107426">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a6242b00b.mp4?token=qU7rVuS-K4OYaHyMiT4yjtlWfEMCmwEiwK8UsET9JLrxrHq3kUzxO5BOyDUBSvo1aI5bKsWjTe0bW0iAGmTXLa0x3h9y9ZwjpmCUdUkFydfWTUgXIurR-Na7-d4dmC6tr96Io9JAZxuQ5Lu3BEuDnRKv2-qhDe21LgR6Anrp3zNCmBjkGaFpBVOE1UDOcwjeppocjjzhHDL0aWvXeeXE12Pi4uj2Rzz_J0C5MerCsaAZ00mJ9qZt-nsgPZl-s9L9vBtKYSBXWfiDR6Ek4m_fc_FvPyTas7AWUk6bmnywsoXVPv_gz-KJJaDyQwSrPtDI9EoLjwgQpda1wpSrm6tOrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a6242b00b.mp4?token=qU7rVuS-K4OYaHyMiT4yjtlWfEMCmwEiwK8UsET9JLrxrHq3kUzxO5BOyDUBSvo1aI5bKsWjTe0bW0iAGmTXLa0x3h9y9ZwjpmCUdUkFydfWTUgXIurR-Na7-d4dmC6tr96Io9JAZxuQ5Lu3BEuDnRKv2-qhDe21LgR6Anrp3zNCmBjkGaFpBVOE1UDOcwjeppocjjzhHDL0aWvXeeXE12Pi4uj2Rzz_J0C5MerCsaAZ00mJ9qZt-nsgPZl-s9L9vBtKYSBXWfiDR6Ek4m_fc_FvPyTas7AWUk6bmnywsoXVPv_gz-KJJaDyQwSrPtDI9EoLjwgQpda1wpSrm6tOrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
مهدی‌مهدوی‌کیا: عدد فوتبال ایران پول خرده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/Futball180TV/107426" target="_blank">📅 16:33 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107425">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63162a7ef0.mp4?token=MloN4xR6vAiA5yo67h2V6iL0hSpwTs0hSLdawPdO-pc_xubpmxOP5yTSrlLBQAMlYoYlsRjEjEKVtTGJNq9TbN5fUL2ZqVf5G7i2_GJALgP5aCL0JiFpxZ4DsowYke7XWj44tBHVReq-WKfHPIO0Bm8SWm-Aud8ZJCImfJT44mMozneh4W81MmjjmoTxjAhwMECc2cUkV8VEuUrAtAA79XL_AyHVJqtC5o_vtLiG6evPMP0iX7uclOdnU3-V57JcfvKKFCmxwYQg2mBjVSu5J8T-Id_NihutQAeHeTB8kVnPIFk7c1WkUlHs4Y9kIwZBKxHdlSnfQfwuStyak8f_SA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63162a7ef0.mp4?token=MloN4xR6vAiA5yo67h2V6iL0hSpwTs0hSLdawPdO-pc_xubpmxOP5yTSrlLBQAMlYoYlsRjEjEKVtTGJNq9TbN5fUL2ZqVf5G7i2_GJALgP5aCL0JiFpxZ4DsowYke7XWj44tBHVReq-WKfHPIO0Bm8SWm-Aud8ZJCImfJT44mMozneh4W81MmjjmoTxjAhwMECc2cUkV8VEuUrAtAA79XL_AyHVJqtC5o_vtLiG6evPMP0iX7uclOdnU3-V57JcfvKKFCmxwYQg2mBjVSu5J8T-Id_NihutQAeHeTB8kVnPIFk7c1WkUlHs4Y9kIwZBKxHdlSnfQfwuStyak8f_SA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇪
نحوه برخورد بازیکنان ایرلند با اسرائیل در بازی دیشب که حسابی جنجالی شده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/107425" target="_blank">📅 16:05 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107424">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e6d3f57825.mp4?token=MBf3vMTJpcsCnR4tSigjZQPTkOMdLVb9_pDNUnE8bzFJ3PvrASGDQakLFCnL_Krg6ng-klL1Ei8rz226j1FTNmIvgB6exseU7PXINIHn3TMLh3JCjXRpD2p_WL-wATWDFpEYr_SSWTqe8z04RLpfDHyr19Rm9DDjxa715x7A3ST42NH-tXBS4fl86JpPcYHB7w-3W4L0vbM5JkprbbmpRvZIZaHUobr24p8ijnuwet7AHdZ3yM5N-hRi-9paxU9nEFneHPgwqmiV9fZZ-uXLQqXmgjWHjl_KmZnrbgIiQwSDNfCwONlcE97KjdM_f_xFVgb45ulV4NHcfhqq9z4neQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e6d3f57825.mp4?token=MBf3vMTJpcsCnR4tSigjZQPTkOMdLVb9_pDNUnE8bzFJ3PvrASGDQakLFCnL_Krg6ng-klL1Ei8rz226j1FTNmIvgB6exseU7PXINIHn3TMLh3JCjXRpD2p_WL-wATWDFpEYr_SSWTqe8z04RLpfDHyr19Rm9DDjxa715x7A3ST42NH-tXBS4fl86JpPcYHB7w-3W4L0vbM5JkprbbmpRvZIZaHUobr24p8ijnuwet7AHdZ3yM5N-hRi-9paxU9nEFneHPgwqmiV9fZZ-uXLQqXmgjWHjl_KmZnrbgIiQwSDNfCwONlcE97KjdM_f_xFVgb45ulV4NHcfhqq9z4neQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیتِ ناراحت کننده ی سرخیو آگوئرو.
🙁
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/Futball180TV/107424" target="_blank">📅 15:40 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107423">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qUztCKqAIyFZ6pBjDi4LOl8ATfcpNLR1GGNp0trqy50-H5cFaR2eyy4ODK9fzlHYPHU16DCt0UD_Ub2f4uC7lQE5MfqMzGjpHqwN8bRHga-ldqwuUgu2hrkvcZ-CiZRl5j2tOJ9RqmzOAyM-WbP5_Vbn6EY8cnI8lqF55J1Vp7Q8Dw-0vc8sDzuS87Upeaqwis9SWOX9vpCA3VNnoga4j6nIag2Hy9DK2ypxLatJiLrxqm5vAn34cD02-mqrWsLeKbe9zjV3GZF10zAnap4Shw4zYRqT_TOF8OqEPOoYQ3rd55m4h8YdmJ9xILnbbNyAIxbvXdM9dX8Zq0HU2GwQ6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🤯
مقایسه آمار هالند و رونالدو تا ۲۶ سالگی!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/Futball180TV/107423" target="_blank">📅 15:15 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107422">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/42ff849b11.mp4?token=tvOGtE230pDK4yAC6a3niBxmL0V5jQmbWFcpxCqMXdNhUBILa03YOBFodszbKeCRG0sI5Y1wdswOqJwSDsZTmVq-b_tRpLwRKsi2VAQVGMOwNAAjW7yCC0VnAC68T_3R6CIgteQmfgeQNfHWfkD2BfgDB_RnsAeTSGTJO8pJDZovO9qub4dLhK4CsN18MQvrpcrpNq7e1BNb_h5rJQ2aJ1Ek2SLk-qyEJ8OdgZ1Q1ChaArRzCsxth9Yo-c8zWqJrUUtfIaHGBqIRtIqy65PQEkJ71Yna5Wa6RjITSFIqIwfuwV46Y2rx5yxJGEDuFGeIQxEUtTZkfXf5vlEX5_2mVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/42ff849b11.mp4?token=tvOGtE230pDK4yAC6a3niBxmL0V5jQmbWFcpxCqMXdNhUBILa03YOBFodszbKeCRG0sI5Y1wdswOqJwSDsZTmVq-b_tRpLwRKsi2VAQVGMOwNAAjW7yCC0VnAC68T_3R6CIgteQmfgeQNfHWfkD2BfgDB_RnsAeTSGTJO8pJDZovO9qub4dLhK4CsN18MQvrpcrpNq7e1BNb_h5rJQ2aJ1Ek2SLk-qyEJ8OdgZ1Q1ChaArRzCsxth9Yo-c8zWqJrUUtfIaHGBqIRtIqy65PQEkJ71Yna5Wa6RjITSFIqIwfuwV46Y2rx5yxJGEDuFGeIQxEUtTZkfXf5vlEX5_2mVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⭕️
بیژن مرتضوی به ایران بازگشت  بیژن مرتضوی، خواننده و آهنگساز، دو روز پیش وارد ایران و روز گذشته در منطقه نیاوران مستقر شده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/107422" target="_blank">📅 14:59 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107421">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1947c53917.mp4?token=ogGcROtN0zV7cvV1rtbYlAnbyUh7PDiMEoBetVw0Ev54U6m2Wz9R2Jli7VvNLA1eutio6wwWi0Gr6s5TGN_F9K3hRmvnJdxa2kRLH87wWFATfpnO5667TmOAv40QGnNecD90XetvFOwTdBXtUqUf_fTZcYT_AtKwACwZjH6Yo5XI6g6NT4mVe_GL2wOXfofiG3qIPREJWZ_4q6jc7ZCjOxxH98Hkb7XoN-iTumha2jUhz4jBr_AqT6gnTY8P1VlGRDkUELelNGezJin_l9eZ_DiBkaRx97WkkkivClGu-Je39grEHUkGDQbjCgeS8_5EJTUSWopt9V0A0wL5NTkKDLdBGohSVFmRvnOa4RiJdwXUNbvXq9sisLmT5SW6gI3vKSr8YI8gR8-434nA1Eg2fxchi6jrC9yNuNOI2ZQIa97xq8tIovDTZjS0L7YwYiM0uqC14Ga6VFA0fo2pkDo2b5bqtNii5lSSx7XAiDTT_q_bFGnsmh0nikUbIgkCeqAbGuFMdP38OoIKa0iVsMywA-C_Q9_0NmC1CfPp499-RAxhxe4sMCld5tfrJdj8uFpzJQmWhwwFJZroQ-scUpgV69Z6L8QIYYDpQrER9cYHjDm40thIjTSMQZXLazXRH2GUwat9Hl5RhB5J1hYmKN2NuzvSfcvBunrFpJd6gmKJupg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1947c53917.mp4?token=ogGcROtN0zV7cvV1rtbYlAnbyUh7PDiMEoBetVw0Ev54U6m2Wz9R2Jli7VvNLA1eutio6wwWi0Gr6s5TGN_F9K3hRmvnJdxa2kRLH87wWFATfpnO5667TmOAv40QGnNecD90XetvFOwTdBXtUqUf_fTZcYT_AtKwACwZjH6Yo5XI6g6NT4mVe_GL2wOXfofiG3qIPREJWZ_4q6jc7ZCjOxxH98Hkb7XoN-iTumha2jUhz4jBr_AqT6gnTY8P1VlGRDkUELelNGezJin_l9eZ_DiBkaRx97WkkkivClGu-Je39grEHUkGDQbjCgeS8_5EJTUSWopt9V0A0wL5NTkKDLdBGohSVFmRvnOa4RiJdwXUNbvXq9sisLmT5SW6gI3vKSr8YI8gR8-434nA1Eg2fxchi6jrC9yNuNOI2ZQIa97xq8tIovDTZjS0L7YwYiM0uqC14Ga6VFA0fo2pkDo2b5bqtNii5lSSx7XAiDTT_q_bFGnsmh0nikUbIgkCeqAbGuFMdP38OoIKa0iVsMywA-C_Q9_0NmC1CfPp499-RAxhxe4sMCld5tfrJdj8uFpzJQmWhwwFJZroQ-scUpgV69Z6L8QIYYDpQrER9cYHjDm40thIjTSMQZXLazXRH2GUwat9Hl5RhB5J1hYmKN2NuzvSfcvBunrFpJd6gmKJupg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
على تاجرنيا مدیرعامل استقلال: پاى حرفم هستم ؛ پول كاريله رو ميدم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/107421" target="_blank">📅 14:50 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107420">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bdc8f323f.mp4?token=dblWtPfLxDn5yKpaQMsH2NDfRWd_o84JYsKZ4MtAX1Ue3X_eqaCPaQ4XINhEauaRDBKeYyCWiw8qcEmrt0JxCS6Rsl1n52_2uQy62rvY0WJwNCUbskAxe8n5YFLm3ON9mk8r0vDvWAwSDpH3GCo8bbIO4MojK2TeicQhM9dW_eyfhutQtzuGG-6tIx50-2Tb-w6iS8xqnpxeHQM2hy_AYITdF5P7_NakiAiZgAFpBizXu3chhEprhtA6qjC9oRlsLfx-iengEaIdB4zETQS28-nPwDwU3Tj_zrL0cIAhwKaJMqXbw13WrcnIGf8ZnSpSB20Ys4b0hHUCygxl3MR5nw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bdc8f323f.mp4?token=dblWtPfLxDn5yKpaQMsH2NDfRWd_o84JYsKZ4MtAX1Ue3X_eqaCPaQ4XINhEauaRDBKeYyCWiw8qcEmrt0JxCS6Rsl1n52_2uQy62rvY0WJwNCUbskAxe8n5YFLm3ON9mk8r0vDvWAwSDpH3GCo8bbIO4MojK2TeicQhM9dW_eyfhutQtzuGG-6tIx50-2Tb-w6iS8xqnpxeHQM2hy_AYITdF5P7_NakiAiZgAFpBizXu3chhEprhtA6qjC9oRlsLfx-iengEaIdB4zETQS28-nPwDwU3Tj_zrL0cIAhwKaJMqXbw13WrcnIGf8ZnSpSB20Ys4b0hHUCygxl3MR5nw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقتی بیرانوند از خیابانی تو خدمت مرخصی میخواد
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/107420" target="_blank">📅 14:25 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107419">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39074d4c05.mp4?token=M5gftEjO25f3-fMLfyn65QzJnEEecN4-iruYJD_xIycaMOdI5Emv6p4BOLiLpUrOfDGhWtT4-Xxi-T9CBD4eLGoHtLqGhoWB43VOXk7o7RNsGATDbG0W56hTG7vASpaKjJ2ybw9lwVvRBJHg8uT0E-vjZ413L2wPpGcteun_4KmXGjX_a_dwenkhoP6Yiu4BgMOUHAmdUnrUcS2l1Y9AqFNhK83xnke5HDeUc-Khx11wkIXfUkOjU518qCV2qAqUTKDlyAmuuV45oECurVpKqoV4iS02T92AOjHscECHVXefnYj6998uMDtbC9TGaYJ8Yh6QCrqUQUcBymmyX9ZjYEJBf70nGoMQ0Kx6rstRxd4ghMrlcuXxhNi0ZGusavfUfP0yABIY4bYPq4YxH9ToHDITTUJtJuhZSm_tilMoVlsInonCX-pat2xfVnhiFQGO6s4582EjuXK3HSMgGzli5-lBZU1oeKs3LmgfeIuk7cDrdqxUc37AlauenWyoJS6SxoRH48ePt2ks2phaHfwAgR_kT1UYQ6tQWAMpuGV9trhpxPZ0p5F5ntQ0JRwiSxlhazXA49JmVNlHRu6cZa41mKqL-5JZ_3xPPWxuUVVLaZYk-acfsZjaVL2JkkEBz8izHOUt1p-Evkccq5kcJTVqHKxiEV4n2KcFEBU1QIRQYQ8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39074d4c05.mp4?token=M5gftEjO25f3-fMLfyn65QzJnEEecN4-iruYJD_xIycaMOdI5Emv6p4BOLiLpUrOfDGhWtT4-Xxi-T9CBD4eLGoHtLqGhoWB43VOXk7o7RNsGATDbG0W56hTG7vASpaKjJ2ybw9lwVvRBJHg8uT0E-vjZ413L2wPpGcteun_4KmXGjX_a_dwenkhoP6Yiu4BgMOUHAmdUnrUcS2l1Y9AqFNhK83xnke5HDeUc-Khx11wkIXfUkOjU518qCV2qAqUTKDlyAmuuV45oECurVpKqoV4iS02T92AOjHscECHVXefnYj6998uMDtbC9TGaYJ8Yh6QCrqUQUcBymmyX9ZjYEJBf70nGoMQ0Kx6rstRxd4ghMrlcuXxhNi0ZGusavfUfP0yABIY4bYPq4YxH9ToHDITTUJtJuhZSm_tilMoVlsInonCX-pat2xfVnhiFQGO6s4582EjuXK3HSMgGzli5-lBZU1oeKs3LmgfeIuk7cDrdqxUc37AlauenWyoJS6SxoRH48ePt2ks2phaHfwAgR_kT1UYQ6tQWAMpuGV9trhpxPZ0p5F5ntQ0JRwiSxlhazXA49JmVNlHRu6cZa41mKqL-5JZ_3xPPWxuUVVLaZYk-acfsZjaVL2JkkEBz8izHOUt1p-Evkccq5kcJTVqHKxiEV4n2KcFEBU1QIRQYQ8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
🔺
آنخل دی‌ماریا پس از به ثمر رساندن گلی شبیه گل مسی:⁣ قبل از بازی استرس داشتم و سعی می‌کردم با موبایلم خودم رو مشغول کنم و به بازی فکر نکنم که یهو گل ضربه آزاد مسب جلوی آمریکا روی صفحه گوشیم ظاهر شد. وقتی توی بازی صاحب کاشته شدیم، با خودم گفتم امتحان کنم؛ درسته من مسی نیستم، اما شاید جواب بده. و واقعاً جواب داد!⁣
🥇
روزاریو سنترال در فینال سوپرکوپا اینترنشنال آرژانتین با دبل دی‌ماریا ۳ بر ۱ استودیانتس رو برد و قهرمان شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/107419" target="_blank">📅 14:05 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107418">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb4774088c.mp4?token=A5ICiUTzwXdcWaQaHun6y4VMrZioRDQ7jkTi9OpnfTFcVkcQN9b9meoUjLIbNYmehlMNiA-6s-cJGom9sMl9qjj3yFYQ5i_e5-jtbWmSceSDKwLDWAWne4Wwl2PVvyA4iO4ai7SMOqoYJesUHhlPVLjJxsfnXWzI-5drlC7MuIA4jLrU_p59mq4NhQDChTDfEYE-uKDvlvs-Z7ZOE27K3j8OMozh62f_xnh1JphvG2uCeFTIJO1A7GrwmLF_6hKqs7Bn81ni_tcV6q1b-JZPABx0ayD4MSPu1K53wwdAYGxmQytmvMAQFFIZ-vo7p7jvHd0bpvVhofez_VCd6KHInA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb4774088c.mp4?token=A5ICiUTzwXdcWaQaHun6y4VMrZioRDQ7jkTi9OpnfTFcVkcQN9b9meoUjLIbNYmehlMNiA-6s-cJGom9sMl9qjj3yFYQ5i_e5-jtbWmSceSDKwLDWAWne4Wwl2PVvyA4iO4ai7SMOqoYJesUHhlPVLjJxsfnXWzI-5drlC7MuIA4jLrU_p59mq4NhQDChTDfEYE-uKDvlvs-Z7ZOE27K3j8OMozh62f_xnh1JphvG2uCeFTIJO1A7GrwmLF_6hKqs7Bn81ni_tcV6q1b-JZPABx0ayD4MSPu1K53wwdAYGxmQytmvMAQFFIZ-vo7p7jvHd0bpvVhofez_VCd6KHInA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🐐
سوپرگل دیشب لیونل‌مسی از نماهای مختلف
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/107418" target="_blank">📅 13:35 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107417">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2a5b80ac0.mp4?token=VCYUEWSdMC5H3s0y7mTVnoS4wQny3_5oCS7l0IqxKUMTNMLVn9uWYQKjKY1MqK2b42X-pmnm_QiTH80VsQaxvQB_Ef4cz3wJ7uQfih5rtBibkYW2YS_HG3lz_OHXeBkWYzr9my_hDTjQ8k7vX-LlmW_CGs2dXi8Qu_P8qQpeST7s7LriLMBRfp33osv9sA5mv6SDb-4crS1B3cnEV6vkecJBDrLwv3x-Y9qXEiGwelCxbnFqAfut-5Qnr4xvDzuiTGJprO6q4Q89nxY0njLK254QtsH-WJQrWDUwnBFEJnOmbxwsbubUVlgDahfeO5aYubGte8VPxI0MA0c6c2SM4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2a5b80ac0.mp4?token=VCYUEWSdMC5H3s0y7mTVnoS4wQny3_5oCS7l0IqxKUMTNMLVn9uWYQKjKY1MqK2b42X-pmnm_QiTH80VsQaxvQB_Ef4cz3wJ7uQfih5rtBibkYW2YS_HG3lz_OHXeBkWYzr9my_hDTjQ8k7vX-LlmW_CGs2dXi8Qu_P8qQpeST7s7LriLMBRfp33osv9sA5mv6SDb-4crS1B3cnEV6vkecJBDrLwv3x-Y9qXEiGwelCxbnFqAfut-5Qnr4xvDzuiTGJprO6q4Q89nxY0njLK254QtsH-WJQrWDUwnBFEJnOmbxwsbubUVlgDahfeO5aYubGte8VPxI0MA0c6c2SM4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇪🇸
ویدویی از درگیری بلینگهام و کوکوریا دو بازیکن رئال در بازی اخیر اسپانیا و انگلیس!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/107417" target="_blank">📅 13:12 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107415">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55f2619929.mp4?token=ntfZY7soYID_oIQD-vR7vgvPsBYjoDgchg3ZSBI3PjNJ5D18OhOZy-g7MGV144a9ky_wH-A_J3-jRem8NMuZ-s0WVQv4G3Op3tGZy7E13AaAOEQFOrwqWbHhaV-v6RCif78btg3mfvcTu3xORtQFiTEICrE2N1o2Kx0ogD99pk866mSOLNXOGix2a4jZOya52DCD5ryFuZ_lqf84tv91VDhKf24xJK7h1pZdfrNvf3CFPNBl2CGdB_ug1j8LmJi3SLgrUjZhb4WiwaY16QmPYQ7IvIefKA_PCzNkxdgFczBopn9Kw1GFGC88TkYCB3qimxC9V1qdGUPXWcgnMWcKkaCllYrQ6aMVPOeSpPG8dw9Kat-1qo5xAWmqQ-2xU72VPY3Pc9ULpXQp9r9FZtQsGeIKsA764z3m-F2CY6_8xzLj6nWQ0O-GvZ3u1J3Wn_GWl-ORdj4NthGuL64O5K0xXeQ6kXKX-TJcMATFDO4OG0kCfCeNZaULX3VTxK_QHM8b00_5Q1JxfK60JLLSgKTGgp8MVYReMll_BXPQuNsq3ubx3VLYYh-vGEfY_tuzL5qJ152BXiEiicpftpdUAS35PybB_eSxSt2avUfYoUYsmBpQk-TtKifvv8PKQYBCN7ssmvX3YqrNgDi00IVQwApyw--8-hFGvVA1PJZd_H3BaZY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55f2619929.mp4?token=ntfZY7soYID_oIQD-vR7vgvPsBYjoDgchg3ZSBI3PjNJ5D18OhOZy-g7MGV144a9ky_wH-A_J3-jRem8NMuZ-s0WVQv4G3Op3tGZy7E13AaAOEQFOrwqWbHhaV-v6RCif78btg3mfvcTu3xORtQFiTEICrE2N1o2Kx0ogD99pk866mSOLNXOGix2a4jZOya52DCD5ryFuZ_lqf84tv91VDhKf24xJK7h1pZdfrNvf3CFPNBl2CGdB_ug1j8LmJi3SLgrUjZhb4WiwaY16QmPYQ7IvIefKA_PCzNkxdgFczBopn9Kw1GFGC88TkYCB3qimxC9V1qdGUPXWcgnMWcKkaCllYrQ6aMVPOeSpPG8dw9Kat-1qo5xAWmqQ-2xU72VPY3Pc9ULpXQp9r9FZtQsGeIKsA764z3m-F2CY6_8xzLj6nWQ0O-GvZ3u1J3Wn_GWl-ORdj4NthGuL64O5K0xXeQ6kXKX-TJcMATFDO4OG0kCfCeNZaULX3VTxK_QHM8b00_5Q1JxfK60JLLSgKTGgp8MVYReMll_BXPQuNsq3ubx3VLYYh-vGEfY_tuzL5qJ152BXiEiicpftpdUAS35PybB_eSxSt2avUfYoUYsmBpQk-TtKifvv8PKQYBCN7ssmvX3YqrNgDi00IVQwApyw--8-hFGvVA1PJZd_H3BaZY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🇮🇷
🇮🇷
على تاجرنيا:صحبت های بازگشا مدیر پرسپولیس سخیف است و در شان من نیست جواب او را بدهم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/107415" target="_blank">📅 12:50 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107414">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/107414" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/Futball180TV/107414" target="_blank">📅 12:50 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107413">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ifxups_JdCNM1qwdWccrm6P-uD2CnGMSWaFQhekmyE2EH2FKEq8LPXksFBsJTR-yDtrDSdHSG7YFeT71Euty9eNIW6MJoGTowQDI0DarzHWD-EsEaVxOZx1OchONzVaGe47CKjXvbk5VZ4dtt30St1yJ2FP225OlnROkLull8midtfl7rdzWF22pA5aHXzJfiksG80sMCL13qWo9iDEp311d6krlpqVMrPfb1yx3w48UYmyxyaL_dUdn_ozllEHDPZXScQRPdRjzvTAqGcJEfkGGHtlACoIk5RyjNEGTavyb3G3uBfEhwYujszx_BxDrNl6ir5vEpHp70mlQYY55hA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
نبرد هیجان انگیز
فرانسه
🆚
بلژیک
را در
TrexBet
پیش بینی کنید!
📉
نگاهی به آمار ۵ بازی اخیر دو تیم:
فرانسه: ۳ برد، ۲ تساوی و ۸ گل زده
بلژیک: ۴ برد، ۱ شکست و ۱۵ کل زده
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
🦖
هیجان بازی، وقتی بیشتره که انتخابت حساب‌شده باشه!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/107413" target="_blank">📅 12:50 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107412">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SVztY7hVfrKa6QC1YVdBxtS3jivW6Bq26ClYhR-33EeLGZLvc8d_uf7XyVqY6YC2vU1Wj8Sg8wzMMKZVWTOZb-nw_iz2oHaQByiIXLHvuOxG2cjilyexF8-i7kWA2pnAvN_gx3iozsMXhAsgJZaUeOZcZhJo-2QLqTs4GDQIhQn-ZBfDWXmx_kcwzQ6ldvB8baq3q9kOIQB-pQAQZQ5-D5yb6z1fjLqwDfxM3qH7jmWXTSRMxFgPNpLCkXs37qOu4XCXQ1qnB8sr7-_jHj16Zl3A65HXqOEgf47Xv8lHspQtuete1ZsDP_jGJajjqh2ZFvX541N2u4KSHeDhqsU24A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🌍
آپدیت رنکینگ فیفا پس از بازی‌های اخیر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/Futball180TV/107412" target="_blank">📅 12:41 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107411">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2bfc79cd9.mp4?token=cMC86RhMq4Dal-KN10t-1p7MKhnvDfZrxu5eFvBHtOFod9GI6Ky1QyxZTMJbDcxgt0zVN-jJyT6_xo1ZOfu6afnmidrYz6ycyH6q04mSWjtf3DQma03cFWWXLt1965yzbpIchOduOL2kwpqw6gBUEegOZksCnlqglGxxk1VA4-ZkcZAEEHdqLoWHyXIBJ14kAnJ47RlD3I8bYiuSUbMzLvGWhgAThwIZypNkQjqc0JxqirGukIKJh17rfSot7kNs8Sbb0yWvOBAL2w_xf0YofjpdVPaaQQB8-nXE7nJOZlYO8pvH3k9vx41mVyqhPrykM6cd4TOvVrKYQtcmCeZp1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2bfc79cd9.mp4?token=cMC86RhMq4Dal-KN10t-1p7MKhnvDfZrxu5eFvBHtOFod9GI6Ky1QyxZTMJbDcxgt0zVN-jJyT6_xo1ZOfu6afnmidrYz6ycyH6q04mSWjtf3DQma03cFWWXLt1965yzbpIchOduOL2kwpqw6gBUEegOZksCnlqglGxxk1VA4-ZkcZAEEHdqLoWHyXIBJ14kAnJ47RlD3I8bYiuSUbMzLvGWhgAThwIZypNkQjqc0JxqirGukIKJh17rfSot7kNs8Sbb0yWvOBAL2w_xf0YofjpdVPaaQQB8-nXE7nJOZlYO8pvH3k9vx41mVyqhPrykM6cd4TOvVrKYQtcmCeZp1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقتی پرویز برومند در جوانی ادای جلال طالبی رو در میاورد؛ عجب تقلید سمی بود
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/107411" target="_blank">📅 12:20 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107409">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RlBZLuJ33Nyc7o-BnNiRCBMXynB_6XcOFGsjwAG55bCJA0MEsdoiWX33qL_xiVJOO1P6Yg9VC9jvmIAUmlsiDTXIPqjcjkGRnGeP-WBE9IcgYlIwFgl6OCub20z94ehvN8lgddwWTfS7SKgANMR4CcmFQrDf5ga1RveqDMAV1itE6u6EJ1nts6ifxEGLVflKWkGxCFh12BTOFR3fXhyIml8BCmRnHz2BsNvmcUDlQ-cbYU8zxK-AT4L-5E0hC0yQZfHdfygVFCWAIM3Li_WvUnPStBQ9b1OXXNwozhhQWBoUMlcqbrPF5qVt511W8Ax2ZVyqO_fM5b1b5kPHGXkDbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
بیژن مرتضوی به ایران بازگشت
بیژن مرتضوی، خواننده و آهنگساز، دو روز پیش وارد ایران و روز گذشته در منطقه نیاوران مستقر شده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/107409" target="_blank">📅 11:51 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107408">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/573c62a08a.mp4?token=MXlHK2s41V1VqKD4mZx2YLJxXf9O60CU6lb2zg8duPiP4OTxFy3ywD_X0X9Iooo0Ukqh4cKbLFFIcOVfRmT-Nh76QejXCNfL3ohVpM5qgmKHU0uJrcaPs3mlAYHDD195F2R5MGH8W4RZjHewRjymrKkAjOB1BXOiAFkhalY3HL5W2D97aJKJtfOGyfL_ykcL_gG-2cCETKdDYAYE-twqyQJfyM8Em1Q4a7BR6yZArsoQAOCo7SzNGo3AuoYoY8oiMbzHxxBWPX-Sy-OYZIRCB9nkMbhj5XQquBbsWLwHJUXNjF1Zh-uC2njA2QnoJiWTGH95gNMGTTZhM6ISk4trYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/573c62a08a.mp4?token=MXlHK2s41V1VqKD4mZx2YLJxXf9O60CU6lb2zg8duPiP4OTxFy3ywD_X0X9Iooo0Ukqh4cKbLFFIcOVfRmT-Nh76QejXCNfL3ohVpM5qgmKHU0uJrcaPs3mlAYHDD195F2R5MGH8W4RZjHewRjymrKkAjOB1BXOiAFkhalY3HL5W2D97aJKJtfOGyfL_ykcL_gG-2cCETKdDYAYE-twqyQJfyM8Em1Q4a7BR6yZArsoQAOCo7SzNGo3AuoYoY8oiMbzHxxBWPX-Sy-OYZIRCB9nkMbhj5XQquBbsWLwHJUXNjF1Zh-uC2njA2QnoJiWTGH95gNMGTTZhM6ISk4trYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚔️
درگیری شدید بازیکنان در بازی دو تیم عراق و کویت در تورنمنت جعلی خلیج‌عربی!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/107408" target="_blank">📅 11:35 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107407">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2719da70df.mp4?token=Zr_OsJLL-UbV5C7vx-LZSs46BR3E0W-xzCG9RZdmLEjb-h_CEJNxBjrqa29uiwujQKCvOP6XigXT0KqZL4S9zuXYkyW1iBQwL_Pw249uhniPU5pmUTxb1M1WzMpocMb5GLFr5U5Wgv4PwAqXcmM1-6vZ77CSTFNxdJNU11dOkEE_m5mtwGc_PGm1-mwVW1pkhMtYSXe6E7s9IF8g6I5gjUTkedyPOu_vWjrbWYY2ghEJwa3sygoq72o2O_HMk1mdG99lG-eUkOkowYKPqEjG-N9frPry1LOYvKNx7uyhhbe3VD3HTjEwADvJ8JDkjl_NpLLveNCpxfyuhVe7rYOR1V0usGOucDnaT2bowzM6cnioxug9VpvYwFpfy2TsyBGRC3wUFB28fix8mXPUonhxvYzp4q-d10zIMM89od4UAPfF7VZPS5rnS4Brzhr7Sfj61Ef5TX6G05AtJA7x8NaoB-8fK_0PVkkJNoUmd1SSgvUfNJaB_bHufSEHbiBMS8Yw8tdi0zCzZWlRwYuleNq5lgNX-cyeo0pK8nNq0lhk8_NKnO8Fe4_UTJfmFv0O2FSN5pXs86tQCWdAFaP5ehuAa23RGK_mhp1V3FsFdiXGa5cnRFX5dJY2J_H-ovGakr6BD-3ZSfIIu_uXAGAb-pyeNHGlsG5qwTNCynKAi8EgI6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2719da70df.mp4?token=Zr_OsJLL-UbV5C7vx-LZSs46BR3E0W-xzCG9RZdmLEjb-h_CEJNxBjrqa29uiwujQKCvOP6XigXT0KqZL4S9zuXYkyW1iBQwL_Pw249uhniPU5pmUTxb1M1WzMpocMb5GLFr5U5Wgv4PwAqXcmM1-6vZ77CSTFNxdJNU11dOkEE_m5mtwGc_PGm1-mwVW1pkhMtYSXe6E7s9IF8g6I5gjUTkedyPOu_vWjrbWYY2ghEJwa3sygoq72o2O_HMk1mdG99lG-eUkOkowYKPqEjG-N9frPry1LOYvKNx7uyhhbe3VD3HTjEwADvJ8JDkjl_NpLLveNCpxfyuhVe7rYOR1V0usGOucDnaT2bowzM6cnioxug9VpvYwFpfy2TsyBGRC3wUFB28fix8mXPUonhxvYzp4q-d10zIMM89od4UAPfF7VZPS5rnS4Brzhr7Sfj61Ef5TX6G05AtJA7x8NaoB-8fK_0PVkkJNoUmd1SSgvUfNJaB_bHufSEHbiBMS8Yw8tdi0zCzZWlRwYuleNq5lgNX-cyeo0pK8nNq0lhk8_NKnO8Fe4_UTJfmFv0O2FSN5pXs86tQCWdAFaP5ehuAa23RGK_mhp1V3FsFdiXGa5cnRFX5dJY2J_H-ovGakr6BD-3ZSfIIu_uXAGAb-pyeNHGlsG5qwTNCynKAi8EgI6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🇮🇷
خاطره حنیف عمران‌زاده بازیکن سابق استقلال: هر بار گوسفندان را می‌شمردم، یکی اضافه می‌آمد؛ متوجه شدم خودم را هم دارم با آنها حساب می‌کنم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/107407" target="_blank">📅 11:05 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107406">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/818f1ea358.mp4?token=qnPCtBEoMxwmkPxDBgUw2mxih4RG2AK-qLpAtmXX9MQUIlphlngHprKb_LNSrxNFDVIXoluy1oeYaOZXPLsEdOPCyzSSuxzZTRB2kjg5DAEdkiu-RbWLvLrnslaiO-eb3ugMaEO_wZpYBAjwyIcwRGJmoMqrsgef8GKu0xpMjLJnfLiO2I1rYQuK3xxKEvvdEvXjDcQC7fTCuHaZ1IgLEp-aSkku5sPzznokLKSg-BWI4c_9rvRMFtikzsZFUQFC1nL3aoOXQ_OUTifGmM3gwRQkRnr19Vy1gyLzZLQByjmM88h48dPQ9F5kz2diq2zzycbtuGoh2jT6u995T0Srp4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/818f1ea358.mp4?token=qnPCtBEoMxwmkPxDBgUw2mxih4RG2AK-qLpAtmXX9MQUIlphlngHprKb_LNSrxNFDVIXoluy1oeYaOZXPLsEdOPCyzSSuxzZTRB2kjg5DAEdkiu-RbWLvLrnslaiO-eb3ugMaEO_wZpYBAjwyIcwRGJmoMqrsgef8GKu0xpMjLJnfLiO2I1rYQuK3xxKEvvdEvXjDcQC7fTCuHaZ1IgLEp-aSkku5sPzznokLKSg-BWI4c_9rvRMFtikzsZFUQFC1nL3aoOXQ_OUTifGmM3gwRQkRnr19Vy1gyLzZLQByjmM88h48dPQ9F5kz2diq2zzycbtuGoh2jT6u995T0Srp4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
با لابی‌های علیرضا دبیر،‌ معافیت بیرانوند همین‌ شکل یک‌ماه یک‌ماه جلو‌ خواهد رفت!!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/107406" target="_blank">📅 10:40 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107405">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6fe4bcfcae.mp4?token=saIdb19OwbH2_hxP5nff8hvftdaAq9fqSDibBXV_U6etZrNpzPJJreXEvEbEbHddSwR8PEnonW2bxhfLxl90RiJywBR6_L4VMdjwcba_0-Qw4JpQGddKNDQTZCKMoHXFS0HETJeeh2nP68gX0IPYXe2-zLMaKmadyGk_QW5_TkYTxAxHy6EJzAApsOX4cn1UHT0lOp48Uu5fOl23sKFpBjiOlp-gk7TxPvBrTfGvmwZJSkaUvr4-z7jYSqrUT1dnXpTlsQPqU_nIg484Xn_hyuKqZqhtVyOrzZjouI1UqNQgVfRgiPVOwUFDhTzft_UEXtt9achUudAg_6mwzxwPahkRxKy8pKk-paRdhGIapWt-uy6TDmXOvhouebIQwAS8pNI4wvPJCdtuhVVFaOQcJ5lEIKoLwx4UHc0DpuoEbJojTwW3R_0TSsX2p6cxUh-m8FU8tbslIkZs_2Gnh4IkY_RJhMpTGgd9qYmTChkSiEYwJZCVPgbOY5cVJxVeAk0iEIjyUdUlyVO6am9wY3bk7Cm_vvQ3_slCQK0qRHcSDiBpOj4Yb1lpF3N2WXVrTyixv5p0oTUzFGjD8RIzOpT9YDGuZjvPWWDdaJO5PIhhQwSwOg0sUBkMys5CGDbjcq6lmre-pFkkhFJvEQmKo5IqgVLcwYuTBGLUkjgptWR2jAI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6fe4bcfcae.mp4?token=saIdb19OwbH2_hxP5nff8hvftdaAq9fqSDibBXV_U6etZrNpzPJJreXEvEbEbHddSwR8PEnonW2bxhfLxl90RiJywBR6_L4VMdjwcba_0-Qw4JpQGddKNDQTZCKMoHXFS0HETJeeh2nP68gX0IPYXe2-zLMaKmadyGk_QW5_TkYTxAxHy6EJzAApsOX4cn1UHT0lOp48Uu5fOl23sKFpBjiOlp-gk7TxPvBrTfGvmwZJSkaUvr4-z7jYSqrUT1dnXpTlsQPqU_nIg484Xn_hyuKqZqhtVyOrzZjouI1UqNQgVfRgiPVOwUFDhTzft_UEXtt9achUudAg_6mwzxwPahkRxKy8pKk-paRdhGIapWt-uy6TDmXOvhouebIQwAS8pNI4wvPJCdtuhVVFaOQcJ5lEIKoLwx4UHc0DpuoEbJojTwW3R_0TSsX2p6cxUh-m8FU8tbslIkZs_2Gnh4IkY_RJhMpTGgd9qYmTChkSiEYwJZCVPgbOY5cVJxVeAk0iEIjyUdUlyVO6am9wY3bk7Cm_vvQ3_slCQK0qRHcSDiBpOj4Yb1lpF3N2WXVrTyixv5p0oTUzFGjD8RIzOpT9YDGuZjvPWWDdaJO5PIhhQwSwOg0sUBkMys5CGDbjcq6lmre-pFkkhFJvEQmKo5IqgVLcwYuTBGLUkjgptWR2jAI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
❌
آنالیز فنی از تیم‌قلعه‌نویی که مشخصا چیزی به اسم‌فوتبال بازی کردن بلد نیستن!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/107405" target="_blank">📅 10:15 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107404">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e340f6f2fc.mp4?token=aa1m5p8q_h3HKuMVKxo5mqsRhAfFRcV2jFl8Jgw9_9q4A8XCrk2a7q1xj-bAqwStWLEn29kSlVxYWkGBRtofs_UnX5cDVVI8n7tpgdWVXTxUxtLqmHbYH0paZkDpMv6wNt7qRbZYgpRUpcOx5AklyBY-QZzIRBWGwvJ8_niYBJl1yzjXI95zaYCpTvFq4ejTih2gffxCe9TOsOYFTHzy0-AJISjYHbOmZWZXH01TTY2niu8YF7hr1fmFnPq816SnjksJB8Sy-mOD1rEAfDDArxT3uBlJg9P8m0844af0Md7d3xvXdz_kTinjq1ofWtQyUh3GsamaPbFVV1GgBnxyhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e340f6f2fc.mp4?token=aa1m5p8q_h3HKuMVKxo5mqsRhAfFRcV2jFl8Jgw9_9q4A8XCrk2a7q1xj-bAqwStWLEn29kSlVxYWkGBRtofs_UnX5cDVVI8n7tpgdWVXTxUxtLqmHbYH0paZkDpMv6wNt7qRbZYgpRUpcOx5AklyBY-QZzIRBWGwvJ8_niYBJl1yzjXI95zaYCpTvFq4ejTih2gffxCe9TOsOYFTHzy0-AJISjYHbOmZWZXH01TTY2niu8YF7hr1fmFnPq816SnjksJB8Sy-mOD1rEAfDDArxT3uBlJg9P8m0844af0Md7d3xvXdz_kTinjq1ofWtQyUh3GsamaPbFVV1GgBnxyhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔺
🎙
مرور صحبت‌های ژوزه مورینیو در ۲۰ آذر ۱۴۰۳ درباره اتهامات منچسترسیتی و پپ گواردیولا⁣
⁣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/107404" target="_blank">📅 09:50 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107403">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jScwkw3igrmQCQwZ4QZG1DDvn4mD3Jq8zvV6bicmAYDHi_rLUDGE8qQ_5DbHeNre3jIjjveHzdi4E9pWrIRT-ANNFPibvUbhokfIqsMLcwDvocLWhfh11pKzB0nlFtruzaEdUvSEf_2nkO_9Fw7zA7ipgcinJySqq3_tMmX0JkJpSymIYNfYQP2aZKpjHKhB4VwSssTTF5TleUFlKLOL5KQlh0r7cJ4X4doG4XdPIo8SmN6V83A_rhRFvV6Beigs553ISKHM-7mwLYhVZlMI1u4YWJApRKGhRbXKKvZnVUA-NRwXrrp3CSR-9wgS5aENESH_v48BoNatr1U1znvjWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
🇮🇷
علی‌تاجرنیا خطاب به هواداران استقلال: جواب پرسپولیسی‌هارو ندید چون مکتب استقلال بر پایه احترام و اخلاق است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/107403" target="_blank">📅 09:33 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107402">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UO5SynNRraco1bP8ZTIJ7Q4uFtJ6G2Z0LeVBASM_CoNkYk0pJp5yChheqSWLUdedrSaGR0xcZ66ePeyBlgTij7lEYYqOoJK32ZZ3qLbM7ZkWLXDpkwqCUAzhPRrLmz_jNyY3GdqJcKLrY0TaL7d_cuSrYJJLCdpLCiB2TEL3VPaAdXWh4svxcraphdkYhMU9kEtkDbynwX9dAfpX1ZQoJWuYvJChDuKd5rkdGq-00h93GXQCEjLK869FiXNc-OxfpWubWour1b-Q22zJrzwXrGbIvfJYwh5iOupF85xQ6i9yQx_4GR-Ah2THd3VbOIkjo3yYKZC84Q_oRVu5tkd27Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
⚽️
۱۳ سال ناکامی‌مطلق امیر قلعه‌نویی در ایران!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/107402" target="_blank">📅 09:25 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107401">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f1638a09e.mp4?token=JXcSc5DnNcUvvh6dES1wILIOFMN6HS9izw9jYimATtguG3bvvtCeAdCDgqTPCUFeorCzCYhYayjynkZpSOwaP8vvvJ3BGudWTq9zh0CELIcr2OPmKhBczPsWHikva8sVg-MzVAEV0Oq-J4VuLffdvwdh0gME5YW6QuL0hkDB1o1W0t1Ke0LYwaNrOHnQIwNDlV5zP3vE73Bg_I-CYG_wNuZAgfhPKRXSQK3Az1aB34FYBG0lxP3Rtb9RlsUfWJEIKq0rsYhOyKtiHzKoXBMOj7nnKDXoHFBFQmo3ZQQpEC1u502e_svPfe3Bp5LBLtZPiWxRyYa45PJNT238oj9qyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f1638a09e.mp4?token=JXcSc5DnNcUvvh6dES1wILIOFMN6HS9izw9jYimATtguG3bvvtCeAdCDgqTPCUFeorCzCYhYayjynkZpSOwaP8vvvJ3BGudWTq9zh0CELIcr2OPmKhBczPsWHikva8sVg-MzVAEV0Oq-J4VuLffdvwdh0gME5YW6QuL0hkDB1o1W0t1Ke0LYwaNrOHnQIwNDlV5zP3vE73Bg_I-CYG_wNuZAgfhPKRXSQK3Az1aB34FYBG0lxP3Rtb9RlsUfWJEIKq0rsYhOyKtiHzKoXBMOj7nnKDXoHFBFQmo3ZQQpEC1u502e_svPfe3Bp5LBLtZPiWxRyYa45PJNT238oj9qyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
❌
مصاحبه جالب بازیکن خاتون‌بم پس از گلزنی و برتری مقابل استقلال در لیگ‌برتر بانوان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/107401" target="_blank">📅 09:00 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107400">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c65f44125.mp4?token=T9mlXy7njtc-PASddGK6b2j5fg0qqg8TvoM2zaQ2VepVqu0OT9R6Ius0A91NVwRIdo5SnK0KMqgNW89p1nX_5HoRw_Q47gg0VcgojmfDpE3a_eTyp4ep9vk9BfWRaUheO94rEXPGUptzPg15mFAErI0ZdQgijlfAmo9qqWu0IwJiFsCpsXWHSqEB83KlKqXf8pOGtRq2LgS-rWHl5EnDFSlmye2M6WtEmp83H8CC74qK5bPFJPZKyk20mPHn1TQNrFBoNxkwLcEsohtdhqA-LO1ljlEg-K68T703TGPjgwgOWDoAr1cIkfAvdKu6r7-xgsu2tKaYx-3ySxjR0GI1Iw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c65f44125.mp4?token=T9mlXy7njtc-PASddGK6b2j5fg0qqg8TvoM2zaQ2VepVqu0OT9R6Ius0A91NVwRIdo5SnK0KMqgNW89p1nX_5HoRw_Q47gg0VcgojmfDpE3a_eTyp4ep9vk9BfWRaUheO94rEXPGUptzPg15mFAErI0ZdQgijlfAmo9qqWu0IwJiFsCpsXWHSqEB83KlKqXf8pOGtRq2LgS-rWHl5EnDFSlmye2M6WtEmp83H8CC74qK5bPFJPZKyk20mPHn1TQNrFBoNxkwLcEsohtdhqA-LO1ljlEg-K68T703TGPjgwgOWDoAr1cIkfAvdKu6r7-xgsu2tKaYx-3ySxjR0GI1Iw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🟣
سوپرگل لیونل‌مسی از روی ضربه‌کاشته در بازی بامداد امروز اینترمیامی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/107400" target="_blank">📅 07:12 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107397">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PrJpQ3EYBONlB34etvyi6weYyD63D7smtW4mR8Iy_sGqSQaBwrPeOKgzASeyUwCez6Ku6Rx22a_IAZPJ6UTWDHibVL2YTLb-aBnhMrHoyuI0C8g0wNFkcpZ3DzvdbShAFyPH6JXWq8hsG2OSY_Xt0EdrwGlF6jMJUZFrwGGRvOR45_ZI6RqnkOckYFLRgHgqVwZaHU6ja7eFL-EWlJGpjgzXQx5lkYleKiug2BRHg_p2C2HvTSC9yAHn349te2H2M6CcNiqEFFoTB9b2a9kEBDoiW9lChMmZ_lJ_ayERY47_gGrfRZVIGDu1_y_KPdIoZbWUPO5pO7ptiS2lnrmjGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❗️
ژرژ ژسوس در مورد نيمکت‌نشینی رونالدو
او می‌توانست در این بازی بازی کند و مشکلی نداشت، اما احساس کردم به بازیکنی با ویژگی‌های متفاوت در این مسابقه نیاز داشتیم. این به این معنی نیست که او از برنامه‌های ما خارج شده است؛ ما قطعاً به او تکیه می‌کنیم و ممکن است در بازی‌های آینده نقش بزرگ‌تری ایفا کند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/107397" target="_blank">📅 00:58 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107396">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tlaow4RKJrqmB-Vn0FpB42XA_K8_yR1ifU50MWIEAtzKv3fregoiog15pzpXJmaDWZt_EJKBYfJe5rwLWB7R74xgk1i2hpplPkhcrD7tbtE0CqH0EayhiEYnMQ2ya9Al9L0h1aS5Al1EZjxqIKDAsQ6aMJePh-0vZIJ3XWrfBEHt37s_74KCwAdlyGq69KP8dx_tab7SFDoiYZXAtSZnUSMIjyTw8qazz6RD5iy0lfK4c0VMeMSG86KSdRb_yKVZMnE39mCiBKFw6YOrFuLBw-RjbC9Ymipoim4APCsi8erKZZ-M1E_a3vjgdyojuUeQs2U8RntLcSLPUaSgVRR83A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
📊
❌
آلمان تحت رهبری یورگن کلوب:
❌
تساوی مقابل هلند در اولین بازی.
❌
شکست مقابل یونان در دومین بازی.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/107396" target="_blank">📅 00:50 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107395">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WYCqJoVb1YbFohLSg3eM2ET-xj0pEqff3Gge9f6B88gn15IENJWl24uD-w222u1hgUUhH-Q90LZNJFOuTo2c0cRkYBnnEpvhYVSDUqwCuAy2gmuR6Ws5e2P8zvFcm66uJt2AJOUqyB4BqHBnxTgj9u0-SnUQt99zQ9ZaFq-YS_SDCRn9VEd0PlRdIye6thv7qXsMQlI7jnco-r3dxBCvrG-wRgbqOug2MyptspLf3fjRON8rmtdDjZrGz24FnwOJcVSjdUaMAfI66h1ImfAAy4jsdr9LY9YAwSggAhsnUJac7J0MuXoA8xiJzlVaocWcdFsIhNETH2iK5OYKWgX00g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇳🇴
🔥
ارلینگ هالاند، [65] گل در [57] بازی با تیم ملی نروژ.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/107395" target="_blank">📅 00:47 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107394">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HQFGuzUwcGPrhIgQ-EOUM4E5m6ONoVtAd0O568mdXfe2h_O0jn7psxI32xqsVWHbhZiLQMv2wjEQh1xs5HSUHbTf5Qr9cbO_T0WBqaw4V6iFmZGWUJQsSrdNdLf0HkZoixSFzU6dzseTOXtBU-hmeoYYrHcb7P5rOAa7H57oU_JC03MTAOcSPwhLZXIvYPtSyRprUJZB8AiivelgpHcSnpSla-lFpNJQ667JaowUnrPOxQecNQ2iiLQYCGgTGsFZ5gYgEeFT1H8NqVA9_vIWU9yk6nBKCgrakH9Sdnq_wKGgLjbkZfmYdmbmwjuRsfgYPmTu2Dbuk09s7mgBjk3s5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
کنایه معاون فرهنگی استقلال به پرسپولیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/107394" target="_blank">📅 23:00 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107393">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lh5_Nc3spBIPzx4wupJquoTWcqNtkEyUn2ZOheuRd-QfaSKFTMTVD3RDrhG6I6p32zsZH0XPOXemPjqcFv1n9uVt_TiTg7ShOPRAWSRW8PmyZU98OVh_6eeGSTS8ZlKGFLAfovT_0bOKB9F1l54emccv_rq3b7Pw59oiZ8bCiOC8II_0m1f5otqAHBE51DgG8JoWbJ72N7fiTeQdE7vrcmSOMdktSEYMz4BsZ7zOWf480g5KDMMaxbYVbGiugSYnKTgY3YLBJpL1X_IfpH-CmpLi5fI7-Kgnr7kBUT8fx78U3pG_Gsz-SDt-ExL6poJic2h4MPJq_yLciv-GRqWS1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇮🇷
🇮🇷
صحبت‌های تند زنوزی علیه سرخابی‌ها؛ جام در منیریه زیاد است با هزینه من یکی را بخرند!
🔻
تا جایی که ما به خاطر میاریم، جام قهرمانی رو در زمین به دست میارن و نتایج مسابقات باید تعیین‌کننده سرنوشت تیم‌ها باشه و شایسته‌ترین گروه جام رو بالای سر ببره اما متاسفانه…</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/107393" target="_blank">📅 22:47 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107392">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jG2u5IoRy14Jbsy_T4fufwbKgDNqvpbHi1yDX1KTj2xpxjVaXSwHzGnD-r7PZvt3hqXMaM27ThyNoAQlsX9ekbN4FR0XHW9GiNCV5X-HgEM3wD6J6DSb8EkkhQpAMq1s2DwjvoZobVHecrZbZRm68LeiV-uIumjf28E4GtZNB54jUDVq78cFsrBv3wLWDeHTFLydzdEpe6CpXyC9HalNd0u-0OTyzgpTn4m37LagN2vgef7sCYU4ziPp8qzjmi0LNUqO8Ti1DdZozNIpZ-LiCuUv0xLA--MV2J-ZzrulBbBvd54KiZ7slvrIknEO1aBflcov2f5XqbONgUJSnMmw3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
🇮🇷
🇮🇷
امیرمهدی علوی سخنگوی فدراسیون فوتبال: من نمی‌دانم چه کسی به علی‌تاجرنیا گفته که جام قهرمانی را به استقلال می‌دهیم. هیچ‌ بحثی در این زمینه شکل نگرفته و صحبت‌های مدیر استقلال برای نمایش است!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/107392" target="_blank">📅 22:24 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107391">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/niRj9DMG4fF1X6zH7SfAVIDMQfSQ8tpupXh1lmVqNCRxRW8qkRU6dNw17SolCa5UkLJEFTuZdVJbO7D3gbpn9frszhAyDDvhzD53d_P0HIPqIYtV1buk5X_xMTU0F4gJ14G8OJBwBLr3_4-LuikE8Nw6rOfDTsx4TfQA9ag_FKosuwhupnv3zK0Z5Gj4UhtS-RPEz6cBxXA1QCHaRBhrKF2NDc78a78eNbxShunjaHPdTMZUDcpBDW7-ZTM6i33mvOBFEiR51f6gYxEQAwILgonMY-C1J3AP1NwnUQIzqbB7avrP8w7t-jw-rYffjy7rqEHMyDlAzHr0Rg5966Hf-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
کنایه معاون فرهنگی استقلال به پرسپولیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/107391" target="_blank">📅 21:56 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107390">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DSzLkRS8w3OxOJwYGOPAOHFHsuwSJ4QkKR7RaZ2zA0EUNgatvkIpE4JKZaV22inxKR20VKjBSMzCnK1r7b8pElI_r93rhxi2i42AhYWtFqgRpK7BPM3L9Bk1bCnw5RZgt24xb2fW1t0hXhsTjwFPzcxkzJIi11nZSmMcazt33yG2EjitWehy1YdpYjWEBSGKzMVxL0pWPgNGNRx9209ak68kfX5epyQKNcUflcVJUMb8itJkzWal9pY6_2xgYFWkeXzgkA9FcxiCXzOcJMdCvGQsGjv3Cpq4rZ78iD2UYKpjo7pAVOZPO-Q83hxK8-ta1c1ddEivp62FU-6IiON65g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇵🇹
رونالدو روی نیمکت پرتغال مقابل نروژ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/107390" target="_blank">📅 21:08 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107389">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c2062dc3d8.mp4?token=QGBTIar9SqzH-RbLMTGjgq7YoQqoghF0CYSpy94qdv1MiWWWk6LdlGg733_CeaGENGlfD59C807vUHT66VQUxhgqXymApaW4iPtNP9wmAFNq6odDcFSRZlH8g0QgtQneWSVKpb_gTKVNZeVTNWGPSqDa16KeR3C2W_A8rKjKrpuucBcepcQ9DWXgsJ0yYII1TovaaoF1SWLLCg2n20_RmTMSoBL7zGEKShWfwtsRK4_cSSt7_mlugGONb51jldQnIP04H91YqHtQUielasV3jdp1ie0quRZHKRzF2P6WSexy_vaNOKah-qfcVpKVvY4u12olakoelCswDaKGmY6YSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c2062dc3d8.mp4?token=QGBTIar9SqzH-RbLMTGjgq7YoQqoghF0CYSpy94qdv1MiWWWk6LdlGg733_CeaGENGlfD59C807vUHT66VQUxhgqXymApaW4iPtNP9wmAFNq6odDcFSRZlH8g0QgtQneWSVKpb_gTKVNZeVTNWGPSqDa16KeR3C2W_A8rKjKrpuucBcepcQ9DWXgsJ0yYII1TovaaoF1SWLLCg2n20_RmTMSoBL7zGEKShWfwtsRK4_cSSt7_mlugGONb51jldQnIP04H91YqHtQUielasV3jdp1ie0quRZHKRzF2P6WSexy_vaNOKah-qfcVpKVvY4u12olakoelCswDaKGmY6YSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
انتقاد شدید مجتبی جباری از داریوش شجاعیان!
مجتبی جباری، سرمربی جزیره قشم، بعد از تساوی برابر فرد البرز، به انتقاد از رفتار داریوش شجاعیان که در دقایق پایانی بازی در نقش یک مربی به جباری مشاوره می داد، پرداخت و مدعی شد هیچ بازیکنی حق ندارد در کار فنی دخالت کند. جباری همچنین خاطرنشان کرد حتما با شجاعیان برخورد می کند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/107389" target="_blank">📅 21:06 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107388">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XzCjJCLOX3tRlNYxDKhsu5_Z290cml_CusiKHAnXxhmvSnV32n1ykIJjZDuZzEteyr7Fnab_mNheWymR_4pp6SCGfouDJvMii3LY4SFM6uagLFUyB_wTHflKXWg6J4xPoJAY0j5qpkqicCYAFVPegmvmg6HHg4fsPaFrBNZmxMMlfir0EwOhkvh9PCAay3X67WfIin5Xt2GDJjFylZ36uRMn66oR-cY8uBIblgl5VVgsw_OZq9q26ji9tD0jZLT4NbzYNMExBsjVvhj5JynkIkFH9sYIbOIOYdluMU4M-WQuLtJTeC3yQkYac-qE0YlkxB_8BINJ9UXzYW8h8y6GkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🙂
🔴
استوری تتلو گونه‌ای رونالدو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/107388" target="_blank">📅 21:05 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107387">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AiQTlSuIIuhbGdF-qRHLHxe1MTuK3jRnl5OnD-uEOFzlPpH_1IEM6lP9fleUrftBRW1rTquuMhPoLJlPY4HfBRv_fe6gk-93DBowZzxHrn6f9pU-yn31g1UubcHK_UFYrK2HEYI-_1-LCjzzPbVdC8nH6rxfKObuTjIKFc7wRabiRwH_2Z6mSmyAasd8Ry1C0J2eKnYqKXTtOE7rjA-GdeWFsqlKvLpUWBy2LrQMlAn1j0DoRS9iWzKcx-Ra9GIaz9eEJaDTlqrLwaJ3D1LjV3Ui1sQRyKo8a12UOWYYjdJUpWF4XynSqo8DmD96msidvqkSEf0r7xKg5TXaEAgrYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇮🇷
🇮🇷
صحبت‌های تند زنوزی علیه سرخابی‌ها؛ جام در منیریه زیاد است با هزینه من یکی را بخرند!
🔻
تا جایی که ما به خاطر میاریم، جام قهرمانی رو در زمین به دست میارن و نتایج مسابقات باید تعیین‌کننده سرنوشت تیم‌ها باشه و شایسته‌ترین گروه جام رو بالای سر ببره اما متاسفانه چند سالیه رویه جدیدی در فوتبال حاکم شده و بعضی تیما دوست دارن بدون مسابقه جام ببرن و حتی فاتح مهم‌ترین عنوان ورزشی در طول یک سال بشن. جالب اینکه درباره عدالت هم صحبت می‌کنن اما در روز روشن چنین ادعایی رو به زبان میارن.
🔻
یک باشگاه میاد به زور و با زیرفشار گذاشتن فدراسیون و لابی کردن، باعث و بانی برگزاری یک تورنمنت سه جانبه میشه و دیگری میگه جام رو به ما بدید! معلومه چکار دارید می‌کنید؟ البته من دلیل این تلاش رو می‌دونم. هزینه‌های بسیار گزاف و چند همتی و خارج از قاعده‌ای انجام شده که برای توجیه آن‌ها باید هرطور شده یک جام بیاوریم حتی اگه تیم‌های شایسته‌تری وجود داشته باشن!
🔻
به هرحال در خیابان منیریه در شکل های مختلف و در سایزهای مختلف زیاده. اگه دوست دارن می‌تونن حتی با هزینه من برای خودشون جام بگیرن و روی پوسترشون بزنن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/107387" target="_blank">📅 20:26 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107386">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbc500f316.mp4?token=v84NZI2_v8s1lwFqsjN2QbUPi4Q3NlBi5LgSkmZkoVP57EkbJPeKYsw1x0Z5meL5Xn3d6OHZp7B6AquE-AW6ZyIvGu9acLUElXHA6zOImL_NulBeJh4z-z-54kVk1S3i51wE1y-QkVpXeJ-cDRuVp5sz46kawdPVmJf83w7ZczycqGeB8GK9ILbs5-UIVmBbdufJ3ocqNqHe-_1cnarq8G6k8aSy-8jo5hgw9wWmGd2fgxMx6k2_updqnlUVo0hQUH8hEPHgkfQEa96zeI1TFFFWhkrk9BpufypT_9Y4MVQRjTO8Hi0ReDqfDh-zptjQW5pXpB6i7dfggw4RsK4daw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbc500f316.mp4?token=v84NZI2_v8s1lwFqsjN2QbUPi4Q3NlBi5LgSkmZkoVP57EkbJPeKYsw1x0Z5meL5Xn3d6OHZp7B6AquE-AW6ZyIvGu9acLUElXHA6zOImL_NulBeJh4z-z-54kVk1S3i51wE1y-QkVpXeJ-cDRuVp5sz46kawdPVmJf83w7ZczycqGeB8GK9ILbs5-UIVmBbdufJ3ocqNqHe-_1cnarq8G6k8aSy-8jo5hgw9wWmGd2fgxMx6k2_updqnlUVo0hQUH8hEPHgkfQEa96zeI1TFFFWhkrk9BpufypT_9Y4MVQRjTO8Hi0ReDqfDh-zptjQW5pXpB6i7dfggw4RsK4daw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اشتباه وحشتناک ووزینیا بهترین گلر جام جهانی مقابل مالی در لیگ ملت ‌های آفریقا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/107386" target="_blank">📅 20:09 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107385">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ce2bef5a1.mp4?token=WCE_bJvc7p4DYRkEzkOQTaMx_h9ki3WOGAWVTvK-Z-7h9sUiyaBwK6VwHghVnj77-RieGUZ092GC95yjpPz_E5TUagPnKIqTDVblaKYcmVwMhSVbJJ1g37kuPgT48DzIN6RyqImy5EJQWF19mXDeNHVAs1icjD_Sq-c_tAXlwAg44jMQL9jY7vHcLlsoEfeTg6Dj3NvAaMBkkn9LhnchqS3ka0hr4dsl8rkCQwX7JAdfaVu6yDogijJoTh5BRNW6Wpx5dF67Ctw7wlYMFyYWwM7VvcSnB4K4escNOAGKKGiluEtlbzaewuZVGJhEPFrW_iB-09ndP6aAUmARnKRLAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ce2bef5a1.mp4?token=WCE_bJvc7p4DYRkEzkOQTaMx_h9ki3WOGAWVTvK-Z-7h9sUiyaBwK6VwHghVnj77-RieGUZ092GC95yjpPz_E5TUagPnKIqTDVblaKYcmVwMhSVbJJ1g37kuPgT48DzIN6RyqImy5EJQWF19mXDeNHVAs1icjD_Sq-c_tAXlwAg44jMQL9jY7vHcLlsoEfeTg6Dj3NvAaMBkkn9LhnchqS3ka0hr4dsl8rkCQwX7JAdfaVu6yDogijJoTh5BRNW6Wpx5dF67Ctw7wlYMFyYWwM7VvcSnB4K4escNOAGKKGiluEtlbzaewuZVGJhEPFrW_iB-09ndP6aAUmARnKRLAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قلعه نویی برنامه نداره ...
وقتی حمید استیلی میخواست برای فرهاد مجیدی
در تیم ملی امید دستیار ایرانی بگیره ولی مورد قبولش
قرار نگرفت ، در ادامه به مجیدی میگن چطور مربی ایرانی
برنامه نداره ؟ امیر قلعه نویی رو براش مثال زدن اونم گفت
که اصلا قلعه نویی برنامه ای نداره
حالا برگردیم به مصاحبه کاناوارو سرمربی ازبکستان !
که گفت تاکتیک ایران فقط ضربه آزاد و کرنر هست
چرا قلعه نویی باید ماندگار باشه ؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/107385" target="_blank">📅 20:03 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107384">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbd8f68cc2.mp4?token=WGRuUW0lQybrLzvVDEwFYjlKvRq3i5hm2e916OD7vRMCcsMRwzRGdNS-DMaVt1O8ftdDXZO4lPn7mTb4-WMFfUcgqMAcWqa7a9hiqLwLqMfOVLWuOZWpvp00-rn53mTgkFjg4xKvf6nDUd4yST9Z_A2xXnZx6HOtDt9XFsUaxj3F85CXhEVbPk1L0E4LFfNkI8ZUDVxX87RiHUuWwt3XZrt-tOO8soMJvJOJ0vB4hsGcdwyk4trJcSIOqQZBnuQs-3wayGnVKLoANtbRlSRDqm-5a8nRsSw5ODTW_e7BMOrB6idwwpIwFu_InsMoyDSGwlXQ0Ud98M5A3BuZca39gg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbd8f68cc2.mp4?token=WGRuUW0lQybrLzvVDEwFYjlKvRq3i5hm2e916OD7vRMCcsMRwzRGdNS-DMaVt1O8ftdDXZO4lPn7mTb4-WMFfUcgqMAcWqa7a9hiqLwLqMfOVLWuOZWpvp00-rn53mTgkFjg4xKvf6nDUd4yST9Z_A2xXnZx6HOtDt9XFsUaxj3F85CXhEVbPk1L0E4LFfNkI8ZUDVxX87RiHUuWwt3XZrt-tOO8soMJvJOJ0vB4hsGcdwyk4trJcSIOqQZBnuQs-3wayGnVKLoANtbRlSRDqm-5a8nRsSw5ODTW_e7BMOrB6idwwpIwFu_InsMoyDSGwlXQ0Ud98M5A3BuZca39gg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
وزیر خزانه‌داری آمریکا: اقتصاد ایران تا دو هفته دیگه نابود می‌شه
چون اونا فقط ۱۵ میلیون بشکه نفت روی آب دارن و بعد از انتقالشون به چین، هیچ‌چیزی براشون نمی‌مونه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/107384" target="_blank">📅 19:52 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107383">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8f6084ad3.mp4?token=Kd_x8NFlCqjGLVes1pSp6GqZMFlKk76E9gJ91h_b9IrpCKEyGJI9IO8iXoR4ZKIl-tbbcKbOciPcHFRr7wt6wRfdVpt6PYEmGsLHf6H_alvgmOJMBQncXT66nTrQfCtbHelXRiqeure1d54_zQXcv0vKLkV3oEYQ7OqitqtpfMXt1A4LQKvv4yri0Y5bJ4FcoWhJtU6r-LGsuzAT4UzpjXC0eCtJwOULuIH2QKAPDHu4yS9YeDAozJx5xnS5hOcgyxbNx7ZX9c9LI2HD2ILkgHLbxsD3w6rESVOCavYumcL6LcStwEECJ974JCSJMfTeP7pWM6nJxALSZRysC26u8QlydUsz_g5q9fbCXPcFtwPHg6wTUSlfmPYtu2guPKEEPvQaJ3SesCn-9dlEq19b9aAd3G3Q0hOearBa5MxNxCgzKpzRZAIPytp0g7cKV71HRub9rtGeTZJiOYVUeYEUkfUylp4_F1vc6wk38154a93Uu8Yhr3PwohmoljXlHv9e_Po7knBwaLnrS_2NMuOTdgMLnQ74FYjQ7mTjy_xKaEUBPldtIkpeboOuuORep_JPd-R4pdQfA346AY9z3ozzHMjefCabBqwn1F57uAPpo2E1WsR6TOP6K5MfThoHereRdPOkofLqJhtKChlAYKlqMnK9Jw6PRf0DzTGLIwWAQcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8f6084ad3.mp4?token=Kd_x8NFlCqjGLVes1pSp6GqZMFlKk76E9gJ91h_b9IrpCKEyGJI9IO8iXoR4ZKIl-tbbcKbOciPcHFRr7wt6wRfdVpt6PYEmGsLHf6H_alvgmOJMBQncXT66nTrQfCtbHelXRiqeure1d54_zQXcv0vKLkV3oEYQ7OqitqtpfMXt1A4LQKvv4yri0Y5bJ4FcoWhJtU6r-LGsuzAT4UzpjXC0eCtJwOULuIH2QKAPDHu4yS9YeDAozJx5xnS5hOcgyxbNx7ZX9c9LI2HD2ILkgHLbxsD3w6rESVOCavYumcL6LcStwEECJ974JCSJMfTeP7pWM6nJxALSZRysC26u8QlydUsz_g5q9fbCXPcFtwPHg6wTUSlfmPYtu2guPKEEPvQaJ3SesCn-9dlEq19b9aAd3G3Q0hOearBa5MxNxCgzKpzRZAIPytp0g7cKV71HRub9rtGeTZJiOYVUeYEUkfUylp4_F1vc6wk38154a93Uu8Yhr3PwohmoljXlHv9e_Po7knBwaLnrS_2NMuOTdgMLnQ74FYjQ7mTjy_xKaEUBPldtIkpeboOuuORep_JPd-R4pdQfA346AY9z3ozzHMjefCabBqwn1F57uAPpo2E1WsR6TOP6K5MfThoHereRdPOkofLqJhtKChlAYKlqMnK9Jw6PRf0DzTGLIwWAQcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
🎙
تقلید صدای باحال از گزارشگران مراکز استان!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/107383" target="_blank">📅 19:34 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107382">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/464a64d711.mp4?token=G3BeBDvOQ9biH6MoKJ_geCS1D6sZyT4f-UPayoIMgV-wncaocCVbHKQvkv3zJLW3n8_-HF5FU44gO5LqeVNaRC0qE4PspZGnNXssmKdwFHNUD6GUVHwmaxNBNEoZ0WESmqwghpi5Tw7b3KF8is5mvCAu1TvEYo8NJRG5p9wwdwrsEPqN-fYi4FHUDqwTAWyg_aDpQ3MXaAVnxEObmdq6C-FgDetdvmfY6zhP1ZI0VHTqvJ1YPvSsRMv7e6QX4Vdjq30ofg37Ni61jgiDe5dlf9nPsxPfwzw1DAeWV0A2SjanEy44t_LFhsn-OrVYFBpXnD4vOjoAMeNqtnWvD-msUDU9nXEoBgsR2Qb8dbKS-3tQlwGFMva6Z6MW0QqETuijsQpQ2E-8zXBs4XPtih6qFpKUtY4RGAyGdewv-PbAGPmtGSQTG9nj1fmqVESPCd_Vl0Joe_2txHAu1_VwFGDQcCIZUO9K8UpzQZxdiJN2su5ykp1JFQ-P5Q4fTo2RMumnOuW1a4vb7z2ylO0tVSpR9g_m1Wp_onp1eBgthyTo6IVMaKQdo_7Ysjo6HsL-vR4763ZgsPLh9Zf6cxXxZG__uu8rnUkLERQ0sV77wDJfkwL2KexUEu6Gzjuk3ZFIR323WDyh254ewjPqp97vdIPbPYq64O4roeJjEMFGwoBanR4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/464a64d711.mp4?token=G3BeBDvOQ9biH6MoKJ_geCS1D6sZyT4f-UPayoIMgV-wncaocCVbHKQvkv3zJLW3n8_-HF5FU44gO5LqeVNaRC0qE4PspZGnNXssmKdwFHNUD6GUVHwmaxNBNEoZ0WESmqwghpi5Tw7b3KF8is5mvCAu1TvEYo8NJRG5p9wwdwrsEPqN-fYi4FHUDqwTAWyg_aDpQ3MXaAVnxEObmdq6C-FgDetdvmfY6zhP1ZI0VHTqvJ1YPvSsRMv7e6QX4Vdjq30ofg37Ni61jgiDe5dlf9nPsxPfwzw1DAeWV0A2SjanEy44t_LFhsn-OrVYFBpXnD4vOjoAMeNqtnWvD-msUDU9nXEoBgsR2Qb8dbKS-3tQlwGFMva6Z6MW0QqETuijsQpQ2E-8zXBs4XPtih6qFpKUtY4RGAyGdewv-PbAGPmtGSQTG9nj1fmqVESPCd_Vl0Joe_2txHAu1_VwFGDQcCIZUO9K8UpzQZxdiJN2su5ykp1JFQ-P5Q4fTo2RMumnOuW1a4vb7z2ylO0tVSpR9g_m1Wp_onp1eBgthyTo6IVMaKQdo_7Ysjo6HsL-vR4763ZgsPLh9Zf6cxXxZG__uu8rnUkLERQ0sV77wDJfkwL2KexUEu6Gzjuk3ZFIR323WDyh254ewjPqp97vdIPbPYq64O4roeJjEMFGwoBanR4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
⚪️
⚽️
چرا تیم امید همیشه ناکام است؟ این ۱۴۰ ثانیه از فرهاد مجیدی را گوش کنید!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/107382" target="_blank">📅 18:51 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107379">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/36187cd975.mp4?token=OrnFhd9HfWrOs8_0crCZwNwl432n8VkiWyP4yx2lmsdQssHPq-6uEi1dwY-r0PhZ9R0DS6k88BuRJfYxbAFmBADPTOJKnJNx0zjBWpQKC1sJd5fM70g5ojMcxZlNTZXq-yGs3u1Rrsg_Bhp4B5rhFxhjc-dBdg3gQwvOTpxxSM6RSoLVvrOFMAI_40chfrO2XkJNGGCL4W58Npmf4cjqGPJfZkce3geRRyLZdc9k7M-riNSpQIm1hAa0_A-4mbMSQ99tFf_6-HcMscj0OhUmEcDj88HpukNRxwCYOsiK4IdJsSsCfm-mmchdwfKhPbpWV9lzJkqbBDD6XzAIw_x70g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/36187cd975.mp4?token=OrnFhd9HfWrOs8_0crCZwNwl432n8VkiWyP4yx2lmsdQssHPq-6uEi1dwY-r0PhZ9R0DS6k88BuRJfYxbAFmBADPTOJKnJNx0zjBWpQKC1sJd5fM70g5ojMcxZlNTZXq-yGs3u1Rrsg_Bhp4B5rhFxhjc-dBdg3gQwvOTpxxSM6RSoLVvrOFMAI_40chfrO2XkJNGGCL4W58Npmf4cjqGPJfZkce3geRRyLZdc9k7M-riNSpQIm1hAa0_A-4mbMSQ99tFf_6-HcMscj0OhUmEcDj88HpukNRxwCYOsiK4IdJsSsCfm-mmchdwfKhPbpWV9lzJkqbBDD6XzAIw_x70g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
🇮🇷
محکومیت ۴۰۰ هزار دلاری استقلال در پرونده کاریله؛ آیا تاجرنیا طبق وعده ای که قبلا روی آنتن زنده تلویزیون داده بود، مطبش را برای پرداخت این جریمه می‌فروشد؟ آیا دیگر اعضای وقت هیات مدیره، طبق گفته تاجرنیا از جیبشان این خسارت تقریبا ۹۳ میلیارد تومانی را می‌پردازند؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/107379" target="_blank">📅 18:31 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107378">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ea1431c1f.mp4?token=czIn89ijQ53wu1dkAp2mFL3DrOANPrLSK1McQXMp-op1VNm0xm02McjEng0ndXdiHiInfJTx1sroWEdBDw24P8RVfUN5R79c4nPOpbJvMLSo-TabzDM0R9IVUuA-6zhpuHm7MhAhjTkD8Ck_nZDbh-d6eT6wGCryDRTlXwv08o1bYbIrmcQan_68u3BPCFor43oB4oVtoCY_x2JKmDuQGxOcP6V1lugI6ziAyL5GRKqyuPWt8QKwcL2WqjClhlHtiR8Bg0MFEq-xqyhFYF7mKztasSPSHAn4Wg_6NveNHR-Om_ZGEWrtkmIPnttlghPqSC0MfWLOTfupoQFJf3No2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ea1431c1f.mp4?token=czIn89ijQ53wu1dkAp2mFL3DrOANPrLSK1McQXMp-op1VNm0xm02McjEng0ndXdiHiInfJTx1sroWEdBDw24P8RVfUN5R79c4nPOpbJvMLSo-TabzDM0R9IVUuA-6zhpuHm7MhAhjTkD8Ck_nZDbh-d6eT6wGCryDRTlXwv08o1bYbIrmcQan_68u3BPCFor43oB4oVtoCY_x2JKmDuQGxOcP6V1lugI6ziAyL5GRKqyuPWt8QKwcL2WqjClhlHtiR8Bg0MFEq-xqyhFYF7mKztasSPSHAn4Wg_6NveNHR-Om_ZGEWrtkmIPnttlghPqSC0MfWLOTfupoQFJf3No2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
درگیری شدید سوبوسلای و بازیکنان حریف در بازی اخیر مجارستان مقابل اوکراین!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/107378" target="_blank">📅 18:02 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107377">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a49852d72a.mp4?token=Oou-eehae3i9UNrEfC2AVrk7EIj1_uLp7jiKaOYpLeztXQmCwGgCYM_jkkkiqIhW-BHR1xSvJ3iJRQMmpn3YdV9PR5p2dCdugSSM36AHAG_aeHskcZmXQwwncRUDCUlyFcVtpTeSHeXkeij9ULzz1BYYBIt-SNHqSnQg3vjbdL_aQS5AGoag1jECBfrIhHMMMUJnegSLmx-beB0fErln98RpGhICVEfq9-q9T5LeFsJhoMSyT9gRVO3JSwARriRQTNK5FYG38PJGkeF0g0MYs-QrB7EJstrWTGNdbmYglmi5HyTTgnKTT8Ii022k6km6LIiVH-nvbc74DROxmne3Yg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a49852d72a.mp4?token=Oou-eehae3i9UNrEfC2AVrk7EIj1_uLp7jiKaOYpLeztXQmCwGgCYM_jkkkiqIhW-BHR1xSvJ3iJRQMmpn3YdV9PR5p2dCdugSSM36AHAG_aeHskcZmXQwwncRUDCUlyFcVtpTeSHeXkeij9ULzz1BYYBIt-SNHqSnQg3vjbdL_aQS5AGoag1jECBfrIhHMMMUJnegSLmx-beB0fErln98RpGhICVEfq9-q9T5LeFsJhoMSyT9gRVO3JSwARriRQTNK5FYG38PJGkeF0g0MYs-QrB7EJstrWTGNdbmYglmi5HyTTgnKTT8Ii022k6km6LIiVH-nvbc74DROxmne3Yg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
گریه‌های آرش‌افشین بازیکن سابق استقلال: نتونستم پول خوبی از فوتبال در بیارم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/107377" target="_blank">📅 17:20 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107376">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d81597ceff.mp4?token=vx9BMB5mDr9N82-JqMabzQC09Rn-qqyurKIq7L0oDmVTnXFbdVSbYBsi9wtGpxENuDSGJyoXVaNrQEr9Zd3f-7p30Oxgv-UZBgWblbmfpcZ64fe-QsERR3S8Lxvsq15pWCwpfTElRY61YInJKO2Qg0dOOxK-SatvEFj1h5IBu-AKqPSEosxMQnSqu-PeLfdXP9niqgf6ugzn5ojH54Pf1tVW2d_ivKWnw8C2p40HpOFb1thPibK49cQRqTLJdTuD5j9r7Zh2irlbRaM3ESP6549DEgmWG6YVOs5YkaWRYlzN4QlHnEZyvtuK4XOqYxnJ86F1N-kYoLSU8jPMG5N-RA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d81597ceff.mp4?token=vx9BMB5mDr9N82-JqMabzQC09Rn-qqyurKIq7L0oDmVTnXFbdVSbYBsi9wtGpxENuDSGJyoXVaNrQEr9Zd3f-7p30Oxgv-UZBgWblbmfpcZ64fe-QsERR3S8Lxvsq15pWCwpfTElRY61YInJKO2Qg0dOOxK-SatvEFj1h5IBu-AKqPSEosxMQnSqu-PeLfdXP9niqgf6ugzn5ojH54Pf1tVW2d_ivKWnw8C2p40HpOFb1thPibK49cQRqTLJdTuD5j9r7Zh2irlbRaM3ESP6549DEgmWG6YVOs5YkaWRYlzN4QlHnEZyvtuK4XOqYxnJ86F1N-kYoLSU8jPMG5N-RA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
⚪️
⚽️
افشاگری حجت‌کریمی عضو هیئت رئیسه فدراسیون: قلعه‌نویی قرارداد ۴ ساله می‌خواست!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/107376" target="_blank">📅 16:55 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107375">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30882bf1b3.mp4?token=rjXeoutoXhf8R0B11pym7_zINkJLiKOgo0K4xzKgpbtDcYtAWwGxq1gxA3WWEtRFuUlGJQw1TqxYDkw_JKXbirny1y4j-h0dcqKwRKXm0vNMrbvZ0FgkuU6seYodVgvCMA16ed0La0Eu2uHZTRCmvbIO2GbZCjHJ_BT0nYXN5wEc7F7U9DQCSbutjGK_Q2irD6vBa0sKPjW4_hLyq9RH_IvkTL7lXUKjK38pbk5Xz-Fh6zdf42xZnRM6UAWV_ABp-B2_hcaHhZDjHZOPW8GPT-fXmnvWIhO6SoaB3WDj5JzWcbcFj1o3ApGari1-PLE0BgzwIw-UOjcYBvpdkvI9UA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30882bf1b3.mp4?token=rjXeoutoXhf8R0B11pym7_zINkJLiKOgo0K4xzKgpbtDcYtAWwGxq1gxA3WWEtRFuUlGJQw1TqxYDkw_JKXbirny1y4j-h0dcqKwRKXm0vNMrbvZ0FgkuU6seYodVgvCMA16ed0La0Eu2uHZTRCmvbIO2GbZCjHJ_BT0nYXN5wEc7F7U9DQCSbutjGK_Q2irD6vBa0sKPjW4_hLyq9RH_IvkTL7lXUKjK38pbk5Xz-Fh6zdf42xZnRM6UAWV_ABp-B2_hcaHhZDjHZOPW8GPT-fXmnvWIhO6SoaB3WDj5JzWcbcFj1o3ApGari1-PLE0BgzwIw-UOjcYBvpdkvI9UA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نبرد دو هیولا از دو نسل! امشب در اسلوی نروژ.
🔥
🥶
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/107375" target="_blank">📅 16:34 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107374">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/119aac7582.mp4?token=tVPWHiPx7EnK1mzEg2gsokgnHBm80fGZYZHHxSqj81QnRCY_0XxUQYtsdtJxLs4eCuSLMOt0UGhhfejTfc7wyUeAnXIVYUyY-6eAlaS39KOykwmq6Bx67bHSIAvLS2NsUuglnkPf6qThp4UmmJgl5HWdIxpj6hdhIk2taQjLBFzv0deHDC0waIS19H81gKKF7qRPCroZ6sAPl0HArHytb3ROVKY4EBq7LUm98vORryxYYeldEgaFZiIFtzeiVWHhU5t7g_Zzw-wpFmpQdfyYPTik7TKvb7qGfxjqfUHWWYV8tQ3VCLilOMtj97AurL7X9510XYrqQEL9Gsfn4uQ11A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/119aac7582.mp4?token=tVPWHiPx7EnK1mzEg2gsokgnHBm80fGZYZHHxSqj81QnRCY_0XxUQYtsdtJxLs4eCuSLMOt0UGhhfejTfc7wyUeAnXIVYUyY-6eAlaS39KOykwmq6Bx67bHSIAvLS2NsUuglnkPf6qThp4UmmJgl5HWdIxpj6hdhIk2taQjLBFzv0deHDC0waIS19H81gKKF7qRPCroZ6sAPl0HArHytb3ROVKY4EBq7LUm98vORryxYYeldEgaFZiIFtzeiVWHhU5t7g_Zzw-wpFmpQdfyYPTik7TKvb7qGfxjqfUHWWYV8tQ3VCLilOMtj97AurL7X9510XYrqQEL9Gsfn4uQ11A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
🇮🇷
دو بازی، دو گزارش، یک تفاوت عجیب!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/107374" target="_blank">📅 16:05 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107373">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EkBWPRXRy1ffAZvqj4p1V04ed3TTKwyixrDlDyhpGMSBXtmBP7G1gAv4v82JTfzlPqw4xrMSOiKDUf83IbVd0_y2OpMznwu8-ylcqLS77SRwLZhpYS5ImSh7TA1Zs6R-sri0U3mUZKSDRgTk9al2crLsq97rd6lMoTFh5L7ihnhd7Pdj3lIHEjjG7rZ9AVrvfp5a_tEJ6EZ7vgtanKxzLAnF2GfT9ct0LDs7HPRxlNNIk_qluYiwPPIZ2-w5dW2BJjg-rMgHq0lOdSicM32RZknr7VQNxfTxu8EAvMHnROaI8xcIgO8qtbgwq2r3JW2YNH_N7HEZc7ocvdF9wytMEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
گاتزتا | روبرتو مانچینی در زمان حضورش تو منچسترسیتی دوتا قرارداد بسته بوده. یک قرارداد رسمی با خود باشگاه به ارزش 1.69 میلیون یورو در سال و یکی هم یه قرارداد با الجزیره امارات برای فقط چهار روز کار مشاوره به ارزش 2.03 میلیون یورو!
هردوی این باشگاه ها متعلق به شیخ منصوره.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/107373" target="_blank">📅 15:40 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107372">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a4c9c45d7.mp4?token=WKMrJfBcVeWAsIg-E5c3Gq4kz7SGHJUVe2rVUAbiOyITSt-EZYSUChvhwTdlAQ-szqTR8gDuptOrL2Rn4a3QTaaHGYeRadcl6m22XE6Dn8QxNxTawiO4QZAddM1zsFmCfcHadugFl4YnshY_nmvdV8-PL2X2E4ngJdYO_0nOHmsvTmqITXVKZEtkKl3GRKEweGYXnmdPFwaQapbyy4aSws0Iar0yv4kiQxLAfZiouny1wBNmOtihPxwD8F2TSarly35PzJWxHq999kmxJsN0Z5Mk7cF5z3jB5EyS7_b6NWAGFh5sOphYh0wYpz01P2tAllzIGP9XyOOrNOa-kyTyjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a4c9c45d7.mp4?token=WKMrJfBcVeWAsIg-E5c3Gq4kz7SGHJUVe2rVUAbiOyITSt-EZYSUChvhwTdlAQ-szqTR8gDuptOrL2Rn4a3QTaaHGYeRadcl6m22XE6Dn8QxNxTawiO4QZAddM1zsFmCfcHadugFl4YnshY_nmvdV8-PL2X2E4ngJdYO_0nOHmsvTmqITXVKZEtkKl3GRKEweGYXnmdPFwaQapbyy4aSws0Iar0yv4kiQxLAfZiouny1wBNmOtihPxwD8F2TSarly35PzJWxHq999kmxJsN0Z5Mk7cF5z3jB5EyS7_b6NWAGFh5sOphYh0wYpz01P2tAllzIGP9XyOOrNOa-kyTyjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🏆
یامال: این توپ طلای ما رو بدید بریم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/107372" target="_blank">📅 15:15 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107371">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8c98790b5.mp4?token=oY2OY2IDVd_V0jYZNCsdYmNTJ9mAkwNRZCBqfT8mEoH9uH96ASGIncTmtxnBZdvj9V9J8zch94aBfh-f3T9gP27Gi_4rb-qyehHs5Zi4XB-jN3lc2i9toPXqcQPhEpiWy0YY-EcAY12q_YhOzgpefpt62pplDASKp6hYpwBuRYYoZ8V8g7d-lheRwuFyRB38bTR6l-ZDShbKyy77Smoz4ePdzLibYO8t6LBmnvD3s9mkaOe72FrHAu9guAIyt73Xr8wnwnIWepidjPPxNaIPoFvK9U9sSK2bUboz4yuoDtmyRYkKEgZ1ct5Y4Fqmd2QWVKT-AtX6YUXxEI6KrL5kyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8c98790b5.mp4?token=oY2OY2IDVd_V0jYZNCsdYmNTJ9mAkwNRZCBqfT8mEoH9uH96ASGIncTmtxnBZdvj9V9J8zch94aBfh-f3T9gP27Gi_4rb-qyehHs5Zi4XB-jN3lc2i9toPXqcQPhEpiWy0YY-EcAY12q_YhOzgpefpt62pplDASKp6hYpwBuRYYoZ8V8g7d-lheRwuFyRB38bTR6l-ZDShbKyy77Smoz4ePdzLibYO8t6LBmnvD3s9mkaOe72FrHAu9guAIyt73Xr8wnwnIWepidjPPxNaIPoFvK9U9sSK2bUboz4yuoDtmyRYkKEgZ1ct5Y4Fqmd2QWVKT-AtX6YUXxEI6KrL5kyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پنالتی که هری‌کین در تقابل مستقیم با یامال از دست داد تا سرنوشت بازی دیشب تغییر کنه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/107371" target="_blank">📅 14:50 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107370">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e4Qe1Tjy17EJepFg5mPW6Xh1ukx7eXfr872-fDJANTeLMbuHVhzqaOFzTbb2JeWaAhkZnBm1NE8sAhipH158esT_eRdEqCwwUbp_HbNq-C8XSjP9OERHxSL6e_UZoVXqlYVM1yVlK9koniX4yUGSWSUCnpuZAMY23m5eYiw27jf9rGbwYQyo7A4IioF626KMsqNOMk5834zIbZ9x043c40HlDQnlyXWN83Wzfq6HWpCEreL9Y53V3MFjM_Cn9yF_2W-b4Wh_OkZRXAdKqguNlXvWx5CAQaU-fnooppqMLQnma80_ILq32Aj5uLcYJjyvEXXO_G1hCXoyaBgT-2EjTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پریشب نبرد منتخب آفریقا و منتخب ترکیه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/107370" target="_blank">📅 14:25 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107369">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rw5qw56DE6H6tnic7ADEvPTrfIIsbFqnCZk1aCrN49iQVmzj945Gp0-bF7TJRGMiFN0Yx2J_wm3EfHIAKiFKCQTNItMypKFasNcXxd1W2I4-ufV_V9_kPk9O4S1bMV-P7B73eIUXh4Tr7f7WBEDpeuyjLUyOj-wYWkgevSawKL5q_ujbfJFjiPyIoOOlAzTJQpBB2yS6HUABKuVevZjObC-_VPhS6PmFwDe1S-dydL4o0NTPrenXqfuQ_nxRl6Xa_TTJ_40SdD3ldswbQPAlkZZVivSoR9LO8Vq-dhZ0FWdBSbOIFDzIZeSAGDXlAexhNuYONKWPBOVznuz2bQAFew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
💥
🇪🇸
برخی رسانه‌های اسپانیایی گفتن که اگه سیتی محکوم بشه،‌ ممکنه هالند درخواست جدایی بده و با توجه به نیاز بارسا به مهاجم نوک، این بازیکن گزینه اول کاتالان‌ها میشه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/107369" target="_blank">📅 14:03 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107368">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LLXTznBs7UL8i_YmGWUWMeD49gNP1unYAFqOb25X_sjylYzpit5wU2Wif8jVyHIi9KCyLtHYv2YXqFYqoNhgOu3iNeQYasFYcG2p3v__HG683GTyO-W-JKpvCSRwp4O5y0vg2uP4sL2PPWOfWSswXaZyd6SQCJoBRplObL-gG6B2gxnX8fGiKCX1Kp-aMdAFrNwsTW8n661p04wcFkUMD0S9OU-0dM5prS1WY7whpZQu9324x-QNTlSDVOiLrKOc5xB5KZKO7p1MdlZdviXSzszcVElmkDd92taYe9aUFmlvUBbu5SeSGgLFFSG0CWuktNQGyjIclh5lGr5C-ZdwvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
🇧🇷
نتایج ضعیف برزیل آنجلوتی در مقایسه با سرمربی اسبق سلسائو در بازی‌های دوستانه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/107368" target="_blank">📅 13:42 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107367">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H8-gpqf3w8KREV6HT5lPHg0HJOqeSLc_dg8Zk5SjlXY6M1l3ZtMxlCwIHa-baYVH3Gqyp_-sxkxL43AYihu96Q_UZYtIveY6-tYVFrLcRCewr0tcPjc8EzABfB9q7ob82RnvGZ6iLEj9wT05MA6cJuGQWH7NoMfDd378DdIQHCmPYIRDIzZm_uxuEen6_juvR0XxEYNy1i0IioCbOiJt3Sjat_oqcVMvHkBxlYuVoGeourryhDFsyiRe3ojXwraqsfX6tSBjtyh6m9V9rcX4tvEFFIIlwufA0ucjTxdxAOBlwM4DV7CH31AU7AJ0Sl93a2LQ1BW9ZDcQCwwy6glMkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
‼️
اعتراض تند عضو هیئت مدیره پرسپولیس به شایعه قهرمانی فصل‌گذشته استقلال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/107367" target="_blank">📅 13:32 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107366">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39d99adabc.mp4?token=AOkKxJwaBJ0HALHLMAKP8rc9BRPej08JBZ7VlEXYqoTsHV9tPoPCR_FxUuMq2KcFxpxJDRzl2goaGIb7OCdVLcqn7Z5VsOuGeomZQGJ-XBVLNTcoQb7lT1kBcB5SBsKR7S-vzCSPlr0hhL9MnHbAh-VlnY3VeQWTo7Ru_uKaVX3cSVvByzf8IyFp2fNhE8s4xqfs6pwv7vaB-iPBonWJmFSNJTKuodw6y-IEvTpZExxe4cl16bK__EV2tXxmNZzqAaJaCJU19pnD3-Ey6C7P1yoCAzMc60SVduU0HSYKBrjFTBgZzlyjtU5bzHwiLzZ1GgQ2kChJlQRmIX0X2ChjQ0Ouej3XuCUKv3AuuiWX8ncUwKr0Ib8uCH4ZY-C92xCe5Ux9ZYMpzwZDFsE8Tpe_oAkjeCLWnOGuFXiXhreoT4wO176-unxS2k6ppMvu25OJMBUpS8vZSV2xjAEnzg3L3XF8AiQng3VSeeArr0mHWboZdm853eA547QPav2RPZma3ifYa2R3mopuIg38R1l6341JmD0ARbe1c8coJUeG2KWyEwuASWI0rvqIMAqnfMDyS2X35bIaBaQOV2YS0xYP3HofXBSMNZe7Kz4MCyrZsL7xPB_QdUdErqRe_iPzWgAFf3beKi4NKzn7ZrB5Xc5uyU53cSZNsjZs798vKbpseyY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39d99adabc.mp4?token=AOkKxJwaBJ0HALHLMAKP8rc9BRPej08JBZ7VlEXYqoTsHV9tPoPCR_FxUuMq2KcFxpxJDRzl2goaGIb7OCdVLcqn7Z5VsOuGeomZQGJ-XBVLNTcoQb7lT1kBcB5SBsKR7S-vzCSPlr0hhL9MnHbAh-VlnY3VeQWTo7Ru_uKaVX3cSVvByzf8IyFp2fNhE8s4xqfs6pwv7vaB-iPBonWJmFSNJTKuodw6y-IEvTpZExxe4cl16bK__EV2tXxmNZzqAaJaCJU19pnD3-Ey6C7P1yoCAzMc60SVduU0HSYKBrjFTBgZzlyjtU5bzHwiLzZ1GgQ2kChJlQRmIX0X2ChjQ0Ouej3XuCUKv3AuuiWX8ncUwKr0Ib8uCH4ZY-C92xCe5Ux9ZYMpzwZDFsE8Tpe_oAkjeCLWnOGuFXiXhreoT4wO176-unxS2k6ppMvu25OJMBUpS8vZSV2xjAEnzg3L3XF8AiQng3VSeeArr0mHWboZdm853eA547QPav2RPZma3ifYa2R3mopuIg38R1l6341JmD0ARbe1c8coJUeG2KWyEwuASWI0rvqIMAqnfMDyS2X35bIaBaQOV2YS0xYP3HofXBSMNZe7Kz4MCyrZsL7xPB_QdUdErqRe_iPzWgAFf3beKi4NKzn7ZrB5Xc5uyU53cSZNsjZs798vKbpseyY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
على تاجرنيا مدیرعامل استقلال: بیرانوند برای آمدن به استقلال پیام فرستاده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/107366" target="_blank">📅 13:10 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107365">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1582f31111.mp4?token=XWrDjhny8t7YwUp7IskU_jzPyN2wZRZS2KUSgPDLgNR9_ZovAIEtqd6xw19q2DXRU_dTBN_vVLLKNrkEIxRl1dDE-ca8jgQfwGMxctYlsIVIZ_RytETKZss5Yp_RGx7DZ4TvCcLlPfNaI3jcIEJzxul62Pms0GZoUIhblx4rHOC15FqRraIYeibbVTgO0_AgPUOyIQsI8Yxb7sJMrQqVQxvA-gyzOki7pgEka4UPfnPJEjzzXLJ66oS8ivoyV7B_J8xJn5lYHEEh22fovD2KxSf98veBIfHqbl_LZkJ6Ct2psiL8T2q6_fAXAPN0bSWg5eVapFZQ0DY8I448JhQH5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1582f31111.mp4?token=XWrDjhny8t7YwUp7IskU_jzPyN2wZRZS2KUSgPDLgNR9_ZovAIEtqd6xw19q2DXRU_dTBN_vVLLKNrkEIxRl1dDE-ca8jgQfwGMxctYlsIVIZ_RytETKZss5Yp_RGx7DZ4TvCcLlPfNaI3jcIEJzxul62Pms0GZoUIhblx4rHOC15FqRraIYeibbVTgO0_AgPUOyIQsI8Yxb7sJMrQqVQxvA-gyzOki7pgEka4UPfnPJEjzzXLJ66oS8ivoyV7B_J8xJn5lYHEEh22fovD2KxSf98veBIfHqbl_LZkJ6Ct2psiL8T2q6_fAXAPN0bSWg5eVapFZQ0DY8I448JhQH5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جوری‌که بازیکنان آلمان از یورگن‌کلوپ حساب میبرن!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/107365" target="_blank">📅 12:45 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107364">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a8b1d7243.mp4?token=dYDvL4CJDPAVm2M_JnVDjLjRd-S6pHD6DvBi_dd40_-Jmj4y6eqmYI2A59TlknjcdNfWbR3vWtdMGqf-hSuEWLnZGudhcKjcScyxGyJ--sKnYmoG2EZz-QDBdL_srkojESXugPV8UxoDVSwIloQEgnbZl1IiclEquI4Etg-BfA61Fn5H4ezMkkyCjuksijpQe8b8hpab6MdcynebHYKKiJAeG9WUrhwOk2XdyzNIxlU3Z8YGgdt1MwIjaX8Op-Wy8hYtWa3icgCkOI5iVv1f7KkhuxtqaI8ld-86JNc4ODoF7VOV7Rym5aaGF52ErjWLIw3OLTlw1ql0NW7-veTVpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a8b1d7243.mp4?token=dYDvL4CJDPAVm2M_JnVDjLjRd-S6pHD6DvBi_dd40_-Jmj4y6eqmYI2A59TlknjcdNfWbR3vWtdMGqf-hSuEWLnZGudhcKjcScyxGyJ--sKnYmoG2EZz-QDBdL_srkojESXugPV8UxoDVSwIloQEgnbZl1IiclEquI4Etg-BfA61Fn5H4ezMkkyCjuksijpQe8b8hpab6MdcynebHYKKiJAeG9WUrhwOk2XdyzNIxlU3Z8YGgdt1MwIjaX8Op-Wy8hYtWa3icgCkOI5iVv1f7KkhuxtqaI8ld-86JNc4ODoF7VOV7Rym5aaGF52ErjWLIw3OLTlw1ql0NW7-veTVpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
🇮🇷
❌
تاجرنیا: در پرونده توهین دسته‌جمعی هواداران پرسپولیس می‌خواستیم به دادگاه CAS شکایت کنیم که شخص آقای مهدی تاج به من زنگ زد و گفت از پرسپولیس شکایت نکن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/107364" target="_blank">📅 12:15 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107361">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6292835767.mp4?token=PbboC04g31qrPokSefmMgz6qCt4COT57V_IBJkU7kCWVpZ6VN61oaLOY4nDBvjigeucM3fqE1-tVPBeKjgSxBhP92gyHW_DaN9DpO9XFOsCA9jcyEODQ64uvVvJ3koJwuNHjSj7S_6rFGEiQ6hJhYZYnn8GDYXtcnz8JMxXHZKs9StMMJVIvBkNeh2qy9nBar9PWNUta5Q_C8jSN4dXsSrT5Y2UfO28bBSUB2MW6IdrcGGvpMA2wD5oc9Zq4FJ3RrfpThp5SE1bQ0rlVyf2BDOK99q2lZ5mQfGb2zAM0r1rU8rQVhQDjGd1V551fUSbQmCoSA3_0nhGojADqtv6AMk3lUYSOi_3WVlcB50VNIVAcWnMtlyDSkK-X3DdKfkGy0qtT-91RHMXIWd4J7FsuH4J7ahBFUCYjdPtJry9d6kWzXd2XGdpAgBp-1s6DAFMWUyhuyyFMwbqIEp8pF9mIWC8Z3RoJeAlfBsV8lFfiOAHK7GRafWuTTtnzY3JSZJsXq1urBsUEjnteMtbRnI-iwozRGGJmwvr5zTleVWibdCFm9Gg8OAWXUvUDD0k0VYfgd5-fQytm99_fQrBQM0wyFEOynu7GueFNUudnb8oCT0wgjAdiZG2bf2yWhLvqu1ES1B_ZXBbJe9qjO9dCcIlrnl8hSy6KwRjZBHTzc-mFKaI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6292835767.mp4?token=PbboC04g31qrPokSefmMgz6qCt4COT57V_IBJkU7kCWVpZ6VN61oaLOY4nDBvjigeucM3fqE1-tVPBeKjgSxBhP92gyHW_DaN9DpO9XFOsCA9jcyEODQ64uvVvJ3koJwuNHjSj7S_6rFGEiQ6hJhYZYnn8GDYXtcnz8JMxXHZKs9StMMJVIvBkNeh2qy9nBar9PWNUta5Q_C8jSN4dXsSrT5Y2UfO28bBSUB2MW6IdrcGGvpMA2wD5oc9Zq4FJ3RrfpThp5SE1bQ0rlVyf2BDOK99q2lZ5mQfGb2zAM0r1rU8rQVhQDjGd1V551fUSbQmCoSA3_0nhGojADqtv6AMk3lUYSOi_3WVlcB50VNIVAcWnMtlyDSkK-X3DdKfkGy0qtT-91RHMXIWd4J7FsuH4J7ahBFUCYjdPtJry9d6kWzXd2XGdpAgBp-1s6DAFMWUyhuyyFMwbqIEp8pF9mIWC8Z3RoJeAlfBsV8lFfiOAHK7GRafWuTTtnzY3JSZJsXq1urBsUEjnteMtbRnI-iwozRGGJmwvr5zTleVWibdCFm9Gg8OAWXUvUDD0k0VYfgd5-fQytm99_fQrBQM0wyFEOynu7GueFNUudnb8oCT0wgjAdiZG2bf2yWhLvqu1ES1B_ZXBbJe9qjO9dCcIlrnl8hSy6KwRjZBHTzc-mFKaI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
سوپرگل‌های زده شده با ضربه‌سر رو ببینیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/107361" target="_blank">📅 11:55 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107360">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k5mkzlgld3SjUMnnEskg17rtsZvEmqP9YIcoIwDwr6Ayawu99gH12CmO3Bk9RkibNCsfRVOXOQRuF06kk-pwvW6jdLwjN9HjS5NYp1fxV4q1ZTJVAan3iCKwP7ccWvenppeFwpeLwqtDOa0B8h5x5vvcupIEHvOzeJcoLBBCWP4slUPD7WBxYBDpXmRQDfm6qOmqkPCnakt1v0wSo1-MIK2legfjuUIXbP4ZA7BsgMxDV_8wNIZVhPAdHJtkoyqCduQVGHsffylVU8IWgKSdFzQ6wkVWZ3dldAYoHH7z6noZ17ea4LmIZu6jpDGOr34lYEZyaJimzrB5VKU2trrA8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
⭕️
علی تاجرنیا: همه چیز برای اهدای جام استقلال تا قبل از بازی بعدی آماده هست و صراحتا می‌گویم به من این قول را دادند که این اتفاق بیفتد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/107360" target="_blank">📅 11:42 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107359">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d5bEyL7OGIhJiQYor19lkYdbIWv2wmnhL6JHUOnU0B52pO8oz0W-lRRmK9OpMlvLYSJSp3NwgH61IRpMyVBmxJLMqoejwQaGKc0kGpfMBjJ9wZucTq2Jb2WL0Rz_vWx-6SOtJSBKwLaqmAVlONmua4HrT-Q9PbGZaTA8LU1Jyvttg7VeFbRVa4Jey3tn8sMlvmMHN3FJ9qctLwKUfDUi7NFH1MfjN6KNIfP5Gy1L6Tzmg4_fBE-WAawAzE6mE3QPiZSWENbwRLFxFNibXZDIyTU5pp4BDFRxevlzBbfv6vHhGot2YU_Di6Owr6YtGlTOJ8IMr-7MFFiKhwZb9mWzaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
لیست محبوبان و مغضوبان امیر قلعه‌نویی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/107359" target="_blank">📅 11:32 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107358">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/184858d60e.mp4?token=FJKoSdhGNgbgGAGLkEBkuRKOis2rIeEgkYbSFH4O7BPLIr9dOj5QX8JE1Kt0mxYCASci6oyBUvb16cMO5YIDenc0RWn-nRseVxkk2XBdQKLz7nLCnoWhv9J14e6I5OogXyJKqMJkMWV_2xDD-eIpzWO27hO-OPyxan5sCViyBCJm53C_7w_jAol8F8uQXY8QG5SuRh3yhZRxasjggRPq55E5yPohjLhND-CfDnhsu95OXAhWawuflMF_WrMjnEhkHVcDJFRfEhsnleaLH_lSSlRQJlPBTSrRtvuSUnv77PzGQv6uHgP8pvUWGrw29x_Sl-pNkqWnTsLny3adPS1kYoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/184858d60e.mp4?token=FJKoSdhGNgbgGAGLkEBkuRKOis2rIeEgkYbSFH4O7BPLIr9dOj5QX8JE1Kt0mxYCASci6oyBUvb16cMO5YIDenc0RWn-nRseVxkk2XBdQKLz7nLCnoWhv9J14e6I5OogXyJKqMJkMWV_2xDD-eIpzWO27hO-OPyxan5sCViyBCJm53C_7w_jAol8F8uQXY8QG5SuRh3yhZRxasjggRPq55E5yPohjLhND-CfDnhsu95OXAhWawuflMF_WrMjnEhkHVcDJFRfEhsnleaLH_lSSlRQJlPBTSrRtvuSUnv77PzGQv6uHgP8pvUWGrw29x_Sl-pNkqWnTsLny3adPS1kYoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
به‌مناسبت عملکرد قلعه‌نویی یادی کنیم از این افشاگری تاریخی محمد مایلی‌کهن!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/107358" target="_blank">📅 11:05 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107357">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22f1db9d0d.mp4?token=h5n_zXjVD7KOv1e6fnax2exi_bGSsuMlVV8ac1YPRdxsMFxc0J9rH2DsuMH8CkHTcBEw-jQcd-9AE87juiT--LlEXLblQsc1mkuDTR2DwQWxxOKSgL31zoE-cuZjgt9UW4QcRVqZntE5jnyQXspj8RpwQLeUyk-5RLCPPD4nIH50LRvNZifN24xR5nNJVp7HUXQz_9avw3TuoIAi_tJgTaOuD4TNVuLk2xfgMc-iCfAwVN64z9A09l-MU4fPMoUz8nBi-EUrwk0MWbTjSF5tQHIsoCwQcoxaKN0O90cEQip16kziybj7EYk1JKyFRKB0K9eePuG649tT63mK9bzL5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22f1db9d0d.mp4?token=h5n_zXjVD7KOv1e6fnax2exi_bGSsuMlVV8ac1YPRdxsMFxc0J9rH2DsuMH8CkHTcBEw-jQcd-9AE87juiT--LlEXLblQsc1mkuDTR2DwQWxxOKSgL31zoE-cuZjgt9UW4QcRVqZntE5jnyQXspj8RpwQLeUyk-5RLCPPD4nIH50LRvNZifN24xR5nNJVp7HUXQz_9avw3TuoIAi_tJgTaOuD4TNVuLk2xfgMc-iCfAwVN64z9A09l-MU4fPMoUz8nBi-EUrwk0MWbTjSF5tQHIsoCwQcoxaKN0O90cEQip16kziybj7EYk1JKyFRKB0K9eePuG649tT63mK9bzL5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
❗️
سوپرگل‌های بازیکنان ایرانی در تاریخ به چلسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/107357" target="_blank">📅 10:40 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107356">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/805925ad6b.mp4?token=V-YdeVmk0yYZ2C2X4KZyBK4mfHCYBFmSchzBSxzuhPBFutua4iP_K-PNaNT2ynfS9SHVEcknwKgTQbEEAwJPb6C6fA9sdXyaiV8kQ-B1ycAc7OSk-BfRcBc1FRuvFNurxzL0_A0AMXLMxXTobBRZfSWx3fHtzOtH3dh7_ZoQadRZOgLTFyakYVNnrtFj45f32eb_3di_Ynh2ck5MWrMyE4w92MQ3aFrpw3woIhaU20CSHodDydeuGL7x4n__8hLV0Wd9J9L_BYoE3IyPoh-mhY1pmFE4HM5oxl7PELuHdT4n_DJVF0lyxtRfYVdVQsJpy3Xgv-ok8H41Tvsi80eHHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/805925ad6b.mp4?token=V-YdeVmk0yYZ2C2X4KZyBK4mfHCYBFmSchzBSxzuhPBFutua4iP_K-PNaNT2ynfS9SHVEcknwKgTQbEEAwJPb6C6fA9sdXyaiV8kQ-B1ycAc7OSk-BfRcBc1FRuvFNurxzL0_A0AMXLMxXTobBRZfSWx3fHtzOtH3dh7_ZoQadRZOgLTFyakYVNnrtFj45f32eb_3di_Ynh2ck5MWrMyE4w92MQ3aFrpw3woIhaU20CSHodDydeuGL7x4n__8hLV0Wd9J9L_BYoE3IyPoh-mhY1pmFE4HM5oxl7PELuHdT4n_DJVF0lyxtRfYVdVQsJpy3Xgv-ok8H41Tvsi80eHHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
سکانس‌جالب و وایرال شده از مرد سه‌هزارچهره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/107356" target="_blank">📅 10:15 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107355">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">‼️
⚔️
برخی از لحظات خشونت دیگو کاستا ستاره سابق چلسی و اتلتیکومادرید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/107355" target="_blank">📅 09:50 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107354">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mnLge9sOnwajCaqelv5jEFqJLpSHf-gjXxZY3u0w3qWEhKJ2rpjhmeVA5qM_Pfh4cz7W-31kh5hsa9miBTQsVEwoJh2GKiZAiOOQmluJz2d_KW9OBLxDWFZHJ_rZAsl1-WdHp1UM3gE8kIvaK-eNFyI9aaqPXgkip6BsqDjHqFZXzZHO6PQlh0-GjKRttMX2W8vxNixwaoqb3rOiZQx4KFCHSW8LVy5EDuytF0B7L8LKGypzFytcC4n-G027_vVicx1axwGcucjC4NhmUGg_Xx7nEAiXi67h3rVoFtLEqITJfz8LRsl8pa38Z8GWHFwXCEEkn2hc0uLn4WFSQzURPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
📊
ضعیف‌ترین عملکرد‌های تاریخ رونالدو در‌ پرتغال که بازی مقابل ولز در جایگاه دوم قرار گرفت!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/107354" target="_blank">📅 09:25 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107353">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8bc355e5eb.mp4?token=MSDKMW8dTO5HP1xuD3NJvzU_wDErM4e6LOMcqrOZ8uV10vySXfeOZ_z7-_UqIbHJmgdkkmKlL2Bs7GH50FTRqIVNMu6qFTGbJrCha8YIP1N6czrzAelQgUdjEMALTM5UAE0VBIkc-r4cR-FaWMjNGVINvQHhkGIvL8dlYpOViKFYN7XXh-aVb4zA4eKUvznRqYBkVWkmvewllDG8XWqFCrRbzDsiE23uXuPdGIypcE8Mi2JFHa8wEFxBTjLPXYtqTuBKsbvCDKFOX7CjU5cEA57RZtQrMo-eJPeUDDWec9gd1Uy-cr4O_7crCBtteGrzdFwITJAqCDO73gTkhl_dJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8bc355e5eb.mp4?token=MSDKMW8dTO5HP1xuD3NJvzU_wDErM4e6LOMcqrOZ8uV10vySXfeOZ_z7-_UqIbHJmgdkkmKlL2Bs7GH50FTRqIVNMu6qFTGbJrCha8YIP1N6czrzAelQgUdjEMALTM5UAE0VBIkc-r4cR-FaWMjNGVINvQHhkGIvL8dlYpOViKFYN7XXh-aVb4zA4eKUvznRqYBkVWkmvewllDG8XWqFCrRbzDsiE23uXuPdGIypcE8Mi2JFHa8wEFxBTjLPXYtqTuBKsbvCDKFOX7CjU5cEA57RZtQrMo-eJPeUDDWec9gd1Uy-cr4O_7crCBtteGrzdFwITJAqCDO73gTkhl_dJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
آیت نوری مدافع سیتیزن‌ها تو بازی الجزایر مقابل زامبیا از دستور کادر فنی برای گرم کردن خودداری کرده و به همین خاطر از اردوی تیم ملی الجزایر اخراج شده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/107353" target="_blank">📅 09:01 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107352">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1e5fa478dc.mp4?token=jtAEAoIB5dJ1bskmW0YwTK1lYcKSLDYDgNdUBmlxqDw9rGPJqp-T-Dk84zBsFr2upY4FA7KGcmJP0dOaUWCMz0m9-UjfE5F-HO8h3wEHqPgQONQS3L6zrZpXBG4Nj98D4mDj9M3C2ljvlNHyhaFgDtSsovBPPIqxcC_DpS8Kye5IPgv3HpzXNlG0O9A9GehvCHuKztsVRXHEvNbZcwQbvfHqIyF01iAIEz2L3GWDjNMr_oaCgaX4Ufn9zz1z3XQprOnm1vCzdFwl19eYI_mwWMp37vU5ZCTHKf-BfY5CEH8ic83zNN9GaVGdQhiqGCrr3Z2u6jTMdbfjWLaTJFaBjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1e5fa478dc.mp4?token=jtAEAoIB5dJ1bskmW0YwTK1lYcKSLDYDgNdUBmlxqDw9rGPJqp-T-Dk84zBsFr2upY4FA7KGcmJP0dOaUWCMz0m9-UjfE5F-HO8h3wEHqPgQONQS3L6zrZpXBG4Nj98D4mDj9M3C2ljvlNHyhaFgDtSsovBPPIqxcC_DpS8Kye5IPgv3HpzXNlG0O9A9GehvCHuKztsVRXHEvNbZcwQbvfHqIyF01iAIEz2L3GWDjNMr_oaCgaX4Ufn9zz1z3XQprOnm1vCzdFwl19eYI_mwWMp37vU5ZCTHKf-BfY5CEH8ic83zNN9GaVGdQhiqGCrr3Z2u6jTMdbfjWLaTJFaBjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
حجت کریمی: قطعا انتخاب سردار آزمون در ایران، تراکتور است. به هیچ عنوان دنبال جذب اوستون اورونوف نیستیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/107352" target="_blank">📅 08:04 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107349">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UMWFjvTTKJd_FBIEAhRmseedcvx1MidYpHFcs12aT6u85GxzIr02Cl0kH5DFCtAOR12uRgZFzbcRmHk9y0CD400fzZ0trTBquj_Y1DRixiaY_yNRtECBcUd9QhsHYLglzFPsBV6Sc0tpLt223EcTtM2Q0N0tEFI2CI3_iAI2ErxyXDM22RwiQSnO4BoQeYNJVPS-f_1l7Y_qqWXJH9DCj-PhVeeSkF-0GiijzEGZ3K_fp363GJuVvj3sMnVVl40_GF9Tgjc7JFiA_L0BxIvpaDkN5sK5QEmLuj-5OMFtlWENwo7jwIUGn44Bn6KBCTw9jeePdMMkVAMCVBwyBxL0wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
گوگل رسما ایرانیا رو تحریم کرد و از این به بعد مردم ایران دیگه نمیتونن حساب جدید جیمیل بسازن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/107349" target="_blank">📅 00:46 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107348">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tmizhpv4lg2YwUTXbTUOmMkwH7pL5XUtNgznlZTQ9HKa-X_YKlviZZJnhFJSqZfO5R_RZ9OJZrqKzkEBIIplpu9s6jUhX4f325HlzgbvfEOE04m8qM829p46KrMUx5VW5dGInmfpw9BzM0kW57gXNMi5yh3uarG0HEKJaI-dP8nw08--70RrAmT2ZJFJGJ0Qpjr7CFQ2lK9wiiCUEKGtdu3DlvPI_ZX4d6clVOfZfqO6NThtlnhwYDVhQkl6rNhhvYo0lccKcGlqyQiC6eCYjPFzhYt8BjWmZfboQ27irF1MmiBfTo6anBEi1N4Mqy3MaAM2yxa6Womdn4BRoMT-Zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚨
📊
🇪🇸
فابیان رویز تا به امروز هیچ بازی‌ای را با پیراهن تیم ملی اسپانیا نباخته است:
‏
🔻
51 بازی؛ 36 برد‏؛ 15 تساوی؛ 0 باخت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/107348" target="_blank">📅 00:31 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107347">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
🇪🇸
🚑
رئال‌مادرید اعلام کرد که ابراهیم کوناته دچار مصدومیت شده و مدتی از میادین دور خواهد بود. به گزارش برخی منابع، این بازیکن به دیدار ۱۰ اکتبر مقابل ویارئال خواهد رسید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/107347" target="_blank">📅 00:28 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107346">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KA9VK7I0cDM5QMx-ZYSSZjenN4jTFUnV3luZNFOFWq56ggI_O7c_4qpiB8OJE-VQeiYn9ilWKX0ciR7bZRnmFXKc6mZUsJ8fUJ_pJtaqh1BLNyawMRaP2zik4QnOv7VZXYwXQbWuB3zyY55X_c5Oz6wXc3rZdUbNCAGz86NuXAu1NUW5qdHPZHozGgxKMxF8MaUlOl3jT7X_GXFO1jRCw16A8gbgXmXvE6yWgEfJhsCql75g8Xj446vqe8sg4NaZlIuBmfMmjUoIZCBl9F5Ekdw_mB_oKBlfvrjaC0cTaSeB1A7mSr8FHwbT_f0YQMHTN9uZJKRUVQLHs-HdcnnvTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚨
📊
طولانی‌ترین روند عدم شکست در تاریخ تیم‌های ملی:
‏42 مسابقه —
🇲🇦
مراکش [2023 و 2026]
‏39 مسابقه —
🇪🇸
اسپانیا [2024 و ادامه دارد]
😳
🔥
‏37 مسابقه —
🇮🇹
ایتالیا [2018 و 2021]
‏36 مسابقه —
🇦🇷
آرژانتین [2019 و 2022]
‏35 مسابقه —
🇩🇿
الجزایر [2018 و 2021]
‏35 مسابقه —
🇪🇸
اسپانیا [2007 و 2009].
‏35 مسابقه —
🇧🇷
برزیل [1993 و 1996].
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/107346" target="_blank">📅 00:26 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107345">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d2YMpJZtSOlOI88FTqCAwLTztYS277j876lakNRwR_Fk_Ic2P1zHaZIPzCHfXsLVGcnbP7D7NISz3UNBgYoGBgllIEhlW0IY8ncFCOdFON1r_FKmhXOa2ctXuNuOzkA4TJRDe8DutcwT-x_sYGz27gF6KzHn9wh77E9ThO9E-FgL8Qd3DLEsY0PyzVSaS9xFphQccSbPRkG24wVnUFJsU9Ip8emQf2Im1Pw_y_yi_NqjbJQ9GMhtf7snT7jkDmMDNrgz5AtewRxfZf5gweyITIS1SqTwyzg5Pcktll3dKMlmUeD0Wlt-rwYKri3R3LEqd_iSsmteEa0HOAV842ju2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
🇭🇷
کرواسی در شب درخشش لوکا مودریچ ۴۱ ساله مقابل جمهوری چک به برتری رسید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/107345" target="_blank">📅 00:15 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107344">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZznGa4DCsVO4QMCmrogqt_8C7lXPvG_nVP8XgHdn0utgF2iCJiWqArkwV2e8vCpOA5BGCFec-2ZYrf26L3nnyGJ9iXfVOA-Y_63gXE078TgGbTfvjHNNPINBUkYC65FDYVvavpu3CL1quqUOYypHll8-qzV4oKO1Th6pD-eXtjJUZXwPTH-JcxBYf2Qa3V-98ual4fy7C75499PcPDT_QtafkEn2RfSN32P-60suJytUtMS5lTMMSHkGOYaW6it1xvGREF7lVI3LWHWitt8zbzKXMqDBbckxXQN-ETy_qWb0u4O7n81GL7mQrHfB3eZ6UE3LdAAz7l3pxwVOCn8zMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇺
لیگ‌ملت‌های اروپا؛ قهرمان جهان در لندن انگلیس را از پا در آورد؛ یامال بازهم ارزش خودش را در زمین نشان داد!
🇪🇸
اسپانیا
3️⃣
-
2️⃣
انگلیس
🏴󠁧󠁢󠁥󠁮󠁧󠁿
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/107344" target="_blank">📅 00:10 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107343">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/494ff796bb.mp4?token=pu6M6nqKp-0fxpMAbWAb6BYiY6b1441I6OCUwtmVEgEcXa5y7kwdv2zhMCuE-kDYcDJpTurxLqew6fMnu8GdwLP2bAjIc44PCAacd--xUpLXYsBA6JkAHVna6JrerrzikNIeD7oewiRP1ytGXmEFzdKR3cpySAGlgfDA6Azn_gdUNMndlQ_Gg9xtZZDq3A_7LNXxID3F-7yL7tdolXE4pLdF6m8kpkUguqdgDLLyJWd06ff4rro_qRTrQ63hzlI4fnNSPIXzleDCySoMlGnaO20agzxBGb8EVDN6Vh7tfAmj-mcUCBgfRV4xQrXjyO5vrsrn89WinGNitCjKMInPEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/494ff796bb.mp4?token=pu6M6nqKp-0fxpMAbWAb6BYiY6b1441I6OCUwtmVEgEcXa5y7kwdv2zhMCuE-kDYcDJpTurxLqew6fMnu8GdwLP2bAjIc44PCAacd--xUpLXYsBA6JkAHVna6JrerrzikNIeD7oewiRP1ytGXmEFzdKR3cpySAGlgfDA6Azn_gdUNMndlQ_Gg9xtZZDq3A_7LNXxID3F-7yL7tdolXE4pLdF6m8kpkUguqdgDLLyJWd06ff4rro_qRTrQ63hzlI4fnNSPIXzleDCySoMlGnaO20agzxBGb8EVDN6Vh7tfAmj-mcUCBgfRV4xQrXjyO5vrsrn89WinGNitCjKMInPEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل‌سوم اسپانیا به انگلیس توسط اویارزابال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/107343" target="_blank">📅 23:52 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107342">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">اویارزابالللللل</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/107342" target="_blank">📅 23:50 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107341">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">گلگلگلگلگلگ سوم اسپانیا</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/107341" target="_blank">📅 23:50 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107340">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a0a10c6d7.mp4?token=S_fQJFxhBGOENc-pZ3gW76r4y-526SD-E92cMaXgW7O_cn2UkjU5S0QPCc8CC0jZAGXDmqjssY7QPAnj5ZfQFTf6Fed2IkNR8T0sa9f4TXzHJhwlC_R3SfTb30bxLYjz4GUamBN2dseJRYyK8O4HUJQwnpp4BfpsHA0Uq5MljY9MUsQzPW0uKi4o5PV7KOtGq3Uc2SY65sKjaTgVfEYFsBM-KIQryhhIDB2G-NMZqKEdewHEYIk7DtjlJq-jRUK5ckLpfg9XRGYrCbku1RcWv4cjot5VjDAgzKqfse7UIFWUp7n974MJdO8GOE-NFUmmG22WtKHJdC4niMeTnPLZ9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a0a10c6d7.mp4?token=S_fQJFxhBGOENc-pZ3gW76r4y-526SD-E92cMaXgW7O_cn2UkjU5S0QPCc8CC0jZAGXDmqjssY7QPAnj5ZfQFTf6Fed2IkNR8T0sa9f4TXzHJhwlC_R3SfTb30bxLYjz4GUamBN2dseJRYyK8O4HUJQwnpp4BfpsHA0Uq5MljY9MUsQzPW0uKi4o5PV7KOtGq3Uc2SY65sKjaTgVfEYFsBM-KIQryhhIDB2G-NMZqKEdewHEYIk7DtjlJq-jRUK5ckLpfg9XRGYrCbku1RcWv4cjot5VjDAgzKqfse7UIFWUp7n974MJdO8GOE-NFUmmG22WtKHJdC4niMeTnPLZ9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل‌تساوی اسپانیا توسط الکس بائنا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/107340" target="_blank">📅 23:40 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107339">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ed28ae0d69.mp4?token=NXW5vfpPmaj9-vCDpdrvOMvEKDg5ix9okaaBy5DSdZ-_YKiP_LIrfZlvjPAwPNN0AohUTH2IbtI1XF0ItWMK0GvGGSqklOO-h6Uqt3rsM9gVhmlW5bwdWqfZEIbNmlueedEjCD_5mOK6YJnf0ucCUC5XyKZtyfffgNe15cNMrVfepSDh_FBgX5S8y-qcbgcc7mzjCWIiy1aIuLe-uCHjnF9bTWEl9a8vLaJ-8CGf2Mq2QJI359j5xRERpLpifGJtIZ7eG_b6OlM1m_T_kXfAsYn8u1Q6iAKhStdBy5e-HJAAraxLWPMnXdg9ZMgAjjrQe3Gp-xizHjBBF1tGqUDegQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ed28ae0d69.mp4?token=NXW5vfpPmaj9-vCDpdrvOMvEKDg5ix9okaaBy5DSdZ-_YKiP_LIrfZlvjPAwPNN0AohUTH2IbtI1XF0ItWMK0GvGGSqklOO-h6Uqt3rsM9gVhmlW5bwdWqfZEIbNmlueedEjCD_5mOK6YJnf0ucCUC5XyKZtyfffgNe15cNMrVfepSDh_FBgX5S8y-qcbgcc7mzjCWIiy1aIuLe-uCHjnF9bTWEl9a8vLaJ-8CGf2Mq2QJI359j5xRERpLpifGJtIZ7eG_b6OlM1m_T_kXfAsYn8u1Q6iAKhStdBy5e-HJAAraxLWPMnXdg9ZMgAjjrQe3Gp-xizHjBBF1tGqUDegQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل‌دوم انگلیس به اسپانیا با گل بخودی کوکوریا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/107339" target="_blank">📅 23:39 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107338">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/8bcae065f2.mp4?token=ZUfkbeQ5Jr1j4qBxMIikVj03TojOBEaDXdBVVnPqhWQELWu22hlXO9w6KZO9dpcA36ZiOVXVdA39S7WP5Zt21yEZdXqwuZr_EMcHWH9TSSvMN5pSr5K4ttXIG8dzFd7iOT--ETEDu5AdR_ZHIWge9YG-tH-RDQfnFEKyMsOWf4U6SFh_OEn_w61J2jjtyjKhMy6rsyRQE1rr4ursQzin3JKx8Oh_35VwCiDfrNXXJ3PmplvUrTO0Rh7BbaPzOucGRThb_ks5xcsVXUxtM-vG9VMkXVli4cgGbUScj2u7LfNdBf7S9xr0ChfEmjSovyYd2N3KhK8QQGr2IsszIn0vrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/8bcae065f2.mp4?token=ZUfkbeQ5Jr1j4qBxMIikVj03TojOBEaDXdBVVnPqhWQELWu22hlXO9w6KZO9dpcA36ZiOVXVdA39S7WP5Zt21yEZdXqwuZr_EMcHWH9TSSvMN5pSr5K4ttXIG8dzFd7iOT--ETEDu5AdR_ZHIWge9YG-tH-RDQfnFEKyMsOWf4U6SFh_OEn_w61J2jjtyjKhMy6rsyRQE1rr4ursQzin3JKx8Oh_35VwCiDfrNXXJ3PmplvUrTO0Rh7BbaPzOucGRThb_ks5xcsVXUxtM-vG9VMkXVli4cgGbUScj2u7LfNdBf7S9xr0ChfEmjSovyYd2N3KhK8QQGr2IsszIn0vrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل‌اول انگلیس به اسپانیا توسط گوردون
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/107338" target="_blank">📅 23:39 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107337">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚨
🇮🇷
⭕️
علی تاجرنیا: همه چیز برای اهدای جام استقلال تا قبل از بازی بعدی آماده هست و صراحتا می‌گویم به من این قول را دادند که این اتفاق بیفتد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/107337" target="_blank">📅 22:35 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107336">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c757a44e62.mp4?token=psj20BPVVA67RPLAM1RvON93uihmSZTvvpr-9dCbtHL2Qfyt7Cn2mb_8uhPF04Ucxp7AmI7wtEpAf0W_smQ0tI7aiVyfXLIqdJ_FZPXHaNpNLTudZo-fnIcJ-0zJIZSOi2H_MHP3_XMu8SQAATTVV2T9R6oFcJ-DK47ecs1TA2NQSqmFVNh3zpfCIFV2aA-lPJ5cpTiv286aXo-_y6yIjUbw15bgLid4jyOY12Rk6MVpxcr1CqepJe7aVDf57RS4a_rufcEFyvjiOEdPiHyuK1gavwcU8vrrKoMp_u31ElnUeswHgUBIFXaizqii3rMLIlxV8EiGGwO5KcmbzRPMrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c757a44e62.mp4?token=psj20BPVVA67RPLAM1RvON93uihmSZTvvpr-9dCbtHL2Qfyt7Cn2mb_8uhPF04Ucxp7AmI7wtEpAf0W_smQ0tI7aiVyfXLIqdJ_FZPXHaNpNLTudZo-fnIcJ-0zJIZSOi2H_MHP3_XMu8SQAATTVV2T9R6oFcJ-DK47ecs1TA2NQSqmFVNh3zpfCIFV2aA-lPJ5cpTiv286aXo-_y6yIjUbw15bgLid4jyOY12Rk6MVpxcr1CqepJe7aVDf57RS4a_rufcEFyvjiOEdPiHyuK1gavwcU8vrrKoMp_u31ElnUeswHgUBIFXaizqii3rMLIlxV8EiGGwO5KcmbzRPMrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
گل‌اول اسپانیا به انگلیس توسط لامین‌یامال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/107336" target="_blank">📅 22:24 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107335">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">اسپانیا ییککککککککک</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/107335" target="_blank">📅 22:22 · 04 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
