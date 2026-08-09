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
<img src="https://cdn4.telesco.pe/file/LS3aAaFhtq0KVGUsAKWBXtM5RKCtqYzs077z4e2EHIw3oA-UhYQKODuLcm8ENz0V8pkOFf6AfjFe_Bv4Yr-Ru50z8IodLnnToCXrYCHDvlQyuzwWj71arb89cGAAUvj2vtztZ-ii3ZDv4Ak4M8iAsBLtrt42DQvmAEktxn0haRfhgZ1XB7kf_yQktJNoOEH2wyPVxy-5yUzh0vPOqd2T3Z6NRGChWZ8zqREtKxQ0PVZkK8DjvgeaAB5JFO2ubG9sPIzdLjPcbOoY2t8TeQ5TKj_NqU8aqL9-TszyCSA5WArgXoKCAJwzrunJjBLkO1rJRhtP6_GsoZFrLKMsin1gmw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.82M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-18 22:40:19</div>
<hr>

<div class="tg-post" id="msg-455206">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cfc934aeb7.mp4?token=UUe6oSpMUX_bGXpqXx0JEI23xI6pSLouEEbKrtFe-yIJsZ-xbJzdzUqpxAva3APsGSHAaOy1HbdXBI4hBxKSZjFC1fVWS7Tv3tgJXRSVtv-M9SWOmpSbmh6kIzbbHMt3cRbba8cYoSEZ-9Rw1NgMSHCEVXBC2wQzG95BGNLkDTRhUKegnqRgtjPRiHMZVuve4AA_mTWBKhsucjDGtFsb9cI8qAc4CNJdAlc-lhG0T3D0Sa5gYmCaraavPBu5DgpBAKEV5IWyAwGO3vuii0fvrNRGAUb8LasKh5nar8rxNHgXoNmaVID6P4Nu3r5fzhKBfbRtYzT_N77g6rLshiSjag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cfc934aeb7.mp4?token=UUe6oSpMUX_bGXpqXx0JEI23xI6pSLouEEbKrtFe-yIJsZ-xbJzdzUqpxAva3APsGSHAaOy1HbdXBI4hBxKSZjFC1fVWS7Tv3tgJXRSVtv-M9SWOmpSbmh6kIzbbHMt3cRbba8cYoSEZ-9Rw1NgMSHCEVXBC2wQzG95BGNLkDTRhUKegnqRgtjPRiHMZVuve4AA_mTWBKhsucjDGtFsb9cI8qAc4CNJdAlc-lhG0T3D0Sa5gYmCaraavPBu5DgpBAKEV5IWyAwGO3vuii0fvrNRGAUb8LasKh5nar8rxNHgXoNmaVID6P4Nu3r5fzhKBfbRtYzT_N77g6rLshiSjag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
۱۶۲ شب ایستادگی؛ حماسهٔ مردم همچنان ادامه دارد
@Farsna</div>
<div class="tg-footer">👁️ 338 · <a href="https://t.me/farsna/455206" target="_blank">📅 22:40 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455205">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a012b9df14.mp4?token=CKiV4euGnljzJnfkp_Q_8b72wrI1veA9Enx4sv1ubDlmVzPifnuoBuU72MrqasTMJSy7ds1xXckpZFqtQ5qxhqxYyzHjfDTYCiZa4BxvxgkmsMfzVKzI_X1ns1i-Bc5KRGEHPjHfhH7CMc6N2n5jnGL874FiE2EgSMuQ5Xd5TmAPbadWEjL0ObWRXSylxDD55T0ViH-sGdUpnznhAX0CLk9nmq5Wa-RUY8aSVPZ0j9b1yf9y4i2wdmvieVFzXkrrQ1wIndQGPaWElxZwOQBrbs4rVlTs0q9I-jgDx6Aa3xNM3YoN83nTWW4Oj2_20A_WYS5nrOXKJR8BkRSifVvNDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a012b9df14.mp4?token=CKiV4euGnljzJnfkp_Q_8b72wrI1veA9Enx4sv1ubDlmVzPifnuoBuU72MrqasTMJSy7ds1xXckpZFqtQ5qxhqxYyzHjfDTYCiZa4BxvxgkmsMfzVKzI_X1ns1i-Bc5KRGEHPjHfhH7CMc6N2n5jnGL874FiE2EgSMuQ5Xd5TmAPbadWEjL0ObWRXSylxDD55T0ViH-sGdUpnznhAX0CLk9nmq5Wa-RUY8aSVPZ0j9b1yf9y4i2wdmvieVFzXkrrQ1wIndQGPaWElxZwOQBrbs4rVlTs0q9I-jgDx6Aa3xNM3YoN83nTWW4Oj2_20A_WYS5nrOXKJR8BkRSifVvNDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حادثۀ امنیتی در نزدیکی باشگاه گلف ترامپ
🔹
فرماندهی دفاع هوافضای آمریکای شمالی اعلام کرد جنگنده‌های اف-۱۶، ۲ فروند هواپیمای غیرنظامی را که وارد فضای هوایی ممنوعه موقت در نزدیکی باشگاه گلف "بدمنستر" متعلق به ترامپ در ایالت نیوجرسی شده بودند، رهگیری کردند.
@Farsna</div>
<div class="tg-footer">👁️ 3.3K · <a href="https://t.me/farsna/455205" target="_blank">📅 22:21 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455198">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T8JnFBSHt6rdEQ5lTpMoxAlGZc26WmCHbzhcj0NZUUbay465u9KYSv3bmrrMRhXvRxjiXiGRh55FFKV2rOpaivjal_wYTGs4cbksmqwZj7npeFyIBBTQX7cc-8d8cnyQaNXuNg80xlXKfK3FfWBL5_BqtgXCah0DuPOMyRbXP0oVHFn0A9-DS5m02p82pvtemTaC-nncKmK3D5-kUauUeMGc_MhLjrEUByY0jfyutbRChCrUUo_B2wFh4DyCb3bDiVrOUiBxiwvcoHkpN-fhtVIbpGsNNoaeo2fecBRqgAReTpEwFFaNwwpRRsUhWFZfdlEirVvPc4E8wbCMeIkiiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OEwr09bSZR_s4hkJoESvy2XD8eyByKw5rMeVXo8wjK0opuoBWVKqi031qJOrqjCVEzTmooImoOx-W4Ai2TFuafKbkIHZaz8mEK6FyK78CMZZMDo3qxCHI8rgyR4jMPqVNv1tw7wV1hrfByXySVmnp6LdXY4J6xudomQOGDzOvSmStycc4Oo75HI2Un1SLKm7qxLQXLyvrTE6yP1Tm4oz4umftWs9Iv_tERt5xSavw_xkAQ5h-5TzLAQVb2BOtxtsPa8Z-Rm6p1lkyFW64fqFtM3WdA8r_owfs98ilGeyQwRtMdAxnXPv9CieaTOz3V-s_GOpMyQIArLS5EXE_cZdqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BXUsOiKOh2T-W3WZ7U6x270tJKKYBwPo0cmW-xGrCaaf3pn8S8Gt3Y5EXIeBHXKpI-iXxktZRDBthWRZFolSMFwy3FXKmHZbDyPF-pOYHnJGkZYqVEpaj7nVYUXlsdJTZPP6UhGZL2qVazWY-_a-9Ny7eiCKyelb7K08_Rlz80l2VjahRaBGgprHdyL7biFEz7pQXMTZdFIAeA6Dm-XRxle3TMYApPakbpAkkiHV8KsMz0AfX97Pq6xsXEo1FvDXE-8oNzbcQbmVBIUnV2zCukIiCGXDpPA4f2BGWLzIrEzN7sxt9EkY-Of5mo4EJx4qq-4mkoNt8PWOw4_zHZLeMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uDSDkUHPy7ALus39RQJ14_USK07kWwt7UFpehyNtINYLJsn6M9OfY1ACHKXrflGh2Bcnz2WRQYIN9VxjZr13GxVRebsGZFbiOOfTdsRbTPOvP3HalZkOuQaBrQ1DLCQCH94F-QbCK7lViLpJQ1ioR7QZdKpwnyMFbQdslkTyuvmBuMQaEgFDKDYW6ELmbEu-XzO0rNzLCxktFFqetdgpWgnGRXfWs-wpz-CGfRSrCjPE6BX57bAojYXSOd9Gs-Ew2vshsmGBlsAv5iNDwkGiFMzseH5ADxiSjTCqr2VPuk_NZGYTrGjBx0gzqca3tXSPZR1ycXZBVbqxu2ASX5fKKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YSO5XmAyzOYb9YhO5pgGqyGFSPiPviTGnweCEdD3tQZArldhJC918YiNa_1vVRXqoa2GsisOi2ANXpHscl4ZC6qvA22SMBxAguUS4zfVzZeFNeMNjl63JWQopN_eHZqhDWDvhlwJ_zMUjj-g6kjkH14osqrEtToDV1GKdKfXWvb9wmekkyn8yo29firA48aqJBXI6NV2D4WUMVKz98TaTX_gnaYftGH4GSnFID6-KRDJ8X4RkT1rCxT2HSSRZbo8mmHIUImstTkvrFrOzIX0RE4RhMrZJyz2Tsv6inCPpNF-kTLdbkCSpYb6xf2nbpvPMsH6qcSyz_aZNoActcb2vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rbrJxIwIKIzTdrhmmk_-sfkW2pSV820BWFyUaOPfAIlrCbfPfFF_hOEPKRCrbUKHXDxdDd__epFZmbQsRRujqH22-Kuwa3Hru6zNjmgwYefvh2jykFcCKico_BC81YvW_t9sZhVw65mxtNTYDQdlWgY5nQCN0js3LioXK8h3ZVh1xpcykrjZLEtccDUxcwfBGmVD1MVDROfSL--vgC9eEGclZoTn2oaIxb45dQCqYfsEoiZX1U9LEkaHppF-xtd7Qpc7a9Q_kdQJl9UYGo8thqp0oyQ7B153lrTrm3WSiEf1OM4iQx_84FLZn_PVkFxITc6DDIoxgQ-N32oR03Nd5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ikUCUMY07a5g601Q0IGncSBU-QNzlkWiHilx8i2RCdGFkoPP3lj514lfZznVf2U2z3NkM_JWrECI7gxhfhiZGC-ZJ8cXKQEanwZn0fI8gnC7T-k2t01nXcMkA5dj0YNsfNJmtw3HYoXAhlDsUlVxTZrRWHZnOuGRgNVeIOZqF3SLRZdXxUYRCtigj1PzPNLBkiJf35uGpt3ovOvhZFAdqKNiVvOZYi4m7MzqyiOEeFJgP9KGpbXkJCO0bYNiW5c1VeVnM3YprqkN5CqKa-LVZhjmRCgzpPQ_Q5wZrPeo1VUhdrdsZyHTynfPu36yVC0RvwtmdXh_UoghrwdPaIxc6w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
سالگرد درگذشت استاد فرشچیان
🔹
مراسم بزرگداشت سالگرد درگذشت محمود فرشچیان باحضور وزیر ارشاد و سخنگوی دولت امروز در مجموعه تاریخی سعدآباد برگزار شد.
عکس:
‌ محمدمهدی دهقانی
@Farsna</div>
<div class="tg-footer">👁️ 4.29K · <a href="https://t.me/farsna/455198" target="_blank">📅 22:10 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455196">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qkGfQTBbK_xhEDn_1npL_iv8FBf1mRxgsjPF2ZLqEZTJVFZsqieZDS23kGizWux_TQTUzaX1E0VS228lZqxVeAlPBw5FW5an22knoqn9-URUKdlgwe1M4_W_kvmdfx3ewsCMkL2moZuXwVOsvfi4sF3hvETCGAUsax7Tv6EzLPGDtnEd9kImtYd9kEoZA3mB9I9GfsrRFKfdJ-LpIANi7xkGGO66a035VOZ4kTvr3xEc98dGorAsoAoaEzzc3xZAgeyweGh4AfEMz2G8J9gePEicCor9pdIzCAEZg18_QqGgz4g9g8xsiLMfsRUQlVeFvUxmJhMJdMAia6_IqvtGdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جزئیات جدید از ضربات ایران به یکی از مهم‌ترین مراکز ارتش آمریکا
🔹
بررسی های اطلاعاتی نشان می‌دهد که در جریان عملیات «وعده صادق ۴» و هم‌زمان با پاسخ نظامی ایران در ۲۸ فوریه ۲۰۲۶، پایگاه هوایی الظفره در امارات طی چند موج حمله پهپادی هدف قرار گرفت.
🔹
این پایگاه که تنها ۳۰ کیلومتر با ابوظبی فاصله دارد، یکی از مهم‌ترین مراکز استقرار نیروها و تجهیزات آمریکا در خلیج فارس و محل هماهنگی بخش مهمی از عملیات‌های هوایی ائتلاف غربی به شمار می‌رود و میزبان جنگنده‌ها، پهپادهای راهبردی و سامانه‌های پیشرفته فرماندهی و پدافندی است.
🔹
نیروی هوافضای سپاه با اجرای تاکتیک «ازدحام پهپادی» و به‌کارگیری پهپادهای انتحاری از جمله شاهد-۱۳۶، موفق شد از لایه‌های متراکم پدافندی پایگاه عبور کند.
🔹
بررسی تصاویر ماهواره‌ای نشان می دهد که در اثر این حملات، منطقه استقرار پهپادهای شناسایی و تهاجمی ارتش آمریکا، آشیانه‌های هواپیماهای هشدار زودهنگام، یک رینگ پدافندی کرتال (Crotal) و مرکز فرماندهی و ارتباطات ارتش آمریکا مورد اصابت قرار گرفته و منجر به تخریب و نابودی آن‌ها شده است.
🔹
اطلاعات به دست آمده نشان می‌دهد که پیامدهای این حمله فراتر از خسارت‌های فیزیکی بوده است؛ از کاهش توان شناسایی و فرماندهی ائتلاف تحت رهبری آمریکا گرفته تا ایجاد شکاف در پدافند هوایی الظفره و زیر سؤال رفتن امنیت یکی از مهم‌ترین پایگاه‌های نظامی آمریکا در منطقه.
🔹
این عملیات یکی از مهم‌ترین نمونه‌های به‌کارگیری تاکتیک‌های نوین پهپادی در جنگ ۴۰ روزه بوده و می‌تواند بر معادلات بازدارندگی و امنیتی خلیج فارس تأثیرگذار باشد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/farsna/455196" target="_blank">📅 21:58 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455188">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39826177dd.mp4?token=D956e4SLKi_xxsDBu3FH-NN_tvzkIs2mEO4MmcqP1V_QvfEp2RUPYLy1l1gEZOfE5egBlF3Zd1pkG0KQ04EufIuuBKCQ-bW_CK-J4xiYfomLjO-NmTxgE-2TOSVT9tz79LW0FnTAZ6vaD19-m8a6WOJxDbU1icnucKSBM7uD2ULeBUOJZ-BYFUwmgPPXULpXRNhyGfN7T-1yxRuwhdxm03K2rjqo2XjcY2jiMlcBeQdxtOYrLQBK6T-iM3UIdjbnZp80sArU18MplhnmauheVgZNfBj-lz1PSqUi7R48S4zncA0LT6bfNUVA3FcdHVlSSxiDPMUDAKAJdj8BQaWlRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39826177dd.mp4?token=D956e4SLKi_xxsDBu3FH-NN_tvzkIs2mEO4MmcqP1V_QvfEp2RUPYLy1l1gEZOfE5egBlF3Zd1pkG0KQ04EufIuuBKCQ-bW_CK-J4xiYfomLjO-NmTxgE-2TOSVT9tz79LW0FnTAZ6vaD19-m8a6WOJxDbU1icnucKSBM7uD2ULeBUOJZ-BYFUwmgPPXULpXRNhyGfN7T-1yxRuwhdxm03K2rjqo2XjcY2jiMlcBeQdxtOYrLQBK6T-iM3UIdjbnZp80sArU18MplhnmauheVgZNfBj-lz1PSqUi7R48S4zncA0LT6bfNUVA3FcdHVlSSxiDPMUDAKAJdj8BQaWlRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نقل‌قول جعلی منتسب به سردار وحیدی چگونه از هند به سخنرانی نتانیاهو رسید؟
🔹
هفتۀ گذشته نتانیاهو، نخست‌وزیر رژیم صهیونیستی گفت «امروز شنیدیم احمد وحیدی، فرمانده سپاه پاسداران به صراحت قصد ایران برای توسعۀ سلاح هسته‌ای را اعلام کرده است.
🔹
این درحالی است که این نقل‌وقول جعلی در هیچ سخنرانی یا گزارش رسانه‌های رسمی مطرح نشده است.
🔹
روزنامه اسرائیلی «یدیعوت آحارونوت» نیز ضمن اشاره به اشتباه فاحش نتانیاهو، در گزارشی بررسی کرده که این نقل‌وقول ساختگی از یک حساب هندی در پلتفرم ایکس آغاز شده و در حدود ۱۵ ساعت، از چندین رسانه عبور کرده و در نهایت به سخنرانی نتانیاهو و سپس به فاکس‌نیوز و مقام‌های آمریکایی رسیده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/farsna/455188" target="_blank">📅 21:44 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455187">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OxUmcoNaSR_XZ9Ck0bB8XN2A5zJlnbiQd_4TNr_uS7Lk3-Uckmpal2IayPbyW9RPgcaO6ngoNuc-5iZIJjfAFOqUM7Z0CBEams3RlCEvnmhywDDrwc3NZQRE6F496dXGg7GL0m3sML5HTNfDrwEaZ9E8efnA6nUAjk8W-T06BuCo1qAbY16yDNRZi4oRfFUfbsbykx1QFC0RTpWWbUg9fxNICtt7UARsfss8E4m8wWNeESQpewA-Blly7zalQXR3-GEeaTQ9bDX0YTzNZzZf1vvY3fBSVOxw0x7FPVyhFBL8PgFFQg4P1DwqmBUtiWKekcBJ-i-a1OWcjLFsxLCW2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fyL1vQ0pozGXEVXdEWFLbOMdVsriNfqTTodmssaFGj4vTRd_U8h-L83cRvz0XV7ybODdF-VF9Tm-KL_85Q2p1wtDyyrF942WXEDXheX81gVv5zJwE5duUw-44aes7P_pAMOJy8FRLlXhXW29IXkglJUm-uXs96amPD4SnazEjUnbxFZs8L6l68_k3s0vgCbSvK98ToyvKsbbt2fe6xKUSqadKq4aZRndAUaAys3GjT3-Dtq_6QoNH1n4l0ZbyEYS2_PzSDHyW-Z-3wcTro5Z8PNFMRbM-b5qwOCTeU1tgCPcPSeLE2paiRwWueLntr3RfU2rWcBXXnah-abz3w0U4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GcwkJb5MBnZ8pTeHF9yrFGXeNnaI1T6hLWd4q1fxVpIXXOmEDNdnZew7298-zwiqXphLjnXmfAtnGNhRxRVq-gjaz6-mknha7d3XvU2vEwIhrnKOdzQ2yXasGsgkPj_WAdIMsSYrE7yI-br--4-qDtV8kQZ-GDksKVk2Q0QUTb9IJVaOqxKVHnRAbkiSYqyykwjeUPM4bFVhsZmwWkWes1BmarCovN0xYESioL0JQ9sefOQwXDJlqUPPO9b7FH4JgPKSurpjVz5z5hcyda4QdRu5AztDzpnNeABnB3hB5bfcLOvH-r2TTRxjy6MUNmnGUZkkqdDFUbm3J_sfPLwIGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Apyin8gwV6Mj3aSh3_q61-cY9suu5-pkASuQDlL07QQilsn39NC0XeQws_y7j710ZUNAc5NXGuUUWXtRzE-p90KhHUaeCqoayXAMYPMu8uLLgDRmR3G0iy7JQGU6G34w5Ek2Y97WEUX6hs5H_B6nYc1ypUaR7JHcogIzqYp8qTNOw9g03lAHJxuAUlHSJBCrRFU7EvXt1KLMObK3oPen_YsHnag2olXVqC9TRb4Dbi3R50VaA_pFZ5wVw5Z8QblP2ybigND30oDCs04YVjMYaTtIbfCE1abKkxfYgt1FEWlcwmwMEcHqgAPrCF_W-eiJ50TwVPdSWEjSJgi7BFhGXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iTUY_UY9255kvQvB8jcHjPq1xxfW5xo6TqS1l3i-rly8goEJD6BMvHgJdPK5dWhHfH1dW7QAPXHeDKVwuh9fJo1t92_pyzGmSO_Y7WqJ0MZRTbx6rNZRlnb_D8FFl9T3lgUSe1N_6DMT7ifFe-jXon4KY9mTApPzWsINb8WWR9y1oMO0tHtSJ3AmaeNiKjnBtMcjsARfnr-haLa73-JvOYAubetzrKbE42zFDbwvG2DbNWrUgh8-U6pPvznRwEyfVXwi2qq-LbAQ4PcatTIbqx262e9yIlS229LwKserW60m8CLQj76kv8HwfkM9OXNmjziCncASFcyTSQyFx-YD3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jDSL-kFAi_Ysa0uJxNxlEyrQgtoqbJc6vT6Ja9JV1KCVBNPBo86aBXnmAtsKs47iHKvoGO6FS7tOaBDyrGMd_P2dLPuYI3pGNlr-f6gR3e4M7nNjTp0zWOJdyCHPGXKFBpg0dIM1RO9pULnk4i6Pq55y28SleJwZLNbGTKytvaINIuXFQcDaEwX0sq692GfKOvWrJJ-_ZsuQD-2uevkzgGZUnRDozNxcG3ZMFer2ari1P99OQDmSnQ7qm0WVsXwbgg_NP4QAWzO105--JHwkiHKt5RQhh15tdQ35KpLI310SgJ03dYxwgDcApXaUxTODn2hqsRbSaL0rSQlzkAyN2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q-hY_0Rs3c2eWQROXMK31gTNyCw749OZlTNqUDliBY4UgvhsQLuQJLXwwtxORrJvE4hgHUUuGJXExn3JDyg4L3eM23hhdGp_gn31RlqMn5iNsqSNw4ehoLVPx1aTl3540oTiZdWPaV-D-9SKVhdMV-iMUeDdMQEeKh3d1RIdftENY5nmO62HSC0rlvmN2VfgCtiHZq8RLVsSCMGAag4JRZr6KWKkByaCoYXHsklf_pfd6kwk-66PPJjKNZYyrLT6bRcEGFe_YBZKma_CVPLeHaY79IwPAuJU3qykH9lTFhYgW3f0vE3UGMXJf3KC2wTfDdS2V9wfi1oDRenoUnCB1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OTIegI7A0bPDDg6-31sMtTzA_J8QrxMIAcWEmUNL74sUTGaVTknsjj9rx_FzROvVki0TsO3djqXq8Fje41T7ACoK_HIGZyx6yNbcXySrsr-sLrXjRINugaHvq8SxSH-hobs8GxYGHZbI61Gsw0CVHS29NtFFjcIXF6SbqMfbpQsX7Thhn8zZiNB9GMxioe06Wzb6nLzuS2KZ3_mGNLrPfs8uGsNs6z7tEvo09BqXggvpzWFdnzsqXvTsHpKHmcaVmkQ9DQkZ1_ka9P4uGU-J5B_TBAjGvHRw05fY9yglj2QniDyAYpnt6-iX4TVAOQQofEU11t7Ml-P0bPo-DKLbCA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
تصاویر جدید از انهدام مواضع نیروهای آمریکایی در غرب آسیا
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.66K · <a href="https://t.me/farsna/455187" target="_blank">📅 21:44 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455186">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/36ce2e9abd.mp4?token=S_Ca4LNs3IhI-RJqqjQ-Jl23KnMEuG3aknZqWSvK6ptZf2T3r1OYsClukhDtYM6tSy0wKqHF68OPscZdYktIaFv-F7Xh-ybu2RNjaUn8uZTKwZJ_PkAgyrZOST4PFV17Q-etuT2ZXE5gAOCEgCgqTi2koNbJxhWn2L1fdHq7CbYRhM7NUG4kn1ox6y8syDLkaIhNvooU6KBtTkR5aWzUH_gKVLy6cdg9FbNaGtebN3guetmTIinUhP_p0M_u-JgB6QUMELlxRQC-8-9DzX0RHqA9a7HE1tIQceHOFhdgImX1IeDRKqmsvgiB-rZhSSWnx2_f0aCa6gkf3FhB644uGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/36ce2e9abd.mp4?token=S_Ca4LNs3IhI-RJqqjQ-Jl23KnMEuG3aknZqWSvK6ptZf2T3r1OYsClukhDtYM6tSy0wKqHF68OPscZdYktIaFv-F7Xh-ybu2RNjaUn8uZTKwZJ_PkAgyrZOST4PFV17Q-etuT2ZXE5gAOCEgCgqTi2koNbJxhWn2L1fdHq7CbYRhM7NUG4kn1ox6y8syDLkaIhNvooU6KBtTkR5aWzUH_gKVLy6cdg9FbNaGtebN3guetmTIinUhP_p0M_u-JgB6QUMELlxRQC-8-9DzX0RHqA9a7HE1tIQceHOFhdgImX1IeDRKqmsvgiB-rZhSSWnx2_f0aCa6gkf3FhB644uGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خبری از ۶۰ ناو جنگی آمریکا نیست!
@Farsna</div>
<div class="tg-footer">👁️ 5.99K · <a href="https://t.me/farsna/455186" target="_blank">📅 21:36 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455183">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🔴
حضرت آیت‌الله سیدمجتبی خامنه‌ای در حکمی محسن رضایی را به‌عنوان نماینده خود در شورای‌عالی امنیت ملی منصوب کردند  متن حکم رهبر معظم انقلاب اسلامی به این شرح است: بسم الله الرحمن الرحیم برادر گرامی جناب آقای دکتر محسن رضایی
🔹
با توجه به تجارب ارزشمندتان بدین‌وسیله…</div>
<div class="tg-footer">👁️ 9.51K · <a href="https://t.me/farsna/455183" target="_blank">📅 21:20 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455182">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">انتصاب ذوالقدر به‌عنوان مشاور سیاسی رهبر معظم انقلاب
🔹
رهبر انقلاب اسلامی در حکمی آقای ذوالقدر را به‌عنوان مشاور سیاسی خود منصوب کردند.
🔹
متن حکم حضرت آیت‌الله سیدمجتبی حسینی خامنه‌ای بدین شرح است:
بسم الله الرحمن الرحیم
برادر گرامی جناب آقای دکتر محمدباقر ذوالقدر
🔹
باتوجّه به تجارب ارزشمندتان بدین‌وسیله جناب‌عالی را به‌عنوان مشاور سیاسی خود منصوب می‌کنم. امیدوارم در انجام این مسئولیت و در پیشبرد آرمان‌های انقلاب اسلامی، تحت توجّهات سرورمان حضرت بقیة‌الله‌الاعظم عجل‌الله‌تعالی‌فرجه‌الشریف موفّق و مویّد باشید.
@Farsna</div>
<div class="tg-footer">👁️ 8.88K · <a href="https://t.me/farsna/455182" target="_blank">📅 21:16 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455181">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1aba5bc2af.mp4?token=UU57yjVTPn-bYlRkNKnVBC_bU3dbU2cU8mvznysIUYh-d0cyY2RuDG4lLr_PFyo19mo-GeS0dUZ7qX4zaWY6hlx8G8XnbiJEzSALdWYhjCE3Ru3OgnpyKovFLThz9pQLQ9ZAs3etdO0Yi0Gd3qtCUNtFVqT8FrgDZtecxkVfa7f2mrEMWpqIAEZHmwBqC7q215ideaV5leRSkyvrFK3EHGDBKtTWr8YXQ8rbNjH1K1Yu0ow2gvuUgijUqH3nHaFD1PlzPqFY3iezwDQ31kHGqqw8uPVhjVBRc3I27IOcYSqgUVobixd2JgDcb7GjDi39r5AFBF6l99Wj-XeelO94kA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1aba5bc2af.mp4?token=UU57yjVTPn-bYlRkNKnVBC_bU3dbU2cU8mvznysIUYh-d0cyY2RuDG4lLr_PFyo19mo-GeS0dUZ7qX4zaWY6hlx8G8XnbiJEzSALdWYhjCE3Ru3OgnpyKovFLThz9pQLQ9ZAs3etdO0Yi0Gd3qtCUNtFVqT8FrgDZtecxkVfa7f2mrEMWpqIAEZHmwBqC7q215ideaV5leRSkyvrFK3EHGDBKtTWr8YXQ8rbNjH1K1Yu0ow2gvuUgijUqH3nHaFD1PlzPqFY3iezwDQ31kHGqqw8uPVhjVBRc3I27IOcYSqgUVobixd2JgDcb7GjDi39r5AFBF6l99Wj-XeelO94kA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خضریان: کلیات طرح اقدام راهبردی امنیت تنگهٔ هرمز در کمیسیون امنیت ملی تصویب شد
🔹
عضو کمیسیون امنیت ملی: با توجه به موقعیت راهبردی خلیج فارس و تنگهٔ هرمز و لزوم اعمال حاکمیت جمهوری اسلامی ایران به‌منظور پیشگیری از تکرار اقدامات خصمانه علیه ایران، کلیات طرح…</div>
<div class="tg-footer">👁️ 7.91K · <a href="https://t.me/farsna/455181" target="_blank">📅 21:15 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455180">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c44ea7008.mp4?token=tHwNMbCErM-ovttPr6y6vcdT20L5ktf8rSTs3LDI1KH-crN37V6NYoP4_AaLumXR9z4znj4JmA1hdxxgcV-I28iBkFxEKAe9neZdFbrJZw7gi0Yeb1QDlh7yKd9lOJpk136PB8gXcmfMLXmy_n1_P7MaH0ot-BSbtXVeSVF-Bvcf6HplmM9kBLoysXYS1vgusWLgkBgSHbn3YDowSe1CnmDzZjYxfs37fGm1i8dmEKTBAf2leCRTEVLg4Q6aj_cDhaKzmZ4PAFOS4dAUpB6F3Ep9Of-TnkHfmmSM9oPJ8QY9d5sbmYUVQv1M0SoircVMqxpX4MysKIUl2TB6fLEc3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c44ea7008.mp4?token=tHwNMbCErM-ovttPr6y6vcdT20L5ktf8rSTs3LDI1KH-crN37V6NYoP4_AaLumXR9z4znj4JmA1hdxxgcV-I28iBkFxEKAe9neZdFbrJZw7gi0Yeb1QDlh7yKd9lOJpk136PB8gXcmfMLXmy_n1_P7MaH0ot-BSbtXVeSVF-Bvcf6HplmM9kBLoysXYS1vgusWLgkBgSHbn3YDowSe1CnmDzZjYxfs37fGm1i8dmEKTBAf2leCRTEVLg4Q6aj_cDhaKzmZ4PAFOS4dAUpB6F3Ep9Of-TnkHfmmSM9oPJ8QY9d5sbmYUVQv1M0SoircVMqxpX4MysKIUl2TB6fLEc3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
افزایش اعتبار کالابرگ؛ از وعده تا اجرا
@Farsna</div>
<div class="tg-footer">👁️ 7.3K · <a href="https://t.me/farsna/455180" target="_blank">📅 21:11 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455179">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ax56nqeqd7RTTSMI3YAcCS3CV43xay7uHYWGeFNB0D4yZnYWtdP3jtbeYsVlJEqgIpxc3_Oe9uEe0cKgkfo7nafh_m0YSp4Rl4x80YaF6W67rfYbAWLxYFIlhYnB_ftS-eNoi5h_OjTq_WMU-aOoa9Sykt5MsFaOh4_OxcfcoOzT9BsrNfIShr3TFF-RTUPKgiuci3e7pOdlr9TtkJkeoc1ubeGOHljZ6qq9s1o_pyW3KwuoKib6YNDnlh6_il3F-3UMSOhBRxBOIltdULV4TkzR6tigzgRYdmnsqk69UKLHtA7vNxiJCTsiPgSMP_cEc0lmDXQzURa09GDIyYpDdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بمب نقل‌وانتقالاتی تراکتور عمل نکرد
⚽️
بعد از معرفی جواب نکونام به‌عنوان سرمربی تراکتور، شایعاتی پیرامون علاقۀ تی‌تی‌ها به جذب منیر الحدادی و توافق اولیه با این ستارۀ فصل گذشتۀ استقلال مطرح شده است.
⚽️
بااین‌حال پیگیری‌های خبرنگار فارس نشان می‌دهد این ستارۀ…</div>
<div class="tg-footer">👁️ 7.64K · <a href="https://t.me/farsna/455179" target="_blank">📅 21:06 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455178">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/372042832b.mp4?token=K9IT8ekcVGRU39b7DwuZaN8elnVLzaNEC89dFyCNU13Ot_IQ_SOpyFJy-OtnW_Phi--n3DVLn0XdXk4VZzibVyyP7qc4RmQfu_lU1Yn6bSN2WlJgzivYdkAGSkPG_arY8JKUNpyinYroUFnzdBc28veFZWYo_sTliC5y2hQg-DvXeUP0ul5l4UWQO5I0SzU0HwqxBazD2FxFRkYBxr4A6xCCg46Y5s4w_NYvHkhM1c5jBKv1D25aXcQL5pDgRrxhk01XftGL8Q4Bv0uQWi62e9wwIy8KWaqiICcU7OvTLAiVikOFfJX4SKRNAcs6_OJwdO61j7svmnEGySirLOn9Ew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/372042832b.mp4?token=K9IT8ekcVGRU39b7DwuZaN8elnVLzaNEC89dFyCNU13Ot_IQ_SOpyFJy-OtnW_Phi--n3DVLn0XdXk4VZzibVyyP7qc4RmQfu_lU1Yn6bSN2WlJgzivYdkAGSkPG_arY8JKUNpyinYroUFnzdBc28veFZWYo_sTliC5y2hQg-DvXeUP0ul5l4UWQO5I0SzU0HwqxBazD2FxFRkYBxr4A6xCCg46Y5s4w_NYvHkhM1c5jBKv1D25aXcQL5pDgRrxhk01XftGL8Q4Bv0uQWi62e9wwIy8KWaqiICcU7OvTLAiVikOFfJX4SKRNAcs6_OJwdO61j7svmnEGySirLOn9Ew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پاسخ روشن به ادعاهای بی‌اساس آمریکا
@Farsna</div>
<div class="tg-footer">👁️ 7.31K · <a href="https://t.me/farsna/455178" target="_blank">📅 20:57 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455177">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VDxR0nVL1kKG25JnXU1j0GAqmwJPB4ux3uApsz9dfutCtIvugTpjpMF8hLri12bMJ8pWkQIsvfg-8OBcMtf4IhtTaIgVnw77ma0phl_bKh5OeErAQK_cC2oec-dxgyYpvNWKtWwfBOFYNa77HL4hNefMVpa_xy-laVJDAWApNVjF3mXv_vvpA8RfV1BcMNgZsT4fddzfn7Nn90KDtnlMfFeNfPJ1Y1kA8klx6O9X1txzW0A9r2zKtfOZCyDxT3UXpMENZXCKBImkPTqBQHo7v6f7i8DA_4zUOq-BSuIQsBmhmQ8NJ_MfLtIXLENJoIbbOfLqclnuELwHuWqQBv9OUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنگ‌فرش خیابان‌های تاریخی برچیده می‌شود
🔹
طرح سنگ‌فرش کردن معابر در بافت مرکزی تهران، با هدف تبدیل این محدوده‌ها به پیاده‌راه و کاهش تردد خودروها، یکی از پروژه‌های بحث‌برانگیز مدیریت شهری در سال‌های اخیر بوده است.
🔹
حالا آقامیری، رئیس کمیتۀ عمران شورای شهر…</div>
<div class="tg-footer">👁️ 8.29K · <a href="https://t.me/farsna/455177" target="_blank">📅 20:46 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455176">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aISWlH01VcyjnLXIwGALCGPAFcfL6PJYMoCPeOZ8IkxysgknS-tfr2wr5D5KPwABx9HeMRtQQ5_kOCHy1tJ-999Zk27krIXmgaLZzd8nDhcD3bfwL3WXqJnCD2tRTZeIziOzxZkvVYnRRQ3LSW0j4BxKHCI5lv39JiNkrp_XOBctjF3UOE1sMmoHRRuUEml4HFnaOPP8ez7f3WN2qh4JU7G1UEFmammrrmGQJf8WOYRJPWkrcue2ctvleoU1b47bsLzzddUW8wtL1oXIE2tifVVQh9u8UlAz5tZfHShdO69NpxzlgI2Z9jyutNQyxqVzMN-Hnl1UJk1lQRns-HVpag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حزب‌الله: دولت لبنان در برابر نقشه الحاق سکوت نکند
🔹
حزب‌الله در بیانیه‌ای اعلام کرد که ورود رژیم صهیونیستی به مذاکرات مستقیم با هیات حاکمه لبنان چیزی جز تلاشی آشکار برای وقت‌کشی و تحمیل واقعیت‌های جدید در میدان نیست.
🔹
هیئت حاکمۀ لبنان مسئول وضعیت کنونی است و باید با بازنگری در سیاست خود، مسیر امتیازدهی و مذاکرات مستقیم با دشمن را متوقف کند.
🔹
همچنین ضروری است در تمامی سطوح، از دولت گرفته تا شورای عالی دفاع، اقدام فوری صورت گیرد و جلسه‌ای اضطراری برای مقابله با این موضوع خطرناک و ارائه شکایت فوری به شورای امنیت سازمان ملل متحد تشکیل شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.97K · <a href="https://t.me/farsna/455176" target="_blank">📅 20:45 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455174">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lTrlSlPjMRYVwgricftIw2sZxIZT0lRTgcbkXIUkilv-WJpAsLriPGYRPt8mDt8G2Cu25r4eXPkJ971vu3iqaTmfihB3uuRJdIVnRu5n6T8_4IDyzBX3V-hTCF7pfWeQqAsccLHqteNKI3P1-ZVELnFiTeT5zq2EAQ3FHG1edalb84puRYXgodgrR2uMFvc8cwaN5tHrKG87r5a--aGVDxzv8WYNccY-xZVB9s2XoApzsXZf0V4t9ltQSokRTTMlpiG_N4xoksZaqxlaMVTg0LNKaHlqLY8FxSADxpgGOZVKOqdPXzRqi6qT0raHPOkrb7sSUlTrrjtraB19h8p7vQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
حضرت آیت‌الله سیدمجتبی خامنه‌ای در حکمی محسن رضایی را به‌عنوان نماینده خود در شورای‌عالی امنیت ملی منصوب کردند
متن حکم رهبر معظم انقلاب اسلامی به این شرح است:
بسم الله الرحمن الرحیم
برادر گرامی جناب آقای دکتر محسن رضایی
🔹
با توجه به تجارب ارزشمندتان بدین‌وسیله جناب‌عالی را که از پیشگامان دوره‌ی پرافتخار هشت سال دفاع مقدس هستید، به‌عنوان نماینده خود در شورای عالی امنیت ملی منصوب می‌کنم. امیدوارم در انجام این مسئولیت مهم، کمال موفقیت را کسب نمایید.
🔹
ضمناً از تلاش شبانه‌روزی برادر عزیز جناب آقای دکتر محمدباقر ذوالقدر تشکر می‌شود.
🔹
إن‌شاء‌الله تحت توجهات سرورمان حضرت بقیة‌الله‌الاعظم عجل الله تعالی فرجه الشریف همواره سربازی مجاهد برای ملت سرافراز ایران باشید.
@Farsna</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/455174" target="_blank">📅 20:30 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455173">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e6c72983f7.mp4?token=ZPX_W6UftlNYjOHstk2tt7T55Z06rV2U3EW1MeysZpTvkiWJGE7gm6Sk5MFvYDWjj76GlJz08cFHa9uGzUAhTBZUg4l891ZMxIU0ImQ33a8aeacGuz7OL80nAV2dFCuAR9B6_u1YwLwTG1nKd7-gtL2tgVPMGqgflL1W03zMUUULsErRvRODtNTzXLBGh7EPuGtKksZZXaj1kIgAp1CeSs6QvXrLNccn8OScwSWIJMARfc0VGm1eIt7a-QbLMyN1VO4as-3ka6fE0SYFAweUzqskPF5aDql76KLfj5QHCl1FpBpl55nV81kZSmsGLY3P2iDGGwu4udWcNNuqq6200JJYEbDUKeWkeA_8B6-36JfOgg8skNsYm7eU7KIwEEFEZmXEKzkQXGjajFi_t3z69nHMHQViZ4ViLJGJizKXZhMXgtkCVbGeS4ktIxtHTA7o9SAkhFwqbSD7cyipbL9bkULqZ8bFIjsypWPq3kemvQzn36IZV0jOvcZmiUSDace2oqZ9LPpmvKKSkani4O70LKg9zb4Ze_otStNZ80fCmlU8w8fP9cquJLMjSPui3dvYEY-uBuoal8K3fB5ca8gh-e7U1ewHU7O9G2wmTQUGpoe8GuM285HQ05y9BN0e0QOencvbTC6IpGM_fPjeGHefnxqdEyt0G9TCh8DATh7z5is" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e6c72983f7.mp4?token=ZPX_W6UftlNYjOHstk2tt7T55Z06rV2U3EW1MeysZpTvkiWJGE7gm6Sk5MFvYDWjj76GlJz08cFHa9uGzUAhTBZUg4l891ZMxIU0ImQ33a8aeacGuz7OL80nAV2dFCuAR9B6_u1YwLwTG1nKd7-gtL2tgVPMGqgflL1W03zMUUULsErRvRODtNTzXLBGh7EPuGtKksZZXaj1kIgAp1CeSs6QvXrLNccn8OScwSWIJMARfc0VGm1eIt7a-QbLMyN1VO4as-3ka6fE0SYFAweUzqskPF5aDql76KLfj5QHCl1FpBpl55nV81kZSmsGLY3P2iDGGwu4udWcNNuqq6200JJYEbDUKeWkeA_8B6-36JfOgg8skNsYm7eU7KIwEEFEZmXEKzkQXGjajFi_t3z69nHMHQViZ4ViLJGJizKXZhMXgtkCVbGeS4ktIxtHTA7o9SAkhFwqbSD7cyipbL9bkULqZ8bFIjsypWPq3kemvQzn36IZV0jOvcZmiUSDace2oqZ9LPpmvKKSkani4O70LKg9zb4Ze_otStNZ80fCmlU8w8fP9cquJLMjSPui3dvYEY-uBuoal8K3fB5ca8gh-e7U1ewHU7O9G2wmTQUGpoe8GuM285HQ05y9BN0e0QOencvbTC6IpGM_fPjeGHefnxqdEyt0G9TCh8DATh7z5is" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مدافعان حرم و درخشش جهان‌نگری انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 8.64K · <a href="https://t.me/farsna/455173" target="_blank">📅 20:28 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455172">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XCqVMFdIVOkMzJvG69p70-Mb5DmzSKW_l21ittynQYDDSLXDS8YFglf4J-3AGKK9aAVDrGDrGz-wBzQDspcNCi3_FMjkhPOU39WpWxX3HzB6f9y1eE2Xfv9jxlYINZYUGuAXHdjJGIJpd7eH_S1FyAqVnH_VEh2yBINMr_-4QKea7hz0RNItJHaPXdiDKcdJW_CTUUmpyzi7QnHdIJGe55sUhNEtd-7lFd8Jg-dCVK9gV5R91kjvQdMhZK7Qfn3xlvoxc0-3NL1IdDsBfD0oUcDRSn-RmCD35T_PZrb9C28pMvO1TRm8GY_NpPKUmoL1LivSIcxv0BdMNxFVoHZuyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بمب نقل‌وانتقالاتی تراکتور عمل نکرد
⚽️
بعد از معرفی جواب نکونام به‌عنوان سرمربی تراکتور، شایعاتی پیرامون علاقۀ تی‌تی‌ها به جذب منیر الحدادی و توافق اولیه با این ستارۀ فصل گذشتۀ استقلال مطرح شده است.
⚽️
بااین‌حال پیگیری‌های خبرنگار فارس نشان می‌دهد این ستارۀ مراکشی ازآنجایی‌که به دلیل شرایط ویژه منطقه از استقلال جدا شده، برنامه‌ای برای بازگشت به ایران ندارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.3K · <a href="https://t.me/farsna/455172" target="_blank">📅 20:25 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455171">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6dd0280352.mp4?token=XZJVOJQwvPFcorNpHIDtaDP-X7AGmzUW9nJ_2oHpNAKSHAljsuIKOviJtmm9RiDsAtWIVsJOCUtEfHBOVndGP95ipf1IlLm02qUuB7eaM3S27NB2y8R3bg1375c8u7Akhu6IxDSdWPc7ezjUUJ5E6aJ_tFjAozXIfOtjBDvCQBKzEnYivh0jYmLvb941xr8BYbp4UiS2mZ3_wXElcxpHtm-ZxPytV60lahu2_YwYSTpqJQEbG3gS9_62Hu5eUOcwna_ELMEAeDRj6sXOgLeI9DxiSBwJ8w_9JMZZBZbzWOOkNcGwCX91xwz1zQ2PwoGdaChQJByRuuovc677dD6LLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6dd0280352.mp4?token=XZJVOJQwvPFcorNpHIDtaDP-X7AGmzUW9nJ_2oHpNAKSHAljsuIKOviJtmm9RiDsAtWIVsJOCUtEfHBOVndGP95ipf1IlLm02qUuB7eaM3S27NB2y8R3bg1375c8u7Akhu6IxDSdWPc7ezjUUJ5E6aJ_tFjAozXIfOtjBDvCQBKzEnYivh0jYmLvb941xr8BYbp4UiS2mZ3_wXElcxpHtm-ZxPytV60lahu2_YwYSTpqJQEbG3gS9_62Hu5eUOcwna_ELMEAeDRj6sXOgLeI9DxiSBwJ8w_9JMZZBZbzWOOkNcGwCX91xwz1zQ2PwoGdaChQJByRuuovc677dD6LLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حجت‌الاسلام عابدینی در برنامۀ سمت خدا: بازسازی کشور احتیاج به حضور پررنگ مردم دارد
🔹
از حالا باید برای این حضور مردم طرح‌ریزی انجام شد.
@Farsna</div>
<div class="tg-footer">👁️ 9.01K · <a href="https://t.me/farsna/455171" target="_blank">📅 20:17 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455170">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jPx5B4fpR4Z3ZPxo6fxsmE3dNuTVvsg-jnecfeDcvx4EHHMzrR4_WevnlogWO7AAJR56K7ZsCxXdKacK_CL6oBgxoe9jA-WKTeRGCx_Knehm53kTypFZ-z_i4CYOXw-He0cPSrJW0tQnkCL3fGhpu3OJZDOV1nrizlPLCZvE2d25JujD_uErMD7snvyWBHTVO15fVXvbBtSR_fIUbBvUSsqCMbsMtzqcb-0NjT5kHciacUyADwP4G4t4HDLXgvidBoUym_7qLQr73YW3ufB0hXtRTFg9OEEqf48lQyEhtStuM_ZYcoW4l2vHZdRm1rksUjxoqm6VJ1b60bzarQKM3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عضو کنگرۀ آمریکا: به‌خاطر جنگ با ایران، نه‌فقط بنزین بلکه همه‌چیز گران می‌شود
🔹
الکساندریا کورتز: من فکر می‌کنم که مردم عادی آمریکا شکاف بسیار بزرگی که میان حرف‌ها و عملکرد دونالد ترامپ می‌بینند.
🔹
آن‌چه ما دیده‌ایم سیاست‌های ترامپ، منجر به افزایش قیمت‌ها می‌شود؛ نه فقط در پمپ بنزین‌ها بلکه در هر چیزی که شما می‌خرید.
🔹
ترامپ بدون هیچ دلیل و منطقی و بدون مجوز کنگره جنگی بزرگ به راه انداخته که خطرات بسیار بالا و پیامدهای فاجعه‌باری دارد.
🔹
هر روز که این وضعیت ادامه پیدا کند خطرات و دامنۀ این جنایت برای کشور و تمام جهان بیشتر می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.09K · <a href="https://t.me/farsna/455170" target="_blank">📅 20:08 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455169">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/441a65f11d.mp4?token=hmCBUgBZvTdQpgUWMdvN7Eduaj_oGfwoDDHXeD1vnOAa0wXM8LRd0clvRyFDCIuTSCJrxZNuyhGl1FtccW65z-tSeiOVSN57UrSU81uONtANPgo3vggdMTBwCBbo6eawIC2kFk9OOXh3l-P5aGpSAY0A0PSCiy6Ts_-5kha7Ylb5oeJ4kQkVTLrkBFyFFSrlOckRG70YWmbNPerrH5R9F6SoLjWE-Vi3caGo1ECefLgVQH3WLA6Hr2GMZazuLpqfQF48ixVSM2kh6TdNbt41cXXH4lsN_2-VWzlgwm8Iz3EueADVUkLg3quUoBfpKolx8Dk1CwNbPlw4FbqwpT8g9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/441a65f11d.mp4?token=hmCBUgBZvTdQpgUWMdvN7Eduaj_oGfwoDDHXeD1vnOAa0wXM8LRd0clvRyFDCIuTSCJrxZNuyhGl1FtccW65z-tSeiOVSN57UrSU81uONtANPgo3vggdMTBwCBbo6eawIC2kFk9OOXh3l-P5aGpSAY0A0PSCiy6Ts_-5kha7Ylb5oeJ4kQkVTLrkBFyFFSrlOckRG70YWmbNPerrH5R9F6SoLjWE-Vi3caGo1ECefLgVQH3WLA6Hr2GMZazuLpqfQF48ixVSM2kh6TdNbt41cXXH4lsN_2-VWzlgwm8Iz3EueADVUkLg3quUoBfpKolx8Dk1CwNbPlw4FbqwpT8g9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: افغانستان و پاکستان نگذاشتند تروریست‌ها و تجزیه‌طلبان از خاکشان وارد ایران شوند.  @Farsna</div>
<div class="tg-footer">👁️ 7.73K · <a href="https://t.me/farsna/455169" target="_blank">📅 20:03 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455163">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ieal6VSOIkv0Xf4suFSt0RdI-apXoufXJCtLwL_m2V6AyhC66Lw7uOeYNR73EgapPIGoJPdHDbDfamk4tcAyEYgX3AtUs4rYtVmhypODX4xKiBweVOpzJLXQgfW1GUS-30RoQwlBXlnkJwHjGAOo3N_S5DS5xKwUsDGH0qWrphfti8yJDSQmagersZqou3kyCJFc0-MAjWX1F9WHZLLQ1dVk1S3a4wpF7nQRqrC1qX9cR5rbaFJ0RdQkZD6zrMc0pBmMfMVrwtUwtLn8voLN98ZODhGFH16cUlI6ihLqAk68mCG9_1Imw0PaeSeXS81Wa9_Qg1AsVg2MbYI8CizBuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y0zBaTAYA1tQnMSXlndWhSQADAd93iNAJjKuKWbk6gAARtM0EeNxG-1NLkgNiiTja2JhYViyAYB97uDET8qzMloG6rh5nUZj3CV4Ffc2nkwKrxtDHFOdJWR9rcXZWIOiBDNnUtCzHrIpL4fZocBVjliUE-CyhhaMqHSUwbda2VCK7GNxAsxZaqa4WAcx7CWPpO8_exLs_A2qMl6vmghhQZVDrVMAvEJ1-LeQtFlxU8YQ54eDzkcFsM8Fi5se8B0CS0acfXMQyfEUMWYr03v-gYNgzk1qr4KPtSYpVb6CgkKS8MCFTAiVeyMcBTxMGZTdpnn1Xy0Fb1Go9xE4xsr1eQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/llIo18UuFUw22m8cXq6pyyylHgFArR4vM-Z9HlKDumFd71I10-hb4stf7yIWy5uEr2goK3-MLAV_e04x05brOsWoeqjf3b1B8Vh87PAZ4gVjaq6rMp4COey56VxQfRF1MX0VKmam6GXtiJ8CuBA08nBooZ7oARViF0e14055OaXOB8QUiE-o-lC709NU3bXtnix3MHjTXo7mtHUh1q74_B-0aKXyts3doSj86lx7r_2YL33oKYFSwH4HTh4oDyIWMjJaQQbS6X8pQJpFI2KL0ZWhtRR2VdR0uBiGfwZ_qER2WEsqAyXaJuYZC0UffM8_qZtvc3MKpJgpK9MWpqpwlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MEdvI4Gta703M_PTa6bIrqjV1UT6Pe1SpKzIVy9Bb8Y9pfukeY-5qJZjC7mtTTwggJ_tBPqkaIeGzes2REGivcJuVoQvmbEb6OTMaRj9L5vSDV5oHateS-6RsmwGaEEpqFLZrW2uHqvnWniV0iFKnx-yBQlZakUu9C8-DSAoKE9lxravQ8I-QTiNg2OBuMaB7mgevp-ucLZG7Oqy6RUPgdhNaDrCszsN53y3nO-g0mNEtGzRQPjeBVqD9SRCfO7yb0NjfZ32ARHwsLQUNgI06-zHmA9wJTeOBmJOr1-eK3fl_wiZgO-lHQxZEMxkp8hYy6P-5gFv2wZ-hpXCT6lTzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aqZhK4z9JS8KGXBhbshCBsbCQ1f1p_0kYDMFUKHtGVHcqxiiP1wombWkDOeWKl0fxwnu2DiCY4rQVmXvmZtIMPZux9W_IZ_E2fuzvSxZbGGJUwiwL9Ru0V5WeK8ewPEuxaNUwfwvChQVSxsIzl0QJ6MsTAbfv3eKjpmJNEXgks3mEPt--XUmE3zTPOb4ajzBOh9Mft6nLkkGalw9zYegJfa4DBObe_axBRsgj5nAmN3-l6epIH2L3NpdJBI01sLARPgy1Dk6J2bq5NnFlDLQpeaOED6r4kEHcCnPjI2O4o0ublvVGsljac66btLZT3oZl6zRoYF-zPcYRbx8dLoQ8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JnRoH6z25V5Egb3RVm0FqVoGOcc9t4kHhI8IiWRO_6sDaIF5Gl2uqe9bnx_4Hq21AL77l-6ajSjNj2KD3z-7N_MtrN_YujQXBpZcYBvrwpmqChLay5N9f-v-JZQ3-aS3l36cxsVvcDpyk54rw59953pQCyMTFXh2ONe6cER8TMQkiai8lBLpzrFKP5tAN4oPK1myX992IAcp7HNqPhgZsWyGNRwqBAKIBrczxnTu1KAS2FOsGpwK-gcP5c3Ti9vRtb6W1BgqtOMvIlKw0Ju4WlaQBZUvRjfsH2cE1FuNkJkVo_FTviM3Caap7AsGpNZOuNWXiNvZ5ebvxRoq2YpPvw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
بازدید حجت‌الاسلام موسوی‌مقدم، نماینده ولی‌فقیه در بنیاد شهید، از خبرگزاری فارس
عکس:
میثم نهاوندی
@Farsna</div>
<div class="tg-footer">👁️ 8.44K · <a href="https://t.me/farsna/455163" target="_blank">📅 19:57 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455162">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31a5d6e71f.mp4?token=sOPC5Bg04ZDuh_MQxQmIpa4--G0mcpj7y34Rq4UcQpM0EM1ikj6bwtvP2jj6BWOxpX3gW7OgfP4lIegHzqvAR0Lpgez-4y9Ratp2_ohF3cbNh2c6rl55hKg4UIwxsNTtDmTzjyIXZQPP6Z2l1PkJbdhlZtALAepaomJHFRb05PaN6dLEa8fShNoC_g19_3SQuR6BDxPv4nqcqa8QunZHeEieX12TEK53-bKb7JVHLfwl-x597ip61IcLTNllPymHgLNEdnjMaOv1H3AE3kIYeHGTJ2VUUpGFzjKPiNSNvP7nNF5Fpgx5wvkS0y2kB-Nnwx4D6XLq_Y-D59kr3FuCLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31a5d6e71f.mp4?token=sOPC5Bg04ZDuh_MQxQmIpa4--G0mcpj7y34Rq4UcQpM0EM1ikj6bwtvP2jj6BWOxpX3gW7OgfP4lIegHzqvAR0Lpgez-4y9Ratp2_ohF3cbNh2c6rl55hKg4UIwxsNTtDmTzjyIXZQPP6Z2l1PkJbdhlZtALAepaomJHFRb05PaN6dLEa8fShNoC_g19_3SQuR6BDxPv4nqcqa8QunZHeEieX12TEK53-bKb7JVHLfwl-x597ip61IcLTNllPymHgLNEdnjMaOv1H3AE3kIYeHGTJ2VUUpGFzjKPiNSNvP7nNF5Fpgx5wvkS0y2kB-Nnwx4D6XLq_Y-D59kr3FuCLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: باوجود پیچیدگی دیپلماسی پس‌از جنگ، ارتباط مطلوبی با کشورهای منطقه داریم  @Farsna</div>
<div class="tg-footer">👁️ 8.19K · <a href="https://t.me/farsna/455162" target="_blank">📅 19:52 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455160">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38c87c18ff.mp4?token=pEDc2Wo649RMEgd7LS7UdW_JNvgJnnSqthFGsVhjAxU2eFQcFTFOrQt5aAHf6Zr1vbElvXhaxu-3G37Rz4oVsvMgMZfL9JAq0mHvVlHsb95nlYV9405wIVgm6Pt8GkX5fceQfjG2aTBWSge_7XmLZCIsUR63u3_pBGwLZlpSBCfKvovR8lTV1I_at0fgMsI7TajHYwCljKehPlF9Mz735rIETGLR6YmCrjxykUF3QiJqfTcTZHXJ2YF6g9JXQ8jLafInrcZ0NYfs1hNnIYOXrwu36-7WaTxYlpEb0z2bQZXPw5FYBG_C6yM6ih5R1dYqBNA1aqMeXq6Ia0o3svJakQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38c87c18ff.mp4?token=pEDc2Wo649RMEgd7LS7UdW_JNvgJnnSqthFGsVhjAxU2eFQcFTFOrQt5aAHf6Zr1vbElvXhaxu-3G37Rz4oVsvMgMZfL9JAq0mHvVlHsb95nlYV9405wIVgm6Pt8GkX5fceQfjG2aTBWSge_7XmLZCIsUR63u3_pBGwLZlpSBCfKvovR8lTV1I_at0fgMsI7TajHYwCljKehPlF9Mz735rIETGLR6YmCrjxykUF3QiJqfTcTZHXJ2YF6g9JXQ8jLafInrcZ0NYfs1hNnIYOXrwu36-7WaTxYlpEb0z2bQZXPw5FYBG_C6yM6ih5R1dYqBNA1aqMeXq6Ia0o3svJakQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: باوجود پیچیدگی دیپلماسی پس‌از جنگ، ارتباط مطلوبی با کشورهای منطقه داریم
@Farsna</div>
<div class="tg-footer">👁️ 8.56K · <a href="https://t.me/farsna/455160" target="_blank">📅 19:44 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455159">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r0mvIz1JW9O0QuXUX3BJSDu58sjU0ccFmGa2lA-dZFbkmOpaU4AWvlYr64pYK6_i27nygHTaX2SIksFD9_nVM1ZM5TN3XOWvu2IDEorQuTsOXh_ZQ1FWsJG7Tp0heCpbnVbHvleTsfKPul0VOI38uJ1fVhT0VJMm0ckPXjKPWpIDwoq-lITmiFahU6Ej3Z6V3VcoFWYoRkZ-iUGUelYYBpl1eyZbuTuM2S827QNFtZmVsVI7Dv7ue_LG93o0-vS2J4Cn12k6hPnsIa7g1Ai8wHEUlo1ZFVCnF0FSS-yS5mJtWjizYGQwxOUAf7AY8HljZ73ZhTeMDllVYwtu_1GdwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بی‌برقی، سهم مردم ونزوئلا از پیروزی بزرگ ترامپ
🔹
قطعی‌های مکرر برق، پایتخت ونزوئلا را برای نخستین بار در هفت سال گذشته در تاریکی فرو برده و مردم دست به تجمع و اعتراض زده‌اند.
🔹
ترامپ یک ماه پیش باز هم مقابل دوربین گفت که ما خیلی از ونزوئلا پول درمی‌آوریم و این «حق ماست که این را داشته باشیم».
🔹
حالا فایننشال تایمز می‌گوید که واشنگتن از فروش نفت این کشور چیزی حدود ۱۳ میلیارد دلار درآمد کسب کرده است اما باوجود وعده‌های دولت مورد حمایت آمریکا در این کشور و واشنگتن، صدای نارضایتی مردم بلند شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.76K · <a href="https://t.me/farsna/455159" target="_blank">📅 19:33 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455158">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tC47ZJlgX-jXobWGLdKAjbgOI85x_8pqjpS47Ke9eZPjzYmeQJyfU3svFvb-IS4Y5m3bUsQ-V90kwdTewUDXmQ-TsxmRHEwfcs0GtuZmxejXR0rrSBR_90AvXwQlSxjli3aQfjlZcjlv825rOsv9oDVW5ZFOdwyNHaG6grRcbWMylOW3eNGDXXydM02YDxh7-4H2Gag9KPd-ZF9JD4Nia1nTBJlRdcXRyZ8u0myv3uZssFMLol7NL8THxC_muljKHyIVXMWhIaRrAdKWkUsjKewntWCZeSgnvwUbpDAsslfxFcSQRX6aSSlP8ESFK_x9wo0arQOhYJ3hRgh0t4W2Xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دریاچهٔ ارومیه جان گرفت
🔹
شرکت آب منطقه‌ای آذربایجان‌شرقی: حجم آب ورودی به دریاچهٔ ارومیه از ۴.۵ میلیارد مترمکعب در سال آبی جاری عبور کرد؛ این میزان، بالاتر از حقابهٔ تعیین‌شده برای دریاچه بوده و بیانگر بهبود شرایط آبی این پهنه نسبت به سال‌های گذشته است. …</div>
<div class="tg-footer">👁️ 8.38K · <a href="https://t.me/farsna/455158" target="_blank">📅 19:32 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455157">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f85c2b1087.mp4?token=gN5BpD2yjRVX4khkeycqBz_7HWwn90v0lHg7ZcmpaXP6Ija1Ox4gwG3z9zMhGF35UVIYcBHNXhAPv_hp0xi_hkndFa6MIl6Fcotny1hngry0n9NRvJeYyje5PIbLrojl1U6b6TCyibMg2ZOKch12aoiaRYD8AbPBkk_50P79FGFWSSQg6voAd5wxBWYfQ3tBRbYaIdh6ecaQGD-8z0bGfi4UtfRkDVvj8998amI2Avd_wTUmt98nNr_SEc1WG0LMwp3AMlo1hhwyqjfSmjO55nGSXPFgHN6B8RXK6NY9OjuoAKrb_2GWyVfAej66iHKf2DNMiOSItjYr1U1a6lmgUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f85c2b1087.mp4?token=gN5BpD2yjRVX4khkeycqBz_7HWwn90v0lHg7ZcmpaXP6Ija1Ox4gwG3z9zMhGF35UVIYcBHNXhAPv_hp0xi_hkndFa6MIl6Fcotny1hngry0n9NRvJeYyje5PIbLrojl1U6b6TCyibMg2ZOKch12aoiaRYD8AbPBkk_50P79FGFWSSQg6voAd5wxBWYfQ3tBRbYaIdh6ecaQGD-8z0bGfi4UtfRkDVvj8998amI2Avd_wTUmt98nNr_SEc1WG0LMwp3AMlo1hhwyqjfSmjO55nGSXPFgHN6B8RXK6NY9OjuoAKrb_2GWyVfAej66iHKf2DNMiOSItjYr1U1a6lmgUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مجری آمریکایی به یک اسرائیلی: دیگر نمی‌شود از شما دفاع کرد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.48K · <a href="https://t.me/farsna/455157" target="_blank">📅 19:21 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455156">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4fbbd8f7d2.mp4?token=DjJJUrR1-92LauQw8gHpVzJDrcKI7SM9IHPN_ULNC6NHv9hJM-HMV6FhyKJrhbMIoXAZJAQq7Sbv2W7f0cMTr5mWR2FBDAPJSZCbNOL2-NCbO6jtF8aMTx_A0BCHb8UZymR9rEYu3UD3qpuNn-xRYfgk6p3KDZ1GzCb_dTlfq7LjeiUc_jvChPY4uL4AiJ0WrPSbgZIH39AgR5r8p4sl0tCQ9dLuBP1pBC6s7SRt3g-rvSnZC5nvJU-PCeDJF2-nlLnvIrJsDF5odV-6IpfZ-CbEkPTsBJbszdxm2c6gOBylu1lelGPc5lhLAP-h5XlgkQSnKd3V3KFXx40oIluauQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4fbbd8f7d2.mp4?token=DjJJUrR1-92LauQw8gHpVzJDrcKI7SM9IHPN_ULNC6NHv9hJM-HMV6FhyKJrhbMIoXAZJAQq7Sbv2W7f0cMTr5mWR2FBDAPJSZCbNOL2-NCbO6jtF8aMTx_A0BCHb8UZymR9rEYu3UD3qpuNn-xRYfgk6p3KDZ1GzCb_dTlfq7LjeiUc_jvChPY4uL4AiJ0WrPSbgZIH39AgR5r8p4sl0tCQ9dLuBP1pBC6s7SRt3g-rvSnZC5nvJU-PCeDJF2-nlLnvIrJsDF5odV-6IpfZ-CbEkPTsBJbszdxm2c6gOBylu1lelGPc5lhLAP-h5XlgkQSnKd3V3KFXx40oIluauQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
منابع سعودی: انصارالله یمن با ۳۰ موشک مواضعی در بندر المخا را هدف قرارداد.  @Farsna</div>
<div class="tg-footer">👁️ 9.15K · <a href="https://t.me/farsna/455156" target="_blank">📅 18:59 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455155">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80c2022554.mp4?token=Zwbq_fh2v6PWF9KFB9OzcgZfNglFbsh9_B0toyt4fwADF1zOdLMjdaF2f6xmxonRgdk9C-htI4CsNP2HqVVKnEoRFu82n4b92LbBaQztBwXTaT0mfsy5DE2TV7Nut6ZGZUGOiwWd1ZDwZrf8dUSFCMiXiB30GP3K3weDSc9DWvQHzGVlGXG0cdQoz_3DvwzQs2yeW2Lj7cjcuiWpHi42tEBX8rTrkAMnrpFwzAJ7A-Dsk2ueSSMMMWFIZ8mOU-FZPlVIPZ6W0FQbq90Wh5krvKl6YcisRTRQWFMZWXY19dyrrSfa67blExwOLJstMr3jrtA5qVmGYSKNikC_CMcoJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80c2022554.mp4?token=Zwbq_fh2v6PWF9KFB9OzcgZfNglFbsh9_B0toyt4fwADF1zOdLMjdaF2f6xmxonRgdk9C-htI4CsNP2HqVVKnEoRFu82n4b92LbBaQztBwXTaT0mfsy5DE2TV7Nut6ZGZUGOiwWd1ZDwZrf8dUSFCMiXiB30GP3K3weDSc9DWvQHzGVlGXG0cdQoz_3DvwzQs2yeW2Lj7cjcuiWpHi42tEBX8rTrkAMnrpFwzAJ7A-Dsk2ueSSMMMWFIZ8mOU-FZPlVIPZ6W0FQbq90Wh5krvKl6YcisRTRQWFMZWXY19dyrrSfa67blExwOLJstMr3jrtA5qVmGYSKNikC_CMcoJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پایان یکه‌تازی آمریکا در صنعت هوش مصنوعی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.13K · <a href="https://t.me/farsna/455155" target="_blank">📅 18:53 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455154">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">‌ سخنگوی فراجا: در پروندۀ قتل رجب‌زاده تاکنون ۵ نفر دستگیر شده‌اند
🔹
سردار منتظرالمهدی: در پروندهٔ حمیدرضا رجب‌زاده تاکنون ۴ مرد و یک زن دستگیر شده‌اند که یکی از آن‌ها عنصر اصلی دخیل در قتل بوده است.
🔸
حمیدرضا رجب‌زاده حدود ۱۵ روز پیش ناپدید شده بود اما ۴…</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/455154" target="_blank">📅 18:37 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455153">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🔴
منابع سعودی: انصارالله یمن با ۳۰ موشک مواضعی در بندر المخا را هدف قرارداد.
@Farsna</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/455153" target="_blank">📅 18:35 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455152">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6ca6e5f69.mp4?token=YSJg0vaW-agmDKxIkHihIZDoPuUwF0wn1dcZEX6J5bssm7hxJk81rEcagtbAA4PHOAeV4DG2CCKzYP_fvumiT0x-N5wEJmgKW8W4I4XBxgfPGJTkNkpnZYuQj3C2F-za6pRfHRlUPP3BA0q5Ff6q6faJ6vtVNEaaGiK7_fgvDp_b0pLXMMdYt2exF-qZ9CHMGJH3W6CYiUlNQwwM4MpHnikLAzsyt2ckkNhlt1h_Pjd7NGgIhReCTHiM6VwWf4S_gJOO1KHnZ93PzF9TPsLbBIZKbzWXtDjh88Ow7r-n8t_I0xO7vBEQ7KZQu4m2p6BTqtJe_xIonSpgtr-4h4QDIocHcIrKGMPbXutWGdCY5bG_I6zxbmSW3j8BUEe4LC-1EtiWdsJW5-xNc3U4Fd6RnY27IwWSuptBGWqEjjsrrii8ZD8x9wQrAdz1PJJ3PFO5X17EVdK8geA1AYqCxGrUT3FeChzuVMyUIu6Ztm-23IPCgf6DyI9Mewqk1BSUmtJBCxrWH8Y4pLQE4D2QC3WNg0CG0wpHgkgImIRVAfRGNrwU3fZRVGgqQhQXvOgKlMzAKIXtLznxODhR0yrxt-An7XsaPdTwReNxI-tDS6m4VU-g8zqHghyMYzUwvLOTE9y4wE1Kx7rYc6FszIG65oPE4o9cJAGqq_dg9KyjbXdW2cU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6ca6e5f69.mp4?token=YSJg0vaW-agmDKxIkHihIZDoPuUwF0wn1dcZEX6J5bssm7hxJk81rEcagtbAA4PHOAeV4DG2CCKzYP_fvumiT0x-N5wEJmgKW8W4I4XBxgfPGJTkNkpnZYuQj3C2F-za6pRfHRlUPP3BA0q5Ff6q6faJ6vtVNEaaGiK7_fgvDp_b0pLXMMdYt2exF-qZ9CHMGJH3W6CYiUlNQwwM4MpHnikLAzsyt2ckkNhlt1h_Pjd7NGgIhReCTHiM6VwWf4S_gJOO1KHnZ93PzF9TPsLbBIZKbzWXtDjh88Ow7r-n8t_I0xO7vBEQ7KZQu4m2p6BTqtJe_xIonSpgtr-4h4QDIocHcIrKGMPbXutWGdCY5bG_I6zxbmSW3j8BUEe4LC-1EtiWdsJW5-xNc3U4Fd6RnY27IwWSuptBGWqEjjsrrii8ZD8x9wQrAdz1PJJ3PFO5X17EVdK8geA1AYqCxGrUT3FeChzuVMyUIu6Ztm-23IPCgf6DyI9Mewqk1BSUmtJBCxrWH8Y4pLQE4D2QC3WNg0CG0wpHgkgImIRVAfRGNrwU3fZRVGgqQhQXvOgKlMzAKIXtLznxODhR0yrxt-An7XsaPdTwReNxI-tDS6m4VU-g8zqHghyMYzUwvLOTE9y4wE1Kx7rYc6FszIG65oPE4o9cJAGqq_dg9KyjbXdW2cU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصاویری از شکوه طبیعت در زیست‌بوم زاگرس
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/455152" target="_blank">📅 18:13 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455151">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XWA8jVm6nz2tJ6zIriQQs-lSIbp0ZBJeA7IszYpHrB9Mdn5fvvOiH8QcbT90YLVOSMD7y40AQDBED-ovYrh7Pp1YLgSp0NMdDaLnLexavmY3WflxeCxM_JJWBGsL_1vJ1vWERaj-76fXTEcqcoIJxy0vh0LORPzvuRnU87KBbz9_51fKRaL_qGQ3UrjnuNfJwuQrMAXc2xYIRXzshZJSUOnI9Ir9Sxi_tkLUle6EdlJf-EI3E-c3SNERNPELuS21cHka35ebwJu8YROyq48wfVDXnRaEo4PWj3N4QAiCZvdniQYmxuNj8DPkyDsgoUtYbUW-2NWX2MiOsGSKTL9kXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جزئیات متن اولیۀ طرح راهبردی مدیریت تنگه هرمز
🔹
سلیمی، عضو هیئت‌رئیسه مجلس: متن اولیۀ طرح «اقدام راهبردی تأمین امنیت و پیشرفت پایدار تنگۀ هرمز و خلیج‌فارس» در کمیسیون امنیت ملی در دست بررسی است.  براساس این طرح:
🔸
عبور شناورهای متعلق به آمریکا، رژیم صهیونیستی…</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/455151" target="_blank">📅 18:08 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455150">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SxecfvbeiFF7GoqLfdoHqv102unNwBQUTTqiBep9lDzyxZEoT9jVXKTNxtIcMX_HNZxAHBENPMtd0AbNKUHHeYhwEcLx2DhFjsEGdRDvHA629yylDWl4-IDvAjdUUxrLo7812tIsO1eM3kNe9ZnxNiC2ICGqRfLDEsfKzU4_1F2YsbXEn4AJBTy0Gjh2zsgc0bdh8hj408UmF46mz0z11QR-zfL33_iypRGgNOuPUvVc8ac-5_YxSUjqDVNQKHEvCVf6HaqTXnshTJIBwtyFzBw7GljSXiHnenMCctYIOBOhU6iQr69MGV2Ay69bsQn42oDzs1noM4Nut1hALkL3ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تخصیص بیش از ۵۰۰ هزار تن ورق فولاد مبارکه به پروژه‌های انتقال آب، نفت و گاز
نخستین محموله ورق فولاد مبارکه در سال ۱۴۰۵ به کارخانه‌های لوله‌سازی پروژه‌های انتقال آب تحویل شد.
پیش‌بینی می‌شود امسال بیش از ۵۰۰ هزار تن ورق فولاد مبارکه به پروژه‌های انتقال آب، نفت و گاز اختصاص یابد.
این ورق‌ها پس از عرضه‌های متوالی فولاد مبارکه در بورس کالا و انجام تعهدات این شرکت در زمینه کف عرضه، بر اساس مدل فروش توافق‌شده به پروژه‌های مذکور تخصیص می‌یابد.
اجرای این طرح علاوه بر تأمین ورق موردنیاز پروژه‌های استراتژیک کشور، به تأمین نقدینگی فولاد مبارکه برای بازسازی بخش‌های آسیب‌دیده این شرکت نیز کمک خواهد کرد.
@farsna</div>
<div class="tg-footer">👁️ 9.28K · <a href="https://t.me/farsna/455150" target="_blank">📅 18:07 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455149">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mKwswDugGQpw_VjwaVOejRw4XFU2gHDaR2xL2GXmw2smKmqUwECtcK-HVI_FZEwdU-JaEHDkuVMrUZjNpHpVSfSPd1OT18BnR7KmVN_2jYUb1dfkS0WGs5AM4yeoT17lpSjuDEGAYQd_7y-HV1u39ChwWODwTr6aiyGl5sNTEPUc0Wnb4I5mYY5PndEVNlpc1KXfjfNLFttO65pSwG-LjULxSk8obUwTrdmNVS4OOdXDcHhGM_v8Is7yCGee1uXSBNi7HlqBroAkM4qfGTF88sp5ge-kvomMHBAKFUixEzQH_hkaVKW9qxaq_GlFnqMuEsp8XyUT5lbY65U99ABauw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
شرکت گروه پتروشیمی تابان فردا (سهامی عام) با نماد "تابان" در فهرست نرخ‌های تابلو اصلی بازار دوم بورس تهران درج شد.
🔸
به گزارش مدیریت ارتباطات بورس تهران و به نقل از مدیریت پذیرش، با توجه به موافقت هیئت ‌پذیرش بورس تهران در جلسه مورخ 1404/09/12 با پذیرش سهام شرکت گروه پتروشیمی تابان فردا (سهامی عام) در بورس تهران، از تاریخ 05/06/ 1405، این شرکت به‌ عنوان ششصد و سی و هفتمین شرکت پذیرفته ‌شده در ﺑﺨﺶ "محصولات شیمیایی"، طبقه "تولید مواد شیمیایی پایه به جز کود" با کد "4411" و نماد "تابان" در فهرست نرخ‌های تابلو اصلی بازار دوم بورس تهران درج شد.
🔸
سرمایه‌گذاران محترم و علاقه‌مندان می‌توانند به منظور کسب اطلاعات بیشتر در مورد شرکت یادشده به سامانه اطلاع‌رسانی ناشران (کدال) و سايت بورس مراجعه کنند.</div>
<div class="tg-footer">👁️ 8.03K · <a href="https://t.me/farsna/455149" target="_blank">📅 18:07 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455148">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-footer">👁️ 7.89K · <a href="https://t.me/farsna/455148" target="_blank">📅 18:07 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455147">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0ffc69a97.mp4?token=cajEFLJGP_5zH2QNZh81bdVK39qHQ27g402Z9jXoq4BtX246Q1WOvHkZCvhOD0oo_5Qcza3JrA-OnOee3lkakR4e0LDIoBtvIcgzgvjEtFp_co-GklG0wPdruJEzffECYVHzSRfmeMybxf3MuN3PgW-5MfSiw-3_J2k8VyFN5EjZjRG9K4zOtrafiJKwWPtjUpIoZBtmCBhGgvUEVAQG42MYAmL2KIiNtGCArYxsfsbqV8Gik32JHe0G1qTc3BHmjFY2k7TKMXKCEAW5kyDjWjN4hJeOerAOv-OyHT333Z_5Ju236zgGtbAVRsqAjArD6KslYP3TVf46USvUT2yI4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0ffc69a97.mp4?token=cajEFLJGP_5zH2QNZh81bdVK39qHQ27g402Z9jXoq4BtX246Q1WOvHkZCvhOD0oo_5Qcza3JrA-OnOee3lkakR4e0LDIoBtvIcgzgvjEtFp_co-GklG0wPdruJEzffECYVHzSRfmeMybxf3MuN3PgW-5MfSiw-3_J2k8VyFN5EjZjRG9K4zOtrafiJKwWPtjUpIoZBtmCBhGgvUEVAQG42MYAmL2KIiNtGCArYxsfsbqV8Gik32JHe0G1qTc3BHmjFY2k7TKMXKCEAW5kyDjWjN4hJeOerAOv-OyHT333Z_5Ju236zgGtbAVRsqAjArD6KslYP3TVf46USvUT2yI4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حرکت مشکوک یک هواپیما در نزدیکی پایگاه آمریکا در جیبوتی
🔹
یک هواپیمای ناشناس و سانحه‌دیده درحال سقوط به‌سمت پایگاه هوایی چابلی در جیبوتی است.
🔹
ساعتی پیش سفارت آمریکا در جیبوتی با ردیابی این هواپیمای سانحه‌دیده از مردم خواست تا اطلاع ثانوی از تردد در اطراف…</div>
<div class="tg-footer">👁️ 9.2K · <a href="https://t.me/farsna/455147" target="_blank">📅 17:58 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455146">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🎥
تنها خواستهٔ خبرنگاران و مستندسازان دربارهٔ جنگ
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.62K · <a href="https://t.me/farsna/455146" target="_blank">📅 17:56 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455144">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d573febfb6.mp4?token=k09U8hSwgzHJXbgn2S0YXPfSNvhuCwzsEU7_ZJSBKXEyxNXzS9ZX1N1LEKs4SnP7l06QU-LCF2g5duontldR3D-UVn03rdD-K9ZWNajrneccTc1tUcXM_4gZ6YXIeemlwE9YIByXovh33KCw3PGI8WFMS4zQoE6-PO0E2U9OD5jqjVDcxzWJT3jew_lz6FHXJuaLG5u_wkxKL-M6BvdvMhh7umpffHmr98e5hD3zz24rucrJmzmgzvB4RM7a5sEIXokbMOjyNerTNCX5qi83jWnNnH6dX9_uG0HqcRsUezT_X-nHqNeVz7-6aBKkFTK5i9ey0Y46ZIdbnKyCDa9d0avt38GXseqU8BJC5ERdWKgnjA2NsBCx-wwADt6DZotLRgRD1HfVkdDgWrM55CADbi0vhMQr_RlR0cFgPDwIe2QUmit63XaGzExoop45QJHlMgosMifHxATaN75mqt36eQHT0dBCb_9j7__Dj7Q25iCFE1q-xw13kYI-hp6BO20nkWjOGy6CT5Gfu1p1GzwsJUiL8AwbKzTdSdLoTdaBzOKb-EpR6Brw9HaVWzowEzYbUuAAiEtZFrfZDKUihTcp3sEi7f4QpTPk3DybyJXCNzDlgxhydOOaAWg0uuSM4FEiHTdlC8uM_zxm_mrybRHXkTHWjihuRgquV1UIdRWR0qA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d573febfb6.mp4?token=k09U8hSwgzHJXbgn2S0YXPfSNvhuCwzsEU7_ZJSBKXEyxNXzS9ZX1N1LEKs4SnP7l06QU-LCF2g5duontldR3D-UVn03rdD-K9ZWNajrneccTc1tUcXM_4gZ6YXIeemlwE9YIByXovh33KCw3PGI8WFMS4zQoE6-PO0E2U9OD5jqjVDcxzWJT3jew_lz6FHXJuaLG5u_wkxKL-M6BvdvMhh7umpffHmr98e5hD3zz24rucrJmzmgzvB4RM7a5sEIXokbMOjyNerTNCX5qi83jWnNnH6dX9_uG0HqcRsUezT_X-nHqNeVz7-6aBKkFTK5i9ey0Y46ZIdbnKyCDa9d0avt38GXseqU8BJC5ERdWKgnjA2NsBCx-wwADt6DZotLRgRD1HfVkdDgWrM55CADbi0vhMQr_RlR0cFgPDwIe2QUmit63XaGzExoop45QJHlMgosMifHxATaN75mqt36eQHT0dBCb_9j7__Dj7Q25iCFE1q-xw13kYI-hp6BO20nkWjOGy6CT5Gfu1p1GzwsJUiL8AwbKzTdSdLoTdaBzOKb-EpR6Brw9HaVWzowEzYbUuAAiEtZFrfZDKUihTcp3sEi7f4QpTPk3DybyJXCNzDlgxhydOOaAWg0uuSM4FEiHTdlC8uM_zxm_mrybRHXkTHWjihuRgquV1UIdRWR0qA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آغاز خدمت‌رسانی موکب کفشداران حرم رضوی به زائران
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.08K · <a href="https://t.me/farsna/455144" target="_blank">📅 17:37 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455143">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R4gkH5h0ubla3twwmjVQhzT1iO6yTAvFkeeVu4x8VxCAxotfgJ_H8S8P2QQYBmhU_BWM4LlZ1-NnCrAbg5wM2-8KzBmUwiJM3znLO-z7uzf_d2AIMNlm2ZN2_X-WmzWv85Shkj9gUI3EFZWsJCPDyaNEotN1D5aLeEBAPp6CIgmUsXTT3Lci2Gq60dIhQQDcYRFaMVxIK-zscm28pXcRMJGOW_rLPUzveqIDCx_rIBbrg1XcexnuTocq3-m1qLhePl2faw3s3wWyRgNy1Ph9NmHt5y8elhJN4C9IJUtu23WieXHABwe0NDuzc9k8A0jbNLoInX0HAYVYu40I6g9HFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکایی‌ها برای مهار شبکه‌های اجتماعی متحد شدند
🔹
رویترز: نظرسنجی جدید در آمریکا نشان می‌دهد اکثریت مردم خواهان نظارت و مقررات سخت‌گیرانه‌تر بر شرکت‌های شبکه‌های اجتماعی هستند.
🔹
۶۱ درصد آمریکایی‌ها معتقدند دولت باید نظارت بیشتری بر شرکت‌های شبکه‌های اجتماعی اعمال کند.
🔹
یکی از برجسته‌ترین نتایج نظرسنجی، حمایت گسترده از اعمال محدودیت سنی است. ۶۶ درصد آمریکایی‌ها از قوانینی حمایت می‌کنند که شبکه‌های اجتماعی را ملزم کند برای جلوگیری از دسترسی افراد زیر ۱۶ سال، سن کاربران را احراز کنند.
🔹
این حمایت حتی در میان جمهوری‌خواهان، که معمولاً نسبت به گسترش مقررات دولتی با احتیاط بیشتری برخورد می‌کنند، به ۷۴ درصد رسیده است.
🔹
نتیجه نشان می‌دهد نگرانی دربارهٔ کودکان تا حدی از اختلافات سیاسی معمول عبور کرده و به یک مطالبه عمومی تبدیل شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.82K · <a href="https://t.me/farsna/455143" target="_blank">📅 17:33 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455142">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vI4n_1lCYNsITjAyG5hpBV2XjZ2-U7N5gYP864qdohmruyzt-_V1F96cD6tjYCp4jIO0LGGqbWiudgzmPdMpO25auuMd62ZDfin1ZEGl5Gjsoi7HmiAwl3kWfc4PZZmilrJeoofhNEwvtmB9cetDlBdYjCBeKv72KZJTwbXQ2nJUnLNWzekUy2bHsdcJdeZQE9rTah3_eVH8_CtwqG29SFS-eBIylY2KSxOHyV5_dpgNgSQO8M2f0dm_YP6g2puknW_x7KaaS1nHwooizxmcDZaUlwvLTvyD7rg_JMatcmGcqrzv90M0XsXeV749cKhauwryR459tleASyViIRfufQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آیت‌الله آملی‌لاریجانی: تنگهٔ هرمز به شرایط پیشین باز نخواهد گشت
🔹
رئیس مجمع تشخیص مصلحت نظام: ملت ایران و نیروهای مسلح پای تنگهٔ هرمز ایستاده‌اند و حاکمیت این آبراه با جمهوری اسلامی ایران است.
🔹
به‌هیچ‌قیمتی عقب‌نشینی نخواهیم کرد و تنگهٔ هرمز به شرایط پیشین باز نخواهد گشت؛ اگر خواهان تردد آزاد هستند، باید به شروط تفاهمنامه عمل کنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.51K · <a href="https://t.me/farsna/455142" target="_blank">📅 17:31 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455141">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kqg8E3VZo9aX1vPNlmTxTw9UgwlSsmn5e8xD5M4KfTiUDuRxO6uaqTucr8pUBgSQ96xzxNtE58TAQG9dhieA1cuS6tuvAfk6T_i8dTahzvDzbplU91IZlsp1_rum4d8N0SjjKFr_ZFmtbSjvRW5IJvvzZwfYOe1SMZ6m4Gf7XL9HTAEcIxGNrjUz9gY6JCHMOb_PvSKYkmxkuXLoOtmLcxJSCr09pHmmitwnY1GpEmFM8IO0Zs4dxBQr9GqtCNh1MTy8UOMQ_DqERDjfPkXwyM5BZx30_NxpDveUl5JOnrPu1ksA8QYbRQpZeesq7SiRbmaZyHtC3vJUj_jUMbgolw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشف ۱۹۷ ماینر در یک مرغداری زاهدان
🔹
تعزیرات حکومتی سیستان‌وبلوچستان: ۱۹۷ ماینر غیرمجاز به‌ارزش ۳ میلیارد و ۶۳۰ میلیون تومان در یک مرغداری زاهدان کشف شد.
🔹
در این راستا یک متهم دستگیر شده و به ۳.۵ میلیارد تومان جزای نقدی محکوم شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.07K · <a href="https://t.me/farsna/455141" target="_blank">📅 17:21 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455140">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/up2j7DYryUieBusadkrMKeI4OrL10HkZRXXBtx2N-tVey0SAD0_7n-orpFvgOzJ6CQBT9u4bWU9V1l0W_XO17LjjKBoaUqfq7Wenjy667eqWfUZ2yaRVcOvvYPJQ9d3D0vp6rkE8-egFPaCYHjJSOESsSJgziRbFutlpPF2UwVgWo8UShTk6gj1d_IXqy-qi34Z_erGRPMrJa60pOXpVlKNGnL6vdYw61WYBSapNtiq7peKP5OrRF3osQ9UiAkdlob5kF7doKkrcKJF005qVJ1nKfkO16R6CNQjM091VMZOk33ebK-gtwjRDyKu5VZ-dU5L6_EUUlr_q0h9p1j4fnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏀
ترکیب تیم ملی بسکتبال با ویلچر مردان برای حضور در مسابقات جهانی کانادا مشخص شد
@Farsna</div>
<div class="tg-footer">👁️ 9.02K · <a href="https://t.me/farsna/455140" target="_blank">📅 17:15 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455139">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a549d3423.mp4?token=M6rlQlBbY0kiuq0lekehYk5u_H3jlQgDu4jU-o7chCZVd8ojiVBm2qrdvR3IIGpb6TogZV6XvBF0G7-NF7LJGxZcen0JyxBPgE9F0n9pDX_xu9YWCesa7BfHWG2zWB3wk82gdhsM3CNnx99m2qhOGCxoZVbJWi00HZTA_h1OdgYK2m6AlCxa8mFIAYxLuezRYDR5nI-NG_vv3B__huzl_6SYG-dL92H0KoAVzicxAqR9qYek_35b7eR4RUt7YFjbY5M8ajfMdZRdGpwsQSLu-Hyz4zo-ICuwVkdi4M65EoiZwpeZpqONrV11CNXuD36YnN6Kl5wunypyZrQjXp7zCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a549d3423.mp4?token=M6rlQlBbY0kiuq0lekehYk5u_H3jlQgDu4jU-o7chCZVd8ojiVBm2qrdvR3IIGpb6TogZV6XvBF0G7-NF7LJGxZcen0JyxBPgE9F0n9pDX_xu9YWCesa7BfHWG2zWB3wk82gdhsM3CNnx99m2qhOGCxoZVbJWi00HZTA_h1OdgYK2m6AlCxa8mFIAYxLuezRYDR5nI-NG_vv3B__huzl_6SYG-dL92H0KoAVzicxAqR9qYek_35b7eR4RUt7YFjbY5M8ajfMdZRdGpwsQSLu-Hyz4zo-ICuwVkdi4M65EoiZwpeZpqONrV11CNXuD36YnN6Kl5wunypyZrQjXp7zCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شوک شبانهٔ تراکتور؛ ربیعی رفت و نکونام سرمربی شد
🔹
محمد ربیعی در فاصله ۵ روز تا نخستین دیدار تراکتور در لیگ برتر، از این تیم جدا شد و جواد نکونام هدایت سرخ‌پوشان تبریزی را بر عهده گرفت. @Farsna - Link</div>
<div class="tg-footer">👁️ 9.77K · <a href="https://t.me/farsna/455139" target="_blank">📅 17:00 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455138">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d143b9e96.mp4?token=livNvHoPmkWcsbjZZRIQMbY3vx1GyVqIfWIOqp-y33SN5JQZnri0rnlc8J661fxTuBWk4G4wm7qxQiybRgJvmpGJWK_4SLRB_bpV6b9DdBmmWb06LWQ1h3KJzj1aekA1qXngNA0Jp8mL7yVFQBQDDRUfWmvhemsar-Aye_V__BKMGMu7FeXCrRhIyKNPIZGDj8pvjovZuClvrUr-78cJAOrGBjXgsEOKu12qd8I-PuRvPbCsUtKPoEKI4i-YW_-5jeJUoCt0N2OM06Hghy3ntR9ubm7-GFbeDB7sh62_rA4EuHx3t6uRXETa18ix1jJdSEn-ruJ9J4N2kFIAEyiimw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d143b9e96.mp4?token=livNvHoPmkWcsbjZZRIQMbY3vx1GyVqIfWIOqp-y33SN5JQZnri0rnlc8J661fxTuBWk4G4wm7qxQiybRgJvmpGJWK_4SLRB_bpV6b9DdBmmWb06LWQ1h3KJzj1aekA1qXngNA0Jp8mL7yVFQBQDDRUfWmvhemsar-Aye_V__BKMGMu7FeXCrRhIyKNPIZGDj8pvjovZuClvrUr-78cJAOrGBjXgsEOKu12qd8I-PuRvPbCsUtKPoEKI4i-YW_-5jeJUoCt0N2OM06Hghy3ntR9ubm7-GFbeDB7sh62_rA4EuHx3t6uRXETa18ix1jJdSEn-ruJ9J4N2kFIAEyiimw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شوتی که در بزرگراه باعث تصادف شد
🔹
در جریان دیدار تیم‌های مونته‌ویدئو و پایساندو در لیگ دسته دوم اروگوئه، دفع توپ توسط مدافع یکی از تیم‌ها و رفتن توپ به بزرگراه باعث تصادف خودروها شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.6K · <a href="https://t.me/farsna/455138" target="_blank">📅 16:55 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455137">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f605262cb.mp4?token=MSW-cC50s-BSPtQDyVrbldgY0H8AwCpR8CcrKEoMMrZUndCwKBiDCI3tZe0Hd-qsr8tFDlHRsvGgJUjAfnnEzYLQHCmLQTyaEwkWGoJ9abOhVW0y7agPxZFBXqUkpcU4P1dWUBLpdpmWUgleSu8bb2QaDmdM8djBppAdtDGQXaLMu6sbLhvb2HMwrjoesvY0Q4Sc-ZyikIR3bJaAswrpDFCQcRrFNl5M1RUu6-nBRDDjynXwt4PAWl7E2PVeVIvcjriKsdWbh-B3TFG-y6dYhgJwSNFdodS3ujGl5hmtbjtBkdKeHFEfTy4zUTgFj8zTNOTIRmQUuaiRrpTcWcQzwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f605262cb.mp4?token=MSW-cC50s-BSPtQDyVrbldgY0H8AwCpR8CcrKEoMMrZUndCwKBiDCI3tZe0Hd-qsr8tFDlHRsvGgJUjAfnnEzYLQHCmLQTyaEwkWGoJ9abOhVW0y7agPxZFBXqUkpcU4P1dWUBLpdpmWUgleSu8bb2QaDmdM8djBppAdtDGQXaLMu6sbLhvb2HMwrjoesvY0Q4Sc-ZyikIR3bJaAswrpDFCQcRrFNl5M1RUu6-nBRDDjynXwt4PAWl7E2PVeVIvcjriKsdWbh-B3TFG-y6dYhgJwSNFdodS3ujGl5hmtbjtBkdKeHFEfTy4zUTgFj8zTNOTIRmQUuaiRrpTcWcQzwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مصاحبهٔ عجیب خبرنگار BBC با یک اشغالگر اسرائیلی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.61K · <a href="https://t.me/farsna/455137" target="_blank">📅 16:55 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455136">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c08f1d721e.mp4?token=ZcrlXeteVXREcdadkhl6K0MxSNxCdPa4Yy6Xy8o6zJm9eiLyivGrUmTmhvM-U71aErHL6qJNMuslePVWOxeSx-XJAHB2gJwyl1gromInjTdlZeQyymTD545t88DH1p77L_zW7JmfErfqdR-7YTWgqueNr7PeSej7tiiQ4tO-BDyKh60MmvJ5OIh_RhWwzN4mQwafeMvecXDCpJWlV_GjHLuIs6b6cUsnP7toetIpEKkDL9Y5wf_9Q4r3zewhWW8wSfWHUvPSmbLeKysW7blslBglOiaDPNZ8DbEKLqMi3oE4xJPhjaONn5k-6Sh9cIESegRSRmG56SWJpFO8CWWb8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c08f1d721e.mp4?token=ZcrlXeteVXREcdadkhl6K0MxSNxCdPa4Yy6Xy8o6zJm9eiLyivGrUmTmhvM-U71aErHL6qJNMuslePVWOxeSx-XJAHB2gJwyl1gromInjTdlZeQyymTD545t88DH1p77L_zW7JmfErfqdR-7YTWgqueNr7PeSej7tiiQ4tO-BDyKh60MmvJ5OIh_RhWwzN4mQwafeMvecXDCpJWlV_GjHLuIs6b6cUsnP7toetIpEKkDL9Y5wf_9Q4r3zewhWW8wSfWHUvPSmbLeKysW7blslBglOiaDPNZ8DbEKLqMi3oE4xJPhjaONn5k-6Sh9cIESegRSRmG56SWJpFO8CWWb8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
چین در محاصرهٔ طوفان دلفین
قرار گرفت!
🔹
تلویزیون مرکزی چین از وقوع طوفان سهمگین دلفین در چجیانگ خبر داد؛ حادثه‌ای که با وزش بادهای شدید همراه بوده و وضعیت اضطراری ایجاد کرده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.43K · <a href="https://t.me/farsna/455136" target="_blank">📅 16:50 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455135">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SpoPhaVKOm7TnzWCZ2vLhtaN3e2KAkB03URuDEBOO-r8bgLE4RVFJa-9Yu5awr1SHNdDflqDc7z23O_j5wD8M57EAiRHE8LWWDUJHF6XSx6mVMn1hGRgQm9GomSa4cfchBAixGFB9PCw3qPVhbe4J7pylQf9exvqeT4P0s0V3iYptt4QD3Y-kM9ql9BfwGB3EJCNgzHSxc_HF-Jkkq7njHUjAqG_a1XeRMvvPhsW3j9S4WYZEdmISAofDefEU9JvYPToHWChqcDc_2RDyTD7L_BAysUSI2YPELCMDkrby8pjyixHOToPc2SZXFF1j2FvIq6rUAPDK6Mxxi6TfeBJKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توافق دمشق و مسکو بر سر وضعیت پایگاه‌های نظامی روسیه در سوریه
🔹
وزارت خارجه دولت شورشیان حاکم بر سوریه اعلام کرد که دمشق و مسکو به یادداشت تفاهمی جهت تعیین تکلیف و آینده دو پایگاه راهبردی روسیه در طرطوس و حمیمیم دست یافته‌اند.
🔹
این وزارتخانه تصریح کرد که این یادداشت تفاهم بر آغاز فرآیند «سازماندهی مجدد» حضور نیروهای روسی در سواحل سوریه تصریح دارد و بر اساس این توافق، قرار است پایگاه‌های نظامی روسیه به «مراکز آموزش مشترک» تبدیل شوند.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 9.52K · <a href="https://t.me/farsna/455135" target="_blank">📅 16:45 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455134">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3e35e5383.mp4?token=CP4NtHJLN0E9YVFPyJe28oiR79YPoxuOZUoLcuLIqAKaxYJcY16pIapFt1N_Bz9hqCwvpqLVBB6rpn8n4eO4dQoyAah2ugFXNkztYzZhYS8ALhFZSrYscpVEl5i3pUbET6D19A0RxveJx56Rg3_n3qf0ZBU_za_Y2d0Pon1fUoi-wqXV_G9akQ5RnxIQjMVt_8fbHI5mjiJf-NMHOp16PKI7ut2HcbBZ8gM3ATLMyIk7VIjkB4MHc4kCdABYs8rrzn4UhFG6yanYAuD2ePBw9WPojG9xYMaERN-pRlQ0uN3M0NSD9WehImQY-AJgIjNa2Ua25HXRe1z7xyCQtxbAsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3e35e5383.mp4?token=CP4NtHJLN0E9YVFPyJe28oiR79YPoxuOZUoLcuLIqAKaxYJcY16pIapFt1N_Bz9hqCwvpqLVBB6rpn8n4eO4dQoyAah2ugFXNkztYzZhYS8ALhFZSrYscpVEl5i3pUbET6D19A0RxveJx56Rg3_n3qf0ZBU_za_Y2d0Pon1fUoi-wqXV_G9akQ5RnxIQjMVt_8fbHI5mjiJf-NMHOp16PKI7ut2HcbBZ8gM3ATLMyIk7VIjkB4MHc4kCdABYs8rrzn4UhFG6yanYAuD2ePBw9WPojG9xYMaERN-pRlQ0uN3M0NSD9WehImQY-AJgIjNa2Ua25HXRe1z7xyCQtxbAsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مردم ایران چطور برنامۀ ترامپ را به‌هم ریختند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/455134" target="_blank">📅 16:27 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455133">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e02de7fa7f.mp4?token=uirMSRVim1pCgKOTj5vR1Fzm6Y_teYYbptyp66DJIxtg3JzsSl1B4iBG68iEc0LGTeJQR9WTPQenmwoRWwMlOnADhSYrr4hOWJ0-SYkM6wGwtpqa7GzDvmv3HaGLbQObtjWYnL2-8tarLTON8v2uBXhnF_qtdPO6Yw-Fwf-YLYVkSNh34XLl6PecNAW-446wRLQ-pakn6l4eM8Vzc04NQ8BqN_haSN8ooAKs2ksqWXzK5oSb7Lr4AikFGHfl9QSGG2VFGdCLxzh9N-ssi70c10hE2PIQiE3vhLC6fYUyCGOBMjuZIBNDEZHjxRBftrSXgfEcQQuZp8GpldEErFkEAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e02de7fa7f.mp4?token=uirMSRVim1pCgKOTj5vR1Fzm6Y_teYYbptyp66DJIxtg3JzsSl1B4iBG68iEc0LGTeJQR9WTPQenmwoRWwMlOnADhSYrr4hOWJ0-SYkM6wGwtpqa7GzDvmv3HaGLbQObtjWYnL2-8tarLTON8v2uBXhnF_qtdPO6Yw-Fwf-YLYVkSNh34XLl6PecNAW-446wRLQ-pakn6l4eM8Vzc04NQ8BqN_haSN8ooAKs2ksqWXzK5oSb7Lr4AikFGHfl9QSGG2VFGdCLxzh9N-ssi70c10hE2PIQiE3vhLC6fYUyCGOBMjuZIBNDEZHjxRBftrSXgfEcQQuZp8GpldEErFkEAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
کشته‌های آمریکا در یک فهرست جا نشد!
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/455133" target="_blank">📅 15:49 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455132">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d050cf1aaa.mp4?token=eO2ybgnaqs4OfLRhs2LhuYofXZwYC8VCj3lv9IcqzBdGzIDjQoR2wNCiWzt6ONRKaSi1di7zxFa4qaBsOkvvjs5MFiPByzH4R7zwEN5THhoyZoFWcnwyZ57-pEB9kkMPdQrux-F5L_IJxarlbSen1FBlkD1LFaYbtybyNvydh1Pec0xWg-IbovlZ8k3e1ECRmZokHAv1cCI_qh0kBjw_dvC3PWBam501Ce2KBE7XeVOvGdD47m4UTHGIugSAWuQJij0apwHahieqKZs6SWvXVIYSS9xLs2BA7f_cYiIRLOb2WMmmSTbRNAA1G90ryeya_AQjhs60TRk0rHDVQMj1DA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d050cf1aaa.mp4?token=eO2ybgnaqs4OfLRhs2LhuYofXZwYC8VCj3lv9IcqzBdGzIDjQoR2wNCiWzt6ONRKaSi1di7zxFa4qaBsOkvvjs5MFiPByzH4R7zwEN5THhoyZoFWcnwyZ57-pEB9kkMPdQrux-F5L_IJxarlbSen1FBlkD1LFaYbtybyNvydh1Pec0xWg-IbovlZ8k3e1ECRmZokHAv1cCI_qh0kBjw_dvC3PWBam501Ce2KBE7XeVOvGdD47m4UTHGIugSAWuQJij0apwHahieqKZs6SWvXVIYSS9xLs2BA7f_cYiIRLOb2WMmmSTbRNAA1G90ryeya_AQjhs60TRk0rHDVQMj1DA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایت فرزند شهید لاریجانی از واکنش پدرش به ردصلاحیتش
🔹
محمدرضا لاریجانی: درباره حوادث ۱۴۰۰ ایشان می‌گفت آبروی هرکس متاعی است که خداوند به او می‌دهد. ما موظفیم وظیفۀ خود را انجام دهیم.
🔹
فردی به ایشان گفته بود حالا که این‌طور شده، اطلاعیه‌ای تند بدهید اما پدرم تاکید کرد من فلان شورا و فلان نهاد را نمی‌بینم، خدا را در نظر می‌گیرم این‌ها اشتباهی هستند و باید تغییر کنند، چرا ما باید پنجه به چهره انقلاب بکشیم؟
🔹
در ماجرای رد صلاحیت، آقای اژه‌ای مردانه ایستاد حکم صادر شد و دست آنهایی که پرونده‌سازی کردند رو شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/455132" target="_blank">📅 15:39 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455131">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NJYmRhZUKUE8OXXHzas00q-LcYPwJ4NiJHZiH_SWbOCUan5gL3znzrhL5JUJ79i5O17caUEewDqbSmRqqe8x2kngXEcaWNFW3PYOY1n3ZdY063BaKo48bjG3HNig_WebEvNXVoPjmxqARqFERo1d2YcU4U_Fvy0wvkBGzZZsSQEvXaAqrfCZ_Y8Y2u6Pxj2tK9AnHvX6H4k6kY4agK2dY7HaqGpmKoZlfQa2GDULIV-AmKrXnsgRaU9-yEmb1WXZA41UhsreCc5kINLeLeRuvS2uUBd0YPA4oU8nUiZTc6vRg3d20BONIDInIs0P5S6k6tPikeIsZOblcV0Y2iYk4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پای ترامپ به نفت گرینلند باز شد
🔹
همزمان با تهدیدهای تازهٔ ترامپ برای تصرف گرینلند، یک شرکت نفتی آمریکایی بدون دریافت مجوز رسمی، تجهیزات حفاری خود را به سواحل شرقی این جزیره منتقل کرده و برای آغاز عملیات اکتشافی آماده می‌شود.
🔹
شرکت تگزاسی «گرینلند انرژی» قصد دارد با هزینهٔ حدود ۶۰ میلیون دلار ۲ چاه اکتشافی حفر کند؛ این شرکت مدعی است منطقهٔ جیمسون‌لند ممکن است دارای ذخایر نفتی به‌ارزش یک تریلیون دلار باشد.
🔹
دولت گرینلند اما تأکید کرده که هیچ مجوزی برای این عملیات صادر نشده و هرگونه فعالیت اکتشافی باید با تأیید نهادهای مربوطه انجام شود.
🔹
انتقال تجهیزات نفتی در کنار تهدیدهای ترامپ برای سلطه بر گرینلند، نگرانی‌هایی دربارهٔ ارتباط این پروژه با برنامه‌های آمریکا ایجاد کرده؛ موضوعی که مدیر شرکت نفتی آن را رد کرده است.
🔸
گرینلند از سال ۲۰۲۱ صدور مجوزهای جدید نفتی را به‌دلایل زیست‌محیطی متوقف کرده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/455131" target="_blank">📅 15:32 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455130">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qCGOOJCo5d8utfWEWfvFnZPSF0v4oYxK2OgVFJy514cmTpokyA1FnH3Jy1nKcIhzrYA3JnlKSERvCx0dKHFU705RTozfGMn6GQ0hRAcdwgDB0MHeq1vHlOrXoN4vA_OrSo4_wvO5YRP6X9haHjJtnoExBjAnxLvMms2LmM0ata1qHoYbCG2e-WvYxJCjkPO_YzKYkeXGiUaBFEO8vWicgNjUXQSL-N0EzdG4wJHyascMNAdP4kbu7h7eh_eVz0JLtYlQqG3ry181hsXxzAlzvwXrOpLYhskqgHa64dGTfCCh5GMdPvfJPSEsaFsbFkjHr1N9LKoH65yTW5thaeG-PQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حرکت مشکوک یک هواپیما در نزدیکی پایگاه آمریکا در جیبوتی
🔹
یک هواپیمای ناشناس و سانحه‌دیده درحال سقوط به‌سمت پایگاه هوایی چابلی در جیبوتی است.
🔹
ساعتی پیش سفارت آمریکا در جیبوتی با ردیابی این هواپیمای سانحه‌دیده از مردم خواست تا اطلاع ثانوی از تردد در اطراف این پایگاه دوری کنند.
🔸
پایگاه هوایی چابلی میزبان ادوات نیروی هوایی آمریکا است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farsna/455130" target="_blank">📅 15:17 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455129">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FrJJagGtIkO3hR_Q_kLEI-IsRoq_sBMzD7Z5_rADh3TJe2D8lgmBCBT4u_qw5dEHf-IZzIRne5c4pbTWqGK-3sHecGNwARD5XLmnv6O_CinE1ij8vVmqGtF48NLHA6njf-emtpJN8_kvSedp3FiDfoA_v74r0blpjY_0sfumO7zlP1mlinepjLpjJlXyLlFY985EbQU3JmreZGsyC7RufM9RWOZjUnsi1UjGKdRHyGM1ulHkeJXk36CAyFXOBiGKy0lCBG58rBQo6KXA3LlgCebwVgGyMB4ZbqQzK8M78HKVz4W-0nN6bCQ7NTneliGNf_kD_aRd5FtvePapGNFftA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رضاییان در فهرست پرسپولیس جایی ندارد
🔹
در روزهای گذشته شایعاتی دربارهٔ احتمال بازگشت رامین رضاییان به پرسپولیس مطرح شده؛ اما پیگیری‌های فارس نشان می‌دهد این بازیکن در فهرست خرید سرخ‌پوشان قرار ندارد و باشگاه پرسپولیس برنامه‌ای برای جذب او ندارد.
🔹
یکی از دلایل این تصمیم، شرایط پرسپولیس در پست بازی رضاییان است؛ چراکه سرخ‌پوشان در این پست بازیکن در اختیار دارند و نیازی به جذب بازیکن دیگری در این منطقه احساس نمی‌شود.
🔹
همچنین رامین رضاییان با توجه به اینکه بیش از ۳۶ سال سن دارد، در چارچوب سیاست جوان‌گرایی این تیم قرار نمی‌گیرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/farsna/455129" target="_blank">📅 14:54 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455128">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dcacf87c4c.mp4?token=bQ6e7XRnGH6aAQetYubg_25GH3b9Wwu-SJwJgGKb2aXg8URlhLm7y8jzRzkFkKjmkQqqRvDnF_NwaRnHRtkN94q4T5_qY27itVnIBv8yBrOm2AqT9npov8VrdTkJYa_WD2gbSK7set3FqNXxhLHpVQHgYtjklQMLoGfqV6xsHU-v2h-xnV1hOvl9UYmswdJORrRrTx7w5xfp1fBiS-Y75ZizoHkn5P9ShWmesGEAWAs-jNDtyy0otZFGtWDdDqeCVSiDBcCDWOfvraueYtzyIVnQehvlGWUlpbGulgZXmjC5lHAIP_C-uSbdmlBwOTOx-nYFdkOY40wknBX3F6RrIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dcacf87c4c.mp4?token=bQ6e7XRnGH6aAQetYubg_25GH3b9Wwu-SJwJgGKb2aXg8URlhLm7y8jzRzkFkKjmkQqqRvDnF_NwaRnHRtkN94q4T5_qY27itVnIBv8yBrOm2AqT9npov8VrdTkJYa_WD2gbSK7set3FqNXxhLHpVQHgYtjklQMLoGfqV6xsHU-v2h-xnV1hOvl9UYmswdJORrRrTx7w5xfp1fBiS-Y75ZizoHkn5P9ShWmesGEAWAs-jNDtyy0otZFGtWDdDqeCVSiDBcCDWOfvraueYtzyIVnQehvlGWUlpbGulgZXmjC5lHAIP_C-uSbdmlBwOTOx-nYFdkOY40wknBX3F6RrIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: دشمن آدم‌هایی را ترور می‌کند که گره‌گشا هستند
🔹
برادران نظامی در سپاه و ارتش کاری کردند کارستان؛ با ایستادن مقابل دو قدرت اتمی دنیا را به حیرت وادار کردند.
@Farsna</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/farsna/455128" target="_blank">📅 14:17 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455127">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🔴
رئیس‌جمهور با رهبر معظم انقلاب دربارهٔ مسائل اقتصادی و نظامی کشور دیدار و گفت‌وگو کرد
🔹
پزشکیان همزمان با شروع سومین سال ریاست‌جمهوری با حضرت آیت‌الله سیدمجتبی حسینی خامنه‌ای دیدار و گفت‌وگو کرد.
🔹
در این دیدار به‌تفصیل دربارهٔ مسائل و مشکلات کشور به‌ویژه تأمین نیازهای معیشتی مردم، شرایط موجود جنگ تحمیلی سوم و آیندهٔ پیش‌رو، تحولات حوزهٔ نظامی، راهکارهای ناظر به تأمین منابع و مدیریت مصارف «ریالی، ارزی و انرژی» و همچنین تعامل اقتصادی با طرف‌های خارجی تبادل نظر شد.
@Farsna</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/farsna/455127" target="_blank">📅 14:01 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455126">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">آزمون وکالت ۱۴۰۵ اواسط آبان برگزار می‌شود
🔹
رئیس کانون وکلای دادگستری مرکز: طبق قانون، کانون وکلا مکلف است سالانه یک آزمون برگزار کند و آزمون وکالت سال ۱۴۰۵، ان‌شاءالله در اواسط آبان برگزار خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/farsna/455126" target="_blank">📅 13:56 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455119">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eNTjjI35JUytUVUuEHS5iGIBFMfppoGq2NzZx2pSEx1akgcuwEez5BiJLbJB-FVmfqwuDhfHkW8sbZGYJBCwYA8PQDM23ARgrEL1KwPm8l6KDrz67ZSEX6qizJ3ZM115qAS6KT9XPE14qssFoAf4EXkNIM8gCcY2jdRrXsBz8qsVE0DwvPSc5iYldlHxdguxQFkg3UGdzPgrS2k8_JpuJzOceC7WqZ3S9pqTcujCQmOpdNCPqUsF7VbXSfeXQ9V1lFzxFu-eYsJpQosfV6RDYKntnM1XbIFMLuY8QM7J4qhtx-EQ55uX6SM6zsZUsLYcJXwmsz6bXCt-OWz1ubGgtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XSxvaCVd_CXx_LUxilf3ldD_NZRfWqQYvZtcIUgqvX13X-G7ujME8MwU3tWG0OgUkEbdlMv07Qg1HWzGIiDkYdFKzRqXrowFOfgBmJvDeDMJEY21o48uR2eu-gktW6AMEDv9fpbv7KpCfkt_bI3ND3kwvu0ATQPEduG5BAiSwQW74zr-qeeQb5LOhqfdxkPsD6shwaJ1gGwBM4TCr21wgmyqiJ4v5Vg7Sy3W5Vv7Wv8fxR5aw1eMhNXDouIby66rCm2Cc2Xok56FOgdgmzn80GmjJTPMNjOGaE-smHaTLvMhKMcRGlSOJTXsapfdj1aCgqr1dis17HhzPM713JxWgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZHZYhX5BjCpjdkL7f-cTkPpnHaZ7Uh6aUMN59TG5NswVOtTxnRd5n2oB-HQgv4MIHD_DX9PqxZDvy2JUkHQ0WoVMEFZrloybSF3eBNm8vmkmxtovt9wONV2P-NnzsRkHxQdCDOhWoyNlw0wMX44G8jyCac_z9yeab7Zghu7eSrxZO3uH_vmde0PgB6FHQDnsSymhgFVQcJN_s13QFi-cwb_tpBgAClRApGJ7Q0eF5jLS0hmVg9lPEIwWwXtIQVbc_Sb9n6bT2IMCHxAvRXcB96xWxUQwlPuOzzjAV-efEepZzbt6uA2Vb76-slZssu3cQHkvLeH6ujYzUlL3aPS1qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZwN-JQioQ4VBtXT1GyvXy0pF3meb3mYottX-mg1eIvL8LfuXtAkyd0hQFxyZBR8-AkgZ_UGLfp8qlSorHgB4b0WmwEMt7UbdYN0l_2ikYKFjuyyb2TkbpCwanoLp1M6ixzkL_aBSIhsBPGZgyK_GE_pxyBgNyMN9roneyeO3sZIuAkwxeDb8v4hTHH0D-p1xVBWZj2pBo8HJsvCOBC-c1kLhgEKCHfM7HfoEZW5D2qSsYizBojtTYaYpw_AhALOcC6PrfPNbzx6noxBa08ry148GZstVsUeF2km4s7BMCa9f73rOIWl9rebrlpVVGw_8FadGMCklMlmCyUdu7JatdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KXQqVIN2zwaa9Y39Kg7Gc9jPkDATDymzH3ykQKZ7wYXj7S_bKlM5-8X9x132iXcxkz5rrCG75CH0i8qqiTJ59pcs5Jy4MvdYekQU-iOHTV73oTTy486PcA3yJRwS7D3QUNcHGkOloUlr30AojI9O2B9CafWj5LHj93Xl1zEbzNvKzMKelj7P9T2nlZZoV4dK6RgTxGiMJ4dhQAuIdIRNpxjrusAYbtMwvDfmNbwSPDk20hHQwAe4VE_5uV5mTTgYxm2U1Qq0NeP-jc2RZyCq8Yj7r_e5WDzzdIK5Y_UiEljhwJxrTL6hpQFNlkMIDAP2uScCtMVmw644yJEEBs3mOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/siXGLk3T5ajC7cKIWZYA42pX2yyAznqEFhxqhO1qrbYsBPlKSQhihV7E-iJF3xeLdPeQqYhTxupxdPqOMNTh-cpeSkPYOO3K8pkMNomIjFw-laYLnq_djizb5u30b7yo9l-tKiLqNWvHzMWQhaaR_lGNsxEjflo7Jr486pTG6ToWiM_vsHw76v0b_zI0UkeMyRtVRcwhlwBsGvCf-CKl4RodTFuZ01Dk3ykEUBZtj8pBEOETZzQp6S-Oq2JRwYIAYi0Kpk6bimt06dtQuf0s2pE5l0L7OC8QUGsAhBWTFRXKGldxR8L3ltI1hRWElDfV87AUjYfakyze7j8guzRd9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AngV0Uqcg48LbMpg_ZmTHxvS1jg7377AnC3fL8PWU75MmpvO1epHqsArvwrVuHhH680P1Cf8WfgkSJ1_Gl8TbJpRXeYTtflN2Qcqv3K1JdoO5xCeFXqTBYPfbrHva2WMoM2lj9GO7zvk9fHbpzXALHcH7C0ult8NVkpQ-NklDUa5pL7ITMJcOjY827Wi-v3hslBbCBXyU6nczMOufiQJWmaTnbB-kYuQktvMCjQuYQWGdF8Dp3g_o9cVDN1K_gu3XO1j5YVgOg_0OpoO9nEMTYIEBHTG1Z-6ytWkHaOHhhkxi9xadCOzVCIVfqyLuWARLmGQzBIWalcP9aUEDQyZww.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
مراسم محرم و عاشورا در آینهٔ اسناد وزارت خارجه
عکس:
زینب حمزه‌لویی
@Farsna</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/farsna/455119" target="_blank">📅 13:53 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455118">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XmKWaigs_Ve47epQaXPhMtmXM6UJby0uVKT1i5eSzJCA6Az1nncvAtGyGngIrgsZtUN21Qor9sxOlI5eZ2cRsLJeOB_MUN1OvgDQPpyfoLwsHtIjwzgg24sggmx8BEuYAI8X8YJ-EmgekcHgrV0RuDPTfsMthBktZC9WtOyFTzKgzVlQrAyOj9WBk5-o4bC0FR0wQHuj8aQIjoBmQfVButLYGG1KFdKrqmfdU2RUC9LIfEvChTpvLi9ucqaMJP3FFd1U3TbF7Ysc52Gq4tvw4FDQwshXMK1bPOhyL04yvuPNm_u483Ec8P5YT8avQmRvAtjAOwPDn63qmU1bBs13RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نجات لنج حامل ۵۰۰ تن برنج از غرق‌شدن در بندرلنگه
🔹
یک موتورلنج باری حامل ۵۰۰ تن برنج که از کراچی به مقصد بندرلنگه در حرکت بود، در مسیر دچار آبگرفتگی شد، اما با وجود حادثه توانست خود را به بندرلنگه برساند.
🔹
پس از پهلوگیری، تیم امداد و نجات دریایی با تخلیهٔ آب ورودی، سبک‌سازی شناور و تخلیهٔ بخشی از محموله، از غرق‌شدن لنج جلوگیری کرد و شناور در اسکله مهار شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farsna/455118" target="_blank">📅 13:42 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455117">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0dcb47fdfd.mp4?token=jaIpdSbNwDHc0MLDU5WgkNYWO4SVjj3a_ScnjwLwxo9uBrF1qDcYC7enRboFqybPhMdLxRjWsWbS_g9LFkBP1GWZrX3hdyuN-Ss9VuKhgkh-_OGX-fePjLueCAUySQE1BmKi8IzDCBeCgHcPYNpP2LOobN1PjQNqhGK_a-pbmZPpgU-nhpW3kuEYtsugAgV-dZ-uqdjRqiaLhCsQiUFgNoBEQXBlpxFsAQv3zvbgfY-q4u73W8QUnOdVpCEdA39s_6A1yT6efanIjrP_X4BMnyiUzLM2ZPWq2J2hCupjuVqc1Vl-FqJxceTbfvzVoPeG4JxTOHSdohySwv32ctyyZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dcb47fdfd.mp4?token=jaIpdSbNwDHc0MLDU5WgkNYWO4SVjj3a_ScnjwLwxo9uBrF1qDcYC7enRboFqybPhMdLxRjWsWbS_g9LFkBP1GWZrX3hdyuN-Ss9VuKhgkh-_OGX-fePjLueCAUySQE1BmKi8IzDCBeCgHcPYNpP2LOobN1PjQNqhGK_a-pbmZPpgU-nhpW3kuEYtsugAgV-dZ-uqdjRqiaLhCsQiUFgNoBEQXBlpxFsAQv3zvbgfY-q4u73W8QUnOdVpCEdA39s_6A1yT6efanIjrP_X4BMnyiUzLM2ZPWq2J2hCupjuVqc1Vl-FqJxceTbfvzVoPeG4JxTOHSdohySwv32ctyyZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
فرمانده نیروی زمینی ارتش: پای نظامی آمریکایی به ایران باز شود آن را قطع می‌کنیم.
@Farsna</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/455117" target="_blank">📅 13:38 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455116">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">حملات مجدد انصارالله به مواضع مزدوران در بندر المخا
🔹
رسانه‌های یمنی از حملات مجدد انصارالله یمن به بندر المخا که تحت‌تصرف ائتلاف مزدوران سعودی است، خبر دادند.
🔹
بندر المخا به‌دلیل موقعیتش در ساحل غربی یمن و نزدیک‌بودن به باب‌المندب، اهمیت ویژه‌ای دارد.
🔸
پیش‌تر…</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farsna/455116" target="_blank">📅 13:34 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455115">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ItRMP9lhoTpzewA6zdBlm049EK9qq6ohiDl4H-ZoR22kgNQUAljG1tpQfVs_LzWjLHKmIOTLhMSLhTiL8YSt97Bm-RyuJDh1IsG_J0mtGxfCuzhKzvuMvpYOY0bwIeoH_btAFHE-_IcpsskOY-NASUQ3HceWl0Oj3Ewbub2uLLv5ETWn3v8YryrLTAS5e9Ka5h0BtjhWXjvMQpxX2kfS64pUPVdkVzgrb4zVx4zTRfpAwJKYYYBY3LquqLa3zmG1BNn5H0T7WHtor4WDrq9Zfy-d_cW-D_g25YWdvLsjSIAlN1MNk8OaDxVT1L4DJqT3Y7m3V7eYPDzCxiY2pU6aKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شهادت یک جانباز حملهٔ آمریکا به جنوب کرمان
🔹
ایمان انوری از پرسنل فرودگاه جیرفت، که درپی حملهٔ جنایتکارانه دشمن به سایت راداری جبالبارز در جنوب کرمان مجروح شده بود، سرانجام به درجهٔ رفیع شهادت نائل آمد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/455115" target="_blank">📅 13:27 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455114">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">حملات مجدد انصارالله به مواضع مزدوران در بندر المخا
🔹
رسانه‌های یمنی از حملات مجدد انصارالله یمن به بندر المخا که تحت‌تصرف ائتلاف مزدوران سعودی است، خبر دادند.
🔹
بندر المخا به‌دلیل موقعیتش در ساحل غربی یمن و نزدیک‌بودن به باب‌المندب، اهمیت ویژه‌ای دارد.
🔸
پیش‌تر یک منبع یمنی به المیادین گفته بود: صنعا این معادلهٔ جدید را در داخل خاک یمن إعمال کرده که هرگونه حضور نظامی یا تحرک نیروهای سعودی به‌سمت یمن و بالعکس، بلافاصله هدف قرار خواهد گرفت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/455114" target="_blank">📅 13:05 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455113">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QfS__wTKL2nzEQodJKwdRV4juyrpdXMxA3iFinjQzqJ5Z-jA-kKG41X9v69wQ72cLAh5z0PLdcgr-gEvzES6PJrJnATfSCR85pCmtDcWN0SrbX835DOYuq5IQa9GYHVy_5L7GbFJvFTSx_tHeHDnM4uvf1qm0nQrzRwcPwV4fTsI1NSlRCvGSA5D2sM1Wp7z0jhmQy2WVZYpwKLGDyK4TaCL7KtjqnjiU3GJdZlNcUBL-KCUigTQYyBLx04Fzck0hhwsSEMUWeDBnKDWSUkVRbhi6423PuJuFyKyjwCuRLE8gUlSNAMNktwcKPMjWJoUZ8Zzq4x5jMBVJ3GpnW5pSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زاکانی: کالاهای اساسی را برای دهک‌های پایین جامعه با تخفیف ۵۰ درصدی عرضه می‌کنیم
🔹
شهردار تهران: یکی از اقدامات مهمی که شهرداری تهران به‌دنبال عملیاتی‌کردن آن است، ارائهٔ تخفیف ۳۰ تا ۵۰ درصدی در کالاهای اساسی به دهک‌های پایین جامعه است.
🔹
در نخستین گام به‌دنبال تأمین ۱۰۰ قلم کالای اساسی برای شش‌ماههٔ دوم سال هستیم که این رقم معادل ۵۰ درصد از ظرفیت کل سال خواهد بود.
🔹
شهرداری تهران علاوه بر ظرفیت‌سازی برای خرید کارکنان نیروهای مسلح از فروشگاه‌های شهروند با حکمت‌کارت، این آمادگی را دارد که خدمات جدیدی را برای این عزیزان در مجموعه‌های مختلف شهرداری تعریف کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/455113" target="_blank">📅 13:01 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455112">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cp7B-97oY_eWRDoAvyyzdYmYDdD5UIfHf4BOD7crW_j_JFsAvL4dXlGq_vL5qSFN3F5oUxcpVm6liGq9Z7j_huJQvtakvKhiYy7r7eUwNXHi2q3OrhtKQIO_CQE3f-1WLxnoTzeGB2PJ6S_CB8aec91J9sT-H1lwUb0aW_lWG8T-PWRcsrZHLdbmOurPSeNx5ZeDEWsv2BoQ9YS58RHU8si_U2lGGyQTFoT7vquTkqG9vvCsXb-lyd6lVoFEX3oS8TcSyho05fxLba0AISBe1IHLWEvqRw57br_tvVZWjKi-Q9x0F_EYyVtI_EPHx061gkZy74NqpERLbevmFZcXaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ورود ۱۲۵ اتوبوس‌ ۱۸ و ۲۶ متری برقی به تهران تا شهریور
🔹
معاون حمل‌ونقل شهردار تهران: قرارداد تأمین ۷۵ اتوبوس ۲۶ متری و ۵۰ اتوبوس ۱۸ متری برای ناوگان اتوبوسرانی پایتخت نهایی شده.
🔹
در صورت تأمین نقدینگی، پیش‌بینی می‌شود تا شهریور ناوگان به حمل‌ونقل عمومی اضافه شوند.
@Farsna</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/455112" target="_blank">📅 13:00 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455111">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SaYzhYa_tlS7JDaJL_0LztGr0VZfUxwde_RldBQ6u86EpOc18Rb7lG-1tJItdASXeKlP-d_GbQzX-QVlQCSRC_3x6IcHMr77HNQJwJBVB91Kur3mP8VJFGZWFgucUsDfepK2zPdX8BML8gwczOLDFAy6kN_0jQzAoqSfnzOtYcvKe-vhtdUJ-lpd2SuqLYUJQX1zebq8DS3xqacZxW6KVRxsuxHuXtT2fJfIvRHj23fz4DCCHEvqq7LBBoGnLOLdEd0La1QyqHuP3ZpOsaIHB19GproML6Qv8mt4Cx6bN-ua0X9-JWfFzU3tcZEgpuk5OipcZwtLXiqFOqYToUe4eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شاخص کل بورس در پایان معاملات امروز با رشد ۴۰ هزار واحدی به ۵ میلیون و ۵۶۰ هزار واحد رسید.
@Farsna</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/455111" target="_blank">📅 12:35 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455109">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f11c9456f6.mp4?token=emF8xPRYHQHjoFtzT8BrHsyFAYOZpyHrxbdKneSu4nRZ3enES0HHM7GNxp2p5CZEuyW0j65IC-hfBHKF7r2CloCecmgNllm_mt0eTxNYHn6sOJpASEPAmCcQWUXcVX3Jc1ugvKLg8kisauLxQtevqjdDLrjbtOxcJIrWyxem_Vwyp3cBY7w6lPlvIBn-u__Wjm7YvMam_CSE9HLAp04w2j6iM-VAYsN5wmgf-4Ov9bNVpICx2RALo5_1vxZH04rwEavsd7uElnHpP1eFjp73cN7CCC4b6jQoIRk7qi_Q0N_OvUGNQMYDS0HLkS9BtTWmJkKgTVm4GCQcYKCnDG-6lQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f11c9456f6.mp4?token=emF8xPRYHQHjoFtzT8BrHsyFAYOZpyHrxbdKneSu4nRZ3enES0HHM7GNxp2p5CZEuyW0j65IC-hfBHKF7r2CloCecmgNllm_mt0eTxNYHn6sOJpASEPAmCcQWUXcVX3Jc1ugvKLg8kisauLxQtevqjdDLrjbtOxcJIrWyxem_Vwyp3cBY7w6lPlvIBn-u__Wjm7YvMam_CSE9HLAp04w2j6iM-VAYsN5wmgf-4Ov9bNVpICx2RALo5_1vxZH04rwEavsd7uElnHpP1eFjp73cN7CCC4b6jQoIRk7qi_Q0N_OvUGNQMYDS0HLkS9BtTWmJkKgTVm4GCQcYKCnDG-6lQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس فدراسیون فوتبال: در همهٔ بخش‌های فوتبال باید از هوش مصنوعی استفاده کنیم
🔹
تمام کارهایی که برای داوری و VAR انجام دادیم توسط متخصصان ایرانی انجام شده است.
🔹
سامانه فنی هوش مصنوعی ما برای داوری‌ توسط متخصصان ایرانی صورت گرفته است. @Farsna</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/455109" target="_blank">📅 12:34 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455108">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/591ff6e1cf.mp4?token=pEnfq-jjeJX0W847Gdo71z-OqwV9dZSNmZxC8FAZ6BaB2u92GFTg2IDb_sottW34SaNSE9fGZOaclUlW78SQTZ0_wzfUFdzGq8o6s57mTDusjI7jqYfD2yc1j1NX73sFaZlRzvxYN3GRlp2twGUfSWa6UNK82kkwgJ-G3vlv9yNdXOehFLGcLD9B2V8rP8_GvuxsoyZJFL3zVTJKP1F9SYwCsxZ_q5VhEL79XZSt-vzqMn6vVC4ccRnTSvNlkb-3WgTtv8N-VVwoZMl5cjb0QV5Hvmb-F4y5VxDgGybKlZn8A3MSDoooiQNXsbYwCUGyeR-yO2GI7k7u2irCyWLIvTug3xrBj2D7YVyFmymcmHHCvugucp2MLh1q5mLDS78jiNaiPcnk4oGABArVwdJahinkvYlj7_9VittZnq2nWCuEuJBhIfS10B3oE7ZW88ZXONS94gsqY8MrAbVuC5zyWT6n6suf4zhth14k6bb8WNw3N2BoPdxmq25y6dCu16QwmeOE3lQ9O9Xq81VrzgYq9-1tjBQeqVzpaxFlw1XRoveqeqXWJGX3VvNW9LuGpRhI7aYFdfcQ3QVxtdTD9UgQ2SAV1d5OYQk4q5SOICEbNm2sIeL1at5aMUTHa7_QPd9IVf_B-lYI_ejOT0cF_oYbzOpwVU3UstTX-_aooPOZ7iE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/591ff6e1cf.mp4?token=pEnfq-jjeJX0W847Gdo71z-OqwV9dZSNmZxC8FAZ6BaB2u92GFTg2IDb_sottW34SaNSE9fGZOaclUlW78SQTZ0_wzfUFdzGq8o6s57mTDusjI7jqYfD2yc1j1NX73sFaZlRzvxYN3GRlp2twGUfSWa6UNK82kkwgJ-G3vlv9yNdXOehFLGcLD9B2V8rP8_GvuxsoyZJFL3zVTJKP1F9SYwCsxZ_q5VhEL79XZSt-vzqMn6vVC4ccRnTSvNlkb-3WgTtv8N-VVwoZMl5cjb0QV5Hvmb-F4y5VxDgGybKlZn8A3MSDoooiQNXsbYwCUGyeR-yO2GI7k7u2irCyWLIvTug3xrBj2D7YVyFmymcmHHCvugucp2MLh1q5mLDS78jiNaiPcnk4oGABArVwdJahinkvYlj7_9VittZnq2nWCuEuJBhIfS10B3oE7ZW88ZXONS94gsqY8MrAbVuC5zyWT6n6suf4zhth14k6bb8WNw3N2BoPdxmq25y6dCu16QwmeOE3lQ9O9Xq81VrzgYq9-1tjBQeqVzpaxFlw1XRoveqeqXWJGX3VvNW9LuGpRhI7aYFdfcQ3QVxtdTD9UgQ2SAV1d5OYQk4q5SOICEbNm2sIeL1at5aMUTHa7_QPd9IVf_B-lYI_ejOT0cF_oYbzOpwVU3UstTX-_aooPOZ7iE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس فدراسیون فوتبال: در همهٔ بخش‌های فوتبال باید از هوش مصنوعی استفاده کنیم
🔹
تمام کارهایی که برای داوری و VAR انجام دادیم توسط متخصصان ایرانی انجام شده است.
🔹
سامانه فنی هوش مصنوعی ما برای داوری‌ توسط متخصصان ایرانی صورت گرفته است.
@Farsna</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/455108" target="_blank">📅 12:32 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455107">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5bc7ea0515.mp4?token=NChukZJEEzwhXVdVitW2ZGX-H3SdEGb4fNFq6WNF9T5BntIWzQAEaggdEq4UEKXEPRYNVlZgcM5eZeGmyyo2gZx2rwAAzGBcUZkr88jpqOALImobWEzKd8md8I_ZxLVMqBK8zvk_lrGgCEqlpxWqF3Nf1WgVSJdi_pYL6LpcgZh7FnR988TQrNusFQ0dEMQ9sD9lbFcy7hKgJZktphHcMpwZSwDyKN0TmbPoEzdn_Y451nk5WLD8OJNV5FA11DMk6z7M4a7iVMPIqfEL3QL3xnDK9NDw9_KFdzAE1sReNH2J7da0_WMJrRbECRcMxu_S966CyAGlNNsB2lyMh9y1lSU0DMg-0HZOLR14aJqKbQrwAXXMnfefvRkgmty4yIHfApHHdgprOGapVe1Kvqi72Go3ycCLaAQURw0EoVxR4s6UhWB_qiilru5YJW94gPIaVLKLtjXIl0HssIyRGPqNQwjrALppE9UDAmrMBebE3Yx05gcAgCMDDZYVx4IQvNJ1EK2azmHnt1y93gR3zcinNRhQ-U1LlhrYwwDyoWRn3KPU0OF_vsy1f4TMSFiBvse4lpGwh5QqztXpzZeSNiMfDraFsXkIb5s5xhJkBFZ9Xlquwr1bmAZOj-MtaYpNfjDeY_l6YxpVO_kp_VEwobjsMEKhNC6lbGGHmoEl1BqwTi8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5bc7ea0515.mp4?token=NChukZJEEzwhXVdVitW2ZGX-H3SdEGb4fNFq6WNF9T5BntIWzQAEaggdEq4UEKXEPRYNVlZgcM5eZeGmyyo2gZx2rwAAzGBcUZkr88jpqOALImobWEzKd8md8I_ZxLVMqBK8zvk_lrGgCEqlpxWqF3Nf1WgVSJdi_pYL6LpcgZh7FnR988TQrNusFQ0dEMQ9sD9lbFcy7hKgJZktphHcMpwZSwDyKN0TmbPoEzdn_Y451nk5WLD8OJNV5FA11DMk6z7M4a7iVMPIqfEL3QL3xnDK9NDw9_KFdzAE1sReNH2J7da0_WMJrRbECRcMxu_S966CyAGlNNsB2lyMh9y1lSU0DMg-0HZOLR14aJqKbQrwAXXMnfefvRkgmty4yIHfApHHdgprOGapVe1Kvqi72Go3ycCLaAQURw0EoVxR4s6UhWB_qiilru5YJW94gPIaVLKLtjXIl0HssIyRGPqNQwjrALppE9UDAmrMBebE3Yx05gcAgCMDDZYVx4IQvNJ1EK2azmHnt1y93gR3zcinNRhQ-U1LlhrYwwDyoWRn3KPU0OF_vsy1f4TMSFiBvse4lpGwh5QqztXpzZeSNiMfDraFsXkIb5s5xhJkBFZ9Xlquwr1bmAZOj-MtaYpNfjDeY_l6YxpVO_kp_VEwobjsMEKhNC6lbGGHmoEl1BqwTi8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
امیرعلی جداوی، دومین جاویدالاثر مدرسهٔ میناب
🔸
علت اینکه تا به الان اسمی از این شهید منتشر نشده بود، درخواست پدر او برای باخبرنشدن مادر باردارش بود.   @Farsna - Link</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/455107" target="_blank">📅 12:22 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455106">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RMFEMCJ-oReBPm4yqtX5UjvKjStOV37oxrd3HzZjUGQaU5RPO8Mof8oNIqWdB9Edb5ogt7S9TL6Ut4vjq0WaWHzvSpmnDrlEiNC54wYlanqyArQG7HebfAxCVRefltNOYzDTaBZOG-6sOj88xqMefDm1kjKrAY4V1MATm7UBBXfr2-KSSFn2pcVveBjXmfMw7LxH8N4ULEWiNddAdsHOeXSjr_QrxZgYRqoSLrC5RWkOcyYv1Wkf9xVKzUFYfSJ3KWdVu4svs6BHjLwBJETgB2i8d8aVVQqKcfqmVl9sYZ2-xwQsPPgXyI5R_ijFzbVtBArCJa3WYktJ5L1K0KTONA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دخانیات پای ثابت ۴۰ درصد سرطان‌ها در مردان ایرانی
🔹
معاون بهداشت وزیر بهداشت اعلام کرده ۴۰ درصد سرطان‌ها در مردان و ۲۱ درصد سرطان‌ها در زنان ایرانی با عوامل شناخته‌شده‌ای مانند مصرف سیگار، قلیان، تریاک و چاقی ارتباط دارد.
🔹
دود سیگار، قلیان و ویپ بیش‌از ۷ هزار مادهٔ شیمیایی دارد که دست‌کم ۷۰ مورد آنها سرطان‌زا هستند؛ قلیان هم برخلاف تصور رایج، گزینه‌ای کم‌خطرتر از سیگار محسوب نمی‌شود.
🔹
از سوی دیگر، مصرف دخانیات در میان جوانان روند نگران‌کننده‌ای دارد؛ در گروه سنی ۱۸ تا ۲۴ سال، مصرف دخانیات در زنان ۹۰ درصد و در مردان ۳۴ درصد افزایش یافته است.
🔹
پیامد این روند، سالانه حدود ۵۰ هزار و ۵۰۰ مرگ و نزدیک به ۵۰ همت هزینه برای سلامت و اقتصاد کشور است؛ درحالی‌که متخصصان، دخانیات را یکی از عوامل اصلی بروز سرطان، سکتهٔ قلبی و سکتهٔ مغزی می‌دانند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/455106" target="_blank">📅 12:01 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455105">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromShahr Bank | بانک شهر(El Nv)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lxzdU5WCsJu8N1zsbhRY2EtZnDggFXgOnC4MO8Ag_rYX-QlhL8F84T4e9POkH5OQseW12WTHYD5Bf1KzDsJqyuF8yLD1L-QgyOU7CAyIIgEnzYSbCp475_qoZDjIczd3Zxcy5cRB_GcwoNeLjZQEXGOtIDsomGB2sPIhHGPmGTF-JDO7vVZTpJgshZ3HSrfccpfGDcRRhn_cteU9k7JMiuuJtdx2ujYVsdAoqFtXYCV_ks3laAJogdww3W7VFk2Qo-i1HBR5Gi8HnhWmk1pikUUZmk_p1W1ZIeHeDZ76Sn2oqOekOkrHHE4VaMt-wvtM4j8Yzt_8XRYdcBLt8CtpmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭐️
موافقت صندوق توسعه ملی با پرداخت تسهیلات ارزی به صنایع آسیب دیده از جنگ با عاملیت "بانک شهر"
◀️
مهدی غضنفری رئیس هیات عامل صندوق توسعه ملی:
◀️
صندوق توسعه ملی با پرداخت تسهیلات ارزی برای بازسازی برخی صنایع آسیب دیده از جنگ تحمیلی اخیر موافقت کرده است.
◀️
با توجه به درخواست های اخیر برای بازسازی صنایع آسیب‌دیده، صندوق با درخواست پرداخت تسهیلات ارزی از سوی  بانک های شهر و تجارت که عاملیت بازسازی را بر عهده دارند، موافقت کرده است.</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/455105" target="_blank">📅 11:59 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455104">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nmMTAXdbfahif8OM9U46xr-urq8jby4z4raQjGGRSGtBb2SH0x-YjkQQ-17a3scpw8UtCAnTOnSRbuzdPCDVFpFEiHFOachv2kE5nZEfTODHMYEDwPl1oNwcrKraDH9yJxP-t7-duu7z2aV8eDTx2ActgGMGIiKLHOF5SeAb8zUMEtQJc3X2daLiSTOjkyCoXaDjwEgoc4KlICVPYefeAGgSvckQW7Sg72MAiuoeJIXIzkh8YcFWRFbbl4Te9mK38RkckhdCZFPVLv4dsz_ifAerMZlnKUTLLS8hmlnbH0jJdoKEyfQTgnIBH8VyNbk-mIGj9Cs-Upc2YP-fhxoEQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه حال خوب بساز...
💦
مرداد، قراره هر بار که به پارک آبی اُپارک میای، یه تجربه متفاوت منتظرت باشه
😍
از بازی‌های گروهی و لحظه‌های پرهیجان کنار دوستات گرفته تا هدیه بلیت آنلاین و برنامه‌های ویژه‌ای که فقط در مرداد تجربه‌شون می‌کنی؛
اگر دنبال هیجان، تفریح و ساختن خاطره‌های خوب هستی، این ماه بهترین فرصت برای اومدن به اُپارکه
🎉
🎟
برای تهیه بلیت، همین حالا وارد سایت شو</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/455104" target="_blank">📅 11:58 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455103">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/455103" target="_blank">📅 11:57 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455102">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q0jylYTTeZ36BjL_8E9fjViyWimY2t-1XxEO7glKo7RQZ_sCe0Qb-uKbMbQWMGVHxCIQ7vi5nH19Ef8eOtT5WkG-0N5B2aepFJMoD9ZDpoEYgwTIjm9UAaBMu8QrN7nKQqgZ4TA_E7wW85fgZxRCu0nxfCD_w2ilZFdKW7OKkEz0nnOG2TdpLGVvcCqYXqw3fJXwUtsyHJt1FnzsNpZH1HgxX47TqlB51K0QmtfDjnWEgcfVrFradCxDOfOYNffV8M-4FGP2Y0-qUac5wLKN8B6dftMAqWpnXphqgKgKhxTm5z588XmCcESQtkg-yuMlKq6cckBF8eNqZZX2pPYZQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دبیر شورای‌عالی امنیت ملی: تا آمریکا رفتارش را تصحیح نکند، تنگهٔ هرمز باز نخواهد شد.   @Farsna</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/455102" target="_blank">📅 11:53 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455101">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">‌ سخنگوی پلیس: نفر اصلی دخیل در قتل حمیدرضا رجب‌زاده دستگیر شد.  @Farsna</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/farsna/455101" target="_blank">📅 11:40 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455100">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">متهم متواری مخل نظام ارزی کشور در پیرانشهر دستگیر شد
🔹
دادگستری آذربایجان غربی: یک متهم متواری که تعهدات ارزی خود به میزان ۵۱ میلیون یورو (معادل ۱۰ همت) را رفع تعهد نکرده بود در پیرانشهر دستگیر و با صدور قرار تامین کیفری به زندان معرفی شد.
🔹
علاوه‌بر موضوع عدم رفع تعهدات ارزی پرونده فرار مالیاتی به مبلغ ۲ همت نیز برای متهم تشکیل و در فرآیند قضایی قرار گرفت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/farsna/455100" target="_blank">📅 11:37 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455098">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🎥
معاون امنیتی وزیر کشور:  ابعاد مختلف قتل آقای رجب‌زاده در دست بررسی است و نتیجه در اولین فرصت اطلاع‌رسانی خواهد شد  @Farsna</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/farsna/455098" target="_blank">📅 11:15 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455096">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/niVf7A9hb4qujCeHRJjyQIlFx0paZoKjvKiv3T6FqhUOIW5DG5TCjcaNaYIvRLB1kCuC6PT8uSFJzkLyX53T2h3gHZ_d4uP1Iv4nJ2G9XEoC63DUFM8PAtcdgD0DATc2jS4oKK0CsAIffJoSz4n98nNlQ85iKfvc9c65OEw9zNte0aBDOd1cjRCEl_gszMrs0ZaljOwCDWZqRYUn-3GE78zUuG98l4SUi-YoT4fCBkiivfwflFOwztcg_iq9m9CKFNfivZuNK7IKWfAnBV9WXj_Zb5kFF5wUzAV8wSnZQP-kJnjUD235B2z3LUGF-l70dWgztY6-_at9UTtTgj9oxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشف ۳۳ سلاح در مرزهای آذربایجان‌غربی
🔹
فرمانده مرزبانی آذربایجان‌غربی: در عملیات‌های یک هفتهٔ اخیر ۳۳ سلاح جنگی و شکاری، تعدادی خشاب و ۱۲۲۹ تیر مهمات کشف و ۱۷ نفر دستگیر شدند.
عکس: مرضیه موسوی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/farsna/455096" target="_blank">📅 10:30 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455095">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🎥
آتش‌سوزی در کارگاه فندک‌سازی شهرک نصیرآباد تهران
🔹
سخنگوی اورژانس تهران: درپی آتش‌سوزی در کارگاه فندک‌سازی شهرک صنعتی نصیر‌آباد که ساعت ۷:۲۰ امروز رخ داد، تاکنون ۴ نفر مصدوم شده‌اند که از این تعداد ۲ نفر به بیمارستان منتقل شده‌اند. @Farsna - Link</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farsna/455095" target="_blank">📅 10:24 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455094">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k0FFtn1g5FKn0Pb6RQUBIxh03mKwmBhEvd585pFCY4IrgOOAKuJoGQaTYfWV4p5ItnBrzJVqdB4HOgbbJYihNrOG2fHse7CZLN8D2JCpkVeM7T1STQwAspIEIjjwkzP7yIeTi9dNMP1Yr0f-Wx2B_OqNFw4Wu7W7Qm2iW06JwLWjhw7NtwaLQfm6iz6w_5stkWiHxj3KKbMcP5Mv2IyFATGYdyUZafre-E8o6r9ogfb5XwiN58uovZP-y2lzdfaGFP45iHWa3M7O0cAONl83C86qkxtVIPrEFjFPKfjDk6ep4lMIInS-20mAVmfEgLLFai9ROdHhY2LBsYH--hjTyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سخنگوی نیروهای مسلح یمن: با توفیق خداوند پالایشگاه آرامکو در جیزان را با استفاده از پهپاد به‌صورت دقیق هدف قرار دادیم.
🔹
این اقدام در پاسخ به نفوذ پهپادهای دشمن سعودی به حریم هوایی استان‌های صعده و حجه صورت گرفت.
@Farsna</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farsna/455094" target="_blank">📅 10:18 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455093">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Iz0KmcS0Jp59fX--Yjk7sSYf2UtMliLw_raNzT8LQlMHH9I7Sdm-smL9_qWbntguSUPcvp2_yNR_u40FF6KFEzczY-ZvjHN3PbNsv_2Xi0SOtGnMGCyrgKVDWk_-2RLAIuH1qnCTx8VTmrMpBq_32XKLvaWBTGaVhyCHGNShq3ewao2ScoJbY7CyL3neqh1cI-onJQkO5pK2CNCBA3FMWMISfAK6lkHvwwikwGYJDJQo7iAPHOuiDIqQ8YFF_Q9mfRrSsJfvUmgV8lyOfUr0di6U627JU7kEd5bx-WiSuCzMZGPYMN78L300EfW8fU8zcT7gvh4ee25j3vasKq2Vwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پادگان ۰۶ به فضای سبز شهری تبدیل می‌شود
🔹
رئیس ‌شورای‌شهر تهران: قرار است پادگان ۰۶ به‌عنوان فضای سبز شهری مورد استفاده قرار گیرد و درحال‌حاضر برنامه دیگری برای تغییر وضعیت پادگان مطرح نیست.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/455093" target="_blank">📅 10:12 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455092">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CIlnGXCx1sgnHAfqVLPNHzyChuqeu-O7tSKZf6yfRbDH2UMa1RLJme4Z8IzxCl9koj7V6PbsMHeLGe3-qiC52tZANP1urKC0RJKirLcuTn8jxnmITCmZu4_n3U7o2jyHS-u4J8y8GFendwCOsPItfZ20CkGc4KtTWeZtLQylerAtZQj96LHiKZkcxJ146VUqImfJ3YK58x4M_nIvWvVly8VrQ1mfxHFSansHWfkIGkVrgjfIMsVIUQ3iytaPDlijYL-uP2RIsz_Qp4l_GBmTgvJbT3dHSKdUW59upZ-ACj1D5Bodd755oyVH2NrLLjp1MJkwButao4vUctxObZSr4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انهدام باند بزرگ شکارچیان در چهارمحال‌وبختیاری
🔹
سازمان حفاظت محیط‌زیست: درپی شناسایی مخفیگاه اعضای یک باند بزرگ شکارچیان غیرمجاز در چهارمحال‌وبختیاری، ۴ سلاح شکاری، مقادیر زیادی فشنگ جنگی و شکاری، یک فشنگ‌ساز دستی، ۲ کیلوگرم باروت، یک مین ضدنفر و تعدادی از آثار و بقایای حیات‌وحش شامل موارد تاکسیدرمی‌شده و پوست پازن، قوچ وحشی، گرگ و پرندگان کشف شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/455092" target="_blank">📅 09:56 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455091">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LAFMfmUExZpPtfloM2pvoOM3f7t2m-K060zsomHo1X4ne9hkLzu7Sl4arOhTcJecUA77yOA732nRkfYOP9Y5Pe5oRzxKTiha7z1_1XYa3UicKiQX9RCBGXC_kK72QNhzptHWl9pPhn3jEc0MqAxLi745E3MN3OBRPP2XPNJx0doBzQG_F4_Kaj8juqUZthsdol8T2ozVBKxt_f4X752eFFmrrIL_YswBsF2KDZpyg7uryf-ljHdwwMr1fV6uyQSwhVu6RkT2SzdTeklKAYeZ6vdUGO_eOaZLPj9TdEsWb86VXJ9ccBJ6zEBRbw_aq_v2wG9MgU61vDp5AsQjeXDWkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شوک شبانهٔ تراکتور؛ ربیعی رفت و نکونام سرمربی شد
🔹
محمد ربیعی در فاصله ۵ روز تا نخستین دیدار تراکتور در لیگ برتر، از این تیم جدا شد و جواد نکونام هدایت سرخ‌پوشان تبریزی را بر عهده گرفت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/455091" target="_blank">📅 09:43 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455090">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cfb9d5ae3b.mp4?token=XVGzaJ_81VB_xPsRtpxHjUKKjUgE57pbN7Vw9OdlI_dj9rt8WpYQ9Xh6e3zZvqnoUILqgmJq3nRW5blv4WiMbmK6wo5jX720aZfTP-KvQykwU0W_bM6ytoPD7DWEqIVD9u8eiHUVZDdsw_9cxQ2K5QO88lp5Ni99YYX4NTmza3xca8UJ6uPVZOvZkAGcFzpWWxqms5qfUMeuvnlckhgb9hM94aS61XEMSFoBXd9N3heICST-RgRDWFqi6H4TWQJAek0AZy3DmaeLQkts3A7ad5zjGGp5Ax8P2Lvo2JegnVHUpVUMlvsYrrG16_lPxaGO0InutMZmCGyyHCvtFG7Kyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cfb9d5ae3b.mp4?token=XVGzaJ_81VB_xPsRtpxHjUKKjUgE57pbN7Vw9OdlI_dj9rt8WpYQ9Xh6e3zZvqnoUILqgmJq3nRW5blv4WiMbmK6wo5jX720aZfTP-KvQykwU0W_bM6ytoPD7DWEqIVD9u8eiHUVZDdsw_9cxQ2K5QO88lp5Ni99YYX4NTmza3xca8UJ6uPVZOvZkAGcFzpWWxqms5qfUMeuvnlckhgb9hM94aS61XEMSFoBXd9N3heICST-RgRDWFqi6H4TWQJAek0AZy3DmaeLQkts3A7ad5zjGGp5Ax8P2Lvo2JegnVHUpVUMlvsYrrG16_lPxaGO0InutMZmCGyyHCvtFG7Kyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آتش‌سوزی در کارگاه فندک‌سازی شهرک نصیرآباد تهران
🔹
سخنگوی اورژانس تهران: درپی آتش‌سوزی در کارگاه فندک‌سازی شهرک صنعتی نصیر‌آباد که ساعت ۷:۲۰ امروز رخ داد، تاکنون ۴ نفر مصدوم شده‌اند که از این تعداد ۲ نفر به بیمارستان منتقل شده‌اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/455090" target="_blank">📅 09:30 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455088">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/34b23b31c7.mp4?token=i9PiFW3vNEef1PXmekMOLuHTM48sIkDjmp47z3k3e961P_t__xpMrg2lzHQFh0-Y2-U6foRuKPGeHC2ekLpQRaXAmiHfGlrpTHv0dX9brzKYpmnddforaQoWFAG6CWuwdUFgtVKbdxflG2hoqePz66Ljbtx5lgia841FVuYRj6ZiSuNwttbDMEOWdaBWXwtpDBdFkmeAoXGeJhZLiKtptfIAlyA7tTNwcOaEC-AhGZcndMrF7PDlqdDqaclzurU5fv5hmSjEn9cxCp_bpkGZM6TzBsRsYC9Rmc1ncO4Onk7aHOyPlwGWzirZ0iVu_oz9vWZalVq4CAkUR_yu6PcCHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/34b23b31c7.mp4?token=i9PiFW3vNEef1PXmekMOLuHTM48sIkDjmp47z3k3e961P_t__xpMrg2lzHQFh0-Y2-U6foRuKPGeHC2ekLpQRaXAmiHfGlrpTHv0dX9brzKYpmnddforaQoWFAG6CWuwdUFgtVKbdxflG2hoqePz66Ljbtx5lgia841FVuYRj6ZiSuNwttbDMEOWdaBWXwtpDBdFkmeAoXGeJhZLiKtptfIAlyA7tTNwcOaEC-AhGZcndMrF7PDlqdDqaclzurU5fv5hmSjEn9cxCp_bpkGZM6TzBsRsYC9Rmc1ncO4Onk7aHOyPlwGWzirZ0iVu_oz9vWZalVq4CAkUR_yu6PcCHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آتش‌سوزی‌ها در جنوب لبنان توسط رژیم صهیونیستی
🔹
شبکه المنار لبنان گزارش داد دشمن اسرائیلی ارتفاعات «دیر المزرعه»، «کفر حونه»، «نیحا» و «عین التینه» در جنوب لبنان را به آتش کشیده است.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/455088" target="_blank">📅 09:23 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455087">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">اما هنوز هیچ خانه‌ای تحویل نگرفته‌ام و هیچ مقام مسئولی پاسخگو نیست.</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/farsna/455087" target="_blank">📅 08:15 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455086">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p6nLSGBgqXUAxPkLtf6hxCYsVfDgHoZadQBOf9RYILhUytJManl1dOVKHn5iKOnkZYop_5k_ZkunVr29dLaqdkkVRXocjq09XCYyLMQLJc93mTkLvFTIdJr0U78f_38s9xbtaCA_bEQ1-kNiIlsk07VE2Z7dtEJwfUzgXuE0ZWbEGWJeBRbNS_kUer-w6gIr3ZPVBGLdkiReV_3MPdrbfhxye_3aMZkxSTtB0xyl_y31omEfb_cfFejkskI3AojMzvEz_Ed9XAT0aVruFQ1Of7QNN2F_ApTEji3W0Me8PwYjkAYGJjfOFwZAiO5z5yySlHsjpeA21S8pCJfzwa_AIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پرتودرمانی بایدن برای سرطان تهاجمی پروستات
🔹
سخنگوی جو بایدن امروز به شبکه سی‌ان‌ان گفت که «در چارچوب برنامه درمانی سرطان پروستات، رئیس‌جمهور بایدن هم‌اکنون تحت پرتودرمانی و درمان هورمونی قرار دارد». او زمان مشخصی برای طول درمان اعلام نکرد.  @FarsNewsInt …</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/farsna/455086" target="_blank">📅 07:43 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455085">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z7mwjZ2eDtjmon7J8-zqb3QQd1_yThQIEb6BPNguQ0zY0kJxUCyCiBrorpoelc3UK-yMCHx7nuaA02wzdj6WeqtIEo7wF-ZOSkXcxEKBDvrCpT7WIu5VwHF8QfWH7ttMJ0QqKBZEkZtjblPUwbYk4CRcQQT9qw-LUi5K41vLz7zJLjFTXcizY_9iZbor2YR9fxuZXRoerEoOEy5MlxNsO5qyVvLbJUJ76rvE4t_lNZWgSHgoh06M76EIBjTkrkBH2siJoTadaWxo1fiySfC1TlOteq-mk5DL6xbYzgVwyvJD9p-ZgM8L1UjPiWBi5_ygckeKh4c91Kfy8b9NpNYeug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
تاسیسات آرامکوی عربستان منفجر شد
🔹
وزارت انرژی عربستان حمله به تاسیسات آرامکو در منطقه جازان طی بامداد یکشنبه را تایید کرد. طبق منابع عربی چندین انفجار در این تاسیسات گزارش شده است.
🔹
همچنین ماهواره‌های ناسا از انفجار در نیروگاه گازی بری آرامکو واقع در جبیل در شرق عربستان خبر می‌دهند.
🔹
پیش‌تر نیز پالایشگاه جازان آرامکو هدف حمله قرار گرفت و بیش از ۲ هفته می‌سوخت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/farsna/455085" target="_blank">📅 07:22 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455084">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">منابع اسرائیلی: ارتش اسرائیل خروج از بخش‌هایی از غزه را بررسی می‌کند
🔹
شبکۀ ۱۲ تلویزیون رژیم صهیونیستی اعلام کرد که نهادهای امنیتی این رژیم موضوع خروج از برخی مواضع تحت کنترل ارتش اسرائیل در نوار غزه و تحویل آنها به نیروهای بین‌المللی را بررسی کرده‌اند.
🔹
یک مقام امنیتی اسرائیلی در گفت‌وگو با شبکۀ ۱۲ مدعی شده است که آمریکا «گزینه‌های زیادی برای اسرائیل باقی نگذاشته» و تل‌آویو را به سمت «مشکلی در غزه» سوق می‌دهد.
🔹
با این حال، این مقام اسرائیلی جزئیاتی دربارۀ نقاطی که احتمال خروج نیروهای اسرائیلی از آنها مطرح شده یا زمان احتمالی اجرای این اقدام ارائه نکرده است.
@Farsna</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farsna/455084" target="_blank">📅 05:19 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455083">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">پنتاگون شرکت‌های آمریکایی را برای تولید مهمات تحت فشار گذاشت
🔹
روزنامۀ واشنگتن‌پست در گزارشی فاش کرد وزارت جنگ آمریکا در پی کاهش شدید ذخایر تسلیحاتی این کشور در جریان جنگ با ایران، به شرکت‌های تسلیحاتی دستور داده است تولید و تحویل سلاح‌های مورد نیاز ارتش را به‌طور چشمگیری افزایش دهند.
🔹
اقدامی که به گفتۀ منابع آمریکایی، نشان می‌دهد واشنگتن برای بازسازی ذخایر مهمات خود با یک چالش جدی صنعتی و مالی مواجه شده است.
🔹
به نوشتۀ واشنگتن‌پست، معاون وزیر جنگ آمریکا در یادداشتی خطاب به مدیران صنایع دفاعی از آنها خواسته است حداکثر ظرف ۲۱ روز برنامه‌های خود را برای تسریع تولید و تحویل تسلیحات ارائه کنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/farsna/455083" target="_blank">📅 03:43 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455082">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dJt5O1pGvVzQ8BClNMnPk2eMMJHKC0Jawy9_loZrcjmkgwfvRHEF3O6B-BPzVD3hYnUjI6foR7zXLEMo0tTIAM4RANzBObyWjbWLkkBZYsj1VbZUz1PDy5ZkGGZUmBRReSom7uKhYhGASvuH6eK56KW117R2nUa75uTtwDLe09Vb8GDpH2uUWnMo6ckuFjavqjlLtluV2iVN4dxeHmp8yruncjoyev7IeFJHwnCf6iJ_-1VJySOGS447oSBQMfsK6rCxt5Kp3Rk6TWrgO_LK-Q0Why6eCUbgavdv8MsoyxV6LGMYowidBE60Timmt1rjSltupFKvMd-kEAbIoFm-Wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زلزلۀ ۴ ریشتری در هفتکل خوزستان
🔹
دقایقی پیش، ساعت ۰۳:۰۸ بامداد، زمین‌لرزه‌ای به بزرگی ۴ ریشتر حوالی هفتکل و ایذه در استان خوزستان را لرزاند.
@Farsna</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/farsna/455082" target="_blank">📅 03:31 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455081">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/joNa6-ZuGWk7SBmbFp6_C0N41c_vQIbtlxo2hSiyqSZ7LWSL0-kOFFLP-2rlYyNZQUX8UfDuNxd6A53s3CrLS11dL0-qAHIujM3Eu3siZsFm8MJiDMDK2arjCVrLoDU5AMv3o-WJoJEP3rASoYKoLk18ndriqlqTCSD6b0swF_i__cINxvj46LX6lEZsiPjRcMb2cIn8wAgv_InuvdIgn4KT7sLKPsJUsGyQ7-ysq8FgQMhpXOSqu80lPkav_Wycua0dLke7mBxnbgUPTxk-okHlryKyPcf8MJoLQhcpCWmDwDN4TVsnbQKQR8DgWNjoZxcZdgNHZmUNyf7qhtM1cQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر خارجه ترکیه: در مکه علیه ایران ائتلاف نکردیم
🔹
هاکان فیدان، وزیر امور خارجه ترکیه در مصاحبه‌ با خبرگزاری آناتولی گفت که ائتلاف سه‌گانه مکه می‌تواند گسترش یابد و علیه هیچ کشوری از جمله ایران نیست.
🔹
او همچنین تأکید کرد که ایران «هدف» این توافق نیست. فیدان افزود: «آن‌هایی که به کشورهای امضاکننده توافق حمله نکنند، «هدف» این توافق نیستند».
🔹
فیدان همچنین ادعا کرد که مذاکرات درباره این توافق پیش از آغاز جنگ میان ایران با آمریکا و اسرائیل آغاز شده بود.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/farsna/455081" target="_blank">📅 03:22 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455076">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fktZx8srXo8xioVYcs4TpdORuEhw0q_ynNTmzAfqEBsdIb7-186U-BPAA_SpxnbV_YgVXq_VlJCxSjxdu2ldJV6_Kr5vhVz_amazdZ50JYOfPQKurw4ur3OyAN0Zq5GsdPrREpLf_L0K0SlBmXEC81dOpI0GQfjkO6ZMtH-TN_I80wduMyHlvTPh5DrKE-rOvtAowC7BZHnMv4N9UsGTjmMSxzC-JXYYudRJK6lz7ZaB_1ZXVIJ5ChZ4BGYa6uImyp-730XXu60iY_IUqqNjmylSAe9tcyLh5RyQfN_tEZugVgXlynVmQdaqbx-8kVUR93FaeH_-d5Y4qCW5Lp4UUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SvyPnJNn7CTLxpTkLs7jZxVJne6dQcDVsM3HyvYH1LDoeDXVyzar3Vsu8SW209Ee6TM08Qpjqxc6sitTwoZ7zicA9KO_ILcS9TYPs774cmO7-uVV-coAntX2YaBvuTfiCmeSSCYzNgVdV6rzHJvBLXdoO-c5UDopTGESTbqWDhws_8TDtUdEOw1sz03ELDIjqntR0QmjRyyLEfKTIjU4YKLbHK2GOPvjdIsOtdh1gUu1QzUerwvYMJ2NJe_MK9uusVccJNto8vN6thr1IbIV5oZRL4acroLL1hUQvb3_WDRqw3tSU23KCgONINLJINWltHADan9DimkaxnzinQxWog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YCVFxNr8X8KCunM0R3P7VsMRfRW9GyaivuEJql9QmEF_Xktok1UBzKmnvgxL9d2S-BNSO-3aCHFPX2dnZ_sH9KittkY2YJiW3Vl9oC_rXBqkcXrwsK0c5eK7rtMBa3z5jXUTognv9KFkk-SLPHVOpjrME2vKWXHu9wJBuwMWqRip8qarJkf4h8lO6xRbgWmsatum_U60acdUlEKkQTgR4G8TnSygO7t69vKsDFirkuvVGkJQd4Lg6tniLO8ZL_QWA4Xnzx-25IsBneA9lGxHlRQk3BdYeV8zLJZAg-I_DL5zwoYDyr28YPMNReY2jiaZA65bczqA-ejKMzqxihaJhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JuUY_3hIR_PQVbcmbdeSxZS4izTytx-gePrcerpTMn3n7ahc7lGOlkyfuCRhtG8Yee24Owf1GfINBXDkCAwsLpHRReE76jBnJlY5RL9a6eBvnLenfCNFNBRiLWkqlT-kWwoAAHkuKj1hN3SjRE846JtIDZf26pF80cpDiFAJFbwPVv3gddMkwXCy2otlggY6T7sE10SxWey9pA2S023nqyNkMAK4lEM9oPum3-syFXSSyCJymIBekPZTRfvQ44UvSXEbG2x23lhbWUwPyvp4JFthNkPnVcQgQGWbIx2RJ9gXr0ZcBiUYY7-Kb3scM9H8qYEk0aKfqWM9gNFK93FhUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vm4Go6imW264IjbnAJRQd_ON4bXBIXoqrsg1a1Qa8ZJnqxXtg6I_ZDNyOhkyW44INiQ104HbzZzm5X7abA7mV82ed-OT1YQXGmU9EP9JVwY1dnzKPa7nfSEJH1TsuohZvoZnCZbUIS-ZC4TWlkpQxZ-5jyImufDv1Cr22XiOlNYBwI0Ng3d28jH_JbTDk9KoYL-4Tn4iWH_pxtavhs5baPWZSu2Cc7Scid0KDcFcCkU4rZgoVCUR5NaJLMvSMAAgG1c1i0UwvfSwMNTEmB7078o_rX8IwUdwTLdeOSH1JDvRr0KMsHXQK0k3pY-SxHrQu4yg5phmwFyX6vIcbp2k_Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📰
دکۀ روزنامه | یک‌شنبه ۱۸ مرداد ۱۴۰۵
@Farsna</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/farsna/455076" target="_blank">📅 03:20 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455066">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/o2EM5UNjokTXliXkbAX1z7bvHLYT_-RbCOvsEE9uo4CISJOGClkZExdA_BJ7nvB2S4SDvdUZhqSmPqjgzDafSXjskloTWiNl3ArGK_dwF8FEBFcZts84dGHsa231EsheoGTlkeQZrcxAD9p_O-RperEeVhpKmKiqVT16Xu8aCqwcT_GSj7xdA8E9wZydfWImk0P4cF6SjjXB15WdK8hBspUHDOgRolWka0xKL8Sv71-ozSCsyQgKrFPWoJtYnlMmey_pct5RndC6X2iwlumsZuHbPW0n-Yeo4QJGPwg6UKrMr1deMH4vMJ2a3WHTuCDi_-IogcSSflw_pH3iYJS9Fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bMmHOY2JrIABhkSpgRD_7gxB5GGW5K7G50HFnkgSEfCoI0hJeiAdtYOOzlW3lWLwfRd3tlobotp6FzePkY_j2PRF_zlyoUGpNt1Hk0M-BCVqbhD66NAlvRJnTMZNu8S8Xg_eyy9LHz-1PqJRY_r1y1Q95CnvWx9aYHAZeTlIWBKjp28TDEpW7nti95Fv1p_ywajWr1oPUDk-ISxQi_YhzywWrKfFFTbkfTuuRDC0PS15eIj6yQK_sPuU5NysFtKH33cg62xFZpsGoigAhB_PmghEdZHqsU5p5MTOroCm40vSz7FLtxVGaC-eRcDpxgEV8oclTeGWn8uh0-bgBBFzDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R4moAC8UkERj9F4Sc6oOJMMfPk5twYV925p8-tEImik5PU0ke5C_X0XHSxKZwFi1CU8m2LirwDmVvxB3-tp-mBCle2dkKLZ1tTutLhRvcAP0eChHh4QMfAicOF8TJue2c8_qEgqp1SYS24ehyrKvpStfJHGIWD53sH22yCF2BgxaDcTzk3lPhRlqNwYbcaOGUFQiE9Yc6nAmZnB5GYE-f7lPzcmxY3fJgQBYHcsCOY7oEdP3Chsa-gIArJ-VmFWdT2rakykg_OHn1WnQV1BtISTVz_iE37xIpZemge6yuoab6a6_SF0puY3hKlYjlkuGCKuGn0B9AXUr93LVL0gB5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sWLMSj3QcU8zJeuC9kjyVrP64HmrGhxI0ayiR8QfG6-v14PRTC-VflE1Ag9HXijcQyOUX7iYefYv8Uiil3dftf3ooqGq4T2v9RWdcaazpLBv6uWW_TZLYT1iKQl6n39n0W6VdqR3GmCWrhpYZs2P1Qpu6G8E7iQNgvbAI_2V2wiaJUoVp2tt4O8jNYW_RQMsmx7HPI_AdjADas_K8DNrbJlJc2j1veD0HOYzzk0ZbDGbqIuq0jYzx2oZERfGqdlBDI9u4-uffbsSRx1pmnWrvDO6Ewmg574R8rcqPSE_XvNe-z29240Pn0D3EP8RCc2br28RUPvMl6vwNXitNH6aMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GTPFFKwJldyj_LCqlRboQvJxW0hlWTITlmQqGKx-DXuJlOoNP4cOSjojFdFk8Hde3hpVP_WENBciYQjs8Dj7d6qALCxgCIEKG8qiqohCsDKbeYHjKpcZtokq7PqIEBXXFTAGRxArCr7LjvoNDx69ovI3swxBurXBwNQeMh1bMeQipMbFO5_l5J1btZv4SUBrZ4dIgUw_0xWvOz8KKCtcnDOdn5Mwb3ig04lEkwwZbkOgiYtT4KJ56fd9SrSZk-hhHhUmf4cilXIDMURihkGu3J4zFKfrYcwWRIkcmV2h6pfI5ln0xT6xXbUZzcm98UFPFjYH_XorF6Hwi3phGlZVOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/emNTHr0wrdE7b7uHI1MLxccFzND4uVDw8Xlbk19vkEm86kA85hd2JccbuaoiK7K0zeOaFAoaWImIrII__se0rE65Po-bgb0tu5vd6a3UXwD0_vhi5DC4xVHO71fljG45afvRAD-LfMmgSWbMI3H39MceM5SaLBO_fmm70HUoq-VkYldOc9SsF0PbgczILem6iy6VFcL8ydYnY2jd73FcdcJGeBbr3m18vGBPr3oWcu0DaLIY8ZR-VzYsF8lsDrgQwSQUumbDqmuC-dbu_6BR6wJr4xiIeLatz_FUyyOHzh3VGMjB7E7t0kFxcmB57jI2wzN0PrXgvKY5tRK4oghOdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UK7l_RrPfdZAnzj7in8mEVjpCDQC5BunJLBPHzl708IeRy0E-TVTRB6WSLdlW0cn6K6Y4JO-7TihHdkFfGWhKj4TodFHpBmlQqZ2iAn0iTqnau46sOz1qz7oj2uJZ0i3nCsTJ6BCaClV13Z24FU20ZagWRtgB52bzq7P-7DM8zmMwyJ2dLUFzvZVx2PPygRJzRkQtooR2nxbUDG_tiE0oAAF3VnHJjSkvhz1XakVcwVLUTj7pwwipNr_cjVWydOyi-c-5X4d_ZYelAzWCKKx8HQXuaX5CPIbfQ3kDxqQmBsKVWdgyVytuEx03nphSqchxCEAiHXEodRD5Iwjtk-HsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B1F6-HE3XXApGji-VlGed9s4lUswnlll_lH7ZrzShoMB0DqHTfNAFktF8WLxB3DXIG_gc-cO2NlpFFvMDdy1ELx-BYmzFc9N5mGMgX07jT3t44Qt0TklfgLVuKEgUJW_lEry9u2jEbwvr5-FsEiUcSEpwpKRSXUC1j9OzyogaUHIUI4d0vHNXAyUSnDna0NCtfueddJa1AqhZMHOshCPeuWtyGvrxI8fFeOybieQ86KaUkFk6oEapjB40FI8YMNMl4iGMbctXtQJZHfL1Dyc4abfrlihbXXDUD__iOvGd__CY9WggesT55xijYxOXvk_G8ZC6KNJkjJvSrsoSiFyFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/m99un8xEirRnmDMp0viwYeXIml3_J5Rp_YgB8rQVqEoqisTJ9U5Hst9j-Kr_Cq0tN_b3U8W-QyCbA0Xybnjs7wj7HKjJJaIJfndKMif2FnpXmTmgF2pxlSlvS7aMYEEG_zKKUQyHYxviT-FWAZLHurO4qGATluuWaBie-WWQZvP28VPnMT88Z56tYiq5faxUcY13oxOqd2ZICZbJrSqUEv-bsUc-sgb9Qx_QFXSlExHUs5sA7SLE5LB9WuWbT_KcQbTAxb18lbTx5TBLwZWYkBtXgoqiYuyjiwHMiSoZ4_IPM2S5Ryw01b9gSLXSj50tbqAvBsfWK0Mpm2ScjqoJ_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ix0R5d4WYnLP0Y437H3Sq2Eg6SOiHpJkkcpujbiEmT_0DmoH1hqHnyXszSlUR0eONr1IsAyGUfGUj-yC7XDbjnavwSErb3lTL36HXDMW4wqG_x2XV_vc4ydfB_6W3a64EJVDoGGhZWMEJ0KUhTuFPwabJNcgiqubTHeeaymLHEPR9DrLwGvneILtEvA-9Z430ecMvj_Zr6gMorlIc1olz2BYIJetZwUGv4-IIv2wXUTXUTun0WeAduXNEZY4Qsbgup8HEGVpB784u8J91582-jlhrPOv_b2VW1w53_9IlESN2nV0o_2TdCc2pmJnjCrga6BihYFGWIFLFvGMmgm99A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/farsna/455066" target="_blank">📅 03:20 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455065">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pZ7eI3gF2PD7K4K69GrJUyiPcPpoaUBXPXD3r5e3nJEvGAJmjJ0aDmkr6bWFwfzKHCP-m8uYaDC394H0ocK_HQRkenejdfU7ywT_49MBp3USztxsVa4X0AJ3VLeugrNYKWbRzHABFtJQZjRQC73A0AI7-W6iLTbbmIGSRKX9uIhY3XLPj5h5Hs5Z_Xr3jpQlm79HAT39vo9-9m_orSwI2HY1Rj-eaXUvfQVCJXeDcWZ0XFJL1ekUr3oh5rN5gZBdepCaZ1ylLn42-Ok6q0XHy_itnX0CG_LiGupAXHymAcj-r3V7PIaPHLORQd0ZjiDAJz7pMFc6kHdwebL4NuU3PA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنگ‌فرش خیابان‌های تاریخی برچیده می‌شود
🔹
طرح سنگ‌فرش کردن معابر در بافت مرکزی تهران، با هدف تبدیل این محدوده‌ها به پیاده‌راه و کاهش تردد خودروها، یکی از پروژه‌های بحث‌برانگیز مدیریت شهری در سال‌های اخیر بوده است.
🔹
حالا آقامیری، رئیس کمیتۀ عمران شورای شهر تهران اعلام کرد با توجه به سنگین شدن بار ترافیکی معابر و با تصمیم پلیس راهور، مدیریت شهری اقدام به جمع‌آوری سنگ‌فرش، و تبدیل مسیرهای پیاده‌راه به سواره‌رو می‌کند تا گره‌های ترافیکی کاهش یابد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/farsna/455065" target="_blank">📅 02:58 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455064">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">یک کشته و ۱۲ مسموم درپی مصرف مشروبات الکلی در نیشابور
🔹
دانشگاه علوم پزشکی نیشابور: پنج‌شنبه شب ۱۳ نفر با علائم مسمومیت شدید ناشی از مصرف مشروبات الکلی به بیمارستان ۲۲ بهمن نیشابور مراجعه کردند.
🔹
روز بعد، ۷ نفر از آنان نیازمند دیالیز شدند که پس از انجام اقدامات اولیه انتقال بیماران در دستور کار قرار گرفت؛ متأسفانه باوجود تلاش‌های کادر درمان، یکی از این بیماران جان خود را از دست داد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/farsna/455064" target="_blank">📅 02:22 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455063">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cDrhPOFUMW9jxed8luGEw5_Pyr639fIE4kNkIuwKDpSEheNcqMkjslbslD209t40RWt9d3AqrffuLksX4j-x1p0Z9OY3tQcUnT8340WQD2O0OlZjWbQCUmjlKnFleg65q25smXWdexCcCK9Yv9A6xd9HM47oNVAoQ95bcP9ZgVjzOZCqLz2AtWsbE4X0JVCor7f2siJzxIKhKgBiVgY_ZIM9LrnonmXVQ9JGcyrUsWunQrhL0V0SUrPgpn-PHP2T1dvOp9Xr4Jlw_b0OkvcgkqPCq94f-Ie9d1XCd3F6HzdsTO83nJL109Jh4tfD7ywp1fjkL3cjkTXCxyKLc2rJTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خودروها روی دست خودروسازان ماند
🔹
پارکینگ خودروسازان پر شده است و قطعات تولیدی خریدار چندانی نداشته است.
🔹
مرکز پژوهش های مجلس می‌گوید که موجودی انبار خودروسازان، در زمستان ۱۴۰۴ روندی افزایشی یافته و حتی کاهش جزئی تقاضای فصلی نتوانسته سد انباشت کالا در انبار را بشکند.
🔹
در سه‌سال گذشته حجم کالاهای انبار مدام افزایش یافته و از ابتدای ۱۴۰۴ به شکلی بی‌سابقه، از میانگین پنج سال گذشته خود بیشتر شده که نتیجۀ آن قفل شدن نقدینگی در انبارها بوده است.
🔹
بخشی از این وضعیت مربوط به خودروهای ناقصی است که به دلیل کمبود قطعه در پارکینگ‌ها معطل مانده اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farsna/455063" target="_blank">📅 00:33 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455062">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hEyqFJn5U003H74fCPPqvwi3yUsd35C6Z3hCmw2hvrVDlQ9q9EvI91BMiv0zgLMwXxPscvaa9rl3lynHT-_KTSOCvByJRP4dQnrelH2TAXhtnMOlRonQeemiqMVvkF2cWuXUajwQs07_wbHl3yOPYjUS8PGJ_SkuelsErsz40eOk3aMP3eNUboHX3uAzJPbLSdTwZwiRwON6lZPDHelqBzt5_6OMaQQTJfyK0gZy9Jty0KKrYEvEgD-FtOPCrRJpTaQeFpzJa1i8ziG7FX2MW-Ys8Ax6Oj__McGZH29hMizxJaC-MdO-a0YGiq1_7E-V1UVAylTdKUtWn0IuHG-Dww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران دست چین را می‌گیرد
🔹
بخش بزرگی از کالاهای چین برای رسیدن به غرب آسیا، آفریقا و اروپا باید از آبراه‌هایی مانند تنگه مالاکا، اقیانوس هند، دریای سرخ و کانال سوئز عبور کند.
🔹
طولانی‌بودن مسیر، هزینه حمل و آسیب‌پذیری در برابر بحران‌های امنیتی، انسداد آبراه‌ها و افزایش نرخ بیمه را بالا می‌برد.
🔹
کالاهای چینی می‌توانند از مسیر آسیای مرکزی وارد ایران شوند و پس از عبور از شبکه ریلی یا جاده‌ای کشور، از مرز ترکیه به بازارهای این کشور و اروپا برسند.
🔹
در مسیر دیگر، کالا از بنادر جنوبی وارد ایران شده و سپس از طریق خطوط زمینی به عراق، ترکیه، قفقاز و آسیای مرکزی منتقل می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/farsna/455062" target="_blank">📅 00:20 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455061">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">حملۀ پهپادی اوکراین به شریان گازی روسیه-ترکیه-اروپا
🔹
بلغارستان ادعا کرد که صبح امروز یک پهباد اوکراینی به خط لولۀ ترانس-بالکان شلیک شده است.
🔹
خط لولۀ ترانس‌-بالکان گاز روسیه را از مسیر ترکیه به اروپا می‌رساند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/farsna/455061" target="_blank">📅 00:13 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455060">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9172d880e3.mp4?token=vInyLctBI9BGwINA_Z-RKRqWvCk1NfryNAXhTidm8CgdkwKHP8MBGAEHooSxA1_VQem07pxRXs70BpFLJBLzgNmV147nDY6dKTycBlM4ArAI0fiZZOEjjtu6EeebcVWXxtxzdtxHuEXpg_QHLkbaU_GibJdUSFNkAR6eoTiSEujYtf_l7X2zk_Xg--jgWTt2siWv9V8kd7YNms-93-SXDFMtgGFvFPBTctofa4NekHoBpvTGrN9vBLpx1yg7gkj4M3TCbPNvsxKOjyzLQ66sT8dZhtVbr_qU3-eeMIzaTnCVlkreYvjF_R3-20Hdlv6HYG-2wLrXOLUYtM_Sh1OMnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9172d880e3.mp4?token=vInyLctBI9BGwINA_Z-RKRqWvCk1NfryNAXhTidm8CgdkwKHP8MBGAEHooSxA1_VQem07pxRXs70BpFLJBLzgNmV147nDY6dKTycBlM4ArAI0fiZZOEjjtu6EeebcVWXxtxzdtxHuEXpg_QHLkbaU_GibJdUSFNkAR6eoTiSEujYtf_l7X2zk_Xg--jgWTt2siWv9V8kd7YNms-93-SXDFMtgGFvFPBTctofa4NekHoBpvTGrN9vBLpx1yg7gkj4M3TCbPNvsxKOjyzLQ66sT8dZhtVbr_qU3-eeMIzaTnCVlkreYvjF_R3-20Hdlv6HYG-2wLrXOLUYtM_Sh1OMnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایتی از حملهٔ سنگین دشمن صهیونیست به ارتفاعات علی الطاهر برای اشغال این منطقه با سو‌ءاستفاده از فرصت آتش‌بس
@Farsna</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/farsna/455060" target="_blank">📅 23:53 · 17 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
