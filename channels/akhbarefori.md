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
<img src="https://cdn4.telesco.pe/file/gGqzAfwT_q-OmEUkRMRaUVE7hAV667MKtdi4Z_LS0S4J-0J-gmPaKcgHIVEbI2mmtcJa1KjHQ2W9JH6gwvCuARQt1UN0kBclRMU3u6fRZ-SyT6_XV3N-ojir149mFMr9BWPaQITHvI8b0NZfUT0GJO6Jd3Cd2omQdh9aeq_jTDvQfNySwCy2zaVbWqVe4Pz01Kr_9MxECGJp88YJibIeux4FTF0F3RvNieljWeQorObpFmbTsvzFz6L39rrUWqakfYdSk6l1eFdRbzP9wWmfVlYV55T1dzgA7_5iSJeScCETehwJpRh0NzFpWiiCpiEsX7NiErNIvOTP78kSKctPiA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.26M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-05 00:54:15</div>
<hr>

<div class="tg-post" id="msg-675625">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/850e2e6b24.mp4?token=N6GL_lpgKvn3VdDkFRTmrs5Il1q8x4p4d6sh8tgniDozkFC6kjPHjMRMACAivCuoQf1CLMnqrT4bKvlX_qGUkFovj59mKk60EUhd4JpOPOS9a6X_Gh0i99zSe8_GcKVo6fivRIliLXAoN6CTuA8eBcoHU0ZKr_La2rqC2WTj2pOjjUcCd3aT4KQe2VLQ1tOXfc6W9hgdYSESEJTxhV_a9IV2rFfiC39K4veaWcStRoGeNnqGsXsj2YmUSIP6ftjNJjrV8_1_qpf4I1_S1bELkcHaikBOC_Mvo2xx3fhjlCKR_Ou3py-HAJSagM3oYgdHHF34f_QKRMitqcp8-0Kl8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/850e2e6b24.mp4?token=N6GL_lpgKvn3VdDkFRTmrs5Il1q8x4p4d6sh8tgniDozkFC6kjPHjMRMACAivCuoQf1CLMnqrT4bKvlX_qGUkFovj59mKk60EUhd4JpOPOS9a6X_Gh0i99zSe8_GcKVo6fivRIliLXAoN6CTuA8eBcoHU0ZKr_La2rqC2WTj2pOjjUcCd3aT4KQe2VLQ1tOXfc6W9hgdYSESEJTxhV_a9IV2rFfiC39K4veaWcStRoGeNnqGsXsj2YmUSIP6ftjNJjrV8_1_qpf4I1_S1bELkcHaikBOC_Mvo2xx3fhjlCKR_Ou3py-HAJSagM3oYgdHHF34f_QKRMitqcp8-0Kl8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عملکرد تصفیه‌ شدن فاضلاب با استفاده از لخته‌سازها و فیلترپرس‌ها، لجن را در کمتر از یک دقیقه از آب جدا می‌کنند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 1.32K · <a href="https://t.me/akhbarefori/675625" target="_blank">📅 00:53 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675624">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">♦️
شیطان زرد به وال‌استریت ژورنال: ما بسیار بیشتر از هر کشور دیگری در جهان و بسیار فراتر از نیازمان مهمات داریم
#Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 3.37K · <a href="https://t.me/akhbarefori/675624" target="_blank">📅 00:48 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675622">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/si_vqycMFv7tMyfuGbEs0pxgjn8W4BFpOx5z0ANhZa7KCeyxRmvvk7gwy1-loinstpNd0QraaY_JwpMjVGpGYQyXCY0K9J65j34HVzUnj0QJs20L8pNqi4k89d_z2v95AgzASODCq6JehOx0hTisr9OloHvEgfcfBHuARLmEWFWJbSbaEEM8BkALWq-0PU7ykfXm7kVn8t9IKoLLOCXXNStm3bpuJlxgBEgu8d6pCxwzVBZg3UPDJi0hKm2EeDPZeZ2jYp9ZYPgtX8ihGWFLYFtyOZKWhWzXPhNuEl8rjJytrSYcJp3tp31yIND7kKIfZW7Cvc9_em7Ua4IO114j2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
درخواست دختر اکبر عبدی از مردم برای اقامه نماز شب اول قبر
🔹
المیرا عبدی، فرزند اکبر عبدی، با انتشار پیامی در صفحه اینستاگرام پدرش از مردم قدردانی کرد و خواست برای آرامش روح پدرش، نماز شب اول قبر اقامه کنند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 8.77K · <a href="https://t.me/akhbarefori/675622" target="_blank">📅 00:40 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675621">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b348c813e.mp4?token=JmSH7pKTkS0pi8wFn88TfXWqL9Fu36YaLir9_q3Q8I-hrMpkGfdqJATjgHggne-CEWXcRktEF1GP-KbjfTpV1xU2gbTvFBv6YLwk0gxZvYy_e6wYbPKsJHgpOOS4mq-GYFNRvwarDd_JLAGn6SKszW-bkTzyzzM4xISLm1M1AK9o7_w1GBGl_0Y1KZLOa9b7jJ0v_XQE2zvzffr_Ujqv91a03Q8Z1AQh5rsY814FnV4UydN0KFfZ6VgsJSEKvb-GEVbkVRJuVkiAKU90OHxgG70KktFZJLNMqeMVj3YEI0pxvAoW6UEmpDjZwxSdrud3rI0GwIeQmfmmpVKfvEl2eA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b348c813e.mp4?token=JmSH7pKTkS0pi8wFn88TfXWqL9Fu36YaLir9_q3Q8I-hrMpkGfdqJATjgHggne-CEWXcRktEF1GP-KbjfTpV1xU2gbTvFBv6YLwk0gxZvYy_e6wYbPKsJHgpOOS4mq-GYFNRvwarDd_JLAGn6SKszW-bkTzyzzM4xISLm1M1AK9o7_w1GBGl_0Y1KZLOa9b7jJ0v_XQE2zvzffr_Ujqv91a03Q8Z1AQh5rsY814FnV4UydN0KFfZ6VgsJSEKvb-GEVbkVRJuVkiAKU90OHxgG70KktFZJLNMqeMVj3YEI0pxvAoW6UEmpDjZwxSdrud3rI0GwIeQmfmmpVKfvEl2eA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدیویی از یک تصادف در چین که دو طرف حادثه تا رسیدن مأموران، همان‌جا منتظر مانده‌اند و ظاهراً در این فاصله سرگرم گوشی‌هایشان شده‌اند، در فضای مجازی مورد توجه قرار گرفته است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/akhbarefori/675621" target="_blank">📅 00:34 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675620">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mZgP8mnt6r-1PV_o8e-pP2nw7RD4-B6FT28yPSgVY7lspYyygNYbgxA54keapS7JQ3ewRHV9eQzRiok2TPTmqqoG4vz4Wy1nfYmwZp4GuLTE4f7_KyOMIqekeppZN-IFv_TqAF5lxGiDvycaU24_6LW3D1fsjwHQCE9LOIxIWSg0QYM7iorQ0mdVZff286ErfB-s0HRshtmDLVxyCzTyQdHbtPedl_B2xbvdDqYspqdlBkxL02hhF1jhMOWN8LIfArIOrtG-TK82zfofh4O_NnPotozsXY28_Ef_SCJKjxS9z79abIA7uVrmG5pn0w4MLmWs4zPey8nFal0gzYWzxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شیطان زرد با کمک هوش مصنوعی به خط مقدم نبرد آمد
🔹
رئیس جمهور آمریکا طی ساعات گذشته پستهای مختلفی با کمک هوش مصنوعی در حساب خود در تروث سوشال منتشر کرده است.
#Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/akhbarefori/675620" target="_blank">📅 00:22 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675619">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3212f3f8f5.mp4?token=cm6Ew1544AWO9SeisSIR2oAYgco2tzEjd7uYz8v7GqKYDpO5SgW-wzwoFqag3lNA4DlbSF40EltPqU7ThkIIgsuK3exFXISKJ4pvY9LDSSa8dgsB-daL0yK9CR5MX2Hs2lfUGPAeKtk8dmKm6qDZBxxq9yRsIyErTTxtL0Tb2dtJa5gupgW-m3YD6Ri0rbJteVIrgFDe3Q1YmzB3VjL-UWzO0JXc_N1BgOt7YapC0-qZiPTuM-SeQZ7fVUjyZyq49TiukYHVCXFTbVmo_X9OFQPXINUkn9iwmZj04_DcOfAHmoo6tbaPNzGzou_N7EoRBaSoOOlgM28NgvwOkwPBWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3212f3f8f5.mp4?token=cm6Ew1544AWO9SeisSIR2oAYgco2tzEjd7uYz8v7GqKYDpO5SgW-wzwoFqag3lNA4DlbSF40EltPqU7ThkIIgsuK3exFXISKJ4pvY9LDSSa8dgsB-daL0yK9CR5MX2Hs2lfUGPAeKtk8dmKm6qDZBxxq9yRsIyErTTxtL0Tb2dtJa5gupgW-m3YD6Ri0rbJteVIrgFDe3Q1YmzB3VjL-UWzO0JXc_N1BgOt7YapC0-qZiPTuM-SeQZ7fVUjyZyq49TiukYHVCXFTbVmo_X9OFQPXINUkn9iwmZj04_DcOfAHmoo6tbaPNzGzou_N7EoRBaSoOOlgM28NgvwOkwPBWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خادمان عراقی اربعین امسال با سینی‌های موشکی از زائران ایرانی پذیرایی می‌کنند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/akhbarefori/675619" target="_blank">📅 00:06 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675618">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e830fb3882.mp4?token=MWFDK9f21sDMevHMhJch3tGk3uCTLYrKaAsLC0rwCIvOAzhYqFKu4hGd04h34R4U-rSFzU_KkyzKXoCb3ucSIIDZbZNX3R4q_z7NBTsUcFIGt14VBBrAuoakJaxgfucHfer_9LvNYrStCk1gnZeXv0GykYCWTQrbfnjasaBjyGKvvm0S3q1FTk6Nrx77z8VJ2usy4qzvKqerR9_iHRnPmoRe3A7wNgxk518GDmXJkTeLqXqdja1l7Y9U7DUN7rE5shUbYoTl7PS5sPB20pHvwp_rATGAu1UeKSKHAmgv-6MyLQZkJ3vY6gD_oErqTqEVrIfqmJe3p6CQ7Tsq5cBEFDHebgUVvtbA39TSH_m71kIi94JrobvJXqh1mnsIB9HWYZWp3krrhsMqSAFXkacX5YvTkqMeQRuu_fxBTO34y1kLIg8Q87Zg3XfnPleUrDHZWPMvMN0JlWQqolRItPahsbH5J54FKOIIYgShnyW394U3D0mnwXx5DeCTZNYGfklm_RzJDmVcgi2hFoKNh446JbDRCjTFGhrCFu0BuobGRk296M1ZesieA7LTzI66SYTTpZ3T56APEkujjB5fDOnOpkUwr6EtEJ4dfech4jrFUAcQism39UX2MtDJTRUpnS-OArp72vZcL6wiWmPEHSfqwxK08pW6LkwuhBPfi-BBOxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e830fb3882.mp4?token=MWFDK9f21sDMevHMhJch3tGk3uCTLYrKaAsLC0rwCIvOAzhYqFKu4hGd04h34R4U-rSFzU_KkyzKXoCb3ucSIIDZbZNX3R4q_z7NBTsUcFIGt14VBBrAuoakJaxgfucHfer_9LvNYrStCk1gnZeXv0GykYCWTQrbfnjasaBjyGKvvm0S3q1FTk6Nrx77z8VJ2usy4qzvKqerR9_iHRnPmoRe3A7wNgxk518GDmXJkTeLqXqdja1l7Y9U7DUN7rE5shUbYoTl7PS5sPB20pHvwp_rATGAu1UeKSKHAmgv-6MyLQZkJ3vY6gD_oErqTqEVrIfqmJe3p6CQ7Tsq5cBEFDHebgUVvtbA39TSH_m71kIi94JrobvJXqh1mnsIB9HWYZWp3krrhsMqSAFXkacX5YvTkqMeQRuu_fxBTO34y1kLIg8Q87Zg3XfnPleUrDHZWPMvMN0JlWQqolRItPahsbH5J54FKOIIYgShnyW394U3D0mnwXx5DeCTZNYGfklm_RzJDmVcgi2hFoKNh446JbDRCjTFGhrCFu0BuobGRk296M1ZesieA7LTzI66SYTTpZ3T56APEkujjB5fDOnOpkUwr6EtEJ4dfech4jrFUAcQism39UX2MtDJTRUpnS-OArp72vZcL6wiWmPEHSfqwxK08pW6LkwuhBPfi-BBOxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
زیاده‌گویی
جولانی: ما هرگز نباید مجبور باشیم بین جاه‌طلبی‌های اسرائیل و ایران در منطقه یکی را انتخاب کنیم
!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/akhbarefori/675618" target="_blank">📅 00:03 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675617">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/toTtHKhU-3EUElbukAZzZ0CgWszrU0WvIpFByaMz6CrV396JjnjXh_V_xZK5n7Op48S7fKPgLbh7clZh83OIOR7GAKpkkNmjJfNq4xr0VfUNFD3de-c5PB0-P6BUg6A6n00beNoRPT42U2wZ4JpZhkfXJNsW2j5YMb4b78txlNfVxuIVdvHOhDGvREngshnNL_J-01-Z3ZvCIofgdI1UfaxKGuMnLNfm2enoulQmY3oZSe1aFgL-II3SZUJ_UOsQ2W0FuBPesIBh-znH7QlFWCRc8Ey3qZrS9nmvNSKzmsPShxnqwFu7K1ejeX84C1xzuvh9TZn_nh9eeF4DDDizJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.38K · <a href="https://t.me/akhbarefori/675617" target="_blank">📅 00:00 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675616">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/84cd7cb3c4.mp4?token=KIm62_BGHVNLrizDhHxKK5cDpRQLzG7yT8li7qD1Cj3Lr-2mRr60eImInnEuZEI_avEKp-acKmJ9LA3JcgllY-sRHDesBrXj28rnP_L-8FzrWGFoVQJ17mriIU10SLjKbaqr7xg6pfuGnLpWOoaHy7viotYECzM-dXTD5Upm67VRY_wJSycRg2M-H3Y5rdi23ghdutb6loDC2cvrViJCX-iEWikDGcZUQtrC5NGnngPCdk_5xif0uVVDyQbnKlhnE4J1VA4iyJwahOYEfbWASpLaFWyrN3_PSteS4GC3IIVorWctNY9cPgxugG41wHop_CcwK64sPJH6Bb7-9sYS6TzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/84cd7cb3c4.mp4?token=KIm62_BGHVNLrizDhHxKK5cDpRQLzG7yT8li7qD1Cj3Lr-2mRr60eImInnEuZEI_avEKp-acKmJ9LA3JcgllY-sRHDesBrXj28rnP_L-8FzrWGFoVQJ17mriIU10SLjKbaqr7xg6pfuGnLpWOoaHy7viotYECzM-dXTD5Upm67VRY_wJSycRg2M-H3Y5rdi23ghdutb6loDC2cvrViJCX-iEWikDGcZUQtrC5NGnngPCdk_5xif0uVVDyQbnKlhnE4J1VA4iyJwahOYEfbWASpLaFWyrN3_PSteS4GC3IIVorWctNY9cPgxugG41wHop_CcwK64sPJH6Bb7-9sYS6TzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
در اوایل ماه مارس، لیندسی گراهام پیش‌بینی کرده بود که حکومت ایران ظرف «سه تا چهار هفته» کنترل شهرها را از دست خواهد داد و مشارکت گسترده‌تر کشورهای عربی، «شتابی تقریباً غیرقابل بازگشت» ایجاد خواهد کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/akhbarefori/675616" target="_blank">📅 23:58 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675615">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32d175a29b.mp4?token=OQrq8XEVWeV3RxPWYnYQHfLXoaZRl7eAaC83MkRT8AzyNjZjImZf5YYNfxTqk7YnatxRJly8NlFIcSAX0XJiHiMjVtc1-_geVW9nCCRep4xMWALMJiaITBuKm3QEgNKoBTIthE_6lMMNQZyiQkwa8kFyfZ1YueJSx0xekxsVWaKAjRm0cUJ3GJiAmojiXvqxIn7bOBHrPA_CLRtCqvOjlX9G__947Xxa8k2dL9s0Wt00f_r-kFT5fNFG1UzuXItLEVAgFlbM6cORtPmGKl19tEkVqM9BSd1JcRfQg95Jk0gVk7pQMYY5rbEjRcapwfHFe9ubUwvWqqf91ERhhf6hQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32d175a29b.mp4?token=OQrq8XEVWeV3RxPWYnYQHfLXoaZRl7eAaC83MkRT8AzyNjZjImZf5YYNfxTqk7YnatxRJly8NlFIcSAX0XJiHiMjVtc1-_geVW9nCCRep4xMWALMJiaITBuKm3QEgNKoBTIthE_6lMMNQZyiQkwa8kFyfZ1YueJSx0xekxsVWaKAjRm0cUJ3GJiAmojiXvqxIn7bOBHrPA_CLRtCqvOjlX9G__947Xxa8k2dL9s0Wt00f_r-kFT5fNFG1UzuXItLEVAgFlbM6cORtPmGKl19tEkVqM9BSd1JcRfQg95Jk0gVk7pQMYY5rbEjRcapwfHFe9ubUwvWqqf91ERhhf6hQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پست جدید شیطان زرد: دشمن را دچار کابوس کنید - ترامپ ٢٠٢٨
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/akhbarefori/675615" target="_blank">📅 23:54 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675614">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qDW1eFPEfU-Tqu6q9OpcsYsTpjxdgawaP0l6E5RZ_y9RfzuIa4UjVxRVg3xRqYOPv9K8UX3ndEfvDQbMGDiTMhGzTPj-v7vt-Hg_VIdDGrpYAWdGB9yQ2MvcSUbvNYPKf57_AwNXLgvMLm6tSWD01cuqkvTLAYC7P4if8CrlJbw3amXWOfwYR137wBhvbNU68q0ixqGSPCAqa3QUSC0dV-PyRkq74BogWd80O0GMT58aISzmOPwbS9UbZh54atfOAwzGNp_JykOqPtA3bmIHyASXixCZBmH91IL5jrJ58wwUrJplzDO30jIShgyvujHghkrwLQiWRGHq_25spenfCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
غریب‌آبادی: دیوان را «فاسد» می‌خوانند، چون جرأت کرده جنایتکار مطلوب واشنگتن را تحت تعقیب قرار دهد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/akhbarefori/675614" target="_blank">📅 23:52 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675613">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93448d9c96.mp4?token=mpiYBlBFz1oAI3a7ujz-7wrdYBzjpaG9ZvgJDgb5QDM7C0hsTZ6TtvG80JszVZOusZtDYJ9OkM8tV-YSfB-8VKCT5bY_Jz-PLGjh2MStBvr1eJQ8yN8jIwq_bZRdagM1-5hUyBqJdJJPl5mQQbWi3kkVemBXSosilvwB8EEzzTNxDYrraAEYyCDDIWkZaQSBUH-Q30UuwVrznnIW07FLnnGhmWO3uM_tloM8LIPvOrSvHMWQ_Pat9QXz3R0MWgsZCnXRjtKRGWU52iwDozaC5gZzQkuPeZC-3moSpFlRO88jL-PezYQKyQuO6URcXUZPRam6LGRsg5S5VYleMdof6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93448d9c96.mp4?token=mpiYBlBFz1oAI3a7ujz-7wrdYBzjpaG9ZvgJDgb5QDM7C0hsTZ6TtvG80JszVZOusZtDYJ9OkM8tV-YSfB-8VKCT5bY_Jz-PLGjh2MStBvr1eJQ8yN8jIwq_bZRdagM1-5hUyBqJdJJPl5mQQbWi3kkVemBXSosilvwB8EEzzTNxDYrraAEYyCDDIWkZaQSBUH-Q30UuwVrznnIW07FLnnGhmWO3uM_tloM8LIPvOrSvHMWQ_Pat9QXz3R0MWgsZCnXRjtKRGWU52iwDozaC5gZzQkuPeZC-3moSpFlRO88jL-PezYQKyQuO6URcXUZPRam6LGRsg5S5VYleMdof6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
الموت ثبت جهانی شد
🔹
سی‌امین اثر ایران با عنوان «دژ الموت و استحکامات دفاعی وابسته به آن» در فهرست میراث جهانی یونسکو ثبت شد.
#اخبار_قزوین
در فضای مجازی
👇
@akhbarghazvin</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/akhbarefori/675613" target="_blank">📅 23:48 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675611">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rb8V3CIiFryptBN3JbUNKTFBL0_uR1kBxPA5z__dYNCJmYndgLWTyVjixRHfjRJ9M-8b1tMCy4i55dVpfbnWRtVEWpUx_LM7ijmg9FkNGHNXHwF6q5-adroiJI09-AxDoTuDztx6h1rJry8655KDk_JDm-dmIX9FAUov881Qe1FDzIMV7BNmChwkSaL6L81qaxiz7hP-fUklVD17-fngiiqpMeot-jS7BWYENO88gGIUQSVDiM_CWD6z_59T0lgQGCVtLzZCh1y3Zs9AzgIrI8jo3PpSUgzzhl2BJHcikUuELgALfCsZyWq40qwXOxVPsiMuW7jFGOHWE1BA4GR1lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X5hmxNkYoZ4HDF8KPJnKSvHL3-ATp2utTyauaXiRGaVZKSq-sdmNrybCFZ7KxXjwgk31P2u_97xVVqHHLLf-CKHBrx-0u5-xZKOJgiSqL_7H1Qr6WO9v5ueBlYjnho2zNPDfCYDbdyLtdMOJC4vW3RWTsEgxewO_0yheXwWskyLCY9WEsX69-yMCnGlvI0qj1RH1drVopPEbe9eIkXQnPun8T_lClZr4d92rPIJgjkKTULRSyvIBpbcmA6C87UER94ATcsV0HePbumbEdIet63CTOpoD9xMAPxqMX96AbXJtn4F7RL-m9eYsbcnD6iTYf31kjJHHdE0DruunOvSnXA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
اگر برای تربیت دینی نوجوان خود چالش دارید، این کتاب را به فرزندانتان هدیه دهید
🔹
«نامه‌های بلوغ» میراث فکری و تربیتی اندیشمند بزرگ، علی صفایی حائری برای همه جوانانی است که در آستانه انتخاب‌های سرنوشت‌ساز زندگی ایستاده‌اند. او با زبانی صمیمی و عمیق، از بحران‌های بلوغ، آزادی، انتخاب، اخلاق، عمل، رضایت الهی و ساختن شخصیت سخن می‌گوید و همچون پدری دلسوز راه درست زندگی کردن را نشان می‌دهد.
#فوری_کتاب
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/akhbarefori/675611" target="_blank">📅 23:46 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675610">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c89c9b87c.mp4?token=toeOs7V_SP1Qgs06ndFEMdLezdgSK-lI1LQyNpg2mC9L33C9Zi9RWC3x51ED2SeYxo1XD-t6go53oGYylVYr-NIl__Ipu7gIvjOp1Gk5RC_F01xPx4f-YtGMIAmVUdAsPPusDceau3VpB-2XUK_fh7pmirWxXkrbI5ypn9_gt1kKmt5Zy6pP_DlAG1biFs1Xfa1w9Qt7C3JZawTY2EAuED0BO7RtFApF3KxTmjZ_XyvleQArYRlobQkjtl9zxQ5wX65HNE397BZZ96qBNTNIHLMO5XToXNILAJE87a_EXKy0b0GhOjDD4zMfVFDOyNGiJjOlmxmyPNZqQWyNn8mn7FmbqA3f0RaQDgmKQokrCdmwBzYrRj6zhqQrK5KUVNfaX_6ThiVbcq6DZrGrqUxLMqCvn3ipZz1oe6BKqh_LIsfsOQFKRtiKbxJ7Eqj_M9Jox4wK0lzZpOJZrWivlEJtJVtPOOR-dPxwApztEMbL8WVc3QcuaFuuF8X4hD21NUUDyP3Bh7UNC2HN8I87SqeEB774oFUfT3zaJuqZml_RU1iYQ4czIOJcKTMXFZEJLMv1_GnM-9LzETuFOGX3KAFaRBmYVOqzM6d3U7hJpWUn9tkYnMVBbvcX-bCkrWSb2GifGdGn6jvTQ8yR4jPu-Q152jMFfDCsqW4gAKaQruvVoHc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c89c9b87c.mp4?token=toeOs7V_SP1Qgs06ndFEMdLezdgSK-lI1LQyNpg2mC9L33C9Zi9RWC3x51ED2SeYxo1XD-t6go53oGYylVYr-NIl__Ipu7gIvjOp1Gk5RC_F01xPx4f-YtGMIAmVUdAsPPusDceau3VpB-2XUK_fh7pmirWxXkrbI5ypn9_gt1kKmt5Zy6pP_DlAG1biFs1Xfa1w9Qt7C3JZawTY2EAuED0BO7RtFApF3KxTmjZ_XyvleQArYRlobQkjtl9zxQ5wX65HNE397BZZ96qBNTNIHLMO5XToXNILAJE87a_EXKy0b0GhOjDD4zMfVFDOyNGiJjOlmxmyPNZqQWyNn8mn7FmbqA3f0RaQDgmKQokrCdmwBzYrRj6zhqQrK5KUVNfaX_6ThiVbcq6DZrGrqUxLMqCvn3ipZz1oe6BKqh_LIsfsOQFKRtiKbxJ7Eqj_M9Jox4wK0lzZpOJZrWivlEJtJVtPOOR-dPxwApztEMbL8WVc3QcuaFuuF8X4hD21NUUDyP3Bh7UNC2HN8I87SqeEB774oFUfT3zaJuqZml_RU1iYQ4czIOJcKTMXFZEJLMv1_GnM-9LzETuFOGX3KAFaRBmYVOqzM6d3U7hJpWUn9tkYnMVBbvcX-bCkrWSb2GifGdGn6jvTQ8yR4jPu-Q152jMFfDCsqW4gAKaQruvVoHc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری از آتش‌سوزی‌های گسترده در پالایشگاه آرامکو در عربستان سعودی پس از پاسخ کوبنده یمن
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/675610" target="_blank">📅 23:42 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675609">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">♦️
بقائی: آمریکا بستر مناسب برای گفت‌وگو را از بین برد
🔹
تبادل پیام از طریق میانجی‌ها ادامه دارد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/675609" target="_blank">📅 23:41 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675608">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">♦️
نماینده کنگره: آمریکا به خاطر جنگ با ایران به شدت تضعیف شده است
🔹
هم‌حزبی ترامپ و عضو کنگره آمریکا توماس مسی روز یکشنبه گفت که آمریکا «به خاطر اسرائیل» زرادخانه موشکی خود را از دست داده، ذخایر نفتی خود را خالی کرده و بر بدهی‌های خود افزوده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/akhbarefori/675608" target="_blank">📅 23:36 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675602">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MPJiC3kIElHZWQyAgMQYqIx52BrHfJVovoeYAp-oVnuK-i2Kh4q016tHpSoSvwKjPORuLuWqXOvLTac9jH5CjnRvUhgQ9Yf9nEKLgoI-MXYretbiw_LnAVd_WH3oi8N2MzBU-pz0bx_S9LfpQYffrF3E42uUxqcqoEu8X_xiFZDPcYGDMKP9yeMWp7y1xKgblhlfx4fZBsF3Sltwqto-rG-UHxlT0jG4ooOTQJUDgcAN8SJ9jClju46s9tXm8kNtxH8mYoY1Tnz7SexBrjtlBLCZP8snZDePTySe2jf-KC1b4U908ZFY6vKisS80yyOI24YwdA2xPl2J85Cx5N4jMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UQ2e1W0TmWUTB_QOQ9pNebWuyaW0tlvxNxdYH7hf3SufMXS3X8ipVf_8WHXcxoiD7YnYjBoKK05s0HXR39GA-709sknQxp9-vXNx0NtKZI5sbX1PeYlqXpRkBXyusT_Svs99cQNMUch-_8HlW6pWvmpHkQ1IRZ8Fms7qfQpAtcNnXNjNVIeED1H9yCdtkC1GETZPDGFXNZyp_oIIhfNQfmK58nUfDp-SMGjFB0Yqhc_K0Chn_KwksEdYa8Yw9G3weaGuGnqBI0UN5uRLHryzU7UHLj8tTiLHciSA3-UjUdN97CiG-E9Vu7sODQcqVLuaxkNLdwdhYoXEunXNhKmENg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gZxLVfEmfmnlOmWeVIZstBgoStZwbY4bSgVt4E06FtzksEVmYHe0oeAw5hlnlS4L_7Rps86NZWdW3koI5MGmI_ied7gO4KNwaw3DF1dMQU5Kkh8Dm7Zv-q5w_3-XBWG4PeWvZOkeUzDoQhcJXibKSbHFI8lTN4Txcsgma8v27eo18_kOcLvc_L3HQE0X36duAo88u-Iq6jgqzm3-v4_9bdcqJlkX-9HiC1FAhMEoUsCTdRKHTiT6szb4DDdPyBbu4qd-dmBJzhIxrqtVtExh1Ad6cdxefn2JnSOvBy_kbO_nuihnQRxD7AFeeaeAG4tKMx0nWeePbdnDXLnl8R0g6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qwWtMdLToGeQ9qV_FSuOf6qEuwJIEwZTwDoGNxeavR0w7PUDCKn-VYiLcIPj9CKy8kqlfu3Rd9XhsfYeiAljFLE-1vmhtB48wNCHDMpAdpkfSjtgR3gMpUggFiIpyk_UOnCrreRuSvnoYc0vk8s-QyWXsmTeliyhDJCvWulFjnlgW2ziuQhrzWn3QlVg8ielYrHqFNU44TG5qCBw4snBW9h1FmWlxA0_4XUN4nOwVubTRcwK2pASYUCFDPt-TBJkqkOrZKtd7kKWoU-A1pRGBj4paLde2kGi8G6p3DPDAZ3EIbXk-AO2ArSgV0gNLQNwXQr0O7cospNXSGiCCnh8wQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L21MtjZISGzbG0m5hmGMRs2hPxp9Kzs7csowpbioDX49uav_j34eBDw3t9Zw9fVg8rKKbudU9EVAs93pmo7opguZRArtFLAmP50J88HSJslSgmDDNV9lFlL2oasz9o1_zEzn8vwmRMhT85Fs4SfrgfSjSgCr0OBN74KOmFUEyUKEgP-HCPLp4L38Y7aDKKlupXpxIdnGRDKTxyFCdgLOQpr3Ld0W2BQv_bPBMvLZZ0j_rBY0vdn51Cjx-Bquq_pfmaphZIw6nHxQBMFe94igqB1YkGqt4nIYKfr0dAPWumA30ca4Q0OcsE0k0xhRLVTupRyt1k5eIPYA0P-VFT1lBg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f703df7c8.mp4?token=QlhrsrY10Q7nbs9x6kUFWDYgqpDyWazCA9WIRD0ECmjWgj9bJrt4oEulljn1IsBDjcQE1_PDmHVCRwaEmE2R-4wNURE8Eof8uEPKSJYjgN28Jhhf_pkjCNAn3TrohOl9d3q03Q7b_uJ5YKUWXaO3Ll-MUGQUijB9Vg8GGVX49PqjA0v0teEETy5RaS_2QheKE-qTI3ZwzTh65Bjx_uvoNvemSazxVqsqose7rLfgdx4pHDb584MnmatQaix4cUcYdY7xwn6QUj6UDrbqbx3r5Vl6RVarnzbJ6UMFJKS4L4wLJeRDXSRNfN80bmuEySj4MrfSWz5yBFGz8f97dpdVXL6wVqza_LTDYNolniPKKmphjYTYvkyH3wf2ny6Bmrj-6YRSbL5tB3j8z0Rfjp6QWfe0Y5SwU7nwqo1BjXDwyqgeCelbDZt9IqRqWxl3XFZpE7cn9ju3eDn8jdIGRikhk2mUstHHWzkflHpN19xXWB2JBFabesrhKaRVYwhEmWjBjoH-8gVGV4rS1dnkTq4md2cB9MVFXb69JYVDuQqeY-BRsNeNalvevIQ1oKLsRP3h8E-sn105RPuoEdhmb7bfYezkbPiKAr1yZ4JdnNh2gm_5k9FvHHbPh06EsrqmHbFlgwp7gwffMyQQtMvas8Y0pg9ihaLGWO9IL-GXUn_t9Dc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f703df7c8.mp4?token=QlhrsrY10Q7nbs9x6kUFWDYgqpDyWazCA9WIRD0ECmjWgj9bJrt4oEulljn1IsBDjcQE1_PDmHVCRwaEmE2R-4wNURE8Eof8uEPKSJYjgN28Jhhf_pkjCNAn3TrohOl9d3q03Q7b_uJ5YKUWXaO3Ll-MUGQUijB9Vg8GGVX49PqjA0v0teEETy5RaS_2QheKE-qTI3ZwzTh65Bjx_uvoNvemSazxVqsqose7rLfgdx4pHDb584MnmatQaix4cUcYdY7xwn6QUj6UDrbqbx3r5Vl6RVarnzbJ6UMFJKS4L4wLJeRDXSRNfN80bmuEySj4MrfSWz5yBFGz8f97dpdVXL6wVqza_LTDYNolniPKKmphjYTYvkyH3wf2ny6Bmrj-6YRSbL5tB3j8z0Rfjp6QWfe0Y5SwU7nwqo1BjXDwyqgeCelbDZt9IqRqWxl3XFZpE7cn9ju3eDn8jdIGRikhk2mUstHHWzkflHpN19xXWB2JBFabesrhKaRVYwhEmWjBjoH-8gVGV4rS1dnkTq4md2cB9MVFXb69JYVDuQqeY-BRsNeNalvevIQ1oKLsRP3h8E-sn105RPuoEdhmb7bfYezkbPiKAr1yZ4JdnNh2gm_5k9FvHHbPh06EsrqmHbFlgwp7gwffMyQQtMvas8Y0pg9ihaLGWO9IL-GXUn_t9Dc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گزارش تصویری روز دوم حضور شاعران و نویسندگان ایرانی در اربعین به نیابت از رهبر شهید انقلاب
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/akhbarefori/675602" target="_blank">📅 23:32 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675601">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A_dK3AGezak8XH2Ter5t1bDUwHWDogF27xD38zAsK4uK2N2qKcvQbHbdbpC4UAPo3qWODjRcJBkOUZQkazw5afsNBfgk7ooHbbteCBUKq1tAZXRV-sJajvONgtmjc3VWtaIobiVoHUHBUghNzy2hitZp36heKWwkD1_SRKTBdAE5L0lAECTlmUgQC0w9mn9AnE7sqroDYB4jiWWr0W9Ps3qvDYP0pdZvQ794NSi0bb3KJ4sGwbjiAOsCvD1dLMwAVAycYxLUz7YpNNAWhltu2KKcsYbkppYzjoEL9SmXFk2QVb-P8-oy_ZpfQMI4QuBtvZQeX1bBprF-3qPCueTbgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سکوت مشکوک و مرموز نتانیاهو در بحبوحه جنگ با آمریکا/ اسرائیل ترسیده یا آماده «جنگ بزرگ» با ایران می شود؟
🔹
اگر اسرائیل وارد جنگ مستقیم با ایران شود، ایران نسبت به فعالیت های این رژیم بیش از پیش حساس می شود و اقدامات اطلاعاتی و جاسوسی موساد سخت‌ می گردد.
گزارش خبرفوری را اینجا بخوانید
👇
khabarfoori.com/fa/tiny/news-3233259</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/akhbarefori/675601" target="_blank">📅 23:28 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675600">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/19ecc9840c.mp4?token=jsHLKpWZo9BWvHh97adYQDDPTBvCpAUrkus9_TiGnDLs96dg4kGy9NNyIn6DTA9xhI2kES_SXbfCu1NVVKNm_Gz0SmS3kH7FxF71QUtIe-zcTaPcm86cf3Ywcpsn0hEVJC53FCUHO2YnWR-VvYA099V60l00Uwfo9pibuNVGRJnPPtq3taT5hfv9LD3kZGso4RNExCFzdRuKCgkGA31z3QV_eBFObfJCl9yjytBS0V7Jsa1XO7e7h1kWYEdtnbQWdkuNl19xr-cym1HSbJBw1ugnBtwBiaLXjyqH-xKfB21YrJ1HOKdycBs1ZdMeZ2A6xLIPGMuKZSS3LEk2bUI-Rg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/19ecc9840c.mp4?token=jsHLKpWZo9BWvHh97adYQDDPTBvCpAUrkus9_TiGnDLs96dg4kGy9NNyIn6DTA9xhI2kES_SXbfCu1NVVKNm_Gz0SmS3kH7FxF71QUtIe-zcTaPcm86cf3Ywcpsn0hEVJC53FCUHO2YnWR-VvYA099V60l00Uwfo9pibuNVGRJnPPtq3taT5hfv9LD3kZGso4RNExCFzdRuKCgkGA31z3QV_eBFObfJCl9yjytBS0V7Jsa1XO7e7h1kWYEdtnbQWdkuNl19xr-cym1HSbJBw1ugnBtwBiaLXjyqH-xKfB21YrJ1HOKdycBs1ZdMeZ2A6xLIPGMuKZSS3LEk2bUI-Rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هشدار رئیس سازمان بازرسی به بانک‌ها: اگر چنانچه به موقع نسبت به تعهدات خود عمل نکنند، قطعا با آن‌ها برخورد خواهد شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/akhbarefori/675600" target="_blank">📅 23:25 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675599">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🔹
داغ‌ترین خبرها را هر لحظه در وبسایت خبرفوری دنبال کنید
🔹
🔹
حدادعادل: انشالله آقا مجتبی سلامت هستند/ روایتی از شغل و درآمد ایشان پیش از رهبری
👇
khabarfoori.com/fa/tiny/news-3233395
🔹
تصاویر حضور چهره‌ها در مراسم تشییع پیکر اکبر عبدی
👇
khabarfoori.com/fa/tiny/news-3233343
🔹
سکوت مشکوک و مرموز نتانیاهو در بحبوحه جنگ با آمریکا/ اسرائیل ترسیده یا آماده «جنگ بزرگ» با ایران می شود؟
👇
khabarfoori.com/fa/tiny/news-3233259
🔹
عجیب اما واقعی/ فوتبال بازی کردن زن مشهور با شکم برآمده
👇
khabarfoori.com/fa/tiny/news-3233331
🔹
تراستی‌ کیست و چه‌ کسی مسئول فرار آنها با میلیاردها دلار پول بیت‌المال است؟
👇
khabarfoori.com/fa/tiny/news-3233211
🔹
برای اطلاع از تازه‌ترین خبرها، اپلیکیشن خبرفوری را نصب کنید
🔹
https://B2n.ir/jb2310</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/akhbarefori/675599" target="_blank">📅 23:23 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675598">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mhCQyj1-SkmSDfbR8BFm1xD04cKjJISueZTStOZDz_IXdI1wboHHfqWw9-_QoLE1h6CPM4NGDsYl0e1wegBfNGrR9D6X4Wrn5hVaI1kBspWNCLExZmzoXAQEA9Gyf7LIMcS-drpPs8tSRK2_vIx2R4k62fU7fKhwBnHR1IAe01_Akrq_uyXZ_sfaapptAkgJkl3F8KGds9BvImrN7_RB_kHjO7bRoEheNPUYZ3u0JXHHSQT66c9ULlKiBfMNW4kxYGRGHn5xGCulZKsIpH6sjinPlZIJy_zLBzpG_Nc2caSq_lCbKU-NXwpbHccNANFtejkq6KJLQcW5aXkXjNpqJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویر گستاخانه و عجیبی که شیطان زرد منتشر کرد: حمله به خارک
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/akhbarefori/675598" target="_blank">📅 23:18 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675597">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
ادعای تازه ترامپ متوهم: مهمات بسیاری داریم
وال استریت ژورنال:
شیطان زرد، رئیس متوهم دولت تروریستی آمریکا ادعا کرد:
🔹
آمریکا مهمات بسیار بیشتری از آنچه نیاز است در اختیار دارد.
🔹
این در حالی است که ارتش امریکا در جریان درگیری‌های اخیر با ایران، حدود یک سوم از کل ذخایر مهمات دقیق خود را که پیش از آغاز جنگ در اختیار داشته، مصرف کرده است.
#Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/akhbarefori/675597" target="_blank">📅 23:17 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675596">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I4bX1XDFgQpnfv9WT0CAM9AmLRvtNiMi_H0pmmrovVzqTXKxh29RNvxeO-CSk0l4SP0WlS8aQnHWkF53h37MIT4KoiYC6MGGYSt2iR25KnAJjFgKTYsNP62AhL4dJ_UiUuWdOyOIuIYzXiPHUcy1Lfw2D5_gVg6Z00KXeN4QYh6yX8qmufw3uhXZEAEiQJYYAJErNwz0UN4aeK02Ylc8Mk1NQpCtwpbsvNaWCE-5GarJLj5a4BgUVSvVtEwZYGwctDe1lJetHkGQXnQ48hZ27HefvKF1KKyL-i4UExNXdQmo7-yi0Jqp5l2WnC9lTNM-401SUklofkyg11uCU6V3yQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ریشه‌های شک از نگاه امیرالمؤمنین(ع)
🔹
امام علی(ع) شک را محصول چهار عامل می‌داند: مراء (بحث‌های بی‌حاصل و لجوجانه)، هول (هراس از مواجهه با حقیقت)، تردد (وسواس و دودلی در تصمیم‌گیری) و استسلام (تسلیم منفعلانه در برابر شبهات). این عوامل مانع از رسیدن به یقین…</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/akhbarefori/675596" target="_blank">📅 23:15 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675595">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/74090f25e4.mp4?token=sMeFIO_u79jGVuzYM3oE1kZK7omdHhrUdbRYyGqpU_YaJr9juLZTu1rilc-vWIsHx43Y1P1bGQ3flTIgdz2zqZTTSE8atm6j8sx1AM4wfgkvahEvfDr43qHMWuYW8dQjJ8xRFWnKKvbBAY_X2haE_M-WN4Og1ld3hSr4Ge0FUiR3y2wx-e5TllD8Lvmk6ABNlO-j0QyPoqOJjgCHG74sL9QuOmuVjVPJ8bbz9hGtccqtKn7L5FKTZxEFH2KqviVe21w0c1JrEvMIjbcm22ujEf0lnIewDnJDe8k3jd1QQn07IySoggvQCboBg8vHOVkR3pXFrS0i77IY0lhfxtfBDB_Mcw73dJhoZDHk8K7va3pTzLFybwLzgRenuY8rRKYtX5PIuPOqMzD98cLJgmcXcJMQe0Zst-4zWed4G2xqpBVq8olTN0L8BqdGc6t6wHhBsgpdaO9ICQn3kKaleDxb7BUOD7FmBNrVBt-ebaeIy70aJPHUnj5c1WEmJASa4Qp4jCGGK5oQ2jWu40X7NCxMF4zW3Xn4Z2VkpURUjYpJiWNwcwL0PaJ1gcErOwVxrbMyRSOg2WOmn_B_b7Hkh-eHrJHLMbCm7beICsvXpxPX4Nu9d-arymaqigedfnyRN9eYt2Yh9KpGV5-LS6UvDkKER5nDYR0l1AGbYDOQiAcHT_4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/74090f25e4.mp4?token=sMeFIO_u79jGVuzYM3oE1kZK7omdHhrUdbRYyGqpU_YaJr9juLZTu1rilc-vWIsHx43Y1P1bGQ3flTIgdz2zqZTTSE8atm6j8sx1AM4wfgkvahEvfDr43qHMWuYW8dQjJ8xRFWnKKvbBAY_X2haE_M-WN4Og1ld3hSr4Ge0FUiR3y2wx-e5TllD8Lvmk6ABNlO-j0QyPoqOJjgCHG74sL9QuOmuVjVPJ8bbz9hGtccqtKn7L5FKTZxEFH2KqviVe21w0c1JrEvMIjbcm22ujEf0lnIewDnJDe8k3jd1QQn07IySoggvQCboBg8vHOVkR3pXFrS0i77IY0lhfxtfBDB_Mcw73dJhoZDHk8K7va3pTzLFybwLzgRenuY8rRKYtX5PIuPOqMzD98cLJgmcXcJMQe0Zst-4zWed4G2xqpBVq8olTN0L8BqdGc6t6wHhBsgpdaO9ICQn3kKaleDxb7BUOD7FmBNrVBt-ebaeIy70aJPHUnj5c1WEmJASa4Qp4jCGGK5oQ2jWu40X7NCxMF4zW3Xn4Z2VkpURUjYpJiWNwcwL0PaJ1gcErOwVxrbMyRSOg2WOmn_B_b7Hkh-eHrJHLMbCm7beICsvXpxPX4Nu9d-arymaqigedfnyRN9eYt2Yh9KpGV5-LS6UvDkKER5nDYR0l1AGbYDOQiAcHT_4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رئیس سازمان بازرسی کل کشور: ما در شرایط تحریم اقتصادی هستیم و در این شرایط ورود ارز به کشور دچار اختلال می‌شود و عرضه و تقاضا و کنترل قیمت نیاز به مدیریت دارد
🔹
ریاست قوه قضاییه شخصا به موضوع افزایش قیمت ارز ورود کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/akhbarefori/675595" target="_blank">📅 23:13 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675594">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-text">🥀
السلام ای محور هنگامه اش
ای همه حرف وصیت نامه اش…
▫️
باز خوانی شعری که در وصف فراق حاج قاسم در محضر امام شهید امت خوانده شده بود اما اینبار متفاوت تر…
💔
@Heyate_gharar</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/akhbarefori/675594" target="_blank">📅 23:10 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675593">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">♦️
ادعای رسانه عبری درباره پرواز پهپاد شناسایی حزب‌الله در اطراف ارتفاعات علی‌الطاهر
🔹
رادیو ارتش اسرائیل ادعا کرد که نظامیان این رژیم امروز به سمت پهپاد حزب‌الله در اطراف ارتفاعات علی‌الطاهر شلیک کردند و این پهپاد دارای دوربین برای پایش منطقه بود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/akhbarefori/675593" target="_blank">📅 23:09 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675592">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f8eca1d072.mp4?token=CopXoWr7Ikz0DEyyIFWQ3mu7cG9LKSTGkIQrUfFFUwqFITgrDoukOxKgpr-GXcRAr3d8bMlhcOiHC3ZUEFsPiwUYiAM-K-6UtqOwtf2PU39KhLd3ExBwHmFlUVmCJtSR5nHNBfDd2BgU8-t1VlzgdEt6OFgfVscaoNSVwLm2T9xOxLxqb6f4FTUsvncf9JaUijNQ1IcZp8c5zHCVNgWzZV0miBQ9K82kE5fVCDLUA2lVF-6RI9NpiCf5C5nSDtffGHWj8g1TWu0Vr56vvm9ODeGPRQUFmEDxLZi6q_Ft1f4hKBKJ4GtE1AiBH_kMNV48Bx9NxXw_N-1cvEHD1f1JKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f8eca1d072.mp4?token=CopXoWr7Ikz0DEyyIFWQ3mu7cG9LKSTGkIQrUfFFUwqFITgrDoukOxKgpr-GXcRAr3d8bMlhcOiHC3ZUEFsPiwUYiAM-K-6UtqOwtf2PU39KhLd3ExBwHmFlUVmCJtSR5nHNBfDd2BgU8-t1VlzgdEt6OFgfVscaoNSVwLm2T9xOxLxqb6f4FTUsvncf9JaUijNQ1IcZp8c5zHCVNgWzZV0miBQ9K82kE5fVCDLUA2lVF-6RI9NpiCf5C5nSDtffGHWj8g1TWu0Vr56vvm9ODeGPRQUFmEDxLZi6q_Ft1f4hKBKJ4GtE1AiBH_kMNV48Bx9NxXw_N-1cvEHD1f1JKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مجری: آیا با توافق هسته‌ای عربستان سعودی راحت هستید؟
🔹
ما برای مقابله با سلاح هسته‌ای ایران را بمباران می‌کنیم، اما با عربستان هم‌پیمان می‌شویم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/akhbarefori/675592" target="_blank">📅 23:00 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675591">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">♦️
العربیه به نقل از یک منبع بلندپایه: رایزنی‌های چین در هماهنگی با پاکستان برای کاهش تنش میان آمریکا و ایران انجام شده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/675591" target="_blank">📅 22:57 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675590">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1cf60d3589.mp4?token=ZafnDG-6fGta6-kfam0532wKm11yqOPrK5AvRCx51MvK96QVvrodLMVEKLI1Coy3_HiRiWGGL1F1fPiHQsPgMJ6dJhvBJKsQ1Ff4pkVlmCbDzeXx7nyDYmoAM4oDZofQ9KWUBymKbxJbG6pyUYeWqPvZtdQPF80fx8-3K4SNbnCKBUxP0gAQ1lmQeQALwS0v-yp2eAM5UOFMhHfwvstbxpDDy8lLYCPk_amOBX1W6vKhBPnvKZsJzsRuUIScw9ZaPp3Bk4FOSyGFjGdQGFaReYjnXehdWZEv94N46OMhXwS2DGX3OdKKwG6XnewtcFQm1favQ6B7pybRU7TYIsEBvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1cf60d3589.mp4?token=ZafnDG-6fGta6-kfam0532wKm11yqOPrK5AvRCx51MvK96QVvrodLMVEKLI1Coy3_HiRiWGGL1F1fPiHQsPgMJ6dJhvBJKsQ1Ff4pkVlmCbDzeXx7nyDYmoAM4oDZofQ9KWUBymKbxJbG6pyUYeWqPvZtdQPF80fx8-3K4SNbnCKBUxP0gAQ1lmQeQALwS0v-yp2eAM5UOFMhHfwvstbxpDDy8lLYCPk_amOBX1W6vKhBPnvKZsJzsRuUIScw9ZaPp3Bk4FOSyGFjGdQGFaReYjnXehdWZEv94N46OMhXwS2DGX3OdKKwG6XnewtcFQm1favQ6B7pybRU7TYIsEBvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رئیس سازمان بازرسی: برخی تراستی‌ها خیانت کردند
🔹
یک تراستی ۲۰۰ میلیون دلار از سرمایه کشور را برنگرداند و از کشور هم خارج شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/akhbarefori/675590" target="_blank">📅 22:54 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675589">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/996d5978c6.mp4?token=Y31RhMOliYY3npm5LDkmSdu_9_YoZvQml9Pn5Z61ud5FoaeA9D_kCW-QxGLXZSxYA3eMZ3fQJ7w9w6Zb9JT00mPYSLkXviOhUdkiq6034o5EeliIXG399vvEU2leLBPXMoSRd9xaQwdBtBO8O7NWig93Ysnl_TiB92vz2ceFaeFFjwIXRQx1g5hPFr_9vo-XHOjmZW2t3GprBmMFn_DYDuPpwoTEq6Vfb8-S_B_w6YZ9yWXdJLH42k1_0xshzU0e2ixB3LAu4rfHMNJCL0Quly6l83jA_atQmx_hqjh52ces-h4R_TYXAJ4cRrfriMI3oWD0VoKbrkmkEW-65r8nUj-FOTeYIp0jHvJ0n154hQDgLInwu1tJ3XyRyFJdsEmKOLE68yLRS5d_n02V0XqSExCwU34jeUkXtBcglQmziKkr2NLZHgc5UoHEQ1aTT5C_h4iT4nPEIHVRXpX792n2nO65W4yAvGW-vAep6JZHT6mT3J6JtlAlGpV3wN3kzcawMywvTpcSu9dBK58b9fIunLYBxHmgn6pPwQcdBNpn2htMUKRprr3Qfb8QZA7DfSul6A3tPJUeB_32Hts2yuYZ1Lcr8SBijt-tCaA9e1NcsmRdWIiX6XztyxOkS4tLGU6UwxgYPei-LsxBp73uTSCguQat14SkDnea6bc3yyq0ZCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/996d5978c6.mp4?token=Y31RhMOliYY3npm5LDkmSdu_9_YoZvQml9Pn5Z61ud5FoaeA9D_kCW-QxGLXZSxYA3eMZ3fQJ7w9w6Zb9JT00mPYSLkXviOhUdkiq6034o5EeliIXG399vvEU2leLBPXMoSRd9xaQwdBtBO8O7NWig93Ysnl_TiB92vz2ceFaeFFjwIXRQx1g5hPFr_9vo-XHOjmZW2t3GprBmMFn_DYDuPpwoTEq6Vfb8-S_B_w6YZ9yWXdJLH42k1_0xshzU0e2ixB3LAu4rfHMNJCL0Quly6l83jA_atQmx_hqjh52ces-h4R_TYXAJ4cRrfriMI3oWD0VoKbrkmkEW-65r8nUj-FOTeYIp0jHvJ0n154hQDgLInwu1tJ3XyRyFJdsEmKOLE68yLRS5d_n02V0XqSExCwU34jeUkXtBcglQmziKkr2NLZHgc5UoHEQ1aTT5C_h4iT4nPEIHVRXpX792n2nO65W4yAvGW-vAep6JZHT6mT3J6JtlAlGpV3wN3kzcawMywvTpcSu9dBK58b9fIunLYBxHmgn6pPwQcdBNpn2htMUKRprr3Qfb8QZA7DfSul6A3tPJUeB_32Hts2yuYZ1Lcr8SBijt-tCaA9e1NcsmRdWIiX6XztyxOkS4tLGU6UwxgYPei-LsxBp73uTSCguQat14SkDnea6bc3yyq0ZCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کری‌خوانی جنجالی بین دو چهره قهرمان مردان آهنین
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/akhbarefori/675589" target="_blank">📅 22:54 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675588">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">♦️
پزشکیان با اشاره به برخی فضاسازی‌ها و روایت‌های نادرست درباره عملکرد دولت اشار
ه
کرد
🔹
مگر امکان دارد دولت بدون هماهنگی و اذن مقام معظم رهبری اقدامی در مسائل کلان کشور انجام دهد؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/akhbarefori/675588" target="_blank">📅 22:50 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675578">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاقدامات هیئت قرار</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mWNC17oDQiMLu-8DwS1124PmndjuaMRjBOTRrz-2_Cn5J3r-c8qmc8ynJBeVaognyx-O55tMgfg_O8huc8MZJkZu7BTskva4WBfIOqqOjFNE4TY_cYIMBcIskcfypKTB_1ixQP3-QcAUOjnL5ZvTkAWpeT8DH2WlbIz45JBTyGJYQXqawyd4ihobMeXKqwPvt8YJUa5jJgdaV-vuOdHBcP2rvKUvoWPDCxgZQMiSWtmBwzvzMpnxKTvJDokLKwMWCUI3grC5di0oLMHhxt2Si8foGUrLQJYQ5QbNoWxWtMwZma6HpKPeXGU8QN4rNeaO0P9-avhc6WeZBrWS7_HhBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cfh3-J2jtMowk2dISDjvstvQfpnULNp9KR2g23FNV14AJ-cD_q5JK6GC9HKSOuEmUQOMKprLvJNcZDs38dsm2ws9PQ54M_usIFQPPLQ5-ekvaxx225EWBHJz82Gq9fy1mb5uq5_k800N25hkXbg5XNBhOamJm16DVqoYYethQvfY0WCJe8c4nlqPuK-OJwZXlJ6eWlhtyeUxchOL66VosAL1aujCk47ratml4NgQf8qxQUiFkUkLjpbN3J28FxH_1SM89KcotfgTfkVZ0GDAT51beYbyFNiYfWGurLc9h4pds4gLjz9SXSW37YRvlX-F2iRgQQX0N0dr1kmezs7tMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eNaRPfyTv0X6S1b3UxTKJRINwRCjNN9_RrVamN_vGskCg3ETAQ-yDLkeTz83luLDqef3j5Ztsks43Uf0joQp8nTdqMo-oS6wZg1EzHon5LvzWtyzqruq654kNahnKR9_VxCesjX8xQq5rRcNit0bZtCKJi55k9M3liu00cQ6f_I9M0bx19rMii3Xgyq1vUzJzYDb1KYsQSIS4J9Foi3qr-_B1jTBk5htQuCLjLQFYf-8gFturZ8NttNYuLye9e32CxZiJJjm3jDBxIRTapHdDyiQ_15mJms-oATnvRBGF0O2UL50wonP52bYHxv6BenwGuBqUz3YyIx4CHP2Bhia8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IwFPuan3dgEnRindrH9XRMinUZtK1J6cxBNtk5NlIrvW0eJTV7wwWKYMa4NHOaXsAd6Dbq-En3qkCXMkKIY9Z-OTA67RNIdm6Pdj24ixRjvM-YXboEqffkdQjV_3q7tKjvruRFxcyC5TTBGonRY3HlCbzfMSJnwHg0FP-LZUzebgAEuwAhiFL17OpydFYU9AgvxaxlFOOwvtIABwSRBBOVjSwxum0IKCSWNx3jto4zwwFxaxZy4BK6qvrGp3_06EuwGx0B1Zz9vwkkzVghhlx3zBhWahvBh_BFqDEEDXjlJCIjP-bdcgm2qLc8mAjiCFGi5BwWuYCM00B0BCUxSbcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UMH7J03AEXPPtS_maOnRLC306eFjAWO4N8SFh3cmyhaMSYkTESYdBkSUgd_4qXOLI8RajF4ShVXYZikUIp-vPSqdOxxQqBLe6DKDfhJia7KY3uNVC_CP-MtmmQjPPXrTtlZAp6o274iZEXw58SzQvUYHAVtHWyuSNIfJBGRaBaNgh9S1KJ5dhfysJ118VgtYFAQOiFk5fGfC_s3D5ruFOtbgC32n816OfGAMDGFTZ3xnlz83XM6fCYar9TrKA5wU3AOzC7Qv_VKLkSNyTdNKwcT70u-_k5JOgkO5KzfUbxlHYar5R6-Hx0NZJdkrBCwvBj9pkb45pjpKqzGaJCR3VA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cs3rpZkGWheD8BPhkVb3hMEhVUBv-msQoTLNnqxHzYFDo8hOfgSthWtkPztbTuo6Jw1MZ0yY9dBizRRjnOGYUiRTqbUaQcCTAiCtfTrbx_vfFIbTix6GAzrE94yE5QngLw-z32nTZCDXIKb8rXjlTKKrJn3H-L4psVUNuvnVGHRp6w4YxC9wPRFDJNByfOL2zawrPl8HTCWaOAS0RhZofZdpvmcAvC_WwbPGjOBi3brf-bxJacyjOOrIXr0GfrT3FLNbfp8rovnmOWVfntXjSVn-iGKz_5FZygei3I8GOp9_9uZQpNXwDperKB7Da6HL8nHGt3lcCZ6Rc6j25YwSHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lVbu9nDxS8BsfADOGgjffhpKGXhS09Ng-Bd6EsoXO8DWsDpcQG1WqB_-H8pTMtr_CiokPwY2O2FNNetTCWhFs1AYntU9fZCUAPEQCrI12OW--hJBXPFFjcnTot4kV0ik9txMqU7_CekAGbJrmlUP3Gf1CbrI6R6Wnj2ezr1nHCL0EM547pahVtktStZyc3f-3nTuO5GwMbuzCKF3yh8IevbywVFEq93XI-GB7RJW_yVPULloMwv0_5xfWD98nY--RHQZ3cu5xF_1qjSQNp_ysEbIXLzN0O5JcJX9ruWHvkSClZuacBYRFBBnxA2wdxh1VOzXj1ClS1TJ3ZQIR77tag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XYky0k_3CYKEu989XW-VOd_EtggpJwfsCz3OUx4Mt_eF4HP1f6Zw2pWiR1UFAPT-k2scWrDalkqxfdZYu0t0qSq1DY9ce2cBOPNR9TXSEPjlVPvYHqOcdwiDku0FGsoPfA8j46IUjb-kaHvDy5ZBqNLaZeFMi0Nwj6kZi1Vgl6du4wz1ZJufS_W8ITHcd3LNAHES2jww4OXOmRacdhmQqLhI66UdCwipmRDYOnQukR057RLSpOUH0OUbbh1BVNSBynz21StgPJS84amOkeK6N5A59eFNGRwZuq1uqSBOi6FusKoArOqQ_DQ2mDjCpGfFENZmn0B8oBH_um5HlMaQbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nBEOEG9roZN5Fdfxj1xo4-kB6n75kB1fxLg1yjdDaVKuXXD0kcz7nlQmlPG6qI3B1fmEPpRWxVAZZH8M4V1GESholnFBs0jiKeCv24q2trwDmhjLcB0vuhfEQbNnF688lDvUGrXW_czZWBWCW8TKcCktKRKcuUfEkgUybjWGp31tYSp6ZzOPhm3B2QTHuL1gQHqX51JRxYwbVgiGb7ZaGqfRoosBE8GVtm3Ed493ddOKCePO_Bgu_2FxQ5T5ciSI_C3cYRv1OTRSae_FOxzu1YKcuqHwI1EWg59zbbqujFG36a8Iaoac-GM3a8NDwNUrzc2ZVexnkh9z70WKEDKTlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bfnAamTJg3mMBSY878mrLp_E_9qxmu4xwwOGhK5oY3PMFDRF5unPXhUKb-XQSyIXIB4tr3F1_ux17uTdUU8RD9ORrsy58as2S4u6LPROIDAKrffJOuaAmuY3XM1a_jqGiV-EuxT1tYU_RyH6kroYP1HOsiqARQ3htclDOptLsj-oyt6B9UnZ1y3auXs328E6jSjIbwUo26abLnCR8JwphLfRPKSuqK5VmDsz_CmdVtaiNwSLGs77Aivf9Ih045LBp1nl-_Uay4RiMHt49VStU_Be-qmi6m52Ud5blKuwS1OvuEQyWDFhbROlkacIh_6XFOKcBUCeycOUWsWQLZHJlg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">💫
روایت راهِ حسین(ع)
💫
✨
راه امام حسین علیه‌السلام، راهِ مهر، ایثار و دستگیری از مردم است.
🌱
این روزها
#هیات_قرار
با همراهی شما مردم عزیز، با توزیع گوشت قربانی، در مسیر حمایت از خانواده‌های حائز صلاحیت گام برمی‌دارد.
گزارش اقدامات هیئت قرار را در کانال زیر ببینید
👇🏻
@Heyate_gharar
شما نیز میتوانید در این کار خیر سهیم باشید
👇🏻
5029087002135690</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/akhbarefori/675578" target="_blank">📅 22:47 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675577">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m5vcS3yYoglAd6FuYvbhev5pdu1_LLO1Lp7LJ8MK9IaOAdzp4Y-455oBctWSrfJPfaxHGVC1FYoww6Qq6MNcogJC40h2Wmu29shcDL7iZ6W4aUnuAgGhWdEpgoglDCdFzgp7onFtETTMfBI7EKQK6kHA_6TbYFT8KEdeigFwZ2taPrVHrbINbMiDT_4mmbymOEO_adQX-UdM73ZpKJngxk9_eDUJIT08BnaAnLYpUDEFVeSbRIX0WYUGItzP_tBnalDPt5s3iiTt95ZllaAgX4T6Oi6YrRzrv3PvEe7cMBaabgQ1nTdk9hcGG4cxMAJJ6UNTuIuZ4YjRJQMAEXk9Vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نتانیاهو: ایرانی ها سلاح شیمیایی دارند تهدیدی برای جهان هست
#Demon
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/akhbarefori/675577" target="_blank">📅 22:43 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675576">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
الحدث به نقل از وزارت خارجه آمریکا: تبادل پیام‌ها بین واشنگتن و تهران همچنان ادامه دارد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/akhbarefori/675576" target="_blank">📅 22:38 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675575">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a7dfcd159a.mp4?token=EX8CAnJPgOPp8-CMl0iF75OlQlibuVVRB5ddDuMCYAydQjH7zXXhraWwSIWLbWpqsz6M6kQjzYesYb_fFOxN_3gu3ysbwSv2LqsQnWpkWcHonzMOhPjOQRDmGN1YQm_Nv2a1S0i2tIGvJd-puGTrgOa3uowwfKsCfiuode6csFwQoGNchyzNBb62mi8UWLE858XvEQmeLW6ojwi0eP6ZoHpbE6dLcIiTGh3wPZhBP7jII1pTkum790kFWcejfB29qPhB5S2sTLxz8q6Pq6kyYpapQHK7svS3AMt_dLupIqB1z8ycOB_aNTxF3iApg4Jn3K1X36hd_cfnluKS-QcUWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7dfcd159a.mp4?token=EX8CAnJPgOPp8-CMl0iF75OlQlibuVVRB5ddDuMCYAydQjH7zXXhraWwSIWLbWpqsz6M6kQjzYesYb_fFOxN_3gu3ysbwSv2LqsQnWpkWcHonzMOhPjOQRDmGN1YQm_Nv2a1S0i2tIGvJd-puGTrgOa3uowwfKsCfiuode6csFwQoGNchyzNBb62mi8UWLE858XvEQmeLW6ojwi0eP6ZoHpbE6dLcIiTGh3wPZhBP7jII1pTkum790kFWcejfB29qPhB5S2sTLxz8q6Pq6kyYpapQHK7svS3AMt_dLupIqB1z8ycOB_aNTxF3iApg4Jn3K1X36hd_cfnluKS-QcUWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قدرت ایران از خانه‌های ما آغاز می‌شود
🔹
هر قطره آبی که حفظ می‌شود، هر لقمه‌ای که هدر نمی‌رود و هر کیلووات برقی که بی‌دلیل مصرف نمی‌شود، سرمایه‌ای است که برای فردای این سرزمین باقی می‌ماند.
🤩
#همه_باهم_برای_ایران
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/akhbarefori/675575" target="_blank">📅 22:35 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675574">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5aad3726c0.mp4?token=Uk9WfhQlHN7aUaiCzaOfIogrDYM7-Q4hKdgZWAt-B3y0zcl6ylsWbJMjGcFRJnczMDy81JgDIUrBVLEvQSIa54MrbNefNN1rT-89qMCkQwUYK_9gkNgsjAw53kAO7wQzCzmhkKNE1bgzVwbmb4N-JycOz1Ic0y9ISqJ3cEOwxz92_W_LBPzGIX0FUi9HIUUvLarOdtydmRBiwj5fCIy7eLxIKr7VN-DuPrP6AxN1GhZqaefRI6SXMFlSsqA6dSk4d6zBwnVldM3lei9djnomc3Nc6bAqSWvfjDLgdCkhWdhptFp5SeqgWUb11-V2EVThbVYY5IeXMG-yT6YWUdjQwUSYkJpsprSG6hNhxOgsZRNjAx9BR7tkxSoqbL5g2kuR8tvpomLOgoS4aa7eRQWjOiDRvXde8af-Hge6_bSGv_HluuKqOuHNXkThW07p_6yPj72E58Faf1q2q4Wkq_9spTK-L1NjvDkI10lUO9T9kb6N1rAE66jkMgasfa2zK-H1RdBkei319QzRrWQ_4z5yiz3M1Kc3ranh_FYxzEgTnfGWZlcitBpEJo2YS2xFfJiObalUiv7Bx_eW0QsW8Kgu1NYIU9mGrsLiBAt2qmKcFpn-_VIuOAGq9tBEXIzH67Et03N2_rDF3i-xcc3ksNyhaFwJ3PfUMB-RBLoB7OV4WTM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5aad3726c0.mp4?token=Uk9WfhQlHN7aUaiCzaOfIogrDYM7-Q4hKdgZWAt-B3y0zcl6ylsWbJMjGcFRJnczMDy81JgDIUrBVLEvQSIa54MrbNefNN1rT-89qMCkQwUYK_9gkNgsjAw53kAO7wQzCzmhkKNE1bgzVwbmb4N-JycOz1Ic0y9ISqJ3cEOwxz92_W_LBPzGIX0FUi9HIUUvLarOdtydmRBiwj5fCIy7eLxIKr7VN-DuPrP6AxN1GhZqaefRI6SXMFlSsqA6dSk4d6zBwnVldM3lei9djnomc3Nc6bAqSWvfjDLgdCkhWdhptFp5SeqgWUb11-V2EVThbVYY5IeXMG-yT6YWUdjQwUSYkJpsprSG6hNhxOgsZRNjAx9BR7tkxSoqbL5g2kuR8tvpomLOgoS4aa7eRQWjOiDRvXde8af-Hge6_bSGv_HluuKqOuHNXkThW07p_6yPj72E58Faf1q2q4Wkq_9spTK-L1NjvDkI10lUO9T9kb6N1rAE66jkMgasfa2zK-H1RdBkei319QzRrWQ_4z5yiz3M1Kc3ranh_FYxzEgTnfGWZlcitBpEJo2YS2xFfJiObalUiv7Bx_eW0QsW8Kgu1NYIU9mGrsLiBAt2qmKcFpn-_VIuOAGq9tBEXIzH67Et03N2_rDF3i-xcc3ksNyhaFwJ3PfUMB-RBLoB7OV4WTM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فیلمی جدید از حمله ارتش یمن به منطقه جیزان عربستان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/akhbarefori/675574" target="_blank">📅 22:34 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675573">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fad6e203b4.mp4?token=fm3Xf5nk2EEFmmSTijJ9tWFDEA70v_AL0QrxIANJkXaWpHU4WXWlGX0veNVOz_JdkAURlWmE0G5ucE8EjH2M_Q6oEzIrYqLyXs1PDy9HxUun3FFRjEaO_NfLRLRgpnNDklV6laEWme8kgxgzY8d_rH8ms8konSfnQ8DjSECaoZMyYmC6t_rSL4zhg7iLtxi4qQf6eIu1F_WY-WLCvU9yVvLGqnaRlb8PSb7TzJoH3rwaMb4ObF14fkzg9zSNOaBfBPRrFngqL1JfDmBdFM7Q2-Qych71q4-wYEtAQIOpU5WJXXNyFM14v4IoIK6JsbC0E_8gL3KEh8U-d4wyrhmE6hxKzws5FbytmTSuUpIZmi7NG8fGxwCxLwerZ1EEG5NRhiOrUjxH8qwyFR7L2i3eL5JcT2l-HlTzNVE52zQiMXF1WvvDlgySGfRcmz7vd3LAWaRXXmZ1swthjfIb-qYe3jbvWR1G9mJ1HenTOID9xgNTXYkcRvo0oKplxsqcPXMtrlVeZFxXVv_7LWhvaoetR70tcFC3kdBfvhs6ZRpYlMSYz8tLp8Ew3fY5R4QZYb3zQ7Crxin_Jodv48dK2AX2LgTQpvaBGW-cx7DRVSRHxV28IHcM2FDjLUgO8xl_0U_bBS4H-91fWlqMfjihdyv8bQ1n3sIhk_7DFyKZFunQG9s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fad6e203b4.mp4?token=fm3Xf5nk2EEFmmSTijJ9tWFDEA70v_AL0QrxIANJkXaWpHU4WXWlGX0veNVOz_JdkAURlWmE0G5ucE8EjH2M_Q6oEzIrYqLyXs1PDy9HxUun3FFRjEaO_NfLRLRgpnNDklV6laEWme8kgxgzY8d_rH8ms8konSfnQ8DjSECaoZMyYmC6t_rSL4zhg7iLtxi4qQf6eIu1F_WY-WLCvU9yVvLGqnaRlb8PSb7TzJoH3rwaMb4ObF14fkzg9zSNOaBfBPRrFngqL1JfDmBdFM7Q2-Qych71q4-wYEtAQIOpU5WJXXNyFM14v4IoIK6JsbC0E_8gL3KEh8U-d4wyrhmE6hxKzws5FbytmTSuUpIZmi7NG8fGxwCxLwerZ1EEG5NRhiOrUjxH8qwyFR7L2i3eL5JcT2l-HlTzNVE52zQiMXF1WvvDlgySGfRcmz7vd3LAWaRXXmZ1swthjfIb-qYe3jbvWR1G9mJ1HenTOID9xgNTXYkcRvo0oKplxsqcPXMtrlVeZFxXVv_7LWhvaoetR70tcFC3kdBfvhs6ZRpYlMSYz8tLp8Ew3fY5R4QZYb3zQ7Crxin_Jodv48dK2AX2LgTQpvaBGW-cx7DRVSRHxV28IHcM2FDjLUgO8xl_0U_bBS4H-91fWlqMfjihdyv8bQ1n3sIhk_7DFyKZFunQG9s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رازهای پخت یک کباب تابه‌ای خوشمزه رو از زبان خودش بشنوید
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/akhbarefori/675573" target="_blank">📅 22:31 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675572">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">♦️
یمن ۳ نفتکش سعودی را هدف قرار داد
🔹
شبکه المیادین به نقل از یک منبع ویژه خبر داد که نیروهای مسلح یمن طی ۴۸ ساعت گذشته ۳ نفتکش سعودی را هدف قرار داده‌اند.
🔹
تعداد کشتی‌های عربستانی که از دوشنبه گذشته تا امروز یکشنبه برگشت داده شده‌اند و اجازه عبور پیدا نکرده‌اند،…</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/akhbarefori/675572" target="_blank">📅 22:24 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675571">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/942771bc59.mp4?token=QH-Wde4MKbWQcJ1HRsrOzrCZX5kE2r4XSdUM3uejYGcr2-jNjQGVqX6ch4ymWfmMEHDCpASxS1vS_pxPPqLiyv9kmCW2P8z9xpToDZ37X37k3Y0S_V2ZLANA4Gai14XEqA0RiM1GhXSH8tCOgpAOSF-bcVKFxt00AG0aLYCkew_YHFvxPDT5hHWEQiqTSNXVt9_xXPZIXC9tn6MN3nH2IP96ZZSkaBwf4IVP8WYiaBv9WmpCXPfVQELluMRiWLDoKVb4KSpR8VIKadKVMGaIiLnqun4voVqYIdwq7f6bTXCNY0zzc-hjsfG1cnU2r73VcOM5o6869JptzJaRBlNb8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/942771bc59.mp4?token=QH-Wde4MKbWQcJ1HRsrOzrCZX5kE2r4XSdUM3uejYGcr2-jNjQGVqX6ch4ymWfmMEHDCpASxS1vS_pxPPqLiyv9kmCW2P8z9xpToDZ37X37k3Y0S_V2ZLANA4Gai14XEqA0RiM1GhXSH8tCOgpAOSF-bcVKFxt00AG0aLYCkew_YHFvxPDT5hHWEQiqTSNXVt9_xXPZIXC9tn6MN3nH2IP96ZZSkaBwf4IVP8WYiaBv9WmpCXPfVQELluMRiWLDoKVb4KSpR8VIKadKVMGaIiLnqun4voVqYIdwq7f6bTXCNY0zzc-hjsfG1cnU2r73VcOM5o6869JptzJaRBlNb8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
معرفی فیلم: جنگل پرتقال
🔹
ژانر: درام، عاشقانه
🔹
خلاصه: جنگل پرتقال، درامی آرام، شاعرانه و تأثیرگذار است. این فیلم داستان معلمی را روایت می‌کند که برای دریافت مدرک دانشگاهی‌اش به شهر محل تحصیلش بازمی‌گردد؛ سفری که او را با عشق‌های ناتمام، خاطرات فراموش‌شده…</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/akhbarefori/675571" target="_blank">📅 22:20 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675570">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">♦️
بقائی به شبکه اتریشی: اولویت ایران دفاع برابر جنایات آمریکاست
اسماعیل بقائی، سخنگوی وزارلت خارجه ایران  در مصاحبه با شبکه تلویزیونی «اوآر‌اف» اتریش، در پاسخ به این سوال که کانال دیپلماتیک بین ایران و سایر طرف‌ها باز است یا خیر:
🔹
بله، آنها (آمریکایی‌ها) در حال تبادل پیام هستند، اما برای ایران، اولویت در شرایط کنونی دفاع از حاکمیت، تمامیت ارضی و حفاظت از مردم‌مان در برابر این جنایت‌های جنگی است که ایالات متحده مرتکب می‌شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/akhbarefori/675570" target="_blank">📅 22:10 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675569">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">♦️
سندرز: جنگ غیرقانونی علیه ایران خلاف قانون اساسی است
سناتور مستقل آمریکایی:
🔹
جنگ غیرقانونی علیه ایران خلاف قانون اساسی است و هرگز نباید آغاز می‌شد.
🔹
ما باید بنشینیم، مذاکره کنیم و این جنگ را در اسرع وقت پایان دهیم.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/akhbarefori/675569" target="_blank">📅 22:10 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675568">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">♦️
انفجار کنترل‌شده در جهرم
سپاه استان فارس:
🔹
انهدام تعدادی بمب عمل‌نکرده از فردا تا آخر هفته در ساعت ۷صبح تا ۱۲ ظهر انجام می‌شود.
#اخبار_فارس
در فضای مجازی
👇
@akhbarfars</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/akhbarefori/675568" target="_blank">📅 22:07 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675567">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iV2KCMsHl8pOpiOkSr4zYzVRUH0TU1YiB5k-ShzsFtzev5hgHARrW9JWRWA7MLK7bWgPS9Uu1Ml9VkkLtDkwgDmVlObaY97g7_LITYXjhuclSY6dTnJf5hWJUwxC_c1yrkHQGdaYuNH4UvGEzPqbIKTizX4bHDOBGIOvmnzqVknC1YelHhNmfCeQZuswAnHPixCTW2SyyRh8eRb44ilfsnICuGnlo-QrE5EEjyANbwglitv9AThJnKVAMw1sHv_iogR7mG3sgKLwLa9yOupj6K4NXjca-nembGz0pKG7_acNJ31pKHVvRBrTV9k7TFtW658VX6R643nSuXTzUIZ8vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تقابل شبکه‌های تجاری ایران با تحریم‌های آمریکا
🔹
به گزارش رویترز، واشنگتن در ادامه جنگ اقتصادی خود، شبکه‌ای از شرکت‌ها و کشتی‌های حمل‌ونقل کالایی را برای اختلال در صادرات نفت ایران هدف قرار داده تا زیرساخت‌های مالی صادرات نفت ایران را مختل کند؛ شبکه‌ای که آن را تهدیدی برای «امنیت ملی» خود می‌داند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/akhbarefori/675567" target="_blank">📅 21:58 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675566">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
یمن ۳ نفتکش سعودی را هدف قرار داد
🔹
شبکه المیادین به نقل از یک منبع ویژه خبر داد که نیروهای مسلح یمن طی ۴۸ ساعت گذشته ۳ نفتکش سعودی را هدف قرار داده‌اند.
🔹
تعداد کشتی‌های عربستانی که از دوشنبه گذشته تا امروز یکشنبه برگشت داده شده‌اند و اجازه عبور پیدا نکرده‌اند، به ۱۶ کشتی رسیده است.
🔹
این منبع همچنین خبر داد، از زمان آغاز محاصره یمن، تاکنون هیچ نفتکش سعودی از باب‌المندب عبور نکرده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/akhbarefori/675566" target="_blank">📅 21:54 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675565">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f55295d9c0.mp4?token=rZCMK50OCqz24EjaxBrlGUuU50CN9YiT1xpT9cZ1uz2g5X4M6PikdHvisCdFR0p6oYZHPfqZskyCeITPG-WgCmxv1i6S-ryGg_crJQMYdGm5O8v8SmIb-FJOmpc04DYSWvVJGC2S2zqw83KeuCUMY8TdsBOO_bLtHMmsDaCSNZR2cT6ztexzKlknHNW4CJW89qoKO6rsdZz8uzwLiWojb1NzR3N6xcOMIM-S7Ohkf1hY-Y4HIyACXplqaurRdIqmgqHPtWJAwMu2pHaHgD1BrWf5SoE6SNZKWcU1oTNzKcgKHqlTrZrtwmeF5Z7woBKhy0Ue-hj-DyXM4uogavoLNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f55295d9c0.mp4?token=rZCMK50OCqz24EjaxBrlGUuU50CN9YiT1xpT9cZ1uz2g5X4M6PikdHvisCdFR0p6oYZHPfqZskyCeITPG-WgCmxv1i6S-ryGg_crJQMYdGm5O8v8SmIb-FJOmpc04DYSWvVJGC2S2zqw83KeuCUMY8TdsBOO_bLtHMmsDaCSNZR2cT6ztexzKlknHNW4CJW89qoKO6rsdZz8uzwLiWojb1NzR3N6xcOMIM-S7Ohkf1hY-Y4HIyACXplqaurRdIqmgqHPtWJAwMu2pHaHgD1BrWf5SoE6SNZKWcU1oTNzKcgKHqlTrZrtwmeF5Z7woBKhy0Ue-hj-DyXM4uogavoLNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هذیان‌گویی مقام دولت ترامپ درباره عقب‌نشینی آمریکا در برابر ایران
🔹
«مایک والتز» نماینده آمریکا در سازمان ملل روز یکشنبه در مصاحبه‌ای اذعان کرد که پیشتر، حجم زیادی از انبار مهمات آمریکا به دلیل جنگ اوکراین و درگیری پیشین آمریکا با یمن خالی شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/akhbarefori/675565" target="_blank">📅 21:52 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675564">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">♦️
الجزیره انگلیسی: ایران می‌تواند با پهپاد یا موشک «کی‌یف» را هدف قرار دهد
🔹
تحلیلگران بر این باورند که واکنش ایران به حمله اخیر اوکراین به دریای خزر بر اساس ملاحظات سیاسی گرفته خواهد شد.
🔹
از لحاظ فنی نیز این امکان وجود دارد، چراکه فاصله کی‌یف تا تهران کمتر از ۲۰۰۰ کیلومتر (۱۲۴۰ مایل) است و این فاصله در برد موشک‌ها و پهپادهای ایران قرار دارد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/akhbarefori/675564" target="_blank">📅 21:50 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675563">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ldFHXiHYa3I36KPl5B6RdysDcDWrPz22Cmx0mVvZAlxwyNCynv1aXEwim7IiyVr6I4X9yWur-yVKiO76DyRUTmJkk7_EzrmxV_wehk0edtZUPyVFV2SGiODyruMez3UNkWcwZO6GoDReUpPDI7KrkBv-u_zrY6XOCwaeI-3hxr5iYKtnncuHUisqHiDwbwqNoQzJnIymFiMBfvWwbny-FrPXma3LfWvIEAdlupHAE_yq0RiBAggva1G9PwI5owe4LLtrfl3ahqHL9OJOAVtcE2XHobVt7-dwv6adVMdcIdpXah7Ys-MKKPIb1fzaMpFGVFM7-OUGlGScuLz6hnL_zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شرط اول
رهبر معظم انقلاب در پاسخ به نامه دبیرکل و رزمندگان حزب الله لبنان فرمودند:
🔹
جمهوری اسلامی ایران نیز در راستای خط مشی رهبر معظم و شهید انقلاب امام سید علی خامنه‌ای رضوان الله تعالی علیه دفاع از این مجاهدان مظلوم و مقتدر را سیاست راهبردی خود تعیین کرده و حفظ تمامیت ارضی لبنان و رفع کامل و بدون قید و شرط تجاوز رژیم صهیونیستی را به عنوان شرط اول تفاهم نامه ی پایان جنگ تحمیلی با امریکای متجاوز قرار داده است.
🔹
هشتصدوبیستمین شماره جلد یک خبرفوری
#تیتر_یک
@rozname_fori</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/akhbarefori/675563" target="_blank">📅 21:41 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675562">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cIjvCf4fkp6pEMFOS4IrKvv2HllkYfHQ1jq77SoeTC0_nuKsbSLols7_bfEuYokViPRUPZFcGNYRXXVZDnHx630ztiARp6GdA8Kt2sy6Y7jMMD3LmLy6xqcEq-KNv6iRNS1UgtqnWZDFq-B9BP0sK4W93FWoO78pUWGf2CgmS9zhDPaASIGIoT2Biv4LsAcKcyp-EQvoXHHsRy9dqXEYghfa_aueo9kqK_UE_SZ3tDX-O52iV8yIKz-INCJGq9srfaWy6FexZmYDQQoxczNIN1-ShbIPnsWE8ohihL-dtzlSJ3x4baJkcERXlohoGs1CPi8UosA3S0AuM_08x22H4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اگر دلت هوای زیارت اربعین کرده، این فرصت را از دست نده...
‼️
🔸
با پویش «زیارت به نیابت امام شهید» می‌توانی هم به نیابت از رهبر شهید انقلاب در پیاده‌روی اربعین سهیم باشی و هم شانس حضور در سفر کربلا را پیدا کنی.
🔸
به همت هیئت قرار، ۱۰۰۱ نفر به قید قرعه راهی کربلای معلی خواهند شد.
📲
برای پیوستن به پویش و شرکت در قرعه‌کشی، عدد ۲ را به سامانه ۳۰۰۰۱۱۵۲ پیامک کنید.
@Heyate_gharar</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/akhbarefori/675562" target="_blank">📅 21:38 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675561">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aed82fe27d.mp4?token=cA3EGKeC1AgQ74AXV_HIBUqqlu9xipuWQZhDA8UfcbLBg1mf1d4omixIXuJOutY_nIM5WKBI7m3AE9riaXNnaKEYPMzwfgEhiI6f9sMySUAvaQI_GtwFSnaLzqTimUH4XnYeUR3a8X8HBI7WyGSGp3-SuJ75q3x_Pmo3eBN9jX2PkfEPcCxdOg6HFmBSmHkSH67njOI7qnXts_rC-vuMgxCUG0UxXUfw0BOJtm9vw84oncKtTSJdgr5mFX9kYQocewY1uJergtHXXFYSqhtaf52qJCMOohUZamOqSZftpn7Vp78_7Echw4IoxMAEpM1WQDkPmg1t8dYMy3vDgRCMrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aed82fe27d.mp4?token=cA3EGKeC1AgQ74AXV_HIBUqqlu9xipuWQZhDA8UfcbLBg1mf1d4omixIXuJOutY_nIM5WKBI7m3AE9riaXNnaKEYPMzwfgEhiI6f9sMySUAvaQI_GtwFSnaLzqTimUH4XnYeUR3a8X8HBI7WyGSGp3-SuJ75q3x_Pmo3eBN9jX2PkfEPcCxdOg6HFmBSmHkSH67njOI7qnXts_rC-vuMgxCUG0UxXUfw0BOJtm9vw84oncKtTSJdgr5mFX9kYQocewY1uJergtHXXFYSqhtaf52qJCMOohUZamOqSZftpn7Vp78_7Echw4IoxMAEpM1WQDkPmg1t8dYMy3vDgRCMrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری از سرنگونی پهپاد «بیرقدار» متعلق به نیروهای سعودی در استان «الجوف» یمن
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/akhbarefori/675561" target="_blank">📅 21:25 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675560">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
قیمت برنج و حبوبات تا ۲۵ درصد کم شد
رضا کنگری، رئیس اتحادیه بنکداران مواد غذایی تهران در
#گفتگو
با خبرفوری:
🔹
با آغاز فصل برداشت، قیمت برنج ایرانی و حبوبات بین ۲۰ تا ۲۵ درصد کاهش یافته و امسال برخلاف سال‌های گذشته، کمبود یا افزایش قیمت در مورد این اقلام نداریم.
@Tv_Fori</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/akhbarefori/675560" target="_blank">📅 21:22 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675559">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">♦️
ادعای سی‌ان‌ان درباره مدیریت آینده تنگه هرمز
سی‌ان‌ان به نقل از منابع آگاه:
🔹
عمان پیشنهاد ایجاد یک ائتلاف منطقه‌ای برای ارائه خدمات در تنگه هرمز، مشابه آنچه در تنگه مالاکا انجام می‌شود، را مطرح کرده است.
🔹
پیشنهاد عمان شامل سازوکاری برای پرداخت داوطلبانه در ازای خدماتی است که در تنگه هرمز ارائه می‌شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/akhbarefori/675559" target="_blank">📅 21:22 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675558">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">♦️
احتمال رأی‌گیری کنگره برای مجوز جنگ با ایران
🔹
بیل کسیدی، سناتور جمهوری‌خواه که ماه گذشته رأی خود را برای محدود کردن اختیارات جنگی دونالد ترامپ پس گرفت، می‌گوید ممکن است به زودی زمان آن فرا رسد که کنگره درباره‌ی جنگ فرسایشی اظهارنظر کند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/akhbarefori/675558" target="_blank">📅 21:21 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675557">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">♦️
انفجار بمب جاده‌ای و انفجاری در مسیر ترانزیتی زاهدان ـ خاش
🔹
گروهک ضدانقلاب به تخریب زیرساخت‌ها روی آورد
🔹
عصر امروز در محور زاهدان ـ خاش یکی از گروهک‌های ضدانقلاب با کار گذاشتن بمب جاده‌ای و انفجار آن به تاسی از آمریکا و رژیم صهیونیستی در زدن زیر ساخت‌های شهری، باعث گردید تا بخش اعظمی از آسفالت جاده تخریب، و این محور مواصلاتی مسدود شود.
🔹
در حال حاضر با حضور عوامل اداره راهداری، پلیس راه با یک طرفه کردن مسیر، تردد با کندی در حال انجام است.
#اخبار_سیستان_و_بلوچستان
در فضای مجازی
👇
@Akhbar_sob</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/akhbarefori/675557" target="_blank">📅 21:18 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675556">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nkX0-LS5qnRpqPAbahiyL8fnInYZ-dj3WwZsNZTUxyugwpDuqJ5FoCHXbwgE9RAf_Uo09pUkzViNDfPZtedVYRHkVmZ9lQpd_2KrSUj35wap91lpp30pEOjvS1e-c9PRDnlMq7ZlxBci_IjNSCn6q8ttK6wSSg6r420q9nMVkd75UTr8-Vn5fNfZE9Y34NxCvYXuVj3fAR_bD2mUmGNC7lcA3fhOg7i_cnx_q4emM7oP5WPDaUM78894wlkxNZVCV89lmir8QHL34XxshYzYTWyVMpiDBwTzxVTa8L95f2C6bIhS-3E6tZTI2wfHPrsjTUQAMFUS_0cJ81p7Dt3wEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رواق دارالذکر به روی زائران امام رضا(ع) آغوش گشود
🔹
رواق مبارکه دارالذکر، مدفن مطهر رهبر شهید انقلاب اسلامی به روی عاشقان و زائران حضرت امام رضا علیه‌السلام آغوش گشود.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/akhbarefori/675556" target="_blank">📅 21:16 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675551">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qwRQpd70ProOG-rtYGRQwaQBcnetdgMgfKimzMmOBZhaUEFh8YWk-RO066417OGOZio0iemnP1Xh192e8U3KxD93yOoXfiMLgZrYefBNGKwbCyUCuDR4oK4RhWYAW_fxvAfpyeaEb_05QOPPSFRJa2aSPqu_2nVaE9l6I72M6kDpnmCV0QU_IvTuJLftzkiMFUWNSeIHrPerFamn5UhQFb6qImoTbXkNEGf4xRWAOvgxAMLvzDQWUCUC9hkiNSJ1r97W6Dc-8x8T_-wrv828lC42Mt1oGE3j1QTov3RxxUfOOv-R_G1gBQ8wkkSn2uoo6-mbD46gMZucICU7Bdy_eA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ej8LlqP1eiHMgFK2kiPkZFRL-zoccR0C54Vqe_WN0Zko-8iWLh14okclzpxR8va5bXoxcoeZWjeoNGVrbvMopWwAD-JmPuXe3phZgVU0JR0ahlWetluh8ebRpDlsMElML4X1o38-XpXvCOn6O86-DrLgs0vtyk-OjjxELT0WskUFNmoU0N741vo92Bwb1Zgj73hGfL1EBe-gXdhX07HCN5shx8uXMq2MUXqEMeNRzV8ISKosZf23zwb7UxmUGw__O5PoKJuRr6INcwQ3EAgdvlf6iksYftpSyJCa0lBxDRiMn8sMi0Ub8eN07VQh2QgEA7QSgbpuGLODFz581ALGzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O3nVY4yl9mVlCAlK3ELgLeX3KJ5mIBCxDsU9OL6sHimsS3mcvYG6TusaGt0KiVrseAwcg4jfwMi_yba66bGpgXVK1zs8K2W88E3l4QUA_WUkab-US4snqyyECXg9lF93X3DvVDKtxdrsGC-J_ZcPaKdlMEgjYDPfmUzTYGQxT4-Okqww9F5Q8C3tFmMnrXJwTSe7dNO4pAvv8xekapctjqzTAXsn0pWtwm4EDyfIU3Ckp2jCVwUGbYVD5Pr9h7hLjHWwFkzi4ApQZv9Gi2ndU_0WBfvPAjGPacgvG_sQWNyXblZ4di4Qb4egxICigp0mvrucSeouURqbYnWMaL8oYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C1_kmwtmo31x3_9_VppjJMr_G8_J98MdP4uxf7zpUYNi6a1obrq3JXAMYD_XgrgHjdNdAYERfAj420SIBqwG2CvxVYhVGwRXDH3RZSx7Jde6MU5wgf9bmlSIhkpo0Y0OdWouvE_hS3khi5gTQHOPuR1GJ_g04yDDMcKcJKTcEXgca4Rp6TTMkjvuaRetqJN5RYQDg2yTOOIXuPK6hJ-NarkcQOyS1Jr8xGs8F5wG_Le9br1n4EIR0BiRPkKAJkFRUwmEmgnzNuJzIrQA0Dpu0OtPlJaljN7-b4XF0TiEq6hrIWAUvblQoBX19d0u-aEt2Co98RO9jSL_pnI0hwaD-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YN_cR6hEleuNDl4qcONqXkl4RUlFoYLuLJ3-MEhiKDbZN39FPF-BoUpgVlQmaPxaO-hEYklX4sVKf0SdUbwSbOM5oGcYlSOeyK4OwU6dhiBEtU0_jFXHanE8bhTmHcZ0fxTA4FHWJl1jWG_B4yihmxpJwxWsECCmExr1RPPDwtAmbnyTNoJWG1FizqrhQ7k44XoUTePeXaoNqRkFEjsiQfSaSaDrORmL4NZDmZIvuvalWi3RJR7CB4f86dIGyBRxuR4xAGPT_qYv8CVTfLa7-PtVqoz4oJQWdGZy7LW42xKJNaSJ-bjjCKmPBXprMfpU2Jh-bHmTvAk72P9R9Uc6nA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
تصاویری از سرنگونی پهپاد «بیرقدار» متعلق به نیروهای سعودی در استان «الجوف» یمن
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/akhbarefori/675551" target="_blank">📅 21:11 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675548">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t4oGxAxcYggueMBR5zcH4E5EPm31B0cuC-Fdw36Xytlv0WG_O4VhXaVrvOYbdQXIyK3mQqqi2jGKdfzML_uo9t-zg2d961eMVEPiJ843Ur5Y6wZxJh0acOZojIoPbKYXsSKh1Lv7PqEUK1wrOtYUGxpbMDwdmehzlwXSD6p5lqanGp-uAUb7cjtzioKwx0c_nfCcSOfdCgIBTq93GQQjYbZMH5Z_0pL8HZ3OpNbeUxdJMuFKctFyBhywqtnq_AZFCXjcaJulWDFuukTaaaHoiQ4Ciy3yuN8M2MupX4B0SMKSStHWS4BeMMlPMWfk4cC0NYT7f2oeV1L3gSJ9P3aUDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gnkvYYqM-65WPhzpZyPv5tZy641aoLfE6tlHRoKKkQDNBHOOVbecCZ5ydaKXTDOZcLjXA0gAdcnXLUOvPpVxDqTmRCvDxnKsA5gZ4ngU7ZR3YJyLaesqZFeOvE5qwFx6vLbuc2D-3o_WNccfoTSKlMXKW-agaz_jiS0ffBL1XBZqHobAJsV4VrJAScKPQtf1voRZQW3pDiPNU2EfFsi1aqsCQJ0_ABSJhM0zFDdGVshg6KjKWaD2kbyXcNDO-BVsGOiPrM_Pp9O7cnyFr25CR5mRpNZK-iA0hUFCSrvMbYOYNVnhFdsNt9Qb3GiQFbAxg6quSOEbhj2b_Y2VtkSLQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HQfqsDKkNoDtErHvJh3wAUyaM4HVnv0J2aaL6fAYdoVC6oYnMAk2Vv4yt-sGWVnaoVjJC2bZZM783W5immpVs4rzTeumZDa6neus8DHNdTRDqbkTX4aNlmQcV72pIPJ7jHxvWS9rwsuGGBx0YrWxVIxVbcZ0u_68xUNLv2ZIjm-ZDBPC8M3Rh6eH-IKaaSWj_7Z-sfaW-YUHsEjwpkcMAr6uRcYy92CwT__0fNtaMKKaHtGu0FDDnb8FA2gQHzwnjOoQ2E9B2qEYWvPeY7EW2sKUQWfvx4rMEEb3bltZpO69FJE5UEFrmur40m70uzqy2e62UmMYWeIpZ6B8oOD1tg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
۸۳ درصد جوانان آمریکایی خواهان اتمام فوری جنگ با ایران
🔹
سی‌بی‌اس‌نیوز در یک نظرسنجی نظرات عموم مردم آمریکا دربارۀ جنگ با ایران را بررسی کرده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/akhbarefori/675548" target="_blank">📅 21:08 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675547">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">♦️
بیانیه سپاه پاسداران انقلاب اسلامی به مناسبت پنجم مردادماه، سی و هشتمین سالگرد عملیات غرورآفرین مرصاد
روابط عمومی کل سپاه پاسداران انقلاب اسلامی:
🔹
حافظه تاریخی ملت ایران نشان می‌دهد یکی از شکوهمندترین جلوه‌های اقتدار و بصیرت ملت سرافراز ایران در عرصه‌ رویارویی با جریان نفاق و مقابله با گروهک منفور و تروریستی منافقین تجلی پیدا کرده و حماسه مرصاد را رقم زد.
🔹
عملیات غرورآفرین مرصاد که در پی خیانت و لشکر کشی منافقین کوردل در پنجم مردادماه سال ۱۳۶۷ با پشتیبانی استکبار جهانی به کشور انجام گرفت، با تار و مار کردن منافقین فریب خورده، درس بزرگی به خائنین به ملت و میهن اسلامی داد که تا همیشه تاریخ طعم تلخ شکست در برابر اراده ملت را مزمزه کرده و هوس هر گونه تجاوز را از سر بیرون کنند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/akhbarefori/675547" target="_blank">📅 20:50 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675546">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c48a0e4ce7.mp4?token=CgkLwgR7HJMzzbCAopNuGkkRgi8WPEJU54v0N27Q7tC8253-tydIZvIMANrwh4OuNzMwbpDyaS9s0qw7CHyJMerb8iDfGotznzQCRakWGQcBy_Z0dp6-UCPK9c7X2Vhgo4WSSGg8aa6cccUbWWVbcfsxGBUa6n7L7ifNSLX64_CqwoVlWvR2lciSFkNEu07MlnH0mNdkG86Uu5N9bDmgp5Ci-WBnr-LLVrbWYdMkbYUrSAWteAXmTZ_PBe1x3643vgYjXG9dS09JMri9IW8_mh9u5bVKCh4p3KVmTmjA8utSrm7xs2bOpKhLDbyHiM_hLGy4lNWS3CHBYtYcM_Xd4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c48a0e4ce7.mp4?token=CgkLwgR7HJMzzbCAopNuGkkRgi8WPEJU54v0N27Q7tC8253-tydIZvIMANrwh4OuNzMwbpDyaS9s0qw7CHyJMerb8iDfGotznzQCRakWGQcBy_Z0dp6-UCPK9c7X2Vhgo4WSSGg8aa6cccUbWWVbcfsxGBUa6n7L7ifNSLX64_CqwoVlWvR2lciSFkNEu07MlnH0mNdkG86Uu5N9bDmgp5Ci-WBnr-LLVrbWYdMkbYUrSAWteAXmTZ_PBe1x3643vgYjXG9dS09JMri9IW8_mh9u5bVKCh4p3KVmTmjA8utSrm7xs2bOpKhLDbyHiM_hLGy4lNWS3CHBYtYcM_Xd4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رواق دارالذکر به روی زائران امام رضا(ع) آغوش گشود
🔹
رواق مبارکه دارالذکر، مدفن مطهر رهبر شهید انقلاب اسلامی به روی عاشقان و زائران حضرت امام رضا علیه‌السلام آغوش گشود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/akhbarefori/675546" target="_blank">📅 20:48 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675544">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">♦️
آکسیوس مدعی شد: رئیس ستاد مشترک ارتش، ژنرال «دن کین» به صورت محرمانه به وزیر دفاع «پیت هگست» و ترامپ هشدار داده که کمبود موشک‌های پدافند هوایی می‌تواند توانایی حفاظت از نیروهای آمریکایی و متحدانشان در منطقه را مختل کند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/akhbarefori/675544" target="_blank">📅 20:44 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675543">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">♦️
فرمانده سنتکام مدعی شد جزئیات حمله بعدی آمریکا را بیان میکند  آکسیوس مدعی شد:
🔹
فرمانده سنتکام گفت گام بعدی احتمالی ارتش آمریکا، از سرگیری عملیات نظامی گسترده برای نابودی ۲۰ درصد از اهدافی است که نیروهای آمریکایی در جریان عملیات «خشم حماسی» تعیین کرده بودند…</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/akhbarefori/675543" target="_blank">📅 20:43 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675541">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">♦️
فرمانده سنتکام مدعی شد جزئیات حمله بعدی آمریکا را بیان میکند
آکسیوس مدعی شد:
🔹
فرمانده سنتکام گفت گام بعدی احتمالی ارتش آمریکا، از سرگیری عملیات نظامی گسترده برای نابودی ۲۰ درصد از اهدافی است که نیروهای آمریکایی در جریان عملیات «خشم حماسی» تعیین کرده بودند اما مورد حمله قرار نداده بودند.
🔹
کوپر گفته در صورت عدم تصمیم به بازگشت به عملیات نظامی گسترده، ادامهٔ کارزار بمباران دو هفتهٔ اخیر بی‌فایده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/akhbarefori/675541" target="_blank">📅 20:38 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675540">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hpMWyy2u5i8o032Ms2NuLRbcb9zbyovBNjEa9gki5cA6oAXac_Cj-5Nr7dQxMFMs4BQksPc0VNk9QHzBs3lWZUbAPwKU0IXrU4YBBv4gNzpoO0oJi4DeS-UlD_D7HC8HJlvkZdiJhT-TDcLS8DHEh-Wk2iTFmLVBPPt4BfGjSRGBGDRigLOKwpCV9EF5Wi42yijVZvbBZl-uhXNMLv_w98K0L06gHk5YJ_eFE8SP3pWzyUEfo4nS8HTHEywDRypDMyYuPrPEbALw_t1Uh_94wEqfSrTUeZSvAScMGOhpo494UPxG86JtZzE79o1-7RPzxVzm5L7LDszRWNGIp0rjHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
جهاد و مقاومت رزمندگان حزب‌الله، عزّت و سربلندی لبنان را در جهان اسلام رقم زد
🔹
سلام خدا بر روح ملکوتی سیّدالشّهدای حزب‌الله سیّدحسن نصرالله و همه‌ی فرماندهان سَلَف مقاومت و یاران شهیدش رضوان‌الله تعالی‌علیهم‌اجمعین که نهال مقاومت اسلامی را به درختی تنومند مبدّل کردند که اصلُها ثابت و فرعُها فی‌السّماء، رزمندگانی که با جهاد و مقاومت خود، عزّت و سربلندی لبنان را در جهان اسلام به ارمغان آورده‌اند.
🔹
بخشی از پاسخ رهبر انقلاب اسلامی به نامه بیعت دبیرکل و رزمندگان حزب‌الله لبنان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/akhbarefori/675540" target="_blank">📅 20:36 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675539">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">♦️
جهاد شهدا، مقاومت اسلامی را به درختی تنومند تبدیل کرده و عزت لبنان را رقم زده‌ است
🔹
صلوات و رحمت خدای متعال بر شهدا و مجروحین و خانواده‌های صبور آنان، مهاجران فی‌سبیل‌الله که تحمّل مصائب را بر خود هموار کردند. سلام خدا بر روح ملکوتی سیّدالشّهدای حزب‌الله سیّدحسن نصرالله و همه‌ی فرماندهان سَلَف مقاومت و یاران شهیدش رضوان‌الله تعالی‌علیهم‌اجمعین که نهال مقاومت اسلامی را به درختی تنومند مبدّل کردند که اصلُها ثابت و فرعُها فی‌السّماء، رزمندگانی که با جهاد و مقاومت خود، عزّت و سربلندی لبنان را در جهان اسلام به ارمغان آورده‌اند.
🔹
امیدوارم به برکت دعای خیر سرورمان عجّل‌الله‌تعالی‌فرجه‌الشّریف انواع عنایات و الطاف الهیّه شامل حال همه‌ی مجاهدان و شهدا و جانبازان مقاومت و مهاجران و خانواده‌های صبور آنان باشد.
«وَنُرِيدُ أَنْ نَمُنَّ عَلَى الَّذِينَ اسْتُضْعِفُوا فِي الْأَرْضِ وَنَجْعَلَهُمْ أَئِمَّةً وَنَجْعَلَهُمُ الْوَارِثِينَ»
🔹
بخشی از پاسخ رهبر انقلاب اسلامی به نامه بیعت دبیرکل و رزمندگان حزب‌الله لبنان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/akhbarefori/675539" target="_blank">📅 20:35 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675538">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">♦️
جمهوری اسلامی دفاع از مجاهدان لبنان را به عنوان سیاست راهبردی خود تعیین کرده است
🔹
اکنون که حزب‌الله لبنان به‌عنوان پیش‌گام گروه‌های جهادی در برابر هجوم سَبُعانه‌ی رژیم صهیونیستی و حامیانش، چون صخره‌ای ستبر ایستاده است، این پایداری پیامی الهام‌بخش برای ملّت‌های آزاده‌ی جهان در جهت رهایی از ظلم و ستم استکبار جهانی و دست‌‌نشاندگانش شده است. بی‌تردید بخش قابل توجهی از این دستاورد بزرگ مرهون صبوری، نجابت، فداکاری و همراهی مردم لبنان خصوصاً منطقه‌ی جنوب بوده ‌است.
🔹
جمهوری اسلامی ایران نیز در راستای خطّ‌مشی رهبر معظّم و شهید انقلاب امام سیّدعلی خامنه‌ای رضوان‌الله‌تعالی‌‌علیه دفاع از این مجاهدان مظلوم و مقتدر را سیاست راهبردی خود تعیین کرده، و حفظ تمامیّت ارضی لبنان و رفع کامل و بدون قید و شرط تجاوز رژیم صهیونیستی را به‌عنوان شرط اوّل تفاهم‌نامه‌ی پایان جنگ تحمیلی با امریکای متجاوز قرار داده است.
🔹
بخشی از پاسخ رهبر انقلاب اسلامی به نامه بیعت دبیرکل و رزمندگان حزب‌الله لبنان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/akhbarefori/675538" target="_blank">📅 20:33 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675536">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">♦️
پاسخ رهبر معظم انقلاب به نامه دبیرکل و رزمندگان حزب‌الله: پایداری در راه مقاومت، نصرت الهی را در پی دارد
🔹
نامه‌ی شما برادران و فرزندانم، رزمندگان مؤمن و شجاع حزب‌الله سرافراز که حامل پیام پایداری و استقامت برای اعتلای کلمة‌‌الله و باورمندی به وعده‌های قرآن عظیم و آرمان‌های عزّت‌آفرین امام خمینی و قائد شهید آیت‌الله‌العظمی خامنه‌ای رضوان‌الله‌تعالی‌علیهما بود، موجب تقدیر و تکریم است.
🔹
امروز که ملّت‌های جهان از ظلم و بیداد دولت امریکا و صهیونیست‌های جنایتکار و نابودکننده‌ی حرث و نسل به ستوه آمده‌اند، راهی جز جهاد و مقاومت، پیشِ ‌رو نمانده است و پایداری در این راه، نصرت موعود الهی را نصیب مجاهدانِ راه حق خواهد کرد «...وَكَانَ حَقًّا عَلَيْنَا نَصْرُ الْمُؤْمِنِينَ»
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/akhbarefori/675536" target="_blank">📅 20:31 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675535">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">♦️
رژیم اسرائیل با ورود شورای صلح ترامپ به غزه موافقت کرد
🔹
کابینه امنیتی و سیاسی رژیم صهیونیستی با ورود شورای موسوم به «شورای صلح ترامپ برای غزه»، به این منطقه موافقت کرده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/akhbarefori/675535" target="_blank">📅 20:29 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675534">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">♦️
سعید آجورلو عضو تیم رسانه ای مذاکره کننده ایران: انتقام فقط یک تصمیم سیاسی نیست؛ برآمده از خواست مردم و روح جمعی یک ملت است/ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/akhbarefori/675534" target="_blank">📅 20:26 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675533">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">♦️
محمد حسین پویانفر: ما مداحان نباید در مصادیق ورود کنیم. چون به هرحال همه ما سلیقه‌ خودمان را داریم و اگر بخواهیم از تریبون مداحی سلایق خودمان را بگوییم اتفاقات خوبی نمی‌افتد. ما باید از نظام و انقلاب اسلامی دفاع کنیم و جانمان را هم در این راه بدهیم
/ خبرفوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/akhbarefori/675533" target="_blank">📅 20:25 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675532">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6b424b8bc.mp4?token=BDwvEiHScWHtf_DAISaah7zhGPShiCNsWvnAF4ni-Egyva8vkIRWNzlPtfHLW0NLVLEqBRB2q9vQLgyYdyeI4ynbs57yKryddOPespd4hoIMAN5nOBScSymW-r5IMsLfTrJRh6HsEyFV0FAf8vNPP6lXglPdGzhP-RpLra47ApOn4bQ4q6y6IeFaKhk2nPo6uvJOfUZ9JCbzTDEp4IPCWvFcjAptzEvfHGQG6sQuXODvytbjo64dFCjo6DIhK-uN3wSFCGKhJw5TOrCiFu-8REm6xcxdTJah8DqqRgBLcn2NZHAqAi89sLD-UVAIV1Gn1JI5pPoSbPqc4R6pBHCniaj1lcrG_g_HS7JXXVeqD2V4slJo0gLuHEslf1jdRmlIwVwL2v1Dl7E5Bm2LED18XsDMlCDnVAMg-b2EKSLJkPaXZvZ9m5TIwYrhBDffpzqwhFlCH84_irtOMQMC5W74-hcAH25iO7gVMI2PIWM_rLl2j2Dlaa5McVTMIS640m8DpOH7_p_vl2z1JFV2HFZGyEkMSgXkSDkAa_4rSNst9a2F2YX_9HG0UiKdJUon2O-g-3bc2vD_SiH4_6GWTWwywNMoJmvHt8nLz2eN3A0CcYuXxS0ASsZe8McAADwAfDs9eKRq_39d9bP-D-GlywNDZH2GXjpja1DLcPmWiLl2fUo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6b424b8bc.mp4?token=BDwvEiHScWHtf_DAISaah7zhGPShiCNsWvnAF4ni-Egyva8vkIRWNzlPtfHLW0NLVLEqBRB2q9vQLgyYdyeI4ynbs57yKryddOPespd4hoIMAN5nOBScSymW-r5IMsLfTrJRh6HsEyFV0FAf8vNPP6lXglPdGzhP-RpLra47ApOn4bQ4q6y6IeFaKhk2nPo6uvJOfUZ9JCbzTDEp4IPCWvFcjAptzEvfHGQG6sQuXODvytbjo64dFCjo6DIhK-uN3wSFCGKhJw5TOrCiFu-8REm6xcxdTJah8DqqRgBLcn2NZHAqAi89sLD-UVAIV1Gn1JI5pPoSbPqc4R6pBHCniaj1lcrG_g_HS7JXXVeqD2V4slJo0gLuHEslf1jdRmlIwVwL2v1Dl7E5Bm2LED18XsDMlCDnVAMg-b2EKSLJkPaXZvZ9m5TIwYrhBDffpzqwhFlCH84_irtOMQMC5W74-hcAH25iO7gVMI2PIWM_rLl2j2Dlaa5McVTMIS640m8DpOH7_p_vl2z1JFV2HFZGyEkMSgXkSDkAa_4rSNst9a2F2YX_9HG0UiKdJUon2O-g-3bc2vD_SiH4_6GWTWwywNMoJmvHt8nLz2eN3A0CcYuXxS0ASsZe8McAADwAfDs9eKRq_39d9bP-D-GlywNDZH2GXjpja1DLcPmWiLl2fUo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آیت الله جوادی آملی: هیچ فکر می‌کردیم روزی برسد که دو ابر قدرت دنیا رو مچاله کنیم آیا این معجزه نیست اگر معجزه نیست پس چیست؟
🔹
یک روز آیت الله بروجردی حتی نمی‌توانست یک مجلس دعا علیه اسرائیل و به نفع مردم مصر برگزار کند؛
🔹
از کجا به کجا رسیدیم!
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/akhbarefori/675532" target="_blank">📅 20:25 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675530">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">♦️
اشتباه را پذیرفتیم؛ مسئولیت را هم
🔹
در روزهای گذشته، خبر محدود شدن فعالیت «خبرفوری» در برخی پلتفرم‌های داخلی، بازتاب گسترده‌ای در فضای رسانه‌ای کشور داشت.
🔹
فارغ از هر قضاوتی، یک واقعیت را نمی‌توان نادیده گرفت؛ امروز، میدان رسانه، خط مقدم نبرد روایت‌هاست. میدانی که هر لحظه میلیون‌ها خبر، تحلیل و روایت در آن منتشر می‌شود و تصمیم‌گیری در آن، گاه در کسری از ثانیه رقم می‌خورد.
🔹
در چنین عرصه‌ای، همانند هر میدان نبرد دیگری، احتمال بروز خطای انسانی هرگز صفر نیست.
🔹
همان‌گونه که هیچ فرمانده‌ای در سخت‌ترین میدان‌های نبرد از احتمال خطا مصون نیست، در میدان پرتلاطم رسانه نیز وقوع خطای انسانی، هرچند تلخ و ناخواسته، امری اجتناب‌ناپذیر است.
🔹
چندی پیش نیز به دلیل یک اشتباه انسانی، مطلبی کذب برخلاف سیاست‌های رسانه‌ای و مصالح کشور به اشتباه در کانال‌های «خبرفوری» منتشر شد؛ موضوعی که نه با رویکرد همیشگی این رسانه همخوانی داشت و نه با سابقه آن در حمایت از خطوط قرمز امنیت ملی کشور.
🔹
خبرفوری ضمن تاکید بر استقلال دستگاه قضا و ضرورت اجتناب از هرگونه حاشیه‌سازی، اعلام می‌کند که خوشبختانه نهادهای نظارتی با اشراف کامل نسبت به فضای رسانه و بدون هرگونه تاثیرپذیری از انواع واکنش‌های بیرونی، همراهی ستودنی با مجموعه خبرفوری نشان دادند که خود الگویی برای مواجهه با اشتباهات ناخواسته رسانه‌ای است.
🔹
خبرفوری طی سال‌های گذشته، با میلیون‌ها مخاطب، یکی از مؤثرترین رسانه‌های فارسی‌زبان در مقابله با جنگ روایت‌ها و جریان‌های ضدایرانی بوده است. رسانه‌ای که همواره تلاش کرده در کنار منافع ملی بایستد و سهم خود را در دفاع از امنیت روانی جامعه ایفا کند.
🔹
این مجموعه رسانه‌ای، ضمن پذیرش مسئولیت این خطای انسانی، خود را متعهد می‌داند با همراهی با نهادهای دلسوز کشور، همچنان در قامت یک رسانه مسئول و سربازی وفادار برای ایران، به مسیر خدمت و اطلاع‌رسانی صادقانه ادامه دهد و خطای رخ داده را در همین مسیر جبران کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/akhbarefori/675530" target="_blank">📅 20:22 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675528">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bLkymNliNn1nGh89fG8lT1aneEMJFE2CHemX9ZRuUsGfdT9fJHPMMZbvVQGsvgOZnyW80tmpELMYyCNiol38xJDoQ2tTZbL_CDi1XF-qOyPgNkpNZtJ1bEmftk5CRfXu4Kmf_BOLH2VYAxIY8Ga8Q-zdzVSNmY2zLAY34RakjTghPeyTV_rI7I1I-M0XbOHl457pVpXPA3DVzYRfbA13zZTjb2SR9HR2kRrVLcWrnMGvuuzFvAJ53ibb3bN1d_Ca08C4MKpyL2N5IsAuj8Ng5RpNjcdi7T-6LQHIQa3auPQ1ExafP08yc9ciyJrGnQWMZ9ZlDvXyE6E1iKqSb-JJwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پایان بلاتکلیفی صرافی‌های رمزارزی؛ نسخه جدید برای رگولاتوری رمزارزها در راه است
🔹
عباس آشتیانی، رئیس کمیسیون بلاک‌چین و رمزارز نصر کشور، از تدوین متنی در کارگروه ویژه اقتصاد دیجیتال خبر داده که با هدف تنظیم‌گری میان‌بخشی و تقسیم وظایف میان دستگاه‌ها بر اساس ماهیت انواع دارایی‌های دیجیتال تهیه شده است.
🔹
رضا باقری‌اصل، رئیس کارگروه ویژه اقتصاد دیجیتال نیز می‌گوید: قانون، دارایی‌های دیجیتال را به رسمیت شناخته و کاربردهایی مانند توثیق، ضمانت و پذیره‌نویسی را برای آنها پیش‌بینی کرده است. به گفته او آیین‌نامه در حال تدوین، با استناد به همین حکم قانونی و سایر قوانین موجود، مسئولیت هر دستگاه را در حوزه‌های مختلف مشخص می‌کند.
🔹
با این مصوبه می‌توان انتظار داشت اختلاف‌های میان بانک مرکزی، وزارت اقتصاد و سایر دستگاه‌ها بر سر تنظیم‌گری دارایی‌های دیجیتال برطرف شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/akhbarefori/675528" target="_blank">📅 20:16 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675525">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاخبار رهبر شهید انقلاب🇮🇷</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pg1GiILbp8MXoRJPkAi_hKm8j8qCqkhfu5sXhctPiuSGqc2K40kDV-JdPbehWCmOfV0cQO5YkplvNj-4tf8TBtuB68N9_MG5dU-Wm18BJ91U9jEcJ5CgKxlEgLarAxObsKmb-i41iB-_DL8ygqYt2KcboD_TbcDJ1-CrUMpXbCs1_dcdm8IBGzHoUGwuXW7IfcdtLUH2Z1tsnTv-Ea4x8Z-WFFgfbII1hnpeXSs4eaVhf--j8xVlWY7biT2Xv_dzsPUV-fAFm2aYmdKWkjKtOcT8P6kotrF4aNK6KOOdDqEC-pmqDQ037gUVXIrgIiyWs3hVDtE4lWAJCcOV9BGrng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📣
توصیه‌ حضرت آیت‌الله العظمی خامنه‌ای رضوان‌الله‌علیه به قرائت قرآن و دعا برای پیروزی جبهه مقاومت
🔹️
رهبر شهید انقلاب اسلامی در پاسخ به سوالی، قرائت
سوره فتح
،
دعای ۱۴ صحیفه سجادیه
و
دعای توسل
را برای پیروزی جبهه مقاومت توصیه کرده بودند.
💻
Farsi.khamenei.ir</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/akhbarefori/675525" target="_blank">📅 20:08 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675523">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J7JizUPPZ0o246jhB6kGnagvQjF3XJumQhamm7areZi5toe6cOxB_ZNFQlRQiyu5xkCAImng29rgUrAxvG1VNMuGai6HrYT6ceFIWlgTVG9XRWZ1JijFTSHytTyQSTx0R1j8iOnVEUbqQakJqYFvY1W6aLk-HVXvu_6Tv7Fzj0jJn7qEfzNhVXfrMVb4pjyOvsVjjpQgZchcLvZJgNt-s1oXnIm71vcQVVJbTRaRNcwk8spwmo6k9-r52cr3VLocSARkbmk_yQIsUgEwYRgtK94M-NyTUIG3uMbEHhGeoEHemudKz0994H6pV9xpPf7y5KAWT1oXypx685xR9s4kYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رونمایی از یک دستخط رهبر شهید در دفاع مقدس
🔹
آیین رونمایی از دستخط تاریخی رهبر شهید حضرت آیت‌الله العظمی سیدعلی حسینی خامنه‌ای برگزار شد.
🔹
این دست خط در جریان بازدید تاریخی رهبر شهید از بیمارستان صحرایی حضرت علی‌بن‌ابیطالب (ع) و عیادت از مجروحان جنگ تحمیلی در تاریخ ۴ مرداد ۱۳۶۷ به یادگار نگاشته شده است و برای اولین بار رونمایی شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/akhbarefori/675523" target="_blank">📅 20:06 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675519">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p3sOEsYWD1Z6qhlbak2L_gIoSxne7R0XVYv14ZfEFNqWJNuYs-H-Nyh7ssXbZVZwvYHEJ4W9Bb8oQG5P5NYJKQ3cWUVnLaPyG2atzLD49EBq1uHmrLqQD4uvmozs-euvHhSmP4FTh2MY_Juc6tKKb9ee5b16o2Di6gON76mwhXtHiOTXZZYA2FeJ8Nbo2Ktfi9sOzArWIZWwkXKnjnBi0QMiVYMviCadzFVljNct0t7FHHFQ-45PnXFBXJ0ZDXW58w54D3MvPkxTvVxWc0joX1URN1oRXv6ta7ZcyxpktkTC17wY8WyUOMPygTKEco5R_jjx_dZCqrsT6OXL8u313Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مشکل تسویه بدهی کالابرگ‌ها حل شد
🔹
محسن فتحی عضو کمیسیون اجتماعی مجلس خبر داد: تا پایان هفته جاری تمامی مطالبات و معوقات فروشگاه‌ها (تا قبل ۲۰ تیرماه) تسویه می‌شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/akhbarefori/675519" target="_blank">📅 20:01 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675518">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aea43d43f7.mp4?token=f48SgpTqAnTTyj-PJJdv9ZTyYQmRNeM3ERtinlGsko7IQf8OUBipjMYW_1s0CpM97D4dgR2yFsj17ihofYpohIhO9MS3Q5P1KfqE9zk356WKI9JQv88ISTEsGw1JfAsx-FS5vA0YVr-tJMXY7OzH3loM_t3YHP-PUHujB92-yxEUm6PwV712XJxdfcOjplVs9vg30yzfutjGajx25TfG6bKjZvXE6yGlorzTqZHJKAw_l8eOKAM9odnA3gOodDDMqxwpq1nfw6lXZ-lAP3lRokObKv0QKvNB1TcAaLdY19syg55cirhMaTDG48MAW1uIzZg4n33r_Org7_pUQWzPuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aea43d43f7.mp4?token=f48SgpTqAnTTyj-PJJdv9ZTyYQmRNeM3ERtinlGsko7IQf8OUBipjMYW_1s0CpM97D4dgR2yFsj17ihofYpohIhO9MS3Q5P1KfqE9zk356WKI9JQv88ISTEsGw1JfAsx-FS5vA0YVr-tJMXY7OzH3loM_t3YHP-PUHujB92-yxEUm6PwV712XJxdfcOjplVs9vg30yzfutjGajx25TfG6bKjZvXE6yGlorzTqZHJKAw_l8eOKAM9odnA3gOodDDMqxwpq1nfw6lXZ-lAP3lRokObKv0QKvNB1TcAaLdY19syg55cirhMaTDG48MAW1uIzZg4n33r_Org7_pUQWzPuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حضور سردار رادان در مرزبانی مرز خسروی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/akhbarefori/675518" target="_blank">📅 19:52 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675514">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">♦️
شاکی پرونده پژمان جمشیدی فاش کرد  «ادعای اخاذی ما کذب محض است!»
🔹
شاکی پرونده پژمان جمشیدی بعد از پایان جلسه دادگاه در شعبه نهم دادگاه کیفری یک با لحنی قاطع و شفاف توضیح داد: تمام ادعاهایی که درباره قصد اخاذی من و مادرم از پژمان جمشیدی مطرح شده، کذب محض…</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/akhbarefori/675514" target="_blank">📅 19:32 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675513">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h69nXO4xAJPC7JsXBBZmUDlTIVEeuF0hW_Lm7ZXVCBIFv0oCGlgsbkrxQbAAeysYhEmEpMDK9MMgMzIs_5veuQ2mTybfUxjZXX86xrVoINdHuYmNJw-kHvprpwuUbYSaon5sbWzyzt3bG0Fvl9ZBSpz7iuFwM2D4VAtrpmG-mqAb1rPlKa3062HfoZOpaAR84YeksAx45339r0bPMRqE0JLVJIGUoNqGwF_ueAWyOhXGAKJllDlQlIJIvhXvlPsj_kmdSgpX0ENoA0aLviZzAqQLuHcQQrEvkpVDp6sEB6vV2WopaI-0Xvolqc4ahaIWNDntlsk-v5AijKvLT4bBGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
عراقچی: اقدام «فرصت‌طلب مستقر در کی‌یف» نمی‌تواند بی‌پاسخ بماند
وزیر امور خارجه:
🔹
زلنسکی به یک کشتی تجاری ایرانی حمله کرده و یک ملوان را کشته است. این اقدامی است که به‌وضوح منشور سازمان ملل را نقض می‌کند و به تحریک اسرائیل انجام شده تا اروپا را به جنگ آن بکشاند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/akhbarefori/675513" target="_blank">📅 19:22 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675511">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">♦️
چین جنگ‌های آینده را با پهپادهای بیونیک و هوش مصنوعی تصور می‌کند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/akhbarefori/675511" target="_blank">📅 19:17 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675510">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XDQBQ8HToyUNxk0nTpKWyn80SKcqUys_G9IeYdNMXoqR2s6KEe_kro13OkkTXnqW82wK7MFwtqkuWS1C3y6dwIeAHqNaUkxAFkwKAujEcUGXVcVXy2VwovCTA6DmUfzuFNsJsoVBiEqaXsr8z6Z4rFjoDLU9qjiDyadS0eoOAH5_zJIG2HgGrJKPjbPPU4_sQL-ZZm4-gDGx7QNLgXm2lpfHWltlS5FoAZgVHiR5gafV9_qE6fT6R-gyYRQLaAePwVyJtl5Wte_9J2SnsY7p0NdxNaJHSZf8BYr7pIFThmU8IxJLSRdgN-vLAleUQ3JHxPr9TsY6N_ruNkDCNXg8DA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فخری؛ زنی که در پشت آینه‌های تاریخ گم شد
🔹
در دل شیراز قاجاری، دختری به نام فخری زندگی می‌کرد؛ دختری شیفته‌ی بازتاب‌ها و نور، فرزندِ استاد بزرگ آینه‌کاری شیراز. او هنر را از پدر آموخته بود، اما دیوارهای ضخیم سنت و روزگار قاجار، هرگز به یک زن اجازه نمی‌داد…</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/akhbarefori/675510" target="_blank">📅 19:03 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675508">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YChLmJ4OrJkjCFNJ2Uk0QUPsMWmGeckqQisuplmR38Ao9YQyYFFQo907GB94XqsDLyGLp4oExu02cX34rlbFleIF2V6wGPjcfQ7dHrc7mkn1nsARAT7eDaBhtqkYv0bnf7da4FlM-8aU-TfNB_couJZdsCJwZUvgdZmSnXqojWKMMqKcGfd5ovTv4dUZ9VdotqBqVuw66_4Kdr9KWH-ru0IZ24MKeFnWmFPxeFw1bXl7dYtAz3_1c3_jzl3vypi44d1U_BoYBoKJLmmlkyMCL4Y9kgQGroyFDbCudo8TCP0p2GAjaSH9jfjINY_g1xHywjQq6gQSHf7AKtU5X3qWHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
پنل تخصصی نمای ساختمان
.
✅
اجرای سریع
.
✅
مقاوم در برابر آتش، رطوبت و تغییرات اقلیمی
.
✅
مناسب برای مناطق مرطوب
.
جهت آشنایی بیشتر با مصالح و استعلام قیمت، بر روی لینک زیر کلیک نمایید:
👇
👇
👇
👇
👇
👇
👇
👇
👇
👇
👇
https://hbboardiran.com/landing/</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/akhbarefori/675508" target="_blank">📅 19:00 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675507">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">♦️
اینتِرپل علیه سران گروه‌های جدایی‌طلب ایرانی اعلان قرمز صادر کرد
یک وب‌سایت عراقی:
🔹
اینترپل با پذیرش درخواست‌های قضایی ایران، علیه ده‌ها نفر از سران و اعضای گروه‌های جدایی‌طلب مخالف ایران «اعلان قرمز» و حکم استرداد صادر کرده است./ ایسنا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/akhbarefori/675507" target="_blank">📅 18:53 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675505">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/106915264d.mp4?token=I9HBE4AbxZtzxgFBUJYesz1V6FZU9gmryGq0VdbHwsz7Hsgu2Pgj8d4xdWa2jNZEHwn1V4xAvglNTK8oQIRGe50oKkX8IEm4h-PZhnGwucWF6My18kY_tVdwEo0OR-9pqtT_iyPogES2lFgoGvZwx7Vf8ocsWXGnx3ql6s28N3hRfHtLckyydjLniRE6-JkKClYSmK0SG53qS6Ul9Xdt0JNIY2Uteqa8Ws2B3nRMwdoSHeJAYQxBYdEIJycm7CODP3p3b7cIvZTXjDvjKL2HEfLs48MxevzvsoOCCtNZWu2jguNs8MQkYV9NyEZBeEXMFfyPbbgdS7p35O4cODB_2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/106915264d.mp4?token=I9HBE4AbxZtzxgFBUJYesz1V6FZU9gmryGq0VdbHwsz7Hsgu2Pgj8d4xdWa2jNZEHwn1V4xAvglNTK8oQIRGe50oKkX8IEm4h-PZhnGwucWF6My18kY_tVdwEo0OR-9pqtT_iyPogES2lFgoGvZwx7Vf8ocsWXGnx3ql6s28N3hRfHtLckyydjLniRE6-JkKClYSmK0SG53qS6Ul9Xdt0JNIY2Uteqa8Ws2B3nRMwdoSHeJAYQxBYdEIJycm7CODP3p3b7cIvZTXjDvjKL2HEfLs48MxevzvsoOCCtNZWu2jguNs8MQkYV9NyEZBeEXMFfyPbbgdS7p35O4cODB_2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
راب مالی، نماینده سابق ویژه ایران ایالات متحده: با توجه به حملاتی که علیه ایران انجام شده، توافق‌هایی که نقض شده و وعده‌هایی که هرگز عملی نشده‌اند، اینکه ایرانی‌ها به دنبال ساخت بمب اتم بروند، از نظر آنها رفتاری منطقی و عقلانی به نظر می‌رسد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/akhbarefori/675505" target="_blank">📅 18:40 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675504">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">♦️
خوک هار به کانادا: جلوی دود را بگیرید وگرنه تحریمتان می‌کنیم
🔹
رئیس‌جمهور آمریکا با متهم کردن کانادا به «مسموم کردن» هوای آمریکا بر اثر دود ناشی از آتش‌‌سوزی‌‌های جنگلی، بار دیگر اتاوا را به اعمال تعرفه‌‌های سنگین و دریافت خسارت تهدید کرد. #Devil
🇮🇷
✊
…</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/akhbarefori/675504" target="_blank">📅 18:37 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675501">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ffmrwNs4TRjub6RCmjOfQkCFtRgRhOnqZTFD1LHtUl8-ihkvLolIv9iAq2PX_H-MbHrdU6fy1iz3r5acf51cRDSWO5VxsLgJObvXlJM4Wl2OrCn_E0PPw_ZS44hwEj_1phPkXfboQfKChoI_yfzLsxDoHCWRPdym1vjX2lV1Q2XWDNd44rIolk8HF9oFTU5fE7JbaOm_36_Ye2ZPXeDvAJHiTzSAT800vXWsRRklVGNBmZPiqn3NrpYTG_HmX9NSqDanGLg94d5wgrMrBAwatZyw-b5Wi6jiZYD2ztTMbKcQEVmt689dA2P1ZpnHXbIok3muKqO8b7EdX3W3-_EuPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وزارت جنگ آمریکا آمار تلفات را اعلام کرد
وزارت جنگ آمریکا:
🔹
از ۷ ژوئیه ۲۰۲۶ تاکنون ۴ نظامی آمریکایی در عملیات خارجی کشته و ۲۰۷ نفر دیگر زخمی شده‌اند./ خبرفوری
🔹
رقم اعلامی بیش از دو برابر آمار قبلیِ اعلام‌شده از سوی سخنگوی پنتاگون است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/akhbarefori/675501" target="_blank">📅 18:29 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675499">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YhLxMhg975gBWPvPaIUoIJg1691Ti6V6Fy1LWgDjo26FwZkhzfEgGxe4nYNwrWWOHramzWp2F-js_FTiBMU0lP5vDG2dn5QD2oM-8TWSDKS0IRoihz52FA_HhoRM6JHz2We15VzVEqehCb8Yj_RbwGfWNMAvGSBxGCxTKa24LnOlSELfqV7j6l499hFEKSP69xSldIOPvNzgNRQc_4B6sUGBfAHxwXwcNc6B01SQWOiStrqYnTnL7aFVf4jm8v1cw-1B7zSTh5h2Iynv-HpcS_cNnMqmDzkU61GJip6gtYhBgMY6Ni4kUfVqXmZedvKjrBgI-Tdbyccy7c-tBuXJQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مردی که زنگ مدرسه را برای همیشه در ایران به صدا درآورد
🔹
میرزا حسن رشدیه، پدر آموزش نوین ایران، مردی بود که در روزگاری پر از مخالفت و تعصب، نخستین مدرسه به سبک جدید را بنیان گذاشت. او با ابداع شیوه‌ای ساده برای آموزش خواندن و نوشتن، راه سوادآموزی هزاران…</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/akhbarefori/675499" target="_blank">📅 18:06 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675498">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f7f1fdad6.mp4?token=FVkM584rpuuCeiD9KMgvmUtPMabNUN9rjAyygAc7AbcS2nPG2PyuU1JErw8C1hAYxCWnmmhsKZNCnmP_tAgtg-0U8fJ2aTuxu_VFnqAJYMI5rJ5lcnuMz93mzsXvw1s5aK8712pP8kRFkwLN0RJHx9i0Lpsz2_h_s-FTtIrQ5NCnk-v4Njyqd2GMRWc-bH-44UtsOcUBPHfm1pdaY83CztWFAreB4lrEnUMpIoFxdOovfCeYIO4H5FxXEICGkIGsoCgSbaLNRlvZkVWw4Rl2yasYo5hDYH9mefNP8VI9ptvgU4J_Ve57Coy0OnUqzAJOAu2O_nIxMRNUABDlvgXqmzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f7f1fdad6.mp4?token=FVkM584rpuuCeiD9KMgvmUtPMabNUN9rjAyygAc7AbcS2nPG2PyuU1JErw8C1hAYxCWnmmhsKZNCnmP_tAgtg-0U8fJ2aTuxu_VFnqAJYMI5rJ5lcnuMz93mzsXvw1s5aK8712pP8kRFkwLN0RJHx9i0Lpsz2_h_s-FTtIrQ5NCnk-v4Njyqd2GMRWc-bH-44UtsOcUBPHfm1pdaY83CztWFAreB4lrEnUMpIoFxdOovfCeYIO4H5FxXEICGkIGsoCgSbaLNRlvZkVWw4Rl2yasYo5hDYH9mefNP8VI9ptvgU4J_Ve57Coy0OnUqzAJOAu2O_nIxMRNUABDlvgXqmzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اگر قصد دارین تو خونه کباب کوبیده درست کنید، حتما به این چند نکته کلیدی توجه کنید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/akhbarefori/675498" target="_blank">📅 18:05 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675497">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">♦️
زیاده گویی نتانیاهو کودک‌کش: برنامه هسته‌ای ایران باید چه از راه توافق و چه بدون توافق متوقف شود؛ این جنگ با سقوط نظام ایران پایان می‌یابد یا با تضعیف آن تا جایی که لزوم توقف برنامه هسته‌ای را بپذیرد
#Demon
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/akhbarefori/675497" target="_blank">📅 18:03 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675492">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/153e794733.mp4?token=htsF0AoA8yPLe_2mY_OUOZAPkKzs3ULPrpjnCBM4grwsvkwPEEmuBHX8SQe0PvyxJGLIygXt4cOQjNW5zillkpgdHggRi0fQjYHmB6zFSWlSNaJNjYz6CyU2nc4AvZnYoz6Ps2mQts56EIwH8MzRIn8-KOdxgvNdMy0LP38lRNC6vxLynDz5KxVf6uZ3etFmFZpcMlHYCv7CDtP02i74Nk52Qlpgnqgu-df-AndwFkrjxr06xpy5gF4-CewIBVcVdXv_jEdcNZZTvkqI5qwupJmPLU82iT9vut9YvRFFRNuFhwGRU5pzQ0M__-ImUqARxz9jV9mXkF96Vt-UJacC_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/153e794733.mp4?token=htsF0AoA8yPLe_2mY_OUOZAPkKzs3ULPrpjnCBM4grwsvkwPEEmuBHX8SQe0PvyxJGLIygXt4cOQjNW5zillkpgdHggRi0fQjYHmB6zFSWlSNaJNjYz6CyU2nc4AvZnYoz6Ps2mQts56EIwH8MzRIn8-KOdxgvNdMy0LP38lRNC6vxLynDz5KxVf6uZ3etFmFZpcMlHYCv7CDtP02i74Nk52Qlpgnqgu-df-AndwFkrjxr06xpy5gF4-CewIBVcVdXv_jEdcNZZTvkqI5qwupJmPLU82iT9vut9YvRFFRNuFhwGRU5pzQ0M__-ImUqARxz9jV9mXkF96Vt-UJacC_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نون پنیر سبزی با شکلی خاص
😍
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/akhbarefori/675492" target="_blank">📅 17:35 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675491">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a84e97bfb4.mp4?token=Nv0dfZELgW3Lw1ScaXnJ67Q6mnPNPPkAbGFb0qfXTnEP18rQFcAAe1gI5jBabM8HHlhXCbZy68MEx2kAaq8BZDg4HMvHLTnt3l5UQy2BvnV6iAaLKKfzVwTd-0dWRfiMvzt38WAJ9eHwfDyy0XsJV3zKh73uDG8Q9_ItxMvLp6PGf7wEdcCRBFYfOQIoG1e2r0LHJ-5Fi7OvvL6Mu1RA6_3o0Cu8Ktpz_PRGOmwcrNW4m75xMBT9BtcFVZtDOqPABqeAjW22dElVI4gKR7KJtRvTYwL8quHhEpX8HVyZaADvsSZug5I94w0GghCwu1msS80vZEf1qL5izpXPZoZgag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a84e97bfb4.mp4?token=Nv0dfZELgW3Lw1ScaXnJ67Q6mnPNPPkAbGFb0qfXTnEP18rQFcAAe1gI5jBabM8HHlhXCbZy68MEx2kAaq8BZDg4HMvHLTnt3l5UQy2BvnV6iAaLKKfzVwTd-0dWRfiMvzt38WAJ9eHwfDyy0XsJV3zKh73uDG8Q9_ItxMvLp6PGf7wEdcCRBFYfOQIoG1e2r0LHJ-5Fi7OvvL6Mu1RA6_3o0Cu8Ktpz_PRGOmwcrNW4m75xMBT9BtcFVZtDOqPABqeAjW22dElVI4gKR7KJtRvTYwL8quHhEpX8HVyZaADvsSZug5I94w0GghCwu1msS80vZEf1qL5izpXPZoZgag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یک شب به‌یادماندنی برای بچه‌ها؛ دعوت احسان مهدی به «سر سفره خدا» در محرم شهر
🔹
اگر به دنبال یک برنامه متفاوت برای فرزندانتان هستید، «محرم شهر» هر شب تا اربعین در میدان آزادی با بخش‌های متنوع و ویژه کودکان و خانواده‌ها میزبان شهروندان است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/akhbarefori/675491" target="_blank">📅 17:30 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675490">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">♦️
قتل خانوادگی در قزوین؛ پدر و پسر به اتهام قتل مادر و دختر ۸ ساله بازداشت شدند
پلیس قزوین:
🔹
مردی ۴۵ ساله به همراه پسر ۱۷ ساله‌اش به اتهام قتل همسر و دختر ۸ ساله خانواده بازداشت شده‌اند.
🔹
متهم ابتدا ماجرا را سرقت عنوان کرده بود، اما پس از بررسی تناقض‌ها، به قتل همسرش بر سر اختلافات خانوادگی و قتل دخترش به‌دلیل شاهد بودن در جنایت اعتراف کرد؛ هر دو متهم با دستور قضایی روانه زندان شدند.
#اخبار_قزوین
در فضای مجازی
👇
@akhbarghazvin</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/akhbarefori/675490" target="_blank">📅 17:27 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675489">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d069bb518e.mp4?token=vvctKUXKkKfVscBayT5hOvLCXy7A1gMrhuNwkFAV1fN4NO6O4lVzavbkhJXPzj7GqW245IGJ9zsDejV51PeEJurSSRGyRlQJ_h4kHfmacQiDSzON_2lA26lgLdgqyRhFJ_aML7zTHXGuDW9WOiKuYkyhj1Xr_V6fvjST-DzNQykgtZYMjcnODBM3C4eYMFsUy8XmUIU5rSdIxQQZMQRe2epKNfW5CuMhb4hho_H6TYF0rpyn7gcU_UsVcq7sDpQRyNWbhBik8xtgUsPBOYtF6dApyVU3VWZR-8Sufo3r01hXetdl_GhfRasg_y4QxR-FJzAZmB2q_ExL57OLr_dafTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d069bb518e.mp4?token=vvctKUXKkKfVscBayT5hOvLCXy7A1gMrhuNwkFAV1fN4NO6O4lVzavbkhJXPzj7GqW245IGJ9zsDejV51PeEJurSSRGyRlQJ_h4kHfmacQiDSzON_2lA26lgLdgqyRhFJ_aML7zTHXGuDW9WOiKuYkyhj1Xr_V6fvjST-DzNQykgtZYMjcnODBM3C4eYMFsUy8XmUIU5rSdIxQQZMQRe2epKNfW5CuMhb4hho_H6TYF0rpyn7gcU_UsVcq7sDpQRyNWbhBik8xtgUsPBOYtF6dApyVU3VWZR-8Sufo3r01hXetdl_GhfRasg_y4QxR-FJzAZmB2q_ExL57OLr_dafTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مرحبا به صاحبان پهپادها
🔹
خوش‌آمدگویی موکب‌دار عراقی به زائران ایرانی؛ عراقی‌ها امسال بیشتر از هر سالی مشتاق استقبال و خدمت‌رسانی به زائران ایرانی هستند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/akhbarefori/675489" target="_blank">📅 17:23 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675488">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iTfN7XEASneaz_NE1yvTqPnFi3LIRfJKUVfLdBR8HG49XghMthzFsCduevtqUMfSpN_DONcBWUYDEaOjMXEdqeyHpjN7IT8z7tOJYCZvcb9_qET7FSz2PPV1WfZApDrWNuyiEHC5OXaK0gEFJNXR_0pJPUHq7idSHk85NxnoqwEE2QGbTI9-J4HIst0K0zw-sOzZiryG-EIywojo5-vXgqZLTeKQVOG5GJu57rrv6EQxJhqtZ5JlagYO07YSkMyf45FkbdLs2-IRg17LyZ_KH88ThKrUq1Yz3zjBR4yWjJhg8uhXKpHUrsow2HV3Hl9Yn23FbB5jqHqpa1onLQTpNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای العربیه به نقل از یک منبع آگاه: ایران به پاکستان تأکید کرده است که آمادگی دارد مذاکرات را در ژنو، دوحه یا اسلام‌آباد ادامه دهد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/akhbarefori/675488" target="_blank">📅 17:21 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675487">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WHpQRPqhfzJNeH9rd-uE7tibujOQxFdMZ8ptWmFxyixKJUyraqPFmjr34OUn4a_pnOUjRh0xYW2ksMKa7phbN9z4sLe5LgEYVhr0Yo0HlfQ0_niKHK8NT67ZFl0od2Iz2EeebkMTyvmRkAGHevPCarUD681I4fN-1gUsTj12edd_5dKtfhDHIDlTeO-Mf5bLXbuzia3c0fAJ1ItmLsFeqe5JT5Jrsxe5wMslf-W2B3A74IO8OLCYMRana0-wuRqcylCGPJOxkH6a99vMOjTbYZP0_1FQSgfCx_KyrDj3eCzIjftlhcG4XGrkt_yGJciEPlFWNGHfGl9wDtJozIbyKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
باج‌خواهی طلایی برای زایمان؛ سکه طلا شرط جدید برخی پزشکان
🔹
یک سلبریتی‌پزشک فعال در فضای مجازی، علاوه بر دریافت هزینه‌های مصوب ۷۰ تا ۱۰۰ میلیون تومانی در بیمارستان‌های خصوصی، شرط انجام زایمان را دریافت یک سکه طلا یک‌گرمی به عنوان زیرمیزی قرار داده است.
🔹
با وجود فراهم بودن بستر شکایت، بیماران به دلیل حساسیت شرایط جراحی کمتر اقدام به ثبت گزارش می‌کنند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/akhbarefori/675487" target="_blank">📅 17:16 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675485">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c18874268.mp4?token=Ahm9HlppvxGLDxj1irxioAEwIzxwdx3KyB9b7q5UBMqhrEWdvTqs2PQpaRcKmh0iJCCIs1DzDK54yB9av5YR9Gauh4_oEFP-_khW4eYcSxaJtegl9XCIUB1WZXyhoipc8tjTW8j21z2izM9EOgGUA7c1oOlxrCGG7TYfxf4YRQKrKSmyxVRFTnF1z3zd6thbw_dksfw6W0KOtX9FcLpQwn1w2xrDN2i9rswgTeBvYka_rk9hVLvPReetQreYH0S-2seuNp7To0Ki3sKvbfppFoCRouWQjjk6-6SHbm1L6XCW3ZaJWUo_3P1Nqy2jMfeKF6DAds50Fui8wfCT_fEqHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c18874268.mp4?token=Ahm9HlppvxGLDxj1irxioAEwIzxwdx3KyB9b7q5UBMqhrEWdvTqs2PQpaRcKmh0iJCCIs1DzDK54yB9av5YR9Gauh4_oEFP-_khW4eYcSxaJtegl9XCIUB1WZXyhoipc8tjTW8j21z2izM9EOgGUA7c1oOlxrCGG7TYfxf4YRQKrKSmyxVRFTnF1z3zd6thbw_dksfw6W0KOtX9FcLpQwn1w2xrDN2i9rswgTeBvYka_rk9hVLvPReetQreYH0S-2seuNp7To0Ki3sKvbfppFoCRouWQjjk6-6SHbm1L6XCW3ZaJWUo_3P1Nqy2jMfeKF6DAds50Fui8wfCT_fEqHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آنتونی جاشوآ بوکسور سرشناس بریتانیایی و قهرمان سابق سنگین‌وزن بوکس جهان، در مسابقه دیشب خود برابر کریستین پرنگا، با آهنگ ایرانی وارد سالن شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/akhbarefori/675485" target="_blank">📅 17:08 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675484">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبنیاد برکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fEXBTbLmDGYgLkaGD67M5TJHal7HZNTNC9s63VzhnTNZllBXxhhSaMnvwAE8IZ96EJTv2vYgXeUaPpBjeYrCq2j1pvto_OCdukxrlLr5ajGqj-vZNTxBuULT8uD5HMgRi9hWJTMM17tRf3FrvnDnNxrs_CKGu7iwhjgxmz637zWKODOjmJy9W_i80BDsPQhv_NLEAOcO0vTsvlulOsVGsqsFYQvK7dVCvWNUtyaxCQn63AP-ACPjpf8pPkdJ49KzhCzruXUDEzNUFUplFSSDp-eBtfNy7qPC8zgo5QGIp2cvkTScMmDUz-xkhiFK6wCvjM-MZ_wtANmumwsqTpcKvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📞
مشاوره درمانی ۴۰۳۰ با تماس رایگان از عراق برای زوار اربعین
🔸
سوالی درباره مسائل پزشکی یا درمانی در مسیر اربعین داری؟
🔹
سامانه ۴۰۳۰ به صورت رایگان و ۲۴ ساعته آماده پاسخگویی
🔹
مشاوره رایگان در زمینه‌ سلامت، تغذیه، لیست داروهای ممنوعه و معرفی نزدیک‌ترین موکب درمانی
فقط با شماره گیری 4030 بدون نیاز به پیش شماره از عراق
یا با شماره گیری *4030# (ستاره چهل‌سی مربع)
@bonyad_barkat</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/akhbarefori/675484" target="_blank">📅 17:05 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675480">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/90be754f92.mp4?token=Sr4kHhZLzskcQ6_38Z35ImpVDb7uoKlAV7NYJiWpQRqyLi4zylx-nHknelhLyVmCvTV1oF2lv-rm_cEnd6UFV1b8lqARVDgwG0MLVX3HmI25fozhvHhSaq9owPGoNl1qd_G7ZuM5Wl_vUOfJ1_l4oQTc0Se86wWo6VP4N3Mo8e3qm_YPRn8IbXqVmWm3wMaHmaVRK_j0Jgg9Iexl8Pa8uB1Sj3O6CC0OvE9PHIICAy8bIP6flDrCoa0Bfqu94AzqQP4LqdjRIismIbDmsxDQ-9TDq9ULh7El0BAUFtYMDJDtxcRz4nhshkWpjLkzoHXbFP3QlGa9iSepovrHgOiipz74KH-WU2J3eefYNEbA_ttcj6d3J_P7amyrKkHRqVPp5N1JGO0PLPI9Tn2bM3d--_pAKTs1kAoC5o8QGUVhVSsOHUe4b98K8rjPBghYzNTKhNusnY9NvZXLbOLBg-oO_Z5nxHTmVF4u8CcUP93iD1ofBt-LrUflB6K-2kny0YYQj0_kNd-d6m7bWnelB6O1-cnucyzWjraTdRO3PXXr6vbxLAOkLWyAjONO1dZev-Q4A9g7MvbZAcMy_Bl8ZB1pjtNUh_wzjOc7m3ato2b1neQHQ3fOkkXHP8fTAENLhBfIe4n5q9ySsRXuX-1vbzomV4lpkXKApya2R8yQDUZU1Rs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/90be754f92.mp4?token=Sr4kHhZLzskcQ6_38Z35ImpVDb7uoKlAV7NYJiWpQRqyLi4zylx-nHknelhLyVmCvTV1oF2lv-rm_cEnd6UFV1b8lqARVDgwG0MLVX3HmI25fozhvHhSaq9owPGoNl1qd_G7ZuM5Wl_vUOfJ1_l4oQTc0Se86wWo6VP4N3Mo8e3qm_YPRn8IbXqVmWm3wMaHmaVRK_j0Jgg9Iexl8Pa8uB1Sj3O6CC0OvE9PHIICAy8bIP6flDrCoa0Bfqu94AzqQP4LqdjRIismIbDmsxDQ-9TDq9ULh7El0BAUFtYMDJDtxcRz4nhshkWpjLkzoHXbFP3QlGa9iSepovrHgOiipz74KH-WU2J3eefYNEbA_ttcj6d3J_P7amyrKkHRqVPp5N1JGO0PLPI9Tn2bM3d--_pAKTs1kAoC5o8QGUVhVSsOHUe4b98K8rjPBghYzNTKhNusnY9NvZXLbOLBg-oO_Z5nxHTmVF4u8CcUP93iD1ofBt-LrUflB6K-2kny0YYQj0_kNd-d6m7bWnelB6O1-cnucyzWjraTdRO3PXXr6vbxLAOkLWyAjONO1dZev-Q4A9g7MvbZAcMy_Bl8ZB1pjtNUh_wzjOc7m3ato2b1neQHQ3fOkkXHP8fTAENLhBfIe4n5q9ySsRXuX-1vbzomV4lpkXKApya2R8yQDUZU1Rs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روضه‌خوانی سید مجید بنی‌فاطمه در منزل زنده یاد اکبر عبدی
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/akhbarefori/675480" target="_blank">📅 17:00 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675475">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">♦️
از میدان آزادی تا کربلا با پرچم «یالثارات الحسین» به نیابت رهبر شهید ایران
🔹
مصطفی زیبایی‌نژاد مدیر کل فرهنگی شهرداری تهران: امسال با پرچم‌های «یا لثارات الحسین» میادین شهر تهران و به نیابت و خونخواهی رهبر شهید ایران در اربعین و آیین جاماندگان شرکت خواهیم کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/akhbarefori/675475" target="_blank">📅 16:53 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675474">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kQJR69hxBLau3p7Lu6geUUxuy2debICLYuho_u1sJUhPFt3eXxNtOblXpjn3ZnFh3KN10vW9Yq28eUa5kq-ea8gBaRws4tZ9IsNmSYEymr0VVez5N1ofkK21XYRHQ9nnD64CStQh2n5uwCuyh9_5CcO1FJVHQl2yXLGpQK15ZAQoooEJSPlERFYxFAxfGKpMd4mB69hL6j4oaMN90nvu19IQoOCcuX6JMSm0gRkIuaDW95oBmmLtnF9VdJNMA0WYVrSLm6Viy5AQdh573mGfCB_7muNwjuHCjBWLP08dS9bAoZh7Fdcy1fELR-E3mUFr7Rp8LybwNzPqkhZR6YiylA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نسل جدید هوش مصنوعی OpenAI معرفی شد؛ GPT-5.6 با سه مدل Sol، Terra و Luna  سه مدل مختلف معرفی شده:
🔹
Sol → قوی‌ترین و دقیق‌ترین نسخه
🔹
Terra → تعادل بین سرعت و قدرت
🔹
Luna → سریع‌تر و اقتصادی‌تر
🔹
عملکرد بهتر در کارهای تخصصی مثل، برنامه‌نویسی، تحلیل‌های پیچیده،…</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/akhbarefori/675474" target="_blank">📅 16:48 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675473">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7ef1d20ad.mp4?token=a52T1UKO8oLkWjqUF34kYMM_XcX5gUA-iE6W-R-p5Uj4EoBVY8Kedkp19LBzvXWig52fbM3jSnTmokIUKDcgove9xJkBPtK8aPWbALb1MPTuBCnjY_yvTVtjdACcKEnoHkphSqsCyNw_z3Ej4oKsSW-mG803TBiQ7AxeaGWMYroepSEiE42vzvx1uMBYdiVtlMRiRKlvZNM2xaTIXqUXW6eYyh2jE0dRT0VZY7_QDsL6-c-HHEk7Gvf8GCb-rrd9mF4zNPYDsBuTK9o_uHqz5YIDLXGyzQ3DI8oAT-YsSw-jdnlvc_245TxlN4gOZUXFG8XOofAWb-PDUA4PolJ94g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7ef1d20ad.mp4?token=a52T1UKO8oLkWjqUF34kYMM_XcX5gUA-iE6W-R-p5Uj4EoBVY8Kedkp19LBzvXWig52fbM3jSnTmokIUKDcgove9xJkBPtK8aPWbALb1MPTuBCnjY_yvTVtjdACcKEnoHkphSqsCyNw_z3Ej4oKsSW-mG803TBiQ7AxeaGWMYroepSEiE42vzvx1uMBYdiVtlMRiRKlvZNM2xaTIXqUXW6eYyh2jE0dRT0VZY7_QDsL6-c-HHEk7Gvf8GCb-rrd9mF4zNPYDsBuTK9o_uHqz5YIDLXGyzQ3DI8oAT-YsSw-jdnlvc_245TxlN4gOZUXFG8XOofAWb-PDUA4PolJ94g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گروهک‌های ضدانقلاب را در نطفه خفه می‌کنیم   سردار محبی سخنگوی سپاه:
🔹
ما از نقشه دشمن غافل نیستیم. اینطور نیست که سرگرم تنگه هرمز باشیم و از بقیه توطئه‌ها غفلت کنیم.
🔹
دشمن می خواهد گروهک‌های ضدانقلاب، منافقین و سلطنت‌طلبها را مجدداً سازماندهی کند و کاری شبیه…</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/akhbarefori/675473" target="_blank">📅 16:47 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675472">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/039b48e83b.mp4?token=CETsBEPlSkTmWtHVNvFDtjsZNfxL0_csIoDGoTOMTX-3Glhe9dmVbdbeQhVnSL9eyUwcFfeVAl6VTc-vhKnBVQ3FtcXivXdoFfQgrW6omHu3qJeNCB3aneMcsEfeuqEX2D65YgDDsKL3LQ_afb1Jq4YN6QjL9oqVm-sEZx4Kpy6gMD6_uYdD5Kyh6D-yLvW_o_H6scUsjmZJW-uhIYTa8kWzRjfrSPQlKRuRWChyi33TGcajYPqqGxGdeOC-JkMFfImOuKecVAi-6_wl8y_C8CUWz3pRCZelBV_SXYCq2v96MNlRabQas71WWMeB6iEBIY3JHIXyDA77DX2FuJhuMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/039b48e83b.mp4?token=CETsBEPlSkTmWtHVNvFDtjsZNfxL0_csIoDGoTOMTX-3Glhe9dmVbdbeQhVnSL9eyUwcFfeVAl6VTc-vhKnBVQ3FtcXivXdoFfQgrW6omHu3qJeNCB3aneMcsEfeuqEX2D65YgDDsKL3LQ_afb1Jq4YN6QjL9oqVm-sEZx4Kpy6gMD6_uYdD5Kyh6D-yLvW_o_H6scUsjmZJW-uhIYTa8kWzRjfrSPQlKRuRWChyi33TGcajYPqqGxGdeOC-JkMFfImOuKecVAi-6_wl8y_C8CUWz3pRCZelBV_SXYCq2v96MNlRabQas71WWMeB6iEBIY3JHIXyDA77DX2FuJhuMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نکات مهم درباره ساعت و نحوه ی مصرف مکمل‌ها
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/akhbarefori/675472" target="_blank">📅 16:41 · 04 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
