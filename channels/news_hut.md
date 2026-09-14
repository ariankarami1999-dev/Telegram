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
<img src="https://cdn4.telesco.pe/file/WygcAuCcEozahrsNiYhKU9OCl5yh_ztITpu-NnznMYi2Oc9ZKIgyMazgJ3MHYtOJdbtXRymoKLCh2NZvrFtyf3WItFSA2MgsaKuUSf0iU8oRnIyPH_C8iofPItrGh3E7wtKpN1Q4Qc4Q-lcvqPadrwNe0m7Fv6QNx-9l0LQ7F_ZPsj0WylvwmIM-4-F1TkiyJ6Z2zC-2-7YY_TXLHP1jTd1UtUHbwwVCuO9n4OIwBA83TSPuoPX7aB3ygnQmtPBdIrDEh2CIrcBlCL2FZoC7TNcEoi-_YM-uqCEnHa_b_z-V6x5K0JWqrc7juPdwMYAwpho4lNhJJRIy0Mj-rO03_Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 108K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-23 23:22:57</div>
<hr>

<div class="tg-post" id="msg-71641">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AMEtLvAVRW9t9Gxi9ORM61Dp7Mc7BA-dnJY4Cxr-2pD_egKR4_LkPqTmEwVvDYebPkU8MItiLL26QikxLtgyvwzBtmyPFb75eCIK4r_D5sfbX5moWG5BFuStVh_hcTGcEbeySN-WL4-v2JpnAUDyHxL79URtERVoRocrA36WtsjLOQZpfnu-f-QN75ye96Lk6wZzzPyAS7l0Lvb-LVRVNeFAsOveBzUeOSwf2aP1xGnvfO8FbV3QQncMJniL_G8wHTqomxVQ9HdgOt7X5TBX7uLOIskPQgOBZlHGz55-tRLNXX56KLorYGC1iaHM6763uYq17Q9Ii7xR4-hKDESdww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیروی دریایی سپاه پاسداران:
نفت‌کش غول‌پیکر «ال‌گایا» (EL GAIA) هنگام تلاش برای عبور از یک «منطقه ممنوعه» در جنوب تنگه هرمز، با یک مین دریایی برخورد کرده است.
تلاش‌ها برای مهار آتش بی‌نتیجه ماند و تمام بدنه نفت‌کش در شعله‌های آتش می‌سوزد.
سپاه پاسداران اعلام کرد که پیش‌تر درباره خطرات این مسیر غیرقانونی هشدار داده بود و تأکید کرد که تنگه هرمز «همچنان بسته و تحت کنترل هوشمند ماست.»
@News_Hut</div>
<div class="tg-footer">👁️ 3.28K · <a href="https://t.me/news_hut/71641" target="_blank">📅 22:59 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71640">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d776b60914.mp4?token=YZuISWFjPNzvGBkv4oImMszy2FsDuUKMo5VZqcfdOxTzQPbg-8Q5_CN3a2cHsmpvRN25byoGtD8xj0mpVkmvM6pHPIyF7nmKIocnm9ijdLj4mciq6bzF1WAQYbK9l6uT3bcu7hC9bckqimE9268U1FCai3wnl3hYCC5MToalm7M4wsmPJeqesvVIqZJs0V1bpudbtfohDlMdeUOo2Q0vFe0ujnufs0hk_QuBEkHHONXvts6B8wwPK3ZHo0QwlUfaCMv6Pauh18LSDYX3ADMgVzpBiOSLItGshz74ySyvXloL9wpA8ZWV1CCqoTU2_gqkGyKASs5OTPjdBusL-xCG1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d776b60914.mp4?token=YZuISWFjPNzvGBkv4oImMszy2FsDuUKMo5VZqcfdOxTzQPbg-8Q5_CN3a2cHsmpvRN25byoGtD8xj0mpVkmvM6pHPIyF7nmKIocnm9ijdLj4mciq6bzF1WAQYbK9l6uT3bcu7hC9bckqimE9268U1FCai3wnl3hYCC5MToalm7M4wsmPJeqesvVIqZJs0V1bpudbtfohDlMdeUOo2Q0vFe0ujnufs0hk_QuBEkHHONXvts6B8wwPK3ZHo0QwlUfaCMv6Pauh18LSDYX3ADMgVzpBiOSLItGshz74ySyvXloL9wpA8ZWV1CCqoTU2_gqkGyKASs5OTPjdBusL-xCG1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
حرفای یه آخوند درباره سرگرمی های روزمره :
سودوکو بازی نکنید اعدادی که کنار هم قرار میگیرن یه رمزه یه چیز نهفته رو آزاد میکنه
فضای سیاه سفید تخته و شطرنج هم شدیدا جذب کننده اجنه هستش
🎙
مجری:
اونوقت بگو هیچی بازی نکنیم دیگه
@News_Hut</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/news_hut/71640" target="_blank">📅 22:45 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71636">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/bxt0EQCo-qljsgizjuqdw7phKAME7cLi8bzL34_Lw-MxUHZ7J8T38SetEZ7ImTIA545aGv0MTy_z7UNpMkrfhVLMlHe7H_57Yk69YZcquhnLxF-N_q03Kg2aOzn1KVwjllfCg0N0hR8xQVXZ1_nMRQGBuU6boKYwLBRpx9tsZXOD67Jv_QyI66_YZs77KWAoqMITGDBQRaFyzAB8A04q-phhfpDDIFVTUlOVjfN1WIasT92DKiD5l9x3deQJ22UcdNzypaCOP2Ep4d1zKtI1OQx6XvxKWfArqqktc0ToxBDl22nMUzct3KHgLr7_WArlcoAXC_22KduIJjEJ5bbYBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Vo9MfpysCYX2Rn-IZDlq5CYtHezPBT8p2FKKzoV4cV6_SRfdp2jQ6lvEFydWg-x30McNBVAGPZLRRLYPKuUoe_VnlwtQsUKFQjJGzcbbLSYCyYd3PScJTojb-FRitivn9LOWLz6kVb-hj_G7bY6hb2_emV2deXPtUDpZmRNcRj5DRFzswseMxiY-gsAT08Q-H1qzjfLWiVPOfOtpiBQ0d4nLpS_W47QquEeSLdVm0wnUEla_HECHeHbu9C_AvXRKE9QEk3RvWh7FVohxySZCxhCGpPDU2s_nYAiGmEJSd4wLNOHgvsYEqQIAn3S8elfKaIvkai5m7-aByS6lZ_iZ6Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پیامکی که داره برای مردم ارسال میشه، از فردا رسما جانفداها برای شرکت در دوره‌های نظامی و امدادی، اعزام میشن
😂
@News_Hut</div>
<div class="tg-footer">👁️ 6.8K · <a href="https://t.me/news_hut/71636" target="_blank">📅 22:34 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71635">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22f9266483.mp4?token=bJ03AZ7_efJ91XVgIr-7fyMqReGTgNXAyKPDrfrgHylvDrqyV-vN3IsAILlOknHQQSTIKjdLqj0yfS9PlG6F8Ph3sEc6_clLy77-Lhm1MtOFWbOI-EBhz6zW8g5vlQeqr4ytwjf5YAtF_avSyqfNwNo0k1db8ouo9clNrN17lj3qnHA8QpdFz4s8-k2GaAIWn4MIyL8X5gdoLrtC9uuSn1ePlRADzDsrKazkn9Sn117eeTW1wxMpLXxHIhl0M1sRCQcmIhrfS-4s_oeNib7xushj_ffSXfLaL-26RgLLnZyQ0f7FU39uAVdkPzASbi8tHVXDyCYgBU7xfSCSMQ2ndA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22f9266483.mp4?token=bJ03AZ7_efJ91XVgIr-7fyMqReGTgNXAyKPDrfrgHylvDrqyV-vN3IsAILlOknHQQSTIKjdLqj0yfS9PlG6F8Ph3sEc6_clLy77-Lhm1MtOFWbOI-EBhz6zW8g5vlQeqr4ytwjf5YAtF_avSyqfNwNo0k1db8ouo9clNrN17lj3qnHA8QpdFz4s8-k2GaAIWn4MIyL8X5gdoLrtC9uuSn1ePlRADzDsrKazkn9Sn117eeTW1wxMpLXxHIhl0M1sRCQcmIhrfS-4s_oeNib7xushj_ffSXfLaL-26RgLLnZyQ0f7FU39uAVdkPzASbi8tHVXDyCYgBU7xfSCSMQ2ndA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
بنیامین نتانیاهو:
سیاست ما روشن است: ما به نابودی زیرساخت‌های تروریستی در «منطقه امنیتی» لبنان و رفع هرگونه تهدید علیه دولت اسرائیل ادامه خواهیم داد.
به دشمنانمان می‌گویم: اگر تا به حال درس نگرفته‌اید و تصمیم دارید دوباره به ما حمله کنید، ضربات سنگین‌تری متحمل خواهید شد.
هنوز کارهای ناتمامی باقی مانده است و به یاری خداوند، آن‌ها را به سرانجام خواهیم رساند.
@News_Hut</div>
<div class="tg-footer">👁️ 8.6K · <a href="https://t.me/news_hut/71635" target="_blank">📅 22:00 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71634">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y7k7CjUnQWFPTnRb5gQCV8e6QbSye-4wtiwkqaIAX3PAFuNjqlYWubrVPdNXOjpJUmzj4x8dTIqGpHnZyqMZ4xlafQwVuvCbWgKaVWHrdjhJrWYAv240sCTLW02TGrlImsOAJLJIbZ_8Ofm_uBvcbC9DimD_as_12zkJF3WvydlvgXBaKxEqnNbFgvBG_4xNU6yoFKUGFd3OG-23eBQWMoJ3pAZM7aDvdajaB_V_yx36759cpmd4WfAQXzTvwSstfDRc23mX56vWzeX-rOxR79vn6C_8h_vHWRdcPulf8ucFeLf6KDwbcgR9YTU_mPiLaFOxyUEGiRntMoqTRNCESw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
❌
🇮🇷
اسکات بسنت وزیر خزانه‌داری آمریکا:
وزارت خزانه‌داری «عملیات طرد اقتصادی» (Operation Economic Outcast) را با هدف قطع تمامی شریان‌های حیاتی مالی رژیم ایران و حامیان آن آغاز کرده است. به همین دلیل، من فراخوان جدیدی صادر کردم تا افشاگران اطلاعات خود را درباره کسانی که اقدامات تروریستی ایران را تسهیل می‌کنند، ارائه دهند.
خطاب به هر کسی در سراسر جهان که اطلاعاتی درباره این شریان‌های مالی دارد: این فرصت شماست. اگر اطلاعاتی قابل‌استفاده برای وزارت خزانه‌داری دارید، ممکن است واجد شرایط دریافت پاداش باشید؛ فارغ از اینکه کجا زندگی می‌کنید یا چه کسی حقوق شما را پرداخت می‌کند. اگر چیزی دیدید، اطلاع دهید.
@News_Hut</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/news_hut/71634" target="_blank">📅 21:15 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71633">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O4USVGQQ8wh6geSIohNIzunH9IHGvvBpVq07lyrGh_rRXQPOBvKFMqeg8qp3Kap0skgr3oIFDUuvSipRqOIW3lMqY4HdLJ7gtL48mkvPYO1BzyuNRl6paCaQ2875ccIIZbNAPqGP-pYZ5r887Vjmi2xMhh78sAwSpZU6g0cxu3IFvG9Et3Q6o5HmjsW3uoG6U-ye9ntYpEtOif6Carr8OtFVg438XeQH0EWsD7mY2carp8ihqER3X7X23DqRdvkdLILYH6-PPELdBQEUkMlutrO_6VwbeqY9umVoM_emfyohLBrbpN14gT1vfqVVCjaOVJFWP_9Rz9Gq2_GM015mwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث:
نفت در حال عبور از تنگه هرمز است.
کشورهای جهان — که هیچ‌گونه کمکی به ما نکرده‌اند — باید پس از پایان یافتن این غائله و فتنه‌انگیزیِ ساختگی، هزینه‌های ایالات متحده آمریکا را جبران کنند؛ و قطعاً چنین خواهند کرد.
ما این کار را بسیار بیشتر به خاطر دیگران انجام می‌دهیم تا به خاطر خودمان، و نسل‌هاست که چنین رویه‌ای داشته‌ایم!
@News_Hut</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/news_hut/71633" target="_blank">📅 20:35 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71632">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qSVoZlF1LlZnWROyvtLqR2XX9g1ExyS0Oeehj-T0vi6fdrR1VmIKYgS7nVMNDuEcq9lxutYbIppQ5Pv7_pQ3JiHKeS3D3jCJDbCfs4e4XEVm0CGJPLrKO5LM7NcCtkAFwHN7pVltTfn6eETY06LegrjmfuvxfJQgqfQRB09jY2kTGtZ7n83B218KfCXunapHIDd98wmKXaT9vNAbo360kCbebbsdg-juSudBj8NZ5JeOm07L86jKzrtDi4ev6-sV02LNJai7UjuwoXtxk_5JB1DXi-gGKECEH7tPJpa3azze7CYwokX9CextIZN5Fj68QlAwjT4IOIPQxznbGKRI2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث:
امیدوارم همه متوجه باشند که افزایش قیمت‌ها در سراسر آمریکا ناشی از عملکرد «جو بایدنِ خواب‌آلود» و دولت او بوده است، نه «ترامپ».
حتی قیمت نفت در دوران بایدن بالاتر از سطح فعلی بود، حال آنکه ما مانع از دستیابی ایران به سلاح هسته‌ای شده بودیم!
به‌جز نفت که فعلاً وضعیتی متفاوت دارد، قیمت‌ها به‌شدت در حال کاهش هستند؛ قیمت نفت نیز به‌محض پایان یافتن درگیری نظامی با ایران — که زمان زیادی هم تا آن نمانده — به‌شدت سقوط خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/news_hut/71632" target="_blank">📅 20:08 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71631">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eoupUfQCa6tfug5nINqMNv57_tdZHGiMNexruJSJdjPuGCLHGcKsYLZwNn-DUMScoxcEKvarOuDORAiV7FGG0c3KLZuPVV-s3p9Oz5iFlvZdxkkRkZ_JCcChmCumw0JZeXSG6Z5zQz9oRSbit2gUQvT-BbA5any0SEeTTiKHI8aeTHXj5DxMFLbIrfEehPqNLo203YnLGxM6BMayzdh_RtJEzlmOCq8F778ERNKH69NjTXLRifsddT7fFu1QuVKzo8Fs5e7jZMuNhZUyjKefAwMbeJb5EQ2WnAdZTm7wREJkgi_KzwxCpzLW93KVOgjf8nVB8TjzX5gT3fhz-MeW3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث:
من به تازگی گزارشی دریافت کرده‌ام مبنی بر اینکه ایالات متحده بیش از هر زمان دیگری در تاریخ خود، سلاح‌های نفیس و ویژه تولید می‌کند.
این سلاح‌ها روزانه به نیروهای ما در خاورمیانه و فراتر از آن تحویل داده می‌شوند. کارخانه‌های شرکت دفاعی ما به صورت شبانه‌روزی در حال فعالیت هستند و همزمان به طور متوسط هر کدام ۴ تا ۵ کارخانه جدید در مقیاس بزرگ می‌سازند!
تمرکز اصلی این تولید بر روی پاتریوت‌ها، سیستم‌های THAAD، تاماهاوک‌ها و سایر سیستم‌های موشکی استاندارد بوده است که ما در حال حاضر تعداد زیادی از آنها را در انبار داریم.
@News_Hut</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/news_hut/71631" target="_blank">📅 20:02 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71630">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🚨
تسنیم:
ایران بارها اعلام کرده است که به دنبال مذاکره برای رسیدن به توافقی با دولت ایالات متحده نیست.
ترامپ همچنان ادعاهای نادرستی درباره توافقی با ایران مطرح می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/news_hut/71630" target="_blank">📅 19:58 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71629">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🚨
🇺🇸
ترامپ:  «ایرانِ در حال فروپاشی، می‌خواهد هرچه سریع‌تر و به‌شدت به یک توافق برسد. این من هستم که تصمیم می‌گیرم آیا آمریکا وارد این تعامل شود یا نه؛ البته ما در اصل، با چنین ایده‌ای مخالفتی نداریم.  @News_Hut</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/news_hut/71629" target="_blank">📅 19:12 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71628">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cgt3dCQEOp8-kO3RgfzO4jGHzoWbnWRcxaMGiUg6cCNvHsvRxUxGUJDNHU7t1C78QsEDl1CVJEmgKKqphoug2aQo7tfSPjRtqmuPWBqfyMQKN7WRaoQfDdeGLx0Eiy1sn_nixbQHdkUtfG8SerO1eion4zXmhN6L2YolQIBBe23cwm8__FDaJF91XKtcfDI6mFXjqBchAcKlubxSX_YGJbbKXwrpgj5V3QyR_W92Ic7OARYeiRWUIwXF82R-panCX6P1WX0Li1A1j0b7yfJeqN26Nxi9DlzfJMCktnYIPzEm2TsG6VXh7-tAU6oJu-XN6ep7euPxqd1m8WUooGtrnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
ترامپ:
«ایرانِ در حال فروپاشی، می‌خواهد هرچه سریع‌تر و به‌شدت به یک توافق برسد.
این من هستم که تصمیم می‌گیرم آیا آمریکا وارد این تعامل شود یا نه؛ البته ما در اصل، با چنین ایده‌ای مخالفتی نداریم.
@News_Hut</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/news_hut/71628" target="_blank">📅 19:10 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71627">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/7f7efeeca0.mp4?token=sKsOEKf6MesSJtz1KUMS9if6uvAFYYCLCu2inubSU6NGQLsc_RzkmnFJB6GKCSbHmZz7IzmEylEdRkgBh4s8HCTvVM2b3UhzqRPczCV0hcP_2XitHVl_Xvn_aqgX9mfbtBqlCSynZd-B7ZiXK2b_6QBu5gcjMV0zjtTFZlMz6RnXXitiSdskRvkCSBGh02uiynENBqFchub40pXOhPd5uLzr_9XFiW_EQvhXIKpZ8sPg2UvSVRxpBfyVzaG_mIYodY_54pTY05dJIaSwnFb_GA_kpYg3iBZqniXDDcZnv2StpK0QKSp5CUX4ZnvWLAdbkaqQXkGqPgqIIuQcndcqOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/7f7efeeca0.mp4?token=sKsOEKf6MesSJtz1KUMS9if6uvAFYYCLCu2inubSU6NGQLsc_RzkmnFJB6GKCSbHmZz7IzmEylEdRkgBh4s8HCTvVM2b3UhzqRPczCV0hcP_2XitHVl_Xvn_aqgX9mfbtBqlCSynZd-B7ZiXK2b_6QBu5gcjMV0zjtTFZlMz6RnXXitiSdskRvkCSBGh02uiynENBqFchub40pXOhPd5uLzr_9XFiW_EQvhXIKpZ8sPg2UvSVRxpBfyVzaG_mIYodY_54pTY05dJIaSwnFb_GA_kpYg3iBZqniXDDcZnv2StpK0QKSp5CUX4ZnvWLAdbkaqQXkGqPgqIIuQcndcqOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ رفته ایرلند و چپای ایرلند هم برای اعتراض این حرکتو زدن؛
@News_Hut</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/news_hut/71627" target="_blank">📅 19:04 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71626">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71626" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/news_hut/71626" target="_blank">📅 19:04 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71625">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SmQkFJkRe5LWxwm6MvnTs-IJ1E0Wxbrupm2bPP99PwjXbKIERdjOoN9znp5IKFLzrERbfhMswcgiP4WcnNRYWG99KMnrceV18leFnasOS0MR2kafd8Umr5KwXuq5UfSftRlo0scw1QMY1VH-saTQEPFWn6x20Hr2mgM2pB3qbt7ogIfwW5DuSGW-O4csyyJJxNkWgCGdnnMJFPIwy2msVmgL7lDRwj4nRsn91hd8i-gEDT_m0WibCeFVQJ2jOkkUHqxWBiA6j_N-WnR1dPQqFoq0qk9yzUQZoMZdvCr1LvX8v37vz4WTwHM1we4tk-Z6XtNCe5NDQ0COul8mRx9-WQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
شب بزرگ فوتبال آسیا !
نبرد هیجان انگیز
⚽️
السد
🆚
استقلال
⚽️
را در
TrexBet
پیش‌‌بینی کنید!
📉
نگاهی به ۵ تقابل دو تیم باهم:
⚽️
السد: ۲ برد، ۳ تساوی و ۱۰ گل زده
⚽️
استقلال: ۳ تساوی، ۲ شکست و ۶ گل زده
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
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/news_hut/71625" target="_blank">📅 19:04 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71624">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N9hTaQzWvXPzyy1LLLkjhjRnRLiMhDm0uYQxKxxfwnhC7QrepdyVUAMkxRFZBn1bNNhGyutyUGJ9D4O1GxcrGbxE9UtoH6H2QoUce_z6Qxxw7QV3h_skXOTi7kzgm0zHSLDKmlthqysv_L7rcwnzvtPL-OmTR5Q3B-lHLwFFREyIVzKS7pOyxjbGKO_YqXiWaj-mJf8eg7ESF-iuVBWbyfiiTKxBKNPiN6hMooLQJb67EnlbaSlfwnSpC2x6jPhSNDj9IpnOFqkbiC1fhljh5mKsO9Ag4vz-vUgKxBN9EHZJs_LcRwWhkxmjQaEWh3rfH_XVb7BJLeRtgdIt9OMcWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇺🇸
پرزیدنت ترامپ:
اوکراین موافقت کرده است که به تأسیسات انرژی روسیه حمله نکند؛ روسیه نیز متعهد شده است که همین کار را انجام دهد!
افزایش قیمت جهانی گازوئیل عمدتاً ناشی از جنگ روسیه و اوکراین است، نه ایران.
@News_Hut</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/news_hut/71624" target="_blank">📅 18:39 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71623">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🚨
دقایقی پیش چندین انفجار سنگین در چابهار سیستان و بلوچستان رخ داد.
@News_Hut</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/news_hut/71623" target="_blank">📅 18:35 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71622">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🚨
🇺🇸
❌
🇮🇷
ویدیویی از عملیات نجات افسر تسلیحات ملقب به "براوو Bravo"(زیرنویس فارسی)
@News_Hut</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/news_hut/71622" target="_blank">📅 18:15 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71621">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ctcEcPGIehp7Kx4Je-u6VzKJejDoST3uZswmPdmBM38cC6naCeK-F79SRlM-6vvYYFJGWZPIGSOdIbOzzuMhFIr5ClCQzbi-f74SoSoEgRpJpRltCF4_k3XNiFXyZTSs6Jn5RK2luD0r9QX4-2se78buC9SjfDNoQS-4-cijyxLsHN6DVeUn0VsAiLkWb_ZS2Bq7Hl7BggDG0S1TuCa30RcJKV-st4CWjQTsHpEePgYYov3xDZPN2bkMDTXweNSE5PkXHR0UYmkn-W0sb5c1l0DtM5s7AhoRNP73NdUFB3e94Q7izhvPc7tsFCx5SY-N9WeVH3FeFa4crklNEKTFww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇱
نتانیاهو هفته آینده برای سخنرانی در مجمع عمومی سازمان ملل در نیویورک خواهد بود.
@News_Hut</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/news_hut/71621" target="_blank">📅 17:33 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71620">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/36d8765cb4.mp4?token=d1ZxyzES8ByhpN74Uv4BAmoh0OgVkWXBXmNHYUYf5DlVjJvYWlJDUiLqMcLNuquWz-qD6qDQYCv8h7VpW3tlOXKdUl3HHwitmoew30FsqfAWxI556VWZFu2G4NH3yHMWNVdrJIsQr8d0VNEb26zePxCOAy4AP2Okxni0xpVGKA6TAxQfqq_xXB-Bunrie00pFgqSWMJhj1R-tcPngCQQJaLP0t04s9txn1ycjicxjlcrf3BA_KY5ZHcls7q5H_KyI3GzFQFswDzQyB2erUZXscNnEy9oO-Dmfmml3bSwAhOlRHKYDSrNuLe28YFftg7xeqSzNc694OMlxY0Ie0tXRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/36d8765cb4.mp4?token=d1ZxyzES8ByhpN74Uv4BAmoh0OgVkWXBXmNHYUYf5DlVjJvYWlJDUiLqMcLNuquWz-qD6qDQYCv8h7VpW3tlOXKdUl3HHwitmoew30FsqfAWxI556VWZFu2G4NH3yHMWNVdrJIsQr8d0VNEb26zePxCOAy4AP2Okxni0xpVGKA6TAxQfqq_xXB-Bunrie00pFgqSWMJhj1R-tcPngCQQJaLP0t04s9txn1ycjicxjlcrf3BA_KY5ZHcls7q5H_KyI3GzFQFswDzQyB2erUZXscNnEy9oO-Dmfmml3bSwAhOlRHKYDSrNuLe28YFftg7xeqSzNc694OMlxY0Ie0tXRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇷🇺
❌
🇺🇦
یک پهپاد روسی «گران» (Geran) در بخشی از جاده در شهر «پاولوگراد» که مملو از خودروهای غیرنظامیان بود، سقوط کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/news_hut/71620" target="_blank">📅 17:06 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71619">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00f9fc5142.mp4?token=fiZKPsnoeh_oX4delG2EEZnwcnwXIqrp1nvX423vbh6zhhWmLjYz6lgcQeg8SxFelw9JZqME9MDvk9UPe_k_zOxVInCmDwNZKYXCbJYqs2fjdJXnnP2A4B6i4ICGkB2yiH_wD2CZVBSQ48UB8h1v87tvMfjzRuA54TxbTQQvrSIom6HcJ_sDIdunNzrIYy_MPAKOy2V8gtMFn8zQQ9MWDqfAINyUVAbHXdXae--UzurSwTO078iGmDQIv-jvIgmkmNvrfO9okCss5K7iX1YECH7UOhDoGdcObnILOf8ADhEhyVP5dXff28bAP57C2P4QJY-huNEY9cHQ2qGbFljleA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00f9fc5142.mp4?token=fiZKPsnoeh_oX4delG2EEZnwcnwXIqrp1nvX423vbh6zhhWmLjYz6lgcQeg8SxFelw9JZqME9MDvk9UPe_k_zOxVInCmDwNZKYXCbJYqs2fjdJXnnP2A4B6i4ICGkB2yiH_wD2CZVBSQ48UB8h1v87tvMfjzRuA54TxbTQQvrSIom6HcJ_sDIdunNzrIYy_MPAKOy2V8gtMFn8zQQ9MWDqfAINyUVAbHXdXae--UzurSwTO078iGmDQIv-jvIgmkmNvrfO9okCss5K7iX1YECH7UOhDoGdcObnILOf8ADhEhyVP5dXff28bAP57C2P4QJY-huNEY9cHQ2qGbFljleA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
برگزاری این کنسرت خیابونی مختلط توی کیش باعث شده صدای طرفداران حکومت در بیاد
@News_Hut</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/news_hut/71619" target="_blank">📅 16:35 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71618">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9cbffc3d5.mp4?token=QVNeShKHLR8pdQKUFTw11PWVwtIsYLKWdGUhi-xByGyqeieAm1fh4tGBhIJ_7iCh3CMMhWTx3sLv28dPel22KLtBVxKH9uwooFmO2xcdGmtaY-qA_r3cqdneM_JIVFqWQg106I4yo7R4_7u1f_UbeLdZamHYnWxPInLZAwfERJcJopPeqGNpgeltkhezQIsTtpOcjFIuSpmVUqD29TQpgRFuWChJqVe5D1skplmgHadMCvRfZ3QFA9tkdqHmNfJ6Av0eRfZvusmUdAyrnpnXvSIDp-zSNLG4UjbtaVdqfODebC0kRmoGjFe_h7AUjRaNyGg1Nc9YSJ3UG4w5osf4ig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9cbffc3d5.mp4?token=QVNeShKHLR8pdQKUFTw11PWVwtIsYLKWdGUhi-xByGyqeieAm1fh4tGBhIJ_7iCh3CMMhWTx3sLv28dPel22KLtBVxKH9uwooFmO2xcdGmtaY-qA_r3cqdneM_JIVFqWQg106I4yo7R4_7u1f_UbeLdZamHYnWxPInLZAwfERJcJopPeqGNpgeltkhezQIsTtpOcjFIuSpmVUqD29TQpgRFuWChJqVe5D1skplmgHadMCvRfZ3QFA9tkdqHmNfJ6Av0eRfZvusmUdAyrnpnXvSIDp-zSNLG4UjbtaVdqfODebC0kRmoGjFe_h7AUjRaNyGg1Nc9YSJ3UG4w5osf4ig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ و بی‌بی ترسیدن نکنید اقا
😐
@News_Hut</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/71618" target="_blank">📅 16:01 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71617">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2eadd25c0f.mp4?token=mmG8xpD-VOug-25w65dAxtHitzV5iVOWQMVYravxcecCBzERODGXOyxqPP6Tnniaz0y0kwMumYVywI7nLob9F6P3m1GjCtwc4Yl7_TMpN-8xZkeR6LGWNqeNhde6suT3ii5JsemNaxFbsXP24iOVwxq1-w5rF1Bn3-FMt-jhQfCimfenpN7aE7EAp_kPtDBX3laieSw-ZxSnDPNpnwPPpULHc0yPwCoXCr41i2wjG4Fo2_FskLz_T90036hBzN23eG-9GYto67VIf2MZK4DM3DcuvxQoWYNUaidUy-wq1ik0zZM2uvAtGc1ckBRaEfo0lSZKmdtQSUDI3GRrvVEBOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2eadd25c0f.mp4?token=mmG8xpD-VOug-25w65dAxtHitzV5iVOWQMVYravxcecCBzERODGXOyxqPP6Tnniaz0y0kwMumYVywI7nLob9F6P3m1GjCtwc4Yl7_TMpN-8xZkeR6LGWNqeNhde6suT3ii5JsemNaxFbsXP24iOVwxq1-w5rF1Bn3-FMt-jhQfCimfenpN7aE7EAp_kPtDBX3laieSw-ZxSnDPNpnwPPpULHc0yPwCoXCr41i2wjG4Fo2_FskLz_T90036hBzN23eG-9GYto67VIf2MZK4DM3DcuvxQoWYNUaidUy-wq1ik0zZM2uvAtGc1ckBRaEfo0lSZKmdtQSUDI3GRrvVEBOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
سرقت آیفون ۱۷ پرو ، در کسری از ثانیه در کافه ای در اندرزگو تهران
@News_Hut</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/71617" target="_blank">📅 15:34 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71616">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4caee63fca.mp4?token=TnZlxOln6nIz5ukeqhw6-MSHGRas2vYRPMetoZL8Tw5PtXa8e9wg8zpAV_VoLsUYdfXLCrUInpkL63Awzw7lLY9yn7DmzXk5n-zF-Wb1n9fJkItY9pxsrvxutcZaFkxM1dc93cgsTQfAPXDTbFEtgvQTKnQf7QC723IKA3_M2o96FboOks3rlogjiqddLlTFOJPj7stDMhfyg0qUJEe7Ms_I-6ftU2j5EwfHw0lJe_dTIjHcSafUVHrmxJT1AHCW_l_PvJweLwuzjguOU5S6cRyERLagfShYyn7C9R0YAPy_dwisfGwjegCoX2zbg82CXOy8uqsKp3IqAb_0qaQN6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4caee63fca.mp4?token=TnZlxOln6nIz5ukeqhw6-MSHGRas2vYRPMetoZL8Tw5PtXa8e9wg8zpAV_VoLsUYdfXLCrUInpkL63Awzw7lLY9yn7DmzXk5n-zF-Wb1n9fJkItY9pxsrvxutcZaFkxM1dc93cgsTQfAPXDTbFEtgvQTKnQf7QC723IKA3_M2o96FboOks3rlogjiqddLlTFOJPj7stDMhfyg0qUJEe7Ms_I-6ftU2j5EwfHw0lJe_dTIjHcSafUVHrmxJT1AHCW_l_PvJweLwuzjguOU5S6cRyERLagfShYyn7C9R0YAPy_dwisfGwjegCoX2zbg82CXOy8uqsKp3IqAb_0qaQN6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
در ۴۵ روز گذشته، ۹ آتشفشان فوران کرده؛ انگار در جهان، یک تغییر بزرگ در جریانه
!
@News_Hut</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/71616" target="_blank">📅 15:02 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71615">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c7aec3e1c.mp4?token=vc8aAvw7g8vFR7keZ14nctRzF3M2g00H3Gt-Yaav7MkyKU2ybXNnitdsWEVfCzWDr_EklrQqVJIyYfjNfAeSi9zLGyAWYBXtXVHjPNU6LdMlkPFY37E383FiAKJ_uz_JIB3WK5e2ytjRmeZr04JZ5_XYSn9wgbTMczI7Lh2CX9yfTZq90M3kP_8xUBm9JdV1QGRqcpArzDrGopJFtWkyvubUBrQXstGK6SJXftkSnqpuM70NIJolUL9CzURHGjRtsl9dzXefpKcJ4Ts0PKcYodzK1kwNyXrLPvR4VXFg-o-EMqesJCqXcuLcsuZ5zbriReKXcIcBZPyWrSsF1w0HpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c7aec3e1c.mp4?token=vc8aAvw7g8vFR7keZ14nctRzF3M2g00H3Gt-Yaav7MkyKU2ybXNnitdsWEVfCzWDr_EklrQqVJIyYfjNfAeSi9zLGyAWYBXtXVHjPNU6LdMlkPFY37E383FiAKJ_uz_JIB3WK5e2ytjRmeZr04JZ5_XYSn9wgbTMczI7Lh2CX9yfTZq90M3kP_8xUBm9JdV1QGRqcpArzDrGopJFtWkyvubUBrQXstGK6SJXftkSnqpuM70NIJolUL9CzURHGjRtsl9dzXefpKcJ4Ts0PKcYodzK1kwNyXrLPvR4VXFg-o-EMqesJCqXcuLcsuZ5zbriReKXcIcBZPyWrSsF1w0HpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
رادان:
ما امروز از قبل از جنگ هم آماده‌تریم!
تو حوزه مرزبانی، انتظامی و خدماتی آماده‌تریم.
با امنیت مردم شوخی نداریم، ما شرایط‌مون جنگیه، اگه وطن‌فروشی به دعوت دشمن بخواد ناامنی ایجاد بکنه، ما اون رو مثل دشمن می‌بینیم و باهاشون برخوردی رو می‌کنیم که دارن با دشمن برخورد میکنن.
دشمن میخواست چهارشنبه آخر سال 1404، همون مدل دیِ 1404 رو راه بندازه ولی حضور مردم تو صحنه، متوقفش کرد.
مردم ما فریب دشمن رو نمیخورن، 30 میلیون جان‌فدا داریم.
@News_Hut</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/71615" target="_blank">📅 14:31 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71614">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OycgADxJvm3xeKHGQbE_yHDoUjtLQ4iZvddirRnnYPWlFblW9y-pbIjhAbYhC1dC4CLQpiIjyLFug272yyijOxrWRK3FOk3k9WNSqyOa9fQPyZaTe9GASQOS-ZtHQByvXSqwzAFPdWelZqlhNln38o6XUAyCM2yei34KN49FT741QFKLPVkyHfiZvQ7XHroHMmb3BttUWmDIw-dAyF9mzcNivamRnQXQt2_ZEo_buHm0qbZmUmJT9Ni_Dl6RzUY2fFgdFPgDuPR-gtUIrIger7pVfAZScBrtZN9GWaquxSUd0KO1zfmC8BZr1Huy0gEdgaYnWZZf5S21D707TKs65g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖥
🇮🇷
🇺🇸
بلومبرگ:
پس از آنکه اتریش تحت فشار دولت ترامپ از ورود محمد اسلامی، رئیس سازمان انرژی اتمی ایران، به این کشور جلوگیری کرد، حضور او در کنفرانس عمومی آژانس بین‌المللی انرژی اتمی در وین منتفی شد.
قرار بود اسلامی روز دوشنبه در این کنفرانس سخنرانی کند؛ اکنون احتمال دارد نماینده‌ای دیگر از ایران در اواخر هفته به جای او سخنرانی نماید.
انتظار می‌رود کریس رایت، وزیر انرژی آمریکا، در این کنفرانس ضمن تأکید بر اینکه «ایران هرگز نباید به سلاح هسته‌ای دست یابد یا آن را تولید کند»، خواستار همکاری کامل ایران با آژانس و دسترسی بازرسان آن شود.
@News_Hut</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/71614" target="_blank">📅 13:51 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71613">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ec91c05b9.mp4?token=bw_UZOAp6VTlOXRmrolZI-kOd5pncvfE_vXuTCyjnJlEK__rrKB3PVu1JfI_eV-v4HdNAQH56Lm5iLJvzTM8O3K0FIV17uDubWnp9xEHQ5qjzv-eQB7RcN6mJq8_X-LVVEC2coD_PK4n0h1nXmWtzNTGKwR-KcUakdwl6tULR19RUYRDU8JzZIaqTPoctvvmnIUtEv297P5lv3966zBcD48W10O1cdPuicq38gXLrq8ndG74pXtkTnrbZyD4eXXTvBz8-Jw1NX3tjV95xb8n045cfUUpM_ZbSlFI5hnOU3nnhfxX1YW9KPMpok8L6coy9ESqjRtXWtrLjwNoMrBwNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ec91c05b9.mp4?token=bw_UZOAp6VTlOXRmrolZI-kOd5pncvfE_vXuTCyjnJlEK__rrKB3PVu1JfI_eV-v4HdNAQH56Lm5iLJvzTM8O3K0FIV17uDubWnp9xEHQ5qjzv-eQB7RcN6mJq8_X-LVVEC2coD_PK4n0h1nXmWtzNTGKwR-KcUakdwl6tULR19RUYRDU8JzZIaqTPoctvvmnIUtEv297P5lv3966zBcD48W10O1cdPuicq38gXLrq8ndG74pXtkTnrbZyD4eXXTvBz8-Jw1NX3tjV95xb8n045cfUUpM_ZbSlFI5hnOU3nnhfxX1YW9KPMpok8L6coy9ESqjRtXWtrLjwNoMrBwNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇳
سخنگوی وزارت امور خارجه هند در جریان سخنرانی مسعود پزشکیان در اجلاس بریکس در دهلی نو، با خوردن یک‌نفسِ یک ظرف آجیل — شامل خوردن، لیسیدن انگشتان و برداشتن دوباره از ظرف تا زمانی که کارکنان تشریفات آن را گرفتند خبرساز شد
😏
@News_Hut</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/71613" target="_blank">📅 13:14 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71612">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/567356c89d.mp4?token=BqTS8dMJYN5MIpiw4Rc1s9LHQuKEpS8J8pfFPFnOEhsC38UuFjG20bkErpWwTikFGmtscpjMUwWzLqXa7FXSJaYnX08RM_28T8kkGc44NdJoeekg1Rr90bXqTNxSoZdqYICEM0uGeh5QfmIPBdOAXxpF8PJICIE5Q6KnrL1Q2_ycBqHFmMeAeEE5MIGIp77LJld04hNOcNpHPaqMoayBD9gHMGxSB1wxQIgFrGbk3EXycB-gYss0HdW7ysNQfAB5NTaYkDi4gNuD_BRtwxlK7Du3CWsnjv_JAKQA1LFFlAdCvgJDWFqjPKu24lyPBgumQU6JT0p_0DaB4QG23hctUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/567356c89d.mp4?token=BqTS8dMJYN5MIpiw4Rc1s9LHQuKEpS8J8pfFPFnOEhsC38UuFjG20bkErpWwTikFGmtscpjMUwWzLqXa7FXSJaYnX08RM_28T8kkGc44NdJoeekg1Rr90bXqTNxSoZdqYICEM0uGeh5QfmIPBdOAXxpF8PJICIE5Q6KnrL1Q2_ycBqHFmMeAeEE5MIGIp77LJld04hNOcNpHPaqMoayBD9gHMGxSB1wxQIgFrGbk3EXycB-gYss0HdW7ysNQfAB5NTaYkDi4gNuD_BRtwxlK7Du3CWsnjv_JAKQA1LFFlAdCvgJDWFqjPKu24lyPBgumQU6JT0p_0DaB4QG23hctUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
اسماعیل بقایی سخنگوی وزارت خارجه جمهوری اسلامی:
توافق میان ایران و عمان حاصل هفته‌ها مذاکرات فشرده است و حقوق حاکمیتی هر دو کشور را به‌طور کامل محترم می‌شمارد.
از کشورهای همسایه انتظار می‌رود اختلافات گذشته را کنار بگذارند، برای تقویت امنیت منطقه‌ای گفتگو کنند و نفوذ بازیگران مخرب فرامنطقه‌ای را محدود سازند.
@News_Hut</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/71612" target="_blank">📅 12:48 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71611">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rD3B7HUyyDCamfdVArpMSVlCQOGzdjsLupxubGgscFwFZ_yScz7XsZnYWzk8SDC7SkmMVQA9tHUs3pMIro-sEyGubTpMKVubCtDQcqtXIDGX9OUaPvp91xv_XG66j46vFuJMjo-BDIbyWecWu1fBIN44Y7Q5IWGqGq7dzBUsZ_dFJy8urkkgHAsNFvVhe-kWGDZdCO46g-SwFFcUX5Lvq0LbNzfq7_D3UkoqxZW9JAmq2oNrOu9hCVm9ExuxQ3z_4N34OaO0L7CtMAbLbonIYT8JOs3rRbQFYX9cODdiJGQzoUinoyU6592GQC81DKMrTryFcF_lWyKEGYHktobCxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
یه دختر شماره یه پسرو که روش کراش داشته داده رفیقش، و رفیقش تو نیم ساعت این اطلاعات رو از پسره درآورده!
@News_Hut</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/71611" target="_blank">📅 12:31 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71610">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71610" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/news_hut/71610" target="_blank">📅 12:31 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71609">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/azrIIJ2QPp5N4ho5LghiC-iw2JX5jPK0ZDYjzbLH6VKFQbJfpbrH9v-iQB8hVRNA1JY_9nScb5irC_D50ctodfQG4Q96Qj9w21wj-RiLKGsIA2f5t5AguRddw5ZPlwnn0qkO6740t7cVO7MQ_7kNxhbpdmwSV382bnij4rN8YOZ7OaodlvXQ-y2M2ATvOVJkZ4Gkf6Y3VmwmDP0ruidlUUrDrjviPT0gzeJP7kTDsaXhe4Y25gm6WRr9HRmyfSb6RgXmvQ0eQD1-XGgk8D06tMm05usnPqqLS_xTOItF8YBb6S_Q2BEHkcf2ufLoo44DOyNE-0-rztqO-rcuKAP7OQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت بین‌المللی
TrexBet
نیوکاسل
🆚
لیدز
رم
🆚
تورینو
اودینزه
🆚
اینتر
السد
🆚
استقلال
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
انتخابت رو انجام بده و آماده‌ی هیجان باش!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/71609" target="_blank">📅 12:31 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71608">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/001bfae793.mp4?token=aTfHQ0gHkgUvpIN4K_F06BaQMUUcM3UMYCJ47M4u5q6xUO5_D8xnv0dLbiPX9XP9slSU1hdaSlUo3BKL6y6PSSOO5G8iTTkzQspV8QhsFtZrUI49UijujjSkBwbM8jOgvYr5wnGTsyJFmFJdLfjxvVXKolupcQE0KHb8E8cXOAoyVwqaNjKANBgv8sAGIVu0HXLrhckiaFDIR-PCLLH-C6WicRrRLmFza2zw2kc4Fz4QV70PV4SlIy9XfBPV2CRrASIETZcyfUiEjNGXqdeoyvkNMjeOz-4ldUZke42zz8S79UHroYOhMf7c562iDNWVV-Mc6bBxjTHuvI7SXRD-YA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/001bfae793.mp4?token=aTfHQ0gHkgUvpIN4K_F06BaQMUUcM3UMYCJ47M4u5q6xUO5_D8xnv0dLbiPX9XP9slSU1hdaSlUo3BKL6y6PSSOO5G8iTTkzQspV8QhsFtZrUI49UijujjSkBwbM8jOgvYr5wnGTsyJFmFJdLfjxvVXKolupcQE0KHb8E8cXOAoyVwqaNjKANBgv8sAGIVu0HXLrhckiaFDIR-PCLLH-C6WicRrRLmFza2zw2kc4Fz4QV70PV4SlIy9XfBPV2CRrASIETZcyfUiEjNGXqdeoyvkNMjeOz-4ldUZke42zz8S79UHroYOhMf7c562iDNWVV-Mc6bBxjTHuvI7SXRD-YA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🤡
مجری صداوسیما:
اصلا نگران نباشید اوستاد خوش‌چشم مجدد توی برنامه ها شرکت خواهند کرد و انقد پیام ندید و مارو نوازش نکنید که چرا اوستاد چند وقته نیست.
@News_Hut</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/news_hut/71608" target="_blank">📅 12:00 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71607">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f19ca22a78.mp4?token=JEOdp7KbZeSxgr9CyYfqh9KclQkLdwwJPxNX5-QMDtAT6Of8RC3v7dBfwklNblYPDY6COCUhNyqhOEAsVYIWN1VT-9HXXshaFs0bfyHMV9KJ1nsJsw3t_SsjF64pMarJjHj686k7VMck6VMWH0cpOnHVYP6_T7cEjF4yBd4OxHrTQRSM4OSnsSX1h0efWH5_WTBlSHrjPrc21JL8uZMhbznryJFQq7MfL5ilLxes5uCmqcziIGlptN6vYJAk5lEiRlGLUVmubMiR9NguQgpMdoBe1bTT_9rW_o2K7Cqf59RVtBhZrDMvZ9m_gcExAAP2nWIvoWocbyW3vbHSesFf6x_MJL0HN2OzVoEV_4z0Re1RUQN_fvy4ylxuBd85ite-5wghZM5LMnaxfRd4OtwncKnKP34DJsX1Nk5dGbVADIJL3-kh__SUlTFia_30HtkAIt4e1ksg1lKJtIoESCU2rjFobxl7SSYv6DHlTcv6rrsihc_APPVxqJbOVDW-cgawFjhQDVZl3JUWV6QbYBzuVeZ-UfSNPGwjIynXOjpoL2l8YVEXTaJdN4nvhZvt07oI6eLb4EC7W4dWKelmBBDEIbWLOnUO9s0tw3IZNG-klTu26p2J9HYAvp4Rlm_Ys9YG35ahdu2EuUu-nKpt_Fz5alBVBO_BW7FJ4ce7qo4Hoxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f19ca22a78.mp4?token=JEOdp7KbZeSxgr9CyYfqh9KclQkLdwwJPxNX5-QMDtAT6Of8RC3v7dBfwklNblYPDY6COCUhNyqhOEAsVYIWN1VT-9HXXshaFs0bfyHMV9KJ1nsJsw3t_SsjF64pMarJjHj686k7VMck6VMWH0cpOnHVYP6_T7cEjF4yBd4OxHrTQRSM4OSnsSX1h0efWH5_WTBlSHrjPrc21JL8uZMhbznryJFQq7MfL5ilLxes5uCmqcziIGlptN6vYJAk5lEiRlGLUVmubMiR9NguQgpMdoBe1bTT_9rW_o2K7Cqf59RVtBhZrDMvZ9m_gcExAAP2nWIvoWocbyW3vbHSesFf6x_MJL0HN2OzVoEV_4z0Re1RUQN_fvy4ylxuBd85ite-5wghZM5LMnaxfRd4OtwncKnKP34DJsX1Nk5dGbVADIJL3-kh__SUlTFia_30HtkAIt4e1ksg1lKJtIoESCU2rjFobxl7SSYv6DHlTcv6rrsihc_APPVxqJbOVDW-cgawFjhQDVZl3JUWV6QbYBzuVeZ-UfSNPGwjIynXOjpoL2l8YVEXTaJdN4nvhZvt07oI6eLb4EC7W4dWKelmBBDEIbWLOnUO9s0tw3IZNG-klTu26p2J9HYAvp4Rlm_Ys9YG35ahdu2EuUu-nKpt_Fz5alBVBO_BW7FJ4ce7qo4Hoxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ℹ️
باز و بسته کردن (مونتاژ و دمونتاژ) کلاشنیکف AK-74 توسط این بانوی روس
@News_Hut</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/71607" target="_blank">📅 11:30 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71606">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">‼️
اگه نیسان کشنده ندیده بودی
این ویدیو رو ببین تا ببینی همچی توی ایران ممکنه
😟
@News_Hut</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/71606" target="_blank">📅 10:56 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71605">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/48ed023bda.mp4?token=aP-xgjD48SCMFqMRyvGKJH31Rwd044StfkdmnM7eXQIiRf5E6qkNi2CPizdVyjukshM3XBVRv0eHV5nheniGpVw2U4Yz7hoVYJSCdjQ6B3a-DiJBCS5GwCrIFbe9ARvqIMa3dv9IVzdZwyn4uDQmo_K954Flqb2IlHdejUcsFjEU-sPG5Kgttcuy2bcx7PsJIGsHJwVrzuSIhmWGp2XcHReZjjvwS2GcVZUcSHVlw_6yK5CsthK_PN3B3St6SgfYLOqInzTov5qkrpNmNdNSudDNoZTlNXYAt56ZANORjobBKWM89fNFOncPXYaOFNqdo6CNHwuiW4ly0kWl-V0G-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/48ed023bda.mp4?token=aP-xgjD48SCMFqMRyvGKJH31Rwd044StfkdmnM7eXQIiRf5E6qkNi2CPizdVyjukshM3XBVRv0eHV5nheniGpVw2U4Yz7hoVYJSCdjQ6B3a-DiJBCS5GwCrIFbe9ARvqIMa3dv9IVzdZwyn4uDQmo_K954Flqb2IlHdejUcsFjEU-sPG5Kgttcuy2bcx7PsJIGsHJwVrzuSIhmWGp2XcHReZjjvwS2GcVZUcSHVlw_6yK5CsthK_PN3B3St6SgfYLOqInzTov5qkrpNmNdNSudDNoZTlNXYAt56ZANORjobBKWM89fNFOncPXYaOFNqdo6CNHwuiW4ly0kWl-V0G-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تست سلاح جنگی بر روی شتر توسط یک عرب
😳
@News_Hut</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/71605" target="_blank">📅 10:32 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71604">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69e312dde1.mp4?token=rzYgSS67SuHatGv6nG-BVSKBt6LPq6zhWCBYZIFlLpRl7MwM8YB-fnxsnlJZJL-vrQExRmuHAYBPqn6jtvwJ2mNDB7WWnBQepoqTpc3n4ZzawbvAwXPPhMFo3yjq6D6o1aVI2sRex2_4zcUTdbca9Rmo79K2oMRCH-YFt4c_4gDZvj10JEEjCwEHsVETBGABNUhbXAzxYHIqiRZJcDD0prdJys3G7gIclNLxxDw402Yt2kT0t8KWJpG5s-0BKHP5D07-d5BYq5tr_XQA2LtsgLP8DVj7CU0tNWfPrFM5bwVgO2VDObWf0pfmLbTpSsB2yn5PD9S5wIT3iC1a_uoviQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69e312dde1.mp4?token=rzYgSS67SuHatGv6nG-BVSKBt6LPq6zhWCBYZIFlLpRl7MwM8YB-fnxsnlJZJL-vrQExRmuHAYBPqn6jtvwJ2mNDB7WWnBQepoqTpc3n4ZzawbvAwXPPhMFo3yjq6D6o1aVI2sRex2_4zcUTdbca9Rmo79K2oMRCH-YFt4c_4gDZvj10JEEjCwEHsVETBGABNUhbXAzxYHIqiRZJcDD0prdJys3G7gIclNLxxDw402Yt2kT0t8KWJpG5s-0BKHP5D07-d5BYq5tr_XQA2LtsgLP8DVj7CU0tNWfPrFM5bwVgO2VDObWf0pfmLbTpSsB2yn5PD9S5wIT3iC1a_uoviQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
زنده یاد مانوک خدابخشیان:
تنها برگ برنده دونالد ترامپ این است که پرونده رژیم جمهوری اسلامی بسته شود. این بزرگترین پیروزی است، درست مثل فروپاشی شوروی؛ این را فراموش نکنید.
چرا او باید وارد جنگی شود که سال‌ها طول بکشد و دوباره در باتلاق خاورمیانه بماند؟
هدف این است که از خاورمیانه بیرون بیاید.
شما به اصطلاح آن دکه جمهوری اسلامی را ببندید، همان‌طوری که دکه کمونیسم بسته شد و همه فرو ریختند، تمام این‌ها هم فرو خواهند ریخت.
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/71604" target="_blank">📅 10:01 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71603">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🚨
🇮🇷
روابط عمومی سپاه پاسداران:
لحظاتی قبل یک فروند پهپاد پیشرفته MQ۱ توسط سامانه نوین پدافند پیشرفته هوافضای سپاه و تحت کنترل شبکه یکپارچه پدافند هوایی کشور بر فراز آسمان تنگه هرمز رهگیری و منهدم شد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/71603" target="_blank">📅 09:39 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71602">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">‼️
یه ایرانی رفته توی تجمعات حامیان فلسطین توی خارج و بهشون میگه <<کص ننت فلسطین>> یعنی فلسطین رو دوس دارم
😂
اونا هم بدون اینکه معنیشو بدونن دارن تکرار میکنن
در ادامه میگه فلسطین رو از حماس آزاد کنید
در آخرم شعار جاویدشاه رو سر میده
👑
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/71602" target="_blank">📅 09:31 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71601">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
🇺🇸
❌
🇮🇷
مصاحبه کامل و ترجمه شده افسر تسلیحات نجات یافته ملقب به "براوو Bravo" با برنامه Minutes 60 پیرامون عملیات CSAR که در ماه آوریل در عمق خاک ایران انجام شد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/71601" target="_blank">📅 09:03 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71600">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
🇺🇸
❌
🇮🇷
⭕️
تصاویر تازه‌منتشرشده‌ای که توسط برنامه «۶۰ دقیقه» (60 Minutes) پخش شد، عملیات نجات دو افسر نیروی هوایی ایالات متحده را نشان می‌دهد؛ افسرانی که با نام‌های عملیاتی «آلفا» و «براوو» شناخته می‌شوند و جت جنگنده F-15E آن‌ها در ماه آوریل بر فراز ایران سرنگون شده بود.
این دو نفر در حالی که نیروهای ایرانی در جستجوی آن‌ها بودند، در منطقه‌ای کوهستانی در جنوب اصفهان و با فاصله‌ای حدود پنج مایل از یکدیگر فرود آمدند. در این گزارش همچنین تصاویری از حمله به نیروهای ایرانی به نمایش درآمد.
آلفا» هشت ساعت پس از خروج اضطراری (اجکت) از هواپیما، طی یک عملیات پرخطر در روز که با مشارکت ۲۱ فروند هواپیمای آمریکایی انجام شد، نجات یافت.
«براوو» حدود دو روز در پشت خطوط دشمن باقی ماند. او با وجود شکستگی کمر و سایر جراحات ناشی از فرود سخت (به‌دلیل نقص در چتر نجات)، از یک خط‌الرأس کوهستانی به ارتفاع ۷۰۰۰ پا بالا رفت تا اینکه دو تن از نیروهای ویژه امداد و نجات نیروی هوایی به او رسیدند و وی را به بالگرد آمریکایی منتقل کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/71600" target="_blank">📅 07:52 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71599">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71599" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/71599" target="_blank">📅 01:46 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71598">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gs5VDHjEzI41xFh0t5Ndx3sC60CQHGxfKXIvmI8YfJhxS247RGsIKfwmNUA2tGT16HtDDZwS3guNC5CRms6JXk86o6OzvAcdbIzLWay74yMvp20hsNYXPNOHzPp49Ch-bBnTaKVO9chqzOrqBbJ1OKFxScp2X7-t9uKRiCiAcGEswpEoepTDPhwsJZXZ8EvZZaCaItrvtZbJ1K55m-7teptmp7j5B9KGuONu-ltJG3iPUDRQahvMGJo9fiZOiTD9rgaLdQYMhAwWcpEQfCufIk6CW9YRVqQM6BT3BMWlixE-ENla9cQpj7TJpuOC-SFtEblYcuqybiGWm5-Et1cp0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
آماده‌ای هیجان واقعی رو تجربه کنی؟
🦖
در
TrexBet
، دنیایی از اسلات‌های جذاب، بازی‌های کازینوی زنده و لحظه‌های هیجان‌انگیز منتظر توئه!
🦖
صدها بازی متنوع
🦖
تجربه‌ای سریع و روان
🦖
هیجان در هر اسپین
🦖
🦖
🦖
🦖
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/71598" target="_blank">📅 01:46 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71597">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b94dc744f.mp4?token=kJpw0uwLlgTVoS9kTNrVRFQlLp_j5osdICSWtBFRdm5vLIF65Wr-p8Co64Q8tVpe41AsCzQrvV5lm06jJbeDlxWVN0S81_r1IUU-vE-qwMjXpCfILkfpTglprcQpmAWcHSb-F0UUN7hKLX6XQ_mrZ57TcUziM9HpkH9Oj1gomnVkXQSIk2LJSVjBTCInpKoT1Ex9MisBXAjxlhrXp29Q4mtvoKdnfGm2zuBogJ1Toprsw6KaJGl4DGSHJ0p4k3JMvxkXtT3DVcz1ynPM3KNXaNfFyL7AVL1rCts5xn2JA_x-a692V_fGraG3LPqGIYqGbID8PPGaA5lEfutr4OTlKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b94dc744f.mp4?token=kJpw0uwLlgTVoS9kTNrVRFQlLp_j5osdICSWtBFRdm5vLIF65Wr-p8Co64Q8tVpe41AsCzQrvV5lm06jJbeDlxWVN0S81_r1IUU-vE-qwMjXpCfILkfpTglprcQpmAWcHSb-F0UUN7hKLX6XQ_mrZ57TcUziM9HpkH9Oj1gomnVkXQSIk2LJSVjBTCInpKoT1Ex9MisBXAjxlhrXp29Q4mtvoKdnfGm2zuBogJ1Toprsw6KaJGl4DGSHJ0p4k3JMvxkXtT3DVcz1ynPM3KNXaNfFyL7AVL1rCts5xn2JA_x-a692V_fGraG3LPqGIYqGbID8PPGaA5lEfutr4OTlKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
سپاه به طرف تنگه هرمز موشک شلیک کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/71597" target="_blank">📅 01:43 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71596">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pZisGzl6WolWFcsoCmKj-CkyjfABzleqXUFjmg6wXkIPxWAWkUcglpRLB8F3mU03YohXseR3GSZXOpLJnNiWoe0nVMhhqpCOxrLZzmDaOi2iLhvzpJ78ONRSymGttF-EOa0TyfQ8oHfLwio-zWcPJuSqMDmQ85onYwIlIaVQYsPH3XpfYh4MaG-TnK1f0ZoYbRVpIi3GfW0ZalQRVscZQgbDnQdC1Y5Rf2uyEev-A1AiAkxU5N1Hk7WqAhuE36PLFKOjC-m-RtUvdt9yxrHiwgQc_wc_DJIAxkiIirtMFyaztKpinS6EDBSPnuHhp82Peg4xCnsx6w2y0hyodKOOFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇸🇦
❌
🇮🇷
🇴🇲
باراک راوید:
یک مقام حوزه خلیج فارس به من گفت که عربستان سعودی اصلاحاتی را در طرح پیشنهادی عمان و ایران در خصوص تنگه هرمز ارائه کرده است؛
زیرا نگران بود که عبارات پیشنهادی عملاً منجر به ایجاد وضعیت موجود جدیدی در این تنگه شود که برای این کشور یا سایر کشورهای عضو شورای همکاری خلیج فارس قابل قبول نباشد.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/71596" target="_blank">📅 01:02 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71595">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5c7311729.mp4?token=OEFgQZgaIMAZGEfLkUa5ig9DcCZqw_xdhGzZrAe6bHt4D1YtMnSYnWUb-vU15BSnWNsTBfjd4lcM4Fhac9ippLYC9zUwT1mLDXibV16idfBYOx8yjA0MiKctSW87PFnsglJuxegDZCuQuKGbDzO--EamKYsybYs4oNwrHwShLKOciB17pUxGnVB0OKx4XzkA4j_eHAX8wcr-vCeV-PrpV_htPWImA0UkxmCZkS66Ph4Nvg4ZTwIJkaa3xOPLiS0z2LZNXgwYfKKZYSkn_k9jjZ9AdiCKls2qOrG7m_BAl7t8bj2K-430NxynUWg0GjsOx3cLfylESoeLeRdQJ-blrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5c7311729.mp4?token=OEFgQZgaIMAZGEfLkUa5ig9DcCZqw_xdhGzZrAe6bHt4D1YtMnSYnWUb-vU15BSnWNsTBfjd4lcM4Fhac9ippLYC9zUwT1mLDXibV16idfBYOx8yjA0MiKctSW87PFnsglJuxegDZCuQuKGbDzO--EamKYsybYs4oNwrHwShLKOciB17pUxGnVB0OKx4XzkA4j_eHAX8wcr-vCeV-PrpV_htPWImA0UkxmCZkS66Ph4Nvg4ZTwIJkaa3xOPLiS0z2LZNXgwYfKKZYSkn_k9jjZ9AdiCKls2qOrG7m_BAl7t8bj2K-430NxynUWg0GjsOx3cLfylESoeLeRdQJ-blrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار:
ایران می‌گوید دیشب به یکی از شناورهایش حمله شده است. آیا کار آمریکا بود؟
🇺🇸
ترامپ:
نمی‌خواهم بگویم.
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/71595" target="_blank">📅 00:58 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71594">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cjXNAsNK9kIPlaPl3gUBcmD_mVLPQ7oM2Mf9TK_Yzf2kfLu18bIHZlOv4WEfq_ulZyTFzKmYvtsHcNMonpafmbowGfEkHIX85qmheh9LIhWqne0ndKI3EqTlxQl1ZtOtuEkjVXeVpZu5cGbNK5SMAWFzabaOjO4li_NBQ_jlJm5WhzD3c7iIi5tysF1Vi0IiddsDyR-vLE225njU1JE7fL_KuKjWiIjhtFythdlyC0iM-oSB66S-Q38ZOBHPYu0Yf7ArLXYJK6a0-H88O9VFkmrEbXYHi-fZcczxvGE3ToUXA_iWqtYUa4-7tbksiuFikGtKwomrHAg7rxJP9ZE-KA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇴🇲
بدر‌البوسعیدی وزیر خارجه عمان:
در راستای دستیابی به اجماع، نشست منطقه‌ای که قرار بود فردا در صلاله برگزار شود، به تعویق افتاد.
ما همچنان به ترویج گفت‌وگویی که حامی ثبات و همکاری پایدار در منطقه ما باشد، متعهد هستیم.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/71594" target="_blank">📅 00:29 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71593">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
⭕️
نشستی که قرار بود فردا در عمان میان ایران و کشورهای حوزه خلیج فارس درباره تنگه هرمز برگزار شود، به تعویق افتاده است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/71593" target="_blank">📅 00:24 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71592">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AyR0sj-Jtvt13HxzwAiz-l-bSmkLcQ7rQOTsodt7ztl2xyS_GmN3AZp4Q5uGFUPt64Fs93Gmk2lKXOO55-4yAIh3CYI7gr3VqEI1KN9hlmm4BREELnNqRhsY3bmbW67hpNivr_GvLP1xg42mrpGc3ygfcnimKkyem87srMVv5qqtWp4h7qYZMiq2tdzU38htA79-EUFv9ue-U48B2cI2s3AAxNZFG-63t9fN29gR6rhXH-OGsdr1MK3BqT74SDEkOjBsA_qU-7E8X8rid4ajTtXsD7tpltoMRJEKu2q5S9W26iXw9_aWCFP40gTpO_BvNdsCdhsh6FeNZR5oRE9Rvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صحبت های عجیب پوریا بختیاری کارشناس اقتصادی در مصاحبه با علی ضیا درباره ابراهیم رئیسی:</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/71592" target="_blank">📅 00:20 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71591">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec76e7285d.mp4?token=KXYSY11i2kikyHJybMRgnfenTC9CIORXWfNkxI8jjtpVssfXwETflvyN9oUBjizWEh__AQ-aOIn500u9HkgF0Kes9IC2QwOeR7ThFZVwKxaS0y2bSpespU4PL4nAshTLq4zwi0N-9VmyF7LsqGrWMykbZ1wKRab3PcKh50u9EmQsAO2O-8W_zWCQ7hUMMVXbxPUyUVJhxli5fcjyqacmrTv76OrfizV575x-l6UlyHou7aFbpGT4GqelvWey_qDopGUYrt701j4EexZOKnXoLOh51y2l7P8SFgJujt2pwL2ctojWDqSdxfTJC8SU6EkFvOjYtLwTSeivVZoIkJWm_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec76e7285d.mp4?token=KXYSY11i2kikyHJybMRgnfenTC9CIORXWfNkxI8jjtpVssfXwETflvyN9oUBjizWEh__AQ-aOIn500u9HkgF0Kes9IC2QwOeR7ThFZVwKxaS0y2bSpespU4PL4nAshTLq4zwi0N-9VmyF7LsqGrWMykbZ1wKRab3PcKh50u9EmQsAO2O-8W_zWCQ7hUMMVXbxPUyUVJhxli5fcjyqacmrTv76OrfizV575x-l6UlyHou7aFbpGT4GqelvWey_qDopGUYrt701j4EexZOKnXoLOh51y2l7P8SFgJujt2pwL2ctojWDqSdxfTJC8SU6EkFvOjYtLwTSeivVZoIkJWm_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
ویدیو تبلیغاتی بانو سیدنی سویینی برای novig
😟
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/71591" target="_blank">📅 23:32 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71590">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ar1WSi0eweDPDr8EbUQIHMie7uUxgWh01XkjlHlyQnxVY1ZOQHmLpC2siZ8c98CeoO7jw9hCn_b2tkWYFTQHgLRaMbBv6Lvco3V8TAOYvRHWactN2CM5455_Gzqq5jPKlbW26hhH-dEkY91YI3IbSI1pz2JDYAJQulcgxEAxXidctkadm88PbXLJdnGEh50aUysq_OlKAal9t8XNuNGqho7TotvAlo2i80kFbJ4OBi-t5D8htDQc-qmIXiyIIxsA_gslha2qnRwRhe_sT_V4kIgM8a0Djkfs-Sa2gkKsuu9guCpriQjsJcOqmXGGMd4tswqlcgP2a9jctJovAuO2Iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇮🇷
🇺🇸
نیویورک‌تایمز:
مقامات ایرانی می‌گویند که رهبری این کشور طی هفته‌های اخیر بر سر دو راهبرد برای شکستن بن‌بست با ایالات متحده دچار اختلاف نظر بوده است: بازگشت به مذاکرات یا تشدید درگیری‌ها.
بر اساس طرح تشدید تنش، ایران حملات خود به اهداف آمریکایی - از جمله شناورهای نیروی دریایی و نیروهای نظامی ایالات متحده - را افزایش می‌دهد و هم‌زمان تلاش می‌کند با بالا بردن قیمت جهانی نفت، طرف مقابل را وادار به پایان دادن به محاصره دریایی کند؛ محاصره‌ای که تجارت ایران را فلج کرده و صادرات نفت این کشور را به صفر رسانده است.
ژنرال‌های تندرو، از جمله سرتیپ سید مجید موسوی (فرمانده نیروی هوافضای سپاه پاسداران)، طرح جنگی مفصلی را به شورای عالی امنیت ملی ارائه کردند. این طرح خواستار آن بود که ایران و گروه‌های هم‌پیمانش - به‌ویژه حوثی‌ها (انصارالله) در یمن و شبه‌نظامیان شیعه در عراق - دامنه حملات خود علیه نیروهای آمریکایی و زیرساخت‌های نفتی منطقه را گسترش دهند.
مسعود پزشکیان، رئیس‌جمهور، و محمدباقر قالیباف، رئیس مجلس، با این طرح مخالفت کردند و هشدار دادند که اجرای آن می‌تواند ایران را به جنگی بسیار گسترده‌تر بکشاند، موجب حملات هوایی سنگین‌تر آمریکا شود و بحران اقتصادی کشور را عمیق‌تر سازد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/71590" target="_blank">📅 23:05 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71589">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f02f69702f.mp4?token=H6lQOCMvqcVBmF6Xq00uW0_A9QalMeOZ0CqP_D5dL0HkKAnTf9uyS6k_xOdeQa9PxYK8OITXdsYlW1GSz6s62IGYZX1xkYLXBZ3BVQaoiJ3DUaL0_HDAmgOhc8tujRQ2dOKQyVPUfRId5WDS-2FuB0y9F3XJOGf8sFaYaxJ8j1rM4-TPggbpjpEP8KUlmWjXqhNhUb4GOINP-jnGCF_hiBr1LrZH0gQfwtU_GIq3ZH3KQmnAH_KaPKQjl-eQrutik2LXcxDZB33qXC1MGjtHDei-03rlEyjHR6WXPlxIrUREV1iI3WpsoKY5KrLud8ysE8VikOiyG8Qfkzd-wXDtbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f02f69702f.mp4?token=H6lQOCMvqcVBmF6Xq00uW0_A9QalMeOZ0CqP_D5dL0HkKAnTf9uyS6k_xOdeQa9PxYK8OITXdsYlW1GSz6s62IGYZX1xkYLXBZ3BVQaoiJ3DUaL0_HDAmgOhc8tujRQ2dOKQyVPUfRId5WDS-2FuB0y9F3XJOGf8sFaYaxJ8j1rM4-TPggbpjpEP8KUlmWjXqhNhUb4GOINP-jnGCF_hiBr1LrZH0gQfwtU_GIq3ZH3KQmnAH_KaPKQjl-eQrutik2LXcxDZB33qXC1MGjtHDei-03rlEyjHR6WXPlxIrUREV1iI3WpsoKY5KrLud8ysE8VikOiyG8Qfkzd-wXDtbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
کشتی که امروز صبح در نزدیکی جزیره قشم در جنوب ایران مورد حمله قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/71589" target="_blank">📅 22:15 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71588">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d18ae06116.mp4?token=vt1WH-u1ry6Ft7_y9BJBG2f5oJkUUvGz3jhakFDv4Cz0Pru7ZLOo-S4uq28-vpAJM0ORp10bO5lOwIHa1GJYnZoU9LJ2FCf9jDsgdL8HgDf3v48o4mZmtPbi-SIrZg9vfQEE8J8s4uMNIz2pf9hHE3lTXmrAuuHIoIOGC8YEphjZY4PZe-i4gfOSRWILeIbQVybHnB4gN2Sxm2-XCWgsSlAFru-9wCnR0_1xt-uSfVdl7FvTE74QQBmcG01EsckcN_cCaq8LAwFyACQN9ZD3lXTJmMfkAxSwn9CL5ViRqdl7aPTge3udfak_SXaKhMWBg1mQvsgwUps7arCThJgmaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d18ae06116.mp4?token=vt1WH-u1ry6Ft7_y9BJBG2f5oJkUUvGz3jhakFDv4Cz0Pru7ZLOo-S4uq28-vpAJM0ORp10bO5lOwIHa1GJYnZoU9LJ2FCf9jDsgdL8HgDf3v48o4mZmtPbi-SIrZg9vfQEE8J8s4uMNIz2pf9hHE3lTXmrAuuHIoIOGC8YEphjZY4PZe-i4gfOSRWILeIbQVybHnB4gN2Sxm2-XCWgsSlAFru-9wCnR0_1xt-uSfVdl7FvTE74QQBmcG01EsckcN_cCaq8LAwFyACQN9ZD3lXTJmMfkAxSwn9CL5ViRqdl7aPTge3udfak_SXaKhMWBg1mQvsgwUps7arCThJgmaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
زهران ممدانی شهردار نیویورک :
قربانی اصلی حمله ۱۱ سپتامبر عمه‌ی من بود که بعد از اون اتفاق نمی‌تونست با امنیت از مترو استفاده کنه چون حجاب داشت
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/71588" target="_blank">📅 21:31 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71587">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ezx5_pUbU18oJCbfiJjq3hkSRt5usjAY7IxgybZ8NQozNBmXR9y5O_dU6ZbXC256aWfKfdHD8M-teNDJtwudXXQ6I1R_cIVX2-2AWRK7CgbfuKcWYQ3f7rNbsV4ydJhlxka86PX-z41rALhAYnz3tQbHu85HvbSE2dlL_MC1r8otJMbtg42W1iGRFaPfuiWcjBDHzgxwshq7KRLdS2teESuwlzcXakpI2J_XrUZtYLijkIOR29I_OtYSeDC6BVD9R7N34b5lwihjVXIoeWs0EltLVc0qtzV6V3bZpGtsSxHAzsOU9GDcXVlWGHYNNpDgWjeRs9n9acy5egVDBExw4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🧩
🎮
کنسول بازی ps5 pro به قیمت تقریبا ۳۰۰ میلیون تومان رسیده!
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/71587" target="_blank">📅 21:04 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71586">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/643027f01a.mp4?token=q3JysQfe6kw-MNtXr7cbS-RQWrk5_duA-bkBeEi6xXR46WbAQuD0SmEI5OLIb1qSFkWcm2LVXaKGkFiXLybi4vy1g13rq1ZvUoQVDeL3hw8rilqoKddbuk_8755kq3lhnfZ3BFOcT2-NB0iLwBMUvyNq1lzcgLaFaDtxMqLqhsyQcRuuUjbWexW5GsI8nzEy8XDzczByZap_5byP9e_6PcQ56VBa_9H4KUidrnbU5VXHl92cjyL9Q4cp4OVu0sFp-x3pIPdOB1xxu6sciDQBpIn2YU6-9HpWXxlVtp_XLmdpX7VmUwEv0hjAEgvyohgy87AJE92kzPxoJXRzbN-3Jg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/643027f01a.mp4?token=q3JysQfe6kw-MNtXr7cbS-RQWrk5_duA-bkBeEi6xXR46WbAQuD0SmEI5OLIb1qSFkWcm2LVXaKGkFiXLybi4vy1g13rq1ZvUoQVDeL3hw8rilqoKddbuk_8755kq3lhnfZ3BFOcT2-NB0iLwBMUvyNq1lzcgLaFaDtxMqLqhsyQcRuuUjbWexW5GsI8nzEy8XDzczByZap_5byP9e_6PcQ56VBa_9H4KUidrnbU5VXHl92cjyL9Q4cp4OVu0sFp-x3pIPdOB1xxu6sciDQBpIn2YU6-9HpWXxlVtp_XLmdpX7VmUwEv0hjAEgvyohgy87AJE92kzPxoJXRzbN-3Jg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
مدیر سامانۀ هوشمند سوخت:
خودروهای نوشمارۀ بالای یک میلیارد تومان سهمیۀ ۱۵۰۰ و ۳۰۰۰ تومانی بنزین نمی‌گیرند!
این خودروها ماهانه ۱۱۰ لیتر بنزین ۱۰ هزار تومانی می‌گیرند
😐
😐
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/71586" target="_blank">📅 20:34 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71585">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🇮🇷
اطلاعیه قرارگاه جانفدا:
از سه شنبه 24 شهریور ماه قراره هزار گردان مقاومت ملی تشکیل بدیم که شامل کسایی هست که جانفدا ثبت‌نام کردن.
قراره به این افراد آموزش نظامی و امدادی بدن تا اگه جنگ شد، فورا اعزام بشن.
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/71585" target="_blank">📅 20:22 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71584">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75c23e20e2.mp4?token=AVxhyNE8J8cilXkNk1QdDsgFrCwNdwpN3wNHNqxZx3TrW37YLQ8tEDdUSBq4W_h_VtUqd0k8DC_UtbsAG2M-pYA5XmF6MKJotVXLp7fyfPrvuLJSgcodqrU-E0SxveSJRzq1ZeXHMWuNw08jj8gzWlniZG15tBQKiGx2Rfu35lzbZ7PAncF51mQaM2BLtFtK9h40ybvQdjFODXS3cJVP__SCxkmKRQVZgLsA4k8SL13PYVsEAbTy2o_B17zWzjok4C2FtUzHfUHNdISB3AAfZBqRvhy4I3WnjBRUqqtw7v43DzlSeUFdy7xJsBIQBRryoWn1vYoY-n3fQkVfroo4kYUOd95O7ztg_SssXMfU77Rir2r-qkujCD-5MAoOL9U5SmtPS_Jp9a02yVfuMfPZZqfxYWK12IdH9l5c13pnOd-EFWcLKkZAWm4tDql7Em_USuyMWMEAc_gr5OKlM6Xat-aQPNeFvgsNKj-bSSwW7Xpvluu9EbDNaOn8jYNGdpk7FjWKUlQWUhTb0V6ZYirA31n2snNI5rSXCUPG_kC-VQ6ISImiFYtzsp4N3LXiKTTnBK53bJ3xVZeyDC0v08FcTi5G0SPnJtS7hghbcJCGqWG1d4IQIefKLIwUOUW4ElxKLVQsmtzTvfvoQpmiq-NXYdBHG2DgbplBWLIW8U2zpv4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75c23e20e2.mp4?token=AVxhyNE8J8cilXkNk1QdDsgFrCwNdwpN3wNHNqxZx3TrW37YLQ8tEDdUSBq4W_h_VtUqd0k8DC_UtbsAG2M-pYA5XmF6MKJotVXLp7fyfPrvuLJSgcodqrU-E0SxveSJRzq1ZeXHMWuNw08jj8gzWlniZG15tBQKiGx2Rfu35lzbZ7PAncF51mQaM2BLtFtK9h40ybvQdjFODXS3cJVP__SCxkmKRQVZgLsA4k8SL13PYVsEAbTy2o_B17zWzjok4C2FtUzHfUHNdISB3AAfZBqRvhy4I3WnjBRUqqtw7v43DzlSeUFdy7xJsBIQBRryoWn1vYoY-n3fQkVfroo4kYUOd95O7ztg_SssXMfU77Rir2r-qkujCD-5MAoOL9U5SmtPS_Jp9a02yVfuMfPZZqfxYWK12IdH9l5c13pnOd-EFWcLKkZAWm4tDql7Em_USuyMWMEAc_gr5OKlM6Xat-aQPNeFvgsNKj-bSSwW7Xpvluu9EbDNaOn8jYNGdpk7FjWKUlQWUhTb0V6ZYirA31n2snNI5rSXCUPG_kC-VQ6ISImiFYtzsp4N3LXiKTTnBK53bJ3xVZeyDC0v08FcTi5G0SPnJtS7hghbcJCGqWG1d4IQIefKLIwUOUW4ElxKLVQsmtzTvfvoQpmiq-NXYdBHG2DgbplBWLIW8U2zpv4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیویی آموزشی برای دخترای موتور‌سوار چنل که قطعا بکارشون میاد
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/71584" target="_blank">📅 19:31 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71582">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gfEMw3onpSHWU28NJjczy2jhu2K8UEjgJ-3U7WIikJKEopfkOm6cu2Cl_fHLUCLaK7MmWAZRr9iyro5c9LryvWA2iWu6j5Tni1eR3kAdoBpI_u4_jJrM_mThhXCwRDrCZxXJnqSu9Aa4DLPMJl3i7nUaNJd9B4lRaw4pHkJWgRGGI3or0Etf4Ox9wGL-s6vBnKZho81OvcwmsB1udYQPenLlaMwxQ4DGQiW3uqG_39v5zwGFmWWio47SdpNeiAuV0rHdx81j_GAcXt-Ty3GIVPyxXqj8873SDzW3qTfmLHj2ZR85M8C77gtgf6ufazeBa-A4e_lPR1_4Pc0i7FKMuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/b5vStwuQbt37-4o3QKFA1HCEsLiMYjT0WLaVV_HDj2ja_tjF4M4jUnwdumr4BDI45sxRo6Qy6V4TW_Atfs8H7RU6FdTN9A0EcH_XbgATt8F3xdXDk6v65OVGcegoc9VRHnBgZZsHp6-3jHRlaGQi0S1vg_4ITRnChG9afZxQg9q7OKwURqvRcLPTGsaeQusoXvgej3MV4_Z6TBVw76pJnj-BeTVL_1pXIiNNOwnvl_JBCtsBZpG37AZ_7fA1B9Glzpdh9ZZKPyJUatSBGSqp9zCBVwNM4wPNuN91Es7XUngo3bSL9uy1lhuAVhchCuSRJZ_BFjjgaJPPZwQuVblybA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👑
دفتر شاهزاده رضا پهلوی:دستگاه کشتار و سرکوب جمهوری اسلامی بار دیگر قصد جان یک زن جوان را کرده است. سودا (مرضیه) ابراهیمی شمس‌آبادی، بلاگر ۳۳ ساله اهل بندرعباس، پس از ماه‌ها بازداشت و تحمل شکنجه، تنها به دلیل فعالیت رسانه‌ای، در بی‌دادگاه رژیم با مجازات اعدام روبه‌رو شده است.
صدای سودا باشیم و از همه ظرفیت‌ها برای فشار بین‌المللی جهت توقف ماشین کشتار رژیم استفاده کنیم.
سودا ۳۳سال دارد و ساکن بندرعباس است.
او در تاریخ ۹فروردین بازداشت و اکنون با اتهاماتی چون "عکسبرداری از فاصله دور محل اصابت یک موشک و ارسال این تصویر برای یک رسانه فارسی خارج از کشور" به اعدام محکوم شده است.
او حدود شش سال است که به بیماری ام‌اس مبتلاست و علاوه بر آن از بیماری‌های پسوریازیس، نارکولپسی و کولیک معده نیز رنج می‌برد و نمیتواند در زندان بماند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/71582" target="_blank">📅 18:39 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71581">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mor02-pMo1ythnvCidGgNo0BVu_R6RUtXId4_K2t3MPFkG7XsagCJoApYz1-BXAp5CYBNlZB9Vn9Ypq0EsLR2YYAE6PqnrmFLLAU9Q1qj0PS8LPn3v-kkwaQen2hQ31Ts3jJ6swFB2WtcKxW0verVnHmm9UJXTzJBrCLb9y2UKxKIcPN4Z1pqJpEvtxri6XXwy29WKfKcrai_Xgyd48Ncf4SwXFD-rv39fpQjO5NbgB9I25p6692WfiGHTdEBX_Ojx9ji15FAvoYNn0yLuT3SLjaPElE0XZYCzZ8U7wYz-nN7Zexpd9dzX7B1aZFWEQGQi0GSgaB-RQ7Rfafw3KunA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
🇮🇷
🇺🇸
نیویورک تایمز:به گفته مقامات ایرانی، تندروهای ایران با صدور دستور حمله به سه کشتی تجاری در تنگه هرمز در تاریخ ۷ ژوئیه، مخفیانه توافق صلح با ایالات متحده را که اوایل همان ماه حاصل شده بود، مختل کردند.
گزارش‌ها حاکی از آن است که مسعود پزشکیان، رئیس‌جمهور، احمد وحیدی و بخش عمده‌ای از رهبری ایران از این عملیات بی‌اطلاع بودند.
بازرسان رد این تصمیم را به جناحی مرتبط با حسین طائب — روحانی بانفوذ و رئیس پیشین اطلاعات سپاه که از همان ابتدا با این توافق مخالف بود — رساندند.
حملات ۷ ژوئیه منجر به حملات متقابل ایالات متحده در روز بعد و همچنین یک کشمکش قدرت بزرگ در داخل ایران شد.
تا ماه سپتامبر، ژنرال‌های تندرو دست بالا را پیدا کردند و به جای بازگشت به میز مذاکره، راهبرد تشدید حملات علیه نیروهای آمریکایی و زیرساخت‌های نفتی منطقه را پیش گرفتند.
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/71581" target="_blank">📅 18:29 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71580">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71580" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/71580" target="_blank">📅 18:29 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71579">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XytRX1L9jfHDSY5dX78_JiRiGNtlARTESv_wzM5QR8ZqQ9zfuUMuIZ7uMIJZFMfeP0E6ocGwp43Sa2fu0NbpYofFnQ4hr-UNQEJZn90rH7KobQIo2F4L1rc6W3bXsYkumZYqzrJYlGXsRc9WtL5ewQdoPe6ob0CoqCUSlBn-75RTrnzSCi3bd80ZRNZP2Ebh-BOzdFVwlk2cIMzUpZaX1sCTNNmEY-neMjnVKV8k8jufdAU4ZA-jV-YU0gCQZQ-uIwtC2j8FhpyUhd2NGyrKduP1YGwGDLoAFKbnK627iEY92PU6e7XrFDL6nZ7vSa2qb7hUATFDZo2Qrq2WlvCPsQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/71579" target="_blank">📅 18:29 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71578">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cfc5dc935e.mp4?token=t46RAolgLTdOIlAxWPu-2ldQZQQgIJzhu0U6aa44Fu9WgnGvVNigpYPviH7i7SJzDVhYPLuOWTFjzK1QMo1dWcigCzZDRK-HwBeb-YHKvnlTE5TW_aXjwTIjyU_vMv9De-xzpmbkMf1ab4dq1jw8Xbqzw_Y3lpfEk7R4jQLSRF3K9mv3nbGPzc98IGkFqGZi8_JeJA7jrlhriyjHJoe03dpyg6mRgB5m8xkYcp70WX7Q8cqdrbLWCvmXwN3fxgE_-yDWmHp0PcmUqyBTFVcxBCDzPJFcTgY23eaX5YKsRc6SBHjD0_Lv10RlBkPbfBDGondHT8IOSAcTM9_Cgv4cA5GFZdYn7orlps8MyO7byQcUI5Hz-SA1rqyYRPLHohZOezLCudKn9XhDFBvXbG5YGVitSwbfLBxthf4aqAg8RUQtlM7EkZwjsmX7I7w4Xs9xONkRrFFWQcE_AgYX524dIw9Uyc7BoSzVJ2v79Ea6ATGumTMpYXRtKvwrblvNjhkeLL0N3A6AT4DS4Y2m8Zi-OuoIYwvg-t8MZVk4ocWSuiMz3g1dJklOnKePpN6gZGXrGQYsUvnRyoBzAetkiH6VbB4zUoArM4kvoOi3nK5hAhPuwMggLRFnnyfG_G_xrygmsCNvvz2uCeUF_fRLp2V6E_xjptBtbu_QH87jEO6-6IU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cfc5dc935e.mp4?token=t46RAolgLTdOIlAxWPu-2ldQZQQgIJzhu0U6aa44Fu9WgnGvVNigpYPviH7i7SJzDVhYPLuOWTFjzK1QMo1dWcigCzZDRK-HwBeb-YHKvnlTE5TW_aXjwTIjyU_vMv9De-xzpmbkMf1ab4dq1jw8Xbqzw_Y3lpfEk7R4jQLSRF3K9mv3nbGPzc98IGkFqGZi8_JeJA7jrlhriyjHJoe03dpyg6mRgB5m8xkYcp70WX7Q8cqdrbLWCvmXwN3fxgE_-yDWmHp0PcmUqyBTFVcxBCDzPJFcTgY23eaX5YKsRc6SBHjD0_Lv10RlBkPbfBDGondHT8IOSAcTM9_Cgv4cA5GFZdYn7orlps8MyO7byQcUI5Hz-SA1rqyYRPLHohZOezLCudKn9XhDFBvXbG5YGVitSwbfLBxthf4aqAg8RUQtlM7EkZwjsmX7I7w4Xs9xONkRrFFWQcE_AgYX524dIw9Uyc7BoSzVJ2v79Ea6ATGumTMpYXRtKvwrblvNjhkeLL0N3A6AT4DS4Y2m8Zi-OuoIYwvg-t8MZVk4ocWSuiMz3g1dJklOnKePpN6gZGXrGQYsUvnRyoBzAetkiH6VbB4zUoArM4kvoOi3nK5hAhPuwMggLRFnnyfG_G_xrygmsCNvvz2uCeUF_fRLp2V6E_xjptBtbu_QH87jEO6-6IU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
ترامپ درباره ایران:
ایران به‌شدت خواهان توافق است.
آن‌ها مدام تماس می‌گیرند. می‌خواهند توافق کنند. اما باید توافق درستی باشد؛
من تن به توافقی که خوب نباشد، نخواهم داد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/71578" target="_blank">📅 17:38 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71577">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f46b70464e.mp4?token=E086XbFJxl3JQM2JociRuxa89KXT4BBoxn_7lSXZbWyTEUA-7LbADD2zhiO7zoWYzP6MK_GCcyrquBh-YFXR1xJTbWTair83qdmFWODWwn2_GaKgN7YX6FIFnB0yFwhNzew9avYoulONmYblUt3M2VOgdVwvE_9W81kTV9uTt5lHMMkhiQd_NQJkO8rwLCx6KVaNb_R7jNzk0aNZksJA8B1gB7g6EiOWa0bSmANpWFWPsjhpQjbRBoF98z-50_LApQXpDPHZTHgJzrcPHz99jhGO-tJjSWymLVpJzy69F2mqs8Oz4rdzc1ETRDh36SMmtJfT_I7e1NpfU0cOJur3aK3T4kzp3NQXA5eHaQx8u1PMVTs3fUSpL58ual9sZ8szgn_f9dvEQmuB68LNgq1EZwPksZtrWjhW0s3uC_zxYWoF35TK71bH0NXHOI4izPnfT1DxnyFmYeoE8v_3sntDT7sEpwGHoJjJRzvAha3XuYOwuqKqd94WmCmmN7ktMUHDvmPcr2b6VCpSm_RB1W4Q_n5EFz-p_CnXnQdaAsCpbWQzHyZmO8EwAjr8xa0YBJlzND3Gw4pxXL88OV3VSCwpohgZDAJooVCLNOtFUc912-q8nrCXeIFpp8TEEDXr9xBlx5MLazisDoxxGmjaH2LnW3r2UFEwhem8UszcqzNVdNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f46b70464e.mp4?token=E086XbFJxl3JQM2JociRuxa89KXT4BBoxn_7lSXZbWyTEUA-7LbADD2zhiO7zoWYzP6MK_GCcyrquBh-YFXR1xJTbWTair83qdmFWODWwn2_GaKgN7YX6FIFnB0yFwhNzew9avYoulONmYblUt3M2VOgdVwvE_9W81kTV9uTt5lHMMkhiQd_NQJkO8rwLCx6KVaNb_R7jNzk0aNZksJA8B1gB7g6EiOWa0bSmANpWFWPsjhpQjbRBoF98z-50_LApQXpDPHZTHgJzrcPHz99jhGO-tJjSWymLVpJzy69F2mqs8Oz4rdzc1ETRDh36SMmtJfT_I7e1NpfU0cOJur3aK3T4kzp3NQXA5eHaQx8u1PMVTs3fUSpL58ual9sZ8szgn_f9dvEQmuB68LNgq1EZwPksZtrWjhW0s3uC_zxYWoF35TK71bH0NXHOI4izPnfT1DxnyFmYeoE8v_3sntDT7sEpwGHoJjJRzvAha3XuYOwuqKqd94WmCmmN7ktMUHDvmPcr2b6VCpSm_RB1W4Q_n5EFz-p_CnXnQdaAsCpbWQzHyZmO8EwAjr8xa0YBJlzND3Gw4pxXL88OV3VSCwpohgZDAJooVCLNOtFUc912-q8nrCXeIFpp8TEEDXr9xBlx5MLazisDoxxGmjaH2LnW3r2UFEwhem8UszcqzNVdNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
ترامپ درباره ایران:
ماجرای ایران درست بعد از انتخابات میان‌دوره‌ای تمام می‌شود؛ شاید هم قبل از آن، اما قطعاً بلافاصله پس از انتخابات میان‌دوره‌ای پایان می‌یابد.
قیمت بنزین به‌شدت سقوط خواهد کرد،خب، من می‌دانستم چه کار می‌کنم و باید آن کار را انجام می‌دادم.
ایران نباید به سلاح هسته‌ای دست پیدا کند.
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/71577" target="_blank">📅 17:35 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71576">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a78bb4d113.mp4?token=ZYEaA_zy72juBDxQFiQRgtfaXat-5AN84kpq14HBv0cWTLsUJjZNIDxg-UUdsqdY1TMlQiw4KnMBYQ9FNKmM0qjRd0omNOlmOEKhnnlT7IoeTjtB-K4hY9YkHRtljsoEpXkQvykkkf8FUmenCUg-8m0htmu8s0aUGN19jlOF6X8CCyppAtzJ4AfuxOe1qLwWy41--ojKqUslvu93T1NohjxeDeyMwdyc517EotOP0YQu-Rs-KutiI8HGsoIm1VifTZp3P5BosrI1Ll-ntadOK35vg_hnmYt6SoLCYjsCbn72uPQh88kKGwFLD2QJLpuOoO1wqVcQ7VHLfX5gV1mDpH6PHMcb4_KKEI9rGQlZx08o5i9Sak14nFEwzxYN9aSU8VlzAmaOiOBLkFztpUDG_cGKmFHzBDbnxx_OMC8XY88sBoKucjv43QGE7t_Nsyz4vqcwwqrdb7FfxzcFAHK4QxlT7UQ0MQxzIC6RBZsspwiXDlaiwDSrK3F3lmarpyQ9srRNGaBZlasI-4GTrZb91fjgfuTfHokqW705ddjBuAMgCf9GYj28hrmUzPRFbLBZy77dqgwMRn-XLnhc8ln5AHIKBbQLhpOMXYq5ug2QQRXLz1K-F_rpjvQFcnmXQJ_5sMBg1yCZE7kOQ_a5ZOR__gJNbch1XXRT6giKr1kWYDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a78bb4d113.mp4?token=ZYEaA_zy72juBDxQFiQRgtfaXat-5AN84kpq14HBv0cWTLsUJjZNIDxg-UUdsqdY1TMlQiw4KnMBYQ9FNKmM0qjRd0omNOlmOEKhnnlT7IoeTjtB-K4hY9YkHRtljsoEpXkQvykkkf8FUmenCUg-8m0htmu8s0aUGN19jlOF6X8CCyppAtzJ4AfuxOe1qLwWy41--ojKqUslvu93T1NohjxeDeyMwdyc517EotOP0YQu-Rs-KutiI8HGsoIm1VifTZp3P5BosrI1Ll-ntadOK35vg_hnmYt6SoLCYjsCbn72uPQh88kKGwFLD2QJLpuOoO1wqVcQ7VHLfX5gV1mDpH6PHMcb4_KKEI9rGQlZx08o5i9Sak14nFEwzxYN9aSU8VlzAmaOiOBLkFztpUDG_cGKmFHzBDbnxx_OMC8XY88sBoKucjv43QGE7t_Nsyz4vqcwwqrdb7FfxzcFAHK4QxlT7UQ0MQxzIC6RBZsspwiXDlaiwDSrK3F3lmarpyQ9srRNGaBZlasI-4GTrZb91fjgfuTfHokqW705ddjBuAMgCf9GYj28hrmUzPRFbLBZy77dqgwMRn-XLnhc8ln5AHIKBbQLhpOMXYq5ug2QQRXLz1K-F_rpjvQFcnmXQJ_5sMBg1yCZE7kOQ_a5ZOR__gJNbch1XXRT6giKr1kWYDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار:
آقای رئیس‌جمهور، آیا فکر می‌کنید کنگره باید آن ۵۰۰۰ دلار را تصویب کند؟
🇺🇸
ترامپ:
همان‌طور که گفتم، نمی‌دانم اگر جمهوری‌خواهان پیروز شوند، انجام این کار چقدر آسان خواهد بود.
صحبت از ۵۰۰۰ دلار برای تمام بزرگسالان کشور است و ما به‌راحتی از پسِ آن برمی‌آییم، چون درآمدهای کلانی داریم؛
وضعیت ما هرگز تا این حد عالی نبوده است. دموکرات‌ها نمی‌توانند چنین وعده‌ای بدهند، چون در آن صورت اوضاع بلافاصله به هم می‌ریزد و نابود می‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/71576" target="_blank">📅 17:32 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71575">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2f2319501.mp4?token=GDrN83ZA-GollUtywV5BhSbbO8hXQWoqtRQnvY3cX1V8UPUCRpIAts5ZO6ezwDsjHm6o8gm5Gsi8L_hfbT7hTlUKnhXNKvGNOi4hgVSeFlQ-Gg8BdJ3HWxcegBek7pPxBjw1U6Hz55Ita_4i7AxZliQmhpWqe1TDblTuyxgOiQ_zPjnrwtFDHnTVcqQjrZpuPQyDGSSuTJ7txJIUiZYsIigbx4DAK5umqj-vFf7PrQSOk3LBJBM0yIvf6CHSYSzHklCX327vLhrfSK5T9Tz4-MZGe8h4so_9-dDqmlINRVX1s8tAXM8ioKUC7bYzZCMPR30K9f7W4yMUgLNcDX9CvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2f2319501.mp4?token=GDrN83ZA-GollUtywV5BhSbbO8hXQWoqtRQnvY3cX1V8UPUCRpIAts5ZO6ezwDsjHm6o8gm5Gsi8L_hfbT7hTlUKnhXNKvGNOi4hgVSeFlQ-Gg8BdJ3HWxcegBek7pPxBjw1U6Hz55Ita_4i7AxZliQmhpWqe1TDblTuyxgOiQ_zPjnrwtFDHnTVcqQjrZpuPQyDGSSuTJ7txJIUiZYsIigbx4DAK5umqj-vFf7PrQSOk3LBJBM0yIvf6CHSYSzHklCX327vLhrfSK5T9Tz4-MZGe8h4so_9-dDqmlINRVX1s8tAXM8ioKUC7bYzZCMPR30K9f7W4yMUgLNcDX9CvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار:
نظر شما درباره دیدار کشورهای حوزه خلیج فارس با ایران چیست؟
🇺🇸
ترامپ:
برایم اهمیتی ندارد. این به خودشان مربوط است. اشکالی ندارد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/71575" target="_blank">📅 17:29 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71574">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0e5ba3545.mp4?token=ZfOzcnQ89Hqh1RQbWcFrZrUE0n5Z7LjshH8SmozogW0-rbipe1YOSctomuCiBksthLs0KOXZHPyzRqeADjhFbsUCF3tCxQ2YlvnBYDMxf-dTKyxgZ8VvS98xoGra_goDM8TUNcK8ThPaxcHe51I41f9CJ8hpu2Ca2VgqlFefw-Li6Rp1yGNzePG93qp3DdZBeGJ9ZO9WX7txjCfHGyFlBsEqsGO5lzSCFeR8PSgMU8Vxiql6toHupxDaSQCZoUunAw6gefbxXUjUMbCD58GONzXs5_qUJv8wvU0ZrbZNgsZD07mj6iYzBFqEgV2e7JUqv6OBcT0u28xlfybc0JlcZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0e5ba3545.mp4?token=ZfOzcnQ89Hqh1RQbWcFrZrUE0n5Z7LjshH8SmozogW0-rbipe1YOSctomuCiBksthLs0KOXZHPyzRqeADjhFbsUCF3tCxQ2YlvnBYDMxf-dTKyxgZ8VvS98xoGra_goDM8TUNcK8ThPaxcHe51I41f9CJ8hpu2Ca2VgqlFefw-Li6Rp1yGNzePG93qp3DdZBeGJ9ZO9WX7txjCfHGyFlBsEqsGO5lzSCFeR8PSgMU8Vxiql6toHupxDaSQCZoUunAw6gefbxXUjUMbCD58GONzXs5_qUJv8wvU0ZrbZNgsZD07mj6iYzBFqEgV2e7JUqv6OBcT0u28xlfybc0JlcZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
ترامپ درباره ایران:
در نهایت ما آنجا را ترک خواهیم کرد، مگر اینکه تصمیم بگیریم بمانیم و نفت را برای خود نگه داریم؛ درست مثل ونزوئلا.
دیگر درباره ونزوئلا حرفی نمی‌زنید، مگر نه؟ خوب به این موضوع فکر کنید: میلیاردها و میلیاردها و میلیاردها دلار.
@News_Hut</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/71574" target="_blank">📅 17:27 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71573">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🇾🇪
حوثی‌های یمن تصاویر مفصلی از عملیات نظامی جدید خود با عنوان «و خداوند از نظر قدرت و کیفر، سخت‌گیرتر است» منتشر کردند؛ ویدئویی که صحنه‌های نبرد در جریان تهاجم اخیر آن‌ها در ساحل غربی را به تصویر می‌کشد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/71573" target="_blank">📅 17:02 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71572">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c9fa2fdcc9.mp4?token=b_SGbx5C_KlYT8Bpgfo72ZJ1bgY6fdtKPDjU9KtVLwyuZCCdebcALidKZjzZMrAI9gFEEMTLKa-Xvhoq8URIc1M2QQ-8632ucnogWLuH1dI2dzbc14mEw8o44A3HHBKimBxlRsE-2smZ_vISDl2XX-UVQi8Hc8U5bJX2765QmghKGpOhW2zz5NxK11h5DrmMXZtr7-8r1paDKCtalxbxV5hFuxmnTN3LDiMYoX-tGYGDkLk3uuQQP7J48vpGrKB7ZCM-sfox_E9VHQLMdaA1ZU739L-FMR-Zr-JWJu6Tr__6-YipuuRXV5PkBaX-cDfjEIqQ3mDTl4CusXF5oYhnGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c9fa2fdcc9.mp4?token=b_SGbx5C_KlYT8Bpgfo72ZJ1bgY6fdtKPDjU9KtVLwyuZCCdebcALidKZjzZMrAI9gFEEMTLKa-Xvhoq8URIc1M2QQ-8632ucnogWLuH1dI2dzbc14mEw8o44A3HHBKimBxlRsE-2smZ_vISDl2XX-UVQi8Hc8U5bJX2765QmghKGpOhW2zz5NxK11h5DrmMXZtr7-8r1paDKCtalxbxV5hFuxmnTN3LDiMYoX-tGYGDkLk3uuQQP7J48vpGrKB7ZCM-sfox_E9VHQLMdaA1ZU739L-FMR-Zr-JWJu6Tr__6-YipuuRXV5PkBaX-cDfjEIqQ3mDTl4CusXF5oYhnGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
توی مملکت یه سری کارگاه آموزشی گذاشتن و به افراد بالای 60 سال آموزش میدن که چطوری اسنپ بگیرن.
هزینه شرکت تو این کارگاه بین ۱ـ۲ میلیونه.
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/71572" target="_blank">📅 16:31 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71571">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cc03db8a0.mp4?token=c1Ebqvtc4HRSygS9f9cc2vOBEKUo16bIzDeJsqSDBRDir0nUnj-N3GPEe2TBFE_jvCiKzrTMp7CJsdj3lvMsNcJccn0svBOIDDvJzx51Pd0kaTUlR75-a0_59DIdHYqb33kAWcfbQOa3WJJHT1PI1Bc0fcTCtTZh52gbHli5zKzvUi8vumwoGI45X5UNsutD6mitmCpckxhh8_ivrLR15t-JaYLYF15Iec1szIb5bGJ8j5ZjtDcQWmww1HuZiBwWsHWitzCF2d3pm5yYL3bk3IAIu-BXX0jUjx8rA5TCi6t4OK1PIcjgMQeUsuMaqFhVlOkr3KWLmAuihfE82EgJGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cc03db8a0.mp4?token=c1Ebqvtc4HRSygS9f9cc2vOBEKUo16bIzDeJsqSDBRDir0nUnj-N3GPEe2TBFE_jvCiKzrTMp7CJsdj3lvMsNcJccn0svBOIDDvJzx51Pd0kaTUlR75-a0_59DIdHYqb33kAWcfbQOa3WJJHT1PI1Bc0fcTCtTZh52gbHli5zKzvUi8vumwoGI45X5UNsutD6mitmCpckxhh8_ivrLR15t-JaYLYF15Iec1szIb5bGJ8j5ZjtDcQWmww1HuZiBwWsHWitzCF2d3pm5yYL3bk3IAIu-BXX0jUjx8rA5TCi6t4OK1PIcjgMQeUsuMaqFhVlOkr3KWLmAuihfE82EgJGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇦
❌
🇷🇺
ویدیویی جالب از یک پهپاد اوکراینی که به سمت یک کشتی روسی در حال حرکته و یه بالگرد روسی تلاش می‌کنه اونو بزنه ولی، این پهباد در نهایت خودشو به کشتی میرسونه و منفجرش میکنه
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/71571" target="_blank">📅 16:02 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71570">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31fa8bd2c9.mp4?token=QyhXTgdr6_Nhqdxt5YSmORXYxoUYWp0mSMfiqz_uDbFUqoGHQtrnphet3hSmwpDPX9LOcTgi_OT26KzW4edlHlMLI8Ulm4ezcgrPb1azUhbZyfTsZraljxtnmwccy0XcjxztO3x9zyiZsnamlghQEAypIyK-pQsYLkylQnz-ie8jzC9b_Omc1UCEEfUQRIbYJF0g-puXzk0ej3GXnAo4OF-UbK-SdR_dNAdtDTY0iW9tHtt9_u2hedPJrMb-eAlYM6GtplTsMpGUFPtXnQQ5HQOW0URxrWd6ei0hFXqf4DRIR2HFfDhsE87RVObJDzNcDeLjQm2j5IkXbeU0hnI4HQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31fa8bd2c9.mp4?token=QyhXTgdr6_Nhqdxt5YSmORXYxoUYWp0mSMfiqz_uDbFUqoGHQtrnphet3hSmwpDPX9LOcTgi_OT26KzW4edlHlMLI8Ulm4ezcgrPb1azUhbZyfTsZraljxtnmwccy0XcjxztO3x9zyiZsnamlghQEAypIyK-pQsYLkylQnz-ie8jzC9b_Omc1UCEEfUQRIbYJF0g-puXzk0ej3GXnAo4OF-UbK-SdR_dNAdtDTY0iW9tHtt9_u2hedPJrMb-eAlYM6GtplTsMpGUFPtXnQQ5HQOW0URxrWd6ei0hFXqf4DRIR2HFfDhsE87RVObJDzNcDeLjQm2j5IkXbeU0hnI4HQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
مجری صداوسیما:
از جنگ تحمیلی دوم حدود ۱۵ ماه اینا هست میگذره دیگه
مقامات صهیونیستی و امریکایی پر تکرار گفته ان که با حمله به ایران ظهور مهدی موعود رو به عقب انداختیم
دلیل اصلی بمباران تاسیسات هسته‌ای ایران به عقب انداختن ظهور بود
اونا نگاهشون آخرالزمانی هستش
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/71570" target="_blank">📅 15:34 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71569">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d522fc2430.mp4?token=B_vkisx89pVwJ0TChY8R9GKkiqqWNucSQCS2pZHCPNd732aGcbLctq1vDDeQYbF-yEwymNioF00D9TAnVvVHJbFYDwGfNCchoC38gmh1podz3SHrhudHnrOIuw_IyEASqUSvfC_Mmlc6v18R9suv80CY0374i3Y1VlzCV9o5NYjb5ghPhODZJIZze1CGm6rATQCMK0mvhTlFMENDa0fyB902aZfKBDUU_Cfgoe270FuJH3D3RY4OURmYSpKQ6VsQzt73mXPu3PsahKEvCohKdR8grovRpWq09kzyyYpvwfp5zAYxN8hG9rA0mdqwvZV0O9xNFGFpDA3Wb1KFdwQOL4sn89sqo72bwIx_fZF254pC-87nNcbgyI8bCQao0VdDi7n80VY9dtCCtqD1qBj6Z30yV0ZlBzpiL0JvL21FGLy4mN4DA0kwoYnOnDgXtG-N1jdxdtb4-OGiudEzyNmOoHbwmd1TMQZsJSSh8ylRIZZ-eijDuth0ev83enIkwx_d5L4ITOk6oVmybeEBJB6cvl_bGdsn11VSQ8gP0hJamuBkMWPPP14355tY6OFTgvcRJ66lw00XXV_6uVMj_1Mos-xYFh9ZHajKykAga4vLY-B4axGZ2w_dw0EFYYY8eS1Mv0rO9ToM0YODiEg0jPiQcCKe8rLaSLUKBEYSCV-y4iw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d522fc2430.mp4?token=B_vkisx89pVwJ0TChY8R9GKkiqqWNucSQCS2pZHCPNd732aGcbLctq1vDDeQYbF-yEwymNioF00D9TAnVvVHJbFYDwGfNCchoC38gmh1podz3SHrhudHnrOIuw_IyEASqUSvfC_Mmlc6v18R9suv80CY0374i3Y1VlzCV9o5NYjb5ghPhODZJIZze1CGm6rATQCMK0mvhTlFMENDa0fyB902aZfKBDUU_Cfgoe270FuJH3D3RY4OURmYSpKQ6VsQzt73mXPu3PsahKEvCohKdR8grovRpWq09kzyyYpvwfp5zAYxN8hG9rA0mdqwvZV0O9xNFGFpDA3Wb1KFdwQOL4sn89sqo72bwIx_fZF254pC-87nNcbgyI8bCQao0VdDi7n80VY9dtCCtqD1qBj6Z30yV0ZlBzpiL0JvL21FGLy4mN4DA0kwoYnOnDgXtG-N1jdxdtb4-OGiudEzyNmOoHbwmd1TMQZsJSSh8ylRIZZ-eijDuth0ev83enIkwx_d5L4ITOk6oVmybeEBJB6cvl_bGdsn11VSQ8gP0hJamuBkMWPPP14355tY6OFTgvcRJ66lw00XXV_6uVMj_1Mos-xYFh9ZHajKykAga4vLY-B4axGZ2w_dw0EFYYY8eS1Mv0rO9ToM0YODiEg0jPiQcCKe8rLaSLUKBEYSCV-y4iw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
🇾🇪
تصاویر بسیج قبایل حوثی، ستون‌های طویلی از خودروهای تویوتا (تکنیکال) مجهز به سلاح را در بیابان به نمایش می‌گذارد؛ تصویری که نماد کلاسیک جنگ یمن است.
قبایل «بنی‌حشیش» برای پیشروی به سوی «مأرب» — آخرین پایگاه عمده دولت در شمال — اعلام آمادگی کرده‌اند.
وانت‌های تویوتا مجهز به سلاح، همچنان ستون فقرات نیروی زمینی حوثی‌ها را تشکیل می‌دهند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/71569" target="_blank">📅 14:59 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71568">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L8BW_tf6glJ3VBzhYmW49PldbLJT9cQvx-qg_UepvxPu98bMnEOscpbSFsWw1J4dqgmkKH1FR-BQc0I56LCXuykhwXF_AfItDp6TUD8dwibJMu9KbuSFwLwKNVF3F1nc-RNodaYt1OyALQMTsF8knTWMPSD_eJHdeZlJ_5aBP33VhCLvzxujbfugM0VNkVD5DicoP0xUzNDrr7xFQO-XCN2CzGxeo0d7rGwFgu6sac0lSePM2X5Hy0MgHMoTDYCfw1aPdJiegxtb2MpFMUjW_paRQ8JugfXANzNT7yb6hkDLlaOHw0gxTwmPePbMYoV0XgMgNmPEBQ9mNxKvVdNbWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
📰
اکسیوس: محمد بن سلمان، ولیعهد عربستان سعودی، روز پنج‌شنبه دو بار با دونالد ترامپ، رئیس‌جمهور آمریکا، تماس گرفت و از ایالات متحده خواست تا هم‌زمان با پیشروی حوثی‌ها به سوی یک نقطه راهبردی و حیاتی در دریای سرخ، به آن‌ها حمله کند.
ترامپ این درخواست را نپذیرفت و مقامات آمریکایی اعلام کردند که در حال حاضر هیچ برنامه‌ای برای مداخله مستقیم علیه حوثی‌ها وجود ندارد.
دریاسالار کوپر، فرمانده ستاد فرماندهی مرکزی ایالات متحده (سنتکام)، نیز روز پنج‌شنبه برای هماهنگی‌های اضطراری به ریاض سفر کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/71568" target="_blank">📅 14:31 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71567">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/363bcb9915.mp4?token=nz6jXkbYMiFbekujDwLL5s9w7kmrpg8HGeiYanynOyxxuUM3e4BIyzCjogXTBdj5DCSutCGjr-ZGzTHVgRBbBrPMSQPufH43Xtp4q1aS6HYkHCwRESX0VLU5jbtA3hjHy_swZCPQL0DnDvCe0ZSnoZe_ebrx0Oj0bxy5rYx1JDiJWzQgeHB2IiySTPMH6eX8VUQCYAwf2KnMWOozp1L5Sa3LYUIN5VVFU_N9d_sOus1FRYBKB9aq2ecc9PIKSWuHBHDPy0Wxa2MBzL41homEmKk_a7rowQ4GlWHFpCFOtzleAmobIhuYUuckh75ZrInlThA17dXpw3Kvn8hhFEwX0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/363bcb9915.mp4?token=nz6jXkbYMiFbekujDwLL5s9w7kmrpg8HGeiYanynOyxxuUM3e4BIyzCjogXTBdj5DCSutCGjr-ZGzTHVgRBbBrPMSQPufH43Xtp4q1aS6HYkHCwRESX0VLU5jbtA3hjHy_swZCPQL0DnDvCe0ZSnoZe_ebrx0Oj0bxy5rYx1JDiJWzQgeHB2IiySTPMH6eX8VUQCYAwf2KnMWOozp1L5Sa3LYUIN5VVFU_N9d_sOus1FRYBKB9aq2ecc9PIKSWuHBHDPy0Wxa2MBzL41homEmKk_a7rowQ4GlWHFpCFOtzleAmobIhuYUuckh75ZrInlThA17dXpw3Kvn8hhFEwX0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
کنعانی مقدم:
اگر رهبری اجازه دهند، ظرف ۲۴ ساعت از سلاح هسته‌ای استفاده خواهیم کرد
خرید فیوز هسته‌ای از کره شمالی، کار خیلی ساده‌ای است و ۵۰ تا فیوز می‌توانیم بخریم
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/71567" target="_blank">📅 13:49 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71566">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f67e4c7321.mp4?token=Suo0wuqsV_x4HX4-WHR73gUp_WgoWmKzWYh_SUNuzd4wxfdOSTTeafxgu8mUKjWYkFbJDoF2g8AxjGM2VoTawRWHlOvWszX9aow-omUwArdQ3DkZERz2einK0UBtxbvcTr3gLhUaQ4HNED96Eyl52nNABwnljm2bA7hluycw3aqS3iqInl4tKnccym5T4wTSIYWP-tXltsQE7ihzUFNIRcN8Ln5UgDVDjUYDO3jKux_maqm0NeaxF7v01KzT_ug85xWzQS3s9kJDBli-wRG1-t3atBu3DOfX-6-O1twmiWCU9qZQYpEAjzphBq5HDmLelGsSAD49ac8ylJeeZyhDDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f67e4c7321.mp4?token=Suo0wuqsV_x4HX4-WHR73gUp_WgoWmKzWYh_SUNuzd4wxfdOSTTeafxgu8mUKjWYkFbJDoF2g8AxjGM2VoTawRWHlOvWszX9aow-omUwArdQ3DkZERz2einK0UBtxbvcTr3gLhUaQ4HNED96Eyl52nNABwnljm2bA7hluycw3aqS3iqInl4tKnccym5T4wTSIYWP-tXltsQE7ihzUFNIRcN8Ln5UgDVDjUYDO3jKux_maqm0NeaxF7v01KzT_ug85xWzQS3s9kJDBli-wRG1-t3atBu3DOfX-6-O1twmiWCU9qZQYpEAjzphBq5HDmLelGsSAD49ac8ylJeeZyhDDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎯
ویدیویی از هدف قرار گرفتن نیروهای انصارالله توسط نیروی اسنایپر مورد حمایت عربستان سعودی
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/71566" target="_blank">📅 13:14 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71565">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0000373bd7.mp4?token=NlKVHQMSeSnKDId7mUyWpTxVY0YbpH0CBt9XOBlel6czH05-DTRLb8Z9a73_P41e-n6rldgiS7N2Qv04Fnpnj6v9EkgC6RC63C0kToD0PTVf3vTKSv2AALPufkwSNtCwMpRWA1cvy_ZKOezP-f9TxacIyKWilb4foTLzIF8c2Mfu6QQWtc3zKkWpseepkeJVYTk2fqlHnQAgJxthr7mfot1BGKtHOJtM4ZAGiDwqudcgUSqikuHKgIgjb5BskIkW2lr2vkXWkwV_Gv_FlvXbX8SdodojSQ72rAlhK12-c4RW0jGG-mo1G2rYGutzRamkJl760lQ_tTpRYCgknWAr4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0000373bd7.mp4?token=NlKVHQMSeSnKDId7mUyWpTxVY0YbpH0CBt9XOBlel6czH05-DTRLb8Z9a73_P41e-n6rldgiS7N2Qv04Fnpnj6v9EkgC6RC63C0kToD0PTVf3vTKSv2AALPufkwSNtCwMpRWA1cvy_ZKOezP-f9TxacIyKWilb4foTLzIF8c2Mfu6QQWtc3zKkWpseepkeJVYTk2fqlHnQAgJxthr7mfot1BGKtHOJtM4ZAGiDwqudcgUSqikuHKgIgjb5BskIkW2lr2vkXWkwV_Gv_FlvXbX8SdodojSQ72rAlhK12-c4RW0jGG-mo1G2rYGutzRamkJl760lQ_tTpRYCgknWAr4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
مجری:
این رهبران جدید و رهبران واقعی که رئیس‌جمهور ترامپ از آن‌ها صحبت می‌کند، چه کسانی هستند؟
🇮🇷
پزشکیان:
به گمانم باید این را از خود او پرسید، چرا که هر روز حرف متفاوتی می‌زند.
یک روز می‌خواهد ایران را نابود کند و روز دیگر می‌گوید ما دوست ایران هستیم؛ یک روز می‌گوید ما را به رسمیت می‌شناسد و روز دیگر می‌گوید ما را قبول ندارد.
بنابراین، ما مطمئن نیستیم که باید کدام اظهارنظر را بپذیریم و بر اساس کدام‌یک عمل کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/71565" target="_blank">📅 12:51 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71564">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71564" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/71564" target="_blank">📅 12:50 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71563">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PfFe2pCoJmxxduTShi1VxmPFyXRcFNgKtSIgoDrAD0bUXTOeNUN4a9-Nc6ACyN_xCywcA9_4kT3q7k8ADBghpdyJdC4wTwYrmZYCgeP1PSSaovN2LLX1MySJby7vtnjVjFdd2oNBz6KjPjH1fjuvITJOe-DVAnjWBBMXqvq-N3ffGhsrUiK8Wlwtbg7f6Jquei56BsztbyNamejO_WA4eNfDgvHpgcopJA5yHonx8XtsrPrww428iYa2D_1x95tfYyg-GSKQqdUL0ocdraMaTpSXp7paLUTb2KMKpscJaQfXg4s6fSgdEO8qfbGsNIw8w9vAXEg5ASyvJ5vQhiuC5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
نبرد بزرگ منچستر در راه است!
نبرد هیجان انگیز
⚽️
منچستریونایتد
🆚
منچسترسیتی
⚽️
را در
TrexBet
پیش بینی کنید!
📉
نگاهی به آمار ۵ دربی اخیر منچستر:
⚽️
منچستریونایتد: ۲ برد، ۲ تساوی، ۱ شکست و ۵ گل زده
⚽️
منچسترسیتی: ۱ برد، ۲ تساوی، ۲ شکست و ۵ گل زده
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
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/71563" target="_blank">📅 12:50 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71562">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fKHa2SDCg43BaGzmosIs4xKUZMv7tufqSW-eAv5kAp1ydp93UOA7yDZ3nQrMJo1giGvSJfYdPIl5yTIPMoqJpOWmBcveobPGzI_4ss6ZHUT5D075YeB7lGFW4PLohuMCW0kZdHcpTD2DIfUZb1Y8rh5LU0ac7RDZj7SokWsRZf-1x_y2EBUVThEGt5UB-7lq2TqtwUKHc3KjtbRLJrubH8KCqhlwmMOgPNtrCYQm1JtLk3pvKuzBK7El4r_EnvGMUGSSaSPjaQ4r-iEO_GiQt-6ocoXFHxeSRAbFSmRnE10dYUxgcB0MUyFr1UcWMvvw4lrEgY08Mtts6NAvSoXjFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
سازمان عملیات تجارت دریایی بریتانیا (UKMTO):
روز یکشنبه در گزارشی اعلام کرد که بر اثر اصابت یک پرتابه ناشناس به شناوری در حال عبور از تنگه هرمز، در آن کشتی آتش‌سوزی رخ داده است.
این سازمان اعلام کرد که مقامات محلی در حال کمک به تخلیه خدمه کشتی هستند. در این گزارش، نام شناور یا اطلاعاتی درباره تلفات، خسارات و یا پیامدهای احتمالی زیست‌محیطی آن ذکر نشده است
.
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/71562" target="_blank">📅 11:40 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71561">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🇮🇷
🇯🇴
ویدئویی از پرتاب انبوه موشک‌های رهگیر «پاتریوت PAC-3» از پایگاه هوایی «موفق سلطی» در اردن در سه روز گذشته، برای مقابله با موشک‌های بالستیک ورودی ایران.
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/71561" target="_blank">📅 11:25 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71560">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/58c7237eb3.mp4?token=WGYjimuvUmehn4Oy4-leHi8s9a13S_aB3wzYVryIkQyh3CpIfHCJ9ImNmRTzTUaz7UJU0NJLMjQpx62BG8GuO6zW3yLZenVqQuuT8JZ60-sGaulFXeoac6h1d2_zQChq0C7gBjX_-u7zq6uIr9-vu6ojTepZ02_FnsPaZJHk0pZznf75Ed7f2LXKFuLv6gBh43CjjT1hsR15gtAQSiRhIPrfHV3QrhqlvFl2jvR0LUpRhphxg91gljNP0VJBKxYIUyK9BHOy6mW-ixQjRO2u0u11dmBtdE3S88vZi5A45D72aUkFv4cFCFEynArnfAKeEwmzNRwBta8-tl5KbBm5JA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/58c7237eb3.mp4?token=WGYjimuvUmehn4Oy4-leHi8s9a13S_aB3wzYVryIkQyh3CpIfHCJ9ImNmRTzTUaz7UJU0NJLMjQpx62BG8GuO6zW3yLZenVqQuuT8JZ60-sGaulFXeoac6h1d2_zQChq0C7gBjX_-u7zq6uIr9-vu6ojTepZ02_FnsPaZJHk0pZznf75Ed7f2LXKFuLv6gBh43CjjT1hsR15gtAQSiRhIPrfHV3QrhqlvFl2jvR0LUpRhphxg91gljNP0VJBKxYIUyK9BHOy6mW-ixQjRO2u0u11dmBtdE3S88vZi5A45D72aUkFv4cFCFEynArnfAKeEwmzNRwBta8-tl5KbBm5JA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
نظرات متناقض هادی چوپان درباره هانی رامبد:
بعد از قهرمانی
بعد از جدایی
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/71560" target="_blank">📅 11:03 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71559">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/097559287c.mp4?token=IWj_9Cbi0WhUSVjbWmkwP8taVS83uflDwZjnHjaAHa3cPtxZdb8AQ67WXII9Jqe4DrzGanUGsTm-Kqzoqdw3hS0cBPlXsroMY-2-sHsp5YZnPmnRdciCrz2iNs9Qfv-7qP4n8JnoHnZrtCKTPNpAtFbfGE7g-RsCMxPDBg_97kIMIpVuZICBDf33i6bhG7rjoU_gN3g9mkjj3YgJy3BBxYhDFFCflE5NyNDadGa4P3LQPVlTtQIaDG4cJuTcX6S_3ncfxvJo57VhfhJGX56PDx7_u3beJaI5qOLZ0ICDj5H75cf0N1j9cN-0vr59LCGp4iuh5mU1gGpKv1q-xx3Y1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/097559287c.mp4?token=IWj_9Cbi0WhUSVjbWmkwP8taVS83uflDwZjnHjaAHa3cPtxZdb8AQ67WXII9Jqe4DrzGanUGsTm-Kqzoqdw3hS0cBPlXsroMY-2-sHsp5YZnPmnRdciCrz2iNs9Qfv-7qP4n8JnoHnZrtCKTPNpAtFbfGE7g-RsCMxPDBg_97kIMIpVuZICBDf33i6bhG7rjoU_gN3g9mkjj3YgJy3BBxYhDFFCflE5NyNDadGa4P3LQPVlTtQIaDG4cJuTcX6S_3ncfxvJo57VhfhJGX56PDx7_u3beJaI5qOLZ0ICDj5H75cf0N1j9cN-0vr59LCGp4iuh5mU1gGpKv1q-xx3Y1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
تلاش ابی برای بوسیدن دست یکی از بازیگران برنامه عشق ابدی که ویدئوش به شدت در حال وایرال شدنه!
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/71559" target="_blank">📅 10:34 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71558">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/427cd49fec.mp4?token=aC6hcoLPrHIfn7whmeAIhOPhr0S962_H5VxGHr7Lh4P6Z4yKyotpA8GmrQ5kFgzL9RsJo1qRLy-D0oky_8dGEMgTz_zR26zy-jIg8aG9SuCnL87_X5X49GHH7vdngAIcFtZY3UvdkXyihfrBWQvYvIuYkfOsEPESOLIMHNgl6ciemU0O5VoZhJt0-2W-OQq4Ba1wL_PD81Mcu6JLKsYwqNAyOHFbRXEXWhJJrViE71aKJKo-GE1j7b9aBzuL0CjYXnBhdRi-g0C8p-7361o3iESx3aAFOCcMPRlqsIugxLSFJn84tlUYIL_iJLOvh47TOdCYkP0pcF2gIkoMkfPgHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/427cd49fec.mp4?token=aC6hcoLPrHIfn7whmeAIhOPhr0S962_H5VxGHr7Lh4P6Z4yKyotpA8GmrQ5kFgzL9RsJo1qRLy-D0oky_8dGEMgTz_zR26zy-jIg8aG9SuCnL87_X5X49GHH7vdngAIcFtZY3UvdkXyihfrBWQvYvIuYkfOsEPESOLIMHNgl6ciemU0O5VoZhJt0-2W-OQq4Ba1wL_PD81Mcu6JLKsYwqNAyOHFbRXEXWhJJrViE71aKJKo-GE1j7b9aBzuL0CjYXnBhdRi-g0C8p-7361o3iESx3aAFOCcMPRlqsIugxLSFJn84tlUYIL_iJLOvh47TOdCYkP0pcF2gIkoMkfPgHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدئو وایرال شده از 9 اسفند - روز شروع جنگ و بمباران تهران و واکنش  دانش‌آموزانی که خرکیف شدن
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/71558" target="_blank">📅 09:59 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71557">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
🇮🇷
امیر تیموری فرماندار شهرستان قشم:
یک کشتی تجاری حدود ساعت ۵ صبح امروز در محدوده جزیره هنگام و ساحل شیب دراز جزیره قشم مورد اصابت قرار گرفته است.
در این حادثه  یک نفر شهید  و سه نفر مجروح شده اند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/71557" target="_blank">📅 09:31 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71556">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uXBhcEwHB0fapOqZqAHQGda9EBVEiIB6Es8pzjqVAKwr7CGpQPzfJoacPSd3bVehHEfmi7LLFDE_DFIdRz8ATuTmCvcqGqD-SMCIfVVFxzPllBt9Kdrtb5-rMQK-pU_d09pYwZQryzMKzKtjkFfAJsC6qruhDL_EimjQCvhsMZr8hEg6K9hll5hl3E65XKo3OejriIHCbQFjNSnhOVJwkXy3amHxQE-BSrOQP6dlMal2f0XZo2RAfCgFyanyk24WHBwUmLAN0q0-et92vFh_rz0iKucrhH2aX4wqT2bi5X9JE3vk6vUUQQ0oZnZ4bmVGxWKETEaPjGdMIrMsbfDBzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇨🇳
🇮🇷
📰
وال استریت ژورنال:
مقامات آمریکایی می‌گویند ایران پیش از حمله موشکی بالستیک ۱۷ ژوئیه به پایگاه هوایی «موفق سلطی» در اردن — که منجر به کشته شدن سه سرباز آمریکایی و زخمی شدن چهار تن دیگر شد — تصاویر ماهواره‌ای با وضوح بالا از نهادهای چینی دریافت کرده بود.
این مقامات معتقدند که تصاویر مذکور با این حمله مرتبط بوده و احتمالاً به ایران در شناسایی دقیق‌تر اهداف ارزشمند کمک کرده است.
آن‌ها دولت چین را به مشارکت مستقیم در این حمله متهم نکرده‌اند و هویت نهادهای چینیِ دخیل در این ماجرا نیز مشخص نشده است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/71556" target="_blank">📅 09:00 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71555">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🦖
2 چالش، 2 کد مخفی، 2 جایزه 1$ در سایت بین‌المللی TREXBET !   فردا در دو زمان مشخص، عکس‌های چالشی داخل استوری کانال منتشر میشه؛ اما کدها همین‌طوری به دستت نمی‌رسن…
👀
🔎
باید با دقت بگردی، Promo Code یک‌دلاری رو پیدا کنی و قبل از بقیه داخل سایت ثبتش کنی! …</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/71555" target="_blank">📅 01:45 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71554">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/djhSzWCtYvFrZo0Li3hvg-fhhYP7zjjjC0tplULd13qes5VGSrijd8wgASNVJDRVHWUEOhKzXhzNRZvw7yppx_tOq-TzecqWkAj3cNxY4zLeQQi6jK_KIW_60wJRMxPXEcLyqowKyLJNTS6giQ8yzdiebxnBDoeU1SJCn0mL0hronxkUCr9mfCXiDlfF9s816RnU8kN9DciUNCvvX4I_wkp4zTr1wUitMOrZK4WJHMCqtDXJO8kJlNxG9nYHBhrXxi1e5rpyveJ4-cGDCK288N-jRh10WjjjMvg9T1gzUgD-VcqwqTge4dqQJXN-YVwJHkOHSAIk5-pN_38E0SG4vA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
2 چالش، 2 کد مخفی، 2 جایزه 1$ در سایت بین‌المللی
TREXBET
!
فردا در دو زمان مشخص، عکس‌های چالشی داخل استوری کانال منتشر میشه؛
اما کدها همین‌طوری به دستت نمی‌رسن…
👀
🔎
باید با دقت بگردی،
Promo Code یک‌دلاری
رو پیدا کنی و قبل از بقیه داخل سایت ثبتش کنی!
⏰
چالش اول → 18:30
⏰
چالش دوم → 20:00
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/71554" target="_blank">📅 01:45 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71553">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bad61e1e00.mp4?token=Tc_VNnsvd4zqgeoAvq0qRygB-irOOwJtp-DToGmLoovdROaVpzf1EDgvZUJP77Y9qIWH-CGCgIZsyXae7Y9iD0teqNS9icKNZn6QDm_Wzh9xX-0fFvJ5qG5w9pM4Nncq5qMaYzAQxPjzchMAgHIaAElQ0XssxoWabWuf-tEaEal7QZiB6MXXyv8SB2Wnb-Sw4o0HWVxiYPw4EjGb16RkbzEcLe4xjINGCzB1-QhtxeCrDN7HG0R4XU8sb6XTT42_148HJF_xF6Py6r6HG4IVHUtdv7hVl0axsXFaJ3GaQi9BiUgxYGtY1luq47idh1oyH63r_MaL3zTnZKLVATSg7kS7YVM8Uhmgr3kwqmDNw24jZ3Fw6jBibzPNPxRQnswf7uEl4TOCCviS_rzlil7BJis1bD3r6IKHVCDSKaqWcQXuvpRnlJLSM3krPTUhsaPmYo8pl30y3WeZECkkBrY6vc3ygPZ2z1zFx3qReSNngrk3qPD8tYqlkj3H1E9a3pktrnvZ96x1_OX5WJdWqgZWdt6yZVgEe6rsuS6n67vxB-SuNZ5QD9xN4x9vGtjxvGia0ikTs1Y8yjynfHr31rR9Ty_bVXkAfAJaSNs-ED694DhkI2mVWVxoq1S28YUohKDQMaGeNsGM-RHWiAEfW-AE2Wah4QefI5AFHz1jIub0lIE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bad61e1e00.mp4?token=Tc_VNnsvd4zqgeoAvq0qRygB-irOOwJtp-DToGmLoovdROaVpzf1EDgvZUJP77Y9qIWH-CGCgIZsyXae7Y9iD0teqNS9icKNZn6QDm_Wzh9xX-0fFvJ5qG5w9pM4Nncq5qMaYzAQxPjzchMAgHIaAElQ0XssxoWabWuf-tEaEal7QZiB6MXXyv8SB2Wnb-Sw4o0HWVxiYPw4EjGb16RkbzEcLe4xjINGCzB1-QhtxeCrDN7HG0R4XU8sb6XTT42_148HJF_xF6Py6r6HG4IVHUtdv7hVl0axsXFaJ3GaQi9BiUgxYGtY1luq47idh1oyH63r_MaL3zTnZKLVATSg7kS7YVM8Uhmgr3kwqmDNw24jZ3Fw6jBibzPNPxRQnswf7uEl4TOCCviS_rzlil7BJis1bD3r6IKHVCDSKaqWcQXuvpRnlJLSM3krPTUhsaPmYo8pl30y3WeZECkkBrY6vc3ygPZ2z1zFx3qReSNngrk3qPD8tYqlkj3H1E9a3pktrnvZ96x1_OX5WJdWqgZWdt6yZVgEe6rsuS6n67vxB-SuNZ5QD9xN4x9vGtjxvGia0ikTs1Y8yjynfHr31rR9Ty_bVXkAfAJaSNs-ED694DhkI2mVWVxoq1S28YUohKDQMaGeNsGM-RHWiAEfW-AE2Wah4QefI5AFHz1jIub0lIE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🟥
گزارش فاکس‌نیوز:
جنگنده‌ها از ناو «یو‌اس‌اس جورج واشنگتن» (USS George Washington) در حال برخاستن هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/71553" target="_blank">📅 01:10 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71552">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I4l9EX-bf1csVo6bXRasxxa8WMVjd6Ph2BhyX1FWcch0V-DTS_IQld0Ieki3vFpIkdOmiVLLqrEpaNv7u8FtIBaLl7oy-AhwEHazzOuilXg3vghUvTg_vveyFF1M6REkBg5kAgB86H0nkalQVBE6BaUpHS0RYr--n6suWCth0wM1a4MivtUXEVnYyLhFH7j-S5p4F9p6gc1n7PiD1OjlnoNOVqP1qnbah9-F9sqUoqPQIrsCiwUZnauy2oTOAu6H4fwvr7vksg7Smd2Ot5TGHY8ifOe5DxHJt7idLyY3OylbGzss6lqzeOaM1YE7S-Yn6TTjf_y4rWscQuTXvnao9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇮🇷
#فوری
؛کانال۱۴ اسرائیل:ایران برای خروج از پیمان منع گسترش سلاح‌های هسته‌ای (NPT) و آزمایش بمب هسته‌ای آماده می‌شود.
حاجی‌دلیگانی، نماینده مجلس، از آماده بودن طرحی با قید سه فوریت خبر داد و افزود: «باید هرچه سریع‌تر آزمایش‌های لازم برای سلاح هسته‌ای را انجام دهیم.»
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/71552" target="_blank">📅 00:21 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71549">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NCyd_6yjARlIGTB4kecTfa91uimEjhHUrPirTx6TjkidSdHIDTZE6l9wU3F1Frsn6sjpXv7D8lLDt1pNqj-D_nEFCx6MBT3j3VSrF5WQlUYrOVide-kxdpcSJCf4X7AXxqUuzA-bKkm4EhUIJ_kuhRsuJmz3Vx9Z-Ic1OY-VID_RQZ_XSxFXnh9aqeir5IjoXTF14UwX-OqQ1V8ikRpCz-aBjA3-EKorthNlT9i4u5zKoAgsqnIWxecwz6LYInyLrHgPlAwKQSEAhOfoUbF5i-fKJPF_LcJ7-FxOBzYvfvR8Ialxfrdaw1bCiy80TR5b2V_pQuzZifoKS4ZmblkokQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12ddef7d0b.mp4?token=qltPElEHiJWOnJ6w6FZmQQHW-dIr-clLU4v7mWAVoFPZoHdhTQL-Vw-jYwFBhKYgzdjQXtmeN3ndRoOgUFdvieiz3IJX0bVF1QMUjihAuWDHjdQhxgbcwFOON8d5Q36mubJavRi7MApLhGZU0gwl0B5Dd1ZJnuYJsrt2laIY3vTZmzXRZ2OeO6Q340eH535F5R5Qs_m_HxGXaq_4-1264h5mmhjarQP7fXTBmjCt9W-k5H_UPsNzqLnG6ZzS5ICtkofHUPIxaRWaL-3QyQQFq5LzoSISbBhIf3GKkTA9qf2Nk7NFDjoEgN43r4SP6HAaIMRXYxjIQKj19V0_uOgELg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12ddef7d0b.mp4?token=qltPElEHiJWOnJ6w6FZmQQHW-dIr-clLU4v7mWAVoFPZoHdhTQL-Vw-jYwFBhKYgzdjQXtmeN3ndRoOgUFdvieiz3IJX0bVF1QMUjihAuWDHjdQhxgbcwFOON8d5Q36mubJavRi7MApLhGZU0gwl0B5Dd1ZJnuYJsrt2laIY3vTZmzXRZ2OeO6Q340eH535F5R5Qs_m_HxGXaq_4-1264h5mmhjarQP7fXTBmjCt9W-k5H_UPsNzqLnG6ZzS5ICtkofHUPIxaRWaL-3QyQQFq5LzoSISbBhIf3GKkTA9qf2Nk7NFDjoEgN43r4SP6HAaIMRXYxjIQKj19V0_uOgELg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🍏
درحالی‌که شرکت اپل ایران رو تحریم کرده، قمی‌ها طی یه حرکت عجیب، همزمان با مراسم معرفی محصولات جدید اپل، خودشون هم به‌صورت جداگانه یه ایونت برگزار کردن و از آیفون‌های جدید این شرکت رونمایی کردن
🙁
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/71549" target="_blank">📅 23:31 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71548">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac8d39358d.mp4?token=efwujyZQqoBB-Fqp30xqSb2i_UHe8rlbpDzN-gfW613_sO9mBlTCTU8FELSm_BAmDeSIxOHhlSkUVqc-1ax72ikOUoc4pdTQ4w_ZhVias0lVUbmsyMeLVGOPXXeOTk7y0f8BoGiuX6mvM8xNEeS_K40CCDWr1gP3V5LtE9EPb2bUt9y2wlTKtNflWfgMhRAynD4UHsS3xS9nUMetPoFOwjPPs6rzVBoo6vlYnkh4t7G16tdCbbkY3kCwLqL4gkhCxBnzPp2Zwkt-SxbJC_KaYtyJzEi_kTBrAhQXVgzWnppKX6V7t5zxitQT7mnd8Z-pODqEJY-0frUq6ik1LJIgTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac8d39358d.mp4?token=efwujyZQqoBB-Fqp30xqSb2i_UHe8rlbpDzN-gfW613_sO9mBlTCTU8FELSm_BAmDeSIxOHhlSkUVqc-1ax72ikOUoc4pdTQ4w_ZhVias0lVUbmsyMeLVGOPXXeOTk7y0f8BoGiuX6mvM8xNEeS_K40CCDWr1gP3V5LtE9EPb2bUt9y2wlTKtNflWfgMhRAynD4UHsS3xS9nUMetPoFOwjPPs6rzVBoo6vlYnkh4t7G16tdCbbkY3kCwLqL4gkhCxBnzPp2Zwkt-SxbJC_KaYtyJzEi_kTBrAhQXVgzWnppKX6V7t5zxitQT7mnd8Z-pODqEJY-0frUq6ik1LJIgTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇺🇸
لحظه‌ای که جورج دبلیو بوش خبر حمله به برج‌های دوقلو را دریافت می‌کند
جورج دبلیو بوش آن صبح در مدرسه ابتدایی Emma E. Booker در ساراسوتای فلوریدا بود و برای دانش‌آموزان کلاس دوم در یک برنامه کتاب‌خوانی حضور داشت.
نکته جالب این است که بلافاصله از جا بلند نشد و کلاس را ترک نکرد. چند لحظه در همان صندلی ماند و سعی کرد آرامش خود را حفظ کند تا دانش‌آموزان وحشت نکنند.
چهره‌اش به‌وضوح تغییر کرد و حالت شوک و نگرانی در آن دیده می‌شود. دانش‌آموزانی که آنجا بودند بعدها گفتند تغییر حالت چهره او را به‌خوبی به یاد دارند.
جالب‌تر اینکه او حدود هفت دقیقه دیگر در کلاس ماند و بعد از پایان بخش کوتاه کتاب‌خوانی، از کلاس خارج شد و در همان مدرسه برای خبرنگاران صحبت کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/71548" target="_blank">📅 23:02 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71547">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0e621bd826.mp4?token=SboTOc4FCPGR4UTy9LHjSWtPdz_4lyhImQjXXywl3UKry65Q5sktE8X5LcgG9WV8d0v6cY6Ck46NvrH1j3X43S0fu0zWJ1vwxGygc4LdqQYq4RBp3dUAorrsj3ekWh2SdL0UOuqQ2oZnKusSld26sRYuJpClGxt-BQ4DJTQftwbwMqg4Ss8hE9Zd0Q2wxoARpGyHyU7If-qjXvjbH12w0RTlU5VFSPhcJMQvc49-kVfUyZ7mytomNOyStBBV0zOjT0IpDzOL3e61GccpUd29EKrGqCIldbChSqoIXqYLiGreT5kfepll_KiWdHxsFIgrUlDz0E_edJZfZGPXQJdF_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0e621bd826.mp4?token=SboTOc4FCPGR4UTy9LHjSWtPdz_4lyhImQjXXywl3UKry65Q5sktE8X5LcgG9WV8d0v6cY6Ck46NvrH1j3X43S0fu0zWJ1vwxGygc4LdqQYq4RBp3dUAorrsj3ekWh2SdL0UOuqQ2oZnKusSld26sRYuJpClGxt-BQ4DJTQftwbwMqg4Ss8hE9Zd0Q2wxoARpGyHyU7If-qjXvjbH12w0RTlU5VFSPhcJMQvc49-kVfUyZ7mytomNOyStBBV0zOjT0IpDzOL3e61GccpUd29EKrGqCIldbChSqoIXqYLiGreT5kfepll_KiWdHxsFIgrUlDz0E_edJZfZGPXQJdF_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیروز تو مشهد اردهالِ کاشان، از " نمادِ مشت گره کرده‌ی علی خامنه‌ای " رونمایی کردن ولی انقد بد ساخته بودنش که صدای طرفدارهای حکومت رو هم دراوردن
😂
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/71547" target="_blank">📅 22:15 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71544">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/C33eF0JDU-YlqUmgTPpk23_x6u0S7IBea4MwH-txTlOhU8E70VlRzu2QZwsf_RCd8Bd4cqqbn6RoseCC8B5KhntweGU5tbEtzLXuMLhmjt6C5a3SyCIdal6dlDdR0Azr4kS7TQC8bekOHLJxVAlT-xHtuEypk4Hd68uqIFhwo8baKzliy80wqPJPXYoPttA8WWD0tKqdOapVlOeVXo4LAgKT4UAlNWHaX1hWihTZhoPuEJmsA9oUgHsCP7K4bwLc6teO4kcmmm3inbQ1p43MLpGqgEvOHynq7EszSmVTQTQ0Z8jaqgUNHPWyqGD4Kd3M26cJCTZVgXKTqQ6cHx9A8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/oGs1ek--3yx57Fv31CXquGyfjajCVDRdZ9-38KritNmSZzvnRgc-QN20aMf-0_bbQQ4ZwaNmeum253XbN7aGpEWLislhtJT6AicqNiTdW0cLVgAVs_jV_AoUHjeNnKFOI5AKwuIJESpzmzSgv8N-6f_7-rK2dL0_LDkDjguS-UoS0H1dILuLOvl_Gy-EnK34jCijoJIkX54phZiXmSfY7rOV-xugSUdeSXPN8ZuXHlCdrzVIcMsdpqm8UInuwHdOHmdByhIrnWjs1kdkNkJMMavLuD-CKakU-5V50WSkditf-Pc9cysvpZaj0wm29Qztk1XHqbGgCDriIhTM1NP5Xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/vwtreMnu03R1fDQs-OH-o1ni7GaWe5q3fmeAE9HtV4-pdaOdZItaz1QIJN-nUXIR8ULQA_UiI9n1GJBiiHZ7LeHhpGFgUUq_UzY2oICWDwggdHEK5ojieCk2JjGSWj7wme3rejxwh1-Uu0Hw1SDbzQTmBY_PJ7o5HMpP8CrYF_OvMyCIRcBx5uZh6vi7wtwIxNCFITVHYy7qmlWiRbQy8MMtKaGvaZFnbyc4bWkZmaPqQY5iY4OTG1fCVz7nY2SacjFKZZUyVU7U91LzvG3jbcNFuGSsHJq9B8M5vJuD-Wn36XPwGZzwr2qgU7rK7GYjHcVmzSQGusE7oaYQ0jWftw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚠️
کشتی‌ها و نفتکش‌های آسیب‌دیده ایرانی در خلیج فارس.
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/71544" target="_blank">📅 21:32 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71543">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🚨
شلیک یک موشک/پهباد به سمت تنگه هرمز
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/71543" target="_blank">📅 21:07 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71542">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XIDrJYcOXg8acPgZgiXYTEWStDS50K5DGmtJgXnsxxrLZIdBmi669cawBtVDSw2z4nRI8-bXq7RsTiEnfR4gcDT9B636KOOml7lqI7m6iVSn4JdYgFIWPQQVUt4iTihYyjaei2ojEiXlFHRtSJ_vVnqRuzRczDa91DhNfZArMHwFNq8d6NFMB1se2qujUJkNNF2nZ-Lnfmco6FduHK_5SzUtLMSLWmiY_XV0jau3xK7HW0KVybMkOjjgx2GgyzMZ5UJbYBiuDSdpRTR3Ppw6Ozlr4iPSEowNW0MZ_LITp8bdNZiJUAcycEr6TXNnGrhjSpAMvDreu7q7BI6GlqPJsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💬
شعار جدید عرزشی‌ها برای حسن روحانی
😂
نهپاد: نفوذی هدایت پذیر از راه دور
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/71542" target="_blank">📅 21:03 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71540">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a60a908ab2.mp4?token=s5_BD8TsbX6IfCLd-SepeaElg53OVfrprZGj5XjP9OWUExe0H8j1sf-PdzpPmpMSaIZWejloSiRdiRoXftPf46N2-kDsTIQaBnpBwhUyYoGNJXqM8m8wVnJCchfnxTCGw9WKXW-fet6YA-SbaBolUPYadDJAFGE_fvwHPsrV3eBtLM1IYPHFLMmMC0VADkXOvkbnogLp_eo-fWWp8clHwGfTH9cENV6rco6cYJdItfTFctrKGwW1FR2A0EuG-LHr7g_IRjPPctZC1jMOvGk_Ki5kUkI42PLDsbsH8l6PWUL-DC2nKz5_p6Ntr2nyji6p6qKagYxAr7lML4vmIEKKVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a60a908ab2.mp4?token=s5_BD8TsbX6IfCLd-SepeaElg53OVfrprZGj5XjP9OWUExe0H8j1sf-PdzpPmpMSaIZWejloSiRdiRoXftPf46N2-kDsTIQaBnpBwhUyYoGNJXqM8m8wVnJCchfnxTCGw9WKXW-fet6YA-SbaBolUPYadDJAFGE_fvwHPsrV3eBtLM1IYPHFLMmMC0VADkXOvkbnogLp_eo-fWWp8clHwGfTH9cENV6rco6cYJdItfTFctrKGwW1FR2A0EuG-LHr7g_IRjPPctZC1jMOvGk_Ki5kUkI42PLDsbsH8l6PWUL-DC2nKz5_p6Ntr2nyji6p6qKagYxAr7lML4vmIEKKVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇦
❌
🇾🇪
حملات هوایی جنگنده‌های عربستان سعودی به استان البیضاء یمن
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/71540" target="_blank">📅 20:19 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71539">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xpd5MQOaKwXuIyrkhWfGu24FRIB_GXK343kueCZEb9UoKfEoA9LaZG5qVWCZ18Wn8eSeF17ie41jjsaew320nrZUoS8TkCKlBm0k74tMZTWO2QZmw8WtVpAgfTed6CBib7KH-QGCqyd5NZPYQxKBxJYgzfxgSPGeYutcNJMunHPaGsjoliQtzNi3ccnRrPCghmS8zwLAFIj3hVnH9_pGAi6csSRMIBB41y5inzOey2pToqTaY4reNjc0Jr1F3jU0GVcQGIA4kWjCHS04VU4koiuNKLvQ7HkN-kn4SDIH3Pxz-pcReW6REQXp1azHriiUR4pHr8Uw96GyzcZX0iqb-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
علی قلهکی:
مذاکره متوقف شده است چیزی وجود ندارد که میانجیگر داشته باشد.
عاصم منیر هم جمع بندی ندارد که اگر وارد جنگ یمن شد، بتواند پیروز شود و پرتابه‌ای سمت تاسیسات حیاتی پاکستان نرود
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/71539" target="_blank">📅 19:55 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71538">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d9ZUqJwzr5JL64I3Arm0NPresq_FnH9Qg20rsfJAI6pJVMPyyyBwth5SeeSe10SJM-LcVIuixUYvEb-mrzYA1kSeWS54lXqjVNI10qw-AvadrS3vU2Lv5ZSY7f7gfm3i4CfV56uW6IFUYZqLR3cjYuuKumGWMJk-JlYdBeCm__MLtodzoeWZfJKiNXJ8UKt8XMLBlM0_WMLC6a_y4k0kri-0C7SsoGQnmWh_1UQJiUlQ-537g_5VRq8fhp_c4zN-1FugNP-HvuyXXx_AynIFsnijXkwTi2rXfr0sMdhi3wCeepqq70ot7_76Vl0ycHNKBqyu3t3soSg0A7Lpl8uo5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">〰️
فرماندهی مرکزی ایالات متحده:
از زمان ازسرگیری محاصره موسوم به «دیوار فولادی» علیه ایران توسط آمریکا در ۶۰ روز گذشته، نیروهای سنتکام مسیر ۱۰۰ کشتی تجاری را تغییر داده‌اند.
حتی یک کشتی هم بدون مجوز نیروهای آمریکایی از این محاصره عبور نکرده است و نظامیان آمریکایی همچنان با تمرکز کامل بر این مأموریت متمرکز هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/71538" target="_blank">📅 19:24 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71537">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🇧🇭
❌
🇮🇷
بحرین اعلام کرد تا زمانی که روابط دیپلماتیک با ایران از سر گرفته نشود، در هیچ‌گونه نشستی با این کشور شرکت نخواهد کرد و بدین ترتیب پیشنهاد عمان برای برگزاری نشست وزرای کشورهای حوزه خلیج فارس و ایران پیرامون مسئله هرمز را رد کرد.
🗣️
بحرین چهار شرط تعیین کرد:
توقف حملات
پرداخت غرامت
احترام به حاکمیت
حل‌وفصل اختلافات از مجاری قانونی.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/71537" target="_blank">📅 19:10 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71533">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b779ef03e.mp4?token=YlFSlblY0lLCOXrOGTmC8t39JVyrj090X3PzP6NCEDbuodiImfrskWBXS8G7TkBVdOFwtLfNDrAzsoIbhlSPkD9_JkLlpXKlAv8Yrc6DfJS8K1Xv9v615-04-xgcy0hAw1C_-9xCG_FO01QKsZcZP87Rk8kHiNxlGGnrJ-6mTHA3u17_LdQcdWOpJRPXwAwlmcozY7WlUba9ysEl_96OX8Nvd-HAtjTv1tYY25-VAidIJ-ZY-epMjisVYpAYv20viq_TCdQtPm91jwddxFaXXVTNDa7SxQy9SiaJyw62WL2Nv7N8ie7GmQBd2TwitF3O0BpZQUNPJriXh3-9Nm-xIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b779ef03e.mp4?token=YlFSlblY0lLCOXrOGTmC8t39JVyrj090X3PzP6NCEDbuodiImfrskWBXS8G7TkBVdOFwtLfNDrAzsoIbhlSPkD9_JkLlpXKlAv8Yrc6DfJS8K1Xv9v615-04-xgcy0hAw1C_-9xCG_FO01QKsZcZP87Rk8kHiNxlGGnrJ-6mTHA3u17_LdQcdWOpJRPXwAwlmcozY7WlUba9ysEl_96OX8Nvd-HAtjTv1tYY25-VAidIJ-ZY-epMjisVYpAYv20viq_TCdQtPm91jwddxFaXXVTNDa7SxQy9SiaJyw62WL2Nv7N8ie7GmQBd2TwitF3O0BpZQUNPJriXh3-9Nm-xIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇦
❌
🇷🇺
اوکراین  به اهدافی در چهار منطقه روسیه حمله کرد که حملات ساراتوف تایید شده‌ترین و چشمگیرترین آنها بود.
مرکز لجستیک عظیم اوزون در ساراتوف (با بیش از ۱۰۰۰۰۰ متر مربع مساحت، بیش از ۳۰ میلیون قلم کالا ذخیره شده، تا ۹۰۰ هزار سفارش در روز).
طبق گزارش‌ها، پالایشگاه نفت ساراتوف (روس‌نفت، که قبلاً بارها هدف قرار گرفته بود) نیز آتش گرفت.
در ولگوگراد، فرماندار تایید کرد که آوار به یک مرکز صنعتی و یک ساختمان آپارتمانی برخورد کرده است.
منابع اوکراینی می‌گویند که هدف صنعتی، پالایشگاه ولگوگراد لوک‌اویل بوده است.
برخی ادعا می‌کنند که از موشک‌های کروز در کنار پهپادها استفاده شده است.
انفجارهایی در انگلس (محل پایگاه بمب‌افکن‌های استراتژیک روسیه) گزارش شده است، اما هنوز هیچ اصابت تایید شده‌ای به فرودگاه وجود ندارد.
بنا به گزارش‌ها، منطقه بندری کاسپیسک/داغستان نیز هدف قرار گرفته است - پس از حمله تایید شده شب گذشته به بندر ماخاچکالا.
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/71533" target="_blank">📅 18:52 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71532">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71532" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/71532" target="_blank">📅 18:51 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71531">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SCaltWAthz4w9p5yUQPzTdQe8dyeZFUuNFCBjth7tHF_CNsCRENomPHsJ1W3ODn5V0oaLaPRgRX2wBV1ijklc6XLrTQfCfiSgL0VSUWe2Zhce8EKKiqsh0SV1AM1b_USW4nWxEUNq5ocMpngVNsx8i1nH3JMdHHHnakN0YCpCDK8hrz5yBj7ERBe56sfK8t3gZPeZaP5Y7jHfdhYQ_rZ09NcEkbfWzpzpYRTeEZszx5Zvhn3YtjYU_8L1zsca9y__aCiSCUIRHg2mfLY8Jy8iNM-edKjjcWy7MwbdYy-Df_xe7D4JrMNjrzdfHCkwq_AZehviAIo4kkcCWr154K8lA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
نبرد هیجان انگیز
⚽️
میلان
🆚
لاتزیو
⚽️
را در
TrexBet
پیش‌بینی کنید.
📉
نگاهی به آمار دو تیم در ۵ بازی اخیر:
⚽️
میلان: ۳ برد، ۱ تساوی و ۱ شکست و ۹ گل زده
⚽️
لاتزیو: ۴ برد، ۱ شکست و ۶ گل زده
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
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/71531" target="_blank">📅 18:51 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71530">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/554b629d89.mp4?token=HNa0R355CITL93CvmkksypHLrijKhrtxV9qvoMZKa0eS-chuBYZMZNpganyUAzbpW1yu3spVC7QOoVMUu_-_Sdk-veFZNDaG1UL42EpKGOyJtBC2_-c8hij8bDtXZa6Y2VmT17twW4G2keB_-Bz6ySmB4Dq1FGO85HfSLheprJMOUpijSZi40SfarpYyQxVfzKoFE3vL7mQ9BEIgD2PnBGt5tiw8gYQ3iZ-TQCFZ3g-zz74xgXkso7SCTl0WoN369iJbu91b17NFu6LLCwr0fjJ6ZLGK5s0Qd0scrym2oWbNAIu0W8nerKPS-D9cAA2zsc0TX8nvB_0FQ9shIK1WY5cE8ZK_XwTQzda-YHHLBEn12KTnY8vrbaRBIgF5taMoMCFwBl0RMQAvX2z-gKjcbZ7UQfcFD3tZ6UUVHxqwLlAp-vv25Uvd3N6y0m8-Lf4OyxA6J2KhcfmmLet7WyPLdU3iZG5-jGT3OfjcfuSxWyCVqJOeoUB_kGJC7jqmlZSFr3mbPYb_YjGNHDOENRxr-mqqcukHaTOPlA0BQ-99XJVQ5_RP8C1aAKC7mJ7tBz_qitFaRzMo7QuCN7PCWOUCC-MZVIKciR19kRKJVh9TnLSzgIuaHjF8qYVbXcF3awwuWenbR9V5-Q4dSkAd_pmpcWtwleBLvdzDaEcw58uh1ls" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/554b629d89.mp4?token=HNa0R355CITL93CvmkksypHLrijKhrtxV9qvoMZKa0eS-chuBYZMZNpganyUAzbpW1yu3spVC7QOoVMUu_-_Sdk-veFZNDaG1UL42EpKGOyJtBC2_-c8hij8bDtXZa6Y2VmT17twW4G2keB_-Bz6ySmB4Dq1FGO85HfSLheprJMOUpijSZi40SfarpYyQxVfzKoFE3vL7mQ9BEIgD2PnBGt5tiw8gYQ3iZ-TQCFZ3g-zz74xgXkso7SCTl0WoN369iJbu91b17NFu6LLCwr0fjJ6ZLGK5s0Qd0scrym2oWbNAIu0W8nerKPS-D9cAA2zsc0TX8nvB_0FQ9shIK1WY5cE8ZK_XwTQzda-YHHLBEn12KTnY8vrbaRBIgF5taMoMCFwBl0RMQAvX2z-gKjcbZ7UQfcFD3tZ6UUVHxqwLlAp-vv25Uvd3N6y0m8-Lf4OyxA6J2KhcfmmLet7WyPLdU3iZG5-jGT3OfjcfuSxWyCVqJOeoUB_kGJC7jqmlZSFr3mbPYb_YjGNHDOENRxr-mqqcukHaTOPlA0BQ-99XJVQ5_RP8C1aAKC7mJ7tBz_qitFaRzMo7QuCN7PCWOUCC-MZVIKciR19kRKJVh9TnLSzgIuaHjF8qYVbXcF3awwuWenbR9V5-Q4dSkAd_pmpcWtwleBLvdzDaEcw58uh1ls" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
پست جدید هیچکس (سروش لشگری ) توی اینستاگرام که وایرال شده؛
«هنو به یادتم»
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/71530" target="_blank">📅 18:15 · 21 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
